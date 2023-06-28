print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"
head1 = x3d.head()
#comment #1
#comment #2
#comment #3
#comment #4
component2 = x3d.component()
component2.name = "Navigation"
component2.level = 3

head1.children.append(component2)
component3 = x3d.component()
component3.name = "Layering"
component3.level = 1

head1.children.append(component3)
unit4 = x3d.unit()
unit4.name = "AngleUnitConversion"
unit4.category = "angle"
unit4.conversionFactor = 1

head1.children.append(unit4)
unit5 = x3d.unit()
unit5.name = "LengthUnitConversion"
unit5.category = "length"
unit5.conversionFactor = 1

head1.children.append(unit5)
meta6 = x3d.meta()
meta6.name = "title"
meta6.content = "HelloWorldProgramOutput.x3d"

head1.children.append(meta6)
meta7 = x3d.meta()
meta7.name = "description"
meta7.content = "Example HelloWorldProgram creates an X3D model using the X3D Java Scene Access Interface (SAI) Library"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.name = "reference"
meta8.content = "https://www.web3d.org/specifications/java/X3DJSAIL.html"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "generator"
meta9.content = "HelloWorldProgramOutput.java"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "created"
meta10.content = "6 September 2016"

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.name = "modified"
meta11.content = "7 April 2018"

head1.children.append(meta11)
meta12 = x3d.meta()
meta12.name = "generator"
meta12.content = "X3D Java Scene Access Interface Library (X3DJSAIL)"

head1.children.append(meta12)
meta13 = x3d.meta()
meta13.name = "generator"
meta13.content = "https://www.web3d.org/specifications/java/examples/HelloWorldProgram.java"

head1.children.append(meta13)
meta14 = x3d.meta()
meta14.name = "generator"
meta14.content = "Netbeans http://www.netbeans.org"

head1.children.append(meta14)
meta15 = x3d.meta()
meta15.name = "creator"
meta15.content = "Don Brutzman"

head1.children.append(meta15)
meta16 = x3d.meta()
meta16.name = "reference"
meta16.content = "https://sourceforge.net/p/x3d/code/HEAD/tree/www.web3d.org/x3d/stylesheets/java/examples/HelloWorldProgramOutput.x3d"

head1.children.append(meta16)
meta17 = x3d.meta()
meta17.name = "reference"
meta17.content = "Console output, ClassicVRML encoding, VRML97 encoding and pretty-print documentation:"

head1.children.append(meta17)
meta18 = x3d.meta()
meta18.name = "reference"
meta18.content = "HelloWorldProgramOutput.txt"

head1.children.append(meta18)
meta19 = x3d.meta()
meta19.name = "reference"
meta19.content = "HelloWorldProgramOutput.x3dv"

head1.children.append(meta19)
meta20 = x3d.meta()
meta20.name = "reference"
meta20.content = "HelloWorldProgramOutput.wrl"

head1.children.append(meta20)
meta21 = x3d.meta()
meta21.name = "reference"
meta21.content = "HelloWorldProgramOutput.html"

head1.children.append(meta21)
meta22 = x3d.meta()
meta22.name = "reference"
meta22.content = "X3dValidator https://savage.nps.edu/X3dValidator?url=https://www.web3d.org/specifications/java/examples/HelloWorldProgramOutput.x3d"

head1.children.append(meta22)
meta23 = x3d.meta()
meta23.name = "identifier"
meta23.content = "https://www.web3d.org/specifications/java/examples/HelloWorldProgramOutput.x3d"

head1.children.append(meta23)
meta24 = x3d.meta()
meta24.name = "license"
meta24.content = "../license.html"

head1.children.append(meta24)
meta25 = x3d.meta()
meta25.name = "info"
meta25.content = "tested sat: name value cannot contain embedded space character"

head1.children.append(meta25)
meta26 = x3d.meta()
meta26.name = "translated"
meta26.content = "30 April 2018"

head1.children.append(meta26)
meta27 = x3d.meta()
meta27.name = "generator"
meta27.content = "X3dToJson.xslt, https://www.web3d.org/x3d/stylesheets/X3dToJson.html"

head1.children.append(meta27)
meta28 = x3d.meta()
meta28.name = "reference"
meta28.content = "X3D JSON encoding: https://www.web3d.org/wiki/index.php/X3D_JSON_Encoding"

