import jnius_config
jnius_config.set_classpath('.', 'X3DJSAIL.3.3.full.jar')
from jnius import autoclass
from X3Dautoclass import *
X3D0 = X3DObject() \
   .setProfile("Immersive") \
   .setVersion("3.3") \
   .setHead(headObject() \
.addComments(CommentsBlock("""comment #1""")) \
.addComments(CommentsBlock("""comment #2""")) \
.addComments(CommentsBlock("""comment #3""")) \
.addComments(CommentsBlock("""comment #4""")) \
    .addComponent(componentObject() \
     .setName("Navigation") \
     .setLevel(3) \
    ) \
    .addComponent(componentObject() \
     .setName("Layering") \
     .setLevel(1) \
    ) \
    .addUnit(unitObject() \
     .setName("AngleUnitConversion") \
     .setCategory("angle") \
     .setConversionFactor(1) \
    ) \
    .addUnit(unitObject() \
     .setName("LengthUnitConversion") \
     .setCategory("length") \
     .setConversionFactor(1) \
    ) \
    .addMeta(metaObject() \
     .setName("title") \
     .setContent("HelloWorldProgramOutput.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("description") \
     .setContent("Example HelloWorldProgram creates an X3D model using the X3D Java Scene Access Interface (SAI) Library") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("http://www.web3d.org/specifications/java/X3DJSAIL.html") \
    ) \
    .addMeta(metaObject() \
     .setName("generator") \
     .setContent("HelloWorldProgramOutput.java") \
    ) \
    .addMeta(metaObject() \
     .setName("created") \
     .setContent("6 September 2016") \
    ) \
    .addMeta(metaObject() \
     .setName("modified") \
     .setContent("10 September 2018") \
    ) \
    .addMeta(metaObject() \
     .setName("generator") \
     .setContent("X3D Java Scene Access Interface Library (X3DJSAIL)") \
    ) \
    .addMeta(metaObject() \
     .setName("generator") \
     .setContent("http://www.web3d.org/specifications/java/examples/HelloWorldProgram.java") \
    ) \
    .addMeta(metaObject() \
     .setName("generator") \
     .setContent("Netbeans http://www.netbeans.org") \
    ) \
    .addMeta(metaObject() \
     .setName("creator") \
     .setContent("Don Brutzman") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("https://sourceforge.net/p/x3d/code/HEAD/tree/www.web3d.org/x3d/stylesheets/java/examples/HelloWorldProgramOutput.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("Console output, ClassicVRML encoding, VRML97 encoding and pretty-print documentation:") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("HelloWorldProgramOutput.txt") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("HelloWorldProgramOutput.x3dv") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("HelloWorldProgramOutput.wrl") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("HelloWorldProgramOutput.html") \
    ) \
    .addMeta(metaObject() \
     .setName("X3dValidator") \
     .setContent("https://savage.nps.edu/X3dValidator?url=http://www.web3d.org/specifications/java/examples/HelloWorldProgramOutput.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("identifier") \
     .setContent("http://www.web3d.org/specifications/java/examples/HelloWorldProgramOutput.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("license") \
     .setContent("../license.html") \
    ) \
    .addMeta(metaObject() \
     .setName("SpecialTest") \
     .setContent("tested sat: name value cannot contain embedded space character") \
    ) \
   ) \
   .setScene(SceneObject() \
    .addChild(ViewpointGroupObject() \
     .setDescription("Available viewpoints") \
     .addChild(ViewpointObject() \
      .setDEF("DefaultView") \
      .setDescription("Hello X3DJSAIL") \
     ) \
     .addChild(ViewpointObject() \
      .setDEF("TopDownView") \
      .setDescription("top-down view from above") \
      .setOrientation([1,0,0,-1.570796]) \
      .setPosition([0,100,0]) \
     ) \
    ) \
    .addChild(WorldInfoObject() \
     .setDEF("WorldInfoDEF") \
     .setTitle("HelloWorldProgram produced by X3D Java SAI Library (X3DJSAIL)") \
    ) \
    .addChild(WorldInfoObject() \
     .setUSE("WorldInfoDEF") \
    ) \
    .addChild(WorldInfoObject() \
     .setUSE("WorldInfoDEF") \
    ) \
    .addChild(MetadataStringObject() \
     .setName("test") \
     .setDEF("scene.addChildMetadata") \
     .setValue(["Top-level root Metadata node beneath Scene needs to be one of '-children' in JSON encoding"]) \
    ) \
    .addLayerSet(LayerSetObject() \
     .setDEF("scene.addChildLayerSetTest") \
    ) \
    .addChild(TransformObject() \
     .setDEF("LogoGeometryTransform") \
     .setTranslation([0,1.5,0]) \
     .addChild(AnchorObject() \
      .setDescription("select for X3D Java SAI Library (X3DJSAIL) description") \
      .setUrl(["../X3DJSAIL.html","http://www.web3d.org/specifications/java/X3DJSAIL.html"]) \
      .addChild(ShapeObject() \
       .setDEF("BoxShape") \
       .setAppearance(AppearanceObject() \
        .setMaterial(MaterialObject() \
         .setDEF("GreenMaterial") \
         .setDiffuseColor([0,1,1]) \
         .setEmissiveColor([0.8,0,0]) \
         .setTransparency(0.1) \
        ) \
        .setTexture(ImageTextureObject() \
         .setUrl(["images/X3dJavaSceneAccessInterfaceSaiLibrary.png","http://www.web3d.org/specifications/java/examples/images/X3dJavaSceneAccessInterfaceSaiLibrary.png"]) \
        ) \
       ) \
       .setGeometry(BoxObject() \
        .setDEF("test-NMTOKEN_regex.0123456789") \
        .setCssClass("untextured") \
       ) \
      ) \
     ) \
    ) \
    .addChild(ShapeObject() \
     .setDEF("LineShape") \
     .setAppearance(AppearanceObject() \
      .setMaterial(MaterialObject() \
       .setEmissiveColor([0.6,0.19607843,0.8]) \
      ) \
     ) \
     .setGeometry(IndexedLineSetObject() \
      .setCoordIndex([0,1,2,3,4,0]) \
.addComments(CommentsBlock("""Coordinate 3-tuple point count: 6""")) \
      .setCoord(CoordinateObject() \
       .setPoint([0,1.5,0,2,1.5,0,2,1.5,-2,-2,1.5,-2,-2,1.5,0,0,1.5,0]) \
      ) \
     ) \
    ) \
    .addChild(PositionInterpolatorObject() \
     .setDEF("BoxPathAnimator") \
     .setKey([0,0.125,0.375,0.625,0.875,1]) \
     .setKeyValue([0,1.5,0,2,1.5,0,2,1.5,-2,-2,1.5,-2,-2,1.5,0,0,1.5,0]) \
    ) \
    .addChild(TimeSensorObject() \
     .setDEF("OrbitClock") \
     .setCycleInterval(8) \
     .setLoop(True) \
    ) \
    .addChild(ROUTEObject() \
     .setFromField("fraction_changed") \
     .setFromNode("OrbitClock") \
     .setToField("set_fraction") \
     .setToNode("BoxPathAnimator") \
    ) \
    .addChild(ROUTEObject() \
     .setFromField("value_changed") \
     .setFromNode("BoxPathAnimator") \
     .setToField("set_translation") \
     .setToNode("LogoGeometryTransform") \
    ) \
    .addChild(TransformObject() \
     .setDEF("TextTransform") \
     .setTranslation([0,-1.5,0]) \
     .addChild(ShapeObject() \
      .setAppearance(AppearanceObject() \
       .setMaterial(MaterialObject() \
        .setUSE("GreenMaterial") \
       ) \
      ) \
      .setGeometry(TextObject() \
       .setString(["X3D Java","SAI Library","X3DJSAIL"]) \
.addComments(CommentsBlock("""Comment example A, plain quotation marks: He said, \"Immel did it!\"""")) \
.addComments(CommentsBlock("""Comment example B, XML character entities: He said, &quot;Immel did it!&quot;""")) \
       .setMetadata(MetadataSetObject() \
        .setName("EscapedQuotationMarksMetadataSet") \
        .addValue(MetadataStringObject() \
         .setName("quotesTestC") \
         .setValue(["MFString example C, backslash-escaped quotes: He said, \"Immel did it!\""]) \
        ) \
        .addValue(MetadataStringObject() \
         .setName("extraChildTest") \
         .setValue(["checks MetadataSetObject addValue() method"]) \
        ) \
       ) \
       .setFontStyle(FontStyleObject() \
        .setJustify(["MIDDLE","MIDDLE"]) \
       ) \
      ) \
     ) \
     .addChild(CollisionObject() \
.addComments(CommentsBlock("""test containerField='proxy'""")) \
      .setProxy(ShapeObject() \
       .setDEF("ProxyShape") \
.addComments(CommentsBlock("""alternative XML encoding: Text string='\"One, Two, Comment\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\"'""")) \
.addComments(CommentsBlock("""alternative XML encoding: Text string='\"One, Two, Comment\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\" \"\"'""")) \
.addComments(CommentsBlock("""alternative Java source: .setString(new String [] {\"One, Two, Comment\", \"\", \"He said, \\\"\"Immel did it!\\\"\"\"})""")) \
.addComments(CommentsBlock("""reference: http://www.web3d.org/x3d/content/examples/Basic/X3dSpecifications/StringArrayEncodingExamplesIndex.html""")) \
       .setGeometry(TextObject() \
        .setString(["One, Two, Text","","He said, \"Immel did it!\" \"\""]) \
       ) \
      ) \
     ) \
.addComments(CommentsBlock("""It's a beautiful world""")) \
.addComments(CommentsBlock("""... for you!""")) \
.addComments(CommentsBlock("""https://en.wikipedia.org/wiki/Beautiful_World_(Devo_song)""")) \
    ) \
.addComments(CommentsBlock("""repeatedly spin 180 degrees as a readable special effect""")) \
    .addChild(OrientationInterpolatorObject() \
     .setDEF("SpinInterpolator") \
     .setKey([0,0.5,1]) \
     .setKeyValue([0,1,0,4.712389,0,1,0,0,0,1,0,1.5707964]) \
    ) \
    .addChild(TimeSensorObject() \
     .setDEF("SpinClock") \
     .setCycleInterval(5) \
     .setLoop(True) \
    ) \
    .addChild(ROUTEObject() \
     .setFromField("fraction_changed") \
     .setFromNode("SpinClock") \
     .setToField("set_fraction") \
     .setToNode("SpinInterpolator") \
    ) \
    .addChild(ROUTEObject() \
     .setFromField("value_changed") \
     .setFromNode("SpinInterpolator") \
     .setToField("rotation") \
     .setToNode("TextTransform") \
    ) \
    .addChild(GroupObject() \
     .setDEF("BackgroundGroup") \
     .addChild(BackgroundObject() \
      .setDEF("GradualBackground") \
     ) \
     .addChild(ScriptObject() \
      .setDEF("colorTypeConversionScript") \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFCOLOR) \
       .setName("colorInput") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTONLY) \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_MFCOLOR) \
       .setName("colorsOutput") \
       .setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY) \
      ) \
