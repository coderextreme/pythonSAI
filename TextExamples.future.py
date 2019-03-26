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
     .setContent("TextExamples.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("description") \
     .setContent("Show different escape-character text examples for embedded quotation marks.") \
    ) \
    .addMeta(metaObject() \
     .setName("creator") \
     .setContent("Don Brutzman") \
    ) \
    .addMeta(metaObject() \
     .setName("created") \
     .setContent("7 April 2001") \
    ) \
    .addMeta(metaObject() \
     .setName("modified") \
     .setContent("26 April 2016") \
    ) \
    .addMeta(metaObject() \
     .setName("warning") \
     .setContent("Note that X3D Canonicalization (C14N) will scrub alternate XML character representations, be careful to check original encoding into version control.") \
    ) \
    .addMeta(metaObject() \
     .setName("warning") \
     .setContent("Usually this source document needs to be inspected and edited using a plain-text editor in order to see the differences in these XML-equivalent text representations.") \
    ) \
    .addMeta(metaObject() \
     .setName("identifier") \
     .setContent("http://www.web3d.org/x3d/content/examples/Basic/development/TextExamples.x3d") \
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
    .addChildren(TransformObject() \
     .setTranslation([0,2,0]) \
     .addChildren(ShapeObject() \
      .setGeometry(TextObject() \
       .setString(["Compare special character escaping"]) \
       .setFontStyle(FontStyleObject(justify = ["MIDDLE","MIDDLE"], size = 0.8) \
        .setDEF("testFontStyle") \
       ) \
      ) \
      .setAppearance(AppearanceObject() \
       .setDEF("LightBlueAppearance") \
       .setMaterial(MaterialObject() \
        .setDiffuseColor([0.1,0.7,0.7]) \
       ) \
      ) \
     ) \
    ) \
    .addChildren(TransformObject() \
     .setTranslation([-3,0,0]) \
     .addChildren(ShapeObject() \
      .setGeometry(TextObject() \
       .setString(["I don't think so","","he said \"Hi\""]) \
       .setFontStyle(FontStyleObject() \
        .setUSE("testFontStyle") \
       ) \
      ) \
      .setAppearance(AppearanceObject() \
       .setUSE("LightBlueAppearance") \
      ) \
     ) \
    ) \
    .addChildren(TransformObject() \
     .setTranslation([3,0,0]) \
     .addChildren(ShapeObject() \
      .setGeometry(TextObject() \
       .setString(["I don't think so","","he said \"Hi\""]) \
       .setFontStyle(FontStyleObject() \
        .setUSE("testFontStyle") \
       ) \
      ) \
      .setAppearance(AppearanceObject() \
       .setUSE("LightBlueAppearance") \
      ) \
     ) \
    ) \
   ) \

X3D0.toFileX3D("./future/./TextExamples.newf.x3d")
