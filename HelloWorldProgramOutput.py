# -*- coding: UTF-8 -*-
import jnius_config
jnius_config.set_classpath('.', 'X3DJSAIL.3.3.full.jar')
from jnius import autoclass
from X3Dautoclass import *
X3D0 =  X3DObject()
X3D0.setProfile("Immersive")
X3D0.setVersion("3.3")

head1 = headObject()


head1.addComments(CommentsBlock("""comment #1"""))

head1.addComments(CommentsBlock("""comment #2"""))

head1.addComments(CommentsBlock("""comment #3"""))

head1.addComments(CommentsBlock("""comment #4"""))
component2 = componentObject()
component2.setName("Navigation")
component2.setLevel(3)

head1.addComponent(component2)
component3 = componentObject()
component3.setName("Layering")
component3.setLevel(1)

head1.addComponent(component3)
unit4 = unitObject()
unit4.setName("AngleUnitConversion")
unit4.setCategory("angle")
unit4.setConversionFactor(1)

head1.addUnit(unit4)
unit5 = unitObject()
unit5.setName("LengthUnitConversion")
unit5.setCategory("length")
unit5.setConversionFactor(1)

head1.addUnit(unit5)
meta6 = metaObject()
meta6.setName("title")
meta6.setContent("HelloWorldProgramOutput.x3d")

head1.addMeta(meta6)
meta7 = metaObject()
meta7.setName("description")
meta7.setContent("Example HelloWorldProgram creates an X3D model using the X3D Java Scene Access Interface (SAI) Library")

head1.addMeta(meta7)
meta8 = metaObject()
meta8.setName("reference")
meta8.setContent("http://www.web3d.org/specifications/java/X3DJSAIL.html")

head1.addMeta(meta8)
meta9 = metaObject()
meta9.setName("generator")
meta9.setContent("HelloWorldProgramOutput.java")

head1.addMeta(meta9)
meta10 = metaObject()
meta10.setName("created")
meta10.setContent("6 September 2016")

head1.addMeta(meta10)
meta11 = metaObject()
meta11.setName("modified")
meta11.setContent("10 September 2018")

head1.addMeta(meta11)
meta12 = metaObject()
meta12.setName("generator")
meta12.setContent("X3D Java Scene Access Interface Library (X3DJSAIL)")

head1.addMeta(meta12)
meta13 = metaObject()
meta13.setName("generator")
meta13.setContent("http://www.web3d.org/specifications/java/examples/HelloWorldProgram.java")

head1.addMeta(meta13)
meta14 = metaObject()
meta14.setName("generator")
meta14.setContent("Netbeans http://www.netbeans.org")

head1.addMeta(meta14)
meta15 = metaObject()
meta15.setName("creator")
meta15.setContent("Don Brutzman")

head1.addMeta(meta15)
meta16 = metaObject()
meta16.setName("reference")
meta16.setContent("https://sourceforge.net/p/x3d/code/HEAD/tree/www.web3d.org/x3d/stylesheets/java/examples/HelloWorldProgramOutput.x3d")

head1.addMeta(meta16)
meta17 = metaObject()
meta17.setName("reference")
meta17.setContent("Console output, ClassicVRML encoding, VRML97 encoding and pretty-print documentation:")

head1.addMeta(meta17)
meta18 = metaObject()
meta18.setName("reference")
meta18.setContent("HelloWorldProgramOutput.txt")

head1.addMeta(meta18)
meta19 = metaObject()
meta19.setName("reference")
meta19.setContent("HelloWorldProgramOutput.x3dv")

head1.addMeta(meta19)
meta20 = metaObject()
meta20.setName("reference")
meta20.setContent("HelloWorldProgramOutput.wrl")

head1.addMeta(meta20)
meta21 = metaObject()
meta21.setName("reference")
meta21.setContent("HelloWorldProgramOutput.html")

head1.addMeta(meta21)
meta22 = metaObject()
meta22.setName("X3dValidator")
meta22.setContent("https://savage.nps.edu/X3dValidator?url=http://www.web3d.org/specifications/java/examples/HelloWorldProgramOutput.x3d")

head1.addMeta(meta22)
meta23 = metaObject()
meta23.setName("identifier")
meta23.setContent("http://www.web3d.org/specifications/java/examples/HelloWorldProgramOutput.x3d")

head1.addMeta(meta23)
meta24 = metaObject()
meta24.setName("license")
meta24.setContent("../license.html")

head1.addMeta(meta24)
meta25 = metaObject()
meta25.setName("SpecialTest")
meta25.setContent("tested sat: name value cannot contain embedded space character")

