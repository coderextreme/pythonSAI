import jnius_config
jnius_config.set_classpath('.', 'X3DJSAIL.3.3.full.jar')
from jnius import autoclass
from X3Dautoclass import *
X3D0 = X3DObject() \
   .setProfile("Immersive") \
   .setVersion("3.0") \
   .setHead(headObject() \
    .addMeta(metaObject() \
     .setName("title") \
     .setContent("ExtrusionHeart.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("description") \
     .setContent("Simple extrusion of a Valentine heart.") \
    ) \
    .addMeta(metaObject() \
     .setName("creator") \
     .setContent("Class participants in course Introduction to VRML/X3D.") \
    ) \
    .addMeta(metaObject() \
     .setName("created") \
     .setContent("14 February 2001") \
    ) \
    .addMeta(metaObject() \
     .setName("modified") \
     .setContent("27 November 2015") \
    ) \
    .addMeta(metaObject() \
     .setName("identifier") \
     .setContent("http://www.web3d.org/x3d/content/examples/Basic/course/ExtrusionHeart.x3d") \
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
    .addChild(ViewpointObject() \
     .setDescription("Extrusion Heart") \
     .setOrientation([1,0,0,1.57]) \
     .setPosition([0,-4,0]) \
    ) \
    .addChild(TransformObject() \
     .setTranslation([0,-0.5,0]) \
     .addChild(ShapeObject() \
      .setGeometry(ExtrusionObject() \
       .setCreaseAngle(3.14159) \
       .setCrossSection([0,0.8,0.2,1,0.7,0.95,1,0.5,0.8,0,0.5,-0.3,0,-0.7,-0.5,-0.3,-0.8,0,-1,0.5,-0.7,0.95,-0.2,1,0,0.8]) \
       .setScale([0.01,0.01,0.8,0.8,1,1,0.8,0.8,0.01,0.01]) \
       .setSolid(False) \
       .setSpine([0,0,0,0,0.1,0,0,0.5,0,0,0.9,0,0,1,0]) \
      ) \
      .setAppearance(AppearanceObject() \
       .setMaterial(MaterialObject() \
        .setDiffuseColor([0.8,0.3,0.3]) \
       ) \
      ) \
     ) \
    ) \
   ) \

X3D0.toFileX3D("./future/./ExtrusionHeart.newf.x3d")
