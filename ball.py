import x3dpsail as x3d
X3D0 = x3d.X3D()
X3D0.setProfile("Immersive")
X3D0.setVersion("3.3")
head1 = x3d.head()
component2 = x3d.component()
component2.setName("EnvironmentalEffects")
component2.setLevel(1)

head1.addComponent(component2)
component3 = x3d.component()
component3.setName("EnvironmentalEffects")
component3.setLevel(3)

head1.addComponent(component3)
component4 = x3d.component()
component4.setName("Shaders")
component4.setLevel(1)

head1.addComponent(component4)
component5 = x3d.component()
component5.setName("CubeMapTexturing")
component5.setLevel(1)

head1.addComponent(component5)
meta6 = x3d.meta()
meta6.setName("title")
meta6.setContent("ball.x3d")

head1.addMeta(meta6)
meta7 = x3d.meta()
meta7.setName("creator")
meta7.setContent("John Carlson")

head1.addMeta(meta7)
meta8 = x3d.meta()
meta8.setName("generator")
meta8.setContent("manual")

head1.addMeta(meta8)
meta9 = x3d.meta()
meta9.setName("identifier")
meta9.setContent("https://coderextreme.net/X3DJSONLD/ball.x3d")

head1.addMeta(meta9)
meta10 = x3d.meta()
meta10.setName("description")
meta10.setContent("a prismatic sphere")

head1.addMeta(meta10)

X3D0.setHead(head1)
Scene11 = x3d.Scene()
NavigationInfo12 = x3d.NavigationInfo()
NavigationInfo12.setType(["ANY","EXAMINE","FLY","LOOKAT"])

Scene11.addChildren(NavigationInfo12)
Viewpoint13 = x3d.Viewpoint()
Viewpoint13.setDescription("Tour Views")

Scene11.addChildren(Viewpoint13)
Background14 = x3d.Background()
Background14.setBackUrl(["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"])
Background14.setBottomUrl(["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"])
Background14.setFrontUrl(["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"])
Background14.setLeftUrl(["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"])
Background14.setRightUrl(["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"])
Background14.setTopUrl(["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"])

Scene11.addChildren(Background14)
Transform15 = x3d.Transform()
Shape16 = x3d.Shape()
Sphere17 = x3d.Sphere()

Shape16.setGeometry(Sphere17)
Appearance18 = x3d.Appearance()
Material19 = x3d.Material()
Material19.setDiffuseColor([0.7,0.7,0.7])
Material19.setSpecularColor([0.5,0.5,0.5])

Appearance18.setMaterial(Material19)
ComposedCubeMapTexture20 = x3d.ComposedCubeMapTexture()
ComposedCubeMapTexture20.setDEF("texture")
ImageTexture21 = x3d.ImageTexture()
ImageTexture21.setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"])

ComposedCubeMapTexture20.setBack(ImageTexture21)
ImageTexture22 = x3d.ImageTexture()
ImageTexture22.setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"])

ComposedCubeMapTexture20.setBottom(ImageTexture22)
ImageTexture23 = x3d.ImageTexture()
ImageTexture23.setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"])

ComposedCubeMapTexture20.setFront(ImageTexture23)
ImageTexture24 = x3d.ImageTexture()
ImageTexture24.setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"])

ComposedCubeMapTexture20.setLeft(ImageTexture24)
ImageTexture25 = x3d.ImageTexture()
ImageTexture25.setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"])

ComposedCubeMapTexture20.setRight(ImageTexture25)
ImageTexture26 = x3d.ImageTexture()
ImageTexture26.setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"])

ComposedCubeMapTexture20.setTop(ImageTexture26)

