# -*- coding: UTF-8 -*-
from jnius import autoclass
from X3Dautoclass import *
X3D0 =  X3DObject()
X3D0.setProfile("Immersive")
X3D0.setVersion("3.3")

head1 = headObject()

meta2 = metaObject()
meta2.setName("title")
meta2.setContent("flowers7.x3d")

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
meta5.setContent("http://coderextreme.net/X3DJSONLD/flowers7.x3d")

head1.addMeta(meta5)
meta6 = metaObject()
meta6.setName("description")
meta6.setContent("a flower")

head1.addMeta(meta6)
X3D0.setHead(head1)
Scene7 = SceneObject()

NavigationInfo8 = NavigationInfoObject()

Scene7.addChild(NavigationInfo8)

Scene7.addComments(CommentsBlock("Images courtesy of Paul Debevec's Light Probe Image Gallery"))
Background9 = BackgroundObject()
Background9.setDEF("background")
Background9.setBackUrl(["cubemap/all_probes/beach_cross/beach_back.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/beach_cross/beach_back.png"])
Background9.setBottomUrl(["cubemap/all_probes/beach_cross/beach_bottom.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/beach_cross/beach_bottom.png"])
Background9.setFrontUrl(["cubemap/all_probes/beach_cross/beach_front.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/beach_cross/beach_front.png"])
Background9.setLeftUrl(["cubemap/all_probes/beach_cross/beach_left.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/beach_cross/beach_left.png"])
Background9.setRightUrl(["cubemap/all_probes/beach_cross/beach_right.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/beach_cross/beach_right.png"])
Background9.setTopUrl(["cubemap/all_probes/beach_cross/beach_top.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/beach_cross/beach_top.png"])

Scene7.addChild(Background9)
Viewpoint10 = ViewpointObject()
Viewpoint10.setPosition([0,0,40])
Viewpoint10.setDescription("Transparent rose")

Scene7.addChild(Viewpoint10)
Transform11 = TransformObject()
Transform11.setDEF("Rose01")

Shape12 = ShapeObject()

Appearance13 = AppearanceObject()

Material14 = MaterialObject()
Material14.setDiffuseColor([0.7,0.7,0.7])
Material14.setSpecularColor([0.5,0.5,0.5])

Appearance13.setMaterial(Material14)
ComposedCubeMapTexture15 = ComposedCubeMapTextureObject()

ImageTexture16 = ImageTextureObject()
ImageTexture16.setDEF("backShader")
ImageTexture16.setUrl(["cubemap/all_probes/beach_cross/beach_back.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/beach_cross/beach_back.png"])

ComposedCubeMapTexture15.setBack(ImageTexture16)
ImageTexture17 = ImageTextureObject()
ImageTexture17.setDEF("bottomShader")
ImageTexture17.setUrl(["cubemap/all_probes/beach_cross/beach_bottom.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/beach_cross/beach_bottom.png"])

ComposedCubeMapTexture15.setBottom(ImageTexture17)
ImageTexture18 = ImageTextureObject()
ImageTexture18.setDEF("frontShader")
ImageTexture18.setUrl(["cubemap/all_probes/beach_cross/beach_front.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/beach_cross/beach_front.png"])

ComposedCubeMapTexture15.setFront(ImageTexture18)
ImageTexture19 = ImageTextureObject()
ImageTexture19.setDEF("leftShader")
ImageTexture19.setUrl(["cubemap/all_probes/beach_cross/beach_left.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/beach_cross/beach_left.png"])

ComposedCubeMapTexture15.setLeft(ImageTexture19)
ImageTexture20 = ImageTextureObject()
ImageTexture20.setDEF("rightShader")
ImageTexture20.setUrl(["cubemap/all_probes/beach_cross/beach_right.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/beach_cross/beach_right.png"])

ComposedCubeMapTexture15.setRight(ImageTexture20)
ImageTexture21 = ImageTextureObject()
ImageTexture21.setDEF("topShader")
ImageTexture21.setUrl(["cubemap/all_probes/beach_cross/beach_top.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/beach_cross/beach_top.png"])

