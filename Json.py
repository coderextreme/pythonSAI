print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"
#x3dVersionComparisonTest for this model: supportsX3dVersion(X3D.VERSION_3_0)=true
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
unit9.conversionFactor = 1

head1.children.append(unit9)
unit10 = x3d.unit()
unit10.name = "LengthUnitConversion"
unit10.category = "length"
unit10.conversionFactor = 1

head1.children.append(unit10)
unit11 = x3d.unit()
unit11.name = "ForceFromPoundsToNewtons"
unit11.category = "force"
unit11.conversionFactor = 4.4482

head1.children.append(unit11)
meta12 = x3d.meta()
meta12.name = "title"
meta12.content = "HelloWorldProgramOutput.x3d"

head1.children.append(meta12)
meta13 = x3d.meta()
meta13.name = "info"
meta13.content = "continued development and testing in progress"

head1.children.append(meta13)
meta14 = x3d.meta()
meta14.name = "description"
meta14.content = "Example HelloWorldProgram creates an X3D model using the X3D Java Scene Access Interface Library (X3DJSAIL)"

head1.children.append(meta14)
meta15 = x3d.meta()
meta15.name = "reference"
meta15.content = "https://www.web3d.org/specifications/java/X3DJSAIL.html"

head1.children.append(meta15)
meta16 = x3d.meta()
meta16.name = "generator"
meta16.content = "HelloWorldProgramOutput.java"

head1.children.append(meta16)
meta17 = x3d.meta()
meta17.name = "created"
meta17.content = "6 September 2016"

head1.children.append(meta17)
meta18 = x3d.meta()
meta18.name = "modified"
meta18.content = "25 May 2020"

head1.children.append(meta18)
meta19 = x3d.meta()
meta19.name = "generator"
meta19.content = "X3D Java Scene Access Interface Library (X3DJSAIL)"

head1.children.append(meta19)
meta20 = x3d.meta()
meta20.name = "generator"
meta20.content = "https://www.web3d.org/specifications/java/examples/HelloWorldProgram.java"

head1.children.append(meta20)
meta21 = x3d.meta()
meta21.name = "generator"
meta21.content = "Netbeans http://www.netbeans.org"

head1.children.append(meta21)
meta22 = x3d.meta()
meta22.name = "creator"
meta22.content = "Don Brutzman"

head1.children.append(meta22)
meta23 = x3d.meta()
meta23.name = "reference"
meta23.content = "https://sourceforge.net/p/x3d/code/HEAD/tree/www.web3d.org/x3d/stylesheets/java/examples/HelloWorldProgramOutput.x3d"

head1.children.append(meta23)
meta24 = x3d.meta()
meta24.name = "reference"
meta24.content = "Console output, ClassicVRML encoding, VRML97 encoding and pretty-print documentation:"

head1.children.append(meta24)
meta25 = x3d.meta()
meta25.name = "reference"
meta25.content = "HelloWorldProgramOutput.txt"

head1.children.append(meta25)
meta26 = x3d.meta()
meta26.name = "reference"
meta26.content = "HelloWorldProgramOutput.x3dv"

head1.children.append(meta26)
meta27 = x3d.meta()
meta27.name = "reference"
meta27.content = "HelloWorldProgramOutput.wrl"

head1.children.append(meta27)
meta28 = x3d.meta()
meta28.name = "reference"
meta28.content = "HelloWorldProgramOutput.html"

head1.children.append(meta28)
meta29 = x3d.meta()
meta29.name = "reference"
meta29.content = "https://savage.nps.edu/X3dValidator?url=https://www.web3d.org/specifications/java/examples/HelloWorldProgramOutput.x3d"

head1.children.append(meta29)
meta30 = x3d.meta()
meta30.name = "identifier"
meta30.content = "https://www.web3d.org/specifications/java/examples/HelloWorldProgramOutput.x3d"

head1.children.append(meta30)
meta31 = x3d.meta()
meta31.name = "license"
meta31.content = "../license.html"

head1.children.append(meta31)
meta32 = x3d.meta()
meta32.name = "translated"
meta32.content = "25 May 2020"

head1.children.append(meta32)
meta33 = x3d.meta()
meta33.name = "generator"
meta33.content = "X3dToJson.xslt, https://www.web3d.org/x3d/stylesheets/X3dToJson.html"

head1.children.append(meta33)
meta34 = x3d.meta()
meta34.name = "reference"
meta34.content = "X3D JSON encoding: https://www.web3d.org/wiki/index.php/X3D_JSON_Encoding"

head1.children.append(meta34)

X3D0.head = head1
Scene35 = x3d.Scene()
ViewpointGroup36 = x3d.ViewpointGroup()
ViewpointGroup36.description = "Available viewpoints"
Viewpoint37 = x3d.Viewpoint()
Viewpoint37.DEF = "DefaultView"
Viewpoint37.description = "Hello X3DJSAIL"

