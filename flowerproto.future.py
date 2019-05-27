import x3dpsail


X3D0 = (x3dpsail.X3D().setProfile(x3dpsail.SFString("Immersive")).setVersion(x3dpsail.SFString("3.3"))
      .setHead(x3dpsail.head()
        .addComponent(x3dpsail.component().setName(x3dpsail.SFString("Shaders")).setLevel(x3dpsail.SFInt32(1)))
        .addComponent(x3dpsail.component().setName(x3dpsail.SFString("CubeMapTexturing")).setLevel(x3dpsail.SFInt32(1)))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("title")).setContent(x3dpsail.SFString("flowerproto.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("creator")).setContent(x3dpsail.SFString("John Carlson")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("description")).setContent(x3dpsail.SFString("A flower proto with configurable shaders")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("generator")).setContent(x3dpsail.SFString("X3D-Edit, https://savage.nps.edu/X3D-Edit")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("identifier")).setContent(x3dpsail.SFString("https://coderextreme.net/X3DJSONLD/flowerproto.x3d"))))
      .setScene(x3dpsail.Scene()
        .addChild(x3dpsail.ProtoDeclare().setName(x3dpsail.SFString("FlowerProto"))
          .setProtoInterface(x3dpsail.ProtoInterface()
            .addField(x3dpsail.field().setName(x3dpsail.SFString("vertex")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("MFString")).setValue(x3dpsail.SFString("\"../shaders/gl_flowers_chromatic.vs\"")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("fragment")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("MFString")).setValue(x3dpsail.SFString("\"../shaders/pc_flowers.fs\""))))
          .setProtoBody(x3dpsail.ProtoBody()
            .addChild(x3dpsail.Transform().setDEF(x3dpsail.SFString("transform"))
              .addChild(x3dpsail.Shape()
                .setAppearance(x3dpsail.Appearance()
                  .setMaterial(x3dpsail.Material().setDiffuseColor(x3dpsail.SFColor(0.7,0.7,0.7)))
                  .setTexture(x3dpsail.ComposedCubeMapTexture().setDEF(x3dpsail.SFString("texture"))
                    .setBack(x3dpsail.ImageTexture().setUrl(x3dpsail.MFString(["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"])))
                    .setBottom(x3dpsail.ImageTexture().setUrl(x3dpsail.MFString(["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"])))
                    .setFront(x3dpsail.ImageTexture().setUrl(x3dpsail.MFString(["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"])))
                    .setLeft(x3dpsail.ImageTexture().setUrl(x3dpsail.MFString(["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"])))
                    .setRight(x3dpsail.ImageTexture().setUrl(x3dpsail.MFString(["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"])))
                    .setTop(x3dpsail.ImageTexture().setUrl(x3dpsail.MFString(["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"]))))
                  .addShaders(x3dpsail.ComposedShader().setDEF(x3dpsail.SFString("shader")).setLanguage(x3dpsail.SFString("GLSL"))
                    .addField(x3dpsail.field().setName(x3dpsail.SFString("cube")).setType(x3dpsail.SFString("SFInt32")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("0")))
                    .addField(x3dpsail.field().setName(x3dpsail.SFString("chromaticDispertion")).setType(x3dpsail.SFString("SFVec3f")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("0.98 1 1.033")))
                    .addField(x3dpsail.field().setName(x3dpsail.SFString("bias")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("10")))
                    .addField(x3dpsail.field().setName(x3dpsail.SFString("scale")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("10")))
                    .addField(x3dpsail.field().setName(x3dpsail.SFString("power")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("2")))
                    .addField(x3dpsail.field().setName(x3dpsail.SFString("a")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("3")))
                    .addField(x3dpsail.field().setName(x3dpsail.SFString("b")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("1")))
                    .addField(x3dpsail.field().setName(x3dpsail.SFString("c")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("3")))
                    .addField(x3dpsail.field().setName(x3dpsail.SFString("d")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("3")))
                    .addField(x3dpsail.field().setName(x3dpsail.SFString("tdelta")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("0.5")))
                    .addField(x3dpsail.field().setName(x3dpsail.SFString("pdelta")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("0.5")))
                    #<field name='cube' type='SFNode' accessType=\"inputOutput\"> <ComposedCubeMapTexture USE=\"texture\"/> </field>

                    .addParts(x3dpsail.ShaderPart().setType(x3dpsail.SFString("VERTEX"))
                      .setIS(x3dpsail.IS()
                        .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("url")).setProtoField(x3dpsail.SFString("vertex")))))
                    .addParts(x3dpsail.ShaderPart().setType(x3dpsail.SFString("FRAGMENT"))
                      .setIS(x3dpsail.IS()
                        .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("url")).setProtoField(x3dpsail.SFString("fragment")))))))
                .setGeometry(x3dpsail.Sphere()))
              .addChild(x3dpsail.Script().setDEF(x3dpsail.SFString("Bounce"))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("translation")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFVec3f")).setValue(x3dpsail.SFString("0 0 0")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("velocity")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFVec3f")).setValue(x3dpsail.SFString("0 0 0")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("set_fraction")).setAccessType(x3dpsail.SFString("inputOnly")).setType(x3dpsail.SFString("SFTime")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("a")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("0.5")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("b")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("0.5")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("c")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("3")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("d")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("3")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("tdelta")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("0.5")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("pdelta")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("0.5"))).setSourceCode('''ecmascript:\n"+
"			function initialize() {\n"+
"			    translation = new SFVec3f(0, 0, 0);\n"+
"			    velocity = new SFVec3f(\n"+
"			    	Math.random() - 0.5,\n"+
"				Math.random() - 0.5,\n"+
"				Math.random() - 0.5);\n"+
"			}\n"+
"			function set_fraction() {\n"+
"			    translation = new SFVec3f(\n"+
"			    	translation.x + velocity.x,\n"+
"				translation.y + velocity.y,\n"+
"				translation.z + velocity.z);\n"+
"			    for (var j = 0; j <= 2; j++) {\n"+
"				    if (Math.abs(translation.x) > 10) {\n"+
"					initialize();\n"+
"				    } else if (Math.abs(translation.y) > 10) {\n"+
"					initialize();\n"+
"				    } else if (Math.abs(translation.z) > 10) {\n"+
"					initialize();\n"+
"				    } else {\n"+
"					velocity.x += Math.random() * 0.2 - 0.1;\n"+
"					velocity.y += Math.random() * 0.2 - 0.1;\n"+
"					velocity.z += Math.random() * 0.2 - 0.1;\n"+
"				    }\n"+
"			    }\n"+
"			    animate_flowers();\n"+
"			}\n"+
"\n"+
"			function animate_flowers(fraction, eventTime) {\n"+
"				choice = Math.floor(Math.random() * 4);\n"+
"				switch (choice) {\n"+
"				case 0:\n"+
"					a += Math.random() * 0.2 - 0.1;\n"+
"					break;\n"+
"				case 1:\n"+
"					b += Math.random() * 0.2 - 0.1;\n"+
"					break;\n"+
"				case 2:\n"+
"					c += Math.random() * 2 - 1;\n"+
"					break;\n"+
"				case 3:\n"+
"					d += Math.random() * 2 - 1;\n"+
"					break;\n"+
"				}\n"+
"				tdelta += 0.5;\n"+
"				pdelta += 0.5;\n"+
"				if (a > 1) {\n"+
"					a =  0.5;\n"+
"				}\n"+
"				if (b > 1) {\n"+
"					b =  0.5;\n"+
"				}\n"+
"				if (c < 1) {\n"+
"					c =  4;\n"+
"				}\n"+
"				if (d < 1) {\n"+
"					d =  4;\n"+
"				}\n"+
"				if (c > 10) {\n"+
"					c = 4;\n"+
"				}\n"+
"				if (d > 10) {\n"+
"					d = 4;\n"+
"				}\n"+
"			}''')
)
              .addChild(x3dpsail.TimeSensor().setDEF(x3dpsail.SFString("TourTime")).setCycleInterval(x3dpsail.SFTime(0.15)).setLoop(x3dpsail.SFBool(True)))
              .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("TourTime")).setFromField(x3dpsail.SFString("cycleTime")).setToNode(x3dpsail.SFString("Bounce")).setToField(x3dpsail.SFString("set_fraction")))
              .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("Bounce")).setFromField(x3dpsail.SFString("translation_changed")).setToNode(x3dpsail.SFString("transform")).setToField(x3dpsail.SFString("set_translation")))
              .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("Bounce")).setFromField(x3dpsail.SFString("a")).setToNode(x3dpsail.SFString("shader")).setToField(x3dpsail.SFString("a")))
              .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("Bounce")).setFromField(x3dpsail.SFString("b")).setToNode(x3dpsail.SFString("shader")).setToField(x3dpsail.SFString("b")))
              .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("Bounce")).setFromField(x3dpsail.SFString("c")).setToNode(x3dpsail.SFString("shader")).setToField(x3dpsail.SFString("c")))
              .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("Bounce")).setFromField(x3dpsail.SFString("d")).setToNode(x3dpsail.SFString("shader")).setToField(x3dpsail.SFString("d")))
              .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("Bounce")).setFromField(x3dpsail.SFString("tdelta")).setToNode(x3dpsail.SFString("shader")).setToField(x3dpsail.SFString("tdelta")))
              .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("Bounce")).setFromField(x3dpsail.SFString("pdelta")).setToNode(x3dpsail.SFString("shader")).setToField(x3dpsail.SFString("pdelta"))))))))

X3D0.toFileX3D("./future/./flowerproto_RoundTrip.x3d")
