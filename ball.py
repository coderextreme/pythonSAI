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
component3.name = "EnvironmentalEffects"
component3.level = 3

head1.children.append(component3)
component4 = x3d.component()
component4.name = "Shaders"
component4.level = 1

head1.children.append(component4)
component5 = x3d.component()
component5.name = "CubeMapTexturing"
component5.level = 1

head1.children.append(component5)
component6 = x3d.component()
component6.name = "Texturing"
component6.level = 1

head1.children.append(component6)
component7 = x3d.component()
component7.name = "Rendering"
component7.level = 1

head1.children.append(component7)
component8 = x3d.component()
component8.name = "Shape"
component8.level = 4

head1.children.append(component8)
component9 = x3d.component()
component9.name = "Grouping"
component9.level = 3

head1.children.append(component9)
component10 = x3d.component()
component10.name = "Core"
component10.level = 1

head1.children.append(component10)
#component name='EnvironmentalEffects' level='1'></component
meta11 = x3d.meta()
meta11.name = "title"
meta11.content = "ball.x3d"

head1.children.append(meta11)
meta12 = x3d.meta()
meta12.name = "creator"
meta12.content = "John Carlson"

head1.children.append(meta12)
meta13 = x3d.meta()
meta13.name = "generator"
meta13.content = "manual"

head1.children.append(meta13)
meta14 = x3d.meta()
meta14.name = "identifier"
meta14.content = "https://coderextreme.net/X3DJSONLD/ball.x3d"

head1.children.append(meta14)
meta15 = x3d.meta()
meta15.name = "description"
meta15.content = "a prismatic sphere"

head1.children.append(meta15)

X3D0.head = head1
Scene16 = x3d.Scene()
WorldInfo17 = x3d.WorldInfo()
WorldInfo17.title = "ball.x3d"

Scene16.children.append(WorldInfo17)
NavigationInfo18 = x3d.NavigationInfo()
NavigationInfo18.type = ["ANY","EXAMINE","FLY","LOOKAT"]

Scene16.children.append(NavigationInfo18)
Viewpoint19 = x3d.Viewpoint()
Viewpoint19.description = "Tour Views"

Scene16.children.append(Viewpoint19)
Background20 = x3d.Background()
Background20.backUrl = ["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"]
Background20.bottomUrl = ["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"]
Background20.frontUrl = ["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"]
Background20.leftUrl = ["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"]
Background20.rightUrl = ["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"]
Background20.topUrl = ["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"]

Scene16.children.append(Background20)
Transform21 = x3d.Transform()
Shape22 = x3d.Shape()
Sphere23 = x3d.Sphere()

Shape22.geometry = Sphere23
Appearance24 = x3d.Appearance()
Material25 = x3d.Material()
Material25.diffuseColor = [0.7,0.7,0.7]
Material25.specularColor = [0.5,0.5,0.5]

Appearance24.material = Material25
ComposedCubeMapTexture26 = x3d.ComposedCubeMapTexture()
ComposedCubeMapTexture26.DEF = "texture"
ImageTexture27 = x3d.ImageTexture()
ImageTexture27.url = ["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"]

ComposedCubeMapTexture26.backTexture = ImageTexture27
ImageTexture28 = x3d.ImageTexture()
ImageTexture28.url = ["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"]

ComposedCubeMapTexture26.bottomTexture = ImageTexture28
ImageTexture29 = x3d.ImageTexture()
ImageTexture29.url = ["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"]

ComposedCubeMapTexture26.frontTexture = ImageTexture29
ImageTexture30 = x3d.ImageTexture()
ImageTexture30.url = ["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"]

ComposedCubeMapTexture26.leftTexture = ImageTexture30
ImageTexture31 = x3d.ImageTexture()
ImageTexture31.url = ["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"]

ComposedCubeMapTexture26.rightTexture = ImageTexture31
ImageTexture32 = x3d.ImageTexture()
ImageTexture32.url = ["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"]

ComposedCubeMapTexture26.topTexture = ImageTexture32

