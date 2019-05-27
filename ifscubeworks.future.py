import x3dpsail


X3D0 = (x3dpsail.X3D().setProfile(x3dpsail.SFString("Interchange")).setVersion(x3dpsail.SFString("3.3"))
      .setHead(x3dpsail.head()
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("title")).setContent(x3dpsail.SFString("template.json")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("identifier")).setContent(x3dpsail.SFString("http://coderextreme.net/X3DJSONLD/template.json")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("description")).setContent(x3dpsail.SFString("Template for an Indexed Face Set")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("creator")).setContent(x3dpsail.SFString("John Carlson")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("created")).setContent(x3dpsail.SFString("4 April 2017"))))
      .setScene(x3dpsail.Scene()
        .addChild(x3dpsail.Group()
          .addChild(x3dpsail.Shape()
            .setGeometry(x3dpsail.IndexedFaceSet().setDEF(x3dpsail.SFString("IndexedFaceSet")).setCoordIndex(x3dpsail.MFInt32([0,0,1,-1,0,1,1,-1,2,2,3,3,-1,0,3,3,0,-1,0,3,2,1,-1,1,2,2,1,-1,1,2,3,0,-1])).setNormalIndex(x3dpsail.MFInt32([0,0,1,2,3,4,5])).setNormalPerVertex(x3dpsail.SFBool(False)).setColorIndex(x3dpsail.MFInt32([0,0,0,-1,0,0,0,-1,0,0,0,0,-1,0,0,0,0,-1,0,0,0,0,-1,0,0,0,0,-1,0,0,0,0,-1]))
              .setCoord(x3dpsail.Coordinate().setPoint(x3dpsail.MFVec3f([0,0,1,0,1,1,1,1,1,1,0,1])))
              .setNormal(x3dpsail.Normal().setVector(x3dpsail.MFVec3f([1,0,0,-1,0,0,0,1,0,0,0,-1,0,-1,0,0,0,1])))
              .setColor(x3dpsail.Color().setColor(x3dpsail.MFColor([0,1,0]))))))))

X3D0.toFileX3D("./future/./ifscubeworks_RoundTrip.x3d")
