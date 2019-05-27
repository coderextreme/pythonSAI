import x3dpsail


X3D0 = (x3dpsail.X3D().setProfile(x3dpsail.SFString("Immersive")).setVersion(x3dpsail.SFString("3.3"))
      .setHead(x3dpsail.head()
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("creator")).setContent(x3dpsail.SFString("John W Carlson")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("created")).setContent(x3dpsail.SFString("December 13 2015")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("title")).setContent(x3dpsail.SFString("force.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("identifier")).setContent(x3dpsail.SFString("https://coderextreme.net/X3DJSONLD/force.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("description")).setContent(x3dpsail.SFString("beginnings of a force directed graph in 3D")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("generator")).setContent(x3dpsail.SFString("Vim, X3D-Edit, https://savage.nps.edu/X3D-Edit"))))
      .setScene(x3dpsail.Scene()
        .addChild(x3dpsail.ProtoDeclare().setName(x3dpsail.SFString("node"))
          .setProtoInterface(x3dpsail.ProtoInterface()
            .addField(x3dpsail.field().setName(x3dpsail.SFString("position")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFVec3f")).setValue(x3dpsail.SFString("0 0 0"))))
          .setProtoBody(x3dpsail.ProtoBody()
            .addChild(x3dpsail.Transform().setDEF(x3dpsail.SFString("transform"))
              .setIS(x3dpsail.IS()
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("translation")).setProtoField(x3dpsail.SFString("position"))))
              .addChild(x3dpsail.Shape()
                .setGeometry(x3dpsail.Sphere())
                .setAppearance(x3dpsail.Appearance()
                  .setMaterial(x3dpsail.Material().setDiffuseColor(x3dpsail.SFColor(1,0,0)))))
              .addChild(x3dpsail.Transform().setTranslation(x3dpsail.SFVec3f(1,0,0))
                .addChild(x3dpsail.Shape()
                  .setGeometry(x3dpsail.Text().setString(x3dpsail.MFString(["Node"]))
                    .setFontStyle(x3dpsail.FontStyle().setJustify(x3dpsail.MFString(["MIDDLE","MIDDLE"])).setSize(x3dpsail.SFFloat(5))))
                  .setAppearance(x3dpsail.Appearance()
                    .setMaterial(x3dpsail.Material().setDiffuseColor(x3dpsail.SFColor(0,0,1)))))))
            .addChild(x3dpsail.PositionInterpolator().setDEF(x3dpsail.SFString("NodePosition")).setKey(x3dpsail.MFFloat([0,1])).setKeyValue(x3dpsail.MFVec3f([0,0,0,0,5,0])))
            .addChild(x3dpsail.Script().setDEF(x3dpsail.SFString("MoveBall"))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("translation")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFVec3f")).setValue(x3dpsail.SFString("50 50 0")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("old")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFVec3f")).setValue(x3dpsail.SFString("0 0 0")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("set_cycle")).setAccessType(x3dpsail.SFString("inputOnly")).setType(x3dpsail.SFString("SFTime")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("keyValue")).setAccessType(x3dpsail.SFString("outputOnly")).setType(x3dpsail.SFString("MFVec3f"))).setSourceCode('''ecmascript:\n"+
"					function set_cycle(value) {\n"+
"                                                old = translation;\n"+
"						translation = new SFVec3f(Math.random()*100-50, Math.random()*100-50, Math.random()*100-50);\n"+
"                                                keyValue = new MFVec3f([old, translation]);\n"+
"						// Browser.println(translation);\n"+
"					}''')
)
            .addChild(x3dpsail.TimeSensor().setDEF(x3dpsail.SFString("nodeClock")).setCycleInterval(x3dpsail.SFTime(3)).setLoop(x3dpsail.SFBool(True)))
            .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("nodeClock")).setFromField(x3dpsail.SFString("cycleTime")).setToNode(x3dpsail.SFString("MoveBall")).setToField(x3dpsail.SFString("set_cycle")))
            .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("nodeClock")).setFromField(x3dpsail.SFString("fraction_changed")).setToNode(x3dpsail.SFString("NodePosition")).setToField(x3dpsail.SFString("set_fraction")))
            .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("MoveBall")).setFromField(x3dpsail.SFString("keyValue")).setToNode(x3dpsail.SFString("NodePosition")).setToField(x3dpsail.SFString("keyValue")))
            .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("NodePosition")).setFromField(x3dpsail.SFString("value_changed")).setToNode(x3dpsail.SFString("transform")).setToField(x3dpsail.SFString("set_translation")))))
        .addChild(x3dpsail.ProtoDeclare().setName(x3dpsail.SFString("cylinder"))
          .setProtoInterface(x3dpsail.ProtoInterface()
            .addField(x3dpsail.field().setName(x3dpsail.SFString("set_positionA")).setAccessType(x3dpsail.SFString("inputOnly")).setType(x3dpsail.SFString("SFVec3f")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("set_positionB")).setAccessType(x3dpsail.SFString("inputOnly")).setType(x3dpsail.SFString("SFVec3f"))))
          .setProtoBody(x3dpsail.ProtoBody()
            .addChild(x3dpsail.Shape()
              .setGeometry(x3dpsail.Extrusion().setDEF(x3dpsail.SFString("extrusion")).setCreaseAngle(x3dpsail.SFFloat(0.785)).setCrossSection(x3dpsail.MFVec2f([1,0,0.92,-0.38,0.71,-0.71,0.38,-0.92,0,-1,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1,0,-0.92,0.38,-0.71,0.71,-0.38,0.92,0,1,0.38,0.92,0.71,0.71,0.92,0.38,1,0])).setSpine(x3dpsail.MFVec3f([0,-50,0,0,50,0])))
              .setAppearance(x3dpsail.Appearance()
                .setMaterial(x3dpsail.Material().setDiffuseColor(x3dpsail.SFColor(0,1,0)))))
            .addChild(x3dpsail.Script().setDEF(x3dpsail.SFString("MoveCylinder"))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("spine")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("MFVec3f")).setValue(x3dpsail.SFString("0 -50 0 0 50 0")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("set_endA")).setAccessType(x3dpsail.SFString("inputOnly")).setType(x3dpsail.SFString("SFVec3f")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("set_endB")).setAccessType(x3dpsail.SFString("inputOnly")).setType(x3dpsail.SFString("SFVec3f")))
              .setIS(x3dpsail.IS()
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("set_endA")).setProtoField(x3dpsail.SFString("set_positionA")))
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("set_endB")).setProtoField(x3dpsail.SFString("set_positionB")))).setSourceCode('''ecmascript:\n"+
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
)
            .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("MoveCylinder")).setFromField(x3dpsail.SFString("spine")).setToNode(x3dpsail.SFString("extrusion")).setToField(x3dpsail.SFString("set_spine")))))
        .addChild(x3dpsail.Transform().setDEF(x3dpsail.SFString("HoldsContent")).setScale(x3dpsail.SFVec3f(0.1,0.1,0.1))
          .addChild(x3dpsail.PlaneSensor().setDEF(x3dpsail.SFString("clickGenerator")).setMinPosition(x3dpsail.SFVec2f(-50,-50)).setMaxPosition(x3dpsail.SFVec2f(50,50)).setDescription(x3dpsail.SFString("click on background to add nodes, click on nodes to add links")))
          .addChild(x3dpsail.ProtoInstance().setName(x3dpsail.SFString("node")).setDEF(x3dpsail.SFString("nodeA"))
            .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("position")).setValue(x3dpsail.SFString("0 0 0"))))
          .addChild(x3dpsail.ProtoInstance().setName(x3dpsail.SFString("node")).setDEF(x3dpsail.SFString("nodeB"))
            .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("position")).setValue(x3dpsail.SFString("50 50 50"))))
          .addChild(x3dpsail.ProtoInstance().setName(x3dpsail.SFString("cylinder")).setDEF(x3dpsail.SFString("linkA"))
            .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("set_positionA")).setValue(x3dpsail.SFString("0 0 0")))
            .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("set_positionB")).setValue(x3dpsail.SFString("50 50 50")))))
        .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("nodeA")).setFromField(x3dpsail.SFString("position")).setToNode(x3dpsail.SFString("linkA")).setToField(x3dpsail.SFString("set_positionA")))
        .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("nodeB")).setFromField(x3dpsail.SFString("position")).setToNode(x3dpsail.SFString("linkA")).setToField(x3dpsail.SFString("set_positionB")))))

X3D0.toFileX3D("./future/./fors_RoundTrip.x3d")
