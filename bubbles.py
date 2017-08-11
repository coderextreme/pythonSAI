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
meta4.setContent("bubbles.x3d")

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
meta7.setContent("http://coderextreme.net/X3DJSONLD/bubbles.x3d")

head1.addMeta(meta7)
meta8 = metaObject()
meta8.setName("description")
meta8.setContent("not sure what this is")

head1.addMeta(meta8)
X3D0.setHead(head1)
Scene9 = SceneObject()

NavigationInfo10 = NavigationInfoObject()
NavigationInfo10.setType(["EXAMINE"])

Scene9.addChild(NavigationInfo10)
Viewpoint11 = ViewpointObject()
Viewpoint11.setDEF("Tour")
Viewpoint11.setDescription("Tour Views")

Scene9.addChild(Viewpoint11)
Viewpoint12 = ViewpointObject()
Viewpoint12.setPosition([0,0,4])
Viewpoint12.setDescription("sphere in road")

Scene9.addChild(Viewpoint12)
Background13 = BackgroundObject()
Background13.setBackUrl(["cubemap/all_probes/uffizi_cross/uffizi_back.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/uffizi_cross/uffizi_back.png"])
Background13.setBottomUrl(["cubemap/all_probes/uffizi_cross/uffizi_bottom.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/uffizi_cross/uffizi_bottom.png"])
Background13.setFrontUrl(["cubemap/all_probes/uffizi_cross/uffizi_front.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/uffizi_cross/uffizi_front.png"])
Background13.setLeftUrl(["cubemap/all_probes/uffizi_cross/uffizi_left.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/uffizi_cross/uffizi_left.png"])
Background13.setRightUrl(["cubemap/all_probes/uffizi_cross/uffizi_right.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/uffizi_cross/uffizi_right.png"])
Background13.setTopUrl(["cubemap/all_probes/uffizi_cross/uffizi_top.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/uffizi_cross/uffizi_top.png"])

Scene9.addChild(Background13)
Transform14 = TransformObject()
Transform14.setDEF("Rose01")

Shape15 = ShapeObject()

Sphere16 = SphereObject()

Shape15.setGeometry(Sphere16)
Appearance17 = AppearanceObject()
Appearance17.setDEF("_01_-_Default")

Material18 = MaterialObject()
Material18.setDiffuseColor([0.7,0.7,0.7])
Material18.setSpecularColor([0.5,0.5,0.5])

Appearance17.setMaterial(Material18)
ComposedCubeMapTexture19 = ComposedCubeMapTextureObject()

ImageTexture20 = ImageTextureObject()
ImageTexture20.setUrl(["cubemap/all_probes/uffizi_cross/uffizi_back.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/uffizi_cross/uffizi_back.png"])

ComposedCubeMapTexture19.setBack(ImageTexture20)
ImageTexture21 = ImageTextureObject()
ImageTexture21.setUrl(["cubemap/all_probes/uffizi_cross/uffizi_bottom.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/uffizi_cross/uffizi_bottom.png"])

ComposedCubeMapTexture19.setBottom(ImageTexture21)
ImageTexture22 = ImageTextureObject()
ImageTexture22.setUrl(["cubemap/all_probes/uffizi_cross/uffizi_front.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/uffizi_cross/uffizi_front.png"])

ComposedCubeMapTexture19.setFront(ImageTexture22)
ImageTexture23 = ImageTextureObject()
ImageTexture23.setUrl(["cubemap/all_probes/uffizi_cross/uffizi_left.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/uffizi_cross/uffizi_left.png"])

ComposedCubeMapTexture19.setLeft(ImageTexture23)
ImageTexture24 = ImageTextureObject()
ImageTexture24.setUrl(["cubemap/all_probes/uffizi_cross/uffizi_right.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/uffizi_cross/uffizi_right.png"])

ComposedCubeMapTexture19.setRight(ImageTexture24)
ImageTexture25 = ImageTextureObject()
ImageTexture25.setUrl(["cubemap/all_probes/uffizi_cross/uffizi_top.png","http://coderextreme.net/X3DJSONLD/cubemap/all_probes/uffizi_cross/uffizi_top.png"])

ComposedCubeMapTexture19.setTop(ImageTexture25)
Appearance17.setTexture(ComposedCubeMapTexture19)
ComposedShader26 = ComposedShaderObject()
ComposedShader26.setDEF("cobweb")
ComposedShader26.setLanguage("GLSL")

field27 = fieldObject()
field27.setType(fieldObject.TYPE_SFINT32)
field27.setName("cube")
field27.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field27.setValue("0")

ComposedShader26.addField(field27)
field28 = fieldObject()
field28.setType(fieldObject.TYPE_SFVEC3F)
field28.setName("chromaticDispertion")
field28.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field28.setValue("0.98 1 1.033")