Appearance24.texture = ComposedCubeMapTexture26
#<ProgramShader DEF='ProgramShader' containerField='shaders' language='GLSL'> <ShaderProgram url='\"../shaders/freewrl.vs\" \"https://coderextreme.net/X3DJSONLD/src/main/shaders/freewrl.vs\"' containerField='programs' type='VERTEX'> <field name='chromaticDispertion' accessType='initializeOnly' type='SFVec3f' value='0.98 1 1.033'/> <field name='bias' accessType='initializeOnly' type='SFFloat' value='0.5'/> <field name='scale' accessType='initializeOnly' type='SFFloat' value='0.5'/> <field name='power' accessType='initializeOnly' type='SFFloat' value='2'/> </ShaderProgram> <ShaderProgram url='\"../shaders/freewrl.fs\" \"https://coderextreme.net/X3DJSONLD/src/main/shaders/freewrl.fs\"' containerField='programs' type='FRAGMENT'/> </ProgramShader>
#<ComposedShader language='GLSL'> <field name='chromaticDispertion' accessType='initializeOnly' type='SFVec3f' value='0.98 1 1.033'></field> <field name='fw_Texture_unit0' type='SFNode' accessType=\"initializeOnly\"> <ComposedCubeMapTexture USE=\"texture\"></ComposedCubeMapTexture> </field> <field name='bias' accessType='initializeOnly' type='SFFloat' value='0.5'></field> <field name='scale' accessType='initializeOnly' type='SFFloat' value='0.5'></field> <field name='power' accessType='initializeOnly' type='SFFloat' value='2'></field> <ShaderPart url='\"../shaders/contact.vs\" \"https://coderextreme.net/X3DJSONLD/src/main/shaders/contact.vs\"' type=\"VERTEX\" containerField='parts'></ShaderPart> <ShaderPart url='\"../shaders/common.fs\" \"https://coderextreme.net/X3DJSONLD/src/main/shaders/common.fs\"' containerField='parts' type='FRAGMENT'></ShaderPart> </ComposedShader>
#<ComposedShader language='GLSL'> <field name='chromaticDispertion' accessType='inputOutput' type='SFVec3f' value='0.98 1 1.033'></field> <field name='cube' type='SFNode' accessType=\"inputOutput\"> <ComposedCubeMapTexture USE=\"texture\"></ComposedCubeMapTexture> </field> <field name='bias' accessType='inputOutput' type='SFFloat' value='0.5'></field> <field name='scale' accessType='inputOutput' type='SFFloat' value='0.5'></field> <field name='power' accessType='inputOutput' type='SFFloat' value='2'></field> <ShaderPart url='\"../shaders/octaga.vs\" \"https://coderextreme.net/X3DJSONLD/src/main/shaders/octaga.vs\"' type=\"VERTEX\" containerField='parts'></ShaderPart> <ShaderPart url='\"../shaders/common.fs\" \"https://coderextreme.net/X3DJSONLD/src/main/shaders/common.fs\"' containerField='parts' type='FRAGMENT'></ShaderPart> </ComposedShader>
#<ComposedShader language='GLSL'> <field name='chromaticDispertion' accessType='initializeOnly' type='SFVec3f' value='0.98 1 1.033'></field> <field name='cube' accessType='initializeOnly' type='SFInt32' value='0'></field> <field name='bias' accessType='initializeOnly' type='SFFloat' value='0.5'></field> <field name='scale' accessType='initializeOnly' type='SFFloat' value='0.5'></field> <field name='power' accessType='initializeOnly' type='SFFloat' value='2'></field> <ShaderPart url='\"../shaders/instant.vs\" \"https://coderextreme.net/X3DJSONLD/src/main/shaders/instant.vs\"' type=\"VERTEX\" containerField='parts'></ShaderPart> <ShaderPart url='\"../shaders/common.fs\" \"https://coderextreme.net/X3DJSONLD/src/main/shaders/common.fs\"' containerField='parts' type='FRAGMENT'></ShaderPart> </ComposedShader>
#
ComposedShader33 = x3d.ComposedShader()
ComposedShader33.language = "GLSL"
field34 = x3d.field()
field34.name = "chromaticDispertion"
field34.accessType = "inputOutput"
field34.type = "SFVec3f"
field34.value = [0.98,1,1.033]

