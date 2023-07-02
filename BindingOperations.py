print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"
head1 = x3d.head()
meta2 = x3d.meta()
meta2.name = "title"
meta2.content = "BindingOperations.x3d"

head1.children.append(meta2)
meta3 = x3d.meta()
meta3.name = "description"
meta3.content = "Illustrate Viewpoint binding operations (in gory detail!) as described in Chapter 4 concepts. Scene design: a TimeSensor clock drives and IntegerSequencer for each t0/t1/etc. event, and a customized Script node sends bind/unbind events to the correct Viewpoint. Display the browser console to see occurrence of each event."

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.name = "creator"
meta4.content = "Don Brutzman"

head1.children.append(meta4)
meta5 = x3d.meta()
meta5.name = "created"
meta5.content = "5 January 2008"

head1.children.append(meta5)
meta6 = x3d.meta()
meta6.name = "modified"
meta6.content = "22 July 2013"

head1.children.append(meta6)
meta7 = x3d.meta()
meta7.name = "reference"
meta7.content = "BindingOperations.console.txt"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.name = "reference"
meta8.content = "BindingStackOperations.png"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "reference"
meta9.content = "X3D for Web Authors, Section 2.5.1, Figure 4.1"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "reference"
meta10.content = "http://X3dGraphics.com"

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.name = "reference"
meta11.content = "https://www.web3d.org/x3d/content/examples/X3dResources.html"

head1.children.append(meta11)
meta12 = x3d.meta()
meta12.name = "rights"
meta12.content = "Copyright Don Brutzman and Leonard Daly 2007"

head1.children.append(meta12)
meta13 = x3d.meta()
meta13.name = "subject"
meta13.content = "X3D book, X3D graphics, X3D-Edit, http://www.x3dGraphics.com"

head1.children.append(meta13)
meta14 = x3d.meta()
meta14.name = "identifier"
meta14.content = "http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter04ViewingNavigation/BindingOperations.x3d"

head1.children.append(meta14)
meta15 = x3d.meta()
meta15.name = "generator"
meta15.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"

head1.children.append(meta15)
meta16 = x3d.meta()
meta16.name = "license"
meta16.content = "../license.html"

head1.children.append(meta16)

X3D0.head = head1
Scene17 = x3d.Scene()
Viewpoint18 = x3d.Viewpoint()
Viewpoint18.DEF = "View1"
Viewpoint18.centerOfRotation = [-6,0,0]
Viewpoint18.description = "Viewpoint 1"
Viewpoint18.position = [-6,0,5]

Scene17.children.append(Viewpoint18)
Viewpoint19 = x3d.Viewpoint()
Viewpoint19.DEF = "View2"
Viewpoint19.centerOfRotation = [-2,0,0]
Viewpoint19.description = "Viewpoint 2"
Viewpoint19.position = [-2,0,5]

Scene17.children.append(Viewpoint19)
Viewpoint20 = x3d.Viewpoint()
Viewpoint20.DEF = "View3"
Viewpoint20.centerOfRotation = [2,0,0]
Viewpoint20.description = "Viewpoint 3"
Viewpoint20.position = [2,0,5]

Scene17.children.append(Viewpoint20)
Viewpoint21 = x3d.Viewpoint()
Viewpoint21.DEF = "View4"
Viewpoint21.centerOfRotation = [6,0,0]
Viewpoint21.description = "Viewpoint 4"
Viewpoint21.position = [6,0,5]

Scene17.children.append(Viewpoint21)
#Script initialization ought to first bind view5 below.
Group22 = x3d.Group()
Transform23 = x3d.Transform()
Transform23.DEF = "Text1"
Transform23.translation = [-6,0,0]
Shape24 = x3d.Shape()
Text25 = x3d.Text()
Text25.string = ["View","# 1"]
FontStyle26 = x3d.FontStyle()
FontStyle26.DEF = "CenterJustify"
FontStyle26.justify = ["MIDDLE","MIDDLE"]

Text25.fontStyle = FontStyle26

Shape24.geometry = Text25
Appearance27 = x3d.Appearance()
Material28 = x3d.Material()
Material28.diffuseColor = [1,0,0]

Appearance27.material = Material28

Shape24.appearance = Appearance27

Transform23.children.append(Shape24)

Group22.children.append(Transform23)
Transform29 = x3d.Transform()
Transform29.DEF = "Text2"
Transform29.translation = [-2,0,0]
Shape30 = x3d.Shape()
Text31 = x3d.Text()
Text31.string = ["View","# 2"]
FontStyle32 = x3d.FontStyle()
FontStyle32.USE = "CenterJustify"

Text31.fontStyle = FontStyle32

