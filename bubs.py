import x3dpsail as x3d
X3D0 = x3d.X3D()
X3D0.setProfile("Immersive")
X3D0.setVersion("3.3")
head1 = x3d.head()
meta2 = x3d.meta()
meta2.setName("title")
meta2.setContent("bubs.x3d")

head1.addMeta(meta2)
meta3 = x3d.meta()
meta3.setName("creator")
meta3.setContent("John Carlson")

head1.addMeta(meta3)
meta4 = x3d.meta()
meta4.setName("description")
meta4.setContent("Tour around a prismatic sphere")

head1.addMeta(meta4)
meta5 = x3d.meta()
meta5.setName("generator")
meta5.setContent("X3D-Edit, https://savage.nps.edu/X3D-Edit")

head1.addMeta(meta5)
meta6 = x3d.meta()
meta6.setName("identifier")
meta6.setContent("https://coderextreme.net/X3DJSONLD/bubs.x3d")

head1.addMeta(meta6)

X3D0.setHead(head1)
Scene7 = x3d.Scene()
NavigationInfo8 = x3d.NavigationInfo()
NavigationInfo8.setType(["EXAMINE"])

Scene7.addChildren(NavigationInfo8)
Viewpoint9 = x3d.Viewpoint()
Viewpoint9.setPosition([0,0,4])
Viewpoint9.setOrientation([1,0,0,0])
Viewpoint9.setDescription("Bubbles in action")

Scene7.addChildren(Viewpoint9)
Background10 = x3d.Background()
Background10.setBackUrl(["../resources/images/BK.png","https://coderextreme.net/X3DJSONLD/images/BK.png"])
Background10.setBottomUrl(["../resources/images/BT.png","https://coderextreme.net/X3DJSONLD/images/BT.png"])
Background10.setFrontUrl(["../resources/images/FR.png","https://coderextreme.net/X3DJSONLD/images/FR.png"])
Background10.setLeftUrl(["../resources/images/LF.png","https://coderextreme.net/X3DJSONLD/images/LF.png"])
Background10.setRightUrl(["../resources/images/RT.png","https://coderextreme.net/X3DJSONLD/images/RT.png"])
Background10.setTopUrl(["../resources/images/TP.png","https://coderextreme.net/X3DJSONLD/images/TP.png"])

Scene7.addChildren(Background10)
ProtoDeclare11 = x3d.ProtoDeclare()
ProtoDeclare11.setName("Bubble")
ProtoBody12 = x3d.ProtoBody()
Transform13 = x3d.Transform()
Transform13.setDEF("transform")
Shape14 = x3d.Shape()
Sphere15 = x3d.Sphere()
Sphere15.setRadius(0.25)

Shape14.setGeometry(Sphere15)
Appearance16 = x3d.Appearance()
Material17 = x3d.Material()
Material17.setDiffuseColor([1,0,0])
Material17.setTransparency(0.2)

Appearance16.setMaterial(Material17)

Shape14.setAppearance(Appearance16)

Transform13.addChildren(Shape14)
Script18 = x3d.Script()
Script18.setDEF("bounce")
field19 = x3d.field()
field19.setName("scale")
field19.setAccessType("inputOutput")
field19.setType("SFVec3f")
field19.setValue("1 1 1")

Script18.addField(field19)
field20 = x3d.field()
field20.setName("translation")
field20.setAccessType("inputOutput")
field20.setType("SFVec3f")
field20.setValue("0 0 0")

Script18.addField(field20)
field21 = x3d.field()
field21.setName("velocity")
field21.setAccessType("inputOutput")
field21.setType("SFVec3f")
field21.setValue("0 0 0")

Script18.addField(field21)
field22 = x3d.field()
field22.setName("scalvel")
field22.setAccessType("inputOutput")
field22.setType("SFVec3f")
field22.setValue("0 0 0")

Script18.addField(field22)
field23 = x3d.field()
field23.setName("set_fraction")
field23.setAccessType("inputOnly")
field23.setType("SFFloat")

Script18.addField(field23)

