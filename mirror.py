from jnius import autoclass
from X3Dautoclass import *
X3D0 =  X3DObject().setProfile("Immersive").setVersion("3.3")
head1 = headObject()
component2 = componentObject().setName("EnvironmentalEffects").setLevel(3)
head1.addComponent(component2)
meta3 = metaObject().setName("title").setContent("mirror.x3d")
head1.addMeta(meta3)
meta4 = metaObject().setName("creator").setContent("John Carlson")
head1.addMeta(meta4)
meta5 = metaObject().setName("generator").setContent("manual")
head1.addMeta(meta5)
meta6 = metaObject().setName("identifier").setContent("http://coderextreme.net/X3DJSONLD/mirror.x3d")
head1.addMeta(meta6)
meta7 = metaObject().setName("description").setContent("sphere with alternating backgrounds")
head1.addMeta(meta7)
meta8 = metaObject().setName("translated").setContent("10 May 2017")
head1.addMeta(meta8)
meta9 = metaObject().setName("generator").setContent("X3dToJson.xslt, http://www.web3d.org/x3d/stylesheets/X3dToJson.html")
head1.addMeta(meta9)
meta10 = metaObject().setName("reference").setContent("X3D JSON encoding: http://www.web3d.org/wiki/index.php/X3D_JSON_Encoding")
head1.addMeta(meta10)
meta11 = metaObject().setName("translated").setContent("10 May 2017")
head1.addMeta(meta11)
meta12 = metaObject().setName("generator").setContent("X3DJSONLD: https://github.com/coderextreme/X3DJSONLD")
head1.addMeta(meta12)
X3D0.setHead(head1)
Scene13 = SceneObject()
Viewpoint14 = ViewpointObject().setPosition([0,5,100]).setDescription("Switch background and cubemap texture")
Scene13.addChild(Viewpoint14)
TextureBackground15 = TextureBackgroundObject()
ImageTexture16 = ImageTextureObject().setDEF("leftBack").setUrl(["cubemap/all_probes/beach_cross/beach_left.png","http://coderextreme.net/cubemap/all_probes/beach_cross/beach_left.png"])
TextureBackground15.setLeftTexture(ImageTexture16)
ImageTexture17 = ImageTextureObject().setDEF("rightBack").setUrl(["cubemap/all_probes/beach_cross/beach_right.png","http://coderextreme.net/cubemap/all_probes/beach_cross/beach_right.png"])
TextureBackground15.setRightTexture(ImageTexture17)
ImageTexture18 = ImageTextureObject().setDEF("frontBack").setUrl(["cubemap/all_probes/beach_cross/beach_front.png","http://coderextreme.net/cubemap/all_probes/beach_cross/beach_front.png"])
TextureBackground15.setFrontTexture(ImageTexture18)
ImageTexture19 = ImageTextureObject().setDEF("backBack").setUrl(["cubemap/all_probes/beach_cross/beach_back.png","http://coderextreme.net/cubemap/all_probes/beach_cross/beach_back.png"])
TextureBackground15.setBackTexture(ImageTexture19)
ImageTexture20 = ImageTextureObject().setDEF("topBack").setUrl(["cubemap/all_probes/beach_cross/beach_top.png","http://coderextreme.net/cubemap/all_probes/beach_cross/beach_top.png"])
TextureBackground15.setTopTexture(ImageTexture20)
ImageTexture21 = ImageTextureObject().setDEF("bottomBack").setUrl(["cubemap/all_probes/beach_cross/beach_bottom.png","http://coderextreme.net/cubemap/all_probes/beach_cross/beach_bottom.png"])
TextureBackground15.setBottomTexture(ImageTexture21)
Scene13.addChild(TextureBackground15)
Transform22 = TransformObject()
Shape23 = ShapeObject()
Appearance24 = AppearanceObject()
Material25 = MaterialObject().setDiffuseColor([0.7,0.7,0.7]).setSpecularColor([0.5,0.5,0.5])
Appearance24.setMaterial(Material25)
ComposedCubeMapTexture26 = ComposedCubeMapTextureObject()
ImageTexture27 = ImageTextureObject().setDEF("backShader").setUrl(["cubemap/all_probes/beach_cross/beach_back.png","http://coderextreme.net/cubemap/all_probes/beach_cross/beach_back.png"])
ComposedCubeMapTexture26.setBack(ImageTexture27)
ImageTexture28 = ImageTextureObject().setDEF("bottomShader").setUrl(["cubemap/all_probes/beach_cross/beach_bottom.png","http://coderextreme.net/cubemap/all_probes/beach_cross/beach_bottom.png"])
ComposedCubeMapTexture26.setBottom(ImageTexture28)
ImageTexture29 = ImageTextureObject().setDEF("frontShader").setUrl(["cubemap/all_probes/beach_cross/beach_front.png","http://coderextreme.net/cubemap/all_probes/beach_cross/beach_front.png"])
ComposedCubeMapTexture26.setFront(ImageTexture29)
ImageTexture30 = ImageTextureObject().setDEF("leftShader").setUrl(["cubemap/all_probes/beach_cross/beach_left.png","http://coderextreme.net/cubemap/all_probes/beach_cross/beach_left.png"])
ComposedCubeMapTexture26.setLeft(ImageTexture30)
ImageTexture31 = ImageTextureObject().setDEF("rightShader").setUrl(["cubemap/all_probes/beach_cross/beach_right.png","http://coderextreme.net/cubemap/all_probes/beach_cross/beach_right.png"])
ComposedCubeMapTexture26.setRight(ImageTexture31)
ImageTexture32 = ImageTextureObject().setDEF("topShader").setUrl(["cubemap/all_probes/beach_cross/beach_top.png","http://coderextreme.net/cubemap/all_probes/beach_cross/beach_top.png"])
ComposedCubeMapTexture26.setTop(ImageTexture32)
Appearance24.setTexture(ComposedCubeMapTexture26)
ComposedShader33 = ComposedShaderObject().setDEF("x3dom").setLanguage("GLSL")

