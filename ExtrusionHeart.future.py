import x3dpsail


X3D0 = (x3dpsail.X3D().setProfile(x3dpsail.SFString("Immersive")).setVersion(x3dpsail.SFString("3.0"))
      .setHead(x3dpsail.head()
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("title")).setContent(x3dpsail.SFString("ExtrusionHeart.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("description")).setContent(x3dpsail.SFString("Simple extrusion of a Valentine heart.")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("creator")).setContent(x3dpsail.SFString("Class participants in course Introduction to VRML/X3D.")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("created")).setContent(x3dpsail.SFString("14 February 2001")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("modified")).setContent(x3dpsail.SFString("27 November 2015")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("identifier")).setContent(x3dpsail.SFString("http://www.web3d.org/x3d/content/examples/Basic/course/ExtrusionHeart.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("generator")).setContent(x3dpsail.SFString("X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("license")).setContent(x3dpsail.SFString("../license.html"))))
      .setScene(x3dpsail.Scene()
        .addChild(x3dpsail.Viewpoint().setDescription(x3dpsail.SFString("Extrusion Heart")).setOrientation(x3dpsail.SFRotation(1,0,0,1.57)).setPosition(x3dpsail.SFVec3f(0,-4,0)))
        .addChild(x3dpsail.Transform().setTranslation(x3dpsail.SFVec3f(0,-0.5,0))
          .addChild(x3dpsail.Shape()
            .setGeometry(x3dpsail.Extrusion().setCreaseAngle(x3dpsail.SFFloat(3.14159)).setCrossSection(x3dpsail.MFVec2f([0,0.8,0.2,1,0.7,0.95,1,0.5,0.8,0,0.5,-0.3,0,-0.7,-0.5,-0.3,-0.8,0,-1,0.5,-0.7,0.95,-0.2,1,0,0.8])).setScale(x3dpsail.MFVec2f([0.01,0.01,0.8,0.8,1,1,0.8,0.8,0.01,0.01])).setSolid(x3dpsail.SFBool(False)).setSpine(x3dpsail.MFVec3f([0,0,0,0,0.1,0,0,0.5,0,0,0.9,0,0,1,0])))
            .setAppearance(x3dpsail.Appearance()
              .setMaterial(x3dpsail.Material().setDiffuseColor(x3dpsail.SFColor(0.8,0.3,0.3))))))))

X3D0.toFileX3D("./future/./ExtrusionHeart_RoundTrip.x3d")
