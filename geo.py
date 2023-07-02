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
meta8.content = "geo.x3d"

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
meta11.content = "https://coderextreme.net/X3DJSONLD/geo.x3d"

head1.children.append(meta11)
meta12 = x3d.meta()
meta12.name = "description"
meta12.content = "a sphere"

head1.children.append(meta12)

X3D0.head = head1
Scene13 = x3d.Scene()
NavigationInfo14 = x3d.NavigationInfo()
NavigationInfo14.type = ["ANY","EXAMINE","FLY","LOOKAT"]

Scene13.children.append(NavigationInfo14)
Viewpoint15 = x3d.Viewpoint()
Viewpoint15.DEF = "Tour"
Viewpoint15.description = "Tour Views"

Scene13.children.append(Viewpoint15)
#Viewpoint position='0 0 4' description='sphere in road'/
Background16 = x3d.Background()
Background16.backUrl = ["../resources/images/bBK.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bBK.png"]
Background16.bottomUrl = ["../resources/images/bBT.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bBT.png"]
Background16.frontUrl = ["../resources/images/bFR.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bFR.png"]
Background16.leftUrl = ["../resources/images/bLF.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bLF.png"]
Background16.rightUrl = ["../resources/images/bRT.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bRT.png"]
Background16.topUrl = ["../resources/images/bTP.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bTP.png"]

Scene13.children.append(Background16)
Transform17 = x3d.Transform()
Shape18 = x3d.Shape()
Sphere19 = x3d.Sphere()

Shape18.geometry = Sphere19
Appearance20 = x3d.Appearance()
Material21 = x3d.Material()
Material21.diffuseColor = [0.7,0.7,0.7]
Material21.specularColor = [0.5,0.5,0.5]

Appearance20.material = Material21
ComposedCubeMapTexture22 = x3d.ComposedCubeMapTexture()
ComposedCubeMapTexture22.DEF = "texture"
ImageTexture23 = x3d.ImageTexture()
ImageTexture23.url = ["../resources/images/bBK.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bBK.png"]

ComposedCubeMapTexture22.backTexture = ImageTexture23
ImageTexture24 = x3d.ImageTexture()
ImageTexture24.url = ["../resources/images/bBT.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bBT.png"]

ComposedCubeMapTexture22.bottomTexture = ImageTexture24
ImageTexture25 = x3d.ImageTexture()
ImageTexture25.url = ["../resources/images/bFR.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bFR.png"]

ComposedCubeMapTexture22.frontTexture = ImageTexture25
ImageTexture26 = x3d.ImageTexture()
ImageTexture26.url = ["../resources/images/bLF.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bLF.png"]

ComposedCubeMapTexture22.leftTexture = ImageTexture26
ImageTexture27 = x3d.ImageTexture()
ImageTexture27.url = ["../resources/images/bRT.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bRT.png"]

ComposedCubeMapTexture22.rightTexture = ImageTexture27
ImageTexture28 = x3d.ImageTexture()
ImageTexture28.url = ["../resources/images/bTP.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bTP.png"]

ComposedCubeMapTexture22.topTexture = ImageTexture28

Appearance20.texture = ComposedCubeMapTexture22
ComposedShader29 = x3d.ComposedShader()
ComposedShader29.language = "GLSL"
field30 = x3d.field()
field30.name = "chromaticDispertion"
field30.accessType = "inputOutput"
field30.type = "SFVec3f"
field30.value = [0.98,1,1.033]

ComposedShader29.field.append(field30)
field31 = x3d.field()
field31.name = "cube"
field31.type = "SFNode"
field31.accessType = "inputOutput"
ComposedCubeMapTexture32 = x3d.ComposedCubeMapTexture()
ComposedCubeMapTexture32.USE = "texture"

field31.children.append(ComposedCubeMapTexture32)

ComposedShader29.field.append(field31)
field33 = x3d.field()
field33.name = "bias"
field33.accessType = "inputOutput"
field33.type = "SFFloat"
field33.value = 0.5

ComposedShader29.field.append(field33)
field34 = x3d.field()
field34.name = "scale"
field34.accessType = "inputOutput"
field34.type = "SFFloat"
field34.value = 0.5

ComposedShader29.field.append(field34)
field35 = x3d.field()
field35.name = "power"
field35.accessType = "inputOutput"
field35.type = "SFFloat"
field35.value = 2

ComposedShader29.field.append(field35)
ShaderPart36 = x3d.ShaderPart()
ShaderPart36.url = ["../shaders/x3dom.vs","https://coderextreme.net/X3DJSONLD/src/main/shaders/x3dom.vs"]
ShaderPart36.type = "VERTEX"

ComposedShader29.parts.append(ShaderPart36)
ShaderPart37 = x3d.ShaderPart()
ShaderPart37.DEF = "common"
ShaderPart37.url = ["../shaders/common.fs","https://coderextreme.net/X3DJSONLD/src/main/shaders/common.fs"]
ShaderPart37.type = "FRAGMENT"

ComposedShader29.parts.append(ShaderPart37)

Appearance20.shaders.append(ComposedShader29)
ComposedShader38 = x3d.ComposedShader()
ComposedShader38.language = "GLSL"
field39 = x3d.field()
field39.name = "chromaticDispertion"
field39.accessType = "initializeOnly"
field39.type = "SFVec3f"
field39.value = [0.98,1,1.033]

ComposedShader38.field.append(field39)
field40 = x3d.field()
field40.name = "cube"
field40.type = "SFNode"
field40.accessType = "initializeOnly"
ComposedCubeMapTexture41 = x3d.ComposedCubeMapTexture()
ComposedCubeMapTexture41.USE = "texture"

field40.children.append(ComposedCubeMapTexture41)

ComposedShader38.field.append(field40)
field42 = x3d.field()
field42.name = "bias"
field42.accessType = "initializeOnly"
field42.type = "SFFloat"
field42.value = 0.5

ComposedShader38.field.append(field42)
field43 = x3d.field()
field43.name = "scale"
field43.accessType = "initializeOnly"
field43.type = "SFFloat"
field43.value = 0.5

ComposedShader38.field.append(field43)
field44 = x3d.field()
field44.name = "power"
field44.accessType = "initializeOnly"
field44.type = "SFFloat"
field44.value = 2

ComposedShader38.field.append(field44)
ShaderPart45 = x3d.ShaderPart()
ShaderPart45.url = ["../shaders/x_ite.vs","https://coderextreme.net/X3DJSONLD/src/main/shaders/x_ite.vs"]
ShaderPart45.type = "VERTEX"

ComposedShader38.parts.append(ShaderPart45)
ShaderPart46 = x3d.ShaderPart()
ShaderPart46.url = ["../shaders/x_ite.fs","https://coderextreme.net/X3DJSONLD/src/main/shaders/x_ite.fs"]
ShaderPart46.type = "FRAGMENT"

ComposedShader38.parts.append(ShaderPart46)

Appearance20.shaders.append(ComposedShader38)

Shape18.appearance = Appearance20

Transform17.children.append(Shape18)

Scene13.children.append(Transform17)

X3D0.Scene = Scene13
f = open("././geo_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