ComposedShader33.addComments(CommentsBlock("http://hypertextbook.com/facts/2005/JustinChe.shtml"))
field34 = fieldObject().setType(fieldObject.TYPE_SFVEC3F).setName("chromaticDispertion").setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT).setValue("0.98 1 1.033")
ComposedShader33.addField(field34)
field35 = fieldObject().setType(fieldObject.TYPE_SFINT32).setName("cube").setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT).setValue("0")
ComposedShader33.addField(field35)
field36 = fieldObject().setType(fieldObject.TYPE_SFFLOAT).setName("bias").setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT).setValue("0.5")
ComposedShader33.addField(field36)
field37 = fieldObject().setType(fieldObject.TYPE_SFFLOAT).setName("scale").setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT).setValue("0.5")
ComposedShader33.addField(field37)
field38 = fieldObject().setType(fieldObject.TYPE_SFFLOAT).setName("power").setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT).setValue("2")
ComposedShader33.addField(field38)
ShaderPart39 = ShaderPartObject().setType("VERTEX").setUrl(["x3dom.vs","http://coderextreme.net/X3DJSONLD/x3dom.vs"])
ComposedShader33.addParts(ShaderPart39)
ShaderPart40 = ShaderPartObject().setType("FRAGMENT").setUrl(["mix.fs","http://coderextreme.net/X3DJSONLD/mix.fs"])
ComposedShader33.addParts(ShaderPart40)
Appearance24.addShaders(ComposedShader33)
ComposedShader41 = ComposedShaderObject().setDEF("cobweb").setLanguage("GLSL")

