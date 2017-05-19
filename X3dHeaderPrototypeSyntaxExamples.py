from jnius import autoclass
from X3Dautoclass import *
X3D0 =  X3DObject().setProfile("Immersive").setVersion("3.2")
head1 = headObject()
component2 = componentObject().setName("Geospatial").setLevel(1)
head1.addComponent(component2)
component3 = componentObject().setName("NURBS").setLevel(2)
head1.addComponent(component3)
component4 = componentObject().setName("Core").setLevel(2)
head1.addComponent(component4)
component5 = componentObject().setName("Navigation").setLevel(1)
head1.addComponent(component5)
component6 = componentObject().setName("Text").setLevel(1)
head1.addComponent(component6)
meta7 = metaObject().setName("title").setContent("X3dHeaderPrototypeSyntaxExamples.x3d")
head1.addMeta(meta7)
meta8 = metaObject().setName("description").setContent("X3D scene header and prototype syntax examples. This example header indicates that the content is XML encoded, follows the Interactive Profile and explicitly lists additional necessary components. The X3D header may also contain additional semantic information. Used for specification EXAMPLE excerpts in 19776:1 XML Encoding.")
head1.addMeta(meta8)
meta9 = metaObject().setName("created").setContent("14 October 2002")
head1.addMeta(meta9)
meta10 = metaObject().setName("modified").setContent("26 November 2015")
head1.addMeta(meta10)
meta11 = metaObject().setName("creator").setContent("Don Brutzman")
head1.addMeta(meta11)
meta12 = metaObject().setName("specificationSection").setContent("X3D encodings, ISO/IEC 19776-1.3, Part 1: XML encoding, 4.3 XML file syntax")
head1.addMeta(meta12)
meta13 = metaObject().setName("specificationUrl").setContent("http://www.web3d.org/documents/specifications/19776-1/V3.3/Part01/concepts.html#XMLFileSyntax")
head1.addMeta(meta13)
meta14 = metaObject().setName("identifier").setContent("http://www.web3d.org/x3d/content/examples/Basic/X3dSpecifications/X3dHeaderPrototypeSyntaxExamples.x3d")
head1.addMeta(meta14)
meta15 = metaObject().setName("generator").setContent("X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit")
head1.addMeta(meta15)
meta16 = metaObject().setName("license").setContent("../license.html")
head1.addMeta(meta16)
meta17 = metaObject().setName("translated").setContent("17 May 2017")
head1.addMeta(meta17)
meta18 = metaObject().setName("generator").setContent("X3dToJson.xslt, http://www.web3d.org/x3d/stylesheets/X3dToJson.html")
head1.addMeta(meta18)
meta19 = metaObject().setName("reference").setContent("X3D JSON encoding: http://www.web3d.org/wiki/index.php/X3D_JSON_Encoding")
head1.addMeta(meta19)
meta20 = metaObject().setName("translated").setContent("17 May 2017")
head1.addMeta(meta20)
meta21 = metaObject().setName("generator").setContent("X3DJSONLD: https://github.com/coderextreme/X3DJSONLD")
head1.addMeta(meta21)
X3D0.setHead(head1)
Scene22 = SceneObject()
ExternProtoDeclare23 = ExternProtoDeclareObject().setName("ViewPositionOrientation").setUrl(["../../Savage/Tools/Authoring/ViewPositionOrientationPrototype.x3d#ViewPositionOrientation","https://savage.nps.edu/Savage/Tools/Authoring/ViewPositionOrientationPrototype.x3d#ViewPositionOrientation","../../Savage/Tools/Authoring/ViewPositionOrientationPrototype.wrl#ViewPositionOrientation","https://savage.nps.edu/Savage/Tools/Authoring/ViewPositionOrientationPrototype.wrl#ViewPositionOrientation"])
field24 = fieldObject().setType(fieldObject.TYPE_SFBOOL).setName("enabled").setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
ExternProtoDeclare23.addField(field24)
field25 = fieldObject().setType(fieldObject.TYPE_SFBOOL).setName("traceEnabled").setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY)
ExternProtoDeclare23.addField(field25)
field26 = fieldObject().setType(fieldObject.TYPE_SFBOOL).setName("set_traceEnabled").setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)
ExternProtoDeclare23.addField(field26)
field27 = fieldObject().setType(fieldObject.TYPE_SFVEC3F).setName("position_changed").setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY)
ExternProtoDeclare23.addField(field27)
field28 = fieldObject().setType(fieldObject.TYPE_SFROTATION).setName("orientation_changed").setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY)
ExternProtoDeclare23.addField(field28)
field29 = fieldObject().setType(fieldObject.TYPE_MFSTRING).setName("outputViewpointString").setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY)
ExternProtoDeclare23.addField(field29)
Scene22.addChild(ExternProtoDeclare23)
ProtoDeclare30 = ProtoDeclareObject().setName("NewWorldInfoNode")
ProtoBody31 = ProtoBodyObject()
WorldInfo32 = WorldInfoObject().setDEF("ExamplePrototypeBody")
ProtoBody31.addChild(WorldInfo32)
ProtoDeclare30.setProtoBody(ProtoBody31)
Scene22.addChild(ProtoDeclare30)
ProtoInstance33 = ProtoInstanceObject().setName("NewWorldInfoNode")
Scene22.addChild(ProtoInstance33)
ProtoDeclare34 = ProtoDeclareObject().setName("EmissiveMaterial")
ProtoInterface35 = ProtoInterfaceObject()
field36 = fieldObject().setType(fieldObject.TYPE_SFCOLOR).setName("onlyColor").setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT).setValue("1 0 0")
ProtoInterface35.addField(field36)
ProtoDeclare34.setProtoInterface(ProtoInterface35)
ProtoBody37 = ProtoBodyObject()

