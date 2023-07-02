print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"
#x3dVersionComparisonTest for this model: supportsX3dVersion(X3DObject.VERSION_3_0)=true
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
component4.name = "Layering"
component4.level = 1

head1.children.append(component4)
unit5 = x3d.unit()
unit5.name = "AngleUnitConversion"
unit5.category = "angle"
unit5.conversionFactor = 1

head1.children.append(unit5)
unit6 = x3d.unit()
unit6.name = "LengthUnitConversion"
unit6.category = "length"
unit6.conversionFactor = 1

head1.children.append(unit6)
meta7 = x3d.meta()
meta7.name = "title"
meta7.content = "HelloWorldProgramOutputCanonical.x3d"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.name = "description"
meta8.content = "Example HelloWorldProgram creates an X3D model using the X3D Java Scene Access Interface Library (X3DJSAIL)"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "reference"
meta9.content = "http://www.web3d.org/specifications/java/X3DJSAIL.html"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "generator"
meta10.content = "HelloWorldProgramOutput.java"

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.name = "created"
meta11.content = "6 September 2016"

head1.children.append(meta11)
meta12 = x3d.meta()
meta12.name = "modified"
meta12.content = "27 December 2018"

head1.children.append(meta12)
meta13 = x3d.meta()
meta13.name = "generator"
meta13.content = "X3D Java Scene Access Interface Library (X3DJSAIL)"

head1.children.append(meta13)
meta14 = x3d.meta()
meta14.name = "generator"
meta14.content = "http://www.web3d.org/specifications/java/examples/HelloWorldProgram.java"

head1.children.append(meta14)
meta15 = x3d.meta()
meta15.name = "generator"
meta15.content = "Netbeans http://www.netbeans.org"

head1.children.append(meta15)
meta16 = x3d.meta()
meta16.name = "creator"
meta16.content = "Don Brutzman"

head1.children.append(meta16)
meta17 = x3d.meta()
meta17.name = "reference"
meta17.content = "https://sourceforge.net/p/x3d/code/HEAD/tree/www.web3d.org/x3d/stylesheets/java/examples/HelloWorldProgramOutput.x3d"

head1.children.append(meta17)
meta18 = x3d.meta()
meta18.name = "reference"
meta18.content = "Console output, ClassicVRML encoding, VRML97 encoding and pretty-print documentation:"

head1.children.append(meta18)
meta19 = x3d.meta()
meta19.name = "reference"
meta19.content = "HelloWorldProgramOutput.txt"

head1.children.append(meta19)
meta20 = x3d.meta()
meta20.name = "reference"
meta20.content = "HelloWorldProgramOutput.x3dv"

head1.children.append(meta20)
meta21 = x3d.meta()
meta21.name = "reference"
meta21.content = "HelloWorldProgramOutput.wrl"

head1.children.append(meta21)
meta22 = x3d.meta()
meta22.name = "reference"
meta22.content = "HelloWorldProgramOutput.html"

head1.children.append(meta22)
meta23 = x3d.meta()
meta23.name = "reference"
meta23.content = "https://savage.nps.edu/X3dValidator?url=http://www.web3d.org/specifications/java/examples/HelloWorldProgramOutput.x3d"

head1.children.append(meta23)
meta24 = x3d.meta()
meta24.name = "identifier"
meta24.content = "http://www.web3d.org/specifications/java/examples/HelloWorldProgramOutput.x3d"

head1.children.append(meta24)
meta25 = x3d.meta()
meta25.name = "license"
meta25.content = "../license.html"

head1.children.append(meta25)

X3D0.head = head1
Scene26 = x3d.Scene()
ViewpointGroup27 = x3d.ViewpointGroup()
ViewpointGroup27.description = "Available viewpoints"
Viewpoint28 = x3d.Viewpoint()
Viewpoint28.DEF = "DefaultView"
Viewpoint28.description = "Hello X3DJSAIL"

ViewpointGroup27.children.append(Viewpoint28)
Viewpoint29 = x3d.Viewpoint()
Viewpoint29.DEF = "TopDownView"
Viewpoint29.description = "top-down view from above"
Viewpoint29.orientation = [1,0,0,-1.570796]
Viewpoint29.position = [0,100,0]

ViewpointGroup27.children.append(Viewpoint29)

Scene26.children.append(ViewpointGroup27)
NavigationInfo30 = x3d.NavigationInfo()
NavigationInfo30.type = ["EXAMINE","FLY","ANY"]

