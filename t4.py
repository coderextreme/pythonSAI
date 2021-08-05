from x3dpsail import *
X3D0 = X3D()
X3D0.setProfile("Immersive")
X3D0.setVersion("3.3")
head1 = head()
component2 = component()
component2.setName("Networking")
component2.setLevel(2)

head1.addComponent(component2)
component3 = component()
component3.setName("Core")
component3.setLevel(2)

head1.addComponent(component3)
meta4 = meta()
meta4.setName("title")
meta4.setContent("t4.x3d")

head1.addMeta(meta4)
meta5 = meta()
meta5.setName("identifier")
meta5.setContent("http://coderextreme.net/X3DJSONLD/src/main/data/t4.x3d")

head1.addMeta(meta5)
meta6 = meta()
meta6.setName("generator")
meta6.setContent("view3dscene, https://castle-engine.io/view3dscene.php")

head1.addMeta(meta6)
meta7 = meta()
meta7.setName("creator")
meta7.setContent("Andreas Plesch and John Carlson")

head1.addMeta(meta7)
meta8 = meta()
meta8.setName("source")
meta8.setContent("t1.wrl")

head1.addMeta(meta8)
meta9 = meta()
meta9.setName("description")
meta9.setContent("Test Case for Proto Expander")

head1.addMeta(meta9)
meta10 = meta()
meta10.setName("license")
meta10.setContent("https://www.web3d.org/x3d/content/examples/license.html")

head1.addMeta(meta10)

X3D0.setHead(head1)
Scene11 = Scene()
NavigationInfo12 = NavigationInfo()
NavigationInfo12.setType(["EXAMINE","FLY","WALK"])
NavigationInfo12.setSpeed(3)
NavigationInfo12.setAvatarSize([200,200,120])

Scene11.addChildren(NavigationInfo12)
WorldInfo13 = WorldInfo()
WorldInfo13.setTitle("Arts Mapper")

Scene11.addChildren(WorldInfo13)
Viewpoint14 = Viewpoint()
Viewpoint14.setDescription("looking North")
Viewpoint14.setPosition([0,60,110])
Viewpoint14.setOrientation([1,0,0,-0.699999988079071])
Viewpoint14.setFieldOfView(0.785398125648499)

Scene11.addChildren(Viewpoint14)
ProtoDeclare15 = ProtoDeclare()
ProtoDeclare15.setName("org")
ProtoInterface16 = ProtoInterface()
field17 = field()
field17.setName("posi")
field17.setAccessType("initializeOnly")
field17.setType("SFVec3f")
field17.setValue("0 0 0")

ProtoInterface16.addField(field17)
field18 = field()
field18.setName("col")
field18.setAccessType("initializeOnly")
field18.setType("SFColor")
field18.setValue("0 0 0")

ProtoInterface16.addField(field18)

ProtoDeclare15.setProtoInterface(ProtoInterface16)
ProtoBody19 = ProtoBody()
Transform20 = Transform()
IS21 = IS()
connect22 = connect()
connect22.setNodeField("translation")
connect22.setProtoField("posi")

IS21.addConnect(connect22)

Transform20.setIS(IS21)
Shape23 = Shape()
Appearance24 = Appearance()
Material25 = Material()
Material25.setDiffuseColor([1,1,1])
IS26 = IS()
connect27 = connect()
connect27.setNodeField("emissiveColor")
connect27.setProtoField("col")

IS26.addConnect(connect27)

Material25.setIS(IS26)

Appearance24.setMaterial(Material25)

Shape23.setAppearance(Appearance24)
Sphere28 = Sphere()
Sphere28.setRadius(5.10000002384186)

Shape23.setGeometry(Sphere28)

Transform20.addChildren(Shape23)

ProtoBody19.addChildren(Transform20)

ProtoDeclare15.setProtoBody(ProtoBody19)

Scene11.addChildren(ProtoDeclare15)
ProtoDeclare29 = ProtoDeclare()
ProtoDeclare29.setName("r")
ProtoInterface30 = ProtoInterface()
field31 = field()
field31.setName("pos")
field31.setAccessType("initializeOnly")
field31.setType("SFVec3f")
field31.setValue("0 0 0")

ProtoInterface30.addField(field31)

