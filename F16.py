print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.0"
head1 = x3d.head()
meta2 = x3d.meta()
meta2.name = "title"
meta2.content = "F16.x3d"

head1.children.append(meta2)
meta3 = x3d.meta()
meta3.name = "description"
meta3.content = "F-16, The Fighting Falcon, Turkish Air Force (TUAF), Turkey"

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.name = "creator"
meta4.content = "Murat ONDER, LTJG, Turkish Navy"

head1.children.append(meta4)
meta5 = x3d.meta()
meta5.name = "creator"
meta5.content = "The coordinates of the main body (Except landing gears, nose antenna, flag, weapons, missile holders, cockpit, cockpit seat and fuel tanks) are mostly similar to the model of Soji Yamakawa and used with permission."

head1.children.append(meta5)
meta6 = x3d.meta()
meta6.name = "created"
meta6.content = "13 July 2003"

head1.children.append(meta6)
meta7 = x3d.meta()
meta7.name = "modified"
meta7.content = "27 November 2015"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.name = "reference"
meta8.content = "http://www.fas.org/man/dod-101/sys/ac/f-16.htm"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "permission"
meta9.content = "Here is a copy of the permission for the usage of the main hull; -----Original Message----- From: Soji Yamakawa [mailto:soji@andrew.cmu.edu] Sent: Tuesday, September 16, 2003 8:00 PM To: Onder, Murat TUR Subject: Re: VRML model points usage permission Sure. No problem. Soji ----- Original Message ----- From: \"Murat Onder\" <monder@nps.navy.mil> To: <Soji_Yamakawa@cmu.edu>; <PEB01130@nifty.ne.jp> Sent: Monday, September 15, 2003 3:50 PM Subject: VRML model points usage permission Hi Sir, I&apos;m a MS student in Naval Postgraduate School. I'm making a model of Turkish F-16 for my project in a VRML course. For the main hull of the F-16, I want to use the coordinate points of your VRML model since I think that model represents well enough F-16. This is going to be only a student project and will not be used for any commercial purposes. Of course I'll make the citation and put the reference links to your page in the meta files of x3d file. I'd like to know if you can give permission to use those points in my model. V/R, Murat Onder LTJG, TU NAVY"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "reference"
meta10.content = "The landing gears are taken from the Savage Archive, from F18 Blue Angel, then modified and re-animated."

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.name = "drawing"
meta11.content = "\"Drawing.jpg\" \"../../../Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/Drawing.jpg\" \"https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/Drawing.jpg\""

head1.children.append(meta11)
meta12 = x3d.meta()
meta12.name = "Image"
meta12.content = "\"FrontView.jpg\" \"FrontView2.jpg\" \"Missiles.jpg\" \"../../../Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/FrontView.jpg\" \"https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/FrontView.jpg\" \"../../../Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/FrontView2.jpg\" \"https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/FrontView2.jpg\" \"../../../Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/Missiles.jpg\" \"https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/Missiles.jpg\""

head1.children.append(meta12)
meta13 = x3d.meta()
meta13.name = "identifier"
meta13.content = "https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/F16.x3d"

head1.children.append(meta13)
meta14 = x3d.meta()
meta14.name = "subject"
meta14.content = "F16, F-16, Fighting Falcon"

head1.children.append(meta14)
meta15 = x3d.meta()
meta15.name = "generator"
meta15.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"

head1.children.append(meta15)
meta16 = x3d.meta()
meta16.name = "license"
meta16.content = "../../license.html"

head1.children.append(meta16)

X3D0.head = head1
Scene17 = x3d.Scene()
Transform18 = x3d.Transform()
Transform18.DEF = "F16Transform"
Transform19 = x3d.Transform()
Transform19.DEF = "MainFrameTransform"
Transform19.scale = [3,3,3]
Shape20 = x3d.Shape()
Shape20.DEF = "Nose"
Appearance21 = x3d.Appearance()
Material22 = x3d.Material()
Material22.diffuseColor = [0.25,0.25,0.25]

Appearance21.material = Material22

