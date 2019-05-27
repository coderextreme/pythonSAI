import x3dpsail


X3D0 = (x3dpsail.X3D().setProfile(x3dpsail.SFString("Immersive")).setVersion(x3dpsail.SFString("3.3"))
      .setHead(x3dpsail.head()
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("title")).setContent(x3dpsail.SFString("SFVec3f.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("creator")).setContent(x3dpsail.SFString("John Carlson")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("description")).setContent(x3dpsail.SFString("3 prismatic spheres")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("identifier")).setContent(x3dpsail.SFString("https://coderextreme.net/X3DJSONLD/SFVec3f.x3d"))))
      .setScene(x3dpsail.Scene()
        .addChild(x3dpsail.NavigationInfo())
        .addChild(x3dpsail.Transform().setDEF(x3dpsail.SFString("transform"))
          .addChild(x3dpsail.Shape()
            .setAppearance(x3dpsail.Appearance()
              .setMaterial(x3dpsail.Material().setDiffuseColor(x3dpsail.SFColor(0.7,0.7,0.7)).setSpecularColor(x3dpsail.SFColor(0.5,0.5,0.5))))
            .setGeometry(x3dpsail.Sphere())))
        .addChild(x3dpsail.Script().setDEF(x3dpsail.SFString("Bounce"))
          .addField(x3dpsail.field().setName(x3dpsail.SFString("set_translation")).setAccessType(x3dpsail.SFString("inputOnly")).setType(x3dpsail.SFString("SFVec3f")).setValue(x3dpsail.SFString("0 0 0")))
          .addField(x3dpsail.field().setName(x3dpsail.SFString("translation_changed")).setAccessType(x3dpsail.SFString("outputOnly")).setType(x3dpsail.SFString("SFVec3f")).setValue(x3dpsail.SFString("0 0 0")))
          .addField(x3dpsail.field().setName(x3dpsail.SFString("translation")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFVec3f")).setValue(x3dpsail.SFString("0 0 0")))
          .addField(x3dpsail.field().setName(x3dpsail.SFString("velocity")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFVec3f")).setValue(x3dpsail.SFString("0 0 0")))
          .addField(x3dpsail.field().setName(x3dpsail.SFString("set_fraction")).setAccessType(x3dpsail.SFString("inputOnly")).setType(x3dpsail.SFString("SFTime"))).setSourceCode('''ecmascript:\n"+
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
"				if (Math.abs(translation.x) > 10) {\n"+
"					newBubble();\n"+
"				} else if (Math.abs(translation.y) > 10) {\n"+
"					newBubble();\n"+
"				} else if (Math.abs(translation.z) > 10) {\n"+
"					newBubble();\n"+
"				} else {\n"+
"					velocity = new SFVec3f(\n"+
"						velocity.x + Math.random() * 0.2 - 0.1,\n"+
"						velocity.y + Math.random() * 0.2 - 0.1,\n"+
"						velocity.z + Math.random() * 0.2 - 0.1\n"+
"					);\n"+
"				}\n"+
"			}\n"+
"\n"+
"			function initialize() {\n"+
"			     newBubble();\n"+
"			}''')
)
        .addChild(x3dpsail.TimeSensor().setDEF(x3dpsail.SFString("TourTime")).setCycleInterval(x3dpsail.SFTime(0.15)).setLoop(x3dpsail.SFBool(True)))
        .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("TourTime")).setFromField(x3dpsail.SFString("cycleTime")).setToNode(x3dpsail.SFString("Bounce")).setToField(x3dpsail.SFString("set_fraction")))
        .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("Bounce")).setFromField(x3dpsail.SFString("translation_changed")).setToNode(x3dpsail.SFString("transform")).setToField(x3dpsail.SFString("set_translation")))))

X3D0.toFileX3D("./future/./SFVec3f_RoundTrip.x3d")
