print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Interchange"
X3D0.version = "3.0"
head1 = x3d.head()
meta2 = x3d.meta()
meta2.name = "generator"
meta2.content = "tovrmlx3d, http://castle-engine.sourceforge.net/view3dscene.php#section_converting"

head1.children.append(meta2)
meta3 = x3d.meta()
meta3.name = "source"
meta3.content = "t1.wrl"

head1.children.append(meta3)

X3D0.head = head1
Scene4 = x3d.Scene()
NavigationInfo5 = x3d.NavigationInfo()
NavigationInfo5.type = ["EXAMINE","FLY","WALK"]
NavigationInfo5.speed = 3
NavigationInfo5.avatarSize = [200,200,120]

Scene4.children.append(NavigationInfo5)
WorldInfo6 = x3d.WorldInfo()
WorldInfo6.title = "Arts Mapper"

Scene4.children.append(WorldInfo6)
Viewpoint7 = x3d.Viewpoint()
Viewpoint7.description = "looking North"
Viewpoint7.position = [0,60,110]
Viewpoint7.orientation = [1,0,0,-0.699999988079071]
Viewpoint7.fieldOfView = 0.7853981256484985

Scene4.children.append(Viewpoint7)
Viewpoint8 = x3d.Viewpoint()
Viewpoint8.description = "looking East"
Viewpoint8.position = [-140,30,0]
Viewpoint8.orientation = [0,0.4000000059604645,0,-1.399999976158142]
Viewpoint8.fieldOfView = 0.7853981256484985

Scene4.children.append(Viewpoint8)
Viewpoint9 = x3d.Viewpoint()
Viewpoint9.description = "Overhead"
Viewpoint9.position = [0,150,0]
Viewpoint9.orientation = [1,0,0,-1.5700000524520874]
Viewpoint9.fieldOfView = 0.7853981256484985

Scene4.children.append(Viewpoint9)
ProtoDeclare10 = x3d.ProtoDeclare()
ProtoDeclare10.name = "school"
ProtoInterface11 = x3d.ProtoInterface()
field12 = x3d.field()
field12.name = "pos"
field12.accessType = "initializeOnly"
field12.type = "SFVec3f"
field12.value = [0,0,0]

ProtoInterface11.field.append(field12)

ProtoDeclare10.ProtoInterface = ProtoInterface11
ProtoBody13 = x3d.ProtoBody()
Transform14 = x3d.Transform()
Shape15 = x3d.Shape()
Appearance16 = x3d.Appearance()
Material17 = x3d.Material()
Material17.transparency = 0.20000000298023224
Material17.diffuseColor = [0.5,0,1]

Appearance16.material = Material17

Shape15.appearance = Appearance16
IndexedFaceSet18 = x3d.IndexedFaceSet()
IndexedFaceSet18.coordIndex = [0,1,4,-1,1,2,4,-1,2,3,4,-1,3,0,4,-1,0,3,2,1,-1]
Coordinate19 = x3d.Coordinate()

IndexedFaceSet18.coord = Coordinate19

Shape15.geometry = IndexedFaceSet18

Transform14.children.append(Shape15)
IS20 = x3d.IS()
connect21 = x3d.connect()
connect21.nodeField = "translation"
connect21.protoField = "pos"

IS20.connect.append(connect21)

Transform14.IS = IS20

ProtoBody13.children.append(Transform14)

ProtoDeclare10.ProtoBody = ProtoBody13

Scene4.children.append(ProtoDeclare10)
ProtoDeclare22 = x3d.ProtoDeclare()
ProtoDeclare22.name = "institute"
ProtoInterface23 = x3d.ProtoInterface()
field24 = x3d.field()
field24.name = "pos"
field24.accessType = "initializeOnly"
field24.type = "SFVec3f"
field24.value = [0,0,0]

ProtoInterface23.field.append(field24)

ProtoDeclare22.ProtoInterface = ProtoInterface23
ProtoBody25 = x3d.ProtoBody()
Transform26 = x3d.Transform()
Shape27 = x3d.Shape()
Appearance28 = x3d.Appearance()
Material29 = x3d.Material()
Material29.transparency = 0.20000000298023224
Material29.diffuseColor = [1,1,0]

Appearance28.material = Material29

Shape27.appearance = Appearance28
Box30 = x3d.Box()
Box30.size = [0.699999988079071,0.699999988079071,0.699999988079071]

Shape27.geometry = Box30

Transform26.children.append(Shape27)
IS31 = x3d.IS()
connect32 = x3d.connect()
connect32.nodeField = "translation"
connect32.protoField = "pos"

IS31.connect.append(connect32)

Transform26.IS = IS31

ProtoBody25.children.append(Transform26)

ProtoDeclare22.ProtoBody = ProtoBody25

Scene4.children.append(ProtoDeclare22)
ProtoDeclare33 = x3d.ProtoDeclare()
ProtoDeclare33.name = "disart_org"
ProtoInterface34 = x3d.ProtoInterface()
field35 = x3d.field()
field35.name = "pos"
field35.accessType = "initializeOnly"
field35.type = "SFVec3f"
field35.value = [0,0,0]

ProtoInterface34.field.append(field35)

ProtoDeclare33.ProtoInterface = ProtoInterface34
ProtoBody36 = x3d.ProtoBody()
Transform37 = x3d.Transform()
Shape38 = x3d.Shape()
Appearance39 = x3d.Appearance()
Material40 = x3d.Material()
Material40.diffuseColor = [1,1,0]

Appearance39.material = Material40

Shape38.appearance = Appearance39
Sphere41 = x3d.Sphere()
Sphere41.radius = 0.699999988079071

