print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Immersive"
X3D0.version = "4.0"
head1 = x3d.head()
component2 = x3d.component()
component2.name = "Scripting"
component2.level = 1

head1.children.append(component2)
component3 = x3d.component()
component3.name = "Shaders"
component3.level = 1

head1.children.append(component3)
component4 = x3d.component()
component4.name = "CubeMapTexturing"
component4.level = 1

head1.children.append(component4)
component5 = x3d.component()
component5.name = "Texturing"
component5.level = 1

head1.children.append(component5)
component6 = x3d.component()
component6.name = "Rendering"
component6.level = 1

head1.children.append(component6)
component7 = x3d.component()
component7.name = "Shape"
component7.level = 4

head1.children.append(component7)
component8 = x3d.component()
component8.name = "Grouping"
component8.level = 3

head1.children.append(component8)
meta9 = x3d.meta()
meta9.name = "title"
meta9.content = "flowers.x3d"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "creator"
meta10.content = "John Carlson"

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.name = "description"
meta11.content = "5 or more prismatic flowers"

head1.children.append(meta11)
meta12 = x3d.meta()
meta12.name = "generator"
meta12.content = "X3D-Edit, https://savage.nps.edu/X3D-Edit"

head1.children.append(meta12)
meta13 = x3d.meta()
meta13.name = "identifier"
meta13.content = "https://coderextreme.net/X3DJSONLD/flowers.x3d"

head1.children.append(meta13)

X3D0.head = head1
Scene14 = x3d.Scene()
NavigationInfo15 = x3d.NavigationInfo()

Scene14.children.append(NavigationInfo15)
#Images courtesy of Paul Debevec's Light Probe Image Gallery
Background16 = x3d.Background()
Background16.backUrl = ["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"]
Background16.bottomUrl = ["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"]
Background16.frontUrl = ["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"]
Background16.leftUrl = ["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"]
Background16.rightUrl = ["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"]
Background16.topUrl = ["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"]

Scene14.children.append(Background16)
ProtoDeclare17 = x3d.ProtoDeclare()
ProtoDeclare17.name = "flower"
ProtoBody18 = x3d.ProtoBody()
Transform19 = x3d.Transform()
Transform19.DEF = "animate_transform"
Shape20 = x3d.Shape()
Appearance21 = x3d.Appearance()
Material22 = x3d.Material()
Material22.diffuseColor = [0.7,0.7,0.7]
Material22.specularColor = [0.5,0.5,0.5]

Appearance21.material = Material22
ComposedCubeMapTexture23 = x3d.ComposedCubeMapTexture()
ComposedCubeMapTexture23.DEF = "texture"
ImageTexture24 = x3d.ImageTexture()
ImageTexture24.url = ["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"]

ComposedCubeMapTexture23.backTexture = ImageTexture24
ImageTexture25 = x3d.ImageTexture()
ImageTexture25.url = ["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"]

ComposedCubeMapTexture23.bottomTexture = ImageTexture25
ImageTexture26 = x3d.ImageTexture()
ImageTexture26.url = ["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"]

ComposedCubeMapTexture23.frontTexture.append(ImageTexture26)
ImageTexture27 = x3d.ImageTexture()
ImageTexture27.url = ["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"]

ComposedCubeMapTexture23.leftTexture = ImageTexture27
ImageTexture28 = x3d.ImageTexture()
ImageTexture28.url = ["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"]

ComposedCubeMapTexture23.rightTexture.append(ImageTexture28)
ImageTexture29 = x3d.ImageTexture()
ImageTexture29.url = ["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"]

ComposedCubeMapTexture23.topTexture.append(ImageTexture29)

Appearance21.texture = ComposedCubeMapTexture23
ComposedShader30 = x3d.ComposedShader()
ComposedShader30.DEF = "x3dom"
ComposedShader30.language = "GLSL"
field31 = x3d.field()
field31.name = "cube"
field31.type = "SFInt32"
field31.accessType = "inputOutput"
field31.value = 0

ComposedShader30.field.append(field31)
field32 = x3d.field()
field32.name = "chromaticDispertion"
field32.accessType = "initializeOnly"
field32.type = "SFVec3f"
field32.value = [0.98,1,1.033]

ComposedShader30.field.append(field32)
field33 = x3d.field()
field33.name = "bias"
field33.type = "SFFloat"
field33.accessType = "inputOutput"
field33.value = 0.5