.setSourceCode('''ecmascript:\n"+
"\n"+
"function colorInput (eventValue) // Example source code\n"+
"{\n"+
"   colorsOutput = new MFColor(eventValue); // assigning value sends output event\n"+
"// Browser.print('colorInput=' + eventValue + ', colorsOutput=' + colorsOutput + '\\n');\n"+
"}''')
     ) \
     .addChild(ColorInterpolatorObject() \
      .setDEF("ColorAnimator") \
      .setKey([0,0.5,1]) \
      .setKeyValue([0.9411765,1,1,0.29411766,0,0.50980395,0.9411765,1,1]) \
.addComments(CommentsBlock("""AZURE to INDIGO and back again""")) \
     ) \
     .addChild(TimeSensorObject() \
      .setDEF("ColorClock") \
      .setCycleInterval(60) \
      .setLoop(True) \
     ) \
     .addChild(ROUTEObject() \
      .setFromField("colorsOutput") \
      .setFromNode("colorTypeConversionScript") \
      .setToField("skyColor") \
      .setToNode("GradualBackground") \
     ) \
     .addChild(ROUTEObject() \
      .setFromField("value_changed") \
      .setFromNode("ColorAnimator") \
      .setToField("colorInput") \
      .setToNode("colorTypeConversionScript") \
     ) \
     .addChild(ROUTEObject() \
      .setFromField("fraction_changed") \
      .setFromNode("ColorClock") \
      .setToField("set_fraction") \
      .setToNode("ColorAnimator") \
     ) \
    ) \
    .addChild(ProtoDeclareObject() \
     .setName("ArtDeco01Material") \
     .setAppinfo("tooltip: ArtDeco01Material prototype is a Material node") \
     .setProtoInterface(ProtoInterfaceObject() \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFSTRING) \
       .setName("description") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setAppinfo("tooltip for descriptionField") \
       .setValue("ArtDeco01Material prototype is a Material node") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFBOOL) \
       .setName("enabled") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setValue("true") \
      ) \
     ) \
     .setProtoBody(ProtoBodyObject() \
.addComments(CommentsBlock("""Initial node of ProtoBody determines prototype node type""")) \
      .addChild(MaterialObject() \
       .setAmbientIntensity(0.25) \
       .setDiffuseColor([0.282435,0.085159,0.134462]) \
       .setShininess(0.127273) \
       .setSpecularColor([0.276305,0.11431,0.139857]) \
      ) \
.addComments(CommentsBlock("""[HelloWorldProgram diagnostic] should be connected to scene graph: ArtDeco01ProtoDeclare.getNodeType()=\"Material\"""")) \
.addComments(CommentsBlock("""presence of follow-on TouchSensor shows that additional nodes are allowed in ProtoBody after initial node, regardless of node types""")) \
      .addChild(TouchSensorObject() \
       .setDescription("within ProtoBody") \
       .setIS(ISObject() \
        .addConnect(connectObject() \
         .setNodeField("description") \
         .setProtoField("description") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("enabled") \
         .setProtoField("enabled") \
        ) \
       ) \
      ) \
     ) \
    ) \
    .addChild(ExternProtoDeclareObject() \
     .setName("ArtDeco02Material") \
     .setAppinfo("this is a different Material node") \
     .setUrl(["http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3d#ArtDeco02Material","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3dv#ArtDeco02Material"]) \
.addComments(CommentsBlock("""[HelloWorldProgram diagnostic] ArtDeco02ExternProtoDeclare.getNodeType()=\"ERROR_UNKNOWN_EXTERNPROTODECLARE_NODE_TYPE: ExternProtoDeclare name='ArtDeco02Material' type cannot be remotely accessed at run time, TODO X3DJSAIL needs to add further capability.\"""")) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFSTRING) \
      .setName("description") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setAppinfo("tooltip for descriptionField") \
     ) \
    ) \
