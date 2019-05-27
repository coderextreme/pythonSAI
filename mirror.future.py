import x3dpsail


X3D0 = (x3dpsail.X3D().setProfile(x3dpsail.SFString("Immersive")).setVersion(x3dpsail.SFString("3.3"))
      .setHead(x3dpsail.head()
        .addComponent(x3dpsail.component().setName(x3dpsail.SFString("EnvironmentalEffects")).setLevel(x3dpsail.SFInt32(3)))
        .addComponent(x3dpsail.component().setName(x3dpsail.SFString("Shaders")).setLevel(x3dpsail.SFInt32(1)))
        .addComponent(x3dpsail.component().setName(x3dpsail.SFString("CubeMapTexturing")).setLevel(x3dpsail.SFInt32(1)))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("title")).setContent(x3dpsail.SFString("mirror.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("creator")).setContent(x3dpsail.SFString("John Carlson")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("generator")).setContent(x3dpsail.SFString("manual")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("identifier")).setContent(x3dpsail.SFString("https://coderextreme.net/X3DJSONLD/mirror.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("description")).setContent(x3dpsail.SFString("sphere with alternating backgrounds"))))
      .setScene(x3dpsail.Scene()
        .addChild(x3dpsail.Viewpoint().setPosition(x3dpsail.SFVec3f(0,5,100)).setDescription(x3dpsail.SFString("Switch background and images texture")))
        .addChild(x3dpsail.TextureBackground()
          .setLeftTexture(x3dpsail.ImageTexture().setDEF(x3dpsail.SFString("leftBack")).setUrl(x3dpsail.MFString(["../resources/images/all_probes/beach_cross/beach_left.png","https://coderextreme.net/images/all_probes/beach_cross/beach_left.png"])))
          .setRightTexture(x3dpsail.ImageTexture().setDEF(x3dpsail.SFString("rightBack")).setUrl(x3dpsail.MFString(["../resources/images/all_probes/beach_cross/beach_right.png","https://coderextreme.net/images/all_probes/beach_cross/beach_right.png"])))
          .setFrontTexture(x3dpsail.ImageTexture().setDEF(x3dpsail.SFString("frontBack")).setUrl(x3dpsail.MFString(["../resources/images/all_probes/beach_cross/beach_front.png","https://coderextreme.net/images/all_probes/beach_cross/beach_front.png"])))
          .setBackTexture(x3dpsail.ImageTexture().setDEF(x3dpsail.SFString("backBack")).setUrl(x3dpsail.MFString(["../resources/images/all_probes/beach_cross/beach_back.png","https://coderextreme.net/images/all_probes/beach_cross/beach_back.png"])))
          .setTopTexture(x3dpsail.ImageTexture().setDEF(x3dpsail.SFString("topBack")).setUrl(x3dpsail.MFString(["../resources/images/all_probes/beach_cross/beach_top.png","https://coderextreme.net/images/all_probes/beach_cross/beach_top.png"])))
          .setBottomTexture(x3dpsail.ImageTexture().setDEF(x3dpsail.SFString("bottomBack")).setUrl(x3dpsail.MFString(["../resources/images/all_probes/beach_cross/beach_bottom.png","https://coderextreme.net/images/all_probes/beach_cross/beach_bottom.png"]))))
        .addChild(x3dpsail.Transform()
          .addChild(x3dpsail.Shape()
            .setAppearance(x3dpsail.Appearance()
              .setMaterial(x3dpsail.Material().setDiffuseColor(x3dpsail.SFColor(0.7,0.7,0.7)).setSpecularColor(x3dpsail.SFColor(0.5,0.5,0.5)))
              .setTexture(x3dpsail.ComposedCubeMapTexture()
                .setBack(x3dpsail.ImageTexture().setDEF(x3dpsail.SFString("backShader")).setUrl(x3dpsail.MFString(["../resources/images/all_probes/beach_cross/beach_back.png","https://coderextreme.net/images/all_probes/beach_cross/beach_back.png"])))
                .setBottom(x3dpsail.ImageTexture().setDEF(x3dpsail.SFString("bottomShader")).setUrl(x3dpsail.MFString(["../resources/images/all_probes/beach_cross/beach_bottom.png","https://coderextreme.net/images/all_probes/beach_cross/beach_bottom.png"])))
                .setFront(x3dpsail.ImageTexture().setDEF(x3dpsail.SFString("frontShader")).setUrl(x3dpsail.MFString(["../resources/images/all_probes/beach_cross/beach_front.png","https://coderextreme.net/images/all_probes/beach_cross/beach_front.png"])))
                .setLeft(x3dpsail.ImageTexture().setDEF(x3dpsail.SFString("leftShader")).setUrl(x3dpsail.MFString(["../resources/images/all_probes/beach_cross/beach_left.png","https://coderextreme.net/images/all_probes/beach_cross/beach_left.png"])))
                .setRight(x3dpsail.ImageTexture().setDEF(x3dpsail.SFString("rightShader")).setUrl(x3dpsail.MFString(["../resources/images/all_probes/beach_cross/beach_right.png","https://coderextreme.net/images/all_probes/beach_cross/beach_right.png"])))
                .setTop(x3dpsail.ImageTexture().setDEF(x3dpsail.SFString("topShader")).setUrl(x3dpsail.MFString(["../resources/images/all_probes/beach_cross/beach_top.png","https://coderextreme.net/images/all_probes/beach_cross/beach_top.png"]))))
              .addShaders(x3dpsail.ComposedShader().setDEF(x3dpsail.SFString("x3dom")).setLanguage(x3dpsail.SFString("GLSL"))
                #http://hypertextbook.com/facts/2005/JustinChe.shtml

                .addField(x3dpsail.field().setName(x3dpsail.SFString("chromaticDispertion")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFVec3f")).setValue(x3dpsail.SFString("0.98 1 1.033")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("cube")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFInt32")).setValue(x3dpsail.SFString("0")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("bias")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("0.5")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("scale")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("0.5")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("power")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("2")))
                .addParts(x3dpsail.ShaderPart().setUrl(x3dpsail.MFString(["../shaders/x3dom.vs","https://coderextreme.net/X3DJSONLD/shaders/x3dom.vs"])).setType(x3dpsail.SFString("VERTEX")))
                .addParts(x3dpsail.ShaderPart().setUrl(x3dpsail.MFString(["../shaders/mix.fs","https://coderextreme.net/X3DJSONLD/shaders/mix.fs"])).setType(x3dpsail.SFString("FRAGMENT"))))
              .addShaders(x3dpsail.ComposedShader().setDEF(x3dpsail.SFString("cobweb")).setLanguage(x3dpsail.SFString("GLSL"))
                #http://hypertextbook.com/facts/2005/JustinChe.shtml

                .addField(x3dpsail.field().setName(x3dpsail.SFString("chromaticDispertion")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFVec3f")).setValue(x3dpsail.SFString("0.98 1 1.033")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("cube")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFInt32")).setValue(x3dpsail.SFString("0")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("bias")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("0.5")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("scale")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("0.5")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("power")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("2")))
                .addParts(x3dpsail.ShaderPart().setUrl(x3dpsail.MFString(["../shaders/cobweb.vs","https://coderextreme.net/X3DJSONLD/shaders/cobweb.vs"])).setType(x3dpsail.SFString("VERTEX")))
                .addParts(x3dpsail.ShaderPart().setUrl(x3dpsail.MFString(["../shaders/mix.fs","https://coderextreme.net/X3DJSONLD/shaders/mix.fs"])).setType(x3dpsail.SFString("FRAGMENT")))))
            .setGeometry(x3dpsail.Sphere().setRadius(x3dpsail.SFFloat(30))))
          .addChild(x3dpsail.Script().setDEF(x3dpsail.SFString("UrlSelector")).setDirectOutput(x3dpsail.SFBool(True))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("frontUrls")).setType(x3dpsail.SFString("MFString")).setAccessType(x3dpsail.SFString("initializeOnly")).setValue(x3dpsail.SFString("\"../resources/images/all_probes/beach_cross/beach_front.png\" \"../resources/images/all_probes/building_cross/building_front.png\" \"../resources/images/all_probes/campus_cross/campus_front.png\" \"../resources/images/all_probes/galileo_cross/galileo_front.png\" \"../resources/images/all_probes/grace_cross/grace_front.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_front.png\" \"../resources/images/all_probes/rnl_cross/rnl_front.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_front.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_front.png\"")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("backUrls")).setType(x3dpsail.SFString("MFString")).setAccessType(x3dpsail.SFString("initializeOnly")).setValue(x3dpsail.SFString("\"../resources/images/all_probes/beach_cross/beach_back.png\" \"../resources/images/all_probes/building_cross/building_back.png\" \"../resources/images/all_probes/campus_cross/campus_back.png\" \"../resources/images/all_probes/galileo_cross/galileo_back.png\" \"../resources/images/all_probes/grace_cross/grace_back.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_back.png\" \"../resources/images/all_probes/rnl_cross/rnl_back.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_back.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_back.png\"")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("leftUrls")).setType(x3dpsail.SFString("MFString")).setAccessType(x3dpsail.SFString("initializeOnly")).setValue(x3dpsail.SFString("\"../resources/images/all_probes/beach_cross/beach_left.png\" \"../resources/images/all_probes/building_cross/building_left.png\" \"../resources/images/all_probes/campus_cross/campus_left.png\" \"../resources/images/all_probes/galileo_cross/galileo_left.png\" \"../resources/images/all_probes/grace_cross/grace_left.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_left.png\" \"../resources/images/all_probes/rnl_cross/rnl_left.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_left.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_left.png\"")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("rightUrls")).setType(x3dpsail.SFString("MFString")).setAccessType(x3dpsail.SFString("initializeOnly")).setValue(x3dpsail.SFString("\"../resources/images/all_probes/beach_cross/beach_right.png\" \"../resources/images/all_probes/building_cross/building_right.png\" \"../resources/images/all_probes/campus_cross/campus_right.png\" \"../resources/images/all_probes/galileo_cross/galileo_right.png\" \"../resources/images/all_probes/grace_cross/grace_right.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_right.png\" \"../resources/images/all_probes/rnl_cross/rnl_right.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_right.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_right.png\"")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("topUrls")).setType(x3dpsail.SFString("MFString")).setAccessType(x3dpsail.SFString("initializeOnly")).setValue(x3dpsail.SFString("\"../resources/images/all_probes/beach_cross/beach_top.png\" \"../resources/images/all_probes/building_cross/building_top.png\" \"../resources/images/all_probes/campus_cross/campus_top.png\" \"../resources/images/all_probes/galileo_cross/galileo_top.png\" \"../resources/images/all_probes/grace_cross/grace_top.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_top.png\" \"../resources/images/all_probes/rnl_cross/rnl_top.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_top.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_top.png\"")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("bottomUrls")).setType(x3dpsail.SFString("MFString")).setAccessType(x3dpsail.SFString("initializeOnly")).setValue(x3dpsail.SFString("\"../resources/images/all_probes/beach_cross/beach_bottom.png\" \"../resources/images/all_probes/building_cross/building_bottom.png\" \"../resources/images/all_probes/campus_cross/campus_bottom.png\" \"../resources/images/all_probes/galileo_cross/galileo_bottom.png\" \"../resources/images/all_probes/grace_cross/grace_bottom.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_bottom.png\" \"../resources/images/all_probes/rnl_cross/rnl_bottom.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_bottom.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_bottom.png\"")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("front_changed")).setType(x3dpsail.SFString("MFString")).setAccessType(x3dpsail.SFString("outputOnly")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("back_changed")).setType(x3dpsail.SFString("MFString")).setAccessType(x3dpsail.SFString("outputOnly")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("left_changed")).setType(x3dpsail.SFString("MFString")).setAccessType(x3dpsail.SFString("outputOnly")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("right_changed")).setType(x3dpsail.SFString("MFString")).setAccessType(x3dpsail.SFString("outputOnly")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("top_changed")).setType(x3dpsail.SFString("MFString")).setAccessType(x3dpsail.SFString("outputOnly")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("bottom_changed")).setType(x3dpsail.SFString("MFString")).setAccessType(x3dpsail.SFString("outputOnly")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("set_fraction")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOnly")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("old")).setType(x3dpsail.SFString("SFInt32")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("-1"))).setSourceCode('''ecmascript:\n"+
"        function set_fraction( f, tm ) {\n"+
"	    var side = Math.floor(f*frontUrls.length);\n"+
"	    if (side > frontUrls.length-1) {\n"+
"	    	side = 0;\n"+
"	    }\n"+
"	    if (side != old) {\n"+
"	    	    Browser.print(f+\" \"+side);\n"+
"	    	    old = side;\n"+
"		    front_changed[0] = frontUrls[side];\n"+
"		    back_changed[0] = backUrls[side];\n"+
"		    left_changed[0] = leftUrls[side];\n"+
"		    right_changed[0] = rightUrls[side];\n"+
"		    top_changed[0] = topUrls[side];\n"+
"		    bottom_changed[0] = bottomUrls[side];\n"+
"            }\n"+
"        }''')
)
          .addChild(x3dpsail.TimeSensor().setDEF(x3dpsail.SFString("Clock")).setCycleInterval(x3dpsail.SFTime(45)).setLoop(x3dpsail.SFBool(True)))
          .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("Clock")).setFromField(x3dpsail.SFString("fraction_changed")).setToNode(x3dpsail.SFString("UrlSelector")).setToField(x3dpsail.SFString("set_fraction")))
          .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("UrlSelector")).setFromField(x3dpsail.SFString("front_changed")).setToNode(x3dpsail.SFString("frontBack")).setToField(x3dpsail.SFString("url")))
          .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("UrlSelector")).setFromField(x3dpsail.SFString("back_changed")).setToNode(x3dpsail.SFString("backBack")).setToField(x3dpsail.SFString("url")))
          .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("UrlSelector")).setFromField(x3dpsail.SFString("left_changed")).setToNode(x3dpsail.SFString("leftBack")).setToField(x3dpsail.SFString("url")))
          .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("UrlSelector")).setFromField(x3dpsail.SFString("right_changed")).setToNode(x3dpsail.SFString("rightBack")).setToField(x3dpsail.SFString("url")))
          .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("UrlSelector")).setFromField(x3dpsail.SFString("top_changed")).setToNode(x3dpsail.SFString("topBack")).setToField(x3dpsail.SFString("url")))
          .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("UrlSelector")).setFromField(x3dpsail.SFString("bottom_changed")).setToNode(x3dpsail.SFString("bottomBack")).setToField(x3dpsail.SFString("url")))
          .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("UrlSelector")).setFromField(x3dpsail.SFString("front_changed")).setToNode(x3dpsail.SFString("frontShader")).setToField(x3dpsail.SFString("url")))
          .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("UrlSelector")).setFromField(x3dpsail.SFString("back_changed")).setToNode(x3dpsail.SFString("backShader")).setToField(x3dpsail.SFString("url")))
          .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("UrlSelector")).setFromField(x3dpsail.SFString("left_changed")).setToNode(x3dpsail.SFString("leftShader")).setToField(x3dpsail.SFString("url")))
          .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("UrlSelector")).setFromField(x3dpsail.SFString("right_changed")).setToNode(x3dpsail.SFString("rightShader")).setToField(x3dpsail.SFString("url")))
          .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("UrlSelector")).setFromField(x3dpsail.SFString("top_changed")).setToNode(x3dpsail.SFString("topShader")).setToField(x3dpsail.SFString("url")))
          .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("UrlSelector")).setFromField(x3dpsail.SFString("bottom_changed")).setToNode(x3dpsail.SFString("bottomShader")).setToField(x3dpsail.SFString("url"))))))

X3D0.toFileX3D("./future/./mirror_RoundTrip.x3d")
