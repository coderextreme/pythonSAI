import x3dpsail


X3D0 = (x3dpsail.X3D().setProfile(x3dpsail.SFString("Immersive")).setVersion(x3dpsail.SFString("3.3"))
      .setHead(x3dpsail.head()
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("title")).setContent(x3dpsail.SFString("sphereflowers.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("creator")).setContent(x3dpsail.SFString("John Carlson")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("description")).setContent(x3dpsail.SFString("5 or more prismatic flowers")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("generator")).setContent(x3dpsail.SFString("X3D-Edit, https://savage.nps.edu/X3D-Edit")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("identifier")).setContent(x3dpsail.SFString("https://coderextreme.net/X3DJSONLD/sphereflowers.x3d"))))
      .setScene(x3dpsail.Scene()
        .addChild(x3dpsail.NavigationInfo())
        .addChild(x3dpsail.Background().setBackUrl(x3dpsail.MFString(["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"])).setBottomUrl(x3dpsail.MFString(["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"])).setFrontUrl(x3dpsail.MFString(["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"])).setLeftUrl(x3dpsail.MFString(["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"])).setRightUrl(x3dpsail.MFString(["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"])).setTopUrl(x3dpsail.MFString(["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"])))
        .addChild(x3dpsail.Group()
          .addChild(x3dpsail.ExternProtoDeclare().setName(x3dpsail.SFString("FlowerProto")).setUrl(x3dpsail.MFString(["../data/flowerproto.x3d#FlowerProto"]))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("vertex")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("MFString")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("fragment")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("MFString"))))
          .addChild(x3dpsail.ProtoDeclare().setName(x3dpsail.SFString("flower"))
            .setProtoBody(x3dpsail.ProtoBody()
              .addChild(x3dpsail.Group()
                .addChild(x3dpsail.ProtoInstance().setName(x3dpsail.SFString("FlowerProto"))
                  .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("vertex")).setValue(x3dpsail.SFString("\"../shaders/freewrl_flowers_chromatic.vs\"")))
                  .addFieldValue(x3dpsail.fieldValue().setName(x3dpsail.SFString("fragment")).setValue(x3dpsail.SFString("\"../shaders/freewrl.fs\"")))))))
          .addChild(x3dpsail.ProtoInstance().setName(x3dpsail.SFString("flower")))
          .addChild(x3dpsail.ProtoInstance().setName(x3dpsail.SFString("flower")))
          .addChild(x3dpsail.ProtoInstance().setName(x3dpsail.SFString("flower")))
          .addChild(x3dpsail.ProtoInstance().setName(x3dpsail.SFString("flower")))
          .addChild(x3dpsail.ProtoInstance().setName(x3dpsail.SFString("flower")))
          .addChild(x3dpsail.ProtoInstance().setName(x3dpsail.SFString("flower"))))))

X3D0.toFileX3D("./future/./freewrlflowers_RoundTrip.x3d")
