# -*- coding: UTF-8 -*-
from jnius import autoclass
from X3Dautoclass import *
X3D0 =  X3DObject()
X3D0.setProfile("Immersive")
X3D0.setVersion("3.3")

head1 = headObject()

meta2 = metaObject()
meta2.setName("title")
meta2.setContent("flowers.x3d")

head1.addMeta(meta2)
meta3 = metaObject()
meta3.setName("creator")
meta3.setContent("John Carlson")

head1.addMeta(meta3)
meta4 = metaObject()
meta4.setName("description")
meta4.setContent("5 or more prismatic flowers")

head1.addMeta(meta4)
meta5 = metaObject()
meta5.setName("generator")
meta5.setContent("X3D-Edit, https://savage.nps.edu/X3D-Edit")

head1.addMeta(meta5)
meta6 = metaObject()
meta6.setName("identifier")
meta6.setContent("http://coderextreme.net/X3DJSONLD/flowers.x3d")

head1.addMeta(meta6)
X3D0.setHead(head1)
Scene7 = SceneObject()

NavigationInfo8 = NavigationInfoObject()

Scene7.addChild(NavigationInfo8)
Background9 = BackgroundObject()
Background9.setBackUrl(["cubemap/all_probes/stpeters_cross/stpeters_back.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_back.png"])
Background9.setBottomUrl(["cubemap/all_probes/stpeters_cross/stpeters_bottom.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_bottom.png"])
Background9.setFrontUrl(["cubemap/all_probes/stpeters_cross/stpeters_front.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_front.png"])
Background9.setLeftUrl(["cubemap/all_probes/stpeters_cross/stpeters_left.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_left.png"])
Background9.setRightUrl(["cubemap/all_probes/stpeters_cross/stpeters_right.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_right.png"])
Background9.setTopUrl(["cubemap/all_probes/stpeters_cross/stpeters_top.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_top.png"])

Scene7.addChild(Background9)
ProtoDeclare10 = ProtoDeclareObject()
ProtoDeclare10.setName("flower")

ProtoBody11 = ProtoBodyObject()

Transform12 = TransformObject()
Transform12.setDEF("transform")

Shape13 = ShapeObject()

Appearance14 = AppearanceObject()

Material15 = MaterialObject()
Material15.setDiffuseColor([0.7,0.7,0.7])
Material15.setSpecularColor([0.5,0.5,0.5])

Appearance14.setMaterial(Material15)
ComposedCubeMapTexture16 = ComposedCubeMapTextureObject()
ComposedCubeMapTexture16.setDEF("texture")

ImageTexture17 = ImageTextureObject()
ImageTexture17.setUrl(["cubemap/all_probes/stpeters_cross/stpeters_back.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_back.png"])

ComposedCubeMapTexture16.setBack(ImageTexture17)
ImageTexture18 = ImageTextureObject()
ImageTexture18.setUrl(["cubemap/all_probes/stpeters_cross/stpeters_bottom.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_bottom.png"])

ComposedCubeMapTexture16.setBottom(ImageTexture18)
ImageTexture19 = ImageTextureObject()
ImageTexture19.setUrl(["cubemap/all_probes/stpeters_cross/stpeters_front.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_front.png"])

ComposedCubeMapTexture16.setFront(ImageTexture19)
ImageTexture20 = ImageTextureObject()
ImageTexture20.setUrl(["cubemap/all_probes/stpeters_cross/stpeters_left.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_left.png"])

ComposedCubeMapTexture16.setLeft(ImageTexture20)
ImageTexture21 = ImageTextureObject()
ImageTexture21.setUrl(["cubemap/all_probes/stpeters_cross/stpeters_right.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_right.png"])

ComposedCubeMapTexture16.setRight(ImageTexture21)
ImageTexture22 = ImageTextureObject()
ImageTexture22.setUrl(["cubemap/all_probes/stpeters_cross/stpeters_top.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_top.png"])