head1.addMeta(meta25)
X3D0.setHead(head1)
Scene26 = SceneObject()

ViewpointGroup27 = ViewpointGroupObject()
ViewpointGroup27.setDescription("Available viewpoints")

Viewpoint28 = ViewpointObject()
Viewpoint28.setDEF("DefaultView")
Viewpoint28.setDescription("Hello X3DJSAIL")

ViewpointGroup27.addChild(Viewpoint28)
Viewpoint29 = ViewpointObject()
Viewpoint29.setDEF("TopDownView")
Viewpoint29.setDescription("top-down view from above")
Viewpoint29.setOrientation([1,0,0,-1.570796])
Viewpoint29.setPosition([0,100,0])

ViewpointGroup27.addChild(Viewpoint29)
Scene26.addChild(ViewpointGroup27)
WorldInfo30 = WorldInfoObject()
WorldInfo30.setDEF("WorldInfoDEF")
WorldInfo30.setTitle("HelloWorldProgram produced by X3D Java SAI Library (X3DJSAIL)")

Scene26.addChild(WorldInfo30)
WorldInfo31 = WorldInfoObject()
WorldInfo31.setUSE("WorldInfoDEF")

Scene26.addChild(WorldInfo31)
WorldInfo32 = WorldInfoObject()
WorldInfo32.setUSE("WorldInfoDEF")

Scene26.addChild(WorldInfo32)
MetadataString33 = MetadataStringObject()
MetadataString33.setName("test")
MetadataString33.setDEF("scene.addChildMetadata")
MetadataString33.setValue(["Top-level root Metadata node beneath Scene needs to be one of '-children' in JSON encoding"])

Scene26.addChild(MetadataString33)
LayerSet34 = LayerSetObject()
LayerSet34.setDEF("scene.addChildLayerSetTest")

Scene26.addLayerSet(LayerSet34)
Transform35 = TransformObject()
Transform35.setDEF("LogoGeometryTransform")
Transform35.setTranslation([0,1.5,0])

Anchor36 = AnchorObject()
Anchor36.setDescription("select for X3D Java SAI Library (X3DJSAIL) description")
Anchor36.setUrl(["../X3DJSAIL.html","http://www.web3d.org/specifications/java/X3DJSAIL.html"])

Shape37 = ShapeObject()
Shape37.setDEF("BoxShape")

Appearance38 = AppearanceObject()

Material39 = MaterialObject()
Material39.setDEF("GreenMaterial")
Material39.setDiffuseColor([0,1,1])
Material39.setEmissiveColor([0.8,0,0])
Material39.setTransparency(0.1)

Appearance38.setMaterial(Material39)
ImageTexture40 = ImageTextureObject()
ImageTexture40.setUrl(["images/X3dJavaSceneAccessInterfaceSaiLibrary.png","http://www.web3d.org/specifications/java/examples/images/X3dJavaSceneAccessInterfaceSaiLibrary.png"])

Appearance38.setTexture(ImageTexture40)
Shape37.setAppearance(Appearance38)
Box41 = BoxObject()
Box41.setDEF("test-NMTOKEN_regex.0123456789")
Box41.setCssClass("untextured")

Shape37.setGeometry(Box41)
Anchor36.addChild(Shape37)
Transform35.addChild(Anchor36)
Scene26.addChild(Transform35)
Shape42 = ShapeObject()
Shape42.setDEF("LineShape")

Appearance43 = AppearanceObject()

Material44 = MaterialObject()
Material44.setEmissiveColor([0.6,0.19607843,0.8])

Appearance43.setMaterial(Material44)
Shape42.setAppearance(Appearance43)
IndexedLineSet45 = IndexedLineSetObject()
IndexedLineSet45.setCoordIndex([0,1,2,3,4,0])


IndexedLineSet45.addComments(CommentsBlock("""Coordinate 3-tuple point count: 6"""))
Coordinate46 = CoordinateObject()
Coordinate46.setPoint([0,1.5,0,2,1.5,0,2,1.5,-2,-2,1.5,-2,-2,1.5,0,0,1.5,0])

IndexedLineSet45.setCoord(Coordinate46)
Shape42.setGeometry(IndexedLineSet45)
Scene26.addChild(Shape42)
PositionInterpolator47 = PositionInterpolatorObject()
PositionInterpolator47.setDEF("BoxPathAnimator")
PositionInterpolator47.setKey([0,0.125,0.375,0.625,0.875,1])
PositionInterpolator47.setKeyValue([0,1.5,0,2,1.5,0,2,1.5,-2,-2,1.5,-2,-2,1.5,0,0,1.5,0])

