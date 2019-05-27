import x3dpsail
X3D0 = x3dpsail.X3D()
X3D0.setProfile("Immersive")
X3D0.setVersion("3.3")
head1 = x3dpsail.head()
meta2 = x3dpsail.meta()
meta2.setName("title")
meta2.setContent("abox.x3d")

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
meta5.setContent("https://coderextreme.net/X3DJSONLD/abox.x3d")

head1.addMeta(meta5)
meta6 = x3dpsail.meta()
meta6.setName("description")
meta6.setContent("a box")

head1.addMeta(meta6)

X3D0.setHead(head1)
Scene7 = x3dpsail.Scene()
ProtoDeclare8 = x3dpsail.ProtoDeclare()
ProtoDeclare8.setName("anyShape")
ProtoInterface9 = x3dpsail.ProtoInterface()
field10 = x3dpsail.field()
field10.setName("myShape")
field10.setAccessType("inputOutput")
field10.setType("MFNode")
Shape11 = x3dpsail.Shape()
Sphere12 = x3dpsail.Sphere()

Shape11.setGeometry(Sphere12)

field10.addChildren(Shape11)

ProtoInterface9.addField(field10)

ProtoDeclare8.setProtoInterface(ProtoInterface9)
ProtoBody13 = x3dpsail.ProtoBody()
Transform14 = x3dpsail.Transform()
IS15 = x3dpsail.IS()
connect16 = x3dpsail.connect()
connect16.setNodeField("children")
connect16.setProtoField("myShape")

IS15.addConnect(connect16)

Transform14.setIS(IS15)

ProtoBody13.addChildren(Transform14)

ProtoDeclare8.setProtoBody(ProtoBody13)

Scene7.addChildren(ProtoDeclare8)
ProtoDeclare17 = x3dpsail.ProtoDeclare()
ProtoDeclare17.setName("one")
ProtoInterface18 = x3dpsail.ProtoInterface()
field19 = x3dpsail.field()
field19.setName("myShape")
field19.setAccessType("inputOutput")
field19.setType("MFNode")
Shape20 = x3dpsail.Shape()
Cylinder21 = x3dpsail.Cylinder()

Shape20.setGeometry(Cylinder21)

field19.addChildren(Shape20)

ProtoInterface18.addField(field19)

ProtoDeclare17.setProtoInterface(ProtoInterface18)
ProtoBody22 = x3dpsail.ProtoBody()
Transform23 = x3dpsail.Transform()
ProtoInstance24 = x3dpsail.ProtoInstance()
ProtoInstance24.setName("anyShape")
IS25 = x3dpsail.IS()
connect26 = x3dpsail.connect()
connect26.setNodeField("myShape")
connect26.setProtoField("myShape")

IS25.addConnect(connect26)

ProtoInstance24.setIS(IS25)

Transform23.addChildren(ProtoInstance24)

ProtoBody22.addChildren(Transform23)

ProtoDeclare17.setProtoBody(ProtoBody22)

Scene7.addChildren(ProtoDeclare17)
ProtoInstance27 = x3dpsail.ProtoInstance()
ProtoInstance27.setName("one")
fieldValue28 = x3dpsail.fieldValue()
fieldValue28.setName("myShape")
Shape29 = x3dpsail.Shape()
Box30 = x3dpsail.Box()
Box30.setSize([140,140,140])

Shape29.setGeometry(Box30)

fieldValue28.addChildren(Shape29)

ProtoInstance27.addFieldValue(fieldValue28)

Scene7.addChildren(ProtoInstance27)

X3D0.setScene(Scene7)
X3D0.toFileX3D("././abox_RoundTrip.x3d")
