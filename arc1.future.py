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
    .addChildren(ProtoDeclareObject() \
     .setName("point") \
     .setProtoInterface(ProtoInterfaceObject() \
      .addField(fieldObject() \
       .setName("translation") \
       .setAccessType("inputOutput") \
       .setType("SFVec3f") \
       .setValue("0 0 0") \
      ) \
     ) \
     .setProtoBody(ProtoBodyObject() \
      .addChildren(TransformObject() \
       .setDEF("node") \
       .setIS(ISObject() \
        .addConnect(connectObject() \
         .setNodeField("translation") \
         .setProtoField("translation") \
        ) \
       ) \
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
        .setDEF("PI1") \
        .setKey([0,1]) \
        .setKeyValue([0,0,0,0,5,0]) \
       ) \
       .addChildren(ScriptObject() \
        .setDEF("MB1") \
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
        .setDEF("CL1") \
        .setCycleInterval(3) \
        .setLoop(True) \
       ) \
       .addChildren(ROUTEObject() \
        .setFromNode("CL1") \
        .setFromField("cycleTime") \
        .setToNode("MB1") \
        .setToField("set_location") \
       ) \
       .addChildren(ROUTEObject() \
        .setFromNode("CL1") \
        .setFromField("fraction_changed") \
        .setToNode("PI1") \
        .setToField("set_fraction") \
       ) \
       .addChildren(ROUTEObject() \
        .setFromNode("MB1") \
        .setFromField("keyValue") \
        .setToNode("PI1") \
        .setToField("keyValue") \
       ) \
       .addChildren(ROUTEObject() \
        .setFromNode("PI1") \
        .setFromField("value_changed") \
        .setToNode("node") \
        .setToField("set_translation") \
       ) \
      ) \
     ) \
    ) \
    .addChildren(ProtoDeclareObject() \
     .setName("x3dconnector") \
     .setProtoInterface(ProtoInterfaceObject() \
      .addField(fieldObject() \
       .setName("startnode") \
       .setAccessType("initializeOnly") \
       .setType("SFNode") \
      ) \
      .addField(fieldObject() \
       .setName("endnode") \
       .setAccessType("initializeOnly") \
       .setType("SFNode") \
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
     ) \
     .setProtoBody(ProtoBodyObject() \
      .addChildren(GroupObject() \
       .addChildren(TransformObject() \
        .setDEF("trans") \
        .addChildren(TransformObject() \
         .setDEF("rotscale") \
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
        .setDEF("S1") \
        .addField(fieldObject() \
         .setName("startnode") \
         .setAccessType("initializeOnly") \
         .setType("SFNode") \
        ) \
        .addField(fieldObject() \
         .setName("endnode") \
         .setAccessType("initializeOnly") \
         .setType("SFNode") \
        ) \
        .addField(fieldObject() \
         .setName("position") \
         .setAccessType("inputOutput") \
         .setType("SFNode") \
         .addChildren(TransformObject() \
          .setUSE("trans") \
         ) \
        ) \
        .addField(fieldObject() \
         .setName("rotscale") \
         .setAccessType("inputOutput") \
         .setType("SFNode") \
         .addChildren(TransformObject() \
          .setUSE("rotscale") \
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
        .setIS(ISObject() \
         .addConnect(connectObject() \
          .setNodeField("startnode") \
          .setProtoField("startnode") \
         ) \
         .addConnect(connectObject() \
          .setNodeField("endnode") \
          .setProtoField("endnode") \
         ) \
         .addConnect(connectObject() \
          .setNodeField("set_startpoint") \
          .setProtoField("set_startpoint") \
         ) \
         .addConnect(connectObject() \
          .setNodeField("set_endpoint") \
          .setProtoField("set_endpoint") \
         ) \
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
     ) \
    ) \
    .addChildren(ProtoInstanceObject() \
     .setName("point") \
     .setDEF("G1") \
    ) \
    .addChildren(ProtoInstanceObject() \
     .setName("point") \
     .setDEF("G2") \
    ) \
    .addChildren(ProtoInstanceObject() \
     .setName("x3dconnector") \
     .setDEF("connector1") \
     .addFieldValue(fieldValueObject() \
      .setName("startnode") \
      .addChildren(ProtoInstanceObject() \
       .setUSE("G1") \
      ) \
     ) \
     .addFieldValue(fieldValueObject() \
      .setName("endnode") \
      .addChildren(ProtoInstanceObject() \
       .setUSE("G2") \
      ) \
     ) \
     .addFieldValue(fieldValueObject() \
      .setName("set_startpoint") \
     ) \
     .addFieldValue(fieldValueObject() \
      .setName("set_endpoint") \
     ) \
    ) \
    .addChildren(ROUTEObject() \
     .setFromNode("G1") \
     .setFromField("translation") \
     .setToNode("connector1") \
     .setToField("set_startpoint") \
    ) \
    .addChildren(ROUTEObject() \
     .setFromNode("G2") \
     .setFromField("translation") \
     .setToNode("connector1") \
     .setToField("set_endpoint") \
    ) \
   ) \

X3D0.toFileX3D("./future/./arc1.newf.x3d")
