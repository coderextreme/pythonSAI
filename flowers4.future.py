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
     .setContent("flowers4.x3d") \
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
     .setContent("https://coderextreme.net/X3DJSONLD/flowers4.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("description") \
     .setContent("an animated flower") \
    ) \
   ) \
   .setScene(SceneObject() \
    .addChild(NavigationInfoObject() \
    ) \
    .addChild(BackgroundObject() \
     .setBackUrl(["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"]) \
     .setBottomUrl(["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"]) \
     .setFrontUrl(["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"]) \
     .setLeftUrl(["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"]) \
     .setRightUrl(["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"]) \
     .setTopUrl(["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"]) \
    ) \
    .addChild(TransformObject() \
     .setDEF("transform") \
     .addChild(ShapeObject() \
      .setAppearance(AppearanceObject() \
       .setMaterial(MaterialObject() \
        .setDiffuseColor([0.7,0.7,0.7]) \
        .setSpecularColor([0.5,0.5,0.5]) \
       ) \
       .setTexture(ComposedCubeMapTextureObject() \
        .setBack(ImageTextureObject() \
         .setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"]) \
        ) \
        .setBottom(ImageTextureObject() \
         .setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"]) \
        ) \
        .setFront(ImageTextureObject() \
         .setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"]) \
        ) \
        .setLeft(ImageTextureObject() \
         .setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"]) \
        ) \
        .setRight(ImageTextureObject() \
         .setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"]) \
        ) \
        .setTop(ImageTextureObject() \
         .setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"]) \
        ) \
       ) \
       .addShaders(ComposedShaderObject() \
        .setDEF("shader") \
        .setLanguage("GLSL") \
        .addField(fieldObject() \
         .setType(fieldObject.TYPE_SFINT32) \
         .setName("cube") \
         .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
         .setValue("0") \
        ) \
        .addField(fieldObject() \
         .setType(fieldObject.TYPE_SFVEC3F) \
         .setName("chromaticDispertion") \
         .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
         .setValue("0.98 1 1.033") \
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
         .setUrl(["../shaders/pc_bubbles.fs","https://coderextreme.net/X3DJSONLD/shaders/pc_bubbles.fs"]) \
        ) \
       ) \
      ) \
      .addComments(CommentsBlock("""<Sphere>""")) \
      .setGeometry(IndexedFaceSetObject() \
       .setConvex(False) \
       .setDEF("Orbit") \
       .setCoord(CoordinateObject() \
        .setDEF("OrbitCoordinates") \
       ) \
      ) \
     ) \
    ) \
    .addChild(ScriptObject() \
     .setDEF("OrbitScript") \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFFLOAT) \
      .setName("set_fraction") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTONLY) \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_MFVEC3F) \
      .setName("coordinates") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_MFINT32) \
      .setName("coordIndexes") \
      .setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY) \
     ) \
     .setSourceCode('''ecmascript:\n"+
"\n"+
"var e = 5;\n"+
"var f = 5;\n"+
"var g = 5;\n"+
"var h = 5;\n"+
"\n"+
"function initialize() {\n"+
"     resolution = 100;\n"+
"     updateCoordinates(resolution);\n"+
"     var cis = [];\n"+
"     for ( i = 0; i < resolution-1; i++) {\n"+
"     	for ( j = 0; j < resolution-1; j++) {\n"+
"	     cis.push(i*resolution+j);\n"+
"	     cis.push(i*resolution+j+1);\n"+
"	     cis.push((i+1)*resolution+j+1);\n"+
"	     cis.push((i+1)*resolution+j);\n"+
"	     cis.push(-1);\n"+
"	}\n"+
"    }\n"+
"    coordIndexes = new MFInt32(cis);\n"+
"}\n"+
"\n"+
"function updateCoordinates(resolution) {\n"+
"     theta = 0.0;\n"+
"     phi = 0.0;\n"+
"     delta = (2 * 3.141592653) / (resolution-1);\n"+
"     var crds = [];\n"+
"     for ( i = 0; i < resolution; i++) {\n"+
"     	for ( j = 0; j < resolution; j++) {\n"+
"		rho = e + f * Math.cos(g * theta) * Math.cos(h * phi);\n"+
"		crds.push(new SFVec3f(\n"+
"			rho * Math.cos(phi) * Math.cos(theta),\n"+
"			rho * Math.cos(phi) * Math.sin(theta),\n"+
"			rho * Math.sin(phi)\n"+
"		));\n"+
"		theta += delta;\n"+
"	}\n"+
"	phi += delta;\n"+
"     }\n"+
"     coordinates = new MFVec3f(crds);\n"+
"}\n"+
"\n"+
"function set_fraction(fraction, eventTime) {\n"+
"	choice = Math.floor(Math.random() * 4);\n"+
"	switch (choice) {\n"+
"	case 0:\n"+
"		e += Math.floor(Math.random() * 2) * 2 - 1;\n"+
"		break;\n"+
"	case 1:\n"+
"		f += Math.floor(Math.random() * 2) * 2 - 1;\n"+
"		break;\n"+
"	case 2:\n"+
"		g += Math.floor(Math.random() * 2) * 2 - 1;\n"+
"		break;\n"+
"	case 3:\n"+
"		h += Math.floor(Math.random() * 2) * 2 - 1;\n"+
"		break;\n"+
"	}\n"+
"	if (f < 1) {\n"+
"		f = 10;\n"+
"	}\n"+
"	if (g < 1) {\n"+
"		g = 4;\n"+
"	}\n"+
"	if (h < 1) {\n"+
"		h = 4;\n"+
"	}\n"+
"	resolution = 100;\n"+
"	updateCoordinates(resolution);\n"+
"}''')
    ) \
    .addChild(TimeSensorObject() \
     .setDEF("Clock") \
     .setCycleInterval(16) \
     .setLoop(True) \
    ) \
    .addChild(ROUTEObject() \
     .setFromField("coordIndexes") \
     .setFromNode("OrbitScript") \
     .setToField("set_coordIndex") \
     .setToNode("Orbit") \
    ) \
    .addChild(ROUTEObject() \
     .setFromField("coordinates") \
     .setFromNode("OrbitScript") \
     .setToField("set_point") \
     .setToNode("OrbitCoordinates") \
    ) \
    .addChild(ROUTEObject() \
     .setFromField("fraction_changed") \
     .setFromNode("Clock") \
     .setToField("set_fraction") \
     .setToNode("OrbitScript") \
    ) \
   ) \

X3D0.toFileX3D("./future/./flowers4.newf.x3d")
