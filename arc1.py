import x3dpsail
X3D0 = x3dpsail.X3D()
X3D0.setProfile("Immersive")
X3D0.setVersion("3.3")
head1 = x3dpsail.head()
meta2 = x3dpsail.meta()
meta2.setName("title")
meta2.setContent("x3dconnectorProto")

head1.addMeta(meta2)
meta3 = x3dpsail.meta()
meta3.setName("creator")
meta3.setContent("Lost, Doug Sanden I think")

head1.addMeta(meta3)
meta4 = x3dpsail.meta()
meta4.setName("generator")
meta4.setContent("manual")

head1.addMeta(meta4)
meta5 = x3dpsail.meta()
meta5.setName("identifier")
meta5.setContent("https://coderextreme.net/X3DJSONLD/x3dconnectorProto.x3d")

head1.addMeta(meta5)
meta6 = x3dpsail.meta()
meta6.setName("description")
meta6.setContent("a generic proto to connect two objects")

head1.addMeta(meta6)

X3D0.setHead(head1)
Scene7 = x3dpsail.Scene()
Viewpoint8 = x3dpsail.Viewpoint()
Viewpoint8.setPosition([0,0,5])
Viewpoint8.setDescription("Only Viewpoint")

Scene7.addChildren(Viewpoint8)
Background9 = x3dpsail.Background()
Background9.setSkyColor([0.4,0.4,0.4])

Scene7.addChildren(Background9)
ProtoDeclare10 = x3dpsail.ProtoDeclare()
ProtoDeclare10.setName("point")
ProtoInterface11 = x3dpsail.ProtoInterface()
field12 = x3dpsail.field()
field12.setName("translation")
field12.setAccessType("inputOutput")
field12.setType("SFVec3f")
field12.setValue("0 0 0")

ProtoInterface11.addField(field12)

ProtoDeclare10.setProtoInterface(ProtoInterface11)
ProtoBody13 = x3dpsail.ProtoBody()
Transform14 = x3dpsail.Transform()
Transform14.setDEF("node")
IS15 = x3dpsail.IS()
connect16 = x3dpsail.connect()
connect16.setNodeField("translation")
connect16.setProtoField("translation")

IS15.addConnect(connect16)

Transform14.setIS(IS15)
Shape17 = x3dpsail.Shape()
Sphere18 = x3dpsail.Sphere()
Sphere18.setRadius(0.1)

Shape17.setGeometry(Sphere18)
Appearance19 = x3dpsail.Appearance()
Material20 = x3dpsail.Material()
Material20.setDiffuseColor([1,0,0])

Appearance19.setMaterial(Material20)

Shape17.setAppearance(Appearance19)

Transform14.addChildren(Shape17)
PositionInterpolator21 = x3dpsail.PositionInterpolator()
PositionInterpolator21.setDEF("PI1")
PositionInterpolator21.setKey([0,1])
PositionInterpolator21.setKeyValue([0,0,0,0,5,0])

Transform14.addChildren(PositionInterpolator21)
Script22 = x3dpsail.Script()
Script22.setDEF("MB1")
field23 = x3dpsail.field()
field23.setName("translation")
field23.setAccessType("inputOutput")
field23.setType("SFVec3f")
field23.setValue("50 50 0")

Script22.addField(field23)
field24 = x3dpsail.field()
field24.setName("old")
field24.setAccessType("inputOutput")
field24.setType("SFVec3f")
field24.setValue("0 0 0")

Script22.addField(field24)
field25 = x3dpsail.field()
field25.setName("set_location")
field25.setAccessType("inputOnly")
field25.setType("SFTime")

Script22.addField(field25)
field26 = x3dpsail.field()
field26.setName("keyValue")
field26.setAccessType("inputOutput")
field26.setType("MFVec3f")
field26.setValue("0 0 0 0 5 0")

Script22.addField(field26)

Script22.setSourceCode('''ecmascript:\n"+
"		function set_location(value) {\n"+
"                    old = translation;\n"+
"		    translation = new SFVec3f(Math.random()*10-5, Math.random()*10-5, Math.random()*10-5);\n"+
"                    keyValue = new MFVec3f([old, translation]);\n"+
"		    // Browser.println(keyValue);\n"+
"		}''')

Transform14.addChildren(Script22)
TimeSensor27 = x3dpsail.TimeSensor()
TimeSensor27.setDEF("CL1")
TimeSensor27.setCycleInterval(3)
TimeSensor27.setLoop(True)

Transform14.addChildren(TimeSensor27)
ROUTE28 = x3dpsail.ROUTE()
ROUTE28.setFromNode("CL1")
ROUTE28.setFromField("cycleTime")
ROUTE28.setToNode("MB1")
ROUTE28.setToField("set_location")

