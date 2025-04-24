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
meta6.content = "h.pl"

head1.children.append(meta6)
meta7 = x3d.meta()
meta7.content = "John Carlson"
meta7.name = "creator"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.content = "12 June 2020"
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
HAnimHumanoid42.DEF = "STD_HAnim"
HAnimHumanoid42.info = ["humanoidVersion=2.0"]
HAnimHumanoid42.name = "HAnim"
HAnimHumanoid42.scale = [1,1,1]
HAnimHumanoid42.translation = [0,0,0]
HAnimHumanoid42.version = "2.0"
HAnimJoint43 = x3d.HAnimJoint()
HAnimJoint43.DEF = "STD_Joint_humanoid_root"
HAnimJoint43.name = "humanoid_root"
HAnimJoint43.center = [0.0000,0.8240,0.0277]
HAnimSegment44 = x3d.HAnimSegment()
HAnimSegment44.DEF = "STD_Segment_sacrum"
HAnimSegment44.name = "sacrum"
Transform45 = x3d.Transform()
Transform45.translation = [0.0000,0.8240,0.0277]
Shape46 = x3d.Shape()
Shape46.USE = "HAnimJointShape"

Transform45.children.append(Shape46)

HAnimSegment44.children.append(Transform45)
Transform47 = x3d.Transform()
Shape48 = x3d.Shape()
LineSet49 = x3d.LineSet()
LineSet49.vertexCount = [2]
Coordinate50 = x3d.Coordinate()

LineSet49.coord = Coordinate50
ColorRGBA51 = x3d.ColorRGBA()
ColorRGBA51.USE = "HAnimSegmentLineColorRGBA"

LineSet49.color = ColorRGBA51

Shape48.geometry = LineSet49

Transform47.children.append(Shape48)

HAnimSegment44.children.append(Transform47)

HAnimJoint43.children.append(HAnimSegment44)
HAnimJoint52 = x3d.HAnimJoint()
HAnimJoint52.DEF = "STD_Joint_sacroiliac"
HAnimJoint52.name = "sacroiliac"
HAnimJoint52.center = [0.0000,0.9149,0.0016]
HAnimSegment53 = x3d.HAnimSegment()
HAnimSegment53.DEF = "STD_Segment_pelvis"
HAnimSegment53.name = "pelvis"
Transform54 = x3d.Transform()
Transform54.translation = [0.0000,0.9149,0.0016]
Shape55 = x3d.Shape()
Shape55.USE = "HAnimJointShape"

Transform54.children.append(Shape55)

HAnimSegment53.children.append(Transform54)
Transform56 = x3d.Transform()
Shape57 = x3d.Shape()
LineSet58 = x3d.LineSet()
LineSet58.vertexCount = [2]
Coordinate59 = x3d.Coordinate()

LineSet58.coord = Coordinate59
ColorRGBA60 = x3d.ColorRGBA()
ColorRGBA60.USE = "HAnimSegmentLineColorRGBA"

LineSet58.color = ColorRGBA60

Shape57.geometry = LineSet58

Transform56.children.append(Shape57)

HAnimSegment53.children.append(Transform56)
HAnimSite61 = x3d.HAnimSite()
HAnimSite61.DEF = "STD_Site_buttocks_standing_wall_contact_point_pt"
HAnimSite61.name = "buttocks_standing_wall_contact_point_pt"
TouchSensor62 = x3d.TouchSensor()
TouchSensor62.description = "HAnimSite buttocks_standing_wall_contact_point_pt"

HAnimSite61.children.append(TouchSensor62)
Shape63 = x3d.Shape()
Shape63.USE = "HAnimSiteShape"

HAnimSite61.children.append(Shape63)

HAnimSegment53.children.append(HAnimSite61)
HAnimSite64 = x3d.HAnimSite()
HAnimSite64.DEF = "STD_Site_crotch_pt"
HAnimSite64.name = "crotch_pt"
HAnimSite64.translation = [0.0034,0.8266,0.0257]
TouchSensor65 = x3d.TouchSensor()
TouchSensor65.description = "HAnimSite crotch_pt"

HAnimSite64.children.append(TouchSensor65)
Shape66 = x3d.Shape()
Shape66.USE = "HAnimSiteShape"

HAnimSite64.children.append(Shape66)

HAnimSegment53.children.append(HAnimSite64)
HAnimSite67 = x3d.HAnimSite()
HAnimSite67.DEF = "STD_Site_l_asis_pt"
HAnimSite67.name = "l_asis_pt"
HAnimSite67.translation = [0.0925,0.9983,0.1052]
TouchSensor68 = x3d.TouchSensor()
TouchSensor68.description = "HAnimSite l_asis_pt"

HAnimSite67.children.append(TouchSensor68)
Shape69 = x3d.Shape()
Shape69.USE = "HAnimSiteShape"

HAnimSite67.children.append(Shape69)

HAnimSegment53.children.append(HAnimSite67)
HAnimSite70 = x3d.HAnimSite()
HAnimSite70.DEF = "STD_Site_l_iliocristale_pt"
HAnimSite70.name = "l_iliocristale_pt"
HAnimSite70.translation = [0.1612,1.0537,0.0008]
TouchSensor71 = x3d.TouchSensor()
TouchSensor71.description = "HAnimSite l_iliocristale_pt"

HAnimSite70.children.append(TouchSensor71)
Shape72 = x3d.Shape()
Shape72.USE = "HAnimSiteShape"

HAnimSite70.children.append(Shape72)

HAnimSegment53.children.append(HAnimSite70)
HAnimSite73 = x3d.HAnimSite()
HAnimSite73.DEF = "STD_Site_l_psis_pt"
HAnimSite73.name = "l_psis_pt"
HAnimSite73.translation = [0.0774,1.0190,-0.1151]
TouchSensor74 = x3d.TouchSensor()
TouchSensor74.description = "HAnimSite l_psis_pt"

HAnimSite73.children.append(TouchSensor74)
Shape75 = x3d.Shape()
Shape75.USE = "HAnimSiteShape"

HAnimSite73.children.append(Shape75)

HAnimSegment53.children.append(HAnimSite73)
HAnimSite76 = x3d.HAnimSite()
HAnimSite76.DEF = "STD_Site_l_trochanterion_pt"
HAnimSite76.name = "l_trochanterion_pt"
HAnimSite76.translation = [0.1677,0.8336,0.0303]
TouchSensor77 = x3d.TouchSensor()
TouchSensor77.description = "HAnimSite l_trochanterion_pt"

HAnimSite76.children.append(TouchSensor77)
Shape78 = x3d.Shape()
Shape78.USE = "HAnimSiteShape"

HAnimSite76.children.append(Shape78)

HAnimSegment53.children.append(HAnimSite76)
HAnimSite79 = x3d.HAnimSite()
HAnimSite79.DEF = "STD_Site_r_asis_pt"
HAnimSite79.name = "r_asis_pt"
HAnimSite79.translation = [-0.0887,1.0021,0.1112]
TouchSensor80 = x3d.TouchSensor()
TouchSensor80.description = "HAnimSite r_asis_pt"

HAnimSite79.children.append(TouchSensor80)
Shape81 = x3d.Shape()
Shape81.USE = "HAnimSiteShape"

HAnimSite79.children.append(Shape81)

HAnimSegment53.children.append(HAnimSite79)
HAnimSite82 = x3d.HAnimSite()
HAnimSite82.DEF = "STD_Site_r_iliocristale_pt"
HAnimSite82.name = "r_iliocristale_pt"
HAnimSite82.translation = [-0.1525,1.0628,0.0035]
TouchSensor83 = x3d.TouchSensor()
TouchSensor83.description = "HAnimSite r_iliocristale_pt"

HAnimSite82.children.append(TouchSensor83)
Shape84 = x3d.Shape()
Shape84.USE = "HAnimSiteShape"

HAnimSite82.children.append(Shape84)

HAnimSegment53.children.append(HAnimSite82)
HAnimSite85 = x3d.HAnimSite()
HAnimSite85.DEF = "STD_Site_r_psis_pt"
HAnimSite85.name = "r_psis_pt"
HAnimSite85.translation = [-0.0716,1.0190,-0.1138]
TouchSensor86 = x3d.TouchSensor()
TouchSensor86.description = "HAnimSite r_psis_pt"

HAnimSite85.children.append(TouchSensor86)
Shape87 = x3d.Shape()
Shape87.USE = "HAnimSiteShape"

HAnimSite85.children.append(Shape87)

HAnimSegment53.children.append(HAnimSite85)
HAnimSite88 = x3d.HAnimSite()
HAnimSite88.DEF = "STD_Site_r_trochanterion_pt"
HAnimSite88.name = "r_trochanterion_pt"
HAnimSite88.translation = [-0.1689,0.8419,0.0352]
TouchSensor89 = x3d.TouchSensor()
TouchSensor89.description = "HAnimSite r_trochanterion_pt"

HAnimSite88.children.append(TouchSensor89)
Shape90 = x3d.Shape()
Shape90.USE = "HAnimSiteShape"

HAnimSite88.children.append(Shape90)

HAnimSegment53.children.append(HAnimSite88)

HAnimJoint52.children.append(HAnimSegment53)
HAnimJoint91 = x3d.HAnimJoint()
HAnimJoint91.DEF = "STD_Joint_l_hip"
HAnimJoint91.name = "l_hip"
HAnimJoint91.center = [0.0961,0.9124,-0.0001]
HAnimSegment92 = x3d.HAnimSegment()
HAnimSegment92.DEF = "STD_Segment_l_thigh"
HAnimSegment92.name = "l_thigh"
Transform93 = x3d.Transform()
Transform93.translation = [0.0961,0.9124,-0.0001]
Shape94 = x3d.Shape()
Shape94.USE = "HAnimJointShape"

Transform93.children.append(Shape94)

HAnimSegment92.children.append(Transform93)
Transform95 = x3d.Transform()
Shape96 = x3d.Shape()
LineSet97 = x3d.LineSet()
LineSet97.vertexCount = [2]
Coordinate98 = x3d.Coordinate()

LineSet97.coord = Coordinate98
ColorRGBA99 = x3d.ColorRGBA()
ColorRGBA99.USE = "HAnimSegmentLineColorRGBA"

LineSet97.color = ColorRGBA99

Shape96.geometry = LineSet97

Transform95.children.append(Shape96)

HAnimSegment92.children.append(Transform95)
HAnimSite100 = x3d.HAnimSite()
HAnimSite100.DEF = "STD_Site_l_femoral_lateral_epicondyles_pt"
HAnimSite100.name = "l_femoral_lateral_epicondyles_pt"
HAnimSite100.translation = [0.1598,0.4967,0.0297]
TouchSensor101 = x3d.TouchSensor()
TouchSensor101.description = "HAnimSite l_femoral_lateral_epicondyles_pt"

HAnimSite100.children.append(TouchSensor101)
Shape102 = x3d.Shape()
Shape102.USE = "HAnimSiteShape"

HAnimSite100.children.append(Shape102)

HAnimSegment92.children.append(HAnimSite100)
HAnimSite103 = x3d.HAnimSite()
HAnimSite103.DEF = "STD_Site_l_femoral_medial_epicondyles_pt"
HAnimSite103.name = "l_femoral_medial_epicondyles_pt"
HAnimSite103.translation = [0.0398,0.4946,0.0303]
TouchSensor104 = x3d.TouchSensor()
TouchSensor104.description = "HAnimSite l_femoral_medial_epicondyles_pt"

HAnimSite103.children.append(TouchSensor104)
Shape105 = x3d.Shape()
Shape105.USE = "HAnimSiteShape"

HAnimSite103.children.append(Shape105)

HAnimSegment92.children.append(HAnimSite103)
HAnimSite106 = x3d.HAnimSite()
HAnimSite106.DEF = "STD_Site_l_knee_crease_pt"
HAnimSite106.name = "l_knee_crease_pt"
HAnimSite106.translation = [0.0993,0.4881,-0.0309]
TouchSensor107 = x3d.TouchSensor()
TouchSensor107.description = "HAnimSite l_knee_crease_pt"

HAnimSite106.children.append(TouchSensor107)
Shape108 = x3d.Shape()
Shape108.USE = "HAnimSiteShape"

HAnimSite106.children.append(Shape108)

HAnimSegment92.children.append(HAnimSite106)
HAnimSite109 = x3d.HAnimSite()
HAnimSite109.DEF = "STD_Site_l_suprapatella_pt"
HAnimSite109.name = "l_suprapatella_pt"
TouchSensor110 = x3d.TouchSensor()
TouchSensor110.description = "HAnimSite l_suprapatella_pt"

HAnimSite109.children.append(TouchSensor110)
Shape111 = x3d.Shape()
Shape111.USE = "HAnimSiteShape"

HAnimSite109.children.append(Shape111)

HAnimSegment92.children.append(HAnimSite109)

HAnimJoint91.children.append(HAnimSegment92)
HAnimJoint112 = x3d.HAnimJoint()
HAnimJoint112.DEF = "STD_Joint_l_knee"
HAnimJoint112.name = "l_knee"
HAnimJoint112.center = [0.1040,0.4867,0.0308]
HAnimSegment113 = x3d.HAnimSegment()
HAnimSegment113.DEF = "STD_Segment_l_calf"
HAnimSegment113.name = "l_calf"
Transform114 = x3d.Transform()
Transform114.translation = [0.1040,0.4867,0.0308]
Shape115 = x3d.Shape()
Shape115.USE = "HAnimJointShape"

Transform114.children.append(Shape115)

HAnimSegment113.children.append(Transform114)
Transform116 = x3d.Transform()
Shape117 = x3d.Shape()
LineSet118 = x3d.LineSet()
LineSet118.vertexCount = [2]
Coordinate119 = x3d.Coordinate()

LineSet118.coord = Coordinate119
ColorRGBA120 = x3d.ColorRGBA()
ColorRGBA120.USE = "HAnimSegmentLineColorRGBA"

LineSet118.color = ColorRGBA120

Shape117.geometry = LineSet118

Transform116.children.append(Shape117)

HAnimSegment113.children.append(Transform116)
HAnimSite121 = x3d.HAnimSite()
HAnimSite121.DEF = "STD_Site_l_lateral_malleolus_pt"
HAnimSite121.name = "l_lateral_malleolus_pt"
HAnimSite121.translation = [0.1308,0.0597,-0.1032]
TouchSensor122 = x3d.TouchSensor()
TouchSensor122.description = "HAnimSite l_lateral_malleolus_pt"

HAnimSite121.children.append(TouchSensor122)
Shape123 = x3d.Shape()
Shape123.USE = "HAnimSiteShape"

HAnimSite121.children.append(Shape123)

HAnimSegment113.children.append(HAnimSite121)
HAnimSite124 = x3d.HAnimSite()
HAnimSite124.DEF = "STD_Site_l_medial_malleolus_pt"
HAnimSite124.name = "l_medial_malleolus_pt"
HAnimSite124.translation = [0.0890,0.0716,-0.0881]
TouchSensor125 = x3d.TouchSensor()
TouchSensor125.description = "HAnimSite l_medial_malleolus_pt"

HAnimSite124.children.append(TouchSensor125)
Shape126 = x3d.Shape()
Shape126.USE = "HAnimSiteShape"

HAnimSite124.children.append(Shape126)

HAnimSegment113.children.append(HAnimSite124)
HAnimSite127 = x3d.HAnimSite()
HAnimSite127.DEF = "STD_Site_l_tibiale_pt"
HAnimSite127.name = "l_tibiale_pt"
TouchSensor128 = x3d.TouchSensor()
TouchSensor128.description = "HAnimSite l_tibiale_pt"

HAnimSite127.children.append(TouchSensor128)
Shape129 = x3d.Shape()
Shape129.USE = "HAnimSiteShape"

HAnimSite127.children.append(Shape129)

HAnimSegment113.children.append(HAnimSite127)

HAnimJoint112.children.append(HAnimSegment113)
HAnimJoint130 = x3d.HAnimJoint()
HAnimJoint130.DEF = "STD_Joint_l_talocrural"
HAnimJoint130.name = "l_talocrural"
HAnimJoint130.center = [0.1101,0.0656,-0.0736]
HAnimSegment131 = x3d.HAnimSegment()
HAnimSegment131.DEF = "STD_Segment_l_talus"
HAnimSegment131.name = "l_talus"
Transform132 = x3d.Transform()
Transform132.translation = [0.1101,0.0656,-0.0736]
Shape133 = x3d.Shape()
Shape133.USE = "HAnimJointShape"

Transform132.children.append(Shape133)

HAnimSegment131.children.append(Transform132)
Transform134 = x3d.Transform()
Shape135 = x3d.Shape()
LineSet136 = x3d.LineSet()
LineSet136.vertexCount = [2]
Coordinate137 = x3d.Coordinate()

LineSet136.coord = Coordinate137
ColorRGBA138 = x3d.ColorRGBA()
ColorRGBA138.USE = "HAnimSegmentLineColorRGBA"

LineSet136.color = ColorRGBA138

Shape135.geometry = LineSet136

Transform134.children.append(Shape135)

HAnimSegment131.children.append(Transform134)
HAnimSite139 = x3d.HAnimSite()
HAnimSite139.DEF = "STD_Site_l_calcaneus_posterior_pt"
HAnimSite139.name = "l_calcaneus_posterior_pt"
HAnimSite139.translation = [0.0974,0.0259,-0.1171]
TouchSensor140 = x3d.TouchSensor()
TouchSensor140.description = "HAnimSite l_calcaneus_posterior_pt"

HAnimSite139.children.append(TouchSensor140)
Shape141 = x3d.Shape()
Shape141.USE = "HAnimSiteShape"

HAnimSite139.children.append(Shape141)

HAnimSegment131.children.append(HAnimSite139)
HAnimSite142 = x3d.HAnimSite()
HAnimSite142.DEF = "STD_Site_l_sphyrion_pt"
HAnimSite142.name = "l_sphyrion_pt"
HAnimSite142.translation = [0.0890,0.0575,-0.0943]
TouchSensor143 = x3d.TouchSensor()
TouchSensor143.description = "HAnimSite l_sphyrion_pt"

HAnimSite142.children.append(TouchSensor143)
Shape144 = x3d.Shape()
Shape144.USE = "HAnimSiteShape"

HAnimSite142.children.append(Shape144)

HAnimSegment131.children.append(HAnimSite142)

HAnimJoint130.children.append(HAnimSegment131)
HAnimJoint145 = x3d.HAnimJoint()
HAnimJoint145.DEF = "STD_Joint_l_talocalcaneonavicular"
HAnimJoint145.name = "l_talocalcaneonavicular"
HAnimSegment146 = x3d.HAnimSegment()
HAnimSegment146.DEF = "STD_Segment_l_navicular"
HAnimSegment146.name = "l_navicular"
Transform147 = x3d.Transform()
Shape148 = x3d.Shape()
LineSet149 = x3d.LineSet()
LineSet149.vertexCount = [2]
Coordinate150 = x3d.Coordinate()

LineSet149.coord = Coordinate150
ColorRGBA151 = x3d.ColorRGBA()
ColorRGBA151.USE = "HAnimSegmentLineColorRGBA"

LineSet149.color = ColorRGBA151

Shape148.geometry = LineSet149

Transform147.children.append(Shape148)

HAnimSegment146.children.append(Transform147)

HAnimJoint145.children.append(HAnimSegment146)
HAnimJoint152 = x3d.HAnimJoint()
HAnimJoint152.DEF = "STD_Joint_l_cuneonavicular_1"
HAnimJoint152.name = "l_cuneonavicular_1"
HAnimSegment153 = x3d.HAnimSegment()
HAnimSegment153.DEF = "STD_Segment_l_cuneiform_1"
HAnimSegment153.name = "l_cuneiform_1"

HAnimJoint152.children.append(HAnimSegment153)
HAnimJoint154 = x3d.HAnimJoint()
HAnimJoint154.DEF = "STD_Joint_l_tarsometatarsal_1"
HAnimJoint154.name = "l_tarsometatarsal_1"
HAnimSegment155 = x3d.HAnimSegment()
HAnimSegment155.DEF = "STD_Segment_l_metatarsal_1"
HAnimSegment155.name = "l_metatarsal_1"

HAnimJoint154.children.append(HAnimSegment155)
HAnimJoint156 = x3d.HAnimJoint()
HAnimJoint156.DEF = "STD_Joint_l_metatarsophalangeal_1"
HAnimJoint156.name = "l_metatarsophalangeal_1"
HAnimSegment157 = x3d.HAnimSegment()
HAnimSegment157.DEF = "STD_Segment_l_tarsal_proximal_phalanx_1"
HAnimSegment157.name = "l_tarsal_proximal_phalanx_1"
HAnimSite158 = x3d.HAnimSite()
HAnimSite158.DEF = "STD_Site_l_metatarsal_phalanx_1_pt"
HAnimSite158.name = "l_metatarsal_phalanx_1_pt"
TouchSensor159 = x3d.TouchSensor()
TouchSensor159.description = "HAnimSite l_metatarsal_phalanx_1_pt"

HAnimSite158.children.append(TouchSensor159)
Shape160 = x3d.Shape()
Shape160.USE = "HAnimSiteShape"

HAnimSite158.children.append(Shape160)

HAnimSegment157.children.append(HAnimSite158)

HAnimJoint156.children.append(HAnimSegment157)
HAnimJoint161 = x3d.HAnimJoint()
HAnimJoint161.DEF = "STD_Joint_l_tarsal_interphalangeal_1"
HAnimJoint161.name = "l_tarsal_interphalangeal_1"
HAnimSegment162 = x3d.HAnimSegment()
HAnimSegment162.DEF = "STD_Segment_l_tarsal_distal_phalanx_1"
HAnimSegment162.name = "l_tarsal_distal_phalanx_1"
HAnimSite163 = x3d.HAnimSite()
HAnimSite163.DEF = "STD_Site_l_tarsal_distal_phalanx_1_tip"
HAnimSite163.name = "l_tarsal_distal_phalanx_1_tip"
TouchSensor164 = x3d.TouchSensor()
TouchSensor164.description = "HAnimSite l_tarsal_distal_phalanx_1_tip"

HAnimSite163.children.append(TouchSensor164)
Shape165 = x3d.Shape()
Shape165.USE = "HAnimSiteShape"

HAnimSite163.children.append(Shape165)

HAnimSegment162.children.append(HAnimSite163)

HAnimJoint161.children.append(HAnimSegment162)

HAnimJoint156.children.append(HAnimJoint161)

HAnimJoint154.children.append(HAnimJoint156)

HAnimJoint152.children.append(HAnimJoint154)

HAnimJoint145.children.append(HAnimJoint152)
HAnimJoint166 = x3d.HAnimJoint()
HAnimJoint166.DEF = "STD_Joint_l_cuneonavicular_2"
HAnimJoint166.name = "l_cuneonavicular_2"
HAnimSegment167 = x3d.HAnimSegment()
HAnimSegment167.DEF = "STD_Segment_l_cuneiform_2"
HAnimSegment167.name = "l_cuneiform_2"

HAnimJoint166.children.append(HAnimSegment167)
HAnimJoint168 = x3d.HAnimJoint()
HAnimJoint168.DEF = "STD_Joint_l_tarsometatarsal_2"
HAnimJoint168.name = "l_tarsometatarsal_2"
HAnimSegment169 = x3d.HAnimSegment()
HAnimSegment169.DEF = "STD_Segment_l_metatarsal_2"
HAnimSegment169.name = "l_metatarsal_2"

HAnimJoint168.children.append(HAnimSegment169)
HAnimJoint170 = x3d.HAnimJoint()
HAnimJoint170.DEF = "STD_Joint_l_metatarsophalangeal_2"
HAnimJoint170.name = "l_metatarsophalangeal_2"
HAnimSegment171 = x3d.HAnimSegment()
HAnimSegment171.DEF = "STD_Segment_l_tarsal_proximal_phalanx_2"
HAnimSegment171.name = "l_tarsal_proximal_phalanx_2"

HAnimJoint170.children.append(HAnimSegment171)
HAnimJoint172 = x3d.HAnimJoint()
HAnimJoint172.DEF = "STD_Joint_l_tarsal_proximal_interphalangeal_2"
HAnimJoint172.name = "l_tarsal_proximal_interphalangeal_2"
HAnimSegment173 = x3d.HAnimSegment()
HAnimSegment173.DEF = "STD_Segment_l_tarsal_middle_phalanx_2"
HAnimSegment173.name = "l_tarsal_middle_phalanx_2"

HAnimJoint172.children.append(HAnimSegment173)
HAnimJoint174 = x3d.HAnimJoint()
HAnimJoint174.DEF = "STD_Joint_l_tarsal_distal_interphalangeal_2"
HAnimJoint174.name = "l_tarsal_distal_interphalangeal_2"
HAnimSegment175 = x3d.HAnimSegment()
HAnimSegment175.DEF = "STD_Segment_l_tarsal_distal_phalanx_2"
HAnimSegment175.name = "l_tarsal_distal_phalanx_2"
HAnimSite176 = x3d.HAnimSite()
HAnimSite176.DEF = "STD_Site_l_tarsal_distal_phalanx_2_tip"
HAnimSite176.name = "l_tarsal_distal_phalanx_2_tip"
HAnimSite176.translation = [0.1195,0.0079,0.1433]
TouchSensor177 = x3d.TouchSensor()
TouchSensor177.description = "HAnimSite l_tarsal_distal_phalanx_2_tip"

HAnimSite176.children.append(TouchSensor177)
Shape178 = x3d.Shape()
Shape178.USE = "HAnimSiteShape"

HAnimSite176.children.append(Shape178)

HAnimSegment175.children.append(HAnimSite176)

HAnimJoint174.children.append(HAnimSegment175)

HAnimJoint172.children.append(HAnimJoint174)

HAnimJoint170.children.append(HAnimJoint172)

HAnimJoint168.children.append(HAnimJoint170)

HAnimJoint166.children.append(HAnimJoint168)

HAnimJoint145.children.append(HAnimJoint166)
HAnimJoint179 = x3d.HAnimJoint()
HAnimJoint179.DEF = "STD_Joint_l_cuneonavicular_3"
HAnimJoint179.name = "l_cuneonavicular_3"
HAnimSegment180 = x3d.HAnimSegment()
HAnimSegment180.DEF = "STD_Segment_l_cuneiform_3"
HAnimSegment180.name = "l_cuneiform_3"

HAnimJoint179.children.append(HAnimSegment180)
HAnimJoint181 = x3d.HAnimJoint()
HAnimJoint181.DEF = "STD_Joint_l_tarsometatarsal_3 "
HAnimJoint181.name = "l_tarsometatarsal_3 "
HAnimSegment182 = x3d.HAnimSegment()
HAnimSegment182.DEF = "STD_Segment_l_metatarsal_3"
HAnimSegment182.name = "l_metatarsal_3"

HAnimJoint181.children.append(HAnimSegment182)
HAnimJoint183 = x3d.HAnimJoint()
HAnimJoint183.DEF = "STD_Joint_l_metatarsophalangeal_3"
HAnimJoint183.name = "l_metatarsophalangeal_3"
HAnimSegment184 = x3d.HAnimSegment()
HAnimSegment184.DEF = "STD_Segment_l_tarsal_proximal_phalanx_3"
HAnimSegment184.name = "l_tarsal_proximal_phalanx_3"

HAnimJoint183.children.append(HAnimSegment184)
HAnimJoint185 = x3d.HAnimJoint()
HAnimJoint185.DEF = "STD_Joint_l_tarsal_proximal_interphalangeal_3"
HAnimJoint185.name = "l_tarsal_proximal_interphalangeal_3"
HAnimSegment186 = x3d.HAnimSegment()
HAnimSegment186.DEF = "STD_Segment_l_tarsal_middle_phalanx_3"
HAnimSegment186.name = "l_tarsal_middle_phalanx_3"

HAnimJoint185.children.append(HAnimSegment186)
HAnimJoint187 = x3d.HAnimJoint()
HAnimJoint187.DEF = "STD_Joint_l_tarsal_distal_interphalangeal_3"
HAnimJoint187.name = "l_tarsal_distal_interphalangeal_3"
HAnimSegment188 = x3d.HAnimSegment()
HAnimSegment188.DEF = "STD_Segment_l_tarsal_distal_phalanx_3"
HAnimSegment188.name = "l_tarsal_distal_phalanx_3"
HAnimSite189 = x3d.HAnimSite()
HAnimSite189.DEF = "STD_Site_l_tarsal_distal_phalanx_3_tip"
HAnimSite189.name = "l_tarsal_distal_phalanx_3_tip"
TouchSensor190 = x3d.TouchSensor()
TouchSensor190.description = "HAnimSite l_tarsal_distal_phalanx_3_tip"

HAnimSite189.children.append(TouchSensor190)
Shape191 = x3d.Shape()
Shape191.USE = "HAnimSiteShape"

HAnimSite189.children.append(Shape191)

HAnimSegment188.children.append(HAnimSite189)

HAnimJoint187.children.append(HAnimSegment188)

HAnimJoint185.children.append(HAnimJoint187)

HAnimJoint183.children.append(HAnimJoint185)

HAnimJoint181.children.append(HAnimJoint183)

HAnimJoint179.children.append(HAnimJoint181)

HAnimJoint145.children.append(HAnimJoint179)

HAnimJoint130.children.append(HAnimJoint145)
HAnimJoint192 = x3d.HAnimJoint()
HAnimJoint192.DEF = "STD_Joint_l_calcaneocuboid"
HAnimJoint192.name = "l_calcaneocuboid"
HAnimSegment193 = x3d.HAnimSegment()
HAnimSegment193.DEF = "STD_Segment_l_calcaneus"
HAnimSegment193.name = "l_calcaneus"

HAnimJoint192.children.append(HAnimSegment193)
HAnimJoint194 = x3d.HAnimJoint()
HAnimJoint194.DEF = "STD_Joint_l_transversetarsal"
HAnimJoint194.name = "l_transversetarsal"
HAnimSegment195 = x3d.HAnimSegment()
HAnimSegment195.DEF = "STD_Segment_l_cuboid"
HAnimSegment195.name = "l_cuboid"

HAnimJoint194.children.append(HAnimSegment195)
HAnimJoint196 = x3d.HAnimJoint()
HAnimJoint196.DEF = "STD_Joint_l_tarsometatarsal_4"
HAnimJoint196.name = "l_tarsometatarsal_4"
HAnimSegment197 = x3d.HAnimSegment()
HAnimSegment197.DEF = "STD_Segment_l_metatarsal_4"
HAnimSegment197.name = "l_metatarsal_4"

HAnimJoint196.children.append(HAnimSegment197)
HAnimJoint198 = x3d.HAnimJoint()
HAnimJoint198.DEF = "STD_Joint_l_metatarsophalangeal_4"
HAnimJoint198.name = "l_metatarsophalangeal_4"
HAnimSegment199 = x3d.HAnimSegment()
HAnimSegment199.DEF = "STD_Segment_l_tarsal_proximal_phalanx_4"
HAnimSegment199.name = "l_tarsal_proximal_phalanx_4"

HAnimJoint198.children.append(HAnimSegment199)
HAnimJoint200 = x3d.HAnimJoint()
HAnimJoint200.DEF = "STD_Joint_l_tarsal_proximal_interphalangeal_4"
HAnimJoint200.name = "l_tarsal_proximal_interphalangeal_4"
HAnimSegment201 = x3d.HAnimSegment()
HAnimSegment201.DEF = "STD_Segment_l_tarsal_middle_phalanx_4"
HAnimSegment201.name = "l_tarsal_middle_phalanx_4"

HAnimJoint200.children.append(HAnimSegment201)
HAnimJoint202 = x3d.HAnimJoint()
HAnimJoint202.DEF = "STD_Joint_l_tarsal_distal_interphalangeal_4"
HAnimJoint202.name = "l_tarsal_distal_interphalangeal_4"
HAnimSegment203 = x3d.HAnimSegment()
HAnimSegment203.DEF = "STD_Segment_l_tarsal_distal_phalanx_4"
HAnimSegment203.name = "l_tarsal_distal_phalanx_4"
HAnimSite204 = x3d.HAnimSite()
HAnimSite204.DEF = "STD_Site_l_tarsal_distal_phalanx_4_tip"
HAnimSite204.name = "l_tarsal_distal_phalanx_4_tip"
TouchSensor205 = x3d.TouchSensor()
TouchSensor205.description = "HAnimSite l_tarsal_distal_phalanx_4_tip"

HAnimSite204.children.append(TouchSensor205)
Shape206 = x3d.Shape()
Shape206.USE = "HAnimSiteShape"

HAnimSite204.children.append(Shape206)

HAnimSegment203.children.append(HAnimSite204)

HAnimJoint202.children.append(HAnimSegment203)

HAnimJoint200.children.append(HAnimJoint202)

HAnimJoint198.children.append(HAnimJoint200)

HAnimJoint196.children.append(HAnimJoint198)

HAnimJoint194.children.append(HAnimJoint196)
HAnimJoint207 = x3d.HAnimJoint()
HAnimJoint207.DEF = "STD_Joint_l_tarsometatarsal_5"
HAnimJoint207.name = "l_tarsometatarsal_5"
HAnimSegment208 = x3d.HAnimSegment()
HAnimSegment208.DEF = "STD_Segment_l_metatarsal_5"
HAnimSegment208.name = "l_metatarsal_5"

HAnimJoint207.children.append(HAnimSegment208)
HAnimJoint209 = x3d.HAnimJoint()
HAnimJoint209.DEF = "STD_Joint_l_metatarsophalangeal_5"
HAnimJoint209.name = "l_metatarsophalangeal_5"
HAnimSegment210 = x3d.HAnimSegment()
HAnimSegment210.DEF = "STD_Segment_l_tarsal_proximal_phalanx_5"
HAnimSegment210.name = "l_tarsal_proximal_phalanx_5"
HAnimSite211 = x3d.HAnimSite()
HAnimSite211.DEF = "STD_Site_l_metatarsal_phalanx_5_pt"
HAnimSite211.name = "l_metatarsal_phalanx_5_pt"
TouchSensor212 = x3d.TouchSensor()
TouchSensor212.description = "HAnimSite l_metatarsal_phalanx_5_pt"

HAnimSite211.children.append(TouchSensor212)
Shape213 = x3d.Shape()
Shape213.USE = "HAnimSiteShape"

HAnimSite211.children.append(Shape213)

HAnimSegment210.children.append(HAnimSite211)

HAnimJoint209.children.append(HAnimSegment210)
HAnimJoint214 = x3d.HAnimJoint()
HAnimJoint214.DEF = "STD_Joint_l_tarsal_proximal_interphalangeal_5"
HAnimJoint214.name = "l_tarsal_proximal_interphalangeal_5"
HAnimSegment215 = x3d.HAnimSegment()
HAnimSegment215.DEF = "STD_Segment_l_tarsal_middle_phalanx_5"
HAnimSegment215.name = "l_tarsal_middle_phalanx_5"

HAnimJoint214.children.append(HAnimSegment215)
HAnimJoint216 = x3d.HAnimJoint()
HAnimJoint216.DEF = "STD_Joint_l_tarsal_distal_interphalangeal_5"
HAnimJoint216.name = "l_tarsal_distal_interphalangeal_5"
HAnimSegment217 = x3d.HAnimSegment()
HAnimSegment217.DEF = "STD_Segment_l_tarsal_distal_phalanx_5"
HAnimSegment217.name = "l_tarsal_distal_phalanx_5"
HAnimSite218 = x3d.HAnimSite()
HAnimSite218.DEF = "STD_Site_l_tarsal_distal_phalanx_5_tip"
HAnimSite218.name = "l_tarsal_distal_phalanx_5_tip"
TouchSensor219 = x3d.TouchSensor()
TouchSensor219.description = "HAnimSite l_tarsal_distal_phalanx_5_tip"

HAnimSite218.children.append(TouchSensor219)
Shape220 = x3d.Shape()
Shape220.USE = "HAnimSiteShape"

HAnimSite218.children.append(Shape220)

HAnimSegment217.children.append(HAnimSite218)

HAnimJoint216.children.append(HAnimSegment217)

HAnimJoint214.children.append(HAnimJoint216)

HAnimJoint209.children.append(HAnimJoint214)

HAnimJoint207.children.append(HAnimJoint209)

HAnimJoint194.children.append(HAnimJoint207)

HAnimJoint192.children.append(HAnimJoint194)

HAnimJoint130.children.append(HAnimJoint192)

HAnimJoint112.children.append(HAnimJoint130)

HAnimJoint91.children.append(HAnimJoint112)

HAnimJoint52.children.append(HAnimJoint91)
HAnimJoint221 = x3d.HAnimJoint()
HAnimJoint221.DEF = "STD_Joint_r_hip"
HAnimJoint221.name = "r_hip"
HAnimJoint221.center = [-0.0950,0.9171,0.0029]
HAnimSegment222 = x3d.HAnimSegment()
HAnimSegment222.DEF = "STD_Segment_r_thigh"
HAnimSegment222.name = "r_thigh"
Transform223 = x3d.Transform()
Transform223.translation = [-0.0950,0.9171,0.0029]
Shape224 = x3d.Shape()
Shape224.USE = "HAnimJointShape"

Transform223.children.append(Shape224)

HAnimSegment222.children.append(Transform223)
Transform225 = x3d.Transform()
Shape226 = x3d.Shape()
LineSet227 = x3d.LineSet()
LineSet227.vertexCount = [2]
Coordinate228 = x3d.Coordinate()

