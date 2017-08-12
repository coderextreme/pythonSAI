# -*- coding: UTF-8 -*-
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

Sphere17 = SphereObject()

Shape16.setGeometry(Sphere17)
Appearance18 = AppearanceObject()

Material19 = MaterialObject()
Material19.setDiffuseColor([1,0,0])

Appearance18.setMaterial(Material19)
Shape16.setAppearance(Appearance18)
Transform13.addChild(Shape16)
Transform20 = TransformObject()
Transform20.setTranslation([1,0,0])

Shape21 = ShapeObject()

Text22 = TextObject()
Text22.setString(["Node"])

FontStyle23 = FontStyleObject()
FontStyle23.setJustify(["MIDDLE","MIDDLE"])
FontStyle23.setSize(5)

Text22.setFontStyle(FontStyle23)
Shape21.setGeometry(Text22)
Appearance24 = AppearanceObject()

Material25 = MaterialObject()
Material25.setDiffuseColor([0,0,1])

Appearance24.setMaterial(Material25)
Shape21.setAppearance(Appearance24)
Transform20.addChild(Shape21)
Transform13.addChild(Transform20)
ProtoBody12.addChild(Transform13)
PositionInterpolator26 = PositionInterpolatorObject()
PositionInterpolator26.setDEF("NodePosition")
PositionInterpolator26.setKey([0,1])
PositionInterpolator26.setKeyValue([0,0,0,0,5,0])

ProtoBody12.addChild(PositionInterpolator26)
Script27 = ScriptObject()
Script27.setDEF("MoveBall")

field28 = fieldObject()
field28.setType(fieldObject.TYPE_SFVEC3F)
field28.setName("translation")
field28.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field28.setValue("50 50 0")

Script27.addField(field28)
field29 = fieldObject()
field29.setType(fieldObject.TYPE_SFVEC3F)
field29.setName("old")
field29.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field29.setValue("0 0 0")

Script27.addField(field29)
field30 = fieldObject()
field30.setType(fieldObject.TYPE_SFTIME)
field30.setName("set_cycle")
field30.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)

Script27.addField(field30)
field31 = fieldObject()
field31.setType(fieldObject.TYPE_MFVEC3F)
field31.setName("keyValue")
field31.setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY)

Script27.addField(field31)

Script27.setSourceCode("\n"+
"\n"+
"ecmascript:\n"+
"					function set_cycle(value) {\n"+
"                                                old = translation;\n"+
"						translation = new SFVec3f(Math.random()*100-50, Math.random()*100-50, Math.random()*100-50);\n"+
"                                                keyValue = new MFVec3f(old, translation);\n"+
"						// Browser.println(translation);\n"+
"					}\n"+
"")
ProtoBody12.addChild(Script27)
TimeSensor32 = TimeSensorObject()
TimeSensor32.setDEF("nodeClock")
TimeSensor32.setCycleInterval(3)
TimeSensor32.setLoop(True)

ProtoBody12.addChild(TimeSensor32)
ROUTE33 = ROUTEObject()
ROUTE33.setFromNode("nodeClock")
ROUTE33.setFromField("cycleTime")
ROUTE33.setToNode("MoveBall")
ROUTE33.setToField("set_cycle")

ProtoBody12.addChild(ROUTE33)
ROUTE34 = ROUTEObject()
ROUTE34.setFromNode("nodeClock")
ROUTE34.setFromField("fraction_changed")
ROUTE34.setToNode("NodePosition")
ROUTE34.setToField("set_fraction")

ProtoBody12.addChild(ROUTE34)
ROUTE35 = ROUTEObject()
ROUTE35.setFromNode("MoveBall")
ROUTE35.setFromField("keyValue")
ROUTE35.setToNode("NodePosition")
ROUTE35.setToField("keyValue")

ProtoBody12.addChild(ROUTE35)
ROUTE36 = ROUTEObject()
ROUTE36.setFromNode("NodePosition")
ROUTE36.setFromField("value_changed")
ROUTE36.setToNode("transform")
ROUTE36.setToField("set_translation")

ProtoBody12.addChild(ROUTE36)
ProtoDeclare9.setProtoBody(ProtoBody12)
Scene8.addChild(ProtoDeclare9)
ProtoDeclare37 = ProtoDeclareObject()
ProtoDeclare37.setName("cylinder")

ProtoInterface38 = ProtoInterfaceObject()

field39 = fieldObject()
field39.setType(fieldObject.TYPE_SFVEC3F)
field39.setName("set_positionA")
field39.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)

ProtoInterface38.addField(field39)
field40 = fieldObject()
field40.setType(fieldObject.TYPE_SFVEC3F)
field40.setName("set_positionB")
field40.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)

ProtoInterface38.addField(field40)
ProtoDeclare37.setProtoInterface(ProtoInterface38)
ProtoBody41 = ProtoBodyObject()

Shape42 = ShapeObject()

