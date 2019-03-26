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
    .addChildren(ProtoDeclareObject() \
     .setName("node") \
     .setProtoInterface(ProtoInterfaceObject() \
      .addField(fieldObject() \
       .setName("position") \
       .setAccessType("inputOutput") \
       .setType("SFVec3f") \
       .setValue("0 0 0") \
      ) \
     ) \
     .setProtoBody(ProtoBodyObject() \
      .addChildren(GroupObject() \
       .addChildren(TransformObject() \
        .setDEF("transform") \
        .setIS(ISObject() \
         .addConnect(connectObject() \
          .setNodeField("translation") \
          .setProtoField("position") \
         ) \
        ) \
        .addChildren(ShapeObject() \
         .setGeometry(SphereObject() \
         ) \
         .setAppearance(AppearanceObject() \
          .setMaterial(MaterialObject() \
           .setDiffuseColor([1,0,0]) \
          ) \
         ) \
        ) \
        .addChildren(TransformObject() \
         .setTranslation([1,0,0]) \
         .addChildren(ShapeObject() \
          .setGeometry(TextObject() \
           .setString(["Node"]) \
           .setFontStyle(FontStyleObject(justify = ["MIDDLE","MIDDLE"], size = 5) \
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
       .addChildren(PositionInterpolatorObject() \
        .setDEF("NodePosition") \
        .setKey([0,1]) \
        .setKeyValue([0,0,0,0,5,0]) \
       ) \
       .addChildren(ScriptObject() \
        .setDEF("MoveBall") \
        .addField(fieldObject() \
         .setName("translation") \
         .setAccessType("inputOutput") \
         .setType("SFVec3f") \
         .setValue("50 50 0") \
        ) \
        .addField(fieldObject() \
         .setName("old") \
         .setAccessType("inputOutput") \
         .setType("SFVec3f") \
         .setValue("0 0 0") \
        ) \
        .addField(fieldObject() \
         .setName("set_cycle") \
         .setAccessType("inputOnly") \
         .setType("SFTime") \
        ) \
        .addField(fieldObject() \
         .setName("keyValue") \
         .setAccessType("outputOnly") \
         .setType("MFVec3f") \
        ) \
.setSourceCode('''ecmascript:\n"+
"					function set_cycle(value) {\n"+
"                                                old = translation;\n"+
"						translation = new SFVec3f(Math.random()*100-50, Math.random()*100-50, Math.random()*100-50);\n"+
"                                                keyValue = new MFVec3f([old, translation]);\n"+
"						// Browser.println(translation);\n"+
"					}''')
       ) \
       .addChildren(TimeSensorObject() \
        .setDEF("nodeClock") \
        .setCycleInterval(3) \
        .setLoop(True) \
       ) \
       .addChildren(ROUTEObject() \
        .setFromNode("nodeClock") \
        .setFromField("cycleTime") \
        .setToNode("MoveBall") \
        .setToField("set_cycle") \
       ) \
       .addChildren(ROUTEObject() \
        .setFromNode("nodeClock") \
        .setFromField("fraction_changed") \
        .setToNode("NodePosition") \
        .setToField("set_fraction") \
       ) \
       .addChildren(ROUTEObject() \
        .setFromNode("MoveBall") \
        .setFromField("keyValue") \
        .setToNode("NodePosition") \
        .setToField("keyValue") \
       ) \
       .addChildren(ROUTEObject() \
        .setFromNode("NodePosition") \
        .setFromField("value_changed") \
        .setToNode("transform") \
        .setToField("set_translation") \
       ) \
      ) \
     ) \
    ) \
    .addChildren(ProtoDeclareObject() \
     .setName("cylinder") \
     .setProtoInterface(ProtoInterfaceObject() \
      .addField(fieldObject() \
       .setName("set_positionA") \
       .setAccessType("inputOnly") \
       .setType("SFVec3f") \
      ) \
      .addField(fieldObject() \
       .setName("set_positionB") \
       .setAccessType("inputOnly") \
       .setType("SFVec3f") \
      ) \
     ) \
     .setProtoBody(ProtoBodyObject() \
      .addChildren(GroupObject() \
       .addChildren(ShapeObject() \
        .setGeometry(ExtrusionObject(creaseAngle = 0.785, crossSection = [1,0,0.92,-0.38,0.71,-0.71,0.38,-0.92,0,-1,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1,0,-0.92,0.38,-0.71,0.71,-0.38,0.92,0,1,0.38,0.92,0.71,0.71,0.92,0.38,1,0], spine = [0,-50,0,0,50,0]) \
         .setDEF("extrusion") \
        ) \
        .setAppearance(AppearanceObject() \
         .setMaterial(MaterialObject() \
          .setDiffuseColor([0,1,0]) \
         ) \
        ) \
       ) \
       .addChildren(ScriptObject() \
        .setDEF("MoveCylinder") \
        .addField(fieldObject() \
         .setName("spine") \
         .setAccessType("inputOutput") \
         .setType("MFVec3f") \
         .setValue("0 -50 0 0 50 0") \
        ) \
        .addField(fieldObject() \
         .setName("set_endA") \
         .setAccessType("inputOnly") \
         .setType("SFVec3f") \
        ) \
        .addField(fieldObject() \
         .setName("set_endB") \
         .setAccessType("inputOnly") \
         .setType("SFVec3f") \
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
       .addChildren(ROUTEObject() \
        .setFromNode("MoveCylinder") \
        .setFromField("spine") \
        .setToNode("extrusion") \
        .setToField("set_spine") \
       ) \
      ) \
     ) \
    ) \
    .addChildren(TransformObject() \
     .setDEF("HoldsContent") \
     .setScale([0.1,0.1,0.1]) \
     .addChildren(PlaneSensorObject() \
      .setDEF("clickGenerator") \
      .setMinPosition([-50,-50]) \
      .setMaxPosition([50,50]) \
      .setDescription("click on background to add nodes, click on nodes to add links") \
     ) \
     .addChildren(ProtoInstanceObject() \
      .setName("node") \
      .setDEF("nodeA") \
      .addFieldValue(fieldValueObject() \
       .setName("position") \
       .setValue("0 0 0") \
      ) \
     ) \
     .addChildren(ProtoInstanceObject() \
      .setName("node") \
      .setDEF("nodeB") \
      .addFieldValue(fieldValueObject() \
       .setName("position") \
       .setValue("50 50 50") \
      ) \
     ) \
     .addChildren(ProtoInstanceObject() \
      .setName("node") \
      .setDEF("nodeC") \
      .addFieldValue(fieldValueObject() \
       .setName("position") \
       .setValue("-50 -50 -50") \
      ) \
     ) \
     .addChildren(ProtoInstanceObject() \
      .setName("node") \
      .setDEF("nodeD") \
      .addFieldValue(fieldValueObject() \
       .setName("position") \
       .setValue("50 50 -50") \
      ) \
     ) \
     .addChildren(ProtoInstanceObject() \
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
     .addChildren(ProtoInstanceObject() \
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
     .addChildren(ProtoInstanceObject() \
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
    .addChildren(ScriptObject() \
     .setDEF("clickHandler") \
     .addField(fieldObject() \
      .setName("counter") \
      .setAccessType("inputOutput") \
      .setValue("0") \
      .setType("SFInt32") \
     ) \
     .addField(fieldObject() \
      .setName("node_changed") \
      .setAccessType("outputOnly") \
      .setType("SFNode") \
     ) \
     .addField(fieldObject() \
      .setName("add_node") \
      .setAccessType("inputOnly") \
      .setValue("false") \
      .setType("SFBool") \
     ) \
#<field name=\"ModifiableNode\" type=\"SFNode\" accessType=\"inputOutput\"> <Transform USE=\"HoldsContent\"/> </field>
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
    .addChildren(ROUTEObject() \
     .setFromNode("clickGenerator") \
     .setFromField("isActive") \
     .setToNode("clickHandler") \
     .setToField("add_node") \
    ) \
    .addChildren(ROUTEObject() \
     .setFromNode("nodeA") \
     .setFromField("position") \
     .setToNode("linkA") \
     .setToField("set_positionA") \
    ) \
    .addChildren(ROUTEObject() \
     .setFromNode("nodeB") \
     .setFromField("position") \
     .setToNode("linkA") \
     .setToField("set_positionB") \
    ) \
    .addChildren(ROUTEObject() \
     .setFromNode("nodeA") \
     .setFromField("position") \
     .setToNode("linkB") \
     .setToField("set_positionA") \
    ) \
    .addChildren(ROUTEObject() \
     .setFromNode("nodeC") \
     .setFromField("position") \
     .setToNode("linkB") \
     .setToField("set_positionB") \
    ) \
    .addChildren(ROUTEObject() \
     .setFromNode("nodeA") \
     .setFromField("position") \
     .setToNode("linkC") \
     .setToField("set_positionA") \
    ) \
    .addChildren(ROUTEObject() \
     .setFromNode("nodeD") \
     .setFromField("position") \
     .setToNode("linkC") \
     .setToField("set_positionB") \
    ) \
   ) \

X3D0.toFileX3D("./future/./force.newf.x3d")
