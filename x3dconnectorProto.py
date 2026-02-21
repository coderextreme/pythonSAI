print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"
head1 = x3d.head()
meta2 = x3d.meta()
meta2.name = "title"
meta2.content = "x3dconnectorProto"

head1.children.append(meta2)
meta3 = x3d.meta()
meta3.name = "creator"
meta3.content = "Lost, Doug Sanden I think"

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.name = "generator"
meta4.content = "manual"

head1.children.append(meta4)
meta5 = x3d.meta()
meta5.name = "identifier"
meta5.content = "https://coderextreme.net/X3DJSONLD/x3dconnectorProto.x3d"

head1.children.append(meta5)
meta6 = x3d.meta()
meta6.name = "description"
meta6.content = "a generic proto to connect two objects"

head1.children.append(meta6)
meta7 = x3d.meta()
meta7.content = "https://www.web3d.org/x3d/content/examples/license.html"
meta7.name = "license"

head1.children.append(meta7)

X3D0.head = head1
Scene8 = x3d.Scene()
WorldInfo9 = x3d.WorldInfo()
WorldInfo9.title = "Connector Proto"

Scene8.children.append(WorldInfo9)
Viewpoint10 = x3d.Viewpoint()
Viewpoint10.position = [0,0,5]
Viewpoint10.description = "Only Viewpoint"

Scene8.children.append(Viewpoint10)
Background11 = x3d.Background()

Scene8.children.append(Background11)
Transform12 = x3d.Transform()
Transform12.DEF = "G1"
Shape13 = x3d.Shape()
Appearance14 = x3d.Appearance()
Material15 = x3d.Material()
Material15.diffuseColor = [0.7,0.2,0.2]

Appearance14.material = Material15

Shape13.appearance = Appearance14
Sphere16 = x3d.Sphere()
Sphere16.radius = .1

Shape13.geometry = Sphere16

Transform12.children.append(Shape13)
PlaneSensor17 = x3d.PlaneSensor()
PlaneSensor17.description = "Grab to move"
PlaneSensor17.DEF = "PS1"

Transform12.children.append(PlaneSensor17)
ROUTE18 = x3d.ROUTE()
ROUTE18.fromNode = "PS1"
ROUTE18.fromField = "translation_changed"
ROUTE18.toNode = "G1"
ROUTE18.toField = "set_translation"

Transform12.children.append(ROUTE18)

Scene8.children.append(Transform12)
Transform19 = x3d.Transform()
Transform19.DEF = "G2"
Transform19.translation = [1,-1,.01]
Shape20 = x3d.Shape()
Appearance21 = x3d.Appearance()
Material22 = x3d.Material()
Material22.diffuseColor = [0.2,0.7,0.2]

Appearance21.material = Material22

Shape20.appearance = Appearance21
Sphere23 = x3d.Sphere()
Sphere23.radius = .1

Shape20.geometry = Sphere23

Transform19.children.append(Shape20)
PlaneSensor24 = x3d.PlaneSensor()
PlaneSensor24.description = "Grab to move"
PlaneSensor24.offset = [1,-1,.01]
PlaneSensor24.DEF = "PS2"

Transform19.children.append(PlaneSensor24)
ROUTE25 = x3d.ROUTE()
ROUTE25.fromNode = "PS2"
ROUTE25.fromField = "translation_changed"
ROUTE25.toNode = "G2"
ROUTE25.toField = "set_translation"

Transform19.children.append(ROUTE25)

Scene8.children.append(Transform19)
Transform26 = x3d.Transform()
Transform26.DEF = "G3"
Transform26.translation = [1,1,.01]
Shape27 = x3d.Shape()
Appearance28 = x3d.Appearance()
Material29 = x3d.Material()
Material29.diffuseColor = [0.2,0.7,0.2]

Appearance28.material = Material29

Shape27.appearance = Appearance28
Sphere30 = x3d.Sphere()
Sphere30.radius = .1

Shape27.geometry = Sphere30

Transform26.children.append(Shape27)
PlaneSensor31 = x3d.PlaneSensor()
PlaneSensor31.description = "Grab to move"
PlaneSensor31.offset = [1,1,.01]
PlaneSensor31.DEF = "PS3"

Transform26.children.append(PlaneSensor31)
ROUTE32 = x3d.ROUTE()
ROUTE32.fromNode = "PS3"
ROUTE32.fromField = "translation_changed"
ROUTE32.toNode = "G3"
ROUTE32.toField = "set_translation"

Transform26.children.append(ROUTE32)

