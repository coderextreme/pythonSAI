print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"
head1 = x3d.head()
meta2 = x3d.meta()
meta2.name = "title"
meta2.content = "PixelTextureComponentExamples.x3d"

head1.children.append(meta2)
meta3 = x3d.meta()
meta3.name = "description"
meta3.content = "This example shows the five PixelTexture components, with 0 to 4 components each, shown in Table 5-18."

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.name = "creator"
meta4.content = "Leonard Daly and Don Brutzman"

head1.children.append(meta4)
meta5 = x3d.meta()
meta5.name = "created"
meta5.content = "25 August 2008"

head1.children.append(meta5)
meta6 = x3d.meta()
meta6.name = "modified"
meta6.content = "7 January 2014"

head1.children.append(meta6)
meta7 = x3d.meta()
meta7.name = "reference"
meta7.content = "http://X3dGraphics.com"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.name = "reference"
meta8.content = "X3D for Web Authors, Table 5.18"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "reference"
meta9.content = "https://www.web3d.org/x3d/content/examples/X3dResources.html"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "rights"
meta10.content = "Copyright (c) 2006, Daly Realism and Don Brutzman"

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.name = "subject"
meta11.content = "X3D book, X3D graphics, X3D-Edit, http://www.x3dGraphics.com"

head1.children.append(meta11)
meta12 = x3d.meta()
meta12.name = "identifier"
meta12.content = "http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter05AppearanceMaterialTextures/PixelTextureComponentExamples.x3d"

head1.children.append(meta12)
meta13 = x3d.meta()
meta13.name = "generator"
meta13.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"

head1.children.append(meta13)
meta14 = x3d.meta()
meta14.name = "license"
meta14.content = "../license.html"

head1.children.append(meta14)

X3D0.head = head1
Scene15 = x3d.Scene()
Background16 = x3d.Background()

Scene15.children.append(Background16)
Viewpoint17 = x3d.Viewpoint()
Viewpoint17.description = "Table 5.18 SFImage component examples"
Viewpoint17.position = [0,0,14]

Scene15.children.append(Viewpoint17)
Transform18 = x3d.Transform()
Transform18.translation = [-6,0,0]
Shape19 = x3d.Shape()
Appearance20 = x3d.Appearance()
PixelTexture21 = x3d.PixelTexture()
PixelTexture21.DEF = "ZeroComponents"

Appearance20.texture = PixelTexture21

Shape19.appearance = Appearance20
Box22 = x3d.Box()

Shape19.geometry = Box22

Transform18.children.append(Shape19)
Transform23 = x3d.Transform()
Transform23.translation = [0,-2,0]
Shape24 = x3d.Shape()
Text25 = x3d.Text()
Text25.string = ["0"]
FontStyle26 = x3d.FontStyle()
FontStyle26.DEF = "CenterJustify"
FontStyle26.justify = ["MIDDLE","MIDDLE"]

Text25.fontStyle = FontStyle26

Shape24.geometry = Text25
Appearance27 = x3d.Appearance()
Appearance27.DEF = "TextMaterial"
Material28 = x3d.Material()
Material28.diffuseColor = [1,1,1]

Appearance27.material = Material28

Shape24.appearance = Appearance27

Transform23.children.append(Shape24)

Transform18.children.append(Transform23)

Scene15.children.append(Transform18)
Transform29 = x3d.Transform()
Transform29.translation = [-3,0,0]
Shape30 = x3d.Shape()
Appearance31 = x3d.Appearance()
PixelTexture32 = x3d.PixelTexture()
PixelTexture32.DEF = "OneComponent"
PixelTexture32.image = [1,2,1,255,0]

Appearance31.texture = PixelTexture32

Shape30.appearance = Appearance31
Box33 = x3d.Box()

Shape30.geometry = Box33

Transform29.children.append(Shape30)
Transform34 = x3d.Transform()
Transform34.translation = [0,-2,0]
Shape35 = x3d.Shape()
Text36 = x3d.Text()
Text36.string = ["1"]
FontStyle37 = x3d.FontStyle()
FontStyle37.USE = "CenterJustify"

Text36.fontStyle = FontStyle37

Shape35.geometry = Text36
Appearance38 = x3d.Appearance()
Appearance38.USE = "TextMaterial"

Shape35.appearance = Appearance38

Transform34.children.append(Shape35)

Transform29.children.append(Transform34)