ComposedShader30.field.append(field33)
field34 = x3d.field()
field34.name = "scale"
field34.type = "SFFloat"
field34.accessType = "inputOutput"
field34.value = 0.5

ComposedShader30.field.append(field34)
field35 = x3d.field()
field35.name = "power"
field35.type = "SFFloat"
field35.accessType = "inputOutput"
field35.value = 2

ComposedShader30.field.append(field35)
field36 = x3d.field()
field36.name = "a"
field36.type = "SFFloat"
field36.accessType = "inputOutput"
field36.value = 10

ComposedShader30.field.append(field36)
field37 = x3d.field()
field37.name = "b"
field37.type = "SFFloat"
field37.accessType = "inputOutput"
field37.value = 1

ComposedShader30.field.append(field37)
field38 = x3d.field()
field38.name = "c"
field38.type = "SFFloat"
field38.accessType = "inputOutput"
field38.value = 20

ComposedShader30.field.append(field38)
field39 = x3d.field()
field39.name = "d"
field39.type = "SFFloat"
field39.accessType = "inputOutput"
field39.value = 20

ComposedShader30.field.append(field39)
field40 = x3d.field()
field40.name = "tdelta"
field40.type = "SFFloat"
field40.accessType = "inputOutput"
field40.value = 0

ComposedShader30.field.append(field40)
field41 = x3d.field()
field41.name = "pdelta"
field41.type = "SFFloat"
field41.accessType = "inputOutput"
field41.value = 0

ComposedShader30.field.append(field41)
#<field name='cube' type='SFNode' accessType=\"inputOutput\"> <ComposedCubeMapTexture USE=\"texture\"/> </field>
ShaderPart42 = x3d.ShaderPart()
ShaderPart42.url = ["../shaders/x3dom_flowers_chromatic.vs","https://coderextreme.net/X3DJSONLD/src/main/shaders/x3dom_flowers_chromatic.vs"]
ShaderPart42.type = "VERTEX"

ComposedShader30.parts.append(ShaderPart42)
ShaderPart43 = x3d.ShaderPart()
ShaderPart43.url = ["../shaders/common.fs","https://coderextreme.net/X3DJSONLD/src/main/shaders/common.fs"]
ShaderPart43.type = "FRAGMENT"

ComposedShader30.parts.append(ShaderPart43)

Appearance21.shaders.append(ComposedShader30)
ComposedShader44 = x3d.ComposedShader()
ComposedShader44.DEF = "x_ite"
ComposedShader44.language = "GLSL"
field45 = x3d.field()
field45.name = "cube"
field45.type = "SFNode"
field45.accessType = "inputOutput"
ComposedCubeMapTexture46 = x3d.ComposedCubeMapTexture()
ComposedCubeMapTexture46.USE = "texture"

field45.children.append(ComposedCubeMapTexture46)

ComposedShader44.field.append(field45)
field47 = x3d.field()
field47.name = "chromaticDispertion"
field47.accessType = "initializeOnly"
field47.type = "SFVec3f"
field47.value = [0.98,1,1.033]

ComposedShader44.field.append(field47)
field48 = x3d.field()
field48.name = "bias"
field48.type = "SFFloat"
field48.accessType = "inputOnly"
field48.value = 0.5

ComposedShader44.field.append(field48)
field49 = x3d.field()
field49.name = "scale"
field49.type = "SFFloat"
field49.accessType = "inputOnly"
field49.value = 0.5

ComposedShader44.field.append(field49)
field50 = x3d.field()
field50.name = "power"
field50.type = "SFFloat"
field50.accessType = "inputOnly"
field50.value = 2

ComposedShader44.field.append(field50)
field51 = x3d.field()
field51.name = "a"
field51.type = "SFFloat"
field51.accessType = "inputOnly"
field51.value = 10

ComposedShader44.field.append(field51)
field52 = x3d.field()
field52.name = "b"
field52.type = "SFFloat"
field52.accessType = "inputOnly"
field52.value = 1

ComposedShader44.field.append(field52)
field53 = x3d.field()
field53.name = "c"
field53.type = "SFFloat"
field53.accessType = "inputOnly"
field53.value = 20

ComposedShader44.field.append(field53)
field54 = x3d.field()
field54.name = "d"
field54.type = "SFFloat"
field54.accessType = "inputOnly"
field54.value = 20

