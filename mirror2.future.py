import jnius_config
jnius_config.set_classpath('.', 'X3DJSAIL.3.3.full.jar')
from jnius import autoclass
from X3Dautoclass import *
X3D0 = X3DObject() \
   .setProfile("Immersive") \
   .setVersion("3.3") \
   .setHead(headObject() \
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
     .setContent("mirro2.x3d") \
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
     .setContent("https://coderextreme.net/X3DJSONLD/mirro2.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("description") \
     .setContent("a mirrored sphere") \
    ) \
   ) \
   .setScene(SceneObject() \
    .addChildren(ViewpointObject() \
     .setPosition([0,5,100]) \
     .setDescription("Switch background and images texture") \
    ) \
    .addChildren(BackgroundObject() \
     .setDEF("cube") \
     .setLeftUrl(["../resources/images/all_probes/beach_cross/beach_left.png","https://coderextreme.net/images/all_probes/beach_cross/beach_left.png"]) \
     .setRightUrl(["../resources/images/all_probes/beach_cross/beach_right.png","https://coderextreme.net/images/all_probes/beach_cross/beach_right.png"]) \
     .setFrontUrl(["../resources/images/all_probes/beach_cross/beach_front.png","https://coderextreme.net/images/all_probes/beach_cross/beach_front.png"]) \
     .setBackUrl(["../resources/images/all_probes/beach_cross/beach_back.png","https://coderextreme.net/images/all_probes/beach_cross/beach_back.png"]) \
     .setTopUrl(["../resources/images/all_probes/beach_cross/beach_top.png","https://coderextreme.net/images/all_probes/beach_cross/beach_top.png"]) \
     .setBottomUrl(["../resources/images/all_probes/beach_cross/beach_bottom.png","https://coderextreme.net/images/all_probes/beach_cross/beach_bottom.png"]) \
    ) \
    .addChildren(TransformObject() \
     .addChildren(ShapeObject() \
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
       .addShaders(ComposedShaderObject(language = "GLSL") \
        .setDEF("cobweb") \
#http://hypertextbook.com/facts/2005/JustinChe.shtml
        .addField(fieldObject() \
         .setName("chromaticDispertion") \
         .setAccessType("inputOutput") \
         .setType("SFVec3f") \
         .setValue("0.98 1 1.033") \
        ) \
        .addField(fieldObject() \
         .setName("cube") \
         .setAccessType("inputOutput") \
         .setType("SFInt32") \
         .setValue("0") \
        ) \
        .addField(fieldObject() \
         .setName("bias") \
         .setAccessType("inputOutput") \
         .setType("SFFloat") \
         .setValue("0.5") \
        ) \
        .addField(fieldObject() \
         .setName("scale") \
         .setAccessType("inputOutput") \
         .setType("SFFloat") \
         .setValue("0.5") \
        ) \
        .addField(fieldObject() \
         .setName("power") \
         .setAccessType("inputOutput") \
         .setType("SFFloat") \
         .setValue("2") \
        ) \
        .addParts(ShaderPartObject() \
         .setUrl(["../shaders/cobweb.vs","https://coderextreme.net/X3DJSONLD/shaders/cobweb.vs"]) \
         .setType("VERTEX") \
        ) \
        .addParts(ShaderPartObject() \
         .setUrl(["../shaders/mix.fs","https://coderextreme.net/X3DJSONLD/shaders/mix.fs"]) \
         .setType("FRAGMENT") \
        ) \
       ) \
       .addShaders(ComposedShaderObject(language = "GLSL") \
        .setDEF("x3dom") \
#http://hypertextbook.com/facts/2005/JustinChe.shtml
        .addField(fieldObject() \
         .setName("chromaticDispertion") \
         .setAccessType("inputOutput") \
         .setType("SFVec3f") \
         .setValue("0.98 1 1.033") \
        ) \
        .addField(fieldObject() \
         .setName("cube") \
         .setAccessType("inputOutput") \
         .setType("SFInt32") \
         .setValue("0") \
        ) \
        .addField(fieldObject() \
         .setName("bias") \
         .setAccessType("inputOutput") \
         .setType("SFFloat") \
         .setValue("0.5") \
        ) \
        .addField(fieldObject() \
         .setName("scale") \
         .setAccessType("inputOutput") \
         .setType("SFFloat") \
         .setValue("0.5") \
        ) \
        .addField(fieldObject() \
         .setName("power") \
         .setAccessType("inputOutput") \
         .setType("SFFloat") \
         .setValue("2") \
        ) \
        .addParts(ShaderPartObject() \
         .setUrl(["../shaders/x3dom.vs","https://coderextreme.net/X3DJSONLD/shaders/x3dom.vs"]) \
         .setType("VERTEX") \
        ) \
        .addParts(ShaderPartObject() \
         .setUrl(["../shaders/mix.fs","https://coderextreme.net/X3DJSONLD/shaders/mix.fs"]) \
         .setType("FRAGMENT") \
        ) \
       ) \
      ) \
      .setGeometry(SphereObject(radius = 30) \
      ) \
     ) \
     .addChildren(ScriptObject(directOutput = True) \
      .setDEF("UrlSelector") \
      .addField(fieldObject() \
       .setName("frontUrls") \
       .setType("MFString") \
       .setAccessType("initializeOnly") \
       .setValue("\"../resources/images/all_probes/beach_cross/beach_front.png\" \"../resources/images/all_probes/building_cross/building_front.png\" \"../resources/images/all_probes/campus_cross/campus_front.png\" \"../resources/images/all_probes/galileo_cross/galileo_front.png\" \"../resources/images/all_probes/grace_cross/grace_front.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_front.png\" \"../resources/images/all_probes/rnl_cross/rnl_front.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_front.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_front.png\"") \
      ) \
      .addField(fieldObject() \
       .setName("backUrls") \
       .setType("MFString") \
       .setAccessType("initializeOnly") \
       .setValue("\"../resources/images/all_probes/beach_cross/beach_back.png\" \"../resources/images/all_probes/building_cross/building_back.png\" \"../resources/images/all_probes/campus_cross/campus_back.png\" \"../resources/images/all_probes/galileo_cross/galileo_back.png\" \"../resources/images/all_probes/grace_cross/grace_back.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_back.png\" \"../resources/images/all_probes/rnl_cross/rnl_back.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_back.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_back.png\"") \
      ) \
      .addField(fieldObject() \
       .setName("leftUrls") \
       .setType("MFString") \
       .setAccessType("initializeOnly") \
       .setValue("\"../resources/images/all_probes/beach_cross/beach_left.png\" \"../resources/images/all_probes/building_cross/building_left.png\" \"../resources/images/all_probes/campus_cross/campus_left.png\" \"../resources/images/all_probes/galileo_cross/galileo_left.png\" \"../resources/images/all_probes/grace_cross/grace_left.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_left.png\" \"../resources/images/all_probes/rnl_cross/rnl_left.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_left.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_left.png\"") \
      ) \
      .addField(fieldObject() \
       .setName("rightUrls") \
       .setType("MFString") \
       .setAccessType("initializeOnly") \
       .setValue("\"../resources/images/all_probes/beach_cross/beach_right.png\" \"../resources/images/all_probes/building_cross/building_right.png\" \"../resources/images/all_probes/campus_cross/campus_right.png\" \"../resources/images/all_probes/galileo_cross/galileo_right.png\" \"../resources/images/all_probes/grace_cross/grace_right.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_right.png\" \"../resources/images/all_probes/rnl_cross/rnl_right.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_right.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_right.png\"") \
      ) \
      .addField(fieldObject() \
       .setName("topUrls") \
       .setType("MFString") \
       .setAccessType("initializeOnly") \
       .setValue("\"../resources/images/all_probes/beach_cross/beach_top.png\" \"../resources/images/all_probes/building_cross/building_top.png\" \"../resources/images/all_probes/campus_cross/campus_top.png\" \"../resources/images/all_probes/galileo_cross/galileo_top.png\" \"../resources/images/all_probes/grace_cross/grace_top.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_top.png\" \"../resources/images/all_probes/rnl_cross/rnl_top.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_top.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_top.png\"") \
      ) \
      .addField(fieldObject() \
       .setName("bottomUrls") \
       .setType("MFString") \
       .setAccessType("initializeOnly") \
       .setValue("\"../resources/images/all_probes/beach_cross/beach_bottom.png\" \"../resources/images/all_probes/building_cross/building_bottom.png\" \"../resources/images/all_probes/campus_cross/campus_bottom.png\" \"../resources/images/all_probes/galileo_cross/galileo_bottom.png\" \"../resources/images/all_probes/grace_cross/grace_bottom.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_bottom.png\" \"../resources/images/all_probes/rnl_cross/rnl_bottom.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_bottom.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_bottom.png\"") \
      ) \
      .addField(fieldObject() \
       .setName("front_changed") \
       .setType("MFString") \
       .setAccessType("outputOnly") \
      ) \
      .addField(fieldObject() \
       .setName("back_changed") \
       .setType("MFString") \
       .setAccessType("outputOnly") \
      ) \
      .addField(fieldObject() \
       .setName("left_changed") \
       .setType("MFString") \
       .setAccessType("outputOnly") \
      ) \
      .addField(fieldObject() \
       .setName("right_changed") \
       .setType("MFString") \
       .setAccessType("outputOnly") \
      ) \
      .addField(fieldObject() \
       .setName("top_changed") \
       .setType("MFString") \
       .setAccessType("outputOnly") \
      ) \
      .addField(fieldObject() \
       .setName("bottom_changed") \
       .setType("MFString") \
       .setAccessType("outputOnly") \
      ) \
      .addField(fieldObject() \
       .setName("set_fraction") \
       .setType("SFFloat") \
       .setAccessType("inputOnly") \
      ) \
      .addField(fieldObject() \
       .setName("old") \
       .setType("SFInt32") \
       .setAccessType("inputOutput") \
       .setValue("-1") \
      ) \
.setSourceCode('''ecmascript:\n"+
"        function set_fraction( f, tm ) {\n"+
"	    var side = Math.floor(f*frontUrls.length);\n"+
"	    if (side > frontUrls.length-1) {\n"+
"	    	side = 0;\n"+
"	    }\n"+
"	    if (side != old) {\n"+
"	    	    // Browser.print(f+\" \"+side);\n"+
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
     .addChildren(TimeSensorObject() \
      .setDEF("Clock") \
      .setCycleInterval(45) \
      .setLoop(True) \
     ) \
     .addChildren(ROUTEObject() \
      .setFromNode("Clock") \
      .setFromField("fraction_changed") \
      .setToNode("UrlSelector") \
      .setToField("set_fraction") \
     ) \
     .addChildren(ROUTEObject() \
      .setFromNode("UrlSelector") \
      .setFromField("front_changed") \
      .setToNode("cube") \
      .setToField("frontUrl") \
     ) \
     .addChildren(ROUTEObject() \
      .setFromNode("UrlSelector") \
      .setFromField("back_changed") \
      .setToNode("cube") \
      .setToField("backUrl") \
     ) \
     .addChildren(ROUTEObject() \
      .setFromNode("UrlSelector") \
      .setFromField("left_changed") \
      .setToNode("cube") \
      .setToField("leftUrl") \
     ) \
     .addChildren(ROUTEObject() \
      .setFromNode("UrlSelector") \
      .setFromField("right_changed") \
      .setToNode("cube") \
      .setToField("rightUrl") \
     ) \
     .addChildren(ROUTEObject() \
      .setFromNode("UrlSelector") \
      .setFromField("top_changed") \
      .setToNode("cube") \
      .setToField("topUrl") \
     ) \
     .addChildren(ROUTEObject() \
      .setFromNode("UrlSelector") \
      .setFromField("bottom_changed") \
      .setToNode("cube") \
      .setToField("bottomUrl") \
     ) \
     .addChildren(ROUTEObject() \
      .setFromNode("UrlSelector") \
      .setFromField("front_changed") \
      .setToNode("frontShader") \
      .setToField("url") \
     ) \
     .addChildren(ROUTEObject() \
      .setFromNode("UrlSelector") \
      .setFromField("back_changed") \
      .setToNode("backShader") \
      .setToField("url") \
     ) \
     .addChildren(ROUTEObject() \
      .setFromNode("UrlSelector") \
      .setFromField("left_changed") \
      .setToNode("leftShader") \
      .setToField("url") \
     ) \
     .addChildren(ROUTEObject() \
      .setFromNode("UrlSelector") \
      .setFromField("right_changed") \
      .setToNode("rightShader") \
      .setToField("url") \
     ) \
     .addChildren(ROUTEObject() \
      .setFromNode("UrlSelector") \
      .setFromField("top_changed") \
      .setToNode("topShader") \
      .setToField("url") \
     ) \
     .addChildren(ROUTEObject() \
      .setFromNode("UrlSelector") \
      .setFromField("bottom_changed") \
      .setToNode("bottomShader") \
      .setToField("url") \
     ) \
    ) \
   ) \

X3D0.toFileX3D("./future/./mirror2.newf.x3d")