LineSet227.coord = Coordinate228
ColorRGBA229 = x3d.ColorRGBA()
ColorRGBA229.USE = "HAnimSegmentLineColorRGBA"

LineSet227.color = ColorRGBA229

Shape226.geometry = LineSet227

Transform225.children.append(Shape226)

HAnimSegment222.children.append(Transform225)
HAnimSite230 = x3d.HAnimSite()
HAnimSite230.DEF = "STD_Site_r_femoral_lateral_epicondyles_pt"
HAnimSite230.name = "r_femoral_lateral_epicondyles_pt"
HAnimSite230.translation = [-0.1421,0.4992,0.0310]
TouchSensor231 = x3d.TouchSensor()
TouchSensor231.description = "HAnimSite r_femoral_lateral_epicondyles_pt"

HAnimSite230.children.append(TouchSensor231)
Shape232 = x3d.Shape()
Shape232.USE = "HAnimSiteShape"

HAnimSite230.children.append(Shape232)

HAnimSegment222.children.append(HAnimSite230)
HAnimSite233 = x3d.HAnimSite()
HAnimSite233.DEF = "STD_Site_r_femoral_medial_epicondyles_pt"
HAnimSite233.name = "r_femoral_medial_epicondyles_pt"
HAnimSite233.translation = [-0.0221,0.5014,0.0289]
TouchSensor234 = x3d.TouchSensor()
TouchSensor234.description = "HAnimSite r_femoral_medial_epicondyles_pt"

HAnimSite233.children.append(TouchSensor234)
Shape235 = x3d.Shape()
Shape235.USE = "HAnimSiteShape"

HAnimSite233.children.append(Shape235)

HAnimSegment222.children.append(HAnimSite233)
HAnimSite236 = x3d.HAnimSite()
HAnimSite236.DEF = "STD_Site_r_knee_crease_pt"
HAnimSite236.name = "r_knee_crease_pt"
HAnimSite236.translation = [-0.0825,0.4932,-0.0326]
TouchSensor237 = x3d.TouchSensor()
TouchSensor237.description = "HAnimSite r_knee_crease_pt"

HAnimSite236.children.append(TouchSensor237)
Shape238 = x3d.Shape()
Shape238.USE = "HAnimSiteShape"

HAnimSite236.children.append(Shape238)

HAnimSegment222.children.append(HAnimSite236)
HAnimSite239 = x3d.HAnimSite()
HAnimSite239.DEF = "STD_Site_r_suprapatella_pt"
HAnimSite239.name = "r_suprapatella_pt"
TouchSensor240 = x3d.TouchSensor()
TouchSensor240.description = "HAnimSite r_suprapatella_pt"

HAnimSite239.children.append(TouchSensor240)
Shape241 = x3d.Shape()
Shape241.USE = "HAnimSiteShape"

HAnimSite239.children.append(Shape241)

HAnimSegment222.children.append(HAnimSite239)

HAnimJoint221.children.append(HAnimSegment222)
HAnimJoint242 = x3d.HAnimJoint()
HAnimJoint242.DEF = "STD_Joint_r_knee"
HAnimJoint242.name = "r_knee"
HAnimJoint242.center = [-0.0867,0.4913,0.0318]
HAnimSegment243 = x3d.HAnimSegment()
HAnimSegment243.DEF = "STD_Segment_r_calf"
HAnimSegment243.name = "r_calf"
Transform244 = x3d.Transform()
Transform244.translation = [-0.0867,0.4913,0.0318]
Shape245 = x3d.Shape()
Shape245.USE = "HAnimJointShape"

Transform244.children.append(Shape245)

HAnimSegment243.children.append(Transform244)
Transform246 = x3d.Transform()
Shape247 = x3d.Shape()
LineSet248 = x3d.LineSet()
LineSet248.vertexCount = [2]
Coordinate249 = x3d.Coordinate()

LineSet248.coord = Coordinate249
ColorRGBA250 = x3d.ColorRGBA()
ColorRGBA250.USE = "HAnimSegmentLineColorRGBA"

LineSet248.color = ColorRGBA250

Shape247.geometry = LineSet248

Transform246.children.append(Shape247)

HAnimSegment243.children.append(Transform246)
HAnimSite251 = x3d.HAnimSite()
HAnimSite251.DEF = "STD_Site_r_lateral_malleolus_pt"
HAnimSite251.name = "r_lateral_malleolus_pt"
HAnimSite251.translation = [-0.1006,0.0658,-0.1075]
TouchSensor252 = x3d.TouchSensor()
TouchSensor252.description = "HAnimSite r_lateral_malleolus_pt"

HAnimSite251.children.append(TouchSensor252)
Shape253 = x3d.Shape()
Shape253.USE = "HAnimSiteShape"

HAnimSite251.children.append(Shape253)

HAnimSegment243.children.append(HAnimSite251)
HAnimSite254 = x3d.HAnimSite()
HAnimSite254.DEF = "STD_Site_r_medial_malleolus_pt"
HAnimSite254.name = "r_medial_malleolus_pt"
HAnimSite254.translation = [-0.0591,0.0760,-0.0928]
TouchSensor255 = x3d.TouchSensor()
TouchSensor255.description = "HAnimSite r_medial_malleolus_pt"

HAnimSite254.children.append(TouchSensor255)
Shape256 = x3d.Shape()
Shape256.USE = "HAnimSiteShape"

HAnimSite254.children.append(Shape256)

HAnimSegment243.children.append(HAnimSite254)
HAnimSite257 = x3d.HAnimSite()
HAnimSite257.DEF = "STD_Site_r_tibiale_pt"
HAnimSite257.name = "r_tibiale_pt"
TouchSensor258 = x3d.TouchSensor()
TouchSensor258.description = "HAnimSite r_tibiale_pt"

HAnimSite257.children.append(TouchSensor258)
Shape259 = x3d.Shape()
Shape259.USE = "HAnimSiteShape"

HAnimSite257.children.append(Shape259)

HAnimSegment243.children.append(HAnimSite257)

HAnimJoint242.children.append(HAnimSegment243)
HAnimJoint260 = x3d.HAnimJoint()
HAnimJoint260.DEF = "STD_Joint_r_talocrural"
HAnimJoint260.name = "r_talocrural"
HAnimJoint260.center = [-0.0801,0.0712,-0.0766]
HAnimSegment261 = x3d.HAnimSegment()
HAnimSegment261.DEF = "STD_Segment_r_talus"
HAnimSegment261.name = "r_talus"
Transform262 = x3d.Transform()
Transform262.translation = [-0.0801,0.0712,-0.0766]
Shape263 = x3d.Shape()
Shape263.USE = "HAnimJointShape"

Transform262.children.append(Shape263)

HAnimSegment261.children.append(Transform262)
Transform264 = x3d.Transform()
Shape265 = x3d.Shape()
LineSet266 = x3d.LineSet()
LineSet266.vertexCount = [2]
Coordinate267 = x3d.Coordinate()

LineSet266.coord = Coordinate267
ColorRGBA268 = x3d.ColorRGBA()
ColorRGBA268.USE = "HAnimSegmentLineColorRGBA"

LineSet266.color = ColorRGBA268

Shape265.geometry = LineSet266

Transform264.children.append(Shape265)

HAnimSegment261.children.append(Transform264)
HAnimSite269 = x3d.HAnimSite()
HAnimSite269.DEF = "STD_Site_r_calcaneus_posterior_pt"
HAnimSite269.name = "r_calcaneus_posterior_pt"
HAnimSite269.translation = [-0.0692,0.0297,-0.1221]
TouchSensor270 = x3d.TouchSensor()
TouchSensor270.description = "HAnimSite r_calcaneus_posterior_pt"

HAnimSite269.children.append(TouchSensor270)
Shape271 = x3d.Shape()
Shape271.USE = "HAnimSiteShape"

HAnimSite269.children.append(Shape271)

HAnimSegment261.children.append(HAnimSite269)
HAnimSite272 = x3d.HAnimSite()
HAnimSite272.DEF = "STD_Site_r_sphyrion_pt"
HAnimSite272.name = "r_sphyrion_pt"
HAnimSite272.translation = [-0.0603,0.0610,-0.1002]
TouchSensor273 = x3d.TouchSensor()
TouchSensor273.description = "HAnimSite r_sphyrion_pt"

HAnimSite272.children.append(TouchSensor273)
Shape274 = x3d.Shape()
Shape274.USE = "HAnimSiteShape"

HAnimSite272.children.append(Shape274)

HAnimSegment261.children.append(HAnimSite272)

HAnimJoint260.children.append(HAnimSegment261)
HAnimJoint275 = x3d.HAnimJoint()
HAnimJoint275.DEF = "STD_Joint_r_talocalcaneonavicular"
HAnimJoint275.name = "r_talocalcaneonavicular"
HAnimSegment276 = x3d.HAnimSegment()
HAnimSegment276.DEF = "STD_Segment_r_navicular"
HAnimSegment276.name = "r_navicular"
Transform277 = x3d.Transform()
Shape278 = x3d.Shape()
LineSet279 = x3d.LineSet()
LineSet279.vertexCount = [2]
Coordinate280 = x3d.Coordinate()

LineSet279.coord = Coordinate280
ColorRGBA281 = x3d.ColorRGBA()
ColorRGBA281.USE = "HAnimSegmentLineColorRGBA"

LineSet279.color = ColorRGBA281

Shape278.geometry = LineSet279

Transform277.children.append(Shape278)

HAnimSegment276.children.append(Transform277)

HAnimJoint275.children.append(HAnimSegment276)
HAnimJoint282 = x3d.HAnimJoint()
HAnimJoint282.DEF = "STD_Joint_r_cuneonavicular_1"
HAnimJoint282.name = "r_cuneonavicular_1"
HAnimSegment283 = x3d.HAnimSegment()
HAnimSegment283.DEF = "STD_Segment_r_cuneiform_1"
HAnimSegment283.name = "r_cuneiform_1"

HAnimJoint282.children.append(HAnimSegment283)
HAnimJoint284 = x3d.HAnimJoint()
HAnimJoint284.DEF = "STD_Joint_r_tarsometatarsal_1"
HAnimJoint284.name = "r_tarsometatarsal_1"
HAnimSegment285 = x3d.HAnimSegment()
HAnimSegment285.DEF = "STD_Segment_r_metatarsal_1"
HAnimSegment285.name = "r_metatarsal_1"

HAnimJoint284.children.append(HAnimSegment285)
HAnimJoint286 = x3d.HAnimJoint()
HAnimJoint286.DEF = "STD_Joint_r_metatarsophalangeal_1"
HAnimJoint286.name = "r_metatarsophalangeal_1"
HAnimSegment287 = x3d.HAnimSegment()
HAnimSegment287.DEF = "STD_Segment_r_tarsal_proximal_phalanx_1"
HAnimSegment287.name = "r_tarsal_proximal_phalanx_1"
HAnimSite288 = x3d.HAnimSite()
HAnimSite288.DEF = "STD_Site_r_metatarsal_phalanx_1_pt"
HAnimSite288.name = "r_metatarsal_phalanx_1_pt"
TouchSensor289 = x3d.TouchSensor()
TouchSensor289.description = "HAnimSite r_metatarsal_phalanx_1_pt"

HAnimSite288.children.append(TouchSensor289)
Shape290 = x3d.Shape()
Shape290.USE = "HAnimSiteShape"

HAnimSite288.children.append(Shape290)

HAnimSegment287.children.append(HAnimSite288)

HAnimJoint286.children.append(HAnimSegment287)
HAnimJoint291 = x3d.HAnimJoint()
HAnimJoint291.DEF = "STD_Joint_r_tarsal_interphalangeal_1"
HAnimJoint291.name = "r_tarsal_interphalangeal_1"
HAnimSegment292 = x3d.HAnimSegment()
HAnimSegment292.DEF = "STD_Segment_r_tarsal_distal_phalanx_1"
HAnimSegment292.name = "r_tarsal_distal_phalanx_1"
HAnimSite293 = x3d.HAnimSite()
HAnimSite293.DEF = "STD_Site_r_tarsal_distal_phalanx_1_tip"
HAnimSite293.name = "r_tarsal_distal_phalanx_1_tip"
TouchSensor294 = x3d.TouchSensor()
TouchSensor294.description = "HAnimSite r_tarsal_distal_phalanx_1_tip"

HAnimSite293.children.append(TouchSensor294)
Shape295 = x3d.Shape()
Shape295.USE = "HAnimSiteShape"

HAnimSite293.children.append(Shape295)

HAnimSegment292.children.append(HAnimSite293)

HAnimJoint291.children.append(HAnimSegment292)

HAnimJoint286.children.append(HAnimJoint291)

HAnimJoint284.children.append(HAnimJoint286)

HAnimJoint282.children.append(HAnimJoint284)

HAnimJoint275.children.append(HAnimJoint282)
HAnimJoint296 = x3d.HAnimJoint()
HAnimJoint296.DEF = "STD_Joint_r_cuneonavicular_2"
HAnimJoint296.name = "r_cuneonavicular_2"
HAnimSegment297 = x3d.HAnimSegment()
HAnimSegment297.DEF = "STD_Segment_r_cuneiform_2"
HAnimSegment297.name = "r_cuneiform_2"

HAnimJoint296.children.append(HAnimSegment297)
HAnimJoint298 = x3d.HAnimJoint()
HAnimJoint298.DEF = "STD_Joint_r_tarsometatarsal_2"
HAnimJoint298.name = "r_tarsometatarsal_2"
HAnimSegment299 = x3d.HAnimSegment()
HAnimSegment299.DEF = "STD_Segment_r_metatarsal_2"
HAnimSegment299.name = "r_metatarsal_2"

HAnimJoint298.children.append(HAnimSegment299)
HAnimJoint300 = x3d.HAnimJoint()
HAnimJoint300.DEF = "STD_Joint_r_metatarsophalangeal_2"
HAnimJoint300.name = "r_metatarsophalangeal_2"
HAnimSegment301 = x3d.HAnimSegment()
HAnimSegment301.DEF = "STD_Segment_r_tarsal_proximal_phalanx_2"
HAnimSegment301.name = "r_tarsal_proximal_phalanx_2"

HAnimJoint300.children.append(HAnimSegment301)
HAnimJoint302 = x3d.HAnimJoint()
HAnimJoint302.DEF = "STD_Joint_r_tarsal_proximal_interphalangeal_2"
HAnimJoint302.name = "r_tarsal_proximal_interphalangeal_2"
HAnimSegment303 = x3d.HAnimSegment()
HAnimSegment303.DEF = "STD_Segment_r_tarsal_middle_phalanx_2"
HAnimSegment303.name = "r_tarsal_middle_phalanx_2"

HAnimJoint302.children.append(HAnimSegment303)
HAnimJoint304 = x3d.HAnimJoint()
HAnimJoint304.DEF = "STD_Joint_r_tarsal_distal_interphalangeal_2"
HAnimJoint304.name = "r_tarsal_distal_interphalangeal_2"
HAnimSegment305 = x3d.HAnimSegment()
HAnimSegment305.DEF = "STD_Segment_r_tarsal_distal_phalanx_2"
HAnimSegment305.name = "r_tarsal_distal_phalanx_2"
HAnimSite306 = x3d.HAnimSite()
HAnimSite306.DEF = "STD_Site_r_tarsal_distal_phalanx_2_tip"
HAnimSite306.name = "r_tarsal_distal_phalanx_2_tip"
HAnimSite306.translation = [-0.0883,0.0134,0.1383]
TouchSensor307 = x3d.TouchSensor()
TouchSensor307.description = "HAnimSite r_tarsal_distal_phalanx_2_tip"

HAnimSite306.children.append(TouchSensor307)
Shape308 = x3d.Shape()
Shape308.USE = "HAnimSiteShape"

HAnimSite306.children.append(Shape308)

HAnimSegment305.children.append(HAnimSite306)

HAnimJoint304.children.append(HAnimSegment305)

HAnimJoint302.children.append(HAnimJoint304)

HAnimJoint300.children.append(HAnimJoint302)

HAnimJoint298.children.append(HAnimJoint300)

HAnimJoint296.children.append(HAnimJoint298)

HAnimJoint275.children.append(HAnimJoint296)
HAnimJoint309 = x3d.HAnimJoint()
HAnimJoint309.DEF = "STD_Joint_r_cuneonavicular_3"
HAnimJoint309.name = "r_cuneonavicular_3"
HAnimSegment310 = x3d.HAnimSegment()
HAnimSegment310.DEF = "STD_Segment_r_cuneiform_3"
HAnimSegment310.name = "r_cuneiform_3"

HAnimJoint309.children.append(HAnimSegment310)
HAnimJoint311 = x3d.HAnimJoint()
HAnimJoint311.DEF = "STD_Joint_r_tarsometatarsal_3 "
HAnimJoint311.name = "r_tarsometatarsal_3 "
HAnimSegment312 = x3d.HAnimSegment()
HAnimSegment312.DEF = "STD_Segment_r_metatarsal_3"
HAnimSegment312.name = "r_metatarsal_3"

HAnimJoint311.children.append(HAnimSegment312)
HAnimJoint313 = x3d.HAnimJoint()
HAnimJoint313.DEF = "STD_Joint_r_metatarsophalangeal_3"
HAnimJoint313.name = "r_metatarsophalangeal_3"
HAnimSegment314 = x3d.HAnimSegment()
HAnimSegment314.DEF = "STD_Segment_r_tarsal_proximal_phalanx_3"
HAnimSegment314.name = "r_tarsal_proximal_phalanx_3"

HAnimJoint313.children.append(HAnimSegment314)
HAnimJoint315 = x3d.HAnimJoint()
HAnimJoint315.DEF = "STD_Joint_r_tarsal_proximal_interphalangeal_3"
HAnimJoint315.name = "r_tarsal_proximal_interphalangeal_3"
HAnimSegment316 = x3d.HAnimSegment()
HAnimSegment316.DEF = "STD_Segment_r_tarsal_middle_phalanx_3"
HAnimSegment316.name = "r_tarsal_middle_phalanx_3"

HAnimJoint315.children.append(HAnimSegment316)
HAnimJoint317 = x3d.HAnimJoint()
HAnimJoint317.DEF = "STD_Joint_r_tarsal_distal_interphalangeal_3"
HAnimJoint317.name = "r_tarsal_distal_interphalangeal_3"
HAnimSegment318 = x3d.HAnimSegment()
HAnimSegment318.DEF = "STD_Segment_r_tarsal_distal_phalanx_3"
HAnimSegment318.name = "r_tarsal_distal_phalanx_3"
HAnimSite319 = x3d.HAnimSite()
HAnimSite319.DEF = "STD_Site_r_tarsal_distal_phalanx_3_tip"
HAnimSite319.name = "r_tarsal_distal_phalanx_3_tip"
TouchSensor320 = x3d.TouchSensor()
TouchSensor320.description = "HAnimSite r_tarsal_distal_phalanx_3_tip"

HAnimSite319.children.append(TouchSensor320)
Shape321 = x3d.Shape()
Shape321.USE = "HAnimSiteShape"

HAnimSite319.children.append(Shape321)

HAnimSegment318.children.append(HAnimSite319)

HAnimJoint317.children.append(HAnimSegment318)

HAnimJoint315.children.append(HAnimJoint317)

HAnimJoint313.children.append(HAnimJoint315)

HAnimJoint311.children.append(HAnimJoint313)

HAnimJoint309.children.append(HAnimJoint311)

HAnimJoint275.children.append(HAnimJoint309)

HAnimJoint260.children.append(HAnimJoint275)
HAnimJoint322 = x3d.HAnimJoint()
HAnimJoint322.DEF = "STD_Joint_r_calcaneocuboid"
HAnimJoint322.name = "r_calcaneocuboid"
HAnimSegment323 = x3d.HAnimSegment()
HAnimSegment323.DEF = "STD_Segment_r_calcaneus"
HAnimSegment323.name = "r_calcaneus"

HAnimJoint322.children.append(HAnimSegment323)
HAnimJoint324 = x3d.HAnimJoint()
HAnimJoint324.DEF = "STD_Joint_r_transversetarsal"
HAnimJoint324.name = "r_transversetarsal"
HAnimSegment325 = x3d.HAnimSegment()
HAnimSegment325.DEF = "STD_Segment_r_cuboid"
HAnimSegment325.name = "r_cuboid"

HAnimJoint324.children.append(HAnimSegment325)
HAnimJoint326 = x3d.HAnimJoint()
HAnimJoint326.DEF = "STD_Joint_r_tarsometatarsal_4"
HAnimJoint326.name = "r_tarsometatarsal_4"
HAnimSegment327 = x3d.HAnimSegment()
HAnimSegment327.DEF = "STD_Segment_r_metatarsal_4"
HAnimSegment327.name = "r_metatarsal_4"

HAnimJoint326.children.append(HAnimSegment327)
HAnimJoint328 = x3d.HAnimJoint()
HAnimJoint328.DEF = "STD_Joint_r_metatarsophalangeal_4"
HAnimJoint328.name = "r_metatarsophalangeal_4"
HAnimSegment329 = x3d.HAnimSegment()
HAnimSegment329.DEF = "STD_Segment_r_tarsal_proximal_phalanx_4"
HAnimSegment329.name = "r_tarsal_proximal_phalanx_4"

HAnimJoint328.children.append(HAnimSegment329)
HAnimJoint330 = x3d.HAnimJoint()
HAnimJoint330.DEF = "STD_Joint_r_tarsal_proximal_interphalangeal_4"
HAnimJoint330.name = "r_tarsal_proximal_interphalangeal_4"
HAnimSegment331 = x3d.HAnimSegment()
HAnimSegment331.DEF = "STD_Segment_r_tarsal_middle_phalanx_4"
HAnimSegment331.name = "r_tarsal_middle_phalanx_4"

HAnimJoint330.children.append(HAnimSegment331)
HAnimJoint332 = x3d.HAnimJoint()
HAnimJoint332.DEF = "STD_Joint_r_tarsal_distal_interphalangeal_4"
HAnimJoint332.name = "r_tarsal_distal_interphalangeal_4"
HAnimSegment333 = x3d.HAnimSegment()
HAnimSegment333.DEF = "STD_Segment_r_tarsal_distal_phalanx_4"
HAnimSegment333.name = "r_tarsal_distal_phalanx_4"
HAnimSite334 = x3d.HAnimSite()
HAnimSite334.DEF = "STD_Site_r_tarsal_distal_phalanx_4_tip"
HAnimSite334.name = "r_tarsal_distal_phalanx_4_tip"
TouchSensor335 = x3d.TouchSensor()
TouchSensor335.description = "HAnimSite r_tarsal_distal_phalanx_4_tip"

HAnimSite334.children.append(TouchSensor335)
Shape336 = x3d.Shape()
Shape336.USE = "HAnimSiteShape"

HAnimSite334.children.append(Shape336)

HAnimSegment333.children.append(HAnimSite334)

HAnimJoint332.children.append(HAnimSegment333)

HAnimJoint330.children.append(HAnimJoint332)

HAnimJoint328.children.append(HAnimJoint330)

HAnimJoint326.children.append(HAnimJoint328)

HAnimJoint324.children.append(HAnimJoint326)
HAnimJoint337 = x3d.HAnimJoint()
HAnimJoint337.DEF = "STD_Joint_r_tarsometatarsal_5"
HAnimJoint337.name = "r_tarsometatarsal_5"
HAnimSegment338 = x3d.HAnimSegment()
HAnimSegment338.DEF = "STD_Segment_r_metatarsal_5"
HAnimSegment338.name = "r_metatarsal_5"

HAnimJoint337.children.append(HAnimSegment338)
HAnimJoint339 = x3d.HAnimJoint()
HAnimJoint339.DEF = "STD_Joint_r_metatarsophalangeal_5"
HAnimJoint339.name = "r_metatarsophalangeal_5"
HAnimSegment340 = x3d.HAnimSegment()
HAnimSegment340.DEF = "STD_Segment_r_tarsal_proximal_phalanx_5"
HAnimSegment340.name = "r_tarsal_proximal_phalanx_5"
HAnimSite341 = x3d.HAnimSite()
HAnimSite341.DEF = "STD_Site_r_metatarsal_phalanx_5_pt"
HAnimSite341.name = "r_metatarsal_phalanx_5_pt"
TouchSensor342 = x3d.TouchSensor()
TouchSensor342.description = "HAnimSite r_metatarsal_phalanx_5_pt"

HAnimSite341.children.append(TouchSensor342)
Shape343 = x3d.Shape()
Shape343.USE = "HAnimSiteShape"

HAnimSite341.children.append(Shape343)

HAnimSegment340.children.append(HAnimSite341)

HAnimJoint339.children.append(HAnimSegment340)
HAnimJoint344 = x3d.HAnimJoint()
HAnimJoint344.DEF = "STD_Joint_r_tarsal_proximal_interphalangeal_5"
HAnimJoint344.name = "r_tarsal_proximal_interphalangeal_5"
HAnimSegment345 = x3d.HAnimSegment()
HAnimSegment345.DEF = "STD_Segment_r_tarsal_middle_phalanx_5"
HAnimSegment345.name = "r_tarsal_middle_phalanx_5"

HAnimJoint344.children.append(HAnimSegment345)
HAnimJoint346 = x3d.HAnimJoint()
HAnimJoint346.DEF = "STD_Joint_r_tarsal_distal_interphalangeal_5"
HAnimJoint346.name = "r_tarsal_distal_interphalangeal_5"
HAnimSegment347 = x3d.HAnimSegment()
HAnimSegment347.DEF = "STD_Segment_r_tarsal_distal_phalanx_5"
HAnimSegment347.name = "r_tarsal_distal_phalanx_5"
HAnimSite348 = x3d.HAnimSite()
HAnimSite348.DEF = "STD_Site_r_tarsal_distal_phalanx_5_tip"
HAnimSite348.name = "r_tarsal_distal_phalanx_5_tip"
TouchSensor349 = x3d.TouchSensor()
TouchSensor349.description = "HAnimSite r_tarsal_distal_phalanx_5_tip"

HAnimSite348.children.append(TouchSensor349)
Shape350 = x3d.Shape()
Shape350.USE = "HAnimSiteShape"

HAnimSite348.children.append(Shape350)

HAnimSegment347.children.append(HAnimSite348)

HAnimJoint346.children.append(HAnimSegment347)

HAnimJoint344.children.append(HAnimJoint346)

HAnimJoint339.children.append(HAnimJoint344)

HAnimJoint337.children.append(HAnimJoint339)

HAnimJoint324.children.append(HAnimJoint337)

HAnimJoint322.children.append(HAnimJoint324)

HAnimJoint260.children.append(HAnimJoint322)

HAnimJoint242.children.append(HAnimJoint260)

HAnimJoint221.children.append(HAnimJoint242)

HAnimJoint52.children.append(HAnimJoint221)

HAnimJoint43.children.append(HAnimJoint52)
HAnimJoint351 = x3d.HAnimJoint()
HAnimJoint351.DEF = "STD_Joint_vl5"
HAnimJoint351.name = "vl5"
HAnimJoint351.center = [0.0028,1.0568,-0.0776]
HAnimSegment352 = x3d.HAnimSegment()
HAnimSegment352.DEF = "STD_Segment_l5"
HAnimSegment352.name = "l5"
Transform353 = x3d.Transform()
Transform353.translation = [0.0028,1.0568,-0.0776]
Shape354 = x3d.Shape()
Shape354.USE = "HAnimJointShape"

Transform353.children.append(Shape354)

HAnimSegment352.children.append(Transform353)
Transform355 = x3d.Transform()
Shape356 = x3d.Shape()
LineSet357 = x3d.LineSet()
LineSet357.vertexCount = [2]
Coordinate358 = x3d.Coordinate()

LineSet357.coord = Coordinate358
ColorRGBA359 = x3d.ColorRGBA()
ColorRGBA359.USE = "HAnimSegmentLineColorRGBA"

LineSet357.color = ColorRGBA359

Shape356.geometry = LineSet357

Transform355.children.append(Shape356)

HAnimSegment352.children.append(Transform355)
HAnimSite360 = x3d.HAnimSite()
HAnimSite360.DEF = "STD_Site_navel_pt"
HAnimSite360.name = "navel_pt"
HAnimSite360.translation = [0.0069,1.0966,0.1017]
TouchSensor361 = x3d.TouchSensor()
TouchSensor361.description = "HAnimSite navel_pt"

HAnimSite360.children.append(TouchSensor361)
Shape362 = x3d.Shape()
Shape362.USE = "HAnimSiteShape"

HAnimSite360.children.append(Shape362)

HAnimSegment352.children.append(HAnimSite360)
HAnimSite363 = x3d.HAnimSite()
HAnimSite363.DEF = "STD_Site_waist_preferred_anterior_pt"
HAnimSite363.name = "waist_preferred_anterior_pt"
TouchSensor364 = x3d.TouchSensor()
TouchSensor364.description = "HAnimSite waist_preferred_anterior_pt"

HAnimSite363.children.append(TouchSensor364)
Shape365 = x3d.Shape()
Shape365.USE = "HAnimSiteShape"

HAnimSite363.children.append(Shape365)

HAnimSegment352.children.append(HAnimSite363)
HAnimSite366 = x3d.HAnimSite()
HAnimSite366.DEF = "STD_Site_waist_preferred_posterior_pt"
HAnimSite366.name = "waist_preferred_posterior_pt"
HAnimSite366.translation = [0.2900,1.0915,-0.1091]
TouchSensor367 = x3d.TouchSensor()
TouchSensor367.description = "HAnimSite waist_preferred_posterior_pt"

HAnimSite366.children.append(TouchSensor367)
Shape368 = x3d.Shape()
Shape368.USE = "HAnimSiteShape"

HAnimSite366.children.append(Shape368)

HAnimSegment352.children.append(HAnimSite366)

HAnimJoint351.children.append(HAnimSegment352)
HAnimJoint369 = x3d.HAnimJoint()
HAnimJoint369.DEF = "STD_Joint_vl4"
HAnimJoint369.name = "vl4"
HAnimJoint369.center = [0.0035,1.0925,-0.0787]
HAnimSegment370 = x3d.HAnimSegment()
HAnimSegment370.DEF = "STD_Segment_l4"
HAnimSegment370.name = "l4"
Transform371 = x3d.Transform()
Transform371.translation = [0.0035,1.0925,-0.0787]
Shape372 = x3d.Shape()
Shape372.USE = "HAnimJointShape"

Transform371.children.append(Shape372)

HAnimSegment370.children.append(Transform371)
Transform373 = x3d.Transform()
Shape374 = x3d.Shape()
LineSet375 = x3d.LineSet()
LineSet375.vertexCount = [2]
Coordinate376 = x3d.Coordinate()

LineSet375.coord = Coordinate376
ColorRGBA377 = x3d.ColorRGBA()
ColorRGBA377.USE = "HAnimSegmentLineColorRGBA"

LineSet375.color = ColorRGBA377

Shape374.geometry = LineSet375

Transform373.children.append(Shape374)

HAnimSegment370.children.append(Transform373)

HAnimJoint369.children.append(HAnimSegment370)
HAnimJoint378 = x3d.HAnimJoint()
HAnimJoint378.DEF = "STD_Joint_vl3"
HAnimJoint378.name = "vl3"
HAnimJoint378.center = [0.0041,1.1276,-0.0796]
HAnimSegment379 = x3d.HAnimSegment()
HAnimSegment379.DEF = "STD_Segment_l3"
HAnimSegment379.name = "l3"
Transform380 = x3d.Transform()
Transform380.translation = [0.0041,1.1276,-0.0796]
Shape381 = x3d.Shape()
Shape381.USE = "HAnimJointShape"

Transform380.children.append(Shape381)

HAnimSegment379.children.append(Transform380)
Transform382 = x3d.Transform()
Shape383 = x3d.Shape()
LineSet384 = x3d.LineSet()
LineSet384.vertexCount = [2]
Coordinate385 = x3d.Coordinate()

LineSet384.coord = Coordinate385
ColorRGBA386 = x3d.ColorRGBA()
ColorRGBA386.USE = "HAnimSegmentLineColorRGBA"

LineSet384.color = ColorRGBA386

Shape383.geometry = LineSet384

Transform382.children.append(Shape383)

HAnimSegment379.children.append(Transform382)

HAnimJoint378.children.append(HAnimSegment379)
HAnimJoint387 = x3d.HAnimJoint()
HAnimJoint387.DEF = "STD_Joint_vl2"
HAnimJoint387.name = "vl2"
HAnimJoint387.center = [0.0045,1.1546,-0.0800]
HAnimSegment388 = x3d.HAnimSegment()
HAnimSegment388.DEF = "STD_Segment_l2"
HAnimSegment388.name = "l2"
Transform389 = x3d.Transform()
Transform389.translation = [0.0045,1.1546,-0.0800]
Shape390 = x3d.Shape()
Shape390.USE = "HAnimJointShape"

Transform389.children.append(Shape390)

HAnimSegment388.children.append(Transform389)
Transform391 = x3d.Transform()
Shape392 = x3d.Shape()
LineSet393 = x3d.LineSet()
LineSet393.vertexCount = [2]
Coordinate394 = x3d.Coordinate()

LineSet393.coord = Coordinate394
ColorRGBA395 = x3d.ColorRGBA()
ColorRGBA395.USE = "HAnimSegmentLineColorRGBA"

LineSet393.color = ColorRGBA395

Shape392.geometry = LineSet393

Transform391.children.append(Shape392)

HAnimSegment388.children.append(Transform391)
HAnimSite396 = x3d.HAnimSite()
HAnimSite396.DEF = "STD_Site_l_rib10_pt"
HAnimSite396.name = "l_rib10_pt"
HAnimSite396.translation = [0.0871,1.1925,0.0992]
TouchSensor397 = x3d.TouchSensor()
TouchSensor397.description = "HAnimSite l_rib10_pt"

HAnimSite396.children.append(TouchSensor397)
Shape398 = x3d.Shape()
Shape398.USE = "HAnimSiteShape"

HAnimSite396.children.append(Shape398)

HAnimSegment388.children.append(HAnimSite396)
HAnimSite399 = x3d.HAnimSite()
HAnimSite399.DEF = "STD_Site_r_rib10_pt"
HAnimSite399.name = "r_rib10_pt"
HAnimSite399.translation = [-0.0711,1.1941,0.1016]
TouchSensor400 = x3d.TouchSensor()
TouchSensor400.description = "HAnimSite r_rib10_pt"

HAnimSite399.children.append(TouchSensor400)
Shape401 = x3d.Shape()
Shape401.USE = "HAnimSiteShape"

HAnimSite399.children.append(Shape401)

HAnimSegment388.children.append(HAnimSite399)
HAnimSite402 = x3d.HAnimSite()
HAnimSite402.DEF = "STD_Site_spine_2_middle_back_pt"
HAnimSite402.name = "spine_2_middle_back_pt"
TouchSensor403 = x3d.TouchSensor()
TouchSensor403.description = "HAnimSite spine_2_middle_back_pt"

HAnimSite402.children.append(TouchSensor403)
Shape404 = x3d.Shape()
Shape404.USE = "HAnimSiteShape"

HAnimSite402.children.append(Shape404)

HAnimSegment388.children.append(HAnimSite402)

HAnimJoint387.children.append(HAnimSegment388)
HAnimJoint405 = x3d.HAnimJoint()
HAnimJoint405.DEF = "STD_Joint_vl1"
HAnimJoint405.name = "vl1"
HAnimJoint405.center = [0.0048,1.1912,-0.0805]
HAnimSegment406 = x3d.HAnimSegment()
HAnimSegment406.DEF = "STD_Segment_l1"
HAnimSegment406.name = "l1"
Transform407 = x3d.Transform()
Transform407.translation = [0.0048,1.1912,-0.0805]
Shape408 = x3d.Shape()
Shape408.USE = "HAnimJointShape"

Transform407.children.append(Shape408)

HAnimSegment406.children.append(Transform407)
Transform409 = x3d.Transform()
Shape410 = x3d.Shape()
LineSet411 = x3d.LineSet()
LineSet411.vertexCount = [2]
Coordinate412 = x3d.Coordinate()

LineSet411.coord = Coordinate412
ColorRGBA413 = x3d.ColorRGBA()
ColorRGBA413.USE = "HAnimSegmentLineColorRGBA"

LineSet411.color = ColorRGBA413

Shape410.geometry = LineSet411

Transform409.children.append(Shape410)

HAnimSegment406.children.append(Transform409)

HAnimJoint405.children.append(HAnimSegment406)
HAnimJoint414 = x3d.HAnimJoint()
HAnimJoint414.DEF = "STD_Joint_vt12"
HAnimJoint414.name = "vt12"
HAnimJoint414.center = [0.0051,1.2278,-0.0808]
HAnimSegment415 = x3d.HAnimSegment()
HAnimSegment415.DEF = "STD_Segment_t12"
HAnimSegment415.name = "t12"
Transform416 = x3d.Transform()
Transform416.translation = [0.0051,1.2278,-0.0808]
Shape417 = x3d.Shape()
Shape417.USE = "HAnimJointShape"

Transform416.children.append(Shape417)

HAnimSegment415.children.append(Transform416)
Transform418 = x3d.Transform()
Shape419 = x3d.Shape()
LineSet420 = x3d.LineSet()
LineSet420.vertexCount = [2]
Coordinate421 = x3d.Coordinate()

LineSet420.coord = Coordinate421
ColorRGBA422 = x3d.ColorRGBA()
ColorRGBA422.USE = "HAnimSegmentLineColorRGBA"

LineSet420.color = ColorRGBA422

Shape419.geometry = LineSet420

Transform418.children.append(Shape419)