Scene15.children.append(Transform29)
Transform39 = x3d.Transform()
Shape40 = x3d.Shape()
Appearance41 = x3d.Appearance()
PixelTexture42 = x3d.PixelTexture()
PixelTexture42.DEF = "TwoComponents"
PixelTexture42.image = [2,1,2,52479,8823]

Appearance41.texture = PixelTexture42

Shape40.appearance = Appearance41
Box43 = x3d.Box()

Shape40.geometry = Box43

Transform39.children.append(Shape40)
Transform44 = x3d.Transform()
Transform44.translation = [0,-2,0]
Shape45 = x3d.Shape()
Text46 = x3d.Text()
Text46.string = ["2"]
FontStyle47 = x3d.FontStyle()
FontStyle47.USE = "CenterJustify"

Text46.fontStyle = FontStyle47

Shape45.geometry = Text46
Appearance48 = x3d.Appearance()
Appearance48.USE = "TextMaterial"

Shape45.appearance = Appearance48

Transform44.children.append(Shape45)

Transform39.children.append(Transform44)

Scene15.children.append(Transform39)
Transform49 = x3d.Transform()
Transform49.translation = [3,0,0]
Shape50 = x3d.Shape()
Appearance51 = x3d.Appearance()
#note 0x000000 = 0
PixelTexture52 = x3d.PixelTexture()
PixelTexture52.DEF = "ThreeComponents"
PixelTexture52.image = [2,4,3,16711680,65280,0,0,0,0,16777215,16776960]

Appearance51.texture = PixelTexture52

Shape50.appearance = Appearance51
Box53 = x3d.Box()

Shape50.geometry = Box53

Transform49.children.append(Shape50)
Transform54 = x3d.Transform()
Transform54.translation = [0,-2,0]
Shape55 = x3d.Shape()
Text56 = x3d.Text()
Text56.string = ["3"]
FontStyle57 = x3d.FontStyle()
FontStyle57.USE = "CenterJustify"

Text56.fontStyle = FontStyle57

Shape55.geometry = Text56
Appearance58 = x3d.Appearance()
Appearance58.USE = "TextMaterial"

Shape55.appearance = Appearance58

Transform54.children.append(Shape55)

Transform49.children.append(Transform54)

Scene15.children.append(Transform49)
Transform59 = x3d.Transform()
Transform59.translation = [6,0,0]
Shape60 = x3d.Shape()
Appearance61 = x3d.Appearance()
#Erroneous value in book: 1 0 0 255, 0 1 0 255, 0 0 1 255, 1 0 0 127, 0 1 0 127, 0 0 1 127
PixelTexture62 = x3d.PixelTexture()
PixelTexture62.DEF = "FourComponents"
PixelTexture62.image = [3,2,4,-16776961,16711935,65535,-16777089,16711807,65407]

Appearance61.texture = PixelTexture62

Shape60.appearance = Appearance61
Box63 = x3d.Box()

Shape60.geometry = Box63

Transform59.children.append(Shape60)
Transform64 = x3d.Transform()
Transform64.translation = [0,-2,0]
Shape65 = x3d.Shape()
Text66 = x3d.Text()
Text66.string = ["4"]
FontStyle67 = x3d.FontStyle()
FontStyle67.USE = "CenterJustify"

Text66.fontStyle = FontStyle67

Shape65.geometry = Text66
Appearance68 = x3d.Appearance()
Appearance68.USE = "TextMaterial"

Shape65.appearance = Appearance68

Transform64.children.append(Shape65)

Transform59.children.append(Transform64)

Scene15.children.append(Transform59)
#Background from PixelTextureBW.x3d
Transform69 = x3d.Transform()
Transform69.translation = [0,6,-2]
Shape70 = x3d.Shape()
Appearance71 = x3d.Appearance()
PixelTexture72 = x3d.PixelTexture()
PixelTexture72.image = [8,8,1,204,0,204,0,204,0,204,0,0,204,0,204,0,204,0,204,204,0,204,0,204,0,204,0,0,204,0,204,0,204,0,204,204,0,204,0,204,0,204,0,0,204,0,204,0,204,0,204,204,0,204,0,204,0,204,0,0,204,0,204,0,204,0,204]

Appearance71.texture = PixelTexture72

Shape70.appearance = Appearance71
Box73 = x3d.Box()
Box73.size = [16,16,0.1]

Shape70.geometry = Box73

Transform69.children.append(Shape70)

Scene15.children.append(Transform69)

X3D0.Scene = Scene15
f = open("././PixelTextureComponentExamples_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
