import x3dpsail as x3d
X3D0 = x3d.X3D()
X3D0.setProfile("Immersive")
X3D0.setVersion("3.3")
head1 = x3d.head()
component2 = x3d.component()
component2.setName("Shaders")
component2.setLevel(1)

head1.addComponent(component2)
component3 = x3d.component()
component3.setName("CubeMapTexturing")
component3.setLevel(1)

head1.addComponent(component3)
meta4 = x3d.meta()
meta4.setName("title")
meta4.setContent("geo.x3d")

head1.addMeta(meta4)
meta5 = x3d.meta()
meta5.setName("creator")
meta5.setContent("John Carlson")

head1.addMeta(meta5)
meta6 = x3d.meta()
meta6.setName("generator")
meta6.setContent("manual")

head1.addMeta(meta6)
meta7 = x3d.meta()
meta7.setName("identifier")
meta7.setContent("https://coderextreme.net/X3DJSONLD/geo.x3d")

head1.addMeta(meta7)
meta8 = x3d.meta()
meta8.setName("description")
meta8.setContent("a sphere")

head1.addMeta(meta8)

X3D0.setHead(head1)
Scene9 = x3d.Scene()
NavigationInfo10 = x3d.NavigationInfo()
NavigationInfo10.setType(["ANY","EXAMINE","FLY","LOOKAT"])

Scene9.addChildren(NavigationInfo10)
Viewpoint11 = x3d.Viewpoint()
Viewpoint11.setDEF("Tour")
Viewpoint11.setDescription("Tour Views")

Scene9.addChildren(Viewpoint11)
#Viewpoint position='0 0 4' description='sphere in road'/
Background12 = x3d.Background()
Background12.setBackUrl(["resources/images/bBK.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bBK.png"])
Background12.setBottomUrl(["resources/images/bBT.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bBT.png"])
Background12.setFrontUrl(["resources/images/bFR.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bFR.png"])
Background12.setLeftUrl(["resources/images/bLF.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bLF.png"])
Background12.setRightUrl(["resources/images/bRT.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bRT.png"])
Background12.setTopUrl(["resources/images/bTP.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bTP.png"])

Scene9.addChildren(Background12)
Transform13 = x3d.Transform()
Shape14 = x3d.Shape()
Sphere15 = x3d.Sphere()

Shape14.setGeometry(Sphere15)
Appearance16 = x3d.Appearance()
Material17 = x3d.Material()
Material17.setDiffuseColor([0.7,0.7,0.7])
Material17.setSpecularColor([0.5,0.5,0.5])

Appearance16.setMaterial(Material17)
ComposedCubeMapTexture18 = x3d.ComposedCubeMapTexture()
ComposedCubeMapTexture18.setDEF("texture")
ImageTexture19 = x3d.ImageTexture()
ImageTexture19.setUrl(["resources/images/bBK.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bBK.png"])

ComposedCubeMapTexture18.setBack(ImageTexture19)
ImageTexture20 = x3d.ImageTexture()
ImageTexture20.setUrl(["resources/images/bBT.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bBT.png"])

ComposedCubeMapTexture18.setBottom(ImageTexture20)
ImageTexture21 = x3d.ImageTexture()
ImageTexture21.setUrl(["resources/images/bFR.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bFR.png"])

ComposedCubeMapTexture18.setFront(ImageTexture21)
ImageTexture22 = x3d.ImageTexture()
ImageTexture22.setUrl(["resources/images/bLF.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bLF.png"])

ComposedCubeMapTexture18.setLeft(ImageTexture22)
ImageTexture23 = x3d.ImageTexture()
ImageTexture23.setUrl(["resources/images/bRT.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bRT.png"])

ComposedCubeMapTexture18.setRight(ImageTexture23)
ImageTexture24 = x3d.ImageTexture()
ImageTexture24.setUrl(["resources/images/bTP.png","https://coderextreme.net/X3DJSONLD/src/main/resources/images/bTP.png"])

ComposedCubeMapTexture18.setTop(ImageTexture24)

