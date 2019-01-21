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
     .setContent("SFVec3f.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("creator") \
     .setContent("John Carlson") \
    ) \
    .addMeta(metaObject() \
     .setName("description") \
     .setContent("3 prismatic spheres") \
    ) \
    .addMeta(metaObject() \
     .setName("identifier") \
     .setContent("https://coderextreme.net/X3DJSONLD/SFVec3f.x3d") \
    ) \
   ) \
   .setScene(SceneObject() \
    .addChild(NavigationInfoObject() \
    ) \
    .addChild(TransformObject() \
     .setDEF("transform") \
     .addChild(ShapeObject() \
      .setAppearance(AppearanceObject() \
       .setMaterial(MaterialObject() \
        .setDiffuseColor([0.7,0.7,0.7]) \
        .setSpecularColor([0.5,0.5,0.5]) \
       ) \
      ) \
      .setGeometry(SphereObject() \
      ) \
     ) \
    ) \
    .addChild(ScriptObject() \
     .setDEF("Bounce") \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFVEC3F) \
      .setName("set_translation") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTONLY) \
      .setValue("0 0 0") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFVEC3F) \
      .setName("translation_changed") \
      .setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY) \
      .setValue("0 0 0") \
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
      .setType(fieldObject.TYPE_SFTIME) \
      .setName("set_fraction") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTONLY) \
     ) \
     .setSourceCode('''ecmascript:\n"+
"			function newBubble() {\n"+
"			    translation = new SFVec3f(0, 0, 0);\n"+
"			    velocity = new SFVec3f(\n"+
"			    	Math.random() - 0.5,\n"+
"				Math.random() - 0.5,\n"+
"				Math.random() - 0.5);\n"+
"			}\n"+
"			function set_fraction() {\n"+
"			    translation = new SFVec3f(\n"+
"			    	translation.x + velocity.x,\n"+
"				translation.y + velocity.y,\n"+
"				translation.z + velocity.z);\n"+
"				if (Math.abs(translation.x) > 10) {\n"+
"					newBubble();\n"+
"				} else if (Math.abs(translation.y) > 10) {\n"+
"					newBubble();\n"+
"				} else if (Math.abs(translation.z) > 10) {\n"+
"					newBubble();\n"+
"				} else {\n"+
"					velocity = new SFVec3f(\n"+
"						velocity.x + Math.random() * 0.2 - 0.1,\n"+
"						velocity.y + Math.random() * 0.2 - 0.1,\n"+
"						velocity.z + Math.random() * 0.2 - 0.1\n"+
"					);\n"+
"				}\n"+
"			}\n"+
"\n"+
"			function initialize() {\n"+
"			     newBubble();\n"+
"			}''')
    ) \
    .addChild(TimeSensorObject() \
     .setDEF("TourTime") \
     .setCycleInterval(0.15) \
     .setLoop(True) \
    ) \
    .addChild(ROUTEObject() \
     .setFromNode("TourTime") \
     .setFromField("cycleTime") \
     .setToNode("Bounce") \
     .setToField("set_fraction") \
    ) \
    .addChild(ROUTEObject() \
     .setFromNode("Bounce") \
     .setFromField("translation_changed") \
     .setToNode("transform") \
     .setToField("set_translation") \
    ) \
   ) \

X3D0.toFileX3D("./future/./SFVec3f.newf.x3d")
