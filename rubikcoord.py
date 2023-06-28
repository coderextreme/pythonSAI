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
Background10 = x3d.Background()
Background10.skyColor = [1,1,1]

Scene7.children.append(Background10)
ProtoDeclare11 = x3d.ProtoDeclare()
ProtoDeclare11.name = "boxproto"
ProtoInterface12 = x3d.ProtoInterface()
field13 = x3d.field()
field13.name = "xtranslation"
field13.accessType = "inputOutput"
field13.type = "SFVec3f"
field13.value = [0,0,0]

ProtoInterface12.field.append(field13)
field14 = x3d.field()
field14.name = "diffuseColor"
field14.accessType = "inputOutput"
field14.type = "SFColor"
field14.value = [1,1,1]

ProtoInterface12.field.append(field14)

ProtoDeclare11.ProtoInterface = ProtoInterface12
ProtoBody15 = x3d.ProtoBody()
Transform16 = x3d.Transform()
IS17 = x3d.IS()
connect18 = x3d.connect()
connect18.nodeField = "translation"
connect18.protoField = "xtranslation"

IS17.connect.append(connect18)

Transform16.IS = IS17
Shape19 = x3d.Shape()
Box20 = x3d.Box()

Shape19.geometry = Box20
Appearance21 = x3d.Appearance()
Material22 = x3d.Material()
Material22.diffuseColor = [1,1,1]
IS23 = x3d.IS()
connect24 = x3d.connect()
connect24.nodeField = "diffuseColor"
connect24.protoField = "diffuseColor"

IS23.connect.append(connect24)

Material22.IS = IS23

Appearance21.material = Material22

Shape19.appearance = Appearance21

Transform16.children.append(Shape19)

ProtoBody15.children.append(Transform16)

ProtoDeclare11.ProtoBody = ProtoBody15

Scene7.children.append(ProtoDeclare11)
ProtoDeclare25 = x3d.ProtoDeclare()
ProtoDeclare25.name = "two"
ProtoInterface26 = x3d.ProtoInterface()
field27 = x3d.field()
field27.name = "ytranslation"
field27.accessType = "inputOutput"
field27.type = "SFVec3f"
field27.value = [0,0,0]

ProtoInterface26.field.append(field27)
field28 = x3d.field()
field28.name = "diffuseColor"
field28.accessType = "inputOutput"
field28.type = "SFColor"
field28.value = [1,0,0]

ProtoInterface26.field.append(field28)

ProtoDeclare25.ProtoInterface = ProtoInterface26
ProtoBody29 = x3d.ProtoBody()
Transform30 = x3d.Transform()
IS31 = x3d.IS()
connect32 = x3d.connect()
connect32.nodeField = "translation"
connect32.protoField = "ytranslation"

IS31.connect.append(connect32)

Transform30.IS = IS31
ProtoInstance33 = x3d.ProtoInstance()
ProtoInstance33.name = "boxproto"
fieldValue34 = x3d.fieldValue()
fieldValue34.name = "xtranslation"
fieldValue34.value = "0 0 0"

ProtoInstance33.fieldValue.append(fieldValue34)
fieldValue35 = x3d.fieldValue()
fieldValue35.name = "diffuseColor"
fieldValue35.value = "1 0 0"
IS36 = x3d.IS()
connect37 = x3d.connect()
connect37.nodeField = "diffuseColor"
connect37.protoField = "diffuseColor"

IS36.connect.append(connect37)

fieldValue35.children.append(IS36)

ProtoInstance33.fieldValue.append(fieldValue35)

Transform30.children.append(ProtoInstance33)
ProtoInstance38 = x3d.ProtoInstance()
ProtoInstance38.name = "boxproto"
fieldValue39 = x3d.fieldValue()
fieldValue39.name = "xtranslation"
fieldValue39.value = "2 0 0"

ProtoInstance38.fieldValue.append(fieldValue39)
fieldValue40 = x3d.fieldValue()
fieldValue40.name = "diffuseColor"
fieldValue40.value = "1 0 0"
IS41 = x3d.IS()
connect42 = x3d.connect()
connect42.nodeField = "diffuseColor"
connect42.protoField = "diffuseColor"

IS41.connect.append(connect42)

