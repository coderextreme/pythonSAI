import x3dpsail


X3D0 = (x3dpsail.X3D().setProfile(x3dpsail.SFString("Immersive")).setVersion(x3dpsail.SFString("3.3"))
      .setHead(x3dpsail.head()
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("title")).setContent(x3dpsail.SFString("x3dconnectorProto")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("creator")).setContent(x3dpsail.SFString("Lost, Doug Sanden I think")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("generator")).setContent(x3dpsail.SFString("manual")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("identifier")).setContent(x3dpsail.SFString("https://coderextreme.net/X3DJSONLD/x3dconnectorProto.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("description")).setContent(x3dpsail.SFString("a generic proto to connect two objects"))))
      .setScene(x3dpsail.Scene()
        .addChild(x3dpsail.Viewpoint().setPosition(x3dpsail.SFVec3f(0,0,5)).setDescription(x3dpsail.SFString("Only Viewpoint")))
        .addChild(x3dpsail.Background().setSkyColor(x3dpsail.MFColor([0.4,0.4,0.4])))
        .addChild(x3dpsail.Transform().setDEF(x3dpsail.SFString("G1"))
          .addChild(x3dpsail.Shape()
            .setAppearance(x3dpsail.Appearance()
              .setMaterial(x3dpsail.Material().setDiffuseColor(x3dpsail.SFColor(0.7,0.2,0.2))))
            .setGeometry(x3dpsail.Sphere().setRadius(x3dpsail.SFFloat(0.1))))
          .addChild(x3dpsail.PlaneSensor().setDescription(x3dpsail.SFString("Grab to move")).setDEF(x3dpsail.SFString("PS1")))
          .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("PS1")).setFromField(x3dpsail.SFString("translation_changed")).setToNode(x3dpsail.SFString("G1")).setToField(x3dpsail.SFString("set_translation"))))
        .addChild(x3dpsail.Transform().setDEF(x3dpsail.SFString("G2")).setTranslation(x3dpsail.SFVec3f(1,-1,0.01))
          .addChild(x3dpsail.Shape()
            .setAppearance(x3dpsail.Appearance()
              .setMaterial(x3dpsail.Material().setDiffuseColor(x3dpsail.SFColor(0.2,0.7,0.2))))
            .setGeometry(x3dpsail.Sphere().setRadius(x3dpsail.SFFloat(0.1))))
          .addChild(x3dpsail.PlaneSensor().setDescription(x3dpsail.SFString("Grab to move")).setOffset(x3dpsail.SFVec3f(1,-1,0.01)).setDEF(x3dpsail.SFString("PS2")))
          .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("PS2")).setFromField(x3dpsail.SFString("translation_changed")).setToNode(x3dpsail.SFString("G2")).setToField(x3dpsail.SFString("set_translation"))))
        .addChild(x3dpsail.Transform().setDEF(x3dpsail.SFString("G3")).setTranslation(x3dpsail.SFVec3f(1,1,0.01))
          .addChild(x3dpsail.Shape()
            .setAppearance(x3dpsail.Appearance()
              .setMaterial(x3dpsail.Material().setDiffuseColor(x3dpsail.SFColor(0.2,0.7,0.2))))
            .setGeometry(x3dpsail.Sphere().setRadius(x3dpsail.SFFloat(0.1))))
          .addChild(x3dpsail.PlaneSensor().setDescription(x3dpsail.SFString("Grab to move")).setOffset(x3dpsail.SFVec3f(1,1,0.01)).setDEF(x3dpsail.SFString("PS3")))
          .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("PS3")).setFromField(x3dpsail.SFString("translation_changed")).setToNode(x3dpsail.SFString("G3")).setToField(x3dpsail.SFString("set_translation"))))
        .addChild(x3dpsail.Transform().setDEF(x3dpsail.SFString("G4")).setTranslation(x3dpsail.SFVec3f(-1,1,0.01))
          .addChild(x3dpsail.Shape()
            .setAppearance(x3dpsail.Appearance()
              .setMaterial(x3dpsail.Material().setDiffuseColor(x3dpsail.SFColor(0.2,0.7,0.2))))
            .setGeometry(x3dpsail.Sphere().setRadius(x3dpsail.SFFloat(0.1))))
          .addChild(x3dpsail.PlaneSensor().setDescription(x3dpsail.SFString("Grab to move")).setOffset(x3dpsail.SFVec3f(-1,1,0.01)).setDEF(x3dpsail.SFString("PS4")))
          .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("PS4")).setFromField(x3dpsail.SFString("translation_changed")).setToNode(x3dpsail.SFString("G4")).setToField(x3dpsail.SFString("set_translation"))))
        .addChild(x3dpsail.Transform().setDEF(x3dpsail.SFString("transC1"))
          .addChild(x3dpsail.Transform().setDEF(x3dpsail.SFString("rotscaleC1"))
            .addChild(x3dpsail.Shape()
              .setAppearance(x3dpsail.Appearance()
                .setMaterial(x3dpsail.Material().setDiffuseColor(x3dpsail.SFColor(0.2,0.7,0.7)).setTransparency(x3dpsail.SFFloat(0.5))))
              .setGeometry(x3dpsail.Cylinder().setRadius(x3dpsail.SFFloat(0.05))))))
        .addChild(x3dpsail.Transform().setDEF(x3dpsail.SFString("transC2"))
          .addChild(x3dpsail.Transform().setDEF(x3dpsail.SFString("rotscaleC2"))
            .addChild(x3dpsail.Shape()
              .setAppearance(x3dpsail.Appearance()
                .setMaterial(x3dpsail.Material().setDiffuseColor(x3dpsail.SFColor(0.2,0.7,0.7)).setTransparency(x3dpsail.SFFloat(0.5))))
              .setGeometry(x3dpsail.Cylinder().setRadius(x3dpsail.SFFloat(0.05))))))
        .addChild(x3dpsail.Transform().setDEF(x3dpsail.SFString("transC3"))
          .addChild(x3dpsail.Transform().setDEF(x3dpsail.SFString("rotscaleC3"))
            .addChild(x3dpsail.Shape()
              .setAppearance(x3dpsail.Appearance()
                .setMaterial(x3dpsail.Material().setDiffuseColor(x3dpsail.SFColor(0.2,0.7,0.7)).setTransparency(x3dpsail.SFFloat(0.5))))
              .setGeometry(x3dpsail.Cylinder().setRadius(x3dpsail.SFFloat(0.05))))))
        .addChild(x3dpsail.ProtoDeclare().setName(x3dpsail.SFString("x3dconnector"))
          .setProtoInterface(x3dpsail.ProtoInterface()
            .addField(x3dpsail.field().setName(x3dpsail.SFString("startnode")).setAccessType(x3dpsail.SFString("initializeOnly")).setType(x3dpsail.SFString("SFNode")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("endnode")).setAccessType(x3dpsail.SFString("initializeOnly")).setType(x3dpsail.SFString("SFNode")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("transnode")).setAccessType(x3dpsail.SFString("initializeOnly")).setType(x3dpsail.SFString("SFNode")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("rotscalenode")).setAccessType(x3dpsail.SFString("initializeOnly")).setType(x3dpsail.SFString("SFNode")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("set_startpoint")).setAccessType(x3dpsail.SFString("inputOnly")).setType(x3dpsail.SFString("SFVec3f")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("set_endpoint")).setAccessType(x3dpsail.SFString("inputOnly")).setType(x3dpsail.SFString("SFVec3f"))))
          .setProtoBody(x3dpsail.ProtoBody()
            .addChild(x3dpsail.Script().setDEF(x3dpsail.SFString("S1"))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("startnode")).setAccessType(x3dpsail.SFString("initializeOnly")).setType(x3dpsail.SFString("SFNode")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("endnode")).setAccessType(x3dpsail.SFString("initializeOnly")).setType(x3dpsail.SFString("SFNode")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("transnode")).setAccessType(x3dpsail.SFString("initializeOnly")).setType(x3dpsail.SFString("SFNode")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("rotscalenode")).setAccessType(x3dpsail.SFString("initializeOnly")).setType(x3dpsail.SFString("SFNode")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("set_startpoint")).setAccessType(x3dpsail.SFString("inputOnly")).setType(x3dpsail.SFString("SFVec3f")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("set_endpoint")).setAccessType(x3dpsail.SFString("inputOnly")).setType(x3dpsail.SFString("SFVec3f")))
              .setIS(x3dpsail.IS()
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("startnode")).setProtoField(x3dpsail.SFString("startnode")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("endnode")).setProtoField(x3dpsail.SFString("endnode")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("transnode")).setProtoField(x3dpsail.SFString("transnode")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("rotscalenode")).setProtoField(x3dpsail.SFString("rotscalenode")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("set_startpoint")).setProtoField(x3dpsail.SFString("set_startpoint")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("set_endpoint")).setProtoField(x3dpsail.SFString("set_endpoint")))).setSourceCode('''ecmascript:\n"+
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
)))
        .addChild(x3dpsail.ProtoInstance().setName(x3dpsail.SFString("x3dconnector")).setDEF(x3dpsail.SFString("connector1"))
          .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("startnode"))
            .addChild(x3dpsail.Transform().setUSE(x3dpsail.SFString("G1"))))
          .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("endnode"))
            .addChild(x3dpsail.Transform().setUSE(x3dpsail.SFString("G2"))))
          .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("transnode"))
            .addChild(x3dpsail.Transform().setUSE(x3dpsail.SFString("transC1"))))
          .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("rotscalenode"))
            .addChild(x3dpsail.Transform().setUSE(x3dpsail.SFString("rotscaleC1"))))
          .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("set_startpoint")))
          .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("set_endpoint"))))
        .addChild(x3dpsail.ProtoInstance().setName(x3dpsail.SFString("x3dconnector")).setDEF(x3dpsail.SFString("connector2"))
          .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("startnode"))
            .addChild(x3dpsail.Transform().setUSE(x3dpsail.SFString("G1"))))
          .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("endnode"))
            .addChild(x3dpsail.Transform().setUSE(x3dpsail.SFString("G3"))))
          .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("transnode"))
            .addChild(x3dpsail.Transform().setUSE(x3dpsail.SFString("transC2"))))
          .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("rotscalenode"))
            .addChild(x3dpsail.Transform().setUSE(x3dpsail.SFString("rotscaleC2"))))
          .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("set_startpoint")))
          .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("set_endpoint"))))
        .addChild(x3dpsail.ProtoInstance().setName(x3dpsail.SFString("x3dconnector")).setDEF(x3dpsail.SFString("connector3"))
          .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("startnode"))
            .addChild(x3dpsail.Transform().setUSE(x3dpsail.SFString("G1"))))
          .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("endnode"))
            .addChild(x3dpsail.Transform().setUSE(x3dpsail.SFString("G4"))))
          .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("transnode"))
            .addChild(x3dpsail.Transform().setUSE(x3dpsail.SFString("transC3"))))
          .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("rotscalenode"))
            .addChild(x3dpsail.Transform().setUSE(x3dpsail.SFString("rotscaleC3"))))
          .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("set_startpoint")))
          .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("set_endpoint"))))
        .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("G1")).setFromField(x3dpsail.SFString("translation_changed")).setToNode(x3dpsail.SFString("connector1")).setToField(x3dpsail.SFString("set_startpoint")))
        .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("G2")).setFromField(x3dpsail.SFString("translation_changed")).setToNode(x3dpsail.SFString("connector1")).setToField(x3dpsail.SFString("set_endpoint")))
        .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("G1")).setFromField(x3dpsail.SFString("translation_changed")).setToNode(x3dpsail.SFString("connector2")).setToField(x3dpsail.SFString("set_startpoint")))
        .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("G3")).setFromField(x3dpsail.SFString("translation_changed")).setToNode(x3dpsail.SFString("connector2")).setToField(x3dpsail.SFString("set_endpoint")))
        .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("G1")).setFromField(x3dpsail.SFString("translation_changed")).setToNode(x3dpsail.SFString("connector3")).setToField(x3dpsail.SFString("set_startpoint")))
        .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("G4")).setFromField(x3dpsail.SFString("translation_changed")).setToNode(x3dpsail.SFString("connector3")).setToField(x3dpsail.SFString("set_endpoint")))))

X3D0.toFileX3D("./future/./x3dconnectorProto_RoundTrip.x3d")
