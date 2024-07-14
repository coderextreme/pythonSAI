print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"
head1 = x3d.head()
component2 = x3d.component()
component2.name = "Geospatial"
component2.level = 1

head1.children.append(component2)
component3 = x3d.component()
component3.name = "NURBS"
component3.level = 2

head1.children.append(component3)
component4 = x3d.component()
component4.name = "Core"
component4.level = 2

head1.children.append(component4)
component5 = x3d.component()
component5.name = "Navigation"
component5.level = 1

head1.children.append(component5)
component6 = x3d.component()
component6.name = "Text"
component6.level = 1

head1.children.append(component6)
meta7 = x3d.meta()
meta7.name = "title"
meta7.content = "X3dHeaderPrototypeSyntaxExamples.x3d"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.name = "description"
meta8.content = "X3D scene header and prototype syntax examples. This example header indicates that the content is XML encoded, follows the Interactive Profile and explicitly lists additional necessary components. The X3D header may also contain additional semantic information. Used for specification EXAMPLE excerpts in 19776:1 XML Encoding."

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "created"
meta9.content = "14 October 2002"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "modified"
meta10.content = "27 May 2017"

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.name = "creator"
meta11.content = "Don Brutzman"

head1.children.append(meta11)
meta12 = x3d.meta()
meta12.name = "specificationSection"
meta12.content = "X3D encodings, ISO/IEC 19776-1.3, Part 1: XML encoding, 4.3 XML file syntax"

head1.children.append(meta12)
meta13 = x3d.meta()
meta13.name = "specificationUrl"
meta13.content = "https://www.web3d.org/documents/specifications/19776-1/V3.3/Part01/concepts.html#XMLFileSyntax"

head1.children.append(meta13)
meta14 = x3d.meta()
meta14.name = "identifier"
meta14.content = "https://www.web3d.org/x3d/content/examples/Basic/X3dSpecifications/X3dHeaderPrototypeSyntaxExamples.x3d"

head1.children.append(meta14)
meta15 = x3d.meta()
meta15.name = "generator"
meta15.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"

head1.children.append(meta15)
meta16 = x3d.meta()
meta16.name = "license"
meta16.content = "../license.html"

head1.children.append(meta16)

X3D0.head = head1
Scene17 = x3d.Scene()
ExternProtoDeclare18 = x3d.ExternProtoDeclare()
ExternProtoDeclare18.name = "ViewPositionOrientation"
ExternProtoDeclare18.url = ["../../Savage/Tools/Authoring/ViewPositionOrientationPrototype.x3d#ViewPositionOrientation","https://savage.nps.edu/Savage/Tools/Authoring/ViewPositionOrientationPrototype.x3d#ViewPositionOrientation","../../Savage/Tools/Authoring/ViewPositionOrientationPrototype.wrl#ViewPositionOrientation","https://savage.nps.edu/Savage/Tools/Authoring/ViewPositionOrientationPrototype.wrl#ViewPositionOrientation"]
field19 = x3d.field()
field19.name = "enabled"
field19.accessType = "inputOutput"
field19.type = "SFBool"

ExternProtoDeclare18.field.append(field19)
field20 = x3d.field()
field20.name = "traceEnabled"
field20.accessType = "initializeOnly"
field20.type = "SFBool"

ExternProtoDeclare18.field.append(field20)
field21 = x3d.field()
field21.name = "set_traceEnabled"
field21.accessType = "inputOnly"
field21.type = "SFBool"

ExternProtoDeclare18.field.append(field21)
field22 = x3d.field()
field22.name = "position_changed"
field22.accessType = "outputOnly"
field22.type = "SFVec3f"

ExternProtoDeclare18.field.append(field22)
field23 = x3d.field()
field23.name = "orientation_changed"
field23.accessType = "outputOnly"
field23.type = "SFRotation"

ExternProtoDeclare18.field.append(field23)
field24 = x3d.field()
field24.name = "outputViewpointString"
field24.accessType = "outputOnly"
field24.type = "MFString"

ExternProtoDeclare18.field.append(field24)

