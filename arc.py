from jnius import autoclass
from X3Dautoclass import *
X3D0 =  X3DObject()
X3D0.setProfile("Immersive")
X3D0.setVersion("3.3")

head1 = headObject()

meta2 = metaObject()
meta2.setName("title")
meta2.setContent("arc.x3d")

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
meta5.setContent("http://coderextreme.net/X3DJSONLD/arc.x3d")

head1.addMeta(meta5)
meta6 = metaObject()
meta6.setName("description")
meta6.setContent("an attempt to implement an arc in a graph")

head1.addMeta(meta6)
X3D0.setHead(head1)
Scene7 = SceneObject()

Viewpoint8 = ViewpointObject()
Viewpoint8.setPosition([0,0,5])
Viewpoint8.setDescription("a moving graph")

Scene7.addChild(Viewpoint8)
Background9 = BackgroundObject()
Background9.setSkyColor([0.4,0.4,0.4])

Scene7.addChild(Background9)
Transform10 = TransformObject()
Transform10.setDEF("cylinder1")

Shape11 = ShapeObject()

Appearance12 = AppearanceObject()

Material13 = MaterialObject()
Material13.setDiffuseColor([0.2,0.7,0.7])

Appearance12.setMaterial(Material13)
Shape11.setAppearance(Appearance12)
Cylinder14 = CylinderObject()
Cylinder14.setRadius(0.1)

Shape11.setGeometry(Cylinder14)
Transform10.addChild(Shape11)
Scene7.addChild(Transform10)
Transform15 = TransformObject()
Transform15.setDEF("cylinder2")

Shape16 = ShapeObject()

Appearance17 = AppearanceObject()

Material18 = MaterialObject()
Material18.setDiffuseColor([0.2,0.7,0.7])

Appearance17.setMaterial(Material18)
Shape16.setAppearance(Appearance17)
Cylinder19 = CylinderObject()
Cylinder19.setRadius(0.1)

Shape16.setGeometry(Cylinder19)
Transform15.addChild(Shape16)
Scene7.addChild(Transform15)
Transform20 = TransformObject()
Transform20.setDEF("cylinder3")

Shape21 = ShapeObject()

Appearance22 = AppearanceObject()

Material23 = MaterialObject()
Material23.setDiffuseColor([0.2,0.7,0.7])

Appearance22.setMaterial(Material23)
Shape21.setAppearance(Appearance22)
Cylinder24 = CylinderObject()
Cylinder24.setRadius(0.1)

Shape21.setGeometry(Cylinder24)
Transform20.addChild(Shape21)
Scene7.addChild(Transform20)
ProtoDeclare25 = ProtoDeclareObject()
ProtoDeclare25.setName("point")

ProtoInterface26 = ProtoInterfaceObject()

field27 = fieldObject()
field27.setType(fieldObject.TYPE_SFVEC3F)
field27.setName("translation")
field27.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field27.setValue("0 0 0")

ProtoInterface26.addField(field27)
ProtoDeclare25.setProtoInterface(ProtoInterface26)
ProtoBody28 = ProtoBodyObject()

Transform29 = TransformObject()
Transform29.setDEF("node")

IS30 = ISObject()

connect31 = connectObject()
connect31.setNodeField("translation")
connect31.setProtoField("translation")

IS30.addConnect(connect31)
Transform29.setIS(IS30)
Shape32 = ShapeObject()

Sphere33 = SphereObject()
Sphere33.setRadius(0.1)

Shape32.setGeometry(Sphere33)
Appearance34 = AppearanceObject()

Material35 = MaterialObject()
Material35.setDiffuseColor([1,0,0])

Appearance34.setMaterial(Material35)
Shape32.setAppearance(Appearance34)
Transform29.addChild(Shape32)
PositionInterpolator36 = PositionInterpolatorObject()
PositionInterpolator36.setDEF("PI1")
PositionInterpolator36.setKey([0,1])
PositionInterpolator36.setKeyValue([0,0,0,0,5,0])

Transform29.addChild(PositionInterpolator36)
Script37 = ScriptObject()
Script37.setDEF("MB1")

field38 = fieldObject()
field38.setType(fieldObject.TYPE_SFVEC3F)
field38.setName("translation")
field38.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field38.setValue("50 50 0")

