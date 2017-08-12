# -*- coding: UTF-8 -*-
from jnius import autoclass
from X3Dautoclass import *
X3D0 =  X3DObject()
X3D0.setProfile("Immersive")
X3D0.setVersion("3.3")

head1 = headObject()

meta2 = metaObject()
meta2.setName("title")
meta2.setContent("bub.x3d")

head1.addMeta(meta2)
meta3 = metaObject()
meta3.setName("creator")
meta3.setContent("John Carlson")

head1.addMeta(meta3)
meta4 = metaObject()
meta4.setName("description")
meta4.setContent("3 prismatic spheres")

head1.addMeta(meta4)
meta5 = metaObject()
meta5.setName("generator")
meta5.setContent("X3D-Edit, https://savage.nps.edu/X3D-Edit")

head1.addMeta(meta5)
meta6 = metaObject()
meta6.setName("identifier")
meta6.setContent("http://coderextreme.net/X3DJSONLD/bub.x3d")

head1.addMeta(meta6)
X3D0.setHead(head1)
Scene7 = SceneObject()

NavigationInfo8 = NavigationInfoObject()

Scene7.addChild(NavigationInfo8)
Background9 = BackgroundObject()
Background9.setBackUrl(["cubemap/all_probes/stpeters_cross/stpeters_back.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_back.png"])
Background9.setBottomUrl(["cubemap/all_probes/stpeters_cross/stpeters_bottom.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_bottom.png"])
Background9.setFrontUrl(["cubemap/all_probes/stpeters_cross/stpeters_front.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_front.png"])
Background9.setLeftUrl(["cubemap/all_probes/stpeters_cross/stpeters_left.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_left.png"])
Background9.setRightUrl(["cubemap/all_probes/stpeters_cross/stpeters_right.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_right.png"])
Background9.setTopUrl(["cubemap/all_probes/stpeters_cross/stpeters_top.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_top.png"])

Scene7.addChild(Background9)
Transform10 = TransformObject()

Shape11 = ShapeObject()

Appearance12 = AppearanceObject()

Material13 = MaterialObject()
Material13.setDiffuseColor([0.7,0.7,0.7])
Material13.setSpecularColor([0.5,0.5,0.5])

Appearance12.setMaterial(Material13)
ComposedCubeMapTexture14 = ComposedCubeMapTextureObject()
ComposedCubeMapTexture14.setDEF("texture")

ImageTexture15 = ImageTextureObject()
ImageTexture15.setUrl(["cubemap/all_probes/stpeters_cross/stpeters_back.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_back.png"])

ComposedCubeMapTexture14.setBack(ImageTexture15)
ImageTexture16 = ImageTextureObject()
ImageTexture16.setUrl(["cubemap/all_probes/stpeters_cross/stpeters_bottom.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_bottom.png"])

ComposedCubeMapTexture14.setBottom(ImageTexture16)
ImageTexture17 = ImageTextureObject()
ImageTexture17.setUrl(["cubemap/all_probes/stpeters_cross/stpeters_front.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_front.png"])

ComposedCubeMapTexture14.setFront(ImageTexture17)
ImageTexture18 = ImageTextureObject()
ImageTexture18.setUrl(["cubemap/all_probes/stpeters_cross/stpeters_left.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_left.png"])

ComposedCubeMapTexture14.setLeft(ImageTexture18)
ImageTexture19 = ImageTextureObject()
ImageTexture19.setUrl(["cubemap/all_probes/stpeters_cross/stpeters_right.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_right.png"])

ComposedCubeMapTexture14.setRight(ImageTexture19)
ImageTexture20 = ImageTextureObject()
ImageTexture20.setUrl(["cubemap/all_probes/stpeters_cross/stpeters_top.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_top.png"])

ComposedCubeMapTexture14.setTop(ImageTexture20)
Appearance12.setTexture(ComposedCubeMapTexture14)
ComposedShader21 = ComposedShaderObject()
ComposedShader21.setLanguage("GLSL")

field22 = fieldObject()
field22.setType(fieldObject.TYPE_SFINT32)
field22.setName("xxxcube")
field22.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field22.setValue("0")

ComposedShader21.addField(field22)
field23 = fieldObject()
field23.setType(fieldObject.TYPE_SFNODE)
field23.setName("cube")
field23.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)

ComposedCubeMapTexture24 = ComposedCubeMapTextureObject()
ComposedCubeMapTexture24.setUSE("texture")

field23.addChild(ComposedCubeMapTexture24)
ComposedShader21.addField(field23)
field25 = fieldObject()
field25.setType(fieldObject.TYPE_SFVEC3F)
field25.setName("chromaticDispertion")
field25.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field25.setValue("0.98 1 1.033")

