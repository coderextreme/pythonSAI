print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"
head1 = x3d.head()
component2 = x3d.component()
component2.name = "H-Anim"
component2.level = 1

head1.children.append(component2)
meta3 = x3d.meta()
meta3.name = "title"
meta3.content = "DiamondManLOA_2.x3d"

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.name = "description"
meta4.content = "hanim skeletal structure at level of articulation two, one diamond at the base node for the structure"

head1.children.append(meta4)
meta5 = x3d.meta()
meta5.name = "creator"
meta5.content = "Matthew T. Beitler"

head1.children.append(meta5)
meta6 = x3d.meta()
meta6.name = "translator"
meta6.content = "Joel S. Pawloski"

head1.children.append(meta6)
meta7 = x3d.meta()
meta7.name = "created"
meta7.content = "12 November 2001"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.name = "modified"
meta8.content = "22 February 2022"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "Image"
meta9.content = "DiamondManLOA_2.png"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "Image"
meta10.content = "images/BonesAllSkeletonFrontViewLOA2.png"

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.name = "motto"
meta11.content = "(a) \"Diamonds are a girl's best friend.\" (b) \"Gosh, it sure is chilly in here.\""

head1.children.append(meta11)
meta12 = x3d.meta()
meta12.name = "reference"
meta12.content = "The joint centers of this figure are based on the work of Norman Badler, director of the Center for Human Modeling and Simulation at the University of Pennsylvania. The original document which these joint centers are based on can be found at: http://www.cis.upenn.edu/~badler/anthro/89-71.ps"

head1.children.append(meta12)
meta13 = x3d.meta()
meta13.name = "subject"
meta13.content = "human animation, x3d, vrml, animation"

head1.children.append(meta13)
meta14 = x3d.meta()
meta14.name = "identifier"
meta14.content = "https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Templates/DiamondManLOA_2.x3d"

head1.children.append(meta14)
meta15 = x3d.meta()
meta15.name = "generator"
meta15.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"

head1.children.append(meta15)
meta16 = x3d.meta()
meta16.name = "license"
meta16.content = "../license.html"

head1.children.append(meta16)

X3D0.head = head1
Scene17 = x3d.Scene()
WorldInfo18 = x3d.WorldInfo()
WorldInfo18.info = ["HAnim 2.0 Default Joint Centers, Level Of Articulation (LOA) 2 -------------------------------------------------------- HANIM 1.1 (VRML 2.0) Author name: eMpTy (a.k.a. Matthew T. Beitler) HANIM 1.1 (VRML 2.0) Author email: beitler@graphics.cis.upenn.edu or beitler@acm.org HANIM 1.1 (VRML 2.0) Author homepage: http://www.cis.upenn.edu/~beitler HANIM 1.1 (VRML 2.0) Compliance Date: May 12, 1999 HANIM 1.1 Compliance Information: http://ece.uwaterloo.ca/~HAnim/ Construction Info (joint centers): The joint centers of this figure are based on the work of Norman Badler, director of the Center for Human Modeling and Simulation at the University of Pennsylvania. The original document which these joint centers are based on can be found at: http://www.cis.upenn.edu/~badler/anthro/89-71.ps, .pdf"]
WorldInfo18.title = "HANIM 1.1 Default Joint Centers, LOA1"

Scene17.children.append(WorldInfo18)
NavigationInfo19 = x3d.NavigationInfo()
NavigationInfo19.speed = 1.5

Scene17.children.append(NavigationInfo19)
Viewpoint20 = x3d.Viewpoint()
Viewpoint20.centerOfRotation = [0,1,0]
Viewpoint20.description = "Diamond Man, LOA 2"
Viewpoint20.position = [0,1,3]

Scene17.children.append(Viewpoint20)
Transform21 = x3d.Transform()
Transform21.translation = [1,1.5,0]
Billboard22 = x3d.Billboard()
Shape23 = x3d.Shape()
Text24 = x3d.Text()
Text24.string = ["Diamond Man Key"]
FontStyle25 = x3d.FontStyle()
FontStyle25.family = ["SANS"]
FontStyle25.size = 0.1

Text24.fontStyle = FontStyle25

Shape23.geometry = Text24
Appearance26 = x3d.Appearance()
Material27 = x3d.Material()
Material27.DEF = "TextMaterial"
Material27.diffuseColor = [0.9,0.9,0.9]

Appearance26.material = Material27

Shape23.appearance = Appearance26

Billboard22.children.append(Shape23)
Transform28 = x3d.Transform()
Transform28.translation = [0,-0.3,0]
Shape29 = x3d.Shape()
Sphere30 = x3d.Sphere()
Sphere30.radius = 0.08

Shape29.geometry = Sphere30
Appearance31 = x3d.Appearance()
Material32 = x3d.Material()
Material32.DEF = "MIN_COLOR"
Material32.diffuseColor = [1,0,0]

Appearance31.material = Material32

Shape29.appearance = Appearance31

Transform28.children.append(Shape29)
Transform33 = x3d.Transform()
Transform33.translation = [0.2,0,0]
Shape34 = x3d.Shape()
Text35 = x3d.Text()
Text35.string = ["Minimal Humanoid Joints"]
FontStyle36 = x3d.FontStyle()
FontStyle36.family = ["SANS"]
FontStyle36.size = 0.1

Text35.fontStyle = FontStyle36

Shape34.geometry = Text35
Appearance37 = x3d.Appearance()
Material38 = x3d.Material()
Material38.USE = "TextMaterial"

Appearance37.material = Material38

Shape34.appearance = Appearance37

Transform33.children.append(Shape34)

Transform28.children.append(Transform33)

Billboard22.children.append(Transform28)
Transform39 = x3d.Transform()
Transform39.translation = [0,-0.5,0]
Shape40 = x3d.Shape()
Sphere41 = x3d.Sphere()
Sphere41.radius = 0.08

Shape40.geometry = Sphere41
Appearance42 = x3d.Appearance()
Material43 = x3d.Material()
Material43.DEF = "JOINT_COLOR"
Material43.diffuseColor = [1,1,0]

Appearance42.material = Material43

Shape40.appearance = Appearance42

Transform39.children.append(Shape40)
Transform44 = x3d.Transform()
Transform44.translation = [0.2,0,0]
Shape45 = x3d.Shape()
Text46 = x3d.Text()
Text46.string = ["Humanoid Joints"]
FontStyle47 = x3d.FontStyle()
FontStyle47.family = ["SANS"]
FontStyle47.size = 0.1

Text46.fontStyle = FontStyle47

Shape45.geometry = Text46
Appearance48 = x3d.Appearance()
Material49 = x3d.Material()
Material49.USE = "TextMaterial"

Appearance48.material = Material49

Shape45.appearance = Appearance48

Transform44.children.append(Shape45)

Transform39.children.append(Transform44)

Billboard22.children.append(Transform39)
Transform50 = x3d.Transform()
Transform50.translation = [0,-0.7,0]
Shape51 = x3d.Shape()
Sphere52 = x3d.Sphere()
Sphere52.radius = 0.08

Shape51.geometry = Sphere52
Appearance53 = x3d.Appearance()
Material54 = x3d.Material()
Material54.DEF = "REC_SPINAL_COLOR"
Material54.diffuseColor = [1,0,1]

Appearance53.material = Material54

Shape51.appearance = Appearance53

Transform50.children.append(Shape51)
Transform55 = x3d.Transform()
Transform55.translation = [0.2,0,0]
Shape56 = x3d.Shape()
Text57 = x3d.Text()
Text57.string = ["Recommended Spinal Joints"]
FontStyle58 = x3d.FontStyle()
FontStyle58.family = ["SANS"]
FontStyle58.size = 0.1

Text57.fontStyle = FontStyle58

Shape56.geometry = Text57
Appearance59 = x3d.Appearance()
Material60 = x3d.Material()
Material60.USE = "TextMaterial"

Appearance59.material = Material60

Shape56.appearance = Appearance59

Transform55.children.append(Shape56)

Transform50.children.append(Transform55)

Billboard22.children.append(Transform50)
Transform61 = x3d.Transform()
Transform61.translation = [0,-0.9,0]
Shape62 = x3d.Shape()
Sphere63 = x3d.Sphere()
Sphere63.radius = 0.08

Shape62.geometry = Sphere63
Appearance64 = x3d.Appearance()
Material65 = x3d.Material()
Material65.DEF = "SPINAL_COLOR"
Material65.diffuseColor = [0,1,0]

Appearance64.material = Material65

Shape62.appearance = Appearance64

Transform61.children.append(Shape62)
Transform66 = x3d.Transform()
Transform66.translation = [0.2,0,0]
Shape67 = x3d.Shape()
Text68 = x3d.Text()
Text68.string = ["Spinal Joints"]
FontStyle69 = x3d.FontStyle()
FontStyle69.family = ["SANS"]
FontStyle69.size = 0.1

Text68.fontStyle = FontStyle69

Shape67.geometry = Text68
Appearance70 = x3d.Appearance()
Material71 = x3d.Material()
Material71.USE = "TextMaterial"

Appearance70.material = Material71

Shape67.appearance = Appearance70

Transform66.children.append(Shape67)

Transform61.children.append(Transform66)

Billboard22.children.append(Transform61)
Transform72 = x3d.Transform()
Transform72.translation = [0,-1.3,0]
Shape73 = x3d.Shape()
Sphere74 = x3d.Sphere()
Sphere74.radius = 0.08

Shape73.geometry = Sphere74
Appearance75 = x3d.Appearance()
Material76 = x3d.Material()
Material76.DEF = "SITE_COLOR"
Material76.diffuseColor = [0,0,1]

Appearance75.material = Material76

Shape73.appearance = Appearance75

Transform72.children.append(Shape73)
Transform77 = x3d.Transform()
Transform77.translation = [0.2,0,0]
Shape78 = x3d.Shape()
Text79 = x3d.Text()
Text79.string = ["Humanoid Sites"]
FontStyle80 = x3d.FontStyle()
FontStyle80.family = ["SANS"]
FontStyle80.size = 0.1

Text79.fontStyle = FontStyle80

Shape78.geometry = Text79
Appearance81 = x3d.Appearance()
Material82 = x3d.Material()
Material82.USE = "TextMaterial"

Appearance81.material = Material82

Shape78.appearance = Appearance81

Transform77.children.append(Shape78)

Transform72.children.append(Transform77)

Billboard22.children.append(Transform72)
Transform83 = x3d.Transform()
Transform83.translation = [0,-1.1,0]
Shape84 = x3d.Shape()
Sphere85 = x3d.Sphere()
Sphere85.radius = 0.08

Shape84.geometry = Sphere85
Appearance86 = x3d.Appearance()
Material87 = x3d.Material()
Material87.DEF = "HAND_FEET_COLOR"
Material87.diffuseColor = [0,1,1]

Appearance86.material = Material87

Shape84.appearance = Appearance86

Transform83.children.append(Shape84)
Transform88 = x3d.Transform()
Transform88.translation = [0.2,0,0]
Shape89 = x3d.Shape()
Text90 = x3d.Text()
Text90.string = ["Hand & Feet Joints"]
FontStyle91 = x3d.FontStyle()
FontStyle91.family = ["SANS"]
FontStyle91.size = 0.1

Text90.fontStyle = FontStyle91

Shape89.geometry = Text90
Appearance92 = x3d.Appearance()
Material93 = x3d.Material()
Material93.USE = "TextMaterial"

Appearance92.material = Material93

Shape89.appearance = Appearance92

Transform88.children.append(Shape89)

Transform83.children.append(Transform88)

Billboard22.children.append(Transform83)

Transform21.children.append(Billboard22)

Scene17.children.append(Transform21)
HAnimHumanoid94 = x3d.HAnimHumanoid()
HAnimHumanoid94.name = "humanoid"
HAnimHumanoid94.DEF = "hanim_humanoid"
HAnimHumanoid94.version = "1.0"
#original HAnimHumanoid info='\"humanoidVersion=Nancy V1.2b\" \"authorName=Cindy Ballreich\" \"authorEmail=cindy@ballreich.net\" \"copyright=1997 3Name3D / Yglesias Wallock Divekar Inc. all rights reserved.\" \"creationDate=Tue Dec 30 08:30:08 PST 1997\" \"usageRestrictions=Noncommercial usage is ok if 3Name3D name and logo <www.ballreich.net/vrml/HAnim/small_logo.gif> is present and proper credit is given.\"'
MetadataSet95 = x3d.MetadataSet()
MetadataSet95.name = "HAnimHumanoid.info"
MetadataSet95.reference = "https://www.web3d.org/documents/specifications/19774/V2.0/Architecture/ObjectInterfaces.html#Humanoid"
MetadataString96 = x3d.MetadataString()
MetadataString96.name = "humanoidVersion"
MetadataString96.value = ["Nancy V1.2b"]

MetadataSet95.value.append(MetadataString96)
MetadataString97 = x3d.MetadataString()
MetadataString97.name = "authorEmail"
MetadataString97.value = ["cindy@ballreich.net"]

MetadataSet95.value.append(MetadataString97)
MetadataString98 = x3d.MetadataString()
MetadataString98.name = "authorName"
MetadataString98.value = ["Cindy Ballreich"]

MetadataSet95.value.append(MetadataString98)
MetadataString99 = x3d.MetadataString()
MetadataString99.name = "copyright"
MetadataString99.value = ["1997 3Name3D / Yglesias Wallock Divekar Inc. all rights reserved."]

MetadataSet95.value.append(MetadataString99)
MetadataString100 = x3d.MetadataString()
MetadataString100.name = "creationDate"
MetadataString100.value = ["Tue Dec 30 08:30:08 PST 1997"]

MetadataSet95.value.append(MetadataString100)
MetadataString101 = x3d.MetadataString()
MetadataString101.name = "usageRestrictions"
MetadataString101.value = ["Noncommercial usage is ok if 3Name3D name and logo www.ballreich.net/vrml/HAnim/small_logo.gif is present and proper credit is given."]

MetadataSet95.value.append(MetadataString101)

HAnimHumanoid94.metadata.append(MetadataSet95)
HAnimJoint102 = x3d.HAnimJoint()
HAnimJoint102.name = "HumanoidRoot"
HAnimJoint102.DEF = "hanim_HumanoidRoot"
HAnimJoint102.center = [0,0.824,0.0277]
HAnimJoint102.ulimit = [0,0,0]
HAnimJoint102.llimit = [0,0,0]
HAnimSegment103 = x3d.HAnimSegment()
HAnimSegment103.name = "sacrum"
HAnimSegment103.DEF = "hanim_sacrum"
Transform104 = x3d.Transform()
Transform104.translation = [0,0.824,0.0277]
Shape105 = x3d.Shape()
Shape105.DEF = "DiamondShape"
IndexedFaceSet106 = x3d.IndexedFaceSet()
IndexedFaceSet106.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet106.creaseAngle = 0.5
Coordinate107 = x3d.Coordinate()
Coordinate107.DEF = "points"
Coordinate107.point = (0.0000,0.0100,0.0000,-0.0100,0.0000,0.0000,0.0000,0.0000,0.0100,0.0100,0.0000,0.0000,0.0000,0.0000,-0.0100,0.0000,-0.0100,0.0000)

IndexedFaceSet106.coord.append(Coordinate107)

Shape105.geometry = IndexedFaceSet106
Appearance108 = x3d.Appearance()
Material109 = x3d.Material()
Material109.DEF = "ROOT_COLOR"
Material109.diffuseColor = [1,1,1]

Appearance108.material = Material109

Shape105.appearance = Appearance108

Transform104.children.append(Shape105)
Transform110 = x3d.Transform()
Transform110.translation = [0,0.01,0]
Billboard111 = x3d.Billboard()
Shape112 = x3d.Shape()
Text113 = x3d.Text()
Text113.string = ["Humanoid Root"]
FontStyle114 = x3d.FontStyle()
FontStyle114.family = ["SANS"]
FontStyle114.size = 0.01
FontStyle114.style = "ITALIC"

Text113.fontStyle = FontStyle114

Shape112.geometry = Text113
Appearance115 = x3d.Appearance()
Material116 = x3d.Material()
Material116.diffuseColor = [0.039216,1,0.568627]

Appearance115.material = Material116

Shape112.appearance = Appearance115

Billboard111.children.append(Shape112)

Transform110.children.append(Billboard111)

Transform104.children.append(Transform110)

HAnimSegment103.children.append(Transform104)

HAnimJoint102.children.append(HAnimSegment103)
HAnimJoint117 = x3d.HAnimJoint()
HAnimJoint117.name = "sacroiliac"
HAnimJoint117.DEF = "hanim_sacroiliac"
HAnimJoint117.center = [0,0.9149,0.0016]
HAnimJoint117.ulimit = [0,0,0]
HAnimJoint117.llimit = [0,0,0]
HAnimSegment118 = x3d.HAnimSegment()
HAnimSegment118.name = "pelvis"
HAnimSegment118.DEF = "hanim_pelvis"
Transform119 = x3d.Transform()
Transform119.DEF = "sacroiliacPos"
Transform119.translation = [0,0.9149,0.0016]
Shape120 = x3d.Shape()
IndexedFaceSet121 = x3d.IndexedFaceSet()
IndexedFaceSet121.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet121.creaseAngle = 0.5
Coordinate122 = x3d.Coordinate()
Coordinate122.USE = "points"

IndexedFaceSet121.coord.append(Coordinate122)

Shape120.geometry = IndexedFaceSet121
Appearance123 = x3d.Appearance()
Material124 = x3d.Material()
Material124.USE = "MIN_COLOR"

Appearance123.material = Material124

Shape120.appearance = Appearance123

Transform119.children.append(Shape120)

HAnimSegment118.children.append(Transform119)
HAnimSite125 = x3d.HAnimSite()
HAnimSite125.name = "r_iliocristale_pt"
HAnimSite125.DEF = "hanim_r_iliocristale_pt"
HAnimSite125.translation = [-0.1525,1.0628,0.0035]
Shape126 = x3d.Shape()
IndexedFaceSet127 = x3d.IndexedFaceSet()
IndexedFaceSet127.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet127.creaseAngle = 0.5
Coordinate128 = x3d.Coordinate()
Coordinate128.USE = "points"

IndexedFaceSet127.coord.append(Coordinate128)

Shape126.geometry = IndexedFaceSet127
Appearance129 = x3d.Appearance()
Material130 = x3d.Material()
Material130.USE = "SITE_COLOR"

Appearance129.material = Material130

Shape126.appearance = Appearance129

HAnimSite125.children.append(Shape126)

HAnimSegment118.children.append(HAnimSite125)
HAnimSite131 = x3d.HAnimSite()
HAnimSite131.name = "r_trochanterion_pt"
HAnimSite131.DEF = "hanim_r_trochanterion_pt"
HAnimSite131.translation = [-0.1689,0.8419,0.0352]
Shape132 = x3d.Shape()
IndexedFaceSet133 = x3d.IndexedFaceSet()
IndexedFaceSet133.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet133.creaseAngle = 0.5
Coordinate134 = x3d.Coordinate()
Coordinate134.USE = "points"

IndexedFaceSet133.coord.append(Coordinate134)

Shape132.geometry = IndexedFaceSet133
Appearance135 = x3d.Appearance()
Material136 = x3d.Material()
Material136.USE = "SITE_COLOR"

Appearance135.material = Material136

Shape132.appearance = Appearance135

HAnimSite131.children.append(Shape132)

HAnimSegment118.children.append(HAnimSite131)
HAnimSite137 = x3d.HAnimSite()
HAnimSite137.name = "l_iliocristale_pt"
HAnimSite137.DEF = "hanim_l_iliocristale_pt"
HAnimSite137.translation = [0.1612,1.0537,0.0008]
Shape138 = x3d.Shape()
IndexedFaceSet139 = x3d.IndexedFaceSet()
IndexedFaceSet139.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet139.creaseAngle = 0.5
Coordinate140 = x3d.Coordinate()
Coordinate140.USE = "points"

IndexedFaceSet139.coord.append(Coordinate140)

Shape138.geometry = IndexedFaceSet139
Appearance141 = x3d.Appearance()
Material142 = x3d.Material()
Material142.USE = "SITE_COLOR"

Appearance141.material = Material142

Shape138.appearance = Appearance141

HAnimSite137.children.append(Shape138)

HAnimSegment118.children.append(HAnimSite137)
HAnimSite143 = x3d.HAnimSite()
HAnimSite143.name = "l_trochanterion_pt"
HAnimSite143.DEF = "hanim_l_trochanterion_pt"
HAnimSite143.translation = [0.1677,0.8336,0.0303]
Shape144 = x3d.Shape()
IndexedFaceSet145 = x3d.IndexedFaceSet()
IndexedFaceSet145.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet145.creaseAngle = 0.5
Coordinate146 = x3d.Coordinate()
Coordinate146.USE = "points"

IndexedFaceSet145.coord.append(Coordinate146)

Shape144.geometry = IndexedFaceSet145
Appearance147 = x3d.Appearance()
Material148 = x3d.Material()
Material148.USE = "SITE_COLOR"

Appearance147.material = Material148

Shape144.appearance = Appearance147

HAnimSite143.children.append(Shape144)

HAnimSegment118.children.append(HAnimSite143)
HAnimSite149 = x3d.HAnimSite()
HAnimSite149.name = "r_asis_pt"
HAnimSite149.DEF = "hanim_r_asis_pt"
HAnimSite149.translation = [-0.0887,1.0021,0.1112]
Shape150 = x3d.Shape()
IndexedFaceSet151 = x3d.IndexedFaceSet()
IndexedFaceSet151.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet151.creaseAngle = 0.5
Coordinate152 = x3d.Coordinate()
Coordinate152.USE = "points"