head1.children.append(meta28)

X3D0.head = head1
Scene29 = x3d.Scene()
ViewpointGroup30 = x3d.ViewpointGroup()
ViewpointGroup30.description = "Available viewpoints"
Viewpoint31 = x3d.Viewpoint()
Viewpoint31.DEF = "DefaultView"
Viewpoint31.description = "Hello X3DJSAIL"

ViewpointGroup30.children.append(Viewpoint31)
Viewpoint32 = x3d.Viewpoint()
Viewpoint32.DEF = "TopDownView"
Viewpoint32.description = "top-down view from above"
Viewpoint32.orientation = [1,0,0,-1.570796]
Viewpoint32.position = [0,100,0]

ViewpointGroup30.children.append(Viewpoint32)

Scene29.children.append(ViewpointGroup30)
WorldInfo33 = x3d.WorldInfo()
WorldInfo33.DEF = "WorldInfoDEF"
WorldInfo33.title = "HelloWorldProgram produced by X3D Java SAI Library (X3DJSAIL)"

Scene29.children.append(WorldInfo33)
WorldInfo34 = x3d.WorldInfo()
WorldInfo34.USE = "WorldInfoDEF"

Scene29.children.append(WorldInfo34)
WorldInfo35 = x3d.WorldInfo()
WorldInfo35.USE = "WorldInfoDEF"

Scene29.children.append(WorldInfo35)
MetadataString36 = x3d.MetadataString()
MetadataString36.name = "test"
MetadataString36.DEF = "scene.addChildMetadata"
MetadataString36.value = ["Top-level root Metadata node beneath Scene needs to be one of '-children' in JSON encoding"]

Scene29.metadata.append(MetadataString36)
LayerSet37 = x3d.LayerSet()
LayerSet37.DEF = "scene.addChildLayerSetTest"

Scene29.layerSet.append(LayerSet37)
Transform38 = x3d.Transform()
Transform38.DEF = "LogoGeometryTransform"
Transform38.translation = [0,1.5,0]
Anchor39 = x3d.Anchor()
Anchor39.description = "select for X3D Java SAI Library (X3DJSAIL) description"
Anchor39.url = ["../X3DJSAIL.html","https://www.web3d.org/specifications/java/X3DJSAIL.html"]
Shape40 = x3d.Shape()
Shape40.DEF = "BoxShape"
Appearance41 = x3d.Appearance()
Material42 = x3d.Material()
Material42.DEF = "GreenMaterial"
Material42.diffuseColor = [0,1,1]
Material42.emissiveColor = [0.8,0,0]
Material42.transparency = 0.1

Appearance41.material = Material42
ImageTexture43 = x3d.ImageTexture()
ImageTexture43.url = ["images/X3dJavaSceneAccessInterfaceSaiLibrary.png","https://www.web3d.org/specifications/java/examples/images/X3dJavaSceneAccessInterfaceSaiLibrary.png"]

Appearance41.texture = ImageTexture43

Shape40.appearance = Appearance41
Box44 = x3d.Box()
Box44.DEF = "test-NMTOKEN_regex.0123456789"
Box44.cssClass = "untextured"

Shape40.geometry = Box44

Anchor39.children.append(Shape40)

Transform38.children.append(Anchor39)

Scene29.children.append(Transform38)
Shape45 = x3d.Shape()
Shape45.DEF = "LineShape"
Appearance46 = x3d.Appearance()
Material47 = x3d.Material()
Material47.emissiveColor = [0.6,0.19607843,0.8]

Appearance46.material = Material47

Shape45.appearance = Appearance46
IndexedLineSet48 = x3d.IndexedLineSet()
IndexedLineSet48.coordIndex = [0,1,2,3,4,0]
#Coordinate 3-tuple point count: 6
Coordinate49 = x3d.Coordinate()
Coordinate49.point = (0.0000,1.5000,0.0000,2.0000,1.5000,0.0000,2.0000,1.5000,-2.0000,-2.0000,1.5000,-2.0000,-2.0000,1.5000,0.0000,0.0000,1.5000,0.0000)

IndexedLineSet48.coord.append(Coordinate49)

Shape45.geometry = IndexedLineSet48