ComposedShader21.addField(field25)
field26 = fieldObject()
field26.setType(fieldObject.TYPE_SFFLOAT)
field26.setName("bias")
field26.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field26.setValue("0.5")

ComposedShader21.addField(field26)
field27 = fieldObject()
field27.setType(fieldObject.TYPE_SFFLOAT)
field27.setName("scale")
field27.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field27.setValue("0.5")

ComposedShader21.addField(field27)
field28 = fieldObject()
field28.setType(fieldObject.TYPE_SFFLOAT)
field28.setName("power")
field28.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field28.setValue("2")

ComposedShader21.addField(field28)
field29 = fieldObject()
field29.setType(fieldObject.TYPE_SFFLOAT)
field29.setName("a")
field29.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)
field29.setValue("0.5")

ComposedShader21.addField(field29)
field30 = fieldObject()
field30.setType(fieldObject.TYPE_SFFLOAT)
field30.setName("b")
field30.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)
field30.setValue("0.5")

ComposedShader21.addField(field30)
field31 = fieldObject()
field31.setType(fieldObject.TYPE_SFFLOAT)
field31.setName("c")
field31.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)
field31.setValue("3")

ComposedShader21.addField(field31)
field32 = fieldObject()
field32.setType(fieldObject.TYPE_SFFLOAT)
field32.setName("d")
field32.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)
field32.setValue("3")

ComposedShader21.addField(field32)
field33 = fieldObject()
field33.setType(fieldObject.TYPE_SFFLOAT)
field33.setName("tdelta")
field33.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)
field33.setValue("0.5")

ComposedShader21.addField(field33)
field34 = fieldObject()
field34.setType(fieldObject.TYPE_SFFLOAT)
field34.setName("pdelta")
field34.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)
field34.setValue("0.5")

ComposedShader21.addField(field34)
ShaderPart35 = ShaderPartObject()
ShaderPart35.setType("VERTEX")
ShaderPart35.setUrl(["x3dom_flowers_chromatic.vs","http://coderextreme.net/X3DJSONLD/x3dom.vs"])

ComposedShader21.addParts(ShaderPart35)
ShaderPart36 = ShaderPartObject()
ShaderPart36.setType("FRAGMENT")
ShaderPart36.setUrl(["pc_bubbles.fs","http://coderextreme.net/X3DJSONLD/pc_bubbles.fs"])

ComposedShader21.addParts(ShaderPart36)
Appearance12.addShaders(ComposedShader21)
Shape11.setAppearance(Appearance12)
Sphere37 = SphereObject()
Sphere37.setRadius(20)

Shape11.setGeometry(Sphere37)
Transform10.addChild(Shape11)
Scene7.addChild(Transform10)
Transform38 = TransformObject()
Transform38.setTranslation([-2,0,0])

Shape39 = ShapeObject()

Appearance40 = AppearanceObject()

Material41 = MaterialObject()
Material41.setDiffuseColor([0.7,0.7,0.7])
Material41.setSpecularColor([0.5,0.5,0.5])

Appearance40.setMaterial(Material41)
ComposedCubeMapTexture42 = ComposedCubeMapTextureObject()

ImageTexture43 = ImageTextureObject()
ImageTexture43.setUrl(["cubemap/all_probes/stpeters_cross/stpeters_back.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_back.png"])

ComposedCubeMapTexture42.setBack(ImageTexture43)
ImageTexture44 = ImageTextureObject()
ImageTexture44.setUrl(["cubemap/all_probes/stpeters_cross/stpeters_bottom.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_bottom.png"])

ComposedCubeMapTexture42.setBottom(ImageTexture44)
ImageTexture45 = ImageTextureObject()
ImageTexture45.setUrl(["cubemap/all_probes/stpeters_cross/stpeters_front.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_front.png"])

ComposedCubeMapTexture42.setFront(ImageTexture45)
ImageTexture46 = ImageTextureObject()
ImageTexture46.setUrl(["cubemap/all_probes/stpeters_cross/stpeters_left.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_left.png"])

ComposedCubeMapTexture42.setLeft(ImageTexture46)
ImageTexture47 = ImageTextureObject()
ImageTexture47.setUrl(["cubemap/all_probes/stpeters_cross/stpeters_right.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_right.png"])

ComposedCubeMapTexture42.setRight(ImageTexture47)
ImageTexture48 = ImageTextureObject()
ImageTexture48.setUrl(["cubemap/all_probes/stpeters_cross/stpeters_top.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_top.png"])

