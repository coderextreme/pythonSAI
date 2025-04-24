print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.cssClass = "x3dModel.class"
X3D0.profile = "Full"
X3D0.style = "x3dModel.style"
X3D0.version = "4.0"
""" x3dVersionComparisonTest for this model: supportsX3dVersion(X3D.VERSION_3_0)=true """
head1 = x3d.head()
""" comment #1 """
""" comment #2 """
""" comment #3 """
""" comment #4 """
component2 = x3d.component()
component2.name = "Navigation"
component2.level = 3

head1.children.append(component2)
component3 = x3d.component()
component3.name = "Shaders"
component3.level = 1

head1.children.append(component3)
component4 = x3d.component()
component4.name = "CADGeometry"
component4.level = 2

head1.children.append(component4)
component5 = x3d.component()
component5.name = "DIS"
component5.level = 2

head1.children.append(component5)
component6 = x3d.component()
component6.name = "H-Anim"
component6.level = 1

head1.children.append(component6)
component7 = x3d.component()
component7.name = "Grouping"
component7.level = 1

head1.children.append(component7)
component8 = x3d.component()
component8.name = "Layering"
component8.level = 1

head1.children.append(component8)
unit9 = x3d.unit()
unit9.name = "AngleUnitConversion"
unit9.category = "angle"
unit9.conversionFactor = 1.0

head1.children.append(unit9)
unit10 = x3d.unit()
unit10.name = "LengthUnitConversion"
unit10.category = "length"
unit10.conversionFactor = 1.0

head1.children.append(unit10)
unit11 = x3d.unit()
unit11.name = "ForceFromPoundsToNewtons"
unit11.category = "force"
unit11.conversionFactor = 4.4482

head1.children.append(unit11)
meta12 = x3d.meta()
meta12.content = "HelloWorldProgramOutput.x3d"
meta12.name = "title"

head1.children.append(meta12)
meta13 = x3d.meta()
meta13.content = "continued development and testing in progress"
meta13.name = "info"

head1.children.append(meta13)
meta14 = x3d.meta()
meta14.content = "Example HelloWorldProgram creates an X3D model using the X3D Java Scene Access Interface Library (X3DJSAIL)"
meta14.name = "description"

head1.children.append(meta14)
meta15 = x3d.meta()
meta15.content = "https://www.web3d.org/specifications/java/X3DJSAIL.html"
meta15.name = "reference"

head1.children.append(meta15)
meta16 = x3d.meta()
meta16.content = "HelloWorldProgramOutput.java"
meta16.name = "generator"

head1.children.append(meta16)
meta17 = x3d.meta()
meta17.content = "6 September 2016"
meta17.name = "created"

head1.children.append(meta17)
meta18 = x3d.meta()
meta18.content = "29 April 2023"
meta18.name = "modified"

head1.children.append(meta18)
meta19 = x3d.meta()
meta19.content = "X3D Java Scene Access Interface Library (X3DJSAIL)"
meta19.name = "generator"

head1.children.append(meta19)
meta20 = x3d.meta()
meta20.content = "https://www.web3d.org/specifications/java/examples/HelloWorldProgram.java"
meta20.name = "generator"

head1.children.append(meta20)
meta21 = x3d.meta()
meta21.content = "Netbeans https://www.netbeans.org"
meta21.name = "generator"

head1.children.append(meta21)
meta22 = x3d.meta()
meta22.content = "Don Brutzman"
meta22.name = "creator"

head1.children.append(meta22)
meta23 = x3d.meta()
meta23.content = "https://sourceforge.net/p/x3d/code/HEAD/tree/www.web3d.org/x3d/stylesheets/java/examples/HelloWorldProgramOutput.x3d"
meta23.name = "reference"

head1.children.append(meta23)
meta24 = x3d.meta()
meta24.content = "Console output, ClassicVRML encoding, VRML97 encoding and pretty-print documentation:"
meta24.name = "reference"

head1.children.append(meta24)
meta25 = x3d.meta()
meta25.content = "HelloWorldProgramOutput.txt"
meta25.name = "reference"

head1.children.append(meta25)
meta26 = x3d.meta()
meta26.content = "HelloWorldProgramOutput.x3dv"
meta26.name = "reference"

head1.children.append(meta26)
meta27 = x3d.meta()
meta27.content = "HelloWorldProgramOutput.wrl"
meta27.name = "reference"

head1.children.append(meta27)
meta28 = x3d.meta()
meta28.content = "HelloWorldProgramOutput.html"
meta28.name = "reference"

head1.children.append(meta28)
meta29 = x3d.meta()
meta29.content = "https://savage.nps.edu/X3dValidator?url=https://www.web3d.org/specifications/java/examples/HelloWorldProgramOutput.x3d"
meta29.name = "reference"

head1.children.append(meta29)
meta30 = x3d.meta()
meta30.content = "https://www.web3d.org/specifications/java/examples/HelloWorldProgramOutput.x3d"
meta30.name = "identifier"

head1.children.append(meta30)
meta31 = x3d.meta()
meta31.content = "../license.html"
meta31.name = "license"

head1.children.append(meta31)

X3D0.head = head1
Scene32 = x3d.Scene()
MetadataSet33 = x3d.MetadataSet()
MetadataSet33.name = "topLevelSceneMetadata"