Scene26.addChild(PositionInterpolator47)
TimeSensor48 = TimeSensorObject()
TimeSensor48.setDEF("OrbitClock")
TimeSensor48.setCycleInterval(8)
TimeSensor48.setLoop(True)

Scene26.addChild(TimeSensor48)
ROUTE49 = ROUTEObject()
ROUTE49.setFromField("fraction_changed")
ROUTE49.setFromNode("OrbitClock")
ROUTE49.setToField("set_fraction")
ROUTE49.setToNode("BoxPathAnimator")

Scene26.addChild(ROUTE49)
ROUTE50 = ROUTEObject()
ROUTE50.setFromField("value_changed")
ROUTE50.setFromNode("BoxPathAnimator")
ROUTE50.setToField("set_translation")
ROUTE50.setToNode("LogoGeometryTransform")

Scene26.addChild(ROUTE50)
Transform51 = TransformObject()
Transform51.setDEF("TextTransform")
Transform51.setTranslation([0,-1.5,0])

Shape52 = ShapeObject()

Appearance53 = AppearanceObject()

Material54 = MaterialObject()
Material54.setUSE("GreenMaterial")

Appearance53.setMaterial(Material54)
Shape52.setAppearance(Appearance53)
Text55 = TextObject()
Text55.setString(["X3D Java","SAI Library","X3DJSAIL"])


Text55.addComments(CommentsBlock("""Comment example A, plain quotation marks: He said, \"Immel did it!\""""))

Text55.addComments(CommentsBlock("""Comment example B, XML character entities: He said, &quot;Immel did it!&quot;"""))
MetadataSet56 = MetadataSetObject()
MetadataSet56.setName("EscapedQuotationMarksMetadataSet")

MetadataString57 = MetadataStringObject()
MetadataString57.setName("quotesTestC")
MetadataString57.setValue(["MFString example C, backslash-escaped quotes: He said, \"Immel did it!\""])

MetadataSet56.addValue(MetadataString57)
MetadataString58 = MetadataStringObject()
MetadataString58.setName("extraChildTest")
MetadataString58.setValue(["checks MetadataSetObject addValue() method"])

MetadataSet56.addValue(MetadataString58)
Text55.setMetadata(MetadataSet56)
FontStyle59 = FontStyleObject()
FontStyle59.setJustify(["MIDDLE","MIDDLE"])

Text55.setFontStyle(FontStyle59)
Shape52.setGeometry(Text55)
Transform51.addChild(Shape52)
Collision60 = CollisionObject()


Collision60.addComments(CommentsBlock("""test containerField='proxy'"""))
Shape61 = ShapeObject()
Shape61.setDEF("ProxyShape")


Shape61.addComments(CommentsBlock("""alternative XML encoding: Text string='\"One, Two, Comment\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\"'"""))

Shape61.addComments(CommentsBlock("""alternative XML encoding: Text string='\"One, Two, Comment\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\" \"\"'"""))

Shape61.addComments(CommentsBlock("""alternative Java source: .setString(new String [] {\"One, Two, Comment\", \"\", \"He said, \\\"\"Immel did it!\\\"\"\"})"""))

Shape61.addComments(CommentsBlock("""reference: http://www.web3d.org/x3d/content/examples/Basic/X3dSpecifications/StringArrayEncodingExamplesIndex.html"""))
Text62 = TextObject()
Text62.setString(["One, Two, Text","","He said, \"Immel did it!\" \"\""])

Shape61.setGeometry(Text62)
Collision60.setProxy(Shape61)
Transform51.addChild(Collision60)

Transform51.addComments(CommentsBlock("""It's a beautiful world"""))

Transform51.addComments(CommentsBlock("""... for you!"""))

Transform51.addComments(CommentsBlock("""https://en.wikipedia.org/wiki/Beautiful_World_(Devo_song)"""))
Scene26.addChild(Transform51)

Scene26.addComments(CommentsBlock("""repeatedly spin 180 degrees as a readable special effect"""))
OrientationInterpolator63 = OrientationInterpolatorObject()
OrientationInterpolator63.setDEF("SpinInterpolator")
OrientationInterpolator63.setKey([0,0.5,1])
OrientationInterpolator63.setKeyValue([0,1,0,4.712389,0,1,0,0,0,1,0,1.5707964])

Scene26.addChild(OrientationInterpolator63)
TimeSensor64 = TimeSensorObject()
TimeSensor64.setDEF("SpinClock")
TimeSensor64.setCycleInterval(5)
TimeSensor64.setLoop(True)