ComposedCubeMapTexture42.setTop(ImageTexture48)
Appearance40.setTexture(ComposedCubeMapTexture42)
ComposedShader49 = ComposedShaderObject()
ComposedShader49.setLanguage("GLSL")

field50 = fieldObject()
field50.setType(fieldObject.TYPE_SFINT32)
field50.setName("xxxcube")
field50.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field50.setValue("0")

ComposedShader49.addField(field50)
field51 = fieldObject()
field51.setType(fieldObject.TYPE_SFNODE)
field51.setName("cube")
field51.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)

ComposedCubeMapTexture52 = ComposedCubeMapTextureObject()
ComposedCubeMapTexture52.setUSE("texture")

field51.addChild(ComposedCubeMapTexture52)
ComposedShader49.addField(field51)
field53 = fieldObject()
field53.setType(fieldObject.TYPE_SFVEC3F)
field53.setName("chromaticDispertion")
field53.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field53.setValue("0.98 1 1.033")

ComposedShader49.addField(field53)
field54 = fieldObject()
field54.setType(fieldObject.TYPE_SFFLOAT)
field54.setName("bias")
field54.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field54.setValue("0.5")

ComposedShader49.addField(field54)
field55 = fieldObject()
field55.setType(fieldObject.TYPE_SFFLOAT)
field55.setName("scale")
field55.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field55.setValue("0.5")

ComposedShader49.addField(field55)
field56 = fieldObject()
field56.setType(fieldObject.TYPE_SFFLOAT)
field56.setName("power")
field56.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field56.setValue("2")

ComposedShader49.addField(field56)
field57 = fieldObject()
field57.setType(fieldObject.TYPE_SFFLOAT)
field57.setName("a")
field57.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)
field57.setValue("0.5")

ComposedShader49.addField(field57)
field58 = fieldObject()
field58.setType(fieldObject.TYPE_SFFLOAT)
field58.setName("b")
field58.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)
field58.setValue("0.5")

ComposedShader49.addField(field58)
field59 = fieldObject()
field59.setType(fieldObject.TYPE_SFFLOAT)
field59.setName("c")
field59.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)
field59.setValue("3")

ComposedShader49.addField(field59)
field60 = fieldObject()
field60.setType(fieldObject.TYPE_SFFLOAT)
field60.setName("d")
field60.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)
field60.setValue("3")

ComposedShader49.addField(field60)
field61 = fieldObject()
field61.setType(fieldObject.TYPE_SFFLOAT)
field61.setName("tdelta")
field61.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)
field61.setValue("0.5")

ComposedShader49.addField(field61)
field62 = fieldObject()
field62.setType(fieldObject.TYPE_SFFLOAT)
field62.setName("pdelta")
field62.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)
field62.setValue("0.5")

ComposedShader49.addField(field62)
ShaderPart63 = ShaderPartObject()
ShaderPart63.setType("VERTEX")
ShaderPart63.setUrl(["x3dom_flowers_chromatic.vs","http://coderextreme.net/X3DJSONLD/x3dom.vs"])

ComposedShader49.addParts(ShaderPart63)
ShaderPart64 = ShaderPartObject()
ShaderPart64.setType("FRAGMENT")
ShaderPart64.setUrl(["pc_bubbles.fs","http://coderextreme.net/X3DJSONLD/pc_bubbles.fs"])

ComposedShader49.addParts(ShaderPart64)
Appearance40.addShaders(ComposedShader49)
Shape39.setAppearance(Appearance40)
Sphere65 = SphereObject()
Sphere65.setRadius(20)

Shape39.setGeometry(Sphere65)
Transform38.addChild(Shape39)
Scene7.addChild(Transform38)
Transform66 = TransformObject()
Transform66.setTranslation([2,0,0])

Shape67 = ShapeObject()

Appearance68 = AppearanceObject()

Material69 = MaterialObject()
Material69.setDiffuseColor([0.7,0.7,0.7])
Material69.setSpecularColor([0.5,0.5,0.5])

Appearance68.setMaterial(Material69)
ComposedCubeMapTexture70 = ComposedCubeMapTextureObject()

ImageTexture71 = ImageTextureObject()
ImageTexture71.setUrl(["cubemap/all_probes/stpeters_cross/stpeters_back.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_back.png"])

ComposedCubeMapTexture70.setBack(ImageTexture71)
ImageTexture72 = ImageTextureObject()
ImageTexture72.setUrl(["cubemap/all_probes/stpeters_cross/stpeters_bottom.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_bottom.png"])