ComposedCubeMapTexture15.setTop(ImageTexture21)
Appearance13.setTexture(ComposedCubeMapTexture15)
ComposedShader22 = ComposedShaderObject()
ComposedShader22.setDEF("cobweb")
ComposedShader22.setLanguage("GLSL")

field23 = fieldObject()
field23.setType(fieldObject.TYPE_SFINT32)
field23.setName("set_cube")
field23.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)
field23.setValue("0")

ComposedShader22.addField(field23)
field24 = fieldObject()
field24.setType(fieldObject.TYPE_SFVEC3F)
field24.setName("set_chromaticDispertion")
field24.setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY)
field24.setValue("0.98 1 1.033")

ComposedShader22.addField(field24)
field25 = fieldObject()
field25.setType(fieldObject.TYPE_SFFLOAT)
field25.setName("set_bias")
field25.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)
field25.setValue("0.5")

ComposedShader22.addField(field25)
field26 = fieldObject()
field26.setType(fieldObject.TYPE_SFFLOAT)
field26.setName("set_scale")
field26.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)
field26.setValue("0.5")

ComposedShader22.addField(field26)
field27 = fieldObject()
field27.setType(fieldObject.TYPE_SFFLOAT)
field27.setName("set_power")
field27.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)
field27.setValue("2")

ComposedShader22.addField(field27)
field28 = fieldObject()
field28.setType(fieldObject.TYPE_SFFLOAT)
field28.setName("set_a")
field28.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)
field28.setValue("10")

ComposedShader22.addField(field28)
field29 = fieldObject()
field29.setType(fieldObject.TYPE_SFFLOAT)
field29.setName("set_b")
field29.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)
field29.setValue("1")

ComposedShader22.addField(field29)
field30 = fieldObject()
field30.setType(fieldObject.TYPE_SFFLOAT)
field30.setName("set_c")
field30.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)
field30.setValue("20")

ComposedShader22.addField(field30)
field31 = fieldObject()
field31.setType(fieldObject.TYPE_SFFLOAT)
field31.setName("set_d")
field31.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)
field31.setValue("20")

ComposedShader22.addField(field31)
field32 = fieldObject()
field32.setType(fieldObject.TYPE_SFFLOAT)
field32.setName("set_tdelta")
field32.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)
field32.setValue("0")

ComposedShader22.addField(field32)
field33 = fieldObject()
field33.setType(fieldObject.TYPE_SFFLOAT)
field33.setName("set_pdelta")
field33.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)
field33.setValue("0")

ComposedShader22.addField(field33)
ShaderPart34 = ShaderPartObject()
ShaderPart34.setType("VERTEX")
ShaderPart34.setUrl(["cobweb_flowers_input.vs","http://coderextreme.net/X3DJSONLD/cobweb_flowers_input.vs"])

ComposedShader22.addParts(ShaderPart34)
ShaderPart35 = ShaderPartObject()
ShaderPart35.setType("FRAGMENT")
ShaderPart35.setUrl(["pc_input_flowers.fs","http://coderextreme.net/X3DJSONLD/pc_input_flowers.fs"])

ComposedShader22.addParts(ShaderPart35)
Appearance13.addShaders(ComposedShader22)
Shape12.setAppearance(Appearance13)
Sphere36 = SphereObject()
Sphere36.setSolid(False)
Sphere36.setRadius(20)

Shape12.setGeometry(Sphere36)
Transform11.addChild(Shape12)
Scene7.addChild(Transform11)
Script37 = ScriptObject()
Script37.setDEF("UrlSelector")
Script37.setDirectOutput(True)

field38 = fieldObject()
field38.setType(fieldObject.TYPE_MFSTRING)
field38.setName("frontUrls")
field38.setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY)
field38.setValue("\"cubemap/all_probes/beach_cross/beach_front.png\" \"cubemap/all_probes/building_cross/building_front.png\" \"cubemap/all_probes/campus_cross/campus_front.png\" \"cubemap/all_probes/galileo_cross/galileo_front.png\" \"cubemap/all_probes/grace_cross/grace_front.png\" \"cubemap/all_probes/kitchen_cross/kitchen_front.png\" \"cubemap/all_probes/rnl_cross/rnl_front.png\" \"cubemap/all_probes/stpeters_cross/stpeters_front.png\" \"cubemap/all_probes/uffizi_cross/uffizi_front.png\"")

