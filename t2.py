print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Interchange"
X3D0.version = "3.0"
head1 = x3d.head()
component2 = x3d.component()
component2.name = "Networking"
component2.level = 2

head1.children.append(component2)
meta3 = x3d.meta()
meta3.name = "generator"
meta3.content = "view3dscene, https://castle-engine.io/view3dscene.php"

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.name = "source"
meta4.content = "t1.wrl"

head1.children.append(meta4)

X3D0.head = head1
Scene5 = x3d.Scene()
NavigationInfo6 = x3d.NavigationInfo()
NavigationInfo6.type = ["EXAMINE","FLY","WALK"]
NavigationInfo6.speed = 3
NavigationInfo6.avatarSize = [200,200,120]

Scene5.children.append(NavigationInfo6)
WorldInfo7 = x3d.WorldInfo()
WorldInfo7.title = "Arts Mapper"

Scene5.children.append(WorldInfo7)
Viewpoint8 = x3d.Viewpoint()
Viewpoint8.description = "looking North"
Viewpoint8.position = [0,60,110]
Viewpoint8.orientation = [1,0,0,-0.699999988079071]
Viewpoint8.fieldOfView = 0.785398125648499

Scene5.children.append(Viewpoint8)
Viewpoint9 = x3d.Viewpoint()
Viewpoint9.description = "looking East"
Viewpoint9.position = [-140,30,0]
Viewpoint9.orientation = [0,0.400000005960464,0,-1.39999997615814]
Viewpoint9.fieldOfView = 0.785398125648499

Scene5.children.append(Viewpoint9)
Viewpoint10 = x3d.Viewpoint()
Viewpoint10.description = "Overhead"
Viewpoint10.position = [0,150,0]
Viewpoint10.orientation = [1,0,0,-1.57000005245209]
Viewpoint10.fieldOfView = 0.785398125648499

Scene5.children.append(Viewpoint10)
ProtoDeclare11 = x3d.ProtoDeclare()
ProtoDeclare11.name = "org"
ProtoInterface12 = x3d.ProtoInterface()
field13 = x3d.field()
field13.accessType = "initializeOnly"
field13.type = "SFVec3f"
field13.name = "posi"
field13.value = [0,0,0]

ProtoInterface12.field.append(field13)
field14 = x3d.field()
field14.accessType = "initializeOnly"
field14.type = "SFColor"
field14.name = "col"
field14.value = [0,0,0]

ProtoInterface12.field.append(field14)

ProtoDeclare11.ProtoInterface = ProtoInterface12
ProtoBody15 = x3d.ProtoBody()
Transform16 = x3d.Transform()
Shape17 = x3d.Shape()
Appearance18 = x3d.Appearance()
Material19 = x3d.Material()
Material19.transparency = 0.400000005960464
IS20 = x3d.IS()
connect21 = x3d.connect()
connect21.nodeField = "emissiveColor"
connect21.protoField = "col"

IS20.connect.append(connect21)

Material19.IS = IS20

Appearance18.material = Material19

Shape17.appearance = Appearance18
Sphere22 = x3d.Sphere()
Sphere22.radius = 1.10000002384186

Shape17.geometry = Sphere22

Transform16.children.append(Shape17)
IS23 = x3d.IS()
connect24 = x3d.connect()
connect24.nodeField = "translation"
connect24.protoField = "posi"

IS23.connect.append(connect24)

Transform16.IS = IS23

ProtoBody15.children.append(Transform16)

ProtoDeclare11.ProtoBody = ProtoBody15

Scene5.children.append(ProtoDeclare11)
ProtoDeclare25 = x3d.ProtoDeclare()
ProtoDeclare25.name = "r"
ProtoInterface26 = x3d.ProtoInterface()
field27 = x3d.field()
field27.accessType = "initializeOnly"
field27.type = "SFVec3f"
field27.name = "pos"
field27.value = [0,0,0]

ProtoInterface26.field.append(field27)

ProtoDeclare25.ProtoInterface = ProtoInterface26
ProtoBody28 = x3d.ProtoBody()
ProtoInstance29 = x3d.ProtoInstance()
ProtoInstance29.name = "org"
fieldValue30 = x3d.fieldValue()
fieldValue30.name = "col"
fieldValue30.value = "0 0.300000011920929 1"

ProtoInstance29.fieldValue.append(fieldValue30)
fieldValue31 = x3d.fieldValue()
fieldValue31.name = "posi"

ProtoInstance29.fieldValue.append(fieldValue31)
IS32 = x3d.IS()
connect33 = x3d.connect()
connect33.nodeField = "posi"
connect33.protoField = "pos"

IS32.connect.append(connect33)

ProtoInstance29.IS = IS32

ProtoBody28.children.append(ProtoInstance29)

ProtoDeclare25.ProtoBody = ProtoBody28

Scene5.children.append(ProtoDeclare25)
Anchor34 = x3d.Anchor()
Anchor34.url = ["javascript:window.open('./data/574.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor34.description = "High Peak Community Arts"
ProtoInstance35 = x3d.ProtoInstance()
ProtoInstance35.name = "r"
fieldValue36 = x3d.fieldValue()
fieldValue36.name = "pos"
fieldValue36.value = "400 0.100000001490116 -385"

ProtoInstance35.fieldValue.append(fieldValue36)

Anchor34.children.append(ProtoInstance35)

Scene5.children.append(Anchor34)

X3D0.Scene = Scene5
f = open("t2_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