fieldValue40.children.append(IS41)

ProtoInstance38.fieldValue.append(fieldValue40)

Transform30.children.append(ProtoInstance38)

ProtoBody29.children.append(Transform30)

ProtoDeclare25.ProtoBody = ProtoBody29

Scene7.children.append(ProtoDeclare25)
ProtoDeclare43 = x3d.ProtoDeclare()
ProtoDeclare43.name = "four"
ProtoInterface44 = x3d.ProtoInterface()
field45 = x3d.field()
field45.name = "ztranslation"
field45.accessType = "inputOutput"
field45.type = "SFVec3f"
field45.value = [0,0,0]

ProtoInterface44.field.append(field45)
field46 = x3d.field()
field46.name = "x1diffuseColor"
field46.accessType = "inputOutput"
field46.type = "SFColor"
field46.value = [1,0,0]

ProtoInterface44.field.append(field46)
field47 = x3d.field()
field47.name = "x2diffuseColor"
field47.accessType = "inputOutput"
field47.type = "SFColor"
field47.value = [0,1,0]

ProtoInterface44.field.append(field47)

ProtoDeclare43.ProtoInterface = ProtoInterface44
ProtoBody48 = x3d.ProtoBody()
Transform49 = x3d.Transform()
IS50 = x3d.IS()
connect51 = x3d.connect()
connect51.nodeField = "translation"
connect51.protoField = "ztranslation"

IS50.connect.append(connect51)

Transform49.IS = IS50
ProtoInstance52 = x3d.ProtoInstance()
ProtoInstance52.name = "two"
fieldValue53 = x3d.fieldValue()
fieldValue53.name = "ytranslation"
fieldValue53.value = "0 0 0"

ProtoInstance52.fieldValue.append(fieldValue53)
fieldValue54 = x3d.fieldValue()
fieldValue54.name = "diffuseColor"
fieldValue54.value = "1 0 0"
IS55 = x3d.IS()
connect56 = x3d.connect()
connect56.nodeField = "diffuseColor"
connect56.protoField = "x1diffuseColor"

IS55.connect.append(connect56)

fieldValue54.children.append(IS55)

ProtoInstance52.fieldValue.append(fieldValue54)

Transform49.children.append(ProtoInstance52)
ProtoInstance57 = x3d.ProtoInstance()
ProtoInstance57.name = "two"
fieldValue58 = x3d.fieldValue()
fieldValue58.name = "ytranslation"
fieldValue58.value = "0 2 0"

ProtoInstance57.fieldValue.append(fieldValue58)
fieldValue59 = x3d.fieldValue()
fieldValue59.name = "diffuseColor"
fieldValue59.value = "0 1 0"
IS60 = x3d.IS()
connect61 = x3d.connect()
connect61.nodeField = "diffuseColor"
connect61.protoField = "x2diffuseColor"

IS60.connect.append(connect61)

fieldValue59.children.append(IS60)

ProtoInstance57.fieldValue.append(fieldValue59)

Transform49.children.append(ProtoInstance57)

ProtoBody48.children.append(Transform49)

ProtoDeclare43.ProtoBody = ProtoBody48

Scene7.children.append(ProtoDeclare43)
ProtoDeclare62 = x3d.ProtoDeclare()
ProtoDeclare62.name = "eight"
ProtoInterface63 = x3d.ProtoInterface()
field64 = x3d.field()
field64.name = "ttranslation"
field64.accessType = "inputOutput"
field64.type = "SFVec3f"
field64.value = [0,0,0]

ProtoInterface63.field.append(field64)

ProtoDeclare62.ProtoInterface = ProtoInterface63
ProtoBody65 = x3d.ProtoBody()
Transform66 = x3d.Transform()
IS67 = x3d.IS()
connect68 = x3d.connect()
connect68.nodeField = "translation"
connect68.protoField = "ttranslation"

IS67.connect.append(connect68)

Transform66.IS = IS67
ProtoInstance69 = x3d.ProtoInstance()
ProtoInstance69.name = "four"
fieldValue70 = x3d.fieldValue()
fieldValue70.name = "ztranslation"
fieldValue70.value = "0 0 0"

