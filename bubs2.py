print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"
head1 = x3d.head()
meta2 = x3d.meta()
meta2.name = "title"
meta2.content = "bubs2.x3d"

head1.children.append(meta2)
meta3 = x3d.meta()
meta3.name = "creator"
meta3.content = "John Carlson"

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.name = "description"
meta4.content = "Tour around a prismatic sphere"

head1.children.append(meta4)
meta5 = x3d.meta()
meta5.name = "generator"
meta5.content = "X3D-Edit, https://savage.nps.edu/X3D-Edit"

head1.children.append(meta5)
meta6 = x3d.meta()
meta6.name = "identifier"
meta6.content = "https://coderextreme.net/X3DJSONLD/geo.x3d"

head1.children.append(meta6)
meta7 = x3d.meta()
meta7.name = "translated"
meta7.content = "13 March 2016"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.name = "generator"
meta8.content = "X3dToJson.xslt, https://www.web3d.org/x3d/stylesheets/X3dToJson.html"

head1.children.append(meta8)

X3D0.head = head1
Scene9 = x3d.Scene()
NavigationInfo10 = x3d.NavigationInfo()
NavigationInfo10.type = ["EXAMINE"]

Scene9.children.append(NavigationInfo10)
Viewpoint11 = x3d.Viewpoint()
Viewpoint11.position = [0,0,4]
Viewpoint11.orientation = [1,0,0,0]
Viewpoint11.description = "Bubbles in action"

Scene9.children.append(Viewpoint11)
Background12 = x3d.Background()
Background12.backUrl = ["../resources/images/BK.png","https://coderextreme.net/X3DJSONLD/images/BK.png"]
Background12.bottomUrl = ["../resources/images/BT.png","https://coderextreme.net/X3DJSONLD/images/BT.png"]
Background12.frontUrl = ["../resources/images/FR.png","https://coderextreme.net/X3DJSONLD/images/FR.png"]
Background12.leftUrl = ["../resources/images/LF.png","https://coderextreme.net/X3DJSONLD/images/LF.png"]
Background12.rightUrl = ["../resources/images/RT.png","https://coderextreme.net/X3DJSONLD/images/RT.png"]
Background12.topUrl = ["../resources/images/TP.png","https://coderextreme.net/X3DJSONLD/images/TP.png"]

Scene9.children.append(Background12)
ProtoDeclare13 = x3d.ProtoDeclare()
ProtoDeclare13.name = "Bubble"
ProtoBody14 = x3d.ProtoBody()
Transform15 = x3d.Transform()
Transform15.DEF = "body_trans"
Shape16 = x3d.Shape()
Sphere17 = x3d.Sphere()
Sphere17.radius = 0.25

Shape16.geometry = Sphere17
Appearance18 = x3d.Appearance()
Material19 = x3d.Material()
Material19.diffuseColor = [1,0,0]
Material19.transparency = 0.2

Appearance18.material = Material19

Shape16.appearance = Appearance18

Transform15.children.append(Shape16)
Script20 = x3d.Script()
Script20.DEF = "bounce"
field21 = x3d.field()
field21.name = "scale"
field21.accessType = "inputOutput"
field21.type = "SFVec3f"
field21.value = [1,1,1]

Script20.field.append(field21)
field22 = x3d.field()
field22.name = "translation"
field22.accessType = "inputOutput"
field22.type = "SFVec3f"
field22.value = [0,0,0]

Script20.field.append(field22)
field23 = x3d.field()
field23.name = "velocity"
field23.accessType = "inputOutput"
field23.type = "SFVec3f"
field23.value = [0,0,0]

Script20.field.append(field23)
field24 = x3d.field()
field24.name = "scalvel"
field24.accessType = "inputOutput"
field24.type = "SFVec3f"
field24.value = [0,0,0]

Script20.field.append(field24)
field25 = x3d.field()
field25.name = "set_fraction"
field25.accessType = "inputOnly"
field25.type = "SFFloat"

Script20.field.append(field25)

Script20.sourceCode = '''ecmascript:\n"+
"function initialize() {\n"+
"    velocity = new SFVec3f(Math.random() * 0.25 - 0.125, Math.random() * 0.25 - 0.125, Math.random() * 0.25 - 0.125);\n"+
"\n"+
"    scalvel = new SFVec3f(Math.random() * 0.4, Math.random() * 0.4, Math.random() * 0.4);\n"+
"}\n"+
"\n"+
"function set_fraction(value) {\n"+
"    if (typeof translation === 'undefined') {\n"+
"		translation = new SFVec3f(0, 0, 0);\n"+
"    }\n"+
"    if (typeof velocity === 'undefined') {\n"+
"		velocity = new SFVec3f(0, 0, 0);\n"+
"    }\n"+
"    if (typeof scalvel === 'undefined') {\n"+
"		scalvel = new SFVec3f(0, 0, 0);\n"+
"    }\n"+
"    if (typeof scale === 'undefined') {\n"+
"		scale = new SFVec3f(1, 1, 1);\n"+
"    }\n"+
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
"}'''

Transform15.children.append(Script20)
TimeSensor26 = x3d.TimeSensor()
TimeSensor26.DEF = "bubbleClock"
TimeSensor26.cycleInterval = 10
TimeSensor26.loop = True

Transform15.children.append(TimeSensor26)
ROUTE27 = x3d.ROUTE()
ROUTE27.fromNode = "bounce"
ROUTE27.fromField = "translation_changed"
ROUTE27.toNode = "body_trans"
ROUTE27.toField = "set_translation"

Transform15.children.append(ROUTE27)
ROUTE28 = x3d.ROUTE()
ROUTE28.fromNode = "bounce"
ROUTE28.fromField = "scale_changed"
ROUTE28.toNode = "body_trans"
ROUTE28.toField = "set_scale"

Transform15.children.append(ROUTE28)
ROUTE29 = x3d.ROUTE()
ROUTE29.fromNode = "bubbleClock"
ROUTE29.fromField = "fraction_changed"
ROUTE29.toNode = "bounce"
ROUTE29.toField = "set_fraction"

Transform15.children.append(ROUTE29)

ProtoBody14.children.append(Transform15)

ProtoDeclare13.ProtoBody = ProtoBody14

Scene9.children.append(ProtoDeclare13)
ProtoInstance30 = x3d.ProtoInstance()
ProtoInstance30.name = "Bubble"
ProtoInstance30.DEF = "bubbleA"

Scene9.children.append(ProtoInstance30)
ProtoInstance31 = x3d.ProtoInstance()
ProtoInstance31.name = "Bubble"
ProtoInstance31.DEF = "bubbleB"

Scene9.children.append(ProtoInstance31)
ProtoInstance32 = x3d.ProtoInstance()
ProtoInstance32.name = "Bubble"
ProtoInstance32.DEF = "bubbleC"

Scene9.children.append(ProtoInstance32)
ProtoInstance33 = x3d.ProtoInstance()
ProtoInstance33.name = "Bubble"
ProtoInstance33.DEF = "bubbleD"

Scene9.children.append(ProtoInstance33)

X3D0.Scene = Scene9
f = open("././bubs2_RoundTrip.x3d", "w")
f.write(X3D0.XML())
f.close()