ViewpointGroup36.children.append(Viewpoint37)
Viewpoint38 = x3d.Viewpoint()
Viewpoint38.DEF = "TopDownView"
Viewpoint38.description = "top-down view from above"
Viewpoint38.orientation = [1,0,0,-1.570796]
Viewpoint38.position = [0,100,0]

ViewpointGroup36.children.append(Viewpoint38)

Scene35.children.append(ViewpointGroup36)
NavigationInfo39 = x3d.NavigationInfo()
NavigationInfo39.type = ["EXAMINE","FLY","ANY"]

Scene35.children.append(NavigationInfo39)
WorldInfo40 = x3d.WorldInfo()
WorldInfo40.DEF = "WorldInfoDEF"
WorldInfo40.title = "HelloWorldProgram produced by X3D Java SAI Library (X3DJSAIL)"

Scene35.children.append(WorldInfo40)
WorldInfo41 = x3d.WorldInfo()
WorldInfo41.USE = "WorldInfoDEF"

Scene35.children.append(WorldInfo41)
WorldInfo42 = x3d.WorldInfo()
WorldInfo42.USE = "WorldInfoDEF"

Scene35.children.append(WorldInfo42)
MetadataString43 = x3d.MetadataString()
MetadataString43.name = "test"
MetadataString43.DEF = "scene.addChildMetadata"
MetadataString43.value = ["Top-level root Metadata node beneath Scene needs to be one of '-children' in JSON encoding"]

Scene35.metadata.append(MetadataString43)
LayerSet44 = x3d.LayerSet()
LayerSet44.DEF = "scene.addChildLayerSetTest"

Scene35.layerSet.append(LayerSet44)
Transform45 = x3d.Transform()
Transform45.DEF = "LogoGeometryTransform"
Transform45.translation = [0,1.5,0]
Anchor46 = x3d.Anchor()
Anchor46.description = "select for X3D Java SAI Library (X3DJSAIL) description"
Anchor46.url = ["../X3DJSAIL.html","https://www.web3d.org/specifications/java/X3DJSAIL.html"]
Shape47 = x3d.Shape()
Shape47.DEF = "BoxShape"
Appearance48 = x3d.Appearance()
Material49 = x3d.Material()
Material49.DEF = "GreenMaterial"
Material49.diffuseColor = [0,1,1]
Material49.emissiveColor = [0.8,0,0]
Material49.transparency = 0.1

Appearance48.material = Material49
ImageTexture50 = x3d.ImageTexture()
ImageTexture50.url = ["images/X3dJavaSceneAccessInterfaceSaiLibrary.png","https://www.web3d.org/specifications/java/examples/images/X3dJavaSceneAccessInterfaceSaiLibrary.png"]

Appearance48.texture = ImageTexture50

Shape47.appearance = Appearance48
Box51 = x3d.Box()
Box51.DEF = "test-NMTOKEN_regex.0123456789"
Box51.cssClass = "untextured"

Shape47.geometry = Box51

Anchor46.children.append(Shape47)

Transform45.children.append(Anchor46)

Scene35.children.append(Transform45)
Shape52 = x3d.Shape()
Shape52.DEF = "LineShape"
Appearance53 = x3d.Appearance()
Material54 = x3d.Material()
Material54.emissiveColor = [0.6,0.19607843,0.8]

Appearance53.material = Material54

Shape52.appearance = Appearance53
IndexedLineSet55 = x3d.IndexedLineSet()
IndexedLineSet55.coordIndex = [0,1,2,3,4,0]
#Coordinate 3-tuple point count: 6
Coordinate56 = x3d.Coordinate()
Coordinate56.point = (0.0000,1.5000,0.0000,2.0000,1.5000,0.0000,2.0000,1.5000,-2.0000,-2.0000,1.5000,-2.0000,-2.0000,1.5000,0.0000,0.0000,1.5000,0.0000)

IndexedLineSet55.coord.append(Coordinate56)

Shape52.geometry = IndexedLineSet55

Scene35.children.append(Shape52)
PositionInterpolator57 = x3d.PositionInterpolator()
PositionInterpolator57.DEF = "BoxPathAnimator"
PositionInterpolator57.key = [0,0.125,0.375,0.625,0.875,1]
PositionInterpolator57.keyValue = (0.0000,1.5000,0.0000,2.0000,1.5000,0.0000,2.0000,1.5000,-2.0000,-2.0000,1.5000,-2.0000,-2.0000,1.5000,0.0000,0.0000,1.5000,0.0000)

Scene35.children.append(PositionInterpolator57)
TimeSensor58 = x3d.TimeSensor()
TimeSensor58.DEF = "OrbitClock"
TimeSensor58.cycleInterval = 8
TimeSensor58.loop = True

