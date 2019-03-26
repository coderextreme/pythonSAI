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
     .setContent("x3dconnectorProto") \
    ) \
    .addMeta(metaObject() \
     .setName("creator") \
     .setContent("Lost, Doug Sanden I think") \
    ) \
    .addMeta(metaObject() \
     .setName("generator") \
     .setContent("manual") \
    ) \
    .addMeta(metaObject() \
     .setName("identifier") \
     .setContent("https://coderextreme.net/X3DJSONLD/x3dconnectorProto.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("description") \
     .setContent("a generic proto to connect two objects") \
    ) \
   ) \
   .setScene(SceneObject() \
    .addChildren(ViewpointObject() \
     .setPosition([0,0,5]) \
     .setDescription("Only Viewpoint") \
    ) \
    .addChildren(BackgroundObject() \
     .setSkyColor([0.4,0.4,0.4]) \
    ) \
    .addChildren(TransformObject() \
     .setDEF("DECLpoint_G1_node") \
     .addChildren(ShapeObject() \
      .setGeometry(SphereObject(radius = 0.1) \
      ) \
      .setAppearance(AppearanceObject() \
       .setMaterial(MaterialObject() \
        .setDiffuseColor([1,0,0]) \
       ) \
      ) \
     ) \
     .addChildren(PositionInterpolatorObject() \
      .setDEF("DECLpoint_G1_PI1") \
      .setKey([0,1]) \
      .setKeyValue([0,0,0,0,5,0]) \
     ) \
     .addChildren(ScriptObject() \
      .setDEF("DECLpoint_G1_MB1") \
      .addField(fieldObject() \
       .setName("translation") \
       .setAccessType("inputOutput") \
       .setType("SFVec3f") \
       .setValue("0 0 0") \
      ) \
      .addField(fieldObject() \
       .setName("old") \
       .setAccessType("inputOutput") \
       .setType("SFVec3f") \
       .setValue("0 0 0") \
      ) \
      .addField(fieldObject() \
       .setName("set_location") \
       .setAccessType("inputOnly") \
       .setType("SFTime") \
      ) \
      .addField(fieldObject() \
       .setName("keyValue") \
       .setAccessType("inputOutput") \
       .setType("MFVec3f") \
       .setValue("0 0 0 0 5 0") \
      ) \
.setSourceCode('''ecmascript:\n"+
"		function set_location(value) {\n"+
"                    old = translation;\n"+
"		    translation = new SFVec3f(Math.random()*10-5, Math.random()*10-5, Math.random()*10-5);\n"+
"                    keyValue = new MFVec3f([old, translation]);\n"+
"		    // Browser.println(keyValue);\n"+
"		}''')
     ) \
     .addChildren(TimeSensorObject() \
      .setDEF("DECLpoint_G1_CL1") \
      .setCycleInterval(3) \
      .setLoop(True) \
     ) \
     .addChildren(ROUTEObject() \
      .setFromNode("DECLpoint_G1_CL1") \
      .setFromField("cycleTime") \
      .setToNode("DECLpoint_G1_MB1") \
      .setToField("set_location") \
     ) \
     .addChildren(ROUTEObject() \
      .setFromNode("DECLpoint_G1_CL1") \
      .setFromField("fraction_changed") \
      .setToNode("DECLpoint_G1_PI1") \
      .setToField("set_fraction") \
     ) \
     .addChildren(ROUTEObject() \
      .setFromNode("DECLpoint_G1_MB1") \
      .setFromField("keyValue") \
      .setToNode("DECLpoint_G1_PI1") \
      .setToField("keyValue") \
     ) \
     .addChildren(ROUTEObject() \
      .setFromNode("DECLpoint_G1_PI1") \
      .setFromField("value_changed") \
      .setToNode("DECLpoint_G1_node") \
      .setToField("set_translation") \
     ) \
    ) \
    .addChildren(TransformObject() \
     .setDEF("DECLpoint_G2_node") \
     .addChildren(ShapeObject() \
      .setGeometry(SphereObject(radius = 0.1) \
      ) \
      .setAppearance(AppearanceObject() \
       .setMaterial(MaterialObject() \
        .setDiffuseColor([1,0,0]) \
       ) \
      ) \
     ) \
     .addChildren(PositionInterpolatorObject() \
      .setDEF("DECLpoint_G2_PI1") \
      .setKey([0,1]) \
      .setKeyValue([0,0,0,0,5,0]) \
     ) \
     .addChildren(ScriptObject() \
      .setDEF("DECLpoint_G2_MB1") \
      .addField(fieldObject() \
       .setName("translation") \
       .setAccessType("inputOutput") \
       .setType("SFVec3f") \
       .setValue("0 0 0") \
      ) \
      .addField(fieldObject() \
       .setName("old") \
       .setAccessType("inputOutput") \
       .setType("SFVec3f") \
       .setValue("0 0 0") \
      ) \
      .addField(fieldObject() \
       .setName("set_location") \
       .setAccessType("inputOnly") \
       .setType("SFTime") \
      ) \
      .addField(fieldObject() \
       .setName("keyValue") \
       .setAccessType("inputOutput") \
       .setType("MFVec3f") \
       .setValue("0 0 0 0 5 0") \
      ) \
.setSourceCode('''ecmascript:\n"+
"		function set_location(value) {\n"+
"                    old = translation;\n"+
"		    translation = new SFVec3f(Math.random()*10-5, Math.random()*10-5, Math.random()*10-5);\n"+
"                    keyValue = new MFVec3f([old, translation]);\n"+
"		    // Browser.println(keyValue);\n"+
"		}''')
     ) \
     .addChildren(TimeSensorObject() \
      .setDEF("DECLpoint_G2_CL1") \
      .setCycleInterval(3) \
      .setLoop(True) \
     ) \
     .addChildren(ROUTEObject() \
      .setFromNode("DECLpoint_G2_CL1") \
      .setFromField("cycleTime") \
      .setToNode("DECLpoint_G2_MB1") \
      .setToField("set_location") \
     ) \
     .addChildren(ROUTEObject() \
      .setFromNode("DECLpoint_G2_CL1") \
      .setFromField("fraction_changed") \
      .setToNode("DECLpoint_G2_PI1") \
      .setToField("set_fraction") \
     ) \
     .addChildren(ROUTEObject() \
      .setFromNode("DECLpoint_G2_MB1") \
      .setFromField("keyValue") \
      .setToNode("DECLpoint_G2_PI1") \
      .setToField("keyValue") \
     ) \
     .addChildren(ROUTEObject() \
      .setFromNode("DECLpoint_G2_PI1") \
      .setFromField("value_changed") \
      .setToNode("DECLpoint_G2_node") \
      .setToField("set_translation") \
     ) \
    ) \
    .addChildren(GroupObject() \
     .addChildren(TransformObject() \
      .setDEF("DECLx3dconnector_connector1_trans") \
      .addChildren(TransformObject() \
       .setDEF("DECLx3dconnector_connector1_rotscale") \
       .addChildren(ShapeObject() \
        .setAppearance(AppearanceObject() \
         .setMaterial(MaterialObject() \
          .setDiffuseColor([0.2,0.7,0.7]) \
          .setTransparency(0.5) \
         ) \
        ) \
        .setGeometry(CylinderObject(radius = 0.05) \
        ) \
       ) \
      ) \
     ) \
     .addChildren(ScriptObject() \
      .setDEF("DECLx3dconnector_connector1_S1") \
      .addField(fieldObject() \
       .setName("startnode") \
       .setAccessType("initializeOnly") \
       .setType("SFNode") \
       .addChildren(GroupObject() \
        .setUSE("DECLpoint_G1_node") \
       ) \
      ) \
      .addField(fieldObject() \
       .setName("endnode") \
       .setAccessType("initializeOnly") \
       .setType("SFNode") \
       .addChildren(GroupObject() \
        .setUSE("DECLpoint_G2_node") \
       ) \
      ) \
      .addField(fieldObject() \
       .setName("position") \
       .setAccessType("inputOutput") \
       .setType("SFNode") \
       .addChildren(TransformObject() \
        .setUSE("DECLx3dconnector_connector1_trans") \
       ) \
      ) \
      .addField(fieldObject() \
       .setName("rotscale") \
       .setAccessType("inputOutput") \
       .setType("SFNode") \
       .addChildren(TransformObject() \
        .setUSE("DECLx3dconnector_connector1_rotscale") \
       ) \
      ) \
      .addField(fieldObject() \
       .setName("set_startpoint") \
       .setAccessType("inputOnly") \
       .setType("SFVec3f") \
      ) \
      .addField(fieldObject() \
       .setName("set_endpoint") \
       .setAccessType("inputOnly") \
       .setType("SFVec3f") \
      ) \
.setSourceCode('''ecmascript:\n"+
"        function recompute(startpoint,endpoint){\n"+
"	    if (typeof endpoint === 'undefined') {\n"+
"		return;\n"+
"	    }\n"+
"            var dif = endpoint.subtract(startpoint);\n"+
"            var dist = dif.length()*0.5;\n"+
"            var dif2 = dif.multiply(0.5);\n"+
"            var norm = dif.normalize();\n"+
"            var transl = startpoint.add(dif2);\n"+
"	    if (typeof Quaternion !== 'undefined') {\n"+
"		    return {\n"+
"			    scale : new SFVec3f(1.0,dist,1.0),\n"+
"			    translation : transl,\n"+
"			    rotation : new Quaternion.rotateFromTo(new SFVec3f(0.0,1.0,0.0), norm)\n"+
"		    };\n"+
"	    } else if (typeof SFRotation !== 'undefined') {\n"+
"		    return {\n"+
"			    scale : new SFVec3f(1.0,dist,1.0),\n"+
"			    translation : transl,\n"+
"			    rotation : new SFRotation(new SFVec3f(0.0,1.0,0.0),norm)\n"+
"		    };\n"+
"	    } else {\n"+
"		    return {\n"+
"			    scale : new SFVec3f(1.0,dist,1.0),\n"+
"			    translation : transl\n"+
"		    };\n"+
"	    }\n"+
"	}\n"+
"	function recompute_and_route(startpoint, endpoint) {\n"+
"	      var trafo = recompute(startpoint, endpoint);\n"+
"	      position.translation = trafo.translation;\n"+
"	      rotscale.rotation = trafo.rotation;\n"+
"	      rotscale.scale = trafo.scale;\n"+
"	}\n"+
"        function initialize(){\n"+
"            recompute_and_route(startnode.translation,endnode.translation);\n"+
"        }\n"+
"        function set_startpoint(val,t){\n"+
"            recompute_and_route(val,endnode.translation);\n"+
"        }\n"+
"        function set_endpoint(val,t){\n"+
"            recompute_and_route(startnode.translation,val);\n"+
"        }''')
     ) \
    ) \
    .addChildren(ROUTEObject() \
     .setFromNode("DECLpoint_G1_node") \
     .setFromField("translation") \
     .setToNode("DECLx3dconnector_connector1_S1") \
     .setToField("set_startpoint") \
    ) \
    .addChildren(ROUTEObject() \
     .setFromNode("DECLpoint_G2_node") \
     .setFromField("translation") \
     .setToNode("DECLx3dconnector_connector1_S1") \
     .setToField("set_endpoint") \
    ) \
   ) \

X3D0.toFileX3D("./future/./arc3.newf.x3d")
