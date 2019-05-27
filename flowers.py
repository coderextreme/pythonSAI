import x3dpsail
X3D0 = x3dpsail.X3D()
X3D0.setProfile("Immersive")
X3D0.setVersion("3.3")
head1 = x3dpsail.head()
component2 = x3dpsail.component()
component2.setName("Shaders")
component2.setLevel(1)

head1.addComponent(component2)
component3 = x3dpsail.component()
component3.setName("CubeMapTexturing")
component3.setLevel(1)

head1.addComponent(component3)
meta4 = x3dpsail.meta()
meta4.setName("title")
meta4.setContent("flowers.x3d")

head1.addMeta(meta4)
meta5 = x3dpsail.meta()
meta5.setName("creator")
meta5.setContent("John Carlson")

head1.addMeta(meta5)
meta6 = x3dpsail.meta()
meta6.setName("description")
meta6.setContent("5 or more prismatic flowers")

head1.addMeta(meta6)
meta7 = x3dpsail.meta()
meta7.setName("generator")
meta7.setContent("X3D-Edit, https://savage.nps.edu/X3D-Edit")

head1.addMeta(meta7)
meta8 = x3dpsail.meta()
meta8.setName("identifier")
meta8.setContent("https://coderextreme.net/X3DJSONLD/flowers.x3d")

head1.addMeta(meta8)

X3D0.setHead(head1)
Scene9 = x3dpsail.Scene()
NavigationInfo10 = x3dpsail.NavigationInfo()

Scene9.addChildren(NavigationInfo10)
Background11 = x3dpsail.Background()
Background11.setBackUrl(["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"])
Background11.setBottomUrl(["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"])
Background11.setFrontUrl(["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"])
Background11.setLeftUrl(["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"])
Background11.setRightUrl(["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"])
Background11.setTopUrl(["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"])

Scene9.addChildren(Background11)
ProtoDeclare12 = x3dpsail.ProtoDeclare()
ProtoDeclare12.setName("flower")
ProtoBody13 = x3dpsail.ProtoBody()
Transform14 = x3dpsail.Transform()
Transform14.setDEF("transform")
Shape15 = x3dpsail.Shape()
Appearance16 = x3dpsail.Appearance()
Material17 = x3dpsail.Material()
Material17.setDiffuseColor([0.7,0.7,0.7])
Material17.setSpecularColor([0.5,0.5,0.5])

Appearance16.setMaterial(Material17)
ComposedCubeMapTexture18 = x3dpsail.ComposedCubeMapTexture()
ComposedCubeMapTexture18.setDEF("texture")
ImageTexture19 = x3dpsail.ImageTexture()
ImageTexture19.setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"])

ComposedCubeMapTexture18.setBack(ImageTexture19)
ImageTexture20 = x3dpsail.ImageTexture()
ImageTexture20.setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"])

ComposedCubeMapTexture18.setBottom(ImageTexture20)
ImageTexture21 = x3dpsail.ImageTexture()
ImageTexture21.setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"])

ComposedCubeMapTexture18.setFront(ImageTexture21)
ImageTexture22 = x3dpsail.ImageTexture()
ImageTexture22.setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"])

ComposedCubeMapTexture18.setLeft(ImageTexture22)
ImageTexture23 = x3dpsail.ImageTexture()
ImageTexture23.setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"])

ComposedCubeMapTexture18.setRight(ImageTexture23)
ImageTexture24 = x3dpsail.ImageTexture()
ImageTexture24.setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"])

ComposedCubeMapTexture18.setTop(ImageTexture24)

Appearance16.setTexture(ComposedCubeMapTexture18)
ComposedShader25 = x3dpsail.ComposedShader()
ComposedShader25.setLanguage("GLSL")
field26 = x3dpsail.field()
field26.setName("xxxcube")
field26.setType("SFInt32")
field26.setAccessType("inputOutput")
field26.setValue("0")

ComposedShader25.addField(field26)
field27 = x3dpsail.field()
field27.setName("cube")
field27.setType("SFNode")
field27.setAccessType("inputOutput")
ComposedCubeMapTexture28 = x3dpsail.ComposedCubeMapTexture()
ComposedCubeMapTexture28.setUSE("texture")

field27.addChildren(ComposedCubeMapTexture28)

ComposedShader25.addField(field27)
field29 = x3dpsail.field()
field29.setName("chromaticDispertion")
field29.setType("SFVec3f")
field29.setAccessType("inputOutput")
field29.setValue("0.98 1 1.033")

