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
        .addChild(x3dpsail.Group()
          .addChild(x3dpsail.Shape()
            .setGeometry(x3dpsail.Extrusion().setDEF(x3dpsail.SFString("extrusion")).setSpine(x3dpsail.MFVec3f([-50,-50,0,50,50,0])).setCreaseAngle(x3dpsail.SFFloat(0.785)).setCrossSection(x3dpsail.MFVec2f([1,0,0.92,-0.38,0.71,-0.71,0.38,-0.92,0,-1,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1,0,-0.92,0.38,-0.71,0.71,-0.38,0.92,0,1,0.38,0.92,0.71,0.71,0.92,0.38,1,0])))
            .setAppearance(x3dpsail.Appearance()
              .setMaterial(x3dpsail.Material().setDiffuseColor(x3dpsail.SFColor(0,1,0)))))
          .addChild(x3dpsail.TimeSensor().setDEF(x3dpsail.SFString("TourTime")).setLoop(x3dpsail.SFBool(True)))
          .addChild(x3dpsail.Script().setDEF(x3dpsail.SFString("MoveCylinder"))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("set_cycle")).setAccessType(x3dpsail.SFString("inputOnly")).setType(x3dpsail.SFString("SFTime")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("spine")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("MFVec3f")).setValue(x3dpsail.SFString("-50 -50 0 50 50 0"))).setSourceCode('''ecmascript:\n"+
"\n"+
"                function set_cycle(value) {\n"+
"                        Browser.print(value);\n"+
"                        var endA = new SFVec3f(spine[0].x*Math.random()*2, spine[0].y*Math.random()*2, spine[0].z*Math.random()*2);\n"+
"                        var endB = new SFVec3f(spine[1].x*Math.random()*2, spine[1].y*Math.random()*2, spine[1].z*Math.random()*2);\n"+
"		        spine = new MFVec3f([endA, endB]);\n"+
"                }''')
)
          .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("TourTime")).setFromField(x3dpsail.SFString("cycleTime")).setToNode(x3dpsail.SFString("MoveCylinder")).setToField(x3dpsail.SFString("set_cycle")))
          .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("MoveCylinder")).setFromField(x3dpsail.SFString("spine_changed")).setToNode(x3dpsail.SFString("extrusion")).setToField(x3dpsail.SFString("spine"))))))

X3D0.toFileX3D("./future/./extrusion_RoundTrip.x3d")
