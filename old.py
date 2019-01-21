from bs4 import BeautifulSoup
import re

class ClassPrinter:
    def __init__(self, node):
        self.__choice_table = \
        {
            "initializeOnly": self.initialize,
            "inputOnly": self.setter,
            "inputOutput": self.settergetter,
            "outputOnly": self.getter,
            None: self.getter
        }
        self.node = node
        self.parents = []

        addinhers = self.node.find_all("AdditionalInheritance")
        for addinher in addinhers:
            self.parents.append(addinher['baseType'])

        inhers = self.node.find_all("Inheritance")
        for inher in inhers:
            self.parents.append(inher['baseType'])

        self.printed = False


    def initialize(self, field, func):
        str = ""
        if re.search(r"^add", func):
            fld = func[3:]
        elif re.search(r"^remove", func):
            fld = func[6:]
        elif re.search(r"^is", func):
            fld = func[2:]
        elif re.search(r"^set", func):
            fld = func[3:]
        else:
            fld = func
        str += self.settervalidation(field, fld)
        setfield = '        self.'+ fld + '_ = '
        str += setfield + 'kwargs.pop("' + fld + '"'
        try:
            if field['type'] == 'SFString':
                str += ', "'+field['default']+'"'
            elif re.search(r"\s", field['default']):
                str += ', [' + ", ".join(field['default'].split()) + ']'
            else:
                if field['default'] == 'true':
                    field['default'] = 'True'
                if field['default'] == 'false':
                    field['default'] = 'False'
                if field['default'] == 'NULL':
                    field['default'] = 'None'
                str += ', '+field['default']
        except KeyError:
            pass
        str += ')\n'
        return str

    def settervalidation(self, field, fld):
        str = ""
        inex = { 'minInclusive':" < ",
                 'maxInclusive':" > ",
                 'minExclusive':" <= ",
                 'maxExclusive':" >= "}
        str += '        if type('+fld+"_" + ') is not ' + field['type'] + ":" + """
            raise InvalidFieldTypeException()
"""
        for k,v in inex.items():
            try:
                str += """        if """ +fld+"_" + v + field[k] + ":" + """
                raise InvalidFieldValueException()
"""
            except KeyError:
                pass

        enumerations = field.find_all("enumeration")
        efound = 0
        for enum in enumerations:
            if efound == 0:
                str += "        if " + "'"+enum['value']+"'" + ' == ' + fld +"_:\n"
                str += "            pass\n"
                efound = 1
            else:
                str += "        elif " + "'"+enum['value']+"'" + ' == ' + fld +"_:\n"
                str += "            pass\n"
        if efound == 1:
            str += """        else:
            raise InvalidFieldValueException()
"""
        return str

    def setterbody(self, field, fld):
        str = ""
        str += '        self.'+ fld + '_ = ' + fld + "_\n"
        return str

    def setter(self, field, func):
        str = ""
        if re.search(r"^add", func):
            fld = func[3:]
        elif re.search(r"^remove", func):
            fld = func[6:]
        elif re.search(r"^is", func):
            fld = func[2:]
            func = 'set' + func[2:]
        elif re.search(r"^set", func):
            fld = func[3:]
        else:
            fld = func
            func = 'set'+ func[:1].upper() + func[1:]
        str += '    def ' + func + '(self, ' + fld +"_"
        try:
            if field['type'] == 'SFString':
                str += ' = ' + '"'+field['default']+'"'
            elif re.search(r"\s", field['default']):
                str += ' = [' + ", ".join(field['default'].split()) + ']'
            else:
                if field['default'] == 'true':
                    field['default'] = 'True'
                if field['default'] == 'false':
                    field['default'] = 'False'
                if field['default'] == 'NULL':
                    field['default'] = 'None'
                str += ' = ' + field['default']
        except KeyError:
            pass
        str += "):\n"
        if self.parents != []:
            str += "        super("+self.node['name']+", self)."+func+"("+fld+"_)\n"
        str += self.settervalidation(field, fld)
        str += self.setterbody(field, fld)
        return str

    def getter(self, field, func):
        str = "\n"
        if re.search(r"^is", func):
            fld = func[2:]
            str += '    def is'+ func[2:] + '(self):\n'
        elif field['type'] == 'SFBool':
            fld = func
            str += '    def is'+ func[:1].upper() + func[1:] + '(self):\n'
        else:
            fld = func
            str += '    def get'+ func[:1].upper() + func[1:] + '(self):\n'
        str += '        if type(self.' +  fld + "_" + ') is not ' + field['type'] + ":" + """
            raise InvalidFieldTypeException()
"""
        str += '        return self.' + fld + "_\n\n"
        return str

    def settergetter(self, field, func):
        str = ""
        str += self.setter(field, func)
        str += self.getter(field, func)
        return str

    def printClass(self):
        str = ""
        if self.printed:
            return str
        for parent in self.parents:
            try:
                str += classes[parent].printClass()
            except:
                pass
        str += 'class ' + self.node['name'] + "("

        str += ", ".join(self.parents)
        str += "):\n"
        str += "    def __init__(self, **kwargs):\n"
        str += "        super()."+"__init__()\n"
        getsetstr = ""
        fields = self.node.find_all("field")
        for field in fields:
            fn = field['name']
            fn = re.sub(r"-", "_", fn)
            fn = re.sub(r":", "_", fn)
            if field['accessType'] == 'initializeOnly':
                str += self.__choice_table[field['accessType']](field, fn)
            else:
                getsetstr += self.__choice_table[field['accessType']](field, fn)
        str += '        return\n\n'
        str += getsetstr
        str += '    pass\n\n\n'
        self.printed = True
        return str

code = ""

code += """class InvalidFieldValueException (BaseException):
    def __init__(self):
        return

class InvalidFieldTypeException (BaseException):
    def __init__(self):
        return
"""

soup = BeautifulSoup(open("X3dUnifiedObjectModel-4.0.xml"), "xml")

classes = {}

ants = soup.find_all("AbstractNodeType")
for ant in ants:
    classes[ant['name']] = ClassPrinter(ant)

aots = soup.find_all("AbstractObjectType")
for aot in aots:
    classes[aot['name']] = ClassPrinter(aot)

cns = soup.find_all("ConcreteNode")
for cn in cns:
    classes[cn['name']] = ClassPrinter(cn)

sts = soup.find_all("Statement")
for st in sts:
    classes[st['name']] = ClassPrinter(st)

for k,v in classes.items():
    code += v.printClass()

f = open("X3Dpackage.py", "w")
f.write(code)
f.close()