ComposedShader25.addField(field29)
field30 = x3dpsail.field()
field30.setName("bias")
field30.setType("SFFloat")
field30.setAccessType("inputOutput")
field30.setValue("0.5")

ComposedShader25.addField(field30)
field31 = x3dpsail.field()
field31.setName("scale")
field31.setType("SFFloat")
field31.setAccessType("inputOutput")
field31.setValue("0.5")

ComposedShader25.addField(field31)
field32 = x3dpsail.field()
field32.setName("power")
field32.setType("SFFloat")
field32.setAccessType("inputOutput")
field32.setValue("2")

ComposedShader25.addField(field32)
ShaderPart33 = x3dpsail.ShaderPart()
ShaderPart33.setUrl(["../shaders/common.vs","https://coderextreme.net/X3DJSONLD/shaders/common.vs"])
ShaderPart33.setType("VERTEX")

ComposedShader25.addParts(ShaderPart33)
ShaderPart34 = x3dpsail.ShaderPart()
ShaderPart34.setUrl(["../shaders/gl_flowers_chromatic.fs","https://coderextreme.net/X3DJSONLD/shaders/gl_flowers_chromatic.fs"])
ShaderPart34.setType("FRAGMENT")

ComposedShader25.addParts(ShaderPart34)

Appearance16.addShaders(ComposedShader25)
ComposedShader35 = x3dpsail.ComposedShader()
ComposedShader35.setLanguage("GLSL")
field36 = x3dpsail.field()
field36.setName("xxxcube")
field36.setType("SFInt32")
field36.setAccessType("inputOutput")
field36.setValue("0")

ComposedShader35.addField(field36)
field37 = x3dpsail.field()
field37.setName("cube")
field37.setType("SFNode")
field37.setAccessType("inputOutput")
ComposedCubeMapTexture38 = x3dpsail.ComposedCubeMapTexture()
ComposedCubeMapTexture38.setUSE("texture")

field37.addChildren(ComposedCubeMapTexture38)

ComposedShader35.addField(field37)
field39 = x3dpsail.field()
field39.setName("chromaticDispertion")
field39.setType("SFVec3f")
field39.setAccessType("inputOutput")
field39.setValue("0.98 1 1.033")

ComposedShader35.addField(field39)
field40 = x3dpsail.field()
field40.setName("bias")
field40.setType("SFFloat")
field40.setAccessType("inputOutput")
field40.setValue("0.5")

ComposedShader35.addField(field40)
field41 = x3dpsail.field()
field41.setName("scale")
field41.setType("SFFloat")
field41.setAccessType("inputOutput")
field41.setValue("0.5")

ComposedShader35.addField(field41)
field42 = x3dpsail.field()
field42.setName("power")
field42.setType("SFFloat")
field42.setAccessType("inputOutput")
field42.setValue("2")

ComposedShader35.addField(field42)
ShaderPart43 = x3dpsail.ShaderPart()
ShaderPart43.setUrl(["../shaders/x3dom.vs","https://coderextreme.net/X3DJSONLD/shaders/x3dom.vs"])
ShaderPart43.setType("VERTEX")

ComposedShader35.addParts(ShaderPart43)
ShaderPart44 = x3dpsail.ShaderPart()
ShaderPart44.setUrl(["../shaders/pc_bubbles.fs","https://coderextreme.net/X3DJSONLD/shaders/pc_bubbles.fs"])
ShaderPart44.setType("FRAGMENT")

ComposedShader35.addParts(ShaderPart44)

Appearance16.addShaders(ComposedShader35)
ComposedShader45 = x3dpsail.ComposedShader()
ComposedShader45.setDEF("shader")
ComposedShader45.setLanguage("GLSL")
field46 = x3dpsail.field()
field46.setName("xxxcube")
field46.setType("SFInt32")
field46.setAccessType("inputOutput")
field46.setValue("0")

ComposedShader45.addField(field46)
field47 = x3dpsail.field()
field47.setName("cube")
field47.setType("SFNode")
field47.setAccessType("inputOutput")
ComposedCubeMapTexture48 = x3dpsail.ComposedCubeMapTexture()
ComposedCubeMapTexture48.setUSE("texture")

field47.addChildren(ComposedCubeMapTexture48)

ComposedShader45.addField(field47)
field49 = x3dpsail.field()
field49.setName("chromaticDispertion")
field49.setType("SFVec3f")
field49.setAccessType("inputOutput")
field49.setValue("0.98 1 1.033")

ComposedShader45.addField(field49)
field50 = x3dpsail.field()
field50.setName("bias")
field50.setType("SFFloat")
field50.setAccessType("inputOutput")
field50.setValue("10")