Scene32.children.append(MetadataSet33)
ViewpointGroup34 = x3d.ViewpointGroup()
ViewpointGroup34.description = "Available viewpoints"
Viewpoint35 = x3d.Viewpoint()
Viewpoint35.DEF = "DefaultView"
Viewpoint35.description = "Hello X3DJSAIL"

ViewpointGroup34.children.append(Viewpoint35)
Viewpoint36 = x3d.Viewpoint()
Viewpoint36.DEF = "TopDownView"
Viewpoint36.description = "top-down view from above"
Viewpoint36.orientation = [1,0,0,-1.570796]
Viewpoint36.position = [0,100,0]

ViewpointGroup34.children.append(Viewpoint36)

Scene32.children.append(ViewpointGroup34)
NavigationInfo37 = x3d.NavigationInfo()
NavigationInfo37.avatarSize = [0.25,1.6,0.75]
NavigationInfo37.transitionType = ["LINEAR"]
NavigationInfo37.type = ["EXAMINE","FLY","ANY"]

Scene32.children.append(NavigationInfo37)
WorldInfo38 = x3d.WorldInfo()
WorldInfo38.DEF = "WorldInfoDEF"
WorldInfo38.cssClass = "worldInfoNode.class"
WorldInfo38.style = "worldInfoNode.style"
WorldInfo38.title = "HelloWorldProgram produced by X3D Java SAI Library (X3DJSAIL)"

Scene32.children.append(WorldInfo38)
WorldInfo39 = x3d.WorldInfo()
WorldInfo39.USE = "WorldInfoDEF"

Scene32.children.append(WorldInfo39)
WorldInfo40 = x3d.WorldInfo()
WorldInfo40.USE = "WorldInfoDEF"

Scene32.children.append(WorldInfo40)
MetadataString41 = x3d.MetadataString()
MetadataString41.DEF = "scene.addChildMetadata"
MetadataString41.name = "test"
MetadataString41.value = ["Top-level root Metadata node beneath Scene needs to be one of '-children' in JSON encoding"]

Scene32.metadata = MetadataString41
LayerSet42 = x3d.LayerSet()
LayerSet42.DEF = "scene.addChildLayerSetTest"
LayerSet42.order = [0]

Scene32.layerSet = LayerSet42
Transform43 = x3d.Transform()
Transform43.DEF = "LogoGeometryTransform"
Transform43.translation = [0,1.5,0]
Anchor44 = x3d.Anchor()
Anchor44.DEF = "siteAnchor"
Anchor44.description = "select for X3D Java SAI Library (X3DJSAIL) description"
Anchor44.url = ["../X3DJSAIL.html","https://www.web3d.org/specifications/java/X3DJSAIL.html"]
Shape45 = x3d.Shape()
Shape45.DEF = "BoxShape"
Appearance46 = x3d.Appearance()
Material47 = x3d.Material()
Material47.DEF = "GreenMaterial"
Material47.diffuseColor = [0,1,1]
Material47.emissiveColor = [0.8,0,0]
Material47.transparency = 0.1

Appearance46.material = Material47
ImageTexture48 = x3d.ImageTexture()
ImageTexture48.url = ["images/X3dJavaSceneAccessInterfaceSaiLibrary.png","https://www.web3d.org/specifications/java/examples/images/X3dJavaSceneAccessInterfaceSaiLibrary.png"]

Appearance46.texture = ImageTexture48

Shape45.appearance = Appearance46
Box49 = x3d.Box()
Box49.DEF = "test-NMTOKEN_regex.0123456789"
Box49.cssClass = "untextured"

Shape45.geometry = Box49

Anchor44.children.append(Shape45)

Transform43.children.append(Anchor44)

Scene32.children.append(Transform43)
Shape50 = x3d.Shape()
Shape50.DEF = "LineShape"
Appearance51 = x3d.Appearance()
Material52 = x3d.Material()
Material52.emissiveColor = [0.6,0.19607843,0.8]

Appearance51.material = Material52

Shape50.appearance = Appearance51
IndexedLineSet53 = x3d.IndexedLineSet()
IndexedLineSet53.coordIndex = [0,1,2,3,4,0]
""" Coordinate 3-tuple point count: 6 """
Coordinate54 = x3d.Coordinate()

IndexedLineSet53.coord = Coordinate54

Shape50.geometry = IndexedLineSet53

Scene32.children.append(Shape50)
PositionInterpolator55 = x3d.PositionInterpolator()
PositionInterpolator55.DEF = "BoxPathAnimator"
PositionInterpolator55.key = [0,0.125,0.375,0.625,0.875,1]

Scene32.children.append(PositionInterpolator55)
TimeSensor56 = x3d.TimeSensor()
TimeSensor56.DEF = "OrbitClock"
TimeSensor56.cycleInterval = 8.0
TimeSensor56.loop = True

Scene32.children.append(TimeSensor56)
ROUTE57 = x3d.ROUTE()
ROUTE57.fromField = "fraction_changed"
ROUTE57.fromNode = "OrbitClock"
ROUTE57.toField = "set_fraction"
ROUTE57.toNode = "BoxPathAnimator"

Scene32.children.append(ROUTE57)
ROUTE58 = x3d.ROUTE()
ROUTE58.fromField = "value_changed"
ROUTE58.fromNode = "BoxPathAnimator"
ROUTE58.toField = "set_translation"
ROUTE58.toNode = "LogoGeometryTransform"

