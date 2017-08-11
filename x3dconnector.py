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
ROUTE16.setToField("translation")

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
ROUTE23.setToField("translation")

Transform17.addChild(ROUTE23)
Scene7.addChild(Transform17)
Transform24 = TransformObject()
Transform24.setDEF("C0")

Transform25 = TransformObject()
Transform25.setDEF("C1")

Transform26 = TransformObject()
Transform26.setDEF("C2")

Shape27 = ShapeObject()

Appearance28 = AppearanceObject()

Material29 = MaterialObject()
Material29.setDiffuseColor([0.2,0.7,0.7])
Material29.setTransparency(0.5)

Appearance28.setMaterial(Material29)
Shape27.setAppearance(Appearance28)
Cylinder30 = CylinderObject()
Cylinder30.setRadius(0.05)

Shape27.setGeometry(Cylinder30)
Transform26.addChild(Shape27)
Transform25.addChild(Transform26)
Transform24.addChild(Transform25)
Scene7.addChild(Transform24)
Script31 = ScriptObject()
Script31.setDEF("S1")

field32 = fieldObject()
field32.setType(fieldObject.TYPE_SFNODE)
field32.setName("startnode")
field32.setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY)

Transform33 = TransformObject()
Transform33.setUSE("G1")

field32.addChild(Transform33)
Script31.addField(field32)
field34 = fieldObject()
field34.setType(fieldObject.TYPE_SFNODE)
field34.setName("endnode")
field34.setAccessType(fieldObject.ACCESSTYPE_INITIALIZEONLY)

Transform35 = TransformObject()
Transform35.setUSE("G2")

field34.addChild(Transform35)
Script31.addField(field34)
field36 = fieldObject()
field36.setType(fieldObject.TYPE_SFVEC3F)
field36.setName("set_startpoint")
field36.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)

Script31.addField(field36)
field37 = fieldObject()
field37.setType(fieldObject.TYPE_SFVEC3F)
field37.setName("set_endpoint")
field37.setAccessType(fieldObject.ACCESSTYPE_INPUTONLY)

Script31.addField(field37)
field38 = fieldObject()
field38.setType(fieldObject.TYPE_SFVEC3F)
field38.setName("translation")
field38.setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY)

Script31.addField(field38)
field39 = fieldObject()
field39.setType(fieldObject.TYPE_SFROTATION)
field39.setName("rotation")
field39.setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY)

Script31.addField(field39)
field40 = fieldObject()
field40.setType(fieldObject.TYPE_SFVEC3F)
field40.setName("scale")
field40.setAccessType(fieldObject.ACCESSTYPE_OUTPUTONLY)

Script31.addField(field40)

Script31.setSourceCode("\n"+
"        ecmascript:\n"+
"        function recompute(startpoint,endpoint){\n"+
"            var dif = endpoint.subtract(startpoint);\n"+
"            var dist = dif.length()*.5;\n"+
"            var dif2 = dif.multiply(.5);\n"+
"            var norm = dif.normalize();\n"+
"            var trans = startpoint.add(dif2);\n"+
"            scale = new SFVec3f(1.0,dist,1.0);\n"+
"            translation = trans;\n"+
"            rotation = new SFRotation(new SFVec3f(0.0,1.0,0.0),norm);\n"+
"            //Browser.print('norm='+norm.toString());\n"+
"            //Browser.print('rotation='+rotation.toString());\n"+
"        }\n"+
"        function initialize(){\n"+
"            recompute(startnode.translation,endnode.translation);\n"+
"        }\n"+
"        function set_startpoint(val,t){\n"+
"            recompute(val,endnode.translation);\n"+
"        }\n"+
"        function set_endpoint(val,t){\n"+
"            recompute(startnode.translation,val);\n"+
"        }\n"+
"")
Scene7.addChild(Script31)
ROUTE41 = ROUTEObject()
ROUTE41.setFromNode("G1")
ROUTE41.setFromField("translation")
ROUTE41.setToNode("S1")
ROUTE41.setToField("set_startpoint")

Scene7.addChild(ROUTE41)
ROUTE42 = ROUTEObject()
ROUTE42.setFromNode("G2")
ROUTE42.setFromField("translation")
ROUTE42.setToNode("S1")
ROUTE42.setToField("set_endpoint")

Scene7.addChild(ROUTE42)
ROUTE43 = ROUTEObject()
ROUTE43.setFromNode("S1")
ROUTE43.setFromField("translation")
ROUTE43.setToNode("C0")
ROUTE43.setToField("translation")

Scene7.addChild(ROUTE43)
ROUTE44 = ROUTEObject()
ROUTE44.setFromNode("S1")
ROUTE44.setFromField("rotation")
ROUTE44.setToNode("C2")
ROUTE44.setToField("rotation")

Scene7.addChild(ROUTE44)
ROUTE45 = ROUTEObject()
ROUTE45.setFromNode("S1")
ROUTE45.setFromField("scale")
ROUTE45.setToNode("C2")
ROUTE45.setToField("scale")

Scene7.addChild(ROUTE45)
X3D0.setScene(Scene7)

X3D0.toFileX3D("./x3dconnector.new.x3d")