Scene26.addChild(TimeSensor64)
ROUTE65 = ROUTEObject()
ROUTE65.setFromField("fraction_changed")
ROUTE65.setFromNode("SpinClock")
ROUTE65.setToField("set_fraction")
ROUTE65.setToNode("SpinInterpolator")

Scene26.addChild(ROUTE65)
ROUTE66 = ROUTEObject()
ROUTE66.setFromField("value_changed")
ROUTE66.setFromNode("SpinInterpolator")
ROUTE66.setToField("rotation")
ROUTE66.setToNode("TextTransform")

Scene26.addChild(ROUTE66)
Group67 = GroupObject()
Group67.setDEF("BackgroundGroup")

Background68 = BackgroundObject()
Background68.setDEF("GradualBackground")

Group67.addChild(Background68)
Script69 = ScriptObject()
Script69.setDEF("colorTypeConversionScript")

field70 = fieldObject()
field70.setType(fieldObject.TYPE_SFCOLOR)
field70.setName("colorInput")
field70.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)

Script69.addField(field70)
field71 = fieldObject()
field71.setType(fieldObject.TYPE_MFCOLOR)
field71.setName("colorsOutput")
field71.setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY)

Script69.addField(field71)

Script69.setSourceCode("ecmascript:\n"+
"\n"+
"function colorInput (eventValue) // Example source code\n"+
"{\n"+
"   colorsOutput = new MFColor(eventValue); // assigning value sends output event\n"+
"// Browser.print('colorInput=' + eventValue + ', colorsOutput=' + colorsOutput + '\\n');\n"+
"}")
Group67.addChild(Script69)
ColorInterpolator72 = ColorInterpolatorObject()
ColorInterpolator72.setDEF("ColorAnimator")
ColorInterpolator72.setKey([0,0.5,1])
ColorInterpolator72.setKeyValue([0.9411765,1,1,0.29411766,0,0.50980395,0.9411765,1,1])


ColorInterpolator72.addComments(CommentsBlock("""AZURE to INDIGO and back again"""))
Group67.addChild(ColorInterpolator72)
TimeSensor73 = TimeSensorObject()
TimeSensor73.setDEF("ColorClock")
TimeSensor73.setCycleInterval(60)
TimeSensor73.setLoop(True)

Group67.addChild(TimeSensor73)
ROUTE74 = ROUTEObject()
ROUTE74.setFromField("colorsOutput")
ROUTE74.setFromNode("colorTypeConversionScript")
ROUTE74.setToField("skyColor")
ROUTE74.setToNode("GradualBackground")

Group67.addChild(ROUTE74)
ROUTE75 = ROUTEObject()
ROUTE75.setFromField("value_changed")
ROUTE75.setFromNode("ColorAnimator")
ROUTE75.setToField("colorInput")
ROUTE75.setToNode("colorTypeConversionScript")

Group67.addChild(ROUTE75)
ROUTE76 = ROUTEObject()
ROUTE76.setFromField("fraction_changed")
ROUTE76.setFromNode("ColorClock")
ROUTE76.setToField("set_fraction")
ROUTE76.setToNode("ColorAnimator")

Group67.addChild(ROUTE76)
Scene26.addChild(Group67)
ProtoDeclare77 = ProtoDeclareObject()
ProtoDeclare77.setName("ArtDeco01Material")
ProtoDeclare77.setAppinfo("tooltip: ArtDeco01Material prototype is a Material node")

ProtoInterface78 = ProtoInterfaceObject()

field79 = fieldObject()
field79.setType(fieldObject.TYPE_SFSTRING)
field79.setName("description")
field79.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field79.setAppinfo("tooltip for descriptionField")
field79.setValue("ArtDeco01Material prototype is a Material node")

ProtoInterface78.addField(field79)
field80 = fieldObject()
field80.setType(fieldObject.TYPE_SFBOOL)
field80.setName("enabled")
field80.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field80.setValue("true")

ProtoInterface78.addField(field80)
ProtoDeclare77.setProtoInterface(ProtoInterface78)
ProtoBody81 = ProtoBodyObject()


ProtoBody81.addComments(CommentsBlock("""Initial node of ProtoBody determines prototype node type"""))
Material82 = MaterialObject()
Material82.setAmbientIntensity(0.25)
Material82.setDiffuseColor([0.282435,0.085159,0.134462])
Material82.setShininess(0.127273)
Material82.setSpecularColor([0.276305,0.11431,0.139857])

ProtoBody81.addChild(Material82)

ProtoBody81.addComments(CommentsBlock("""[HelloWorldProgram diagnostic] should be connected to scene graph: ArtDeco01ProtoDeclare.getNodeType()=\"Material\""""))

