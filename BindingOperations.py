import x3dpsail
X3D0 = x3dpsail.X3D()
X3D0.setProfile("Immersive")
X3D0.setVersion("3.3")
head1 = x3dpsail.head()
meta2 = x3dpsail.meta()
meta2.setName("title")
meta2.setContent("BindingOperations.x3d")

head1.addMeta(meta2)
meta3 = x3dpsail.meta()
meta3.setName("description")
meta3.setContent("Illustrate Viewpoint binding operations (in gory detail!) as described in Chapter 4 concepts. Scene design: a TimeSensor clock drives and IntegerSequencer for each t0/t1/etc. event, and a customized Script node sends bind/unbind events to the correct Viewpoint. Display the browser console to see occurrence of each event.")

head1.addMeta(meta3)
meta4 = x3dpsail.meta()
meta4.setName("creator")
meta4.setContent("Don Brutzman")

head1.addMeta(meta4)
meta5 = x3dpsail.meta()
meta5.setName("created")
meta5.setContent("5 January 2008")

head1.addMeta(meta5)
meta6 = x3dpsail.meta()
meta6.setName("modified")
meta6.setContent("22 July 2013")

head1.addMeta(meta6)
meta7 = x3dpsail.meta()
meta7.setName("reference")
meta7.setContent("BindingOperations.console.txt")

head1.addMeta(meta7)
meta8 = x3dpsail.meta()
meta8.setName("reference")
meta8.setContent("BindingStackOperations.png")

head1.addMeta(meta8)
meta9 = x3dpsail.meta()
meta9.setName("reference")
meta9.setContent("X3D for Web Authors, Section 2.5.1, Figure 4.1")

head1.addMeta(meta9)
meta10 = x3dpsail.meta()
meta10.setName("reference")
meta10.setContent("http://X3dGraphics.com")

head1.addMeta(meta10)
meta11 = x3dpsail.meta()
meta11.setName("reference")
meta11.setContent("http://www.web3d.org/x3d/content/examples/X3dResources.html")

head1.addMeta(meta11)
meta12 = x3dpsail.meta()
meta12.setName("rights")
meta12.setContent("Copyright Don Brutzman and Leonard Daly 2007")

head1.addMeta(meta12)
meta13 = x3dpsail.meta()
meta13.setName("subject")
meta13.setContent("X3D book, X3D graphics, X3D-Edit, http://www.x3dGraphics.com")

head1.addMeta(meta13)
meta14 = x3dpsail.meta()
meta14.setName("identifier")
meta14.setContent("http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter04ViewingNavigation/BindingOperations.x3d")

head1.addMeta(meta14)
meta15 = x3dpsail.meta()
meta15.setName("generator")
meta15.setContent("X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit")

head1.addMeta(meta15)
meta16 = x3dpsail.meta()
meta16.setName("license")
meta16.setContent("../license.html")

head1.addMeta(meta16)

X3D0.setHead(head1)
Scene17 = x3dpsail.Scene()
Viewpoint18 = x3dpsail.Viewpoint()
Viewpoint18.setDEF("View1")
Viewpoint18.setCenterOfRotation([-6,0,0])
Viewpoint18.setDescription("Viewpoint 1")
Viewpoint18.setPosition([-6,0,5])

Scene17.addChildren(Viewpoint18)
Viewpoint19 = x3dpsail.Viewpoint()
Viewpoint19.setDEF("View2")
Viewpoint19.setCenterOfRotation([-2,0,0])
Viewpoint19.setDescription("Viewpoint 2")
Viewpoint19.setPosition([-2,0,5])

Scene17.addChildren(Viewpoint19)
Viewpoint20 = x3dpsail.Viewpoint()
Viewpoint20.setDEF("View3")
Viewpoint20.setCenterOfRotation([2,0,0])
Viewpoint20.setDescription("Viewpoint 3")
Viewpoint20.setPosition([2,0,5])

