import x3dpsail
X3D0 = x3dpsail.X3D()
X3D0.setProfile("Immersive")
X3D0.setVersion("3.3")
head1 = x3dpsail.head()
meta2 = x3dpsail.meta()
meta2.setName("title")
meta2.setContent("rubikOnFire.x3d")

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
meta5.setContent("https://coderextreme.net/X3DJSONLD/rubikOnFire.x3d")

head1.addMeta(meta5)
meta6 = x3dpsail.meta()
meta6.setName("description")
meta6.setContent("a white rubik cube")

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
field13.setType("SFNode")
Sphere14 = x3dpsail.Sphere()

field13.addChildren(Sphere14)

ProtoInterface11.addField(field13)

ProtoDeclare10.setProtoInterface(ProtoInterface11)
ProtoBody15 = x3dpsail.ProtoBody()
Transform16 = x3dpsail.Transform()
IS17 = x3dpsail.IS()
connect18 = x3dpsail.connect()
connect18.setNodeField("translation")
connect18.setProtoField("xtranslation")

IS17.addConnect(connect18)

Transform16.setIS(IS17)
Shape19 = x3dpsail.Shape()
IS20 = x3dpsail.IS()
connect21 = x3dpsail.connect()
connect21.setNodeField("geometry")
connect21.setProtoField("myShape")

IS20.addConnect(connect21)

Shape19.setIS(IS20)
Appearance22 = x3dpsail.Appearance()
Material23 = x3dpsail.Material()
Material23.setDiffuseColor([1,1,1])

Appearance22.setMaterial(Material23)

Shape19.setAppearance(Appearance22)

Transform16.addChildren(Shape19)

ProtoBody15.addChildren(Transform16)

ProtoDeclare10.setProtoBody(ProtoBody15)

Scene7.addChildren(ProtoDeclare10)
ProtoDeclare24 = x3dpsail.ProtoDeclare()
ProtoDeclare24.setName("three")
ProtoInterface25 = x3dpsail.ProtoInterface()
field26 = x3dpsail.field()
field26.setName("ytranslation")
field26.setAccessType("inputOutput")
field26.setType("SFVec3f")
field26.setValue("0 0 0")

ProtoInterface25.addField(field26)
field27 = x3dpsail.field()
field27.setName("myShape")
field27.setAccessType("inputOutput")
field27.setType("SFNode")
Sphere28 = x3dpsail.Sphere()

field27.addChildren(Sphere28)

ProtoInterface25.addField(field27)

ProtoDeclare24.setProtoInterface(ProtoInterface25)
ProtoBody29 = x3dpsail.ProtoBody()
Transform30 = x3dpsail.Transform()
IS31 = x3dpsail.IS()
connect32 = x3dpsail.connect()
connect32.setNodeField("translation")
connect32.setProtoField("ytranslation")

IS31.addConnect(connect32)

Transform30.setIS(IS31)
ProtoInstance33 = x3dpsail.ProtoInstance()
ProtoInstance33.setName("anyShape")
fieldValue34 = x3dpsail.fieldValue()
fieldValue34.setName("xtranslation")
fieldValue34.setValue("0 0 0")

ProtoInstance33.addFieldValue(fieldValue34)
IS35 = x3dpsail.IS()
connect36 = x3dpsail.connect()
connect36.setNodeField("myShape")
connect36.setProtoField("myShape")

IS35.addConnect(connect36)

ProtoInstance33.setIS(IS35)

Transform30.addChildren(ProtoInstance33)
ProtoInstance37 = x3dpsail.ProtoInstance()
ProtoInstance37.setName("anyShape")
fieldValue38 = x3dpsail.fieldValue()
fieldValue38.setName("xtranslation")
fieldValue38.setValue("2 0 0")

ProtoInstance37.addFieldValue(fieldValue38)
IS39 = x3dpsail.IS()
connect40 = x3dpsail.connect()
connect40.setNodeField("myShape")
connect40.setProtoField("myShape")

