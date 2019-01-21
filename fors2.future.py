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
     .setName("modified") \
     .setContent("April 18 2017") \
    ) \
    .addMeta(metaObject() \
     .setName("title") \
     .setContent("fors2.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("identifier") \
     .setContent("https://coderextreme.net/X3DJSONLD/fors2.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("description") \
     .setContent("beginnings of a force directed graph in 3D") \
    ) \
    .addMeta(metaObject() \
     .setName("generator") \
     .setContent("Vim, X3D-Edit, https://savage.nps.edu/X3D-Edit") \
    ) \
   ) \
   .setScene(SceneObject() \
    .addChild(ProtoDeclareObject() \
     .setName("node") \
     .setProtoInterface(ProtoInterfaceObject() \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFVEC3F) \
       .setName("position") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setValue("0 0 0") \
      ) \
     ) \
     .setProtoBody(ProtoBodyObject() \
      .addChild(TransformObject() \
       .setDEF("transform") \
       .setIS(ISObject() \
        .addConnect(connectObject() \
         .setNodeField("translation") \
         .setProtoField("position") \
        ) \
       ) \
       .addChild(ShapeObject() \
        .addComments(CommentsBlock("""comment before Sphere""")) \
        .addComments(CommentsBlock("""comment after Sphere""")) \
        .addComments(CommentsBlock("""comment after Appearance""")) \
        .setGeometry(SphereObject() \
        ) \
        .setAppearance(AppearanceObject() \
         .addComments(CommentsBlock("""comment before Material""")) \
         .addComments(CommentsBlock("""comment after Material""")) \
         .setMaterial(MaterialObject() \
          .setDiffuseColor([1,0,0]) \
         ) \
        ) \
       ) \
      ) \
      .addChild(PositionInterpolatorObject() \
       .setDEF("NodePosition") \
       .setKey([0,1]) \
       .setKeyValue([0,0,0,0,5,0]) \
      ) \
      .addChild(ScriptObject() \
       .setDEF("MoveBall") \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFVEC3F) \
        .setName("translation") \
        .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
        .setValue("50 50 0") \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFVEC3F) \
        .setName("old") \
        .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
        .setValue("0 0 0") \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFTIME) \
        .setName("set_cycle") \
        .setAccessType(fieldObject.ACCESSTYPE_INPUTONLY) \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_MFVEC3F) \
        .setName("keyValue") \
        .setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY) \
       ) \
       .setSourceCode('''ecmascript:\n"+
"					function set_cycle(value) {\n"+
"                                                old = translation;\n"+
"						translation = new SFVec3f(Math.random()*100-50, Math.random()*100-50, Math.random()*100-50);\n"+
"                                                keyValue = new MFVec3f([old, translation]);\n"+
"						// Browser.println(translation);\n"+
"					}''')
      ) \
      .addChild(TimeSensorObject() \
       .setDEF("nodeClock") \
       .setCycleInterval(3) \
       .setLoop(True) \
      ) \
      .addChild(ROUTEObject() \
       .setFromNode("nodeClock") \
       .setFromField("cycleTime") \
       .setToNode("MoveBall") \
       .setToField("set_cycle") \
      ) \
      .addChild(ROUTEObject() \
       .setFromNode("nodeClock") \
       .setFromField("fraction_changed") \
       .setToNode("NodePosition") \
       .setToField("set_fraction") \
      ) \
      .addChild(ROUTEObject() \
       .setFromNode("MoveBall") \
       .setFromField("keyValue") \
       .setToNode("NodePosition") \
       .setToField("keyValue") \
      ) \
      .addChild(ROUTEObject() \
       .setFromNode("NodePosition") \
       .setFromField("value_changed") \
       .setToNode("transform") \
       .setToField("set_translation") \
      ) \
     ) \
    ) \
    .addChild(ProtoDeclareObject() \
     .setName("cylinder") \
     .setProtoInterface(ProtoInterfaceObject() \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFVEC3F) \
       .setName("positionA") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTONLY) \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFVEC3F) \
       .setName("positionB") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTONLY) \
      ) \
     ) \
     .setProtoBody(ProtoBodyObject() \
      .addChild(ShapeObject() \
       .setGeometry(ExtrusionObject() \
        .setDEF("extrusion") \
        .setCreaseAngle(0.785) \
        .setCrossSection([1,0,0.92,-0.38,0.71,-0.71,0.38,-0.92,0,-1,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1,0,-0.92,0.38,-0.71,0.71,-0.38,0.92,0,1,0.38,0.92,0.71,0.71,0.92,0.38,1,0]) \
        .setSpine([0,-50,0,0,0,0,0,50,0]) \
       ) \
       .setAppearance(AppearanceObject() \
        .setMaterial(MaterialObject() \
         .setDiffuseColor([0,1,0]) \
        ) \
       ) \
      ) \
      .addChild(ScriptObject() \
       .setDEF("MoveCylinder") \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_MFVEC3F) \
        .setName("spine") \
        .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
        .setValue("0 -50 0 0 0 0 0 50 0") \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFVEC3F) \
        .setName("set_endA") \
        .setAccessType(fieldObject.ACCESSTYPE_INPUTONLY) \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFVEC3F) \
        .setName("set_endB") \
        .setAccessType(fieldObject.ACCESSTYPE_INPUTONLY) \
       ) \
       .setIS(ISObject() \
        .addConnect(connectObject() \
         .setNodeField("set_endA") \
         .setProtoField("positionA") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("set_endB") \
         .setProtoField("positionB") \
        ) \
       ) \
       .setSourceCode('''ecmascript:\n"+
"\n"+
"                function set_endA(value) {\n"+
"		    if (typeof spine === \"undefined\") {\n"+
"		        spine = new MFVec3f([value, value]);\n"+
"		    } else {\n"+
"		        spine = new MFVec3f([value, spine[1]]);\n"+
"		    }\n"+
"                }\n"+
"\n"+
"                function set_endB(value) {\n"+
"		    if (typeof spine === \"undefined\") {\n"+
"		        spine = new MFVec3f([value, value]);\n"+
"		    } else {\n"+
"		        spine = new MFVec3f([spine[0], value]);\n"+
"		    }\n"+
"                }\n"+
"\n"+
"                function set_spine(value) {\n"+
"		    Browser.print('\\n'+'\"');\n"+
"                    spine = value;\n"+
"                }''')
      ) \
      .addChild(ROUTEObject() \
       .setFromNode("MoveCylinder") \
       .setFromField("spine") \
       .setToNode("extrusion") \
       .setToField("set_spine") \
      ) \
     ) \
    ) \
    .addChild(TransformObject() \
     .setScale([0.1,0.1,0.1]) \
     .addChild(ProtoInstanceObject() \
      .setName("node") \
      .setDEF("nodeA") \
      .addFieldValue(fieldValueObject() \
       .setName("position") \
       .setValue("-50 -50 -50") \
      ) \
     ) \
     .addChild(ProtoInstanceObject() \
      .setName("node") \
      .setDEF("nodeB") \
      .addFieldValue(fieldValueObject() \
       .setName("position") \
       .setValue("50 50 50") \
      ) \
     ) \
     .addChild(ProtoInstanceObject() \
      .setName("cylinder") \
      .setDEF("linkA") \
      .addFieldValue(fieldValueObject() \
       .setName("positionA") \
       .setValue("0 0 0") \
      ) \
      .addFieldValue(fieldValueObject() \
       .setName("positionB") \
       .setValue("50 50 50") \
      ) \
     ) \
    ) \
    .addChild(ROUTEObject() \
     .setFromNode("nodeA") \
     .setFromField("position") \
     .setToNode("linkA") \
     .setToField("positionA") \
    ) \
    .addChild(ROUTEObject() \
     .setFromNode("nodeB") \
     .setFromField("position") \
     .setToNode("linkA") \
     .setToField("positionB") \
    ) \
   ) \

X3D0.toFileX3D("./future/./fors2.newf.x3d")