Scene32.children.append(ROUTE58)
Transform59 = x3d.Transform()
Transform59.DEF = "TextTransform"
Transform59.translation = [0,-1.5,0]
Shape60 = x3d.Shape()
Appearance61 = x3d.Appearance()
Material62 = x3d.Material()
Material62.USE = "GreenMaterial"

Appearance61.material = Material62

Shape60.appearance = Appearance61
Text63 = x3d.Text()
Text63.string = ["X3D Java","SAI Library","X3DJSAIL"]
""" Comment example A, plain quotation marks: He said, \"Immel did it!\" """
""" Comment example B, XML character entities: He said, &quot;Immel did it!&quot; """
MetadataSet64 = x3d.MetadataSet()
MetadataSet64.name = "EscapedQuotationMarksMetadataSet"
MetadataString65 = x3d.MetadataString()
MetadataString65.name = "quotesTestC"
MetadataString65.value = ["MFString example C, backslash-escaped quotes: He said, \"Immel did it!\""]

if MetadataSet64.value is None:
    MetadataSet64.value = []
MetadataSet64.value.append(MetadataString65)
MetadataString66 = x3d.MetadataString()
MetadataString66.name = "extraChildTest"
MetadataString66.value = ["checks MetadataSet addValue() method"]

if MetadataSet64.value is None:
    MetadataSet64.value = []
MetadataSet64.value.append(MetadataString66)

Text63.metadata = MetadataSet64
FontStyle67 = x3d.FontStyle()
FontStyle67.family = ["SERIF"]
FontStyle67.justify = ["MIDDLE","MIDDLE"]

Text63.fontStyle = FontStyle67

Shape60.geometry = Text63

Transform59.children.append(Shape60)
Collision68 = x3d.Collision()
""" test containerField='proxy' """
Shape69 = x3d.Shape()
Shape69.DEF = "ProxyShape"
""" alternative XML encoding: Text string='\"One, Two, Comment\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\"' """
""" alternative XML encoding: Text string='\"One, Two, Comment\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\" \"\"' """
""" alternative Java source: .setString(new String [] {\"One, Two, Comment\", \"\", \"He said, \\\"Immel did it!\\\"\"}) """
""" reference: https://www.web3d.org/x3d/content/examples/Basic/X3dSpecifications/StringArrayEncodingExamplesIndex.html """
Text70 = x3d.Text()
Text70.string = ["One, Two, Text","","He said, \"Immel did it!\" \"\""]

Shape69.geometry = Text70

Collision68.proxy = Shape69

Transform59.children.append(Collision68)
""" It's a beautiful world """
""" ... for you! """
""" https://en.wikipedia.org/wiki/Beautiful_World_(Devo_song) """

Scene32.children.append(Transform59)
""" repeatedly spin 180 degrees as a readable special effect """
OrientationInterpolator71 = x3d.OrientationInterpolator()
OrientationInterpolator71.DEF = "SpinInterpolator"
OrientationInterpolator71.key = [0,0.5,1]

Scene32.children.append(OrientationInterpolator71)
TimeSensor72 = x3d.TimeSensor()
TimeSensor72.DEF = "SpinClock"
TimeSensor72.cycleInterval = 5.0
TimeSensor72.loop = True

Scene32.children.append(TimeSensor72)
ROUTE73 = x3d.ROUTE()
ROUTE73.fromField = "fraction_changed"
ROUTE73.fromNode = "SpinClock"
ROUTE73.toField = "set_fraction"
ROUTE73.toNode = "SpinInterpolator"

Scene32.children.append(ROUTE73)
ROUTE74 = x3d.ROUTE()
ROUTE74.fromField = "value_changed"
ROUTE74.fromNode = "SpinInterpolator"
ROUTE74.toField = "rotation"
ROUTE74.toNode = "TextTransform"

Scene32.children.append(ROUTE74)
Group75 = x3d.Group()
Group75.DEF = "BackgroundGroup"
Background76 = x3d.Background()
Background76.DEF = "GradualBackground"

Group75.children.append(Background76)
Script77 = x3d.Script()
Script77.DEF = "colorTypeConversionScript"
field78 = x3d.field()
field78.name = "colorInput"
field78.accessType = "inputOnly"
field78.type = "SFColor"

Script77.field.append(field78)
field79 = x3d.field()
field79.name = "colorsOutput"
field79.accessType = "outputOnly"
field79.type = "MFColor"

Script77.field.append(field79)

Script77.sourceCode = '''\n"+
"ecmascript:\n"+
"\n"+
"function colorInput (eventValue) // Example source code\n"+
"{\n"+
"   colorsOutput = new MFColor(eventValue); // assigning value sends output event\n"+
"// Browser.print('colorInput=' + eventValue + ', colorsOutput=' + colorsOutput + '\\n');\n"+
"}\n"+
"'''

Group75.children.append(Script77)
ColorInterpolator80 = x3d.ColorInterpolator()
ColorInterpolator80.DEF = "ColorAnimator"
ColorInterpolator80.key = [0,0.5,1]
""" AZURE to INDIGO and back again """

Group75.children.append(ColorInterpolator80)
TimeSensor81 = x3d.TimeSensor()
TimeSensor81.DEF = "ColorClock"
TimeSensor81.cycleInterval = 60.0
TimeSensor81.loop = True

Group75.children.append(TimeSensor81)
ROUTE82 = x3d.ROUTE()
ROUTE82.fromField = "colorsOutput"
ROUTE82.fromNode = "colorTypeConversionScript"
ROUTE82.toField = "skyColor"
ROUTE82.toNode = "GradualBackground"

