import x3dpsail
X3D0 = x3dpsail.X3D()
X3D0.setProfile("Immersive")
X3D0.setVersion("3.3")
head1 = x3dpsail.head()
meta2 = x3dpsail.meta()
meta2.setName("title")
meta2.setContent("pp3.x3d")

head1.addMeta(meta2)
meta3 = x3dpsail.meta()
meta3.setName("creator")
meta3.setContent("John Carlson")

head1.addMeta(meta3)
meta4 = x3dpsail.meta()
meta4.setName("translator")
meta4.setContent("John Carlson")

head1.addMeta(meta4)
meta5 = x3dpsail.meta()
meta5.setName("created")
meta5.setContent("5 May 2015")

head1.addMeta(meta5)
meta6 = x3dpsail.meta()
meta6.setName("modified")
meta6.setContent("05 May 2017")

head1.addMeta(meta6)
meta7 = x3dpsail.meta()
meta7.setName("description")
meta7.setContent("A process pipeline between three spheres (try typing on spheres and blue")

head1.addMeta(meta7)
meta8 = x3dpsail.meta()
meta8.setName("identifier")
meta8.setContent("https://coderextreme.net/x3d/pp3.x3d")

head1.addMeta(meta8)
meta9 = x3dpsail.meta()
meta9.setName("generator")
meta9.setContent("manual")

head1.addMeta(meta9)

X3D0.setHead(head1)
Scene10 = x3dpsail.Scene()
ProtoDeclare11 = x3dpsail.ProtoDeclare()
ProtoDeclare11.setName("Process")
ProtoBody12 = x3dpsail.ProtoBody()
Group13 = x3dpsail.Group()
#left
Transform14 = x3dpsail.Transform()
Transform14.setScale([0.5,0.5,0.5])
Shape15 = x3dpsail.Shape()
Appearance16 = x3dpsail.Appearance()
Material17 = x3dpsail.Material()
Material17.setDiffuseColor([0.7,1,0])
Material17.setTransparency(0.5)

Appearance16.setMaterial(Material17)

Shape15.setAppearance(Appearance16)
Extrusion18 = x3dpsail.Extrusion()
Extrusion18.setCreaseAngle(0.785)
Extrusion18.setCrossSection([1,0,0.92,-0.38,0.71,-0.71,0.38,-0.92,0,-1,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1,0,-0.92,0.38,-0.71,0.71,-0.38,0.92,0,1,0.38,0.92,0.71,0.71,0.92,0.38,1,0])
Extrusion18.setSpine([-2.5,0,0,-1.5,0,0])

Shape15.setGeometry(Extrusion18)

Transform14.addChildren(Shape15)
#<Transform translation=\"-2.5 0 0\"> <Shape> <Text DEF=\"LeftString\" string='\"l\"'/> </Shape> </Transform> <StringSensor DEF=\"LeftSensor\" enabled=\"false\"/> <TouchSensor DEF=\"LeftTouch\" enabled=\"true\"/>

Group13.addChildren(Transform14)
#right
Transform19 = x3dpsail.Transform()
Transform19.setScale([0.5,0.5,0.5])
Shape20 = x3dpsail.Shape()
Appearance21 = x3dpsail.Appearance()
Material22 = x3dpsail.Material()
Material22.setDiffuseColor([0,0.7,1])
Material22.setTransparency(0.5)

Appearance21.setMaterial(Material22)

Shape20.setAppearance(Appearance21)
Extrusion23 = x3dpsail.Extrusion()
Extrusion23.setCreaseAngle(0.785)
Extrusion23.setCrossSection([1,0,0.92,-0.38,0.71,-0.71,0.38,-0.92,0,-1,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1,0,-0.92,0.38,-0.71,0.71,-0.38,0.92,0,1,0.38,0.92,0.71,0.71,0.92,0.38,1,0])
Extrusion23.setSpine([1.5,0,0,2.5,0,0])

Shape20.setGeometry(Extrusion23)

