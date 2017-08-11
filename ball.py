from jnius import autoclass
from X3Dautoclass import *
X3D0 =  X3DObject()
X3D0.setProfile("Immersive")
X3D0.setVersion("3.3")

head1 = headObject()

component2 = componentObject()
component2.setName("EnvironmentalEffects")
component2.setLevel(1)

head1.addComponent(component2)
component3 = componentObject()
component3.setName("EnvironmentalEffects")
component3.setLevel(3)

head1.addComponent(component3)
meta4 = metaObject()
meta4.setName("title")
meta4.setContent("ball.x3d")

head1.addMeta(meta4)
meta5 = metaObject()
meta5.setName("creator")
meta5.setContent("John Carlson")

head1.addMeta(meta5)
meta6 = metaObject()
meta6.setName("generator")
meta6.setContent("manual")

head1.addMeta(meta6)
meta7 = metaObject()
meta7.setName("identifier")
meta7.setContent("http://coderextreme.net/X3DJSONLD/ball.x3d")

head1.addMeta(meta7)
meta8 = metaObject()
meta8.setName("description")
meta8.setContent("a prismatic sphere")

head1.addMeta(meta8)
X3D0.setHead(head1)
Scene9 = SceneObject()

NavigationInfo10 = NavigationInfoObject()
NavigationInfo10.setType(["ANY","EXAMINE","FLY","LOOKAT"])

Scene9.addChild(NavigationInfo10)
Viewpoint11 = ViewpointObject()
Viewpoint11.setDescription("Tour Views")

Scene9.addChild(Viewpoint11)
Background12 = BackgroundObject()
Background12.setBackUrl(["cubemap/all_probes/stpeters_cross/stpeters_back.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_back.png"])
Background12.setBottomUrl(["cubemap/all_probes/stpeters_cross/stpeters_bottom.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_bottom.png"])
Background12.setFrontUrl(["cubemap/all_probes/stpeters_cross/stpeters_front.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_front.png"])
Background12.setLeftUrl(["cubemap/all_probes/stpeters_cross/stpeters_left.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_left.png"])
Background12.setRightUrl(["cubemap/all_probes/stpeters_cross/stpeters_right.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_right.png"])
Background12.setTopUrl(["cubemap/all_probes/stpeters_cross/stpeters_top.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_top.png"])

Scene9.addChild(Background12)
Transform13 = TransformObject()

Shape14 = ShapeObject()

Sphere15 = SphereObject()

Shape14.setGeometry(Sphere15)
Appearance16 = AppearanceObject()

Material17 = MaterialObject()

Appearance16.setMaterial(Material17)
ComposedCubeMapTexture18 = ComposedCubeMapTextureObject()
ComposedCubeMapTexture18.setDEF("texture")

ImageTexture19 = ImageTextureObject()
ImageTexture19.setUrl(["cubemap/all_probes/stpeters_cross/stpeters_back.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_back.png"])

ComposedCubeMapTexture18.setBack(ImageTexture19)
ImageTexture20 = ImageTextureObject()
ImageTexture20.setUrl(["cubemap/all_probes/stpeters_cross/stpeters_bottom.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_bottom.png"])

ComposedCubeMapTexture18.setBottom(ImageTexture20)
ImageTexture21 = ImageTextureObject()
ImageTexture21.setUrl(["cubemap/all_probes/stpeters_cross/stpeters_front.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_front.png"])

ComposedCubeMapTexture18.setFront(ImageTexture21)
ImageTexture22 = ImageTextureObject()
ImageTexture22.setUrl(["cubemap/all_probes/stpeters_cross/stpeters_left.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_left.png"])

ComposedCubeMapTexture18.setLeft(ImageTexture22)
ImageTexture23 = ImageTextureObject()
ImageTexture23.setUrl(["cubemap/all_probes/stpeters_cross/stpeters_right.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_right.png"])

ComposedCubeMapTexture18.setRight(ImageTexture23)
ImageTexture24 = ImageTextureObject()
ImageTexture24.setUrl(["cubemap/all_probes/stpeters_cross/stpeters_top.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/stpeters_cross/stpeters_top.png"])