.addComments(CommentsBlock("""Tested ArtDeco01ProtoInstance, ArtDeco02ProtoInstance for improper node type when ProtoInstance is added in wrong place""")) \
    .addChild(ShapeObject() \
     .setDEF("TestShape1") \
     .setAppearance(AppearanceObject() \
      .setDEF("TestAppearance1") \
.addComments(CommentsBlock("""ArtDeco01Material prototype goes here... TODO ensure setContainerField is handled in exported Java""")) \
      .setMaterial(ProtoInstanceObject() \
       .setName("ArtDeco01Material") \
.addComments(CommentsBlock("""[HelloWorldProgram diagnostic] ArtDeco01ProtoInstance.getNodeType()=\"Material\"""")) \
       .addFieldValue(fieldValueObject() \
        .setName("description") \
        .setValue("ArtDeco01Material can substitute for a Material node") \
       ) \
      ) \
     ) \
     .setGeometry(SphereObject() \
      .setRadius(0.001) \
     ) \
    ) \
    .addChild(ShapeObject() \
     .setDEF("TestShape2") \
     .setAppearance(AppearanceObject() \
      .setDEF("TestAppearance2") \
.addComments(CommentsBlock("""ArtDeco02Material prototype goes here... TODO ensure setContainerField is handled in exported Java""")) \
      .setMaterial(ProtoInstanceObject() \
       .setName("ArtDeco02Material") \
       .setDEF("ArtDeco02MaterialDEF") \
.addComments(CommentsBlock("""[HelloWorldProgram diagnostic] ArtDeco02ProtoInstance.getNodeType()=\"ERROR_UNKNOWN_EXTERNPROTODECLARE_NODE_TYPE: ExternProtoDeclare name='ArtDeco02Material' type cannot be remotely accessed at run time, TODO X3DJSAIL needs to add further capability.\"""")) \
       .addFieldValue(fieldValueObject() \
        .setName("description") \
        .setValue("ArtDeco02Material can substitute for another Material node") \
       ) \
      ) \
     ) \
     .setGeometry(ConeObject() \
      .setBottomRadius(0.001) \
      .setHeight(0.001) \
     ) \
    ) \
    .addChild(ShapeObject() \
     .setDEF("TestShape3") \
     .setAppearance(AppearanceObject() \
      .setDEF("TestAppearance3") \
.addComments(CommentsBlock("""ArtDeco02Material ProtoInstance USE goes here...""")) \
      .setMaterial(ProtoInstanceObject() \
       .setUSE("ArtDeco02MaterialDEF") \
      ) \
     ) \
     .setGeometry(CylinderObject() \
      .setHeight(0.001) \
      .setRadius(0.001) \
     ) \
    ) \
    .addChild(InlineObject() \
     .setDEF("inlineSceneDef") \
     .setUrl(["someOtherScene.x3d"]) \
    ) \
    .addChild(IMPORTObject() \
     .setAS("WorldInfoDEF2") \
     .setImportedDEF("WorldInfoDEF") \
     .setInlineDEF("inlineSceneDef") \
    ) \
    .addChild(EXPORTObject() \
     .setAS("WorldInfoDEF3") \
     .setLocalDEF("WorldInfoDEF") \
    ) \
    .addChild(ProtoDeclareObject() \
     .setName("MaterialModulator") \
     .setAppinfo("mimic a Material node and modulate fields as an animation effect") \
     .setDocumentation("http://x3dgraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/MaterialModulatorIndex.html") \
     .setProtoInterface(ProtoInterfaceObject() \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFBOOL) \
       .setName("enabled") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setValue("true") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFCOLOR) \
       .setName("diffuseColor") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setValue("0 0 0") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFCOLOR) \
       .setName("emissiveColor") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setValue("0.05 0.05 0.5") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFCOLOR) \
       .setName("specularColor") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setValue("0 0 0") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFFLOAT) \
       .setName("transparency") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setValue("0") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFFLOAT) \
       .setName("shininess") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setValue("0") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFFLOAT) \
       .setName("ambientIntensity") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setValue("0") \
      ) \
     ) \
     .setProtoBody(ProtoBodyObject() \
      .addChild(MaterialObject() \
       .setDEF("MaterialNode") \
       .setIS(ISObject() \
        .addConnect(connectObject() \
         .setNodeField("diffuseColor") \
         .setProtoField("diffuseColor") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("emissiveColor") \
         .setProtoField("emissiveColor") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("specularColor") \
         .setProtoField("specularColor") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("transparency") \
         .setProtoField("transparency") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("shininess") \
         .setProtoField("shininess") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("ambientIntensity") \
         .setProtoField("ambientIntensity") \
        ) \
       ) \
      ) \
.addComments(CommentsBlock("""Only first node (the node type) is renderable, others are along for the ride""")) \
      .addChild(ScriptObject() \
       .setDEF("MaterialModulatorScript") \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFBOOL) \
        .setName("enabled") \
        .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFCOLOR) \
        .setName("diffuseColor") \
        .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFCOLOR) \
        .setName("newColor") \
        .setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY) \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFTIME) \
        .setName("clockTrigger") \
        .setAccessType(fieldObject.ACCESSTYPE_INPUTONLY) \
       ) \
       .setIS(ISObject() \
        .addConnect(connectObject() \
         .setNodeField("enabled") \
         .setProtoField("enabled") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("diffuseColor") \
         .setProtoField("diffuseColor") \
        ) \
       ) \