Scene8.children.append(Transform26)
Transform33 = x3d.Transform()
Transform33.DEF = "G4"
Transform33.translation = [-1,1,.01]
Shape34 = x3d.Shape()
Appearance35 = x3d.Appearance()
Material36 = x3d.Material()
Material36.diffuseColor = [0.2,0.7,0.2]

Appearance35.material = Material36

Shape34.appearance = Appearance35
Sphere37 = x3d.Sphere()
Sphere37.radius = .1

Shape34.geometry = Sphere37

Transform33.children.append(Shape34)
PlaneSensor38 = x3d.PlaneSensor()
PlaneSensor38.description = "Grab to move"
PlaneSensor38.offset = [-1,1,.01]
PlaneSensor38.DEF = "PS4"

Transform33.children.append(PlaneSensor38)
ROUTE39 = x3d.ROUTE()
ROUTE39.fromNode = "PS4"
ROUTE39.fromField = "translation_changed"
ROUTE39.toNode = "G4"
ROUTE39.toField = "set_translation"

Transform33.children.append(ROUTE39)

Scene8.children.append(Transform33)
Transform40 = x3d.Transform()
Transform40.DEF = "transC1"
Transform41 = x3d.Transform()
Transform41.DEF = "rotscaleC1"
Shape42 = x3d.Shape()
Appearance43 = x3d.Appearance()
Material44 = x3d.Material()
Material44.diffuseColor = [0.2,0.7,0.7]
Material44.transparency = .5

Appearance43.material = Material44

Shape42.appearance = Appearance43
Cylinder45 = x3d.Cylinder()
Cylinder45.radius = .05

Shape42.geometry = Cylinder45

Transform41.children.append(Shape42)

Transform40.children.append(Transform41)

Scene8.children.append(Transform40)
Transform46 = x3d.Transform()
Transform46.DEF = "transC2"
Transform47 = x3d.Transform()
Transform47.DEF = "rotscaleC2"
Shape48 = x3d.Shape()
Appearance49 = x3d.Appearance()
Material50 = x3d.Material()
Material50.diffuseColor = [0.2,0.7,0.7]
Material50.transparency = .5

Appearance49.material = Material50

Shape48.appearance = Appearance49
Cylinder51 = x3d.Cylinder()
Cylinder51.radius = .05

Shape48.geometry = Cylinder51

Transform47.children.append(Shape48)

Transform46.children.append(Transform47)

Scene8.children.append(Transform46)
Transform52 = x3d.Transform()
Transform52.DEF = "transC3"
Transform53 = x3d.Transform()
Transform53.DEF = "rotscaleC3"
Shape54 = x3d.Shape()
Appearance55 = x3d.Appearance()
Material56 = x3d.Material()
Material56.diffuseColor = [0.2,0.7,0.7]
Material56.transparency = .5

Appearance55.material = Material56

Shape54.appearance = Appearance55
Cylinder57 = x3d.Cylinder()
Cylinder57.radius = .05

Shape54.geometry = Cylinder57

Transform53.children.append(Shape54)

Transform52.children.append(Transform53)

Scene8.children.append(Transform52)
ProtoDeclare58 = x3d.ProtoDeclare()
ProtoDeclare58.name = "x3dconnector"
ProtoInterface59 = x3d.ProtoInterface()
field60 = x3d.field()
field60.accessType = "initializeOnly"
field60.name = "startnode"
field60.type = "SFNode"

ProtoInterface59.field.append(field60)
field61 = x3d.field()
field61.accessType = "initializeOnly"
field61.name = "endnode"
field61.type = "SFNode"

ProtoInterface59.field.append(field61)
field62 = x3d.field()
field62.accessType = "initializeOnly"
field62.name = "transnode"
field62.type = "SFNode"

ProtoInterface59.field.append(field62)
field63 = x3d.field()
field63.accessType = "initializeOnly"
field63.name = "rotscalenode"
field63.type = "SFNode"

ProtoInterface59.field.append(field63)
field64 = x3d.field()
field64.accessType = "inputOnly"
field64.name = "set_startpoint"
field64.type = "SFVec3f"

ProtoInterface59.field.append(field64)
field65 = x3d.field()
field65.accessType = "inputOnly"
field65.name = "set_endpoint"
field65.type = "SFVec3f"

ProtoInterface59.field.append(field65)

ProtoDeclare58.ProtoInterface = ProtoInterface59
ProtoBody66 = x3d.ProtoBody()
Script67 = x3d.Script()
Script67.DEF = "S1"
field68 = x3d.field()
field68.accessType = "initializeOnly"
field68.name = "startnode"
field68.type = "SFNode"

Script67.field.append(field68)
field69 = x3d.field()
field69.accessType = "initializeOnly"
field69.name = "endnode"
field69.type = "SFNode"