Scene17.addChildren(Viewpoint20)
Viewpoint21 = x3dpsail.Viewpoint()
Viewpoint21.setDEF("View4")
Viewpoint21.setCenterOfRotation([6,0,0])
Viewpoint21.setDescription("Viewpoint 4")
Viewpoint21.setPosition([6,0,5])

Scene17.addChildren(Viewpoint21)
#Script initialization ought to first bind view5 below.
Group22 = x3dpsail.Group()
Transform23 = x3dpsail.Transform()
Transform23.setDEF("Text1")
Transform23.setTranslation([-6,0,0])
Shape24 = x3dpsail.Shape()
Text25 = x3dpsail.Text()
Text25.setString(["View","# 1"])
FontStyle26 = x3dpsail.FontStyle()
FontStyle26.setDEF("CenterJustify")
FontStyle26.setJustify(["MIDDLE","MIDDLE"])

Text25.setFontStyle(FontStyle26)

Shape24.setGeometry(Text25)
Appearance27 = x3dpsail.Appearance()
Material28 = x3dpsail.Material()
Material28.setDiffuseColor([1,0,0])

Appearance27.setMaterial(Material28)

Shape24.setAppearance(Appearance27)

Transform23.addChildren(Shape24)

Group22.addChildren(Transform23)
Transform29 = x3dpsail.Transform()
Transform29.setDEF("Text2")
Transform29.setTranslation([-2,0,0])
Shape30 = x3dpsail.Shape()
Text31 = x3dpsail.Text()
Text31.setString(["View","# 2"])
FontStyle32 = x3dpsail.FontStyle()
FontStyle32.setUSE("CenterJustify")

Text31.setFontStyle(FontStyle32)

Shape30.setGeometry(Text31)
Appearance33 = x3dpsail.Appearance()
Material34 = x3dpsail.Material()
Material34.setDiffuseColor([0,1,0])

Appearance33.setMaterial(Material34)

Shape30.setAppearance(Appearance33)

Transform29.addChildren(Shape30)

Group22.addChildren(Transform29)
Transform35 = x3dpsail.Transform()
Transform35.setDEF("Text3")
Transform35.setTranslation([2,0,0])
Shape36 = x3dpsail.Shape()
Text37 = x3dpsail.Text()
Text37.setString(["View","# 3"])
FontStyle38 = x3dpsail.FontStyle()
FontStyle38.setUSE("CenterJustify")

Text37.setFontStyle(FontStyle38)

Shape36.setGeometry(Text37)
Appearance39 = x3dpsail.Appearance()
Material40 = x3dpsail.Material()
Material40.setDiffuseColor([0,0,1])

Appearance39.setMaterial(Material40)

Shape36.setAppearance(Appearance39)

Transform35.addChildren(Shape36)

Group22.addChildren(Transform35)
Transform41 = x3dpsail.Transform()
Transform41.setDEF("Text4")
Transform41.setTranslation([6,0,0])
Shape42 = x3dpsail.Shape()
Text43 = x3dpsail.Text()
Text43.setString(["View","# 4"])
FontStyle44 = x3dpsail.FontStyle()
FontStyle44.setUSE("CenterJustify")

Text43.setFontStyle(FontStyle44)

Shape42.setGeometry(Text43)
Appearance45 = x3dpsail.Appearance()
Material46 = x3dpsail.Material()

Appearance45.setMaterial(Material46)

Shape42.setAppearance(Appearance45)

Transform41.addChildren(Shape42)

Group22.addChildren(Transform41)

Scene17.addChildren(Group22)
#The following advanced animation sequence uses nodes covered in Chapters 7, 8 and 9.
#It does not need to be studied in this chapter.
Transform47 = x3dpsail.Transform()
Transform47.setTranslation([0,-3,8])
#notice this next Viewpoint has been transformed with the text, so its position is relative. it is called view5 in the Script.
Viewpoint48 = x3dpsail.Viewpoint()
Viewpoint48.setDEF("ClickToAnimateView")
Viewpoint48.setDescription("Select animation sequence")
Viewpoint48.setPosition([0,0,7])