ComposedCubeMapTexture16.setTop(ImageTexture22)
Appearance14.setTexture(ComposedCubeMapTexture16)
ComposedShader23 = ComposedShaderObject()
ComposedShader23.setDEF("shader")
ComposedShader23.setLanguage("GLSL")

field24 = fieldObject()
field24.setType(fieldObject.TYPE_SFINT32)
field24.setName("xxxcube")
field24.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field24.setValue("0")

ComposedShader23.addField(field24)
field25 = fieldObject()
field25.setType(fieldObject.TYPE_SFNODE)
field25.setName("cube")
field25.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)

ComposedCubeMapTexture26 = ComposedCubeMapTextureObject()
ComposedCubeMapTexture26.setUSE("texture")

field25.addChild(ComposedCubeMapTexture26)
ComposedShader23.addField(field25)
field27 = fieldObject()
field27.setType(fieldObject.TYPE_SFVEC3F)
field27.setName("chromaticDispertion")
field27.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field27.setValue("0.98 1 1.033")

ComposedShader23.addField(field27)
field28 = fieldObject()
field28.setType(fieldObject.TYPE_SFFLOAT)
field28.setName("bias")
field28.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field28.setValue("10")

ComposedShader23.addField(field28)
field29 = fieldObject()
field29.setType(fieldObject.TYPE_SFFLOAT)
field29.setName("scale")
field29.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field29.setValue("10")

ComposedShader23.addField(field29)
field30 = fieldObject()
field30.setType(fieldObject.TYPE_SFFLOAT)
field30.setName("power")
field30.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field30.setValue("2")

ComposedShader23.addField(field30)
ShaderPart31 = ShaderPartObject()
ShaderPart31.setType("VERTEX")
ShaderPart31.setUrl(["cobweb.vs","http://coderextreme.net/X3DJSONLD/cobweb.vs"])

ComposedShader23.addParts(ShaderPart31)
ShaderPart32 = ShaderPartObject()
ShaderPart32.setType("FRAGMENT")
ShaderPart32.setUrl(["pc_bubbles.fs","http://coderextreme.net/X3DJSONLD/pc_bubbles.fs"])

ComposedShader23.addParts(ShaderPart32)
Appearance14.addShaders(ComposedShader23)
Shape13.setAppearance(Appearance14)
IndexedFaceSet33 = IndexedFaceSetObject()
IndexedFaceSet33.setDEF("Orbit")

Coordinate34 = CoordinateObject()
Coordinate34.setDEF("OrbitCoordinates")

IndexedFaceSet33.setCoord(Coordinate34)
Shape13.setGeometry(IndexedFaceSet33)
Transform12.addChild(Shape13)
ProtoBody11.addChild(Transform12)
Script35 = ScriptObject()
Script35.setDEF("Bounce")

field36 = fieldObject()
field36.setType(fieldObject.TYPE_SFVEC3F)
field36.setName("translation")
field36.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field36.setValue("0 0 0")

Script35.addField(field36)
field37 = fieldObject()
field37.setType(fieldObject.TYPE_SFVEC3F)
field37.setName("velocity")
field37.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field37.setValue("0 0 0")

Script35.addField(field37)
field38 = fieldObject()
field38.setType(fieldObject.TYPE_SFTIME)
field38.setName("set_fraction")
field38.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)

Script35.addField(field38)
field39 = fieldObject()
field39.setType(fieldObject.TYPE_MFVEC3F)
field39.setName("coordinates")
field39.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)

Script35.addField(field39)
field40 = fieldObject()
field40.setType(fieldObject.TYPE_MFINT32)
field40.setName("coordIndexes")
field40.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)

Script35.addField(field40)
field41 = fieldObject()
field41.setType(fieldObject.TYPE_SFFLOAT)
field41.setName("a")
field41.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field41.setValue("0.5")