Scene26.children.append(NavigationInfo30)
WorldInfo31 = x3d.WorldInfo()
WorldInfo31.DEF = "WorldInfoDEF"
WorldInfo31.title = "HelloWorldProgram produced by X3D Java SAI Library (X3DJSAIL)"

Scene26.children.append(WorldInfo31)
WorldInfo32 = x3d.WorldInfo()
WorldInfo32.USE = "WorldInfoDEF"

Scene26.children.append(WorldInfo32)
WorldInfo33 = x3d.WorldInfo()
WorldInfo33.USE = "WorldInfoDEF"

Scene26.children.append(WorldInfo33)
MetadataString34 = x3d.MetadataString()
MetadataString34.name = "test"
MetadataString34.DEF = "scene.addChildMetadata"
MetadataString34.value = ["Top-level root Metadata node beneath Scene needs to be one of '-children' in JSON encoding"]

Scene26.metadata = MetadataString34
LayerSet35 = x3d.LayerSet()
LayerSet35.DEF = "scene.addChildLayerSetTest"

Scene26.layerSet = LayerSet35
Transform36 = x3d.Transform()
Transform36.DEF = "LogoGeometryTransform"
Transform36.translation = [0,1.5,0]
Anchor37 = x3d.Anchor()
Anchor37.description = "select for X3D Java SAI Library (X3DJSAIL) description"
Anchor37.url = ["../X3DJSAIL.html","http://www.web3d.org/specifications/java/X3DJSAIL.html"]
Shape38 = x3d.Shape()
Shape38.DEF = "BoxShape"
Appearance39 = x3d.Appearance()
Material40 = x3d.Material()
Material40.DEF = "GreenMaterial"
Material40.diffuseColor = [0,1,1]
Material40.emissiveColor = [0.8,0,0]
Material40.transparency = 0.1

Appearance39.material = Material40
ImageTexture41 = x3d.ImageTexture()
ImageTexture41.url = ["images/X3dJavaSceneAccessInterfaceSaiLibrary.png","http://www.web3d.org/specifications/java/examples/images/X3dJavaSceneAccessInterfaceSaiLibrary.png"]

Appearance39.texture = ImageTexture41

Shape38.appearance = Appearance39
Box42 = x3d.Box()
Box42.DEF = "test-NMTOKEN_regex.0123456789"
Box42.cssClass = "untextured"

Shape38.geometry = Box42

Anchor37.children.append(Shape38)

Transform36.children.append(Anchor37)

Scene26.children.append(Transform36)
Shape43 = x3d.Shape()
Shape43.DEF = "LineShape"
Appearance44 = x3d.Appearance()
Material45 = x3d.Material()
Material45.emissiveColor = [0.6,0.19607843,0.8]

Appearance44.material = Material45

Shape43.appearance = Appearance44
IndexedLineSet46 = x3d.IndexedLineSet()
IndexedLineSet46.coordIndex = [0,1,2,3,4,0]
#Coordinate 3-tuple point count: 6
Coordinate47 = x3d.Coordinate()

IndexedLineSet46.coord = Coordinate47

Shape43.geometry = IndexedLineSet46

Scene26.children.append(Shape43)
PositionInterpolator48 = x3d.PositionInterpolator()
PositionInterpolator48.DEF = "BoxPathAnimator"
PositionInterpolator48.key = [0,0.125,0.375,0.625,0.875,1]

Scene26.children.append(PositionInterpolator48)
TimeSensor49 = x3d.TimeSensor()
TimeSensor49.DEF = "OrbitClock"
TimeSensor49.cycleInterval = 8
TimeSensor49.loop = True

Scene26.children.append(TimeSensor49)
ROUTE50 = x3d.ROUTE()
ROUTE50.fromField = "fraction_changed"
ROUTE50.fromNode = "OrbitClock"
ROUTE50.toField = "set_fraction"
ROUTE50.toNode = "BoxPathAnimator"

Scene26.children.append(ROUTE50)
ROUTE51 = x3d.ROUTE()
ROUTE51.fromField = "value_changed"
ROUTE51.fromNode = "BoxPathAnimator"
ROUTE51.toField = "set_translation"
ROUTE51.toNode = "LogoGeometryTransform"

Scene26.children.append(ROUTE51)
Transform52 = x3d.Transform()
Transform52.DEF = "TextTransform"
Transform52.translation = [0,-1.5,0]
Shape53 = x3d.Shape()
Appearance54 = x3d.Appearance()
Material55 = x3d.Material()
Material55.USE = "GreenMaterial"

