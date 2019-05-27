import x3dpsail
X3D0 = x3dpsail.X3D()
X3D0.setProfile("Immersive")
X3D0.setVersion("3.3")
head1 = x3dpsail.head()
meta2 = x3dpsail.meta()
meta2.setName("title")
meta2.setContent("rubikFurnace.x3d")

head1.addMeta(meta2)
meta3 = x3dpsail.meta()
meta3.setName("creator")
meta3.setContent("John Carlson")

head1.addMeta(meta3)
meta4 = x3dpsail.meta()
meta4.setName("generator")
meta4.setContent("manual")

head1.addMeta(meta4)
meta5 = x3dpsail.meta()
meta5.setName("identifier")
meta5.setContent("https://coderextreme.net/X3DJSONLD/rubikFurnace.x3d")

head1.addMeta(meta5)
meta6 = x3dpsail.meta()
meta6.setName("description")
meta6.setContent("a green rubik cube")

head1.addMeta(meta6)

X3D0.setHead(head1)
Scene7 = x3dpsail.Scene()
NavigationInfo8 = x3dpsail.NavigationInfo()
NavigationInfo8.setType(["EXAMINE"])

Scene7.addChildren(NavigationInfo8)
Viewpoint9 = x3dpsail.Viewpoint()
Viewpoint9.setDescription("Rubiks Cube on Fire")
Viewpoint9.setPosition([0,0,12])

Scene7.addChildren(Viewpoint9)
ProtoDeclare10 = x3dpsail.ProtoDeclare()
ProtoDeclare10.setName("anyShape")
ProtoInterface11 = x3dpsail.ProtoInterface()
field12 = x3dpsail.field()
field12.setName("xtranslation")
field12.setAccessType("inputOutput")
field12.setType("SFVec3f")
field12.setValue("0 0 0")

ProtoInterface11.addField(field12)
field13 = x3dpsail.field()
field13.setName("myShape")
field13.setAccessType("inputOutput")
field13.setType("MFNode")
Shape14 = x3dpsail.Shape()
Sphere15 = x3dpsail.Sphere()

Shape14.setGeometry(Sphere15)
Appearance16 = x3dpsail.Appearance()
Material17 = x3dpsail.Material()
Material17.setDiffuseColor([1,1,1])

Appearance16.setMaterial(Material17)

Shape14.setAppearance(Appearance16)

field13.addChildren(Shape14)

ProtoInterface11.addField(field13)

ProtoDeclare10.setProtoInterface(ProtoInterface11)
ProtoBody18 = x3dpsail.ProtoBody()
Transform19 = x3dpsail.Transform()
IS20 = x3dpsail.IS()
connect21 = x3dpsail.connect()
connect21.setNodeField("translation")
connect21.setProtoField("xtranslation")

IS20.addConnect(connect21)
connect22 = x3dpsail.connect()
connect22.setNodeField("children")
connect22.setProtoField("myShape")

IS20.addConnect(connect22)

Transform19.setIS(IS20)

ProtoBody18.addChildren(Transform19)

ProtoDeclare10.setProtoBody(ProtoBody18)

Scene7.addChildren(ProtoDeclare10)
ProtoDeclare23 = x3dpsail.ProtoDeclare()
ProtoDeclare23.setName("three")
ProtoInterface24 = x3dpsail.ProtoInterface()
field25 = x3dpsail.field()
field25.setName("ytranslation")
field25.setAccessType("inputOutput")
field25.setType("SFVec3f")
field25.setValue("0 0 0")

ProtoInterface24.addField(field25)
field26 = x3dpsail.field()
field26.setName("myShape")
field26.setAccessType("inputOutput")
field26.setType("MFNode")
Shape27 = x3dpsail.Shape()
Sphere28 = x3dpsail.Sphere()

Shape27.setGeometry(Sphere28)
Appearance29 = x3dpsail.Appearance()
Material30 = x3dpsail.Material()
Material30.setDiffuseColor([1,1,1])

Appearance29.setMaterial(Material30)

Shape27.setAppearance(Appearance29)

field26.addChildren(Shape27)

ProtoInterface24.addField(field26)

ProtoDeclare23.setProtoInterface(ProtoInterface24)
ProtoBody31 = x3dpsail.ProtoBody()
Transform32 = x3dpsail.Transform()
IS33 = x3dpsail.IS()
connect34 = x3dpsail.connect()
connect34.setNodeField("translation")
connect34.setProtoField("ytranslation")

IS33.addConnect(connect34)

Transform32.setIS(IS33)
ProtoInstance35 = x3dpsail.ProtoInstance()
ProtoInstance35.setName("anyShape")
fieldValue36 = x3dpsail.fieldValue()
fieldValue36.setName("xtranslation")
fieldValue36.setValue("0 0 0")