ComposedShader45.addField(field50)
field51 = x3dpsail.field()
field51.setName("scale")
field51.setType("SFFloat")
field51.setAccessType("inputOutput")
field51.setValue("10")

ComposedShader45.addField(field51)
field52 = x3dpsail.field()
field52.setName("power")
field52.setType("SFFloat")
field52.setAccessType("inputOutput")
field52.setValue("2")

ComposedShader45.addField(field52)
ShaderPart53 = x3dpsail.ShaderPart()
ShaderPart53.setUrl(["../shaders/cobweb.vs","https://coderextreme.net/X3DJSONLD/shaders/cobweb.vs"])
ShaderPart53.setType("VERTEX")

ComposedShader45.addParts(ShaderPart53)
ShaderPart54 = x3dpsail.ShaderPart()
ShaderPart54.setUrl(["../shaders/pc_bubbles.fs","https://coderextreme.net/X3DJSONLD/shaders/pc_bubbles.fs"])
ShaderPart54.setType("FRAGMENT")

ComposedShader45.addParts(ShaderPart54)

Appearance16.addShaders(ComposedShader45)

Shape15.setAppearance(Appearance16)
#<Sphere></Sphere>
IndexedFaceSet55 = x3dpsail.IndexedFaceSet()
IndexedFaceSet55.setConvex(False)
IndexedFaceSet55.setDEF("Orbit")
Coordinate56 = x3dpsail.Coordinate()
Coordinate56.setDEF("OrbitCoordinates")

IndexedFaceSet55.setCoord(Coordinate56)

Shape15.setGeometry(IndexedFaceSet55)

Transform14.addChildren(Shape15)

ProtoBody13.addChildren(Transform14)
Script57 = x3dpsail.Script()
Script57.setDEF("Bounce")
field58 = x3dpsail.field()
field58.setName("translation")
field58.setAccessType("inputOutput")
field58.setType("SFVec3f")
field58.setValue("0 0 0")

Script57.addField(field58)
field59 = x3dpsail.field()
field59.setName("velocity")
field59.setAccessType("inputOutput")
field59.setType("SFVec3f")
field59.setValue("0 0 0")

Script57.addField(field59)
field60 = x3dpsail.field()
field60.setName("set_fraction")
field60.setAccessType("inputOnly")
field60.setType("SFTime")

Script57.addField(field60)
field61 = x3dpsail.field()
field61.setName("coordinates")
field61.setAccessType("inputOutput")
field61.setType("MFVec3f")

Script57.addField(field61)
field62 = x3dpsail.field()
field62.setName("coordIndexes")
field62.setAccessType("outputOnly")
field62.setType("MFInt32")

Script57.addField(field62)
field63 = x3dpsail.field()
field63.setName("a")
field63.setType("SFFloat")
field63.setAccessType("inputOutput")
field63.setValue("0.5")

Script57.addField(field63)
field64 = x3dpsail.field()
field64.setName("b")
field64.setType("SFFloat")
field64.setAccessType("inputOutput")
field64.setValue("0.5")

Script57.addField(field64)
field65 = x3dpsail.field()
field65.setName("c")
field65.setType("SFFloat")
field65.setAccessType("inputOutput")
field65.setValue("3")

Script57.addField(field65)
field66 = x3dpsail.field()
field66.setName("d")
field66.setType("SFFloat")
field66.setAccessType("inputOutput")
field66.setValue("3")

Script57.addField(field66)
field67 = x3dpsail.field()
field67.setName("tdelta")
field67.setType("SFFloat")
field67.setAccessType("inputOutput")
field67.setValue("0.5")

Script57.addField(field67)
field68 = x3dpsail.field()
field68.setName("pdelta")
field68.setType("SFFloat")
field68.setAccessType("inputOutput")
field68.setValue("0.5")

Script57.addField(field68)

