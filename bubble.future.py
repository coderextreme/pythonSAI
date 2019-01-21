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
     .setContent("bubble.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("creator") \
     .setContent("John Carlson") \
    ) \
    .addMeta(metaObject() \
     .setName("description") \
     .setContent("Tour around a prismatic sphere") \
    ) \
    .addMeta(metaObject() \
     .setName("generator") \
     .setContent("X3D-Edit, https://savage.nps.edu/X3D-Edit") \
    ) \
    .addMeta(metaObject() \
     .setName("identifier") \
     .setContent("https://coderextreme.net/X3DJSONLD/bubble.x3d") \
    ) \
   ) \
   .setScene(SceneObject() \
    .addChild(NavigationInfoObject() \
     .setType(["EXAMINE"]) \
    ) \
    .addChild(ViewpointObject() \
     .setPosition([0,0,4]) \
     .setOrientation([1,0,0,0]) \
     .setDescription("Bubble in action") \
    ) \
    .addChild(ProtoDeclareObject() \
     .setName("Bubble") \
     .setProtoBody(ProtoBodyObject() \
      .addChild(TransformObject() \
       .setDEF("transform") \
       .addChild(ShapeObject() \
        .setGeometry(SphereObject() \
         .setRadius(0.25) \
        ) \
        .setAppearance(AppearanceObject() \
         .setMaterial(MaterialObject() \
          .setDiffuseColor([1,0,0]) \
          .setTransparency(0.2) \
         ) \
        ) \
       ) \
       .addChild(ScriptObject() \
        .setDEF("bounce") \
        .addField(fieldObject() \
         .setType(fieldObject.TYPE_SFVEC3F) \
         .setName("scale") \
         .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
         .setValue("1 1 1") \
        ) \
        .addField(fieldObject() \
         .setType(fieldObject.TYPE_SFVEC3F) \
         .setName("translation") \
         .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
         .setValue("0 0 0") \
        ) \
        .addField(fieldObject() \
         .setType(fieldObject.TYPE_SFVEC3F) \
         .setName("velocity") \
         .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
         .setValue("0 0 0") \
        ) \
        .addField(fieldObject() \
         .setType(fieldObject.TYPE_SFVEC3F) \
         .setName("scalvel") \
         .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
         .setValue("0 0 0") \
        ) \
        .addField(fieldObject() \
         .setType(fieldObject.TYPE_SFFLOAT) \
         .setName("set_fraction") \
         .setAccessType(fieldObject.ACCESSTYPE_INPUTONLY) \
        ) \
        .setSourceCode('''ecmascript:\n"+
"function initialize() {\n"+
"    velocity = new SFVec3f(Math.random() * 0.25 - 0.125, Math.random() * 0.25 - 0.125, Math.random() * 0.25 - 0.125);\n"+
"\n"+
"    scalvel = new SFVec3f(Math.random() * 0.4, Math.random() * 0.4, Math.random() * 0.4);\n"+
"}\n"+
"\n"+
"function set_fraction(value) {\n"+
"	translation = new SFVec3f(\n"+
"		translation.x + velocity.x,\n"+
"		translation.y + velocity.y,\n"+
"		translation.z + velocity.z);\n"+
"	scale = new SFVec3f(\n"+
"		scale.x + scalvel.x,\n"+
"		scale.y + scalvel.y,\n"+
"		scale.z + scalvel.z);\n"+
"        // if you get to far away or too big, explode\n"+
"        if ( Math.abs(translation.x) > 256) {\n"+
"		translation.x = 0;\n"+
"		initialize();\n"+
"	}\n"+
"        if ( Math.abs(translation.y) > 256) {\n"+
"		translation.y = 0;\n"+
"		initialize();\n"+
"	}\n"+
"        if ( Math.abs(translation.z) > 256) {\n"+
"		translation.z = 0;\n"+
"		initialize();\n"+
"	}\n"+
"	if (Math.abs(scale.x) > 20) {\n"+
"		scale.x = scale.x/2;\n"+
"		translation.x = 0;\n"+
"		initialize();\n"+
"	}\n"+
"	if (Math.abs(scale.y) > 20) {\n"+
"		scale.y = scale.y/2;\n"+
"		translation.y = 0;\n"+
"		initialize();\n"+
"	}\n"+
"	if (Math.abs(scale.z) > 20) {\n"+
"		scale.z = scale.z/2;\n"+
"		translation.z = 0;\n"+
"		initialize();\n"+
"	}\n"+
"}''')
       ) \
       .addChild(TimeSensorObject() \
        .setDEF("bubbleClock") \
        .setCycleInterval(10) \
        .setLoop(True) \
       ) \
       .addChild(ROUTEObject() \
        .setFromNode("bounce") \
        .setFromField("translation_changed") \
        .setToNode("transform") \
        .setToField("set_translation") \
       ) \
       .addChild(ROUTEObject() \
        .setFromNode("bounce") \
        .setFromField("scale_changed") \
        .setToNode("transform") \
        .setToField("set_scale") \
       ) \
       .addChild(ROUTEObject() \
        .setFromNode("bubbleClock") \
        .setFromField("fraction_changed") \
        .setToNode("bounce") \
        .setToField("set_fraction") \
       ) \
      ) \
     ) \
    ) \
    .addChild(ProtoInstanceObject() \
     .setName("Bubble") \
     .setDEF("bubbleA") \
    ) \
   ) \

X3D0.toFileX3D("./future/./bubble.newf.x3d")
