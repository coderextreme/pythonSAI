print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.cssClass = "x3dModel.class"
X3D0.profile = "Full"
X3D0.style = "x3dModel.style"
X3D0.version = "4.0"
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
meta18.content = "29 April 2023"

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
meta21.content = "Netbeans https://www.netbeans.org"

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

X3D0.head = head1
Scene32 = x3d.Scene()
ViewpointGroup33 = x3d.ViewpointGroup()
ViewpointGroup33.description = "Available viewpoints"
Viewpoint34 = x3d.Viewpoint()
Viewpoint34.DEF = "DefaultView"
Viewpoint34.description = "Hello X3DJSAIL"

ViewpointGroup33.children.append(Viewpoint34)
Viewpoint35 = x3d.Viewpoint()
Viewpoint35.DEF = "TopDownView"
Viewpoint35.description = "top-down view from above"
Viewpoint35.orientation = [1,0,0,-1.570796]
Viewpoint35.position = [0,100,0]

ViewpointGroup33.children.append(Viewpoint35)

Scene32.children.append(ViewpointGroup33)
NavigationInfo36 = x3d.NavigationInfo()
NavigationInfo36.type = ["EXAMINE","FLY","ANY"]

Scene32.children.append(NavigationInfo36)
WorldInfo37 = x3d.WorldInfo()
WorldInfo37.DEF = "WorldInfoDEF"
WorldInfo37.cssClass = "worldInfoNode.class"
WorldInfo37.style = "worldInfoNode.style"
WorldInfo37.title = "HelloWorldProgram produced by X3D Java SAI Library (X3DJSAIL)"

Scene32.children.append(WorldInfo37)
WorldInfo38 = x3d.WorldInfo()
WorldInfo38.USE = "WorldInfoDEF"

Scene32.children.append(WorldInfo38)
WorldInfo39 = x3d.WorldInfo()
WorldInfo39.USE = "WorldInfoDEF"

Scene32.children.append(WorldInfo39)
MetadataString40 = x3d.MetadataString()
MetadataString40.name = "test"
MetadataString40.DEF = "scene.addChildMetadata"
MetadataString40.value = ["Top-level root Metadata node beneath Scene needs to be one of '-children' in JSON encoding"]

Scene32.metadata = MetadataString40
LayerSet41 = x3d.LayerSet()
LayerSet41.DEF = "scene.addChildLayerSetTest"

Scene32.layerSet = LayerSet41
Transform42 = x3d.Transform()
Transform42.DEF = "LogoGeometryTransform"
Transform42.translation = [0,1.5,0]
Anchor43 = x3d.Anchor()
Anchor43.DEF = "siteAnchor"
Anchor43.description = "select for X3D Java SAI Library (X3DJSAIL) description"
Anchor43.url = ["../X3DJSAIL.html","https://www.web3d.org/specifications/java/X3DJSAIL.html"]
Shape44 = x3d.Shape()
Shape44.DEF = "BoxShape"
Appearance45 = x3d.Appearance()
Material46 = x3d.Material()
Material46.DEF = "GreenMaterial"
Material46.diffuseColor = [0,1,1]
Material46.emissiveColor = [0.8,0,0]
Material46.transparency = 0.1

Appearance45.material = Material46
ImageTexture47 = x3d.ImageTexture()
ImageTexture47.url = ["images/X3dJavaSceneAccessInterfaceSaiLibrary.png","https://www.web3d.org/specifications/java/examples/images/X3dJavaSceneAccessInterfaceSaiLibrary.png"]

Appearance45.texture = ImageTexture47

Shape44.appearance = Appearance45
Box48 = x3d.Box()
Box48.DEF = "test-NMTOKEN_regex.0123456789"
Box48.cssClass = "untextured"

Shape44.geometry = Box48

Anchor43.children.append(Shape44)

Transform42.children.append(Anchor43)

Scene32.children.append(Transform42)
Shape49 = x3d.Shape()
Shape49.DEF = "LineShape"
Appearance50 = x3d.Appearance()
Material51 = x3d.Material()
Material51.emissiveColor = [0.6,0.19607843,0.8]

Appearance50.material = Material51