Transform19.addChildren(Shape20)
Transform24 = x3dpsail.Transform()
Transform24.setTranslation([2,0,0])
Shape25 = x3dpsail.Shape()
Appearance26 = x3dpsail.Appearance()
Material27 = x3dpsail.Material()
Material27.setDEF("MaterialLightBlue")
Material27.setDiffuseColor([1,1,1])

Appearance26.setMaterial(Material27)

Shape25.setAppearance(Appearance26)
Text28 = x3dpsail.Text()
Text28.setDEF("RightString")
Text28.setString(["r"])

Shape25.setGeometry(Text28)

Transform24.addChildren(Shape25)

Transform19.addChildren(Transform24)
StringSensor29 = x3dpsail.StringSensor()
StringSensor29.setDEF("RightSensor")
StringSensor29.setEnabled(False)

Transform19.addChildren(StringSensor29)
TouchSensor30 = x3dpsail.TouchSensor()
TouchSensor30.setDescription("touch to activate")
TouchSensor30.setDEF("RightTouch")

Transform19.addChildren(TouchSensor30)

Group13.addChildren(Transform19)
#up
Transform31 = x3dpsail.Transform()
Transform31.setScale([0.5,0.5,0.5])
Shape32 = x3dpsail.Shape()
Appearance33 = x3dpsail.Appearance()
Material34 = x3dpsail.Material()
Material34.setDiffuseColor([0,0.7,1])
Material34.setTransparency(0.5)

Appearance33.setMaterial(Material34)

Shape32.setAppearance(Appearance33)
Extrusion35 = x3dpsail.Extrusion()
Extrusion35.setCreaseAngle(0.785)
Extrusion35.setCrossSection([1,0,0.92,-0.38,0.71,-0.71,0.38,-0.92,0,-1,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1,0,-0.92,0.38,-0.71,0.71,-0.38,0.92,0,1,0.38,0.92,0.71,0.71,0.92,0.38,1,0])
Extrusion35.setSpine([0,1.5,0,0,2.5,0])

Shape32.setGeometry(Extrusion35)

Transform31.addChildren(Shape32)
Transform36 = x3dpsail.Transform()
Transform36.setTranslation([-0.5,2,0])
Shape37 = x3dpsail.Shape()
Appearance38 = x3dpsail.Appearance()
Material39 = x3dpsail.Material()
Material39.setUSE("MaterialLightBlue")

Appearance38.setMaterial(Material39)

Shape37.setAppearance(Appearance38)
Text40 = x3dpsail.Text()
Text40.setDEF("UpString")
Text40.setString(["u"])

Shape37.setGeometry(Text40)

Transform36.addChildren(Shape37)

Transform31.addChildren(Transform36)
StringSensor41 = x3dpsail.StringSensor()
StringSensor41.setDEF("UpSensor")
StringSensor41.setEnabled(False)

Transform31.addChildren(StringSensor41)
TouchSensor42 = x3dpsail.TouchSensor()
TouchSensor42.setDescription("touch to activate")
TouchSensor42.setDEF("UpTouch")

Transform31.addChildren(TouchSensor42)

Group13.addChildren(Transform31)
#down
Transform43 = x3dpsail.Transform()
Transform43.setScale([0.5,0.5,0.5])
Shape44 = x3dpsail.Shape()
Appearance45 = x3dpsail.Appearance()
Material46 = x3dpsail.Material()
Material46.setDiffuseColor([0.7,1,0])
Material46.setTransparency(0.5)

Appearance45.setMaterial(Material46)

Shape44.setAppearance(Appearance45)
Extrusion47 = x3dpsail.Extrusion()
Extrusion47.setCreaseAngle(0.785)
Extrusion47.setCrossSection([1,0,0.92,-0.38,0.71,-0.71,0.38,-0.92,0,-1,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1,0,-0.92,0.38,-0.71,0.71,-0.38,0.92,0,1,0.38,0.92,0.71,0.71,0.92,0.38,1,0])
Extrusion47.setSpine([0,-2.5,0,0,-1.5,0])

Shape44.setGeometry(Extrusion47)

Transform43.addChildren(Shape44)
#<Transform translation=\"-0.5 -2.5 0\"> <Shape> <Text DEF=\"DownString\" string='\"d\"'/> </Shape> </Transform> <StringSensor DEF=\"DownSensor\" enabled=\"false\"/> <TouchSensor description='touch to activate' DEF=\"DownTouch\" enabled=\"true\"/>