Shape20.appearance = Appearance21
IndexedFaceSet23 = x3d.IndexedFaceSet()
IndexedFaceSet23.coordIndex = [24,0,3,-1,4,0,24,-1,25,26,27,-1,28,25,27,-1,27,29,28,-1,27,30,29,-1,27,31,30,-1,3,18,24,-1]
IndexedFaceSet23.creaseAngle = 0.5
IndexedFaceSet23.normalIndex = [16,0,3,-1,4,0,16,-1,17,17,17,-1,18,18,18,-1,19,19,19,-1,20,20,20,-1,21,21,21,-1,3,14,16,-1]
IndexedFaceSet23.solid = False
Coordinate24 = x3d.Coordinate()
Coordinate24.DEF = "coordinates"
Coordinate24.point = (-0.3200,0.3600,-4.9100,-0.3800,0.4300,-4.2100,0.0000,0.6000,-4.2000,0.0000,0.5000,-4.9000,-0.5000,0.0000,-4.9000,-0.6000,0.0000,-4.2000,1.0000,0.0000,5.8000,1.0000,0.0000,5.3000,2.8000,-0.4000,6.3000,2.8000,-0.4000,6.6100,0.3100,-0.3600,-4.9000,0.4000,-0.3500,-4.2000,0.0000,-0.4000,-4.2000,0.0000,-0.4000,-4.9000,-0.3100,-0.3600,-4.9000,-0.4000,-0.3500,-4.2000,0.5000,0.0000,-4.9000,0.6000,0.0000,-4.2000,0.3200,0.3600,-4.9100,0.3800,0.4300,-4.2100,-1.0000,0.0000,5.8000,-1.0000,0.0000,5.3000,-2.8000,-0.4000,6.3000,-2.8000,-0.4000,6.6100,0.0000,-0.1000,-7.0000,-0.3100,-0.3600,-4.9000,-0.5000,0.0000,-4.9000,0.0000,-0.1000,-7.0000,0.0000,-0.4000,-4.9000,0.3100,-0.3600,-4.9000,0.5000,0.0000,-4.9000,0.3200,0.3600,-4.9100,-0.2700,0.9300,-3.5100,0.0000,1.1000,-3.6000,-0.3300,0.5000,-3.4100,-0.3400,0.9000,-1.7300,0.0000,0.9000,-1.0000,0.0000,1.1000,-1.8000,-0.3800,0.6400,-1.6800,0.3400,0.9000,-1.7300,0.0000,0.9000,-1.0000,0.3800,0.6400,-1.6800,0.3400,0.9000,-1.7300,0.2700,0.9300,-3.5100,0.3300,0.5000,-3.4100,0.0000,1.3000,-2.8000,0.4500,1.0200,-2.6800,0.3800,0.6400,-1.6800,0.5300,0.5000,-2.5600,-0.5300,0.5000,-2.5600,-0.4500,1.0200,-2.6800,-0.5300,0.7500,0.0000,-0.5600,0.6600,2.8000,0.0000,0.7000,2.8000,0.0000,0.8000,0.0000,-1.1000,0.3000,0.0000,-1.0000,0.3000,2.8000,-0.3700,0.5700,4.9000,0.0000,0.5900,4.9000,-0.7000,0.3000,4.9000,-0.7000,0.3000,4.9000,-0.7000,0.0000,7.0000,-0.5000,0.4900,7.0000,-0.5000,0.4900,7.0000,0.0000,0.7000,7.0000,-1.4000,0.0000,0.0000,-1.4000,0.0000,3.9000,-1.4000,0.0000,3.9000,-1.0000,0.0000,3.9000,-1.0000,0.3000,2.8000,-1.0000,0.3000,4.9000,-0.5900,0.6500,-0.7700,-0.8000,0.3000,-0.6000,-1.4000,0.0000,-0.7000,-1.0000,-0.1000,2.8000,-0.7000,-0.7000,-2.5000,-0.5000,-0.9000,-2.5000,-0.5000,-0.9000,-0.6000,-0.7000,-0.7000,-0.6000,0.0000,-1.0000,-2.5000,0.0000,-1.0000,-0.6000,-0.7200,-0.1200,-2.5000,-0.8000,-0.3000,-2.5000,-0.8000,-0.3000,-0.6000,-0.8000,-0.3000,-2.5000,-0.8000,-0.3000,-0.6000,-1.4000,0.0000,0.0000,-1.4000,0.0000,-0.7000,-0.7000,-0.1000,4.9000,-1.0000,-0.1000,4.9000,-0.5000,-0.9000,4.9000,-0.7000,-0.7000,4.9000,0.0000,-1.0000,4.9000,-0.7000,-0.1000,4.9000,-0.5000,-0.5000,7.0000,-0.7000,0.0000,7.0000,0.0000,-0.7000,7.0000,-1.0000,0.0000,7.4000,-2.8000,-0.4000,7.1000,-2.5700,-0.3200,7.4200,-4.9000,0.1000,4.0000,-5.1000,0.1000,4.0000,-5.1000,-0.1000,4.0000,-4.9000,-0.1000,4.0000,-5.1000,0.1000,1.6000,-5.1000,-0.1000,1.6000,-4.9000,0.1000,2.8000,-4.9000,-0.1000,2.8000,-0.5800,-0.8300,3.6000,-0.7200,-1.4000,3.9000,-0.6900,-1.3200,4.9000,-0.5800,-0.8300,4.9000,0.5800,-0.8300,3.6000,0.7200,-1.4000,3.9000,0.6900,-1.3200,4.9000,0.5800,-0.8300,4.9000,4.9000,-0.1000,2.8000,5.1000,-0.1000,1.6000,5.1000,-0.1000,4.0000,4.9000,-0.1000,4.0000,-0.8000,0.0000,-2.5000,4.9000,0.1000,4.0000,5.1000,0.1000,4.0000,5.1000,0.1000,1.6000,4.9000,0.1000,2.8000,0.5900,0.6500,-0.7700,0.8000,0.3000,-0.6000,0.8000,0.0000,-2.5000,-0.8000,0.0000,-2.5000,0.8000,-0.3000,-0.6000,0.7200,-0.1200,-2.5000,0.8000,0.0000,-2.5000,1.0000,0.0000,7.4000,2.8000,-0.4000,7.1000,2.5700,-0.3200,7.4200,-0.7000,0.0000,7.4000,0.5000,-0.9000,4.9000,0.7000,-0.7000,4.9000,0.5000,-0.5000,7.0000,-4.9000,0.0000,2.8000,-4.9000,0.0000,3.9000,0.7000,-0.1000,4.9000,0.7000,0.0000,7.0000,1.4000,0.0000,0.0000,4.9000,0.0000,2.8000,4.9000,0.0000,3.9000,1.4000,0.0000,3.9000,1.4000,0.0000,-0.7000,1.4000,0.0000,-0.7000,0.7000,-0.7000,-0.6000,0.8000,-0.3000,-0.6000,0.5000,-0.9000,-0.6000,1.0000,-0.1000,4.9000,1.0000,0.3000,4.9000,0.7000,0.0000,7.4000,0.7000,0.3000,4.9000,0.7000,-0.1000,4.9000,0.5600,0.6600,2.8000,0.5300,0.7500,0.0000,1.0000,0.3000,2.8000,1.1000,0.3000,0.0000,0.3700,0.5700,4.9000,0.7000,0.3000,4.9000,0.5000,0.4900,7.0000,0.7000,0.0000,7.0000,0.5000,0.4900,7.0000,1.4000,0.0000,3.9000,1.4000,0.0000,0.0000,1.0000,0.3000,2.8000,1.0000,0.0000,3.9000,1.0000,-0.1000,2.8000,0.5000,-0.9000,-2.5000,0.7000,-0.7000,-2.5000,0.8000,-0.3000,-2.5000,0.8000,-0.3000,-2.5000,1.0000,0.3000,3.9000,0.5900,0.6500,-0.7700,0.0000,0.7000,2.8000,0.0000,1.4000,4.5000,0.0000,0.5900,4.9000,0.0000,3.5000,6.8000,0.0000,3.5000,8.1000,0.0000,1.4000,7.3000,0.0000,0.7000,7.0000,0.0000,0.7000,7.3000,-1.0000,0.3000,3.9000,0.0000,0.3500,7.7000,-0.2500,0.2400,7.7000,-0.3500,0.0000,7.7000,-0.2500,-0.2500,7.7000,0.0000,-0.3500,7.7000,0.2500,-0.2500,7.7000,0.3500,0.0000,7.7000,0.2500,0.2400,7.7000,0.0000,-0.2000,-2.5000,0.7000,-0.7000,-2.5000,0.5000,-0.9000,-2.5000,0.0000,-1.0000,-2.5000,-0.5000,-0.9000,-2.5000,-0.7000,-0.7000,-2.5000,0.0000,-0.2000,-2.5000,-0.7200,-0.1200,-2.5000,0.7200,-0.1200,-2.5000,0.2500,0.2400,7.7000,0.3500,0.0000,7.7000,-0.3500,0.0000,7.7000,-0.2500,0.2400,7.7000)

IndexedFaceSet23.coord.append(Coordinate24)
Normal25 = x3d.Normal()
Normal25.DEF = "normalVector"
Normal25.vector = (-0.6800,0.7140,-0.1660,-0.6890,0.7210,-0.0720,0.0000,0.9650,-0.2600,0.0000,0.9850,-0.1750,-0.9900,-0.0160,-0.1380,-0.9990,-0.0220,-0.0370,0.5670,-0.8190,-0.0930,0.5610,-0.8280,0.0000,0.0000,-1.0000,0.0000,0.0000,-0.9970,-0.0710,-0.5670,-0.8190,-0.0930,-0.5610,-0.8280,0.0000,0.9900,-0.0160,-0.1380,0.9990,-0.0220,-0.0370,0.6800,0.7140,-0.1660,0.6890,0.7210,-0.0720,-0.3510,0.8890,-0.2940,-0.8680,-0.4590,-0.1900,-0.1300,-0.9820,-0.1400,0.1300,-0.9820,-0.1400,0.8680,-0.4590,-0.1900,0.8720,0.4310,-0.2310,-0.8340,0.4450,-0.3270,0.0000,0.9290,-0.3690,-0.8800,0.4010,-0.2560,-0.7990,0.5770,0.1690,-0.5800,0.7980,0.1640,0.0000,0.9980,0.0650,-0.8620,0.4860,0.1460,0.8860,0.2190,0.4080,0.7990,0.5770,0.1690,0.8340,0.4450,-0.3270,0.8800,0.4010,-0.2560,0.0000,0.9950,-0.0960,0.8420,0.5340,-0.0800,0.8620,0.4860,0.1460,0.8330,0.5490,-0.0730,-0.8330,0.5490,-0.0730,-0.8420,0.5340,-0.0800,-0.4850,0.8700,-0.0890,-0.3700,0.9290,0.0000,0.0000,1.0000,0.0000,0.0000,1.0000,-0.0100,-0.5920,0.7960,-0.1250,-0.5730,0.8180,0.0500,-0.3700,0.9290,-0.0100,0.0000,1.0000,-0.0250,-0.4870,0.8730,0.0360,-0.9230,0.3810,0.0500,-0.6830,0.7040,0.1950,0.0000,0.9900,0.1400,-0.7070,0.7070,0.0000,-0.3850,0.9120,0.1410,0.0000,0.9660,0.2590,-0.5630,0.8260,-0.0370,-0.6610,0.7380,-0.1380,-0.5210,0.8460,-0.1150,0.0000,-0.9960,0.0900,-0.7730,-0.4360,-0.4610,-0.4200,-0.7810,-0.4630,-0.4740,-0.8810,0.0000,-0.8710,-0.4920,0.0000,0.0000,-0.8910,-0.4550,-0.9170,0.3990,0.0000,-0.8810,0.0740,-0.4670,-0.9020,-0.4290,-0.0390,-0.0900,-0.9950,0.0500,-0.4510,-0.8920,0.0000,-0.2800,-0.9590,0.0400,-0.4680,-0.8780,0.0970,-0.8770,-0.4740,0.0850,0.0000,-0.9970,0.0720,-0.6930,-0.7200,0.0450,-0.7900,-0.5620,0.2440,-0.9680,0.0030,0.2500,0.0000,-0.9660,0.2570,0.0000,0.0000,1.0000,-1.0000,0.0000,0.0000,0.9870,0.0000,-0.1600,1.0000,0.0000,0.0000,-0.8310,-0.5510,-0.0800,0.5630,0.8260,-0.0370,0.6610,0.7380,-0.1380,0.9980,-0.0370,-0.0490,-0.9870,0.0000,-0.1600,-0.9980,-0.0370,-0.0490,0.8310,-0.5510,-0.0800,0.0000,-0.9990,0.0400,0.0000,0.9930,0.1200,0.4680,-0.8780,0.0970,0.8770,-0.4740,0.0850,0.7900,-0.5620,0.2440,-0.4190,-0.8970,-0.1400,0.6930,-0.7200,0.0450,0.9680,0.0030,0.2500,0.5210,0.8460,-0.1150,0.4190,-0.8970,-0.1400,0.8710,-0.4920,0.0000,0.9020,-0.4290,-0.0390,0.4740,-0.8810,0.0000,0.3700,0.9290,0.0000,0.4850,0.8700,-0.0890,0.5730,0.8180,0.0500,0.5920,0.7960,-0.1250,0.3700,0.9290,-0.0100,0.4870,0.8730,0.0360,0.9230,0.3810,0.0500,0.6830,0.7040,0.1950,0.3850,0.9120,0.1410,0.7070,0.7070,0.0000,0.4200,-0.7810,-0.4630,0.7730,-0.4360,-0.4610,0.9170,0.3990,0.0000,0.8810,0.0740,-0.4670,0.0900,-0.9950,0.0500,0.4510,-0.8920,0.0000,0.2800,-0.9590,0.0400,0.4200,0.9010,-0.1100,0.0000,0.6660,0.7460,-0.4810,0.4680,0.7410,-0.6740,0.0000,0.7380,-0.4750,-0.4750,0.7410,0.0000,-0.6740,0.7380,0.4750,-0.4750,0.7410,0.6740,0.0000,0.7380,0.4810,0.4680,0.7410,0.0000,0.0000,-1.0000,0.0000,-0.8930,-0.4500,-0.9010,-0.2240,-0.3720,0.9010,-0.2240,-0.3720,0.8410,0.3400,0.4210,-0.8410,0.3400,0.4210)

