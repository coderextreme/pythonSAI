import x3dpsail as x3d
X3D0 = x3d.X3D()
X3D0.setProfile("Immersive")
X3D0.setVersion("3.0")
head1 = x3d.head()
meta2 = x3d.meta()
meta2.setName("title")
meta2.setContent("HeadsUpDisplayPrototype.x3d")

head1.addMeta(meta2)
meta3 = x3d.meta()
meta3.setName("description")
meta3.setContent("Generic Heads Up Display (HUD) prototype to keep children on screen.")

head1.addMeta(meta3)
meta4 = x3d.meta()
meta4.setName("creator")
meta4.setContent("Don Brutzman")

head1.addMeta(meta4)
meta5 = x3d.meta()
meta5.setName("created")
meta5.setContent("9 November 2003")

head1.addMeta(meta5)
meta6 = x3d.meta()
meta6.setName("modified")
meta6.setContent("14 January 2014")

head1.addMeta(meta6)
meta7 = x3d.meta()
meta7.setName("subject")
meta7.setContent("HUD Heads Up Display")

head1.addMeta(meta7)
meta8 = x3d.meta()
meta8.setName("identifier")
meta8.setContent("https://savage.nps.edu/Savage/Tools/HeadsUpDisplays/HeadsUpDisplayPrototype.x3d")

head1.addMeta(meta8)
meta9 = x3d.meta()
meta9.setName("generator")
meta9.setContent("X3D-Edit 3.2, https://savage.nps.edu/X3D-Edit")

head1.addMeta(meta9)
meta10 = x3d.meta()
meta10.setName("license")
meta10.setContent("../../license.html")

head1.addMeta(meta10)

X3D0.setHead(head1)
Scene11 = x3d.Scene()
ProtoDeclare12 = x3d.ProtoDeclare()
ProtoDeclare12.setName("HeadsUpDisplay")
ProtoDeclare12.setAppinfo("HeadsUpDisplay positions child geometry in screen space, movable by the user")
ProtoInterface13 = x3d.ProtoInterface()
field14 = x3d.field()
field14.setName("children")
field14.setAccessType("inputOutput")
field14.setAppinfo("Displayed subscene positioned as a HUD.")
field14.setType("MFNode")
#default is null array of nodes

ProtoInterface13.addField(field14)
field15 = x3d.field()
field15.setName("dragChildren")
field15.setAccessType("inputOutput")
field15.setAppinfo("Additional HUD geometry which can be touched and dragged for repositioning. If this geometry goes offscreen (perhaps due to screen resizing) then it snaps back to original position.")
field15.setType("MFNode")
#default is null array of nodes

ProtoInterface13.addField(field15)
field16 = x3d.field()
field16.setName("locationOffset")
field16.setAccessType("initializeOnly")
field16.setAppinfo("Modified screen location and distance (for size).")
field16.setType("SFVec3f")
field16.setValue("-2 -2 0")

ProtoInterface13.addField(field16)
field17 = x3d.field()
field17.setName("traceEnabled")
field17.setAccessType("initializeOnly")
field17.setAppinfo("Enable/disable console output for troubleshooting.")
field17.setType("SFBool")
field17.setValue("false")

ProtoInterface13.addField(field17)

ProtoDeclare12.setProtoInterface(ProtoInterface13)
ProtoBody18 = x3d.ProtoBody()
Group19 = x3d.Group()
ProximitySensor20 = x3d.ProximitySensor()
ProximitySensor20.setDEF("WhereSensor")
ProximitySensor20.setSize([1000000000,1000000000,1000000000])
IS21 = x3d.IS()
connect22 = x3d.connect()
connect22.setNodeField("center")
connect22.setProtoField("locationOffset")

IS21.addConnect(connect22)

ProximitySensor20.setIS(IS21)

Group19.addChildren(ProximitySensor20)
Transform23 = x3d.Transform()
Transform23.setDEF("FixedLocation")
Transform24 = x3d.Transform()
Transform24.setDEF("MovableLocation")
Transform25 = x3d.Transform()
Transform25.setDEF("LocationOffset")
IS26 = x3d.IS()
connect27 = x3d.connect()
connect27.setNodeField("translation")
connect27.setProtoField("locationOffset")

IS26.addConnect(connect27)

Transform25.setIS(IS26)
Transform28 = x3d.Transform()
Transform28.setTranslation([0,0,-10])
Group29 = x3d.Group()
IS30 = x3d.IS()
connect31 = x3d.connect()
connect31.setNodeField("children")
connect31.setProtoField("children")