Shape30.geometry = Text31
Appearance33 = x3d.Appearance()
Material34 = x3d.Material()
Material34.diffuseColor = [0,1,0]

Appearance33.material = Material34

Shape30.appearance = Appearance33

Transform29.children.append(Shape30)

Group22.children.append(Transform29)
Transform35 = x3d.Transform()
Transform35.DEF = "Text3"
Transform35.translation = [2,0,0]
Shape36 = x3d.Shape()
Text37 = x3d.Text()
Text37.string = ["View","# 3"]
FontStyle38 = x3d.FontStyle()
FontStyle38.USE = "CenterJustify"

Text37.fontStyle = FontStyle38

Shape36.geometry = Text37
Appearance39 = x3d.Appearance()
Material40 = x3d.Material()
Material40.diffuseColor = [0,0,1]

Appearance39.material = Material40

Shape36.appearance = Appearance39

Transform35.children.append(Shape36)

Group22.children.append(Transform35)
Transform41 = x3d.Transform()
Transform41.DEF = "Text4"
Transform41.translation = [6,0,0]
Shape42 = x3d.Shape()
Text43 = x3d.Text()
Text43.string = ["View","# 4"]
FontStyle44 = x3d.FontStyle()
FontStyle44.USE = "CenterJustify"

Text43.fontStyle = FontStyle44

Shape42.geometry = Text43
Appearance45 = x3d.Appearance()
Material46 = x3d.Material()

Appearance45.material = Material46

Shape42.appearance = Appearance45

Transform41.children.append(Shape42)

Group22.children.append(Transform41)

Scene17.children.append(Group22)
#The following advanced animation sequence uses nodes covered in Chapters 7, 8 and 9.
#It does not need to be studied in this chapter.
Transform47 = x3d.Transform()
Transform47.translation = [0,-3,8]
#notice this next Viewpoint has been transformed with the text, so its position is relative. it is called view5 in the Script.
Viewpoint48 = x3d.Viewpoint()
Viewpoint48.DEF = "ClickToAnimateView"
Viewpoint48.description = "Select animation sequence"
Viewpoint48.position = [0,0,7]

Transform47.children.append(Viewpoint48)
Shape49 = x3d.Shape()
Text50 = x3d.Text()
Text50.string = ["Click here to animate"]
FontStyle51 = x3d.FontStyle()
FontStyle51.justify = ["MIDDLE","BEGIN"]

Text50.fontStyle = FontStyle51

Shape49.geometry = Text50
Appearance52 = x3d.Appearance()
Material53 = x3d.Material()
Material53.diffuseColor = [0.8,0.4,0]

Appearance52.material = Material53

Shape49.appearance = Appearance52

Transform47.children.append(Shape49)
Shape54 = x3d.Shape()
Box55 = x3d.Box()
Box55.size = [7,1,0.02]

Shape54.geometry = Box55
Appearance56 = x3d.Appearance()
Material57 = x3d.Material()
Material57.transparency = 1

Appearance56.material = Material57

Shape54.appearance = Appearance56

Transform47.children.append(Shape54)
TouchSensor58 = x3d.TouchSensor()
TouchSensor58.DEF = "TextTouchSensor"
TouchSensor58.description = "Click to begin animating viewpoint selections"

Transform47.children.append(TouchSensor58)
TimeSensor59 = x3d.TimeSensor()
TimeSensor59.DEF = "Clock"
TimeSensor59.cycleInterval = 10

Transform47.children.append(TimeSensor59)
ROUTE60 = x3d.ROUTE()
ROUTE60.fromField = "touchTime"
ROUTE60.fromNode = "TextTouchSensor"
ROUTE60.toField = "set_startTime"
ROUTE60.toNode = "Clock"

Transform47.children.append(ROUTE60)
IntegerSequencer61 = x3d.IntegerSequencer()
IntegerSequencer61.DEF = "TimingSequencer"
IntegerSequencer61.key = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,1]
IntegerSequencer61.keyValue = [0,1,2,3,4,5,6,7,8,10]

Transform47.children.append(IntegerSequencer61)
ROUTE62 = x3d.ROUTE()
ROUTE62.fromField = "fraction_changed"
ROUTE62.fromNode = "Clock"
ROUTE62.toField = "set_fraction"
ROUTE62.toNode = "TimingSequencer"

Transform47.children.append(ROUTE62)
Script63 = x3d.Script()
Script63.DEF = "BindingSequencerEngine"
field64 = x3d.field()
field64.name = "set_timeEvent"
field64.accessType = "inputOnly"
field64.type = "SFInt32"

Script63.field.append(field64)
field65 = x3d.field()
field65.name = "bindView1"
field65.accessType = "outputOnly"
field65.type = "SFBool"