ComposedShader33.field.append(field34)
field35 = x3d.field()
field35.name = "cube"
field35.type = "SFNode"
field35.accessType = "inputOutput"
ComposedCubeMapTexture36 = x3d.ComposedCubeMapTexture()
ComposedCubeMapTexture36.USE = "texture"

field35.children.append(ComposedCubeMapTexture36)

ComposedShader33.field.append(field35)
field37 = x3d.field()
field37.name = "bias"
field37.accessType = "inputOutput"
field37.type = "SFFloat"
field37.value = 0.5

ComposedShader33.field.append(field37)
field38 = x3d.field()
field38.name = "scale"
field38.accessType = "inputOutput"
field38.type = "SFFloat"
field38.value = 0.5

ComposedShader33.field.append(field38)
field39 = x3d.field()
field39.name = "power"
field39.accessType = "inputOutput"
field39.type = "SFFloat"
field39.value = 2

ComposedShader33.field.append(field39)
ShaderPart40 = x3d.ShaderPart()
ShaderPart40.url = ["../shaders/x3dom.vs","https://coderextreme.net/X3DJSONLD/src/main/shaders/x3dom.vs"]
ShaderPart40.type = "VERTEX"

ComposedShader33.parts.append(ShaderPart40)
ShaderPart41 = x3d.ShaderPart()
ShaderPart41.DEF = "common"
ShaderPart41.url = ["../shaders/common.fs","https://coderextreme.net/X3DJSONLD/src/main/shaders/common.fs"]
ShaderPart41.type = "FRAGMENT"

ComposedShader33.parts.append(ShaderPart41)

Appearance24.shaders.append(ComposedShader33)
ComposedShader42 = x3d.ComposedShader()
ComposedShader42.language = "GLSL"
field43 = x3d.field()
field43.name = "chromaticDispertion"
field43.accessType = "initializeOnly"
field43.type = "SFVec3f"
field43.value = [0.98,1,1.033]

ComposedShader42.field.append(field43)
field44 = x3d.field()
field44.name = "cube"
field44.type = "SFNode"
field44.accessType = "initializeOnly"
ComposedCubeMapTexture45 = x3d.ComposedCubeMapTexture()
ComposedCubeMapTexture45.USE = "texture"

field44.children.append(ComposedCubeMapTexture45)

ComposedShader42.field.append(field44)
field46 = x3d.field()
field46.name = "bias"
field46.accessType = "initializeOnly"
field46.type = "SFFloat"
field46.value = 0.5

ComposedShader42.field.append(field46)
field47 = x3d.field()
field47.name = "scale"
field47.accessType = "initializeOnly"
field47.type = "SFFloat"
field47.value = 0.5

ComposedShader42.field.append(field47)
field48 = x3d.field()
field48.name = "power"
field48.accessType = "initializeOnly"
field48.type = "SFFloat"
field48.value = 2

ComposedShader42.field.append(field48)
ShaderPart49 = x3d.ShaderPart()
ShaderPart49.url = ["../shaders/x_ite.vs","https://coderextreme.net/X3DJSONLD/src/main/shaders/x_ite.vs"]
ShaderPart49.type = "VERTEX"

ComposedShader42.parts.append(ShaderPart49)
ShaderPart50 = x3d.ShaderPart()
ShaderPart50.url = ["../shaders/x_itebubbles.fs","https://coderextreme.net/X3DJSONLD/src/main/shaders/x_itebubbles.fs"]
ShaderPart50.type = "FRAGMENT"

ComposedShader42.parts.append(ShaderPart50)

Appearance24.shaders.append(ComposedShader42)

Shape22.appearance = Appearance24

Transform21.children.append(Shape22)

Scene16.children.append(Transform21)

X3D0.Scene = Scene16
f = open("././ball_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