Group13.addChildren(Transform43)
#center
Transform48 = x3dpsail.Transform()
Shape49 = x3dpsail.Shape()
Appearance50 = x3dpsail.Appearance()
Material51 = x3dpsail.Material()
Material51.setDiffuseColor([1,0,0.7])

Appearance50.setMaterial(Material51)

Shape49.setAppearance(Appearance50)
Sphere52 = x3dpsail.Sphere()

Shape49.setGeometry(Sphere52)

Transform48.addChildren(Shape49)
Transform53 = x3dpsail.Transform()
Transform53.setScale([0.5,0.5,0.5])
Transform53.setTranslation([-0.5,0,1])
Shape54 = x3dpsail.Shape()
Appearance55 = x3dpsail.Appearance()
Material56 = x3dpsail.Material()
Material56.setUSE("MaterialLightBlue")

Appearance55.setMaterial(Material56)

Shape54.setAppearance(Appearance55)
Text57 = x3dpsail.Text()
Text57.setDEF("CenterString")

Shape54.setGeometry(Text57)

Transform53.addChildren(Shape54)

Transform48.addChildren(Transform53)
StringSensor58 = x3dpsail.StringSensor()
StringSensor58.setDEF("CenterSensor")
StringSensor58.setEnabled(False)

Transform48.addChildren(StringSensor58)
TouchSensor59 = x3dpsail.TouchSensor()
TouchSensor59.setDescription("touch to activate")
TouchSensor59.setDEF("CenterTouch")

Transform48.addChildren(TouchSensor59)

Group13.addChildren(Transform48)

ProtoBody12.addChildren(Group13)
Script60 = x3dpsail.Script()
Script60.setDEF("RightSingleToMultiString")
field61 = x3dpsail.field()
field61.setName("set_rightstring")
field61.setAccessType("inputOnly")
field61.setType("SFString")

Script60.addField(field61)
field62 = x3dpsail.field()
field62.setName("rightlines")
field62.setAccessType("outputOnly")
field62.setType("MFString")

Script60.addField(field62)

Script60.setSourceCode('''ecmascript:\n"+
"\n"+
"function initialize() {\n"+
"	rightlines = new MFString(\"\");\n"+
"}\n"+
"\n"+
"function set_rightstring(rightstr) {\n"+
"	rightlines = new MFString(rightstr);\n"+
"}''')

ProtoBody12.addChildren(Script60)
Script63 = x3dpsail.Script()
Script63.setDEF("UpSingleToMultiString")
field64 = x3dpsail.field()
field64.setName("set_upstring")
field64.setAccessType("inputOnly")
field64.setType("SFString")

Script63.addField(field64)
field65 = x3dpsail.field()
field65.setName("uplines")
field65.setAccessType("outputOnly")
field65.setType("MFString")

Script63.addField(field65)

Script63.setSourceCode('''ecmascript:\n"+
"\n"+
"function initialize() {\n"+
"	uplines = new MFString(\"\");\n"+
"}\n"+
"\n"+
"function set_upstring(upstr) {\n"+
"	uplines = new MFString(upstr);\n"+
"}''')

ProtoBody12.addChildren(Script63)
Script66 = x3dpsail.Script()
Script66.setDEF("CenterSingleToMultiString")
field67 = x3dpsail.field()
field67.setName("set_centerstring")
field67.setAccessType("inputOnly")
field67.setType("SFString")

Script66.addField(field67)
field68 = x3dpsail.field()
field68.setName("centerlines")
field68.setAccessType("outputOnly")
field68.setType("MFString")

Script66.addField(field68)

Script66.setSourceCode('''ecmascript:\n"+
"\n"+
"function initialize() {\n"+
"	centerlines = new MFString(\"\");\n"+
"}\n"+
"\n"+
"function set_centerstring(centerstr) {\n"+
"	centerlines = new MFString(centerstr);\n"+
"}''')