ProtoInstance35.addFieldValue(fieldValue36)
IS37 = x3dpsail.IS()
connect38 = x3dpsail.connect()
connect38.setNodeField("myShape")
connect38.setProtoField("myShape")

IS37.addConnect(connect38)

ProtoInstance35.setIS(IS37)

Transform32.addChildren(ProtoInstance35)
ProtoInstance39 = x3dpsail.ProtoInstance()
ProtoInstance39.setName("anyShape")
fieldValue40 = x3dpsail.fieldValue()
fieldValue40.setName("xtranslation")
fieldValue40.setValue("2 0 0")

ProtoInstance39.addFieldValue(fieldValue40)
IS41 = x3dpsail.IS()
connect42 = x3dpsail.connect()
connect42.setNodeField("myShape")
connect42.setProtoField("myShape")

IS41.addConnect(connect42)

ProtoInstance39.setIS(IS41)

Transform32.addChildren(ProtoInstance39)
ProtoInstance43 = x3dpsail.ProtoInstance()
ProtoInstance43.setName("anyShape")
fieldValue44 = x3dpsail.fieldValue()
fieldValue44.setName("xtranslation")
fieldValue44.setValue("-2 0 0")

ProtoInstance43.addFieldValue(fieldValue44)
IS45 = x3dpsail.IS()
connect46 = x3dpsail.connect()
connect46.setNodeField("myShape")
connect46.setProtoField("myShape")

IS45.addConnect(connect46)

ProtoInstance43.setIS(IS45)

Transform32.addChildren(ProtoInstance43)

ProtoBody31.addChildren(Transform32)

ProtoDeclare23.setProtoBody(ProtoBody31)

Scene7.addChildren(ProtoDeclare23)
ProtoDeclare47 = x3dpsail.ProtoDeclare()
ProtoDeclare47.setName("nine")
ProtoInterface48 = x3dpsail.ProtoInterface()
field49 = x3dpsail.field()
field49.setName("ztranslation")
field49.setAccessType("inputOutput")
field49.setType("SFVec3f")
field49.setValue("0 0 0")

ProtoInterface48.addField(field49)
field50 = x3dpsail.field()
field50.setName("myShape")
field50.setAccessType("inputOutput")
field50.setType("MFNode")
Shape51 = x3dpsail.Shape()
Sphere52 = x3dpsail.Sphere()

Shape51.setGeometry(Sphere52)
Appearance53 = x3dpsail.Appearance()
Material54 = x3dpsail.Material()
Material54.setDiffuseColor([1,1,1])

Appearance53.setMaterial(Material54)

Shape51.setAppearance(Appearance53)

field50.addChildren(Shape51)

ProtoInterface48.addField(field50)

ProtoDeclare47.setProtoInterface(ProtoInterface48)
ProtoBody55 = x3dpsail.ProtoBody()
Transform56 = x3dpsail.Transform()
IS57 = x3dpsail.IS()
connect58 = x3dpsail.connect()
connect58.setNodeField("translation")
connect58.setProtoField("ztranslation")

IS57.addConnect(connect58)

Transform56.setIS(IS57)
ProtoInstance59 = x3dpsail.ProtoInstance()
ProtoInstance59.setName("three")
fieldValue60 = x3dpsail.fieldValue()
fieldValue60.setName("ytranslation")
fieldValue60.setValue("0 0 0")

ProtoInstance59.addFieldValue(fieldValue60)
IS61 = x3dpsail.IS()
connect62 = x3dpsail.connect()
connect62.setNodeField("myShape")
connect62.setProtoField("myShape")

IS61.addConnect(connect62)

ProtoInstance59.setIS(IS61)

Transform56.addChildren(ProtoInstance59)
ProtoInstance63 = x3dpsail.ProtoInstance()
ProtoInstance63.setName("three")
fieldValue64 = x3dpsail.fieldValue()
fieldValue64.setName("ytranslation")
fieldValue64.setValue("0 2 0")

ProtoInstance63.addFieldValue(fieldValue64)
IS65 = x3dpsail.IS()
connect66 = x3dpsail.connect()
connect66.setNodeField("myShape")
connect66.setProtoField("myShape")

IS65.addConnect(connect66)

ProtoInstance63.setIS(IS65)

Transform56.addChildren(ProtoInstance63)
ProtoInstance67 = x3dpsail.ProtoInstance()
ProtoInstance67.setName("three")
fieldValue68 = x3dpsail.fieldValue()
fieldValue68.setName("ytranslation")
fieldValue68.setValue("0 -2 0")

ProtoInstance67.addFieldValue(fieldValue68)
IS69 = x3dpsail.IS()
connect70 = x3dpsail.connect()
connect70.setNodeField("myShape")
connect70.setProtoField("myShape")