ComposedCubeMapTexture18.setTop(ImageTexture24)
Appearance16.setTexture(ComposedCubeMapTexture18)

Appearance16.addComments(CommentsBlock("<ProgramShader DEF='ProgramShader' containerField='shaders' language='GLSL'> <ShaderProgram url='\"freewrl.vs\" \"http://coderextreme.net/X3DJSONLD/freewrl.vs\"' containerField='programs' type='VERTEX'> <field name='chromaticDispertion' accessType='initializeOnly' type='SFVec3f' value='0.98 1 1.033'/> <field name='bias' accessType='initializeOnly' type='SFFloat' value='0.5'/> <field name='scale' accessType='initializeOnly' type='SFFloat' value='0.5'/> <field name='power' accessType='initializeOnly' type='SFFloat' value='2'/> </ShaderProgram> <ShaderProgram url='\"freewrl.fs\" \"http://coderextreme.net/X3DJSONLD/freewrl.fs\"' containerField='programs' type='FRAGMENT'/> </ProgramShader>"))

Appearance16.addComments(CommentsBlock("<ComposedShader language='GLSL'> <field name='chromaticDispertion' accessType='initializeOnly' type='SFVec3f' value='0.98 1 1.033'></field> <field name='fw_Texture_unit0' type='SFNode' accessType=\"initializeOnly\"> <ComposedCubeMapTexture USE=\"texture\"></ComposedCubeMapTexture> </field> <field name='bias' accessType='initializeOnly' type='SFFloat' value='0.5'></field> <field name='scale' accessType='initializeOnly' type='SFFloat' value='0.5'></field> <field name='power' accessType='initializeOnly' type='SFFloat' value='2'></field> <ShaderPart url='\"contact.vs\" \"http://coderextreme.net/X3DJSONLD/contact.vs\"' type=\"VERTEX\" containerField='parts'></ShaderPart> <ShaderPart url='\"common.fs\" \"http://coderextreme.net/X3DJSONLD/common.fs\"' containerField='parts' type='FRAGMENT'></ShaderPart> </ComposedShader>"))

Appearance16.addComments(CommentsBlock("<ComposedShader language='GLSL'> <field name='chromaticDispertion' accessType='inputOutput' type='SFVec3f' value='0.98 1 1.033'></field> <field name='cube' type='SFNode' accessType=\"inputOutput\"> <ComposedCubeMapTexture USE=\"texture\"></ComposedCubeMapTexture> </field> <field name='bias' accessType='inputOutput' type='SFFloat' value='0.5'></field> <field name='scale' accessType='inputOutput' type='SFFloat' value='0.5'></field> <field name='power' accessType='inputOutput' type='SFFloat' value='2'></field> <ShaderPart url='\"octaga.vs\" \"http://coderextreme.net/X3DJSONLD/octaga.vs\"' type=\"VERTEX\" containerField='parts'></ShaderPart> <ShaderPart url='\"common.fs\" \"http://coderextreme.net/X3DJSONLD/common.fs\"' containerField='parts' type='FRAGMENT'></ShaderPart> </ComposedShader>"))

Appearance16.addComments(CommentsBlock("<ComposedShader language='GLSL'> <field name='chromaticDispertion' accessType='initializeOnly' type='SFVec3f' value='0.98 1 1.033'></field> <field name='cube' accessType='initializeOnly' type='SFInt32' value='0'></field> <field name='bias' accessType='initializeOnly' type='SFFloat' value='0.5'></field> <field name='scale' accessType='initializeOnly' type='SFFloat' value='0.5'></field> <field name='power' accessType='initializeOnly' type='SFFloat' value='2'></field> <ShaderPart url='\"instant.vs\" \"http://coderextreme.net/X3DJSONLD/instant.vs\"' type=\"VERTEX\" containerField='parts'></ShaderPart> <ShaderPart url='\"common.fs\" \"http://coderextreme.net/X3DJSONLD/common.fs\"' containerField='parts' type='FRAGMENT'></ShaderPart> </ComposedShader>"))