Appearance18.setTexture(ComposedCubeMapTexture20)
#<ProgramShader DEF='ProgramShader' containerField='shaders' language='GLSL'> <ShaderProgram url='\"../shaders/freewrl.vs\" \"https://coderextreme.net/X3DJSONLD/src/main/shaders/freewrl.vs\"' containerField='programs' type='VERTEX'> <field name='chromaticDispertion' accessType='initializeOnly' type='SFVec3f' value='0.98 1 1.033'/> <field name='bias' accessType='initializeOnly' type='SFFloat' value='0.5'/> <field name='scale' accessType='initializeOnly' type='SFFloat' value='0.5'/> <field name='power' accessType='initializeOnly' type='SFFloat' value='2'/> </ShaderProgram> <ShaderProgram url='\"../shaders/freewrl.fs\" \"https://coderextreme.net/X3DJSONLD/src/main/shaders/freewrl.fs\"' containerField='programs' type='FRAGMENT'/> </ProgramShader>
#<ComposedShader language='GLSL'> <field name='chromaticDispertion' accessType='initializeOnly' type='SFVec3f' value='0.98 1 1.033'></field> <field name='fw_Texture_unit0' type='SFNode' accessType=\"initializeOnly\"> <ComposedCubeMapTexture USE=\"texture\"></ComposedCubeMapTexture> </field> <field name='bias' accessType='initializeOnly' type='SFFloat' value='0.5'></field> <field name='scale' accessType='initializeOnly' type='SFFloat' value='0.5'></field> <field name='power' accessType='initializeOnly' type='SFFloat' value='2'></field> <ShaderPart url='\"../shaders/contact.vs\" \"https://coderextreme.net/X3DJSONLD/src/main/shaders/contact.vs\"' type=\"VERTEX\" containerField='parts'></ShaderPart> <ShaderPart url='\"../shaders/common.fs\" \"https://coderextreme.net/X3DJSONLD/src/main/shaders/common.fs\"' containerField='parts' type='FRAGMENT'></ShaderPart> </ComposedShader>
#<ComposedShader language='GLSL'> <field name='chromaticDispertion' accessType='inputOutput' type='SFVec3f' value='0.98 1 1.033'></field> <field name='cube' type='SFNode' accessType=\"inputOutput\"> <ComposedCubeMapTexture USE=\"texture\"></ComposedCubeMapTexture> </field> <field name='bias' accessType='inputOutput' type='SFFloat' value='0.5'></field> <field name='scale' accessType='inputOutput' type='SFFloat' value='0.5'></field> <field name='power' accessType='inputOutput' type='SFFloat' value='2'></field> <ShaderPart url='\"../shaders/octaga.vs\" \"https://coderextreme.net/X3DJSONLD/src/main/shaders/octaga.vs\"' type=\"VERTEX\" containerField='parts'></ShaderPart> <ShaderPart url='\"../shaders/common.fs\" \"https://coderextreme.net/X3DJSONLD/src/main/shaders/common.fs\"' containerField='parts' type='FRAGMENT'></ShaderPart> </ComposedShader>
#<ComposedShader language='GLSL'> <field name='chromaticDispertion' accessType='initializeOnly' type='SFVec3f' value='0.98 1 1.033'></field> <field name='cube' accessType='initializeOnly' type='SFInt32' value='0'></field> <field name='bias' accessType='initializeOnly' type='SFFloat' value='0.5'></field> <field name='scale' accessType='initializeOnly' type='SFFloat' value='0.5'></field> <field name='power' accessType='initializeOnly' type='SFFloat' value='2'></field> <ShaderPart url='\"../shaders/instant.vs\" \"https://coderextreme.net/X3DJSONLD/src/main/shaders/instant.vs\"' type=\"VERTEX\" containerField='parts'></ShaderPart> <ShaderPart url='\"../shaders/common.fs\" \"https://coderextreme.net/X3DJSONLD/src/main/shaders/common.fs\"' containerField='parts' type='FRAGMENT'></ShaderPart> </ComposedShader>
#
ComposedShader27 = x3d.ComposedShader()
ComposedShader27.setLanguage("GLSL")
field28 = x3d.field()
field28.setName("chromaticDispertion")
field28.setAccessType("inputOutput")
field28.setType("SFVec3f")
field28.setValue("0.98 1 1.033")