IndexedFaceSet23.normal.append(Normal25)

Shape20.geometry = IndexedFaceSet23

Transform19.children.append(Shape20)
Shape26 = x3d.Shape()
Shape26.DEF = "Canopy"
Appearance27 = x3d.Appearance()
Material28 = x3d.Material()
Material28.diffuseColor = [0.25,0.25,0.25]
Material28.transparency = 0.8

Appearance27.material = Material28

Shape26.appearance = Appearance27
IndexedFaceSet29 = x3d.IndexedFaceSet()
IndexedFaceSet29.coordIndex = [2,32,33,-1,34,32,2,-1,35,36,37,-1,38,36,35,-1,39,40,41,-1,37,36,42,-1,2,43,44,-1,33,43,2,-1,45,37,42,46,-1,46,42,47,48,-1,33,45,46,43,-1,43,46,48,44,-1,34,49,50,32,-1,32,50,45,33,-1,49,38,35,50,-1,50,35,37,45,-1]
IndexedFaceSet29.creaseAngle = 0.5
IndexedFaceSet29.normalIndex = [2,22,23,-1,24,22,2,-1,25,26,27,-1,28,26,25,-1,29,29,29,-1,27,26,30,-1,2,31,32,-1,23,31,2,-1,33,27,30,34,-1,34,30,35,36,-1,23,33,34,31,-1,31,34,36,32,-1,24,37,38,22,-1,22,38,33,23,-1,37,28,25,38,-1,38,25,27,33,-1]
IndexedFaceSet29.solid = False
Coordinate30 = x3d.Coordinate()
Coordinate30.USE = "coordinates"

IndexedFaceSet29.coord.append(Coordinate30)
Normal31 = x3d.Normal()
Normal31.USE = "normalVector"

IndexedFaceSet29.normal.append(Normal31)

Shape26.geometry = IndexedFaceSet29

Transform19.children.append(Shape26)
Shape32 = x3d.Shape()
Shape32.DEF = "MainBodyAndWingEdges"
Appearance33 = x3d.Appearance()
Material34 = x3d.Material()
Material34.diffuseColor = [0.1796,0.1914,0.2382]

Appearance33.material = Material34

Shape32.appearance = Appearance33
IndexedFaceSet35 = x3d.IndexedFaceSet()
IndexedFaceSet35.coordIndex = [51,52,53,54,-1,55,56,52,51,-1,52,57,58,53,-1,56,59,57,52,-1,60,61,62,-1,57,59,63,-1,57,63,64,-1,58,57,64,-1,56,55,65,66,-1,67,68,69,-1,69,70,60,-1,71,54,36,-1,51,54,71,-1,72,51,71,-1,55,51,72,-1,72,73,55,-1,65,55,73,-1,68,67,74,-1,75,76,77,78,-1,76,79,80,77,-1,81,82,83,-1,84,75,78,85,-1,83,74,67,-1,67,86,87,83,-1,74,88,89,-1,88,74,83,-1,78,77,90,91,-1,77,80,92,90,-1,85,91,93,-1,85,78,91,-1,94,95,93,-1,94,93,91,-1,91,96,94,-1,96,91,90,-1,90,92,96,-1,100,101,102,103,-1,101,104,105,102,-1,104,106,107,105,-1,106,100,103,107,-1,106,104,101,100,-1,103,102,105,107,-1,116,117,118,119,-1,120,81,83,-1,121,122,123,124,-1,116,119,121,124,-1,48,125,126,127,-1,117,116,124,123,-1,128,72,71,49,-1,118,117,123,122,-1,119,118,122,121,-1,129,130,131,-1,89,88,135,97,-1,60,70,97,135,-1,70,89,97,-1,96,92,136,-1,136,137,96,-1,138,96,137,-1,120,83,87,-1,128,73,72,-1,137,141,138,-1,141,142,138,-1,126,147,127,-1,148,129,131,-1,137,149,150,-1,141,137,150,-1,136,92,80,151,-1,137,136,151,149,-1,132,152,153,-1,154,132,153,155,-1,132,154,156,152,-1,54,53,157,158,-1,158,157,159,160,-1,53,58,161,157,-1,157,161,162,159,-1,163,164,155,-1,165,162,161,-1,64,165,161,-1,64,161,58,-1,166,167,160,159,-1,168,169,146,-1,155,153,168,-1,36,54,125,-1,125,54,158,-1,125,158,126,-1,126,158,160,-1,160,147,126,-1,147,160,167,-1,170,146,169,-1,149,151,171,172,-1,151,80,79,171,-1,129,173,130,-1,150,149,172,174,-1,146,170,129,-1,129,148,143,146,-1,152,156,170,-1,129,170,156,-1,156,154,164,-1,154,155,164,-1,168,175,169,-1,175,153,152,169,-1,152,170,169,-1,48,47,125,-1,41,40,176,-1,71,38,49,-1,71,36,38,-1,61,135,88,-1,61,60,135,-1,68,185,69,-1,68,74,89,-1,68,89,70,185,-1]
IndexedFaceSet35.creaseAngle = 0.5
IndexedFaceSet35.normalIndex = [39,40,41,42,-1,43,44,40,39,-1,40,45,46,41,-1,44,47,45,40,-1,48,48,48,-1,45,47,49,-1,45,49,50,-1,46,45,50,-1,44,43,51,52,-1,53,53,53,-1,41,41,41,-1,54,42,26,-1,39,42,54,-1,55,39,54,-1,43,39,55,-1,55,56,43,-1,51,43,56,-1,57,57,57,-1,58,59,60,61,-1,59,62,8,60,-1,63,63,63,-1,64,58,61,65,-1,66,66,66,-1,67,67,67,67,-1,8,8,8,-1,68,68,68,-1,61,60,69,70,-1,60,8,71,69,-1,65,70,72,-1,65,61,70,-1,73,74,72,-1,73,72,70,-1,70,75,73,-1,75,70,69,-1,69,71,75,-1,76,76,76,76,-1,77,77,77,77,-1,78,78,78,78,-1,79,79,79,79,-1,41,41,41,41,-1,8,8,8,8,-1,8,8,8,8,-1,80,80,80,-1,41,41,41,41,-1,77,77,77,77,-1,36,81,82,83,-1,84,84,84,84,-1,85,55,54,37,-1,79,79,79,79,-1,76,76,76,76,-1,86,86,86,-1,87,87,87,87,-1,88,88,88,88,-1,77,77,77,-1,75,71,89,-1,89,90,75,-1,91,75,90,-1,92,92,92,-1,85,56,55,-1,90,93,91,-1,93,94,91,-1,82,95,83,-1,96,96,96,-1,90,97,98,-1,93,90,98,-1,89,71,8,99,-1,90,89,99,97,-1,79,79,79,-1,88,88,88,88,-1,87,87,87,87,-1,42,41,100,101,-1,101,100,102,103,-1,41,46,104,100,-1,100,104,105,102,-1,106,106,106,-1,107,105,104,-1,50,107,104,-1,50,104,46,-1,108,109,103,102,-1,53,53,53,-1,41,41,41,-1,26,42,81,-1,81,42,101,-1,81,101,82,-1,82,101,103,-1,103,95,82,-1,95,103,109,-1,57,57,57,-1,97,99,110,111,-1,99,8,62,110,-1,112,112,112,-1,98,97,111,113,-1,114,114,114,-1,115,115,115,115,-1,8,8,8,-1,116,116,116,-1,77,77,77,-1,77,77,77,-1,79,79,79,-1,79,79,79,79,-1,79,79,79,-1,36,35,81,-1,117,117,117,-1,54,28,37,-1,54,26,28,-1,79,79,79,-1,79,79,79,-1,77,77,77,-1,77,77,77,-1,77,77,77,77,-1]
IndexedFaceSet35.solid = False
Coordinate36 = x3d.Coordinate()
Coordinate36.USE = "coordinates"