HAnimSegment415.children.append(Transform418)

HAnimJoint414.children.append(HAnimSegment415)
HAnimJoint423 = x3d.HAnimJoint()
HAnimJoint423.DEF = "STD_Joint_vt11"
HAnimJoint423.name = "vt11"
HAnimJoint423.center = [0.0053,1.2679,-0.0810]
HAnimSegment424 = x3d.HAnimSegment()
HAnimSegment424.DEF = "STD_Segment_t11"
HAnimSegment424.name = "t11"
Transform425 = x3d.Transform()
Transform425.translation = [0.0053,1.2679,-0.0810]
Shape426 = x3d.Shape()
Shape426.USE = "HAnimJointShape"

Transform425.children.append(Shape426)

HAnimSegment424.children.append(Transform425)
Transform427 = x3d.Transform()
Shape428 = x3d.Shape()
LineSet429 = x3d.LineSet()
LineSet429.vertexCount = [2]
Coordinate430 = x3d.Coordinate()

LineSet429.coord = Coordinate430
ColorRGBA431 = x3d.ColorRGBA()
ColorRGBA431.USE = "HAnimSegmentLineColorRGBA"

LineSet429.color = ColorRGBA431

Shape428.geometry = LineSet429

Transform427.children.append(Shape428)

HAnimSegment424.children.append(Transform427)

HAnimJoint423.children.append(HAnimSegment424)
HAnimJoint432 = x3d.HAnimJoint()
HAnimJoint432.DEF = "STD_Joint_vt10"
HAnimJoint432.name = "vt10"
HAnimJoint432.center = [0.0056,1.2848,-0.0822]
HAnimSegment433 = x3d.HAnimSegment()
HAnimSegment433.DEF = "STD_Segment_t10"
HAnimSegment433.name = "t10"
Transform434 = x3d.Transform()
Transform434.translation = [0.0056,1.2848,-0.0822]
Shape435 = x3d.Shape()
Shape435.USE = "HAnimJointShape"

Transform434.children.append(Shape435)

HAnimSegment433.children.append(Transform434)
Transform436 = x3d.Transform()
Shape437 = x3d.Shape()
LineSet438 = x3d.LineSet()
LineSet438.vertexCount = [2]
Coordinate439 = x3d.Coordinate()

LineSet438.coord = Coordinate439
ColorRGBA440 = x3d.ColorRGBA()
ColorRGBA440.USE = "HAnimSegmentLineColorRGBA"

LineSet438.color = ColorRGBA440

Shape437.geometry = LineSet438

Transform436.children.append(Shape437)

HAnimSegment433.children.append(Transform436)
HAnimSite441 = x3d.HAnimSite()
HAnimSite441.DEF = "STD_Site_substernale_pt"
HAnimSite441.name = "substernale_pt"
HAnimSite441.translation = [0.0085,1.2995,0.1147]
TouchSensor442 = x3d.TouchSensor()
TouchSensor442.description = "HAnimSite substernale_pt"

HAnimSite441.children.append(TouchSensor442)
Shape443 = x3d.Shape()
Shape443.USE = "HAnimSiteShape"

HAnimSite441.children.append(Shape443)

HAnimSegment433.children.append(HAnimSite441)

HAnimJoint432.children.append(HAnimSegment433)
HAnimJoint444 = x3d.HAnimJoint()
HAnimJoint444.DEF = "STD_Joint_vt9"
HAnimJoint444.name = "vt9"
HAnimJoint444.center = [0.0057,1.3126,-0.0838]
HAnimSegment445 = x3d.HAnimSegment()
HAnimSegment445.DEF = "STD_Segment_t9"
HAnimSegment445.name = "t9"
Transform446 = x3d.Transform()
Transform446.translation = [0.0057,1.3126,-0.0838]
Shape447 = x3d.Shape()
Shape447.USE = "HAnimJointShape"

Transform446.children.append(Shape447)

HAnimSegment445.children.append(Transform446)
Transform448 = x3d.Transform()
Shape449 = x3d.Shape()
LineSet450 = x3d.LineSet()
LineSet450.vertexCount = [2]
Coordinate451 = x3d.Coordinate()

LineSet450.coord = Coordinate451
ColorRGBA452 = x3d.ColorRGBA()
ColorRGBA452.USE = "HAnimSegmentLineColorRGBA"

LineSet450.color = ColorRGBA452

Shape449.geometry = LineSet450

Transform448.children.append(Shape449)

HAnimSegment445.children.append(Transform448)
HAnimSite453 = x3d.HAnimSite()
HAnimSite453.DEF = "STD_Site_l_thelion_pt"
HAnimSite453.name = "l_thelion_pt"
HAnimSite453.translation = [0.0918,1.3382,0.1192]
TouchSensor454 = x3d.TouchSensor()
TouchSensor454.description = "HAnimSite l_thelion_pt"

HAnimSite453.children.append(TouchSensor454)
Shape455 = x3d.Shape()
Shape455.USE = "HAnimSiteShape"

HAnimSite453.children.append(Shape455)

HAnimSegment445.children.append(HAnimSite453)
HAnimSite456 = x3d.HAnimSite()
HAnimSite456.DEF = "STD_Site_r_thelion_pt"
HAnimSite456.name = "r_thelion_pt"
HAnimSite456.translation = [-0.0736,1.3385,0.1217]
TouchSensor457 = x3d.TouchSensor()
TouchSensor457.description = "HAnimSite r_thelion_pt"

HAnimSite456.children.append(TouchSensor457)
Shape458 = x3d.Shape()
Shape458.USE = "HAnimSiteShape"

HAnimSite456.children.append(Shape458)

HAnimSegment445.children.append(HAnimSite456)

HAnimJoint444.children.append(HAnimSegment445)
HAnimJoint459 = x3d.HAnimJoint()
HAnimJoint459.DEF = "STD_Joint_vt8"
HAnimJoint459.name = "vt8"
HAnimJoint459.center = [0.0057,1.3382,-0.0845]
HAnimSegment460 = x3d.HAnimSegment()
HAnimSegment460.DEF = "STD_Segment_t8"
HAnimSegment460.name = "t8"
Transform461 = x3d.Transform()
Transform461.translation = [0.0057,1.3382,-0.0845]
Shape462 = x3d.Shape()
Shape462.USE = "HAnimJointShape"

Transform461.children.append(Shape462)

HAnimSegment460.children.append(Transform461)
Transform463 = x3d.Transform()
Shape464 = x3d.Shape()
LineSet465 = x3d.LineSet()
LineSet465.vertexCount = [2]
Coordinate466 = x3d.Coordinate()

LineSet465.coord = Coordinate466
ColorRGBA467 = x3d.ColorRGBA()
ColorRGBA467.USE = "HAnimSegmentLineColorRGBA"

LineSet465.color = ColorRGBA467

Shape464.geometry = LineSet465

Transform463.children.append(Shape464)

HAnimSegment460.children.append(Transform463)

HAnimJoint459.children.append(HAnimSegment460)
HAnimJoint468 = x3d.HAnimJoint()
HAnimJoint468.DEF = "STD_Joint_vt7"
HAnimJoint468.name = "vt7"
HAnimJoint468.center = [0.0058,1.3625,-0.0833]
HAnimSegment469 = x3d.HAnimSegment()
HAnimSegment469.DEF = "STD_Segment_t7"
HAnimSegment469.name = "t7"
Transform470 = x3d.Transform()
Transform470.translation = [0.0058,1.3625,-0.0833]
Shape471 = x3d.Shape()
Shape471.USE = "HAnimJointShape"

Transform470.children.append(Shape471)

HAnimSegment469.children.append(Transform470)
Transform472 = x3d.Transform()
Shape473 = x3d.Shape()
LineSet474 = x3d.LineSet()
LineSet474.vertexCount = [2]
Coordinate475 = x3d.Coordinate()

LineSet474.coord = Coordinate475
ColorRGBA476 = x3d.ColorRGBA()
ColorRGBA476.USE = "HAnimSegmentLineColorRGBA"

LineSet474.color = ColorRGBA476

Shape473.geometry = LineSet474

Transform472.children.append(Shape473)

HAnimSegment469.children.append(Transform472)

HAnimJoint468.children.append(HAnimSegment469)
HAnimJoint477 = x3d.HAnimJoint()
HAnimJoint477.DEF = "STD_Joint_vt6"
HAnimJoint477.name = "vt6"
HAnimJoint477.center = [0.0059,1.3866,-0.0800]
HAnimSegment478 = x3d.HAnimSegment()
HAnimSegment478.DEF = "STD_Segment_t6"
HAnimSegment478.name = "t6"
Transform479 = x3d.Transform()
Transform479.translation = [0.0059,1.3866,-0.0800]
Shape480 = x3d.Shape()
Shape480.USE = "HAnimJointShape"

Transform479.children.append(Shape480)

HAnimSegment478.children.append(Transform479)
Transform481 = x3d.Transform()
Shape482 = x3d.Shape()
LineSet483 = x3d.LineSet()
LineSet483.vertexCount = [2]
Coordinate484 = x3d.Coordinate()

LineSet483.coord = Coordinate484
ColorRGBA485 = x3d.ColorRGBA()
ColorRGBA485.USE = "HAnimSegmentLineColorRGBA"

LineSet483.color = ColorRGBA485

Shape482.geometry = LineSet483

Transform481.children.append(Shape482)

HAnimSegment478.children.append(Transform481)
HAnimSite486 = x3d.HAnimSite()
HAnimSite486.DEF = "STD_Site_l_chest_midsagittal_plane_pt"
HAnimSite486.name = "l_chest_midsagittal_plane_pt"
TouchSensor487 = x3d.TouchSensor()
TouchSensor487.description = "HAnimSite l_chest_midsagittal_plane_pt"

HAnimSite486.children.append(TouchSensor487)
Shape488 = x3d.Shape()
Shape488.USE = "HAnimSiteShape"

HAnimSite486.children.append(Shape488)

HAnimSegment478.children.append(HAnimSite486)
HAnimSite489 = x3d.HAnimSite()
HAnimSite489.DEF = "STD_Site_mesosternale_pt"
HAnimSite489.name = "mesosternale_pt"
TouchSensor490 = x3d.TouchSensor()
TouchSensor490.description = "HAnimSite mesosternale_pt"

HAnimSite489.children.append(TouchSensor490)
Shape491 = x3d.Shape()
Shape491.USE = "HAnimSiteShape"

HAnimSite489.children.append(Shape491)

HAnimSegment478.children.append(HAnimSite489)
HAnimSite492 = x3d.HAnimSite()
HAnimSite492.DEF = "STD_Site_r_chest_midsagittal_plane_pt"
HAnimSite492.name = "r_chest_midsagittal_plane_pt"
TouchSensor493 = x3d.TouchSensor()
TouchSensor493.description = "HAnimSite r_chest_midsagittal_plane_pt"

HAnimSite492.children.append(TouchSensor493)
Shape494 = x3d.Shape()
Shape494.USE = "HAnimSiteShape"

HAnimSite492.children.append(Shape494)

HAnimSegment478.children.append(HAnimSite492)
HAnimSite495 = x3d.HAnimSite()
HAnimSite495.DEF = "STD_Site_rear_center_midsagittal_plane_pt"
HAnimSite495.name = "rear_center_midsagittal_plane_pt"
TouchSensor496 = x3d.TouchSensor()
TouchSensor496.description = "HAnimSite rear_center_midsagittal_plane_pt"

HAnimSite495.children.append(TouchSensor496)
Shape497 = x3d.Shape()
Shape497.USE = "HAnimSiteShape"

HAnimSite495.children.append(Shape497)

HAnimSegment478.children.append(HAnimSite495)

HAnimJoint477.children.append(HAnimSegment478)
HAnimJoint498 = x3d.HAnimJoint()
HAnimJoint498.DEF = "STD_Joint_vt5"
HAnimJoint498.name = "vt5"
HAnimJoint498.center = [0.0060,1.4102,-0.0745]
HAnimSegment499 = x3d.HAnimSegment()
HAnimSegment499.DEF = "STD_Segment_t5"
HAnimSegment499.name = "t5"
Transform500 = x3d.Transform()
Transform500.translation = [0.0060,1.4102,-0.0745]
Shape501 = x3d.Shape()
Shape501.USE = "HAnimJointShape"

Transform500.children.append(Shape501)

HAnimSegment499.children.append(Transform500)
Transform502 = x3d.Transform()
Shape503 = x3d.Shape()
LineSet504 = x3d.LineSet()
LineSet504.vertexCount = [2]
Coordinate505 = x3d.Coordinate()

LineSet504.coord = Coordinate505
ColorRGBA506 = x3d.ColorRGBA()
ColorRGBA506.USE = "HAnimSegmentLineColorRGBA"

LineSet504.color = ColorRGBA506

Shape503.geometry = LineSet504

Transform502.children.append(Shape503)

HAnimSegment499.children.append(Transform502)
HAnimSite507 = x3d.HAnimSite()
HAnimSite507.DEF = "STD_Site_spine_1_middle_back_pt"
HAnimSite507.name = "spine_1_middle_back_pt"
TouchSensor508 = x3d.TouchSensor()
TouchSensor508.description = "HAnimSite spine_1_middle_back_pt"

HAnimSite507.children.append(TouchSensor508)
Shape509 = x3d.Shape()
Shape509.USE = "HAnimSiteShape"

HAnimSite507.children.append(Shape509)

HAnimSegment499.children.append(HAnimSite507)

HAnimJoint498.children.append(HAnimSegment499)
HAnimJoint510 = x3d.HAnimJoint()
HAnimJoint510.DEF = "STD_Joint_vt4"
HAnimJoint510.name = "vt4"
HAnimJoint510.center = [0.0061,1.4320,-0.0675]
HAnimSegment511 = x3d.HAnimSegment()
HAnimSegment511.DEF = "STD_Segment_t4"
HAnimSegment511.name = "t4"
Transform512 = x3d.Transform()
Transform512.translation = [0.0061,1.4320,-0.0675]
Shape513 = x3d.Shape()
Shape513.USE = "HAnimJointShape"

Transform512.children.append(Shape513)

HAnimSegment511.children.append(Transform512)
Transform514 = x3d.Transform()
Shape515 = x3d.Shape()
LineSet516 = x3d.LineSet()
LineSet516.vertexCount = [2]
Coordinate517 = x3d.Coordinate()

LineSet516.coord = Coordinate517
ColorRGBA518 = x3d.ColorRGBA()
ColorRGBA518.USE = "HAnimSegmentLineColorRGBA"

LineSet516.color = ColorRGBA518

Shape515.geometry = LineSet516

Transform514.children.append(Shape515)

HAnimSegment511.children.append(Transform514)

HAnimJoint510.children.append(HAnimSegment511)
HAnimJoint519 = x3d.HAnimJoint()
HAnimJoint519.DEF = "STD_Joint_vt3"
HAnimJoint519.name = "vt3"
HAnimJoint519.center = [0.0062,1.4583,-0.0570]
HAnimSegment520 = x3d.HAnimSegment()
HAnimSegment520.DEF = "STD_Segment_t3"
HAnimSegment520.name = "t3"
Transform521 = x3d.Transform()
Transform521.translation = [0.0062,1.4583,-0.0570]
Shape522 = x3d.Shape()
Shape522.USE = "HAnimJointShape"

Transform521.children.append(Shape522)

HAnimSegment520.children.append(Transform521)
Transform523 = x3d.Transform()
Shape524 = x3d.Shape()
LineSet525 = x3d.LineSet()
LineSet525.vertexCount = [2]
Coordinate526 = x3d.Coordinate()

LineSet525.coord = Coordinate526
ColorRGBA527 = x3d.ColorRGBA()
ColorRGBA527.USE = "HAnimSegmentLineColorRGBA"

LineSet525.color = ColorRGBA527

Shape524.geometry = LineSet525

Transform523.children.append(Shape524)

HAnimSegment520.children.append(Transform523)

HAnimJoint519.children.append(HAnimSegment520)
HAnimJoint528 = x3d.HAnimJoint()
HAnimJoint528.DEF = "STD_Joint_vt2"
HAnimJoint528.name = "vt2"
HAnimJoint528.center = [0.0063,1.4761,-0.0484]
HAnimSegment529 = x3d.HAnimSegment()
HAnimSegment529.DEF = "STD_Segment_t2"
HAnimSegment529.name = "t2"
Transform530 = x3d.Transform()
Transform530.translation = [0.0063,1.4761,-0.0484]
Shape531 = x3d.Shape()
Shape531.USE = "HAnimJointShape"

Transform530.children.append(Shape531)

HAnimSegment529.children.append(Transform530)
Transform532 = x3d.Transform()
Shape533 = x3d.Shape()
LineSet534 = x3d.LineSet()
LineSet534.vertexCount = [2]
Coordinate535 = x3d.Coordinate()

LineSet534.coord = Coordinate535
ColorRGBA536 = x3d.ColorRGBA()
ColorRGBA536.USE = "HAnimSegmentLineColorRGBA"

LineSet534.color = ColorRGBA536

Shape533.geometry = LineSet534

Transform532.children.append(Shape533)

HAnimSegment529.children.append(Transform532)

HAnimJoint528.children.append(HAnimSegment529)
HAnimJoint537 = x3d.HAnimJoint()
HAnimJoint537.DEF = "STD_Joint_vt1"
HAnimJoint537.name = "vt1"
HAnimJoint537.center = [0.0065,1.4951,-0.0387]
HAnimSegment538 = x3d.HAnimSegment()
HAnimSegment538.DEF = "STD_Segment_t1"
HAnimSegment538.name = "t1"
Transform539 = x3d.Transform()
Transform539.translation = [0.0065,1.4951,-0.0387]
Shape540 = x3d.Shape()
Shape540.USE = "HAnimJointShape"

Transform539.children.append(Shape540)

HAnimSegment538.children.append(Transform539)
Transform541 = x3d.Transform()
Shape542 = x3d.Shape()
LineSet543 = x3d.LineSet()
LineSet543.vertexCount = [2]
Coordinate544 = x3d.Coordinate()

LineSet543.coord = Coordinate544
ColorRGBA545 = x3d.ColorRGBA()
ColorRGBA545.USE = "HAnimSegmentLineColorRGBA"

LineSet543.color = ColorRGBA545

Shape542.geometry = LineSet543

Transform541.children.append(Shape542)

HAnimSegment538.children.append(Transform541)
HAnimSite546 = x3d.HAnimSite()
HAnimSite546.DEF = "STD_Site_cervicale_pt"
HAnimSite546.name = "cervicale_pt"
HAnimSite546.translation = [0.0064,1.520,-0.0815]
TouchSensor547 = x3d.TouchSensor()
TouchSensor547.description = "HAnimSite cervicale_pt"

HAnimSite546.children.append(TouchSensor547)
Shape548 = x3d.Shape()
Shape548.USE = "HAnimSiteShape"

HAnimSite546.children.append(Shape548)

HAnimSegment538.children.append(HAnimSite546)
HAnimSite549 = x3d.HAnimSite()
HAnimSite549.DEF = "STD_Site_suprasternale_pt"
HAnimSite549.name = "suprasternale_pt"
HAnimSite549.translation = [0.0084,1.4714,0.0551]
TouchSensor550 = x3d.TouchSensor()
TouchSensor550.description = "HAnimSite suprasternale_pt"

HAnimSite549.children.append(TouchSensor550)
Shape551 = x3d.Shape()
Shape551.USE = "HAnimSiteShape"

HAnimSite549.children.append(Shape551)

HAnimSegment538.children.append(HAnimSite549)

HAnimJoint537.children.append(HAnimSegment538)
HAnimJoint552 = x3d.HAnimJoint()
HAnimJoint552.DEF = "STD_Joint_vc7"
HAnimJoint552.name = "vc7"
HAnimJoint552.center = [0.0066,1.5132,-0.0301]
HAnimSegment553 = x3d.HAnimSegment()
HAnimSegment553.DEF = "STD_Segment_c7"
HAnimSegment553.name = "c7"
Transform554 = x3d.Transform()
Transform554.translation = [0.0066,1.5132,-0.0301]
Shape555 = x3d.Shape()
Shape555.USE = "HAnimJointShape"

Transform554.children.append(Shape555)

HAnimSegment553.children.append(Transform554)
Transform556 = x3d.Transform()
Shape557 = x3d.Shape()
LineSet558 = x3d.LineSet()
LineSet558.vertexCount = [2]
Coordinate559 = x3d.Coordinate()

LineSet558.coord = Coordinate559
ColorRGBA560 = x3d.ColorRGBA()
ColorRGBA560.USE = "HAnimSegmentLineColorRGBA"

LineSet558.color = ColorRGBA560

Shape557.geometry = LineSet558

Transform556.children.append(Shape557)

HAnimSegment553.children.append(Transform556)
HAnimSite561 = x3d.HAnimSite()
HAnimSite561.DEF = "STD_Site_l_neck_base_pt"
HAnimSite561.name = "l_neck_base_pt"
HAnimSite561.translation = [0.0646,1.5141,-0.0380]
TouchSensor562 = x3d.TouchSensor()
TouchSensor562.description = "HAnimSite l_neck_base_pt"

HAnimSite561.children.append(TouchSensor562)
Shape563 = x3d.Shape()
Shape563.USE = "HAnimSiteShape"

HAnimSite561.children.append(Shape563)

HAnimSegment553.children.append(HAnimSite561)
HAnimSite564 = x3d.HAnimSite()
HAnimSite564.DEF = "STD_Site_r_neck_base_pt"
HAnimSite564.name = "r_neck_base_pt"
HAnimSite564.translation = [-0.0419,1.5149,-0.0220]
TouchSensor565 = x3d.TouchSensor()
TouchSensor565.description = "HAnimSite r_neck_base_pt"

HAnimSite564.children.append(TouchSensor565)
Shape566 = x3d.Shape()
Shape566.USE = "HAnimSiteShape"

HAnimSite564.children.append(Shape566)

HAnimSegment553.children.append(HAnimSite564)

HAnimJoint552.children.append(HAnimSegment553)
HAnimJoint567 = x3d.HAnimJoint()
HAnimJoint567.DEF = "STD_Joint_vc6"
HAnimJoint567.name = "vc6"
HAnimJoint567.center = [0.0066,1.5357,-0.0143]
HAnimSegment568 = x3d.HAnimSegment()
HAnimSegment568.DEF = "STD_Segment_c6"
HAnimSegment568.name = "c6"
Transform569 = x3d.Transform()
Transform569.translation = [0.0066,1.5357,-0.0143]
Shape570 = x3d.Shape()
Shape570.USE = "HAnimJointShape"

Transform569.children.append(Shape570)

HAnimSegment568.children.append(Transform569)
Transform571 = x3d.Transform()
Shape572 = x3d.Shape()
LineSet573 = x3d.LineSet()
LineSet573.vertexCount = [2]
Coordinate574 = x3d.Coordinate()

LineSet573.coord = Coordinate574
ColorRGBA575 = x3d.ColorRGBA()
ColorRGBA575.USE = "HAnimSegmentLineColorRGBA"

LineSet573.color = ColorRGBA575

Shape572.geometry = LineSet573

Transform571.children.append(Shape572)

HAnimSegment568.children.append(Transform571)

HAnimJoint567.children.append(HAnimSegment568)
HAnimJoint576 = x3d.HAnimJoint()
HAnimJoint576.DEF = "STD_Joint_vc5"
HAnimJoint576.name = "vc5"
HAnimJoint576.center = [0.0066,1.5520,-0.0082]
HAnimSegment577 = x3d.HAnimSegment()
HAnimSegment577.DEF = "STD_Segment_c5"
HAnimSegment577.name = "c5"
Transform578 = x3d.Transform()
Transform578.translation = [0.0066,1.5520,-0.0082]
Shape579 = x3d.Shape()
Shape579.USE = "HAnimJointShape"

Transform578.children.append(Shape579)

HAnimSegment577.children.append(Transform578)
Transform580 = x3d.Transform()
Shape581 = x3d.Shape()
LineSet582 = x3d.LineSet()
LineSet582.vertexCount = [2]
Coordinate583 = x3d.Coordinate()

LineSet582.coord = Coordinate583
ColorRGBA584 = x3d.ColorRGBA()
ColorRGBA584.USE = "HAnimSegmentLineColorRGBA"

LineSet582.color = ColorRGBA584

Shape581.geometry = LineSet582

Transform580.children.append(Shape581)

HAnimSegment577.children.append(Transform580)

HAnimJoint576.children.append(HAnimSegment577)
HAnimJoint585 = x3d.HAnimJoint()
HAnimJoint585.DEF = "STD_Joint_vc4"
HAnimJoint585.name = "vc4"
HAnimJoint585.center = [0.0066,1.5662,-0.0084]
HAnimSegment586 = x3d.HAnimSegment()
HAnimSegment586.DEF = "STD_Segment_c4"
HAnimSegment586.name = "c4"
Transform587 = x3d.Transform()
Transform587.translation = [0.0066,1.5662,-0.0084]
Shape588 = x3d.Shape()
Shape588.USE = "HAnimJointShape"

Transform587.children.append(Shape588)

HAnimSegment586.children.append(Transform587)
Transform589 = x3d.Transform()
Shape590 = x3d.Shape()
LineSet591 = x3d.LineSet()
LineSet591.vertexCount = [2]
Coordinate592 = x3d.Coordinate()

LineSet591.coord = Coordinate592
ColorRGBA593 = x3d.ColorRGBA()
ColorRGBA593.USE = "HAnimSegmentLineColorRGBA"

LineSet591.color = ColorRGBA593

Shape590.geometry = LineSet591

Transform589.children.append(Shape590)

HAnimSegment586.children.append(Transform589)

HAnimJoint585.children.append(HAnimSegment586)
HAnimJoint594 = x3d.HAnimJoint()
HAnimJoint594.DEF = "STD_Joint_vc3"
HAnimJoint594.name = "vc3"
HAnimJoint594.center = [0.0066,1.5800,-0.0103]
HAnimSegment595 = x3d.HAnimSegment()
HAnimSegment595.DEF = "STD_Segment_c3"
HAnimSegment595.name = "c3"
Transform596 = x3d.Transform()
Transform596.translation = [0.0066,1.5800,-0.0103]
Shape597 = x3d.Shape()
Shape597.USE = "HAnimJointShape"

Transform596.children.append(Shape597)

HAnimSegment595.children.append(Transform596)
Transform598 = x3d.Transform()
Shape599 = x3d.Shape()
LineSet600 = x3d.LineSet()
LineSet600.vertexCount = [2]
Coordinate601 = x3d.Coordinate()

LineSet600.coord = Coordinate601
ColorRGBA602 = x3d.ColorRGBA()
ColorRGBA602.USE = "HAnimSegmentLineColorRGBA"

LineSet600.color = ColorRGBA602

Shape599.geometry = LineSet600

Transform598.children.append(Shape599)

HAnimSegment595.children.append(Transform598)

HAnimJoint594.children.append(HAnimSegment595)
HAnimJoint603 = x3d.HAnimJoint()
HAnimJoint603.DEF = "STD_Joint_vc2"
HAnimJoint603.name = "vc2"
HAnimJoint603.center = [0.0066,1.5928,-0.0103]
HAnimSegment604 = x3d.HAnimSegment()
HAnimSegment604.DEF = "STD_Segment_c2"
HAnimSegment604.name = "c2"
Transform605 = x3d.Transform()
Transform605.translation = [0.0066,1.5928,-0.0103]
Shape606 = x3d.Shape()
Shape606.USE = "HAnimJointShape"

Transform605.children.append(Shape606)

HAnimSegment604.children.append(Transform605)
Transform607 = x3d.Transform()
Shape608 = x3d.Shape()
LineSet609 = x3d.LineSet()
LineSet609.vertexCount = [2]
Coordinate610 = x3d.Coordinate()

LineSet609.coord = Coordinate610
ColorRGBA611 = x3d.ColorRGBA()
ColorRGBA611.USE = "HAnimSegmentLineColorRGBA"

LineSet609.color = ColorRGBA611

Shape608.geometry = LineSet609

Transform607.children.append(Shape608)

HAnimSegment604.children.append(Transform607)
HAnimSite612 = x3d.HAnimSite()
HAnimSite612.DEF = "STD_Site_adams_apple_pt"
HAnimSite612.name = "adams_apple_pt"
TouchSensor613 = x3d.TouchSensor()
TouchSensor613.description = "HAnimSite adams_apple_pt"

HAnimSite612.children.append(TouchSensor613)
Shape614 = x3d.Shape()
Shape614.USE = "HAnimSiteShape"

HAnimSite612.children.append(Shape614)

HAnimSegment604.children.append(HAnimSite612)

HAnimJoint603.children.append(HAnimSegment604)
HAnimJoint615 = x3d.HAnimJoint()
HAnimJoint615.DEF = "STD_Joint_vc1"
HAnimJoint615.name = "vc1"
HAnimJoint615.center = [0.0066,1.6144,-0.0034]
HAnimSegment616 = x3d.HAnimSegment()
HAnimSegment616.DEF = "STD_Segment_c1"
HAnimSegment616.name = "c1"
Transform617 = x3d.Transform()
Transform617.translation = [0.0066,1.6144,-0.0034]
Shape618 = x3d.Shape()
Shape618.USE = "HAnimJointShape"

Transform617.children.append(Shape618)

HAnimSegment616.children.append(Transform617)
Transform619 = x3d.Transform()
Shape620 = x3d.Shape()
LineSet621 = x3d.LineSet()
LineSet621.vertexCount = [2]
Coordinate622 = x3d.Coordinate()

LineSet621.coord = Coordinate622
ColorRGBA623 = x3d.ColorRGBA()
ColorRGBA623.USE = "HAnimSegmentLineColorRGBA"

LineSet621.color = ColorRGBA623

Shape620.geometry = LineSet621

Transform619.children.append(Shape620)

HAnimSegment616.children.append(Transform619)

HAnimJoint615.children.append(HAnimSegment616)
HAnimJoint624 = x3d.HAnimJoint()
HAnimJoint624.DEF = "STD_Joint_skullbase"
HAnimJoint624.name = "skullbase"
HAnimJoint624.center = [0.0044,1.6209,0.0236]
HAnimSegment625 = x3d.HAnimSegment()
HAnimSegment625.DEF = "STD_Segment_skull"
HAnimSegment625.name = "skull"
Transform626 = x3d.Transform()
Transform626.translation = [0.0044,1.6209,0.0236]
Shape627 = x3d.Shape()
Shape627.USE = "HAnimJointShape"

Transform626.children.append(Shape627)

HAnimSegment625.children.append(Transform626)
Transform628 = x3d.Transform()
Shape629 = x3d.Shape()
LineSet630 = x3d.LineSet()
LineSet630.vertexCount = [2]
Coordinate631 = x3d.Coordinate()

LineSet630.coord = Coordinate631
ColorRGBA632 = x3d.ColorRGBA()
ColorRGBA632.USE = "HAnimSegmentLineColorRGBA"

LineSet630.color = ColorRGBA632

Shape629.geometry = LineSet630

Transform628.children.append(Shape629)

HAnimSegment625.children.append(Transform628)
HAnimSite633 = x3d.HAnimSite()
HAnimSite633.DEF = "STD_Site_glabella_pt"
HAnimSite633.name = "glabella_pt"
TouchSensor634 = x3d.TouchSensor()
TouchSensor634.description = "HAnimSite glabella_pt"

HAnimSite633.children.append(TouchSensor634)
Shape635 = x3d.Shape()
Shape635.USE = "HAnimSiteShape"

HAnimSite633.children.append(Shape635)

HAnimSegment625.children.append(HAnimSite633)
HAnimSite636 = x3d.HAnimSite()
HAnimSite636.DEF = "STD_Site_l_ectocanthus_pt"
HAnimSite636.name = "l_ectocanthus_pt"
TouchSensor637 = x3d.TouchSensor()
TouchSensor637.description = "HAnimSite l_ectocanthus_pt"

HAnimSite636.children.append(TouchSensor637)
Shape638 = x3d.Shape()
Shape638.USE = "HAnimSiteShape"

HAnimSite636.children.append(Shape638)

HAnimSegment625.children.append(HAnimSite636)
HAnimSite639 = x3d.HAnimSite()
HAnimSite639.DEF = "STD_Site_l_infraorbitale_pt"
HAnimSite639.name = "l_infraorbitale_pt"
HAnimSite639.translation = [0.0341,1.6171,0.0752]
TouchSensor640 = x3d.TouchSensor()
TouchSensor640.description = "HAnimSite l_infraorbitale_pt"

HAnimSite639.children.append(TouchSensor640)
Shape641 = x3d.Shape()
Shape641.USE = "HAnimSiteShape"

HAnimSite639.children.append(Shape641)

HAnimSegment625.children.append(HAnimSite639)
HAnimSite642 = x3d.HAnimSite()
HAnimSite642.DEF = "STD_Site_l_tragion_pt"
HAnimSite642.name = "l_tragion_pt"
HAnimSite642.translation = [0.0739,1.6348,0.0282]
TouchSensor643 = x3d.TouchSensor()
TouchSensor643.description = "HAnimSite l_tragion_pt"

HAnimSite642.children.append(TouchSensor643)
Shape644 = x3d.Shape()
Shape644.USE = "HAnimSiteShape"

HAnimSite642.children.append(Shape644)

HAnimSegment625.children.append(HAnimSite642)
HAnimSite645 = x3d.HAnimSite()
HAnimSite645.DEF = "STD_Site_nuchale_pt"
HAnimSite645.name = "nuchale_pt"
HAnimSite645.translation = [0.0039,1.5972,-0.0796]
TouchSensor646 = x3d.TouchSensor()
TouchSensor646.description = "HAnimSite nuchale_pt"

HAnimSite645.children.append(TouchSensor646)
Shape647 = x3d.Shape()
Shape647.USE = "HAnimSiteShape"

HAnimSite645.children.append(Shape647)

HAnimSegment625.children.append(HAnimSite645)
HAnimSite648 = x3d.HAnimSite()
HAnimSite648.DEF = "STD_Site_opisthocranion_pt"
HAnimSite648.name = "opisthocranion_pt"
TouchSensor649 = x3d.TouchSensor()
TouchSensor649.description = "HAnimSite opisthocranion_pt"

HAnimSite648.children.append(TouchSensor649)
Shape650 = x3d.Shape()
Shape650.USE = "HAnimSiteShape"

HAnimSite648.children.append(Shape650)

HAnimSegment625.children.append(HAnimSite648)
HAnimSite651 = x3d.HAnimSite()
HAnimSite651.DEF = "STD_Site_r_ectocanthus_pt"
HAnimSite651.name = "r_ectocanthus_pt"
TouchSensor652 = x3d.TouchSensor()
TouchSensor652.description = "HAnimSite r_ectocanthus_pt"

HAnimSite651.children.append(TouchSensor652)
Shape653 = x3d.Shape()
Shape653.USE = "HAnimSiteShape"

HAnimSite651.children.append(Shape653)

HAnimSegment625.children.append(HAnimSite651)
HAnimSite654 = x3d.HAnimSite()
HAnimSite654.DEF = "STD_Site_r_infraorbitale_pt"
HAnimSite654.name = "r_infraorbitale_pt"
HAnimSite654.translation = [-0.0237,1.6171,0.0752]
TouchSensor655 = x3d.TouchSensor()
TouchSensor655.description = "HAnimSite r_infraorbitale_pt"

HAnimSite654.children.append(TouchSensor655)
Shape656 = x3d.Shape()
Shape656.USE = "HAnimSiteShape"

HAnimSite654.children.append(Shape656)

HAnimSegment625.children.append(HAnimSite654)
HAnimSite657 = x3d.HAnimSite()
HAnimSite657.DEF = "STD_Site_r_tragion_pt"
HAnimSite657.name = "r_tragion_pt"
HAnimSite657.translation = [-0.0646,1.6347,0.0302]
TouchSensor658 = x3d.TouchSensor()
TouchSensor658.description = "HAnimSite r_tragion_pt"

HAnimSite657.children.append(TouchSensor658)
Shape659 = x3d.Shape()
Shape659.USE = "HAnimSiteShape"

HAnimSite657.children.append(Shape659)

HAnimSegment625.children.append(HAnimSite657)
HAnimSite660 = x3d.HAnimSite()
HAnimSite660.DEF = "STD_Site_sellion_pt"
HAnimSite660.name = "sellion_pt"
HAnimSite660.translation = [0.0058,1.6316,0.0852]
TouchSensor661 = x3d.TouchSensor()
TouchSensor661.description = "HAnimSite sellion_pt"

HAnimSite660.children.append(TouchSensor661)
Shape662 = x3d.Shape()
Shape662.USE = "HAnimSiteShape"

HAnimSite660.children.append(Shape662)

HAnimSegment625.children.append(HAnimSite660)
HAnimSite663 = x3d.HAnimSite()
HAnimSite663.DEF = "STD_Site_skull_vertex_pt"
HAnimSite663.name = "skull_vertex_pt"
HAnimSite663.translation = [0.0050,1.7504,0.0055]
TouchSensor664 = x3d.TouchSensor()
TouchSensor664.description = "HAnimSite skull_vertex_pt"

HAnimSite663.children.append(TouchSensor664)
Shape665 = x3d.Shape()
Shape665.USE = "HAnimSiteShape"

HAnimSite663.children.append(Shape665)

HAnimSegment625.children.append(HAnimSite663)