Shape49.appearance = Appearance50
IndexedLineSet52 = x3d.IndexedLineSet()
IndexedLineSet52.coordIndex = [0,1,2,3,4,0]
#Coordinate 3-tuple point count: 6
Coordinate53 = x3d.Coordinate()
Coordinate53.point = (0.0000,1.5000,0.0000,2.0000,1.5000,0.0000,2.0000,1.5000,-2.0000,-2.0000,1.5000,-2.0000,-2.0000,1.5000,0.0000,0.0000,1.5000,0.0000)

IndexedLineSet52.coord = Coordinate53

Shape49.geometry = IndexedLineSet52

Scene32.children.append(Shape49)
PositionInterpolator54 = x3d.PositionInterpolator()
PositionInterpolator54.DEF = "BoxPathAnimator"
PositionInterpolator54.key = [0,0.125,0.375,0.625,0.875,1]
PositionInterpolator54.keyValue = (0.0000,1.5000,0.0000,2.0000,1.5000,0.0000,2.0000,1.5000,-2.0000,-2.0000,1.5000,-2.0000,-2.0000,1.5000,0.0000,0.0000,1.5000,0.0000)

Scene32.children.append(PositionInterpolator54)
TimeSensor55 = x3d.TimeSensor()
TimeSensor55.DEF = "OrbitClock"
TimeSensor55.cycleInterval = 8
TimeSensor55.loop = True

Scene32.children.append(TimeSensor55)
ROUTE56 = x3d.ROUTE()
ROUTE56.fromField = "fraction_changed"
ROUTE56.fromNode = "OrbitClock"
ROUTE56.toField = "set_fraction"
ROUTE56.toNode = "BoxPathAnimator"

Scene32.children.append(ROUTE56)
ROUTE57 = x3d.ROUTE()
ROUTE57.fromField = "value_changed"
ROUTE57.fromNode = "BoxPathAnimator"
ROUTE57.toField = "set_translation"
ROUTE57.toNode = "LogoGeometryTransform"

Scene32.children.append(ROUTE57)
Transform58 = x3d.Transform()
Transform58.DEF = "TextTransform"
Transform58.translation = [0,-1.5,0]
Shape59 = x3d.Shape()
Appearance60 = x3d.Appearance()
Material61 = x3d.Material()
Material61.USE = "GreenMaterial"

Appearance60.material = Material61

Shape59.appearance = Appearance60
Text62 = x3d.Text()
Text62.string = ["X3D Java","SAI Library","X3DJSAIL"]
#Comment example A, plain quotation marks: He said, \"Immel did it!\"
#Comment example B, XML character entities: He said, &quot;Immel did it!&quot;
MetadataSet63 = x3d.MetadataSet()
MetadataSet63.name = "EscapedQuotationMarksMetadataSet"
MetadataString64 = x3d.MetadataString()
MetadataString64.name = "quotesTestC"
MetadataString64.value = ["MFString example C, backslash-escaped quotes: He said, \"Immel did it!\""]

MetadataSet63.value = MetadataString64
MetadataString65 = x3d.MetadataString()
MetadataString65.name = "extraChildTest"
MetadataString65.value = ["checks MetadataSet addValue() method"]

MetadataSet63.value = MetadataString65

Text62.metadata = MetadataSet63
FontStyle66 = x3d.FontStyle()
FontStyle66.justify = ["MIDDLE","MIDDLE"]

Text62.fontStyle = FontStyle66

Shape59.geometry = Text62

Transform58.children.append(Shape59)
Collision67 = x3d.Collision()
#test containerField='proxy'
Shape68 = x3d.Shape()
Shape68.DEF = "ProxyShape"
#alternative XML encoding: Text string='\"One, Two, Comment\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\"'
#alternative XML encoding: Text string='\"One, Two, Comment\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\" \"\"'
#alternative Java source: .setString(new String [] {\"One, Two, Comment\", \"\", \"He said, \\\"\"Immel did it!\\\"\"\"})
#reference: https://www.web3d.org/x3d/content/examples/Basic/X3dSpecifications/StringArrayEncodingExamplesIndex.html
Text69 = x3d.Text()
Text69.string = ["One, Two, Text","","He said, \"Immel did it!\" \"\""]

Shape68.geometry = Text69

Collision67.proxy = Shape68

Transform58.children.append(Collision67)
#It's a beautiful world
#... for you!
#https://en.wikipedia.org/wiki/Beautiful_World_(Devo_song)