.setSourceCode('''ecmascript:\n"+
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
"}''')
      ) \
     ) \
    ) \
.addComments(CommentsBlock("""Test success: declarative statement createDeclarativeShapeTests()""")) \
    .addChild(GroupObject() \
     .setDEF("DeclarativeGroupExample") \
     .addChild(ShapeObject() \
      .setMetadata(MetadataStringObject() \
       .setName("findThisNameValue") \
       .setDEF("FindableMetadataStringTest") \
       .setValue(["test case"]) \
      ) \
      .setAppearance(AppearanceObject() \
       .setDEF("DeclarativeAppearanceExample") \
.addComments(CommentsBlock("""DeclarativeMaterialExample gets overridden by subsequently added MaterialModulator ProtoInstance""")) \
       .setMaterial(ProtoInstanceObject() \
        .setName("MaterialModulator") \
        .setDEF("MyMaterialModulator") \
       ) \
      ) \
      .setGeometry(ConeObject() \
       .setBottom(False) \
       .setBottomRadius(0.05) \
       .setHeight(0.1) \
      ) \
     ) \
.addComments(CommentsBlock("""Test success: declarativeGroup.addChild() singleton pipeline method""")) \
    ) \
.addComments(CommentsBlock("""Test success: declarative statement addChild()""")) \
.addComments(CommentsBlock("""Test success: x3dModel.findNodeByDEF(DeclarativeAppearanceExample) = <Appearance DEF='DeclarativeAppearanceExample'/> i.e. <Appearance DEF='DeclarativeAppearanceExample'> <!- - DeclarativeMaterialExample gets overridden by subsequently added MaterialModulator ProtoInstance - -> <ProtoInstance DEF='MyMaterialModulator' name='MaterialModulator' containerField='material'/> </Appearance>""")) \
.addComments(CommentsBlock("""Test success: x3dModel.findElementByNameValue(findThisNameValue) = <MetadataString DEF='FindableMetadataStringTest' name='findThisNameValue' value='\"test case\"'/>""")) \
.addComments(CommentsBlock("""Test success: x3dModel.findElementByNameValue(\"ArtDeco01Material\", \"ProtoDeclare\") found""")) \
.addComments(CommentsBlock("""Test success: x3dModel.findElementByNameValue(\"MaterialModulator\", \"ProtoDeclare\") found""")) \
.addComments(CommentsBlock("""Test success: x3dModel.findElementByNameValue(\"MaterialModulator\", \"ProtoInstance\") found""")) \
    .addChild(GroupObject() \
     .setDEF("TestFieldObjectsGroup") \
.addComments(CommentsBlock("""testFieldObjects() results""")) \
.addComments(CommentsBlock("""SFBool default=true, true=true, false=false, negate()=true""")) \
.addComments(CommentsBlock("""MFBool default=, initial=true false true, negate()=false true false""")) \
.addComments(CommentsBlock("""SFFloat default=0.0, initial=1.0, setValue(2)=2.0, setValue(3.0f)=3.0, setValue(4.0)=4.0""")) \
.addComments(CommentsBlock("""MFFloat default=, initial=1 2 3, append(5)=1 2 3 5, inserts(3,4)(0,0)=0 1 2 3 4 5, append(6)=0 1 2 3 4 5 6, size()=7""")) \
.addComments(CommentsBlock("""... get1Value[3]=3.0, remove[1]=0 2 3 4 5 6, set1Value(0,10)=10 2 3 4 5 6, multiply(2)=20 4 6 8 10 12, clear=""")) \
.addComments(CommentsBlock("""SFVec3f default=0 0 0, initial=1 2 3, setValue=4 5 6, multiply(2)=8 10 12, normalize()=0.45584232 0.5698029 0.68376344, regex matches()=true""")) \
.addComments(CommentsBlock("""regex test SFVec3f().matches(\"1 2 3\")=true, regex test SFVec3f().matches(\"1 2 3 4\")=false, regex test (SFRotationObject.matches(\"0 0 0 0\")=true, failure detecting illegal (zero axis) rotation value""")) \
    ) \
    .addChild(SoundObject() \
     .setLocation([0,1.6,0]) \
.addComments(CommentsBlock("""set sound-ellipsoid location height at 1.6m to match typical avatar height""")) \
     .setSource(AudioClipObject() \
      .setDescription("chimes") \
      .setUrl(["chimes.wav","http://www.web3d.org/x3d/content/examples/ConformanceNist/Sounds/AudioClip/chimes.wav"]) \
.addComments(CommentsBlock("""Scene example fragment from http://www.web3d.org/x3d/content/examples/ConformanceNist/Sounds/AudioClip/default.x3d""")) \
     ) \
    ) \
    .addChild(SoundObject() \
     .setLocation([0,1.6,0]) \
.addComments(CommentsBlock("""set sound-ellipsoid location height at 1.6m to match typical avatar height""")) \
     .setSource(MovieTextureObject() \
      .setDescription("mpgsys.mpg from ConformanceNist suite") \
      .setUrl(["mpgsys.mpg","http://www.web3d.org/x3d/content/examples/ConformanceNist/Appearance/MovieTexture/mpgsys.mpg"]) \
.addComments(CommentsBlock("""Scene example fragment from http://www.web3d.org/x3d/content/examples/ConformanceNist/Appearance/MovieTexture/mpeg1-systems.x3d""")) \
.addComments(CommentsBlock("""Expected containerField='source', allowed containerField values=\"texture\" \"source\" \"back\" \"bottom\" \"front\" \"left\" \"right\" \"top\" \"backTexture\" \"bottomTexture\" \"frontTexture\" \"leftTexture\" \"rightTexture\" \"topTexture\" \"watchList\"""")) \
     ) \
    ) \