ProtoBody81.addComments(CommentsBlock("""presence of follow-on TouchSensor shows that additional nodes are allowed in ProtoBody after initial node, regardless of node types"""))
TouchSensor83 = TouchSensorObject()
TouchSensor83.setDescription("within ProtoBody")

IS84 = ISObject()

connect85 = connectObject()
connect85.setNodeField("description")
connect85.setProtoField("description")

IS84.addConnect(connect85)
connect86 = connectObject()
connect86.setNodeField("enabled")
connect86.setProtoField("enabled")

IS84.addConnect(connect86)
TouchSensor83.setIS(IS84)
ProtoBody81.addChild(TouchSensor83)
ProtoDeclare77.setProtoBody(ProtoBody81)
Scene26.addChild(ProtoDeclare77)
ExternProtoDeclare87 = ExternProtoDeclareObject()
ExternProtoDeclare87.setName("ArtDeco02Material")
ExternProtoDeclare87.setAppinfo("this is a different Material node")
ExternProtoDeclare87.setUrl(["http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3d#ArtDeco02Material","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3dv#ArtDeco02Material"])


ExternProtoDeclare87.addComments(CommentsBlock("""[HelloWorldProgram diagnostic] ArtDeco02ExternProtoDeclare.getNodeType()=\"ERROR_UNKNOWN_EXTERNPROTODECLARE_NODE_TYPE: ExternProtoDeclare name='ArtDeco02Material' type cannot be remotely accessed at run time, TODO X3DJSAIL needs to add further capability.\""""))
field88 = fieldObject()
field88.setType(fieldObject.TYPE_SFSTRING)
field88.setName("description")
field88.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field88.setAppinfo("tooltip for descriptionField")

ExternProtoDeclare87.addField(field88)
Scene26.addChild(ExternProtoDeclare87)

Scene26.addComments(CommentsBlock("""Tested ArtDeco01ProtoInstance, ArtDeco02ProtoInstance for improper node type when ProtoInstance is added in wrong place"""))
Shape89 = ShapeObject()
Shape89.setDEF("TestShape1")

Appearance90 = AppearanceObject()
Appearance90.setDEF("TestAppearance1")


Appearance90.addComments(CommentsBlock("""ArtDeco01Material prototype goes here... TODO ensure setContainerField is handled in exported Java"""))
ProtoInstance91 = ProtoInstanceObject()
ProtoInstance91.setName("ArtDeco01Material")


ProtoInstance91.addComments(CommentsBlock("""[HelloWorldProgram diagnostic] ArtDeco01ProtoInstance.getNodeType()=\"Material\""""))
fieldValue92 = fieldValueObject()
fieldValue92.setName("description")
fieldValue92.setValue("ArtDeco01Material can substitute for a Material node")

ProtoInstance91.addFieldValue(fieldValue92)
Appearance90.setMaterial(ProtoInstance91)
Shape89.setAppearance(Appearance90)
Sphere93 = SphereObject()
Sphere93.setRadius(0.001)

Shape89.setGeometry(Sphere93)
Scene26.addChild(Shape89)
Shape94 = ShapeObject()
Shape94.setDEF("TestShape2")

Appearance95 = AppearanceObject()
Appearance95.setDEF("TestAppearance2")


Appearance95.addComments(CommentsBlock("""ArtDeco02Material prototype goes here... TODO ensure setContainerField is handled in exported Java"""))
ProtoInstance96 = ProtoInstanceObject()
ProtoInstance96.setName("ArtDeco02Material")
ProtoInstance96.setDEF("ArtDeco02MaterialDEF")


ProtoInstance96.addComments(CommentsBlock("""[HelloWorldProgram diagnostic] ArtDeco02ProtoInstance.getNodeType()=\"ERROR_UNKNOWN_EXTERNPROTODECLARE_NODE_TYPE: ExternProtoDeclare name='ArtDeco02Material' type cannot be remotely accessed at run time, TODO X3DJSAIL needs to add further capability.\""""))
fieldValue97 = fieldValueObject()
fieldValue97.setName("description")
fieldValue97.setValue("ArtDeco02Material can substitute for another Material node")

ProtoInstance96.addFieldValue(fieldValue97)
Appearance95.setMaterial(ProtoInstance96)
Shape94.setAppearance(Appearance95)
Cone98 = ConeObject()
Cone98.setBottomRadius(0.001)
Cone98.setHeight(0.001)

Shape94.setGeometry(Cone98)
Scene26.addChild(Shape94)
Shape99 = ShapeObject()
Shape99.setDEF("TestShape3")

Appearance100 = AppearanceObject()
Appearance100.setDEF("TestAppearance3")