IndexedFaceSet35.coord.append(Coordinate36)
Normal37 = x3d.Normal()
Normal37.USE = "normalVector"

IndexedFaceSet35.normal.append(Normal37)

Shape32.geometry = IndexedFaceSet35

Transform19.children.append(Shape32)
Shape38 = x3d.Shape()
Shape38.DEF = "ExhaustExitFlatPanel"
Appearance39 = x3d.Appearance()
Material40 = x3d.Material()
Material40.diffuseColor = [0.5,0.5,0.5]

Appearance39.material = Material40

Shape38.appearance = Appearance39
IndexedFaceSet41 = x3d.IndexedFaceSet()
IndexedFaceSet41.coordIndex = [186,187,188,189,190,-1,190,191,192,193,186,-1]
IndexedFaceSet41.creaseAngle = 0.5
IndexedFaceSet41.normalIndex = [118,119,120,121,122,-1,122,123,124,125,118,-1]
IndexedFaceSet41.solid = False
Coordinate42 = x3d.Coordinate()
Coordinate42.USE = "coordinates"

IndexedFaceSet41.coord.append(Coordinate42)
Normal43 = x3d.Normal()
Normal43.USE = "normalVector"

IndexedFaceSet41.normal.append(Normal43)

Shape38.geometry = IndexedFaceSet41

Transform19.children.append(Shape38)
Shape44 = x3d.Shape()
Shape44.DEF = "ExhaustEntranceFrontBottomPart"
Appearance45 = x3d.Appearance()
Material46 = x3d.Material()
Material46.diffuseColor = [0.2304,0.2304,0.2304]

Appearance45.material = Material46

Shape44.appearance = Appearance45
IndexedFaceSet47 = x3d.IndexedFaceSet()
IndexedFaceSet47.coordIndex = [194,130,173,195,196,197,-1,197,198,199,82,81,194,-1]
IndexedFaceSet47.creaseAngle = 0.5
IndexedFaceSet47.normalIndex = [126,126,126,126,126,126,-1,126,126,126,126,126,126,-1]
IndexedFaceSet47.solid = False
Coordinate48 = x3d.Coordinate()
Coordinate48.USE = "coordinates"

IndexedFaceSet47.coord.append(Coordinate48)
Normal49 = x3d.Normal()
Normal49.USE = "normalVector"

IndexedFaceSet47.normal.append(Normal49)

Shape44.geometry = IndexedFaceSet47

Transform19.children.append(Shape44)
Shape50 = x3d.Shape()
Shape50.DEF = "ThirdPartFromNoseUnderCanopy"
Appearance51 = x3d.Appearance()
Material52 = x3d.Material()
Material52.diffuseColor = [0.6,0.6,0.6]

Appearance51.material = Material52

Shape50.appearance = Appearance51
IndexedFaceSet53 = x3d.IndexedFaceSet()
IndexedFaceSet53.coordIndex = [12,200,201,15,-1,19,48,127,17,-1,15,201,128,5,-1,17,127,202,11,-1,11,202,200,12,-1,5,128,49,1,-1,48,19,44,-1,19,2,44,-1,34,1,49,-1,34,2,1,-1]
IndexedFaceSet53.creaseAngle = 0.5
IndexedFaceSet53.normalIndex = [8,127,128,11,-1,15,36,83,13,-1,11,128,85,5,-1,13,83,129,7,-1,7,129,127,8,-1,5,85,37,1,-1,36,15,32,-1,15,2,32,-1,24,1,37,-1,24,2,1,-1]
IndexedFaceSet53.solid = False
Coordinate54 = x3d.Coordinate()
Coordinate54.USE = "coordinates"

IndexedFaceSet53.coord.append(Coordinate54)
Normal55 = x3d.Normal()
Normal55.USE = "normalVector"

IndexedFaceSet53.normal.append(Normal55)

Shape50.geometry = IndexedFaceSet53

Transform19.children.append(Shape50)
Shape56 = x3d.Shape()
Shape56.DEF = "RearExhaustExitPartLastPartOfMainBody"
Appearance57 = x3d.Appearance()
Material58 = x3d.Material()
Material58.diffuseColor = [0.37,0.37,0.37]
Material58.shininess = 0.5

Appearance57.material = Material58

Shape56.appearance = Appearance57
IndexedFaceSet59 = x3d.IndexedFaceSet()
IndexedFaceSet59.coordIndex = [64,186,193,165,-1,203,204,164,163,-1,192,191,138,142,-1,191,190,96,138,-1,94,96,190,189,-1,95,94,189,188,-1,63,187,186,64,-1,62,61,205,206,-1]
IndexedFaceSet59.creaseAngle = 0.5
IndexedFaceSet59.normalIndex = [50,118,125,107,-1,130,130,130,130,-1,124,123,91,94,-1,123,122,75,91,-1,73,75,122,121,-1,74,73,121,120,-1,49,119,118,50,-1,131,131,131,131,-1]
IndexedFaceSet59.solid = False
Coordinate60 = x3d.Coordinate()
Coordinate60.USE = "coordinates"

IndexedFaceSet59.coord.append(Coordinate60)
Normal61 = x3d.Normal()
Normal61.USE = "normalVector"

IndexedFaceSet59.normal.append(Normal61)

Shape56.geometry = IndexedFaceSet59

Transform19.children.append(Shape56)
Shape62 = x3d.Shape()
Shape62.DEF = "WingsAndTail"
Appearance63 = x3d.Appearance()
Material64 = x3d.Material()
Material64.emissiveColor = [0.1796,0.1914,0.2382]

Appearance63.material = Material64

Shape62.appearance = Appearance63
IndexedFaceSet65 = x3d.IndexedFaceSet()
IndexedFaceSet65.colorPerVertex = False
IndexedFaceSet65.coordIndex = [6,7,8,9,-1,9,8,7,6,-1,20,21,22,23,-1,23,22,21,20,-1,97,20,23,98,99,-1,99,98,23,20,97,-1,108,109,110,111,-1,111,110,109,108,-1,112,113,114,115,-1,115,114,113,112,-1,132,6,9,133,134,-1,134,133,9,6,132,-1,86,139,140,67,-1,67,140,139,86,-1,143,144,145,146,-1,146,145,144,143,-1,177,178,179,-1,179,178,177,-1,178,180,181,182,183,179,-1,179,183,182,181,180,178,-1,182,184,183,-1,183,184,182,-1,177,178,179,-1,179,178,177,-1,178,180,181,182,183,179,-1,179,183,182,181,180,178,-1,182,184,183,-1,183,184,182,-1]
IndexedFaceSet65.creaseAngle = 0.5
IndexedFaceSet65.normalIndex = [50,118,125,107,-1,130,130,130,130,-1,124,123,91,94,-1,123,122,75,91,-1,73,75,122,121,-1,74,73,121,120,-1,49,119,118,50,-1,131,131,131,131,-1]
IndexedFaceSet65.solid = False
Coordinate66 = x3d.Coordinate()
Coordinate66.USE = "coordinates"

