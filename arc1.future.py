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
    .addChild(ViewpointObject() \
     .setPosition([0,0,5]) \
     .setDescription("Only Viewpoint") \
    ) \
    .addChild(BackgroundObject() \
     .setSkyColor([0.4,0.4,0.4]) \
    ) \
    .addChild(ProtoDeclareObject() \
     .setName("point") \
     .setProtoInterface(ProtoInterfaceObject() \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFVEC3F) \
       .setName("translation") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
       .setValue("0 0 0") \
      ) \
     ) \
     .setProtoBody(ProtoBodyObject() \
      .addChild(TransformObject() \
       .setDEF("node") \
       .setIS(ISObject() \
        .addConnect(connectObject() \
         .setNodeField("translation") \
         .setProtoField("translation") \
        ) \
       ) \
       .addChild(ShapeObject() \
        .setGeometry(SphereObject() \
         .setRadius(0.1) \
        ) \
        .setAppearance(AppearanceObject() \
         .setMaterial(MaterialObject() \
          .setDiffuseColor([1,0,0]) \
         ) \
        ) \
       ) \
       .addChild(PositionInterpolatorObject() \
        .setDEF("PI1") \
        .setKey([0,1]) \
        .setKeyValue([0,0,0,0,5,0]) \
       ) \
       .addChild(ScriptObject() \
        .setDEF("MB1") \
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
         .setName("set_location") \
         .setAccessType(fieldObject.ACCESSTYPE_INPUTONLY) \
        ) \
        .addField(fieldObject() \
         .setType(fieldObject.TYPE_MFVEC3F) \
         .setName("keyValue") \
         .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
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
       .addChild(TimeSensorObject() \
        .setDEF("CL1") \
        .setCycleInterval(3) \
        .setLoop(True) \
       ) \
       .addChild(ROUTEObject() \
        .setFromNode("CL1") \
        .setFromField("cycleTime") \
        .setToNode("MB1") \
        .setToField("set_location") \
       ) \
       .addChild(ROUTEObject() \
        .setFromNode("CL1") \
        .setFromField("fraction_changed") \
        .setToNode("PI1") \
        .setToField("set_fraction") \
       ) \
       .addChild(ROUTEObject() \
        .setFromNode("MB1") \
        .setFromField("keyValue") \
        .setToNode("PI1") \
        .setToField("keyValue") \
       ) \
       .addChild(ROUTEObject() \
        .setFromNode("PI1") \
        .setFromField("value_changed") \
        .setToNode("node") \
        .setToField("set_translation") \
       ) \
      ) \
     ) \
    ) \
    .addChild(ProtoDeclareObject() \
     .setName("x3dconnector") \
     .setProtoInterface(ProtoInterfaceObject() \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFNODE) \
       .setName("startnode") \
       .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFNODE) \
       .setName("endnode") \
       .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFVEC3F) \
       .setName("set_startpoint") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTONLY) \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFVEC3F) \
       .setName("set_endpoint") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTONLY) \
      ) \
     ) \
     .setProtoBody(ProtoBodyObject() \
      .addChild(GroupObject() \
       .addChild(TransformObject() \
        .setDEF("trans") \
        .addChild(TransformObject() \
         .setDEF("rotscale") \
         .addChild(ShapeObject() \
          .setAppearance(AppearanceObject() \
           .setMaterial(MaterialObject() \
            .setDiffuseColor([0.2,0.7,0.7]) \
            .setTransparency(0.5) \
           ) \
          ) \
          .setGeometry(CylinderObject() \
           .setRadius(0.05) \
          ) \
         ) \
        ) \
       ) \
       .addChild(ScriptObject() \
        .setDEF("S1") \
        .addField(fieldObject() \
         .setType(fieldObject.TYPE_SFNODE) \
         .setName("startnode") \
         .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
        ) \
        .addField(fieldObject() \
         .setType(fieldObject.TYPE_SFNODE) \
         .setName("endnode") \
         .setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY) \
        ) \
        .addField(fieldObject() \
         .setType(fieldObject.TYPE_SFNODE) \
         .setName("position") \
         .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
         .addChild(TransformObject() \
          .setUSE("trans") \
         ) \
        ) \
        .addField(fieldObject() \
         .setType(fieldObject.TYPE_SFNODE) \
         .setName("rotscale") \
         .setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT) \
         .addChild(TransformObject() \
          .setUSE("rotscale") \
         ) \
        ) \
        .addField(fieldObject() \
         .setType(fieldObject.TYPE_SFVEC3F) \
         .setName("set_startpoint") \
         .setAccessType(fieldObject.ACCESSTYPE_INPUTONLY) \
        ) \
        .addField(fieldObject() \
         .setType(fieldObject.TYPE_SFVEC3F) \
         .setName("set_endpoint") \
         .setAccessType(fieldObject.ACCESSTYPE_INPUTONLY) \
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
    .addChild(ProtoInstanceObject() \
     .setName("point") \
     .setDEF("G1") \
    ) \
    .addChild(ProtoInstanceObject() \
     .setName("point") \
     .setDEF("G2") \
    ) \
    .addChild(ProtoInstanceObject() \
     .setName("x3dconnector") \
     .setDEF("connector1") \
     .addFieldValue(fieldValueObject() \
      .setName("startnode") \
      .addChild(ProtoInstanceObject() \
       .setUSE("G1") \
      ) \
     ) \
     .addFieldValue(fieldValueObject() \
      .setName("endnode") \
      .addChild(ProtoInstanceObject() \
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
    .addChild(ROUTEObject() \
     .setFromNode("G1") \
     .setFromField("translation") \
     .setToNode("connector1") \
     .setToField("set_startpoint") \
    ) \
    .addChild(ROUTEObject() \
     .setFromNode("G2") \
     .setFromField("translation") \
     .setToNode("connector1") \
     .setToField("set_endpoint") \
    ) \
   ) \

X3D0.toFileX3D("./future/./arc1.newf.x3d")