Script35.addField(field41)
field42 = fieldObject()
field42.setType(fieldObject.TYPE_SFFLOAT)
field42.setName("b")
field42.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field42.setValue("0.5")

Script35.addField(field42)
field43 = fieldObject()
field43.setType(fieldObject.TYPE_SFFLOAT)
field43.setName("c")
field43.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field43.setValue("3")

Script35.addField(field43)
field44 = fieldObject()
field44.setType(fieldObject.TYPE_SFFLOAT)
field44.setName("d")
field44.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field44.setValue("3")

Script35.addField(field44)
field45 = fieldObject()
field45.setType(fieldObject.TYPE_SFFLOAT)
field45.setName("tdelta")
field45.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field45.setValue("0.5")

Script35.addField(field45)
field46 = fieldObject()
field46.setType(fieldObject.TYPE_SFFLOAT)
field46.setName("pdelta")
field46.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field46.setValue("0.5")

Script35.addField(field46)

Script35.setSourceCode("ecmascript:\n"+
"			function set_translation(value) {\n"+
"				translation = value;\n"+
"			}\n"+
"			function translation_changed() {\n"+
"				return translation;\n"+
"			}\n"+
"			function initialize() {\n"+
"			    translation = new SFVec3f(0, 0, 0);\n"+
"			    velocity = new SFVec3f(\n"+
"			    	Math.random() - 0.5,\n"+
"				Math.random() - 0.5,\n"+
"				Math.random() - 0.5);\n"+
"			}\n"+
"			function set_fraction() {\n"+
"			    translation = new SFVec3f(\n"+
"			    	translation[0] + velocity[0],\n"+
"				translation[1] + velocity[1],\n"+
"				translation[2] + velocity[2]);\n"+
"			    for (var j = 0; j <= 2; j++) {\n"+
"				    if (Math.abs(translation[j]) > 10) {\n"+
"					initialize();\n"+
"				    } else {\n"+
"					velocity[0] += Math.random() * 0.2 - 0.1;\n"+
"					velocity[1] += Math.random() * 0.2 - 0.1;\n"+
"					velocity[2] += Math.random() * 0.2 - 0.1;\n"+
"				    }\n"+
"			    }\n"+
"			    animate_flowers();\n"+
"			}\n"+
"\n"+
"			function initialize() {\n"+
"			     resolution = 100;\n"+
"			     updateCoordinates(resolution);\n"+
"			     if (typeof coordIndexes == 'undefined' || coordIndexes == null) {\n"+
"				coordIndexes = new MFInt32();\n"+
"			     }\n"+
"			     ci = 0;\n"+
"			     for ( i = 0; i < resolution-1; i++) {\n"+
"				for ( j = 0; j < resolution-1; j++) {\n"+
"				     coordIndexes[ci] = i*resolution+j;\n"+
"				     coordIndexes[ci+1] = i*resolution+j+1;\n"+
"				     coordIndexes[ci+2] = (i+1)*resolution+j+1;\n"+
"				     coordIndexes[ci+3] = (i+1)*resolution+j;\n"+
"				     coordIndexes[ci+4] = -1;\n"+
"				     ci += 5;\n"+
"				}\n"+
"			    }\n"+
"			}\n"+
"\n"+
"			function updateCoordinates(resolution) {\n"+
"			     theta = 0.0;\n"+
"			     phi = 0.0;\n"+
"			     delta = (2 * 3.141592653) / (resolution-1);\n"+
"			     if (typeof coordinates == 'undefined' || coordinates == null) {\n"+
"				coordinates = new MFVec3f();\n"+
"			     }\n"+
"			     for ( i = 0; i < resolution; i++) {\n"+
"				for ( j = 0; j < resolution; j++) {\n"+
"					rho = a + b * Math.cos(c * theta) * Math.cos(d * phi);\n"+
"					coordinates[i*resolution+j] = new SFVec3f();\n"+
"					coordinates[i*resolution+j][0] = rho * Math.cos(phi) * Math.cos(theta);\n"+
"					coordinates[i*resolution+j][1] = rho * Math.cos(phi) * Math.sin(theta);\n"+
"					coordinates[i*resolution+j][2] = rho * Math.sin(phi);\n"+
"					theta += delta;\n"+
"				}\n"+
"				phi += delta;\n"+
"			     }\n"+
"			}\n"+
"\n"+
"			function animate_flowers(fraction, eventTime) {\n"+
"				choice = Math.floor(Math.random() * 4);\n"+
"				switch (choice) {\n"+
"				case 0:\n"+
"					a += Math.random() * 0.2 - 0.1;\n"+
"					break;\n"+
"				case 1:\n"+
"					b += Math.random() * 0.2 - 0.1;\n"+
"					break;\n"+
"				case 2:\n"+
"					c += Math.random() * 2 - 1;\n"+
"					break;\n"+
"				case 3:\n"+
"					d += Math.random() * 2 - 1;\n"+
"					break;\n"+
"				}\n"+
"				if (a > 1) {\n"+
"					a =  0.5;\n"+
"				}\n"+
"				if (b > 1) {\n"+
"					b =  0.5;\n"+
"				}\n"+
"				if (c < 1) {\n"+
"					c =  4;\n"+
"				}\n"+
"				if (d < 1) {\n"+
"					d =  4;\n"+
"				}\n"+
"				if (c > 10) {\n"+
"					c = 4;\n"+
"				}\n"+
"				if (d > 10) {\n"+
"					d = 4;\n"+
"				}\n"+
"				resolution = 100;\n"+
"				updateCoordinates(resolution);\n"+
"			}\n"+
"")
ProtoBody11.addChild(Script35)
TimeSensor47 = TimeSensorObject()
TimeSensor47.setDEF("TourTime")
TimeSensor47.setCycleInterval(0.15)
TimeSensor47.setLoop(True)