Group75.children.append(ROUTE82)
ROUTE83 = x3d.ROUTE()
ROUTE83.fromField = "value_changed"
ROUTE83.fromNode = "ColorAnimator"
ROUTE83.toField = "colorInput"
ROUTE83.toNode = "colorTypeConversionScript"

Group75.children.append(ROUTE83)
ROUTE84 = x3d.ROUTE()
ROUTE84.fromField = "fraction_changed"
ROUTE84.fromNode = "ColorClock"
ROUTE84.toField = "set_fraction"
ROUTE84.toNode = "ColorAnimator"

Group75.children.append(ROUTE84)

Scene32.children.append(Group75)
ProtoDeclare85 = x3d.ProtoDeclare()
ProtoDeclare85.name = "ArtDeco01Material"
ProtoDeclare85.appinfo = "tooltip: ArtDeco01Material prototype is a Material node"
ProtoInterface86 = x3d.ProtoInterface()
field87 = x3d.field()
field87.name = "description"
field87.accessType = "inputOutput"
field87.appinfo = "tooltip for descriptionField"
field87.type = "SFString"
field87.value = "ArtDeco01Material prototype is a Material node"

ProtoInterface86.field.append(field87)
field88 = x3d.field()
field88.name = "enabled"
field88.accessType = "inputOutput"
field88.type = "SFBool"
field88.value = True

ProtoInterface86.field.append(field88)

ProtoDeclare85.ProtoInterface = ProtoInterface86
ProtoBody89 = x3d.ProtoBody()
""" Initial node of ProtoBody determines prototype node type """
Material90 = x3d.Material()
Material90.ambientIntensity = 0.25
Material90.diffuseColor = [0.282435,0.085159,0.134462]
Material90.shininess = 0.127273
Material90.specularColor = [0.276305,0.11431,0.139857]

ProtoBody89.children.append(Material90)
""" [HelloWorldProgram diagnostic] should be connected to scene graph: artDeco01ProtoDeclare.getNodeType()=\"Material\" """
""" presence of follow-on TouchSensor shows that additional nodes are allowed in ProtoBody after initial node, regardless of node types """
TouchSensor91 = x3d.TouchSensor()
TouchSensor91.description = "within ProtoBody"
IS92 = x3d.IS()
connect93 = x3d.connect()
connect93.nodeField = "description"
connect93.protoField = "description"

IS92.connect.append(connect93)
connect94 = x3d.connect()
connect94.nodeField = "enabled"
connect94.protoField = "enabled"

IS92.connect.append(connect94)

TouchSensor91.IS = IS92

ProtoBody89.children.append(TouchSensor91)

ProtoDeclare85.ProtoBody = ProtoBody89

Scene32.children.append(ProtoDeclare85)
ExternProtoDeclare95 = x3d.ExternProtoDeclare()
ExternProtoDeclare95.name = "ArtDeco02Material"
ExternProtoDeclare95.appinfo = "this is a different Material node"
ExternProtoDeclare95.url = ["https://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3d#ArtDeco02Material","https://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3dv#ArtDeco02Material"]
""" [HelloWorldProgram diagnostic] artDeco02ExternProtoDeclare.getNodeType()=\"ERROR_UNKNOWN_EXTERNPROTODECLARE_NODE_TYPE: ExternProtoDeclare name='ArtDeco02Material' type cannot be remotely accessed at run time. TODO X3DJSAIL needs to add further capability that retrieves the ExternProtoDeclare file.\" """
field96 = x3d.field()
field96.name = "description"
field96.accessType = "inputOutput"
field96.appinfo = "tooltip for descriptionField"
field96.type = "SFString"

ExternProtoDeclare95.field.append(field96)

Scene32.children.append(ExternProtoDeclare95)
""" Tested ArtDeco01ProtoInstance, ArtDeco02ProtoInstance for improper node type when ProtoInstance is added in wrong place """
Shape97 = x3d.Shape()
Shape97.DEF = "TestShape1"
Appearance98 = x3d.Appearance()
Appearance98.DEF = "TestAppearance1"
""" ArtDeco01Material prototype goes here... TODO ensure setContainerField is handled in exported Java """
ProtoInstance99 = x3d.ProtoInstance()
ProtoInstance99.name = "ArtDeco01Material"
""" [HelloWorldProgram diagnostic] ArtDeco01ProtoInstance.getNodeType()=\"Material\" """
fieldValue100 = x3d.fieldValue()
fieldValue100.name = "description"
fieldValue100.value = "ArtDeco01Material can substitute for a Material node"

ProtoInstance99.fieldValue.append(fieldValue100)

Appearance98.material = ProtoInstance99

Shape97.appearance = Appearance98
Sphere101 = x3d.Sphere()
Sphere101.radius = 0.001

Shape97.geometry = Sphere101

Scene32.children.append(Shape97)
Shape102 = x3d.Shape()
Shape102.DEF = "TestShape2"
Appearance103 = x3d.Appearance()
Appearance103.DEF = "TestAppearance2"
""" ArtDeco02Material prototype goes here... TODO ensure setContainerField is handled in exported Java """
ProtoInstance104 = x3d.ProtoInstance()
ProtoInstance104.DEF = "ArtDeco02MaterialDEF"
ProtoInstance104.name = "ArtDeco02Material"
""" [HelloWorldProgram diagnostic] ArtDeco02ProtoInstance.getNodeType()=\"ERROR_UNKNOWN_EXTERNPROTODECLARE_NODE_TYPE: ExternProtoDeclare name='ArtDeco02Material' type cannot be remotely accessed at run time. TODO X3DJSAIL needs to add further capability that retrieves the ExternProtoDeclare file.\" """
fieldValue105 = x3d.fieldValue()
fieldValue105.name = "description"
fieldValue105.value = "ArtDeco02Material can substitute for another Material node"