ComposedShader26.addField(field28)
field29 = fieldObject()
field29.setType(fieldObject.TYPE_SFFLOAT)
field29.setName("bias")
field29.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field29.setValue("0.5")

ComposedShader26.addField(field29)
field30 = fieldObject()
field30.setType(fieldObject.TYPE_SFFLOAT)
field30.setName("scale")
field30.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field30.setValue("0.5")

ComposedShader26.addField(field30)
field31 = fieldObject()
field31.setType(fieldObject.TYPE_SFFLOAT)
field31.setName("power")
field31.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field31.setValue("2")

ComposedShader26.addField(field31)
ShaderPart32 = ShaderPartObject()
ShaderPart32.setType("VERTEX")
ShaderPart32.setUrl(["cobweb.vs","http://coderextreme.net/X3DJSONLD/cobweb.vs"])

ComposedShader26.addParts(ShaderPart32)
ShaderPart33 = ShaderPartObject()
ShaderPart33.setType("FRAGMENT")
ShaderPart33.setUrl(["pc_bubbles.fs","http://coderextreme.net/X3DJSONLD/pc_bubbles.fs"])

ComposedShader26.addParts(ShaderPart33)
Appearance17.addShaders(ComposedShader26)
ComposedShader34 = ComposedShaderObject()
ComposedShader34.setDEF("x3dom")
ComposedShader34.setLanguage("GLSL")

field35 = fieldObject()
field35.setType(fieldObject.TYPE_SFINT32)
field35.setName("cube")
field35.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field35.setValue("0")

ComposedShader34.addField(field35)
field36 = fieldObject()
field36.setType(fieldObject.TYPE_SFVEC3F)
field36.setName("chromaticDispertion")
field36.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field36.setValue("0.98 1 1.033")

ComposedShader34.addField(field36)
field37 = fieldObject()
field37.setType(fieldObject.TYPE_SFFLOAT)
field37.setName("bias")
field37.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field37.setValue("0.5")

ComposedShader34.addField(field37)
field38 = fieldObject()
field38.setType(fieldObject.TYPE_SFFLOAT)
field38.setName("scale")
field38.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field38.setValue("0.5")

ComposedShader34.addField(field38)
field39 = fieldObject()
field39.setType(fieldObject.TYPE_SFFLOAT)
field39.setName("power")
field39.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field39.setValue("2")

ComposedShader34.addField(field39)
ShaderPart40 = ShaderPartObject()
ShaderPart40.setType("VERTEX")
ShaderPart40.setUrl(["x3dom.vs","http://coderextreme.net/X3DJSONLD/x3dom.vs"])

ComposedShader34.addParts(ShaderPart40)
ShaderPart41 = ShaderPartObject()
ShaderPart41.setType("FRAGMENT")
ShaderPart41.setUrl(["pc_bubbles.fs","http://coderextreme.net/X3DJSONLD/pc_bubbles.fs"])

ComposedShader34.addParts(ShaderPart41)
Appearance17.addShaders(ComposedShader34)
Shape15.setAppearance(Appearance17)
Transform14.addChild(Shape15)
Scene9.addChild(Transform14)
TimeSensor42 = TimeSensorObject()
TimeSensor42.setDEF("TourTime")
TimeSensor42.setCycleInterval(5)
TimeSensor42.setLoop(True)

Scene9.addChild(TimeSensor42)
PositionInterpolator43 = PositionInterpolatorObject()
PositionInterpolator43.setDEF("TourPosition")
PositionInterpolator43.setKey([0,1])
PositionInterpolator43.setKeyValue([0,0,10,0,0,-10])

Scene9.addChild(PositionInterpolator43)
OrientationInterpolator44 = OrientationInterpolatorObject()
OrientationInterpolator44.setDEF("TourOrientation")
OrientationInterpolator44.setKey([0,1])
OrientationInterpolator44.setKeyValue([0,1,0,0,0,1,0,3.1416])

Scene9.addChild(OrientationInterpolator44)
Script45 = ScriptObject()
Script45.setDEF("RandomTourTime")

field46 = fieldObject()
field46.setType(fieldObject.TYPE_SFTIME)
field46.setName("set_cycle")
field46.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)

Script45.addField(field46)
field47 = fieldObject()
field47.setType(fieldObject.TYPE_SFFLOAT)
field47.setName("lastKey")
field47.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field47.setValue("0")

Script45.addField(field47)
field48 = fieldObject()
field48.setType(fieldObject.TYPE_MFROTATION)
field48.setName("orientations")
field48.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field48.setValue("0 1 0 0 0 1 0 -1.57 0 1 0 3.14 0 1 0 1.57 0 1 0 0 1 0 0 -1.57 0 1 0 0 1 0 0 1.57 0 1 0 0")