ProtoDeclare29.setProtoInterface(ProtoInterface30)
ProtoBody32 = ProtoBody()
ProtoInstance33 = ProtoInstance()
ProtoInstance33.setName("org")
fieldValue34 = fieldValue()
fieldValue34.setName("col")
fieldValue34.setValue("0 0.300000011920929 1")

ProtoInstance33.addFieldValue(fieldValue34)
IS35 = IS()
connect36 = connect()
connect36.setNodeField("posi")
connect36.setProtoField("pos")

IS35.addConnect(connect36)

ProtoInstance33.setIS(IS35)

ProtoBody32.addChildren(ProtoInstance33)

ProtoDeclare29.setProtoBody(ProtoBody32)

Scene11.addChildren(ProtoDeclare29)
ProtoDeclare37 = ProtoDeclare()
ProtoDeclare37.setName("n")
ProtoInterface38 = ProtoInterface()
field39 = field()
field39.setName("pos")
field39.setAccessType("initializeOnly")
field39.setType("SFVec3f")
field39.setValue("0 0 0")

ProtoInterface38.addField(field39)

ProtoDeclare37.setProtoInterface(ProtoInterface38)
ProtoBody40 = ProtoBody()
ProtoInstance41 = ProtoInstance()
ProtoInstance41.setName("org")
fieldValue42 = fieldValue()
fieldValue42.setName("col")
fieldValue42.setValue("1 0 0.200000002980232")

ProtoInstance41.addFieldValue(fieldValue42)
IS43 = IS()
connect44 = connect()
connect44.setNodeField("posi")
connect44.setProtoField("pos")

IS43.addConnect(connect44)

ProtoInstance41.setIS(IS43)

ProtoBody40.addChildren(ProtoInstance41)

ProtoDeclare37.setProtoBody(ProtoBody40)

Scene11.addChildren(ProtoDeclare37)
ProtoDeclare45 = ProtoDeclare()
ProtoDeclare45.setName("i")
ProtoInterface46 = ProtoInterface()
field47 = field()
field47.setName("pos")
field47.setAccessType("initializeOnly")
field47.setType("SFVec3f")
field47.setValue("0 0 0")

ProtoInterface46.addField(field47)

ProtoDeclare45.setProtoInterface(ProtoInterface46)
ProtoBody48 = ProtoBody()
ProtoInstance49 = ProtoInstance()
ProtoInstance49.setName("org")
fieldValue50 = fieldValue()
fieldValue50.setName("col")
fieldValue50.setValue("0.600000023841858 0 0.600000023841858")

ProtoInstance49.addFieldValue(fieldValue50)
IS51 = IS()
connect52 = connect()
connect52.setNodeField("posi")
connect52.setProtoField("pos")

IS51.addConnect(connect52)

ProtoInstance49.setIS(IS51)

ProtoBody48.addChildren(ProtoInstance49)

ProtoDeclare45.setProtoBody(ProtoBody48)

Scene11.addChildren(ProtoDeclare45)
Transform53 = Transform()
Transform53.setTranslation([-468,0,315])
Anchor54 = Anchor()
Anchor54.setUrl([", ","javascript:window.open('https://coderextreme.net/X3DJSONLD/src/main/data/574.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');javascript:window.open('./data/574.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"])
Anchor54.setDescription("High Peak Community Arts")
ProtoInstance55 = ProtoInstance()
ProtoInstance55.setName("r")
fieldValue56 = fieldValue()
fieldValue56.setName("pos")
fieldValue56.setValue("400 0.100000001490116 -385")

ProtoInstance55.addFieldValue(fieldValue56)

Anchor54.addChildren(ProtoInstance55)

Transform53.addChildren(Anchor54)
Anchor57 = Anchor()
Anchor57.setUrl([", ","javascript:window.open('https://coderextreme.net/X3DJSONLD/src/main/data/583.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');javascript:window.open('./data/583.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"])
Anchor57.setDescription("People Express")
ProtoInstance58 = ProtoInstance()
ProtoInstance58.setName("i")
fieldValue59 = fieldValue()
fieldValue59.setName("pos")
fieldValue59.setValue("429.899993896484 0.100000001490116 -319.600006103516")

ProtoInstance58.addFieldValue(fieldValue59)

Anchor57.addChildren(ProtoInstance58)

