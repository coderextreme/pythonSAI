import jnius_config
jnius_config.set_classpath('.', 'X3DJSAIL.3.3.full.jar')
from jnius import autoclass
from X3Dautoclass import *
X3D0 = X3DObject() \
   .setProfile("Immersive") \
   .setVersion("3.3") \
   .setHead(headObject() \
    .addMeta(metaObject() \
     .setName("creator") \
     .setContent("John W Carlson") \
    ) \
    .addMeta(metaObject() \
     .setName("created") \
     .setContent("December 13 2015") \
    ) \
    .addMeta(metaObject() \
     .setName("title") \
     .setContent("text.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("identifier") \
     .setContent("https://coderextreme.net/X3DJSONLD/text.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("description") \
     .setContent("test \\n text") \
    ) \
    .addMeta(metaObject() \
     .setName("generator") \
     .setContent("Vim, X3D-Edit, https://savage.nps.edu/X3D-Edit") \
    ) \
   ) \
   .setScene(SceneObject() \
    .addChildren(TransformObject() \
     .addChildren(ShapeObject() \
      .setGeometry(TextObject() \
       .setString(["Node\"\"\""]) \
       .setFontStyle(FontStyleObject() \
       ) \
      ) \
      .setAppearance(AppearanceObject() \
       .setMaterial(MaterialObject() \
       ) \
      ) \
     ) \
     .addChildren(ShapeObject() \
      .setGeometry(TextObject() \
       .setString(["Node2","\\\\","\\\\\\\\","Node2"]) \
       .setFontStyle(FontStyleObject() \
       ) \
      ) \
      .setAppearance(AppearanceObject() \
       .setMaterial(MaterialObject() \
       ) \
      ) \
     ) \
     .addChildren(ShapeObject() \
      .setGeometry(TextObject() \
       .setString(["Node3 \\\\\\\\ \\\\ ","Node3\"\"\""]) \
       .setFontStyle(FontStyleObject() \
       ) \
      ) \
      .setAppearance(AppearanceObject() \
       .setMaterial(MaterialObject() \
       ) \
      ) \
     ) \
     .addChildren(ScriptObject() \
      .addField(fieldObject() \
       .setName("frontUrls") \
       .setType("MFString") \
       .setAccessType("initializeOnly") \
       .setValue("\"rnl_front.png\" \"uffizi_front.png\"") \
      ) \
.setSourceCode('''ecmascript:\n"+
"			    var me = '\"1\" \"\"2\" \"\\n3\"';''')
     ) \
    ) \
   ) \

X3D0.toFileX3D("./future/./text.newf.x3d")