Script67.field.append(field69)
field70 = x3d.field()
field70.accessType = "initializeOnly"
field70.name = "transnode"
field70.type = "SFNode"

Script67.field.append(field70)
field71 = x3d.field()
field71.accessType = "initializeOnly"
field71.name = "rotscalenode"
field71.type = "SFNode"

Script67.field.append(field71)
field72 = x3d.field()
field72.accessType = "inputOnly"
field72.name = "set_startpoint"
field72.type = "SFVec3f"

Script67.field.append(field72)
field73 = x3d.field()
field73.accessType = "inputOnly"
field73.name = "set_endpoint"
field73.type = "SFVec3f"

Script67.field.append(field73)
IS74 = x3d.IS()
connect75 = x3d.connect()
connect75.nodeField = "startnode"
connect75.protoField = "startnode"

IS74.connect.append(connect75)
connect76 = x3d.connect()
connect76.nodeField = "endnode"
connect76.protoField = "endnode"

IS74.connect.append(connect76)
connect77 = x3d.connect()
connect77.nodeField = "transnode"
connect77.protoField = "transnode"

IS74.connect.append(connect77)
connect78 = x3d.connect()
connect78.nodeField = "rotscalenode"
connect78.protoField = "rotscalenode"

IS74.connect.append(connect78)
connect79 = x3d.connect()
connect79.nodeField = "set_startpoint"
connect79.protoField = "set_startpoint"

IS74.connect.append(connect79)
connect80 = x3d.connect()
connect80.nodeField = "set_endpoint"
connect80.protoField = "set_endpoint"

IS74.connect.append(connect80)

Script67.IS = IS74

Script67.sourceCode = '''ecmascript:\n"+
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
"	      if (trafo) {\n"+
"		      transnode.translation = trafo.translation;\n"+
"		      rotscalenode.rotation = trafo.rotation;\n"+
"		      rotscalenode.scale = trafo.scale;\n"+
"	      }\n"+
"	}\n"+
"        function initialize(){\n"+
"            recompute_and_route(startnode.translation,endnode.translation);\n"+
"        }\n"+
"        function set_startpoint(val,t){\n"+
"            recompute_and_route(val,endnode.translation);\n"+
"        }\n"+
"        function set_endpoint(val,t){\n"+
"            recompute_and_route(startnode.translation,val);\n"+
"        }\n"+
"            '''

ProtoBody66.children.append(Script67)

ProtoDeclare58.ProtoBody = ProtoBody66

Scene8.children.append(ProtoDeclare58)
ProtoInstance81 = x3d.ProtoInstance()
ProtoInstance81.name = "x3dconnector"
ProtoInstance81.DEF = "connector1"
fieldValue82 = x3d.fieldValue()
fieldValue82.name = "startnode"
Transform83 = x3d.Transform()
Transform83.USE = "G1"

fieldValue82.children.append(Transform83)

ProtoInstance81.fieldValue.append(fieldValue82)
fieldValue84 = x3d.fieldValue()
fieldValue84.name = "endnode"
Transform85 = x3d.Transform()
Transform85.USE = "G2"

fieldValue84.children.append(Transform85)

ProtoInstance81.fieldValue.append(fieldValue84)
fieldValue86 = x3d.fieldValue()
fieldValue86.name = "transnode"
Transform87 = x3d.Transform()
Transform87.USE = "transC1"

fieldValue86.children.append(Transform87)

ProtoInstance81.fieldValue.append(fieldValue86)
fieldValue88 = x3d.fieldValue()
fieldValue88.name = "rotscalenode"
Transform89 = x3d.Transform()
Transform89.USE = "rotscaleC1"

fieldValue88.children.append(Transform89)

ProtoInstance81.fieldValue.append(fieldValue88)
fieldValue90 = x3d.fieldValue()
fieldValue90.name = "set_startpoint"
fieldValue90.value = "0 0 0"

ProtoInstance81.fieldValue.append(fieldValue90)
fieldValue91 = x3d.fieldValue()
fieldValue91.name = "set_endpoint"
fieldValue91.value = "0 0 0"

ProtoInstance81.fieldValue.append(fieldValue91)

Scene8.children.append(ProtoInstance81)
ProtoInstance92 = x3d.ProtoInstance()
ProtoInstance92.name = "x3dconnector"
ProtoInstance92.DEF = "connector2"
fieldValue93 = x3d.fieldValue()
fieldValue93.name = "startnode"
Transform94 = x3d.Transform()
Transform94.USE = "G1"

fieldValue93.children.append(Transform94)