Scene35.children.append(TimeSensor58)
ROUTE59 = x3d.ROUTE()
ROUTE59.fromField = "fraction_changed"
ROUTE59.fromNode = "OrbitClock"
ROUTE59.toField = "set_fraction"
ROUTE59.toNode = "BoxPathAnimator"

Scene35.children.append(ROUTE59)
ROUTE60 = x3d.ROUTE()
ROUTE60.fromField = "value_changed"
ROUTE60.fromNode = "BoxPathAnimator"
ROUTE60.toField = "set_translation"
ROUTE60.toNode = "LogoGeometryTransform"

Scene35.children.append(ROUTE60)
Transform61 = x3d.Transform()
Transform61.DEF = "TextTransform"
Transform61.translation = [0,-1.5,0]
Shape62 = x3d.Shape()
Appearance63 = x3d.Appearance()
Material64 = x3d.Material()
Material64.USE = "GreenMaterial"

Appearance63.material = Material64

Shape62.appearance = Appearance63
Text65 = x3d.Text()
Text65.string = ["X3D Java","SAI Library","X3DJSAIL"]
#Comment example A, plain quotation marks: He said, \"Immel did it!\"
#Comment example B, XML character entities: He said, &quot;Immel did it!&quot;
MetadataSet66 = x3d.MetadataSet()
MetadataSet66.name = "EscapedQuotationMarksMetadataSet"
MetadataString67 = x3d.MetadataString()
MetadataString67.name = "quotesTestC"
MetadataString67.value = ["MFString example C, backslash-escaped quotes: He said, \"Immel did it!\""]

MetadataSet66.value.append(MetadataString67)
MetadataString68 = x3d.MetadataString()
MetadataString68.name = "extraChildTest"
MetadataString68.value = ["checks MetadataSetObject addValue() method"]

MetadataSet66.value.append(MetadataString68)

Text65.metadata.append(MetadataSet66)
FontStyle69 = x3d.FontStyle()
FontStyle69.justify = ["MIDDLE","MIDDLE"]

Text65.fontStyle = FontStyle69

Shape62.geometry = Text65

Transform61.children.append(Shape62)
Collision70 = x3d.Collision()
#test containerField='proxy'
Shape71 = x3d.Shape()
Shape71.DEF = "ProxyShape"
#alternative XML encoding: Text string='\"One, Two, Comment\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\"'
#alternative XML encoding: Text string='\"One, Two, Comment\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\" \"\"'
#alternative Java source: .setString(new String [] {\"One, Two, Comment\", \"\", \"He said, \\\"\"Immel did it!\\\"\"\"})
#reference: https://www.web3d.org/x3d/content/examples/Basic/X3dSpecifications/StringArrayEncodingExamplesIndex.html
Text72 = x3d.Text()
Text72.string = ["One, Two, Text","","He said, \"Immel did it!\" \"\""]

Shape71.geometry = Text72

Collision70.proxy = Shape71

Transform61.children.append(Collision70)
#It's a beautiful world
#... for you!
#https://en.wikipedia.org/wiki/Beautiful_World_(Devo_song)

Scene35.children.append(Transform61)
#repeatedly spin 180 degrees as a readable special effect
OrientationInterpolator73 = x3d.OrientationInterpolator()
OrientationInterpolator73.DEF = "SpinInterpolator"
OrientationInterpolator73.key = [0,0.5,1]
OrientationInterpolator73.keyValue = (0.0000,1.0000,0.0000,4.7124,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,1.5708)

Scene35.children.append(OrientationInterpolator73)
TimeSensor74 = x3d.TimeSensor()
TimeSensor74.DEF = "SpinClock"
TimeSensor74.cycleInterval = 5
TimeSensor74.loop = True

Scene35.children.append(TimeSensor74)
ROUTE75 = x3d.ROUTE()
ROUTE75.fromField = "fraction_changed"
ROUTE75.fromNode = "SpinClock"
ROUTE75.toField = "set_fraction"
ROUTE75.toNode = "SpinInterpolator"

Scene35.children.append(ROUTE75)
ROUTE76 = x3d.ROUTE()
ROUTE76.fromField = "value_changed"
ROUTE76.fromNode = "SpinInterpolator"
ROUTE76.toField = "rotation"
ROUTE76.toNode = "TextTransform"

Scene35.children.append(ROUTE76)
Group77 = x3d.Group()
Group77.DEF = "BackgroundGroup"
Background78 = x3d.Background()
Background78.DEF = "GradualBackground"

Group77.children.append(Background78)
Script79 = x3d.Script()
Script79.DEF = "colorTypeConversionScript"
field80 = x3d.field()
field80.name = "colorInput"
field80.accessType = "inputOnly"
field80.type = "SFColor"