IS39.addConnect(connect40)

ProtoInstance37.setIS(IS39)

Transform30.addChildren(ProtoInstance37)
ProtoInstance41 = x3dpsail.ProtoInstance()
ProtoInstance41.setName("anyShape")
fieldValue42 = x3dpsail.fieldValue()
fieldValue42.setName("xtranslation")
fieldValue42.setValue("-2 0 0")

ProtoInstance41.addFieldValue(fieldValue42)
IS43 = x3dpsail.IS()
connect44 = x3dpsail.connect()
connect44.setNodeField("myShape")
connect44.setProtoField("myShape")

IS43.addConnect(connect44)

ProtoInstance41.setIS(IS43)

Transform30.addChildren(ProtoInstance41)

ProtoBody29.addChildren(Transform30)

ProtoDeclare24.setProtoBody(ProtoBody29)

Scene7.addChildren(ProtoDeclare24)
ProtoDeclare45 = x3dpsail.ProtoDeclare()
ProtoDeclare45.setName("nine")
ProtoInterface46 = x3dpsail.ProtoInterface()
field47 = x3dpsail.field()
field47.setName("ztranslation")
field47.setAccessType("inputOutput")
field47.setType("SFVec3f")
field47.setValue("0 0 0")

ProtoInterface46.addField(field47)
field48 = x3dpsail.field()
field48.setName("myShape")
field48.setAccessType("inputOutput")
field48.setType("SFNode")
Sphere49 = x3dpsail.Sphere()

field48.addChildren(Sphere49)

ProtoInterface46.addField(field48)

ProtoDeclare45.setProtoInterface(ProtoInterface46)
ProtoBody50 = x3dpsail.ProtoBody()
Transform51 = x3dpsail.Transform()
IS52 = x3dpsail.IS()
connect53 = x3dpsail.connect()
connect53.setNodeField("translation")
connect53.setProtoField("ztranslation")

IS52.addConnect(connect53)

Transform51.setIS(IS52)
ProtoInstance54 = x3dpsail.ProtoInstance()
ProtoInstance54.setName("three")
fieldValue55 = x3dpsail.fieldValue()
fieldValue55.setName("ytranslation")
fieldValue55.setValue("0 0 0")

ProtoInstance54.addFieldValue(fieldValue55)
IS56 = x3dpsail.IS()
connect57 = x3dpsail.connect()
connect57.setNodeField("myShape")
connect57.setProtoField("myShape")

IS56.addConnect(connect57)

ProtoInstance54.setIS(IS56)

Transform51.addChildren(ProtoInstance54)
ProtoInstance58 = x3dpsail.ProtoInstance()
ProtoInstance58.setName("three")
fieldValue59 = x3dpsail.fieldValue()
fieldValue59.setName("ytranslation")
fieldValue59.setValue("0 2 0")

ProtoInstance58.addFieldValue(fieldValue59)
IS60 = x3dpsail.IS()
connect61 = x3dpsail.connect()
connect61.setNodeField("myShape")
connect61.setProtoField("myShape")

IS60.addConnect(connect61)

ProtoInstance58.setIS(IS60)

Transform51.addChildren(ProtoInstance58)
ProtoInstance62 = x3dpsail.ProtoInstance()
ProtoInstance62.setName("three")
fieldValue63 = x3dpsail.fieldValue()
fieldValue63.setName("ytranslation")
fieldValue63.setValue("0 -2 0")

ProtoInstance62.addFieldValue(fieldValue63)
IS64 = x3dpsail.IS()
connect65 = x3dpsail.connect()
connect65.setNodeField("myShape")
connect65.setProtoField("myShape")

IS64.addConnect(connect65)

ProtoInstance62.setIS(IS64)

Transform51.addChildren(ProtoInstance62)

ProtoBody50.addChildren(Transform51)