Script63.field.append(field65)
field66 = x3d.field()
field66.name = "bindView2"
field66.accessType = "outputOnly"
field66.type = "SFBool"

Script63.field.append(field66)
field67 = x3d.field()
field67.name = "bindView3"
field67.accessType = "outputOnly"
field67.type = "SFBool"

Script63.field.append(field67)
field68 = x3d.field()
field68.name = "bindView4"
field68.accessType = "outputOnly"
field68.type = "SFBool"

Script63.field.append(field68)
field69 = x3d.field()
field69.name = "bindView5"
field69.accessType = "outputOnly"
field69.type = "SFBool"

Script63.field.append(field69)
field70 = x3d.field()
field70.name = "view1Bound"
field70.accessType = "inputOnly"
field70.type = "SFBool"

Script63.field.append(field70)
field71 = x3d.field()
field71.name = "view2Bound"
field71.accessType = "inputOnly"
field71.type = "SFBool"

Script63.field.append(field71)
field72 = x3d.field()
field72.name = "view3Bound"
field72.accessType = "inputOnly"
field72.type = "SFBool"

Script63.field.append(field72)
field73 = x3d.field()
field73.name = "view4Bound"
field73.accessType = "inputOnly"
field73.type = "SFBool"

Script63.field.append(field73)
field74 = x3d.field()
field74.name = "priorInputvalue"
field74.accessType = "initializeOnly"
field74.type = "SFInt32"
field74.value = -1

Script63.field.append(field74)

Script63.sourceCode = '''ecmascript:\n"+
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
"}'''

Transform47.children.append(Script63)
#drive Script with TimeSensor clock
ROUTE75 = x3d.ROUTE()
ROUTE75.fromField = "value_changed"
ROUTE75.fromNode = "TimingSequencer"
ROUTE75.toField = "set_timeEvent"
ROUTE75.toNode = "BindingSequencerEngine"

Transform47.children.append(ROUTE75)
#Script will bind and unbind Viewpoint nodes
ROUTE76 = x3d.ROUTE()
ROUTE76.fromField = "bindView1"
ROUTE76.fromNode = "BindingSequencerEngine"
ROUTE76.toField = "set_bind"
ROUTE76.toNode = "View1"

Transform47.children.append(ROUTE76)
ROUTE77 = x3d.ROUTE()
ROUTE77.fromField = "bindView2"
ROUTE77.fromNode = "BindingSequencerEngine"
ROUTE77.toField = "set_bind"
ROUTE77.toNode = "View2"

Transform47.children.append(ROUTE77)
ROUTE78 = x3d.ROUTE()
ROUTE78.fromField = "bindView3"
ROUTE78.fromNode = "BindingSequencerEngine"
ROUTE78.toField = "set_bind"
ROUTE78.toNode = "View3"

Transform47.children.append(ROUTE78)
ROUTE79 = x3d.ROUTE()
ROUTE79.fromField = "bindView4"
ROUTE79.fromNode = "BindingSequencerEngine"
ROUTE79.toField = "set_bind"
ROUTE79.toNode = "View4"

Transform47.children.append(ROUTE79)
ROUTE80 = x3d.ROUTE()
ROUTE80.fromField = "bindView5"
ROUTE80.fromNode = "BindingSequencerEngine"
ROUTE80.toField = "set_bind"
ROUTE80.toNode = "ClickToAnimateView"

Transform47.children.append(ROUTE80)
#Viewpoint nodes report bind and unbind events
ROUTE81 = x3d.ROUTE()
ROUTE81.fromField = "isBound"
ROUTE81.fromNode = "View1"
ROUTE81.toField = "view1Bound"
ROUTE81.toNode = "BindingSequencerEngine"

Transform47.children.append(ROUTE81)
ROUTE82 = x3d.ROUTE()
ROUTE82.fromField = "isBound"
ROUTE82.fromNode = "View2"
ROUTE82.toField = "view2Bound"
ROUTE82.toNode = "BindingSequencerEngine"

Transform47.children.append(ROUTE82)
ROUTE83 = x3d.ROUTE()
ROUTE83.fromField = "isBound"
ROUTE83.fromNode = "View3"
ROUTE83.toField = "view3Bound"
ROUTE83.toNode = "BindingSequencerEngine"

Transform47.children.append(ROUTE83)
ROUTE84 = x3d.ROUTE()
ROUTE84.fromField = "isBound"
ROUTE84.fromNode = "View4"
ROUTE84.toField = "view4Bound"
ROUTE84.toNode = "BindingSequencerEngine"

Transform47.children.append(ROUTE84)

Scene17.children.append(Transform47)

X3D0.Scene = Scene17
f = open("././BindingOperations_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
