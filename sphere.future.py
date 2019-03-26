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
     .setContent("sphere.x3d") \
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
     .setContent("https://coderextreme.net/X3DJSONLD/sphere.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("description") \
     .setContent("a sphere") \
    ) \
   ) \
   .setScene(SceneObject() \
    .addChildren(GroupObject() \
     .addChildren(ShapeObject() \
      .setAppearance(AppearanceObject() \
       .setMaterial(MaterialObject() \
        .setDiffuseColor([1,1,1]) \
       ) \
      ) \
      .setGeometry(SphereObject() \
      ) \
     ) \
    ) \
   ) \

X3D0.toFileX3D("./future/./sphere.newf.x3d")