Script37.addField(field38)
field39 = fieldObject()
field39.setType(fieldObject.TYPE_MFSTRING)
field39.setName("backUrls")
field39.setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY)
field39.setValue("\"cubemap/all_probes/beach_cross/beach_back.png\" \"cubemap/all_probes/building_cross/building_back.png\" \"cubemap/all_probes/campus_cross/campus_back.png\" \"cubemap/all_probes/galileo_cross/galileo_back.png\" \"cubemap/all_probes/grace_cross/grace_back.png\" \"cubemap/all_probes/kitchen_cross/kitchen_back.png\" \"cubemap/all_probes/rnl_cross/rnl_back.png\" \"cubemap/all_probes/stpeters_cross/stpeters_back.png\" \"cubemap/all_probes/uffizi_cross/uffizi_back.png\"")

Script37.addField(field39)
field40 = fieldObject()
field40.setType(fieldObject.TYPE_MFSTRING)
field40.setName("leftUrls")
field40.setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY)
field40.setValue("\"cubemap/all_probes/beach_cross/beach_left.png\" \"cubemap/all_probes/building_cross/building_left.png\" \"cubemap/all_probes/campus_cross/campus_left.png\" \"cubemap/all_probes/galileo_cross/galileo_left.png\" \"cubemap/all_probes/grace_cross/grace_left.png\" \"cubemap/all_probes/kitchen_cross/kitchen_left.png\" \"cubemap/all_probes/rnl_cross/rnl_left.png\" \"cubemap/all_probes/stpeters_cross/stpeters_left.png\" \"cubemap/all_probes/uffizi_cross/uffizi_left.png\"")

Script37.addField(field40)
field41 = fieldObject()
field41.setType(fieldObject.TYPE_MFSTRING)
field41.setName("rightUrls")
field41.setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY)
field41.setValue("\"cubemap/all_probes/beach_cross/beach_right.png\" \"cubemap/all_probes/building_cross/building_right.png\" \"cubemap/all_probes/campus_cross/campus_right.png\" \"cubemap/all_probes/galileo_cross/galileo_right.png\" \"cubemap/all_probes/grace_cross/grace_right.png\" \"cubemap/all_probes/kitchen_cross/kitchen_right.png\" \"cubemap/all_probes/rnl_cross/rnl_right.png\" \"cubemap/all_probes/stpeters_cross/stpeters_right.png\" \"cubemap/all_probes/uffizi_cross/uffizi_right.png\"")

Script37.addField(field41)
field42 = fieldObject()
field42.setType(fieldObject.TYPE_MFSTRING)
field42.setName("topUrls")
field42.setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY)
field42.setValue("\"cubemap/all_probes/beach_cross/beach_top.png\" \"cubemap/all_probes/building_cross/building_top.png\" \"cubemap/all_probes/campus_cross/campus_top.png\" \"cubemap/all_probes/galileo_cross/galileo_top.png\" \"cubemap/all_probes/grace_cross/grace_top.png\" \"cubemap/all_probes/kitchen_cross/kitchen_top.png\" \"cubemap/all_probes/rnl_cross/rnl_top.png\" \"cubemap/all_probes/stpeters_cross/stpeters_top.png\" \"cubemap/all_probes/uffizi_cross/uffizi_top.png\"")

Script37.addField(field42)
field43 = fieldObject()
field43.setType(fieldObject.TYPE_MFSTRING)
field43.setName("bottomUrls")
field43.setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY)
field43.setValue("\"cubemap/all_probes/beach_cross/beach_bottom.png\" \"cubemap/all_probes/building_cross/building_bottom.png\" \"cubemap/all_probes/campus_cross/campus_bottom.png\" \"cubemap/all_probes/galileo_cross/galileo_bottom.png\" \"cubemap/all_probes/grace_cross/grace_bottom.png\" \"cubemap/all_probes/kitchen_cross/kitchen_bottom.png\" \"cubemap/all_probes/rnl_cross/rnl_bottom.png\" \"cubemap/all_probes/stpeters_cross/stpeters_bottom.png\" \"cubemap/all_probes/uffizi_cross/uffizi_bottom.png\"")

