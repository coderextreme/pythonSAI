print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Immersive"
X3D0.version = "4.0"
head1 = x3d.head()
component2 = x3d.component()
component2.name = "Shaders"
component2.level = 1

head1.children.append(component2)
component3 = x3d.component()
component3.name = "CubeMapTexturing"
component3.level = 1

head1.children.append(component3)
component4 = x3d.component()
component4.name = "Texturing"
component4.level = 1

head1.children.append(component4)
component5 = x3d.component()
component5.name = "Rendering"
component5.level = 1

head1.children.append(component5)
component6 = x3d.component()
component6.name = "Shape"
component6.level = 4

head1.children.append(component6)
component7 = x3d.component()
component7.name = "Grouping"
component7.level = 3

head1.children.append(component7)
meta8 = x3d.meta()
meta8.name = "title"
meta8.content = "flowers4.x3d"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "creator"
meta9.content = "John Carlson"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "generator"
meta10.content = "manual"

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.name = "identifier"
meta11.content = "https://coderextreme.net/X3DJSONLD/flowers4.x3d"

head1.children.append(meta11)
meta12 = x3d.meta()
meta12.name = "description"
meta12.content = "an animated flower"

head1.children.append(meta12)

X3D0.head = head1
Scene13 = x3d.Scene()
NavigationInfo14 = x3d.NavigationInfo()

Scene13.children.append(NavigationInfo14)
Background15 = x3d.Background()
Background15.backUrl = ["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"]
Background15.bottomUrl = ["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"]
Background15.frontUrl = ["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"]
Background15.leftUrl = ["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"]
Background15.rightUrl = ["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"]
Background15.topUrl = ["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"]

Scene13.children.append(Background15)
Transform16 = x3d.Transform()
Transform16.DEF = "transform"
Shape17 = x3d.Shape()
Appearance18 = x3d.Appearance()
Material19 = x3d.Material()
Material19.diffuseColor = [0.7,0.7,0.7]
Material19.specularColor = [0.5,0.5,0.5]

Appearance18.material = Material19
ComposedCubeMapTexture20 = x3d.ComposedCubeMapTexture()
ImageTexture21 = x3d.ImageTexture()
ImageTexture21.url = ["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"]

ComposedCubeMapTexture20.backTexture.append(ImageTexture21)
ImageTexture22 = x3d.ImageTexture()
ImageTexture22.url = ["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"]

ComposedCubeMapTexture20.bottomTexture.append(ImageTexture22)
ImageTexture23 = x3d.ImageTexture()
ImageTexture23.url = ["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"]

ComposedCubeMapTexture20.frontTexture.append(ImageTexture23)
ImageTexture24 = x3d.ImageTexture()
ImageTexture24.url = ["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"]

ComposedCubeMapTexture20.leftTexture.append(ImageTexture24)
ImageTexture25 = x3d.ImageTexture()
ImageTexture25.url = ["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"]

ComposedCubeMapTexture20.rightTexture.append(ImageTexture25)
ImageTexture26 = x3d.ImageTexture()
ImageTexture26.url = ["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"]

ComposedCubeMapTexture20.topTexture.append(ImageTexture26)

Appearance18.texture = ComposedCubeMapTexture20
ComposedShader27 = x3d.ComposedShader()
ComposedShader27.DEF = "shader"
ComposedShader27.language = "GLSL"
field28 = x3d.field()
field28.name = "cube"
field28.type = "SFInt32"
field28.accessType = "inputOutput"
field28.value = 0

ComposedShader27.field.append(field28)
field29 = x3d.field()
field29.name = "chromaticDispertion"
field29.accessType = "inputOutput"
field29.type = "SFVec3f"
field29.value = [0.98,1,1.033]

ComposedShader27.field.append(field29)
field30 = x3d.field()
field30.name = "bias"
field30.type = "SFFloat"
field30.accessType = "inputOutput"
field30.value = 0.5

ComposedShader27.field.append(field30)
field31 = x3d.field()
field31.name = "scale"
field31.type = "SFFloat"
field31.accessType = "inputOutput"
field31.value = 0.5

ComposedShader27.field.append(field31)
field32 = x3d.field()
field32.name = "power"
field32.type = "SFFloat"
field32.accessType = "inputOutput"
field32.value = 2

ComposedShader27.field.append(field32)
ShaderPart33 = x3d.ShaderPart()
ShaderPart33.url = ["../shaders/x3dom.vs","https://coderextreme.net/X3DJSONLD/src/main/shaders/x3dom.vs"]
ShaderPart33.type = "VERTEX"