Script57.setSourceCode('''ecmascript:\n"+
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
"			    if (Math.abs(translation.x) > 10) {\n"+
"					newBubble();\n"+
"			    } else if (Math.abs(translation.y) > 10) {\n"+
"					newBubble();\n"+
"			    } else if (Math.abs(translation.z) > 10) {\n"+
"					newBubble();\n"+
"			    } else {\n"+
"					velocity = new SFVec3f(\n"+
"						velocity.x + Math.random() * 0.2 - 0.1,\n"+
"						velocity.y + Math.random() * 0.2 - 0.1,\n"+
"						velocity.z + Math.random() * 0.2 - 0.1\n"+
"					);\n"+
"			    }\n"+
"			    animate_flowers();\n"+
"			}\n"+
"\n"+
"			function initialize() {\n"+
"			     var cis = [];\n"+
"			     newBubble();\n"+
"			     resolution = 100;\n"+
"			     updateCoordinates(resolution);\n"+
"			     for ( i = 0; i < resolution-1; i++) {\n"+
"				for ( j = 0; j < resolution-1; j++) {\n"+
"				     cis.push(i*resolution+j);\n"+
"				     cis.push(i*resolution+j+1);\n"+
"				     cis.push((i+1)*resolution+j+1);\n"+
"				     cis.push((i+1)*resolution+j);\n"+
"				     cis.push(-1);\n"+
"				}\n"+
"			    }\n"+
"			     coordIndexes = new MFInt32(cis);\n"+
"			}\n"+
"\n"+
"			function updateCoordinates(resolution) {\n"+
"			     theta = 0.0;\n"+
"			     phi = 0.0;\n"+
"			     delta = (2 * 3.141592653) / (resolution-1);\n"+
"			     var crds = [];\n"+
"			     for ( i = 0; i < resolution; i++) {\n"+
"				for ( j = 0; j < resolution; j++) {\n"+
"					rho = a + b * Math.cos(c * theta) * Math.cos(d * phi);\n"+
"					crds.push(new SFVec3f(\n"+
"						rho * Math.cos(phi) * Math.cos(theta),\n"+
"						rho * Math.cos(phi) * Math.sin(theta),\n"+
"						rho * Math.sin(phi)\n"+
"					));\n"+
"					theta += delta;\n"+
"				}\n"+
"				phi += delta;\n"+
"				coordinates = new MFVec3f(crds);\n"+
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
"			}''')

ProtoBody13.addChildren(Script57)
TimeSensor69 = x3dpsail.TimeSensor()
TimeSensor69.setDEF("TourTime")
TimeSensor69.setCycleInterval(0.15)
TimeSensor69.setLoop(True)

ProtoBody13.addChildren(TimeSensor69)
TimeSensor70 = x3dpsail.TimeSensor()
TimeSensor70.setDEF("SongTime")
TimeSensor70.setLoop(True)

ProtoBody13.addChildren(TimeSensor70)
Sound71 = x3dpsail.Sound()
Sound71.setMaxBack(100)
Sound71.setMaxFront(100)
Sound71.setMinBack(20)
Sound71.setMinFront(20)
AudioClip72 = x3dpsail.AudioClip()
AudioClip72.setDEF("AudioClip")
AudioClip72.setDescription("Chandubabamusic #1")
AudioClip72.setUrl(["../resources/chandubabamusic1.wav"])

Sound71.setSource(AudioClip72)

ProtoBody13.addChildren(Sound71)
ROUTE73 = x3dpsail.ROUTE()
ROUTE73.setFromField("cycleTime")
ROUTE73.setFromNode("SongTime")
ROUTE73.setToField("startTime")
ROUTE73.setToNode("AudioClip")

ProtoBody13.addChildren(ROUTE73)
ROUTE74 = x3dpsail.ROUTE()
ROUTE74.setFromNode("TourTime")
ROUTE74.setFromField("cycleTime")
ROUTE74.setToNode("Bounce")
ROUTE74.setToField("set_fraction")

ProtoBody13.addChildren(ROUTE74)
ROUTE75 = x3dpsail.ROUTE()
ROUTE75.setFromNode("Bounce")
ROUTE75.setFromField("translation")
ROUTE75.setToNode("transform")
ROUTE75.setToField("set_translation")

ProtoBody13.addChildren(ROUTE75)
#<ROUTE fromField=\"coordIndexes\" fromNode=\"Bounce\" toField=\"set_coordIndex\" toNode=\"Orbit\"/> <ROUTE fromField=\"coordinates\" fromNode=\"Bounce\" toField=\"set_point\" toNode=\"OrbitCoordinates\"/>

ProtoDeclare12.setProtoBody(ProtoBody13)

Scene9.addChildren(ProtoDeclare12)
Transform76 = x3dpsail.Transform()
ProtoInstance77 = x3dpsail.ProtoInstance()
ProtoInstance77.setName("flower")

Transform76.addChildren(ProtoInstance77)
#<ProtoInstance name=\"flower\"/> <ProtoInstance name=\"flower\"/>

Scene9.addChildren(Transform76)

X3D0.setScene(Scene9)
X3D0.toFileX3D("././flowers_RoundTrip.x3d")
