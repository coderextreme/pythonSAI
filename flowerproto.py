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
meta8.content = "flowerproto.x3d"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "creator"
meta9.content = "John Carlson"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "description"
meta10.content = "A flower proto with configurable shaders"

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.name = "generator"
meta11.content = "X3D-Edit, https://savage.nps.edu/X3D-Edit"

head1.children.append(meta11)
meta12 = x3d.meta()
meta12.name = "identifier"
meta12.content = "https://coderextreme.net/X3DJSONLD/flowerproto.x3d"

head1.children.append(meta12)

X3D0.head = head1
Scene13 = x3d.Scene()
ProtoDeclare14 = x3d.ProtoDeclare()
ProtoDeclare14.name = "FlowerProto"
ProtoInterface15 = x3d.ProtoInterface()
field16 = x3d.field()
field16.name = "vertex"
field16.accessType = "inputOutput"
field16.type = "MFString"
field16.value = ["../shaders/gl_flowers_chromatic.vs"]

ProtoInterface15.field.append(field16)
field17 = x3d.field()
field17.name = "fragment"
field17.accessType = "inputOutput"
field17.type = "MFString"
field17.value = ["../shaders/pc_flowers.fs"]

ProtoInterface15.field.append(field17)

ProtoDeclare14.ProtoInterface = ProtoInterface15
ProtoBody18 = x3d.ProtoBody()
Transform19 = x3d.Transform()
Transform19.DEF = "transform"
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

ComposedCubeMapTexture23.backTexture.append(ImageTexture24)
ImageTexture25 = x3d.ImageTexture()
ImageTexture25.url = ["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"]

ComposedCubeMapTexture23.bottomTexture.append(ImageTexture25)
ImageTexture26 = x3d.ImageTexture()
ImageTexture26.url = ["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"]

ComposedCubeMapTexture23.frontTexture.append(ImageTexture26)
ImageTexture27 = x3d.ImageTexture()
ImageTexture27.url = ["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"]

ComposedCubeMapTexture23.leftTexture.append(ImageTexture27)
ImageTexture28 = x3d.ImageTexture()
ImageTexture28.url = ["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"]

ComposedCubeMapTexture23.rightTexture.append(ImageTexture28)
ImageTexture29 = x3d.ImageTexture()
ImageTexture29.url = ["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"]

ComposedCubeMapTexture23.topTexture.append(ImageTexture29)

Appearance21.texture = ComposedCubeMapTexture23
ComposedShader30 = x3d.ComposedShader()
ComposedShader30.DEF = "shader"
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
ShaderPart42.type = "VERTEX"
IS43 = x3d.IS()
connect44 = x3d.connect()
connect44.nodeField = "url"
connect44.protoField = "vertex"

IS43.connect.append(connect44)

ShaderPart42.IS = IS43

ComposedShader30.parts.append(ShaderPart42)
ShaderPart45 = x3d.ShaderPart()
ShaderPart45.type = "FRAGMENT"
IS46 = x3d.IS()
connect47 = x3d.connect()
connect47.nodeField = "url"
connect47.protoField = "fragment"

IS46.connect.append(connect47)

ShaderPart45.IS = IS46

ComposedShader30.parts.append(ShaderPart45)

Appearance21.shaders.append(ComposedShader30)

Shape20.appearance = Appearance21
Sphere48 = x3d.Sphere()

Shape20.geometry = Sphere48

Transform19.children.append(Shape20)
Script49 = x3d.Script()
Script49.DEF = "Animate"
field50 = x3d.field()
field50.name = "translation"
field50.accessType = "inputOutput"
field50.type = "SFVec3f"
field50.value = [0,0,0]

Script49.field.append(field50)
field51 = x3d.field()
field51.name = "velocity"
field51.accessType = "inputOutput"
field51.type = "SFVec3f"
field51.value = [0,0,0]

Script49.field.append(field51)
field52 = x3d.field()
field52.name = "set_fraction"
field52.accessType = "inputOnly"
field52.type = "SFFloat"

