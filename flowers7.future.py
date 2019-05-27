import x3dpsail


X3D0 = (x3dpsail.X3D().setProfile(x3dpsail.SFString("Immersive")).setVersion(x3dpsail.SFString("3.3"))
      .setHead(x3dpsail.head()
        .addComponent(x3dpsail.component().setName(x3dpsail.SFString("Shaders")).setLevel(x3dpsail.SFInt32(1)))
        .addComponent(x3dpsail.component().setName(x3dpsail.SFString("CubeMapTexturing")).setLevel(x3dpsail.SFInt32(1)))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("title")).setContent(x3dpsail.SFString("flowers7.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("creator")).setContent(x3dpsail.SFString("John Carlson")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("generator")).setContent(x3dpsail.SFString("manual")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("identifier")).setContent(x3dpsail.SFString("https://coderextreme.net/X3DJSONLD/flowers7.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("description")).setContent(x3dpsail.SFString("a flower"))))
      .setScene(x3dpsail.Scene()
        .addChild(x3dpsail.NavigationInfo())
        #Images courtesy of Paul Debevec's Light Probe Image Gallery

        .addChild(x3dpsail.Background().setDEF(x3dpsail.SFString("background")).setBackUrl(x3dpsail.MFString(["../resources/images/all_probes/beach_cross/beach_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_back.png"])).setBottomUrl(x3dpsail.MFString(["../resources/images/all_probes/beach_cross/beach_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_bottom.png"])).setFrontUrl(x3dpsail.MFString(["../resources/images/all_probes/beach_cross/beach_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_front.png"])).setLeftUrl(x3dpsail.MFString(["../resources/images/all_probes/beach_cross/beach_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_left.png"])).setRightUrl(x3dpsail.MFString(["../resources/images/all_probes/beach_cross/beach_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_right.png"])).setTopUrl(x3dpsail.MFString(["../resources/images/all_probes/beach_cross/beach_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_top.png"])))
        .addChild(x3dpsail.Viewpoint().setPosition(x3dpsail.SFVec3f(0,0,40)).setDescription(x3dpsail.SFString("Transparent rose")))
        .addChild(x3dpsail.Transform().setDEF(x3dpsail.SFString("Rose01"))
          .addChild(x3dpsail.Shape()
            .setAppearance(x3dpsail.Appearance()
              .setMaterial(x3dpsail.Material().setDiffuseColor(x3dpsail.SFColor(0.7,0.7,0.7)).setSpecularColor(x3dpsail.SFColor(0.5,0.5,0.5)))
              .setTexture(x3dpsail.ComposedCubeMapTexture().setDEF(x3dpsail.SFString("texture"))
                .setBack(x3dpsail.ImageTexture().setDEF(x3dpsail.SFString("backShader")).setUrl(x3dpsail.MFString(["../resources/images/all_probes/beach_cross/beach_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_back.png"])))
                .setBottom(x3dpsail.ImageTexture().setDEF(x3dpsail.SFString("bottomShader")).setUrl(x3dpsail.MFString(["../resources/images/all_probes/beach_cross/beach_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_bottom.png"])))
                .setFront(x3dpsail.ImageTexture().setDEF(x3dpsail.SFString("frontShader")).setUrl(x3dpsail.MFString(["../resources/images/all_probes/beach_cross/beach_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_front.png"])))
                .setLeft(x3dpsail.ImageTexture().setDEF(x3dpsail.SFString("leftShader")).setUrl(x3dpsail.MFString(["../resources/images/all_probes/beach_cross/beach_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_left.png"])))
                .setRight(x3dpsail.ImageTexture().setDEF(x3dpsail.SFString("rightShader")).setUrl(x3dpsail.MFString(["../resources/images/all_probes/beach_cross/beach_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_right.png"])))
                .setTop(x3dpsail.ImageTexture().setDEF(x3dpsail.SFString("topShader")).setUrl(x3dpsail.MFString(["../resources/images/all_probes/beach_cross/beach_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/beach_cross/beach_top.png"]))))
              .addShaders(x3dpsail.ComposedShader().setDEF(x3dpsail.SFString("x3dom")).setLanguage(x3dpsail.SFString("GLSL"))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("cube")).setType(x3dpsail.SFString("SFInt32")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("0")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("chromaticDispertion")).setAccessType(x3dpsail.SFString("initializeOnly")).setType(x3dpsail.SFString("SFVec3f")).setValue(x3dpsail.SFString("0.98 1 1.033")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("bias")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("0.5")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("scale")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("0.5")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("power")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("2")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("a")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("10")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("b")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("1")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("c")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("20")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("d")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("20")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("tdelta")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("0")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("pdelta")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("0")))
                #field name='cube' type='SFNode' accessType=\"inputOutput\"> <ComposedCubeMapTexture USE=\"texture\"/> </field

                .addParts(x3dpsail.ShaderPart().setUrl(x3dpsail.MFString(["../shaders/x3dom_flowers_chromatic.vs","https://coderextreme.net/X3DJSONLD/shaders/x3dom_flowers_chromatic.vs"])).setType(x3dpsail.SFString("VERTEX")))
                .addParts(x3dpsail.ShaderPart().setUrl(x3dpsail.MFString(["../shaders/pc_bubbles.fs","https://coderextreme.net/X3DJSONLD/shaders/common.fs"])).setType(x3dpsail.SFString("FRAGMENT"))))
              .addShaders(x3dpsail.ComposedShader().setDEF(x3dpsail.SFString("cobweb")).setLanguage(x3dpsail.SFString("GLSL"))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("cube")).setType(x3dpsail.SFString("SFNode")).setAccessType(x3dpsail.SFString("inputOutput"))
                  .addChild(x3dpsail.ComposedCubeMapTexture().setUSE(x3dpsail.SFString("texture"))))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("chromaticDispertion")).setAccessType(x3dpsail.SFString("initializeOnly")).setType(x3dpsail.SFString("SFVec3f")).setValue(x3dpsail.SFString("0.98 1 1.033")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("bias")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOnly")).setValue(x3dpsail.SFString("0.5")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("scale")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOnly")).setValue(x3dpsail.SFString("0.5")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("power")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOnly")).setValue(x3dpsail.SFString("2")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("a")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOnly")).setValue(x3dpsail.SFString("10")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("b")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOnly")).setValue(x3dpsail.SFString("1")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("c")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOnly")).setValue(x3dpsail.SFString("20")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("d")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOnly")).setValue(x3dpsail.SFString("20")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("tdelta")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOnly")).setValue(x3dpsail.SFString("0")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("pdelta")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOnly")).setValue(x3dpsail.SFString("0")))
                .addParts(x3dpsail.ShaderPart().setUrl(x3dpsail.MFString(["../shaders/cobweb_flowers_chromatic.vs","https://coderextreme.net/X3DJSONLD/shaders/cobweb_flowers_chromatic.vs"])).setType(x3dpsail.SFString("VERTEX")))
                .addParts(x3dpsail.ShaderPart().setUrl(x3dpsail.MFString(["../shaders/common.fs","https://coderextreme.net/X3DJSONLD/shaders/common.fs"])).setType(x3dpsail.SFString("FRAGMENT")))))
            .setGeometry(x3dpsail.Sphere().setSolid(x3dpsail.SFBool(False)))))
        .addChild(x3dpsail.Script().setDEF(x3dpsail.SFString("UrlSelector")).setDirectOutput(x3dpsail.SFBool(True))
          .addField(x3dpsail.field().setName(x3dpsail.SFString("frontUrls")).setType(x3dpsail.SFString("MFString")).setAccessType(x3dpsail.SFString("initializeOnly")).setValue(x3dpsail.SFString("\"../resources/images/all_probes/beach_cross/beach_front.png\" \"../resources/images/all_probes/building_cross/building_front.png\" \"../resources/images/all_probes/campus_cross/campus_front.png\" \"../resources/images/all_probes/galileo_cross/galileo_front.png\" \"../resources/images/all_probes/grace_cross/grace_front.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_front.png\" \"../resources/images/all_probes/rnl_cross/rnl_front.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_front.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_front.png\"")))
          .addField(x3dpsail.field().setName(x3dpsail.SFString("backUrls")).setType(x3dpsail.SFString("MFString")).setAccessType(x3dpsail.SFString("initializeOnly")).setValue(x3dpsail.SFString("\"../resources/images/all_probes/beach_cross/beach_back.png\" \"../resources/images/all_probes/building_cross/building_back.png\" \"../resources/images/all_probes/campus_cross/campus_back.png\" \"../resources/images/all_probes/galileo_cross/galileo_back.png\" \"../resources/images/all_probes/grace_cross/grace_back.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_back.png\" \"../resources/images/all_probes/rnl_cross/rnl_back.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_back.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_back.png\"")))
          .addField(x3dpsail.field().setName(x3dpsail.SFString("leftUrls")).setType(x3dpsail.SFString("MFString")).setAccessType(x3dpsail.SFString("initializeOnly")).setValue(x3dpsail.SFString("\"../resources/images/all_probes/beach_cross/beach_left.png\" \"../resources/images/all_probes/building_cross/building_left.png\" \"../resources/images/all_probes/campus_cross/campus_left.png\" \"../resources/images/all_probes/galileo_cross/galileo_left.png\" \"../resources/images/all_probes/grace_cross/grace_left.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_left.png\" \"../resources/images/all_probes/rnl_cross/rnl_left.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_left.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_left.png\"")))
          .addField(x3dpsail.field().setName(x3dpsail.SFString("rightUrls")).setType(x3dpsail.SFString("MFString")).setAccessType(x3dpsail.SFString("initializeOnly")).setValue(x3dpsail.SFString("\"../resources/images/all_probes/beach_cross/beach_right.png\" \"../resources/images/all_probes/building_cross/building_right.png\" \"../resources/images/all_probes/campus_cross/campus_right.png\" \"../resources/images/all_probes/galileo_cross/galileo_right.png\" \"../resources/images/all_probes/grace_cross/grace_right.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_right.png\" \"../resources/images/all_probes/rnl_cross/rnl_right.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_right.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_right.png\"")))
          .addField(x3dpsail.field().setName(x3dpsail.SFString("topUrls")).setType(x3dpsail.SFString("MFString")).setAccessType(x3dpsail.SFString("initializeOnly")).setValue(x3dpsail.SFString("\"../resources/images/all_probes/beach_cross/beach_top.png\" \"../resources/images/all_probes/building_cross/building_top.png\" \"../resources/images/all_probes/campus_cross/campus_top.png\" \"../resources/images/all_probes/galileo_cross/galileo_top.png\" \"../resources/images/all_probes/grace_cross/grace_top.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_top.png\" \"../resources/images/all_probes/rnl_cross/rnl_top.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_top.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_top.png\"")))
          .addField(x3dpsail.field().setName(x3dpsail.SFString("bottomUrls")).setType(x3dpsail.SFString("MFString")).setAccessType(x3dpsail.SFString("initializeOnly")).setValue(x3dpsail.SFString("\"../resources/images/all_probes/beach_cross/beach_bottom.png\" \"../resources/images/all_probes/building_cross/building_bottom.png\" \"../resources/images/all_probes/campus_cross/campus_bottom.png\" \"../resources/images/all_probes/galileo_cross/galileo_bottom.png\" \"../resources/images/all_probes/grace_cross/grace_bottom.png\" \"../resources/images/all_probes/kitchen_cross/kitchen_bottom.png\" \"../resources/images/all_probes/rnl_cross/rnl_bottom.png\" \"../resources/images/all_probes/stpeters_cross/stpeters_bottom.png\" \"../resources/images/all_probes/uffizi_cross/uffizi_bottom.png\"")))
          .addField(x3dpsail.field().setName(x3dpsail.SFString("front")).setType(x3dpsail.SFString("MFString")).setAccessType(x3dpsail.SFString("inputOutput")))
          .addField(x3dpsail.field().setName(x3dpsail.SFString("back")).setType(x3dpsail.SFString("MFString")).setAccessType(x3dpsail.SFString("inputOutput")))
          .addField(x3dpsail.field().setName(x3dpsail.SFString("left")).setType(x3dpsail.SFString("MFString")).setAccessType(x3dpsail.SFString("inputOutput")))
          .addField(x3dpsail.field().setName(x3dpsail.SFString("right")).setType(x3dpsail.SFString("MFString")).setAccessType(x3dpsail.SFString("inputOutput")))
          .addField(x3dpsail.field().setName(x3dpsail.SFString("top")).setType(x3dpsail.SFString("MFString")).setAccessType(x3dpsail.SFString("inputOutput")))
          .addField(x3dpsail.field().setName(x3dpsail.SFString("bottom")).setType(x3dpsail.SFString("MFString")).setAccessType(x3dpsail.SFString("inputOutput")))
          .addField(x3dpsail.field().setName(x3dpsail.SFString("set_fraction")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOnly")))
          .addField(x3dpsail.field().setName(x3dpsail.SFString("old")).setType(x3dpsail.SFString("SFInt32")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("-1"))).setSourceCode('''ecmascript:\n"+
"        function set_fraction( f, tm ) {\n"+
"            var side = Math.floor(f*frontUrls.length);\n"+
"            if (side > frontUrls.length-1) {\n"+
"                side = 0;\n"+
"            }\n"+
"            if (side != old) {\n"+
"                    old = side;\n"+
"                    front[0] = frontUrls[side];\n"+
"                    back[0] = backUrls[side];\n"+
"                    left[0] = leftUrls[side];\n"+
"                    right[0] = rightUrls[side];\n"+
"                    top[0] = topUrls[side];\n"+
"                    bottom[0] = bottomUrls[side];\n"+
"            }\n"+
"        }''')
)
        #<TimeSensor DEF=\"Clock\" cycleInterval=\"45\" loop='true'/> <ROUTE fromNode='Clock' fromField='fraction_changed' toNode='UrlSelector' toField='set_fraction'/> <ROUTE fromNode='UrlSelector' fromField='front' toNode='background' toField='frontUrl'/> <ROUTE fromNode='UrlSelector' fromField='back' toNode='background' toField='backUrl'/> <ROUTE fromNode='UrlSelector' fromField='left' toNode='background' toField='leftUrl'/> <ROUTE fromNode='UrlSelector' fromField='right' toNode='background' toField='rightUrl'/> <ROUTE fromNode='UrlSelector' fromField='top' toNode='background' toField='topUrl'/> <ROUTE fromNode='UrlSelector' fromField='bottom' toNode='background' toField='bottomUrl'/> <ROUTE fromNode='UrlSelector' fromField='front' toNode='frontShader' toField='url'/> <ROUTE fromNode='UrlSelector' fromField='back' toNode='backShader' toField='url'/> <ROUTE fromNode='UrlSelector' fromField='left' toNode='leftShader' toField='url'/> <ROUTE fromNode='UrlSelector' fromField='right' toNode='rightShader' toField='url'/> <ROUTE fromNode='UrlSelector' fromField='top' toNode='topShader' toField='url'/> <ROUTE fromNode='UrlSelector' fromField='bottom' toNode='bottomShader' toField='url'/>

        .addChild(x3dpsail.Script().setDEF(x3dpsail.SFString("Animate")).setDirectOutput(x3dpsail.SFBool(True))
          .addField(x3dpsail.field().setName(x3dpsail.SFString("set_fraction")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOnly")))
          .addField(x3dpsail.field().setName(x3dpsail.SFString("a")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("10")))
          .addField(x3dpsail.field().setName(x3dpsail.SFString("b")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("1")))
          .addField(x3dpsail.field().setName(x3dpsail.SFString("c")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("20")))
          .addField(x3dpsail.field().setName(x3dpsail.SFString("d")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("20")))
          .addField(x3dpsail.field().setName(x3dpsail.SFString("tdelta")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("0")))
          .addField(x3dpsail.field().setName(x3dpsail.SFString("pdelta")).setType(x3dpsail.SFString("SFFloat")).setAccessType(x3dpsail.SFString("inputOutput")).setValue(x3dpsail.SFString("0"))).setSourceCode('''ecmascript:\n"+
"\n"+
"function set_fraction() {\n"+
"	var choice = Math.floor(Math.random() * 4);\n"+
"	if (choice == 0) {\n"+
"		a = a + Math.floor(Math.random() * 2) * 2 - 1;\n"+
"	} else if (choice == 1) {\n"+
"		b = b + Math.floor(Math.random() * 2) * 2 - 1;\n"+
"	} else if (choice == 2) {\n"+
"		c = c + Math.floor(Math.random() * 2) * 2 - 1;\n"+
"	} else if (choice == 3) {\n"+
"		d = d + Math.floor(Math.random() * 2) * 2 - 1;\n"+
"	}\n"+
"	tdelta = tdelta + 0.5;\n"+
"	pdelta = pdelta + 0.5;\n"+
"	if (a < 1) {\n"+
"		a = 10;\n"+
"	}\n"+
"	if (b < 1) {\n"+
"		b = 10;\n"+
"	}\n"+
"	if (c < 1) {\n"+
"		c = 4;\n"+
"	}\n"+
"	if (c > 20) {\n"+
"		c = 4;\n"+
"	}\n"+
"	if (d < 1) {\n"+
"		d = 4;\n"+
"	}\n"+
"	if (d > 20) {\n"+
"		d = 4;\n"+
"	}\n"+
"}''')
)
        .addChild(x3dpsail.TimeSensor().setDEF(x3dpsail.SFString("TourTime")).setCycleInterval(x3dpsail.SFTime(5)).setLoop(x3dpsail.SFBool(True)))
        .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("TourTime")).setFromField(x3dpsail.SFString("fraction_changed")).setToNode(x3dpsail.SFString("Animate")).setToField(x3dpsail.SFString("set_fraction")))
        .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("Animate")).setFromField(x3dpsail.SFString("a")).setToNode(x3dpsail.SFString("cobweb")).setToField(x3dpsail.SFString("a")))
        .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("Animate")).setFromField(x3dpsail.SFString("b")).setToNode(x3dpsail.SFString("cobweb")).setToField(x3dpsail.SFString("b")))
        .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("Animate")).setFromField(x3dpsail.SFString("c")).setToNode(x3dpsail.SFString("cobweb")).setToField(x3dpsail.SFString("c")))
        .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("Animate")).setFromField(x3dpsail.SFString("d")).setToNode(x3dpsail.SFString("cobweb")).setToField(x3dpsail.SFString("d")))
        .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("Animate")).setFromField(x3dpsail.SFString("pdelta")).setToNode(x3dpsail.SFString("cobweb")).setToField(x3dpsail.SFString("pdelta")))
        .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("Animate")).setFromField(x3dpsail.SFString("tdelta")).setToNode(x3dpsail.SFString("cobweb")).setToField(x3dpsail.SFString("tdelta")))
        .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("Animate")).setFromField(x3dpsail.SFString("a")).setToNode(x3dpsail.SFString("x3dom")).setToField(x3dpsail.SFString("a")))
        .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("Animate")).setFromField(x3dpsail.SFString("b")).setToNode(x3dpsail.SFString("x3dom")).setToField(x3dpsail.SFString("b")))
        .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("Animate")).setFromField(x3dpsail.SFString("c")).setToNode(x3dpsail.SFString("x3dom")).setToField(x3dpsail.SFString("c")))
        .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("Animate")).setFromField(x3dpsail.SFString("d")).setToNode(x3dpsail.SFString("x3dom")).setToField(x3dpsail.SFString("d")))
        .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("Animate")).setFromField(x3dpsail.SFString("pdelta")).setToNode(x3dpsail.SFString("x3dom")).setToField(x3dpsail.SFString("pdelta")))
        .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("Animate")).setFromField(x3dpsail.SFString("tdelta")).setToNode(x3dpsail.SFString("x3dom")).setToField(x3dpsail.SFString("tdelta")))))

X3D0.toFileX3D("./future/./flowers7_RoundTrip.x3d")
