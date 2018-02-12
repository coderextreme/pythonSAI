# -*- coding: UTF-8 -*-
from jnius import autoclass
from X3Dautoclass import *
X3D0 =  X3DObject()
X3D0.setProfile("Immersive")
X3D0.setVersion("3.3")

head1 = headObject()

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
meta11.setContent("9 December 2017")

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

head1.addComments(CommentsBlock("""comment #1"""))

head1.addComments(CommentsBlock("""comment #2"""))

head1.addComments(CommentsBlock("""comment #3"""))

head1.addComments(CommentsBlock("""comment #4"""))
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
MetadataString33.setDEF("scene.addChildMetadataObject")

Scene26.addChild(MetadataString33)
LayerSet34 = LayerSetObject()
LayerSet34.setDEF("scene.addChildLayerSetObjectTest")

Scene26.addChild(LayerSet34)
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
Box41.setCssClass("textured")

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

MetadataSet56 = MetadataSetObject()
MetadataSet56.setName("EscapedQuotationMarksMetadataSet")

MetadataString57 = MetadataStringObject()
MetadataString57.setName("escapedQuotesTest2")
MetadataString57.setValue(["escaped quotation marks example 2: He said, &quot;Immel did it!&quot;"])

MetadataSet56.setMetadata(MetadataString57)
Text55.setMetadata(MetadataSet56)
FontStyle58 = FontStyleObject()
FontStyle58.setJustify(["MIDDLE","MIDDLE"])

Text55.setFontStyle(FontStyle58)

Text55.addComments(CommentsBlock("""escaped quotation marks example 3: He said, \"Immel did it!\""""))

Text55.addComments(CommentsBlock("""escaped quotation marks example 4: He said, &quot;Immel did it!&quot;"""))
Shape52.setGeometry(Text55)
Transform51.addChild(Shape52)
Collision59 = CollisionObject()


Collision59.addComments(CommentsBlock("""test containerField='proxy'"""))
Shape60 = ShapeObject()
Shape60.setDEF("ProxyShape")

Text61 = TextObject()
Text61.setString(["One, Two, Three","","He said, \"Immel did it!\""])

Shape60.setGeometry(Text61)

Shape60.addComments(CommentsBlock("""alternative XML encoding: Text string='\"One, Two, Three\", \"\", \"He said, \\&quot;Immel did it!\\&quot;\"'"""))

Shape60.addComments(CommentsBlock("""alternative Java source: .setString(new String [] {\"One, Two, Three\", \"\", \"He said, \\\"Immel did it!\\\"\"})"""))

Shape60.addComments(CommentsBlock("""reference: http://www.web3d.org/x3d/content/examples/Basic/X3dSpecifications/StringArrayEncodingExamplesIndex.html"""))
Collision59.addChild(Shape60)
Transform51.addChild(Collision59)

Transform51.addComments(CommentsBlock("""It's a beautiful world"""))

Transform51.addComments(CommentsBlock("""... for you!"""))

Transform51.addComments(CommentsBlock("""https://en.wikipedia.org/wiki/Beautiful_World_(Devo_song)"""))
Scene26.addChild(Transform51)

Scene26.addComments(CommentsBlock("""repeatedly spin 180 degrees as a readable special effect"""))
OrientationInterpolator62 = OrientationInterpolatorObject()
OrientationInterpolator62.setDEF("SpinInterpolator")
OrientationInterpolator62.setKey([0,0.5,1])
OrientationInterpolator62.setKeyValue([0,1,0,4.712389,0,1,0,0,0,1,0,1.5707964])

Scene26.addChild(OrientationInterpolator62)
TimeSensor63 = TimeSensorObject()
TimeSensor63.setDEF("SpinClock")
TimeSensor63.setCycleInterval(5)
TimeSensor63.setLoop(True)

Scene26.addChild(TimeSensor63)
ROUTE64 = ROUTEObject()
ROUTE64.setFromField("fraction_changed")
ROUTE64.setFromNode("SpinClock")
ROUTE64.setToField("set_fraction")
ROUTE64.setToNode("SpinInterpolator")

Scene26.addChild(ROUTE64)
ROUTE65 = ROUTEObject()
ROUTE65.setFromField("value_changed")
ROUTE65.setFromNode("SpinInterpolator")
ROUTE65.setToField("rotation")
ROUTE65.setToNode("TextTransform")

