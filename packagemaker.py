import xml.etree.ElementTree
import re

class alone_field(object):
    def __init__(self, name, type):
        self.attrs = {}
        self.attrs['name'] = name
        self.attrs['type'] = type
        return None
    def get(self, field):
        return self.attrs[field]
    def __getitem__(self, field):
        return self.attrs[field]
    def iter(self, field):
        return []

class ClassPrinter(object):
    def __init__(self, node, name, meta = ""):
        self.__choice_table = \
        {
            "initializeOnly": self.initialize,
            "inputOnly": self.setter,
            "inputOutput": self.settergetter,
            "outputOnly": self.getter,
            None: self.getter
        }
        self.node = node
        self.name = name
        self.parents = []
        self.metaInfo = meta

        addinhers = self.node.iter("AdditionalInheritance")
        for addinher in addinhers:
            self.parents.append(addinher.get('baseType'))

        inhers = self.node.iter("Inheritance")
        for inher in inhers:
            self.parents.append(inher.get('baseType'))

        self.printed = False

    def getField(self, name):
        start = self.getStart(name)
        name = self.getName(name)
        if name == 'class':
            fld = name + "_"
        elif name == 'global':
            fld = name + "_"
        else:
            fld = name
        return fld

    def getName(self, name):
        start = self.getStart(name)
        if name == "address":
            pass
        elif re.search(r"_changed$", name):
            name = name
        elif re.search(r"^addSet", name):
            name = name[start+3:start+4].upper() + name[start+4:]
        elif re.search(r"^removeSet", name):
            name = name[start+3:start+4].upper() + name[start+4:]
        elif re.search(r"^getSet", name):
            name = name[start+3:start+4].upper() + name[start+4:]
        elif re.search(r"^add", name):
            name = name[start:start+1].upper() + name[start+1:]
        elif re.search(r"^remove", name):
            name = name[start:start+1].upper() + name[start+1:]
        elif re.search(r"^is", name):
            name = name[start:start+1].upper() + name[start+1:]
        elif re.search(r"^set_", name):
            name = name[start:start+1].upper() + name[start+1:]
        elif re.search(r"^set", name):
            name = name[start:start+1].upper() + name[start+1:]
        elif re.search(r"^get", name):
            name = name[start:start+1].upper() + name[start+1:]
        return name

    def getFunctionName(self, name):
        start = self.getStart(name)
        functionName = name[:start] + self.getName(name)
        return functionName

    def getStart(self, name):
        start = 0
        if name == "address":
            start = 0
        elif re.search(r"_changed$", name):
            start = 0
        elif re.search(r"^addSet", name):
            start = 3
        elif re.search(r"^removeSet", name):
            start = 6
        elif re.search(r"^getSet", name):
            start = 3
        elif re.search(r"^add", name):
            start = 3
        elif re.search(r"^remove", name):
            start = 6
        elif re.search(r"^is", name):
            start = 2
        elif re.search(r"^set_", name):
            start = 4
        elif re.search(r"^set", name):
            start = 3
        elif re.search(r"^get", name):
            start = 3
        return start


    def getDefault(self, field):
        str = ""
        try:
            if field.get('type') == 'SFString':
                str += '"'+field.get('default')+'"'
            elif re.search(r"\s", field.get('default')):
                str += '[' + ", ".join(field.get('default').split()) + ']'
            else:
                if field.get('default') == 'true':
                    field.set('default', 'True')
                if field.get('default') == 'false':
                    field.set('default', 'False')
                if field.get('default') == 'NULL':
                    field.set('default', 'None')
                str += field.get('default')
        except:
            if field.get('type').startswith("MF") or field.get('type') == "SFColor" or field.get('type') == "SFVec2f" or field.get('type') == "SFVec3f":
                str += "[]"
            else:
                str += "None"
        return str


    def initialize(self, field, name):
        str = ""
        fld = self.getField(name)
        str += self.recoverInit(field, fld)
        str += self.settervalidate(field, "self."+fld)
        str += self.setter(field, name)
        return str

    def settervalidate(self, field, fld):
        str = ""
        rel = { 'minInclusive':" < ",
                 'maxInclusive':" > ",
                 'minExclusive':" <= ",
                 'maxExclusive':" >= "}
        for k,v in rel.items():
            try:
                if field.get('type').startswith("MF") or field.get('type') == "SFColor" or field.get('type') == "SFVec2f" or field.get('type') == "SFVec3f":
                    str += "        if "+fld+" == None or len("+fld+") <= 0 or "+k[0:3] +"("+fld+") " + v + " " + field.get(k) + ":\n"
                    str += "            return None\n"
                else:
                    str += "        if "+fld+" == None or "+fld+" " + v + " " + field.get(k) + ":\n"
                    str += "            return None\n"
            
            except:
                pass

        try:
            if field.get('additionalEnumerationValuesAllowed') != "true":
                enumerations = field.iter("enumeration")
                efound = 0
                for enum in enumerations:
                    if efound == 0:
                        str += "        if " + "'"+enum.get('value')+"'" + ' == '+fld+':\n'
                        str += "            pass\n"
                        efound = 1
                    else:
                        str += "        elif " + "'"+enum.get('value')+"'" + ' == '+fld+':\n'
                        str += "            pass\n"
                if efound == 1:
                    str +=     "        else:\n"
                    str +=     "            return None\n"
        except KeyError:
            pass
        return str

    def recoverInit(self, field, fld):
        str = ""
        str += '        self.'+fld+' = ' + self.getDefault(field) + "\n"
        str += '        if not self.'+fld+':\n'
        str += '            self.'+fld+' = ' + 'kwargs.pop("' + fld + '", ' + self.getDefault(field) + ")\n"
        return str

    def setter(self, field, name):
        str = ""
        fld = self.getField(name)

        functionName = self.getFunctionName("set"+name)
        str += '    def ' + functionName +'(self, ' + fld +' = ' + self.getDefault(field) +  "):\n"
        str += self.settervalidate(field, fld)
        str += "        try:\n"
        str += "            super()." + functionName +'(' + fld +")\n"
        str += "        except AttributeError:\n"
        str += "           pass\n"
        str += '        self.'+fld+' = '+fld+"\n"
        str += "        return self\n"