IndexedFaceSet151.coord.append(Coordinate152)

Shape150.geometry = IndexedFaceSet151
Appearance153 = x3d.Appearance()
Material154 = x3d.Material()
Material154.USE = "SITE_COLOR"

Appearance153.material = Material154

Shape150.appearance = Appearance153

HAnimSite149.children.append(Shape150)

HAnimSegment118.children.append(HAnimSite149)
HAnimSite155 = x3d.HAnimSite()
HAnimSite155.name = "l_asis_pt"
HAnimSite155.DEF = "hanim_l_asis_pt"
HAnimSite155.translation = [0.0925,0.9983,0.1052]
Shape156 = x3d.Shape()
IndexedFaceSet157 = x3d.IndexedFaceSet()
IndexedFaceSet157.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet157.creaseAngle = 0.5
Coordinate158 = x3d.Coordinate()
Coordinate158.USE = "points"

IndexedFaceSet157.coord.append(Coordinate158)

Shape156.geometry = IndexedFaceSet157
Appearance159 = x3d.Appearance()
Material160 = x3d.Material()
Material160.USE = "SITE_COLOR"

Appearance159.material = Material160

Shape156.appearance = Appearance159

HAnimSite155.children.append(Shape156)

HAnimSegment118.children.append(HAnimSite155)
HAnimSite161 = x3d.HAnimSite()
HAnimSite161.name = "r_psis_pt"
HAnimSite161.DEF = "hanim_r_psis_pt"
HAnimSite161.translation = [-0.0716,1.019,-0.1138]
Shape162 = x3d.Shape()
IndexedFaceSet163 = x3d.IndexedFaceSet()
IndexedFaceSet163.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet163.creaseAngle = 0.5
Coordinate164 = x3d.Coordinate()
Coordinate164.USE = "points"

IndexedFaceSet163.coord.append(Coordinate164)

Shape162.geometry = IndexedFaceSet163
Appearance165 = x3d.Appearance()
Material166 = x3d.Material()
Material166.USE = "SITE_COLOR"

Appearance165.material = Material166

Shape162.appearance = Appearance165

HAnimSite161.children.append(Shape162)

HAnimSegment118.children.append(HAnimSite161)
HAnimSite167 = x3d.HAnimSite()
HAnimSite167.name = "l_psis_pt"
HAnimSite167.DEF = "hanim_l_psis_pt"
HAnimSite167.translation = [0.0774,1.019,-0.1151]
Shape168 = x3d.Shape()
IndexedFaceSet169 = x3d.IndexedFaceSet()
IndexedFaceSet169.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet169.creaseAngle = 0.5
Coordinate170 = x3d.Coordinate()
Coordinate170.USE = "points"

IndexedFaceSet169.coord.append(Coordinate170)

Shape168.geometry = IndexedFaceSet169
Appearance171 = x3d.Appearance()
Material172 = x3d.Material()
Material172.USE = "SITE_COLOR"

Appearance171.material = Material172

Shape168.appearance = Appearance171

HAnimSite167.children.append(Shape168)

HAnimSegment118.children.append(HAnimSite167)
HAnimSite173 = x3d.HAnimSite()
HAnimSite173.name = "crotch_pt"
HAnimSite173.DEF = "hanim_crotch_pt"
HAnimSite173.translation = [0.0034,0.8266,0.0257]
Shape174 = x3d.Shape()
IndexedFaceSet175 = x3d.IndexedFaceSet()
IndexedFaceSet175.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet175.creaseAngle = 0.5
Coordinate176 = x3d.Coordinate()
Coordinate176.USE = "points"

IndexedFaceSet175.coord.append(Coordinate176)

Shape174.geometry = IndexedFaceSet175
Appearance177 = x3d.Appearance()
Material178 = x3d.Material()
Material178.USE = "SITE_COLOR"

Appearance177.material = Material178

Shape174.appearance = Appearance177

HAnimSite173.children.append(Shape174)

HAnimSegment118.children.append(HAnimSite173)

HAnimJoint117.children.append(HAnimSegment118)
HAnimJoint179 = x3d.HAnimJoint()
HAnimJoint179.name = "l_hip"
HAnimJoint179.DEF = "hanim_l_hip"
HAnimJoint179.center = [0.0961,0.9124,-0.0001]
HAnimJoint179.ulimit = [0,0,0]
HAnimJoint179.llimit = [0,0,0]
HAnimSegment180 = x3d.HAnimSegment()
HAnimSegment180.name = "l_thigh"
HAnimSegment180.DEF = "hanim_l_thigh"
Transform181 = x3d.Transform()
Transform181.translation = [0.0961,0.9124,-0.0001]
Shape182 = x3d.Shape()
IndexedFaceSet183 = x3d.IndexedFaceSet()
IndexedFaceSet183.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet183.creaseAngle = 0.5
Coordinate184 = x3d.Coordinate()
Coordinate184.USE = "points"

IndexedFaceSet183.coord.append(Coordinate184)

Shape182.geometry = IndexedFaceSet183
Appearance185 = x3d.Appearance()
Material186 = x3d.Material()
Material186.USE = "MIN_COLOR"

Appearance185.material = Material186

Shape182.appearance = Appearance185

Transform181.children.append(Shape182)

HAnimSegment180.children.append(Transform181)
HAnimSite187 = x3d.HAnimSite()
HAnimSite187.name = "l_knee_crease_pt"
HAnimSite187.DEF = "hanim_l_knee_crease_pt"
HAnimSite187.translation = [0.0993,0.4881,-0.0309]
Shape188 = x3d.Shape()
IndexedFaceSet189 = x3d.IndexedFaceSet()
IndexedFaceSet189.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet189.creaseAngle = 0.5
Coordinate190 = x3d.Coordinate()
Coordinate190.USE = "points"

IndexedFaceSet189.coord.append(Coordinate190)

Shape188.geometry = IndexedFaceSet189
Appearance191 = x3d.Appearance()
Material192 = x3d.Material()
Material192.USE = "SITE_COLOR"

Appearance191.material = Material192

Shape188.appearance = Appearance191

HAnimSite187.children.append(Shape188)

HAnimSegment180.children.append(HAnimSite187)
HAnimSite193 = x3d.HAnimSite()
HAnimSite193.name = "l_femoral_lateral_epicn_pt"
HAnimSite193.DEF = "hanim_l_femoral_lateral_epicn_pt"
HAnimSite193.translation = [0.1598,0.4967,0.0297]
Shape194 = x3d.Shape()
IndexedFaceSet195 = x3d.IndexedFaceSet()
IndexedFaceSet195.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet195.creaseAngle = 0.5
Coordinate196 = x3d.Coordinate()
Coordinate196.USE = "points"

IndexedFaceSet195.coord.append(Coordinate196)

Shape194.geometry = IndexedFaceSet195
Appearance197 = x3d.Appearance()
Material198 = x3d.Material()
Material198.USE = "SITE_COLOR"

Appearance197.material = Material198

Shape194.appearance = Appearance197

HAnimSite193.children.append(Shape194)

HAnimSegment180.children.append(HAnimSite193)
HAnimSite199 = x3d.HAnimSite()
HAnimSite199.name = "l_femoral_medial_epicn_pt"
HAnimSite199.DEF = "hanim_l_femoral_medial_epicn_pt"
HAnimSite199.translation = [0.0398,0.4946,0.0303]
Shape200 = x3d.Shape()
IndexedFaceSet201 = x3d.IndexedFaceSet()
IndexedFaceSet201.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet201.creaseAngle = 0.5
Coordinate202 = x3d.Coordinate()
Coordinate202.USE = "points"

IndexedFaceSet201.coord.append(Coordinate202)

Shape200.geometry = IndexedFaceSet201
Appearance203 = x3d.Appearance()
Material204 = x3d.Material()
Material204.USE = "SITE_COLOR"

Appearance203.material = Material204

Shape200.appearance = Appearance203

HAnimSite199.children.append(Shape200)

HAnimSegment180.children.append(HAnimSite199)

HAnimJoint179.children.append(HAnimSegment180)
HAnimJoint205 = x3d.HAnimJoint()
HAnimJoint205.name = "l_knee"
HAnimJoint205.DEF = "hanim_l_knee"
HAnimJoint205.center = [0.104,0.4867,0.0308]
HAnimJoint205.ulimit = [0,0,0]
HAnimJoint205.llimit = [0,0,0]
HAnimSegment206 = x3d.HAnimSegment()
HAnimSegment206.name = "l_calf"
HAnimSegment206.DEF = "hanim_l_calf"
Transform207 = x3d.Transform()
Transform207.translation = [0.104,0.4867,0.0308]
Shape208 = x3d.Shape()
IndexedFaceSet209 = x3d.IndexedFaceSet()
IndexedFaceSet209.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet209.creaseAngle = 0.5
Coordinate210 = x3d.Coordinate()
Coordinate210.USE = "points"

IndexedFaceSet209.coord.append(Coordinate210)

Shape208.geometry = IndexedFaceSet209
Appearance211 = x3d.Appearance()
Material212 = x3d.Material()
Material212.USE = "MIN_COLOR"

Appearance211.material = Material212

Shape208.appearance = Appearance211

Transform207.children.append(Shape208)

HAnimSegment206.children.append(Transform207)

HAnimJoint205.children.append(HAnimSegment206)
HAnimJoint213 = x3d.HAnimJoint()
HAnimJoint213.name = "l_ankle"
HAnimJoint213.DEF = "hanim_l_ankle"
HAnimJoint213.center = [0.1101,0.0656,-0.0736]
HAnimJoint213.ulimit = [0,0,0]
HAnimJoint213.llimit = [0,0,0]
HAnimSegment214 = x3d.HAnimSegment()
HAnimSegment214.name = "l_hindfoot"
HAnimSegment214.DEF = "hanim_l_hindfoot"
Transform215 = x3d.Transform()
Transform215.translation = [0.1101,0.0656,-0.0736]
Shape216 = x3d.Shape()
IndexedFaceSet217 = x3d.IndexedFaceSet()
IndexedFaceSet217.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet217.creaseAngle = 0.5
Coordinate218 = x3d.Coordinate()
Coordinate218.USE = "points"

IndexedFaceSet217.coord.append(Coordinate218)

Shape216.geometry = IndexedFaceSet217
Appearance219 = x3d.Appearance()
Material220 = x3d.Material()
Material220.USE = "MIN_COLOR"

Appearance219.material = Material220

Shape216.appearance = Appearance219

Transform215.children.append(Shape216)

HAnimSegment214.children.append(Transform215)
HAnimSite221 = x3d.HAnimSite()
HAnimSite221.name = "l_lateral_malleolus_pt"
HAnimSite221.DEF = "hanim_l_lateral_malleolus_pt"
HAnimSite221.translation = [0.1308,0.0597,-0.1032]
Shape222 = x3d.Shape()
IndexedFaceSet223 = x3d.IndexedFaceSet()
IndexedFaceSet223.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet223.creaseAngle = 0.5
Coordinate224 = x3d.Coordinate()
Coordinate224.USE = "points"

IndexedFaceSet223.coord.append(Coordinate224)

Shape222.geometry = IndexedFaceSet223
Appearance225 = x3d.Appearance()
Material226 = x3d.Material()
Material226.USE = "HAND_FEET_COLOR"

Appearance225.material = Material226

Shape222.appearance = Appearance225

HAnimSite221.children.append(Shape222)

HAnimSegment214.children.append(HAnimSite221)
HAnimSite227 = x3d.HAnimSite()
HAnimSite227.name = "l_medial_malleolus_pt"
HAnimSite227.DEF = "hanim_l_medial_malleolus_pt"
HAnimSite227.translation = [0.089,0.0716,-0.0881]
Shape228 = x3d.Shape()
IndexedFaceSet229 = x3d.IndexedFaceSet()
IndexedFaceSet229.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet229.creaseAngle = 0.5
Coordinate230 = x3d.Coordinate()
Coordinate230.USE = "points"

IndexedFaceSet229.coord.append(Coordinate230)

Shape228.geometry = IndexedFaceSet229
Appearance231 = x3d.Appearance()
Material232 = x3d.Material()
Material232.USE = "HAND_FEET_COLOR"

Appearance231.material = Material232

Shape228.appearance = Appearance231

HAnimSite227.children.append(Shape228)

HAnimSegment214.children.append(HAnimSite227)
HAnimSite233 = x3d.HAnimSite()
HAnimSite233.name = "l_sphyrion_pt"
HAnimSite233.DEF = "hanim_l_sphyrion_pt"
HAnimSite233.translation = [0.089,0.0575,-0.0943]
Shape234 = x3d.Shape()
IndexedFaceSet235 = x3d.IndexedFaceSet()
IndexedFaceSet235.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet235.creaseAngle = 0.5
Coordinate236 = x3d.Coordinate()
Coordinate236.USE = "points"

IndexedFaceSet235.coord.append(Coordinate236)

Shape234.geometry = IndexedFaceSet235
Appearance237 = x3d.Appearance()
Material238 = x3d.Material()
Material238.USE = "HAND_FEET_COLOR"

Appearance237.material = Material238

Shape234.appearance = Appearance237

HAnimSite233.children.append(Shape234)

HAnimSegment214.children.append(HAnimSite233)
HAnimSite239 = x3d.HAnimSite()
HAnimSite239.name = "l_calcaneous_post_pt"
HAnimSite239.DEF = "hanim_l_calcaneous_post_pt"
HAnimSite239.translation = [0.0974,0.0259,-0.1171]
Shape240 = x3d.Shape()
IndexedFaceSet241 = x3d.IndexedFaceSet()
IndexedFaceSet241.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet241.creaseAngle = 0.5
Coordinate242 = x3d.Coordinate()
Coordinate242.USE = "points"

IndexedFaceSet241.coord.append(Coordinate242)

Shape240.geometry = IndexedFaceSet241
Appearance243 = x3d.Appearance()
Material244 = x3d.Material()
Material244.USE = "HAND_FEET_COLOR"

Appearance243.material = Material244

Shape240.appearance = Appearance243

HAnimSite239.children.append(Shape240)

HAnimSegment214.children.append(HAnimSite239)

HAnimJoint213.children.append(HAnimSegment214)
HAnimJoint245 = x3d.HAnimJoint()
HAnimJoint245.name = "l_subtalar"
HAnimJoint245.DEF = "hanim_l_subtalar"
HAnimJoint245.center = [0.1086,0.0001,-0.0368]
HAnimJoint245.ulimit = [0,0,0]
HAnimJoint245.llimit = [0,0,0]
HAnimSegment246 = x3d.HAnimSegment()
HAnimSegment246.name = "midproximal"
HAnimSegment246.DEF = "hanim_midproximal"
Transform247 = x3d.Transform()
Transform247.translation = [0.1086,0.0001,-0.0368]
Shape248 = x3d.Shape()
IndexedFaceSet249 = x3d.IndexedFaceSet()
IndexedFaceSet249.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet249.creaseAngle = 0.5
Coordinate250 = x3d.Coordinate()
Coordinate250.USE = "points"

IndexedFaceSet249.coord.append(Coordinate250)

Shape248.geometry = IndexedFaceSet249
Appearance251 = x3d.Appearance()
Material252 = x3d.Material()
Material252.USE = "MIN_COLOR"

Appearance251.material = Material252

Shape248.appearance = Appearance251

Transform247.children.append(Shape248)

HAnimSegment246.children.append(Transform247)

HAnimJoint245.children.append(HAnimSegment246)
HAnimJoint253 = x3d.HAnimJoint()
HAnimJoint253.name = "l_midtarsal"
HAnimJoint253.DEF = "hanim_l_midtarsal"
HAnimJoint253.center = [0.1086,0.0001,0.0368]
HAnimJoint253.ulimit = [0,0,0]
HAnimJoint253.llimit = [0,0,0]
HAnimSegment254 = x3d.HAnimSegment()
HAnimSegment254.name = "l_middistal"
HAnimSegment254.DEF = "hanim_l_middistal"
Transform255 = x3d.Transform()
Transform255.translation = [0.1086,0.0001,0.0368]
Shape256 = x3d.Shape()
IndexedFaceSet257 = x3d.IndexedFaceSet()
IndexedFaceSet257.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet257.creaseAngle = 0.5
Coordinate258 = x3d.Coordinate()
Coordinate258.USE = "points"

IndexedFaceSet257.coord.append(Coordinate258)

Shape256.geometry = IndexedFaceSet257
Appearance259 = x3d.Appearance()
Material260 = x3d.Material()
Material260.USE = "JOINT_COLOR"

Appearance259.material = Material260

Shape256.appearance = Appearance259

Transform255.children.append(Shape256)

HAnimSegment254.children.append(Transform255)
HAnimSite261 = x3d.HAnimSite()
HAnimSite261.name = "l_middistal_tip"
HAnimSite261.DEF = "hanim_l_middistal_tip"
HAnimSite261.translation = [0.1354,0.0016,0.1476]
Shape262 = x3d.Shape()
IndexedFaceSet263 = x3d.IndexedFaceSet()
IndexedFaceSet263.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet263.creaseAngle = 0.5
Coordinate264 = x3d.Coordinate()
Coordinate264.USE = "points"

IndexedFaceSet263.coord.append(Coordinate264)

Shape262.geometry = IndexedFaceSet263
Appearance265 = x3d.Appearance()
Material266 = x3d.Material()
Material266.USE = "HAND_FEET_COLOR"

Appearance265.material = Material266

Shape262.appearance = Appearance265

HAnimSite261.children.append(Shape262)

HAnimSegment254.children.append(HAnimSite261)
HAnimSite267 = x3d.HAnimSite()
HAnimSite267.name = "l_metatarsal_pha1_pt"
HAnimSite267.DEF = "hanim_l_metatarsal_pha1_pt"
HAnimSite267.translation = [0.0816,0.0232,0.0106]
Shape268 = x3d.Shape()
IndexedFaceSet269 = x3d.IndexedFaceSet()
IndexedFaceSet269.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet269.creaseAngle = 0.5
Coordinate270 = x3d.Coordinate()
Coordinate270.USE = "points"

IndexedFaceSet269.coord.append(Coordinate270)

Shape268.geometry = IndexedFaceSet269
Appearance271 = x3d.Appearance()
Material272 = x3d.Material()
Material272.USE = "HAND_FEET_COLOR"

Appearance271.material = Material272

Shape268.appearance = Appearance271

HAnimSite267.children.append(Shape268)

HAnimSegment254.children.append(HAnimSite267)

HAnimJoint253.children.append(HAnimSegment254)
HAnimJoint273 = x3d.HAnimJoint()
HAnimJoint273.name = "l_metatarsal"
HAnimJoint273.DEF = "hanim_l_metatarsal"
HAnimJoint273.center = [0.1086,0,0.0762]
HAnimJoint273.ulimit = [0,0,0]
HAnimJoint273.llimit = [0,0,0]
HAnimSegment274 = x3d.HAnimSegment()
HAnimSegment274.name = "l_forefoot"
HAnimSegment274.DEF = "hanim_l_forefoot"
Transform275 = x3d.Transform()
Transform275.translation = [0.1086,0,0.0762]
Shape276 = x3d.Shape()
IndexedFaceSet277 = x3d.IndexedFaceSet()
IndexedFaceSet277.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet277.creaseAngle = 0.5
Coordinate278 = x3d.Coordinate()
Coordinate278.USE = "points"

IndexedFaceSet277.coord.append(Coordinate278)

Shape276.geometry = IndexedFaceSet277
Appearance279 = x3d.Appearance()
Material280 = x3d.Material()
Material280.USE = "JOINT_COLOR"

Appearance279.material = Material280

Shape276.appearance = Appearance279

Transform275.children.append(Shape276)

HAnimSegment274.children.append(Transform275)
HAnimSite281 = x3d.HAnimSite()
HAnimSite281.name = "l_forefoot_tip"
HAnimSite281.DEF = "hanim_l_forefoot_tip"
HAnimSite281.translation = [0.1354,0.0016,0.1476]
Shape282 = x3d.Shape()
IndexedFaceSet283 = x3d.IndexedFaceSet()
IndexedFaceSet283.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet283.creaseAngle = 0.5
Coordinate284 = x3d.Coordinate()
Coordinate284.USE = "points"

IndexedFaceSet283.coord.append(Coordinate284)

Shape282.geometry = IndexedFaceSet283
Appearance285 = x3d.Appearance()
Material286 = x3d.Material()
Material286.USE = "HAND_FEET_COLOR"

Appearance285.material = Material286

Shape282.appearance = Appearance285

HAnimSite281.children.append(Shape282)

HAnimSegment274.children.append(HAnimSite281)
HAnimSite287 = x3d.HAnimSite()
HAnimSite287.name = "l_metatarsal_pha5_pt"
HAnimSite287.DEF = "hanim_l_metatarsal_pha5_pt"
HAnimSite287.translation = [0.1825,0.007,0.0928]
## CAESAR Feature Point #66
Shape288 = x3d.Shape()
IndexedFaceSet289 = x3d.IndexedFaceSet()
IndexedFaceSet289.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet289.creaseAngle = 0.5
Coordinate290 = x3d.Coordinate()
Coordinate290.USE = "points"

IndexedFaceSet289.coord.append(Coordinate290)

Shape288.geometry = IndexedFaceSet289
Appearance291 = x3d.Appearance()
Material292 = x3d.Material()
Material292.USE = "HAND_FEET_COLOR"

Appearance291.material = Material292

Shape288.appearance = Appearance291

