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
     .setContent("bub.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("creator") \
     .setContent("John Carlson") \
    ) \
    .addMeta(metaObject() \
     .setName("description") \
     .setContent("3 prismatic spheres") \
    ) \
    .addMeta(metaObject() \
     .setName("generator") \
     .setContent("X3D-Edit, https://savage.nps.edu/X3D-Edit") \
    ) \
    .addMeta(metaObject() \
     .setName("identifier") \
     .setContent("https://coderextreme.net/X3DJSONLD/bub.x3d") \
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
    .addChild(ViewpointObject() \
     .setPosition([0,0,20]) \
     .setDescription("Look at the bubbles flying") \
    ) \
    .addChild(ProtoDeclareObject() \
     .setName("Bubble") \
     .setProtoBody(ProtoBodyObject() \
      .addChild(TransformObject() \
       .setDEF("transform") \
       .addChild(ShapeObject() \
        .setDEF("myShape") \
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
         .addComments(CommentsBlock("""<ComposedShader DEF='gl' language=\"GLSL\"> <field name='cube' type='SFInt32' accessType=\"inputOutput\" value='0'/> <field name='chromaticDispertion' type='SFVec3f' accessType=\"inputOutput\" value='0.98 1.0 1.033'/> <field name='bias' type='SFFloat' accessType=\"inputOutput\" value='0.5'/> <field name='scale' type='SFFloat' accessType=\"inputOutput\" value='0.5'/> <field name='power' type='SFFloat' accessType=\"inputOutput\" value='2.0'/> <ShaderPart url='\"../shaders/gl.vs\" \"https://coderextreme.net/X3DJSONLD/shaders/gl.vs\"' type='VERTEX'></ShaderPart> <ShaderPart url='\"../shaders/pc_bubbles.fs\" \"https://coderextreme.net/X3DJSONLD/shaders/pc_bubbles.fs\"' type='FRAGMENT'></ShaderPart> </ComposedShader> <ComposedShader DEF='freewrl' language=\"GLSL\"> <field name='fw_textureCoodGenType' type='SFInt32' accessType=\"inputOutput\" value='0'/> <field name='chromaticDispertion' type='SFVec3f' accessType=\"inputOutput\" value='0.98 1.0 1.033'/> <field name='bias' type='SFFloat' accessType=\"inputOutput\" value='0.5'/> <field name='scale' type='SFFloat' accessType=\"inputOutput\" value='0.5'/> <field name='power' type='SFFloat' accessType=\"inputOutput\" value='2.0'/> <ShaderPart url='\"../shaders/freewrl.vs\" \"https://coderextreme.net/X3DJSONLD/shaders/freewrl.vs\"' type='VERTEX'></ShaderPart> <ShaderPart url='\"../shaders/pc_bubbles.fs\" \"https://coderextreme.net/X3DJSONLD/shaders/pc_bubbles.fs\"' type='FRAGMENT'></ShaderPart> </ComposedShader>""")) \
         .addComments(CommentsBlock("""<ComposedShader DEF='instant' language=\"GLSL\"> <field name='cube' type='SFInt32' accessType=\"inputOutput\" value='0'/> <field name='chromaticDispertion' type='SFVec3f' accessType=\"inputOutput\" value='0.98 1.0 1.033'/> <field name='bias' type='SFFloat' accessType=\"inputOutput\" value='0.5'/> <field name='scale' type='SFFloat' accessType=\"inputOutput\" value='0.5'/> <field name='power' type='SFFloat' accessType=\"inputOutput\" value='2.0'/> <ShaderPart url='\"../shaders/instant.vs\" \"https://coderextreme.net/X3DJSONLD/shaders/instant.vs\"' type='VERTEX'></ShaderPart> <ShaderPart url='\"../shaders/pc_bubbles.fs\" \"https://coderextreme.net/X3DJSONLD/shaders/pc_bubbles.fs\"' type='FRAGMENT'></ShaderPart> </ComposedShader>""")) \
         .addShaders(ComposedShaderObject() \
          .setDEF("x3dom") \
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
         .addShaders(ComposedShaderObject() \
          .setDEF("cobweb") \
          .setLanguage("GLSL") \
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
           .setUrl(["../shaders/cobweb.vs","https://coderextreme.net/X3DJSONLD/shaders/cobweb.vs"]) \
          ) \
          .addParts(ShaderPartObject() \
           .setType("FRAGMENT") \
           .setUrl(["../shaders/pc_bubbles.fs","https://coderextreme.net/X3DJSONLD/shaders/pc.fs"]) \
          ) \
         ) \
        ) \
        .setGeometry(SphereObject() \
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
"			    if (Math.abs(translation.x) > 10) {\n"+
"				initialize();\n"+
"			    } else if (Math.abs(translation.y) > 10) {\n"+
"				initialize();\n"+
"			    } else if (Math.abs(translation.z) > 10) {\n"+
"				initialize();\n"+
"			    } else {\n"+
"				velocity.x += Math.random() * 0.2 - 0.1;\n"+
"				velocity.y += Math.random() * 0.2 - 0.1;\n"+
"				velocity.z += Math.random() * 0.2 - 0.1;\n"+
"			    }\n"+
"			}''')
      ) \
      .addChild(TimeSensorObject() \
       .setDEF("TourTime") \
       .setCycleInterval(0.15) \
       .setLoop(True) \
      ) \
      .addChild(ROUTEObject() \
       .setFromNode("TourTime") \
       .setFromField("cycleTime") \
       .setToNode("Bounce") \
       .setToField("set_fraction") \
      ) \
      .addChild(ROUTEObject() \
       .setFromNode("Bounce") \
       .setFromField("translation_changed") \
       .setToNode("transform") \
       .setToField("set_translation") \
      ) \
     ) \
    ) \
    .addChild(ProtoInstanceObject() \
     .setName("Bubble") \
    ) \
    .addChild(ProtoInstanceObject() \
     .setName("Bubble") \
    ) \
    .addChild(ProtoInstanceObject() \
     .setName("Bubble") \
    ) \
   ) \

X3D0.toFileX3D("./future/./bub.newf.x3d")
