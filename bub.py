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
meta8.content = "bub.x3d"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "creator"
meta9.content = "John Carlson"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "description"
meta10.content = "3 prismatic spheres"

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.name = "generator"
meta11.content = "X3D-Edit, https://savage.nps.edu/X3D-Edit"

head1.children.append(meta11)
meta12 = x3d.meta()
meta12.name = "identifier"
meta12.content = "https://coderextreme.net/X3DJSONLD/bub.x3d"

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
Viewpoint16 = x3d.Viewpoint()
Viewpoint16.position = [0,0,20]
Viewpoint16.description = "Look at the bubbles flying"

Scene13.children.append(Viewpoint16)
ProtoDeclare17 = x3d.ProtoDeclare()
ProtoDeclare17.name = "Bubble"
ProtoBody18 = x3d.ProtoBody()
Transform19 = x3d.Transform()
Transform19.DEF = "transform"
Shape20 = x3d.Shape()
Shape20.DEF = "myShape"
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
#<ComposedShader DEF='gl' language=\"GLSL\"> <field name='cube' type='SFInt32' accessType=\"inputOutput\" value='0'/> <field name='chromaticDispertion' type='SFVec3f' accessType=\"inputOutput\" value='0.98 1.0 1.033'/> <field name='bias' type='SFFloat' accessType=\"inputOutput\" value='0.5'/> <field name='scale' type='SFFloat' accessType=\"inputOutput\" value='0.5'/> <field name='power' type='SFFloat' accessType=\"inputOutput\" value='2.0'/> <ShaderPart url='\"../shaders/gl.vs\" \"https://coderextreme.net/X3DJSONLD/src/main/shaders/gl.vs\"' type='VERTEX'></ShaderPart> <ShaderPart url='\"../shaders/pc_bubbles.fs\" \"https://coderextreme.net/X3DJSONLD/src/main/shaders/pc_bubbles.fs\"' type='FRAGMENT'></ShaderPart> </ComposedShader> <ComposedShader DEF='freewrl' language=\"GLSL\"> <field name='fw_textureCoodGenType' type='SFInt32' accessType=\"inputOutput\" value='0'/> <field name='chromaticDispertion' type='SFVec3f' accessType=\"inputOutput\" value='0.98 1.0 1.033'/> <field name='bias' type='SFFloat' accessType=\"inputOutput\" value='0.5'/> <field name='scale' type='SFFloat' accessType=\"inputOutput\" value='0.5'/> <field name='power' type='SFFloat' accessType=\"inputOutput\" value='2.0'/> <ShaderPart url='\"../shaders/freewrl.vs\" \"https://coderextreme.net/X3DJSONLD/src/main/shaders/freewrl.vs\"' type='VERTEX'></ShaderPart> <ShaderPart url='\"../shaders/pc_bubbles.fs\" \"https://coderextreme.net/X3DJSONLD/src/main/shaders/pc_bubbles.fs\"' type='FRAGMENT'></ShaderPart> </ComposedShader>
#<ComposedShader DEF='instant' language=\"GLSL\"> <field name='cube' type='SFInt32' accessType=\"inputOutput\" value='0'/> <field name='chromaticDispertion' type='SFVec3f' accessType=\"inputOutput\" value='0.98 1.0 1.033'/> <field name='bias' type='SFFloat' accessType=\"inputOutput\" value='0.5'/> <field name='scale' type='SFFloat' accessType=\"inputOutput\" value='0.5'/> <field name='power' type='SFFloat' accessType=\"inputOutput\" value='2.0'/> <ShaderPart url='\"../shaders/instant.vs\" \"https://coderextreme.net/X3DJSONLD/src/main/shaders/instant.vs\"' type='VERTEX'></ShaderPart> <ShaderPart url='\"../shaders/pc_bubbles.fs\" \"https://coderextreme.net/X3DJSONLD/src/main/shaders/pc_bubbles.fs\"' type='FRAGMENT'></ShaderPart> </ComposedShader>
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
field32.type = "SFVec3f"
field32.accessType = "inputOutput"
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
ShaderPart36 = x3d.ShaderPart()
ShaderPart36.url = ["../shaders/x3dom.vs","https://coderextreme.net/X3DJSONLD/src/main/shaders/x3dom.vs"]
ShaderPart36.type = "VERTEX"

ComposedShader30.parts.append(ShaderPart36)
ShaderPart37 = x3d.ShaderPart()
ShaderPart37.url = ["../shaders/pc_bubbles.fs","https://coderextreme.net/X3DJSONLD/src/main/shaders/pc_bubbles.fs"]
ShaderPart37.type = "FRAGMENT"

ComposedShader30.parts.append(ShaderPart37)