ProtoInstance104.fieldValue.append(fieldValue105)

Appearance103.material = ProtoInstance104

Shape102.appearance = Appearance103
Cone106 = x3d.Cone()
Cone106.bottomRadius = 0.001
Cone106.height = 0.001

Shape102.geometry = Cone106

Scene32.children.append(Shape102)
Shape107 = x3d.Shape()
Shape107.DEF = "TestShape3"
Appearance108 = x3d.Appearance()
Appearance108.DEF = "TestAppearance3"
""" ArtDeco02Material ProtoInstance USE goes here. Note that name field is NOT defined as part of ProtoInstance USE. """
ProtoInstance109 = x3d.ProtoInstance()
ProtoInstance109.USE = "ArtDeco02MaterialDEF"

Appearance108.material = ProtoInstance109

Shape107.appearance = Appearance108
Cylinder110 = x3d.Cylinder()
Cylinder110.height = 0.001
Cylinder110.radius = 0.001

Shape107.geometry = Cylinder110

Scene32.children.append(Shape107)
Inline111 = x3d.Inline()
Inline111.DEF = "inlineScene"
Inline111.url = ["someOtherScene.x3d","https://www.web3d.org/specifications/java/examples/someOtherScene.x3d"]

Scene32.children.append(Inline111)
IMPORT112 = x3d.IMPORT()
IMPORT112.AS = "WorldInfoDEF2"
IMPORT112.importedDEF = "WorldInfoDEF"
IMPORT112.inlineDEF = "inlineScene"

Scene32.children.append(IMPORT112)
EXPORT113 = x3d.EXPORT()
EXPORT113.AS = "WorldInfoDEF3"
EXPORT113.localDEF = "WorldInfoDEF"

Scene32.children.append(EXPORT113)
ProtoDeclare114 = x3d.ProtoDeclare()
ProtoDeclare114.name = "MaterialModulator"
ProtoDeclare114.appinfo = "mimic a Material node and modulate fields as an animation effect"
ProtoDeclare114.documentation = "https://x3dgraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/MaterialModulatorIndex.html"
ProtoInterface115 = x3d.ProtoInterface()
field116 = x3d.field()
field116.name = "enabled"
field116.accessType = "inputOutput"
field116.type = "SFBool"
field116.value = True

ProtoInterface115.field.append(field116)
field117 = x3d.field()
field117.name = "diffuseColor"
field117.accessType = "inputOutput"
field117.type = "SFColor"
field117.value = [0,0,0]

ProtoInterface115.field.append(field117)
field118 = x3d.field()
field118.name = "emissiveColor"
field118.accessType = "inputOutput"
field118.type = "SFColor"
field118.value = [0.05,0.05,0.5]

ProtoInterface115.field.append(field118)
field119 = x3d.field()
field119.name = "specularColor"
field119.accessType = "inputOutput"
field119.type = "SFColor"
field119.value = [0,0,0]

ProtoInterface115.field.append(field119)
field120 = x3d.field()
field120.name = "transparency"
field120.accessType = "inputOutput"
field120.type = "SFFloat"
field120.value = 0.0

ProtoInterface115.field.append(field120)
field121 = x3d.field()
field121.name = "shininess"
field121.accessType = "inputOutput"
field121.type = "SFFloat"
field121.value = 0.0

ProtoInterface115.field.append(field121)
field122 = x3d.field()
field122.name = "ambientIntensity"
field122.accessType = "inputOutput"
field122.type = "SFFloat"
field122.value = 0.0

ProtoInterface115.field.append(field122)

ProtoDeclare114.ProtoInterface = ProtoInterface115
ProtoBody123 = x3d.ProtoBody()
Material124 = x3d.Material()
Material124.DEF = "MaterialNode"
IS125 = x3d.IS()
connect126 = x3d.connect()
connect126.nodeField = "diffuseColor"
connect126.protoField = "diffuseColor"

IS125.connect.append(connect126)
connect127 = x3d.connect()
connect127.nodeField = "emissiveColor"
connect127.protoField = "emissiveColor"

IS125.connect.append(connect127)
connect128 = x3d.connect()
connect128.nodeField = "specularColor"
connect128.protoField = "specularColor"

IS125.connect.append(connect128)
connect129 = x3d.connect()
connect129.nodeField = "transparency"
connect129.protoField = "transparency"

IS125.connect.append(connect129)
connect130 = x3d.connect()
connect130.nodeField = "shininess"
connect130.protoField = "shininess"

IS125.connect.append(connect130)
connect131 = x3d.connect()
connect131.nodeField = "ambientIntensity"
connect131.protoField = "ambientIntensity"

IS125.connect.append(connect131)

Material124.IS = IS125

ProtoBody123.children.append(Material124)
""" Only first node (the node type) is renderable, others are along for the ride """
Script132 = x3d.Script()
Script132.DEF = "MaterialModulatorScript"
field133 = x3d.field()
field133.name = "enabled"
field133.accessType = "inputOutput"
field133.type = "SFBool"