Scene17.children.append(ExternProtoDeclare18)
ProtoDeclare25 = x3d.ProtoDeclare()
ProtoDeclare25.name = "NewWorldInfoNode"
ProtoBody26 = x3d.ProtoBody()
WorldInfo27 = x3d.WorldInfo()
WorldInfo27.DEF = "ExamplePrototypeBody"

ProtoBody26.children.append(WorldInfo27)

ProtoDeclare25.ProtoBody = ProtoBody26

Scene17.children.append(ProtoDeclare25)
ProtoInstance28 = x3d.ProtoInstance()
ProtoInstance28.name = "NewWorldInfoNode"

Scene17.children.append(ProtoInstance28)
ProtoDeclare29 = x3d.ProtoDeclare()
ProtoDeclare29.name = "EmissiveMaterial"
ProtoInterface30 = x3d.ProtoInterface()
field31 = x3d.field()
field31.name = "onlyColor"
field31.accessType = "inputOutput"
field31.type = "SFColor"
field31.value = [1,0,0]

ProtoInterface30.field.append(field31)

ProtoDeclare29.ProtoInterface = ProtoInterface30
ProtoBody32 = x3d.ProtoBody()
#Override default diffuseColor value 0.8 0.8 0.8
Material33 = x3d.Material()
Material33.diffuseColor = [0,0,0]
#Connect emissiveColor field of current node to onlyColor field of parent ProtoDeclare.
IS34 = x3d.IS()
connect35 = x3d.connect()
connect35.nodeField = "emissiveColor"
connect35.protoField = "onlyColor"

IS34.connect.append(connect35)

Material33.IS = IS34

ProtoBody32.children.append(Material33)

ProtoDeclare29.ProtoBody = ProtoBody32

Scene17.children.append(ProtoDeclare29)
ProtoDeclare36 = x3d.ProtoDeclare()
ProtoDeclare36.name = "ShiftGroupUp2m"
ProtoInterface37 = x3d.ProtoInterface()
field38 = x3d.field()
field38.name = "children"
field38.accessType = "inputOutput"
field38.type = "MFNode"
Group39 = x3d.Group()
Group39.DEF = "DefaultNodeValue"
Group39.bboxSize = [2,2,2]
#Authors need to override this node when creating the ProtoInstance fieldValue name=\"children\"

field38.children.append(Group39)

ProtoInterface37.field.append(field38)

ProtoDeclare36.ProtoInterface = ProtoInterface37
ProtoBody40 = x3d.ProtoBody()
Transform41 = x3d.Transform()
Transform41.translation = [0,2,0]
Group42 = x3d.Group()
IS43 = x3d.IS()
connect44 = x3d.connect()
connect44.nodeField = "children"
connect44.protoField = "children"

IS43.connect.append(connect44)

Group42.IS = IS43

Transform41.children.append(Group42)

ProtoBody40.children.append(Transform41)

ProtoDeclare36.ProtoBody = ProtoBody40

Scene17.children.append(ProtoDeclare36)
ProtoInstance45 = x3d.ProtoInstance()
ProtoInstance45.name = "ShiftGroupUp2m"

Scene17.children.append(ProtoInstance45)
#====================
Viewpoint46 = x3d.Viewpoint()
Viewpoint46.DEF = "ExampleSingleElement"
Viewpoint46.description = "Hello syntax"

Scene17.children.append(Viewpoint46)
Group47 = x3d.Group()
Group47.DEF = "ExampleChildElement"
Shape48 = x3d.Shape()
Box49 = x3d.Box()

Shape48.geometry = Box49
Appearance50 = x3d.Appearance()
Material51 = x3d.Material()
Material51.diffuseColor = [0.6,0.4,0.2]

Appearance50.material = Material51

Shape48.appearance = Appearance50

Group47.children.append(Shape48)

Scene17.children.append(Group47)
Transform52 = x3d.Transform()
Transform52.DEF = "TransformExampleUSE"
Transform52.rotation = [0,1,0,0.78]
Transform52.translation = [0,2.5,0]
Group53 = x3d.Group()
Group53.USE = "ExampleChildElement"

Transform52.children.append(Group53)

Scene17.children.append(Transform52)
Collision54 = x3d.Collision()
Shape55 = x3d.Shape()
#note that Collision proxy Shape is not rendered
Sphere56 = x3d.Sphere()