Scene26.addChild(ROUTE65)
Group66 = GroupObject()
Group66.setDEF("BackgroundGroup")

Background67 = BackgroundObject()
Background67.setDEF("GradualBackground")

Group66.addChild(Background67)
Script68 = ScriptObject()
Script68.setDEF("colorTypeConversionScript")

field69 = fieldObject()
field69.setType(fieldObject.TYPE_SFCOLOR)
field69.setName("colorInput")
field69.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)

Script68.addField(field69)
field70 = fieldObject()
field70.setType(fieldObject.TYPE_MFCOLOR)
field70.setName("colorsOutput")
field70.setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY)

Script68.addField(field70)

Script68.setSourceCode("ecmascript: function colorInput (eventValue) // Example source code { colorsOutput = new MFColor(eventValue); // assigning value sends output event // Browser.print('colorInput=' + eventValue + ', colorsOutput=' + colorsOutput + '\\n'); }\n"+
"")
Group66.addChild(Script68)
ColorInterpolator71 = ColorInterpolatorObject()
ColorInterpolator71.setDEF("ColorAnimator")
ColorInterpolator71.setKey([0,0.5,1])
ColorInterpolator71.setKeyValue([0.9411765,1,1,0.29411766,0,0.50980395,0.9411765,1,1])


ColorInterpolator71.addComments(CommentsBlock("""AZURE to INDIGO and back again"""))
Group66.addChild(ColorInterpolator71)
TimeSensor72 = TimeSensorObject()
TimeSensor72.setDEF("ColorClock")
TimeSensor72.setCycleInterval(60)
TimeSensor72.setLoop(True)

Group66.addChild(TimeSensor72)
ROUTE73 = ROUTEObject()
ROUTE73.setFromField("colorsOutput")
ROUTE73.setFromNode("colorTypeConversionScript")
ROUTE73.setToField("skyColor")
ROUTE73.setToNode("GradualBackground")

Group66.addChild(ROUTE73)
ROUTE74 = ROUTEObject()
ROUTE74.setFromField("value_changed")
ROUTE74.setFromNode("ColorAnimator")
ROUTE74.setToField("colorInput")
ROUTE74.setToNode("colorTypeConversionScript")

Group66.addChild(ROUTE74)
ROUTE75 = ROUTEObject()
ROUTE75.setFromField("fraction_changed")
ROUTE75.setFromNode("ColorClock")
ROUTE75.setToField("set_fraction")
ROUTE75.setToNode("ColorAnimator")

Group66.addChild(ROUTE75)
Scene26.addChild(Group66)
ProtoDeclare76 = ProtoDeclareObject()
ProtoDeclare76.setName("ArtDeco01Material")
ProtoDeclare76.setAppinfo("tooltip: ArtDeco01 prototype is a Material node")

ProtoInterface77 = ProtoInterfaceObject()

field78 = fieldObject()
field78.setType(fieldObject.TYPE_SFSTRING)
field78.setName("description")
field78.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field78.setAppinfo("tooltip for descriptionField")
field78.setValue("ArtDeco01 prototype is a Material node")

ProtoInterface77.addField(field78)
field79 = fieldObject()
field79.setType(fieldObject.TYPE_SFBOOL)
field79.setName("enabled")
field79.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field79.setValue("true")

ProtoInterface77.addField(field79)
ProtoDeclare76.setProtoInterface(ProtoInterface77)
ProtoBody80 = ProtoBodyObject()


ProtoBody80.addComments(CommentsBlock("""Initial node of ProtoBody determines prototype node type"""))
Material81 = MaterialObject()
Material81.setAmbientIntensity(0.25)
Material81.setDiffuseColor([0.282435,0.085159,0.134462])
Material81.setShininess(0.127273)
Material81.setSpecularColor([0.276305,0.11431,0.139857])

ProtoBody80.addChild(Material81)

ProtoBody80.addComments(CommentsBlock("""[HelloWorldProgram diagnostic] should be connected to scene graph: ArtDeco01ProtoDeclare.getNodeType()=\"Material\""""))

ProtoBody80.addComments(CommentsBlock("""presence of follow-on TouchSensor shows that additional nodes are allowed in ProtoBody after initial node, regardless of node types"""))
TouchSensor82 = TouchSensorObject()
TouchSensor82.setDescription("within ProtoBody")