Scene32.children.append(Transform58)
#repeatedly spin 180 degrees as a readable special effect
OrientationInterpolator70 = x3d.OrientationInterpolator()
OrientationInterpolator70.DEF = "SpinInterpolator"
OrientationInterpolator70.key = [0,0.5,1]
OrientationInterpolator70.keyValue = (0.0000,1.0000,0.0000,4.7124,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,1.5708)

Scene32.children.append(OrientationInterpolator70)
TimeSensor71 = x3d.TimeSensor()
TimeSensor71.DEF = "SpinClock"
TimeSensor71.cycleInterval = 5
TimeSensor71.loop = True

Scene32.children.append(TimeSensor71)
ROUTE72 = x3d.ROUTE()
ROUTE72.fromField = "fraction_changed"
ROUTE72.fromNode = "SpinClock"
ROUTE72.toField = "set_fraction"
ROUTE72.toNode = "SpinInterpolator"

Scene32.children.append(ROUTE72)
ROUTE73 = x3d.ROUTE()
ROUTE73.fromField = "value_changed"
ROUTE73.fromNode = "SpinInterpolator"
ROUTE73.toField = "rotation"
ROUTE73.toNode = "TextTransform"

Scene32.children.append(ROUTE73)
Group74 = x3d.Group()
Group74.DEF = "BackgroundGroup"
Background75 = x3d.Background()
Background75.DEF = "GradualBackground"

Group74.children.append(Background75)
Script76 = x3d.Script()
Script76.DEF = "colorTypeConversionScript"
field77 = x3d.field()
field77.name = "colorInput"
field77.accessType = "inputOnly"
field77.type = "SFColor"

Script76.field.append(field77)
field78 = x3d.field()
field78.name = "colorsOutput"
field78.accessType = "outputOnly"
field78.type = "MFColor"

Script76.field.append(field78)

Script76.sourceCode = '''ecmascript:\n"+
"\n"+
"function colorInput (eventValue) // Example source code\n"+
"{\n"+
"   colorsOutput = new MFColor(eventValue); // assigning value sends output event\n"+
"// Browser.print('colorInput=' + eventValue + ', colorsOutput=' + colorsOutput + '\\n');\n"+
"}'''

Group74.children.append(Script76)
ColorInterpolator79 = x3d.ColorInterpolator()
ColorInterpolator79.DEF = "ColorAnimator"
ColorInterpolator79.key = [0,0.5,1]
ColorInterpolator79.keyValue = [0.9411765,1,1,0.29411766,0,0.50980395,0.9411765,1,1]
#AZURE to INDIGO and back again

Group74.children.append(ColorInterpolator79)
TimeSensor80 = x3d.TimeSensor()
TimeSensor80.DEF = "ColorClock"
TimeSensor80.cycleInterval = 60
TimeSensor80.loop = True

Group74.children.append(TimeSensor80)
ROUTE81 = x3d.ROUTE()
ROUTE81.fromField = "colorsOutput"
ROUTE81.fromNode = "colorTypeConversionScript"
ROUTE81.toField = "skyColor"
ROUTE81.toNode = "GradualBackground"

Group74.children.append(ROUTE81)
ROUTE82 = x3d.ROUTE()
ROUTE82.fromField = "value_changed"
ROUTE82.fromNode = "ColorAnimator"
ROUTE82.toField = "colorInput"
ROUTE82.toNode = "colorTypeConversionScript"

Group74.children.append(ROUTE82)
ROUTE83 = x3d.ROUTE()
ROUTE83.fromField = "fraction_changed"
ROUTE83.fromNode = "ColorClock"
ROUTE83.toField = "set_fraction"
ROUTE83.toNode = "ColorAnimator"

Group74.children.append(ROUTE83)

Scene32.children.append(Group74)
ProtoDeclare84 = x3d.ProtoDeclare()
ProtoDeclare84.name = "ArtDeco01Material"
ProtoDeclare84.appinfo = "tooltip: ArtDeco01Material prototype is a Material node"
ProtoInterface85 = x3d.ProtoInterface()
field86 = x3d.field()
field86.name = "description"
field86.accessType = "inputOutput"
field86.appinfo = "tooltip for descriptionField"
field86.type = "SFString"
field86.value = "ArtDeco01Material prototype is a Material node"

ProtoInterface85.field.append(field86)
field87 = x3d.field()
field87.name = "enabled"
field87.accessType = "inputOutput"
field87.type = "SFBool"
field87.value = True

ProtoInterface85.field.append(field87)

