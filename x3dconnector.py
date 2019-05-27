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
Transform10 = x3dpsail.Transform()
Transform10.setDEF("G1")
Shape11 = x3dpsail.Shape()
Appearance12 = x3dpsail.Appearance()
Material13 = x3dpsail.Material()
Material13.setDiffuseColor([0.7,0.2,0.2])

Appearance12.setMaterial(Material13)

Shape11.setAppearance(Appearance12)
Sphere14 = x3dpsail.Sphere()
Sphere14.setRadius(0.1)

Shape11.setGeometry(Sphere14)

Transform10.addChildren(Shape11)
PlaneSensor15 = x3dpsail.PlaneSensor()
PlaneSensor15.setDescription("Grab to move")
PlaneSensor15.setDEF("PS1")

Transform10.addChildren(PlaneSensor15)
ROUTE16 = x3dpsail.ROUTE()
ROUTE16.setFromNode("PS1")
ROUTE16.setFromField("translation_changed")
ROUTE16.setToNode("G1")
ROUTE16.setToField("set_translation")

Transform10.addChildren(ROUTE16)

Scene7.addChildren(Transform10)
Transform17 = x3dpsail.Transform()
Transform17.setDEF("G2")
Transform17.setTranslation([1,-1,0.01])
Shape18 = x3dpsail.Shape()
Appearance19 = x3dpsail.Appearance()
Material20 = x3dpsail.Material()
Material20.setDiffuseColor([0.2,0.7,0.2])

Appearance19.setMaterial(Material20)

Shape18.setAppearance(Appearance19)
Sphere21 = x3dpsail.Sphere()
Sphere21.setRadius(0.1)

Shape18.setGeometry(Sphere21)

Transform17.addChildren(Shape18)
PlaneSensor22 = x3dpsail.PlaneSensor()
PlaneSensor22.setDescription("Grab to move")
PlaneSensor22.setOffset([1,-1,0.01])
PlaneSensor22.setDEF("PS2")

Transform17.addChildren(PlaneSensor22)
ROUTE23 = x3dpsail.ROUTE()
ROUTE23.setFromNode("PS2")
ROUTE23.setFromField("translation_changed")
ROUTE23.setToNode("G2")
ROUTE23.setToField("set_translation")

Transform17.addChildren(ROUTE23)

Scene7.addChildren(Transform17)
Transform24 = x3dpsail.Transform()
Transform24.setDEF("transC1")
Transform25 = x3dpsail.Transform()
Transform25.setDEF("rotscaleC1")
Shape26 = x3dpsail.Shape()
Appearance27 = x3dpsail.Appearance()
Material28 = x3dpsail.Material()
Material28.setDiffuseColor([0.2,0.7,0.7])
Material28.setTransparency(0.5)

Appearance27.setMaterial(Material28)

Shape26.setAppearance(Appearance27)
Cylinder29 = x3dpsail.Cylinder()
Cylinder29.setRadius(0.05)

Shape26.setGeometry(Cylinder29)

Transform25.addChildren(Shape26)

Transform24.addChildren(Transform25)

Scene7.addChildren(Transform24)
ProtoDeclare30 = x3dpsail.ProtoDeclare()
ProtoDeclare30.setName("x3dconnector")
ProtoInterface31 = x3dpsail.ProtoInterface()
field32 = x3dpsail.field()
field32.setName("startnode")
field32.setAccessType("initializeOnly")
field32.setType("SFNode")

ProtoInterface31.addField(field32)
field33 = x3dpsail.field()
field33.setName("endnode")
field33.setAccessType("initializeOnly")
field33.setType("SFNode")

ProtoInterface31.addField(field33)
field34 = x3dpsail.field()
field34.setName("transnode")
field34.setAccessType("initializeOnly")
field34.setType("SFNode")

ProtoInterface31.addField(field34)
field35 = x3dpsail.field()
field35.setName("rotscalenode")
field35.setAccessType("initializeOnly")
field35.setType("SFNode")

ProtoInterface31.addField(field35)
field36 = x3dpsail.field()
field36.setName("set_startpoint")
field36.setAccessType("inputOnly")
field36.setType("SFVec3f")

ProtoInterface31.addField(field36)
field37 = x3dpsail.field()
field37.setName("set_endpoint")
field37.setAccessType("inputOnly")
field37.setType("SFVec3f")

ProtoInterface31.addField(field37)

ProtoDeclare30.setProtoInterface(ProtoInterface31)
ProtoBody38 = x3dpsail.ProtoBody()
Script39 = x3dpsail.Script()
Script39.setDEF("S1")
field40 = x3dpsail.field()
field40.setName("startnode")
field40.setAccessType("initializeOnly")
field40.setType("SFNode")

Script39.addField(field40)
field41 = x3dpsail.field()
field41.setName("endnode")
field41.setAccessType("initializeOnly")
field41.setType("SFNode")