Shape55.geometry = Sphere56
Appearance57 = x3d.Appearance()
Material58 = x3d.Material()

Appearance57.material = Material58

Shape55.appearance = Appearance57

Collision54.proxy = Shape55
Group59 = x3d.Group()
Group59.USE = "ExampleChildElement"

Collision54.proxy = Group59

Scene17.children.append(Collision54)
Transform60 = x3d.Transform()
Transform60.translation = [0,-2.5,0]
Shape61 = x3d.Shape()
Appearance62 = x3d.Appearance()
ProtoInstance63 = x3d.ProtoInstance()
ProtoInstance63.name = "EmissiveMaterial"
fieldValue64 = x3d.fieldValue()
fieldValue64.name = "onlyColor"
fieldValue64.value = "0.2 0.6 0.6"

ProtoInstance63.fieldValue.append(fieldValue64)

Appearance62.material = ProtoInstance63

Shape61.appearance = Appearance62
Text65 = x3d.Text()
Text65.string = ["X3D Header Prototype syntax examples","(view console for EXTERNPROTO output)"]
FontStyle66 = x3d.FontStyle()
FontStyle66.justify = ["MIDDLE","MIDDLE"]
FontStyle66.size = 0.6

Text65.fontStyle = FontStyle66

Shape61.geometry = Text65

Transform60.children.append(Shape61)

Scene17.children.append(Transform60)
ProtoInstance67 = x3d.ProtoInstance()
ProtoInstance67.name = "ViewPositionOrientation"
fieldValue68 = x3d.fieldValue()
fieldValue68.name = "enabled"
fieldValue68.value = "true"

ProtoInstance67.fieldValue.append(fieldValue68)

Scene17.children.append(ProtoInstance67)
TimeSensor69 = x3d.TimeSensor()
TimeSensor69.DEF = "Clock"
TimeSensor69.cycleInterval = 4
TimeSensor69.loop = True

Scene17.children.append(TimeSensor69)
OrientationInterpolator70 = x3d.OrientationInterpolator()
OrientationInterpolator70.DEF = "Spinner"
OrientationInterpolator70.key = [0,0.5,1]

Scene17.children.append(OrientationInterpolator70)
ROUTE71 = x3d.ROUTE()
ROUTE71.fromField = "fraction_changed"
ROUTE71.fromNode = "Clock"
ROUTE71.toField = "set_fraction"
ROUTE71.toNode = "Spinner"

Scene17.children.append(ROUTE71)
ROUTE72 = x3d.ROUTE()
ROUTE72.fromField = "value_changed"
ROUTE72.fromNode = "Spinner"
ROUTE72.toField = "rotation"
ROUTE72.toNode = "TransformExampleUSE"

Scene17.children.append(ROUTE72)
Inline73 = x3d.Inline()
Inline73.DEF = "someInline"
Inline73.url = ["someUrl.x3d","https://www.web3d.org/x3d/content/examples/Basic/X3dSpecifications/someUrl.x3d"]

Scene17.children.append(Inline73)
IMPORT74 = x3d.IMPORT()
IMPORT74.AS = "someInlineRoot"
IMPORT74.importedDEF = "someName"
IMPORT74.inlineDEF = "someInline"

Scene17.children.append(IMPORT74)
PositionInterpolator75 = x3d.PositionInterpolator()
PositionInterpolator75.DEF = "StayInPlace"
PositionInterpolator75.key = [0,1]

Scene17.children.append(PositionInterpolator75)
ROUTE76 = x3d.ROUTE()
ROUTE76.fromField = "fraction_changed"
ROUTE76.fromNode = "Clock"
ROUTE76.toField = "set_fraction"
ROUTE76.toNode = "StayInPlace"

Scene17.children.append(ROUTE76)
ROUTE77 = x3d.ROUTE()
ROUTE77.fromField = "value_changed"
ROUTE77.fromNode = "StayInPlace"
ROUTE77.toField = "set_translation"
ROUTE77.toNode = "someInlineRoot"

Scene17.children.append(ROUTE77)

X3D0.Scene = Scene17
f = open("././X3dHeaderPrototypeSyntaxExamples_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
