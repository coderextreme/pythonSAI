import jnius_config
jnius_config.set_classpath('.', 'X3DJSAIL.3.3.full.jar')
from jnius import autoclass
from X3Dautoclass import *
X3D0 = X3DObject() \
   .setProfile("Immersive") \
   .setVersion("3.3") \
   .setHead(headObject() \
    .addComponent(componentObject() \
     .setName("EnvironmentalEffects") \
     .setLevel(3) \
    ) \
    .addComponent(componentObject() \
     .setName("Shaders") \
     .setLevel(1) \
    ) \
    .addComponent(componentObject() \
     .setName("CubeMapTexturing") \
     .setLevel(1) \
    ) \
    .addMeta(metaObject() \
     .setName("title") \
     .setContent("mirror.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("creator") \
     .setContent("John Carlson") \
    ) \
    .addMeta(metaObject() \
     .setName("generator") \
     .setContent("manual") \
    ) \
    .addMeta(metaObject() \
     .setName("identifier") \
     .setContent("https://coderextreme.net/X3DJSONLD/mirror.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("description") \
     .setContent("sphere with alternating backgrounds") \
    ) \
   ) \
   .setScene(SceneObject() \
    .addChild(ViewpointObject() \
     .setPosition([0,5,100]) \
     .setDescription("Switch background and images texture") \
    ) \
    .addChild(TextureBackgroundObject() \
     .setLeftTexture(ImageTextureObject() \
      .setDEF("leftBack") \
      .setUrl(["../resources/images/all_probes/beach_cross/beach_left.png","https://coderextreme.net/images/all_probes/beach_cross/beach_left.png"]) \
     ) \
     .setRightTexture(ImageTextureObject() \
      .setDEF("rightBack") \
      .setUrl(["../resources/images/all_probes/beach_cross/beach_right.png","https://coderextreme.net/images/all_probes/beach_cross/beach_right.png"]) \
     ) \
     .setFrontTexture(ImageTextureObject() \
      .setDEF("frontBack") \
      .setUrl(["../resources/images/all_probes/beach_cross/beach_front.png","https://coderextreme.net/images/all_probes/beach_cross/beach_front.png"]) \
     ) \
     .setBackTexture(ImageTextureObject() \
      .setDEF("backBack") \
      .setUrl(["../resources/images/all_probes/beach_cross/beach_back.png","https://coderextreme.net/images/all_probes/beach_cross/beach_back.png"]) \
     ) \
     .setTopTexture(ImageTextureObject() \
      .setDEF("topBack") \
      .setUrl(["../resources/images/all_probes/beach_cross/beach_top.png","https://coderextreme.net/images/all_probes/beach_cross/beach_top.png"]) \
     ) \
     .setBottomTexture(ImageTextureObject() \
      .setDEF("bottomBack") \
      .setUrl(["../resources/images/all_probes/beach_cross/beach_bottom.png","https://coderextreme.net/images/all_probes/beach_cross/beach_bottom.png"]) \
     ) \
    ) \
    .addChild(TransformObject() \
     .addChild(ShapeObject() \
      .setAppearance(AppearanceObject() \
       .setMaterial(MaterialObject() \
        .setDiffuseColor([0.7,0.7,0.7]) \
        .setSpecularColor([0.5,0.5,0.5]) \
       ) \
       .setTexture(ComposedCubeMapTextureObject() \
        .setBack(ImageTextureObject() \
         .setDEF("backShader") \
         .setUrl(["../resources/images/all_probes/beach_cross/beach_back.png","https://coderextreme.net/images/all_probes/beach_cross/beach_back.png"]) \
        ) \
        .setBottom(ImageTextureObject() \
         .setDEF("bottomShader") \
         .setUrl(["../resources/images/all_probes/beach_cross/beach_bottom.png","https://coderextreme.net/images/all_probes/beach_cross/beach_bottom.png"]) \
        ) \
        .setFront(ImageTextureObject() \
         .setDEF("frontShader") \
         .setUrl(["../resources/images/all_probes/beach_cross/beach_front.png","https://coderextreme.net/images/all_probes/beach_cross/beach_front.png"]) \
        ) \
        .setLeft(ImageTextureObject() \
         .setDEF("leftShader") \
         .setUrl(["../resources/images/all_probes/beach_cross/beach_left.png","https://coderextreme.net/images/all_probes/beach_cross/beach_left.png"]) \
        ) \
        .setRight(ImageTextureObject() \
         .setDEF("rightShader") \
         .setUrl(["../resources/images/all_probes/beach_cross/beach_right.png","https://coderextreme.net/images/all_probes/beach_cross/beach_right.png"]) \
        ) \
        .setTop(ImageTextureObject() \
         .setDEF("topShader") \
         .setUrl(["../resources/images/all_probes/beach_cross/beach_top.png","https://coderextreme.net/images/all_probes/beach_cross/beach_top.png"]) \
        ) \
       ) \
       .addShaders(ComposedShaderObject() \
        .setDEF("x3dom") \
        .setLanguage("GLSL") \
.addComments(CommentsBlock("""http://hypertextbook.com/facts/2005/JustinChe.shtml""")) \
        .addField(fieldObject() \
         .setType(fieldObject.TYPE_SFVEC3F) \
         .setName("chromaticDispertion") \
         .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
         .setValue("0.98 1 1.033") \
        ) \
        .addField(fieldObject() \
         .setType(fieldObject.TYPE_SFINT32) \
         .setName("cube") \
         .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
         .setValue("0") \
        ) \
        .addField(fieldObject() \
         .setType(fieldObject.TYPE_SFFLOAT) \
         .setName("bias") \
         .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
         .setValue("0.5") \
        ) \
        .addField(fieldObject() \
         .setType(fieldObject.TYPE_SFFLOAT) \
         .setName("scale") \
         .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
         .setValue("0.5") \
        ) \
        .addField(fieldObject() \
         .setType(fieldObject.TYPE_SFFLOAT) \
         .setName("power") \
         .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
         .setValue("2") \
        ) \
        .addParts(ShaderPartObject() \
         .setType("VERTEX") \
         .setUrl(["../shaders/x3dom.vs","https://coderextreme.net/X3DJSONLD/shaders/x3dom.vs"]) \
        ) \
        .addParts(ShaderPartObject() \
         .setType("FRAGMENT") \
         .setUrl(["../shaders/mix.fs","https://coderextreme.net/X3DJSONLD/shaders/mix.fs"]) \
        ) \
       ) \
       .addShaders(ComposedShaderObject() \
        .setDEF("cobweb") \
        .setLanguage("GLSL") \
.addComments(CommentsBlock("""http://hypertextbook.com/facts/2005/JustinChe.shtml""")) \
        .addField(fieldObject() \
         .setType(fieldObject.TYPE_SFVEC3F) \
         .setName("chromaticDispertion") \
         .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
         .setValue("0.98 1 1.033") \
        ) \
        .addField(fieldObject() \
         .setType(fieldObject.TYPE_SFINT32) \
         .setName("cube") \
         .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
         .setValue("0") \
        ) \
        .addField(fieldObject() \
         .setType(fieldObject.TYPE_SFFLOAT) \
         .setName("bias") \
         .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
         .setValue("0.5") \
        ) \
        .addField(fieldObject() \
         .setType(fieldObject.TYPE_SFFLOAT) \
         .setName("scale") \
         .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
         .setValue("0.5") \
        ) \
        .addField(fieldObject() \
         .setType(fieldObject.TYPE_SFFLOAT) \
         .setName("power") \
         .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
         .setValue("2") \
        ) \
        .addParts(ShaderPartObject() \
         .setType("VERTEX") \
         .setUrl(["../shaders/cobweb.vs","https://coderextreme.net/X3DJSONLD/shaders/cobweb.vs"]) \
        ) \
        .addParts(ShaderPartObject() \
         .setType("FRAGMENT") \
         .setUrl(["../shaders/mix.fs","https://coderextreme.net/X3DJSONLD/shaders/mix.fs"]) \
        ) \
       ) \
      ) \
      .setGeometry(SphereObject() \
       .setRadius(30) \
      ) \
     ) \
     .addChild(ScriptObject() \
      .setDEF("UrlSelector") \
      .setDirectOutput(True) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_MFSTRING) \
       .setName("frontUrls") \
       .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
       .setValue("\"../resources/images/all_probes/beach_cross/beach_front.png\" \"../resources/images/all_probes/building_cross/building_front.png\" \"../resources/images/all_probes/campus_cross/campus_front.png\" \"../resources/images/all_probes/galileo_cross/galileo_front.png\" \"../resources/images/all_probes/grace_cross/grace_front.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_front.png\" \"../resources/images/all_probes/rnl_cross/rnl_front.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_front.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_front.png\"") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_MFSTRING) \
       .setName("backUrls") \
       .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
       .setValue("\"../resources/images/all_probes/beach_cross/beach_back.png\" \"../resources/images/all_probes/building_cross/building_back.png\" \"../resources/images/all_probes/campus_cross/campus_back.png\" \"../resources/images/all_probes/galileo_cross/galileo_back.png\" \"../resources/images/all_probes/grace_cross/grace_back.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_back.png\" \"../resources/images/all_probes/rnl_cross/rnl_back.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_back.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_back.png\"") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_MFSTRING) \
       .setName("leftUrls") \
       .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
       .setValue("\"../resources/images/all_probes/beach_cross/beach_left.png\" \"../resources/images/all_probes/building_cross/building_left.png\" \"../resources/images/all_probes/campus_cross/campus_left.png\" \"../resources/images/all_probes/galileo_cross/galileo_left.png\" \"../resources/images/all_probes/grace_cross/grace_left.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_left.png\" \"../resources/images/all_probes/rnl_cross/rnl_left.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_left.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_left.png\"") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_MFSTRING) \
       .setName("rightUrls") \
       .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
       .setValue("\"../resources/images/all_probes/beach_cross/beach_right.png\" \"../resources/images/all_probes/building_cross/building_right.png\" \"../resources/images/all_probes/campus_cross/campus_right.png\" \"../resources/images/all_probes/galileo_cross/galileo_right.png\" \"../resources/images/all_probes/grace_cross/grace_right.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_right.png\" \"../resources/images/all_probes/rnl_cross/rnl_right.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_right.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_right.png\"") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_MFSTRING) \
       .setName("topUrls") \
       .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
       .setValue("\"../resources/images/all_probes/beach_cross/beach_top.png\" \"../resources/images/all_probes/building_cross/building_top.png\" \"../resources/images/all_probes/campus_cross/campus_top.png\" \"../resources/images/all_probes/galileo_cross/galileo_top.png\" \"../resources/images/all_probes/grace_cross/grace_top.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_top.png\" \"../resources/images/all_probes/rnl_cross/rnl_top.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_top.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_top.png\"") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_MFSTRING) \
       .setName("bottomUrls") \
       .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
       .setValue("\"../resources/images/all_probes/beach_cross/beach_bottom.png\" \"../resources/images/all_probes/building_cross/building_bottom.png\" \"../resources/images/all_probes/campus_cross/campus_bottom.png\" \"../resources/images/all_probes/galileo_cross/galileo_bottom.png\" \"../resources/images/all_probes/grace_cross/grace_bottom.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_bottom.png\" \"../resources/images/all_probes/rnl_cross/rnl_bottom.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_bottom.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_bottom.png\"") \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_MFSTRING) \
       .setName("front_changed") \
       .setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY) \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_MFSTRING) \
       .setName("back_changed") \
       .setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY) \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_MFSTRING) \
       .setName("left_changed") \
       .setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY) \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_MFSTRING) \
       .setName("right_changed") \
       .setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY) \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_MFSTRING) \
       .setName("top_changed") \
       .setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY) \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_MFSTRING) \
       .setName("bottom_changed") \
       .setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY) \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFFLOAT) \
       .setName("set_fraction") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTONLY) \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFINT32) \
       .setName("old") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setValue("-1") \
      ) \
