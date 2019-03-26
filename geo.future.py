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
    .addChildren(NavigationInfoObject() \
     .setType(["ANY","EXAMINE","FLY","LOOKAT"]) \
    ) \
    .addChildren(ViewpointObject() \
     .setDEF("Tour") \
     .setDescription("Tour Views") \
    ) \
#Viewpoint position='0 0 4' description='sphere in road'/
    .addChildren(BackgroundObject() \
     .setBackUrl(["resources/images/bBK.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bBK.png"]) \
     .setBottomUrl(["resources/images/bBT.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bBT.png"]) \
     .setFrontUrl(["resources/images/bFR.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bFR.png"]) \
     .setLeftUrl(["resources/images/bLF.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bLF.png"]) \
     .setRightUrl(["resources/images/bRT.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bRT.png"]) \
     .setTopUrl(["resources/images/bTP.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bTP.png"]) \
    ) \
    .addChildren(TransformObject() \
     .addChildren(ShapeObject() \
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
       .addShaders(ComposedShaderObject(language = "GLSL") \
        .addField(fieldObject() \
         .setName("chromaticDispertion") \
         .setAccessType("inputOutput") \
         .setType("SFVec3f") \
         .setValue("0.98 1 1.033") \
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
         .setDEF("common") \
         .setUrl(["../shaders/common.fs","https://coderextreme.net/X3DJSONLD/shaders/common.fs"]) \
         .setType("FRAGMENT") \
        ) \
       ) \
       .addShaders(ComposedShaderObject(language = "GLSL") \
        .addField(fieldObject() \
         .setName("chromaticDispertion") \
         .setAccessType("initializeOnly") \
         .setType("SFVec3f") \
         .setValue("0.98 1 1.033") \
        ) \
        .addField(fieldObject() \
         .setName("cube") \
         .setType("SFNode") \
         .setAccessType("initializeOnly") \
         .addChildren(ComposedCubeMapTextureObject() \
          .setUSE("texture") \
         ) \
        ) \
        .addField(fieldObject() \
         .setName("bias") \
         .setAccessType("initializeOnly") \
         .setType("SFFloat") \
         .setValue("0.5") \
        ) \
        .addField(fieldObject() \
         .setName("scale") \
         .setAccessType("initializeOnly") \
         .setType("SFFloat") \
         .setValue("0.5") \
        ) \
        .addField(fieldObject() \
         .setName("power") \
         .setAccessType("initializeOnly") \
         .setType("SFFloat") \
         .setValue("2") \
        ) \
        .addParts(ShaderPartObject() \
         .setUrl(["../shaders/cobweb.vs","https://coderextreme.net/X3DJSONLD/shaders/cobweb.vs"]) \
         .setType("VERTEX") \
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
