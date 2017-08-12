# -*- coding: UTF-8 -*-
from jnius import autoclass
from X3Dautoclass import *
X3D0 =  X3DObject()
X3D0.setProfile("Immersive")
X3D0.setVersion("3.3")

head1 = headObject()

meta2 = metaObject()
meta2.setName("title")
meta2.setContent("x3dconnectorProto")

head1.addMeta(meta2)
meta3 = metaObject()
meta3.setName("creator")
meta3.setContent("Lost, Doug Sanden I think")

head1.addMeta(meta3)
meta4 = metaObject()
meta4.setName("generator")
meta4.setContent("manual")

head1.addMeta(meta4)
meta5 = metaObject()
meta5.setName("identifier")
meta5.setContent("http://coderextreme.net/X3DJSONLD/x3dconnectorProto.x3d")

head1.addMeta(meta5)
meta6 = metaObject()
meta6.setName("description")
meta6.setContent("a generic proto to connect two objects")

head1.addMeta(meta6)
X3D0.setHead(head1)
Scene7 = SceneObject()

Viewpoint8 = ViewpointObject()
Viewpoint8.setPosition([0,0,5])
Viewpoint8.setDescription("Only Viewpoint")

Scene7.addChild(Viewpoint8)
Background9 = BackgroundObject()
Background9.setSkyColor([0.4,0.4,0.4])

Scene7.addChild(Background9)
Transform10 = TransformObject()
Transform10.setDEF("G1")

Shape11 = ShapeObject()

Appearance12 = AppearanceObject()

Material13 = MaterialObject()
Material13.setDiffuseColor([0.7,0.2,0.2])

Appearance12.setMaterial(Material13)
Shape11.setAppearance(Appearance12)
Sphere14 = SphereObject()
Sphere14.setRadius(0.1)

Shape11.setGeometry(Sphere14)
Transform10.addChild(Shape11)
PlaneSensor15 = PlaneSensorObject()
PlaneSensor15.setDescription("Grab to move")
PlaneSensor15.setDEF("PS1")

Transform10.addChild(PlaneSensor15)
ROUTE16 = ROUTEObject()
ROUTE16.setFromNode("PS1")
ROUTE16.setFromField("translation_changed")
ROUTE16.setToNode("G1")
ROUTE16.setToField("set_translation")

Transform10.addChild(ROUTE16)
Scene7.addChild(Transform10)
Transform17 = TransformObject()
Transform17.setDEF("G2")
Transform17.setTranslation([1,-1,0.01])

Shape18 = ShapeObject()

Appearance19 = AppearanceObject()

Material20 = MaterialObject()
Material20.setDiffuseColor([0.2,0.7,0.2])

Appearance19.setMaterial(Material20)
Shape18.setAppearance(Appearance19)
Sphere21 = SphereObject()
Sphere21.setRadius(0.1)

Shape18.setGeometry(Sphere21)
Transform17.addChild(Shape18)
PlaneSensor22 = PlaneSensorObject()
PlaneSensor22.setDescription("Grab to move")
PlaneSensor22.setDEF("PS2")

Transform17.addChild(PlaneSensor22)
ROUTE23 = ROUTEObject()
ROUTE23.setFromNode("PS2")
ROUTE23.setFromField("translation_changed")
ROUTE23.setToNode("G2")
ROUTE23.setToField("set_translation")

Transform17.addChild(ROUTE23)
Scene7.addChild(Transform17)
Transform24 = TransformObject()
Transform24.setDEF("G3")
Transform24.setTranslation([1,1,0.01])

Shape25 = ShapeObject()

Appearance26 = AppearanceObject()

Material27 = MaterialObject()
Material27.setDiffuseColor([0.2,0.7,0.2])

Appearance26.setMaterial(Material27)
Shape25.setAppearance(Appearance26)
Sphere28 = SphereObject()
Sphere28.setRadius(0.1)

Shape25.setGeometry(Sphere28)
Transform24.addChild(Shape25)
PlaneSensor29 = PlaneSensorObject()
PlaneSensor29.setDescription("Grab to move")
PlaneSensor29.setDEF("PS3")

Transform24.addChild(PlaneSensor29)
ROUTE30 = ROUTEObject()
ROUTE30.setFromNode("PS3")
ROUTE30.setFromField("translation_changed")
ROUTE30.setToNode("G3")
ROUTE30.setToField("set_translation")

Transform24.addChild(ROUTE30)
Scene7.addChild(Transform24)
Transform31 = TransformObject()
Transform31.setDEF("G4")
Transform31.setTranslation([-1,1,0.01])

Shape32 = ShapeObject()

Appearance33 = AppearanceObject()

Material34 = MaterialObject()
Material34.setDiffuseColor([0.2,0.7,0.2])

Appearance33.setMaterial(Material34)
Shape32.setAppearance(Appearance33)
Sphere35 = SphereObject()
Sphere35.setRadius(0.1)