.setSourceCode('''ecmascript:\n"+
"        function set_fraction( f, tm ) {\n"+
"	    var side = Math.floor(f*frontUrls.length);\n"+
"	    if (side > frontUrls.length-1) {\n"+
"	    	side = 0;\n"+
"	    }\n"+
"	    if (side != old) {\n"+
"	    	    Browser.print(f+\" \"+side);\n"+
"	    	    old = side;\n"+
"		    front_changed[0] = frontUrls[side];\n"+
"		    back_changed[0] = backUrls[side];\n"+
"		    left_changed[0] = leftUrls[side];\n"+
"		    right_changed[0] = rightUrls[side];\n"+
"		    top_changed[0] = topUrls[side];\n"+
"		    bottom_changed[0] = bottomUrls[side];\n"+
"            }\n"+
"        }''')
     ) \
     .addChild(TimeSensorObject() \
      .setDEF("Clock") \
      .setCycleInterval(45) \
      .setLoop(True) \
     ) \
     .addChild(ROUTEObject() \
      .setFromNode("Clock") \
      .setFromField("fraction_changed") \
      .setToNode("UrlSelector") \
      .setToField("set_fraction") \
     ) \
     .addChild(ROUTEObject() \
      .setFromNode("UrlSelector") \
      .setFromField("front_changed") \
      .setToNode("frontBack") \
      .setToField("url") \
     ) \
     .addChild(ROUTEObject() \
      .setFromNode("UrlSelector") \
      .setFromField("back_changed") \
      .setToNode("backBack") \
      .setToField("url") \
     ) \
     .addChild(ROUTEObject() \
      .setFromNode("UrlSelector") \
      .setFromField("left_changed") \
      .setToNode("leftBack") \
      .setToField("url") \
     ) \
     .addChild(ROUTEObject() \
      .setFromNode("UrlSelector") \
      .setFromField("right_changed") \
      .setToNode("rightBack") \
      .setToField("url") \
     ) \
     .addChild(ROUTEObject() \
      .setFromNode("UrlSelector") \
      .setFromField("top_changed") \
      .setToNode("topBack") \
      .setToField("url") \
     ) \
     .addChild(ROUTEObject() \
      .setFromNode("UrlSelector") \
      .setFromField("bottom_changed") \
      .setToNode("bottomBack") \
      .setToField("url") \
     ) \
     .addChild(ROUTEObject() \
      .setFromNode("UrlSelector") \
      .setFromField("front_changed") \
      .setToNode("frontShader") \
      .setToField("url") \
     ) \
     .addChild(ROUTEObject() \
      .setFromNode("UrlSelector") \
      .setFromField("back_changed") \
      .setToNode("backShader") \
      .setToField("url") \
     ) \
     .addChild(ROUTEObject() \
      .setFromNode("UrlSelector") \
      .setFromField("left_changed") \
      .setToNode("leftShader") \
      .setToField("url") \
     ) \
     .addChild(ROUTEObject() \
      .setFromNode("UrlSelector") \
      .setFromField("right_changed") \
      .setToNode("rightShader") \
      .setToField("url") \
     ) \
     .addChild(ROUTEObject() \
      .setFromNode("UrlSelector") \
      .setFromField("top_changed") \
      .setToNode("topShader") \
      .setToField("url") \
     ) \
     .addChild(ROUTEObject() \
      .setFromNode("UrlSelector") \
      .setFromField("bottom_changed") \
      .setToNode("bottomShader") \
      .setToField("url") \
     ) \
    ) \
   ) \

X3D0.toFileX3D("./future/./mirror.newf.x3d")
