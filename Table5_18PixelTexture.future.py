import jnius_config
jnius_config.set_classpath('.', 'X3DJSAIL.3.3.full.jar')
from jnius import autoclass
from X3Dautoclass import *
X3D0 = X3DObject() \
   .setProfile("Interchange") \
   .setVersion("3.3") \
   .setHead(headObject() \
    .addMeta(metaObject() \
     .setName("title") \
     .setContent("Table5_18PixelTexture") \
    ) \
    .addMeta(metaObject() \
     .setName("description") \
     .setContent("PixelTexture example for Table 5.18") \
    ) \
    .addMeta(metaObject() \
     .setName("creator") \
     .setContent("Leonard Daly and Don Brutzman") \
    ) \
    .addMeta(metaObject() \
     .setName("created") \
     .setContent("18 December 2006") \
    ) \
    .addMeta(metaObject() \
     .setName("modified") \
     .setContent("2 April 2017") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("http://X3dGraphics.com") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("http://www.web3d.org/x3d/content/examples/X3dResources.html") \
    ) \
    .addMeta(metaObject() \
     .setName("rights") \
     .setContent("Copyright 2006, Daly Realism and Don Brutzman") \
    ) \
    .addMeta(metaObject() \
     .setName("subject") \
     .setContent("X3D, PixelTexture") \
    ) \
    .addMeta(metaObject() \
     .setName("identifier") \
     .setContent("http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter05AppearanceMaterialTextures/Table5_18PixelTexture") \
    ) \
    .addMeta(metaObject() \
     .setName("generator") \
     .setContent("X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit") \
    ) \
    .addMeta(metaObject() \
     .setName("license") \
     .setContent("../license.html") \
    ) \
   ) \
   .setScene(SceneObject() \
    .addChild(BackgroundObject() \
     .setSkyColor([0,0,1]) \
    ) \
    .addChild(TransformObject() \
     .setDEF("Checkerboard") \
     .setTranslation([0,0,-10]) \
     .addChild(ShapeObject() \
      .setAppearance(AppearanceObject() \
       .setTextureTransform(TextureTransformObject() \
        .setScale([500,500]) \
       ) \
       .setTexture(PixelTextureObject() \
        .setImage([2,2,3,15119869,16767927,16767927,15119869]) \
       ) \
      ) \
      .setGeometry(BoxObject() \
       .setSize([1000,1000,0.01]) \
      ) \
     ) \
    ) \
    .addChild(ViewpointObject() \
     .setDescription("View All") \
     .setPosition([0,0,20]) \
    ) \
    .addChild(ViewpointObject() \
     .setDescription("Empty Image") \
     .setPosition([0,5,5]) \
    ) \
    .addChild(TransformObject() \
     .setDEF("EmptyImage") \
     .setRotation([1,1,0,1]) \
     .setTranslation([0,5,0]) \
     .addChild(ShapeObject() \
      .setAppearance(AppearanceObject() \
       .setTexture(PixelTextureObject() \
       ) \
      ) \
      .setGeometry(BoxObject() \
       .setDEF("StandardBox") \
      ) \
     ) \
    ) \
    .addChild(ViewpointObject() \
     .setDescription("Black and white PixelTexture") \
     .setPosition([-5,0,5]) \
    ) \
    .addChild(TransformObject() \
     .setDEF("BW") \
     .setRotation([1,1,0,1]) \
     .setTranslation([-5,0,0]) \
     .addChild(ShapeObject() \
      .setAppearance(AppearanceObject() \
       .setTexture(PixelTextureObject() \
        .setImage([1,2,1,255,0]) \
       ) \
      ) \
      .setGeometry(BoxObject() \
       .setUSE("StandardBox") \
      ) \
     ) \
    ) \
    .addChild(ViewpointObject() \
     .setDescription("Black and white with Alpha PixelTexture") \
     .setPosition([5,0,5]) \
    ) \
    .addChild(TransformObject() \
     .setDEF("AlphaBW") \
     .setRotation([1,1,0,1]) \
     .setTranslation([5,0,0]) \
     .addChild(ShapeObject() \
      .setAppearance(AppearanceObject() \
       .setTexture(PixelTextureObject() \
        .setImage([2,1,2,52479,8823]) \
       ) \
      ) \
      .setGeometry(BoxObject() \
       .setUSE("StandardBox") \
      ) \
     ) \
    ) \
    .addChild(ViewpointObject() \
     .setDescription("RGB PixelTexture") \
     .setPosition([-5,-5,5]) \
    ) \
    .addChild(TransformObject() \
     .setDEF("RGB") \
     .setRotation([1,1,0,1]) \
     .setTranslation([-5,-5,0]) \
     .addChild(ShapeObject() \
      .setAppearance(AppearanceObject() \
       .setTexture(PixelTextureObject() \
        .setImage([2,4,3,16711680,65280,0,0,0,0,16777215,16776960]) \
       ) \
      ) \
      .setGeometry(BoxObject() \
       .setUSE("StandardBox") \
      ) \
     ) \
    ) \
    .addChild(ViewpointObject() \
     .setDescription("RGB with Alpha PixelTexture") \
     .setPosition([5,-5,5]) \
    ) \
    .addChild(TransformObject() \
     .setDEF("AlphaRGB") \
     .setRotation([1,1,0,1]) \
     .setTranslation([5,-5,0]) \
     .addChild(ShapeObject() \
      .setAppearance(AppearanceObject() \
       .setTexture(PixelTextureObject() \
        .setImage([3,2,4,-16776961,16711935,65535,-16777089,16711807,65407]) \
       ) \
      ) \
      .setGeometry(BoxObject() \
       .setUSE("StandardBox") \
      ) \
     ) \
    ) \
   ) \

X3D0.toFileX3D("./future/./Table5_18PixelTexture.newf.x3d")
