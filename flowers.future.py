import x3dpsail


X3D0 = (x3dpsail.X3D().setProfile(x3dpsail.SFString("Immersive")).setVersion(x3dpsail.SFString("3.3"))
      .setHead(x3dpsail.head()
        .addComponent(x3dpsail.component().setName(x3dpsail.SFString("Shaders")).setLevel(x3dpsail.SFInt32(1)))
        .addComponent(x3dpsail.component().setName(x3dpsail.SFString("CubeMapTexturing")).setLevel(x3dpsail.SFInt32(1)))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("title")).setContent(x3dpsail.SFString("flowers.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("creator")).setContent(x3dpsail.SFString("John Carlson")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("description")).setContent(x3dpsail.SFString("5 or more prismatic flowers")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("generator")).setContent(x3dpsail.SFString("X3D-Edit, https://savage.nps.edu/X3D-Edit")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("identifier")).setContent(x3dpsail.SFString("https://coderextreme.net/X3DJSONLD/flowers.x3d"))))
      .setScene(x3dpsail.Scene()
        .addChild(x3dpsail.NavigationInfo())
        .addChild(x3dpsail.Background().setBackUrl(x3dpsail.MFString(["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"])).setBottomUrl(x3dpsail.MFString(["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"])).setFrontUrl(x3dpsail.MFString(["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"])).setLeftUrl(x3dpsail.MFString(["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"])).setRightUrl(x3dpsail.MFString(["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"])).setTopUrl(x3dpsail.MFString(["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"])))
        .addChild(x3dpsail.ProtoDeclare().setName(x3dpsail.SFString("flower"))
          .setProtoBody(x3dpsail.ProtoBody()
            .addChild(x3dpsail.Transform().setDEF(x3dpsail.SFString("transform"))
              .addChild(x3dpsail.Shape()
                .setAppearance(x3dpsail.Appearance()
                  .setMaterial(x3dpsail.Material().setDiffuseColor(x3dpsail.SFColor(0.7,0.7,0.7)).setSpecularColor(x3dpsail.SFColor(0.5,0.5,0.5)))
                  .setTexture(x3dpsail.ComposedCubeMapTexture().setDEF(x3dpsail.SFString("texture"))
                    .setBack(x3dpsail.ImageTexture().setUrl(x3dpsail.MFString(["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"])))
                    .setBottom(x3dpsail.ImageTexture().setUrl(x3dpsail.MFString(["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"])))
                    .setFront(x3dpsail.ImageTexture().setUrl(x3dpsail.MFString(["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"])))
                    .setLeft(x3dpsail.ImageTexture().setUrl(x3dpsail.MFString(["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"])))
                    .setRight(x3dpsail.ImageTexture().setUrl(x3dpsail.MFString(["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"])))
                    .setTop(x3dpsail.ImageTexture().setUrl(x3dpsail.MFString(["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"]))))
                  .addShaders(x3dpsail.ComposedShader().setLanguage(x3dpsail.SFString("GLSL"))
                    .addField(x3dpsail.field().setName(x3dpsail.SFString("xxxcube")).setType(x3dpsail.SFString("SFInt32")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("0")))
                    .addField(x3dpsail.field().setName(x3dpsail.SFString("cube")).setType(x3dpsail.SFString("SFNode")).setAccessType(x3dpsail.SFString("inputOutput"))
                      .addChild(x3dpsail.ComposedCubeMapTexture().setUSE(x3dpsail.SFString("texture"))))
                    .addField(x3dpsail.field().setName(x3dpsail.SFString("chromaticDispertion")).setType(x3dpsail.SFString("SFVec3f")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("0.98 1 1.033")))
                    .addField(x3dpsail.field().setName(x3dpsail.SFString("bias")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("0.5")))
                    .addField(x3dpsail.field().setName(x3dpsail.SFString("scale")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("0.5")))
                    .addField(x3dpsail.field().setName(x3dpsail.SFString("power")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("2")))
                    .addParts(x3dpsail.ShaderPart().setUrl(x3dpsail.MFString(["../shaders/common.vs","https://coderextreme.net/X3DJSONLD/shaders/common.vs"])).setType(x3dpsail.SFString("VERTEX")))
                    .addParts(x3dpsail.ShaderPart().setUrl(x3dpsail.MFString(["../shaders/gl_flowers_chromatic.fs","https://coderextreme.net/X3DJSONLD/shaders/gl_flowers_chromatic.fs"])).setType(x3dpsail.SFString("FRAGMENT"))))
                  .addShaders(x3dpsail.ComposedShader().setLanguage(x3dpsail.SFString("GLSL"))
                    .addField(x3dpsail.field().setName(x3dpsail.SFString("xxxcube")).setType(x3dpsail.SFString("SFInt32")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("0")))
                    .addField(x3dpsail.field().setName(x3dpsail.SFString("cube")).setType(x3dpsail.SFString("SFNode")).setAccessType(x3dpsail.SFString("inputOutput"))
                      .addChild(x3dpsail.ComposedCubeMapTexture().setUSE(x3dpsail.SFString("texture"))))
                    .addField(x3dpsail.field().setName(x3dpsail.SFString("chromaticDispertion")).setType(x3dpsail.SFString("SFVec3f")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("0.98 1 1.033")))
                    .addField(x3dpsail.field().setName(x3dpsail.SFString("bias")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("0.5")))
                    .addField(x3dpsail.field().setName(x3dpsail.SFString("scale")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("0.5")))
                    .addField(x3dpsail.field().setName(x3dpsail.SFString("power")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("2")))
                    .addParts(x3dpsail.ShaderPart().setUrl(x3dpsail.MFString(["../shaders/x3dom.vs","https://coderextreme.net/X3DJSONLD/shaders/x3dom.vs"])).setType(x3dpsail.SFString("VERTEX")))
                    .addParts(x3dpsail.ShaderPart().setUrl(x3dpsail.MFString(["../shaders/pc_bubbles.fs","https://coderextreme.net/X3DJSONLD/shaders/pc_bubbles.fs"])).setType(x3dpsail.SFString("FRAGMENT"))))
                  .addShaders(x3dpsail.ComposedShader().setDEF(x3dpsail.SFString("shader")).setLanguage(x3dpsail.SFString("GLSL"))
                    .addField(x3dpsail.field().setName(x3dpsail.SFString("xxxcube")).setType(x3dpsail.SFString("SFInt32")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("0")))
                    .addField(x3dpsail.field().setName(x3dpsail.SFString("cube")).setType(x3dpsail.SFString("SFNode")).setAccessType(x3dpsail.SFString("inputOutput"))
                      .addChild(x3dpsail.ComposedCubeMapTexture().setUSE(x3dpsail.SFString("texture"))))
                    .addField(x3dpsail.field().setName(x3dpsail.SFString("chromaticDispertion")).setType(x3dpsail.SFString("SFVec3f")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("0.98 1 1.033")))
                    .addField(x3dpsail.field().setName(x3dpsail.SFString("bias")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("10")))
                    .addField(x3dpsail.field().setName(x3dpsail.SFString("scale")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("10")))
                    .addField(x3dpsail.field().setName(x3dpsail.SFString("power")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("2")))
                    .addParts(x3dpsail.ShaderPart().setUrl(x3dpsail.MFString(["../shaders/cobweb.vs","https://coderextreme.net/X3DJSONLD/shaders/cobweb.vs"])).setType(x3dpsail.SFString("VERTEX")))
                    .addParts(x3dpsail.ShaderPart().setUrl(x3dpsail.MFString(["../shaders/pc_bubbles.fs","https://coderextreme.net/X3DJSONLD/shaders/pc_bubbles.fs"])).setType(x3dpsail.SFString("FRAGMENT")))))
                #<Sphere></Sphere>

                .setGeometry(x3dpsail.IndexedFaceSet().setConvex(x3dpsail.SFBool(False)).setDEF(x3dpsail.SFString("Orbit"))
                  .setCoord(x3dpsail.Coordinate().setDEF(x3dpsail.SFString("OrbitCoordinates"))))))
            .addChild(x3dpsail.Script().setDEF(x3dpsail.SFString("Bounce"))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("translation")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFVec3f")).setValue(x3dpsail.SFString("0 0 0")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("velocity")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFVec3f")).setValue(x3dpsail.SFString("0 0 0")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("set_fraction")).setAccessType(x3dpsail.SFString("inputOnly")).setType(x3dpsail.SFString("SFTime")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("coordinates")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("MFVec3f")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("coordIndexes")).setAccessType(x3dpsail.SFString("outputOnly")).setType(x3dpsail.SFString("MFInt32")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("a")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("0.5")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("b")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("0.5")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("c")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("3")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("d")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("3")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("tdelta")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("0.5")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("pdelta")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("0.5"))).setSourceCode('''ecmascript:\n"+
"			function newBubble() {\n"+
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
"			    if (Math.abs(translation.x) > 10) {\n"+
"					newBubble();\n"+
"			    } else if (Math.abs(translation.y) > 10) {\n"+
"					newBubble();\n"+
"			    } else if (Math.abs(translation.z) > 10) {\n"+
"					newBubble();\n"+
"			    } else {\n"+
"					velocity = new SFVec3f(\n"+
"						velocity.x + Math.random() * 0.2 - 0.1,\n"+
"						velocity.y + Math.random() * 0.2 - 0.1,\n"+
"						velocity.z + Math.random() * 0.2 - 0.1\n"+
"					);\n"+
"			    }\n"+
"			    animate_flowers();\n"+
"			}\n"+
"\n"+
"			function initialize() {\n"+
"			     var cis = [];\n"+
"			     newBubble();\n"+
"			     resolution = 100;\n"+
"			     updateCoordinates(resolution);\n"+
"			     for ( i = 0; i < resolution-1; i++) {\n"+
"				for ( j = 0; j < resolution-1; j++) {\n"+
"				     cis.push(i*resolution+j);\n"+
"				     cis.push(i*resolution+j+1);\n"+
"				     cis.push((i+1)*resolution+j+1);\n"+
"				     cis.push((i+1)*resolution+j);\n"+
"				     cis.push(-1);\n"+
"				}\n"+
"			    }\n"+
"			     coordIndexes = new MFInt32(cis);\n"+
"			}\n"+
"\n"+
"			function updateCoordinates(resolution) {\n"+
"			     theta = 0.0;\n"+
"			     phi = 0.0;\n"+
"			     delta = (2 * 3.141592653) / (resolution-1);\n"+
"			     var crds = [];\n"+
"			     for ( i = 0; i < resolution; i++) {\n"+
"				for ( j = 0; j < resolution; j++) {\n"+
"					rho = a + b * Math.cos(c * theta) * Math.cos(d * phi);\n"+
"					crds.push(new SFVec3f(\n"+
"						rho * Math.cos(phi) * Math.cos(theta),\n"+
"						rho * Math.cos(phi) * Math.sin(theta),\n"+
"						rho * Math.sin(phi)\n"+
"					));\n"+
"					theta += delta;\n"+
"				}\n"+
"				phi += delta;\n"+
"				coordinates = new MFVec3f(crds);\n"+
"			     }\n"+
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
"				resolution = 100;\n"+
"				updateCoordinates(resolution);\n"+
"			}''')
)
            .addChild(x3dpsail.TimeSensor().setDEF(x3dpsail.SFString("TourTime")).setCycleInterval(x3dpsail.SFTime(0.15)).setLoop(x3dpsail.SFBool(True)))
            .addChild(x3dpsail.TimeSensor().setDEF(x3dpsail.SFString("SongTime")).setLoop(x3dpsail.SFBool(True)))
            .addChild(x3dpsail.Sound().setMaxBack(x3dpsail.SFFloat(100)).setMaxFront(x3dpsail.SFFloat(100)).setMinBack(x3dpsail.SFFloat(20)).setMinFront(x3dpsail.SFFloat(20))
              .setSource(x3dpsail.AudioClip().setDEF(x3dpsail.SFString("AudioClip")).setDescription(x3dpsail.SFString("Chandubabamusic #1")).setUrl(x3dpsail.MFString(["../resources/chandubabamusic1.wav"]))))
            .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("cycleTime")).setFromNode(x3dpsail.SFString("SongTime")).setToField(x3dpsail.SFString("startTime")).setToNode(x3dpsail.SFString("AudioClip")))
            .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("TourTime")).setFromField(x3dpsail.SFString("cycleTime")).setToNode(x3dpsail.SFString("Bounce")).setToField(x3dpsail.SFString("set_fraction")))
            .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("Bounce")).setFromField(x3dpsail.SFString("translation")).setToNode(x3dpsail.SFString("transform")).setToField(x3dpsail.SFString("set_translation")))
            #<ROUTE fromField=\"coordIndexes\" fromNode=\"Bounce\" toField=\"set_coordIndex\" toNode=\"Orbit\"/> <ROUTE fromField=\"coordinates\" fromNode=\"Bounce\" toField=\"set_point\" toNode=\"OrbitCoordinates\"/>

            ))
        .addChild(x3dpsail.Transform()
          .addChild(x3dpsail.ProtoInstance().setName(x3dpsail.SFString("flower")))
          #<ProtoInstance name=\"flower\"/> <ProtoInstance name=\"flower\"/>

          )))

X3D0.toFileX3D("./future/./flowers_RoundTrip.x3d")
