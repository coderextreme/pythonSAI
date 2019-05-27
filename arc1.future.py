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
        .addChild(x3dpsail.ProtoDeclare().setName(x3dpsail.SFString("point"))
          .setProtoInterface(x3dpsail.ProtoInterface()
            .addField(x3dpsail.field().setName(x3dpsail.SFString("translation")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFVec3f")).setValue(x3dpsail.SFString("0 0 0"))))
          .setProtoBody(x3dpsail.ProtoBody()
            .addChild(x3dpsail.Transform().setDEF(x3dpsail.SFString("node"))
              .setIS(x3dpsail.IS()
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("translation")).setProtoField(x3dpsail.SFString("translation"))))
              .addChild(x3dpsail.Shape()
                .setGeometry(x3dpsail.Sphere().setRadius(x3dpsail.SFFloat(0.1)))
                .setAppearance(x3dpsail.Appearance()
                  .setMaterial(x3dpsail.Material().setDiffuseColor(x3dpsail.SFColor(1,0,0)))))
              .addChild(x3dpsail.PositionInterpolator().setDEF(x3dpsail.SFString("PI1")).setKey(x3dpsail.MFFloat([0,1])).setKeyValue(x3dpsail.MFVec3f([0,0,0,0,5,0])))
              .addChild(x3dpsail.Script().setDEF(x3dpsail.SFString("MB1"))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("translation")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFVec3f")).setValue(x3dpsail.SFString("50 50 0")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("old")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFVec3f")).setValue(x3dpsail.SFString("0 0 0")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("set_location")).setAccessType(x3dpsail.SFString("inputOnly")).setType(x3dpsail.SFString("SFTime")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("keyValue")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("MFVec3f")).setValue(x3dpsail.SFString("0 0 0 0 5 0"))).setSourceCode('''ecmascript:\n"+
"		function set_location(value) {\n"+
"                    old = translation;\n"+
"		    translation = new SFVec3f(Math.random()*10-5, Math.random()*10-5, Math.random()*10-5);\n"+
"                    keyValue = new MFVec3f([old, translation]);\n"+
"		    // Browser.println(keyValue);\n"+
"		}''')
)
              .addChild(x3dpsail.TimeSensor().setDEF(x3dpsail.SFString("CL1")).setCycleInterval(x3dpsail.SFTime(3)).setLoop(x3dpsail.SFBool(True)))
              .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("CL1")).setFromField(x3dpsail.SFString("cycleTime")).setToNode(x3dpsail.SFString("MB1")).setToField(x3dpsail.SFString("set_location")))
              .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("CL1")).setFromField(x3dpsail.SFString("fraction_changed")).setToNode(x3dpsail.SFString("PI1")).setToField(x3dpsail.SFString("set_fraction")))
              .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("MB1")).setFromField(x3dpsail.SFString("keyValue")).setToNode(x3dpsail.SFString("PI1")).setToField(x3dpsail.SFString("keyValue")))
              .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("PI1")).setFromField(x3dpsail.SFString("value_changed")).setToNode(x3dpsail.SFString("node")).setToField(x3dpsail.SFString("set_translation"))))))
        .addChild(x3dpsail.ProtoDeclare().setName(x3dpsail.SFString("x3dconnector"))
          .setProtoInterface(x3dpsail.ProtoInterface()
            .addField(x3dpsail.field().setName(x3dpsail.SFString("startnode")).setAccessType(x3dpsail.SFString("initializeOnly")).setType(x3dpsail.SFString("SFNode")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("endnode")).setAccessType(x3dpsail.SFString("initializeOnly")).setType(x3dpsail.SFString("SFNode")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("set_startpoint")).setAccessType(x3dpsail.SFString("inputOnly")).setType(x3dpsail.SFString("SFVec3f")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("set_endpoint")).setAccessType(x3dpsail.SFString("inputOnly")).setType(x3dpsail.SFString("SFVec3f"))))
          .setProtoBody(x3dpsail.ProtoBody()
            .addChild(x3dpsail.Group()
              .addChild(x3dpsail.Transform().setDEF(x3dpsail.SFString("trans"))
                .addChild(x3dpsail.Transform().setDEF(x3dpsail.SFString("rotscale"))
                  .addChild(x3dpsail.Shape()
                    .setAppearance(x3dpsail.Appearance()
                      .setMaterial(x3dpsail.Material().setDiffuseColor(x3dpsail.SFColor(0.2,0.7,0.7)).setTransparency(x3dpsail.SFFloat(0.5))))
                    .setGeometry(x3dpsail.Cylinder().setRadius(x3dpsail.SFFloat(0.05))))))
              .addChild(x3dpsail.Script().setDEF(x3dpsail.SFString("S1"))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("startnode")).setAccessType(x3dpsail.SFString("initializeOnly")).setType(x3dpsail.SFString("SFNode")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("endnode")).setAccessType(x3dpsail.SFString("initializeOnly")).setType(x3dpsail.SFString("SFNode")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("position")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFNode"))
                  .addChild(x3dpsail.Transform().setUSE(x3dpsail.SFString("trans"))))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("rotscale")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFNode"))
                  .addChild(x3dpsail.Transform().setUSE(x3dpsail.SFString("rotscale"))))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("set_startpoint")).setAccessType(x3dpsail.SFString("inputOnly")).setType(x3dpsail.SFString("SFVec3f")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("set_endpoint")).setAccessType(x3dpsail.SFString("inputOnly")).setType(x3dpsail.SFString("SFVec3f")))
                .setIS(x3dpsail.IS()
                  .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("startnode")).setProtoField(x3dpsail.SFString("startnode")))
                  .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("endnode")).setProtoField(x3dpsail.SFString("endnode")))
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
))))
        .addChild(x3dpsail.ProtoInstance().setName(x3dpsail.SFString("point")).setDEF(x3dpsail.SFString("G1")))
        .addChild(x3dpsail.ProtoInstance().setName(x3dpsail.SFString("point")).setDEF(x3dpsail.SFString("G2")))
        .addChild(x3dpsail.ProtoInstance().setName(x3dpsail.SFString("x3dconnector")).setDEF(x3dpsail.SFString("connector1"))
          .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("startnode"))
            .addChild(x3dpsail.ProtoInstance().setUSE(x3dpsail.SFString("G1"))))
          .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("endnode"))
            .addChild(x3dpsail.ProtoInstance().setUSE(x3dpsail.SFString("G2"))))
          .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("set_startpoint")))
          .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("set_endpoint"))))
        .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("G1")).setFromField(x3dpsail.SFString("translation")).setToNode(x3dpsail.SFString("connector1")).setToField(x3dpsail.SFString("set_startpoint")))
        .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("G2")).setFromField(x3dpsail.SFString("translation")).setToNode(x3dpsail.SFString("connector1")).setToField(x3dpsail.SFString("set_endpoint")))))

X3D0.toFileX3D("./future/./arc1_RoundTrip.x3d")
