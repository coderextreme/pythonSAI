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
    .addChildren(ProtoDeclareObject() \
     .setName("Process") \
     .setProtoBody(ProtoBodyObject() \
      .addChildren(GroupObject() \
#left
       .addChildren(TransformObject() \
        .setScale([0.5,0.5,0.5]) \
        .addChildren(ShapeObject() \
         .setAppearance(AppearanceObject() \
          .setMaterial(MaterialObject() \
           .setDiffuseColor([0.7,1,0]) \
           .setTransparency(0.5) \
          ) \
         ) \
         .setGeometry(ExtrusionObject(creaseAngle = 0.785, crossSection = [1,0,0.92,-0.38,0.71,-0.71,0.38,-0.92,0,-1,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1,0,-0.92,0.38,-0.71,0.71,-0.38,0.92,0,1,0.38,0.92,0.71,0.71,0.92,0.38,1,0], spine = [-2.5,0,0,-1.5,0,0]) \
         ) \
        ) \
#<Transform translation=\"-2.5 0 0\"> <Shape> <Text DEF=\"LeftString\" string='\"l\"'/> </Shape> </Transform> <StringSensor DEF=\"LeftSensor\" enabled=\"false\"/> <TouchSensor DEF=\"LeftTouch\" enabled=\"true\"/>
       ) \
#right
       .addChildren(TransformObject() \
        .setScale([0.5,0.5,0.5]) \
        .addChildren(ShapeObject() \
         .setAppearance(AppearanceObject() \
          .setMaterial(MaterialObject() \
           .setDiffuseColor([0,0.7,1]) \
           .setTransparency(0.5) \
          ) \
         ) \
         .setGeometry(ExtrusionObject(creaseAngle = 0.785, crossSection = [1,0,0.92,-0.38,0.71,-0.71,0.38,-0.92,0,-1,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1,0,-0.92,0.38,-0.71,0.71,-0.38,0.92,0,1,0.38,0.92,0.71,0.71,0.92,0.38,1,0], spine = [1.5,0,0,2.5,0,0]) \
         ) \
        ) \
        .addChildren(TransformObject() \
         .setTranslation([2,0,0]) \
         .addChildren(ShapeObject() \
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
        .addChildren(StringSensorObject() \
         .setDEF("RightSensor") \
         .setEnabled(False) \
        ) \
        .addChildren(TouchSensorObject() \
         .setDescription("touch to activate") \
         .setDEF("RightTouch") \
        ) \
       ) \
#up
       .addChildren(TransformObject() \
        .setScale([0.5,0.5,0.5]) \
        .addChildren(ShapeObject() \
         .setAppearance(AppearanceObject() \
          .setMaterial(MaterialObject() \
           .setDiffuseColor([0,0.7,1]) \
           .setTransparency(0.5) \
          ) \
         ) \
         .setGeometry(ExtrusionObject(creaseAngle = 0.785, crossSection = [1,0,0.92,-0.38,0.71,-0.71,0.38,-0.92,0,-1,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1,0,-0.92,0.38,-0.71,0.71,-0.38,0.92,0,1,0.38,0.92,0.71,0.71,0.92,0.38,1,0], spine = [0,1.5,0,0,2.5,0]) \
         ) \
        ) \
        .addChildren(TransformObject() \
         .setTranslation([-0.5,2,0]) \
         .addChildren(ShapeObject() \
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
        .addChildren(StringSensorObject() \
         .setDEF("UpSensor") \
         .setEnabled(False) \
        ) \
        .addChildren(TouchSensorObject() \
         .setDescription("touch to activate") \
         .setDEF("UpTouch") \
        ) \
       ) \
#down
       .addChildren(TransformObject() \
        .setScale([0.5,0.5,0.5]) \
        .addChildren(ShapeObject() \
         .setAppearance(AppearanceObject() \
          .setMaterial(MaterialObject() \
           .setDiffuseColor([0.7,1,0]) \
           .setTransparency(0.5) \
          ) \
         ) \
         .setGeometry(ExtrusionObject(creaseAngle = 0.785, crossSection = [1,0,0.92,-0.38,0.71,-0.71,0.38,-0.92,0,-1,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1,0,-0.92,0.38,-0.71,0.71,-0.38,0.92,0,1,0.38,0.92,0.71,0.71,0.92,0.38,1,0], spine = [0,-2.5,0,0,-1.5,0]) \
         ) \
        ) \
#<Transform translation=\"-0.5 -2.5 0\"> <Shape> <Text DEF=\"DownString\" string='\"d\"'/> </Shape> </Transform> <StringSensor DEF=\"DownSensor\" enabled=\"false\"/> <TouchSensor description='touch to activate' DEF=\"DownTouch\" enabled=\"true\"/>
       ) \
#center
       .addChildren(TransformObject() \
        .addChildren(ShapeObject() \
         .setAppearance(AppearanceObject() \
          .setMaterial(MaterialObject() \
           .setDiffuseColor([1,0,0.7]) \
          ) \
         ) \
         .setGeometry(SphereObject() \
         ) \
        ) \
        .addChildren(TransformObject() \
         .setScale([0.5,0.5,0.5]) \
         .setTranslation([-0.5,0,1]) \
         .addChildren(ShapeObject() \
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
        .addChildren(StringSensorObject() \
         .setDEF("CenterSensor") \
         .setEnabled(False) \
        ) \
        .addChildren(TouchSensorObject() \
         .setDescription("touch to activate") \
         .setDEF("CenterTouch") \
        ) \
       ) \
      ) \
      .addChildren(ScriptObject() \
       .setDEF("RightSingleToMultiString") \
       .addField(fieldObject() \
        .setName("set_rightstring") \
        .setAccessType("inputOnly") \
        .setType("SFString") \
       ) \
       .addField(fieldObject() \
        .setName("rightlines") \
        .setAccessType("outputOnly") \
        .setType("MFString") \
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
      .addChildren(ScriptObject() \
       .setDEF("UpSingleToMultiString") \
       .addField(fieldObject() \
        .setName("set_upstring") \
        .setAccessType("inputOnly") \
        .setType("SFString") \
       ) \
       .addField(fieldObject() \
        .setName("uplines") \
        .setAccessType("outputOnly") \
        .setType("MFString") \
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
      .addChildren(ScriptObject() \
       .setDEF("CenterSingleToMultiString") \
       .addField(fieldObject() \
        .setName("set_centerstring") \
        .setAccessType("inputOnly") \
        .setType("SFString") \
       ) \
       .addField(fieldObject() \
        .setName("centerlines") \
        .setAccessType("outputOnly") \
        .setType("MFString") \
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
      .addChildren(ROUTEObject() \
       .setFromField("enteredText") \
       .setFromNode("CenterSensor") \
       .setToField("set_centerstring") \
       .setToNode("CenterSingleToMultiString") \
      ) \
      .addChildren(ROUTEObject() \
       .setFromField("centerlines") \
       .setFromNode("CenterSingleToMultiString") \
       .setToField("set_string") \
       .setToNode("CenterString") \
      ) \
      .addChildren(ROUTEObject() \
       .setFromField("isOver") \
       .setFromNode("CenterTouch") \
       .setToField("set_enabled") \
       .setToNode("CenterSensor") \
      ) \
      .addChildren(ROUTEObject() \
       .setFromField("enteredText") \
       .setFromNode("RightSensor") \
       .setToField("set_rightstring") \
       .setToNode("RightSingleToMultiString") \
      ) \
      .addChildren(ROUTEObject() \
       .setFromField("rightlines") \
       .setFromNode("RightSingleToMultiString") \
       .setToField("set_string") \
       .setToNode("RightString") \
      ) \
      .addChildren(ROUTEObject() \
       .setFromField("isOver") \
       .setFromNode("RightTouch") \
       .setToField("set_enabled") \
       .setToNode("RightSensor") \
      ) \
      .addChildren(ROUTEObject() \
       .setFromField("enteredText") \
       .setFromNode("UpSensor") \
       .setToField("set_upstring") \
       .setToNode("UpSingleToMultiString") \
      ) \
      .addChildren(ROUTEObject() \
       .setFromField("uplines") \
       .setFromNode("UpSingleToMultiString") \
       .setToField("set_string") \
       .setToNode("UpString") \
      ) \
      .addChildren(ROUTEObject() \
       .setFromField("isOver") \
       .setFromNode("UpTouch") \
       .setToField("set_enabled") \
       .setToNode("UpSensor") \
      ) \
     ) \
    ) \
    .addChildren(NavigationInfoObject() \
    ) \
    .addChildren(ViewpointObject() \
     .setDescription("Process pipes") \
     .setOrientation([1,0,0,-0.4]) \
     .setPosition([0,5,12]) \
    ) \
    .addChildren(TransformObject() \
     .setTranslation([0,-2.5,0]) \
     .addChildren(ProtoInstanceObject() \
      .setName("Process") \
     ) \
    ) \
    .addChildren(TransformObject() \
     .addChildren(ProtoInstanceObject() \
      .setName("Process") \
     ) \
    ) \
    .addChildren(TransformObject() \
     .setTranslation([0,2.5,0]) \
     .addChildren(ProtoInstanceObject() \
      .setName("Process") \
     ) \
    ) \
   ) \

X3D0.toFileX3D("./future/./pp3.newf.x3d")
