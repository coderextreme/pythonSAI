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
Shape46 = x3d.Shape()
Shape46.USE = "HAnimJointShape"

Transform45.children.append(Shape46)

HAnimSegment44.children.append(Transform45)
Shape47 = x3d.Shape()
LineSet48 = x3d.LineSet()
LineSet48.vertexCount = [2]
Coordinate49 = x3d.Coordinate()

LineSet48.coord = Coordinate49
""" from humanoid_root to sacroiliac """
ColorRGBA50 = x3d.ColorRGBA()
ColorRGBA50.USE = "HAnimSegmentLineColorRGBA"

LineSet48.color = ColorRGBA50

Shape47.geometry = LineSet48

HAnimSegment44.children.append(Shape47)
HAnimSite51 = x3d.HAnimSite()
HAnimSite51.DEF = "hanim_buttocks_standing_wall_contact_point_pt"
HAnimSite51.name = "buttocks_standing_wall_contact_point_pt"
HAnimSite51.translation = [0,1,0]
TouchSensor52 = x3d.TouchSensor()
TouchSensor52.description = "HAnimSite buttocks_standing_wall_contact_point_pt"

HAnimSite51.children.append(TouchSensor52)
Shape53 = x3d.Shape()
Shape53.USE = "HAnimSiteShape"

HAnimSite51.children.append(Shape53)

HAnimSegment44.children.append(HAnimSite51)
HAnimSite54 = x3d.HAnimSite()
HAnimSite54.DEF = "hanim_crotch_pt"
HAnimSite54.name = "crotch_pt"
HAnimSite54.translation = [0.0034,0.8266,0.0257]
TouchSensor55 = x3d.TouchSensor()
TouchSensor55.description = "HAnimSite crotch_pt"

HAnimSite54.children.append(TouchSensor55)
Shape56 = x3d.Shape()
Shape56.USE = "HAnimSiteShape"

HAnimSite54.children.append(Shape56)

HAnimSegment44.children.append(HAnimSite54)
HAnimSite57 = x3d.HAnimSite()
HAnimSite57.DEF = "hanim_l_asis_pt"
HAnimSite57.name = "l_asis_pt"
HAnimSite57.translation = [0.0925,0.9983,0.1052]
TouchSensor58 = x3d.TouchSensor()
TouchSensor58.description = "HAnimSite l_asis_pt"

HAnimSite57.children.append(TouchSensor58)
Shape59 = x3d.Shape()
Shape59.USE = "HAnimSiteShape"

HAnimSite57.children.append(Shape59)

HAnimSegment44.children.append(HAnimSite57)
HAnimSite60 = x3d.HAnimSite()
HAnimSite60.DEF = "hanim_l_iliocristale_pt"
HAnimSite60.name = "l_iliocristale_pt"
HAnimSite60.translation = [0.1612,1.0537,0.0008]
TouchSensor61 = x3d.TouchSensor()
TouchSensor61.description = "HAnimSite l_iliocristale_pt"

HAnimSite60.children.append(TouchSensor61)
Shape62 = x3d.Shape()
Shape62.USE = "HAnimSiteShape"

HAnimSite60.children.append(Shape62)

HAnimSegment44.children.append(HAnimSite60)
HAnimSite63 = x3d.HAnimSite()
HAnimSite63.DEF = "hanim_l_psis_pt"
HAnimSite63.name = "l_psis_pt"
HAnimSite63.translation = [0.0774,1.0190,-0.1151]
TouchSensor64 = x3d.TouchSensor()
TouchSensor64.description = "HAnimSite l_psis_pt"

HAnimSite63.children.append(TouchSensor64)
Shape65 = x3d.Shape()
Shape65.USE = "HAnimSiteShape"

HAnimSite63.children.append(Shape65)

HAnimSegment44.children.append(HAnimSite63)
HAnimSite66 = x3d.HAnimSite()
HAnimSite66.DEF = "hanim_l_trochanterion_pt"
HAnimSite66.name = "l_trochanterion_pt"
HAnimSite66.translation = [0.1677,0.8336,0.0303]
TouchSensor67 = x3d.TouchSensor()
TouchSensor67.description = "HAnimSite l_trochanterion_pt"

HAnimSite66.children.append(TouchSensor67)
Shape68 = x3d.Shape()
Shape68.USE = "HAnimSiteShape"

HAnimSite66.children.append(Shape68)

HAnimSegment44.children.append(HAnimSite66)
HAnimSite69 = x3d.HAnimSite()
HAnimSite69.DEF = "hanim_r_asis_pt"
HAnimSite69.name = "r_asis_pt"
HAnimSite69.translation = [-0.0887,1.0021,0.1112]
TouchSensor70 = x3d.TouchSensor()
TouchSensor70.description = "HAnimSite r_asis_pt"

HAnimSite69.children.append(TouchSensor70)
Shape71 = x3d.Shape()
Shape71.USE = "HAnimSiteShape"

HAnimSite69.children.append(Shape71)

HAnimSegment44.children.append(HAnimSite69)
HAnimSite72 = x3d.HAnimSite()
HAnimSite72.DEF = "hanim_r_iliocristale_pt"
HAnimSite72.name = "r_iliocristale_pt"
HAnimSite72.translation = [-0.1525,1.0628,0.0035]
TouchSensor73 = x3d.TouchSensor()
TouchSensor73.description = "HAnimSite r_iliocristale_pt"

HAnimSite72.children.append(TouchSensor73)
Shape74 = x3d.Shape()
Shape74.USE = "HAnimSiteShape"

HAnimSite72.children.append(Shape74)

HAnimSegment44.children.append(HAnimSite72)
HAnimSite75 = x3d.HAnimSite()
HAnimSite75.DEF = "hanim_r_psis_pt"
HAnimSite75.name = "r_psis_pt"
HAnimSite75.translation = [-0.0716,1.0190,-0.1138]
TouchSensor76 = x3d.TouchSensor()
TouchSensor76.description = "HAnimSite r_psis_pt"

HAnimSite75.children.append(TouchSensor76)
Shape77 = x3d.Shape()
Shape77.USE = "HAnimSiteShape"

HAnimSite75.children.append(Shape77)

HAnimSegment44.children.append(HAnimSite75)
HAnimSite78 = x3d.HAnimSite()
HAnimSite78.DEF = "hanim_r_trochanterion_pt"
HAnimSite78.name = "r_trochanterion_pt"
HAnimSite78.translation = [-0.1689,0.8419,0.0352]
TouchSensor79 = x3d.TouchSensor()
TouchSensor79.description = "HAnimSite r_trochanterion_pt"

HAnimSite78.children.append(TouchSensor79)
Shape80 = x3d.Shape()
Shape80.USE = "HAnimSiteShape"

HAnimSite78.children.append(Shape80)

HAnimSegment44.children.append(HAnimSite78)
Shape81 = x3d.Shape()
LineSet82 = x3d.LineSet()
LineSet82.vertexCount = [2]
Coordinate83 = x3d.Coordinate()

LineSet82.coord = Coordinate83
""" from humanoid_root to vl5 """
ColorRGBA84 = x3d.ColorRGBA()
ColorRGBA84.USE = "HAnimSegmentLineColorRGBA"

LineSet82.color = ColorRGBA84

Shape81.geometry = LineSet82

HAnimSegment44.children.append(Shape81)
HAnimSite85 = x3d.HAnimSite()
HAnimSite85.DEF = "hanim_navel_pt"
HAnimSite85.name = "navel_pt"
HAnimSite85.translation = [0.0069,1.0966,0.1017]
TouchSensor86 = x3d.TouchSensor()
TouchSensor86.description = "HAnimSite navel_pt"

HAnimSite85.children.append(TouchSensor86)
Shape87 = x3d.Shape()
Shape87.USE = "HAnimSiteShape"

HAnimSite85.children.append(Shape87)

HAnimSegment44.children.append(HAnimSite85)
HAnimSite88 = x3d.HAnimSite()
HAnimSite88.DEF = "hanim_waist_preferred_anterior_pt"
HAnimSite88.name = "waist_preferred_anterior_pt"
HAnimSite88.translation = [0,1,0]
TouchSensor89 = x3d.TouchSensor()
TouchSensor89.description = "HAnimSite waist_preferred_anterior_pt"

HAnimSite88.children.append(TouchSensor89)
Shape90 = x3d.Shape()
Shape90.USE = "HAnimSiteShape"

HAnimSite88.children.append(Shape90)

HAnimSegment44.children.append(HAnimSite88)
HAnimSite91 = x3d.HAnimSite()
HAnimSite91.DEF = "hanim_waist_preferred_posterior_pt"
HAnimSite91.name = "waist_preferred_posterior_pt"
HAnimSite91.translation = [0.2900,1.0915,-0.1091]
TouchSensor92 = x3d.TouchSensor()
TouchSensor92.description = "HAnimSite waist_preferred_posterior_pt"

HAnimSite91.children.append(TouchSensor92)
Shape93 = x3d.Shape()
Shape93.USE = "HAnimSiteShape"

HAnimSite91.children.append(Shape93)

HAnimSegment44.children.append(HAnimSite91)

HAnimJoint43.children.append(HAnimSegment44)
HAnimJoint94 = x3d.HAnimJoint()
HAnimJoint94.DEF = "hanim_sacroiliac"
HAnimJoint94.name = "sacroiliac"
HAnimJoint94.center = [0.0000,0.9149,0.0016]
HAnimSegment95 = x3d.HAnimSegment()
HAnimSegment95.DEF = "hanim_pelvis"
HAnimSegment95.name = "pelvis"
Transform96 = x3d.Transform()
Transform96.translation = [0.0000,0.9149,0.0016]
Shape97 = x3d.Shape()
Shape97.USE = "HAnimJointShape"

Transform96.children.append(Shape97)

HAnimSegment95.children.append(Transform96)
Shape98 = x3d.Shape()
LineSet99 = x3d.LineSet()
LineSet99.vertexCount = [2]
Coordinate100 = x3d.Coordinate()

LineSet99.coord = Coordinate100
""" from sacroiliac to l_hip """
ColorRGBA101 = x3d.ColorRGBA()
ColorRGBA101.USE = "HAnimSegmentLineColorRGBA"

LineSet99.color = ColorRGBA101

Shape98.geometry = LineSet99

HAnimSegment95.children.append(Shape98)
HAnimSite102 = x3d.HAnimSite()
HAnimSite102.DEF = "hanim_l_femoral_lateral_epicondyles_pt"
HAnimSite102.name = "l_femoral_lateral_epicondyles_pt"
HAnimSite102.translation = [0.1598,0.4967,0.0297]
TouchSensor103 = x3d.TouchSensor()
TouchSensor103.description = "HAnimSite l_femoral_lateral_epicondyles_pt"

HAnimSite102.children.append(TouchSensor103)
Shape104 = x3d.Shape()
Shape104.USE = "HAnimSiteShape"

HAnimSite102.children.append(Shape104)

HAnimSegment95.children.append(HAnimSite102)
HAnimSite105 = x3d.HAnimSite()
HAnimSite105.DEF = "hanim_l_femoral_medial_epicondyles_pt"
HAnimSite105.name = "l_femoral_medial_epicondyles_pt"
HAnimSite105.translation = [0.0398,0.4946,0.0303]
TouchSensor106 = x3d.TouchSensor()
TouchSensor106.description = "HAnimSite l_femoral_medial_epicondyles_pt"

HAnimSite105.children.append(TouchSensor106)
Shape107 = x3d.Shape()
Shape107.USE = "HAnimSiteShape"

HAnimSite105.children.append(Shape107)

HAnimSegment95.children.append(HAnimSite105)
HAnimSite108 = x3d.HAnimSite()
HAnimSite108.DEF = "hanim_l_knee_crease_pt"
HAnimSite108.name = "l_knee_crease_pt"
HAnimSite108.translation = [0.0993,0.4881,-0.0309]
TouchSensor109 = x3d.TouchSensor()
TouchSensor109.description = "HAnimSite l_knee_crease_pt"

HAnimSite108.children.append(TouchSensor109)
Shape110 = x3d.Shape()
Shape110.USE = "HAnimSiteShape"

HAnimSite108.children.append(Shape110)

HAnimSegment95.children.append(HAnimSite108)
HAnimSite111 = x3d.HAnimSite()
HAnimSite111.DEF = "hanim_l_suprapatella_pt"
HAnimSite111.name = "l_suprapatella_pt"
HAnimSite111.translation = [0,1,0]
TouchSensor112 = x3d.TouchSensor()
TouchSensor112.description = "HAnimSite l_suprapatella_pt"

HAnimSite111.children.append(TouchSensor112)
Shape113 = x3d.Shape()
Shape113.USE = "HAnimSiteShape"

HAnimSite111.children.append(Shape113)

HAnimSegment95.children.append(HAnimSite111)
Shape114 = x3d.Shape()
LineSet115 = x3d.LineSet()
LineSet115.vertexCount = [2]
Coordinate116 = x3d.Coordinate()

LineSet115.coord = Coordinate116
""" from sacroiliac to r_hip """
ColorRGBA117 = x3d.ColorRGBA()
ColorRGBA117.USE = "HAnimSegmentLineColorRGBA"

LineSet115.color = ColorRGBA117

Shape114.geometry = LineSet115

HAnimSegment95.children.append(Shape114)
HAnimSite118 = x3d.HAnimSite()
HAnimSite118.DEF = "hanim_r_femoral_lateral_epicondyles_pt"
HAnimSite118.name = "r_femoral_lateral_epicondyles_pt"
HAnimSite118.translation = [-0.1421,0.4992,0.0310]
TouchSensor119 = x3d.TouchSensor()
TouchSensor119.description = "HAnimSite r_femoral_lateral_epicondyles_pt"

HAnimSite118.children.append(TouchSensor119)
Shape120 = x3d.Shape()
Shape120.USE = "HAnimSiteShape"

HAnimSite118.children.append(Shape120)

HAnimSegment95.children.append(HAnimSite118)
HAnimSite121 = x3d.HAnimSite()
HAnimSite121.DEF = "hanim_r_femoral_medial_epicondyles_pt"
HAnimSite121.name = "r_femoral_medial_epicondyles_pt"
HAnimSite121.translation = [-0.0221,0.5014,0.0289]
TouchSensor122 = x3d.TouchSensor()
TouchSensor122.description = "HAnimSite r_femoral_medial_epicondyles_pt"

HAnimSite121.children.append(TouchSensor122)
Shape123 = x3d.Shape()
Shape123.USE = "HAnimSiteShape"

HAnimSite121.children.append(Shape123)

HAnimSegment95.children.append(HAnimSite121)
HAnimSite124 = x3d.HAnimSite()
HAnimSite124.DEF = "hanim_r_knee_crease_pt"
HAnimSite124.name = "r_knee_crease_pt"
HAnimSite124.translation = [-0.0825,0.4932,-0.0326]
TouchSensor125 = x3d.TouchSensor()
TouchSensor125.description = "HAnimSite r_knee_crease_pt"

HAnimSite124.children.append(TouchSensor125)
Shape126 = x3d.Shape()
Shape126.USE = "HAnimSiteShape"

HAnimSite124.children.append(Shape126)

HAnimSegment95.children.append(HAnimSite124)
HAnimSite127 = x3d.HAnimSite()
HAnimSite127.DEF = "hanim_r_suprapatella_pt"
HAnimSite127.name = "r_suprapatella_pt"
HAnimSite127.translation = [0,1,0]
TouchSensor128 = x3d.TouchSensor()
TouchSensor128.description = "HAnimSite r_suprapatella_pt"

HAnimSite127.children.append(TouchSensor128)
Shape129 = x3d.Shape()
Shape129.USE = "HAnimSiteShape"

HAnimSite127.children.append(Shape129)

HAnimSegment95.children.append(HAnimSite127)

HAnimJoint94.children.append(HAnimSegment95)
HAnimJoint130 = x3d.HAnimJoint()
HAnimJoint130.DEF = "hanim_l_hip"
HAnimJoint130.name = "l_hip"
HAnimJoint130.center = [0.0961,0.9124,-0.0001]
HAnimSegment131 = x3d.HAnimSegment()
HAnimSegment131.DEF = "hanim_l_thigh"
HAnimSegment131.name = "l_thigh"
Transform132 = x3d.Transform()
Transform132.translation = [0.0961,0.9124,-0.0001]
Shape133 = x3d.Shape()
Shape133.USE = "HAnimJointShape"

Transform132.children.append(Shape133)

HAnimSegment131.children.append(Transform132)
Shape134 = x3d.Shape()
LineSet135 = x3d.LineSet()
LineSet135.vertexCount = [2]
Coordinate136 = x3d.Coordinate()

LineSet135.coord = Coordinate136
""" from l_hip to l_knee """
ColorRGBA137 = x3d.ColorRGBA()
ColorRGBA137.USE = "HAnimSegmentLineColorRGBA"

LineSet135.color = ColorRGBA137

Shape134.geometry = LineSet135

HAnimSegment131.children.append(Shape134)
HAnimSite138 = x3d.HAnimSite()
HAnimSite138.DEF = "hanim_l_lateral_malleolus_pt"
HAnimSite138.name = "l_lateral_malleolus_pt"
HAnimSite138.translation = [0.1308,0.0597,-0.1032]
TouchSensor139 = x3d.TouchSensor()
TouchSensor139.description = "HAnimSite l_lateral_malleolus_pt"

HAnimSite138.children.append(TouchSensor139)
Shape140 = x3d.Shape()
Shape140.USE = "HAnimSiteShape"

HAnimSite138.children.append(Shape140)

HAnimSegment131.children.append(HAnimSite138)
HAnimSite141 = x3d.HAnimSite()
HAnimSite141.DEF = "hanim_l_medial_malleolus_pt"
HAnimSite141.name = "l_medial_malleolus_pt"
HAnimSite141.translation = [0.0890,0.0716,-0.0881]
TouchSensor142 = x3d.TouchSensor()
TouchSensor142.description = "HAnimSite l_medial_malleolus_pt"

HAnimSite141.children.append(TouchSensor142)
Shape143 = x3d.Shape()
Shape143.USE = "HAnimSiteShape"

HAnimSite141.children.append(Shape143)

HAnimSegment131.children.append(HAnimSite141)
HAnimSite144 = x3d.HAnimSite()
HAnimSite144.DEF = "hanim_l_tibiale_pt"
HAnimSite144.name = "l_tibiale_pt"
HAnimSite144.translation = [0,1,0]
TouchSensor145 = x3d.TouchSensor()
TouchSensor145.description = "HAnimSite l_tibiale_pt"

HAnimSite144.children.append(TouchSensor145)
Shape146 = x3d.Shape()
Shape146.USE = "HAnimSiteShape"

HAnimSite144.children.append(Shape146)

HAnimSegment131.children.append(HAnimSite144)

HAnimJoint130.children.append(HAnimSegment131)
HAnimJoint147 = x3d.HAnimJoint()
HAnimJoint147.DEF = "hanim_l_knee"
HAnimJoint147.name = "l_knee"
HAnimJoint147.center = [0.1040,0.4867,0.0308]
HAnimSegment148 = x3d.HAnimSegment()
HAnimSegment148.DEF = "hanim_l_calf"
HAnimSegment148.name = "l_calf"
Transform149 = x3d.Transform()
Transform149.translation = [0.1040,0.4867,0.0308]
Shape150 = x3d.Shape()
Shape150.USE = "HAnimJointShape"

Transform149.children.append(Shape150)

HAnimSegment148.children.append(Transform149)
Shape151 = x3d.Shape()
LineSet152 = x3d.LineSet()
LineSet152.vertexCount = [2]
Coordinate153 = x3d.Coordinate()

LineSet152.coord = Coordinate153
""" from l_knee to l_talocrural """
ColorRGBA154 = x3d.ColorRGBA()
ColorRGBA154.USE = "HAnimSegmentLineColorRGBA"

LineSet152.color = ColorRGBA154

Shape151.geometry = LineSet152

HAnimSegment148.children.append(Shape151)
HAnimSite155 = x3d.HAnimSite()
HAnimSite155.DEF = "hanim_l_calcaneus_posterior_pt"
HAnimSite155.name = "l_calcaneus_posterior_pt"
HAnimSite155.translation = [0.0974,0.0259,-0.1171]
TouchSensor156 = x3d.TouchSensor()
TouchSensor156.description = "HAnimSite l_calcaneus_posterior_pt"

HAnimSite155.children.append(TouchSensor156)
Shape157 = x3d.Shape()
Shape157.USE = "HAnimSiteShape"

HAnimSite155.children.append(Shape157)

HAnimSegment148.children.append(HAnimSite155)
HAnimSite158 = x3d.HAnimSite()
HAnimSite158.DEF = "hanim_l_sphyrion_pt"
HAnimSite158.name = "l_sphyrion_pt"
HAnimSite158.translation = [0.0890,0.0575,-0.0943]
TouchSensor159 = x3d.TouchSensor()
TouchSensor159.description = "HAnimSite l_sphyrion_pt"

HAnimSite158.children.append(TouchSensor159)
Shape160 = x3d.Shape()
Shape160.USE = "HAnimSiteShape"

HAnimSite158.children.append(Shape160)

HAnimSegment148.children.append(HAnimSite158)

HAnimJoint147.children.append(HAnimSegment148)
HAnimJoint161 = x3d.HAnimJoint()
HAnimJoint161.DEF = "hanim_l_talocrural"
HAnimJoint161.name = "l_talocrural"
HAnimJoint161.center = [0.1101,0.0656,-0.0736]
HAnimSegment162 = x3d.HAnimSegment()
HAnimSegment162.DEF = "hanim_l_talus"
HAnimSegment162.name = "l_talus"
Transform163 = x3d.Transform()
Transform163.translation = [0.1101,0.0656,-0.0736]
Shape164 = x3d.Shape()
Shape164.USE = "HAnimJointShape"

Transform163.children.append(Shape164)

HAnimSegment162.children.append(Transform163)
Shape165 = x3d.Shape()
LineSet166 = x3d.LineSet()
LineSet166.vertexCount = [2]
Coordinate167 = x3d.Coordinate()

LineSet166.coord = Coordinate167
""" from l_talocrural to l_talocalcaneonavicular """
ColorRGBA168 = x3d.ColorRGBA()
ColorRGBA168.USE = "HAnimSegmentLineColorRGBA"

LineSet166.color = ColorRGBA168

Shape165.geometry = LineSet166

HAnimSegment162.children.append(Shape165)
Shape169 = x3d.Shape()
LineSet170 = x3d.LineSet()
LineSet170.vertexCount = [2]
Coordinate171 = x3d.Coordinate()

LineSet170.coord = Coordinate171
""" from l_talocrural to l_calcaneocuboid """
ColorRGBA172 = x3d.ColorRGBA()
ColorRGBA172.USE = "HAnimSegmentLineColorRGBA"

LineSet170.color = ColorRGBA172

Shape169.geometry = LineSet170

HAnimSegment162.children.append(Shape169)

HAnimJoint161.children.append(HAnimSegment162)
HAnimJoint173 = x3d.HAnimJoint()
HAnimJoint173.DEF = "hanim_l_talocalcaneonavicular"
HAnimJoint173.name = "l_talocalcaneonavicular"
HAnimJoint173.center = [0.0,-0.3,0]
HAnimSegment174 = x3d.HAnimSegment()
HAnimSegment174.DEF = "hanim_l_navicular"
HAnimSegment174.name = "l_navicular"
Transform175 = x3d.Transform()
Transform175.translation = [0.0,-0.3,0]
Shape176 = x3d.Shape()
Shape176.USE = "HAnimJointShape"

Transform175.children.append(Shape176)

HAnimSegment174.children.append(Transform175)
Shape177 = x3d.Shape()
LineSet178 = x3d.LineSet()
LineSet178.vertexCount = [2]
Coordinate179 = x3d.Coordinate()

LineSet178.coord = Coordinate179
""" from l_talocalcaneonavicular to l_cuneonavicular_1 """
ColorRGBA180 = x3d.ColorRGBA()
ColorRGBA180.USE = "HAnimSegmentLineColorRGBA"

LineSet178.color = ColorRGBA180

Shape177.geometry = LineSet178

HAnimSegment174.children.append(Shape177)
Shape181 = x3d.Shape()
LineSet182 = x3d.LineSet()
LineSet182.vertexCount = [2]
Coordinate183 = x3d.Coordinate()

LineSet182.coord = Coordinate183
""" from l_talocalcaneonavicular to l_cuneonavicular_2 """
ColorRGBA184 = x3d.ColorRGBA()
ColorRGBA184.USE = "HAnimSegmentLineColorRGBA"

LineSet182.color = ColorRGBA184

Shape181.geometry = LineSet182

HAnimSegment174.children.append(Shape181)
Shape185 = x3d.Shape()
LineSet186 = x3d.LineSet()
LineSet186.vertexCount = [2]
Coordinate187 = x3d.Coordinate()

LineSet186.coord = Coordinate187
""" from l_talocalcaneonavicular to l_cuneonavicular_3 """
ColorRGBA188 = x3d.ColorRGBA()
ColorRGBA188.USE = "HAnimSegmentLineColorRGBA"

LineSet186.color = ColorRGBA188

Shape185.geometry = LineSet186

HAnimSegment174.children.append(Shape185)

HAnimJoint173.children.append(HAnimSegment174)
HAnimJoint189 = x3d.HAnimJoint()
HAnimJoint189.DEF = "hanim_l_cuneonavicular_1"
HAnimJoint189.name = "l_cuneonavicular_1"
HAnimJoint189.center = [-0.1,-0.45,0]
HAnimSegment190 = x3d.HAnimSegment()
HAnimSegment190.DEF = "hanim_l_cuneiform_1"
HAnimSegment190.name = "l_cuneiform_1"
Transform191 = x3d.Transform()
Transform191.translation = [-0.1,-0.45,0]
Shape192 = x3d.Shape()
Shape192.USE = "HAnimJointShape"

Transform191.children.append(Shape192)

HAnimSegment190.children.append(Transform191)
Shape193 = x3d.Shape()
LineSet194 = x3d.LineSet()
LineSet194.vertexCount = [2]
Coordinate195 = x3d.Coordinate()

LineSet194.coord = Coordinate195
""" from l_cuneonavicular_1 to l_tarsometatarsal_1 """
ColorRGBA196 = x3d.ColorRGBA()
ColorRGBA196.USE = "HAnimSegmentLineColorRGBA"

LineSet194.color = ColorRGBA196

Shape193.geometry = LineSet194

HAnimSegment190.children.append(Shape193)

HAnimJoint189.children.append(HAnimSegment190)
HAnimJoint197 = x3d.HAnimJoint()
HAnimJoint197.DEF = "hanim_l_tarsometatarsal_1"
HAnimJoint197.name = "l_tarsometatarsal_1"
HAnimJoint197.center = [-0.1,-0.6,0]
HAnimSegment198 = x3d.HAnimSegment()
HAnimSegment198.DEF = "hanim_l_metatarsal_1"
HAnimSegment198.name = "l_metatarsal_1"
Transform199 = x3d.Transform()
Transform199.translation = [-0.1,-0.6,0]
Shape200 = x3d.Shape()
Shape200.USE = "HAnimJointShape"

Transform199.children.append(Shape200)

HAnimSegment198.children.append(Transform199)
Shape201 = x3d.Shape()
LineSet202 = x3d.LineSet()
LineSet202.vertexCount = [2]
Coordinate203 = x3d.Coordinate()

LineSet202.coord = Coordinate203
""" from l_tarsometatarsal_1 to l_metatarsophalangeal_1 """
ColorRGBA204 = x3d.ColorRGBA()
ColorRGBA204.USE = "HAnimSegmentLineColorRGBA"

LineSet202.color = ColorRGBA204

Shape201.geometry = LineSet202

HAnimSegment198.children.append(Shape201)
HAnimSite205 = x3d.HAnimSite()
HAnimSite205.DEF = "hanim_l_metatarsal_phalanx_1_pt"
HAnimSite205.name = "l_metatarsal_phalanx_1_pt"
HAnimSite205.translation = [0,1,0]
TouchSensor206 = x3d.TouchSensor()
TouchSensor206.description = "HAnimSite l_metatarsal_phalanx_1_pt"

HAnimSite205.children.append(TouchSensor206)
Shape207 = x3d.Shape()
Shape207.USE = "HAnimSiteShape"

HAnimSite205.children.append(Shape207)

HAnimSegment198.children.append(HAnimSite205)

HAnimJoint197.children.append(HAnimSegment198)
HAnimJoint208 = x3d.HAnimJoint()
HAnimJoint208.DEF = "hanim_l_metatarsophalangeal_1"
HAnimJoint208.name = "l_metatarsophalangeal_1"
HAnimJoint208.center = [-0.1,-0.9,0]
HAnimSegment209 = x3d.HAnimSegment()
HAnimSegment209.DEF = "hanim_l_tarsal_proximal_phalanx_1"
HAnimSegment209.name = "l_tarsal_proximal_phalanx_1"
Transform210 = x3d.Transform()
Transform210.translation = [-0.1,-0.9,0]
Shape211 = x3d.Shape()
Shape211.USE = "HAnimJointShape"

Transform210.children.append(Shape211)

HAnimSegment209.children.append(Transform210)
Shape212 = x3d.Shape()
LineSet213 = x3d.LineSet()
LineSet213.vertexCount = [2]
Coordinate214 = x3d.Coordinate()

LineSet213.coord = Coordinate214
""" from l_metatarsophalangeal_1 to l_tarsal_interphalangeal_1 """
ColorRGBA215 = x3d.ColorRGBA()
ColorRGBA215.USE = "HAnimSegmentLineColorRGBA"

LineSet213.color = ColorRGBA215

Shape212.geometry = LineSet213

HAnimSegment209.children.append(Shape212)
HAnimSite216 = x3d.HAnimSite()
HAnimSite216.DEF = "hanim_l_tarsal_distal_phalanx_1_tip"
HAnimSite216.name = "l_tarsal_distal_phalanx_1_tip"
HAnimSite216.translation = [-0.1,-1.05,0]
TouchSensor217 = x3d.TouchSensor()
TouchSensor217.description = "HAnimSite l_tarsal_distal_phalanx_1_tip"

HAnimSite216.children.append(TouchSensor217)
Shape218 = x3d.Shape()
Shape218.USE = "HAnimSiteShape"

HAnimSite216.children.append(Shape218)

HAnimSegment209.children.append(HAnimSite216)

HAnimJoint208.children.append(HAnimSegment209)
HAnimJoint219 = x3d.HAnimJoint()
HAnimJoint219.DEF = "hanim_l_tarsal_interphalangeal_1"
HAnimJoint219.name = "l_tarsal_interphalangeal_1"
HAnimJoint219.center = [-0.1,-1.05,0]

HAnimJoint208.children.append(HAnimJoint219)

HAnimJoint197.children.append(HAnimJoint208)

HAnimJoint189.children.append(HAnimJoint197)

HAnimJoint173.children.append(HAnimJoint189)
HAnimJoint220 = x3d.HAnimJoint()
HAnimJoint220.DEF = "hanim_l_cuneonavicular_2"
HAnimJoint220.name = "l_cuneonavicular_2"
HAnimJoint220.center = [0.0,-0.45,0]
HAnimSegment221 = x3d.HAnimSegment()
HAnimSegment221.DEF = "hanim_l_cuneiform_2"
HAnimSegment221.name = "l_cuneiform_2"
Transform222 = x3d.Transform()
Transform222.translation = [0.0,-0.45,0]
Shape223 = x3d.Shape()
Shape223.USE = "HAnimJointShape"

Transform222.children.append(Shape223)

HAnimSegment221.children.append(Transform222)
Shape224 = x3d.Shape()
LineSet225 = x3d.LineSet()
LineSet225.vertexCount = [2]
Coordinate226 = x3d.Coordinate()

LineSet225.coord = Coordinate226
""" from l_cuneonavicular_2 to l_tarsometatarsal_2 """
ColorRGBA227 = x3d.ColorRGBA()
ColorRGBA227.USE = "HAnimSegmentLineColorRGBA"

LineSet225.color = ColorRGBA227

Shape224.geometry = LineSet225

HAnimSegment221.children.append(Shape224)

HAnimJoint220.children.append(HAnimSegment221)
HAnimJoint228 = x3d.HAnimJoint()
HAnimJoint228.DEF = "hanim_l_tarsometatarsal_2"
HAnimJoint228.name = "l_tarsometatarsal_2"
HAnimJoint228.center = [0.05,-0.6,0]
HAnimSegment229 = x3d.HAnimSegment()
HAnimSegment229.DEF = "hanim_l_metatarsal_2"
HAnimSegment229.name = "l_metatarsal_2"
Transform230 = x3d.Transform()
Transform230.translation = [0.05,-0.6,0]
Shape231 = x3d.Shape()
Shape231.USE = "HAnimJointShape"

Transform230.children.append(Shape231)

HAnimSegment229.children.append(Transform230)
Shape232 = x3d.Shape()
LineSet233 = x3d.LineSet()
LineSet233.vertexCount = [2]
Coordinate234 = x3d.Coordinate()

LineSet233.coord = Coordinate234
""" from l_tarsometatarsal_2 to l_metatarsophalangeal_2 """
ColorRGBA235 = x3d.ColorRGBA()
ColorRGBA235.USE = "HAnimSegmentLineColorRGBA"

LineSet233.color = ColorRGBA235

Shape232.geometry = LineSet233

HAnimSegment229.children.append(Shape232)

HAnimJoint228.children.append(HAnimSegment229)
HAnimJoint236 = x3d.HAnimJoint()
HAnimJoint236.DEF = "hanim_l_metatarsophalangeal_2"
HAnimJoint236.name = "l_metatarsophalangeal_2"
HAnimJoint236.center = [0.05,-0.9,0]
HAnimSegment237 = x3d.HAnimSegment()
HAnimSegment237.DEF = "hanim_l_tarsal_proximal_phalanx_2"
HAnimSegment237.name = "l_tarsal_proximal_phalanx_2"
Transform238 = x3d.Transform()
Transform238.translation = [0.05,-0.9,0]
Shape239 = x3d.Shape()
Shape239.USE = "HAnimJointShape"

Transform238.children.append(Shape239)

HAnimSegment237.children.append(Transform238)
Shape240 = x3d.Shape()
LineSet241 = x3d.LineSet()
LineSet241.vertexCount = [2]
Coordinate242 = x3d.Coordinate()

LineSet241.coord = Coordinate242
""" from l_metatarsophalangeal_2 to l_tarsal_proximal_interphalangeal_2 """
ColorRGBA243 = x3d.ColorRGBA()
ColorRGBA243.USE = "HAnimSegmentLineColorRGBA"

LineSet241.color = ColorRGBA243

Shape240.geometry = LineSet241

HAnimSegment237.children.append(Shape240)

HAnimJoint236.children.append(HAnimSegment237)
HAnimJoint244 = x3d.HAnimJoint()
HAnimJoint244.DEF = "hanim_l_tarsal_proximal_interphalangeal_2"
HAnimJoint244.name = "l_tarsal_proximal_interphalangeal_2"
HAnimJoint244.center = [0.05,-1.05,0]
HAnimSegment245 = x3d.HAnimSegment()
HAnimSegment245.DEF = "hanim_l_tarsal_middle_phalanx_2"
HAnimSegment245.name = "l_tarsal_middle_phalanx_2"
Transform246 = x3d.Transform()
Transform246.translation = [0.05,-1.05,0]
Shape247 = x3d.Shape()
Shape247.USE = "HAnimJointShape"

Transform246.children.append(Shape247)

HAnimSegment245.children.append(Transform246)
Shape248 = x3d.Shape()
LineSet249 = x3d.LineSet()
LineSet249.vertexCount = [2]
Coordinate250 = x3d.Coordinate()

LineSet249.coord = Coordinate250
""" from l_tarsal_proximal_interphalangeal_2 to l_tarsal_distal_interphalangeal_2 """
ColorRGBA251 = x3d.ColorRGBA()
ColorRGBA251.USE = "HAnimSegmentLineColorRGBA"

LineSet249.color = ColorRGBA251

Shape248.geometry = LineSet249

HAnimSegment245.children.append(Shape248)
HAnimSite252 = x3d.HAnimSite()
HAnimSite252.DEF = "hanim_l_tarsal_distal_phalanx_2_tip"
HAnimSite252.name = "l_tarsal_distal_phalanx_2_tip"
HAnimSite252.translation = [0.05,-1.12,0]
TouchSensor253 = x3d.TouchSensor()
TouchSensor253.description = "HAnimSite l_tarsal_distal_phalanx_2_tip"

HAnimSite252.children.append(TouchSensor253)
Shape254 = x3d.Shape()
Shape254.USE = "HAnimSiteShape"

HAnimSite252.children.append(Shape254)

HAnimSegment245.children.append(HAnimSite252)

HAnimJoint244.children.append(HAnimSegment245)
HAnimJoint255 = x3d.HAnimJoint()
HAnimJoint255.DEF = "hanim_l_tarsal_distal_interphalangeal_2"
HAnimJoint255.name = "l_tarsal_distal_interphalangeal_2"
HAnimJoint255.center = [0.05,-1.12,0]

HAnimJoint244.children.append(HAnimJoint255)

HAnimJoint236.children.append(HAnimJoint244)

HAnimJoint228.children.append(HAnimJoint236)

HAnimJoint220.children.append(HAnimJoint228)

HAnimJoint173.children.append(HAnimJoint220)
HAnimJoint256 = x3d.HAnimJoint()
HAnimJoint256.DEF = "hanim_l_cuneonavicular_3"
HAnimJoint256.name = "l_cuneonavicular_3"
HAnimJoint256.center = [0.1,-0.4,0]
HAnimSegment257 = x3d.HAnimSegment()
HAnimSegment257.DEF = "hanim_l_cuneiform_3"
HAnimSegment257.name = "l_cuneiform_3"
Transform258 = x3d.Transform()
Transform258.translation = [0.1,-0.4,0]
Shape259 = x3d.Shape()
Shape259.USE = "HAnimJointShape"

Transform258.children.append(Shape259)

HAnimSegment257.children.append(Transform258)
Shape260 = x3d.Shape()
LineSet261 = x3d.LineSet()
LineSet261.vertexCount = [2]
Coordinate262 = x3d.Coordinate()

LineSet261.coord = Coordinate262
""" from l_cuneonavicular_3 to l_tarsometatarsal_3 """
ColorRGBA263 = x3d.ColorRGBA()
ColorRGBA263.USE = "HAnimSegmentLineColorRGBA"

LineSet261.color = ColorRGBA263

Shape260.geometry = LineSet261

HAnimSegment257.children.append(Shape260)

HAnimJoint256.children.append(HAnimSegment257)
HAnimJoint264 = x3d.HAnimJoint()
HAnimJoint264.DEF = "hanim_l_tarsometatarsal_3"
HAnimJoint264.name = "l_tarsometatarsal_3"
HAnimJoint264.center = [0.15,-0.6,0]
HAnimSegment265 = x3d.HAnimSegment()
HAnimSegment265.DEF = "hanim_l_metatarsal_3"
HAnimSegment265.name = "l_metatarsal_3"
Transform266 = x3d.Transform()
Transform266.translation = [0.15,-0.6,0]
Shape267 = x3d.Shape()
Shape267.USE = "HAnimJointShape"

Transform266.children.append(Shape267)

HAnimSegment265.children.append(Transform266)
Shape268 = x3d.Shape()
LineSet269 = x3d.LineSet()
LineSet269.vertexCount = [2]
Coordinate270 = x3d.Coordinate()

LineSet269.coord = Coordinate270
""" from l_tarsometatarsal_3 to l_metatarsophalangeal_3 """
ColorRGBA271 = x3d.ColorRGBA()
ColorRGBA271.USE = "HAnimSegmentLineColorRGBA"

LineSet269.color = ColorRGBA271

Shape268.geometry = LineSet269

HAnimSegment265.children.append(Shape268)

HAnimJoint264.children.append(HAnimSegment265)
HAnimJoint272 = x3d.HAnimJoint()
HAnimJoint272.DEF = "hanim_l_metatarsophalangeal_3"
HAnimJoint272.name = "l_metatarsophalangeal_3"
HAnimJoint272.center = [0.15,-0.9,0]
HAnimSegment273 = x3d.HAnimSegment()
HAnimSegment273.DEF = "hanim_l_tarsal_proximal_phalanx_3"
HAnimSegment273.name = "l_tarsal_proximal_phalanx_3"
Transform274 = x3d.Transform()
Transform274.translation = [0.15,-0.9,0]
Shape275 = x3d.Shape()
Shape275.USE = "HAnimJointShape"

Transform274.children.append(Shape275)

HAnimSegment273.children.append(Transform274)
Shape276 = x3d.Shape()
LineSet277 = x3d.LineSet()
LineSet277.vertexCount = [2]
Coordinate278 = x3d.Coordinate()

LineSet277.coord = Coordinate278
""" from l_metatarsophalangeal_3 to l_tarsal_proximal_interphalangeal_3 """
ColorRGBA279 = x3d.ColorRGBA()
ColorRGBA279.USE = "HAnimSegmentLineColorRGBA"

LineSet277.color = ColorRGBA279

Shape276.geometry = LineSet277

HAnimSegment273.children.append(Shape276)

HAnimJoint272.children.append(HAnimSegment273)
HAnimJoint280 = x3d.HAnimJoint()
HAnimJoint280.DEF = "hanim_l_tarsal_proximal_interphalangeal_3"
HAnimJoint280.name = "l_tarsal_proximal_interphalangeal_3"
HAnimJoint280.center = [0.15,-1.05,0]
HAnimSegment281 = x3d.HAnimSegment()
HAnimSegment281.DEF = "hanim_l_tarsal_middle_phalanx_3"
HAnimSegment281.name = "l_tarsal_middle_phalanx_3"
Transform282 = x3d.Transform()
Transform282.translation = [0.15,-1.05,0]
Shape283 = x3d.Shape()
Shape283.USE = "HAnimJointShape"

Transform282.children.append(Shape283)

HAnimSegment281.children.append(Transform282)
Shape284 = x3d.Shape()
LineSet285 = x3d.LineSet()
LineSet285.vertexCount = [2]
Coordinate286 = x3d.Coordinate()

LineSet285.coord = Coordinate286
""" from l_tarsal_proximal_interphalangeal_3 to l_tarsal_distal_interphalangeal_3 """
ColorRGBA287 = x3d.ColorRGBA()
ColorRGBA287.USE = "HAnimSegmentLineColorRGBA"

LineSet285.color = ColorRGBA287

Shape284.geometry = LineSet285

HAnimSegment281.children.append(Shape284)
HAnimSite288 = x3d.HAnimSite()
HAnimSite288.DEF = "hanim_l_tarsal_distal_phalanx_3_tip"
HAnimSite288.name = "l_tarsal_distal_phalanx_3_tip"
HAnimSite288.translation = [0.15,-1.13,0]
TouchSensor289 = x3d.TouchSensor()
TouchSensor289.description = "HAnimSite l_tarsal_distal_phalanx_3_tip"

HAnimSite288.children.append(TouchSensor289)
Shape290 = x3d.Shape()
Shape290.USE = "HAnimSiteShape"

HAnimSite288.children.append(Shape290)

HAnimSegment281.children.append(HAnimSite288)

HAnimJoint280.children.append(HAnimSegment281)
HAnimJoint291 = x3d.HAnimJoint()
HAnimJoint291.DEF = "hanim_l_tarsal_distal_interphalangeal_3"
HAnimJoint291.name = "l_tarsal_distal_interphalangeal_3"
HAnimJoint291.center = [0.15,-1.13,0]

HAnimJoint280.children.append(HAnimJoint291)

HAnimJoint272.children.append(HAnimJoint280)

HAnimJoint264.children.append(HAnimJoint272)

HAnimJoint256.children.append(HAnimJoint264)

HAnimJoint173.children.append(HAnimJoint256)

HAnimJoint161.children.append(HAnimJoint173)
HAnimJoint292 = x3d.HAnimJoint()
HAnimJoint292.DEF = "hanim_l_calcaneocuboid"
HAnimJoint292.name = "l_calcaneocuboid"
HAnimJoint292.center = [0.2,0.3,0]
HAnimSegment293 = x3d.HAnimSegment()
HAnimSegment293.DEF = "hanim_l_calcaneus"
HAnimSegment293.name = "l_calcaneus"
Transform294 = x3d.Transform()
Transform294.translation = [0.2,0.3,0]
Shape295 = x3d.Shape()
Shape295.USE = "HAnimJointShape"

Transform294.children.append(Shape295)

HAnimSegment293.children.append(Transform294)
Shape296 = x3d.Shape()
LineSet297 = x3d.LineSet()
LineSet297.vertexCount = [2]
Coordinate298 = x3d.Coordinate()

LineSet297.coord = Coordinate298
""" from l_calcaneocuboid to l_transversetarsal """
ColorRGBA299 = x3d.ColorRGBA()
ColorRGBA299.USE = "HAnimSegmentLineColorRGBA"

LineSet297.color = ColorRGBA299

Shape296.geometry = LineSet297

HAnimSegment293.children.append(Shape296)

HAnimJoint292.children.append(HAnimSegment293)
HAnimJoint300 = x3d.HAnimJoint()
HAnimJoint300.DEF = "hanim_l_transversetarsal"
HAnimJoint300.name = "l_transversetarsal"
HAnimJoint300.center = [0.21,-0.3,0]
HAnimSegment301 = x3d.HAnimSegment()
HAnimSegment301.DEF = "hanim_l_cuboid"
HAnimSegment301.name = "l_cuboid"
Transform302 = x3d.Transform()
Transform302.translation = [0.21,-0.3,0]
Shape303 = x3d.Shape()
Shape303.USE = "HAnimJointShape"

Transform302.children.append(Shape303)

HAnimSegment301.children.append(Transform302)
Shape304 = x3d.Shape()
LineSet305 = x3d.LineSet()
LineSet305.vertexCount = [2]
Coordinate306 = x3d.Coordinate()

LineSet305.coord = Coordinate306
""" from l_transversetarsal to l_tarsometatarsal_4 """
ColorRGBA307 = x3d.ColorRGBA()
ColorRGBA307.USE = "HAnimSegmentLineColorRGBA"

LineSet305.color = ColorRGBA307

Shape304.geometry = LineSet305

HAnimSegment301.children.append(Shape304)
Shape308 = x3d.Shape()
LineSet309 = x3d.LineSet()
LineSet309.vertexCount = [2]
Coordinate310 = x3d.Coordinate()

LineSet309.coord = Coordinate310
""" from l_transversetarsal to l_tarsometatarsal_5 """
ColorRGBA311 = x3d.ColorRGBA()
ColorRGBA311.USE = "HAnimSegmentLineColorRGBA"

LineSet309.color = ColorRGBA311

Shape308.geometry = LineSet309

HAnimSegment301.children.append(Shape308)

HAnimJoint300.children.append(HAnimSegment301)
HAnimJoint312 = x3d.HAnimJoint()
HAnimJoint312.DEF = "hanim_l_tarsometatarsal_4"
HAnimJoint312.name = "l_tarsometatarsal_4"
HAnimJoint312.center = [0.25,-0.58,0]
HAnimSegment313 = x3d.HAnimSegment()
HAnimSegment313.DEF = "hanim_l_metatarsal_4"
HAnimSegment313.name = "l_metatarsal_4"
Transform314 = x3d.Transform()
Transform314.translation = [0.25,-0.58,0]
Shape315 = x3d.Shape()
Shape315.USE = "HAnimJointShape"

Transform314.children.append(Shape315)

HAnimSegment313.children.append(Transform314)
Shape316 = x3d.Shape()
LineSet317 = x3d.LineSet()
LineSet317.vertexCount = [2]
Coordinate318 = x3d.Coordinate()

LineSet317.coord = Coordinate318
""" from l_tarsometatarsal_4 to l_metatarsophalangeal_4 """
ColorRGBA319 = x3d.ColorRGBA()
ColorRGBA319.USE = "HAnimSegmentLineColorRGBA"

LineSet317.color = ColorRGBA319

Shape316.geometry = LineSet317

HAnimSegment313.children.append(Shape316)

HAnimJoint312.children.append(HAnimSegment313)
HAnimJoint320 = x3d.HAnimJoint()
HAnimJoint320.DEF = "hanim_l_metatarsophalangeal_4"
HAnimJoint320.name = "l_metatarsophalangeal_4"
HAnimJoint320.center = [0.25,-0.87,0]
HAnimSegment321 = x3d.HAnimSegment()
HAnimSegment321.DEF = "hanim_l_tarsal_proximal_phalanx_4"
HAnimSegment321.name = "l_tarsal_proximal_phalanx_4"
Transform322 = x3d.Transform()
Transform322.translation = [0.25,-0.87,0]
Shape323 = x3d.Shape()
Shape323.USE = "HAnimJointShape"

Transform322.children.append(Shape323)

HAnimSegment321.children.append(Transform322)
Shape324 = x3d.Shape()
LineSet325 = x3d.LineSet()
LineSet325.vertexCount = [2]
Coordinate326 = x3d.Coordinate()

LineSet325.coord = Coordinate326
""" from l_metatarsophalangeal_4 to l_tarsal_proximal_interphalangeal_4 """
ColorRGBA327 = x3d.ColorRGBA()
ColorRGBA327.USE = "HAnimSegmentLineColorRGBA"

LineSet325.color = ColorRGBA327

Shape324.geometry = LineSet325

HAnimSegment321.children.append(Shape324)

HAnimJoint320.children.append(HAnimSegment321)
HAnimJoint328 = x3d.HAnimJoint()
HAnimJoint328.DEF = "hanim_l_tarsal_proximal_interphalangeal_4"
HAnimJoint328.name = "l_tarsal_proximal_interphalangeal_4"
HAnimJoint328.center = [0.25,-1.0,0]
HAnimSegment329 = x3d.HAnimSegment()
HAnimSegment329.DEF = "hanim_l_tarsal_middle_phalanx_4"
HAnimSegment329.name = "l_tarsal_middle_phalanx_4"
Transform330 = x3d.Transform()
Transform330.translation = [0.25,-1.0,0]
Shape331 = x3d.Shape()
Shape331.USE = "HAnimJointShape"

Transform330.children.append(Shape331)

HAnimSegment329.children.append(Transform330)
Shape332 = x3d.Shape()
LineSet333 = x3d.LineSet()
LineSet333.vertexCount = [2]
Coordinate334 = x3d.Coordinate()

LineSet333.coord = Coordinate334
""" from l_tarsal_proximal_interphalangeal_4 to l_tarsal_distal_interphalangeal_4 """
ColorRGBA335 = x3d.ColorRGBA()
ColorRGBA335.USE = "HAnimSegmentLineColorRGBA"

LineSet333.color = ColorRGBA335

Shape332.geometry = LineSet333

HAnimSegment329.children.append(Shape332)
HAnimSite336 = x3d.HAnimSite()
HAnimSite336.DEF = "hanim_l_tarsal_distal_phalanx_4_tip"
HAnimSite336.name = "l_tarsal_distal_phalanx_4_tip"
HAnimSite336.translation = [0.25,-1.1,0]
TouchSensor337 = x3d.TouchSensor()
TouchSensor337.description = "HAnimSite l_tarsal_distal_phalanx_4_tip"

HAnimSite336.children.append(TouchSensor337)
Shape338 = x3d.Shape()
Shape338.USE = "HAnimSiteShape"

HAnimSite336.children.append(Shape338)

HAnimSegment329.children.append(HAnimSite336)

HAnimJoint328.children.append(HAnimSegment329)
HAnimJoint339 = x3d.HAnimJoint()
HAnimJoint339.DEF = "hanim_l_tarsal_distal_interphalangeal_4"
HAnimJoint339.name = "l_tarsal_distal_interphalangeal_4"
HAnimJoint339.center = [0.25,-1.1,0]

HAnimJoint328.children.append(HAnimJoint339)

HAnimJoint320.children.append(HAnimJoint328)

HAnimJoint312.children.append(HAnimJoint320)

HAnimJoint300.children.append(HAnimJoint312)
HAnimJoint340 = x3d.HAnimJoint()
HAnimJoint340.DEF = "hanim_l_tarsometatarsal_5"
HAnimJoint340.name = "l_tarsometatarsal_5"
HAnimJoint340.center = [0.33,-0.52,0]
HAnimSegment341 = x3d.HAnimSegment()
HAnimSegment341.DEF = "hanim_l_metatarsal_5"
HAnimSegment341.name = "l_metatarsal_5"
Transform342 = x3d.Transform()
Transform342.translation = [0.33,-0.52,0]
Shape343 = x3d.Shape()
Shape343.USE = "HAnimJointShape"

Transform342.children.append(Shape343)

HAnimSegment341.children.append(Transform342)
Shape344 = x3d.Shape()
LineSet345 = x3d.LineSet()
LineSet345.vertexCount = [2]
Coordinate346 = x3d.Coordinate()

LineSet345.coord = Coordinate346
""" from l_tarsometatarsal_5 to l_metatarsophalangeal_5 """
ColorRGBA347 = x3d.ColorRGBA()
ColorRGBA347.USE = "HAnimSegmentLineColorRGBA"

LineSet345.color = ColorRGBA347

Shape344.geometry = LineSet345

HAnimSegment341.children.append(Shape344)
HAnimSite348 = x3d.HAnimSite()
HAnimSite348.DEF = "hanim_l_metatarsal_phalanx_5_pt"
HAnimSite348.name = "l_metatarsal_phalanx_5_pt"
HAnimSite348.translation = [0,1,0]
TouchSensor349 = x3d.TouchSensor()
TouchSensor349.description = "HAnimSite l_metatarsal_phalanx_5_pt"

HAnimSite348.children.append(TouchSensor349)
Shape350 = x3d.Shape()
Shape350.USE = "HAnimSiteShape"

HAnimSite348.children.append(Shape350)

HAnimSegment341.children.append(HAnimSite348)

HAnimJoint340.children.append(HAnimSegment341)
HAnimJoint351 = x3d.HAnimJoint()
HAnimJoint351.DEF = "hanim_l_metatarsophalangeal_5"
HAnimJoint351.name = "l_metatarsophalangeal_5"
HAnimJoint351.center = [0.34,-0.8,0]
HAnimSegment352 = x3d.HAnimSegment()
HAnimSegment352.DEF = "hanim_l_tarsal_proximal_phalanx_5"
HAnimSegment352.name = "l_tarsal_proximal_phalanx_5"
Transform353 = x3d.Transform()
Transform353.translation = [0.34,-0.8,0]
Shape354 = x3d.Shape()
Shape354.USE = "HAnimJointShape"

Transform353.children.append(Shape354)

HAnimSegment352.children.append(Transform353)
Shape355 = x3d.Shape()
LineSet356 = x3d.LineSet()
LineSet356.vertexCount = [2]
Coordinate357 = x3d.Coordinate()

LineSet356.coord = Coordinate357
""" from l_metatarsophalangeal_5 to l_tarsal_proximal_interphalangeal_5 """
ColorRGBA358 = x3d.ColorRGBA()
ColorRGBA358.USE = "HAnimSegmentLineColorRGBA"

LineSet356.color = ColorRGBA358

Shape355.geometry = LineSet356

HAnimSegment352.children.append(Shape355)

HAnimJoint351.children.append(HAnimSegment352)
HAnimJoint359 = x3d.HAnimJoint()
HAnimJoint359.DEF = "hanim_l_tarsal_proximal_interphalangeal_5"
HAnimJoint359.name = "l_tarsal_proximal_interphalangeal_5"
HAnimJoint359.center = [0.34,-0.95,0]
HAnimSegment360 = x3d.HAnimSegment()
HAnimSegment360.DEF = "hanim_l_tarsal_middle_phalanx_5"
HAnimSegment360.name = "l_tarsal_middle_phalanx_5"
Transform361 = x3d.Transform()
Transform361.translation = [0.34,-0.95,0]
Shape362 = x3d.Shape()
Shape362.USE = "HAnimJointShape"

Transform361.children.append(Shape362)

HAnimSegment360.children.append(Transform361)
Shape363 = x3d.Shape()
LineSet364 = x3d.LineSet()
LineSet364.vertexCount = [2]
Coordinate365 = x3d.Coordinate()

LineSet364.coord = Coordinate365
""" from l_tarsal_proximal_interphalangeal_5 to l_tarsal_distal_interphalangeal_5 """
ColorRGBA366 = x3d.ColorRGBA()
ColorRGBA366.USE = "HAnimSegmentLineColorRGBA"

LineSet364.color = ColorRGBA366

Shape363.geometry = LineSet364

HAnimSegment360.children.append(Shape363)
HAnimSite367 = x3d.HAnimSite()
HAnimSite367.DEF = "hanim_l_tarsal_distal_phalanx_5_tip"
HAnimSite367.name = "l_tarsal_distal_phalanx_5_tip"
HAnimSite367.translation = [0.34,-1.05,0]
TouchSensor368 = x3d.TouchSensor()
TouchSensor368.description = "HAnimSite l_tarsal_distal_phalanx_5_tip"

HAnimSite367.children.append(TouchSensor368)
Shape369 = x3d.Shape()
Shape369.USE = "HAnimSiteShape"

HAnimSite367.children.append(Shape369)

HAnimSegment360.children.append(HAnimSite367)

HAnimJoint359.children.append(HAnimSegment360)
HAnimJoint370 = x3d.HAnimJoint()
HAnimJoint370.DEF = "hanim_l_tarsal_distal_interphalangeal_5"
HAnimJoint370.name = "l_tarsal_distal_interphalangeal_5"
HAnimJoint370.center = [0.34,-1.05,0]

HAnimJoint359.children.append(HAnimJoint370)

HAnimJoint351.children.append(HAnimJoint359)

HAnimJoint340.children.append(HAnimJoint351)

HAnimJoint300.children.append(HAnimJoint340)

HAnimJoint292.children.append(HAnimJoint300)

HAnimJoint161.children.append(HAnimJoint292)

HAnimJoint147.children.append(HAnimJoint161)

HAnimJoint130.children.append(HAnimJoint147)

HAnimJoint94.children.append(HAnimJoint130)
HAnimJoint371 = x3d.HAnimJoint()
HAnimJoint371.DEF = "hanim_r_hip"
HAnimJoint371.name = "r_hip"
HAnimJoint371.center = [-0.0950,0.9171,0.0029]
HAnimSegment372 = x3d.HAnimSegment()
HAnimSegment372.DEF = "hanim_r_thigh"
HAnimSegment372.name = "r_thigh"
Transform373 = x3d.Transform()
Transform373.translation = [-0.0950,0.9171,0.0029]
Shape374 = x3d.Shape()
Shape374.USE = "HAnimJointShape"

Transform373.children.append(Shape374)

HAnimSegment372.children.append(Transform373)
Shape375 = x3d.Shape()
LineSet376 = x3d.LineSet()
LineSet376.vertexCount = [2]
Coordinate377 = x3d.Coordinate()

LineSet376.coord = Coordinate377
""" from r_hip to r_knee """
ColorRGBA378 = x3d.ColorRGBA()
ColorRGBA378.USE = "HAnimSegmentLineColorRGBA"

LineSet376.color = ColorRGBA378

Shape375.geometry = LineSet376

HAnimSegment372.children.append(Shape375)
HAnimSite379 = x3d.HAnimSite()
HAnimSite379.DEF = "hanim_r_lateral_malleolus_pt"
HAnimSite379.name = "r_lateral_malleolus_pt"
HAnimSite379.translation = [-0.1006,0.0658,-0.1075]
TouchSensor380 = x3d.TouchSensor()
TouchSensor380.description = "HAnimSite r_lateral_malleolus_pt"

HAnimSite379.children.append(TouchSensor380)
Shape381 = x3d.Shape()
Shape381.USE = "HAnimSiteShape"

HAnimSite379.children.append(Shape381)

HAnimSegment372.children.append(HAnimSite379)
HAnimSite382 = x3d.HAnimSite()
HAnimSite382.DEF = "hanim_r_medial_malleolus_pt"
HAnimSite382.name = "r_medial_malleolus_pt"
HAnimSite382.translation = [-0.0591,0.0760,-0.0928]
TouchSensor383 = x3d.TouchSensor()
TouchSensor383.description = "HAnimSite r_medial_malleolus_pt"

HAnimSite382.children.append(TouchSensor383)
Shape384 = x3d.Shape()
Shape384.USE = "HAnimSiteShape"

HAnimSite382.children.append(Shape384)

HAnimSegment372.children.append(HAnimSite382)
HAnimSite385 = x3d.HAnimSite()
HAnimSite385.DEF = "hanim_r_tibiale_pt"
HAnimSite385.name = "r_tibiale_pt"
HAnimSite385.translation = [0,1,0]
TouchSensor386 = x3d.TouchSensor()
TouchSensor386.description = "HAnimSite r_tibiale_pt"

HAnimSite385.children.append(TouchSensor386)
Shape387 = x3d.Shape()
Shape387.USE = "HAnimSiteShape"

HAnimSite385.children.append(Shape387)

HAnimSegment372.children.append(HAnimSite385)

HAnimJoint371.children.append(HAnimSegment372)
HAnimJoint388 = x3d.HAnimJoint()
HAnimJoint388.DEF = "hanim_r_knee"
HAnimJoint388.name = "r_knee"
HAnimJoint388.center = [-0.0867,0.4913,0.0318]
HAnimSegment389 = x3d.HAnimSegment()
HAnimSegment389.DEF = "hanim_r_calf"
HAnimSegment389.name = "r_calf"
Transform390 = x3d.Transform()
Transform390.translation = [-0.0867,0.4913,0.0318]
Shape391 = x3d.Shape()
Shape391.USE = "HAnimJointShape"

Transform390.children.append(Shape391)

HAnimSegment389.children.append(Transform390)
Shape392 = x3d.Shape()
LineSet393 = x3d.LineSet()
LineSet393.vertexCount = [2]
Coordinate394 = x3d.Coordinate()

LineSet393.coord = Coordinate394
""" from r_knee to r_talocrural """
ColorRGBA395 = x3d.ColorRGBA()
ColorRGBA395.USE = "HAnimSegmentLineColorRGBA"

LineSet393.color = ColorRGBA395

Shape392.geometry = LineSet393

HAnimSegment389.children.append(Shape392)
HAnimSite396 = x3d.HAnimSite()
HAnimSite396.DEF = "hanim_r_calcaneus_posterior_pt"
HAnimSite396.name = "r_calcaneus_posterior_pt"
HAnimSite396.translation = [-0.0692,0.0297,-0.1221]
TouchSensor397 = x3d.TouchSensor()
TouchSensor397.description = "HAnimSite r_calcaneus_posterior_pt"

HAnimSite396.children.append(TouchSensor397)
Shape398 = x3d.Shape()
Shape398.USE = "HAnimSiteShape"

HAnimSite396.children.append(Shape398)

HAnimSegment389.children.append(HAnimSite396)
HAnimSite399 = x3d.HAnimSite()
HAnimSite399.DEF = "hanim_r_sphyrion_pt"
HAnimSite399.name = "r_sphyrion_pt"
HAnimSite399.translation = [-0.0603,0.0610,-0.1002]
TouchSensor400 = x3d.TouchSensor()
TouchSensor400.description = "HAnimSite r_sphyrion_pt"

HAnimSite399.children.append(TouchSensor400)
Shape401 = x3d.Shape()
Shape401.USE = "HAnimSiteShape"

HAnimSite399.children.append(Shape401)

HAnimSegment389.children.append(HAnimSite399)

HAnimJoint388.children.append(HAnimSegment389)
HAnimJoint402 = x3d.HAnimJoint()
HAnimJoint402.DEF = "hanim_r_talocrural"
HAnimJoint402.name = "r_talocrural"
HAnimJoint402.center = [-0.0801,0.0712,-0.0766]
HAnimSegment403 = x3d.HAnimSegment()
HAnimSegment403.DEF = "hanim_r_talus"
HAnimSegment403.name = "r_talus"
Transform404 = x3d.Transform()
Transform404.translation = [-0.0801,0.0712,-0.0766]
Shape405 = x3d.Shape()
Shape405.USE = "HAnimJointShape"

Transform404.children.append(Shape405)

HAnimSegment403.children.append(Transform404)
Shape406 = x3d.Shape()
LineSet407 = x3d.LineSet()
LineSet407.vertexCount = [2]
Coordinate408 = x3d.Coordinate()

LineSet407.coord = Coordinate408
""" from r_talocrural to r_talocalcaneonavicular """
ColorRGBA409 = x3d.ColorRGBA()
ColorRGBA409.USE = "HAnimSegmentLineColorRGBA"

LineSet407.color = ColorRGBA409

Shape406.geometry = LineSet407

HAnimSegment403.children.append(Shape406)
Shape410 = x3d.Shape()
LineSet411 = x3d.LineSet()
LineSet411.vertexCount = [2]
Coordinate412 = x3d.Coordinate()

LineSet411.coord = Coordinate412
""" from r_talocrural to r_calcaneocuboid """
ColorRGBA413 = x3d.ColorRGBA()
ColorRGBA413.USE = "HAnimSegmentLineColorRGBA"

LineSet411.color = ColorRGBA413

Shape410.geometry = LineSet411

HAnimSegment403.children.append(Shape410)

HAnimJoint402.children.append(HAnimSegment403)
HAnimJoint414 = x3d.HAnimJoint()
HAnimJoint414.DEF = "hanim_r_talocalcaneonavicular"
HAnimJoint414.name = "r_talocalcaneonavicular"
HAnimJoint414.center = [0.0,-0.3,0]
HAnimSegment415 = x3d.HAnimSegment()
HAnimSegment415.DEF = "hanim_r_navicular"
HAnimSegment415.name = "r_navicular"
Transform416 = x3d.Transform()
Transform416.translation = [0.0,-0.3,0]
Shape417 = x3d.Shape()
Shape417.USE = "HAnimJointShape"

Transform416.children.append(Shape417)

HAnimSegment415.children.append(Transform416)
Shape418 = x3d.Shape()
LineSet419 = x3d.LineSet()
LineSet419.vertexCount = [2]
Coordinate420 = x3d.Coordinate()

LineSet419.coord = Coordinate420
""" from r_talocalcaneonavicular to r_cuneonavicular_1 """
ColorRGBA421 = x3d.ColorRGBA()
ColorRGBA421.USE = "HAnimSegmentLineColorRGBA"

LineSet419.color = ColorRGBA421

Shape418.geometry = LineSet419

HAnimSegment415.children.append(Shape418)
Shape422 = x3d.Shape()
LineSet423 = x3d.LineSet()
LineSet423.vertexCount = [2]
Coordinate424 = x3d.Coordinate()

LineSet423.coord = Coordinate424
""" from r_talocalcaneonavicular to r_cuneonavicular_2 """
ColorRGBA425 = x3d.ColorRGBA()
ColorRGBA425.USE = "HAnimSegmentLineColorRGBA"

LineSet423.color = ColorRGBA425

Shape422.geometry = LineSet423

HAnimSegment415.children.append(Shape422)
Shape426 = x3d.Shape()
LineSet427 = x3d.LineSet()
LineSet427.vertexCount = [2]
Coordinate428 = x3d.Coordinate()

LineSet427.coord = Coordinate428
""" from r_talocalcaneonavicular to r_cuneonavicular_3 """
ColorRGBA429 = x3d.ColorRGBA()
ColorRGBA429.USE = "HAnimSegmentLineColorRGBA"

LineSet427.color = ColorRGBA429

Shape426.geometry = LineSet427

HAnimSegment415.children.append(Shape426)

HAnimJoint414.children.append(HAnimSegment415)
HAnimJoint430 = x3d.HAnimJoint()
HAnimJoint430.DEF = "hanim_r_cuneonavicular_1"
HAnimJoint430.name = "r_cuneonavicular_1"
HAnimJoint430.center = [0.1,-0.45,0]
HAnimSegment431 = x3d.HAnimSegment()
HAnimSegment431.DEF = "hanim_r_cuneiform_1"
HAnimSegment431.name = "r_cuneiform_1"
Transform432 = x3d.Transform()
Transform432.translation = [0.1,-0.45,0]
Shape433 = x3d.Shape()
Shape433.USE = "HAnimJointShape"

Transform432.children.append(Shape433)

HAnimSegment431.children.append(Transform432)
Shape434 = x3d.Shape()
LineSet435 = x3d.LineSet()
LineSet435.vertexCount = [2]
Coordinate436 = x3d.Coordinate()

LineSet435.coord = Coordinate436
""" from r_cuneonavicular_1 to r_tarsometatarsal_1 """
ColorRGBA437 = x3d.ColorRGBA()
ColorRGBA437.USE = "HAnimSegmentLineColorRGBA"

LineSet435.color = ColorRGBA437

Shape434.geometry = LineSet435

HAnimSegment431.children.append(Shape434)

HAnimJoint430.children.append(HAnimSegment431)
HAnimJoint438 = x3d.HAnimJoint()
HAnimJoint438.DEF = "hanim_r_tarsometatarsal_1"
HAnimJoint438.name = "r_tarsometatarsal_1"
HAnimJoint438.center = [0.1,-0.6,0]
HAnimSegment439 = x3d.HAnimSegment()
HAnimSegment439.DEF = "hanim_r_metatarsal_1"
HAnimSegment439.name = "r_metatarsal_1"
Transform440 = x3d.Transform()
Transform440.translation = [0.1,-0.6,0]
Shape441 = x3d.Shape()
Shape441.USE = "HAnimJointShape"

Transform440.children.append(Shape441)

HAnimSegment439.children.append(Transform440)
Shape442 = x3d.Shape()
LineSet443 = x3d.LineSet()
LineSet443.vertexCount = [2]
Coordinate444 = x3d.Coordinate()

LineSet443.coord = Coordinate444
""" from r_tarsometatarsal_1 to r_metatarsophalangeal_1 """
ColorRGBA445 = x3d.ColorRGBA()
ColorRGBA445.USE = "HAnimSegmentLineColorRGBA"

LineSet443.color = ColorRGBA445

Shape442.geometry = LineSet443

HAnimSegment439.children.append(Shape442)
HAnimSite446 = x3d.HAnimSite()
HAnimSite446.DEF = "hanim_r_metatarsal_phalanx_1_pt"
HAnimSite446.name = "r_metatarsal_phalanx_1_pt"
HAnimSite446.translation = [0,1,0]
TouchSensor447 = x3d.TouchSensor()
TouchSensor447.description = "HAnimSite r_metatarsal_phalanx_1_pt"

HAnimSite446.children.append(TouchSensor447)
Shape448 = x3d.Shape()
Shape448.USE = "HAnimSiteShape"

HAnimSite446.children.append(Shape448)

HAnimSegment439.children.append(HAnimSite446)

HAnimJoint438.children.append(HAnimSegment439)
HAnimJoint449 = x3d.HAnimJoint()
HAnimJoint449.DEF = "hanim_r_metatarsophalangeal_1"
HAnimJoint449.name = "r_metatarsophalangeal_1"
HAnimJoint449.center = [0.1,-0.9,0]
HAnimSegment450 = x3d.HAnimSegment()
HAnimSegment450.DEF = "hanim_r_tarsal_proximal_phalanx_1"
HAnimSegment450.name = "r_tarsal_proximal_phalanx_1"
Transform451 = x3d.Transform()
Transform451.translation = [0.1,-0.9,0]
Shape452 = x3d.Shape()
Shape452.USE = "HAnimJointShape"

Transform451.children.append(Shape452)

HAnimSegment450.children.append(Transform451)
Shape453 = x3d.Shape()
LineSet454 = x3d.LineSet()
LineSet454.vertexCount = [2]
Coordinate455 = x3d.Coordinate()

LineSet454.coord = Coordinate455
""" from r_metatarsophalangeal_1 to r_tarsal_interphalangeal_1 """
ColorRGBA456 = x3d.ColorRGBA()
ColorRGBA456.USE = "HAnimSegmentLineColorRGBA"

LineSet454.color = ColorRGBA456

Shape453.geometry = LineSet454

HAnimSegment450.children.append(Shape453)
HAnimSite457 = x3d.HAnimSite()
HAnimSite457.DEF = "hanim_r_tarsal_distal_phalanx_1_tip"
HAnimSite457.name = "r_tarsal_distal_phalanx_1_tip"
HAnimSite457.translation = [0.1,-1.05,0]
TouchSensor458 = x3d.TouchSensor()
TouchSensor458.description = "HAnimSite r_tarsal_distal_phalanx_1_tip"

HAnimSite457.children.append(TouchSensor458)
Shape459 = x3d.Shape()
Shape459.USE = "HAnimSiteShape"

HAnimSite457.children.append(Shape459)

HAnimSegment450.children.append(HAnimSite457)

HAnimJoint449.children.append(HAnimSegment450)
HAnimJoint460 = x3d.HAnimJoint()
HAnimJoint460.DEF = "hanim_r_tarsal_interphalangeal_1"
HAnimJoint460.name = "r_tarsal_interphalangeal_1"
HAnimJoint460.center = [0.1,-1.05,0]

HAnimJoint449.children.append(HAnimJoint460)

HAnimJoint438.children.append(HAnimJoint449)

HAnimJoint430.children.append(HAnimJoint438)

HAnimJoint414.children.append(HAnimJoint430)
HAnimJoint461 = x3d.HAnimJoint()
HAnimJoint461.DEF = "hanim_r_cuneonavicular_2"
HAnimJoint461.name = "r_cuneonavicular_2"
HAnimJoint461.center = [0.0,-0.45,0]
HAnimSegment462 = x3d.HAnimSegment()
HAnimSegment462.DEF = "hanim_r_cuneiform_2"
HAnimSegment462.name = "r_cuneiform_2"
Transform463 = x3d.Transform()
Transform463.translation = [0.0,-0.45,0]
Shape464 = x3d.Shape()
Shape464.USE = "HAnimJointShape"

Transform463.children.append(Shape464)

HAnimSegment462.children.append(Transform463)
Shape465 = x3d.Shape()
LineSet466 = x3d.LineSet()
LineSet466.vertexCount = [2]
Coordinate467 = x3d.Coordinate()

LineSet466.coord = Coordinate467
""" from r_cuneonavicular_2 to r_tarsometatarsal_2 """
ColorRGBA468 = x3d.ColorRGBA()
ColorRGBA468.USE = "HAnimSegmentLineColorRGBA"

LineSet466.color = ColorRGBA468

Shape465.geometry = LineSet466

HAnimSegment462.children.append(Shape465)

HAnimJoint461.children.append(HAnimSegment462)
HAnimJoint469 = x3d.HAnimJoint()
HAnimJoint469.DEF = "hanim_r_tarsometatarsal_2"
HAnimJoint469.name = "r_tarsometatarsal_2"
HAnimJoint469.center = [-0.05,-0.6,0]
HAnimSegment470 = x3d.HAnimSegment()
HAnimSegment470.DEF = "hanim_r_metatarsal_2"
HAnimSegment470.name = "r_metatarsal_2"
Transform471 = x3d.Transform()
Transform471.translation = [-0.05,-0.6,0]
Shape472 = x3d.Shape()
Shape472.USE = "HAnimJointShape"

Transform471.children.append(Shape472)

HAnimSegment470.children.append(Transform471)
Shape473 = x3d.Shape()
LineSet474 = x3d.LineSet()
LineSet474.vertexCount = [2]
Coordinate475 = x3d.Coordinate()

LineSet474.coord = Coordinate475
""" from r_tarsometatarsal_2 to r_metatarsophalangeal_2 """
ColorRGBA476 = x3d.ColorRGBA()
ColorRGBA476.USE = "HAnimSegmentLineColorRGBA"

LineSet474.color = ColorRGBA476

Shape473.geometry = LineSet474

HAnimSegment470.children.append(Shape473)

HAnimJoint469.children.append(HAnimSegment470)
HAnimJoint477 = x3d.HAnimJoint()
HAnimJoint477.DEF = "hanim_r_metatarsophalangeal_2"
HAnimJoint477.name = "r_metatarsophalangeal_2"
HAnimJoint477.center = [-0.05,-0.9,0]
HAnimSegment478 = x3d.HAnimSegment()
HAnimSegment478.DEF = "hanim_r_tarsal_proximal_phalanx_2"
HAnimSegment478.name = "r_tarsal_proximal_phalanx_2"
Transform479 = x3d.Transform()
Transform479.translation = [-0.05,-0.9,0]
Shape480 = x3d.Shape()
Shape480.USE = "HAnimJointShape"

Transform479.children.append(Shape480)

HAnimSegment478.children.append(Transform479)
Shape481 = x3d.Shape()
LineSet482 = x3d.LineSet()
LineSet482.vertexCount = [2]
Coordinate483 = x3d.Coordinate()

LineSet482.coord = Coordinate483
""" from r_metatarsophalangeal_2 to r_tarsal_proximal_interphalangeal_2 """
ColorRGBA484 = x3d.ColorRGBA()
ColorRGBA484.USE = "HAnimSegmentLineColorRGBA"

LineSet482.color = ColorRGBA484

Shape481.geometry = LineSet482

HAnimSegment478.children.append(Shape481)

HAnimJoint477.children.append(HAnimSegment478)
HAnimJoint485 = x3d.HAnimJoint()
HAnimJoint485.DEF = "hanim_r_tarsal_proximal_interphalangeal_2"
HAnimJoint485.name = "r_tarsal_proximal_interphalangeal_2"
HAnimJoint485.center = [-0.05,-1.05,0]
HAnimSegment486 = x3d.HAnimSegment()
HAnimSegment486.DEF = "hanim_r_tarsal_middle_phalanx_2"
HAnimSegment486.name = "r_tarsal_middle_phalanx_2"
Transform487 = x3d.Transform()
Transform487.translation = [-0.05,-1.05,0]
Shape488 = x3d.Shape()
Shape488.USE = "HAnimJointShape"

Transform487.children.append(Shape488)

HAnimSegment486.children.append(Transform487)
Shape489 = x3d.Shape()
LineSet490 = x3d.LineSet()
LineSet490.vertexCount = [2]
Coordinate491 = x3d.Coordinate()

LineSet490.coord = Coordinate491
""" from r_tarsal_proximal_interphalangeal_2 to r_tarsal_distal_interphalangeal_2 """
ColorRGBA492 = x3d.ColorRGBA()
ColorRGBA492.USE = "HAnimSegmentLineColorRGBA"

LineSet490.color = ColorRGBA492

Shape489.geometry = LineSet490

HAnimSegment486.children.append(Shape489)
HAnimSite493 = x3d.HAnimSite()
HAnimSite493.DEF = "hanim_r_tarsal_distal_phalanx_2_tip"
HAnimSite493.name = "r_tarsal_distal_phalanx_2_tip"
HAnimSite493.translation = [-0.05,-1.12,0]
TouchSensor494 = x3d.TouchSensor()
TouchSensor494.description = "HAnimSite r_tarsal_distal_phalanx_2_tip"

HAnimSite493.children.append(TouchSensor494)
Shape495 = x3d.Shape()
Shape495.USE = "HAnimSiteShape"

HAnimSite493.children.append(Shape495)

HAnimSegment486.children.append(HAnimSite493)

HAnimJoint485.children.append(HAnimSegment486)
HAnimJoint496 = x3d.HAnimJoint()
HAnimJoint496.DEF = "hanim_r_tarsal_distal_interphalangeal_2"
HAnimJoint496.name = "r_tarsal_distal_interphalangeal_2"
HAnimJoint496.center = [-0.05,-1.12,0]

HAnimJoint485.children.append(HAnimJoint496)

HAnimJoint477.children.append(HAnimJoint485)

HAnimJoint469.children.append(HAnimJoint477)

HAnimJoint461.children.append(HAnimJoint469)

HAnimJoint414.children.append(HAnimJoint461)
HAnimJoint497 = x3d.HAnimJoint()
HAnimJoint497.DEF = "hanim_r_cuneonavicular_3"
HAnimJoint497.name = "r_cuneonavicular_3"
HAnimJoint497.center = [-0.1,-0.4,0]
HAnimSegment498 = x3d.HAnimSegment()
HAnimSegment498.DEF = "hanim_r_cuneiform_3"
HAnimSegment498.name = "r_cuneiform_3"
Transform499 = x3d.Transform()
Transform499.translation = [-0.1,-0.4,0]
Shape500 = x3d.Shape()
Shape500.USE = "HAnimJointShape"

Transform499.children.append(Shape500)

HAnimSegment498.children.append(Transform499)
Shape501 = x3d.Shape()
LineSet502 = x3d.LineSet()
LineSet502.vertexCount = [2]
Coordinate503 = x3d.Coordinate()

LineSet502.coord = Coordinate503
""" from r_cuneonavicular_3 to r_tarsometatarsal_3 """
ColorRGBA504 = x3d.ColorRGBA()
ColorRGBA504.USE = "HAnimSegmentLineColorRGBA"

LineSet502.color = ColorRGBA504

Shape501.geometry = LineSet502

HAnimSegment498.children.append(Shape501)

HAnimJoint497.children.append(HAnimSegment498)
HAnimJoint505 = x3d.HAnimJoint()
HAnimJoint505.DEF = "hanim_r_tarsometatarsal_3"
HAnimJoint505.name = "r_tarsometatarsal_3"
HAnimJoint505.center = [-0.15,-0.6,0]
HAnimSegment506 = x3d.HAnimSegment()
HAnimSegment506.DEF = "hanim_r_metatarsal_3"
HAnimSegment506.name = "r_metatarsal_3"
Transform507 = x3d.Transform()
Transform507.translation = [-0.15,-0.6,0]
Shape508 = x3d.Shape()
Shape508.USE = "HAnimJointShape"

Transform507.children.append(Shape508)

HAnimSegment506.children.append(Transform507)
Shape509 = x3d.Shape()
LineSet510 = x3d.LineSet()
LineSet510.vertexCount = [2]
Coordinate511 = x3d.Coordinate()

LineSet510.coord = Coordinate511
""" from r_tarsometatarsal_3 to r_metatarsophalangeal_3 """
ColorRGBA512 = x3d.ColorRGBA()
ColorRGBA512.USE = "HAnimSegmentLineColorRGBA"

LineSet510.color = ColorRGBA512

Shape509.geometry = LineSet510

HAnimSegment506.children.append(Shape509)

HAnimJoint505.children.append(HAnimSegment506)
HAnimJoint513 = x3d.HAnimJoint()
HAnimJoint513.DEF = "hanim_r_metatarsophalangeal_3"
HAnimJoint513.name = "r_metatarsophalangeal_3"
HAnimJoint513.center = [-0.15,-0.9,0]
HAnimSegment514 = x3d.HAnimSegment()
HAnimSegment514.DEF = "hanim_r_tarsal_proximal_phalanx_3"
HAnimSegment514.name = "r_tarsal_proximal_phalanx_3"
Transform515 = x3d.Transform()
Transform515.translation = [-0.15,-0.9,0]
Shape516 = x3d.Shape()
Shape516.USE = "HAnimJointShape"

Transform515.children.append(Shape516)

HAnimSegment514.children.append(Transform515)
Shape517 = x3d.Shape()
LineSet518 = x3d.LineSet()
LineSet518.vertexCount = [2]
Coordinate519 = x3d.Coordinate()

LineSet518.coord = Coordinate519
""" from r_metatarsophalangeal_3 to r_tarsal_proximal_interphalangeal_3 """
ColorRGBA520 = x3d.ColorRGBA()
ColorRGBA520.USE = "HAnimSegmentLineColorRGBA"

LineSet518.color = ColorRGBA520

Shape517.geometry = LineSet518

HAnimSegment514.children.append(Shape517)

HAnimJoint513.children.append(HAnimSegment514)
HAnimJoint521 = x3d.HAnimJoint()
HAnimJoint521.DEF = "hanim_r_tarsal_proximal_interphalangeal_3"
HAnimJoint521.name = "r_tarsal_proximal_interphalangeal_3"
HAnimJoint521.center = [-0.15,-1.05,0]
HAnimSegment522 = x3d.HAnimSegment()
HAnimSegment522.DEF = "hanim_r_tarsal_middle_phalanx_3"
HAnimSegment522.name = "r_tarsal_middle_phalanx_3"
Transform523 = x3d.Transform()
Transform523.translation = [-0.15,-1.05,0]
Shape524 = x3d.Shape()
Shape524.USE = "HAnimJointShape"

Transform523.children.append(Shape524)

HAnimSegment522.children.append(Transform523)
Shape525 = x3d.Shape()
LineSet526 = x3d.LineSet()
LineSet526.vertexCount = [2]
Coordinate527 = x3d.Coordinate()

LineSet526.coord = Coordinate527
""" from r_tarsal_proximal_interphalangeal_3 to r_tarsal_distal_interphalangeal_3 """
ColorRGBA528 = x3d.ColorRGBA()
ColorRGBA528.USE = "HAnimSegmentLineColorRGBA"

LineSet526.color = ColorRGBA528

Shape525.geometry = LineSet526

HAnimSegment522.children.append(Shape525)
HAnimSite529 = x3d.HAnimSite()
HAnimSite529.DEF = "hanim_r_tarsal_distal_phalanx_3_tip"
HAnimSite529.name = "r_tarsal_distal_phalanx_3_tip"
HAnimSite529.translation = [-0.15,-1.13,0]
TouchSensor530 = x3d.TouchSensor()
TouchSensor530.description = "HAnimSite r_tarsal_distal_phalanx_3_tip"

HAnimSite529.children.append(TouchSensor530)
Shape531 = x3d.Shape()
Shape531.USE = "HAnimSiteShape"

HAnimSite529.children.append(Shape531)

HAnimSegment522.children.append(HAnimSite529)

HAnimJoint521.children.append(HAnimSegment522)
HAnimJoint532 = x3d.HAnimJoint()
HAnimJoint532.DEF = "hanim_r_tarsal_distal_interphalangeal_3"
HAnimJoint532.name = "r_tarsal_distal_interphalangeal_3"
HAnimJoint532.center = [-0.15,-1.13,0]

HAnimJoint521.children.append(HAnimJoint532)

HAnimJoint513.children.append(HAnimJoint521)

HAnimJoint505.children.append(HAnimJoint513)

HAnimJoint497.children.append(HAnimJoint505)

HAnimJoint414.children.append(HAnimJoint497)

HAnimJoint402.children.append(HAnimJoint414)
HAnimJoint533 = x3d.HAnimJoint()
HAnimJoint533.DEF = "hanim_r_calcaneocuboid"
HAnimJoint533.name = "r_calcaneocuboid"
HAnimJoint533.center = [-0.2,0.3,0]
HAnimSegment534 = x3d.HAnimSegment()
HAnimSegment534.DEF = "hanim_r_calcaneus"
HAnimSegment534.name = "r_calcaneus"
Transform535 = x3d.Transform()
Transform535.translation = [-0.2,0.3,0]
Shape536 = x3d.Shape()
Shape536.USE = "HAnimJointShape"

Transform535.children.append(Shape536)

HAnimSegment534.children.append(Transform535)
Shape537 = x3d.Shape()
LineSet538 = x3d.LineSet()
LineSet538.vertexCount = [2]
Coordinate539 = x3d.Coordinate()

LineSet538.coord = Coordinate539
""" from r_calcaneocuboid to r_transversetarsal """
ColorRGBA540 = x3d.ColorRGBA()
ColorRGBA540.USE = "HAnimSegmentLineColorRGBA"

LineSet538.color = ColorRGBA540

Shape537.geometry = LineSet538

HAnimSegment534.children.append(Shape537)

HAnimJoint533.children.append(HAnimSegment534)
HAnimJoint541 = x3d.HAnimJoint()
HAnimJoint541.DEF = "hanim_r_transversetarsal"
HAnimJoint541.name = "r_transversetarsal"
HAnimJoint541.center = [-0.21,-0.3,0]
HAnimSegment542 = x3d.HAnimSegment()
HAnimSegment542.DEF = "hanim_r_cuboid"
HAnimSegment542.name = "r_cuboid"
Transform543 = x3d.Transform()
Transform543.translation = [-0.21,-0.3,0]
Shape544 = x3d.Shape()
Shape544.USE = "HAnimJointShape"

Transform543.children.append(Shape544)

HAnimSegment542.children.append(Transform543)
Shape545 = x3d.Shape()
LineSet546 = x3d.LineSet()
LineSet546.vertexCount = [2]
Coordinate547 = x3d.Coordinate()

LineSet546.coord = Coordinate547
""" from r_transversetarsal to r_tarsometatarsal_4 """
ColorRGBA548 = x3d.ColorRGBA()
ColorRGBA548.USE = "HAnimSegmentLineColorRGBA"

LineSet546.color = ColorRGBA548

Shape545.geometry = LineSet546

HAnimSegment542.children.append(Shape545)
Shape549 = x3d.Shape()
LineSet550 = x3d.LineSet()
LineSet550.vertexCount = [2]
Coordinate551 = x3d.Coordinate()

LineSet550.coord = Coordinate551
""" from r_transversetarsal to r_tarsometatarsal_5 """
ColorRGBA552 = x3d.ColorRGBA()
ColorRGBA552.USE = "HAnimSegmentLineColorRGBA"

LineSet550.color = ColorRGBA552

Shape549.geometry = LineSet550

HAnimSegment542.children.append(Shape549)

HAnimJoint541.children.append(HAnimSegment542)
HAnimJoint553 = x3d.HAnimJoint()
HAnimJoint553.DEF = "hanim_r_tarsometatarsal_4"
HAnimJoint553.name = "r_tarsometatarsal_4"
HAnimJoint553.center = [-0.25,-0.58,0]
HAnimSegment554 = x3d.HAnimSegment()
HAnimSegment554.DEF = "hanim_r_metatarsal_4"
HAnimSegment554.name = "r_metatarsal_4"
Transform555 = x3d.Transform()
Transform555.translation = [-0.25,-0.58,0]
Shape556 = x3d.Shape()
Shape556.USE = "HAnimJointShape"

Transform555.children.append(Shape556)

HAnimSegment554.children.append(Transform555)
Shape557 = x3d.Shape()
LineSet558 = x3d.LineSet()
LineSet558.vertexCount = [2]
Coordinate559 = x3d.Coordinate()

LineSet558.coord = Coordinate559
""" from r_tarsometatarsal_4 to r_metatarsophalangeal_4 """
ColorRGBA560 = x3d.ColorRGBA()
ColorRGBA560.USE = "HAnimSegmentLineColorRGBA"

LineSet558.color = ColorRGBA560

Shape557.geometry = LineSet558

HAnimSegment554.children.append(Shape557)

HAnimJoint553.children.append(HAnimSegment554)
HAnimJoint561 = x3d.HAnimJoint()
HAnimJoint561.DEF = "hanim_r_metatarsophalangeal_4"
HAnimJoint561.name = "r_metatarsophalangeal_4"
HAnimJoint561.center = [-0.25,-0.87,0]
HAnimSegment562 = x3d.HAnimSegment()
HAnimSegment562.DEF = "hanim_r_tarsal_proximal_phalanx_4"
HAnimSegment562.name = "r_tarsal_proximal_phalanx_4"
Transform563 = x3d.Transform()
Transform563.translation = [-0.25,-0.87,0]
Shape564 = x3d.Shape()
Shape564.USE = "HAnimJointShape"

Transform563.children.append(Shape564)

HAnimSegment562.children.append(Transform563)
Shape565 = x3d.Shape()
LineSet566 = x3d.LineSet()
LineSet566.vertexCount = [2]
Coordinate567 = x3d.Coordinate()

LineSet566.coord = Coordinate567
""" from r_metatarsophalangeal_4 to r_tarsal_proximal_interphalangeal_4 """
ColorRGBA568 = x3d.ColorRGBA()
ColorRGBA568.USE = "HAnimSegmentLineColorRGBA"

LineSet566.color = ColorRGBA568

Shape565.geometry = LineSet566

HAnimSegment562.children.append(Shape565)

HAnimJoint561.children.append(HAnimSegment562)
HAnimJoint569 = x3d.HAnimJoint()
HAnimJoint569.DEF = "hanim_r_tarsal_proximal_interphalangeal_4"
HAnimJoint569.name = "r_tarsal_proximal_interphalangeal_4"
HAnimJoint569.center = [-0.25,-1.0,0]
HAnimSegment570 = x3d.HAnimSegment()
HAnimSegment570.DEF = "hanim_r_tarsal_middle_phalanx_4"
HAnimSegment570.name = "r_tarsal_middle_phalanx_4"
Transform571 = x3d.Transform()
Transform571.translation = [-0.25,-1.0,0]
Shape572 = x3d.Shape()
Shape572.USE = "HAnimJointShape"

Transform571.children.append(Shape572)

HAnimSegment570.children.append(Transform571)
Shape573 = x3d.Shape()
LineSet574 = x3d.LineSet()
LineSet574.vertexCount = [2]
Coordinate575 = x3d.Coordinate()

LineSet574.coord = Coordinate575
""" from r_tarsal_proximal_interphalangeal_4 to r_tarsal_distal_interphalangeal_4 """
ColorRGBA576 = x3d.ColorRGBA()
ColorRGBA576.USE = "HAnimSegmentLineColorRGBA"

LineSet574.color = ColorRGBA576

Shape573.geometry = LineSet574

HAnimSegment570.children.append(Shape573)
HAnimSite577 = x3d.HAnimSite()
HAnimSite577.DEF = "hanim_r_tarsal_distal_phalanx_4_tip"
HAnimSite577.name = "r_tarsal_distal_phalanx_4_tip"
HAnimSite577.translation = [-0.25,-1.1,0]
TouchSensor578 = x3d.TouchSensor()
TouchSensor578.description = "HAnimSite r_tarsal_distal_phalanx_4_tip"

HAnimSite577.children.append(TouchSensor578)
Shape579 = x3d.Shape()
Shape579.USE = "HAnimSiteShape"

HAnimSite577.children.append(Shape579)

HAnimSegment570.children.append(HAnimSite577)

HAnimJoint569.children.append(HAnimSegment570)
HAnimJoint580 = x3d.HAnimJoint()
HAnimJoint580.DEF = "hanim_r_tarsal_distal_interphalangeal_4"
HAnimJoint580.name = "r_tarsal_distal_interphalangeal_4"
HAnimJoint580.center = [-0.25,-1.1,0]

HAnimJoint569.children.append(HAnimJoint580)

HAnimJoint561.children.append(HAnimJoint569)

HAnimJoint553.children.append(HAnimJoint561)

HAnimJoint541.children.append(HAnimJoint553)
HAnimJoint581 = x3d.HAnimJoint()
HAnimJoint581.DEF = "hanim_r_tarsometatarsal_5"
HAnimJoint581.name = "r_tarsometatarsal_5"
HAnimJoint581.center = [-0.33,-0.52,0]
HAnimSegment582 = x3d.HAnimSegment()
HAnimSegment582.DEF = "hanim_r_metatarsal_5"
HAnimSegment582.name = "r_metatarsal_5"
Transform583 = x3d.Transform()
Transform583.translation = [-0.33,-0.52,0]
Shape584 = x3d.Shape()
Shape584.USE = "HAnimJointShape"

Transform583.children.append(Shape584)

HAnimSegment582.children.append(Transform583)
Shape585 = x3d.Shape()
LineSet586 = x3d.LineSet()
LineSet586.vertexCount = [2]
Coordinate587 = x3d.Coordinate()

LineSet586.coord = Coordinate587
""" from r_tarsometatarsal_5 to r_metatarsophalangeal_5 """
ColorRGBA588 = x3d.ColorRGBA()
ColorRGBA588.USE = "HAnimSegmentLineColorRGBA"

LineSet586.color = ColorRGBA588

Shape585.geometry = LineSet586

HAnimSegment582.children.append(Shape585)
HAnimSite589 = x3d.HAnimSite()
HAnimSite589.DEF = "hanim_r_metatarsal_phalanx_5_pt"
HAnimSite589.name = "r_metatarsal_phalanx_5_pt"
HAnimSite589.translation = [0,1,0]
TouchSensor590 = x3d.TouchSensor()
TouchSensor590.description = "HAnimSite r_metatarsal_phalanx_5_pt"

HAnimSite589.children.append(TouchSensor590)
Shape591 = x3d.Shape()
Shape591.USE = "HAnimSiteShape"

HAnimSite589.children.append(Shape591)

HAnimSegment582.children.append(HAnimSite589)

HAnimJoint581.children.append(HAnimSegment582)
HAnimJoint592 = x3d.HAnimJoint()
HAnimJoint592.DEF = "hanim_r_metatarsophalangeal_5"
HAnimJoint592.name = "r_metatarsophalangeal_5"
HAnimJoint592.center = [-0.34,-0.8,0]
HAnimSegment593 = x3d.HAnimSegment()
HAnimSegment593.DEF = "hanim_r_tarsal_proximal_phalanx_5"
HAnimSegment593.name = "r_tarsal_proximal_phalanx_5"
Transform594 = x3d.Transform()
Transform594.translation = [-0.34,-0.8,0]
Shape595 = x3d.Shape()
Shape595.USE = "HAnimJointShape"

Transform594.children.append(Shape595)

HAnimSegment593.children.append(Transform594)
Shape596 = x3d.Shape()
LineSet597 = x3d.LineSet()
LineSet597.vertexCount = [2]
Coordinate598 = x3d.Coordinate()

LineSet597.coord = Coordinate598
""" from r_metatarsophalangeal_5 to r_tarsal_proximal_interphalangeal_5 """
ColorRGBA599 = x3d.ColorRGBA()
ColorRGBA599.USE = "HAnimSegmentLineColorRGBA"

LineSet597.color = ColorRGBA599

Shape596.geometry = LineSet597

HAnimSegment593.children.append(Shape596)

HAnimJoint592.children.append(HAnimSegment593)
HAnimJoint600 = x3d.HAnimJoint()
HAnimJoint600.DEF = "hanim_r_tarsal_proximal_interphalangeal_5"
HAnimJoint600.name = "r_tarsal_proximal_interphalangeal_5"
HAnimJoint600.center = [-0.34,-0.95,0]
HAnimSegment601 = x3d.HAnimSegment()
HAnimSegment601.DEF = "hanim_r_tarsal_middle_phalanx_5"
HAnimSegment601.name = "r_tarsal_middle_phalanx_5"
Transform602 = x3d.Transform()
Transform602.translation = [-0.34,-0.95,0]
Shape603 = x3d.Shape()
Shape603.USE = "HAnimJointShape"

Transform602.children.append(Shape603)

HAnimSegment601.children.append(Transform602)
Shape604 = x3d.Shape()
LineSet605 = x3d.LineSet()
LineSet605.vertexCount = [2]
Coordinate606 = x3d.Coordinate()

LineSet605.coord = Coordinate606
""" from r_tarsal_proximal_interphalangeal_5 to r_tarsal_distal_interphalangeal_5 """
ColorRGBA607 = x3d.ColorRGBA()
ColorRGBA607.USE = "HAnimSegmentLineColorRGBA"

LineSet605.color = ColorRGBA607

Shape604.geometry = LineSet605

HAnimSegment601.children.append(Shape604)
HAnimSite608 = x3d.HAnimSite()
HAnimSite608.DEF = "hanim_r_tarsal_distal_phalanx_5_tip"
HAnimSite608.name = "r_tarsal_distal_phalanx_5_tip"
HAnimSite608.translation = [-0.34,-1.05,0]
TouchSensor609 = x3d.TouchSensor()
TouchSensor609.description = "HAnimSite r_tarsal_distal_phalanx_5_tip"

HAnimSite608.children.append(TouchSensor609)
Shape610 = x3d.Shape()
Shape610.USE = "HAnimSiteShape"

HAnimSite608.children.append(Shape610)

HAnimSegment601.children.append(HAnimSite608)

HAnimJoint600.children.append(HAnimSegment601)
HAnimJoint611 = x3d.HAnimJoint()
HAnimJoint611.DEF = "hanim_r_tarsal_distal_interphalangeal_5"
HAnimJoint611.name = "r_tarsal_distal_interphalangeal_5"
HAnimJoint611.center = [-0.34,-1.05,0]

HAnimJoint600.children.append(HAnimJoint611)

HAnimJoint592.children.append(HAnimJoint600)

HAnimJoint581.children.append(HAnimJoint592)

HAnimJoint541.children.append(HAnimJoint581)

HAnimJoint533.children.append(HAnimJoint541)

HAnimJoint402.children.append(HAnimJoint533)

HAnimJoint388.children.append(HAnimJoint402)

HAnimJoint371.children.append(HAnimJoint388)

HAnimJoint94.children.append(HAnimJoint371)

HAnimJoint43.children.append(HAnimJoint94)
HAnimJoint612 = x3d.HAnimJoint()
HAnimJoint612.DEF = "hanim_vl5"
HAnimJoint612.name = "vl5"
HAnimJoint612.center = [0.0028,1.0568,-0.0776]
HAnimSegment613 = x3d.HAnimSegment()
HAnimSegment613.DEF = "hanim_l5"
HAnimSegment613.name = "l5"
Transform614 = x3d.Transform()
Transform614.translation = [0.0028,1.0568,-0.0776]
Shape615 = x3d.Shape()
Shape615.USE = "HAnimJointShape"

Transform614.children.append(Shape615)

HAnimSegment613.children.append(Transform614)
Shape616 = x3d.Shape()
LineSet617 = x3d.LineSet()
LineSet617.vertexCount = [2]
Coordinate618 = x3d.Coordinate()

LineSet617.coord = Coordinate618
""" from vl5 to vl4 """
ColorRGBA619 = x3d.ColorRGBA()
ColorRGBA619.USE = "HAnimSegmentLineColorRGBA"

LineSet617.color = ColorRGBA619

Shape616.geometry = LineSet617

HAnimSegment613.children.append(Shape616)

HAnimJoint612.children.append(HAnimSegment613)
HAnimJoint620 = x3d.HAnimJoint()
HAnimJoint620.DEF = "hanim_vl4"
HAnimJoint620.name = "vl4"
HAnimJoint620.center = [0.0035,1.0925,-0.0787]
HAnimSegment621 = x3d.HAnimSegment()
HAnimSegment621.DEF = "hanim_l4"
HAnimSegment621.name = "l4"
Transform622 = x3d.Transform()
Transform622.translation = [0.0035,1.0925,-0.0787]
Shape623 = x3d.Shape()
Shape623.USE = "HAnimJointShape"

Transform622.children.append(Shape623)

HAnimSegment621.children.append(Transform622)
Shape624 = x3d.Shape()
LineSet625 = x3d.LineSet()
LineSet625.vertexCount = [2]
Coordinate626 = x3d.Coordinate()

LineSet625.coord = Coordinate626
""" from vl4 to vl3 """
ColorRGBA627 = x3d.ColorRGBA()
ColorRGBA627.USE = "HAnimSegmentLineColorRGBA"

LineSet625.color = ColorRGBA627

Shape624.geometry = LineSet625

HAnimSegment621.children.append(Shape624)

HAnimJoint620.children.append(HAnimSegment621)
HAnimJoint628 = x3d.HAnimJoint()
HAnimJoint628.DEF = "hanim_vl3"
HAnimJoint628.name = "vl3"
HAnimJoint628.center = [0.0041,1.1276,-0.0796]
HAnimSegment629 = x3d.HAnimSegment()
HAnimSegment629.DEF = "hanim_l3"
HAnimSegment629.name = "l3"
Transform630 = x3d.Transform()
Transform630.translation = [0.0041,1.1276,-0.0796]
Shape631 = x3d.Shape()
Shape631.USE = "HAnimJointShape"

Transform630.children.append(Shape631)

HAnimSegment629.children.append(Transform630)
Shape632 = x3d.Shape()
LineSet633 = x3d.LineSet()
LineSet633.vertexCount = [2]
Coordinate634 = x3d.Coordinate()

LineSet633.coord = Coordinate634
""" from vl3 to vl2 """
ColorRGBA635 = x3d.ColorRGBA()
ColorRGBA635.USE = "HAnimSegmentLineColorRGBA"

LineSet633.color = ColorRGBA635

Shape632.geometry = LineSet633

HAnimSegment629.children.append(Shape632)
HAnimSite636 = x3d.HAnimSite()
HAnimSite636.DEF = "hanim_l_rib10_pt"
HAnimSite636.name = "l_rib10_pt"
HAnimSite636.translation = [0.0871,1.1925,0.0992]
TouchSensor637 = x3d.TouchSensor()
TouchSensor637.description = "HAnimSite l_rib10_pt"

HAnimSite636.children.append(TouchSensor637)
Shape638 = x3d.Shape()
Shape638.USE = "HAnimSiteShape"

HAnimSite636.children.append(Shape638)

HAnimSegment629.children.append(HAnimSite636)
HAnimSite639 = x3d.HAnimSite()
HAnimSite639.DEF = "hanim_r_rib10_pt"
HAnimSite639.name = "r_rib10_pt"
HAnimSite639.translation = [-0.0711,1.1941,0.1016]
TouchSensor640 = x3d.TouchSensor()
TouchSensor640.description = "HAnimSite r_rib10_pt"

HAnimSite639.children.append(TouchSensor640)
Shape641 = x3d.Shape()
Shape641.USE = "HAnimSiteShape"

HAnimSite639.children.append(Shape641)

HAnimSegment629.children.append(HAnimSite639)
HAnimSite642 = x3d.HAnimSite()
HAnimSite642.DEF = "hanim_spine_2_middle_back_pt"
HAnimSite642.name = "spine_2_middle_back_pt"
HAnimSite642.translation = [0,1,0]
TouchSensor643 = x3d.TouchSensor()
TouchSensor643.description = "HAnimSite spine_2_middle_back_pt"

HAnimSite642.children.append(TouchSensor643)
Shape644 = x3d.Shape()
Shape644.USE = "HAnimSiteShape"

HAnimSite642.children.append(Shape644)

HAnimSegment629.children.append(HAnimSite642)

HAnimJoint628.children.append(HAnimSegment629)
HAnimJoint645 = x3d.HAnimJoint()
HAnimJoint645.DEF = "hanim_vl2"
HAnimJoint645.name = "vl2"
HAnimJoint645.center = [0.0045,1.1546,-0.0800]
HAnimSegment646 = x3d.HAnimSegment()
HAnimSegment646.DEF = "hanim_l2"
HAnimSegment646.name = "l2"
Transform647 = x3d.Transform()
Transform647.translation = [0.0045,1.1546,-0.0800]
Shape648 = x3d.Shape()
Shape648.USE = "HAnimJointShape"

Transform647.children.append(Shape648)

HAnimSegment646.children.append(Transform647)
Shape649 = x3d.Shape()
LineSet650 = x3d.LineSet()
LineSet650.vertexCount = [2]
Coordinate651 = x3d.Coordinate()

LineSet650.coord = Coordinate651
""" from vl2 to vl1 """
ColorRGBA652 = x3d.ColorRGBA()
ColorRGBA652.USE = "HAnimSegmentLineColorRGBA"

LineSet650.color = ColorRGBA652

Shape649.geometry = LineSet650

HAnimSegment646.children.append(Shape649)

HAnimJoint645.children.append(HAnimSegment646)
HAnimJoint653 = x3d.HAnimJoint()
HAnimJoint653.DEF = "hanim_vl1"
HAnimJoint653.name = "vl1"
HAnimJoint653.center = [0.0048,1.1912,-0.0805]
HAnimSegment654 = x3d.HAnimSegment()
HAnimSegment654.DEF = "hanim_l1"
HAnimSegment654.name = "l1"
Transform655 = x3d.Transform()
Transform655.translation = [0.0048,1.1912,-0.0805]
Shape656 = x3d.Shape()
Shape656.USE = "HAnimJointShape"

Transform655.children.append(Shape656)

HAnimSegment654.children.append(Transform655)
Shape657 = x3d.Shape()
LineSet658 = x3d.LineSet()
LineSet658.vertexCount = [2]
Coordinate659 = x3d.Coordinate()

LineSet658.coord = Coordinate659
""" from vl1 to vt12 """
ColorRGBA660 = x3d.ColorRGBA()
ColorRGBA660.USE = "HAnimSegmentLineColorRGBA"

LineSet658.color = ColorRGBA660

Shape657.geometry = LineSet658

HAnimSegment654.children.append(Shape657)

HAnimJoint653.children.append(HAnimSegment654)
HAnimJoint661 = x3d.HAnimJoint()
HAnimJoint661.DEF = "hanim_vt12"
HAnimJoint661.name = "vt12"
HAnimJoint661.center = [0.0051,1.2278,-0.0808]
HAnimSegment662 = x3d.HAnimSegment()
HAnimSegment662.DEF = "hanim_t12"
HAnimSegment662.name = "t12"
Transform663 = x3d.Transform()
Transform663.translation = [0.0051,1.2278,-0.0808]
Shape664 = x3d.Shape()
Shape664.USE = "HAnimJointShape"

Transform663.children.append(Shape664)

HAnimSegment662.children.append(Transform663)
Shape665 = x3d.Shape()
LineSet666 = x3d.LineSet()
LineSet666.vertexCount = [2]
Coordinate667 = x3d.Coordinate()

LineSet666.coord = Coordinate667
""" from vt12 to vt11 """
ColorRGBA668 = x3d.ColorRGBA()
ColorRGBA668.USE = "HAnimSegmentLineColorRGBA"

LineSet666.color = ColorRGBA668

Shape665.geometry = LineSet666

HAnimSegment662.children.append(Shape665)

HAnimJoint661.children.append(HAnimSegment662)
HAnimJoint669 = x3d.HAnimJoint()
HAnimJoint669.DEF = "hanim_vt11"
HAnimJoint669.name = "vt11"
HAnimJoint669.center = [0.0053,1.2679,-0.0810]
HAnimSegment670 = x3d.HAnimSegment()
HAnimSegment670.DEF = "hanim_t11"
HAnimSegment670.name = "t11"
Transform671 = x3d.Transform()
Transform671.translation = [0.0053,1.2679,-0.0810]
Shape672 = x3d.Shape()
Shape672.USE = "HAnimJointShape"

Transform671.children.append(Shape672)

HAnimSegment670.children.append(Transform671)
Shape673 = x3d.Shape()
LineSet674 = x3d.LineSet()
LineSet674.vertexCount = [2]
Coordinate675 = x3d.Coordinate()

LineSet674.coord = Coordinate675
""" from vt11 to vt10 """
ColorRGBA676 = x3d.ColorRGBA()
ColorRGBA676.USE = "HAnimSegmentLineColorRGBA"

LineSet674.color = ColorRGBA676

Shape673.geometry = LineSet674

HAnimSegment670.children.append(Shape673)
HAnimSite677 = x3d.HAnimSite()
HAnimSite677.DEF = "hanim_substernale_pt"
HAnimSite677.name = "substernale_pt"
HAnimSite677.translation = [0.0085,1.2995,0.1147]
TouchSensor678 = x3d.TouchSensor()
TouchSensor678.description = "HAnimSite substernale_pt"

HAnimSite677.children.append(TouchSensor678)
Shape679 = x3d.Shape()
Shape679.USE = "HAnimSiteShape"

HAnimSite677.children.append(Shape679)

HAnimSegment670.children.append(HAnimSite677)

HAnimJoint669.children.append(HAnimSegment670)
HAnimJoint680 = x3d.HAnimJoint()
HAnimJoint680.DEF = "hanim_vt10"
HAnimJoint680.name = "vt10"
HAnimJoint680.center = [0.0056,1.2848,-0.0822]
HAnimSegment681 = x3d.HAnimSegment()
HAnimSegment681.DEF = "hanim_t10"
HAnimSegment681.name = "t10"
Transform682 = x3d.Transform()
Transform682.translation = [0.0056,1.2848,-0.0822]
Shape683 = x3d.Shape()
Shape683.USE = "HAnimJointShape"

Transform682.children.append(Shape683)

HAnimSegment681.children.append(Transform682)
Shape684 = x3d.Shape()
LineSet685 = x3d.LineSet()
LineSet685.vertexCount = [2]
Coordinate686 = x3d.Coordinate()

LineSet685.coord = Coordinate686
""" from vt10 to vt9 """
ColorRGBA687 = x3d.ColorRGBA()
ColorRGBA687.USE = "HAnimSegmentLineColorRGBA"

LineSet685.color = ColorRGBA687

Shape684.geometry = LineSet685

HAnimSegment681.children.append(Shape684)
HAnimSite688 = x3d.HAnimSite()
HAnimSite688.DEF = "hanim_l_thelion_pt"
HAnimSite688.name = "l_thelion_pt"
HAnimSite688.translation = [0.0918,1.3382,0.1192]
TouchSensor689 = x3d.TouchSensor()
TouchSensor689.description = "HAnimSite l_thelion_pt"

HAnimSite688.children.append(TouchSensor689)
Shape690 = x3d.Shape()
Shape690.USE = "HAnimSiteShape"

HAnimSite688.children.append(Shape690)

HAnimSegment681.children.append(HAnimSite688)
HAnimSite691 = x3d.HAnimSite()
HAnimSite691.DEF = "hanim_r_thelion_pt"
HAnimSite691.name = "r_thelion_pt"
HAnimSite691.translation = [-0.0736,1.3385,0.1217]
TouchSensor692 = x3d.TouchSensor()
TouchSensor692.description = "HAnimSite r_thelion_pt"

HAnimSite691.children.append(TouchSensor692)
Shape693 = x3d.Shape()
Shape693.USE = "HAnimSiteShape"

HAnimSite691.children.append(Shape693)

HAnimSegment681.children.append(HAnimSite691)

HAnimJoint680.children.append(HAnimSegment681)
HAnimJoint694 = x3d.HAnimJoint()
HAnimJoint694.DEF = "hanim_vt9"
HAnimJoint694.name = "vt9"
HAnimJoint694.center = [0.0057,1.3126,-0.0838]
HAnimSegment695 = x3d.HAnimSegment()
HAnimSegment695.DEF = "hanim_t9"
HAnimSegment695.name = "t9"
Transform696 = x3d.Transform()
Transform696.translation = [0.0057,1.3126,-0.0838]
Shape697 = x3d.Shape()
Shape697.USE = "HAnimJointShape"

Transform696.children.append(Shape697)

HAnimSegment695.children.append(Transform696)
Shape698 = x3d.Shape()
LineSet699 = x3d.LineSet()
LineSet699.vertexCount = [2]
Coordinate700 = x3d.Coordinate()

LineSet699.coord = Coordinate700
""" from vt9 to vt8 """
ColorRGBA701 = x3d.ColorRGBA()
ColorRGBA701.USE = "HAnimSegmentLineColorRGBA"

LineSet699.color = ColorRGBA701

Shape698.geometry = LineSet699

HAnimSegment695.children.append(Shape698)

HAnimJoint694.children.append(HAnimSegment695)
HAnimJoint702 = x3d.HAnimJoint()
HAnimJoint702.DEF = "hanim_vt8"
HAnimJoint702.name = "vt8"
HAnimJoint702.center = [0.0057,1.3382,-0.0845]
HAnimSegment703 = x3d.HAnimSegment()
HAnimSegment703.DEF = "hanim_t8"
HAnimSegment703.name = "t8"
Transform704 = x3d.Transform()
Transform704.translation = [0.0057,1.3382,-0.0845]
Shape705 = x3d.Shape()
Shape705.USE = "HAnimJointShape"

Transform704.children.append(Shape705)

HAnimSegment703.children.append(Transform704)
Shape706 = x3d.Shape()
LineSet707 = x3d.LineSet()
LineSet707.vertexCount = [2]
Coordinate708 = x3d.Coordinate()

LineSet707.coord = Coordinate708
""" from vt8 to vt7 """
ColorRGBA709 = x3d.ColorRGBA()
ColorRGBA709.USE = "HAnimSegmentLineColorRGBA"

LineSet707.color = ColorRGBA709

Shape706.geometry = LineSet707

HAnimSegment703.children.append(Shape706)

HAnimJoint702.children.append(HAnimSegment703)
HAnimJoint710 = x3d.HAnimJoint()
HAnimJoint710.DEF = "hanim_vt7"
HAnimJoint710.name = "vt7"
HAnimJoint710.center = [0.0058,1.3625,-0.0833]
HAnimSegment711 = x3d.HAnimSegment()
HAnimSegment711.DEF = "hanim_t7"
HAnimSegment711.name = "t7"
Transform712 = x3d.Transform()
Transform712.translation = [0.0058,1.3625,-0.0833]
Shape713 = x3d.Shape()
Shape713.USE = "HAnimJointShape"

Transform712.children.append(Shape713)

HAnimSegment711.children.append(Transform712)
Shape714 = x3d.Shape()
LineSet715 = x3d.LineSet()
LineSet715.vertexCount = [2]
Coordinate716 = x3d.Coordinate()

LineSet715.coord = Coordinate716
""" from vt7 to vt6 """
ColorRGBA717 = x3d.ColorRGBA()
ColorRGBA717.USE = "HAnimSegmentLineColorRGBA"

LineSet715.color = ColorRGBA717

Shape714.geometry = LineSet715

HAnimSegment711.children.append(Shape714)
HAnimSite718 = x3d.HAnimSite()
HAnimSite718.DEF = "hanim_l_chest_midsagittal_plane_pt"
HAnimSite718.name = "l_chest_midsagittal_plane_pt"
HAnimSite718.translation = [0,1,0]
TouchSensor719 = x3d.TouchSensor()
TouchSensor719.description = "HAnimSite l_chest_midsagittal_plane_pt"

HAnimSite718.children.append(TouchSensor719)
Shape720 = x3d.Shape()
Shape720.USE = "HAnimSiteShape"

HAnimSite718.children.append(Shape720)

HAnimSegment711.children.append(HAnimSite718)
HAnimSite721 = x3d.HAnimSite()
HAnimSite721.DEF = "hanim_mesosternale_pt"
HAnimSite721.name = "mesosternale_pt"
HAnimSite721.translation = [0,1,0]
TouchSensor722 = x3d.TouchSensor()
TouchSensor722.description = "HAnimSite mesosternale_pt"

HAnimSite721.children.append(TouchSensor722)
Shape723 = x3d.Shape()
Shape723.USE = "HAnimSiteShape"

HAnimSite721.children.append(Shape723)

HAnimSegment711.children.append(HAnimSite721)
HAnimSite724 = x3d.HAnimSite()
HAnimSite724.DEF = "hanim_r_chest_midsagittal_plane_pt"
HAnimSite724.name = "r_chest_midsagittal_plane_pt"
HAnimSite724.translation = [0,1,0]
TouchSensor725 = x3d.TouchSensor()
TouchSensor725.description = "HAnimSite r_chest_midsagittal_plane_pt"

HAnimSite724.children.append(TouchSensor725)
Shape726 = x3d.Shape()
Shape726.USE = "HAnimSiteShape"

HAnimSite724.children.append(Shape726)

HAnimSegment711.children.append(HAnimSite724)
HAnimSite727 = x3d.HAnimSite()
HAnimSite727.DEF = "hanim_rear_center_midsagittal_plane_pt"
HAnimSite727.name = "rear_center_midsagittal_plane_pt"
HAnimSite727.translation = [0,1,0]
TouchSensor728 = x3d.TouchSensor()
TouchSensor728.description = "HAnimSite rear_center_midsagittal_plane_pt"

HAnimSite727.children.append(TouchSensor728)
Shape729 = x3d.Shape()
Shape729.USE = "HAnimSiteShape"

HAnimSite727.children.append(Shape729)

HAnimSegment711.children.append(HAnimSite727)

HAnimJoint710.children.append(HAnimSegment711)
HAnimJoint730 = x3d.HAnimJoint()
HAnimJoint730.DEF = "hanim_vt6"
HAnimJoint730.name = "vt6"
HAnimJoint730.center = [0.0059,1.3866,-0.0800]
HAnimSegment731 = x3d.HAnimSegment()
HAnimSegment731.DEF = "hanim_t6"
HAnimSegment731.name = "t6"
Transform732 = x3d.Transform()
Transform732.translation = [0.0059,1.3866,-0.0800]
Shape733 = x3d.Shape()
Shape733.USE = "HAnimJointShape"

Transform732.children.append(Shape733)

HAnimSegment731.children.append(Transform732)
Shape734 = x3d.Shape()
LineSet735 = x3d.LineSet()
LineSet735.vertexCount = [2]
Coordinate736 = x3d.Coordinate()

LineSet735.coord = Coordinate736
""" from vt6 to vt5 """
ColorRGBA737 = x3d.ColorRGBA()
ColorRGBA737.USE = "HAnimSegmentLineColorRGBA"

LineSet735.color = ColorRGBA737

Shape734.geometry = LineSet735

HAnimSegment731.children.append(Shape734)
HAnimSite738 = x3d.HAnimSite()
HAnimSite738.DEF = "hanim_spine_1_middle_back_pt"
HAnimSite738.name = "spine_1_middle_back_pt"
HAnimSite738.translation = [0,1,0]
TouchSensor739 = x3d.TouchSensor()
TouchSensor739.description = "HAnimSite spine_1_middle_back_pt"

HAnimSite738.children.append(TouchSensor739)
Shape740 = x3d.Shape()
Shape740.USE = "HAnimSiteShape"

HAnimSite738.children.append(Shape740)

HAnimSegment731.children.append(HAnimSite738)

HAnimJoint730.children.append(HAnimSegment731)
HAnimJoint741 = x3d.HAnimJoint()
HAnimJoint741.DEF = "hanim_vt5"
HAnimJoint741.name = "vt5"
HAnimJoint741.center = [0.0060,1.4102,-0.0745]
HAnimSegment742 = x3d.HAnimSegment()
HAnimSegment742.DEF = "hanim_t5"
HAnimSegment742.name = "t5"
Transform743 = x3d.Transform()
Transform743.translation = [0.0060,1.4102,-0.0745]
Shape744 = x3d.Shape()
Shape744.USE = "HAnimJointShape"

Transform743.children.append(Shape744)

HAnimSegment742.children.append(Transform743)
Shape745 = x3d.Shape()
LineSet746 = x3d.LineSet()
LineSet746.vertexCount = [2]
Coordinate747 = x3d.Coordinate()

LineSet746.coord = Coordinate747
""" from vt5 to vt4 """
ColorRGBA748 = x3d.ColorRGBA()
ColorRGBA748.USE = "HAnimSegmentLineColorRGBA"

LineSet746.color = ColorRGBA748

Shape745.geometry = LineSet746

HAnimSegment742.children.append(Shape745)

HAnimJoint741.children.append(HAnimSegment742)
HAnimJoint749 = x3d.HAnimJoint()
HAnimJoint749.DEF = "hanim_vt4"
HAnimJoint749.name = "vt4"
HAnimJoint749.center = [0.0061,1.4320,-0.0675]
HAnimSegment750 = x3d.HAnimSegment()
HAnimSegment750.DEF = "hanim_t4"
HAnimSegment750.name = "t4"
Transform751 = x3d.Transform()
Transform751.translation = [0.0061,1.4320,-0.0675]
Shape752 = x3d.Shape()
Shape752.USE = "HAnimJointShape"

Transform751.children.append(Shape752)

HAnimSegment750.children.append(Transform751)
Shape753 = x3d.Shape()
LineSet754 = x3d.LineSet()
LineSet754.vertexCount = [2]
Coordinate755 = x3d.Coordinate()

LineSet754.coord = Coordinate755
""" from vt4 to vt3 """
ColorRGBA756 = x3d.ColorRGBA()
ColorRGBA756.USE = "HAnimSegmentLineColorRGBA"

LineSet754.color = ColorRGBA756

Shape753.geometry = LineSet754

HAnimSegment750.children.append(Shape753)

HAnimJoint749.children.append(HAnimSegment750)
HAnimJoint757 = x3d.HAnimJoint()
HAnimJoint757.DEF = "hanim_vt3"
HAnimJoint757.name = "vt3"
HAnimJoint757.center = [0.0062,1.4583,-0.0570]
HAnimSegment758 = x3d.HAnimSegment()
HAnimSegment758.DEF = "hanim_t3"
HAnimSegment758.name = "t3"
Transform759 = x3d.Transform()
Transform759.translation = [0.0062,1.4583,-0.0570]
Shape760 = x3d.Shape()
Shape760.USE = "HAnimJointShape"

Transform759.children.append(Shape760)

HAnimSegment758.children.append(Transform759)
Shape761 = x3d.Shape()
LineSet762 = x3d.LineSet()
LineSet762.vertexCount = [2]
Coordinate763 = x3d.Coordinate()

LineSet762.coord = Coordinate763
""" from vt3 to vt2 """
ColorRGBA764 = x3d.ColorRGBA()
ColorRGBA764.USE = "HAnimSegmentLineColorRGBA"

LineSet762.color = ColorRGBA764

Shape761.geometry = LineSet762

HAnimSegment758.children.append(Shape761)

HAnimJoint757.children.append(HAnimSegment758)
HAnimJoint765 = x3d.HAnimJoint()
HAnimJoint765.DEF = "hanim_vt2"
HAnimJoint765.name = "vt2"
HAnimJoint765.center = [0.0063,1.4761,-0.0484]
HAnimSegment766 = x3d.HAnimSegment()
HAnimSegment766.DEF = "hanim_t2"
HAnimSegment766.name = "t2"
Transform767 = x3d.Transform()
Transform767.translation = [0.0063,1.4761,-0.0484]
Shape768 = x3d.Shape()
Shape768.USE = "HAnimJointShape"

Transform767.children.append(Shape768)

HAnimSegment766.children.append(Transform767)
Shape769 = x3d.Shape()
LineSet770 = x3d.LineSet()
LineSet770.vertexCount = [2]
Coordinate771 = x3d.Coordinate()

LineSet770.coord = Coordinate771
""" from vt2 to vt1 """
ColorRGBA772 = x3d.ColorRGBA()
ColorRGBA772.USE = "HAnimSegmentLineColorRGBA"

LineSet770.color = ColorRGBA772

Shape769.geometry = LineSet770

HAnimSegment766.children.append(Shape769)
HAnimSite773 = x3d.HAnimSite()
HAnimSite773.DEF = "hanim_cervicale_pt"
HAnimSite773.name = "cervicale_pt"
HAnimSite773.translation = [0.0064,1.520,-0.0815]
TouchSensor774 = x3d.TouchSensor()
TouchSensor774.description = "HAnimSite cervicale_pt"

HAnimSite773.children.append(TouchSensor774)
Shape775 = x3d.Shape()
Shape775.USE = "HAnimSiteShape"

HAnimSite773.children.append(Shape775)

HAnimSegment766.children.append(HAnimSite773)
HAnimSite776 = x3d.HAnimSite()
HAnimSite776.DEF = "hanim_suprasternale_pt"
HAnimSite776.name = "suprasternale_pt"
HAnimSite776.translation = [0.0084,1.4714,0.0551]
TouchSensor777 = x3d.TouchSensor()
TouchSensor777.description = "HAnimSite suprasternale_pt"

HAnimSite776.children.append(TouchSensor777)
Shape778 = x3d.Shape()
Shape778.USE = "HAnimSiteShape"

HAnimSite776.children.append(Shape778)

HAnimSegment766.children.append(HAnimSite776)

HAnimJoint765.children.append(HAnimSegment766)
HAnimJoint779 = x3d.HAnimJoint()
HAnimJoint779.DEF = "hanim_vt1"
HAnimJoint779.name = "vt1"
HAnimJoint779.center = [0.0065,1.4951,-0.0387]
HAnimSegment780 = x3d.HAnimSegment()
HAnimSegment780.DEF = "hanim_t1"
HAnimSegment780.name = "t1"
Transform781 = x3d.Transform()
Transform781.translation = [0.0065,1.4951,-0.0387]
Shape782 = x3d.Shape()
Shape782.USE = "HAnimJointShape"

Transform781.children.append(Shape782)

HAnimSegment780.children.append(Transform781)
Shape783 = x3d.Shape()
LineSet784 = x3d.LineSet()
LineSet784.vertexCount = [2]
Coordinate785 = x3d.Coordinate()

LineSet784.coord = Coordinate785
""" from vt1 to vc7 """
ColorRGBA786 = x3d.ColorRGBA()
ColorRGBA786.USE = "HAnimSegmentLineColorRGBA"

LineSet784.color = ColorRGBA786

Shape783.geometry = LineSet784

HAnimSegment780.children.append(Shape783)
HAnimSite787 = x3d.HAnimSite()
HAnimSite787.DEF = "hanim_l_neck_base_pt"
HAnimSite787.name = "l_neck_base_pt"
HAnimSite787.translation = [0.0646,1.5141,-0.0380]
TouchSensor788 = x3d.TouchSensor()
TouchSensor788.description = "HAnimSite l_neck_base_pt"

HAnimSite787.children.append(TouchSensor788)
Shape789 = x3d.Shape()
Shape789.USE = "HAnimSiteShape"

HAnimSite787.children.append(Shape789)

HAnimSegment780.children.append(HAnimSite787)
HAnimSite790 = x3d.HAnimSite()
HAnimSite790.DEF = "hanim_r_neck_base_pt"
HAnimSite790.name = "r_neck_base_pt"
HAnimSite790.translation = [-0.0419,1.5149,-0.0220]
TouchSensor791 = x3d.TouchSensor()
TouchSensor791.description = "HAnimSite r_neck_base_pt"

HAnimSite790.children.append(TouchSensor791)
Shape792 = x3d.Shape()
Shape792.USE = "HAnimSiteShape"

HAnimSite790.children.append(Shape792)

HAnimSegment780.children.append(HAnimSite790)
Shape793 = x3d.Shape()
LineSet794 = x3d.LineSet()
LineSet794.vertexCount = [2]
Coordinate795 = x3d.Coordinate()

LineSet794.coord = Coordinate795
""" from vt1 to l_sternoclavicular """
ColorRGBA796 = x3d.ColorRGBA()
ColorRGBA796.USE = "HAnimSegmentLineColorRGBA"

LineSet794.color = ColorRGBA796

Shape793.geometry = LineSet794

HAnimSegment780.children.append(Shape793)
HAnimSite797 = x3d.HAnimSite()
HAnimSite797.DEF = "hanim_l_acromion_pt"
HAnimSite797.name = "l_acromion_pt"
HAnimSite797.translation = [0.2032,1.4760,-0.0490]
TouchSensor798 = x3d.TouchSensor()
TouchSensor798.description = "HAnimSite l_acromion_pt"

HAnimSite797.children.append(TouchSensor798)
Shape799 = x3d.Shape()
Shape799.USE = "HAnimSiteShape"

HAnimSite797.children.append(Shape799)

HAnimSegment780.children.append(HAnimSite797)
HAnimSite800 = x3d.HAnimSite()
HAnimSite800.DEF = "hanim_l_axilla_distal_pt"
HAnimSite800.name = "l_axilla_distal_pt"
HAnimSite800.translation = [0.1706,1.4072,-0.0875]
TouchSensor801 = x3d.TouchSensor()
TouchSensor801.description = "HAnimSite l_axilla_distal_pt"

HAnimSite800.children.append(TouchSensor801)
Shape802 = x3d.Shape()
Shape802.USE = "HAnimSiteShape"

HAnimSite800.children.append(Shape802)

HAnimSegment780.children.append(HAnimSite800)
HAnimSite803 = x3d.HAnimSite()
HAnimSite803.DEF = "hanim_l_axilla_posterior_folds_pt"
HAnimSite803.name = "l_axilla_posterior_folds_pt"
HAnimSite803.translation = [0,1,0]
TouchSensor804 = x3d.TouchSensor()
TouchSensor804.description = "HAnimSite l_axilla_posterior_folds_pt"

HAnimSite803.children.append(TouchSensor804)
Shape805 = x3d.Shape()
Shape805.USE = "HAnimSiteShape"

HAnimSite803.children.append(Shape805)

HAnimSegment780.children.append(HAnimSite803)
HAnimSite806 = x3d.HAnimSite()
HAnimSite806.DEF = "hanim_l_axilla_proximal_pt"
HAnimSite806.name = "l_axilla_proximal_pt"
HAnimSite806.translation = [0.1777,1.4065,-0.0075]
TouchSensor807 = x3d.TouchSensor()
TouchSensor807.description = "HAnimSite l_axilla_proximal_pt"

HAnimSite806.children.append(TouchSensor807)
Shape808 = x3d.Shape()
Shape808.USE = "HAnimSiteShape"

HAnimSite806.children.append(Shape808)

HAnimSegment780.children.append(HAnimSite806)
HAnimSite809 = x3d.HAnimSite()
HAnimSite809.DEF = "hanim_l_clavicale_pt"
HAnimSite809.name = "l_clavicale_pt"
HAnimSite809.translation = [0.0271,1.4943,0.0394]
TouchSensor810 = x3d.TouchSensor()
TouchSensor810.description = "HAnimSite l_clavicale_pt"

HAnimSite809.children.append(TouchSensor810)
Shape811 = x3d.Shape()
Shape811.USE = "HAnimSiteShape"

HAnimSite809.children.append(Shape811)

HAnimSegment780.children.append(HAnimSite809)
Shape812 = x3d.Shape()
LineSet813 = x3d.LineSet()
LineSet813.vertexCount = [2]
Coordinate814 = x3d.Coordinate()

LineSet813.coord = Coordinate814
""" from vt1 to r_sternoclavicular """
ColorRGBA815 = x3d.ColorRGBA()
ColorRGBA815.USE = "HAnimSegmentLineColorRGBA"

LineSet813.color = ColorRGBA815

Shape812.geometry = LineSet813

HAnimSegment780.children.append(Shape812)
HAnimSite816 = x3d.HAnimSite()
HAnimSite816.DEF = "hanim_r_acromion_pt"
HAnimSite816.name = "r_acromion_pt"
HAnimSite816.translation = [-0.1905,1.4791,-0.0431]
TouchSensor817 = x3d.TouchSensor()
TouchSensor817.description = "HAnimSite r_acromion_pt"

HAnimSite816.children.append(TouchSensor817)
Shape818 = x3d.Shape()
Shape818.USE = "HAnimSiteShape"

HAnimSite816.children.append(Shape818)

HAnimSegment780.children.append(HAnimSite816)
HAnimSite819 = x3d.HAnimSite()
HAnimSite819.DEF = "hanim_r_axilla_distal_pt"
HAnimSite819.name = "r_axilla_distal_pt"
HAnimSite819.translation = [-0.1603,1.4098,-0.0826]
TouchSensor820 = x3d.TouchSensor()
TouchSensor820.description = "HAnimSite r_axilla_distal_pt"

HAnimSite819.children.append(TouchSensor820)
Shape821 = x3d.Shape()
Shape821.USE = "HAnimSiteShape"

HAnimSite819.children.append(Shape821)

HAnimSegment780.children.append(HAnimSite819)
HAnimSite822 = x3d.HAnimSite()
HAnimSite822.DEF = "hanim_r_axilla_posterior_folds_pt"
HAnimSite822.name = "r_axilla_posterior_folds_pt"
HAnimSite822.translation = [0,1,0]
TouchSensor823 = x3d.TouchSensor()
TouchSensor823.description = "HAnimSite r_axilla_posterior_folds_pt"

HAnimSite822.children.append(TouchSensor823)
Shape824 = x3d.Shape()
Shape824.USE = "HAnimSiteShape"

HAnimSite822.children.append(Shape824)

HAnimSegment780.children.append(HAnimSite822)
HAnimSite825 = x3d.HAnimSite()
HAnimSite825.DEF = "hanim_r_axilla_proximal_pt"
HAnimSite825.name = "r_axilla_proximal_pt"
HAnimSite825.translation = [-0.1626,1.4072,-0.0031]
TouchSensor826 = x3d.TouchSensor()
TouchSensor826.description = "HAnimSite r_axilla_proximal_pt"

HAnimSite825.children.append(TouchSensor826)
Shape827 = x3d.Shape()
Shape827.USE = "HAnimSiteShape"

HAnimSite825.children.append(Shape827)

HAnimSegment780.children.append(HAnimSite825)
HAnimSite828 = x3d.HAnimSite()
HAnimSite828.DEF = "hanim_r_clavicale_pt"
HAnimSite828.name = "r_clavicale_pt"
HAnimSite828.translation = [-0.0115,1.4943,0.0400]
TouchSensor829 = x3d.TouchSensor()
TouchSensor829.description = "HAnimSite r_clavicale_pt"

HAnimSite828.children.append(TouchSensor829)
Shape830 = x3d.Shape()
Shape830.USE = "HAnimSiteShape"

HAnimSite828.children.append(Shape830)

HAnimSegment780.children.append(HAnimSite828)

HAnimJoint779.children.append(HAnimSegment780)
HAnimJoint831 = x3d.HAnimJoint()
HAnimJoint831.DEF = "hanim_vc7"
HAnimJoint831.name = "vc7"
HAnimJoint831.center = [0.0066,1.5132,-0.0301]
HAnimSegment832 = x3d.HAnimSegment()
HAnimSegment832.DEF = "hanim_c7"
HAnimSegment832.name = "c7"
Transform833 = x3d.Transform()
Transform833.translation = [0.0066,1.5132,-0.0301]
Shape834 = x3d.Shape()
Shape834.USE = "HAnimJointShape"

Transform833.children.append(Shape834)

HAnimSegment832.children.append(Transform833)
Shape835 = x3d.Shape()
LineSet836 = x3d.LineSet()
LineSet836.vertexCount = [2]
Coordinate837 = x3d.Coordinate()

LineSet836.coord = Coordinate837
""" from vc7 to vc6 """
ColorRGBA838 = x3d.ColorRGBA()
ColorRGBA838.USE = "HAnimSegmentLineColorRGBA"

LineSet836.color = ColorRGBA838

Shape835.geometry = LineSet836

HAnimSegment832.children.append(Shape835)

HAnimJoint831.children.append(HAnimSegment832)
HAnimJoint839 = x3d.HAnimJoint()
HAnimJoint839.DEF = "hanim_vc6"
HAnimJoint839.name = "vc6"
HAnimJoint839.center = [0.0066,1.5357,-0.0143]
HAnimSegment840 = x3d.HAnimSegment()
HAnimSegment840.DEF = "hanim_c6"
HAnimSegment840.name = "c6"
Transform841 = x3d.Transform()
Transform841.translation = [0.0066,1.5357,-0.0143]
Shape842 = x3d.Shape()
Shape842.USE = "HAnimJointShape"

Transform841.children.append(Shape842)

HAnimSegment840.children.append(Transform841)
Shape843 = x3d.Shape()
LineSet844 = x3d.LineSet()
LineSet844.vertexCount = [2]
Coordinate845 = x3d.Coordinate()

LineSet844.coord = Coordinate845
""" from vc6 to vc5 """
ColorRGBA846 = x3d.ColorRGBA()
ColorRGBA846.USE = "HAnimSegmentLineColorRGBA"

LineSet844.color = ColorRGBA846

Shape843.geometry = LineSet844

HAnimSegment840.children.append(Shape843)

HAnimJoint839.children.append(HAnimSegment840)
HAnimJoint847 = x3d.HAnimJoint()
HAnimJoint847.DEF = "hanim_vc5"
HAnimJoint847.name = "vc5"
HAnimJoint847.center = [0.0066,1.5520,-0.0082]
HAnimSegment848 = x3d.HAnimSegment()
HAnimSegment848.DEF = "hanim_c5"
HAnimSegment848.name = "c5"
Transform849 = x3d.Transform()
Transform849.translation = [0.0066,1.5520,-0.0082]
Shape850 = x3d.Shape()
Shape850.USE = "HAnimJointShape"

Transform849.children.append(Shape850)

HAnimSegment848.children.append(Transform849)
Shape851 = x3d.Shape()
LineSet852 = x3d.LineSet()
LineSet852.vertexCount = [2]
Coordinate853 = x3d.Coordinate()

LineSet852.coord = Coordinate853
""" from vc5 to vc4 """
ColorRGBA854 = x3d.ColorRGBA()
ColorRGBA854.USE = "HAnimSegmentLineColorRGBA"

LineSet852.color = ColorRGBA854

Shape851.geometry = LineSet852

HAnimSegment848.children.append(Shape851)

HAnimJoint847.children.append(HAnimSegment848)
HAnimJoint855 = x3d.HAnimJoint()
HAnimJoint855.DEF = "hanim_vc4"
HAnimJoint855.name = "vc4"
HAnimJoint855.center = [0.0066,1.5662,-0.0084]
HAnimSegment856 = x3d.HAnimSegment()
HAnimSegment856.DEF = "hanim_c4"
HAnimSegment856.name = "c4"
Transform857 = x3d.Transform()
Transform857.translation = [0.0066,1.5662,-0.0084]
Shape858 = x3d.Shape()
Shape858.USE = "HAnimJointShape"

Transform857.children.append(Shape858)

HAnimSegment856.children.append(Transform857)
Shape859 = x3d.Shape()
LineSet860 = x3d.LineSet()
LineSet860.vertexCount = [2]
Coordinate861 = x3d.Coordinate()

LineSet860.coord = Coordinate861
""" from vc4 to vc3 """
ColorRGBA862 = x3d.ColorRGBA()
ColorRGBA862.USE = "HAnimSegmentLineColorRGBA"

LineSet860.color = ColorRGBA862

Shape859.geometry = LineSet860

HAnimSegment856.children.append(Shape859)

HAnimJoint855.children.append(HAnimSegment856)
HAnimJoint863 = x3d.HAnimJoint()
HAnimJoint863.DEF = "hanim_vc3"
HAnimJoint863.name = "vc3"
HAnimJoint863.center = [0.0066,1.5800,-0.0103]
HAnimSegment864 = x3d.HAnimSegment()
HAnimSegment864.DEF = "hanim_c3"
HAnimSegment864.name = "c3"
Transform865 = x3d.Transform()
Transform865.translation = [0.0066,1.5800,-0.0103]
Shape866 = x3d.Shape()
Shape866.USE = "HAnimJointShape"

Transform865.children.append(Shape866)

HAnimSegment864.children.append(Transform865)
Shape867 = x3d.Shape()
LineSet868 = x3d.LineSet()
LineSet868.vertexCount = [2]
Coordinate869 = x3d.Coordinate()

LineSet868.coord = Coordinate869
""" from vc3 to vc2 """
ColorRGBA870 = x3d.ColorRGBA()
ColorRGBA870.USE = "HAnimSegmentLineColorRGBA"

LineSet868.color = ColorRGBA870

Shape867.geometry = LineSet868

HAnimSegment864.children.append(Shape867)
HAnimSite871 = x3d.HAnimSite()
HAnimSite871.DEF = "hanim_adams_apple_pt"
HAnimSite871.name = "adams_apple_pt"
HAnimSite871.translation = [0,1,0]
TouchSensor872 = x3d.TouchSensor()
TouchSensor872.description = "HAnimSite adams_apple_pt"

HAnimSite871.children.append(TouchSensor872)
Shape873 = x3d.Shape()
Shape873.USE = "HAnimSiteShape"

HAnimSite871.children.append(Shape873)

HAnimSegment864.children.append(HAnimSite871)

HAnimJoint863.children.append(HAnimSegment864)
HAnimJoint874 = x3d.HAnimJoint()
HAnimJoint874.DEF = "hanim_vc2"
HAnimJoint874.name = "vc2"
HAnimJoint874.center = [0.0066,1.5928,-0.0103]
HAnimSegment875 = x3d.HAnimSegment()
HAnimSegment875.DEF = "hanim_c2"
HAnimSegment875.name = "c2"
Transform876 = x3d.Transform()
Transform876.translation = [0.0066,1.5928,-0.0103]
Shape877 = x3d.Shape()
Shape877.USE = "HAnimJointShape"

Transform876.children.append(Shape877)

HAnimSegment875.children.append(Transform876)
Shape878 = x3d.Shape()
LineSet879 = x3d.LineSet()
LineSet879.vertexCount = [2]
Coordinate880 = x3d.Coordinate()

LineSet879.coord = Coordinate880
""" from vc2 to vc1 """
ColorRGBA881 = x3d.ColorRGBA()
ColorRGBA881.USE = "HAnimSegmentLineColorRGBA"

LineSet879.color = ColorRGBA881

Shape878.geometry = LineSet879

HAnimSegment875.children.append(Shape878)

HAnimJoint874.children.append(HAnimSegment875)
HAnimJoint882 = x3d.HAnimJoint()
HAnimJoint882.DEF = "hanim_vc1"
HAnimJoint882.name = "vc1"
HAnimJoint882.center = [0.0066,1.6144,-0.0034]
HAnimSegment883 = x3d.HAnimSegment()
HAnimSegment883.DEF = "hanim_c1"
HAnimSegment883.name = "c1"
Transform884 = x3d.Transform()
Transform884.translation = [0.0066,1.6144,-0.0034]
Shape885 = x3d.Shape()
Shape885.USE = "HAnimJointShape"

Transform884.children.append(Shape885)

HAnimSegment883.children.append(Transform884)
Shape886 = x3d.Shape()
LineSet887 = x3d.LineSet()
LineSet887.vertexCount = [2]
Coordinate888 = x3d.Coordinate()

LineSet887.coord = Coordinate888
""" from vc1 to skullbase """
ColorRGBA889 = x3d.ColorRGBA()
ColorRGBA889.USE = "HAnimSegmentLineColorRGBA"

LineSet887.color = ColorRGBA889

Shape886.geometry = LineSet887

HAnimSegment883.children.append(Shape886)
HAnimSite890 = x3d.HAnimSite()
HAnimSite890.DEF = "hanim_glabella_pt"
HAnimSite890.name = "glabella_pt"
HAnimSite890.translation = [0,1,0]
TouchSensor891 = x3d.TouchSensor()
TouchSensor891.description = "HAnimSite glabella_pt"

HAnimSite890.children.append(TouchSensor891)
Shape892 = x3d.Shape()
Shape892.USE = "HAnimSiteShape"

HAnimSite890.children.append(Shape892)

HAnimSegment883.children.append(HAnimSite890)
HAnimSite893 = x3d.HAnimSite()
HAnimSite893.DEF = "hanim_l_ectocanthus_pt"
HAnimSite893.name = "l_ectocanthus_pt"
HAnimSite893.translation = [0,1,0]
TouchSensor894 = x3d.TouchSensor()
TouchSensor894.description = "HAnimSite l_ectocanthus_pt"

HAnimSite893.children.append(TouchSensor894)
Shape895 = x3d.Shape()
Shape895.USE = "HAnimSiteShape"

HAnimSite893.children.append(Shape895)

HAnimSegment883.children.append(HAnimSite893)
HAnimSite896 = x3d.HAnimSite()
HAnimSite896.DEF = "hanim_l_infraorbitale_pt"
HAnimSite896.name = "l_infraorbitale_pt"
HAnimSite896.translation = [0.0341,1.6171,0.0752]
TouchSensor897 = x3d.TouchSensor()
TouchSensor897.description = "HAnimSite l_infraorbitale_pt"

HAnimSite896.children.append(TouchSensor897)
Shape898 = x3d.Shape()
Shape898.USE = "HAnimSiteShape"

HAnimSite896.children.append(Shape898)

HAnimSegment883.children.append(HAnimSite896)
HAnimSite899 = x3d.HAnimSite()
HAnimSite899.DEF = "hanim_l_tragion_pt"
HAnimSite899.name = "l_tragion_pt"
HAnimSite899.translation = [0.0739,1.6348,0.0282]
TouchSensor900 = x3d.TouchSensor()
TouchSensor900.description = "HAnimSite l_tragion_pt"

HAnimSite899.children.append(TouchSensor900)
Shape901 = x3d.Shape()
Shape901.USE = "HAnimSiteShape"

HAnimSite899.children.append(Shape901)

HAnimSegment883.children.append(HAnimSite899)
HAnimSite902 = x3d.HAnimSite()
HAnimSite902.DEF = "hanim_nuchale_pt"
HAnimSite902.name = "nuchale_pt"
HAnimSite902.translation = [0.0039,1.5972,-0.0796]
TouchSensor903 = x3d.TouchSensor()
TouchSensor903.description = "HAnimSite nuchale_pt"

HAnimSite902.children.append(TouchSensor903)
Shape904 = x3d.Shape()
Shape904.USE = "HAnimSiteShape"

HAnimSite902.children.append(Shape904)

HAnimSegment883.children.append(HAnimSite902)
HAnimSite905 = x3d.HAnimSite()
HAnimSite905.DEF = "hanim_opisthocranion_pt"
HAnimSite905.name = "opisthocranion_pt"
HAnimSite905.translation = [0,1,0]
TouchSensor906 = x3d.TouchSensor()
TouchSensor906.description = "HAnimSite opisthocranion_pt"

HAnimSite905.children.append(TouchSensor906)
Shape907 = x3d.Shape()
Shape907.USE = "HAnimSiteShape"

HAnimSite905.children.append(Shape907)

HAnimSegment883.children.append(HAnimSite905)
HAnimSite908 = x3d.HAnimSite()
HAnimSite908.DEF = "hanim_r_ectocanthus_pt"
HAnimSite908.name = "r_ectocanthus_pt"
HAnimSite908.translation = [0,1,0]
TouchSensor909 = x3d.TouchSensor()
TouchSensor909.description = "HAnimSite r_ectocanthus_pt"

HAnimSite908.children.append(TouchSensor909)
Shape910 = x3d.Shape()
Shape910.USE = "HAnimSiteShape"

HAnimSite908.children.append(Shape910)

HAnimSegment883.children.append(HAnimSite908)
HAnimSite911 = x3d.HAnimSite()
HAnimSite911.DEF = "hanim_r_infraorbitale_pt"
HAnimSite911.name = "r_infraorbitale_pt"
HAnimSite911.translation = [-0.0237,1.6171,0.0752]
TouchSensor912 = x3d.TouchSensor()
TouchSensor912.description = "HAnimSite r_infraorbitale_pt"

HAnimSite911.children.append(TouchSensor912)
Shape913 = x3d.Shape()
Shape913.USE = "HAnimSiteShape"

HAnimSite911.children.append(Shape913)

HAnimSegment883.children.append(HAnimSite911)
HAnimSite914 = x3d.HAnimSite()
HAnimSite914.DEF = "hanim_r_tragion_pt"
HAnimSite914.name = "r_tragion_pt"
HAnimSite914.translation = [-0.0646,1.6347,0.0302]
TouchSensor915 = x3d.TouchSensor()
TouchSensor915.description = "HAnimSite r_tragion_pt"

HAnimSite914.children.append(TouchSensor915)
Shape916 = x3d.Shape()
Shape916.USE = "HAnimSiteShape"

HAnimSite914.children.append(Shape916)

HAnimSegment883.children.append(HAnimSite914)
HAnimSite917 = x3d.HAnimSite()
HAnimSite917.DEF = "hanim_sellion_pt"
HAnimSite917.name = "sellion_pt"
HAnimSite917.translation = [0.0058,1.6316,0.0852]
TouchSensor918 = x3d.TouchSensor()
TouchSensor918.description = "HAnimSite sellion_pt"

HAnimSite917.children.append(TouchSensor918)
Shape919 = x3d.Shape()
Shape919.USE = "HAnimSiteShape"

HAnimSite917.children.append(Shape919)

HAnimSegment883.children.append(HAnimSite917)
HAnimSite920 = x3d.HAnimSite()
HAnimSite920.DEF = "hanim_skull_vertex_pt"
HAnimSite920.name = "skull_vertex_pt"
HAnimSite920.translation = [0.0050,1.7504,0.0055]
TouchSensor921 = x3d.TouchSensor()
TouchSensor921.description = "HAnimSite skull_vertex_pt"

HAnimSite920.children.append(TouchSensor921)
Shape922 = x3d.Shape()
Shape922.USE = "HAnimSiteShape"

HAnimSite920.children.append(Shape922)

HAnimSegment883.children.append(HAnimSite920)

HAnimJoint882.children.append(HAnimSegment883)
HAnimJoint923 = x3d.HAnimJoint()
HAnimJoint923.DEF = "hanim_skullbase"
HAnimJoint923.name = "skullbase"
HAnimJoint923.center = [0.0044,1.6209,0.0236]
HAnimSegment924 = x3d.HAnimSegment()
HAnimSegment924.DEF = "hanim_skull"
HAnimSegment924.name = "skull"
Transform925 = x3d.Transform()
Transform925.translation = [0.0044,1.6209,0.0236]
Shape926 = x3d.Shape()
Shape926.USE = "HAnimJointShape"

Transform925.children.append(Shape926)

HAnimSegment924.children.append(Transform925)
Shape927 = x3d.Shape()
LineSet928 = x3d.LineSet()
LineSet928.vertexCount = [2]
Coordinate929 = x3d.Coordinate()

LineSet928.coord = Coordinate929
""" from skullbase to l_eyelid_joint """
ColorRGBA930 = x3d.ColorRGBA()
ColorRGBA930.USE = "HAnimSegmentLineColorRGBA"

LineSet928.color = ColorRGBA930

Shape927.geometry = LineSet928

HAnimSegment924.children.append(Shape927)
Shape931 = x3d.Shape()
LineSet932 = x3d.LineSet()
LineSet932.vertexCount = [2]
Coordinate933 = x3d.Coordinate()

LineSet932.coord = Coordinate933
""" from skullbase to r_eyelid_joint """
ColorRGBA934 = x3d.ColorRGBA()
ColorRGBA934.USE = "HAnimSegmentLineColorRGBA"

LineSet932.color = ColorRGBA934

Shape931.geometry = LineSet932

HAnimSegment924.children.append(Shape931)
Shape935 = x3d.Shape()
LineSet936 = x3d.LineSet()
LineSet936.vertexCount = [2]
Coordinate937 = x3d.Coordinate()

LineSet936.coord = Coordinate937
""" from skullbase to l_eyeball_joint """
ColorRGBA938 = x3d.ColorRGBA()
ColorRGBA938.USE = "HAnimSegmentLineColorRGBA"

LineSet936.color = ColorRGBA938

Shape935.geometry = LineSet936

HAnimSegment924.children.append(Shape935)
Shape939 = x3d.Shape()
LineSet940 = x3d.LineSet()
LineSet940.vertexCount = [2]
Coordinate941 = x3d.Coordinate()

LineSet940.coord = Coordinate941
""" from skullbase to r_eyeball_joint """
ColorRGBA942 = x3d.ColorRGBA()
ColorRGBA942.USE = "HAnimSegmentLineColorRGBA"

LineSet940.color = ColorRGBA942

Shape939.geometry = LineSet940

HAnimSegment924.children.append(Shape939)
Shape943 = x3d.Shape()
LineSet944 = x3d.LineSet()
LineSet944.vertexCount = [2]
Coordinate945 = x3d.Coordinate()

LineSet944.coord = Coordinate945
""" from skullbase to l_eyebrow_joint """
ColorRGBA946 = x3d.ColorRGBA()
ColorRGBA946.USE = "HAnimSegmentLineColorRGBA"

LineSet944.color = ColorRGBA946

Shape943.geometry = LineSet944

HAnimSegment924.children.append(Shape943)
Shape947 = x3d.Shape()
LineSet948 = x3d.LineSet()
LineSet948.vertexCount = [2]
Coordinate949 = x3d.Coordinate()

LineSet948.coord = Coordinate949
""" from skullbase to r_eyebrow_joint """
ColorRGBA950 = x3d.ColorRGBA()
ColorRGBA950.USE = "HAnimSegmentLineColorRGBA"

LineSet948.color = ColorRGBA950

Shape947.geometry = LineSet948

HAnimSegment924.children.append(Shape947)
Shape951 = x3d.Shape()
LineSet952 = x3d.LineSet()
LineSet952.vertexCount = [2]
Coordinate953 = x3d.Coordinate()

LineSet952.coord = Coordinate953
""" from skullbase to temporomandibular """
ColorRGBA954 = x3d.ColorRGBA()
ColorRGBA954.USE = "HAnimSegmentLineColorRGBA"

LineSet952.color = ColorRGBA954

Shape951.geometry = LineSet952

HAnimSegment924.children.append(Shape951)
HAnimSite955 = x3d.HAnimSite()
HAnimSite955.DEF = "hanim_l_gonion_pt"
HAnimSite955.name = "l_gonion_pt"
HAnimSite955.translation = [0.0631,1.5530,0.0330]
TouchSensor956 = x3d.TouchSensor()
TouchSensor956.description = "HAnimSite l_gonion_pt"

HAnimSite955.children.append(TouchSensor956)
Shape957 = x3d.Shape()
Shape957.USE = "HAnimSiteShape"

HAnimSite955.children.append(Shape957)

HAnimSegment924.children.append(HAnimSite955)
HAnimSite958 = x3d.HAnimSite()
HAnimSite958.DEF = "hanim_menton_pt"
HAnimSite958.name = "menton_pt"
HAnimSite958.translation = [0,1,0]
TouchSensor959 = x3d.TouchSensor()
TouchSensor959.description = "HAnimSite menton_pt"

HAnimSite958.children.append(TouchSensor959)
Shape960 = x3d.Shape()
Shape960.USE = "HAnimSiteShape"

HAnimSite958.children.append(Shape960)

HAnimSegment924.children.append(HAnimSite958)
HAnimSite961 = x3d.HAnimSite()
HAnimSite961.DEF = "hanim_r_gonion_pt"
HAnimSite961.name = "r_gonion_pt"
HAnimSite961.translation = [-0.0520,1.5529,0.0347]
TouchSensor962 = x3d.TouchSensor()
TouchSensor962.description = "HAnimSite r_gonion_pt"

HAnimSite961.children.append(TouchSensor962)
Shape963 = x3d.Shape()
Shape963.USE = "HAnimSiteShape"

HAnimSite961.children.append(Shape963)

HAnimSegment924.children.append(HAnimSite961)
HAnimSite964 = x3d.HAnimSite()
HAnimSite964.DEF = "hanim_supramenton_pt"
HAnimSite964.name = "supramenton_pt"
HAnimSite964.translation = [0.0061,1.5410,0.0805]
TouchSensor965 = x3d.TouchSensor()
TouchSensor965.description = "HAnimSite supramenton_pt"

HAnimSite964.children.append(TouchSensor965)
Shape966 = x3d.Shape()
Shape966.USE = "HAnimSiteShape"

HAnimSite964.children.append(Shape966)

HAnimSegment924.children.append(HAnimSite964)

HAnimJoint923.children.append(HAnimSegment924)
HAnimJoint967 = x3d.HAnimJoint()
HAnimJoint967.DEF = "hanim_l_eyelid_joint"
HAnimJoint967.name = "l_eyelid_joint"
HAnimJoint967.center = [0,1,0]

HAnimJoint923.children.append(HAnimJoint967)
HAnimJoint968 = x3d.HAnimJoint()
HAnimJoint968.DEF = "hanim_r_eyelid_joint"
HAnimJoint968.name = "r_eyelid_joint"
HAnimJoint968.center = [0,1,0]

HAnimJoint923.children.append(HAnimJoint968)
HAnimJoint969 = x3d.HAnimJoint()
HAnimJoint969.DEF = "hanim_l_eyeball_joint"
HAnimJoint969.name = "l_eyeball_joint"
HAnimJoint969.center = [0,1,0]

HAnimJoint923.children.append(HAnimJoint969)
HAnimJoint970 = x3d.HAnimJoint()
HAnimJoint970.DEF = "hanim_r_eyeball_joint"
HAnimJoint970.name = "r_eyeball_joint"
HAnimJoint970.center = [0,1,0]

HAnimJoint923.children.append(HAnimJoint970)
HAnimJoint971 = x3d.HAnimJoint()
HAnimJoint971.DEF = "hanim_l_eyebrow_joint"
HAnimJoint971.name = "l_eyebrow_joint"
HAnimJoint971.center = [0,1,0]

HAnimJoint923.children.append(HAnimJoint971)
HAnimJoint972 = x3d.HAnimJoint()
HAnimJoint972.DEF = "hanim_r_eyebrow_joint"
HAnimJoint972.name = "r_eyebrow_joint"
HAnimJoint972.center = [0,1,0]

HAnimJoint923.children.append(HAnimJoint972)
HAnimJoint973 = x3d.HAnimJoint()
HAnimJoint973.DEF = "hanim_temporomandibular"
HAnimJoint973.name = "temporomandibular"
HAnimJoint973.center = [0,1,0]

HAnimJoint923.children.append(HAnimJoint973)

HAnimJoint882.children.append(HAnimJoint923)

HAnimJoint874.children.append(HAnimJoint882)

HAnimJoint863.children.append(HAnimJoint874)

HAnimJoint855.children.append(HAnimJoint863)

HAnimJoint847.children.append(HAnimJoint855)

HAnimJoint839.children.append(HAnimJoint847)

HAnimJoint831.children.append(HAnimJoint839)

HAnimJoint779.children.append(HAnimJoint831)
HAnimJoint974 = x3d.HAnimJoint()
HAnimJoint974.DEF = "hanim_l_sternoclavicular"
HAnimJoint974.name = "l_sternoclavicular"
HAnimJoint974.center = [0.0820,1.4488,-0.0353]
HAnimSegment975 = x3d.HAnimSegment()
HAnimSegment975.DEF = "hanim_l_clavicle"
HAnimSegment975.name = "l_clavicle"
Transform976 = x3d.Transform()
Transform976.translation = [0.0820,1.4488,-0.0353]
Shape977 = x3d.Shape()
Shape977.USE = "HAnimJointShape"

Transform976.children.append(Shape977)

HAnimSegment975.children.append(Transform976)
Shape978 = x3d.Shape()
LineSet979 = x3d.LineSet()
LineSet979.vertexCount = [2]
Coordinate980 = x3d.Coordinate()

LineSet979.coord = Coordinate980
""" from l_sternoclavicular to l_acromioclavicular """
ColorRGBA981 = x3d.ColorRGBA()
ColorRGBA981.USE = "HAnimSegmentLineColorRGBA"

LineSet979.color = ColorRGBA981

Shape978.geometry = LineSet979

HAnimSegment975.children.append(Shape978)

HAnimJoint974.children.append(HAnimSegment975)
HAnimJoint982 = x3d.HAnimJoint()
HAnimJoint982.DEF = "hanim_l_acromioclavicular"
HAnimJoint982.name = "l_acromioclavicular"
HAnimJoint982.center = [0.0962,1.4269,-0.0424]
HAnimSegment983 = x3d.HAnimSegment()
HAnimSegment983.DEF = "hanim_l_scapula"
HAnimSegment983.name = "l_scapula"
Transform984 = x3d.Transform()
Transform984.translation = [0.0962,1.4269,-0.0424]
Shape985 = x3d.Shape()
Shape985.USE = "HAnimJointShape"

Transform984.children.append(Shape985)

HAnimSegment983.children.append(Transform984)
Shape986 = x3d.Shape()
LineSet987 = x3d.LineSet()
LineSet987.vertexCount = [2]
Coordinate988 = x3d.Coordinate()

LineSet987.coord = Coordinate988
""" from l_acromioclavicular to l_shoulder """
ColorRGBA989 = x3d.ColorRGBA()
ColorRGBA989.USE = "HAnimSegmentLineColorRGBA"

LineSet987.color = ColorRGBA989

Shape986.geometry = LineSet987

HAnimSegment983.children.append(Shape986)
HAnimSite990 = x3d.HAnimSite()
HAnimSite990.DEF = "hanim_l_bideltoid_pt"
HAnimSite990.name = "l_bideltoid_pt"
HAnimSite990.translation = [0,1,0]
TouchSensor991 = x3d.TouchSensor()
TouchSensor991.description = "HAnimSite l_bideltoid_pt"

HAnimSite990.children.append(TouchSensor991)
Shape992 = x3d.Shape()
Shape992.USE = "HAnimSiteShape"

HAnimSite990.children.append(Shape992)

HAnimSegment983.children.append(HAnimSite990)
HAnimSite993 = x3d.HAnimSite()
HAnimSite993.DEF = "hanim_l_humeral_lateral_epicondyles_pt"
HAnimSite993.name = "l_humeral_lateral_epicondyles_pt"
HAnimSite993.translation = [0.2280,1.1482,-0.1100]
TouchSensor994 = x3d.TouchSensor()
TouchSensor994.description = "HAnimSite l_humeral_lateral_epicondyles_pt"

HAnimSite993.children.append(TouchSensor994)
Shape995 = x3d.Shape()
Shape995.USE = "HAnimSiteShape"

HAnimSite993.children.append(Shape995)

HAnimSegment983.children.append(HAnimSite993)

HAnimJoint982.children.append(HAnimSegment983)
HAnimJoint996 = x3d.HAnimJoint()
HAnimJoint996.DEF = "hanim_l_shoulder"
HAnimJoint996.name = "l_shoulder"
HAnimJoint996.center = [0.2029,1.4376,-0.0387]
HAnimSegment997 = x3d.HAnimSegment()
HAnimSegment997.DEF = "hanim_l_upperarm"
HAnimSegment997.name = "l_upperarm"
Transform998 = x3d.Transform()
Transform998.translation = [0.2029,1.4376,-0.0387]
Shape999 = x3d.Shape()
Shape999.USE = "HAnimJointShape"

Transform998.children.append(Shape999)

HAnimSegment997.children.append(Transform998)
Shape1000 = x3d.Shape()
LineSet1001 = x3d.LineSet()
LineSet1001.vertexCount = [2]
Coordinate1002 = x3d.Coordinate()

LineSet1001.coord = Coordinate1002
""" from l_shoulder to l_elbow """
ColorRGBA1003 = x3d.ColorRGBA()
ColorRGBA1003.USE = "HAnimSegmentLineColorRGBA"

LineSet1001.color = ColorRGBA1003

Shape1000.geometry = LineSet1001

HAnimSegment997.children.append(Shape1000)
HAnimSite1004 = x3d.HAnimSite()
HAnimSite1004.DEF = "hanim_l_humeral_medial_epicondyles_pt"
HAnimSite1004.name = "l_humeral_medial_epicondyles_pt"
HAnimSite1004.translation = [0.1735,1.1272,-0.1113]
TouchSensor1005 = x3d.TouchSensor()
TouchSensor1005.description = "HAnimSite l_humeral_medial_epicondyles_pt"

HAnimSite1004.children.append(TouchSensor1005)
Shape1006 = x3d.Shape()
Shape1006.USE = "HAnimSiteShape"

HAnimSite1004.children.append(Shape1006)

HAnimSegment997.children.append(HAnimSite1004)
HAnimSite1007 = x3d.HAnimSite()
HAnimSite1007.DEF = "hanim_l_olecranon_pt"
HAnimSite1007.name = "l_olecranon_pt"
HAnimSite1007.translation = [-0.1962,1.1375,-0.1123]
TouchSensor1008 = x3d.TouchSensor()
TouchSensor1008.description = "HAnimSite l_olecranon_pt"

HAnimSite1007.children.append(TouchSensor1008)
Shape1009 = x3d.Shape()
Shape1009.USE = "HAnimSiteShape"

HAnimSite1007.children.append(Shape1009)

HAnimSegment997.children.append(HAnimSite1007)
HAnimSite1010 = x3d.HAnimSite()
HAnimSite1010.DEF = "hanim_l_radial_styloid_pt"
HAnimSite1010.name = "l_radial_styloid_pt"
HAnimSite1010.translation = [0.1901,0.8645,-0.0415]
TouchSensor1011 = x3d.TouchSensor()
TouchSensor1011.description = "HAnimSite l_radial_styloid_pt"

HAnimSite1010.children.append(TouchSensor1011)
Shape1012 = x3d.Shape()
Shape1012.USE = "HAnimSiteShape"

HAnimSite1010.children.append(Shape1012)

HAnimSegment997.children.append(HAnimSite1010)
HAnimSite1013 = x3d.HAnimSite()
HAnimSite1013.DEF = "hanim_l_radiale_pt"
HAnimSite1013.name = "l_radiale_pt"
HAnimSite1013.translation = [0.2182,1.1212,-0.1167]
TouchSensor1014 = x3d.TouchSensor()
TouchSensor1014.description = "HAnimSite l_radiale_pt"

HAnimSite1013.children.append(TouchSensor1014)
Shape1015 = x3d.Shape()
Shape1015.USE = "HAnimSiteShape"

HAnimSite1013.children.append(Shape1015)

HAnimSegment997.children.append(HAnimSite1013)

HAnimJoint996.children.append(HAnimSegment997)
HAnimJoint1016 = x3d.HAnimJoint()
HAnimJoint1016.DEF = "hanim_l_elbow"
HAnimJoint1016.name = "l_elbow"
HAnimJoint1016.center = [0.2014,1.1357,-0.0682]
HAnimSegment1017 = x3d.HAnimSegment()
HAnimSegment1017.DEF = "hanim_l_forearm"
HAnimSegment1017.name = "l_forearm"
Transform1018 = x3d.Transform()
Transform1018.translation = [0.2014,1.1357,-0.0682]
Shape1019 = x3d.Shape()
Shape1019.USE = "HAnimJointShape"

Transform1018.children.append(Shape1019)

HAnimSegment1017.children.append(Transform1018)
Shape1020 = x3d.Shape()
LineSet1021 = x3d.LineSet()
LineSet1021.vertexCount = [2]
Coordinate1022 = x3d.Coordinate()

LineSet1021.coord = Coordinate1022
""" from l_elbow to l_radiocarpal """
ColorRGBA1023 = x3d.ColorRGBA()
ColorRGBA1023.USE = "HAnimSegmentLineColorRGBA"

LineSet1021.color = ColorRGBA1023

Shape1020.geometry = LineSet1021

HAnimSegment1017.children.append(Shape1020)
HAnimSite1024 = x3d.HAnimSite()
HAnimSite1024.DEF = "hanim_l_ulnar_styloid_pt"
HAnimSite1024.name = "l_ulnar_styloid_pt"
HAnimSite1024.translation = [-0.2142,0.8529,-0.0648]
TouchSensor1025 = x3d.TouchSensor()
TouchSensor1025.description = "HAnimSite l_ulnar_styloid_pt"

HAnimSite1024.children.append(TouchSensor1025)
Shape1026 = x3d.Shape()
Shape1026.USE = "HAnimSiteShape"

HAnimSite1024.children.append(Shape1026)

HAnimSegment1017.children.append(HAnimSite1024)

HAnimJoint1016.children.append(HAnimSegment1017)
HAnimJoint1027 = x3d.HAnimJoint()
HAnimJoint1027.DEF = "hanim_l_radiocarpal"
HAnimJoint1027.name = "l_radiocarpal"
HAnimJoint1027.center = [0.1984,0.8663,-0.0583]
HAnimSegment1028 = x3d.HAnimSegment()
HAnimSegment1028.DEF = "hanim_l_carpal"
HAnimSegment1028.name = "l_carpal"
Transform1029 = x3d.Transform()
Transform1029.translation = [0.1984,0.8663,-0.0583]
Shape1030 = x3d.Shape()
Shape1030.USE = "HAnimJointShape"

Transform1029.children.append(Shape1030)

HAnimSegment1028.children.append(Transform1029)
Shape1031 = x3d.Shape()
LineSet1032 = x3d.LineSet()
LineSet1032.vertexCount = [2]
Coordinate1033 = x3d.Coordinate()

LineSet1032.coord = Coordinate1033
""" from l_radiocarpal to l_midcarpal_1 """
ColorRGBA1034 = x3d.ColorRGBA()
ColorRGBA1034.USE = "HAnimSegmentLineColorRGBA"

LineSet1032.color = ColorRGBA1034

Shape1031.geometry = LineSet1032

HAnimSegment1028.children.append(Shape1031)
Shape1035 = x3d.Shape()
LineSet1036 = x3d.LineSet()
LineSet1036.vertexCount = [2]
Coordinate1037 = x3d.Coordinate()

LineSet1036.coord = Coordinate1037
""" from l_radiocarpal to l_midcarpal_2 """
ColorRGBA1038 = x3d.ColorRGBA()
ColorRGBA1038.USE = "HAnimSegmentLineColorRGBA"

LineSet1036.color = ColorRGBA1038

Shape1035.geometry = LineSet1036

HAnimSegment1028.children.append(Shape1035)
Shape1039 = x3d.Shape()
LineSet1040 = x3d.LineSet()
LineSet1040.vertexCount = [2]
Coordinate1041 = x3d.Coordinate()

LineSet1040.coord = Coordinate1041
""" from l_radiocarpal to l_midcarpal_3 """
ColorRGBA1042 = x3d.ColorRGBA()
ColorRGBA1042.USE = "HAnimSegmentLineColorRGBA"

LineSet1040.color = ColorRGBA1042

Shape1039.geometry = LineSet1040

HAnimSegment1028.children.append(Shape1039)
Shape1043 = x3d.Shape()
LineSet1044 = x3d.LineSet()
LineSet1044.vertexCount = [2]
Coordinate1045 = x3d.Coordinate()

LineSet1044.coord = Coordinate1045
""" from l_radiocarpal to l_midcarpal_4_5 """
ColorRGBA1046 = x3d.ColorRGBA()
ColorRGBA1046.USE = "HAnimSegmentLineColorRGBA"

LineSet1044.color = ColorRGBA1046

Shape1043.geometry = LineSet1044

HAnimSegment1028.children.append(Shape1043)

HAnimJoint1027.children.append(HAnimSegment1028)
HAnimJoint1047 = x3d.HAnimJoint()
HAnimJoint1047.DEF = "hanim_l_midcarpal_1"
HAnimJoint1047.name = "l_midcarpal_1"
HAnimJoint1047.center = [0,1,0]
HAnimSegment1048 = x3d.HAnimSegment()
HAnimSegment1048.DEF = "hanim_l_trapezium"
HAnimSegment1048.name = "l_trapezium"
Transform1049 = x3d.Transform()
Transform1049.translation = [0,1,0]
Shape1050 = x3d.Shape()
Shape1050.USE = "HAnimJointShape"

Transform1049.children.append(Shape1050)

HAnimSegment1048.children.append(Transform1049)
Shape1051 = x3d.Shape()
LineSet1052 = x3d.LineSet()
LineSet1052.vertexCount = [1]
Coordinate1053 = x3d.Coordinate()

LineSet1052.coord = Coordinate1053
""" from l_midcarpal_1 to l_carpometacarpal_1 """
ColorRGBA1054 = x3d.ColorRGBA()
ColorRGBA1054.USE = "HAnimSegmentLineColorRGBA"

LineSet1052.color = ColorRGBA1054

Shape1051.geometry = LineSet1052

HAnimSegment1048.children.append(Shape1051)

HAnimJoint1047.children.append(HAnimSegment1048)
HAnimJoint1055 = x3d.HAnimJoint()
HAnimJoint1055.DEF = "hanim_l_carpometacarpal_1"
HAnimJoint1055.name = "l_carpometacarpal_1"
HAnimJoint1055.center = [0.2,0.15,0]
HAnimSegment1056 = x3d.HAnimSegment()
HAnimSegment1056.DEF = "hanim_l_metacarpal_1"
HAnimSegment1056.name = "l_metacarpal_1"
Transform1057 = x3d.Transform()
Transform1057.translation = [0.2,0.15,0]
Shape1058 = x3d.Shape()
Shape1058.USE = "HAnimJointShape"

Transform1057.children.append(Shape1058)

HAnimSegment1056.children.append(Transform1057)
Shape1059 = x3d.Shape()
LineSet1060 = x3d.LineSet()
LineSet1060.vertexCount = [2]
Coordinate1061 = x3d.Coordinate()

LineSet1060.coord = Coordinate1061
""" from l_carpometacarpal_1 to l_metacarpophalangeal_1 """
ColorRGBA1062 = x3d.ColorRGBA()
ColorRGBA1062.USE = "HAnimSegmentLineColorRGBA"

LineSet1060.color = ColorRGBA1062

Shape1059.geometry = LineSet1060

HAnimSegment1056.children.append(Shape1059)

HAnimJoint1055.children.append(HAnimSegment1056)
HAnimJoint1063 = x3d.HAnimJoint()
HAnimJoint1063.DEF = "hanim_l_metacarpophalangeal_1"
HAnimJoint1063.name = "l_metacarpophalangeal_1"
HAnimJoint1063.center = [0.3,0.3,0]
HAnimSegment1064 = x3d.HAnimSegment()
HAnimSegment1064.DEF = "hanim_l_carpal_proximal_phalanx_1"
HAnimSegment1064.name = "l_carpal_proximal_phalanx_1"
Transform1065 = x3d.Transform()
Transform1065.translation = [0.3,0.3,0]
Shape1066 = x3d.Shape()
Shape1066.USE = "HAnimJointShape"

Transform1065.children.append(Shape1066)

HAnimSegment1064.children.append(Transform1065)
Shape1067 = x3d.Shape()
LineSet1068 = x3d.LineSet()
LineSet1068.vertexCount = [2]
Coordinate1069 = x3d.Coordinate()

LineSet1068.coord = Coordinate1069
""" from l_metacarpophalangeal_1 to l_carpal_interphalangeal_1 """
ColorRGBA1070 = x3d.ColorRGBA()
ColorRGBA1070.USE = "HAnimSegmentLineColorRGBA"

LineSet1068.color = ColorRGBA1070

Shape1067.geometry = LineSet1068

HAnimSegment1064.children.append(Shape1067)
HAnimSite1071 = x3d.HAnimSite()
HAnimSite1071.DEF = "hanim_l_carpal_distal_phalanx_1_tip"
HAnimSite1071.name = "l_carpal_distal_phalanx_1_tip"
HAnimSite1071.translation = [0.35,0.4,0]
TouchSensor1072 = x3d.TouchSensor()
TouchSensor1072.description = "HAnimSite l_carpal_distal_phalanx_1_tip"

HAnimSite1071.children.append(TouchSensor1072)
Shape1073 = x3d.Shape()
Shape1073.USE = "HAnimSiteShape"

HAnimSite1071.children.append(Shape1073)

HAnimSegment1064.children.append(HAnimSite1071)

HAnimJoint1063.children.append(HAnimSegment1064)
HAnimJoint1074 = x3d.HAnimJoint()
HAnimJoint1074.DEF = "hanim_l_carpal_interphalangeal_1"
HAnimJoint1074.name = "l_carpal_interphalangeal_1"
HAnimJoint1074.center = [0.35,0.4,0]

HAnimJoint1063.children.append(HAnimJoint1074)

HAnimJoint1055.children.append(HAnimJoint1063)

HAnimJoint1047.children.append(HAnimJoint1055)

HAnimJoint1027.children.append(HAnimJoint1047)
HAnimJoint1075 = x3d.HAnimJoint()
HAnimJoint1075.DEF = "hanim_l_midcarpal_2"
HAnimJoint1075.name = "l_midcarpal_2"
HAnimJoint1075.center = [0.1,0.1,0]
HAnimSegment1076 = x3d.HAnimSegment()
HAnimSegment1076.DEF = "hanim_l_trapezoid"
HAnimSegment1076.name = "l_trapezoid"
Transform1077 = x3d.Transform()
Transform1077.translation = [0.1,0.1,0]
Shape1078 = x3d.Shape()
Shape1078.USE = "HAnimJointShape"

Transform1077.children.append(Shape1078)

HAnimSegment1076.children.append(Transform1077)
Shape1079 = x3d.Shape()
LineSet1080 = x3d.LineSet()
LineSet1080.vertexCount = [2]
Coordinate1081 = x3d.Coordinate()

LineSet1080.coord = Coordinate1081
""" from l_midcarpal_2 to l_carpometacarpal_2 """
ColorRGBA1082 = x3d.ColorRGBA()
ColorRGBA1082.USE = "HAnimSegmentLineColorRGBA"

LineSet1080.color = ColorRGBA1082

Shape1079.geometry = LineSet1080

HAnimSegment1076.children.append(Shape1079)
HAnimSite1083 = x3d.HAnimSite()
HAnimSite1083.DEF = "hanim_l_metacarpal_phalanx_2_pt"
HAnimSite1083.name = "l_metacarpal_phalanx_2_pt"
HAnimSite1083.translation = [0.2009,0.8139,-0.0237]
TouchSensor1084 = x3d.TouchSensor()
TouchSensor1084.description = "HAnimSite l_metacarpal_phalanx_2_pt"

HAnimSite1083.children.append(TouchSensor1084)
Shape1085 = x3d.Shape()
Shape1085.USE = "HAnimSiteShape"

HAnimSite1083.children.append(Shape1085)

HAnimSegment1076.children.append(HAnimSite1083)

HAnimJoint1075.children.append(HAnimSegment1076)
HAnimJoint1086 = x3d.HAnimJoint()
HAnimJoint1086.DEF = "hanim_l_carpometacarpal_2"
HAnimJoint1086.name = "l_carpometacarpal_2"
HAnimJoint1086.center = [0.1,0.2,0]
HAnimSegment1087 = x3d.HAnimSegment()
HAnimSegment1087.DEF = "hanim_l_metacarpal_2"
HAnimSegment1087.name = "l_metacarpal_2"
Transform1088 = x3d.Transform()
Transform1088.translation = [0.1,0.2,0]
Shape1089 = x3d.Shape()
Shape1089.USE = "HAnimJointShape"

Transform1088.children.append(Shape1089)

HAnimSegment1087.children.append(Transform1088)
Shape1090 = x3d.Shape()
LineSet1091 = x3d.LineSet()
LineSet1091.vertexCount = [2]
Coordinate1092 = x3d.Coordinate()

LineSet1091.coord = Coordinate1092
""" from l_carpometacarpal_2 to l_metacarpophalangeal_2 """
ColorRGBA1093 = x3d.ColorRGBA()
ColorRGBA1093.USE = "HAnimSegmentLineColorRGBA"

LineSet1091.color = ColorRGBA1093

Shape1090.geometry = LineSet1091

HAnimSegment1087.children.append(Shape1090)

HAnimJoint1086.children.append(HAnimSegment1087)
HAnimJoint1094 = x3d.HAnimJoint()
HAnimJoint1094.DEF = "hanim_l_metacarpophalangeal_2"
HAnimJoint1094.name = "l_metacarpophalangeal_2"
HAnimJoint1094.center = [0.15,0.5,0]
HAnimSegment1095 = x3d.HAnimSegment()
HAnimSegment1095.DEF = "hanim_l_carpal_proximal_phalanx_2"
HAnimSegment1095.name = "l_carpal_proximal_phalanx_2"
Transform1096 = x3d.Transform()
Transform1096.translation = [0.15,0.5,0]
Shape1097 = x3d.Shape()
Shape1097.USE = "HAnimJointShape"

Transform1096.children.append(Shape1097)

HAnimSegment1095.children.append(Transform1096)
Shape1098 = x3d.Shape()
LineSet1099 = x3d.LineSet()
LineSet1099.vertexCount = [2]
Coordinate1100 = x3d.Coordinate()

LineSet1099.coord = Coordinate1100
""" from l_metacarpophalangeal_2 to l_carpal_proximal_interphalangeal_2 """
ColorRGBA1101 = x3d.ColorRGBA()
ColorRGBA1101.USE = "HAnimSegmentLineColorRGBA"

LineSet1099.color = ColorRGBA1101

Shape1098.geometry = LineSet1099

HAnimSegment1095.children.append(Shape1098)

HAnimJoint1094.children.append(HAnimSegment1095)
HAnimJoint1102 = x3d.HAnimJoint()
HAnimJoint1102.DEF = "hanim_l_carpal_proximal_interphalangeal_2"
HAnimJoint1102.name = "l_carpal_proximal_interphalangeal_2"
HAnimJoint1102.center = [0.2,0.7,0]
HAnimSegment1103 = x3d.HAnimSegment()
HAnimSegment1103.DEF = "hanim_l_carpal_middle_phalanx_2"
HAnimSegment1103.name = "l_carpal_middle_phalanx_2"
Transform1104 = x3d.Transform()
Transform1104.translation = [0.2,0.7,0]
Shape1105 = x3d.Shape()
Shape1105.USE = "HAnimJointShape"

Transform1104.children.append(Shape1105)

HAnimSegment1103.children.append(Transform1104)
Shape1106 = x3d.Shape()
LineSet1107 = x3d.LineSet()
LineSet1107.vertexCount = [2]
Coordinate1108 = x3d.Coordinate()

LineSet1107.coord = Coordinate1108
""" from l_carpal_proximal_interphalangeal_2 to l_carpal_distal_interphalangeal_2 """
ColorRGBA1109 = x3d.ColorRGBA()
ColorRGBA1109.USE = "HAnimSegmentLineColorRGBA"

LineSet1107.color = ColorRGBA1109

Shape1106.geometry = LineSet1107

HAnimSegment1103.children.append(Shape1106)
HAnimSite1110 = x3d.HAnimSite()
HAnimSite1110.DEF = "hanim_l_carpal_distal_phalanx_2_tip"
HAnimSite1110.name = "l_carpal_distal_phalanx_2_tip"
HAnimSite1110.translation = [0.24,0.87,0]
TouchSensor1111 = x3d.TouchSensor()
TouchSensor1111.description = "HAnimSite l_carpal_distal_phalanx_2_tip"

HAnimSite1110.children.append(TouchSensor1111)
Shape1112 = x3d.Shape()
Shape1112.USE = "HAnimSiteShape"

HAnimSite1110.children.append(Shape1112)

HAnimSegment1103.children.append(HAnimSite1110)
HAnimSite1113 = x3d.HAnimSite()
HAnimSite1113.DEF = "hanim_l_dactylion_pt"
HAnimSite1113.name = "l_dactylion_pt"
HAnimSite1113.translation = [0.2056,0.6743,-0.0482]
TouchSensor1114 = x3d.TouchSensor()
TouchSensor1114.description = "HAnimSite l_dactylion_pt"

HAnimSite1113.children.append(TouchSensor1114)
Shape1115 = x3d.Shape()
Shape1115.USE = "HAnimSiteShape"

HAnimSite1113.children.append(Shape1115)

HAnimSegment1103.children.append(HAnimSite1113)

HAnimJoint1102.children.append(HAnimSegment1103)
HAnimJoint1116 = x3d.HAnimJoint()
HAnimJoint1116.DEF = "hanim_l_carpal_distal_interphalangeal_2"
HAnimJoint1116.name = "l_carpal_distal_interphalangeal_2"
HAnimJoint1116.center = [0.24,0.87,0]

HAnimJoint1102.children.append(HAnimJoint1116)

HAnimJoint1094.children.append(HAnimJoint1102)

HAnimJoint1086.children.append(HAnimJoint1094)

HAnimJoint1075.children.append(HAnimJoint1086)

HAnimJoint1027.children.append(HAnimJoint1075)
HAnimJoint1117 = x3d.HAnimJoint()
HAnimJoint1117.DEF = "hanim_l_midcarpal_3"
HAnimJoint1117.name = "l_midcarpal_3"
HAnimJoint1117.center = [0.0,0.07,0]
HAnimSegment1118 = x3d.HAnimSegment()
HAnimSegment1118.DEF = "hanim_l_capitate"
HAnimSegment1118.name = "l_capitate"
Transform1119 = x3d.Transform()
Transform1119.translation = [0.0,0.07,0]
Shape1120 = x3d.Shape()
Shape1120.USE = "HAnimJointShape"

Transform1119.children.append(Shape1120)

HAnimSegment1118.children.append(Transform1119)
Shape1121 = x3d.Shape()
LineSet1122 = x3d.LineSet()
LineSet1122.vertexCount = [2]
Coordinate1123 = x3d.Coordinate()

LineSet1122.coord = Coordinate1123
""" from l_midcarpal_3 to l_carpometacarpal_3 """
ColorRGBA1124 = x3d.ColorRGBA()
ColorRGBA1124.USE = "HAnimSegmentLineColorRGBA"

LineSet1122.color = ColorRGBA1124

Shape1121.geometry = LineSet1122

HAnimSegment1118.children.append(Shape1121)
HAnimSite1125 = x3d.HAnimSite()
HAnimSite1125.DEF = "hanim_l_metacarpal_phalanx_3_pt"
HAnimSite1125.name = "l_metacarpal_phalanx_3_pt"
HAnimSite1125.translation = [0,1,0]
TouchSensor1126 = x3d.TouchSensor()
TouchSensor1126.description = "HAnimSite l_metacarpal_phalanx_3_pt"

HAnimSite1125.children.append(TouchSensor1126)
Shape1127 = x3d.Shape()
Shape1127.USE = "HAnimSiteShape"

HAnimSite1125.children.append(Shape1127)

HAnimSegment1118.children.append(HAnimSite1125)

HAnimJoint1117.children.append(HAnimSegment1118)
HAnimJoint1128 = x3d.HAnimJoint()
HAnimJoint1128.DEF = "hanim_l_carpometacarpal_3"
HAnimJoint1128.name = "l_carpometacarpal_3"
HAnimJoint1128.center = [0.0,0.2,0]
HAnimSegment1129 = x3d.HAnimSegment()
HAnimSegment1129.DEF = "hanim_l_metacarpal_3"
HAnimSegment1129.name = "l_metacarpal_3"
Transform1130 = x3d.Transform()
Transform1130.translation = [0.0,0.2,0]
Shape1131 = x3d.Shape()
Shape1131.USE = "HAnimJointShape"

Transform1130.children.append(Shape1131)

HAnimSegment1129.children.append(Transform1130)
Shape1132 = x3d.Shape()
LineSet1133 = x3d.LineSet()
LineSet1133.vertexCount = [2]
Coordinate1134 = x3d.Coordinate()

LineSet1133.coord = Coordinate1134
""" from l_carpometacarpal_3 to l_metacarpophalangeal_3 """
ColorRGBA1135 = x3d.ColorRGBA()
ColorRGBA1135.USE = "HAnimSegmentLineColorRGBA"

LineSet1133.color = ColorRGBA1135

Shape1132.geometry = LineSet1133

HAnimSegment1129.children.append(Shape1132)

HAnimJoint1128.children.append(HAnimSegment1129)
HAnimJoint1136 = x3d.HAnimJoint()
HAnimJoint1136.DEF = "hanim_l_metacarpophalangeal_3"
HAnimJoint1136.name = "l_metacarpophalangeal_3"
HAnimJoint1136.center = [0.03,0.5,0]
HAnimSegment1137 = x3d.HAnimSegment()
HAnimSegment1137.DEF = "hanim_l_carpal_proximal_phalanx_3"
HAnimSegment1137.name = "l_carpal_proximal_phalanx_3"
Transform1138 = x3d.Transform()
Transform1138.translation = [0.03,0.5,0]
Shape1139 = x3d.Shape()
Shape1139.USE = "HAnimJointShape"

Transform1138.children.append(Shape1139)

HAnimSegment1137.children.append(Transform1138)
Shape1140 = x3d.Shape()
LineSet1141 = x3d.LineSet()
LineSet1141.vertexCount = [2]
Coordinate1142 = x3d.Coordinate()

LineSet1141.coord = Coordinate1142
""" from l_metacarpophalangeal_3 to l_carpal_proximal_interphalangeal_3 """
ColorRGBA1143 = x3d.ColorRGBA()
ColorRGBA1143.USE = "HAnimSegmentLineColorRGBA"

LineSet1141.color = ColorRGBA1143

Shape1140.geometry = LineSet1141

HAnimSegment1137.children.append(Shape1140)

HAnimJoint1136.children.append(HAnimSegment1137)
HAnimJoint1144 = x3d.HAnimJoint()
HAnimJoint1144.DEF = "hanim_l_carpal_proximal_interphalangeal_3"
HAnimJoint1144.name = "l_carpal_proximal_interphalangeal_3"
HAnimJoint1144.center = [0.05,0.75,0]
HAnimSegment1145 = x3d.HAnimSegment()
HAnimSegment1145.DEF = "hanim_l_carpal_middle_phalanx_3"
HAnimSegment1145.name = "l_carpal_middle_phalanx_3"
Transform1146 = x3d.Transform()
Transform1146.translation = [0.05,0.75,0]
Shape1147 = x3d.Shape()
Shape1147.USE = "HAnimJointShape"

Transform1146.children.append(Shape1147)

HAnimSegment1145.children.append(Transform1146)
Shape1148 = x3d.Shape()
LineSet1149 = x3d.LineSet()
LineSet1149.vertexCount = [2]
Coordinate1150 = x3d.Coordinate()

LineSet1149.coord = Coordinate1150
""" from l_carpal_proximal_interphalangeal_3 to l_carpal_distal_interphalangeal_3 """
ColorRGBA1151 = x3d.ColorRGBA()
ColorRGBA1151.USE = "HAnimSegmentLineColorRGBA"

LineSet1149.color = ColorRGBA1151

Shape1148.geometry = LineSet1149

HAnimSegment1145.children.append(Shape1148)
HAnimSite1152 = x3d.HAnimSite()
HAnimSite1152.DEF = "hanim_l_carpal_distal_phalanx_3_tip"
HAnimSite1152.name = "l_carpal_distal_phalanx_3_tip"
HAnimSite1152.translation = [0.08,0.96,0]
TouchSensor1153 = x3d.TouchSensor()
TouchSensor1153.description = "HAnimSite l_carpal_distal_phalanx_3_tip"

HAnimSite1152.children.append(TouchSensor1153)
Shape1154 = x3d.Shape()
Shape1154.USE = "HAnimSiteShape"

HAnimSite1152.children.append(Shape1154)

HAnimSegment1145.children.append(HAnimSite1152)

HAnimJoint1144.children.append(HAnimSegment1145)
HAnimJoint1155 = x3d.HAnimJoint()
HAnimJoint1155.DEF = "hanim_l_carpal_distal_interphalangeal_3"
HAnimJoint1155.name = "l_carpal_distal_interphalangeal_3"
HAnimJoint1155.center = [0.08,0.96,0]

HAnimJoint1144.children.append(HAnimJoint1155)

HAnimJoint1136.children.append(HAnimJoint1144)

HAnimJoint1128.children.append(HAnimJoint1136)

HAnimJoint1117.children.append(HAnimJoint1128)

HAnimJoint1027.children.append(HAnimJoint1117)
HAnimJoint1156 = x3d.HAnimJoint()
HAnimJoint1156.DEF = "hanim_l_midcarpal_4_5"
HAnimJoint1156.name = "l_midcarpal_4_5"
HAnimJoint1156.center = [-0.1,0.1,0]
HAnimSegment1157 = x3d.HAnimSegment()
HAnimSegment1157.DEF = "hanim_l_hamate"
HAnimSegment1157.name = "l_hamate"
Transform1158 = x3d.Transform()
Transform1158.translation = [-0.1,0.1,0]
Shape1159 = x3d.Shape()
Shape1159.USE = "HAnimJointShape"

Transform1158.children.append(Shape1159)

HAnimSegment1157.children.append(Transform1158)
Shape1160 = x3d.Shape()
LineSet1161 = x3d.LineSet()
LineSet1161.vertexCount = [2]
Coordinate1162 = x3d.Coordinate()

LineSet1161.coord = Coordinate1162
""" from l_midcarpal_4_5 to l_carpometacarpal_4 """
ColorRGBA1163 = x3d.ColorRGBA()
ColorRGBA1163.USE = "HAnimSegmentLineColorRGBA"

LineSet1161.color = ColorRGBA1163

Shape1160.geometry = LineSet1161

HAnimSegment1157.children.append(Shape1160)
Shape1164 = x3d.Shape()
LineSet1165 = x3d.LineSet()
LineSet1165.vertexCount = [2]
Coordinate1166 = x3d.Coordinate()

LineSet1165.coord = Coordinate1166
""" from l_midcarpal_4_5 to l_carpometacarpal_5 """
ColorRGBA1167 = x3d.ColorRGBA()
ColorRGBA1167.USE = "HAnimSegmentLineColorRGBA"

LineSet1165.color = ColorRGBA1167

Shape1164.geometry = LineSet1165

HAnimSegment1157.children.append(Shape1164)
HAnimSite1168 = x3d.HAnimSite()
HAnimSite1168.DEF = "hanim_l_metacarpal_phalanx_5_pt"
HAnimSite1168.name = "l_metacarpal_phalanx_5_pt"
HAnimSite1168.translation = [0.1929,0.7860,-0.1122]
TouchSensor1169 = x3d.TouchSensor()
TouchSensor1169.description = "HAnimSite l_metacarpal_phalanx_5_pt"

HAnimSite1168.children.append(TouchSensor1169)
Shape1170 = x3d.Shape()
Shape1170.USE = "HAnimSiteShape"

HAnimSite1168.children.append(Shape1170)

HAnimSegment1157.children.append(HAnimSite1168)

HAnimJoint1156.children.append(HAnimSegment1157)
HAnimJoint1171 = x3d.HAnimJoint()
HAnimJoint1171.DEF = "hanim_l_carpometacarpal_4"
HAnimJoint1171.name = "l_carpometacarpal_4"
HAnimJoint1171.center = [-0.1,0.2,0]
HAnimSegment1172 = x3d.HAnimSegment()
HAnimSegment1172.DEF = "hanim_l_metacarpal_4"
HAnimSegment1172.name = "l_metacarpal_4"
Transform1173 = x3d.Transform()
Transform1173.translation = [-0.1,0.2,0]
Shape1174 = x3d.Shape()
Shape1174.USE = "HAnimJointShape"

Transform1173.children.append(Shape1174)

HAnimSegment1172.children.append(Transform1173)
Shape1175 = x3d.Shape()
LineSet1176 = x3d.LineSet()
LineSet1176.vertexCount = [2]
Coordinate1177 = x3d.Coordinate()

LineSet1176.coord = Coordinate1177
""" from l_carpometacarpal_4 to l_metacarpophalangeal_4 """
ColorRGBA1178 = x3d.ColorRGBA()
ColorRGBA1178.USE = "HAnimSegmentLineColorRGBA"

LineSet1176.color = ColorRGBA1178

Shape1175.geometry = LineSet1176

HAnimSegment1172.children.append(Shape1175)

HAnimJoint1171.children.append(HAnimSegment1172)
HAnimJoint1179 = x3d.HAnimJoint()
HAnimJoint1179.DEF = "hanim_l_metacarpophalangeal_4"
HAnimJoint1179.name = "l_metacarpophalangeal_4"
HAnimJoint1179.center = [-0.1,0.47,0]
HAnimSegment1180 = x3d.HAnimSegment()
HAnimSegment1180.DEF = "hanim_l_carpal_proximal_phalanx_4"
HAnimSegment1180.name = "l_carpal_proximal_phalanx_4"
Transform1181 = x3d.Transform()
Transform1181.translation = [-0.1,0.47,0]
Shape1182 = x3d.Shape()
Shape1182.USE = "HAnimJointShape"

Transform1181.children.append(Shape1182)

HAnimSegment1180.children.append(Transform1181)
Shape1183 = x3d.Shape()
LineSet1184 = x3d.LineSet()
LineSet1184.vertexCount = [2]
Coordinate1185 = x3d.Coordinate()

LineSet1184.coord = Coordinate1185
""" from l_metacarpophalangeal_4 to l_carpal_proximal_interphalangeal_4 """
ColorRGBA1186 = x3d.ColorRGBA()
ColorRGBA1186.USE = "HAnimSegmentLineColorRGBA"

LineSet1184.color = ColorRGBA1186

Shape1183.geometry = LineSet1184

HAnimSegment1180.children.append(Shape1183)

HAnimJoint1179.children.append(HAnimSegment1180)
HAnimJoint1187 = x3d.HAnimJoint()
HAnimJoint1187.DEF = "hanim_l_carpal_proximal_interphalangeal_4"
HAnimJoint1187.name = "l_carpal_proximal_interphalangeal_4"
HAnimJoint1187.center = [-0.1,0.7,0]
HAnimSegment1188 = x3d.HAnimSegment()
HAnimSegment1188.DEF = "hanim_l_carpal_middle_phalanx_4"
HAnimSegment1188.name = "l_carpal_middle_phalanx_4"
Transform1189 = x3d.Transform()
Transform1189.translation = [-0.1,0.7,0]
Shape1190 = x3d.Shape()
Shape1190.USE = "HAnimJointShape"

Transform1189.children.append(Shape1190)

HAnimSegment1188.children.append(Transform1189)
Shape1191 = x3d.Shape()
LineSet1192 = x3d.LineSet()
LineSet1192.vertexCount = [2]
Coordinate1193 = x3d.Coordinate()

LineSet1192.coord = Coordinate1193
""" from l_carpal_proximal_interphalangeal_4 to l_carpal_distal_interphalangeal_4 """
ColorRGBA1194 = x3d.ColorRGBA()
ColorRGBA1194.USE = "HAnimSegmentLineColorRGBA"

LineSet1192.color = ColorRGBA1194

Shape1191.geometry = LineSet1192

HAnimSegment1188.children.append(Shape1191)
HAnimSite1195 = x3d.HAnimSite()
HAnimSite1195.DEF = "hanim_l_carpal_distal_phalanx_4_tip"
HAnimSite1195.name = "l_carpal_distal_phalanx_4_tip"
HAnimSite1195.translation = [-0.1,0.93,0]
TouchSensor1196 = x3d.TouchSensor()
TouchSensor1196.description = "HAnimSite l_carpal_distal_phalanx_4_tip"

HAnimSite1195.children.append(TouchSensor1196)
Shape1197 = x3d.Shape()
Shape1197.USE = "HAnimSiteShape"

HAnimSite1195.children.append(Shape1197)

HAnimSegment1188.children.append(HAnimSite1195)

HAnimJoint1187.children.append(HAnimSegment1188)
HAnimJoint1198 = x3d.HAnimJoint()
HAnimJoint1198.DEF = "hanim_l_carpal_distal_interphalangeal_4"
HAnimJoint1198.name = "l_carpal_distal_interphalangeal_4"
HAnimJoint1198.center = [-0.1,0.93,0]

HAnimJoint1187.children.append(HAnimJoint1198)

HAnimJoint1179.children.append(HAnimJoint1187)

HAnimJoint1171.children.append(HAnimJoint1179)

HAnimJoint1156.children.append(HAnimJoint1171)
HAnimJoint1199 = x3d.HAnimJoint()
HAnimJoint1199.DEF = "hanim_l_carpometacarpal_5"
HAnimJoint1199.name = "l_carpometacarpal_5"
HAnimJoint1199.center = [-0.15,0.17,0]
HAnimSegment1200 = x3d.HAnimSegment()
HAnimSegment1200.DEF = "hanim_l_metacarpal_5"
HAnimSegment1200.name = "l_metacarpal_5"
Transform1201 = x3d.Transform()
Transform1201.translation = [-0.15,0.17,0]
Shape1202 = x3d.Shape()
Shape1202.USE = "HAnimJointShape"

Transform1201.children.append(Shape1202)

HAnimSegment1200.children.append(Transform1201)
Shape1203 = x3d.Shape()
LineSet1204 = x3d.LineSet()
LineSet1204.vertexCount = [2]
Coordinate1205 = x3d.Coordinate()

LineSet1204.coord = Coordinate1205
""" from l_carpometacarpal_5 to l_metacarpophalangeal_5 """
ColorRGBA1206 = x3d.ColorRGBA()
ColorRGBA1206.USE = "HAnimSegmentLineColorRGBA"

LineSet1204.color = ColorRGBA1206

Shape1203.geometry = LineSet1204

HAnimSegment1200.children.append(Shape1203)

HAnimJoint1199.children.append(HAnimSegment1200)
HAnimJoint1207 = x3d.HAnimJoint()
HAnimJoint1207.DEF = "hanim_l_metacarpophalangeal_5"
HAnimJoint1207.name = "l_metacarpophalangeal_5"
HAnimJoint1207.center = [-0.2,0.4,0]
HAnimSegment1208 = x3d.HAnimSegment()
HAnimSegment1208.DEF = "hanim_l_carpal_proximal_phalanx_5"
HAnimSegment1208.name = "l_carpal_proximal_phalanx_5"
Transform1209 = x3d.Transform()
Transform1209.translation = [-0.2,0.4,0]
Shape1210 = x3d.Shape()
Shape1210.USE = "HAnimJointShape"

Transform1209.children.append(Shape1210)

HAnimSegment1208.children.append(Transform1209)
Shape1211 = x3d.Shape()
LineSet1212 = x3d.LineSet()
LineSet1212.vertexCount = [2]
Coordinate1213 = x3d.Coordinate()

LineSet1212.coord = Coordinate1213
""" from l_metacarpophalangeal_5 to l_carpal_proximal_interphalangeal_5 """
ColorRGBA1214 = x3d.ColorRGBA()
ColorRGBA1214.USE = "HAnimSegmentLineColorRGBA"

LineSet1212.color = ColorRGBA1214

Shape1211.geometry = LineSet1212

HAnimSegment1208.children.append(Shape1211)

HAnimJoint1207.children.append(HAnimSegment1208)
HAnimJoint1215 = x3d.HAnimJoint()
HAnimJoint1215.DEF = "hanim_l_carpal_proximal_interphalangeal_5"
HAnimJoint1215.name = "l_carpal_proximal_interphalangeal_5"
HAnimJoint1215.center = [-0.23,0.63,0]
HAnimSegment1216 = x3d.HAnimSegment()
HAnimSegment1216.DEF = "hanim_l_carpal_middle_phalanx_5"
HAnimSegment1216.name = "l_carpal_middle_phalanx_5"
Transform1217 = x3d.Transform()
Transform1217.translation = [-0.23,0.63,0]
Shape1218 = x3d.Shape()
Shape1218.USE = "HAnimJointShape"

Transform1217.children.append(Shape1218)

HAnimSegment1216.children.append(Transform1217)
Shape1219 = x3d.Shape()
LineSet1220 = x3d.LineSet()
LineSet1220.vertexCount = [2]
Coordinate1221 = x3d.Coordinate()

LineSet1220.coord = Coordinate1221
""" from l_carpal_proximal_interphalangeal_5 to l_carpal_distal_interphalangeal_5 """
ColorRGBA1222 = x3d.ColorRGBA()
ColorRGBA1222.USE = "HAnimSegmentLineColorRGBA"

LineSet1220.color = ColorRGBA1222

Shape1219.geometry = LineSet1220

HAnimSegment1216.children.append(Shape1219)
HAnimSite1223 = x3d.HAnimSite()
HAnimSite1223.DEF = "hanim_l_carpal_distal_phalanx_5_tip"
HAnimSite1223.name = "l_carpal_distal_phalanx_5_tip"
HAnimSite1223.translation = [-0.25,0.79,0]
TouchSensor1224 = x3d.TouchSensor()
TouchSensor1224.description = "HAnimSite l_carpal_distal_phalanx_5_tip"

HAnimSite1223.children.append(TouchSensor1224)
Shape1225 = x3d.Shape()
Shape1225.USE = "HAnimSiteShape"

HAnimSite1223.children.append(Shape1225)

HAnimSegment1216.children.append(HAnimSite1223)

HAnimJoint1215.children.append(HAnimSegment1216)
HAnimJoint1226 = x3d.HAnimJoint()
HAnimJoint1226.DEF = "hanim_l_carpal_distal_interphalangeal_5"
HAnimJoint1226.name = "l_carpal_distal_interphalangeal_5"
HAnimJoint1226.center = [-0.25,0.79,0]

HAnimJoint1215.children.append(HAnimJoint1226)

HAnimJoint1207.children.append(HAnimJoint1215)

HAnimJoint1199.children.append(HAnimJoint1207)

HAnimJoint1156.children.append(HAnimJoint1199)

HAnimJoint1027.children.append(HAnimJoint1156)

HAnimJoint1016.children.append(HAnimJoint1027)

HAnimJoint996.children.append(HAnimJoint1016)

HAnimJoint982.children.append(HAnimJoint996)

HAnimJoint974.children.append(HAnimJoint982)

HAnimJoint779.children.append(HAnimJoint974)
HAnimJoint1227 = x3d.HAnimJoint()
HAnimJoint1227.DEF = "hanim_r_sternoclavicular"
HAnimJoint1227.name = "r_sternoclavicular"
HAnimJoint1227.center = [-0.0694,1.4600,-0.0330]
HAnimSegment1228 = x3d.HAnimSegment()
HAnimSegment1228.DEF = "hanim_r_clavicle"
HAnimSegment1228.name = "r_clavicle"
Transform1229 = x3d.Transform()
Transform1229.translation = [-0.0694,1.4600,-0.0330]
Shape1230 = x3d.Shape()
Shape1230.USE = "HAnimJointShape"

Transform1229.children.append(Shape1230)

HAnimSegment1228.children.append(Transform1229)
Shape1231 = x3d.Shape()
LineSet1232 = x3d.LineSet()
LineSet1232.vertexCount = [2]
Coordinate1233 = x3d.Coordinate()

LineSet1232.coord = Coordinate1233
""" from r_sternoclavicular to r_acromioclavicular """
ColorRGBA1234 = x3d.ColorRGBA()
ColorRGBA1234.USE = "HAnimSegmentLineColorRGBA"

LineSet1232.color = ColorRGBA1234

Shape1231.geometry = LineSet1232

HAnimSegment1228.children.append(Shape1231)

HAnimJoint1227.children.append(HAnimSegment1228)
HAnimJoint1235 = x3d.HAnimJoint()
HAnimJoint1235.DEF = "hanim_r_acromioclavicular"
HAnimJoint1235.name = "r_acromioclavicular"
HAnimJoint1235.center = [-0.0836,1.4281,-0.0401]
HAnimSegment1236 = x3d.HAnimSegment()
HAnimSegment1236.DEF = "hanim_r_scapula"
HAnimSegment1236.name = "r_scapula"
Transform1237 = x3d.Transform()
Transform1237.translation = [-0.0836,1.4281,-0.0401]
Shape1238 = x3d.Shape()
Shape1238.USE = "HAnimJointShape"

Transform1237.children.append(Shape1238)

HAnimSegment1236.children.append(Transform1237)
Shape1239 = x3d.Shape()
LineSet1240 = x3d.LineSet()
LineSet1240.vertexCount = [2]
Coordinate1241 = x3d.Coordinate()

LineSet1240.coord = Coordinate1241
""" from r_acromioclavicular to r_shoulder """
ColorRGBA1242 = x3d.ColorRGBA()
ColorRGBA1242.USE = "HAnimSegmentLineColorRGBA"

LineSet1240.color = ColorRGBA1242

Shape1239.geometry = LineSet1240

HAnimSegment1236.children.append(Shape1239)
HAnimSite1243 = x3d.HAnimSite()
HAnimSite1243.DEF = "hanim_r_bideltoid_pt"
HAnimSite1243.name = "r_bideltoid_pt"
HAnimSite1243.translation = [0,1,0]
TouchSensor1244 = x3d.TouchSensor()
TouchSensor1244.description = "HAnimSite r_bideltoid_pt"

HAnimSite1243.children.append(TouchSensor1244)
Shape1245 = x3d.Shape()
Shape1245.USE = "HAnimSiteShape"

HAnimSite1243.children.append(Shape1245)

HAnimSegment1236.children.append(HAnimSite1243)
HAnimSite1246 = x3d.HAnimSite()
HAnimSite1246.DEF = "hanim_r_humeral_lateral_epicondyles_pt"
HAnimSite1246.name = "r_humeral_lateral_epicondyles_pt"
HAnimSite1246.translation = [-0.2224,1.1517,-0.1033]
TouchSensor1247 = x3d.TouchSensor()
TouchSensor1247.description = "HAnimSite r_humeral_lateral_epicondyles_pt"

HAnimSite1246.children.append(TouchSensor1247)
Shape1248 = x3d.Shape()
Shape1248.USE = "HAnimSiteShape"

HAnimSite1246.children.append(Shape1248)

HAnimSegment1236.children.append(HAnimSite1246)

HAnimJoint1235.children.append(HAnimSegment1236)
HAnimJoint1249 = x3d.HAnimJoint()
HAnimJoint1249.DEF = "hanim_r_shoulder"
HAnimJoint1249.name = "r_shoulder"
HAnimJoint1249.center = [-0.1907,1.4407,-0.0325]
HAnimSegment1250 = x3d.HAnimSegment()
HAnimSegment1250.DEF = "hanim_r_upperarm"
HAnimSegment1250.name = "r_upperarm"
Transform1251 = x3d.Transform()
Transform1251.translation = [-0.1907,1.4407,-0.0325]
Shape1252 = x3d.Shape()
Shape1252.USE = "HAnimJointShape"

Transform1251.children.append(Shape1252)

HAnimSegment1250.children.append(Transform1251)
Shape1253 = x3d.Shape()
LineSet1254 = x3d.LineSet()
LineSet1254.vertexCount = [2]
Coordinate1255 = x3d.Coordinate()

LineSet1254.coord = Coordinate1255
""" from r_shoulder to r_elbow """
ColorRGBA1256 = x3d.ColorRGBA()
ColorRGBA1256.USE = "HAnimSegmentLineColorRGBA"

LineSet1254.color = ColorRGBA1256

Shape1253.geometry = LineSet1254

HAnimSegment1250.children.append(Shape1253)
HAnimSite1257 = x3d.HAnimSite()
HAnimSite1257.DEF = "hanim_r_humeral_medial_epicondyles_pt"
HAnimSite1257.name = "r_humeral_medial_epicondyles_pt"
HAnimSite1257.translation = [-0.1680,1.1298,-0.1062]
TouchSensor1258 = x3d.TouchSensor()
TouchSensor1258.description = "HAnimSite r_humeral_medial_epicondyles_pt"

HAnimSite1257.children.append(TouchSensor1258)
Shape1259 = x3d.Shape()
Shape1259.USE = "HAnimSiteShape"

HAnimSite1257.children.append(Shape1259)

HAnimSegment1250.children.append(HAnimSite1257)
HAnimSite1260 = x3d.HAnimSite()
HAnimSite1260.DEF = "hanim_r_olecranon_pt"
HAnimSite1260.name = "r_olecranon_pt"
HAnimSite1260.translation = [-0.1907,1.1405,-0.1065]
TouchSensor1261 = x3d.TouchSensor()
TouchSensor1261.description = "HAnimSite r_olecranon_pt"

HAnimSite1260.children.append(TouchSensor1261)
Shape1262 = x3d.Shape()
Shape1262.USE = "HAnimSiteShape"

HAnimSite1260.children.append(Shape1262)

HAnimSegment1250.children.append(HAnimSite1260)
HAnimSite1263 = x3d.HAnimSite()
HAnimSite1263.DEF = "hanim_r_radial_styloid_pt"
HAnimSite1263.name = "r_radial_styloid_pt"
HAnimSite1263.translation = [-0.1884,0.8676,-0.0360]
TouchSensor1264 = x3d.TouchSensor()
TouchSensor1264.description = "HAnimSite r_radial_styloid_pt"

HAnimSite1263.children.append(TouchSensor1264)
Shape1265 = x3d.Shape()
Shape1265.USE = "HAnimSiteShape"

HAnimSite1263.children.append(Shape1265)

HAnimSegment1250.children.append(HAnimSite1263)
HAnimSite1266 = x3d.HAnimSite()
HAnimSite1266.DEF = "hanim_r_radiale_pt"
HAnimSite1266.name = "r_radiale_pt"
HAnimSite1266.translation = [-0.2130,1.1305,-0.1091]
TouchSensor1267 = x3d.TouchSensor()
TouchSensor1267.description = "HAnimSite r_radiale_pt"

HAnimSite1266.children.append(TouchSensor1267)
Shape1268 = x3d.Shape()
Shape1268.USE = "HAnimSiteShape"

HAnimSite1266.children.append(Shape1268)

HAnimSegment1250.children.append(HAnimSite1266)

HAnimJoint1249.children.append(HAnimSegment1250)
HAnimJoint1269 = x3d.HAnimJoint()
HAnimJoint1269.DEF = "hanim_r_elbow"
HAnimJoint1269.name = "r_elbow"
HAnimJoint1269.center = [-0.1949,1.1388,-0.0620]
HAnimSegment1270 = x3d.HAnimSegment()
HAnimSegment1270.DEF = "hanim_r_forearm"
HAnimSegment1270.name = "r_forearm"
Transform1271 = x3d.Transform()
Transform1271.translation = [-0.1949,1.1388,-0.0620]
Shape1272 = x3d.Shape()
Shape1272.USE = "HAnimJointShape"

Transform1271.children.append(Shape1272)

HAnimSegment1270.children.append(Transform1271)
Shape1273 = x3d.Shape()
LineSet1274 = x3d.LineSet()
LineSet1274.vertexCount = [2]
Coordinate1275 = x3d.Coordinate()

LineSet1274.coord = Coordinate1275
""" from r_elbow to r_radiocarpal """
ColorRGBA1276 = x3d.ColorRGBA()
ColorRGBA1276.USE = "HAnimSegmentLineColorRGBA"

LineSet1274.color = ColorRGBA1276

Shape1273.geometry = LineSet1274

HAnimSegment1270.children.append(Shape1273)
HAnimSite1277 = x3d.HAnimSite()
HAnimSite1277.DEF = "hanim_r_ulnar_styloid_pt"
HAnimSite1277.name = "r_ulnar_styloid_pt"
HAnimSite1277.translation = [-0.2117,0.8562,-0.0584]
TouchSensor1278 = x3d.TouchSensor()
TouchSensor1278.description = "HAnimSite r_ulnar_styloid_pt"

HAnimSite1277.children.append(TouchSensor1278)
Shape1279 = x3d.Shape()
Shape1279.USE = "HAnimSiteShape"

HAnimSite1277.children.append(Shape1279)

HAnimSegment1270.children.append(HAnimSite1277)

HAnimJoint1269.children.append(HAnimSegment1270)
HAnimJoint1280 = x3d.HAnimJoint()
HAnimJoint1280.DEF = "hanim_r_radiocarpal"
HAnimJoint1280.name = "r_radiocarpal"
HAnimJoint1280.center = [-0.1959,0.8694,-0.0521]
HAnimSegment1281 = x3d.HAnimSegment()
HAnimSegment1281.DEF = "hanim_r_carpal"
HAnimSegment1281.name = "r_carpal"
Transform1282 = x3d.Transform()
Transform1282.translation = [-0.1959,0.8694,-0.0521]
Shape1283 = x3d.Shape()
Shape1283.USE = "HAnimJointShape"

Transform1282.children.append(Shape1283)

HAnimSegment1281.children.append(Transform1282)
Shape1284 = x3d.Shape()
LineSet1285 = x3d.LineSet()
LineSet1285.vertexCount = [2]
Coordinate1286 = x3d.Coordinate()

LineSet1285.coord = Coordinate1286
""" from r_radiocarpal to r_midcarpal_1 """
ColorRGBA1287 = x3d.ColorRGBA()
ColorRGBA1287.USE = "HAnimSegmentLineColorRGBA"

LineSet1285.color = ColorRGBA1287

Shape1284.geometry = LineSet1285

HAnimSegment1281.children.append(Shape1284)
Shape1288 = x3d.Shape()
LineSet1289 = x3d.LineSet()
LineSet1289.vertexCount = [2]
Coordinate1290 = x3d.Coordinate()

LineSet1289.coord = Coordinate1290
""" from r_radiocarpal to r_midcarpal_2 """
ColorRGBA1291 = x3d.ColorRGBA()
ColorRGBA1291.USE = "HAnimSegmentLineColorRGBA"

LineSet1289.color = ColorRGBA1291

Shape1288.geometry = LineSet1289

HAnimSegment1281.children.append(Shape1288)
Shape1292 = x3d.Shape()
LineSet1293 = x3d.LineSet()
LineSet1293.vertexCount = [2]
Coordinate1294 = x3d.Coordinate()

LineSet1293.coord = Coordinate1294
""" from r_radiocarpal to r_midcarpal_3 """
ColorRGBA1295 = x3d.ColorRGBA()
ColorRGBA1295.USE = "HAnimSegmentLineColorRGBA"

LineSet1293.color = ColorRGBA1295

Shape1292.geometry = LineSet1293

HAnimSegment1281.children.append(Shape1292)
Shape1296 = x3d.Shape()
LineSet1297 = x3d.LineSet()
LineSet1297.vertexCount = [2]
Coordinate1298 = x3d.Coordinate()

LineSet1297.coord = Coordinate1298
""" from r_radiocarpal to r_midcarpal_4_5 """
ColorRGBA1299 = x3d.ColorRGBA()
ColorRGBA1299.USE = "HAnimSegmentLineColorRGBA"

LineSet1297.color = ColorRGBA1299

Shape1296.geometry = LineSet1297

HAnimSegment1281.children.append(Shape1296)

HAnimJoint1280.children.append(HAnimSegment1281)
HAnimJoint1300 = x3d.HAnimJoint()
HAnimJoint1300.DEF = "hanim_r_midcarpal_1"
HAnimJoint1300.name = "r_midcarpal_1"
HAnimJoint1300.center = [0,1,0]
HAnimSegment1301 = x3d.HAnimSegment()
HAnimSegment1301.DEF = "hanim_r_trapezium"
HAnimSegment1301.name = "r_trapezium"
Transform1302 = x3d.Transform()
Transform1302.translation = [0,1,0]
Shape1303 = x3d.Shape()
Shape1303.USE = "HAnimJointShape"

Transform1302.children.append(Shape1303)

HAnimSegment1301.children.append(Transform1302)
Shape1304 = x3d.Shape()
LineSet1305 = x3d.LineSet()
LineSet1305.vertexCount = [1]
Coordinate1306 = x3d.Coordinate()

LineSet1305.coord = Coordinate1306
""" from r_midcarpal_1 to r_carpometacarpal_1 """
ColorRGBA1307 = x3d.ColorRGBA()
ColorRGBA1307.USE = "HAnimSegmentLineColorRGBA"

LineSet1305.color = ColorRGBA1307

Shape1304.geometry = LineSet1305

HAnimSegment1301.children.append(Shape1304)

HAnimJoint1300.children.append(HAnimSegment1301)
HAnimJoint1308 = x3d.HAnimJoint()
HAnimJoint1308.DEF = "hanim_r_carpometacarpal_1"
HAnimJoint1308.name = "r_carpometacarpal_1"
HAnimJoint1308.center = [-0.2,0.15,0]
HAnimSegment1309 = x3d.HAnimSegment()
HAnimSegment1309.DEF = "hanim_r_metacarpal_1"
HAnimSegment1309.name = "r_metacarpal_1"
Transform1310 = x3d.Transform()
Transform1310.translation = [-0.2,0.15,0]
Shape1311 = x3d.Shape()
Shape1311.USE = "HAnimJointShape"

Transform1310.children.append(Shape1311)

HAnimSegment1309.children.append(Transform1310)
Shape1312 = x3d.Shape()
LineSet1313 = x3d.LineSet()
LineSet1313.vertexCount = [2]
Coordinate1314 = x3d.Coordinate()

LineSet1313.coord = Coordinate1314
""" from r_carpometacarpal_1 to r_metacarpophalangeal_1 """
ColorRGBA1315 = x3d.ColorRGBA()
ColorRGBA1315.USE = "HAnimSegmentLineColorRGBA"

LineSet1313.color = ColorRGBA1315

Shape1312.geometry = LineSet1313

HAnimSegment1309.children.append(Shape1312)

HAnimJoint1308.children.append(HAnimSegment1309)
HAnimJoint1316 = x3d.HAnimJoint()
HAnimJoint1316.DEF = "hanim_r_metacarpophalangeal_1"
HAnimJoint1316.name = "r_metacarpophalangeal_1"
HAnimJoint1316.center = [-0.3,0.3,0]
HAnimSegment1317 = x3d.HAnimSegment()
HAnimSegment1317.DEF = "hanim_r_carpal_proximal_phalanx_1"
HAnimSegment1317.name = "r_carpal_proximal_phalanx_1"
Transform1318 = x3d.Transform()
Transform1318.translation = [-0.3,0.3,0]
Shape1319 = x3d.Shape()
Shape1319.USE = "HAnimJointShape"

Transform1318.children.append(Shape1319)

HAnimSegment1317.children.append(Transform1318)
Shape1320 = x3d.Shape()
LineSet1321 = x3d.LineSet()
LineSet1321.vertexCount = [2]
Coordinate1322 = x3d.Coordinate()

LineSet1321.coord = Coordinate1322
""" from r_metacarpophalangeal_1 to r_carpal_interphalangeal_1 """
ColorRGBA1323 = x3d.ColorRGBA()
ColorRGBA1323.USE = "HAnimSegmentLineColorRGBA"

LineSet1321.color = ColorRGBA1323

Shape1320.geometry = LineSet1321

HAnimSegment1317.children.append(Shape1320)
HAnimSite1324 = x3d.HAnimSite()
HAnimSite1324.DEF = "hanim_r_carpal_distal_phalanx_1_tip"
HAnimSite1324.name = "r_carpal_distal_phalanx_1_tip"
HAnimSite1324.translation = [-0.35,0.4,0]
TouchSensor1325 = x3d.TouchSensor()
TouchSensor1325.description = "HAnimSite r_carpal_distal_phalanx_1_tip"

HAnimSite1324.children.append(TouchSensor1325)
Shape1326 = x3d.Shape()
Shape1326.USE = "HAnimSiteShape"

HAnimSite1324.children.append(Shape1326)

HAnimSegment1317.children.append(HAnimSite1324)

HAnimJoint1316.children.append(HAnimSegment1317)
HAnimJoint1327 = x3d.HAnimJoint()
HAnimJoint1327.DEF = "hanim_r_carpal_interphalangeal_1"
HAnimJoint1327.name = "r_carpal_interphalangeal_1"
HAnimJoint1327.center = [-0.35,0.4,0]

HAnimJoint1316.children.append(HAnimJoint1327)

HAnimJoint1308.children.append(HAnimJoint1316)

HAnimJoint1300.children.append(HAnimJoint1308)

HAnimJoint1280.children.append(HAnimJoint1300)
HAnimJoint1328 = x3d.HAnimJoint()
HAnimJoint1328.DEF = "hanim_r_midcarpal_2"
HAnimJoint1328.name = "r_midcarpal_2"
HAnimJoint1328.center = [0,1,0]
HAnimSegment1329 = x3d.HAnimSegment()
HAnimSegment1329.DEF = "hanim_r_trapezoid"
HAnimSegment1329.name = "r_trapezoid"
Transform1330 = x3d.Transform()
Transform1330.translation = [0,1,0]
Shape1331 = x3d.Shape()
Shape1331.USE = "HAnimJointShape"

Transform1330.children.append(Shape1331)

HAnimSegment1329.children.append(Transform1330)
Shape1332 = x3d.Shape()
LineSet1333 = x3d.LineSet()
LineSet1333.vertexCount = [1]
Coordinate1334 = x3d.Coordinate()

LineSet1333.coord = Coordinate1334
""" from r_midcarpal_2 to r_carpometacarpal_2 """
ColorRGBA1335 = x3d.ColorRGBA()
ColorRGBA1335.USE = "HAnimSegmentLineColorRGBA"

LineSet1333.color = ColorRGBA1335

Shape1332.geometry = LineSet1333

HAnimSegment1329.children.append(Shape1332)
HAnimSite1336 = x3d.HAnimSite()
HAnimSite1336.DEF = "hanim_r_metacarpal_phalanx_2_pt"
HAnimSite1336.name = "r_metacarpal_phalanx_2_pt"
HAnimSite1336.translation = [-0.1977,0.8169,-0.0177]
TouchSensor1337 = x3d.TouchSensor()
TouchSensor1337.description = "HAnimSite r_metacarpal_phalanx_2_pt"

HAnimSite1336.children.append(TouchSensor1337)
Shape1338 = x3d.Shape()
Shape1338.USE = "HAnimSiteShape"

HAnimSite1336.children.append(Shape1338)

HAnimSegment1329.children.append(HAnimSite1336)

HAnimJoint1328.children.append(HAnimSegment1329)
HAnimJoint1339 = x3d.HAnimJoint()
HAnimJoint1339.DEF = "hanim_r_carpometacarpal_2"
HAnimJoint1339.name = "r_carpometacarpal_2"
HAnimJoint1339.center = [-0.1,0.2,0]
HAnimSegment1340 = x3d.HAnimSegment()
HAnimSegment1340.DEF = "hanim_r_metacarpal_2"
HAnimSegment1340.name = "r_metacarpal_2"
Transform1341 = x3d.Transform()
Transform1341.translation = [-0.1,0.2,0]
Shape1342 = x3d.Shape()
Shape1342.USE = "HAnimJointShape"

Transform1341.children.append(Shape1342)

HAnimSegment1340.children.append(Transform1341)
Shape1343 = x3d.Shape()
LineSet1344 = x3d.LineSet()
LineSet1344.vertexCount = [2]
Coordinate1345 = x3d.Coordinate()

LineSet1344.coord = Coordinate1345
""" from r_carpometacarpal_2 to r_metacarpophalangeal_2 """
ColorRGBA1346 = x3d.ColorRGBA()
ColorRGBA1346.USE = "HAnimSegmentLineColorRGBA"

LineSet1344.color = ColorRGBA1346

Shape1343.geometry = LineSet1344

HAnimSegment1340.children.append(Shape1343)

HAnimJoint1339.children.append(HAnimSegment1340)
HAnimJoint1347 = x3d.HAnimJoint()
HAnimJoint1347.DEF = "hanim_r_metacarpophalangeal_2"
HAnimJoint1347.name = "r_metacarpophalangeal_2"
HAnimJoint1347.center = [-0.15,0.5,0]
HAnimSegment1348 = x3d.HAnimSegment()
HAnimSegment1348.DEF = "hanim_r_carpal_proximal_phalanx_2"
HAnimSegment1348.name = "r_carpal_proximal_phalanx_2"
Transform1349 = x3d.Transform()
Transform1349.translation = [-0.15,0.5,0]
Shape1350 = x3d.Shape()
Shape1350.USE = "HAnimJointShape"

Transform1349.children.append(Shape1350)

HAnimSegment1348.children.append(Transform1349)
Shape1351 = x3d.Shape()
LineSet1352 = x3d.LineSet()
LineSet1352.vertexCount = [2]
Coordinate1353 = x3d.Coordinate()

LineSet1352.coord = Coordinate1353
""" from r_metacarpophalangeal_2 to r_carpal_proximal_interphalangeal_2 """
ColorRGBA1354 = x3d.ColorRGBA()
ColorRGBA1354.USE = "HAnimSegmentLineColorRGBA"

LineSet1352.color = ColorRGBA1354

Shape1351.geometry = LineSet1352

HAnimSegment1348.children.append(Shape1351)

HAnimJoint1347.children.append(HAnimSegment1348)
HAnimJoint1355 = x3d.HAnimJoint()
HAnimJoint1355.DEF = "hanim_r_carpal_proximal_interphalangeal_2"
HAnimJoint1355.name = "r_carpal_proximal_interphalangeal_2"
HAnimJoint1355.center = [-0.2,0.7,0]
HAnimSegment1356 = x3d.HAnimSegment()
HAnimSegment1356.DEF = "hanim_r_carpal_middle_phalanx_2"
HAnimSegment1356.name = "r_carpal_middle_phalanx_2"
Transform1357 = x3d.Transform()
Transform1357.translation = [-0.2,0.7,0]
Shape1358 = x3d.Shape()
Shape1358.USE = "HAnimJointShape"

Transform1357.children.append(Shape1358)

HAnimSegment1356.children.append(Transform1357)
Shape1359 = x3d.Shape()
LineSet1360 = x3d.LineSet()
LineSet1360.vertexCount = [2]
Coordinate1361 = x3d.Coordinate()

LineSet1360.coord = Coordinate1361
""" from r_carpal_proximal_interphalangeal_2 to r_carpal_distal_interphalangeal_2 """
ColorRGBA1362 = x3d.ColorRGBA()
ColorRGBA1362.USE = "HAnimSegmentLineColorRGBA"

LineSet1360.color = ColorRGBA1362

Shape1359.geometry = LineSet1360

HAnimSegment1356.children.append(Shape1359)
HAnimSite1363 = x3d.HAnimSite()
HAnimSite1363.DEF = "hanim_r_carpal_distal_phalanx_2_tip"
HAnimSite1363.name = "r_carpal_distal_phalanx_2_tip"
HAnimSite1363.translation = [-0.24,0.87,0]
TouchSensor1364 = x3d.TouchSensor()
TouchSensor1364.description = "HAnimSite r_carpal_distal_phalanx_2_tip"

HAnimSite1363.children.append(TouchSensor1364)
Shape1365 = x3d.Shape()
Shape1365.USE = "HAnimSiteShape"

HAnimSite1363.children.append(Shape1365)

HAnimSegment1356.children.append(HAnimSite1363)
HAnimSite1366 = x3d.HAnimSite()
HAnimSite1366.DEF = "hanim_r_dactylion_pt"
HAnimSite1366.name = "r_dactylion_pt"
HAnimSite1366.translation = [-0.1941,0.6772,-0.0423]
TouchSensor1367 = x3d.TouchSensor()
TouchSensor1367.description = "HAnimSite r_dactylion_pt"

HAnimSite1366.children.append(TouchSensor1367)
Shape1368 = x3d.Shape()
Shape1368.USE = "HAnimSiteShape"

HAnimSite1366.children.append(Shape1368)

HAnimSegment1356.children.append(HAnimSite1366)

HAnimJoint1355.children.append(HAnimSegment1356)
HAnimJoint1369 = x3d.HAnimJoint()
HAnimJoint1369.DEF = "hanim_r_carpal_distal_interphalangeal_2"
HAnimJoint1369.name = "r_carpal_distal_interphalangeal_2"
HAnimJoint1369.center = [-0.24,0.87,0]

HAnimJoint1355.children.append(HAnimJoint1369)

HAnimJoint1347.children.append(HAnimJoint1355)

HAnimJoint1339.children.append(HAnimJoint1347)

HAnimJoint1328.children.append(HAnimJoint1339)

HAnimJoint1280.children.append(HAnimJoint1328)
HAnimJoint1370 = x3d.HAnimJoint()
HAnimJoint1370.DEF = "hanim_r_midcarpal_3"
HAnimJoint1370.name = "r_midcarpal_3"
HAnimJoint1370.center = [0.0,0.07,0]
HAnimSegment1371 = x3d.HAnimSegment()
HAnimSegment1371.DEF = "hanim_r_capitate"
HAnimSegment1371.name = "r_capitate"
Transform1372 = x3d.Transform()
Transform1372.translation = [0.0,0.07,0]
Shape1373 = x3d.Shape()
Shape1373.USE = "HAnimJointShape"

Transform1372.children.append(Shape1373)

HAnimSegment1371.children.append(Transform1372)
Shape1374 = x3d.Shape()
LineSet1375 = x3d.LineSet()
LineSet1375.vertexCount = [2]
Coordinate1376 = x3d.Coordinate()

LineSet1375.coord = Coordinate1376
""" from r_midcarpal_3 to r_carpometacarpal_3 """
ColorRGBA1377 = x3d.ColorRGBA()
ColorRGBA1377.USE = "HAnimSegmentLineColorRGBA"

LineSet1375.color = ColorRGBA1377

Shape1374.geometry = LineSet1375

HAnimSegment1371.children.append(Shape1374)
HAnimSite1378 = x3d.HAnimSite()
HAnimSite1378.DEF = "hanim_r_metacarpal_phalanx_3_pt"
HAnimSite1378.name = "r_metacarpal_phalanx_3_pt"
HAnimSite1378.translation = [0,1,0]
TouchSensor1379 = x3d.TouchSensor()
TouchSensor1379.description = "HAnimSite r_metacarpal_phalanx_3_pt"

HAnimSite1378.children.append(TouchSensor1379)
Shape1380 = x3d.Shape()
Shape1380.USE = "HAnimSiteShape"

HAnimSite1378.children.append(Shape1380)

HAnimSegment1371.children.append(HAnimSite1378)

HAnimJoint1370.children.append(HAnimSegment1371)
HAnimJoint1381 = x3d.HAnimJoint()
HAnimJoint1381.DEF = "hanim_r_carpometacarpal_3"
HAnimJoint1381.name = "r_carpometacarpal_3"
HAnimJoint1381.center = [0.0,0.2,0]
HAnimSegment1382 = x3d.HAnimSegment()
HAnimSegment1382.DEF = "hanim_r_metacarpal_3"
HAnimSegment1382.name = "r_metacarpal_3"
Transform1383 = x3d.Transform()
Transform1383.translation = [0.0,0.2,0]
Shape1384 = x3d.Shape()
Shape1384.USE = "HAnimJointShape"

Transform1383.children.append(Shape1384)

HAnimSegment1382.children.append(Transform1383)
Shape1385 = x3d.Shape()
LineSet1386 = x3d.LineSet()
LineSet1386.vertexCount = [2]
Coordinate1387 = x3d.Coordinate()

LineSet1386.coord = Coordinate1387
""" from r_carpometacarpal_3 to r_metacarpophalangeal_3 """
ColorRGBA1388 = x3d.ColorRGBA()
ColorRGBA1388.USE = "HAnimSegmentLineColorRGBA"

LineSet1386.color = ColorRGBA1388

Shape1385.geometry = LineSet1386

HAnimSegment1382.children.append(Shape1385)

HAnimJoint1381.children.append(HAnimSegment1382)
HAnimJoint1389 = x3d.HAnimJoint()
HAnimJoint1389.DEF = "hanim_r_metacarpophalangeal_3"
HAnimJoint1389.name = "r_metacarpophalangeal_3"
HAnimJoint1389.center = [-0.03,0.5,0]
HAnimSegment1390 = x3d.HAnimSegment()
HAnimSegment1390.DEF = "hanim_r_carpal_proximal_phalanx_3"
HAnimSegment1390.name = "r_carpal_proximal_phalanx_3"
Transform1391 = x3d.Transform()
Transform1391.translation = [-0.03,0.5,0]
Shape1392 = x3d.Shape()
Shape1392.USE = "HAnimJointShape"

Transform1391.children.append(Shape1392)

HAnimSegment1390.children.append(Transform1391)
Shape1393 = x3d.Shape()
LineSet1394 = x3d.LineSet()
LineSet1394.vertexCount = [2]
Coordinate1395 = x3d.Coordinate()

LineSet1394.coord = Coordinate1395
""" from r_metacarpophalangeal_3 to r_carpal_proximal_interphalangeal_3 """
ColorRGBA1396 = x3d.ColorRGBA()
ColorRGBA1396.USE = "HAnimSegmentLineColorRGBA"

LineSet1394.color = ColorRGBA1396

Shape1393.geometry = LineSet1394

HAnimSegment1390.children.append(Shape1393)

HAnimJoint1389.children.append(HAnimSegment1390)
HAnimJoint1397 = x3d.HAnimJoint()
HAnimJoint1397.DEF = "hanim_r_carpal_proximal_interphalangeal_3"
HAnimJoint1397.name = "r_carpal_proximal_interphalangeal_3"
HAnimJoint1397.center = [-0.05,0.75,0]
HAnimSegment1398 = x3d.HAnimSegment()
HAnimSegment1398.DEF = "hanim_r_carpal_middle_phalanx_3"
HAnimSegment1398.name = "r_carpal_middle_phalanx_3"
Transform1399 = x3d.Transform()
Transform1399.translation = [-0.05,0.75,0]
Shape1400 = x3d.Shape()
Shape1400.USE = "HAnimJointShape"

Transform1399.children.append(Shape1400)

HAnimSegment1398.children.append(Transform1399)
Shape1401 = x3d.Shape()
LineSet1402 = x3d.LineSet()
LineSet1402.vertexCount = [2]
Coordinate1403 = x3d.Coordinate()

LineSet1402.coord = Coordinate1403
""" from r_carpal_proximal_interphalangeal_3 to r_carpal_distal_interphalangeal_3 """
ColorRGBA1404 = x3d.ColorRGBA()
ColorRGBA1404.USE = "HAnimSegmentLineColorRGBA"

LineSet1402.color = ColorRGBA1404

Shape1401.geometry = LineSet1402

HAnimSegment1398.children.append(Shape1401)
HAnimSite1405 = x3d.HAnimSite()
HAnimSite1405.DEF = "hanim_r_carpal_distal_phalanx_3_tip"
HAnimSite1405.name = "r_carpal_distal_phalanx_3_tip"
HAnimSite1405.translation = [-0.08,0.96,0]
TouchSensor1406 = x3d.TouchSensor()
TouchSensor1406.description = "HAnimSite r_carpal_distal_phalanx_3_tip"

HAnimSite1405.children.append(TouchSensor1406)
Shape1407 = x3d.Shape()
Shape1407.USE = "HAnimSiteShape"

HAnimSite1405.children.append(Shape1407)

HAnimSegment1398.children.append(HAnimSite1405)

HAnimJoint1397.children.append(HAnimSegment1398)
HAnimJoint1408 = x3d.HAnimJoint()
HAnimJoint1408.DEF = "hanim_r_carpal_distal_interphalangeal_3"
HAnimJoint1408.name = "r_carpal_distal_interphalangeal_3"
HAnimJoint1408.center = [-0.08,0.96,0]

HAnimJoint1397.children.append(HAnimJoint1408)

HAnimJoint1389.children.append(HAnimJoint1397)

HAnimJoint1381.children.append(HAnimJoint1389)

HAnimJoint1370.children.append(HAnimJoint1381)

HAnimJoint1280.children.append(HAnimJoint1370)
HAnimJoint1409 = x3d.HAnimJoint()
HAnimJoint1409.DEF = "hanim_r_midcarpal_4_5"
HAnimJoint1409.name = "r_midcarpal_4_5"
HAnimJoint1409.center = [0.1,0.1,0]
HAnimSegment1410 = x3d.HAnimSegment()
HAnimSegment1410.DEF = "hanim_r_hamate"
HAnimSegment1410.name = "r_hamate"
Transform1411 = x3d.Transform()
Transform1411.translation = [0.1,0.1,0]
Shape1412 = x3d.Shape()
Shape1412.USE = "HAnimJointShape"

Transform1411.children.append(Shape1412)

HAnimSegment1410.children.append(Transform1411)
Shape1413 = x3d.Shape()
LineSet1414 = x3d.LineSet()
LineSet1414.vertexCount = [2]
Coordinate1415 = x3d.Coordinate()

LineSet1414.coord = Coordinate1415
""" from r_midcarpal_4_5 to r_carpometacarpal_4 """
ColorRGBA1416 = x3d.ColorRGBA()
ColorRGBA1416.USE = "HAnimSegmentLineColorRGBA"

LineSet1414.color = ColorRGBA1416

Shape1413.geometry = LineSet1414

HAnimSegment1410.children.append(Shape1413)
Shape1417 = x3d.Shape()
LineSet1418 = x3d.LineSet()
LineSet1418.vertexCount = [2]
Coordinate1419 = x3d.Coordinate()

LineSet1418.coord = Coordinate1419
""" from r_midcarpal_4_5 to r_carpometacarpal_5 """
ColorRGBA1420 = x3d.ColorRGBA()
ColorRGBA1420.USE = "HAnimSegmentLineColorRGBA"

LineSet1418.color = ColorRGBA1420

Shape1417.geometry = LineSet1418

HAnimSegment1410.children.append(Shape1417)
HAnimSite1421 = x3d.HAnimSite()
HAnimSite1421.DEF = "hanim_r_metacarpal_phalanx_5_pt"
HAnimSite1421.name = "r_metacarpal_phalanx_5_pt"
HAnimSite1421.translation = [-0.1929,0.7890,-0.1064]
TouchSensor1422 = x3d.TouchSensor()
TouchSensor1422.description = "HAnimSite r_metacarpal_phalanx_5_pt"

HAnimSite1421.children.append(TouchSensor1422)
Shape1423 = x3d.Shape()
Shape1423.USE = "HAnimSiteShape"

HAnimSite1421.children.append(Shape1423)

HAnimSegment1410.children.append(HAnimSite1421)

HAnimJoint1409.children.append(HAnimSegment1410)
HAnimJoint1424 = x3d.HAnimJoint()
HAnimJoint1424.DEF = "hanim_r_carpometacarpal_4"
HAnimJoint1424.name = "r_carpometacarpal_4"
HAnimJoint1424.center = [0.1,0.2,0]
HAnimSegment1425 = x3d.HAnimSegment()
HAnimSegment1425.DEF = "hanim_r_metacarpal_4"
HAnimSegment1425.name = "r_metacarpal_4"
Transform1426 = x3d.Transform()
Transform1426.translation = [0.1,0.2,0]
Shape1427 = x3d.Shape()
Shape1427.USE = "HAnimJointShape"

Transform1426.children.append(Shape1427)

HAnimSegment1425.children.append(Transform1426)
Shape1428 = x3d.Shape()
LineSet1429 = x3d.LineSet()
LineSet1429.vertexCount = [2]
Coordinate1430 = x3d.Coordinate()

LineSet1429.coord = Coordinate1430
""" from r_carpometacarpal_4 to r_metacarpophalangeal_4 """
ColorRGBA1431 = x3d.ColorRGBA()
ColorRGBA1431.USE = "HAnimSegmentLineColorRGBA"

LineSet1429.color = ColorRGBA1431

Shape1428.geometry = LineSet1429

HAnimSegment1425.children.append(Shape1428)

HAnimJoint1424.children.append(HAnimSegment1425)
HAnimJoint1432 = x3d.HAnimJoint()
HAnimJoint1432.DEF = "hanim_r_metacarpophalangeal_4"
HAnimJoint1432.name = "r_metacarpophalangeal_4"
HAnimJoint1432.center = [0.1,0.47,0]
HAnimSegment1433 = x3d.HAnimSegment()
HAnimSegment1433.DEF = "hanim_r_carpal_proximal_phalanx_4"
HAnimSegment1433.name = "r_carpal_proximal_phalanx_4"
Transform1434 = x3d.Transform()
Transform1434.translation = [0.1,0.47,0]
Shape1435 = x3d.Shape()
Shape1435.USE = "HAnimJointShape"

Transform1434.children.append(Shape1435)

HAnimSegment1433.children.append(Transform1434)
Shape1436 = x3d.Shape()
LineSet1437 = x3d.LineSet()
LineSet1437.vertexCount = [2]
Coordinate1438 = x3d.Coordinate()

LineSet1437.coord = Coordinate1438
""" from r_metacarpophalangeal_4 to r_carpal_proximal_interphalangeal_4 """
ColorRGBA1439 = x3d.ColorRGBA()
ColorRGBA1439.USE = "HAnimSegmentLineColorRGBA"

LineSet1437.color = ColorRGBA1439

Shape1436.geometry = LineSet1437

HAnimSegment1433.children.append(Shape1436)

HAnimJoint1432.children.append(HAnimSegment1433)
HAnimJoint1440 = x3d.HAnimJoint()
HAnimJoint1440.DEF = "hanim_r_carpal_proximal_interphalangeal_4"
HAnimJoint1440.name = "r_carpal_proximal_interphalangeal_4"
HAnimJoint1440.center = [0.1,0.7,0]
HAnimSegment1441 = x3d.HAnimSegment()
HAnimSegment1441.DEF = "hanim_r_carpal_middle_phalanx_4"
HAnimSegment1441.name = "r_carpal_middle_phalanx_4"
Transform1442 = x3d.Transform()
Transform1442.translation = [0.1,0.7,0]
Shape1443 = x3d.Shape()
Shape1443.USE = "HAnimJointShape"

Transform1442.children.append(Shape1443)

HAnimSegment1441.children.append(Transform1442)
Shape1444 = x3d.Shape()
LineSet1445 = x3d.LineSet()
LineSet1445.vertexCount = [2]
Coordinate1446 = x3d.Coordinate()

LineSet1445.coord = Coordinate1446
""" from r_carpal_proximal_interphalangeal_4 to r_carpal_distal_interphalangeal_4 """
ColorRGBA1447 = x3d.ColorRGBA()
ColorRGBA1447.USE = "HAnimSegmentLineColorRGBA"

LineSet1445.color = ColorRGBA1447

Shape1444.geometry = LineSet1445

HAnimSegment1441.children.append(Shape1444)
HAnimSite1448 = x3d.HAnimSite()
HAnimSite1448.DEF = "hanim_r_carpal_distal_phalanx_4_tip"
HAnimSite1448.name = "r_carpal_distal_phalanx_4_tip"
HAnimSite1448.translation = [0.1,0.93,0]
TouchSensor1449 = x3d.TouchSensor()
TouchSensor1449.description = "HAnimSite r_carpal_distal_phalanx_4_tip"

HAnimSite1448.children.append(TouchSensor1449)
Shape1450 = x3d.Shape()
Shape1450.USE = "HAnimSiteShape"

HAnimSite1448.children.append(Shape1450)

HAnimSegment1441.children.append(HAnimSite1448)

HAnimJoint1440.children.append(HAnimSegment1441)
HAnimJoint1451 = x3d.HAnimJoint()
HAnimJoint1451.DEF = "hanim_r_carpal_distal_interphalangeal_4"
HAnimJoint1451.name = "r_carpal_distal_interphalangeal_4"
HAnimJoint1451.center = [0.1,0.93,0]

HAnimJoint1440.children.append(HAnimJoint1451)

HAnimJoint1432.children.append(HAnimJoint1440)

HAnimJoint1424.children.append(HAnimJoint1432)

HAnimJoint1409.children.append(HAnimJoint1424)
HAnimJoint1452 = x3d.HAnimJoint()
HAnimJoint1452.DEF = "hanim_r_carpometacarpal_5"
HAnimJoint1452.name = "r_carpometacarpal_5"
HAnimJoint1452.center = [0.15,0.17,0]
HAnimSegment1453 = x3d.HAnimSegment()
HAnimSegment1453.DEF = "hanim_r_metacarpal_5"
HAnimSegment1453.name = "r_metacarpal_5"
Transform1454 = x3d.Transform()
Transform1454.translation = [0.15,0.17,0]
Shape1455 = x3d.Shape()
Shape1455.USE = "HAnimJointShape"

Transform1454.children.append(Shape1455)

HAnimSegment1453.children.append(Transform1454)
Shape1456 = x3d.Shape()
LineSet1457 = x3d.LineSet()
LineSet1457.vertexCount = [2]
Coordinate1458 = x3d.Coordinate()

LineSet1457.coord = Coordinate1458
""" from r_carpometacarpal_5 to r_metacarpophalangeal_5 """
ColorRGBA1459 = x3d.ColorRGBA()
ColorRGBA1459.USE = "HAnimSegmentLineColorRGBA"

LineSet1457.color = ColorRGBA1459

Shape1456.geometry = LineSet1457

HAnimSegment1453.children.append(Shape1456)

HAnimJoint1452.children.append(HAnimSegment1453)
HAnimJoint1460 = x3d.HAnimJoint()
HAnimJoint1460.DEF = "hanim_r_metacarpophalangeal_5"
HAnimJoint1460.name = "r_metacarpophalangeal_5"
HAnimJoint1460.center = [0.2,0.4,0]
HAnimSegment1461 = x3d.HAnimSegment()
HAnimSegment1461.DEF = "hanim_r_carpal_proximal_phalanx_5"
HAnimSegment1461.name = "r_carpal_proximal_phalanx_5"
Transform1462 = x3d.Transform()
Transform1462.translation = [0.2,0.4,0]
Shape1463 = x3d.Shape()
Shape1463.USE = "HAnimJointShape"

Transform1462.children.append(Shape1463)

HAnimSegment1461.children.append(Transform1462)
Shape1464 = x3d.Shape()
LineSet1465 = x3d.LineSet()
LineSet1465.vertexCount = [2]
Coordinate1466 = x3d.Coordinate()

LineSet1465.coord = Coordinate1466
""" from r_metacarpophalangeal_5 to r_carpal_proximal_interphalangeal_5 """
ColorRGBA1467 = x3d.ColorRGBA()
ColorRGBA1467.USE = "HAnimSegmentLineColorRGBA"

LineSet1465.color = ColorRGBA1467

Shape1464.geometry = LineSet1465

HAnimSegment1461.children.append(Shape1464)

HAnimJoint1460.children.append(HAnimSegment1461)
HAnimJoint1468 = x3d.HAnimJoint()
HAnimJoint1468.DEF = "hanim_r_carpal_proximal_interphalangeal_5"
HAnimJoint1468.name = "r_carpal_proximal_interphalangeal_5"
HAnimJoint1468.center = [0.23,0.63,0]
HAnimSegment1469 = x3d.HAnimSegment()
HAnimSegment1469.DEF = "hanim_r_carpal_middle_phalanx_5"
HAnimSegment1469.name = "r_carpal_middle_phalanx_5"
Transform1470 = x3d.Transform()
Transform1470.translation = [0.23,0.63,0]
Shape1471 = x3d.Shape()
Shape1471.USE = "HAnimJointShape"

Transform1470.children.append(Shape1471)

HAnimSegment1469.children.append(Transform1470)
Shape1472 = x3d.Shape()
LineSet1473 = x3d.LineSet()
LineSet1473.vertexCount = [2]
Coordinate1474 = x3d.Coordinate()

LineSet1473.coord = Coordinate1474
""" from r_carpal_proximal_interphalangeal_5 to r_carpal_distal_interphalangeal_5 """
ColorRGBA1475 = x3d.ColorRGBA()
ColorRGBA1475.USE = "HAnimSegmentLineColorRGBA"

LineSet1473.color = ColorRGBA1475

Shape1472.geometry = LineSet1473

HAnimSegment1469.children.append(Shape1472)
HAnimSite1476 = x3d.HAnimSite()
HAnimSite1476.DEF = "hanim_r_carpal_distal_phalanx_5_tip"
HAnimSite1476.name = "r_carpal_distal_phalanx_5_tip"
HAnimSite1476.translation = [0.25,0.79,0]
TouchSensor1477 = x3d.TouchSensor()
TouchSensor1477.description = "HAnimSite r_carpal_distal_phalanx_5_tip"

HAnimSite1476.children.append(TouchSensor1477)
Shape1478 = x3d.Shape()
Shape1478.USE = "HAnimSiteShape"

HAnimSite1476.children.append(Shape1478)

HAnimSegment1469.children.append(HAnimSite1476)

HAnimJoint1468.children.append(HAnimSegment1469)
HAnimJoint1479 = x3d.HAnimJoint()
HAnimJoint1479.DEF = "hanim_r_carpal_distal_interphalangeal_5"
HAnimJoint1479.name = "r_carpal_distal_interphalangeal_5"
HAnimJoint1479.center = [0.25,0.79,0]

HAnimJoint1468.children.append(HAnimJoint1479)

HAnimJoint1460.children.append(HAnimJoint1468)

HAnimJoint1452.children.append(HAnimJoint1460)

HAnimJoint1409.children.append(HAnimJoint1452)

HAnimJoint1280.children.append(HAnimJoint1409)

HAnimJoint1269.children.append(HAnimJoint1280)

HAnimJoint1249.children.append(HAnimJoint1269)

HAnimJoint1235.children.append(HAnimJoint1249)

HAnimJoint1227.children.append(HAnimJoint1235)

HAnimJoint779.children.append(HAnimJoint1227)

HAnimJoint765.children.append(HAnimJoint779)

HAnimJoint757.children.append(HAnimJoint765)

HAnimJoint749.children.append(HAnimJoint757)

HAnimJoint741.children.append(HAnimJoint749)

HAnimJoint730.children.append(HAnimJoint741)

HAnimJoint710.children.append(HAnimJoint730)

HAnimJoint702.children.append(HAnimJoint710)

HAnimJoint694.children.append(HAnimJoint702)

HAnimJoint680.children.append(HAnimJoint694)

HAnimJoint669.children.append(HAnimJoint680)

HAnimJoint661.children.append(HAnimJoint669)

HAnimJoint653.children.append(HAnimJoint661)

HAnimJoint645.children.append(HAnimJoint653)

HAnimJoint628.children.append(HAnimJoint645)

HAnimJoint620.children.append(HAnimJoint628)

HAnimJoint612.children.append(HAnimJoint620)

HAnimJoint43.children.append(HAnimJoint612)

HAnimHumanoid42.joints.append(HAnimJoint43)
HAnimJoint1480 = x3d.HAnimJoint()
HAnimJoint1480.USE = "hanim_humanoid_root"

HAnimHumanoid42.joints.append(HAnimJoint1480)
HAnimSegment1481 = x3d.HAnimSegment()
HAnimSegment1481.USE = "hanim_sacrum"

HAnimHumanoid42.segments.append(HAnimSegment1481)
HAnimSite1482 = x3d.HAnimSite()
HAnimSite1482.USE = "hanim_buttocks_standing_wall_contact_point_pt"

HAnimHumanoid42.sites.append(HAnimSite1482)
HAnimSite1483 = x3d.HAnimSite()
HAnimSite1483.USE = "hanim_crotch_pt"

HAnimHumanoid42.sites.append(HAnimSite1483)
HAnimSite1484 = x3d.HAnimSite()
HAnimSite1484.USE = "hanim_l_asis_pt"

HAnimHumanoid42.sites.append(HAnimSite1484)
HAnimSite1485 = x3d.HAnimSite()
HAnimSite1485.USE = "hanim_l_iliocristale_pt"

HAnimHumanoid42.sites.append(HAnimSite1485)
HAnimSite1486 = x3d.HAnimSite()
HAnimSite1486.USE = "hanim_l_psis_pt"

HAnimHumanoid42.sites.append(HAnimSite1486)
HAnimSite1487 = x3d.HAnimSite()
HAnimSite1487.USE = "hanim_l_trochanterion_pt"

HAnimHumanoid42.sites.append(HAnimSite1487)
HAnimSite1488 = x3d.HAnimSite()
HAnimSite1488.USE = "hanim_r_asis_pt"

HAnimHumanoid42.sites.append(HAnimSite1488)
HAnimSite1489 = x3d.HAnimSite()
HAnimSite1489.USE = "hanim_r_iliocristale_pt"

HAnimHumanoid42.sites.append(HAnimSite1489)
HAnimSite1490 = x3d.HAnimSite()
HAnimSite1490.USE = "hanim_r_psis_pt"

HAnimHumanoid42.sites.append(HAnimSite1490)
HAnimSite1491 = x3d.HAnimSite()
HAnimSite1491.USE = "hanim_r_trochanterion_pt"

HAnimHumanoid42.sites.append(HAnimSite1491)
HAnimSite1492 = x3d.HAnimSite()
HAnimSite1492.USE = "hanim_navel_pt"

HAnimHumanoid42.sites.append(HAnimSite1492)
HAnimSite1493 = x3d.HAnimSite()
HAnimSite1493.USE = "hanim_waist_preferred_anterior_pt"

HAnimHumanoid42.sites.append(HAnimSite1493)
HAnimSite1494 = x3d.HAnimSite()
HAnimSite1494.USE = "hanim_waist_preferred_posterior_pt"

HAnimHumanoid42.sites.append(HAnimSite1494)
HAnimJoint1495 = x3d.HAnimJoint()
HAnimJoint1495.USE = "hanim_sacroiliac"

HAnimHumanoid42.joints.append(HAnimJoint1495)
HAnimSegment1496 = x3d.HAnimSegment()
HAnimSegment1496.USE = "hanim_pelvis"

HAnimHumanoid42.segments.append(HAnimSegment1496)
HAnimSite1497 = x3d.HAnimSite()
HAnimSite1497.USE = "hanim_l_femoral_lateral_epicondyles_pt"

HAnimHumanoid42.sites.append(HAnimSite1497)
HAnimSite1498 = x3d.HAnimSite()
HAnimSite1498.USE = "hanim_l_femoral_medial_epicondyles_pt"

HAnimHumanoid42.sites.append(HAnimSite1498)
HAnimSite1499 = x3d.HAnimSite()
HAnimSite1499.USE = "hanim_l_knee_crease_pt"

HAnimHumanoid42.sites.append(HAnimSite1499)
HAnimSite1500 = x3d.HAnimSite()
HAnimSite1500.USE = "hanim_l_suprapatella_pt"

HAnimHumanoid42.sites.append(HAnimSite1500)
HAnimSite1501 = x3d.HAnimSite()
HAnimSite1501.USE = "hanim_r_femoral_lateral_epicondyles_pt"

HAnimHumanoid42.sites.append(HAnimSite1501)
HAnimSite1502 = x3d.HAnimSite()
HAnimSite1502.USE = "hanim_r_femoral_medial_epicondyles_pt"

HAnimHumanoid42.sites.append(HAnimSite1502)
HAnimSite1503 = x3d.HAnimSite()
HAnimSite1503.USE = "hanim_r_knee_crease_pt"

HAnimHumanoid42.sites.append(HAnimSite1503)
HAnimSite1504 = x3d.HAnimSite()
HAnimSite1504.USE = "hanim_r_suprapatella_pt"

HAnimHumanoid42.sites.append(HAnimSite1504)
HAnimJoint1505 = x3d.HAnimJoint()
HAnimJoint1505.USE = "hanim_l_hip"

HAnimHumanoid42.joints.append(HAnimJoint1505)
HAnimSegment1506 = x3d.HAnimSegment()
HAnimSegment1506.USE = "hanim_l_thigh"

HAnimHumanoid42.segments.append(HAnimSegment1506)
HAnimSite1507 = x3d.HAnimSite()
HAnimSite1507.USE = "hanim_l_lateral_malleolus_pt"

HAnimHumanoid42.sites.append(HAnimSite1507)
HAnimSite1508 = x3d.HAnimSite()
HAnimSite1508.USE = "hanim_l_medial_malleolus_pt"

HAnimHumanoid42.sites.append(HAnimSite1508)
HAnimSite1509 = x3d.HAnimSite()
HAnimSite1509.USE = "hanim_l_tibiale_pt"

HAnimHumanoid42.sites.append(HAnimSite1509)
HAnimJoint1510 = x3d.HAnimJoint()
HAnimJoint1510.USE = "hanim_l_knee"

HAnimHumanoid42.joints.append(HAnimJoint1510)
HAnimSegment1511 = x3d.HAnimSegment()
HAnimSegment1511.USE = "hanim_l_calf"

HAnimHumanoid42.segments.append(HAnimSegment1511)
HAnimSite1512 = x3d.HAnimSite()
HAnimSite1512.USE = "hanim_l_calcaneus_posterior_pt"

HAnimHumanoid42.sites.append(HAnimSite1512)
HAnimSite1513 = x3d.HAnimSite()
HAnimSite1513.USE = "hanim_l_sphyrion_pt"

HAnimHumanoid42.sites.append(HAnimSite1513)
HAnimJoint1514 = x3d.HAnimJoint()
HAnimJoint1514.USE = "hanim_l_talocrural"

HAnimHumanoid42.joints.append(HAnimJoint1514)
HAnimSegment1515 = x3d.HAnimSegment()
HAnimSegment1515.USE = "hanim_l_talus"

HAnimHumanoid42.segments.append(HAnimSegment1515)
HAnimJoint1516 = x3d.HAnimJoint()
HAnimJoint1516.USE = "hanim_l_talocalcaneonavicular"

HAnimHumanoid42.joints.append(HAnimJoint1516)
HAnimSegment1517 = x3d.HAnimSegment()
HAnimSegment1517.USE = "hanim_l_navicular"

HAnimHumanoid42.segments.append(HAnimSegment1517)
HAnimJoint1518 = x3d.HAnimJoint()
HAnimJoint1518.USE = "hanim_l_cuneonavicular_1"

HAnimHumanoid42.joints.append(HAnimJoint1518)
HAnimSegment1519 = x3d.HAnimSegment()
HAnimSegment1519.USE = "hanim_l_cuneiform_1"

HAnimHumanoid42.segments.append(HAnimSegment1519)
HAnimJoint1520 = x3d.HAnimJoint()
HAnimJoint1520.USE = "hanim_l_tarsometatarsal_1"

HAnimHumanoid42.joints.append(HAnimJoint1520)
HAnimSegment1521 = x3d.HAnimSegment()
HAnimSegment1521.USE = "hanim_l_metatarsal_1"

HAnimHumanoid42.segments.append(HAnimSegment1521)
HAnimSite1522 = x3d.HAnimSite()
HAnimSite1522.USE = "hanim_l_metatarsal_phalanx_1_pt"

HAnimHumanoid42.sites.append(HAnimSite1522)
HAnimJoint1523 = x3d.HAnimJoint()
HAnimJoint1523.USE = "hanim_l_metatarsophalangeal_1"

HAnimHumanoid42.joints.append(HAnimJoint1523)
HAnimSegment1524 = x3d.HAnimSegment()
HAnimSegment1524.USE = "hanim_l_tarsal_proximal_phalanx_1"

HAnimHumanoid42.segments.append(HAnimSegment1524)
HAnimSite1525 = x3d.HAnimSite()
HAnimSite1525.USE = "hanim_l_tarsal_distal_phalanx_1_tip"

HAnimHumanoid42.sites.append(HAnimSite1525)
HAnimJoint1526 = x3d.HAnimJoint()
HAnimJoint1526.USE = "hanim_l_tarsal_interphalangeal_1"

HAnimHumanoid42.joints.append(HAnimJoint1526)
HAnimJoint1527 = x3d.HAnimJoint()
HAnimJoint1527.USE = "hanim_l_cuneonavicular_2"

HAnimHumanoid42.joints.append(HAnimJoint1527)
HAnimSegment1528 = x3d.HAnimSegment()
HAnimSegment1528.USE = "hanim_l_cuneiform_2"

HAnimHumanoid42.segments.append(HAnimSegment1528)
HAnimJoint1529 = x3d.HAnimJoint()
HAnimJoint1529.USE = "hanim_l_tarsometatarsal_2"

HAnimHumanoid42.joints.append(HAnimJoint1529)
HAnimSegment1530 = x3d.HAnimSegment()
HAnimSegment1530.USE = "hanim_l_metatarsal_2"

HAnimHumanoid42.segments.append(HAnimSegment1530)
HAnimJoint1531 = x3d.HAnimJoint()
HAnimJoint1531.USE = "hanim_l_metatarsophalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint1531)
HAnimSegment1532 = x3d.HAnimSegment()
HAnimSegment1532.USE = "hanim_l_tarsal_proximal_phalanx_2"

HAnimHumanoid42.segments.append(HAnimSegment1532)
HAnimJoint1533 = x3d.HAnimJoint()
HAnimJoint1533.USE = "hanim_l_tarsal_proximal_interphalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint1533)
HAnimSegment1534 = x3d.HAnimSegment()
HAnimSegment1534.USE = "hanim_l_tarsal_middle_phalanx_2"

HAnimHumanoid42.segments.append(HAnimSegment1534)
HAnimSite1535 = x3d.HAnimSite()
HAnimSite1535.USE = "hanim_l_tarsal_distal_phalanx_2_tip"

HAnimHumanoid42.sites.append(HAnimSite1535)
HAnimJoint1536 = x3d.HAnimJoint()
HAnimJoint1536.USE = "hanim_l_tarsal_distal_interphalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint1536)
HAnimJoint1537 = x3d.HAnimJoint()
HAnimJoint1537.USE = "hanim_l_cuneonavicular_3"

HAnimHumanoid42.joints.append(HAnimJoint1537)
HAnimSegment1538 = x3d.HAnimSegment()
HAnimSegment1538.USE = "hanim_l_cuneiform_3"

HAnimHumanoid42.segments.append(HAnimSegment1538)
HAnimJoint1539 = x3d.HAnimJoint()
HAnimJoint1539.USE = "hanim_l_tarsometatarsal_3"

HAnimHumanoid42.joints.append(HAnimJoint1539)
HAnimSegment1540 = x3d.HAnimSegment()
HAnimSegment1540.USE = "hanim_l_metatarsal_3"

HAnimHumanoid42.segments.append(HAnimSegment1540)
HAnimJoint1541 = x3d.HAnimJoint()
HAnimJoint1541.USE = "hanim_l_metatarsophalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint1541)
HAnimSegment1542 = x3d.HAnimSegment()
HAnimSegment1542.USE = "hanim_l_tarsal_proximal_phalanx_3"

HAnimHumanoid42.segments.append(HAnimSegment1542)
HAnimJoint1543 = x3d.HAnimJoint()
HAnimJoint1543.USE = "hanim_l_tarsal_proximal_interphalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint1543)
HAnimSegment1544 = x3d.HAnimSegment()
HAnimSegment1544.USE = "hanim_l_tarsal_middle_phalanx_3"

HAnimHumanoid42.segments.append(HAnimSegment1544)
HAnimSite1545 = x3d.HAnimSite()
HAnimSite1545.USE = "hanim_l_tarsal_distal_phalanx_3_tip"

HAnimHumanoid42.sites.append(HAnimSite1545)
HAnimJoint1546 = x3d.HAnimJoint()
HAnimJoint1546.USE = "hanim_l_tarsal_distal_interphalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint1546)
HAnimJoint1547 = x3d.HAnimJoint()
HAnimJoint1547.USE = "hanim_l_calcaneocuboid"

HAnimHumanoid42.joints.append(HAnimJoint1547)
HAnimSegment1548 = x3d.HAnimSegment()
HAnimSegment1548.USE = "hanim_l_calcaneus"

HAnimHumanoid42.segments.append(HAnimSegment1548)
HAnimJoint1549 = x3d.HAnimJoint()
HAnimJoint1549.USE = "hanim_l_transversetarsal"

HAnimHumanoid42.joints.append(HAnimJoint1549)
HAnimSegment1550 = x3d.HAnimSegment()
HAnimSegment1550.USE = "hanim_l_cuboid"

HAnimHumanoid42.segments.append(HAnimSegment1550)
HAnimJoint1551 = x3d.HAnimJoint()
HAnimJoint1551.USE = "hanim_l_tarsometatarsal_4"

HAnimHumanoid42.joints.append(HAnimJoint1551)
HAnimSegment1552 = x3d.HAnimSegment()
HAnimSegment1552.USE = "hanim_l_metatarsal_4"

HAnimHumanoid42.segments.append(HAnimSegment1552)
HAnimJoint1553 = x3d.HAnimJoint()
HAnimJoint1553.USE = "hanim_l_metatarsophalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint1553)
HAnimSegment1554 = x3d.HAnimSegment()
HAnimSegment1554.USE = "hanim_l_tarsal_proximal_phalanx_4"

HAnimHumanoid42.segments.append(HAnimSegment1554)
HAnimJoint1555 = x3d.HAnimJoint()
HAnimJoint1555.USE = "hanim_l_tarsal_proximal_interphalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint1555)
HAnimSegment1556 = x3d.HAnimSegment()
HAnimSegment1556.USE = "hanim_l_tarsal_middle_phalanx_4"

HAnimHumanoid42.segments.append(HAnimSegment1556)
HAnimSite1557 = x3d.HAnimSite()
HAnimSite1557.USE = "hanim_l_tarsal_distal_phalanx_4_tip"

HAnimHumanoid42.sites.append(HAnimSite1557)
HAnimJoint1558 = x3d.HAnimJoint()
HAnimJoint1558.USE = "hanim_l_tarsal_distal_interphalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint1558)
HAnimJoint1559 = x3d.HAnimJoint()
HAnimJoint1559.USE = "hanim_l_tarsometatarsal_5"

HAnimHumanoid42.joints.append(HAnimJoint1559)
HAnimSegment1560 = x3d.HAnimSegment()
HAnimSegment1560.USE = "hanim_l_metatarsal_5"

HAnimHumanoid42.segments.append(HAnimSegment1560)
HAnimSite1561 = x3d.HAnimSite()
HAnimSite1561.USE = "hanim_l_metatarsal_phalanx_5_pt"

HAnimHumanoid42.sites.append(HAnimSite1561)
HAnimJoint1562 = x3d.HAnimJoint()
HAnimJoint1562.USE = "hanim_l_metatarsophalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint1562)
HAnimSegment1563 = x3d.HAnimSegment()
HAnimSegment1563.USE = "hanim_l_tarsal_proximal_phalanx_5"

HAnimHumanoid42.segments.append(HAnimSegment1563)
HAnimJoint1564 = x3d.HAnimJoint()
HAnimJoint1564.USE = "hanim_l_tarsal_proximal_interphalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint1564)
HAnimSegment1565 = x3d.HAnimSegment()
HAnimSegment1565.USE = "hanim_l_tarsal_middle_phalanx_5"

HAnimHumanoid42.segments.append(HAnimSegment1565)
HAnimSite1566 = x3d.HAnimSite()
HAnimSite1566.USE = "hanim_l_tarsal_distal_phalanx_5_tip"

HAnimHumanoid42.sites.append(HAnimSite1566)
HAnimJoint1567 = x3d.HAnimJoint()
HAnimJoint1567.USE = "hanim_l_tarsal_distal_interphalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint1567)
HAnimJoint1568 = x3d.HAnimJoint()
HAnimJoint1568.USE = "hanim_r_hip"

HAnimHumanoid42.joints.append(HAnimJoint1568)
HAnimSegment1569 = x3d.HAnimSegment()
HAnimSegment1569.USE = "hanim_r_thigh"

HAnimHumanoid42.segments.append(HAnimSegment1569)
HAnimSite1570 = x3d.HAnimSite()
HAnimSite1570.USE = "hanim_r_lateral_malleolus_pt"

HAnimHumanoid42.sites.append(HAnimSite1570)
HAnimSite1571 = x3d.HAnimSite()
HAnimSite1571.USE = "hanim_r_medial_malleolus_pt"

HAnimHumanoid42.sites.append(HAnimSite1571)
HAnimSite1572 = x3d.HAnimSite()
HAnimSite1572.USE = "hanim_r_tibiale_pt"

HAnimHumanoid42.sites.append(HAnimSite1572)
HAnimJoint1573 = x3d.HAnimJoint()
HAnimJoint1573.USE = "hanim_r_knee"

HAnimHumanoid42.joints.append(HAnimJoint1573)
HAnimSegment1574 = x3d.HAnimSegment()
HAnimSegment1574.USE = "hanim_r_calf"

HAnimHumanoid42.segments.append(HAnimSegment1574)
HAnimSite1575 = x3d.HAnimSite()
HAnimSite1575.USE = "hanim_r_calcaneus_posterior_pt"

HAnimHumanoid42.sites.append(HAnimSite1575)
HAnimSite1576 = x3d.HAnimSite()
HAnimSite1576.USE = "hanim_r_sphyrion_pt"

HAnimHumanoid42.sites.append(HAnimSite1576)
HAnimJoint1577 = x3d.HAnimJoint()
HAnimJoint1577.USE = "hanim_r_talocrural"

HAnimHumanoid42.joints.append(HAnimJoint1577)
HAnimSegment1578 = x3d.HAnimSegment()
HAnimSegment1578.USE = "hanim_r_talus"

HAnimHumanoid42.segments.append(HAnimSegment1578)
HAnimJoint1579 = x3d.HAnimJoint()
HAnimJoint1579.USE = "hanim_r_talocalcaneonavicular"

HAnimHumanoid42.joints.append(HAnimJoint1579)
HAnimSegment1580 = x3d.HAnimSegment()
HAnimSegment1580.USE = "hanim_r_navicular"

HAnimHumanoid42.segments.append(HAnimSegment1580)
HAnimJoint1581 = x3d.HAnimJoint()
HAnimJoint1581.USE = "hanim_r_cuneonavicular_1"

HAnimHumanoid42.joints.append(HAnimJoint1581)
HAnimSegment1582 = x3d.HAnimSegment()
HAnimSegment1582.USE = "hanim_r_cuneiform_1"

HAnimHumanoid42.segments.append(HAnimSegment1582)
HAnimJoint1583 = x3d.HAnimJoint()
HAnimJoint1583.USE = "hanim_r_tarsometatarsal_1"

HAnimHumanoid42.joints.append(HAnimJoint1583)
HAnimSegment1584 = x3d.HAnimSegment()
HAnimSegment1584.USE = "hanim_r_metatarsal_1"

HAnimHumanoid42.segments.append(HAnimSegment1584)
HAnimSite1585 = x3d.HAnimSite()
HAnimSite1585.USE = "hanim_r_metatarsal_phalanx_1_pt"

HAnimHumanoid42.sites.append(HAnimSite1585)
HAnimJoint1586 = x3d.HAnimJoint()
HAnimJoint1586.USE = "hanim_r_metatarsophalangeal_1"

HAnimHumanoid42.joints.append(HAnimJoint1586)
HAnimSegment1587 = x3d.HAnimSegment()
HAnimSegment1587.USE = "hanim_r_tarsal_proximal_phalanx_1"

HAnimHumanoid42.segments.append(HAnimSegment1587)
HAnimSite1588 = x3d.HAnimSite()
HAnimSite1588.USE = "hanim_r_tarsal_distal_phalanx_1_tip"

HAnimHumanoid42.sites.append(HAnimSite1588)
HAnimJoint1589 = x3d.HAnimJoint()
HAnimJoint1589.USE = "hanim_r_tarsal_interphalangeal_1"

HAnimHumanoid42.joints.append(HAnimJoint1589)
HAnimJoint1590 = x3d.HAnimJoint()
HAnimJoint1590.USE = "hanim_r_cuneonavicular_2"

HAnimHumanoid42.joints.append(HAnimJoint1590)
HAnimSegment1591 = x3d.HAnimSegment()
HAnimSegment1591.USE = "hanim_r_cuneiform_2"

HAnimHumanoid42.segments.append(HAnimSegment1591)
HAnimJoint1592 = x3d.HAnimJoint()
HAnimJoint1592.USE = "hanim_r_tarsometatarsal_2"

HAnimHumanoid42.joints.append(HAnimJoint1592)
HAnimSegment1593 = x3d.HAnimSegment()
HAnimSegment1593.USE = "hanim_r_metatarsal_2"

HAnimHumanoid42.segments.append(HAnimSegment1593)
HAnimJoint1594 = x3d.HAnimJoint()
HAnimJoint1594.USE = "hanim_r_metatarsophalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint1594)
HAnimSegment1595 = x3d.HAnimSegment()
HAnimSegment1595.USE = "hanim_r_tarsal_proximal_phalanx_2"

HAnimHumanoid42.segments.append(HAnimSegment1595)
HAnimJoint1596 = x3d.HAnimJoint()
HAnimJoint1596.USE = "hanim_r_tarsal_proximal_interphalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint1596)
HAnimSegment1597 = x3d.HAnimSegment()
HAnimSegment1597.USE = "hanim_r_tarsal_middle_phalanx_2"

HAnimHumanoid42.segments.append(HAnimSegment1597)
HAnimSite1598 = x3d.HAnimSite()
HAnimSite1598.USE = "hanim_r_tarsal_distal_phalanx_2_tip"

HAnimHumanoid42.sites.append(HAnimSite1598)
HAnimJoint1599 = x3d.HAnimJoint()
HAnimJoint1599.USE = "hanim_r_tarsal_distal_interphalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint1599)
HAnimJoint1600 = x3d.HAnimJoint()
HAnimJoint1600.USE = "hanim_r_cuneonavicular_3"

HAnimHumanoid42.joints.append(HAnimJoint1600)
HAnimSegment1601 = x3d.HAnimSegment()
HAnimSegment1601.USE = "hanim_r_cuneiform_3"

HAnimHumanoid42.segments.append(HAnimSegment1601)
HAnimJoint1602 = x3d.HAnimJoint()
HAnimJoint1602.USE = "hanim_r_tarsometatarsal_3"

HAnimHumanoid42.joints.append(HAnimJoint1602)
HAnimSegment1603 = x3d.HAnimSegment()
HAnimSegment1603.USE = "hanim_r_metatarsal_3"

HAnimHumanoid42.segments.append(HAnimSegment1603)
HAnimJoint1604 = x3d.HAnimJoint()
HAnimJoint1604.USE = "hanim_r_metatarsophalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint1604)
HAnimSegment1605 = x3d.HAnimSegment()
HAnimSegment1605.USE = "hanim_r_tarsal_proximal_phalanx_3"

HAnimHumanoid42.segments.append(HAnimSegment1605)
HAnimJoint1606 = x3d.HAnimJoint()
HAnimJoint1606.USE = "hanim_r_tarsal_proximal_interphalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint1606)
HAnimSegment1607 = x3d.HAnimSegment()
HAnimSegment1607.USE = "hanim_r_tarsal_middle_phalanx_3"

HAnimHumanoid42.segments.append(HAnimSegment1607)
HAnimSite1608 = x3d.HAnimSite()
HAnimSite1608.USE = "hanim_r_tarsal_distal_phalanx_3_tip"

HAnimHumanoid42.sites.append(HAnimSite1608)
HAnimJoint1609 = x3d.HAnimJoint()
HAnimJoint1609.USE = "hanim_r_tarsal_distal_interphalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint1609)
HAnimJoint1610 = x3d.HAnimJoint()
HAnimJoint1610.USE = "hanim_r_calcaneocuboid"

HAnimHumanoid42.joints.append(HAnimJoint1610)
HAnimSegment1611 = x3d.HAnimSegment()
HAnimSegment1611.USE = "hanim_r_calcaneus"

HAnimHumanoid42.segments.append(HAnimSegment1611)
HAnimJoint1612 = x3d.HAnimJoint()
HAnimJoint1612.USE = "hanim_r_transversetarsal"

HAnimHumanoid42.joints.append(HAnimJoint1612)
HAnimSegment1613 = x3d.HAnimSegment()
HAnimSegment1613.USE = "hanim_r_cuboid"

HAnimHumanoid42.segments.append(HAnimSegment1613)
HAnimJoint1614 = x3d.HAnimJoint()
HAnimJoint1614.USE = "hanim_r_tarsometatarsal_4"

HAnimHumanoid42.joints.append(HAnimJoint1614)
HAnimSegment1615 = x3d.HAnimSegment()
HAnimSegment1615.USE = "hanim_r_metatarsal_4"

HAnimHumanoid42.segments.append(HAnimSegment1615)
HAnimJoint1616 = x3d.HAnimJoint()
HAnimJoint1616.USE = "hanim_r_metatarsophalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint1616)
HAnimSegment1617 = x3d.HAnimSegment()
HAnimSegment1617.USE = "hanim_r_tarsal_proximal_phalanx_4"

HAnimHumanoid42.segments.append(HAnimSegment1617)
HAnimJoint1618 = x3d.HAnimJoint()
HAnimJoint1618.USE = "hanim_r_tarsal_proximal_interphalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint1618)
HAnimSegment1619 = x3d.HAnimSegment()
HAnimSegment1619.USE = "hanim_r_tarsal_middle_phalanx_4"

HAnimHumanoid42.segments.append(HAnimSegment1619)
HAnimSite1620 = x3d.HAnimSite()
HAnimSite1620.USE = "hanim_r_tarsal_distal_phalanx_4_tip"

HAnimHumanoid42.sites.append(HAnimSite1620)
HAnimJoint1621 = x3d.HAnimJoint()
HAnimJoint1621.USE = "hanim_r_tarsal_distal_interphalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint1621)
HAnimJoint1622 = x3d.HAnimJoint()
HAnimJoint1622.USE = "hanim_r_tarsometatarsal_5"

HAnimHumanoid42.joints.append(HAnimJoint1622)
HAnimSegment1623 = x3d.HAnimSegment()
HAnimSegment1623.USE = "hanim_r_metatarsal_5"

HAnimHumanoid42.segments.append(HAnimSegment1623)
HAnimSite1624 = x3d.HAnimSite()
HAnimSite1624.USE = "hanim_r_metatarsal_phalanx_5_pt"

HAnimHumanoid42.sites.append(HAnimSite1624)
HAnimJoint1625 = x3d.HAnimJoint()
HAnimJoint1625.USE = "hanim_r_metatarsophalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint1625)
HAnimSegment1626 = x3d.HAnimSegment()
HAnimSegment1626.USE = "hanim_r_tarsal_proximal_phalanx_5"

HAnimHumanoid42.segments.append(HAnimSegment1626)
HAnimJoint1627 = x3d.HAnimJoint()
HAnimJoint1627.USE = "hanim_r_tarsal_proximal_interphalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint1627)
HAnimSegment1628 = x3d.HAnimSegment()
HAnimSegment1628.USE = "hanim_r_tarsal_middle_phalanx_5"

HAnimHumanoid42.segments.append(HAnimSegment1628)
HAnimSite1629 = x3d.HAnimSite()
HAnimSite1629.USE = "hanim_r_tarsal_distal_phalanx_5_tip"

HAnimHumanoid42.sites.append(HAnimSite1629)
HAnimJoint1630 = x3d.HAnimJoint()
HAnimJoint1630.USE = "hanim_r_tarsal_distal_interphalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint1630)
HAnimJoint1631 = x3d.HAnimJoint()
HAnimJoint1631.USE = "hanim_vl5"

HAnimHumanoid42.joints.append(HAnimJoint1631)
HAnimSegment1632 = x3d.HAnimSegment()
HAnimSegment1632.USE = "hanim_l5"

HAnimHumanoid42.segments.append(HAnimSegment1632)
HAnimJoint1633 = x3d.HAnimJoint()
HAnimJoint1633.USE = "hanim_vl4"

HAnimHumanoid42.joints.append(HAnimJoint1633)
HAnimSegment1634 = x3d.HAnimSegment()
HAnimSegment1634.USE = "hanim_l4"

HAnimHumanoid42.segments.append(HAnimSegment1634)
HAnimJoint1635 = x3d.HAnimJoint()
HAnimJoint1635.USE = "hanim_vl3"

HAnimHumanoid42.joints.append(HAnimJoint1635)
HAnimSegment1636 = x3d.HAnimSegment()
HAnimSegment1636.USE = "hanim_l3"

HAnimHumanoid42.segments.append(HAnimSegment1636)
HAnimSite1637 = x3d.HAnimSite()
HAnimSite1637.USE = "hanim_l_rib10_pt"

HAnimHumanoid42.sites.append(HAnimSite1637)
HAnimSite1638 = x3d.HAnimSite()
HAnimSite1638.USE = "hanim_r_rib10_pt"

HAnimHumanoid42.sites.append(HAnimSite1638)
HAnimSite1639 = x3d.HAnimSite()
HAnimSite1639.USE = "hanim_spine_2_middle_back_pt"

HAnimHumanoid42.sites.append(HAnimSite1639)
HAnimJoint1640 = x3d.HAnimJoint()
HAnimJoint1640.USE = "hanim_vl2"

HAnimHumanoid42.joints.append(HAnimJoint1640)
HAnimSegment1641 = x3d.HAnimSegment()
HAnimSegment1641.USE = "hanim_l2"

HAnimHumanoid42.segments.append(HAnimSegment1641)
HAnimJoint1642 = x3d.HAnimJoint()
HAnimJoint1642.USE = "hanim_vl1"

HAnimHumanoid42.joints.append(HAnimJoint1642)
HAnimSegment1643 = x3d.HAnimSegment()
HAnimSegment1643.USE = "hanim_l1"

HAnimHumanoid42.segments.append(HAnimSegment1643)
HAnimJoint1644 = x3d.HAnimJoint()
HAnimJoint1644.USE = "hanim_vt12"

HAnimHumanoid42.joints.append(HAnimJoint1644)
HAnimSegment1645 = x3d.HAnimSegment()
HAnimSegment1645.USE = "hanim_t12"

HAnimHumanoid42.segments.append(HAnimSegment1645)
HAnimJoint1646 = x3d.HAnimJoint()
HAnimJoint1646.USE = "hanim_vt11"

HAnimHumanoid42.joints.append(HAnimJoint1646)
HAnimSegment1647 = x3d.HAnimSegment()
HAnimSegment1647.USE = "hanim_t11"

HAnimHumanoid42.segments.append(HAnimSegment1647)
HAnimSite1648 = x3d.HAnimSite()
HAnimSite1648.USE = "hanim_substernale_pt"

HAnimHumanoid42.sites.append(HAnimSite1648)
HAnimJoint1649 = x3d.HAnimJoint()
HAnimJoint1649.USE = "hanim_vt10"

HAnimHumanoid42.joints.append(HAnimJoint1649)
HAnimSegment1650 = x3d.HAnimSegment()
HAnimSegment1650.USE = "hanim_t10"

HAnimHumanoid42.segments.append(HAnimSegment1650)
HAnimSite1651 = x3d.HAnimSite()
HAnimSite1651.USE = "hanim_l_thelion_pt"

HAnimHumanoid42.sites.append(HAnimSite1651)
HAnimSite1652 = x3d.HAnimSite()
HAnimSite1652.USE = "hanim_r_thelion_pt"

HAnimHumanoid42.sites.append(HAnimSite1652)
HAnimJoint1653 = x3d.HAnimJoint()
HAnimJoint1653.USE = "hanim_vt9"

HAnimHumanoid42.joints.append(HAnimJoint1653)
HAnimSegment1654 = x3d.HAnimSegment()
HAnimSegment1654.USE = "hanim_t9"

HAnimHumanoid42.segments.append(HAnimSegment1654)
HAnimJoint1655 = x3d.HAnimJoint()
HAnimJoint1655.USE = "hanim_vt8"

HAnimHumanoid42.joints.append(HAnimJoint1655)
HAnimSegment1656 = x3d.HAnimSegment()
HAnimSegment1656.USE = "hanim_t8"

HAnimHumanoid42.segments.append(HAnimSegment1656)
HAnimJoint1657 = x3d.HAnimJoint()
HAnimJoint1657.USE = "hanim_vt7"

HAnimHumanoid42.joints.append(HAnimJoint1657)
HAnimSegment1658 = x3d.HAnimSegment()
HAnimSegment1658.USE = "hanim_t7"

HAnimHumanoid42.segments.append(HAnimSegment1658)
HAnimSite1659 = x3d.HAnimSite()
HAnimSite1659.USE = "hanim_l_chest_midsagittal_plane_pt"

HAnimHumanoid42.sites.append(HAnimSite1659)
HAnimSite1660 = x3d.HAnimSite()
HAnimSite1660.USE = "hanim_mesosternale_pt"

HAnimHumanoid42.sites.append(HAnimSite1660)
HAnimSite1661 = x3d.HAnimSite()
HAnimSite1661.USE = "hanim_r_chest_midsagittal_plane_pt"

HAnimHumanoid42.sites.append(HAnimSite1661)
HAnimSite1662 = x3d.HAnimSite()
HAnimSite1662.USE = "hanim_rear_center_midsagittal_plane_pt"

HAnimHumanoid42.sites.append(HAnimSite1662)
HAnimJoint1663 = x3d.HAnimJoint()
HAnimJoint1663.USE = "hanim_vt6"

HAnimHumanoid42.joints.append(HAnimJoint1663)
HAnimSegment1664 = x3d.HAnimSegment()
HAnimSegment1664.USE = "hanim_t6"

HAnimHumanoid42.segments.append(HAnimSegment1664)
HAnimSite1665 = x3d.HAnimSite()
HAnimSite1665.USE = "hanim_spine_1_middle_back_pt"

HAnimHumanoid42.sites.append(HAnimSite1665)
HAnimJoint1666 = x3d.HAnimJoint()
HAnimJoint1666.USE = "hanim_vt5"

HAnimHumanoid42.joints.append(HAnimJoint1666)
HAnimSegment1667 = x3d.HAnimSegment()
HAnimSegment1667.USE = "hanim_t5"

HAnimHumanoid42.segments.append(HAnimSegment1667)
HAnimJoint1668 = x3d.HAnimJoint()
HAnimJoint1668.USE = "hanim_vt4"

HAnimHumanoid42.joints.append(HAnimJoint1668)
HAnimSegment1669 = x3d.HAnimSegment()
HAnimSegment1669.USE = "hanim_t4"

HAnimHumanoid42.segments.append(HAnimSegment1669)
HAnimJoint1670 = x3d.HAnimJoint()
HAnimJoint1670.USE = "hanim_vt3"

HAnimHumanoid42.joints.append(HAnimJoint1670)
HAnimSegment1671 = x3d.HAnimSegment()
HAnimSegment1671.USE = "hanim_t3"

HAnimHumanoid42.segments.append(HAnimSegment1671)
HAnimJoint1672 = x3d.HAnimJoint()
HAnimJoint1672.USE = "hanim_vt2"

HAnimHumanoid42.joints.append(HAnimJoint1672)
HAnimSegment1673 = x3d.HAnimSegment()
HAnimSegment1673.USE = "hanim_t2"

HAnimHumanoid42.segments.append(HAnimSegment1673)
HAnimSite1674 = x3d.HAnimSite()
HAnimSite1674.USE = "hanim_cervicale_pt"

HAnimHumanoid42.sites.append(HAnimSite1674)
HAnimSite1675 = x3d.HAnimSite()
HAnimSite1675.USE = "hanim_suprasternale_pt"

HAnimHumanoid42.sites.append(HAnimSite1675)
HAnimJoint1676 = x3d.HAnimJoint()
HAnimJoint1676.USE = "hanim_vt1"

HAnimHumanoid42.joints.append(HAnimJoint1676)
HAnimSegment1677 = x3d.HAnimSegment()
HAnimSegment1677.USE = "hanim_t1"

HAnimHumanoid42.segments.append(HAnimSegment1677)
HAnimSite1678 = x3d.HAnimSite()
HAnimSite1678.USE = "hanim_l_neck_base_pt"

HAnimHumanoid42.sites.append(HAnimSite1678)
HAnimSite1679 = x3d.HAnimSite()
HAnimSite1679.USE = "hanim_r_neck_base_pt"

HAnimHumanoid42.sites.append(HAnimSite1679)
HAnimSite1680 = x3d.HAnimSite()
HAnimSite1680.USE = "hanim_l_acromion_pt"

HAnimHumanoid42.sites.append(HAnimSite1680)
HAnimSite1681 = x3d.HAnimSite()
HAnimSite1681.USE = "hanim_l_axilla_distal_pt"

HAnimHumanoid42.sites.append(HAnimSite1681)
HAnimSite1682 = x3d.HAnimSite()
HAnimSite1682.USE = "hanim_l_axilla_posterior_folds_pt"

HAnimHumanoid42.sites.append(HAnimSite1682)
HAnimSite1683 = x3d.HAnimSite()
HAnimSite1683.USE = "hanim_l_axilla_proximal_pt"

HAnimHumanoid42.sites.append(HAnimSite1683)
HAnimSite1684 = x3d.HAnimSite()
HAnimSite1684.USE = "hanim_l_clavicale_pt"

HAnimHumanoid42.sites.append(HAnimSite1684)
HAnimSite1685 = x3d.HAnimSite()
HAnimSite1685.USE = "hanim_r_acromion_pt"

HAnimHumanoid42.sites.append(HAnimSite1685)
HAnimSite1686 = x3d.HAnimSite()
HAnimSite1686.USE = "hanim_r_axilla_distal_pt"

HAnimHumanoid42.sites.append(HAnimSite1686)
HAnimSite1687 = x3d.HAnimSite()
HAnimSite1687.USE = "hanim_r_axilla_posterior_folds_pt"

HAnimHumanoid42.sites.append(HAnimSite1687)
HAnimSite1688 = x3d.HAnimSite()
HAnimSite1688.USE = "hanim_r_axilla_proximal_pt"

HAnimHumanoid42.sites.append(HAnimSite1688)
HAnimSite1689 = x3d.HAnimSite()
HAnimSite1689.USE = "hanim_r_clavicale_pt"

HAnimHumanoid42.sites.append(HAnimSite1689)
HAnimJoint1690 = x3d.HAnimJoint()
HAnimJoint1690.USE = "hanim_vc7"

HAnimHumanoid42.joints.append(HAnimJoint1690)
HAnimSegment1691 = x3d.HAnimSegment()
HAnimSegment1691.USE = "hanim_c7"

HAnimHumanoid42.segments.append(HAnimSegment1691)
HAnimJoint1692 = x3d.HAnimJoint()
HAnimJoint1692.USE = "hanim_vc6"

HAnimHumanoid42.joints.append(HAnimJoint1692)
HAnimSegment1693 = x3d.HAnimSegment()
HAnimSegment1693.USE = "hanim_c6"

HAnimHumanoid42.segments.append(HAnimSegment1693)
HAnimJoint1694 = x3d.HAnimJoint()
HAnimJoint1694.USE = "hanim_vc5"

HAnimHumanoid42.joints.append(HAnimJoint1694)
HAnimSegment1695 = x3d.HAnimSegment()
HAnimSegment1695.USE = "hanim_c5"

HAnimHumanoid42.segments.append(HAnimSegment1695)
HAnimJoint1696 = x3d.HAnimJoint()
HAnimJoint1696.USE = "hanim_vc4"

HAnimHumanoid42.joints.append(HAnimJoint1696)
HAnimSegment1697 = x3d.HAnimSegment()
HAnimSegment1697.USE = "hanim_c4"

HAnimHumanoid42.segments.append(HAnimSegment1697)
HAnimJoint1698 = x3d.HAnimJoint()
HAnimJoint1698.USE = "hanim_vc3"

HAnimHumanoid42.joints.append(HAnimJoint1698)
HAnimSegment1699 = x3d.HAnimSegment()
HAnimSegment1699.USE = "hanim_c3"

HAnimHumanoid42.segments.append(HAnimSegment1699)
HAnimSite1700 = x3d.HAnimSite()
HAnimSite1700.USE = "hanim_adams_apple_pt"

HAnimHumanoid42.sites.append(HAnimSite1700)
HAnimJoint1701 = x3d.HAnimJoint()
HAnimJoint1701.USE = "hanim_vc2"

HAnimHumanoid42.joints.append(HAnimJoint1701)
HAnimSegment1702 = x3d.HAnimSegment()
HAnimSegment1702.USE = "hanim_c2"

HAnimHumanoid42.segments.append(HAnimSegment1702)
HAnimJoint1703 = x3d.HAnimJoint()
HAnimJoint1703.USE = "hanim_vc1"

HAnimHumanoid42.joints.append(HAnimJoint1703)
HAnimSegment1704 = x3d.HAnimSegment()
HAnimSegment1704.USE = "hanim_c1"

HAnimHumanoid42.segments.append(HAnimSegment1704)
HAnimSite1705 = x3d.HAnimSite()
HAnimSite1705.USE = "hanim_glabella_pt"

HAnimHumanoid42.sites.append(HAnimSite1705)
HAnimSite1706 = x3d.HAnimSite()
HAnimSite1706.USE = "hanim_l_ectocanthus_pt"

HAnimHumanoid42.sites.append(HAnimSite1706)
HAnimSite1707 = x3d.HAnimSite()
HAnimSite1707.USE = "hanim_l_infraorbitale_pt"

HAnimHumanoid42.sites.append(HAnimSite1707)
HAnimSite1708 = x3d.HAnimSite()
HAnimSite1708.USE = "hanim_l_tragion_pt"

HAnimHumanoid42.sites.append(HAnimSite1708)
HAnimSite1709 = x3d.HAnimSite()
HAnimSite1709.USE = "hanim_nuchale_pt"

HAnimHumanoid42.sites.append(HAnimSite1709)
HAnimSite1710 = x3d.HAnimSite()
HAnimSite1710.USE = "hanim_opisthocranion_pt"

HAnimHumanoid42.sites.append(HAnimSite1710)
HAnimSite1711 = x3d.HAnimSite()
HAnimSite1711.USE = "hanim_r_ectocanthus_pt"

HAnimHumanoid42.sites.append(HAnimSite1711)
HAnimSite1712 = x3d.HAnimSite()
HAnimSite1712.USE = "hanim_r_infraorbitale_pt"

HAnimHumanoid42.sites.append(HAnimSite1712)
HAnimSite1713 = x3d.HAnimSite()
HAnimSite1713.USE = "hanim_r_tragion_pt"

HAnimHumanoid42.sites.append(HAnimSite1713)
HAnimSite1714 = x3d.HAnimSite()
HAnimSite1714.USE = "hanim_sellion_pt"

HAnimHumanoid42.sites.append(HAnimSite1714)
HAnimSite1715 = x3d.HAnimSite()
HAnimSite1715.USE = "hanim_skull_vertex_pt"

HAnimHumanoid42.sites.append(HAnimSite1715)
HAnimJoint1716 = x3d.HAnimJoint()
HAnimJoint1716.USE = "hanim_skullbase"

HAnimHumanoid42.joints.append(HAnimJoint1716)
HAnimSegment1717 = x3d.HAnimSegment()
HAnimSegment1717.USE = "hanim_skull"

HAnimHumanoid42.segments.append(HAnimSegment1717)
HAnimSite1718 = x3d.HAnimSite()
HAnimSite1718.USE = "hanim_l_gonion_pt"

HAnimHumanoid42.sites.append(HAnimSite1718)
HAnimSite1719 = x3d.HAnimSite()
HAnimSite1719.USE = "hanim_menton_pt"

HAnimHumanoid42.sites.append(HAnimSite1719)
HAnimSite1720 = x3d.HAnimSite()
HAnimSite1720.USE = "hanim_r_gonion_pt"

HAnimHumanoid42.sites.append(HAnimSite1720)
HAnimSite1721 = x3d.HAnimSite()
HAnimSite1721.USE = "hanim_supramenton_pt"

HAnimHumanoid42.sites.append(HAnimSite1721)
HAnimJoint1722 = x3d.HAnimJoint()
HAnimJoint1722.USE = "hanim_l_eyelid_joint"

HAnimHumanoid42.joints.append(HAnimJoint1722)
HAnimJoint1723 = x3d.HAnimJoint()
HAnimJoint1723.USE = "hanim_r_eyelid_joint"

HAnimHumanoid42.joints.append(HAnimJoint1723)
HAnimJoint1724 = x3d.HAnimJoint()
HAnimJoint1724.USE = "hanim_l_eyeball_joint"

HAnimHumanoid42.joints.append(HAnimJoint1724)
HAnimJoint1725 = x3d.HAnimJoint()
HAnimJoint1725.USE = "hanim_r_eyeball_joint"

HAnimHumanoid42.joints.append(HAnimJoint1725)
HAnimJoint1726 = x3d.HAnimJoint()
HAnimJoint1726.USE = "hanim_l_eyebrow_joint"

HAnimHumanoid42.joints.append(HAnimJoint1726)
HAnimJoint1727 = x3d.HAnimJoint()
HAnimJoint1727.USE = "hanim_r_eyebrow_joint"

HAnimHumanoid42.joints.append(HAnimJoint1727)
HAnimJoint1728 = x3d.HAnimJoint()
HAnimJoint1728.USE = "hanim_temporomandibular"

HAnimHumanoid42.joints.append(HAnimJoint1728)
HAnimJoint1729 = x3d.HAnimJoint()
HAnimJoint1729.USE = "hanim_l_sternoclavicular"

HAnimHumanoid42.joints.append(HAnimJoint1729)
HAnimSegment1730 = x3d.HAnimSegment()
HAnimSegment1730.USE = "hanim_l_clavicle"

HAnimHumanoid42.segments.append(HAnimSegment1730)
HAnimJoint1731 = x3d.HAnimJoint()
HAnimJoint1731.USE = "hanim_l_acromioclavicular"

HAnimHumanoid42.joints.append(HAnimJoint1731)
HAnimSegment1732 = x3d.HAnimSegment()
HAnimSegment1732.USE = "hanim_l_scapula"

HAnimHumanoid42.segments.append(HAnimSegment1732)
HAnimSite1733 = x3d.HAnimSite()
HAnimSite1733.USE = "hanim_l_bideltoid_pt"

HAnimHumanoid42.sites.append(HAnimSite1733)
HAnimSite1734 = x3d.HAnimSite()
HAnimSite1734.USE = "hanim_l_humeral_lateral_epicondyles_pt"

HAnimHumanoid42.sites.append(HAnimSite1734)
HAnimJoint1735 = x3d.HAnimJoint()
HAnimJoint1735.USE = "hanim_l_shoulder"

HAnimHumanoid42.joints.append(HAnimJoint1735)
HAnimSegment1736 = x3d.HAnimSegment()
HAnimSegment1736.USE = "hanim_l_upperarm"

HAnimHumanoid42.segments.append(HAnimSegment1736)
HAnimSite1737 = x3d.HAnimSite()
HAnimSite1737.USE = "hanim_l_humeral_medial_epicondyles_pt"

HAnimHumanoid42.sites.append(HAnimSite1737)
HAnimSite1738 = x3d.HAnimSite()
HAnimSite1738.USE = "hanim_l_olecranon_pt"

HAnimHumanoid42.sites.append(HAnimSite1738)
HAnimSite1739 = x3d.HAnimSite()
HAnimSite1739.USE = "hanim_l_radial_styloid_pt"

HAnimHumanoid42.sites.append(HAnimSite1739)
HAnimSite1740 = x3d.HAnimSite()
HAnimSite1740.USE = "hanim_l_radiale_pt"

HAnimHumanoid42.sites.append(HAnimSite1740)
HAnimJoint1741 = x3d.HAnimJoint()
HAnimJoint1741.USE = "hanim_l_elbow"

HAnimHumanoid42.joints.append(HAnimJoint1741)
HAnimSegment1742 = x3d.HAnimSegment()
HAnimSegment1742.USE = "hanim_l_forearm"

HAnimHumanoid42.segments.append(HAnimSegment1742)
HAnimSite1743 = x3d.HAnimSite()
HAnimSite1743.USE = "hanim_l_ulnar_styloid_pt"

HAnimHumanoid42.sites.append(HAnimSite1743)
HAnimJoint1744 = x3d.HAnimJoint()
HAnimJoint1744.USE = "hanim_l_radiocarpal"

HAnimHumanoid42.joints.append(HAnimJoint1744)
HAnimSegment1745 = x3d.HAnimSegment()
HAnimSegment1745.USE = "hanim_l_carpal"

HAnimHumanoid42.segments.append(HAnimSegment1745)
HAnimJoint1746 = x3d.HAnimJoint()
HAnimJoint1746.USE = "hanim_l_midcarpal_1"

HAnimHumanoid42.joints.append(HAnimJoint1746)
HAnimSegment1747 = x3d.HAnimSegment()
HAnimSegment1747.USE = "hanim_l_trapezium"

HAnimHumanoid42.segments.append(HAnimSegment1747)
HAnimJoint1748 = x3d.HAnimJoint()
HAnimJoint1748.USE = "hanim_l_carpometacarpal_1"

HAnimHumanoid42.joints.append(HAnimJoint1748)
HAnimSegment1749 = x3d.HAnimSegment()
HAnimSegment1749.USE = "hanim_l_metacarpal_1"

HAnimHumanoid42.segments.append(HAnimSegment1749)
HAnimJoint1750 = x3d.HAnimJoint()
HAnimJoint1750.USE = "hanim_l_metacarpophalangeal_1"

HAnimHumanoid42.joints.append(HAnimJoint1750)
HAnimSegment1751 = x3d.HAnimSegment()
HAnimSegment1751.USE = "hanim_l_carpal_proximal_phalanx_1"

HAnimHumanoid42.segments.append(HAnimSegment1751)
HAnimSite1752 = x3d.HAnimSite()
HAnimSite1752.USE = "hanim_l_carpal_distal_phalanx_1_tip"

HAnimHumanoid42.sites.append(HAnimSite1752)
HAnimJoint1753 = x3d.HAnimJoint()
HAnimJoint1753.USE = "hanim_l_carpal_interphalangeal_1"

HAnimHumanoid42.joints.append(HAnimJoint1753)
HAnimJoint1754 = x3d.HAnimJoint()
HAnimJoint1754.USE = "hanim_l_midcarpal_2"

HAnimHumanoid42.joints.append(HAnimJoint1754)
HAnimSegment1755 = x3d.HAnimSegment()
HAnimSegment1755.USE = "hanim_l_trapezoid"

HAnimHumanoid42.segments.append(HAnimSegment1755)
HAnimSite1756 = x3d.HAnimSite()
HAnimSite1756.USE = "hanim_l_metacarpal_phalanx_2_pt"

HAnimHumanoid42.sites.append(HAnimSite1756)
HAnimJoint1757 = x3d.HAnimJoint()
HAnimJoint1757.USE = "hanim_l_carpometacarpal_2"

HAnimHumanoid42.joints.append(HAnimJoint1757)
HAnimSegment1758 = x3d.HAnimSegment()
HAnimSegment1758.USE = "hanim_l_metacarpal_2"

HAnimHumanoid42.segments.append(HAnimSegment1758)
HAnimJoint1759 = x3d.HAnimJoint()
HAnimJoint1759.USE = "hanim_l_metacarpophalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint1759)
HAnimSegment1760 = x3d.HAnimSegment()
HAnimSegment1760.USE = "hanim_l_carpal_proximal_phalanx_2"

HAnimHumanoid42.segments.append(HAnimSegment1760)
HAnimJoint1761 = x3d.HAnimJoint()
HAnimJoint1761.USE = "hanim_l_carpal_proximal_interphalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint1761)
HAnimSegment1762 = x3d.HAnimSegment()
HAnimSegment1762.USE = "hanim_l_carpal_middle_phalanx_2"

HAnimHumanoid42.segments.append(HAnimSegment1762)
HAnimSite1763 = x3d.HAnimSite()
HAnimSite1763.USE = "hanim_l_carpal_distal_phalanx_2_tip"

HAnimHumanoid42.sites.append(HAnimSite1763)
HAnimSite1764 = x3d.HAnimSite()
HAnimSite1764.USE = "hanim_l_dactylion_pt"

HAnimHumanoid42.sites.append(HAnimSite1764)
HAnimJoint1765 = x3d.HAnimJoint()
HAnimJoint1765.USE = "hanim_l_carpal_distal_interphalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint1765)
HAnimJoint1766 = x3d.HAnimJoint()
HAnimJoint1766.USE = "hanim_l_midcarpal_3"

HAnimHumanoid42.joints.append(HAnimJoint1766)
HAnimSegment1767 = x3d.HAnimSegment()
HAnimSegment1767.USE = "hanim_l_capitate"

HAnimHumanoid42.segments.append(HAnimSegment1767)
HAnimSite1768 = x3d.HAnimSite()
HAnimSite1768.USE = "hanim_l_metacarpal_phalanx_3_pt"

HAnimHumanoid42.sites.append(HAnimSite1768)
HAnimJoint1769 = x3d.HAnimJoint()
HAnimJoint1769.USE = "hanim_l_carpometacarpal_3"

HAnimHumanoid42.joints.append(HAnimJoint1769)
HAnimSegment1770 = x3d.HAnimSegment()
HAnimSegment1770.USE = "hanim_l_metacarpal_3"

HAnimHumanoid42.segments.append(HAnimSegment1770)
HAnimJoint1771 = x3d.HAnimJoint()
HAnimJoint1771.USE = "hanim_l_metacarpophalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint1771)
HAnimSegment1772 = x3d.HAnimSegment()
HAnimSegment1772.USE = "hanim_l_carpal_proximal_phalanx_3"

HAnimHumanoid42.segments.append(HAnimSegment1772)
HAnimJoint1773 = x3d.HAnimJoint()
HAnimJoint1773.USE = "hanim_l_carpal_proximal_interphalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint1773)
HAnimSegment1774 = x3d.HAnimSegment()
HAnimSegment1774.USE = "hanim_l_carpal_middle_phalanx_3"

HAnimHumanoid42.segments.append(HAnimSegment1774)
HAnimSite1775 = x3d.HAnimSite()
HAnimSite1775.USE = "hanim_l_carpal_distal_phalanx_3_tip"

HAnimHumanoid42.sites.append(HAnimSite1775)
HAnimJoint1776 = x3d.HAnimJoint()
HAnimJoint1776.USE = "hanim_l_carpal_distal_interphalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint1776)
HAnimJoint1777 = x3d.HAnimJoint()
HAnimJoint1777.USE = "hanim_l_midcarpal_4_5"

HAnimHumanoid42.joints.append(HAnimJoint1777)
HAnimSegment1778 = x3d.HAnimSegment()
HAnimSegment1778.USE = "hanim_l_hamate"

HAnimHumanoid42.segments.append(HAnimSegment1778)
HAnimSite1779 = x3d.HAnimSite()
HAnimSite1779.USE = "hanim_l_metacarpal_phalanx_5_pt"

HAnimHumanoid42.sites.append(HAnimSite1779)
HAnimJoint1780 = x3d.HAnimJoint()
HAnimJoint1780.USE = "hanim_l_carpometacarpal_4"

HAnimHumanoid42.joints.append(HAnimJoint1780)
HAnimSegment1781 = x3d.HAnimSegment()
HAnimSegment1781.USE = "hanim_l_metacarpal_4"

HAnimHumanoid42.segments.append(HAnimSegment1781)
HAnimJoint1782 = x3d.HAnimJoint()
HAnimJoint1782.USE = "hanim_l_metacarpophalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint1782)
HAnimSegment1783 = x3d.HAnimSegment()
HAnimSegment1783.USE = "hanim_l_carpal_proximal_phalanx_4"

HAnimHumanoid42.segments.append(HAnimSegment1783)
HAnimJoint1784 = x3d.HAnimJoint()
HAnimJoint1784.USE = "hanim_l_carpal_proximal_interphalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint1784)
HAnimSegment1785 = x3d.HAnimSegment()
HAnimSegment1785.USE = "hanim_l_carpal_middle_phalanx_4"

HAnimHumanoid42.segments.append(HAnimSegment1785)
HAnimSite1786 = x3d.HAnimSite()
HAnimSite1786.USE = "hanim_l_carpal_distal_phalanx_4_tip"

HAnimHumanoid42.sites.append(HAnimSite1786)
HAnimJoint1787 = x3d.HAnimJoint()
HAnimJoint1787.USE = "hanim_l_carpal_distal_interphalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint1787)
HAnimJoint1788 = x3d.HAnimJoint()
HAnimJoint1788.USE = "hanim_l_carpometacarpal_5"

HAnimHumanoid42.joints.append(HAnimJoint1788)
HAnimSegment1789 = x3d.HAnimSegment()
HAnimSegment1789.USE = "hanim_l_metacarpal_5"

HAnimHumanoid42.segments.append(HAnimSegment1789)
HAnimJoint1790 = x3d.HAnimJoint()
HAnimJoint1790.USE = "hanim_l_metacarpophalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint1790)
HAnimSegment1791 = x3d.HAnimSegment()
HAnimSegment1791.USE = "hanim_l_carpal_proximal_phalanx_5"

HAnimHumanoid42.segments.append(HAnimSegment1791)
HAnimJoint1792 = x3d.HAnimJoint()
HAnimJoint1792.USE = "hanim_l_carpal_proximal_interphalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint1792)
HAnimSegment1793 = x3d.HAnimSegment()
HAnimSegment1793.USE = "hanim_l_carpal_middle_phalanx_5"

HAnimHumanoid42.segments.append(HAnimSegment1793)
HAnimSite1794 = x3d.HAnimSite()
HAnimSite1794.USE = "hanim_l_carpal_distal_phalanx_5_tip"

HAnimHumanoid42.sites.append(HAnimSite1794)
HAnimJoint1795 = x3d.HAnimJoint()
HAnimJoint1795.USE = "hanim_l_carpal_distal_interphalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint1795)
HAnimJoint1796 = x3d.HAnimJoint()
HAnimJoint1796.USE = "hanim_r_sternoclavicular"

HAnimHumanoid42.joints.append(HAnimJoint1796)
HAnimSegment1797 = x3d.HAnimSegment()
HAnimSegment1797.USE = "hanim_r_clavicle"

HAnimHumanoid42.segments.append(HAnimSegment1797)
HAnimJoint1798 = x3d.HAnimJoint()
HAnimJoint1798.USE = "hanim_r_acromioclavicular"

HAnimHumanoid42.joints.append(HAnimJoint1798)
HAnimSegment1799 = x3d.HAnimSegment()
HAnimSegment1799.USE = "hanim_r_scapula"

HAnimHumanoid42.segments.append(HAnimSegment1799)
HAnimSite1800 = x3d.HAnimSite()
HAnimSite1800.USE = "hanim_r_bideltoid_pt"

HAnimHumanoid42.sites.append(HAnimSite1800)
HAnimSite1801 = x3d.HAnimSite()
HAnimSite1801.USE = "hanim_r_humeral_lateral_epicondyles_pt"

HAnimHumanoid42.sites.append(HAnimSite1801)
HAnimJoint1802 = x3d.HAnimJoint()
HAnimJoint1802.USE = "hanim_r_shoulder"

HAnimHumanoid42.joints.append(HAnimJoint1802)
HAnimSegment1803 = x3d.HAnimSegment()
HAnimSegment1803.USE = "hanim_r_upperarm"

HAnimHumanoid42.segments.append(HAnimSegment1803)
HAnimSite1804 = x3d.HAnimSite()
HAnimSite1804.USE = "hanim_r_humeral_medial_epicondyles_pt"

HAnimHumanoid42.sites.append(HAnimSite1804)
HAnimSite1805 = x3d.HAnimSite()
HAnimSite1805.USE = "hanim_r_olecranon_pt"

HAnimHumanoid42.sites.append(HAnimSite1805)
HAnimSite1806 = x3d.HAnimSite()
HAnimSite1806.USE = "hanim_r_radial_styloid_pt"

HAnimHumanoid42.sites.append(HAnimSite1806)
HAnimSite1807 = x3d.HAnimSite()
HAnimSite1807.USE = "hanim_r_radiale_pt"

HAnimHumanoid42.sites.append(HAnimSite1807)
HAnimJoint1808 = x3d.HAnimJoint()
HAnimJoint1808.USE = "hanim_r_elbow"

HAnimHumanoid42.joints.append(HAnimJoint1808)
HAnimSegment1809 = x3d.HAnimSegment()
HAnimSegment1809.USE = "hanim_r_forearm"

HAnimHumanoid42.segments.append(HAnimSegment1809)
HAnimSite1810 = x3d.HAnimSite()
HAnimSite1810.USE = "hanim_r_ulnar_styloid_pt"

HAnimHumanoid42.sites.append(HAnimSite1810)
HAnimJoint1811 = x3d.HAnimJoint()
HAnimJoint1811.USE = "hanim_r_radiocarpal"

HAnimHumanoid42.joints.append(HAnimJoint1811)
HAnimSegment1812 = x3d.HAnimSegment()
HAnimSegment1812.USE = "hanim_r_carpal"

HAnimHumanoid42.segments.append(HAnimSegment1812)
HAnimJoint1813 = x3d.HAnimJoint()
HAnimJoint1813.USE = "hanim_r_midcarpal_1"

HAnimHumanoid42.joints.append(HAnimJoint1813)
HAnimSegment1814 = x3d.HAnimSegment()
HAnimSegment1814.USE = "hanim_r_trapezium"

HAnimHumanoid42.segments.append(HAnimSegment1814)
HAnimJoint1815 = x3d.HAnimJoint()
HAnimJoint1815.USE = "hanim_r_carpometacarpal_1"

HAnimHumanoid42.joints.append(HAnimJoint1815)
HAnimSegment1816 = x3d.HAnimSegment()
HAnimSegment1816.USE = "hanim_r_metacarpal_1"

HAnimHumanoid42.segments.append(HAnimSegment1816)
HAnimJoint1817 = x3d.HAnimJoint()
HAnimJoint1817.USE = "hanim_r_metacarpophalangeal_1"

HAnimHumanoid42.joints.append(HAnimJoint1817)
HAnimSegment1818 = x3d.HAnimSegment()
HAnimSegment1818.USE = "hanim_r_carpal_proximal_phalanx_1"

HAnimHumanoid42.segments.append(HAnimSegment1818)
HAnimSite1819 = x3d.HAnimSite()
HAnimSite1819.USE = "hanim_r_carpal_distal_phalanx_1_tip"

HAnimHumanoid42.sites.append(HAnimSite1819)
HAnimJoint1820 = x3d.HAnimJoint()
HAnimJoint1820.USE = "hanim_r_carpal_interphalangeal_1"

HAnimHumanoid42.joints.append(HAnimJoint1820)
HAnimJoint1821 = x3d.HAnimJoint()
HAnimJoint1821.USE = "hanim_r_midcarpal_2"

HAnimHumanoid42.joints.append(HAnimJoint1821)
HAnimSegment1822 = x3d.HAnimSegment()
HAnimSegment1822.USE = "hanim_r_trapezoid"

HAnimHumanoid42.segments.append(HAnimSegment1822)
HAnimSite1823 = x3d.HAnimSite()
HAnimSite1823.USE = "hanim_r_metacarpal_phalanx_2_pt"

HAnimHumanoid42.sites.append(HAnimSite1823)
HAnimJoint1824 = x3d.HAnimJoint()
HAnimJoint1824.USE = "hanim_r_carpometacarpal_2"

HAnimHumanoid42.joints.append(HAnimJoint1824)
HAnimSegment1825 = x3d.HAnimSegment()
HAnimSegment1825.USE = "hanim_r_metacarpal_2"

HAnimHumanoid42.segments.append(HAnimSegment1825)
HAnimJoint1826 = x3d.HAnimJoint()
HAnimJoint1826.USE = "hanim_r_metacarpophalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint1826)
HAnimSegment1827 = x3d.HAnimSegment()
HAnimSegment1827.USE = "hanim_r_carpal_proximal_phalanx_2"

HAnimHumanoid42.segments.append(HAnimSegment1827)
HAnimJoint1828 = x3d.HAnimJoint()
HAnimJoint1828.USE = "hanim_r_carpal_proximal_interphalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint1828)
HAnimSegment1829 = x3d.HAnimSegment()
HAnimSegment1829.USE = "hanim_r_carpal_middle_phalanx_2"

HAnimHumanoid42.segments.append(HAnimSegment1829)
HAnimSite1830 = x3d.HAnimSite()
HAnimSite1830.USE = "hanim_r_carpal_distal_phalanx_2_tip"

HAnimHumanoid42.sites.append(HAnimSite1830)
HAnimSite1831 = x3d.HAnimSite()
HAnimSite1831.USE = "hanim_r_dactylion_pt"

HAnimHumanoid42.sites.append(HAnimSite1831)
HAnimJoint1832 = x3d.HAnimJoint()
HAnimJoint1832.USE = "hanim_r_carpal_distal_interphalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint1832)
HAnimJoint1833 = x3d.HAnimJoint()
HAnimJoint1833.USE = "hanim_r_midcarpal_3"

HAnimHumanoid42.joints.append(HAnimJoint1833)
HAnimSegment1834 = x3d.HAnimSegment()
HAnimSegment1834.USE = "hanim_r_capitate"

HAnimHumanoid42.segments.append(HAnimSegment1834)
HAnimSite1835 = x3d.HAnimSite()
HAnimSite1835.USE = "hanim_r_metacarpal_phalanx_3_pt"

HAnimHumanoid42.sites.append(HAnimSite1835)
HAnimJoint1836 = x3d.HAnimJoint()
HAnimJoint1836.USE = "hanim_r_carpometacarpal_3"

HAnimHumanoid42.joints.append(HAnimJoint1836)
HAnimSegment1837 = x3d.HAnimSegment()
HAnimSegment1837.USE = "hanim_r_metacarpal_3"

HAnimHumanoid42.segments.append(HAnimSegment1837)
HAnimJoint1838 = x3d.HAnimJoint()
HAnimJoint1838.USE = "hanim_r_metacarpophalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint1838)
HAnimSegment1839 = x3d.HAnimSegment()
HAnimSegment1839.USE = "hanim_r_carpal_proximal_phalanx_3"

HAnimHumanoid42.segments.append(HAnimSegment1839)
HAnimJoint1840 = x3d.HAnimJoint()
HAnimJoint1840.USE = "hanim_r_carpal_proximal_interphalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint1840)
HAnimSegment1841 = x3d.HAnimSegment()
HAnimSegment1841.USE = "hanim_r_carpal_middle_phalanx_3"

HAnimHumanoid42.segments.append(HAnimSegment1841)
HAnimSite1842 = x3d.HAnimSite()
HAnimSite1842.USE = "hanim_r_carpal_distal_phalanx_3_tip"

HAnimHumanoid42.sites.append(HAnimSite1842)
HAnimJoint1843 = x3d.HAnimJoint()
HAnimJoint1843.USE = "hanim_r_carpal_distal_interphalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint1843)
HAnimJoint1844 = x3d.HAnimJoint()
HAnimJoint1844.USE = "hanim_r_midcarpal_4_5"

HAnimHumanoid42.joints.append(HAnimJoint1844)
HAnimSegment1845 = x3d.HAnimSegment()
HAnimSegment1845.USE = "hanim_r_hamate"

HAnimHumanoid42.segments.append(HAnimSegment1845)
HAnimSite1846 = x3d.HAnimSite()
HAnimSite1846.USE = "hanim_r_metacarpal_phalanx_5_pt"

HAnimHumanoid42.sites.append(HAnimSite1846)
HAnimJoint1847 = x3d.HAnimJoint()
HAnimJoint1847.USE = "hanim_r_carpometacarpal_4"

HAnimHumanoid42.joints.append(HAnimJoint1847)
HAnimSegment1848 = x3d.HAnimSegment()
HAnimSegment1848.USE = "hanim_r_metacarpal_4"

HAnimHumanoid42.segments.append(HAnimSegment1848)
HAnimJoint1849 = x3d.HAnimJoint()
HAnimJoint1849.USE = "hanim_r_metacarpophalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint1849)
HAnimSegment1850 = x3d.HAnimSegment()
HAnimSegment1850.USE = "hanim_r_carpal_proximal_phalanx_4"

HAnimHumanoid42.segments.append(HAnimSegment1850)
HAnimJoint1851 = x3d.HAnimJoint()
HAnimJoint1851.USE = "hanim_r_carpal_proximal_interphalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint1851)
HAnimSegment1852 = x3d.HAnimSegment()
HAnimSegment1852.USE = "hanim_r_carpal_middle_phalanx_4"

HAnimHumanoid42.segments.append(HAnimSegment1852)
HAnimSite1853 = x3d.HAnimSite()
HAnimSite1853.USE = "hanim_r_carpal_distal_phalanx_4_tip"

HAnimHumanoid42.sites.append(HAnimSite1853)
HAnimJoint1854 = x3d.HAnimJoint()
HAnimJoint1854.USE = "hanim_r_carpal_distal_interphalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint1854)
HAnimJoint1855 = x3d.HAnimJoint()
HAnimJoint1855.USE = "hanim_r_carpometacarpal_5"

HAnimHumanoid42.joints.append(HAnimJoint1855)
HAnimSegment1856 = x3d.HAnimSegment()
HAnimSegment1856.USE = "hanim_r_metacarpal_5"

HAnimHumanoid42.segments.append(HAnimSegment1856)
HAnimJoint1857 = x3d.HAnimJoint()
HAnimJoint1857.USE = "hanim_r_metacarpophalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint1857)
HAnimSegment1858 = x3d.HAnimSegment()
HAnimSegment1858.USE = "hanim_r_carpal_proximal_phalanx_5"

HAnimHumanoid42.segments.append(HAnimSegment1858)
HAnimJoint1859 = x3d.HAnimJoint()
HAnimJoint1859.USE = "hanim_r_carpal_proximal_interphalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint1859)
HAnimSegment1860 = x3d.HAnimSegment()
HAnimSegment1860.USE = "hanim_r_carpal_middle_phalanx_5"

HAnimHumanoid42.segments.append(HAnimSegment1860)
HAnimSite1861 = x3d.HAnimSite()
HAnimSite1861.USE = "hanim_r_carpal_distal_phalanx_5_tip"

HAnimHumanoid42.sites.append(HAnimSite1861)
HAnimJoint1862 = x3d.HAnimJoint()
HAnimJoint1862.USE = "hanim_r_carpal_distal_interphalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint1862)

HAnimHumanoid10.skeleton.append(HAnimHumanoid10)

X3D0.Scene = Scene10
f = open("skeleton8_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