Appearance54.material = Material55

Shape53.appearance = Appearance54
Text56 = x3d.Text()
Text56.string = ["X3D Java","SAI Library","X3DJSAIL"]
#Comment example A, plain quotation marks: He said, \"Immel did it!\"
#Comment example B, XML character entities: He said, &quot;Immel did it!&quot;
MetadataSet57 = x3d.MetadataSet()
MetadataSet57.name = "EscapedQuotationMarksMetadataSet"
MetadataString58 = x3d.MetadataString()
MetadataString58.name = "quotesTestC"
MetadataString58.value = ["MFString example C, backslash-escaped quotes: He said, \"Immel did it!\""]

if MetadataSet57.value is None:
    MetadataSet57.value = []
MetadataSet57.value.append(MetadataString58)
MetadataString59 = x3d.MetadataString()
MetadataString59.name = "extraChildTest"
MetadataString59.value = ["checks MetadataSetObject addValue() method"]

if MetadataSet57.value is None:
    MetadataSet57.value = []
MetadataSet57.value.append(MetadataString59)

Text56.metadata = MetadataSet57
FontStyle60 = x3d.FontStyle()
FontStyle60.justify = ["MIDDLE","MIDDLE"]

Text56.fontStyle = FontStyle60

Shape53.geometry = Text56

Transform52.children.append(Shape53)
Collision61 = x3d.Collision()
#test containerField='proxy'
Shape62 = x3d.Shape()
Shape62.DEF = "ProxyShape"
#alternative XML encoding: Text string='\"One, Two, Comment\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\"'
#alternative XML encoding: Text string='\"One, Two, Comment\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\" \"\"'
#alternative Java source: .setString(new String [] {\"One, Two, Comment\", \"\", \"He said, \\\"\"Immel did it!\\\"\"\"})
#reference: http://www.web3d.org/x3d/content/examples/Basic/X3dSpecifications/StringArrayEncodingExamplesIndex.html
Text63 = x3d.Text()
Text63.string = ["One, Two, Text","","He said, \"Immel did it!\" \"\""]

Shape62.geometry = Text63

Collision61.proxy = Shape62

Transform52.children.append(Collision61)
#It's a beautiful world
#... for you!
#https://en.wikipedia.org/wiki/Beautiful_World_(Devo_song)

Scene26.children.append(Transform52)
#repeatedly spin 180 degrees as a readable special effect
OrientationInterpolator64 = x3d.OrientationInterpolator()
OrientationInterpolator64.DEF = "SpinInterpolator"
OrientationInterpolator64.key = [0,0.5,1]

Scene26.children.append(OrientationInterpolator64)
TimeSensor65 = x3d.TimeSensor()
TimeSensor65.DEF = "SpinClock"
TimeSensor65.cycleInterval = 5
TimeSensor65.loop = True

Scene26.children.append(TimeSensor65)
ROUTE66 = x3d.ROUTE()
ROUTE66.fromField = "fraction_changed"
ROUTE66.fromNode = "SpinClock"
ROUTE66.toField = "set_fraction"
ROUTE66.toNode = "SpinInterpolator"

Scene26.children.append(ROUTE66)
ROUTE67 = x3d.ROUTE()
ROUTE67.fromField = "value_changed"
ROUTE67.fromNode = "SpinInterpolator"
ROUTE67.toField = "rotation"
ROUTE67.toNode = "TextTransform"

Scene26.children.append(ROUTE67)
Group68 = x3d.Group()
Group68.DEF = "BackgroundGroup"
Background69 = x3d.Background()
Background69.DEF = "GradualBackground"

Group68.children.append(Background69)
Script70 = x3d.Script()
Script70.DEF = "colorTypeConversionScript"
field71 = x3d.field()
field71.name = "colorInput"
field71.accessType = "inputOnly"
field71.type = "SFColor"

Script70.field.append(field71)
field72 = x3d.field()
field72.name = "colorsOutput"
field72.accessType = "outputOnly"
field72.type = "MFColor"

Script70.field.append(field72)

Script70.sourceCode = '''ecmascript:\n"+
"\n"+
"function colorInput (eventValue) // Example source code\n"+
"{\n"+
"   colorsOutput = new MFColor(eventValue); // assigning value sends output event\n"+
"// Browser.print('colorInput=' + eventValue + ', colorsOutput=' + colorsOutput + '\\n');\n"+
"}'''

Group68.children.append(Script70)
ColorInterpolator73 = x3d.ColorInterpolator()
ColorInterpolator73.DEF = "ColorAnimator"
ColorInterpolator73.key = [0,0.5,1]
#AZURE to INDIGO and back again

