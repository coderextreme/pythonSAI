import x3dpsail


X3D0 = (x3dpsail.X3D().setProfile(x3dpsail.SFString("Immersive")).setVersion(x3dpsail.SFString("3.3"))
      .setHead(x3dpsail.head()
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("title")).setContent(x3dpsail.SFString("geo.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("creator")).setContent(x3dpsail.SFString("John Carlson")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("description")).setContent(x3dpsail.SFString("Tour around a prismatic sphere")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("generator")).setContent(x3dpsail.SFString("X3D-Edit, https://savage.nps.edu/X3D-Edit")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("identifier")).setContent(x3dpsail.SFString("https://coderextreme.net/X3DJSONLD/geo.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("translated")).setContent(x3dpsail.SFString("13 March 2016")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("generator")).setContent(x3dpsail.SFString("X3dToJson.xslt, http://www.web3d.org/x3d/stylesheets/X3dToJson.html"))))
      .setScene(x3dpsail.Scene()
        .addChild(x3dpsail.NavigationInfo().setType(x3dpsail.MFString(["EXAMINE"])))
        .addChild(x3dpsail.Viewpoint().setPosition(x3dpsail.SFVec3f(0,0,4)).setOrientation(x3dpsail.SFRotation(1,0,0,0)).setDescription(x3dpsail.SFString("Bubbles in action")))
        .addChild(x3dpsail.Background().setBackUrl(x3dpsail.MFString(["../resources/images/BK.png","https://coderextreme.net/X3DJSONLD/images/BK.png"])).setBottomUrl(x3dpsail.MFString(["../resources/images/BT.png","https://coderextreme.net/X3DJSONLD/images/BT.png"])).setFrontUrl(x3dpsail.MFString(["../resources/images/FR.png","https://coderextreme.net/X3DJSONLD/images/FR.png"])).setLeftUrl(x3dpsail.MFString(["../resources/images/LF.png","https://coderextreme.net/X3DJSONLD/images/LF.png"])).setRightUrl(x3dpsail.MFString(["../resources/images/RT.png","https://coderextreme.net/X3DJSONLD/images/RT.png"])).setTopUrl(x3dpsail.MFString(["../resources/images/TP.png","https://coderextreme.net/X3DJSONLD/images/TP.png"])))
        .addChild(x3dpsail.ProtoDeclare().setName(x3dpsail.SFString("Bubble"))
          .setProtoBody(x3dpsail.ProtoBody()
            .addChild(x3dpsail.Transform().setDEF(x3dpsail.SFString("transform"))
              .addChild(x3dpsail.Shape()
                .setGeometry(x3dpsail.Sphere().setRadius(x3dpsail.SFFloat(0.25)))
                .setAppearance(x3dpsail.Appearance()
                  .setMaterial(x3dpsail.Material().setDiffuseColor(x3dpsail.SFColor(1,0,0)).setTransparency(x3dpsail.SFFloat(0.2)))))
              .addChild(x3dpsail.Script().setDEF(x3dpsail.SFString("bounce"))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("scale")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFVec3f")).setValue(x3dpsail.SFString("1 1 1")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("translation")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFVec3f")).setValue(x3dpsail.SFString("0 0 0")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("velocity")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFVec3f")).setValue(x3dpsail.SFString("0 0 0")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("scalvel")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFVec3f")).setValue(x3dpsail.SFString("0 0 0")))
                .addField(x3dpsail.field().setName(x3dpsail.SFString("set_fraction")).setAccessType(x3dpsail.SFString("inputOnly")).setType(x3dpsail.SFString("SFFloat"))).setSourceCode('''ecmascript:\n"+
"function initialize() {\n"+
"    velocity = new SFVec3f(Math.random() * 0.25 - 0.125, Math.random() * 0.25 - 0.125, Math.random() * 0.25 - 0.125);\n"+
"\n"+
"    scalvel = new SFVec3f(Math.random() * 0.4, Math.random() * 0.4, Math.random() * 0.4);\n"+
"}\n"+
"\n"+
"function set_fraction(value) {\n"+
"    if (typeof translation === 'undefined') {\n"+
"		translation = new SFVec3f(0, 0, 0);\n"+
"    }\n"+
"    if (typeof velocity === 'undefined') {\n"+
"		velocity = new SFVec3f(0, 0, 0);\n"+
"    }\n"+
"    if (typeof scalevel === 'undefined') {\n"+
"		scalevel = new SFVec3f(0, 0, 0);\n"+
"    }\n"+
"    if (typeof scale === 'undefined') {\n"+
"		scale = new SFVec3f(1, 1, 1);\n"+
"    }\n"+
"    translation = new SFVec3f(	translation.x + velocity.x, translation.y + velocity.y, translation.z + velocity.z);\n"+
"    scale = new SFVec3f(scale.x + scalvel.x, scale.y + scalvel.y, scale.z + scalvel.z);\n"+
"    // if you get to far away or too big, explode\n"+
"    if ( Math.abs(translation.x) > 256) {\n"+
"	translation.x = 0;\n"+
"	initialize();\n"+
"    }\n"+
"    if ( Math.abs(translation.y) > 256) {\n"+
"	translation.y = 0;\n"+
"	initialize();\n"+
"    }\n"+
"    if ( Math.abs(translation.z) > 256) {\n"+
"	translation.z = 0;\n"+
"	initialize();\n"+
"    }\n"+
"    if (Math.abs(scale.x) > 20) {\n"+
"	scale.x = scale.x/20;\n"+
"	translation.x = 0;\n"+
"	initialize();\n"+
"    }\n"+
"    if (Math.abs(scale.y) > 20) {\n"+
"	scale.y = scale.y/20;\n"+
"	translation.y = 0;\n"+
"	initialize();\n"+
"    }\n"+
"    if (Math.abs(scale.z) > 20) {\n"+
"	scale.z = scale.z/20;\n"+
"	translation.z = 0;\n"+
"	initialize();\n"+
"    }\n"+
"}''')
)
              .addChild(x3dpsail.TimeSensor().setDEF(x3dpsail.SFString("bubbleClock")).setCycleInterval(x3dpsail.SFTime(10)).setLoop(x3dpsail.SFBool(True)))
              .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("bounce")).setFromField(x3dpsail.SFString("translation_changed")).setToNode(x3dpsail.SFString("transform")).setToField(x3dpsail.SFString("set_translation")))
              .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("bounce")).setFromField(x3dpsail.SFString("scale_changed")).setToNode(x3dpsail.SFString("transform")).setToField(x3dpsail.SFString("set_scale")))
              .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("bubbleClock")).setFromField(x3dpsail.SFString("fraction_changed")).setToNode(x3dpsail.SFString("bounce")).setToField(x3dpsail.SFString("set_fraction"))))))
        .addChild(x3dpsail.ProtoInstance().setName(x3dpsail.SFString("Bubble")).setDEF(x3dpsail.SFString("bubbleA")))
        .addChild(x3dpsail.ProtoInstance().setName(x3dpsail.SFString("Bubble")).setDEF(x3dpsail.SFString("bubbleB")))
        .addChild(x3dpsail.ProtoInstance().setName(x3dpsail.SFString("Bubble")).setDEF(x3dpsail.SFString("bubbleC")))
        .addChild(x3dpsail.ProtoInstance().setName(x3dpsail.SFString("Bubble")).setDEF(x3dpsail.SFString("bubbleD")))))

X3D0.toFileX3D("./future/./cobweb2_RoundTrip.x3d")
