import x3dpsail


X3D0 = (x3dpsail.X3D().setProfile(x3dpsail.SFString("Immersive")).setVersion(x3dpsail.SFString("3.3"))
      .setHead(x3dpsail.head()
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("title")).setContent(x3dpsail.SFString("bubble.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("creator")).setContent(x3dpsail.SFString("John Carlson")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("description")).setContent(x3dpsail.SFString("Tour around a prismatic sphere")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("generator")).setContent(x3dpsail.SFString("X3D-Edit, https://savage.nps.edu/X3D-Edit")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("identifier")).setContent(x3dpsail.SFString("https://coderextreme.net/X3DJSONLD/bubble.x3d"))))
      .setScene(x3dpsail.Scene()
        .addChild(x3dpsail.NavigationInfo().setType(x3dpsail.MFString(["EXAMINE"])))
        .addChild(x3dpsail.Viewpoint().setPosition(x3dpsail.SFVec3f(0,0,4)).setOrientation(x3dpsail.SFRotation(1,0,0,0)).setDescription(x3dpsail.SFString("Bubble in action")))
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
"	translation = new SFVec3f(\n"+
"		translation.x + velocity.x,\n"+
"		translation.y + velocity.y,\n"+
"		translation.z + velocity.z);\n"+
"	scale = new SFVec3f(\n"+
"		scale.x + scalvel.x,\n"+
"		scale.y + scalvel.y,\n"+
"		scale.z + scalvel.z);\n"+
"        // if you get to far away or too big, explode\n"+
"        if ( Math.abs(translation.x) > 256) {\n"+
"		translation.x = 0;\n"+
"		initialize();\n"+
"	}\n"+
"        if ( Math.abs(translation.y) > 256) {\n"+
"		translation.y = 0;\n"+
"		initialize();\n"+
"	}\n"+
"        if ( Math.abs(translation.z) > 256) {\n"+
"		translation.z = 0;\n"+
"		initialize();\n"+
"	}\n"+
"	if (Math.abs(scale.x) > 20) {\n"+
"		scale.x = scale.x/2;\n"+
"		translation.x = 0;\n"+
"		initialize();\n"+
"	}\n"+
"	if (Math.abs(scale.y) > 20) {\n"+
"		scale.y = scale.y/2;\n"+
"		translation.y = 0;\n"+
"		initialize();\n"+
"	}\n"+
"	if (Math.abs(scale.z) > 20) {\n"+
"		scale.z = scale.z/2;\n"+
"		translation.z = 0;\n"+
"		initialize();\n"+
"	}\n"+
"}''')
)
              .addChild(x3dpsail.TimeSensor().setDEF(x3dpsail.SFString("bubbleClock")).setCycleInterval(x3dpsail.SFTime(10)).setLoop(x3dpsail.SFBool(True)))
              .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("bounce")).setFromField(x3dpsail.SFString("translation_changed")).setToNode(x3dpsail.SFString("transform")).setToField(x3dpsail.SFString("set_translation")))
              .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("bounce")).setFromField(x3dpsail.SFString("scale_changed")).setToNode(x3dpsail.SFString("transform")).setToField(x3dpsail.SFString("set_scale")))
              .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("bubbleClock")).setFromField(x3dpsail.SFString("fraction_changed")).setToNode(x3dpsail.SFString("bounce")).setToField(x3dpsail.SFString("set_fraction"))))))
        .addChild(x3dpsail.ProtoInstance().setName(x3dpsail.SFString("Bubble")).setDEF(x3dpsail.SFString("bubbleA")))))

X3D0.toFileX3D("./future/./bubble_RoundTrip.x3d")
