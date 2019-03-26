import jnius_config
jnius_config.set_classpath('.', 'X3DJSAIL.3.3.full.jar')
from jnius import autoclass
from X3Dautoclass import *
X3D0 = X3DObject() \
   .setProfile("Immersive") \
   .setVersion("3.3") \
   .setHead(headObject() \
    .addMeta(metaObject() \
     .setName("title") \
     .setContent("HelloWorld.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("description") \
     .setContent("Simple X3D scene example: Hello World!") \
    ) \
    .addMeta(metaObject() \
     .setName("created") \
     .setContent("30 October 2000") \
    ) \
    .addMeta(metaObject() \
     .setName("modified") \
     .setContent("14 April 2017") \
    ) \
    .addMeta(metaObject() \
     .setName("creator") \
     .setContent("Don Brutzman") \
    ) \
    .addMeta(metaObject() \
     .setName("Image") \
     .setContent("HelloWorld.tall.png") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("http://en.wikipedia.org/wiki/Hello_world") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("https://en.wikipedia.org/wiki/Hello#.22Hello.2C_World.22_computer_program") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("https://en.wikipedia.org/wiki/\"Hello,_World!\"_program") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("http://en.wikibooks.org/w/index.php?title=Computer_Programming/Hello_world") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("http://www.HelloWorldExample.net") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("http://www.web3D.org") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("http://www.web3d.org/realtime-3d/news/internationalization-x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("http://www.web3d.org/x3d/content/examples/HelloWorld.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("http://X3dGraphics.com/examples/X3dForAdvancedModeling/HelloWorldScenes") \
    ) \
    .addMeta(metaObject() \
     .setName("identifier") \
     .setContent("http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter01TechnicalOverview/HelloWorld.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("license") \
     .setContent("http://www.web3d.org/x3d/content/examples/license.html") \
    ) \
    .addMeta(metaObject() \
     .setName("generator") \
     .setContent("X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("HelloWorld.wrl") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("HelloWorld.x3dv") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("HelloWorld.x3db") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("HelloWorld.xhtml") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("HelloWorld.json") \
    ) \
#Alternate encodings: VRML97, X3D ClassicVRML Encoding, X3D Compressed Binary Encoding (CBE), X3DOM, JSON
   ) \
   .setScene(SceneObject() \
#Example scene to illustrate X3D nodes and fields (XML elements and attributes)
    .addChildren(WorldInfoObject() \
     .setTitle("Hello world!") \
    ) \
    .addChildren(GroupObject() \
     .addChildren(ViewpointObject() \
      .setDEF("ViewUpClose") \
      .setCenterOfRotation([0,-1,0]) \
      .setDescription("Hello world!") \
      .setPosition([0,-1,7]) \
     ) \
     .addChildren(TransformObject() \
      .setRotation([0,1,0,3]) \
      .addChildren(ShapeObject() \
       .setGeometry(SphereObject() \
       ) \
       .setAppearance(AppearanceObject() \
        .setMaterial(MaterialObject() \
         .setDEF("MaterialLightBlue") \
         .setDiffuseColor([0.1,0.5,1]) \
        ) \
        .setTexture(ImageTextureObject() \
         .setDEF("ImageCloudlessEarth") \
         .setUrl(["earth-topo.png","earth-topo.jpg","earth-topo-small.gif","http://www.web3d.org/x3d/content/examples/Basic/earth-topo.png","http://www.web3d.org/x3d/content/examples/Basic/earth-topo.jpg","http://www.web3d.org/x3d/content/examples/Basic/earth-topo-small.gif"]) \
        ) \
       ) \
      ) \
     ) \
     .addChildren(TransformObject() \
      .setTranslation([0,-2,0]) \
      .addChildren(ShapeObject() \
       .setGeometry(TextObject() \
        .setDEF("TextMessage") \
        .setString(["Hello","world!"]) \
        .setFontStyle(FontStyleObject(justify = ["MIDDLE","MIDDLE"]) \
        ) \
       ) \
       .setAppearance(AppearanceObject() \
        .setMaterial(MaterialObject() \
         .setUSE("MaterialLightBlue") \
        ) \
       ) \
      ) \
     ) \
    ) \
   ) \

X3D0.toFileX3D("./future/./HelloWorld.newf.x3d")