IS30.addConnect(connect31)

Group29.setIS(IS30)

Transform28.addChildren(Group29)
Group32 = x3d.Group()
Group32.setDEF("PlaneMovementSensorGroup")
Group33 = x3d.Group()
Group33.setDEF("DragGeometry")
IS34 = x3d.IS()
connect35 = x3d.connect()
connect35.setNodeField("children")
connect35.setProtoField("dragChildren")

IS34.addConnect(connect35)

Group33.setIS(IS34)

Group32.addChildren(Group33)
PlaneSensor36 = x3d.PlaneSensor()
PlaneSensor36.setDEF("PlaneMovementSensor")
PlaneSensor36.setDescription("click and drag to move interface")
IS37 = x3d.IS()
connect38 = x3d.connect()
connect38.setNodeField("offset")
connect38.setProtoField("locationOffset")

IS37.addConnect(connect38)

PlaneSensor36.setIS(IS37)

Group32.addChildren(PlaneSensor36)
VisibilitySensor39 = x3d.VisibilitySensor()
VisibilitySensor39.setDEF("MovementVisibilitySensor")

Group32.addChildren(VisibilitySensor39)
Script40 = x3d.Script()
Script40.setDEF("VisibilityControlScript")
field41 = x3d.field()
field41.setName("traceEnabled")
field41.setAccessType("initializeOnly")
field41.setType("SFBool")

Script40.addField(field41)
field42 = x3d.field()
field42.setName("isVisible")
field42.setAccessType("initializeOnly")
field42.setType("SFBool")
field42.setValue("true")

Script40.addField(field42)
field43 = x3d.field()
field43.setName("planeSensorTranslation")
field43.setAccessType("initializeOnly")
field43.setType("SFVec3f")
field43.setValue("0 0 0")

Script40.addField(field43)
field44 = x3d.field()
field44.setName("setIsVisible")
field44.setAccessType("inputOnly")
field44.setType("SFBool")

Script40.addField(field44)
field45 = x3d.field()
field45.setName("setPlaneSensorIsActive")
field45.setAccessType("inputOnly")
field45.setType("SFBool")

Script40.addField(field45)
field46 = x3d.field()
field46.setName("setPlaneSensorTranslation")
field46.setAccessType("inputOnly")
field46.setType("SFVec3f")

Script40.addField(field46)
field47 = x3d.field()
field47.setName("translationChanged")
field47.setAccessType("outputOnly")
field47.setType("SFVec3f")

Script40.addField(field47)
field48 = x3d.field()
field48.setName("translationOffsetChanged")
field48.setAccessType("outputOnly")
field48.setType("SFVec3f")

Script40.addField(field48)
IS49 = x3d.IS()
connect50 = x3d.connect()
connect50.setNodeField("traceEnabled")
connect50.setProtoField("traceEnabled")

IS49.addConnect(connect50)

Script40.setIS(IS49)

Script40.setSourceCode('''ecmascript:\n"+
"\n"+
"function tracePrint (text)\n"+
"{\n"+
"	if (traceEnabled) Browser.print ('[HeadsUpDisplayPrototype VisibilityControlScript] ' + text);\n"+
"}\n"+
"function setIsVisible (value, timeStamp)\n"+
"{\n"+
"	isVisible = value;\n"+
"	tracePrint('isVisible=' + value);\n"+
"}\n"+
"function setPlaneSensorIsActive (value, timeStamp)\n"+
"{\n"+
"	tracePrint('PlaneSensor isActive=' + value);\n"+
"\n"+
"	if (value == false)\n"+
"	{\n"+
"		tracePrint('planeSensorTranslation=' + planeSensorTranslation);\n"+
"		if (isVisible)\n"+
"		{\n"+
"			translationChanged = planeSensorTranslation;\n"+
"		}\n"+
"		else\n"+
"		{\n"+
"			// fell off screen, reset to center\n"+
"			translationChanged = new SFVec3f(0, 0, 0);\n"+
"			translationOffsetChanged  = new SFVec3f(0, 0, 0);\n"+
"		}\n"+
"	}\n"+
"}\n"+
"function setPlaneSensorTranslation (value, timeStamp)\n"+
"{\n"+
"	planeSensorTranslation = value;\n"+
"	tracePrint('planeSensorTranslation=' + value);\n"+
"}''')

