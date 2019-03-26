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
     .setContent("flowerproto.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("creator") \
     .setContent("John Carlson") \
    ) \
    .addMeta(metaObject() \
     .setName("description") \
     .setContent("A flower proto with configurable shaders") \
    ) \
    .addMeta(metaObject() \
     .setName("generator") \
     .setContent("X3D-Edit, https://savage.nps.edu/X3D-Edit") \
    ) \
    .addMeta(metaObject() \
     .setName("identifier") \
     .setContent("https://coderextreme.net/X3DJSONLD/flowerproto.x3d") \
    ) \
   ) \
   .setScene(SceneObject() \
    .addChildren(ProtoDeclareObject() \
     .setName("FlowerProto") \
     .setProtoInterface(ProtoInterfaceObject() \
      .addField(fieldObject() \
       .setName("vertex") \
       .setAccessType("inputOutput") \
       .setType("MFString") \
       .setValue("\"../shaders/gl_flowers_chromatic.vs\"") \
      ) \
      .addField(fieldObject() \
       .setName("fragment") \
       .setAccessType("inputOutput") \
       .setType("MFString") \
       .setValue("\"../shaders/pc_flowers.fs\"") \
      ) \
     ) \
     .setProtoBody(ProtoBodyObject() \
      .addChildren(TransformObject() \
       .setDEF("transform") \
       .addChildren(ShapeObject() \
        .setAppearance(AppearanceObject() \
         .setMaterial(MaterialObject() \
          .setDiffuseColor([0.7,0.7,0.7]) \
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
          .setDEF("shader") \
          .addField(fieldObject() \
           .setName("cube") \
           .setType("SFInt32") \
           .setAccessType("inputOutput") \
           .setValue("0") \
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
          .addField(fieldObject() \
           .setName("a") \
           .setType("SFFloat") \
           .setAccessType("inputOutput") \
           .setValue("3") \
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
#<field name='cube' type='SFNode' accessType=\"inputOutput\"> <ComposedCubeMapTexture USE=\"texture\"/> </field>
          .addParts(ShaderPartObject() \
           .setType("VERTEX") \
           .setIS(ISObject() \
            .addConnect(connectObject() \
             .setNodeField("url") \
             .setProtoField("vertex") \
            ) \
           ) \
          ) \
          .addParts(ShaderPartObject() \
           .setType("FRAGMENT") \
           .setIS(ISObject() \
            .addConnect(connectObject() \
             .setNodeField("url") \
             .setProtoField("fragment") \
            ) \
           ) \
          ) \
         ) \
        ) \
        .setGeometry(SphereObject() \
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
"			function initialize() {\n"+
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
"			    for (var j = 0; j <= 2; j++) {\n"+
"				    if (Math.abs(translation.x) > 10) {\n"+
"					initialize();\n"+
"				    } else if (Math.abs(translation.y) > 10) {\n"+
"					initialize();\n"+
"				    } else if (Math.abs(translation.z) > 10) {\n"+
"					initialize();\n"+
"				    } else {\n"+
"					velocity.x += Math.random() * 0.2 - 0.1;\n"+
"					velocity.y += Math.random() * 0.2 - 0.1;\n"+
"					velocity.z += Math.random() * 0.2 - 0.1;\n"+
"				    }\n"+
"			    }\n"+
"			    animate_flowers();\n"+
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
"				tdelta += 0.5;\n"+
"				pdelta += 0.5;\n"+
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
"			}''')
       ) \
       .addChildren(TimeSensorObject() \
        .setDEF("TourTime") \
        .setCycleInterval(0.15) \
        .setLoop(True) \
       ) \
       .addChildren(ROUTEObject() \
        .setFromNode("TourTime") \
        .setFromField("cycleTime") \
        .setToNode("Bounce") \
        .setToField("set_fraction") \
       ) \
       .addChildren(ROUTEObject() \
        .setFromNode("Bounce") \
        .setFromField("translation_changed") \
        .setToNode("transform") \
        .setToField("set_translation") \
       ) \
       .addChildren(ROUTEObject() \
        .setFromNode("Bounce") \
        .setFromField("a") \
        .setToNode("shader") \
        .setToField("a") \
       ) \
       .addChildren(ROUTEObject() \
        .setFromNode("Bounce") \
        .setFromField("b") \
        .setToNode("shader") \
        .setToField("b") \
       ) \
       .addChildren(ROUTEObject() \
        .setFromNode("Bounce") \
        .setFromField("c") \
        .setToNode("shader") \
        .setToField("c") \
       ) \
       .addChildren(ROUTEObject() \
        .setFromNode("Bounce") \
        .setFromField("d") \
        .setToNode("shader") \
        .setToField("d") \
       ) \
       .addChildren(ROUTEObject() \
        .setFromNode("Bounce") \
        .setFromField("tdelta") \
        .setToNode("shader") \
        .setToField("tdelta") \
       ) \
       .addChildren(ROUTEObject() \
        .setFromNode("Bounce") \
        .setFromField("pdelta") \
        .setToNode("shader") \
        .setToField("pdelta") \
       ) \
      ) \
     ) \
    ) \
   ) \

X3D0.toFileX3D("./future/./flowerproto.newf.x3d")
