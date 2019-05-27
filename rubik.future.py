import x3dpsail


X3D0 = (x3dpsail.X3D().setProfile(x3dpsail.SFString("Immersive")).setVersion(x3dpsail.SFString("3.3"))
      .setHead(x3dpsail.head()
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("title")).setContent(x3dpsail.SFString("rubik.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("creator")).setContent(x3dpsail.SFString("John Carlson")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("generator")).setContent(x3dpsail.SFString("manual")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("identifier")).setContent(x3dpsail.SFString("https://coderextreme.net/X3DJSONLD/rubik.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("description")).setContent(x3dpsail.SFString("a kind of rubik cube with spheres"))))
      .setScene(x3dpsail.Scene()
        .addChild(x3dpsail.NavigationInfo().setType(x3dpsail.MFString(["EXAMINE"])))
        .addChild(x3dpsail.Viewpoint().setDescription(x3dpsail.SFString("Rubiks Cube")).setPosition(x3dpsail.SFVec3f(0,0,12)))
        .addChild(x3dpsail.ProtoDeclare().setName(x3dpsail.SFString("sphere"))
          .setProtoInterface(x3dpsail.ProtoInterface()
            .addField(x3dpsail.field().setName(x3dpsail.SFString("xtranslation")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFVec3f")).setValue(x3dpsail.SFString("0 0 0"))))
          .setProtoBody(x3dpsail.ProtoBody()
            .addChild(x3dpsail.Transform()
              .setIS(x3dpsail.IS()
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("translation")).setProtoField(x3dpsail.SFString("xtranslation"))))
              .addChild(x3dpsail.Shape()
                .setGeometry(x3dpsail.Sphere())
                .setAppearance(x3dpsail.Appearance()
                  .setMaterial(x3dpsail.Material().setDiffuseColor(x3dpsail.SFColor(1,1,1))))))))
        .addChild(x3dpsail.ProtoDeclare().setName(x3dpsail.SFString("three"))
          .setProtoInterface(x3dpsail.ProtoInterface()
            .addField(x3dpsail.field().setName(x3dpsail.SFString("ytranslation")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFVec3f")).setValue(x3dpsail.SFString("0 0 0"))))
          .setProtoBody(x3dpsail.ProtoBody()
            .addChild(x3dpsail.Transform()
              .setIS(x3dpsail.IS()
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("translation")).setProtoField(x3dpsail.SFString("ytranslation"))))
              .addChild(x3dpsail.ProtoInstance().setName(x3dpsail.SFString("sphere"))
                .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("xtranslation")).setValue(x3dpsail.SFString("0 0 0"))))
              .addChild(x3dpsail.ProtoInstance().setName(x3dpsail.SFString("sphere"))
                .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("xtranslation")).setValue(x3dpsail.SFString("2 0 0"))))
              .addChild(x3dpsail.ProtoInstance().setName(x3dpsail.SFString("sphere"))
                .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("xtranslation")).setValue(x3dpsail.SFString("-2 0 0")))))))
        .addChild(x3dpsail.ProtoDeclare().setName(x3dpsail.SFString("nine"))
          .setProtoInterface(x3dpsail.ProtoInterface()
            .addField(x3dpsail.field().setName(x3dpsail.SFString("ztranslation")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFVec3f")).setValue(x3dpsail.SFString("0 0 0"))))
          .setProtoBody(x3dpsail.ProtoBody()
            .addChild(x3dpsail.Transform()
              .setIS(x3dpsail.IS()
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("translation")).setProtoField(x3dpsail.SFString("ztranslation"))))
              .addChild(x3dpsail.ProtoInstance().setName(x3dpsail.SFString("three"))
                .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("ytranslation")).setValue(x3dpsail.SFString("0 0 0"))))
              .addChild(x3dpsail.ProtoInstance().setName(x3dpsail.SFString("three"))
                .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("ytranslation")).setValue(x3dpsail.SFString("0 2 0"))))
              .addChild(x3dpsail.ProtoInstance().setName(x3dpsail.SFString("three"))
                .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("ytranslation")).setValue(x3dpsail.SFString("0 -2 0")))))))
        .addChild(x3dpsail.ProtoDeclare().setName(x3dpsail.SFString("twentyseven"))
          .setProtoInterface(x3dpsail.ProtoInterface()
            .addField(x3dpsail.field().setName(x3dpsail.SFString("ttranslation")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFVec3f")).setValue(x3dpsail.SFString("0 0 0"))))
          .setProtoBody(x3dpsail.ProtoBody()
            .addChild(x3dpsail.Transform()
              .setIS(x3dpsail.IS()
                .addConnect(x3dpsail.connect().setNodeField(x3dpsail.SFString("translation")).setProtoField(x3dpsail.SFString("ttranslation"))))
              .addChild(x3dpsail.ProtoInstance().setName(x3dpsail.SFString("nine"))
                .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("ztranslation")).setValue(x3dpsail.SFString("0 0 0"))))
              .addChild(x3dpsail.ProtoInstance().setName(x3dpsail.SFString("nine"))
                .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("ztranslation")).setValue(x3dpsail.SFString("0 0 2"))))
              .addChild(x3dpsail.ProtoInstance().setName(x3dpsail.SFString("nine"))
                .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("ztranslation")).setValue(x3dpsail.SFString("0 0 -2")))))))
        .addChild(x3dpsail.ProtoInstance().setName(x3dpsail.SFString("twentyseven"))
          .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("ttranslation")).setValue(x3dpsail.SFString("0 0 0"))))))

X3D0.toFileX3D("./future/./rubik_RoundTrip.x3d")