IS83 = ISObject()

connect84 = connectObject()
connect84.setNodeField("description")
connect84.setProtoField("description")

IS83.addConnect(connect84)
connect85 = connectObject()
connect85.setNodeField("enabled")
connect85.setProtoField("enabled")

IS83.addConnect(connect85)
TouchSensor82.setIS(IS83)
ProtoBody80.addChild(TouchSensor82)
ProtoDeclare76.setProtoBody(ProtoBody80)
Scene26.addChild(ProtoDeclare76)
ExternProtoDeclare86 = ExternProtoDeclareObject()
ExternProtoDeclare86.setName("ArtDeco02Material")
ExternProtoDeclare86.setAppinfo("this is a different Material node")
ExternProtoDeclare86.setUrl(["http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3d#ArtDeco02","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3dv#ArtDeco02"])

field87 = fieldObject()
field87.setType(fieldObject.TYPE_SFSTRING)
field87.setName("description")
field87.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field87.setAppinfo("tooltip for descriptionField")

ExternProtoDeclare86.addField(field87)

ExternProtoDeclare86.addComments(CommentsBlock("""[HelloWorldProgram diagnostic] ArtDeco02ExternProtoDeclare.getNodeType()=\"ERROR_UNKNOWN_EXTERNPROTODECLARE_NODE_TYPE: ExternProtoDeclare name='ArtDeco02Material' type cannot be remotely accessed at run time, TODO X3DJSAIL needs to add further capability.\""""))
Scene26.addChild(ExternProtoDeclare86)

Scene26.addComments(CommentsBlock("""Tested ArtDeco01ProtoInstance, ArtDeco02ProtoInstance for improper node type when ProtoInstance is added in wrong place"""))
Shape88 = ShapeObject()
Shape88.setDEF("TestShape1")

Appearance89 = AppearanceObject()
Appearance89.setDEF("TestAppearance1")

ProtoInstance90 = ProtoInstanceObject()
ProtoInstance90.setName("ArtDeco01")

fieldValue91 = fieldValueObject()
fieldValue91.setName("description")
fieldValue91.setValue("ArtDeco01 can substitute for a Material node")

ProtoInstance90.addFieldValue(fieldValue91)

ProtoInstance90.addComments(CommentsBlock("""[HelloWorldProgram diagnostic] ArtDeco01ProtoInstance.getNodeType()=\"ERROR_UNKNOWN_PROTOINSTANCE_NODE_TYPE: ProtoInstance name='ArtDeco01' has no corresponding ProtoDeclareObject or ExternProtoDeclareObject to provide type.\""""))
Appearance89.setProtoInstance(ProtoInstance90)

Appearance89.addComments(CommentsBlock("""ArtDeco01 Material prototype goes here..."""))
Shape88.setAppearance(Appearance89)
Sphere92 = SphereObject()
Sphere92.setRadius(0.001)

Shape88.setGeometry(Sphere92)
Scene26.addChild(Shape88)
Shape93 = ShapeObject()
Shape93.setDEF("TestShape2")

Appearance94 = AppearanceObject()
Appearance94.setDEF("TestAppearance2")

ProtoInstance95 = ProtoInstanceObject()
ProtoInstance95.setName("ArtDeco02")

fieldValue96 = fieldValueObject()
fieldValue96.setName("description")
fieldValue96.setValue("ArtDeco02 can substitute for another Material node")

ProtoInstance95.addFieldValue(fieldValue96)

ProtoInstance95.addComments(CommentsBlock("""[HelloWorldProgram diagnostic] ArtDeco02ProtoInstance.getNodeType()=\"ERROR_UNKNOWN_PROTOINSTANCE_NODE_TYPE: ProtoInstance name='ArtDeco02' has no corresponding ProtoDeclareObject or ExternProtoDeclareObject to provide type.\""""))
Appearance94.setProtoInstance(ProtoInstance95)

Appearance94.addComments(CommentsBlock("""ArtDeco02 Material prototype goes here..."""))
Shape93.setAppearance(Appearance94)
Cone97 = ConeObject()
Cone97.setBottomRadius(0.001)
Cone97.setHeight(0.001)

Shape93.setGeometry(Cone97)
Scene26.addChild(Shape93)
Inline98 = InlineObject()
Inline98.setDEF("inlineSceneDef")
Inline98.setUrl(["someOtherScene.x3d"])

