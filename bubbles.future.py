import jnius_config
jnius_config.set_classpath('.', 'X3DJSAIL.3.3.full.jar')
from jnius import autoclass
from X3Dautoclass import *
X3D0 = X3DObject() \
   .setProfile("Immersive") \
   .setVersion("3.3") \
   .setHead(headObject() \
    .addComponent(componentObject() \
     .setName("EnvironmentalEffects") \
     .setLevel(1) \
    ) \
    .addComponent(componentObject() \
     .setName("EnvironmentalEffects") \
     .setLevel(3) \
    ) \
    .addComponent(componentObject() \
     .setName("Shaders") \
     .setLevel(1) \
    ) \
    .addComponent(componentObject() \
     .setName("CubeMapTexturing") \
     .setLevel(1) \
    ) \
    .addMeta(metaObject() \
     .setName("title") \
     .setContent("bubbles.x3d") \
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
     .setContent("https://coderextreme.net/X3DJSONLD/bubbles.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("description") \
     .setContent("not sure what this is") \
    ) \
   ) \
   .setScene(SceneObject() \
    .addChildren(NavigationInfoObject() \
     .setType(["EXAMINE"]) \
    ) \
    .addChildren(ViewpointObject() \
     .setDEF("Tour") \
     .setDescription("Tour Views") \
    ) \
    .addChildren(ViewpointObject() \
     .setPosition([0,0,4]) \
     .setDescription("sphere in road") \
    ) \
    .addChildren(BackgroundObject() \
     .setBackUrl(["../resources/images/all_probes/uffizi_cross/uffizi_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_back.png"]) \
     .setBottomUrl(["../resources/images/all_probes/uffizi_cross/uffizi_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_bottom.png"]) \
     .setFrontUrl(["../resources/images/all_probes/uffizi_cross/uffizi_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_front.png"]) \
     .setLeftUrl(["../resources/images/all_probes/uffizi_cross/uffizi_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_left.png"]) \
     .setRightUrl(["../resources/images/all_probes/uffizi_cross/uffizi_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_right.png"]) \
     .setTopUrl(["../resources/images/all_probes/uffizi_cross/uffizi_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_top.png"]) \
    ) \
    .addChildren(TransformObject() \
     .setDEF("Rose01") \
     .addChildren(ShapeObject() \
      .setGeometry(SphereObject() \
      ) \
      .setAppearance(AppearanceObject() \
       .setDEF("_01_-_Default") \
       .setMaterial(MaterialObject() \
        .setDiffuseColor([0.7,0.7,0.7]) \
        .setSpecularColor([0.5,0.5,0.5]) \
       ) \
       .setTexture(ComposedCubeMapTextureObject() \
        .setBack(ImageTextureObject() \
         .setUrl(["../resources/images/all_probes/uffizi_cross/uffizi_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_back.png"]) \
        ) \
        .setBottom(ImageTextureObject() \
         .setUrl(["../resources/images/all_probes/uffizi_cross/uffizi_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_bottom.png"]) \
        ) \
        .setFront(ImageTextureObject() \
         .setUrl(["../resources/images/all_probes/uffizi_cross/uffizi_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_front.png"]) \
        ) \
        .setLeft(ImageTextureObject() \
         .setUrl(["../resources/images/all_probes/uffizi_cross/uffizi_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_left.png"]) \
        ) \
        .setRight(ImageTextureObject() \
         .setUrl(["../resources/images/all_probes/uffizi_cross/uffizi_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_right.png"]) \
        ) \
        .setTop(ImageTextureObject() \
         .setUrl(["../resources/images/all_probes/uffizi_cross/uffizi_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_top.png"]) \
        ) \
       ) \
       .addShaders(ComposedShaderObject(language = "GLSL") \
        .setDEF("cobweb") \
        .addField(fieldObject() \
         .setName("cube") \
         .setAccessType("inputOutput") \
         .setType("SFInt32") \
         .setValue("0") \
        ) \
        .addField(fieldObject() \
         .setName("chromaticDispertion") \
         .setAccessType("inputOutput") \
         .setType("SFVec3f") \
         .setValue("0.98 1 1.033") \
        ) \
        .addField(fieldObject() \
         .setName("bias") \
         .setAccessType("inputOutput") \
         .setType("SFFloat") \
         .setValue("0.5") \
        ) \
        .addField(fieldObject() \
         .setName("scale") \
         .setAccessType("inputOutput") \
         .setType("SFFloat") \
         .setValue("0.5") \
        ) \
        .addField(fieldObject() \
         .setName("power") \
         .setAccessType("inputOutput") \
         .setType("SFFloat") \
         .setValue("2") \
        ) \
        .addParts(ShaderPartObject() \
         .setUrl(["../shaders/cobweb.vs","https://coderextreme.net/X3DJSONLD/shaders/cobweb.vs"]) \
         .setType("VERTEX") \
        ) \
        .addParts(ShaderPartObject() \
         .setUrl(["../shaders/pc_bubbles.fs","https://coderextreme.net/X3DJSONLD/shaders/pc_bubbles.fs"]) \
         .setType("FRAGMENT") \
        ) \
       ) \
       .addShaders(ComposedShaderObject(language = "GLSL") \
        .setDEF("x3dom") \
        .addField(fieldObject() \
         .setName("cube") \
         .setAccessType("inputOutput") \
         .setType("SFInt32") \
         .setValue("0") \
        ) \
        .addField(fieldObject() \
         .setName("chromaticDispertion") \
         .setAccessType("inputOutput") \
         .setType("SFVec3f") \
         .setValue("0.98 1 1.033") \
        ) \
        .addField(fieldObject() \
         .setName("bias") \
         .setAccessType("inputOutput") \
         .setType("SFFloat") \
         .setValue("0.5") \
        ) \
        .addField(fieldObject() \
         .setName("scale") \
         .setAccessType("inputOutput") \
         .setType("SFFloat") \
         .setValue("0.5") \
        ) \
        .addField(fieldObject() \
         .setName("power") \
         .setAccessType("inputOutput") \
         .setType("SFFloat") \
         .setValue("2") \
        ) \
        .addParts(ShaderPartObject() \
         .setUrl(["../shaders/x3dom.vs","https://coderextreme.net/X3DJSONLD/shaders/x3dom.vs"]) \
         .setType("VERTEX") \
        ) \
        .addParts(ShaderPartObject() \
         .setUrl(["../shaders/pc_bubbles.fs","https://coderextreme.net/X3DJSONLD/shaders/pc_bubbles.fs"]) \
         .setType("FRAGMENT") \
        ) \
       ) \
      ) \
     ) \
    ) \
    .addChildren(TimeSensorObject() \
     .setDEF("TourTime") \
     .setCycleInterval(5) \
     .setLoop(True) \
    ) \
    .addChildren(PositionInterpolatorObject() \
     .setDEF("TourPosition") \
     .setKey([0,1]) \
     .setKeyValue([0,0,10,0,0,-10]) \
    ) \
    .addChildren(OrientationInterpolatorObject() \
     .setDEF("TourOrientation") \
     .setKey([0,1]) \
     .setKeyValue([0,1,0,0,0,1,0,3.1416]) \
    ) \
    .addChildren(ScriptObject() \
     .setDEF("RandomTourTime") \
     .addField(fieldObject() \
      .setName("set_cycle") \
      .setAccessType("inputOnly") \
      .setType("SFTime") \
     ) \
     .addField(fieldObject() \
      .setName("lastKey") \
      .setAccessType("inputOutput") \
      .setType("SFFloat") \
      .setValue("0") \
     ) \
     .addField(fieldObject() \
      .setName("orientations") \
      .setAccessType("inputOutput") \
      .setType("MFRotation") \
      .setValue("0 1 0 0 0 1 0 -1.57 0 1 0 3.14 0 1 0 1.57 0 1 0 0 1 0 0 -1.57 0 1 0 0 1 0 0 1.57 0 1 0 0") \
     ) \
     .addField(fieldObject() \
      .setName("positions") \
      .setAccessType("inputOutput") \
      .setType("MFVec3f") \
      .setValue("0 0 10 -10 0 0 0 0 -10 10 0 0 0 0 10 0 10 0 0 0 10 0 -10 0 0 0 10") \
     ) \
     .addField(fieldObject() \
      .setName("position_changed") \
      .setAccessType("outputOnly") \
      .setType("MFVec3f") \
     ) \
     .addField(fieldObject() \
      .setName("set_orientation") \
      .setAccessType("inputOnly") \
      .setType("MFRotation") \
     ) \
     .addField(fieldObject() \
      .setName("orientation_changed") \
      .setAccessType("outputOnly") \
      .setType("MFRotation") \
     ) \
.setSourceCode('''ecmascript:\n"+
"               function set_cycle(value) {\n"+
"                        var ov = lastKey;\n"+
"                        do {\n"+
"                            lastKey = Math.round(Math.random()*(positions.length-1));\n"+
"                        } while (lastKey === ov);\n"+
"                        var vc = lastKey;\n"+
"\n"+
"                        orientation_changed = new MFRotation();\n"+
"                        orientation_changed[0] = new SFRotation(orientations[ov].x, orientations[ov].y, orientations[ov].z, orientations[ov].w);\n"+
"                        orientation_changed[1] = new SFRotation(orientations[vc].x, orientations[vc].y, orientations[vc].z, orientations[vc].w);\n"+
"                        position_changed = new MFVec3f();\n"+
"                        position_changed[0] = new SFVec3f(positions[ov].x,positions[ov].y,positions[ov].z);\n"+
"                        position_changed[1] = new SFVec3f(positions[vc].x,positions[vc].y,positions[vc].z);\n"+
"                    // }\n"+
"               }''')
    ) \
    .addChildren(ROUTEObject() \
     .setFromNode("TourTime") \
     .setFromField("cycleTime_changed") \
     .setToNode("RandomTourTime") \
     .setToField("set_cycle") \
    ) \
    .addChildren(ROUTEObject() \
     .setFromNode("RandomTourTime") \
     .setFromField("orientation_changed") \
     .setToNode("TourOrientation") \
     .setToField("set_keyValue") \
    ) \
    .addChildren(ROUTEObject() \
     .setFromNode("RandomTourTime") \
     .setFromField("position_changed") \
     .setToNode("TourPosition") \
     .setToField("set_keyValue") \
    ) \
    .addChildren(ROUTEObject() \
     .setFromNode("TourTime") \
     .setFromField("fraction_changed") \
     .setToNode("TourOrientation") \
     .setToField("set_fraction") \
    ) \
    .addChildren(ROUTEObject() \
     .setFromNode("TourOrientation") \
     .setFromField("value_changed") \
     .setToNode("Tour") \
     .setToField("set_orientation") \
    ) \
    .addChildren(ROUTEObject() \
     .setFromNode("TourTime") \
     .setFromField("fraction_changed") \
     .setToNode("TourPosition") \
     .setToField("set_fraction") \
    ) \
    .addChildren(ROUTEObject() \
     .setFromNode("TourPosition") \
     .setFromField("value_changed") \
     .setToNode("Tour") \
     .setToField("set_position") \
    ) \
   ) \

X3D0.toFileX3D("./future/./bubbles.newf.x3d")