ComposedCubeMapTexture70.setBottom(ImageTexture72)
ImageTexture73 = ImageTextureObject()
ImageTexture73.setUrl(["cubemap/all_probes/stpeters_cross/stpeters_front.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_front.png"])

ComposedCubeMapTexture70.setFront(ImageTexture73)
ImageTexture74 = ImageTextureObject()
ImageTexture74.setUrl(["cubemap/all_probes/stpeters_cross/stpeters_left.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_left.png"])

ComposedCubeMapTexture70.setLeft(ImageTexture74)
ImageTexture75 = ImageTextureObject()
ImageTexture75.setUrl(["cubemap/all_probes/stpeters_cross/stpeters_right.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_right.png"])

ComposedCubeMapTexture70.setRight(ImageTexture75)
ImageTexture76 = ImageTextureObject()
ImageTexture76.setUrl(["cubemap/all_probes/stpeters_cross/stpeters_top.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_top.png"])

ComposedCubeMapTexture70.setTop(ImageTexture76)
Appearance68.setTexture(ComposedCubeMapTexture70)
ComposedShader77 = ComposedShaderObject()
ComposedShader77.setLanguage("GLSL")

field78 = fieldObject()
field78.setType(fieldObject.TYPE_SFINT32)
field78.setName("xxxcube")
field78.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field78.setValue("0")

ComposedShader77.addField(field78)
field79 = fieldObject()
field79.setType(fieldObject.TYPE_SFNODE)
field79.setName("cube")
field79.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)

ComposedCubeMapTexture80 = ComposedCubeMapTextureObject()
ComposedCubeMapTexture80.setUSE("texture")

field79.addChild(ComposedCubeMapTexture80)
ComposedShader77.addField(field79)
field81 = fieldObject()
field81.setType(fieldObject.TYPE_SFVEC3F)
field81.setName("chromaticDispertion")
field81.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field81.setValue("0.98 1 1.033")

ComposedShader77.addField(field81)
field82 = fieldObject()
field82.setType(fieldObject.TYPE_SFFLOAT)
field82.setName("bias")
field82.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field82.setValue("0.5")

ComposedShader77.addField(field82)
field83 = fieldObject()
field83.setType(fieldObject.TYPE_SFFLOAT)
field83.setName("scale")
field83.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field83.setValue("0.5")

ComposedShader77.addField(field83)
field84 = fieldObject()
field84.setType(fieldObject.TYPE_SFFLOAT)
field84.setName("power")
field84.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field84.setValue("2")

ComposedShader77.addField(field84)
field85 = fieldObject()
field85.setType(fieldObject.TYPE_SFFLOAT)
field85.setName("a")
field85.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)
field85.setValue("0.5")

ComposedShader77.addField(field85)
field86 = fieldObject()
field86.setType(fieldObject.TYPE_SFFLOAT)
field86.setName("b")
field86.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)
field86.setValue("0.5")

ComposedShader77.addField(field86)
field87 = fieldObject()
field87.setType(fieldObject.TYPE_SFFLOAT)
field87.setName("c")
field87.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)
field87.setValue("3")

ComposedShader77.addField(field87)
field88 = fieldObject()
field88.setType(fieldObject.TYPE_SFFLOAT)
field88.setName("d")
field88.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)
field88.setValue("3")

ComposedShader77.addField(field88)
field89 = fieldObject()
field89.setType(fieldObject.TYPE_SFFLOAT)
field89.setName("tdelta")
field89.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)
field89.setValue("0.5")

ComposedShader77.addField(field89)
field90 = fieldObject()
field90.setType(fieldObject.TYPE_SFFLOAT)
field90.setName("pdelta")
field90.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)
field90.setValue("0.5")

ComposedShader77.addField(field90)
ShaderPart91 = ShaderPartObject()
ShaderPart91.setType("VERTEX")
ShaderPart91.setUrl(["x3dom_flowers_plain.vs","http://coderextreme.net/X3DJSONLD/x3dom_flowers_plain.vs"])

ComposedShader77.addParts(ShaderPart91)
ShaderPart92 = ShaderPartObject()
ShaderPart92.setType("FRAGMENT")
ShaderPart92.setUrl(["plain.fs","http://coderextreme.net/X3DJSONLD/pc_bubbles.fs"])

ComposedShader77.addParts(ShaderPart92)
Appearance68.addShaders(ComposedShader77)
Shape67.setAppearance(Appearance68)
Sphere93 = SphereObject()
Sphere93.setRadius(20)

Shape67.setGeometry(Sphere93)
Transform66.addChild(Shape67)
Scene7.addChild(Transform66)
X3D0.setScene(Scene7)

X3D0.toFileX3D("./x3domflower.new.x3d")