HAnimJoint624.children.append(HAnimSegment625)
HAnimJoint666 = x3d.HAnimJoint()
HAnimJoint666.DEF = "STD_Joint_l_eyelid_joint"
HAnimJoint666.name = "l_eyelid_joint"
HAnimSegment667 = x3d.HAnimSegment()
HAnimSegment667.DEF = "STD_Segment_l_eyelid"
HAnimSegment667.name = "l_eyelid"
Transform668 = x3d.Transform()
Shape669 = x3d.Shape()
LineSet670 = x3d.LineSet()
LineSet670.vertexCount = [2]
Coordinate671 = x3d.Coordinate()

LineSet670.coord = Coordinate671
ColorRGBA672 = x3d.ColorRGBA()
ColorRGBA672.USE = "HAnimSegmentLineColorRGBA"

LineSet670.color = ColorRGBA672

Shape669.geometry = LineSet670

Transform668.children.append(Shape669)

HAnimSegment667.children.append(Transform668)

HAnimJoint666.children.append(HAnimSegment667)
HAnimJoint673 = x3d.HAnimJoint()
HAnimJoint673.DEF = "STD_Joint_r_eyelid_joint"
HAnimJoint673.name = "r_eyelid_joint"
HAnimSegment674 = x3d.HAnimSegment()
HAnimSegment674.DEF = "STD_Segment_r_eyelid"
HAnimSegment674.name = "r_eyelid"

HAnimJoint673.children.append(HAnimSegment674)
HAnimJoint675 = x3d.HAnimJoint()
HAnimJoint675.DEF = "STD_Joint_l_eyeball_joint"
HAnimJoint675.name = "l_eyeball_joint"
HAnimSegment676 = x3d.HAnimSegment()
HAnimSegment676.DEF = "STD_Segment_l_eyeball"
HAnimSegment676.name = "l_eyeball"

HAnimJoint675.children.append(HAnimSegment676)
HAnimJoint677 = x3d.HAnimJoint()
HAnimJoint677.DEF = "STD_Joint_r_eyeball_joint"
HAnimJoint677.name = "r_eyeball_joint"
HAnimSegment678 = x3d.HAnimSegment()
HAnimSegment678.DEF = "STD_Segment_r_eyeball"
HAnimSegment678.name = "r_eyeball"

HAnimJoint677.children.append(HAnimSegment678)
HAnimJoint679 = x3d.HAnimJoint()
HAnimJoint679.DEF = "STD_Joint_l_eyebrow_joint"
HAnimJoint679.name = "l_eyebrow_joint"
HAnimSegment680 = x3d.HAnimSegment()
HAnimSegment680.DEF = "STD_Segment_l_eyebrow"
HAnimSegment680.name = "l_eyebrow"

HAnimJoint679.children.append(HAnimSegment680)
HAnimJoint681 = x3d.HAnimJoint()
HAnimJoint681.DEF = "STD_Joint_r_eyebrow_joint"
HAnimJoint681.name = "r_eyebrow_joint"
HAnimSegment682 = x3d.HAnimSegment()
HAnimSegment682.DEF = "STD_Segment_r_eyebrow"
HAnimSegment682.name = "r_eyebrow"

HAnimJoint681.children.append(HAnimSegment682)
HAnimJoint683 = x3d.HAnimJoint()
HAnimJoint683.DEF = "STD_Joint_temporomandibular"
HAnimJoint683.name = "temporomandibular"
HAnimSegment684 = x3d.HAnimSegment()
HAnimSegment684.DEF = "STD_Segment_jaw"
HAnimSegment684.name = "jaw"
HAnimSite685 = x3d.HAnimSite()
HAnimSite685.DEF = "STD_Site_l_gonion_pt"
HAnimSite685.name = "l_gonion_pt"
HAnimSite685.translation = [0.0631,1.5530,0.0330]
TouchSensor686 = x3d.TouchSensor()
TouchSensor686.description = "HAnimSite l_gonion_pt"

HAnimSite685.children.append(TouchSensor686)
Shape687 = x3d.Shape()
Shape687.USE = "HAnimSiteShape"

HAnimSite685.children.append(Shape687)

HAnimSegment684.children.append(HAnimSite685)
HAnimSite688 = x3d.HAnimSite()
HAnimSite688.DEF = "STD_Site_menton_pt"
HAnimSite688.name = "menton_pt"
TouchSensor689 = x3d.TouchSensor()
TouchSensor689.description = "HAnimSite menton_pt"

HAnimSite688.children.append(TouchSensor689)
Shape690 = x3d.Shape()
Shape690.USE = "HAnimSiteShape"

HAnimSite688.children.append(Shape690)

HAnimSegment684.children.append(HAnimSite688)
HAnimSite691 = x3d.HAnimSite()
HAnimSite691.DEF = "STD_Site_r_gonion_pt"
HAnimSite691.name = "r_gonion_pt"
HAnimSite691.translation = [-0.0520,1.5529,0.0347]
TouchSensor692 = x3d.TouchSensor()
TouchSensor692.description = "HAnimSite r_gonion_pt"

HAnimSite691.children.append(TouchSensor692)
Shape693 = x3d.Shape()
Shape693.USE = "HAnimSiteShape"

HAnimSite691.children.append(Shape693)

HAnimSegment684.children.append(HAnimSite691)
HAnimSite694 = x3d.HAnimSite()
HAnimSite694.DEF = "STD_Site_supramenton_pt"
HAnimSite694.name = "supramenton_pt"
HAnimSite694.translation = [0.0061,1.5410,0.0805]
TouchSensor695 = x3d.TouchSensor()
TouchSensor695.description = "HAnimSite supramenton_pt"

HAnimSite694.children.append(TouchSensor695)
Shape696 = x3d.Shape()
Shape696.USE = "HAnimSiteShape"

HAnimSite694.children.append(Shape696)

HAnimSegment684.children.append(HAnimSite694)

HAnimJoint683.children.append(HAnimSegment684)

HAnimJoint681.children.append(HAnimJoint683)

HAnimJoint679.children.append(HAnimJoint681)

HAnimJoint677.children.append(HAnimJoint679)

HAnimJoint675.children.append(HAnimJoint677)

HAnimJoint673.children.append(HAnimJoint675)

HAnimJoint666.children.append(HAnimJoint673)

HAnimJoint624.children.append(HAnimJoint666)

HAnimJoint615.children.append(HAnimJoint624)

HAnimJoint603.children.append(HAnimJoint615)

HAnimJoint594.children.append(HAnimJoint603)

HAnimJoint585.children.append(HAnimJoint594)

HAnimJoint576.children.append(HAnimJoint585)

HAnimJoint567.children.append(HAnimJoint576)

HAnimJoint552.children.append(HAnimJoint567)

HAnimJoint537.children.append(HAnimJoint552)
HAnimJoint697 = x3d.HAnimJoint()
HAnimJoint697.DEF = "STD_Joint_l_sternoclavicular"
HAnimJoint697.name = "l_sternoclavicular"
HAnimJoint697.center = [0.0820,1.4488,-0.0353]
HAnimSegment698 = x3d.HAnimSegment()
HAnimSegment698.DEF = "STD_Segment_l_clavicle"
HAnimSegment698.name = "l_clavicle"
Transform699 = x3d.Transform()
Transform699.translation = [0.0820,1.4488,-0.0353]
Shape700 = x3d.Shape()
Shape700.USE = "HAnimJointShape"

Transform699.children.append(Shape700)

HAnimSegment698.children.append(Transform699)
Transform701 = x3d.Transform()
Shape702 = x3d.Shape()
LineSet703 = x3d.LineSet()
LineSet703.vertexCount = [2]
Coordinate704 = x3d.Coordinate()

LineSet703.coord = Coordinate704
ColorRGBA705 = x3d.ColorRGBA()
ColorRGBA705.USE = "HAnimSegmentLineColorRGBA"

LineSet703.color = ColorRGBA705

Shape702.geometry = LineSet703

Transform701.children.append(Shape702)

HAnimSegment698.children.append(Transform701)
HAnimSite706 = x3d.HAnimSite()
HAnimSite706.DEF = "STD_Site_l_acromion_pt"
HAnimSite706.name = "l_acromion_pt"
HAnimSite706.translation = [0.2032,1.4760,-0.0490]
TouchSensor707 = x3d.TouchSensor()
TouchSensor707.description = "HAnimSite l_acromion_pt"

HAnimSite706.children.append(TouchSensor707)
Shape708 = x3d.Shape()
Shape708.USE = "HAnimSiteShape"

HAnimSite706.children.append(Shape708)

HAnimSegment698.children.append(HAnimSite706)
HAnimSite709 = x3d.HAnimSite()
HAnimSite709.DEF = "STD_Site_l_axilla_distal_pt"
HAnimSite709.name = "l_axilla_distal_pt"
HAnimSite709.translation = [0.1706,1.4072,-0.0875]
TouchSensor710 = x3d.TouchSensor()
TouchSensor710.description = "HAnimSite l_axilla_distal_pt"

HAnimSite709.children.append(TouchSensor710)
Shape711 = x3d.Shape()
Shape711.USE = "HAnimSiteShape"

HAnimSite709.children.append(Shape711)

HAnimSegment698.children.append(HAnimSite709)
HAnimSite712 = x3d.HAnimSite()
HAnimSite712.DEF = "STD_Site_l_axilla_posterior_folds_pt"
HAnimSite712.name = "l_axilla_posterior_folds_pt"
TouchSensor713 = x3d.TouchSensor()
TouchSensor713.description = "HAnimSite l_axilla_posterior_folds_pt"

HAnimSite712.children.append(TouchSensor713)
Shape714 = x3d.Shape()
Shape714.USE = "HAnimSiteShape"

HAnimSite712.children.append(Shape714)

HAnimSegment698.children.append(HAnimSite712)
HAnimSite715 = x3d.HAnimSite()
HAnimSite715.DEF = "STD_Site_l_axilla_proximal_pt"
HAnimSite715.name = "l_axilla_proximal_pt"
HAnimSite715.translation = [0.1777,1.4065,-0.0075]
TouchSensor716 = x3d.TouchSensor()
TouchSensor716.description = "HAnimSite l_axilla_proximal_pt"

HAnimSite715.children.append(TouchSensor716)
Shape717 = x3d.Shape()
Shape717.USE = "HAnimSiteShape"

HAnimSite715.children.append(Shape717)

HAnimSegment698.children.append(HAnimSite715)
HAnimSite718 = x3d.HAnimSite()
HAnimSite718.DEF = "STD_Site_l_clavicale_pt"
HAnimSite718.name = "l_clavicale_pt"
HAnimSite718.translation = [0.0271,1.4943,0.0394]
TouchSensor719 = x3d.TouchSensor()
TouchSensor719.description = "HAnimSite l_clavicale_pt"

HAnimSite718.children.append(TouchSensor719)
Shape720 = x3d.Shape()
Shape720.USE = "HAnimSiteShape"

HAnimSite718.children.append(Shape720)

HAnimSegment698.children.append(HAnimSite718)

HAnimJoint697.children.append(HAnimSegment698)
HAnimJoint721 = x3d.HAnimJoint()
HAnimJoint721.DEF = "STD_Joint_l_acromioclavicular"
HAnimJoint721.name = "l_acromioclavicular"
HAnimJoint721.center = [0.0962,1.4269,-0.0424]
HAnimSegment722 = x3d.HAnimSegment()
HAnimSegment722.DEF = "STD_Segment_l_scapula"
HAnimSegment722.name = "l_scapula"
Transform723 = x3d.Transform()
Transform723.translation = [0.0962,1.4269,-0.0424]
Shape724 = x3d.Shape()
Shape724.USE = "HAnimJointShape"

Transform723.children.append(Shape724)

HAnimSegment722.children.append(Transform723)
Transform725 = x3d.Transform()
Shape726 = x3d.Shape()
LineSet727 = x3d.LineSet()
LineSet727.vertexCount = [2]
Coordinate728 = x3d.Coordinate()

LineSet727.coord = Coordinate728
ColorRGBA729 = x3d.ColorRGBA()
ColorRGBA729.USE = "HAnimSegmentLineColorRGBA"

LineSet727.color = ColorRGBA729

Shape726.geometry = LineSet727

Transform725.children.append(Shape726)

HAnimSegment722.children.append(Transform725)

HAnimJoint721.children.append(HAnimSegment722)
HAnimJoint730 = x3d.HAnimJoint()
HAnimJoint730.DEF = "STD_Joint_l_shoulder"
HAnimJoint730.name = "l_shoulder"
HAnimJoint730.center = [0.2029,1.4376,-0.0387]
HAnimSegment731 = x3d.HAnimSegment()
HAnimSegment731.DEF = "STD_Segment_l_upperarm"
HAnimSegment731.name = "l_upperarm"
Transform732 = x3d.Transform()
Transform732.translation = [0.2029,1.4376,-0.0387]
Shape733 = x3d.Shape()
Shape733.USE = "HAnimJointShape"

Transform732.children.append(Shape733)

HAnimSegment731.children.append(Transform732)
Transform734 = x3d.Transform()
Shape735 = x3d.Shape()
LineSet736 = x3d.LineSet()
LineSet736.vertexCount = [2]
Coordinate737 = x3d.Coordinate()

LineSet736.coord = Coordinate737
ColorRGBA738 = x3d.ColorRGBA()
ColorRGBA738.USE = "HAnimSegmentLineColorRGBA"

LineSet736.color = ColorRGBA738

Shape735.geometry = LineSet736

Transform734.children.append(Shape735)

HAnimSegment731.children.append(Transform734)
HAnimSite739 = x3d.HAnimSite()
HAnimSite739.DEF = "STD_Site_l_bideltoid_pt"
HAnimSite739.name = "l_bideltoid_pt"
TouchSensor740 = x3d.TouchSensor()
TouchSensor740.description = "HAnimSite l_bideltoid_pt"

HAnimSite739.children.append(TouchSensor740)
Shape741 = x3d.Shape()
Shape741.USE = "HAnimSiteShape"

HAnimSite739.children.append(Shape741)

HAnimSegment731.children.append(HAnimSite739)
HAnimSite742 = x3d.HAnimSite()
HAnimSite742.DEF = "STD_Site_l_humeral_lateral_epicondyles_pt"
HAnimSite742.name = "l_humeral_lateral_epicondyles_pt"
HAnimSite742.translation = [0.2280,1.1482,-0.1100]
TouchSensor743 = x3d.TouchSensor()
TouchSensor743.description = "HAnimSite l_humeral_lateral_epicondyles_pt"

HAnimSite742.children.append(TouchSensor743)
Shape744 = x3d.Shape()
Shape744.USE = "HAnimSiteShape"

HAnimSite742.children.append(Shape744)

HAnimSegment731.children.append(HAnimSite742)

HAnimJoint730.children.append(HAnimSegment731)
HAnimJoint745 = x3d.HAnimJoint()
HAnimJoint745.DEF = "STD_Joint_l_elbow"
HAnimJoint745.name = "l_elbow"
HAnimJoint745.center = [0.2014,1.1357,-0.0682]
HAnimSegment746 = x3d.HAnimSegment()
HAnimSegment746.DEF = "STD_Segment_l_forearm"
HAnimSegment746.name = "l_forearm"
Transform747 = x3d.Transform()
Transform747.translation = [0.2014,1.1357,-0.0682]
Shape748 = x3d.Shape()
Shape748.USE = "HAnimJointShape"

Transform747.children.append(Shape748)

HAnimSegment746.children.append(Transform747)
Transform749 = x3d.Transform()
Shape750 = x3d.Shape()
LineSet751 = x3d.LineSet()
LineSet751.vertexCount = [2]
Coordinate752 = x3d.Coordinate()

LineSet751.coord = Coordinate752
ColorRGBA753 = x3d.ColorRGBA()
ColorRGBA753.USE = "HAnimSegmentLineColorRGBA"

LineSet751.color = ColorRGBA753

Shape750.geometry = LineSet751

Transform749.children.append(Shape750)

HAnimSegment746.children.append(Transform749)
HAnimSite754 = x3d.HAnimSite()
HAnimSite754.DEF = "STD_Site_l_humeral_medial_epicondyles_pt"
HAnimSite754.name = "l_humeral_medial_epicondyles_pt"
HAnimSite754.translation = [0.1735,1.1272,-0.1113]
TouchSensor755 = x3d.TouchSensor()
TouchSensor755.description = "HAnimSite l_humeral_medial_epicondyles_pt"

HAnimSite754.children.append(TouchSensor755)
Shape756 = x3d.Shape()
Shape756.USE = "HAnimSiteShape"

HAnimSite754.children.append(Shape756)

HAnimSegment746.children.append(HAnimSite754)
HAnimSite757 = x3d.HAnimSite()
HAnimSite757.DEF = "STD_Site_l_olecranon_pt"
HAnimSite757.name = "l_olecranon_pt"
HAnimSite757.translation = [-0.1962,1.1375,-0.1123]
TouchSensor758 = x3d.TouchSensor()
TouchSensor758.description = "HAnimSite l_olecranon_pt"

HAnimSite757.children.append(TouchSensor758)
Shape759 = x3d.Shape()
Shape759.USE = "HAnimSiteShape"

HAnimSite757.children.append(Shape759)

HAnimSegment746.children.append(HAnimSite757)
HAnimSite760 = x3d.HAnimSite()
HAnimSite760.DEF = "STD_Site_l_radial_styloid_pt"
HAnimSite760.name = "l_radial_styloid_pt"
HAnimSite760.translation = [0.1901,0.8645,-0.0415]
TouchSensor761 = x3d.TouchSensor()
TouchSensor761.description = "HAnimSite l_radial_styloid_pt"

HAnimSite760.children.append(TouchSensor761)
Shape762 = x3d.Shape()
Shape762.USE = "HAnimSiteShape"

HAnimSite760.children.append(Shape762)

HAnimSegment746.children.append(HAnimSite760)
HAnimSite763 = x3d.HAnimSite()
HAnimSite763.DEF = "STD_Site_l_radiale_pt"
HAnimSite763.name = "l_radiale_pt"
HAnimSite763.translation = [0.2182,1.1212,-0.1167]
TouchSensor764 = x3d.TouchSensor()
TouchSensor764.description = "HAnimSite l_radiale_pt"

HAnimSite763.children.append(TouchSensor764)
Shape765 = x3d.Shape()
Shape765.USE = "HAnimSiteShape"

HAnimSite763.children.append(Shape765)

HAnimSegment746.children.append(HAnimSite763)

HAnimJoint745.children.append(HAnimSegment746)
HAnimJoint766 = x3d.HAnimJoint()
HAnimJoint766.DEF = "STD_Joint_l_radiocarpal"
HAnimJoint766.name = "l_radiocarpal"
HAnimJoint766.center = [0.1984,0.8663,-0.0583]
HAnimSegment767 = x3d.HAnimSegment()
HAnimSegment767.DEF = "STD_Segment_l_carpal"
HAnimSegment767.name = "l_carpal"
Transform768 = x3d.Transform()
Transform768.translation = [0.1984,0.8663,-0.0583]
Shape769 = x3d.Shape()
Shape769.USE = "HAnimJointShape"

Transform768.children.append(Shape769)

HAnimSegment767.children.append(Transform768)
Transform770 = x3d.Transform()
Shape771 = x3d.Shape()
LineSet772 = x3d.LineSet()
LineSet772.vertexCount = [2]
Coordinate773 = x3d.Coordinate()

LineSet772.coord = Coordinate773
ColorRGBA774 = x3d.ColorRGBA()
ColorRGBA774.USE = "HAnimSegmentLineColorRGBA"

LineSet772.color = ColorRGBA774

Shape771.geometry = LineSet772

Transform770.children.append(Shape771)

HAnimSegment767.children.append(Transform770)
HAnimSite775 = x3d.HAnimSite()
HAnimSite775.DEF = "STD_Site_l_ulnar_styloid_pt"
HAnimSite775.name = "l_ulnar_styloid_pt"
HAnimSite775.translation = [-0.2142,0.8529,-0.0648]
TouchSensor776 = x3d.TouchSensor()
TouchSensor776.description = "HAnimSite l_ulnar_styloid_pt"

HAnimSite775.children.append(TouchSensor776)
Shape777 = x3d.Shape()
Shape777.USE = "HAnimSiteShape"

HAnimSite775.children.append(Shape777)

HAnimSegment767.children.append(HAnimSite775)

HAnimJoint766.children.append(HAnimSegment767)
HAnimJoint778 = x3d.HAnimJoint()
HAnimJoint778.DEF = "STD_Joint_l_midcarpal_1"
HAnimJoint778.name = "l_midcarpal_1"
HAnimSegment779 = x3d.HAnimSegment()
HAnimSegment779.DEF = "STD_Segment_l_trapezium"
HAnimSegment779.name = "l_trapezium"
Transform780 = x3d.Transform()
Shape781 = x3d.Shape()
LineSet782 = x3d.LineSet()
LineSet782.vertexCount = [2]
Coordinate783 = x3d.Coordinate()

LineSet782.coord = Coordinate783
ColorRGBA784 = x3d.ColorRGBA()
ColorRGBA784.USE = "HAnimSegmentLineColorRGBA"

LineSet782.color = ColorRGBA784

Shape781.geometry = LineSet782

Transform780.children.append(Shape781)

HAnimSegment779.children.append(Transform780)

HAnimJoint778.children.append(HAnimSegment779)
HAnimJoint785 = x3d.HAnimJoint()
HAnimJoint785.DEF = "STD_Joint_l_carpometacarpal_1"
HAnimJoint785.name = "l_carpometacarpal_1"
HAnimJoint785.center = [0.1924,0.8472,-0.0534]
HAnimSegment786 = x3d.HAnimSegment()
HAnimSegment786.DEF = "STD_Segment_l_metacarpal_1"
HAnimSegment786.name = "l_metacarpal_1"
Transform787 = x3d.Transform()
Transform787.translation = [0.1924,0.8472,-0.0534]
Shape788 = x3d.Shape()
Shape788.USE = "HAnimJointShape"

Transform787.children.append(Shape788)

HAnimSegment786.children.append(Transform787)
Transform789 = x3d.Transform()
Shape790 = x3d.Shape()
LineSet791 = x3d.LineSet()
LineSet791.vertexCount = [2]
Coordinate792 = x3d.Coordinate()

LineSet791.coord = Coordinate792
ColorRGBA793 = x3d.ColorRGBA()
ColorRGBA793.USE = "HAnimSegmentLineColorRGBA"

LineSet791.color = ColorRGBA793

Shape790.geometry = LineSet791

Transform789.children.append(Shape790)

HAnimSegment786.children.append(Transform789)

HAnimJoint785.children.append(HAnimSegment786)
HAnimJoint794 = x3d.HAnimJoint()
HAnimJoint794.DEF = "STD_Joint_l_metacarpophalangeal_1"
HAnimJoint794.name = "l_metacarpophalangeal_1"
HAnimJoint794.center = [0.1951,0.8226,0.0246]
HAnimSegment795 = x3d.HAnimSegment()
HAnimSegment795.DEF = "STD_Segment_l_carpal_proximal_phalanx_1"
HAnimSegment795.name = "l_carpal_proximal_phalanx_1"
Transform796 = x3d.Transform()
Transform796.translation = [0.1951,0.8226,0.0246]
Shape797 = x3d.Shape()
Shape797.USE = "HAnimJointShape"

Transform796.children.append(Shape797)

HAnimSegment795.children.append(Transform796)
Transform798 = x3d.Transform()
Shape799 = x3d.Shape()
LineSet800 = x3d.LineSet()
LineSet800.vertexCount = [2]
Coordinate801 = x3d.Coordinate()

LineSet800.coord = Coordinate801
ColorRGBA802 = x3d.ColorRGBA()
ColorRGBA802.USE = "HAnimSegmentLineColorRGBA"

LineSet800.color = ColorRGBA802

Shape799.geometry = LineSet800

Transform798.children.append(Shape799)

HAnimSegment795.children.append(Transform798)

HAnimJoint794.children.append(HAnimSegment795)
HAnimJoint803 = x3d.HAnimJoint()
HAnimJoint803.DEF = "STD_Joint_l_carpal_interphalangeal_1"
HAnimJoint803.name = "l_carpal_interphalangeal_1"
HAnimJoint803.center = [0.1955,0.8159,0.0464]
HAnimSegment804 = x3d.HAnimSegment()
HAnimSegment804.DEF = "STD_Segment_l_carpal_distal_phalanx_1"
HAnimSegment804.name = "l_carpal_distal_phalanx_1"
Transform805 = x3d.Transform()
Transform805.translation = [0.1955,0.8159,0.0464]
Shape806 = x3d.Shape()
Shape806.USE = "HAnimJointShape"

Transform805.children.append(Shape806)

HAnimSegment804.children.append(Transform805)
Transform807 = x3d.Transform()
Shape808 = x3d.Shape()
LineSet809 = x3d.LineSet()
LineSet809.vertexCount = [2]
Coordinate810 = x3d.Coordinate()

LineSet809.coord = Coordinate810
ColorRGBA811 = x3d.ColorRGBA()
ColorRGBA811.USE = "HAnimSegmentLineColorRGBA"

LineSet809.color = ColorRGBA811

Shape808.geometry = LineSet809

Transform807.children.append(Shape808)

HAnimSegment804.children.append(Transform807)
HAnimSite812 = x3d.HAnimSite()
HAnimSite812.DEF = "STD_Site_l_carpal_distal_phalanx_1_tip"
HAnimSite812.name = "l_carpal_distal_phalanx_1_tip"
TouchSensor813 = x3d.TouchSensor()
TouchSensor813.description = "HAnimSite l_carpal_distal_phalanx_1_tip"

HAnimSite812.children.append(TouchSensor813)
Shape814 = x3d.Shape()
Shape814.USE = "HAnimSiteShape"

HAnimSite812.children.append(Shape814)

HAnimSegment804.children.append(HAnimSite812)

HAnimJoint803.children.append(HAnimSegment804)

HAnimJoint794.children.append(HAnimJoint803)

HAnimJoint785.children.append(HAnimJoint794)

HAnimJoint778.children.append(HAnimJoint785)

HAnimJoint766.children.append(HAnimJoint778)
HAnimJoint815 = x3d.HAnimJoint()
HAnimJoint815.DEF = "STD_Joint_l_midcarpal_2"
HAnimJoint815.name = "l_midcarpal_2"
HAnimSegment816 = x3d.HAnimSegment()
HAnimSegment816.DEF = "STD_Segment_l_trapezoid"
HAnimSegment816.name = "l_trapezoid"

HAnimJoint815.children.append(HAnimSegment816)
HAnimJoint817 = x3d.HAnimJoint()
HAnimJoint817.DEF = "STD_Joint_l_carpometacarpal_2"
HAnimJoint817.name = "l_carpometacarpal_2"
HAnimJoint817.center = [0.1983,0.8024,-0.0280]
HAnimSegment818 = x3d.HAnimSegment()
HAnimSegment818.DEF = "STD_Segment_l_metacarpal_2"
HAnimSegment818.name = "l_metacarpal_2"
Transform819 = x3d.Transform()
Transform819.translation = [0.1983,0.8024,-0.0280]
Shape820 = x3d.Shape()
Shape820.USE = "HAnimJointShape"

Transform819.children.append(Shape820)

HAnimSegment818.children.append(Transform819)
Transform821 = x3d.Transform()
Shape822 = x3d.Shape()
LineSet823 = x3d.LineSet()
LineSet823.vertexCount = [2]
Coordinate824 = x3d.Coordinate()

LineSet823.coord = Coordinate824
ColorRGBA825 = x3d.ColorRGBA()
ColorRGBA825.USE = "HAnimSegmentLineColorRGBA"

LineSet823.color = ColorRGBA825

Shape822.geometry = LineSet823

Transform821.children.append(Shape822)

HAnimSegment818.children.append(Transform821)
HAnimSite826 = x3d.HAnimSite()
HAnimSite826.DEF = "STD_Site_l_metacarpal_phalanx_2_pt"
HAnimSite826.name = "l_metacarpal_phalanx_2_pt"
HAnimSite826.translation = [0.2009,0.8139,-0.0237]
TouchSensor827 = x3d.TouchSensor()
TouchSensor827.description = "HAnimSite l_metacarpal_phalanx_2_pt"

HAnimSite826.children.append(TouchSensor827)
Shape828 = x3d.Shape()
Shape828.USE = "HAnimSiteShape"

HAnimSite826.children.append(Shape828)

HAnimSegment818.children.append(HAnimSite826)

HAnimJoint817.children.append(HAnimSegment818)
HAnimJoint829 = x3d.HAnimJoint()
HAnimJoint829.DEF = "STD_Joint_l_metacarpophalangeal_2"
HAnimJoint829.name = "l_metacarpophalangeal_2"
HAnimJoint829.center = [0.1983,0.7815,-0.0280]
HAnimSegment830 = x3d.HAnimSegment()
HAnimSegment830.DEF = "STD_Segment_l_carpal_proximal_phalanx_2 "
HAnimSegment830.name = "l_carpal_proximal_phalanx_2 "
Transform831 = x3d.Transform()
Transform831.translation = [0.1983,0.7815,-0.0280]
Shape832 = x3d.Shape()
Shape832.USE = "HAnimJointShape"

Transform831.children.append(Shape832)

HAnimSegment830.children.append(Transform831)
Transform833 = x3d.Transform()
Shape834 = x3d.Shape()
LineSet835 = x3d.LineSet()
LineSet835.vertexCount = [2]
Coordinate836 = x3d.Coordinate()

LineSet835.coord = Coordinate836
ColorRGBA837 = x3d.ColorRGBA()
ColorRGBA837.USE = "HAnimSegmentLineColorRGBA"

LineSet835.color = ColorRGBA837

Shape834.geometry = LineSet835

Transform833.children.append(Shape834)

HAnimSegment830.children.append(Transform833)

HAnimJoint829.children.append(HAnimSegment830)
HAnimJoint838 = x3d.HAnimJoint()
HAnimJoint838.DEF = "STD_Joint_l_carpal_proximal_interphalangeal_2"
HAnimJoint838.name = "l_carpal_proximal_interphalangeal_2"
HAnimJoint838.center = [0.2017,0.7363,-0.0248]
HAnimSegment839 = x3d.HAnimSegment()
HAnimSegment839.DEF = "STD_Segment_l_carpal_middle_phalanx_2"
HAnimSegment839.name = "l_carpal_middle_phalanx_2"
Transform840 = x3d.Transform()
Transform840.translation = [0.2017,0.7363,-0.0248]
Shape841 = x3d.Shape()
Shape841.USE = "HAnimJointShape"

Transform840.children.append(Shape841)

HAnimSegment839.children.append(Transform840)
Transform842 = x3d.Transform()
Shape843 = x3d.Shape()
LineSet844 = x3d.LineSet()
LineSet844.vertexCount = [2]
Coordinate845 = x3d.Coordinate()

LineSet844.coord = Coordinate845
ColorRGBA846 = x3d.ColorRGBA()
ColorRGBA846.USE = "HAnimSegmentLineColorRGBA"

LineSet844.color = ColorRGBA846

Shape843.geometry = LineSet844

Transform842.children.append(Shape843)

HAnimSegment839.children.append(Transform842)

HAnimJoint838.children.append(HAnimSegment839)
HAnimJoint847 = x3d.HAnimJoint()
HAnimJoint847.DEF = "STD_Joint_l_carpal_distal_interphalangeal_2"
HAnimJoint847.name = "l_carpal_distal_interphalangeal_2"
HAnimJoint847.center = [0.2028,0.7139,-0.0236]
HAnimSegment848 = x3d.HAnimSegment()
HAnimSegment848.DEF = "STD_Segment_l_carpal_distal_phalanx_2"
HAnimSegment848.name = "l_carpal_distal_phalanx_2"
Transform849 = x3d.Transform()
Transform849.translation = [0.2028,0.7139,-0.0236]
Shape850 = x3d.Shape()
Shape850.USE = "HAnimJointShape"

Transform849.children.append(Shape850)

HAnimSegment848.children.append(Transform849)
Transform851 = x3d.Transform()
Shape852 = x3d.Shape()
LineSet853 = x3d.LineSet()
LineSet853.vertexCount = [2]
Coordinate854 = x3d.Coordinate()

LineSet853.coord = Coordinate854
ColorRGBA855 = x3d.ColorRGBA()
ColorRGBA855.USE = "HAnimSegmentLineColorRGBA"

LineSet853.color = ColorRGBA855

Shape852.geometry = LineSet853

Transform851.children.append(Shape852)

HAnimSegment848.children.append(Transform851)
HAnimSite856 = x3d.HAnimSite()
HAnimSite856.DEF = "STD_Site_l_carpal_distal_phalanx_2_tip"
HAnimSite856.name = "l_carpal_distal_phalanx_2_tip"
TouchSensor857 = x3d.TouchSensor()
TouchSensor857.description = "HAnimSite l_carpal_distal_phalanx_2_tip"

HAnimSite856.children.append(TouchSensor857)
Shape858 = x3d.Shape()
Shape858.USE = "HAnimSiteShape"

HAnimSite856.children.append(Shape858)

HAnimSegment848.children.append(HAnimSite856)
HAnimSite859 = x3d.HAnimSite()
HAnimSite859.DEF = "STD_Site_l_dactylion_pt"
HAnimSite859.name = "l_dactylion_pt"
HAnimSite859.translation = [0.2056,0.6743,-0.0482]
TouchSensor860 = x3d.TouchSensor()
TouchSensor860.description = "HAnimSite l_dactylion_pt"

HAnimSite859.children.append(TouchSensor860)
Shape861 = x3d.Shape()
Shape861.USE = "HAnimSiteShape"

HAnimSite859.children.append(Shape861)

HAnimSegment848.children.append(HAnimSite859)

HAnimJoint847.children.append(HAnimSegment848)

HAnimJoint838.children.append(HAnimJoint847)

HAnimJoint829.children.append(HAnimJoint838)

HAnimJoint817.children.append(HAnimJoint829)

HAnimJoint815.children.append(HAnimJoint817)

HAnimJoint766.children.append(HAnimJoint815)
HAnimJoint862 = x3d.HAnimJoint()
HAnimJoint862.DEF = "STD_Joint_l_midcarpal_3"
HAnimJoint862.name = "l_midcarpal_3"
HAnimSegment863 = x3d.HAnimSegment()
HAnimSegment863.DEF = "STD_Segment_l_capitate"
HAnimSegment863.name = "l_capitate"

HAnimJoint862.children.append(HAnimSegment863)
HAnimJoint864 = x3d.HAnimJoint()
HAnimJoint864.DEF = "STD_Joint_l_carpometacarpal_3"
HAnimJoint864.name = "l_carpometacarpal_3"
HAnimJoint864.center = [0.1987,0.8029,-0.0530]
HAnimSegment865 = x3d.HAnimSegment()
HAnimSegment865.DEF = "STD_Segment_l_metacarpal_3"
HAnimSegment865.name = "l_metacarpal_3"
Transform866 = x3d.Transform()
Transform866.translation = [0.1987,0.8029,-0.0530]
Shape867 = x3d.Shape()
Shape867.USE = "HAnimJointShape"

Transform866.children.append(Shape867)

HAnimSegment865.children.append(Transform866)
Transform868 = x3d.Transform()
Shape869 = x3d.Shape()
LineSet870 = x3d.LineSet()
LineSet870.vertexCount = [2]
Coordinate871 = x3d.Coordinate()

LineSet870.coord = Coordinate871
ColorRGBA872 = x3d.ColorRGBA()
ColorRGBA872.USE = "HAnimSegmentLineColorRGBA"

LineSet870.color = ColorRGBA872

Shape869.geometry = LineSet870

Transform868.children.append(Shape869)

HAnimSegment865.children.append(Transform868)
HAnimSite873 = x3d.HAnimSite()
HAnimSite873.DEF = "STD_Site_l_metacarpal_phalanx_3_pt"
HAnimSite873.name = "l_metacarpal_phalanx_3_pt"
TouchSensor874 = x3d.TouchSensor()
TouchSensor874.description = "HAnimSite l_metacarpal_phalanx_3_pt"

HAnimSite873.children.append(TouchSensor874)
Shape875 = x3d.Shape()
Shape875.USE = "HAnimSiteShape"

HAnimSite873.children.append(Shape875)

HAnimSegment865.children.append(HAnimSite873)

HAnimJoint864.children.append(HAnimSegment865)
HAnimJoint876 = x3d.HAnimJoint()
HAnimJoint876.DEF = "STD_Joint_l_metacarpophalangeal_3"
HAnimJoint876.name = "l_metacarpophalangeal_3"
HAnimJoint876.center = [0.1987,0.7818,-0.0530]
HAnimSegment877 = x3d.HAnimSegment()
HAnimSegment877.DEF = "STD_Segment_l_carpal_proximal_phalanx_3"
HAnimSegment877.name = "l_carpal_proximal_phalanx_3"
Transform878 = x3d.Transform()
Transform878.translation = [0.1987,0.7818,-0.0530]
Shape879 = x3d.Shape()
Shape879.USE = "HAnimJointShape"

Transform878.children.append(Shape879)

HAnimSegment877.children.append(Transform878)
Transform880 = x3d.Transform()
Shape881 = x3d.Shape()
LineSet882 = x3d.LineSet()
LineSet882.vertexCount = [2]
Coordinate883 = x3d.Coordinate()

LineSet882.coord = Coordinate883
ColorRGBA884 = x3d.ColorRGBA()
ColorRGBA884.USE = "HAnimSegmentLineColorRGBA"

LineSet882.color = ColorRGBA884

Shape881.geometry = LineSet882

Transform880.children.append(Shape881)

HAnimSegment877.children.append(Transform880)