Group68.children.append(ColorInterpolator73)
TimeSensor74 = x3d.TimeSensor()
TimeSensor74.DEF = "ColorClock"
TimeSensor74.cycleInterval = 60
TimeSensor74.loop = True

Group68.children.append(TimeSensor74)
ROUTE75 = x3d.ROUTE()
ROUTE75.fromField = "colorsOutput"
ROUTE75.fromNode = "colorTypeConversionScript"
ROUTE75.toField = "skyColor"
ROUTE75.toNode = "GradualBackground"

Group68.children.append(ROUTE75)
ROUTE76 = x3d.ROUTE()
ROUTE76.fromField = "value_changed"
ROUTE76.fromNode = "ColorAnimator"
ROUTE76.toField = "colorInput"
ROUTE76.toNode = "colorTypeConversionScript"

Group68.children.append(ROUTE76)
ROUTE77 = x3d.ROUTE()
ROUTE77.fromField = "fraction_changed"
ROUTE77.fromNode = "ColorClock"
ROUTE77.toField = "set_fraction"
ROUTE77.toNode = "ColorAnimator"

Group68.children.append(ROUTE77)

Scene26.children.append(Group68)
ProtoDeclare78 = x3d.ProtoDeclare()
ProtoDeclare78.name = "ArtDeco01Material"
ProtoDeclare78.appinfo = "tooltip: ArtDeco01Material prototype is a Material node"
ProtoInterface79 = x3d.ProtoInterface()
field80 = x3d.field()
field80.name = "description"
field80.accessType = "inputOutput"
field80.appinfo = "tooltip for descriptionField"
field80.type = "SFString"
field80.value = "ArtDeco01Material prototype is a Material node"

ProtoInterface79.field.append(field80)
field81 = x3d.field()
field81.name = "enabled"
field81.accessType = "inputOutput"
field81.type = "SFBool"
field81.value = True

ProtoInterface79.field.append(field81)

ProtoDeclare78.ProtoInterface = ProtoInterface79
ProtoBody82 = x3d.ProtoBody()
#Initial node of ProtoBody determines prototype node type
Material83 = x3d.Material()
Material83.ambientIntensity = 0.25
Material83.diffuseColor = [0.282435,0.085159,0.134462]
Material83.shininess = 0.127273
Material83.specularColor = [0.276305,0.11431,0.139857]

ProtoBody82.children.append(Material83)
#[HelloWorldProgram diagnostic] should be connected to scene graph: artDeco01ProtoDeclare.getNodeType()=\"Material\"
#presence of follow-on TouchSensor shows that additional nodes are allowed in ProtoBody after initial node, regardless of node types
TouchSensor84 = x3d.TouchSensor()
TouchSensor84.description = "within ProtoBody"
IS85 = x3d.IS()
connect86 = x3d.connect()
connect86.nodeField = "description"
connect86.protoField = "description"

IS85.connect.append(connect86)
connect87 = x3d.connect()
connect87.nodeField = "enabled"
connect87.protoField = "enabled"

IS85.connect.append(connect87)

TouchSensor84.IS = IS85

ProtoBody82.children.append(TouchSensor84)

ProtoDeclare78.ProtoBody = ProtoBody82

Scene26.children.append(ProtoDeclare78)
ExternProtoDeclare88 = x3d.ExternProtoDeclare()
ExternProtoDeclare88.name = "ArtDeco02Material"
ExternProtoDeclare88.appinfo = "this is a different Material node"
ExternProtoDeclare88.url = ["http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3d#ArtDeco02Material","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3dv#ArtDeco02Material"]
#[HelloWorldProgram diagnostic] artDeco02ExternProtoDeclare.getNodeType()=\"ERROR_UNKNOWN_EXTERNPROTODECLARE_NODE_TYPE: ExternProtoDeclare name='ArtDeco02Material' type cannot be remotely accessed at run time. TODO X3DJSAIL needs to add further capability that retrieves the ExternProtoDeclare file.\"
field89 = x3d.field()
field89.name = "description"
field89.accessType = "inputOutput"
field89.appinfo = "tooltip for descriptionField"
field89.type = "SFString"

ExternProtoDeclare88.field.append(field89)