ComposedShader27.addField(field28)
field29 = x3d.field()
field29.setName("cube")
field29.setType("SFNode")
field29.setAccessType("inputOutput")
ComposedCubeMapTexture30 = x3d.ComposedCubeMapTexture()
ComposedCubeMapTexture30.setUSE("texture")

field29.addChildren(ComposedCubeMapTexture30)

ComposedShader27.addField(field29)
field31 = x3d.field()
field31.setName("bias")
field31.setAccessType("inputOutput")
field31.setType("SFFloat")
field31.setValue("0.5")

ComposedShader27.addField(field31)
field32 = x3d.field()
field32.setName("scale")
field32.setAccessType("inputOutput")
field32.setType("SFFloat")
field32.setValue("0.5")

ComposedShader27.addField(field32)
field33 = x3d.field()
field33.setName("power")
field33.setAccessType("inputOutput")
field33.setType("SFFloat")
field33.setValue("2")

ComposedShader27.addField(field33)
ShaderPart34 = x3d.ShaderPart()
ShaderPart34.setUrl(["../shaders/x3dom.vs","https://coderextreme.net/X3DJSONLD/src/main/src/main/shaders/x3dom.vs"])
ShaderPart34.setType("VERTEX")

ComposedShader27.addParts(ShaderPart34)
ShaderPart35 = x3d.ShaderPart()
ShaderPart35.setDEF("common")
ShaderPart35.setUrl(["../shaders/common.fs","https://coderextreme.net/X3DJSONLD/src/main/shaders/common.fs"])
ShaderPart35.setType("FRAGMENT")

ComposedShader27.addParts(ShaderPart35)

Appearance18.addShaders(ComposedShader27)
ComposedShader36 = x3d.ComposedShader()
ComposedShader36.setLanguage("GLSL")
field37 = x3d.field()
field37.setName("chromaticDispertion")
field37.setAccessType("initializeOnly")
field37.setType("SFVec3f")
field37.setValue("0.98 1 1.033")

ComposedShader36.addField(field37)
field38 = x3d.field()
field38.setName("cube")
field38.setType("SFNode")
field38.setAccessType("initializeOnly")
ComposedCubeMapTexture39 = x3d.ComposedCubeMapTexture()
ComposedCubeMapTexture39.setUSE("texture")

field38.addChildren(ComposedCubeMapTexture39)

ComposedShader36.addField(field38)
field40 = x3d.field()
field40.setName("bias")
field40.setAccessType("initializeOnly")
field40.setType("SFFloat")
field40.setValue("0.5")

ComposedShader36.addField(field40)
field41 = x3d.field()
field41.setName("scale")
field41.setAccessType("initializeOnly")
field41.setType("SFFloat")
field41.setValue("0.5")

ComposedShader36.addField(field41)
field42 = x3d.field()
field42.setName("power")
field42.setAccessType("initializeOnly")
field42.setType("SFFloat")
field42.setValue("2")

ComposedShader36.addField(field42)
ShaderPart43 = x3d.ShaderPart()
ShaderPart43.setUrl(["../shaders/x_ite.vs","https://coderextreme.net/X3DJSONLD/src/main/shaders/x_ite.vs"])
ShaderPart43.setType("VERTEX")

ComposedShader36.addParts(ShaderPart43)
ShaderPart44 = x3d.ShaderPart()
ShaderPart44.setUSE("common")

ComposedShader36.addParts(ShaderPart44)

Appearance18.addShaders(ComposedShader36)

Shape16.setAppearance(Appearance18)

Transform15.addChildren(Shape16)

Scene11.addChildren(Transform15)

X3D0.setScene(Scene11)
X3D0.toFileX3D("././ball_RoundTrip.x3d")
