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
     .setContent("arc.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("creator") \
     .setContent("John Carlson") \
    ) \
    .addMeta(metaObject() \
     .setName("generator") \
     .setContent("manual") \
    ) \
    .addMeta(metaObject() \
     .setName("identifier") \
     .setContent("https://coderextreme.net/X3DJSONLD/arc.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("description") \
     .setContent("an attempt to implement an arc in a graph") \
    ) \
   ) \
   .setScene(SceneObject() \
    .addChildren(ViewpointObject() \
     .setPosition([0,0,5]) \
     .setDescription("a moving graph") \
    ) \
    .addChildren(BackgroundObject() \
     .setSkyColor([0.4,0.4,0.4]) \
    ) \
    .addChildren(TransformObject() \
     .setDEF("trans1") \
     .addChildren(TransformObject() \
      .setDEF("rotscale1") \
      .addChildren(ShapeObject() \
       .setAppearance(AppearanceObject() \
        .setMaterial(MaterialObject() \
         .setDiffuseColor([0.2,0.7,0.7]) \
        ) \
       ) \
       .setGeometry(CylinderObject(radius = 0.1) \
       ) \
      ) \
     ) \
    ) \
    .addChildren(TransformObject() \
     .setDEF("trans2") \
     .addChildren(TransformObject() \
      .setDEF("rotscale2") \
      .addChildren(ShapeObject() \
       .setAppearance(AppearanceObject() \
        .setMaterial(MaterialObject() \
         .setDiffuseColor([0.2,0.7,0.7]) \
        ) \
       ) \
       .setGeometry(CylinderObject(radius = 0.1) \
       ) \
      ) \
     ) \
    ) \
    .addChildren(TransformObject() \
     .setDEF("trans3") \
     .addChildren(TransformObject() \
      .setDEF("rotscale3") \
      .addChildren(ShapeObject() \
       .setAppearance(AppearanceObject() \
        .setMaterial(MaterialObject() \
         .setDiffuseColor([0.2,0.7,0.7]) \
        ) \
       ) \
       .setGeometry(CylinderObject(radius = 0.1) \
       ) \
      ) \
     ) \
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
         .setAccessType("outputOnly") \
         .setType("MFVec3f") \
        ) \
.setSourceCode('''ecmascript:\n"+
"		function set_location(value) {\n"+
"                    old = translation;\n"+
"		    translation = new SFVec3f(Math.random()*10-5, Math.random()*10-5, Math.random()*10-5);\n"+
"                    keyValue = new MFVec3f([old, translation]);\n"+
"		    // Browser.println(translation);\n"+
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
#from doug sanden
    .addChildren(ProtoDeclareObject() \
     .setName("x3dconnector") \
     .setProtoInterface(ProtoInterfaceObject() \
      .addField(fieldObject() \
       .setName("startnode") \
       .setAccessType("inputOutput") \
       .setType("SFNode") \
      ) \
      .addField(fieldObject() \
       .setName("endnode") \
       .setAccessType("inputOutput") \
       .setType("SFNode") \
      ) \
      .addField(fieldObject() \
       .setName("transnode") \
       .setAccessType("inputOutput") \
       .setType("SFNode") \
      ) \
      .addField(fieldObject() \
       .setName("rotscalenode") \
       .setAccessType("inputOutput") \
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
      .addChildren(ScriptObject() \
       .setDEF("S1") \
       .addField(fieldObject() \
        .setName("startnode") \
        .setAccessType("inputOutput") \
        .setType("SFNode") \
       ) \
       .addField(fieldObject() \
        .setName("endnode") \
        .setAccessType("inputOutput") \
        .setType("SFNode") \
       ) \
       .addField(fieldObject() \
        .setName("transnode") \
        .setAccessType("inputOutput") \
        .setType("SFNode") \
       ) \
       .addField(fieldObject() \
        .setName("rotscalenode") \
        .setAccessType("inputOutput") \
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
         .setNodeField("transnode") \
         .setProtoField("transnode") \
        ) \
        .addConnect(connectObject() \
         .setNodeField("rotscalenode") \
         .setProtoField("rotscalenode") \
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
"	    } else {\n"+
"		    return {\n"+
"			    scale : new SFVec3f(1.0,dist,1.0),\n"+
"			    translation : transl,\n"+
"			    rotation : new SFRotation(new SFVec3f(0.0,1.0,0.0),norm)\n"+
"		    };\n"+
"	    }\n"+
"	}\n"+
"	function recompute_and_route(startpoint, endpoint) {\n"+
"		var trafo = recompute(startpoint, endpoint);\n"+
"		if (typeof trafo !== 'undefined') {\n"+
"			transnode.translation = trafo.translation;\n"+
"			rotscalenode.rotation = trafo.rotation;\n"+
"			rotscalenode.scale = trafo.scale;\n"+
"		} else {\n"+
"			Browser.print(\"recompute returned undefined\");\n"+
"		}\n"+
"	}\n"+
"        function initialize(){\n"+
"            recompute_and_route(startnode.translation,endnode.translation);\n"+
"        }\n"+
"        function set_startpoint(val,t){\n"+
"            recompute_and_route(val || startnode.translation,endnode.translation);\n"+
"        }\n"+
"        function set_endpoint(val,t){\n"+
"            recompute_and_route(startnode.translation,val || endnode.translation);\n"+
"        }''')
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
     .setName("point") \
     .setDEF("G3") \
    ) \
    .addChildren(ProtoInstanceObject() \
     .setName("point") \
     .setDEF("G4") \
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
      .setName("transnode") \
      .addChildren(TransformObject() \
       .setUSE("trans1") \
      ) \
     ) \
     .addFieldValue(fieldValueObject() \
      .setName("rotscalenode") \
      .addChildren(TransformObject() \
       .setUSE("rotscale1") \
      ) \
     ) \
    ) \
    .addChildren(ProtoInstanceObject() \
     .setName("x3dconnector") \
     .setDEF("connector2") \
     .addFieldValue(fieldValueObject() \
      .setName("startnode") \
      .addChildren(ProtoInstanceObject() \
       .setUSE("G1") \
      ) \
     ) \
     .addFieldValue(fieldValueObject() \
      .setName("endnode") \
      .addChildren(ProtoInstanceObject() \
       .setUSE("G3") \
      ) \
     ) \
     .addFieldValue(fieldValueObject() \
      .setName("transnode") \
      .addChildren(TransformObject() \
       .setUSE("trans2") \
      ) \
     ) \
     .addFieldValue(fieldValueObject() \
      .setName("rotscalenode") \
      .addChildren(TransformObject() \
       .setUSE("rotscale2") \
      ) \
     ) \
    ) \
    .addChildren(ProtoInstanceObject() \
     .setName("x3dconnector") \
     .setDEF("connector3") \
     .addFieldValue(fieldValueObject() \
      .setName("startnode") \
      .addChildren(ProtoInstanceObject() \
       .setUSE("G1") \
      ) \
     ) \
     .addFieldValue(fieldValueObject() \
      .setName("endnode") \
      .addChildren(ProtoInstanceObject() \
       .setUSE("G4") \
      ) \
     ) \
     .addFieldValue(fieldValueObject() \
      .setName("transnode") \
      .addChildren(TransformObject() \
       .setUSE("trans3") \
      ) \
     ) \
     .addFieldValue(fieldValueObject() \
      .setName("rotscalenode") \
      .addChildren(TransformObject() \
       .setUSE("rotscale3") \
      ) \
     ) \
    ) \
    .addChildren(ROUTEObject() \
     .setFromNode("G1") \
     .setFromField("translation_changed") \
     .setToNode("connector1") \
     .setToField("set_startpoint") \
    ) \
    .addChildren(ROUTEObject() \
     .setFromNode("G2") \
     .setFromField("translation_changed") \
     .setToNode("connector1") \
     .setToField("set_endpoint") \
    ) \
    .addChildren(ROUTEObject() \
     .setFromNode("G1") \
     .setFromField("translation_changed") \
     .setToNode("connector2") \
     .setToField("set_startpoint") \
    ) \
    .addChildren(ROUTEObject() \
     .setFromNode("G3") \
     .setFromField("translation_changed") \
     .setToNode("connector2") \
     .setToField("set_endpoint") \
    ) \
    .addChildren(ROUTEObject() \
     .setFromNode("G1") \
     .setFromField("translation_changed") \
     .setToNode("connector3") \
     .setToField("set_startpoint") \
    ) \
    .addChildren(ROUTEObject() \
     .setFromNode("G4") \
     .setFromField("translation_changed") \
     .setToNode("connector3") \
     .setToField("set_endpoint") \
    ) \
   ) \

X3D0.toFileX3D("./future/./arcold.newf.x3d")