Scene29.children.append(Shape45)
PositionInterpolator50 = x3d.PositionInterpolator()
PositionInterpolator50.DEF = "BoxPathAnimator"
PositionInterpolator50.key = [0,0.125,0.375,0.625,0.875,1]
PositionInterpolator50.keyValue = (0.0000,1.5000,0.0000,2.0000,1.5000,0.0000,2.0000,1.5000,-2.0000,-2.0000,1.5000,-2.0000,-2.0000,1.5000,0.0000,0.0000,1.5000,0.0000)

Scene29.children.append(PositionInterpolator50)
TimeSensor51 = x3d.TimeSensor()
TimeSensor51.DEF = "OrbitClock"
TimeSensor51.cycleInterval = 8
TimeSensor51.loop = True

Scene29.children.append(TimeSensor51)
ROUTE52 = x3d.ROUTE()
ROUTE52.fromField = "fraction_changed"
ROUTE52.fromNode = "OrbitClock"
ROUTE52.toField = "set_fraction"
ROUTE52.toNode = "BoxPathAnimator"

Scene29.children.append(ROUTE52)
ROUTE53 = x3d.ROUTE()
ROUTE53.fromField = "value_changed"
ROUTE53.fromNode = "BoxPathAnimator"
ROUTE53.toField = "set_translation"
ROUTE53.toNode = "LogoGeometryTransform"

Scene29.children.append(ROUTE53)
Transform54 = x3d.Transform()
Transform54.DEF = "TextTransform"
Transform54.translation = [0,-1.5,0]
Shape55 = x3d.Shape()
Appearance56 = x3d.Appearance()
Material57 = x3d.Material()
Material57.USE = "GreenMaterial"

Appearance56.material = Material57

Shape55.appearance = Appearance56
Text58 = x3d.Text()
Text58.string = ["X3D Java","SAI Library","X3DJSAIL"]
#Comment example A, plain quotation marks: He said, \"Immel did it!\"
#Comment example B, XML character entities: He said, &quot;Immel did it!&quot;
MetadataSet59 = x3d.MetadataSet()
MetadataSet59.name = "EscapedQuotationMarksMetadataSet"
MetadataString60 = x3d.MetadataString()
MetadataString60.name = "quotesTestC"
MetadataString60.value = ["MFString example C, backslash-escaped quotes: He said, \"Immel did it!\""]

MetadataSet59.value.append(MetadataString60)
MetadataString61 = x3d.MetadataString()
MetadataString61.name = "extraChildTest"
MetadataString61.value = ["checks MetadataSetObject addValue() method"]

MetadataSet59.value.append(MetadataString61)

Text58.metadata.append(MetadataSet59)
FontStyle62 = x3d.FontStyle()
FontStyle62.justify = ["MIDDLE","MIDDLE"]

Text58.fontStyle = FontStyle62

Shape55.geometry = Text58

Transform54.children.append(Shape55)
Collision63 = x3d.Collision()
#test containerField='proxy'
Shape64 = x3d.Shape()
Shape64.DEF = "ProxyShape"
#alternative XML encoding: Text string='\"One, Two, Comment\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\"'
#alternative XML encoding: Text string='\"One, Two, Comment\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\" \"\"'
#alternative Java source: .setString(new String [] {\"One, Two, Comment\", \"\", \"He said, \\\"\"\"Immel did it!\\\"\"\\\"\"})
#reference: https://www.web3d.org/x3d/content/examples/Basic/X3dSpecifications/StringArrayEncodingExamplesIndex.html
Text65 = x3d.Text()
Text65.string = ["One, Two, Text","","He said, \"Immel did it!\" \"\""]

Shape64.geometry = Text65

Collision63.proxy = Shape64

Transform54.children.append(Collision63)
#It's a beautiful world
#... for you!
#https://en.wikipedia.org/wiki/Beautiful_World_(Devo_song)

Scene29.children.append(Transform54)
#repeatedly spin 180 degrees as a readable special effect
OrientationInterpolator66 = x3d.OrientationInterpolator()
OrientationInterpolator66.DEF = "SpinInterpolator"
OrientationInterpolator66.key = [0,0.5,1]
OrientationInterpolator66.keyValue = (0.0000,1.0000,0.0000,4.7124,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,1.5708)