Appearance100.addComments(CommentsBlock("""ArtDeco02Material ProtoInstance USE goes here..."""))
ProtoInstance101 = ProtoInstanceObject()
ProtoInstance101.setUSE("ArtDeco02MaterialDEF")

Appearance100.setMaterial(ProtoInstance101)
Shape99.setAppearance(Appearance100)
Cylinder102 = CylinderObject()
Cylinder102.setHeight(0.001)
Cylinder102.setRadius(0.001)

Shape99.setGeometry(Cylinder102)
Scene26.addChild(Shape99)
Inline103 = InlineObject()
Inline103.setDEF("inlineSceneDef")
Inline103.setUrl(["someOtherScene.x3d"])

Scene26.addChild(Inline103)
IMPORT104 = IMPORTObject()
IMPORT104.setAS("WorldInfoDEF2")
IMPORT104.setImportedDEF("WorldInfoDEF")
IMPORT104.setInlineDEF("inlineSceneDef")

Scene26.addChild(IMPORT104)
EXPORT105 = EXPORTObject()
EXPORT105.setAS("WorldInfoDEF3")
EXPORT105.setLocalDEF("WorldInfoDEF")

Scene26.addChild(EXPORT105)
ProtoDeclare106 = ProtoDeclareObject()
ProtoDeclare106.setName("MaterialModulator")
ProtoDeclare106.setAppinfo("mimic a Material node and modulate fields as an animation effect")
ProtoDeclare106.setDocumentation("http://x3dgraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/MaterialModulatorIndex.html")

ProtoInterface107 = ProtoInterfaceObject()

field108 = fieldObject()
field108.setType(fieldObject.TYPE_SFBOOL)
field108.setName("enabled")
field108.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field108.setValue("true")

ProtoInterface107.addField(field108)
field109 = fieldObject()
field109.setType(fieldObject.TYPE_SFCOLOR)
field109.setName("diffuseColor")
field109.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field109.setValue("0 0 0")

ProtoInterface107.addField(field109)
field110 = fieldObject()
field110.setType(fieldObject.TYPE_SFCOLOR)
field110.setName("emissiveColor")
field110.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field110.setValue("0.05 0.05 0.5")

ProtoInterface107.addField(field110)
field111 = fieldObject()
field111.setType(fieldObject.TYPE_SFCOLOR)
field111.setName("specularColor")
field111.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field111.setValue("0 0 0")

ProtoInterface107.addField(field111)
field112 = fieldObject()
field112.setType(fieldObject.TYPE_SFFLOAT)
field112.setName("transparency")
field112.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field112.setValue("0")

ProtoInterface107.addField(field112)
field113 = fieldObject()
field113.setType(fieldObject.TYPE_SFFLOAT)
field113.setName("shininess")
field113.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field113.setValue("0")

ProtoInterface107.addField(field113)
field114 = fieldObject()
field114.setType(fieldObject.TYPE_SFFLOAT)
field114.setName("ambientIntensity")
field114.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field114.setValue("0")

ProtoInterface107.addField(field114)
ProtoDeclare106.setProtoInterface(ProtoInterface107)
ProtoBody115 = ProtoBodyObject()

Material116 = MaterialObject()
Material116.setDEF("MaterialNode")

IS117 = ISObject()

connect118 = connectObject()
connect118.setNodeField("diffuseColor")
connect118.setProtoField("diffuseColor")

IS117.addConnect(connect118)
connect119 = connectObject()
connect119.setNodeField("emissiveColor")
connect119.setProtoField("emissiveColor")

IS117.addConnect(connect119)
connect120 = connectObject()
connect120.setNodeField("specularColor")
connect120.setProtoField("specularColor")

IS117.addConnect(connect120)
connect121 = connectObject()
connect121.setNodeField("transparency")
connect121.setProtoField("transparency")

IS117.addConnect(connect121)
connect122 = connectObject()
connect122.setNodeField("shininess")
connect122.setProtoField("shininess")

IS117.addConnect(connect122)
connect123 = connectObject()
connect123.setNodeField("ambientIntensity")
connect123.setProtoField("ambientIntensity")

IS117.addConnect(connect123)
Material116.setIS(IS117)
ProtoBody115.addChild(Material116)

ProtoBody115.addComments(CommentsBlock("""Only first node (the node type) is renderable, others are along for the ride"""))
Script124 = ScriptObject()
Script124.setDEF("MaterialModulatorScript")

field125 = fieldObject()
field125.setType(fieldObject.TYPE_SFBOOL)
field125.setName("enabled")
field125.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)

