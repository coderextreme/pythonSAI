print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"
head1 = x3d.head()
meta2 = x3d.meta()
meta2.name = "title"
meta2.content = "HeadsUpDisplayExample.x3d"

head1.children.append(meta2)
meta3 = x3d.meta()
meta3.name = "description"
meta3.content = "Prototype definition that demonstrates use of a simple HeadsUpDisplay (HUD) prototype that maintains a stable position for its children on the screen."

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.name = "creator"
meta4.content = "Leonard Daly and Don Brutzman"

head1.children.append(meta4)
meta5 = x3d.meta()
meta5.name = "created"
meta5.content = "15 July 2006"

head1.children.append(meta5)
meta6 = x3d.meta()
meta6.name = "modified"
meta6.content = "24 October 2016"

head1.children.append(meta6)
meta7 = x3d.meta()
meta7.name = "reference"
meta7.content = "HeadsUpDisplayPrototype.x3d"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.name = "reference"
meta8.content = "http://X3dGraphics.com"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "reference"
meta9.content = "https://www.web3d.org/x3d/content/examples/X3dResources.html"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "rights"
meta10.content = "Copyright 2006, Daly Realism and Don Brutzman"

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.name = "subject"
meta11.content = "X3D book, X3D graphics, X3D-Edit, http://www.x3dGraphics.com"

head1.children.append(meta11)
meta12 = x3d.meta()
meta12.name = "identifier"
meta12.content = "http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/HeadsUpDisplayExample.x3d"

head1.children.append(meta12)
meta13 = x3d.meta()
meta13.name = "generator"
meta13.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"

head1.children.append(meta13)
meta14 = x3d.meta()
meta14.name = "license"
meta14.content = "../license.html"

head1.children.append(meta14)

X3D0.head = head1
Scene15 = x3d.Scene()
#Simple Heads-Up Display (HUD) Prototype\\n \\n Manages the display of a HUD and maintains its position on the screen.\\n Changes to fieldOfView (in Viewpoint node) will change screen position\\n \\n Fields:\\n hudSize Size of HUD (initializeOnly - SFVec3f) default=\"1 1 .01\"\\n hudColor Color of HUD (inputOutput - SFColor) default=\"1 1 1\"\\n screenOffset Offset of HUD. This field positions the HUD on the display screen (inputOutput - SFVec3f) default=\"0 0 0\"\\n hudGeometry Geometry to be placed on the HUD. Origin is center of HUD. (inputOutput - MFNode) default = []\\n position_changed Current viewer location (outputOnly - SFVec3f)\\n orientation_changed Current viewer orientation (outputOnly - SFRotation)\\n \\n \\n
ExternProtoDeclare16 = x3d.ExternProtoDeclare()
ExternProtoDeclare16.name = "HeadsUpDisplay"
ExternProtoDeclare16.appinfo = "Heads-up display (HUD) keeps child geometry aligned on screen in a consistent location"
ExternProtoDeclare16.url = ["HeadsUpDisplayPrototype.x3d#HeadsUpDisplay","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/HeadsUpDisplayPrototype.x3d#HeadsUpDisplay","HeadsUpDisplayPrototype.wrl#HeadsUpDisplay","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/HeadsUpDisplayPrototype.wrl#HeadsUpDisplay"]
field17 = x3d.field()
field17.name = "screenOffset"
field17.accessType = "inputOutput"
field17.appinfo = "offset position for HUD relative to current view location, default 0 0 -5"
field17.type = "SFVec3f"

ExternProtoDeclare16.field.append(field17)
field18 = x3d.field()
field18.name = "children"
field18.accessType = "inputOutput"
field18.appinfo = "X3D content positioned at HUD offset"
field18.type = "MFNode"

ExternProtoDeclare16.field.append(field18)
field19 = x3d.field()
field19.name = "position_changed"
field19.accessType = "outputOnly"
field19.appinfo = "HUD position update (in world coordinates) relative to original location"
field19.type = "SFVec3f"

ExternProtoDeclare16.field.append(field19)
field20 = x3d.field()
field20.name = "orientation_changed"
field20.accessType = "outputOnly"
field20.appinfo = "HUD orientation update relative to original location"
field20.type = "SFRotation"

ExternProtoDeclare16.field.append(field20)

Scene15.children.append(ExternProtoDeclare16)
Background21 = x3d.Background()
Background21.DEF = "SandyShallowBottom"
Background21.groundAngle = [0.05,1.52,1.56,1.5707]
Background21.skyAngle = [0.04,0.05,0.1,1.309,1.57]

Scene15.children.append(Background21)
Viewpoint22 = x3d.Viewpoint()
Viewpoint22.description = "Heads-up display (HUD)"

Scene15.children.append(Viewpoint22)
#ProtoDeclare is the \"cookie cutter\" template, ProtoInstance creates an actual occurrence
ProtoInstance23 = x3d.ProtoInstance()
ProtoInstance23.name = "HeadsUpDisplay"
ProtoInstance23.DEF = "HeadsUpDisplayInstance"
#example: upper left-hand corner of screen (x=-2, y=1) and set back z=-5 from user view
fieldValue24 = x3d.fieldValue()
fieldValue24.name = "screenOffset"
fieldValue24.value = "-0.75 1 -5"

ProtoInstance23.fieldValue.append(fieldValue24)
fieldValue25 = x3d.fieldValue()
fieldValue25.name = "children"
Shape26 = x3d.Shape()
Text27 = x3d.Text()
Text27.string = ["HUD text stays fixed","while user navigates"]
FontStyle28 = x3d.FontStyle()
FontStyle28.justify = ["MIDDLE","MIDDLE"]
FontStyle28.size = 0.3

Text27.fontStyle = FontStyle28

Shape26.geometry = Text27
Appearance29 = x3d.Appearance()
Material30 = x3d.Material()
Material30.diffuseColor = [0.894118,0.819608,1]

Appearance29.material = Material30

Shape26.appearance = Appearance29

fieldValue25.children.append(Shape26)

ProtoInstance23.fieldValue.append(fieldValue25)

Scene15.children.append(ProtoInstance23)
Inline31 = x3d.Inline()
Inline31.url = ["../HelloWorld.x3d","http://X3dGraphics.com/examples/X3dForWebAuthors/HelloWorld.x3d","../HelloWorld.wrl","http://X3dGraphics.com/examples/X3dForWebAuthors/HelloWorld.wrl"]

Scene15.children.append(Inline31)

X3D0.Scene = Scene15
f = open("././HeadsUpDisplayExample_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
