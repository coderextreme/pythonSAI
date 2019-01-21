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
     .setContent("flowers.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("creator") \
     .setContent("John Carlson") \
    ) \
    .addMeta(metaObject() \
     .setName("description") \
     .setContent("5 or more prismatic flowers") \
    ) \
    .addMeta(metaObject() \
     .setName("generator") \
     .setContent("X3D-Edit, https://savage.nps.edu/X3D-Edit") \
    ) \
    .addMeta(metaObject() \
     .setName("identifier") \
     .setContent("https://coderextreme.net/X3DJSONLD/flowers.x3d") \
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
    .addChild(ProtoDeclareObject() \
     .setName("flower") \
     .setProtoBody(ProtoBodyObject() \
      .addChild(TransformObject() \
       .setDEF("transform") \
       .addChild(ShapeObject() \
        .setAppearance(AppearanceObject() \
         .setMaterial(MaterialObject() \
          .setDiffuseColor([0.7,0.7,0.7]) \
          .setSpecularColor([0.5,0.5,0.5]) \
         ) \
         .setTexture(ComposedCubeMapTextureObject() \
          .setDEF("texture") \
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
          .setLanguage("GLSL") \
          .addField(fieldObject() \
           .setType(fieldObject.TYPE_SFINT32) \
           .setName("xxxcube") \
           .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
           .setValue("0") \
          ) \
          .addField(fieldObject() \
           .setType(fieldObject.TYPE_SFNODE) \
           .setName("cube") \
           .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
           .addChild(ComposedCubeMapTextureObject() \
            .setUSE("texture") \
           ) \
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
           .setUrl(["../shaders/common.vs","https://coderextreme.net/X3DJSONLD/shaders/common.vs"]) \
          ) \
          .addParts(ShaderPartObject() \
           .setType("FRAGMENT") \
           .setUrl(["../shaders/gl_flowers_chromatic.fs","https://coderextreme.net/X3DJSONLD/shaders/gl_flowers_chromatic.fs"]) \
          ) \
         ) \
         .addShaders(ComposedShaderObject() \
          .setLanguage("GLSL") \
          .addField(fieldObject() \
           .setType(fieldObject.TYPE_SFINT32) \
           .setName("xxxcube") \
           .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
           .setValue("0") \
          ) \
          .addField(fieldObject() \
           .setType(fieldObject.TYPE_SFNODE) \
           .setName("cube") \
           .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
           .addChild(ComposedCubeMapTextureObject() \
            .setUSE("texture") \
           ) \
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
         .addShaders(ComposedShaderObject() \
          .setDEF("shader") \
          .setLanguage("GLSL") \
          .addField(fieldObject() \
           .setType(fieldObject.TYPE_SFINT32) \
           .setName("xxxcube") \
           .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
           .setValue("0") \
          ) \
          .addField(fieldObject() \
           .setType(fieldObject.TYPE_SFNODE) \
           .setName("cube") \
           .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
           .addChild(ComposedCubeMapTextureObject() \
            .setUSE("texture") \
           ) \
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
           .setValue("10") \
          ) \
          .addField(fieldObject() \
           .setType(fieldObject.TYPE_SFFLOAT) \
           .setName("scale") \
           .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
           .setValue("10") \
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
           .setUrl(["../shaders/pc_bubbles.fs","https://coderextreme.net/X3DJSONLD/shaders/pc_bubbles.fs"]) \
          ) \
         ) \
        ) \
        .addComments(CommentsBlock("""<Sphere></Sphere>""")) \
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
       .setDEF("Bounce") \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFVEC3F) \
        .setName("translation") \
        .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
        .setValue("0 0 0") \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFVEC3F) \
        .setName("velocity") \
        .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
        .setValue("0 0 0") \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFTIME) \
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
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFFLOAT) \
        .setName("a") \
        .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
        .setValue("0.5") \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFFLOAT) \
        .setName("b") \
        .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
        .setValue("0.5") \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFFLOAT) \
        .setName("c") \
        .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
        .setValue("3") \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFFLOAT) \
        .setName("d") \
        .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
        .setValue("3") \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFFLOAT) \
        .setName("tdelta") \
        .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
        .setValue("0.5") \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFFLOAT) \
        .setName("pdelta") \
        .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
        .setValue("0.5") \
       ) \
       .setSourceCode('''ecmascript:\n"+
"			function newBubble() {\n"+
"			    translation = new SFVec3f(0, 0, 0);\n"+
"			    velocity = new SFVec3f(\n"+
"			    	Math.random() - 0.5,\n"+
"				Math.random() - 0.5,\n"+
"				Math.random() - 0.5);\n"+
"			}\n"+
"			function set_fraction() {\n"+
"			    translation = new SFVec3f(\n"+
"			    	translation.x + velocity.x,\n"+
"				translation.y + velocity.y,\n"+
"				translation.z + velocity.z);\n"+
"			    if (Math.abs(translation.x) > 10) {\n"+
"					newBubble();\n"+
"			    } else if (Math.abs(translation.y) > 10) {\n"+
"					newBubble();\n"+
"			    } else if (Math.abs(translation.z) > 10) {\n"+
"					newBubble();\n"+
"			    } else {\n"+
"					velocity = new SFVec3f(\n"+
"						velocity.x + Math.random() * 0.2 - 0.1,\n"+
"						velocity.y + Math.random() * 0.2 - 0.1,\n"+
"						velocity.z + Math.random() * 0.2 - 0.1\n"+
"					);\n"+
"			    }\n"+
"			    animate_flowers();\n"+
"			}\n"+
"\n"+
"			function initialize() {\n"+
"			     var cis = [];\n"+
"			     newBubble();\n"+
"			     resolution = 100;\n"+
"			     updateCoordinates(resolution);\n"+
"			     for ( i = 0; i < resolution-1; i++) {\n"+
"				for ( j = 0; j < resolution-1; j++) {\n"+
"				     cis.push(i*resolution+j);\n"+
"				     cis.push(i*resolution+j+1);\n"+
"				     cis.push((i+1)*resolution+j+1);\n"+
"				     cis.push((i+1)*resolution+j);\n"+
"				     cis.push(-1);\n"+
"				}\n"+
"			    }\n"+
"			     coordIndexes = new MFInt32(cis);\n"+
"			}\n"+
"\n"+
"			function updateCoordinates(resolution) {\n"+
"			     theta = 0.0;\n"+
"			     phi = 0.0;\n"+
"			     delta = (2 * 3.141592653) / (resolution-1);\n"+
"			     var crds = [];\n"+
"			     for ( i = 0; i < resolution; i++) {\n"+
"				for ( j = 0; j < resolution; j++) {\n"+
"					rho = a + b * Math.cos(c * theta) * Math.cos(d * phi);\n"+
"					crds.push(new SFVec3f(\n"+
"						rho * Math.cos(phi) * Math.cos(theta),\n"+
"						rho * Math.cos(phi) * Math.sin(theta),\n"+
"						rho * Math.sin(phi)\n"+
"					));\n"+
"					theta += delta;\n"+
"				}\n"+
"				phi += delta;\n"+
"				coordinates = new MFVec3f(crds);\n"+
"			     }\n"+
"			}\n"+
"\n"+
"			function animate_flowers(fraction, eventTime) {\n"+
"				choice = Math.floor(Math.random() * 4);\n"+
"				switch (choice) {\n"+
"				case 0:\n"+
"					a += Math.random() * 0.2 - 0.1;\n"+
"					break;\n"+
"				case 1:\n"+
"					b += Math.random() * 0.2 - 0.1;\n"+
"					break;\n"+
"				case 2:\n"+
"					c += Math.random() * 2 - 1;\n"+
"					break;\n"+
"				case 3:\n"+
"					d += Math.random() * 2 - 1;\n"+
"					break;\n"+
"				}\n"+
"				if (a > 1) {\n"+
"					a =  0.5;\n"+
"				}\n"+
"				if (b > 1) {\n"+
"					b =  0.5;\n"+
"				}\n"+
"				if (c < 1) {\n"+
"					c =  4;\n"+
"				}\n"+
"				if (d < 1) {\n"+
"					d =  4;\n"+
"				}\n"+
"				if (c > 10) {\n"+
"					c = 4;\n"+
"				}\n"+
"				if (d > 10) {\n"+
"					d = 4;\n"+
"				}\n"+
"				resolution = 100;\n"+
"				updateCoordinates(resolution);\n"+
"			}''')
      ) \
      .addChild(TimeSensorObject() \
       .setDEF("TourTime") \
       .setCycleInterval(0.15) \
       .setLoop(True) \
      ) \
      .addChild(TimeSensorObject() \
       .setDEF("SongTime") \
       .setLoop(True) \
      ) \
      .addChild(SoundObject() \
       .setMaxBack(100) \
       .setMaxFront(100) \
       .setMinBack(20) \
       .setMinFront(20) \
       .setSource(AudioClipObject() \
        .setDEF("AudioClip") \
        .setDescription("Chandubabamusic #1") \
        .setUrl(["../resources/chandubabamusic1.wav"]) \
       ) \
      ) \
      .addChild(ROUTEObject() \
       .setFromField("cycleTime") \
       .setFromNode("SongTime") \
       .setToField("startTime") \
       .setToNode("AudioClip") \
      ) \
      .addChild(ROUTEObject() \
       .setFromNode("TourTime") \
       .setFromField("cycleTime") \
       .setToNode("Bounce") \
       .setToField("set_fraction") \
      ) \
      .addChild(ROUTEObject() \
       .setFromNode("Bounce") \
       .setFromField("translation") \
       .setToNode("transform") \
       .setToField("set_translation") \
      ) \
      .addComments(CommentsBlock("""<ROUTE fromField=\"coordIndexes\" fromNode=\"Bounce\" toField=\"set_coordIndex\" toNode=\"Orbit\"/> <ROUTE fromField=\"coordinates\" fromNode=\"Bounce\" toField=\"set_point\" toNode=\"OrbitCoordinates\"/>""")) \
     ) \
    ) \
    .addChild(TransformObject() \
     .addChild(ProtoInstanceObject() \
      .setName("flower") \
     ) \
     .addComments(CommentsBlock("""<ProtoInstance name=\"flower\"/> <ProtoInstance name=\"flower\"/>""")) \
    ) \
   ) \

X3D0.toFileX3D("./future/./flowers.newf.x3d")