Scene29.children.append(OrientationInterpolator66)
TimeSensor67 = x3d.TimeSensor()
TimeSensor67.DEF = "SpinClock"
TimeSensor67.cycleInterval = 5
TimeSensor67.loop = True

Scene29.children.append(TimeSensor67)
ROUTE68 = x3d.ROUTE()
ROUTE68.fromField = "fraction_changed"
ROUTE68.fromNode = "SpinClock"
ROUTE68.toField = "set_fraction"
ROUTE68.toNode = "SpinInterpolator"

Scene29.children.append(ROUTE68)
ROUTE69 = x3d.ROUTE()
ROUTE69.fromField = "value_changed"
ROUTE69.fromNode = "SpinInterpolator"
ROUTE69.toField = "rotation"
ROUTE69.toNode = "TextTransform"

Scene29.children.append(ROUTE69)
Group70 = x3d.Group()
Group70.DEF = "BackgroundGroup"
Background71 = x3d.Background()
Background71.DEF = "GradualBackground"

Group70.children.append(Background71)
Script72 = x3d.Script()
Script72.DEF = "colorTypeConversionScript"
field73 = x3d.field()
field73.name = "colorInput"
field73.accessType = "inputOnly"
field73.type = "SFColor"

Script72.field.append(field73)
field74 = x3d.field()
field74.name = "colorsOutput"
field74.accessType = "outputOnly"
field74.type = "MFColor"

Script72.field.append(field74)

Script72.sourceCode = '''ecmascript:\n"+
"\n"+
"function colorInput (eventValue) // Example source code\n"+
"{\n"+
"   colorsOutput = new MFColor(eventValue); // assigning value sends output event\n"+
"// Browser.print('colorInput=' + eventValue + ', colorsOutput=' + colorsOutput + '\\n');\n"+
"}'''

Group70.children.append(Script72)
ColorInterpolator75 = x3d.ColorInterpolator()
ColorInterpolator75.DEF = "ColorAnimator"
ColorInterpolator75.key = [0,0.5,1]
ColorInterpolator75.keyValue = [0.9411765,1,1,0.29411766,0,0.50980395,0.9411765,1,1]
#AZURE to INDIGO and back again

Group70.children.append(ColorInterpolator75)
TimeSensor76 = x3d.TimeSensor()
TimeSensor76.DEF = "ColorClock"
TimeSensor76.cycleInterval = 60
TimeSensor76.loop = True

Group70.children.append(TimeSensor76)
ROUTE77 = x3d.ROUTE()
ROUTE77.fromField = "colorsOutput"
ROUTE77.fromNode = "colorTypeConversionScript"
ROUTE77.toField = "skyColor"
ROUTE77.toNode = "GradualBackground"

Group70.children.append(ROUTE77)
ROUTE78 = x3d.ROUTE()
ROUTE78.fromField = "value_changed"
ROUTE78.fromNode = "ColorAnimator"
ROUTE78.toField = "colorInput"
ROUTE78.toNode = "colorTypeConversionScript"

Group70.children.append(ROUTE78)
ROUTE79 = x3d.ROUTE()
ROUTE79.fromField = "fraction_changed"
ROUTE79.fromNode = "ColorClock"
ROUTE79.toField = "set_fraction"
ROUTE79.toNode = "ColorAnimator"

Group70.children.append(ROUTE79)

Scene29.children.append(Group70)
ProtoDeclare80 = x3d.ProtoDeclare()
ProtoDeclare80.name = "ArtDeco01Material"
ProtoDeclare80.appinfo = "tooltip: ArtDeco01Material prototype is a Material node"
ProtoInterface81 = x3d.ProtoInterface()
field82 = x3d.field()
field82.name = "description"
field82.accessType = "inputOutput"
field82.appinfo = "tooltip for descriptionField"
field82.type = "SFString"
field82.value = "ArtDeco01Material prototype is a Material node"

ProtoInterface81.field.append(field82)
field83 = x3d.field()
field83.name = "enabled"
field83.accessType = "inputOutput"
field83.type = "SFBool"
field83.value = True

ProtoInterface81.field.append(field83)