ProtoBody37.addComments(CommentsBlock("Override default diffuseColor value 0.8 0.8 0.8"))
Material38 = MaterialObject().setDiffuseColor([0,0,0])

Material38.addComments(CommentsBlock("Connect emissiveColor field of current node to onlyColor field of parent ProtoDeclare."))
IS39 = ISObject()
connect40 = connectObject().setNodeField("emissiveColor").setProtoField("onlyColor")
IS39.addConnect(connect40)
Material38.setIS(IS39)
ProtoBody37.addChild(Material38)
ProtoDeclare34.setProtoBody(ProtoBody37)
Scene22.addChild(ProtoDeclare34)
ProtoDeclare41 = ProtoDeclareObject().setName("ShiftGroupUp2m")
ProtoInterface42 = ProtoInterfaceObject()
field43 = fieldObject().setType(fieldObject.TYPE_MFNODE).setName("children").setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
Group44 = GroupObject().setDEF("DefaultNodeValue").setBboxSize([2,2,2])

Group44.addComments(CommentsBlock("Authors need to override this node when creating the ProtoInstance fieldValue name=\"children\""))
field43.addChild(Group44)
ProtoInterface42.addField(field43)
ProtoDeclare41.setProtoInterface(ProtoInterface42)
ProtoBody45 = ProtoBodyObject()
Transform46 = TransformObject().setTranslation([0,2,0])
Group47 = GroupObject()
IS48 = ISObject()
connect49 = connectObject().setNodeField("children").setProtoField("children")
IS48.addConnect(connect49)
Group47.setIS(IS48)
Transform46.addChild(Group47)
ProtoBody45.addChild(Transform46)
ProtoDeclare41.setProtoBody(ProtoBody45)
Scene22.addChild(ProtoDeclare41)
ProtoInstance50 = ProtoInstanceObject().setName("ShiftGroupUp2m")
Scene22.addChild(ProtoInstance50)

Scene22.addComments(CommentsBlock("===================="))
Viewpoint51 = ViewpointObject().setDEF("ExampleSingleElement").setDescription("Hello syntax")
Scene22.addChild(Viewpoint51)
Group52 = GroupObject().setDEF("ExampleChildElement")
Shape53 = ShapeObject()
Box54 = BoxObject()
Shape53.setGeometry(Box54)
Appearance55 = AppearanceObject()
Material56 = MaterialObject().setDiffuseColor([0.6,0.4,0.2])
Appearance55.setMaterial(Material56)
Shape53.setAppearance(Appearance55)
Group52.addChild(Shape53)
Scene22.addChild(Group52)
Transform57 = TransformObject().setDEF("TransformExampleUSE").setRotation([0,1,0,0.78]).setTranslation([0,2.5,0])
Group58 = GroupObject().setUSE("ExampleChildElement")
Transform57.addChild(Group58)
Scene22.addChild(Transform57)
Collision59 = CollisionObject()
Shape60 = ShapeObject()
Text61 = TextObject().setString(["He said, "Immel did it!""])
Shape60.setGeometry(Text61)