Script37.addField(field38)
field39 = fieldObject()
field39.setType(fieldObject.TYPE_SFVEC3F)
field39.setName("old")
field39.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field39.setValue("0 0 0")

Script37.addField(field39)
field40 = fieldObject()
field40.setType(fieldObject.TYPE_SFTIME)
field40.setName("set_location")
field40.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)

Script37.addField(field40)
field41 = fieldObject()
field41.setType(fieldObject.TYPE_MFVEC3F)
field41.setName("keyValue")
field41.setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY)

Script37.addField(field41)

Script37.setSourceCode("\n"+
"\n"+
"ecmascript:\n"+
"		function set_location(value) {\n"+
"                    old = translation;\n"+
"		    translation = new SFVec3f(Math.random()*10-5, Math.random()*10-5, Math.random()*10-5);\n"+
"                    keyValue = new MFVec3f(old, translation);\n"+
"		    // Browser.println(translation);\n"+
"		}\n"+
"")
Transform29.addChild(Script37)
TimeSensor42 = TimeSensorObject()
TimeSensor42.setDEF("CL1")
TimeSensor42.setCycleInterval(3)
TimeSensor42.setLoop(True)

Transform29.addChild(TimeSensor42)
ROUTE43 = ROUTEObject()
ROUTE43.setFromNode("CL1")
ROUTE43.setFromField("cycleTime")
ROUTE43.setToNode("MB1")
ROUTE43.setToField("set_location")

Transform29.addChild(ROUTE43)
ROUTE44 = ROUTEObject()
ROUTE44.setFromNode("CL1")
ROUTE44.setFromField("fraction_changed")
ROUTE44.setToNode("PI1")
ROUTE44.setToField("set_fraction")

Transform29.addChild(ROUTE44)
ROUTE45 = ROUTEObject()
ROUTE45.setFromNode("MB1")
ROUTE45.setFromField("keyValue")
ROUTE45.setToNode("PI1")
ROUTE45.setToField("keyValue")

Transform29.addChild(ROUTE45)
ROUTE46 = ROUTEObject()
ROUTE46.setFromNode("PI1")
ROUTE46.setFromField("value_changed")
ROUTE46.setToNode("node")
ROUTE46.setToField("set_translation")

Transform29.addChild(ROUTE46)
ProtoBody28.addChild(Transform29)
ProtoDeclare25.setProtoBody(ProtoBody28)
Scene7.addChild(ProtoDeclare25)

Scene7.addComments(CommentsBlock("from doug sanden"))
ProtoDeclare47 = ProtoDeclareObject()
ProtoDeclare47.setName("x3dconnector")

ProtoInterface48 = ProtoInterfaceObject()

field49 = fieldObject()
field49.setType(fieldObject.TYPE_SFNODE)
field49.setName("startnode")
field49.setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY)

ProtoInterface48.addField(field49)
field50 = fieldObject()
field50.setType(fieldObject.TYPE_SFNODE)
field50.setName("endnode")
field50.setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY)

ProtoInterface48.addField(field50)
field51 = fieldObject()
field51.setType(fieldObject.TYPE_SFNODE)
field51.setName("connectornode")
field51.setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY)

ProtoInterface48.addField(field51)
field52 = fieldObject()
field52.setType(fieldObject.TYPE_SFVEC3F)
field52.setName("set_startpoint")
field52.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)

ProtoInterface48.addField(field52)
field53 = fieldObject()
field53.setType(fieldObject.TYPE_SFVEC3F)
field53.setName("set_endpoint")
field53.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)

ProtoInterface48.addField(field53)
ProtoDeclare47.setProtoInterface(ProtoInterface48)
ProtoBody54 = ProtoBodyObject()

Script55 = ScriptObject()
Script55.setDEF("S1")

field56 = fieldObject()
field56.setType(fieldObject.TYPE_SFNODE)
field56.setName("startnode")
field56.setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY)

Script55.addField(field56)
field57 = fieldObject()
field57.setType(fieldObject.TYPE_SFNODE)
field57.setName("endnode")
field57.setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY)

Script55.addField(field57)
field58 = fieldObject()
field58.setType(fieldObject.TYPE_SFNODE)
field58.setName("connectornode")
field58.setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY)