HAnimSite287.children.append(Shape288)

HAnimSegment274.children.append(HAnimSite287)
HAnimSite293 = x3d.HAnimSite()
HAnimSite293.name = "l_digit2_pt"
HAnimSite293.DEF = "hanim_l_digit2_pt"
HAnimSite293.translation = [0.1195,0.0079,0.1433]
## CAESAR Feature Point #72
Shape294 = x3d.Shape()
IndexedFaceSet295 = x3d.IndexedFaceSet()
IndexedFaceSet295.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet295.creaseAngle = 0.5
Coordinate296 = x3d.Coordinate()
Coordinate296.USE = "points"

IndexedFaceSet295.coord.append(Coordinate296)

Shape294.geometry = IndexedFaceSet295
Appearance297 = x3d.Appearance()
Material298 = x3d.Material()
Material298.USE = "HAND_FEET_COLOR"

Appearance297.material = Material298

Shape294.appearance = Appearance297

HAnimSite293.children.append(Shape294)

HAnimSegment274.children.append(HAnimSite293)

HAnimJoint273.children.append(HAnimSegment274)

HAnimJoint253.children.append(HAnimJoint273)

HAnimJoint245.children.append(HAnimJoint253)

HAnimJoint213.children.append(HAnimJoint245)

HAnimJoint205.children.append(HAnimJoint213)

HAnimJoint179.children.append(HAnimJoint205)

HAnimJoint117.children.append(HAnimJoint179)
HAnimJoint299 = x3d.HAnimJoint()
HAnimJoint299.name = "r_hip"
HAnimJoint299.DEF = "hanim_r_hip"
HAnimJoint299.center = [-0.095,0.9171,0.0029]
HAnimJoint299.ulimit = [0,0,0]
HAnimJoint299.llimit = [0,0,0]
HAnimSegment300 = x3d.HAnimSegment()
HAnimSegment300.name = "r_thigh"
HAnimSegment300.DEF = "hanim_r_thigh"
Transform301 = x3d.Transform()
Transform301.translation = [-0.095,0.9171,0.0029]
Shape302 = x3d.Shape()
IndexedFaceSet303 = x3d.IndexedFaceSet()
IndexedFaceSet303.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet303.creaseAngle = 0.5
Coordinate304 = x3d.Coordinate()
Coordinate304.USE = "points"

IndexedFaceSet303.coord.append(Coordinate304)

Shape302.geometry = IndexedFaceSet303
Appearance305 = x3d.Appearance()
Material306 = x3d.Material()
Material306.USE = "MIN_COLOR"

Appearance305.material = Material306

Shape302.appearance = Appearance305

Transform301.children.append(Shape302)

HAnimSegment300.children.append(Transform301)
HAnimSite307 = x3d.HAnimSite()
HAnimSite307.name = "r_knee_crease_pt"
HAnimSite307.DEF = "hanim_r_knee_crease_pt"
HAnimSite307.translation = [-0.0825,0.4932,-0.0326]
Shape308 = x3d.Shape()
IndexedFaceSet309 = x3d.IndexedFaceSet()
IndexedFaceSet309.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet309.creaseAngle = 0.5
Coordinate310 = x3d.Coordinate()
Coordinate310.USE = "points"

IndexedFaceSet309.coord.append(Coordinate310)

Shape308.geometry = IndexedFaceSet309
Appearance311 = x3d.Appearance()
Material312 = x3d.Material()
Material312.USE = "SITE_COLOR"

Appearance311.material = Material312

Shape308.appearance = Appearance311

HAnimSite307.children.append(Shape308)

HAnimSegment300.children.append(HAnimSite307)
HAnimSite313 = x3d.HAnimSite()
HAnimSite313.name = "r_femoral_lateral_epicn_pt"
HAnimSite313.DEF = "hanim_r_femoral_lateral_epicn_pt"
HAnimSite313.translation = [-0.1421,0.4992,0.031]
Shape314 = x3d.Shape()
IndexedFaceSet315 = x3d.IndexedFaceSet()
IndexedFaceSet315.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet315.creaseAngle = 0.5
Coordinate316 = x3d.Coordinate()
Coordinate316.USE = "points"

IndexedFaceSet315.coord.append(Coordinate316)

Shape314.geometry = IndexedFaceSet315
Appearance317 = x3d.Appearance()
Material318 = x3d.Material()
Material318.USE = "SITE_COLOR"

Appearance317.material = Material318

Shape314.appearance = Appearance317

HAnimSite313.children.append(Shape314)

HAnimSegment300.children.append(HAnimSite313)
HAnimSite319 = x3d.HAnimSite()
HAnimSite319.name = "r_femoral_medial_epicn_pt"
HAnimSite319.DEF = "hanim_r_femoral_medial_epicn_pt"
HAnimSite319.translation = [-0.0221,0.5014,0.0289]
Shape320 = x3d.Shape()
IndexedFaceSet321 = x3d.IndexedFaceSet()
IndexedFaceSet321.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet321.creaseAngle = 0.5
Coordinate322 = x3d.Coordinate()
Coordinate322.USE = "points"

IndexedFaceSet321.coord.append(Coordinate322)

Shape320.geometry = IndexedFaceSet321
Appearance323 = x3d.Appearance()
Material324 = x3d.Material()
Material324.USE = "SITE_COLOR"

Appearance323.material = Material324

Shape320.appearance = Appearance323

HAnimSite319.children.append(Shape320)

HAnimSegment300.children.append(HAnimSite319)

HAnimJoint299.children.append(HAnimSegment300)
HAnimJoint325 = x3d.HAnimJoint()
HAnimJoint325.name = "r_knee"
HAnimJoint325.DEF = "hanim_r_knee"
HAnimJoint325.center = [-0.0867,0.4913,0.0318]
HAnimJoint325.ulimit = [0,0,0]
HAnimJoint325.llimit = [0,0,0]
HAnimSegment326 = x3d.HAnimSegment()
HAnimSegment326.name = "r_calf"
HAnimSegment326.DEF = "hanim_r_calf"
Transform327 = x3d.Transform()
Transform327.translation = [-0.0867,0.4913,0.0318]
Shape328 = x3d.Shape()
IndexedFaceSet329 = x3d.IndexedFaceSet()
IndexedFaceSet329.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet329.creaseAngle = 0.5
Coordinate330 = x3d.Coordinate()
Coordinate330.USE = "points"

IndexedFaceSet329.coord.append(Coordinate330)

Shape328.geometry = IndexedFaceSet329
Appearance331 = x3d.Appearance()
Material332 = x3d.Material()
Material332.USE = "SITE_COLOR"

Appearance331.material = Material332

Shape328.appearance = Appearance331

Transform327.children.append(Shape328)

HAnimSegment326.children.append(Transform327)

HAnimJoint325.children.append(HAnimSegment326)
HAnimJoint333 = x3d.HAnimJoint()
HAnimJoint333.name = "r_ankle"
HAnimJoint333.DEF = "hanim_r_ankle"
HAnimJoint333.center = [-0.0801,0.0712,-0.0766]
HAnimJoint333.ulimit = [0,0,0]
HAnimJoint333.llimit = [0,0,0]
HAnimSegment334 = x3d.HAnimSegment()
HAnimSegment334.name = "r_hindfoot"
HAnimSegment334.DEF = "hanim_r_hindfoot"
Transform335 = x3d.Transform()
Transform335.translation = [-0.0801,0.0712,-0.0766]
Shape336 = x3d.Shape()
IndexedFaceSet337 = x3d.IndexedFaceSet()
IndexedFaceSet337.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet337.creaseAngle = 0.5
Coordinate338 = x3d.Coordinate()
Coordinate338.USE = "points"

IndexedFaceSet337.coord.append(Coordinate338)

Shape336.geometry = IndexedFaceSet337
Appearance339 = x3d.Appearance()
Material340 = x3d.Material()
Material340.USE = "MIN_COLOR"

Appearance339.material = Material340

Shape336.appearance = Appearance339

Transform335.children.append(Shape336)

HAnimSegment334.children.append(Transform335)
HAnimSite341 = x3d.HAnimSite()
HAnimSite341.name = "r_lateral_malleolus_pt"
HAnimSite341.DEF = "hanim_r_lateral_malleolus_pt"
HAnimSite341.translation = [-0.1006,0.0658,-0.1075]
Shape342 = x3d.Shape()
IndexedFaceSet343 = x3d.IndexedFaceSet()
IndexedFaceSet343.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet343.creaseAngle = 0.5
Coordinate344 = x3d.Coordinate()
Coordinate344.USE = "points"

IndexedFaceSet343.coord.append(Coordinate344)

Shape342.geometry = IndexedFaceSet343
Appearance345 = x3d.Appearance()
Material346 = x3d.Material()
Material346.USE = "HAND_FEET_COLOR"

Appearance345.material = Material346

Shape342.appearance = Appearance345

HAnimSite341.children.append(Shape342)

HAnimSegment334.children.append(HAnimSite341)
HAnimSite347 = x3d.HAnimSite()
HAnimSite347.name = "r_medial_malleolus_pt"
HAnimSite347.DEF = "hanim_r_medial_malleolus_pt"
HAnimSite347.translation = [-0.0591,0.076,-0.0928]
Shape348 = x3d.Shape()
IndexedFaceSet349 = x3d.IndexedFaceSet()
IndexedFaceSet349.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet349.creaseAngle = 0.5
Coordinate350 = x3d.Coordinate()
Coordinate350.USE = "points"

IndexedFaceSet349.coord.append(Coordinate350)

Shape348.geometry = IndexedFaceSet349
Appearance351 = x3d.Appearance()
Material352 = x3d.Material()
Material352.USE = "HAND_FEET_COLOR"

Appearance351.material = Material352

Shape348.appearance = Appearance351

HAnimSite347.children.append(Shape348)

HAnimSegment334.children.append(HAnimSite347)
HAnimSite353 = x3d.HAnimSite()
HAnimSite353.name = "r_sphyrion_pt"
HAnimSite353.DEF = "hanim_r_sphyrion_pt"
HAnimSite353.translation = [-0.0603,0.061,-0.1002]
Shape354 = x3d.Shape()
IndexedFaceSet355 = x3d.IndexedFaceSet()
IndexedFaceSet355.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet355.creaseAngle = 0.5
Coordinate356 = x3d.Coordinate()
Coordinate356.USE = "points"

IndexedFaceSet355.coord.append(Coordinate356)

Shape354.geometry = IndexedFaceSet355
Appearance357 = x3d.Appearance()
Material358 = x3d.Material()
Material358.USE = "HAND_FEET_COLOR"

Appearance357.material = Material358

Shape354.appearance = Appearance357

HAnimSite353.children.append(Shape354)

HAnimSegment334.children.append(HAnimSite353)
HAnimSite359 = x3d.HAnimSite()
HAnimSite359.name = "r_calcaneous_post_pt"
HAnimSite359.DEF = "hanim_r_calcaneous_post_pt"
HAnimSite359.translation = [-0.0692,0.0297,-0.1221]
Shape360 = x3d.Shape()
IndexedFaceSet361 = x3d.IndexedFaceSet()
IndexedFaceSet361.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet361.creaseAngle = 0.5
Coordinate362 = x3d.Coordinate()
Coordinate362.USE = "points"

IndexedFaceSet361.coord.append(Coordinate362)

Shape360.geometry = IndexedFaceSet361
Appearance363 = x3d.Appearance()
Material364 = x3d.Material()
Material364.USE = "HAND_FEET_COLOR"

Appearance363.material = Material364

Shape360.appearance = Appearance363

HAnimSite359.children.append(Shape360)

HAnimSegment334.children.append(HAnimSite359)

HAnimJoint333.children.append(HAnimSegment334)
HAnimJoint365 = x3d.HAnimJoint()
HAnimJoint365.name = "r_midtarsal"
HAnimJoint365.DEF = "hanim_r_midtarsal"
HAnimJoint365.center = [-0.0801,0,0.0368]
HAnimJoint365.ulimit = [0,0,0]
HAnimJoint365.llimit = [0,0,0]
HAnimSegment366 = x3d.HAnimSegment()
HAnimSegment366.name = "r_middistal"
HAnimSegment366.DEF = "hanim_r_middistal"
Transform367 = x3d.Transform()
Transform367.translation = [-0.0801,0,0.0368]
Shape368 = x3d.Shape()
IndexedFaceSet369 = x3d.IndexedFaceSet()
IndexedFaceSet369.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet369.creaseAngle = 0.5
Coordinate370 = x3d.Coordinate()
Coordinate370.USE = "points"

IndexedFaceSet369.coord.append(Coordinate370)

Shape368.geometry = IndexedFaceSet369
Appearance371 = x3d.Appearance()
Material372 = x3d.Material()
Material372.USE = "JOINT_COLOR"

Appearance371.material = Material372

Shape368.appearance = Appearance371

Transform367.children.append(Shape368)

HAnimSegment366.children.append(Transform367)
HAnimSite373 = x3d.HAnimSite()
HAnimSite373.name = "r_middistal_tip"
HAnimSite373.DEF = "hanim_r_middistal_tip"
HAnimSite373.translation = [-0.1043,-0.0227,0.145]
Shape374 = x3d.Shape()
IndexedFaceSet375 = x3d.IndexedFaceSet()
IndexedFaceSet375.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet375.creaseAngle = 0.5
Coordinate376 = x3d.Coordinate()
Coordinate376.USE = "points"

IndexedFaceSet375.coord.append(Coordinate376)

Shape374.geometry = IndexedFaceSet375
Appearance377 = x3d.Appearance()
Material378 = x3d.Material()
Material378.USE = "HAND_FEET_COLOR"

Appearance377.material = Material378

Shape374.appearance = Appearance377

HAnimSite373.children.append(Shape374)

HAnimSegment366.children.append(HAnimSite373)
HAnimSite379 = x3d.HAnimSite()
HAnimSite379.name = "r_metatarsal_pha5_pt"
HAnimSite379.DEF = "hanim_r_metatarsal_pha5_pt"
HAnimSite379.translation = [-0.1523,0.0166,0.0895]
Shape380 = x3d.Shape()
IndexedFaceSet381 = x3d.IndexedFaceSet()
IndexedFaceSet381.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet381.creaseAngle = 0.5
Coordinate382 = x3d.Coordinate()
Coordinate382.USE = "points"

IndexedFaceSet381.coord.append(Coordinate382)

Shape380.geometry = IndexedFaceSet381
Appearance383 = x3d.Appearance()
Material384 = x3d.Material()
Material384.USE = "HAND_FEET_COLOR"

Appearance383.material = Material384

Shape380.appearance = Appearance383

HAnimSite379.children.append(Shape380)

HAnimSegment366.children.append(HAnimSite379)
HAnimSite385 = x3d.HAnimSite()
HAnimSite385.name = "r_metatarsal_pha1_pt"
HAnimSite385.DEF = "hanim_r_metatarsal_pha1_pt"
HAnimSite385.translation = [-0.0521,0.026,0.0127]
Shape386 = x3d.Shape()
IndexedFaceSet387 = x3d.IndexedFaceSet()
IndexedFaceSet387.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet387.creaseAngle = 0.5
Coordinate388 = x3d.Coordinate()
Coordinate388.USE = "points"

IndexedFaceSet387.coord.append(Coordinate388)

Shape386.geometry = IndexedFaceSet387
Appearance389 = x3d.Appearance()
Material390 = x3d.Material()
Material390.USE = "HAND_FEET_COLOR"

Appearance389.material = Material390

Shape386.appearance = Appearance389

HAnimSite385.children.append(Shape386)

HAnimSegment366.children.append(HAnimSite385)
HAnimSite391 = x3d.HAnimSite()
HAnimSite391.name = "r_digit2_pt"
HAnimSite391.DEF = "hanim_r_digit2_pt"
HAnimSite391.translation = [-0.0883,0.0134,0.1383]
Shape392 = x3d.Shape()
IndexedFaceSet393 = x3d.IndexedFaceSet()
IndexedFaceSet393.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet393.creaseAngle = 0.5
Coordinate394 = x3d.Coordinate()
Coordinate394.USE = "points"

IndexedFaceSet393.coord.append(Coordinate394)

Shape392.geometry = IndexedFaceSet393
Appearance395 = x3d.Appearance()
Material396 = x3d.Material()
Material396.USE = "HAND_FEET_COLOR"

Appearance395.material = Material396

Shape392.appearance = Appearance395

HAnimSite391.children.append(Shape392)

HAnimSegment366.children.append(HAnimSite391)

HAnimJoint365.children.append(HAnimSegment366)

HAnimJoint333.children.append(HAnimJoint365)

HAnimJoint325.children.append(HAnimJoint333)

HAnimJoint299.children.append(HAnimJoint325)

HAnimJoint117.children.append(HAnimJoint299)

HAnimJoint102.children.append(HAnimJoint117)
HAnimJoint397 = x3d.HAnimJoint()
HAnimJoint397.name = "vl5"
HAnimJoint397.DEF = "hanim_vl5"
HAnimJoint397.center = [0.0028,1.0568,-0.0776]
HAnimJoint397.ulimit = [0,0,0]
HAnimJoint397.llimit = [0,0,0]
HAnimSegment398 = x3d.HAnimSegment()
HAnimSegment398.name = "l5"
HAnimSegment398.DEF = "hanim_l5"
Transform399 = x3d.Transform()
Transform399.translation = [0.0028,1.0568,-0.0776]
Shape400 = x3d.Shape()
IndexedFaceSet401 = x3d.IndexedFaceSet()
IndexedFaceSet401.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet401.creaseAngle = 0.5
Coordinate402 = x3d.Coordinate()
Coordinate402.USE = "points"

IndexedFaceSet401.coord.append(Coordinate402)

Shape400.geometry = IndexedFaceSet401
Appearance403 = x3d.Appearance()
Material404 = x3d.Material()
Material404.USE = "REC_SPINAL_COLOR"

Appearance403.material = Material404

Shape400.appearance = Appearance403

Transform399.children.append(Shape400)

HAnimSegment398.children.append(Transform399)

HAnimJoint397.children.append(HAnimSegment398)
HAnimJoint405 = x3d.HAnimJoint()
HAnimJoint405.name = "vl4"
HAnimJoint405.DEF = "hanim_vl4"
HAnimJoint405.center = [0.0035,1.0925,-0.0787]
HAnimJoint405.ulimit = [0,0,0]
HAnimJoint405.llimit = [0,0,0]
HAnimSegment406 = x3d.HAnimSegment()
HAnimSegment406.name = "l4"
HAnimSegment406.DEF = "hanim_l4"
Transform407 = x3d.Transform()
Transform407.translation = [0.0035,1.0925,-0.0787]
Shape408 = x3d.Shape()
IndexedFaceSet409 = x3d.IndexedFaceSet()
IndexedFaceSet409.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet409.creaseAngle = 0.5
Coordinate410 = x3d.Coordinate()
Coordinate410.USE = "points"

IndexedFaceSet409.coord.append(Coordinate410)

Shape408.geometry = IndexedFaceSet409
Appearance411 = x3d.Appearance()
Material412 = x3d.Material()
Material412.USE = "SPINAL_COLOR"

Appearance411.material = Material412

Shape408.appearance = Appearance411

Transform407.children.append(Shape408)

HAnimSegment406.children.append(Transform407)

HAnimJoint405.children.append(HAnimSegment406)
HAnimJoint413 = x3d.HAnimJoint()
HAnimJoint413.name = "vl3"
HAnimJoint413.DEF = "hanim_vl3"
HAnimJoint413.center = [0.0041,1.1276,-0.0796]
HAnimJoint413.ulimit = [0,0,0]
HAnimJoint413.llimit = [0,0,0]
HAnimSegment414 = x3d.HAnimSegment()
HAnimSegment414.name = "l3"
HAnimSegment414.DEF = "hanim_l3"
Transform415 = x3d.Transform()
Transform415.translation = [0.0041,1.1276,-0.0796]
Shape416 = x3d.Shape()
IndexedFaceSet417 = x3d.IndexedFaceSet()
IndexedFaceSet417.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet417.creaseAngle = 0.5
Coordinate418 = x3d.Coordinate()
Coordinate418.USE = "points"

IndexedFaceSet417.coord.append(Coordinate418)

Shape416.geometry = IndexedFaceSet417
Appearance419 = x3d.Appearance()
Material420 = x3d.Material()
Material420.USE = "REC_SPINAL_COLOR"

Appearance419.material = Material420

Shape416.appearance = Appearance419

Transform415.children.append(Shape416)

HAnimSegment414.children.append(Transform415)

HAnimJoint413.children.append(HAnimSegment414)
HAnimJoint421 = x3d.HAnimJoint()
HAnimJoint421.name = "vl2"
HAnimJoint421.DEF = "hanim_vl2"
HAnimJoint421.center = [0.0045,1.1546,-0.08]
HAnimJoint421.ulimit = [0,0,0]
HAnimJoint421.llimit = [0,0,0]
HAnimSegment422 = x3d.HAnimSegment()
HAnimSegment422.name = "l2"
HAnimSegment422.DEF = "hanim_l2"
Transform423 = x3d.Transform()
Transform423.translation = [0.0045,1.1546,-0.08]
Shape424 = x3d.Shape()
IndexedFaceSet425 = x3d.IndexedFaceSet()
IndexedFaceSet425.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet425.creaseAngle = 0.5
Coordinate426 = x3d.Coordinate()
Coordinate426.USE = "points"

IndexedFaceSet425.coord.append(Coordinate426)

Shape424.geometry = IndexedFaceSet425
Appearance427 = x3d.Appearance()
Material428 = x3d.Material()
Material428.USE = "SPINAL_COLOR"

