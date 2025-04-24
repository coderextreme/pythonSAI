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
meta4.content = "t3.x3d"

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
meta10.content = "https://www.web3d.org/x3d/content/examples/license.html"
meta10.name = "license"

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.name = "translated"
meta11.content = "12 May 2020"

head1.children.append(meta11)
meta12 = x3d.meta()
meta12.name = "generator"
meta12.content = "DOM2JSONSerializer.js, https://github.com/coderextreme/X3DJSONLD/blob/master/src/main/node/DOM2JSONSerializer.js"

head1.children.append(meta12)
meta13 = x3d.meta()
meta13.name = "reference"
meta13.content = "X3D JSON encoding: https://www.web3d.org/wiki/index.php/X3D_JSON_Encoding"

head1.children.append(meta13)

X3D0.head = head1
Scene14 = x3d.Scene()
NavigationInfo15 = x3d.NavigationInfo()
NavigationInfo15.type = ["EXAMINE","FLY","WALK"]
NavigationInfo15.speed = 3
NavigationInfo15.avatarSize = [200,200,120]

Scene14.children.append(NavigationInfo15)
WorldInfo16 = x3d.WorldInfo()
WorldInfo16.title = "Arts Mapper"

Scene14.children.append(WorldInfo16)
Viewpoint17 = x3d.Viewpoint()
Viewpoint17.description = "looking North"
Viewpoint17.position = [0,60,110]
Viewpoint17.orientation = [1,0,0,-0.699999988079071]
Viewpoint17.fieldOfView = 0.785398125648499