Script49.field.append(field52)
field53 = x3d.field()
field53.name = "a"
field53.type = "SFFloat"
field53.accessType = "inputOutput"
field53.value = 0.5

Script49.field.append(field53)
field54 = x3d.field()
field54.name = "b"
field54.type = "SFFloat"
field54.accessType = "inputOutput"
field54.value = 0.5

Script49.field.append(field54)
field55 = x3d.field()
field55.name = "c"
field55.type = "SFFloat"
field55.accessType = "inputOutput"
field55.value = 3

Script49.field.append(field55)
field56 = x3d.field()
field56.name = "d"
field56.type = "SFFloat"
field56.accessType = "inputOutput"
field56.value = 3

Script49.field.append(field56)
field57 = x3d.field()
field57.name = "tdelta"
field57.type = "SFFloat"
field57.accessType = "inputOutput"
field57.value = 0.5

Script49.field.append(field57)
field58 = x3d.field()
field58.name = "pdelta"
field58.type = "SFFloat"
field58.accessType = "inputOutput"
field58.value = 0.5

Script49.field.append(field58)

Script49.sourceCode = '''ecmascript:\n"+
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
"				tdelta += 0.5;\n"+
"				pdelta += 0.5;\n"+
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

Transform19.children.append(Script49)
TimeSensor59 = x3d.TimeSensor()
TimeSensor59.DEF = "TourTime"
TimeSensor59.cycleInterval = 5
TimeSensor59.loop = True

Transform19.children.append(TimeSensor59)
ROUTE60 = x3d.ROUTE()
ROUTE60.fromNode = "TourTime"
ROUTE60.fromField = "fraction_changed"
ROUTE60.toNode = "Animate"
ROUTE60.toField = "set_fraction"

Transform19.children.append(ROUTE60)
ROUTE61 = x3d.ROUTE()
ROUTE61.fromNode = "Animate"
ROUTE61.fromField = "translation_changed"
ROUTE61.toNode = "transform"
ROUTE61.toField = "set_translation"

Transform19.children.append(ROUTE61)
ROUTE62 = x3d.ROUTE()
ROUTE62.fromNode = "Animate"
ROUTE62.fromField = "a"
ROUTE62.toNode = "shader"
ROUTE62.toField = "a"

Transform19.children.append(ROUTE62)
ROUTE63 = x3d.ROUTE()
ROUTE63.fromNode = "Animate"
ROUTE63.fromField = "b"
ROUTE63.toNode = "shader"
ROUTE63.toField = "b"

Transform19.children.append(ROUTE63)
ROUTE64 = x3d.ROUTE()
ROUTE64.fromNode = "Animate"
ROUTE64.fromField = "c"
ROUTE64.toNode = "shader"
ROUTE64.toField = "c"

Transform19.children.append(ROUTE64)
ROUTE65 = x3d.ROUTE()
ROUTE65.fromNode = "Animate"
ROUTE65.fromField = "d"
ROUTE65.toNode = "shader"
ROUTE65.toField = "d"

Transform19.children.append(ROUTE65)
ROUTE66 = x3d.ROUTE()
ROUTE66.fromNode = "Animate"
ROUTE66.fromField = "tdelta"
ROUTE66.toNode = "shader"
ROUTE66.toField = "tdelta"

Transform19.children.append(ROUTE66)
ROUTE67 = x3d.ROUTE()
ROUTE67.fromNode = "Animate"
ROUTE67.fromField = "pdelta"
ROUTE67.toNode = "shader"
ROUTE67.toField = "pdelta"

Transform19.children.append(ROUTE67)

ProtoBody18.children.append(Transform19)

ProtoDeclare14.ProtoBody = ProtoBody18

Scene13.children.append(ProtoDeclare14)

X3D0.Scene = Scene13
f = open("././flowerproto_RoundTrip.x3d", "w")
f.write(X3D0.XML())
f.close()
