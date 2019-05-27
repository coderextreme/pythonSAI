import x3dpsail


X3D0 = (x3dpsail.X3D().setProfile(x3dpsail.SFString("Immersive")).setVersion(x3dpsail.SFString("3.3"))
      .setHead(x3dpsail.head()
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("title")).setContent(x3dpsail.SFString("CoordinateAxis.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("creator")).setContent(x3dpsail.SFString("Unknown, see X3D Resources Archives")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("generator")).setContent(x3dpsail.SFString("manual")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("identifier")).setContent(x3dpsail.SFString("https://coderextreme.net/X3DJSONLD/CoordinateAxis.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("description")).setContent(x3dpsail.SFString("a box"))))
      .setScene(x3dpsail.Scene()
        .addChild(x3dpsail.Collision().setDEF(x3dpsail.SFString("DoNotCollideWithVisualizationWidget"))
          #Invoke CoordinateAxes in other scenes as an Inline child inside a scaling Transform node, at the topmost level of the scene graph.

          #This NavigationInfo allows examine mode and will be overridden by any parent scene.

          #Each arrow goes from +1m to -1m to allow linear scaling to fit a scene

          #Note each label rotates about the scene's vertical Y axis for consistency, enabling local orientation by user

          .setProxy(x3dpsail.Group()
            #Vertical Y arrow and label

            .addChild(x3dpsail.Group().setDEF(x3dpsail.SFString("ArrowGreen"))
              .addChild(x3dpsail.Shape()
                .setGeometry(x3dpsail.Cylinder().setDEF(x3dpsail.SFString("ArrowCylinder")).setRadius(x3dpsail.SFFloat(0.025)).setTop(x3dpsail.SFBool(False)))
                .setAppearance(x3dpsail.Appearance().setDEF(x3dpsail.SFString("Green"))
                  .setMaterial(x3dpsail.Material().setDiffuseColor(x3dpsail.SFColor(0.1,0.6,0.1)).setEmissiveColor(x3dpsail.SFColor(0.05,0.2,0.05)))))
              .addChild(x3dpsail.Transform().setTranslation(x3dpsail.SFVec3f(0,1,0))
                .addChild(x3dpsail.Shape()
                  .setGeometry(x3dpsail.Cone().setDEF(x3dpsail.SFString("ArrowCone")).setBottomRadius(x3dpsail.SFFloat(0.05)).setHeight(x3dpsail.SFFloat(0.1)))
                  .setAppearance(x3dpsail.Appearance().setUSE(x3dpsail.SFString("Green"))))))
            .addChild(x3dpsail.Transform().setTranslation(x3dpsail.SFVec3f(0,1.08,0))
              .addChild(x3dpsail.Billboard()
                .addChild(x3dpsail.Shape()
                  .setAppearance(x3dpsail.Appearance().setDEF(x3dpsail.SFString("LABEL_APPEARANCE"))
                    .setMaterial(x3dpsail.Material().setDiffuseColor(x3dpsail.SFColor(1,1,0.3)).setEmissiveColor(x3dpsail.SFColor(0.33,0.33,0.1))))
                  .setGeometry(x3dpsail.Text().setString(x3dpsail.MFString(["Y"]))
                    .setFontStyle(x3dpsail.FontStyle().setDEF(x3dpsail.SFString("LABEL_FONT")).setFamily(x3dpsail.MFString(["SANS"])).setJustify(x3dpsail.MFString(["MIDDLE","MIDDLE"])).setSize(x3dpsail.SFFloat(0.2))))))))
          .setProxy(x3dpsail.Transform().setRotation(x3dpsail.SFRotation(0,0,1,-1.57079))
            #Horizontal X arrow and label

            .addChild(x3dpsail.Group()
              .addChild(x3dpsail.Group().setDEF(x3dpsail.SFString("ArrowRed"))
                .addChild(x3dpsail.Shape()
                  .setGeometry(x3dpsail.Cylinder().setUSE(x3dpsail.SFString("ArrowCylinder")))
                  .setAppearance(x3dpsail.Appearance().setDEF(x3dpsail.SFString("Red"))
                    .setMaterial(x3dpsail.Material().setDiffuseColor(x3dpsail.SFColor(0.7,0.1,0.1)).setEmissiveColor(x3dpsail.SFColor(0.33,0,0)))))
                .addChild(x3dpsail.Transform().setTranslation(x3dpsail.SFVec3f(0,1,0))
                  .addChild(x3dpsail.Shape()
                    .setGeometry(x3dpsail.Cone().setUSE(x3dpsail.SFString("ArrowCone")))
                    .setAppearance(x3dpsail.Appearance().setUSE(x3dpsail.SFString("Red"))))))
              .addChild(x3dpsail.Transform().setRotation(x3dpsail.SFRotation(0,0,1,1.57079)).setTranslation(x3dpsail.SFVec3f(0.072,1.1,0))
                #note label rotated back to original coordinate frame

                .addChild(x3dpsail.Billboard()
                  .addChild(x3dpsail.Shape()
                    .setAppearance(x3dpsail.Appearance().setUSE(x3dpsail.SFString("LABEL_APPEARANCE")))
                    .setGeometry(x3dpsail.Text().setString(x3dpsail.MFString(["X"]))
                      .setFontStyle(x3dpsail.FontStyle().setUSE(x3dpsail.SFString("LABEL_FONT")))))))))
          .setProxy(x3dpsail.Transform().setRotation(x3dpsail.SFRotation(1,0,0,1.57079))
            #Perpendicular Z arrow and label, note right-hand rule

            .addChild(x3dpsail.Group()
              .addChild(x3dpsail.Group().setDEF(x3dpsail.SFString("ArrowBlue"))
                .addChild(x3dpsail.Shape()
                  .setGeometry(x3dpsail.Cylinder().setUSE(x3dpsail.SFString("ArrowCylinder")))
                  .setAppearance(x3dpsail.Appearance().setDEF(x3dpsail.SFString("Blue"))
                    .setMaterial(x3dpsail.Material().setDiffuseColor(x3dpsail.SFColor(0.3,0.3,1)).setEmissiveColor(x3dpsail.SFColor(0.1,0.1,0.33)))))
                .addChild(x3dpsail.Transform().setTranslation(x3dpsail.SFVec3f(0,1,0))
                  .addChild(x3dpsail.Shape()
                    .setGeometry(x3dpsail.Cone().setUSE(x3dpsail.SFString("ArrowCone")))
                    .setAppearance(x3dpsail.Appearance().setUSE(x3dpsail.SFString("Blue"))))))
              .addChild(x3dpsail.Transform().setRotation(x3dpsail.SFRotation(1,0,0,-1.57079)).setTranslation(x3dpsail.SFVec3f(0,1.1,0.072))
                #note label rotated back to original coordinate frame

                .addChild(x3dpsail.Billboard()
                  .addChild(x3dpsail.Shape()
                    .setAppearance(x3dpsail.Appearance().setUSE(x3dpsail.SFString("LABEL_APPEARANCE")))
                    .setGeometry(x3dpsail.Text().setString(x3dpsail.MFString(["Z"]))
                      .setFontStyle(x3dpsail.FontStyle().setUSE(x3dpsail.SFString("LABEL_FONT"))))))))))))

X3D0.toFileX3D("./future/./CoordinateAxes_RoundTrip.x3d")
