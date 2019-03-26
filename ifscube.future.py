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
     .setContent("template.json") \
    ) \
    .addMeta(metaObject() \
     .setName("identifier") \
     .setContent("http://coderextreme.net/X3DJSONLD/template.json") \
    ) \
    .addMeta(metaObject() \
     .setName("description") \
     .setContent("Template for an Indexed Face Set") \
    ) \
    .addMeta(metaObject() \
     .setName("creator") \
     .setContent("John Carlson") \
    ) \
    .addMeta(metaObject() \
     .setName("created") \
     .setContent("4 April 2017") \
    ) \
   ) \
   .setScene(SceneObject() \
    .addChildren(GroupObject() \
     .addChildren(ShapeObject() \
      .setGeometry(IndexedFaceSetObject(creaseAngle = 1.57, coordIndex = [0,0,1,-1,0,1,1,-1,2,2,3,3,-1,0,3,3,0,-1,0,3,2,1,-1,1,2,2,1,-1,1,2,3,0,-1], normalIndex = [0,-1,0,-1,1,-1,2,-1,3,-1,4,-1,5,-1], normalPerVertex = False) \
       .setDEF("IndexedFaceSet") \
       .setColorIndex([0,0,0,-1,0,0,0,-1,0,0,0,0,-1,0,0,0,0,-1,0,0,0,0,-1,0,0,0,0,-1,0,0,0,0,-1]) \
       .setCoord(CoordinateObject() \
        .setPoint([0,0,1,0,1,1,1,1,1,1,0,1]) \
       ) \
       .setNormal(NormalObject() \
        .setVector([1,0,0,-1,0,0,0,1,0,0,0,-1,0,-1,0,0,0,1]) \
       ) \
       .setColor(ColorObject() \
        .setColor([0,1,0]) \
       ) \
      ) \
     ) \
    ) \
   ) \

X3D0.toFileX3D("./future/./ifscube.newf.x3d")