ProtoDeclare84.ProtoInterface = ProtoInterface85
ProtoBody88 = x3d.ProtoBody()
#Initial node of ProtoBody determines prototype node type
Material89 = x3d.Material()
Material89.ambientIntensity = 0.25
Material89.diffuseColor = [0.282435,0.085159,0.134462]
Material89.shininess = 0.127273
Material89.specularColor = [0.276305,0.11431,0.139857]

ProtoBody88.children.append(Material89)
#[HelloWorldProgram diagnostic] should be connected to scene graph: artDeco01ProtoDeclare.getNodeType()=\"Material\"
#presence of follow-on TouchSensor shows that additional nodes are allowed in ProtoBody after initial node, regardless of node types
TouchSensor90 = x3d.TouchSensor()
TouchSensor90.description = "within ProtoBody"
IS91 = x3d.IS()
connect92 = x3d.connect()
connect92.nodeField = "description"
connect92.protoField = "description"

IS91.connect.append(connect92)
connect93 = x3d.connect()
connect93.nodeField = "enabled"
connect93.protoField = "enabled"

IS91.connect.append(connect93)

TouchSensor90.IS = IS91

ProtoBody88.children.append(TouchSensor90)

ProtoDeclare84.ProtoBody = ProtoBody88

Scene32.children.append(ProtoDeclare84)
ExternProtoDeclare94 = x3d.ExternProtoDeclare()
ExternProtoDeclare94.name = "ArtDeco02Material"
ExternProtoDeclare94.appinfo = "this is a different Material node"
ExternProtoDeclare94.url = ["https://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3d#ArtDeco02Material","https://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3dv#ArtDeco02Material"]
#[HelloWorldProgram diagnostic] artDeco02ExternProtoDeclare.getNodeType()=\"ERROR_UNKNOWN_EXTERNPROTODECLARE_NODE_TYPE: ExternProtoDeclare name='ArtDeco02Material' type cannot be remotely accessed at run time. TODO X3DJSAIL needs to add further capability that retrieves the ExternProtoDeclare file.\"
field95 = x3d.field()
field95.name = "description"
field95.accessType = "inputOutput"
field95.appinfo = "tooltip for descriptionField"
field95.type = "SFString"

ExternProtoDeclare94.field.append(field95)

Scene32.children.append(ExternProtoDeclare94)
#Tested ArtDeco01ProtoInstance, ArtDeco02ProtoInstance for improper node type when ProtoInstance is added in wrong place
Shape96 = x3d.Shape()
Shape96.DEF = "TestShape1"
Appearance97 = x3d.Appearance()
Appearance97.DEF = "TestAppearance1"
#ArtDeco01Material prototype goes here... TODO ensure setContainerField is handled in exported Java
ProtoInstance98 = x3d.ProtoInstance()
ProtoInstance98.name = "ArtDeco01Material"
#[HelloWorldProgram diagnostic] ArtDeco01ProtoInstance.getNodeType()=\"Material\"
fieldValue99 = x3d.fieldValue()
fieldValue99.name = "description"
fieldValue99.value = "ArtDeco01Material can substitute for a Material node"

ProtoInstance98.fieldValue.append(fieldValue99)

Appearance97.material = ProtoInstance98

Shape96.appearance = Appearance97
Sphere100 = x3d.Sphere()
Sphere100.radius = 0.001

Shape96.geometry = Sphere100

Scene32.children.append(Shape96)
Shape101 = x3d.Shape()
Shape101.DEF = "TestShape2"
Appearance102 = x3d.Appearance()
Appearance102.DEF = "TestAppearance2"
#ArtDeco02Material prototype goes here... TODO ensure setContainerField is handled in exported Java
ProtoInstance103 = x3d.ProtoInstance()
ProtoInstance103.name = "ArtDeco02Material"
ProtoInstance103.DEF = "ArtDeco02MaterialDEF"
#[HelloWorldProgram diagnostic] ArtDeco02ProtoInstance.getNodeType()=\"ERROR_UNKNOWN_EXTERNPROTODECLARE_NODE_TYPE: ExternProtoDeclare name='ArtDeco02Material' type cannot be remotely accessed at run time. TODO X3DJSAIL needs to add further capability that retrieves the ExternProtoDeclare file.\"
fieldValue104 = x3d.fieldValue()
fieldValue104.name = "description"
fieldValue104.value = "ArtDeco02Material can substitute for another Material node"

