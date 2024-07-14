print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"
head1 = x3d.head()
component2 = x3d.component()
component2.name = "Networking"
component2.level = 2

head1.children.append(component2)
component3 = x3d.component()
component3.name = "Core"
component3.level = 2

head1.children.append(component3)
meta4 = x3d.meta()
meta4.name = "title"
meta4.content = "t4.x3d"

head1.children.append(meta4)
meta5 = x3d.meta()
meta5.name = "identifier"
meta5.content = "http://coderextreme.net/X3DJSONLD/src/main/data/t4.x3d"

head1.children.append(meta5)
meta6 = x3d.meta()
meta6.name = "generator"
meta6.content = "view3dscene, https://castle-engine.io/view3dscene.php"

head1.children.append(meta6)
meta7 = x3d.meta()
meta7.name = "creator"
meta7.content = "Andreas Plesch and John Carlson"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.name = "source"
meta8.content = "t1.wrl"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "description"
meta9.content = "Test Case for Proto Expander"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "license"
meta10.content = "https://www.web3d.org/x3d/content/examples/license.html"

head1.children.append(meta10)

X3D0.head = head1
Scene11 = x3d.Scene()
NavigationInfo12 = x3d.NavigationInfo()
NavigationInfo12.type = ["EXAMINE","FLY","WALK"]
NavigationInfo12.speed = 3
NavigationInfo12.avatarSize = [200,200,120]

Scene11.children.append(NavigationInfo12)
WorldInfo13 = x3d.WorldInfo()
WorldInfo13.title = "Arts Mapper"

Scene11.children.append(WorldInfo13)
Viewpoint14 = x3d.Viewpoint()
Viewpoint14.description = "looking North"
Viewpoint14.position = [0,60,110]
Viewpoint14.orientation = [1,0,0,-0.699999988079071]
Viewpoint14.fieldOfView = 0.785398125648499

Scene11.children.append(Viewpoint14)
ProtoDeclare15 = x3d.ProtoDeclare()
ProtoDeclare15.name = "org"
ProtoInterface16 = x3d.ProtoInterface()
field17 = x3d.field()
field17.name = "posi"
field17.accessType = "initializeOnly"
field17.type = "SFVec3f"
field17.value = [0,0,0]

ProtoInterface16.field.append(field17)
field18 = x3d.field()
field18.name = "col"
field18.accessType = "initializeOnly"
field18.type = "SFColor"
field18.value = [0,0,0]

ProtoInterface16.field.append(field18)

ProtoDeclare15.ProtoInterface = ProtoInterface16
ProtoBody19 = x3d.ProtoBody()
Transform20 = x3d.Transform()
IS21 = x3d.IS()
connect22 = x3d.connect()
connect22.nodeField = "translation"
connect22.protoField = "posi"

IS21.connect.append(connect22)

Transform20.IS = IS21
Shape23 = x3d.Shape()
Appearance24 = x3d.Appearance()
Material25 = x3d.Material()
Material25.diffuseColor = [1,1,1]
IS26 = x3d.IS()
connect27 = x3d.connect()
connect27.nodeField = "emissiveColor"
connect27.protoField = "col"

IS26.connect.append(connect27)

Material25.IS = IS26

Appearance24.material = Material25

Shape23.appearance = Appearance24
Sphere28 = x3d.Sphere()
Sphere28.radius = 5.10000002384186

Shape23.geometry = Sphere28

Transform20.children.append(Shape23)

ProtoBody19.children.append(Transform20)

ProtoDeclare15.ProtoBody = ProtoBody19

Scene11.children.append(ProtoDeclare15)
ProtoDeclare29 = x3d.ProtoDeclare()
ProtoDeclare29.name = "r"
ProtoInterface30 = x3d.ProtoInterface()
field31 = x3d.field()
field31.name = "pos"
field31.accessType = "initializeOnly"
field31.type = "SFVec3f"
field31.value = [0,0,0]

ProtoInterface30.field.append(field31)

ProtoDeclare29.ProtoInterface = ProtoInterface30
ProtoBody32 = x3d.ProtoBody()
ProtoInstance33 = x3d.ProtoInstance()
ProtoInstance33.name = "org"
fieldValue34 = x3d.fieldValue()
fieldValue34.name = "col"
fieldValue34.value = "0 0.300000011920929 1"