Script79.field.append(field80)
field81 = x3d.field()
field81.name = "colorsOutput"
field81.accessType = "outputOnly"
field81.type = "MFColor"

Script79.field.append(field81)

Script79.sourceCode = '''ecmascript:\n"+
"\n"+
"function colorInput (eventValue) // Example source code\n"+
"{\n"+
"   colorsOutput = new MFColor(eventValue); // assigning value sends output event\n"+
"// Browser.print('colorInput=' + eventValue + ', colorsOutput=' + colorsOutput + '\\n');\n"+
"}'''

Group77.children.append(Script79)
ColorInterpolator82 = x3d.ColorInterpolator()
ColorInterpolator82.DEF = "ColorAnimator"
ColorInterpolator82.key = [0,0.5,1]
ColorInterpolator82.keyValue = [0.9411765,1,1,0.29411766,0,0.50980395,0.9411765,1,1]
#AZURE to INDIGO and back again

Group77.children.append(ColorInterpolator82)
TimeSensor83 = x3d.TimeSensor()
TimeSensor83.DEF = "ColorClock"
TimeSensor83.cycleInterval = 60
TimeSensor83.loop = True

Group77.children.append(TimeSensor83)
ROUTE84 = x3d.ROUTE()
ROUTE84.fromField = "colorsOutput"
ROUTE84.fromNode = "colorTypeConversionScript"
ROUTE84.toField = "skyColor"
ROUTE84.toNode = "GradualBackground"

Group77.children.append(ROUTE84)
ROUTE85 = x3d.ROUTE()
ROUTE85.fromField = "value_changed"
ROUTE85.fromNode = "ColorAnimator"
ROUTE85.toField = "colorInput"
ROUTE85.toNode = "colorTypeConversionScript"

Group77.children.append(ROUTE85)
ROUTE86 = x3d.ROUTE()
ROUTE86.fromField = "fraction_changed"
ROUTE86.fromNode = "ColorClock"
ROUTE86.toField = "set_fraction"
ROUTE86.toNode = "ColorAnimator"

Group77.children.append(ROUTE86)

Scene35.children.append(Group77)
ProtoDeclare87 = x3d.ProtoDeclare()
ProtoDeclare87.name = "ArtDeco01Material"
ProtoDeclare87.appinfo = "tooltip: ArtDeco01Material prototype is a Material node"
ProtoInterface88 = x3d.ProtoInterface()
field89 = x3d.field()
field89.name = "description"
field89.accessType = "inputOutput"
field89.appinfo = "tooltip for descriptionField"
field89.type = "SFString"
field89.value = "ArtDeco01Material prototype is a Material node"

ProtoInterface88.field.append(field89)
field90 = x3d.field()
field90.name = "enabled"
field90.accessType = "inputOutput"
field90.type = "SFBool"
field90.value = True

ProtoInterface88.field.append(field90)

ProtoDeclare87.ProtoInterface = ProtoInterface88
ProtoBody91 = x3d.ProtoBody()
#Initial node of ProtoBody determines prototype node type
Material92 = x3d.Material()
Material92.ambientIntensity = 0.25
Material92.diffuseColor = [0.282435,0.085159,0.134462]
Material92.shininess = 0.127273
Material92.specularColor = [0.276305,0.11431,0.139857]

ProtoBody91.children.append(Material92)
#[HelloWorldProgram diagnostic] should be connected to scene graph: artDeco01ProtoDeclare.getNodeType()=\"Material\"
#presence of follow-on TouchSensor shows that additional nodes are allowed in ProtoBody after initial node, regardless of node types
TouchSensor93 = x3d.TouchSensor()
TouchSensor93.description = "within ProtoBody"
IS94 = x3d.IS()
connect95 = x3d.connect()
connect95.nodeField = "description"
connect95.protoField = "description"

IS94.connect.append(connect95)
connect96 = x3d.connect()
connect96.nodeField = "enabled"
connect96.protoField = "enabled"

IS94.connect.append(connect96)

TouchSensor93.IS = IS94

ProtoBody91.children.append(TouchSensor93)

ProtoDeclare87.ProtoBody = ProtoBody91

Scene35.children.append(ProtoDeclare87)
ExternProtoDeclare97 = x3d.ExternProtoDeclare()
ExternProtoDeclare97.name = "ArtDeco02Material"
ExternProtoDeclare97.appinfo = "this is a different Material node"
ExternProtoDeclare97.url = ["http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3d#ArtDeco02Material","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3dv#ArtDeco02Material"]
#[HelloWorldProgram diagnostic] artDeco02ExternProtoDeclare.getNodeType()=\"ERROR_UNKNOWN_EXTERNPROTODECLARE_NODE_TYPE: ExternProtoDeclare name='ArtDeco02Material' type cannot be remotely accessed at run time. TODO X3DJSAIL needs to add further capability that retrieves the ExternProtoDeclare file.\"
field98 = x3d.field()
field98.name = "description"
field98.accessType = "inputOutput"
field98.appinfo = "tooltip for descriptionField"
field98.type = "SFString"