Appearance427.material = Material428

Shape424.appearance = Appearance427

Transform423.children.append(Shape424)

HAnimSegment422.children.append(Transform423)

HAnimJoint421.children.append(HAnimSegment422)
HAnimJoint429 = x3d.HAnimJoint()
HAnimJoint429.name = "vl1"
HAnimJoint429.DEF = "hanim_vl1"
HAnimJoint429.center = [0.0048,1.1912,-0.0805]
HAnimJoint429.ulimit = [0,0,0]
HAnimJoint429.llimit = [0,0,0]
HAnimSegment430 = x3d.HAnimSegment()
HAnimSegment430.name = "l1"
HAnimSegment430.DEF = "hanim_l1"
Transform431 = x3d.Transform()
Transform431.translation = [0.0048,1.1912,-0.0805]
Shape432 = x3d.Shape()
IndexedFaceSet433 = x3d.IndexedFaceSet()
IndexedFaceSet433.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet433.creaseAngle = 0.5
Coordinate434 = x3d.Coordinate()
Coordinate434.USE = "points"

IndexedFaceSet433.coord.append(Coordinate434)

Shape432.geometry = IndexedFaceSet433
Appearance435 = x3d.Appearance()
Material436 = x3d.Material()
Material436.USE = "REC_SPINAL_COLOR"

Appearance435.material = Material436

Shape432.appearance = Appearance435

Transform431.children.append(Shape432)

HAnimSegment430.children.append(Transform431)

HAnimJoint429.children.append(HAnimSegment430)
HAnimJoint437 = x3d.HAnimJoint()
HAnimJoint437.name = "vt12"
HAnimJoint437.DEF = "hanim_vt12"
HAnimJoint437.center = [0.0051,1.2278,-0.0808]
HAnimJoint437.ulimit = [0,0,0]
HAnimJoint437.llimit = [0,0,0]
HAnimSegment438 = x3d.HAnimSegment()
HAnimSegment438.name = "t12"
HAnimSegment438.DEF = "hanim_t12"
Transform439 = x3d.Transform()
Transform439.translation = [0.0051,1.2278,-0.0808]
Shape440 = x3d.Shape()
IndexedFaceSet441 = x3d.IndexedFaceSet()
IndexedFaceSet441.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet441.creaseAngle = 0.5
Coordinate442 = x3d.Coordinate()
Coordinate442.USE = "points"

IndexedFaceSet441.coord.append(Coordinate442)

Shape440.geometry = IndexedFaceSet441
Appearance443 = x3d.Appearance()
Material444 = x3d.Material()
Material444.USE = "SPINAL_COLOR"

Appearance443.material = Material444

Shape440.appearance = Appearance443

Transform439.children.append(Shape440)

HAnimSegment438.children.append(Transform439)

HAnimJoint437.children.append(HAnimSegment438)
HAnimJoint445 = x3d.HAnimJoint()
HAnimJoint445.name = "vt11"
HAnimJoint445.DEF = "hanim_vt11"
HAnimJoint445.center = [0.0053,1.2679,-0.081]
HAnimJoint445.ulimit = [0,0,0]
HAnimJoint445.llimit = [0,0,0]
HAnimSegment446 = x3d.HAnimSegment()
HAnimSegment446.name = "t11"
HAnimSegment446.DEF = "hanim_t11"
Transform447 = x3d.Transform()
Transform447.translation = [0.0053,1.2679,-0.081]
Shape448 = x3d.Shape()
IndexedFaceSet449 = x3d.IndexedFaceSet()
IndexedFaceSet449.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet449.creaseAngle = 0.5
Coordinate450 = x3d.Coordinate()
Coordinate450.USE = "points"

IndexedFaceSet449.coord.append(Coordinate450)

Shape448.geometry = IndexedFaceSet449
Appearance451 = x3d.Appearance()
Material452 = x3d.Material()
Material452.USE = "SPINAL_COLOR"

Appearance451.material = Material452

Shape448.appearance = Appearance451

Transform447.children.append(Shape448)

HAnimSegment446.children.append(Transform447)

HAnimJoint445.children.append(HAnimSegment446)
HAnimJoint453 = x3d.HAnimJoint()
HAnimJoint453.name = "vt10"
HAnimJoint453.DEF = "hanim_vt10"
HAnimJoint453.center = [0.0056,1.2848,-0.0822]
HAnimJoint453.ulimit = [0,0,0]
HAnimJoint453.llimit = [0,0,0]
HAnimSegment454 = x3d.HAnimSegment()
HAnimSegment454.name = "t10"
HAnimSegment454.DEF = "hanim_t10"
Transform455 = x3d.Transform()
Transform455.translation = [0.0056,1.2848,-0.0822]
Shape456 = x3d.Shape()
IndexedFaceSet457 = x3d.IndexedFaceSet()
IndexedFaceSet457.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet457.creaseAngle = 0.5
Coordinate458 = x3d.Coordinate()
Coordinate458.USE = "points"

IndexedFaceSet457.coord.append(Coordinate458)

Shape456.geometry = IndexedFaceSet457
Appearance459 = x3d.Appearance()
Material460 = x3d.Material()
Material460.USE = "REC_SPINAL_COLOR"

Appearance459.material = Material460

Shape456.appearance = Appearance459

Transform455.children.append(Shape456)

HAnimSegment454.children.append(Transform455)

HAnimJoint453.children.append(HAnimSegment454)
HAnimJoint461 = x3d.HAnimJoint()
HAnimJoint461.name = "vt9"
HAnimJoint461.DEF = "hanim_vt9"
HAnimJoint461.center = [0.0057,1.3126,-0.0838]
HAnimJoint461.ulimit = [0,0,0]
HAnimJoint461.llimit = [0,0,0]
HAnimSegment462 = x3d.HAnimSegment()
HAnimSegment462.name = "t9"
HAnimSegment462.DEF = "hanim_t9"
Transform463 = x3d.Transform()
Transform463.translation = [0.0057,1.3126,-0.0838]
Shape464 = x3d.Shape()
IndexedFaceSet465 = x3d.IndexedFaceSet()
IndexedFaceSet465.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet465.creaseAngle = 0.5
Coordinate466 = x3d.Coordinate()
Coordinate466.USE = "points"

IndexedFaceSet465.coord.append(Coordinate466)

Shape464.geometry = IndexedFaceSet465
Appearance467 = x3d.Appearance()
Material468 = x3d.Material()
Material468.USE = "SPINAL_COLOR"

Appearance467.material = Material468

Shape464.appearance = Appearance467

Transform463.children.append(Shape464)

HAnimSegment462.children.append(Transform463)

HAnimJoint461.children.append(HAnimSegment462)
HAnimJoint469 = x3d.HAnimJoint()
HAnimJoint469.name = "vt8"
HAnimJoint469.DEF = "hanim_vt8"
HAnimJoint469.center = [0.0057,1.3382,-0.0845]
HAnimJoint469.ulimit = [0,0,0]
HAnimJoint469.llimit = [0,0,0]
HAnimSegment470 = x3d.HAnimSegment()
HAnimSegment470.name = "t8"
HAnimSegment470.DEF = "hanim_t8"
Transform471 = x3d.Transform()
Transform471.translation = [0.0057,1.3382,-0.0845]
Shape472 = x3d.Shape()
IndexedFaceSet473 = x3d.IndexedFaceSet()
IndexedFaceSet473.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet473.creaseAngle = 0.5
Coordinate474 = x3d.Coordinate()
Coordinate474.USE = "points"

IndexedFaceSet473.coord.append(Coordinate474)

Shape472.geometry = IndexedFaceSet473
Appearance475 = x3d.Appearance()
Material476 = x3d.Material()
Material476.USE = "SPINAL_COLOR"

Appearance475.material = Material476

Shape472.appearance = Appearance475

Transform471.children.append(Shape472)

HAnimSegment470.children.append(Transform471)

HAnimJoint469.children.append(HAnimSegment470)
HAnimJoint477 = x3d.HAnimJoint()
HAnimJoint477.name = "vt7"
HAnimJoint477.DEF = "hanim_vt7"
HAnimJoint477.center = [0.0058,1.3625,-0.0833]
HAnimJoint477.ulimit = [0,0,0]
HAnimJoint477.llimit = [0,0,0]
HAnimSegment478 = x3d.HAnimSegment()
HAnimSegment478.name = "t7"
HAnimSegment478.DEF = "hanim_t7"
Transform479 = x3d.Transform()
Transform479.translation = [0.0058,1.3625,-0.0833]
Shape480 = x3d.Shape()
IndexedFaceSet481 = x3d.IndexedFaceSet()
IndexedFaceSet481.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet481.creaseAngle = 0.5
Coordinate482 = x3d.Coordinate()
Coordinate482.USE = "points"

IndexedFaceSet481.coord.append(Coordinate482)

Shape480.geometry = IndexedFaceSet481
Appearance483 = x3d.Appearance()
Material484 = x3d.Material()
Material484.USE = "SPINAL_COLOR"

Appearance483.material = Material484

Shape480.appearance = Appearance483

Transform479.children.append(Shape480)

HAnimSegment478.children.append(Transform479)

HAnimJoint477.children.append(HAnimSegment478)
HAnimJoint485 = x3d.HAnimJoint()
HAnimJoint485.name = "vt6"
HAnimJoint485.DEF = "hanim_vt6"
HAnimJoint485.center = [0.0059,1.3866,-0.08]
HAnimJoint485.ulimit = [0,0,0]
HAnimJoint485.llimit = [0,0,0]
HAnimSegment486 = x3d.HAnimSegment()
HAnimSegment486.name = "t6"
HAnimSegment486.DEF = "hanim_t6"
Transform487 = x3d.Transform()
Transform487.translation = [0.0059,1.3866,-0.08]
Shape488 = x3d.Shape()
IndexedFaceSet489 = x3d.IndexedFaceSet()
IndexedFaceSet489.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet489.creaseAngle = 0.5
Coordinate490 = x3d.Coordinate()
Coordinate490.USE = "points"

IndexedFaceSet489.coord.append(Coordinate490)

Shape488.geometry = IndexedFaceSet489
Appearance491 = x3d.Appearance()
Material492 = x3d.Material()
Material492.USE = "REC_SPINAL_COLOR"

Appearance491.material = Material492

Shape488.appearance = Appearance491

Transform487.children.append(Shape488)

HAnimSegment486.children.append(Transform487)

HAnimJoint485.children.append(HAnimSegment486)
HAnimJoint493 = x3d.HAnimJoint()
HAnimJoint493.name = "vt5"
HAnimJoint493.DEF = "hanim_vt5"
HAnimJoint493.center = [0.006,1.4102,-0.0745]
HAnimJoint493.ulimit = [0,0,0]
HAnimJoint493.llimit = [0,0,0]
HAnimSegment494 = x3d.HAnimSegment()
HAnimSegment494.name = "t5"
HAnimSegment494.DEF = "hanim_t5"
Transform495 = x3d.Transform()
Transform495.translation = [0.006,1.4102,-0.0745]
Shape496 = x3d.Shape()
IndexedFaceSet497 = x3d.IndexedFaceSet()
IndexedFaceSet497.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet497.creaseAngle = 0.5
Coordinate498 = x3d.Coordinate()
Coordinate498.USE = "points"

IndexedFaceSet497.coord.append(Coordinate498)

Shape496.geometry = IndexedFaceSet497
Appearance499 = x3d.Appearance()
Material500 = x3d.Material()
Material500.USE = "SPINAL_COLOR"

Appearance499.material = Material500

Shape496.appearance = Appearance499

Transform495.children.append(Shape496)

HAnimSegment494.children.append(Transform495)

HAnimJoint493.children.append(HAnimSegment494)
HAnimJoint501 = x3d.HAnimJoint()
HAnimJoint501.name = "vt4"
HAnimJoint501.DEF = "hanim_vt4"
HAnimJoint501.center = [0.0061,1.432,-0.0675]
HAnimJoint501.ulimit = [0,0,0]
HAnimJoint501.llimit = [0,0,0]
HAnimSegment502 = x3d.HAnimSegment()
HAnimSegment502.name = "t4"
HAnimSegment502.DEF = "hanim_t4"
Transform503 = x3d.Transform()
Transform503.translation = [0.0061,1.432,-0.0675]
Shape504 = x3d.Shape()
IndexedFaceSet505 = x3d.IndexedFaceSet()
IndexedFaceSet505.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet505.creaseAngle = 0.5
Coordinate506 = x3d.Coordinate()
Coordinate506.USE = "points"

IndexedFaceSet505.coord.append(Coordinate506)

Shape504.geometry = IndexedFaceSet505
Appearance507 = x3d.Appearance()
Material508 = x3d.Material()
Material508.USE = "SPINAL_COLOR"

Appearance507.material = Material508

Shape504.appearance = Appearance507

Transform503.children.append(Shape504)

HAnimSegment502.children.append(Transform503)

HAnimJoint501.children.append(HAnimSegment502)
HAnimJoint509 = x3d.HAnimJoint()
HAnimJoint509.name = "vt3"
HAnimJoint509.DEF = "hanim_vt3"
HAnimJoint509.center = [0.0062,1.4583,-0.057]
HAnimJoint509.ulimit = [0,0,0]
HAnimJoint509.llimit = [0,0,0]
HAnimSegment510 = x3d.HAnimSegment()
HAnimSegment510.name = "t3"
HAnimSegment510.DEF = "hanim_t3"
Transform511 = x3d.Transform()
Transform511.translation = [0.0062,1.4583,-0.057]
Shape512 = x3d.Shape()
IndexedFaceSet513 = x3d.IndexedFaceSet()
IndexedFaceSet513.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet513.creaseAngle = 0.5
Coordinate514 = x3d.Coordinate()
Coordinate514.USE = "points"

IndexedFaceSet513.coord.append(Coordinate514)

Shape512.geometry = IndexedFaceSet513
Appearance515 = x3d.Appearance()
Material516 = x3d.Material()
Material516.USE = "SPINAL_COLOR"

Appearance515.material = Material516

Shape512.appearance = Appearance515

Transform511.children.append(Shape512)

HAnimSegment510.children.append(Transform511)

HAnimJoint509.children.append(HAnimSegment510)
HAnimJoint517 = x3d.HAnimJoint()
HAnimJoint517.name = "vt2"
HAnimJoint517.DEF = "hanim_vt2"
HAnimJoint517.center = [0.0063,1.4761,-0.0484]
HAnimJoint517.ulimit = [0,0,0]
HAnimJoint517.llimit = [0,0,0]
HAnimSegment518 = x3d.HAnimSegment()
HAnimSegment518.name = "t2"
HAnimSegment518.DEF = "hanim_t2"
Transform519 = x3d.Transform()
Transform519.translation = [0.0063,1.4761,-0.0484]
Shape520 = x3d.Shape()
IndexedFaceSet521 = x3d.IndexedFaceSet()
IndexedFaceSet521.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet521.creaseAngle = 0.5
Coordinate522 = x3d.Coordinate()
Coordinate522.USE = "points"

IndexedFaceSet521.coord.append(Coordinate522)

Shape520.geometry = IndexedFaceSet521
Appearance523 = x3d.Appearance()
Material524 = x3d.Material()
Material524.USE = "SPINAL_COLOR"

Appearance523.material = Material524

Shape520.appearance = Appearance523

Transform519.children.append(Shape520)

HAnimSegment518.children.append(Transform519)

HAnimJoint517.children.append(HAnimSegment518)
HAnimJoint525 = x3d.HAnimJoint()
HAnimJoint525.name = "vt1"
HAnimJoint525.DEF = "hanim_vt1"
HAnimJoint525.center = [0.0065,1.4951,-0.0387]
HAnimJoint525.ulimit = [0,0,0]
HAnimJoint525.llimit = [0,0,0]
HAnimSegment526 = x3d.HAnimSegment()
HAnimSegment526.name = "t1"
HAnimSegment526.DEF = "hanim_t1"
Transform527 = x3d.Transform()
Transform527.translation = [0.0065,1.4951,-0.0387]
Shape528 = x3d.Shape()
IndexedFaceSet529 = x3d.IndexedFaceSet()
IndexedFaceSet529.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet529.creaseAngle = 0.5
Coordinate530 = x3d.Coordinate()
Coordinate530.USE = "points"

IndexedFaceSet529.coord.append(Coordinate530)

Shape528.geometry = IndexedFaceSet529
Appearance531 = x3d.Appearance()
Material532 = x3d.Material()
Material532.USE = "REC_SPINAL_COLOR"

Appearance531.material = Material532

Shape528.appearance = Appearance531

Transform527.children.append(Shape528)

HAnimSegment526.children.append(Transform527)

HAnimJoint525.children.append(HAnimSegment526)
HAnimJoint533 = x3d.HAnimJoint()
HAnimJoint533.name = "l_shoulder"
HAnimJoint533.DEF = "hanim_l_shoulder"
HAnimJoint533.center = [0.2029,1.4376,-0.0387]
HAnimJoint533.ulimit = [0,0,0]
HAnimJoint533.llimit = [0,0,0]
HAnimSegment534 = x3d.HAnimSegment()
HAnimSegment534.name = "l_upperarm"
HAnimSegment534.DEF = "hanim_l_upperarm"
Transform535 = x3d.Transform()
Transform535.translation = [0.2029,1.4376,-0.0387]
Shape536 = x3d.Shape()
IndexedFaceSet537 = x3d.IndexedFaceSet()
IndexedFaceSet537.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet537.creaseAngle = 0.5
Coordinate538 = x3d.Coordinate()
Coordinate538.USE = "points"

IndexedFaceSet537.coord.append(Coordinate538)

Shape536.geometry = IndexedFaceSet537
Appearance539 = x3d.Appearance()
Material540 = x3d.Material()
Material540.USE = "MIN_COLOR"

Appearance539.material = Material540

Shape536.appearance = Appearance539

Transform535.children.append(Shape536)

HAnimSegment534.children.append(Transform535)
Transform541 = x3d.Transform()
Transform541.DEF = "l_upperarm_adjust"
Transform541.center = [0.182,1.22,-0.047]
Transform541.rotation = [1,0,0,0.119]
Transform541.translation = [0.2029,1.4376,-0.0387]

HAnimSegment534.children.append(Transform541)
HAnimSite542 = x3d.HAnimSite()
HAnimSite542.name = "l_humeral_lateral_epicn_pt"
HAnimSite542.DEF = "hanim_l_humeral_lateral_epicn_pt"
HAnimSite542.translation = [0.228,1.1482,-0.11]
Shape543 = x3d.Shape()
IndexedFaceSet544 = x3d.IndexedFaceSet()
IndexedFaceSet544.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet544.creaseAngle = 0.5
Coordinate545 = x3d.Coordinate()
Coordinate545.USE = "points"

IndexedFaceSet544.coord.append(Coordinate545)

Shape543.geometry = IndexedFaceSet544
Appearance546 = x3d.Appearance()
Material547 = x3d.Material()
Material547.USE = "SITE_COLOR"

Appearance546.material = Material547

Shape543.appearance = Appearance546

HAnimSite542.children.append(Shape543)

HAnimSegment534.children.append(HAnimSite542)

HAnimJoint533.children.append(HAnimSegment534)
HAnimJoint548 = x3d.HAnimJoint()
HAnimJoint548.name = "l_elbow"
HAnimJoint548.DEF = "hanim_l_elbow"
HAnimJoint548.center = [0.2014,1.1357,-0.0682]
HAnimJoint548.ulimit = [0,0,0]
HAnimJoint548.llimit = [0,0,0]
HAnimSegment549 = x3d.HAnimSegment()
HAnimSegment549.name = "l_forearm"
HAnimSegment549.DEF = "hanim_l_forearm"
Transform550 = x3d.Transform()
Transform550.translation = [0.2014,1.1357,-0.0682]
Shape551 = x3d.Shape()
IndexedFaceSet552 = x3d.IndexedFaceSet()
IndexedFaceSet552.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet552.creaseAngle = 0.5
Coordinate553 = x3d.Coordinate()
Coordinate553.USE = "points"

IndexedFaceSet552.coord.append(Coordinate553)

Shape551.geometry = IndexedFaceSet552
Appearance554 = x3d.Appearance()
Material555 = x3d.Material()
Material555.USE = "MIN_COLOR"

Appearance554.material = Material555

Shape551.appearance = Appearance554

Transform550.children.append(Shape551)

HAnimSegment549.children.append(Transform550)
Transform556 = x3d.Transform()
Transform556.DEF = "l_forearm_adjust"
Transform556.center = [0.198,0.961,-0.0405]
Transform556.rotation = [-1,0,0,0.1]
Transform556.translation = [0.2014,1.1357,-0.0682]

HAnimSegment549.children.append(Transform556)
HAnimSite557 = x3d.HAnimSite()
HAnimSite557.name = "l_radial_styloid_pt"
HAnimSite557.DEF = "hanim_l_radial_styloid_pt"
HAnimSite557.translation = [0.1901,0.8645,-0.0415]
Shape558 = x3d.Shape()
IndexedFaceSet559 = x3d.IndexedFaceSet()
IndexedFaceSet559.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet559.creaseAngle = 0.5
Coordinate560 = x3d.Coordinate()
Coordinate560.USE = "points"

IndexedFaceSet559.coord.append(Coordinate560)

Shape558.geometry = IndexedFaceSet559
Appearance561 = x3d.Appearance()
Material562 = x3d.Material()
Material562.USE = "SITE_COLOR"

Appearance561.material = Material562

Shape558.appearance = Appearance561