Transform14.addChildren(ROUTE28)
ROUTE29 = x3dpsail.ROUTE()
ROUTE29.setFromNode("CL1")
ROUTE29.setFromField("fraction_changed")
ROUTE29.setToNode("PI1")
ROUTE29.setToField("set_fraction")

Transform14.addChildren(ROUTE29)
ROUTE30 = x3dpsail.ROUTE()
ROUTE30.setFromNode("MB1")
ROUTE30.setFromField("keyValue")
ROUTE30.setToNode("PI1")
ROUTE30.setToField("keyValue")

Transform14.addChildren(ROUTE30)
ROUTE31 = x3dpsail.ROUTE()
ROUTE31.setFromNode("PI1")
ROUTE31.setFromField("value_changed")
ROUTE31.setToNode("node")
ROUTE31.setToField("set_translation")

Transform14.addChildren(ROUTE31)

ProtoBody13.addChildren(Transform14)

ProtoDeclare10.setProtoBody(ProtoBody13)

Scene7.addChildren(ProtoDeclare10)
ProtoDeclare32 = x3dpsail.ProtoDeclare()
ProtoDeclare32.setName("x3dconnector")
ProtoInterface33 = x3dpsail.ProtoInterface()
field34 = x3dpsail.field()
field34.setName("startnode")
field34.setAccessType("initializeOnly")
field34.setType("SFNode")

ProtoInterface33.addField(field34)
field35 = x3dpsail.field()
field35.setName("endnode")
field35.setAccessType("initializeOnly")
field35.setType("SFNode")

ProtoInterface33.addField(field35)
field36 = x3dpsail.field()
field36.setName("set_startpoint")
field36.setAccessType("inputOnly")
field36.setType("SFVec3f")

ProtoInterface33.addField(field36)
field37 = x3dpsail.field()
field37.setName("set_endpoint")
field37.setAccessType("inputOnly")
field37.setType("SFVec3f")

ProtoInterface33.addField(field37)

ProtoDeclare32.setProtoInterface(ProtoInterface33)
ProtoBody38 = x3dpsail.ProtoBody()
Group39 = x3dpsail.Group()
Transform40 = x3dpsail.Transform()
Transform40.setDEF("trans")
Transform41 = x3dpsail.Transform()
Transform41.setDEF("rotscale")
Shape42 = x3dpsail.Shape()
Appearance43 = x3dpsail.Appearance()
Material44 = x3dpsail.Material()
Material44.setDiffuseColor([0.2,0.7,0.7])
Material44.setTransparency(0.5)

Appearance43.setMaterial(Material44)

Shape42.setAppearance(Appearance43)
Cylinder45 = x3dpsail.Cylinder()
Cylinder45.setRadius(0.05)

Shape42.setGeometry(Cylinder45)

Transform41.addChildren(Shape42)

Transform40.addChildren(Transform41)

Group39.addChildren(Transform40)
Script46 = x3dpsail.Script()
Script46.setDEF("S1")
field47 = x3dpsail.field()
field47.setName("startnode")
field47.setAccessType("initializeOnly")
field47.setType("SFNode")

Script46.addField(field47)
field48 = x3dpsail.field()
field48.setName("endnode")
field48.setAccessType("initializeOnly")
field48.setType("SFNode")

Script46.addField(field48)
field49 = x3dpsail.field()
field49.setName("position")
field49.setAccessType("inputOutput")
field49.setType("SFNode")
Transform50 = x3dpsail.Transform()
Transform50.setUSE("trans")

field49.addChildren(Transform50)

Script46.addField(field49)
field51 = x3dpsail.field()
field51.setName("rotscale")
field51.setAccessType("inputOutput")
field51.setType("SFNode")
Transform52 = x3dpsail.Transform()
Transform52.setUSE("rotscale")

field51.addChildren(Transform52)

Script46.addField(field51)
field53 = x3dpsail.field()
field53.setName("set_startpoint")
field53.setAccessType("inputOnly")
field53.setType("SFVec3f")

Script46.addField(field53)
field54 = x3dpsail.field()
field54.setName("set_endpoint")
field54.setAccessType("inputOnly")
field54.setType("SFVec3f")

Script46.addField(field54)
IS55 = x3dpsail.IS()
connect56 = x3dpsail.connect()
connect56.setNodeField("startnode")
connect56.setProtoField("startnode")

IS55.addConnect(connect56)
connect57 = x3dpsail.connect()
connect57.setNodeField("endnode")
connect57.setProtoField("endnode")

IS55.addConnect(connect57)
connect58 = x3dpsail.connect()
connect58.setNodeField("set_startpoint")
connect58.setProtoField("set_startpoint")