ExternProtoDeclare97.field.append(field98)

Scene35.children.append(ExternProtoDeclare97)
#Tested ArtDeco01ProtoInstance, ArtDeco02ProtoInstance for improper node type when ProtoInstance is added in wrong place
Shape99 = x3d.Shape()
Shape99.DEF = "TestShape1"
Appearance100 = x3d.Appearance()
Appearance100.DEF = "TestAppearance1"
#ArtDeco01Material prototype goes here... TODO ensure setContainerField is handled in exported Java
ProtoInstance101 = x3d.ProtoInstance()
ProtoInstance101.name = "ArtDeco01Material"
#[HelloWorldProgram diagnostic] ArtDeco01ProtoInstance.getNodeType()=\"Material\"
fieldValue102 = x3d.fieldValue()
fieldValue102.name = "description"
fieldValue102.value = "ArtDeco01Material can substitute for a Material node"

ProtoInstance101.fieldValue.append(fieldValue102)

Appearance100.material = ProtoInstance101

Shape99.appearance = Appearance100
Sphere103 = x3d.Sphere()
Sphere103.radius = 0.001

Shape99.geometry = Sphere103

Scene35.children.append(Shape99)
Shape104 = x3d.Shape()
Shape104.DEF = "TestShape2"
Appearance105 = x3d.Appearance()
Appearance105.DEF = "TestAppearance2"
#ArtDeco02Material prototype goes here... TODO ensure setContainerField is handled in exported Java
ProtoInstance106 = x3d.ProtoInstance()
ProtoInstance106.name = "ArtDeco02Material"
ProtoInstance106.DEF = "ArtDeco02MaterialDEF"
#[HelloWorldProgram diagnostic] ArtDeco02ProtoInstance.getNodeType()=\"ERROR_UNKNOWN_EXTERNPROTODECLARE_NODE_TYPE: ExternProtoDeclare name='ArtDeco02Material' type cannot be remotely accessed at run time. TODO X3DJSAIL needs to add further capability that retrieves the ExternProtoDeclare file.\"
fieldValue107 = x3d.fieldValue()
fieldValue107.name = "description"
fieldValue107.value = "ArtDeco02Material can substitute for another Material node"

ProtoInstance106.fieldValue.append(fieldValue107)

Appearance105.material = ProtoInstance106

Shape104.appearance = Appearance105
Cone108 = x3d.Cone()
Cone108.bottomRadius = 0.001
Cone108.height = 0.001

Shape104.geometry = Cone108

Scene35.children.append(Shape104)
Shape109 = x3d.Shape()
Shape109.DEF = "TestShape3"
Appearance110 = x3d.Appearance()
Appearance110.DEF = "TestAppearance3"
#ArtDeco02Material ProtoInstance USE goes here. Note that name field is NOT defined as part of ProtoInstance USE.
ProtoInstance111 = x3d.ProtoInstance()
ProtoInstance111.USE = "ArtDeco02MaterialDEF"

Appearance110.material = ProtoInstance111

Shape109.appearance = Appearance110
Cylinder112 = x3d.Cylinder()
Cylinder112.height = 0.001
Cylinder112.radius = 0.001

Shape109.geometry = Cylinder112

Scene35.children.append(Shape109)
Inline113 = x3d.Inline()
Inline113.DEF = "inlineSceneDef"
Inline113.url = ["someOtherScene.x3d","https://www.web3d.org/specifications/java/examples/someOtherScene.x3d"]

Scene35.children.append(Inline113)
IMPORT114 = x3d.IMPORT()
IMPORT114.AS = "WorldInfoDEF2"
IMPORT114.importedDEF = "WorldInfoDEF"
IMPORT114.inlineDEF = "inlineSceneDef"

Scene35.children.append(IMPORT114)
EXPORT115 = x3d.EXPORT()
EXPORT115.AS = "WorldInfoDEF3"
EXPORT115.localDEF = "WorldInfoDEF"

Scene35.children.append(EXPORT115)
ProtoDeclare116 = x3d.ProtoDeclare()
ProtoDeclare116.name = "MaterialModulator"
ProtoDeclare116.appinfo = "mimic a Material node and modulate fields as an animation effect"
ProtoDeclare116.documentation = "http://x3dgraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/MaterialModulatorIndex.html"
ProtoInterface117 = x3d.ProtoInterface()
field118 = x3d.field()
field118.name = "enabled"
field118.accessType = "inputOutput"
field118.type = "SFBool"
field118.value = True

