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
     .setDEF("G1") \
     .addChildren(ShapeObject() \
      .setAppearance(AppearanceObject() \
       .setMaterial(MaterialObject() \
        .setDiffuseColor([0.7,0.2,0.2]) \
       ) \
      ) \
      .setGeometry(SphereObject(radius = 0.1) \
      ) \
     ) \
     .addChildren(PlaneSensorObject() \
      .setDescription("Grab to move") \
      .setDEF("PS1") \
     ) \
     .addChildren(ROUTEObject() \
      .setFromNode("PS1") \
      .setFromField("translation_changed") \
      .setToNode("G1") \
      .setToField("set_translation") \
     ) \
    ) \
    .addChildren(TransformObject() \
     .setDEF("G2") \
     .setTranslation([1,-1,0.01]) \
     .addChildren(ShapeObject() \
      .setAppearance(AppearanceObject() \
       .setMaterial(MaterialObject() \
        .setDiffuseColor([0.2,0.7,0.2]) \
       ) \
      ) \
      .setGeometry(SphereObject(radius = 0.1) \
      ) \
     ) \
     .addChildren(PlaneSensorObject() \
      .setDescription("Grab to move") \
      .setOffset([1,-1,0.01]) \
      .setDEF("PS2") \
     ) \
     .addChildren(ROUTEObject() \
      .setFromNode("PS2") \
      .setFromField("translation_changed") \
      .setToNode("G2") \
      .setToField("set_translation") \
     ) \
    ) \
    .addChildren(TransformObject() \
     .setDEF("transC1") \
     .addChildren(TransformObject() \
      .setDEF("rotscaleC1") \
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
       .setName("transnode") \
       .setAccessType("initializeOnly") \
       .setType("SFNode") \
      ) \
      .addField(fieldObject() \
       .setName("rotscalenode") \
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
        .setName("transnode") \
        .setAccessType("initializeOnly") \
        .setType("SFNode") \
       ) \
       .addField(fieldObject() \
        .setName("rotscalenode") \
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
"	      var trafo = recompute(startpoint, endpoint);\n"+
"	      transnode.translation = trafo.translation;\n"+
"	      rotscalenode.rotation = trafo.rotation;\n"+
"	      rotscalenode.scale = trafo.scale;\n"+
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
    .addChildren(ProtoInstanceObject() \
     .setName("x3dconnector") \
     .setDEF("connector1") \
     .addFieldValue(fieldValueObject() \
      .setName("startnode") \
      .addChildren(TransformObject() \
       .setUSE("G1") \
      ) \
     ) \
     .addFieldValue(fieldValueObject() \
      .setName("endnode") \
      .addChildren(TransformObject() \
       .setUSE("G2") \
      ) \
     ) \
     .addFieldValue(fieldValueObject() \
      .setName("transnode") \
      .addChildren(TransformObject() \
       .setUSE("transC1") \
      ) \
     ) \
     .addFieldValue(fieldValueObject() \
      .setName("rotscalenode") \
      .addChildren(TransformObject() \
       .setUSE("rotscaleC1") \
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
   ) \

X3D0.toFileX3D("./future/./x3dconnector.newf.x3d")