Script124.addField(field125)
field126 = fieldObject()
field126.setType(fieldObject.TYPE_SFCOLOR)
field126.setName("diffuseColor")
field126.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)

Script124.addField(field126)
field127 = fieldObject()
field127.setType(fieldObject.TYPE_SFCOLOR)
field127.setName("newColor")
field127.setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY)

Script124.addField(field127)
field128 = fieldObject()
field128.setType(fieldObject.TYPE_SFTIME)
field128.setName("clockTrigger")
field128.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)

Script124.addField(field128)
IS129 = ISObject()

connect130 = connectObject()
connect130.setNodeField("enabled")
connect130.setProtoField("enabled")

IS129.addConnect(connect130)
connect131 = connectObject()
connect131.setNodeField("diffuseColor")
connect131.setProtoField("diffuseColor")

IS129.addConnect(connect131)
Script124.setIS(IS129)

Script124.setSourceCode("ecmascript:\n"+
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
"}")
ProtoBody115.addChild(Script124)
ProtoDeclare106.setProtoBody(ProtoBody115)
Scene26.addChild(ProtoDeclare106)

Scene26.addComments(CommentsBlock("""Test success: declarative statement createDeclarativeShapeTests()"""))
Group132 = GroupObject()
Group132.setDEF("DeclarativeGroupExample")

Shape133 = ShapeObject()

MetadataString134 = MetadataStringObject()
MetadataString134.setName("findThisNameValue")
MetadataString134.setDEF("FindableMetadataStringTest")
MetadataString134.setValue(["test case"])

Shape133.setMetadata(MetadataString134)
Appearance135 = AppearanceObject()
Appearance135.setDEF("DeclarativeAppearanceExample")


Appearance135.addComments(CommentsBlock("""DeclarativeMaterialExample gets overridden by subsequently added MaterialModulator ProtoInstance"""))
ProtoInstance136 = ProtoInstanceObject()
ProtoInstance136.setName("MaterialModulator")
ProtoInstance136.setDEF("MyMaterialModulator")

Appearance135.setMaterial(ProtoInstance136)
Shape133.setAppearance(Appearance135)
Cone137 = ConeObject()
Cone137.setBottom(False)
Cone137.setBottomRadius(0.05)
Cone137.setHeight(0.1)

Shape133.setGeometry(Cone137)
Group132.addChild(Shape133)

Group132.addComments(CommentsBlock("""Test success: declarativeGroup.addChild() singleton pipeline method"""))
Scene26.addChild(Group132)

Scene26.addComments(CommentsBlock("""Test success: declarative statement addChild()"""))

Scene26.addComments(CommentsBlock("""Test success: x3dModel.findNodeByDEF(DeclarativeAppearanceExample) = <Appearance DEF='DeclarativeAppearanceExample'/> i.e. <Appearance DEF='DeclarativeAppearanceExample'> <!- - DeclarativeMaterialExample gets overridden by subsequently added MaterialModulator ProtoInstance - -> <ProtoInstance DEF='MyMaterialModulator' name='MaterialModulator' containerField='material'/> </Appearance>"""))

Scene26.addComments(CommentsBlock("""Test success: x3dModel.findElementByNameValue(findThisNameValue) = <MetadataString DEF='FindableMetadataStringTest' name='findThisNameValue' value='\"test case\"'/>"""))

Scene26.addComments(CommentsBlock("""Test success: x3dModel.findElementByNameValue(\"ArtDeco01Material\", \"ProtoDeclare\") found"""))

Scene26.addComments(CommentsBlock("""Test success: x3dModel.findElementByNameValue(\"MaterialModulator\", \"ProtoDeclare\") found"""))

Scene26.addComments(CommentsBlock("""Test success: x3dModel.findElementByNameValue(\"MaterialModulator\", \"ProtoInstance\") found"""))
Group138 = GroupObject()
Group138.setDEF("TestFieldObjectsGroup")


Group138.addComments(CommentsBlock("""testFieldObjects() results"""))

Group138.addComments(CommentsBlock("""SFBool default=true, true=true, false=false, negate()=true"""))

Group138.addComments(CommentsBlock("""MFBool default=, initial=true false true, negate()=false true false"""))

Group138.addComments(CommentsBlock("""SFFloat default=0.0, initial=1.0, setValue(2)=2.0, setValue(3.0f)=3.0, setValue(4.0)=4.0"""))

Group138.addComments(CommentsBlock("""MFFloat default=, initial=1 2 3, append(5)=1 2 3 5, inserts(3,4)(0,0)=0 1 2 3 4 5, append(6)=0 1 2 3 4 5 6, size()=7"""))