ProtoInterface117.field.append(field118)
field119 = x3d.field()
field119.name = "diffuseColor"
field119.accessType = "inputOutput"
field119.type = "SFColor"
field119.value = [0,0,0]

ProtoInterface117.field.append(field119)
field120 = x3d.field()
field120.name = "emissiveColor"
field120.accessType = "inputOutput"
field120.type = "SFColor"
field120.value = [0.05,0.05,0.5]

ProtoInterface117.field.append(field120)
field121 = x3d.field()
field121.name = "specularColor"
field121.accessType = "inputOutput"
field121.type = "SFColor"
field121.value = [0,0,0]

ProtoInterface117.field.append(field121)
field122 = x3d.field()
field122.name = "transparency"
field122.accessType = "inputOutput"
field122.type = "SFFloat"
field122.value = 0

ProtoInterface117.field.append(field122)
field123 = x3d.field()
field123.name = "shininess"
field123.accessType = "inputOutput"
field123.type = "SFFloat"
field123.value = 0

ProtoInterface117.field.append(field123)
field124 = x3d.field()
field124.name = "ambientIntensity"
field124.accessType = "inputOutput"
field124.type = "SFFloat"
field124.value = 0

ProtoInterface117.field.append(field124)

ProtoDeclare116.ProtoInterface = ProtoInterface117
ProtoBody125 = x3d.ProtoBody()
Material126 = x3d.Material()
Material126.DEF = "MaterialNode"
IS127 = x3d.IS()
connect128 = x3d.connect()
connect128.nodeField = "diffuseColor"
connect128.protoField = "diffuseColor"

IS127.connect.append(connect128)
connect129 = x3d.connect()
connect129.nodeField = "emissiveColor"
connect129.protoField = "emissiveColor"

IS127.connect.append(connect129)
connect130 = x3d.connect()
connect130.nodeField = "specularColor"
connect130.protoField = "specularColor"

IS127.connect.append(connect130)
connect131 = x3d.connect()
connect131.nodeField = "transparency"
connect131.protoField = "transparency"

IS127.connect.append(connect131)
connect132 = x3d.connect()
connect132.nodeField = "shininess"
connect132.protoField = "shininess"

IS127.connect.append(connect132)
connect133 = x3d.connect()
connect133.nodeField = "ambientIntensity"
connect133.protoField = "ambientIntensity"

IS127.connect.append(connect133)

Material126.IS = IS127

ProtoBody125.children.append(Material126)
#Only first node (the node type) is renderable, others are along for the ride
Script134 = x3d.Script()
Script134.DEF = "MaterialModulatorScript"
field135 = x3d.field()
field135.name = "enabled"
field135.accessType = "inputOutput"
field135.type = "SFBool"

Script134.field.append(field135)
field136 = x3d.field()
field136.name = "diffuseColor"
field136.accessType = "inputOutput"
field136.type = "SFColor"

Script134.field.append(field136)
field137 = x3d.field()
field137.name = "newColor"
field137.accessType = "outputOnly"
field137.type = "SFColor"

Script134.field.append(field137)
field138 = x3d.field()
field138.name = "clockTrigger"
field138.accessType = "inputOnly"
field138.type = "SFTime"

Script134.field.append(field138)
IS139 = x3d.IS()
connect140 = x3d.connect()
connect140.nodeField = "enabled"
connect140.protoField = "enabled"

IS139.connect.append(connect140)
connect141 = x3d.connect()
connect141.nodeField = "diffuseColor"
connect141.protoField = "diffuseColor"

IS139.connect.append(connect141)

Script134.IS = IS139