Transform47.addChildren(Viewpoint48)
Shape49 = x3dpsail.Shape()
Text50 = x3dpsail.Text()
Text50.setString(["Click here to animate"])
FontStyle51 = x3dpsail.FontStyle()
FontStyle51.setJustify(["MIDDLE","BEGIN"])

Text50.setFontStyle(FontStyle51)

Shape49.setGeometry(Text50)
Appearance52 = x3dpsail.Appearance()
Material53 = x3dpsail.Material()
Material53.setDiffuseColor([0.8,0.4,0])

Appearance52.setMaterial(Material53)

Shape49.setAppearance(Appearance52)

Transform47.addChildren(Shape49)
Shape54 = x3dpsail.Shape()
Box55 = x3dpsail.Box()
Box55.setSize([7,1,0.02])

Shape54.setGeometry(Box55)
Appearance56 = x3dpsail.Appearance()
Material57 = x3dpsail.Material()
Material57.setTransparency(1)

Appearance56.setMaterial(Material57)

Shape54.setAppearance(Appearance56)

Transform47.addChildren(Shape54)
TouchSensor58 = x3dpsail.TouchSensor()
TouchSensor58.setDEF("TextTouchSensor")
TouchSensor58.setDescription("Click to begin animating viewpoint selections")

Transform47.addChildren(TouchSensor58)
TimeSensor59 = x3dpsail.TimeSensor()
TimeSensor59.setDEF("Clock")
TimeSensor59.setCycleInterval(10)

Transform47.addChildren(TimeSensor59)
ROUTE60 = x3dpsail.ROUTE()
ROUTE60.setFromField("touchTime")
ROUTE60.setFromNode("TextTouchSensor")
ROUTE60.setToField("set_startTime")
ROUTE60.setToNode("Clock")

Transform47.addChildren(ROUTE60)
IntegerSequencer61 = x3dpsail.IntegerSequencer()
IntegerSequencer61.setDEF("TimingSequencer")
IntegerSequencer61.setKey([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,1])
IntegerSequencer61.setKeyValue([0,1,2,3,4,5,6,7,8,10])

Transform47.addChildren(IntegerSequencer61)
ROUTE62 = x3dpsail.ROUTE()
ROUTE62.setFromField("fraction_changed")
ROUTE62.setFromNode("Clock")
ROUTE62.setToField("set_fraction")
ROUTE62.setToNode("TimingSequencer")

Transform47.addChildren(ROUTE62)
Script63 = x3dpsail.Script()
Script63.setDEF("BindingSequencerEngine")
field64 = x3dpsail.field()
field64.setName("set_timeEvent")
field64.setAccessType("inputOnly")
field64.setType("SFInt32")

Script63.addField(field64)
field65 = x3dpsail.field()
field65.setName("bindView1")
field65.setAccessType("outputOnly")
field65.setType("SFBool")

Script63.addField(field65)
field66 = x3dpsail.field()
field66.setName("bindView2")
field66.setAccessType("outputOnly")
field66.setType("SFBool")

Script63.addField(field66)
field67 = x3dpsail.field()
field67.setName("bindView3")
field67.setAccessType("outputOnly")
field67.setType("SFBool")

Script63.addField(field67)
field68 = x3dpsail.field()
field68.setName("bindView4")
field68.setAccessType("outputOnly")
field68.setType("SFBool")

Script63.addField(field68)
field69 = x3dpsail.field()
field69.setName("bindView5")
field69.setAccessType("outputOnly")
field69.setType("SFBool")

Script63.addField(field69)
field70 = x3dpsail.field()
field70.setName("view1Bound")
field70.setAccessType("inputOnly")
field70.setType("SFBool")

Script63.addField(field70)
field71 = x3dpsail.field()
field71.setName("view2Bound")
field71.setAccessType("inputOnly")
field71.setType("SFBool")

