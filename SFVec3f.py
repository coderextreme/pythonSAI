import x3dpsail as x3d
X3D0 = x3d.X3D()
X3D0.setProfile("Immersive")
X3D0.setVersion("3.3")
head1 = x3d.head()
meta2 = x3d.meta()
meta2.setName("title")
meta2.setContent("SFVec3f.x3d")

head1.addMeta(meta2)
meta3 = x3d.meta()
meta3.setName("creator")
meta3.setContent("John Carlson")

head1.addMeta(meta3)
meta4 = x3d.meta()
meta4.setName("description")
meta4.setContent("3 prismatic spheres")

head1.addMeta(meta4)
meta5 = x3d.meta()
meta5.setName("identifier")
meta5.setContent("https://coderextreme.net/X3DJSONLD/SFVec3f.x3d")

head1.addMeta(meta5)

X3D0.setHead(head1)
Scene6 = x3d.Scene()
NavigationInfo7 = x3d.NavigationInfo()
NavigationInfo7.setType(["EXAMINE","ANY"])

Scene6.addChildren(NavigationInfo7)
Transform8 = x3d.Transform()
Transform8.setDEF("transform")
Transform8.setTranslation([0,0,0])
Shape9 = x3d.Shape()
Appearance10 = x3d.Appearance()
Material11 = x3d.Material()
Material11.setDiffuseColor([.7,.7,.7])
Material11.setSpecularColor([.5,.5,.5])

Appearance10.setMaterial(Material11)

Shape9.setAppearance(Appearance10)
Sphere12 = x3d.Sphere()

Shape9.setGeometry(Sphere12)

Transform8.addChildren(Shape9)

Scene6.addChildren(Transform8)
Script13 = x3d.Script()
Script13.setDEF("Bounce")
field14 = x3d.field()
field14.setName("set_translation")
field14.setAccessType("inputOnly")
field14.setType("SFVec3f")
field14.setValue("0 0 0")

Script13.addField(field14)
field15 = x3d.field()
field15.setName("translation_changed")
field15.setAccessType("outputOnly")
field15.setType("SFVec3f")
field15.setValue("0 0 0")

Script13.addField(field15)
field16 = x3d.field()
field16.setName("translation")
field16.setAccessType("inputOutput")
field16.setType("SFVec3f")
field16.setValue("0 0 0")

Script13.addField(field16)
field17 = x3d.field()
field17.setName("velocity")
field17.setAccessType("inputOutput")
field17.setType("SFVec3f")
field17.setValue("0 0 0")

Script13.addField(field17)
field18 = x3d.field()
field18.setName("set_fraction")
field18.setAccessType("inputOnly")
field18.setType("SFTime")

Script13.addField(field18)

Script13.setSourceCode('''ecmascript:\n"+
"			function newBubble() {\n"+
"			    translation = new SFVec3f(0, 0, 0);\n"+
"			    velocity = new SFVec3f(\n"+
"			    	Math.random() - 0.5,\n"+
"				Math.random() - 0.5,\n"+
"				Math.random() - 0.5);\n"+
"			}\n"+
"			function set_fraction() {\n"+
"			    translation = new SFVec3f(\n"+
"			    	translation.x + velocity.x,\n"+
"				translation.y + velocity.y,\n"+
"				translation.z + velocity.z);\n"+
"				if (Math.abs(translation.x) > 10) {\n"+
"					newBubble();\n"+
"				} else if (Math.abs(translation.y) > 10) {\n"+
"					newBubble();\n"+
"				} else if (Math.abs(translation.z) > 10) {\n"+
"					newBubble();\n"+
"				} else {\n"+
"					velocity = new SFVec3f(\n"+
"						velocity.x + Math.random() * 0.2 - 0.1,\n"+
"						velocity.y + Math.random() * 0.2 - 0.1,\n"+
"						velocity.z + Math.random() * 0.2 - 0.1\n"+
"					);\n"+
"				}\n"+
"			}\n"+
"\n"+
"			function initialize() {\n"+
"			     newBubble();\n"+
"			}\n"+
"\n"+
"''')

Scene6.addChildren(Script13)
TimeSensor19 = x3d.TimeSensor()
TimeSensor19.setDEF("TourTime")
TimeSensor19.setCycleInterval(0.150)
TimeSensor19.setLoop(True)

Scene6.addChildren(TimeSensor19)
ROUTE20 = x3d.ROUTE()
ROUTE20.setFromNode("TourTime")
ROUTE20.setFromField("cycleTime")
ROUTE20.setToNode("Bounce")
ROUTE20.setToField("set_fraction")

Scene6.addChildren(ROUTE20)
ROUTE21 = x3d.ROUTE()
ROUTE21.setFromNode("Bounce")
ROUTE21.setFromField("translation_changed")
ROUTE21.setToNode("transform")
ROUTE21.setToField("set_translation")

Scene6.addChildren(ROUTE21)

X3D0.setScene(Scene6)
X3D0.toFileX3D("SFVec3f_RoundTrip.x3d")