Shape32.setGeometry(Sphere35)
Transform31.addChild(Shape32)
PlaneSensor36 = PlaneSensorObject()
PlaneSensor36.setDescription("Grab to move")
PlaneSensor36.setDEF("PS4")

Transform31.addChild(PlaneSensor36)
ROUTE37 = ROUTEObject()
ROUTE37.setFromNode("PS4")
ROUTE37.setFromField("translation_changed")
ROUTE37.setToNode("G4")
ROUTE37.setToField("set_translation")

Transform31.addChild(ROUTE37)
Scene7.addChild(Transform31)
Transform38 = TransformObject()
Transform38.setDEF("C1")

Shape39 = ShapeObject()

Appearance40 = AppearanceObject()

Material41 = MaterialObject()
Material41.setDiffuseColor([0.2,0.7,0.7])
Material41.setTransparency(0.5)

Appearance40.setMaterial(Material41)
Shape39.setAppearance(Appearance40)
Cylinder42 = CylinderObject()
Cylinder42.setRadius(0.05)

Shape39.setGeometry(Cylinder42)
Transform38.addChild(Shape39)
Scene7.addChild(Transform38)
Transform43 = TransformObject()
Transform43.setDEF("C2")

Shape44 = ShapeObject()

Appearance45 = AppearanceObject()

Material46 = MaterialObject()
Material46.setDiffuseColor([0.2,0.7,0.7])
Material46.setTransparency(0.5)

Appearance45.setMaterial(Material46)
Shape44.setAppearance(Appearance45)
Cylinder47 = CylinderObject()
Cylinder47.setRadius(0.05)

Shape44.setGeometry(Cylinder47)
Transform43.addChild(Shape44)
Scene7.addChild(Transform43)
Transform48 = TransformObject()
Transform48.setDEF("C3")

Shape49 = ShapeObject()

Appearance50 = AppearanceObject()

Material51 = MaterialObject()
Material51.setDiffuseColor([0.2,0.7,0.7])
Material51.setTransparency(0.5)

Appearance50.setMaterial(Material51)
Shape49.setAppearance(Appearance50)
Cylinder52 = CylinderObject()
Cylinder52.setRadius(0.05)

Shape49.setGeometry(Cylinder52)
Transform48.addChild(Shape49)
Scene7.addChild(Transform48)
ProtoDeclare53 = ProtoDeclareObject()
ProtoDeclare53.setName("x3dconnector")

ProtoInterface54 = ProtoInterfaceObject()

field55 = fieldObject()
field55.setType(fieldObject.TYPE_SFNODE)
field55.setName("startnode")
field55.setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY)

ProtoInterface54.addField(field55)
field56 = fieldObject()
field56.setType(fieldObject.TYPE_SFNODE)
field56.setName("endnode")
field56.setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY)

ProtoInterface54.addField(field56)
field57 = fieldObject()
field57.setType(fieldObject.TYPE_SFNODE)
field57.setName("connectornode")
field57.setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY)

ProtoInterface54.addField(field57)
field58 = fieldObject()
field58.setType(fieldObject.TYPE_SFVEC3F)
field58.setName("set_startpoint")
field58.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)

ProtoInterface54.addField(field58)
field59 = fieldObject()
field59.setType(fieldObject.TYPE_SFVEC3F)
field59.setName("set_endpoint")
field59.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)

ProtoInterface54.addField(field59)
ProtoDeclare53.setProtoInterface(ProtoInterface54)
ProtoBody60 = ProtoBodyObject()

Script61 = ScriptObject()
Script61.setDEF("S1")

field62 = fieldObject()
field62.setType(fieldObject.TYPE_SFNODE)
field62.setName("startnode")
field62.setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY)

Script61.addField(field62)
field63 = fieldObject()
field63.setType(fieldObject.TYPE_SFNODE)
field63.setName("endnode")
field63.setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY)

Script61.addField(field63)
field64 = fieldObject()
field64.setType(fieldObject.TYPE_SFNODE)
field64.setName("connectornode")
field64.setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY)

Script61.addField(field64)
field65 = fieldObject()
field65.setType(fieldObject.TYPE_SFVEC3F)
field65.setName("set_startpoint")
field65.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)

Script61.addField(field65)
field66 = fieldObject()
field66.setType(fieldObject.TYPE_SFVEC3F)
field66.setName("set_endpoint")
field66.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)

Script61.addField(field66)
IS67 = ISObject()

connect68 = connectObject()
connect68.setNodeField("startnode")
connect68.setProtoField("startnode")

IS67.addConnect(connect68)
connect69 = connectObject()
connect69.setNodeField("endnode")
connect69.setProtoField("endnode")

IS67.addConnect(connect69)
connect70 = connectObject()
connect70.setNodeField("connectornode")
connect70.setProtoField("connectornode")

IS67.addConnect(connect70)
connect71 = connectObject()
connect71.setNodeField("set_startpoint")
connect71.setProtoField("set_startpoint")

IS67.addConnect(connect71)
connect72 = connectObject()
connect72.setNodeField("set_endpoint")
connect72.setProtoField("set_endpoint")