Scene26.children.append(ExternProtoDeclare88)
#Tested ArtDeco01ProtoInstance, ArtDeco02ProtoInstance for improper node type when ProtoInstance is added in wrong place
Shape90 = x3d.Shape()
Shape90.DEF = "TestShape1"
Appearance91 = x3d.Appearance()
Appearance91.DEF = "TestAppearance1"
#ArtDeco01Material prototype goes here... TODO ensure setContainerField is handled in exported Java
ProtoInstance92 = x3d.ProtoInstance()
ProtoInstance92.name = "ArtDeco01Material"
#[HelloWorldProgram diagnostic] ArtDeco01ProtoInstance.getNodeType()=\"Material\"
fieldValue93 = x3d.fieldValue()
fieldValue93.name = "description"
fieldValue93.value = "ArtDeco01Material can substitute for a Material node"

ProtoInstance92.fieldValue.append(fieldValue93)

Appearance91.material = ProtoInstance92

Shape90.appearance = Appearance91
Sphere94 = x3d.Sphere()
Sphere94.radius = 0.001

Shape90.geometry = Sphere94

Scene26.children.append(Shape90)
Shape95 = x3d.Shape()
Shape95.DEF = "TestShape2"
Appearance96 = x3d.Appearance()
Appearance96.DEF = "TestAppearance2"
#ArtDeco02Material prototype goes here... TODO ensure setContainerField is handled in exported Java
ProtoInstance97 = x3d.ProtoInstance()
ProtoInstance97.name = "ArtDeco02Material"
ProtoInstance97.DEF = "ArtDeco02MaterialDEF"
#[HelloWorldProgram diagnostic] ArtDeco02ProtoInstance.getNodeType()=\"ERROR_UNKNOWN_EXTERNPROTODECLARE_NODE_TYPE: ExternProtoDeclare name='ArtDeco02Material' type cannot be remotely accessed at run time. TODO X3DJSAIL needs to add further capability that retrieves the ExternProtoDeclare file.\"
fieldValue98 = x3d.fieldValue()
fieldValue98.name = "description"
fieldValue98.value = "ArtDeco02Material can substitute for another Material node"

ProtoInstance97.fieldValue.append(fieldValue98)

Appearance96.material = ProtoInstance97

Shape95.appearance = Appearance96
Cone99 = x3d.Cone()
Cone99.bottomRadius = 0.001
Cone99.height = 0.001

Shape95.geometry = Cone99

Scene26.children.append(Shape95)
Shape100 = x3d.Shape()
Shape100.DEF = "TestShape3"
Appearance101 = x3d.Appearance()
Appearance101.DEF = "TestAppearance3"
#ArtDeco02Material ProtoInstance USE goes here. Note that name field is NOT defined as part of ProtoInstance USE.
ProtoInstance102 = x3d.ProtoInstance()
ProtoInstance102.USE = "ArtDeco02MaterialDEF"

Appearance101.material = ProtoInstance102

Shape100.appearance = Appearance101
Cylinder103 = x3d.Cylinder()
Cylinder103.height = 0.001
Cylinder103.radius = 0.001

Shape100.geometry = Cylinder103

Scene26.children.append(Shape100)
Inline104 = x3d.Inline()
Inline104.DEF = "inlineSceneDef"
Inline104.url = ["someOtherScene.x3d","http://www.web3d.org/specifications/java/examples/someOtherScene.x3d"]

Scene26.children.append(Inline104)
IMPORT105 = x3d.IMPORT()
IMPORT105.AS = "WorldInfoDEF2"
IMPORT105.importedDEF = "WorldInfoDEF"
IMPORT105.inlineDEF = "inlineSceneDef"

Scene26.children.append(IMPORT105)
EXPORT106 = x3d.EXPORT()
EXPORT106.AS = "WorldInfoDEF3"
EXPORT106.localDEF = "WorldInfoDEF"

Scene26.children.append(EXPORT106)
ProtoDeclare107 = x3d.ProtoDeclare()
ProtoDeclare107.name = "MaterialModulator"
ProtoDeclare107.appinfo = "mimic a Material node and modulate fields as an animation effect"
ProtoDeclare107.documentation = "http://x3dgraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/MaterialModulatorIndex.html"
ProtoInterface108 = x3d.ProtoInterface()
field109 = x3d.field()
field109.name = "enabled"
field109.accessType = "inputOutput"
field109.type = "SFBool"
field109.value = True

ProtoInterface108.field.append(field109)
field110 = x3d.field()
field110.name = "diffuseColor"
field110.accessType = "inputOutput"
field110.type = "SFColor"
field110.value = [0,0,0]