Scene26.addChild(Inline98)
IMPORT99 = IMPORTObject()
IMPORT99.setAS("WorldInfoDEF2")
IMPORT99.setImportedDEF("WorldInfoDEF")
IMPORT99.setInlineDEF("inlineSceneDef")

Scene26.addChild(IMPORT99)
EXPORT100 = EXPORTObject()
EXPORT100.setAS("WorldInfoDEF3")
EXPORT100.setLocalDEF("WorldInfoDEF")

Scene26.addChild(EXPORT100)
ProtoDeclare101 = ProtoDeclareObject()
ProtoDeclare101.setName("MaterialModulator")
ProtoDeclare101.setAppinfo("mimic a Material node and modulate fields as an animation effect")
ProtoDeclare101.setDocumentation("http://x3dgraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/MaterialModulatorIndex.html")

ProtoInterface102 = ProtoInterfaceObject()

field103 = fieldObject()
field103.setType(fieldObject.TYPE_SFBOOL)
field103.setName("enabled")
field103.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field103.setValue("true")

ProtoInterface102.addField(field103)
field104 = fieldObject()
field104.setType(fieldObject.TYPE_SFCOLOR)
field104.setName("diffuseColor")
field104.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field104.setValue("0 0 0")

ProtoInterface102.addField(field104)
field105 = fieldObject()
field105.setType(fieldObject.TYPE_SFCOLOR)
field105.setName("emissiveColor")
field105.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field105.setValue("0.05 0.05 0.5")

ProtoInterface102.addField(field105)
field106 = fieldObject()
field106.setType(fieldObject.TYPE_SFCOLOR)
field106.setName("specularColor")
field106.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field106.setValue("0 0 0")

ProtoInterface102.addField(field106)
field107 = fieldObject()
field107.setType(fieldObject.TYPE_SFFLOAT)
field107.setName("transparency")
field107.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field107.setValue("0")

ProtoInterface102.addField(field107)
field108 = fieldObject()
field108.setType(fieldObject.TYPE_SFFLOAT)
field108.setName("shininess")
field108.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field108.setValue("0")

ProtoInterface102.addField(field108)
field109 = fieldObject()
field109.setType(fieldObject.TYPE_SFFLOAT)
field109.setName("ambientIntensity")
field109.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field109.setValue("0")

ProtoInterface102.addField(field109)
ProtoDeclare101.setProtoInterface(ProtoInterface102)
ProtoBody110 = ProtoBodyObject()

Material111 = MaterialObject()
Material111.setDEF("MaterialNode")

IS112 = ISObject()

connect113 = connectObject()
connect113.setNodeField("diffuseColor")
connect113.setProtoField("diffuseColor")

IS112.addConnect(connect113)
connect114 = connectObject()
connect114.setNodeField("emissiveColor")
connect114.setProtoField("emissiveColor")

IS112.addConnect(connect114)
connect115 = connectObject()
connect115.setNodeField("specularColor")
connect115.setProtoField("specularColor")

IS112.addConnect(connect115)
connect116 = connectObject()
connect116.setNodeField("transparency")
connect116.setProtoField("transparency")

IS112.addConnect(connect116)
connect117 = connectObject()
connect117.setNodeField("shininess")
connect117.setProtoField("shininess")

IS112.addConnect(connect117)
connect118 = connectObject()
connect118.setNodeField("ambientIntensity")
connect118.setProtoField("ambientIntensity")

IS112.addConnect(connect118)
Material111.setIS(IS112)
ProtoBody110.addChild(Material111)

ProtoBody110.addComments(CommentsBlock("""Only first node (the node type) is renderable, others are along for the ride"""))
Script119 = ScriptObject()
Script119.setDEF("MaterialModulatorScript")

field120 = fieldObject()
field120.setType(fieldObject.TYPE_SFBOOL)
field120.setName("enabled")
field120.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)

Script119.addField(field120)
field121 = fieldObject()
field121.setType(fieldObject.TYPE_SFCOLOR)
field121.setName("diffuseColor")
field121.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)

Script119.addField(field121)
field122 = fieldObject()
field122.setType(fieldObject.TYPE_SFCOLOR)
field122.setName("newColor")
field122.setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY)

