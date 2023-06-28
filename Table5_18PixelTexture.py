print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Interchange"
X3D0.version = "3.3"
head1 = x3d.head()
meta2 = x3d.meta()
meta2.name = "title"
meta2.content = "Table5_18PixelTexture"

head1.children.append(meta2)
meta3 = x3d.meta()
meta3.name = "description"
meta3.content = "PixelTexture example for Table 5.18"

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.name = "creator"
meta4.content = "Leonard Daly and Don Brutzman"

head1.children.append(meta4)
meta5 = x3d.meta()
meta5.name = "created"
meta5.content = "18 December 2006"

head1.children.append(meta5)
meta6 = x3d.meta()
meta6.name = "modified"
meta6.content = "2 April 2017"

head1.children.append(meta6)
meta7 = x3d.meta()
meta7.name = "reference"
meta7.content = "http://X3dGraphics.com"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.name = "reference"
meta8.content = "https://www.web3d.org/x3d/content/examples/X3dResources.html"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "rights"
meta9.content = "Copyright 2006, Daly Realism and Don Brutzman"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "subject"
meta10.content = "X3D, PixelTexture"

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.name = "identifier"
meta11.content = "http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter05AppearanceMaterialTextures/Table5_18PixelTexture"

head1.children.append(meta11)
meta12 = x3d.meta()
meta12.name = "generator"
meta12.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"

head1.children.append(meta12)
meta13 = x3d.meta()
meta13.name = "license"
meta13.content = "../license.html"

head1.children.append(meta13)

X3D0.head = head1
Scene14 = x3d.Scene()
Background15 = x3d.Background()
Background15.skyColor = [0,0,1]

Scene14.children.append(Background15)
Transform16 = x3d.Transform()
Transform16.DEF = "Checkerboard"
Transform16.translation = [0,0,-10]
Shape17 = x3d.Shape()
Appearance18 = x3d.Appearance()
TextureTransform19 = x3d.TextureTransform()
TextureTransform19.scale = [500,500]

Appearance18.textureTransform.append(TextureTransform19)
PixelTexture20 = x3d.PixelTexture()
PixelTexture20.image = [2,2,3,15119869,16767927,16767927,15119869]

Appearance18.texture = PixelTexture20

Shape17.appearance = Appearance18
Box21 = x3d.Box()
Box21.size = [1000,1000,0.01]

Shape17.geometry = Box21

Transform16.children.append(Shape17)

Scene14.children.append(Transform16)
Viewpoint22 = x3d.Viewpoint()
Viewpoint22.description = "View All"
Viewpoint22.position = [0,0,20]

Scene14.children.append(Viewpoint22)
Viewpoint23 = x3d.Viewpoint()
Viewpoint23.description = "Empty Image"
Viewpoint23.position = [0,5,5]

Scene14.children.append(Viewpoint23)
Transform24 = x3d.Transform()
Transform24.DEF = "EmptyImage"
Transform24.rotation = [1,1,0,1]
Transform24.translation = [0,5,0]
Shape25 = x3d.Shape()
Appearance26 = x3d.Appearance()
PixelTexture27 = x3d.PixelTexture()

Appearance26.texture = PixelTexture27

Shape25.appearance = Appearance26
Box28 = x3d.Box()
Box28.DEF = "StandardBox"

Shape25.geometry = Box28

Transform24.children.append(Shape25)

Scene14.children.append(Transform24)
Viewpoint29 = x3d.Viewpoint()
Viewpoint29.description = "Black and white PixelTexture"
Viewpoint29.position = [-5,0,5]

Scene14.children.append(Viewpoint29)
Transform30 = x3d.Transform()
Transform30.DEF = "BW"
Transform30.rotation = [1,1,0,1]
Transform30.translation = [-5,0,0]
Shape31 = x3d.Shape()
Appearance32 = x3d.Appearance()
PixelTexture33 = x3d.PixelTexture()
PixelTexture33.image = [1,2,1,255,0]

Appearance32.texture = PixelTexture33

Shape31.appearance = Appearance32
Box34 = x3d.Box()
Box34.USE = "StandardBox"

Shape31.geometry = Box34

Transform30.children.append(Shape31)

Scene14.children.append(Transform30)
Viewpoint35 = x3d.Viewpoint()
Viewpoint35.description = "Black and white with Alpha PixelTexture"
Viewpoint35.position = [5,0,5]

Scene14.children.append(Viewpoint35)
Transform36 = x3d.Transform()
Transform36.DEF = "AlphaBW"
Transform36.rotation = [1,1,0,1]
Transform36.translation = [5,0,0]
Shape37 = x3d.Shape()
Appearance38 = x3d.Appearance()
PixelTexture39 = x3d.PixelTexture()
PixelTexture39.image = [2,1,2,52479,8823]

Appearance38.texture = PixelTexture39

Shape37.appearance = Appearance38
Box40 = x3d.Box()
Box40.USE = "StandardBox"

Shape37.geometry = Box40

Transform36.children.append(Shape37)

Scene14.children.append(Transform36)
Viewpoint41 = x3d.Viewpoint()
Viewpoint41.description = "RGB PixelTexture"
Viewpoint41.position = [-5,-5,5]

Scene14.children.append(Viewpoint41)
Transform42 = x3d.Transform()
Transform42.DEF = "RGB"
Transform42.rotation = [1,1,0,1]
Transform42.translation = [-5,-5,0]
Shape43 = x3d.Shape()
Appearance44 = x3d.Appearance()
PixelTexture45 = x3d.PixelTexture()
PixelTexture45.image = [2,4,3,16711680,65280,0,0,0,0,16777215,16776960]

Appearance44.texture = PixelTexture45

Shape43.appearance = Appearance44
Box46 = x3d.Box()
Box46.USE = "StandardBox"

Shape43.geometry = Box46

Transform42.children.append(Shape43)

Scene14.children.append(Transform42)
Viewpoint47 = x3d.Viewpoint()
Viewpoint47.description = "RGB with Alpha PixelTexture"
Viewpoint47.position = [5,-5,5]

Scene14.children.append(Viewpoint47)
Transform48 = x3d.Transform()
Transform48.DEF = "AlphaRGB"
Transform48.rotation = [1,1,0,1]
Transform48.translation = [5,-5,0]
Shape49 = x3d.Shape()
Appearance50 = x3d.Appearance()
PixelTexture51 = x3d.PixelTexture()
PixelTexture51.image = [3,2,4,-16776961,16711935,65535,-16777089,16711807,65407]

Appearance50.texture = PixelTexture51

Shape49.appearance = Appearance50
Box52 = x3d.Box()
Box52.USE = "StandardBox"

Shape49.geometry = Box52

Transform48.children.append(Shape49)

Scene14.children.append(Transform48)

X3D0.Scene = Scene14
f = open("././Table5_18PixelTexture_RoundTrip.x3d", "w")
f.write(X3D0.XML())
f.close()
