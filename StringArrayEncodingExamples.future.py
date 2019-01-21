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
     .setContent("StringArrayEncodingExamples.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("description") \
     .setContent("Demonstrate simple X3D MFString (string array) encoding.") \
    ) \
    .addMeta(metaObject() \
     .setName("created") \
     .setContent("27 May 2017") \
    ) \
    .addMeta(metaObject() \
     .setName("modified") \
     .setContent("27 May 2017") \
    ) \
    .addMeta(metaObject() \
     .setName("creator") \
     .setContent("Don Brutzman") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("X3dHeaderPrototypeSyntaxExamples.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("specificationSection") \
     .setContent("X3D encodings, ISO/IEC 19775-1, Part 1: Architecture and base components, 5 Field type reference, 5.3.14 SFString and MFString") \
    ) \
    .addMeta(metaObject() \
     .setName("specificationUrl") \
     .setContent("http://www.web3d.org/documents/specifications/19775-1/V3.3/Part01/fieldsDef.html#SFStringAndMFString") \
    ) \
    .addMeta(metaObject() \
     .setName("specificationSection") \
     .setContent("X3D encodings, ISO/IEC 19776-1.3, Part 1: XML encoding, 5.3.14 SFString and MFString") \
    ) \
    .addMeta(metaObject() \
     .setName("specificationUrl") \
     .setContent("http://www.web3d.org/documents/specifications/19776-1/V3.3/Part01/EncodingOfFields.html#SFString") \
    ) \
    .addMeta(metaObject() \
     .setName("specificationSection") \
     .setContent("X3D encodings, ISO/IEC 19776-2 v3.3, Part 2: Classic VRML encoding, 5.15 SFString and MFString") \
    ) \
    .addMeta(metaObject() \
     .setName("specificationUrl") \
     .setContent("http://www.web3d.org/documents/specifications/19776-2/V3.3/Part02/EncodingOfFields.html#SFString") \
    ) \
    .addMeta(metaObject() \
     .setName("identifier") \
     .setContent("http://www.web3d.org/x3d/content/examples/Basic/X3dSpecifications/StringArrayEncodingExamples.x3d") \
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
     .setDEF("EntryView") \
     .setDescription("Hello MFString syntax") \
    ) \
    .addChild(BackgroundObject() \
     .setSkyColor([0.6,1,0.8]) \
    ) \
    .addChild(ShapeObject() \
     .setGeometry(TextObject() \
      .setString(["One, Two, Three","","He said, \"Immel did it!\""]) \
      .addComments(CommentsBlock("""alternative XML encoding: Text string='\"One, Two, Three\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\"'""")) \
      .addComments(CommentsBlock("""alternative Java source: .setString(new String [] {\"One, Two, Three\", \"\", \"He said, \\\"\"Immel did it!\\\"\"\"})""")) \
      .setFontStyle(FontStyleObject() \
       .setJustify(["MIDDLE","MIDDLE"]) \
       .setStyle("BOLD") \
      ) \
     ) \
     .setAppearance(AppearanceObject() \
      .setMaterial(MaterialObject() \
       .setDiffuseColor([0.6,0.4,0.2]) \
      ) \
     ) \
    ) \
   ) \

X3D0.toFileX3D("./future/./StringArrayEncodingExamples.newf.x3d")
