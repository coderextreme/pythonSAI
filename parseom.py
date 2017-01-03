from bs4 import BeautifulSoup
import re

class ClassPrinter:
    def __init__(self, node, metaInfo):
        self.node = node
        self.parents = []
        self.children = []
        inhers = self.node.find_all("Inheritance")
        for inher in inhers:
            self.parents.append(inher['baseType'])

        addinhers = self.node.find_all("AdditionalInheritance")
        for addinher in addinhers:
            self.parents.append(addinher['baseType'])

        self.componentInfo = self.node.find("componentInfo")
        self.metaInfo = metaInfo


        self.printed = False

    def findChildren(self):
        inhers = self.node.find_all("Inheritance")
        for inher in inhers:
            classes[inher['baseType']].children.append(self.node["name"])

        addinhers = self.node.find_all("AdditionalInheritance")
        for addinher in addinhers:
            classes[addinher['baseType']].children.append(self.node["name"])

    def listChildren(self, fieldName, fieldType):
            str = ""
            if fieldName == "addChildren" or fieldName == "removeChildren":
                return str
            if fieldType == "SFNode":
                str += '\t"' + self.node["name"] + '" : "set' + fieldName[:1].upper() + fieldName[1:] + '",\n';
            else:
                str += '\t"' + self.node["name"] + '" : "add' + fieldName[:1].upper() + fieldName[1:] + '",\n';
            for child in self.children:
               str += classes[child].listChildren(fieldName, fieldType)
            return str;

    def print(self):
        str = ""
        if self.printed:
            return str
        for parent in self.parents:
            try:
                str += classes[parent].print()
            except:
                pass
        str += '"'+self.node['name']+'" : {\n'
        fields = self.node.find_all("field")
        for field in fields:
            if field["type"] == "MFNode" or field["type"] == "SFNode":
                acnts = field["acceptableNodeTypes"].split("|")
                for acnt in acnts:
                    str += classes[acnt].listChildren(field["name"], field["type"])
        str += '},\n'
        self.printed = True
        return str

code = "module.exports = {"

soup = BeautifulSoup(open("X3DObjectModel-3.3.xml"), "xml")

classes = {}

ants = soup.find_all("AbstractNodeType")
for ant in ants:
    classes[ant['name']] = ClassPrinter(ant, "")

aots = soup.find_all("AbstractObjectType")
for aot in aots:
    classes[aot['name']] = ClassPrinter(aot, "")

cns = soup.find_all("ConcreteNode")
for cn in cns:
    classes[cn['name']] = ClassPrinter(cn, "Object")

sts = soup.find_all("Statement")
for st in sts:
    classes[st['name']] = ClassPrinter(st, "Object")

for k,v in classes.items():
    v.findChildren()

for k,v in classes.items():
    code += v.print()

code += "};"

f = open("mapToMethod.js", "w")
f.write(code)
f.close()
