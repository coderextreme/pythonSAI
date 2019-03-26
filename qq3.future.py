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
     .setContent("qq3.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("creator") \
     .setContent("John Carlson") \
    ) \
    .addMeta(metaObject() \
     .setName("translator") \
     .setContent("John Carlson") \
    ) \
    .addMeta(metaObject() \
     .setName("created") \
     .setContent("11 Jan 2015") \
    ) \
    .addMeta(metaObject() \
     .setName("modified") \
     .setContent("05 May 2017") \
    ) \
    .addMeta(metaObject() \
     .setName("description") \
     .setContent("12 extrusions to test prototype expander") \
    ) \
    .addMeta(metaObject() \
     .setName("identifier") \
     .setContent("https://coderextreme.net/x3d/qq3.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("generator") \
     .setContent("manual") \
    ) \
   ) \
   .setScene(SceneObject() \
    .addChildren(ProtoDeclareObject() \
     .setName("Process") \
     .setProtoBody(ProtoBodyObject() \
      .addChildren(GroupObject() \
#left
       .addChildren(TransformObject() \
        .setScale([0.5,0.5,0.5]) \
        .addChildren(ShapeObject() \
         .setDEF("ShapeLeftDown") \
         .setAppearance(AppearanceObject() \
          .setMaterial(MaterialObject() \
           .setDiffuseColor([0.7,1,0]) \
          ) \
         ) \
         .setGeometry(ExtrusionObject(spine = [-2.5,0,0,-1.5,0,0], creaseAngle = 0.785, crossSection = [1,0,0.92,-0.38,0.71,-0.71,0.38,-0.92,0,-1,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1,0,-0.92,0.38,-0.71,0.71,-0.38,0.92,0,1,0.38,0.92,0.71,0.71,0.92,0.38,1,0]) \
         ) \
        ) \
       ) \
#right
       .addChildren(TransformObject() \
        .setScale([0.5,0.5,0.5]) \
        .addChildren(ShapeObject() \
         .setDEF("ShapeUpRight") \
         .setAppearance(AppearanceObject() \
          .setMaterial(MaterialObject() \
           .setDiffuseColor([0,0.7,1]) \
          ) \
         ) \
         .setGeometry(ExtrusionObject(spine = [1.5,0,0,2.5,0,0], creaseAngle = 0.785, crossSection = [1,0,0.92,-0.38,0.71,-0.71,0.38,-0.92,0,-1,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1,0,-0.92,0.38,-0.71,0.71,-0.38,0.92,0,1,0.38,0.92,0.71,0.71,0.92,0.38,1,0]) \
         ) \
        ) \
       ) \
#up
       .addChildren(TransformObject() \
        .setScale([0.5,0.5,0.5]) \
        .addChildren(ShapeObject() \
         .setUSE("ShapeUpRight") \
        ) \
       ) \
#down
       .addChildren(TransformObject() \
        .setScale([0.5,0.5,0.5]) \
        .addChildren(ShapeObject() \
         .setUSE("ShapeLeftDown") \
        ) \
       ) \
      ) \
     ) \
    ) \
    .addChildren(ViewpointObject() \
     .setDescription("Process pipes") \
     .setOrientation([1,0,0,-0.4]) \
     .setPosition([0,5,12]) \
    ) \
    .addChildren(TransformObject() \
     .setTranslation([0,-2.5,0]) \
     .addChildren(ProtoInstanceObject() \
      .setName("Process") \
     ) \
    ) \
    .addChildren(TransformObject() \
     .addChildren(ProtoInstanceObject() \
      .setName("Process") \
     ) \
    ) \
    .addChildren(TransformObject() \
     .setTranslation([0,2.5,0]) \
     .addChildren(ProtoInstanceObject() \
      .setName("Process") \
     ) \
    ) \
   ) \

X3D0.toFileX3D("./future/./qq3.newf.x3d")
