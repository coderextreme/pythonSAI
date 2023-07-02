print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.0"
head1 = x3d.head()
meta2 = x3d.meta()
meta2.name = "title"
meta2.content = "HeadsUpDisplayPrototype.x3d"

head1.children.append(meta2)
meta3 = x3d.meta()
meta3.name = "description"
meta3.content = "Generic Heads Up Display (HUD) prototype to keep children on screen."

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.name = "creator"
meta4.content = "Don Brutzman"

head1.children.append(meta4)
meta5 = x3d.meta()
meta5.name = "created"
meta5.content = "9 November 2003"

head1.children.append(meta5)
meta6 = x3d.meta()
meta6.name = "modified"
meta6.content = "14 January 2014"

head1.children.append(meta6)
meta7 = x3d.meta()
meta7.name = "subject"
meta7.content = "HUD Heads Up Display"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.name = "identifier"
meta8.content = "https://savage.nps.edu/Savage/Tools/HeadsUpDisplays/HeadsUpDisplayPrototype.x3d"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "generator"
meta9.content = "X3D-Edit 3.2, https://savage.nps.edu/X3D-Edit"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "license"
meta10.content = "../../license.html"

head1.children.append(meta10)

X3D0.head = head1
Scene11 = x3d.Scene()
ProtoDeclare12 = x3d.ProtoDeclare()
ProtoDeclare12.name = "HeadsUpDisplay"
ProtoDeclare12.appinfo = "HeadsUpDisplay positions child geometry in screen space, movable by the user"
ProtoInterface13 = x3d.ProtoInterface()
field14 = x3d.field()
field14.name = "children"
field14.accessType = "inputOutput"
field14.appinfo = "Displayed subscene positioned as a HUD."
field14.type = "MFNode"
#default is null array of nodes

ProtoInterface13.field.append(field14)
field15 = x3d.field()
field15.name = "dragChildren"
field15.accessType = "inputOutput"
field15.appinfo = "Additional HUD geometry which can be touched and dragged for repositioning. If this geometry goes offscreen (perhaps due to screen resizing) then it snaps back to original position."
field15.type = "MFNode"
#default is null array of nodes

ProtoInterface13.field.append(field15)
field16 = x3d.field()
field16.name = "locationOffset"
field16.accessType = "initializeOnly"
field16.appinfo = "Modified screen location and distance (for size)."
field16.type = "SFVec3f"
field16.value = [-2,-2,0]

ProtoInterface13.field.append(field16)
field17 = x3d.field()
field17.name = "traceEnabled"
field17.accessType = "initializeOnly"
field17.appinfo = "Enable/disable console output for troubleshooting."
field17.type = "SFBool"
field17.value = False

ProtoInterface13.field.append(field17)

ProtoDeclare12.ProtoInterface = ProtoInterface13
ProtoBody18 = x3d.ProtoBody()
Group19 = x3d.Group()
ProximitySensor20 = x3d.ProximitySensor()
ProximitySensor20.DEF = "WhereSensor"
ProximitySensor20.size = [1000000000,1000000000,1000000000]
IS21 = x3d.IS()
connect22 = x3d.connect()
connect22.nodeField = "center"
connect22.protoField = "locationOffset"

IS21.connect.append(connect22)

ProximitySensor20.IS = IS21

Group19.children.append(ProximitySensor20)
Transform23 = x3d.Transform()
Transform23.DEF = "FixedLocation"
Transform24 = x3d.Transform()
Transform24.DEF = "MovableLocation"
Transform25 = x3d.Transform()
Transform25.DEF = "LocationOffset"
IS26 = x3d.IS()
connect27 = x3d.connect()
connect27.nodeField = "translation"
connect27.protoField = "locationOffset"

IS26.connect.append(connect27)

Transform25.IS = IS26
Transform28 = x3d.Transform()
Transform28.translation = [0,0,-10]
Group29 = x3d.Group()
IS30 = x3d.IS()
connect31 = x3d.connect()
connect31.nodeField = "children"
connect31.protoField = "children"

IS30.connect.append(connect31)

Group29.IS = IS30

Transform28.children.append(Group29)
Group32 = x3d.Group()
Group32.DEF = "PlaneMovementSensorGroup"
Group33 = x3d.Group()
Group33.DEF = "DragGeometry"
IS34 = x3d.IS()
connect35 = x3d.connect()
connect35.nodeField = "children"
connect35.protoField = "dragChildren"

IS34.connect.append(connect35)

Group33.IS = IS34

Group32.children.append(Group33)
PlaneSensor36 = x3d.PlaneSensor()
PlaneSensor36.DEF = "PlaneMovementSensor"
PlaneSensor36.description = "click and drag to move interface"
IS37 = x3d.IS()
connect38 = x3d.connect()
connect38.nodeField = "offset"
connect38.protoField = "locationOffset"

IS37.connect.append(connect38)

PlaneSensor36.IS = IS37

Group32.children.append(PlaneSensor36)
VisibilitySensor39 = x3d.VisibilitySensor()
VisibilitySensor39.DEF = "MovementVisibilitySensor"

Group32.children.append(VisibilitySensor39)
Script40 = x3d.Script()
Script40.DEF = "VisibilityControlScript"
field41 = x3d.field()
field41.name = "traceEnabled"
field41.accessType = "initializeOnly"
field41.type = "SFBool"

Script40.field.append(field41)
field42 = x3d.field()
field42.name = "isVisible"
field42.accessType = "initializeOnly"
field42.type = "SFBool"
field42.value = True

