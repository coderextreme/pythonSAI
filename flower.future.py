import x3dpsail


X3D0 = (x3dpsail.X3D().setProfile(x3dpsail.SFString("Immersive")).setVersion(x3dpsail.SFString("3.3"))
      .setScene(x3dpsail.Scene()
        .addChild(x3dpsail.NavigationInfo())
        .addChild(x3dpsail.DirectionalLight().setDirection(x3dpsail.SFVec3f(0,-0.8,-0.2)).setIntensity(x3dpsail.SFFloat(0.5)))
        .addChild(x3dpsail.Background().setSkyColor(x3dpsail.MFColor([1,1,1])))
        .addChild(x3dpsail.Viewpoint().setDescription(x3dpsail.SFString("One mathematical orbital")).setPosition(x3dpsail.SFVec3f(0,0,50)))
        .addChild(x3dpsail.Transform().setTranslation(x3dpsail.SFVec3f(0,-1,1)).setRotation(x3dpsail.SFRotation(0,1,0,3.1415926)).setScale(x3dpsail.SFVec3f(1.5,1.5,1.5))
          .addChild(x3dpsail.Shape()
            .setAppearance(x3dpsail.Appearance()
              .setMaterial(x3dpsail.Material().setTransparency(x3dpsail.SFFloat(0.1)).setDiffuseColor(x3dpsail.SFColor(0.9,0.3,0.3)).setSpecularColor(x3dpsail.SFColor(0.8,0.8,0.8)).setShininess(x3dpsail.SFFloat(0.145))))
            .setGeometry(x3dpsail.IndexedFaceSet().setCcw(x3dpsail.SFBool(False)).setConvex(x3dpsail.SFBool(False)).setCoordIndex(x3dpsail.MFInt32([0,1,2,-1])).setDEF(x3dpsail.SFString("ifs"))
              .setCoord(x3dpsail.Coordinate().setDEF(x3dpsail.SFString("crd")).setPoint(x3dpsail.MFVec3f([0,0,1,0,1,0,1,0,0]))))))
        .addChild(x3dpsail.Script().setDEF(x3dpsail.SFString("FlowerScript"))
          .addField(x3dpsail.field().setName(x3dpsail.SFString("set_fraction")).setAccessType(x3dpsail.SFString("inputOnly")).setType(x3dpsail.SFString("SFFloat")))
          .addField(x3dpsail.field().setName(x3dpsail.SFString("coordinates")).setAccessType(x3dpsail.SFString("outputOnly")).setType(x3dpsail.SFString("MFVec3f")))
          .addField(x3dpsail.field().setName(x3dpsail.SFString("coordIndexes")).setAccessType(x3dpsail.SFString("outputOnly")).setType(x3dpsail.SFString("MFInt32"))).setSourceCode('''ecmascript:\n"+
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
)
        .addChild(x3dpsail.TimeSensor().setDEF(x3dpsail.SFString("Clock")).setCycleInterval(x3dpsail.SFTime(16)).setLoop(x3dpsail.SFBool(True)))
        .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("FlowerScript")).setFromField(x3dpsail.SFString("coordIndexes")).setToNode(x3dpsail.SFString("ifs")).setToField(x3dpsail.SFString("coordIndex")))
        .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("FlowerScript")).setFromField(x3dpsail.SFString("coordinates")).setToNode(x3dpsail.SFString("crd")).setToField(x3dpsail.SFString("point")))
        .addChild(x3dpsail.ROUTE().setFromNode(x3dpsail.SFString("Clock")).setFromField(x3dpsail.SFString("fraction_changed")).setToNode(x3dpsail.SFString("FlowerScript")).setToField(x3dpsail.SFString("set_fraction")))))

X3D0.toFileX3D("./future/./flower_RoundTrip.x3d")