ProtoInstance33.fieldValue.append(fieldValue34)
IS35 = x3d.IS()
connect36 = x3d.connect()
connect36.nodeField = "posi"
connect36.protoField = "pos"

IS35.connect.append(connect36)

ProtoInstance33.IS = IS35

ProtoBody32.children.append(ProtoInstance33)

ProtoDeclare29.ProtoBody = ProtoBody32

Scene11.children.append(ProtoDeclare29)
ProtoDeclare37 = x3d.ProtoDeclare()
ProtoDeclare37.name = "n"
ProtoInterface38 = x3d.ProtoInterface()
field39 = x3d.field()
field39.name = "pos"
field39.accessType = "initializeOnly"
field39.type = "SFVec3f"
field39.value = [0,0,0]

ProtoInterface38.field.append(field39)

ProtoDeclare37.ProtoInterface = ProtoInterface38
ProtoBody40 = x3d.ProtoBody()
ProtoInstance41 = x3d.ProtoInstance()
ProtoInstance41.name = "org"
fieldValue42 = x3d.fieldValue()
fieldValue42.name = "col"
fieldValue42.value = "1 0 0.200000002980232"

ProtoInstance41.fieldValue.append(fieldValue42)
IS43 = x3d.IS()
connect44 = x3d.connect()
connect44.nodeField = "posi"
connect44.protoField = "pos"

IS43.connect.append(connect44)

ProtoInstance41.IS = IS43

ProtoBody40.children.append(ProtoInstance41)

ProtoDeclare37.ProtoBody = ProtoBody40

Scene11.children.append(ProtoDeclare37)
ProtoDeclare45 = x3d.ProtoDeclare()
ProtoDeclare45.name = "i"
ProtoInterface46 = x3d.ProtoInterface()
field47 = x3d.field()
field47.name = "pos"
field47.accessType = "initializeOnly"
field47.type = "SFVec3f"
field47.value = [0,0,0]

ProtoInterface46.field.append(field47)

ProtoDeclare45.ProtoInterface = ProtoInterface46
ProtoBody48 = x3d.ProtoBody()
ProtoInstance49 = x3d.ProtoInstance()
ProtoInstance49.name = "org"
fieldValue50 = x3d.fieldValue()
fieldValue50.name = "col"
fieldValue50.value = "0.600000023841858 0 0.600000023841858"

ProtoInstance49.fieldValue.append(fieldValue50)
IS51 = x3d.IS()
connect52 = x3d.connect()
connect52.nodeField = "posi"
connect52.protoField = "pos"

IS51.connect.append(connect52)

ProtoInstance49.IS = IS51

ProtoBody48.children.append(ProtoInstance49)

ProtoDeclare45.ProtoBody = ProtoBody48

