import jnius_config
jnius_config.set_classpath('.', 'X3DJSAIL.3.3.full.jar')
from jnius import autoclass
from X3Dautoclass import *
X3D0 = X3DObject()
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
component4 = componentObject()
component4.setName("Shaders")
component4.setLevel(1)

head1.addComponent(component4)
component5 = componentObject()
component5.setName("CubeMapTexturing")
component5.setLevel(1)

head1.addComponent(component5)
meta6 = metaObject()
meta6.setName("title")
meta6.setContent("bubbles.x3d")

head1.addMeta(meta6)
meta7 = metaObject()
meta7.setName("creator")
meta7.setContent("John Carlson")

head1.addMeta(meta7)
meta8 = metaObject()
meta8.setName("generator")
meta8.setContent("manual")

head1.addMeta(meta8)
meta9 = metaObject()
meta9.setName("identifier")
meta9.setContent("https://coderextreme.net/X3DJSONLD/bubbles.x3d")

head1.addMeta(meta9)
meta10 = metaObject()
meta10.setName("description")
meta10.setContent("not sure what this is")

head1.addMeta(meta10)

X3D0.setHead(head1)
Scene11 = SceneObject()
NavigationInfo12 = NavigationInfoObject()
NavigationInfo12.setType(["EXAMINE"])

Scene11.addChildren(NavigationInfo12)
Viewpoint13 = ViewpointObject()
Viewpoint13.setDEF("Tour")
Viewpoint13.setDescription("Tour Views")

Scene11.addChildren(Viewpoint13)
Viewpoint14 = ViewpointObject()
Viewpoint14.setPosition([0,0,4])
Viewpoint14.setDescription("sphere in road")

Scene11.addChildren(Viewpoint14)
Background15 = BackgroundObject()
Background15.setBackUrl(["../resources/images/all_probes/uffizi_cross/uffizi_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_back.png"])
Background15.setBottomUrl(["../resources/images/all_probes/uffizi_cross/uffizi_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_bottom.png"])
Background15.setFrontUrl(["../resources/images/all_probes/uffizi_cross/uffizi_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_front.png"])
Background15.setLeftUrl(["../resources/images/all_probes/uffizi_cross/uffizi_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_left.png"])
Background15.setRightUrl(["../resources/images/all_probes/uffizi_cross/uffizi_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_right.png"])
Background15.setTopUrl(["../resources/images/all_probes/uffizi_cross/uffizi_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_top.png"])

Scene11.addChildren(Background15)
Transform16 = TransformObject()
Transform16.setDEF("Rose01")
Shape17 = ShapeObject()
Sphere18 = SphereObject()

Shape17.setGeometry(Sphere18)
Appearance19 = AppearanceObject()
Appearance19.setDEF("_01_-_Default")
Material20 = MaterialObject()
Material20.setDiffuseColor([0.7,0.7,0.7])
Material20.setSpecularColor([0.5,0.5,0.5])

Appearance19.setMaterial(Material20)
ComposedCubeMapTexture21 = ComposedCubeMapTextureObject()
ImageTexture22 = ImageTextureObject()
ImageTexture22.setUrl(["../resources/images/all_probes/uffizi_cross/uffizi_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_back.png"])

ComposedCubeMapTexture21.setBack(ImageTexture22)
ImageTexture23 = ImageTextureObject()
ImageTexture23.setUrl(["../resources/images/all_probes/uffizi_cross/uffizi_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_bottom.png"])

ComposedCubeMapTexture21.setBottom(ImageTexture23)
ImageTexture24 = ImageTextureObject()
ImageTexture24.setUrl(["../resources/images/all_probes/uffizi_cross/uffizi_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_front.png"])

ComposedCubeMapTexture21.setFront(ImageTexture24)
ImageTexture25 = ImageTextureObject()
ImageTexture25.setUrl(["../resources/images/all_probes/uffizi_cross/uffizi_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_left.png"])

ComposedCubeMapTexture21.setLeft(ImageTexture25)
ImageTexture26 = ImageTextureObject()
ImageTexture26.setUrl(["../resources/images/all_probes/uffizi_cross/uffizi_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_right.png"])

ComposedCubeMapTexture21.setRight(ImageTexture26)
ImageTexture27 = ImageTextureObject()
ImageTexture27.setUrl(["../resources/images/all_probes/uffizi_cross/uffizi_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/uffizi_cross/uffizi_top.png"])

ComposedCubeMapTexture21.setTop(ImageTexture27)