ProtoBody11.addChild(TimeSensor47)
ROUTE48 = ROUTEObject()
ROUTE48.setFromNode("TourTime")
ROUTE48.setFromField("cycleTime")
ROUTE48.setToNode("Bounce")
ROUTE48.setToField("set_fraction")

ProtoBody11.addChild(ROUTE48)
ROUTE49 = ROUTEObject()
ROUTE49.setFromNode("Bounce")
ROUTE49.setFromField("translation_changed")
ROUTE49.setToNode("transform")
ROUTE49.setToField("set_translation")

ProtoBody11.addChild(ROUTE49)
ROUTE50 = ROUTEObject()
ROUTE50.setFromField("coordIndexes")
ROUTE50.setFromNode("Bounce")
ROUTE50.setToField("set_coordIndex")
ROUTE50.setToNode("Orbit")

ProtoBody11.addChild(ROUTE50)
ROUTE51 = ROUTEObject()
ROUTE51.setFromField("coordinates")
ROUTE51.setFromNode("Bounce")
ROUTE51.setToField("set_point")
ROUTE51.setToNode("OrbitCoordinates")

ProtoBody11.addChild(ROUTE51)
ProtoDeclare10.setProtoBody(ProtoBody11)
Scene7.addChild(ProtoDeclare10)
Transform52 = TransformObject()

ProtoInstance53 = ProtoInstanceObject()
ProtoInstance53.setName("flower")

Transform52.addChild(ProtoInstance53)
ProtoInstance54 = ProtoInstanceObject()
ProtoInstance54.setName("flower")

Transform52.addChild(ProtoInstance54)
ProtoInstance55 = ProtoInstanceObject()
ProtoInstance55.setName("flower")

Transform52.addChild(ProtoInstance55)
Scene7.addChild(Transform52)
X3D0.setScene(Scene7)

X3D0.toFileX3D("./flowers.new.x3d")