HAnimJoint876.children.append(HAnimSegment877)
HAnimJoint885 = x3d.HAnimJoint()
HAnimJoint885.DEF = "STD_Joint_l_carpal_proximal_interphalangeal_3"
HAnimJoint885.name = "l_carpal_proximal_interphalangeal_3"
HAnimJoint885.center = [0.2013,0.7273,-0.0503]
HAnimSegment886 = x3d.HAnimSegment()
HAnimSegment886.DEF = "STD_Segment_l_carpal_middle_phalanx_3"
HAnimSegment886.name = "l_carpal_middle_phalanx_3"
Transform887 = x3d.Transform()
Transform887.translation = [0.2013,0.7273,-0.0503]
Shape888 = x3d.Shape()
Shape888.USE = "HAnimJointShape"

Transform887.children.append(Shape888)

HAnimSegment886.children.append(Transform887)
Transform889 = x3d.Transform()
Shape890 = x3d.Shape()
LineSet891 = x3d.LineSet()
LineSet891.vertexCount = [2]
Coordinate892 = x3d.Coordinate()

LineSet891.coord = Coordinate892
ColorRGBA893 = x3d.ColorRGBA()
ColorRGBA893.USE = "HAnimSegmentLineColorRGBA"

LineSet891.color = ColorRGBA893

Shape890.geometry = LineSet891

Transform889.children.append(Shape890)

HAnimSegment886.children.append(Transform889)

HAnimJoint885.children.append(HAnimSegment886)
HAnimJoint894 = x3d.HAnimJoint()
HAnimJoint894.DEF = "STD_Joint_l_carpal_distal_interphalangeal_3"
HAnimJoint894.name = "l_carpal_distal_interphalangeal_3"
HAnimJoint894.center = [0.2026,0.7011,-0.0494]
HAnimSegment895 = x3d.HAnimSegment()
HAnimSegment895.DEF = "STD_Segment_l_carpal_distal_phalanx_3"
HAnimSegment895.name = "l_carpal_distal_phalanx_3"
Transform896 = x3d.Transform()
Transform896.translation = [0.2026,0.7011,-0.0494]
Shape897 = x3d.Shape()
Shape897.USE = "HAnimJointShape"

Transform896.children.append(Shape897)

HAnimSegment895.children.append(Transform896)
Transform898 = x3d.Transform()
Shape899 = x3d.Shape()
LineSet900 = x3d.LineSet()
LineSet900.vertexCount = [2]
Coordinate901 = x3d.Coordinate()

LineSet900.coord = Coordinate901
ColorRGBA902 = x3d.ColorRGBA()
ColorRGBA902.USE = "HAnimSegmentLineColorRGBA"

LineSet900.color = ColorRGBA902

Shape899.geometry = LineSet900

Transform898.children.append(Shape899)

HAnimSegment895.children.append(Transform898)
HAnimSite903 = x3d.HAnimSite()
HAnimSite903.DEF = "STD_Site_l_carpal_distal_phalanx_3_tip"
HAnimSite903.name = "l_carpal_distal_phalanx_3_tip"
TouchSensor904 = x3d.TouchSensor()
TouchSensor904.description = "HAnimSite l_carpal_distal_phalanx_3_tip"

HAnimSite903.children.append(TouchSensor904)
Shape905 = x3d.Shape()
Shape905.USE = "HAnimSiteShape"

HAnimSite903.children.append(Shape905)

HAnimSegment895.children.append(HAnimSite903)

HAnimJoint894.children.append(HAnimSegment895)

HAnimJoint885.children.append(HAnimJoint894)

HAnimJoint876.children.append(HAnimJoint885)

HAnimJoint864.children.append(HAnimJoint876)

HAnimJoint862.children.append(HAnimJoint864)

HAnimJoint766.children.append(HAnimJoint862)
HAnimJoint906 = x3d.HAnimJoint()
HAnimJoint906.DEF = "STD_Joint_l_midcarpal_4_5"
HAnimJoint906.name = "l_midcarpal_4_5"
HAnimSegment907 = x3d.HAnimSegment()
HAnimSegment907.DEF = "STD_Segment_l_hamate"
HAnimSegment907.name = "l_hamate"

HAnimJoint906.children.append(HAnimSegment907)
HAnimJoint908 = x3d.HAnimJoint()
HAnimJoint908.DEF = "STD_Joint_l_carpometacarpal_4"
HAnimJoint908.name = "l_carpometacarpal_4"
HAnimJoint908.center = [0.1956,0.8019,-0.0794]
HAnimSegment909 = x3d.HAnimSegment()
HAnimSegment909.DEF = "STD_Segment_l_metacarpal_4"
HAnimSegment909.name = "l_metacarpal_4"
Transform910 = x3d.Transform()
Transform910.translation = [0.1956,0.8019,-0.0794]
Shape911 = x3d.Shape()
Shape911.USE = "HAnimJointShape"

Transform910.children.append(Shape911)

HAnimSegment909.children.append(Transform910)
Transform912 = x3d.Transform()
Shape913 = x3d.Shape()
LineSet914 = x3d.LineSet()
LineSet914.vertexCount = [2]
Coordinate915 = x3d.Coordinate()

LineSet914.coord = Coordinate915
ColorRGBA916 = x3d.ColorRGBA()
ColorRGBA916.USE = "HAnimSegmentLineColorRGBA"

LineSet914.color = ColorRGBA916

Shape913.geometry = LineSet914

Transform912.children.append(Shape913)

HAnimSegment909.children.append(Transform912)

HAnimJoint908.children.append(HAnimSegment909)
HAnimJoint917 = x3d.HAnimJoint()
HAnimJoint917.DEF = "STD_Joint_l_metacarpophalangeal_4"
HAnimJoint917.name = "l_metacarpophalangeal_4"
HAnimJoint917.center = [0.1956,0.7815,-0.0794]
HAnimSegment918 = x3d.HAnimSegment()
HAnimSegment918.DEF = "STD_Segment_l_carpal_proximal_phalanx_4"
HAnimSegment918.name = "l_carpal_proximal_phalanx_4"
Transform919 = x3d.Transform()
Transform919.translation = [0.1956,0.7815,-0.0794]
Shape920 = x3d.Shape()
Shape920.USE = "HAnimJointShape"

Transform919.children.append(Shape920)

HAnimSegment918.children.append(Transform919)
Transform921 = x3d.Transform()
Shape922 = x3d.Shape()
LineSet923 = x3d.LineSet()
LineSet923.vertexCount = [2]
Coordinate924 = x3d.Coordinate()

LineSet923.coord = Coordinate924
ColorRGBA925 = x3d.ColorRGBA()
ColorRGBA925.USE = "HAnimSegmentLineColorRGBA"

LineSet923.color = ColorRGBA925

Shape922.geometry = LineSet923

Transform921.children.append(Shape922)

HAnimSegment918.children.append(Transform921)

HAnimJoint917.children.append(HAnimSegment918)
HAnimJoint926 = x3d.HAnimJoint()
HAnimJoint926.DEF = "STD_Joint_l_carpal_proximal_interphalangeal_4"
HAnimJoint926.name = "l_carpal_proximal_interphalangeal_4"
HAnimJoint926.center = [0.1973,0.7287,-0.0777]
HAnimSegment927 = x3d.HAnimSegment()
HAnimSegment927.DEF = "STD_Segment_l_carpal_middle_phalanx_4"
HAnimSegment927.name = "l_carpal_middle_phalanx_4"
Transform928 = x3d.Transform()
Transform928.translation = [0.1973,0.7287,-0.0777]
Shape929 = x3d.Shape()
Shape929.USE = "HAnimJointShape"

Transform928.children.append(Shape929)

HAnimSegment927.children.append(Transform928)
Transform930 = x3d.Transform()
Shape931 = x3d.Shape()
LineSet932 = x3d.LineSet()
LineSet932.vertexCount = [2]
Coordinate933 = x3d.Coordinate()

LineSet932.coord = Coordinate933
ColorRGBA934 = x3d.ColorRGBA()
ColorRGBA934.USE = "HAnimSegmentLineColorRGBA"

LineSet932.color = ColorRGBA934

Shape931.geometry = LineSet932

Transform930.children.append(Shape931)

HAnimSegment927.children.append(Transform930)

HAnimJoint926.children.append(HAnimSegment927)
HAnimJoint935 = x3d.HAnimJoint()
HAnimJoint935.DEF = "STD_Joint_l_carpal_distal_interphalangeal_4"
HAnimJoint935.name = "l_carpal_distal_interphalangeal_4"
HAnimJoint935.center = [0.1983,0.7045,-0.0767]
HAnimSegment936 = x3d.HAnimSegment()
HAnimSegment936.DEF = "STD_Segment_l_carpal_distal_phalanx_4"
HAnimSegment936.name = "l_carpal_distal_phalanx_4"
Transform937 = x3d.Transform()
Transform937.translation = [0.1983,0.7045,-0.0767]
Shape938 = x3d.Shape()
Shape938.USE = "HAnimJointShape"

Transform937.children.append(Shape938)

HAnimSegment936.children.append(Transform937)
Transform939 = x3d.Transform()
Shape940 = x3d.Shape()
LineSet941 = x3d.LineSet()
LineSet941.vertexCount = [2]
Coordinate942 = x3d.Coordinate()

LineSet941.coord = Coordinate942
ColorRGBA943 = x3d.ColorRGBA()
ColorRGBA943.USE = "HAnimSegmentLineColorRGBA"

LineSet941.color = ColorRGBA943

Shape940.geometry = LineSet941

Transform939.children.append(Shape940)

HAnimSegment936.children.append(Transform939)
HAnimSite944 = x3d.HAnimSite()
HAnimSite944.DEF = "STD_Site_l_carpal_distal_phalanx_4_tip"
HAnimSite944.name = "l_carpal_distal_phalanx_4_tip"
TouchSensor945 = x3d.TouchSensor()
TouchSensor945.description = "HAnimSite l_carpal_distal_phalanx_4_tip"

HAnimSite944.children.append(TouchSensor945)
Shape946 = x3d.Shape()
Shape946.USE = "HAnimSiteShape"

HAnimSite944.children.append(Shape946)

HAnimSegment936.children.append(HAnimSite944)

HAnimJoint935.children.append(HAnimSegment936)

HAnimJoint926.children.append(HAnimJoint935)

HAnimJoint917.children.append(HAnimJoint926)

HAnimJoint908.children.append(HAnimJoint917)

HAnimJoint906.children.append(HAnimJoint908)
HAnimJoint947 = x3d.HAnimJoint()
HAnimJoint947.DEF = "STD_Joint_l_carpometacarpal_5"
HAnimJoint947.name = "l_carpometacarpal_5"
HAnimJoint947.center = [0.1925,0.8066,-0.1036]
HAnimSegment948 = x3d.HAnimSegment()
HAnimSegment948.DEF = "STD_Segment_l_metacarpal_5"
HAnimSegment948.name = "l_metacarpal_5"
Transform949 = x3d.Transform()
Transform949.translation = [0.1925,0.8066,-0.1036]
Shape950 = x3d.Shape()
Shape950.USE = "HAnimJointShape"

Transform949.children.append(Shape950)

HAnimSegment948.children.append(Transform949)
Transform951 = x3d.Transform()
Shape952 = x3d.Shape()
LineSet953 = x3d.LineSet()
LineSet953.vertexCount = [2]
Coordinate954 = x3d.Coordinate()

LineSet953.coord = Coordinate954
ColorRGBA955 = x3d.ColorRGBA()
ColorRGBA955.USE = "HAnimSegmentLineColorRGBA"

LineSet953.color = ColorRGBA955

Shape952.geometry = LineSet953

Transform951.children.append(Shape952)

HAnimSegment948.children.append(Transform951)
HAnimSite956 = x3d.HAnimSite()
HAnimSite956.DEF = "STD_Site_l_metacarpal_phalanx_5_pt"
HAnimSite956.name = "l_metacarpal_phalanx_5_pt"
HAnimSite956.translation = [0.1929,0.7860,-0.1122]
TouchSensor957 = x3d.TouchSensor()
TouchSensor957.description = "HAnimSite l_metacarpal_phalanx_5_pt"

HAnimSite956.children.append(TouchSensor957)
Shape958 = x3d.Shape()
Shape958.USE = "HAnimSiteShape"

HAnimSite956.children.append(Shape958)

HAnimSegment948.children.append(HAnimSite956)

HAnimJoint947.children.append(HAnimSegment948)
HAnimJoint959 = x3d.HAnimJoint()
HAnimJoint959.DEF = "STD_Joint_l_metacarpophalangeal_5"
HAnimJoint959.name = "l_metacarpophalangeal_5"
HAnimJoint959.center = [0.1925,0.7866,-0.1036]
HAnimSegment960 = x3d.HAnimSegment()
HAnimSegment960.DEF = "STD_Segment_l_carpal_proximal_phalanx_5"
HAnimSegment960.name = "l_carpal_proximal_phalanx_5"
Transform961 = x3d.Transform()
Transform961.translation = [0.1925,0.7866,-0.1036]
Shape962 = x3d.Shape()
Shape962.USE = "HAnimJointShape"

Transform961.children.append(Shape962)

HAnimSegment960.children.append(Transform961)
Transform963 = x3d.Transform()
Shape964 = x3d.Shape()
LineSet965 = x3d.LineSet()
LineSet965.vertexCount = [2]
Coordinate966 = x3d.Coordinate()

LineSet965.coord = Coordinate966
ColorRGBA967 = x3d.ColorRGBA()
ColorRGBA967.USE = "HAnimSegmentLineColorRGBA"

LineSet965.color = ColorRGBA967

Shape964.geometry = LineSet965

Transform963.children.append(Shape964)

HAnimSegment960.children.append(Transform963)

HAnimJoint959.children.append(HAnimSegment960)
HAnimJoint968 = x3d.HAnimJoint()
HAnimJoint968.DEF = "STD_Joint_l_carpal_proximal_interphalangeal_5"
HAnimJoint968.name = "l_carpal_proximal_interphalangeal_5"
HAnimJoint968.center = [0.1938,0.7452,-0.1024]
HAnimSegment969 = x3d.HAnimSegment()
HAnimSegment969.DEF = "STD_Segment_l_carpal_middle_phalanx_5"
HAnimSegment969.name = "l_carpal_middle_phalanx_5"
Transform970 = x3d.Transform()
Transform970.translation = [0.1938,0.7452,-0.1024]
Shape971 = x3d.Shape()
Shape971.USE = "HAnimJointShape"

Transform970.children.append(Shape971)

HAnimSegment969.children.append(Transform970)
Transform972 = x3d.Transform()
Shape973 = x3d.Shape()
LineSet974 = x3d.LineSet()
LineSet974.vertexCount = [2]
Coordinate975 = x3d.Coordinate()

LineSet974.coord = Coordinate975
ColorRGBA976 = x3d.ColorRGBA()
ColorRGBA976.USE = "HAnimSegmentLineColorRGBA"

LineSet974.color = ColorRGBA976

Shape973.geometry = LineSet974

Transform972.children.append(Shape973)

HAnimSegment969.children.append(Transform972)

HAnimJoint968.children.append(HAnimSegment969)
HAnimJoint977 = x3d.HAnimJoint()
HAnimJoint977.DEF = "STD_Joint_l_carpal_distal_interphalangeal_5"
HAnimJoint977.name = "l_carpal_distal_interphalangeal_5"
HAnimJoint977.center = [0.1948,0.7277,-0.1017]
HAnimSegment978 = x3d.HAnimSegment()
HAnimSegment978.DEF = "STD_Segment_l_carpal_distal_phalanx_5"
HAnimSegment978.name = "l_carpal_distal_phalanx_5"
Transform979 = x3d.Transform()
Transform979.translation = [0.1948,0.7277,-0.1017]
Shape980 = x3d.Shape()
Shape980.USE = "HAnimJointShape"

Transform979.children.append(Shape980)

HAnimSegment978.children.append(Transform979)
Transform981 = x3d.Transform()
Shape982 = x3d.Shape()
LineSet983 = x3d.LineSet()
LineSet983.vertexCount = [2]
Coordinate984 = x3d.Coordinate()

LineSet983.coord = Coordinate984
ColorRGBA985 = x3d.ColorRGBA()
ColorRGBA985.USE = "HAnimSegmentLineColorRGBA"

LineSet983.color = ColorRGBA985

Shape982.geometry = LineSet983

Transform981.children.append(Shape982)

HAnimSegment978.children.append(Transform981)
HAnimSite986 = x3d.HAnimSite()
HAnimSite986.DEF = "STD_Site_l_carpal_distal_phalanx_5_tip"
HAnimSite986.name = "l_carpal_distal_phalanx_5_tip"
TouchSensor987 = x3d.TouchSensor()
TouchSensor987.description = "HAnimSite l_carpal_distal_phalanx_5_tip"

HAnimSite986.children.append(TouchSensor987)
Shape988 = x3d.Shape()
Shape988.USE = "HAnimSiteShape"

HAnimSite986.children.append(Shape988)

HAnimSegment978.children.append(HAnimSite986)

HAnimJoint977.children.append(HAnimSegment978)

HAnimJoint968.children.append(HAnimJoint977)

HAnimJoint959.children.append(HAnimJoint968)

HAnimJoint947.children.append(HAnimJoint959)

HAnimJoint906.children.append(HAnimJoint947)

HAnimJoint766.children.append(HAnimJoint906)

HAnimJoint745.children.append(HAnimJoint766)

HAnimJoint730.children.append(HAnimJoint745)

HAnimJoint721.children.append(HAnimJoint730)

HAnimJoint697.children.append(HAnimJoint721)

HAnimJoint537.children.append(HAnimJoint697)
HAnimJoint989 = x3d.HAnimJoint()
HAnimJoint989.DEF = "STD_Joint_r_sternoclavicular"
HAnimJoint989.name = "r_sternoclavicular"
HAnimJoint989.center = [-0.0694,1.4600,-0.0330]
HAnimSegment990 = x3d.HAnimSegment()
HAnimSegment990.DEF = "STD_Segment_r_clavicle"
HAnimSegment990.name = "r_clavicle"
Transform991 = x3d.Transform()
Transform991.translation = [-0.0694,1.4600,-0.0330]
Shape992 = x3d.Shape()
Shape992.USE = "HAnimJointShape"

Transform991.children.append(Shape992)

HAnimSegment990.children.append(Transform991)
Transform993 = x3d.Transform()
Shape994 = x3d.Shape()
LineSet995 = x3d.LineSet()
LineSet995.vertexCount = [2]
Coordinate996 = x3d.Coordinate()

LineSet995.coord = Coordinate996
ColorRGBA997 = x3d.ColorRGBA()
ColorRGBA997.USE = "HAnimSegmentLineColorRGBA"

LineSet995.color = ColorRGBA997

Shape994.geometry = LineSet995

Transform993.children.append(Shape994)

HAnimSegment990.children.append(Transform993)
HAnimSite998 = x3d.HAnimSite()
HAnimSite998.DEF = "STD_Site_r_acromion_pt"
HAnimSite998.name = "r_acromion_pt"
HAnimSite998.translation = [-0.1905,1.4791,-0.0431]
TouchSensor999 = x3d.TouchSensor()
TouchSensor999.description = "HAnimSite r_acromion_pt"

HAnimSite998.children.append(TouchSensor999)
Shape1000 = x3d.Shape()
Shape1000.USE = "HAnimSiteShape"

HAnimSite998.children.append(Shape1000)

HAnimSegment990.children.append(HAnimSite998)
HAnimSite1001 = x3d.HAnimSite()
HAnimSite1001.DEF = "STD_Site_r_axilla_distal_pt"
HAnimSite1001.name = "r_axilla_distal_pt"
HAnimSite1001.translation = [-0.1603,1.4098,-0.0826]
TouchSensor1002 = x3d.TouchSensor()
TouchSensor1002.description = "HAnimSite r_axilla_distal_pt"

HAnimSite1001.children.append(TouchSensor1002)
Shape1003 = x3d.Shape()
Shape1003.USE = "HAnimSiteShape"

HAnimSite1001.children.append(Shape1003)

HAnimSegment990.children.append(HAnimSite1001)
HAnimSite1004 = x3d.HAnimSite()
HAnimSite1004.DEF = "STD_Site_r_axilla_posterior_folds_pt"
HAnimSite1004.name = "r_axilla_posterior_folds_pt"
TouchSensor1005 = x3d.TouchSensor()
TouchSensor1005.description = "HAnimSite r_axilla_posterior_folds_pt"

HAnimSite1004.children.append(TouchSensor1005)
Shape1006 = x3d.Shape()
Shape1006.USE = "HAnimSiteShape"

HAnimSite1004.children.append(Shape1006)

HAnimSegment990.children.append(HAnimSite1004)
HAnimSite1007 = x3d.HAnimSite()
HAnimSite1007.DEF = "STD_Site_r_axilla_proximal_pt"
HAnimSite1007.name = "r_axilla_proximal_pt"
HAnimSite1007.translation = [-0.1626,1.4072,-0.0031]
TouchSensor1008 = x3d.TouchSensor()
TouchSensor1008.description = "HAnimSite r_axilla_proximal_pt"

HAnimSite1007.children.append(TouchSensor1008)
Shape1009 = x3d.Shape()
Shape1009.USE = "HAnimSiteShape"

HAnimSite1007.children.append(Shape1009)

HAnimSegment990.children.append(HAnimSite1007)
HAnimSite1010 = x3d.HAnimSite()
HAnimSite1010.DEF = "STD_Site_r_clavicale_pt"
HAnimSite1010.name = "r_clavicale_pt"
HAnimSite1010.translation = [-0.0115,1.4943,0.0400]
TouchSensor1011 = x3d.TouchSensor()
TouchSensor1011.description = "HAnimSite r_clavicale_pt"

HAnimSite1010.children.append(TouchSensor1011)
Shape1012 = x3d.Shape()
Shape1012.USE = "HAnimSiteShape"

HAnimSite1010.children.append(Shape1012)

HAnimSegment990.children.append(HAnimSite1010)

HAnimJoint989.children.append(HAnimSegment990)
HAnimJoint1013 = x3d.HAnimJoint()
HAnimJoint1013.DEF = "STD_Joint_r_acromioclavicular"
HAnimJoint1013.name = "r_acromioclavicular"
HAnimJoint1013.center = [-0.0836,1.4281,-0.0401]
HAnimSegment1014 = x3d.HAnimSegment()
HAnimSegment1014.DEF = "STD_Segment_r_scapula"
HAnimSegment1014.name = "r_scapula"
Transform1015 = x3d.Transform()
Transform1015.translation = [-0.0836,1.4281,-0.0401]
Shape1016 = x3d.Shape()
Shape1016.USE = "HAnimJointShape"

Transform1015.children.append(Shape1016)

HAnimSegment1014.children.append(Transform1015)
Transform1017 = x3d.Transform()
Shape1018 = x3d.Shape()
LineSet1019 = x3d.LineSet()
LineSet1019.vertexCount = [2]
Coordinate1020 = x3d.Coordinate()

LineSet1019.coord = Coordinate1020
ColorRGBA1021 = x3d.ColorRGBA()
ColorRGBA1021.USE = "HAnimSegmentLineColorRGBA"

LineSet1019.color = ColorRGBA1021

Shape1018.geometry = LineSet1019

Transform1017.children.append(Shape1018)

HAnimSegment1014.children.append(Transform1017)

HAnimJoint1013.children.append(HAnimSegment1014)
HAnimJoint1022 = x3d.HAnimJoint()
HAnimJoint1022.DEF = "STD_Joint_r_shoulder"
HAnimJoint1022.name = "r_shoulder"
HAnimJoint1022.center = [-0.1907,1.4407,-0.0325]
HAnimSegment1023 = x3d.HAnimSegment()
HAnimSegment1023.DEF = "STD_Segment_r_upperarm"
HAnimSegment1023.name = "r_upperarm"
Transform1024 = x3d.Transform()
Transform1024.translation = [-0.1907,1.4407,-0.0325]
Shape1025 = x3d.Shape()
Shape1025.USE = "HAnimJointShape"

Transform1024.children.append(Shape1025)

HAnimSegment1023.children.append(Transform1024)
Transform1026 = x3d.Transform()
Shape1027 = x3d.Shape()
LineSet1028 = x3d.LineSet()
LineSet1028.vertexCount = [2]
Coordinate1029 = x3d.Coordinate()

LineSet1028.coord = Coordinate1029
ColorRGBA1030 = x3d.ColorRGBA()
ColorRGBA1030.USE = "HAnimSegmentLineColorRGBA"

LineSet1028.color = ColorRGBA1030

Shape1027.geometry = LineSet1028

Transform1026.children.append(Shape1027)

HAnimSegment1023.children.append(Transform1026)
HAnimSite1031 = x3d.HAnimSite()
HAnimSite1031.DEF = "STD_Site_r_bideltoid_pt"
HAnimSite1031.name = "r_bideltoid_pt"
TouchSensor1032 = x3d.TouchSensor()
TouchSensor1032.description = "HAnimSite r_bideltoid_pt"

HAnimSite1031.children.append(TouchSensor1032)
Shape1033 = x3d.Shape()
Shape1033.USE = "HAnimSiteShape"

HAnimSite1031.children.append(Shape1033)

HAnimSegment1023.children.append(HAnimSite1031)
HAnimSite1034 = x3d.HAnimSite()
HAnimSite1034.DEF = "STD_Site_r_humeral_lateral_epicondyles_pt"
HAnimSite1034.name = "r_humeral_lateral_epicondyles_pt"
HAnimSite1034.translation = [-0.2224,1.1517,-0.1033]
TouchSensor1035 = x3d.TouchSensor()
TouchSensor1035.description = "HAnimSite r_humeral_lateral_epicondyles_pt"

HAnimSite1034.children.append(TouchSensor1035)
Shape1036 = x3d.Shape()
Shape1036.USE = "HAnimSiteShape"

HAnimSite1034.children.append(Shape1036)

HAnimSegment1023.children.append(HAnimSite1034)

HAnimJoint1022.children.append(HAnimSegment1023)
HAnimJoint1037 = x3d.HAnimJoint()
HAnimJoint1037.DEF = "STD_Joint_r_elbow"
HAnimJoint1037.name = "r_elbow"
HAnimJoint1037.center = [-0.1949,1.1388,-0.0620]
HAnimSegment1038 = x3d.HAnimSegment()
HAnimSegment1038.DEF = "STD_Segment_r_forearm"
HAnimSegment1038.name = "r_forearm"
Transform1039 = x3d.Transform()
Transform1039.translation = [-0.1949,1.1388,-0.0620]
Shape1040 = x3d.Shape()
Shape1040.USE = "HAnimJointShape"

Transform1039.children.append(Shape1040)

HAnimSegment1038.children.append(Transform1039)
Transform1041 = x3d.Transform()
Shape1042 = x3d.Shape()
LineSet1043 = x3d.LineSet()
LineSet1043.vertexCount = [2]
Coordinate1044 = x3d.Coordinate()

LineSet1043.coord = Coordinate1044
ColorRGBA1045 = x3d.ColorRGBA()
ColorRGBA1045.USE = "HAnimSegmentLineColorRGBA"

LineSet1043.color = ColorRGBA1045

Shape1042.geometry = LineSet1043

Transform1041.children.append(Shape1042)

HAnimSegment1038.children.append(Transform1041)
HAnimSite1046 = x3d.HAnimSite()
HAnimSite1046.DEF = "STD_Site_r_humeral_medial_epicondyles_pt"
HAnimSite1046.name = "r_humeral_medial_epicondyles_pt"
HAnimSite1046.translation = [-0.1680,1.1298,-0.1062]
TouchSensor1047 = x3d.TouchSensor()
TouchSensor1047.description = "HAnimSite r_humeral_medial_epicondyles_pt"

HAnimSite1046.children.append(TouchSensor1047)
Shape1048 = x3d.Shape()
Shape1048.USE = "HAnimSiteShape"

HAnimSite1046.children.append(Shape1048)

HAnimSegment1038.children.append(HAnimSite1046)
HAnimSite1049 = x3d.HAnimSite()
HAnimSite1049.DEF = "STD_Site_r_olecranon_pt"
HAnimSite1049.name = "r_olecranon_pt"
HAnimSite1049.translation = [-0.1907,1.1405,-0.1065]
TouchSensor1050 = x3d.TouchSensor()
TouchSensor1050.description = "HAnimSite r_olecranon_pt"

HAnimSite1049.children.append(TouchSensor1050)
Shape1051 = x3d.Shape()
Shape1051.USE = "HAnimSiteShape"

HAnimSite1049.children.append(Shape1051)

HAnimSegment1038.children.append(HAnimSite1049)
HAnimSite1052 = x3d.HAnimSite()
HAnimSite1052.DEF = "STD_Site_r_radial_styloid_pt"
HAnimSite1052.name = "r_radial_styloid_pt"
HAnimSite1052.translation = [-0.1884,0.8676,-0.0360]
TouchSensor1053 = x3d.TouchSensor()
TouchSensor1053.description = "HAnimSite r_radial_styloid_pt"

HAnimSite1052.children.append(TouchSensor1053)
Shape1054 = x3d.Shape()
Shape1054.USE = "HAnimSiteShape"

HAnimSite1052.children.append(Shape1054)

HAnimSegment1038.children.append(HAnimSite1052)
HAnimSite1055 = x3d.HAnimSite()
HAnimSite1055.DEF = "STD_Site_r_radiale_pt"
HAnimSite1055.name = "r_radiale_pt"
HAnimSite1055.translation = [-0.2130,1.1305,-0.1091]
TouchSensor1056 = x3d.TouchSensor()
TouchSensor1056.description = "HAnimSite r_radiale_pt"

HAnimSite1055.children.append(TouchSensor1056)
Shape1057 = x3d.Shape()
Shape1057.USE = "HAnimSiteShape"

HAnimSite1055.children.append(Shape1057)

HAnimSegment1038.children.append(HAnimSite1055)

HAnimJoint1037.children.append(HAnimSegment1038)
HAnimJoint1058 = x3d.HAnimJoint()
HAnimJoint1058.DEF = "STD_Joint_r_radiocarpal"
HAnimJoint1058.name = "r_radiocarpal"
HAnimJoint1058.center = [-0.1959,0.8694,-0.0521]
HAnimSegment1059 = x3d.HAnimSegment()
HAnimSegment1059.DEF = "STD_Segment_r_carpal"
HAnimSegment1059.name = "r_carpal"
Transform1060 = x3d.Transform()
Transform1060.translation = [-0.1959,0.8694,-0.0521]
Shape1061 = x3d.Shape()
Shape1061.USE = "HAnimJointShape"

Transform1060.children.append(Shape1061)

HAnimSegment1059.children.append(Transform1060)
Transform1062 = x3d.Transform()
Shape1063 = x3d.Shape()
LineSet1064 = x3d.LineSet()
LineSet1064.vertexCount = [2]
Coordinate1065 = x3d.Coordinate()

LineSet1064.coord = Coordinate1065
ColorRGBA1066 = x3d.ColorRGBA()
ColorRGBA1066.USE = "HAnimSegmentLineColorRGBA"

LineSet1064.color = ColorRGBA1066

Shape1063.geometry = LineSet1064

Transform1062.children.append(Shape1063)

HAnimSegment1059.children.append(Transform1062)
HAnimSite1067 = x3d.HAnimSite()
HAnimSite1067.DEF = "STD_Site_r_ulnar_styloid_pt"
HAnimSite1067.name = "r_ulnar_styloid_pt"
HAnimSite1067.translation = [-0.2117,0.8562,-0.0584]
TouchSensor1068 = x3d.TouchSensor()
TouchSensor1068.description = "HAnimSite r_ulnar_styloid_pt"

HAnimSite1067.children.append(TouchSensor1068)
Shape1069 = x3d.Shape()
Shape1069.USE = "HAnimSiteShape"

HAnimSite1067.children.append(Shape1069)

HAnimSegment1059.children.append(HAnimSite1067)

HAnimJoint1058.children.append(HAnimSegment1059)
HAnimJoint1070 = x3d.HAnimJoint()
HAnimJoint1070.DEF = "STD_Joint_r_midcarpal_1"
HAnimJoint1070.name = "r_midcarpal_1"
HAnimSegment1071 = x3d.HAnimSegment()
HAnimSegment1071.DEF = "STD_Segment_r_trapezium"
HAnimSegment1071.name = "r_trapezium"
Transform1072 = x3d.Transform()
Shape1073 = x3d.Shape()
LineSet1074 = x3d.LineSet()
LineSet1074.vertexCount = [2]
Coordinate1075 = x3d.Coordinate()

LineSet1074.coord = Coordinate1075
ColorRGBA1076 = x3d.ColorRGBA()
ColorRGBA1076.USE = "HAnimSegmentLineColorRGBA"

LineSet1074.color = ColorRGBA1076

Shape1073.geometry = LineSet1074

Transform1072.children.append(Shape1073)

HAnimSegment1071.children.append(Transform1072)

HAnimJoint1070.children.append(HAnimSegment1071)
HAnimJoint1077 = x3d.HAnimJoint()
HAnimJoint1077.DEF = "STD_Joint_r_carpometacarpal_1"
HAnimJoint1077.name = "r_carpometacarpal_1"
HAnimJoint1077.center = [-0.1899,0.8502,-0.0473]
HAnimSegment1078 = x3d.HAnimSegment()
HAnimSegment1078.DEF = "STD_Segment_r_metacarpal_1"
HAnimSegment1078.name = "r_metacarpal_1"
Transform1079 = x3d.Transform()
Transform1079.translation = [-0.1899,0.8502,-0.0473]
Shape1080 = x3d.Shape()
Shape1080.USE = "HAnimJointShape"

Transform1079.children.append(Shape1080)

HAnimSegment1078.children.append(Transform1079)
Transform1081 = x3d.Transform()
Shape1082 = x3d.Shape()
LineSet1083 = x3d.LineSet()
LineSet1083.vertexCount = [2]
Coordinate1084 = x3d.Coordinate()

LineSet1083.coord = Coordinate1084
ColorRGBA1085 = x3d.ColorRGBA()
ColorRGBA1085.USE = "HAnimSegmentLineColorRGBA"

LineSet1083.color = ColorRGBA1085

Shape1082.geometry = LineSet1083

Transform1081.children.append(Shape1082)

HAnimSegment1078.children.append(Transform1081)

HAnimJoint1077.children.append(HAnimSegment1078)
HAnimJoint1086 = x3d.HAnimJoint()
HAnimJoint1086.DEF = "STD_Joint_r_metacarpophalangeal_1"
HAnimJoint1086.name = "r_metacarpophalangeal_1"
HAnimJoint1086.center = [-0.1874,0.8256,0.0306]
HAnimSegment1087 = x3d.HAnimSegment()
HAnimSegment1087.DEF = "STD_Segment_r_carpal_proximal_phalanx_1"
HAnimSegment1087.name = "r_carpal_proximal_phalanx_1"
Transform1088 = x3d.Transform()
Transform1088.translation = [-0.1874,0.8256,0.0306]
Shape1089 = x3d.Shape()
Shape1089.USE = "HAnimJointShape"

Transform1088.children.append(Shape1089)

HAnimSegment1087.children.append(Transform1088)
Transform1090 = x3d.Transform()
Shape1091 = x3d.Shape()
LineSet1092 = x3d.LineSet()
LineSet1092.vertexCount = [2]
Coordinate1093 = x3d.Coordinate()

LineSet1092.coord = Coordinate1093
ColorRGBA1094 = x3d.ColorRGBA()
ColorRGBA1094.USE = "HAnimSegmentLineColorRGBA"

LineSet1092.color = ColorRGBA1094

Shape1091.geometry = LineSet1092

Transform1090.children.append(Shape1091)

HAnimSegment1087.children.append(Transform1090)

HAnimJoint1086.children.append(HAnimSegment1087)
HAnimJoint1095 = x3d.HAnimJoint()
HAnimJoint1095.DEF = "STD_Joint_r_carpal_interphalangeal_1"
HAnimJoint1095.name = "r_carpal_interphalangeal_1"
HAnimJoint1095.center = [-0.1864,0.8190,0.0506]
HAnimSegment1096 = x3d.HAnimSegment()
HAnimSegment1096.DEF = "STD_Segment_r_carpal_distal_phalanx_1"
HAnimSegment1096.name = "r_carpal_distal_phalanx_1"
Transform1097 = x3d.Transform()
Transform1097.translation = [-0.1864,0.8190,0.0506]
Shape1098 = x3d.Shape()
Shape1098.USE = "HAnimJointShape"

Transform1097.children.append(Shape1098)

HAnimSegment1096.children.append(Transform1097)
Transform1099 = x3d.Transform()
Shape1100 = x3d.Shape()
LineSet1101 = x3d.LineSet()
LineSet1101.vertexCount = [2]
Coordinate1102 = x3d.Coordinate()

LineSet1101.coord = Coordinate1102
ColorRGBA1103 = x3d.ColorRGBA()
ColorRGBA1103.USE = "HAnimSegmentLineColorRGBA"

LineSet1101.color = ColorRGBA1103

Shape1100.geometry = LineSet1101

Transform1099.children.append(Shape1100)

HAnimSegment1096.children.append(Transform1099)
HAnimSite1104 = x3d.HAnimSite()
HAnimSite1104.DEF = "STD_Site_r_carpal_distal_phalanx_1_tip"
HAnimSite1104.name = "r_carpal_distal_phalanx_1_tip"
TouchSensor1105 = x3d.TouchSensor()
TouchSensor1105.description = "HAnimSite r_carpal_distal_phalanx_1_tip"