Appearance19.setTexture(ComposedCubeMapTexture21)
ComposedShader28 = ComposedShaderObject()
ComposedShader28.setDEF("cobweb")
ComposedShader28.setLanguage("GLSL")
field29 = fieldObject()
field29.setName("cube")
field29.setAccessType("inputOutput")
field29.setType("SFInt32")
field29.setValue("0")

ComposedShader28.addField(field29)
field30 = fieldObject()
field30.setName("chromaticDispertion")
field30.setAccessType("inputOutput")
field30.setType("SFVec3f")
field30.setValue("0.98 1 1.033")

ComposedShader28.addField(field30)
field31 = fieldObject()
field31.setName("bias")
field31.setAccessType("inputOutput")
field31.setType("SFFloat")
field31.setValue("0.5")

ComposedShader28.addField(field31)
field32 = fieldObject()
field32.setName("scale")
field32.setAccessType("inputOutput")
field32.setType("SFFloat")
field32.setValue("0.5")

ComposedShader28.addField(field32)
field33 = fieldObject()
field33.setName("power")
field33.setAccessType("inputOutput")
field33.setType("SFFloat")
field33.setValue("2")

ComposedShader28.addField(field33)
ShaderPart34 = ShaderPartObject()
ShaderPart34.setUrl(["../shaders/cobweb.vs","https://coderextreme.net/X3DJSONLD/shaders/cobweb.vs"])
ShaderPart34.setType("VERTEX")

ComposedShader28.addParts(ShaderPart34)
ShaderPart35 = ShaderPartObject()
ShaderPart35.setUrl(["../shaders/pc_bubbles.fs","https://coderextreme.net/X3DJSONLD/shaders/pc_bubbles.fs"])
ShaderPart35.setType("FRAGMENT")

ComposedShader28.addParts(ShaderPart35)

Appearance19.addShaders(ComposedShader28)
ComposedShader36 = ComposedShaderObject()
ComposedShader36.setDEF("x3dom")
ComposedShader36.setLanguage("GLSL")
field37 = fieldObject()
field37.setName("cube")
field37.setAccessType("inputOutput")
field37.setType("SFInt32")
field37.setValue("0")

ComposedShader36.addField(field37)
field38 = fieldObject()
field38.setName("chromaticDispertion")
field38.setAccessType("inputOutput")
field38.setType("SFVec3f")
field38.setValue("0.98 1 1.033")

ComposedShader36.addField(field38)
field39 = fieldObject()
field39.setName("bias")
field39.setAccessType("inputOutput")
field39.setType("SFFloat")
field39.setValue("0.5")

ComposedShader36.addField(field39)
field40 = fieldObject()
field40.setName("scale")
field40.setAccessType("inputOutput")
field40.setType("SFFloat")
field40.setValue("0.5")

ComposedShader36.addField(field40)
field41 = fieldObject()
field41.setName("power")
field41.setAccessType("inputOutput")
field41.setType("SFFloat")
field41.setValue("2")

ComposedShader36.addField(field41)
ShaderPart42 = ShaderPartObject()
ShaderPart42.setUrl(["../shaders/x3dom.vs","https://coderextreme.net/X3DJSONLD/shaders/x3dom.vs"])
ShaderPart42.setType("VERTEX")

ComposedShader36.addParts(ShaderPart42)
ShaderPart43 = ShaderPartObject()
ShaderPart43.setUrl(["../shaders/pc_bubbles.fs","https://coderextreme.net/X3DJSONLD/shaders/pc_bubbles.fs"])
ShaderPart43.setType("FRAGMENT")

ComposedShader36.addParts(ShaderPart43)

Appearance19.addShaders(ComposedShader36)

Shape17.setAppearance(Appearance19)

Transform16.addChildren(Shape17)

Scene11.addChildren(Transform16)
TimeSensor44 = TimeSensorObject()
TimeSensor44.setDEF("TourTime")
TimeSensor44.setCycleInterval(5)
TimeSensor44.setLoop(True)

Scene11.addChildren(TimeSensor44)
PositionInterpolator45 = PositionInterpolatorObject()
PositionInterpolator45.setDEF("TourPosition")
PositionInterpolator45.setKey([0,1])
PositionInterpolator45.setKeyValue([0,0,10,0,0,-10])

Scene11.addChildren(PositionInterpolator45)
OrientationInterpolator46 = OrientationInterpolatorObject()
OrientationInterpolator46.setDEF("TourOrientation")
OrientationInterpolator46.setKey([0,1])
OrientationInterpolator46.setKeyValue([0,1,0,0,0,1,0,3.1416])

Scene11.addChildren(OrientationInterpolator46)
Script47 = ScriptObject()
Script47.setDEF("RandomTourTime")
field48 = fieldObject()
field48.setName("set_cycle")
field48.setAccessType("inputOnly")
field48.setType("SFTime")