Extrusion43 = ExtrusionObject()
Extrusion43.setDEF("extrusion")
Extrusion43.setCreaseAngle(0.785)
Extrusion43.setCrossSection([1,0,0.92,-0.38,0.71,-0.71,0.38,-0.92,0,-1,-0.38,-0.92,-0.71,-0.71,-0.92,-0.38,-1,0,-0.92,0.38,-0.71,0.71,-0.38,0.92,0,1,0.38,0.92,0.71,0.71,0.92,0.38,1,0])
Extrusion43.setSpine([0,-50,0,0,50,0])

Shape42.setGeometry(Extrusion43)
Appearance44 = AppearanceObject()

Material45 = MaterialObject()
Material45.setDiffuseColor([0,1,0])

Appearance44.setMaterial(Material45)
Shape42.setAppearance(Appearance44)
ProtoBody41.addChild(Shape42)
Script46 = ScriptObject()
Script46.setDEF("MoveCylinder")

field47 = fieldObject()
field47.setType(fieldObject.TYPE_MFVEC3F)
field47.setName("spine")
field47.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field47.setValue("0 -50 0 0 50 0")

Script46.addField(field47)
field48 = fieldObject()
field48.setType(fieldObject.TYPE_SFVEC3F)
field48.setName("set_endA")
field48.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)

Script46.addField(field48)
field49 = fieldObject()
field49.setType(fieldObject.TYPE_SFVEC3F)
field49.setName("set_endB")
field49.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)

Script46.addField(field49)
IS50 = ISObject()

connect51 = connectObject()
connect51.setNodeField("set_endA")
connect51.setProtoField("set_positionA")

IS50.addConnect(connect51)
connect52 = connectObject()
connect52.setNodeField("set_endB")
connect52.setProtoField("set_positionB")

IS50.addConnect(connect52)
Script46.setIS(IS50)

Script46.setSourceCode("\n"+
"\n"+
"ecmascript:\n"+
"\n"+
"                function set_endA(value) {\n"+
"		    if (typeof spine === 'undefined') {\n"+
"		        spine = new MFVec3f(value, value);\n"+
"		    } else {\n"+
"		        spine = new MFVec3f(value, spine[1]);\n"+
"		    }\n"+
"                }\n"+
"                \n"+
"                function set_endB(value) {\n"+
"		    if (typeof spine === 'undefined') {\n"+
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
ProtoBody41.addChild(Script46)
ROUTE53 = ROUTEObject()
ROUTE53.setFromNode("MoveCylinder")
ROUTE53.setFromField("spine")
ROUTE53.setToNode("extrusion")
ROUTE53.setToField("set_spine")

ProtoBody41.addChild(ROUTE53)
ProtoDeclare37.setProtoBody(ProtoBody41)
Scene8.addChild(ProtoDeclare37)
Transform54 = TransformObject()
Transform54.setDEF("HoldsContent")
Transform54.setScale([0.1,0.1,0.1])

PlaneSensor55 = PlaneSensorObject()
PlaneSensor55.setDEF("clickGenerator")
PlaneSensor55.setMinPosition([-50,-50])
PlaneSensor55.setMaxPosition([50,50])
PlaneSensor55.setDescription("click on background to add nodes, click on nodes to add links")

Transform54.addChild(PlaneSensor55)
ProtoInstance56 = ProtoInstanceObject()
ProtoInstance56.setName("node")
ProtoInstance56.setDEF("nodeA")

fieldValue57 = fieldValueObject()
fieldValue57.setName("position")
fieldValue57.setValue("0 0 0")

ProtoInstance56.addFieldValue(fieldValue57)
Transform54.addChild(ProtoInstance56)
ProtoInstance58 = ProtoInstanceObject()
ProtoInstance58.setName("node")
ProtoInstance58.setDEF("nodeB")

fieldValue59 = fieldValueObject()
fieldValue59.setName("position")
fieldValue59.setValue("50 50 50")

ProtoInstance58.addFieldValue(fieldValue59)
Transform54.addChild(ProtoInstance58)
ProtoInstance60 = ProtoInstanceObject()
ProtoInstance60.setName("node")
ProtoInstance60.setDEF("nodeC")

fieldValue61 = fieldValueObject()
fieldValue61.setName("position")
fieldValue61.setValue("-50 -50 -50")

ProtoInstance60.addFieldValue(fieldValue61)
Transform54.addChild(ProtoInstance60)
ProtoInstance62 = ProtoInstanceObject()
ProtoInstance62.setName("node")
ProtoInstance62.setDEF("nodeD")

fieldValue63 = fieldValueObject()
fieldValue63.setName("position")
fieldValue63.setValue("50 50 -50")

ProtoInstance62.addFieldValue(fieldValue63)
Transform54.addChild(ProtoInstance62)
ProtoInstance64 = ProtoInstanceObject()
ProtoInstance64.setName("cylinder")
ProtoInstance64.setDEF("linkA")

fieldValue65 = fieldValueObject()
fieldValue65.setName("set_positionA")
fieldValue65.setValue("0 0 0")

ProtoInstance64.addFieldValue(fieldValue65)
fieldValue66 = fieldValueObject()
fieldValue66.setName("set_positionB")
fieldValue66.setValue("50 50 50")

ProtoInstance64.addFieldValue(fieldValue66)
Transform54.addChild(ProtoInstance64)
ProtoInstance67 = ProtoInstanceObject()
ProtoInstance67.setName("cylinder")
ProtoInstance67.setDEF("linkB")

fieldValue68 = fieldValueObject()
fieldValue68.setName("set_positionA")
fieldValue68.setValue("0 0 0")

ProtoInstance67.addFieldValue(fieldValue68)
fieldValue69 = fieldValueObject()
fieldValue69.setName("set_positionB")
fieldValue69.setValue("-50 -50 -50")

ProtoInstance67.addFieldValue(fieldValue69)
Transform54.addChild(ProtoInstance67)
ProtoInstance70 = ProtoInstanceObject()
ProtoInstance70.setName("cylinder")
ProtoInstance70.setDEF("linkC")

fieldValue71 = fieldValueObject()
fieldValue71.setName("set_positionA")
fieldValue71.setValue("50 50 50")

ProtoInstance70.addFieldValue(fieldValue71)
fieldValue72 = fieldValueObject()
fieldValue72.setName("set_positionB")
fieldValue72.setValue("50 50 -50")

ProtoInstance70.addFieldValue(fieldValue72)
Transform54.addChild(ProtoInstance70)
Scene8.addChild(Transform54)
Script73 = ScriptObject()
Script73.setDEF("clickHandler")

field74 = fieldObject()
field74.setType(fieldObject.TYPE_SFINT32)
field74.setName("counter")
field74.setAccessType(fieldObject.ACCESSTYPE_INPUTOUTPUT)
field74.setValue("0")

Script73.addField(field74)
field75 = fieldObject()
field75.setType(fieldObject.TYPE_SFNODE)
field75.setName("node_changed")
field75.setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY)

