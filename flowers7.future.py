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
     .setContent("flowers7.x3d") \
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
     .setContent("https://coderextreme.net/X3DJSONLD/flowers7.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("description") \
     .setContent("a flower") \
    ) \
   ) \
   .setScene(SceneObject() \
    .addChildren(NavigationInfoObject() \
    ) \
#Images courtesy of Paul Debevec's Light Probe Image Gallery
    .addChildren(BackgroundObject() \
     .setDEF("background") \
     .setBackUrl(["../resources/images/all_probes/beach_cross/beach_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_back.png"]) \
     .setBottomUrl(["../resources/images/all_probes/beach_cross/beach_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_bottom.png"]) \
     .setFrontUrl(["../resources/images/all_probes/beach_cross/beach_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_front.png"]) \
     .setLeftUrl(["../resources/images/all_probes/beach_cross/beach_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_left.png"]) \
     .setRightUrl(["../resources/images/all_probes/beach_cross/beach_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_right.png"]) \
     .setTopUrl(["../resources/images/all_probes/beach_cross/beach_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_top.png"]) \
    ) \
    .addChildren(ViewpointObject() \
     .setPosition([0,0,40]) \
     .setDescription("Transparent rose") \
    ) \
    .addChildren(TransformObject() \
     .setDEF("Rose01") \
     .addChildren(ShapeObject() \
      .setAppearance(AppearanceObject() \
       .setMaterial(MaterialObject() \
        .setDiffuseColor([0.7,0.7,0.7]) \
        .setSpecularColor([0.5,0.5,0.5]) \
       ) \
       .setTexture(ComposedCubeMapTextureObject() \
        .setDEF("texture") \
        .setBack(ImageTextureObject() \
         .setDEF("backShader") \
         .setUrl(["../resources/images/all_probes/beach_cross/beach_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_back.png"]) \
        ) \
        .setBottom(ImageTextureObject() \
         .setDEF("bottomShader") \
         .setUrl(["../resources/images/all_probes/beach_cross/beach_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_bottom.png"]) \
        ) \
        .setFront(ImageTextureObject() \
         .setDEF("frontShader") \
         .setUrl(["../resources/images/all_probes/beach_cross/beach_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_front.png"]) \
        ) \
        .setLeft(ImageTextureObject() \
         .setDEF("leftShader") \
         .setUrl(["../resources/images/all_probes/beach_cross/beach_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_left.png"]) \
        ) \
        .setRight(ImageTextureObject() \
         .setDEF("rightShader") \
         .setUrl(["../resources/images/all_probes/beach_cross/beach_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_right.png"]) \
        ) \
        .setTop(ImageTextureObject() \
         .setDEF("topShader") \
         .setUrl(["../resources/images/all_probes/beach_cross/beach_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_top.png"]) \
        ) \
       ) \
       .addShaders(ComposedShaderObject(language = "GLSL") \
        .setDEF("x3dom") \
        .addField(fieldObject() \
         .setName("cube") \
         .setType("SFInt32") \
         .setAccessType("inputOutput") \
         .setValue("0") \
        ) \
        .addField(fieldObject() \
         .setName("chromaticDispertion") \
         .setAccessType("initializeOnly") \
         .setType("SFVec3f") \
         .setValue("0.98 1 1.033") \
        ) \
        .addField(fieldObject() \
         .setName("bias") \
         .setType("SFFloat") \
         .setAccessType("inputOutput") \
         .setValue("0.5") \
        ) \
        .addField(fieldObject() \
         .setName("scale") \
         .setType("SFFloat") \
         .setAccessType("inputOutput") \
         .setValue("0.5") \
        ) \
        .addField(fieldObject() \
         .setName("power") \
         .setType("SFFloat") \
         .setAccessType("inputOutput") \
         .setValue("2") \
        ) \
        .addField(fieldObject() \
         .setName("a") \
         .setType("SFFloat") \
         .setAccessType("inputOutput") \
         .setValue("10") \
        ) \
        .addField(fieldObject() \
         .setName("b") \
         .setType("SFFloat") \
         .setAccessType("inputOutput") \
         .setValue("1") \
        ) \
        .addField(fieldObject() \
         .setName("c") \
         .setType("SFFloat") \
         .setAccessType("inputOutput") \
         .setValue("20") \
        ) \
        .addField(fieldObject() \
         .setName("d") \
         .setType("SFFloat") \
         .setAccessType("inputOutput") \
         .setValue("20") \
        ) \
        .addField(fieldObject() \
         .setName("tdelta") \
         .setType("SFFloat") \
         .setAccessType("inputOutput") \
         .setValue("0") \
        ) \
        .addField(fieldObject() \
         .setName("pdelta") \
         .setType("SFFloat") \
         .setAccessType("inputOutput") \
         .setValue("0") \
        ) \
#field name='cube' type='SFNode' accessType=\"inputOutput\"> <ComposedCubeMapTexture USE=\"texture\"/> </field
        .addParts(ShaderPartObject() \
         .setUrl(["../shaders/x3dom_flowers_chromatic.vs","https://coderextreme.net/X3DJSONLD/shaders/x3dom_flowers_chromatic.vs"]) \
         .setType("VERTEX") \
        ) \
        .addParts(ShaderPartObject() \
         .setUrl(["../shaders/pc_bubbles.fs","https://coderextreme.net/X3DJSONLD/shaders/common.fs"]) \
         .setType("FRAGMENT") \
        ) \
       ) \
       .addShaders(ComposedShaderObject(language = "GLSL") \
        .setDEF("cobweb") \
        .addField(fieldObject() \
         .setName("cube") \
         .setType("SFNode") \
         .setAccessType("inputOutput") \
         .addChildren(ComposedCubeMapTextureObject() \
          .setUSE("texture") \
         ) \
        ) \
        .addField(fieldObject() \
         .setName("chromaticDispertion") \
         .setAccessType("initializeOnly") \
         .setType("SFVec3f") \
         .setValue("0.98 1 1.033") \
        ) \
        .addField(fieldObject() \
         .setName("bias") \
         .setType("SFFloat") \
         .setAccessType("inputOnly") \
         .setValue("0.5") \
        ) \
        .addField(fieldObject() \
         .setName("scale") \
         .setType("SFFloat") \
         .setAccessType("inputOnly") \
         .setValue("0.5") \
        ) \
        .addField(fieldObject() \
         .setName("power") \
         .setType("SFFloat") \
         .setAccessType("inputOnly") \
         .setValue("2") \
        ) \
        .addField(fieldObject() \
         .setName("a") \
         .setType("SFFloat") \
         .setAccessType("inputOnly") \
         .setValue("10") \
        ) \
        .addField(fieldObject() \
         .setName("b") \
         .setType("SFFloat") \
         .setAccessType("inputOnly") \
         .setValue("1") \
        ) \
        .addField(fieldObject() \
         .setName("c") \
         .setType("SFFloat") \
         .setAccessType("inputOnly") \
         .setValue("20") \
        ) \
        .addField(fieldObject() \
         .setName("d") \
         .setType("SFFloat") \
         .setAccessType("inputOnly") \
         .setValue("20") \
        ) \
        .addField(fieldObject() \
         .setName("tdelta") \
         .setType("SFFloat") \
         .setAccessType("inputOnly") \
         .setValue("0") \
        ) \
        .addField(fieldObject() \
         .setName("pdelta") \
         .setType("SFFloat") \
         .setAccessType("inputOnly") \
         .setValue("0") \
        ) \
        .addParts(ShaderPartObject() \
         .setUrl(["../shaders/cobweb_flowers_chromatic.vs","https://coderextreme.net/X3DJSONLD/shaders/cobweb_flowers_chromatic.vs"]) \
         .setType("VERTEX") \
        ) \
        .addParts(ShaderPartObject() \
         .setUrl(["../shaders/common.fs","https://coderextreme.net/X3DJSONLD/shaders/common.fs"]) \
         .setType("FRAGMENT") \
        ) \
       ) \
      ) \
      .setGeometry(SphereObject(solid = False) \
      ) \
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
      .setName("front") \
      .setType("MFString") \
      .setAccessType("inputOutput") \
     ) \
     .addField(fieldObject() \
      .setName("back") \
      .setType("MFString") \
      .setAccessType("inputOutput") \
     ) \
     .addField(fieldObject() \
      .setName("left") \
      .setType("MFString") \
      .setAccessType("inputOutput") \
     ) \
     .addField(fieldObject() \
      .setName("right") \
      .setType("MFString") \
      .setAccessType("inputOutput") \
     ) \
     .addField(fieldObject() \
      .setName("top") \
      .setType("MFString") \
      .setAccessType("inputOutput") \
     ) \
     .addField(fieldObject() \
      .setName("bottom") \
      .setType("MFString") \
      .setAccessType("inputOutput") \
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
"            var side = Math.floor(f*frontUrls.length);\n"+
"            if (side > frontUrls.length-1) {\n"+
"                side = 0;\n"+
"            }\n"+
"            if (side != old) {\n"+
"                    old = side;\n"+
"                    front[0] = frontUrls[side];\n"+
"                    back[0] = backUrls[side];\n"+
"                    left[0] = leftUrls[side];\n"+
"                    right[0] = rightUrls[side];\n"+
"                    top[0] = topUrls[side];\n"+
"                    bottom[0] = bottomUrls[side];\n"+
"            }\n"+
"        }''')
    ) \
#<TimeSensor DEF=\"Clock\" cycleInterval=\"45\" loop='true'/> <ROUTE fromNode='Clock' fromField='fraction_changed' toNode='UrlSelector' toField='set_fraction'/> <ROUTE fromNode='UrlSelector' fromField='front' toNode='background' toField='frontUrl'/> <ROUTE fromNode='UrlSelector' fromField='back' toNode='background' toField='backUrl'/> <ROUTE fromNode='UrlSelector' fromField='left' toNode='background' toField='leftUrl'/> <ROUTE fromNode='UrlSelector' fromField='right' toNode='background' toField='rightUrl'/> <ROUTE fromNode='UrlSelector' fromField='top' toNode='background' toField='topUrl'/> <ROUTE fromNode='UrlSelector' fromField='bottom' toNode='background' toField='bottomUrl'/> <ROUTE fromNode='UrlSelector' fromField='front' toNode='frontShader' toField='url'/> <ROUTE fromNode='UrlSelector' fromField='back' toNode='backShader' toField='url'/> <ROUTE fromNode='UrlSelector' fromField='left' toNode='leftShader' toField='url'/> <ROUTE fromNode='UrlSelector' fromField='right' toNode='rightShader' toField='url'/> <ROUTE fromNode='UrlSelector' fromField='top' toNode='topShader' toField='url'/> <ROUTE fromNode='UrlSelector' fromField='bottom' toNode='bottomShader' toField='url'/>
    .addChildren(ScriptObject(directOutput = True) \
     .setDEF("Animate") \
     .addField(fieldObject() \
      .setName("set_fraction") \
      .setType("SFFloat") \
      .setAccessType("inputOnly") \
     ) \
     .addField(fieldObject() \
      .setName("a") \
      .setType("SFFloat") \
      .setAccessType("inputOutput") \
      .setValue("10") \
     ) \
     .addField(fieldObject() \
      .setName("b") \
      .setType("SFFloat") \
      .setAccessType("inputOutput") \
      .setValue("1") \
     ) \
     .addField(fieldObject() \
      .setName("c") \
      .setType("SFFloat") \
      .setAccessType("inputOutput") \
      .setValue("20") \
     ) \
     .addField(fieldObject() \
      .setName("d") \
      .setType("SFFloat") \
      .setAccessType("inputOutput") \
      .setValue("20") \
     ) \
     .addField(fieldObject() \
      .setName("tdelta") \
      .setType("SFFloat") \
      .setAccessType("inputOutput") \
      .setValue("0") \
     ) \
     .addField(fieldObject() \
      .setName("pdelta") \
      .setType("SFFloat") \
      .setAccessType("inputOutput") \
      .setValue("0") \
     ) \
.setSourceCode('''ecmascript:\n"+
"\n"+
"function set_fraction() {\n"+
"	var choice = Math.floor(Math.random() * 4);\n"+
"	if (choice == 0) {\n"+
"		a = a + Math.floor(Math.random() * 2) * 2 - 1;\n"+
"	} else if (choice == 1) {\n"+
"		b = b + Math.floor(Math.random() * 2) * 2 - 1;\n"+
"	} else if (choice == 2) {\n"+
"		c = c + Math.floor(Math.random() * 2) * 2 - 1;\n"+
"	} else if (choice == 3) {\n"+
"		d = d + Math.floor(Math.random() * 2) * 2 - 1;\n"+
"	}\n"+
"	tdelta = tdelta + 0.5;\n"+
"	pdelta = pdelta + 0.5;\n"+
"	if (a < 1) {\n"+
"		a = 10;\n"+
"	}\n"+
"	if (b < 1) {\n"+
"		b = 10;\n"+
"	}\n"+
"	if (c < 1) {\n"+
"		c = 4;\n"+
"	}\n"+
"	if (c > 20) {\n"+
"		c = 4;\n"+
"	}\n"+
"	if (d < 1) {\n"+
"		d = 4;\n"+
"	}\n"+
"	if (d > 20) {\n"+
"		d = 4;\n"+
"	}\n"+
"}''')
    ) \
    .addChildren(TimeSensorObject() \
     .setDEF("TourTime") \
     .setCycleInterval(5) \
     .setLoop(True) \
    ) \
    .addChildren(ROUTEObject() \
     .setFromNode("TourTime") \
     .setFromField("fraction_changed") \
     .setToNode("Animate") \
     .setToField("set_fraction") \
    ) \
    .addChildren(ROUTEObject() \
     .setFromNode("Animate") \
     .setFromField("a") \
     .setToNode("cobweb") \
     .setToField("a") \
    ) \
    .addChildren(ROUTEObject() \
     .setFromNode("Animate") \
     .setFromField("b") \
     .setToNode("cobweb") \
     .setToField("b") \
    ) \
    .addChildren(ROUTEObject() \
     .setFromNode("Animate") \
     .setFromField("c") \
     .setToNode("cobweb") \
     .setToField("c") \
    ) \
    .addChildren(ROUTEObject() \
     .setFromNode("Animate") \
     .setFromField("d") \
     .setToNode("cobweb") \
     .setToField("d") \
    ) \
    .addChildren(ROUTEObject() \
     .setFromNode("Animate") \
     .setFromField("pdelta") \
     .setToNode("cobweb") \
     .setToField("pdelta") \
    ) \
    .addChildren(ROUTEObject() \
     .setFromNode("Animate") \
     .setFromField("tdelta") \
     .setToNode("cobweb") \
     .setToField("tdelta") \
    ) \
    .addChildren(ROUTEObject() \
     .setFromNode("Animate") \
     .setFromField("a") \
     .setToNode("x3dom") \
     .setToField("a") \
    ) \
    .addChildren(ROUTEObject() \
     .setFromNode("Animate") \
     .setFromField("b") \
     .setToNode("x3dom") \
     .setToField("b") \
    ) \
    .addChildren(ROUTEObject() \
     .setFromNode("Animate") \
     .setFromField("c") \
     .setToNode("x3dom") \
     .setToField("c") \
    ) \
    .addChildren(ROUTEObject() \
     .setFromNode("Animate") \
     .setFromField("d") \
     .setToNode("x3dom") \
     .setToField("d") \
    ) \
    .addChildren(ROUTEObject() \
     .setFromNode("Animate") \
     .setFromField("pdelta") \
     .setToNode("x3dom") \
     .setToField("pdelta") \
    ) \
    .addChildren(ROUTEObject() \
     .setFromNode("Animate") \
     .setFromField("tdelta") \
     .setToNode("x3dom") \
     .setToField("tdelta") \
    ) \
   ) \

X3D0.toFileX3D("./future/./flowers7.newf.x3d")