ComposedShader44.field.append(field54)
field55 = x3d.field()
field55.name = "tdelta"
field55.type = "SFFloat"
field55.accessType = "inputOnly"
field55.value = 0

ComposedShader44.field.append(field55)
field56 = x3d.field()
field56.name = "pdelta"
field56.type = "SFFloat"
field56.accessType = "inputOnly"
field56.value = 0

ComposedShader44.field.append(field56)
ShaderPart57 = x3d.ShaderPart()
ShaderPart57.url = ["../shaders/x_ite_flowers_chromatic.vs","https://coderextreme.net/X3DJSONLD/src/main/shaders/x_ite_flowers_chromatic.vs"]
ShaderPart57.type = "VERTEX"

ComposedShader44.parts.append(ShaderPart57)
ShaderPart58 = x3d.ShaderPart()
ShaderPart58.url = ["../shaders/x_ite.fs","https://coderextreme.net/X3DJSONLD/src/main/shaders/x_ite.fs"]
ShaderPart58.type = "FRAGMENT"

ComposedShader44.parts.append(ShaderPart58)

Appearance21.shaders.append(ComposedShader44)

Shape20.appearance = Appearance21
Sphere59 = x3d.Sphere()

Shape20.geometry = Sphere59

Transform19.children.append(Shape20)

ProtoBody18.children.append(Transform19)
Script60 = x3d.Script()
Script60.DEF = "Animate"
field61 = x3d.field()
field61.name = "translation"
field61.accessType = "inputOutput"
field61.type = "SFVec3f"
field61.value = [0,0,0]

Script60.field.append(field61)
field62 = x3d.field()
field62.name = "velocity"
field62.accessType = "inputOutput"
field62.type = "SFVec3f"
field62.value = [0,0,0]

Script60.field.append(field62)
field63 = x3d.field()
field63.name = "set_fraction"
field63.accessType = "inputOnly"
field63.type = "SFFloat"

Script60.field.append(field63)
field64 = x3d.field()
field64.name = "a"
field64.type = "SFFloat"
field64.accessType = "inputOutput"
field64.value = 0.5

Script60.field.append(field64)
field65 = x3d.field()
field65.name = "b"
field65.type = "SFFloat"
field65.accessType = "inputOutput"
field65.value = 0.5

Script60.field.append(field65)
field66 = x3d.field()
field66.name = "c"
field66.type = "SFFloat"
field66.accessType = "inputOutput"
field66.value = 3

Script60.field.append(field66)
field67 = x3d.field()
field67.name = "d"
field67.type = "SFFloat"
field67.accessType = "inputOutput"
field67.value = 3

Script60.field.append(field67)
field68 = x3d.field()
field68.name = "tdelta"
field68.type = "SFFloat"
field68.accessType = "inputOutput"
field68.value = 0.5

Script60.field.append(field68)
field69 = x3d.field()
field69.name = "pdelta"
field69.type = "SFFloat"
field69.accessType = "inputOutput"
field69.value = 0.5

Script60.field.append(field69)

Script60.sourceCode = '''ecmascript:\n"+
"\n"+
"			function initialize() {\n"+
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
"			    for (var j = 0; j <= 2; j++) {\n"+
"				    if (Math.abs(translation.x) > 10) {\n"+
"					initialize();\n"+
"				    } else if (Math.abs(translation.y) > 10) {\n"+
"					initialize();\n"+
"				    } else if (Math.abs(translation.z) > 10) {\n"+
"					initialize();\n"+
"				    } else {\n"+
"					velocity.x += Math.random() * 0.2 - 0.1;\n"+
"					velocity.y += Math.random() * 0.2 - 0.1;\n"+
"					velocity.z += Math.random() * 0.2 - 0.1;\n"+
"				    }\n"+
"			    }\n"+
"			    animate_flowers();\n"+
"			}\n"+
"\n"+
"			function animate_flowers(fraction, eventTime) {\n"+
"				var choice = Math.floor(Math.random() * 4);\n"+
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
"				tdelta = tdelta + 0.5;\n"+
"				pdelta = pdelta + 0.5;\n"+
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
"			}'''

ProtoBody18.children.append(Script60)
TimeSensor70 = x3d.TimeSensor()
TimeSensor70.DEF = "TourTime"
TimeSensor70.cycleInterval = 5
TimeSensor70.loop = True

