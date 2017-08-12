# -*- coding: UTF-8 -*-
from jnius import autoclass
from X3Dautoclass import *
X3D0 =  X3DObject()
X3D0.setProfile("Immersive")
X3D0.setVersion("3.3")

head1 = headObject()

meta2 = metaObject()
meta2.setName("title")
meta2.setContent("geo.x3d")

head1.addMeta(meta2)
meta3 = metaObject()
meta3.setName("creator")
meta3.setContent("John Carlson")

head1.addMeta(meta3)
meta4 = metaObject()
meta4.setName("generator")
meta4.setContent("manual")

head1.addMeta(meta4)
meta5 = metaObject()
meta5.setName("identifier")
meta5.setContent("http://coderextreme.net/X3DJSONLD/geo.x3d")

head1.addMeta(meta5)
meta6 = metaObject()
meta6.setName("description")
meta6.setContent("a sphere")

head1.addMeta(meta6)
X3D0.setHead(head1)
Scene7 = SceneObject()

NavigationInfo8 = NavigationInfoObject()
NavigationInfo8.setType(["EXAMINE"])

Scene7.addChild(NavigationInfo8)
Viewpoint9 = ViewpointObject()
Viewpoint9.setDEF("Tour")
Viewpoint9.setDescription("Tour Views")

Scene7.addChild(Viewpoint9)
Viewpoint10 = ViewpointObject()
Viewpoint10.setPosition([0,0,4])
Viewpoint10.setDescription("sphere in road")

Scene7.addChild(Viewpoint10)
Background11 = BackgroundObject()
Background11.setBackUrl(["bBK.png","http://coderextreme.net/bug/bBK.png"])
Background11.setBottomUrl(["bBT.png","http://coderextreme.net/bug/bBT.png"])
Background11.setFrontUrl(["bFR.png","http://coderextreme.net/bug/bFR.png"])
Background11.setLeftUrl(["bLF.png","http://coderextreme.net/bug/bLF.png"])
Background11.setRightUrl(["bRT.png","http://coderextreme.net/bug/bRT.png"])
Background11.setTopUrl(["bTP.png","http://coderextreme.net/bug/bTP.png"])

Scene7.addChild(Background11)
Transform12 = TransformObject()
Transform12.setDEF("Rose01")

Shape13 = ShapeObject()

Sphere14 = SphereObject()

Shape13.setGeometry(Sphere14)
Appearance15 = AppearanceObject()
Appearance15.setDEF("_01_-_Default")

Material16 = MaterialObject()
Material16.setDiffuseColor([0.7,0.7,0.7])
Material16.setSpecularColor([0.5,0.5,0.5])

Appearance15.setMaterial(Material16)
ComposedCubeMapTexture17 = ComposedCubeMapTextureObject()

ImageTexture18 = ImageTextureObject()
ImageTexture18.setUrl(["bBK.png","http://coderextreme.net/bug/bBK.png"])

ComposedCubeMapTexture17.setBack(ImageTexture18)
ImageTexture19 = ImageTextureObject()
ImageTexture19.setUrl(["bBT.png","http://coderextreme.net/bug/bBT.png"])

ComposedCubeMapTexture17.setBottom(ImageTexture19)
ImageTexture20 = ImageTextureObject()
ImageTexture20.setUrl(["bFR.png","http://coderextreme.net/bug/bFR.png"])

ComposedCubeMapTexture17.setFront(ImageTexture20)
ImageTexture21 = ImageTextureObject()
ImageTexture21.setUrl(["bLF.png","http://coderextreme.net/bug/bLF.png"])

ComposedCubeMapTexture17.setLeft(ImageTexture21)
ImageTexture22 = ImageTextureObject()
ImageTexture22.setUrl(["bRT.png","http://coderextreme.net/bug/bRT.png"])

ComposedCubeMapTexture17.setRight(ImageTexture22)
ImageTexture23 = ImageTextureObject()
ImageTexture23.setUrl(["bTP.png","http://coderextreme.net/bug/bTP.png"])