HAnimSite557.children.append(Shape558)

HAnimSegment549.children.append(HAnimSite557)
HAnimSite563 = x3d.HAnimSite()
HAnimSite563.name = "l_olecranon_pt"
HAnimSite563.DEF = "hanim_l_olecranon_pt"
HAnimSite563.translation = [-0.1962,1.1375,-0.1123]
Shape564 = x3d.Shape()
IndexedFaceSet565 = x3d.IndexedFaceSet()
IndexedFaceSet565.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet565.creaseAngle = 0.5
Coordinate566 = x3d.Coordinate()
Coordinate566.USE = "points"

IndexedFaceSet565.coord.append(Coordinate566)

Shape564.geometry = IndexedFaceSet565
Appearance567 = x3d.Appearance()
Material568 = x3d.Material()
Material568.USE = "SITE_COLOR"

Appearance567.material = Material568

Shape564.appearance = Appearance567

HAnimSite563.children.append(Shape564)

HAnimSegment549.children.append(HAnimSite563)
HAnimSite569 = x3d.HAnimSite()
HAnimSite569.name = "l_humeral_medial_epicn_pt"
HAnimSite569.DEF = "hanim_l_humeral_medial_epicn_pt"
HAnimSite569.translation = [0.1735,1.1272,-0.1113]
Shape570 = x3d.Shape()
IndexedFaceSet571 = x3d.IndexedFaceSet()
IndexedFaceSet571.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet571.creaseAngle = 0.5
Coordinate572 = x3d.Coordinate()
Coordinate572.USE = "points"

IndexedFaceSet571.coord.append(Coordinate572)

Shape570.geometry = IndexedFaceSet571
Appearance573 = x3d.Appearance()
Material574 = x3d.Material()
Material574.USE = "SITE_COLOR"

Appearance573.material = Material574

Shape570.appearance = Appearance573

HAnimSite569.children.append(Shape570)

HAnimSegment549.children.append(HAnimSite569)
HAnimSite575 = x3d.HAnimSite()
HAnimSite575.name = "l_radiale_pt"
HAnimSite575.DEF = "hanim_l_radiale_pt"
HAnimSite575.translation = [0.2182,1.1212,-0.1167]
Shape576 = x3d.Shape()
IndexedFaceSet577 = x3d.IndexedFaceSet()
IndexedFaceSet577.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet577.creaseAngle = 0.5
Coordinate578 = x3d.Coordinate()
Coordinate578.USE = "points"

IndexedFaceSet577.coord.append(Coordinate578)

Shape576.geometry = IndexedFaceSet577
Appearance579 = x3d.Appearance()
Material580 = x3d.Material()
Material580.USE = "SITE_COLOR"

Appearance579.material = Material580

Shape576.appearance = Appearance579

HAnimSite575.children.append(Shape576)

HAnimSegment549.children.append(HAnimSite575)

HAnimJoint548.children.append(HAnimSegment549)
HAnimJoint581 = x3d.HAnimJoint()
HAnimJoint581.name = "l_wrist"
HAnimJoint581.DEF = "hanim_l_wrist"
HAnimJoint581.center = [0.1984,0.8663,-0.0583]
HAnimJoint581.ulimit = [0,0,0]
HAnimJoint581.llimit = [0,0,0]
HAnimSegment582 = x3d.HAnimSegment()
HAnimSegment582.name = "l_hand"
HAnimSegment582.DEF = "hanim_l_hand"
Transform583 = x3d.Transform()
Transform583.translation = [0.1984,0.8663,-0.0583]
Shape584 = x3d.Shape()
IndexedFaceSet585 = x3d.IndexedFaceSet()
IndexedFaceSet585.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet585.creaseAngle = 0.5
Coordinate586 = x3d.Coordinate()
Coordinate586.USE = "points"

IndexedFaceSet585.coord.append(Coordinate586)

Shape584.geometry = IndexedFaceSet585
Appearance587 = x3d.Appearance()
Material588 = x3d.Material()
Material588.USE = "MIN_COLOR"

Appearance587.material = Material588

Shape584.appearance = Appearance587

Transform583.children.append(Shape584)

HAnimSegment582.children.append(Transform583)
Transform589 = x3d.Transform()
Transform589.DEF = "l_hand_adjust"
Transform589.center = [0.213,0.811,-0.0338]
Transform589.rotation = [-0.06361,-0.9967,0.04988,1.333]
Transform589.translation = [0.1984,0.8663,-0.0583]

HAnimSegment582.children.append(Transform589)
HAnimSite590 = x3d.HAnimSite()
HAnimSite590.name = "l_hand_tip"
HAnimSite590.DEF = "hanim_l_hand_tip"
HAnimSite590.translation = [0.208,0.6731,-0.0491]
Shape591 = x3d.Shape()
IndexedFaceSet592 = x3d.IndexedFaceSet()
IndexedFaceSet592.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet592.creaseAngle = 0.5
Coordinate593 = x3d.Coordinate()
Coordinate593.USE = "points"

IndexedFaceSet592.coord.append(Coordinate593)

Shape591.geometry = IndexedFaceSet592
Appearance594 = x3d.Appearance()
Material595 = x3d.Material()
Material595.USE = "SITE_COLOR"

Appearance594.material = Material595

Shape591.appearance = Appearance594

HAnimSite590.children.append(Shape591)

HAnimSegment582.children.append(HAnimSite590)
HAnimSite596 = x3d.HAnimSite()
HAnimSite596.name = "l_metacarpal_pha2_pt"
HAnimSite596.DEF = "hanim_l_metacarpal_pha2_pt"
HAnimSite596.translation = [0.2009,0.8139,-0.0237]
Shape597 = x3d.Shape()
IndexedFaceSet598 = x3d.IndexedFaceSet()
IndexedFaceSet598.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet598.creaseAngle = 0.5
Coordinate599 = x3d.Coordinate()
Coordinate599.USE = "points"

IndexedFaceSet598.coord.append(Coordinate599)

Shape597.geometry = IndexedFaceSet598
Appearance600 = x3d.Appearance()
Material601 = x3d.Material()
Material601.USE = "SITE_COLOR"

Appearance600.material = Material601

Shape597.appearance = Appearance600

HAnimSite596.children.append(Shape597)

HAnimSegment582.children.append(HAnimSite596)
HAnimSite602 = x3d.HAnimSite()
HAnimSite602.name = "l_dactylion_pt"
HAnimSite602.DEF = "hanim_l_dactylion_pt"
HAnimSite602.translation = [0.2056,0.6743,-0.0482]
Shape603 = x3d.Shape()
IndexedFaceSet604 = x3d.IndexedFaceSet()
IndexedFaceSet604.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet604.creaseAngle = 0.5
Coordinate605 = x3d.Coordinate()
Coordinate605.USE = "points"

IndexedFaceSet604.coord.append(Coordinate605)

Shape603.geometry = IndexedFaceSet604
Appearance606 = x3d.Appearance()
Material607 = x3d.Material()
Material607.USE = "SITE_COLOR"

Appearance606.material = Material607

Shape603.appearance = Appearance606

HAnimSite602.children.append(Shape603)

HAnimSegment582.children.append(HAnimSite602)
HAnimSite608 = x3d.HAnimSite()
HAnimSite608.name = "l_ulnar_styloid_pt"
HAnimSite608.DEF = "hanim_l_ulnar_styloid_pt"
HAnimSite608.translation = [-0.2142,0.8529,-0.0648]
Shape609 = x3d.Shape()
IndexedFaceSet610 = x3d.IndexedFaceSet()
IndexedFaceSet610.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet610.creaseAngle = 0.5
Coordinate611 = x3d.Coordinate()
Coordinate611.USE = "points"

IndexedFaceSet610.coord.append(Coordinate611)

Shape609.geometry = IndexedFaceSet610
Appearance612 = x3d.Appearance()
Material613 = x3d.Material()
Material613.USE = "SITE_COLOR"

Appearance612.material = Material613

Shape609.appearance = Appearance612

HAnimSite608.children.append(Shape609)

HAnimSegment582.children.append(HAnimSite608)
HAnimSite614 = x3d.HAnimSite()
HAnimSite614.name = "l_metacarpal_pha5_pt"
HAnimSite614.DEF = "hanim_l_metacarpal_pha5_pt"
HAnimSite614.translation = [0.1929,0.786,-0.1122]
Shape615 = x3d.Shape()
IndexedFaceSet616 = x3d.IndexedFaceSet()
IndexedFaceSet616.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet616.creaseAngle = 0.5
Coordinate617 = x3d.Coordinate()
Coordinate617.USE = "points"

IndexedFaceSet616.coord.append(Coordinate617)

Shape615.geometry = IndexedFaceSet616
Appearance618 = x3d.Appearance()
Material619 = x3d.Material()
Material619.USE = "SITE_COLOR"

Appearance618.material = Material619

Shape615.appearance = Appearance618

HAnimSite614.children.append(Shape615)

HAnimSegment582.children.append(HAnimSite614)

HAnimJoint581.children.append(HAnimSegment582)
HAnimJoint620 = x3d.HAnimJoint()
HAnimJoint620.name = "l_thumb1"
HAnimJoint620.DEF = "hanim_l_thumb1"
HAnimJoint620.center = [0.1924,0.8472,-0.0534]
HAnimJoint620.ulimit = [0,0,0]
HAnimJoint620.llimit = [0,0,0]
HAnimSegment621 = x3d.HAnimSegment()
HAnimSegment621.name = "l_thumb_metacarpal"
HAnimSegment621.DEF = "hanim_l_thumb_metacarpal"
Transform622 = x3d.Transform()
Transform622.translation = [0.1924,0.8472,-0.0534]
Shape623 = x3d.Shape()
IndexedFaceSet624 = x3d.IndexedFaceSet()
IndexedFaceSet624.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet624.creaseAngle = 0.5
Coordinate625 = x3d.Coordinate()
Coordinate625.USE = "points"

IndexedFaceSet624.coord.append(Coordinate625)

Shape623.geometry = IndexedFaceSet624
Appearance626 = x3d.Appearance()
Material627 = x3d.Material()
Material627.USE = "JOINT_COLOR"

Appearance626.material = Material627

Shape623.appearance = Appearance626

Transform622.children.append(Shape623)

HAnimSegment621.children.append(Transform622)

HAnimJoint620.children.append(HAnimSegment621)
HAnimJoint628 = x3d.HAnimJoint()
HAnimJoint628.name = "l_thumb2"
HAnimJoint628.DEF = "hanim_l_thumb2"
HAnimJoint628.center = [0.1951,0.8226,0.0246]
HAnimJoint628.ulimit = [0,0,0]
HAnimJoint628.llimit = [0,0,0]
HAnimSegment629 = x3d.HAnimSegment()
HAnimSegment629.name = "l_thumb_proximal"
HAnimSegment629.DEF = "hanim_l_thumb_proximal"
Transform630 = x3d.Transform()
Transform630.translation = [0.1951,0.8226,0.0246]
Shape631 = x3d.Shape()
IndexedFaceSet632 = x3d.IndexedFaceSet()
IndexedFaceSet632.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet632.creaseAngle = 0.5
Coordinate633 = x3d.Coordinate()
Coordinate633.USE = "points"

IndexedFaceSet632.coord.append(Coordinate633)

Shape631.geometry = IndexedFaceSet632
Appearance634 = x3d.Appearance()
Material635 = x3d.Material()
Material635.USE = "JOINT_COLOR"

Appearance634.material = Material635

Shape631.appearance = Appearance634

Transform630.children.append(Shape631)

HAnimSegment629.children.append(Transform630)

HAnimJoint628.children.append(HAnimSegment629)
HAnimJoint636 = x3d.HAnimJoint()
HAnimJoint636.name = "l_thumb3"
HAnimJoint636.DEF = "hanim_l_thumb3"
HAnimJoint636.center = [0.1955,0.8159,0.0464]
HAnimJoint636.ulimit = [0,0,0]
HAnimJoint636.llimit = [0,0,0]
HAnimSegment637 = x3d.HAnimSegment()
HAnimSegment637.name = "l_thumb_distal"
HAnimSegment637.DEF = "hanim_l_thumb_distal"
Transform638 = x3d.Transform()
Transform638.translation = [0.1955,0.8159,0.0464]
Shape639 = x3d.Shape()
IndexedFaceSet640 = x3d.IndexedFaceSet()
IndexedFaceSet640.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet640.creaseAngle = 0.5
Coordinate641 = x3d.Coordinate()
Coordinate641.USE = "points"

IndexedFaceSet640.coord.append(Coordinate641)

Shape639.geometry = IndexedFaceSet640
Appearance642 = x3d.Appearance()
Material643 = x3d.Material()
Material643.USE = "JOINT_COLOR"

Appearance642.material = Material643

Shape639.appearance = Appearance642

Transform638.children.append(Shape639)

HAnimSegment637.children.append(Transform638)
HAnimSite644 = x3d.HAnimSite()
HAnimSite644.name = "l_thumb_distal_tip"
HAnimSite644.DEF = "hanim_l_thumb_distal_tip"
HAnimSite644.translation = [0.1982,0.8061,0.0759]
Shape645 = x3d.Shape()
IndexedFaceSet646 = x3d.IndexedFaceSet()
IndexedFaceSet646.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet646.creaseAngle = 0.5
Coordinate647 = x3d.Coordinate()
Coordinate647.USE = "points"

IndexedFaceSet646.coord.append(Coordinate647)

Shape645.geometry = IndexedFaceSet646
Appearance648 = x3d.Appearance()
Material649 = x3d.Material()
Material649.USE = "HAND_FEET_COLOR"

Appearance648.material = Material649

Shape645.appearance = Appearance648

HAnimSite644.children.append(Shape645)

HAnimSegment637.children.append(HAnimSite644)

HAnimJoint636.children.append(HAnimSegment637)

HAnimJoint628.children.append(HAnimJoint636)

HAnimJoint620.children.append(HAnimJoint628)

HAnimJoint581.children.append(HAnimJoint620)
HAnimJoint650 = x3d.HAnimJoint()
HAnimJoint650.name = "l_index0"
HAnimJoint650.DEF = "hanim_l_index0"
HAnimJoint650.center = [0.1983,0.8024,-0.028]
HAnimJoint650.ulimit = [0,0,0]
HAnimJoint650.llimit = [0,0,0]
HAnimSegment651 = x3d.HAnimSegment()
HAnimSegment651.name = "l_index_metacarpal"
HAnimSegment651.DEF = "hanim_l_index_metacarpal"
Transform652 = x3d.Transform()
Transform652.translation = [0.1983,0.8024,-0.028]
Shape653 = x3d.Shape()
IndexedFaceSet654 = x3d.IndexedFaceSet()
IndexedFaceSet654.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet654.creaseAngle = 0.5
Coordinate655 = x3d.Coordinate()
Coordinate655.USE = "points"

IndexedFaceSet654.coord.append(Coordinate655)

Shape653.geometry = IndexedFaceSet654
Appearance656 = x3d.Appearance()
Material657 = x3d.Material()
Material657.USE = "JOINT_COLOR"

Appearance656.material = Material657

Shape653.appearance = Appearance656

Transform652.children.append(Shape653)

HAnimSegment651.children.append(Transform652)

HAnimJoint650.children.append(HAnimSegment651)
HAnimJoint658 = x3d.HAnimJoint()
HAnimJoint658.name = "l_index1"
HAnimJoint658.DEF = "hanim_l_index1"
HAnimJoint658.center = [0.1983,0.7815,-0.028]
HAnimJoint658.ulimit = [0,0,0]
HAnimJoint658.llimit = [0,0,0]
HAnimSegment659 = x3d.HAnimSegment()
HAnimSegment659.name = "l_index_proximal"
HAnimSegment659.DEF = "hanim_l_index_proximal"
Transform660 = x3d.Transform()
Transform660.translation = [0.1983,0.7815,-0.028]
Shape661 = x3d.Shape()
IndexedFaceSet662 = x3d.IndexedFaceSet()
IndexedFaceSet662.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet662.creaseAngle = 0.5
Coordinate663 = x3d.Coordinate()
Coordinate663.USE = "points"

IndexedFaceSet662.coord.append(Coordinate663)

Shape661.geometry = IndexedFaceSet662
Appearance664 = x3d.Appearance()
Material665 = x3d.Material()
Material665.USE = "JOINT_COLOR"

Appearance664.material = Material665

Shape661.appearance = Appearance664

Transform660.children.append(Shape661)

HAnimSegment659.children.append(Transform660)

HAnimJoint658.children.append(HAnimSegment659)
HAnimJoint666 = x3d.HAnimJoint()
HAnimJoint666.name = "l_index2"
HAnimJoint666.DEF = "hanim_l_index2"
HAnimJoint666.center = [0.2017,0.7363,-0.0248]
HAnimJoint666.ulimit = [0,0,0]
HAnimJoint666.llimit = [0,0,0]
HAnimSegment667 = x3d.HAnimSegment()
HAnimSegment667.name = "l_index_middle"
HAnimSegment667.DEF = "hanim_l_index_middle"
Transform668 = x3d.Transform()
Transform668.translation = [0.2017,0.7363,-0.0248]
Shape669 = x3d.Shape()
IndexedFaceSet670 = x3d.IndexedFaceSet()
IndexedFaceSet670.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet670.creaseAngle = 0.5
Coordinate671 = x3d.Coordinate()
Coordinate671.USE = "points"

IndexedFaceSet670.coord.append(Coordinate671)

Shape669.geometry = IndexedFaceSet670
Appearance672 = x3d.Appearance()
Material673 = x3d.Material()
Material673.USE = "JOINT_COLOR"

Appearance672.material = Material673

Shape669.appearance = Appearance672

Transform668.children.append(Shape669)

HAnimSegment667.children.append(Transform668)

HAnimJoint666.children.append(HAnimSegment667)
HAnimJoint674 = x3d.HAnimJoint()
HAnimJoint674.name = "l_index3"
HAnimJoint674.DEF = "hanim_l_index3"
HAnimJoint674.center = [0.2028,0.7139,-0.0236]
HAnimJoint674.ulimit = [0,0,0]
HAnimJoint674.llimit = [0,0,0]
HAnimSegment675 = x3d.HAnimSegment()
HAnimSegment675.name = "l_index_distal"
HAnimSegment675.DEF = "hanim_l_index_distal"
Transform676 = x3d.Transform()
Transform676.translation = [0.2028,0.7139,-0.0236]
Shape677 = x3d.Shape()
IndexedFaceSet678 = x3d.IndexedFaceSet()
IndexedFaceSet678.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet678.creaseAngle = 0.5
Coordinate679 = x3d.Coordinate()
Coordinate679.USE = "points"

IndexedFaceSet678.coord.append(Coordinate679)

Shape677.geometry = IndexedFaceSet678
Appearance680 = x3d.Appearance()
Material681 = x3d.Material()
Material681.USE = "JOINT_COLOR"

Appearance680.material = Material681

Shape677.appearance = Appearance680

Transform676.children.append(Shape677)

HAnimSegment675.children.append(Transform676)
HAnimSite682 = x3d.HAnimSite()
HAnimSite682.name = "l_index_distal_tip"
HAnimSite682.DEF = "hanim_l_index_distal_tip"
HAnimSite682.translation = [0.2089,0.6858,-0.0245]
Shape683 = x3d.Shape()
IndexedFaceSet684 = x3d.IndexedFaceSet()
IndexedFaceSet684.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet684.creaseAngle = 0.5
Coordinate685 = x3d.Coordinate()
Coordinate685.USE = "points"

IndexedFaceSet684.coord.append(Coordinate685)

Shape683.geometry = IndexedFaceSet684
Appearance686 = x3d.Appearance()
Material687 = x3d.Material()
Material687.USE = "HAND_FEET_COLOR"

Appearance686.material = Material687

Shape683.appearance = Appearance686

HAnimSite682.children.append(Shape683)

HAnimSegment675.children.append(HAnimSite682)

HAnimJoint674.children.append(HAnimSegment675)

HAnimJoint666.children.append(HAnimJoint674)

HAnimJoint658.children.append(HAnimJoint666)

HAnimJoint650.children.append(HAnimJoint658)

HAnimJoint581.children.append(HAnimJoint650)

HAnimJoint548.children.append(HAnimJoint581)

HAnimJoint533.children.append(HAnimJoint548)

HAnimJoint525.children.append(HAnimJoint533)
HAnimJoint688 = x3d.HAnimJoint()
HAnimJoint688.name = "r_shoulder"
HAnimJoint688.DEF = "hanim_r_shoulder"
HAnimJoint688.center = [-0.1907,1.4407,-0.0325]
HAnimJoint688.ulimit = [0,0,0]
HAnimJoint688.llimit = [0,0,0]
HAnimSegment689 = x3d.HAnimSegment()
HAnimSegment689.name = "r_upperarm"
HAnimSegment689.DEF = "hanim_r_upperarm"
Transform690 = x3d.Transform()
Transform690.translation = [-0.1907,1.4407,-0.0325]
Shape691 = x3d.Shape()
IndexedFaceSet692 = x3d.IndexedFaceSet()
IndexedFaceSet692.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet692.creaseAngle = 0.5
Coordinate693 = x3d.Coordinate()
Coordinate693.USE = "points"

IndexedFaceSet692.coord.append(Coordinate693)

Shape691.geometry = IndexedFaceSet692
Appearance694 = x3d.Appearance()
Material695 = x3d.Material()
Material695.USE = "MIN_COLOR"

Appearance694.material = Material695

Shape691.appearance = Appearance694

Transform690.children.append(Shape691)