Shape38.geometry = Sphere41

Transform37.children.append(Shape38)
IS42 = x3d.IS()
connect43 = x3d.connect()
connect43.nodeField = "translation"
connect43.protoField = "pos"

IS42.connect.append(connect43)

Transform37.IS = IS42

ProtoBody36.children.append(Transform37)

ProtoDeclare33.ProtoBody = ProtoBody36

Scene4.children.append(ProtoDeclare33)
ProtoDeclare44 = x3d.ProtoDeclare()
ProtoDeclare44.name = "org"
ProtoInterface45 = x3d.ProtoInterface()
field46 = x3d.field()
field46.name = "posi"
field46.accessType = "initializeOnly"
field46.type = "SFVec3f"
field46.value = [0,0,0]

ProtoInterface45.field.append(field46)
field47 = x3d.field()
field47.name = "col"
field47.accessType = "initializeOnly"
field47.type = "SFColor"
field47.value = [0,0,0]

ProtoInterface45.field.append(field47)

ProtoDeclare44.ProtoInterface = ProtoInterface45
ProtoBody48 = x3d.ProtoBody()
Transform49 = x3d.Transform()
Shape50 = x3d.Shape()
Appearance51 = x3d.Appearance()
Material52 = x3d.Material()
Material52.transparency = 0.4000000059604645
IS53 = x3d.IS()
connect54 = x3d.connect()
connect54.nodeField = "emissiveColor"
connect54.protoField = "col"

IS53.connect.append(connect54)

Material52.IS = IS53

Appearance51.material = Material52

Shape50.appearance = Appearance51
Sphere55 = x3d.Sphere()
Sphere55.radius = 1.100000023841858

Shape50.geometry = Sphere55

Transform49.children.append(Shape50)
IS56 = x3d.IS()
connect57 = x3d.connect()
connect57.nodeField = "translation"
connect57.protoField = "posi"

IS56.connect.append(connect57)

Transform49.IS = IS56

ProtoBody48.children.append(Transform49)

ProtoDeclare44.ProtoBody = ProtoBody48

Scene4.children.append(ProtoDeclare44)
ProtoDeclare58 = x3d.ProtoDeclare()
ProtoDeclare58.name = "l"
ProtoInterface59 = x3d.ProtoInterface()
field60 = x3d.field()
field60.name = "pos"
field60.accessType = "initializeOnly"
field60.type = "SFVec3f"
field60.value = [0,0,0]

ProtoInterface59.field.append(field60)

ProtoDeclare58.ProtoInterface = ProtoInterface59
ProtoBody61 = x3d.ProtoBody()
ProtoInstance62 = x3d.ProtoInstance()
ProtoInstance62.name = "org"
fieldValue63 = x3d.fieldValue()
fieldValue63.name = "col"
fieldValue63.value = "0 0.6000000238418579 0"

ProtoInstance62.fieldValue.append(fieldValue63)
IS64 = x3d.IS()
connect65 = x3d.connect()
connect65.nodeField = "posi"
connect65.protoField = "pos"

IS64.connect.append(connect65)

ProtoInstance62.IS = IS64

ProtoBody61.children.append(ProtoInstance62)

ProtoDeclare58.ProtoBody = ProtoBody61

Scene4.children.append(ProtoDeclare58)
ProtoDeclare66 = x3d.ProtoDeclare()
ProtoDeclare66.name = "r"
ProtoInterface67 = x3d.ProtoInterface()
field68 = x3d.field()
field68.name = "pos"
field68.accessType = "initializeOnly"
field68.type = "SFVec3f"
field68.value = [0,0,0]

ProtoInterface67.field.append(field68)

ProtoDeclare66.ProtoInterface = ProtoInterface67
ProtoBody69 = x3d.ProtoBody()
ProtoInstance70 = x3d.ProtoInstance()
ProtoInstance70.name = "org"
fieldValue71 = x3d.fieldValue()
fieldValue71.name = "col"
fieldValue71.value = "0 0.30000001192092896 1"

ProtoInstance70.fieldValue.append(fieldValue71)
IS72 = x3d.IS()
connect73 = x3d.connect()
connect73.nodeField = "posi"
connect73.protoField = "pos"

IS72.connect.append(connect73)

ProtoInstance70.IS = IS72

ProtoBody69.children.append(ProtoInstance70)

ProtoDeclare66.ProtoBody = ProtoBody69

Scene4.children.append(ProtoDeclare66)
ProtoDeclare74 = x3d.ProtoDeclare()
ProtoDeclare74.name = "n"
ProtoInterface75 = x3d.ProtoInterface()
field76 = x3d.field()
field76.name = "pos"
field76.accessType = "initializeOnly"
field76.type = "SFVec3f"
field76.value = [0,0,0]

ProtoInterface75.field.append(field76)

ProtoDeclare74.ProtoInterface = ProtoInterface75
ProtoBody77 = x3d.ProtoBody()
ProtoInstance78 = x3d.ProtoInstance()
ProtoInstance78.name = "org"
fieldValue79 = x3d.fieldValue()
fieldValue79.name = "col"
fieldValue79.value = "1 0 0.20000000298023224"

ProtoInstance78.fieldValue.append(fieldValue79)
IS80 = x3d.IS()
connect81 = x3d.connect()
connect81.nodeField = "posi"
connect81.protoField = "pos"

IS80.connect.append(connect81)

ProtoInstance78.IS = IS80

ProtoBody77.children.append(ProtoInstance78)

ProtoDeclare74.ProtoBody = ProtoBody77