ProtoDeclare45.setProtoBody(ProtoBody50)

Scene7.addChildren(ProtoDeclare45)
ProtoDeclare66 = x3dpsail.ProtoDeclare()
ProtoDeclare66.setName("twentyseven")
ProtoInterface67 = x3dpsail.ProtoInterface()
field68 = x3dpsail.field()
field68.setName("ttranslation")
field68.setAccessType("inputOutput")
field68.setType("SFVec3f")
field68.setValue("0 0 0")

ProtoInterface67.addField(field68)
field69 = x3dpsail.field()
field69.setName("myShape")
field69.setAccessType("inputOutput")
field69.setType("SFNode")
Sphere70 = x3dpsail.Sphere()

field69.addChildren(Sphere70)

ProtoInterface67.addField(field69)

ProtoDeclare66.setProtoInterface(ProtoInterface67)
ProtoBody71 = x3dpsail.ProtoBody()
Transform72 = x3dpsail.Transform()
IS73 = x3dpsail.IS()
connect74 = x3dpsail.connect()
connect74.setNodeField("translation")
connect74.setProtoField("ttranslation")

IS73.addConnect(connect74)

Transform72.setIS(IS73)
ProtoInstance75 = x3dpsail.ProtoInstance()
ProtoInstance75.setName("nine")
fieldValue76 = x3dpsail.fieldValue()
fieldValue76.setName("ztranslation")
fieldValue76.setValue("0 0 0")

ProtoInstance75.addFieldValue(fieldValue76)
IS77 = x3dpsail.IS()
connect78 = x3dpsail.connect()
connect78.setNodeField("myShape")
connect78.setProtoField("myShape")

IS77.addConnect(connect78)

ProtoInstance75.setIS(IS77)

Transform72.addChildren(ProtoInstance75)
ProtoInstance79 = x3dpsail.ProtoInstance()
ProtoInstance79.setName("nine")
fieldValue80 = x3dpsail.fieldValue()
fieldValue80.setName("ztranslation")
fieldValue80.setValue("0 0 2")

ProtoInstance79.addFieldValue(fieldValue80)
IS81 = x3dpsail.IS()
connect82 = x3dpsail.connect()
connect82.setNodeField("myShape")
connect82.setProtoField("myShape")

IS81.addConnect(connect82)

ProtoInstance79.setIS(IS81)

Transform72.addChildren(ProtoInstance79)
ProtoInstance83 = x3dpsail.ProtoInstance()
ProtoInstance83.setName("nine")
fieldValue84 = x3dpsail.fieldValue()
fieldValue84.setName("ztranslation")
fieldValue84.setValue("0 0 -2")

ProtoInstance83.addFieldValue(fieldValue84)
IS85 = x3dpsail.IS()
connect86 = x3dpsail.connect()
connect86.setNodeField("myShape")
connect86.setProtoField("myShape")

IS85.addConnect(connect86)

ProtoInstance83.setIS(IS85)

Transform72.addChildren(ProtoInstance83)

ProtoBody71.addChildren(Transform72)

ProtoDeclare66.setProtoBody(ProtoBody71)

Scene7.addChildren(ProtoDeclare66)
ProtoInstance87 = x3dpsail.ProtoInstance()
ProtoInstance87.setName("twentyseven")
fieldValue88 = x3dpsail.fieldValue()
fieldValue88.setName("ttranslation")
fieldValue88.setValue("0 0 0")

ProtoInstance87.addFieldValue(fieldValue88)
fieldValue89 = x3dpsail.fieldValue()
fieldValue89.setName("myShape")
Box90 = x3dpsail.Box()
Box90.setSize([1,1,1])

fieldValue89.addChildren(Box90)

ProtoInstance87.addFieldValue(fieldValue89)

Scene7.addChildren(ProtoInstance87)

X3D0.setScene(Scene7)
X3D0.toFileX3D("././rubikOnFire_RoundTrip.x3d")