HAnimSite1104.children.append(TouchSensor1105)
Shape1106 = x3d.Shape()
Shape1106.USE = "HAnimSiteShape"

HAnimSite1104.children.append(Shape1106)

HAnimSegment1096.children.append(HAnimSite1104)

HAnimJoint1095.children.append(HAnimSegment1096)

HAnimJoint1086.children.append(HAnimJoint1095)

HAnimJoint1077.children.append(HAnimJoint1086)

HAnimJoint1070.children.append(HAnimJoint1077)

HAnimJoint1058.children.append(HAnimJoint1070)
HAnimJoint1107 = x3d.HAnimJoint()
HAnimJoint1107.DEF = "STD_Joint_r_midcarpal_2"
HAnimJoint1107.name = "r_midcarpal_2"
HAnimSegment1108 = x3d.HAnimSegment()
HAnimSegment1108.DEF = "STD_Segment_r_trapezoid"
HAnimSegment1108.name = "r_trapezoid"

HAnimJoint1107.children.append(HAnimSegment1108)
HAnimJoint1109 = x3d.HAnimJoint()
HAnimJoint1109.DEF = "STD_Joint_r_carpometacarpal_2"
HAnimJoint1109.name = "r_carpometacarpal_2"
HAnimJoint1109.center = [-0.1961,0.8055,-0.0218]
HAnimSegment1110 = x3d.HAnimSegment()
HAnimSegment1110.DEF = "STD_Segment_r_metacarpal_2"
HAnimSegment1110.name = "r_metacarpal_2"
Transform1111 = x3d.Transform()
Transform1111.translation = [-0.1961,0.8055,-0.0218]
Shape1112 = x3d.Shape()
Shape1112.USE = "HAnimJointShape"

Transform1111.children.append(Shape1112)

HAnimSegment1110.children.append(Transform1111)
Transform1113 = x3d.Transform()
Shape1114 = x3d.Shape()
LineSet1115 = x3d.LineSet()
LineSet1115.vertexCount = [2]
Coordinate1116 = x3d.Coordinate()

LineSet1115.coord = Coordinate1116
ColorRGBA1117 = x3d.ColorRGBA()
ColorRGBA1117.USE = "HAnimSegmentLineColorRGBA"

LineSet1115.color = ColorRGBA1117

Shape1114.geometry = LineSet1115

Transform1113.children.append(Shape1114)

HAnimSegment1110.children.append(Transform1113)
HAnimSite1118 = x3d.HAnimSite()
HAnimSite1118.DEF = "STD_Site_r_metacarpal_phalanx_2_pt"
HAnimSite1118.name = "r_metacarpal_phalanx_2_pt"
HAnimSite1118.translation = [-0.1977,0.8169,-0.0177]
TouchSensor1119 = x3d.TouchSensor()
TouchSensor1119.description = "HAnimSite r_metacarpal_phalanx_2_pt"

HAnimSite1118.children.append(TouchSensor1119)
Shape1120 = x3d.Shape()
Shape1120.USE = "HAnimSiteShape"

HAnimSite1118.children.append(Shape1120)

HAnimSegment1110.children.append(HAnimSite1118)

HAnimJoint1109.children.append(HAnimSegment1110)
HAnimJoint1121 = x3d.HAnimJoint()
HAnimJoint1121.DEF = "STD_Joint_r_metacarpophalangeal_2"
HAnimJoint1121.name = "r_metacarpophalangeal_2"
HAnimJoint1121.center = [-0.1961,0.7846,-0.0218]
HAnimSegment1122 = x3d.HAnimSegment()
HAnimSegment1122.DEF = "STD_Segment_r_carpal_proximal_phalanx_2 "
HAnimSegment1122.name = "r_carpal_proximal_phalanx_2 "
Transform1123 = x3d.Transform()
Transform1123.translation = [-0.1961,0.7846,-0.0218]
Shape1124 = x3d.Shape()
Shape1124.USE = "HAnimJointShape"

Transform1123.children.append(Shape1124)

HAnimSegment1122.children.append(Transform1123)
Transform1125 = x3d.Transform()
Shape1126 = x3d.Shape()
LineSet1127 = x3d.LineSet()
LineSet1127.vertexCount = [2]
Coordinate1128 = x3d.Coordinate()

LineSet1127.coord = Coordinate1128
ColorRGBA1129 = x3d.ColorRGBA()
ColorRGBA1129.USE = "HAnimSegmentLineColorRGBA"

LineSet1127.color = ColorRGBA1129

Shape1126.geometry = LineSet1127

Transform1125.children.append(Shape1126)

HAnimSegment1122.children.append(Transform1125)

HAnimJoint1121.children.append(HAnimSegment1122)
HAnimJoint1130 = x3d.HAnimJoint()
HAnimJoint1130.DEF = "STD_Joint_r_carpal_proximal_interphalangeal_2"
HAnimJoint1130.name = "r_carpal_proximal_interphalangeal_2"
HAnimJoint1130.center = [-0.1954,0.7393,-0.0185]
HAnimSegment1131 = x3d.HAnimSegment()
HAnimSegment1131.DEF = "STD_Segment_r_carpal_middle_phalanx_2"
HAnimSegment1131.name = "r_carpal_middle_phalanx_2"
Transform1132 = x3d.Transform()
Transform1132.translation = [-0.1954,0.7393,-0.0185]
Shape1133 = x3d.Shape()
Shape1133.USE = "HAnimJointShape"

Transform1132.children.append(Shape1133)

HAnimSegment1131.children.append(Transform1132)
Transform1134 = x3d.Transform()
Shape1135 = x3d.Shape()
LineSet1136 = x3d.LineSet()
LineSet1136.vertexCount = [2]
Coordinate1137 = x3d.Coordinate()

LineSet1136.coord = Coordinate1137
ColorRGBA1138 = x3d.ColorRGBA()
ColorRGBA1138.USE = "HAnimSegmentLineColorRGBA"

LineSet1136.color = ColorRGBA1138

Shape1135.geometry = LineSet1136

Transform1134.children.append(Shape1135)

HAnimSegment1131.children.append(Transform1134)

HAnimJoint1130.children.append(HAnimSegment1131)
HAnimJoint1139 = x3d.HAnimJoint()
HAnimJoint1139.DEF = "STD_Joint_r_carpal_distal_interphalangeal_2"
HAnimJoint1139.name = "r_carpal_distal_interphalangeal_2"
HAnimJoint1139.center = [-0.1945,0.7169,-0.0173]
HAnimSegment1140 = x3d.HAnimSegment()
HAnimSegment1140.DEF = "STD_Segment_r_carpal_distal_phalanx_2"
HAnimSegment1140.name = "r_carpal_distal_phalanx_2"
Transform1141 = x3d.Transform()
Transform1141.translation = [-0.1945,0.7169,-0.0173]
Shape1142 = x3d.Shape()
Shape1142.USE = "HAnimJointShape"

Transform1141.children.append(Shape1142)

HAnimSegment1140.children.append(Transform1141)
Transform1143 = x3d.Transform()
Shape1144 = x3d.Shape()
LineSet1145 = x3d.LineSet()
LineSet1145.vertexCount = [2]
Coordinate1146 = x3d.Coordinate()

LineSet1145.coord = Coordinate1146
ColorRGBA1147 = x3d.ColorRGBA()
ColorRGBA1147.USE = "HAnimSegmentLineColorRGBA"

LineSet1145.color = ColorRGBA1147

Shape1144.geometry = LineSet1145

Transform1143.children.append(Shape1144)

HAnimSegment1140.children.append(Transform1143)
HAnimSite1148 = x3d.HAnimSite()
HAnimSite1148.DEF = "STD_Site_r_carpal_distal_phalanx_2_tip"
HAnimSite1148.name = "r_carpal_distal_phalanx_2_tip"
TouchSensor1149 = x3d.TouchSensor()
TouchSensor1149.description = "HAnimSite r_carpal_distal_phalanx_2_tip"

HAnimSite1148.children.append(TouchSensor1149)
Shape1150 = x3d.Shape()
Shape1150.USE = "HAnimSiteShape"

HAnimSite1148.children.append(Shape1150)

HAnimSegment1140.children.append(HAnimSite1148)
HAnimSite1151 = x3d.HAnimSite()
HAnimSite1151.DEF = "STD_Site_r_dactylion_pt"
HAnimSite1151.name = "r_dactylion_pt"
HAnimSite1151.translation = [-0.1941,0.6772,-0.0423]
TouchSensor1152 = x3d.TouchSensor()
TouchSensor1152.description = "HAnimSite r_dactylion_pt"

HAnimSite1151.children.append(TouchSensor1152)
Shape1153 = x3d.Shape()
Shape1153.USE = "HAnimSiteShape"

HAnimSite1151.children.append(Shape1153)

HAnimSegment1140.children.append(HAnimSite1151)

HAnimJoint1139.children.append(HAnimSegment1140)

HAnimJoint1130.children.append(HAnimJoint1139)

HAnimJoint1121.children.append(HAnimJoint1130)

HAnimJoint1109.children.append(HAnimJoint1121)

HAnimJoint1107.children.append(HAnimJoint1109)

HAnimJoint1058.children.append(HAnimJoint1107)
HAnimJoint1154 = x3d.HAnimJoint()
HAnimJoint1154.DEF = "STD_Joint_r_midcarpal_3"
HAnimJoint1154.name = "r_midcarpal_3"
HAnimSegment1155 = x3d.HAnimSegment()
HAnimSegment1155.DEF = "STD_Segment_r_capitate"
HAnimSegment1155.name = "r_capitate"

HAnimJoint1154.children.append(HAnimSegment1155)
HAnimJoint1156 = x3d.HAnimJoint()
HAnimJoint1156.DEF = "STD_Joint_r_carpometacarpal_3"
HAnimJoint1156.name = "r_carpometacarpal_3"
HAnimJoint1156.center = [-0.1972,0.8060,-0.0468]
HAnimSegment1157 = x3d.HAnimSegment()
HAnimSegment1157.DEF = "STD_Segment_r_metacarpal_3"
HAnimSegment1157.name = "r_metacarpal_3"
Transform1158 = x3d.Transform()
Transform1158.translation = [-0.1972,0.8060,-0.0468]
Shape1159 = x3d.Shape()
Shape1159.USE = "HAnimJointShape"

Transform1158.children.append(Shape1159)

HAnimSegment1157.children.append(Transform1158)
Transform1160 = x3d.Transform()
Shape1161 = x3d.Shape()
LineSet1162 = x3d.LineSet()
LineSet1162.vertexCount = [2]
Coordinate1163 = x3d.Coordinate()

LineSet1162.coord = Coordinate1163
ColorRGBA1164 = x3d.ColorRGBA()
ColorRGBA1164.USE = "HAnimSegmentLineColorRGBA"

LineSet1162.color = ColorRGBA1164

Shape1161.geometry = LineSet1162

Transform1160.children.append(Shape1161)

HAnimSegment1157.children.append(Transform1160)
HAnimSite1165 = x3d.HAnimSite()
HAnimSite1165.DEF = "STD_Site_r_metacarpal_phalanx_3_pt"
HAnimSite1165.name = "r_metacarpal_phalanx_3_pt"
TouchSensor1166 = x3d.TouchSensor()
TouchSensor1166.description = "HAnimSite r_metacarpal_phalanx_3_pt"

HAnimSite1165.children.append(TouchSensor1166)
Shape1167 = x3d.Shape()
Shape1167.USE = "HAnimSiteShape"

HAnimSite1165.children.append(Shape1167)

HAnimSegment1157.children.append(HAnimSite1165)

HAnimJoint1156.children.append(HAnimSegment1157)
HAnimJoint1168 = x3d.HAnimJoint()
HAnimJoint1168.DEF = "STD_Joint_r_metacarpophalangeal_3"
HAnimJoint1168.name = "r_metacarpophalangeal_3"
HAnimJoint1168.center = [-0.1972,0.7849,-0.0468]
HAnimSegment1169 = x3d.HAnimSegment()
HAnimSegment1169.DEF = "STD_Segment_r_carpal_proximal_phalanx_3"
HAnimSegment1169.name = "r_carpal_proximal_phalanx_3"
Transform1170 = x3d.Transform()
Transform1170.translation = [-0.1972,0.7849,-0.0468]
Shape1171 = x3d.Shape()
Shape1171.USE = "HAnimJointShape"

Transform1170.children.append(Shape1171)

HAnimSegment1169.children.append(Transform1170)
Transform1172 = x3d.Transform()
Shape1173 = x3d.Shape()
LineSet1174 = x3d.LineSet()
LineSet1174.vertexCount = [2]
Coordinate1175 = x3d.Coordinate()

LineSet1174.coord = Coordinate1175
ColorRGBA1176 = x3d.ColorRGBA()
ColorRGBA1176.USE = "HAnimSegmentLineColorRGBA"

LineSet1174.color = ColorRGBA1176

Shape1173.geometry = LineSet1174

Transform1172.children.append(Shape1173)

HAnimSegment1169.children.append(Transform1172)

HAnimJoint1168.children.append(HAnimSegment1169)
HAnimJoint1177 = x3d.HAnimJoint()
HAnimJoint1177.DEF = "STD_Joint_r_carpal_proximal_interphalangeal_3"
HAnimJoint1177.name = "r_carpal_proximal_interphalangeal_3"
HAnimJoint1177.center = [-0.1950,0.7304,-0.0441]
HAnimSegment1178 = x3d.HAnimSegment()
HAnimSegment1178.DEF = "STD_Segment_r_carpal_middle_phalanx_3"
HAnimSegment1178.name = "r_carpal_middle_phalanx_3"
Transform1179 = x3d.Transform()
Transform1179.translation = [-0.1950,0.7304,-0.0441]
Shape1180 = x3d.Shape()
Shape1180.USE = "HAnimJointShape"

Transform1179.children.append(Shape1180)

HAnimSegment1178.children.append(Transform1179)
Transform1181 = x3d.Transform()
Shape1182 = x3d.Shape()
LineSet1183 = x3d.LineSet()
LineSet1183.vertexCount = [2]
Coordinate1184 = x3d.Coordinate()

LineSet1183.coord = Coordinate1184
ColorRGBA1185 = x3d.ColorRGBA()
ColorRGBA1185.USE = "HAnimSegmentLineColorRGBA"

LineSet1183.color = ColorRGBA1185

Shape1182.geometry = LineSet1183

Transform1181.children.append(Shape1182)

HAnimSegment1178.children.append(Transform1181)

HAnimJoint1177.children.append(HAnimSegment1178)
HAnimJoint1186 = x3d.HAnimJoint()
HAnimJoint1186.DEF = "STD_Joint_r_carpal_distal_interphalangeal_3"
HAnimJoint1186.name = "r_carpal_distal_interphalangeal_3"
HAnimJoint1186.center = [-0.1939,0.7042,-0.0432]
HAnimSegment1187 = x3d.HAnimSegment()
HAnimSegment1187.DEF = "STD_Segment_r_carpal_distal_phalanx_3"
HAnimSegment1187.name = "r_carpal_distal_phalanx_3"
Transform1188 = x3d.Transform()
Transform1188.translation = [-0.1939,0.7042,-0.0432]
Shape1189 = x3d.Shape()
Shape1189.USE = "HAnimJointShape"

Transform1188.children.append(Shape1189)

HAnimSegment1187.children.append(Transform1188)
Transform1190 = x3d.Transform()
Shape1191 = x3d.Shape()
LineSet1192 = x3d.LineSet()
LineSet1192.vertexCount = [2]
Coordinate1193 = x3d.Coordinate()

LineSet1192.coord = Coordinate1193
ColorRGBA1194 = x3d.ColorRGBA()
ColorRGBA1194.USE = "HAnimSegmentLineColorRGBA"

LineSet1192.color = ColorRGBA1194

Shape1191.geometry = LineSet1192

Transform1190.children.append(Shape1191)

HAnimSegment1187.children.append(Transform1190)
HAnimSite1195 = x3d.HAnimSite()
HAnimSite1195.DEF = "STD_Site_r_carpal_distal_phalanx_3_tip"
HAnimSite1195.name = "r_carpal_distal_phalanx_3_tip"
TouchSensor1196 = x3d.TouchSensor()
TouchSensor1196.description = "HAnimSite r_carpal_distal_phalanx_3_tip"

HAnimSite1195.children.append(TouchSensor1196)
Shape1197 = x3d.Shape()
Shape1197.USE = "HAnimSiteShape"

HAnimSite1195.children.append(Shape1197)

HAnimSegment1187.children.append(HAnimSite1195)

HAnimJoint1186.children.append(HAnimSegment1187)

HAnimJoint1177.children.append(HAnimJoint1186)

HAnimJoint1168.children.append(HAnimJoint1177)

HAnimJoint1156.children.append(HAnimJoint1168)

HAnimJoint1154.children.append(HAnimJoint1156)

HAnimJoint1058.children.append(HAnimJoint1154)
HAnimJoint1198 = x3d.HAnimJoint()
HAnimJoint1198.DEF = "STD_Joint_r_midcarpal_4_5"
HAnimJoint1198.name = "r_midcarpal_4_5"
HAnimSegment1199 = x3d.HAnimSegment()
HAnimSegment1199.DEF = "STD_Segment_r_hamate"
HAnimSegment1199.name = "r_hamate"

HAnimJoint1198.children.append(HAnimSegment1199)
HAnimJoint1200 = x3d.HAnimJoint()
HAnimJoint1200.DEF = "STD_Joint_r_carpometacarpal_4"
HAnimJoint1200.name = "r_carpometacarpal_4"
HAnimJoint1200.center = [-0.1951,0.8049,-0.0732]
HAnimSegment1201 = x3d.HAnimSegment()
HAnimSegment1201.DEF = "STD_Segment_r_metacarpal_4"
HAnimSegment1201.name = "r_metacarpal_4"
Transform1202 = x3d.Transform()
Transform1202.translation = [-0.1951,0.8049,-0.0732]
Shape1203 = x3d.Shape()
Shape1203.USE = "HAnimJointShape"

Transform1202.children.append(Shape1203)

HAnimSegment1201.children.append(Transform1202)
Transform1204 = x3d.Transform()
Shape1205 = x3d.Shape()
LineSet1206 = x3d.LineSet()
LineSet1206.vertexCount = [2]
Coordinate1207 = x3d.Coordinate()

LineSet1206.coord = Coordinate1207
ColorRGBA1208 = x3d.ColorRGBA()
ColorRGBA1208.USE = "HAnimSegmentLineColorRGBA"

LineSet1206.color = ColorRGBA1208

Shape1205.geometry = LineSet1206

Transform1204.children.append(Shape1205)

HAnimSegment1201.children.append(Transform1204)

HAnimJoint1200.children.append(HAnimSegment1201)
HAnimJoint1209 = x3d.HAnimJoint()
HAnimJoint1209.DEF = "STD_Joint_r_metacarpophalangeal_4"
HAnimJoint1209.name = "r_metacarpophalangeal_4"
HAnimJoint1209.center = [-0.1951,0.7845,-0.0732]
HAnimSegment1210 = x3d.HAnimSegment()
HAnimSegment1210.DEF = "STD_Segment_r_carpal_proximal_phalanx_4"
HAnimSegment1210.name = "r_carpal_proximal_phalanx_4"
Transform1211 = x3d.Transform()
Transform1211.translation = [-0.1951,0.7845,-0.0732]
Shape1212 = x3d.Shape()
Shape1212.USE = "HAnimJointShape"

Transform1211.children.append(Shape1212)

HAnimSegment1210.children.append(Transform1211)
Transform1213 = x3d.Transform()
Shape1214 = x3d.Shape()
LineSet1215 = x3d.LineSet()
LineSet1215.vertexCount = [2]
Coordinate1216 = x3d.Coordinate()

LineSet1215.coord = Coordinate1216
ColorRGBA1217 = x3d.ColorRGBA()
ColorRGBA1217.USE = "HAnimSegmentLineColorRGBA"

LineSet1215.color = ColorRGBA1217

Shape1214.geometry = LineSet1215

Transform1213.children.append(Shape1214)

HAnimSegment1210.children.append(Transform1213)

HAnimJoint1209.children.append(HAnimSegment1210)
HAnimJoint1218 = x3d.HAnimJoint()
HAnimJoint1218.DEF = "STD_Joint_r_carpal_proximal_interphalangeal_4"
HAnimJoint1218.name = "r_carpal_proximal_interphalangeal_4"
HAnimJoint1218.center = [-0.1920,0.7318,-0.0716]
HAnimSegment1219 = x3d.HAnimSegment()
HAnimSegment1219.DEF = "STD_Segment_r_carpal_middle_phalanx_4"
HAnimSegment1219.name = "r_carpal_middle_phalanx_4"
Transform1220 = x3d.Transform()
Transform1220.translation = [-0.1920,0.7318,-0.0716]
Shape1221 = x3d.Shape()
Shape1221.USE = "HAnimJointShape"

Transform1220.children.append(Shape1221)

HAnimSegment1219.children.append(Transform1220)
Transform1222 = x3d.Transform()
Shape1223 = x3d.Shape()
LineSet1224 = x3d.LineSet()
LineSet1224.vertexCount = [2]
Coordinate1225 = x3d.Coordinate()

LineSet1224.coord = Coordinate1225
ColorRGBA1226 = x3d.ColorRGBA()
ColorRGBA1226.USE = "HAnimSegmentLineColorRGBA"

LineSet1224.color = ColorRGBA1226

Shape1223.geometry = LineSet1224

Transform1222.children.append(Shape1223)

HAnimSegment1219.children.append(Transform1222)

HAnimJoint1218.children.append(HAnimSegment1219)
HAnimJoint1227 = x3d.HAnimJoint()
HAnimJoint1227.DEF = "STD_Joint_r_carpal_distal_interphalangeal_4"
HAnimJoint1227.name = "r_carpal_distal_interphalangeal_4"
HAnimJoint1227.center = [-0.1908,0.7077,-0.0706]
HAnimSegment1228 = x3d.HAnimSegment()
HAnimSegment1228.DEF = "STD_Segment_r_carpal_distal_phalanx_4"
HAnimSegment1228.name = "r_carpal_distal_phalanx_4"
Transform1229 = x3d.Transform()
Transform1229.translation = [-0.1908,0.7077,-0.0706]
Shape1230 = x3d.Shape()
Shape1230.USE = "HAnimJointShape"

Transform1229.children.append(Shape1230)

HAnimSegment1228.children.append(Transform1229)
Transform1231 = x3d.Transform()
Shape1232 = x3d.Shape()
LineSet1233 = x3d.LineSet()
LineSet1233.vertexCount = [2]
Coordinate1234 = x3d.Coordinate()

LineSet1233.coord = Coordinate1234
ColorRGBA1235 = x3d.ColorRGBA()
ColorRGBA1235.USE = "HAnimSegmentLineColorRGBA"

LineSet1233.color = ColorRGBA1235

Shape1232.geometry = LineSet1233

Transform1231.children.append(Shape1232)

HAnimSegment1228.children.append(Transform1231)
HAnimSite1236 = x3d.HAnimSite()
HAnimSite1236.DEF = "STD_Site_r_carpal_distal_phalanx_4_tip"
HAnimSite1236.name = "r_carpal_distal_phalanx_4_tip"
TouchSensor1237 = x3d.TouchSensor()
TouchSensor1237.description = "HAnimSite r_carpal_distal_phalanx_4_tip"

HAnimSite1236.children.append(TouchSensor1237)
Shape1238 = x3d.Shape()
Shape1238.USE = "HAnimSiteShape"

HAnimSite1236.children.append(Shape1238)

HAnimSegment1228.children.append(HAnimSite1236)

HAnimJoint1227.children.append(HAnimSegment1228)

HAnimJoint1218.children.append(HAnimJoint1227)

HAnimJoint1209.children.append(HAnimJoint1218)

HAnimJoint1200.children.append(HAnimJoint1209)

HAnimJoint1198.children.append(HAnimJoint1200)
HAnimJoint1239 = x3d.HAnimJoint()
HAnimJoint1239.DEF = "STD_Joint_r_carpometacarpal_5"
HAnimJoint1239.name = "r_carpometacarpal_5"
HAnimJoint1239.center = [-0.1926,0.8096,-0.0975]
HAnimSegment1240 = x3d.HAnimSegment()
HAnimSegment1240.DEF = "STD_Segment_r_metacarpal_5"
HAnimSegment1240.name = "r_metacarpal_5"
Transform1241 = x3d.Transform()
Transform1241.translation = [-0.1926,0.8096,-0.0975]
Shape1242 = x3d.Shape()
Shape1242.USE = "HAnimJointShape"

Transform1241.children.append(Shape1242)

HAnimSegment1240.children.append(Transform1241)
Transform1243 = x3d.Transform()
Shape1244 = x3d.Shape()
LineSet1245 = x3d.LineSet()
LineSet1245.vertexCount = [2]
Coordinate1246 = x3d.Coordinate()

LineSet1245.coord = Coordinate1246
ColorRGBA1247 = x3d.ColorRGBA()
ColorRGBA1247.USE = "HAnimSegmentLineColorRGBA"

LineSet1245.color = ColorRGBA1247

Shape1244.geometry = LineSet1245

Transform1243.children.append(Shape1244)

HAnimSegment1240.children.append(Transform1243)
HAnimSite1248 = x3d.HAnimSite()
HAnimSite1248.DEF = "STD_Site_r_metacarpal_phalanx_5_pt"
HAnimSite1248.name = "r_metacarpal_phalanx_5_pt"
HAnimSite1248.translation = [-0.1929,0.7890,-0.1064]
TouchSensor1249 = x3d.TouchSensor()
TouchSensor1249.description = "HAnimSite r_metacarpal_phalanx_5_pt"

HAnimSite1248.children.append(TouchSensor1249)
Shape1250 = x3d.Shape()
Shape1250.USE = "HAnimSiteShape"

HAnimSite1248.children.append(Shape1250)

HAnimSegment1240.children.append(HAnimSite1248)

HAnimJoint1239.children.append(HAnimSegment1240)
HAnimJoint1251 = x3d.HAnimJoint()
HAnimJoint1251.DEF = "STD_Joint_r_metacarpophalangeal_5"
HAnimJoint1251.name = "r_metacarpophalangeal_5"
HAnimJoint1251.center = [-0.1926,0.7896,-0.0975]
HAnimSegment1252 = x3d.HAnimSegment()
HAnimSegment1252.DEF = "STD_Segment_r_carpal_proximal_phalanx_5"
HAnimSegment1252.name = "r_carpal_proximal_phalanx_5"
Transform1253 = x3d.Transform()
Transform1253.translation = [-0.1926,0.7896,-0.0975]
Shape1254 = x3d.Shape()
Shape1254.USE = "HAnimJointShape"

Transform1253.children.append(Shape1254)

HAnimSegment1252.children.append(Transform1253)
Transform1255 = x3d.Transform()
Shape1256 = x3d.Shape()
LineSet1257 = x3d.LineSet()
LineSet1257.vertexCount = [2]
Coordinate1258 = x3d.Coordinate()

LineSet1257.coord = Coordinate1258
ColorRGBA1259 = x3d.ColorRGBA()
ColorRGBA1259.USE = "HAnimSegmentLineColorRGBA"

LineSet1257.color = ColorRGBA1259

Shape1256.geometry = LineSet1257

Transform1255.children.append(Shape1256)

HAnimSegment1252.children.append(Transform1255)

HAnimJoint1251.children.append(HAnimSegment1252)
HAnimJoint1260 = x3d.HAnimJoint()
HAnimJoint1260.DEF = "STD_Joint_r_carpal_proximal_interphalangeal_5"
HAnimJoint1260.name = "r_carpal_proximal_interphalangeal_5"
HAnimJoint1260.center = [-0.1902,0.7483,-0.0963]
HAnimSegment1261 = x3d.HAnimSegment()
HAnimSegment1261.DEF = "STD_Segment_r_carpal_middle_phalanx_5"
HAnimSegment1261.name = "r_carpal_middle_phalanx_5"
Transform1262 = x3d.Transform()
Transform1262.translation = [-0.1902,0.7483,-0.0963]
Shape1263 = x3d.Shape()
Shape1263.USE = "HAnimJointShape"

Transform1262.children.append(Shape1263)

HAnimSegment1261.children.append(Transform1262)
Transform1264 = x3d.Transform()
Shape1265 = x3d.Shape()
LineSet1266 = x3d.LineSet()
LineSet1266.vertexCount = [2]
Coordinate1267 = x3d.Coordinate()

LineSet1266.coord = Coordinate1267
ColorRGBA1268 = x3d.ColorRGBA()
ColorRGBA1268.USE = "HAnimSegmentLineColorRGBA"

LineSet1266.color = ColorRGBA1268

Shape1265.geometry = LineSet1266

Transform1264.children.append(Shape1265)

HAnimSegment1261.children.append(Transform1264)

HAnimJoint1260.children.append(HAnimSegment1261)
HAnimJoint1269 = x3d.HAnimJoint()
HAnimJoint1269.DEF = "STD_Joint_r_carpal_distal_interphalangeal_5"
HAnimJoint1269.name = "r_carpal_distal_interphalangeal_5"
HAnimJoint1269.center = [-0.1908,0.7540,-0.0960]
HAnimSegment1270 = x3d.HAnimSegment()
HAnimSegment1270.DEF = "STD_Segment_r_carpal_distal_phalanx_5"
HAnimSegment1270.name = "r_carpal_distal_phalanx_5"
Transform1271 = x3d.Transform()
Transform1271.translation = [-0.1908,0.7540,-0.0960]
Shape1272 = x3d.Shape()
Shape1272.USE = "HAnimJointShape"

Transform1271.children.append(Shape1272)

HAnimSegment1270.children.append(Transform1271)
Transform1273 = x3d.Transform()
Shape1274 = x3d.Shape()
LineSet1275 = x3d.LineSet()
LineSet1275.vertexCount = [2]
Coordinate1276 = x3d.Coordinate()

LineSet1275.coord = Coordinate1276
ColorRGBA1277 = x3d.ColorRGBA()
ColorRGBA1277.USE = "HAnimSegmentLineColorRGBA"

LineSet1275.color = ColorRGBA1277

Shape1274.geometry = LineSet1275

Transform1273.children.append(Shape1274)

HAnimSegment1270.children.append(Transform1273)
HAnimSite1278 = x3d.HAnimSite()
HAnimSite1278.DEF = "STD_Site_r_carpal_distal_phalanx_5_tip"
HAnimSite1278.name = "r_carpal_distal_phalanx_5_tip"
TouchSensor1279 = x3d.TouchSensor()
TouchSensor1279.description = "HAnimSite r_carpal_distal_phalanx_5_tip"

HAnimSite1278.children.append(TouchSensor1279)
Shape1280 = x3d.Shape()
Shape1280.USE = "HAnimSiteShape"

HAnimSite1278.children.append(Shape1280)

HAnimSegment1270.children.append(HAnimSite1278)

HAnimJoint1269.children.append(HAnimSegment1270)

HAnimJoint1260.children.append(HAnimJoint1269)

HAnimJoint1251.children.append(HAnimJoint1260)

HAnimJoint1239.children.append(HAnimJoint1251)

HAnimJoint1198.children.append(HAnimJoint1239)

HAnimJoint1058.children.append(HAnimJoint1198)

HAnimJoint1037.children.append(HAnimJoint1058)

HAnimJoint1022.children.append(HAnimJoint1037)

HAnimJoint1013.children.append(HAnimJoint1022)

HAnimJoint989.children.append(HAnimJoint1013)

HAnimJoint537.children.append(HAnimJoint989)

HAnimJoint528.children.append(HAnimJoint537)

HAnimJoint519.children.append(HAnimJoint528)

HAnimJoint510.children.append(HAnimJoint519)

HAnimJoint498.children.append(HAnimJoint510)

HAnimJoint477.children.append(HAnimJoint498)

HAnimJoint468.children.append(HAnimJoint477)

HAnimJoint459.children.append(HAnimJoint468)

HAnimJoint444.children.append(HAnimJoint459)

HAnimJoint432.children.append(HAnimJoint444)

HAnimJoint423.children.append(HAnimJoint432)

HAnimJoint414.children.append(HAnimJoint423)

HAnimJoint405.children.append(HAnimJoint414)

HAnimJoint387.children.append(HAnimJoint405)

HAnimJoint378.children.append(HAnimJoint387)

HAnimJoint369.children.append(HAnimJoint378)

HAnimJoint351.children.append(HAnimJoint369)

HAnimJoint43.children.append(HAnimJoint351)

HAnimHumanoid42.joints.append(HAnimJoint43)
HAnimJoint1281 = x3d.HAnimJoint()
HAnimJoint1281.USE = "STD_Joint_humanoid_root"

HAnimHumanoid42.joints.append(HAnimJoint1281)
HAnimSegment1282 = x3d.HAnimSegment()
HAnimSegment1282.USE = "STD_Segment_sacrum"

HAnimHumanoid42.segments.append(HAnimSegment1282)
HAnimJoint1283 = x3d.HAnimJoint()
HAnimJoint1283.USE = "STD_Joint_sacroiliac"

HAnimHumanoid42.joints.append(HAnimJoint1283)
HAnimSite1284 = x3d.HAnimSite()
HAnimSite1284.USE = "STD_Site_buttocks_standing_wall_contact_point_pt"

HAnimHumanoid42.sites.append(HAnimSite1284)
HAnimSite1285 = x3d.HAnimSite()
HAnimSite1285.USE = "STD_Site_crotch_pt"

HAnimHumanoid42.sites.append(HAnimSite1285)
HAnimSite1286 = x3d.HAnimSite()
HAnimSite1286.USE = "STD_Site_l_asis_pt"

HAnimHumanoid42.sites.append(HAnimSite1286)
HAnimSite1287 = x3d.HAnimSite()
HAnimSite1287.USE = "STD_Site_l_iliocristale_pt"

HAnimHumanoid42.sites.append(HAnimSite1287)
HAnimSite1288 = x3d.HAnimSite()
HAnimSite1288.USE = "STD_Site_l_psis_pt"

HAnimHumanoid42.sites.append(HAnimSite1288)
HAnimSite1289 = x3d.HAnimSite()
HAnimSite1289.USE = "STD_Site_l_trochanterion_pt"

HAnimHumanoid42.sites.append(HAnimSite1289)
HAnimSite1290 = x3d.HAnimSite()
HAnimSite1290.USE = "STD_Site_r_asis_pt"

HAnimHumanoid42.sites.append(HAnimSite1290)
HAnimSite1291 = x3d.HAnimSite()
HAnimSite1291.USE = "STD_Site_r_iliocristale_pt"

HAnimHumanoid42.sites.append(HAnimSite1291)
HAnimSite1292 = x3d.HAnimSite()
HAnimSite1292.USE = "STD_Site_r_psis_pt"

HAnimHumanoid42.sites.append(HAnimSite1292)
HAnimSite1293 = x3d.HAnimSite()
HAnimSite1293.USE = "STD_Site_r_trochanterion_pt"

HAnimHumanoid42.sites.append(HAnimSite1293)
HAnimSegment1294 = x3d.HAnimSegment()
HAnimSegment1294.USE = "STD_Segment_pelvis"

HAnimHumanoid42.segments.append(HAnimSegment1294)
HAnimJoint1295 = x3d.HAnimJoint()
HAnimJoint1295.USE = "STD_Joint_l_hip"

HAnimHumanoid42.joints.append(HAnimJoint1295)
HAnimSite1296 = x3d.HAnimSite()
HAnimSite1296.USE = "STD_Site_l_femoral_lateral_epicondyles_pt"

HAnimHumanoid42.sites.append(HAnimSite1296)
HAnimSite1297 = x3d.HAnimSite()
HAnimSite1297.USE = "STD_Site_l_femoral_medial_epicondyles_pt"

HAnimHumanoid42.sites.append(HAnimSite1297)
HAnimSite1298 = x3d.HAnimSite()
HAnimSite1298.USE = "STD_Site_l_knee_crease_pt"

HAnimHumanoid42.sites.append(HAnimSite1298)
HAnimSite1299 = x3d.HAnimSite()
HAnimSite1299.USE = "STD_Site_l_suprapatella_pt"

HAnimHumanoid42.sites.append(HAnimSite1299)
HAnimSegment1300 = x3d.HAnimSegment()
HAnimSegment1300.USE = "STD_Segment_l_thigh"

HAnimHumanoid42.segments.append(HAnimSegment1300)
HAnimJoint1301 = x3d.HAnimJoint()
HAnimJoint1301.USE = "STD_Joint_l_knee"

HAnimHumanoid42.joints.append(HAnimJoint1301)
HAnimSite1302 = x3d.HAnimSite()
HAnimSite1302.USE = "STD_Site_l_lateral_malleolus_pt"

HAnimHumanoid42.sites.append(HAnimSite1302)
HAnimSite1303 = x3d.HAnimSite()
HAnimSite1303.USE = "STD_Site_l_medial_malleolus_pt"

HAnimHumanoid42.sites.append(HAnimSite1303)
HAnimSite1304 = x3d.HAnimSite()
HAnimSite1304.USE = "STD_Site_l_tibiale_pt"

HAnimHumanoid42.sites.append(HAnimSite1304)
HAnimSegment1305 = x3d.HAnimSegment()
HAnimSegment1305.USE = "STD_Segment_l_calf"

HAnimHumanoid42.segments.append(HAnimSegment1305)
HAnimJoint1306 = x3d.HAnimJoint()
HAnimJoint1306.USE = "STD_Joint_l_talocrural"