ProtoBody18.children.append(TimeSensor70)
ROUTE71 = x3d.ROUTE()
ROUTE71.fromNode = "TourTime"
ROUTE71.fromField = "fraction_changed"
ROUTE71.toNode = "Animate"
ROUTE71.toField = "set_fraction"

ProtoBody18.children.append(ROUTE71)
ROUTE72 = x3d.ROUTE()
ROUTE72.fromNode = "Animate"
ROUTE72.fromField = "translation_changed"
ROUTE72.toNode = "animate_transform"
ROUTE72.toField = "set_translation"

ProtoBody18.children.append(ROUTE72)
ROUTE73 = x3d.ROUTE()
ROUTE73.fromNode = "Animate"
ROUTE73.fromField = "a"
ROUTE73.toNode = "x_ite"
ROUTE73.toField = "a"

ProtoBody18.children.append(ROUTE73)
ROUTE74 = x3d.ROUTE()
ROUTE74.fromNode = "Animate"
ROUTE74.fromField = "b"
ROUTE74.toNode = "x_ite"
ROUTE74.toField = "b"

ProtoBody18.children.append(ROUTE74)
ROUTE75 = x3d.ROUTE()
ROUTE75.fromNode = "Animate"
ROUTE75.fromField = "c"
ROUTE75.toNode = "x_ite"
ROUTE75.toField = "c"

ProtoBody18.children.append(ROUTE75)
ROUTE76 = x3d.ROUTE()
ROUTE76.fromNode = "Animate"
ROUTE76.fromField = "d"
ROUTE76.toNode = "x_ite"
ROUTE76.toField = "d"

ProtoBody18.children.append(ROUTE76)
ROUTE77 = x3d.ROUTE()
ROUTE77.fromNode = "Animate"
ROUTE77.fromField = "pdelta"
ROUTE77.toNode = "x_ite"
ROUTE77.toField = "pdelta"

ProtoBody18.children.append(ROUTE77)
ROUTE78 = x3d.ROUTE()
ROUTE78.fromNode = "Animate"
ROUTE78.fromField = "tdelta"
ROUTE78.toNode = "x_ite"
ROUTE78.toField = "tdelta"

ProtoBody18.children.append(ROUTE78)
ROUTE79 = x3d.ROUTE()
ROUTE79.fromNode = "Animate"
ROUTE79.fromField = "a"
ROUTE79.toNode = "x3dom"
ROUTE79.toField = "a"

ProtoBody18.children.append(ROUTE79)
ROUTE80 = x3d.ROUTE()
ROUTE80.fromNode = "Animate"
ROUTE80.fromField = "b"
ROUTE80.toNode = "x3dom"
ROUTE80.toField = "b"

ProtoBody18.children.append(ROUTE80)
ROUTE81 = x3d.ROUTE()
ROUTE81.fromNode = "Animate"
ROUTE81.fromField = "c"
ROUTE81.toNode = "x3dom"
ROUTE81.toField = "c"

ProtoBody18.children.append(ROUTE81)
ROUTE82 = x3d.ROUTE()
ROUTE82.fromNode = "Animate"
ROUTE82.fromField = "d"
ROUTE82.toNode = "x3dom"
ROUTE82.toField = "d"

ProtoBody18.children.append(ROUTE82)
ROUTE83 = x3d.ROUTE()
ROUTE83.fromNode = "Animate"
ROUTE83.fromField = "pdelta"
ROUTE83.toNode = "x3dom"
ROUTE83.toField = "pdelta"

ProtoBody18.children.append(ROUTE83)
ROUTE84 = x3d.ROUTE()
ROUTE84.fromNode = "Animate"
ROUTE84.fromField = "tdelta"
ROUTE84.toNode = "x3dom"
ROUTE84.toField = "tdelta"

ProtoBody18.children.append(ROUTE84)

ProtoDeclare17.ProtoBody = ProtoBody18

Scene14.children.append(ProtoDeclare17)
ProtoInstance85 = x3d.ProtoInstance()
ProtoInstance85.name = "flower"

Scene14.children.append(ProtoInstance85)
ProtoInstance86 = x3d.ProtoInstance()
ProtoInstance86.name = "flower"

Scene14.children.append(ProtoInstance86)
ProtoInstance87 = x3d.ProtoInstance()
ProtoInstance87.name = "flower"

Scene14.children.append(ProtoInstance87)

X3D0.Scene = Scene14
f = open("././flowers_RoundTrip.x3d", "w")
f.write(X3D0.XML())
f.close()