HAnimSegment689.children.append(Transform690)
Transform696 = x3d.Transform()
Transform696.DEF = "r_upperarm_adjust"
Transform696.center = [-0.182,1.22,-0.047]
Transform696.rotation = [1,0,0,0.0836]
Transform696.translation = [-0.1907,1.4407,-0.0325]

HAnimSegment689.children.append(Transform696)
HAnimSite697 = x3d.HAnimSite()
HAnimSite697.name = "r_humeral_lateral_epicn_pt"
HAnimSite697.DEF = "hanim_r_humeral_lateral_epicn_pt"
HAnimSite697.translation = [-0.2224,1.1517,-0.1033]
Shape698 = x3d.Shape()
IndexedFaceSet699 = x3d.IndexedFaceSet()
IndexedFaceSet699.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet699.creaseAngle = 0.5
Coordinate700 = x3d.Coordinate()
Coordinate700.USE = "points"

IndexedFaceSet699.coord.append(Coordinate700)

Shape698.geometry = IndexedFaceSet699
Appearance701 = x3d.Appearance()
Material702 = x3d.Material()
Material702.USE = "SITE_COLOR"

Appearance701.material = Material702

Shape698.appearance = Appearance701

HAnimSite697.children.append(Shape698)

HAnimSegment689.children.append(HAnimSite697)

HAnimJoint688.children.append(HAnimSegment689)
HAnimJoint703 = x3d.HAnimJoint()
HAnimJoint703.name = "r_elbow"
HAnimJoint703.DEF = "hanim_r_elbow"
HAnimJoint703.center = [-0.1949,1.1388,-0.062]
HAnimJoint703.ulimit = [0,0,0]
HAnimJoint703.llimit = [0,0,0]
HAnimSegment704 = x3d.HAnimSegment()
HAnimSegment704.name = "r_forearm"
HAnimSegment704.DEF = "hanim_r_forearm"
Transform705 = x3d.Transform()
Transform705.translation = [-0.1949,1.1388,-0.062]
Shape706 = x3d.Shape()
IndexedFaceSet707 = x3d.IndexedFaceSet()
IndexedFaceSet707.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet707.creaseAngle = 0.5
Coordinate708 = x3d.Coordinate()
Coordinate708.USE = "points"

IndexedFaceSet707.coord.append(Coordinate708)

Shape706.geometry = IndexedFaceSet707
Appearance709 = x3d.Appearance()
Material710 = x3d.Material()
Material710.USE = "MIN_COLOR"

Appearance709.material = Material710

Shape706.appearance = Appearance709

Transform705.children.append(Shape706)

HAnimSegment704.children.append(Transform705)
Transform711 = x3d.Transform()
Transform711.DEF = "r_forearm_adjust"
Transform711.center = [-0.198,0.961,-0.0397]
Transform711.rotation = [-1,0,0,0.1254]
Transform711.translation = [-0.1949,1.1388,-0.062]

HAnimSegment704.children.append(Transform711)
HAnimSite712 = x3d.HAnimSite()
HAnimSite712.name = "r_radial_styloid_pt"
HAnimSite712.DEF = "hanim_r_radial_styloid_pt"
HAnimSite712.translation = [-0.1884,0.8676,-0.036]
Shape713 = x3d.Shape()
IndexedFaceSet714 = x3d.IndexedFaceSet()
IndexedFaceSet714.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet714.creaseAngle = 0.5
Coordinate715 = x3d.Coordinate()
Coordinate715.USE = "points"

IndexedFaceSet714.coord.append(Coordinate715)

Shape713.geometry = IndexedFaceSet714
Appearance716 = x3d.Appearance()
Material717 = x3d.Material()
Material717.USE = "SITE_COLOR"

Appearance716.material = Material717

Shape713.appearance = Appearance716

HAnimSite712.children.append(Shape713)

HAnimSegment704.children.append(HAnimSite712)
HAnimSite718 = x3d.HAnimSite()
HAnimSite718.name = "r_olecranon_pt"
HAnimSite718.DEF = "hanim_r_olecranon_pt"
HAnimSite718.translation = [-0.1907,1.1405,-0.1065]
Shape719 = x3d.Shape()
IndexedFaceSet720 = x3d.IndexedFaceSet()
IndexedFaceSet720.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet720.creaseAngle = 0.5
Coordinate721 = x3d.Coordinate()
Coordinate721.USE = "points"

IndexedFaceSet720.coord.append(Coordinate721)

Shape719.geometry = IndexedFaceSet720
Appearance722 = x3d.Appearance()
Material723 = x3d.Material()
Material723.USE = "SITE_COLOR"

Appearance722.material = Material723

Shape719.appearance = Appearance722

HAnimSite718.children.append(Shape719)

HAnimSegment704.children.append(HAnimSite718)
HAnimSite724 = x3d.HAnimSite()
HAnimSite724.name = "r_humeral_medial_epicn_pt"
HAnimSite724.DEF = "hanim_r_humeral_medial_epicn_pt"
HAnimSite724.translation = [-0.168,1.1298,-0.1062]
Shape725 = x3d.Shape()
IndexedFaceSet726 = x3d.IndexedFaceSet()
IndexedFaceSet726.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet726.creaseAngle = 0.5
Coordinate727 = x3d.Coordinate()
Coordinate727.USE = "points"

IndexedFaceSet726.coord.append(Coordinate727)

Shape725.geometry = IndexedFaceSet726
Appearance728 = x3d.Appearance()
Material729 = x3d.Material()
Material729.USE = "SITE_COLOR"

Appearance728.material = Material729

Shape725.appearance = Appearance728

HAnimSite724.children.append(Shape725)

HAnimSegment704.children.append(HAnimSite724)
HAnimSite730 = x3d.HAnimSite()
HAnimSite730.name = "r_radiale_pt"
HAnimSite730.DEF = "hanim_r_radiale_pt"
HAnimSite730.translation = [-0.213,1.1305,-0.1091]
Shape731 = x3d.Shape()
IndexedFaceSet732 = x3d.IndexedFaceSet()
IndexedFaceSet732.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet732.creaseAngle = 0.5
Coordinate733 = x3d.Coordinate()
Coordinate733.USE = "points"

IndexedFaceSet732.coord.append(Coordinate733)

Shape731.geometry = IndexedFaceSet732
Appearance734 = x3d.Appearance()
Material735 = x3d.Material()
Material735.USE = "SITE_COLOR"

Appearance734.material = Material735

Shape731.appearance = Appearance734

HAnimSite730.children.append(Shape731)

HAnimSegment704.children.append(HAnimSite730)

HAnimJoint703.children.append(HAnimSegment704)
HAnimJoint736 = x3d.HAnimJoint()
HAnimJoint736.name = "r_wrist"
HAnimJoint736.DEF = "hanim_r_wrist"
HAnimJoint736.center = [-0.1959,0.8694,-0.0521]
HAnimJoint736.ulimit = [0,0,0]
HAnimJoint736.llimit = [0,0,0]
HAnimSegment737 = x3d.HAnimSegment()
HAnimSegment737.name = "r_hand"
HAnimSegment737.DEF = "hanim_r_hand"
Transform738 = x3d.Transform()
Transform738.translation = [-0.1959,0.8694,-0.0521]
Shape739 = x3d.Shape()
IndexedFaceSet740 = x3d.IndexedFaceSet()
IndexedFaceSet740.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet740.creaseAngle = 0.5
Coordinate741 = x3d.Coordinate()
Coordinate741.USE = "points"

IndexedFaceSet740.coord.append(Coordinate741)

Shape739.geometry = IndexedFaceSet740
Appearance742 = x3d.Appearance()
Material743 = x3d.Material()
Material743.USE = "MIN_COLOR"

Appearance742.material = Material743

Shape739.appearance = Appearance742

Transform738.children.append(Shape739)

HAnimSegment737.children.append(Transform738)
Transform744 = x3d.Transform()
Transform744.DEF = "r_hand_adjust"
Transform744.center = [-0.217,0.811,-0.0338]
Transform744.rotation = [-0.09024,0.994,-0.0624,1.216]

HAnimSegment737.children.append(Transform744)
HAnimSite745 = x3d.HAnimSite()
HAnimSite745.name = "r_hand_tip"
HAnimSite745.DEF = "hanim_r_hand_tip"
HAnimSite745.translation = [-0.1969,0.6758,-0.0427]
Shape746 = x3d.Shape()
IndexedFaceSet747 = x3d.IndexedFaceSet()
IndexedFaceSet747.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet747.creaseAngle = 0.5
Coordinate748 = x3d.Coordinate()
Coordinate748.USE = "points"

IndexedFaceSet747.coord.append(Coordinate748)

Shape746.geometry = IndexedFaceSet747
Appearance749 = x3d.Appearance()
Material750 = x3d.Material()
Material750.USE = "SITE_COLOR"

Appearance749.material = Material750

Shape746.appearance = Appearance749

HAnimSite745.children.append(Shape746)

HAnimSegment737.children.append(HAnimSite745)
HAnimSite751 = x3d.HAnimSite()
HAnimSite751.name = "r_metacarpal_pha2_pt"
HAnimSite751.DEF = "hanim_r_metacarpal_pha2_pt"
HAnimSite751.translation = [-0.1977,0.8169,-0.0177]
Shape752 = x3d.Shape()
IndexedFaceSet753 = x3d.IndexedFaceSet()
IndexedFaceSet753.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet753.creaseAngle = 0.5
Coordinate754 = x3d.Coordinate()
Coordinate754.USE = "points"

IndexedFaceSet753.coord.append(Coordinate754)

Shape752.geometry = IndexedFaceSet753
Appearance755 = x3d.Appearance()
Material756 = x3d.Material()
Material756.USE = "SITE_COLOR"

Appearance755.material = Material756

Shape752.appearance = Appearance755

HAnimSite751.children.append(Shape752)

HAnimSegment737.children.append(HAnimSite751)
HAnimSite757 = x3d.HAnimSite()
HAnimSite757.name = "r_dactylion_pt"
HAnimSite757.DEF = "hanim_r_dactylion_pt"
HAnimSite757.translation = [-0.1941,0.6772,-0.0423]
Shape758 = x3d.Shape()
IndexedFaceSet759 = x3d.IndexedFaceSet()
IndexedFaceSet759.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet759.creaseAngle = 0.5
Coordinate760 = x3d.Coordinate()
Coordinate760.USE = "points"

IndexedFaceSet759.coord.append(Coordinate760)

Shape758.geometry = IndexedFaceSet759
Appearance761 = x3d.Appearance()
Material762 = x3d.Material()
Material762.USE = "SITE_COLOR"

Appearance761.material = Material762

Shape758.appearance = Appearance761

HAnimSite757.children.append(Shape758)

HAnimSegment737.children.append(HAnimSite757)
HAnimSite763 = x3d.HAnimSite()
HAnimSite763.name = "r_ulnar_styloid_pt"
HAnimSite763.DEF = "hanim_r_ulnar_styloid_pt"
HAnimSite763.translation = [-0.2117,0.8562,-0.0584]
Shape764 = x3d.Shape()
IndexedFaceSet765 = x3d.IndexedFaceSet()
IndexedFaceSet765.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet765.creaseAngle = 0.5
Coordinate766 = x3d.Coordinate()
Coordinate766.USE = "points"

IndexedFaceSet765.coord.append(Coordinate766)

Shape764.geometry = IndexedFaceSet765
Appearance767 = x3d.Appearance()
Material768 = x3d.Material()
Material768.USE = "SITE_COLOR"

Appearance767.material = Material768

Shape764.appearance = Appearance767

HAnimSite763.children.append(Shape764)

HAnimSegment737.children.append(HAnimSite763)
HAnimSite769 = x3d.HAnimSite()
HAnimSite769.name = "r_metacarpal_pha5_pt"
HAnimSite769.DEF = "hanim_r_metacarpal_pha5_pt"
HAnimSite769.translation = [-0.1929,0.789,-0.1064]
Shape770 = x3d.Shape()
IndexedFaceSet771 = x3d.IndexedFaceSet()
IndexedFaceSet771.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet771.creaseAngle = 0.5
Coordinate772 = x3d.Coordinate()
Coordinate772.USE = "points"

IndexedFaceSet771.coord.append(Coordinate772)

Shape770.geometry = IndexedFaceSet771
Appearance773 = x3d.Appearance()
Material774 = x3d.Material()
Material774.USE = "SITE_COLOR"

Appearance773.material = Material774

Shape770.appearance = Appearance773

HAnimSite769.children.append(Shape770)

HAnimSegment737.children.append(HAnimSite769)

HAnimJoint736.children.append(HAnimSegment737)

HAnimJoint703.children.append(HAnimJoint736)

HAnimJoint688.children.append(HAnimJoint703)

HAnimJoint525.children.append(HAnimJoint688)
HAnimJoint775 = x3d.HAnimJoint()
HAnimJoint775.name = "vc7"
HAnimJoint775.DEF = "hanim_vc7"
HAnimJoint775.center = [0.0066,1.5132,-0.0301]
HAnimJoint775.ulimit = [0,0,0]
HAnimJoint775.llimit = [0,0,0]
HAnimSegment776 = x3d.HAnimSegment()
HAnimSegment776.name = "c7"
HAnimSegment776.DEF = "hanim_c7"
Transform777 = x3d.Transform()
Transform777.translation = [0.0066,1.5132,-0.0301]
Shape778 = x3d.Shape()
IndexedFaceSet779 = x3d.IndexedFaceSet()
IndexedFaceSet779.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet779.creaseAngle = 0.5
Coordinate780 = x3d.Coordinate()
Coordinate780.USE = "points"

IndexedFaceSet779.coord.append(Coordinate780)

Shape778.geometry = IndexedFaceSet779
Appearance781 = x3d.Appearance()
Material782 = x3d.Material()
Material782.USE = "SPINAL_COLOR"

Appearance781.material = Material782

Shape778.appearance = Appearance781

Transform777.children.append(Shape778)

HAnimSegment776.children.append(Transform777)

HAnimJoint775.children.append(HAnimSegment776)
HAnimJoint783 = x3d.HAnimJoint()
HAnimJoint783.name = "vc6"
HAnimJoint783.DEF = "hanim_vc6"
HAnimJoint783.center = [0.0066,1.5357,-0.0143]
HAnimJoint783.ulimit = [0,0,0]
HAnimJoint783.llimit = [0,0,0]
HAnimSegment784 = x3d.HAnimSegment()
HAnimSegment784.name = "c6"
HAnimSegment784.DEF = "hanim_c6"
Transform785 = x3d.Transform()
Transform785.translation = [0.0066,1.5357,-0.0143]
Shape786 = x3d.Shape()
IndexedFaceSet787 = x3d.IndexedFaceSet()
IndexedFaceSet787.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet787.creaseAngle = 0.5
Coordinate788 = x3d.Coordinate()
Coordinate788.USE = "points"

IndexedFaceSet787.coord.append(Coordinate788)

Shape786.geometry = IndexedFaceSet787
Appearance789 = x3d.Appearance()
Material790 = x3d.Material()
Material790.USE = "SPINAL_COLOR"

Appearance789.material = Material790

Shape786.appearance = Appearance789

Transform785.children.append(Shape786)

HAnimSegment784.children.append(Transform785)

HAnimJoint783.children.append(HAnimSegment784)
HAnimJoint791 = x3d.HAnimJoint()
HAnimJoint791.name = "vc5"
HAnimJoint791.DEF = "hanim_vc5"
HAnimJoint791.center = [0.0066,1.552,-0.0082]
HAnimJoint791.ulimit = [0,0,0]
HAnimJoint791.llimit = [0,0,0]
HAnimSegment792 = x3d.HAnimSegment()
HAnimSegment792.name = "c5"
HAnimSegment792.DEF = "hanim_c5"
Transform793 = x3d.Transform()
Transform793.translation = [0.0066,1.552,-0.0082]
Shape794 = x3d.Shape()
IndexedFaceSet795 = x3d.IndexedFaceSet()
IndexedFaceSet795.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet795.creaseAngle = 0.5
Coordinate796 = x3d.Coordinate()
Coordinate796.USE = "points"

IndexedFaceSet795.coord.append(Coordinate796)

Shape794.geometry = IndexedFaceSet795
Appearance797 = x3d.Appearance()
Material798 = x3d.Material()
Material798.USE = "SPINAL_COLOR"

Appearance797.material = Material798

Shape794.appearance = Appearance797

Transform793.children.append(Shape794)

HAnimSegment792.children.append(Transform793)

HAnimJoint791.children.append(HAnimSegment792)
HAnimJoint799 = x3d.HAnimJoint()
HAnimJoint799.name = "vc4"
HAnimJoint799.DEF = "hanim_vc4"
HAnimJoint799.center = [0.0066,1.5662,-0.0084]
HAnimJoint799.ulimit = [0,0,0]
HAnimJoint799.llimit = [0,0,0]
HAnimSegment800 = x3d.HAnimSegment()
HAnimSegment800.name = "c4"
HAnimSegment800.DEF = "hanim_c4"
Transform801 = x3d.Transform()
Transform801.translation = [0.0066,1.5662,-0.0084]
Shape802 = x3d.Shape()
IndexedFaceSet803 = x3d.IndexedFaceSet()
IndexedFaceSet803.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet803.creaseAngle = 0.5
Coordinate804 = x3d.Coordinate()
Coordinate804.USE = "points"

IndexedFaceSet803.coord.append(Coordinate804)

Shape802.geometry = IndexedFaceSet803
Appearance805 = x3d.Appearance()
Material806 = x3d.Material()
Material806.USE = "SPINAL_COLOR"

Appearance805.material = Material806

Shape802.appearance = Appearance805

Transform801.children.append(Shape802)

HAnimSegment800.children.append(Transform801)

HAnimJoint799.children.append(HAnimSegment800)
HAnimJoint807 = x3d.HAnimJoint()
HAnimJoint807.name = "vc3"
HAnimJoint807.DEF = "hanim_vc3"
HAnimJoint807.center = [0.0066,1.58,-0.0103]
HAnimJoint807.ulimit = [0,0,0]
HAnimJoint807.llimit = [0,0,0]
HAnimSegment808 = x3d.HAnimSegment()
HAnimSegment808.name = "c3"
HAnimSegment808.DEF = "hanim_c3"
Transform809 = x3d.Transform()
Transform809.translation = [0.0066,1.58,-0.0103]
Shape810 = x3d.Shape()
IndexedFaceSet811 = x3d.IndexedFaceSet()
IndexedFaceSet811.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet811.creaseAngle = 0.5
Coordinate812 = x3d.Coordinate()
Coordinate812.USE = "points"

IndexedFaceSet811.coord.append(Coordinate812)

Shape810.geometry = IndexedFaceSet811
Appearance813 = x3d.Appearance()
Material814 = x3d.Material()
Material814.USE = "SPINAL_COLOR"

Appearance813.material = Material814

Shape810.appearance = Appearance813

Transform809.children.append(Shape810)

HAnimSegment808.children.append(Transform809)

HAnimJoint807.children.append(HAnimSegment808)
HAnimJoint815 = x3d.HAnimJoint()
HAnimJoint815.name = "vc2"
HAnimJoint815.DEF = "hanim_vc2"
HAnimJoint815.center = [0.0066,1.5928,-0.0103]
HAnimJoint815.ulimit = [0,0,0]
HAnimJoint815.llimit = [0,0,0]
HAnimSegment816 = x3d.HAnimSegment()
HAnimSegment816.name = "c2"
HAnimSegment816.DEF = "hanim_c2"
Transform817 = x3d.Transform()
Transform817.translation = [0.0066,1.5928,-0.0103]
Shape818 = x3d.Shape()
IndexedFaceSet819 = x3d.IndexedFaceSet()
IndexedFaceSet819.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet819.creaseAngle = 0.5
Coordinate820 = x3d.Coordinate()
Coordinate820.USE = "points"

IndexedFaceSet819.coord.append(Coordinate820)

Shape818.geometry = IndexedFaceSet819
Appearance821 = x3d.Appearance()
Material822 = x3d.Material()
Material822.USE = "REC_SPINAL_COLOR"

Appearance821.material = Material822

Shape818.appearance = Appearance821

Transform817.children.append(Shape818)

HAnimSegment816.children.append(Transform817)

HAnimJoint815.children.append(HAnimSegment816)
HAnimJoint823 = x3d.HAnimJoint()
HAnimJoint823.name = "vc1"
HAnimJoint823.DEF = "hanim_vc1"
HAnimJoint823.center = [0.0066,1.6144,-0.0034]
HAnimJoint823.ulimit = [0,0,0]
HAnimJoint823.llimit = [0,0,0]
HAnimSegment824 = x3d.HAnimSegment()
HAnimSegment824.name = "c1"
HAnimSegment824.DEF = "hanim_c1"
Transform825 = x3d.Transform()
Transform825.translation = [0.0066,1.6144,-0.0034]
Shape826 = x3d.Shape()
IndexedFaceSet827 = x3d.IndexedFaceSet()
IndexedFaceSet827.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet827.creaseAngle = 0.5
Coordinate828 = x3d.Coordinate()
Coordinate828.USE = "points"

IndexedFaceSet827.coord.append(Coordinate828)

Shape826.geometry = IndexedFaceSet827
Appearance829 = x3d.Appearance()
Material830 = x3d.Material()
Material830.USE = "SPINAL_COLOR"

Appearance829.material = Material830

Shape826.appearance = Appearance829

Transform825.children.append(Shape826)

HAnimSegment824.children.append(Transform825)

