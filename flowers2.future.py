import jnius_config
jnius_config.set_classpath('.', 'X3DJSAIL.3.3.full.jar')
from jnius import autoclass
from X3Dautoclass import *
X3D0 = X3DObject() \
   .setProfile("Immersive") \
   .setVersion("3.0") \
   .setHead(headObject() \
    .addMeta(metaObject() \
     .setName("flowers2.x3d") \
     .setContent("title") \
    ) \
    .addMeta(metaObject() \
     .setName("author") \
     .setContent("John Carlson") \
    ) \
    .addMeta(metaObject() \
     .setName("transcriber") \
     .setContent("John Carlson") \
    ) \
    .addMeta(metaObject() \
     .setName("created") \
     .setContent("23 January 2005") \
    ) \
    .addMeta(metaObject() \
     .setName("modified") \
     .setContent("05 May 2017") \
    ) \
    .addMeta(metaObject() \
     .setName("description") \
     .setContent("2 random mathematical roses in spherical dimensions. rho = a + b * cos(c * theta) * cos(d * phi)") \
    ) \
    .addMeta(metaObject() \
     .setName("url") \
     .setContent("https://coderextreme.net/x3d/flowers2.x3d") \
    ) \
    .addMeta(metaObject() \
     .setName("generator") \
     .setContent("manually written") \
    ) \
   ) \
   .setScene(SceneObject() \
    .addChild(NavigationInfoObject() \
    ) \
    .addChild(ViewpointObject() \
     .setDescription("Two mathematical orbitals") \
     .setPosition([0,0,50]) \
    ) \
    .addChild(GroupObject() \
     .addChild(DirectionalLightObject() \
      .setDirection([1,1,1]) \
     ) \
     .addChild(TransformObject() \
      .setDEF("OrbitTransform") \
      .setTranslation([8,0,0]) \
      .addChild(ShapeObject() \
       .setAppearance(AppearanceObject() \
        .setMaterial(MaterialObject() \
         .setDiffuseColor([0,0.5,1]) \
         .setSpecularColor([0,0.5,1]) \
        ) \
       ) \
       .setGeometry(IndexedFaceSetObject() \
        .setConvex(False) \
        .setDEF("Orbit") \
        .setCoord(CoordinateObject() \
         .setDEF("OrbitCoordinates") \
        ) \
       ) \
      ) \
     ) \
     .addChild(TransformObject() \
      .setDEF("OrbitTransform2") \
      .setTranslation([-8,0,0]) \
      .addChild(ShapeObject() \
       .setAppearance(AppearanceObject() \
        .setMaterial(MaterialObject() \
         .setDiffuseColor([1,0.5,0]) \
         .setSpecularColor([1,0.5,0]) \
         .setTransparency(0.75) \
        ) \
       ) \
       .setGeometry(IndexedFaceSetObject() \
        .setDEF("Orbit2") \
        .setCoord(CoordinateObject() \
         .setDEF("OrbitCoordinates2") \
        ) \
       ) \
      ) \
     ) \
     .addChild(TimeSensorObject() \
      .setDEF("Clock") \
      .setCycleInterval(16) \
      .setLoop(True) \
     ) \
     .addChild(OrientationInterpolatorObject() \
      .setDEF("OrbitPath") \
      .setKey([0,0.5,1]) \
      .setKeyValue([1,0,0,0,1,0,0,3.14,1,0,0,6.28]) \
     ) \
     .addChild(ScriptObject() \
      .setDEF("OrbitScript") \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFFLOAT) \
       .setName("set_fraction") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTONLY) \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_MFVEC3F) \
       .setName("coordinates") \
       .setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY) \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_MFINT32) \
       .setName("coordIndexes") \
       .setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY) \
      ) \
      .setSourceCode('''ecmascript:\n"+
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
     ) \
     .addChild(ScriptObject() \
      .setDEF("OrbitScript2") \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_SFFLOAT) \
       .setName("set_fraction") \
       .setAccessType(fieldObject.ACCESSTYPE_INPUTONLY) \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_MFVEC3F) \
       .setName("coordinates") \
       .setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY) \
      ) \
      .addField(fieldObject() \
       .setType(fieldObject.TYPE_MFINT32) \
       .setName("coordIndexes") \
       .setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY) \
      ) \
      .setSourceCode('''ecmascript:\n"+
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
     ) \
    ) \
    .addChild(ROUTEObject() \
     .setFromField("coordIndexes") \
     .setFromNode("OrbitScript") \
     .setToField("coordIndex") \
     .setToNode("Orbit") \
    ) \
    .addChild(ROUTEObject() \
     .setFromField("coordinates") \
     .setFromNode("OrbitScript") \
     .setToField("point") \
     .setToNode("OrbitCoordinates") \
    ) \
    .addChild(ROUTEObject() \
     .setFromField("fraction_changed") \
     .setFromNode("Clock") \
     .setToField("set_fraction") \
     .setToNode("OrbitScript") \
    ) \
    .addChild(ROUTEObject() \
     .setFromField("coordIndexes") \
     .setFromNode("OrbitScript2") \
     .setToField("coordIndex") \
     .setToNode("Orbit2") \
    ) \
    .addChild(ROUTEObject() \
     .setFromField("coordinates") \
     .setFromNode("OrbitScript2") \
     .setToField("point") \
     .setToNode("OrbitCoordinates2") \
    ) \
    .addChild(ROUTEObject() \
     .setFromField("fraction_changed") \
     .setFromNode("Clock") \
     .setToField("set_fraction") \
     .setToNode("OrbitScript2") \
    ) \
    .addChild(ROUTEObject() \
     .setFromField("fraction_changed") \
     .setFromNode("Clock") \
     .setToField("set_fraction") \
     .setToNode("OrbitPath") \
    ) \
    .addChild(ROUTEObject() \
     .setFromField("value_changed") \
     .setFromNode("OrbitPath") \
     .setToField("rotation") \
     .setToNode("OrbitTransform") \
    ) \
    .addChild(ROUTEObject() \
     .setFromField("value_changed") \
     .setFromNode("OrbitPath") \
     .setToField("rotation") \
     .setToNode("OrbitTransform2") \
    ) \
   ) \

X3D0.toFileX3D("./future/./flowers2.newf.x3d")