IndexedFaceSet65.coord.append(Coordinate66)
Normal67 = x3d.Normal()
Normal67.USE = "normalVector"

IndexedFaceSet65.normal.append(Normal67)

Shape62.geometry = IndexedFaceSet65

Transform19.children.append(Shape62)
Shape68 = x3d.Shape()
Shape68.DEF = "SecondPartAfterNose"
Appearance69 = x3d.Appearance()
Material70 = x3d.Material()
Material70.diffuseColor = [0.6,0.6,0.6]

Appearance69.material = Material70

Shape68.appearance = Appearance69
IndexedFaceSet71 = x3d.IndexedFaceSet()
IndexedFaceSet71.coordIndex = [0,1,2,3,-1,4,5,1,0,-1,10,11,12,13,-1,14,15,5,4,-1,13,12,15,14,-1,16,17,11,10,-1,18,19,17,16,-1,3,2,19,18,-1]
IndexedFaceSet71.creaseAngle = 0.5
IndexedFaceSet71.normalIndex = [0,1,2,3,-1,4,5,1,0,-1,6,7,8,9,-1,10,11,5,4,-1,9,8,11,10,-1,12,13,7,6,-1,14,15,13,12,-1,3,2,15,14,-1]
IndexedFaceSet71.solid = False
Coordinate72 = x3d.Coordinate()
Coordinate72.USE = "coordinates"

IndexedFaceSet71.coord.append(Coordinate72)
Normal73 = x3d.Normal()
Normal73.USE = "normalVector"

IndexedFaceSet71.normal.append(Normal73)

Shape68.geometry = IndexedFaceSet71

Transform19.children.append(Shape68)

Transform18.children.append(Transform19)
Transform74 = x3d.Transform()
Transform74.DEF = "CockpitTransform"
Transform74.rotation = [1,0,0,-0.1]
Transform74.scale = [0.045,0.045,0.045]
Transform74.translation = [0,1,-10]
Inline75 = x3d.Inline()
Inline75.url = ["Cockpit.x3d","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/Cockpit.x3d","Cockpit.wrl","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/Cockpit.wrl"]

Transform74.children.append(Inline75)

Transform18.children.append(Transform74)
Transform76 = x3d.Transform()
Transform76.DEF = "SeatTransform"
Transform76.rotation = [-1,0,0,-0.1]
Transform76.scale = [0.9,0.9,0.9]
Transform76.translation = [0,0,-8.3]
Inline77 = x3d.Inline()
Inline77.url = ["Seat.x3d","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/Seat.x3d","Seat.wrl","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/Seat.wrl"]

Transform76.children.append(Inline77)

Transform18.children.append(Transform76)
Transform78 = x3d.Transform()
Transform78.DEF = "FrontWheelTransform"
Transform78.center = [0,2.5,0]
Transform78.rotation = [-1,0,0,1.92]
Transform78.translation = [0.7,-5.2,-6.5]
#Front wheel is taken from the Savage Library, modified and re-animated.(from F18 Blue Angel)
Inline79 = x3d.Inline()
Inline79.url = ["FrontWheel.x3d","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/FrontWheel.x3d","FrontWheel.wrl","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/FrontWheel.wrl"]

Transform78.children.append(Inline79)

Transform18.children.append(Transform78)
Transform80 = x3d.Transform()
Transform80.DEF = "RearLeftWheelTransform"
Transform80.center = [0,2.5,0]
Transform80.rotation = [1,0,1,1.92]
Transform80.translation = [-2.95,-5,7]
#Rear wheels are taken from the Savage Library and re-animated (from F18 Blue Angel)
Inline81 = x3d.Inline()
Inline81.url = ["RearLeftWheel.x3d","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/RearLeftWheel.x3d","RearLeftWheel.wrl","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/RearLeftWheel.wrl"]

Transform80.children.append(Inline81)

Transform18.children.append(Transform80)
Transform82 = x3d.Transform()
Transform82.DEF = "RearRightWheelTransform"
Transform82.center = [0,2.5,0]
Transform82.rotation = [-1,0,-1,1.92]
Transform82.translation = [2.95,-5,7]
#Rear wheels are taken from the Savage Library and re-animated (from F18 Blue Angel)
Inline83 = x3d.Inline()
Inline83.url = ["RearRightWheel.x3d","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/RearRightWheel.x3d","RearRightWheel.wrl","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/RearRightWheel.wrl"]

Transform82.children.append(Inline83)

Transform18.children.append(Transform82)
Transform84 = x3d.Transform()
Transform84.DEF = "CockpitButtonsTransform"
Transform85 = x3d.Transform()
Transform85.DEF = "UpButtonTransform"
Transform85.rotation = [1,0,0,1.57]
Transform85.scale = [0.008,0.008,0.008]
Transform85.translation = [-0.95,1.05,-10]
Shape86 = x3d.Shape()
Cylinder87 = x3d.Cylinder()
Cylinder87.height = 1
Cylinder87.radius = 4

Shape86.geometry = Cylinder87
Appearance88 = x3d.Appearance()
Material89 = x3d.Material()
Material89.diffuseColor = [1,0,0]
Material89.shininess = 0.8

Appearance88.material = Material89

Shape86.appearance = Appearance88

Transform85.children.append(Shape86)
TouchSensor90 = x3d.TouchSensor()
TouchSensor90.DEF = "TouchSensorUp"
TouchSensor90.description = "click for gears up"

Transform85.children.append(TouchSensor90)

Transform84.children.append(Transform85)
Transform91 = x3d.Transform()
Transform91.DEF = "DownButtonTransform"
Transform91.rotation = [1,0,0,1.57]
Transform91.scale = [0.008,0.008,0.008]
Transform91.translation = [-0.83,1.05,-10]
Shape92 = x3d.Shape()
Cylinder93 = x3d.Cylinder()
Cylinder93.height = 1
Cylinder93.radius = 4

Shape92.geometry = Cylinder93
Appearance94 = x3d.Appearance()
Material95 = x3d.Material()
Material95.diffuseColor = [1,1,0]
Material95.shininess = 0.8

Appearance94.material = Material95

Shape92.appearance = Appearance94

Transform91.children.append(Shape92)
TouchSensor96 = x3d.TouchSensor()
TouchSensor96.DEF = "TouchSensorDown"
TouchSensor96.description = "click for gears down"

Transform91.children.append(TouchSensor96)

Transform84.children.append(Transform91)
Transform97 = x3d.Transform()
Transform97.DEF = "GearUpTextTransform"
Transform97.scale = [0.06,0.06,0.06]
Transform97.translation = [-0.65,1.55,-10]
Shape98 = x3d.Shape()
Text99 = x3d.Text()
Text99.string = ["RED Button","Gear Up"]

Shape98.geometry = Text99
Appearance100 = x3d.Appearance()
Material101 = x3d.Material()
Material101.diffuseColor = [1,0,0]

Appearance100.material = Material101

Shape98.appearance = Appearance100

Transform97.children.append(Shape98)

Transform84.children.append(Transform97)
Transform102 = x3d.Transform()
Transform102.DEF = "GearDownTextTransform"
Transform102.scale = [0.06,0.06,0.06]
Transform102.translation = [-0.65,1.35,-10]
Shape103 = x3d.Shape()
Text104 = x3d.Text()
Text104.length = [5.5]
Text104.string = ["YELLOW Button","Gear Down"]

Shape103.geometry = Text104
Appearance105 = x3d.Appearance()
Material106 = x3d.Material()
Material106.diffuseColor = [1,1,0]

Appearance105.material = Material106

Shape103.appearance = Appearance105