Scene4.children.append(ProtoDeclare74)
ProtoDeclare82 = x3d.ProtoDeclare()
ProtoDeclare82.name = "i"
ProtoInterface83 = x3d.ProtoInterface()
field84 = x3d.field()
field84.name = "pos"
field84.accessType = "initializeOnly"
field84.type = "SFVec3f"
field84.value = [0,0,0]

ProtoInterface83.field.append(field84)

ProtoDeclare82.ProtoInterface = ProtoInterface83
ProtoBody85 = x3d.ProtoBody()
ProtoInstance86 = x3d.ProtoInstance()
ProtoInstance86.name = "org"
fieldValue87 = x3d.fieldValue()
fieldValue87.name = "col"
fieldValue87.value = "0.6000000238418579 0 0.6000000238418579"

ProtoInstance86.fieldValue.append(fieldValue87)
IS88 = x3d.IS()
connect89 = x3d.connect()
connect89.nodeField = "posi"
connect89.protoField = "pos"

IS88.connect.append(connect89)

ProtoInstance86.IS = IS88

ProtoBody85.children.append(ProtoInstance86)

ProtoDeclare82.ProtoBody = ProtoBody85

Scene4.children.append(ProtoDeclare82)
Transform90 = x3d.Transform()
Transform90.translation = [-468,0,315]
Inline91 = x3d.Inline()
Inline91.url = ["t.wrl"]