Script119.addField(field122)
field123 = fieldObject()
field123.setType(fieldObject.TYPE_SFTIME)
field123.setName("clockTrigger")
field123.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)

Script119.addField(field123)
IS124 = ISObject()

connect125 = connectObject()
connect125.setNodeField("enabled")
connect125.setProtoField("enabled")

IS124.addConnect(connect125)
connect126 = connectObject()
connect126.setNodeField("diffuseColor")
connect126.setProtoField("diffuseColor")

IS124.addConnect(connect126)
Script119.setIS(IS124)

Script119.setSourceCode("ecmascript: function initialize () { newColor = diffuseColor; // start with correct color } function set_enabled (newValue) { enabled = newValue; } function clockTrigger (timeValue) { if (!enabled) return; red = newColor.r; green = newColor.g; blue = newColor.b; // note different modulation rates for each color component, % is modulus operator newColor = new SFColor ((red + 0.02) % 1, (green + 0.03) % 1, (blue + 0.04) % 1); if (enabled) { Browser.print ('diffuseColor=(' + red + ',' + green + ',' + blue + ') newColor=' + newColor.toString() + '\\n'); } }\n"+
"")
ProtoBody110.addChild(Script119)
ProtoDeclare101.setProtoBody(ProtoBody110)
Scene26.addChild(ProtoDeclare101)

Scene26.addComments(CommentsBlock("""Test success: declarative statement createDeclarativeShapeTests()"""))
Group127 = GroupObject()
Group127.setDEF("DeclarativeGroupExample")

Shape128 = ShapeObject()

MetadataString129 = MetadataStringObject()
MetadataString129.setName("findThisNameValue")
MetadataString129.setDEF("FindableMetadataStringTest")
MetadataString129.setValue(["test case"])

Shape128.setMetadata(MetadataString129)
Appearance130 = AppearanceObject()
Appearance130.setDEF("DeclarativeAppearanceExample")

ProtoInstance131 = ProtoInstanceObject()
ProtoInstance131.setName("MaterialModulator")
ProtoInstance131.setDEF("MyMaterialModulator")

Appearance130.setProtoInstance(ProtoInstance131)

Appearance130.addComments(CommentsBlock("""DeclarativeMaterialExample gets overridden by subsequently added MaterialModulator ProtoInstance"""))
Shape128.setAppearance(Appearance130)
Cone132 = ConeObject()
Cone132.setBottom(False)
Cone132.setBottomRadius(0.05)
Cone132.setHeight(0.1)

Shape128.setGeometry(Cone132)
Group127.addChild(Shape128)

Group127.addComments(CommentsBlock("""Test success: declarativeGroup.addChild() singleton pipeline method"""))
Scene26.addChild(Group127)

Scene26.addComments(CommentsBlock("""Test success: declarative statement addChild()"""))

Scene26.addComments(CommentsBlock("""Test success: x3dModel.findNodeByDEF(DeclarativeAppearanceExample) = <Appearance DEF='DeclarativeAppearanceExample'/> i.e. <Appearance DEF='DeclarativeAppearanceExample'> <ProtoInstance DEF='MyMaterialModulator' name='MaterialModulator' containerField='material'/> <!- - DeclarativeMaterialExample gets overridden by subsequently added MaterialModulator ProtoInstance - -> </Appearance>"""))

Scene26.addComments(CommentsBlock("""Test success: x3dModel.findElementByNameValue(findThisNameValue) = <MetadataString DEF='FindableMetadataStringTest' name='findThisNameValue' value='\"test case\"'/>"""))

Scene26.addComments(CommentsBlock("""Test success: x3dModel.findElementByNameValue(\"ArtDeco01Material\", \"ProtoDeclare\") found"""))

Scene26.addComments(CommentsBlock("""Test success: x3dModel.findElementByNameValue(\"MaterialModulator\", \"ProtoDeclare\") found"""))

Scene26.addComments(CommentsBlock("""Test success: x3dModel.findElementByNameValue(\"MaterialModulator\", \"ProtoInstance\") found"""))
Group133 = GroupObject()
Group133.setDEF("TestFieldObjectsGroup")


Group133.addComments(CommentsBlock("""testFieldObjects() results"""))

Group133.addComments(CommentsBlock("""SFBool default=true, true=true, false=false, negate()=true"""))