HAnimHumanoid42.joints.append(HAnimJoint1306)
HAnimSite1307 = x3d.HAnimSite()
HAnimSite1307.USE = "STD_Site_l_calcaneus_posterior_pt"

HAnimHumanoid42.sites.append(HAnimSite1307)
HAnimSite1308 = x3d.HAnimSite()
HAnimSite1308.USE = "STD_Site_l_sphyrion_pt"

HAnimHumanoid42.sites.append(HAnimSite1308)
HAnimSegment1309 = x3d.HAnimSegment()
HAnimSegment1309.USE = "STD_Segment_l_talus"

HAnimHumanoid42.segments.append(HAnimSegment1309)
HAnimJoint1310 = x3d.HAnimJoint()
HAnimJoint1310.USE = "STD_Joint_l_talocalcaneonavicular"

HAnimHumanoid42.joints.append(HAnimJoint1310)
HAnimSegment1311 = x3d.HAnimSegment()
HAnimSegment1311.USE = "STD_Segment_l_navicular"

HAnimHumanoid42.segments.append(HAnimSegment1311)
HAnimJoint1312 = x3d.HAnimJoint()
HAnimJoint1312.USE = "STD_Joint_l_cuneonavicular_1"

HAnimHumanoid42.joints.append(HAnimJoint1312)
HAnimSegment1313 = x3d.HAnimSegment()
HAnimSegment1313.USE = "STD_Segment_l_cuneiform_1"

HAnimHumanoid42.segments.append(HAnimSegment1313)
HAnimJoint1314 = x3d.HAnimJoint()
HAnimJoint1314.USE = "STD_Joint_l_tarsometatarsal_1"

HAnimHumanoid42.joints.append(HAnimJoint1314)
HAnimSegment1315 = x3d.HAnimSegment()
HAnimSegment1315.USE = "STD_Segment_l_metatarsal_1"

HAnimHumanoid42.segments.append(HAnimSegment1315)
HAnimJoint1316 = x3d.HAnimJoint()
HAnimJoint1316.USE = "STD_Joint_l_metatarsophalangeal_1"

HAnimHumanoid42.joints.append(HAnimJoint1316)
HAnimSite1317 = x3d.HAnimSite()
HAnimSite1317.USE = "STD_Site_l_metatarsal_phalanx_1_pt"

HAnimHumanoid42.sites.append(HAnimSite1317)
HAnimSegment1318 = x3d.HAnimSegment()
HAnimSegment1318.USE = "STD_Segment_l_tarsal_proximal_phalanx_1"

HAnimHumanoid42.segments.append(HAnimSegment1318)
HAnimJoint1319 = x3d.HAnimJoint()
HAnimJoint1319.USE = "STD_Joint_l_tarsal_interphalangeal_1"

HAnimHumanoid42.joints.append(HAnimJoint1319)
HAnimSite1320 = x3d.HAnimSite()
HAnimSite1320.USE = "STD_Site_l_tarsal_distal_phalanx_1_tip"

HAnimHumanoid42.sites.append(HAnimSite1320)
HAnimSegment1321 = x3d.HAnimSegment()
HAnimSegment1321.USE = "STD_Segment_l_tarsal_distal_phalanx_1"

HAnimHumanoid42.segments.append(HAnimSegment1321)
HAnimJoint1322 = x3d.HAnimJoint()
HAnimJoint1322.USE = "STD_Joint_l_cuneonavicular_2"

HAnimHumanoid42.joints.append(HAnimJoint1322)
HAnimSegment1323 = x3d.HAnimSegment()
HAnimSegment1323.USE = "STD_Segment_l_cuneiform_2"

HAnimHumanoid42.segments.append(HAnimSegment1323)
HAnimJoint1324 = x3d.HAnimJoint()
HAnimJoint1324.USE = "STD_Joint_l_tarsometatarsal_2"

HAnimHumanoid42.joints.append(HAnimJoint1324)
HAnimSegment1325 = x3d.HAnimSegment()
HAnimSegment1325.USE = "STD_Segment_l_metatarsal_2"

HAnimHumanoid42.segments.append(HAnimSegment1325)
HAnimJoint1326 = x3d.HAnimJoint()
HAnimJoint1326.USE = "STD_Joint_l_metatarsophalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint1326)
HAnimSegment1327 = x3d.HAnimSegment()
HAnimSegment1327.USE = "STD_Segment_l_tarsal_proximal_phalanx_2"

HAnimHumanoid42.segments.append(HAnimSegment1327)
HAnimJoint1328 = x3d.HAnimJoint()
HAnimJoint1328.USE = "STD_Joint_l_tarsal_proximal_interphalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint1328)
HAnimSegment1329 = x3d.HAnimSegment()
HAnimSegment1329.USE = "STD_Segment_l_tarsal_middle_phalanx_2"

HAnimHumanoid42.segments.append(HAnimSegment1329)
HAnimJoint1330 = x3d.HAnimJoint()
HAnimJoint1330.USE = "STD_Joint_l_tarsal_distal_interphalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint1330)
HAnimSite1331 = x3d.HAnimSite()
HAnimSite1331.USE = "STD_Site_l_tarsal_distal_phalanx_2_tip"

HAnimHumanoid42.sites.append(HAnimSite1331)
HAnimSegment1332 = x3d.HAnimSegment()
HAnimSegment1332.USE = "STD_Segment_l_tarsal_distal_phalanx_2"

HAnimHumanoid42.segments.append(HAnimSegment1332)
HAnimJoint1333 = x3d.HAnimJoint()
HAnimJoint1333.USE = "STD_Joint_l_cuneonavicular_3"

HAnimHumanoid42.joints.append(HAnimJoint1333)
HAnimSegment1334 = x3d.HAnimSegment()
HAnimSegment1334.USE = "STD_Segment_l_cuneiform_3"

HAnimHumanoid42.segments.append(HAnimSegment1334)
HAnimJoint1335 = x3d.HAnimJoint()
HAnimJoint1335.USE = "STD_Joint_l_tarsometatarsal_3 "

HAnimHumanoid42.joints.append(HAnimJoint1335)
HAnimSegment1336 = x3d.HAnimSegment()
HAnimSegment1336.USE = "STD_Segment_l_metatarsal_3"

HAnimHumanoid42.segments.append(HAnimSegment1336)
HAnimJoint1337 = x3d.HAnimJoint()
HAnimJoint1337.USE = "STD_Joint_l_metatarsophalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint1337)
HAnimSegment1338 = x3d.HAnimSegment()
HAnimSegment1338.USE = "STD_Segment_l_tarsal_proximal_phalanx_3"

HAnimHumanoid42.segments.append(HAnimSegment1338)
HAnimJoint1339 = x3d.HAnimJoint()
HAnimJoint1339.USE = "STD_Joint_l_tarsal_proximal_interphalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint1339)
HAnimSegment1340 = x3d.HAnimSegment()
HAnimSegment1340.USE = "STD_Segment_l_tarsal_middle_phalanx_3"

HAnimHumanoid42.segments.append(HAnimSegment1340)
HAnimJoint1341 = x3d.HAnimJoint()
HAnimJoint1341.USE = "STD_Joint_l_tarsal_distal_interphalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint1341)
HAnimSite1342 = x3d.HAnimSite()
HAnimSite1342.USE = "STD_Site_l_tarsal_distal_phalanx_3_tip"

HAnimHumanoid42.sites.append(HAnimSite1342)
HAnimSegment1343 = x3d.HAnimSegment()
HAnimSegment1343.USE = "STD_Segment_l_tarsal_distal_phalanx_3"

HAnimHumanoid42.segments.append(HAnimSegment1343)
HAnimJoint1344 = x3d.HAnimJoint()
HAnimJoint1344.USE = "STD_Joint_l_calcaneocuboid"

HAnimHumanoid42.joints.append(HAnimJoint1344)
HAnimSegment1345 = x3d.HAnimSegment()
HAnimSegment1345.USE = "STD_Segment_l_calcaneus"

HAnimHumanoid42.segments.append(HAnimSegment1345)
HAnimJoint1346 = x3d.HAnimJoint()
HAnimJoint1346.USE = "STD_Joint_l_transversetarsal"

HAnimHumanoid42.joints.append(HAnimJoint1346)
HAnimSegment1347 = x3d.HAnimSegment()
HAnimSegment1347.USE = "STD_Segment_l_cuboid"

HAnimHumanoid42.segments.append(HAnimSegment1347)
HAnimJoint1348 = x3d.HAnimJoint()
HAnimJoint1348.USE = "STD_Joint_l_tarsometatarsal_4"

HAnimHumanoid42.joints.append(HAnimJoint1348)
HAnimSegment1349 = x3d.HAnimSegment()
HAnimSegment1349.USE = "STD_Segment_l_metatarsal_4"

HAnimHumanoid42.segments.append(HAnimSegment1349)
HAnimJoint1350 = x3d.HAnimJoint()
HAnimJoint1350.USE = "STD_Joint_l_metatarsophalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint1350)
HAnimSegment1351 = x3d.HAnimSegment()
HAnimSegment1351.USE = "STD_Segment_l_tarsal_proximal_phalanx_4"

HAnimHumanoid42.segments.append(HAnimSegment1351)
HAnimJoint1352 = x3d.HAnimJoint()
HAnimJoint1352.USE = "STD_Joint_l_tarsal_proximal_interphalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint1352)
HAnimSegment1353 = x3d.HAnimSegment()
HAnimSegment1353.USE = "STD_Segment_l_tarsal_middle_phalanx_4"

HAnimHumanoid42.segments.append(HAnimSegment1353)
HAnimJoint1354 = x3d.HAnimJoint()
HAnimJoint1354.USE = "STD_Joint_l_tarsal_distal_interphalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint1354)
HAnimSite1355 = x3d.HAnimSite()
HAnimSite1355.USE = "STD_Site_l_tarsal_distal_phalanx_4_tip"

HAnimHumanoid42.sites.append(HAnimSite1355)
HAnimSegment1356 = x3d.HAnimSegment()
HAnimSegment1356.USE = "STD_Segment_l_tarsal_distal_phalanx_4"

HAnimHumanoid42.segments.append(HAnimSegment1356)
HAnimJoint1357 = x3d.HAnimJoint()
HAnimJoint1357.USE = "STD_Joint_l_tarsometatarsal_5"

HAnimHumanoid42.joints.append(HAnimJoint1357)
HAnimSegment1358 = x3d.HAnimSegment()
HAnimSegment1358.USE = "STD_Segment_l_metatarsal_5"

HAnimHumanoid42.segments.append(HAnimSegment1358)
HAnimJoint1359 = x3d.HAnimJoint()
HAnimJoint1359.USE = "STD_Joint_l_metatarsophalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint1359)
HAnimSite1360 = x3d.HAnimSite()
HAnimSite1360.USE = "STD_Site_l_metatarsal_phalanx_5_pt"

HAnimHumanoid42.sites.append(HAnimSite1360)
HAnimSegment1361 = x3d.HAnimSegment()
HAnimSegment1361.USE = "STD_Segment_l_tarsal_proximal_phalanx_5"

HAnimHumanoid42.segments.append(HAnimSegment1361)
HAnimJoint1362 = x3d.HAnimJoint()
HAnimJoint1362.USE = "STD_Joint_l_tarsal_proximal_interphalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint1362)
HAnimSegment1363 = x3d.HAnimSegment()
HAnimSegment1363.USE = "STD_Segment_l_tarsal_middle_phalanx_5"

HAnimHumanoid42.segments.append(HAnimSegment1363)
HAnimJoint1364 = x3d.HAnimJoint()
HAnimJoint1364.USE = "STD_Joint_l_tarsal_distal_interphalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint1364)
HAnimSite1365 = x3d.HAnimSite()
HAnimSite1365.USE = "STD_Site_l_tarsal_distal_phalanx_5_tip"

HAnimHumanoid42.sites.append(HAnimSite1365)
HAnimSegment1366 = x3d.HAnimSegment()
HAnimSegment1366.USE = "STD_Segment_l_tarsal_distal_phalanx_5"

HAnimHumanoid42.segments.append(HAnimSegment1366)
HAnimJoint1367 = x3d.HAnimJoint()
HAnimJoint1367.USE = "STD_Joint_r_hip"

HAnimHumanoid42.joints.append(HAnimJoint1367)
HAnimSite1368 = x3d.HAnimSite()
HAnimSite1368.USE = "STD_Site_r_femoral_lateral_epicondyles_pt"

HAnimHumanoid42.sites.append(HAnimSite1368)
HAnimSite1369 = x3d.HAnimSite()
HAnimSite1369.USE = "STD_Site_r_femoral_medial_epicondyles_pt"

HAnimHumanoid42.sites.append(HAnimSite1369)
HAnimSite1370 = x3d.HAnimSite()
HAnimSite1370.USE = "STD_Site_r_knee_crease_pt"

HAnimHumanoid42.sites.append(HAnimSite1370)
HAnimSite1371 = x3d.HAnimSite()
HAnimSite1371.USE = "STD_Site_r_suprapatella_pt"

HAnimHumanoid42.sites.append(HAnimSite1371)
HAnimSegment1372 = x3d.HAnimSegment()
HAnimSegment1372.USE = "STD_Segment_r_thigh"

HAnimHumanoid42.segments.append(HAnimSegment1372)
HAnimJoint1373 = x3d.HAnimJoint()
HAnimJoint1373.USE = "STD_Joint_r_knee"

HAnimHumanoid42.joints.append(HAnimJoint1373)
HAnimSite1374 = x3d.HAnimSite()
HAnimSite1374.USE = "STD_Site_r_lateral_malleolus_pt"

HAnimHumanoid42.sites.append(HAnimSite1374)
HAnimSite1375 = x3d.HAnimSite()
HAnimSite1375.USE = "STD_Site_r_medial_malleolus_pt"

HAnimHumanoid42.sites.append(HAnimSite1375)
HAnimSite1376 = x3d.HAnimSite()
HAnimSite1376.USE = "STD_Site_r_tibiale_pt"

HAnimHumanoid42.sites.append(HAnimSite1376)
HAnimSegment1377 = x3d.HAnimSegment()
HAnimSegment1377.USE = "STD_Segment_r_calf"

HAnimHumanoid42.segments.append(HAnimSegment1377)
HAnimJoint1378 = x3d.HAnimJoint()
HAnimJoint1378.USE = "STD_Joint_r_talocrural"

HAnimHumanoid42.joints.append(HAnimJoint1378)
HAnimSite1379 = x3d.HAnimSite()
HAnimSite1379.USE = "STD_Site_r_calcaneus_posterior_pt"

HAnimHumanoid42.sites.append(HAnimSite1379)
HAnimSite1380 = x3d.HAnimSite()
HAnimSite1380.USE = "STD_Site_r_sphyrion_pt"

HAnimHumanoid42.sites.append(HAnimSite1380)
HAnimSegment1381 = x3d.HAnimSegment()
HAnimSegment1381.USE = "STD_Segment_r_talus"

HAnimHumanoid42.segments.append(HAnimSegment1381)
HAnimJoint1382 = x3d.HAnimJoint()
HAnimJoint1382.USE = "STD_Joint_r_talocalcaneonavicular"

HAnimHumanoid42.joints.append(HAnimJoint1382)
HAnimSegment1383 = x3d.HAnimSegment()
HAnimSegment1383.USE = "STD_Segment_r_navicular"

HAnimHumanoid42.segments.append(HAnimSegment1383)
HAnimJoint1384 = x3d.HAnimJoint()
HAnimJoint1384.USE = "STD_Joint_r_cuneonavicular_1"

HAnimHumanoid42.joints.append(HAnimJoint1384)
HAnimSegment1385 = x3d.HAnimSegment()
HAnimSegment1385.USE = "STD_Segment_r_cuneiform_1"

HAnimHumanoid42.segments.append(HAnimSegment1385)
HAnimJoint1386 = x3d.HAnimJoint()
HAnimJoint1386.USE = "STD_Joint_r_tarsometatarsal_1"

HAnimHumanoid42.joints.append(HAnimJoint1386)
HAnimSegment1387 = x3d.HAnimSegment()
HAnimSegment1387.USE = "STD_Segment_r_metatarsal_1"

HAnimHumanoid42.segments.append(HAnimSegment1387)
HAnimJoint1388 = x3d.HAnimJoint()
HAnimJoint1388.USE = "STD_Joint_r_metatarsophalangeal_1"

HAnimHumanoid42.joints.append(HAnimJoint1388)
HAnimSite1389 = x3d.HAnimSite()
HAnimSite1389.USE = "STD_Site_r_metatarsal_phalanx_1_pt"

HAnimHumanoid42.sites.append(HAnimSite1389)
HAnimSegment1390 = x3d.HAnimSegment()
HAnimSegment1390.USE = "STD_Segment_r_tarsal_proximal_phalanx_1"

HAnimHumanoid42.segments.append(HAnimSegment1390)
HAnimJoint1391 = x3d.HAnimJoint()
HAnimJoint1391.USE = "STD_Joint_r_tarsal_interphalangeal_1"

HAnimHumanoid42.joints.append(HAnimJoint1391)
HAnimSite1392 = x3d.HAnimSite()
HAnimSite1392.USE = "STD_Site_r_tarsal_distal_phalanx_1_tip"

HAnimHumanoid42.sites.append(HAnimSite1392)
HAnimSegment1393 = x3d.HAnimSegment()
HAnimSegment1393.USE = "STD_Segment_r_tarsal_distal_phalanx_1"

HAnimHumanoid42.segments.append(HAnimSegment1393)
HAnimJoint1394 = x3d.HAnimJoint()
HAnimJoint1394.USE = "STD_Joint_r_cuneonavicular_2"

HAnimHumanoid42.joints.append(HAnimJoint1394)
HAnimSegment1395 = x3d.HAnimSegment()
HAnimSegment1395.USE = "STD_Segment_r_cuneiform_2"

HAnimHumanoid42.segments.append(HAnimSegment1395)
HAnimJoint1396 = x3d.HAnimJoint()
HAnimJoint1396.USE = "STD_Joint_r_tarsometatarsal_2"

HAnimHumanoid42.joints.append(HAnimJoint1396)
HAnimSegment1397 = x3d.HAnimSegment()
HAnimSegment1397.USE = "STD_Segment_r_metatarsal_2"

HAnimHumanoid42.segments.append(HAnimSegment1397)
HAnimJoint1398 = x3d.HAnimJoint()
HAnimJoint1398.USE = "STD_Joint_r_metatarsophalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint1398)
HAnimSegment1399 = x3d.HAnimSegment()
HAnimSegment1399.USE = "STD_Segment_r_tarsal_proximal_phalanx_2"

HAnimHumanoid42.segments.append(HAnimSegment1399)
HAnimJoint1400 = x3d.HAnimJoint()
HAnimJoint1400.USE = "STD_Joint_r_tarsal_proximal_interphalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint1400)
HAnimSegment1401 = x3d.HAnimSegment()
HAnimSegment1401.USE = "STD_Segment_r_tarsal_middle_phalanx_2"

HAnimHumanoid42.segments.append(HAnimSegment1401)
HAnimJoint1402 = x3d.HAnimJoint()
HAnimJoint1402.USE = "STD_Joint_r_tarsal_distal_interphalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint1402)
HAnimSite1403 = x3d.HAnimSite()
HAnimSite1403.USE = "STD_Site_r_tarsal_distal_phalanx_2_tip"

HAnimHumanoid42.sites.append(HAnimSite1403)
HAnimSegment1404 = x3d.HAnimSegment()
HAnimSegment1404.USE = "STD_Segment_r_tarsal_distal_phalanx_2"

HAnimHumanoid42.segments.append(HAnimSegment1404)
HAnimJoint1405 = x3d.HAnimJoint()
HAnimJoint1405.USE = "STD_Joint_r_cuneonavicular_3"

HAnimHumanoid42.joints.append(HAnimJoint1405)
HAnimSegment1406 = x3d.HAnimSegment()
HAnimSegment1406.USE = "STD_Segment_r_cuneiform_3"

HAnimHumanoid42.segments.append(HAnimSegment1406)
HAnimJoint1407 = x3d.HAnimJoint()
HAnimJoint1407.USE = "STD_Joint_r_tarsometatarsal_3 "

HAnimHumanoid42.joints.append(HAnimJoint1407)
HAnimSegment1408 = x3d.HAnimSegment()
HAnimSegment1408.USE = "STD_Segment_r_metatarsal_3"

HAnimHumanoid42.segments.append(HAnimSegment1408)
HAnimJoint1409 = x3d.HAnimJoint()
HAnimJoint1409.USE = "STD_Joint_r_metatarsophalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint1409)
HAnimSegment1410 = x3d.HAnimSegment()
HAnimSegment1410.USE = "STD_Segment_r_tarsal_proximal_phalanx_3"

HAnimHumanoid42.segments.append(HAnimSegment1410)
HAnimJoint1411 = x3d.HAnimJoint()
HAnimJoint1411.USE = "STD_Joint_r_tarsal_proximal_interphalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint1411)
HAnimSegment1412 = x3d.HAnimSegment()
HAnimSegment1412.USE = "STD_Segment_r_tarsal_middle_phalanx_3"

HAnimHumanoid42.segments.append(HAnimSegment1412)
HAnimJoint1413 = x3d.HAnimJoint()
HAnimJoint1413.USE = "STD_Joint_r_tarsal_distal_interphalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint1413)
HAnimSite1414 = x3d.HAnimSite()
HAnimSite1414.USE = "STD_Site_r_tarsal_distal_phalanx_3_tip"

HAnimHumanoid42.sites.append(HAnimSite1414)
HAnimSegment1415 = x3d.HAnimSegment()
HAnimSegment1415.USE = "STD_Segment_r_tarsal_distal_phalanx_3"

HAnimHumanoid42.segments.append(HAnimSegment1415)
HAnimJoint1416 = x3d.HAnimJoint()
HAnimJoint1416.USE = "STD_Joint_r_calcaneocuboid"

HAnimHumanoid42.joints.append(HAnimJoint1416)
HAnimSegment1417 = x3d.HAnimSegment()
HAnimSegment1417.USE = "STD_Segment_r_calcaneus"

HAnimHumanoid42.segments.append(HAnimSegment1417)
HAnimJoint1418 = x3d.HAnimJoint()
HAnimJoint1418.USE = "STD_Joint_r_transversetarsal"

HAnimHumanoid42.joints.append(HAnimJoint1418)
HAnimSegment1419 = x3d.HAnimSegment()
HAnimSegment1419.USE = "STD_Segment_r_cuboid"

HAnimHumanoid42.segments.append(HAnimSegment1419)
HAnimJoint1420 = x3d.HAnimJoint()
HAnimJoint1420.USE = "STD_Joint_r_tarsometatarsal_4"

HAnimHumanoid42.joints.append(HAnimJoint1420)
HAnimSegment1421 = x3d.HAnimSegment()
HAnimSegment1421.USE = "STD_Segment_r_metatarsal_4"

HAnimHumanoid42.segments.append(HAnimSegment1421)
HAnimJoint1422 = x3d.HAnimJoint()
HAnimJoint1422.USE = "STD_Joint_r_metatarsophalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint1422)
HAnimSegment1423 = x3d.HAnimSegment()
HAnimSegment1423.USE = "STD_Segment_r_tarsal_proximal_phalanx_4"

HAnimHumanoid42.segments.append(HAnimSegment1423)
HAnimJoint1424 = x3d.HAnimJoint()
HAnimJoint1424.USE = "STD_Joint_r_tarsal_proximal_interphalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint1424)
HAnimSegment1425 = x3d.HAnimSegment()
HAnimSegment1425.USE = "STD_Segment_r_tarsal_middle_phalanx_4"

HAnimHumanoid42.segments.append(HAnimSegment1425)
HAnimJoint1426 = x3d.HAnimJoint()
HAnimJoint1426.USE = "STD_Joint_r_tarsal_distal_interphalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint1426)
HAnimSite1427 = x3d.HAnimSite()
HAnimSite1427.USE = "STD_Site_r_tarsal_distal_phalanx_4_tip"

HAnimHumanoid42.sites.append(HAnimSite1427)
HAnimSegment1428 = x3d.HAnimSegment()
HAnimSegment1428.USE = "STD_Segment_r_tarsal_distal_phalanx_4"

HAnimHumanoid42.segments.append(HAnimSegment1428)
HAnimJoint1429 = x3d.HAnimJoint()
HAnimJoint1429.USE = "STD_Joint_r_tarsometatarsal_5"

HAnimHumanoid42.joints.append(HAnimJoint1429)
HAnimSegment1430 = x3d.HAnimSegment()
HAnimSegment1430.USE = "STD_Segment_r_metatarsal_5"

HAnimHumanoid42.segments.append(HAnimSegment1430)
HAnimJoint1431 = x3d.HAnimJoint()
HAnimJoint1431.USE = "STD_Joint_r_metatarsophalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint1431)
HAnimSite1432 = x3d.HAnimSite()
HAnimSite1432.USE = "STD_Site_r_metatarsal_phalanx_5_pt"

HAnimHumanoid42.sites.append(HAnimSite1432)
HAnimSegment1433 = x3d.HAnimSegment()
HAnimSegment1433.USE = "STD_Segment_r_tarsal_proximal_phalanx_5"

HAnimHumanoid42.segments.append(HAnimSegment1433)
HAnimJoint1434 = x3d.HAnimJoint()
HAnimJoint1434.USE = "STD_Joint_r_tarsal_proximal_interphalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint1434)
HAnimSegment1435 = x3d.HAnimSegment()
HAnimSegment1435.USE = "STD_Segment_r_tarsal_middle_phalanx_5"

HAnimHumanoid42.segments.append(HAnimSegment1435)
HAnimJoint1436 = x3d.HAnimJoint()
HAnimJoint1436.USE = "STD_Joint_r_tarsal_distal_interphalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint1436)
HAnimSite1437 = x3d.HAnimSite()
HAnimSite1437.USE = "STD_Site_r_tarsal_distal_phalanx_5_tip"

HAnimHumanoid42.sites.append(HAnimSite1437)
HAnimSegment1438 = x3d.HAnimSegment()
HAnimSegment1438.USE = "STD_Segment_r_tarsal_distal_phalanx_5"

HAnimHumanoid42.segments.append(HAnimSegment1438)
HAnimJoint1439 = x3d.HAnimJoint()
HAnimJoint1439.USE = "STD_Joint_vl5"

HAnimHumanoid42.joints.append(HAnimJoint1439)
HAnimSite1440 = x3d.HAnimSite()
HAnimSite1440.USE = "STD_Site_navel_pt"

HAnimHumanoid42.sites.append(HAnimSite1440)
HAnimSite1441 = x3d.HAnimSite()
HAnimSite1441.USE = "STD_Site_waist_preferred_anterior_pt"

HAnimHumanoid42.sites.append(HAnimSite1441)
HAnimSite1442 = x3d.HAnimSite()
HAnimSite1442.USE = "STD_Site_waist_preferred_posterior_pt"

HAnimHumanoid42.sites.append(HAnimSite1442)
HAnimSegment1443 = x3d.HAnimSegment()
HAnimSegment1443.USE = "STD_Segment_l5"

HAnimHumanoid42.segments.append(HAnimSegment1443)
HAnimJoint1444 = x3d.HAnimJoint()
HAnimJoint1444.USE = "STD_Joint_vl4"

HAnimHumanoid42.joints.append(HAnimJoint1444)
HAnimSegment1445 = x3d.HAnimSegment()
HAnimSegment1445.USE = "STD_Segment_l4"

HAnimHumanoid42.segments.append(HAnimSegment1445)
HAnimJoint1446 = x3d.HAnimJoint()
HAnimJoint1446.USE = "STD_Joint_vl3"

HAnimHumanoid42.joints.append(HAnimJoint1446)
HAnimSegment1447 = x3d.HAnimSegment()
HAnimSegment1447.USE = "STD_Segment_l3"

HAnimHumanoid42.segments.append(HAnimSegment1447)
HAnimJoint1448 = x3d.HAnimJoint()
HAnimJoint1448.USE = "STD_Joint_vl2"

HAnimHumanoid42.joints.append(HAnimJoint1448)
HAnimSite1449 = x3d.HAnimSite()
HAnimSite1449.USE = "STD_Site_l_rib10_pt"

HAnimHumanoid42.sites.append(HAnimSite1449)
HAnimSite1450 = x3d.HAnimSite()
HAnimSite1450.USE = "STD_Site_r_rib10_pt"

HAnimHumanoid42.sites.append(HAnimSite1450)
HAnimSite1451 = x3d.HAnimSite()
HAnimSite1451.USE = "STD_Site_spine_2_middle_back_pt"

HAnimHumanoid42.sites.append(HAnimSite1451)
HAnimSegment1452 = x3d.HAnimSegment()
HAnimSegment1452.USE = "STD_Segment_l2"

HAnimHumanoid42.segments.append(HAnimSegment1452)
HAnimJoint1453 = x3d.HAnimJoint()
HAnimJoint1453.USE = "STD_Joint_vl1"

HAnimHumanoid42.joints.append(HAnimJoint1453)
HAnimSegment1454 = x3d.HAnimSegment()
HAnimSegment1454.USE = "STD_Segment_l1"

HAnimHumanoid42.segments.append(HAnimSegment1454)
HAnimJoint1455 = x3d.HAnimJoint()
HAnimJoint1455.USE = "STD_Joint_vt12"

HAnimHumanoid42.joints.append(HAnimJoint1455)
HAnimSegment1456 = x3d.HAnimSegment()
HAnimSegment1456.USE = "STD_Segment_t12"

HAnimHumanoid42.segments.append(HAnimSegment1456)
HAnimJoint1457 = x3d.HAnimJoint()
HAnimJoint1457.USE = "STD_Joint_vt11"

HAnimHumanoid42.joints.append(HAnimJoint1457)
HAnimSegment1458 = x3d.HAnimSegment()
HAnimSegment1458.USE = "STD_Segment_t11"

HAnimHumanoid42.segments.append(HAnimSegment1458)
HAnimJoint1459 = x3d.HAnimJoint()
HAnimJoint1459.USE = "STD_Joint_vt10"

HAnimHumanoid42.joints.append(HAnimJoint1459)
HAnimSite1460 = x3d.HAnimSite()
HAnimSite1460.USE = "STD_Site_substernale_pt"

HAnimHumanoid42.sites.append(HAnimSite1460)
HAnimSegment1461 = x3d.HAnimSegment()
HAnimSegment1461.USE = "STD_Segment_t10"

HAnimHumanoid42.segments.append(HAnimSegment1461)
HAnimJoint1462 = x3d.HAnimJoint()
HAnimJoint1462.USE = "STD_Joint_vt9"

HAnimHumanoid42.joints.append(HAnimJoint1462)
HAnimSite1463 = x3d.HAnimSite()
HAnimSite1463.USE = "STD_Site_l_thelion_pt"

HAnimHumanoid42.sites.append(HAnimSite1463)
HAnimSite1464 = x3d.HAnimSite()
HAnimSite1464.USE = "STD_Site_r_thelion_pt"

HAnimHumanoid42.sites.append(HAnimSite1464)
HAnimSegment1465 = x3d.HAnimSegment()
HAnimSegment1465.USE = "STD_Segment_t9"

HAnimHumanoid42.segments.append(HAnimSegment1465)
HAnimJoint1466 = x3d.HAnimJoint()
HAnimJoint1466.USE = "STD_Joint_vt8"

HAnimHumanoid42.joints.append(HAnimJoint1466)
HAnimSegment1467 = x3d.HAnimSegment()
HAnimSegment1467.USE = "STD_Segment_t8"

HAnimHumanoid42.segments.append(HAnimSegment1467)
HAnimJoint1468 = x3d.HAnimJoint()
HAnimJoint1468.USE = "STD_Joint_vt7"

HAnimHumanoid42.joints.append(HAnimJoint1468)
HAnimSegment1469 = x3d.HAnimSegment()
HAnimSegment1469.USE = "STD_Segment_t7"

HAnimHumanoid42.segments.append(HAnimSegment1469)
HAnimJoint1470 = x3d.HAnimJoint()
HAnimJoint1470.USE = "STD_Joint_vt6"

HAnimHumanoid42.joints.append(HAnimJoint1470)
HAnimSite1471 = x3d.HAnimSite()
HAnimSite1471.USE = "STD_Site_l_chest_midsagittal_plane_pt"

HAnimHumanoid42.sites.append(HAnimSite1471)
HAnimSite1472 = x3d.HAnimSite()
HAnimSite1472.USE = "STD_Site_mesosternale_pt"

HAnimHumanoid42.sites.append(HAnimSite1472)
HAnimSite1473 = x3d.HAnimSite()
HAnimSite1473.USE = "STD_Site_r_chest_midsagittal_plane_pt"

HAnimHumanoid42.sites.append(HAnimSite1473)
HAnimSite1474 = x3d.HAnimSite()
HAnimSite1474.USE = "STD_Site_rear_center_midsagittal_plane_pt"

HAnimHumanoid42.sites.append(HAnimSite1474)
HAnimSegment1475 = x3d.HAnimSegment()
HAnimSegment1475.USE = "STD_Segment_t6"

HAnimHumanoid42.segments.append(HAnimSegment1475)
HAnimJoint1476 = x3d.HAnimJoint()
HAnimJoint1476.USE = "STD_Joint_vt5"

HAnimHumanoid42.joints.append(HAnimJoint1476)
HAnimSite1477 = x3d.HAnimSite()
HAnimSite1477.USE = "STD_Site_spine_1_middle_back_pt"

HAnimHumanoid42.sites.append(HAnimSite1477)
HAnimSegment1478 = x3d.HAnimSegment()
HAnimSegment1478.USE = "STD_Segment_t5"

HAnimHumanoid42.segments.append(HAnimSegment1478)
HAnimJoint1479 = x3d.HAnimJoint()
HAnimJoint1479.USE = "STD_Joint_vt4"

HAnimHumanoid42.joints.append(HAnimJoint1479)
HAnimSegment1480 = x3d.HAnimSegment()
HAnimSegment1480.USE = "STD_Segment_t4"

HAnimHumanoid42.segments.append(HAnimSegment1480)
HAnimJoint1481 = x3d.HAnimJoint()
HAnimJoint1481.USE = "STD_Joint_vt3"

HAnimHumanoid42.joints.append(HAnimJoint1481)
HAnimSegment1482 = x3d.HAnimSegment()
HAnimSegment1482.USE = "STD_Segment_t3"

HAnimHumanoid42.segments.append(HAnimSegment1482)
HAnimJoint1483 = x3d.HAnimJoint()
HAnimJoint1483.USE = "STD_Joint_vt2"

HAnimHumanoid42.joints.append(HAnimJoint1483)
HAnimSegment1484 = x3d.HAnimSegment()
HAnimSegment1484.USE = "STD_Segment_t2"

HAnimHumanoid42.segments.append(HAnimSegment1484)
HAnimJoint1485 = x3d.HAnimJoint()
HAnimJoint1485.USE = "STD_Joint_vt1"

HAnimHumanoid42.joints.append(HAnimJoint1485)
HAnimSite1486 = x3d.HAnimSite()
HAnimSite1486.USE = "STD_Site_cervicale_pt"

HAnimHumanoid42.sites.append(HAnimSite1486)
HAnimSite1487 = x3d.HAnimSite()
HAnimSite1487.USE = "STD_Site_suprasternale_pt"

HAnimHumanoid42.sites.append(HAnimSite1487)
HAnimSegment1488 = x3d.HAnimSegment()
HAnimSegment1488.USE = "STD_Segment_t1"

HAnimHumanoid42.segments.append(HAnimSegment1488)
HAnimJoint1489 = x3d.HAnimJoint()
HAnimJoint1489.USE = "STD_Joint_vc7"

HAnimHumanoid42.joints.append(HAnimJoint1489)
HAnimSite1490 = x3d.HAnimSite()
HAnimSite1490.USE = "STD_Site_l_neck_base_pt"

HAnimHumanoid42.sites.append(HAnimSite1490)
HAnimSite1491 = x3d.HAnimSite()
HAnimSite1491.USE = "STD_Site_r_neck_base_pt"

HAnimHumanoid42.sites.append(HAnimSite1491)
HAnimSegment1492 = x3d.HAnimSegment()
HAnimSegment1492.USE = "STD_Segment_c7"

HAnimHumanoid42.segments.append(HAnimSegment1492)
HAnimJoint1493 = x3d.HAnimJoint()
HAnimJoint1493.USE = "STD_Joint_vc6"

HAnimHumanoid42.joints.append(HAnimJoint1493)
HAnimSegment1494 = x3d.HAnimSegment()
HAnimSegment1494.USE = "STD_Segment_c6"

HAnimHumanoid42.segments.append(HAnimSegment1494)
HAnimJoint1495 = x3d.HAnimJoint()
HAnimJoint1495.USE = "STD_Joint_vc5"

HAnimHumanoid42.joints.append(HAnimJoint1495)
HAnimSegment1496 = x3d.HAnimSegment()
HAnimSegment1496.USE = "STD_Segment_c5"

HAnimHumanoid42.segments.append(HAnimSegment1496)
HAnimJoint1497 = x3d.HAnimJoint()
HAnimJoint1497.USE = "STD_Joint_vc4"

HAnimHumanoid42.joints.append(HAnimJoint1497)
HAnimSegment1498 = x3d.HAnimSegment()
HAnimSegment1498.USE = "STD_Segment_c4"

HAnimHumanoid42.segments.append(HAnimSegment1498)
HAnimJoint1499 = x3d.HAnimJoint()
HAnimJoint1499.USE = "STD_Joint_vc3"