Transform53.addChildren(Anchor57)
Anchor60 = Anchor()
Anchor60.setUrl([", ","javascript:window.open('https://coderextreme.net/X3DJSONLD/src/main/data/589.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');javascript:window.open('./data/589.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"])
Anchor60.setDescription("QArts/Studios")
ProtoInstance61 = ProtoInstance()
ProtoInstance61.setName("i")
fieldValue62 = fieldValue()
fieldValue62.setName("pos")
fieldValue62.setValue("430 0.100000001490116 -335")

ProtoInstance61.addFieldValue(fieldValue62)

Anchor60.addChildren(ProtoInstance61)

Transform53.addChildren(Anchor60)
Anchor63 = Anchor()
Anchor63.setUrl([", ","javascript:window.open('https://coderextreme.net/X3DJSONLD/src/main/data/593.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');javascript:window.open('./data/593.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"])
Anchor63.setDescription("First Movement")
ProtoInstance64 = ProtoInstance()
ProtoInstance64.setName("n")
fieldValue65 = fieldValue()
fieldValue65.setName("pos")
fieldValue65.setValue("429.899993896484 0.100000001490116 -360.299987792969")

ProtoInstance64.addFieldValue(fieldValue65)

Anchor63.addChildren(ProtoInstance64)

Transform53.addChildren(Anchor63)
Anchor66 = Anchor()
Anchor66.setUrl([", ","javascript:window.open('https://coderextreme.net/X3DJSONLD/src/main/data/612.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');javascript:window.open('./data/612.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"])
Anchor66.setDescription("City Arts")
ProtoInstance67 = ProtoInstance()
ProtoInstance67.setName("i")
fieldValue68 = fieldValue()
fieldValue68.setName("pos")
fieldValue68.setValue("455.899993896484 0.100000001490116 -341.299987792969")

ProtoInstance67.addFieldValue(fieldValue68)

Anchor66.addChildren(ProtoInstance67)

Transform53.addChildren(Anchor66)
Anchor69 = Anchor()
Anchor69.setUrl([", ","javascript:window.open('https://coderextreme.net/X3DJSONLD/src/main/data/615.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');javascript:window.open('./data/615.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"])
Anchor69.setDescription("Indigo Dance Group (Salamanda Tandem)")
ProtoInstance70 = ProtoInstance()
ProtoInstance70.setName("r")
fieldValue71 = fieldValue()
fieldValue71.setName("pos")
fieldValue71.setValue("456.100006103516 0.100000001490116 -341.5")

ProtoInstance70.addFieldValue(fieldValue71)

Anchor69.addChildren(ProtoInstance70)

Transform53.addChildren(Anchor69)
Anchor72 = Anchor()
Anchor72.setUrl([", ","javascript:window.open('https://coderextreme.net/X3DJSONLD/src/main/data/623.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');javascript:window.open('./data/623.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"])
Anchor72.setDescription("Watering Seeds")
ProtoInstance73 = ProtoInstance()
ProtoInstance73.setName("r")
fieldValue74 = fieldValue()
fieldValue74.setName("pos")
fieldValue74.setValue("454 0.100000001490116 -361.299987792969")

ProtoInstance73.addFieldValue(fieldValue74)

Anchor72.addChildren(ProtoInstance73)

Transform53.addChildren(Anchor72)
Anchor75 = Anchor()
Anchor75.setUrl([", ","javascript:window.open('https://coderextreme.net/X3DJSONLD/src/main/data/630.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');javascript:window.open('./data/630.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"])
Anchor75.setDescription("Fased In The Arts")
ProtoInstance76 = ProtoInstance()
ProtoInstance76.setName("r")
fieldValue77 = fieldValue()
fieldValue77.setName("pos")
fieldValue77.setValue("440 0.100000001490116 -350")

ProtoInstance76.addFieldValue(fieldValue77)

Anchor75.addChildren(ProtoInstance76)

Transform53.addChildren(Anchor75)
Anchor78 = Anchor()
Anchor78.setUrl([", ","javascript:window.open('https://coderextreme.net/X3DJSONLD/src/main/data/633.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');javascript:window.open('./data/633.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"])
Anchor78.setDescription("27a Access Artspace")
ProtoInstance79 = ProtoInstance()
ProtoInstance79.setName("n")
fieldValue80 = fieldValue()
fieldValue80.setName("pos")
fieldValue80.setValue("458.899993896484 0.100000001490116 -304.299987792969")