HAnimJoint823.children.append(HAnimSegment824)
HAnimJoint831 = x3d.HAnimJoint()
HAnimJoint831.name = "skullbase"
HAnimJoint831.DEF = "hanim_skullbase"
HAnimJoint831.center = [0.0044,1.6209,0.0236]
HAnimJoint831.ulimit = [0,0,0]
HAnimJoint831.llimit = [0,0,0]
HAnimSegment832 = x3d.HAnimSegment()
HAnimSegment832.name = "skull"
HAnimSegment832.DEF = "hanim_skull"
Transform833 = x3d.Transform()
Transform833.translation = [0.0044,1.6209,0.0236]
Shape834 = x3d.Shape()
IndexedFaceSet835 = x3d.IndexedFaceSet()
IndexedFaceSet835.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet835.creaseAngle = 0.5
Coordinate836 = x3d.Coordinate()
Coordinate836.USE = "points"

IndexedFaceSet835.coord.append(Coordinate836)

Shape834.geometry = IndexedFaceSet835
Appearance837 = x3d.Appearance()
Material838 = x3d.Material()
Material838.USE = "MIN_COLOR"

Appearance837.material = Material838

Shape834.appearance = Appearance837

Transform833.children.append(Shape834)

HAnimSegment832.children.append(Transform833)
HAnimSite839 = x3d.HAnimSite()
HAnimSite839.name = "skull_tip"
HAnimSite839.DEF = "hanim_skull_tip"
HAnimSite839.translation = [0.005,1.7504,0.0055]
Shape840 = x3d.Shape()
IndexedFaceSet841 = x3d.IndexedFaceSet()
IndexedFaceSet841.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet841.creaseAngle = 0.5
Coordinate842 = x3d.Coordinate()
Coordinate842.USE = "points"

IndexedFaceSet841.coord.append(Coordinate842)

Shape840.geometry = IndexedFaceSet841
Appearance843 = x3d.Appearance()
Material844 = x3d.Material()
Material844.USE = "SITE_COLOR"

Appearance843.material = Material844

Shape840.appearance = Appearance843

HAnimSite839.children.append(Shape840)

HAnimSegment832.children.append(HAnimSite839)
HAnimSite845 = x3d.HAnimSite()
HAnimSite845.name = "sellion_pt"
HAnimSite845.DEF = "hanim_sellion_pt"
HAnimSite845.translation = [0.0058,1.6316,0.0852]
Shape846 = x3d.Shape()
IndexedFaceSet847 = x3d.IndexedFaceSet()
IndexedFaceSet847.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet847.creaseAngle = 0.5
Coordinate848 = x3d.Coordinate()
Coordinate848.USE = "points"

IndexedFaceSet847.coord.append(Coordinate848)

Shape846.geometry = IndexedFaceSet847
Appearance849 = x3d.Appearance()
Material850 = x3d.Material()
Material850.USE = "SITE_COLOR"

Appearance849.material = Material850

Shape846.appearance = Appearance849

HAnimSite845.children.append(Shape846)

HAnimSegment832.children.append(HAnimSite845)
HAnimSite851 = x3d.HAnimSite()
HAnimSite851.name = "r_infraorbitale_pt"
HAnimSite851.DEF = "hanim_r_infraorbitale_pt"
HAnimSite851.translation = [-0.0237,1.6171,0.0752]
Shape852 = x3d.Shape()
IndexedFaceSet853 = x3d.IndexedFaceSet()
IndexedFaceSet853.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet853.creaseAngle = 0.5
Coordinate854 = x3d.Coordinate()
Coordinate854.USE = "points"

IndexedFaceSet853.coord.append(Coordinate854)

Shape852.geometry = IndexedFaceSet853
Appearance855 = x3d.Appearance()
Material856 = x3d.Material()
Material856.USE = "SITE_COLOR"

Appearance855.material = Material856

Shape852.appearance = Appearance855

HAnimSite851.children.append(Shape852)

HAnimSegment832.children.append(HAnimSite851)
HAnimSite857 = x3d.HAnimSite()
HAnimSite857.name = "l_infraorbitale_pt"
HAnimSite857.DEF = "hanim_l_infraorbitale_pt"
HAnimSite857.translation = [0.0341,1.6171,0.0752]
Shape858 = x3d.Shape()
IndexedFaceSet859 = x3d.IndexedFaceSet()
IndexedFaceSet859.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet859.creaseAngle = 0.5
Coordinate860 = x3d.Coordinate()
Coordinate860.USE = "points"

IndexedFaceSet859.coord.append(Coordinate860)

Shape858.geometry = IndexedFaceSet859
Appearance861 = x3d.Appearance()
Material862 = x3d.Material()
Material862.USE = "SITE_COLOR"

Appearance861.material = Material862

Shape858.appearance = Appearance861

HAnimSite857.children.append(Shape858)

HAnimSegment832.children.append(HAnimSite857)
HAnimSite863 = x3d.HAnimSite()
HAnimSite863.name = "supramenton_pt"
HAnimSite863.DEF = "hanim_supramenton_pt"
HAnimSite863.translation = [0.0061,1.541,0.0805]
Shape864 = x3d.Shape()
IndexedFaceSet865 = x3d.IndexedFaceSet()
IndexedFaceSet865.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet865.creaseAngle = 0.5
Coordinate866 = x3d.Coordinate()
Coordinate866.USE = "points"

IndexedFaceSet865.coord.append(Coordinate866)

Shape864.geometry = IndexedFaceSet865
Appearance867 = x3d.Appearance()
Material868 = x3d.Material()
Material868.USE = "SITE_COLOR"

Appearance867.material = Material868

Shape864.appearance = Appearance867

HAnimSite863.children.append(Shape864)

HAnimSegment832.children.append(HAnimSite863)
HAnimSite869 = x3d.HAnimSite()
HAnimSite869.name = "r_tragion_pt"
HAnimSite869.DEF = "hanim_r_tragion_pt"
HAnimSite869.translation = [-0.0646,1.6347,0.0302]
Shape870 = x3d.Shape()
IndexedFaceSet871 = x3d.IndexedFaceSet()
IndexedFaceSet871.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet871.creaseAngle = 0.5
Coordinate872 = x3d.Coordinate()
Coordinate872.USE = "points"

IndexedFaceSet871.coord.append(Coordinate872)

Shape870.geometry = IndexedFaceSet871
Appearance873 = x3d.Appearance()
Material874 = x3d.Material()
Material874.USE = "SITE_COLOR"

Appearance873.material = Material874

Shape870.appearance = Appearance873

HAnimSite869.children.append(Shape870)

HAnimSegment832.children.append(HAnimSite869)
HAnimSite875 = x3d.HAnimSite()
HAnimSite875.name = "r_gonion_pt"
HAnimSite875.DEF = "hanim_r_gonion_pt"
HAnimSite875.translation = [-0.052,1.5529,0.0347]
Shape876 = x3d.Shape()
IndexedFaceSet877 = x3d.IndexedFaceSet()
IndexedFaceSet877.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet877.creaseAngle = 0.5
Coordinate878 = x3d.Coordinate()
Coordinate878.USE = "points"

IndexedFaceSet877.coord.append(Coordinate878)

Shape876.geometry = IndexedFaceSet877
Appearance879 = x3d.Appearance()
Material880 = x3d.Material()
Material880.USE = "SITE_COLOR"

Appearance879.material = Material880

Shape876.appearance = Appearance879

HAnimSite875.children.append(Shape876)

HAnimSegment832.children.append(HAnimSite875)
HAnimSite881 = x3d.HAnimSite()
HAnimSite881.name = "l_tragion_pt"
HAnimSite881.DEF = "hanim_l_tragion_pt"
HAnimSite881.translation = [0.0739,1.6348,0.0282]
Shape882 = x3d.Shape()
IndexedFaceSet883 = x3d.IndexedFaceSet()
IndexedFaceSet883.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet883.creaseAngle = 0.5
Coordinate884 = x3d.Coordinate()
Coordinate884.USE = "points"

IndexedFaceSet883.coord.append(Coordinate884)

Shape882.geometry = IndexedFaceSet883
Appearance885 = x3d.Appearance()
Material886 = x3d.Material()
Material886.USE = "SITE_COLOR"

Appearance885.material = Material886

Shape882.appearance = Appearance885

HAnimSite881.children.append(Shape882)

HAnimSegment832.children.append(HAnimSite881)
HAnimSite887 = x3d.HAnimSite()
HAnimSite887.name = "l_gonion_pt"
HAnimSite887.DEF = "hanim_l_gonion_pt"
HAnimSite887.translation = [0.0631,1.553,0.033]
Shape888 = x3d.Shape()
IndexedFaceSet889 = x3d.IndexedFaceSet()
IndexedFaceSet889.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet889.creaseAngle = 0.5
Coordinate890 = x3d.Coordinate()
Coordinate890.USE = "points"

IndexedFaceSet889.coord.append(Coordinate890)

Shape888.geometry = IndexedFaceSet889
Appearance891 = x3d.Appearance()
Material892 = x3d.Material()
Material892.USE = "SITE_COLOR"

Appearance891.material = Material892

Shape888.appearance = Appearance891

HAnimSite887.children.append(Shape888)

HAnimSegment832.children.append(HAnimSite887)
HAnimSite893 = x3d.HAnimSite()
HAnimSite893.name = "nuchale_pt"
HAnimSite893.DEF = "hanim_nuchale_pt"
HAnimSite893.translation = [0.0039,1.5972,-0.0796]
Shape894 = x3d.Shape()
IndexedFaceSet895 = x3d.IndexedFaceSet()
IndexedFaceSet895.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet895.creaseAngle = 0.5
Coordinate896 = x3d.Coordinate()
Coordinate896.USE = "points"

IndexedFaceSet895.coord.append(Coordinate896)

Shape894.geometry = IndexedFaceSet895
Appearance897 = x3d.Appearance()
Material898 = x3d.Material()
Material898.USE = "SITE_COLOR"

Appearance897.material = Material898

Shape894.appearance = Appearance897

HAnimSite893.children.append(Shape894)

HAnimSegment832.children.append(HAnimSite893)

HAnimJoint831.children.append(HAnimSegment832)

HAnimJoint823.children.append(HAnimJoint831)

HAnimJoint815.children.append(HAnimJoint823)

HAnimJoint807.children.append(HAnimJoint815)

HAnimJoint799.children.append(HAnimJoint807)

HAnimJoint791.children.append(HAnimJoint799)

HAnimJoint783.children.append(HAnimJoint791)

HAnimJoint775.children.append(HAnimJoint783)

HAnimJoint525.children.append(HAnimJoint775)

HAnimJoint517.children.append(HAnimJoint525)

HAnimJoint509.children.append(HAnimJoint517)

HAnimJoint501.children.append(HAnimJoint509)

HAnimJoint493.children.append(HAnimJoint501)

HAnimJoint485.children.append(HAnimJoint493)

HAnimJoint477.children.append(HAnimJoint485)

HAnimJoint469.children.append(HAnimJoint477)

HAnimJoint461.children.append(HAnimJoint469)

HAnimJoint453.children.append(HAnimJoint461)

HAnimJoint445.children.append(HAnimJoint453)

HAnimJoint437.children.append(HAnimJoint445)

HAnimJoint429.children.append(HAnimJoint437)

HAnimJoint421.children.append(HAnimJoint429)

HAnimJoint413.children.append(HAnimJoint421)

HAnimJoint405.children.append(HAnimJoint413)

HAnimJoint397.children.append(HAnimJoint405)

HAnimJoint102.children.append(HAnimJoint397)

HAnimHumanoid94.skeleton.append(HAnimJoint102)
HAnimSite899 = x3d.HAnimSite()
HAnimSite899.name = "DiamondManLOA_2_view"
HAnimSite899.DEF = "hanim_DiamondManLOA_2_view"
Viewpoint900 = x3d.Viewpoint()
Viewpoint900.DEF = "FrontView"
Viewpoint900.description = "Front View"
Viewpoint900.position = [0.35,0.854,2.57665]

HAnimSite899.children.append(Viewpoint900)
Viewpoint901 = x3d.Viewpoint()
Viewpoint901.DEF = "SideView"
Viewpoint901.description = "Side View"
Viewpoint901.orientation = [0,1,0,1.57079]
Viewpoint901.position = [2,0.854,0]

HAnimSite899.children.append(Viewpoint901)
Viewpoint902 = x3d.Viewpoint()
Viewpoint902.DEF = "TopView"
Viewpoint902.description = "Top View"
Viewpoint902.orientation = [1,0,0,-1.57079]
Viewpoint902.position = [0,3.4495,0]

HAnimSite899.children.append(Viewpoint902)
Viewpoint903 = x3d.Viewpoint()
Viewpoint903.DEF = "RootView"
Viewpoint903.description = "Humanoid Root View"
Viewpoint903.position = [0,0.824,0.277]

HAnimSite899.children.append(Viewpoint903)
Viewpoint904 = x3d.Viewpoint()
Viewpoint904.DEF = "InclinedView"
Viewpoint904.description = "Inclined View"
Viewpoint904.orientation = [-0.113,0.993,0.0347,0.671]
Viewpoint904.position = [1.62,1.05,2.06]

HAnimSite899.children.append(Viewpoint904)

HAnimHumanoid94.viewpoints.append(HAnimSite899)
HAnimJoint905 = x3d.HAnimJoint()
HAnimJoint905.USE = "hanim_HumanoidRoot"

HAnimHumanoid94.joints.append(HAnimJoint905)
HAnimJoint906 = x3d.HAnimJoint()
HAnimJoint906.USE = "hanim_sacroiliac"

HAnimHumanoid94.joints.append(HAnimJoint906)
HAnimJoint907 = x3d.HAnimJoint()
HAnimJoint907.USE = "hanim_vl1"

HAnimHumanoid94.joints.append(HAnimJoint907)
HAnimJoint908 = x3d.HAnimJoint()
HAnimJoint908.USE = "hanim_vc4"

HAnimHumanoid94.joints.append(HAnimJoint908)
HAnimJoint909 = x3d.HAnimJoint()
HAnimJoint909.USE = "hanim_skullbase"

HAnimHumanoid94.joints.append(HAnimJoint909)
HAnimJoint910 = x3d.HAnimJoint()
HAnimJoint910.USE = "hanim_vl5"

HAnimHumanoid94.joints.append(HAnimJoint910)
HAnimJoint911 = x3d.HAnimJoint()
HAnimJoint911.USE = "hanim_vl4"

HAnimHumanoid94.joints.append(HAnimJoint911)
HAnimJoint912 = x3d.HAnimJoint()
HAnimJoint912.USE = "hanim_vl3"

HAnimHumanoid94.joints.append(HAnimJoint912)
HAnimJoint913 = x3d.HAnimJoint()
HAnimJoint913.USE = "hanim_vl2"

HAnimHumanoid94.joints.append(HAnimJoint913)
HAnimJoint914 = x3d.HAnimJoint()
HAnimJoint914.USE = "hanim_vt12"

HAnimHumanoid94.joints.append(HAnimJoint914)
HAnimJoint915 = x3d.HAnimJoint()
HAnimJoint915.USE = "hanim_vt11"

HAnimHumanoid94.joints.append(HAnimJoint915)
HAnimJoint916 = x3d.HAnimJoint()
HAnimJoint916.USE = "hanim_vt10"

HAnimHumanoid94.joints.append(HAnimJoint916)
HAnimJoint917 = x3d.HAnimJoint()
HAnimJoint917.USE = "hanim_vt9"

HAnimHumanoid94.joints.append(HAnimJoint917)
HAnimJoint918 = x3d.HAnimJoint()
HAnimJoint918.USE = "hanim_vt8"

HAnimHumanoid94.joints.append(HAnimJoint918)
HAnimJoint919 = x3d.HAnimJoint()
HAnimJoint919.USE = "hanim_vt7"

HAnimHumanoid94.joints.append(HAnimJoint919)
HAnimJoint920 = x3d.HAnimJoint()
HAnimJoint920.USE = "hanim_vt6"

HAnimHumanoid94.joints.append(HAnimJoint920)
HAnimJoint921 = x3d.HAnimJoint()
HAnimJoint921.USE = "hanim_vt5"

HAnimHumanoid94.joints.append(HAnimJoint921)
HAnimJoint922 = x3d.HAnimJoint()
HAnimJoint922.USE = "hanim_vt4"

HAnimHumanoid94.joints.append(HAnimJoint922)
HAnimJoint923 = x3d.HAnimJoint()
HAnimJoint923.USE = "hanim_vt3"

HAnimHumanoid94.joints.append(HAnimJoint923)
HAnimJoint924 = x3d.HAnimJoint()
HAnimJoint924.USE = "hanim_vt2"

HAnimHumanoid94.joints.append(HAnimJoint924)
HAnimJoint925 = x3d.HAnimJoint()
HAnimJoint925.USE = "hanim_vt1"

HAnimHumanoid94.joints.append(HAnimJoint925)
HAnimJoint926 = x3d.HAnimJoint()
HAnimJoint926.USE = "hanim_vc7"

HAnimHumanoid94.joints.append(HAnimJoint926)
HAnimJoint927 = x3d.HAnimJoint()
HAnimJoint927.USE = "hanim_vc6"

HAnimHumanoid94.joints.append(HAnimJoint927)
HAnimJoint928 = x3d.HAnimJoint()
HAnimJoint928.USE = "hanim_vc5"

HAnimHumanoid94.joints.append(HAnimJoint928)
HAnimJoint929 = x3d.HAnimJoint()
HAnimJoint929.USE = "hanim_vc3"

HAnimHumanoid94.joints.append(HAnimJoint929)
HAnimJoint930 = x3d.HAnimJoint()
HAnimJoint930.USE = "hanim_vc2"

HAnimHumanoid94.joints.append(HAnimJoint930)
HAnimJoint931 = x3d.HAnimJoint()
HAnimJoint931.USE = "hanim_vc1"

HAnimHumanoid94.joints.append(HAnimJoint931)
HAnimJoint932 = x3d.HAnimJoint()
HAnimJoint932.USE = "hanim_l_ankle"

HAnimHumanoid94.joints.append(HAnimJoint932)
HAnimJoint933 = x3d.HAnimJoint()
HAnimJoint933.USE = "hanim_r_ankle"

HAnimHumanoid94.joints.append(HAnimJoint933)
HAnimJoint934 = x3d.HAnimJoint()
HAnimJoint934.USE = "hanim_l_elbow"

HAnimHumanoid94.joints.append(HAnimJoint934)
HAnimJoint935 = x3d.HAnimJoint()
HAnimJoint935.USE = "hanim_r_elbow"

HAnimHumanoid94.joints.append(HAnimJoint935)
HAnimJoint936 = x3d.HAnimJoint()
HAnimJoint936.USE = "hanim_l_hip"

HAnimHumanoid94.joints.append(HAnimJoint936)
HAnimJoint937 = x3d.HAnimJoint()
HAnimJoint937.USE = "hanim_r_hip"

HAnimHumanoid94.joints.append(HAnimJoint937)
HAnimJoint938 = x3d.HAnimJoint()
HAnimJoint938.USE = "hanim_l_index0"

HAnimHumanoid94.joints.append(HAnimJoint938)
HAnimJoint939 = x3d.HAnimJoint()
HAnimJoint939.USE = "hanim_l_index1"

HAnimHumanoid94.joints.append(HAnimJoint939)
HAnimJoint940 = x3d.HAnimJoint()
HAnimJoint940.USE = "hanim_l_index2"

HAnimHumanoid94.joints.append(HAnimJoint940)
HAnimJoint941 = x3d.HAnimJoint()
HAnimJoint941.USE = "hanim_l_index3"

HAnimHumanoid94.joints.append(HAnimJoint941)
HAnimJoint942 = x3d.HAnimJoint()
HAnimJoint942.USE = "hanim_l_knee"

HAnimHumanoid94.joints.append(HAnimJoint942)
HAnimJoint943 = x3d.HAnimJoint()
HAnimJoint943.USE = "hanim_r_knee"

HAnimHumanoid94.joints.append(HAnimJoint943)
HAnimJoint944 = x3d.HAnimJoint()
HAnimJoint944.USE = "hanim_l_metatarsal"

HAnimHumanoid94.joints.append(HAnimJoint944)
HAnimJoint945 = x3d.HAnimJoint()
HAnimJoint945.USE = "hanim_l_midtarsal"

HAnimHumanoid94.joints.append(HAnimJoint945)
HAnimJoint946 = x3d.HAnimJoint()
HAnimJoint946.USE = "hanim_r_midtarsal"

HAnimHumanoid94.joints.append(HAnimJoint946)
HAnimJoint947 = x3d.HAnimJoint()
HAnimJoint947.USE = "hanim_l_shoulder"

HAnimHumanoid94.joints.append(HAnimJoint947)
HAnimJoint948 = x3d.HAnimJoint()
HAnimJoint948.USE = "hanim_r_shoulder"

HAnimHumanoid94.joints.append(HAnimJoint948)
HAnimJoint949 = x3d.HAnimJoint()
HAnimJoint949.USE = "hanim_l_subtalar"

HAnimHumanoid94.joints.append(HAnimJoint949)
HAnimJoint950 = x3d.HAnimJoint()
HAnimJoint950.USE = "hanim_l_thumb1"

HAnimHumanoid94.joints.append(HAnimJoint950)
HAnimJoint951 = x3d.HAnimJoint()
HAnimJoint951.USE = "hanim_l_thumb2"

HAnimHumanoid94.joints.append(HAnimJoint951)
HAnimJoint952 = x3d.HAnimJoint()
HAnimJoint952.USE = "hanim_l_thumb3"