Script55.addField(field58)
field59 = fieldObject()
field59.setType(fieldObject.TYPE_SFVEC3F)
field59.setName("set_startpoint")
field59.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)

Script55.addField(field59)
field60 = fieldObject()
field60.setType(fieldObject.TYPE_SFVEC3F)
field60.setName("set_endpoint")
field60.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)

Script55.addField(field60)
IS61 = ISObject()

connect62 = connectObject()
connect62.setNodeField("startnode")
connect62.setProtoField("startnode")

IS61.addConnect(connect62)
connect63 = connectObject()
connect63.setNodeField("endnode")
connect63.setProtoField("endnode")

IS61.addConnect(connect63)
connect64 = connectObject()
connect64.setNodeField("connectornode")
connect64.setProtoField("connectornode")

IS61.addConnect(connect64)
connect65 = connectObject()
connect65.setNodeField("set_startpoint")
connect65.setProtoField("set_startpoint")

IS61.addConnect(connect65)
connect66 = connectObject()
connect66.setNodeField("set_endpoint")
connect66.setProtoField("set_endpoint")

IS61.addConnect(connect66)
Script55.setIS(IS61)

Script55.setSourceCode("\n"+
"            ecmascript:\n"+
"            function recompute(startpoint,endpoint) {\n"+
"	        if (typeof endpoint === 'undefined') {\n"+
"			return;\n"+
"		}\n"+
"                var dif = endpoint.subtract(startpoint);\n"+
"                var dist = dif.length()*.5;\n"+
"                var dif2 = dif.multiply(.5);\n"+
"                var norm = dif.normalize();\n"+
"                var trans = startpoint.add(dif2);\n"+
"                connectornode.scale = new SFVec3f(1.0,dist,1.0);\n"+
"                connectornode.translation = trans;\n"+
"                connectornode.rotation = new SFRotation(new SFVec3f(0.0,1.0,0.0),norm);\n"+
"                //Browser.print('norm='+norm.toString());\n"+
"                //Browser.print('rotation='+rotation.toString());\n"+
"            }\n"+
"            function initialize(){\n"+
"                recompute(startnode.translation,endnode.translation);\n"+
"            }\n"+
"            function set_startpoint(val,t){\n"+
"                recompute(val,endnode.translation);\n"+
"            }\n"+
"            function set_endpoint(val,t){\n"+
"                recompute(startnode.translation,val);\n"+
"            }\n"+
"")
ProtoBody54.addChild(Script55)
ProtoDeclare47.setProtoBody(ProtoBody54)
Scene7.addChild(ProtoDeclare47)
ProtoInstance67 = ProtoInstanceObject()
ProtoInstance67.setName("point")
ProtoInstance67.setDEF("start")

Scene7.addChild(ProtoInstance67)
ProtoInstance68 = ProtoInstanceObject()
ProtoInstance68.setName("point")
ProtoInstance68.setDEF("end1")

Scene7.addChild(ProtoInstance68)
ProtoInstance69 = ProtoInstanceObject()
ProtoInstance69.setName("point")
ProtoInstance69.setDEF("end2")

Scene7.addChild(ProtoInstance69)
ProtoInstance70 = ProtoInstanceObject()
ProtoInstance70.setName("point")
ProtoInstance70.setDEF("end3")

Scene7.addChild(ProtoInstance70)
ProtoInstance71 = ProtoInstanceObject()
ProtoInstance71.setName("x3dconnector")
ProtoInstance71.setDEF("connector1")

fieldValue72 = fieldValueObject()
fieldValue72.setName("startnode")

ProtoInstance73 = ProtoInstanceObject()
ProtoInstance73.setName("point")
ProtoInstance73.setUSE("start")

fieldValue72.addChild(ProtoInstance73)
ProtoInstance71.addFieldValue(fieldValue72)
fieldValue74 = fieldValueObject()
fieldValue74.setName("endnode")

ProtoInstance75 = ProtoInstanceObject()
ProtoInstance75.setName("point")
ProtoInstance75.setUSE("end1")

fieldValue74.addChild(ProtoInstance75)
ProtoInstance71.addFieldValue(fieldValue74)
fieldValue76 = fieldValueObject()
fieldValue76.setName("connectornode")