ProtoInstance103.fieldValue.append(fieldValue104)

Appearance102.material = ProtoInstance103

Shape101.appearance = Appearance102
Cone105 = x3d.Cone()
Cone105.bottomRadius = 0.001
Cone105.height = 0.001

Shape101.geometry = Cone105

Scene32.children.append(Shape101)
Shape106 = x3d.Shape()
Shape106.DEF = "TestShape3"
Appearance107 = x3d.Appearance()
Appearance107.DEF = "TestAppearance3"
#ArtDeco02Material ProtoInstance USE goes here. Note that name field is NOT defined as part of ProtoInstance USE.
ProtoInstance108 = x3d.ProtoInstance()
ProtoInstance108.USE = "ArtDeco02MaterialDEF"

Appearance107.material = ProtoInstance108

Shape106.appearance = Appearance107
Cylinder109 = x3d.Cylinder()
Cylinder109.height = 0.001
Cylinder109.radius = 0.001

Shape106.geometry = Cylinder109

Scene32.children.append(Shape106)
Inline110 = x3d.Inline()
Inline110.DEF = "inlineScene"
Inline110.url = ["someOtherScene.x3d","https://www.web3d.org/specifications/java/examples/someOtherScene.x3d"]

Scene32.children.append(Inline110)
IMPORT111 = x3d.IMPORT()
IMPORT111.AS = "WorldInfoDEF2"
IMPORT111.importedDEF = "WorldInfoDEF"
IMPORT111.inlineDEF = "inlineScene"

Scene32.children.append(IMPORT111)
EXPORT112 = x3d.EXPORT()
EXPORT112.AS = "WorldInfoDEF3"
EXPORT112.localDEF = "WorldInfoDEF"

Scene32.children.append(EXPORT112)
ProtoDeclare113 = x3d.ProtoDeclare()
ProtoDeclare113.name = "MaterialModulator"
ProtoDeclare113.appinfo = "mimic a Material node and modulate fields as an animation effect"
ProtoDeclare113.documentation = "https://x3dgraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/MaterialModulatorIndex.html"
ProtoInterface114 = x3d.ProtoInterface()
field115 = x3d.field()
field115.name = "enabled"
field115.accessType = "inputOutput"
field115.type = "SFBool"
field115.value = True

ProtoInterface114.field.append(field115)
field116 = x3d.field()
field116.name = "diffuseColor"
field116.accessType = "inputOutput"
field116.type = "SFColor"
field116.value = [0,0,0]

ProtoInterface114.field.append(field116)
field117 = x3d.field()
field117.name = "emissiveColor"
field117.accessType = "inputOutput"
field117.type = "SFColor"
field117.value = [0.05,0.05,0.5]

ProtoInterface114.field.append(field117)
field118 = x3d.field()
field118.name = "specularColor"
field118.accessType = "inputOutput"
field118.type = "SFColor"
field118.value = [0,0,0]

ProtoInterface114.field.append(field118)
field119 = x3d.field()
field119.name = "transparency"
field119.accessType = "inputOutput"
field119.type = "SFFloat"
field119.value = 0

ProtoInterface114.field.append(field119)
field120 = x3d.field()
field120.name = "shininess"
field120.accessType = "inputOutput"
field120.type = "SFFloat"
field120.value = 0

ProtoInterface114.field.append(field120)
field121 = x3d.field()
field121.name = "ambientIntensity"
field121.accessType = "inputOutput"
field121.type = "SFFloat"
field121.value = 0

ProtoInterface114.field.append(field121)

ProtoDeclare113.ProtoInterface = ProtoInterface114
ProtoBody122 = x3d.ProtoBody()
Material123 = x3d.Material()
Material123.DEF = "MaterialNode"
IS124 = x3d.IS()
connect125 = x3d.connect()
connect125.nodeField = "diffuseColor"
connect125.protoField = "diffuseColor"

IS124.connect.append(connect125)
connect126 = x3d.connect()
connect126.nodeField = "emissiveColor"
connect126.protoField = "emissiveColor"

IS124.connect.append(connect126)
connect127 = x3d.connect()
connect127.nodeField = "specularColor"
connect127.protoField = "specularColor"

IS124.connect.append(connect127)
connect128 = x3d.connect()
connect128.nodeField = "transparency"
connect128.protoField = "transparency"