Script132.field.append(field133)
field134 = x3d.field()
field134.name = "diffuseColor"
field134.accessType = "inputOutput"
field134.type = "SFColor"

Script132.field.append(field134)
field135 = x3d.field()
field135.name = "newColor"
field135.accessType = "outputOnly"
field135.type = "SFColor"

Script132.field.append(field135)
field136 = x3d.field()
field136.name = "clockTrigger"
field136.accessType = "inputOnly"
field136.type = "SFTime"

Script132.field.append(field136)
IS137 = x3d.IS()
connect138 = x3d.connect()
connect138.nodeField = "enabled"
connect138.protoField = "enabled"

IS137.connect.append(connect138)
connect139 = x3d.connect()
connect139.nodeField = "diffuseColor"
connect139.protoField = "diffuseColor"

IS137.connect.append(connect139)

Script132.IS = IS137

Script132.sourceCode = '''\n"+
"ecmascript:\n"+
"function initialize ()\n"+
"{\n"+
"    newColor = diffuseColor; // start with correct color\n"+
"}\n"+
"function set_enabled (newValue)\n"+
"{\n"+
"	enabled = newValue;\n"+
"}\n"+
"function clockTrigger (timeValue)\n"+
"{\n"+
"    if (!enabled) return;\n"+
"    red   = newColor.r;\n"+
"    green = newColor.g;\n"+
"    blue  = newColor.b;\n"+
"    \n"+
"    // note different modulation rates for each color component, % is modulus operator\n"+
"    newColor = new SFColor ((red + 0.02) % 1, (green + 0.03) % 1, (blue + 0.04) % 1);\n"+
"	if (enabled)\n"+
"	{\n"+
"		Browser.print ('diffuseColor=(' + red + ',' + green + ',' + blue + ') newColor=' + newColor.toString() + '\\n');\n"+
"	}\n"+
"}\n"+
"'''

ProtoBody123.children.append(Script132)

ProtoDeclare114.ProtoBody = ProtoBody123

Scene32.children.append(ProtoDeclare114)
""" Test success: declarative statement createDeclarativeShapeTests() """
Group140 = x3d.Group()
Group140.DEF = "DeclarativeGroupExample"
Shape141 = x3d.Shape()
MetadataString142 = x3d.MetadataString()
MetadataString142.DEF = "FindableMetadataStringTest"
MetadataString142.name = "findThisNameValue"
MetadataString142.value = ["test case"]

Shape141.metadata = MetadataString142
Appearance143 = x3d.Appearance()
Appearance143.DEF = "DeclarativeAppearanceExample"
""" DeclarativeMaterialExample gets overridden by subsequently added MaterialModulator ProtoInstance """
ProtoInstance144 = x3d.ProtoInstance()
ProtoInstance144.DEF = "MyMaterialModulator"
ProtoInstance144.name = "MaterialModulator"

Appearance143.material = ProtoInstance144

Shape141.appearance = Appearance143
Cone145 = x3d.Cone()
Cone145.bottom = False
Cone145.bottomRadius = 0.05
Cone145.height = 0.1

Shape141.geometry = Cone145

Group140.children.append(Shape141)
""" Test success: declarativeGroup.addChild() singleton pipeline method """

Scene32.children.append(Group140)
""" Test success: declarative statement addChild() """
""" Test success: x3dModel.findNodeByDEF(DeclarativeAppearanceExample) = <Appearance DEF='DeclarativeAppearanceExample'/> i.e. <Appearance DEF='DeclarativeAppearanceExample'> <!- - DeclarativeMaterialExample gets overridden by subsequently added MaterialModulator ProtoInstance - -> <ProtoInstance DEF='MyMaterialModulator' name='MaterialModulator' containerField='material'/> </Appearance> """
""" Test success: x3dModel.findElementByNameValue(findThisNameValue) = <MetadataString DEF='FindableMetadataStringTest' name='findThisNameValue' value='\"test case\"'/> """
""" Test success: x3dModel.findElementByNameValue(\"ArtDeco01Material\", \"ProtoDeclare\") found """
""" Test success: x3dModel.findElementByNameValue(\"MaterialModulator\", \"ProtoDeclare\") found """
""" Test success: x3dModel.findElementByNameValue(\"MaterialModulator\", \"ProtoInstance\") found """
Group146 = x3d.Group()
Group146.DEF = "TestFieldObjectsGroup"
""" testFieldObjects() results """
""" SFBool default=false, true=true, false=false, negate()=true """
""" MFBool default=, initial=true false true, negate()=false true false """
""" SFFloat default=0.0, initial=1.0, setValue(2)=2.0, setValue(3.0f)=3.0, setValue(4.0)=4.0 """
""" MFFloat default=, initial=1 2 3, append(5)=1 2 3 5, inserts(3,4)(0,0)=0 1 2 3 4 5, append(6)=0 1 2 3 4 5 6, size()=7 """
""" ... get1Value[3]=3.0, remove[1]=0 2 3 4 5 6, set1Value(0,10)=10 2 3 4 5 6, multiply(2)=20 4 6 8 10 12, clear= """
""" SFVec3f default=0 0 0, initial=1 2 3, setValue=4 5 6, multiply(2)=8 10 12, normalize()=0.45584232 0.5698029 0.68376344, regex matches()=true """
""" regex test SFVec3f().matches(\"1 2 3\")=true, regex test SFVec3f().matches(\"1 2 3 4\")=false, regex test (SFRotation.matches(\"0 0 0 0\")=true, failure detecting illegal (zero axis) rotation value """