ComposedShader41.addComments(CommentsBlock("http://hypertextbook.com/facts/2005/JustinChe.shtml"))
field42 = fieldObject().setType(fieldObject.TYPE_SFVEC3F).setName("chromaticDispertion").setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT).setValue("0.98 1 1.033")
ComposedShader41.addField(field42)
field43 = fieldObject().setType(fieldObject.TYPE_SFINT32).setName("cube").setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT).setValue("0")
ComposedShader41.addField(field43)
field44 = fieldObject().setType(fieldObject.TYPE_SFFLOAT).setName("bias").setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT).setValue("0.5")
ComposedShader41.addField(field44)
field45 = fieldObject().setType(fieldObject.TYPE_SFFLOAT).setName("scale").setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT).setValue("0.5")
ComposedShader41.addField(field45)
field46 = fieldObject().setType(fieldObject.TYPE_SFFLOAT).setName("power").setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT).setValue("2")
ComposedShader41.addField(field46)
ShaderPart47 = ShaderPartObject().setType("VERTEX").setUrl(["cobweb.vs","http://coderextreme.net/X3DJSONLD/cobweb.vs"])
ComposedShader41.addParts(ShaderPart47)
ShaderPart48 = ShaderPartObject().setType("FRAGMENT").setUrl(["mix.fs","http://coderextreme.net/X3DJSONLD/mix.fs"])
ComposedShader41.addParts(ShaderPart48)
Appearance24.addShaders(ComposedShader41)
Shape23.setAppearance(Appearance24)
Sphere49 = SphereObject().setRadius(30)
Shape23.setGeometry(Sphere49)
Transform22.addChild(Shape23)
Script50 = ScriptObject().setDEF("UrlSelector").setDirectOutput(True)
field51 = fieldObject().setType(fieldObject.TYPE_MFSTRING).setName("frontUrls").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setValue("\"cubemap/all_probes/beach_cross/beach_front.png\" \"cubemap/all_probes/building_cross/building_front.png\" \"cubemap/all_probes/campus_cross/campus_front.png\" \"cubemap/all_probes/galileo_cross/galileo_front.png\" \"cubemap/all_probes/grace_cross/grace_front.png\" \"cubemap/all_probes/kitchen_cross/kitchen_front.png\" \"cubemap/all_probes/rnl_cross/rnl_front.png\" \"cubemap/all_probes/stpeters_cross/stpeters_front.png\" \"cubemap/all_probes/uffizi_cross/uffizi_front.png\"")
Script50.addField(field51)
field52 = fieldObject().setType(fieldObject.TYPE_MFSTRING).setName("backUrls").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setValue("\"cubemap/all_probes/beach_cross/beach_back.png\" \"cubemap/all_probes/building_cross/building_back.png\" \"cubemap/all_probes/campus_cross/campus_back.png\" \"cubemap/all_probes/galileo_cross/galileo_back.png\" \"cubemap/all_probes/grace_cross/grace_back.png\" \"cubemap/all_probes/kitchen_cross/kitchen_back.png\" \"cubemap/all_probes/rnl_cross/rnl_back.png\" \"cubemap/all_probes/stpeters_cross/stpeters_back.png\" \"cubemap/all_probes/uffizi_cross/uffizi_back.png\"")
Script50.addField(field52)
field53 = fieldObject().setType(fieldObject.TYPE_MFSTRING).setName("leftUrls").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setValue("\"cubemap/all_probes/beach_cross/beach_left.png\" \"cubemap/all_probes/building_cross/building_left.png\" \"cubemap/all_probes/campus_cross/campus_left.png\" \"cubemap/all_probes/galileo_cross/galileo_left.png\" \"cubemap/all_probes/grace_cross/grace_left.png\" \"cubemap/all_probes/kitchen_cross/kitchen_left.png\" \"cubemap/all_probes/rnl_cross/rnl_left.png\" \"cubemap/all_probes/stpeters_cross/stpeters_left.png\" \"cubemap/all_probes/uffizi_cross/uffizi_left.png\"")
Script50.addField(field53)
field54 = fieldObject().setType(fieldObject.TYPE_MFSTRING).setName("rightUrls").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setValue("\"cubemap/all_probes/beach_cross/beach_right.png\" \"cubemap/all_probes/building_cross/building_right.png\" \"cubemap/all_probes/campus_cross/campus_right.png\" \"cubemap/all_probes/galileo_cross/galileo_right.png\" \"cubemap/all_probes/grace_cross/grace_right.png\" \"cubemap/all_probes/kitchen_cross/kitchen_right.png\" \"cubemap/all_probes/rnl_cross/rnl_right.png\" \"cubemap/all_probes/stpeters_cross/stpeters_right.png\" \"cubemap/all_probes/uffizi_cross/uffizi_right.png\"")
Script50.addField(field54)
field55 = fieldObject().setType(fieldObject.TYPE_MFSTRING).setName("topUrls").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setValue("\"cubemap/all_probes/beach_cross/beach_top.png\" \"cubemap/all_probes/building_cross/building_top.png\" \"cubemap/all_probes/campus_cross/campus_top.png\" \"cubemap/all_probes/galileo_cross/galileo_top.png\" \"cubemap/all_probes/grace_cross/grace_top.png\" \"cubemap/all_probes/kitchen_cross/kitchen_top.png\" \"cubemap/all_probes/rnl_cross/rnl_top.png\" \"cubemap/all_probes/stpeters_cross/stpeters_top.png\" \"cubemap/all_probes/uffizi_cross/uffizi_top.png\"")
Script50.addField(field55)
field56 = fieldObject().setType(fieldObject.TYPE_MFSTRING).setName("bottomUrls").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY).setValue("\"cubemap/all_probes/beach_cross/beach_bottom.png\" \"cubemap/all_probes/building_cross/building_bottom.png\" \"cubemap/all_probes/campus_cross/campus_bottom.png\" \"cubemap/all_probes/galileo_cross/galileo_bottom.png\" \"cubemap/all_probes/grace_cross/grace_bottom.png\" \"cubemap/all_probes/kitchen_cross/kitchen_bottom.png\" \"cubemap/all_probes/rnl_cross/rnl_bottom.png\" \"cubemap/all_probes/stpeters_cross/stpeters_bottom.png\" \"cubemap/all_probes/uffizi_cross/uffizi_bottom.png\"")
Script50.addField(field56)
field57 = fieldObject().setType(fieldObject.TYPE_MFSTRING).setName("front_changed").setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY)
Script50.addField(field57)
field58 = fieldObject().setType(fieldObject.TYPE_MFSTRING).setName("back_changed").setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY)
Script50.addField(field58)
field59 = fieldObject().setType(fieldObject.TYPE_MFSTRING).setName("left_changed").setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY)
Script50.addField(field59)
field60 = fieldObject().setType(fieldObject.TYPE_MFSTRING).setName("right_changed").setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY)
Script50.addField(field60)
field61 = fieldObject().setType(fieldObject.TYPE_MFSTRING).setName("top_changed").setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY)
Script50.addField(field61)
field62 = fieldObject().setType(fieldObject.TYPE_MFSTRING).setName("bottom_changed").setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY)
Script50.addField(field62)
field63 = fieldObject().setType(fieldObject.TYPE_SFFLOAT).setName("set_fraction").setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)
Script50.addField(field63)
field64 = fieldObject().setType(fieldObject.TYPE_SFINT32).setName("old").setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT).setValue("-1")
Script50.addField(field64)