Script45.addField(field48)
field49 = fieldObject()
field49.setType(fieldObject.TYPE_MFVEC3F)
field49.setName("positions")
field49.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field49.setValue("0 0 10 -10 0 0 0 0 -10 10 0 0 0 0 10 0 10 0 0 0 10 0 -10 0 0 0 10")

Script45.addField(field49)
field50 = fieldObject()
field50.setType(fieldObject.TYPE_MFVEC3F)
field50.setName("position")
field50.setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY)

Script45.addField(field50)
field51 = fieldObject()
field51.setType(fieldObject.TYPE_MFROTATION)
field51.setName("orientation")
field51.setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY)

Script45.addField(field51)

Script45.setSourceCode("ecmascript:\n"+
"               function set_cycle(value) {\n"+
"                        //var positions = [[0, 0, 10], [-10, 0, 0], [0, 0, -10], [10, 0, 0], [0, 0, 10], [0, 10, 0], [0, 0, 10], [0, -10, 0], [0, 0, 10]];\n"+
"                        //var orientations = [[0, 1, 0, 0], [0, 1, 0, -1.57], [0, 1, 0, 3.14], [0, 1, 0, 1.57], [0, 1, 0, 0] [1, 0, 0, -1.57], [0, 1, 0, 0], [1, 0, 0, 1.57], [0, 1, 0, 0]];\n"+
"                        //Browser.println(lastKey);\n"+
"                        var ov = lastKey;\n"+
"                        // Browser.println(ov);      \n"+
"                        //Browser.println(positions.length);                  \n"+
"                        do {\n"+
"                            lastKey = Math.round(Math.random()*(positions.length-1));\n"+
"                        } while (lastKey === ov);\n"+
"                        // Browser.println(lastKey);\n"+
"                        var vc = lastKey;\n"+
"                        \n"+
"                        // Browser.println(orientations[ov]);\n"+
"                        // Browser.println(orientations[vc]);\n"+
"                        orientation = new MFRotation();\n"+
"                        orientation[0] = new SFRotation(orientations[ov][0], orientations[ov][1], orientations[ov][2], orientations[ov][3]);\n"+
"                        orientation[1] = new SFRotation(orientations[vc][0], orientations[vc][1], orientations[vc][2], orientations[vc][3]);\n"+
"                        // Browser.println(positions[ov]);\n"+
"                        // Browser.println(positions[vc]);\n"+
"                        position = new MFVec3f();\n"+
"                        position[0] = new SFVec3f(positions[ov][0],positions[ov][1],positions[ov][2]);\n"+
"                        position[1] = new SFVec3f(positions[vc][0],positions[vc][1],positions[vc][2]);\n"+
"                    // }\n"+
"               }\n"+
"")
Scene9.addChild(Script45)
ROUTE52 = ROUTEObject()
ROUTE52.setFromNode("TourTime")
ROUTE52.setFromField("cycleTime")
ROUTE52.setToNode("RandomTourTime")
ROUTE52.setToField("set_cycle")

Scene9.addChild(ROUTE52)
ROUTE53 = ROUTEObject()
ROUTE53.setFromNode("RandomTourTime")
ROUTE53.setFromField("orientation")
ROUTE53.setToNode("TourOrientation")
ROUTE53.setToField("keyValue")

Scene9.addChild(ROUTE53)
ROUTE54 = ROUTEObject()
ROUTE54.setFromNode("RandomTourTime")
ROUTE54.setFromField("position")
ROUTE54.setToNode("TourPosition")
ROUTE54.setToField("keyValue")

Scene9.addChild(ROUTE54)
ROUTE55 = ROUTEObject()
ROUTE55.setFromNode("TourTime")
ROUTE55.setFromField("fraction_changed")
ROUTE55.setToNode("TourOrientation")
ROUTE55.setToField("set_fraction")

Scene9.addChild(ROUTE55)
ROUTE56 = ROUTEObject()
ROUTE56.setFromNode("TourOrientation")
ROUTE56.setFromField("value_changed")
ROUTE56.setToNode("Tour")
ROUTE56.setToField("set_orientation")

Scene9.addChild(ROUTE56)
ROUTE57 = ROUTEObject()
ROUTE57.setFromNode("TourTime")
ROUTE57.setFromField("fraction_changed")
ROUTE57.setToNode("TourPosition")
ROUTE57.setToField("set_fraction")

Scene9.addChild(ROUTE57)
ROUTE58 = ROUTEObject()
ROUTE58.setFromNode("TourPosition")
ROUTE58.setFromField("value_changed")
ROUTE58.setToNode("Tour")
ROUTE58.setToField("set_position")

Scene9.addChild(ROUTE58)
X3D0.setScene(Scene9)

X3D0.toFileX3D("./bubbles.new.x3d")
