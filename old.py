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
        inhers = self.node.find_all("Inheritance")
        for inher in inhers:
            self.parents.append(inher['baseType'])

        addinhers = self.node.find_all("AdditionalInheritance")
        for addinher in addinhers:
            self.parents.append(addinher['baseType'])

        self.printed = False


    def initialize(self, field, fn):
        str = ""
        str += self.settervalidation(field, fn)
        setfield = '        self.'+ fn + '_ = '
        str += setfield + 'kwargs.pop("' + fn + '"'
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

    def settervalidation(self, field, fn):
        str = ""
        inex = { 'minInclusive':" < ",
                 'maxInclusive':" > ",
                 'minExclusive':" <= ",
                 'maxExclusive':" >= "}
        str += '        if type('+fn+"_" + ') is not ' + field['type'] + ":" + """
            raise InvalidFieldTypeException()
"""
        for k,v in inex.items():
            try:
                str += """        if """ +fn+"_" + v + field[k] + ":" + """
                raise InvalidFieldValueException()
"""
            except KeyError:
                pass

        enumerations = field.find_all("enumeration")
        efound = 0
        for enum in enumerations:
            if efound == 0:
                str += "        if " + "'"+enum['value']+"'" + ' == ' + fn +"_:\n"
                str += "            pass\n"
                efound = 1
            else:
                str += "        elif " + "'"+enum['value']+"'" + ' == ' + fn +"_:\n"
                str += "            pass\n"
        if efound == 1:
            str += """        else:
            raise InvalidFieldValueException()
"""
        return str

    def setterbody(self, field, fn):
        str = ""
        str += '        self.'+ fn + '_ = ' + fn + "_\n"
        return str

    def setter(self, field, fn):
        str = ""
        if fn == 'addChildren':
            fn = 'add_children'
        elif fn == 'removeChildren':
            fn = 'remove_children'
        elif re.search(r"^remove", fn):
            fn = fn 
        elif re.search(r"^set_", fn):
            fn = fn 
        else:
            fn = 'set_'+ fn 
        str += '    def ' + fn + '(self, ' + fn +"_"
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
            str += "        super("+self.node['name']+", self)."+fn+"("+fn+"_)\n"
        str += self.settervalidation(field, fn)
        str += self.setterbody(field, fn)
        return str

    def getter(self, field, fn):
        str = "\n"
        str += '    def get_'+ fn + '(self):\n'
        str += '        if type(self.' +  fn + "_" + ') is not ' + field['type'] + ":" + """
            raise InvalidFieldTypeException()
"""
        str += '        return self.' + fn + "_\n\n"
        return str

    def settergetter(self, field, fn):
        str = ""
        str += self.setter(field, fn)
        str += self.getter(field, fn)
        return str

    def print(self):
        str = ""
        if self.printed:
            return str
        for parent in self.parents:
            try:
                str += classes[parent].print()
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

soup = BeautifulSoup(open("X3DObjectModel-3.3.xml"), "xml")

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
    code += v.print()

f = open("X3Dpackage.py", "w")
f.write(code)
f.close()
