from jnius import autoclass
from X3Dautoclass import *
X3D0 =  X3DObject().setProfile("Interchange").setVersion("3.3")
head1 = headObject()
meta2 = metaObject().setName("title").setContent("Table5_18PixelTexture")
head1.addMeta(meta2)
meta3 = metaObject().setName("description").setContent("PixelTexture example for Table 5.18")
head1.addMeta(meta3)
meta4 = metaObject().setName("creator").setContent("Leonard Daly and Don Brutzman")
head1.addMeta(meta4)
meta5 = metaObject().setName("created").setContent("18 December 2006")
head1.addMeta(meta5)
meta6 = metaObject().setName("modified").setContent("2 April 2017")
head1.addMeta(meta6)
meta7 = metaObject().setName("reference").setContent("http://X3dGraphics.com")
head1.addMeta(meta7)
meta8 = metaObject().setName("reference").setContent("http://www.web3d.org/x3d/content/examples/X3dResources.html")
head1.addMeta(meta8)
meta9 = metaObject().setName("rights").setContent("Copyright 2006, Daly Realism and Don Brutzman")
head1.addMeta(meta9)
meta10 = metaObject().setName("subject").setContent("X3D, PixelTexture")
head1.addMeta(meta10)
meta11 = metaObject().setName("identifier").setContent("http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter05AppearanceMaterialTextures/Table5_18PixelTexture")
head1.addMeta(meta11)
meta12 = metaObject().setName("generator").setContent("X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit")
head1.addMeta(meta12)
meta13 = metaObject().setName("license").setContent("../license.html")
head1.addMeta(meta13)
X3D0.setHead(head1)
Scene14 = SceneObject()
Background15 = BackgroundObject().setSkyColor([0,0,1])
Scene14.addChild(Background15)
Transform16 = TransformObject().setDEF("Checkerboard").setTranslation([0,0,-10])
Shape17 = ShapeObject()
Appearance18 = AppearanceObject()
TextureTransform19 = TextureTransformObject().setScale([500,500])
Appearance18.setTextureTransform(TextureTransform19)
PixelTexture20 = PixelTextureObject().setImage([2,2,3,15119869,16767927,16767927,15119869])
Appearance18.setTexture(PixelTexture20)
Shape17.setAppearance(Appearance18)
Box21 = BoxObject().setSize([1000,1000,0.01])
Shape17.setGeometry(Box21)
Transform16.addChild(Shape17)
Scene14.addChild(Transform16)
Viewpoint22 = ViewpointObject().setDescription("View All").setPosition([0,0,20])
Scene14.addChild(Viewpoint22)
Viewpoint23 = ViewpointObject().setDescription("Empty Image").setPosition([0,5,5])
Scene14.addChild(Viewpoint23)
Transform24 = TransformObject().setDEF("EmptyImage").setRotation([1,1,0,1]).setTranslation([0,5,0])
Shape25 = ShapeObject()
Appearance26 = AppearanceObject()
PixelTexture27 = PixelTextureObject()
Appearance26.setTexture(PixelTexture27)
Shape25.setAppearance(Appearance26)
Box28 = BoxObject().setDEF("StandardBox")
Shape25.setGeometry(Box28)
Transform24.addChild(Shape25)
Scene14.addChild(Transform24)
Viewpoint29 = ViewpointObject().setDescription("Black and white PixelTexture").setPosition([-5,0,5])
Scene14.addChild(Viewpoint29)
Transform30 = TransformObject().setDEF("BW").setRotation([1,1,0,1]).setTranslation([-5,0,0])
Shape31 = ShapeObject()
Appearance32 = AppearanceObject()
PixelTexture33 = PixelTextureObject().setImage([1,2,1,255,0])
Appearance32.setTexture(PixelTexture33)
Shape31.setAppearance(Appearance32)
Box34 = BoxObject().setUSE("StandardBox")
Shape31.setGeometry(Box34)
Transform30.addChild(Shape31)
Scene14.addChild(Transform30)
Viewpoint35 = ViewpointObject().setDescription("Black and white with Alpha PixelTexture").setPosition([5,0,5])
Scene14.addChild(Viewpoint35)
Transform36 = TransformObject().setDEF("AlphaBW").setRotation([1,1,0,1]).setTranslation([5,0,0])
Shape37 = ShapeObject()
Appearance38 = AppearanceObject()
PixelTexture39 = PixelTextureObject().setImage([2,1,2,52479,8823])
Appearance38.setTexture(PixelTexture39)
Shape37.setAppearance(Appearance38)
Box40 = BoxObject().setUSE("StandardBox")
Shape37.setGeometry(Box40)
Transform36.addChild(Shape37)
Scene14.addChild(Transform36)
Viewpoint41 = ViewpointObject().setDescription("RGB PixelTexture").setPosition([-5,-5,5])
Scene14.addChild(Viewpoint41)
Transform42 = TransformObject().setDEF("RGB").setRotation([1,1,0,1]).setTranslation([-5,-5,0])
Shape43 = ShapeObject()
Appearance44 = AppearanceObject()
PixelTexture45 = PixelTextureObject().setImage([2,4,3,16711680,65280,0,0,0,0,16777215,16776960])
Appearance44.setTexture(PixelTexture45)
Shape43.setAppearance(Appearance44)
Box46 = BoxObject().setUSE("StandardBox")
Shape43.setGeometry(Box46)
Transform42.addChild(Shape43)
Scene14.addChild(Transform42)
Viewpoint47 = ViewpointObject().setDescription("RGB with Alpha PixelTexture").setPosition([5,-5,5])
Scene14.addChild(Viewpoint47)
Transform48 = TransformObject().setDEF("AlphaRGB").setRotation([1,1,0,1]).setTranslation([5,-5,0])
Shape49 = ShapeObject()
Appearance50 = AppearanceObject()
PixelTexture51 = PixelTextureObject().setImage([3,2,4,4278190335,16711935,65535,4278190207,16711807,65407])
Appearance50.setTexture(PixelTexture51)
Shape49.setAppearance(Appearance50)
Box52 = BoxObject().setUSE("StandardBox")
Shape49.setGeometry(Box52)
Transform48.addChild(Shape49)
Scene14.addChild(Transform48)
X3D0.setScene(Scene14)

X3D0.toFileX3D("./Table5_18PixelTexture.new.x3d")