Appearance16.addComments(CommentsBlock(""))
ComposedShader25 = ComposedShaderObject()
ComposedShader25.setLanguage("GLSL")

field26 = fieldObject()
field26.setType(fieldObject.TYPE_SFVEC3F)
field26.setName("chromaticDispertion")
field26.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field26.setValue("0.98 1 1.033")

ComposedShader25.addField(field26)
field27 = fieldObject()
field27.setType(fieldObject.TYPE_SFNODE)
field27.setName("cube")
field27.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)

ComposedCubeMapTexture28 = ComposedCubeMapTextureObject()
ComposedCubeMapTexture28.setUSE("texture")

field27.addChild(ComposedCubeMapTexture28)
ComposedShader25.addField(field27)
field29 = fieldObject()
field29.setType(fieldObject.TYPE_SFFLOAT)
field29.setName("bias")
field29.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field29.setValue("0.5")

ComposedShader25.addField(field29)
field30 = fieldObject()
field30.setType(fieldObject.TYPE_SFFLOAT)
field30.setName("scale")
field30.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field30.setValue("0.5")

ComposedShader25.addField(field30)
field31 = fieldObject()
field31.setType(fieldObject.TYPE_SFFLOAT)
field31.setName("power")
field31.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field31.setValue("2")

ComposedShader25.addField(field31)
ShaderPart32 = ShaderPartObject()
ShaderPart32.setType("VERTEX")
ShaderPart32.setUrl(["x3dom.vs","http://coderextreme.net/X3DJSONLD/x3dom.vs"])

ComposedShader25.addParts(ShaderPart32)
ShaderPart33 = ShaderPartObject()
ShaderPart33.setType("FRAGMENT")
ShaderPart33.setDEF("common")
ShaderPart33.setUrl(["common.fs","http://coderextreme.net/X3DJSONLD/common.fs"])

ComposedShader25.addParts(ShaderPart33)
Appearance16.addShaders(ComposedShader25)
ComposedShader34 = ComposedShaderObject()
ComposedShader34.setLanguage("GLSL")

field35 = fieldObject()
field35.setType(fieldObject.TYPE_SFVEC3F)
field35.setName("chromaticDispertion")
field35.setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY)
field35.setValue("0.98 1 1.033")

ComposedShader34.addField(field35)
field36 = fieldObject()
field36.setType(fieldObject.TYPE_SFNODE)
field36.setName("cube")
field36.setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY)

ComposedCubeMapTexture37 = ComposedCubeMapTextureObject()
ComposedCubeMapTexture37.setUSE("texture")

field36.addChild(ComposedCubeMapTexture37)
ComposedShader34.addField(field36)
field38 = fieldObject()
field38.setType(fieldObject.TYPE_SFFLOAT)
field38.setName("bias")
field38.setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY)
field38.setValue("0.5")

ComposedShader34.addField(field38)
field39 = fieldObject()
field39.setType(fieldObject.TYPE_SFFLOAT)
field39.setName("scale")
field39.setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY)
field39.setValue("0.5")

ComposedShader34.addField(field39)
field40 = fieldObject()
field40.setType(fieldObject.TYPE_SFFLOAT)
field40.setName("power")
field40.setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY)
field40.setValue("2")

ComposedShader34.addField(field40)
ShaderPart41 = ShaderPartObject()
ShaderPart41.setType("VERTEX")
ShaderPart41.setUrl(["cobweb.vs","http://coderextreme.net/X3DJSONLD/cobweb.vs"])

ComposedShader34.addParts(ShaderPart41)
ShaderPart42 = ShaderPartObject()
ShaderPart42.setUSE("common")

ComposedShader34.addParts(ShaderPart42)
Appearance16.addShaders(ComposedShader34)
Shape14.setAppearance(Appearance16)
Transform13.addChild(Shape14)
Scene9.addChild(Transform13)
X3D0.setScene(Scene9)

X3D0.toFileX3D("./ball.new.x3d")