Script18.setSourceCode('''ecmascript:\n"+
"function initialize() {\n"+
"    velocity = new SFVec3f(Math.random() * 0.25 - 0.125, Math.random() * 0.25 - 0.125, Math.random() * 0.25 - 0.125);\n"+
"\n"+
"    scalvel = new SFVec3f(Math.random() * 0.4, Math.random() * 0.4, Math.random() * 0.4);\n"+
"}\n"+
"\n"+
"function set_fraction(value) {\n"+
"    translation = new SFVec3f(	translation.x + velocity.x, translation.y + velocity.y, translation.z + velocity.z);\n"+
"    scale = new SFVec3f(scale.x + scalvel.x, scale.y + scalvel.y, scale.z + scalvel.z);\n"+
"    // if you get to far away or too big, explode\n"+
"    if ( Math.abs(translation.x) > 256) {\n"+
"	translation.x = 0;\n"+
"	initialize();\n"+
"    }\n"+
"    if ( Math.abs(translation.y) > 256) {\n"+
"	translation.y = 0;\n"+
"	initialize();\n"+
"    }\n"+
"    if ( Math.abs(translation.z) > 256) {\n"+
"	translation.z = 0;\n"+
"	initialize();\n"+
"    }\n"+
"    if (Math.abs(scale.x) > 20) {\n"+
"	scale.x = scale.x/20;\n"+
"	translation.x = 0;\n"+
"	initialize();\n"+
"    }\n"+
"    if (Math.abs(scale.y) > 20) {\n"+
"	scale.y = scale.y/20;\n"+
"	translation.y = 0;\n"+
"	initialize();\n"+
"    }\n"+
"    if (Math.abs(scale.z) > 20) {\n"+
"	scale.z = scale.z/20;\n"+
"	translation.z = 0;\n"+
"	initialize();\n"+
"    }\n"+
"}''')

Transform13.addChildren(Script18)
TimeSensor24 = x3d.TimeSensor()
TimeSensor24.setDEF("bubbleClock")
TimeSensor24.setCycleInterval(10)
TimeSensor24.setLoop(True)

Transform13.addChildren(TimeSensor24)
ROUTE25 = x3d.ROUTE()
ROUTE25.setFromNode("bounce")
ROUTE25.setFromField("translation_changed")
ROUTE25.setToNode("transform")
ROUTE25.setToField("set_translation")

Transform13.addChildren(ROUTE25)
ROUTE26 = x3d.ROUTE()
ROUTE26.setFromNode("bounce")
ROUTE26.setFromField("scale_changed")
ROUTE26.setToNode("transform")
ROUTE26.setToField("set_scale")

Transform13.addChildren(ROUTE26)
ROUTE27 = x3d.ROUTE()
ROUTE27.setFromNode("bubbleClock")
ROUTE27.setFromField("fraction_changed")
ROUTE27.setToNode("bounce")
ROUTE27.setToField("set_fraction")

Transform13.addChildren(ROUTE27)

ProtoBody12.addChildren(Transform13)

ProtoDeclare11.setProtoBody(ProtoBody12)

Scene7.addChildren(ProtoDeclare11)
ProtoInstance28 = x3d.ProtoInstance()
ProtoInstance28.setName("Bubble")
ProtoInstance28.setDEF("bubbleA")

Scene7.addChildren(ProtoInstance28)
ProtoInstance29 = x3d.ProtoInstance()
ProtoInstance29.setName("Bubble")
ProtoInstance29.setDEF("bubbleB")

Scene7.addChildren(ProtoInstance29)
ProtoInstance30 = x3d.ProtoInstance()
ProtoInstance30.setName("Bubble")
ProtoInstance30.setDEF("bubbleC")

Scene7.addChildren(ProtoInstance30)
ProtoInstance31 = x3d.ProtoInstance()
ProtoInstance31.setName("Bubble")
ProtoInstance31.setDEF("bubbleD")

Scene7.addChildren(ProtoInstance31)

X3D0.setScene(Scene7)
X3D0.toFileX3D("././bubs_RoundTrip.x3d")
