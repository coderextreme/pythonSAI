import x3dpsail as x3d
X3D0 = x3d.X3D()
X3D0.setProfile("Immersive")
X3D0.setVersion("3.3")
Scene1 = x3d.Scene()
NavigationInfo2 = x3d.NavigationInfo()

Scene1.addChildren(NavigationInfo2)
DirectionalLight3 = x3d.DirectionalLight()
DirectionalLight3.setDirection([0,-0.8,-0.2])
DirectionalLight3.setIntensity(0.5)

Scene1.addChildren(DirectionalLight3)
Background4 = x3d.Background()
Background4.setSkyColor([1,1,1])

Scene1.addChildren(Background4)
Viewpoint5 = x3d.Viewpoint()
Viewpoint5.setDescription("One mathematical orbital")
Viewpoint5.setPosition([0,0,50])

Scene1.addChildren(Viewpoint5)
Transform6 = x3d.Transform()
Transform6.setTranslation([0,-1,1])
Transform6.setRotation([0,1,0,3.1415926])
Transform6.setScale([1.5,1.5,1.5])
Shape7 = x3d.Shape()
Appearance8 = x3d.Appearance()
Material9 = x3d.Material()
Material9.setTransparency(0.1)
Material9.setDiffuseColor([0.9,0.3,0.3])
Material9.setSpecularColor([0.8,0.8,0.8])
Material9.setShininess(0.145)

Appearance8.setMaterial(Material9)

Shape7.setAppearance(Appearance8)
IndexedFaceSet10 = x3d.IndexedFaceSet()
IndexedFaceSet10.setCcw(False)
IndexedFaceSet10.setConvex(False)
IndexedFaceSet10.setCoordIndex([0,1,2,-1])
IndexedFaceSet10.setDEF("ifs")
Coordinate11 = x3d.Coordinate()
Coordinate11.setDEF("crd")
Coordinate11.setPoint([0,0,1,0,1,0,1,0,0])

IndexedFaceSet10.setCoord(Coordinate11)

Shape7.setGeometry(IndexedFaceSet10)

Transform6.addChildren(Shape7)

Scene1.addChildren(Transform6)
Script12 = x3d.Script()
Script12.setDEF("FlowerScript")
field13 = x3d.field()
field13.setName("set_fraction")
field13.setAccessType("inputOnly")
field13.setType("SFFloat")

Script12.addField(field13)
field14 = x3d.field()
field14.setName("coordinates")
field14.setAccessType("outputOnly")
field14.setType("MFVec3f")

Script12.addField(field14)
field15 = x3d.field()
field15.setName("coordIndexes")
field15.setAccessType("outputOnly")
field15.setType("MFInt32")

Script12.addField(field15)

Script12.setSourceCode('''ecmascript:\n"+
"\n"+
"var e = 5;\n"+
"var f = 5;\n"+
"var g = 5;\n"+
"var h = 5;\n"+
"var resolution = 150;\n"+
"var t = 0;\n"+
"var p = 0;\n"+
"\n"+
"function initialize() {\n"+
"     var localci = new Array();\n"+
"     var ci = 0;\n"+
"     var buf = [];\n"+
"     for (var i = 0; i < resolution-1; i++) {\n"+
"     	for (var j = 0; j < resolution-1; j++) {\n"+
"	     localci[ci] = i*resolution+j;\n"+
"	     localci[ci+1] = i*resolution+j+1;\n"+
"	     localci[ci+2] = (i+1)*resolution+j+1;\n"+
"	     localci[ci+3] = (i+1)*resolution+j;\n"+
"	     localci[ci+4] = -1;\n"+
"	     buf.push(localci[ci]);\n"+
"	     buf.push(localci[ci+1]);\n"+
"	     buf.push(localci[ci+3]);\n"+
"	     buf.push(localci[ci+4]);\n"+
"\n"+
"	     buf.push(localci[ci+1]);\n"+
"	     buf.push(localci[ci+2]);\n"+
"	     buf.push(localci[ci+3]);\n"+
"	     buf.push(localci[ci+4]);\n"+
"	     ci += 5;\n"+
"	}\n"+
"    }\n"+
"    updateCoordinates(resolution);\n"+
"    coordIndexes = new x3dom.fields.MFInt32(buf);\n"+
"}\n"+
"\n"+
"function updateCoordinates(resolution) {\n"+
"     theta = 0.0;\n"+
"     phi = 0.0;\n"+
"     delta = (2 * 3.141592653) / (resolution-1);\n"+
"     var buf = [];\n"+
"     for ( i = 0; i < resolution; i++) {\n"+
"     	for ( j = 0; j < resolution; j++) {\n"+
"		rho = e + f * Math.cos(g * theta + t) * Math.cos(h * phi + p);\n"+
"		var coord = new x3dom.fields.SFVec3f(\n"+
"			rho * Math.cos(phi) * Math.cos(theta),\n"+
"			rho * Math.cos(phi) * Math.sin(theta),\n"+
"			rho * Math.sin(phi)\n"+
"		);\n"+
"	     	buf.push(coord);\n"+
"		theta += delta;\n"+
"	}\n"+
"	phi += delta;\n"+
"     }\n"+
"     coordinates = new x3dom.fields.MFVec3f(buf);\n"+
"}\n"+
"\n"+
"function set_fraction() {\n"+
"	choice = Math.floor(Math.random() * 4);\n"+
"	switch (choice) {\n"+
"	case 0:\n"+
"		e += Math.floor(Math.random() * 2) * 2 - 1;\n"+
"		break;\n"+
"	case 1:\n"+
"		f += Math.floor(Math.random() * 2) * 2 - 1;\n"+
"		break;\n"+
"	case 2:\n"+
"		g += Math.floor(Math.random() * 2) * 2 - 1;\n"+
"		break;\n"+
"	case 3:\n"+
"		h += Math.floor(Math.random() * 2) * 2 - 1;\n"+
"		break;\n"+
"	}\n"+
"	t += 0.5;\n"+
"	p += 0.5;\n"+
"	if (f < 1) {\n"+
"		f = 10;\n"+
"	}\n"+
"	if (g < 1) {\n"+
"		g = 4;\n"+
"	}\n"+
"	if (h < 1) {\n"+
"		h = 4;\n"+
"	}\n"+
"	updateCoordinates(resolution);\n"+
"}''')

Scene1.addChildren(Script12)
TimeSensor16 = x3d.TimeSensor()
TimeSensor16.setDEF("Clock")
TimeSensor16.setCycleInterval(16)
TimeSensor16.setLoop(True)

Scene1.addChildren(TimeSensor16)
ROUTE17 = x3d.ROUTE()
ROUTE17.setFromNode("FlowerScript")
ROUTE17.setFromField("coordIndexes")
ROUTE17.setToNode("ifs")
ROUTE17.setToField("coordIndex")

Scene1.addChildren(ROUTE17)
ROUTE18 = x3d.ROUTE()
ROUTE18.setFromNode("FlowerScript")
ROUTE18.setFromField("coordinates")
ROUTE18.setToNode("crd")
ROUTE18.setToField("point")

Scene1.addChildren(ROUTE18)
ROUTE19 = x3d.ROUTE()
ROUTE19.setFromNode("Clock")
ROUTE19.setFromField("fraction_changed")
ROUTE19.setToNode("FlowerScript")
ROUTE19.setToField("set_fraction")

Scene1.addChildren(ROUTE19)

X3D0.setScene(Scene1)
X3D0.toFileX3D("././flower_RoundTrip.x3d")