Transform77 = TransformObject()
Transform77.setUSE("cylinder1")

fieldValue76.addChild(Transform77)
ProtoInstance71.addFieldValue(fieldValue76)
Scene7.addChild(ProtoInstance71)
ProtoInstance78 = ProtoInstanceObject()
ProtoInstance78.setName("x3dconnector")
ProtoInstance78.setDEF("connector2")

fieldValue79 = fieldValueObject()
fieldValue79.setName("startnode")

ProtoInstance80 = ProtoInstanceObject()
ProtoInstance80.setName("point")
ProtoInstance80.setUSE("start")

fieldValue79.addChild(ProtoInstance80)
ProtoInstance78.addFieldValue(fieldValue79)
fieldValue81 = fieldValueObject()
fieldValue81.setName("endnode")

ProtoInstance82 = ProtoInstanceObject()
ProtoInstance82.setName("point")
ProtoInstance82.setUSE("end2")

fieldValue81.addChild(ProtoInstance82)
ProtoInstance78.addFieldValue(fieldValue81)
fieldValue83 = fieldValueObject()
fieldValue83.setName("connectornode")

Transform84 = TransformObject()
Transform84.setUSE("cylinder2")

fieldValue83.addChild(Transform84)
ProtoInstance78.addFieldValue(fieldValue83)
Scene7.addChild(ProtoInstance78)
ProtoInstance85 = ProtoInstanceObject()
ProtoInstance85.setName("x3dconnector")
ProtoInstance85.setDEF("connector3")

fieldValue86 = fieldValueObject()
fieldValue86.setName("startnode")

ProtoInstance87 = ProtoInstanceObject()
ProtoInstance87.setName("point")
ProtoInstance87.setUSE("start")

fieldValue86.addChild(ProtoInstance87)
ProtoInstance85.addFieldValue(fieldValue86)
fieldValue88 = fieldValueObject()
fieldValue88.setName("endnode")

ProtoInstance89 = ProtoInstanceObject()
ProtoInstance89.setName("point")
ProtoInstance89.setUSE("end3")

fieldValue88.addChild(ProtoInstance89)
ProtoInstance85.addFieldValue(fieldValue88)
fieldValue90 = fieldValueObject()
fieldValue90.setName("connectornode")

Transform91 = TransformObject()
Transform91.setUSE("cylinder3")

fieldValue90.addChild(Transform91)
ProtoInstance85.addFieldValue(fieldValue90)
Scene7.addChild(ProtoInstance85)
ROUTE92 = ROUTEObject()
ROUTE92.setFromNode("start")
ROUTE92.setFromField("translation")
ROUTE92.setToNode("connector1")
ROUTE92.setToField("set_startpoint")

Scene7.addChild(ROUTE92)
ROUTE93 = ROUTEObject()
ROUTE93.setFromNode("end1")
ROUTE93.setFromField("translation")
ROUTE93.setToNode("connector1")
ROUTE93.setToField("set_endpoint")

Scene7.addChild(ROUTE93)
ROUTE94 = ROUTEObject()
ROUTE94.setFromNode("start")
ROUTE94.setFromField("translation")
ROUTE94.setToNode("connector2")
ROUTE94.setToField("set_startpoint")

Scene7.addChild(ROUTE94)
ROUTE95 = ROUTEObject()
ROUTE95.setFromNode("end2")
ROUTE95.setFromField("translation")
ROUTE95.setToNode("connector2")
ROUTE95.setToField("set_endpoint")

Scene7.addChild(ROUTE95)
ROUTE96 = ROUTEObject()
ROUTE96.setFromNode("start")
ROUTE96.setFromField("translation")
ROUTE96.setToNode("connector3")
ROUTE96.setToField("set_startpoint")

Scene7.addChild(ROUTE96)
ROUTE97 = ROUTEObject()
ROUTE97.setFromNode("end3")
ROUTE97.setFromField("translation")
ROUTE97.setToNode("connector3")
ROUTE97.setToField("set_endpoint")

Scene7.addChild(ROUTE97)
X3D0.setScene(Scene7)

X3D0.toFileX3D("./arc.new.x3d")