Transform90.children.append(Inline91)
Anchor92 = x3d.Anchor()
Anchor92.url = ["javascript:window.open('./data/566.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor92.description = "Derby Women's Centre"
ProtoInstance93 = x3d.ProtoInstance()
ProtoInstance93.name = "institute"
fieldValue94 = x3d.fieldValue()
fieldValue94.name = "pos"
fieldValue94.value = "435.29998779296875 0.10000000149011612 -335.6000061035156"

ProtoInstance93.fieldValue.append(fieldValue94)

Anchor92.children.append(ProtoInstance93)

Transform90.children.append(Anchor92)
Anchor95 = x3d.Anchor()
Anchor95.url = ["javascript:window.open('./data/574.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor95.description = "High Peak Community Arts"
ProtoInstance96 = x3d.ProtoInstance()
ProtoInstance96.name = "r"
fieldValue97 = x3d.fieldValue()
fieldValue97.name = "pos"
fieldValue97.value = "400 0.10000000149011612 -385"

ProtoInstance96.fieldValue.append(fieldValue97)

Anchor95.children.append(ProtoInstance96)

Transform90.children.append(Anchor95)
Anchor98 = x3d.Anchor()
Anchor98.url = ["javascript:window.open('./data/576.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor98.description = "Charlesworth Primary School"
ProtoInstance99 = x3d.ProtoInstance()
ProtoInstance99.name = "school"
fieldValue100 = x3d.fieldValue()
fieldValue100.name = "pos"
fieldValue100.value = "400.6000061035156 0.10000000149011612 -392.8999938964844"

ProtoInstance99.fieldValue.append(fieldValue100)

Anchor98.children.append(ProtoInstance99)

Transform90.children.append(Anchor98)
Anchor101 = x3d.Anchor()
Anchor101.url = ["javascript:window.open('./data/579.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor101.description = "Hope Valley College"
ProtoInstance102 = x3d.ProtoInstance()
ProtoInstance102.name = "school"
fieldValue103 = x3d.fieldValue()
fieldValue103.name = "pos"
fieldValue103.value = "416.70001220703125 0.10000000149011612 -383.3999938964844"

ProtoInstance102.fieldValue.append(fieldValue103)

Anchor101.children.append(ProtoInstance102)

Transform90.children.append(Anchor101)
Anchor104 = x3d.Anchor()
Anchor104.url = ["javascript:window.open('./data/583.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor104.description = "People Express"
ProtoInstance105 = x3d.ProtoInstance()
ProtoInstance105.name = "i"
fieldValue106 = x3d.fieldValue()
fieldValue106.name = "pos"
fieldValue106.value = "429.8999938964844 0.10000000149011612 -319.6000061035156"

ProtoInstance105.fieldValue.append(fieldValue106)

Anchor104.children.append(ProtoInstance105)

Transform90.children.append(Anchor104)
Anchor107 = x3d.Anchor()
Anchor107.url = ["javascript:window.open('./data/589.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor107.description = "QArts/Studios"
ProtoInstance108 = x3d.ProtoInstance()
ProtoInstance108.name = "i"
fieldValue109 = x3d.fieldValue()
fieldValue109.name = "pos"
fieldValue109.value = "430 0.10000000149011612 -335"

ProtoInstance108.fieldValue.append(fieldValue109)

Anchor107.children.append(ProtoInstance108)

Transform90.children.append(Anchor107)
Anchor110 = x3d.Anchor()
Anchor110.url = ["javascript:window.open('./data/591.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor110.description = "Stroke Unit, Derbyshire Royal Infirmary"
ProtoInstance111 = x3d.ProtoInstance()
ProtoInstance111.name = "institute"
fieldValue112 = x3d.fieldValue()
fieldValue112.name = "pos"
fieldValue112.value = "435.79998779296875 0.10000000149011612 -335.29998779296875"

ProtoInstance111.fieldValue.append(fieldValue112)

Anchor110.children.append(ProtoInstance111)

Transform90.children.append(Anchor110)
Anchor113 = x3d.Anchor()
Anchor113.url = ["javascript:window.open('./data/592.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor113.description = "Park View Primary, Derby"
ProtoInstance114 = x3d.ProtoInstance()
ProtoInstance114.name = "school"
fieldValue115 = x3d.fieldValue()
fieldValue115.name = "pos"
fieldValue115.value = "438.29998779296875 0.10000000149011612 -338.6000061035156"

ProtoInstance114.fieldValue.append(fieldValue115)

Anchor113.children.append(ProtoInstance114)

Transform90.children.append(Anchor113)
Anchor116 = x3d.Anchor()
Anchor116.url = ["javascript:window.open('./data/593.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor116.description = "First Movement"
ProtoInstance117 = x3d.ProtoInstance()
ProtoInstance117.name = "n"
fieldValue118 = x3d.fieldValue()
fieldValue118.name = "pos"
fieldValue118.value = "429.8999938964844 0.10000000149011612 -360.29998779296875"

ProtoInstance117.fieldValue.append(fieldValue118)

Anchor116.children.append(ProtoInstance117)

Transform90.children.append(Anchor116)
Anchor119 = x3d.Anchor()
Anchor119.url = ["javascript:window.open('./data/594.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor119.description = "St. Benedict R.C. School, Visual Impairment Unit"
ProtoInstance120 = x3d.ProtoInstance()
ProtoInstance120.name = "institute"
fieldValue121 = x3d.fieldValue()
fieldValue121.name = "pos"
fieldValue121.value = "434.6000061035156 0.10000000149011612 -338.6000061035156"

ProtoInstance120.fieldValue.append(fieldValue121)

Anchor119.children.append(ProtoInstance120)

Transform90.children.append(Anchor119)
Anchor122 = x3d.Anchor()
Anchor122.url = ["javascript:window.open('./data/595.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor122.description = "Beckett Primary, Derby"
ProtoInstance123 = x3d.ProtoInstance()
ProtoInstance123.name = "school"
fieldValue124 = x3d.fieldValue()
fieldValue124.name = "pos"
fieldValue124.value = "434.79998779296875 0.10000000149011612 -336"

ProtoInstance123.fieldValue.append(fieldValue124)

Anchor122.children.append(ProtoInstance123)

Transform90.children.append(Anchor122)
Anchor125 = x3d.Anchor()
Anchor125.url = ["javascript:window.open('./data/597.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor125.description = "Brackensdale Junior School, Communty Unit"
ProtoInstance126 = x3d.ProtoInstance()
ProtoInstance126.name = "institute"
fieldValue127 = x3d.fieldValue()
fieldValue127.name = "pos"
fieldValue127.value = "432.70001220703125 0.10000000149011612 -336.6000061035156"

ProtoInstance126.fieldValue.append(fieldValue127)

Anchor125.children.append(ProtoInstance126)

Transform90.children.append(Anchor125)
Anchor128 = x3d.Anchor()
Anchor128.url = ["javascript:window.open('./data/598.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor128.description = "Moorhead Primary, Derby"
ProtoInstance129 = x3d.ProtoInstance()
ProtoInstance129.name = "school"
fieldValue130 = x3d.fieldValue()
fieldValue130.name = "pos"
fieldValue130.value = "437.6000061035156 0.10000000149011612 -332.6000061035156"

ProtoInstance129.fieldValue.append(fieldValue130)

Anchor128.children.append(ProtoInstance129)

Transform90.children.append(Anchor128)
Anchor131 = x3d.Anchor()
Anchor131.url = ["javascript:window.open('./data/600.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor131.description = "Derby Deaf Club"
ProtoInstance132 = x3d.ProtoInstance()
ProtoInstance132.name = "institute"
fieldValue133 = x3d.fieldValue()
fieldValue133.name = "pos"
fieldValue133.value = "434.70001220703125 0.10000000149011612 -336.8999938964844"

ProtoInstance132.fieldValue.append(fieldValue133)

Anchor131.children.append(ProtoInstance132)

Transform90.children.append(Anchor131)
Anchor134 = x3d.Anchor()
Anchor134.url = ["javascript:window.open('./data/601.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor134.description = "Nightingale Junior, Derby"
ProtoInstance135 = x3d.ProtoInstance()
ProtoInstance135.name = "school"
fieldValue136 = x3d.fieldValue()
fieldValue136.name = "pos"
fieldValue136.value = "436.29998779296875 0.10000000149011612 -333.3999938964844"

ProtoInstance135.fieldValue.append(fieldValue136)

Anchor134.children.append(ProtoInstance135)

Transform90.children.append(Anchor134)
Anchor137 = x3d.Anchor()
Anchor137.url = ["javascript:window.open('./data/603.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor137.description = "St Mary's Primary, Derby"
ProtoInstance138 = x3d.ProtoInstance()
ProtoInstance138.name = "school"
fieldValue139 = x3d.fieldValue()
fieldValue139.name = "pos"
fieldValue139.value = "435.20001220703125 0.10000000149011612 -336.79998779296875"

ProtoInstance138.fieldValue.append(fieldValue139)

Anchor137.children.append(ProtoInstance138)

Transform90.children.append(Anchor137)
Anchor140 = x3d.Anchor()
Anchor140.url = ["javascript:window.open('./data/604.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor140.description = "Griffe Field Primary, Derby"
ProtoInstance141 = x3d.ProtoInstance()
ProtoInstance141.name = "school"
fieldValue142 = x3d.fieldValue()
fieldValue142.name = "pos"
fieldValue142.value = "432.5 0.10000000149011612 -332.5"

ProtoInstance141.fieldValue.append(fieldValue142)

Anchor140.children.append(ProtoInstance141)

Transform90.children.append(Anchor140)
Anchor143 = x3d.Anchor()
Anchor143.url = ["javascript:window.open('./data/605.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor143.description = "Leicester Road Day Centre, Melton Mowbray"
ProtoInstance144 = x3d.ProtoInstance()
ProtoInstance144.name = "institute"
fieldValue145 = x3d.fieldValue()
fieldValue145.name = "pos"
fieldValue145.value = "474.70001220703125 0.10000000149011612 -318.79998779296875"

ProtoInstance144.fieldValue.append(fieldValue145)

Anchor143.children.append(ProtoInstance144)

Transform90.children.append(Anchor143)
Anchor146 = x3d.Anchor()
Anchor146.url = ["javascript:window.open('./data/606.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor146.description = "Ivy House Special School, Derby"
ProtoInstance147 = x3d.ProtoInstance()
ProtoInstance147.name = "school"
fieldValue148 = x3d.fieldValue()
fieldValue148.name = "pos"
fieldValue148.value = "436.1000061035156 0.10000000149011612 -334.8999938964844"

ProtoInstance147.fieldValue.append(fieldValue148)

Anchor146.children.append(ProtoInstance147)

Transform90.children.append(Anchor146)
Anchor149 = x3d.Anchor()
Anchor149.url = ["javascript:window.open('./data/607.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor149.description = "Oakham Day Centre, Rutland"
ProtoInstance150 = x3d.ProtoInstance()
ProtoInstance150.name = "institute"
fieldValue151 = x3d.fieldValue()
fieldValue151.name = "pos"
fieldValue151.value = "485.6000061035156 0.10000000149011612 -309"

ProtoInstance150.fieldValue.append(fieldValue151)

Anchor149.children.append(ProtoInstance150)

Transform90.children.append(Anchor149)
Anchor152 = x3d.Anchor()
Anchor152.url = ["javascript:window.open('./data/608.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor152.description = "Parkwood School, Alfreton"
ProtoInstance153 = x3d.ProtoInstance()
ProtoInstance153.name = "school"
fieldValue154 = x3d.fieldValue()
fieldValue154.name = "pos"
fieldValue154.value = "440.5 0.10000000149011612 -355.5"

ProtoInstance153.fieldValue.append(fieldValue154)

Anchor152.children.append(ProtoInstance153)

Transform90.children.append(Anchor152)
Anchor155 = x3d.Anchor()
Anchor155.url = ["javascript:window.open('./data/609.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor155.description = "Ash Green, Specialist Learning Disability Resource"
ProtoInstance156 = x3d.ProtoInstance()
ProtoInstance156.name = "institute"
fieldValue157 = x3d.fieldValue()
fieldValue157.name = "pos"
fieldValue157.value = "434.79998779296875 0.10000000149011612 -371.5"

ProtoInstance156.fieldValue.append(fieldValue157)

Anchor155.children.append(ProtoInstance156)

Transform90.children.append(Anchor155)
Anchor158 = x3d.Anchor()
Anchor158.url = ["javascript:window.open('./data/610.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor158.description = "Ashgate Croft School, Chesterfield"
ProtoInstance159 = x3d.ProtoInstance()
ProtoInstance159.name = "school"
fieldValue160 = x3d.fieldValue()
fieldValue160.name = "pos"
fieldValue160.value = "436.29998779296875 0.10000000149011612 -371.70001220703125"

ProtoInstance159.fieldValue.append(fieldValue160)

Anchor158.children.append(ProtoInstance159)

Transform90.children.append(Anchor158)
Anchor161 = x3d.Anchor()
Anchor161.url = ["javascript:window.open('./data/611.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor161.description = "Highfields School, Matlock"
ProtoInstance162 = x3d.ProtoInstance()
ProtoInstance162.name = "school"
fieldValue163 = x3d.fieldValue()
fieldValue163.name = "pos"
fieldValue163.value = "431.20001220703125 0.10000000149011612 -361.20001220703125"

ProtoInstance162.fieldValue.append(fieldValue163)

Anchor161.children.append(ProtoInstance162)

Transform90.children.append(Anchor161)
Anchor164 = x3d.Anchor()
Anchor164.url = ["javascript:window.open('./data/612.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor164.description = "City Arts"
ProtoInstance165 = x3d.ProtoInstance()
ProtoInstance165.name = "i"
fieldValue166 = x3d.fieldValue()
fieldValue166.name = "pos"
fieldValue166.value = "455.8999938964844 0.10000000149011612 -341.29998779296875"

ProtoInstance165.fieldValue.append(fieldValue166)

Anchor164.children.append(ProtoInstance165)

Transform90.children.append(Anchor164)
Anchor167 = x3d.Anchor()
Anchor167.url = ["javascript:window.open('./data/615.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor167.description = "Indigo Dance Group (Salamanda Tandem)"
ProtoInstance168 = x3d.ProtoInstance()
ProtoInstance168.name = "r"
fieldValue169 = x3d.fieldValue()
fieldValue169.name = "pos"
fieldValue169.value = "456.1000061035156 0.10000000149011612 -341.5"

ProtoInstance168.fieldValue.append(fieldValue169)

Anchor167.children.append(ProtoInstance168)

Transform90.children.append(Anchor167)
Anchor170 = x3d.Anchor()
Anchor170.url = ["javascript:window.open('./data/623.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor170.description = "Watering Seeds"
ProtoInstance171 = x3d.ProtoInstance()
ProtoInstance171.name = "r"
fieldValue172 = x3d.fieldValue()
fieldValue172.name = "pos"
fieldValue172.value = "454 0.10000000149011612 -361.29998779296875"

ProtoInstance171.fieldValue.append(fieldValue172)

Anchor170.children.append(ProtoInstance171)

Transform90.children.append(Anchor170)
Anchor173 = x3d.Anchor()
Anchor173.url = ["javascript:window.open('./data/625.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor173.description = "Red oaks"
ProtoInstance174 = x3d.ProtoInstance()
ProtoInstance174.name = "institute"
fieldValue175 = x3d.fieldValue()
fieldValue175.name = "pos"
fieldValue175.value = "457.3999938964844 0.10000000149011612 -359.6000061035156"

ProtoInstance174.fieldValue.append(fieldValue175)

Anchor173.children.append(ProtoInstance174)

Transform90.children.append(Anchor173)
Anchor176 = x3d.Anchor()
Anchor176.url = ["javascript:window.open('./data/626.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor176.description = "West Notts College"
ProtoInstance177 = x3d.ProtoInstance()
ProtoInstance177.name = "school"
fieldValue178 = x3d.fieldValue()
fieldValue178.name = "pos"
fieldValue178.value = "454.20001220703125 0.10000000149011612 -358.6000061035156"

ProtoInstance177.fieldValue.append(fieldValue178)

Anchor176.children.append(ProtoInstance177)

Transform90.children.append(Anchor176)
Anchor179 = x3d.Anchor()
Anchor179.url = ["javascript:window.open('./data/628.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor179.description = "Willow Wood Day Centre"
ProtoInstance180 = x3d.ProtoInstance()
ProtoInstance180.name = "institute"
fieldValue181 = x3d.fieldValue()
fieldValue181.name = "pos"
fieldValue181.value = "450.6000061035156 0.10000000149011612 -358.6000061035156"

ProtoInstance180.fieldValue.append(fieldValue181)

Anchor179.children.append(ProtoInstance180)

Transform90.children.append(Anchor179)
Anchor182 = x3d.Anchor()
Anchor182.url = ["javascript:window.open('./data/630.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor182.description = "Fased In The Arts"
ProtoInstance183 = x3d.ProtoInstance()
ProtoInstance183.name = "r"
fieldValue184 = x3d.fieldValue()
fieldValue184.name = "pos"
fieldValue184.value = "440 0.10000000149011612 -350"

ProtoInstance183.fieldValue.append(fieldValue184)

Anchor182.children.append(ProtoInstance183)

Transform90.children.append(Anchor182)
Anchor185 = x3d.Anchor()
Anchor185.url = ["javascript:window.open('./data/633.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor185.description = "27a Access Artspace"
ProtoInstance186 = x3d.ProtoInstance()
ProtoInstance186.name = "n"
fieldValue187 = x3d.fieldValue()
fieldValue187.name = "pos"
fieldValue187.value = "458.8999938964844 0.10000000149011612 -304.29998779296875"

ProtoInstance186.fieldValue.append(fieldValue187)

Anchor185.children.append(ProtoInstance186)

Transform90.children.append(Anchor185)
Anchor188 = x3d.Anchor()
Anchor188.url = ["javascript:window.open('./data/635.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor188.description = "Roman Way Day Centre, Market Harborough"
ProtoInstance189 = x3d.ProtoInstance()
ProtoInstance189.name = "institute"
fieldValue190 = x3d.fieldValue()
fieldValue190.name = "pos"
fieldValue190.value = "473.5 0.10000000149011612 -287.5"

ProtoInstance189.fieldValue.append(fieldValue190)

Anchor188.children.append(ProtoInstance189)

Transform90.children.append(Anchor188)
Anchor191 = x3d.Anchor()
Anchor191.url = ["javascript:window.open('./data/637.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor191.description = "Mosaic, Leicester Disability Services"
ProtoInstance192 = x3d.ProtoInstance()
ProtoInstance192.name = "institute"
fieldValue193 = x3d.fieldValue()
fieldValue193.name = "pos"
fieldValue193.value = "458 0.10000000149011612 -304.5"

ProtoInstance192.fieldValue.append(fieldValue193)

Anchor191.children.append(ProtoInstance192)

Transform90.children.append(Anchor191)
Anchor194 = x3d.Anchor()
Anchor194.url = ["javascript:window.open('./data/638.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor194.description = "Bamboozle Theatre Company"
ProtoInstance195 = x3d.ProtoInstance()
ProtoInstance195.name = "r"
fieldValue196 = x3d.fieldValue()
fieldValue196.name = "pos"
fieldValue196.value = "457.1000061035156 0.10000000149011612 -300.79998779296875"

ProtoInstance195.fieldValue.append(fieldValue196)

Anchor194.children.append(ProtoInstance195)

Transform90.children.append(Anchor194)
Anchor197 = x3d.Anchor()
Anchor197.url = ["javascript:window.open('./data/640.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor197.description = "Ellesmere College, Leicester"
ProtoInstance198 = x3d.ProtoInstance()
ProtoInstance198.name = "school"
fieldValue199 = x3d.fieldValue()
fieldValue199.name = "pos"
fieldValue199.value = "456.79998779296875 0.10000000149011612 -302.6000061035156"

ProtoInstance198.fieldValue.append(fieldValue199)

Anchor197.children.append(ProtoInstance198)

Transform90.children.append(Anchor197)
Anchor200 = x3d.Anchor()
Anchor200.url = ["javascript:window.open('./data/642.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor200.description = "Ashmount School, Loughborough"
ProtoInstance201 = x3d.ProtoInstance()
ProtoInstance201.name = "school"
fieldValue202 = x3d.fieldValue()
fieldValue202.name = "pos"
fieldValue202.value = "453.29998779296875 0.10000000149011612 -318.6000061035156"

ProtoInstance201.fieldValue.append(fieldValue202)

Anchor200.children.append(ProtoInstance201)

Transform90.children.append(Anchor200)
Anchor203 = x3d.Anchor()
Anchor203.url = ["javascript:window.open('./data/648.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor203.description = "Mantle Community Arts"
ProtoInstance204 = x3d.ProtoInstance()
ProtoInstance204.name = "r"
fieldValue205 = x3d.fieldValue()
fieldValue205.name = "pos"
fieldValue205.value = "442.3999938964844 0.10000000149011612 -314.5"

ProtoInstance204.fieldValue.append(fieldValue205)

Anchor203.children.append(ProtoInstance204)

Transform90.children.append(Anchor203)
Anchor206 = x3d.Anchor()
Anchor206.url = ["javascript:window.open('./data/650.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor206.description = "Forrest Way School"
ProtoInstance207 = x3d.ProtoInstance()
ProtoInstance207.name = "school"
fieldValue208 = x3d.fieldValue()
fieldValue208.name = "pos"
fieldValue208.value = "444.6000061035156 0.10000000149011612 -313.70001220703125"

ProtoInstance207.fieldValue.append(fieldValue208)

Anchor206.children.append(ProtoInstance207)

Transform90.children.append(Anchor206)
Anchor209 = x3d.Anchor()
Anchor209.url = ["javascript:window.open('./data/652.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor209.description = "Ibstock Community College"
ProtoInstance210 = x3d.ProtoInstance()
ProtoInstance210.name = "school"
fieldValue211 = x3d.fieldValue()
fieldValue211.name = "pos"
fieldValue211.value = "440.6000061035156 0.10000000149011612 -310.3999938964844"

ProtoInstance210.fieldValue.append(fieldValue211)

Anchor209.children.append(ProtoInstance210)

Transform90.children.append(Anchor209)
Anchor212 = x3d.Anchor()
Anchor212.url = ["javascript:window.open('./data/658.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor212.description = "Artlink East"
ProtoInstance213 = x3d.ProtoInstance()
ProtoInstance213.name = "r"
fieldValue214 = x3d.fieldValue()
fieldValue214.name = "pos"
fieldValue214.value = "491.6000061035156 0.10000000149011612 -335.70001220703125"

ProtoInstance213.fieldValue.append(fieldValue214)

Anchor212.children.append(ProtoInstance213)

Transform90.children.append(Anchor212)
Anchor215 = x3d.Anchor()
Anchor215.url = ["javascript:window.open('./data/660.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor215.description = "United Hospitals and NHS Trust Lincolnshire"
ProtoInstance216 = x3d.ProtoInstance()
ProtoInstance216.name = "institute"
fieldValue217 = x3d.fieldValue()
fieldValue217.name = "pos"
fieldValue217.value = "491.3999938964844 0.10000000149011612 -336.79998779296875"

ProtoInstance216.fieldValue.append(fieldValue217)

Anchor215.children.append(ProtoInstance216)

Transform90.children.append(Anchor215)
Anchor218 = x3d.Anchor()
Anchor218.url = ["javascript:window.open('./data/662.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor218.description = "Ancaster Day Centre"
ProtoInstance219 = x3d.ProtoInstance()
ProtoInstance219.name = "institute"
fieldValue220 = x3d.fieldValue()
fieldValue220.name = "pos"
fieldValue220.value = "496.8999938964844 0.10000000149011612 -368.8999938964844"

ProtoInstance219.fieldValue.append(fieldValue220)

Anchor218.children.append(ProtoInstance219)

Transform90.children.append(Anchor218)
Anchor221 = x3d.Anchor()
Anchor221.url = ["javascript:window.open('./data/665.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor221.description = "Creations"
ProtoInstance222 = x3d.ProtoInstance()
ProtoInstance222.name = "r"
fieldValue223 = x3d.fieldValue()
fieldValue223.name = "pos"
fieldValue223.value = "467 0.10000000149011612 -243.89999389648438"

ProtoInstance222.fieldValue.append(fieldValue223)

Anchor221.children.append(ProtoInstance222)

Transform90.children.append(Anchor221)
Anchor224 = x3d.Anchor()
Anchor224.url = ["javascript:window.open('./data/667.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor224.description = "Nene Day Centre, Northamtpon"
ProtoInstance225 = x3d.ProtoInstance()
ProtoInstance225.name = "institute"
fieldValue226 = x3d.fieldValue()
fieldValue226.name = "pos"
fieldValue226.value = "477.1000061035156 0.10000000149011612 -260"

ProtoInstance225.fieldValue.append(fieldValue226)

Anchor224.children.append(ProtoInstance225)

Transform90.children.append(Anchor224)
Anchor227 = x3d.Anchor()
Anchor227.url = ["javascript:window.open('./data/668.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor227.description = "Delapre Middle School, Northampton"
ProtoInstance228 = x3d.ProtoInstance()
ProtoInstance228.name = "school"
fieldValue229 = x3d.fieldValue()
fieldValue229.name = "pos"
fieldValue229.value = "474.70001220703125 0.10000000149011612 -259.1000061035156"

ProtoInstance228.fieldValue.append(fieldValue229)

Anchor227.children.append(ProtoInstance228)

Transform90.children.append(Anchor227)
Anchor230 = x3d.Anchor()
Anchor230.url = ["javascript:window.open('./data/669.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor230.description = "The Links, Brackley"
ProtoInstance231 = x3d.ProtoInstance()
ProtoInstance231.name = "institute"
fieldValue232 = x3d.fieldValue()
fieldValue232.name = "pos"
fieldValue232.value = "459 0.10000000149011612 -236.39999389648438"

ProtoInstance231.fieldValue.append(fieldValue232)

Anchor230.children.append(ProtoInstance231)

Transform90.children.append(Anchor230)
Anchor233 = x3d.Anchor()
Anchor233.url = ["javascript:window.open('./data/670.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor233.description = "New Perspectives"
ProtoInstance234 = x3d.ProtoInstance()
ProtoInstance234.name = "n"
fieldValue235 = x3d.fieldValue()
fieldValue235.name = "pos"
fieldValue235.value = "457.3999938964844 0.10000000149011612 -262.70001220703125"

ProtoInstance234.fieldValue.append(fieldValue235)

Anchor233.children.append(ProtoInstance234)

Transform90.children.append(Anchor233)
Anchor236 = x3d.Anchor()
Anchor236.url = ["javascript:window.open('./data/671.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor236.description = "UKan2"
ProtoInstance237 = x3d.ProtoInstance()
ProtoInstance237.name = "r"
fieldValue238 = x3d.fieldValue()
fieldValue238.name = "pos"
fieldValue238.value = "458.70001220703125 0.10000000149011612 -262.70001220703125"

ProtoInstance237.fieldValue.append(fieldValue238)

Anchor236.children.append(ProtoInstance237)

Transform90.children.append(Anchor236)
Anchor239 = x3d.Anchor()
Anchor239.url = ["javascript:window.open('./data/672.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor239.description = "Silverstone County Infants School"
ProtoInstance240 = x3d.ProtoInstance()
ProtoInstance240.name = "school"
fieldValue241 = x3d.fieldValue()
fieldValue241.name = "pos"
fieldValue241.value = "466.8999938964844 0.10000000149011612 -243.8000030517578"

ProtoInstance240.fieldValue.append(fieldValue241)

Anchor239.children.append(ProtoInstance240)

Transform90.children.append(Anchor239)
Anchor242 = x3d.Anchor()
Anchor242.url = ["javascript:window.open('./data/677.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor242.description = "Riverside Resource Centre, Towcester"
ProtoInstance243 = x3d.ProtoInstance()
ProtoInstance243.name = "institute"
fieldValue244 = x3d.fieldValue()
fieldValue244.name = "pos"
fieldValue244.value = "469.5 0.10000000149011612 -249.8000030517578"

ProtoInstance243.fieldValue.append(fieldValue244)

Anchor242.children.append(ProtoInstance243)

Transform90.children.append(Anchor242)
Anchor245 = x3d.Anchor()
Anchor245.url = ["javascript:window.open('./data/678.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor245.description = "Daventry Tertiary College"
ProtoInstance246 = x3d.ProtoInstance()
ProtoInstance246.name = "school"
fieldValue247 = x3d.fieldValue()
fieldValue247.name = "pos"
fieldValue247.value = "456.70001220703125 0.10000000149011612 -261.79998779296875"

ProtoInstance246.fieldValue.append(fieldValue247)

Anchor245.children.append(ProtoInstance246)

Transform90.children.append(Anchor245)
Shape248 = x3d.Shape()
Appearance249 = x3d.Appearance()
Material250 = x3d.Material()
Material250.transparency = 0.20000000298023224
Material250.emissiveColor = [1,0,0]

Appearance249.material = Material250

Shape248.appearance = Appearance249
IndexedLineSet251 = x3d.IndexedLineSet()
IndexedLineSet251.coordIndex = [0,1,-1,2,3,-1,4,5,-1,6,7,-1,8,9,-1,10,11,-1,12,13,-1,14,15,-1,16,17,-1,18,19,-1,20,21,-1,22,23,-1,24,25,-1,26,27,-1,28,29,-1,30,31,-1,32,33,-1,34,35,-1]
Coordinate252 = x3d.Coordinate()

IndexedLineSet251.coord = Coordinate252

Shape248.geometry = IndexedLineSet251

Transform90.children.append(Shape248)
Shape253 = x3d.Shape()
Appearance254 = x3d.Appearance()
Material255 = x3d.Material()
Material255.transparency = 0.20000000298023224
Material255.emissiveColor = [0,1,0]

Appearance254.material = Material255

Shape253.appearance = Appearance254
IndexedLineSet256 = x3d.IndexedLineSet()
IndexedLineSet256.coordIndex = [0,1,-1,2,3,-1,4,5,-1,6,7,-1,8,9,-1,10,11,-1,12,13,-1,14,15,-1,16,17,-1,18,19,-1,20,21,-1,22,23,-1,24,25,-1,26,27,-1,28,29,-1,30,31,-1,32,33,-1,34,35,-1]
Coordinate257 = x3d.Coordinate()

IndexedLineSet256.coord = Coordinate257

Shape253.geometry = IndexedLineSet256

Transform90.children.append(Shape253)
Shape258 = x3d.Shape()
Appearance259 = x3d.Appearance()
Material260 = x3d.Material()
Material260.transparency = 0.20000000298023224
Material260.emissiveColor = [1,0,1]

Appearance259.material = Material260

Shape258.appearance = Appearance259
IndexedLineSet261 = x3d.IndexedLineSet()
IndexedLineSet261.coordIndex = [0,1,-1,2,3,-1,4,5,-1,6,7,-1,8,9,-1]
Coordinate262 = x3d.Coordinate()

IndexedLineSet261.coord = Coordinate262

Shape258.geometry = IndexedLineSet261

Transform90.children.append(Shape258)

Scene4.children.append(Transform90)

X3D0.Scene = Scene4
f = open("././t1_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