ProtoInterface108.field.append(field110)
field111 = x3d.field()
field111.name = "emissiveColor"
field111.accessType = "inputOutput"
field111.type = "SFColor"
field111.value = [0.05,0.05,0.5]

ProtoInterface108.field.append(field111)
field112 = x3d.field()
field112.name = "specularColor"
field112.accessType = "inputOutput"
field112.type = "SFColor"
field112.value = [0,0,0]

ProtoInterface108.field.append(field112)
field113 = x3d.field()
field113.name = "transparency"
field113.accessType = "inputOutput"
field113.type = "SFFloat"
field113.value = 0

ProtoInterface108.field.append(field113)
field114 = x3d.field()
field114.name = "shininess"
field114.accessType = "inputOutput"
field114.type = "SFFloat"
field114.value = 0

ProtoInterface108.field.append(field114)
field115 = x3d.field()
field115.name = "ambientIntensity"
field115.accessType = "inputOutput"
field115.type = "SFFloat"
field115.value = 0

ProtoInterface108.field.append(field115)

ProtoDeclare107.ProtoInterface = ProtoInterface108
ProtoBody116 = x3d.ProtoBody()
Material117 = x3d.Material()
Material117.DEF = "MaterialNode"
IS118 = x3d.IS()
connect119 = x3d.connect()
connect119.nodeField = "diffuseColor"
connect119.protoField = "diffuseColor"

IS118.connect.append(connect119)
connect120 = x3d.connect()
connect120.nodeField = "emissiveColor"
connect120.protoField = "emissiveColor"

IS118.connect.append(connect120)
connect121 = x3d.connect()
connect121.nodeField = "specularColor"
connect121.protoField = "specularColor"

IS118.connect.append(connect121)
connect122 = x3d.connect()
connect122.nodeField = "transparency"
connect122.protoField = "transparency"

IS118.connect.append(connect122)
connect123 = x3d.connect()
connect123.nodeField = "shininess"
connect123.protoField = "shininess"

IS118.connect.append(connect123)
connect124 = x3d.connect()
connect124.nodeField = "ambientIntensity"
connect124.protoField = "ambientIntensity"

IS118.connect.append(connect124)

Material117.IS = IS118

ProtoBody116.children.append(Material117)
#Only first node (the node type) is renderable, others are along for the ride
Script125 = x3d.Script()
Script125.DEF = "MaterialModulatorScript"
field126 = x3d.field()
field126.name = "enabled"
field126.accessType = "inputOutput"
field126.type = "SFBool"

Script125.field.append(field126)
field127 = x3d.field()
field127.name = "diffuseColor"
field127.accessType = "inputOutput"
field127.type = "SFColor"

Script125.field.append(field127)
field128 = x3d.field()
field128.name = "newColor"
field128.accessType = "outputOnly"
field128.type = "SFColor"

Script125.field.append(field128)
field129 = x3d.field()
field129.name = "clockTrigger"
field129.accessType = "inputOnly"
field129.type = "SFTime"

Script125.field.append(field129)
IS130 = x3d.IS()
connect131 = x3d.connect()
connect131.nodeField = "enabled"
connect131.protoField = "enabled"

IS130.connect.append(connect131)
connect132 = x3d.connect()
connect132.nodeField = "diffuseColor"
connect132.protoField = "diffuseColor"

IS130.connect.append(connect132)

Script125.IS = IS130