IS55.addConnect(connect58)
connect59 = x3dpsail.connect()
connect59.setNodeField("set_endpoint")
connect59.setProtoField("set_endpoint")

IS55.addConnect(connect59)

Script46.setIS(IS55)

Script46.setSourceCode('''ecmascript:\n"+
"        function recompute(startpoint,endpoint){\n"+
"	    if (typeof endpoint === 'undefined') {\n"+
"		return;\n"+
"	    }\n"+
"            var dif = endpoint.subtract(startpoint);\n"+
"            var dist = dif.length()*0.5;\n"+
"            var dif2 = dif.multiply(0.5);\n"+
"            var norm = dif.normalize();\n"+
"            var transl = startpoint.add(dif2);\n"+
"	    if (typeof Quaternion !== 'undefined') {\n"+
"		    return {\n"+
"			    scale : new SFVec3f(1.0,dist,1.0),\n"+
"			    translation : transl,\n"+
"			    rotation : new Quaternion.rotateFromTo(new SFVec3f(0.0,1.0,0.0), norm)\n"+
"		    };\n"+
"	    } else if (typeof SFRotation !== 'undefined') {\n"+
"		    return {\n"+
"			    scale : new SFVec3f(1.0,dist,1.0),\n"+
"			    translation : transl,\n"+
"			    rotation : new SFRotation(new SFVec3f(0.0,1.0,0.0),norm)\n"+
"		    };\n"+
"	    } else {\n"+
"		    return {\n"+
"			    scale : new SFVec3f(1.0,dist,1.0),\n"+
"			    translation : transl\n"+
"		    };\n"+
"	    }\n"+
"	}\n"+
"	function recompute_and_route(startpoint, endpoint) {\n"+
"	      var trafo = recompute(startpoint, endpoint);\n"+
"	      position.translation = trafo.translation;\n"+
"	      rotscale.rotation = trafo.rotation;\n"+
"	      rotscale.scale = trafo.scale;\n"+
"	}\n"+
"        function initialize(){\n"+
"            recompute_and_route(startnode.translation,endnode.translation);\n"+
"        }\n"+
"        function set_startpoint(val,t){\n"+
"            recompute_and_route(val,endnode.translation);\n"+
"        }\n"+
"        function set_endpoint(val,t){\n"+
"            recompute_and_route(startnode.translation,val);\n"+
"        }''')

Group39.addChildren(Script46)

ProtoBody38.addChildren(Group39)

ProtoDeclare32.setProtoBody(ProtoBody38)

Scene7.addChildren(ProtoDeclare32)
ProtoInstance60 = x3dpsail.ProtoInstance()
ProtoInstance60.setName("point")
ProtoInstance60.setDEF("G1")

Scene7.addChildren(ProtoInstance60)
ProtoInstance61 = x3dpsail.ProtoInstance()
ProtoInstance61.setName("point")
ProtoInstance61.setDEF("G2")

Scene7.addChildren(ProtoInstance61)
ProtoInstance62 = x3dpsail.ProtoInstance()
ProtoInstance62.setName("x3dconnector")
ProtoInstance62.setDEF("connector1")
fieldValue63 = x3dpsail.fieldValue()
fieldValue63.setName("startnode")
ProtoInstance64 = x3dpsail.ProtoInstance()
ProtoInstance64.setUSE("G1")

fieldValue63.addChildren(ProtoInstance64)

ProtoInstance62.addFieldValue(fieldValue63)
fieldValue65 = x3dpsail.fieldValue()
fieldValue65.setName("endnode")
ProtoInstance66 = x3dpsail.ProtoInstance()
ProtoInstance66.setUSE("G2")

fieldValue65.addChildren(ProtoInstance66)

ProtoInstance62.addFieldValue(fieldValue65)
fieldValue67 = x3dpsail.fieldValue()
fieldValue67.setName("set_startpoint")

ProtoInstance62.addFieldValue(fieldValue67)
fieldValue68 = x3dpsail.fieldValue()
fieldValue68.setName("set_endpoint")

ProtoInstance62.addFieldValue(fieldValue68)

Scene7.addChildren(ProtoInstance62)
ROUTE69 = x3dpsail.ROUTE()
ROUTE69.setFromNode("G1")
ROUTE69.setFromField("translation")
ROUTE69.setToNode("connector1")
ROUTE69.setToField("set_startpoint")

Scene7.addChildren(ROUTE69)
ROUTE70 = x3dpsail.ROUTE()
ROUTE70.setFromNode("G2")
ROUTE70.setFromField("translation")
ROUTE70.setToNode("connector1")
ROUTE70.setToField("set_endpoint")

Scene7.addChildren(ROUTE70)

X3D0.setScene(Scene7)
X3D0.toFileX3D("././arc1_RoundTrip.x3d")