Script63.addField(field71)
field72 = x3dpsail.field()
field72.setName("view3Bound")
field72.setAccessType("inputOnly")
field72.setType("SFBool")

Script63.addField(field72)
field73 = x3dpsail.field()
field73.setName("view4Bound")
field73.setAccessType("inputOnly")
field73.setType("SFBool")

Script63.addField(field73)
field74 = x3dpsail.field()
field74.setName("priorInputvalue")
field74.setAccessType("initializeOnly")
field74.setType("SFInt32")
field74.setValue("-1")

Script63.addField(field74)

Script63.setSourceCode('''ecmascript:\n"+
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

Transform47.addChildren(Script63)
#drive Script with TimeSensor clock
ROUTE75 = x3dpsail.ROUTE()
ROUTE75.setFromField("value_changed")
ROUTE75.setFromNode("TimingSequencer")
ROUTE75.setToField("set_timeEvent")
ROUTE75.setToNode("BindingSequencerEngine")

Transform47.addChildren(ROUTE75)
#Script will bind and unbind Viewpoint nodes
ROUTE76 = x3dpsail.ROUTE()
ROUTE76.setFromField("bindView1")
ROUTE76.setFromNode("BindingSequencerEngine")
ROUTE76.setToField("set_bind")
ROUTE76.setToNode("View1")

Transform47.addChildren(ROUTE76)
ROUTE77 = x3dpsail.ROUTE()
ROUTE77.setFromField("bindView2")
ROUTE77.setFromNode("BindingSequencerEngine")
ROUTE77.setToField("set_bind")
ROUTE77.setToNode("View2")

Transform47.addChildren(ROUTE77)
ROUTE78 = x3dpsail.ROUTE()
ROUTE78.setFromField("bindView3")
ROUTE78.setFromNode("BindingSequencerEngine")
ROUTE78.setToField("set_bind")
ROUTE78.setToNode("View3")

Transform47.addChildren(ROUTE78)
ROUTE79 = x3dpsail.ROUTE()
ROUTE79.setFromField("bindView4")
ROUTE79.setFromNode("BindingSequencerEngine")
ROUTE79.setToField("set_bind")
ROUTE79.setToNode("View4")

Transform47.addChildren(ROUTE79)
ROUTE80 = x3dpsail.ROUTE()
ROUTE80.setFromField("bindView5")
ROUTE80.setFromNode("BindingSequencerEngine")
ROUTE80.setToField("set_bind")
ROUTE80.setToNode("ClickToAnimateView")

Transform47.addChildren(ROUTE80)
#Viewpoint nodes report bind and unbind events
ROUTE81 = x3dpsail.ROUTE()
ROUTE81.setFromField("isBound")
ROUTE81.setFromNode("View1")
ROUTE81.setToField("view1Bound")
ROUTE81.setToNode("BindingSequencerEngine")

Transform47.addChildren(ROUTE81)
ROUTE82 = x3dpsail.ROUTE()
ROUTE82.setFromField("isBound")
ROUTE82.setFromNode("View2")
ROUTE82.setToField("view2Bound")
ROUTE82.setToNode("BindingSequencerEngine")

Transform47.addChildren(ROUTE82)
ROUTE83 = x3dpsail.ROUTE()
ROUTE83.setFromField("isBound")
ROUTE83.setFromNode("View3")
ROUTE83.setToField("view3Bound")
ROUTE83.setToNode("BindingSequencerEngine")

Transform47.addChildren(ROUTE83)
ROUTE84 = x3dpsail.ROUTE()
ROUTE84.setFromField("isBound")
ROUTE84.setFromNode("View4")
ROUTE84.setToField("view4Bound")
ROUTE84.setToNode("BindingSequencerEngine")

Transform47.addChildren(ROUTE84)

Scene17.addChildren(Transform47)

X3D0.setScene(Scene17)
X3D0.toFileX3D("././BindingOperations_RoundTrip.x3d")
