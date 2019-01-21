import jnius_config
jnius_config.set_classpath('.', 'X3DJSAIL.3.3.full.jar')
from jnius import autoclass
from X3Dautoclass import *
X3D0 = X3DObject() \
   .setProfile("Immersive") \
   .setVersion("3.3") \
   .setHead(headObject() \
    .addMeta(metaObject() \
     .setName("title") \
     .setContent("pp3.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("creator") \
     .setContent("John Carlson") \
    ) \
    .addMeta(metaObject() \
     .setName("translator") \
     .setContent("John Carlson") \
    ) \
    .addMeta(metaObject() \
     .setName("created") \
     .setContent("5 May 2015") \
    ) \
    .addMeta(metaObject() \
     .setName("modified") \
     .setContent("05 May 2017") \
    ) \
    .addMeta(metaObject() \
     .setName("description") \
     .setContent("A process pipeline between three spheres (try typing on spheres and blue") \
    ) \
    .addMeta(metaObject() \
     .setName("identifier") \
     .setContent("https://coderextreme.net/x3d/pp3.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("generator") \
     .setContent("manual") \
    ) \
   ) \
   .setScene(SceneObject() \
    .addChild(ProtoDeclareObject() \
     .setName("Process") \
     .setProtoBody(ProtoBodyObject() \
      .addChild(GroupObject() \
.addComments(CommentsBlock("""left""")) \
       .addChild(TransformObject() \
        .setScale([0.5,0.5,0.5]) \
        .addChild(ShapeObject() \
         .setAppearance(AppearanceObject() \
          .setMaterial(MaterialObject() \
           .setDiffuseColor([0.7,1,0]) \
           .setTransparency(0.5) \
          ) \
         ) \
         .setGeometry(ExtrusionObject() \
          .setCreaseAngle(0.785) \
          .setCrossSection([1,0,0.92,-0.38,0.71,-0.71,0.38,-0.92,0,-1,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1,0,-0.92,0.38,-0.71,0.71,-0.38,0.92,0,1,0.38,0.92,0.71,0.71,0.92,0.38,1,0]) \
          .setSpine([-2.5,0,0,-1.5,0,0]) \
         ) \
        ) \
.addComments(CommentsBlock("""<Transform translation=\"-2.5 0 0\"> <Shape> <Text DEF=\"LeftString\" string='\"l\"'/> </Shape> </Transform> <StringSensor DEF=\"LeftSensor\" enabled=\"false\"/> <TouchSensor DEF=\"LeftTouch\" enabled=\"true\"/>""")) \
       ) \
.addComments(CommentsBlock("""right""")) \
       .addChild(TransformObject() \
        .setScale([0.5,0.5,0.5]) \
        .addChild(ShapeObject() \
         .setAppearance(AppearanceObject() \
          .setMaterial(MaterialObject() \
           .setDiffuseColor([0,0.7,1]) \
           .setTransparency(0.5) \
          ) \
         ) \
         .setGeometry(ExtrusionObject() \
          .setCreaseAngle(0.785) \
          .setCrossSection([1,0,0.92,-0.38,0.71,-0.71,0.38,-0.92,0,-1,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1,0,-0.92,0.38,-0.71,0.71,-0.38,0.92,0,1,0.38,0.92,0.71,0.71,0.92,0.38,1,0]) \
          .setSpine([1.5,0,0,2.5,0,0]) \
         ) \
        ) \
        .addChild(TransformObject() \
         .setTranslation([2,0,0]) \
         .addChild(ShapeObject() \
          .setAppearance(AppearanceObject() \
           .setMaterial(MaterialObject() \
            .setDEF("MaterialLightBlue") \
            .setDiffuseColor([1,1,1]) \
           ) \
          ) \
          .setGeometry(TextObject() \
           .setDEF("RightString") \
           .setString(["r"]) \
          ) \
         ) \
        ) \
        .addChild(StringSensorObject() \
         .setDEF("RightSensor") \
         .setEnabled(False) \
        ) \
        .addChild(TouchSensorObject() \
         .setDescription("touch to activate") \
         .setDEF("RightTouch") \
        ) \
       ) \
.addComments(CommentsBlock("""up""")) \
       .addChild(TransformObject() \
        .setScale([0.5,0.5,0.5]) \
        .addChild(ShapeObject() \
         .setAppearance(AppearanceObject() \
          .setMaterial(MaterialObject() \
           .setDiffuseColor([0,0.7,1]) \
           .setTransparency(0.5) \
          ) \
         ) \
         .setGeometry(ExtrusionObject() \
          .setCreaseAngle(0.785) \
          .setCrossSection([1,0,0.92,-0.38,0.71,-0.71,0.38,-0.92,0,-1,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1,0,-0.92,0.38,-0.71,0.71,-0.38,0.92,0,1,0.38,0.92,0.71,0.71,0.92,0.38,1,0]) \
          .setSpine([0,1.5,0,0,2.5,0]) \
         ) \
        ) \
        .addChild(TransformObject() \
         .setTranslation([-0.5,2,0]) \
         .addChild(ShapeObject() \
          .setAppearance(AppearanceObject() \
           .setMaterial(MaterialObject() \
            .setUSE("MaterialLightBlue") \
           ) \
          ) \
          .setGeometry(TextObject() \
           .setDEF("UpString") \
           .setString(["u"]) \
          ) \
         ) \
        ) \
        .addChild(StringSensorObject() \
         .setDEF("UpSensor") \
         .setEnabled(False) \
        ) \
        .addChild(TouchSensorObject() \
         .setDescription("touch to activate") \
         .setDEF("UpTouch") \
        ) \
       ) \
.addComments(CommentsBlock("""down""")) \
       .addChild(TransformObject() \
        .setScale([0.5,0.5,0.5]) \
        .addChild(ShapeObject() \
         .setAppearance(AppearanceObject() \
          .setMaterial(MaterialObject() \
           .setDiffuseColor([0.7,1,0]) \
           .setTransparency(0.5) \
          ) \
         ) \
         .setGeometry(ExtrusionObject() \
          .setCreaseAngle(0.785) \
          .setCrossSection([1,0,0.92,-0.38,0.71,-0.71,0.38,-0.92,0,-1,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1,0,-0.92,0.38,-0.71,0.71,-0.38,0.92,0,1,0.38,0.92,0.71,0.71,0.92,0.38,1,0]) \
          .setSpine([0,-2.5,0,0,-1.5,0]) \
         ) \
        ) \
.addComments(CommentsBlock("""<Transform translation=\"-0.5 -2.5 0\"> <Shape> <Text DEF=\"DownString\" string='\"d\"'/> </Shape> </Transform> <StringSensor DEF=\"DownSensor\" enabled=\"false\"/> <TouchSensor description='touch to activate' DEF=\"DownTouch\" enabled=\"true\"/>""")) \
       ) \
.addComments(CommentsBlock("""center""")) \
       .addChild(TransformObject() \
        .addChild(ShapeObject() \
         .setAppearance(AppearanceObject() \
          .setMaterial(MaterialObject() \
           .setDiffuseColor([1,0,0.7]) \
          ) \
         ) \
         .setGeometry(SphereObject() \
         ) \
        ) \
        .addChild(TransformObject() \
         .setScale([0.5,0.5,0.5]) \
         .setTranslation([-0.5,0,1]) \
         .addChild(ShapeObject() \
          .setAppearance(AppearanceObject() \
           .setMaterial(MaterialObject() \
            .setUSE("MaterialLightBlue") \
           ) \
          ) \
          .setGeometry(TextObject() \
           .setDEF("CenterString") \
          ) \
         ) \
        ) \
        .addChild(StringSensorObject() \
         .setDEF("CenterSensor") \
         .setEnabled(False) \
        ) \
        .addChild(TouchSensorObject() \
         .setDescription("touch to activate") \
         .setDEF("CenterTouch") \
        ) \
       ) \
      ) \
      .addChild(ScriptObject() \
       .setDEF("RightSingleToMultiString") \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFSTRING) \
        .setName("set_rightstring") \
        .setAccessType(fieldObject.ACCESSTYPE_INPUTONLY) \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_MFSTRING) \
        .setName("rightlines") \
        .setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY) \
       ) \
.setSourceCode('''ecmascript:\n"+
"\n"+
"function initialize() {\n"+
"	rightlines = new MFString(\"\");\n"+
"}\n"+
"\n"+
"function set_rightstring(rightstr) {\n"+
"	rightlines = new MFString(rightstr);\n"+
"}''')
      ) \
      .addChild(ScriptObject() \
       .setDEF("UpSingleToMultiString") \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFSTRING) \
        .setName("set_upstring") \
        .setAccessType(fieldObject.ACCESSTYPE_INPUTONLY) \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_MFSTRING) \
        .setName("uplines") \
        .setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY) \
       ) \
