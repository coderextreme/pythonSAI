import x3dpsail


X3D0 = (x3dpsail.X3D().setProfile(x3dpsail.SFString("Immersive")).setVersion(x3dpsail.SFString("3.3"))
      .setHead(x3dpsail.head()
        .addComponent(x3dpsail.component().setName(x3dpsail.SFString("Geospatial")).setLevel(x3dpsail.SFInt32(1)))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("title")).setContent(x3dpsail.SFString("geobubbles.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("creator")).setContent(x3dpsail.SFString("John Carlson")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("generator")).setContent(x3dpsail.SFString("manual")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("identifier")).setContent(x3dpsail.SFString("https://coderextreme.net/X3DJSONLD/geobubbles.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("description")).setContent(x3dpsail.SFString("geo bubbles"))))
      .setScene(x3dpsail.Scene()
        #Viewpoint DEF='Tour' position='0 0 4' orientation='1 0 0 0' description='Tour Views'/

        #PositionInterpolator DEF='TourPosition' key='0 1' keyValue='-0.5 -0.5 4 -0.5 0.5 4'/

        .addChild(x3dpsail.GeoViewpoint().setDEF(x3dpsail.SFString("Tour")).setPosition(x3dpsail.SFVec3d(0,0,4)).setOrientation(x3dpsail.SFRotation(1,0,0,0)).setDescription(x3dpsail.SFString("Tour Views")))
        .addChild(x3dpsail.Background().setBackUrl(x3dpsail.MFString(["../resources/images/BK.png","https://coderextreme.net/X3DJSONLD/images/BK.png"])).setBottomUrl(x3dpsail.MFString(["../resources/images/BT.png","https://coderextreme.net/X3DJSONLD/images/BT.png"])).setFrontUrl(x3dpsail.MFString(["../resources/images/FR.png","https://coderextreme.net/X3DJSONLD/images/FR.png"])).setLeftUrl(x3dpsail.MFString(["../resources/images/LF.png","https://coderextreme.net/X3DJSONLD/images/LF.png"])).setRightUrl(x3dpsail.MFString(["../resources/images/RT.png","https://coderextreme.net/X3DJSONLD/images/RT.png"])).setTopUrl(x3dpsail.MFString(["../resources/images/TP.png","https://coderextreme.net/X3DJSONLD/images/TP.png"])))
        .addChild(x3dpsail.Transform()
          .addChild(x3dpsail.Shape()
            .setGeometry(x3dpsail.Sphere())
            .setAppearance(x3dpsail.Appearance()
              .setMaterial(x3dpsail.Material().setDiffuseColor(x3dpsail.SFColor(0.7,0.7,0.7)).setSpecularColor(x3dpsail.SFColor(0.5,0.5,0.5))))))
        .addChild(x3dpsail.TimeSensor().setDEF(x3dpsail.SFString("TourTime")).setCycleInterval(x3dpsail.SFTime(5)).setLoop(x3dpsail.SFBool(True)))
        .addChild(x3dpsail.GeoPositionInterpolator().setDEF(x3dpsail.SFString("TourPosition")).setKey(x3dpsail.MFFloat([0,1])).setKeyValue(x3dpsail.MFVec3d([0.0015708,0,4,0,0.0015708,4])))
        .addChild(x3dpsail.Script().setDEF(x3dpsail.SFString("RandomTourTime"))
          .addField(x3dpsail.field().setName(x3dpsail.SFString("set_cycle")).setAccessType(x3dpsail.SFString("inputOnly")).setType(x3dpsail.SFString("SFTime")))
          .addField(x3dpsail.field().setName(x3dpsail.SFString("val")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("SFFloat")).setValue(x3dpsail.SFString("0")))
          .addField(x3dpsail.field().setName(x3dpsail.SFString("positions")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("MFVec3d")).setValue(x3dpsail.SFString("0.0015708 0 4 0 0.0015708 4")))
          .addField(x3dpsail.field().setName(x3dpsail.SFString("position")).setAccessType(x3dpsail.SFString("inputOutput")).setType(x3dpsail.SFString("MFVec3d")).setValue(x3dpsail.SFString("0.0015708 0 4 0 0.0015708 4"))).setSourceCode('''ecmascript:\n"+
"\n"+
"               function set_cycle(value) {\n"+
"                        var cartesianMult = -150;  // -150 if cartesian, 1 if geo\n"+
"                        var ov = val;\n"+
"			// Browser.print('old '+ov);\n"+
"                        do {\n"+
"                                val = Math.floor(Math.random()*2);\n"+
"                                var vc = val;\n"+
"                                positions[vc] = new SFVec3d(Math.round(Math.random()*2)*0.0015708*cartesianMult, Math.round(Math.random()*2)*0.0015708*cartesianMult, 4);\n"+
"                        } while ( positions[ov][0] === positions[vc][0] && positions[ov][1] === positions[vc][1] && positions[ov][2] === positions[vc][2]);\n"+
"			// Browser.println(positions[ov]);\n"+
"			// Browser.println(positions[vc]);\n"+
"                        position = new MFVec3d();\n"+
"                        position[0] = new SFVec3d(positions[ov][0],positions[ov][1],positions[ov][2]);\n"+
"                        position[1] = new SFVec3d(positions[vc][0],positions[vc][1],positions[vc][2]);\n"+
"               }''')
)
        .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("TourTime")).setFromField(x3dpsail.SFString("cycleTime")).setToNode(x3dpsail.SFString("RandomTourTime")).setToField(x3dpsail.SFString("set_cycle")))
        .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("RandomTourTime")).setFromField(x3dpsail.SFString("position")).setToNode(x3dpsail.SFString("TourPosition")).setToField(x3dpsail.SFString("keyValue")))
        .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("TourTime")).setFromField(x3dpsail.SFString("fraction_changed")).setToNode(x3dpsail.SFString("TourPosition")).setToField(x3dpsail.SFString("set_fraction")))
        .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("TourPosition")).setFromField(x3dpsail.SFString("geovalue_changed")).setToNode(x3dpsail.SFString("Tour")).setToField(x3dpsail.SFString("set_position")))))

X3D0.toFileX3D("./future/./geobubbles_RoundTrip.x3d")