Group138.addComments(CommentsBlock("""... get1Value[3]=3.0, remove[1]=0 2 3 4 5 6, set1Value(0,10)=10 2 3 4 5 6, multiply(2)=20 4 6 8 10 12, clear="""))

Group138.addComments(CommentsBlock("""SFVec3f default=0 0 0, initial=1 2 3, setValue=4 5 6, multiply(2)=8 10 12, normalize()=0.45584232 0.5698029 0.68376344, regex matches()=true"""))

Group138.addComments(CommentsBlock("""regex test SFVec3f().matches(\"1 2 3\")=true, regex test SFVec3f().matches(\"1 2 3 4\")=false, regex test (SFRotationObject.matches(\"0 0 0 0\")=true, failure detecting illegal (zero axis) rotation value"""))
Scene26.addChild(Group138)
Sound139 = SoundObject()
Sound139.setLocation([0,1.6,0])


Sound139.addComments(CommentsBlock("""set sound-ellipsoid location height at 1.6m to match typical avatar height"""))
AudioClip140 = AudioClipObject()
AudioClip140.setDescription("chimes")
AudioClip140.setUrl(["chimes.wav","http://www.web3d.org/x3d/content/examples/ConformanceNist/Sounds/AudioClip/chimes.wav"])


AudioClip140.addComments(CommentsBlock("""Scene example fragment from http://www.web3d.org/x3d/content/examples/ConformanceNist/Sounds/AudioClip/default.x3d"""))
Sound139.setSource(AudioClip140)
Scene26.addChild(Sound139)
Sound141 = SoundObject()
Sound141.setLocation([0,1.6,0])


Sound141.addComments(CommentsBlock("""set sound-ellipsoid location height at 1.6m to match typical avatar height"""))
MovieTexture142 = MovieTextureObject()
MovieTexture142.setDescription("mpgsys.mpg from ConformanceNist suite")
MovieTexture142.setUrl(["mpgsys.mpg","http://www.web3d.org/x3d/content/examples/ConformanceNist/Appearance/MovieTexture/mpgsys.mpg"])


MovieTexture142.addComments(CommentsBlock("""Scene example fragment from http://www.web3d.org/x3d/content/examples/ConformanceNist/Appearance/MovieTexture/mpeg1-systems.x3d"""))

MovieTexture142.addComments(CommentsBlock("""Expected containerField='source', allowed containerField values=\"texture\" \"source\" \"back\" \"bottom\" \"front\" \"left\" \"right\" \"top\" \"backTexture\" \"bottomTexture\" \"frontTexture\" \"leftTexture\" \"rightTexture\" \"topTexture\" \"watchList\""""))
Sound141.setSource(MovieTexture142)
Scene26.addChild(Sound141)

Scene26.addComments(CommentsBlock("""Test success: AnchorObject.isNode()=true, siteAnchor.isNode()=true"""))

Scene26.addComments(CommentsBlock("""Test success: AnchorObject.isStatement()=false, siteAnchor.isStatement()=false"""))

Scene26.addComments(CommentsBlock("""Test success: ROUTEObject.isNode()=false, orbitPositionROUTE.isNode()=false"""))

Scene26.addComments(CommentsBlock("""Test success: ROUTEObject.isStatement()=true, orbitPositionROUTE.isStatement()=true"""))

Scene26.addComments(CommentsBlock("""Test success: CommentsBlock.isNode()=false, testComments.isNode()=false"""))

Scene26.addComments(CommentsBlock("""Test failure: CommentsBlock.isStatement()=true, testComments.isStatement()=true"""))
Shape143 = ShapeObject()
Shape143.setDEF("ExtrusionShape")


Shape143.addComments(CommentsBlock("""ExampleExtrusion isCrossSectionClosed()=true, crossSection='[1.0, 1.0, 1.0, -1.0, -1.0, -1.0, -1.0, 1.0, 1.0, 1.0]'"""))

Shape143.addComments(CommentsBlock("""ExampleExtrusion isSpineClosed()=false, spine='[0.0, 0.0, 0.0, 0.0, 1.0, 0.0]'"""))
Appearance144 = AppearanceObject()
Appearance144.setDEF("TransparentAppearance")

Material145 = MaterialObject()
Material145.setTransparency(1)

Appearance144.setMaterial(Material145)
Shape143.setAppearance(Appearance144)
Extrusion146 = ExtrusionObject()
Extrusion146.setDEF("ExampleExtrusion")

Shape143.setGeometry(Extrusion146)
Scene26.addChild(Shape143)
X3D0.setScene(Scene26)

X3D0.toFileX3D("./HelloWorldProgramOutput.new.x3d")