Scene14.children.append(Viewpoint17)
Transform18 = x3d.Transform()
Transform18.translation = [-468,0,315]
Anchor19 = x3d.Anchor()
Anchor19.url = ["javascript:window.open('https://coderextreme.net/X3DJSONLD/src/main/data/574.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');","javascript:window.open('./data/574.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor19.description = "High Peak Community Arts"
Transform20 = x3d.Transform()
Shape21 = x3d.Shape()
Appearance22 = x3d.Appearance()
Material23 = x3d.Material()
Material23.diffuseColor = [1,1,1]
Material23.emissiveColor = [0,0.300000011920929,1]

Appearance22.material = Material23

Shape21.appearance = Appearance22
Sphere24 = x3d.Sphere()
Sphere24.radius = 5.10000002384186

Shape21.geometry = Sphere24

Transform20.children.append(Shape21)

Anchor19.children.append(Transform20)

Transform18.children.append(Anchor19)
Anchor25 = x3d.Anchor()
Anchor25.url = ["javascript:window.open('https://coderextreme.net/X3DJSONLD/src/main/data/583.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');","javascript:window.open('./data/583.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor25.description = "People Express"
Transform26 = x3d.Transform()
Shape27 = x3d.Shape()
Appearance28 = x3d.Appearance()
Material29 = x3d.Material()
Material29.diffuseColor = [1,1,1]
Material29.emissiveColor = [0.600000023841858,0,0.600000023841858]

Appearance28.material = Material29

Shape27.appearance = Appearance28
Sphere30 = x3d.Sphere()
Sphere30.radius = 5.10000002384186

Shape27.geometry = Sphere30

Transform26.children.append(Shape27)

Anchor25.children.append(Transform26)

Transform18.children.append(Anchor25)
Anchor31 = x3d.Anchor()
Anchor31.url = ["javascript:window.open('https://coderextreme.net/X3DJSONLD/src/main/data/589.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');","javascript:window.open('./data/589.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor31.description = "QArts/Studios"
Transform32 = x3d.Transform()
Shape33 = x3d.Shape()
Appearance34 = x3d.Appearance()
Material35 = x3d.Material()
Material35.diffuseColor = [1,1,1]
Material35.emissiveColor = [0.600000023841858,0,0.600000023841858]

Appearance34.material = Material35

Shape33.appearance = Appearance34
Sphere36 = x3d.Sphere()
Sphere36.radius = 5.10000002384186

Shape33.geometry = Sphere36

Transform32.children.append(Shape33)

Anchor31.children.append(Transform32)

Transform18.children.append(Anchor31)
Anchor37 = x3d.Anchor()
Anchor37.url = ["javascript:window.open('https://coderextreme.net/X3DJSONLD/src/main/data/593.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');","javascript:window.open('./data/593.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor37.description = "First Movement"
Transform38 = x3d.Transform()
Shape39 = x3d.Shape()
Appearance40 = x3d.Appearance()
Material41 = x3d.Material()
Material41.diffuseColor = [1,1,1]
Material41.emissiveColor = [1,0,0.200000002980232]

Appearance40.material = Material41

Shape39.appearance = Appearance40
Sphere42 = x3d.Sphere()
Sphere42.radius = 5.10000002384186

Shape39.geometry = Sphere42

Transform38.children.append(Shape39)

Anchor37.children.append(Transform38)

Transform18.children.append(Anchor37)
Anchor43 = x3d.Anchor()
Anchor43.url = ["javascript:window.open('https://coderextreme.net/X3DJSONLD/src/main/data/612.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');","javascript:window.open('./data/612.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor43.description = "City Arts"
Transform44 = x3d.Transform()
Shape45 = x3d.Shape()
Appearance46 = x3d.Appearance()
Material47 = x3d.Material()
Material47.diffuseColor = [1,1,1]
Material47.emissiveColor = [0.600000023841858,0,0.600000023841858]

Appearance46.material = Material47

Shape45.appearance = Appearance46
Sphere48 = x3d.Sphere()
Sphere48.radius = 5.10000002384186

Shape45.geometry = Sphere48

Transform44.children.append(Shape45)

Anchor43.children.append(Transform44)

Transform18.children.append(Anchor43)
Anchor49 = x3d.Anchor()
Anchor49.url = ["javascript:window.open('https://coderextreme.net/X3DJSONLD/src/main/data/615.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');","javascript:window.open('./data/615.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor49.description = "Indigo Dance Group (Salamanda Tandem)"
Transform50 = x3d.Transform()
Shape51 = x3d.Shape()
Appearance52 = x3d.Appearance()
Material53 = x3d.Material()
Material53.diffuseColor = [1,1,1]
Material53.emissiveColor = [0,0.300000011920929,1]

Appearance52.material = Material53

Shape51.appearance = Appearance52
Sphere54 = x3d.Sphere()
Sphere54.radius = 5.10000002384186

Shape51.geometry = Sphere54

Transform50.children.append(Shape51)

Anchor49.children.append(Transform50)

Transform18.children.append(Anchor49)
Anchor55 = x3d.Anchor()
Anchor55.url = ["javascript:window.open('https://coderextreme.net/X3DJSONLD/src/main/data/623.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');","javascript:window.open('./data/623.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor55.description = "Watering Seeds"
Transform56 = x3d.Transform()
Shape57 = x3d.Shape()
Appearance58 = x3d.Appearance()
Material59 = x3d.Material()
Material59.diffuseColor = [1,1,1]
Material59.emissiveColor = [0,0.300000011920929,1]

Appearance58.material = Material59

Shape57.appearance = Appearance58
Sphere60 = x3d.Sphere()
Sphere60.radius = 5.10000002384186

Shape57.geometry = Sphere60

Transform56.children.append(Shape57)

Anchor55.children.append(Transform56)

Transform18.children.append(Anchor55)
Anchor61 = x3d.Anchor()
Anchor61.url = ["javascript:window.open('https://coderextreme.net/X3DJSONLD/src/main/data/630.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');","javascript:window.open('./data/630.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor61.description = "Fased In The Arts"
Transform62 = x3d.Transform()
Shape63 = x3d.Shape()
Appearance64 = x3d.Appearance()
Material65 = x3d.Material()
Material65.diffuseColor = [1,1,1]
Material65.emissiveColor = [0,0.300000011920929,1]

Appearance64.material = Material65

Shape63.appearance = Appearance64
Sphere66 = x3d.Sphere()
Sphere66.radius = 5.10000002384186

Shape63.geometry = Sphere66

Transform62.children.append(Shape63)

Anchor61.children.append(Transform62)

Transform18.children.append(Anchor61)
Anchor67 = x3d.Anchor()
Anchor67.url = ["javascript:window.open('https://coderextreme.net/X3DJSONLD/src/main/data/633.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');","javascript:window.open('./data/633.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor67.description = "27a Access Artspace"
Transform68 = x3d.Transform()
Shape69 = x3d.Shape()
Appearance70 = x3d.Appearance()
Material71 = x3d.Material()
Material71.diffuseColor = [1,1,1]
Material71.emissiveColor = [1,0,0.200000002980232]

Appearance70.material = Material71

Shape69.appearance = Appearance70
Sphere72 = x3d.Sphere()
Sphere72.radius = 5.10000002384186

Shape69.geometry = Sphere72

Transform68.children.append(Shape69)

Anchor67.children.append(Transform68)

Transform18.children.append(Anchor67)
Anchor73 = x3d.Anchor()
Anchor73.url = ["javascript:window.open('https://coderextreme.net/X3DJSONLD/src/main/data/638.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');","javascript:window.open('./data/638.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor73.description = "Bamboozle Theatre Company"
Transform74 = x3d.Transform()
Shape75 = x3d.Shape()
Appearance76 = x3d.Appearance()
Material77 = x3d.Material()
Material77.diffuseColor = [1,1,1]
Material77.emissiveColor = [0,0.300000011920929,1]

Appearance76.material = Material77

Shape75.appearance = Appearance76
Sphere78 = x3d.Sphere()
Sphere78.radius = 5.10000002384186

Shape75.geometry = Sphere78

Transform74.children.append(Shape75)

Anchor73.children.append(Transform74)

Transform18.children.append(Anchor73)
Anchor79 = x3d.Anchor()
Anchor79.url = ["javascript:window.open('https://coderextreme.net/X3DJSONLD/src/main/data/648.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');","javascript:window.open('./data/648.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor79.description = "Mantle Community Arts"
Transform80 = x3d.Transform()
Shape81 = x3d.Shape()
Appearance82 = x3d.Appearance()
Material83 = x3d.Material()
Material83.diffuseColor = [1,1,1]
Material83.emissiveColor = [0,0.300000011920929,1]

Appearance82.material = Material83

Shape81.appearance = Appearance82
Sphere84 = x3d.Sphere()
Sphere84.radius = 5.10000002384186

Shape81.geometry = Sphere84

Transform80.children.append(Shape81)

Anchor79.children.append(Transform80)

Transform18.children.append(Anchor79)
Anchor85 = x3d.Anchor()
Anchor85.url = ["javascript:window.open('https://coderextreme.net/X3DJSONLD/src/main/data/658.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');","javascript:window.open('./data/658.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor85.description = "Artlink East"
Transform86 = x3d.Transform()
Shape87 = x3d.Shape()
Appearance88 = x3d.Appearance()
Material89 = x3d.Material()
Material89.diffuseColor = [1,1,1]
Material89.emissiveColor = [0,0.300000011920929,1]

Appearance88.material = Material89

Shape87.appearance = Appearance88
Sphere90 = x3d.Sphere()
Sphere90.radius = 5.10000002384186

Shape87.geometry = Sphere90

Transform86.children.append(Shape87)

Anchor85.children.append(Transform86)

Transform18.children.append(Anchor85)
Anchor91 = x3d.Anchor()
Anchor91.url = ["javascript:window.open('https://coderextreme.net/X3DJSONLD/src/main/data/665.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');","javascript:window.open('./data/665.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor91.description = "Creations"
Transform92 = x3d.Transform()
Shape93 = x3d.Shape()
Appearance94 = x3d.Appearance()
Material95 = x3d.Material()
Material95.diffuseColor = [1,1,1]
Material95.emissiveColor = [0,0.300000011920929,1]

Appearance94.material = Material95

Shape93.appearance = Appearance94
Sphere96 = x3d.Sphere()
Sphere96.radius = 5.10000002384186

Shape93.geometry = Sphere96

Transform92.children.append(Shape93)

Anchor91.children.append(Transform92)

Transform18.children.append(Anchor91)
Anchor97 = x3d.Anchor()
Anchor97.url = ["javascript:window.open('https://coderextreme.net/X3DJSONLD/src/main/data/670.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');","javascript:window.open('./data/670.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor97.description = "New Perspectives"
Transform98 = x3d.Transform()
Shape99 = x3d.Shape()
Appearance100 = x3d.Appearance()
Material101 = x3d.Material()
Material101.diffuseColor = [1,1,1]
Material101.emissiveColor = [1,0,0.200000002980232]

Appearance100.material = Material101

Shape99.appearance = Appearance100
Sphere102 = x3d.Sphere()
Sphere102.radius = 5.10000002384186

Shape99.geometry = Sphere102

Transform98.children.append(Shape99)

Anchor97.children.append(Transform98)

Transform18.children.append(Anchor97)
Anchor103 = x3d.Anchor()
Anchor103.url = ["javascript:window.open('https://coderextreme.net/X3DJSONLD/src/main/data/671.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');","javascript:window.open('./data/671.html','details','height=550,width=400,top=50,left=50,menubar=no,status=no,toolbar=no,titlebar=no');"]
Anchor103.description = "UKan2"
Transform104 = x3d.Transform()
Shape105 = x3d.Shape()
Appearance106 = x3d.Appearance()
Material107 = x3d.Material()
Material107.diffuseColor = [1,1,1]
Material107.emissiveColor = [0,0.300000011920929,1]

Appearance106.material = Material107

Shape105.appearance = Appearance106
Sphere108 = x3d.Sphere()
Sphere108.radius = 5.10000002384186

Shape105.geometry = Sphere108

Transform104.children.append(Shape105)

Anchor103.children.append(Transform104)

Transform18.children.append(Anchor103)

Scene14.children.append(Transform18)

X3D0.Scene = Scene14
f = open("t3_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
