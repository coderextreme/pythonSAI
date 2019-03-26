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
     .setContent("BindingOperations.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("description") \
     .setContent("Illustrate Viewpoint binding operations (in gory detail!) as described in Chapter 4 concepts. Scene design: a TimeSensor clock drives and IntegerSequencer for each t0/t1/etc. event, and a customized Script node sends bind/unbind events to the correct Viewpoint. Display the browser console to see occurrence of each event.") \
    ) \
    .addMeta(metaObject() \
     .setName("creator") \
     .setContent("Don Brutzman") \
    ) \
    .addMeta(metaObject() \
     .setName("created") \
     .setContent("5 January 2008") \
    ) \
    .addMeta(metaObject() \
     .setName("modified") \
     .setContent("22 July 2013") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("BindingOperations.console.txt") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("BindingStackOperations.png") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("X3D for Web Authors, Section 2.5.1, Figure 4.1") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("http://X3dGraphics.com") \
    ) \
    .addMeta(metaObject() \
     .setName("reference") \
     .setContent("http://www.web3d.org/x3d/content/examples/X3dResources.html") \
    ) \
    .addMeta(metaObject() \
     .setName("rights") \
     .setContent("Copyright Don Brutzman and Leonard Daly 2007") \
    ) \
    .addMeta(metaObject() \
     .setName("subject") \
     .setContent("X3D book, X3D graphics, X3D-Edit, http://www.x3dGraphics.com") \
    ) \
    .addMeta(metaObject() \
     .setName("identifier") \
     .setContent("http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter04ViewingNavigation/BindingOperations.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("generator") \
     .setContent("X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit") \
    ) \
    .addMeta(metaObject() \
     .setName("license") \
     .setContent("../license.html") \
    ) \
   ) \
   .setScene(SceneObject() \
    .addChildren(ViewpointObject() \
     .setDEF("View1") \
     .setCenterOfRotation([-6,0,0]) \
     .setDescription("Viewpoint 1") \
     .setPosition([-6,0,5]) \
    ) \
    .addChildren(ViewpointObject() \
     .setDEF("View2") \
     .setCenterOfRotation([-2,0,0]) \
     .setDescription("Viewpoint 2") \
     .setPosition([-2,0,5]) \
    ) \
    .addChildren(ViewpointObject() \
     .setDEF("View3") \
     .setCenterOfRotation([2,0,0]) \
     .setDescription("Viewpoint 3") \
     .setPosition([2,0,5]) \
    ) \
    .addChildren(ViewpointObject() \
     .setDEF("View4") \
     .setCenterOfRotation([6,0,0]) \
     .setDescription("Viewpoint 4") \
     .setPosition([6,0,5]) \
    ) \
#Script initialization ought to first bind view5 below.
    .addChildren(GroupObject() \
     .addChildren(TransformObject() \
      .setDEF("Text1") \
      .setTranslation([-6,0,0]) \
      .addChildren(ShapeObject() \
       .setGeometry(TextObject() \
        .setString(["View","# 1"]) \
        .setFontStyle(FontStyleObject(justify = ["MIDDLE","MIDDLE"]) \
         .setDEF("CenterJustify") \
        ) \
       ) \
       .setAppearance(AppearanceObject() \
        .setMaterial(MaterialObject() \
         .setDiffuseColor([1,0,0]) \
        ) \
       ) \
      ) \
     ) \
     .addChildren(TransformObject() \
      .setDEF("Text2") \
      .setTranslation([-2,0,0]) \
      .addChildren(ShapeObject() \
       .setGeometry(TextObject() \
        .setString(["View","# 2"]) \
        .setFontStyle(FontStyleObject() \
         .setUSE("CenterJustify") \
        ) \
       ) \
       .setAppearance(AppearanceObject() \
        .setMaterial(MaterialObject() \
         .setDiffuseColor([0,1,0]) \
        ) \
       ) \
      ) \
     ) \
     .addChildren(TransformObject() \
      .setDEF("Text3") \
      .setTranslation([2,0,0]) \
      .addChildren(ShapeObject() \
       .setGeometry(TextObject() \
        .setString(["View","# 3"]) \
        .setFontStyle(FontStyleObject() \
         .setUSE("CenterJustify") \
        ) \
       ) \
       .setAppearance(AppearanceObject() \
        .setMaterial(MaterialObject() \
         .setDiffuseColor([0,0,1]) \
        ) \
       ) \
      ) \
     ) \
     .addChildren(TransformObject() \
      .setDEF("Text4") \
      .setTranslation([6,0,0]) \
      .addChildren(ShapeObject() \
       .setGeometry(TextObject() \
        .setString(["View","# 4"]) \
        .setFontStyle(FontStyleObject() \
         .setUSE("CenterJustify") \
        ) \
       ) \
       .setAppearance(AppearanceObject() \
        .setMaterial(MaterialObject() \
        ) \
       ) \
      ) \
     ) \
    ) \
#The following advanced animation sequence uses nodes covered in Chapters 7, 8 and 9.
#It does not need to be studied in this chapter.
    .addChildren(TransformObject() \
     .setTranslation([0,-3,8]) \
#notice this next Viewpoint has been transformed with the text, so its position is relative. it is called view5 in the Script.
     .addChildren(ViewpointObject() \
      .setDEF("ClickToAnimateView") \
      .setDescription("Select animation sequence") \
      .setPosition([0,0,7]) \
     ) \
     .addChildren(ShapeObject() \
      .setGeometry(TextObject() \
       .setString(["Click here to animate"]) \
       .setFontStyle(FontStyleObject(justify = ["MIDDLE","BEGIN"]) \
       ) \
      ) \
      .setAppearance(AppearanceObject() \
       .setMaterial(MaterialObject() \
        .setDiffuseColor([0.8,0.4,0]) \
       ) \
      ) \
     ) \
     .addChildren(ShapeObject() \
      .setGeometry(BoxObject(size = [7,1,0.02]) \
      ) \
      .setAppearance(AppearanceObject() \
       .setMaterial(MaterialObject() \
        .setTransparency(1) \
       ) \
      ) \
     ) \
     .addChildren(TouchSensorObject() \
      .setDEF("TextTouchSensor") \
      .setDescription("Click to begin animating viewpoint selections") \
     ) \
     .addChildren(TimeSensorObject() \
      .setDEF("Clock") \
      .setCycleInterval(10) \
     ) \
     .addChildren(ROUTEObject() \
      .setFromField("touchTime") \
      .setFromNode("TextTouchSensor") \
      .setToField("set_startTime") \
      .setToNode("Clock") \
     ) \
     .addChildren(IntegerSequencerObject() \
      .setDEF("TimingSequencer") \
      .setKey([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,1]) \
      .setKeyValue([0,1,2,3,4,5,6,7,8,10]) \
     ) \
     .addChildren(ROUTEObject() \
      .setFromField("fraction_changed") \
      .setFromNode("Clock") \
      .setToField("set_fraction") \
      .setToNode("TimingSequencer") \
     ) \
     .addChildren(ScriptObject() \
      .setDEF("BindingSequencerEngine") \
      .addField(fieldObject() \
       .setName("set_timeEvent") \
       .setAccessType("inputOnly") \
       .setType("SFInt32") \
      ) \
      .addField(fieldObject() \
       .setName("bindView1") \
       .setAccessType("outputOnly") \
       .setType("SFBool") \
      ) \
      .addField(fieldObject() \
       .setName("bindView2") \
       .setAccessType("outputOnly") \
       .setType("SFBool") \
      ) \
      .addField(fieldObject() \
       .setName("bindView3") \
       .setAccessType("outputOnly") \
       .setType("SFBool") \
      ) \
      .addField(fieldObject() \
       .setName("bindView4") \
       .setAccessType("outputOnly") \
       .setType("SFBool") \
      ) \
      .addField(fieldObject() \
       .setName("bindView5") \
       .setAccessType("outputOnly") \
       .setType("SFBool") \
      ) \
      .addField(fieldObject() \
       .setName("view1Bound") \
       .setAccessType("inputOnly") \
       .setType("SFBool") \
      ) \
      .addField(fieldObject() \
       .setName("view2Bound") \
       .setAccessType("inputOnly") \
       .setType("SFBool") \
      ) \
      .addField(fieldObject() \
       .setName("view3Bound") \
       .setAccessType("inputOnly") \
       .setType("SFBool") \
      ) \
      .addField(fieldObject() \
       .setName("view4Bound") \
       .setAccessType("inputOnly") \
       .setType("SFBool") \
      ) \
      .addField(fieldObject() \
       .setName("priorInputvalue") \
       .setAccessType("initializeOnly") \
       .setType("SFInt32") \
       .setValue("-1") \
      ) \
.setSourceCode('''ecmascript:\n"+
"\n"+
"function initialize ()\n"+
"{\n"+
"    bindView5 = true;\n"+
"    Browser.print ('Timing script initialized and ready for activation');\n"+
"}\n"+
"function set_timeEvent (inputValue)\n"+
"{\n"+
"    if (inputValue == priorInputvalue)\n"+
"    {\n"+
"        return; // ignore repeated inputs\n"+
"    }\n"+
"    // new value provided\n"+
"    priorInputvalue = inputValue;\n"+
"    // Browser.print ('\\ntimeEvent inputValue=' + inputValue);\n"+
"\n"+
"    // mimics user execution of Figure 4.1 steps t_0 through t_8\n"+
"    if (inputValue == 0)\n"+
"    {\n"+
"        Browser.print ('\\n===========\\n time t0');\n"+
"        bindView1 = true;\n"+
"    }\n"+
"    else if (inputValue == 1)\n"+
"    {\n"+
"        Browser.print ('\\n===========\\n time t1');\n"+
"        bindView2 = true;\n"+
"    }\n"+
"    else if (inputValue == 2)\n"+
"    {\n"+
"        Browser.print ('\\n===========\\n time t2');\n"+
"        bindView3 = true;\n"+
"    }\n"+
"    else if (inputValue == 3)\n"+
"    {\n"+
"        Browser.print ('\\n===========\\n time t3');\n"+
"        bindView3 = false;\n"+
"    }\n"+
"    else if (inputValue == 4)\n"+
"    {\n"+
"        Browser.print ('\\n===========\\n time t4');\n"+
"        bindView1 = true;\n"+
"    }\n"+
"    else if (inputValue == 5)\n"+
"    {\n"+
"        Browser.print ('\\n===========\\n time t5');\n"+
"        bindView2 = false;\n"+
"    }\n"+
"    else if (inputValue == 6)\n"+
"    {\n"+
"        Browser.print ('\\n===========\\n time t6');\n"+
"        bindView1 = false;\n"+
"    }\n"+
"    else if (inputValue == 7)\n"+
"    {\n"+
"        Browser.print ('\\n===========\\n time t7');\n"+
"        bindView4 = true;\n"+
"\n"+
"    }\n"+
"    else if (inputValue == 8)\n"+
"    {\n"+
"        Browser.print ('\\n===========\\n time t8');\n"+
"        Browser.print (', no action, all done');\n"+
"        Browser.print ('\\n\\n');\n"+
"    }\n"+
"}\n"+
"\n"+
"function view1Bound (inputValue)\n"+
"{\n"+
"    Browser.print (', view1Bound ' + (inputValue));\n"+
"    if (priorInputvalue == -1) Browser.print ('\\n');\n"+
"}\n"+
"function view2Bound (inputValue)\n"+
"{\n"+
"    Browser.print (', view2Bound ' + (inputValue));\n"+
"}\n"+
"function view3Bound (inputValue)\n"+
"{\n"+
"    Browser.print (', view3Bound ' + (inputValue));\n"+
"}\n"+
"function view4Bound (inputValue)\n"+
"{\n"+
"    Browser.print (', view4Bound ' + (inputValue));\n"+
"}\n"+
"function view5Bound (inputValue)\n"+
"{\n"+
"    Browser.print (', view5Bound ' + (inputValue));\n"+
"}''')
     ) \
#drive Script with TimeSensor clock
     .addChildren(ROUTEObject() \
      .setFromField("value_changed") \
      .setFromNode("TimingSequencer") \
      .setToField("set_timeEvent") \
      .setToNode("BindingSequencerEngine") \
     ) \
#Script will bind and unbind Viewpoint nodes
     .addChildren(ROUTEObject() \
      .setFromField("bindView1") \
      .setFromNode("BindingSequencerEngine") \
      .setToField("set_bind") \
      .setToNode("View1") \
     ) \
     .addChildren(ROUTEObject() \
      .setFromField("bindView2") \
      .setFromNode("BindingSequencerEngine") \
      .setToField("set_bind") \
      .setToNode("View2") \
     ) \
     .addChildren(ROUTEObject() \
      .setFromField("bindView3") \
      .setFromNode("BindingSequencerEngine") \
      .setToField("set_bind") \
      .setToNode("View3") \
     ) \
     .addChildren(ROUTEObject() \
      .setFromField("bindView4") \
      .setFromNode("BindingSequencerEngine") \
      .setToField("set_bind") \
      .setToNode("View4") \
     ) \
     .addChildren(ROUTEObject() \
      .setFromField("bindView5") \
      .setFromNode("BindingSequencerEngine") \
      .setToField("set_bind") \
      .setToNode("ClickToAnimateView") \
     ) \
#Viewpoint nodes report bind and unbind events
     .addChildren(ROUTEObject() \
      .setFromField("isBound") \
      .setFromNode("View1") \
      .setToField("view1Bound") \
      .setToNode("BindingSequencerEngine") \
     ) \
     .addChildren(ROUTEObject() \
      .setFromField("isBound") \
      .setFromNode("View2") \
      .setToField("view2Bound") \
      .setToNode("BindingSequencerEngine") \
     ) \
     .addChildren(ROUTEObject() \
      .setFromField("isBound") \
      .setFromNode("View3") \
      .setToField("view3Bound") \
      .setToNode("BindingSequencerEngine") \
     ) \
     .addChildren(ROUTEObject() \
      .setFromField("isBound") \
      .setFromNode("View4") \
      .setToField("view4Bound") \
      .setToNode("BindingSequencerEngine") \
     ) \
    ) \
   ) \

X3D0.toFileX3D("./future/./BindingOperations.newf.x3d")
