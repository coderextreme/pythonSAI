print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Immersive"
X3D0.version = "4.0"
head1 = x3d.head()
component2 = x3d.component()
component2.level = 1
component2.name = "HAnim"

head1.children.append(component2)
meta3 = x3d.meta()
meta3.content = "JohnBoy.x3d"
meta3.name = "title"

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.name = "identifier"
meta4.content = "http://www.web3d.org/x3d/content/examples/HumanoidAnimation/JohnBoy.x3d"

head1.children.append(meta4)
meta5 = x3d.meta()
meta5.name = "description"
meta5.content = "An attempt at a standard LOA-4 skeleton"

head1.children.append(meta5)
meta6 = x3d.meta()
meta6.name = "generator"
meta6.content = "h2.pl"

head1.children.append(meta6)
meta7 = x3d.meta()
meta7.content = "John Carlson"
meta7.name = "creator"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.content = "9 November 2020"
meta8.name = "created"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.content = "../license.html"
meta9.name = "license"

head1.children.append(meta9)

X3D0.head = head1
Scene10 = x3d.Scene()
Transform11 = x3d.Transform()
Transform11.scale = [1,1,1]
""" DEF for markerfor XYZ axes """
Shape12 = x3d.Shape()
Shape12.DEF = "AxisLinesShape"
""" RGB lines showing XYZ axes """
IndexedLineSet13 = x3d.IndexedLineSet()
IndexedLineSet13.colorIndex = [0,1,2]
IndexedLineSet13.colorPerVertex = False
IndexedLineSet13.coordIndex = [0,1,-1,0,2,-1,0,3,-1]
Coordinate14 = x3d.Coordinate()

IndexedLineSet13.coord = Coordinate14
Color15 = x3d.Color()

IndexedLineSet13.color = Color15

Shape12.geometry = IndexedLineSet13

Transform11.children.append(Shape12)

Scene10.children.append(Transform11)
Group16 = x3d.Group()
""" DEFS for markers of skeleton joints, segments, and sites """
Transform17 = x3d.Transform()
Transform17.translation = [0,0,0]
Transform17.scale = [1,1,1]
Transform18 = x3d.Transform()
Transform18.translation = [0,2,0]
Transform18.scale = [1,1,1]
Shape19 = x3d.Shape()
Shape19.DEF = "HAnimRootShape"
Sphere20 = x3d.Sphere()
Sphere20.radius = 0.02

Shape19.geometry = Sphere20
Appearance21 = x3d.Appearance()
Material22 = x3d.Material()
Material22.DEF = "HAnimRootMaterial"
Material22.diffuseColor = [0.8,0,0]
Material22.transparency = 0.3

Appearance21.material = Material22

Shape19.appearance = Appearance21

Transform18.children.append(Shape19)

Transform17.children.append(Transform18)
Transform23 = x3d.Transform()
Transform23.translation = [0,2.1,0]
Transform23.scale = [1,1,1]
Shape24 = x3d.Shape()
Shape24.DEF = "HAnimJointShape"
Sphere25 = x3d.Sphere()
Sphere25.radius = 0.02

Shape24.geometry = Sphere25
Appearance26 = x3d.Appearance()
Material27 = x3d.Material()
Material27.DEF = "HAnimJointMaterial"
Material27.diffuseColor = [0,0,0.8]
Material27.transparency = 0.3

Appearance26.material = Material27

Shape24.appearance = Appearance26

Transform23.children.append(Shape24)

Transform17.children.append(Transform23)
Transform28 = x3d.Transform()
Transform28.translation = [0,2.05,0]
Transform28.scale = [1,1,1]
Shape29 = x3d.Shape()
Shape29.DEF = "HAnimSegmentLine"
LineSet30 = x3d.LineSet()
LineSet30.vertexCount = [2]
ColorRGBA31 = x3d.ColorRGBA()
ColorRGBA31.DEF = "HAnimSegmentLineColorRGBA"

LineSet30.color = ColorRGBA31
Coordinate32 = x3d.Coordinate()

LineSet30.coord = Coordinate32

Shape29.geometry = LineSet30

Transform28.children.append(Shape29)

Transform17.children.append(Transform28)
Transform33 = x3d.Transform()
Transform33.translation = [0,2.1,0]
Transform33.scale = [1,1,1]
Shape34 = x3d.Shape()
Shape34.DEF = "HAnimSiteShape"
IndexedFaceSet35 = x3d.IndexedFaceSet()
IndexedFaceSet35.DEF = "DiamondIFS"
IndexedFaceSet35.creaseAngle = 0.5
IndexedFaceSet35.solid = False
IndexedFaceSet35.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
ColorRGBA36 = x3d.ColorRGBA()
ColorRGBA36.DEF = "HAnimSiteColorRGBA"

IndexedFaceSet35.color = ColorRGBA36
Coordinate37 = x3d.Coordinate()

IndexedFaceSet35.coord = Coordinate37

Shape34.geometry = IndexedFaceSet35
Appearance38 = x3d.Appearance()
Material39 = x3d.Material()
Material39.diffuseColor = [1,1,0]
Material39.transparency = 0.3

Appearance38.material = Material39

Shape34.appearance = Appearance38

Transform33.children.append(Shape34)

Transform17.children.append(Transform33)

Group16.children.append(Transform17)

Scene10.children.append(Group16)
NavigationInfo40 = x3d.NavigationInfo()
NavigationInfo40.speed = 1.5
NavigationInfo40.type = ["EXAMINE","ANY"]

Scene10.children.append(NavigationInfo40)
Viewpoint41 = x3d.Viewpoint()
Viewpoint41.centerOfRotation = [0,0,0]
Viewpoint41.description = "default"

Scene10.children.append(Viewpoint41)
HAnimHumanoid42 = x3d.HAnimHumanoid()
HAnimHumanoid42.DEF = "hanim_HAnim"
HAnimHumanoid42.info = ["humanoidVersion=2.0"]
HAnimHumanoid42.name = "HAnim"
HAnimHumanoid42.scale = [1,1,1]
HAnimHumanoid42.translation = [0,0,0]
HAnimHumanoid42.version = "2.0"
HAnimJoint43 = x3d.HAnimJoint()
HAnimJoint43.DEF = "hanim_humanoid_root"
HAnimJoint43.name = "humanoid_root"
HAnimJoint43.center = [0.0000,0.8240,0.0277]
HAnimSegment44 = x3d.HAnimSegment()
HAnimSegment44.DEF = "hanim_sacrum"
HAnimSegment44.name = "sacrum"
Transform45 = x3d.Transform()
Transform45.translation = [0.0000,0.8240,0.0277]
Transform46 = x3d.Transform()
""" Empty Transform """
Shape47 = x3d.Shape()
Shape47.USE = "HAnimJointShape"

Transform46.children.append(Shape47)

Transform45.children.append(Transform46)

HAnimSegment44.children.append(Transform45)
Shape48 = x3d.Shape()
LineSet49 = x3d.LineSet()
LineSet49.vertexCount = [2]
Coordinate50 = x3d.Coordinate()

LineSet49.coord = Coordinate50
""" from humanoid_root to sacroiliac """
ColorRGBA51 = x3d.ColorRGBA()
ColorRGBA51.USE = "HAnimSegmentLineColorRGBA"

LineSet49.color = ColorRGBA51

Shape48.geometry = LineSet49

HAnimSegment44.children.append(Shape48)
HAnimSite52 = x3d.HAnimSite()
HAnimSite52.DEF = "hanim_buttocks_standing_wall_contact_point_pt"
HAnimSite52.name = "buttocks_standing_wall_contact_point_pt"
HAnimSite52.translation = [0,1,0]
TouchSensor53 = x3d.TouchSensor()
TouchSensor53.description = "HAnimSite buttocks_standing_wall_contact_point_pt"

HAnimSite52.children.append(TouchSensor53)
Shape54 = x3d.Shape()
Shape54.USE = "HAnimSiteShape"

HAnimSite52.children.append(Shape54)

HAnimSegment44.children.append(HAnimSite52)
HAnimSite55 = x3d.HAnimSite()
HAnimSite55.DEF = "hanim_crotch_pt"
HAnimSite55.name = "crotch_pt"
HAnimSite55.translation = [0.0034,0.8266,0.0257]
TouchSensor56 = x3d.TouchSensor()
TouchSensor56.description = "HAnimSite crotch_pt"

HAnimSite55.children.append(TouchSensor56)
Shape57 = x3d.Shape()
Shape57.USE = "HAnimSiteShape"

HAnimSite55.children.append(Shape57)

HAnimSegment44.children.append(HAnimSite55)
HAnimSite58 = x3d.HAnimSite()
HAnimSite58.DEF = "hanim_l_asis_pt"
HAnimSite58.name = "l_asis_pt"
HAnimSite58.translation = [0.0925,0.9983,0.1052]
TouchSensor59 = x3d.TouchSensor()
TouchSensor59.description = "HAnimSite l_asis_pt"

HAnimSite58.children.append(TouchSensor59)
Shape60 = x3d.Shape()
Shape60.USE = "HAnimSiteShape"

HAnimSite58.children.append(Shape60)

HAnimSegment44.children.append(HAnimSite58)
HAnimSite61 = x3d.HAnimSite()
HAnimSite61.DEF = "hanim_l_iliocristale_pt"
HAnimSite61.name = "l_iliocristale_pt"
HAnimSite61.translation = [0.1612,1.0537,0.0008]
TouchSensor62 = x3d.TouchSensor()
TouchSensor62.description = "HAnimSite l_iliocristale_pt"

HAnimSite61.children.append(TouchSensor62)
Shape63 = x3d.Shape()
Shape63.USE = "HAnimSiteShape"

HAnimSite61.children.append(Shape63)

HAnimSegment44.children.append(HAnimSite61)
HAnimSite64 = x3d.HAnimSite()
HAnimSite64.DEF = "hanim_l_psis_pt"
HAnimSite64.name = "l_psis_pt"
HAnimSite64.translation = [0.0774,1.0190,-0.1151]
TouchSensor65 = x3d.TouchSensor()
TouchSensor65.description = "HAnimSite l_psis_pt"

HAnimSite64.children.append(TouchSensor65)
Shape66 = x3d.Shape()
Shape66.USE = "HAnimSiteShape"

HAnimSite64.children.append(Shape66)

HAnimSegment44.children.append(HAnimSite64)
HAnimSite67 = x3d.HAnimSite()
HAnimSite67.DEF = "hanim_l_trochanterion_pt"
HAnimSite67.name = "l_trochanterion_pt"
HAnimSite67.translation = [0.1677,0.8336,0.0303]
TouchSensor68 = x3d.TouchSensor()
TouchSensor68.description = "HAnimSite l_trochanterion_pt"

HAnimSite67.children.append(TouchSensor68)
Shape69 = x3d.Shape()
Shape69.USE = "HAnimSiteShape"

HAnimSite67.children.append(Shape69)

HAnimSegment44.children.append(HAnimSite67)
HAnimSite70 = x3d.HAnimSite()
HAnimSite70.DEF = "hanim_r_asis_pt"
HAnimSite70.name = "r_asis_pt"
HAnimSite70.translation = [-0.0887,1.0021,0.1112]
TouchSensor71 = x3d.TouchSensor()
TouchSensor71.description = "HAnimSite r_asis_pt"

HAnimSite70.children.append(TouchSensor71)
Shape72 = x3d.Shape()
Shape72.USE = "HAnimSiteShape"

HAnimSite70.children.append(Shape72)

HAnimSegment44.children.append(HAnimSite70)
HAnimSite73 = x3d.HAnimSite()
HAnimSite73.DEF = "hanim_r_iliocristale_pt"
HAnimSite73.name = "r_iliocristale_pt"
HAnimSite73.translation = [-0.1525,1.0628,0.0035]
TouchSensor74 = x3d.TouchSensor()
TouchSensor74.description = "HAnimSite r_iliocristale_pt"

HAnimSite73.children.append(TouchSensor74)
Shape75 = x3d.Shape()
Shape75.USE = "HAnimSiteShape"

HAnimSite73.children.append(Shape75)

HAnimSegment44.children.append(HAnimSite73)
HAnimSite76 = x3d.HAnimSite()
HAnimSite76.DEF = "hanim_r_psis_pt"
HAnimSite76.name = "r_psis_pt"
HAnimSite76.translation = [-0.0716,1.0190,-0.1138]
TouchSensor77 = x3d.TouchSensor()
TouchSensor77.description = "HAnimSite r_psis_pt"

HAnimSite76.children.append(TouchSensor77)
Shape78 = x3d.Shape()
Shape78.USE = "HAnimSiteShape"

HAnimSite76.children.append(Shape78)

HAnimSegment44.children.append(HAnimSite76)
HAnimSite79 = x3d.HAnimSite()
HAnimSite79.DEF = "hanim_r_trochanterion_pt"
HAnimSite79.name = "r_trochanterion_pt"
HAnimSite79.translation = [-0.1689,0.8419,0.0352]
TouchSensor80 = x3d.TouchSensor()
TouchSensor80.description = "HAnimSite r_trochanterion_pt"

HAnimSite79.children.append(TouchSensor80)
Shape81 = x3d.Shape()
Shape81.USE = "HAnimSiteShape"

HAnimSite79.children.append(Shape81)

HAnimSegment44.children.append(HAnimSite79)
Shape82 = x3d.Shape()
LineSet83 = x3d.LineSet()
LineSet83.vertexCount = [2]
Coordinate84 = x3d.Coordinate()

LineSet83.coord = Coordinate84
""" from humanoid_root to vl5 """
ColorRGBA85 = x3d.ColorRGBA()
ColorRGBA85.USE = "HAnimSegmentLineColorRGBA"

LineSet83.color = ColorRGBA85

Shape82.geometry = LineSet83

HAnimSegment44.children.append(Shape82)
HAnimSite86 = x3d.HAnimSite()
HAnimSite86.DEF = "hanim_navel_pt"
HAnimSite86.name = "navel_pt"
HAnimSite86.translation = [0.0069,1.0966,0.1017]
TouchSensor87 = x3d.TouchSensor()
TouchSensor87.description = "HAnimSite navel_pt"

HAnimSite86.children.append(TouchSensor87)
Shape88 = x3d.Shape()
Shape88.USE = "HAnimSiteShape"

HAnimSite86.children.append(Shape88)

HAnimSegment44.children.append(HAnimSite86)
HAnimSite89 = x3d.HAnimSite()
HAnimSite89.DEF = "hanim_waist_preferred_anterior_pt"
HAnimSite89.name = "waist_preferred_anterior_pt"
HAnimSite89.translation = [0,1,0]
TouchSensor90 = x3d.TouchSensor()
TouchSensor90.description = "HAnimSite waist_preferred_anterior_pt"

HAnimSite89.children.append(TouchSensor90)
Shape91 = x3d.Shape()
Shape91.USE = "HAnimSiteShape"

HAnimSite89.children.append(Shape91)

HAnimSegment44.children.append(HAnimSite89)
HAnimSite92 = x3d.HAnimSite()
HAnimSite92.DEF = "hanim_waist_preferred_posterior_pt"
HAnimSite92.name = "waist_preferred_posterior_pt"
HAnimSite92.translation = [0.2900,1.0915,-0.1091]
TouchSensor93 = x3d.TouchSensor()
TouchSensor93.description = "HAnimSite waist_preferred_posterior_pt"

HAnimSite92.children.append(TouchSensor93)
Shape94 = x3d.Shape()
Shape94.USE = "HAnimSiteShape"

HAnimSite92.children.append(Shape94)

HAnimSegment44.children.append(HAnimSite92)

HAnimJoint43.children.append(HAnimSegment44)
HAnimJoint95 = x3d.HAnimJoint()
HAnimJoint95.DEF = "hanim_sacroiliac"
HAnimJoint95.name = "sacroiliac"
HAnimJoint95.center = [0.0000,0.9149,0.0016]
HAnimSegment96 = x3d.HAnimSegment()
HAnimSegment96.DEF = "hanim_pelvis"
HAnimSegment96.name = "pelvis"
Transform97 = x3d.Transform()
Transform97.translation = [0.0000,0.9149,0.0016]
Transform98 = x3d.Transform()
""" Empty Transform """
Shape99 = x3d.Shape()
Shape99.USE = "HAnimJointShape"

Transform98.children.append(Shape99)

Transform97.children.append(Transform98)

HAnimSegment96.children.append(Transform97)
Shape100 = x3d.Shape()
LineSet101 = x3d.LineSet()
LineSet101.vertexCount = [2]
Coordinate102 = x3d.Coordinate()

LineSet101.coord = Coordinate102
""" from sacroiliac to l_hip """
ColorRGBA103 = x3d.ColorRGBA()
ColorRGBA103.USE = "HAnimSegmentLineColorRGBA"

LineSet101.color = ColorRGBA103

Shape100.geometry = LineSet101

HAnimSegment96.children.append(Shape100)
HAnimSite104 = x3d.HAnimSite()
HAnimSite104.DEF = "hanim_l_femoral_lateral_epicondyles_pt"
HAnimSite104.name = "l_femoral_lateral_epicondyles_pt"
HAnimSite104.translation = [0.1598,0.4967,0.0297]
TouchSensor105 = x3d.TouchSensor()
TouchSensor105.description = "HAnimSite l_femoral_lateral_epicondyles_pt"

HAnimSite104.children.append(TouchSensor105)
Shape106 = x3d.Shape()
Shape106.USE = "HAnimSiteShape"

HAnimSite104.children.append(Shape106)

HAnimSegment96.children.append(HAnimSite104)
HAnimSite107 = x3d.HAnimSite()
HAnimSite107.DEF = "hanim_l_femoral_medial_epicondyles_pt"
HAnimSite107.name = "l_femoral_medial_epicondyles_pt"
HAnimSite107.translation = [0.0398,0.4946,0.0303]
TouchSensor108 = x3d.TouchSensor()
TouchSensor108.description = "HAnimSite l_femoral_medial_epicondyles_pt"

HAnimSite107.children.append(TouchSensor108)
Shape109 = x3d.Shape()
Shape109.USE = "HAnimSiteShape"

HAnimSite107.children.append(Shape109)

HAnimSegment96.children.append(HAnimSite107)
HAnimSite110 = x3d.HAnimSite()
HAnimSite110.DEF = "hanim_l_knee_crease_pt"
HAnimSite110.name = "l_knee_crease_pt"
HAnimSite110.translation = [0.0993,0.4881,-0.0309]
TouchSensor111 = x3d.TouchSensor()
TouchSensor111.description = "HAnimSite l_knee_crease_pt"

HAnimSite110.children.append(TouchSensor111)
Shape112 = x3d.Shape()
Shape112.USE = "HAnimSiteShape"

HAnimSite110.children.append(Shape112)

HAnimSegment96.children.append(HAnimSite110)
HAnimSite113 = x3d.HAnimSite()
HAnimSite113.DEF = "hanim_l_suprapatella_pt"
HAnimSite113.name = "l_suprapatella_pt"
HAnimSite113.translation = [0,1,0]
TouchSensor114 = x3d.TouchSensor()
TouchSensor114.description = "HAnimSite l_suprapatella_pt"

HAnimSite113.children.append(TouchSensor114)
Shape115 = x3d.Shape()
Shape115.USE = "HAnimSiteShape"

HAnimSite113.children.append(Shape115)

HAnimSegment96.children.append(HAnimSite113)
Shape116 = x3d.Shape()
LineSet117 = x3d.LineSet()
LineSet117.vertexCount = [2]
Coordinate118 = x3d.Coordinate()

LineSet117.coord = Coordinate118
""" from sacroiliac to r_hip """
ColorRGBA119 = x3d.ColorRGBA()
ColorRGBA119.USE = "HAnimSegmentLineColorRGBA"

LineSet117.color = ColorRGBA119

Shape116.geometry = LineSet117

HAnimSegment96.children.append(Shape116)
HAnimSite120 = x3d.HAnimSite()
HAnimSite120.DEF = "hanim_r_femoral_lateral_epicondyles_pt"
HAnimSite120.name = "r_femoral_lateral_epicondyles_pt"
HAnimSite120.translation = [-0.1421,0.4992,0.0310]
TouchSensor121 = x3d.TouchSensor()
TouchSensor121.description = "HAnimSite r_femoral_lateral_epicondyles_pt"

HAnimSite120.children.append(TouchSensor121)
Shape122 = x3d.Shape()
Shape122.USE = "HAnimSiteShape"

HAnimSite120.children.append(Shape122)

HAnimSegment96.children.append(HAnimSite120)
HAnimSite123 = x3d.HAnimSite()
HAnimSite123.DEF = "hanim_r_femoral_medial_epicondyles_pt"
HAnimSite123.name = "r_femoral_medial_epicondyles_pt"
HAnimSite123.translation = [-0.0221,0.5014,0.0289]
TouchSensor124 = x3d.TouchSensor()
TouchSensor124.description = "HAnimSite r_femoral_medial_epicondyles_pt"

HAnimSite123.children.append(TouchSensor124)
Shape125 = x3d.Shape()
Shape125.USE = "HAnimSiteShape"

HAnimSite123.children.append(Shape125)

HAnimSegment96.children.append(HAnimSite123)
HAnimSite126 = x3d.HAnimSite()
HAnimSite126.DEF = "hanim_r_knee_crease_pt"
HAnimSite126.name = "r_knee_crease_pt"
HAnimSite126.translation = [-0.0825,0.4932,-0.0326]
TouchSensor127 = x3d.TouchSensor()
TouchSensor127.description = "HAnimSite r_knee_crease_pt"

HAnimSite126.children.append(TouchSensor127)
Shape128 = x3d.Shape()
Shape128.USE = "HAnimSiteShape"

HAnimSite126.children.append(Shape128)

HAnimSegment96.children.append(HAnimSite126)
HAnimSite129 = x3d.HAnimSite()
HAnimSite129.DEF = "hanim_r_suprapatella_pt"
HAnimSite129.name = "r_suprapatella_pt"
HAnimSite129.translation = [0,1,0]
TouchSensor130 = x3d.TouchSensor()
TouchSensor130.description = "HAnimSite r_suprapatella_pt"

HAnimSite129.children.append(TouchSensor130)
Shape131 = x3d.Shape()
Shape131.USE = "HAnimSiteShape"

HAnimSite129.children.append(Shape131)

HAnimSegment96.children.append(HAnimSite129)

HAnimJoint95.children.append(HAnimSegment96)
HAnimJoint132 = x3d.HAnimJoint()
HAnimJoint132.DEF = "hanim_l_hip"
HAnimJoint132.name = "l_hip"
HAnimJoint132.center = [0.0961,0.9124,-0.0001]
HAnimSegment133 = x3d.HAnimSegment()
HAnimSegment133.DEF = "hanim_l_thigh"
HAnimSegment133.name = "l_thigh"
Transform134 = x3d.Transform()
Transform134.translation = [0.0961,0.9124,-0.0001]
Transform135 = x3d.Transform()
""" Empty Transform """
Shape136 = x3d.Shape()
Shape136.USE = "HAnimJointShape"

Transform135.children.append(Shape136)

Transform134.children.append(Transform135)

HAnimSegment133.children.append(Transform134)
Shape137 = x3d.Shape()
LineSet138 = x3d.LineSet()
LineSet138.vertexCount = [2]
Coordinate139 = x3d.Coordinate()

LineSet138.coord = Coordinate139
""" from l_hip to l_knee """
ColorRGBA140 = x3d.ColorRGBA()
ColorRGBA140.USE = "HAnimSegmentLineColorRGBA"

LineSet138.color = ColorRGBA140

Shape137.geometry = LineSet138

HAnimSegment133.children.append(Shape137)
HAnimSite141 = x3d.HAnimSite()
HAnimSite141.DEF = "hanim_l_lateral_malleolus_pt"
HAnimSite141.name = "l_lateral_malleolus_pt"
HAnimSite141.translation = [0.1308,0.0597,-0.1032]
TouchSensor142 = x3d.TouchSensor()
TouchSensor142.description = "HAnimSite l_lateral_malleolus_pt"

HAnimSite141.children.append(TouchSensor142)
Shape143 = x3d.Shape()
Shape143.USE = "HAnimSiteShape"

HAnimSite141.children.append(Shape143)

HAnimSegment133.children.append(HAnimSite141)
HAnimSite144 = x3d.HAnimSite()
HAnimSite144.DEF = "hanim_l_medial_malleolus_pt"
HAnimSite144.name = "l_medial_malleolus_pt"
HAnimSite144.translation = [0.0890,0.0716,-0.0881]
TouchSensor145 = x3d.TouchSensor()
TouchSensor145.description = "HAnimSite l_medial_malleolus_pt"

HAnimSite144.children.append(TouchSensor145)
Shape146 = x3d.Shape()
Shape146.USE = "HAnimSiteShape"

HAnimSite144.children.append(Shape146)

HAnimSegment133.children.append(HAnimSite144)
HAnimSite147 = x3d.HAnimSite()
HAnimSite147.DEF = "hanim_l_tibiale_pt"
HAnimSite147.name = "l_tibiale_pt"
HAnimSite147.translation = [0,1,0]
TouchSensor148 = x3d.TouchSensor()
TouchSensor148.description = "HAnimSite l_tibiale_pt"

HAnimSite147.children.append(TouchSensor148)
Shape149 = x3d.Shape()
Shape149.USE = "HAnimSiteShape"

HAnimSite147.children.append(Shape149)

HAnimSegment133.children.append(HAnimSite147)

HAnimJoint132.children.append(HAnimSegment133)
HAnimJoint150 = x3d.HAnimJoint()
HAnimJoint150.DEF = "hanim_l_knee"
HAnimJoint150.name = "l_knee"
HAnimJoint150.center = [0.1040,0.4867,0.0308]
HAnimSegment151 = x3d.HAnimSegment()
HAnimSegment151.DEF = "hanim_l_calf"
HAnimSegment151.name = "l_calf"
Transform152 = x3d.Transform()
Transform152.translation = [0.1040,0.4867,0.0308]
Transform153 = x3d.Transform()
""" Empty Transform """
Shape154 = x3d.Shape()
Shape154.USE = "HAnimJointShape"

Transform153.children.append(Shape154)

Transform152.children.append(Transform153)

HAnimSegment151.children.append(Transform152)
Shape155 = x3d.Shape()
LineSet156 = x3d.LineSet()
LineSet156.vertexCount = [2]
Coordinate157 = x3d.Coordinate()

LineSet156.coord = Coordinate157
""" from l_knee to l_talocrural """
ColorRGBA158 = x3d.ColorRGBA()
ColorRGBA158.USE = "HAnimSegmentLineColorRGBA"

LineSet156.color = ColorRGBA158

Shape155.geometry = LineSet156

HAnimSegment151.children.append(Shape155)
HAnimSite159 = x3d.HAnimSite()
HAnimSite159.DEF = "hanim_l_calcaneus_posterior_pt"
HAnimSite159.name = "l_calcaneus_posterior_pt"
HAnimSite159.translation = [0.0974,0.0259,-0.1171]
TouchSensor160 = x3d.TouchSensor()
TouchSensor160.description = "HAnimSite l_calcaneus_posterior_pt"

HAnimSite159.children.append(TouchSensor160)
Shape161 = x3d.Shape()
Shape161.USE = "HAnimSiteShape"

HAnimSite159.children.append(Shape161)

HAnimSegment151.children.append(HAnimSite159)
HAnimSite162 = x3d.HAnimSite()
HAnimSite162.DEF = "hanim_l_sphyrion_pt"
HAnimSite162.name = "l_sphyrion_pt"
HAnimSite162.translation = [0.0890,0.0575,-0.0943]
TouchSensor163 = x3d.TouchSensor()
TouchSensor163.description = "HAnimSite l_sphyrion_pt"

HAnimSite162.children.append(TouchSensor163)
Shape164 = x3d.Shape()
Shape164.USE = "HAnimSiteShape"

HAnimSite162.children.append(Shape164)

HAnimSegment151.children.append(HAnimSite162)

HAnimJoint150.children.append(HAnimSegment151)
HAnimJoint165 = x3d.HAnimJoint()
HAnimJoint165.DEF = "hanim_l_talocrural"
HAnimJoint165.name = "l_talocrural"
HAnimJoint165.center = [0.1101,0.0656,-0.0736]
HAnimSegment166 = x3d.HAnimSegment()
HAnimSegment166.DEF = "hanim_l_talus"
HAnimSegment166.name = "l_talus"
Transform167 = x3d.Transform()
Transform167.scale = [0.15,0.15,0.15]
Transform167.translation = [0.08,0.06,-0.025]
Transform167.rotation = [1,0,0,-1.57]
""" Transform left foot """
Transform168 = x3d.Transform()
""" Empty Transform left foot """
Shape169 = x3d.Shape()
Shape169.USE = "HAnimJointShape"

Transform168.children.append(Shape169)

Transform167.children.append(Transform168)

HAnimSegment166.children.append(Transform167)
Shape170 = x3d.Shape()
LineSet171 = x3d.LineSet()
LineSet171.vertexCount = [2]
Coordinate172 = x3d.Coordinate()

LineSet171.coord = Coordinate172
""" from l_talocrural to l_talocalcaneonavicular """
ColorRGBA173 = x3d.ColorRGBA()
ColorRGBA173.USE = "HAnimSegmentLineColorRGBA"

LineSet171.color = ColorRGBA173

Shape170.geometry = LineSet171

HAnimSegment166.children.append(Shape170)
Shape174 = x3d.Shape()
LineSet175 = x3d.LineSet()
LineSet175.vertexCount = [2]
Coordinate176 = x3d.Coordinate()

LineSet175.coord = Coordinate176
""" from l_talocrural to l_calcaneocuboid """
ColorRGBA177 = x3d.ColorRGBA()
ColorRGBA177.USE = "HAnimSegmentLineColorRGBA"

LineSet175.color = ColorRGBA177

Shape174.geometry = LineSet175

HAnimSegment166.children.append(Shape174)

HAnimJoint165.children.append(HAnimSegment166)
HAnimJoint178 = x3d.HAnimJoint()
HAnimJoint178.DEF = "hanim_l_talocalcaneonavicular"
HAnimJoint178.name = "l_talocalcaneonavicular"
HAnimJoint178.center = [0,1,0]
HAnimSegment179 = x3d.HAnimSegment()
HAnimSegment179.DEF = "hanim_l_navicular"
HAnimSegment179.name = "l_navicular"
Transform180 = x3d.Transform()
Transform180.translation = [0,1,0]
Transform181 = x3d.Transform()
""" Empty Transform """
Shape182 = x3d.Shape()
Shape182.USE = "HAnimJointShape"

Transform181.children.append(Shape182)

Transform180.children.append(Transform181)

HAnimSegment179.children.append(Transform180)
Shape183 = x3d.Shape()
LineSet184 = x3d.LineSet()
LineSet184.vertexCount = [1]
Coordinate185 = x3d.Coordinate()

LineSet184.coord = Coordinate185
""" from l_talocalcaneonavicular to l_cuneonavicular_1 """
ColorRGBA186 = x3d.ColorRGBA()
ColorRGBA186.USE = "HAnimSegmentLineColorRGBA"

LineSet184.color = ColorRGBA186

Shape183.geometry = LineSet184

HAnimSegment179.children.append(Shape183)
Shape187 = x3d.Shape()
LineSet188 = x3d.LineSet()
LineSet188.vertexCount = [1]
Coordinate189 = x3d.Coordinate()

LineSet188.coord = Coordinate189
""" from l_talocalcaneonavicular to l_cuneonavicular_2 """
ColorRGBA190 = x3d.ColorRGBA()
ColorRGBA190.USE = "HAnimSegmentLineColorRGBA"

LineSet188.color = ColorRGBA190

Shape187.geometry = LineSet188

HAnimSegment179.children.append(Shape187)
Shape191 = x3d.Shape()
LineSet192 = x3d.LineSet()
LineSet192.vertexCount = [1]
Coordinate193 = x3d.Coordinate()

LineSet192.coord = Coordinate193
""" from l_talocalcaneonavicular to l_cuneonavicular_3 """
ColorRGBA194 = x3d.ColorRGBA()
ColorRGBA194.USE = "HAnimSegmentLineColorRGBA"

LineSet192.color = ColorRGBA194

Shape191.geometry = LineSet192

HAnimSegment179.children.append(Shape191)

HAnimJoint178.children.append(HAnimSegment179)
HAnimJoint195 = x3d.HAnimJoint()
HAnimJoint195.DEF = "hanim_l_cuneonavicular_1"
HAnimJoint195.name = "l_cuneonavicular_1"
HAnimJoint195.center = [0,1,0]
HAnimSegment196 = x3d.HAnimSegment()
HAnimSegment196.DEF = "hanim_l_cuneiform_1"
HAnimSegment196.name = "l_cuneiform_1"
Transform197 = x3d.Transform()
Transform197.translation = [0,1,0]
Transform198 = x3d.Transform()
""" Empty Transform """
Shape199 = x3d.Shape()
Shape199.USE = "HAnimJointShape"

Transform198.children.append(Shape199)

Transform197.children.append(Transform198)

HAnimSegment196.children.append(Transform197)
Shape200 = x3d.Shape()
LineSet201 = x3d.LineSet()
LineSet201.vertexCount = [1]
Coordinate202 = x3d.Coordinate()

LineSet201.coord = Coordinate202
""" from l_cuneonavicular_1 to l_tarsometatarsal_1 """
ColorRGBA203 = x3d.ColorRGBA()
ColorRGBA203.USE = "HAnimSegmentLineColorRGBA"

LineSet201.color = ColorRGBA203

Shape200.geometry = LineSet201

HAnimSegment196.children.append(Shape200)

HAnimJoint195.children.append(HAnimSegment196)
HAnimJoint204 = x3d.HAnimJoint()
HAnimJoint204.DEF = "hanim_l_tarsometatarsal_1"
HAnimJoint204.name = "l_tarsometatarsal_1"
HAnimJoint204.center = [0,1,0]
HAnimSegment205 = x3d.HAnimSegment()
HAnimSegment205.DEF = "hanim_l_metatarsal_1"
HAnimSegment205.name = "l_metatarsal_1"
Transform206 = x3d.Transform()
Transform206.translation = [0,1,0]
Transform207 = x3d.Transform()
""" Empty Transform """
Shape208 = x3d.Shape()
Shape208.USE = "HAnimJointShape"

Transform207.children.append(Shape208)

Transform206.children.append(Transform207)

HAnimSegment205.children.append(Transform206)
Shape209 = x3d.Shape()
LineSet210 = x3d.LineSet()
LineSet210.vertexCount = [1]
Coordinate211 = x3d.Coordinate()

LineSet210.coord = Coordinate211
""" from l_tarsometatarsal_1 to l_metatarsophalangeal_1 """
ColorRGBA212 = x3d.ColorRGBA()
ColorRGBA212.USE = "HAnimSegmentLineColorRGBA"

LineSet210.color = ColorRGBA212

Shape209.geometry = LineSet210

HAnimSegment205.children.append(Shape209)
HAnimSite213 = x3d.HAnimSite()
HAnimSite213.DEF = "hanim_l_metatarsal_phalanx_1_pt"
HAnimSite213.name = "l_metatarsal_phalanx_1_pt"
HAnimSite213.translation = [0,1,0]
TouchSensor214 = x3d.TouchSensor()
TouchSensor214.description = "HAnimSite l_metatarsal_phalanx_1_pt"

HAnimSite213.children.append(TouchSensor214)
Shape215 = x3d.Shape()
Shape215.USE = "HAnimSiteShape"

HAnimSite213.children.append(Shape215)

HAnimSegment205.children.append(HAnimSite213)

HAnimJoint204.children.append(HAnimSegment205)
HAnimJoint216 = x3d.HAnimJoint()
HAnimJoint216.DEF = "hanim_l_metatarsophalangeal_1"
HAnimJoint216.name = "l_metatarsophalangeal_1"
HAnimJoint216.center = [0,1,0]
HAnimSegment217 = x3d.HAnimSegment()
HAnimSegment217.DEF = "hanim_l_tarsal_proximal_phalanx_1"
HAnimSegment217.name = "l_tarsal_proximal_phalanx_1"
Transform218 = x3d.Transform()
Transform218.translation = [0,1,0]
Transform219 = x3d.Transform()
""" Empty Transform """
Shape220 = x3d.Shape()
Shape220.USE = "HAnimJointShape"

Transform219.children.append(Shape220)

Transform218.children.append(Transform219)

HAnimSegment217.children.append(Transform218)
Shape221 = x3d.Shape()
LineSet222 = x3d.LineSet()
LineSet222.vertexCount = [1]
Coordinate223 = x3d.Coordinate()

LineSet222.coord = Coordinate223
""" from l_metatarsophalangeal_1 to l_tarsal_interphalangeal_1 """
ColorRGBA224 = x3d.ColorRGBA()
ColorRGBA224.USE = "HAnimSegmentLineColorRGBA"

LineSet222.color = ColorRGBA224

Shape221.geometry = LineSet222

HAnimSegment217.children.append(Shape221)
HAnimSite225 = x3d.HAnimSite()
HAnimSite225.DEF = "hanim_l_tarsal_distal_phalanx_1_tip"
HAnimSite225.name = "l_tarsal_distal_phalanx_1_tip"
HAnimSite225.translation = [0,1,0]
TouchSensor226 = x3d.TouchSensor()
TouchSensor226.description = "HAnimSite l_tarsal_distal_phalanx_1_tip"

HAnimSite225.children.append(TouchSensor226)
Shape227 = x3d.Shape()
Shape227.USE = "HAnimSiteShape"

HAnimSite225.children.append(Shape227)

HAnimSegment217.children.append(HAnimSite225)

HAnimJoint216.children.append(HAnimSegment217)
HAnimJoint228 = x3d.HAnimJoint()
HAnimJoint228.DEF = "hanim_l_tarsal_interphalangeal_1"
HAnimJoint228.name = "l_tarsal_interphalangeal_1"
HAnimJoint228.center = [0,1,0]

HAnimJoint216.children.append(HAnimJoint228)

HAnimJoint204.children.append(HAnimJoint216)

HAnimJoint195.children.append(HAnimJoint204)

HAnimJoint178.children.append(HAnimJoint195)
HAnimJoint229 = x3d.HAnimJoint()
HAnimJoint229.DEF = "hanim_l_cuneonavicular_2"
HAnimJoint229.name = "l_cuneonavicular_2"
HAnimJoint229.center = [0,1,0]
HAnimSegment230 = x3d.HAnimSegment()
HAnimSegment230.DEF = "hanim_l_cuneiform_2"
HAnimSegment230.name = "l_cuneiform_2"
Transform231 = x3d.Transform()
Transform231.translation = [0,1,0]
Transform232 = x3d.Transform()
""" Empty Transform """
Shape233 = x3d.Shape()
Shape233.USE = "HAnimJointShape"

Transform232.children.append(Shape233)

Transform231.children.append(Transform232)

HAnimSegment230.children.append(Transform231)
Shape234 = x3d.Shape()
LineSet235 = x3d.LineSet()
LineSet235.vertexCount = [1]
Coordinate236 = x3d.Coordinate()

LineSet235.coord = Coordinate236
""" from l_cuneonavicular_2 to l_tarsometatarsal_2 """
ColorRGBA237 = x3d.ColorRGBA()
ColorRGBA237.USE = "HAnimSegmentLineColorRGBA"

LineSet235.color = ColorRGBA237

Shape234.geometry = LineSet235

HAnimSegment230.children.append(Shape234)

HAnimJoint229.children.append(HAnimSegment230)
HAnimJoint238 = x3d.HAnimJoint()
HAnimJoint238.DEF = "hanim_l_tarsometatarsal_2"
HAnimJoint238.name = "l_tarsometatarsal_2"
HAnimJoint238.center = [0,1,0]
HAnimSegment239 = x3d.HAnimSegment()
HAnimSegment239.DEF = "hanim_l_metatarsal_2"
HAnimSegment239.name = "l_metatarsal_2"
Transform240 = x3d.Transform()
Transform240.translation = [0,1,0]
Transform241 = x3d.Transform()
""" Empty Transform """
Shape242 = x3d.Shape()
Shape242.USE = "HAnimJointShape"

Transform241.children.append(Shape242)

Transform240.children.append(Transform241)

HAnimSegment239.children.append(Transform240)
Shape243 = x3d.Shape()
LineSet244 = x3d.LineSet()
LineSet244.vertexCount = [1]
Coordinate245 = x3d.Coordinate()

LineSet244.coord = Coordinate245
""" from l_tarsometatarsal_2 to l_metatarsophalangeal_2 """
ColorRGBA246 = x3d.ColorRGBA()
ColorRGBA246.USE = "HAnimSegmentLineColorRGBA"

LineSet244.color = ColorRGBA246

Shape243.geometry = LineSet244

HAnimSegment239.children.append(Shape243)

HAnimJoint238.children.append(HAnimSegment239)
HAnimJoint247 = x3d.HAnimJoint()
HAnimJoint247.DEF = "hanim_l_metatarsophalangeal_2"
HAnimJoint247.name = "l_metatarsophalangeal_2"
HAnimJoint247.center = [0,1,0]
HAnimSegment248 = x3d.HAnimSegment()
HAnimSegment248.DEF = "hanim_l_tarsal_proximal_phalanx_2"
HAnimSegment248.name = "l_tarsal_proximal_phalanx_2"
Transform249 = x3d.Transform()
Transform249.translation = [0,1,0]
Transform250 = x3d.Transform()
""" Empty Transform """
Shape251 = x3d.Shape()
Shape251.USE = "HAnimJointShape"

Transform250.children.append(Shape251)

Transform249.children.append(Transform250)

HAnimSegment248.children.append(Transform249)
Shape252 = x3d.Shape()
LineSet253 = x3d.LineSet()
LineSet253.vertexCount = [1]
Coordinate254 = x3d.Coordinate()

LineSet253.coord = Coordinate254
""" from l_metatarsophalangeal_2 to l_tarsal_proximal_interphalangeal_2 """
ColorRGBA255 = x3d.ColorRGBA()
ColorRGBA255.USE = "HAnimSegmentLineColorRGBA"

LineSet253.color = ColorRGBA255

Shape252.geometry = LineSet253

HAnimSegment248.children.append(Shape252)

HAnimJoint247.children.append(HAnimSegment248)
HAnimJoint256 = x3d.HAnimJoint()
HAnimJoint256.DEF = "hanim_l_tarsal_proximal_interphalangeal_2"
HAnimJoint256.name = "l_tarsal_proximal_interphalangeal_2"
HAnimJoint256.center = [0,1,0]
HAnimSegment257 = x3d.HAnimSegment()
HAnimSegment257.DEF = "hanim_l_tarsal_middle_phalanx_2"
HAnimSegment257.name = "l_tarsal_middle_phalanx_2"
Transform258 = x3d.Transform()
Transform258.translation = [0,1,0]
Transform259 = x3d.Transform()
""" Empty Transform """
Shape260 = x3d.Shape()
Shape260.USE = "HAnimJointShape"

Transform259.children.append(Shape260)

Transform258.children.append(Transform259)

HAnimSegment257.children.append(Transform258)
Shape261 = x3d.Shape()
LineSet262 = x3d.LineSet()
LineSet262.vertexCount = [1]
Coordinate263 = x3d.Coordinate()

LineSet262.coord = Coordinate263
""" from l_tarsal_proximal_interphalangeal_2 to l_tarsal_distal_interphalangeal_2 """
ColorRGBA264 = x3d.ColorRGBA()
ColorRGBA264.USE = "HAnimSegmentLineColorRGBA"

LineSet262.color = ColorRGBA264

Shape261.geometry = LineSet262

HAnimSegment257.children.append(Shape261)
HAnimSite265 = x3d.HAnimSite()
HAnimSite265.DEF = "hanim_l_tarsal_distal_phalanx_2_tip"
HAnimSite265.name = "l_tarsal_distal_phalanx_2_tip"
HAnimSite265.translation = [0.1195,0.0079,0.1433]
TouchSensor266 = x3d.TouchSensor()
TouchSensor266.description = "HAnimSite l_tarsal_distal_phalanx_2_tip"

HAnimSite265.children.append(TouchSensor266)
Shape267 = x3d.Shape()
Shape267.USE = "HAnimSiteShape"

HAnimSite265.children.append(Shape267)

HAnimSegment257.children.append(HAnimSite265)

HAnimJoint256.children.append(HAnimSegment257)
HAnimJoint268 = x3d.HAnimJoint()
HAnimJoint268.DEF = "hanim_l_tarsal_distal_interphalangeal_2"
HAnimJoint268.name = "l_tarsal_distal_interphalangeal_2"
HAnimJoint268.center = [0,1,0]

HAnimJoint256.children.append(HAnimJoint268)

HAnimJoint247.children.append(HAnimJoint256)

HAnimJoint238.children.append(HAnimJoint247)

HAnimJoint229.children.append(HAnimJoint238)

HAnimJoint178.children.append(HAnimJoint229)
HAnimJoint269 = x3d.HAnimJoint()
HAnimJoint269.DEF = "hanim_l_cuneonavicular_3"
HAnimJoint269.name = "l_cuneonavicular_3"
HAnimJoint269.center = [0,1,0]
HAnimSegment270 = x3d.HAnimSegment()
HAnimSegment270.DEF = "hanim_l_cuneiform_3"
HAnimSegment270.name = "l_cuneiform_3"
Transform271 = x3d.Transform()
Transform271.translation = [0,1,0]
Transform272 = x3d.Transform()
""" Empty Transform """
Shape273 = x3d.Shape()
Shape273.USE = "HAnimJointShape"

Transform272.children.append(Shape273)

Transform271.children.append(Transform272)

HAnimSegment270.children.append(Transform271)
Shape274 = x3d.Shape()
LineSet275 = x3d.LineSet()
LineSet275.vertexCount = [1]
Coordinate276 = x3d.Coordinate()

LineSet275.coord = Coordinate276
""" from l_cuneonavicular_3 to l_tarsometatarsal_3 """
ColorRGBA277 = x3d.ColorRGBA()
ColorRGBA277.USE = "HAnimSegmentLineColorRGBA"

LineSet275.color = ColorRGBA277

Shape274.geometry = LineSet275

HAnimSegment270.children.append(Shape274)

HAnimJoint269.children.append(HAnimSegment270)
HAnimJoint278 = x3d.HAnimJoint()
HAnimJoint278.DEF = "hanim_l_tarsometatarsal_3"
HAnimJoint278.name = "l_tarsometatarsal_3"
HAnimJoint278.center = [0,1,0]
HAnimSegment279 = x3d.HAnimSegment()
HAnimSegment279.DEF = "hanim_l_metatarsal_3"
HAnimSegment279.name = "l_metatarsal_3"
Transform280 = x3d.Transform()
Transform280.translation = [0,1,0]
Transform281 = x3d.Transform()
""" Empty Transform """
Shape282 = x3d.Shape()
Shape282.USE = "HAnimJointShape"

Transform281.children.append(Shape282)

Transform280.children.append(Transform281)

HAnimSegment279.children.append(Transform280)
Shape283 = x3d.Shape()
LineSet284 = x3d.LineSet()
LineSet284.vertexCount = [1]
Coordinate285 = x3d.Coordinate()

LineSet284.coord = Coordinate285
""" from l_tarsometatarsal_3 to l_metatarsophalangeal_3 """
ColorRGBA286 = x3d.ColorRGBA()
ColorRGBA286.USE = "HAnimSegmentLineColorRGBA"

LineSet284.color = ColorRGBA286

Shape283.geometry = LineSet284

HAnimSegment279.children.append(Shape283)

HAnimJoint278.children.append(HAnimSegment279)
HAnimJoint287 = x3d.HAnimJoint()
HAnimJoint287.DEF = "hanim_l_metatarsophalangeal_3"
HAnimJoint287.name = "l_metatarsophalangeal_3"
HAnimJoint287.center = [0,1,0]
HAnimSegment288 = x3d.HAnimSegment()
HAnimSegment288.DEF = "hanim_l_tarsal_proximal_phalanx_3"
HAnimSegment288.name = "l_tarsal_proximal_phalanx_3"
Transform289 = x3d.Transform()
Transform289.translation = [0,1,0]
Transform290 = x3d.Transform()
""" Empty Transform """
Shape291 = x3d.Shape()
Shape291.USE = "HAnimJointShape"

Transform290.children.append(Shape291)

Transform289.children.append(Transform290)

HAnimSegment288.children.append(Transform289)
Shape292 = x3d.Shape()
LineSet293 = x3d.LineSet()
LineSet293.vertexCount = [1]
Coordinate294 = x3d.Coordinate()

LineSet293.coord = Coordinate294
""" from l_metatarsophalangeal_3 to l_tarsal_proximal_interphalangeal_3 """
ColorRGBA295 = x3d.ColorRGBA()
ColorRGBA295.USE = "HAnimSegmentLineColorRGBA"

LineSet293.color = ColorRGBA295

Shape292.geometry = LineSet293

HAnimSegment288.children.append(Shape292)

HAnimJoint287.children.append(HAnimSegment288)
HAnimJoint296 = x3d.HAnimJoint()
HAnimJoint296.DEF = "hanim_l_tarsal_proximal_interphalangeal_3"
HAnimJoint296.name = "l_tarsal_proximal_interphalangeal_3"
HAnimJoint296.center = [0,1,0]
HAnimSegment297 = x3d.HAnimSegment()
HAnimSegment297.DEF = "hanim_l_tarsal_middle_phalanx_3"
HAnimSegment297.name = "l_tarsal_middle_phalanx_3"
Transform298 = x3d.Transform()
Transform298.translation = [0,1,0]
Transform299 = x3d.Transform()
""" Empty Transform """
Shape300 = x3d.Shape()
Shape300.USE = "HAnimJointShape"

Transform299.children.append(Shape300)

Transform298.children.append(Transform299)

HAnimSegment297.children.append(Transform298)
Shape301 = x3d.Shape()
LineSet302 = x3d.LineSet()
LineSet302.vertexCount = [1]
Coordinate303 = x3d.Coordinate()

LineSet302.coord = Coordinate303
""" from l_tarsal_proximal_interphalangeal_3 to l_tarsal_distal_interphalangeal_3 """
ColorRGBA304 = x3d.ColorRGBA()
ColorRGBA304.USE = "HAnimSegmentLineColorRGBA"

LineSet302.color = ColorRGBA304

Shape301.geometry = LineSet302

HAnimSegment297.children.append(Shape301)
HAnimSite305 = x3d.HAnimSite()
HAnimSite305.DEF = "hanim_l_tarsal_distal_phalanx_3_tip"
HAnimSite305.name = "l_tarsal_distal_phalanx_3_tip"
HAnimSite305.translation = [0,1,0]
TouchSensor306 = x3d.TouchSensor()
TouchSensor306.description = "HAnimSite l_tarsal_distal_phalanx_3_tip"

HAnimSite305.children.append(TouchSensor306)
Shape307 = x3d.Shape()
Shape307.USE = "HAnimSiteShape"

HAnimSite305.children.append(Shape307)

HAnimSegment297.children.append(HAnimSite305)

HAnimJoint296.children.append(HAnimSegment297)
HAnimJoint308 = x3d.HAnimJoint()
HAnimJoint308.DEF = "hanim_l_tarsal_distal_interphalangeal_3"
HAnimJoint308.name = "l_tarsal_distal_interphalangeal_3"
HAnimJoint308.center = [0,1,0]

HAnimJoint296.children.append(HAnimJoint308)

HAnimJoint287.children.append(HAnimJoint296)

HAnimJoint278.children.append(HAnimJoint287)

HAnimJoint269.children.append(HAnimJoint278)

HAnimJoint178.children.append(HAnimJoint269)

HAnimJoint165.children.append(HAnimJoint178)
HAnimJoint309 = x3d.HAnimJoint()
HAnimJoint309.DEF = "hanim_l_calcaneocuboid"
HAnimJoint309.name = "l_calcaneocuboid"
HAnimJoint309.center = [0,1,0]
HAnimSegment310 = x3d.HAnimSegment()
HAnimSegment310.DEF = "hanim_l_calcaneus"
HAnimSegment310.name = "l_calcaneus"
Transform311 = x3d.Transform()
Transform311.translation = [0,1,0]
Transform312 = x3d.Transform()
""" Empty Transform """
Shape313 = x3d.Shape()
Shape313.USE = "HAnimJointShape"

Transform312.children.append(Shape313)

Transform311.children.append(Transform312)

HAnimSegment310.children.append(Transform311)
Shape314 = x3d.Shape()
LineSet315 = x3d.LineSet()
LineSet315.vertexCount = [1]
Coordinate316 = x3d.Coordinate()

LineSet315.coord = Coordinate316
""" from l_calcaneocuboid to l_transversetarsal """
ColorRGBA317 = x3d.ColorRGBA()
ColorRGBA317.USE = "HAnimSegmentLineColorRGBA"

LineSet315.color = ColorRGBA317

Shape314.geometry = LineSet315

HAnimSegment310.children.append(Shape314)

HAnimJoint309.children.append(HAnimSegment310)
HAnimJoint318 = x3d.HAnimJoint()
HAnimJoint318.DEF = "hanim_l_transversetarsal"
HAnimJoint318.name = "l_transversetarsal"
HAnimJoint318.center = [0,1,0]
HAnimSegment319 = x3d.HAnimSegment()
HAnimSegment319.DEF = "hanim_l_cuboid"
HAnimSegment319.name = "l_cuboid"
Transform320 = x3d.Transform()
Transform320.translation = [0,1,0]
Transform321 = x3d.Transform()
""" Empty Transform """
Shape322 = x3d.Shape()
Shape322.USE = "HAnimJointShape"

Transform321.children.append(Shape322)

Transform320.children.append(Transform321)

HAnimSegment319.children.append(Transform320)
Shape323 = x3d.Shape()
LineSet324 = x3d.LineSet()
LineSet324.vertexCount = [1]
Coordinate325 = x3d.Coordinate()

LineSet324.coord = Coordinate325
""" from l_transversetarsal to l_tarsometatarsal_4 """
ColorRGBA326 = x3d.ColorRGBA()
ColorRGBA326.USE = "HAnimSegmentLineColorRGBA"

LineSet324.color = ColorRGBA326

Shape323.geometry = LineSet324

HAnimSegment319.children.append(Shape323)
Shape327 = x3d.Shape()
LineSet328 = x3d.LineSet()
LineSet328.vertexCount = [1]
Coordinate329 = x3d.Coordinate()

LineSet328.coord = Coordinate329
""" from l_transversetarsal to l_tarsometatarsal_5 """
ColorRGBA330 = x3d.ColorRGBA()
ColorRGBA330.USE = "HAnimSegmentLineColorRGBA"

LineSet328.color = ColorRGBA330

Shape327.geometry = LineSet328

HAnimSegment319.children.append(Shape327)

HAnimJoint318.children.append(HAnimSegment319)
HAnimJoint331 = x3d.HAnimJoint()
HAnimJoint331.DEF = "hanim_l_tarsometatarsal_4"
HAnimJoint331.name = "l_tarsometatarsal_4"
HAnimJoint331.center = [0,1,0]
HAnimSegment332 = x3d.HAnimSegment()
HAnimSegment332.DEF = "hanim_l_metatarsal_4"
HAnimSegment332.name = "l_metatarsal_4"
Transform333 = x3d.Transform()
Transform333.translation = [0,1,0]
Transform334 = x3d.Transform()
""" Empty Transform """
Shape335 = x3d.Shape()
Shape335.USE = "HAnimJointShape"

Transform334.children.append(Shape335)

Transform333.children.append(Transform334)

HAnimSegment332.children.append(Transform333)
Shape336 = x3d.Shape()
LineSet337 = x3d.LineSet()
LineSet337.vertexCount = [1]
Coordinate338 = x3d.Coordinate()

LineSet337.coord = Coordinate338
""" from l_tarsometatarsal_4 to l_metatarsophalangeal_4 """
ColorRGBA339 = x3d.ColorRGBA()
ColorRGBA339.USE = "HAnimSegmentLineColorRGBA"

LineSet337.color = ColorRGBA339

Shape336.geometry = LineSet337

HAnimSegment332.children.append(Shape336)

HAnimJoint331.children.append(HAnimSegment332)
HAnimJoint340 = x3d.HAnimJoint()
HAnimJoint340.DEF = "hanim_l_metatarsophalangeal_4"
HAnimJoint340.name = "l_metatarsophalangeal_4"
HAnimJoint340.center = [0,1,0]
HAnimSegment341 = x3d.HAnimSegment()
HAnimSegment341.DEF = "hanim_l_tarsal_proximal_phalanx_4"
HAnimSegment341.name = "l_tarsal_proximal_phalanx_4"
Transform342 = x3d.Transform()
Transform342.translation = [0,1,0]
Transform343 = x3d.Transform()
""" Empty Transform """
Shape344 = x3d.Shape()
Shape344.USE = "HAnimJointShape"

Transform343.children.append(Shape344)

Transform342.children.append(Transform343)

HAnimSegment341.children.append(Transform342)
Shape345 = x3d.Shape()
LineSet346 = x3d.LineSet()
LineSet346.vertexCount = [1]
Coordinate347 = x3d.Coordinate()

LineSet346.coord = Coordinate347
""" from l_metatarsophalangeal_4 to l_tarsal_proximal_interphalangeal_4 """
ColorRGBA348 = x3d.ColorRGBA()
ColorRGBA348.USE = "HAnimSegmentLineColorRGBA"

LineSet346.color = ColorRGBA348

Shape345.geometry = LineSet346

HAnimSegment341.children.append(Shape345)

HAnimJoint340.children.append(HAnimSegment341)
HAnimJoint349 = x3d.HAnimJoint()
HAnimJoint349.DEF = "hanim_l_tarsal_proximal_interphalangeal_4"
HAnimJoint349.name = "l_tarsal_proximal_interphalangeal_4"
HAnimJoint349.center = [0,1,0]
HAnimSegment350 = x3d.HAnimSegment()
HAnimSegment350.DEF = "hanim_l_tarsal_middle_phalanx_4"
HAnimSegment350.name = "l_tarsal_middle_phalanx_4"
Transform351 = x3d.Transform()
Transform351.translation = [0,1,0]
Transform352 = x3d.Transform()
""" Empty Transform """
Shape353 = x3d.Shape()
Shape353.USE = "HAnimJointShape"

Transform352.children.append(Shape353)

Transform351.children.append(Transform352)

HAnimSegment350.children.append(Transform351)
Shape354 = x3d.Shape()
LineSet355 = x3d.LineSet()
LineSet355.vertexCount = [1]
Coordinate356 = x3d.Coordinate()

LineSet355.coord = Coordinate356
""" from l_tarsal_proximal_interphalangeal_4 to l_tarsal_distal_interphalangeal_4 """
ColorRGBA357 = x3d.ColorRGBA()
ColorRGBA357.USE = "HAnimSegmentLineColorRGBA"

LineSet355.color = ColorRGBA357

Shape354.geometry = LineSet355

HAnimSegment350.children.append(Shape354)
HAnimSite358 = x3d.HAnimSite()
HAnimSite358.DEF = "hanim_l_tarsal_distal_phalanx_4_tip"
HAnimSite358.name = "l_tarsal_distal_phalanx_4_tip"
HAnimSite358.translation = [0,1,0]
TouchSensor359 = x3d.TouchSensor()
TouchSensor359.description = "HAnimSite l_tarsal_distal_phalanx_4_tip"

HAnimSite358.children.append(TouchSensor359)
Shape360 = x3d.Shape()
Shape360.USE = "HAnimSiteShape"

HAnimSite358.children.append(Shape360)

HAnimSegment350.children.append(HAnimSite358)

HAnimJoint349.children.append(HAnimSegment350)
HAnimJoint361 = x3d.HAnimJoint()
HAnimJoint361.DEF = "hanim_l_tarsal_distal_interphalangeal_4"
HAnimJoint361.name = "l_tarsal_distal_interphalangeal_4"
HAnimJoint361.center = [0,1,0]

HAnimJoint349.children.append(HAnimJoint361)

HAnimJoint340.children.append(HAnimJoint349)

HAnimJoint331.children.append(HAnimJoint340)

HAnimJoint318.children.append(HAnimJoint331)
HAnimJoint362 = x3d.HAnimJoint()
HAnimJoint362.DEF = "hanim_l_tarsometatarsal_5"
HAnimJoint362.name = "l_tarsometatarsal_5"
HAnimJoint362.center = [0,1,0]
HAnimSegment363 = x3d.HAnimSegment()
HAnimSegment363.DEF = "hanim_l_metatarsal_5"
HAnimSegment363.name = "l_metatarsal_5"
Transform364 = x3d.Transform()
Transform364.translation = [0,1,0]
Transform365 = x3d.Transform()
""" Empty Transform """
Shape366 = x3d.Shape()
Shape366.USE = "HAnimJointShape"

Transform365.children.append(Shape366)

Transform364.children.append(Transform365)

HAnimSegment363.children.append(Transform364)
Shape367 = x3d.Shape()
LineSet368 = x3d.LineSet()
LineSet368.vertexCount = [1]
Coordinate369 = x3d.Coordinate()

LineSet368.coord = Coordinate369
""" from l_tarsometatarsal_5 to l_metatarsophalangeal_5 """
ColorRGBA370 = x3d.ColorRGBA()
ColorRGBA370.USE = "HAnimSegmentLineColorRGBA"

LineSet368.color = ColorRGBA370

Shape367.geometry = LineSet368

HAnimSegment363.children.append(Shape367)
HAnimSite371 = x3d.HAnimSite()
HAnimSite371.DEF = "hanim_l_metatarsal_phalanx_5_pt"
HAnimSite371.name = "l_metatarsal_phalanx_5_pt"
HAnimSite371.translation = [0,1,0]
TouchSensor372 = x3d.TouchSensor()
TouchSensor372.description = "HAnimSite l_metatarsal_phalanx_5_pt"

HAnimSite371.children.append(TouchSensor372)
Shape373 = x3d.Shape()
Shape373.USE = "HAnimSiteShape"

HAnimSite371.children.append(Shape373)

HAnimSegment363.children.append(HAnimSite371)

HAnimJoint362.children.append(HAnimSegment363)
HAnimJoint374 = x3d.HAnimJoint()
HAnimJoint374.DEF = "hanim_l_metatarsophalangeal_5"
HAnimJoint374.name = "l_metatarsophalangeal_5"
HAnimJoint374.center = [0,1,0]
HAnimSegment375 = x3d.HAnimSegment()
HAnimSegment375.DEF = "hanim_l_tarsal_proximal_phalanx_5"
HAnimSegment375.name = "l_tarsal_proximal_phalanx_5"
Transform376 = x3d.Transform()
Transform376.translation = [0,1,0]
Transform377 = x3d.Transform()
""" Empty Transform """
Shape378 = x3d.Shape()
Shape378.USE = "HAnimJointShape"

Transform377.children.append(Shape378)

Transform376.children.append(Transform377)

HAnimSegment375.children.append(Transform376)
Shape379 = x3d.Shape()
LineSet380 = x3d.LineSet()
LineSet380.vertexCount = [1]
Coordinate381 = x3d.Coordinate()

LineSet380.coord = Coordinate381
""" from l_metatarsophalangeal_5 to l_tarsal_proximal_interphalangeal_5 """
ColorRGBA382 = x3d.ColorRGBA()
ColorRGBA382.USE = "HAnimSegmentLineColorRGBA"

LineSet380.color = ColorRGBA382

Shape379.geometry = LineSet380

HAnimSegment375.children.append(Shape379)

HAnimJoint374.children.append(HAnimSegment375)
HAnimJoint383 = x3d.HAnimJoint()
HAnimJoint383.DEF = "hanim_l_tarsal_proximal_interphalangeal_5"
HAnimJoint383.name = "l_tarsal_proximal_interphalangeal_5"
HAnimJoint383.center = [0,1,0]
HAnimSegment384 = x3d.HAnimSegment()
HAnimSegment384.DEF = "hanim_l_tarsal_middle_phalanx_5"
HAnimSegment384.name = "l_tarsal_middle_phalanx_5"
Transform385 = x3d.Transform()
Transform385.translation = [0,1,0]
Transform386 = x3d.Transform()
""" Empty Transform """
Shape387 = x3d.Shape()
Shape387.USE = "HAnimJointShape"

Transform386.children.append(Shape387)

Transform385.children.append(Transform386)

HAnimSegment384.children.append(Transform385)
Shape388 = x3d.Shape()
LineSet389 = x3d.LineSet()
LineSet389.vertexCount = [1]
Coordinate390 = x3d.Coordinate()

LineSet389.coord = Coordinate390
""" from l_tarsal_proximal_interphalangeal_5 to l_tarsal_distal_interphalangeal_5 """
ColorRGBA391 = x3d.ColorRGBA()
ColorRGBA391.USE = "HAnimSegmentLineColorRGBA"

LineSet389.color = ColorRGBA391

Shape388.geometry = LineSet389

HAnimSegment384.children.append(Shape388)
HAnimSite392 = x3d.HAnimSite()
HAnimSite392.DEF = "hanim_l_tarsal_distal_phalanx_5_tip"
HAnimSite392.name = "l_tarsal_distal_phalanx_5_tip"
HAnimSite392.translation = [0,1,0]
TouchSensor393 = x3d.TouchSensor()
TouchSensor393.description = "HAnimSite l_tarsal_distal_phalanx_5_tip"

HAnimSite392.children.append(TouchSensor393)
Shape394 = x3d.Shape()
Shape394.USE = "HAnimSiteShape"

HAnimSite392.children.append(Shape394)

HAnimSegment384.children.append(HAnimSite392)

HAnimJoint383.children.append(HAnimSegment384)
HAnimJoint395 = x3d.HAnimJoint()
HAnimJoint395.DEF = "hanim_l_tarsal_distal_interphalangeal_5"
HAnimJoint395.name = "l_tarsal_distal_interphalangeal_5"
HAnimJoint395.center = [0,1,0]

HAnimJoint383.children.append(HAnimJoint395)

HAnimJoint374.children.append(HAnimJoint383)

HAnimJoint362.children.append(HAnimJoint374)

HAnimJoint318.children.append(HAnimJoint362)

HAnimJoint309.children.append(HAnimJoint318)

HAnimJoint165.children.append(HAnimJoint309)

HAnimJoint150.children.append(HAnimJoint165)

HAnimJoint132.children.append(HAnimJoint150)

HAnimJoint95.children.append(HAnimJoint132)
HAnimJoint396 = x3d.HAnimJoint()
HAnimJoint396.DEF = "hanim_r_hip"
HAnimJoint396.name = "r_hip"
HAnimJoint396.center = [-0.0950,0.9171,0.0029]
HAnimSegment397 = x3d.HAnimSegment()
HAnimSegment397.DEF = "hanim_r_thigh"
HAnimSegment397.name = "r_thigh"
Transform398 = x3d.Transform()
Transform398.translation = [-0.0950,0.9171,0.0029]
Transform399 = x3d.Transform()
""" Empty Transform """
Shape400 = x3d.Shape()
Shape400.USE = "HAnimJointShape"

Transform399.children.append(Shape400)

Transform398.children.append(Transform399)

HAnimSegment397.children.append(Transform398)
Shape401 = x3d.Shape()
LineSet402 = x3d.LineSet()
LineSet402.vertexCount = [2]
Coordinate403 = x3d.Coordinate()

LineSet402.coord = Coordinate403
""" from r_hip to r_knee """
ColorRGBA404 = x3d.ColorRGBA()
ColorRGBA404.USE = "HAnimSegmentLineColorRGBA"

LineSet402.color = ColorRGBA404

Shape401.geometry = LineSet402

HAnimSegment397.children.append(Shape401)
HAnimSite405 = x3d.HAnimSite()
HAnimSite405.DEF = "hanim_r_lateral_malleolus_pt"
HAnimSite405.name = "r_lateral_malleolus_pt"
HAnimSite405.translation = [-0.1006,0.0658,-0.1075]
TouchSensor406 = x3d.TouchSensor()
TouchSensor406.description = "HAnimSite r_lateral_malleolus_pt"

HAnimSite405.children.append(TouchSensor406)
Shape407 = x3d.Shape()
Shape407.USE = "HAnimSiteShape"

HAnimSite405.children.append(Shape407)

HAnimSegment397.children.append(HAnimSite405)
HAnimSite408 = x3d.HAnimSite()
HAnimSite408.DEF = "hanim_r_medial_malleolus_pt"
HAnimSite408.name = "r_medial_malleolus_pt"
HAnimSite408.translation = [-0.0591,0.0760,-0.0928]
TouchSensor409 = x3d.TouchSensor()
TouchSensor409.description = "HAnimSite r_medial_malleolus_pt"

HAnimSite408.children.append(TouchSensor409)
Shape410 = x3d.Shape()
Shape410.USE = "HAnimSiteShape"

HAnimSite408.children.append(Shape410)

HAnimSegment397.children.append(HAnimSite408)
HAnimSite411 = x3d.HAnimSite()
HAnimSite411.DEF = "hanim_r_tibiale_pt"
HAnimSite411.name = "r_tibiale_pt"
HAnimSite411.translation = [0,1,0]
TouchSensor412 = x3d.TouchSensor()
TouchSensor412.description = "HAnimSite r_tibiale_pt"

HAnimSite411.children.append(TouchSensor412)
Shape413 = x3d.Shape()
Shape413.USE = "HAnimSiteShape"

HAnimSite411.children.append(Shape413)

HAnimSegment397.children.append(HAnimSite411)

HAnimJoint396.children.append(HAnimSegment397)
HAnimJoint414 = x3d.HAnimJoint()
HAnimJoint414.DEF = "hanim_r_knee"
HAnimJoint414.name = "r_knee"
HAnimJoint414.center = [-0.0867,0.4913,0.0318]
HAnimSegment415 = x3d.HAnimSegment()
HAnimSegment415.DEF = "hanim_r_calf"
HAnimSegment415.name = "r_calf"
Transform416 = x3d.Transform()
Transform416.translation = [-0.0867,0.4913,0.0318]
Transform417 = x3d.Transform()
""" Empty Transform """
Shape418 = x3d.Shape()
Shape418.USE = "HAnimJointShape"

Transform417.children.append(Shape418)

Transform416.children.append(Transform417)

HAnimSegment415.children.append(Transform416)
Shape419 = x3d.Shape()
LineSet420 = x3d.LineSet()
LineSet420.vertexCount = [2]
Coordinate421 = x3d.Coordinate()

LineSet420.coord = Coordinate421
""" from r_knee to r_talocrural """
ColorRGBA422 = x3d.ColorRGBA()
ColorRGBA422.USE = "HAnimSegmentLineColorRGBA"

LineSet420.color = ColorRGBA422

Shape419.geometry = LineSet420

HAnimSegment415.children.append(Shape419)
HAnimSite423 = x3d.HAnimSite()
HAnimSite423.DEF = "hanim_r_calcaneus_posterior_pt"
HAnimSite423.name = "r_calcaneus_posterior_pt"
HAnimSite423.translation = [-0.0692,0.0297,-0.1221]
TouchSensor424 = x3d.TouchSensor()
TouchSensor424.description = "HAnimSite r_calcaneus_posterior_pt"

HAnimSite423.children.append(TouchSensor424)
Shape425 = x3d.Shape()
Shape425.USE = "HAnimSiteShape"

HAnimSite423.children.append(Shape425)

HAnimSegment415.children.append(HAnimSite423)
HAnimSite426 = x3d.HAnimSite()
HAnimSite426.DEF = "hanim_r_sphyrion_pt"
HAnimSite426.name = "r_sphyrion_pt"
HAnimSite426.translation = [-0.0603,0.0610,-0.1002]
TouchSensor427 = x3d.TouchSensor()
TouchSensor427.description = "HAnimSite r_sphyrion_pt"

HAnimSite426.children.append(TouchSensor427)
Shape428 = x3d.Shape()
Shape428.USE = "HAnimSiteShape"

HAnimSite426.children.append(Shape428)

HAnimSegment415.children.append(HAnimSite426)

HAnimJoint414.children.append(HAnimSegment415)
HAnimJoint429 = x3d.HAnimJoint()
HAnimJoint429.DEF = "hanim_r_talocrural"
HAnimJoint429.name = "r_talocrural"
HAnimJoint429.center = [-0.0801,0.0712,-0.0766]
HAnimSegment430 = x3d.HAnimSegment()
HAnimSegment430.DEF = "hanim_r_talus"
HAnimSegment430.name = "r_talus"
Transform431 = x3d.Transform()
Transform431.scale = [0.15,0.15,0.15]
Transform431.translation = [-0.05,0.06,-0.025]
Transform431.rotation = [1,0,0,-1.57]
""" Transform right foot """
Transform432 = x3d.Transform()
""" Empty Transform right foot """
Shape433 = x3d.Shape()
Shape433.USE = "HAnimJointShape"

Transform432.children.append(Shape433)

Transform431.children.append(Transform432)

HAnimSegment430.children.append(Transform431)
Shape434 = x3d.Shape()
LineSet435 = x3d.LineSet()
LineSet435.vertexCount = [2]
Coordinate436 = x3d.Coordinate()

LineSet435.coord = Coordinate436
""" from r_talocrural to r_talocalcaneonavicular """
ColorRGBA437 = x3d.ColorRGBA()
ColorRGBA437.USE = "HAnimSegmentLineColorRGBA"

LineSet435.color = ColorRGBA437

Shape434.geometry = LineSet435

HAnimSegment430.children.append(Shape434)
Shape438 = x3d.Shape()
LineSet439 = x3d.LineSet()
LineSet439.vertexCount = [2]
Coordinate440 = x3d.Coordinate()

LineSet439.coord = Coordinate440
""" from r_talocrural to r_calcaneocuboid """
ColorRGBA441 = x3d.ColorRGBA()
ColorRGBA441.USE = "HAnimSegmentLineColorRGBA"

LineSet439.color = ColorRGBA441

Shape438.geometry = LineSet439

HAnimSegment430.children.append(Shape438)

HAnimJoint429.children.append(HAnimSegment430)
HAnimJoint442 = x3d.HAnimJoint()
HAnimJoint442.DEF = "hanim_r_talocalcaneonavicular"
HAnimJoint442.name = "r_talocalcaneonavicular"
HAnimJoint442.center = [0,1,0]
HAnimSegment443 = x3d.HAnimSegment()
HAnimSegment443.DEF = "hanim_r_navicular"
HAnimSegment443.name = "r_navicular"
Transform444 = x3d.Transform()
Transform444.translation = [0,1,0]
Transform445 = x3d.Transform()
""" Empty Transform """
Shape446 = x3d.Shape()
Shape446.USE = "HAnimJointShape"

Transform445.children.append(Shape446)

Transform444.children.append(Transform445)

HAnimSegment443.children.append(Transform444)
Shape447 = x3d.Shape()
LineSet448 = x3d.LineSet()
LineSet448.vertexCount = [1]
Coordinate449 = x3d.Coordinate()

LineSet448.coord = Coordinate449
""" from r_talocalcaneonavicular to r_cuneonavicular_1 """
ColorRGBA450 = x3d.ColorRGBA()
ColorRGBA450.USE = "HAnimSegmentLineColorRGBA"

LineSet448.color = ColorRGBA450

Shape447.geometry = LineSet448

HAnimSegment443.children.append(Shape447)
Shape451 = x3d.Shape()
LineSet452 = x3d.LineSet()
LineSet452.vertexCount = [1]
Coordinate453 = x3d.Coordinate()

LineSet452.coord = Coordinate453
""" from r_talocalcaneonavicular to r_cuneonavicular_2 """
ColorRGBA454 = x3d.ColorRGBA()
ColorRGBA454.USE = "HAnimSegmentLineColorRGBA"

LineSet452.color = ColorRGBA454

Shape451.geometry = LineSet452

HAnimSegment443.children.append(Shape451)
Shape455 = x3d.Shape()
LineSet456 = x3d.LineSet()
LineSet456.vertexCount = [1]
Coordinate457 = x3d.Coordinate()

LineSet456.coord = Coordinate457
""" from r_talocalcaneonavicular to r_cuneonavicular_3 """
ColorRGBA458 = x3d.ColorRGBA()
ColorRGBA458.USE = "HAnimSegmentLineColorRGBA"

LineSet456.color = ColorRGBA458

Shape455.geometry = LineSet456

HAnimSegment443.children.append(Shape455)

HAnimJoint442.children.append(HAnimSegment443)
HAnimJoint459 = x3d.HAnimJoint()
HAnimJoint459.DEF = "hanim_r_cuneonavicular_1"
HAnimJoint459.name = "r_cuneonavicular_1"
HAnimJoint459.center = [0,1,0]
HAnimSegment460 = x3d.HAnimSegment()
HAnimSegment460.DEF = "hanim_r_cuneiform_1"
HAnimSegment460.name = "r_cuneiform_1"
Transform461 = x3d.Transform()
Transform461.translation = [0,1,0]
Transform462 = x3d.Transform()
""" Empty Transform """
Shape463 = x3d.Shape()
Shape463.USE = "HAnimJointShape"

Transform462.children.append(Shape463)

Transform461.children.append(Transform462)

HAnimSegment460.children.append(Transform461)
Shape464 = x3d.Shape()
LineSet465 = x3d.LineSet()
LineSet465.vertexCount = [1]
Coordinate466 = x3d.Coordinate()

LineSet465.coord = Coordinate466
""" from r_cuneonavicular_1 to r_tarsometatarsal_1 """
ColorRGBA467 = x3d.ColorRGBA()
ColorRGBA467.USE = "HAnimSegmentLineColorRGBA"

LineSet465.color = ColorRGBA467

Shape464.geometry = LineSet465

HAnimSegment460.children.append(Shape464)

HAnimJoint459.children.append(HAnimSegment460)
HAnimJoint468 = x3d.HAnimJoint()
HAnimJoint468.DEF = "hanim_r_tarsometatarsal_1"
HAnimJoint468.name = "r_tarsometatarsal_1"
HAnimJoint468.center = [0,1,0]
HAnimSegment469 = x3d.HAnimSegment()
HAnimSegment469.DEF = "hanim_r_metatarsal_1"
HAnimSegment469.name = "r_metatarsal_1"
Transform470 = x3d.Transform()
Transform470.translation = [0,1,0]
Transform471 = x3d.Transform()
""" Empty Transform """
Shape472 = x3d.Shape()
Shape472.USE = "HAnimJointShape"

Transform471.children.append(Shape472)

Transform470.children.append(Transform471)

HAnimSegment469.children.append(Transform470)
Shape473 = x3d.Shape()
LineSet474 = x3d.LineSet()
LineSet474.vertexCount = [1]
Coordinate475 = x3d.Coordinate()

LineSet474.coord = Coordinate475
""" from r_tarsometatarsal_1 to r_metatarsophalangeal_1 """
ColorRGBA476 = x3d.ColorRGBA()
ColorRGBA476.USE = "HAnimSegmentLineColorRGBA"

LineSet474.color = ColorRGBA476

Shape473.geometry = LineSet474

HAnimSegment469.children.append(Shape473)
HAnimSite477 = x3d.HAnimSite()
HAnimSite477.DEF = "hanim_r_metatarsal_phalanx_1_pt"
HAnimSite477.name = "r_metatarsal_phalanx_1_pt"
HAnimSite477.translation = [0,1,0]
TouchSensor478 = x3d.TouchSensor()
TouchSensor478.description = "HAnimSite r_metatarsal_phalanx_1_pt"

HAnimSite477.children.append(TouchSensor478)
Shape479 = x3d.Shape()
Shape479.USE = "HAnimSiteShape"

HAnimSite477.children.append(Shape479)

HAnimSegment469.children.append(HAnimSite477)

HAnimJoint468.children.append(HAnimSegment469)
HAnimJoint480 = x3d.HAnimJoint()
HAnimJoint480.DEF = "hanim_r_metatarsophalangeal_1"
HAnimJoint480.name = "r_metatarsophalangeal_1"
HAnimJoint480.center = [0,1,0]
HAnimSegment481 = x3d.HAnimSegment()
HAnimSegment481.DEF = "hanim_r_tarsal_proximal_phalanx_1"
HAnimSegment481.name = "r_tarsal_proximal_phalanx_1"
Transform482 = x3d.Transform()
Transform482.translation = [0,1,0]
Transform483 = x3d.Transform()
""" Empty Transform """
Shape484 = x3d.Shape()
Shape484.USE = "HAnimJointShape"

Transform483.children.append(Shape484)

Transform482.children.append(Transform483)

HAnimSegment481.children.append(Transform482)
Shape485 = x3d.Shape()
LineSet486 = x3d.LineSet()
LineSet486.vertexCount = [1]
Coordinate487 = x3d.Coordinate()

LineSet486.coord = Coordinate487
""" from r_metatarsophalangeal_1 to r_tarsal_interphalangeal_1 """
ColorRGBA488 = x3d.ColorRGBA()
ColorRGBA488.USE = "HAnimSegmentLineColorRGBA"

LineSet486.color = ColorRGBA488

Shape485.geometry = LineSet486

HAnimSegment481.children.append(Shape485)
HAnimSite489 = x3d.HAnimSite()
HAnimSite489.DEF = "hanim_r_tarsal_distal_phalanx_1_tip"
HAnimSite489.name = "r_tarsal_distal_phalanx_1_tip"
HAnimSite489.translation = [0,1,0]
TouchSensor490 = x3d.TouchSensor()
TouchSensor490.description = "HAnimSite r_tarsal_distal_phalanx_1_tip"

HAnimSite489.children.append(TouchSensor490)
Shape491 = x3d.Shape()
Shape491.USE = "HAnimSiteShape"

HAnimSite489.children.append(Shape491)

HAnimSegment481.children.append(HAnimSite489)

HAnimJoint480.children.append(HAnimSegment481)
HAnimJoint492 = x3d.HAnimJoint()
HAnimJoint492.DEF = "hanim_r_tarsal_interphalangeal_1"
HAnimJoint492.name = "r_tarsal_interphalangeal_1"
HAnimJoint492.center = [0,1,0]

HAnimJoint480.children.append(HAnimJoint492)

HAnimJoint468.children.append(HAnimJoint480)

HAnimJoint459.children.append(HAnimJoint468)

HAnimJoint442.children.append(HAnimJoint459)
HAnimJoint493 = x3d.HAnimJoint()
HAnimJoint493.DEF = "hanim_r_cuneonavicular_2"
HAnimJoint493.name = "r_cuneonavicular_2"
HAnimJoint493.center = [0,1,0]
HAnimSegment494 = x3d.HAnimSegment()
HAnimSegment494.DEF = "hanim_r_cuneiform_2"
HAnimSegment494.name = "r_cuneiform_2"
Transform495 = x3d.Transform()
Transform495.translation = [0,1,0]
Transform496 = x3d.Transform()
""" Empty Transform """
Shape497 = x3d.Shape()
Shape497.USE = "HAnimJointShape"

Transform496.children.append(Shape497)

Transform495.children.append(Transform496)

HAnimSegment494.children.append(Transform495)
Shape498 = x3d.Shape()
LineSet499 = x3d.LineSet()
LineSet499.vertexCount = [1]
Coordinate500 = x3d.Coordinate()

LineSet499.coord = Coordinate500
""" from r_cuneonavicular_2 to r_tarsometatarsal_2 """
ColorRGBA501 = x3d.ColorRGBA()
ColorRGBA501.USE = "HAnimSegmentLineColorRGBA"

LineSet499.color = ColorRGBA501

Shape498.geometry = LineSet499

HAnimSegment494.children.append(Shape498)

HAnimJoint493.children.append(HAnimSegment494)
HAnimJoint502 = x3d.HAnimJoint()
HAnimJoint502.DEF = "hanim_r_tarsometatarsal_2"
HAnimJoint502.name = "r_tarsometatarsal_2"
HAnimJoint502.center = [0,1,0]
HAnimSegment503 = x3d.HAnimSegment()
HAnimSegment503.DEF = "hanim_r_metatarsal_2"
HAnimSegment503.name = "r_metatarsal_2"
Transform504 = x3d.Transform()
Transform504.translation = [0,1,0]
Transform505 = x3d.Transform()
""" Empty Transform """
Shape506 = x3d.Shape()
Shape506.USE = "HAnimJointShape"

Transform505.children.append(Shape506)

Transform504.children.append(Transform505)

HAnimSegment503.children.append(Transform504)
Shape507 = x3d.Shape()
LineSet508 = x3d.LineSet()
LineSet508.vertexCount = [1]
Coordinate509 = x3d.Coordinate()

LineSet508.coord = Coordinate509
""" from r_tarsometatarsal_2 to r_metatarsophalangeal_2 """
ColorRGBA510 = x3d.ColorRGBA()
ColorRGBA510.USE = "HAnimSegmentLineColorRGBA"

LineSet508.color = ColorRGBA510

Shape507.geometry = LineSet508

HAnimSegment503.children.append(Shape507)

HAnimJoint502.children.append(HAnimSegment503)
HAnimJoint511 = x3d.HAnimJoint()
HAnimJoint511.DEF = "hanim_r_metatarsophalangeal_2"
HAnimJoint511.name = "r_metatarsophalangeal_2"
HAnimJoint511.center = [0,1,0]
HAnimSegment512 = x3d.HAnimSegment()
HAnimSegment512.DEF = "hanim_r_tarsal_proximal_phalanx_2"
HAnimSegment512.name = "r_tarsal_proximal_phalanx_2"
Transform513 = x3d.Transform()
Transform513.translation = [0,1,0]
Transform514 = x3d.Transform()
""" Empty Transform """
Shape515 = x3d.Shape()
Shape515.USE = "HAnimJointShape"

Transform514.children.append(Shape515)

Transform513.children.append(Transform514)

HAnimSegment512.children.append(Transform513)
Shape516 = x3d.Shape()
LineSet517 = x3d.LineSet()
LineSet517.vertexCount = [1]
Coordinate518 = x3d.Coordinate()

LineSet517.coord = Coordinate518
""" from r_metatarsophalangeal_2 to r_tarsal_proximal_interphalangeal_2 """
ColorRGBA519 = x3d.ColorRGBA()
ColorRGBA519.USE = "HAnimSegmentLineColorRGBA"

LineSet517.color = ColorRGBA519

Shape516.geometry = LineSet517

HAnimSegment512.children.append(Shape516)

HAnimJoint511.children.append(HAnimSegment512)
HAnimJoint520 = x3d.HAnimJoint()
HAnimJoint520.DEF = "hanim_r_tarsal_proximal_interphalangeal_2"
HAnimJoint520.name = "r_tarsal_proximal_interphalangeal_2"
HAnimJoint520.center = [0,1,0]
HAnimSegment521 = x3d.HAnimSegment()
HAnimSegment521.DEF = "hanim_r_tarsal_middle_phalanx_2"
HAnimSegment521.name = "r_tarsal_middle_phalanx_2"
Transform522 = x3d.Transform()
Transform522.translation = [0,1,0]
Transform523 = x3d.Transform()
""" Empty Transform """
Shape524 = x3d.Shape()
Shape524.USE = "HAnimJointShape"

Transform523.children.append(Shape524)

Transform522.children.append(Transform523)

HAnimSegment521.children.append(Transform522)
Shape525 = x3d.Shape()
LineSet526 = x3d.LineSet()
LineSet526.vertexCount = [1]
Coordinate527 = x3d.Coordinate()

LineSet526.coord = Coordinate527
""" from r_tarsal_proximal_interphalangeal_2 to r_tarsal_distal_interphalangeal_2 """
ColorRGBA528 = x3d.ColorRGBA()
ColorRGBA528.USE = "HAnimSegmentLineColorRGBA"

LineSet526.color = ColorRGBA528

Shape525.geometry = LineSet526

HAnimSegment521.children.append(Shape525)
HAnimSite529 = x3d.HAnimSite()
HAnimSite529.DEF = "hanim_r_tarsal_distal_phalanx_2_tip"
HAnimSite529.name = "r_tarsal_distal_phalanx_2_tip"
HAnimSite529.translation = [-0.0883,0.0134,0.1383]
TouchSensor530 = x3d.TouchSensor()
TouchSensor530.description = "HAnimSite r_tarsal_distal_phalanx_2_tip"

HAnimSite529.children.append(TouchSensor530)
Shape531 = x3d.Shape()
Shape531.USE = "HAnimSiteShape"

HAnimSite529.children.append(Shape531)

HAnimSegment521.children.append(HAnimSite529)

HAnimJoint520.children.append(HAnimSegment521)
HAnimJoint532 = x3d.HAnimJoint()
HAnimJoint532.DEF = "hanim_r_tarsal_distal_interphalangeal_2"
HAnimJoint532.name = "r_tarsal_distal_interphalangeal_2"
HAnimJoint532.center = [0,1,0]

HAnimJoint520.children.append(HAnimJoint532)

HAnimJoint511.children.append(HAnimJoint520)

HAnimJoint502.children.append(HAnimJoint511)

HAnimJoint493.children.append(HAnimJoint502)

HAnimJoint442.children.append(HAnimJoint493)
HAnimJoint533 = x3d.HAnimJoint()
HAnimJoint533.DEF = "hanim_r_cuneonavicular_3"
HAnimJoint533.name = "r_cuneonavicular_3"
HAnimJoint533.center = [0,1,0]
HAnimSegment534 = x3d.HAnimSegment()
HAnimSegment534.DEF = "hanim_r_cuneiform_3"
HAnimSegment534.name = "r_cuneiform_3"
Transform535 = x3d.Transform()
Transform535.translation = [0,1,0]
Transform536 = x3d.Transform()
""" Empty Transform """
Shape537 = x3d.Shape()
Shape537.USE = "HAnimJointShape"

Transform536.children.append(Shape537)

Transform535.children.append(Transform536)

HAnimSegment534.children.append(Transform535)
Shape538 = x3d.Shape()
LineSet539 = x3d.LineSet()
LineSet539.vertexCount = [1]
Coordinate540 = x3d.Coordinate()

LineSet539.coord = Coordinate540
""" from r_cuneonavicular_3 to r_tarsometatarsal_3 """
ColorRGBA541 = x3d.ColorRGBA()
ColorRGBA541.USE = "HAnimSegmentLineColorRGBA"

LineSet539.color = ColorRGBA541

Shape538.geometry = LineSet539

HAnimSegment534.children.append(Shape538)

HAnimJoint533.children.append(HAnimSegment534)
HAnimJoint542 = x3d.HAnimJoint()
HAnimJoint542.DEF = "hanim_r_tarsometatarsal_3"
HAnimJoint542.name = "r_tarsometatarsal_3"
HAnimJoint542.center = [0,1,0]
HAnimSegment543 = x3d.HAnimSegment()
HAnimSegment543.DEF = "hanim_r_metatarsal_3"
HAnimSegment543.name = "r_metatarsal_3"
Transform544 = x3d.Transform()
Transform544.translation = [0,1,0]
Transform545 = x3d.Transform()
""" Empty Transform """
Shape546 = x3d.Shape()
Shape546.USE = "HAnimJointShape"

Transform545.children.append(Shape546)

Transform544.children.append(Transform545)

HAnimSegment543.children.append(Transform544)
Shape547 = x3d.Shape()
LineSet548 = x3d.LineSet()
LineSet548.vertexCount = [1]
Coordinate549 = x3d.Coordinate()

LineSet548.coord = Coordinate549
""" from r_tarsometatarsal_3 to r_metatarsophalangeal_3 """
ColorRGBA550 = x3d.ColorRGBA()
ColorRGBA550.USE = "HAnimSegmentLineColorRGBA"

LineSet548.color = ColorRGBA550

Shape547.geometry = LineSet548

HAnimSegment543.children.append(Shape547)

HAnimJoint542.children.append(HAnimSegment543)
HAnimJoint551 = x3d.HAnimJoint()
HAnimJoint551.DEF = "hanim_r_metatarsophalangeal_3"
HAnimJoint551.name = "r_metatarsophalangeal_3"
HAnimJoint551.center = [0,1,0]
HAnimSegment552 = x3d.HAnimSegment()
HAnimSegment552.DEF = "hanim_r_tarsal_proximal_phalanx_3"
HAnimSegment552.name = "r_tarsal_proximal_phalanx_3"
Transform553 = x3d.Transform()
Transform553.translation = [0,1,0]
Transform554 = x3d.Transform()
""" Empty Transform """
Shape555 = x3d.Shape()
Shape555.USE = "HAnimJointShape"

Transform554.children.append(Shape555)

Transform553.children.append(Transform554)

HAnimSegment552.children.append(Transform553)
Shape556 = x3d.Shape()
LineSet557 = x3d.LineSet()
LineSet557.vertexCount = [1]
Coordinate558 = x3d.Coordinate()

LineSet557.coord = Coordinate558
""" from r_metatarsophalangeal_3 to r_tarsal_proximal_interphalangeal_3 """
ColorRGBA559 = x3d.ColorRGBA()
ColorRGBA559.USE = "HAnimSegmentLineColorRGBA"

LineSet557.color = ColorRGBA559

Shape556.geometry = LineSet557

HAnimSegment552.children.append(Shape556)

HAnimJoint551.children.append(HAnimSegment552)
HAnimJoint560 = x3d.HAnimJoint()
HAnimJoint560.DEF = "hanim_r_tarsal_proximal_interphalangeal_3"
HAnimJoint560.name = "r_tarsal_proximal_interphalangeal_3"
HAnimJoint560.center = [0,1,0]
HAnimSegment561 = x3d.HAnimSegment()
HAnimSegment561.DEF = "hanim_r_tarsal_middle_phalanx_3"
HAnimSegment561.name = "r_tarsal_middle_phalanx_3"
Transform562 = x3d.Transform()
Transform562.translation = [0,1,0]
Transform563 = x3d.Transform()
""" Empty Transform """
Shape564 = x3d.Shape()
Shape564.USE = "HAnimJointShape"

Transform563.children.append(Shape564)

Transform562.children.append(Transform563)

HAnimSegment561.children.append(Transform562)
Shape565 = x3d.Shape()
LineSet566 = x3d.LineSet()
LineSet566.vertexCount = [1]
Coordinate567 = x3d.Coordinate()

LineSet566.coord = Coordinate567
""" from r_tarsal_proximal_interphalangeal_3 to r_tarsal_distal_interphalangeal_3 """
ColorRGBA568 = x3d.ColorRGBA()
ColorRGBA568.USE = "HAnimSegmentLineColorRGBA"

LineSet566.color = ColorRGBA568

Shape565.geometry = LineSet566

HAnimSegment561.children.append(Shape565)
HAnimSite569 = x3d.HAnimSite()
HAnimSite569.DEF = "hanim_r_tarsal_distal_phalanx_3_tip"
HAnimSite569.name = "r_tarsal_distal_phalanx_3_tip"
HAnimSite569.translation = [0,1,0]
TouchSensor570 = x3d.TouchSensor()
TouchSensor570.description = "HAnimSite r_tarsal_distal_phalanx_3_tip"

HAnimSite569.children.append(TouchSensor570)
Shape571 = x3d.Shape()
Shape571.USE = "HAnimSiteShape"

HAnimSite569.children.append(Shape571)

HAnimSegment561.children.append(HAnimSite569)

HAnimJoint560.children.append(HAnimSegment561)
HAnimJoint572 = x3d.HAnimJoint()
HAnimJoint572.DEF = "hanim_r_tarsal_distal_interphalangeal_3"
HAnimJoint572.name = "r_tarsal_distal_interphalangeal_3"
HAnimJoint572.center = [0,1,0]

HAnimJoint560.children.append(HAnimJoint572)

HAnimJoint551.children.append(HAnimJoint560)

HAnimJoint542.children.append(HAnimJoint551)

HAnimJoint533.children.append(HAnimJoint542)

HAnimJoint442.children.append(HAnimJoint533)

HAnimJoint429.children.append(HAnimJoint442)
HAnimJoint573 = x3d.HAnimJoint()
HAnimJoint573.DEF = "hanim_r_calcaneocuboid"
HAnimJoint573.name = "r_calcaneocuboid"
HAnimJoint573.center = [0,1,0]
HAnimSegment574 = x3d.HAnimSegment()
HAnimSegment574.DEF = "hanim_r_calcaneus"
HAnimSegment574.name = "r_calcaneus"
Transform575 = x3d.Transform()
Transform575.translation = [0,1,0]
Transform576 = x3d.Transform()
""" Empty Transform """
Shape577 = x3d.Shape()
Shape577.USE = "HAnimJointShape"

Transform576.children.append(Shape577)

Transform575.children.append(Transform576)

HAnimSegment574.children.append(Transform575)
Shape578 = x3d.Shape()
LineSet579 = x3d.LineSet()
LineSet579.vertexCount = [1]
Coordinate580 = x3d.Coordinate()

LineSet579.coord = Coordinate580
""" from r_calcaneocuboid to r_transversetarsal """
ColorRGBA581 = x3d.ColorRGBA()
ColorRGBA581.USE = "HAnimSegmentLineColorRGBA"

LineSet579.color = ColorRGBA581

Shape578.geometry = LineSet579

HAnimSegment574.children.append(Shape578)

HAnimJoint573.children.append(HAnimSegment574)
HAnimJoint582 = x3d.HAnimJoint()
HAnimJoint582.DEF = "hanim_r_transversetarsal"
HAnimJoint582.name = "r_transversetarsal"
HAnimJoint582.center = [0,1,0]
HAnimSegment583 = x3d.HAnimSegment()
HAnimSegment583.DEF = "hanim_r_cuboid"
HAnimSegment583.name = "r_cuboid"
Transform584 = x3d.Transform()
Transform584.translation = [0,1,0]
Transform585 = x3d.Transform()
""" Empty Transform """
Shape586 = x3d.Shape()
Shape586.USE = "HAnimJointShape"

Transform585.children.append(Shape586)

Transform584.children.append(Transform585)

HAnimSegment583.children.append(Transform584)
Shape587 = x3d.Shape()
LineSet588 = x3d.LineSet()
LineSet588.vertexCount = [1]
Coordinate589 = x3d.Coordinate()

LineSet588.coord = Coordinate589
""" from r_transversetarsal to r_tarsometatarsal_4 """
ColorRGBA590 = x3d.ColorRGBA()
ColorRGBA590.USE = "HAnimSegmentLineColorRGBA"

LineSet588.color = ColorRGBA590

Shape587.geometry = LineSet588

HAnimSegment583.children.append(Shape587)
Shape591 = x3d.Shape()
LineSet592 = x3d.LineSet()
LineSet592.vertexCount = [1]
Coordinate593 = x3d.Coordinate()

LineSet592.coord = Coordinate593
""" from r_transversetarsal to r_tarsometatarsal_5 """
ColorRGBA594 = x3d.ColorRGBA()
ColorRGBA594.USE = "HAnimSegmentLineColorRGBA"

LineSet592.color = ColorRGBA594

Shape591.geometry = LineSet592

HAnimSegment583.children.append(Shape591)

HAnimJoint582.children.append(HAnimSegment583)
HAnimJoint595 = x3d.HAnimJoint()
HAnimJoint595.DEF = "hanim_r_tarsometatarsal_4"
HAnimJoint595.name = "r_tarsometatarsal_4"
HAnimJoint595.center = [0,1,0]
HAnimSegment596 = x3d.HAnimSegment()
HAnimSegment596.DEF = "hanim_r_metatarsal_4"
HAnimSegment596.name = "r_metatarsal_4"
Transform597 = x3d.Transform()
Transform597.translation = [0,1,0]
Transform598 = x3d.Transform()
""" Empty Transform """
Shape599 = x3d.Shape()
Shape599.USE = "HAnimJointShape"

Transform598.children.append(Shape599)

Transform597.children.append(Transform598)

HAnimSegment596.children.append(Transform597)
Shape600 = x3d.Shape()
LineSet601 = x3d.LineSet()
LineSet601.vertexCount = [1]
Coordinate602 = x3d.Coordinate()

LineSet601.coord = Coordinate602
""" from r_tarsometatarsal_4 to r_metatarsophalangeal_4 """
ColorRGBA603 = x3d.ColorRGBA()
ColorRGBA603.USE = "HAnimSegmentLineColorRGBA"

LineSet601.color = ColorRGBA603

Shape600.geometry = LineSet601

HAnimSegment596.children.append(Shape600)

HAnimJoint595.children.append(HAnimSegment596)
HAnimJoint604 = x3d.HAnimJoint()
HAnimJoint604.DEF = "hanim_r_metatarsophalangeal_4"
HAnimJoint604.name = "r_metatarsophalangeal_4"
HAnimJoint604.center = [0,1,0]
HAnimSegment605 = x3d.HAnimSegment()
HAnimSegment605.DEF = "hanim_r_tarsal_proximal_phalanx_4"
HAnimSegment605.name = "r_tarsal_proximal_phalanx_4"
Transform606 = x3d.Transform()
Transform606.translation = [0,1,0]
Transform607 = x3d.Transform()
""" Empty Transform """
Shape608 = x3d.Shape()
Shape608.USE = "HAnimJointShape"

Transform607.children.append(Shape608)

Transform606.children.append(Transform607)

HAnimSegment605.children.append(Transform606)
Shape609 = x3d.Shape()
LineSet610 = x3d.LineSet()
LineSet610.vertexCount = [1]
Coordinate611 = x3d.Coordinate()

LineSet610.coord = Coordinate611
""" from r_metatarsophalangeal_4 to r_tarsal_proximal_interphalangeal_4 """
ColorRGBA612 = x3d.ColorRGBA()
ColorRGBA612.USE = "HAnimSegmentLineColorRGBA"

LineSet610.color = ColorRGBA612

Shape609.geometry = LineSet610

HAnimSegment605.children.append(Shape609)

HAnimJoint604.children.append(HAnimSegment605)
HAnimJoint613 = x3d.HAnimJoint()
HAnimJoint613.DEF = "hanim_r_tarsal_proximal_interphalangeal_4"
HAnimJoint613.name = "r_tarsal_proximal_interphalangeal_4"
HAnimJoint613.center = [0,1,0]
HAnimSegment614 = x3d.HAnimSegment()
HAnimSegment614.DEF = "hanim_r_tarsal_middle_phalanx_4"
HAnimSegment614.name = "r_tarsal_middle_phalanx_4"
Transform615 = x3d.Transform()
Transform615.translation = [0,1,0]
Transform616 = x3d.Transform()
""" Empty Transform """
Shape617 = x3d.Shape()
Shape617.USE = "HAnimJointShape"

Transform616.children.append(Shape617)

Transform615.children.append(Transform616)

HAnimSegment614.children.append(Transform615)
Shape618 = x3d.Shape()
LineSet619 = x3d.LineSet()
LineSet619.vertexCount = [1]
Coordinate620 = x3d.Coordinate()

LineSet619.coord = Coordinate620
""" from r_tarsal_proximal_interphalangeal_4 to r_tarsal_distal_interphalangeal_4 """
ColorRGBA621 = x3d.ColorRGBA()
ColorRGBA621.USE = "HAnimSegmentLineColorRGBA"

LineSet619.color = ColorRGBA621

Shape618.geometry = LineSet619

HAnimSegment614.children.append(Shape618)
HAnimSite622 = x3d.HAnimSite()
HAnimSite622.DEF = "hanim_r_tarsal_distal_phalanx_4_tip"
HAnimSite622.name = "r_tarsal_distal_phalanx_4_tip"
HAnimSite622.translation = [0,1,0]
TouchSensor623 = x3d.TouchSensor()
TouchSensor623.description = "HAnimSite r_tarsal_distal_phalanx_4_tip"

HAnimSite622.children.append(TouchSensor623)
Shape624 = x3d.Shape()
Shape624.USE = "HAnimSiteShape"

HAnimSite622.children.append(Shape624)

HAnimSegment614.children.append(HAnimSite622)

HAnimJoint613.children.append(HAnimSegment614)
HAnimJoint625 = x3d.HAnimJoint()
HAnimJoint625.DEF = "hanim_r_tarsal_distal_interphalangeal_4"
HAnimJoint625.name = "r_tarsal_distal_interphalangeal_4"
HAnimJoint625.center = [0,1,0]

HAnimJoint613.children.append(HAnimJoint625)

HAnimJoint604.children.append(HAnimJoint613)

HAnimJoint595.children.append(HAnimJoint604)

HAnimJoint582.children.append(HAnimJoint595)
HAnimJoint626 = x3d.HAnimJoint()
HAnimJoint626.DEF = "hanim_r_tarsometatarsal_5"
HAnimJoint626.name = "r_tarsometatarsal_5"
HAnimJoint626.center = [0,1,0]
HAnimSegment627 = x3d.HAnimSegment()
HAnimSegment627.DEF = "hanim_r_metatarsal_5"
HAnimSegment627.name = "r_metatarsal_5"
Transform628 = x3d.Transform()
Transform628.translation = [0,1,0]
Transform629 = x3d.Transform()
""" Empty Transform """
Shape630 = x3d.Shape()
Shape630.USE = "HAnimJointShape"

Transform629.children.append(Shape630)

Transform628.children.append(Transform629)

HAnimSegment627.children.append(Transform628)
Shape631 = x3d.Shape()
LineSet632 = x3d.LineSet()
LineSet632.vertexCount = [1]
Coordinate633 = x3d.Coordinate()

LineSet632.coord = Coordinate633
""" from r_tarsometatarsal_5 to r_metatarsophalangeal_5 """
ColorRGBA634 = x3d.ColorRGBA()
ColorRGBA634.USE = "HAnimSegmentLineColorRGBA"

LineSet632.color = ColorRGBA634

Shape631.geometry = LineSet632

HAnimSegment627.children.append(Shape631)
HAnimSite635 = x3d.HAnimSite()
HAnimSite635.DEF = "hanim_r_metatarsal_phalanx_5_pt"
HAnimSite635.name = "r_metatarsal_phalanx_5_pt"
HAnimSite635.translation = [0,1,0]
TouchSensor636 = x3d.TouchSensor()
TouchSensor636.description = "HAnimSite r_metatarsal_phalanx_5_pt"

HAnimSite635.children.append(TouchSensor636)
Shape637 = x3d.Shape()
Shape637.USE = "HAnimSiteShape"

HAnimSite635.children.append(Shape637)

HAnimSegment627.children.append(HAnimSite635)

HAnimJoint626.children.append(HAnimSegment627)
HAnimJoint638 = x3d.HAnimJoint()
HAnimJoint638.DEF = "hanim_r_metatarsophalangeal_5"
HAnimJoint638.name = "r_metatarsophalangeal_5"
HAnimJoint638.center = [0,1,0]
HAnimSegment639 = x3d.HAnimSegment()
HAnimSegment639.DEF = "hanim_r_tarsal_proximal_phalanx_5"
HAnimSegment639.name = "r_tarsal_proximal_phalanx_5"
Transform640 = x3d.Transform()
Transform640.translation = [0,1,0]
Transform641 = x3d.Transform()
""" Empty Transform """
Shape642 = x3d.Shape()
Shape642.USE = "HAnimJointShape"

Transform641.children.append(Shape642)

Transform640.children.append(Transform641)

HAnimSegment639.children.append(Transform640)
Shape643 = x3d.Shape()
LineSet644 = x3d.LineSet()
LineSet644.vertexCount = [1]
Coordinate645 = x3d.Coordinate()

LineSet644.coord = Coordinate645
""" from r_metatarsophalangeal_5 to r_tarsal_proximal_interphalangeal_5 """
ColorRGBA646 = x3d.ColorRGBA()
ColorRGBA646.USE = "HAnimSegmentLineColorRGBA"

LineSet644.color = ColorRGBA646

Shape643.geometry = LineSet644

HAnimSegment639.children.append(Shape643)

HAnimJoint638.children.append(HAnimSegment639)
HAnimJoint647 = x3d.HAnimJoint()
HAnimJoint647.DEF = "hanim_r_tarsal_proximal_interphalangeal_5"
HAnimJoint647.name = "r_tarsal_proximal_interphalangeal_5"
HAnimJoint647.center = [0,1,0]
HAnimSegment648 = x3d.HAnimSegment()
HAnimSegment648.DEF = "hanim_r_tarsal_middle_phalanx_5"
HAnimSegment648.name = "r_tarsal_middle_phalanx_5"
Transform649 = x3d.Transform()
Transform649.translation = [0,1,0]
Transform650 = x3d.Transform()
""" Empty Transform """
Shape651 = x3d.Shape()
Shape651.USE = "HAnimJointShape"

Transform650.children.append(Shape651)

Transform649.children.append(Transform650)

HAnimSegment648.children.append(Transform649)
Shape652 = x3d.Shape()
LineSet653 = x3d.LineSet()
LineSet653.vertexCount = [1]
Coordinate654 = x3d.Coordinate()

LineSet653.coord = Coordinate654
""" from r_tarsal_proximal_interphalangeal_5 to r_tarsal_distal_interphalangeal_5 """
ColorRGBA655 = x3d.ColorRGBA()
ColorRGBA655.USE = "HAnimSegmentLineColorRGBA"

LineSet653.color = ColorRGBA655

Shape652.geometry = LineSet653

HAnimSegment648.children.append(Shape652)
HAnimSite656 = x3d.HAnimSite()
HAnimSite656.DEF = "hanim_r_tarsal_distal_phalanx_5_tip"
HAnimSite656.name = "r_tarsal_distal_phalanx_5_tip"
HAnimSite656.translation = [0,1,0]
TouchSensor657 = x3d.TouchSensor()
TouchSensor657.description = "HAnimSite r_tarsal_distal_phalanx_5_tip"

HAnimSite656.children.append(TouchSensor657)
Shape658 = x3d.Shape()
Shape658.USE = "HAnimSiteShape"

HAnimSite656.children.append(Shape658)

HAnimSegment648.children.append(HAnimSite656)

HAnimJoint647.children.append(HAnimSegment648)
HAnimJoint659 = x3d.HAnimJoint()
HAnimJoint659.DEF = "hanim_r_tarsal_distal_interphalangeal_5"
HAnimJoint659.name = "r_tarsal_distal_interphalangeal_5"
HAnimJoint659.center = [0,1,0]

HAnimJoint647.children.append(HAnimJoint659)

HAnimJoint638.children.append(HAnimJoint647)

HAnimJoint626.children.append(HAnimJoint638)

HAnimJoint582.children.append(HAnimJoint626)

HAnimJoint573.children.append(HAnimJoint582)

HAnimJoint429.children.append(HAnimJoint573)

HAnimJoint414.children.append(HAnimJoint429)

HAnimJoint396.children.append(HAnimJoint414)

HAnimJoint95.children.append(HAnimJoint396)

HAnimJoint43.children.append(HAnimJoint95)
HAnimJoint660 = x3d.HAnimJoint()
HAnimJoint660.DEF = "hanim_vl5"
HAnimJoint660.name = "vl5"
HAnimJoint660.center = [0.0028,1.0568,-0.0776]
HAnimSegment661 = x3d.HAnimSegment()
HAnimSegment661.DEF = "hanim_l5"
HAnimSegment661.name = "l5"
Transform662 = x3d.Transform()
Transform662.translation = [0.0028,1.0568,-0.0776]
Transform663 = x3d.Transform()
""" Empty Transform """
Shape664 = x3d.Shape()
Shape664.USE = "HAnimJointShape"

Transform663.children.append(Shape664)

Transform662.children.append(Transform663)

HAnimSegment661.children.append(Transform662)
Shape665 = x3d.Shape()
LineSet666 = x3d.LineSet()
LineSet666.vertexCount = [2]
Coordinate667 = x3d.Coordinate()

LineSet666.coord = Coordinate667
""" from vl5 to vl4 """
ColorRGBA668 = x3d.ColorRGBA()
ColorRGBA668.USE = "HAnimSegmentLineColorRGBA"

LineSet666.color = ColorRGBA668

Shape665.geometry = LineSet666

HAnimSegment661.children.append(Shape665)

HAnimJoint660.children.append(HAnimSegment661)
HAnimJoint669 = x3d.HAnimJoint()
HAnimJoint669.DEF = "hanim_vl4"
HAnimJoint669.name = "vl4"
HAnimJoint669.center = [0.0035,1.0925,-0.0787]
HAnimSegment670 = x3d.HAnimSegment()
HAnimSegment670.DEF = "hanim_l4"
HAnimSegment670.name = "l4"
Transform671 = x3d.Transform()
Transform671.translation = [0.0035,1.0925,-0.0787]
Transform672 = x3d.Transform()
""" Empty Transform """
Shape673 = x3d.Shape()
Shape673.USE = "HAnimJointShape"

Transform672.children.append(Shape673)

Transform671.children.append(Transform672)

HAnimSegment670.children.append(Transform671)
Shape674 = x3d.Shape()
LineSet675 = x3d.LineSet()
LineSet675.vertexCount = [2]
Coordinate676 = x3d.Coordinate()

LineSet675.coord = Coordinate676
""" from vl4 to vl3 """
ColorRGBA677 = x3d.ColorRGBA()
ColorRGBA677.USE = "HAnimSegmentLineColorRGBA"

LineSet675.color = ColorRGBA677

Shape674.geometry = LineSet675

HAnimSegment670.children.append(Shape674)

HAnimJoint669.children.append(HAnimSegment670)
HAnimJoint678 = x3d.HAnimJoint()
HAnimJoint678.DEF = "hanim_vl3"
HAnimJoint678.name = "vl3"
HAnimJoint678.center = [0.0041,1.1276,-0.0796]
HAnimSegment679 = x3d.HAnimSegment()
HAnimSegment679.DEF = "hanim_l3"
HAnimSegment679.name = "l3"
Transform680 = x3d.Transform()
Transform680.translation = [0.0041,1.1276,-0.0796]
Transform681 = x3d.Transform()
""" Empty Transform """
Shape682 = x3d.Shape()
Shape682.USE = "HAnimJointShape"

Transform681.children.append(Shape682)

Transform680.children.append(Transform681)

HAnimSegment679.children.append(Transform680)
Shape683 = x3d.Shape()
LineSet684 = x3d.LineSet()
LineSet684.vertexCount = [2]
Coordinate685 = x3d.Coordinate()

LineSet684.coord = Coordinate685
""" from vl3 to vl2 """
ColorRGBA686 = x3d.ColorRGBA()
ColorRGBA686.USE = "HAnimSegmentLineColorRGBA"

LineSet684.color = ColorRGBA686

Shape683.geometry = LineSet684

HAnimSegment679.children.append(Shape683)
HAnimSite687 = x3d.HAnimSite()
HAnimSite687.DEF = "hanim_l_rib10_pt"
HAnimSite687.name = "l_rib10_pt"
HAnimSite687.translation = [0.0871,1.1925,0.0992]
TouchSensor688 = x3d.TouchSensor()
TouchSensor688.description = "HAnimSite l_rib10_pt"

HAnimSite687.children.append(TouchSensor688)
Shape689 = x3d.Shape()
Shape689.USE = "HAnimSiteShape"

HAnimSite687.children.append(Shape689)

HAnimSegment679.children.append(HAnimSite687)
HAnimSite690 = x3d.HAnimSite()
HAnimSite690.DEF = "hanim_r_rib10_pt"
HAnimSite690.name = "r_rib10_pt"
HAnimSite690.translation = [-0.0711,1.1941,0.1016]
TouchSensor691 = x3d.TouchSensor()
TouchSensor691.description = "HAnimSite r_rib10_pt"

HAnimSite690.children.append(TouchSensor691)
Shape692 = x3d.Shape()
Shape692.USE = "HAnimSiteShape"

HAnimSite690.children.append(Shape692)

HAnimSegment679.children.append(HAnimSite690)
HAnimSite693 = x3d.HAnimSite()
HAnimSite693.DEF = "hanim_spine_2_middle_back_pt"
HAnimSite693.name = "spine_2_middle_back_pt"
HAnimSite693.translation = [0,1,0]
TouchSensor694 = x3d.TouchSensor()
TouchSensor694.description = "HAnimSite spine_2_middle_back_pt"

HAnimSite693.children.append(TouchSensor694)
Shape695 = x3d.Shape()
Shape695.USE = "HAnimSiteShape"

HAnimSite693.children.append(Shape695)

HAnimSegment679.children.append(HAnimSite693)

HAnimJoint678.children.append(HAnimSegment679)
HAnimJoint696 = x3d.HAnimJoint()
HAnimJoint696.DEF = "hanim_vl2"
HAnimJoint696.name = "vl2"
HAnimJoint696.center = [0.0045,1.1546,-0.0800]
HAnimSegment697 = x3d.HAnimSegment()
HAnimSegment697.DEF = "hanim_l2"
HAnimSegment697.name = "l2"
Transform698 = x3d.Transform()
Transform698.translation = [0.0045,1.1546,-0.0800]
Transform699 = x3d.Transform()
""" Empty Transform """
Shape700 = x3d.Shape()
Shape700.USE = "HAnimJointShape"

Transform699.children.append(Shape700)

Transform698.children.append(Transform699)

HAnimSegment697.children.append(Transform698)
Shape701 = x3d.Shape()
LineSet702 = x3d.LineSet()
LineSet702.vertexCount = [2]
Coordinate703 = x3d.Coordinate()

LineSet702.coord = Coordinate703
""" from vl2 to vl1 """
ColorRGBA704 = x3d.ColorRGBA()
ColorRGBA704.USE = "HAnimSegmentLineColorRGBA"

LineSet702.color = ColorRGBA704

Shape701.geometry = LineSet702

HAnimSegment697.children.append(Shape701)

HAnimJoint696.children.append(HAnimSegment697)
HAnimJoint705 = x3d.HAnimJoint()
HAnimJoint705.DEF = "hanim_vl1"
HAnimJoint705.name = "vl1"
HAnimJoint705.center = [0.0048,1.1912,-0.0805]
HAnimSegment706 = x3d.HAnimSegment()
HAnimSegment706.DEF = "hanim_l1"
HAnimSegment706.name = "l1"
Transform707 = x3d.Transform()
Transform707.translation = [0.0048,1.1912,-0.0805]
Transform708 = x3d.Transform()
""" Empty Transform """
Shape709 = x3d.Shape()
Shape709.USE = "HAnimJointShape"

Transform708.children.append(Shape709)

Transform707.children.append(Transform708)

HAnimSegment706.children.append(Transform707)
Shape710 = x3d.Shape()
LineSet711 = x3d.LineSet()
LineSet711.vertexCount = [2]
Coordinate712 = x3d.Coordinate()

LineSet711.coord = Coordinate712
""" from vl1 to vt12 """
ColorRGBA713 = x3d.ColorRGBA()
ColorRGBA713.USE = "HAnimSegmentLineColorRGBA"

LineSet711.color = ColorRGBA713

Shape710.geometry = LineSet711

HAnimSegment706.children.append(Shape710)

HAnimJoint705.children.append(HAnimSegment706)
HAnimJoint714 = x3d.HAnimJoint()
HAnimJoint714.DEF = "hanim_vt12"
HAnimJoint714.name = "vt12"
HAnimJoint714.center = [0.0051,1.2278,-0.0808]
HAnimSegment715 = x3d.HAnimSegment()
HAnimSegment715.DEF = "hanim_t12"
HAnimSegment715.name = "t12"
Transform716 = x3d.Transform()
Transform716.translation = [0.0051,1.2278,-0.0808]
Transform717 = x3d.Transform()
""" Empty Transform """
Shape718 = x3d.Shape()
Shape718.USE = "HAnimJointShape"

Transform717.children.append(Shape718)

Transform716.children.append(Transform717)

HAnimSegment715.children.append(Transform716)
Shape719 = x3d.Shape()
LineSet720 = x3d.LineSet()
LineSet720.vertexCount = [2]
Coordinate721 = x3d.Coordinate()

LineSet720.coord = Coordinate721
""" from vt12 to vt11 """
ColorRGBA722 = x3d.ColorRGBA()
ColorRGBA722.USE = "HAnimSegmentLineColorRGBA"

LineSet720.color = ColorRGBA722

Shape719.geometry = LineSet720

HAnimSegment715.children.append(Shape719)

HAnimJoint714.children.append(HAnimSegment715)
HAnimJoint723 = x3d.HAnimJoint()
HAnimJoint723.DEF = "hanim_vt11"
HAnimJoint723.name = "vt11"
HAnimJoint723.center = [0.0053,1.2679,-0.0810]
HAnimSegment724 = x3d.HAnimSegment()
HAnimSegment724.DEF = "hanim_t11"
HAnimSegment724.name = "t11"
Transform725 = x3d.Transform()
Transform725.translation = [0.0053,1.2679,-0.0810]
Transform726 = x3d.Transform()
""" Empty Transform """
Shape727 = x3d.Shape()
Shape727.USE = "HAnimJointShape"

Transform726.children.append(Shape727)

Transform725.children.append(Transform726)

HAnimSegment724.children.append(Transform725)
Shape728 = x3d.Shape()
LineSet729 = x3d.LineSet()
LineSet729.vertexCount = [2]
Coordinate730 = x3d.Coordinate()

LineSet729.coord = Coordinate730
""" from vt11 to vt10 """
ColorRGBA731 = x3d.ColorRGBA()
ColorRGBA731.USE = "HAnimSegmentLineColorRGBA"

LineSet729.color = ColorRGBA731

Shape728.geometry = LineSet729

HAnimSegment724.children.append(Shape728)
HAnimSite732 = x3d.HAnimSite()
HAnimSite732.DEF = "hanim_substernale_pt"
HAnimSite732.name = "substernale_pt"
HAnimSite732.translation = [0.0085,1.2995,0.1147]
TouchSensor733 = x3d.TouchSensor()
TouchSensor733.description = "HAnimSite substernale_pt"

HAnimSite732.children.append(TouchSensor733)
Shape734 = x3d.Shape()
Shape734.USE = "HAnimSiteShape"

HAnimSite732.children.append(Shape734)

HAnimSegment724.children.append(HAnimSite732)

HAnimJoint723.children.append(HAnimSegment724)
HAnimJoint735 = x3d.HAnimJoint()
HAnimJoint735.DEF = "hanim_vt10"
HAnimJoint735.name = "vt10"
HAnimJoint735.center = [0.0056,1.2848,-0.0822]
HAnimSegment736 = x3d.HAnimSegment()
HAnimSegment736.DEF = "hanim_t10"
HAnimSegment736.name = "t10"
Transform737 = x3d.Transform()
Transform737.translation = [0.0056,1.2848,-0.0822]
Transform738 = x3d.Transform()
""" Empty Transform """
Shape739 = x3d.Shape()
Shape739.USE = "HAnimJointShape"

Transform738.children.append(Shape739)

Transform737.children.append(Transform738)

HAnimSegment736.children.append(Transform737)
Shape740 = x3d.Shape()
LineSet741 = x3d.LineSet()
LineSet741.vertexCount = [2]
Coordinate742 = x3d.Coordinate()

LineSet741.coord = Coordinate742
""" from vt10 to vt9 """
ColorRGBA743 = x3d.ColorRGBA()
ColorRGBA743.USE = "HAnimSegmentLineColorRGBA"

LineSet741.color = ColorRGBA743

Shape740.geometry = LineSet741

HAnimSegment736.children.append(Shape740)
HAnimSite744 = x3d.HAnimSite()
HAnimSite744.DEF = "hanim_l_thelion_pt"
HAnimSite744.name = "l_thelion_pt"
HAnimSite744.translation = [0.0918,1.3382,0.1192]
TouchSensor745 = x3d.TouchSensor()
TouchSensor745.description = "HAnimSite l_thelion_pt"

HAnimSite744.children.append(TouchSensor745)
Shape746 = x3d.Shape()
Shape746.USE = "HAnimSiteShape"

HAnimSite744.children.append(Shape746)

HAnimSegment736.children.append(HAnimSite744)
HAnimSite747 = x3d.HAnimSite()
HAnimSite747.DEF = "hanim_r_thelion_pt"
HAnimSite747.name = "r_thelion_pt"
HAnimSite747.translation = [-0.0736,1.3385,0.1217]
TouchSensor748 = x3d.TouchSensor()
TouchSensor748.description = "HAnimSite r_thelion_pt"

HAnimSite747.children.append(TouchSensor748)
Shape749 = x3d.Shape()
Shape749.USE = "HAnimSiteShape"

HAnimSite747.children.append(Shape749)

HAnimSegment736.children.append(HAnimSite747)

HAnimJoint735.children.append(HAnimSegment736)
HAnimJoint750 = x3d.HAnimJoint()
HAnimJoint750.DEF = "hanim_vt9"
HAnimJoint750.name = "vt9"
HAnimJoint750.center = [0.0057,1.3126,-0.0838]
HAnimSegment751 = x3d.HAnimSegment()
HAnimSegment751.DEF = "hanim_t9"
HAnimSegment751.name = "t9"
Transform752 = x3d.Transform()
Transform752.translation = [0.0057,1.3126,-0.0838]
Transform753 = x3d.Transform()
""" Empty Transform """
Shape754 = x3d.Shape()
Shape754.USE = "HAnimJointShape"

Transform753.children.append(Shape754)

Transform752.children.append(Transform753)

HAnimSegment751.children.append(Transform752)
Shape755 = x3d.Shape()
LineSet756 = x3d.LineSet()
LineSet756.vertexCount = [2]
Coordinate757 = x3d.Coordinate()

LineSet756.coord = Coordinate757
""" from vt9 to vt8 """
ColorRGBA758 = x3d.ColorRGBA()
ColorRGBA758.USE = "HAnimSegmentLineColorRGBA"

LineSet756.color = ColorRGBA758

Shape755.geometry = LineSet756

HAnimSegment751.children.append(Shape755)

HAnimJoint750.children.append(HAnimSegment751)
HAnimJoint759 = x3d.HAnimJoint()
HAnimJoint759.DEF = "hanim_vt8"
HAnimJoint759.name = "vt8"
HAnimJoint759.center = [0.0057,1.3382,-0.0845]
HAnimSegment760 = x3d.HAnimSegment()
HAnimSegment760.DEF = "hanim_t8"
HAnimSegment760.name = "t8"
Transform761 = x3d.Transform()
Transform761.translation = [0.0057,1.3382,-0.0845]
Transform762 = x3d.Transform()
""" Empty Transform """
Shape763 = x3d.Shape()
Shape763.USE = "HAnimJointShape"

Transform762.children.append(Shape763)

Transform761.children.append(Transform762)

HAnimSegment760.children.append(Transform761)
Shape764 = x3d.Shape()
LineSet765 = x3d.LineSet()
LineSet765.vertexCount = [2]
Coordinate766 = x3d.Coordinate()

LineSet765.coord = Coordinate766
""" from vt8 to vt7 """
ColorRGBA767 = x3d.ColorRGBA()
ColorRGBA767.USE = "HAnimSegmentLineColorRGBA"

LineSet765.color = ColorRGBA767

Shape764.geometry = LineSet765

HAnimSegment760.children.append(Shape764)

HAnimJoint759.children.append(HAnimSegment760)
HAnimJoint768 = x3d.HAnimJoint()
HAnimJoint768.DEF = "hanim_vt7"
HAnimJoint768.name = "vt7"
HAnimJoint768.center = [0.0058,1.3625,-0.0833]
HAnimSegment769 = x3d.HAnimSegment()
HAnimSegment769.DEF = "hanim_t7"
HAnimSegment769.name = "t7"
Transform770 = x3d.Transform()
Transform770.translation = [0.0058,1.3625,-0.0833]
Transform771 = x3d.Transform()
""" Empty Transform """
Shape772 = x3d.Shape()
Shape772.USE = "HAnimJointShape"

Transform771.children.append(Shape772)

Transform770.children.append(Transform771)

HAnimSegment769.children.append(Transform770)
Shape773 = x3d.Shape()
LineSet774 = x3d.LineSet()
LineSet774.vertexCount = [2]
Coordinate775 = x3d.Coordinate()

LineSet774.coord = Coordinate775
""" from vt7 to vt6 """
ColorRGBA776 = x3d.ColorRGBA()
ColorRGBA776.USE = "HAnimSegmentLineColorRGBA"

LineSet774.color = ColorRGBA776

Shape773.geometry = LineSet774

HAnimSegment769.children.append(Shape773)
HAnimSite777 = x3d.HAnimSite()
HAnimSite777.DEF = "hanim_l_chest_midsagittal_plane_pt"
HAnimSite777.name = "l_chest_midsagittal_plane_pt"
HAnimSite777.translation = [0,1,0]
TouchSensor778 = x3d.TouchSensor()
TouchSensor778.description = "HAnimSite l_chest_midsagittal_plane_pt"

HAnimSite777.children.append(TouchSensor778)
Shape779 = x3d.Shape()
Shape779.USE = "HAnimSiteShape"

HAnimSite777.children.append(Shape779)

HAnimSegment769.children.append(HAnimSite777)
HAnimSite780 = x3d.HAnimSite()
HAnimSite780.DEF = "hanim_mesosternale_pt"
HAnimSite780.name = "mesosternale_pt"
HAnimSite780.translation = [0,1,0]
TouchSensor781 = x3d.TouchSensor()
TouchSensor781.description = "HAnimSite mesosternale_pt"

HAnimSite780.children.append(TouchSensor781)
Shape782 = x3d.Shape()
Shape782.USE = "HAnimSiteShape"

HAnimSite780.children.append(Shape782)

HAnimSegment769.children.append(HAnimSite780)
HAnimSite783 = x3d.HAnimSite()
HAnimSite783.DEF = "hanim_r_chest_midsagittal_plane_pt"
HAnimSite783.name = "r_chest_midsagittal_plane_pt"
HAnimSite783.translation = [0,1,0]
TouchSensor784 = x3d.TouchSensor()
TouchSensor784.description = "HAnimSite r_chest_midsagittal_plane_pt"

HAnimSite783.children.append(TouchSensor784)
Shape785 = x3d.Shape()
Shape785.USE = "HAnimSiteShape"

HAnimSite783.children.append(Shape785)

HAnimSegment769.children.append(HAnimSite783)
HAnimSite786 = x3d.HAnimSite()
HAnimSite786.DEF = "hanim_rear_center_midsagittal_plane_pt"
HAnimSite786.name = "rear_center_midsagittal_plane_pt"
HAnimSite786.translation = [0,1,0]
TouchSensor787 = x3d.TouchSensor()
TouchSensor787.description = "HAnimSite rear_center_midsagittal_plane_pt"

HAnimSite786.children.append(TouchSensor787)
Shape788 = x3d.Shape()
Shape788.USE = "HAnimSiteShape"

HAnimSite786.children.append(Shape788)

HAnimSegment769.children.append(HAnimSite786)

HAnimJoint768.children.append(HAnimSegment769)
HAnimJoint789 = x3d.HAnimJoint()
HAnimJoint789.DEF = "hanim_vt6"
HAnimJoint789.name = "vt6"
HAnimJoint789.center = [0.0059,1.3866,-0.0800]
HAnimSegment790 = x3d.HAnimSegment()
HAnimSegment790.DEF = "hanim_t6"
HAnimSegment790.name = "t6"
Transform791 = x3d.Transform()
Transform791.translation = [0.0059,1.3866,-0.0800]
Transform792 = x3d.Transform()
""" Empty Transform """
Shape793 = x3d.Shape()
Shape793.USE = "HAnimJointShape"

Transform792.children.append(Shape793)

Transform791.children.append(Transform792)

HAnimSegment790.children.append(Transform791)
Shape794 = x3d.Shape()
LineSet795 = x3d.LineSet()
LineSet795.vertexCount = [2]
Coordinate796 = x3d.Coordinate()

LineSet795.coord = Coordinate796
""" from vt6 to vt5 """
ColorRGBA797 = x3d.ColorRGBA()
ColorRGBA797.USE = "HAnimSegmentLineColorRGBA"

LineSet795.color = ColorRGBA797

Shape794.geometry = LineSet795

HAnimSegment790.children.append(Shape794)
HAnimSite798 = x3d.HAnimSite()
HAnimSite798.DEF = "hanim_spine_1_middle_back_pt"
HAnimSite798.name = "spine_1_middle_back_pt"
HAnimSite798.translation = [0,1,0]
TouchSensor799 = x3d.TouchSensor()
TouchSensor799.description = "HAnimSite spine_1_middle_back_pt"

HAnimSite798.children.append(TouchSensor799)
Shape800 = x3d.Shape()
Shape800.USE = "HAnimSiteShape"

HAnimSite798.children.append(Shape800)

HAnimSegment790.children.append(HAnimSite798)

HAnimJoint789.children.append(HAnimSegment790)
HAnimJoint801 = x3d.HAnimJoint()
HAnimJoint801.DEF = "hanim_vt5"
HAnimJoint801.name = "vt5"
HAnimJoint801.center = [0.0060,1.4102,-0.0745]
HAnimSegment802 = x3d.HAnimSegment()
HAnimSegment802.DEF = "hanim_t5"
HAnimSegment802.name = "t5"
Transform803 = x3d.Transform()
Transform803.translation = [0.0060,1.4102,-0.0745]
Transform804 = x3d.Transform()
""" Empty Transform """
Shape805 = x3d.Shape()
Shape805.USE = "HAnimJointShape"

Transform804.children.append(Shape805)

Transform803.children.append(Transform804)

HAnimSegment802.children.append(Transform803)
Shape806 = x3d.Shape()
LineSet807 = x3d.LineSet()
LineSet807.vertexCount = [2]
Coordinate808 = x3d.Coordinate()

LineSet807.coord = Coordinate808
""" from vt5 to vt4 """
ColorRGBA809 = x3d.ColorRGBA()
ColorRGBA809.USE = "HAnimSegmentLineColorRGBA"

LineSet807.color = ColorRGBA809

Shape806.geometry = LineSet807

HAnimSegment802.children.append(Shape806)

HAnimJoint801.children.append(HAnimSegment802)
HAnimJoint810 = x3d.HAnimJoint()
HAnimJoint810.DEF = "hanim_vt4"
HAnimJoint810.name = "vt4"
HAnimJoint810.center = [0.0061,1.4320,-0.0675]
HAnimSegment811 = x3d.HAnimSegment()
HAnimSegment811.DEF = "hanim_t4"
HAnimSegment811.name = "t4"
Transform812 = x3d.Transform()
Transform812.translation = [0.0061,1.4320,-0.0675]
Transform813 = x3d.Transform()
""" Empty Transform """
Shape814 = x3d.Shape()
Shape814.USE = "HAnimJointShape"

Transform813.children.append(Shape814)

Transform812.children.append(Transform813)

HAnimSegment811.children.append(Transform812)
Shape815 = x3d.Shape()
LineSet816 = x3d.LineSet()
LineSet816.vertexCount = [2]
Coordinate817 = x3d.Coordinate()

LineSet816.coord = Coordinate817
""" from vt4 to vt3 """
ColorRGBA818 = x3d.ColorRGBA()
ColorRGBA818.USE = "HAnimSegmentLineColorRGBA"

LineSet816.color = ColorRGBA818

Shape815.geometry = LineSet816

HAnimSegment811.children.append(Shape815)

HAnimJoint810.children.append(HAnimSegment811)
HAnimJoint819 = x3d.HAnimJoint()
HAnimJoint819.DEF = "hanim_vt3"
HAnimJoint819.name = "vt3"
HAnimJoint819.center = [0.0062,1.4583,-0.0570]
HAnimSegment820 = x3d.HAnimSegment()
HAnimSegment820.DEF = "hanim_t3"
HAnimSegment820.name = "t3"
Transform821 = x3d.Transform()
Transform821.translation = [0.0062,1.4583,-0.0570]
Transform822 = x3d.Transform()
""" Empty Transform """
Shape823 = x3d.Shape()
Shape823.USE = "HAnimJointShape"

Transform822.children.append(Shape823)

Transform821.children.append(Transform822)

HAnimSegment820.children.append(Transform821)
Shape824 = x3d.Shape()
LineSet825 = x3d.LineSet()
LineSet825.vertexCount = [2]
Coordinate826 = x3d.Coordinate()

LineSet825.coord = Coordinate826
""" from vt3 to vt2 """
ColorRGBA827 = x3d.ColorRGBA()
ColorRGBA827.USE = "HAnimSegmentLineColorRGBA"

LineSet825.color = ColorRGBA827

Shape824.geometry = LineSet825

HAnimSegment820.children.append(Shape824)

HAnimJoint819.children.append(HAnimSegment820)
HAnimJoint828 = x3d.HAnimJoint()
HAnimJoint828.DEF = "hanim_vt2"
HAnimJoint828.name = "vt2"
HAnimJoint828.center = [0.0063,1.4761,-0.0484]
HAnimSegment829 = x3d.HAnimSegment()
HAnimSegment829.DEF = "hanim_t2"
HAnimSegment829.name = "t2"
Transform830 = x3d.Transform()
Transform830.translation = [0.0063,1.4761,-0.0484]
Transform831 = x3d.Transform()
""" Empty Transform """
Shape832 = x3d.Shape()
Shape832.USE = "HAnimJointShape"

Transform831.children.append(Shape832)

Transform830.children.append(Transform831)

HAnimSegment829.children.append(Transform830)
Shape833 = x3d.Shape()
LineSet834 = x3d.LineSet()
LineSet834.vertexCount = [2]
Coordinate835 = x3d.Coordinate()

LineSet834.coord = Coordinate835
""" from vt2 to vt1 """
ColorRGBA836 = x3d.ColorRGBA()
ColorRGBA836.USE = "HAnimSegmentLineColorRGBA"

LineSet834.color = ColorRGBA836

Shape833.geometry = LineSet834

HAnimSegment829.children.append(Shape833)
HAnimSite837 = x3d.HAnimSite()
HAnimSite837.DEF = "hanim_cervicale_pt"
HAnimSite837.name = "cervicale_pt"
HAnimSite837.translation = [0.0064,1.520,-0.0815]
TouchSensor838 = x3d.TouchSensor()
TouchSensor838.description = "HAnimSite cervicale_pt"

HAnimSite837.children.append(TouchSensor838)
Shape839 = x3d.Shape()
Shape839.USE = "HAnimSiteShape"

HAnimSite837.children.append(Shape839)

HAnimSegment829.children.append(HAnimSite837)
HAnimSite840 = x3d.HAnimSite()
HAnimSite840.DEF = "hanim_suprasternale_pt"
HAnimSite840.name = "suprasternale_pt"
HAnimSite840.translation = [0.0084,1.4714,0.0551]
TouchSensor841 = x3d.TouchSensor()
TouchSensor841.description = "HAnimSite suprasternale_pt"

HAnimSite840.children.append(TouchSensor841)
Shape842 = x3d.Shape()
Shape842.USE = "HAnimSiteShape"

HAnimSite840.children.append(Shape842)

HAnimSegment829.children.append(HAnimSite840)

HAnimJoint828.children.append(HAnimSegment829)
HAnimJoint843 = x3d.HAnimJoint()
HAnimJoint843.DEF = "hanim_vt1"
HAnimJoint843.name = "vt1"
HAnimJoint843.center = [0.0065,1.4951,-0.0387]
HAnimSegment844 = x3d.HAnimSegment()
HAnimSegment844.DEF = "hanim_t1"
HAnimSegment844.name = "t1"
Transform845 = x3d.Transform()
Transform845.translation = [0.0065,1.4951,-0.0387]
Transform846 = x3d.Transform()
""" Empty Transform """
Shape847 = x3d.Shape()
Shape847.USE = "HAnimJointShape"

Transform846.children.append(Shape847)

Transform845.children.append(Transform846)

HAnimSegment844.children.append(Transform845)
Shape848 = x3d.Shape()
LineSet849 = x3d.LineSet()
LineSet849.vertexCount = [2]
Coordinate850 = x3d.Coordinate()

LineSet849.coord = Coordinate850
""" from vt1 to vc7 """
ColorRGBA851 = x3d.ColorRGBA()
ColorRGBA851.USE = "HAnimSegmentLineColorRGBA"

LineSet849.color = ColorRGBA851

Shape848.geometry = LineSet849

HAnimSegment844.children.append(Shape848)
HAnimSite852 = x3d.HAnimSite()
HAnimSite852.DEF = "hanim_l_neck_base_pt"
HAnimSite852.name = "l_neck_base_pt"
HAnimSite852.translation = [0.0646,1.5141,-0.0380]
TouchSensor853 = x3d.TouchSensor()
TouchSensor853.description = "HAnimSite l_neck_base_pt"

HAnimSite852.children.append(TouchSensor853)
Shape854 = x3d.Shape()
Shape854.USE = "HAnimSiteShape"

HAnimSite852.children.append(Shape854)

HAnimSegment844.children.append(HAnimSite852)
HAnimSite855 = x3d.HAnimSite()
HAnimSite855.DEF = "hanim_r_neck_base_pt"
HAnimSite855.name = "r_neck_base_pt"
HAnimSite855.translation = [-0.0419,1.5149,-0.0220]
TouchSensor856 = x3d.TouchSensor()
TouchSensor856.description = "HAnimSite r_neck_base_pt"

HAnimSite855.children.append(TouchSensor856)
Shape857 = x3d.Shape()
Shape857.USE = "HAnimSiteShape"

HAnimSite855.children.append(Shape857)

HAnimSegment844.children.append(HAnimSite855)
Shape858 = x3d.Shape()
LineSet859 = x3d.LineSet()
LineSet859.vertexCount = [2]
Coordinate860 = x3d.Coordinate()

LineSet859.coord = Coordinate860
""" from vt1 to l_sternoclavicular """
ColorRGBA861 = x3d.ColorRGBA()
ColorRGBA861.USE = "HAnimSegmentLineColorRGBA"

LineSet859.color = ColorRGBA861

Shape858.geometry = LineSet859

HAnimSegment844.children.append(Shape858)
HAnimSite862 = x3d.HAnimSite()
HAnimSite862.DEF = "hanim_l_acromion_pt"
HAnimSite862.name = "l_acromion_pt"
HAnimSite862.translation = [0.2032,1.4760,-0.0490]
TouchSensor863 = x3d.TouchSensor()
TouchSensor863.description = "HAnimSite l_acromion_pt"

HAnimSite862.children.append(TouchSensor863)
Shape864 = x3d.Shape()
Shape864.USE = "HAnimSiteShape"

HAnimSite862.children.append(Shape864)

HAnimSegment844.children.append(HAnimSite862)
HAnimSite865 = x3d.HAnimSite()
HAnimSite865.DEF = "hanim_l_axilla_distal_pt"
HAnimSite865.name = "l_axilla_distal_pt"
HAnimSite865.translation = [0.1706,1.4072,-0.0875]
TouchSensor866 = x3d.TouchSensor()
TouchSensor866.description = "HAnimSite l_axilla_distal_pt"

HAnimSite865.children.append(TouchSensor866)
Shape867 = x3d.Shape()
Shape867.USE = "HAnimSiteShape"

HAnimSite865.children.append(Shape867)

HAnimSegment844.children.append(HAnimSite865)
HAnimSite868 = x3d.HAnimSite()
HAnimSite868.DEF = "hanim_l_axilla_posterior_folds_pt"
HAnimSite868.name = "l_axilla_posterior_folds_pt"
HAnimSite868.translation = [0,1,0]
TouchSensor869 = x3d.TouchSensor()
TouchSensor869.description = "HAnimSite l_axilla_posterior_folds_pt"

HAnimSite868.children.append(TouchSensor869)
Shape870 = x3d.Shape()
Shape870.USE = "HAnimSiteShape"

HAnimSite868.children.append(Shape870)

HAnimSegment844.children.append(HAnimSite868)
HAnimSite871 = x3d.HAnimSite()
HAnimSite871.DEF = "hanim_l_axilla_proximal_pt"
HAnimSite871.name = "l_axilla_proximal_pt"
HAnimSite871.translation = [0.1777,1.4065,-0.0075]
TouchSensor872 = x3d.TouchSensor()
TouchSensor872.description = "HAnimSite l_axilla_proximal_pt"

HAnimSite871.children.append(TouchSensor872)
Shape873 = x3d.Shape()
Shape873.USE = "HAnimSiteShape"

HAnimSite871.children.append(Shape873)

HAnimSegment844.children.append(HAnimSite871)
HAnimSite874 = x3d.HAnimSite()
HAnimSite874.DEF = "hanim_l_clavicale_pt"
HAnimSite874.name = "l_clavicale_pt"
HAnimSite874.translation = [0.0271,1.4943,0.0394]
TouchSensor875 = x3d.TouchSensor()
TouchSensor875.description = "HAnimSite l_clavicale_pt"

HAnimSite874.children.append(TouchSensor875)
Shape876 = x3d.Shape()
Shape876.USE = "HAnimSiteShape"

HAnimSite874.children.append(Shape876)

HAnimSegment844.children.append(HAnimSite874)
Shape877 = x3d.Shape()
LineSet878 = x3d.LineSet()
LineSet878.vertexCount = [2]
Coordinate879 = x3d.Coordinate()

LineSet878.coord = Coordinate879
""" from vt1 to r_sternoclavicular """
ColorRGBA880 = x3d.ColorRGBA()
ColorRGBA880.USE = "HAnimSegmentLineColorRGBA"

LineSet878.color = ColorRGBA880

Shape877.geometry = LineSet878

HAnimSegment844.children.append(Shape877)
HAnimSite881 = x3d.HAnimSite()
HAnimSite881.DEF = "hanim_r_acromion_pt"
HAnimSite881.name = "r_acromion_pt"
HAnimSite881.translation = [-0.1905,1.4791,-0.0431]
TouchSensor882 = x3d.TouchSensor()
TouchSensor882.description = "HAnimSite r_acromion_pt"

HAnimSite881.children.append(TouchSensor882)
Shape883 = x3d.Shape()
Shape883.USE = "HAnimSiteShape"

HAnimSite881.children.append(Shape883)

HAnimSegment844.children.append(HAnimSite881)
HAnimSite884 = x3d.HAnimSite()
HAnimSite884.DEF = "hanim_r_axilla_distal_pt"
HAnimSite884.name = "r_axilla_distal_pt"
HAnimSite884.translation = [-0.1603,1.4098,-0.0826]
TouchSensor885 = x3d.TouchSensor()
TouchSensor885.description = "HAnimSite r_axilla_distal_pt"

HAnimSite884.children.append(TouchSensor885)
Shape886 = x3d.Shape()
Shape886.USE = "HAnimSiteShape"

HAnimSite884.children.append(Shape886)

HAnimSegment844.children.append(HAnimSite884)
HAnimSite887 = x3d.HAnimSite()
HAnimSite887.DEF = "hanim_r_axilla_posterior_folds_pt"
HAnimSite887.name = "r_axilla_posterior_folds_pt"
HAnimSite887.translation = [0,1,0]
TouchSensor888 = x3d.TouchSensor()
TouchSensor888.description = "HAnimSite r_axilla_posterior_folds_pt"

HAnimSite887.children.append(TouchSensor888)
Shape889 = x3d.Shape()
Shape889.USE = "HAnimSiteShape"

HAnimSite887.children.append(Shape889)

HAnimSegment844.children.append(HAnimSite887)
HAnimSite890 = x3d.HAnimSite()
HAnimSite890.DEF = "hanim_r_axilla_proximal_pt"
HAnimSite890.name = "r_axilla_proximal_pt"
HAnimSite890.translation = [-0.1626,1.4072,-0.0031]
TouchSensor891 = x3d.TouchSensor()
TouchSensor891.description = "HAnimSite r_axilla_proximal_pt"

HAnimSite890.children.append(TouchSensor891)
Shape892 = x3d.Shape()
Shape892.USE = "HAnimSiteShape"

HAnimSite890.children.append(Shape892)

HAnimSegment844.children.append(HAnimSite890)
HAnimSite893 = x3d.HAnimSite()
HAnimSite893.DEF = "hanim_r_clavicale_pt"
HAnimSite893.name = "r_clavicale_pt"
HAnimSite893.translation = [-0.0115,1.4943,0.0400]
TouchSensor894 = x3d.TouchSensor()
TouchSensor894.description = "HAnimSite r_clavicale_pt"

HAnimSite893.children.append(TouchSensor894)
Shape895 = x3d.Shape()
Shape895.USE = "HAnimSiteShape"

HAnimSite893.children.append(Shape895)

HAnimSegment844.children.append(HAnimSite893)

HAnimJoint843.children.append(HAnimSegment844)
HAnimJoint896 = x3d.HAnimJoint()
HAnimJoint896.DEF = "hanim_vc7"
HAnimJoint896.name = "vc7"
HAnimJoint896.center = [0.0066,1.5132,-0.0301]
HAnimSegment897 = x3d.HAnimSegment()
HAnimSegment897.DEF = "hanim_c7"
HAnimSegment897.name = "c7"
Transform898 = x3d.Transform()
Transform898.translation = [0.0066,1.5132,-0.0301]
Transform899 = x3d.Transform()
""" Empty Transform """
Shape900 = x3d.Shape()
Shape900.USE = "HAnimJointShape"

Transform899.children.append(Shape900)

Transform898.children.append(Transform899)

HAnimSegment897.children.append(Transform898)
Shape901 = x3d.Shape()
LineSet902 = x3d.LineSet()
LineSet902.vertexCount = [2]
Coordinate903 = x3d.Coordinate()

LineSet902.coord = Coordinate903
""" from vc7 to vc6 """
ColorRGBA904 = x3d.ColorRGBA()
ColorRGBA904.USE = "HAnimSegmentLineColorRGBA"

LineSet902.color = ColorRGBA904

Shape901.geometry = LineSet902

HAnimSegment897.children.append(Shape901)

HAnimJoint896.children.append(HAnimSegment897)
HAnimJoint905 = x3d.HAnimJoint()
HAnimJoint905.DEF = "hanim_vc6"
HAnimJoint905.name = "vc6"
HAnimJoint905.center = [0.0066,1.5357,-0.0143]
HAnimSegment906 = x3d.HAnimSegment()
HAnimSegment906.DEF = "hanim_c6"
HAnimSegment906.name = "c6"
Transform907 = x3d.Transform()
Transform907.translation = [0.0066,1.5357,-0.0143]
Transform908 = x3d.Transform()
""" Empty Transform """
Shape909 = x3d.Shape()
Shape909.USE = "HAnimJointShape"

Transform908.children.append(Shape909)

Transform907.children.append(Transform908)

HAnimSegment906.children.append(Transform907)
Shape910 = x3d.Shape()
LineSet911 = x3d.LineSet()
LineSet911.vertexCount = [2]
Coordinate912 = x3d.Coordinate()

LineSet911.coord = Coordinate912
""" from vc6 to vc5 """
ColorRGBA913 = x3d.ColorRGBA()
ColorRGBA913.USE = "HAnimSegmentLineColorRGBA"

LineSet911.color = ColorRGBA913

Shape910.geometry = LineSet911

HAnimSegment906.children.append(Shape910)

HAnimJoint905.children.append(HAnimSegment906)
HAnimJoint914 = x3d.HAnimJoint()
HAnimJoint914.DEF = "hanim_vc5"
HAnimJoint914.name = "vc5"
HAnimJoint914.center = [0.0066,1.5520,-0.0082]
HAnimSegment915 = x3d.HAnimSegment()
HAnimSegment915.DEF = "hanim_c5"
HAnimSegment915.name = "c5"
Transform916 = x3d.Transform()
Transform916.translation = [0.0066,1.5520,-0.0082]
Transform917 = x3d.Transform()
""" Empty Transform """
Shape918 = x3d.Shape()
Shape918.USE = "HAnimJointShape"

Transform917.children.append(Shape918)

Transform916.children.append(Transform917)

HAnimSegment915.children.append(Transform916)
Shape919 = x3d.Shape()
LineSet920 = x3d.LineSet()
LineSet920.vertexCount = [2]
Coordinate921 = x3d.Coordinate()

LineSet920.coord = Coordinate921
""" from vc5 to vc4 """
ColorRGBA922 = x3d.ColorRGBA()
ColorRGBA922.USE = "HAnimSegmentLineColorRGBA"

LineSet920.color = ColorRGBA922

Shape919.geometry = LineSet920

HAnimSegment915.children.append(Shape919)

HAnimJoint914.children.append(HAnimSegment915)
HAnimJoint923 = x3d.HAnimJoint()
HAnimJoint923.DEF = "hanim_vc4"
HAnimJoint923.name = "vc4"
HAnimJoint923.center = [0.0066,1.5662,-0.0084]
HAnimSegment924 = x3d.HAnimSegment()
HAnimSegment924.DEF = "hanim_c4"
HAnimSegment924.name = "c4"
Transform925 = x3d.Transform()
Transform925.translation = [0.0066,1.5662,-0.0084]
Transform926 = x3d.Transform()
""" Empty Transform """
Shape927 = x3d.Shape()
Shape927.USE = "HAnimJointShape"

Transform926.children.append(Shape927)

Transform925.children.append(Transform926)

HAnimSegment924.children.append(Transform925)
Shape928 = x3d.Shape()
LineSet929 = x3d.LineSet()
LineSet929.vertexCount = [2]
Coordinate930 = x3d.Coordinate()

LineSet929.coord = Coordinate930
""" from vc4 to vc3 """
ColorRGBA931 = x3d.ColorRGBA()
ColorRGBA931.USE = "HAnimSegmentLineColorRGBA"

LineSet929.color = ColorRGBA931

Shape928.geometry = LineSet929

HAnimSegment924.children.append(Shape928)

HAnimJoint923.children.append(HAnimSegment924)
HAnimJoint932 = x3d.HAnimJoint()
HAnimJoint932.DEF = "hanim_vc3"
HAnimJoint932.name = "vc3"
HAnimJoint932.center = [0.0066,1.5800,-0.0103]
HAnimSegment933 = x3d.HAnimSegment()
HAnimSegment933.DEF = "hanim_c3"
HAnimSegment933.name = "c3"
Transform934 = x3d.Transform()
Transform934.translation = [0.0066,1.5800,-0.0103]
Transform935 = x3d.Transform()
""" Empty Transform """
Shape936 = x3d.Shape()
Shape936.USE = "HAnimJointShape"

Transform935.children.append(Shape936)

Transform934.children.append(Transform935)

HAnimSegment933.children.append(Transform934)
Shape937 = x3d.Shape()
LineSet938 = x3d.LineSet()
LineSet938.vertexCount = [2]
Coordinate939 = x3d.Coordinate()

LineSet938.coord = Coordinate939
""" from vc3 to vc2 """
ColorRGBA940 = x3d.ColorRGBA()
ColorRGBA940.USE = "HAnimSegmentLineColorRGBA"

LineSet938.color = ColorRGBA940

Shape937.geometry = LineSet938

HAnimSegment933.children.append(Shape937)
HAnimSite941 = x3d.HAnimSite()
HAnimSite941.DEF = "hanim_adams_apple_pt"
HAnimSite941.name = "adams_apple_pt"
HAnimSite941.translation = [0,1,0]
TouchSensor942 = x3d.TouchSensor()
TouchSensor942.description = "HAnimSite adams_apple_pt"

HAnimSite941.children.append(TouchSensor942)
Shape943 = x3d.Shape()
Shape943.USE = "HAnimSiteShape"

HAnimSite941.children.append(Shape943)

HAnimSegment933.children.append(HAnimSite941)

HAnimJoint932.children.append(HAnimSegment933)
HAnimJoint944 = x3d.HAnimJoint()
HAnimJoint944.DEF = "hanim_vc2"
HAnimJoint944.name = "vc2"
HAnimJoint944.center = [0.0066,1.5928,-0.0103]
HAnimSegment945 = x3d.HAnimSegment()
HAnimSegment945.DEF = "hanim_c2"
HAnimSegment945.name = "c2"
Transform946 = x3d.Transform()
Transform946.translation = [0.0066,1.5928,-0.0103]
Transform947 = x3d.Transform()
""" Empty Transform """
Shape948 = x3d.Shape()
Shape948.USE = "HAnimJointShape"

Transform947.children.append(Shape948)

Transform946.children.append(Transform947)

HAnimSegment945.children.append(Transform946)
Shape949 = x3d.Shape()
LineSet950 = x3d.LineSet()
LineSet950.vertexCount = [2]
Coordinate951 = x3d.Coordinate()

LineSet950.coord = Coordinate951
""" from vc2 to vc1 """
ColorRGBA952 = x3d.ColorRGBA()
ColorRGBA952.USE = "HAnimSegmentLineColorRGBA"

LineSet950.color = ColorRGBA952

Shape949.geometry = LineSet950

HAnimSegment945.children.append(Shape949)

HAnimJoint944.children.append(HAnimSegment945)
HAnimJoint953 = x3d.HAnimJoint()
HAnimJoint953.DEF = "hanim_vc1"
HAnimJoint953.name = "vc1"
HAnimJoint953.center = [0.0066,1.6144,-0.0034]
HAnimSegment954 = x3d.HAnimSegment()
HAnimSegment954.DEF = "hanim_c1"
HAnimSegment954.name = "c1"
Transform955 = x3d.Transform()
Transform955.translation = [0.0066,1.6144,-0.0034]
Transform956 = x3d.Transform()
""" Empty Transform """
Shape957 = x3d.Shape()
Shape957.USE = "HAnimJointShape"

Transform956.children.append(Shape957)

Transform955.children.append(Transform956)

HAnimSegment954.children.append(Transform955)
Shape958 = x3d.Shape()
LineSet959 = x3d.LineSet()
LineSet959.vertexCount = [2]
Coordinate960 = x3d.Coordinate()

LineSet959.coord = Coordinate960
""" from vc1 to skullbase """
ColorRGBA961 = x3d.ColorRGBA()
ColorRGBA961.USE = "HAnimSegmentLineColorRGBA"

LineSet959.color = ColorRGBA961

Shape958.geometry = LineSet959

HAnimSegment954.children.append(Shape958)
HAnimSite962 = x3d.HAnimSite()
HAnimSite962.DEF = "hanim_glabella_pt"
HAnimSite962.name = "glabella_pt"
HAnimSite962.translation = [0,1,0]
TouchSensor963 = x3d.TouchSensor()
TouchSensor963.description = "HAnimSite glabella_pt"

HAnimSite962.children.append(TouchSensor963)
Shape964 = x3d.Shape()
Shape964.USE = "HAnimSiteShape"

HAnimSite962.children.append(Shape964)

HAnimSegment954.children.append(HAnimSite962)
HAnimSite965 = x3d.HAnimSite()
HAnimSite965.DEF = "hanim_l_ectocanthus_pt"
HAnimSite965.name = "l_ectocanthus_pt"
HAnimSite965.translation = [0,1,0]
TouchSensor966 = x3d.TouchSensor()
TouchSensor966.description = "HAnimSite l_ectocanthus_pt"

HAnimSite965.children.append(TouchSensor966)
Shape967 = x3d.Shape()
Shape967.USE = "HAnimSiteShape"

HAnimSite965.children.append(Shape967)

HAnimSegment954.children.append(HAnimSite965)
HAnimSite968 = x3d.HAnimSite()
HAnimSite968.DEF = "hanim_l_infraorbitale_pt"
HAnimSite968.name = "l_infraorbitale_pt"
HAnimSite968.translation = [0.0341,1.6171,0.0752]
TouchSensor969 = x3d.TouchSensor()
TouchSensor969.description = "HAnimSite l_infraorbitale_pt"

HAnimSite968.children.append(TouchSensor969)
Shape970 = x3d.Shape()
Shape970.USE = "HAnimSiteShape"

HAnimSite968.children.append(Shape970)

HAnimSegment954.children.append(HAnimSite968)
HAnimSite971 = x3d.HAnimSite()
HAnimSite971.DEF = "hanim_l_tragion_pt"
HAnimSite971.name = "l_tragion_pt"
HAnimSite971.translation = [0.0739,1.6348,0.0282]
TouchSensor972 = x3d.TouchSensor()
TouchSensor972.description = "HAnimSite l_tragion_pt"

HAnimSite971.children.append(TouchSensor972)
Shape973 = x3d.Shape()
Shape973.USE = "HAnimSiteShape"

HAnimSite971.children.append(Shape973)

HAnimSegment954.children.append(HAnimSite971)
HAnimSite974 = x3d.HAnimSite()
HAnimSite974.DEF = "hanim_nuchale_pt"
HAnimSite974.name = "nuchale_pt"
HAnimSite974.translation = [0.0039,1.5972,-0.0796]
TouchSensor975 = x3d.TouchSensor()
TouchSensor975.description = "HAnimSite nuchale_pt"

HAnimSite974.children.append(TouchSensor975)
Shape976 = x3d.Shape()
Shape976.USE = "HAnimSiteShape"

HAnimSite974.children.append(Shape976)

HAnimSegment954.children.append(HAnimSite974)
HAnimSite977 = x3d.HAnimSite()
HAnimSite977.DEF = "hanim_opisthocranion_pt"
HAnimSite977.name = "opisthocranion_pt"
HAnimSite977.translation = [0,1,0]
TouchSensor978 = x3d.TouchSensor()
TouchSensor978.description = "HAnimSite opisthocranion_pt"

HAnimSite977.children.append(TouchSensor978)
Shape979 = x3d.Shape()
Shape979.USE = "HAnimSiteShape"

HAnimSite977.children.append(Shape979)

HAnimSegment954.children.append(HAnimSite977)
HAnimSite980 = x3d.HAnimSite()
HAnimSite980.DEF = "hanim_r_ectocanthus_pt"
HAnimSite980.name = "r_ectocanthus_pt"
HAnimSite980.translation = [0,1,0]
TouchSensor981 = x3d.TouchSensor()
TouchSensor981.description = "HAnimSite r_ectocanthus_pt"

HAnimSite980.children.append(TouchSensor981)
Shape982 = x3d.Shape()
Shape982.USE = "HAnimSiteShape"

HAnimSite980.children.append(Shape982)

HAnimSegment954.children.append(HAnimSite980)
HAnimSite983 = x3d.HAnimSite()
HAnimSite983.DEF = "hanim_r_infraorbitale_pt"
HAnimSite983.name = "r_infraorbitale_pt"
HAnimSite983.translation = [-0.0237,1.6171,0.0752]
TouchSensor984 = x3d.TouchSensor()
TouchSensor984.description = "HAnimSite r_infraorbitale_pt"

HAnimSite983.children.append(TouchSensor984)
Shape985 = x3d.Shape()
Shape985.USE = "HAnimSiteShape"

HAnimSite983.children.append(Shape985)

HAnimSegment954.children.append(HAnimSite983)
HAnimSite986 = x3d.HAnimSite()
HAnimSite986.DEF = "hanim_r_tragion_pt"
HAnimSite986.name = "r_tragion_pt"
HAnimSite986.translation = [-0.0646,1.6347,0.0302]
TouchSensor987 = x3d.TouchSensor()
TouchSensor987.description = "HAnimSite r_tragion_pt"

HAnimSite986.children.append(TouchSensor987)
Shape988 = x3d.Shape()
Shape988.USE = "HAnimSiteShape"

HAnimSite986.children.append(Shape988)

HAnimSegment954.children.append(HAnimSite986)
HAnimSite989 = x3d.HAnimSite()
HAnimSite989.DEF = "hanim_sellion_pt"
HAnimSite989.name = "sellion_pt"
HAnimSite989.translation = [0.0058,1.6316,0.0852]
TouchSensor990 = x3d.TouchSensor()
TouchSensor990.description = "HAnimSite sellion_pt"

HAnimSite989.children.append(TouchSensor990)
Shape991 = x3d.Shape()
Shape991.USE = "HAnimSiteShape"

HAnimSite989.children.append(Shape991)

HAnimSegment954.children.append(HAnimSite989)
HAnimSite992 = x3d.HAnimSite()
HAnimSite992.DEF = "hanim_skull_vertex_pt"
HAnimSite992.name = "skull_vertex_pt"
HAnimSite992.translation = [0.0050,1.7504,0.0055]
TouchSensor993 = x3d.TouchSensor()
TouchSensor993.description = "HAnimSite skull_vertex_pt"

HAnimSite992.children.append(TouchSensor993)
Shape994 = x3d.Shape()
Shape994.USE = "HAnimSiteShape"

HAnimSite992.children.append(Shape994)

HAnimSegment954.children.append(HAnimSite992)

HAnimJoint953.children.append(HAnimSegment954)
HAnimJoint995 = x3d.HAnimJoint()
HAnimJoint995.DEF = "hanim_skullbase"
HAnimJoint995.name = "skullbase"
HAnimJoint995.center = [0.0044,1.6209,0.0236]
HAnimSegment996 = x3d.HAnimSegment()
HAnimSegment996.DEF = "hanim_skull"
HAnimSegment996.name = "skull"
Transform997 = x3d.Transform()
Transform997.translation = [0.0044,1.6209,0.0236]
Transform998 = x3d.Transform()
""" Empty Transform """
Shape999 = x3d.Shape()
Shape999.USE = "HAnimJointShape"

Transform998.children.append(Shape999)

Transform997.children.append(Transform998)

HAnimSegment996.children.append(Transform997)
Shape1000 = x3d.Shape()
LineSet1001 = x3d.LineSet()
LineSet1001.vertexCount = [2]
Coordinate1002 = x3d.Coordinate()

LineSet1001.coord = Coordinate1002
""" from skullbase to l_eyelid_joint """
ColorRGBA1003 = x3d.ColorRGBA()
ColorRGBA1003.USE = "HAnimSegmentLineColorRGBA"

LineSet1001.color = ColorRGBA1003

Shape1000.geometry = LineSet1001

HAnimSegment996.children.append(Shape1000)
Shape1004 = x3d.Shape()
LineSet1005 = x3d.LineSet()
LineSet1005.vertexCount = [2]
Coordinate1006 = x3d.Coordinate()

LineSet1005.coord = Coordinate1006
""" from skullbase to r_eyelid_joint """
ColorRGBA1007 = x3d.ColorRGBA()
ColorRGBA1007.USE = "HAnimSegmentLineColorRGBA"

LineSet1005.color = ColorRGBA1007

Shape1004.geometry = LineSet1005

HAnimSegment996.children.append(Shape1004)
Shape1008 = x3d.Shape()
LineSet1009 = x3d.LineSet()
LineSet1009.vertexCount = [2]
Coordinate1010 = x3d.Coordinate()

LineSet1009.coord = Coordinate1010
""" from skullbase to l_eyeball_joint """
ColorRGBA1011 = x3d.ColorRGBA()
ColorRGBA1011.USE = "HAnimSegmentLineColorRGBA"

LineSet1009.color = ColorRGBA1011

Shape1008.geometry = LineSet1009

HAnimSegment996.children.append(Shape1008)
Shape1012 = x3d.Shape()
LineSet1013 = x3d.LineSet()
LineSet1013.vertexCount = [2]
Coordinate1014 = x3d.Coordinate()

LineSet1013.coord = Coordinate1014
""" from skullbase to r_eyeball_joint """
ColorRGBA1015 = x3d.ColorRGBA()
ColorRGBA1015.USE = "HAnimSegmentLineColorRGBA"

LineSet1013.color = ColorRGBA1015

Shape1012.geometry = LineSet1013

HAnimSegment996.children.append(Shape1012)
Shape1016 = x3d.Shape()
LineSet1017 = x3d.LineSet()
LineSet1017.vertexCount = [2]
Coordinate1018 = x3d.Coordinate()

LineSet1017.coord = Coordinate1018
""" from skullbase to l_eyebrow_joint """
ColorRGBA1019 = x3d.ColorRGBA()
ColorRGBA1019.USE = "HAnimSegmentLineColorRGBA"

LineSet1017.color = ColorRGBA1019

Shape1016.geometry = LineSet1017

HAnimSegment996.children.append(Shape1016)
Shape1020 = x3d.Shape()
LineSet1021 = x3d.LineSet()
LineSet1021.vertexCount = [2]
Coordinate1022 = x3d.Coordinate()

LineSet1021.coord = Coordinate1022
""" from skullbase to r_eyebrow_joint """
ColorRGBA1023 = x3d.ColorRGBA()
ColorRGBA1023.USE = "HAnimSegmentLineColorRGBA"

LineSet1021.color = ColorRGBA1023

Shape1020.geometry = LineSet1021

HAnimSegment996.children.append(Shape1020)
Shape1024 = x3d.Shape()
LineSet1025 = x3d.LineSet()
LineSet1025.vertexCount = [2]
Coordinate1026 = x3d.Coordinate()

LineSet1025.coord = Coordinate1026
""" from skullbase to temporomandibular """
ColorRGBA1027 = x3d.ColorRGBA()
ColorRGBA1027.USE = "HAnimSegmentLineColorRGBA"

LineSet1025.color = ColorRGBA1027

Shape1024.geometry = LineSet1025

HAnimSegment996.children.append(Shape1024)
HAnimSite1028 = x3d.HAnimSite()
HAnimSite1028.DEF = "hanim_l_gonion_pt"
HAnimSite1028.name = "l_gonion_pt"
HAnimSite1028.translation = [0.0631,1.5530,0.0330]
TouchSensor1029 = x3d.TouchSensor()
TouchSensor1029.description = "HAnimSite l_gonion_pt"

HAnimSite1028.children.append(TouchSensor1029)
Shape1030 = x3d.Shape()
Shape1030.USE = "HAnimSiteShape"

HAnimSite1028.children.append(Shape1030)

HAnimSegment996.children.append(HAnimSite1028)
HAnimSite1031 = x3d.HAnimSite()
HAnimSite1031.DEF = "hanim_menton_pt"
HAnimSite1031.name = "menton_pt"
HAnimSite1031.translation = [0,1,0]
TouchSensor1032 = x3d.TouchSensor()
TouchSensor1032.description = "HAnimSite menton_pt"

HAnimSite1031.children.append(TouchSensor1032)
Shape1033 = x3d.Shape()
Shape1033.USE = "HAnimSiteShape"

HAnimSite1031.children.append(Shape1033)

HAnimSegment996.children.append(HAnimSite1031)
HAnimSite1034 = x3d.HAnimSite()
HAnimSite1034.DEF = "hanim_r_gonion_pt"
HAnimSite1034.name = "r_gonion_pt"
HAnimSite1034.translation = [-0.0520,1.5529,0.0347]
TouchSensor1035 = x3d.TouchSensor()
TouchSensor1035.description = "HAnimSite r_gonion_pt"

HAnimSite1034.children.append(TouchSensor1035)
Shape1036 = x3d.Shape()
Shape1036.USE = "HAnimSiteShape"

HAnimSite1034.children.append(Shape1036)

HAnimSegment996.children.append(HAnimSite1034)
HAnimSite1037 = x3d.HAnimSite()
HAnimSite1037.DEF = "hanim_supramenton_pt"
HAnimSite1037.name = "supramenton_pt"
HAnimSite1037.translation = [0.0061,1.5410,0.0805]
TouchSensor1038 = x3d.TouchSensor()
TouchSensor1038.description = "HAnimSite supramenton_pt"

HAnimSite1037.children.append(TouchSensor1038)
Shape1039 = x3d.Shape()
Shape1039.USE = "HAnimSiteShape"

HAnimSite1037.children.append(Shape1039)

HAnimSegment996.children.append(HAnimSite1037)

HAnimJoint995.children.append(HAnimSegment996)
HAnimJoint1040 = x3d.HAnimJoint()
HAnimJoint1040.DEF = "hanim_l_eyelid_joint"
HAnimJoint1040.name = "l_eyelid_joint"
HAnimJoint1040.center = [0,1,0]

HAnimJoint995.children.append(HAnimJoint1040)
HAnimJoint1041 = x3d.HAnimJoint()
HAnimJoint1041.DEF = "hanim_r_eyelid_joint"
HAnimJoint1041.name = "r_eyelid_joint"
HAnimJoint1041.center = [0,1,0]

HAnimJoint995.children.append(HAnimJoint1041)
HAnimJoint1042 = x3d.HAnimJoint()
HAnimJoint1042.DEF = "hanim_l_eyeball_joint"
HAnimJoint1042.name = "l_eyeball_joint"
HAnimJoint1042.center = [0,1,0]

HAnimJoint995.children.append(HAnimJoint1042)
HAnimJoint1043 = x3d.HAnimJoint()
HAnimJoint1043.DEF = "hanim_r_eyeball_joint"
HAnimJoint1043.name = "r_eyeball_joint"
HAnimJoint1043.center = [0,1,0]

HAnimJoint995.children.append(HAnimJoint1043)
HAnimJoint1044 = x3d.HAnimJoint()
HAnimJoint1044.DEF = "hanim_l_eyebrow_joint"
HAnimJoint1044.name = "l_eyebrow_joint"
HAnimJoint1044.center = [0,1,0]

HAnimJoint995.children.append(HAnimJoint1044)
HAnimJoint1045 = x3d.HAnimJoint()
HAnimJoint1045.DEF = "hanim_r_eyebrow_joint"
HAnimJoint1045.name = "r_eyebrow_joint"
HAnimJoint1045.center = [0,1,0]

HAnimJoint995.children.append(HAnimJoint1045)
HAnimJoint1046 = x3d.HAnimJoint()
HAnimJoint1046.DEF = "hanim_temporomandibular"
HAnimJoint1046.name = "temporomandibular"
HAnimJoint1046.center = [0,1,0]

HAnimJoint995.children.append(HAnimJoint1046)

HAnimJoint953.children.append(HAnimJoint995)

HAnimJoint944.children.append(HAnimJoint953)

HAnimJoint932.children.append(HAnimJoint944)

HAnimJoint923.children.append(HAnimJoint932)

HAnimJoint914.children.append(HAnimJoint923)

HAnimJoint905.children.append(HAnimJoint914)

HAnimJoint896.children.append(HAnimJoint905)

HAnimJoint843.children.append(HAnimJoint896)
HAnimJoint1047 = x3d.HAnimJoint()
HAnimJoint1047.DEF = "hanim_l_sternoclavicular"
HAnimJoint1047.name = "l_sternoclavicular"
HAnimJoint1047.center = [0.0820,1.4488,-0.0353]
HAnimSegment1048 = x3d.HAnimSegment()
HAnimSegment1048.DEF = "hanim_l_clavicle"
HAnimSegment1048.name = "l_clavicle"
Transform1049 = x3d.Transform()
Transform1049.translation = [0.0820,1.4488,-0.0353]
Transform1050 = x3d.Transform()
""" Empty Transform """
Shape1051 = x3d.Shape()
Shape1051.USE = "HAnimJointShape"

Transform1050.children.append(Shape1051)

Transform1049.children.append(Transform1050)

HAnimSegment1048.children.append(Transform1049)
Shape1052 = x3d.Shape()
LineSet1053 = x3d.LineSet()
LineSet1053.vertexCount = [2]
Coordinate1054 = x3d.Coordinate()

LineSet1053.coord = Coordinate1054
""" from l_sternoclavicular to l_acromioclavicular """
ColorRGBA1055 = x3d.ColorRGBA()
ColorRGBA1055.USE = "HAnimSegmentLineColorRGBA"

LineSet1053.color = ColorRGBA1055

Shape1052.geometry = LineSet1053

HAnimSegment1048.children.append(Shape1052)

HAnimJoint1047.children.append(HAnimSegment1048)
HAnimJoint1056 = x3d.HAnimJoint()
HAnimJoint1056.DEF = "hanim_l_acromioclavicular"
HAnimJoint1056.name = "l_acromioclavicular"
HAnimJoint1056.center = [0.0962,1.4269,-0.0424]
HAnimSegment1057 = x3d.HAnimSegment()
HAnimSegment1057.DEF = "hanim_l_scapula"
HAnimSegment1057.name = "l_scapula"
Transform1058 = x3d.Transform()
Transform1058.translation = [0.0962,1.4269,-0.0424]
Transform1059 = x3d.Transform()
""" Empty Transform """
Shape1060 = x3d.Shape()
Shape1060.USE = "HAnimJointShape"

Transform1059.children.append(Shape1060)

Transform1058.children.append(Transform1059)

HAnimSegment1057.children.append(Transform1058)
Shape1061 = x3d.Shape()
LineSet1062 = x3d.LineSet()
LineSet1062.vertexCount = [2]
Coordinate1063 = x3d.Coordinate()

LineSet1062.coord = Coordinate1063
""" from l_acromioclavicular to l_shoulder """
ColorRGBA1064 = x3d.ColorRGBA()
ColorRGBA1064.USE = "HAnimSegmentLineColorRGBA"

LineSet1062.color = ColorRGBA1064

Shape1061.geometry = LineSet1062

HAnimSegment1057.children.append(Shape1061)
HAnimSite1065 = x3d.HAnimSite()
HAnimSite1065.DEF = "hanim_l_bideltoid_pt"
HAnimSite1065.name = "l_bideltoid_pt"
HAnimSite1065.translation = [0,1,0]
TouchSensor1066 = x3d.TouchSensor()
TouchSensor1066.description = "HAnimSite l_bideltoid_pt"

HAnimSite1065.children.append(TouchSensor1066)
Shape1067 = x3d.Shape()
Shape1067.USE = "HAnimSiteShape"

HAnimSite1065.children.append(Shape1067)

HAnimSegment1057.children.append(HAnimSite1065)
HAnimSite1068 = x3d.HAnimSite()
HAnimSite1068.DEF = "hanim_l_humeral_lateral_epicondyles_pt"
HAnimSite1068.name = "l_humeral_lateral_epicondyles_pt"
HAnimSite1068.translation = [0.2280,1.1482,-0.1100]
TouchSensor1069 = x3d.TouchSensor()
TouchSensor1069.description = "HAnimSite l_humeral_lateral_epicondyles_pt"

HAnimSite1068.children.append(TouchSensor1069)
Shape1070 = x3d.Shape()
Shape1070.USE = "HAnimSiteShape"

HAnimSite1068.children.append(Shape1070)

HAnimSegment1057.children.append(HAnimSite1068)

HAnimJoint1056.children.append(HAnimSegment1057)
HAnimJoint1071 = x3d.HAnimJoint()
HAnimJoint1071.DEF = "hanim_l_shoulder"
HAnimJoint1071.name = "l_shoulder"
HAnimJoint1071.center = [0.2029,1.4376,-0.0387]
HAnimSegment1072 = x3d.HAnimSegment()
HAnimSegment1072.DEF = "hanim_l_upperarm"
HAnimSegment1072.name = "l_upperarm"
Transform1073 = x3d.Transform()
Transform1073.translation = [0.2029,1.4376,-0.0387]
Transform1074 = x3d.Transform()
""" Empty Transform """
Shape1075 = x3d.Shape()
Shape1075.USE = "HAnimJointShape"

Transform1074.children.append(Shape1075)

Transform1073.children.append(Transform1074)

HAnimSegment1072.children.append(Transform1073)
Shape1076 = x3d.Shape()
LineSet1077 = x3d.LineSet()
LineSet1077.vertexCount = [2]
Coordinate1078 = x3d.Coordinate()

LineSet1077.coord = Coordinate1078
""" from l_shoulder to l_elbow """
ColorRGBA1079 = x3d.ColorRGBA()
ColorRGBA1079.USE = "HAnimSegmentLineColorRGBA"

LineSet1077.color = ColorRGBA1079

Shape1076.geometry = LineSet1077

HAnimSegment1072.children.append(Shape1076)
HAnimSite1080 = x3d.HAnimSite()
HAnimSite1080.DEF = "hanim_l_humeral_medial_epicondyles_pt"
HAnimSite1080.name = "l_humeral_medial_epicondyles_pt"
HAnimSite1080.translation = [0.1735,1.1272,-0.1113]
TouchSensor1081 = x3d.TouchSensor()
TouchSensor1081.description = "HAnimSite l_humeral_medial_epicondyles_pt"

HAnimSite1080.children.append(TouchSensor1081)
Shape1082 = x3d.Shape()
Shape1082.USE = "HAnimSiteShape"

HAnimSite1080.children.append(Shape1082)

HAnimSegment1072.children.append(HAnimSite1080)
HAnimSite1083 = x3d.HAnimSite()
HAnimSite1083.DEF = "hanim_l_olecranon_pt"
HAnimSite1083.name = "l_olecranon_pt"
HAnimSite1083.translation = [-0.1962,1.1375,-0.1123]
TouchSensor1084 = x3d.TouchSensor()
TouchSensor1084.description = "HAnimSite l_olecranon_pt"

HAnimSite1083.children.append(TouchSensor1084)
Shape1085 = x3d.Shape()
Shape1085.USE = "HAnimSiteShape"

HAnimSite1083.children.append(Shape1085)

HAnimSegment1072.children.append(HAnimSite1083)
HAnimSite1086 = x3d.HAnimSite()
HAnimSite1086.DEF = "hanim_l_radial_styloid_pt"
HAnimSite1086.name = "l_radial_styloid_pt"
HAnimSite1086.translation = [0.1901,0.8645,-0.0415]
TouchSensor1087 = x3d.TouchSensor()
TouchSensor1087.description = "HAnimSite l_radial_styloid_pt"

HAnimSite1086.children.append(TouchSensor1087)
Shape1088 = x3d.Shape()
Shape1088.USE = "HAnimSiteShape"

HAnimSite1086.children.append(Shape1088)

HAnimSegment1072.children.append(HAnimSite1086)
HAnimSite1089 = x3d.HAnimSite()
HAnimSite1089.DEF = "hanim_l_radiale_pt"
HAnimSite1089.name = "l_radiale_pt"
HAnimSite1089.translation = [0.2182,1.1212,-0.1167]
TouchSensor1090 = x3d.TouchSensor()
TouchSensor1090.description = "HAnimSite l_radiale_pt"

HAnimSite1089.children.append(TouchSensor1090)
Shape1091 = x3d.Shape()
Shape1091.USE = "HAnimSiteShape"

HAnimSite1089.children.append(Shape1091)

HAnimSegment1072.children.append(HAnimSite1089)

HAnimJoint1071.children.append(HAnimSegment1072)
HAnimJoint1092 = x3d.HAnimJoint()
HAnimJoint1092.DEF = "hanim_l_elbow"
HAnimJoint1092.name = "l_elbow"
HAnimJoint1092.center = [0.2014,1.1357,-0.0682]
HAnimSegment1093 = x3d.HAnimSegment()
HAnimSegment1093.DEF = "hanim_l_forearm"
HAnimSegment1093.name = "l_forearm"
Transform1094 = x3d.Transform()
Transform1094.translation = [0.2014,1.1357,-0.0682]
Transform1095 = x3d.Transform()
""" Empty Transform """
Shape1096 = x3d.Shape()
Shape1096.USE = "HAnimJointShape"

Transform1095.children.append(Shape1096)

Transform1094.children.append(Transform1095)

HAnimSegment1093.children.append(Transform1094)
Shape1097 = x3d.Shape()
LineSet1098 = x3d.LineSet()
LineSet1098.vertexCount = [2]
Coordinate1099 = x3d.Coordinate()

LineSet1098.coord = Coordinate1099
""" from l_elbow to l_radiocarpal """
ColorRGBA1100 = x3d.ColorRGBA()
ColorRGBA1100.USE = "HAnimSegmentLineColorRGBA"

LineSet1098.color = ColorRGBA1100

Shape1097.geometry = LineSet1098

HAnimSegment1093.children.append(Shape1097)
HAnimSite1101 = x3d.HAnimSite()
HAnimSite1101.DEF = "hanim_l_ulnar_styloid_pt"
HAnimSite1101.name = "l_ulnar_styloid_pt"
HAnimSite1101.translation = [-0.2142,0.8529,-0.0648]
TouchSensor1102 = x3d.TouchSensor()
TouchSensor1102.description = "HAnimSite l_ulnar_styloid_pt"

HAnimSite1101.children.append(TouchSensor1102)
Shape1103 = x3d.Shape()
Shape1103.USE = "HAnimSiteShape"

HAnimSite1101.children.append(Shape1103)

HAnimSegment1093.children.append(HAnimSite1101)

HAnimJoint1092.children.append(HAnimSegment1093)
HAnimJoint1104 = x3d.HAnimJoint()
HAnimJoint1104.DEF = "hanim_l_radiocarpal"
HAnimJoint1104.name = "l_radiocarpal"
HAnimJoint1104.center = [0.1984,0.8663,-0.0583]
HAnimSegment1105 = x3d.HAnimSegment()
HAnimSegment1105.DEF = "hanim_l_carpal"
HAnimSegment1105.name = "l_carpal"
Transform1106 = x3d.Transform()
Transform1106.scale = [0.2,0.2,0.2]
Transform1106.translation = [0.20,0.85,-0.05]
Transform1106.rotation = [0,0,1,-3.14]
""" Transform left hand """
Transform1107 = x3d.Transform()
Transform1107.rotation = [0,1,0,-1.57]
""" Transform left hand """
Shape1108 = x3d.Shape()
Shape1108.USE = "HAnimJointShape"

Transform1107.children.append(Shape1108)

Transform1106.children.append(Transform1107)

HAnimSegment1105.children.append(Transform1106)
Shape1109 = x3d.Shape()
LineSet1110 = x3d.LineSet()
LineSet1110.vertexCount = [2]
Coordinate1111 = x3d.Coordinate()

LineSet1110.coord = Coordinate1111
""" from l_radiocarpal to l_midcarpal_1 """
ColorRGBA1112 = x3d.ColorRGBA()
ColorRGBA1112.USE = "HAnimSegmentLineColorRGBA"

LineSet1110.color = ColorRGBA1112

Shape1109.geometry = LineSet1110

HAnimSegment1105.children.append(Shape1109)
Shape1113 = x3d.Shape()
LineSet1114 = x3d.LineSet()
LineSet1114.vertexCount = [2]
Coordinate1115 = x3d.Coordinate()

LineSet1114.coord = Coordinate1115
""" from l_radiocarpal to l_midcarpal_2 """
ColorRGBA1116 = x3d.ColorRGBA()
ColorRGBA1116.USE = "HAnimSegmentLineColorRGBA"

LineSet1114.color = ColorRGBA1116

Shape1113.geometry = LineSet1114

HAnimSegment1105.children.append(Shape1113)
Shape1117 = x3d.Shape()
LineSet1118 = x3d.LineSet()
LineSet1118.vertexCount = [2]
Coordinate1119 = x3d.Coordinate()

LineSet1118.coord = Coordinate1119
""" from l_radiocarpal to l_midcarpal_3 """
ColorRGBA1120 = x3d.ColorRGBA()
ColorRGBA1120.USE = "HAnimSegmentLineColorRGBA"

LineSet1118.color = ColorRGBA1120

Shape1117.geometry = LineSet1118

HAnimSegment1105.children.append(Shape1117)
Shape1121 = x3d.Shape()
LineSet1122 = x3d.LineSet()
LineSet1122.vertexCount = [2]
Coordinate1123 = x3d.Coordinate()

LineSet1122.coord = Coordinate1123
""" from l_radiocarpal to l_midcarpal_4_5 """
ColorRGBA1124 = x3d.ColorRGBA()
ColorRGBA1124.USE = "HAnimSegmentLineColorRGBA"

LineSet1122.color = ColorRGBA1124

Shape1121.geometry = LineSet1122

HAnimSegment1105.children.append(Shape1121)

HAnimJoint1104.children.append(HAnimSegment1105)
HAnimJoint1125 = x3d.HAnimJoint()
HAnimJoint1125.DEF = "hanim_l_midcarpal_1"
HAnimJoint1125.name = "l_midcarpal_1"
HAnimJoint1125.center = [0,1,0]
HAnimSegment1126 = x3d.HAnimSegment()
HAnimSegment1126.DEF = "hanim_l_trapezium"
HAnimSegment1126.name = "l_trapezium"
Transform1127 = x3d.Transform()
Transform1127.translation = [0,1,0]
Transform1128 = x3d.Transform()
""" Empty Transform """
Shape1129 = x3d.Shape()
Shape1129.USE = "HAnimJointShape"

Transform1128.children.append(Shape1129)

Transform1127.children.append(Transform1128)

HAnimSegment1126.children.append(Transform1127)
Shape1130 = x3d.Shape()
LineSet1131 = x3d.LineSet()
LineSet1131.vertexCount = [1]
Coordinate1132 = x3d.Coordinate()

LineSet1131.coord = Coordinate1132
""" from l_midcarpal_1 to l_carpometacarpal_1 """
ColorRGBA1133 = x3d.ColorRGBA()
ColorRGBA1133.USE = "HAnimSegmentLineColorRGBA"

LineSet1131.color = ColorRGBA1133

Shape1130.geometry = LineSet1131

HAnimSegment1126.children.append(Shape1130)

HAnimJoint1125.children.append(HAnimSegment1126)
HAnimJoint1134 = x3d.HAnimJoint()
HAnimJoint1134.DEF = "hanim_l_carpometacarpal_1"
HAnimJoint1134.name = "l_carpometacarpal_1"
HAnimJoint1134.center = [0.1924,0.8472,-0.0534]
HAnimSegment1135 = x3d.HAnimSegment()
HAnimSegment1135.DEF = "hanim_l_metacarpal_1"
HAnimSegment1135.name = "l_metacarpal_1"
Transform1136 = x3d.Transform()
Transform1136.translation = [0.1924,0.8472,-0.0534]
Transform1137 = x3d.Transform()
""" Empty Transform """
Shape1138 = x3d.Shape()
Shape1138.USE = "HAnimJointShape"

Transform1137.children.append(Shape1138)

Transform1136.children.append(Transform1137)

HAnimSegment1135.children.append(Transform1136)
Shape1139 = x3d.Shape()
LineSet1140 = x3d.LineSet()
LineSet1140.vertexCount = [2]
Coordinate1141 = x3d.Coordinate()

LineSet1140.coord = Coordinate1141
""" from l_carpometacarpal_1 to l_metacarpophalangeal_1 """
ColorRGBA1142 = x3d.ColorRGBA()
ColorRGBA1142.USE = "HAnimSegmentLineColorRGBA"

LineSet1140.color = ColorRGBA1142

Shape1139.geometry = LineSet1140

HAnimSegment1135.children.append(Shape1139)

HAnimJoint1134.children.append(HAnimSegment1135)
HAnimJoint1143 = x3d.HAnimJoint()
HAnimJoint1143.DEF = "hanim_l_metacarpophalangeal_1"
HAnimJoint1143.name = "l_metacarpophalangeal_1"
HAnimJoint1143.center = [0.1951,0.8226,0.0246]
HAnimSegment1144 = x3d.HAnimSegment()
HAnimSegment1144.DEF = "hanim_l_carpal_proximal_phalanx_1"
HAnimSegment1144.name = "l_carpal_proximal_phalanx_1"
Transform1145 = x3d.Transform()
Transform1145.translation = [0.1951,0.8226,0.0246]
Transform1146 = x3d.Transform()
""" Empty Transform """
Shape1147 = x3d.Shape()
Shape1147.USE = "HAnimJointShape"

Transform1146.children.append(Shape1147)

Transform1145.children.append(Transform1146)

HAnimSegment1144.children.append(Transform1145)
Shape1148 = x3d.Shape()
LineSet1149 = x3d.LineSet()
LineSet1149.vertexCount = [2]
Coordinate1150 = x3d.Coordinate()

LineSet1149.coord = Coordinate1150
""" from l_metacarpophalangeal_1 to l_carpal_interphalangeal_1 """
ColorRGBA1151 = x3d.ColorRGBA()
ColorRGBA1151.USE = "HAnimSegmentLineColorRGBA"

LineSet1149.color = ColorRGBA1151

Shape1148.geometry = LineSet1149

HAnimSegment1144.children.append(Shape1148)
HAnimSite1152 = x3d.HAnimSite()
HAnimSite1152.DEF = "hanim_l_carpal_distal_phalanx_1_tip"
HAnimSite1152.name = "l_carpal_distal_phalanx_1_tip"
HAnimSite1152.translation = [0,1,0]
TouchSensor1153 = x3d.TouchSensor()
TouchSensor1153.description = "HAnimSite l_carpal_distal_phalanx_1_tip"

HAnimSite1152.children.append(TouchSensor1153)
Shape1154 = x3d.Shape()
Shape1154.USE = "HAnimSiteShape"

HAnimSite1152.children.append(Shape1154)

HAnimSegment1144.children.append(HAnimSite1152)

HAnimJoint1143.children.append(HAnimSegment1144)
HAnimJoint1155 = x3d.HAnimJoint()
HAnimJoint1155.DEF = "hanim_l_carpal_interphalangeal_1"
HAnimJoint1155.name = "l_carpal_interphalangeal_1"
HAnimJoint1155.center = [0.1955,0.8159,0.0464]

HAnimJoint1143.children.append(HAnimJoint1155)

HAnimJoint1134.children.append(HAnimJoint1143)

HAnimJoint1125.children.append(HAnimJoint1134)

HAnimJoint1104.children.append(HAnimJoint1125)
HAnimJoint1156 = x3d.HAnimJoint()
HAnimJoint1156.DEF = "hanim_l_midcarpal_2"
HAnimJoint1156.name = "l_midcarpal_2"
HAnimJoint1156.center = [0,1,0]
HAnimSegment1157 = x3d.HAnimSegment()
HAnimSegment1157.DEF = "hanim_l_trapezoid"
HAnimSegment1157.name = "l_trapezoid"
Transform1158 = x3d.Transform()
Transform1158.translation = [0,1,0]
Transform1159 = x3d.Transform()
""" Empty Transform """
Shape1160 = x3d.Shape()
Shape1160.USE = "HAnimJointShape"

Transform1159.children.append(Shape1160)

Transform1158.children.append(Transform1159)

HAnimSegment1157.children.append(Transform1158)
Shape1161 = x3d.Shape()
LineSet1162 = x3d.LineSet()
LineSet1162.vertexCount = [1]
Coordinate1163 = x3d.Coordinate()

LineSet1162.coord = Coordinate1163
""" from l_midcarpal_2 to l_carpometacarpal_2 """
ColorRGBA1164 = x3d.ColorRGBA()
ColorRGBA1164.USE = "HAnimSegmentLineColorRGBA"

LineSet1162.color = ColorRGBA1164

Shape1161.geometry = LineSet1162

HAnimSegment1157.children.append(Shape1161)
HAnimSite1165 = x3d.HAnimSite()
HAnimSite1165.DEF = "hanim_l_metacarpal_phalanx_2_pt"
HAnimSite1165.name = "l_metacarpal_phalanx_2_pt"
HAnimSite1165.translation = [0.2009,0.8139,-0.0237]
TouchSensor1166 = x3d.TouchSensor()
TouchSensor1166.description = "HAnimSite l_metacarpal_phalanx_2_pt"

HAnimSite1165.children.append(TouchSensor1166)
Shape1167 = x3d.Shape()
Shape1167.USE = "HAnimSiteShape"

HAnimSite1165.children.append(Shape1167)

HAnimSegment1157.children.append(HAnimSite1165)

HAnimJoint1156.children.append(HAnimSegment1157)
HAnimJoint1168 = x3d.HAnimJoint()
HAnimJoint1168.DEF = "hanim_l_carpometacarpal_2"
HAnimJoint1168.name = "l_carpometacarpal_2"
HAnimJoint1168.center = [0.1983,0.8024,-0.0280]
HAnimSegment1169 = x3d.HAnimSegment()
HAnimSegment1169.DEF = "hanim_l_metacarpal_2"
HAnimSegment1169.name = "l_metacarpal_2"
Transform1170 = x3d.Transform()
Transform1170.translation = [0.1983,0.8024,-0.0280]
Transform1171 = x3d.Transform()
""" Empty Transform """
Shape1172 = x3d.Shape()
Shape1172.USE = "HAnimJointShape"

Transform1171.children.append(Shape1172)

Transform1170.children.append(Transform1171)

HAnimSegment1169.children.append(Transform1170)
Shape1173 = x3d.Shape()
LineSet1174 = x3d.LineSet()
LineSet1174.vertexCount = [2]
Coordinate1175 = x3d.Coordinate()

LineSet1174.coord = Coordinate1175
""" from l_carpometacarpal_2 to l_metacarpophalangeal_2 """
ColorRGBA1176 = x3d.ColorRGBA()
ColorRGBA1176.USE = "HAnimSegmentLineColorRGBA"

LineSet1174.color = ColorRGBA1176

Shape1173.geometry = LineSet1174

HAnimSegment1169.children.append(Shape1173)

HAnimJoint1168.children.append(HAnimSegment1169)
HAnimJoint1177 = x3d.HAnimJoint()
HAnimJoint1177.DEF = "hanim_l_metacarpophalangeal_2"
HAnimJoint1177.name = "l_metacarpophalangeal_2"
HAnimJoint1177.center = [0.1983,0.7815,-0.0280]
HAnimSegment1178 = x3d.HAnimSegment()
HAnimSegment1178.DEF = "hanim_l_carpal_proximal_phalanx_2"
HAnimSegment1178.name = "l_carpal_proximal_phalanx_2"
Transform1179 = x3d.Transform()
Transform1179.translation = [0.1983,0.7815,-0.0280]
Transform1180 = x3d.Transform()
""" Empty Transform """
Shape1181 = x3d.Shape()
Shape1181.USE = "HAnimJointShape"

Transform1180.children.append(Shape1181)

Transform1179.children.append(Transform1180)

HAnimSegment1178.children.append(Transform1179)
Shape1182 = x3d.Shape()
LineSet1183 = x3d.LineSet()
LineSet1183.vertexCount = [2]
Coordinate1184 = x3d.Coordinate()

LineSet1183.coord = Coordinate1184
""" from l_metacarpophalangeal_2 to l_carpal_proximal_interphalangeal_2 """
ColorRGBA1185 = x3d.ColorRGBA()
ColorRGBA1185.USE = "HAnimSegmentLineColorRGBA"

LineSet1183.color = ColorRGBA1185

Shape1182.geometry = LineSet1183

HAnimSegment1178.children.append(Shape1182)

HAnimJoint1177.children.append(HAnimSegment1178)
HAnimJoint1186 = x3d.HAnimJoint()
HAnimJoint1186.DEF = "hanim_l_carpal_proximal_interphalangeal_2"
HAnimJoint1186.name = "l_carpal_proximal_interphalangeal_2"
HAnimJoint1186.center = [0.2017,0.7363,-0.0248]
HAnimSegment1187 = x3d.HAnimSegment()
HAnimSegment1187.DEF = "hanim_l_carpal_middle_phalanx_2"
HAnimSegment1187.name = "l_carpal_middle_phalanx_2"
Transform1188 = x3d.Transform()
Transform1188.translation = [0.2017,0.7363,-0.0248]
Transform1189 = x3d.Transform()
""" Empty Transform """
Shape1190 = x3d.Shape()
Shape1190.USE = "HAnimJointShape"

Transform1189.children.append(Shape1190)

Transform1188.children.append(Transform1189)

HAnimSegment1187.children.append(Transform1188)
Shape1191 = x3d.Shape()
LineSet1192 = x3d.LineSet()
LineSet1192.vertexCount = [2]
Coordinate1193 = x3d.Coordinate()

LineSet1192.coord = Coordinate1193
""" from l_carpal_proximal_interphalangeal_2 to l_carpal_distal_interphalangeal_2 """
ColorRGBA1194 = x3d.ColorRGBA()
ColorRGBA1194.USE = "HAnimSegmentLineColorRGBA"

LineSet1192.color = ColorRGBA1194

Shape1191.geometry = LineSet1192

HAnimSegment1187.children.append(Shape1191)
HAnimSite1195 = x3d.HAnimSite()
HAnimSite1195.DEF = "hanim_l_carpal_distal_phalanx_2_tip"
HAnimSite1195.name = "l_carpal_distal_phalanx_2_tip"
HAnimSite1195.translation = [0,1,0]
TouchSensor1196 = x3d.TouchSensor()
TouchSensor1196.description = "HAnimSite l_carpal_distal_phalanx_2_tip"

HAnimSite1195.children.append(TouchSensor1196)
Shape1197 = x3d.Shape()
Shape1197.USE = "HAnimSiteShape"

HAnimSite1195.children.append(Shape1197)

HAnimSegment1187.children.append(HAnimSite1195)
HAnimSite1198 = x3d.HAnimSite()
HAnimSite1198.DEF = "hanim_l_dactylion_pt"
HAnimSite1198.name = "l_dactylion_pt"
HAnimSite1198.translation = [0.2056,0.6743,-0.0482]
TouchSensor1199 = x3d.TouchSensor()
TouchSensor1199.description = "HAnimSite l_dactylion_pt"

HAnimSite1198.children.append(TouchSensor1199)
Shape1200 = x3d.Shape()
Shape1200.USE = "HAnimSiteShape"

HAnimSite1198.children.append(Shape1200)

HAnimSegment1187.children.append(HAnimSite1198)

HAnimJoint1186.children.append(HAnimSegment1187)
HAnimJoint1201 = x3d.HAnimJoint()
HAnimJoint1201.DEF = "hanim_l_carpal_distal_interphalangeal_2"
HAnimJoint1201.name = "l_carpal_distal_interphalangeal_2"
HAnimJoint1201.center = [0.2028,0.7139,-0.0236]

HAnimJoint1186.children.append(HAnimJoint1201)

HAnimJoint1177.children.append(HAnimJoint1186)

HAnimJoint1168.children.append(HAnimJoint1177)

HAnimJoint1156.children.append(HAnimJoint1168)

HAnimJoint1104.children.append(HAnimJoint1156)
HAnimJoint1202 = x3d.HAnimJoint()
HAnimJoint1202.DEF = "hanim_l_midcarpal_3"
HAnimJoint1202.name = "l_midcarpal_3"
HAnimJoint1202.center = [0,1,0]
HAnimSegment1203 = x3d.HAnimSegment()
HAnimSegment1203.DEF = "hanim_l_capitate"
HAnimSegment1203.name = "l_capitate"
Transform1204 = x3d.Transform()
Transform1204.translation = [0,1,0]
Transform1205 = x3d.Transform()
""" Empty Transform """
Shape1206 = x3d.Shape()
Shape1206.USE = "HAnimJointShape"

Transform1205.children.append(Shape1206)

Transform1204.children.append(Transform1205)

HAnimSegment1203.children.append(Transform1204)
Shape1207 = x3d.Shape()
LineSet1208 = x3d.LineSet()
LineSet1208.vertexCount = [1]
Coordinate1209 = x3d.Coordinate()

LineSet1208.coord = Coordinate1209
""" from l_midcarpal_3 to l_carpometacarpal_3 """
ColorRGBA1210 = x3d.ColorRGBA()
ColorRGBA1210.USE = "HAnimSegmentLineColorRGBA"

LineSet1208.color = ColorRGBA1210

Shape1207.geometry = LineSet1208

HAnimSegment1203.children.append(Shape1207)
HAnimSite1211 = x3d.HAnimSite()
HAnimSite1211.DEF = "hanim_l_metacarpal_phalanx_3_pt"
HAnimSite1211.name = "l_metacarpal_phalanx_3_pt"
HAnimSite1211.translation = [0,1,0]
TouchSensor1212 = x3d.TouchSensor()
TouchSensor1212.description = "HAnimSite l_metacarpal_phalanx_3_pt"

HAnimSite1211.children.append(TouchSensor1212)
Shape1213 = x3d.Shape()
Shape1213.USE = "HAnimSiteShape"

HAnimSite1211.children.append(Shape1213)

HAnimSegment1203.children.append(HAnimSite1211)

HAnimJoint1202.children.append(HAnimSegment1203)
HAnimJoint1214 = x3d.HAnimJoint()
HAnimJoint1214.DEF = "hanim_l_carpometacarpal_3"
HAnimJoint1214.name = "l_carpometacarpal_3"
HAnimJoint1214.center = [0.1987,0.8029,-0.0530]
HAnimSegment1215 = x3d.HAnimSegment()
HAnimSegment1215.DEF = "hanim_l_metacarpal_3"
HAnimSegment1215.name = "l_metacarpal_3"
Transform1216 = x3d.Transform()
Transform1216.translation = [0.1987,0.8029,-0.0530]
Transform1217 = x3d.Transform()
""" Empty Transform """
Shape1218 = x3d.Shape()
Shape1218.USE = "HAnimJointShape"

Transform1217.children.append(Shape1218)

Transform1216.children.append(Transform1217)

HAnimSegment1215.children.append(Transform1216)
Shape1219 = x3d.Shape()
LineSet1220 = x3d.LineSet()
LineSet1220.vertexCount = [2]
Coordinate1221 = x3d.Coordinate()

LineSet1220.coord = Coordinate1221
""" from l_carpometacarpal_3 to l_metacarpophalangeal_3 """
ColorRGBA1222 = x3d.ColorRGBA()
ColorRGBA1222.USE = "HAnimSegmentLineColorRGBA"

LineSet1220.color = ColorRGBA1222

Shape1219.geometry = LineSet1220

HAnimSegment1215.children.append(Shape1219)

HAnimJoint1214.children.append(HAnimSegment1215)
HAnimJoint1223 = x3d.HAnimJoint()
HAnimJoint1223.DEF = "hanim_l_metacarpophalangeal_3"
HAnimJoint1223.name = "l_metacarpophalangeal_3"
HAnimJoint1223.center = [0.1987,0.7818,-0.0530]
HAnimSegment1224 = x3d.HAnimSegment()
HAnimSegment1224.DEF = "hanim_l_carpal_proximal_phalanx_3"
HAnimSegment1224.name = "l_carpal_proximal_phalanx_3"
Transform1225 = x3d.Transform()
Transform1225.translation = [0.1987,0.7818,-0.0530]
Transform1226 = x3d.Transform()
""" Empty Transform """
Shape1227 = x3d.Shape()
Shape1227.USE = "HAnimJointShape"

Transform1226.children.append(Shape1227)

Transform1225.children.append(Transform1226)

HAnimSegment1224.children.append(Transform1225)
Shape1228 = x3d.Shape()
LineSet1229 = x3d.LineSet()
LineSet1229.vertexCount = [2]
Coordinate1230 = x3d.Coordinate()

LineSet1229.coord = Coordinate1230
""" from l_metacarpophalangeal_3 to l_carpal_proximal_interphalangeal_3 """
ColorRGBA1231 = x3d.ColorRGBA()
ColorRGBA1231.USE = "HAnimSegmentLineColorRGBA"

LineSet1229.color = ColorRGBA1231

Shape1228.geometry = LineSet1229

HAnimSegment1224.children.append(Shape1228)

HAnimJoint1223.children.append(HAnimSegment1224)
HAnimJoint1232 = x3d.HAnimJoint()
HAnimJoint1232.DEF = "hanim_l_carpal_proximal_interphalangeal_3"
HAnimJoint1232.name = "l_carpal_proximal_interphalangeal_3"
HAnimJoint1232.center = [0.2013,0.7273,-0.0503]
HAnimSegment1233 = x3d.HAnimSegment()
HAnimSegment1233.DEF = "hanim_l_carpal_middle_phalanx_3"
HAnimSegment1233.name = "l_carpal_middle_phalanx_3"
Transform1234 = x3d.Transform()
Transform1234.translation = [0.2013,0.7273,-0.0503]
Transform1235 = x3d.Transform()
""" Empty Transform """
Shape1236 = x3d.Shape()
Shape1236.USE = "HAnimJointShape"

Transform1235.children.append(Shape1236)

Transform1234.children.append(Transform1235)

HAnimSegment1233.children.append(Transform1234)
Shape1237 = x3d.Shape()
LineSet1238 = x3d.LineSet()
LineSet1238.vertexCount = [2]
Coordinate1239 = x3d.Coordinate()

LineSet1238.coord = Coordinate1239
""" from l_carpal_proximal_interphalangeal_3 to l_carpal_distal_interphalangeal_3 """
ColorRGBA1240 = x3d.ColorRGBA()
ColorRGBA1240.USE = "HAnimSegmentLineColorRGBA"

LineSet1238.color = ColorRGBA1240

Shape1237.geometry = LineSet1238

HAnimSegment1233.children.append(Shape1237)
HAnimSite1241 = x3d.HAnimSite()
HAnimSite1241.DEF = "hanim_l_carpal_distal_phalanx_3_tip"
HAnimSite1241.name = "l_carpal_distal_phalanx_3_tip"
HAnimSite1241.translation = [0,1,0]
TouchSensor1242 = x3d.TouchSensor()
TouchSensor1242.description = "HAnimSite l_carpal_distal_phalanx_3_tip"

HAnimSite1241.children.append(TouchSensor1242)
Shape1243 = x3d.Shape()
Shape1243.USE = "HAnimSiteShape"

HAnimSite1241.children.append(Shape1243)

HAnimSegment1233.children.append(HAnimSite1241)

HAnimJoint1232.children.append(HAnimSegment1233)
HAnimJoint1244 = x3d.HAnimJoint()
HAnimJoint1244.DEF = "hanim_l_carpal_distal_interphalangeal_3"
HAnimJoint1244.name = "l_carpal_distal_interphalangeal_3"
HAnimJoint1244.center = [0.2026,0.7011,-0.0494]

HAnimJoint1232.children.append(HAnimJoint1244)

HAnimJoint1223.children.append(HAnimJoint1232)

HAnimJoint1214.children.append(HAnimJoint1223)

HAnimJoint1202.children.append(HAnimJoint1214)

HAnimJoint1104.children.append(HAnimJoint1202)
HAnimJoint1245 = x3d.HAnimJoint()
HAnimJoint1245.DEF = "hanim_l_midcarpal_4_5"
HAnimJoint1245.name = "l_midcarpal_4_5"
HAnimJoint1245.center = [0,1,0]
HAnimSegment1246 = x3d.HAnimSegment()
HAnimSegment1246.DEF = "hanim_l_hamate"
HAnimSegment1246.name = "l_hamate"
Transform1247 = x3d.Transform()
Transform1247.translation = [0,1,0]
Transform1248 = x3d.Transform()
""" Empty Transform """
Shape1249 = x3d.Shape()
Shape1249.USE = "HAnimJointShape"

Transform1248.children.append(Shape1249)

Transform1247.children.append(Transform1248)

HAnimSegment1246.children.append(Transform1247)
Shape1250 = x3d.Shape()
LineSet1251 = x3d.LineSet()
LineSet1251.vertexCount = [1]
Coordinate1252 = x3d.Coordinate()

LineSet1251.coord = Coordinate1252
""" from l_midcarpal_4_5 to l_carpometacarpal_4 """
ColorRGBA1253 = x3d.ColorRGBA()
ColorRGBA1253.USE = "HAnimSegmentLineColorRGBA"

LineSet1251.color = ColorRGBA1253

Shape1250.geometry = LineSet1251

HAnimSegment1246.children.append(Shape1250)
Shape1254 = x3d.Shape()
LineSet1255 = x3d.LineSet()
LineSet1255.vertexCount = [1]
Coordinate1256 = x3d.Coordinate()

LineSet1255.coord = Coordinate1256
""" from l_midcarpal_4_5 to l_carpometacarpal_5 """
ColorRGBA1257 = x3d.ColorRGBA()
ColorRGBA1257.USE = "HAnimSegmentLineColorRGBA"

LineSet1255.color = ColorRGBA1257

Shape1254.geometry = LineSet1255

HAnimSegment1246.children.append(Shape1254)
HAnimSite1258 = x3d.HAnimSite()
HAnimSite1258.DEF = "hanim_l_metacarpal_phalanx_5_pt"
HAnimSite1258.name = "l_metacarpal_phalanx_5_pt"
HAnimSite1258.translation = [0.1929,0.7860,-0.1122]
TouchSensor1259 = x3d.TouchSensor()
TouchSensor1259.description = "HAnimSite l_metacarpal_phalanx_5_pt"

HAnimSite1258.children.append(TouchSensor1259)
Shape1260 = x3d.Shape()
Shape1260.USE = "HAnimSiteShape"

HAnimSite1258.children.append(Shape1260)

HAnimSegment1246.children.append(HAnimSite1258)

HAnimJoint1245.children.append(HAnimSegment1246)
HAnimJoint1261 = x3d.HAnimJoint()
HAnimJoint1261.DEF = "hanim_l_carpometacarpal_4"
HAnimJoint1261.name = "l_carpometacarpal_4"
HAnimJoint1261.center = [0.1956,0.8019,-0.0794]
HAnimSegment1262 = x3d.HAnimSegment()
HAnimSegment1262.DEF = "hanim_l_metacarpal_4"
HAnimSegment1262.name = "l_metacarpal_4"
Transform1263 = x3d.Transform()
Transform1263.translation = [0.1956,0.8019,-0.0794]
Transform1264 = x3d.Transform()
""" Empty Transform """
Shape1265 = x3d.Shape()
Shape1265.USE = "HAnimJointShape"

Transform1264.children.append(Shape1265)

Transform1263.children.append(Transform1264)

HAnimSegment1262.children.append(Transform1263)
Shape1266 = x3d.Shape()
LineSet1267 = x3d.LineSet()
LineSet1267.vertexCount = [2]
Coordinate1268 = x3d.Coordinate()

LineSet1267.coord = Coordinate1268
""" from l_carpometacarpal_4 to l_metacarpophalangeal_4 """
ColorRGBA1269 = x3d.ColorRGBA()
ColorRGBA1269.USE = "HAnimSegmentLineColorRGBA"

LineSet1267.color = ColorRGBA1269

Shape1266.geometry = LineSet1267

HAnimSegment1262.children.append(Shape1266)

HAnimJoint1261.children.append(HAnimSegment1262)
HAnimJoint1270 = x3d.HAnimJoint()
HAnimJoint1270.DEF = "hanim_l_metacarpophalangeal_4"
HAnimJoint1270.name = "l_metacarpophalangeal_4"
HAnimJoint1270.center = [0.1956,0.7815,-0.0794]
HAnimSegment1271 = x3d.HAnimSegment()
HAnimSegment1271.DEF = "hanim_l_carpal_proximal_phalanx_4"
HAnimSegment1271.name = "l_carpal_proximal_phalanx_4"
Transform1272 = x3d.Transform()
Transform1272.translation = [0.1956,0.7815,-0.0794]
Transform1273 = x3d.Transform()
""" Empty Transform """
Shape1274 = x3d.Shape()
Shape1274.USE = "HAnimJointShape"

Transform1273.children.append(Shape1274)

Transform1272.children.append(Transform1273)

HAnimSegment1271.children.append(Transform1272)
Shape1275 = x3d.Shape()
LineSet1276 = x3d.LineSet()
LineSet1276.vertexCount = [2]
Coordinate1277 = x3d.Coordinate()

LineSet1276.coord = Coordinate1277
""" from l_metacarpophalangeal_4 to l_carpal_proximal_interphalangeal_4 """
ColorRGBA1278 = x3d.ColorRGBA()
ColorRGBA1278.USE = "HAnimSegmentLineColorRGBA"

LineSet1276.color = ColorRGBA1278

Shape1275.geometry = LineSet1276

HAnimSegment1271.children.append(Shape1275)

HAnimJoint1270.children.append(HAnimSegment1271)
HAnimJoint1279 = x3d.HAnimJoint()
HAnimJoint1279.DEF = "hanim_l_carpal_proximal_interphalangeal_4"
HAnimJoint1279.name = "l_carpal_proximal_interphalangeal_4"
HAnimJoint1279.center = [0.1973,0.7287,-0.0777]
HAnimSegment1280 = x3d.HAnimSegment()
HAnimSegment1280.DEF = "hanim_l_carpal_middle_phalanx_4"
HAnimSegment1280.name = "l_carpal_middle_phalanx_4"
Transform1281 = x3d.Transform()
Transform1281.translation = [0.1973,0.7287,-0.0777]
Transform1282 = x3d.Transform()
""" Empty Transform """
Shape1283 = x3d.Shape()
Shape1283.USE = "HAnimJointShape"

Transform1282.children.append(Shape1283)

Transform1281.children.append(Transform1282)

HAnimSegment1280.children.append(Transform1281)
Shape1284 = x3d.Shape()
LineSet1285 = x3d.LineSet()
LineSet1285.vertexCount = [2]
Coordinate1286 = x3d.Coordinate()

LineSet1285.coord = Coordinate1286
""" from l_carpal_proximal_interphalangeal_4 to l_carpal_distal_interphalangeal_4 """
ColorRGBA1287 = x3d.ColorRGBA()
ColorRGBA1287.USE = "HAnimSegmentLineColorRGBA"

LineSet1285.color = ColorRGBA1287

Shape1284.geometry = LineSet1285

HAnimSegment1280.children.append(Shape1284)
HAnimSite1288 = x3d.HAnimSite()
HAnimSite1288.DEF = "hanim_l_carpal_distal_phalanx_4_tip"
HAnimSite1288.name = "l_carpal_distal_phalanx_4_tip"
HAnimSite1288.translation = [0,1,0]
TouchSensor1289 = x3d.TouchSensor()
TouchSensor1289.description = "HAnimSite l_carpal_distal_phalanx_4_tip"

HAnimSite1288.children.append(TouchSensor1289)
Shape1290 = x3d.Shape()
Shape1290.USE = "HAnimSiteShape"

HAnimSite1288.children.append(Shape1290)

HAnimSegment1280.children.append(HAnimSite1288)

HAnimJoint1279.children.append(HAnimSegment1280)
HAnimJoint1291 = x3d.HAnimJoint()
HAnimJoint1291.DEF = "hanim_l_carpal_distal_interphalangeal_4"
HAnimJoint1291.name = "l_carpal_distal_interphalangeal_4"
HAnimJoint1291.center = [0.1983,0.7045,-0.0767]

HAnimJoint1279.children.append(HAnimJoint1291)

HAnimJoint1270.children.append(HAnimJoint1279)

HAnimJoint1261.children.append(HAnimJoint1270)

HAnimJoint1245.children.append(HAnimJoint1261)
HAnimJoint1292 = x3d.HAnimJoint()
HAnimJoint1292.DEF = "hanim_l_carpometacarpal_5"
HAnimJoint1292.name = "l_carpometacarpal_5"
HAnimJoint1292.center = [0.1925,0.8066,-0.1036]
HAnimSegment1293 = x3d.HAnimSegment()
HAnimSegment1293.DEF = "hanim_l_metacarpal_5"
HAnimSegment1293.name = "l_metacarpal_5"
Transform1294 = x3d.Transform()
Transform1294.translation = [0.1925,0.8066,-0.1036]
Transform1295 = x3d.Transform()
""" Empty Transform """
Shape1296 = x3d.Shape()
Shape1296.USE = "HAnimJointShape"

Transform1295.children.append(Shape1296)

Transform1294.children.append(Transform1295)

HAnimSegment1293.children.append(Transform1294)
Shape1297 = x3d.Shape()
LineSet1298 = x3d.LineSet()
LineSet1298.vertexCount = [2]
Coordinate1299 = x3d.Coordinate()

LineSet1298.coord = Coordinate1299
""" from l_carpometacarpal_5 to l_metacarpophalangeal_5 """
ColorRGBA1300 = x3d.ColorRGBA()
ColorRGBA1300.USE = "HAnimSegmentLineColorRGBA"

LineSet1298.color = ColorRGBA1300

Shape1297.geometry = LineSet1298

HAnimSegment1293.children.append(Shape1297)

HAnimJoint1292.children.append(HAnimSegment1293)
HAnimJoint1301 = x3d.HAnimJoint()
HAnimJoint1301.DEF = "hanim_l_metacarpophalangeal_5"
HAnimJoint1301.name = "l_metacarpophalangeal_5"
HAnimJoint1301.center = [0.1925,0.7866,-0.1036]
HAnimSegment1302 = x3d.HAnimSegment()
HAnimSegment1302.DEF = "hanim_l_carpal_proximal_phalanx_5"
HAnimSegment1302.name = "l_carpal_proximal_phalanx_5"
Transform1303 = x3d.Transform()
Transform1303.translation = [0.1925,0.7866,-0.1036]
Transform1304 = x3d.Transform()
""" Empty Transform """
Shape1305 = x3d.Shape()
Shape1305.USE = "HAnimJointShape"

Transform1304.children.append(Shape1305)

Transform1303.children.append(Transform1304)

HAnimSegment1302.children.append(Transform1303)
Shape1306 = x3d.Shape()
LineSet1307 = x3d.LineSet()
LineSet1307.vertexCount = [2]
Coordinate1308 = x3d.Coordinate()

LineSet1307.coord = Coordinate1308
""" from l_metacarpophalangeal_5 to l_carpal_proximal_interphalangeal_5 """
ColorRGBA1309 = x3d.ColorRGBA()
ColorRGBA1309.USE = "HAnimSegmentLineColorRGBA"

LineSet1307.color = ColorRGBA1309

Shape1306.geometry = LineSet1307

HAnimSegment1302.children.append(Shape1306)

HAnimJoint1301.children.append(HAnimSegment1302)
HAnimJoint1310 = x3d.HAnimJoint()
HAnimJoint1310.DEF = "hanim_l_carpal_proximal_interphalangeal_5"
HAnimJoint1310.name = "l_carpal_proximal_interphalangeal_5"
HAnimJoint1310.center = [0.1938,0.7452,-0.1024]
HAnimSegment1311 = x3d.HAnimSegment()
HAnimSegment1311.DEF = "hanim_l_carpal_middle_phalanx_5"
HAnimSegment1311.name = "l_carpal_middle_phalanx_5"
Transform1312 = x3d.Transform()
Transform1312.translation = [0.1938,0.7452,-0.1024]
Transform1313 = x3d.Transform()
""" Empty Transform """
Shape1314 = x3d.Shape()
Shape1314.USE = "HAnimJointShape"

Transform1313.children.append(Shape1314)

Transform1312.children.append(Transform1313)

HAnimSegment1311.children.append(Transform1312)
Shape1315 = x3d.Shape()
LineSet1316 = x3d.LineSet()
LineSet1316.vertexCount = [2]
Coordinate1317 = x3d.Coordinate()

LineSet1316.coord = Coordinate1317
""" from l_carpal_proximal_interphalangeal_5 to l_carpal_distal_interphalangeal_5 """
ColorRGBA1318 = x3d.ColorRGBA()
ColorRGBA1318.USE = "HAnimSegmentLineColorRGBA"

LineSet1316.color = ColorRGBA1318

Shape1315.geometry = LineSet1316

HAnimSegment1311.children.append(Shape1315)
HAnimSite1319 = x3d.HAnimSite()
HAnimSite1319.DEF = "hanim_l_carpal_distal_phalanx_5_tip"
HAnimSite1319.name = "l_carpal_distal_phalanx_5_tip"
HAnimSite1319.translation = [0,1,0]
TouchSensor1320 = x3d.TouchSensor()
TouchSensor1320.description = "HAnimSite l_carpal_distal_phalanx_5_tip"

HAnimSite1319.children.append(TouchSensor1320)
Shape1321 = x3d.Shape()
Shape1321.USE = "HAnimSiteShape"

HAnimSite1319.children.append(Shape1321)

HAnimSegment1311.children.append(HAnimSite1319)

HAnimJoint1310.children.append(HAnimSegment1311)
HAnimJoint1322 = x3d.HAnimJoint()
HAnimJoint1322.DEF = "hanim_l_carpal_distal_interphalangeal_5"
HAnimJoint1322.name = "l_carpal_distal_interphalangeal_5"
HAnimJoint1322.center = [0.1948,0.7277,-0.1017]

HAnimJoint1310.children.append(HAnimJoint1322)

HAnimJoint1301.children.append(HAnimJoint1310)

HAnimJoint1292.children.append(HAnimJoint1301)

HAnimJoint1245.children.append(HAnimJoint1292)

HAnimJoint1104.children.append(HAnimJoint1245)

HAnimJoint1092.children.append(HAnimJoint1104)

HAnimJoint1071.children.append(HAnimJoint1092)

HAnimJoint1056.children.append(HAnimJoint1071)

HAnimJoint1047.children.append(HAnimJoint1056)

HAnimJoint843.children.append(HAnimJoint1047)
HAnimJoint1323 = x3d.HAnimJoint()
HAnimJoint1323.DEF = "hanim_r_sternoclavicular"
HAnimJoint1323.name = "r_sternoclavicular"
HAnimJoint1323.center = [-0.0694,1.4600,-0.0330]
HAnimSegment1324 = x3d.HAnimSegment()
HAnimSegment1324.DEF = "hanim_r_clavicle"
HAnimSegment1324.name = "r_clavicle"
Transform1325 = x3d.Transform()
Transform1325.translation = [-0.0694,1.4600,-0.0330]
Transform1326 = x3d.Transform()
""" Empty Transform """
Shape1327 = x3d.Shape()
Shape1327.USE = "HAnimJointShape"

Transform1326.children.append(Shape1327)

Transform1325.children.append(Transform1326)

HAnimSegment1324.children.append(Transform1325)
Shape1328 = x3d.Shape()
LineSet1329 = x3d.LineSet()
LineSet1329.vertexCount = [2]
Coordinate1330 = x3d.Coordinate()

LineSet1329.coord = Coordinate1330
""" from r_sternoclavicular to r_acromioclavicular """
ColorRGBA1331 = x3d.ColorRGBA()
ColorRGBA1331.USE = "HAnimSegmentLineColorRGBA"

LineSet1329.color = ColorRGBA1331

Shape1328.geometry = LineSet1329

HAnimSegment1324.children.append(Shape1328)

HAnimJoint1323.children.append(HAnimSegment1324)
HAnimJoint1332 = x3d.HAnimJoint()
HAnimJoint1332.DEF = "hanim_r_acromioclavicular"
HAnimJoint1332.name = "r_acromioclavicular"
HAnimJoint1332.center = [-0.0836,1.4281,-0.0401]
HAnimSegment1333 = x3d.HAnimSegment()
HAnimSegment1333.DEF = "hanim_r_scapula"
HAnimSegment1333.name = "r_scapula"
Transform1334 = x3d.Transform()
Transform1334.translation = [-0.0836,1.4281,-0.0401]
Transform1335 = x3d.Transform()
""" Empty Transform """
Shape1336 = x3d.Shape()
Shape1336.USE = "HAnimJointShape"

Transform1335.children.append(Shape1336)

Transform1334.children.append(Transform1335)

HAnimSegment1333.children.append(Transform1334)
Shape1337 = x3d.Shape()
LineSet1338 = x3d.LineSet()
LineSet1338.vertexCount = [2]
Coordinate1339 = x3d.Coordinate()

LineSet1338.coord = Coordinate1339
""" from r_acromioclavicular to r_shoulder """
ColorRGBA1340 = x3d.ColorRGBA()
ColorRGBA1340.USE = "HAnimSegmentLineColorRGBA"

LineSet1338.color = ColorRGBA1340

Shape1337.geometry = LineSet1338

HAnimSegment1333.children.append(Shape1337)
HAnimSite1341 = x3d.HAnimSite()
HAnimSite1341.DEF = "hanim_r_bideltoid_pt"
HAnimSite1341.name = "r_bideltoid_pt"
HAnimSite1341.translation = [0,1,0]
TouchSensor1342 = x3d.TouchSensor()
TouchSensor1342.description = "HAnimSite r_bideltoid_pt"

HAnimSite1341.children.append(TouchSensor1342)
Shape1343 = x3d.Shape()
Shape1343.USE = "HAnimSiteShape"

HAnimSite1341.children.append(Shape1343)

HAnimSegment1333.children.append(HAnimSite1341)
HAnimSite1344 = x3d.HAnimSite()
HAnimSite1344.DEF = "hanim_r_humeral_lateral_epicondyles_pt"
HAnimSite1344.name = "r_humeral_lateral_epicondyles_pt"
HAnimSite1344.translation = [-0.2224,1.1517,-0.1033]
TouchSensor1345 = x3d.TouchSensor()
TouchSensor1345.description = "HAnimSite r_humeral_lateral_epicondyles_pt"

HAnimSite1344.children.append(TouchSensor1345)
Shape1346 = x3d.Shape()
Shape1346.USE = "HAnimSiteShape"

HAnimSite1344.children.append(Shape1346)

HAnimSegment1333.children.append(HAnimSite1344)

HAnimJoint1332.children.append(HAnimSegment1333)
HAnimJoint1347 = x3d.HAnimJoint()
HAnimJoint1347.DEF = "hanim_r_shoulder"
HAnimJoint1347.name = "r_shoulder"
HAnimJoint1347.center = [-0.1907,1.4407,-0.0325]
HAnimSegment1348 = x3d.HAnimSegment()
HAnimSegment1348.DEF = "hanim_r_upperarm"
HAnimSegment1348.name = "r_upperarm"
Transform1349 = x3d.Transform()
Transform1349.translation = [-0.1907,1.4407,-0.0325]
Transform1350 = x3d.Transform()
""" Empty Transform """
Shape1351 = x3d.Shape()
Shape1351.USE = "HAnimJointShape"

Transform1350.children.append(Shape1351)

Transform1349.children.append(Transform1350)

HAnimSegment1348.children.append(Transform1349)
Shape1352 = x3d.Shape()
LineSet1353 = x3d.LineSet()
LineSet1353.vertexCount = [2]
Coordinate1354 = x3d.Coordinate()

LineSet1353.coord = Coordinate1354
""" from r_shoulder to r_elbow """
ColorRGBA1355 = x3d.ColorRGBA()
ColorRGBA1355.USE = "HAnimSegmentLineColorRGBA"

LineSet1353.color = ColorRGBA1355

Shape1352.geometry = LineSet1353

HAnimSegment1348.children.append(Shape1352)
HAnimSite1356 = x3d.HAnimSite()
HAnimSite1356.DEF = "hanim_r_humeral_medial_epicondyles_pt"
HAnimSite1356.name = "r_humeral_medial_epicondyles_pt"
HAnimSite1356.translation = [-0.1680,1.1298,-0.1062]
TouchSensor1357 = x3d.TouchSensor()
TouchSensor1357.description = "HAnimSite r_humeral_medial_epicondyles_pt"

HAnimSite1356.children.append(TouchSensor1357)
Shape1358 = x3d.Shape()
Shape1358.USE = "HAnimSiteShape"

HAnimSite1356.children.append(Shape1358)

HAnimSegment1348.children.append(HAnimSite1356)
HAnimSite1359 = x3d.HAnimSite()
HAnimSite1359.DEF = "hanim_r_olecranon_pt"
HAnimSite1359.name = "r_olecranon_pt"
HAnimSite1359.translation = [-0.1907,1.1405,-0.1065]
TouchSensor1360 = x3d.TouchSensor()
TouchSensor1360.description = "HAnimSite r_olecranon_pt"

HAnimSite1359.children.append(TouchSensor1360)
Shape1361 = x3d.Shape()
Shape1361.USE = "HAnimSiteShape"

HAnimSite1359.children.append(Shape1361)

HAnimSegment1348.children.append(HAnimSite1359)
HAnimSite1362 = x3d.HAnimSite()
HAnimSite1362.DEF = "hanim_r_radial_styloid_pt"
HAnimSite1362.name = "r_radial_styloid_pt"
HAnimSite1362.translation = [-0.1884,0.8676,-0.0360]
TouchSensor1363 = x3d.TouchSensor()
TouchSensor1363.description = "HAnimSite r_radial_styloid_pt"

HAnimSite1362.children.append(TouchSensor1363)
Shape1364 = x3d.Shape()
Shape1364.USE = "HAnimSiteShape"

HAnimSite1362.children.append(Shape1364)

HAnimSegment1348.children.append(HAnimSite1362)
HAnimSite1365 = x3d.HAnimSite()
HAnimSite1365.DEF = "hanim_r_radiale_pt"
HAnimSite1365.name = "r_radiale_pt"
HAnimSite1365.translation = [-0.2130,1.1305,-0.1091]
TouchSensor1366 = x3d.TouchSensor()
TouchSensor1366.description = "HAnimSite r_radiale_pt"

HAnimSite1365.children.append(TouchSensor1366)
Shape1367 = x3d.Shape()
Shape1367.USE = "HAnimSiteShape"

HAnimSite1365.children.append(Shape1367)

HAnimSegment1348.children.append(HAnimSite1365)

HAnimJoint1347.children.append(HAnimSegment1348)
HAnimJoint1368 = x3d.HAnimJoint()
HAnimJoint1368.DEF = "hanim_r_elbow"
HAnimJoint1368.name = "r_elbow"
HAnimJoint1368.center = [-0.1949,1.1388,-0.0620]
HAnimSegment1369 = x3d.HAnimSegment()
HAnimSegment1369.DEF = "hanim_r_forearm"
HAnimSegment1369.name = "r_forearm"
Transform1370 = x3d.Transform()
Transform1370.translation = [-0.1949,1.1388,-0.0620]
Transform1371 = x3d.Transform()
""" Empty Transform """
Shape1372 = x3d.Shape()
Shape1372.USE = "HAnimJointShape"

Transform1371.children.append(Shape1372)

Transform1370.children.append(Transform1371)

HAnimSegment1369.children.append(Transform1370)
Shape1373 = x3d.Shape()
LineSet1374 = x3d.LineSet()
LineSet1374.vertexCount = [2]
Coordinate1375 = x3d.Coordinate()

LineSet1374.coord = Coordinate1375
""" from r_elbow to r_radiocarpal """
ColorRGBA1376 = x3d.ColorRGBA()
ColorRGBA1376.USE = "HAnimSegmentLineColorRGBA"

LineSet1374.color = ColorRGBA1376

Shape1373.geometry = LineSet1374

HAnimSegment1369.children.append(Shape1373)
HAnimSite1377 = x3d.HAnimSite()
HAnimSite1377.DEF = "hanim_r_ulnar_styloid_pt"
HAnimSite1377.name = "r_ulnar_styloid_pt"
HAnimSite1377.translation = [-0.2117,0.8562,-0.0584]
TouchSensor1378 = x3d.TouchSensor()
TouchSensor1378.description = "HAnimSite r_ulnar_styloid_pt"

HAnimSite1377.children.append(TouchSensor1378)
Shape1379 = x3d.Shape()
Shape1379.USE = "HAnimSiteShape"

HAnimSite1377.children.append(Shape1379)

HAnimSegment1369.children.append(HAnimSite1377)

HAnimJoint1368.children.append(HAnimSegment1369)
HAnimJoint1380 = x3d.HAnimJoint()
HAnimJoint1380.DEF = "hanim_r_radiocarpal"
HAnimJoint1380.name = "r_radiocarpal"
HAnimJoint1380.center = [-0.1959,0.8694,-0.0521]
HAnimSegment1381 = x3d.HAnimSegment()
HAnimSegment1381.DEF = "hanim_r_carpal"
HAnimSegment1381.name = "r_carpal"
Transform1382 = x3d.Transform()
Transform1382.scale = [0.2,0.2,0.2]
Transform1382.translation = [-0.20,0.85,-0.05]
Transform1382.rotation = [0,0,1,-3.14]
""" Transform right hand """
Transform1383 = x3d.Transform()
Transform1383.rotation = [0,1,0,1.57]
""" Transform right hand """
Shape1384 = x3d.Shape()
Shape1384.USE = "HAnimJointShape"

Transform1383.children.append(Shape1384)

Transform1382.children.append(Transform1383)

HAnimSegment1381.children.append(Transform1382)
Shape1385 = x3d.Shape()
LineSet1386 = x3d.LineSet()
LineSet1386.vertexCount = [2]
Coordinate1387 = x3d.Coordinate()

LineSet1386.coord = Coordinate1387
""" from r_radiocarpal to r_midcarpal_1 """
ColorRGBA1388 = x3d.ColorRGBA()
ColorRGBA1388.USE = "HAnimSegmentLineColorRGBA"

LineSet1386.color = ColorRGBA1388

Shape1385.geometry = LineSet1386

HAnimSegment1381.children.append(Shape1385)
Shape1389 = x3d.Shape()
LineSet1390 = x3d.LineSet()
LineSet1390.vertexCount = [2]
Coordinate1391 = x3d.Coordinate()

LineSet1390.coord = Coordinate1391
""" from r_radiocarpal to r_midcarpal_2 """
ColorRGBA1392 = x3d.ColorRGBA()
ColorRGBA1392.USE = "HAnimSegmentLineColorRGBA"

LineSet1390.color = ColorRGBA1392

Shape1389.geometry = LineSet1390

HAnimSegment1381.children.append(Shape1389)
Shape1393 = x3d.Shape()
LineSet1394 = x3d.LineSet()
LineSet1394.vertexCount = [2]
Coordinate1395 = x3d.Coordinate()

LineSet1394.coord = Coordinate1395
""" from r_radiocarpal to r_midcarpal_3 """
ColorRGBA1396 = x3d.ColorRGBA()
ColorRGBA1396.USE = "HAnimSegmentLineColorRGBA"

LineSet1394.color = ColorRGBA1396

Shape1393.geometry = LineSet1394

HAnimSegment1381.children.append(Shape1393)
Shape1397 = x3d.Shape()
LineSet1398 = x3d.LineSet()
LineSet1398.vertexCount = [2]
Coordinate1399 = x3d.Coordinate()

LineSet1398.coord = Coordinate1399
""" from r_radiocarpal to r_midcarpal_4_5 """
ColorRGBA1400 = x3d.ColorRGBA()
ColorRGBA1400.USE = "HAnimSegmentLineColorRGBA"

LineSet1398.color = ColorRGBA1400

Shape1397.geometry = LineSet1398

HAnimSegment1381.children.append(Shape1397)

HAnimJoint1380.children.append(HAnimSegment1381)
HAnimJoint1401 = x3d.HAnimJoint()
HAnimJoint1401.DEF = "hanim_r_midcarpal_1"
HAnimJoint1401.name = "r_midcarpal_1"
HAnimJoint1401.center = [0,1,0]
HAnimSegment1402 = x3d.HAnimSegment()
HAnimSegment1402.DEF = "hanim_r_trapezium"
HAnimSegment1402.name = "r_trapezium"
Transform1403 = x3d.Transform()
Transform1403.translation = [0,1,0]
Transform1404 = x3d.Transform()
""" Empty Transform """
Shape1405 = x3d.Shape()
Shape1405.USE = "HAnimJointShape"

Transform1404.children.append(Shape1405)

Transform1403.children.append(Transform1404)

HAnimSegment1402.children.append(Transform1403)
Shape1406 = x3d.Shape()
LineSet1407 = x3d.LineSet()
LineSet1407.vertexCount = [1]
Coordinate1408 = x3d.Coordinate()

LineSet1407.coord = Coordinate1408
""" from r_midcarpal_1 to r_carpometacarpal_1 """
ColorRGBA1409 = x3d.ColorRGBA()
ColorRGBA1409.USE = "HAnimSegmentLineColorRGBA"

LineSet1407.color = ColorRGBA1409

Shape1406.geometry = LineSet1407

HAnimSegment1402.children.append(Shape1406)

HAnimJoint1401.children.append(HAnimSegment1402)
HAnimJoint1410 = x3d.HAnimJoint()
HAnimJoint1410.DEF = "hanim_r_carpometacarpal_1"
HAnimJoint1410.name = "r_carpometacarpal_1"
HAnimJoint1410.center = [-0.1899,0.8502,-0.0473]
HAnimSegment1411 = x3d.HAnimSegment()
HAnimSegment1411.DEF = "hanim_r_metacarpal_1"
HAnimSegment1411.name = "r_metacarpal_1"
Transform1412 = x3d.Transform()
Transform1412.translation = [-0.1899,0.8502,-0.0473]
Transform1413 = x3d.Transform()
""" Empty Transform """
Shape1414 = x3d.Shape()
Shape1414.USE = "HAnimJointShape"

Transform1413.children.append(Shape1414)

Transform1412.children.append(Transform1413)

HAnimSegment1411.children.append(Transform1412)
Shape1415 = x3d.Shape()
LineSet1416 = x3d.LineSet()
LineSet1416.vertexCount = [2]
Coordinate1417 = x3d.Coordinate()

LineSet1416.coord = Coordinate1417
""" from r_carpometacarpal_1 to r_metacarpophalangeal_1 """
ColorRGBA1418 = x3d.ColorRGBA()
ColorRGBA1418.USE = "HAnimSegmentLineColorRGBA"

LineSet1416.color = ColorRGBA1418

Shape1415.geometry = LineSet1416

HAnimSegment1411.children.append(Shape1415)

HAnimJoint1410.children.append(HAnimSegment1411)
HAnimJoint1419 = x3d.HAnimJoint()
HAnimJoint1419.DEF = "hanim_r_metacarpophalangeal_1"
HAnimJoint1419.name = "r_metacarpophalangeal_1"
HAnimJoint1419.center = [-0.1874,0.8256,0.0306]
HAnimSegment1420 = x3d.HAnimSegment()
HAnimSegment1420.DEF = "hanim_r_carpal_proximal_phalanx_1"
HAnimSegment1420.name = "r_carpal_proximal_phalanx_1"
Transform1421 = x3d.Transform()
Transform1421.translation = [-0.1874,0.8256,0.0306]
Transform1422 = x3d.Transform()
""" Empty Transform """
Shape1423 = x3d.Shape()
Shape1423.USE = "HAnimJointShape"

Transform1422.children.append(Shape1423)

Transform1421.children.append(Transform1422)

HAnimSegment1420.children.append(Transform1421)
Shape1424 = x3d.Shape()
LineSet1425 = x3d.LineSet()
LineSet1425.vertexCount = [2]
Coordinate1426 = x3d.Coordinate()

LineSet1425.coord = Coordinate1426
""" from r_metacarpophalangeal_1 to r_carpal_interphalangeal_1 """
ColorRGBA1427 = x3d.ColorRGBA()
ColorRGBA1427.USE = "HAnimSegmentLineColorRGBA"

LineSet1425.color = ColorRGBA1427

Shape1424.geometry = LineSet1425

HAnimSegment1420.children.append(Shape1424)
HAnimSite1428 = x3d.HAnimSite()
HAnimSite1428.DEF = "hanim_r_carpal_distal_phalanx_1_tip"
HAnimSite1428.name = "r_carpal_distal_phalanx_1_tip"
HAnimSite1428.translation = [0,1,0]
TouchSensor1429 = x3d.TouchSensor()
TouchSensor1429.description = "HAnimSite r_carpal_distal_phalanx_1_tip"

HAnimSite1428.children.append(TouchSensor1429)
Shape1430 = x3d.Shape()
Shape1430.USE = "HAnimSiteShape"

HAnimSite1428.children.append(Shape1430)

HAnimSegment1420.children.append(HAnimSite1428)

HAnimJoint1419.children.append(HAnimSegment1420)
HAnimJoint1431 = x3d.HAnimJoint()
HAnimJoint1431.DEF = "hanim_r_carpal_interphalangeal_1"
HAnimJoint1431.name = "r_carpal_interphalangeal_1"
HAnimJoint1431.center = [-0.1864,0.8190,0.0506]

HAnimJoint1419.children.append(HAnimJoint1431)

HAnimJoint1410.children.append(HAnimJoint1419)

HAnimJoint1401.children.append(HAnimJoint1410)

HAnimJoint1380.children.append(HAnimJoint1401)
HAnimJoint1432 = x3d.HAnimJoint()
HAnimJoint1432.DEF = "hanim_r_midcarpal_2"
HAnimJoint1432.name = "r_midcarpal_2"
HAnimJoint1432.center = [0,1,0]
HAnimSegment1433 = x3d.HAnimSegment()
HAnimSegment1433.DEF = "hanim_r_trapezoid"
HAnimSegment1433.name = "r_trapezoid"
Transform1434 = x3d.Transform()
Transform1434.translation = [0,1,0]
Transform1435 = x3d.Transform()
""" Empty Transform """
Shape1436 = x3d.Shape()
Shape1436.USE = "HAnimJointShape"

Transform1435.children.append(Shape1436)

Transform1434.children.append(Transform1435)

HAnimSegment1433.children.append(Transform1434)
Shape1437 = x3d.Shape()
LineSet1438 = x3d.LineSet()
LineSet1438.vertexCount = [1]
Coordinate1439 = x3d.Coordinate()

LineSet1438.coord = Coordinate1439
""" from r_midcarpal_2 to r_carpometacarpal_2 """
ColorRGBA1440 = x3d.ColorRGBA()
ColorRGBA1440.USE = "HAnimSegmentLineColorRGBA"

LineSet1438.color = ColorRGBA1440

Shape1437.geometry = LineSet1438

HAnimSegment1433.children.append(Shape1437)
HAnimSite1441 = x3d.HAnimSite()
HAnimSite1441.DEF = "hanim_r_metacarpal_phalanx_2_pt"
HAnimSite1441.name = "r_metacarpal_phalanx_2_pt"
HAnimSite1441.translation = [-0.1977,0.8169,-0.0177]
TouchSensor1442 = x3d.TouchSensor()
TouchSensor1442.description = "HAnimSite r_metacarpal_phalanx_2_pt"

HAnimSite1441.children.append(TouchSensor1442)
Shape1443 = x3d.Shape()
Shape1443.USE = "HAnimSiteShape"

HAnimSite1441.children.append(Shape1443)

HAnimSegment1433.children.append(HAnimSite1441)

HAnimJoint1432.children.append(HAnimSegment1433)
HAnimJoint1444 = x3d.HAnimJoint()
HAnimJoint1444.DEF = "hanim_r_carpometacarpal_2"
HAnimJoint1444.name = "r_carpometacarpal_2"
HAnimJoint1444.center = [-0.1961,0.8055,-0.0218]
HAnimSegment1445 = x3d.HAnimSegment()
HAnimSegment1445.DEF = "hanim_r_metacarpal_2"
HAnimSegment1445.name = "r_metacarpal_2"
Transform1446 = x3d.Transform()
Transform1446.translation = [-0.1961,0.8055,-0.0218]
Transform1447 = x3d.Transform()
""" Empty Transform """
Shape1448 = x3d.Shape()
Shape1448.USE = "HAnimJointShape"

Transform1447.children.append(Shape1448)

Transform1446.children.append(Transform1447)

HAnimSegment1445.children.append(Transform1446)
Shape1449 = x3d.Shape()
LineSet1450 = x3d.LineSet()
LineSet1450.vertexCount = [2]
Coordinate1451 = x3d.Coordinate()

LineSet1450.coord = Coordinate1451
""" from r_carpometacarpal_2 to r_metacarpophalangeal_2 """
ColorRGBA1452 = x3d.ColorRGBA()
ColorRGBA1452.USE = "HAnimSegmentLineColorRGBA"

LineSet1450.color = ColorRGBA1452

Shape1449.geometry = LineSet1450

HAnimSegment1445.children.append(Shape1449)

HAnimJoint1444.children.append(HAnimSegment1445)
HAnimJoint1453 = x3d.HAnimJoint()
HAnimJoint1453.DEF = "hanim_r_metacarpophalangeal_2"
HAnimJoint1453.name = "r_metacarpophalangeal_2"
HAnimJoint1453.center = [-0.1961,0.7846,-0.0218]
HAnimSegment1454 = x3d.HAnimSegment()
HAnimSegment1454.DEF = "hanim_r_carpal_proximal_phalanx_2"
HAnimSegment1454.name = "r_carpal_proximal_phalanx_2"
Transform1455 = x3d.Transform()
Transform1455.translation = [-0.1961,0.7846,-0.0218]
Transform1456 = x3d.Transform()
""" Empty Transform """
Shape1457 = x3d.Shape()
Shape1457.USE = "HAnimJointShape"

Transform1456.children.append(Shape1457)

Transform1455.children.append(Transform1456)

HAnimSegment1454.children.append(Transform1455)
Shape1458 = x3d.Shape()
LineSet1459 = x3d.LineSet()
LineSet1459.vertexCount = [2]
Coordinate1460 = x3d.Coordinate()

LineSet1459.coord = Coordinate1460
""" from r_metacarpophalangeal_2 to r_carpal_proximal_interphalangeal_2 """
ColorRGBA1461 = x3d.ColorRGBA()
ColorRGBA1461.USE = "HAnimSegmentLineColorRGBA"

LineSet1459.color = ColorRGBA1461

Shape1458.geometry = LineSet1459

HAnimSegment1454.children.append(Shape1458)

HAnimJoint1453.children.append(HAnimSegment1454)
HAnimJoint1462 = x3d.HAnimJoint()
HAnimJoint1462.DEF = "hanim_r_carpal_proximal_interphalangeal_2"
HAnimJoint1462.name = "r_carpal_proximal_interphalangeal_2"
HAnimJoint1462.center = [-0.1954,0.7393,-0.0185]
HAnimSegment1463 = x3d.HAnimSegment()
HAnimSegment1463.DEF = "hanim_r_carpal_middle_phalanx_2"
HAnimSegment1463.name = "r_carpal_middle_phalanx_2"
Transform1464 = x3d.Transform()
Transform1464.translation = [-0.1954,0.7393,-0.0185]
Transform1465 = x3d.Transform()
""" Empty Transform """
Shape1466 = x3d.Shape()
Shape1466.USE = "HAnimJointShape"

Transform1465.children.append(Shape1466)

Transform1464.children.append(Transform1465)

HAnimSegment1463.children.append(Transform1464)
Shape1467 = x3d.Shape()
LineSet1468 = x3d.LineSet()
LineSet1468.vertexCount = [2]
Coordinate1469 = x3d.Coordinate()

LineSet1468.coord = Coordinate1469
""" from r_carpal_proximal_interphalangeal_2 to r_carpal_distal_interphalangeal_2 """
ColorRGBA1470 = x3d.ColorRGBA()
ColorRGBA1470.USE = "HAnimSegmentLineColorRGBA"

LineSet1468.color = ColorRGBA1470

Shape1467.geometry = LineSet1468

HAnimSegment1463.children.append(Shape1467)
HAnimSite1471 = x3d.HAnimSite()
HAnimSite1471.DEF = "hanim_r_carpal_distal_phalanx_2_tip"
HAnimSite1471.name = "r_carpal_distal_phalanx_2_tip"
HAnimSite1471.translation = [0,1,0]
TouchSensor1472 = x3d.TouchSensor()
TouchSensor1472.description = "HAnimSite r_carpal_distal_phalanx_2_tip"

HAnimSite1471.children.append(TouchSensor1472)
Shape1473 = x3d.Shape()
Shape1473.USE = "HAnimSiteShape"

HAnimSite1471.children.append(Shape1473)

HAnimSegment1463.children.append(HAnimSite1471)
HAnimSite1474 = x3d.HAnimSite()
HAnimSite1474.DEF = "hanim_r_dactylion_pt"
HAnimSite1474.name = "r_dactylion_pt"
HAnimSite1474.translation = [-0.1941,0.6772,-0.0423]
TouchSensor1475 = x3d.TouchSensor()
TouchSensor1475.description = "HAnimSite r_dactylion_pt"

HAnimSite1474.children.append(TouchSensor1475)
Shape1476 = x3d.Shape()
Shape1476.USE = "HAnimSiteShape"

HAnimSite1474.children.append(Shape1476)

HAnimSegment1463.children.append(HAnimSite1474)

HAnimJoint1462.children.append(HAnimSegment1463)
HAnimJoint1477 = x3d.HAnimJoint()
HAnimJoint1477.DEF = "hanim_r_carpal_distal_interphalangeal_2"
HAnimJoint1477.name = "r_carpal_distal_interphalangeal_2"
HAnimJoint1477.center = [-0.1945,0.7169,-0.0173]

HAnimJoint1462.children.append(HAnimJoint1477)

HAnimJoint1453.children.append(HAnimJoint1462)

HAnimJoint1444.children.append(HAnimJoint1453)

HAnimJoint1432.children.append(HAnimJoint1444)

HAnimJoint1380.children.append(HAnimJoint1432)
HAnimJoint1478 = x3d.HAnimJoint()
HAnimJoint1478.DEF = "hanim_r_midcarpal_3"
HAnimJoint1478.name = "r_midcarpal_3"
HAnimJoint1478.center = [0,1,0]
HAnimSegment1479 = x3d.HAnimSegment()
HAnimSegment1479.DEF = "hanim_r_capitate"
HAnimSegment1479.name = "r_capitate"
Transform1480 = x3d.Transform()
Transform1480.translation = [0,1,0]
Transform1481 = x3d.Transform()
""" Empty Transform """
Shape1482 = x3d.Shape()
Shape1482.USE = "HAnimJointShape"

Transform1481.children.append(Shape1482)

Transform1480.children.append(Transform1481)

HAnimSegment1479.children.append(Transform1480)
Shape1483 = x3d.Shape()
LineSet1484 = x3d.LineSet()
LineSet1484.vertexCount = [1]
Coordinate1485 = x3d.Coordinate()

LineSet1484.coord = Coordinate1485
""" from r_midcarpal_3 to r_carpometacarpal_3 """
ColorRGBA1486 = x3d.ColorRGBA()
ColorRGBA1486.USE = "HAnimSegmentLineColorRGBA"

LineSet1484.color = ColorRGBA1486

Shape1483.geometry = LineSet1484

HAnimSegment1479.children.append(Shape1483)
HAnimSite1487 = x3d.HAnimSite()
HAnimSite1487.DEF = "hanim_r_metacarpal_phalanx_3_pt"
HAnimSite1487.name = "r_metacarpal_phalanx_3_pt"
HAnimSite1487.translation = [0,1,0]
TouchSensor1488 = x3d.TouchSensor()
TouchSensor1488.description = "HAnimSite r_metacarpal_phalanx_3_pt"

HAnimSite1487.children.append(TouchSensor1488)
Shape1489 = x3d.Shape()
Shape1489.USE = "HAnimSiteShape"

HAnimSite1487.children.append(Shape1489)

HAnimSegment1479.children.append(HAnimSite1487)

HAnimJoint1478.children.append(HAnimSegment1479)
HAnimJoint1490 = x3d.HAnimJoint()
HAnimJoint1490.DEF = "hanim_r_carpometacarpal_3"
HAnimJoint1490.name = "r_carpometacarpal_3"
HAnimJoint1490.center = [-0.1972,0.8060,-0.0468]
HAnimSegment1491 = x3d.HAnimSegment()
HAnimSegment1491.DEF = "hanim_r_metacarpal_3"
HAnimSegment1491.name = "r_metacarpal_3"
Transform1492 = x3d.Transform()
Transform1492.translation = [-0.1972,0.8060,-0.0468]
Transform1493 = x3d.Transform()
""" Empty Transform """
Shape1494 = x3d.Shape()
Shape1494.USE = "HAnimJointShape"

Transform1493.children.append(Shape1494)

Transform1492.children.append(Transform1493)

HAnimSegment1491.children.append(Transform1492)
Shape1495 = x3d.Shape()
LineSet1496 = x3d.LineSet()
LineSet1496.vertexCount = [2]
Coordinate1497 = x3d.Coordinate()

LineSet1496.coord = Coordinate1497
""" from r_carpometacarpal_3 to r_metacarpophalangeal_3 """
ColorRGBA1498 = x3d.ColorRGBA()
ColorRGBA1498.USE = "HAnimSegmentLineColorRGBA"

LineSet1496.color = ColorRGBA1498

Shape1495.geometry = LineSet1496

HAnimSegment1491.children.append(Shape1495)

HAnimJoint1490.children.append(HAnimSegment1491)
HAnimJoint1499 = x3d.HAnimJoint()
HAnimJoint1499.DEF = "hanim_r_metacarpophalangeal_3"
HAnimJoint1499.name = "r_metacarpophalangeal_3"
HAnimJoint1499.center = [-0.1972,0.7849,-0.0468]
HAnimSegment1500 = x3d.HAnimSegment()
HAnimSegment1500.DEF = "hanim_r_carpal_proximal_phalanx_3"
HAnimSegment1500.name = "r_carpal_proximal_phalanx_3"
Transform1501 = x3d.Transform()
Transform1501.translation = [-0.1972,0.7849,-0.0468]
Transform1502 = x3d.Transform()
""" Empty Transform """
Shape1503 = x3d.Shape()
Shape1503.USE = "HAnimJointShape"

Transform1502.children.append(Shape1503)

Transform1501.children.append(Transform1502)

HAnimSegment1500.children.append(Transform1501)
Shape1504 = x3d.Shape()
LineSet1505 = x3d.LineSet()
LineSet1505.vertexCount = [2]
Coordinate1506 = x3d.Coordinate()

LineSet1505.coord = Coordinate1506
""" from r_metacarpophalangeal_3 to r_carpal_proximal_interphalangeal_3 """
ColorRGBA1507 = x3d.ColorRGBA()
ColorRGBA1507.USE = "HAnimSegmentLineColorRGBA"

LineSet1505.color = ColorRGBA1507

Shape1504.geometry = LineSet1505

HAnimSegment1500.children.append(Shape1504)

HAnimJoint1499.children.append(HAnimSegment1500)
HAnimJoint1508 = x3d.HAnimJoint()
HAnimJoint1508.DEF = "hanim_r_carpal_proximal_interphalangeal_3"
HAnimJoint1508.name = "r_carpal_proximal_interphalangeal_3"
HAnimJoint1508.center = [-0.1950,0.7304,-0.0441]
HAnimSegment1509 = x3d.HAnimSegment()
HAnimSegment1509.DEF = "hanim_r_carpal_middle_phalanx_3"
HAnimSegment1509.name = "r_carpal_middle_phalanx_3"
Transform1510 = x3d.Transform()
Transform1510.translation = [-0.1950,0.7304,-0.0441]
Transform1511 = x3d.Transform()
""" Empty Transform """
Shape1512 = x3d.Shape()
Shape1512.USE = "HAnimJointShape"

Transform1511.children.append(Shape1512)

Transform1510.children.append(Transform1511)

HAnimSegment1509.children.append(Transform1510)
Shape1513 = x3d.Shape()
LineSet1514 = x3d.LineSet()
LineSet1514.vertexCount = [2]
Coordinate1515 = x3d.Coordinate()

LineSet1514.coord = Coordinate1515
""" from r_carpal_proximal_interphalangeal_3 to r_carpal_distal_interphalangeal_3 """
ColorRGBA1516 = x3d.ColorRGBA()
ColorRGBA1516.USE = "HAnimSegmentLineColorRGBA"

LineSet1514.color = ColorRGBA1516

Shape1513.geometry = LineSet1514

HAnimSegment1509.children.append(Shape1513)
HAnimSite1517 = x3d.HAnimSite()
HAnimSite1517.DEF = "hanim_r_carpal_distal_phalanx_3_tip"
HAnimSite1517.name = "r_carpal_distal_phalanx_3_tip"
HAnimSite1517.translation = [0,1,0]
TouchSensor1518 = x3d.TouchSensor()
TouchSensor1518.description = "HAnimSite r_carpal_distal_phalanx_3_tip"

HAnimSite1517.children.append(TouchSensor1518)
Shape1519 = x3d.Shape()
Shape1519.USE = "HAnimSiteShape"

HAnimSite1517.children.append(Shape1519)

HAnimSegment1509.children.append(HAnimSite1517)

HAnimJoint1508.children.append(HAnimSegment1509)
HAnimJoint1520 = x3d.HAnimJoint()
HAnimJoint1520.DEF = "hanim_r_carpal_distal_interphalangeal_3"
HAnimJoint1520.name = "r_carpal_distal_interphalangeal_3"
HAnimJoint1520.center = [-0.1939,0.7042,-0.0432]

HAnimJoint1508.children.append(HAnimJoint1520)

HAnimJoint1499.children.append(HAnimJoint1508)

HAnimJoint1490.children.append(HAnimJoint1499)

HAnimJoint1478.children.append(HAnimJoint1490)

HAnimJoint1380.children.append(HAnimJoint1478)
HAnimJoint1521 = x3d.HAnimJoint()
HAnimJoint1521.DEF = "hanim_r_midcarpal_4_5"
HAnimJoint1521.name = "r_midcarpal_4_5"
HAnimJoint1521.center = [0,1,0]
HAnimSegment1522 = x3d.HAnimSegment()
HAnimSegment1522.DEF = "hanim_r_hamate"
HAnimSegment1522.name = "r_hamate"
Transform1523 = x3d.Transform()
Transform1523.translation = [0,1,0]
Transform1524 = x3d.Transform()
""" Empty Transform """
Shape1525 = x3d.Shape()
Shape1525.USE = "HAnimJointShape"

Transform1524.children.append(Shape1525)

Transform1523.children.append(Transform1524)

HAnimSegment1522.children.append(Transform1523)
Shape1526 = x3d.Shape()
LineSet1527 = x3d.LineSet()
LineSet1527.vertexCount = [1]
Coordinate1528 = x3d.Coordinate()

LineSet1527.coord = Coordinate1528
""" from r_midcarpal_4_5 to r_carpometacarpal_4 """
ColorRGBA1529 = x3d.ColorRGBA()
ColorRGBA1529.USE = "HAnimSegmentLineColorRGBA"

LineSet1527.color = ColorRGBA1529

Shape1526.geometry = LineSet1527

HAnimSegment1522.children.append(Shape1526)
Shape1530 = x3d.Shape()
LineSet1531 = x3d.LineSet()
LineSet1531.vertexCount = [1]
Coordinate1532 = x3d.Coordinate()

LineSet1531.coord = Coordinate1532
""" from r_midcarpal_4_5 to r_carpometacarpal_5 """
ColorRGBA1533 = x3d.ColorRGBA()
ColorRGBA1533.USE = "HAnimSegmentLineColorRGBA"

LineSet1531.color = ColorRGBA1533

Shape1530.geometry = LineSet1531

HAnimSegment1522.children.append(Shape1530)
HAnimSite1534 = x3d.HAnimSite()
HAnimSite1534.DEF = "hanim_r_metacarpal_phalanx_5_pt"
HAnimSite1534.name = "r_metacarpal_phalanx_5_pt"
HAnimSite1534.translation = [-0.1929,0.7890,-0.1064]
TouchSensor1535 = x3d.TouchSensor()
TouchSensor1535.description = "HAnimSite r_metacarpal_phalanx_5_pt"

HAnimSite1534.children.append(TouchSensor1535)
Shape1536 = x3d.Shape()
Shape1536.USE = "HAnimSiteShape"

HAnimSite1534.children.append(Shape1536)

HAnimSegment1522.children.append(HAnimSite1534)

HAnimJoint1521.children.append(HAnimSegment1522)
HAnimJoint1537 = x3d.HAnimJoint()
HAnimJoint1537.DEF = "hanim_r_carpometacarpal_4"
HAnimJoint1537.name = "r_carpometacarpal_4"
HAnimJoint1537.center = [-0.1951,0.8049,-0.0732]
HAnimSegment1538 = x3d.HAnimSegment()
HAnimSegment1538.DEF = "hanim_r_metacarpal_4"
HAnimSegment1538.name = "r_metacarpal_4"
Transform1539 = x3d.Transform()
Transform1539.translation = [-0.1951,0.8049,-0.0732]
Transform1540 = x3d.Transform()
""" Empty Transform """
Shape1541 = x3d.Shape()
Shape1541.USE = "HAnimJointShape"

Transform1540.children.append(Shape1541)

Transform1539.children.append(Transform1540)

HAnimSegment1538.children.append(Transform1539)
Shape1542 = x3d.Shape()
LineSet1543 = x3d.LineSet()
LineSet1543.vertexCount = [2]
Coordinate1544 = x3d.Coordinate()

LineSet1543.coord = Coordinate1544
""" from r_carpometacarpal_4 to r_metacarpophalangeal_4 """
ColorRGBA1545 = x3d.ColorRGBA()
ColorRGBA1545.USE = "HAnimSegmentLineColorRGBA"

LineSet1543.color = ColorRGBA1545

Shape1542.geometry = LineSet1543

HAnimSegment1538.children.append(Shape1542)

HAnimJoint1537.children.append(HAnimSegment1538)
HAnimJoint1546 = x3d.HAnimJoint()
HAnimJoint1546.DEF = "hanim_r_metacarpophalangeal_4"
HAnimJoint1546.name = "r_metacarpophalangeal_4"
HAnimJoint1546.center = [-0.1951,0.7845,-0.0732]
HAnimSegment1547 = x3d.HAnimSegment()
HAnimSegment1547.DEF = "hanim_r_carpal_proximal_phalanx_4"
HAnimSegment1547.name = "r_carpal_proximal_phalanx_4"
Transform1548 = x3d.Transform()
Transform1548.translation = [-0.1951,0.7845,-0.0732]
Transform1549 = x3d.Transform()
""" Empty Transform """
Shape1550 = x3d.Shape()
Shape1550.USE = "HAnimJointShape"

Transform1549.children.append(Shape1550)

Transform1548.children.append(Transform1549)

HAnimSegment1547.children.append(Transform1548)
Shape1551 = x3d.Shape()
LineSet1552 = x3d.LineSet()
LineSet1552.vertexCount = [2]
Coordinate1553 = x3d.Coordinate()

LineSet1552.coord = Coordinate1553
""" from r_metacarpophalangeal_4 to r_carpal_proximal_interphalangeal_4 """
ColorRGBA1554 = x3d.ColorRGBA()
ColorRGBA1554.USE = "HAnimSegmentLineColorRGBA"

LineSet1552.color = ColorRGBA1554

Shape1551.geometry = LineSet1552

HAnimSegment1547.children.append(Shape1551)

HAnimJoint1546.children.append(HAnimSegment1547)
HAnimJoint1555 = x3d.HAnimJoint()
HAnimJoint1555.DEF = "hanim_r_carpal_proximal_interphalangeal_4"
HAnimJoint1555.name = "r_carpal_proximal_interphalangeal_4"
HAnimJoint1555.center = [-0.1920,0.7318,-0.0716]
HAnimSegment1556 = x3d.HAnimSegment()
HAnimSegment1556.DEF = "hanim_r_carpal_middle_phalanx_4"
HAnimSegment1556.name = "r_carpal_middle_phalanx_4"
Transform1557 = x3d.Transform()
Transform1557.translation = [-0.1920,0.7318,-0.0716]
Transform1558 = x3d.Transform()
""" Empty Transform """
Shape1559 = x3d.Shape()
Shape1559.USE = "HAnimJointShape"

Transform1558.children.append(Shape1559)

Transform1557.children.append(Transform1558)

HAnimSegment1556.children.append(Transform1557)
Shape1560 = x3d.Shape()
LineSet1561 = x3d.LineSet()
LineSet1561.vertexCount = [2]
Coordinate1562 = x3d.Coordinate()

LineSet1561.coord = Coordinate1562
""" from r_carpal_proximal_interphalangeal_4 to r_carpal_distal_interphalangeal_4 """
ColorRGBA1563 = x3d.ColorRGBA()
ColorRGBA1563.USE = "HAnimSegmentLineColorRGBA"

LineSet1561.color = ColorRGBA1563

Shape1560.geometry = LineSet1561

HAnimSegment1556.children.append(Shape1560)
HAnimSite1564 = x3d.HAnimSite()
HAnimSite1564.DEF = "hanim_r_carpal_distal_phalanx_4_tip"
HAnimSite1564.name = "r_carpal_distal_phalanx_4_tip"
HAnimSite1564.translation = [0,1,0]
TouchSensor1565 = x3d.TouchSensor()
TouchSensor1565.description = "HAnimSite r_carpal_distal_phalanx_4_tip"

HAnimSite1564.children.append(TouchSensor1565)
Shape1566 = x3d.Shape()
Shape1566.USE = "HAnimSiteShape"

HAnimSite1564.children.append(Shape1566)

HAnimSegment1556.children.append(HAnimSite1564)

HAnimJoint1555.children.append(HAnimSegment1556)
HAnimJoint1567 = x3d.HAnimJoint()
HAnimJoint1567.DEF = "hanim_r_carpal_distal_interphalangeal_4"
HAnimJoint1567.name = "r_carpal_distal_interphalangeal_4"
HAnimJoint1567.center = [-0.1908,0.7077,-0.0706]

HAnimJoint1555.children.append(HAnimJoint1567)

HAnimJoint1546.children.append(HAnimJoint1555)

HAnimJoint1537.children.append(HAnimJoint1546)

HAnimJoint1521.children.append(HAnimJoint1537)
HAnimJoint1568 = x3d.HAnimJoint()
HAnimJoint1568.DEF = "hanim_r_carpometacarpal_5"
HAnimJoint1568.name = "r_carpometacarpal_5"
HAnimJoint1568.center = [-0.1926,0.8096,-0.0975]
HAnimSegment1569 = x3d.HAnimSegment()
HAnimSegment1569.DEF = "hanim_r_metacarpal_5"
HAnimSegment1569.name = "r_metacarpal_5"
Transform1570 = x3d.Transform()
Transform1570.translation = [-0.1926,0.8096,-0.0975]
Transform1571 = x3d.Transform()
""" Empty Transform """
Shape1572 = x3d.Shape()
Shape1572.USE = "HAnimJointShape"

Transform1571.children.append(Shape1572)

Transform1570.children.append(Transform1571)

HAnimSegment1569.children.append(Transform1570)
Shape1573 = x3d.Shape()
LineSet1574 = x3d.LineSet()
LineSet1574.vertexCount = [2]
Coordinate1575 = x3d.Coordinate()

LineSet1574.coord = Coordinate1575
""" from r_carpometacarpal_5 to r_metacarpophalangeal_5 """
ColorRGBA1576 = x3d.ColorRGBA()
ColorRGBA1576.USE = "HAnimSegmentLineColorRGBA"

LineSet1574.color = ColorRGBA1576

Shape1573.geometry = LineSet1574

HAnimSegment1569.children.append(Shape1573)

HAnimJoint1568.children.append(HAnimSegment1569)
HAnimJoint1577 = x3d.HAnimJoint()
HAnimJoint1577.DEF = "hanim_r_metacarpophalangeal_5"
HAnimJoint1577.name = "r_metacarpophalangeal_5"
HAnimJoint1577.center = [-0.1926,0.7896,-0.0975]
HAnimSegment1578 = x3d.HAnimSegment()
HAnimSegment1578.DEF = "hanim_r_carpal_proximal_phalanx_5"
HAnimSegment1578.name = "r_carpal_proximal_phalanx_5"
Transform1579 = x3d.Transform()
Transform1579.translation = [-0.1926,0.7896,-0.0975]
Transform1580 = x3d.Transform()
""" Empty Transform """
Shape1581 = x3d.Shape()
Shape1581.USE = "HAnimJointShape"

Transform1580.children.append(Shape1581)

Transform1579.children.append(Transform1580)

HAnimSegment1578.children.append(Transform1579)
Shape1582 = x3d.Shape()
LineSet1583 = x3d.LineSet()
LineSet1583.vertexCount = [2]
Coordinate1584 = x3d.Coordinate()

LineSet1583.coord = Coordinate1584
""" from r_metacarpophalangeal_5 to r_carpal_proximal_interphalangeal_5 """
ColorRGBA1585 = x3d.ColorRGBA()
ColorRGBA1585.USE = "HAnimSegmentLineColorRGBA"

LineSet1583.color = ColorRGBA1585

Shape1582.geometry = LineSet1583

HAnimSegment1578.children.append(Shape1582)

HAnimJoint1577.children.append(HAnimSegment1578)
HAnimJoint1586 = x3d.HAnimJoint()
HAnimJoint1586.DEF = "hanim_r_carpal_proximal_interphalangeal_5"
HAnimJoint1586.name = "r_carpal_proximal_interphalangeal_5"
HAnimJoint1586.center = [-0.1902,0.7483,-0.0963]
HAnimSegment1587 = x3d.HAnimSegment()
HAnimSegment1587.DEF = "hanim_r_carpal_middle_phalanx_5"
HAnimSegment1587.name = "r_carpal_middle_phalanx_5"
Transform1588 = x3d.Transform()
Transform1588.translation = [-0.1902,0.7483,-0.0963]
Transform1589 = x3d.Transform()
""" Empty Transform """
Shape1590 = x3d.Shape()
Shape1590.USE = "HAnimJointShape"

Transform1589.children.append(Shape1590)

Transform1588.children.append(Transform1589)

HAnimSegment1587.children.append(Transform1588)
Shape1591 = x3d.Shape()
LineSet1592 = x3d.LineSet()
LineSet1592.vertexCount = [2]
Coordinate1593 = x3d.Coordinate()

LineSet1592.coord = Coordinate1593
""" from r_carpal_proximal_interphalangeal_5 to r_carpal_distal_interphalangeal_5 """
ColorRGBA1594 = x3d.ColorRGBA()
ColorRGBA1594.USE = "HAnimSegmentLineColorRGBA"

LineSet1592.color = ColorRGBA1594

Shape1591.geometry = LineSet1592

HAnimSegment1587.children.append(Shape1591)
HAnimSite1595 = x3d.HAnimSite()
HAnimSite1595.DEF = "hanim_r_carpal_distal_phalanx_5_tip"
HAnimSite1595.name = "r_carpal_distal_phalanx_5_tip"
HAnimSite1595.translation = [0,1,0]
TouchSensor1596 = x3d.TouchSensor()
TouchSensor1596.description = "HAnimSite r_carpal_distal_phalanx_5_tip"

HAnimSite1595.children.append(TouchSensor1596)
Shape1597 = x3d.Shape()
Shape1597.USE = "HAnimSiteShape"

HAnimSite1595.children.append(Shape1597)

HAnimSegment1587.children.append(HAnimSite1595)

HAnimJoint1586.children.append(HAnimSegment1587)
HAnimJoint1598 = x3d.HAnimJoint()
HAnimJoint1598.DEF = "hanim_r_carpal_distal_interphalangeal_5"
HAnimJoint1598.name = "r_carpal_distal_interphalangeal_5"
HAnimJoint1598.center = [-0.1908,0.7540,-0.0960]

HAnimJoint1586.children.append(HAnimJoint1598)

HAnimJoint1577.children.append(HAnimJoint1586)

HAnimJoint1568.children.append(HAnimJoint1577)

HAnimJoint1521.children.append(HAnimJoint1568)

HAnimJoint1380.children.append(HAnimJoint1521)

HAnimJoint1368.children.append(HAnimJoint1380)

HAnimJoint1347.children.append(HAnimJoint1368)

HAnimJoint1332.children.append(HAnimJoint1347)

HAnimJoint1323.children.append(HAnimJoint1332)

HAnimJoint843.children.append(HAnimJoint1323)

HAnimJoint828.children.append(HAnimJoint843)

HAnimJoint819.children.append(HAnimJoint828)

HAnimJoint810.children.append(HAnimJoint819)

HAnimJoint801.children.append(HAnimJoint810)

HAnimJoint789.children.append(HAnimJoint801)

HAnimJoint768.children.append(HAnimJoint789)

HAnimJoint759.children.append(HAnimJoint768)

HAnimJoint750.children.append(HAnimJoint759)

HAnimJoint735.children.append(HAnimJoint750)

HAnimJoint723.children.append(HAnimJoint735)

HAnimJoint714.children.append(HAnimJoint723)

HAnimJoint705.children.append(HAnimJoint714)

HAnimJoint696.children.append(HAnimJoint705)

HAnimJoint678.children.append(HAnimJoint696)

HAnimJoint669.children.append(HAnimJoint678)

HAnimJoint660.children.append(HAnimJoint669)

HAnimJoint43.children.append(HAnimJoint660)

HAnimHumanoid42.joints.append(HAnimJoint43)
HAnimJoint1599 = x3d.HAnimJoint()
HAnimJoint1599.USE = "hanim_humanoid_root"

HAnimHumanoid42.joints.append(HAnimJoint1599)
HAnimSegment1600 = x3d.HAnimSegment()
HAnimSegment1600.USE = "hanim_sacrum"

HAnimHumanoid42.segments.append(HAnimSegment1600)
HAnimSite1601 = x3d.HAnimSite()
HAnimSite1601.USE = "hanim_buttocks_standing_wall_contact_point_pt"

HAnimHumanoid42.sites.append(HAnimSite1601)
HAnimSite1602 = x3d.HAnimSite()
HAnimSite1602.USE = "hanim_crotch_pt"

HAnimHumanoid42.sites.append(HAnimSite1602)
HAnimSite1603 = x3d.HAnimSite()
HAnimSite1603.USE = "hanim_l_asis_pt"

HAnimHumanoid42.sites.append(HAnimSite1603)
HAnimSite1604 = x3d.HAnimSite()
HAnimSite1604.USE = "hanim_l_iliocristale_pt"

HAnimHumanoid42.sites.append(HAnimSite1604)
HAnimSite1605 = x3d.HAnimSite()
HAnimSite1605.USE = "hanim_l_psis_pt"

HAnimHumanoid42.sites.append(HAnimSite1605)
HAnimSite1606 = x3d.HAnimSite()
HAnimSite1606.USE = "hanim_l_trochanterion_pt"

HAnimHumanoid42.sites.append(HAnimSite1606)
HAnimSite1607 = x3d.HAnimSite()
HAnimSite1607.USE = "hanim_r_asis_pt"

HAnimHumanoid42.sites.append(HAnimSite1607)
HAnimSite1608 = x3d.HAnimSite()
HAnimSite1608.USE = "hanim_r_iliocristale_pt"

HAnimHumanoid42.sites.append(HAnimSite1608)
HAnimSite1609 = x3d.HAnimSite()
HAnimSite1609.USE = "hanim_r_psis_pt"

HAnimHumanoid42.sites.append(HAnimSite1609)
HAnimSite1610 = x3d.HAnimSite()
HAnimSite1610.USE = "hanim_r_trochanterion_pt"

HAnimHumanoid42.sites.append(HAnimSite1610)
HAnimSite1611 = x3d.HAnimSite()
HAnimSite1611.USE = "hanim_navel_pt"

HAnimHumanoid42.sites.append(HAnimSite1611)
HAnimSite1612 = x3d.HAnimSite()
HAnimSite1612.USE = "hanim_waist_preferred_anterior_pt"

HAnimHumanoid42.sites.append(HAnimSite1612)
HAnimSite1613 = x3d.HAnimSite()
HAnimSite1613.USE = "hanim_waist_preferred_posterior_pt"

HAnimHumanoid42.sites.append(HAnimSite1613)
HAnimJoint1614 = x3d.HAnimJoint()
HAnimJoint1614.USE = "hanim_sacroiliac"

HAnimHumanoid42.joints.append(HAnimJoint1614)
HAnimSegment1615 = x3d.HAnimSegment()
HAnimSegment1615.USE = "hanim_pelvis"

HAnimHumanoid42.segments.append(HAnimSegment1615)
HAnimSite1616 = x3d.HAnimSite()
HAnimSite1616.USE = "hanim_l_femoral_lateral_epicondyles_pt"

HAnimHumanoid42.sites.append(HAnimSite1616)
HAnimSite1617 = x3d.HAnimSite()
HAnimSite1617.USE = "hanim_l_femoral_medial_epicondyles_pt"

HAnimHumanoid42.sites.append(HAnimSite1617)
HAnimSite1618 = x3d.HAnimSite()
HAnimSite1618.USE = "hanim_l_knee_crease_pt"

HAnimHumanoid42.sites.append(HAnimSite1618)
HAnimSite1619 = x3d.HAnimSite()
HAnimSite1619.USE = "hanim_l_suprapatella_pt"

HAnimHumanoid42.sites.append(HAnimSite1619)
HAnimSite1620 = x3d.HAnimSite()
HAnimSite1620.USE = "hanim_r_femoral_lateral_epicondyles_pt"

HAnimHumanoid42.sites.append(HAnimSite1620)
HAnimSite1621 = x3d.HAnimSite()
HAnimSite1621.USE = "hanim_r_femoral_medial_epicondyles_pt"

HAnimHumanoid42.sites.append(HAnimSite1621)
HAnimSite1622 = x3d.HAnimSite()
HAnimSite1622.USE = "hanim_r_knee_crease_pt"

HAnimHumanoid42.sites.append(HAnimSite1622)
HAnimSite1623 = x3d.HAnimSite()
HAnimSite1623.USE = "hanim_r_suprapatella_pt"

HAnimHumanoid42.sites.append(HAnimSite1623)
HAnimJoint1624 = x3d.HAnimJoint()
HAnimJoint1624.USE = "hanim_l_hip"

HAnimHumanoid42.joints.append(HAnimJoint1624)
HAnimSegment1625 = x3d.HAnimSegment()
HAnimSegment1625.USE = "hanim_l_thigh"

HAnimHumanoid42.segments.append(HAnimSegment1625)
HAnimSite1626 = x3d.HAnimSite()
HAnimSite1626.USE = "hanim_l_lateral_malleolus_pt"

HAnimHumanoid42.sites.append(HAnimSite1626)
HAnimSite1627 = x3d.HAnimSite()
HAnimSite1627.USE = "hanim_l_medial_malleolus_pt"

HAnimHumanoid42.sites.append(HAnimSite1627)
HAnimSite1628 = x3d.HAnimSite()
HAnimSite1628.USE = "hanim_l_tibiale_pt"

HAnimHumanoid42.sites.append(HAnimSite1628)
HAnimJoint1629 = x3d.HAnimJoint()
HAnimJoint1629.USE = "hanim_l_knee"

HAnimHumanoid42.joints.append(HAnimJoint1629)
HAnimSegment1630 = x3d.HAnimSegment()
HAnimSegment1630.USE = "hanim_l_calf"

HAnimHumanoid42.segments.append(HAnimSegment1630)
HAnimSite1631 = x3d.HAnimSite()
HAnimSite1631.USE = "hanim_l_calcaneus_posterior_pt"

HAnimHumanoid42.sites.append(HAnimSite1631)
HAnimSite1632 = x3d.HAnimSite()
HAnimSite1632.USE = "hanim_l_sphyrion_pt"

HAnimHumanoid42.sites.append(HAnimSite1632)
HAnimJoint1633 = x3d.HAnimJoint()
HAnimJoint1633.USE = "hanim_l_talocrural"

HAnimHumanoid42.joints.append(HAnimJoint1633)
HAnimSegment1634 = x3d.HAnimSegment()
HAnimSegment1634.USE = "hanim_l_talus"

HAnimHumanoid42.segments.append(HAnimSegment1634)
HAnimJoint1635 = x3d.HAnimJoint()
HAnimJoint1635.USE = "hanim_l_talocalcaneonavicular"

HAnimHumanoid42.joints.append(HAnimJoint1635)
HAnimSegment1636 = x3d.HAnimSegment()
HAnimSegment1636.USE = "hanim_l_navicular"

HAnimHumanoid42.segments.append(HAnimSegment1636)
HAnimJoint1637 = x3d.HAnimJoint()
HAnimJoint1637.USE = "hanim_l_cuneonavicular_1"

HAnimHumanoid42.joints.append(HAnimJoint1637)
HAnimSegment1638 = x3d.HAnimSegment()
HAnimSegment1638.USE = "hanim_l_cuneiform_1"

HAnimHumanoid42.segments.append(HAnimSegment1638)
HAnimJoint1639 = x3d.HAnimJoint()
HAnimJoint1639.USE = "hanim_l_tarsometatarsal_1"

HAnimHumanoid42.joints.append(HAnimJoint1639)
HAnimSegment1640 = x3d.HAnimSegment()
HAnimSegment1640.USE = "hanim_l_metatarsal_1"

HAnimHumanoid42.segments.append(HAnimSegment1640)
HAnimSite1641 = x3d.HAnimSite()
HAnimSite1641.USE = "hanim_l_metatarsal_phalanx_1_pt"

HAnimHumanoid42.sites.append(HAnimSite1641)
HAnimJoint1642 = x3d.HAnimJoint()
HAnimJoint1642.USE = "hanim_l_metatarsophalangeal_1"

HAnimHumanoid42.joints.append(HAnimJoint1642)
HAnimSegment1643 = x3d.HAnimSegment()
HAnimSegment1643.USE = "hanim_l_tarsal_proximal_phalanx_1"

HAnimHumanoid42.segments.append(HAnimSegment1643)
HAnimSite1644 = x3d.HAnimSite()
HAnimSite1644.USE = "hanim_l_tarsal_distal_phalanx_1_tip"

HAnimHumanoid42.sites.append(HAnimSite1644)
HAnimJoint1645 = x3d.HAnimJoint()
HAnimJoint1645.USE = "hanim_l_tarsal_interphalangeal_1"

HAnimHumanoid42.joints.append(HAnimJoint1645)
HAnimJoint1646 = x3d.HAnimJoint()
HAnimJoint1646.USE = "hanim_l_cuneonavicular_2"

HAnimHumanoid42.joints.append(HAnimJoint1646)
HAnimSegment1647 = x3d.HAnimSegment()
HAnimSegment1647.USE = "hanim_l_cuneiform_2"

HAnimHumanoid42.segments.append(HAnimSegment1647)
HAnimJoint1648 = x3d.HAnimJoint()
HAnimJoint1648.USE = "hanim_l_tarsometatarsal_2"

HAnimHumanoid42.joints.append(HAnimJoint1648)
HAnimSegment1649 = x3d.HAnimSegment()
HAnimSegment1649.USE = "hanim_l_metatarsal_2"

HAnimHumanoid42.segments.append(HAnimSegment1649)
HAnimJoint1650 = x3d.HAnimJoint()
HAnimJoint1650.USE = "hanim_l_metatarsophalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint1650)
HAnimSegment1651 = x3d.HAnimSegment()
HAnimSegment1651.USE = "hanim_l_tarsal_proximal_phalanx_2"

HAnimHumanoid42.segments.append(HAnimSegment1651)
HAnimJoint1652 = x3d.HAnimJoint()
HAnimJoint1652.USE = "hanim_l_tarsal_proximal_interphalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint1652)
HAnimSegment1653 = x3d.HAnimSegment()
HAnimSegment1653.USE = "hanim_l_tarsal_middle_phalanx_2"

HAnimHumanoid42.segments.append(HAnimSegment1653)
HAnimSite1654 = x3d.HAnimSite()
HAnimSite1654.USE = "hanim_l_tarsal_distal_phalanx_2_tip"

HAnimHumanoid42.sites.append(HAnimSite1654)
HAnimJoint1655 = x3d.HAnimJoint()
HAnimJoint1655.USE = "hanim_l_tarsal_distal_interphalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint1655)
HAnimJoint1656 = x3d.HAnimJoint()
HAnimJoint1656.USE = "hanim_l_cuneonavicular_3"

HAnimHumanoid42.joints.append(HAnimJoint1656)
HAnimSegment1657 = x3d.HAnimSegment()
HAnimSegment1657.USE = "hanim_l_cuneiform_3"

HAnimHumanoid42.segments.append(HAnimSegment1657)
HAnimJoint1658 = x3d.HAnimJoint()
HAnimJoint1658.USE = "hanim_l_tarsometatarsal_3"

HAnimHumanoid42.joints.append(HAnimJoint1658)
HAnimSegment1659 = x3d.HAnimSegment()
HAnimSegment1659.USE = "hanim_l_metatarsal_3"

HAnimHumanoid42.segments.append(HAnimSegment1659)
HAnimJoint1660 = x3d.HAnimJoint()
HAnimJoint1660.USE = "hanim_l_metatarsophalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint1660)
HAnimSegment1661 = x3d.HAnimSegment()
HAnimSegment1661.USE = "hanim_l_tarsal_proximal_phalanx_3"

HAnimHumanoid42.segments.append(HAnimSegment1661)
HAnimJoint1662 = x3d.HAnimJoint()
HAnimJoint1662.USE = "hanim_l_tarsal_proximal_interphalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint1662)
HAnimSegment1663 = x3d.HAnimSegment()
HAnimSegment1663.USE = "hanim_l_tarsal_middle_phalanx_3"

HAnimHumanoid42.segments.append(HAnimSegment1663)
HAnimSite1664 = x3d.HAnimSite()
HAnimSite1664.USE = "hanim_l_tarsal_distal_phalanx_3_tip"

HAnimHumanoid42.sites.append(HAnimSite1664)
HAnimJoint1665 = x3d.HAnimJoint()
HAnimJoint1665.USE = "hanim_l_tarsal_distal_interphalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint1665)
HAnimJoint1666 = x3d.HAnimJoint()
HAnimJoint1666.USE = "hanim_l_calcaneocuboid"

HAnimHumanoid42.joints.append(HAnimJoint1666)
HAnimSegment1667 = x3d.HAnimSegment()
HAnimSegment1667.USE = "hanim_l_calcaneus"

HAnimHumanoid42.segments.append(HAnimSegment1667)
HAnimJoint1668 = x3d.HAnimJoint()
HAnimJoint1668.USE = "hanim_l_transversetarsal"

HAnimHumanoid42.joints.append(HAnimJoint1668)
HAnimSegment1669 = x3d.HAnimSegment()
HAnimSegment1669.USE = "hanim_l_cuboid"

HAnimHumanoid42.segments.append(HAnimSegment1669)
HAnimJoint1670 = x3d.HAnimJoint()
HAnimJoint1670.USE = "hanim_l_tarsometatarsal_4"

HAnimHumanoid42.joints.append(HAnimJoint1670)
HAnimSegment1671 = x3d.HAnimSegment()
HAnimSegment1671.USE = "hanim_l_metatarsal_4"

HAnimHumanoid42.segments.append(HAnimSegment1671)
HAnimJoint1672 = x3d.HAnimJoint()
HAnimJoint1672.USE = "hanim_l_metatarsophalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint1672)
HAnimSegment1673 = x3d.HAnimSegment()
HAnimSegment1673.USE = "hanim_l_tarsal_proximal_phalanx_4"

HAnimHumanoid42.segments.append(HAnimSegment1673)
HAnimJoint1674 = x3d.HAnimJoint()
HAnimJoint1674.USE = "hanim_l_tarsal_proximal_interphalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint1674)
HAnimSegment1675 = x3d.HAnimSegment()
HAnimSegment1675.USE = "hanim_l_tarsal_middle_phalanx_4"

HAnimHumanoid42.segments.append(HAnimSegment1675)
HAnimSite1676 = x3d.HAnimSite()
HAnimSite1676.USE = "hanim_l_tarsal_distal_phalanx_4_tip"

HAnimHumanoid42.sites.append(HAnimSite1676)
HAnimJoint1677 = x3d.HAnimJoint()
HAnimJoint1677.USE = "hanim_l_tarsal_distal_interphalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint1677)
HAnimJoint1678 = x3d.HAnimJoint()
HAnimJoint1678.USE = "hanim_l_tarsometatarsal_5"

HAnimHumanoid42.joints.append(HAnimJoint1678)
HAnimSegment1679 = x3d.HAnimSegment()
HAnimSegment1679.USE = "hanim_l_metatarsal_5"

HAnimHumanoid42.segments.append(HAnimSegment1679)
HAnimSite1680 = x3d.HAnimSite()
HAnimSite1680.USE = "hanim_l_metatarsal_phalanx_5_pt"

HAnimHumanoid42.sites.append(HAnimSite1680)
HAnimJoint1681 = x3d.HAnimJoint()
HAnimJoint1681.USE = "hanim_l_metatarsophalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint1681)
HAnimSegment1682 = x3d.HAnimSegment()
HAnimSegment1682.USE = "hanim_l_tarsal_proximal_phalanx_5"

HAnimHumanoid42.segments.append(HAnimSegment1682)
HAnimJoint1683 = x3d.HAnimJoint()
HAnimJoint1683.USE = "hanim_l_tarsal_proximal_interphalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint1683)
HAnimSegment1684 = x3d.HAnimSegment()
HAnimSegment1684.USE = "hanim_l_tarsal_middle_phalanx_5"

HAnimHumanoid42.segments.append(HAnimSegment1684)
HAnimSite1685 = x3d.HAnimSite()
HAnimSite1685.USE = "hanim_l_tarsal_distal_phalanx_5_tip"

HAnimHumanoid42.sites.append(HAnimSite1685)
HAnimJoint1686 = x3d.HAnimJoint()
HAnimJoint1686.USE = "hanim_l_tarsal_distal_interphalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint1686)
HAnimJoint1687 = x3d.HAnimJoint()
HAnimJoint1687.USE = "hanim_r_hip"

HAnimHumanoid42.joints.append(HAnimJoint1687)
HAnimSegment1688 = x3d.HAnimSegment()
HAnimSegment1688.USE = "hanim_r_thigh"

HAnimHumanoid42.segments.append(HAnimSegment1688)
HAnimSite1689 = x3d.HAnimSite()
HAnimSite1689.USE = "hanim_r_lateral_malleolus_pt"

HAnimHumanoid42.sites.append(HAnimSite1689)
HAnimSite1690 = x3d.HAnimSite()
HAnimSite1690.USE = "hanim_r_medial_malleolus_pt"

HAnimHumanoid42.sites.append(HAnimSite1690)
HAnimSite1691 = x3d.HAnimSite()
HAnimSite1691.USE = "hanim_r_tibiale_pt"

HAnimHumanoid42.sites.append(HAnimSite1691)
HAnimJoint1692 = x3d.HAnimJoint()
HAnimJoint1692.USE = "hanim_r_knee"

HAnimHumanoid42.joints.append(HAnimJoint1692)
HAnimSegment1693 = x3d.HAnimSegment()
HAnimSegment1693.USE = "hanim_r_calf"

HAnimHumanoid42.segments.append(HAnimSegment1693)
HAnimSite1694 = x3d.HAnimSite()
HAnimSite1694.USE = "hanim_r_calcaneus_posterior_pt"

HAnimHumanoid42.sites.append(HAnimSite1694)
HAnimSite1695 = x3d.HAnimSite()
HAnimSite1695.USE = "hanim_r_sphyrion_pt"

HAnimHumanoid42.sites.append(HAnimSite1695)
HAnimJoint1696 = x3d.HAnimJoint()
HAnimJoint1696.USE = "hanim_r_talocrural"

HAnimHumanoid42.joints.append(HAnimJoint1696)
HAnimSegment1697 = x3d.HAnimSegment()
HAnimSegment1697.USE = "hanim_r_talus"

HAnimHumanoid42.segments.append(HAnimSegment1697)
HAnimJoint1698 = x3d.HAnimJoint()
HAnimJoint1698.USE = "hanim_r_talocalcaneonavicular"

HAnimHumanoid42.joints.append(HAnimJoint1698)
HAnimSegment1699 = x3d.HAnimSegment()
HAnimSegment1699.USE = "hanim_r_navicular"

HAnimHumanoid42.segments.append(HAnimSegment1699)
HAnimJoint1700 = x3d.HAnimJoint()
HAnimJoint1700.USE = "hanim_r_cuneonavicular_1"

HAnimHumanoid42.joints.append(HAnimJoint1700)
HAnimSegment1701 = x3d.HAnimSegment()
HAnimSegment1701.USE = "hanim_r_cuneiform_1"

HAnimHumanoid42.segments.append(HAnimSegment1701)
HAnimJoint1702 = x3d.HAnimJoint()
HAnimJoint1702.USE = "hanim_r_tarsometatarsal_1"

HAnimHumanoid42.joints.append(HAnimJoint1702)
HAnimSegment1703 = x3d.HAnimSegment()
HAnimSegment1703.USE = "hanim_r_metatarsal_1"

HAnimHumanoid42.segments.append(HAnimSegment1703)
HAnimSite1704 = x3d.HAnimSite()
HAnimSite1704.USE = "hanim_r_metatarsal_phalanx_1_pt"

HAnimHumanoid42.sites.append(HAnimSite1704)
HAnimJoint1705 = x3d.HAnimJoint()
HAnimJoint1705.USE = "hanim_r_metatarsophalangeal_1"

HAnimHumanoid42.joints.append(HAnimJoint1705)
HAnimSegment1706 = x3d.HAnimSegment()
HAnimSegment1706.USE = "hanim_r_tarsal_proximal_phalanx_1"

HAnimHumanoid42.segments.append(HAnimSegment1706)
HAnimSite1707 = x3d.HAnimSite()
HAnimSite1707.USE = "hanim_r_tarsal_distal_phalanx_1_tip"

HAnimHumanoid42.sites.append(HAnimSite1707)
HAnimJoint1708 = x3d.HAnimJoint()
HAnimJoint1708.USE = "hanim_r_tarsal_interphalangeal_1"

HAnimHumanoid42.joints.append(HAnimJoint1708)
HAnimJoint1709 = x3d.HAnimJoint()
HAnimJoint1709.USE = "hanim_r_cuneonavicular_2"

HAnimHumanoid42.joints.append(HAnimJoint1709)
HAnimSegment1710 = x3d.HAnimSegment()
HAnimSegment1710.USE = "hanim_r_cuneiform_2"

HAnimHumanoid42.segments.append(HAnimSegment1710)
HAnimJoint1711 = x3d.HAnimJoint()
HAnimJoint1711.USE = "hanim_r_tarsometatarsal_2"

HAnimHumanoid42.joints.append(HAnimJoint1711)
HAnimSegment1712 = x3d.HAnimSegment()
HAnimSegment1712.USE = "hanim_r_metatarsal_2"

HAnimHumanoid42.segments.append(HAnimSegment1712)
HAnimJoint1713 = x3d.HAnimJoint()
HAnimJoint1713.USE = "hanim_r_metatarsophalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint1713)
HAnimSegment1714 = x3d.HAnimSegment()
HAnimSegment1714.USE = "hanim_r_tarsal_proximal_phalanx_2"

HAnimHumanoid42.segments.append(HAnimSegment1714)
HAnimJoint1715 = x3d.HAnimJoint()
HAnimJoint1715.USE = "hanim_r_tarsal_proximal_interphalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint1715)
HAnimSegment1716 = x3d.HAnimSegment()
HAnimSegment1716.USE = "hanim_r_tarsal_middle_phalanx_2"

HAnimHumanoid42.segments.append(HAnimSegment1716)
HAnimSite1717 = x3d.HAnimSite()
HAnimSite1717.USE = "hanim_r_tarsal_distal_phalanx_2_tip"

HAnimHumanoid42.sites.append(HAnimSite1717)
HAnimJoint1718 = x3d.HAnimJoint()
HAnimJoint1718.USE = "hanim_r_tarsal_distal_interphalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint1718)
HAnimJoint1719 = x3d.HAnimJoint()
HAnimJoint1719.USE = "hanim_r_cuneonavicular_3"

HAnimHumanoid42.joints.append(HAnimJoint1719)
HAnimSegment1720 = x3d.HAnimSegment()
HAnimSegment1720.USE = "hanim_r_cuneiform_3"

HAnimHumanoid42.segments.append(HAnimSegment1720)
HAnimJoint1721 = x3d.HAnimJoint()
HAnimJoint1721.USE = "hanim_r_tarsometatarsal_3"

HAnimHumanoid42.joints.append(HAnimJoint1721)
HAnimSegment1722 = x3d.HAnimSegment()
HAnimSegment1722.USE = "hanim_r_metatarsal_3"

HAnimHumanoid42.segments.append(HAnimSegment1722)
HAnimJoint1723 = x3d.HAnimJoint()
HAnimJoint1723.USE = "hanim_r_metatarsophalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint1723)
HAnimSegment1724 = x3d.HAnimSegment()
HAnimSegment1724.USE = "hanim_r_tarsal_proximal_phalanx_3"

HAnimHumanoid42.segments.append(HAnimSegment1724)
HAnimJoint1725 = x3d.HAnimJoint()
HAnimJoint1725.USE = "hanim_r_tarsal_proximal_interphalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint1725)
HAnimSegment1726 = x3d.HAnimSegment()
HAnimSegment1726.USE = "hanim_r_tarsal_middle_phalanx_3"

HAnimHumanoid42.segments.append(HAnimSegment1726)
HAnimSite1727 = x3d.HAnimSite()
HAnimSite1727.USE = "hanim_r_tarsal_distal_phalanx_3_tip"

HAnimHumanoid42.sites.append(HAnimSite1727)
HAnimJoint1728 = x3d.HAnimJoint()
HAnimJoint1728.USE = "hanim_r_tarsal_distal_interphalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint1728)
HAnimJoint1729 = x3d.HAnimJoint()
HAnimJoint1729.USE = "hanim_r_calcaneocuboid"

HAnimHumanoid42.joints.append(HAnimJoint1729)
HAnimSegment1730 = x3d.HAnimSegment()
HAnimSegment1730.USE = "hanim_r_calcaneus"

HAnimHumanoid42.segments.append(HAnimSegment1730)
HAnimJoint1731 = x3d.HAnimJoint()
HAnimJoint1731.USE = "hanim_r_transversetarsal"

HAnimHumanoid42.joints.append(HAnimJoint1731)
HAnimSegment1732 = x3d.HAnimSegment()
HAnimSegment1732.USE = "hanim_r_cuboid"

HAnimHumanoid42.segments.append(HAnimSegment1732)
HAnimJoint1733 = x3d.HAnimJoint()
HAnimJoint1733.USE = "hanim_r_tarsometatarsal_4"

HAnimHumanoid42.joints.append(HAnimJoint1733)
HAnimSegment1734 = x3d.HAnimSegment()
HAnimSegment1734.USE = "hanim_r_metatarsal_4"

HAnimHumanoid42.segments.append(HAnimSegment1734)
HAnimJoint1735 = x3d.HAnimJoint()
HAnimJoint1735.USE = "hanim_r_metatarsophalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint1735)
HAnimSegment1736 = x3d.HAnimSegment()
HAnimSegment1736.USE = "hanim_r_tarsal_proximal_phalanx_4"

HAnimHumanoid42.segments.append(HAnimSegment1736)
HAnimJoint1737 = x3d.HAnimJoint()
HAnimJoint1737.USE = "hanim_r_tarsal_proximal_interphalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint1737)
HAnimSegment1738 = x3d.HAnimSegment()
HAnimSegment1738.USE = "hanim_r_tarsal_middle_phalanx_4"

HAnimHumanoid42.segments.append(HAnimSegment1738)
HAnimSite1739 = x3d.HAnimSite()
HAnimSite1739.USE = "hanim_r_tarsal_distal_phalanx_4_tip"

HAnimHumanoid42.sites.append(HAnimSite1739)
HAnimJoint1740 = x3d.HAnimJoint()
HAnimJoint1740.USE = "hanim_r_tarsal_distal_interphalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint1740)
HAnimJoint1741 = x3d.HAnimJoint()
HAnimJoint1741.USE = "hanim_r_tarsometatarsal_5"

HAnimHumanoid42.joints.append(HAnimJoint1741)
HAnimSegment1742 = x3d.HAnimSegment()
HAnimSegment1742.USE = "hanim_r_metatarsal_5"

HAnimHumanoid42.segments.append(HAnimSegment1742)
HAnimSite1743 = x3d.HAnimSite()
HAnimSite1743.USE = "hanim_r_metatarsal_phalanx_5_pt"

HAnimHumanoid42.sites.append(HAnimSite1743)
HAnimJoint1744 = x3d.HAnimJoint()
HAnimJoint1744.USE = "hanim_r_metatarsophalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint1744)
HAnimSegment1745 = x3d.HAnimSegment()
HAnimSegment1745.USE = "hanim_r_tarsal_proximal_phalanx_5"

HAnimHumanoid42.segments.append(HAnimSegment1745)
HAnimJoint1746 = x3d.HAnimJoint()
HAnimJoint1746.USE = "hanim_r_tarsal_proximal_interphalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint1746)
HAnimSegment1747 = x3d.HAnimSegment()
HAnimSegment1747.USE = "hanim_r_tarsal_middle_phalanx_5"

HAnimHumanoid42.segments.append(HAnimSegment1747)
HAnimSite1748 = x3d.HAnimSite()
HAnimSite1748.USE = "hanim_r_tarsal_distal_phalanx_5_tip"

HAnimHumanoid42.sites.append(HAnimSite1748)
HAnimJoint1749 = x3d.HAnimJoint()
HAnimJoint1749.USE = "hanim_r_tarsal_distal_interphalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint1749)
HAnimJoint1750 = x3d.HAnimJoint()
HAnimJoint1750.USE = "hanim_vl5"

HAnimHumanoid42.joints.append(HAnimJoint1750)
HAnimSegment1751 = x3d.HAnimSegment()
HAnimSegment1751.USE = "hanim_l5"

HAnimHumanoid42.segments.append(HAnimSegment1751)
HAnimJoint1752 = x3d.HAnimJoint()
HAnimJoint1752.USE = "hanim_vl4"

HAnimHumanoid42.joints.append(HAnimJoint1752)
HAnimSegment1753 = x3d.HAnimSegment()
HAnimSegment1753.USE = "hanim_l4"

HAnimHumanoid42.segments.append(HAnimSegment1753)
HAnimJoint1754 = x3d.HAnimJoint()
HAnimJoint1754.USE = "hanim_vl3"

HAnimHumanoid42.joints.append(HAnimJoint1754)
HAnimSegment1755 = x3d.HAnimSegment()
HAnimSegment1755.USE = "hanim_l3"

HAnimHumanoid42.segments.append(HAnimSegment1755)
HAnimSite1756 = x3d.HAnimSite()
HAnimSite1756.USE = "hanim_l_rib10_pt"

HAnimHumanoid42.sites.append(HAnimSite1756)
HAnimSite1757 = x3d.HAnimSite()
HAnimSite1757.USE = "hanim_r_rib10_pt"

HAnimHumanoid42.sites.append(HAnimSite1757)
HAnimSite1758 = x3d.HAnimSite()
HAnimSite1758.USE = "hanim_spine_2_middle_back_pt"

HAnimHumanoid42.sites.append(HAnimSite1758)
HAnimJoint1759 = x3d.HAnimJoint()
HAnimJoint1759.USE = "hanim_vl2"

HAnimHumanoid42.joints.append(HAnimJoint1759)
HAnimSegment1760 = x3d.HAnimSegment()
HAnimSegment1760.USE = "hanim_l2"

HAnimHumanoid42.segments.append(HAnimSegment1760)
HAnimJoint1761 = x3d.HAnimJoint()
HAnimJoint1761.USE = "hanim_vl1"

HAnimHumanoid42.joints.append(HAnimJoint1761)
HAnimSegment1762 = x3d.HAnimSegment()
HAnimSegment1762.USE = "hanim_l1"

HAnimHumanoid42.segments.append(HAnimSegment1762)
HAnimJoint1763 = x3d.HAnimJoint()
HAnimJoint1763.USE = "hanim_vt12"

HAnimHumanoid42.joints.append(HAnimJoint1763)
HAnimSegment1764 = x3d.HAnimSegment()
HAnimSegment1764.USE = "hanim_t12"

HAnimHumanoid42.segments.append(HAnimSegment1764)
HAnimJoint1765 = x3d.HAnimJoint()
HAnimJoint1765.USE = "hanim_vt11"

HAnimHumanoid42.joints.append(HAnimJoint1765)
HAnimSegment1766 = x3d.HAnimSegment()
HAnimSegment1766.USE = "hanim_t11"

HAnimHumanoid42.segments.append(HAnimSegment1766)
HAnimSite1767 = x3d.HAnimSite()
HAnimSite1767.USE = "hanim_substernale_pt"

HAnimHumanoid42.sites.append(HAnimSite1767)
HAnimJoint1768 = x3d.HAnimJoint()
HAnimJoint1768.USE = "hanim_vt10"

HAnimHumanoid42.joints.append(HAnimJoint1768)
HAnimSegment1769 = x3d.HAnimSegment()
HAnimSegment1769.USE = "hanim_t10"

HAnimHumanoid42.segments.append(HAnimSegment1769)
HAnimSite1770 = x3d.HAnimSite()
HAnimSite1770.USE = "hanim_l_thelion_pt"

HAnimHumanoid42.sites.append(HAnimSite1770)
HAnimSite1771 = x3d.HAnimSite()
HAnimSite1771.USE = "hanim_r_thelion_pt"

HAnimHumanoid42.sites.append(HAnimSite1771)
HAnimJoint1772 = x3d.HAnimJoint()
HAnimJoint1772.USE = "hanim_vt9"

HAnimHumanoid42.joints.append(HAnimJoint1772)
HAnimSegment1773 = x3d.HAnimSegment()
HAnimSegment1773.USE = "hanim_t9"

HAnimHumanoid42.segments.append(HAnimSegment1773)
HAnimJoint1774 = x3d.HAnimJoint()
HAnimJoint1774.USE = "hanim_vt8"

HAnimHumanoid42.joints.append(HAnimJoint1774)
HAnimSegment1775 = x3d.HAnimSegment()
HAnimSegment1775.USE = "hanim_t8"

HAnimHumanoid42.segments.append(HAnimSegment1775)
HAnimJoint1776 = x3d.HAnimJoint()
HAnimJoint1776.USE = "hanim_vt7"

HAnimHumanoid42.joints.append(HAnimJoint1776)
HAnimSegment1777 = x3d.HAnimSegment()
HAnimSegment1777.USE = "hanim_t7"

HAnimHumanoid42.segments.append(HAnimSegment1777)
HAnimSite1778 = x3d.HAnimSite()
HAnimSite1778.USE = "hanim_l_chest_midsagittal_plane_pt"

HAnimHumanoid42.sites.append(HAnimSite1778)
HAnimSite1779 = x3d.HAnimSite()
HAnimSite1779.USE = "hanim_mesosternale_pt"

HAnimHumanoid42.sites.append(HAnimSite1779)
HAnimSite1780 = x3d.HAnimSite()
HAnimSite1780.USE = "hanim_r_chest_midsagittal_plane_pt"

HAnimHumanoid42.sites.append(HAnimSite1780)
HAnimSite1781 = x3d.HAnimSite()
HAnimSite1781.USE = "hanim_rear_center_midsagittal_plane_pt"

HAnimHumanoid42.sites.append(HAnimSite1781)
HAnimJoint1782 = x3d.HAnimJoint()
HAnimJoint1782.USE = "hanim_vt6"

HAnimHumanoid42.joints.append(HAnimJoint1782)
HAnimSegment1783 = x3d.HAnimSegment()
HAnimSegment1783.USE = "hanim_t6"

HAnimHumanoid42.segments.append(HAnimSegment1783)
HAnimSite1784 = x3d.HAnimSite()
HAnimSite1784.USE = "hanim_spine_1_middle_back_pt"

HAnimHumanoid42.sites.append(HAnimSite1784)
HAnimJoint1785 = x3d.HAnimJoint()
HAnimJoint1785.USE = "hanim_vt5"

HAnimHumanoid42.joints.append(HAnimJoint1785)
HAnimSegment1786 = x3d.HAnimSegment()
HAnimSegment1786.USE = "hanim_t5"

HAnimHumanoid42.segments.append(HAnimSegment1786)
HAnimJoint1787 = x3d.HAnimJoint()
HAnimJoint1787.USE = "hanim_vt4"

HAnimHumanoid42.joints.append(HAnimJoint1787)
HAnimSegment1788 = x3d.HAnimSegment()
HAnimSegment1788.USE = "hanim_t4"

HAnimHumanoid42.segments.append(HAnimSegment1788)
HAnimJoint1789 = x3d.HAnimJoint()
HAnimJoint1789.USE = "hanim_vt3"

HAnimHumanoid42.joints.append(HAnimJoint1789)
HAnimSegment1790 = x3d.HAnimSegment()
HAnimSegment1790.USE = "hanim_t3"

HAnimHumanoid42.segments.append(HAnimSegment1790)
HAnimJoint1791 = x3d.HAnimJoint()
HAnimJoint1791.USE = "hanim_vt2"

HAnimHumanoid42.joints.append(HAnimJoint1791)
HAnimSegment1792 = x3d.HAnimSegment()
HAnimSegment1792.USE = "hanim_t2"

HAnimHumanoid42.segments.append(HAnimSegment1792)
HAnimSite1793 = x3d.HAnimSite()
HAnimSite1793.USE = "hanim_cervicale_pt"

HAnimHumanoid42.sites.append(HAnimSite1793)
HAnimSite1794 = x3d.HAnimSite()
HAnimSite1794.USE = "hanim_suprasternale_pt"

HAnimHumanoid42.sites.append(HAnimSite1794)
HAnimJoint1795 = x3d.HAnimJoint()
HAnimJoint1795.USE = "hanim_vt1"

HAnimHumanoid42.joints.append(HAnimJoint1795)
HAnimSegment1796 = x3d.HAnimSegment()
HAnimSegment1796.USE = "hanim_t1"

HAnimHumanoid42.segments.append(HAnimSegment1796)
HAnimSite1797 = x3d.HAnimSite()
HAnimSite1797.USE = "hanim_l_neck_base_pt"

HAnimHumanoid42.sites.append(HAnimSite1797)
HAnimSite1798 = x3d.HAnimSite()
HAnimSite1798.USE = "hanim_r_neck_base_pt"

HAnimHumanoid42.sites.append(HAnimSite1798)
HAnimSite1799 = x3d.HAnimSite()
HAnimSite1799.USE = "hanim_l_acromion_pt"

HAnimHumanoid42.sites.append(HAnimSite1799)
HAnimSite1800 = x3d.HAnimSite()
HAnimSite1800.USE = "hanim_l_axilla_distal_pt"

HAnimHumanoid42.sites.append(HAnimSite1800)
HAnimSite1801 = x3d.HAnimSite()
HAnimSite1801.USE = "hanim_l_axilla_posterior_folds_pt"

HAnimHumanoid42.sites.append(HAnimSite1801)
HAnimSite1802 = x3d.HAnimSite()
HAnimSite1802.USE = "hanim_l_axilla_proximal_pt"

HAnimHumanoid42.sites.append(HAnimSite1802)
HAnimSite1803 = x3d.HAnimSite()
HAnimSite1803.USE = "hanim_l_clavicale_pt"

HAnimHumanoid42.sites.append(HAnimSite1803)
HAnimSite1804 = x3d.HAnimSite()
HAnimSite1804.USE = "hanim_r_acromion_pt"

HAnimHumanoid42.sites.append(HAnimSite1804)
HAnimSite1805 = x3d.HAnimSite()
HAnimSite1805.USE = "hanim_r_axilla_distal_pt"

HAnimHumanoid42.sites.append(HAnimSite1805)
HAnimSite1806 = x3d.HAnimSite()
HAnimSite1806.USE = "hanim_r_axilla_posterior_folds_pt"

HAnimHumanoid42.sites.append(HAnimSite1806)
HAnimSite1807 = x3d.HAnimSite()
HAnimSite1807.USE = "hanim_r_axilla_proximal_pt"

HAnimHumanoid42.sites.append(HAnimSite1807)
HAnimSite1808 = x3d.HAnimSite()
HAnimSite1808.USE = "hanim_r_clavicale_pt"

HAnimHumanoid42.sites.append(HAnimSite1808)
HAnimJoint1809 = x3d.HAnimJoint()
HAnimJoint1809.USE = "hanim_vc7"

HAnimHumanoid42.joints.append(HAnimJoint1809)
HAnimSegment1810 = x3d.HAnimSegment()
HAnimSegment1810.USE = "hanim_c7"

HAnimHumanoid42.segments.append(HAnimSegment1810)
HAnimJoint1811 = x3d.HAnimJoint()
HAnimJoint1811.USE = "hanim_vc6"

HAnimHumanoid42.joints.append(HAnimJoint1811)
HAnimSegment1812 = x3d.HAnimSegment()
HAnimSegment1812.USE = "hanim_c6"

HAnimHumanoid42.segments.append(HAnimSegment1812)
HAnimJoint1813 = x3d.HAnimJoint()
HAnimJoint1813.USE = "hanim_vc5"

HAnimHumanoid42.joints.append(HAnimJoint1813)
HAnimSegment1814 = x3d.HAnimSegment()
HAnimSegment1814.USE = "hanim_c5"

HAnimHumanoid42.segments.append(HAnimSegment1814)
HAnimJoint1815 = x3d.HAnimJoint()
HAnimJoint1815.USE = "hanim_vc4"

HAnimHumanoid42.joints.append(HAnimJoint1815)
HAnimSegment1816 = x3d.HAnimSegment()
HAnimSegment1816.USE = "hanim_c4"

HAnimHumanoid42.segments.append(HAnimSegment1816)
HAnimJoint1817 = x3d.HAnimJoint()
HAnimJoint1817.USE = "hanim_vc3"

HAnimHumanoid42.joints.append(HAnimJoint1817)
HAnimSegment1818 = x3d.HAnimSegment()
HAnimSegment1818.USE = "hanim_c3"

HAnimHumanoid42.segments.append(HAnimSegment1818)
HAnimSite1819 = x3d.HAnimSite()
HAnimSite1819.USE = "hanim_adams_apple_pt"

HAnimHumanoid42.sites.append(HAnimSite1819)
HAnimJoint1820 = x3d.HAnimJoint()
HAnimJoint1820.USE = "hanim_vc2"

HAnimHumanoid42.joints.append(HAnimJoint1820)
HAnimSegment1821 = x3d.HAnimSegment()
HAnimSegment1821.USE = "hanim_c2"

HAnimHumanoid42.segments.append(HAnimSegment1821)
HAnimJoint1822 = x3d.HAnimJoint()
HAnimJoint1822.USE = "hanim_vc1"

HAnimHumanoid42.joints.append(HAnimJoint1822)
HAnimSegment1823 = x3d.HAnimSegment()
HAnimSegment1823.USE = "hanim_c1"

HAnimHumanoid42.segments.append(HAnimSegment1823)
HAnimSite1824 = x3d.HAnimSite()
HAnimSite1824.USE = "hanim_glabella_pt"

HAnimHumanoid42.sites.append(HAnimSite1824)
HAnimSite1825 = x3d.HAnimSite()
HAnimSite1825.USE = "hanim_l_ectocanthus_pt"

HAnimHumanoid42.sites.append(HAnimSite1825)
HAnimSite1826 = x3d.HAnimSite()
HAnimSite1826.USE = "hanim_l_infraorbitale_pt"

HAnimHumanoid42.sites.append(HAnimSite1826)
HAnimSite1827 = x3d.HAnimSite()
HAnimSite1827.USE = "hanim_l_tragion_pt"

HAnimHumanoid42.sites.append(HAnimSite1827)
HAnimSite1828 = x3d.HAnimSite()
HAnimSite1828.USE = "hanim_nuchale_pt"

HAnimHumanoid42.sites.append(HAnimSite1828)
HAnimSite1829 = x3d.HAnimSite()
HAnimSite1829.USE = "hanim_opisthocranion_pt"

HAnimHumanoid42.sites.append(HAnimSite1829)
HAnimSite1830 = x3d.HAnimSite()
HAnimSite1830.USE = "hanim_r_ectocanthus_pt"

HAnimHumanoid42.sites.append(HAnimSite1830)
HAnimSite1831 = x3d.HAnimSite()
HAnimSite1831.USE = "hanim_r_infraorbitale_pt"

HAnimHumanoid42.sites.append(HAnimSite1831)
HAnimSite1832 = x3d.HAnimSite()
HAnimSite1832.USE = "hanim_r_tragion_pt"

HAnimHumanoid42.sites.append(HAnimSite1832)
HAnimSite1833 = x3d.HAnimSite()
HAnimSite1833.USE = "hanim_sellion_pt"

HAnimHumanoid42.sites.append(HAnimSite1833)
HAnimSite1834 = x3d.HAnimSite()
HAnimSite1834.USE = "hanim_skull_vertex_pt"

HAnimHumanoid42.sites.append(HAnimSite1834)
HAnimJoint1835 = x3d.HAnimJoint()
HAnimJoint1835.USE = "hanim_skullbase"

HAnimHumanoid42.joints.append(HAnimJoint1835)
HAnimSegment1836 = x3d.HAnimSegment()
HAnimSegment1836.USE = "hanim_skull"

HAnimHumanoid42.segments.append(HAnimSegment1836)
HAnimSite1837 = x3d.HAnimSite()
HAnimSite1837.USE = "hanim_l_gonion_pt"

HAnimHumanoid42.sites.append(HAnimSite1837)
HAnimSite1838 = x3d.HAnimSite()
HAnimSite1838.USE = "hanim_menton_pt"

HAnimHumanoid42.sites.append(HAnimSite1838)
HAnimSite1839 = x3d.HAnimSite()
HAnimSite1839.USE = "hanim_r_gonion_pt"

HAnimHumanoid42.sites.append(HAnimSite1839)
HAnimSite1840 = x3d.HAnimSite()
HAnimSite1840.USE = "hanim_supramenton_pt"

HAnimHumanoid42.sites.append(HAnimSite1840)
HAnimJoint1841 = x3d.HAnimJoint()
HAnimJoint1841.USE = "hanim_l_eyelid_joint"

HAnimHumanoid42.joints.append(HAnimJoint1841)
HAnimJoint1842 = x3d.HAnimJoint()
HAnimJoint1842.USE = "hanim_r_eyelid_joint"

HAnimHumanoid42.joints.append(HAnimJoint1842)
HAnimJoint1843 = x3d.HAnimJoint()
HAnimJoint1843.USE = "hanim_l_eyeball_joint"

HAnimHumanoid42.joints.append(HAnimJoint1843)
HAnimJoint1844 = x3d.HAnimJoint()
HAnimJoint1844.USE = "hanim_r_eyeball_joint"

HAnimHumanoid42.joints.append(HAnimJoint1844)
HAnimJoint1845 = x3d.HAnimJoint()
HAnimJoint1845.USE = "hanim_l_eyebrow_joint"

HAnimHumanoid42.joints.append(HAnimJoint1845)
HAnimJoint1846 = x3d.HAnimJoint()
HAnimJoint1846.USE = "hanim_r_eyebrow_joint"

HAnimHumanoid42.joints.append(HAnimJoint1846)
HAnimJoint1847 = x3d.HAnimJoint()
HAnimJoint1847.USE = "hanim_temporomandibular"

HAnimHumanoid42.joints.append(HAnimJoint1847)
HAnimJoint1848 = x3d.HAnimJoint()
HAnimJoint1848.USE = "hanim_l_sternoclavicular"

HAnimHumanoid42.joints.append(HAnimJoint1848)
HAnimSegment1849 = x3d.HAnimSegment()
HAnimSegment1849.USE = "hanim_l_clavicle"

HAnimHumanoid42.segments.append(HAnimSegment1849)
HAnimJoint1850 = x3d.HAnimJoint()
HAnimJoint1850.USE = "hanim_l_acromioclavicular"

HAnimHumanoid42.joints.append(HAnimJoint1850)
HAnimSegment1851 = x3d.HAnimSegment()
HAnimSegment1851.USE = "hanim_l_scapula"

HAnimHumanoid42.segments.append(HAnimSegment1851)
HAnimSite1852 = x3d.HAnimSite()
HAnimSite1852.USE = "hanim_l_bideltoid_pt"

HAnimHumanoid42.sites.append(HAnimSite1852)
HAnimSite1853 = x3d.HAnimSite()
HAnimSite1853.USE = "hanim_l_humeral_lateral_epicondyles_pt"

HAnimHumanoid42.sites.append(HAnimSite1853)
HAnimJoint1854 = x3d.HAnimJoint()
HAnimJoint1854.USE = "hanim_l_shoulder"

HAnimHumanoid42.joints.append(HAnimJoint1854)
HAnimSegment1855 = x3d.HAnimSegment()
HAnimSegment1855.USE = "hanim_l_upperarm"

HAnimHumanoid42.segments.append(HAnimSegment1855)
HAnimSite1856 = x3d.HAnimSite()
HAnimSite1856.USE = "hanim_l_humeral_medial_epicondyles_pt"

HAnimHumanoid42.sites.append(HAnimSite1856)
HAnimSite1857 = x3d.HAnimSite()
HAnimSite1857.USE = "hanim_l_olecranon_pt"

HAnimHumanoid42.sites.append(HAnimSite1857)
HAnimSite1858 = x3d.HAnimSite()
HAnimSite1858.USE = "hanim_l_radial_styloid_pt"

HAnimHumanoid42.sites.append(HAnimSite1858)
HAnimSite1859 = x3d.HAnimSite()
HAnimSite1859.USE = "hanim_l_radiale_pt"

HAnimHumanoid42.sites.append(HAnimSite1859)
HAnimJoint1860 = x3d.HAnimJoint()
HAnimJoint1860.USE = "hanim_l_elbow"

HAnimHumanoid42.joints.append(HAnimJoint1860)
HAnimSegment1861 = x3d.HAnimSegment()
HAnimSegment1861.USE = "hanim_l_forearm"

HAnimHumanoid42.segments.append(HAnimSegment1861)
HAnimSite1862 = x3d.HAnimSite()
HAnimSite1862.USE = "hanim_l_ulnar_styloid_pt"

HAnimHumanoid42.sites.append(HAnimSite1862)
HAnimJoint1863 = x3d.HAnimJoint()
HAnimJoint1863.USE = "hanim_l_radiocarpal"

HAnimHumanoid42.joints.append(HAnimJoint1863)
HAnimSegment1864 = x3d.HAnimSegment()
HAnimSegment1864.USE = "hanim_l_carpal"

HAnimHumanoid42.segments.append(HAnimSegment1864)
HAnimJoint1865 = x3d.HAnimJoint()
HAnimJoint1865.USE = "hanim_l_midcarpal_1"

HAnimHumanoid42.joints.append(HAnimJoint1865)
HAnimSegment1866 = x3d.HAnimSegment()
HAnimSegment1866.USE = "hanim_l_trapezium"

HAnimHumanoid42.segments.append(HAnimSegment1866)
HAnimJoint1867 = x3d.HAnimJoint()
HAnimJoint1867.USE = "hanim_l_carpometacarpal_1"

HAnimHumanoid42.joints.append(HAnimJoint1867)
HAnimSegment1868 = x3d.HAnimSegment()
HAnimSegment1868.USE = "hanim_l_metacarpal_1"

HAnimHumanoid42.segments.append(HAnimSegment1868)
HAnimJoint1869 = x3d.HAnimJoint()
HAnimJoint1869.USE = "hanim_l_metacarpophalangeal_1"

HAnimHumanoid42.joints.append(HAnimJoint1869)
HAnimSegment1870 = x3d.HAnimSegment()
HAnimSegment1870.USE = "hanim_l_carpal_proximal_phalanx_1"

HAnimHumanoid42.segments.append(HAnimSegment1870)
HAnimSite1871 = x3d.HAnimSite()
HAnimSite1871.USE = "hanim_l_carpal_distal_phalanx_1_tip"

HAnimHumanoid42.sites.append(HAnimSite1871)
HAnimJoint1872 = x3d.HAnimJoint()
HAnimJoint1872.USE = "hanim_l_carpal_interphalangeal_1"

HAnimHumanoid42.joints.append(HAnimJoint1872)
HAnimJoint1873 = x3d.HAnimJoint()
HAnimJoint1873.USE = "hanim_l_midcarpal_2"

HAnimHumanoid42.joints.append(HAnimJoint1873)
HAnimSegment1874 = x3d.HAnimSegment()
HAnimSegment1874.USE = "hanim_l_trapezoid"

HAnimHumanoid42.segments.append(HAnimSegment1874)
HAnimSite1875 = x3d.HAnimSite()
HAnimSite1875.USE = "hanim_l_metacarpal_phalanx_2_pt"

HAnimHumanoid42.sites.append(HAnimSite1875)
HAnimJoint1876 = x3d.HAnimJoint()
HAnimJoint1876.USE = "hanim_l_carpometacarpal_2"

HAnimHumanoid42.joints.append(HAnimJoint1876)
HAnimSegment1877 = x3d.HAnimSegment()
HAnimSegment1877.USE = "hanim_l_metacarpal_2"

HAnimHumanoid42.segments.append(HAnimSegment1877)
HAnimJoint1878 = x3d.HAnimJoint()
HAnimJoint1878.USE = "hanim_l_metacarpophalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint1878)
HAnimSegment1879 = x3d.HAnimSegment()
HAnimSegment1879.USE = "hanim_l_carpal_proximal_phalanx_2"

HAnimHumanoid42.segments.append(HAnimSegment1879)
HAnimJoint1880 = x3d.HAnimJoint()
HAnimJoint1880.USE = "hanim_l_carpal_proximal_interphalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint1880)
HAnimSegment1881 = x3d.HAnimSegment()
HAnimSegment1881.USE = "hanim_l_carpal_middle_phalanx_2"

HAnimHumanoid42.segments.append(HAnimSegment1881)
HAnimSite1882 = x3d.HAnimSite()
HAnimSite1882.USE = "hanim_l_carpal_distal_phalanx_2_tip"

HAnimHumanoid42.sites.append(HAnimSite1882)
HAnimSite1883 = x3d.HAnimSite()
HAnimSite1883.USE = "hanim_l_dactylion_pt"

HAnimHumanoid42.sites.append(HAnimSite1883)
HAnimJoint1884 = x3d.HAnimJoint()
HAnimJoint1884.USE = "hanim_l_carpal_distal_interphalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint1884)
HAnimJoint1885 = x3d.HAnimJoint()
HAnimJoint1885.USE = "hanim_l_midcarpal_3"

HAnimHumanoid42.joints.append(HAnimJoint1885)
HAnimSegment1886 = x3d.HAnimSegment()
HAnimSegment1886.USE = "hanim_l_capitate"

HAnimHumanoid42.segments.append(HAnimSegment1886)
HAnimSite1887 = x3d.HAnimSite()
HAnimSite1887.USE = "hanim_l_metacarpal_phalanx_3_pt"

HAnimHumanoid42.sites.append(HAnimSite1887)
HAnimJoint1888 = x3d.HAnimJoint()
HAnimJoint1888.USE = "hanim_l_carpometacarpal_3"

HAnimHumanoid42.joints.append(HAnimJoint1888)
HAnimSegment1889 = x3d.HAnimSegment()
HAnimSegment1889.USE = "hanim_l_metacarpal_3"

HAnimHumanoid42.segments.append(HAnimSegment1889)
HAnimJoint1890 = x3d.HAnimJoint()
HAnimJoint1890.USE = "hanim_l_metacarpophalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint1890)
HAnimSegment1891 = x3d.HAnimSegment()
HAnimSegment1891.USE = "hanim_l_carpal_proximal_phalanx_3"

HAnimHumanoid42.segments.append(HAnimSegment1891)
HAnimJoint1892 = x3d.HAnimJoint()
HAnimJoint1892.USE = "hanim_l_carpal_proximal_interphalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint1892)
HAnimSegment1893 = x3d.HAnimSegment()
HAnimSegment1893.USE = "hanim_l_carpal_middle_phalanx_3"

HAnimHumanoid42.segments.append(HAnimSegment1893)
HAnimSite1894 = x3d.HAnimSite()
HAnimSite1894.USE = "hanim_l_carpal_distal_phalanx_3_tip"

HAnimHumanoid42.sites.append(HAnimSite1894)
HAnimJoint1895 = x3d.HAnimJoint()
HAnimJoint1895.USE = "hanim_l_carpal_distal_interphalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint1895)
HAnimJoint1896 = x3d.HAnimJoint()
HAnimJoint1896.USE = "hanim_l_midcarpal_4_5"

HAnimHumanoid42.joints.append(HAnimJoint1896)
HAnimSegment1897 = x3d.HAnimSegment()
HAnimSegment1897.USE = "hanim_l_hamate"

HAnimHumanoid42.segments.append(HAnimSegment1897)
HAnimSite1898 = x3d.HAnimSite()
HAnimSite1898.USE = "hanim_l_metacarpal_phalanx_5_pt"

HAnimHumanoid42.sites.append(HAnimSite1898)
HAnimJoint1899 = x3d.HAnimJoint()
HAnimJoint1899.USE = "hanim_l_carpometacarpal_4"

HAnimHumanoid42.joints.append(HAnimJoint1899)
HAnimSegment1900 = x3d.HAnimSegment()
HAnimSegment1900.USE = "hanim_l_metacarpal_4"

HAnimHumanoid42.segments.append(HAnimSegment1900)
HAnimJoint1901 = x3d.HAnimJoint()
HAnimJoint1901.USE = "hanim_l_metacarpophalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint1901)
HAnimSegment1902 = x3d.HAnimSegment()
HAnimSegment1902.USE = "hanim_l_carpal_proximal_phalanx_4"

HAnimHumanoid42.segments.append(HAnimSegment1902)
HAnimJoint1903 = x3d.HAnimJoint()
HAnimJoint1903.USE = "hanim_l_carpal_proximal_interphalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint1903)
HAnimSegment1904 = x3d.HAnimSegment()
HAnimSegment1904.USE = "hanim_l_carpal_middle_phalanx_4"

HAnimHumanoid42.segments.append(HAnimSegment1904)
HAnimSite1905 = x3d.HAnimSite()
HAnimSite1905.USE = "hanim_l_carpal_distal_phalanx_4_tip"

HAnimHumanoid42.sites.append(HAnimSite1905)
HAnimJoint1906 = x3d.HAnimJoint()
HAnimJoint1906.USE = "hanim_l_carpal_distal_interphalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint1906)
HAnimJoint1907 = x3d.HAnimJoint()
HAnimJoint1907.USE = "hanim_l_carpometacarpal_5"

HAnimHumanoid42.joints.append(HAnimJoint1907)
HAnimSegment1908 = x3d.HAnimSegment()
HAnimSegment1908.USE = "hanim_l_metacarpal_5"

HAnimHumanoid42.segments.append(HAnimSegment1908)
HAnimJoint1909 = x3d.HAnimJoint()
HAnimJoint1909.USE = "hanim_l_metacarpophalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint1909)
HAnimSegment1910 = x3d.HAnimSegment()
HAnimSegment1910.USE = "hanim_l_carpal_proximal_phalanx_5"

HAnimHumanoid42.segments.append(HAnimSegment1910)
HAnimJoint1911 = x3d.HAnimJoint()
HAnimJoint1911.USE = "hanim_l_carpal_proximal_interphalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint1911)
HAnimSegment1912 = x3d.HAnimSegment()
HAnimSegment1912.USE = "hanim_l_carpal_middle_phalanx_5"

HAnimHumanoid42.segments.append(HAnimSegment1912)
HAnimSite1913 = x3d.HAnimSite()
HAnimSite1913.USE = "hanim_l_carpal_distal_phalanx_5_tip"

HAnimHumanoid42.sites.append(HAnimSite1913)
HAnimJoint1914 = x3d.HAnimJoint()
HAnimJoint1914.USE = "hanim_l_carpal_distal_interphalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint1914)
HAnimJoint1915 = x3d.HAnimJoint()
HAnimJoint1915.USE = "hanim_r_sternoclavicular"

HAnimHumanoid42.joints.append(HAnimJoint1915)
HAnimSegment1916 = x3d.HAnimSegment()
HAnimSegment1916.USE = "hanim_r_clavicle"

HAnimHumanoid42.segments.append(HAnimSegment1916)
HAnimJoint1917 = x3d.HAnimJoint()
HAnimJoint1917.USE = "hanim_r_acromioclavicular"

HAnimHumanoid42.joints.append(HAnimJoint1917)
HAnimSegment1918 = x3d.HAnimSegment()
HAnimSegment1918.USE = "hanim_r_scapula"

HAnimHumanoid42.segments.append(HAnimSegment1918)
HAnimSite1919 = x3d.HAnimSite()
HAnimSite1919.USE = "hanim_r_bideltoid_pt"

HAnimHumanoid42.sites.append(HAnimSite1919)
HAnimSite1920 = x3d.HAnimSite()
HAnimSite1920.USE = "hanim_r_humeral_lateral_epicondyles_pt"

HAnimHumanoid42.sites.append(HAnimSite1920)
HAnimJoint1921 = x3d.HAnimJoint()
HAnimJoint1921.USE = "hanim_r_shoulder"

HAnimHumanoid42.joints.append(HAnimJoint1921)
HAnimSegment1922 = x3d.HAnimSegment()
HAnimSegment1922.USE = "hanim_r_upperarm"

HAnimHumanoid42.segments.append(HAnimSegment1922)
HAnimSite1923 = x3d.HAnimSite()
HAnimSite1923.USE = "hanim_r_humeral_medial_epicondyles_pt"

HAnimHumanoid42.sites.append(HAnimSite1923)
HAnimSite1924 = x3d.HAnimSite()
HAnimSite1924.USE = "hanim_r_olecranon_pt"

HAnimHumanoid42.sites.append(HAnimSite1924)
HAnimSite1925 = x3d.HAnimSite()
HAnimSite1925.USE = "hanim_r_radial_styloid_pt"

HAnimHumanoid42.sites.append(HAnimSite1925)
HAnimSite1926 = x3d.HAnimSite()
HAnimSite1926.USE = "hanim_r_radiale_pt"

HAnimHumanoid42.sites.append(HAnimSite1926)
HAnimJoint1927 = x3d.HAnimJoint()
HAnimJoint1927.USE = "hanim_r_elbow"

HAnimHumanoid42.joints.append(HAnimJoint1927)
HAnimSegment1928 = x3d.HAnimSegment()
HAnimSegment1928.USE = "hanim_r_forearm"

HAnimHumanoid42.segments.append(HAnimSegment1928)
HAnimSite1929 = x3d.HAnimSite()
HAnimSite1929.USE = "hanim_r_ulnar_styloid_pt"

HAnimHumanoid42.sites.append(HAnimSite1929)
HAnimJoint1930 = x3d.HAnimJoint()
HAnimJoint1930.USE = "hanim_r_radiocarpal"

HAnimHumanoid42.joints.append(HAnimJoint1930)
HAnimSegment1931 = x3d.HAnimSegment()
HAnimSegment1931.USE = "hanim_r_carpal"

HAnimHumanoid42.segments.append(HAnimSegment1931)
HAnimJoint1932 = x3d.HAnimJoint()
HAnimJoint1932.USE = "hanim_r_midcarpal_1"

HAnimHumanoid42.joints.append(HAnimJoint1932)
HAnimSegment1933 = x3d.HAnimSegment()
HAnimSegment1933.USE = "hanim_r_trapezium"

HAnimHumanoid42.segments.append(HAnimSegment1933)
HAnimJoint1934 = x3d.HAnimJoint()
HAnimJoint1934.USE = "hanim_r_carpometacarpal_1"

HAnimHumanoid42.joints.append(HAnimJoint1934)
HAnimSegment1935 = x3d.HAnimSegment()
HAnimSegment1935.USE = "hanim_r_metacarpal_1"

HAnimHumanoid42.segments.append(HAnimSegment1935)
HAnimJoint1936 = x3d.HAnimJoint()
HAnimJoint1936.USE = "hanim_r_metacarpophalangeal_1"

HAnimHumanoid42.joints.append(HAnimJoint1936)
HAnimSegment1937 = x3d.HAnimSegment()
HAnimSegment1937.USE = "hanim_r_carpal_proximal_phalanx_1"

HAnimHumanoid42.segments.append(HAnimSegment1937)
HAnimSite1938 = x3d.HAnimSite()
HAnimSite1938.USE = "hanim_r_carpal_distal_phalanx_1_tip"

HAnimHumanoid42.sites.append(HAnimSite1938)
HAnimJoint1939 = x3d.HAnimJoint()
HAnimJoint1939.USE = "hanim_r_carpal_interphalangeal_1"

HAnimHumanoid42.joints.append(HAnimJoint1939)
HAnimJoint1940 = x3d.HAnimJoint()
HAnimJoint1940.USE = "hanim_r_midcarpal_2"

HAnimHumanoid42.joints.append(HAnimJoint1940)
HAnimSegment1941 = x3d.HAnimSegment()
HAnimSegment1941.USE = "hanim_r_trapezoid"

HAnimHumanoid42.segments.append(HAnimSegment1941)
HAnimSite1942 = x3d.HAnimSite()
HAnimSite1942.USE = "hanim_r_metacarpal_phalanx_2_pt"

HAnimHumanoid42.sites.append(HAnimSite1942)
HAnimJoint1943 = x3d.HAnimJoint()
HAnimJoint1943.USE = "hanim_r_carpometacarpal_2"

HAnimHumanoid42.joints.append(HAnimJoint1943)
HAnimSegment1944 = x3d.HAnimSegment()
HAnimSegment1944.USE = "hanim_r_metacarpal_2"

HAnimHumanoid42.segments.append(HAnimSegment1944)
HAnimJoint1945 = x3d.HAnimJoint()
HAnimJoint1945.USE = "hanim_r_metacarpophalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint1945)
HAnimSegment1946 = x3d.HAnimSegment()
HAnimSegment1946.USE = "hanim_r_carpal_proximal_phalanx_2"

HAnimHumanoid42.segments.append(HAnimSegment1946)
HAnimJoint1947 = x3d.HAnimJoint()
HAnimJoint1947.USE = "hanim_r_carpal_proximal_interphalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint1947)
HAnimSegment1948 = x3d.HAnimSegment()
HAnimSegment1948.USE = "hanim_r_carpal_middle_phalanx_2"

HAnimHumanoid42.segments.append(HAnimSegment1948)
HAnimSite1949 = x3d.HAnimSite()
HAnimSite1949.USE = "hanim_r_carpal_distal_phalanx_2_tip"

HAnimHumanoid42.sites.append(HAnimSite1949)
HAnimSite1950 = x3d.HAnimSite()
HAnimSite1950.USE = "hanim_r_dactylion_pt"

HAnimHumanoid42.sites.append(HAnimSite1950)
HAnimJoint1951 = x3d.HAnimJoint()
HAnimJoint1951.USE = "hanim_r_carpal_distal_interphalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint1951)
HAnimJoint1952 = x3d.HAnimJoint()
HAnimJoint1952.USE = "hanim_r_midcarpal_3"

HAnimHumanoid42.joints.append(HAnimJoint1952)
HAnimSegment1953 = x3d.HAnimSegment()
HAnimSegment1953.USE = "hanim_r_capitate"

HAnimHumanoid42.segments.append(HAnimSegment1953)
HAnimSite1954 = x3d.HAnimSite()
HAnimSite1954.USE = "hanim_r_metacarpal_phalanx_3_pt"

HAnimHumanoid42.sites.append(HAnimSite1954)
HAnimJoint1955 = x3d.HAnimJoint()
HAnimJoint1955.USE = "hanim_r_carpometacarpal_3"

HAnimHumanoid42.joints.append(HAnimJoint1955)
HAnimSegment1956 = x3d.HAnimSegment()
HAnimSegment1956.USE = "hanim_r_metacarpal_3"

HAnimHumanoid42.segments.append(HAnimSegment1956)
HAnimJoint1957 = x3d.HAnimJoint()
HAnimJoint1957.USE = "hanim_r_metacarpophalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint1957)
HAnimSegment1958 = x3d.HAnimSegment()
HAnimSegment1958.USE = "hanim_r_carpal_proximal_phalanx_3"

HAnimHumanoid42.segments.append(HAnimSegment1958)
HAnimJoint1959 = x3d.HAnimJoint()
HAnimJoint1959.USE = "hanim_r_carpal_proximal_interphalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint1959)
HAnimSegment1960 = x3d.HAnimSegment()
HAnimSegment1960.USE = "hanim_r_carpal_middle_phalanx_3"

HAnimHumanoid42.segments.append(HAnimSegment1960)
HAnimSite1961 = x3d.HAnimSite()
HAnimSite1961.USE = "hanim_r_carpal_distal_phalanx_3_tip"

HAnimHumanoid42.sites.append(HAnimSite1961)
HAnimJoint1962 = x3d.HAnimJoint()
HAnimJoint1962.USE = "hanim_r_carpal_distal_interphalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint1962)
HAnimJoint1963 = x3d.HAnimJoint()
HAnimJoint1963.USE = "hanim_r_midcarpal_4_5"

HAnimHumanoid42.joints.append(HAnimJoint1963)
HAnimSegment1964 = x3d.HAnimSegment()
HAnimSegment1964.USE = "hanim_r_hamate"

HAnimHumanoid42.segments.append(HAnimSegment1964)
HAnimSite1965 = x3d.HAnimSite()
HAnimSite1965.USE = "hanim_r_metacarpal_phalanx_5_pt"

HAnimHumanoid42.sites.append(HAnimSite1965)
HAnimJoint1966 = x3d.HAnimJoint()
HAnimJoint1966.USE = "hanim_r_carpometacarpal_4"

HAnimHumanoid42.joints.append(HAnimJoint1966)
HAnimSegment1967 = x3d.HAnimSegment()
HAnimSegment1967.USE = "hanim_r_metacarpal_4"

HAnimHumanoid42.segments.append(HAnimSegment1967)
HAnimJoint1968 = x3d.HAnimJoint()
HAnimJoint1968.USE = "hanim_r_metacarpophalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint1968)
HAnimSegment1969 = x3d.HAnimSegment()
HAnimSegment1969.USE = "hanim_r_carpal_proximal_phalanx_4"

HAnimHumanoid42.segments.append(HAnimSegment1969)
HAnimJoint1970 = x3d.HAnimJoint()
HAnimJoint1970.USE = "hanim_r_carpal_proximal_interphalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint1970)
HAnimSegment1971 = x3d.HAnimSegment()
HAnimSegment1971.USE = "hanim_r_carpal_middle_phalanx_4"

HAnimHumanoid42.segments.append(HAnimSegment1971)
HAnimSite1972 = x3d.HAnimSite()
HAnimSite1972.USE = "hanim_r_carpal_distal_phalanx_4_tip"

HAnimHumanoid42.sites.append(HAnimSite1972)
HAnimJoint1973 = x3d.HAnimJoint()
HAnimJoint1973.USE = "hanim_r_carpal_distal_interphalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint1973)
HAnimJoint1974 = x3d.HAnimJoint()
HAnimJoint1974.USE = "hanim_r_carpometacarpal_5"

HAnimHumanoid42.joints.append(HAnimJoint1974)
HAnimSegment1975 = x3d.HAnimSegment()
HAnimSegment1975.USE = "hanim_r_metacarpal_5"

HAnimHumanoid42.segments.append(HAnimSegment1975)
HAnimJoint1976 = x3d.HAnimJoint()
HAnimJoint1976.USE = "hanim_r_metacarpophalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint1976)
HAnimSegment1977 = x3d.HAnimSegment()
HAnimSegment1977.USE = "hanim_r_carpal_proximal_phalanx_5"

HAnimHumanoid42.segments.append(HAnimSegment1977)
HAnimJoint1978 = x3d.HAnimJoint()
HAnimJoint1978.USE = "hanim_r_carpal_proximal_interphalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint1978)
HAnimSegment1979 = x3d.HAnimSegment()
HAnimSegment1979.USE = "hanim_r_carpal_middle_phalanx_5"

HAnimHumanoid42.segments.append(HAnimSegment1979)
HAnimSite1980 = x3d.HAnimSite()
HAnimSite1980.USE = "hanim_r_carpal_distal_phalanx_5_tip"

HAnimHumanoid42.sites.append(HAnimSite1980)
HAnimJoint1981 = x3d.HAnimJoint()
HAnimJoint1981.USE = "hanim_r_carpal_distal_interphalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint1981)

HAnimHumanoid10.skeleton.append(HAnimHumanoid10)

X3D0.Scene = Scene10
f = open("skeleton10_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