ProtoInstance69.fieldValue.append(fieldValue70)
fieldValue71 = x3d.fieldValue()
fieldValue71.name = "x1diffuseColor"
fieldValue71.value = "1 0 0"

ProtoInstance69.fieldValue.append(fieldValue71)
fieldValue72 = x3d.fieldValue()
fieldValue72.name = "x2diffuseColor"
fieldValue72.value = "0 1 0"

ProtoInstance69.fieldValue.append(fieldValue72)

Transform66.children.append(ProtoInstance69)
ProtoInstance73 = x3d.ProtoInstance()
ProtoInstance73.name = "four"
fieldValue74 = x3d.fieldValue()
fieldValue74.name = "ztranslation"
fieldValue74.value = "0 0 2"

ProtoInstance73.fieldValue.append(fieldValue74)
fieldValue75 = x3d.fieldValue()
fieldValue75.name = "x1diffuseColor"
fieldValue75.value = "0 0 1"

ProtoInstance73.fieldValue.append(fieldValue75)
fieldValue76 = x3d.fieldValue()
fieldValue76.name = "x2diffuseColor"
fieldValue76.value = "1 1 0"

ProtoInstance73.fieldValue.append(fieldValue76)

Transform66.children.append(ProtoInstance73)

ProtoBody65.children.append(Transform66)

ProtoDeclare62.ProtoBody = ProtoBody65

Scene7.children.append(ProtoDeclare62)
ProtoInstance77 = x3d.ProtoInstance()
ProtoInstance77.name = "eight"
fieldValue78 = x3d.fieldValue()
fieldValue78.name = "ttranslation"
fieldValue78.value = "0 0 0"

ProtoInstance77.fieldValue.append(fieldValue78)

Scene7.children.append(ProtoInstance77)
#Axes below <Group> <Group DEF='ArrowGreen'> <Shape> <Cylinder DEF='ArrowCylinder' radius='.025' top='false'/> <Appearance DEF='Green'> <Material diffuseColor='0 0 0'/> </Appearance> </Shape> <Transform translation='0 1 0'> <Shape> <Cone DEF='ArrowCone' bottomRadius='.05' height='.1'/> <Appearance USE='Green'/> </Shape> </Transform> </Group> <Transform translation='0 1.08 0'> <Billboard> <Shape> <Appearance DEF='LABEL_APPEARANCE'> <Material diffuseColor='0 0 0'/> </Appearance> <Text string='\"Y\"'> <FontStyle DEF='LABEL_FONT' family='\"SANS\"' justify='\"MIDDLE\" \"MIDDLE\"' size='.2'/> </Text> </Shape> </Billboard> </Transform> </Group> <Transform rotation='0 0 1 -1.57079'> <Group> <Group DEF='ArrowRed'> <Shape> <Cylinder USE='ArrowCylinder'/> <Appearance DEF='Red'> <Material diffuseColor='0 0 0'/> </Appearance> </Shape> <Transform translation='0 1 0'> <Shape> <Cone USE='ArrowCone'/> <Appearance USE='Red'/> </Shape> </Transform> </Group> <Transform rotation='0 0 1 1.57079' translation='.072 1.1 0'> <Billboard> <Shape> <Appearance USE='LABEL_APPEARANCE'/> <Text string='\"X\"'> <FontStyle USE='LABEL_FONT'/> </Text> </Shape> </Billboard> </Transform> </Group> </Transform> <Transform rotation='1 0 0 1.57079'> <Group> <Group DEF='ArrowBlue'> <Shape> <Cylinder USE='ArrowCylinder'/> <Appearance DEF='Blue'> <Material diffuseColor='0 0 0'/> </Appearance> </Shape> <Transform translation='0 1 0'> <Shape> <Cone USE='ArrowCone'/> <Appearance USE='Blue'/> </Shape> </Transform> </Group> <Transform rotation='1 0 0 -1.57079' translation='0 1.1 .072'> <Billboard> <Shape> <Appearance USE='LABEL_APPEARANCE'/> <Text string='\"Z\"'> <FontStyle USE='LABEL_FONT'/> </Text> </Shape> </Billboard> </Transform> </Group> </Transform>

X3D0.Scene = Scene7
f = open("././rubikcoord_RoundTrip.x3d", "w")
f.write(X3D0.XML())
f.close()