.addComments(CommentsBlock("""Test success: AnchorObject.isNode()=true, siteAnchor.isNode()=true""")) \
.addComments(CommentsBlock("""Test success: AnchorObject.isStatement()=false, siteAnchor.isStatement()=false""")) \
.addComments(CommentsBlock("""Test success: ROUTEObject.isNode()=false, orbitPositionROUTE.isNode()=false""")) \
.addComments(CommentsBlock("""Test success: ROUTEObject.isStatement()=true, orbitPositionROUTE.isStatement()=true""")) \
.addComments(CommentsBlock("""Test success: CommentsBlock.isNode()=false, testComments.isNode()=false""")) \
.addComments(CommentsBlock("""Test failure: CommentsBlock.isStatement()=true, testComments.isStatement()=true""")) \
    .addChild(ShapeObject() \
     .setDEF("ExtrusionShape") \
.addComments(CommentsBlock("""ExampleExtrusion isCrossSectionClosed()=true, crossSection='[1.0, 1.0, 1.0, -1.0, -1.0, -1.0, -1.0, 1.0, 1.0, 1.0]'""")) \
.addComments(CommentsBlock("""ExampleExtrusion isSpineClosed()=false, spine='[0.0, 0.0, 0.0, 0.0, 1.0, 0.0]'""")) \
     .setAppearance(AppearanceObject() \
      .setDEF("TransparentAppearance") \
      .setMaterial(MaterialObject() \
       .setTransparency(1) \
      ) \
     ) \
     .setGeometry(ExtrusionObject() \
      .setDEF("ExampleExtrusion") \
     ) \
    ) \
   ) \

X3D0.toFileX3D("./future/./HelloWorldProgramOutput.newf.x3d")
