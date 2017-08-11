from jnius import autoclass
from X3Dautoclass import *
X3D0 =  X3DObject()
X3D0.setProfile("Immersive")
X3D0.setVersion("3.3")

head1 = headObject()

meta2 = metaObject()
meta2.setName("creator")
meta2.setContent("John W Carlson")

head1.addMeta(meta2)
meta3 = metaObject()
meta3.setName("created")
meta3.setContent("December 13 2015")

head1.addMeta(meta3)
meta4 = metaObject()
meta4.setName("title")
meta4.setContent("force.x3d")

head1.addMeta(meta4)
meta5 = metaObject()
meta5.setName("identifier")
meta5.setContent("http://coderextreme.net/X3DJSONLD/force.x3d")

head1.addMeta(meta5)
meta6 = metaObject()
meta6.setName("description")
meta6.setContent("beginnings of a force directed graph in 3D")

head1.addMeta(meta6)
meta7 = metaObject()
meta7.setName("generator")
meta7.setContent("Vim, X3D-Edit, https://savage.nps.edu/X3D-Edit")

head1.addMeta(meta7)
X3D0.setHead(head1)
Scene8 = SceneObject()

ProtoDeclare9 = ProtoDeclareObject()
ProtoDeclare9.setName("node")

ProtoInterface10 = ProtoInterfaceObject()

field11 = fieldObject()
field11.setType(fieldObject.TYPE_SFVEC3F)
field11.setName("position")
field11.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field11.setValue("0 0 0")

ProtoInterface10.addField(field11)
ProtoDeclare9.setProtoInterface(ProtoInterface10)
ProtoBody12 = ProtoBodyObject()

Transform13 = TransformObject()
Transform13.setDEF("transform")

IS14 = ISObject()

connect15 = connectObject()
connect15.setNodeField("translation")
connect15.setProtoField("position")

IS14.addConnect(connect15)
Transform13.setIS(IS14)
Shape16 = ShapeObject()


Shape16.addComments(CommentsBlock("comment before Sphere"))

Shape16.addComments(CommentsBlock("comment after Sphere"))

Shape16.addComments(CommentsBlock("comment after Appearance"))
Sphere17 = SphereObject()

Shape16.setGeometry(Sphere17)
Appearance18 = AppearanceObject()


Appearance18.addComments(CommentsBlock("comment before Material"))

Appearance18.addComments(CommentsBlock("comment after Material"))
Material19 = MaterialObject()
Material19.setDiffuseColor([1,0,0])

Appearance18.setMaterial(Material19)
Shape16.setAppearance(Appearance18)
Transform13.addChild(Shape16)
ProtoBody12.addChild(Transform13)
PositionInterpolator20 = PositionInterpolatorObject()
PositionInterpolator20.setDEF("NodePosition")
PositionInterpolator20.setKey([0,1])
PositionInterpolator20.setKeyValue([0,0,0,0,5,0])

ProtoBody12.addChild(PositionInterpolator20)
Script21 = ScriptObject()
Script21.setDEF("MoveBall")

field22 = fieldObject()
field22.setType(fieldObject.TYPE_SFVEC3F)
field22.setName("translation")
field22.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field22.setValue("50 50 0")

Script21.addField(field22)
field23 = fieldObject()
field23.setType(fieldObject.TYPE_SFVEC3F)
field23.setName("old")
field23.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field23.setValue("0 0 0")

Script21.addField(field23)
field24 = fieldObject()
field24.setType(fieldObject.TYPE_SFTIME)
field24.setName("set_cycle")
field24.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)

Script21.addField(field24)
field25 = fieldObject()
field25.setType(fieldObject.TYPE_MFVEC3F)
field25.setName("keyValue")
field25.setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY)

Script21.addField(field25)

Script21.setSourceCode("\n"+
"\n"+
"ecmascript:\n"+
"					function set_cycle(value) {\n"+
"                                                old = translation;\n"+
"						translation = new SFVec3f(Math.random()*100-50, Math.random()*100-50, Math.random()*100-50);\n"+
"                                                keyValue = new MFVec3f(old, translation);\n"+
"						// Browser.println(translation);\n"+
"					}\n"+
"")
ProtoBody12.addChild(Script21)
TimeSensor26 = TimeSensorObject()
TimeSensor26.setDEF("nodeClock")
TimeSensor26.setCycleInterval(3)
TimeSensor26.setLoop(True)

ProtoBody12.addChild(TimeSensor26)
ROUTE27 = ROUTEObject()
ROUTE27.setFromNode("nodeClock")
ROUTE27.setFromField("cycleTime")
ROUTE27.setToNode("MoveBall")
ROUTE27.setToField("set_cycle")

ProtoBody12.addChild(ROUTE27)
ROUTE28 = ROUTEObject()
ROUTE28.setFromNode("nodeClock")
ROUTE28.setFromField("fraction_changed")
ROUTE28.setToNode("NodePosition")
ROUTE28.setToField("set_fraction")

ProtoBody12.addChild(ROUTE28)
ROUTE29 = ROUTEObject()
ROUTE29.setFromNode("MoveBall")
ROUTE29.setFromField("keyValue")
ROUTE29.setToNode("NodePosition")
ROUTE29.setToField("keyValue")

ProtoBody12.addChild(ROUTE29)
ROUTE30 = ROUTEObject()
ROUTE30.setFromNode("NodePosition")
ROUTE30.setFromField("value_changed")
ROUTE30.setToNode("transform")
ROUTE30.setToField("set_translation")

ProtoBody12.addChild(ROUTE30)
ProtoDeclare9.setProtoBody(ProtoBody12)
Scene8.addChild(ProtoDeclare9)
ProtoDeclare31 = ProtoDeclareObject()
ProtoDeclare31.setName("cylinder")