IS67.addConnect(connect72)
Script61.setIS(IS67)

Script61.setSourceCode("\n"+
"            ecmascript:\n"+
"            function recompute(startpoint,endpoint){\n"+
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
ProtoBody60.addChild(Script61)
ProtoDeclare53.setProtoBody(ProtoBody60)
Scene7.addChild(ProtoDeclare53)
ProtoInstance73 = ProtoInstanceObject()
ProtoInstance73.setName("x3dconnector")
ProtoInstance73.setDEF("connector1")

fieldValue74 = fieldValueObject()
fieldValue74.setName("startnode")

Transform75 = TransformObject()
Transform75.setUSE("G1")

fieldValue74.addChild(Transform75)
ProtoInstance73.addFieldValue(fieldValue74)
fieldValue76 = fieldValueObject()
fieldValue76.setName("endnode")

Transform77 = TransformObject()
Transform77.setUSE("G2")

fieldValue76.addChild(Transform77)
ProtoInstance73.addFieldValue(fieldValue76)
fieldValue78 = fieldValueObject()
fieldValue78.setName("connectornode")

Transform79 = TransformObject()
Transform79.setUSE("C1")

fieldValue78.addChild(Transform79)
ProtoInstance73.addFieldValue(fieldValue78)
Scene7.addChild(ProtoInstance73)
ProtoInstance80 = ProtoInstanceObject()
ProtoInstance80.setName("x3dconnector")
ProtoInstance80.setDEF("connector2")

fieldValue81 = fieldValueObject()
fieldValue81.setName("startnode")

Transform82 = TransformObject()
Transform82.setUSE("G1")

fieldValue81.addChild(Transform82)
ProtoInstance80.addFieldValue(fieldValue81)
fieldValue83 = fieldValueObject()
fieldValue83.setName("endnode")

Transform84 = TransformObject()
Transform84.setUSE("G3")

fieldValue83.addChild(Transform84)
ProtoInstance80.addFieldValue(fieldValue83)
fieldValue85 = fieldValueObject()
fieldValue85.setName("connectornode")

Transform86 = TransformObject()
Transform86.setUSE("C2")

fieldValue85.addChild(Transform86)
ProtoInstance80.addFieldValue(fieldValue85)
Scene7.addChild(ProtoInstance80)
ProtoInstance87 = ProtoInstanceObject()
ProtoInstance87.setName("x3dconnector")
ProtoInstance87.setDEF("connector3")

fieldValue88 = fieldValueObject()
fieldValue88.setName("startnode")

Transform89 = TransformObject()
Transform89.setUSE("G1")

fieldValue88.addChild(Transform89)
ProtoInstance87.addFieldValue(fieldValue88)
fieldValue90 = fieldValueObject()
fieldValue90.setName("endnode")

Transform91 = TransformObject()
Transform91.setUSE("G4")

fieldValue90.addChild(Transform91)
ProtoInstance87.addFieldValue(fieldValue90)
fieldValue92 = fieldValueObject()
fieldValue92.setName("connectornode")

Transform93 = TransformObject()
Transform93.setUSE("C3")

fieldValue92.addChild(Transform93)
ProtoInstance87.addFieldValue(fieldValue92)
Scene7.addChild(ProtoInstance87)
ROUTE94 = ROUTEObject()
ROUTE94.setFromNode("G1")
ROUTE94.setFromField("translation_changed")
ROUTE94.setToNode("connector1")
ROUTE94.setToField("set_startpoint")

Scene7.addChild(ROUTE94)
ROUTE95 = ROUTEObject()
ROUTE95.setFromNode("G2")
ROUTE95.setFromField("translation_changed")
ROUTE95.setToNode("connector1")
ROUTE95.setToField("set_endpoint")

Scene7.addChild(ROUTE95)
ROUTE96 = ROUTEObject()
ROUTE96.setFromNode("G1")
ROUTE96.setFromField("translation_changed")
ROUTE96.setToNode("connector2")
ROUTE96.setToField("set_startpoint")

Scene7.addChild(ROUTE96)
ROUTE97 = ROUTEObject()
ROUTE97.setFromNode("G3")
ROUTE97.setFromField("translation_changed")
ROUTE97.setToNode("connector2")
ROUTE97.setToField("set_endpoint")

Scene7.addChild(ROUTE97)
ROUTE98 = ROUTEObject()
ROUTE98.setFromNode("G1")
ROUTE98.setFromField("translation_changed")
ROUTE98.setToNode("connector3")
ROUTE98.setToField("set_startpoint")

Scene7.addChild(ROUTE98)
ROUTE99 = ROUTEObject()
ROUTE99.setFromNode("G4")
ROUTE99.setFromField("translation_changed")
ROUTE99.setToNode("connector3")
ROUTE99.setToField("set_endpoint")

Scene7.addChild(ROUTE99)
X3D0.setScene(Scene7)

X3D0.toFileX3D("./x3dconnectorProto.new.x3d")