Script125.sourceCode = '''ecmascript:\n"+
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

ProtoBody116.children.append(Script125)

ProtoDeclare107.ProtoBody = ProtoBody116

Scene26.children.append(ProtoDeclare107)
#Test success: declarative statement createDeclarativeShapeTests()
Group133 = x3d.Group()
Group133.DEF = "DeclarativeGroupExample"
Shape134 = x3d.Shape()
MetadataString135 = x3d.MetadataString()
MetadataString135.name = "findThisNameValue"
MetadataString135.DEF = "FindableMetadataStringTest"
MetadataString135.value = ["test case"]

Shape134.metadata = MetadataString135
Appearance136 = x3d.Appearance()
Appearance136.DEF = "DeclarativeAppearanceExample"
#DeclarativeMaterialExample gets overridden by subsequently added MaterialModulator ProtoInstance
ProtoInstance137 = x3d.ProtoInstance()
ProtoInstance137.name = "MaterialModulator"
ProtoInstance137.DEF = "MyMaterialModulator"

Appearance136.material = ProtoInstance137

Shape134.appearance = Appearance136
Cone138 = x3d.Cone()
Cone138.bottom = False
Cone138.bottomRadius = 0.05
Cone138.height = 0.1

Shape134.geometry = Cone138

Group133.children.append(Shape134)
#Test success: declarativeGroup.addChild() singleton pipeline method

Scene26.children.append(Group133)
#Test success: declarative statement addChild()
#Test success: x3dModel.findNodeByDEF(DeclarativeAppearanceExample) = <Appearance DEF='DeclarativeAppearanceExample'/> i.e. <Appearance DEF='DeclarativeAppearanceExample'> <!- - DeclarativeMaterialExample gets overridden by subsequently added MaterialModulator ProtoInstance - -> <ProtoInstance DEF='MyMaterialModulator' name='MaterialModulator' containerField='material'/> </Appearance>
#Test success: x3dModel.findElementByNameValue(findThisNameValue) = <MetadataString DEF='FindableMetadataStringTest' name='findThisNameValue' value='\"test case\"'/>
#Test success: x3dModel.findElementByNameValue(\"ArtDeco01Material\", \"ProtoDeclare\") found
#Test success: x3dModel.findElementByNameValue(\"MaterialModulator\", \"ProtoDeclare\") found
#Test success: x3dModel.findElementByNameValue(\"MaterialModulator\", \"ProtoInstance\") found
Group139 = x3d.Group()
Group139.DEF = "TestFieldObjectsGroup"
#testFieldObjects() results
#SFBool default=true, true=true, false=false, negate()=true
#MFBool default=, initial=true false true, negate()=false true false
#SFFloat default=0.0, initial=1.0, setValue(2)=2.0, setValue(3.0f)=3.0, setValue(4.0)=4.0
#MFFloat default=, initial=1 2 3, append(5)=1 2 3 5, inserts(3,4)(0,0)=0 1 2 3 4 5, append(6)=0 1 2 3 4 5 6, size()=7
#... get1Value[3]=3.0, remove[1]=0 2 3 4 5 6, set1Value(0,10)=10 2 3 4 5 6, multiply(2)=20 4 6 8 10 12, clear=
#SFVec3f default=0 0 0, initial=1 2 3, setValue=4 5 6, multiply(2)=8 10 12, normalize()=0.45584232 0.5698029 0.68376344, regex matches()=true
#regex test SFVec3f().matches(\"1 2 3\")=true, regex test SFVec3f().matches(\"1 2 3 4\")=false, regex test (SFRotationObject.matches(\"0 0 0 0\")=true, failure detecting illegal (zero axis) rotation value

Scene26.children.append(Group139)
Sound140 = x3d.Sound()
Sound140.location = [0,1.6,0]
#set sound-ellipsoid location height at 1.6m to match typical avatar height
AudioClip141 = x3d.AudioClip()
AudioClip141.description = "chimes"
AudioClip141.url = ["chimes.wav","http://www.web3d.org/x3d/content/examples/ConformanceNist/Sounds/AudioClip/chimes.wav"]
#Scene example fragment from http://www.web3d.org/x3d/content/examples/ConformanceNist/Sounds/AudioClip/default.x3d

Sound140.source = AudioClip141

Scene26.children.append(Sound140)
Sound142 = x3d.Sound()
Sound142.location = [0,1.6,0]
#set sound-ellipsoid location height at 1.6m to match typical avatar height
MovieTexture143 = x3d.MovieTexture()
MovieTexture143.description = "mpgsys.mpg from ConformanceNist suite"
MovieTexture143.url = ["mpgsys.mpg","http://www.web3d.org/x3d/content/examples/ConformanceNist/Appearance/MovieTexture/mpgsys.mpg"]
#Scene example fragment from http://www.web3d.org/x3d/content/examples/ConformanceNist/Appearance/MovieTexture/mpeg1-systems.x3d
#Expected containerField='source', allowed containerField values=\"texture\" \"source\" \"back\" \"bottom\" \"front\" \"left\" \"right\" \"top\" \"backTexture\" \"bottomTexture\" \"frontTexture\" \"leftTexture\" \"rightTexture\" \"topTexture\" \"watchList\"

Sound142.source = MovieTexture143

Scene26.children.append(Sound142)
#Test success: AnchorObject.isNode()=true, siteAnchor.isNode()=true
#Test success: AnchorObject.isStatement()=false, siteAnchor.isStatement()=false
#Test success: ROUTEObject.isNode()=false, orbitPositionROUTE.isNode()=false
#Test success: ROUTEObject.isStatement()=true, orbitPositionROUTE.isStatement()=true
#Test success: CommentsBlock.isNode()=false, testComments.isNode()=false
#Test failure: CommentsBlock.isStatement()=true, testComments.isStatement()=true
Shape144 = x3d.Shape()
Shape144.DEF = "ExtrusionShape"
#ExampleExtrusion isCrossSectionClosed()=true, crossSection='[1.0, 1.0, 1.0, -1.0, -1.0, -1.0, -1.0, 1.0, 1.0, 1.0]'
#ExampleExtrusion isSpineClosed()=false, spine='[0.0, 0.0, 0.0, 0.0, 1.0, 0.0]'
Appearance145 = x3d.Appearance()
Appearance145.DEF = "TransparentAppearance"
Material146 = x3d.Material()
Material146.transparency = 1

Appearance145.material = Material146

Shape144.appearance = Appearance145
Extrusion147 = x3d.Extrusion()
Extrusion147.DEF = "ExampleExtrusion"

Shape144.geometry = Extrusion147

Scene26.children.append(Shape144)
Group148 = x3d.Group()
#Test MFNode children array as an ordered list consisting of comments, statements, ProtoInstance and nodes
ProtoDeclare149 = x3d.ProtoDeclare()
ProtoDeclare149.name = "NewWorldInfo"
ProtoInterface150 = x3d.ProtoInterface()
field151 = x3d.field()
field151.name = "description"
field151.accessType = "initializeOnly"
field151.type = "SFString"

ProtoInterface150.field.append(field151)

ProtoDeclare149.ProtoInterface = ProtoInterface150
ProtoBody152 = x3d.ProtoBody()
WorldInfo153 = x3d.WorldInfo()

ProtoBody152.children.append(WorldInfo153)

ProtoDeclare149.ProtoBody = ProtoBody152

Group148.children.append(ProtoDeclare149)
ProtoInstance154 = x3d.ProtoInstance()
ProtoInstance154.name = "NewWorldInfo"
ProtoInstance154.DEF = "Proto1"
fieldValue155 = x3d.fieldValue()
fieldValue155.name = "description"
fieldValue155.value = "testing 1 2 3"

ProtoInstance154.fieldValue.append(fieldValue155)

Group148.children.append(ProtoInstance154)
Group156 = x3d.Group()
Group156.DEF = "Node2"
#intentionally empty

Group148.children.append(Group156)
ProtoInstance157 = x3d.ProtoInstance()
ProtoInstance157.name = "NewWorldInfo"
ProtoInstance157.DEF = "Proto3"

Group148.children.append(ProtoInstance157)
Transform158 = x3d.Transform()
Transform158.DEF = "Node4"
#intentionally empty

Group148.children.append(Transform158)
#Test satisfactorily creates MFNode children array as an ordered list with mixed content

Scene26.children.append(Group148)
ProtoDeclare159 = x3d.ProtoDeclare()
ProtoDeclare159.name = "ShaderProto"
ProtoBody160 = x3d.ProtoBody()
ProgramShader161 = x3d.ProgramShader()

ProtoBody160.children.append(ProgramShader161)

ProtoDeclare159.ProtoBody = ProtoBody160

Scene26.children.append(ProtoDeclare159)
Shape162 = x3d.Shape()
Appearance163 = x3d.Appearance()
#Test MFNode shaders array as an ordered list consisting of comments, ProtoInstance and nodes
#Test satisfactorily creates MFNode shaders array as an ordered list with mixed content
ProgramShader164 = x3d.ProgramShader()
ProgramShader164.DEF = "TestShader1"
ShaderProgram165 = x3d.ShaderProgram()
ShaderProgram165.DEF = "TestShader2"
ShaderProgram165.type = "VERTEX"

ProgramShader164.programs.append(ShaderProgram165)

Appearance163.shaders.append(ProgramShader164)
ProtoInstance166 = x3d.ProtoInstance()
ProtoInstance166.name = "ShaderProto"
ProtoInstance166.DEF = "TestShader3"

Appearance163.shaders.append(ProtoInstance166)
ComposedShader167 = x3d.ComposedShader()
ComposedShader167.DEF = "TestShader4"
ShaderPart168 = x3d.ShaderPart()
ShaderPart168.DEF = "TestShader5"
ShaderPart168.type = "VERTEX"

ComposedShader167.parts.append(ShaderPart168)

Appearance163.shaders.append(ComposedShader167)

Shape162.appearance = Appearance163

Scene26.children.append(Shape162)

X3D0.Scene = Scene26
f = open("././HelloWorldProgramOutputCanonical_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
