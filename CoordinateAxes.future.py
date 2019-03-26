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
     .setContent("CoordinateAxis.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("creator") \
     .setContent("Unknown, see X3D Resources Archives") \
    ) \
    .addMeta(metaObject() \
     .setName("generator") \
     .setContent("manual") \
    ) \
    .addMeta(metaObject() \
     .setName("identifier") \
     .setContent("https://coderextreme.net/X3DJSONLD/CoordinateAxis.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("description") \
     .setContent("a box") \
    ) \
   ) \
   .setScene(SceneObject() \
    .addChildren(CollisionObject() \
     .setDEF("DoNotCollideWithVisualizationWidget") \
#Invoke CoordinateAxes in other scenes as an Inline child inside a scaling Transform node, at the topmost level of the scene graph.
#This NavigationInfo allows examine mode and will be overridden by any parent scene.
#Each arrow goes from +1m to -1m to allow linear scaling to fit a scene
#Note each label rotates about the scene's vertical Y axis for consistency, enabling local orientation by user
     .setProxy(GroupObject() \
#Vertical Y arrow and label
      .addChildren(GroupObject() \
       .setDEF("ArrowGreen") \
       .addChildren(ShapeObject() \
        .setGeometry(CylinderObject(radius = 0.025) \
         .setDEF("ArrowCylinder") \
         .setTop(False) \
        ) \
        .setAppearance(AppearanceObject() \
         .setDEF("Green") \
         .setMaterial(MaterialObject() \
          .setDiffuseColor([0.1,0.6,0.1]) \
          .setEmissiveColor([0.05,0.2,0.05]) \
         ) \
        ) \
       ) \
       .addChildren(TransformObject() \
        .setTranslation([0,1,0]) \
        .addChildren(ShapeObject() \
         .setGeometry(ConeObject(bottomRadius = 0.05, height = 0.1) \
          .setDEF("ArrowCone") \
         ) \
         .setAppearance(AppearanceObject() \
          .setUSE("Green") \
         ) \
        ) \
       ) \
      ) \
      .addChildren(TransformObject() \
       .setTranslation([0,1.08,0]) \
       .addChildren(BillboardObject() \
        .addChildren(ShapeObject() \
         .setAppearance(AppearanceObject() \
          .setDEF("LABEL_APPEARANCE") \
          .setMaterial(MaterialObject() \
           .setDiffuseColor([1,1,0.3]) \
           .setEmissiveColor([0.33,0.33,0.1]) \
          ) \
         ) \
         .setGeometry(TextObject() \
          .setString(["Y"]) \
          .setFontStyle(FontStyleObject(family = ["SANS"], justify = ["MIDDLE","MIDDLE"], size = 0.2) \
           .setDEF("LABEL_FONT") \
          ) \
         ) \
        ) \
       ) \
      ) \
     ) \
     .setProxy(TransformObject() \
      .setRotation([0,0,1,-1.57079]) \
#Horizontal X arrow and label
      .addChildren(GroupObject() \
       .addChildren(GroupObject() \
        .setDEF("ArrowRed") \
        .addChildren(ShapeObject() \
         .setGeometry(CylinderObject() \
          .setUSE("ArrowCylinder") \
         ) \
         .setAppearance(AppearanceObject() \
          .setDEF("Red") \
          .setMaterial(MaterialObject() \
           .setDiffuseColor([0.7,0.1,0.1]) \
           .setEmissiveColor([0.33,0,0]) \
          ) \
         ) \
        ) \
        .addChildren(TransformObject() \
         .setTranslation([0,1,0]) \
         .addChildren(ShapeObject() \
          .setGeometry(ConeObject() \
           .setUSE("ArrowCone") \
          ) \
          .setAppearance(AppearanceObject() \
           .setUSE("Red") \
          ) \
         ) \
        ) \
       ) \
       .addChildren(TransformObject() \
        .setRotation([0,0,1,1.57079]) \
        .setTranslation([0.072,1.1,0]) \
#note label rotated back to original coordinate frame
        .addChildren(BillboardObject() \
         .addChildren(ShapeObject() \
          .setAppearance(AppearanceObject() \
           .setUSE("LABEL_APPEARANCE") \
          ) \
          .setGeometry(TextObject() \
           .setString(["X"]) \
           .setFontStyle(FontStyleObject() \
            .setUSE("LABEL_FONT") \
           ) \
          ) \
         ) \
        ) \
       ) \
      ) \
     ) \
     .setProxy(TransformObject() \
      .setRotation([1,0,0,1.57079]) \
#Perpendicular Z arrow and label, note right-hand rule
      .addChildren(GroupObject() \
       .addChildren(GroupObject() \
        .setDEF("ArrowBlue") \
        .addChildren(ShapeObject() \
         .setGeometry(CylinderObject() \
          .setUSE("ArrowCylinder") \
         ) \
         .setAppearance(AppearanceObject() \
          .setDEF("Blue") \
          .setMaterial(MaterialObject() \
           .setDiffuseColor([0.3,0.3,1]) \
           .setEmissiveColor([0.1,0.1,0.33]) \
          ) \
         ) \
        ) \
        .addChildren(TransformObject() \
         .setTranslation([0,1,0]) \
         .addChildren(ShapeObject() \
          .setGeometry(ConeObject() \
           .setUSE("ArrowCone") \
          ) \
          .setAppearance(AppearanceObject() \
           .setUSE("Blue") \
          ) \
         ) \
        ) \
       ) \
       .addChildren(TransformObject() \
        .setRotation([1,0,0,-1.57079]) \
        .setTranslation([0,1.1,0.072]) \
#note label rotated back to original coordinate frame
        .addChildren(BillboardObject() \
         .addChildren(ShapeObject() \
          .setAppearance(AppearanceObject() \
           .setUSE("LABEL_APPEARANCE") \
          ) \
          .setGeometry(TextObject() \
           .setString(["Z"]) \
           .setFontStyle(FontStyleObject() \
            .setUSE("LABEL_FONT") \
           ) \
          ) \
         ) \
        ) \
       ) \
      ) \
     ) \
    ) \
   ) \

X3D0.toFileX3D("./future/./CoordinateAxes.newf.x3d")
