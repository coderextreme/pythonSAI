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
    .addChildren(NavigationInfoObject() \
    ) \
    .addChildren(BackgroundObject() \
     .setBackUrl(["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"]) \
     .setBottomUrl(["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"]) \
     .setFrontUrl(["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"]) \
     .setLeftUrl(["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"]) \
     .setRightUrl(["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"]) \
     .setTopUrl(["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"]) \
    ) \
    .addChildren(ProtoDeclareObject() \
     .setName("flower") \
     .setProtoBody(ProtoBodyObject() \
      .addChildren(TransformObject() \
       .setDEF("transform") \
       .addChildren(ShapeObject() \
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
         .addShaders(ComposedShaderObject(language = "GLSL") \
          .addField(fieldObject() \
           .setName("xxxcube") \
           .setType("SFInt32") \
           .setAccessType("inputOutput") \
           .setValue("0") \
          ) \
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
           .setType("SFVec3f") \
           .setAccessType("inputOutput") \
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
          .addParts(ShaderPartObject() \
           .setUrl(["../shaders/common.vs","https://coderextreme.net/X3DJSONLD/shaders/common.vs"]) \
           .setType("VERTEX") \
          ) \
          .addParts(ShaderPartObject() \
           .setUrl(["../shaders/gl_flowers_chromatic.fs","https://coderextreme.net/X3DJSONLD/shaders/gl_flowers_chromatic.fs"]) \
           .setType("FRAGMENT") \
          ) \
         ) \
         .addShaders(ComposedShaderObject(language = "GLSL") \
          .addField(fieldObject() \
           .setName("xxxcube") \
           .setType("SFInt32") \
           .setAccessType("inputOutput") \
           .setValue("0") \
          ) \
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
           .setType("SFVec3f") \
           .setAccessType("inputOutput") \
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
          .addParts(ShaderPartObject() \
           .setUrl(["../shaders/x3dom.vs","https://coderextreme.net/X3DJSONLD/shaders/x3dom.vs"]) \
           .setType("VERTEX") \
          ) \
          .addParts(ShaderPartObject() \
           .setUrl(["../shaders/pc_bubbles.fs","https://coderextreme.net/X3DJSONLD/shaders/pc_bubbles.fs"]) \
           .setType("FRAGMENT") \
          ) \
         ) \
         .addShaders(ComposedShaderObject(language = "GLSL") \
          .setDEF("shader") \
          .addField(fieldObject() \
           .setName("xxxcube") \
           .setType("SFInt32") \
           .setAccessType("inputOutput") \
           .setValue("0") \
          ) \
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
           .setType("SFVec3f") \
           .setAccessType("inputOutput") \
           .setValue("0.98 1 1.033") \
          ) \
          .addField(fieldObject() \
           .setName("bias") \
           .setType("SFFloat") \
           .setAccessType("inputOutput") \
           .setValue("10") \
          ) \
          .addField(fieldObject() \
           .setName("scale") \
           .setType("SFFloat") \
           .setAccessType("inputOutput") \
           .setValue("10") \
          ) \
          .addField(fieldObject() \
           .setName("power") \
           .setType("SFFloat") \
           .setAccessType("inputOutput") \
           .setValue("2") \
          ) \
          .addParts(ShaderPartObject() \
           .setUrl(["../shaders/cobweb.vs","https://coderextreme.net/X3DJSONLD/shaders/cobweb.vs"]) \
           .setType("VERTEX") \
          ) \
          .addParts(ShaderPartObject() \
           .setUrl(["../shaders/pc_bubbles.fs","https://coderextreme.net/X3DJSONLD/shaders/pc_bubbles.fs"]) \
           .setType("FRAGMENT") \
          ) \
         ) \
        ) \
#<Sphere></Sphere>
        .setGeometry(IndexedFaceSetObject(convex = False) \
         .setDEF("Orbit") \
         .setCoord(CoordinateObject() \
          .setDEF("OrbitCoordinates") \
         ) \
        ) \
       ) \
      ) \
      .addChildren(ScriptObject() \
       .setDEF("Bounce") \
       .addField(fieldObject() \
        .setName("translation") \
        .setAccessType("inputOutput") \
        .setType("SFVec3f") \
        .setValue("0 0 0") \
       ) \
       .addField(fieldObject() \
        .setName("velocity") \
        .setAccessType("inputOutput") \
        .setType("SFVec3f") \
        .setValue("0 0 0") \
       ) \
       .addField(fieldObject() \
        .setName("set_fraction") \
        .setAccessType("inputOnly") \
        .setType("SFTime") \
       ) \
       .addField(fieldObject() \
        .setName("coordinates") \
        .setAccessType("inputOutput") \
        .setType("MFVec3f") \
       ) \
       .addField(fieldObject() \
        .setName("coordIndexes") \
        .setAccessType("outputOnly") \
        .setType("MFInt32") \
       ) \
       .addField(fieldObject() \
        .setName("a") \
        .setType("SFFloat") \
        .setAccessType("inputOutput") \
        .setValue("0.5") \
       ) \
       .addField(fieldObject() \
        .setName("b") \
        .setType("SFFloat") \
        .setAccessType("inputOutput") \
        .setValue("0.5") \
       ) \
       .addField(fieldObject() \
        .setName("c") \
        .setType("SFFloat") \
        .setAccessType("inputOutput") \
        .setValue("3") \
       ) \
       .addField(fieldObject() \
        .setName("d") \
        .setType("SFFloat") \
        .setAccessType("inputOutput") \
        .setValue("3") \
       ) \
       .addField(fieldObject() \
        .setName("tdelta") \
        .setType("SFFloat") \
        .setAccessType("inputOutput") \
        .setValue("0.5") \
       ) \
       .addField(fieldObject() \
        .setName("pdelta") \
        .setType("SFFloat") \
        .setAccessType("inputOutput") \
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
      .addChildren(TimeSensorObject() \
       .setDEF("TourTime") \
       .setCycleInterval(0.15) \
       .setLoop(True) \
      ) \
      .addChildren(TimeSensorObject() \
       .setDEF("SongTime") \
       .setLoop(True) \
      ) \
      .addChildren(SoundObject() \
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
      .addChildren(ROUTEObject() \
       .setFromField("cycleTime") \
       .setFromNode("SongTime") \
       .setToField("startTime") \
       .setToNode("AudioClip") \
      ) \
      .addChildren(ROUTEObject() \
       .setFromNode("TourTime") \
       .setFromField("cycleTime") \
       .setToNode("Bounce") \
       .setToField("set_fraction") \
      ) \
      .addChildren(ROUTEObject() \
       .setFromNode("Bounce") \
       .setFromField("translation") \
       .setToNode("transform") \
       .setToField("set_translation") \
      ) \
#<ROUTE fromField=\"coordIndexes\" fromNode=\"Bounce\" toField=\"set_coordIndex\" toNode=\"Orbit\"/> <ROUTE fromField=\"coordinates\" fromNode=\"Bounce\" toField=\"set_point\" toNode=\"OrbitCoordinates\"/>
     ) \
    ) \
    .addChildren(TransformObject() \
     .addChildren(ProtoInstanceObject() \
      .setName("flower") \
     ) \
#<ProtoInstance name=\"flower\"/> <ProtoInstance name=\"flower\"/>
    ) \
   ) \

X3D0.toFileX3D("./future/./flowers.newf.x3d")