Script47.addField(field48)
field49 = fieldObject()
field49.setName("lastKey")
field49.setAccessType("inputOutput")
field49.setType("SFFloat")
field49.setValue("0")

Script47.addField(field49)
field50 = fieldObject()
field50.setName("orientations")
field50.setAccessType("inputOutput")
field50.setType("MFRotation")
field50.setValue("0 1 0 0 0 1 0 -1.57 0 1 0 3.14 0 1 0 1.57 0 1 0 0 1 0 0 -1.57 0 1 0 0 1 0 0 1.57 0 1 0 0")

Script47.addField(field50)
field51 = fieldObject()
field51.setName("positions")
field51.setAccessType("inputOutput")
field51.setType("MFVec3f")
field51.setValue("0 0 10 -10 0 0 0 0 -10 10 0 0 0 0 10 0 10 0 0 0 10 0 -10 0 0 0 10")

Script47.addField(field51)
field52 = fieldObject()
field52.setName("position_changed")
field52.setAccessType("outputOnly")
field52.setType("MFVec3f")

Script47.addField(field52)
field53 = fieldObject()
field53.setName("set_orientation")
field53.setAccessType("inputOnly")
field53.setType("MFRotation")

Script47.addField(field53)
field54 = fieldObject()
field54.setName("orientation_changed")
field54.setAccessType("outputOnly")
field54.setType("MFRotation")

Script47.addField(field54)

Script47.setSourceCode('''ecmascript:\n"+
"               function set_cycle(value) {\n"+
"                        var ov = lastKey;\n"+
"                        do {\n"+
"                            lastKey = Math.round(Math.random()*(positions.length-1));\n"+
"                        } while (lastKey === ov);\n"+
"                        var vc = lastKey;\n"+
"\n"+
"                        orientation_changed = new MFRotation();\n"+
"                        orientation_changed[0] = new SFRotation(orientations[ov].x, orientations[ov].y, orientations[ov].z, orientations[ov].w);\n"+
"                        orientation_changed[1] = new SFRotation(orientations[vc].x, orientations[vc].y, orientations[vc].z, orientations[vc].w);\n"+
"                        position_changed = new MFVec3f();\n"+
"                        position_changed[0] = new SFVec3f(positions[ov].x,positions[ov].y,positions[ov].z);\n"+
"                        position_changed[1] = new SFVec3f(positions[vc].x,positions[vc].y,positions[vc].z);\n"+
"                    // }\n"+
"               }''')

Scene11.addChildren(Script47)
ROUTE55 = ROUTEObject()
ROUTE55.setFromNode("TourTime")
ROUTE55.setFromField("cycleTime_changed")
ROUTE55.setToNode("RandomTourTime")
ROUTE55.setToField("set_cycle")

Scene11.addChildren(ROUTE55)
ROUTE56 = ROUTEObject()
ROUTE56.setFromNode("RandomTourTime")
ROUTE56.setFromField("orientation_changed")
ROUTE56.setToNode("TourOrientation")
ROUTE56.setToField("set_keyValue")

Scene11.addChildren(ROUTE56)
ROUTE57 = ROUTEObject()
ROUTE57.setFromNode("RandomTourTime")
ROUTE57.setFromField("position_changed")
ROUTE57.setToNode("TourPosition")
ROUTE57.setToField("set_keyValue")

Scene11.addChildren(ROUTE57)
ROUTE58 = ROUTEObject()
ROUTE58.setFromNode("TourTime")
ROUTE58.setFromField("fraction_changed")
ROUTE58.setToNode("TourOrientation")
ROUTE58.setToField("set_fraction")

Scene11.addChildren(ROUTE58)
ROUTE59 = ROUTEObject()
ROUTE59.setFromNode("TourOrientation")
ROUTE59.setFromField("value_changed")
ROUTE59.setToNode("Tour")
ROUTE59.setToField("set_orientation")

Scene11.addChildren(ROUTE59)
ROUTE60 = ROUTEObject()
ROUTE60.setFromNode("TourTime")
ROUTE60.setFromField("fraction_changed")
ROUTE60.setToNode("TourPosition")
ROUTE60.setToField("set_fraction")

Scene11.addChildren(ROUTE60)
ROUTE61 = ROUTEObject()
ROUTE61.setFromNode("TourPosition")
ROUTE61.setFromField("value_changed")
ROUTE61.setToNode("Tour")
ROUTE61.setToField("set_position")

Scene11.addChildren(ROUTE61)

X3D0.setScene(Scene11)
X3D0.toFileX3D("././bubbles.new.x3d")
