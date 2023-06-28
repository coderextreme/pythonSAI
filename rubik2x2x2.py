print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"
head1 = x3d.head()
meta2 = x3d.meta()
meta2.name = "title"
meta2.content = "rubik2x2x2.x3d"

head1.children.append(meta2)
meta3 = x3d.meta()
meta3.name = "creator"
meta3.content = "John Carlson"

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.name = "generator"
meta4.content = "manual"

head1.children.append(meta4)
meta5 = x3d.meta()
meta5.name = "identifier"
meta5.content = "https://coderextreme.net/X3DJSONLD/rubik.x3d"

head1.children.append(meta5)
meta6 = x3d.meta()
meta6.name = "description"
meta6.content = "a kind of 2x2x2 rubik cube"

head1.children.append(meta6)

X3D0.head = head1
Scene7 = x3d.Scene()
NavigationInfo8 = x3d.NavigationInfo()
NavigationInfo8.type = ["EXAMINE"]

Scene7.children.append(NavigationInfo8)
Viewpoint9 = x3d.Viewpoint()
Viewpoint9.description = "Rubiks Cube"
Viewpoint9.position = [0,0,12]

Scene7.children.append(Viewpoint9)
ProtoDeclare10 = x3d.ProtoDeclare()
ProtoDeclare10.name = "boxproto"
ProtoInterface11 = x3d.ProtoInterface()
field12 = x3d.field()
field12.name = "xtranslation"
field12.accessType = "inputOutput"
field12.type = "SFVec3f"
field12.value = [0,0,0]

ProtoInterface11.field.append(field12)
field13 = x3d.field()
field13.name = "diffuseColor"
field13.accessType = "inputOutput"
field13.type = "SFColor"
field13.value = [1,1,1]

ProtoInterface11.field.append(field13)

ProtoDeclare10.ProtoInterface = ProtoInterface11
ProtoBody14 = x3d.ProtoBody()
Transform15 = x3d.Transform()
IS16 = x3d.IS()
connect17 = x3d.connect()
connect17.nodeField = "translation"
connect17.protoField = "xtranslation"

IS16.connect.append(connect17)

Transform15.IS = IS16
Shape18 = x3d.Shape()
Box19 = x3d.Box()

Shape18.geometry = Box19
Appearance20 = x3d.Appearance()
Material21 = x3d.Material()
Material21.diffuseColor = [1,1,1]
IS22 = x3d.IS()
connect23 = x3d.connect()
connect23.nodeField = "diffuseColor"
connect23.protoField = "diffuseColor"

IS22.connect.append(connect23)

Material21.IS = IS22

Appearance20.material = Material21

Shape18.appearance = Appearance20

Transform15.children.append(Shape18)

ProtoBody14.children.append(Transform15)

ProtoDeclare10.ProtoBody = ProtoBody14

Scene7.children.append(ProtoDeclare10)
ProtoDeclare24 = x3d.ProtoDeclare()
ProtoDeclare24.name = "two"
ProtoInterface25 = x3d.ProtoInterface()
field26 = x3d.field()
field26.name = "ytranslation"
field26.accessType = "inputOutput"
field26.type = "SFVec3f"
field26.value = [0,0,0]

ProtoInterface25.field.append(field26)
field27 = x3d.field()
field27.name = "diffuseColor"
field27.accessType = "inputOutput"
field27.type = "SFColor"
field27.value = [1,0,0]

ProtoInterface25.field.append(field27)

ProtoDeclare24.ProtoInterface = ProtoInterface25
ProtoBody28 = x3d.ProtoBody()
Transform29 = x3d.Transform()
IS30 = x3d.IS()
connect31 = x3d.connect()
connect31.nodeField = "translation"
connect31.protoField = "ytranslation"

IS30.connect.append(connect31)

Transform29.IS = IS30
ProtoInstance32 = x3d.ProtoInstance()
ProtoInstance32.name = "boxproto"
fieldValue33 = x3d.fieldValue()
fieldValue33.name = "xtranslation"
fieldValue33.value = "0 0 0"

ProtoInstance32.fieldValue.append(fieldValue33)
fieldValue34 = x3d.fieldValue()
fieldValue34.name = "diffuseColor"
IS35 = x3d.IS()
connect36 = x3d.connect()
connect36.nodeField = "diffuseColor"
connect36.protoField = "diffuseColor"

IS35.connect.append(connect36)

fieldValue34.children.append(IS35)

ProtoInstance32.fieldValue.append(fieldValue34)

Transform29.children.append(ProtoInstance32)
ProtoInstance37 = x3d.ProtoInstance()
ProtoInstance37.name = "boxproto"
fieldValue38 = x3d.fieldValue()
fieldValue38.name = "xtranslation"
fieldValue38.value = "2 0 0"

ProtoInstance37.fieldValue.append(fieldValue38)
fieldValue39 = x3d.fieldValue()
fieldValue39.name = "diffuseColor"
IS40 = x3d.IS()
connect41 = x3d.connect()
connect41.nodeField = "diffuseColor"
connect41.protoField = "diffuseColor"

IS40.connect.append(connect41)

fieldValue39.children.append(IS40)

ProtoInstance37.fieldValue.append(fieldValue39)

Transform29.children.append(ProtoInstance37)

ProtoBody28.children.append(Transform29)

ProtoDeclare24.ProtoBody = ProtoBody28

