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
Viewpoint10 = ViewpointObject()
Viewpoint10.setPosition([0,0,20])
Viewpoint10.setDescription("Look at the bubbles flying")

Scene7.addChild(Viewpoint10)
ProtoDeclare11 = ProtoDeclareObject()
ProtoDeclare11.setName("Bubble")

ProtoBody12 = ProtoBodyObject()

Transform13 = TransformObject()
Transform13.setDEF("transform")

Shape14 = ShapeObject()
Shape14.setDEF("myShape")

Appearance15 = AppearanceObject()

Material16 = MaterialObject()
Material16.setDiffuseColor([0.7,0.7,0.7])
Material16.setSpecularColor([0.5,0.5,0.5])

Appearance15.setMaterial(Material16)
ComposedCubeMapTexture17 = ComposedCubeMapTextureObject()
ComposedCubeMapTexture17.setDEF("texture")

ImageTexture18 = ImageTextureObject()
ImageTexture18.setUrl(["cubemap/all_probes/stpeters_cross/stpeters_back.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_back.png"])

ComposedCubeMapTexture17.setBack(ImageTexture18)
ImageTexture19 = ImageTextureObject()
ImageTexture19.setUrl(["cubemap/all_probes/stpeters_cross/stpeters_bottom.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_bottom.png"])

ComposedCubeMapTexture17.setBottom(ImageTexture19)
ImageTexture20 = ImageTextureObject()
ImageTexture20.setUrl(["cubemap/all_probes/stpeters_cross/stpeters_front.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_front.png"])

ComposedCubeMapTexture17.setFront(ImageTexture20)
ImageTexture21 = ImageTextureObject()
ImageTexture21.setUrl(["cubemap/all_probes/stpeters_cross/stpeters_left.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_left.png"])

ComposedCubeMapTexture17.setLeft(ImageTexture21)
ImageTexture22 = ImageTextureObject()
ImageTexture22.setUrl(["cubemap/all_probes/stpeters_cross/stpeters_right.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_right.png"])

ComposedCubeMapTexture17.setRight(ImageTexture22)
ImageTexture23 = ImageTextureObject()
ImageTexture23.setUrl(["cubemap/all_probes/stpeters_cross/stpeters_top.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_top.png"])

ComposedCubeMapTexture17.setTop(ImageTexture23)
Appearance15.setTexture(ComposedCubeMapTexture17)