HAnimHumanoid42.joints.append(HAnimJoint1499)
HAnimSegment1500 = x3d.HAnimSegment()
HAnimSegment1500.USE = "STD_Segment_c3"

HAnimHumanoid42.segments.append(HAnimSegment1500)
HAnimJoint1501 = x3d.HAnimJoint()
HAnimJoint1501.USE = "STD_Joint_vc2"

HAnimHumanoid42.joints.append(HAnimJoint1501)
HAnimSite1502 = x3d.HAnimSite()
HAnimSite1502.USE = "STD_Site_adams_apple_pt"

HAnimHumanoid42.sites.append(HAnimSite1502)
HAnimSegment1503 = x3d.HAnimSegment()
HAnimSegment1503.USE = "STD_Segment_c2"

HAnimHumanoid42.segments.append(HAnimSegment1503)
HAnimJoint1504 = x3d.HAnimJoint()
HAnimJoint1504.USE = "STD_Joint_vc1"

HAnimHumanoid42.joints.append(HAnimJoint1504)
HAnimSegment1505 = x3d.HAnimSegment()
HAnimSegment1505.USE = "STD_Segment_c1"

HAnimHumanoid42.segments.append(HAnimSegment1505)
HAnimJoint1506 = x3d.HAnimJoint()
HAnimJoint1506.USE = "STD_Joint_skullbase"

HAnimHumanoid42.joints.append(HAnimJoint1506)
HAnimSite1507 = x3d.HAnimSite()
HAnimSite1507.USE = "STD_Site_glabella_pt"

HAnimHumanoid42.sites.append(HAnimSite1507)
HAnimSite1508 = x3d.HAnimSite()
HAnimSite1508.USE = "STD_Site_l_ectocanthus_pt"

HAnimHumanoid42.sites.append(HAnimSite1508)
HAnimSite1509 = x3d.HAnimSite()
HAnimSite1509.USE = "STD_Site_l_infraorbitale_pt"

HAnimHumanoid42.sites.append(HAnimSite1509)
HAnimSite1510 = x3d.HAnimSite()
HAnimSite1510.USE = "STD_Site_l_tragion_pt"

HAnimHumanoid42.sites.append(HAnimSite1510)
HAnimSite1511 = x3d.HAnimSite()
HAnimSite1511.USE = "STD_Site_nuchale_pt"

HAnimHumanoid42.sites.append(HAnimSite1511)
HAnimSite1512 = x3d.HAnimSite()
HAnimSite1512.USE = "STD_Site_opisthocranion_pt"

HAnimHumanoid42.sites.append(HAnimSite1512)
HAnimSite1513 = x3d.HAnimSite()
HAnimSite1513.USE = "STD_Site_r_ectocanthus_pt"

HAnimHumanoid42.sites.append(HAnimSite1513)
HAnimSite1514 = x3d.HAnimSite()
HAnimSite1514.USE = "STD_Site_r_infraorbitale_pt"

HAnimHumanoid42.sites.append(HAnimSite1514)
HAnimSite1515 = x3d.HAnimSite()
HAnimSite1515.USE = "STD_Site_r_tragion_pt"

HAnimHumanoid42.sites.append(HAnimSite1515)
HAnimSite1516 = x3d.HAnimSite()
HAnimSite1516.USE = "STD_Site_sellion_pt"

HAnimHumanoid42.sites.append(HAnimSite1516)
HAnimSite1517 = x3d.HAnimSite()
HAnimSite1517.USE = "STD_Site_skull_vertex_pt"

HAnimHumanoid42.sites.append(HAnimSite1517)
HAnimSegment1518 = x3d.HAnimSegment()
HAnimSegment1518.USE = "STD_Segment_skull"

HAnimHumanoid42.segments.append(HAnimSegment1518)
HAnimJoint1519 = x3d.HAnimJoint()
HAnimJoint1519.USE = "STD_Joint_l_eyelid_joint"

HAnimHumanoid42.joints.append(HAnimJoint1519)
HAnimSegment1520 = x3d.HAnimSegment()
HAnimSegment1520.USE = "STD_Segment_l_eyelid"

HAnimHumanoid42.segments.append(HAnimSegment1520)
HAnimJoint1521 = x3d.HAnimJoint()
HAnimJoint1521.USE = "STD_Joint_r_eyelid_joint"

HAnimHumanoid42.joints.append(HAnimJoint1521)
HAnimSegment1522 = x3d.HAnimSegment()
HAnimSegment1522.USE = "STD_Segment_r_eyelid"

HAnimHumanoid42.segments.append(HAnimSegment1522)
HAnimJoint1523 = x3d.HAnimJoint()
HAnimJoint1523.USE = "STD_Joint_l_eyeball_joint"

HAnimHumanoid42.joints.append(HAnimJoint1523)
HAnimSegment1524 = x3d.HAnimSegment()
HAnimSegment1524.USE = "STD_Segment_l_eyeball"

HAnimHumanoid42.segments.append(HAnimSegment1524)
HAnimJoint1525 = x3d.HAnimJoint()
HAnimJoint1525.USE = "STD_Joint_r_eyeball_joint"

HAnimHumanoid42.joints.append(HAnimJoint1525)
HAnimSegment1526 = x3d.HAnimSegment()
HAnimSegment1526.USE = "STD_Segment_r_eyeball"

HAnimHumanoid42.segments.append(HAnimSegment1526)
HAnimJoint1527 = x3d.HAnimJoint()
HAnimJoint1527.USE = "STD_Joint_l_eyebrow_joint"

HAnimHumanoid42.joints.append(HAnimJoint1527)
HAnimSegment1528 = x3d.HAnimSegment()
HAnimSegment1528.USE = "STD_Segment_l_eyebrow"

HAnimHumanoid42.segments.append(HAnimSegment1528)
HAnimJoint1529 = x3d.HAnimJoint()
HAnimJoint1529.USE = "STD_Joint_r_eyebrow_joint"

HAnimHumanoid42.joints.append(HAnimJoint1529)
HAnimSegment1530 = x3d.HAnimSegment()
HAnimSegment1530.USE = "STD_Segment_r_eyebrow"

HAnimHumanoid42.segments.append(HAnimSegment1530)
HAnimJoint1531 = x3d.HAnimJoint()
HAnimJoint1531.USE = "STD_Joint_temporomandibular"

HAnimHumanoid42.joints.append(HAnimJoint1531)
HAnimSite1532 = x3d.HAnimSite()
HAnimSite1532.USE = "STD_Site_l_gonion_pt"

HAnimHumanoid42.sites.append(HAnimSite1532)
HAnimSite1533 = x3d.HAnimSite()
HAnimSite1533.USE = "STD_Site_menton_pt"

HAnimHumanoid42.sites.append(HAnimSite1533)
HAnimSite1534 = x3d.HAnimSite()
HAnimSite1534.USE = "STD_Site_r_gonion_pt"

HAnimHumanoid42.sites.append(HAnimSite1534)
HAnimSite1535 = x3d.HAnimSite()
HAnimSite1535.USE = "STD_Site_supramenton_pt"

HAnimHumanoid42.sites.append(HAnimSite1535)
HAnimSegment1536 = x3d.HAnimSegment()
HAnimSegment1536.USE = "STD_Segment_jaw"

HAnimHumanoid42.segments.append(HAnimSegment1536)
HAnimJoint1537 = x3d.HAnimJoint()
HAnimJoint1537.USE = "STD_Joint_l_sternoclavicular"

HAnimHumanoid42.joints.append(HAnimJoint1537)
HAnimSite1538 = x3d.HAnimSite()
HAnimSite1538.USE = "STD_Site_l_acromion_pt"

HAnimHumanoid42.sites.append(HAnimSite1538)
HAnimSite1539 = x3d.HAnimSite()
HAnimSite1539.USE = "STD_Site_l_axilla_distal_pt"

HAnimHumanoid42.sites.append(HAnimSite1539)
HAnimSite1540 = x3d.HAnimSite()
HAnimSite1540.USE = "STD_Site_l_axilla_posterior_folds_pt"

HAnimHumanoid42.sites.append(HAnimSite1540)
HAnimSite1541 = x3d.HAnimSite()
HAnimSite1541.USE = "STD_Site_l_axilla_proximal_pt"

HAnimHumanoid42.sites.append(HAnimSite1541)
HAnimSite1542 = x3d.HAnimSite()
HAnimSite1542.USE = "STD_Site_l_clavicale_pt"

HAnimHumanoid42.sites.append(HAnimSite1542)
HAnimSegment1543 = x3d.HAnimSegment()
HAnimSegment1543.USE = "STD_Segment_l_clavicle"

HAnimHumanoid42.segments.append(HAnimSegment1543)
HAnimJoint1544 = x3d.HAnimJoint()
HAnimJoint1544.USE = "STD_Joint_l_acromioclavicular"

HAnimHumanoid42.joints.append(HAnimJoint1544)
HAnimSegment1545 = x3d.HAnimSegment()
HAnimSegment1545.USE = "STD_Segment_l_scapula"

HAnimHumanoid42.segments.append(HAnimSegment1545)
HAnimJoint1546 = x3d.HAnimJoint()
HAnimJoint1546.USE = "STD_Joint_l_shoulder"

HAnimHumanoid42.joints.append(HAnimJoint1546)
HAnimSite1547 = x3d.HAnimSite()
HAnimSite1547.USE = "STD_Site_l_bideltoid_pt"

HAnimHumanoid42.sites.append(HAnimSite1547)
HAnimSite1548 = x3d.HAnimSite()
HAnimSite1548.USE = "STD_Site_l_humeral_lateral_epicondyles_pt"

HAnimHumanoid42.sites.append(HAnimSite1548)
HAnimSegment1549 = x3d.HAnimSegment()
HAnimSegment1549.USE = "STD_Segment_l_upperarm"

HAnimHumanoid42.segments.append(HAnimSegment1549)
HAnimJoint1550 = x3d.HAnimJoint()
HAnimJoint1550.USE = "STD_Joint_l_elbow"

HAnimHumanoid42.joints.append(HAnimJoint1550)
HAnimSite1551 = x3d.HAnimSite()
HAnimSite1551.USE = "STD_Site_l_humeral_medial_epicondyles_pt"

HAnimHumanoid42.sites.append(HAnimSite1551)
HAnimSite1552 = x3d.HAnimSite()
HAnimSite1552.USE = "STD_Site_l_olecranon_pt"

HAnimHumanoid42.sites.append(HAnimSite1552)
HAnimSite1553 = x3d.HAnimSite()
HAnimSite1553.USE = "STD_Site_l_radial_styloid_pt"

HAnimHumanoid42.sites.append(HAnimSite1553)
HAnimSite1554 = x3d.HAnimSite()
HAnimSite1554.USE = "STD_Site_l_radiale_pt"

HAnimHumanoid42.sites.append(HAnimSite1554)
HAnimSegment1555 = x3d.HAnimSegment()
HAnimSegment1555.USE = "STD_Segment_l_forearm"

HAnimHumanoid42.segments.append(HAnimSegment1555)
HAnimJoint1556 = x3d.HAnimJoint()
HAnimJoint1556.USE = "STD_Joint_l_radiocarpal"

HAnimHumanoid42.joints.append(HAnimJoint1556)
HAnimSite1557 = x3d.HAnimSite()
HAnimSite1557.USE = "STD_Site_l_ulnar_styloid_pt"

HAnimHumanoid42.sites.append(HAnimSite1557)
HAnimSegment1558 = x3d.HAnimSegment()
HAnimSegment1558.USE = "STD_Segment_l_carpal"

HAnimHumanoid42.segments.append(HAnimSegment1558)
HAnimJoint1559 = x3d.HAnimJoint()
HAnimJoint1559.USE = "STD_Joint_l_midcarpal_1"

HAnimHumanoid42.joints.append(HAnimJoint1559)
HAnimSegment1560 = x3d.HAnimSegment()
HAnimSegment1560.USE = "STD_Segment_l_trapezium"

HAnimHumanoid42.segments.append(HAnimSegment1560)
HAnimJoint1561 = x3d.HAnimJoint()
HAnimJoint1561.USE = "STD_Joint_l_carpometacarpal_1"

HAnimHumanoid42.joints.append(HAnimJoint1561)
HAnimSegment1562 = x3d.HAnimSegment()
HAnimSegment1562.USE = "STD_Segment_l_metacarpal_1"

HAnimHumanoid42.segments.append(HAnimSegment1562)
HAnimJoint1563 = x3d.HAnimJoint()
HAnimJoint1563.USE = "STD_Joint_l_metacarpophalangeal_1"

HAnimHumanoid42.joints.append(HAnimJoint1563)
HAnimSegment1564 = x3d.HAnimSegment()
HAnimSegment1564.USE = "STD_Segment_l_carpal_proximal_phalanx_1"

HAnimHumanoid42.segments.append(HAnimSegment1564)
HAnimJoint1565 = x3d.HAnimJoint()
HAnimJoint1565.USE = "STD_Joint_l_carpal_interphalangeal_1"

HAnimHumanoid42.joints.append(HAnimJoint1565)
HAnimSite1566 = x3d.HAnimSite()
HAnimSite1566.USE = "STD_Site_l_carpal_distal_phalanx_1_tip"

HAnimHumanoid42.sites.append(HAnimSite1566)
HAnimSegment1567 = x3d.HAnimSegment()
HAnimSegment1567.USE = "STD_Segment_l_carpal_distal_phalanx_1"

HAnimHumanoid42.segments.append(HAnimSegment1567)
HAnimJoint1568 = x3d.HAnimJoint()
HAnimJoint1568.USE = "STD_Joint_l_midcarpal_2"

HAnimHumanoid42.joints.append(HAnimJoint1568)
HAnimSegment1569 = x3d.HAnimSegment()
HAnimSegment1569.USE = "STD_Segment_l_trapezoid"

HAnimHumanoid42.segments.append(HAnimSegment1569)
HAnimJoint1570 = x3d.HAnimJoint()
HAnimJoint1570.USE = "STD_Joint_l_carpometacarpal_2"

HAnimHumanoid42.joints.append(HAnimJoint1570)
HAnimSite1571 = x3d.HAnimSite()
HAnimSite1571.USE = "STD_Site_l_metacarpal_phalanx_2_pt"

HAnimHumanoid42.sites.append(HAnimSite1571)
HAnimSegment1572 = x3d.HAnimSegment()
HAnimSegment1572.USE = "STD_Segment_l_metacarpal_2"

HAnimHumanoid42.segments.append(HAnimSegment1572)
HAnimJoint1573 = x3d.HAnimJoint()
HAnimJoint1573.USE = "STD_Joint_l_metacarpophalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint1573)
HAnimSegment1574 = x3d.HAnimSegment()
HAnimSegment1574.USE = "STD_Segment_l_carpal_proximal_phalanx_2 "

HAnimHumanoid42.segments.append(HAnimSegment1574)
HAnimJoint1575 = x3d.HAnimJoint()
HAnimJoint1575.USE = "STD_Joint_l_carpal_proximal_interphalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint1575)
HAnimSegment1576 = x3d.HAnimSegment()
HAnimSegment1576.USE = "STD_Segment_l_carpal_middle_phalanx_2"

HAnimHumanoid42.segments.append(HAnimSegment1576)
HAnimJoint1577 = x3d.HAnimJoint()
HAnimJoint1577.USE = "STD_Joint_l_carpal_distal_interphalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint1577)
HAnimSite1578 = x3d.HAnimSite()
HAnimSite1578.USE = "STD_Site_l_carpal_distal_phalanx_2_tip"

HAnimHumanoid42.sites.append(HAnimSite1578)
HAnimSite1579 = x3d.HAnimSite()
HAnimSite1579.USE = "STD_Site_l_dactylion_pt"

HAnimHumanoid42.sites.append(HAnimSite1579)
HAnimSegment1580 = x3d.HAnimSegment()
HAnimSegment1580.USE = "STD_Segment_l_carpal_distal_phalanx_2"

HAnimHumanoid42.segments.append(HAnimSegment1580)
HAnimJoint1581 = x3d.HAnimJoint()
HAnimJoint1581.USE = "STD_Joint_l_midcarpal_3"

HAnimHumanoid42.joints.append(HAnimJoint1581)
HAnimSegment1582 = x3d.HAnimSegment()
HAnimSegment1582.USE = "STD_Segment_l_capitate"

HAnimHumanoid42.segments.append(HAnimSegment1582)
HAnimJoint1583 = x3d.HAnimJoint()
HAnimJoint1583.USE = "STD_Joint_l_carpometacarpal_3"

HAnimHumanoid42.joints.append(HAnimJoint1583)
HAnimSite1584 = x3d.HAnimSite()
HAnimSite1584.USE = "STD_Site_l_metacarpal_phalanx_3_pt"

HAnimHumanoid42.sites.append(HAnimSite1584)
HAnimSegment1585 = x3d.HAnimSegment()
HAnimSegment1585.USE = "STD_Segment_l_metacarpal_3"

HAnimHumanoid42.segments.append(HAnimSegment1585)
HAnimJoint1586 = x3d.HAnimJoint()
HAnimJoint1586.USE = "STD_Joint_l_metacarpophalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint1586)
HAnimSegment1587 = x3d.HAnimSegment()
HAnimSegment1587.USE = "STD_Segment_l_carpal_proximal_phalanx_3"

HAnimHumanoid42.segments.append(HAnimSegment1587)
HAnimJoint1588 = x3d.HAnimJoint()
HAnimJoint1588.USE = "STD_Joint_l_carpal_proximal_interphalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint1588)
HAnimSegment1589 = x3d.HAnimSegment()
HAnimSegment1589.USE = "STD_Segment_l_carpal_middle_phalanx_3"

HAnimHumanoid42.segments.append(HAnimSegment1589)
HAnimJoint1590 = x3d.HAnimJoint()
HAnimJoint1590.USE = "STD_Joint_l_carpal_distal_interphalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint1590)
HAnimSite1591 = x3d.HAnimSite()
HAnimSite1591.USE = "STD_Site_l_carpal_distal_phalanx_3_tip"

HAnimHumanoid42.sites.append(HAnimSite1591)
HAnimSegment1592 = x3d.HAnimSegment()
HAnimSegment1592.USE = "STD_Segment_l_carpal_distal_phalanx_3"

HAnimHumanoid42.segments.append(HAnimSegment1592)
HAnimJoint1593 = x3d.HAnimJoint()
HAnimJoint1593.USE = "STD_Joint_l_midcarpal_4_5"

HAnimHumanoid42.joints.append(HAnimJoint1593)
HAnimSegment1594 = x3d.HAnimSegment()
HAnimSegment1594.USE = "STD_Segment_l_hamate"

HAnimHumanoid42.segments.append(HAnimSegment1594)
HAnimJoint1595 = x3d.HAnimJoint()
HAnimJoint1595.USE = "STD_Joint_l_carpometacarpal_4"

HAnimHumanoid42.joints.append(HAnimJoint1595)
HAnimSegment1596 = x3d.HAnimSegment()
HAnimSegment1596.USE = "STD_Segment_l_metacarpal_4"

HAnimHumanoid42.segments.append(HAnimSegment1596)
HAnimJoint1597 = x3d.HAnimJoint()
HAnimJoint1597.USE = "STD_Joint_l_metacarpophalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint1597)
HAnimSegment1598 = x3d.HAnimSegment()
HAnimSegment1598.USE = "STD_Segment_l_carpal_proximal_phalanx_4"

HAnimHumanoid42.segments.append(HAnimSegment1598)
HAnimJoint1599 = x3d.HAnimJoint()
HAnimJoint1599.USE = "STD_Joint_l_carpal_proximal_interphalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint1599)
HAnimSegment1600 = x3d.HAnimSegment()
HAnimSegment1600.USE = "STD_Segment_l_carpal_middle_phalanx_4"

HAnimHumanoid42.segments.append(HAnimSegment1600)
HAnimJoint1601 = x3d.HAnimJoint()
HAnimJoint1601.USE = "STD_Joint_l_carpal_distal_interphalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint1601)
HAnimSite1602 = x3d.HAnimSite()
HAnimSite1602.USE = "STD_Site_l_carpal_distal_phalanx_4_tip"

HAnimHumanoid42.sites.append(HAnimSite1602)
HAnimSegment1603 = x3d.HAnimSegment()
HAnimSegment1603.USE = "STD_Segment_l_carpal_distal_phalanx_4"

HAnimHumanoid42.segments.append(HAnimSegment1603)
HAnimJoint1604 = x3d.HAnimJoint()
HAnimJoint1604.USE = "STD_Joint_l_carpometacarpal_5"

HAnimHumanoid42.joints.append(HAnimJoint1604)
HAnimSite1605 = x3d.HAnimSite()
HAnimSite1605.USE = "STD_Site_l_metacarpal_phalanx_5_pt"

HAnimHumanoid42.sites.append(HAnimSite1605)
HAnimSegment1606 = x3d.HAnimSegment()
HAnimSegment1606.USE = "STD_Segment_l_metacarpal_5"

HAnimHumanoid42.segments.append(HAnimSegment1606)
HAnimJoint1607 = x3d.HAnimJoint()
HAnimJoint1607.USE = "STD_Joint_l_metacarpophalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint1607)
HAnimSegment1608 = x3d.HAnimSegment()
HAnimSegment1608.USE = "STD_Segment_l_carpal_proximal_phalanx_5"

HAnimHumanoid42.segments.append(HAnimSegment1608)
HAnimJoint1609 = x3d.HAnimJoint()
HAnimJoint1609.USE = "STD_Joint_l_carpal_proximal_interphalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint1609)
HAnimSegment1610 = x3d.HAnimSegment()
HAnimSegment1610.USE = "STD_Segment_l_carpal_middle_phalanx_5"

HAnimHumanoid42.segments.append(HAnimSegment1610)
HAnimJoint1611 = x3d.HAnimJoint()
HAnimJoint1611.USE = "STD_Joint_l_carpal_distal_interphalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint1611)
HAnimSite1612 = x3d.HAnimSite()
HAnimSite1612.USE = "STD_Site_l_carpal_distal_phalanx_5_tip"

HAnimHumanoid42.sites.append(HAnimSite1612)
HAnimSegment1613 = x3d.HAnimSegment()
HAnimSegment1613.USE = "STD_Segment_l_carpal_distal_phalanx_5"

HAnimHumanoid42.segments.append(HAnimSegment1613)
HAnimJoint1614 = x3d.HAnimJoint()
HAnimJoint1614.USE = "STD_Joint_r_sternoclavicular"

HAnimHumanoid42.joints.append(HAnimJoint1614)
HAnimSite1615 = x3d.HAnimSite()
HAnimSite1615.USE = "STD_Site_r_acromion_pt"

HAnimHumanoid42.sites.append(HAnimSite1615)
HAnimSite1616 = x3d.HAnimSite()
HAnimSite1616.USE = "STD_Site_r_axilla_distal_pt"

HAnimHumanoid42.sites.append(HAnimSite1616)
HAnimSite1617 = x3d.HAnimSite()
HAnimSite1617.USE = "STD_Site_r_axilla_posterior_folds_pt"

HAnimHumanoid42.sites.append(HAnimSite1617)
HAnimSite1618 = x3d.HAnimSite()
HAnimSite1618.USE = "STD_Site_r_axilla_proximal_pt"

HAnimHumanoid42.sites.append(HAnimSite1618)
HAnimSite1619 = x3d.HAnimSite()
HAnimSite1619.USE = "STD_Site_r_clavicale_pt"

HAnimHumanoid42.sites.append(HAnimSite1619)
HAnimSegment1620 = x3d.HAnimSegment()
HAnimSegment1620.USE = "STD_Segment_r_clavicle"

HAnimHumanoid42.segments.append(HAnimSegment1620)
HAnimJoint1621 = x3d.HAnimJoint()
HAnimJoint1621.USE = "STD_Joint_r_acromioclavicular"

HAnimHumanoid42.joints.append(HAnimJoint1621)
HAnimSegment1622 = x3d.HAnimSegment()
HAnimSegment1622.USE = "STD_Segment_r_scapula"

HAnimHumanoid42.segments.append(HAnimSegment1622)
HAnimJoint1623 = x3d.HAnimJoint()
HAnimJoint1623.USE = "STD_Joint_r_shoulder"

HAnimHumanoid42.joints.append(HAnimJoint1623)
HAnimSite1624 = x3d.HAnimSite()
HAnimSite1624.USE = "STD_Site_r_bideltoid_pt"

HAnimHumanoid42.sites.append(HAnimSite1624)
HAnimSite1625 = x3d.HAnimSite()
HAnimSite1625.USE = "STD_Site_r_humeral_lateral_epicondyles_pt"

HAnimHumanoid42.sites.append(HAnimSite1625)
HAnimSegment1626 = x3d.HAnimSegment()
HAnimSegment1626.USE = "STD_Segment_r_upperarm"

HAnimHumanoid42.segments.append(HAnimSegment1626)
HAnimJoint1627 = x3d.HAnimJoint()
HAnimJoint1627.USE = "STD_Joint_r_elbow"

HAnimHumanoid42.joints.append(HAnimJoint1627)
HAnimSite1628 = x3d.HAnimSite()
HAnimSite1628.USE = "STD_Site_r_humeral_medial_epicondyles_pt"

HAnimHumanoid42.sites.append(HAnimSite1628)
HAnimSite1629 = x3d.HAnimSite()
HAnimSite1629.USE = "STD_Site_r_olecranon_pt"

HAnimHumanoid42.sites.append(HAnimSite1629)
HAnimSite1630 = x3d.HAnimSite()
HAnimSite1630.USE = "STD_Site_r_radial_styloid_pt"

HAnimHumanoid42.sites.append(HAnimSite1630)
HAnimSite1631 = x3d.HAnimSite()
HAnimSite1631.USE = "STD_Site_r_radiale_pt"

HAnimHumanoid42.sites.append(HAnimSite1631)
HAnimSegment1632 = x3d.HAnimSegment()
HAnimSegment1632.USE = "STD_Segment_r_forearm"

HAnimHumanoid42.segments.append(HAnimSegment1632)
HAnimJoint1633 = x3d.HAnimJoint()
HAnimJoint1633.USE = "STD_Joint_r_radiocarpal"

HAnimHumanoid42.joints.append(HAnimJoint1633)
HAnimSite1634 = x3d.HAnimSite()
HAnimSite1634.USE = "STD_Site_r_ulnar_styloid_pt"

HAnimHumanoid42.sites.append(HAnimSite1634)
HAnimSegment1635 = x3d.HAnimSegment()
HAnimSegment1635.USE = "STD_Segment_r_carpal"

HAnimHumanoid42.segments.append(HAnimSegment1635)
HAnimJoint1636 = x3d.HAnimJoint()
HAnimJoint1636.USE = "STD_Joint_r_midcarpal_1"

HAnimHumanoid42.joints.append(HAnimJoint1636)
HAnimSegment1637 = x3d.HAnimSegment()
HAnimSegment1637.USE = "STD_Segment_r_trapezium"

HAnimHumanoid42.segments.append(HAnimSegment1637)
HAnimJoint1638 = x3d.HAnimJoint()
HAnimJoint1638.USE = "STD_Joint_r_carpometacarpal_1"

HAnimHumanoid42.joints.append(HAnimJoint1638)
HAnimSegment1639 = x3d.HAnimSegment()
HAnimSegment1639.USE = "STD_Segment_r_metacarpal_1"

HAnimHumanoid42.segments.append(HAnimSegment1639)
HAnimJoint1640 = x3d.HAnimJoint()
HAnimJoint1640.USE = "STD_Joint_r_metacarpophalangeal_1"

HAnimHumanoid42.joints.append(HAnimJoint1640)
HAnimSegment1641 = x3d.HAnimSegment()
HAnimSegment1641.USE = "STD_Segment_r_carpal_proximal_phalanx_1"

HAnimHumanoid42.segments.append(HAnimSegment1641)
HAnimJoint1642 = x3d.HAnimJoint()
HAnimJoint1642.USE = "STD_Joint_r_carpal_interphalangeal_1"

HAnimHumanoid42.joints.append(HAnimJoint1642)
HAnimSite1643 = x3d.HAnimSite()
HAnimSite1643.USE = "STD_Site_r_carpal_distal_phalanx_1_tip"

HAnimHumanoid42.sites.append(HAnimSite1643)
HAnimSegment1644 = x3d.HAnimSegment()
HAnimSegment1644.USE = "STD_Segment_r_carpal_distal_phalanx_1"

HAnimHumanoid42.segments.append(HAnimSegment1644)
HAnimJoint1645 = x3d.HAnimJoint()
HAnimJoint1645.USE = "STD_Joint_r_midcarpal_2"

HAnimHumanoid42.joints.append(HAnimJoint1645)
HAnimSegment1646 = x3d.HAnimSegment()
HAnimSegment1646.USE = "STD_Segment_r_trapezoid"

HAnimHumanoid42.segments.append(HAnimSegment1646)
HAnimJoint1647 = x3d.HAnimJoint()
HAnimJoint1647.USE = "STD_Joint_r_carpometacarpal_2"

HAnimHumanoid42.joints.append(HAnimJoint1647)
HAnimSite1648 = x3d.HAnimSite()
HAnimSite1648.USE = "STD_Site_r_metacarpal_phalanx_2_pt"

HAnimHumanoid42.sites.append(HAnimSite1648)
HAnimSegment1649 = x3d.HAnimSegment()
HAnimSegment1649.USE = "STD_Segment_r_metacarpal_2"

HAnimHumanoid42.segments.append(HAnimSegment1649)
HAnimJoint1650 = x3d.HAnimJoint()
HAnimJoint1650.USE = "STD_Joint_r_metacarpophalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint1650)
HAnimSegment1651 = x3d.HAnimSegment()
HAnimSegment1651.USE = "STD_Segment_r_carpal_proximal_phalanx_2 "

HAnimHumanoid42.segments.append(HAnimSegment1651)
HAnimJoint1652 = x3d.HAnimJoint()
HAnimJoint1652.USE = "STD_Joint_r_carpal_proximal_interphalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint1652)
HAnimSegment1653 = x3d.HAnimSegment()
HAnimSegment1653.USE = "STD_Segment_r_carpal_middle_phalanx_2"

HAnimHumanoid42.segments.append(HAnimSegment1653)
HAnimJoint1654 = x3d.HAnimJoint()
HAnimJoint1654.USE = "STD_Joint_r_carpal_distal_interphalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint1654)
HAnimSite1655 = x3d.HAnimSite()
HAnimSite1655.USE = "STD_Site_r_carpal_distal_phalanx_2_tip"

HAnimHumanoid42.sites.append(HAnimSite1655)
HAnimSite1656 = x3d.HAnimSite()
HAnimSite1656.USE = "STD_Site_r_dactylion_pt"

HAnimHumanoid42.sites.append(HAnimSite1656)
HAnimSegment1657 = x3d.HAnimSegment()
HAnimSegment1657.USE = "STD_Segment_r_carpal_distal_phalanx_2"

HAnimHumanoid42.segments.append(HAnimSegment1657)
HAnimJoint1658 = x3d.HAnimJoint()
HAnimJoint1658.USE = "STD_Joint_r_midcarpal_3"

HAnimHumanoid42.joints.append(HAnimJoint1658)
HAnimSegment1659 = x3d.HAnimSegment()
HAnimSegment1659.USE = "STD_Segment_r_capitate"

HAnimHumanoid42.segments.append(HAnimSegment1659)
HAnimJoint1660 = x3d.HAnimJoint()
HAnimJoint1660.USE = "STD_Joint_r_carpometacarpal_3"

HAnimHumanoid42.joints.append(HAnimJoint1660)
HAnimSite1661 = x3d.HAnimSite()
HAnimSite1661.USE = "STD_Site_r_metacarpal_phalanx_3_pt"

HAnimHumanoid42.sites.append(HAnimSite1661)
HAnimSegment1662 = x3d.HAnimSegment()
HAnimSegment1662.USE = "STD_Segment_r_metacarpal_3"

HAnimHumanoid42.segments.append(HAnimSegment1662)
HAnimJoint1663 = x3d.HAnimJoint()
HAnimJoint1663.USE = "STD_Joint_r_metacarpophalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint1663)
HAnimSegment1664 = x3d.HAnimSegment()
HAnimSegment1664.USE = "STD_Segment_r_carpal_proximal_phalanx_3"

HAnimHumanoid42.segments.append(HAnimSegment1664)
HAnimJoint1665 = x3d.HAnimJoint()
HAnimJoint1665.USE = "STD_Joint_r_carpal_proximal_interphalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint1665)
HAnimSegment1666 = x3d.HAnimSegment()
HAnimSegment1666.USE = "STD_Segment_r_carpal_middle_phalanx_3"

HAnimHumanoid42.segments.append(HAnimSegment1666)
HAnimJoint1667 = x3d.HAnimJoint()
HAnimJoint1667.USE = "STD_Joint_r_carpal_distal_interphalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint1667)
HAnimSite1668 = x3d.HAnimSite()
HAnimSite1668.USE = "STD_Site_r_carpal_distal_phalanx_3_tip"

HAnimHumanoid42.sites.append(HAnimSite1668)
HAnimSegment1669 = x3d.HAnimSegment()
HAnimSegment1669.USE = "STD_Segment_r_carpal_distal_phalanx_3"

HAnimHumanoid42.segments.append(HAnimSegment1669)
HAnimJoint1670 = x3d.HAnimJoint()
HAnimJoint1670.USE = "STD_Joint_r_midcarpal_4_5"

HAnimHumanoid42.joints.append(HAnimJoint1670)
HAnimSegment1671 = x3d.HAnimSegment()
HAnimSegment1671.USE = "STD_Segment_r_hamate"

HAnimHumanoid42.segments.append(HAnimSegment1671)
HAnimJoint1672 = x3d.HAnimJoint()
HAnimJoint1672.USE = "STD_Joint_r_carpometacarpal_4"

HAnimHumanoid42.joints.append(HAnimJoint1672)
HAnimSegment1673 = x3d.HAnimSegment()
HAnimSegment1673.USE = "STD_Segment_r_metacarpal_4"

HAnimHumanoid42.segments.append(HAnimSegment1673)
HAnimJoint1674 = x3d.HAnimJoint()
HAnimJoint1674.USE = "STD_Joint_r_metacarpophalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint1674)
HAnimSegment1675 = x3d.HAnimSegment()
HAnimSegment1675.USE = "STD_Segment_r_carpal_proximal_phalanx_4"

HAnimHumanoid42.segments.append(HAnimSegment1675)
HAnimJoint1676 = x3d.HAnimJoint()
HAnimJoint1676.USE = "STD_Joint_r_carpal_proximal_interphalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint1676)
HAnimSegment1677 = x3d.HAnimSegment()
HAnimSegment1677.USE = "STD_Segment_r_carpal_middle_phalanx_4"

HAnimHumanoid42.segments.append(HAnimSegment1677)
HAnimJoint1678 = x3d.HAnimJoint()
HAnimJoint1678.USE = "STD_Joint_r_carpal_distal_interphalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint1678)
HAnimSite1679 = x3d.HAnimSite()
HAnimSite1679.USE = "STD_Site_r_carpal_distal_phalanx_4_tip"

HAnimHumanoid42.sites.append(HAnimSite1679)
HAnimSegment1680 = x3d.HAnimSegment()
HAnimSegment1680.USE = "STD_Segment_r_carpal_distal_phalanx_4"

HAnimHumanoid42.segments.append(HAnimSegment1680)
HAnimJoint1681 = x3d.HAnimJoint()
HAnimJoint1681.USE = "STD_Joint_r_carpometacarpal_5"

HAnimHumanoid42.joints.append(HAnimJoint1681)
HAnimSite1682 = x3d.HAnimSite()
HAnimSite1682.USE = "STD_Site_r_metacarpal_phalanx_5_pt"

HAnimHumanoid42.sites.append(HAnimSite1682)
HAnimSegment1683 = x3d.HAnimSegment()
HAnimSegment1683.USE = "STD_Segment_r_metacarpal_5"

HAnimHumanoid42.segments.append(HAnimSegment1683)
HAnimJoint1684 = x3d.HAnimJoint()
HAnimJoint1684.USE = "STD_Joint_r_metacarpophalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint1684)
HAnimSegment1685 = x3d.HAnimSegment()
HAnimSegment1685.USE = "STD_Segment_r_carpal_proximal_phalanx_5"

HAnimHumanoid42.segments.append(HAnimSegment1685)
HAnimJoint1686 = x3d.HAnimJoint()
HAnimJoint1686.USE = "STD_Joint_r_carpal_proximal_interphalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint1686)
HAnimSegment1687 = x3d.HAnimSegment()
HAnimSegment1687.USE = "STD_Segment_r_carpal_middle_phalanx_5"

HAnimHumanoid42.segments.append(HAnimSegment1687)
HAnimJoint1688 = x3d.HAnimJoint()
HAnimJoint1688.USE = "STD_Joint_r_carpal_distal_interphalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint1688)
HAnimSite1689 = x3d.HAnimSite()
HAnimSite1689.USE = "STD_Site_r_carpal_distal_phalanx_5_tip"

HAnimHumanoid42.sites.append(HAnimSite1689)
HAnimSegment1690 = x3d.HAnimSegment()
HAnimSegment1690.USE = "STD_Segment_r_carpal_distal_phalanx_5"

HAnimHumanoid42.segments.append(HAnimSegment1690)

HAnimHumanoid10.skeleton.append(HAnimHumanoid10)

X3D0.Scene = Scene10
f = open("skeleton1_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