Group133.addComments(CommentsBlock("""MFBool default=, initial=true false true, negate()=false true false"""))

Group133.addComments(CommentsBlock("""SFFloat default=0.0, initial=1.0, setValue(2)=2.0, setValue(3.0f)=3.0, setValue(4.0)=4.0"""))

Group133.addComments(CommentsBlock("""MFFloat default=, initial=1 2 3, append(5)=1 2 3 5, inserts(3,4)(0,0)=0 1 2 3 4 5, append(6)=0 1 2 3 4 5 6, size()=7"""))

Group133.addComments(CommentsBlock("""... get1Value[3]=3.0, remove[1]=0 2 3 4 5 6, set1Value(0,10)=10 2 3 4 5 6, multiply(2)=20 4 6 8 10 12, clear="""))

Group133.addComments(CommentsBlock("""SFVec3f default=0 0 0, initial=1 2 3, setValue=4 5 6, multiply(2)=8 10 12, normalize()=0.45584232 0.5698029 0.68376344"""))
Scene26.addChild(Group133)
Sound134 = SoundObject()

AudioClip135 = AudioClipObject()
AudioClip135.setUrl(["chimes.wav","http://www.web3d.org/x3d/content/examples/ConformanceNist/Sounds/AudioClip/chimes.wav"])

Sound134.setSource(AudioClip135)

Sound134.addComments(CommentsBlock("""Scene example fragment from http://www.web3d.org/x3d/content/examples/ConformanceNist/Sounds/AudioClip/default.x3d"""))
Scene26.addChild(Sound134)
Sound136 = SoundObject()

MovieTexture137 = MovieTextureObject()
MovieTexture137.setUrl(["mpgsys.mpg","http://www.web3d.org/x3d/content/examples/ConformanceNist/Appearance/MovieTexture/mpgsys.mpg"])

Sound136.setSource(MovieTexture137)

Sound136.addComments(CommentsBlock("""Scene example fragment from http://www.web3d.org/x3d/content/examples/ConformanceNist/Appearance/MovieTexture/mpeg1-systems.x3d"""))

Sound136.addComments(CommentsBlock("""Expected containerField='source', allowed containerField values=\"texture\"\"source\"\"back\"\"bottom\"\"front\"\"left\"\"right\"\"top\"\"backTexture\"\"bottomTexture\"\"frontTexture\"\"leftTexture\"\"rightTexture\"\"topTexture\""""))
Scene26.addChild(Sound136)

Scene26.addComments(CommentsBlock("""Test success: AnchorObject.isNode()=true, siteAnchor.isNode()=true"""))

Scene26.addComments(CommentsBlock("""Test success: AnchorObject.isStatement()=false, siteAnchor.isStatement()=false"""))

Scene26.addComments(CommentsBlock("""Test success: ROUTEObject.isNode()=false, orbitPositionROUTE.isNode()=false"""))

Scene26.addComments(CommentsBlock("""Test success: ROUTEObject.isStatement()=true, orbitPositionROUTE.isStatement()=true"""))

Scene26.addComments(CommentsBlock("""Test success: CommentsBlock.isNode()=false, testComments.isNode()=false"""))

Scene26.addComments(CommentsBlock("""Test success: CommentsBlock.isStatement()=false, testComments.isStatement()=false"""))
Shape138 = ShapeObject()
Shape138.setDEF("ExtrusionShape")

Appearance139 = AppearanceObject()
Appearance139.setDEF("TransparentAppearance")

Material140 = MaterialObject()
Material140.setTransparency(1)

Appearance139.setMaterial(Material140)
Shape138.setAppearance(Appearance139)
Extrusion141 = ExtrusionObject()
Extrusion141.setDEF("ExampleExtrusion")

Shape138.setGeometry(Extrusion141)

Shape138.addComments(CommentsBlock("""ExampleExtrusion isCrossSectionClosed()=true, crossSection='[1.0, 1.0, 1.0, -1.0, -1.0, -1.0, -1.0, 1.0, 1.0, 1.0]'"""))

Shape138.addComments(CommentsBlock("""ExampleExtrusion isSpineClosed()=false, spine='[0.0, 0.0, 0.0, 0.0, 1.0, 0.0]'"""))
Scene26.addChild(Shape138)
X3D0.setScene(Scene26)

X3D0.toFileX3D("././HelloWorldProgramOutput.new.x3d")