Script37.addField(field43)
field44 = fieldObject()
field44.setType(fieldObject.TYPE_MFSTRING)
field44.setName("front_changed")
field44.setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY)

Script37.addField(field44)
field45 = fieldObject()
field45.setType(fieldObject.TYPE_MFSTRING)
field45.setName("back_changed")
field45.setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY)

Script37.addField(field45)
field46 = fieldObject()
field46.setType(fieldObject.TYPE_MFSTRING)
field46.setName("left_changed")
field46.setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY)

Script37.addField(field46)
field47 = fieldObject()
field47.setType(fieldObject.TYPE_MFSTRING)
field47.setName("right_changed")
field47.setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY)

Script37.addField(field47)
field48 = fieldObject()
field48.setType(fieldObject.TYPE_MFSTRING)
field48.setName("top_changed")
field48.setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY)

Script37.addField(field48)
field49 = fieldObject()
field49.setType(fieldObject.TYPE_MFSTRING)
field49.setName("bottom_changed")
field49.setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY)

Script37.addField(field49)
field50 = fieldObject()
field50.setType(fieldObject.TYPE_SFFLOAT)
field50.setName("set_fraction")
field50.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)

Script37.addField(field50)
field51 = fieldObject()
field51.setType(fieldObject.TYPE_SFINT32)
field51.setName("old")
field51.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field51.setValue("-1")

Script37.addField(field51)

Script37.setSourceCode("ecmascript:\n"+
"        function set_fraction( f, tm ) {\n"+
"            var side = Math.floor(f*frontUrls.length);\n"+
"            if (side > frontUrls.length-1) {\n"+
"                side = 0;\n"+
"            }\n"+
"            if (side != old) {\n"+
"                    old = side;\n"+
"                    front_changed[0] = frontUrls[side];\n"+
"                    back_changed[0] = backUrls[side];\n"+
"                    left_changed[0] = leftUrls[side];\n"+
"                    right_changed[0] = rightUrls[side];\n"+
"                    top_changed[0] = topUrls[side];\n"+
"                    bottom_changed[0] = bottomUrls[side];\n"+
"            }\n"+
"        }\n"+
"")
Scene7.addChild(Script37)
TimeSensor52 = TimeSensorObject()
TimeSensor52.setDEF("Clock")
TimeSensor52.setCycleInterval(45)
TimeSensor52.setLoop(True)

Scene7.addChild(TimeSensor52)
ROUTE53 = ROUTEObject()
ROUTE53.setFromNode("Clock")
ROUTE53.setFromField("fraction_changed")
ROUTE53.setToNode("UrlSelector")
ROUTE53.setToField("set_fraction")

Scene7.addChild(ROUTE53)
ROUTE54 = ROUTEObject()
ROUTE54.setFromNode("UrlSelector")
ROUTE54.setFromField("front_changed")
ROUTE54.setToNode("background")
ROUTE54.setToField("frontUrl")

Scene7.addChild(ROUTE54)
ROUTE55 = ROUTEObject()
ROUTE55.setFromNode("UrlSelector")
ROUTE55.setFromField("back_changed")
ROUTE55.setToNode("background")
ROUTE55.setToField("backUrl")

Scene7.addChild(ROUTE55)
ROUTE56 = ROUTEObject()
ROUTE56.setFromNode("UrlSelector")
ROUTE56.setFromField("left_changed")
ROUTE56.setToNode("background")
ROUTE56.setToField("leftUrl")

Scene7.addChild(ROUTE56)
ROUTE57 = ROUTEObject()
ROUTE57.setFromNode("UrlSelector")
ROUTE57.setFromField("right_changed")
ROUTE57.setToNode("background")
ROUTE57.setToField("rightUrl")

Scene7.addChild(ROUTE57)
ROUTE58 = ROUTEObject()
ROUTE58.setFromNode("UrlSelector")
ROUTE58.setFromField("top_changed")
ROUTE58.setToNode("background")
ROUTE58.setToField("topUrl")