ProtoDeclare80.ProtoInterface = ProtoInterface81
ProtoBody84 = x3d.ProtoBody()
#Initial node of ProtoBody determines prototype node type
Material85 = x3d.Material()
Material85.ambientIntensity = 0.25
Material85.diffuseColor = [0.282435,0.085159,0.134462]
Material85.shininess = 0.127273
Material85.specularColor = [0.276305,0.11431,0.139857]

ProtoBody84.children.append(Material85)
#[HelloWorldProgram diagnostic] should be connected to scene graph: ArtDeco01ProtoDeclare.getNodeType()=\"Material\"
#presence of follow-on TouchSensor shows that additional nodes are allowed in ProtoBody after initial node, regardless of node types
TouchSensor86 = x3d.TouchSensor()
TouchSensor86.description = "within ProtoBody"
IS87 = x3d.IS()
connect88 = x3d.connect()
connect88.nodeField = "description"
connect88.protoField = "description"

IS87.connect.append(connect88)
connect89 = x3d.connect()
connect89.nodeField = "enabled"
connect89.protoField = "enabled"

IS87.connect.append(connect89)

TouchSensor86.IS = IS87

ProtoBody84.children.append(TouchSensor86)

ProtoDeclare80.ProtoBody = ProtoBody84

Scene29.children.append(ProtoDeclare80)
ExternProtoDeclare90 = x3d.ExternProtoDeclare()
ExternProtoDeclare90.name = "ArtDeco02Material"
ExternProtoDeclare90.appinfo = "this is a different Material node"
ExternProtoDeclare90.url = ["http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3d#ArtDeco02Material","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3dv#ArtDeco02Material"]
#[HelloWorldProgram diagnostic] ArtDeco02ExternProtoDeclare.getNodeType()=\"ERROR_UNKNOWN_EXTERNPROTODECLARE_NODE_TYPE: ExternProtoDeclare name='ArtDeco02Material' type cannot be remotely accessed at run time, TODO X3DJSAIL needs to add further capability.\"
field91 = x3d.field()
field91.name = "description"
field91.accessType = "inputOutput"
field91.appinfo = "tooltip for descriptionField"
field91.type = "SFString"

ExternProtoDeclare90.field.append(field91)

Scene29.children.append(ExternProtoDeclare90)
#Tested ArtDeco01ProtoInstance, ArtDeco02ProtoInstance for improper node type when ProtoInstance is added in wrong place
Shape92 = x3d.Shape()
Shape92.DEF = "TestShape1"
Appearance93 = x3d.Appearance()
Appearance93.DEF = "TestAppearance1"
#ArtDeco01Material prototype goes here... TODO ensure setContainerField is handled in exported Java
ProtoInstance94 = x3d.ProtoInstance()
ProtoInstance94.name = "ArtDeco01Material"
#[HelloWorldProgram diagnostic] ArtDeco01ProtoInstance.getNodeType()=\"Material\"
fieldValue95 = x3d.fieldValue()
fieldValue95.name = "description"
fieldValue95.value = "ArtDeco01Material can substitute for a Material node"

ProtoInstance94.fieldValue.append(fieldValue95)

Appearance93.material = ProtoInstance94

Shape92.appearance = Appearance93
Sphere96 = x3d.Sphere()
Sphere96.radius = 0.001

Shape92.geometry = Sphere96

Scene29.children.append(Shape92)
Shape97 = x3d.Shape()
Shape97.DEF = "TestShape2"
Appearance98 = x3d.Appearance()
Appearance98.DEF = "TestAppearance2"
#ArtDeco02Material prototype goes here... TODO ensure setContainerField is handled in exported Java
ProtoInstance99 = x3d.ProtoInstance()
ProtoInstance99.name = "ArtDeco02Material"
ProtoInstance99.DEF = "ArtDeco02MaterialDEF"
#[HelloWorldProgram diagnostic] ArtDeco02ProtoInstance.getNodeType()=\"ERROR_UNKNOWN_EXTERNPROTODECLARE_NODE_TYPE: ExternProtoDeclare name='ArtDeco02Material' type cannot be remotely accessed at run time, TODO X3DJSAIL needs to add further capability.\"
fieldValue100 = x3d.fieldValue()
fieldValue100.name = "description"
fieldValue100.value = "ArtDeco02Material can substitute for another Material node"