Transform102.children.append(Shape103)

Transform84.children.append(Transform102)
Transform107 = x3d.Transform()
Transform107.DEF = "FireButtonTransform"
Transform107.rotation = [1,0,0,1.57]
Transform107.scale = [0.008,0.008,0.008]
Transform107.translation = [0.52,1.6,-10]
Shape108 = x3d.Shape()
Cylinder109 = x3d.Cylinder()
Cylinder109.height = 1
Cylinder109.radius = 4

Shape108.geometry = Cylinder109
Appearance110 = x3d.Appearance()
Material111 = x3d.Material()
Material111.diffuseColor = [0,0.75,0.18]
Material111.shininess = 0.8

Appearance110.material = Material111

Shape108.appearance = Appearance110

Transform107.children.append(Shape108)
TouchSensor112 = x3d.TouchSensor()
TouchSensor112.DEF = "FireSensor"
TouchSensor112.description = "click to fire"

Transform107.children.append(TouchSensor112)

Transform84.children.append(Transform107)
Transform113 = x3d.Transform()
Transform113.DEF = "FireTextTransform"
Transform113.scale = [0.06,0.06,0.06]
Transform113.translation = [0.36,1.5,-10]
Shape114 = x3d.Shape()
Text115 = x3d.Text()
Text115.string = ["Target Locked"," FIRE!..","(Green Button)"]

Shape114.geometry = Text115
Appearance116 = x3d.Appearance()
Material117 = x3d.Material()
Material117.diffuseColor = [0,0.75,0.18]

Appearance116.material = Material117

Shape114.appearance = Appearance116

Transform113.children.append(Shape114)

Transform84.children.append(Transform113)

Transform18.children.append(Transform84)
Viewpoint118 = x3d.Viewpoint()
Viewpoint118.description = "F16 Close Look-up"
Viewpoint118.orientation = [-0.559,-0.827,-0.057,1.3534]
Viewpoint118.position = [-28.7,19.9,17.4]

Transform18.children.append(Viewpoint118)
Viewpoint119 = x3d.Viewpoint()
Viewpoint119.description = "Cockpit"
Viewpoint119.orientation = [-1,0,0,0.1249]
Viewpoint119.position = [0,1.5,-7.9]

Transform18.children.append(Viewpoint119)
Viewpoint120 = x3d.Viewpoint()
Viewpoint120.DEF = "LandingGearAnimationView"
Viewpoint120.description = "Landing Gear Animation View"
Viewpoint120.orientation = [-0.003,1,-0.012,2.5741]
Viewpoint120.position = [16.1,-5.8,-24.6]

Transform18.children.append(Viewpoint120)
Viewpoint121 = x3d.Viewpoint()
Viewpoint121.description = "Cockpit Left View"
Viewpoint121.orientation = [-0.276,-0.922,-0.271,1.2338]
Viewpoint121.position = [-6.7,6.1,-3.9]

Transform18.children.append(Viewpoint121)
Viewpoint122 = x3d.Viewpoint()
Viewpoint122.description = "F-16 Front View"
Viewpoint122.orientation = [-0.007,0.995,0.102,3.1152]
Viewpoint122.position = [-0.1,13.4,-65]

Transform18.children.append(Viewpoint122)
Viewpoint123 = x3d.Viewpoint()
Viewpoint123.description = "Cockpit Target View"
Viewpoint123.orientation = [-0.834,-0.523,-0.176,0.0875]
Viewpoint123.position = [0,2.4,-7.9]

Transform18.children.append(Viewpoint123)
Transform124 = x3d.Transform()
Transform124.DEF = "NoseAntennaTransform"
Transform124.rotation = [1,0,0,1.57]
Transform124.translation = [0,-0.275,-21]
Shape125 = x3d.Shape()
Cylinder126 = x3d.Cylinder()
Cylinder126.radius = 0.05

Shape125.geometry = Cylinder126
Appearance127 = x3d.Appearance()
Material128 = x3d.Material()
Material128.diffuseColor = [0.5,0.5,0.5]
Material128.shininess = 0.5

Appearance127.material = Material128

Shape125.appearance = Appearance127

Transform124.children.append(Shape125)

Transform18.children.append(Transform124)

Scene17.children.append(Transform18)
TimeSensor129 = x3d.TimeSensor()
TimeSensor129.DEF = "WheelUp"
TimeSensor129.cycleInterval = 8

Scene17.children.append(TimeSensor129)
OrientationInterpolator130 = x3d.OrientationInterpolator()
OrientationInterpolator130.DEF = "GearUpInterpolator"
OrientationInterpolator130.key = [0,0.5,1]
OrientationInterpolator130.keyValue = (1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,-0.7900,1.0000,0.0000,0.0000,-1.9200)

Scene17.children.append(OrientationInterpolator130)
ROUTE131 = x3d.ROUTE()
ROUTE131.fromField = "touchTime"
ROUTE131.fromNode = "TouchSensorUp"
ROUTE131.toField = "set_startTime"
ROUTE131.toNode = "WheelUp"

Scene17.children.append(ROUTE131)
ROUTE132 = x3d.ROUTE()
ROUTE132.fromField = "fraction_changed"
ROUTE132.fromNode = "WheelUp"
ROUTE132.toField = "set_fraction"
ROUTE132.toNode = "GearUpInterpolator"

Scene17.children.append(ROUTE132)
ROUTE133 = x3d.ROUTE()
ROUTE133.fromField = "value_changed"
ROUTE133.fromNode = "GearUpInterpolator"
ROUTE133.toField = "set_rotation"
ROUTE133.toNode = "FrontWheelTransform"

Scene17.children.append(ROUTE133)
TimeSensor134 = x3d.TimeSensor()
TimeSensor134.DEF = "WheelDown"
TimeSensor134.cycleInterval = 8

Scene17.children.append(TimeSensor134)
OrientationInterpolator135 = x3d.OrientationInterpolator()
OrientationInterpolator135.DEF = "GearDownInterpolator"
OrientationInterpolator135.key = [0,0.5,1]
OrientationInterpolator135.keyValue = (1.0000,0.0000,0.0000,-1.9200,1.0000,0.0000,0.0000,-0.7900,1.0000,0.0000,0.0000,0.0000)

Scene17.children.append(OrientationInterpolator135)
ROUTE136 = x3d.ROUTE()
ROUTE136.fromField = "touchTime"
ROUTE136.fromNode = "TouchSensorDown"
ROUTE136.toField = "set_startTime"
ROUTE136.toNode = "WheelDown"

Scene17.children.append(ROUTE136)
ROUTE137 = x3d.ROUTE()
ROUTE137.fromField = "fraction_changed"
ROUTE137.fromNode = "WheelDown"
ROUTE137.toField = "set_fraction"
ROUTE137.toNode = "GearDownInterpolator"

Scene17.children.append(ROUTE137)
ROUTE138 = x3d.ROUTE()
ROUTE138.fromField = "value_changed"
ROUTE138.fromNode = "GearDownInterpolator"
ROUTE138.toField = "set_rotation"
ROUTE138.toNode = "FrontWheelTransform"

Scene17.children.append(ROUTE138)
#Animation commands for Rear Right Wheel Starts
TimeSensor139 = x3d.TimeSensor()
TimeSensor139.DEF = "RRearUp1"
TimeSensor139.cycleInterval = 8

Scene17.children.append(TimeSensor139)
TimeSensor140 = x3d.TimeSensor()
TimeSensor140.DEF = "RRearDown1"
TimeSensor140.cycleInterval = 8

Scene17.children.append(TimeSensor140)
OrientationInterpolator141 = x3d.OrientationInterpolator()
OrientationInterpolator141.DEF = "RRearInterUp1"
OrientationInterpolator141.key = [0,0.5,1]
OrientationInterpolator141.keyValue = (-1.0000,0.0000,-1.0000,0.0000,-1.0000,0.0000,-1.0000,0.4400,-1.0000,0.0000,-1.0000,1.9200)

Scene17.children.append(OrientationInterpolator141)
OrientationInterpolator142 = x3d.OrientationInterpolator()
OrientationInterpolator142.DEF = "RRearInterDown1"
OrientationInterpolator142.key = [0,0.5,1]
OrientationInterpolator142.keyValue = (-1.0000,0.0000,-1.0000,1.9200,-1.0000,0.0000,-1.0000,0.4400,-1.0000,0.0000,-1.0000,0.0000)