IS124.connect.append(connect128)
connect129 = x3d.connect()
connect129.nodeField = "shininess"
connect129.protoField = "shininess"

IS124.connect.append(connect129)
connect130 = x3d.connect()
connect130.nodeField = "ambientIntensity"
connect130.protoField = "ambientIntensity"

IS124.connect.append(connect130)

Material123.IS = IS124

ProtoBody122.children.append(Material123)
#Only first node (the node type) is renderable, others are along for the ride
Script131 = x3d.Script()
Script131.DEF = "MaterialModulatorScript"
field132 = x3d.field()
field132.name = "enabled"
field132.accessType = "inputOutput"
field132.type = "SFBool"

Script131.field.append(field132)
field133 = x3d.field()
field133.name = "diffuseColor"
field133.accessType = "inputOutput"
field133.type = "SFColor"

Script131.field.append(field133)
field134 = x3d.field()
field134.name = "newColor"
field134.accessType = "outputOnly"
field134.type = "SFColor"

Script131.field.append(field134)
field135 = x3d.field()
field135.name = "clockTrigger"
field135.accessType = "inputOnly"
field135.type = "SFTime"

Script131.field.append(field135)
IS136 = x3d.IS()
connect137 = x3d.connect()
connect137.nodeField = "enabled"
connect137.protoField = "enabled"

IS136.connect.append(connect137)
connect138 = x3d.connect()
connect138.nodeField = "diffuseColor"
connect138.protoField = "diffuseColor"

IS136.connect.append(connect138)

Script131.IS = IS136