Appearance15.addComments(CommentsBlock("<ComposedShader DEF='gl' language=\"GLSL\"> <field name='cube' type='SFInt32' accessType=\"inputOutput\" value='0'/> <field name='chromaticDispertion' type='SFVec3f' accessType=\"inputOutput\" value='0.98 1.0 1.033'/> <field name='bias' type='SFFloat' accessType=\"inputOutput\" value='0.5'/> <field name='scale' type='SFFloat' accessType=\"inputOutput\" value='0.5'/> <field name='power' type='SFFloat' accessType=\"inputOutput\" value='2.0'/> <ShaderPart url='\"gl.vs\" \"http://coderextreme.net/X3DJSONLD/gl.vs\"' type='VERTEX'></ShaderPart> <ShaderPart url='\"pc_bubbles.fs\" \"http://coderextreme.net/X3DJSONLD/pc_bubbles.fs\"' type='FRAGMENT'></ShaderPart> </ComposedShader> <ComposedShader DEF='freewrl' language=\"GLSL\"> <field name='fw_textureCoodGenType' type='SFInt32' accessType=\"inputOutput\" value='0'/> <field name='chromaticDispertion' type='SFVec3f' accessType=\"inputOutput\" value='0.98 1.0 1.033'/> <field name='bias' type='SFFloat' accessType=\"inputOutput\" value='0.5'/> <field name='scale' type='SFFloat' accessType=\"inputOutput\" value='0.5'/> <field name='power' type='SFFloat' accessType=\"inputOutput\" value='2.0'/> <ShaderPart url='\"freewrl.vs\" \"http://coderextreme.net/X3DJSONLD/freewrl.vs\"' type='VERTEX'></ShaderPart> <ShaderPart url='\"pc_bubbles.fs\" \"http://coderextreme.net/X3DJSONLD/pc_bubbles.fs\"' type='FRAGMENT'></ShaderPart> </ComposedShader> <ComposedShader DEF='x3dom' language=\"GLSL\"> <field name='cube' type='SFInt32' accessType=\"inputOutput\" value='0'/> <field name='chromaticDispertion' type='SFVec3f' accessType=\"inputOutput\" value='0.98 1.0 1.033'/> <field name='bias' type='SFFloat' accessType=\"inputOutput\" value='0.5'/> <field name='scale' type='SFFloat' accessType=\"inputOutput\" value='0.5'/> <field name='power' type='SFFloat' accessType=\"inputOutput\" value='2.0'/> <ShaderPart url='\"x3dom.vs\" \"http://coderextreme.net/X3DJSONLD/x3dom.vs\"' type='VERTEX'></ShaderPart> <ShaderPart url='\"pc_bubbles.fs\" \"http://coderextreme.net/X3DJSONLD/pc_bubbles.fs\"' type='FRAGMENT'></ShaderPart> </ComposedShader> <ComposedShader DEF='instant' language=\"GLSL\"> <field name='cube' type='SFInt32' accessType=\"inputOutput\" value='0'/> <field name='chromaticDispertion' type='SFVec3f' accessType=\"inputOutput\" value='0.98 1.0 1.033'/> <field name='bias' type='SFFloat' accessType=\"inputOutput\" value='0.5'/> <field name='scale' type='SFFloat' accessType=\"inputOutput\" value='0.5'/> <field name='power' type='SFFloat' accessType=\"inputOutput\" value='2.0'/> <ShaderPart url='\"instant.vs\" \"http://coderextreme.net/X3DJSONLD/instant.vs\"' type='VERTEX'></ShaderPart> <ShaderPart url='\"pc_bubbles.fs\" \"http://coderextreme.net/X3DJSONLD/pc_bubbles.fs\"' type='FRAGMENT'></ShaderPart> </ComposedShader>"))
ComposedShader24 = ComposedShaderObject()
ComposedShader24.setDEF("cobweb")
ComposedShader24.setLanguage("GLSL")

field25 = fieldObject()
field25.setType(fieldObject.TYPE_SFNODE)
field25.setName("cube")
field25.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)

ComposedCubeMapTexture26 = ComposedCubeMapTextureObject()
ComposedCubeMapTexture26.setUSE("texture")

field25.addChild(ComposedCubeMapTexture26)
ComposedShader24.addField(field25)
field27 = fieldObject()
field27.setType(fieldObject.TYPE_SFVEC3F)
field27.setName("chromaticDispertion")
field27.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field27.setValue("0.98 1 1.033")

ComposedShader24.addField(field27)
field28 = fieldObject()
field28.setType(fieldObject.TYPE_SFFLOAT)
field28.setName("bias")
field28.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field28.setValue("0.5")

ComposedShader24.addField(field28)
field29 = fieldObject()
field29.setType(fieldObject.TYPE_SFFLOAT)
field29.setName("scale")
field29.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field29.setValue("0.5")

ComposedShader24.addField(field29)
field30 = fieldObject()
field30.setType(fieldObject.TYPE_SFFLOAT)
field30.setName("power")
field30.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field30.setValue("2")

ComposedShader24.addField(field30)
ShaderPart31 = ShaderPartObject()
ShaderPart31.setType("VERTEX")
ShaderPart31.setUrl(["cobweb.vs","http://coderextreme.net/X3DJSONLD/cobweb.vs"])