Script50.setSourceCode("ecmascript:\n"+
"        function set_fraction( f, tm ) {\n"+
"	    var side = Math.floor(f*frontUrls.length);\n"+
"	    if (side > frontUrls.length-1) {\n"+
"	    	side = 0;\n"+
"	    }\n"+
"	    if (side != old) {\n"+
"	    	    Browser.print(f+\" \"+side);\n"+
"	    	    old = side;\n"+
"		    front_changed[0] = frontUrls[side];\n"+
"		    back_changed[0] = backUrls[side];\n"+
"		    left_changed[0] = leftUrls[side];\n"+
"		    right_changed[0] = rightUrls[side];\n"+
"		    top_changed[0] = topUrls[side];\n"+
"		    bottom_changed[0] = bottomUrls[side];\n"+
"            }\n"+
"        }\n"+
"")
Transform22.addChild(Script50)
TimeSensor65 = TimeSensorObject().setDEF("Clock").setCycleInterval(45).setLoop(True)
Transform22.addChild(TimeSensor65)
ROUTE66 = ROUTEObject().setFromNode("Clock").setFromField("fraction_changed").setToNode("UrlSelector").setToField("set_fraction")
Transform22.addChild(ROUTE66)
ROUTE67 = ROUTEObject().setFromNode("UrlSelector").setFromField("front_changed").setToNode("frontBack").setToField("url")
Transform22.addChild(ROUTE67)
ROUTE68 = ROUTEObject().setFromNode("UrlSelector").setFromField("back_changed").setToNode("backBack").setToField("url")
Transform22.addChild(ROUTE68)
ROUTE69 = ROUTEObject().setFromNode("UrlSelector").setFromField("left_changed").setToNode("leftBack").setToField("url")
Transform22.addChild(ROUTE69)
ROUTE70 = ROUTEObject().setFromNode("UrlSelector").setFromField("right_changed").setToNode("rightBack").setToField("url")
Transform22.addChild(ROUTE70)
ROUTE71 = ROUTEObject().setFromNode("UrlSelector").setFromField("top_changed").setToNode("topBack").setToField("url")
Transform22.addChild(ROUTE71)
ROUTE72 = ROUTEObject().setFromNode("UrlSelector").setFromField("bottom_changed").setToNode("bottomBack").setToField("url")
Transform22.addChild(ROUTE72)
ROUTE73 = ROUTEObject().setFromNode("UrlSelector").setFromField("front_changed").setToNode("frontShader").setToField("url")
Transform22.addChild(ROUTE73)
ROUTE74 = ROUTEObject().setFromNode("UrlSelector").setFromField("back_changed").setToNode("backShader").setToField("url")
Transform22.addChild(ROUTE74)
ROUTE75 = ROUTEObject().setFromNode("UrlSelector").setFromField("left_changed").setToNode("leftShader").setToField("url")
Transform22.addChild(ROUTE75)
ROUTE76 = ROUTEObject().setFromNode("UrlSelector").setFromField("right_changed").setToNode("rightShader").setToField("url")
Transform22.addChild(ROUTE76)
ROUTE77 = ROUTEObject().setFromNode("UrlSelector").setFromField("top_changed").setToNode("topShader").setToField("url")
Transform22.addChild(ROUTE77)
ROUTE78 = ROUTEObject().setFromNode("UrlSelector").setFromField("bottom_changed").setToNode("bottomShader").setToField("url")
Transform22.addChild(ROUTE78)
Scene13.addChild(Transform22)
X3D0.setScene(Scene13)

X3D0.toFileX3D("mirror.new.x3d")