Appearance21.shaders.append(ComposedShader30)
ComposedShader38 = x3d.ComposedShader()
ComposedShader38.DEF = "x_ite"
ComposedShader38.language = "GLSL"
field39 = x3d.field()
field39.name = "cube"
field39.type = "SFNode"
field39.accessType = "inputOutput"
ComposedCubeMapTexture40 = x3d.ComposedCubeMapTexture()
ComposedCubeMapTexture40.USE = "texture"

field39.children.append(ComposedCubeMapTexture40)

ComposedShader38.field.append(field39)
field41 = x3d.field()
field41.name = "chromaticDispertion"
field41.type = "SFVec3f"
field41.accessType = "inputOutput"
field41.value = [0.98,1,1.033]

ComposedShader38.field.append(field41)
field42 = x3d.field()
field42.name = "bias"
field42.type = "SFFloat"
field42.accessType = "inputOutput"
field42.value = 0.5

ComposedShader38.field.append(field42)
field43 = x3d.field()
field43.name = "scale"
field43.type = "SFFloat"
field43.accessType = "inputOutput"
field43.value = 0.5

ComposedShader38.field.append(field43)
field44 = x3d.field()
field44.name = "power"
field44.type = "SFFloat"
field44.accessType = "inputOutput"
field44.value = 2

ComposedShader38.field.append(field44)
ShaderPart45 = x3d.ShaderPart()
ShaderPart45.url = ["../shaders/x_ite.vs","https://coderextreme.net/X3DJSONLD/src/main/shaders/x_ite.vs"]
ShaderPart45.type = "VERTEX"

ComposedShader38.parts.append(ShaderPart45)
ShaderPart46 = x3d.ShaderPart()
ShaderPart46.url = ["../shaders/x_itebubbles.fs","https://coderextreme.net/X3DJSONLD/src/main/shaders/x_itebubbles.fs"]
ShaderPart46.type = "FRAGMENT"

ComposedShader38.parts.append(ShaderPart46)

Appearance21.shaders.append(ComposedShader38)

Shape20.appearance = Appearance21
Sphere47 = x3d.Sphere()

Shape20.geometry = Sphere47

Transform19.children.append(Shape20)

ProtoBody18.children.append(Transform19)
Script48 = x3d.Script()
Script48.DEF = "Bounce"
field49 = x3d.field()
field49.name = "translation"
field49.accessType = "inputOutput"
field49.type = "SFVec3f"
field49.value = [0,0,0]

Script48.field.append(field49)
field50 = x3d.field()
field50.name = "velocity"
field50.accessType = "inputOutput"
field50.type = "SFVec3f"
field50.value = [0,0,0]

Script48.field.append(field50)
field51 = x3d.field()
field51.name = "set_fraction"
field51.accessType = "inputOnly"
field51.type = "SFTime"

Script48.field.append(field51)

Script48.sourceCode = '''ecmascript:\n"+
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
"			    if (Math.abs(translation.x) > 10) {\n"+
"				initialize();\n"+
"			    } else if (Math.abs(translation.y) > 10) {\n"+
"				initialize();\n"+
"			    } else if (Math.abs(translation.z) > 10) {\n"+
"				initialize();\n"+
"			    } else {\n"+
"				velocity.x += Math.random() * 0.2 - 0.1;\n"+
"				velocity.y += Math.random() * 0.2 - 0.1;\n"+
"				velocity.z += Math.random() * 0.2 - 0.1;\n"+
"			    }\n"+
"			}'''

ProtoBody18.children.append(Script48)
TimeSensor52 = x3d.TimeSensor()
TimeSensor52.DEF = "TourTime"
TimeSensor52.cycleInterval = 0.15
TimeSensor52.loop = True

ProtoBody18.children.append(TimeSensor52)
ROUTE53 = x3d.ROUTE()
ROUTE53.fromNode = "TourTime"
ROUTE53.fromField = "cycleTime"
ROUTE53.toNode = "Bounce"
ROUTE53.toField = "set_fraction"

ProtoBody18.children.append(ROUTE53)
ROUTE54 = x3d.ROUTE()
ROUTE54.fromNode = "Bounce"
ROUTE54.fromField = "translation_changed"
ROUTE54.toNode = "transform"
ROUTE54.toField = "set_translation"

ProtoBody18.children.append(ROUTE54)

ProtoDeclare17.ProtoBody = ProtoBody18

Scene13.children.append(ProtoDeclare17)
ProtoInstance55 = x3d.ProtoInstance()
ProtoInstance55.name = "Bubble"

Scene13.children.append(ProtoInstance55)
ProtoInstance56 = x3d.ProtoInstance()
ProtoInstance56.name = "Bubble"

Scene13.children.append(ProtoInstance56)
ProtoInstance57 = x3d.ProtoInstance()
ProtoInstance57.name = "Bubble"

Scene13.children.append(ProtoInstance57)

X3D0.Scene = Scene13
f = open("././bub_RoundTrip.x3d", "w")
f.write(X3D0.XML())
f.close()