ProtoInstance92.fieldValue.append(fieldValue93)
fieldValue95 = x3d.fieldValue()
fieldValue95.name = "endnode"
Transform96 = x3d.Transform()
Transform96.USE = "G3"

fieldValue95.children.append(Transform96)

ProtoInstance92.fieldValue.append(fieldValue95)
fieldValue97 = x3d.fieldValue()
fieldValue97.name = "transnode"
Transform98 = x3d.Transform()
Transform98.USE = "transC2"

fieldValue97.children.append(Transform98)

ProtoInstance92.fieldValue.append(fieldValue97)
fieldValue99 = x3d.fieldValue()
fieldValue99.name = "rotscalenode"
Transform100 = x3d.Transform()
Transform100.USE = "rotscaleC2"

fieldValue99.children.append(Transform100)

ProtoInstance92.fieldValue.append(fieldValue99)
fieldValue101 = x3d.fieldValue()
fieldValue101.name = "set_startpoint"
fieldValue101.value = "0 0 0"

ProtoInstance92.fieldValue.append(fieldValue101)
fieldValue102 = x3d.fieldValue()
fieldValue102.name = "set_endpoint"
fieldValue102.value = "0 0 0"

ProtoInstance92.fieldValue.append(fieldValue102)

Scene8.children.append(ProtoInstance92)
ProtoInstance103 = x3d.ProtoInstance()
ProtoInstance103.name = "x3dconnector"
ProtoInstance103.DEF = "connector3"
fieldValue104 = x3d.fieldValue()
fieldValue104.name = "startnode"
Transform105 = x3d.Transform()
Transform105.USE = "G1"

fieldValue104.children.append(Transform105)

ProtoInstance103.fieldValue.append(fieldValue104)
fieldValue106 = x3d.fieldValue()
fieldValue106.name = "endnode"
Transform107 = x3d.Transform()
Transform107.USE = "G4"

fieldValue106.children.append(Transform107)

ProtoInstance103.fieldValue.append(fieldValue106)
fieldValue108 = x3d.fieldValue()
fieldValue108.name = "transnode"
Transform109 = x3d.Transform()
Transform109.USE = "transC3"

fieldValue108.children.append(Transform109)

ProtoInstance103.fieldValue.append(fieldValue108)
fieldValue110 = x3d.fieldValue()
fieldValue110.name = "rotscalenode"
Transform111 = x3d.Transform()
Transform111.USE = "rotscaleC3"

fieldValue110.children.append(Transform111)

ProtoInstance103.fieldValue.append(fieldValue110)
fieldValue112 = x3d.fieldValue()
fieldValue112.name = "set_startpoint"
fieldValue112.value = "0 0 0"

ProtoInstance103.fieldValue.append(fieldValue112)
fieldValue113 = x3d.fieldValue()
fieldValue113.name = "set_endpoint"
fieldValue113.value = "0 0 0"

ProtoInstance103.fieldValue.append(fieldValue113)

Scene8.children.append(ProtoInstance103)
ROUTE114 = x3d.ROUTE()
ROUTE114.fromNode = "G1"
ROUTE114.fromField = "translation_changed"
ROUTE114.toNode = "connector1"
ROUTE114.toField = "set_startpoint"

Scene8.children.append(ROUTE114)
ROUTE115 = x3d.ROUTE()
ROUTE115.fromNode = "G2"
ROUTE115.fromField = "translation_changed"
ROUTE115.toNode = "connector1"
ROUTE115.toField = "set_endpoint"

Scene8.children.append(ROUTE115)
ROUTE116 = x3d.ROUTE()
ROUTE116.fromNode = "G1"
ROUTE116.fromField = "translation_changed"
ROUTE116.toNode = "connector2"
ROUTE116.toField = "set_startpoint"

Scene8.children.append(ROUTE116)
ROUTE117 = x3d.ROUTE()
ROUTE117.fromNode = "G3"
ROUTE117.fromField = "translation_changed"
ROUTE117.toNode = "connector2"
ROUTE117.toField = "set_endpoint"

Scene8.children.append(ROUTE117)
ROUTE118 = x3d.ROUTE()
ROUTE118.fromNode = "G1"
ROUTE118.fromField = "translation_changed"
ROUTE118.toNode = "connector3"
ROUTE118.toField = "set_startpoint"

Scene8.children.append(ROUTE118)
ROUTE119 = x3d.ROUTE()
ROUTE119.fromNode = "G4"
ROUTE119.fromField = "translation_changed"
ROUTE119.toNode = "connector3"
ROUTE119.toField = "set_endpoint"

Scene8.children.append(ROUTE119)

X3D0.Scene = Scene8
f = open("x3dconnectorProto_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