Script40.field.append(field42)
field43 = x3d.field()
field43.name = "planeSensorTranslation"
field43.accessType = "initializeOnly"
field43.type = "SFVec3f"
field43.value = [0,0,0]

Script40.field.append(field43)
field44 = x3d.field()
field44.name = "setIsVisible"
field44.accessType = "inputOnly"
field44.type = "SFBool"

Script40.field.append(field44)
field45 = x3d.field()
field45.name = "setPlaneSensorIsActive"
field45.accessType = "inputOnly"
field45.type = "SFBool"

Script40.field.append(field45)
field46 = x3d.field()
field46.name = "setPlaneSensorTranslation"
field46.accessType = "inputOnly"
field46.type = "SFVec3f"

Script40.field.append(field46)
field47 = x3d.field()
field47.name = "translationChanged"
field47.accessType = "outputOnly"
field47.type = "SFVec3f"

Script40.field.append(field47)
field48 = x3d.field()
field48.name = "translationOffsetChanged"
field48.accessType = "outputOnly"
field48.type = "SFVec3f"

Script40.field.append(field48)
IS49 = x3d.IS()
connect50 = x3d.connect()
connect50.nodeField = "traceEnabled"
connect50.protoField = "traceEnabled"

IS49.connect.append(connect50)

Script40.IS = IS49

Script40.sourceCode = '''ecmascript:\n"+
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
"}'''

Group32.children.append(Script40)
ROUTE51 = x3d.ROUTE()
ROUTE51.fromField = "isActive"
ROUTE51.fromNode = "PlaneMovementSensor"
ROUTE51.toField = "setPlaneSensorIsActive"
ROUTE51.toNode = "VisibilityControlScript"

Group32.children.append(ROUTE51)
ROUTE52 = x3d.ROUTE()
ROUTE52.fromField = "translation_changed"
ROUTE52.fromNode = "PlaneMovementSensor"
ROUTE52.toField = "setPlaneSensorTranslation"
ROUTE52.toNode = "VisibilityControlScript"

Group32.children.append(ROUTE52)
ROUTE53 = x3d.ROUTE()
ROUTE53.fromField = "isActive"
ROUTE53.fromNode = "MovementVisibilitySensor"
ROUTE53.toField = "setIsVisible"
ROUTE53.toNode = "VisibilityControlScript"

Group32.children.append(ROUTE53)

Transform28.children.append(Group32)

Transform25.children.append(Transform28)

Transform24.children.append(Transform25)
ROUTE54 = x3d.ROUTE()
ROUTE54.fromField = "translation_changed"
ROUTE54.fromNode = "PlaneMovementSensor"
ROUTE54.toField = "set_translation"
ROUTE54.toNode = "MovableLocation"

Transform24.children.append(ROUTE54)
ROUTE55 = x3d.ROUTE()
ROUTE55.fromField = "translationChanged"
ROUTE55.fromNode = "VisibilityControlScript"
ROUTE55.toField = "set_translation"
ROUTE55.toNode = "MovableLocation"

Transform24.children.append(ROUTE55)
ROUTE56 = x3d.ROUTE()
ROUTE56.fromField = "translationOffsetChanged"
ROUTE56.fromNode = "VisibilityControlScript"
ROUTE56.toField = "set_offset"
ROUTE56.toNode = "PlaneMovementSensor"

Transform24.children.append(ROUTE56)

Transform23.children.append(Transform24)

Group19.children.append(Transform23)
ROUTE57 = x3d.ROUTE()
ROUTE57.fromField = "position_changed"
ROUTE57.fromNode = "WhereSensor"
ROUTE57.toField = "set_translation"
ROUTE57.toNode = "FixedLocation"

Group19.children.append(ROUTE57)
ROUTE58 = x3d.ROUTE()
ROUTE58.fromField = "orientation_changed"
ROUTE58.fromNode = "WhereSensor"
ROUTE58.toField = "set_rotation"
ROUTE58.toNode = "FixedLocation"

Group19.children.append(ROUTE58)

ProtoBody18.children.append(Group19)

ProtoDeclare12.ProtoBody = ProtoBody18

Scene11.children.append(ProtoDeclare12)
#====================
Background59 = x3d.Background()

Scene11.children.append(Background59)
Anchor60 = x3d.Anchor()
Anchor60.description = "HeadsUpDisplayExample"
Anchor60.parameter = ["target=_blank"]
Anchor60.url = ["HeadsUpDisplayExample.x3d","https://savage.nps.edu/Savage/Tools/HeadsUpDisplays/HeadsUpDisplayrExample.x3d","HeadsUpDisplayExample.wrl","https://savage.nps.edu/Savage/Tools/HeadsUpDisplays/HeadsUpDisplayExample.wrl"]
Shape61 = x3d.Shape()
Appearance62 = x3d.Appearance()
Material63 = x3d.Material()
Material63.diffuseColor = [0,1,1]
Material63.emissiveColor = [0,1,1]

Appearance62.material = Material63

Shape61.appearance = Appearance62
Text64 = x3d.Text()
Text64.string = ["HeadsUpDisplayPrototype.x3d","is a Prototype definition file.","","To see an example scene using this node","click this text to view","HeadsUpDisplayExample.x3d"]
FontStyle65 = x3d.FontStyle()
FontStyle65.justify = ["MIDDLE","MIDDLE"]
FontStyle65.size = 0.8

Text64.fontStyle = FontStyle65

Shape61.geometry = Text64

Anchor60.children.append(Shape61)

Scene11.children.append(Anchor60)

X3D0.Scene = Scene11
f = open("././HeadsUpDisplayPrototype_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