.setSourceCode('''ecmascript:\n"+
"\n"+
"function initialize() {\n"+
"	uplines = new MFString(\"\");\n"+
"}\n"+
"\n"+
"function set_upstring(upstr) {\n"+
"	uplines = new MFString(upstr);\n"+
"}''')
      ) \
      .addChild(ScriptObject() \
       .setDEF("CenterSingleToMultiString") \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_SFSTRING) \
        .setName("set_centerstring") \
        .setAccessType(fieldObject.ACCESSTYPE_INPUTONLY) \
       ) \
       .addField(fieldObject() \
        .setType(fieldObject.TYPE_MFSTRING) \
        .setName("centerlines") \
        .setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY) \
       ) \
.setSourceCode('''ecmascript:\n"+
"\n"+
"function initialize() {\n"+
"	centerlines = new MFString(\"\");\n"+
"}\n"+
"\n"+
"function set_centerstring(centerstr) {\n"+
"	centerlines = new MFString(centerstr);\n"+
"}''')
      ) \
      .addChild(ROUTEObject() \
       .setFromField("enteredText") \
       .setFromNode("CenterSensor") \
       .setToField("set_centerstring") \
       .setToNode("CenterSingleToMultiString") \
      ) \
      .addChild(ROUTEObject() \
       .setFromField("centerlines") \
       .setFromNode("CenterSingleToMultiString") \
       .setToField("set_string") \
       .setToNode("CenterString") \
      ) \
      .addChild(ROUTEObject() \
       .setFromField("isOver") \
       .setFromNode("CenterTouch") \
       .setToField("set_enabled") \
       .setToNode("CenterSensor") \
      ) \
      .addChild(ROUTEObject() \
       .setFromField("enteredText") \
       .setFromNode("RightSensor") \
       .setToField("set_rightstring") \
       .setToNode("RightSingleToMultiString") \
      ) \
      .addChild(ROUTEObject() \
       .setFromField("rightlines") \
       .setFromNode("RightSingleToMultiString") \
       .setToField("set_string") \
       .setToNode("RightString") \
      ) \
      .addChild(ROUTEObject() \
       .setFromField("isOver") \
       .setFromNode("RightTouch") \
       .setToField("set_enabled") \
       .setToNode("RightSensor") \
      ) \
      .addChild(ROUTEObject() \
       .setFromField("enteredText") \
       .setFromNode("UpSensor") \
       .setToField("set_upstring") \
       .setToNode("UpSingleToMultiString") \
      ) \
      .addChild(ROUTEObject() \
       .setFromField("uplines") \
       .setFromNode("UpSingleToMultiString") \
       .setToField("set_string") \
       .setToNode("UpString") \
      ) \
      .addChild(ROUTEObject() \
       .setFromField("isOver") \
       .setFromNode("UpTouch") \
       .setToField("set_enabled") \
       .setToNode("UpSensor") \
      ) \
     ) \
    ) \
    .addChild(NavigationInfoObject() \
    ) \
    .addChild(ViewpointObject() \
     .setDescription("Process pipes") \
     .setOrientation([1,0,0,-0.4]) \
     .setPosition([0,5,12]) \
    ) \
    .addChild(TransformObject() \
     .setTranslation([0,-2.5,0]) \
     .addChild(ProtoInstanceObject() \
      .setName("Process") \
     ) \
    ) \
    .addChild(TransformObject() \
     .addChild(ProtoInstanceObject() \
      .setName("Process") \
     ) \
    ) \
    .addChild(TransformObject() \
     .setTranslation([0,2.5,0]) \
     .addChild(ProtoInstanceObject() \
      .setName("Process") \
     ) \
    ) \
   ) \

X3D0.toFileX3D("./future/./pp3.newf.x3d")
