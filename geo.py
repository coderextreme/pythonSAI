from jnius import autoclass
from X3Dautoclass import *
X3D0 =  X3DObject().setProfile("Immersive").setVersion("3.3")
head1 = headObject()
meta2 = metaObject().setName("title").setContent("geo.x3d")
head1.addMeta(meta2)
meta3 = metaObject().setName("creator").setContent("John Carlson")
head1.addMeta(meta3)
meta4 = metaObject().setName("generator").setContent("manual")
head1.addMeta(meta4)
meta5 = metaObject().setName("identifier").setContent("http://coderextreme.net/X3DJSONLD/geo.x3d")
head1.addMeta(meta5)
meta6 = metaObject().setName("description").setContent("a sphere")
head1.addMeta(meta6)
X3D0.setHead(head1)
Scene7 = SceneObject()
NavigationInfo8 = NavigationInfoObject().setType(["EXAMINE"])
Scene7.addChild(NavigationInfo8)
Viewpoint9 = ViewpointObject().setDEF("Tour").setDescription("Tour Views")
Scene7.addChild(Viewpoint9)
Viewpoint10 = ViewpointObject().setPosition([0,0,4]).setDescription("sphere in road")
Scene7.addChild(Viewpoint10)
Background11 = BackgroundObject().setBackUrl(["bBK.png","http://coderextreme.net/bug/bBK.png"]).setBottomUrl(["bBT.png","http://coderextreme.net/bug/bBT.png"]).setFrontUrl(["bFR.png","http://coderextreme.net/bug/bFR.png"]).setLeftUrl(["bLF.png","http://coderextreme.net/bug/bLF.png"]).setRightUrl(["bRT.png","http://coderextreme.net/bug/bRT.png"]).setTopUrl(["bTP.png","http://coderextreme.net/bug/bTP.png"])
Scene7.addChild(Background11)
Transform12 = TransformObject().setDEF("Rose01")
Shape13 = ShapeObject()
Sphere14 = SphereObject()
Shape13.setGeometry(Sphere14)
Appearance15 = AppearanceObject().setDEF("_01_-_Default")
Material16 = MaterialObject().setDiffuseColor([0.7,0.7,0.7]).setSpecularColor([0.5,0.5,0.5])
Appearance15.setMaterial(Material16)
ComposedCubeMapTexture17 = ComposedCubeMapTextureObject()
ImageTexture18 = ImageTextureObject().setUrl(["bBK.png","http://coderextreme.net/bug/bBK.png"])
ComposedCubeMapTexture17.setBack(ImageTexture18)
ImageTexture19 = ImageTextureObject().setUrl(["bBT.png","http://coderextreme.net/bug/bBT.png"])
ComposedCubeMapTexture17.setBottom(ImageTexture19)
ImageTexture20 = ImageTextureObject().setUrl(["bFR.png","http://coderextreme.net/bug/bFR.png"])
ComposedCubeMapTexture17.setFront(ImageTexture20)
ImageTexture21 = ImageTextureObject().setUrl(["bLF.png","http://coderextreme.net/bug/bLF.png"])
ComposedCubeMapTexture17.setLeft(ImageTexture21)
ImageTexture22 = ImageTextureObject().setUrl(["bRT.png","http://coderextreme.net/bug/bRT.png"])
ComposedCubeMapTexture17.setRight(ImageTexture22)
ImageTexture23 = ImageTextureObject().setUrl(["bTP.png","http://coderextreme.net/bug/bTP.png"])
ComposedCubeMapTexture17.setTop(ImageTexture23)
Appearance15.setTexture(ComposedCubeMapTexture17)
ComposedShader24 = ComposedShaderObject().setDEF("cobweb").setLanguage("GLSL")
field25 = fieldObject().setType(fieldObject.TYPE_SFINT32).setName("cube").setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT).setValue("0")
ComposedShader24.addField(field25)
field26 = fieldObject().setType(fieldObject.TYPE_SFVEC3F).setName("chromaticDispertion").setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT).setValue("0.98 1 1.033")
ComposedShader24.addField(field26)
field27 = fieldObject().setType(fieldObject.TYPE_SFFLOAT).setName("bias").setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT).setValue("0.5")
ComposedShader24.addField(field27)
field28 = fieldObject().setType(fieldObject.TYPE_SFFLOAT).setName("scale").setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT).setValue("0.5")
ComposedShader24.addField(field28)
field29 = fieldObject().setType(fieldObject.TYPE_SFFLOAT).setName("power").setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT).setValue("2")
ComposedShader24.addField(field29)
ShaderPart30 = ShaderPartObject().setType("VERTEX").setUrl(["cobweb.vs","http://coderextreme.net/X3DJSONLD/cobweb.vs"])
ComposedShader24.addParts(ShaderPart30)
ShaderPart31 = ShaderPartObject().setType("FRAGMENT").setUrl(["pc_bubbles.fs","http://coderextreme.net/X3DJSONLD/pc_bubbles.fs"])
ComposedShader24.addParts(ShaderPart31)
Appearance15.addShaders(ComposedShader24)
ComposedShader32 = ComposedShaderObject().setDEF("x3dom").setLanguage("GLSL")
field33 = fieldObject().setType(fieldObject.TYPE_SFINT32).setName("cube").setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT).setValue("0")
ComposedShader32.addField(field33)
field34 = fieldObject().setType(fieldObject.TYPE_SFVEC3F).setName("chromaticDispertion").setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT).setValue("0.98 1 1.033")
ComposedShader32.addField(field34)
field35 = fieldObject().setType(fieldObject.TYPE_SFFLOAT).setName("bias").setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT).setValue("0.5")
ComposedShader32.addField(field35)
field36 = fieldObject().setType(fieldObject.TYPE_SFFLOAT).setName("scale").setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT).setValue("0.5")
ComposedShader32.addField(field36)
field37 = fieldObject().setType(fieldObject.TYPE_SFFLOAT).setName("power").setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT).setValue("2")
ComposedShader32.addField(field37)
ShaderPart38 = ShaderPartObject().setType("VERTEX").setUrl(["x3dom.vs","http://coderextreme.net/X3DJSONLD/x3dom.vs"])
ComposedShader32.addParts(ShaderPart38)
ShaderPart39 = ShaderPartObject().setType("FRAGMENT").setUrl(["pc_bubbles.fs","http://coderextreme.net/X3DJSONLD/pc_bubbles.fs"])
ComposedShader32.addParts(ShaderPart39)
Appearance15.addShaders(ComposedShader32)
Shape13.setAppearance(Appearance15)
Transform12.addChild(Shape13)
Scene7.addChild(Transform12)
X3D0.setScene(Scene7)

X3D0.toFileX3D("./geo.new.x3d")