ProtoInstance99.fieldValue.append(fieldValue100)

Appearance98.material = ProtoInstance99

Shape97.appearance = Appearance98
Cone101 = x3d.Cone()
Cone101.bottomRadius = 0.001
Cone101.height = 0.001

Shape97.geometry = Cone101

Scene29.children.append(Shape97)
Shape102 = x3d.Shape()
Shape102.DEF = "TestShape3"
Appearance103 = x3d.Appearance()
Appearance103.DEF = "TestAppearance3"
#ArtDeco02Material ProtoInstance USE goes here...
ProtoInstance104 = x3d.ProtoInstance()
ProtoInstance104.USE = "ArtDeco02MaterialDEF"

Appearance103.material = ProtoInstance104

Shape102.appearance = Appearance103
Cylinder105 = x3d.Cylinder()
Cylinder105.height = 0.001
Cylinder105.radius = 0.001

Shape102.geometry = Cylinder105

Scene29.children.append(Shape102)
Inline106 = x3d.Inline()
Inline106.DEF = "inlineSceneDef"
Inline106.url = ["someOtherScene.x3d"]

Scene29.children.append(Inline106)
IMPORT107 = x3d.IMPORT()
IMPORT107.AS = "WorldInfoDEF2"
IMPORT107.importedDEF = "WorldInfoDEF"
IMPORT107.inlineDEF = "inlineSceneDef"

Scene29.children.append(IMPORT107)
EXPORT108 = x3d.EXPORT()
EXPORT108.AS = "WorldInfoDEF3"
EXPORT108.localDEF = "WorldInfoDEF"

Scene29.children.append(EXPORT108)
ProtoDeclare109 = x3d.ProtoDeclare()
ProtoDeclare109.name = "MaterialModulator"
ProtoDeclare109.appinfo = "mimic a Material node and modulate fields as an animation effect"
ProtoDeclare109.documentation = "http://x3dgraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/MaterialModulatorIndex.html"
ProtoInterface110 = x3d.ProtoInterface()
field111 = x3d.field()
field111.name = "enabled"
field111.accessType = "inputOutput"
field111.type = "SFBool"
field111.value = True

ProtoInterface110.field.append(field111)
field112 = x3d.field()
field112.name = "diffuseColor"
field112.accessType = "inputOutput"
field112.type = "SFColor"
field112.value = [0,0,0]

ProtoInterface110.field.append(field112)
field113 = x3d.field()
field113.name = "emissiveColor"
field113.accessType = "inputOutput"
field113.type = "SFColor"
field113.value = [0.05,0.05,0.5]

ProtoInterface110.field.append(field113)
field114 = x3d.field()
field114.name = "specularColor"
field114.accessType = "inputOutput"
field114.type = "SFColor"
field114.value = [0,0,0]

ProtoInterface110.field.append(field114)
field115 = x3d.field()
field115.name = "transparency"
field115.accessType = "inputOutput"
field115.type = "SFFloat"
field115.value = 0

ProtoInterface110.field.append(field115)
field116 = x3d.field()
field116.name = "shininess"
field116.accessType = "inputOutput"
field116.type = "SFFloat"
field116.value = 0

ProtoInterface110.field.append(field116)
field117 = x3d.field()
field117.name = "ambientIntensity"
field117.accessType = "inputOutput"
field117.type = "SFFloat"
field117.value = 0

ProtoInterface110.field.append(field117)

ProtoDeclare109.ProtoInterface = ProtoInterface110
ProtoBody118 = x3d.ProtoBody()
Material119 = x3d.Material()
Material119.DEF = "MaterialNode"
IS120 = x3d.IS()
connect121 = x3d.connect()
connect121.nodeField = "diffuseColor"
connect121.protoField = "diffuseColor"

IS120.connect.append(connect121)
connect122 = x3d.connect()
connect122.nodeField = "emissiveColor"
connect122.protoField = "emissiveColor"

IS120.connect.append(connect122)
connect123 = x3d.connect()
connect123.nodeField = "specularColor"
connect123.protoField = "specularColor"

IS120.connect.append(connect123)
connect124 = x3d.connect()
connect124.nodeField = "transparency"
connect124.protoField = "transparency"

