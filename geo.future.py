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
     .setContent("geo.x3d") \
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
     .setContent("https://coderextreme.net/X3DJSONLD/geo.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("description") \
     .setContent("a sphere") \
    ) \
   ) \
   .setScene(SceneObject() \
    .addChild(NavigationInfoObject() \
     .setType(["ANY","EXAMINE","FLY","LOOKAT"]) \
    ) \
    .addChild(ViewpointObject() \
     .setDEF("Tour") \
     .setDescription("Tour Views") \
    ) \
.addComments(CommentsBlock("""Viewpoint position='0 0 4' description='sphere in road'/""")) \
    .addChild(BackgroundObject() \
     .setBackUrl(["resources/images/bBK.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bBK.png"]) \
     .setBottomUrl(["resources/images/bBT.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bBT.png"]) \
     .setFrontUrl(["resources/images/bFR.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bFR.png"]) \
     .setLeftUrl(["resources/images/bLF.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bLF.png"]) \
     .setRightUrl(["resources/images/bRT.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bRT.png"]) \
     .setTopUrl(["resources/images/bTP.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bTP.png"]) \
    ) \
    .addChild(TransformObject() \
     .addChild(ShapeObject() \
      .setGeometry(SphereObject() \
      ) \
      .setAppearance(AppearanceObject() \
       .setMaterial(MaterialObject() \
        .setDiffuseColor([0.7,0.7,0.7]) \
        .setSpecularColor([0.5,0.5,0.5]) \
       ) \
       .setTexture(ComposedCubeMapTextureObject() \
        .setDEF("texture") \
        .setBack(ImageTextureObject() \
         .setUrl(["resources/images/bBK.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bBK.png"]) \
        ) \
        .setBottom(ImageTextureObject() \
         .setUrl(["resources/images/bBT.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bBT.png"]) \
        ) \
        .setFront(ImageTextureObject() \
         .setUrl(["resources/images/bFR.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bFR.png"]) \
        ) \
        .setLeft(ImageTextureObject() \
         .setUrl(["resources/images/bLF.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bLF.png"]) \
        ) \
        .setRight(ImageTextureObject() \
         .setUrl(["resources/images/bRT.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bRT.png"]) \
        ) \
        .setTop(ImageTextureObject() \
         .setUrl(["resources/images/bTP.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bTP.png"]) \
        ) \
       ) \
       .addShaders(ComposedShaderObject() \
        .setLanguage("GLSL") \
        .addField(fieldObject() \
         .setType(fieldObject.TYPE_SFVEC3F) \
         .setName("chromaticDispertion") \
         .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
         .setValue("0.98 1 1.033") \
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
         .setDEF("common") \
         .setUrl(["../shaders/common.fs","https://coderextreme.net/X3DJSONLD/shaders/common.fs"]) \
        ) \
       ) \
       .addShaders(ComposedShaderObject() \
        .setLanguage("GLSL") \
        .addField(fieldObject() \
         .setType(fieldObject.TYPE_SFVEC3F) \
         .setName("chromaticDispertion") \
         .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
         .setValue("0.98 1 1.033") \
        ) \
        .addField(fieldObject() \
         .setType(fieldObject.TYPE_SFNODE) \
         .setName("cube") \
         .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
         .addChild(ComposedCubeMapTextureObject() \
          .setUSE("texture") \
         ) \
        ) \
        .addField(fieldObject() \
         .setType(fieldObject.TYPE_SFFLOAT) \
         .setName("bias") \
         .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
         .setValue("0.5") \
        ) \
        .addField(fieldObject() \
         .setType(fieldObject.TYPE_SFFLOAT) \
         .setName("scale") \
         .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
         .setValue("0.5") \
        ) \
        .addField(fieldObject() \
         .setType(fieldObject.TYPE_SFFLOAT) \
         .setName("power") \
         .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
         .setValue("2") \
        ) \
        .addParts(ShaderPartObject() \
         .setType("VERTEX") \
         .setUrl(["../shaders/cobweb.vs","https://coderextreme.net/X3DJSONLD/shaders/cobweb.vs"]) \
        ) \
        .addParts(ShaderPartObject() \
         .setUSE("common") \
        ) \
       ) \
      ) \
     ) \
    ) \
   ) \

X3D0.toFileX3D("./future/./geo.newf.x3d")