Appearance16.setTexture(ComposedCubeMapTexture18)
ComposedShader25 = x3d.ComposedShader()
ComposedShader25.setLanguage("GLSL")
field26 = x3d.field()
field26.setName("chromaticDispertion")
field26.setAccessType("inputOutput")
field26.setType("SFVec3f")
field26.setValue("0.98 1 1.033")

ComposedShader25.addField(field26)
field27 = x3d.field()
field27.setName("cube")
field27.setType("SFNode")
field27.setAccessType("inputOutput")
ComposedCubeMapTexture28 = x3d.ComposedCubeMapTexture()
ComposedCubeMapTexture28.setUSE("texture")

field27.addChildren(ComposedCubeMapTexture28)

ComposedShader25.addField(field27)
field29 = x3d.field()
field29.setName("bias")
field29.setAccessType("inputOutput")
field29.setType("SFFloat")
field29.setValue("0.5")

ComposedShader25.addField(field29)
field30 = x3d.field()
field30.setName("scale")
field30.setAccessType("inputOutput")
field30.setType("SFFloat")
field30.setValue("0.5")

ComposedShader25.addField(field30)
field31 = x3d.field()
field31.setName("power")
field31.setAccessType("inputOutput")
field31.setType("SFFloat")
field31.setValue("2")

ComposedShader25.addField(field31)
ShaderPart32 = x3d.ShaderPart()
ShaderPart32.setUrl(["../shaders/x3dom.vs","https://coderextreme.net/X3DJSONLD/shaders/x3dom.vs"])
ShaderPart32.setType("VERTEX")

ComposedShader25.addParts(ShaderPart32)
ShaderPart33 = x3d.ShaderPart()
ShaderPart33.setDEF("common")
ShaderPart33.setUrl(["../shaders/common.fs","https://coderextreme.net/X3DJSONLD/shaders/common.fs"])
ShaderPart33.setType("FRAGMENT")

ComposedShader25.addParts(ShaderPart33)

Appearance16.addShaders(ComposedShader25)
ComposedShader34 = x3d.ComposedShader()
ComposedShader34.setLanguage("GLSL")
field35 = x3d.field()
field35.setName("chromaticDispertion")
field35.setAccessType("initializeOnly")
field35.setType("SFVec3f")
field35.setValue("0.98 1 1.033")

ComposedShader34.addField(field35)
field36 = x3d.field()
field36.setName("cube")
field36.setType("SFNode")
field36.setAccessType("initializeOnly")
ComposedCubeMapTexture37 = x3d.ComposedCubeMapTexture()
ComposedCubeMapTexture37.setUSE("texture")

field36.addChildren(ComposedCubeMapTexture37)

ComposedShader34.addField(field36)
field38 = x3d.field()
field38.setName("bias")
field38.setAccessType("initializeOnly")
field38.setType("SFFloat")
field38.setValue("0.5")

ComposedShader34.addField(field38)
field39 = x3d.field()
field39.setName("scale")
field39.setAccessType("initializeOnly")
field39.setType("SFFloat")
field39.setValue("0.5")

ComposedShader34.addField(field39)
field40 = x3d.field()
field40.setName("power")
field40.setAccessType("initializeOnly")
field40.setType("SFFloat")
field40.setValue("2")

ComposedShader34.addField(field40)
ShaderPart41 = x3d.ShaderPart()
ShaderPart41.setUrl(["../shaders/cobweb.vs","https://coderextreme.net/X3DJSONLD/shaders/cobweb.vs"])
ShaderPart41.setType("VERTEX")

ComposedShader34.addParts(ShaderPart41)
ShaderPart42 = x3d.ShaderPart()
ShaderPart42.setUSE("common")

ComposedShader34.addParts(ShaderPart42)

Appearance16.addShaders(ComposedShader34)

Shape14.setAppearance(Appearance16)

Transform13.addChildren(Shape14)

Scene9.addChildren(Transform13)

X3D0.setScene(Scene9)
X3D0.toFileX3D("././geo_RoundTrip.x3d")