IS120.connect.append(connect124)
connect125 = x3d.connect()
connect125.nodeField = "shininess"
connect125.protoField = "shininess"

IS120.connect.append(connect125)
connect126 = x3d.connect()
connect126.nodeField = "ambientIntensity"
connect126.protoField = "ambientIntensity"

IS120.connect.append(connect126)

Material119.IS = IS120

ProtoBody118.children.append(Material119)
#Only first node (the node type) is renderable, others are along for the ride
Script127 = x3d.Script()
Script127.DEF = "MaterialModulatorScript"
field128 = x3d.field()
field128.name = "enabled"
field128.accessType = "inputOutput"
field128.type = "SFBool"

Script127.field.append(field128)
field129 = x3d.field()
field129.name = "diffuseColor"
field129.accessType = "inputOutput"
field129.type = "SFColor"

Script127.field.append(field129)
field130 = x3d.field()
field130.name = "newColor"
field130.accessType = "outputOnly"
field130.type = "SFColor"

Script127.field.append(field130)
field131 = x3d.field()
field131.name = "clockTrigger"
field131.accessType = "inputOnly"
field131.type = "SFTime"

Script127.field.append(field131)
IS132 = x3d.IS()
connect133 = x3d.connect()
connect133.nodeField = "enabled"
connect133.protoField = "enabled"

IS132.connect.append(connect133)
connect134 = x3d.connect()
connect134.nodeField = "diffuseColor"
connect134.protoField = "diffuseColor"

IS132.connect.append(connect134)

Script127.IS = IS132

Script127.sourceCode = '''ecmascript:\n"+
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
"\n"+
"    // note different modulation rates for each color component, % is modulus operator\n"+
"    newColor = new SFColor ((red + 0.02) % 1, (green + 0.03) % 1, (blue + 0.04) % 1);\n"+
"	if (enabled)\n"+
"	{\n"+
"		Browser.print ('diffuseColor=(' + red + ',' + green + ',' + blue + ') newColor=' + newColor.toString() + '\\n');\n"+
"	}\n"+
"}'''

ProtoBody118.children.append(Script127)

ProtoDeclare109.ProtoBody = ProtoBody118

Scene29.children.append(ProtoDeclare109)
#Test success: declarative statement createDeclarativeShapeTests()
Group135 = x3d.Group()
Group135.DEF = "DeclarativeGroupExample"
Shape136 = x3d.Shape()
MetadataString137 = x3d.MetadataString()
MetadataString137.name = "findThisNameValue"
MetadataString137.DEF = "FindableMetadataStringTest"
MetadataString137.value = ["test case"]

Shape136.metadata.append(MetadataString137)
Appearance138 = x3d.Appearance()
Appearance138.DEF = "DeclarativeAppearanceExample"
#DeclarativeMaterialExample gets overridden by subsequently added MaterialModulator ProtoInstance
ProtoInstance139 = x3d.ProtoInstance()
ProtoInstance139.name = "MaterialModulator"
ProtoInstance139.DEF = "MyMaterialModulator"

Appearance138.material = ProtoInstance139

Shape136.appearance = Appearance138
Cone140 = x3d.Cone()
Cone140.bottom = False
Cone140.bottomRadius = 0.05
Cone140.height = 0.1

Shape136.geometry = Cone140

Group135.children.append(Shape136)
#Test success: declarativeGroup.addChild() singleton pipeline method