ProtoBody12.addChildren(Script66)
ROUTE69 = x3dpsail.ROUTE()
ROUTE69.setFromField("enteredText")
ROUTE69.setFromNode("CenterSensor")
ROUTE69.setToField("set_centerstring")
ROUTE69.setToNode("CenterSingleToMultiString")

ProtoBody12.addChildren(ROUTE69)
ROUTE70 = x3dpsail.ROUTE()
ROUTE70.setFromField("centerlines")
ROUTE70.setFromNode("CenterSingleToMultiString")
ROUTE70.setToField("set_string")
ROUTE70.setToNode("CenterString")

ProtoBody12.addChildren(ROUTE70)
ROUTE71 = x3dpsail.ROUTE()
ROUTE71.setFromField("isOver")
ROUTE71.setFromNode("CenterTouch")
ROUTE71.setToField("set_enabled")
ROUTE71.setToNode("CenterSensor")

ProtoBody12.addChildren(ROUTE71)
ROUTE72 = x3dpsail.ROUTE()
ROUTE72.setFromField("enteredText")
ROUTE72.setFromNode("RightSensor")
ROUTE72.setToField("set_rightstring")
ROUTE72.setToNode("RightSingleToMultiString")

ProtoBody12.addChildren(ROUTE72)
ROUTE73 = x3dpsail.ROUTE()
ROUTE73.setFromField("rightlines")
ROUTE73.setFromNode("RightSingleToMultiString")
ROUTE73.setToField("set_string")
ROUTE73.setToNode("RightString")

ProtoBody12.addChildren(ROUTE73)
ROUTE74 = x3dpsail.ROUTE()
ROUTE74.setFromField("isOver")
ROUTE74.setFromNode("RightTouch")
ROUTE74.setToField("set_enabled")
ROUTE74.setToNode("RightSensor")

ProtoBody12.addChildren(ROUTE74)
ROUTE75 = x3dpsail.ROUTE()
ROUTE75.setFromField("enteredText")
ROUTE75.setFromNode("UpSensor")
ROUTE75.setToField("set_upstring")
ROUTE75.setToNode("UpSingleToMultiString")

ProtoBody12.addChildren(ROUTE75)
ROUTE76 = x3dpsail.ROUTE()
ROUTE76.setFromField("uplines")
ROUTE76.setFromNode("UpSingleToMultiString")
ROUTE76.setToField("set_string")
ROUTE76.setToNode("UpString")

ProtoBody12.addChildren(ROUTE76)
ROUTE77 = x3dpsail.ROUTE()
ROUTE77.setFromField("isOver")
ROUTE77.setFromNode("UpTouch")
ROUTE77.setToField("set_enabled")
ROUTE77.setToNode("UpSensor")

ProtoBody12.addChildren(ROUTE77)

ProtoDeclare11.setProtoBody(ProtoBody12)

Scene10.addChildren(ProtoDeclare11)
NavigationInfo78 = x3dpsail.NavigationInfo()

Scene10.addChildren(NavigationInfo78)
Viewpoint79 = x3dpsail.Viewpoint()
Viewpoint79.setDescription("Process pipes")
Viewpoint79.setOrientation([1,0,0,-0.4])
Viewpoint79.setPosition([0,5,12])

Scene10.addChildren(Viewpoint79)
Transform80 = x3dpsail.Transform()
Transform80.setTranslation([0,-2.5,0])
ProtoInstance81 = x3dpsail.ProtoInstance()
ProtoInstance81.setName("Process")

Transform80.addChildren(ProtoInstance81)

Scene10.addChildren(Transform80)
Transform82 = x3dpsail.Transform()
ProtoInstance83 = x3dpsail.ProtoInstance()
ProtoInstance83.setName("Process")

Transform82.addChildren(ProtoInstance83)

Scene10.addChildren(Transform82)
Transform84 = x3dpsail.Transform()
Transform84.setTranslation([0,2.5,0])
ProtoInstance85 = x3dpsail.ProtoInstance()
ProtoInstance85.setName("Process")

Transform84.addChildren(ProtoInstance85)

Scene10.addChildren(Transform84)

X3D0.setScene(Scene10)
X3D0.toFileX3D("././pp3_RoundTrip.x3d")
