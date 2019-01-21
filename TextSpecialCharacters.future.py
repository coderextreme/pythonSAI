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
     .setContent("TextSpecialCharacters.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("description") \
     .setContent("Text node demonstration of quotation, apostrophe, ampersand and backslash characters using X3D MFString escaping for XML character entities") \
    ) \
    .addMeta(metaObject() \
     .setName("creator") \
     .setContent("Don Brutzman") \
    ) \
    .addMeta(metaObject() \
     .setName("created") \
     .setContent("12 July 2008") \
    ) \
    .addMeta(metaObject() \
     .setName("modified") \
     .setContent("2 April 2017") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("Character entity references in HTML 4") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("http://www.w3.org/TR/REC-html40/sgml/entities.html") \
    ) \
    .addMeta(metaObject() \
     .setName("rights") \
     .setContent("Copyright (c) Don Brutzman and Leonard Daly, 2008") \
    ) \
    .addMeta(metaObject() \
     .setName("identifier") \
     .setContent("http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter02GeometryPrimitives/TextSpecialCharacters.x3d") \
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
     .setSkyColor([1,1,1]) \
    ) \
    .addChild(ViewpointObject() \
     .setDescription("Default View") \
     .setPosition([0,0,15]) \
    ) \
    .addChild(ShapeObject() \
.addComments(CommentsBlock("""Empty string \"\" means to skip a line""")) \
.addComments(CommentsBlock("""The ampersand escape characters are based on XML rules""")) \
.addComments(CommentsBlock("""apostrophe ' is &apos; and needs to be escaped in single-quote delimiters used for string='value' attribute""")) \
.addComments(CommentsBlock("""ampersand & is &amp; and needs to be escaped""")) \
.addComments(CommentsBlock("""quotation \" is &quot; and isn't needed if single-quote delimiters used for string='value' attribute""")) \
.addComments(CommentsBlock("""quotation \" can be used within an X3D string if escaped with backslash \\ as \\\"\"""")) \
.addComments(CommentsBlock("""backslash \\ is used as escape character for \" (and itself) in X3D""")) \
.addComments(CommentsBlock("""character entities are listed in HTML specification and are good for any XML""")) \
     .setGeometry(TextObject() \
      .setDEF("DefaultText") \
      .setString(["Character entity substitutions:","empty string \"\" skips a line:","","apostrophe ' is &apos;","ampersand & is &amp;","quote mark \" is &quot;","backslash \\\\ is X3D escape character","double backslash \\\\\\\\ is X3D backslash \\\\ character","Pi Π is &#928; XML character entity"]) \
      .setFontStyle(FontStyleObject() \
       .setDEF("CenteredFontStyle") \
       .setJustify(["MIDDLE","MIDDLE"]) \
      ) \
     ) \
     .setAppearance(AppearanceObject() \
      .setMaterial(MaterialObject() \
       .setDEF("DefaultMaterial") \
       .setDiffuseColor([0.2,0.2,0.2]) \
      ) \
     ) \
    ) \
   ) \

X3D0.toFileX3D("./future/./TextSpecialCharacters.newf.x3d")
