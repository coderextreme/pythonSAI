import x3dpsail


X3D0 = (x3dpsail.X3D().setProfile(x3dpsail.SFString("Immersive")).setVersion(x3dpsail.SFString("3.3"))
      .setHead(x3dpsail.head()
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("title")).setContent(x3dpsail.SFString("qq3.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("creator")).setContent(x3dpsail.SFString("John Carlson")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("translator")).setContent(x3dpsail.SFString("John Carlson")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("created")).setContent(x3dpsail.SFString("11 Jan 2015")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("modified")).setContent(x3dpsail.SFString("05 May 2017")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("description")).setContent(x3dpsail.SFString("12 extrusions to test prototype expander")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("identifier")).setContent(x3dpsail.SFString("https://coderextreme.net/x3d/qq3.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("generator")).setContent(x3dpsail.SFString("manual"))))
      .setScene(x3dpsail.Scene()
        .addChild(x3dpsail.ProtoDeclare().setName(x3dpsail.SFString("Process"))
          .setProtoBody(x3dpsail.ProtoBody()
            .addChild(x3dpsail.Group()
              #left

              .addChild(x3dpsail.Transform().setScale(x3dpsail.SFVec3f(0.5,0.5,0.5))
                .addChild(x3dpsail.Shape().setDEF(x3dpsail.SFString("ShapeLeftDown"))
                  .setAppearance(x3dpsail.Appearance()
                    .setMaterial(x3dpsail.Material().setDiffuseColor(x3dpsail.SFColor(0.7,1,0))))
                  .setGeometry(x3dpsail.Extrusion().setSpine(x3dpsail.MFVec3f([-2.5,0,0,-1.5,0,0])).setCreaseAngle(x3dpsail.SFFloat(0.785)).setCrossSection(x3dpsail.MFVec2f([1,0,0.92,-0.38,0.71,-0.71,0.38,-0.92,0,-1,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1,0,-0.92,0.38,-0.71,0.71,-0.38,0.92,0,1,0.38,0.92,0.71,0.71,0.92,0.38,1,0])))))
              #right

              .addChild(x3dpsail.Transform().setScale(x3dpsail.SFVec3f(0.5,0.5,0.5))
                .addChild(x3dpsail.Shape().setDEF(x3dpsail.SFString("ShapeUpRight"))
                  .setAppearance(x3dpsail.Appearance()
                    .setMaterial(x3dpsail.Material().setDiffuseColor(x3dpsail.SFColor(0,0.7,1))))
                  .setGeometry(x3dpsail.Extrusion().setSpine(x3dpsail.MFVec3f([1.5,0,0,2.5,0,0])).setCreaseAngle(x3dpsail.SFFloat(0.785)).setCrossSection(x3dpsail.MFVec2f([1,0,0.92,-0.38,0.71,-0.71,0.38,-0.92,0,-1,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1,0,-0.92,0.38,-0.71,0.71,-0.38,0.92,0,1,0.38,0.92,0.71,0.71,0.92,0.38,1,0])))))
              #up

              .addChild(x3dpsail.Transform().setScale(x3dpsail.SFVec3f(0.5,0.5,0.5))
                .addChild(x3dpsail.Shape().setUSE(x3dpsail.SFString("ShapeUpRight"))))
              #down

              .addChild(x3dpsail.Transform().setScale(x3dpsail.SFVec3f(0.5,0.5,0.5))
                .addChild(x3dpsail.Shape().setUSE(x3dpsail.SFString("ShapeLeftDown")))))))
        .addChild(x3dpsail.Viewpoint().setDescription(x3dpsail.SFString("Process pipes")).setOrientation(x3dpsail.SFRotation(1,0,0,-0.4)).setPosition(x3dpsail.SFVec3f(0,5,12)))
        .addChild(x3dpsail.Transform().setTranslation(x3dpsail.SFVec3f(0,-2.5,0))
          .addChild(x3dpsail.ProtoInstance().setName(x3dpsail.SFString("Process"))))
        .addChild(x3dpsail.Transform()
          .addChild(x3dpsail.ProtoInstance().setName(x3dpsail.SFString("Process"))))
        .addChild(x3dpsail.Transform().setTranslation(x3dpsail.SFVec3f(0,2.5,0))
          .addChild(x3dpsail.ProtoInstance().setName(x3dpsail.SFString("Process"))))))

X3D0.toFileX3D("./future/./qq3_RoundTrip.x3d")
