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
     .setContent("force.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("identifier") \
     .setContent("https://coderextreme.net/X3DJSONLD/force.x3d") \
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
      .addChild(GroupObject() \
       .addChild(TransformObject() \
        .setDEF("transform") \
        .setIS(ISObject() \
         .addConnect(connectObject() \
          .setNodeField("translation") \
          .setProtoField("position") \
         ) \
        ) \
        .addChild(ShapeObject() \
         .setGeometry(SphereObject() \
         ) \
         .setAppearance(AppearanceObject() \
          .setMaterial(MaterialObject() \
           .setDiffuseColor([1,0,0]) \
          ) \
         ) \
        ) \
        .addChild(TransformObject() \
         .setTranslation([1,0,0]) \
         .addChild(ShapeObject() \
          .setGeometry(TextObject() \
           .setString(["Node"]) \
           .setFontStyle(FontStyleObject() \
            .setJustify(["MIDDLE","MIDDLE"]) \
            .setSize(5) \
           ) \
          ) \
          .setAppearance(AppearanceObject() \
           .setMaterial(MaterialObject() \
            .setDiffuseColor([0,0,1]) \
           ) \
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
    ) \
    .addChild(ProtoDeclareObject() \
     .setName("cylinder") \
     .setProtoInterface(ProtoInterfaceObject() \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFVEC3F) \
       .setName("set_positionA") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTONLY) \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFVEC3F) \
       .setName("set_positionB") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTONLY) \
      ) \
     ) \
     .setProtoBody(ProtoBodyObject() \
      .addChild(GroupObject() \
       .addChild(ShapeObject() \
        .setGeometry(ExtrusionObject() \
         .setDEF("extrusion") \
         .setCreaseAngle(0.785) \
         .setCrossSection([1,0,0.92,-0.38,0.71,-0.71,0.38,-0.92,0,-1,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1,0,-0.92,0.38,-0.71,0.71,-0.38,0.92,0,1,0.38,0.92,0.71,0.71,0.92,0.38,1,0]) \
         .setSpine([0,-50,0,0,50,0]) \
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
         .setValue("0 -50 0 0 50 0") \
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
          .setProtoField("set_positionA") \
         ) \
         .addConnect(connectObject() \
          .setNodeField("set_endB") \
          .setProtoField("set_positionB") \
         ) \
        ) \
.setSourceCode('''ecmascript:\n"+
"\n"+
"                function set_endA(value) {\n"+
"		    if (typeof spine === 'undefined') {\n"+
"		        spine = new MFVec3f([value, value]);\n"+
"		    } else {\n"+
"		        spine = new MFVec3f([value, spine[1]]);\n"+
"		    }\n"+
"                }\n"+
"\n"+
"                function set_endB(value) {\n"+
"		    if (typeof spine === 'undefined') {\n"+
"		        spine = new MFVec3f([value, value]);\n"+
"		    } else {\n"+
"		        spine = new MFVec3f([spine[0], value]);\n"+
"		    }\n"+
"                }\n"+
"\n"+
"                function set_spine(value) {\n"+
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
    ) \
    .addChild(TransformObject() \
     .setDEF("HoldsContent") \
     .setScale([0.1,0.1,0.1]) \
     .addChild(PlaneSensorObject() \
      .setDEF("clickGenerator") \
      .setMinPosition([-50,-50]) \
      .setMaxPosition([50,50]) \
      .setDescription("click on background to add nodes, click on nodes to add links") \
     ) \
     .addChild(ProtoInstanceObject() \
      .setName("node") \
      .setDEF("nodeA") \
      .addFieldValue(fieldValueObject() \
       .setName("position") \
       .setValue("0 0 0") \
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
      .setName("node") \
      .setDEF("nodeC") \
      .addFieldValue(fieldValueObject() \
       .setName("position") \
       .setValue("-50 -50 -50") \
      ) \
     ) \
     .addChild(ProtoInstanceObject() \
      .setName("node") \
      .setDEF("nodeD") \
      .addFieldValue(fieldValueObject() \
       .setName("position") \
       .setValue("50 50 -50") \
      ) \
     ) \
     .addChild(ProtoInstanceObject() \
      .setName("cylinder") \
      .setDEF("linkA") \
      .addFieldValue(fieldValueObject() \
       .setName("set_positionA") \
       .setValue("0 0 0") \
      ) \
      .addFieldValue(fieldValueObject() \
       .setName("set_positionB") \
       .setValue("50 50 50") \
      ) \
     ) \
     .addChild(ProtoInstanceObject() \
      .setName("cylinder") \
      .setDEF("linkB") \
      .addFieldValue(fieldValueObject() \
       .setName("set_positionA") \
       .setValue("0 0 0") \
      ) \
      .addFieldValue(fieldValueObject() \
       .setName("set_positionB") \
       .setValue("-50 -50 -50") \
      ) \
     ) \
     .addChild(ProtoInstanceObject() \
      .setName("cylinder") \
      .setDEF("linkC") \
      .addFieldValue(fieldValueObject() \
       .setName("set_positionA") \
       .setValue("50 50 50") \
      ) \
      .addFieldValue(fieldValueObject() \
       .setName("set_positionB") \
       .setValue("50 50 -50") \
      ) \
     ) \
    ) \
    .addChild(ScriptObject() \
     .setDEF("clickHandler") \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFINT32) \
      .setName("counter") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
      .setValue("0") \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFNODE) \
      .setName("node_changed") \
      .setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY) \
     ) \
     .addField(fieldObject() \
      .setType(fieldObject.TYPE_SFBOOL) \
      .setName("add_node") \
      .setAccessType(fieldObject.ACCESSTYPE_INPUTONLY) \
      .setValue("false") \
     ) \
.addComments(CommentsBlock("""<field name=\"ModifiableNode\" type=\"SFNode\" accessType=\"inputOutput\"> <Transform USE=\"HoldsContent\"/> </field>""")) \
.setSourceCode('''ecmascript:\n"+
"	function add_node(value) {\n"+
"                // Browser.print('hey ', counter);\n"+
"                counter = counter++;\n"+
"		Browser.appendTo(Browser.getDocument().querySelector(\"field [name=ModifiableNode]\"),\n"+
"			{ \"ProtoInstance\":\n"+
"				{ \"@name\":\"node\",\n"+
"				  \"@DEF\":\"node'+counter+'\",\n"+
"				  \"fieldValue\": [\n"+
"					{\n"+
"						 \"@name\":\"position\",\n"+
"						 \"@value\":[0.0,0.0,0.0]\n"+
"					}\n"+
"				  ]\n"+
"				}\n"+
"			});\n"+
"\n"+
"        }''')
    ) \
    .addChild(ROUTEObject() \
     .setFromNode("clickGenerator") \
     .setFromField("isActive") \
     .setToNode("clickHandler") \
     .setToField("add_node") \
    ) \
    .addChild(ROUTEObject() \
     .setFromNode("nodeA") \
     .setFromField("position") \
     .setToNode("linkA") \
     .setToField("set_positionA") \
    ) \
    .addChild(ROUTEObject() \
     .setFromNode("nodeB") \
     .setFromField("position") \
     .setToNode("linkA") \
     .setToField("set_positionB") \
    ) \
    .addChild(ROUTEObject() \
     .setFromNode("nodeA") \
     .setFromField("position") \
     .setToNode("linkB") \
     .setToField("set_positionA") \
    ) \
    .addChild(ROUTEObject() \
     .setFromNode("nodeC") \
     .setFromField("position") \
     .setToNode("linkB") \
     .setToField("set_positionB") \
    ) \
    .addChild(ROUTEObject() \
     .setFromNode("nodeA") \
     .setFromField("position") \
     .setToNode("linkC") \
     .setToField("set_positionA") \
    ) \
    .addChild(ROUTEObject() \
     .setFromNode("nodeD") \
     .setFromField("position") \
     .setToNode("linkC") \
     .setToField("set_positionB") \
    ) \
   ) \

X3D0.toFileX3D("./future/./force.newf.x3d")