Scene11.children.append(ProtoDeclare45)
Transform53 = x3d.Transform()
Transform53.translation = [-468,0,315]
Anchor54 = x3d.Anchor()
Anchor54.url = [", ","javascript:window.open('https://coderextreme.net/X3DJSONLD/src/main/data/574.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');javascript:window.open('./data/574.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor54.description = "High Peak Community Arts"
ProtoInstance55 = x3d.ProtoInstance()
ProtoInstance55.name = "r"
fieldValue56 = x3d.fieldValue()
fieldValue56.name = "pos"
fieldValue56.value = "400 0.100000001490116 -385"

ProtoInstance55.fieldValue.append(fieldValue56)

Anchor54.children.append(ProtoInstance55)

Transform53.children.append(Anchor54)
Anchor57 = x3d.Anchor()
Anchor57.url = [", ","javascript:window.open('https://coderextreme.net/X3DJSONLD/src/main/data/583.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');javascript:window.open('./data/583.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor57.description = "People Express"
ProtoInstance58 = x3d.ProtoInstance()
ProtoInstance58.name = "i"
fieldValue59 = x3d.fieldValue()
fieldValue59.name = "pos"
fieldValue59.value = "429.899993896484 0.100000001490116 -319.600006103516"

ProtoInstance58.fieldValue.append(fieldValue59)

Anchor57.children.append(ProtoInstance58)

Transform53.children.append(Anchor57)
Anchor60 = x3d.Anchor()
Anchor60.url = [", ","javascript:window.open('https://coderextreme.net/X3DJSONLD/src/main/data/589.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');javascript:window.open('./data/589.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor60.description = "QArts/Studios"
ProtoInstance61 = x3d.ProtoInstance()
ProtoInstance61.name = "i"
fieldValue62 = x3d.fieldValue()
fieldValue62.name = "pos"
fieldValue62.value = "430 0.100000001490116 -335"

ProtoInstance61.fieldValue.append(fieldValue62)

Anchor60.children.append(ProtoInstance61)

Transform53.children.append(Anchor60)
Anchor63 = x3d.Anchor()
Anchor63.url = [", ","javascript:window.open('https://coderextreme.net/X3DJSONLD/src/main/data/593.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');javascript:window.open('./data/593.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor63.description = "First Movement"
ProtoInstance64 = x3d.ProtoInstance()
ProtoInstance64.name = "n"
fieldValue65 = x3d.fieldValue()
fieldValue65.name = "pos"
fieldValue65.value = "429.899993896484 0.100000001490116 -360.299987792969"

ProtoInstance64.fieldValue.append(fieldValue65)

Anchor63.children.append(ProtoInstance64)

Transform53.children.append(Anchor63)
Anchor66 = x3d.Anchor()
Anchor66.url = [", ","javascript:window.open('https://coderextreme.net/X3DJSONLD/src/main/data/612.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');javascript:window.open('./data/612.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor66.description = "City Arts"
ProtoInstance67 = x3d.ProtoInstance()
ProtoInstance67.name = "i"
fieldValue68 = x3d.fieldValue()
fieldValue68.name = "pos"
fieldValue68.value = "455.899993896484 0.100000001490116 -341.299987792969"

ProtoInstance67.fieldValue.append(fieldValue68)

Anchor66.children.append(ProtoInstance67)

Transform53.children.append(Anchor66)
Anchor69 = x3d.Anchor()
Anchor69.url = [", ","javascript:window.open('https://coderextreme.net/X3DJSONLD/src/main/data/615.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');javascript:window.open('./data/615.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor69.description = "Indigo Dance Group (Salamanda Tandem)"
ProtoInstance70 = x3d.ProtoInstance()
ProtoInstance70.name = "r"
fieldValue71 = x3d.fieldValue()
fieldValue71.name = "pos"
fieldValue71.value = "456.100006103516 0.100000001490116 -341.5"

ProtoInstance70.fieldValue.append(fieldValue71)

Anchor69.children.append(ProtoInstance70)

Transform53.children.append(Anchor69)
Anchor72 = x3d.Anchor()
Anchor72.url = [", ","javascript:window.open('https://coderextreme.net/X3DJSONLD/src/main/data/623.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');javascript:window.open('./data/623.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor72.description = "Watering Seeds"
ProtoInstance73 = x3d.ProtoInstance()
ProtoInstance73.name = "r"
fieldValue74 = x3d.fieldValue()
fieldValue74.name = "pos"
fieldValue74.value = "454 0.100000001490116 -361.299987792969"

ProtoInstance73.fieldValue.append(fieldValue74)

Anchor72.children.append(ProtoInstance73)

Transform53.children.append(Anchor72)
Anchor75 = x3d.Anchor()
Anchor75.url = [", ","javascript:window.open('https://coderextreme.net/X3DJSONLD/src/main/data/630.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');javascript:window.open('./data/630.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor75.description = "Fased In The Arts"
ProtoInstance76 = x3d.ProtoInstance()
ProtoInstance76.name = "r"
fieldValue77 = x3d.fieldValue()
fieldValue77.name = "pos"
fieldValue77.value = "440 0.100000001490116 -350"

ProtoInstance76.fieldValue.append(fieldValue77)

Anchor75.children.append(ProtoInstance76)

Transform53.children.append(Anchor75)
Anchor78 = x3d.Anchor()
Anchor78.url = [", ","javascript:window.open('https://coderextreme.net/X3DJSONLD/src/main/data/633.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');javascript:window.open('./data/633.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor78.description = "27a Access Artspace"
ProtoInstance79 = x3d.ProtoInstance()
ProtoInstance79.name = "n"
fieldValue80 = x3d.fieldValue()
fieldValue80.name = "pos"
fieldValue80.value = "458.899993896484 0.100000001490116 -304.299987792969"

ProtoInstance79.fieldValue.append(fieldValue80)

Anchor78.children.append(ProtoInstance79)

Transform53.children.append(Anchor78)
Anchor81 = x3d.Anchor()
Anchor81.url = [", ","javascript:window.open('https://coderextreme.net/X3DJSONLD/src/main/data/638.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');javascript:window.open('./data/638.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor81.description = "Bamboozle Theatre Company"
ProtoInstance82 = x3d.ProtoInstance()
ProtoInstance82.name = "r"
fieldValue83 = x3d.fieldValue()
fieldValue83.name = "pos"
fieldValue83.value = "457.100006103516 0.100000001490116 -300.799987792969"

ProtoInstance82.fieldValue.append(fieldValue83)

Anchor81.children.append(ProtoInstance82)

Transform53.children.append(Anchor81)
Anchor84 = x3d.Anchor()
Anchor84.url = [", ","javascript:window.open('https://coderextreme.net/X3DJSONLD/src/main/data/648.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');javascript:window.open('./data/648.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor84.description = "Mantle Community Arts"
ProtoInstance85 = x3d.ProtoInstance()
ProtoInstance85.name = "r"
fieldValue86 = x3d.fieldValue()
fieldValue86.name = "pos"
fieldValue86.value = "442.399993896484 0.100000001490116 -314.5"

ProtoInstance85.fieldValue.append(fieldValue86)

Anchor84.children.append(ProtoInstance85)

Transform53.children.append(Anchor84)
Anchor87 = x3d.Anchor()
Anchor87.url = [", ","javascript:window.open('https://coderextreme.net/X3DJSONLD/src/main/data/658.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');javascript:window.open('./data/658.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor87.description = "Artlink East"
ProtoInstance88 = x3d.ProtoInstance()
ProtoInstance88.name = "r"
fieldValue89 = x3d.fieldValue()
fieldValue89.name = "pos"
fieldValue89.value = "491.600006103516 0.100000001490116 -335.700012207031"

ProtoInstance88.fieldValue.append(fieldValue89)

Anchor87.children.append(ProtoInstance88)

Transform53.children.append(Anchor87)
Anchor90 = x3d.Anchor()
Anchor90.url = [", ","javascript:window.open('https://coderextreme.net/X3DJSONLD/src/main/data/665.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');javascript:window.open('./data/665.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor90.description = "Creations"
ProtoInstance91 = x3d.ProtoInstance()
ProtoInstance91.name = "r"
fieldValue92 = x3d.fieldValue()
fieldValue92.name = "pos"
fieldValue92.value = "467 0.100000001490116 -243.899993896484"

ProtoInstance91.fieldValue.append(fieldValue92)

Anchor90.children.append(ProtoInstance91)

Transform53.children.append(Anchor90)
Anchor93 = x3d.Anchor()
Anchor93.url = [", ","javascript:window.open('https://coderextreme.net/X3DJSONLD/src/main/data/670.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');javascript:window.open('./data/670.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor93.description = "New Perspectives"
ProtoInstance94 = x3d.ProtoInstance()
ProtoInstance94.name = "n"
fieldValue95 = x3d.fieldValue()
fieldValue95.name = "pos"
fieldValue95.value = "457.399993896484 0.100000001490116 -262.700012207031"

ProtoInstance94.fieldValue.append(fieldValue95)

Anchor93.children.append(ProtoInstance94)

Transform53.children.append(Anchor93)
Anchor96 = x3d.Anchor()
Anchor96.url = [", ","javascript:window.open('https://coderextreme.net/X3DJSONLD/src/main/data/671.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');javascript:window.open('./data/671.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor96.description = "UKan2"
ProtoInstance97 = x3d.ProtoInstance()
ProtoInstance97.name = "r"
fieldValue98 = x3d.fieldValue()
fieldValue98.name = "pos"
fieldValue98.value = "458.700012207031 0.100000001490116 -262.700012207031"

ProtoInstance97.fieldValue.append(fieldValue98)

Anchor96.children.append(ProtoInstance97)

Transform53.children.append(Anchor96)

Scene11.children.append(Transform53)

X3D0.Scene = Scene11
f = open("././t4_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