IS69.addConnect(connect70)

ProtoInstance67.setIS(IS69)

Transform56.addChildren(ProtoInstance67)

ProtoBody55.addChildren(Transform56)

ProtoDeclare47.setProtoBody(ProtoBody55)

Scene7.addChildren(ProtoDeclare47)
ProtoDeclare71 = x3dpsail.ProtoDeclare()
ProtoDeclare71.setName("twentyseven")
ProtoInterface72 = x3dpsail.ProtoInterface()
field73 = x3dpsail.field()
field73.setName("ttranslation")
field73.setAccessType("inputOutput")
field73.setType("SFVec3f")
field73.setValue("0 0 0")

ProtoInterface72.addField(field73)
field74 = x3dpsail.field()
field74.setName("myShape")
field74.setAccessType("inputOutput")
field74.setType("MFNode")
Shape75 = x3dpsail.Shape()
Sphere76 = x3dpsail.Sphere()

Shape75.setGeometry(Sphere76)
Appearance77 = x3dpsail.Appearance()
Material78 = x3dpsail.Material()
Material78.setDiffuseColor([1,1,1])

Appearance77.setMaterial(Material78)

Shape75.setAppearance(Appearance77)

field74.addChildren(Shape75)

ProtoInterface72.addField(field74)

ProtoDeclare71.setProtoInterface(ProtoInterface72)
ProtoBody79 = x3dpsail.ProtoBody()
Transform80 = x3dpsail.Transform()
IS81 = x3dpsail.IS()
connect82 = x3dpsail.connect()
connect82.setNodeField("translation")
connect82.setProtoField("ttranslation")

IS81.addConnect(connect82)

Transform80.setIS(IS81)
ProtoInstance83 = x3dpsail.ProtoInstance()
ProtoInstance83.setName("nine")
fieldValue84 = x3dpsail.fieldValue()
fieldValue84.setName("ztranslation")
fieldValue84.setValue("0 0 0")

ProtoInstance83.addFieldValue(fieldValue84)
IS85 = x3dpsail.IS()
connect86 = x3dpsail.connect()
connect86.setNodeField("myShape")
connect86.setProtoField("myShape")

IS85.addConnect(connect86)

ProtoInstance83.setIS(IS85)

Transform80.addChildren(ProtoInstance83)
ProtoInstance87 = x3dpsail.ProtoInstance()
ProtoInstance87.setName("nine")
fieldValue88 = x3dpsail.fieldValue()
fieldValue88.setName("ztranslation")
fieldValue88.setValue("0 0 2")

ProtoInstance87.addFieldValue(fieldValue88)
IS89 = x3dpsail.IS()
connect90 = x3dpsail.connect()
connect90.setNodeField("myShape")
connect90.setProtoField("myShape")

IS89.addConnect(connect90)

ProtoInstance87.setIS(IS89)

Transform80.addChildren(ProtoInstance87)
ProtoInstance91 = x3dpsail.ProtoInstance()
ProtoInstance91.setName("nine")
fieldValue92 = x3dpsail.fieldValue()
fieldValue92.setName("ztranslation")
fieldValue92.setValue("0 0 -2")

ProtoInstance91.addFieldValue(fieldValue92)
IS93 = x3dpsail.IS()
connect94 = x3dpsail.connect()
connect94.setNodeField("myShape")
connect94.setProtoField("myShape")

IS93.addConnect(connect94)

ProtoInstance91.setIS(IS93)

Transform80.addChildren(ProtoInstance91)

ProtoBody79.addChildren(Transform80)

ProtoDeclare71.setProtoBody(ProtoBody79)

Scene7.addChildren(ProtoDeclare71)
ProtoInstance95 = x3dpsail.ProtoInstance()
ProtoInstance95.setName("twentyseven")
fieldValue96 = x3dpsail.fieldValue()
fieldValue96.setName("ttranslation")
fieldValue96.setValue("0 0 0")

ProtoInstance95.addFieldValue(fieldValue96)
fieldValue97 = x3dpsail.fieldValue()
fieldValue97.setName("myShape")
Shape98 = x3dpsail.Shape()
Box99 = x3dpsail.Box()
Box99.setSize([1,1,1])

Shape98.setGeometry(Box99)
Appearance100 = x3dpsail.Appearance()
Material101 = x3dpsail.Material()
Material101.setDiffuseColor([0,1,0])

Appearance100.setMaterial(Material101)

Shape98.setAppearance(Appearance100)

fieldValue97.addChildren(Shape98)

ProtoInstance95.addFieldValue(fieldValue97)

Scene7.addChildren(ProtoInstance95)

X3D0.setScene(Scene7)
X3D0.toFileX3D("././rubikFurnace_RoundTrip.x3d")
