import x3dpsail


X3D0 = (x3dpsail.X3D().setProfile(x3dpsail.SFString("Interchange")).setVersion(x3dpsail.SFString("3.3"))
      .setHead(x3dpsail.head()
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("title")).setContent(x3dpsail.SFString("Table5_18PixelTexture")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("description")).setContent(x3dpsail.SFString("PixelTexture example for Table 5.18")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("creator")).setContent(x3dpsail.SFString("Leonard Daly and Don Brutzman")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("created")).setContent(x3dpsail.SFString("18 December 2006")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("modified")).setContent(x3dpsail.SFString("2 April 2017")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("reference")).setContent(x3dpsail.SFString("http://X3dGraphics.com")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("reference")).setContent(x3dpsail.SFString("http://www.web3d.org/x3d/content/examples/X3dResources.html")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("rights")).setContent(x3dpsail.SFString("Copyright 2006, Daly Realism and Don Brutzman")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("subject")).setContent(x3dpsail.SFString("X3D, PixelTexture")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("identifier")).setContent(x3dpsail.SFString("http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter05AppearanceMaterialTextures/Table5_18PixelTexture")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("generator")).setContent(x3dpsail.SFString("X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("license")).setContent(x3dpsail.SFString("../license.html"))))
      .setScene(x3dpsail.Scene()
        .addChild(x3dpsail.Background().setSkyColor(x3dpsail.MFColor([0,0,1])))
        .addChild(x3dpsail.Transform().setDEF(x3dpsail.SFString("Checkerboard")).setTranslation(x3dpsail.SFVec3f(0,0,-10))
          .addChild(x3dpsail.Shape()
            .setAppearance(x3dpsail.Appearance()
              .setTextureTransform(x3dpsail.TextureTransform().setScale(x3dpsail.SFVec2f(500,500)))
              .setTexture(x3dpsail.PixelTexture().setImage(x3dpsail.SFImage(2,2,3,15119869,16767927,16767927,15119869))))
            .setGeometry(x3dpsail.Box().setSize(x3dpsail.SFVec3f(1000,1000,0.01)))))
        .addChild(x3dpsail.Viewpoint().setDescription(x3dpsail.SFString("View All")).setPosition(x3dpsail.SFVec3f(0,0,20)))
        .addChild(x3dpsail.Viewpoint().setDescription(x3dpsail.SFString("Empty Image")).setPosition(x3dpsail.SFVec3f(0,5,5)))
        .addChild(x3dpsail.Transform().setDEF(x3dpsail.SFString("EmptyImage")).setRotation(x3dpsail.SFRotation(1,1,0,1)).setTranslation(x3dpsail.SFVec3f(0,5,0))
          .addChild(x3dpsail.Shape()
            .setAppearance(x3dpsail.Appearance()
              .setTexture(x3dpsail.PixelTexture()))
            .setGeometry(x3dpsail.Box().setDEF(x3dpsail.SFString("StandardBox")))))
        .addChild(x3dpsail.Viewpoint().setDescription(x3dpsail.SFString("Black and white PixelTexture")).setPosition(x3dpsail.SFVec3f(-5,0,5)))
        .addChild(x3dpsail.Transform().setDEF(x3dpsail.SFString("BW")).setRotation(x3dpsail.SFRotation(1,1,0,1)).setTranslation(x3dpsail.SFVec3f(-5,0,0))
          .addChild(x3dpsail.Shape()
            .setAppearance(x3dpsail.Appearance()
              .setTexture(x3dpsail.PixelTexture().setImage(x3dpsail.SFImage(1,2,1,255,0))))
            .setGeometry(x3dpsail.Box().setUSE(x3dpsail.SFString("StandardBox")))))
        .addChild(x3dpsail.Viewpoint().setDescription(x3dpsail.SFString("Black and white with Alpha PixelTexture")).setPosition(x3dpsail.SFVec3f(5,0,5)))
        .addChild(x3dpsail.Transform().setDEF(x3dpsail.SFString("AlphaBW")).setRotation(x3dpsail.SFRotation(1,1,0,1)).setTranslation(x3dpsail.SFVec3f(5,0,0))
          .addChild(x3dpsail.Shape()
            .setAppearance(x3dpsail.Appearance()
              .setTexture(x3dpsail.PixelTexture().setImage(x3dpsail.SFImage(2,1,2,52479,8823))))
            .setGeometry(x3dpsail.Box().setUSE(x3dpsail.SFString("StandardBox")))))
        .addChild(x3dpsail.Viewpoint().setDescription(x3dpsail.SFString("RGB PixelTexture")).setPosition(x3dpsail.SFVec3f(-5,-5,5)))
        .addChild(x3dpsail.Transform().setDEF(x3dpsail.SFString("RGB")).setRotation(x3dpsail.SFRotation(1,1,0,1)).setTranslation(x3dpsail.SFVec3f(-5,-5,0))
          .addChild(x3dpsail.Shape()
            .setAppearance(x3dpsail.Appearance()
              .setTexture(x3dpsail.PixelTexture().setImage(x3dpsail.SFImage(2,4,3,16711680,65280,0,0,0,0,16777215,16776960))))
            .setGeometry(x3dpsail.Box().setUSE(x3dpsail.SFString("StandardBox")))))
        .addChild(x3dpsail.Viewpoint().setDescription(x3dpsail.SFString("RGB with Alpha PixelTexture")).setPosition(x3dpsail.SFVec3f(5,-5,5)))
        .addChild(x3dpsail.Transform().setDEF(x3dpsail.SFString("AlphaRGB")).setRotation(x3dpsail.SFRotation(1,1,0,1)).setTranslation(x3dpsail.SFVec3f(5,-5,0))
          .addChild(x3dpsail.Shape()
            .setAppearance(x3dpsail.Appearance()
              .setTexture(x3dpsail.PixelTexture().setImage(x3dpsail.SFImage(3,2,4,-16776961,16711935,65535,-16777089,16711807,65407))))
            .setGeometry(x3dpsail.Box().setUSE(x3dpsail.SFString("StandardBox")))))))

X3D0.toFileX3D("./future/./Table5_18PixelTexture_RoundTrip.x3d")