Scene7.addChild(ROUTE58)
ROUTE59 = ROUTEObject()
ROUTE59.setFromNode("UrlSelector")
ROUTE59.setFromField("bottom_changed")
ROUTE59.setToNode("background")
ROUTE59.setToField("bottomUrl")

Scene7.addChild(ROUTE59)
ROUTE60 = ROUTEObject()
ROUTE60.setFromNode("UrlSelector")
ROUTE60.setFromField("front_changed")
ROUTE60.setToNode("frontShader")
ROUTE60.setToField("url")

Scene7.addChild(ROUTE60)
ROUTE61 = ROUTEObject()
ROUTE61.setFromNode("UrlSelector")
ROUTE61.setFromField("back_changed")
ROUTE61.setToNode("backShader")
ROUTE61.setToField("url")

Scene7.addChild(ROUTE61)
ROUTE62 = ROUTEObject()
ROUTE62.setFromNode("UrlSelector")
ROUTE62.setFromField("left_changed")
ROUTE62.setToNode("leftShader")
ROUTE62.setToField("url")

Scene7.addChild(ROUTE62)
ROUTE63 = ROUTEObject()
ROUTE63.setFromNode("UrlSelector")
ROUTE63.setFromField("right_changed")
ROUTE63.setToNode("rightShader")
ROUTE63.setToField("url")

Scene7.addChild(ROUTE63)
ROUTE64 = ROUTEObject()
ROUTE64.setFromNode("UrlSelector")
ROUTE64.setFromField("top_changed")
ROUTE64.setToNode("topShader")
ROUTE64.setToField("url")

Scene7.addChild(ROUTE64)
ROUTE65 = ROUTEObject()
ROUTE65.setFromNode("UrlSelector")
ROUTE65.setFromField("bottom_changed")
ROUTE65.setToNode("bottomShader")
ROUTE65.setToField("url")

Scene7.addChild(ROUTE65)
Script66 = ScriptObject()
Script66.setDEF("Animate")
Script66.setDirectOutput(True)

field67 = fieldObject()
field67.setType(fieldObject.TYPE_SFFLOAT)
field67.setName("set_fraction")
field67.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)

Script66.addField(field67)
field68 = fieldObject()
field68.setType(fieldObject.TYPE_SFFLOAT)
field68.setName("a_changed")
field68.setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY)
field68.setValue("10")

Script66.addField(field68)
field69 = fieldObject()
field69.setType(fieldObject.TYPE_SFFLOAT)
field69.setName("b_changed")
field69.setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY)
field69.setValue("1")

Script66.addField(field69)
field70 = fieldObject()
field70.setType(fieldObject.TYPE_SFFLOAT)
field70.setName("c_changed")
field70.setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY)
field70.setValue("20")

Script66.addField(field70)
field71 = fieldObject()
field71.setType(fieldObject.TYPE_SFFLOAT)
field71.setName("d_changed")
field71.setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY)
field71.setValue("20")

Script66.addField(field71)
field72 = fieldObject()
field72.setType(fieldObject.TYPE_SFFLOAT)
field72.setName("tdelta_changed")
field72.setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY)
field72.setValue("0")

Script66.addField(field72)
field73 = fieldObject()
field73.setType(fieldObject.TYPE_SFFLOAT)
field73.setName("pdelta_changed")
field73.setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY)
field73.setValue("0")

Script66.addField(field73)
field74 = fieldObject()
field74.setType(fieldObject.TYPE_SFFLOAT)
field74.setName("set_a")
field74.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)
field74.setValue("10")

Script66.addField(field74)
field75 = fieldObject()
field75.setType(fieldObject.TYPE_SFFLOAT)
field75.setName("set_b")
field75.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)
field75.setValue("1")

Script66.addField(field75)
field76 = fieldObject()
field76.setType(fieldObject.TYPE_SFFLOAT)
field76.setName("set_c")
field76.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)
field76.setValue("20")

Script66.addField(field76)
field77 = fieldObject()
field77.setType(fieldObject.TYPE_SFFLOAT)
field77.setName("set_d")
field77.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)
field77.setValue("20")