Scene17.children.append(OrientationInterpolator142)
ROUTE143 = x3d.ROUTE()
ROUTE143.fromField = "touchTime"
ROUTE143.fromNode = "TouchSensorDown"
ROUTE143.toField = "set_startTime"
ROUTE143.toNode = "RRearDown1"

Scene17.children.append(ROUTE143)
ROUTE144 = x3d.ROUTE()
ROUTE144.fromField = "touchTime"
ROUTE144.fromNode = "TouchSensorUp"
ROUTE144.toField = "set_startTime"
ROUTE144.toNode = "RRearUp1"

Scene17.children.append(ROUTE144)
ROUTE145 = x3d.ROUTE()
ROUTE145.fromField = "fraction_changed"
ROUTE145.fromNode = "RRearDown1"
ROUTE145.toField = "set_fraction"
ROUTE145.toNode = "RRearInterDown1"

Scene17.children.append(ROUTE145)
ROUTE146 = x3d.ROUTE()
ROUTE146.fromField = "fraction_changed"
ROUTE146.fromNode = "RRearUp1"
ROUTE146.toField = "set_fraction"
ROUTE146.toNode = "RRearInterUp1"

Scene17.children.append(ROUTE146)
ROUTE147 = x3d.ROUTE()
ROUTE147.fromField = "value_changed"
ROUTE147.fromNode = "RRearInterDown1"
ROUTE147.toField = "set_rotation"
ROUTE147.toNode = "RearRightWheelTransform"

Scene17.children.append(ROUTE147)
ROUTE148 = x3d.ROUTE()
ROUTE148.fromField = "value_changed"
ROUTE148.fromNode = "RRearInterUp1"
ROUTE148.toField = "set_rotation"
ROUTE148.toNode = "RearRightWheelTransform"

Scene17.children.append(ROUTE148)
#Animation commands for Rear Left Wheel
TimeSensor149 = x3d.TimeSensor()
TimeSensor149.DEF = "LRearUp1"
TimeSensor149.cycleInterval = 8

Scene17.children.append(TimeSensor149)
TimeSensor150 = x3d.TimeSensor()
TimeSensor150.DEF = "LRearDown1"
TimeSensor150.cycleInterval = 8

Scene17.children.append(TimeSensor150)
OrientationInterpolator151 = x3d.OrientationInterpolator()
OrientationInterpolator151.DEF = "LRearInterUp1"
OrientationInterpolator151.key = [0,0.5,1]
OrientationInterpolator151.keyValue = (1.0000,0.0000,1.0000,0.0000,1.0000,0.0000,1.0000,0.4400,1.0000,0.0000,1.0000,1.9200)

Scene17.children.append(OrientationInterpolator151)
OrientationInterpolator152 = x3d.OrientationInterpolator()
OrientationInterpolator152.DEF = "LRearInterDown1"
OrientationInterpolator152.key = [0,0.5,1]
OrientationInterpolator152.keyValue = (1.0000,0.0000,1.0000,1.9200,1.0000,0.0000,1.0000,0.4400,1.0000,0.0000,1.0000,0.0000)

Scene17.children.append(OrientationInterpolator152)
ROUTE153 = x3d.ROUTE()
ROUTE153.fromField = "touchTime"
ROUTE153.fromNode = "TouchSensorDown"
ROUTE153.toField = "set_startTime"
ROUTE153.toNode = "LRearDown1"

Scene17.children.append(ROUTE153)
ROUTE154 = x3d.ROUTE()
ROUTE154.fromField = "touchTime"
ROUTE154.fromNode = "TouchSensorUp"
ROUTE154.toField = "set_startTime"
ROUTE154.toNode = "LRearUp1"

Scene17.children.append(ROUTE154)
ROUTE155 = x3d.ROUTE()
ROUTE155.fromField = "fraction_changed"
ROUTE155.fromNode = "LRearDown1"
ROUTE155.toField = "set_fraction"
ROUTE155.toNode = "LRearInterDown1"

Scene17.children.append(ROUTE155)
ROUTE156 = x3d.ROUTE()
ROUTE156.fromField = "fraction_changed"
ROUTE156.fromNode = "LRearUp1"
ROUTE156.toField = "set_fraction"
ROUTE156.toNode = "LRearInterUp1"

Scene17.children.append(ROUTE156)
ROUTE157 = x3d.ROUTE()
ROUTE157.fromField = "value_changed"
ROUTE157.fromNode = "LRearInterDown1"
ROUTE157.toField = "set_rotation"
ROUTE157.toNode = "RearLeftWheelTransform"

Scene17.children.append(ROUTE157)
ROUTE158 = x3d.ROUTE()
ROUTE158.fromField = "value_changed"
ROUTE158.fromNode = "LRearInterUp1"
ROUTE158.toField = "set_rotation"
ROUTE158.toNode = "RearLeftWheelTransform"

Scene17.children.append(ROUTE158)
Background159 = x3d.Background()
Background159.groundAngle = [1.309,1.570796]
Background159.groundColor = [0,0.3,0.7,0,0.35,0.75,0,0.4,0.8]
Background159.skyAngle = [1.309,1.571]
Background159.skyColor = [0,0.3,0.8,0,0.5,1,1,1,1]

Scene17.children.append(Background159)
Transform160 = x3d.Transform()
Transform160.DEF = "RightmostAmraamTransform"
Transform160.rotation = [-1,0,0,1.57]
Transform160.scale = [1.4,1.4,1.4]
Transform160.translation = [15.65,0,4.5]
Inline161 = x3d.Inline()
Inline161.DEF = "Amraam"
Inline161.url = ["../../Weapons/Missiles/Amraam.x3d","https://savage.nps.edu/Savage/Weapons/Missiles/Amraam.x3d","../../Weapons/Missiles/Amraam.wrl","https://savage.nps.edu/Savage/Weapons/Missiles/Amraam.wrl"]

Transform160.children.append(Inline161)

Scene17.children.append(Transform160)
Transform162 = x3d.Transform()
Transform162.DEF = "LeftmostAmraamTransform"
Transform162.rotation = [-1,0,0,1.57]
Transform162.scale = [1.4,1.4,1.4]
Transform162.translation = [-15.65,0,4.5]
Inline163 = x3d.Inline()
Inline163.USE = "Amraam"

Transform162.children.append(Inline163)

Scene17.children.append(Transform162)
Transform164 = x3d.Transform()
Transform164.DEF = "SidewinderHolderTransformRight"
Transform164.rotation = [0,1,0,1.57]
Transform164.scale = [6,3,3]
Transform164.translation = [9,-1.125,8]
Inline165 = x3d.Inline()
Inline165.DEF = "SidewinderHolder"
Inline165.url = ["SidewinderHolder.x3d","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/SidewinderHolder.x3d","SidewinderHolder.wrl","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/SidewinderHolder.wrl"]

Transform164.children.append(Inline165)

Scene17.children.append(Transform164)
Transform166 = x3d.Transform()
Transform166.DEF = "SidewinderHolderTransformLeft"
Transform166.rotation = [0,1,0,1.57]
Transform166.scale = [6,3,3]
Transform166.translation = [-8.45,-1.125,8]
Inline167 = x3d.Inline()
Inline167.USE = "SidewinderHolder"

Transform166.children.append(Inline167)

Scene17.children.append(Transform166)
Transform168 = x3d.Transform()
Transform168.DEF = "TurkishFlagTransformLeft"
Transform168.rotation = [0,-1,0,1.57]
Transform168.scale = [0.3,0.25,0.3]
Transform168.translation = [-0.01,8,19.5]
Inline169 = x3d.Inline()
Inline169.url = ["TurkishFlagLeft.x3d","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/TurkishFlagLeft.x3d","TurkishFlagLeft.wrl","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/TurkishFlagLeft.wrl"]

Transform168.children.append(Inline169)