Script73.addField(field75)
field76 = fieldObject()
field76.setType(fieldObject.TYPE_SFBOOL)
field76.setName("add_node")
field76.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)
field76.setValue("false")

Script73.addField(field76)
field77 = fieldObject()
field77.setType(fieldObject.TYPE_SFNODE)
field77.setName("ModifiableNode")
field77.setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY)

Transform78 = TransformObject()
Transform78.setUSE("HoldsContent")

field77.addChild(Transform78)
Script73.addField(field77)

Script73.setSourceCode("\n"+
"	\n"+
"ecmascript:\n"+
"	function add_node(value) {\n"+
"                // Browser.print('hey ', counter);\n"+
"                counter = counter++;\n"+
"		Browser.appendTo(Browser.getDocument().getElementById(\"MN\"),\n"+
"			{ \"ProtoInstance\":\n"+
"				{ \"@name\":\"node\",\n"+
"				  \"@DEF\":\"node'+counter+'\",\n"+
"				  \"fieldValue\": [\n"+
"					{\n"+
"						 \"@name\":\"position\",\n"+
"						 \"@value\":[0.0,0.0,0.0]\n"+
"					}\n"+
"				  ]\n"+
"				}\n"+
"			});\n"+
"                \n"+
"        }\n"+
"")
Scene8.addChild(Script73)
ROUTE79 = ROUTEObject()
ROUTE79.setFromNode("clickGenerator")
ROUTE79.setFromField("isActive")
ROUTE79.setToNode("clickHandler")
ROUTE79.setToField("add_node")

Scene8.addChild(ROUTE79)
ROUTE80 = ROUTEObject()
ROUTE80.setFromNode("nodeA")
ROUTE80.setFromField("position")
ROUTE80.setToNode("linkA")
ROUTE80.setToField("set_positionA")

Scene8.addChild(ROUTE80)
ROUTE81 = ROUTEObject()
ROUTE81.setFromNode("nodeB")
ROUTE81.setFromField("position")
ROUTE81.setToNode("linkA")
ROUTE81.setToField("set_positionB")

Scene8.addChild(ROUTE81)
ROUTE82 = ROUTEObject()
ROUTE82.setFromNode("nodeA")
ROUTE82.setFromField("position")
ROUTE82.setToNode("linkB")
ROUTE82.setToField("set_positionA")

Scene8.addChild(ROUTE82)
ROUTE83 = ROUTEObject()
ROUTE83.setFromNode("nodeC")
ROUTE83.setFromField("position")
ROUTE83.setToNode("linkB")
ROUTE83.setToField("set_positionB")

Scene8.addChild(ROUTE83)
ROUTE84 = ROUTEObject()
ROUTE84.setFromNode("nodeA")
ROUTE84.setFromField("position")
ROUTE84.setToNode("linkC")
ROUTE84.setToField("set_positionA")

Scene8.addChild(ROUTE84)
ROUTE85 = ROUTEObject()
ROUTE85.setFromNode("nodeD")
ROUTE85.setFromField("position")
ROUTE85.setToNode("linkC")
ROUTE85.setToField("set_positionB")

Scene8.addChild(ROUTE85)
X3D0.setScene(Scene8)

X3D0.toFileX3D("./force.new.x3d")