Group32.addChildren(Script40)
ROUTE51 = x3d.ROUTE()
ROUTE51.setFromField("isActive")
ROUTE51.setFromNode("PlaneMovementSensor")
ROUTE51.setToField("setPlaneSensorIsActive")
ROUTE51.setToNode("VisibilityControlScript")

Group32.addChildren(ROUTE51)
ROUTE52 = x3d.ROUTE()
ROUTE52.setFromField("translation_changed")
ROUTE52.setFromNode("PlaneMovementSensor")
ROUTE52.setToField("setPlaneSensorTranslation")
ROUTE52.setToNode("VisibilityControlScript")

Group32.addChildren(ROUTE52)
ROUTE53 = x3d.ROUTE()
ROUTE53.setFromField("isActive")
ROUTE53.setFromNode("MovementVisibilitySensor")
ROUTE53.setToField("setIsVisible")
ROUTE53.setToNode("VisibilityControlScript")

Group32.addChildren(ROUTE53)

Transform28.addChildren(Group32)

Transform25.addChildren(Transform28)

Transform24.addChildren(Transform25)
ROUTE54 = x3d.ROUTE()
ROUTE54.setFromField("translation_changed")
ROUTE54.setFromNode("PlaneMovementSensor")
ROUTE54.setToField("set_translation")
ROUTE54.setToNode("MovableLocation")

Transform24.addChildren(ROUTE54)
ROUTE55 = x3d.ROUTE()
ROUTE55.setFromField("translationChanged")
ROUTE55.setFromNode("VisibilityControlScript")
ROUTE55.setToField("set_translation")
ROUTE55.setToNode("MovableLocation")

Transform24.addChildren(ROUTE55)
ROUTE56 = x3d.ROUTE()
ROUTE56.setFromField("translationOffsetChanged")
ROUTE56.setFromNode("VisibilityControlScript")
ROUTE56.setToField("set_offset")
ROUTE56.setToNode("PlaneMovementSensor")

Transform24.addChildren(ROUTE56)

Transform23.addChildren(Transform24)

Group19.addChildren(Transform23)
ROUTE57 = x3d.ROUTE()
ROUTE57.setFromField("position_changed")
ROUTE57.setFromNode("WhereSensor")
ROUTE57.setToField("set_translation")
ROUTE57.setToNode("FixedLocation")

Group19.addChildren(ROUTE57)
ROUTE58 = x3d.ROUTE()
ROUTE58.setFromField("orientation_changed")
ROUTE58.setFromNode("WhereSensor")
ROUTE58.setToField("set_rotation")
ROUTE58.setToNode("FixedLocation")

Group19.addChildren(ROUTE58)

ProtoBody18.addChildren(Group19)

ProtoDeclare12.setProtoBody(ProtoBody18)

Scene11.addChildren(ProtoDeclare12)
#====================
Background59 = x3d.Background()
Background59.setGroundColor([0.1,0.1,0.3])
Background59.setSkyColor([0.5,0.5,0.1])

Scene11.addChildren(Background59)
Anchor60 = x3d.Anchor()
Anchor60.setDescription("HeadsUpDisplayExample")
Anchor60.setParameter(["target=_blank"])
Anchor60.setUrl(["HeadsUpDisplayExample.x3d","https://savage.nps.edu/Savage/Tools/HeadsUpDisplays/HeadsUpDisplayrExample.x3d","HeadsUpDisplayExample.wrl","https://savage.nps.edu/Savage/Tools/HeadsUpDisplays/HeadsUpDisplayExample.wrl"])
Shape61 = x3d.Shape()
Appearance62 = x3d.Appearance()
Material63 = x3d.Material()
Material63.setDiffuseColor([0,1,1])
Material63.setEmissiveColor([0,1,1])

Appearance62.setMaterial(Material63)

Shape61.setAppearance(Appearance62)
Text64 = x3d.Text()
Text64.setString(["HeadsUpDisplayPrototype.x3d","is a Prototype definition file.","","To see an example scene using this node","click this text to view","HeadsUpDisplayExample.x3d"])
FontStyle65 = x3d.FontStyle()
FontStyle65.setJustify(["MIDDLE","MIDDLE"])
FontStyle65.setSize(0.8)

Text64.setFontStyle(FontStyle65)

Shape61.setGeometry(Text64)

Anchor60.addChildren(Shape61)

Scene11.addChildren(Anchor60)

X3D0.setScene(Scene11)
X3D0.toFileX3D("././HeadsUpDisplayPrototype_RoundTrip.x3d")