ComposedShader27.parts.append(ShaderPart33)
ShaderPart34 = x3d.ShaderPart()
ShaderPart34.url = ["../shaders/pc_bubbles.fs","https://coderextreme.net/X3DJSONLD/src/main/shaders/pc_bubbles.fs"]
ShaderPart34.type = "FRAGMENT"

ComposedShader27.parts.append(ShaderPart34)

Appearance18.shaders.append(ComposedShader27)

Shape17.appearance = Appearance18
#<Sphere>
IndexedFaceSet35 = x3d.IndexedFaceSet()
IndexedFaceSet35.convex = False
IndexedFaceSet35.DEF = "Orbit"
Coordinate36 = x3d.Coordinate()
Coordinate36.DEF = "OrbitCoordinates"

IndexedFaceSet35.coord.append(Coordinate36)

Shape17.geometry = IndexedFaceSet35

Transform16.children.append(Shape17)

Scene13.children.append(Transform16)
Script37 = x3d.Script()
Script37.DEF = "OrbitScript"
field38 = x3d.field()
field38.name = "set_fraction"
field38.accessType = "inputOnly"
field38.type = "SFFloat"

Script37.field.append(field38)
field39 = x3d.field()
field39.name = "coordinates"
field39.accessType = "inputOutput"
field39.type = "MFVec3f"

Script37.field.append(field39)
field40 = x3d.field()
field40.name = "coordIndexes"
field40.accessType = "outputOnly"
field40.type = "MFInt32"

Script37.field.append(field40)

Script37.sourceCode = '''ecmascript:\n"+
"\n"+
"var e = 5;\n"+
"var f = 5;\n"+
"var g = 5;\n"+
"var h = 5;\n"+
"\n"+
"function initialize() {\n"+
"     var resolution = 100;\n"+
"     updateCoordinates(resolution);\n"+
"     var cis = [];\n"+
"     for ( i = 0; i < resolution-1; i++) {\n"+
"     	for ( j = 0; j < resolution-1; j++) {\n"+
"	     cis.push(i*resolution+j);\n"+
"	     cis.push(i*resolution+j+1);\n"+
"	     cis.push((i+1)*resolution+j+1);\n"+
"	     cis.push((i+1)*resolution+j);\n"+
"	     cis.push(-1);\n"+
"	}\n"+
"    }\n"+
"    coordIndexes = new MFInt32(cis);\n"+
"}\n"+
"\n"+
"function updateCoordinates(resolution) {\n"+
"     var theta = 0.0;\n"+
"     var phi = 0.0;\n"+
"     var delta = (2 * 3.141592653) / (resolution-1);\n"+
"     var crds = [];\n"+
"     for ( i = 0; i < resolution; i++) {\n"+
"     	for ( j = 0; j < resolution; j++) {\n"+
"		var rho = e + f * Math.cos(g * theta) * Math.cos(h * phi);\n"+
"		crds.push(new SFVec3f(\n"+
"			rho * Math.cos(phi) * Math.cos(theta),\n"+
"			rho * Math.cos(phi) * Math.sin(theta),\n"+
"			rho * Math.sin(phi)\n"+
"		));\n"+
"		theta += delta;\n"+
"	}\n"+
"	phi += delta;\n"+
"     }\n"+
"     coordinates = new MFVec3f(crds);\n"+
"}\n"+
"\n"+
"function set_fraction(fraction, eventTime) {\n"+
"	var choice = Math.floor(Math.random() * 4);\n"+
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
"	var resolution = 100;\n"+
"	updateCoordinates(resolution);\n"+
"}'''

Scene13.children.append(Script37)
TimeSensor41 = x3d.TimeSensor()
TimeSensor41.DEF = "Clock"
TimeSensor41.cycleInterval = 16
TimeSensor41.loop = True

Scene13.children.append(TimeSensor41)
ROUTE42 = x3d.ROUTE()
ROUTE42.fromField = "coordIndexes"
ROUTE42.fromNode = "OrbitScript"
ROUTE42.toField = "set_coordIndex"
ROUTE42.toNode = "Orbit"

Scene13.children.append(ROUTE42)
ROUTE43 = x3d.ROUTE()
ROUTE43.fromField = "coordinates"
ROUTE43.fromNode = "OrbitScript"
ROUTE43.toField = "set_point"
ROUTE43.toNode = "OrbitCoordinates"

Scene13.children.append(ROUTE43)
ROUTE44 = x3d.ROUTE()
ROUTE44.fromField = "fraction_changed"
ROUTE44.fromNode = "Clock"
ROUTE44.toField = "set_fraction"
ROUTE44.toNode = "OrbitScript"

Scene13.children.append(ROUTE44)

X3D0.Scene = Scene13
f = open("././flowers4_RoundTrip.x3d", "w")
f.write(X3D0.XML())
f.close()