ComposedCubeMapTexture17.setTop(ImageTexture23)
Appearance15.setTexture(ComposedCubeMapTexture17)
ComposedShader24 = ComposedShaderObject()
ComposedShader24.setDEF("cobweb")
ComposedShader24.setLanguage("GLSL")

field25 = fieldObject()
field25.setType(fieldObject.TYPE_SFINT32)
field25.setName("cube")
field25.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field25.setValue("0")

ComposedShader24.addField(field25)
field26 = fieldObject()
field26.setType(fieldObject.TYPE_SFVEC3F)
field26.setName("chromaticDispertion")
field26.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field26.setValue("0.98 1 1.033")

ComposedShader24.addField(field26)
field27 = fieldObject()
field27.setType(fieldObject.TYPE_SFFLOAT)
field27.setName("bias")
field27.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field27.setValue("0.5")

ComposedShader24.addField(field27)
field28 = fieldObject()
field28.setType(fieldObject.TYPE_SFFLOAT)
field28.setName("scale")
field28.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field28.setValue("0.5")

ComposedShader24.addField(field28)
field29 = fieldObject()
field29.setType(fieldObject.TYPE_SFFLOAT)
field29.setName("power")
field29.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field29.setValue("2")

ComposedShader24.addField(field29)
ShaderPart30 = ShaderPartObject()
ShaderPart30.setType("VERTEX")
ShaderPart30.setUrl(["cobweb.vs","http://coderextreme.net/X3DJSONLD/cobweb.vs"])

ComposedShader24.addParts(ShaderPart30)
ShaderPart31 = ShaderPartObject()
ShaderPart31.setType("FRAGMENT")
ShaderPart31.setUrl(["pc_bubbles.fs","http://coderextreme.net/X3DJSONLD/pc_bubbles.fs"])

ComposedShader24.addParts(ShaderPart31)
Appearance15.addShaders(ComposedShader24)
ComposedShader32 = ComposedShaderObject()
ComposedShader32.setDEF("x3dom")
ComposedShader32.setLanguage("GLSL")

field33 = fieldObject()
field33.setType(fieldObject.TYPE_SFINT32)
field33.setName("cube")
field33.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field33.setValue("0")

ComposedShader32.addField(field33)
field34 = fieldObject()
field34.setType(fieldObject.TYPE_SFVEC3F)
field34.setName("chromaticDispertion")
field34.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field34.setValue("0.98 1 1.033")

ComposedShader32.addField(field34)
field35 = fieldObject()
field35.setType(fieldObject.TYPE_SFFLOAT)
field35.setName("bias")
field35.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field35.setValue("0.5")

ComposedShader32.addField(field35)
field36 = fieldObject()
field36.setType(fieldObject.TYPE_SFFLOAT)
field36.setName("scale")
field36.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field36.setValue("0.5")

ComposedShader32.addField(field36)
field37 = fieldObject()
field37.setType(fieldObject.TYPE_SFFLOAT)
field37.setName("power")
field37.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field37.setValue("2")

ComposedShader32.addField(field37)
ShaderPart38 = ShaderPartObject()
ShaderPart38.setType("VERTEX")
ShaderPart38.setUrl(["x3dom.vs","http://coderextreme.net/X3DJSONLD/x3dom.vs"])

ComposedShader32.addParts(ShaderPart38)
ShaderPart39 = ShaderPartObject()
ShaderPart39.setType("FRAGMENT")
ShaderPart39.setUrl(["pc_bubbles.fs","http://coderextreme.net/X3DJSONLD/pc_bubbles.fs"])

ComposedShader32.addParts(ShaderPart39)
Appearance15.addShaders(ComposedShader32)
Shape13.setAppearance(Appearance15)
Transform12.addChild(Shape13)
Scene7.addChild(Transform12)
X3D0.setScene(Scene7)

X3D0.toFileX3D("./geo.new.x3d")
