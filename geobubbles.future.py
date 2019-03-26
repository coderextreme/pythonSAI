import jnius_config
jnius_config.set_classpath('.', 'X3DJSAIL.3.3.full.jar')
from jnius import autoclass
from X3Dautoclass import *
X3D0 = X3DObject() \
   .setProfile("Immersive") \
   .setVersion("3.3") \
   .setHead(headObject() \
    .addComponent(componentObject() \
     .setName("Geospatial") \
     .setLevel(1) \
    ) \
    .addMeta(metaObject() \
     .setName("title") \
     .setContent("geobubbles.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("creator") \
     .setContent("John Carlson") \
    ) \
    .addMeta(metaObject() \
     .setName("generator") \
     .setContent("manual") \
    ) \
    .addMeta(metaObject() \
     .setName("identifier") \
     .setContent("https://coderextreme.net/X3DJSONLD/geobubbles.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("description") \
     .setContent("geo bubbles") \
    ) \
   ) \
   .setScene(SceneObject() \
#Viewpoint DEF='Tour' position='0 0 4' orientation='1 0 0 0' description='Tour Views'/
#PositionInterpolator DEF='TourPosition' key='0 1' keyValue='-0.5 -0.5 4 -0.5 0.5 4'/
    .addChildren(GeoViewpointObject() \
     .setDEF("Tour") \
     .setPosition([0,0,4]) \
     .setOrientation([1,0,0,0]) \
     .setDescription("Tour Views") \
    ) \
    .addChildren(BackgroundObject() \
     .setBackUrl(["../resources/images/BK.png","https://coderextreme.net/X3DJSONLD/images/BK.png"]) \
     .setBottomUrl(["../resources/images/BT.png","https://coderextreme.net/X3DJSONLD/images/BT.png"]) \
     .setFrontUrl(["../resources/images/FR.png","https://coderextreme.net/X3DJSONLD/images/FR.png"]) \
     .setLeftUrl(["../resources/images/LF.png","https://coderextreme.net/X3DJSONLD/images/LF.png"]) \
     .setRightUrl(["../resources/images/RT.png","https://coderextreme.net/X3DJSONLD/images/RT.png"]) \
     .setTopUrl(["../resources/images/TP.png","https://coderextreme.net/X3DJSONLD/images/TP.png"]) \
    ) \
    .addChildren(TransformObject() \
     .addChildren(ShapeObject() \
      .setGeometry(SphereObject() \
      ) \
      .setAppearance(AppearanceObject() \
       .setMaterial(MaterialObject() \
        .setDiffuseColor([0.7,0.7,0.7]) \
        .setSpecularColor([0.5,0.5,0.5]) \
       ) \
      ) \
     ) \
    ) \
    .addChildren(TimeSensorObject() \
     .setDEF("TourTime") \
     .setCycleInterval(5) \
     .setLoop(True) \
    ) \
    .addChildren(GeoPositionInterpolatorObject() \
     .setDEF("TourPosition") \
     .setKey([0,1]) \
     .setKeyValue([0.0015708,0,4,0,0.0015708,4]) \
    ) \
    .addChildren(ScriptObject() \
     .setDEF("RandomTourTime") \
     .addField(fieldObject() \
      .setName("set_cycle") \
      .setAccessType("inputOnly") \
      .setType("SFTime") \
     ) \
     .addField(fieldObject() \
      .setName("val") \
      .setAccessType("inputOutput") \
      .setType("SFFloat") \
      .setValue("0") \
     ) \
     .addField(fieldObject() \
      .setName("positions") \
      .setAccessType("inputOutput") \
      .setType("MFVec3d") \
      .setValue("0.0015708 0 4 0 0.0015708 4") \
     ) \
     .addField(fieldObject() \
      .setName("position") \
      .setAccessType("inputOutput") \
      .setType("MFVec3d") \
      .setValue("0.0015708 0 4 0 0.0015708 4") \
     ) \
.setSourceCode('''ecmascript:\n"+
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
    ) \
    .addChildren(ROUTEObject() \
     .setFromNode("TourTime") \
     .setFromField("cycleTime") \
     .setToNode("RandomTourTime") \
     .setToField("set_cycle") \
    ) \
    .addChildren(ROUTEObject() \
     .setFromNode("RandomTourTime") \
     .setFromField("position") \
     .setToNode("TourPosition") \
     .setToField("keyValue") \
    ) \
    .addChildren(ROUTEObject() \
     .setFromNode("TourTime") \
     .setFromField("fraction_changed") \
     .setToNode("TourPosition") \
     .setToField("set_fraction") \
    ) \
    .addChildren(ROUTEObject() \
     .setFromNode("TourPosition") \
     .setFromField("geovalue_changed") \
     .setToNode("Tour") \
     .setToField("set_position") \
    ) \
   ) \

X3D0.toFileX3D("./future/./geobubbles.newf.x3d")