#        functionName = self.getFunctionName("set_"+name)
#        str += '    def ' + functionName +'(self, ' + fld +' = ' + self.getDefault(field) +  "):\n"
#        str += self.settervalidate(field, fld)
#        str += "        try:\n"
#        str += "            super()." + functionName + '(' + fld +")\n"
#        str += "        except AttributeError:\n"
#        str += "           pass\n"
#        str += '        self.'+fld+' = '+fld+"\n"
#        str += "        return self\n"

        functionName = self.getFunctionName("add"+name)
        str += '    def ' + functionName +'(self, ' + fld +' = ' + self.getDefault(field) +  "):\n"
        str += self.settervalidate(field, fld)
        str += '        if not isinstance('+fld+', list):\n'
        str += '            '+fld+' = ['+fld+']\n'
        str += '            self.'+fld+' = []\n'
        str += '            self.'+fld+' = self.'+fld+' + '+fld+'\n'
        str += "        return self\n"

        functionName = self.getFunctionName("addSet"+name)
        str += '    def ' + functionName +'(self, ' + fld +' = ' + self.getDefault(field) +  "):\n"
        str += self.settervalidate(field, fld)
        str += '        if not isinstance('+fld+', list):\n'
        str += '            '+fld+' = ['+fld+']\n'
        str += '            self.'+fld+' = []\n'
        str += '            self.'+fld+' = self.'+fld+' + '+fld+'\n'
        str += "        return self\n"
        return str

    def getter(self, field, name):
        str = ""
        fld = self.getField(name)

        functionName = self.getFunctionName("removeSet"+name)
        str += '    def ' + functionName +'(self, '+fld+"):\n"
        str += '        self.'+fld+' = [x for x in self.'+fld+' if x not in '+fld+']'+"\n"
        str += '        return self.' + fld + "\n"

        functionName = self.getFunctionName("remove"+name)
        str += '    def ' + functionName +'(self, '+fld+"):\n"
        str += '        self.'+fld+' = [x for x in self.'+fld+' if x not in '+fld+']'+"\n"
        str += '        return self.' + fld + "\n"

        if field.get('type') == 'SFBool':
            functionName = self.getFunctionName("is"+name)
            str += '    def '+ functionName + '(self, ' + fld +' = ' + self.getDefault(field) +  "):\n"
            str += '        return self.' + fld + "\n"
        else:
            functionName = self.getFunctionName("get"+name)
            str += '    def '+ functionName + '(self, ' + fld +' = ' + self.getDefault(field) +  "):\n"
            str += '        return self.' + fld + "\n"

            functionName = self.getFunctionName(name+"_changed")
            str += '    def '+ functionName + '(self, ' + fld +' = ' + self.getDefault(field) +  "):\n"
            str += '        return self.' + fld + "\n"

            functionName = self.getFunctionName("getSet"+name)
            str += '    def '+ functionName + '(self, ' + fld +' = ' + self.getDefault(field) +  "):\n"
            str += '        return self.' + fld + "\n"

        return str

    def settergetter(self, field, name):
        str = ""
        str += self.setter(field, name)
        str += self.getter(field, name)
        return str

    def processField(self, field):
        name = field.get('name')
        name = re.sub(r"-", "_", name)
        name = re.sub(r":", "_", name)
        return name


    def printClass(self):
        str = ""
        if self.printed:
            return str
        for parent in self.parents:
            try:
                str += classes[parent].printClass()
            except:
                pass
        str += 'class ' + self.name + self.metaInfo
        strjoin = ", ".join(self.parents)
        if strjoin != "" and not strjoin.startswith("xs:") and strjoin != "SFString":
            str += "("+strjoin+")"
        else:
            str += "(object)"
        str += ":\n"
        str += "    def __init__(self, **kwargs):\n"
            
        if self.name == "X3D" or self.name == "meta" or self.name == "head":
            str += "        pass\n"
        else:
            if strjoin == "":
                str += "        super("+ self.name + self.metaInfo + ", self)."+"__init__()\n"
            else:
                str += "        super("+ self.name + self.metaInfo + ", self)."+"__init__(**kwargs)\n"

        fields = self.node.iter("field")

        for field in fields:
            name = self.processField(field)
            str += self.__choice_table['initializeOnly'](field, name)
        if not re.search(r"^SF", self.name) and not re.search(r"^MF", self.name):
            field = alone_field("comments", '#comment')
            name = self.processField(field)
            str += self.__choice_table['inputOnly'](field, name)
        if self.name == "ComposedShader":
            field = alone_field("sourceCode", '#cdata')
            name = self.processField(field)
            str += self.__choice_table['inputOnly'](field, name)
        if self.name == "Script":
            field = alone_field("sourceCode", '#cdata')
            name = self.processField(field)
            str += self.__choice_table['inputOnly'](field, name)

        for field in fields:
            name = self.processField(field)
            if field.get('accessType') != 'initializeOnly':
                str += self.__choice_table[field.get('accessType')](field, name)

        if self.name == "ComposedShader":
            field = alone_field("field", 'MFNode')
            name = self.processField(field)
            str += self.__choice_table['inputOutput'](field, name)
        if self.name == "head":
            field = alone_field("meta", 'MFNode')
            name = self.processField(field)
            str += self.__choice_table['inputOutput'](field, name)
        elif self.name == "Scene":
            field = alone_field("LayerSet", 'MFNode')
            name = self.processField(field)
            str += self.__choice_table['inputOutput'](field, name)
        elif self.name == "TouchSensor":
            field = alone_field("IS", 'MFNode')
            name = self.processField(field)
            str += self.__choice_table['inputOutput'](field, name)
        elif self.name == "NavigationInfo":
            field = alone_field("IS", 'MFNode')
            name = self.processField(field)
            str += self.__choice_table['inputOutput'](field, name)
        elif self.name == "Viewpoint":
            field = alone_field("IS", 'MFNode')
            name = self.processField(field)
            str += self.__choice_table['inputOutput'](field, name)
        elif self.name == "OrientationInterpolator":
            field = alone_field("IS", 'MFNode')
            name = self.processField(field)
            str += self.__choice_table['inputOutput'](field, name)
        elif self.name == "PositionInterpolator":
            field = alone_field("IS", 'MFNode')
            name = self.processField(field)
            str += self.__choice_table['inputOutput'](field, name)
        elif self.name == "DirectionalLight":
            field = alone_field("IS", 'MFNode')
            name = self.processField(field)
            str += self.__choice_table['inputOutput'](field, name)
        elif self.name == "Group":
            field = alone_field("IS", 'MFNode')
            name = self.processField(field)
            str += self.__choice_table['inputOutput'](field, name)
        elif self.name == "Transform":
            field = alone_field("IS", 'MFNode')
            name = self.processField(field)
            str += self.__choice_table['inputOutput'](field, name)
        elif self.name == "Shape":
            field = alone_field("IS", 'MFNode')
            name = self.processField(field)
            str += self.__choice_table['inputOutput'](field, name)
        elif self.name == "Material":
            field = alone_field("IS", 'MFNode')
            name = self.processField(field)
            str += self.__choice_table['inputOutput'](field, name)
        elif self.name == "Script":
            field = alone_field("IS", 'MFNode')
            name = self.processField(field)
            str += self.__choice_table['inputOutput'](field, name)
            field = alone_field("field", 'MFNode')
            name = self.processField(field)
            str += self.__choice_table['inputOutput'](field, name)
        elif self.name == "ProtoInstance":
            field = alone_field("IS", 'MFNode')
            name = self.processField(field)
            str += self.__choice_table['inputOutput'](field, name)
        elif self.name == "ShaderPart":
            field = alone_field("IS", 'MFNode')
            name = self.processField(field)
            str += self.__choice_table['inputOutput'](field, name)
        str += '\n\n'
        self.printed = True
        return str

code = ""

soup = xml.etree.ElementTree.parse(open("X3dUnifiedObjectModel-4.0.xml")).getroot()

classes = {}

ants = soup.iter("AbstractNodeType")
for ant in ants:
    classes[ant.get('name')] = ClassPrinter(ant, ant.get('name'))

aots = soup.iter("AbstractObjectType")
for aot in aots:
    classes[aot.get('name')] = ClassPrinter(aot, aot.get('name'))

cns = soup.iter("ConcreteNode")
for cn in cns:
    classes[cn.get('name')] = ClassPrinter(cn, cn.get('name'), "")

sts = soup.iter("Statement")
for st in sts:
    classes[st.get('name')] = ClassPrinter(st, st.get('name'), "")

fts = soup.iter("FieldType")
for ft in fts:
    classes[ft.get('type')] = ClassPrinter(ft, ft.get('type'), "")

for k,v in classes.items():
    code += v.printClass()

f = open("X3Dpackage.py", "w")
f.write(code)
f.close()