Scene29.children.append(Group135)
#Test success: declarative statement addChild()
#Test success: x3dModel.findNodeByDEF(DeclarativeAppearanceExample) = <Appearance DEF='DeclarativeAppearanceExample'/> i.e. <Appearance DEF='DeclarativeAppearanceExample'> <!- - DeclarativeMaterialExample gets overridden by subsequently added MaterialModulator ProtoInstance - -> <ProtoInstance DEF='MyMaterialModulator' name='MaterialModulator' containerField='material'/> </Appearance>
#Test success: x3dModel.findElementByNameValue(findThisNameValue) = <MetadataString DEF='FindableMetadataStringTest' name='findThisNameValue' value='\"test case\"'/>
#Test success: x3dModel.findElementByNameValue(\"ArtDeco01Material\", \"ProtoDeclare\") found
#Test success: x3dModel.findElementByNameValue(\"MaterialModulator\", \"ProtoDeclare\") found
#Test success: x3dModel.findElementByNameValue(\"MaterialModulator\", \"ProtoInstance\") found
Group141 = x3d.Group()
Group141.DEF = "TestFieldObjectsGroup"
#testFieldObjects() results
#SFBool default=true, true=true, false=false, negate()=true
#MFBool default=, initial=true false true, negate()=false true false
#SFFloat default=0.0, initial=1.0, setValue(2)=2.0, setValue(3.0f)=3.0, setValue(4.0)=4.0
#MFFloat default=, initial=1 2 3, append(5)=1 2 3 5, inserts(3,4)(0,0)=0 1 2 3 4 5, append(6)=0 1 2 3 4 5 6, size()=7
#... get1Value[3]=3.0, remove[1]=0 2 3 4 5 6, set1Value(0,10)=10 2 3 4 5 6, multiply(2)=20 4 6 8 10 12, clear=
#SFVec3f default=0 0 0, initial=1 2 3, setValue=4 5 6, multiply(2)=8 10 12, normalize()=0.45584232 0.5698029 0.68376344

Scene29.children.append(Group141)
Sound142 = x3d.Sound()
Sound142.location = [0,1.6,0]
#set sound-ellipsoid location height at 1.6m to match typical avatar height
AudioClip143 = x3d.AudioClip()
AudioClip143.description = "chimes"
AudioClip143.url = ["chimes.wav","https://www.web3d.org/x3d/content/examples/ConformanceNist/Sounds/AudioClip/chimes.wav"]
#Scene example fragment from https://www.web3d.org/x3d/content/examples/ConformanceNist/Sounds/AudioClip/default.x3d

Sound142.source.append(AudioClip143)

Scene29.children.append(Sound142)
Sound144 = x3d.Sound()
Sound144.location = [0,1.6,0]
#set sound-ellipsoid location height at 1.6m to match typical avatar height
MovieTexture145 = x3d.MovieTexture()
MovieTexture145.description = "mpgsys.mpg from ConformanceNist suite"
MovieTexture145.url = ["mpgsys.mpg","https://www.web3d.org/x3d/content/examples/ConformanceNist/Appearance/MovieTexture/mpgsys.mpg"]
#Scene example fragment from https://www.web3d.org/x3d/content/examples/ConformanceNist/Appearance/MovieTexture/mpeg1-systems.x3d
#Expected containerField='source', allowed containerField values=\"texture\" \"source\" \"back\" \"bottom\" \"front\" \"left\" \"right\" \"top\" \"backTexture\" \"bottomTexture\" \"frontTexture\" \"leftTexture\" \"rightTexture\" \"topTexture\"

Sound144.source.append(MovieTexture145)

Scene29.children.append(Sound144)
#Test success: AnchorObject.isNode()=true, siteAnchor.isNode()=true
#Test success: AnchorObject.isStatement()=false, siteAnchor.isStatement()=false
#Test success: ROUTEObject.isNode()=false, orbitPositionROUTE.isNode()=false
#Test success: ROUTEObject.isStatement()=true, orbitPositionROUTE.isStatement()=true
#Test success: CommentsBlock.isNode()=false, testComments.isNode()=false
#Test failure: CommentsBlock.isStatement()=true, testComments.isStatement()=true
Shape146 = x3d.Shape()
Shape146.DEF = "ExtrusionShape"
#ExampleExtrusion isCrossSectionClosed()=true, crossSection='[1.0, 1.0, 1.0, -1.0, -1.0, -1.0, -1.0, 1.0, 1.0, 1.0]'
#ExampleExtrusion isSpineClosed()=false, spine='[0.0, 0.0, 0.0, 0.0, 1.0, 0.0]'
Appearance147 = x3d.Appearance()
Appearance147.DEF = "TransparentAppearance"
Material148 = x3d.Material()
Material148.transparency = 1

Appearance147.material = Material148

Shape146.appearance = Appearance147
Extrusion149 = x3d.Extrusion()
Extrusion149.DEF = "ExampleExtrusion"

Shape146.geometry = Extrusion149

Scene29.children.append(Shape146)

X3D0.Scene = Scene29
f = open("././Quotes_RoundTrip.x3d", "w")
f.write(X3D0.XML())
f.close()