Scene17.children.append(Transform168)
Transform170 = x3d.Transform()
Transform170.DEF = "TurkishFlagTransformRight"
Transform170.rotation = [0,1,0,1.57]
Transform170.scale = [0.3,0.25,0.3]
Transform170.translation = [0.01,8,20.5]
Inline171 = x3d.Inline()
Inline171.url = ["TurkishFlagRight.x3d","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/TurkishFlagRight.x3d","TurkishFlagRight.wrl","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/TurkishFlagRight.wrl"]

Transform170.children.append(Inline171)

Scene17.children.append(Transform170)
Transform172 = x3d.Transform()
Transform172.DEF = "AmraamHolderTransformLeft"
Transform172.translation = [-12,-0.176,10.7]
Inline173 = x3d.Inline()
Inline173.DEF = "AmraamHolder"
Inline173.url = ["AmraamHolder.x3d","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/AmraamHolder.x3d","AmraamHolder.wrl","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/AmraamHolder.wrl"]

Transform172.children.append(Inline173)

Scene17.children.append(Transform172)
Transform174 = x3d.Transform()
Transform174.DEF = "AmraamHolderTransformRight"
Transform174.translation = [12,-0.176,10.7]
Inline175 = x3d.Inline()
Inline175.USE = "AmraamHolder"

Transform174.children.append(Inline175)

Scene17.children.append(Transform174)
Transform176 = x3d.Transform()
Transform176.DEF = "AmraamInnerTransformRight"
Transform176.rotation = [-1,0,0,1.57]
Transform176.scale = [1.4,1.4,1.4]
Transform176.translation = [12,-1.6,4.5]
Inline177 = x3d.Inline()
Inline177.USE = "Amraam"

Transform176.children.append(Inline177)

Scene17.children.append(Transform176)
Transform178 = x3d.Transform()
Transform178.DEF = "AmraamInnerTransformLeft"
Transform178.rotation = [-1,0,0,1.57]
Transform178.scale = [1.4,1.4,1.4]
Transform178.translation = [-12,-1.6,4.5]
Inline179 = x3d.Inline()
Inline179.USE = "Amraam"

Transform178.children.append(Inline179)

Scene17.children.append(Transform178)
Transform180 = x3d.Transform()
Transform180.DEF = "SidewinderTransformLeft"
Transform180.rotation = [-1,0,0,1.57]
Transform180.scale = [1.6,1.6,1.6]
Transform180.translation = [-8.7,-2,3.5]
Inline181 = x3d.Inline()
Inline181.DEF = "Sidewinder"
Inline181.url = ["../../Weapons/Missiles/Sidewinder.x3d","https://savage.nps.edu/Savage/Weapons/Missiles/Sidewinder.x3d","../../Weapons/Missiles/Sidewinder.wrl","https://savage.nps.edu/Savage/Weapons/Missiles/Sidewinder.wrl"]

Transform180.children.append(Inline181)

Scene17.children.append(Transform180)
Transform182 = x3d.Transform()
Transform182.DEF = "SidewinderTransformRight"
Transform182.rotation = [-1,0,0,1.57]
Transform182.scale = [1.6,1.6,1.6]
Transform182.translation = [8.7,-2,3.5]
Inline183 = x3d.Inline()
Inline183.USE = "Sidewinder"

Transform182.children.append(Inline183)

Scene17.children.append(Transform182)
Transform184 = x3d.Transform()
Transform184.DEF = "FuelTankHolderTransformLeft"
Transform184.rotation = [0,1,0,1.57]
Transform184.scale = [1.5,1.5,1.5]
Transform184.translation = [-4.8,-1.125,6]
Inline185 = x3d.Inline()
Inline185.DEF = "FuelTankHolder"
Inline185.url = ["FuelTankHolder.x3d","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/FuelTankHolder.x3d","FuelTankHolder.wrl","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/FuelTankHolder.wrl"]

Transform184.children.append(Inline185)

Scene17.children.append(Transform184)
Transform186 = x3d.Transform()
Transform186.DEF = "FuelTankHolderTransformRight"
Transform186.rotation = [0,1,0,1.57]
Transform186.scale = [1.5,1.5,1.5]
Transform186.translation = [5.3,-1.125,6]
Inline187 = x3d.Inline()
Inline187.USE = "FuelTankHolder"

Transform186.children.append(Inline187)

Scene17.children.append(Transform186)
Transform188 = x3d.Transform()
Transform188.DEF = "FuelTankTransformRight"
Transform188.rotation = [-1,0,0,1.57]
Transform188.scale = [1.5,1.5,1.5]
Transform188.translation = [5,-2.85,5.5]
Inline189 = x3d.Inline()
Inline189.DEF = "FuelTank"
Inline189.url = ["FuelTank.x3d","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/FuelTank.x3d","FuelTank.wrl","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/FuelTank.wrl"]

Transform188.children.append(Inline189)

Scene17.children.append(Transform188)
Transform190 = x3d.Transform()
Transform190.DEF = "FuelTankTransformLeft"
Transform190.rotation = [-1,0,0,1.57]
Transform190.scale = [1.5,1.5,1.5]
Transform190.translation = [-5,-2.85,5.5]
Inline191 = x3d.Inline()
Inline191.USE = "FuelTank"

Transform190.children.append(Inline191)

Scene17.children.append(Transform190)
Transform192 = x3d.Transform()
Transform192.DEF = "InlineCoverOfPlaneTansform"
Shape193 = x3d.Shape()
Box194 = x3d.Box()
Box194.size = [4.15,0.1,20]

Shape193.geometry = Box194
Appearance195 = x3d.Appearance()
Material196 = x3d.Material()
Material196.diffuseColor = [0.25,0.25,0.25]

Appearance195.material = Material196

Shape193.appearance = Appearance195

Transform192.children.append(Shape193)

Scene17.children.append(Transform192)
Transform197 = x3d.Transform()
Transform197.DEF = "TargetHelicopterTransform"
Transform197.translation = [16,-50,-500]
Inline198 = x3d.Inline()
Inline198.url = ["Target.x3d","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/Target.x3d","Target.wrl","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/Target.wrl"]

Transform197.children.append(Inline198)

Scene17.children.append(Transform197)
TimeSensor199 = x3d.TimeSensor()
TimeSensor199.DEF = "FireClock"
TimeSensor199.cycleInterval = 8

Scene17.children.append(TimeSensor199)
PositionInterpolator200 = x3d.PositionInterpolator()
PositionInterpolator200.DEF = "MissilePath"
PositionInterpolator200.key = [0,0.1,1]
PositionInterpolator200.keyValue = (-15.6500,0.0000,4.5000,-15.6500,-2.0000,4.5000,16.0000,-50.0000,-500.0000)

Scene17.children.append(PositionInterpolator200)
ROUTE201 = x3d.ROUTE()
ROUTE201.fromField = "touchTime"
ROUTE201.fromNode = "FireSensor"
ROUTE201.toField = "set_startTime"
ROUTE201.toNode = "FireClock"

Scene17.children.append(ROUTE201)
ROUTE202 = x3d.ROUTE()
ROUTE202.fromField = "fraction_changed"
ROUTE202.fromNode = "FireClock"
ROUTE202.toField = "set_fraction"
ROUTE202.toNode = "MissilePath"

Scene17.children.append(ROUTE202)
ROUTE203 = x3d.ROUTE()
ROUTE203.fromField = "value_changed"
ROUTE203.fromNode = "MissilePath"
ROUTE203.toField = "set_translation"
ROUTE203.toNode = "LeftmostAmraamTransform"

Scene17.children.append(ROUTE203)
Viewpoint204 = x3d.Viewpoint()
Viewpoint204.DEF = "MissileLaunchView"
Viewpoint204.description = "Missile Fire View"
Viewpoint204.orientation = [0.094,-0.994,0.057,1.1716]
Viewpoint204.position = [-344.3,-142.8,-27.7]

Scene17.children.append(Viewpoint204)
ROUTE205 = x3d.ROUTE()
ROUTE205.fromField = "isActive"
ROUTE205.fromNode = "FireSensor"
ROUTE205.toField = "set_bind"
ROUTE205.toNode = "MissileLaunchView"

Scene17.children.append(ROUTE205)
#TODO fix type, add filter

X3D0.Scene = Scene17
f = open("././F16_RoundTrip.x3d", "w")
f.write(X3D0.XML())
f.close()