Script134.sourceCode = '''ecmascript:\n"+
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

ProtoBody125.children.append(Script134)

ProtoDeclare116.ProtoBody = ProtoBody125

Scene35.children.append(ProtoDeclare116)
#Test success: declarative statement createDeclarativeShapeTests()
Group142 = x3d.Group()
Group142.DEF = "DeclarativeGroupExample"
Shape143 = x3d.Shape()
MetadataString144 = x3d.MetadataString()
MetadataString144.name = "findThisNameValue"
MetadataString144.DEF = "FindableMetadataStringTest"
MetadataString144.value = ["test case"]

Shape143.metadata.append(MetadataString144)
Appearance145 = x3d.Appearance()
Appearance145.DEF = "DeclarativeAppearanceExample"
#DeclarativeMaterialExample gets overridden by subsequently added MaterialModulator ProtoInstance
ProtoInstance146 = x3d.ProtoInstance()
ProtoInstance146.name = "MaterialModulator"
ProtoInstance146.DEF = "MyMaterialModulator"

Appearance145.material = ProtoInstance146

Shape143.appearance = Appearance145
Cone147 = x3d.Cone()
Cone147.bottom = False
Cone147.bottomRadius = 0.05
Cone147.height = 0.1

Shape143.geometry = Cone147

Group142.children.append(Shape143)
#Test success: declarativeGroup.addChild() singleton pipeline method

Scene35.children.append(Group142)
#Test success: declarative statement addChild()
#Test success: x3dModel.findNodeByDEF(DeclarativeAppearanceExample) = <Appearance DEF='DeclarativeAppearanceExample'/> i.e. <Appearance DEF='DeclarativeAppearanceExample'> <!- - DeclarativeMaterialExample gets overridden by subsequently added MaterialModulator ProtoInstance - -> <ProtoInstance DEF='MyMaterialModulator' name='MaterialModulator' containerField='material'/> </Appearance>
#Test success: x3dModel.findElementByNameValue(findThisNameValue) = <MetadataString DEF='FindableMetadataStringTest' name='findThisNameValue' value='\"test case\"'/>
#Test success: x3dModel.findElementByNameValue(\"ArtDeco01Material\", \"ProtoDeclare\") found
#Test success: x3dModel.findElementByNameValue(\"MaterialModulator\", \"ProtoDeclare\") found
#Test success: x3dModel.findElementByNameValue(\"MaterialModulator\", \"ProtoInstance\") found
Group148 = x3d.Group()
Group148.DEF = "TestFieldObjectsGroup"
#testFieldObjects() results
#SFBool default=true, true=true, false=false, negate()=true
#MFBool default=, initial=true false true, negate()=false true false
#SFFloat default=0.0, initial=1.0, setValue(2)=2.0, setValue(3.0f)=3.0, setValue(4.0)=4.0
#MFFloat default=, initial=1 2 3, append(5)=1 2 3 5, inserts(3,4)(0,0)=0 1 2 3 4 5, append(6)=0 1 2 3 4 5 6, size()=7
#... get1Value[3]=3.0, remove[1]=0 2 3 4 5 6, set1Value(0,10)=10 2 3 4 5 6, multiply(2)=20 4 6 8 10 12, clear=
#SFVec3f default=0 0 0, initial=1 2 3, setValue=4 5 6, multiply(2)=8 10 12, normalize()=0.45584232 0.5698029 0.68376344, regex matches()=true
#regex test SFVec3f().matches(\"1 2 3\")=true, regex test SFVec3f().matches(\"1 2 3 4\")=false, regex test (SFRotationObject.matches(\"0 0 0 0\")=true, failure detecting illegal (zero axis) rotation value

Scene35.children.append(Group148)
Sound149 = x3d.Sound()
Sound149.location = [0,1.6,0]
#set sound-ellipsoid location height at 1.6m to match typical avatar height
AudioClip150 = x3d.AudioClip()
AudioClip150.description = "chimes"
AudioClip150.url = ["chimes.wav","https://www.web3d.org/x3d/content/examples/ConformanceNist/Sounds/AudioClip/chimes.wav"]
#Scene example fragment from https://www.web3d.org/x3d/content/examples/ConformanceNist/Sounds/AudioClip/default.x3d

Sound149.source.append(AudioClip150)

Scene35.children.append(Sound149)
Sound151 = x3d.Sound()
Sound151.location = [0,1.6,0]
#set sound-ellipsoid location height at 1.6m to match typical avatar height
MovieTexture152 = x3d.MovieTexture()
MovieTexture152.description = "mpgsys.mpg from ConformanceNist suite"
MovieTexture152.url = ["mpgsys.mpg","https://www.web3d.org/x3d/content/examples/ConformanceNist/Appearance/MovieTexture/mpgsys.mpg"]
#Scene example fragment from https://www.web3d.org/x3d/content/examples/ConformanceNist/Appearance/MovieTexture/mpeg1-systems.x3d
#Expected containerField='source', allowed containerField values=\"texture\" \"source\" \"back\" \"bottom\" \"front\" \"left\" \"right\" \"top\" \"backTexture\" \"bottomTexture\" \"frontTexture\" \"leftTexture\" \"rightTexture\" \"topTexture\" \"watchList\"

Sound151.source.append(MovieTexture152)

Scene35.children.append(Sound151)
#Test success: AnchorObject.isNode()=true, siteAnchor.isNode()=true
#Test success: AnchorObject.isStatement()=false, siteAnchor.isStatement()=false
#Test success: ROUTEObject.isNode()=false, orbitPositionROUTE.isNode()=false
#Test success: ROUTEObject.isStatement()=true, orbitPositionROUTE.isStatement()=true
#Test success: CommentsBlock.isNode()=false, testComments.isNode()=false
#Test failure: CommentsBlock.isStatement()=true, testComments.isStatement()=true
Shape153 = x3d.Shape()
Shape153.DEF = "ExtrusionShape"
#ExampleExtrusion isCrossSectionClosed()=true, crossSection='[1.0, 1.0, 1.0, -1.0, -1.0, -1.0, -1.0, 1.0, 1.0, 1.0]'
#ExampleExtrusion isSpineClosed()=false, spine='[0.0, 0.0, 0.0, 0.0, 1.0, 0.0]'
Appearance154 = x3d.Appearance()
Appearance154.DEF = "TransparentAppearance"
Material155 = x3d.Material()
Material155.transparency = 1

Appearance154.material = Material155

Shape153.appearance = Appearance154
Extrusion156 = x3d.Extrusion()
Extrusion156.DEF = "ExampleExtrusion"

Shape153.geometry = Extrusion156

Scene35.children.append(Shape153)
Group157 = x3d.Group()
#Test MFNode children array as an ordered list consisting of comments, statements, ProtoInstance and nodes
ProtoDeclare158 = x3d.ProtoDeclare()
ProtoDeclare158.name = "NewWorldInfo"
ProtoInterface159 = x3d.ProtoInterface()
field160 = x3d.field()
field160.name = "description"
field160.accessType = "initializeOnly"
field160.type = "SFString"

ProtoInterface159.field.append(field160)

ProtoDeclare158.ProtoInterface = ProtoInterface159
ProtoBody161 = x3d.ProtoBody()
WorldInfo162 = x3d.WorldInfo()

ProtoBody161.children.append(WorldInfo162)

ProtoDeclare158.ProtoBody = ProtoBody161

Group157.children.append(ProtoDeclare158)
Group163 = x3d.Group()
Group163.DEF = "Node2"
#intentionally empty

Group157.children.append(Group163)
Transform164 = x3d.Transform()
Transform164.DEF = "Node4"
#intentionally empty

Group157.children.append(Transform164)
#Test satisfactorily creates MFNode children array as an ordered list with mixed content

Scene35.children.append(Group157)
ProtoDeclare165 = x3d.ProtoDeclare()
ProtoDeclare165.name = "ShaderProto"
ProtoBody166 = x3d.ProtoBody()
ProgramShader167 = x3d.ProgramShader()

ProtoBody166.children.append(ProgramShader167)

ProtoDeclare165.ProtoBody = ProtoBody166

Scene35.children.append(ProtoDeclare165)
Shape168 = x3d.Shape()
Appearance169 = x3d.Appearance()
#Test MFNode shaders array as an ordered list consisting of comments, ProtoInstance and nodes
#Test satisfactorily creates MFNode shaders array as an ordered list with mixed content
ProgramShader170 = x3d.ProgramShader()
ProgramShader170.DEF = "TestShader1"
ShaderProgram171 = x3d.ShaderProgram()
ShaderProgram171.DEF = "TestShader2"
ShaderProgram171.type = "VERTEX"

ProgramShader170.programs.append(ShaderProgram171)

Appearance169.shaders.append(ProgramShader170)
ProtoInstance172 = x3d.ProtoInstance()
ProtoInstance172.name = "ShaderProto"
ProtoInstance172.DEF = "TestShader3"

Appearance169.shaders.append(ProtoInstance172)
ComposedShader173 = x3d.ComposedShader()
ComposedShader173.DEF = "TestShader4"
ShaderPart174 = x3d.ShaderPart()
ShaderPart174.DEF = "TestShader5"
ShaderPart174.type = "VERTEX"

ComposedShader173.parts.append(ShaderPart174)

Appearance169.shaders.append(ComposedShader173)

Shape168.appearance = Appearance169

Scene35.children.append(Shape168)
Transform175 = x3d.Transform()
Transform175.DEF = "SpecialtyNodes"
CADLayer176 = x3d.CADLayer()
CADAssembly177 = x3d.CADAssembly()
CADPart178 = x3d.CADPart()
CADFace179 = x3d.CADFace()

CADPart178.children.append(CADFace179)

CADAssembly177.children.append(CADPart178)

CADLayer176.children.append(CADAssembly177)

Transform175.children.append(CADLayer176)
EspduTransform180 = x3d.EspduTransform()

Transform175.children.append(EspduTransform180)
ReceiverPdu181 = x3d.ReceiverPdu()

Transform175.children.append(ReceiverPdu181)
SignalPdu182 = x3d.SignalPdu()

Transform175.children.append(SignalPdu182)
TransmitterPdu183 = x3d.TransmitterPdu()

Transform175.children.append(TransmitterPdu183)
DISEntityManager184 = x3d.DISEntityManager()
DISEntityTypeMapping185 = x3d.DISEntityTypeMapping()

DISEntityManager184.children.append(DISEntityTypeMapping185)

Transform175.children.append(DISEntityManager184)

Scene35.children.append(Transform175)

X3D0.Scene = Scene35
f = open("././Json_RoundTrip.x3d", "w")
f.write(X3D0.XML())
f.close()
