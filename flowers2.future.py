import x3dpsail


X3D0 = (x3dpsail.X3D().setProfile(x3dpsail.SFString("Immersive")).setVersion(x3dpsail.SFString("3.0"))
      .setHead(x3dpsail.head()
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("flowers2.x3d")).setContent(x3dpsail.SFString("title")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("author")).setContent(x3dpsail.SFString("John Carlson")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("transcriber")).setContent(x3dpsail.SFString("John Carlson")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("created")).setContent(x3dpsail.SFString("23 January 2005")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("modified")).setContent(x3dpsail.SFString("05 May 2017")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("description")).setContent(x3dpsail.SFString("2 random mathematical roses in spherical dimensions. rho = a + b * cos(c * theta) * cos(d * phi)")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("url")).setContent(x3dpsail.SFString("https://coderextreme.net/x3d/flowers2.x3d")))
        .addMeta(x3dpsail.meta().setName(x3dpsail.SFString("generator")).setContent(x3dpsail.SFString("manually written"))))
      .setScene(x3dpsail.Scene()
        .addChild(x3dpsail.NavigationInfo())
        .addChild(x3dpsail.Viewpoint().setDescription(x3dpsail.SFString("Two mathematical orbitals")).setPosition(x3dpsail.SFVec3f(0,0,50)))
        .addChild(x3dpsail.Group()
          .addChild(x3dpsail.DirectionalLight().setDirection(x3dpsail.SFVec3f(1,1,1)))
          .addChild(x3dpsail.Transform().setDEF(x3dpsail.SFString("OrbitTransform")).setTranslation(x3dpsail.SFVec3f(8,0,0))
            .addChild(x3dpsail.Shape()
              .setAppearance(x3dpsail.Appearance()
                .setMaterial(x3dpsail.Material().setDiffuseColor(x3dpsail.SFColor(0,0.5,1)).setSpecularColor(x3dpsail.SFColor(0,0.5,1))))
              .setGeometry(x3dpsail.IndexedFaceSet().setConvex(x3dpsail.SFBool(False)).setDEF(x3dpsail.SFString("Orbit"))
                .setCoord(x3dpsail.Coordinate().setDEF(x3dpsail.SFString("OrbitCoordinates"))))))
          .addChild(x3dpsail.Transform().setDEF(x3dpsail.SFString("OrbitTransform2")).setTranslation(x3dpsail.SFVec3f(-8,0,0))
            .addChild(x3dpsail.Shape()
              .setAppearance(x3dpsail.Appearance()
                .setMaterial(x3dpsail.Material().setDiffuseColor(x3dpsail.SFColor(1,0.5,0)).setSpecularColor(x3dpsail.SFColor(1,0.5,0)).setTransparency(x3dpsail.SFFloat(0.75))))
              .setGeometry(x3dpsail.IndexedFaceSet().setDEF(x3dpsail.SFString("Orbit2"))
                .setCoord(x3dpsail.Coordinate().setDEF(x3dpsail.SFString("OrbitCoordinates2"))))))
          .addChild(x3dpsail.TimeSensor().setDEF(x3dpsail.SFString("Clock")).setCycleInterval(x3dpsail.SFTime(16)).setLoop(x3dpsail.SFBool(True)))
          .addChild(x3dpsail.OrientationInterpolator().setDEF(x3dpsail.SFString("OrbitPath")).setKey(x3dpsail.MFFloat([0,0.5,1])).setKeyValue(x3dpsail.MFRotation([1,0,0,0,1,0,0,3.14,1,0,0,6.28])))
          .addChild(x3dpsail.Script().setDEF(x3dpsail.SFString("OrbitScript"))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("set_fraction")).setAccessType(x3dpsail.SFString("inputOnly")).setType(x3dpsail.SFString("SFFloat")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("coordinates")).setAccessType(x3dpsail.SFString("outputOnly")).setType(x3dpsail.SFString("MFVec3f")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("coordIndexes")).setAccessType(x3dpsail.SFString("outputOnly")).setType(x3dpsail.SFString("MFInt32"))).setSourceCode('''ecmascript:\n"+
"\n"+
"var e = 5;\n"+
"var f = 5;\n"+
"var g = 5;\n"+
"var h = 5;\n"+
"\n"+
"function initialize() {\n"+
"     resolution = 100;\n"+
"     generateCoordinates(resolution);\n"+
"     var localci = [];\n"+
"     for ( i = 0; i < resolution-1; i++) {\n"+
"     	for ( j = 0; j < resolution-1; j++) {\n"+
"	     localci.push(i*resolution+j);\n"+
"	     localci.push(i*resolution+j+1);\n"+
"	     localci.push((i+1)*resolution+j+1);\n"+
"	     localci.push((i+1)*resolution+j);\n"+
"	     localci.push(-1);\n"+
"	}\n"+
"    }\n"+
"    coordIndexes = new MFInt32(localci);\n"+
"}\n"+
"\n"+
"function generateCoordinates(resolution) {\n"+
"     theta = 0.0;\n"+
"     phi = 0.0;\n"+
"     delta = (2 * 3.141592653) / (resolution-1);\n"+
"     var localc = [];\n"+
"     for ( i = 0; i < resolution; i++) {\n"+
"     	for ( j = 0; j < resolution; j++) {\n"+
"		rho = e + f * Math.cos(g * theta) * Math.cos(h * phi);\n"+
"		localc.push(new SFVec3f(\n"+
"			rho * Math.cos(phi) * Math.cos(theta),\n"+
"			rho * Math.cos(phi) * Math.sin(theta),\n"+
"			rho * Math.sin(phi)\n"+
"		));\n"+
"		theta += delta;\n"+
"	}\n"+
"	phi += delta;\n"+
"     }\n"+
"     coordinates = new MFVec3f(localc);\n"+
"}\n"+
"\n"+
"function set_fraction(fraction, eventTime) {\n"+
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
"	if (f < 1) {\n"+
"		f = 10;\n"+
"	}\n"+
"	if (g < 1) {\n"+
"		g = 4;\n"+
"	}\n"+
"	if (h < 1) {\n"+
"		h = 4;\n"+
"	}\n"+
"	resolution = 100;\n"+
"	generateCoordinates(resolution);\n"+
"}''')
)
          .addChild(x3dpsail.Script().setDEF(x3dpsail.SFString("OrbitScript2"))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("set_fraction")).setAccessType(x3dpsail.SFString("inputOnly")).setType(x3dpsail.SFString("SFFloat")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("coordinates")).setAccessType(x3dpsail.SFString("outputOnly")).setType(x3dpsail.SFString("MFVec3f")))
            .addField(x3dpsail.field().setName(x3dpsail.SFString("coordIndexes")).setAccessType(x3dpsail.SFString("outputOnly")).setType(x3dpsail.SFString("MFInt32"))).setSourceCode('''ecmascript:\n"+
"\n"+
"var e = 5;\n"+
"var f = 5;\n"+
"var g = 5;\n"+
"var h = 5;\n"+
"\n"+
"function initialize() {\n"+
"     resolution = 100;\n"+
"     generateCoordinates(resolution);\n"+
"     var localci = [];\n"+
"     for ( i = 0; i < resolution-1; i++) {\n"+
"     	for ( j = 0; j < resolution-1; j++) {\n"+
"	     localci.push(i*resolution+j);\n"+
"	     localci.push(i*resolution+j+1);\n"+
"	     localci.push((i+1)*resolution+j+1);\n"+
"	     localci.push((i+1)*resolution+j);\n"+
"	     localci.push(-1);\n"+
"	}\n"+
"    }\n"+
"    coordIndexes = new MFInt32(localci);\n"+
"}\n"+
"\n"+
"function generateCoordinates(resolution) {\n"+
"     theta = 0.0;\n"+
"     phi = 0.0;\n"+
"     delta = (2 * 3.141592653) / (resolution-1);\n"+
"     var localc = [];\n"+
"     for ( i = 0; i < resolution; i++) {\n"+
"     	for ( j = 0; j < resolution; j++) {\n"+
"		rho = e + f * Math.cos(g * theta) * Math.cos(h * phi);\n"+
"		localc.push(new SFVec3f(\n"+
"			rho * Math.cos(phi) * Math.cos(theta),\n"+
"			rho * Math.cos(phi) * Math.sin(theta),\n"+
"			rho * Math.sin(phi)\n"+
"		));\n"+
"		theta += delta;\n"+
"	}\n"+
"	phi += delta;\n"+
"     }\n"+
"\n"+
"     coordinates = new MFVec3f(localc);\n"+
"}\n"+
"\n"+
"function set_fraction(fraction, eventTime) {\n"+
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
"	if (f < 1) {\n"+
"		f = 10;\n"+
"	}\n"+
"	if (g < 1) {\n"+
"		g = 4;\n"+
"	}\n"+
"	if (h < 1) {\n"+
"		h = 4;\n"+
"	}\n"+
"	resolution = 100;\n"+
"	generateCoordinates(resolution);\n"+
"}''')
))
        .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("coordIndexes")).setFromNode(x3dpsail.SFString("OrbitScript")).setToField(x3dpsail.SFString("coordIndex")).setToNode(x3dpsail.SFString("Orbit")))
        .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("coordinates")).setFromNode(x3dpsail.SFString("OrbitScript")).setToField(x3dpsail.SFString("point")).setToNode(x3dpsail.SFString("OrbitCoordinates")))
        .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("fraction_changed")).setFromNode(x3dpsail.SFString("Clock")).setToField(x3dpsail.SFString("set_fraction")).setToNode(x3dpsail.SFString("OrbitScript")))
        .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("coordIndexes")).setFromNode(x3dpsail.SFString("OrbitScript2")).setToField(x3dpsail.SFString("coordIndex")).setToNode(x3dpsail.SFString("Orbit2")))
        .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("coordinates")).setFromNode(x3dpsail.SFString("OrbitScript2")).setToField(x3dpsail.SFString("point")).setToNode(x3dpsail.SFString("OrbitCoordinates2")))
        .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("fraction_changed")).setFromNode(x3dpsail.SFString("Clock")).setToField(x3dpsail.SFString("set_fraction")).setToNode(x3dpsail.SFString("OrbitScript2")))
        .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("fraction_changed")).setFromNode(x3dpsail.SFString("Clock")).setToField(x3dpsail.SFString("set_fraction")).setToNode(x3dpsail.SFString("OrbitPath")))
        .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("value_changed")).setFromNode(x3dpsail.SFString("OrbitPath")).setToField(x3dpsail.SFString("rotation")).setToNode(x3dpsail.SFString("OrbitTransform")))
        .addChild(x3dpsail.ROUTE().setFromField(x3dpsail.SFString("value_changed")).setFromNode(x3dpsail.SFString("OrbitPath")).setToField(x3dpsail.SFString("rotation")).setToNode(x3dpsail.SFString("OrbitTransform2")))))

X3D0.toFileX3D("./future/./flowers2_RoundTrip.x3d")