HAnimHumanoid94.joints.append(HAnimJoint952)
HAnimJoint953 = x3d.HAnimJoint()
HAnimJoint953.USE = "hanim_l_wrist"

HAnimHumanoid94.joints.append(HAnimJoint953)
HAnimJoint954 = x3d.HAnimJoint()
HAnimJoint954.USE = "hanim_r_wrist"

HAnimHumanoid94.joints.append(HAnimJoint954)
HAnimSegment955 = x3d.HAnimSegment()
HAnimSegment955.USE = "hanim_pelvis"

HAnimHumanoid94.segments.append(HAnimSegment955)
HAnimSegment956 = x3d.HAnimSegment()
HAnimSegment956.USE = "hanim_c7"

HAnimHumanoid94.segments.append(HAnimSegment956)
HAnimSegment957 = x3d.HAnimSegment()
HAnimSegment957.USE = "hanim_c4"

HAnimHumanoid94.segments.append(HAnimSegment957)
HAnimSegment958 = x3d.HAnimSegment()
HAnimSegment958.USE = "hanim_skull"

HAnimHumanoid94.segments.append(HAnimSegment958)
HAnimSegment959 = x3d.HAnimSegment()
HAnimSegment959.USE = "hanim_sacrum"

HAnimHumanoid94.segments.append(HAnimSegment959)
HAnimSegment960 = x3d.HAnimSegment()
HAnimSegment960.USE = "hanim_midproximal"

HAnimHumanoid94.segments.append(HAnimSegment960)
HAnimSegment961 = x3d.HAnimSegment()
HAnimSegment961.USE = "hanim_l5"

HAnimHumanoid94.segments.append(HAnimSegment961)
HAnimSegment962 = x3d.HAnimSegment()
HAnimSegment962.USE = "hanim_l4"

HAnimHumanoid94.segments.append(HAnimSegment962)
HAnimSegment963 = x3d.HAnimSegment()
HAnimSegment963.USE = "hanim_l3"

HAnimHumanoid94.segments.append(HAnimSegment963)
HAnimSegment964 = x3d.HAnimSegment()
HAnimSegment964.USE = "hanim_l2"

HAnimHumanoid94.segments.append(HAnimSegment964)
HAnimSegment965 = x3d.HAnimSegment()
HAnimSegment965.USE = "hanim_l1"

HAnimHumanoid94.segments.append(HAnimSegment965)
HAnimSegment966 = x3d.HAnimSegment()
HAnimSegment966.USE = "hanim_t12"

HAnimHumanoid94.segments.append(HAnimSegment966)
HAnimSegment967 = x3d.HAnimSegment()
HAnimSegment967.USE = "hanim_t11"

HAnimHumanoid94.segments.append(HAnimSegment967)
HAnimSegment968 = x3d.HAnimSegment()
HAnimSegment968.USE = "hanim_t10"

HAnimHumanoid94.segments.append(HAnimSegment968)
HAnimSegment969 = x3d.HAnimSegment()
HAnimSegment969.USE = "hanim_t9"

HAnimHumanoid94.segments.append(HAnimSegment969)
HAnimSegment970 = x3d.HAnimSegment()
HAnimSegment970.USE = "hanim_t8"

HAnimHumanoid94.segments.append(HAnimSegment970)
HAnimSegment971 = x3d.HAnimSegment()
HAnimSegment971.USE = "hanim_t7"

HAnimHumanoid94.segments.append(HAnimSegment971)
HAnimSegment972 = x3d.HAnimSegment()
HAnimSegment972.USE = "hanim_t6"

HAnimHumanoid94.segments.append(HAnimSegment972)
HAnimSegment973 = x3d.HAnimSegment()
HAnimSegment973.USE = "hanim_t5"

HAnimHumanoid94.segments.append(HAnimSegment973)
HAnimSegment974 = x3d.HAnimSegment()
HAnimSegment974.USE = "hanim_t4"

HAnimHumanoid94.segments.append(HAnimSegment974)
HAnimSegment975 = x3d.HAnimSegment()
HAnimSegment975.USE = "hanim_t3"

HAnimHumanoid94.segments.append(HAnimSegment975)
HAnimSegment976 = x3d.HAnimSegment()
HAnimSegment976.USE = "hanim_t2"

HAnimHumanoid94.segments.append(HAnimSegment976)
HAnimSegment977 = x3d.HAnimSegment()
HAnimSegment977.USE = "hanim_t1"

HAnimHumanoid94.segments.append(HAnimSegment977)
HAnimSegment978 = x3d.HAnimSegment()
HAnimSegment978.USE = "hanim_c6"

HAnimHumanoid94.segments.append(HAnimSegment978)
HAnimSegment979 = x3d.HAnimSegment()
HAnimSegment979.USE = "hanim_c5"

HAnimHumanoid94.segments.append(HAnimSegment979)
HAnimSegment980 = x3d.HAnimSegment()
HAnimSegment980.USE = "hanim_c3"

HAnimHumanoid94.segments.append(HAnimSegment980)
HAnimSegment981 = x3d.HAnimSegment()
HAnimSegment981.USE = "hanim_c2"

HAnimHumanoid94.segments.append(HAnimSegment981)
HAnimSegment982 = x3d.HAnimSegment()
HAnimSegment982.USE = "hanim_c1"

HAnimHumanoid94.segments.append(HAnimSegment982)
HAnimSegment983 = x3d.HAnimSegment()
HAnimSegment983.USE = "hanim_l_calf"

HAnimHumanoid94.segments.append(HAnimSegment983)
HAnimSegment984 = x3d.HAnimSegment()
HAnimSegment984.USE = "hanim_r_calf"

HAnimHumanoid94.segments.append(HAnimSegment984)
HAnimSegment985 = x3d.HAnimSegment()
HAnimSegment985.USE = "hanim_l_forearm"

HAnimHumanoid94.segments.append(HAnimSegment985)
HAnimSegment986 = x3d.HAnimSegment()
HAnimSegment986.USE = "hanim_r_forearm"

HAnimHumanoid94.segments.append(HAnimSegment986)
HAnimSegment987 = x3d.HAnimSegment()
HAnimSegment987.USE = "hanim_l_forefoot"

HAnimHumanoid94.segments.append(HAnimSegment987)
HAnimSegment988 = x3d.HAnimSegment()
HAnimSegment988.USE = "hanim_l_hand"

HAnimHumanoid94.segments.append(HAnimSegment988)
HAnimSegment989 = x3d.HAnimSegment()
HAnimSegment989.USE = "hanim_r_hand"

HAnimHumanoid94.segments.append(HAnimSegment989)
HAnimSegment990 = x3d.HAnimSegment()
HAnimSegment990.USE = "hanim_l_hindfoot"

HAnimHumanoid94.segments.append(HAnimSegment990)
HAnimSegment991 = x3d.HAnimSegment()
HAnimSegment991.USE = "hanim_r_hindfoot"

HAnimHumanoid94.segments.append(HAnimSegment991)
HAnimSegment992 = x3d.HAnimSegment()
HAnimSegment992.USE = "hanim_l_index_distal"

HAnimHumanoid94.segments.append(HAnimSegment992)
HAnimSegment993 = x3d.HAnimSegment()
HAnimSegment993.USE = "hanim_l_index_metacarpal"

HAnimHumanoid94.segments.append(HAnimSegment993)
HAnimSegment994 = x3d.HAnimSegment()
HAnimSegment994.USE = "hanim_l_index_middle"

HAnimHumanoid94.segments.append(HAnimSegment994)
HAnimSegment995 = x3d.HAnimSegment()
HAnimSegment995.USE = "hanim_l_index_proximal"

HAnimHumanoid94.segments.append(HAnimSegment995)
HAnimSegment996 = x3d.HAnimSegment()
HAnimSegment996.USE = "hanim_l_middistal"

HAnimHumanoid94.segments.append(HAnimSegment996)
HAnimSegment997 = x3d.HAnimSegment()
HAnimSegment997.USE = "hanim_r_middistal"

HAnimHumanoid94.segments.append(HAnimSegment997)
HAnimSegment998 = x3d.HAnimSegment()
HAnimSegment998.USE = "hanim_l_thigh"

HAnimHumanoid94.segments.append(HAnimSegment998)
HAnimSegment999 = x3d.HAnimSegment()
HAnimSegment999.USE = "hanim_r_thigh"

HAnimHumanoid94.segments.append(HAnimSegment999)
HAnimSegment1000 = x3d.HAnimSegment()
HAnimSegment1000.USE = "hanim_l_thumb_distal"

HAnimHumanoid94.segments.append(HAnimSegment1000)
HAnimSegment1001 = x3d.HAnimSegment()
HAnimSegment1001.USE = "hanim_l_thumb_metacarpal"

HAnimHumanoid94.segments.append(HAnimSegment1001)
HAnimSegment1002 = x3d.HAnimSegment()
HAnimSegment1002.USE = "hanim_l_thumb_proximal"

HAnimHumanoid94.segments.append(HAnimSegment1002)
HAnimSegment1003 = x3d.HAnimSegment()
HAnimSegment1003.USE = "hanim_l_upperarm"

HAnimHumanoid94.segments.append(HAnimSegment1003)
HAnimSegment1004 = x3d.HAnimSegment()
HAnimSegment1004.USE = "hanim_r_upperarm"

HAnimHumanoid94.segments.append(HAnimSegment1004)
HAnimSite1005 = x3d.HAnimSite()
HAnimSite1005.USE = "hanim_crotch_pt"

HAnimHumanoid94.sites.append(HAnimSite1005)
HAnimSite1006 = x3d.HAnimSite()
HAnimSite1006.USE = "hanim_skull_tip"

HAnimHumanoid94.sites.append(HAnimSite1006)
HAnimSite1007 = x3d.HAnimSite()
HAnimSite1007.USE = "hanim_sellion_pt"

HAnimHumanoid94.sites.append(HAnimSite1007)
HAnimSite1008 = x3d.HAnimSite()
HAnimSite1008.USE = "hanim_supramenton_pt"

HAnimHumanoid94.sites.append(HAnimSite1008)
HAnimSite1009 = x3d.HAnimSite()
HAnimSite1009.USE = "hanim_nuchale_pt"

HAnimHumanoid94.sites.append(HAnimSite1009)
HAnimSite1010 = x3d.HAnimSite()
HAnimSite1010.USE = "hanim_r_asis_pt"

HAnimHumanoid94.sites.append(HAnimSite1010)
HAnimSite1011 = x3d.HAnimSite()
HAnimSite1011.USE = "hanim_l_asis_pt"

HAnimHumanoid94.sites.append(HAnimSite1011)
HAnimSite1012 = x3d.HAnimSite()
HAnimSite1012.USE = "hanim_l_calcaneous_post_pt"

HAnimHumanoid94.sites.append(HAnimSite1012)
HAnimSite1013 = x3d.HAnimSite()
HAnimSite1013.USE = "hanim_r_calcaneous_post_pt"

HAnimHumanoid94.sites.append(HAnimSite1013)
HAnimSite1014 = x3d.HAnimSite()
HAnimSite1014.USE = "hanim_l_dactylion_pt"

HAnimHumanoid94.sites.append(HAnimSite1014)
HAnimSite1015 = x3d.HAnimSite()
HAnimSite1015.USE = "hanim_r_dactylion_pt"

HAnimHumanoid94.sites.append(HAnimSite1015)
HAnimSite1016 = x3d.HAnimSite()
HAnimSite1016.USE = "hanim_l_digit2_pt"

HAnimHumanoid94.sites.append(HAnimSite1016)
HAnimSite1017 = x3d.HAnimSite()
HAnimSite1017.USE = "hanim_r_digit2_pt"

HAnimHumanoid94.sites.append(HAnimSite1017)
HAnimSite1018 = x3d.HAnimSite()
HAnimSite1018.USE = "hanim_l_femoral_lateral_epicn_pt"

HAnimHumanoid94.sites.append(HAnimSite1018)
HAnimSite1019 = x3d.HAnimSite()
HAnimSite1019.USE = "hanim_r_femoral_lateral_epicn_pt"

HAnimHumanoid94.sites.append(HAnimSite1019)
HAnimSite1020 = x3d.HAnimSite()
HAnimSite1020.USE = "hanim_l_femoral_medial_epicn_pt"

HAnimHumanoid94.sites.append(HAnimSite1020)
HAnimSite1021 = x3d.HAnimSite()
HAnimSite1021.USE = "hanim_r_femoral_medial_epicn_pt"

HAnimHumanoid94.sites.append(HAnimSite1021)
HAnimSite1022 = x3d.HAnimSite()
HAnimSite1022.USE = "hanim_l_forefoot_tip"

HAnimHumanoid94.sites.append(HAnimSite1022)
HAnimSite1023 = x3d.HAnimSite()
HAnimSite1023.USE = "hanim_r_gonion_pt"

HAnimHumanoid94.sites.append(HAnimSite1023)
HAnimSite1024 = x3d.HAnimSite()
HAnimSite1024.USE = "hanim_l_gonion_pt"

HAnimHumanoid94.sites.append(HAnimSite1024)
HAnimSite1025 = x3d.HAnimSite()
HAnimSite1025.USE = "hanim_l_hand_tip"

HAnimHumanoid94.sites.append(HAnimSite1025)
HAnimSite1026 = x3d.HAnimSite()
HAnimSite1026.USE = "hanim_r_hand_tip"

HAnimHumanoid94.sites.append(HAnimSite1026)
HAnimSite1027 = x3d.HAnimSite()
HAnimSite1027.USE = "hanim_l_humeral_lateral_epicn_pt"

HAnimHumanoid94.sites.append(HAnimSite1027)
HAnimSite1028 = x3d.HAnimSite()
HAnimSite1028.USE = "hanim_r_humeral_lateral_epicn_pt"

HAnimHumanoid94.sites.append(HAnimSite1028)
HAnimSite1029 = x3d.HAnimSite()
HAnimSite1029.USE = "hanim_l_humeral_medial_epicn_pt"

HAnimHumanoid94.sites.append(HAnimSite1029)
HAnimSite1030 = x3d.HAnimSite()
HAnimSite1030.USE = "hanim_r_humeral_medial_epicn_pt"

HAnimHumanoid94.sites.append(HAnimSite1030)
HAnimSite1031 = x3d.HAnimSite()
HAnimSite1031.USE = "hanim_r_iliocristale_pt"

HAnimHumanoid94.sites.append(HAnimSite1031)
HAnimSite1032 = x3d.HAnimSite()
HAnimSite1032.USE = "hanim_l_iliocristale_pt"

HAnimHumanoid94.sites.append(HAnimSite1032)
HAnimSite1033 = x3d.HAnimSite()
HAnimSite1033.USE = "hanim_l_index_distal_tip"

HAnimHumanoid94.sites.append(HAnimSite1033)
HAnimSite1034 = x3d.HAnimSite()
HAnimSite1034.USE = "hanim_r_infraorbitale_pt"

HAnimHumanoid94.sites.append(HAnimSite1034)
HAnimSite1035 = x3d.HAnimSite()
HAnimSite1035.USE = "hanim_l_infraorbitale_pt"

HAnimHumanoid94.sites.append(HAnimSite1035)
HAnimSite1036 = x3d.HAnimSite()
HAnimSite1036.USE = "hanim_l_knee_crease_pt"

HAnimHumanoid94.sites.append(HAnimSite1036)
HAnimSite1037 = x3d.HAnimSite()
HAnimSite1037.USE = "hanim_r_knee_crease_pt"

HAnimHumanoid94.sites.append(HAnimSite1037)
HAnimSite1038 = x3d.HAnimSite()
HAnimSite1038.USE = "hanim_l_lateral_malleolus_pt"

HAnimHumanoid94.sites.append(HAnimSite1038)
HAnimSite1039 = x3d.HAnimSite()
HAnimSite1039.USE = "hanim_r_lateral_malleolus_pt"

HAnimHumanoid94.sites.append(HAnimSite1039)
HAnimSite1040 = x3d.HAnimSite()
HAnimSite1040.USE = "hanim_l_medial_malleolus_pt"

HAnimHumanoid94.sites.append(HAnimSite1040)
HAnimSite1041 = x3d.HAnimSite()
HAnimSite1041.USE = "hanim_r_medial_malleolus_pt"

HAnimHumanoid94.sites.append(HAnimSite1041)
HAnimSite1042 = x3d.HAnimSite()
HAnimSite1042.USE = "hanim_l_metacarpal_pha2_pt"

HAnimHumanoid94.sites.append(HAnimSite1042)
HAnimSite1043 = x3d.HAnimSite()
HAnimSite1043.USE = "hanim_r_metacarpal_pha2_pt"

HAnimHumanoid94.sites.append(HAnimSite1043)
HAnimSite1044 = x3d.HAnimSite()
HAnimSite1044.USE = "hanim_l_metacarpal_pha5_pt"

HAnimHumanoid94.sites.append(HAnimSite1044)
HAnimSite1045 = x3d.HAnimSite()
HAnimSite1045.USE = "hanim_r_metacarpal_pha5_pt"

HAnimHumanoid94.sites.append(HAnimSite1045)
HAnimSite1046 = x3d.HAnimSite()
HAnimSite1046.USE = "hanim_l_metatarsal_pha1_pt"

HAnimHumanoid94.sites.append(HAnimSite1046)
HAnimSite1047 = x3d.HAnimSite()
HAnimSite1047.USE = "hanim_r_metatarsal_pha1_pt"

HAnimHumanoid94.sites.append(HAnimSite1047)
HAnimSite1048 = x3d.HAnimSite()
HAnimSite1048.USE = "hanim_l_metatarsal_pha5_pt"

HAnimHumanoid94.sites.append(HAnimSite1048)
HAnimSite1049 = x3d.HAnimSite()
HAnimSite1049.USE = "hanim_r_metatarsal_pha5_pt"

HAnimHumanoid94.sites.append(HAnimSite1049)
HAnimSite1050 = x3d.HAnimSite()
HAnimSite1050.USE = "hanim_l_middistal_tip"

HAnimHumanoid94.sites.append(HAnimSite1050)
HAnimSite1051 = x3d.HAnimSite()
HAnimSite1051.USE = "hanim_r_middistal_tip"

HAnimHumanoid94.sites.append(HAnimSite1051)
HAnimSite1052 = x3d.HAnimSite()
HAnimSite1052.USE = "hanim_l_olecranon_pt"

HAnimHumanoid94.sites.append(HAnimSite1052)
HAnimSite1053 = x3d.HAnimSite()
HAnimSite1053.USE = "hanim_r_olecranon_pt"

HAnimHumanoid94.sites.append(HAnimSite1053)
HAnimSite1054 = x3d.HAnimSite()
HAnimSite1054.USE = "hanim_r_psis_pt"

HAnimHumanoid94.sites.append(HAnimSite1054)
HAnimSite1055 = x3d.HAnimSite()
HAnimSite1055.USE = "hanim_l_psis_pt"

HAnimHumanoid94.sites.append(HAnimSite1055)
HAnimSite1056 = x3d.HAnimSite()
HAnimSite1056.USE = "hanim_l_radial_styloid_pt"

HAnimHumanoid94.sites.append(HAnimSite1056)
HAnimSite1057 = x3d.HAnimSite()
HAnimSite1057.USE = "hanim_r_radial_styloid_pt"

HAnimHumanoid94.sites.append(HAnimSite1057)
HAnimSite1058 = x3d.HAnimSite()
HAnimSite1058.USE = "hanim_l_radiale_pt"

HAnimHumanoid94.sites.append(HAnimSite1058)
HAnimSite1059 = x3d.HAnimSite()
HAnimSite1059.USE = "hanim_r_radiale_pt"

HAnimHumanoid94.sites.append(HAnimSite1059)
HAnimSite1060 = x3d.HAnimSite()
HAnimSite1060.USE = "hanim_l_sphyrion_pt"

HAnimHumanoid94.sites.append(HAnimSite1060)
HAnimSite1061 = x3d.HAnimSite()
HAnimSite1061.USE = "hanim_r_sphyrion_pt"

HAnimHumanoid94.sites.append(HAnimSite1061)
HAnimSite1062 = x3d.HAnimSite()
HAnimSite1062.USE = "hanim_l_thumb_distal_tip"

HAnimHumanoid94.sites.append(HAnimSite1062)
HAnimSite1063 = x3d.HAnimSite()
HAnimSite1063.USE = "hanim_r_tragion_pt"

HAnimHumanoid94.sites.append(HAnimSite1063)
HAnimSite1064 = x3d.HAnimSite()
HAnimSite1064.USE = "hanim_l_tragion_pt"

HAnimHumanoid94.sites.append(HAnimSite1064)
HAnimSite1065 = x3d.HAnimSite()
HAnimSite1065.USE = "hanim_r_trochanterion_pt"

HAnimHumanoid94.sites.append(HAnimSite1065)
HAnimSite1066 = x3d.HAnimSite()
HAnimSite1066.USE = "hanim_l_trochanterion_pt"

HAnimHumanoid94.sites.append(HAnimSite1066)
HAnimSite1067 = x3d.HAnimSite()
HAnimSite1067.USE = "hanim_l_ulnar_styloid_pt"

HAnimHumanoid94.sites.append(HAnimSite1067)
HAnimSite1068 = x3d.HAnimSite()
HAnimSite1068.USE = "hanim_r_ulnar_styloid_pt"

HAnimHumanoid94.sites.append(HAnimSite1068)

Scene17.children.append(HAnimHumanoid94)

X3D0.Scene = Scene17
f = open("././DiamondManLOA_2_RoundTrip.x3d", "w")
f.write(X3D0.XML())
f.close()