ComposedShader24.addParts(ShaderPart31)
ShaderPart32 = ShaderPartObject()
ShaderPart32.setType("FRAGMENT")
ShaderPart32.setUrl(["pc_bubbles.fs","http://coderextreme.net/X3DJSONLD/pc.fs"])

ComposedShader24.addParts(ShaderPart32)
Appearance15.addShaders(ComposedShader24)
Shape14.setAppearance(Appearance15)
Sphere33 = SphereObject()

Shape14.setGeometry(Sphere33)
Transform13.addChild(Shape14)
ProtoBody12.addChild(Transform13)
Script34 = ScriptObject()
Script34.setDEF("Bounce")

field35 = fieldObject()
field35.setType(fieldObject.TYPE_SFVEC3F)
field35.setName("translation")
field35.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field35.setValue("0 0 0")

Script34.addField(field35)
field36 = fieldObject()
field36.setType(fieldObject.TYPE_SFVEC3F)
field36.setName("velocity")
field36.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field36.setValue("0 0 0")

Script34.addField(field36)
field37 = fieldObject()
field37.setType(fieldObject.TYPE_SFTIME)
field37.setName("set_fraction")
field37.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)

Script34.addField(field37)

Script34.setSourceCode("ecmascript:\n"+
"			function set_translation(value) {\n"+
"				translation = value;\n"+
"			}\n"+
"			function translation_changed() {\n"+
"				return translation;\n"+
"			}\n"+
"			function initialize() {\n"+
"			    translation = new SFVec3f(0, 0, 0);\n"+
"			    velocity = new SFVec3f(\n"+
"			    	Math.random() - 0.5,\n"+
"				Math.random() - 0.5,\n"+
"				Math.random() - 0.5);\n"+
"			}\n"+
"			function set_fraction() {\n"+
"			    translation = new SFVec3f(\n"+
"			    	translation[0] + velocity[0],\n"+
"				translation[1] + velocity[1],\n"+
"				translation[2] + velocity[2]);\n"+
"			    for (var j = 0; j <= 2; j++) {\n"+
"				    if (Math.abs(translation[j]) > 10) {\n"+
"					initialize();\n"+
"				    } else {\n"+
"					velocity[0] += Math.random() * 0.2 - 0.1;\n"+
"					velocity[1] += Math.random() * 0.2 - 0.1;\n"+
"					velocity[2] += Math.random() * 0.2 - 0.1;\n"+
"				    }\n"+
"			    }\n"+
"			}\n"+
"")
ProtoBody12.addChild(Script34)
TimeSensor38 = TimeSensorObject()
TimeSensor38.setDEF("TourTime")
TimeSensor38.setCycleInterval(0.15)
TimeSensor38.setLoop(True)

ProtoBody12.addChild(TimeSensor38)
ROUTE39 = ROUTEObject()
ROUTE39.setFromNode("TourTime")
ROUTE39.setFromField("cycleTime")
ROUTE39.setToNode("Bounce")
ROUTE39.setToField("set_fraction")

ProtoBody12.addChild(ROUTE39)
ROUTE40 = ROUTEObject()
ROUTE40.setFromNode("Bounce")
ROUTE40.setFromField("translation_changed")
ROUTE40.setToNode("transform")
ROUTE40.setToField("set_translation")

ProtoBody12.addChild(ROUTE40)
ProtoDeclare11.setProtoBody(ProtoBody12)
Scene7.addChild(ProtoDeclare11)
ProtoInstance41 = ProtoInstanceObject()
ProtoInstance41.setName("Bubble")

Scene7.addChild(ProtoInstance41)
ProtoInstance42 = ProtoInstanceObject()
ProtoInstance42.setName("Bubble")

Scene7.addChild(ProtoInstance42)
ProtoInstance43 = ProtoInstanceObject()
ProtoInstance43.setName("Bubble")

Scene7.addChild(ProtoInstance43)
X3D0.setScene(Scene7)

X3D0.toFileX3D("./bub.new.x3d")