ProtoInterface32 = ProtoInterfaceObject()

field33 = fieldObject()
field33.setType(fieldObject.TYPE_SFVEC3F)
field33.setName("positionA")
field33.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)

ProtoInterface32.addField(field33)
field34 = fieldObject()
field34.setType(fieldObject.TYPE_SFVEC3F)
field34.setName("positionB")
field34.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)

ProtoInterface32.addField(field34)
ProtoDeclare31.setProtoInterface(ProtoInterface32)
ProtoBody35 = ProtoBodyObject()

Shape36 = ShapeObject()

Extrusion37 = ExtrusionObject()
Extrusion37.setDEF("extrusion")
Extrusion37.setCreaseAngle(0.785)
Extrusion37.setCrossSection([1,0,0.92,-0.38,0.71,-0.71,0.38,-0.92,0,-1,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1,0,-0.92,0.38,-0.71,0.71,-0.38,0.92,0,1,0.38,0.92,0.71,0.71,0.92,0.38,1,0])
Extrusion37.setSpine([0,-50,0,0,0,0,0,50,0])

Shape36.setGeometry(Extrusion37)
Appearance38 = AppearanceObject()

Material39 = MaterialObject()
Material39.setDiffuseColor([0,1,0])

Appearance38.setMaterial(Material39)
Shape36.setAppearance(Appearance38)
ProtoBody35.addChild(Shape36)
Script40 = ScriptObject()
Script40.setDEF("MoveCylinder")

field41 = fieldObject()
field41.setType(fieldObject.TYPE_MFVEC3F)
field41.setName("spine")
field41.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field41.setValue("0 -50 0 0 0 0 0 50 0")

Script40.addField(field41)
field42 = fieldObject()
field42.setType(fieldObject.TYPE_SFVEC3F)
field42.setName("set_endA")
field42.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)

Script40.addField(field42)
field43 = fieldObject()
field43.setType(fieldObject.TYPE_SFVEC3F)
field43.setName("set_endB")
field43.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)

Script40.addField(field43)
IS44 = ISObject()

connect45 = connectObject()
connect45.setNodeField("set_endA")
connect45.setProtoField("positionA")

IS44.addConnect(connect45)
connect46 = connectObject()
connect46.setNodeField("set_endB")
connect46.setProtoField("positionB")

IS44.addConnect(connect46)
Script40.setIS(IS44)

Script40.setSourceCode("\n"+
"\n"+
"ecmascript:\n"+
"\n"+
"                function set_endA(value) {\n"+
"		    if (typeof spine === \"undefined\") {\n"+
"		        spine = new MFVec3f(value, value);\n"+
"		    } else {\n"+
"		        spine = new MFVec3f(value, spine[1]);\n"+
"		    }\n"+
"                }\n"+
"                \n"+
"                function set_endB(value) {\n"+
"		    if (typeof spine === \"undefined\") {\n"+
"		        spine = new MFVec3f(value, value);\n"+
"		    } else {\n"+
"		        spine = new MFVec3f(spine[0], value);\n"+
"		    }\n"+
"                }\n"+
"                \n"+
"                function set_spine(value) {\n"+
"                    spine = value;\n"+
"                }\n"+
"")
ProtoBody35.addChild(Script40)
ROUTE47 = ROUTEObject()
ROUTE47.setFromNode("MoveCylinder")
ROUTE47.setFromField("spine")
ROUTE47.setToNode("extrusion")
ROUTE47.setToField("set_spine")

ProtoBody35.addChild(ROUTE47)
ProtoDeclare31.setProtoBody(ProtoBody35)
Scene8.addChild(ProtoDeclare31)
Transform48 = TransformObject()
Transform48.setScale([0.1,0.1,0.1])

ProtoInstance49 = ProtoInstanceObject()
ProtoInstance49.setName("node")
ProtoInstance49.setDEF("nodeA")

fieldValue50 = fieldValueObject()
fieldValue50.setName("position")
fieldValue50.setValue("-50 -50 -50")

ProtoInstance49.addFieldValue(fieldValue50)
Transform48.addChild(ProtoInstance49)
ProtoInstance51 = ProtoInstanceObject()
ProtoInstance51.setName("node")
ProtoInstance51.setDEF("nodeB")

fieldValue52 = fieldValueObject()
fieldValue52.setName("position")
fieldValue52.setValue("50 50 50")

ProtoInstance51.addFieldValue(fieldValue52)
Transform48.addChild(ProtoInstance51)
ProtoInstance53 = ProtoInstanceObject()
ProtoInstance53.setName("cylinder")
ProtoInstance53.setDEF("linkA")

fieldValue54 = fieldValueObject()
fieldValue54.setName("positionA")
fieldValue54.setValue("0 0 0")

ProtoInstance53.addFieldValue(fieldValue54)
fieldValue55 = fieldValueObject()
fieldValue55.setName("positionB")
fieldValue55.setValue("50 50 50")

ProtoInstance53.addFieldValue(fieldValue55)
Transform48.addChild(ProtoInstance53)
Scene8.addChild(Transform48)
ROUTE56 = ROUTEObject()
ROUTE56.setFromNode("nodeA")
ROUTE56.setFromField("position")
ROUTE56.setToNode("linkA")
ROUTE56.setToField("positionA")

Scene8.addChild(ROUTE56)
ROUTE57 = ROUTEObject()
ROUTE57.setFromNode("nodeB")
ROUTE57.setFromField("position")
ROUTE57.setToNode("linkA")
ROUTE57.setToField("positionB")

Scene8.addChild(ROUTE57)
X3D0.setScene(Scene8)

X3D0.toFileX3D("./fors.new.x3d")