Scene32.children.append(Group146)
Sound147 = x3d.Sound()
Sound147.location = [0,1.6,0]
""" set sound-ellipsoid location height at 1.6m to match typical avatar height """
AudioClip148 = x3d.AudioClip()
AudioClip148.description = "chimes"
AudioClip148.url = ["chimes.wav","https://www.web3d.org/x3d/content/examples/ConformanceNist/Sounds/AudioClip/chimes.wav"]
""" Scene example fragment from https://www.web3d.org/x3d/content/examples/ConformanceNist/Sounds/AudioClip/default.x3d """

Sound147.source = AudioClip148

Scene32.children.append(Sound147)
Sound149 = x3d.Sound()
Sound149.location = [0,1.6,0]
""" set sound-ellipsoid location height at 1.6m to match typical avatar height """
MovieTexture150 = x3d.MovieTexture()
MovieTexture150.description = "mpgsys.mpg from ConformanceNist suite"
MovieTexture150.url = ["mpgsys.mpg","https://www.web3d.org/x3d/content/examples/ConformanceNist/Appearance/MovieTexture/mpgsys.mpg"]
""" Scene example fragment from https://www.web3d.org/x3d/content/examples/ConformanceNist/Appearance/MovieTexture/mpeg1-systems.x3d """
""" Expected containerField='source', allowed containerField values=\"texture\" \"source\" \"back\" \"bottom\" \"front\" \"left\" \"right\" \"top\" \"backTexture\" \"bottomTexture\" \"frontTexture\" \"leftTexture\" \"rightTexture\" \"topTexture\" \"children\" """

Sound149.source = MovieTexture150

Scene32.children.append(Sound149)
""" Test success: Anchor.isNode()=true, siteAnchor.isNode()=true """
""" Test success: Anchor.isStatement()=false, siteAnchor.isStatement()=false """
""" Test success: ROUTE.isNode()=false, orbitPositionROUTE.isNode()=false """
""" Test success: ROUTE.isStatement()=true, orbitPositionROUTE.isStatement()=true """
""" Test success: CommentsBlock.isNode()=false, testComments.isNode()=false """
""" Test failure: CommentsBlock.isStatement()=true, testComments.isStatement()=true """
Shape151 = x3d.Shape()
Shape151.DEF = "ExtrusionShape"
""" ExampleExtrusion isCrossSectionClosed()=true, crossSection='[1.0, 1.0, 1.0, -1.0, -1.0, -1.0, -1.0, 1.0, 1.0, 1.0]' """
""" ExampleExtrusion isSpineClosed()=false, spine='[0.0, 0.0, 0.0, 0.0, 1.0, 0.0]' """
Appearance152 = x3d.Appearance()
Appearance152.DEF = "TransparentAppearance"
Material153 = x3d.Material()
Material153.transparency = 1.0

Appearance152.material = Material153

Shape151.appearance = Appearance152
Extrusion154 = x3d.Extrusion()
Extrusion154.DEF = "ExampleExtrusion"

Shape151.geometry = Extrusion154

Scene32.children.append(Shape151)
Group155 = x3d.Group()
""" Test MFNode children array as an ordered list consisting of comments, statements, ProtoInstance and nodes """
ProtoDeclare156 = x3d.ProtoDeclare()
ProtoDeclare156.name = "NewWorldInfo"
ProtoInterface157 = x3d.ProtoInterface()
field158 = x3d.field()
field158.name = "description"
field158.accessType = "initializeOnly"
field158.type = "SFString"

ProtoInterface157.field.append(field158)

ProtoDeclare156.ProtoInterface = ProtoInterface157
ProtoBody159 = x3d.ProtoBody()
WorldInfo160 = x3d.WorldInfo()

ProtoBody159.children.append(WorldInfo160)

ProtoDeclare156.ProtoBody = ProtoBody159

Group155.children.append(ProtoDeclare156)
ProtoInstance161 = x3d.ProtoInstance()
ProtoInstance161.DEF = "Proto1"
ProtoInstance161.name = "NewWorldInfo"
fieldValue162 = x3d.fieldValue()
fieldValue162.name = "description"
fieldValue162.value = "testing 1 2 3"

ProtoInstance161.fieldValue.append(fieldValue162)

Group155.children.append(ProtoInstance161)
Group163 = x3d.Group()
Group163.DEF = "Node2"
""" intentionally empty """

Group155.children.append(Group163)
ProtoInstance164 = x3d.ProtoInstance()
ProtoInstance164.DEF = "Proto3"
ProtoInstance164.name = "NewWorldInfo"

Group155.children.append(ProtoInstance164)
Transform165 = x3d.Transform()
Transform165.DEF = "Node4"
""" intentionally empty """

Group155.children.append(Transform165)
""" Test satisfactorily creates MFNode children array as an ordered list with mixed content """

Scene32.children.append(Group155)
ProtoDeclare166 = x3d.ProtoDeclare()
ProtoDeclare166.name = "ShaderProto"
ProtoBody167 = x3d.ProtoBody()
ProgramShader168 = x3d.ProgramShader()

ProtoBody167.children.append(ProgramShader168)

ProtoDeclare166.ProtoBody = ProtoBody167