Script66.addField(field77)
field78 = fieldObject()
field78.setType(fieldObject.TYPE_SFFLOAT)
field78.setName("set_tdelta")
field78.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)
field78.setValue("0")

Script66.addField(field78)
field79 = fieldObject()
field79.setType(fieldObject.TYPE_SFFLOAT)
field79.setName("set_pdelta")
field79.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)
field79.setValue("0")

Script66.addField(field79)

Script66.setSourceCode("ecmascript:\n"+
"\n"+
"function set_a(value) {\n"+
"	a = value;\n"+
"}\n"+
"\n"+
"function set_b(value) {\n"+
"	b = value;\n"+
"}\n"+
"\n"+
"function set_c(value) {\n"+
"	c = value;\n"+
"}\n"+
"\n"+
"function set_d(value) {\n"+
"	d = value;\n"+
"}\n"+
"\n"+
"function set_tdelta(value) {\n"+
"	tdelta = value;\n"+
"}\n"+
"\n"+
"function set_tdelta(value) {\n"+
"	tdelta = value;\n"+
"}\n"+
"\n"+
"function set_fraction() {\n"+
"	var choice = Math.floor(Math.random() * 4);\n"+
"	if (choice == 0) {\n"+
"		set_a(a + Math.floor(Math.random() * 2) * 2 - 1);\n"+
"	} else if (choice == 1) {\n"+
"		set_b(b + Math.floor(Math.random() * 2) * 2 - 1);\n"+
"	} else if (choice == 2) {\n"+
"		set_c(c + Math.floor(Math.random() * 2) * 2 - 1);\n"+
"	} else if (choice == 3) {\n"+
"		set_d(d + Math.floor(Math.random() * 2) * 2 - 1);\n"+
"	}\n"+
"	set_tdelta(tdelta + 0.5);\n"+
"	set_pdelta(pdelta + 0.5);\n"+
"	if (a < 1) {\n"+
"		set_a(10);\n"+
"	}\n"+
"	if (b < 1) {\n"+
"		set_b(10);\n"+
"	}\n"+
"	if (c < 1) {\n"+
"		set_c(4);\n"+
"	}\n"+
"	if (c > 20) {\n"+
"		set_c(4);\n"+
"	}\n"+
"	if (d < 1) {\n"+
"		set_d(4);\n"+
"	}\n"+
"	if (d > 20) {\n"+
"		set_d(4);\n"+
"	}\n"+
"	// console.log(a, b, c, d, tdelta, pdelta);\n"+
"}\n"+
"")
Scene7.addChild(Script66)
ROUTE80 = ROUTEObject()
ROUTE80.setFromNode("Animate")
ROUTE80.setFromField("a_changed")
ROUTE80.setToNode("cobweb")
ROUTE80.setToField("set_a")

Scene7.addChild(ROUTE80)
ROUTE81 = ROUTEObject()
ROUTE81.setFromNode("Animate")
ROUTE81.setFromField("b_changed")
ROUTE81.setToNode("cobweb")
ROUTE81.setToField("set_b")

Scene7.addChild(ROUTE81)
ROUTE82 = ROUTEObject()
ROUTE82.setFromNode("Animate")
ROUTE82.setFromField("c_changed")
ROUTE82.setToNode("cobweb")
ROUTE82.setToField("set_c")

Scene7.addChild(ROUTE82)
ROUTE83 = ROUTEObject()
ROUTE83.setFromNode("Animate")
ROUTE83.setFromField("d_changed")
ROUTE83.setToNode("cobweb")
ROUTE83.setToField("set_d")

Scene7.addChild(ROUTE83)
ROUTE84 = ROUTEObject()
ROUTE84.setFromNode("Animate")
ROUTE84.setFromField("pdelta_changed")
ROUTE84.setToNode("cobweb")
ROUTE84.setToField("set_pdelta")

Scene7.addChild(ROUTE84)
ROUTE85 = ROUTEObject()
ROUTE85.setFromNode("Animate")
ROUTE85.setFromField("tdelta_changed")
ROUTE85.setToNode("cobweb")
ROUTE85.setToField("set_tdelta")

Scene7.addChild(ROUTE85)
X3D0.setScene(Scene7)

X3D0.toFileX3D("./flowers7.new.x3d")