Script131.sourceCode = '''ecmascript:\n"+
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

ProtoBody122.children.append(Script131)

ProtoDeclare113.ProtoBody = ProtoBody122

Scene32.children.append(ProtoDeclare113)
#Test success: declarative statement createDeclarativeShapeTests()
Group139 = x3d.Group()
Group139.DEF = "DeclarativeGroupExample"
Shape140 = x3d.Shape()
MetadataString141 = x3d.MetadataString()
MetadataString141.name = "findThisNameValue"
MetadataString141.DEF = "FindableMetadataStringTest"
MetadataString141.value = ["test case"]

Shape140.value = MetadataString141
Appearance142 = x3d.Appearance()
Appearance142.DEF = "DeclarativeAppearanceExample"
#DeclarativeMaterialExample gets overridden by subsequently added MaterialModulator ProtoInstance
ProtoInstance143 = x3d.ProtoInstance()
ProtoInstance143.name = "MaterialModulator"
ProtoInstance143.DEF = "MyMaterialModulator"

Appearance142.material = ProtoInstance143

Shape140.appearance = Appearance142
Cone144 = x3d.Cone()
Cone144.bottom = False
Cone144.bottomRadius = 0.05
Cone144.height = 0.1

Shape140.geometry = Cone144

Group139.children.append(Shape140)
#Test success: declarativeGroup.addChild() singleton pipeline method

Scene32.children.append(Group139)
#Test success: declarative statement addChild()
#Test success: x3dModel.findNodeByDEF(DeclarativeAppearanceExample) = <Appearance DEF='DeclarativeAppearanceExample'/> i.e. <Appearance DEF='DeclarativeAppearanceExample'> <!- - DeclarativeMaterialExample gets overridden by subsequently added MaterialModulator ProtoInstance - -> <ProtoInstance DEF='MyMaterialModulator' name='MaterialModulator' containerField='material'/> </Appearance>
#Test success: x3dModel.findElementByNameValue(findThisNameValue) = <MetadataString DEF='FindableMetadataStringTest' name='findThisNameValue' value='\"test case\"'/>
#Test success: x3dModel.findElementByNameValue(\"ArtDeco01Material\", \"ProtoDeclare\") found
#Test success: x3dModel.findElementByNameValue(\"MaterialModulator\", \"ProtoDeclare\") found
#Test success: x3dModel.findElementByNameValue(\"MaterialModulator\", \"ProtoInstance\") found
Group145 = x3d.Group()
Group145.DEF = "TestFieldObjectsGroup"
#testFieldObjects() results
#SFBool default=false, true=true, false=false, negate()=true
#MFBool default=, initial=true false true, negate()=false true false
#SFFloat default=0.0, initial=1.0, setValue(2)=2.0, setValue(3.0f)=3.0, setValue(4.0)=4.0
#MFFloat default=, initial=1 2 3, append(5)=1 2 3 5, inserts(3,4)(0,0)=0 1 2 3 4 5, append(6)=0 1 2 3 4 5 6, size()=7
#... get1Value[3]=3.0, remove[1]=0 2 3 4 5 6, set1Value(0,10)=10 2 3 4 5 6, multiply(2)=20 4 6 8 10 12, clear=
#SFVec3f default=0 0 0, initial=1 2 3, setValue=4 5 6, multiply(2)=8 10 12, normalize()=0.45584232 0.5698029 0.68376344, regex matches()=true
#regex test SFVec3f().matches(\"1 2 3\")=true, regex test SFVec3f().matches(\"1 2 3 4\")=false, regex test (SFRotation.matches(\"0 0 0 0\")=true, failure detecting illegal (zero axis) rotation value

Scene32.children.append(Group145)
Sound146 = x3d.Sound()
Sound146.location = [0,1.6,0]
#set sound-ellipsoid location height at 1.6m to match typical avatar height
AudioClip147 = x3d.AudioClip()
AudioClip147.description = "chimes"
AudioClip147.url = ["chimes.wav","https://www.web3d.org/x3d/content/examples/ConformanceNist/Sounds/AudioClip/chimes.wav"]
#Scene example fragment from https://www.web3d.org/x3d/content/examples/ConformanceNist/Sounds/AudioClip/default.x3d

Sound146.source = AudioClip147

Scene32.children.append(Sound146)
Sound148 = x3d.Sound()
Sound148.location = [0,1.6,0]
#set sound-ellipsoid location height at 1.6m to match typical avatar height
MovieTexture149 = x3d.MovieTexture()
MovieTexture149.description = "mpgsys.mpg from ConformanceNist suite"
MovieTexture149.url = ["mpgsys.mpg","https://www.web3d.org/x3d/content/examples/ConformanceNist/Appearance/MovieTexture/mpgsys.mpg"]
#Scene example fragment from https://www.web3d.org/x3d/content/examples/ConformanceNist/Appearance/MovieTexture/mpeg1-systems.x3d
#Expected containerField='source', allowed containerField values=\"texture\" \"source\" \"back\" \"bottom\" \"front\" \"left\" \"right\" \"top\" \"backTexture\" \"bottomTexture\" \"frontTexture\" \"leftTexture\" \"rightTexture\" \"topTexture\" \"children\"

Sound148.source = MovieTexture149

Scene32.children.append(Sound148)
#Test success: Anchor.isNode()=true, siteAnchor.isNode()=true
#Test success: Anchor.isStatement()=false, siteAnchor.isStatement()=false
#Test success: ROUTE.isNode()=false, orbitPositionROUTE.isNode()=false
#Test success: ROUTE.isStatement()=true, orbitPositionROUTE.isStatement()=true
#Test success: CommentsBlock.isNode()=false, testComments.isNode()=false
#Test failure: CommentsBlock.isStatement()=true, testComments.isStatement()=true
Shape150 = x3d.Shape()
Shape150.DEF = "ExtrusionShape"
#ExampleExtrusion isCrossSectionClosed()=true, crossSection='[1.0, 1.0, 1.0, -1.0, -1.0, -1.0, -1.0, 1.0, 1.0, 1.0]'
#ExampleExtrusion isSpineClosed()=false, spine='[0.0, 0.0, 0.0, 0.0, 1.0, 0.0]'
Appearance151 = x3d.Appearance()
Appearance151.DEF = "TransparentAppearance"
Material152 = x3d.Material()
Material152.transparency = 1

Appearance151.material = Material152

Shape150.appearance = Appearance151
Extrusion153 = x3d.Extrusion()
Extrusion153.DEF = "ExampleExtrusion"

Shape150.geometry = Extrusion153

Scene32.children.append(Shape150)
Group154 = x3d.Group()
#Test MFNode children array as an ordered list consisting of comments, statements, ProtoInstance and nodes
ProtoDeclare155 = x3d.ProtoDeclare()
ProtoDeclare155.name = "NewWorldInfo"
ProtoInterface156 = x3d.ProtoInterface()
field157 = x3d.field()
field157.name = "description"
field157.accessType = "initializeOnly"
field157.type = "SFString"

ProtoInterface156.field.append(field157)

ProtoDeclare155.ProtoInterface = ProtoInterface156
ProtoBody158 = x3d.ProtoBody()
WorldInfo159 = x3d.WorldInfo()

ProtoBody158.children.append(WorldInfo159)

ProtoDeclare155.ProtoBody = ProtoBody158

Group154.children.append(ProtoDeclare155)
ProtoInstance160 = x3d.ProtoInstance()
ProtoInstance160.name = "NewWorldInfo"
ProtoInstance160.DEF = "Proto1"
fieldValue161 = x3d.fieldValue()
fieldValue161.name = "description"
fieldValue161.value = "testing 1 2 3"

ProtoInstance160.fieldValue.append(fieldValue161)

Group154.children.append(ProtoInstance160)
Group162 = x3d.Group()
Group162.DEF = "Node2"
#intentionally empty

Group154.children.append(Group162)
ProtoInstance163 = x3d.ProtoInstance()
ProtoInstance163.name = "NewWorldInfo"
ProtoInstance163.DEF = "Proto3"

Group154.children.append(ProtoInstance163)
Transform164 = x3d.Transform()
Transform164.DEF = "Node4"
#intentionally empty

Group154.children.append(Transform164)
#Test satisfactorily creates MFNode children array as an ordered list with mixed content

Scene32.children.append(Group154)
ProtoDeclare165 = x3d.ProtoDeclare()
ProtoDeclare165.name = "ShaderProto"
ProtoBody166 = x3d.ProtoBody()
ProgramShader167 = x3d.ProgramShader()

ProtoBody166.children.append(ProgramShader167)

ProtoDeclare165.ProtoBody = ProtoBody166

Scene32.children.append(ProtoDeclare165)
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

Scene32.children.append(Shape168)
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

Scene32.children.append(Transform175)
EspduTransform186 = x3d.EspduTransform()
WorldInfo187 = x3d.WorldInfo()

EspduTransform186.children.append(WorldInfo187)

Scene32.children.append(EspduTransform186)
ReceiverPdu188 = x3d.ReceiverPdu()

Scene32.children.append(ReceiverPdu188)
SignalPdu189 = x3d.SignalPdu()

Scene32.children.append(SignalPdu189)
TransmitterPdu190 = x3d.TransmitterPdu()

Scene32.children.append(TransmitterPdu190)
DISEntityManager191 = x3d.DISEntityManager()
DISEntityTypeMapping192 = x3d.DISEntityTypeMapping()

DISEntityManager191.children.append(DISEntityTypeMapping192)

Scene32.children.append(DISEntityManager191)
LoadSensor193 = x3d.LoadSensor()
#Contained nodes typically must be USE references for nodes previously DEFined in the scene
#The following nodes are test cases for all X3DUrlObject nodes
Anchor194 = x3d.Anchor()
Anchor194.USE = "siteAnchor"

LoadSensor193.children.append(Anchor194)
Inline195 = x3d.Inline()
Inline195.USE = "inlineScene"

LoadSensor193.children.append(Inline195)
DISEntityTypeMapping196 = x3d.DISEntityTypeMapping()

LoadSensor193.children.append(DISEntityTypeMapping196)
GeoMetadata197 = x3d.GeoMetadata()

LoadSensor193.children.append(GeoMetadata197)
AudioClip198 = x3d.AudioClip()

LoadSensor193.children.append(AudioClip198)
ImageCubeMapTexture199 = x3d.ImageCubeMapTexture()

LoadSensor193.children.append(ImageCubeMapTexture199)
ImageTexture3D200 = x3d.ImageTexture3D()

LoadSensor193.children.append(ImageTexture3D200)
ImageTexture201 = x3d.ImageTexture()

LoadSensor193.children.append(ImageTexture201)
MovieTexture202 = x3d.MovieTexture()

LoadSensor193.children.append(MovieTexture202)
Script203 = x3d.Script()

LoadSensor193.children.append(Script203)
PackagedShader204 = x3d.PackagedShader()

LoadSensor193.children.append(PackagedShader204)
ShaderPart205 = x3d.ShaderPart()
ShaderPart205.type = "VERTEX"

LoadSensor193.children.append(ShaderPart205)
ShaderProgram206 = x3d.ShaderProgram()
ShaderProgram206.type = "VERTEX"

LoadSensor193.children.append(ShaderProgram206)

Scene32.children.append(LoadSensor193)

X3D0.Scene = Scene32
f = open("././HelloWorldProgramOutput_RoundTrip.x3d", "w")
f.write(X3D0.XML())
f.close()
