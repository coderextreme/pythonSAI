import x3dpsail


X3D0 = (x3dpsail.X3D().setProfile(x3dpsail.SFString("Immersive")).setVersion(x3dpsail.SFString("3.3"))
      .setHead(x3dpsail.head()
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("title")).setContent(x3dpsail.SFString("BindingOperations.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("description")).setContent(x3dpsail.SFString("Illustrate Viewpoint binding operations (in gory detail!) as described in Chapter 4 concepts. Scene design: a TimeSensor clock drives and IntegerSequencer for each t0/t1/etc. event, and a customized Script node sends bind/unbind events to the correct Viewpoint. Display the browser console to see occurrence of each event.")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("creator")).setContent(x3dpsail.SFString("Don Brutzman")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("created")).setContent(x3dpsail.SFString("5 January 2008")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("modified")).setContent(x3dpsail.SFString("22 July 2013")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("reference")).setContent(x3dpsail.SFString("BindingOperations.console.txt")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("reference")).setContent(x3dpsail.SFString("BindingStackOperations.png")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("reference")).setContent(x3dpsail.SFString("X3D for Web Authors, Section 2.5.1, Figure 4.1")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("reference")).setContent(x3dpsail.SFString("http://X3dGraphics.com")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("reference")).setContent(x3dpsail.SFString("http://www.web3d.org/x3d/content/examples/X3dResources.html")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("rights")).setContent(x3dpsail.SFString("Copyright Don Brutzman and Leonard Daly 2007")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("subject")).setContent(x3dpsail.SFString("X3D book, X3D graphics, X3D-Edit, http://www.x3dGraphics.com")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("identifier")).setContent(x3dpsail.SFString("http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter04ViewingNavigation/BindingOperations.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("generator")).setContent(x3dpsail.SFString("X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("license")).setContent(x3dpsail.SFString("../license.html"))))
      .setScene(x3dpsail.Scene()
        .addChild(x3dpsail.Viewpoint().setDEF(x3dpsail.SFString("View1")).setCenterOfRotation(x3dpsail.SFVec3f(-6,0,0)).setDescription(x3dpsail.SFString("Viewpoint 1")).setPosition(x3dpsail.SFVec3f(-6,0,5)))
        .addChild(x3dpsail.Viewpoint().setDEF(x3dpsail.SFString("View2")).setCenterOfRotation(x3dpsail.SFVec3f(-2,0,0)).setDescription(x3dpsail.SFString("Viewpoint 2")).setPosition(x3dpsail.SFVec3f(-2,0,5)))
        .addChild(x3dpsail.Viewpoint().setDEF(x3dpsail.SFString("View3")).setCenterOfRotation(x3dpsail.SFVec3f(2,0,0)).setDescription(x3dpsail.SFString("Viewpoint 3")).setPosition(x3dpsail.SFVec3f(2,0,5)))
        .addChild(x3dpsail.Viewpoint().setDEF(x3dpsail.SFString("View4")).setCenterOfRotation(x3dpsail.SFVec3f(6,0,0)).setDescription(x3dpsail.SFString("Viewpoint 4")).setPosition(x3dpsail.SFVec3f(6,0,5)))
        #Script initialization ought to first bind view5 below.

        .addChild(x3dpsail.Group()
          .addChild(x3dpsail.Transform().setDEF(x3dpsail.SFString("Text1")).setTranslation(x3dpsail.SFVec3f(-6,0,0))
            .addChild(x3dpsail.Shape()
              .setGeometry(x3dpsail.Text().setString(x3dpsail.MFString(["View","# 1"]))
                .setFontStyle(x3dpsail.FontStyle().setDEF(x3dpsail.SFString("CenterJustify")).setJustify(x3dpsail.MFString(["MIDDLE","MIDDLE"]))))
              .setAppearance(x3dpsail.Appearance()
                .setMaterial(x3dpsail.Material().setDiffuseColor(x3dpsail.SFColor(1,0,0))))))
          .addChild(x3dpsail.Transform().setDEF(x3dpsail.SFString("Text2")).setTranslation(x3dpsail.SFVec3f(-2,0,0))
            .addChild(x3dpsail.Shape()
              .setGeometry(x3dpsail.Text().setString(x3dpsail.MFString(["View","# 2"]))
                .setFontStyle(x3dpsail.FontStyle().setUSE(x3dpsail.SFString("CenterJustify"))))
              .setAppearance(x3dpsail.Appearance()
                .setMaterial(x3dpsail.Material().setDiffuseColor(x3dpsail.SFColor(0,1,0))))))
          .addChild(x3dpsail.Transform().setDEF(x3dpsail.SFString("Text3")).setTranslation(x3dpsail.SFVec3f(2,0,0))
            .addChild(x3dpsail.Shape()
              .setGeometry(x3dpsail.Text().setString(x3dpsail.MFString(["View","# 3"]))
                .setFontStyle(x3dpsail.FontStyle().setUSE(x3dpsail.SFString("CenterJustify"))))
              .setAppearance(x3dpsail.Appearance()
                .setMaterial(x3dpsail.Material().setDiffuseColor(x3dpsail.SFColor(0,0,1))))))
          .addChild(x3dpsail.Transform().setDEF(x3dpsail.SFString("Text4")).setTranslation(x3dpsail.SFVec3f(6,0,0))
            .addChild(x3dpsail.Shape()
              .setGeometry(x3dpsail.Text().setString(x3dpsail.MFString(["View","# 4"]))
                .setFontStyle(x3dpsail.FontStyle().setUSE(x3dpsail.SFString("CenterJustify"))))
              .setAppearance(x3dpsail.Appearance()
                .setMaterial(x3dpsail.Material())))))
        #The following advanced animation sequence uses nodes covered in Chapters 7, 8 and 9.

        #It does not need to be studied in this chapter.

        .addChild(x3dpsail.Transform().setTranslation(x3dpsail.SFVec3f(0,-3,8))
          #notice this next Viewpoint has been transformed with the text, so its position is relative. it is called view5 in the Script.

          .addChild(x3dpsail.Viewpoint().setDEF(x3dpsail.SFString("ClickToAnimateView")).setDescription(x3dpsail.SFString("Select animation sequence")).setPosition(x3dpsail.SFVec3f(0,0,7)))
          .addChild(x3dpsail.Shape()
            .setGeometry(x3dpsail.Text().setString(x3dpsail.MFString(["Click here to animate"]))
              .setFontStyle(x3dpsail.FontStyle().setJustify(x3dpsail.MFString(["MIDDLE","BEGIN"]))))
            .setAppearance(x3dpsail.Appearance()
              .setMaterial(x3dpsail.Material().setDiffuseColor(x3dpsail.SFColor(0.8,0.4,0)))))
          .addChild(x3dpsail.Shape()
            .setGeometry(x3dpsail.Box().setSize(x3dpsail.SFVec3f(7,1,0.02)))
            .setAppearance(x3dpsail.Appearance()
              .setMaterial(x3dpsail.Material().setTransparency(x3dpsail.SFFloat(1)))))
          .addChild(x3dpsail.TouchSensor().setDEF(x3dpsail.SFString("TextTouchSensor")).setDescription(x3dpsail.SFString("Click to begin animating viewpoint selections")))
          .addChild(x3dpsail.TimeSensor().setDEF(x3dpsail.SFString("Clock")).setCycleInterval(x3dpsail.SFTime(10)))
          .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("touchTime")).setFromNode(x3dpsail.SFString("TextTouchSensor")).setToField(x3dpsail.SFString("set_startTime")).setToNode(x3dpsail.SFString("Clock")))
          .addChild(x3dpsail.IntegerSequencer().setDEF(x3dpsail.SFString("TimingSequencer")).setKey(x3dpsail.MFFloat([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,1])).setKeyValue(x3dpsail.MFInt32([0,1,2,3,4,5,6,7,8,10])))
          .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("fraction_changed")).setFromNode(x3dpsail.SFString("Clock")).setToField(x3dpsail.SFString("set_fraction")).setToNode(x3dpsail.SFString("TimingSequencer")))
          .addChild(x3dpsail.Script().setDEF(x3dpsail.SFString("BindingSequencerEngine"))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("set_timeEvent")).setAccessType(x3dpsail.SFString("inputOnly")).setType(x3dpsail.SFString("SFInt32")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("bindView1")).setAccessType(x3dpsail.SFString("outputOnly")).setType(x3dpsail.SFString("SFBool")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("bindView2")).setAccessType(x3dpsail.SFString("outputOnly")).setType(x3dpsail.SFString("SFBool")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("bindView3")).setAccessType(x3dpsail.SFString("outputOnly")).setType(x3dpsail.SFString("SFBool")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("bindView4")).setAccessType(x3dpsail.SFString("outputOnly")).setType(x3dpsail.SFString("SFBool")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("bindView5")).setAccessType(x3dpsail.SFString("outputOnly")).setType(x3dpsail.SFString("SFBool")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("view1Bound")).setAccessType(x3dpsail.SFString("inputOnly")).setType(x3dpsail.SFString("SFBool")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("view2Bound")).setAccessType(x3dpsail.SFString("inputOnly")).setType(x3dpsail.SFString("SFBool")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("view3Bound")).setAccessType(x3dpsail.SFString("inputOnly")).setType(x3dpsail.SFString("SFBool")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("view4Bound")).setAccessType(x3dpsail.SFString("inputOnly")).setType(x3dpsail.SFString("SFBool")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("priorInputvalue")).setAccessType(x3dpsail.SFString("initializeOnly")).setType(x3dpsail.SFString("SFInt32")).setValue(x3dpsail.SFString("-1"))).setSourceCode('''ecmascript:\n"+
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
)
          #drive Script with TimeSensor clock

          .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("value_changed")).setFromNode(x3dpsail.SFString("TimingSequencer")).setToField(x3dpsail.SFString("set_timeEvent")).setToNode(x3dpsail.SFString("BindingSequencerEngine")))
          #Script will bind and unbind Viewpoint nodes

          .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("bindView1")).setFromNode(x3dpsail.SFString("BindingSequencerEngine")).setToField(x3dpsail.SFString("set_bind")).setToNode(x3dpsail.SFString("View1")))
          .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("bindView2")).setFromNode(x3dpsail.SFString("BindingSequencerEngine")).setToField(x3dpsail.SFString("set_bind")).setToNode(x3dpsail.SFString("View2")))
          .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("bindView3")).setFromNode(x3dpsail.SFString("BindingSequencerEngine")).setToField(x3dpsail.SFString("set_bind")).setToNode(x3dpsail.SFString("View3")))
          .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("bindView4")).setFromNode(x3dpsail.SFString("BindingSequencerEngine")).setToField(x3dpsail.SFString("set_bind")).setToNode(x3dpsail.SFString("View4")))
          .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("bindView5")).setFromNode(x3dpsail.SFString("BindingSequencerEngine")).setToField(x3dpsail.SFString("set_bind")).setToNode(x3dpsail.SFString("ClickToAnimateView")))
          #Viewpoint nodes report bind and unbind events

          .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("isBound")).setFromNode(x3dpsail.SFString("View1")).setToField(x3dpsail.SFString("view1Bound")).setToNode(x3dpsail.SFString("BindingSequencerEngine")))
          .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("isBound")).setFromNode(x3dpsail.SFString("View2")).setToField(x3dpsail.SFString("view2Bound")).setToNode(x3dpsail.SFString("BindingSequencerEngine")))
          .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("isBound")).setFromNode(x3dpsail.SFString("View3")).setToField(x3dpsail.SFString("view3Bound")).setToNode(x3dpsail.SFString("BindingSequencerEngine")))
          .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("isBound")).setFromNode(x3dpsail.SFString("View4")).setToField(x3dpsail.SFString("view4Bound")).setToNode(x3dpsail.SFString("BindingSequencerEngine"))))))

X3D0.toFileX3D("./future/./BindingOperations_RoundTrip.x3d")
