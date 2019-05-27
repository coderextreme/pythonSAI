import x3dpsail


X3D0 = (x3dpsail.X3D().setProfile(x3dpsail.SFString("Immersive")).setVersion(x3dpsail.SFString("3.3"))
      .setHead(x3dpsail.head()
        .addComponent(x3dpsail.component().setName(x3dpsail.SFString("EnvironmentalEffects")).setLevel(x3dpsail.SFInt32(1)))
        .addComponent(x3dpsail.component().setName(x3dpsail.SFString("EnvironmentalEffects")).setLevel(x3dpsail.SFInt32(3)))
        .addComponent(x3dpsail.component().setName(x3dpsail.SFString("Shaders")).setLevel(x3dpsail.SFInt32(1)))
        .addComponent(x3dpsail.component().setName(x3dpsail.SFString("CubeMapTexturing")).setLevel(x3dpsail.SFInt32(1)))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("title")).setContent(x3dpsail.SFString("bubbles.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("creator")).setContent(x3dpsail.SFString("John Carlson")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("generator")).setContent(x3dpsail.SFString("manual")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("identifier")).setContent(x3dpsail.SFString("https://coderextreme.net/X3DJSONLD/bubbles.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("description")).setContent(x3dpsail.SFString("not sure what this is"))))
      .setScene(x3dpsail.Scene()
        .addChild(x3dpsail.NavigationInfo().setType(x3dpsail.MFString(["EXAMINE"])))
        .addChild(x3dpsail.Viewpoint().setDEF(x3dpsail.SFString("Tour")).setDescription(x3dpsail.SFString("Tour Views")))
        .addChild(x3dpsail.Viewpoint().setPosition(x3dpsail.SFVec3f(0,0,4)).setDescription(x3dpsail.SFString("sphere in road")))
        .addChild(x3dpsail.Background().setBackUrl(x3dpsail.MFString(["../resources/images/all_probes/uffizi_cross/uffizi_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_back.png"])).setBottomUrl(x3dpsail.MFString(["../resources/images/all_probes/uffizi_cross/uffizi_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_bottom.png"])).setFrontUrl(x3dpsail.MFString(["../resources/images/all_probes/uffizi_cross/uffizi_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_front.png"])).setLeftUrl(x3dpsail.MFString(["../resources/images/all_probes/uffizi_cross/uffizi_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_left.png"])).setRightUrl(x3dpsail.MFString(["../resources/images/all_probes/uffizi_cross/uffizi_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_right.png"])).setTopUrl(x3dpsail.MFString(["../resources/images/all_probes/uffizi_cross/uffizi_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_top.png"])))
        .addChild(x3dpsail.Transform().setDEF(x3dpsail.SFString("Rose01"))
          .addChild(x3dpsail.Shape()
            .setGeometry(x3dpsail.Sphere())
            .setAppearance(x3dpsail.Appearance().setDEF(x3dpsail.SFString("_01_-_Default"))
              .setMaterial(x3dpsail.Material().setDiffuseColor(x3dpsail.SFColor(0.7,0.7,0.7)).setSpecularColor(x3dpsail.SFColor(0.5,0.5,0.5)))
              .setTexture(x3dpsail.ComposedCubeMapTexture()
                .setBack(x3dpsail.ImageTexture().setUrl(x3dpsail.MFString(["../resources/images/all_probes/uffizi_cross/uffizi_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_back.png"])))
                .setBottom(x3dpsail.ImageTexture().setUrl(x3dpsail.MFString(["../resources/images/all_probes/uffizi_cross/uffizi_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_bottom.png"])))
                .setFront(x3dpsail.ImageTexture().setUrl(x3dpsail.MFString(["../resources/images/all_probes/uffizi_cross/uffizi_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_front.png"])))
                .setLeft(x3dpsail.ImageTexture().setUrl(x3dpsail.MFString(["../resources/images/all_probes/uffizi_cross/uffizi_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_left.png"])))
                .setRight(x3dpsail.ImageTexture().setUrl(x3dpsail.MFString(["../resources/images/all_probes/uffizi_cross/uffizi_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_right.png"])))
                .setTop(x3dpsail.ImageTexture().setUrl(x3dpsail.MFString(["../resources/images/all_probes/uffizi_cross/uffizi_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_top.png"]))))
              .addShaders(x3dpsail.ComposedShader().setDEF(x3dpsail.SFString("cobweb")).setLanguage(x3dpsail.SFString("GLSL"))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("cube")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFInt32")).setValue(x3dpsail.SFString("0")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("chromaticDispertion")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFVec3f")).setValue(x3dpsail.SFString("0.98 1 1.033")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("bias")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("0.5")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("scale")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("0.5")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("power")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("2")))
                .addParts(x3dpsail.ShaderPart().setUrl(x3dpsail.MFString(["../shaders/cobweb.vs","https://coderextreme.net/X3DJSONLD/shaders/cobweb.vs"])).setType(x3dpsail.SFString("VERTEX")))
                .addParts(x3dpsail.ShaderPart().setUrl(x3dpsail.MFString(["../shaders/pc_bubbles.fs","https://coderextreme.net/X3DJSONLD/shaders/pc_bubbles.fs"])).setType(x3dpsail.SFString("FRAGMENT"))))
              .addShaders(x3dpsail.ComposedShader().setDEF(x3dpsail.SFString("x3dom")).setLanguage(x3dpsail.SFString("GLSL"))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("cube")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFInt32")).setValue(x3dpsail.SFString("0")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("chromaticDispertion")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFVec3f")).setValue(x3dpsail.SFString("0.98 1 1.033")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("bias")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("0.5")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("scale")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("0.5")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("power")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("2")))
                .addParts(x3dpsail.ShaderPart().setUrl(x3dpsail.MFString(["../shaders/x3dom.vs","https://coderextreme.net/X3DJSONLD/shaders/x3dom.vs"])).setType(x3dpsail.SFString("VERTEX")))
                .addParts(x3dpsail.ShaderPart().setUrl(x3dpsail.MFString(["../shaders/pc_bubbles.fs","https://coderextreme.net/X3DJSONLD/shaders/pc_bubbles.fs"])).setType(x3dpsail.SFString("FRAGMENT")))))))
        .addChild(x3dpsail.TimeSensor().setDEF(x3dpsail.SFString("TourTime")).setCycleInterval(x3dpsail.SFTime(5)).setLoop(x3dpsail.SFBool(True)))
        .addChild(x3dpsail.PositionInterpolator().setDEF(x3dpsail.SFString("TourPosition")).setKey(x3dpsail.MFFloat([0,1])).setKeyValue(x3dpsail.MFVec3f([0,0,10,0,0,-10])))
        .addChild(x3dpsail.OrientationInterpolator().setDEF(x3dpsail.SFString("TourOrientation")).setKey(x3dpsail.MFFloat([0,1])).setKeyValue(x3dpsail.MFRotation([0,1,0,0,0,1,0,3.1416])))
        .addChild(x3dpsail.Script().setDEF(x3dpsail.SFString("RandomTourTime"))
          .addField(x3dpsail.field().setName(x3dpsail.SFString("set_cycle")).setAccessType(x3dpsail.SFString("inputOnly")).setType(x3dpsail.SFString("SFTime")))
          .addField(x3dpsail.field().setName(x3dpsail.SFString("lastKey")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("0")))
          .addField(x3dpsail.field().setName(x3dpsail.SFString("orientations")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("MFRotation")).setValue(x3dpsail.SFString("0 1 0 0 0 1 0 -1.57 0 1 0 3.14 0 1 0 1.57 0 1 0 0 1 0 0 -1.57 0 1 0 0 1 0 0 1.57 0 1 0 0")))
          .addField(x3dpsail.field().setName(x3dpsail.SFString("positions")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("MFVec3f")).setValue(x3dpsail.SFString("0 0 10 -10 0 0 0 0 -10 10 0 0 0 0 10 0 10 0 0 0 10 0 -10 0 0 0 10")))
          .addField(x3dpsail.field().setName(x3dpsail.SFString("position_changed")).setAccessType(x3dpsail.SFString("outputOnly")).setType(x3dpsail.SFString("MFVec3f")))
          .addField(x3dpsail.field().setName(x3dpsail.SFString("set_orientation")).setAccessType(x3dpsail.SFString("inputOnly")).setType(x3dpsail.SFString("MFRotation")))
          .addField(x3dpsail.field().setName(x3dpsail.SFString("orientation_changed")).setAccessType(x3dpsail.SFString("outputOnly")).setType(x3dpsail.SFString("MFRotation"))).setSourceCode('''ecmascript:\n"+
"               function set_cycle(value) {\n"+
"                        var ov = lastKey;\n"+
"                        do {\n"+
"                            lastKey = Math.round(Math.random()*(positions.length-1));\n"+
"                        } while (lastKey === ov);\n"+
"                        var vc = lastKey;\n"+
"\n"+
"                        orientation_changed = new MFRotation();\n"+
"                        orientation_changed[0] = new SFRotation(orientations[ov].x, orientations[ov].y, orientations[ov].z, orientations[ov].w);\n"+
"                        orientation_changed[1] = new SFRotation(orientations[vc].x, orientations[vc].y, orientations[vc].z, orientations[vc].w);\n"+
"                        position_changed = new MFVec3f();\n"+
"                        position_changed[0] = new SFVec3f(positions[ov].x,positions[ov].y,positions[ov].z);\n"+
"                        position_changed[1] = new SFVec3f(positions[vc].x,positions[vc].y,positions[vc].z);\n"+
"                    // }\n"+
"               }''')
)
        .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("TourTime")).setFromField(x3dpsail.SFString("cycleTime_changed")).setToNode(x3dpsail.SFString("RandomTourTime")).setToField(x3dpsail.SFString("set_cycle")))
        .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("RandomTourTime")).setFromField(x3dpsail.SFString("orientation_changed")).setToNode(x3dpsail.SFString("TourOrientation")).setToField(x3dpsail.SFString("set_keyValue")))
        .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("RandomTourTime")).setFromField(x3dpsail.SFString("position_changed")).setToNode(x3dpsail.SFString("TourPosition")).setToField(x3dpsail.SFString("set_keyValue")))
        .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("TourTime")).setFromField(x3dpsail.SFString("fraction_changed")).setToNode(x3dpsail.SFString("TourOrientation")).setToField(x3dpsail.SFString("set_fraction")))
        .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("TourOrientation")).setFromField(x3dpsail.SFString("value_changed")).setToNode(x3dpsail.SFString("Tour")).setToField(x3dpsail.SFString("set_orientation")))
        .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("TourTime")).setFromField(x3dpsail.SFString("fraction_changed")).setToNode(x3dpsail.SFString("TourPosition")).setToField(x3dpsail.SFString("set_fraction")))
        .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("TourPosition")).setFromField(x3dpsail.SFString("value_changed")).setToNode(x3dpsail.SFString("Tour")).setToField(x3dpsail.SFString("set_position")))))

X3D0.toFileX3D("./future/./bubbles_RoundTrip.x3d")