ProtoInstance79.addFieldValue(fieldValue80)

Anchor78.addChildren(ProtoInstance79)

Transform53.addChildren(Anchor78)
Anchor81 = Anchor()
Anchor81.setUrl([", ","javascript:window.open('https://coderextreme.net/X3DJSONLD/src/main/data/638.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');javascript:window.open('./data/638.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"])
Anchor81.setDescription("Bamboozle Theatre Company")
ProtoInstance82 = ProtoInstance()
ProtoInstance82.setName("r")
fieldValue83 = fieldValue()
fieldValue83.setName("pos")
fieldValue83.setValue("457.100006103516 0.100000001490116 -300.799987792969")

ProtoInstance82.addFieldValue(fieldValue83)

Anchor81.addChildren(ProtoInstance82)

Transform53.addChildren(Anchor81)
Anchor84 = Anchor()
Anchor84.setUrl([", ","javascript:window.open('https://coderextreme.net/X3DJSONLD/src/main/data/648.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');javascript:window.open('./data/648.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"])
Anchor84.setDescription("Mantle Community Arts")
ProtoInstance85 = ProtoInstance()
ProtoInstance85.setName("r")
fieldValue86 = fieldValue()
fieldValue86.setName("pos")
fieldValue86.setValue("442.399993896484 0.100000001490116 -314.5")

ProtoInstance85.addFieldValue(fieldValue86)

Anchor84.addChildren(ProtoInstance85)

Transform53.addChildren(Anchor84)
Anchor87 = Anchor()
Anchor87.setUrl([", ","javascript:window.open('https://coderextreme.net/X3DJSONLD/src/main/data/658.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');javascript:window.open('./data/658.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"])
Anchor87.setDescription("Artlink East")
ProtoInstance88 = ProtoInstance()
ProtoInstance88.setName("r")
fieldValue89 = fieldValue()
fieldValue89.setName("pos")
fieldValue89.setValue("491.600006103516 0.100000001490116 -335.700012207031")

ProtoInstance88.addFieldValue(fieldValue89)

Anchor87.addChildren(ProtoInstance88)

Transform53.addChildren(Anchor87)
Anchor90 = Anchor()
Anchor90.setUrl([", ","javascript:window.open('https://coderextreme.net/X3DJSONLD/src/main/data/665.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');javascript:window.open('./data/665.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"])
Anchor90.setDescription("Creations")
ProtoInstance91 = ProtoInstance()
ProtoInstance91.setName("r")
fieldValue92 = fieldValue()
fieldValue92.setName("pos")
fieldValue92.setValue("467 0.100000001490116 -243.899993896484")

ProtoInstance91.addFieldValue(fieldValue92)

Anchor90.addChildren(ProtoInstance91)

Transform53.addChildren(Anchor90)
Anchor93 = Anchor()
Anchor93.setUrl([", ","javascript:window.open('https://coderextreme.net/X3DJSONLD/src/main/data/670.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');javascript:window.open('./data/670.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"])
Anchor93.setDescription("New Perspectives")
ProtoInstance94 = ProtoInstance()
ProtoInstance94.setName("n")
fieldValue95 = fieldValue()
fieldValue95.setName("pos")
fieldValue95.setValue("457.399993896484 0.100000001490116 -262.700012207031")

ProtoInstance94.addFieldValue(fieldValue95)

Anchor93.addChildren(ProtoInstance94)

Transform53.addChildren(Anchor93)
Anchor96 = Anchor()
Anchor96.setUrl([", ","javascript:window.open('https://coderextreme.net/X3DJSONLD/src/main/data/671.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');javascript:window.open('./data/671.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"])
Anchor96.setDescription("UKan2")
ProtoInstance97 = ProtoInstance()
ProtoInstance97.setName("r")
fieldValue98 = fieldValue()
fieldValue98.setName("pos")
fieldValue98.setValue("458.700012207031 0.100000001490116 -262.700012207031")

ProtoInstance97.addFieldValue(fieldValue98)

Anchor96.addChildren(ProtoInstance97)

Transform53.addChildren(Anchor96)

Scene11.addChildren(Transform53)

X3D0.setScene(Scene11)
X3D0.toFileX3D("././t4_RoundTrip.x3d")
