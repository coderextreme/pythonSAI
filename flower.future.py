import jnius_config
jnius_config.set_classpath('.', 'X3DJSAIL.3.3.full.jar')
from jnius import autoclass
from X3Dautoclass import *
X3D0 = X3DObject() \
   .setProfile("Immersive") \
   .setVersion("3.3") \
   .setScene(SceneObject() \
    .addChild(NavigationInfoObject() \
    ) \
    .addChild(DirectionalLightObject() \
     .setDirection([0,-0.8,-0.2]) \
     .setIntensity(0.5) \
    ) \
    .addChild(BackgroundObject() \
     .setSkyColor([1,1,1]) \
    ) \
    .addChild(ViewpointObject() \
     .setDescription("One mathematical orbital") \
     .setPosition([0,0,50]) \
    ) \
    .addChild(TransformObject() \
     .setTranslation([0,-1,1]) \
     .setRotation([0,1,0,3.1415926]) \
     .setScale([1.5,1.5,1.5]) \
     .addChild(ShapeObject() \
      .setAppearance(AppearanceObject() \
       .setMaterial(MaterialObject() \
        .setTransparency(0.1) \
        .setDiffuseColor([0.9,0.3,0.3]) \
        .setSpecularColor([0.8,0.8,0.8]) \
        .setShininess(0.145) \
       ) \
      ) \
      .setGeometry(IndexedFaceSetObject() \
       .setCcw(False) \
       .setConvex(False) \
       .setCoordIndex([0,1,2,-1]) \
       .setDEF("ifs") \
       .setCoord(CoordinateObject() \
        .setDEF("crd") \
        .setPoint([0,0,1,0,1,0,1,0,0]) \
       ) \
      ) \
     ) \
    ) \
    .addChild(ScriptObject() \
     .setDEF("FlowerScript") \
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
    ) \
    .addChild(TimeSensorObject() \
     .setDEF("Clock") \
     .setCycleInterval(16) \
     .setLoop(True) \
    ) \
    .addChild(ROUTEObject() \
     .setFromNode("FlowerScript") \
     .setFromField("coordIndexes") \
     .setToNode("ifs") \
     .setToField("coordIndex") \
    ) \
    .addChild(ROUTEObject() \
     .setFromNode("FlowerScript") \
     .setFromField("coordinates") \
     .setToNode("crd") \
     .setToField("point") \
    ) \
    .addChild(ROUTEObject() \
     .setFromNode("Clock") \
     .setFromField("fraction_changed") \
     .setToNode("FlowerScript") \
     .setToField("set_fraction") \
    ) \
   ) \

X3D0.toFileX3D("./future/./flower.newf.x3d")