Scene7.children.append(ProtoDeclare24)
ProtoDeclare42 = x3d.ProtoDeclare()
ProtoDeclare42.name = "four"
ProtoInterface43 = x3d.ProtoInterface()
field44 = x3d.field()
field44.name = "ztranslation"
field44.accessType = "inputOutput"
field44.type = "SFVec3f"
field44.value = [0,0,0]

ProtoInterface43.field.append(field44)
field45 = x3d.field()
field45.name = "x1diffuseColor"
field45.accessType = "inputOutput"
field45.type = "SFColor"
field45.value = [1,0,0]

ProtoInterface43.field.append(field45)
field46 = x3d.field()
field46.name = "x2diffuseColor"
field46.accessType = "inputOutput"
field46.type = "SFColor"
field46.value = [0,1,0]

ProtoInterface43.field.append(field46)

ProtoDeclare42.ProtoInterface = ProtoInterface43
ProtoBody47 = x3d.ProtoBody()
Transform48 = x3d.Transform()
IS49 = x3d.IS()
connect50 = x3d.connect()
connect50.nodeField = "translation"
connect50.protoField = "ztranslation"

IS49.connect.append(connect50)

Transform48.IS = IS49
ProtoInstance51 = x3d.ProtoInstance()
ProtoInstance51.name = "two"
fieldValue52 = x3d.fieldValue()
fieldValue52.name = "ytranslation"
fieldValue52.value = "0 0 0"

ProtoInstance51.fieldValue.append(fieldValue52)
fieldValue53 = x3d.fieldValue()
fieldValue53.name = "diffuseColor"
IS54 = x3d.IS()
connect55 = x3d.connect()
connect55.nodeField = "diffuseColor"
connect55.protoField = "x1diffuseColor"

IS54.connect.append(connect55)

fieldValue53.children.append(IS54)

ProtoInstance51.fieldValue.append(fieldValue53)

Transform48.children.append(ProtoInstance51)
ProtoInstance56 = x3d.ProtoInstance()
ProtoInstance56.name = "two"
fieldValue57 = x3d.fieldValue()
fieldValue57.name = "ytranslation"
fieldValue57.value = "0 2 0"

ProtoInstance56.fieldValue.append(fieldValue57)
fieldValue58 = x3d.fieldValue()
fieldValue58.name = "diffuseColor"
IS59 = x3d.IS()
connect60 = x3d.connect()
connect60.nodeField = "diffuseColor"
connect60.protoField = "x2diffuseColor"

IS59.connect.append(connect60)

fieldValue58.children.append(IS59)

ProtoInstance56.fieldValue.append(fieldValue58)

Transform48.children.append(ProtoInstance56)

ProtoBody47.children.append(Transform48)

ProtoDeclare42.ProtoBody = ProtoBody47

Scene7.children.append(ProtoDeclare42)
ProtoDeclare61 = x3d.ProtoDeclare()
ProtoDeclare61.name = "eight"
ProtoInterface62 = x3d.ProtoInterface()
field63 = x3d.field()
field63.name = "ttranslation"
field63.accessType = "inputOutput"
field63.type = "SFVec3f"
field63.value = [0,0,0]

ProtoInterface62.field.append(field63)

ProtoDeclare61.ProtoInterface = ProtoInterface62
ProtoBody64 = x3d.ProtoBody()
Transform65 = x3d.Transform()
IS66 = x3d.IS()
connect67 = x3d.connect()
connect67.nodeField = "translation"
connect67.protoField = "ttranslation"

IS66.connect.append(connect67)

Transform65.IS = IS66
ProtoInstance68 = x3d.ProtoInstance()
ProtoInstance68.name = "four"
fieldValue69 = x3d.fieldValue()
fieldValue69.name = "ztranslation"
fieldValue69.value = "0 0 0"

ProtoInstance68.fieldValue.append(fieldValue69)
fieldValue70 = x3d.fieldValue()
fieldValue70.name = "x1diffuseColor"
fieldValue70.value = "1 0 0"

ProtoInstance68.fieldValue.append(fieldValue70)
fieldValue71 = x3d.fieldValue()
fieldValue71.name = "x2diffuseColor"
fieldValue71.value = "0 1 0"

ProtoInstance68.fieldValue.append(fieldValue71)

Transform65.children.append(ProtoInstance68)
ProtoInstance72 = x3d.ProtoInstance()
ProtoInstance72.name = "four"
fieldValue73 = x3d.fieldValue()
fieldValue73.name = "ztranslation"
fieldValue73.value = "0 0 2"

ProtoInstance72.fieldValue.append(fieldValue73)
fieldValue74 = x3d.fieldValue()
fieldValue74.name = "x1diffuseColor"
fieldValue74.value = "0 0 1"

ProtoInstance72.fieldValue.append(fieldValue74)
fieldValue75 = x3d.fieldValue()
fieldValue75.name = "x2diffuseColor"
fieldValue75.value = "1 1 0"

ProtoInstance72.fieldValue.append(fieldValue75)

Transform65.children.append(ProtoInstance72)

ProtoBody64.children.append(Transform65)

ProtoDeclare61.ProtoBody = ProtoBody64

Scene7.children.append(ProtoDeclare61)
ProtoInstance76 = x3d.ProtoInstance()
ProtoInstance76.name = "eight"
fieldValue77 = x3d.fieldValue()
fieldValue77.name = "ttranslation"
fieldValue77.value = "0 0 0"

ProtoInstance76.fieldValue.append(fieldValue77)

Scene7.children.append(ProtoInstance76)

X3D0.Scene = Scene7
f = open("././rubik2x2x2_RoundTrip.x3d", "w")
f.write(X3D0.XML())
f.close()
