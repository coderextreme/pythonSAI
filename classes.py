from bs4 import BeautifulSoup
import re

class ClassPrinter:
    def __init__(self, node, metaInfo):
        self.node = node
        self.parents = []
        inhers = self.node.find_all("Inheritance")
        for inher in inhers:
            self.parents.append(inher['baseType'])

        addinhers = self.node.find_all("AdditionalInheritance")
        for addinher in addinhers:
            self.parents.append(addinher['baseType'])

        self.componentInfo = self.node.find("componentInfo")
        self.metaInfo = metaInfo

        self.printed = False


    def print(self):
        str = ""
        if self.printed:
            return str
        for parent in self.parents:
            try:
                str += classes[parent].print()
            except:
                pass
        package = self.componentInfo['name']
        package = re.sub(r"-", "", package)
        superpackage = "sai"
        if self.metaInfo == "Object":
                superpackage = "java"
        str += self.node['name'] + self.metaInfo + " = autoclass('org.web3d.x3d."+superpackage+"."+package+"." + self.node['name'] + self.metaInfo + "')\n"
        self.printed = True
        return str

code = ""

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
    code += v.print()

f = open("X3Dautoclass.py", "w")
f.write('import os, sys\n')
f.write('CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))\n')
f.write('sys.path.append(os.path.dirname(CURRENT_DIR))\n')
f.write('from jnius import autoclass\n')
f.write(code)
f.close()
