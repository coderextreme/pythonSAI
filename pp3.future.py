import x3dpsail


X3D0 = (x3dpsail.X3D().setProfile(x3dpsail.SFString("Immersive")).setVersion(x3dpsail.SFString("3.3"))
      .setHead(x3dpsail.head()
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("title")).setContent(x3dpsail.SFString("pp3.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("creator")).setContent(x3dpsail.SFString("John Carlson")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("translator")).setContent(x3dpsail.SFString("John Carlson")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("created")).setContent(x3dpsail.SFString("5 May 2015")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("modified")).setContent(x3dpsail.SFString("05 May 2017")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("description")).setContent(x3dpsail.SFString("A process pipeline between three spheres (try typing on spheres and blue")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("identifier")).setContent(x3dpsail.SFString("https://coderextreme.net/x3d/pp3.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("generator")).setContent(x3dpsail.SFString("manual"))))
      .setScene(x3dpsail.Scene()
        .addChild(x3dpsail.ProtoDeclare().setName(x3dpsail.SFString("Process"))
          .setProtoBody(x3dpsail.ProtoBody()
            .addChild(x3dpsail.Group()
              #left

              .addChild(x3dpsail.Transform().setScale(x3dpsail.SFVec3f(0.5,0.5,0.5))
                .addChild(x3dpsail.Shape()
                  .setAppearance(x3dpsail.Appearance()
                    .setMaterial(x3dpsail.Material().setDiffuseColor(x3dpsail.SFColor(0.7,1,0)).setTransparency(x3dpsail.SFFloat(0.5))))
                  .setGeometry(x3dpsail.Extrusion().setCreaseAngle(x3dpsail.SFFloat(0.785)).setCrossSection(x3dpsail.MFVec2f([1,0,0.92,-0.38,0.71,-0.71,0.38,-0.92,0,-1,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1,0,-0.92,0.38,-0.71,0.71,-0.38,0.92,0,1,0.38,0.92,0.71,0.71,0.92,0.38,1,0])).setSpine(x3dpsail.MFVec3f([-2.5,0,0,-1.5,0,0]))))
                #<Transform translation=\"-2.5 0 0\"> <Shape> <Text DEF=\"LeftString\" string='\"l\"'/> </Shape> </Transform> <StringSensor DEF=\"LeftSensor\" enabled=\"false\"/> <TouchSensor DEF=\"LeftTouch\" enabled=\"true\"/>

                )
              #right

              .addChild(x3dpsail.Transform().setScale(x3dpsail.SFVec3f(0.5,0.5,0.5))
                .addChild(x3dpsail.Shape()
                  .setAppearance(x3dpsail.Appearance()
                    .setMaterial(x3dpsail.Material().setDiffuseColor(x3dpsail.SFColor(0,0.7,1)).setTransparency(x3dpsail.SFFloat(0.5))))
                  .setGeometry(x3dpsail.Extrusion().setCreaseAngle(x3dpsail.SFFloat(0.785)).setCrossSection(x3dpsail.MFVec2f([1,0,0.92,-0.38,0.71,-0.71,0.38,-0.92,0,-1,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1,0,-0.92,0.38,-0.71,0.71,-0.38,0.92,0,1,0.38,0.92,0.71,0.71,0.92,0.38,1,0])).setSpine(x3dpsail.MFVec3f([1.5,0,0,2.5,0,0]))))
                .addChild(x3dpsail.Transform().setTranslation(x3dpsail.SFVec3f(2,0,0))
                  .addChild(x3dpsail.Shape()
                    .setAppearance(x3dpsail.Appearance()
                      .setMaterial(x3dpsail.Material().setDEF(x3dpsail.SFString("MaterialLightBlue")).setDiffuseColor(x3dpsail.SFColor(1,1,1))))
                    .setGeometry(x3dpsail.Text().setDEF(x3dpsail.SFString("RightString")).setString(x3dpsail.MFString(["r"])))))
                .addChild(x3dpsail.StringSensor().setDEF(x3dpsail.SFString("RightSensor")).setEnabled(x3dpsail.SFBool(False)))
                .addChild(x3dpsail.TouchSensor().setDescription(x3dpsail.SFString("touch to activate")).setDEF(x3dpsail.SFString("RightTouch"))))
              #up

              .addChild(x3dpsail.Transform().setScale(x3dpsail.SFVec3f(0.5,0.5,0.5))
                .addChild(x3dpsail.Shape()
                  .setAppearance(x3dpsail.Appearance()
                    .setMaterial(x3dpsail.Material().setDiffuseColor(x3dpsail.SFColor(0,0.7,1)).setTransparency(x3dpsail.SFFloat(0.5))))
                  .setGeometry(x3dpsail.Extrusion().setCreaseAngle(x3dpsail.SFFloat(0.785)).setCrossSection(x3dpsail.MFVec2f([1,0,0.92,-0.38,0.71,-0.71,0.38,-0.92,0,-1,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1,0,-0.92,0.38,-0.71,0.71,-0.38,0.92,0,1,0.38,0.92,0.71,0.71,0.92,0.38,1,0])).setSpine(x3dpsail.MFVec3f([0,1.5,0,0,2.5,0]))))
                .addChild(x3dpsail.Transform().setTranslation(x3dpsail.SFVec3f(-0.5,2,0))
                  .addChild(x3dpsail.Shape()
                    .setAppearance(x3dpsail.Appearance()
                      .setMaterial(x3dpsail.Material().setUSE(x3dpsail.SFString("MaterialLightBlue"))))
                    .setGeometry(x3dpsail.Text().setDEF(x3dpsail.SFString("UpString")).setString(x3dpsail.MFString(["u"])))))
                .addChild(x3dpsail.StringSensor().setDEF(x3dpsail.SFString("UpSensor")).setEnabled(x3dpsail.SFBool(False)))
                .addChild(x3dpsail.TouchSensor().setDescription(x3dpsail.SFString("touch to activate")).setDEF(x3dpsail.SFString("UpTouch"))))
              #down

              .addChild(x3dpsail.Transform().setScale(x3dpsail.SFVec3f(0.5,0.5,0.5))
                .addChild(x3dpsail.Shape()
                  .setAppearance(x3dpsail.Appearance()
                    .setMaterial(x3dpsail.Material().setDiffuseColor(x3dpsail.SFColor(0.7,1,0)).setTransparency(x3dpsail.SFFloat(0.5))))
                  .setGeometry(x3dpsail.Extrusion().setCreaseAngle(x3dpsail.SFFloat(0.785)).setCrossSection(x3dpsail.MFVec2f([1,0,0.92,-0.38,0.71,-0.71,0.38,-0.92,0,-1,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1,0,-0.92,0.38,-0.71,0.71,-0.38,0.92,0,1,0.38,0.92,0.71,0.71,0.92,0.38,1,0])).setSpine(x3dpsail.MFVec3f([0,-2.5,0,0,-1.5,0]))))
                #<Transform translation=\"-0.5 -2.5 0\"> <Shape> <Text DEF=\"DownString\" string='\"d\"'/> </Shape> </Transform> <StringSensor DEF=\"DownSensor\" enabled=\"false\"/> <TouchSensor description='touch to activate' DEF=\"DownTouch\" enabled=\"true\"/>

                )
              #center

              .addChild(x3dpsail.Transform()
                .addChild(x3dpsail.Shape()
                  .setAppearance(x3dpsail.Appearance()
                    .setMaterial(x3dpsail.Material().setDiffuseColor(x3dpsail.SFColor(1,0,0.7))))
                  .setGeometry(x3dpsail.Sphere()))
                .addChild(x3dpsail.Transform().setScale(x3dpsail.SFVec3f(0.5,0.5,0.5)).setTranslation(x3dpsail.SFVec3f(-0.5,0,1))
                  .addChild(x3dpsail.Shape()
                    .setAppearance(x3dpsail.Appearance()
                      .setMaterial(x3dpsail.Material().setUSE(x3dpsail.SFString("MaterialLightBlue"))))
                    .setGeometry(x3dpsail.Text().setDEF(x3dpsail.SFString("CenterString")))))
                .addChild(x3dpsail.StringSensor().setDEF(x3dpsail.SFString("CenterSensor")).setEnabled(x3dpsail.SFBool(False)))
                .addChild(x3dpsail.TouchSensor().setDescription(x3dpsail.SFString("touch to activate")).setDEF(x3dpsail.SFString("CenterTouch")))))
            .addChild(x3dpsail.Script().setDEF(x3dpsail.SFString("RightSingleToMultiString"))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("set_rightstring")).setAccessType(x3dpsail.SFString("inputOnly")).setType(x3dpsail.SFString("SFString")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("rightlines")).setAccessType(x3dpsail.SFString("outputOnly")).setType(x3dpsail.SFString("MFString"))).setSourceCode('''ecmascript:\n"+
"\n"+
"function initialize() {\n"+
"	rightlines = new MFString(\"\");\n"+
"}\n"+
"\n"+
"function set_rightstring(rightstr) {\n"+
"	rightlines = new MFString(rightstr);\n"+
"}''')
)
            .addChild(x3dpsail.Script().setDEF(x3dpsail.SFString("UpSingleToMultiString"))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("set_upstring")).setAccessType(x3dpsail.SFString("inputOnly")).setType(x3dpsail.SFString("SFString")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("uplines")).setAccessType(x3dpsail.SFString("outputOnly")).setType(x3dpsail.SFString("MFString"))).setSourceCode('''ecmascript:\n"+
"\n"+
"function initialize() {\n"+
"	uplines = new MFString(\"\");\n"+
"}\n"+
"\n"+
"function set_upstring(upstr) {\n"+
"	uplines = new MFString(upstr);\n"+
"}''')
)
            .addChild(x3dpsail.Script().setDEF(x3dpsail.SFString("CenterSingleToMultiString"))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("set_centerstring")).setAccessType(x3dpsail.SFString("inputOnly")).setType(x3dpsail.SFString("SFString")))
              .addField(x3dpsail.field().setName(x3dpsail.SFString("centerlines")).setAccessType(x3dpsail.SFString("outputOnly")).setType(x3dpsail.SFString("MFString"))).setSourceCode('''ecmascript:\n"+
"\n"+
"function initialize() {\n"+
"	centerlines = new MFString(\"\");\n"+
"}\n"+
"\n"+
"function set_centerstring(centerstr) {\n"+
"	centerlines = new MFString(centerstr);\n"+
"}''')
)
            .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("enteredText")).setFromNode(x3dpsail.SFString("CenterSensor")).setToField(x3dpsail.SFString("set_centerstring")).setToNode(x3dpsail.SFString("CenterSingleToMultiString")))
            .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("centerlines")).setFromNode(x3dpsail.SFString("CenterSingleToMultiString")).setToField(x3dpsail.SFString("set_string")).setToNode(x3dpsail.SFString("CenterString")))
            .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("isOver")).setFromNode(x3dpsail.SFString("CenterTouch")).setToField(x3dpsail.SFString("set_enabled")).setToNode(x3dpsail.SFString("CenterSensor")))
            .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("enteredText")).setFromNode(x3dpsail.SFString("RightSensor")).setToField(x3dpsail.SFString("set_rightstring")).setToNode(x3dpsail.SFString("RightSingleToMultiString")))
            .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("rightlines")).setFromNode(x3dpsail.SFString("RightSingleToMultiString")).setToField(x3dpsail.SFString("set_string")).setToNode(x3dpsail.SFString("RightString")))
            .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("isOver")).setFromNode(x3dpsail.SFString("RightTouch")).setToField(x3dpsail.SFString("set_enabled")).setToNode(x3dpsail.SFString("RightSensor")))
            .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("enteredText")).setFromNode(x3dpsail.SFString("UpSensor")).setToField(x3dpsail.SFString("set_upstring")).setToNode(x3dpsail.SFString("UpSingleToMultiString")))
            .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("uplines")).setFromNode(x3dpsail.SFString("UpSingleToMultiString")).setToField(x3dpsail.SFString("set_string")).setToNode(x3dpsail.SFString("UpString")))
            .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("isOver")).setFromNode(x3dpsail.SFString("UpTouch")).setToField(x3dpsail.SFString("set_enabled")).setToNode(x3dpsail.SFString("UpSensor")))))
        .addChild(x3dpsail.NavigationInfo())
        .addChild(x3dpsail.Viewpoint().setDescription(x3dpsail.SFString("Process pipes")).setOrientation(x3dpsail.SFRotation(1,0,0,-0.4)).setPosition(x3dpsail.SFVec3f(0,5,12)))
        .addChild(x3dpsail.Transform().setTranslation(x3dpsail.SFVec3f(0,-2.5,0))
          .addChild(x3dpsail.ProtoInstance().setName(x3dpsail.SFString("Process"))))
        .addChild(x3dpsail.Transform()
          .addChild(x3dpsail.ProtoInstance().setName(x3dpsail.SFString("Process"))))
        .addChild(x3dpsail.Transform().setTranslation(x3dpsail.SFVec3f(0,2.5,0))
          .addChild(x3dpsail.ProtoInstance().setName(x3dpsail.SFString("Process"))))))

X3D0.toFileX3D("./future/./pp3_RoundTrip.x3d")