Script39.addField(field41)
field42 = x3dpsail.field()
field42.setName("transnode")
field42.setAccessType("initializeOnly")
field42.setType("SFNode")

Script39.addField(field42)
field43 = x3dpsail.field()
field43.setName("rotscalenode")
field43.setAccessType("initializeOnly")
field43.setType("SFNode")

Script39.addField(field43)
field44 = x3dpsail.field()
field44.setName("set_startpoint")
field44.setAccessType("inputOnly")
field44.setType("SFVec3f")

Script39.addField(field44)
field45 = x3dpsail.field()
field45.setName("set_endpoint")
field45.setAccessType("inputOnly")
field45.setType("SFVec3f")

Script39.addField(field45)
IS46 = x3dpsail.IS()
connect47 = x3dpsail.connect()
connect47.setNodeField("startnode")
connect47.setProtoField("startnode")

IS46.addConnect(connect47)
connect48 = x3dpsail.connect()
connect48.setNodeField("endnode")
connect48.setProtoField("endnode")

IS46.addConnect(connect48)
connect49 = x3dpsail.connect()
connect49.setNodeField("transnode")
connect49.setProtoField("transnode")

IS46.addConnect(connect49)
connect50 = x3dpsail.connect()
connect50.setNodeField("rotscalenode")
connect50.setProtoField("rotscalenode")

IS46.addConnect(connect50)
connect51 = x3dpsail.connect()
connect51.setNodeField("set_startpoint")
connect51.setProtoField("set_startpoint")

IS46.addConnect(connect51)
connect52 = x3dpsail.connect()
connect52.setNodeField("set_endpoint")
connect52.setProtoField("set_endpoint")

IS46.addConnect(connect52)

Script39.setIS(IS46)

Script39.setSourceCode('''ecmascript:\n"+
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
"	    } else {\n"+
"		    return {\n"+
"			    scale : new SFVec3f(1.0,dist,1.0),\n"+
"			    translation : transl,\n"+
"			    rotation : new SFRotation(new SFVec3f(0.0,1.0,0.0),norm)\n"+
"		    };\n"+
"	    }\n"+
"	}\n"+
"	function recompute_and_route(startpoint, endpoint) {\n"+
"	      var trafo = recompute(startpoint, endpoint);\n"+
"	      transnode.translation = trafo.translation;\n"+
"	      rotscalenode.rotation = trafo.rotation;\n"+
"	      rotscalenode.scale = trafo.scale;\n"+
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

ProtoBody38.addChildren(Script39)

ProtoDeclare30.setProtoBody(ProtoBody38)

Scene7.addChildren(ProtoDeclare30)
ProtoInstance53 = x3dpsail.ProtoInstance()
ProtoInstance53.setName("x3dconnector")
ProtoInstance53.setDEF("connector1")
fieldValue54 = x3dpsail.fieldValue()
fieldValue54.setName("startnode")
Transform55 = x3dpsail.Transform()
Transform55.setUSE("G1")

fieldValue54.addChildren(Transform55)

ProtoInstance53.addFieldValue(fieldValue54)
fieldValue56 = x3dpsail.fieldValue()
fieldValue56.setName("endnode")
Transform57 = x3dpsail.Transform()
Transform57.setUSE("G2")

fieldValue56.addChildren(Transform57)

ProtoInstance53.addFieldValue(fieldValue56)
fieldValue58 = x3dpsail.fieldValue()
fieldValue58.setName("transnode")
Transform59 = x3dpsail.Transform()
Transform59.setUSE("transC1")

fieldValue58.addChildren(Transform59)

ProtoInstance53.addFieldValue(fieldValue58)
fieldValue60 = x3dpsail.fieldValue()
fieldValue60.setName("rotscalenode")
Transform61 = x3dpsail.Transform()
Transform61.setUSE("rotscaleC1")

fieldValue60.addChildren(Transform61)

ProtoInstance53.addFieldValue(fieldValue60)
fieldValue62 = x3dpsail.fieldValue()
fieldValue62.setName("set_startpoint")

ProtoInstance53.addFieldValue(fieldValue62)
fieldValue63 = x3dpsail.fieldValue()
fieldValue63.setName("set_endpoint")

ProtoInstance53.addFieldValue(fieldValue63)

Scene7.addChildren(ProtoInstance53)
ROUTE64 = x3dpsail.ROUTE()
ROUTE64.setFromNode("G1")
ROUTE64.setFromField("translation_changed")
ROUTE64.setToNode("connector1")
ROUTE64.setToField("set_startpoint")

Scene7.addChildren(ROUTE64)
ROUTE65 = x3dpsail.ROUTE()
ROUTE65.setFromNode("G2")
ROUTE65.setFromField("translation_changed")
ROUTE65.setToNode("connector1")
ROUTE65.setToField("set_endpoint")

Scene7.addChildren(ROUTE65)

X3D0.setScene(Scene7)
X3D0.toFileX3D("././x3dconnector_RoundTrip.x3d")