Shape60.addComments(CommentsBlock("alternative: Text string='\"He said, \\&quot;Immel did it!\\&quot;\"'"))
Appearance62 = AppearanceObject()
Material63 = MaterialObject()
Appearance62.setMaterial(Material63)
Shape60.setAppearance(Appearance62)
Collision59.setProxy(Shape60)
Group64 = GroupObject().setUSE("ExampleChildElement")
Collision59.addChild(Group64)
Scene22.addChild(Collision59)
Transform65 = TransformObject().setTranslation([0,-2.5,0])
Shape66 = ShapeObject()
Appearance67 = AppearanceObject()
ProtoInstance68 = ProtoInstanceObject().setName("EmissiveMaterial")
fieldValue69 = fieldValueObject().setName("onlyColor").setValue("0.2 0.6 0.6")
ProtoInstance68.addFieldValue(fieldValue69)
Appearance67.setMaterial(ProtoInstance68)
Shape66.setAppearance(Appearance67)
Text70 = TextObject().setString(["X3D Header Prototype syntax examples","(view console for EXTERNPROTO output)"])
FontStyle71 = FontStyleObject().setJustify(["MIDDLE","MIDDLE"]).setSize(0.6)
Text70.setFontStyle(FontStyle71)
Shape66.setGeometry(Text70)
Transform65.addChild(Shape66)
Scene22.addChild(Transform65)
ProtoInstance72 = ProtoInstanceObject().setName("ViewPositionOrientation")
fieldValue73 = fieldValueObject().setName("enabled").setValue("true")
ProtoInstance72.addFieldValue(fieldValue73)
Scene22.addChild(ProtoInstance72)
TimeSensor74 = TimeSensorObject().setDEF("Clock").setCycleInterval(4).setLoop(True)
Scene22.addChild(TimeSensor74)
OrientationInterpolator75 = OrientationInterpolatorObject().setDEF("Spinner").setKey([0,0.5,1]).setKeyValue([0,1,0,0,0,1,0,3.14159,0,1,0,6.28318])
Scene22.addChild(OrientationInterpolator75)
ROUTE76 = ROUTEObject().setFromField("fraction_changed").setFromNode("Clock").setToField("set_fraction").setToNode("Spinner")
Scene22.addChild(ROUTE76)
ROUTE77 = ROUTEObject().setFromField("value_changed").setFromNode("Spinner").setToField("rotation").setToNode("TransformExampleUSE")
Scene22.addChild(ROUTE77)
Inline78 = InlineObject().setDEF("someInline").setUrl(["someUrl.x3d","http://www.web3d.org/x3d/content/examples/Basic/X3dSpecifications/someUrl.x3d"])
Scene22.addChild(Inline78)
IMPORT79 = IMPORTObject().setAS("someInlineRoot").setImportedDEF("someName").setInlineDEF("someInline")
Scene22.addChild(IMPORT79)
PositionInterpolator80 = PositionInterpolatorObject().setDEF("StayInPlace").setKey([0,1]).setKeyValue([0,0,0,0,0,0])
Scene22.addChild(PositionInterpolator80)
ROUTE81 = ROUTEObject().setFromField("fraction_changed").setFromNode("Clock").setToField("set_fraction").setToNode("StayInPlace")
Scene22.addChild(ROUTE81)
ROUTE82 = ROUTEObject().setFromField("value_changed").setFromNode("StayInPlace").setToField("set_translation").setToNode("someInlineRoot")
Scene22.addChild(ROUTE82)
X3D0.setScene(Scene22)

X3D0.toFileX3D("X3dHeaderPrototypeSyntaxExamples.new.x3d")