Scene32.children.append(ProtoDeclare166)
Shape169 = x3d.Shape()
Appearance170 = x3d.Appearance()
""" Test MFNode shaders array as an ordered list consisting of comments, ProtoInstance and nodes """
""" Test satisfactorily creates MFNode shaders array as an ordered list with mixed content """
ProgramShader171 = x3d.ProgramShader()
ProgramShader171.DEF = "TestShader1"
ShaderProgram172 = x3d.ShaderProgram()
ShaderProgram172.DEF = "TestShader2"

ProgramShader171.programs.append(ShaderProgram172)

Appearance170.shaders.append(ProgramShader171)
ProtoInstance173 = x3d.ProtoInstance()
ProtoInstance173.DEF = "TestShader3"
ProtoInstance173.name = "ShaderProto"

Appearance170.shaders.append(ProtoInstance173)
ComposedShader174 = x3d.ComposedShader()
ComposedShader174.DEF = "TestShader4"
ShaderPart175 = x3d.ShaderPart()
ShaderPart175.DEF = "TestShader5"

ComposedShader174.parts.append(ShaderPart175)

Appearance170.shaders.append(ComposedShader174)

Shape169.appearance = Appearance170

Scene32.children.append(Shape169)
Transform176 = x3d.Transform()
Transform176.DEF = "SpecialtyNodes"
CADLayer177 = x3d.CADLayer()
CADAssembly178 = x3d.CADAssembly()
CADPart179 = x3d.CADPart()
CADFace180 = x3d.CADFace()

CADPart179.children.append(CADFace180)

CADAssembly178.children.append(CADPart179)

CADLayer177.children.append(CADAssembly178)

Transform176.children.append(CADLayer177)
EspduTransform181 = x3d.EspduTransform()
EspduTransform181.geoSystem = ["GD","WE"]

Transform176.children.append(EspduTransform181)
ReceiverPdu182 = x3d.ReceiverPdu()
ReceiverPdu182.geoSystem = ["GD","WE"]

Transform176.children.append(ReceiverPdu182)
SignalPdu183 = x3d.SignalPdu()
SignalPdu183.geoSystem = ["GD","WE"]

Transform176.children.append(SignalPdu183)
TransmitterPdu184 = x3d.TransmitterPdu()
TransmitterPdu184.geoSystem = ["GD","WE"]

Transform176.children.append(TransmitterPdu184)
DISEntityManager185 = x3d.DISEntityManager()
DISEntityTypeMapping186 = x3d.DISEntityTypeMapping()

DISEntityManager185.children.append(DISEntityTypeMapping186)

Transform176.children.append(DISEntityManager185)

Scene32.children.append(Transform176)
EspduTransform187 = x3d.EspduTransform()
EspduTransform187.geoSystem = ["GD","WE"]
WorldInfo188 = x3d.WorldInfo()

EspduTransform187.children.append(WorldInfo188)

Scene32.children.append(EspduTransform187)
ReceiverPdu189 = x3d.ReceiverPdu()
ReceiverPdu189.geoSystem = ["GD","WE"]

Scene32.children.append(ReceiverPdu189)
SignalPdu190 = x3d.SignalPdu()
SignalPdu190.geoSystem = ["GD","WE"]

Scene32.children.append(SignalPdu190)
TransmitterPdu191 = x3d.TransmitterPdu()
TransmitterPdu191.geoSystem = ["GD","WE"]

Scene32.children.append(TransmitterPdu191)
DISEntityManager192 = x3d.DISEntityManager()
DISEntityTypeMapping193 = x3d.DISEntityTypeMapping()

DISEntityManager192.children.append(DISEntityTypeMapping193)

Scene32.children.append(DISEntityManager192)
LoadSensor194 = x3d.LoadSensor()
""" Contained nodes typically must be USE references for nodes previously DEFined in the scene """
""" The following nodes are test cases for all X3DUrlObject nodes """
Anchor195 = x3d.Anchor()
Anchor195.USE = "siteAnchor"

LoadSensor194.children.append(Anchor195)
Inline196 = x3d.Inline()
Inline196.USE = "inlineScene"

LoadSensor194.children.append(Inline196)
DISEntityTypeMapping197 = x3d.DISEntityTypeMapping()

LoadSensor194.children.append(DISEntityTypeMapping197)
GeoMetadata198 = x3d.GeoMetadata()

LoadSensor194.children.append(GeoMetadata198)
AudioClip199 = x3d.AudioClip()

LoadSensor194.children.append(AudioClip199)
ImageCubeMapTexture200 = x3d.ImageCubeMapTexture()

LoadSensor194.children.append(ImageCubeMapTexture200)
ImageTexture3D201 = x3d.ImageTexture3D()

LoadSensor194.children.append(ImageTexture3D201)
ImageTexture202 = x3d.ImageTexture()

LoadSensor194.children.append(ImageTexture202)
MovieTexture203 = x3d.MovieTexture()

LoadSensor194.children.append(MovieTexture203)
Script204 = x3d.Script()

LoadSensor194.children.append(Script204)
PackagedShader205 = x3d.PackagedShader()

LoadSensor194.children.append(PackagedShader205)
ShaderPart206 = x3d.ShaderPart()

LoadSensor194.children.append(ShaderPart206)
ShaderProgram207 = x3d.ShaderProgram()

LoadSensor194.children.append(ShaderProgram207)

Scene32.children.append(LoadSensor194)

X3D0.Scene = Scene32
f = open("HelloWorldProgramOutput_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
