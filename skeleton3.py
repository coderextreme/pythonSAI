print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Immersive"
X3D0.version = "4.0"
head1 = x3d.head()
component2 = x3d.component()
component2.level = 1
component2.name = "H-Anim"

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
HAnimJoint145.center = [0,1,0]
HAnimSegment146 = x3d.HAnimSegment()
HAnimSegment146.DEF = "STD_Segment_l_navicular"
HAnimSegment146.name = "l_navicular"
Transform147 = x3d.Transform()
Transform147.translation = [0,1,0]
Shape148 = x3d.Shape()
Shape148.USE = "HAnimJointShape"

Transform147.children.append(Shape148)

HAnimSegment146.children.append(Transform147)
Transform149 = x3d.Transform()
Shape150 = x3d.Shape()
LineSet151 = x3d.LineSet()
LineSet151.vertexCount = [2]
Coordinate152 = x3d.Coordinate()

LineSet151.coord = Coordinate152
ColorRGBA153 = x3d.ColorRGBA()
ColorRGBA153.USE = "HAnimSegmentLineColorRGBA"

LineSet151.color = ColorRGBA153

Shape150.geometry = LineSet151

Transform149.children.append(Shape150)

HAnimSegment146.children.append(Transform149)

HAnimJoint145.children.append(HAnimSegment146)
HAnimJoint154 = x3d.HAnimJoint()
HAnimJoint154.DEF = "STD_Joint_l_cuneonavicular_1"
HAnimJoint154.name = "l_cuneonavicular_1"
HAnimJoint154.center = [0,1,0]
HAnimSegment155 = x3d.HAnimSegment()
HAnimSegment155.DEF = "STD_Segment_l_cuneiform_1"
HAnimSegment155.name = "l_cuneiform_1"
Transform156 = x3d.Transform()
Transform156.translation = [0,1,0]
Shape157 = x3d.Shape()
Shape157.USE = "HAnimJointShape"

Transform156.children.append(Shape157)

HAnimSegment155.children.append(Transform156)
Transform158 = x3d.Transform()
Shape159 = x3d.Shape()
LineSet160 = x3d.LineSet()
LineSet160.vertexCount = [2]
Coordinate161 = x3d.Coordinate()

LineSet160.coord = Coordinate161
ColorRGBA162 = x3d.ColorRGBA()
ColorRGBA162.USE = "HAnimSegmentLineColorRGBA"

LineSet160.color = ColorRGBA162

Shape159.geometry = LineSet160

Transform158.children.append(Shape159)

HAnimSegment155.children.append(Transform158)

HAnimJoint154.children.append(HAnimSegment155)
HAnimJoint163 = x3d.HAnimJoint()
HAnimJoint163.DEF = "STD_Joint_l_tarsometatarsal_1"
HAnimJoint163.name = "l_tarsometatarsal_1"
HAnimJoint163.center = [0,1,0]
HAnimSegment164 = x3d.HAnimSegment()
HAnimSegment164.DEF = "STD_Segment_l_metatarsal_1"
HAnimSegment164.name = "l_metatarsal_1"
Transform165 = x3d.Transform()
Transform165.translation = [0,1,0]
Shape166 = x3d.Shape()
Shape166.USE = "HAnimJointShape"

Transform165.children.append(Shape166)

HAnimSegment164.children.append(Transform165)
Transform167 = x3d.Transform()
Shape168 = x3d.Shape()
LineSet169 = x3d.LineSet()
LineSet169.vertexCount = [2]
Coordinate170 = x3d.Coordinate()

LineSet169.coord = Coordinate170
ColorRGBA171 = x3d.ColorRGBA()
ColorRGBA171.USE = "HAnimSegmentLineColorRGBA"

LineSet169.color = ColorRGBA171

Shape168.geometry = LineSet169

Transform167.children.append(Shape168)

HAnimSegment164.children.append(Transform167)

HAnimJoint163.children.append(HAnimSegment164)
HAnimJoint172 = x3d.HAnimJoint()
HAnimJoint172.DEF = "STD_Joint_l_metatarsophalangeal_1"
HAnimJoint172.name = "l_metatarsophalangeal_1"
HAnimJoint172.center = [0,1,0]
HAnimSegment173 = x3d.HAnimSegment()
HAnimSegment173.DEF = "STD_Segment_l_tarsal_proximal_phalanx_1"
HAnimSegment173.name = "l_tarsal_proximal_phalanx_1"
Transform174 = x3d.Transform()
Transform174.translation = [0,1,0]
Shape175 = x3d.Shape()
Shape175.USE = "HAnimJointShape"

Transform174.children.append(Shape175)

HAnimSegment173.children.append(Transform174)
Transform176 = x3d.Transform()
Shape177 = x3d.Shape()
LineSet178 = x3d.LineSet()
LineSet178.vertexCount = [2]
Coordinate179 = x3d.Coordinate()

LineSet178.coord = Coordinate179
ColorRGBA180 = x3d.ColorRGBA()
ColorRGBA180.USE = "HAnimSegmentLineColorRGBA"

LineSet178.color = ColorRGBA180

Shape177.geometry = LineSet178

Transform176.children.append(Shape177)

HAnimSegment173.children.append(Transform176)
HAnimSite181 = x3d.HAnimSite()
HAnimSite181.DEF = "STD_Site_l_metatarsal_phalanx_1_pt"
HAnimSite181.name = "l_metatarsal_phalanx_1_pt"
TouchSensor182 = x3d.TouchSensor()
TouchSensor182.description = "HAnimSite l_metatarsal_phalanx_1_pt"

HAnimSite181.children.append(TouchSensor182)
Shape183 = x3d.Shape()
Shape183.USE = "HAnimSiteShape"

HAnimSite181.children.append(Shape183)

HAnimSegment173.children.append(HAnimSite181)

HAnimJoint172.children.append(HAnimSegment173)
HAnimJoint184 = x3d.HAnimJoint()
HAnimJoint184.DEF = "STD_Joint_l_tarsal_interphalangeal_1"
HAnimJoint184.name = "l_tarsal_interphalangeal_1"
HAnimJoint184.center = [0,1,0]
HAnimSegment185 = x3d.HAnimSegment()
HAnimSegment185.DEF = "STD_Segment_l_tarsal_distal_phalanx_1"
HAnimSegment185.name = "l_tarsal_distal_phalanx_1"
Transform186 = x3d.Transform()
Transform186.translation = [0,1,0]
Shape187 = x3d.Shape()
Shape187.USE = "HAnimJointShape"

Transform186.children.append(Shape187)

HAnimSegment185.children.append(Transform186)
Transform188 = x3d.Transform()
Shape189 = x3d.Shape()
LineSet190 = x3d.LineSet()
LineSet190.vertexCount = [2]
Coordinate191 = x3d.Coordinate()

LineSet190.coord = Coordinate191
ColorRGBA192 = x3d.ColorRGBA()
ColorRGBA192.USE = "HAnimSegmentLineColorRGBA"

LineSet190.color = ColorRGBA192

Shape189.geometry = LineSet190

Transform188.children.append(Shape189)

HAnimSegment185.children.append(Transform188)
HAnimSite193 = x3d.HAnimSite()
HAnimSite193.DEF = "STD_Site_l_tarsal_distal_phalanx_1_tip"
HAnimSite193.name = "l_tarsal_distal_phalanx_1_tip"
TouchSensor194 = x3d.TouchSensor()
TouchSensor194.description = "HAnimSite l_tarsal_distal_phalanx_1_tip"

HAnimSite193.children.append(TouchSensor194)
Shape195 = x3d.Shape()
Shape195.USE = "HAnimSiteShape"

HAnimSite193.children.append(Shape195)

HAnimSegment185.children.append(HAnimSite193)

HAnimJoint184.children.append(HAnimSegment185)

HAnimJoint172.children.append(HAnimJoint184)

HAnimJoint163.children.append(HAnimJoint172)

HAnimJoint154.children.append(HAnimJoint163)

HAnimJoint145.children.append(HAnimJoint154)
HAnimJoint196 = x3d.HAnimJoint()
HAnimJoint196.DEF = "STD_Joint_l_cuneonavicular_2"
HAnimJoint196.name = "l_cuneonavicular_2"
HAnimJoint196.center = [0,1,0]
HAnimSegment197 = x3d.HAnimSegment()
HAnimSegment197.DEF = "STD_Segment_l_cuneiform_2"
HAnimSegment197.name = "l_cuneiform_2"
Transform198 = x3d.Transform()
Transform198.translation = [0,1,0]
Shape199 = x3d.Shape()
Shape199.USE = "HAnimJointShape"

Transform198.children.append(Shape199)

HAnimSegment197.children.append(Transform198)
Transform200 = x3d.Transform()
Shape201 = x3d.Shape()
LineSet202 = x3d.LineSet()
LineSet202.vertexCount = [2]
Coordinate203 = x3d.Coordinate()

LineSet202.coord = Coordinate203
ColorRGBA204 = x3d.ColorRGBA()
ColorRGBA204.USE = "HAnimSegmentLineColorRGBA"

LineSet202.color = ColorRGBA204

Shape201.geometry = LineSet202

Transform200.children.append(Shape201)

HAnimSegment197.children.append(Transform200)

HAnimJoint196.children.append(HAnimSegment197)
HAnimJoint205 = x3d.HAnimJoint()
HAnimJoint205.DEF = "STD_Joint_l_tarsometatarsal_2"
HAnimJoint205.name = "l_tarsometatarsal_2"
HAnimJoint205.center = [0,1,0]
HAnimSegment206 = x3d.HAnimSegment()
HAnimSegment206.DEF = "STD_Segment_l_metatarsal_2"
HAnimSegment206.name = "l_metatarsal_2"
Transform207 = x3d.Transform()
Transform207.translation = [0,1,0]
Shape208 = x3d.Shape()
Shape208.USE = "HAnimJointShape"

Transform207.children.append(Shape208)

HAnimSegment206.children.append(Transform207)
Transform209 = x3d.Transform()
Shape210 = x3d.Shape()
LineSet211 = x3d.LineSet()
LineSet211.vertexCount = [2]
Coordinate212 = x3d.Coordinate()

LineSet211.coord = Coordinate212
ColorRGBA213 = x3d.ColorRGBA()
ColorRGBA213.USE = "HAnimSegmentLineColorRGBA"

LineSet211.color = ColorRGBA213

Shape210.geometry = LineSet211

Transform209.children.append(Shape210)

HAnimSegment206.children.append(Transform209)

HAnimJoint205.children.append(HAnimSegment206)
HAnimJoint214 = x3d.HAnimJoint()
HAnimJoint214.DEF = "STD_Joint_l_metatarsophalangeal_2"
HAnimJoint214.name = "l_metatarsophalangeal_2"
HAnimJoint214.center = [0,1,0]
HAnimSegment215 = x3d.HAnimSegment()
HAnimSegment215.DEF = "STD_Segment_l_tarsal_proximal_phalanx_2"
HAnimSegment215.name = "l_tarsal_proximal_phalanx_2"
Transform216 = x3d.Transform()
Transform216.translation = [0,1,0]
Shape217 = x3d.Shape()
Shape217.USE = "HAnimJointShape"

Transform216.children.append(Shape217)

HAnimSegment215.children.append(Transform216)
Transform218 = x3d.Transform()
Shape219 = x3d.Shape()
LineSet220 = x3d.LineSet()
LineSet220.vertexCount = [2]
Coordinate221 = x3d.Coordinate()

LineSet220.coord = Coordinate221
ColorRGBA222 = x3d.ColorRGBA()
ColorRGBA222.USE = "HAnimSegmentLineColorRGBA"

LineSet220.color = ColorRGBA222

Shape219.geometry = LineSet220

Transform218.children.append(Shape219)

HAnimSegment215.children.append(Transform218)

HAnimJoint214.children.append(HAnimSegment215)
HAnimJoint223 = x3d.HAnimJoint()
HAnimJoint223.DEF = "STD_Joint_l_tarsal_proximal_interphalangeal_2"
HAnimJoint223.name = "l_tarsal_proximal_interphalangeal_2"
HAnimJoint223.center = [0,1,0]
HAnimSegment224 = x3d.HAnimSegment()
HAnimSegment224.DEF = "STD_Segment_l_tarsal_middle_phalanx_2"
HAnimSegment224.name = "l_tarsal_middle_phalanx_2"
Transform225 = x3d.Transform()
Transform225.translation = [0,1,0]
Shape226 = x3d.Shape()
Shape226.USE = "HAnimJointShape"

Transform225.children.append(Shape226)

HAnimSegment224.children.append(Transform225)
Transform227 = x3d.Transform()
Shape228 = x3d.Shape()
LineSet229 = x3d.LineSet()
LineSet229.vertexCount = [2]
Coordinate230 = x3d.Coordinate()

LineSet229.coord = Coordinate230
ColorRGBA231 = x3d.ColorRGBA()
ColorRGBA231.USE = "HAnimSegmentLineColorRGBA"

LineSet229.color = ColorRGBA231

Shape228.geometry = LineSet229

Transform227.children.append(Shape228)

HAnimSegment224.children.append(Transform227)

HAnimJoint223.children.append(HAnimSegment224)
HAnimJoint232 = x3d.HAnimJoint()
HAnimJoint232.DEF = "STD_Joint_l_tarsal_distal_interphalangeal_2"
HAnimJoint232.name = "l_tarsal_distal_interphalangeal_2"
HAnimJoint232.center = [0,1,0]
HAnimSegment233 = x3d.HAnimSegment()
HAnimSegment233.DEF = "STD_Segment_l_tarsal_distal_phalanx_2"
HAnimSegment233.name = "l_tarsal_distal_phalanx_2"
Transform234 = x3d.Transform()
Transform234.translation = [0,1,0]
Shape235 = x3d.Shape()
Shape235.USE = "HAnimJointShape"

Transform234.children.append(Shape235)

HAnimSegment233.children.append(Transform234)
Transform236 = x3d.Transform()
Shape237 = x3d.Shape()
LineSet238 = x3d.LineSet()
LineSet238.vertexCount = [2]
Coordinate239 = x3d.Coordinate()

LineSet238.coord = Coordinate239
ColorRGBA240 = x3d.ColorRGBA()
ColorRGBA240.USE = "HAnimSegmentLineColorRGBA"

LineSet238.color = ColorRGBA240

Shape237.geometry = LineSet238

Transform236.children.append(Shape237)

HAnimSegment233.children.append(Transform236)
HAnimSite241 = x3d.HAnimSite()
HAnimSite241.DEF = "STD_Site_l_tarsal_distal_phalanx_2_tip"
HAnimSite241.name = "l_tarsal_distal_phalanx_2_tip"
HAnimSite241.translation = [0.1195,0.0079,0.1433]
TouchSensor242 = x3d.TouchSensor()
TouchSensor242.description = "HAnimSite l_tarsal_distal_phalanx_2_tip"

HAnimSite241.children.append(TouchSensor242)
Shape243 = x3d.Shape()
Shape243.USE = "HAnimSiteShape"

HAnimSite241.children.append(Shape243)

HAnimSegment233.children.append(HAnimSite241)

HAnimJoint232.children.append(HAnimSegment233)

HAnimJoint223.children.append(HAnimJoint232)

HAnimJoint214.children.append(HAnimJoint223)

HAnimJoint205.children.append(HAnimJoint214)

HAnimJoint196.children.append(HAnimJoint205)

HAnimJoint145.children.append(HAnimJoint196)
HAnimJoint244 = x3d.HAnimJoint()
HAnimJoint244.DEF = "STD_Joint_l_cuneonavicular_3"
HAnimJoint244.name = "l_cuneonavicular_3"
HAnimJoint244.center = [0,1,0]
HAnimSegment245 = x3d.HAnimSegment()
HAnimSegment245.DEF = "STD_Segment_l_cuneiform_3"
HAnimSegment245.name = "l_cuneiform_3"
Transform246 = x3d.Transform()
Transform246.translation = [0,1,0]
Shape247 = x3d.Shape()
Shape247.USE = "HAnimJointShape"

Transform246.children.append(Shape247)

HAnimSegment245.children.append(Transform246)
Transform248 = x3d.Transform()
Shape249 = x3d.Shape()
LineSet250 = x3d.LineSet()
LineSet250.vertexCount = [2]
Coordinate251 = x3d.Coordinate()

LineSet250.coord = Coordinate251
ColorRGBA252 = x3d.ColorRGBA()
ColorRGBA252.USE = "HAnimSegmentLineColorRGBA"

LineSet250.color = ColorRGBA252

Shape249.geometry = LineSet250

Transform248.children.append(Shape249)

HAnimSegment245.children.append(Transform248)

HAnimJoint244.children.append(HAnimSegment245)
HAnimJoint253 = x3d.HAnimJoint()
HAnimJoint253.DEF = "STD_Joint_l_tarsometatarsal_3 "
HAnimJoint253.name = "l_tarsometatarsal_3 "
HAnimJoint253.center = [0,1,0]
HAnimSegment254 = x3d.HAnimSegment()
HAnimSegment254.DEF = "STD_Segment_l_metatarsal_3"
HAnimSegment254.name = "l_metatarsal_3"
Transform255 = x3d.Transform()
Transform255.translation = [0,1,0]
Shape256 = x3d.Shape()
Shape256.USE = "HAnimJointShape"

Transform255.children.append(Shape256)

HAnimSegment254.children.append(Transform255)
Transform257 = x3d.Transform()
Shape258 = x3d.Shape()
LineSet259 = x3d.LineSet()
LineSet259.vertexCount = [2]
Coordinate260 = x3d.Coordinate()

LineSet259.coord = Coordinate260
ColorRGBA261 = x3d.ColorRGBA()
ColorRGBA261.USE = "HAnimSegmentLineColorRGBA"

LineSet259.color = ColorRGBA261

Shape258.geometry = LineSet259

Transform257.children.append(Shape258)

HAnimSegment254.children.append(Transform257)

HAnimJoint253.children.append(HAnimSegment254)
HAnimJoint262 = x3d.HAnimJoint()
HAnimJoint262.DEF = "STD_Joint_l_metatarsophalangeal_3"
HAnimJoint262.name = "l_metatarsophalangeal_3"
HAnimJoint262.center = [0,1,0]
HAnimSegment263 = x3d.HAnimSegment()
HAnimSegment263.DEF = "STD_Segment_l_tarsal_proximal_phalanx_3"
HAnimSegment263.name = "l_tarsal_proximal_phalanx_3"
Transform264 = x3d.Transform()
Transform264.translation = [0,1,0]
Shape265 = x3d.Shape()
Shape265.USE = "HAnimJointShape"

Transform264.children.append(Shape265)

HAnimSegment263.children.append(Transform264)
Transform266 = x3d.Transform()
Shape267 = x3d.Shape()
LineSet268 = x3d.LineSet()
LineSet268.vertexCount = [2]
Coordinate269 = x3d.Coordinate()

LineSet268.coord = Coordinate269
ColorRGBA270 = x3d.ColorRGBA()
ColorRGBA270.USE = "HAnimSegmentLineColorRGBA"

LineSet268.color = ColorRGBA270

Shape267.geometry = LineSet268

Transform266.children.append(Shape267)

HAnimSegment263.children.append(Transform266)

HAnimJoint262.children.append(HAnimSegment263)
HAnimJoint271 = x3d.HAnimJoint()
HAnimJoint271.DEF = "STD_Joint_l_tarsal_proximal_interphalangeal_3"
HAnimJoint271.name = "l_tarsal_proximal_interphalangeal_3"
HAnimJoint271.center = [0,1,0]
HAnimSegment272 = x3d.HAnimSegment()
HAnimSegment272.DEF = "STD_Segment_l_tarsal_middle_phalanx_3"
HAnimSegment272.name = "l_tarsal_middle_phalanx_3"
Transform273 = x3d.Transform()
Transform273.translation = [0,1,0]
Shape274 = x3d.Shape()
Shape274.USE = "HAnimJointShape"

Transform273.children.append(Shape274)

HAnimSegment272.children.append(Transform273)
Transform275 = x3d.Transform()
Shape276 = x3d.Shape()
LineSet277 = x3d.LineSet()
LineSet277.vertexCount = [2]
Coordinate278 = x3d.Coordinate()

LineSet277.coord = Coordinate278
ColorRGBA279 = x3d.ColorRGBA()
ColorRGBA279.USE = "HAnimSegmentLineColorRGBA"

LineSet277.color = ColorRGBA279

Shape276.geometry = LineSet277

Transform275.children.append(Shape276)

HAnimSegment272.children.append(Transform275)

HAnimJoint271.children.append(HAnimSegment272)
HAnimJoint280 = x3d.HAnimJoint()
HAnimJoint280.DEF = "STD_Joint_l_tarsal_distal_interphalangeal_3"
HAnimJoint280.name = "l_tarsal_distal_interphalangeal_3"
HAnimJoint280.center = [0,1,0]
HAnimSegment281 = x3d.HAnimSegment()
HAnimSegment281.DEF = "STD_Segment_l_tarsal_distal_phalanx_3"
HAnimSegment281.name = "l_tarsal_distal_phalanx_3"
Transform282 = x3d.Transform()
Transform282.translation = [0,1,0]
Shape283 = x3d.Shape()
Shape283.USE = "HAnimJointShape"

Transform282.children.append(Shape283)

HAnimSegment281.children.append(Transform282)
Transform284 = x3d.Transform()
Shape285 = x3d.Shape()
LineSet286 = x3d.LineSet()
LineSet286.vertexCount = [2]
Coordinate287 = x3d.Coordinate()

LineSet286.coord = Coordinate287
ColorRGBA288 = x3d.ColorRGBA()
ColorRGBA288.USE = "HAnimSegmentLineColorRGBA"

LineSet286.color = ColorRGBA288

Shape285.geometry = LineSet286

Transform284.children.append(Shape285)

HAnimSegment281.children.append(Transform284)
HAnimSite289 = x3d.HAnimSite()
HAnimSite289.DEF = "STD_Site_l_tarsal_distal_phalanx_3_tip"
HAnimSite289.name = "l_tarsal_distal_phalanx_3_tip"
TouchSensor290 = x3d.TouchSensor()
TouchSensor290.description = "HAnimSite l_tarsal_distal_phalanx_3_tip"

HAnimSite289.children.append(TouchSensor290)
Shape291 = x3d.Shape()
Shape291.USE = "HAnimSiteShape"

HAnimSite289.children.append(Shape291)

HAnimSegment281.children.append(HAnimSite289)

HAnimJoint280.children.append(HAnimSegment281)

HAnimJoint271.children.append(HAnimJoint280)

HAnimJoint262.children.append(HAnimJoint271)

HAnimJoint253.children.append(HAnimJoint262)

HAnimJoint244.children.append(HAnimJoint253)

HAnimJoint145.children.append(HAnimJoint244)

HAnimJoint130.children.append(HAnimJoint145)
HAnimJoint292 = x3d.HAnimJoint()
HAnimJoint292.DEF = "STD_Joint_l_calcaneocuboid"
HAnimJoint292.name = "l_calcaneocuboid"
HAnimJoint292.center = [0,1,0]
HAnimSegment293 = x3d.HAnimSegment()
HAnimSegment293.DEF = "STD_Segment_l_calcaneus"
HAnimSegment293.name = "l_calcaneus"
Transform294 = x3d.Transform()
Transform294.translation = [0,1,0]
Shape295 = x3d.Shape()
Shape295.USE = "HAnimJointShape"

Transform294.children.append(Shape295)

HAnimSegment293.children.append(Transform294)
Transform296 = x3d.Transform()
Shape297 = x3d.Shape()
LineSet298 = x3d.LineSet()
LineSet298.vertexCount = [2]
Coordinate299 = x3d.Coordinate()

LineSet298.coord = Coordinate299
ColorRGBA300 = x3d.ColorRGBA()
ColorRGBA300.USE = "HAnimSegmentLineColorRGBA"

LineSet298.color = ColorRGBA300

Shape297.geometry = LineSet298

Transform296.children.append(Shape297)

HAnimSegment293.children.append(Transform296)

HAnimJoint292.children.append(HAnimSegment293)
HAnimJoint301 = x3d.HAnimJoint()
HAnimJoint301.DEF = "STD_Joint_l_transversetarsal"
HAnimJoint301.name = "l_transversetarsal"
HAnimJoint301.center = [0,1,0]
HAnimSegment302 = x3d.HAnimSegment()
HAnimSegment302.DEF = "STD_Segment_l_cuboid"
HAnimSegment302.name = "l_cuboid"
Transform303 = x3d.Transform()
Transform303.translation = [0,1,0]
Shape304 = x3d.Shape()
Shape304.USE = "HAnimJointShape"

Transform303.children.append(Shape304)

HAnimSegment302.children.append(Transform303)
Transform305 = x3d.Transform()
Shape306 = x3d.Shape()
LineSet307 = x3d.LineSet()
LineSet307.vertexCount = [2]
Coordinate308 = x3d.Coordinate()

LineSet307.coord = Coordinate308
ColorRGBA309 = x3d.ColorRGBA()
ColorRGBA309.USE = "HAnimSegmentLineColorRGBA"

LineSet307.color = ColorRGBA309

Shape306.geometry = LineSet307

Transform305.children.append(Shape306)

HAnimSegment302.children.append(Transform305)

HAnimJoint301.children.append(HAnimSegment302)
HAnimJoint310 = x3d.HAnimJoint()
HAnimJoint310.DEF = "STD_Joint_l_tarsometatarsal_4"
HAnimJoint310.name = "l_tarsometatarsal_4"
HAnimJoint310.center = [0,1,0]
HAnimSegment311 = x3d.HAnimSegment()
HAnimSegment311.DEF = "STD_Segment_l_metatarsal_4"
HAnimSegment311.name = "l_metatarsal_4"
Transform312 = x3d.Transform()
Transform312.translation = [0,1,0]
Shape313 = x3d.Shape()
Shape313.USE = "HAnimJointShape"

Transform312.children.append(Shape313)

HAnimSegment311.children.append(Transform312)
Transform314 = x3d.Transform()
Shape315 = x3d.Shape()
LineSet316 = x3d.LineSet()
LineSet316.vertexCount = [2]
Coordinate317 = x3d.Coordinate()

LineSet316.coord = Coordinate317
ColorRGBA318 = x3d.ColorRGBA()
ColorRGBA318.USE = "HAnimSegmentLineColorRGBA"

LineSet316.color = ColorRGBA318

Shape315.geometry = LineSet316

Transform314.children.append(Shape315)

HAnimSegment311.children.append(Transform314)

HAnimJoint310.children.append(HAnimSegment311)
HAnimJoint319 = x3d.HAnimJoint()
HAnimJoint319.DEF = "STD_Joint_l_metatarsophalangeal_4"
HAnimJoint319.name = "l_metatarsophalangeal_4"
HAnimJoint319.center = [0,1,0]
HAnimSegment320 = x3d.HAnimSegment()
HAnimSegment320.DEF = "STD_Segment_l_tarsal_proximal_phalanx_4"
HAnimSegment320.name = "l_tarsal_proximal_phalanx_4"
Transform321 = x3d.Transform()
Transform321.translation = [0,1,0]
Shape322 = x3d.Shape()
Shape322.USE = "HAnimJointShape"

Transform321.children.append(Shape322)

HAnimSegment320.children.append(Transform321)
Transform323 = x3d.Transform()
Shape324 = x3d.Shape()
LineSet325 = x3d.LineSet()
LineSet325.vertexCount = [2]
Coordinate326 = x3d.Coordinate()

LineSet325.coord = Coordinate326
ColorRGBA327 = x3d.ColorRGBA()
ColorRGBA327.USE = "HAnimSegmentLineColorRGBA"

LineSet325.color = ColorRGBA327

Shape324.geometry = LineSet325

Transform323.children.append(Shape324)

HAnimSegment320.children.append(Transform323)

HAnimJoint319.children.append(HAnimSegment320)
HAnimJoint328 = x3d.HAnimJoint()
HAnimJoint328.DEF = "STD_Joint_l_tarsal_proximal_interphalangeal_4"
HAnimJoint328.name = "l_tarsal_proximal_interphalangeal_4"
HAnimJoint328.center = [0,1,0]
HAnimSegment329 = x3d.HAnimSegment()
HAnimSegment329.DEF = "STD_Segment_l_tarsal_middle_phalanx_4"
HAnimSegment329.name = "l_tarsal_middle_phalanx_4"
Transform330 = x3d.Transform()
Transform330.translation = [0,1,0]
Shape331 = x3d.Shape()
Shape331.USE = "HAnimJointShape"

Transform330.children.append(Shape331)

HAnimSegment329.children.append(Transform330)
Transform332 = x3d.Transform()
Shape333 = x3d.Shape()
LineSet334 = x3d.LineSet()
LineSet334.vertexCount = [2]
Coordinate335 = x3d.Coordinate()

LineSet334.coord = Coordinate335
ColorRGBA336 = x3d.ColorRGBA()
ColorRGBA336.USE = "HAnimSegmentLineColorRGBA"

LineSet334.color = ColorRGBA336

Shape333.geometry = LineSet334

Transform332.children.append(Shape333)

HAnimSegment329.children.append(Transform332)

HAnimJoint328.children.append(HAnimSegment329)
HAnimJoint337 = x3d.HAnimJoint()
HAnimJoint337.DEF = "STD_Joint_l_tarsal_distal_interphalangeal_4"
HAnimJoint337.name = "l_tarsal_distal_interphalangeal_4"
HAnimJoint337.center = [0,1,0]
HAnimSegment338 = x3d.HAnimSegment()
HAnimSegment338.DEF = "STD_Segment_l_tarsal_distal_phalanx_4"
HAnimSegment338.name = "l_tarsal_distal_phalanx_4"
Transform339 = x3d.Transform()
Transform339.translation = [0,1,0]
Shape340 = x3d.Shape()
Shape340.USE = "HAnimJointShape"

Transform339.children.append(Shape340)

HAnimSegment338.children.append(Transform339)
Transform341 = x3d.Transform()
Shape342 = x3d.Shape()
LineSet343 = x3d.LineSet()
LineSet343.vertexCount = [2]
Coordinate344 = x3d.Coordinate()

LineSet343.coord = Coordinate344
ColorRGBA345 = x3d.ColorRGBA()
ColorRGBA345.USE = "HAnimSegmentLineColorRGBA"

LineSet343.color = ColorRGBA345

Shape342.geometry = LineSet343

Transform341.children.append(Shape342)

HAnimSegment338.children.append(Transform341)
HAnimSite346 = x3d.HAnimSite()
HAnimSite346.DEF = "STD_Site_l_tarsal_distal_phalanx_4_tip"
HAnimSite346.name = "l_tarsal_distal_phalanx_4_tip"
TouchSensor347 = x3d.TouchSensor()
TouchSensor347.description = "HAnimSite l_tarsal_distal_phalanx_4_tip"

HAnimSite346.children.append(TouchSensor347)
Shape348 = x3d.Shape()
Shape348.USE = "HAnimSiteShape"

HAnimSite346.children.append(Shape348)

HAnimSegment338.children.append(HAnimSite346)

HAnimJoint337.children.append(HAnimSegment338)

HAnimJoint328.children.append(HAnimJoint337)

HAnimJoint319.children.append(HAnimJoint328)

HAnimJoint310.children.append(HAnimJoint319)

HAnimJoint301.children.append(HAnimJoint310)
HAnimJoint349 = x3d.HAnimJoint()
HAnimJoint349.DEF = "STD_Joint_l_tarsometatarsal_5"
HAnimJoint349.name = "l_tarsometatarsal_5"
HAnimJoint349.center = [0,1,0]
HAnimSegment350 = x3d.HAnimSegment()
HAnimSegment350.DEF = "STD_Segment_l_metatarsal_5"
HAnimSegment350.name = "l_metatarsal_5"
Transform351 = x3d.Transform()
Transform351.translation = [0,1,0]
Shape352 = x3d.Shape()
Shape352.USE = "HAnimJointShape"

Transform351.children.append(Shape352)

HAnimSegment350.children.append(Transform351)
Transform353 = x3d.Transform()
Shape354 = x3d.Shape()
LineSet355 = x3d.LineSet()
LineSet355.vertexCount = [2]
Coordinate356 = x3d.Coordinate()

LineSet355.coord = Coordinate356
ColorRGBA357 = x3d.ColorRGBA()
ColorRGBA357.USE = "HAnimSegmentLineColorRGBA"

LineSet355.color = ColorRGBA357

Shape354.geometry = LineSet355

Transform353.children.append(Shape354)

HAnimSegment350.children.append(Transform353)

HAnimJoint349.children.append(HAnimSegment350)
HAnimJoint358 = x3d.HAnimJoint()
HAnimJoint358.DEF = "STD_Joint_l_metatarsophalangeal_5"
HAnimJoint358.name = "l_metatarsophalangeal_5"
HAnimJoint358.center = [0,1,0]
HAnimSegment359 = x3d.HAnimSegment()
HAnimSegment359.DEF = "STD_Segment_l_tarsal_proximal_phalanx_5"
HAnimSegment359.name = "l_tarsal_proximal_phalanx_5"
Transform360 = x3d.Transform()
Transform360.translation = [0,1,0]
Shape361 = x3d.Shape()
Shape361.USE = "HAnimJointShape"

Transform360.children.append(Shape361)

HAnimSegment359.children.append(Transform360)
Transform362 = x3d.Transform()
Shape363 = x3d.Shape()
LineSet364 = x3d.LineSet()
LineSet364.vertexCount = [2]
Coordinate365 = x3d.Coordinate()

LineSet364.coord = Coordinate365
ColorRGBA366 = x3d.ColorRGBA()
ColorRGBA366.USE = "HAnimSegmentLineColorRGBA"

LineSet364.color = ColorRGBA366

Shape363.geometry = LineSet364

Transform362.children.append(Shape363)

HAnimSegment359.children.append(Transform362)
HAnimSite367 = x3d.HAnimSite()
HAnimSite367.DEF = "STD_Site_l_metatarsal_phalanx_5_pt"
HAnimSite367.name = "l_metatarsal_phalanx_5_pt"
TouchSensor368 = x3d.TouchSensor()
TouchSensor368.description = "HAnimSite l_metatarsal_phalanx_5_pt"

HAnimSite367.children.append(TouchSensor368)
Shape369 = x3d.Shape()
Shape369.USE = "HAnimSiteShape"

HAnimSite367.children.append(Shape369)

HAnimSegment359.children.append(HAnimSite367)

HAnimJoint358.children.append(HAnimSegment359)
HAnimJoint370 = x3d.HAnimJoint()
HAnimJoint370.DEF = "STD_Joint_l_tarsal_proximal_interphalangeal_5"
HAnimJoint370.name = "l_tarsal_proximal_interphalangeal_5"
HAnimJoint370.center = [0,1,0]
HAnimSegment371 = x3d.HAnimSegment()
HAnimSegment371.DEF = "STD_Segment_l_tarsal_middle_phalanx_5"
HAnimSegment371.name = "l_tarsal_middle_phalanx_5"
Transform372 = x3d.Transform()
Transform372.translation = [0,1,0]
Shape373 = x3d.Shape()
Shape373.USE = "HAnimJointShape"

Transform372.children.append(Shape373)

HAnimSegment371.children.append(Transform372)
Transform374 = x3d.Transform()
Shape375 = x3d.Shape()
LineSet376 = x3d.LineSet()
LineSet376.vertexCount = [2]
Coordinate377 = x3d.Coordinate()

LineSet376.coord = Coordinate377
ColorRGBA378 = x3d.ColorRGBA()
ColorRGBA378.USE = "HAnimSegmentLineColorRGBA"

LineSet376.color = ColorRGBA378

Shape375.geometry = LineSet376

Transform374.children.append(Shape375)

HAnimSegment371.children.append(Transform374)

HAnimJoint370.children.append(HAnimSegment371)
HAnimJoint379 = x3d.HAnimJoint()
HAnimJoint379.DEF = "STD_Joint_l_tarsal_distal_interphalangeal_5"
HAnimJoint379.name = "l_tarsal_distal_interphalangeal_5"
HAnimJoint379.center = [0,1,0]
HAnimSegment380 = x3d.HAnimSegment()
HAnimSegment380.DEF = "STD_Segment_l_tarsal_distal_phalanx_5"
HAnimSegment380.name = "l_tarsal_distal_phalanx_5"
Transform381 = x3d.Transform()
Transform381.translation = [0,1,0]
Shape382 = x3d.Shape()
Shape382.USE = "HAnimJointShape"

Transform381.children.append(Shape382)

HAnimSegment380.children.append(Transform381)
Transform383 = x3d.Transform()
Shape384 = x3d.Shape()
LineSet385 = x3d.LineSet()
LineSet385.vertexCount = [2]
Coordinate386 = x3d.Coordinate()

LineSet385.coord = Coordinate386
ColorRGBA387 = x3d.ColorRGBA()
ColorRGBA387.USE = "HAnimSegmentLineColorRGBA"

LineSet385.color = ColorRGBA387

Shape384.geometry = LineSet385

Transform383.children.append(Shape384)

HAnimSegment380.children.append(Transform383)
HAnimSite388 = x3d.HAnimSite()
HAnimSite388.DEF = "STD_Site_l_tarsal_distal_phalanx_5_tip"
HAnimSite388.name = "l_tarsal_distal_phalanx_5_tip"
TouchSensor389 = x3d.TouchSensor()
TouchSensor389.description = "HAnimSite l_tarsal_distal_phalanx_5_tip"

HAnimSite388.children.append(TouchSensor389)
Shape390 = x3d.Shape()
Shape390.USE = "HAnimSiteShape"

HAnimSite388.children.append(Shape390)

HAnimSegment380.children.append(HAnimSite388)

HAnimJoint379.children.append(HAnimSegment380)

HAnimJoint370.children.append(HAnimJoint379)

HAnimJoint358.children.append(HAnimJoint370)

HAnimJoint349.children.append(HAnimJoint358)

HAnimJoint301.children.append(HAnimJoint349)

HAnimJoint292.children.append(HAnimJoint301)

HAnimJoint130.children.append(HAnimJoint292)

HAnimJoint112.children.append(HAnimJoint130)

HAnimJoint91.children.append(HAnimJoint112)

HAnimJoint52.children.append(HAnimJoint91)
HAnimJoint391 = x3d.HAnimJoint()
HAnimJoint391.DEF = "STD_Joint_r_hip"
HAnimJoint391.name = "r_hip"
HAnimJoint391.center = [-0.0950,0.9171,0.0029]
HAnimSegment392 = x3d.HAnimSegment()
HAnimSegment392.DEF = "STD_Segment_r_thigh"
HAnimSegment392.name = "r_thigh"
Transform393 = x3d.Transform()
Transform393.translation = [-0.0950,0.9171,0.0029]
Shape394 = x3d.Shape()
Shape394.USE = "HAnimJointShape"

Transform393.children.append(Shape394)

HAnimSegment392.children.append(Transform393)
Transform395 = x3d.Transform()
Shape396 = x3d.Shape()
LineSet397 = x3d.LineSet()
LineSet397.vertexCount = [2]
Coordinate398 = x3d.Coordinate()

LineSet397.coord = Coordinate398
ColorRGBA399 = x3d.ColorRGBA()
ColorRGBA399.USE = "HAnimSegmentLineColorRGBA"

LineSet397.color = ColorRGBA399

Shape396.geometry = LineSet397

Transform395.children.append(Shape396)

HAnimSegment392.children.append(Transform395)
HAnimSite400 = x3d.HAnimSite()
HAnimSite400.DEF = "STD_Site_r_femoral_lateral_epicondyles_pt"
HAnimSite400.name = "r_femoral_lateral_epicondyles_pt"
HAnimSite400.translation = [-0.1421,0.4992,0.0310]
TouchSensor401 = x3d.TouchSensor()
TouchSensor401.description = "HAnimSite r_femoral_lateral_epicondyles_pt"

HAnimSite400.children.append(TouchSensor401)
Shape402 = x3d.Shape()
Shape402.USE = "HAnimSiteShape"

HAnimSite400.children.append(Shape402)

HAnimSegment392.children.append(HAnimSite400)
HAnimSite403 = x3d.HAnimSite()
HAnimSite403.DEF = "STD_Site_r_femoral_medial_epicondyles_pt"
HAnimSite403.name = "r_femoral_medial_epicondyles_pt"
HAnimSite403.translation = [-0.0221,0.5014,0.0289]
TouchSensor404 = x3d.TouchSensor()
TouchSensor404.description = "HAnimSite r_femoral_medial_epicondyles_pt"

HAnimSite403.children.append(TouchSensor404)
Shape405 = x3d.Shape()
Shape405.USE = "HAnimSiteShape"

HAnimSite403.children.append(Shape405)

HAnimSegment392.children.append(HAnimSite403)
HAnimSite406 = x3d.HAnimSite()
HAnimSite406.DEF = "STD_Site_r_knee_crease_pt"
HAnimSite406.name = "r_knee_crease_pt"
HAnimSite406.translation = [-0.0825,0.4932,-0.0326]
TouchSensor407 = x3d.TouchSensor()
TouchSensor407.description = "HAnimSite r_knee_crease_pt"

HAnimSite406.children.append(TouchSensor407)
Shape408 = x3d.Shape()
Shape408.USE = "HAnimSiteShape"

HAnimSite406.children.append(Shape408)

HAnimSegment392.children.append(HAnimSite406)
HAnimSite409 = x3d.HAnimSite()
HAnimSite409.DEF = "STD_Site_r_suprapatella_pt"
HAnimSite409.name = "r_suprapatella_pt"
TouchSensor410 = x3d.TouchSensor()
TouchSensor410.description = "HAnimSite r_suprapatella_pt"

HAnimSite409.children.append(TouchSensor410)
Shape411 = x3d.Shape()
Shape411.USE = "HAnimSiteShape"

HAnimSite409.children.append(Shape411)

HAnimSegment392.children.append(HAnimSite409)

HAnimJoint391.children.append(HAnimSegment392)
HAnimJoint412 = x3d.HAnimJoint()
HAnimJoint412.DEF = "STD_Joint_r_knee"
HAnimJoint412.name = "r_knee"
HAnimJoint412.center = [-0.0867,0.4913,0.0318]
HAnimSegment413 = x3d.HAnimSegment()
HAnimSegment413.DEF = "STD_Segment_r_calf"
HAnimSegment413.name = "r_calf"
Transform414 = x3d.Transform()
Transform414.translation = [-0.0867,0.4913,0.0318]
Shape415 = x3d.Shape()
Shape415.USE = "HAnimJointShape"

Transform414.children.append(Shape415)

HAnimSegment413.children.append(Transform414)
Transform416 = x3d.Transform()
Shape417 = x3d.Shape()
LineSet418 = x3d.LineSet()
LineSet418.vertexCount = [2]
Coordinate419 = x3d.Coordinate()

LineSet418.coord = Coordinate419
ColorRGBA420 = x3d.ColorRGBA()
ColorRGBA420.USE = "HAnimSegmentLineColorRGBA"

LineSet418.color = ColorRGBA420

Shape417.geometry = LineSet418

Transform416.children.append(Shape417)

HAnimSegment413.children.append(Transform416)
HAnimSite421 = x3d.HAnimSite()
HAnimSite421.DEF = "STD_Site_r_lateral_malleolus_pt"
HAnimSite421.name = "r_lateral_malleolus_pt"
HAnimSite421.translation = [-0.1006,0.0658,-0.1075]
TouchSensor422 = x3d.TouchSensor()
TouchSensor422.description = "HAnimSite r_lateral_malleolus_pt"

HAnimSite421.children.append(TouchSensor422)
Shape423 = x3d.Shape()
Shape423.USE = "HAnimSiteShape"

HAnimSite421.children.append(Shape423)

HAnimSegment413.children.append(HAnimSite421)
HAnimSite424 = x3d.HAnimSite()
HAnimSite424.DEF = "STD_Site_r_medial_malleolus_pt"
HAnimSite424.name = "r_medial_malleolus_pt"
HAnimSite424.translation = [-0.0591,0.0760,-0.0928]
TouchSensor425 = x3d.TouchSensor()
TouchSensor425.description = "HAnimSite r_medial_malleolus_pt"

HAnimSite424.children.append(TouchSensor425)
Shape426 = x3d.Shape()
Shape426.USE = "HAnimSiteShape"

HAnimSite424.children.append(Shape426)

HAnimSegment413.children.append(HAnimSite424)
HAnimSite427 = x3d.HAnimSite()
HAnimSite427.DEF = "STD_Site_r_tibiale_pt"
HAnimSite427.name = "r_tibiale_pt"
TouchSensor428 = x3d.TouchSensor()
TouchSensor428.description = "HAnimSite r_tibiale_pt"

HAnimSite427.children.append(TouchSensor428)
Shape429 = x3d.Shape()
Shape429.USE = "HAnimSiteShape"

HAnimSite427.children.append(Shape429)

HAnimSegment413.children.append(HAnimSite427)

HAnimJoint412.children.append(HAnimSegment413)
HAnimJoint430 = x3d.HAnimJoint()
HAnimJoint430.DEF = "STD_Joint_r_talocrural"
HAnimJoint430.name = "r_talocrural"
HAnimJoint430.center = [-0.0801,0.0712,-0.0766]
HAnimSegment431 = x3d.HAnimSegment()
HAnimSegment431.DEF = "STD_Segment_r_talus"
HAnimSegment431.name = "r_talus"
Transform432 = x3d.Transform()
Transform432.translation = [-0.0801,0.0712,-0.0766]
Shape433 = x3d.Shape()
Shape433.USE = "HAnimJointShape"

Transform432.children.append(Shape433)

HAnimSegment431.children.append(Transform432)
Transform434 = x3d.Transform()
Shape435 = x3d.Shape()
LineSet436 = x3d.LineSet()
LineSet436.vertexCount = [2]
Coordinate437 = x3d.Coordinate()

LineSet436.coord = Coordinate437
ColorRGBA438 = x3d.ColorRGBA()
ColorRGBA438.USE = "HAnimSegmentLineColorRGBA"

LineSet436.color = ColorRGBA438

Shape435.geometry = LineSet436

Transform434.children.append(Shape435)

HAnimSegment431.children.append(Transform434)
HAnimSite439 = x3d.HAnimSite()
HAnimSite439.DEF = "STD_Site_r_calcaneus_posterior_pt"
HAnimSite439.name = "r_calcaneus_posterior_pt"
HAnimSite439.translation = [-0.0692,0.0297,-0.1221]
TouchSensor440 = x3d.TouchSensor()
TouchSensor440.description = "HAnimSite r_calcaneus_posterior_pt"

HAnimSite439.children.append(TouchSensor440)
Shape441 = x3d.Shape()
Shape441.USE = "HAnimSiteShape"

HAnimSite439.children.append(Shape441)

HAnimSegment431.children.append(HAnimSite439)
HAnimSite442 = x3d.HAnimSite()
HAnimSite442.DEF = "STD_Site_r_sphyrion_pt"
HAnimSite442.name = "r_sphyrion_pt"
HAnimSite442.translation = [-0.0603,0.0610,-0.1002]
TouchSensor443 = x3d.TouchSensor()
TouchSensor443.description = "HAnimSite r_sphyrion_pt"

HAnimSite442.children.append(TouchSensor443)
Shape444 = x3d.Shape()
Shape444.USE = "HAnimSiteShape"

HAnimSite442.children.append(Shape444)

HAnimSegment431.children.append(HAnimSite442)

HAnimJoint430.children.append(HAnimSegment431)
HAnimJoint445 = x3d.HAnimJoint()
HAnimJoint445.DEF = "STD_Joint_r_talocalcaneonavicular"
HAnimJoint445.name = "r_talocalcaneonavicular"
HAnimJoint445.center = [0,1,0]
HAnimSegment446 = x3d.HAnimSegment()
HAnimSegment446.DEF = "STD_Segment_r_navicular"
HAnimSegment446.name = "r_navicular"
Transform447 = x3d.Transform()
Transform447.translation = [0,1,0]
Shape448 = x3d.Shape()
Shape448.USE = "HAnimJointShape"

Transform447.children.append(Shape448)

HAnimSegment446.children.append(Transform447)
Transform449 = x3d.Transform()
Shape450 = x3d.Shape()
LineSet451 = x3d.LineSet()
LineSet451.vertexCount = [2]
Coordinate452 = x3d.Coordinate()

LineSet451.coord = Coordinate452
ColorRGBA453 = x3d.ColorRGBA()
ColorRGBA453.USE = "HAnimSegmentLineColorRGBA"

LineSet451.color = ColorRGBA453

Shape450.geometry = LineSet451

Transform449.children.append(Shape450)

HAnimSegment446.children.append(Transform449)

HAnimJoint445.children.append(HAnimSegment446)
HAnimJoint454 = x3d.HAnimJoint()
HAnimJoint454.DEF = "STD_Joint_r_cuneonavicular_1"
HAnimJoint454.name = "r_cuneonavicular_1"
HAnimJoint454.center = [0,1,0]
HAnimSegment455 = x3d.HAnimSegment()
HAnimSegment455.DEF = "STD_Segment_r_cuneiform_1"
HAnimSegment455.name = "r_cuneiform_1"
Transform456 = x3d.Transform()
Transform456.translation = [0,1,0]
Shape457 = x3d.Shape()
Shape457.USE = "HAnimJointShape"

Transform456.children.append(Shape457)

HAnimSegment455.children.append(Transform456)
Transform458 = x3d.Transform()
Shape459 = x3d.Shape()
LineSet460 = x3d.LineSet()
LineSet460.vertexCount = [2]
Coordinate461 = x3d.Coordinate()

LineSet460.coord = Coordinate461
ColorRGBA462 = x3d.ColorRGBA()
ColorRGBA462.USE = "HAnimSegmentLineColorRGBA"

LineSet460.color = ColorRGBA462

Shape459.geometry = LineSet460

Transform458.children.append(Shape459)

HAnimSegment455.children.append(Transform458)

HAnimJoint454.children.append(HAnimSegment455)
HAnimJoint463 = x3d.HAnimJoint()
HAnimJoint463.DEF = "STD_Joint_r_tarsometatarsal_1"
HAnimJoint463.name = "r_tarsometatarsal_1"
HAnimJoint463.center = [0,1,0]
HAnimSegment464 = x3d.HAnimSegment()
HAnimSegment464.DEF = "STD_Segment_r_metatarsal_1"
HAnimSegment464.name = "r_metatarsal_1"
Transform465 = x3d.Transform()
Transform465.translation = [0,1,0]
Shape466 = x3d.Shape()
Shape466.USE = "HAnimJointShape"

Transform465.children.append(Shape466)

HAnimSegment464.children.append(Transform465)
Transform467 = x3d.Transform()
Shape468 = x3d.Shape()
LineSet469 = x3d.LineSet()
LineSet469.vertexCount = [2]
Coordinate470 = x3d.Coordinate()

LineSet469.coord = Coordinate470
ColorRGBA471 = x3d.ColorRGBA()
ColorRGBA471.USE = "HAnimSegmentLineColorRGBA"

LineSet469.color = ColorRGBA471

Shape468.geometry = LineSet469

Transform467.children.append(Shape468)

HAnimSegment464.children.append(Transform467)

HAnimJoint463.children.append(HAnimSegment464)
HAnimJoint472 = x3d.HAnimJoint()
HAnimJoint472.DEF = "STD_Joint_r_metatarsophalangeal_1"
HAnimJoint472.name = "r_metatarsophalangeal_1"
HAnimJoint472.center = [0,1,0]
HAnimSegment473 = x3d.HAnimSegment()
HAnimSegment473.DEF = "STD_Segment_r_tarsal_proximal_phalanx_1"
HAnimSegment473.name = "r_tarsal_proximal_phalanx_1"
Transform474 = x3d.Transform()
Transform474.translation = [0,1,0]
Shape475 = x3d.Shape()
Shape475.USE = "HAnimJointShape"

Transform474.children.append(Shape475)

HAnimSegment473.children.append(Transform474)
Transform476 = x3d.Transform()
Shape477 = x3d.Shape()
LineSet478 = x3d.LineSet()
LineSet478.vertexCount = [2]
Coordinate479 = x3d.Coordinate()

LineSet478.coord = Coordinate479
ColorRGBA480 = x3d.ColorRGBA()
ColorRGBA480.USE = "HAnimSegmentLineColorRGBA"

LineSet478.color = ColorRGBA480

Shape477.geometry = LineSet478

Transform476.children.append(Shape477)

HAnimSegment473.children.append(Transform476)
HAnimSite481 = x3d.HAnimSite()
HAnimSite481.DEF = "STD_Site_r_metatarsal_phalanx_1_pt"
HAnimSite481.name = "r_metatarsal_phalanx_1_pt"
TouchSensor482 = x3d.TouchSensor()
TouchSensor482.description = "HAnimSite r_metatarsal_phalanx_1_pt"

HAnimSite481.children.append(TouchSensor482)
Shape483 = x3d.Shape()
Shape483.USE = "HAnimSiteShape"

HAnimSite481.children.append(Shape483)

HAnimSegment473.children.append(HAnimSite481)

HAnimJoint472.children.append(HAnimSegment473)
HAnimJoint484 = x3d.HAnimJoint()
HAnimJoint484.DEF = "STD_Joint_r_tarsal_interphalangeal_1"
HAnimJoint484.name = "r_tarsal_interphalangeal_1"
HAnimJoint484.center = [0,1,0]
HAnimSegment485 = x3d.HAnimSegment()
HAnimSegment485.DEF = "STD_Segment_r_tarsal_distal_phalanx_1"
HAnimSegment485.name = "r_tarsal_distal_phalanx_1"
Transform486 = x3d.Transform()
Transform486.translation = [0,1,0]
Shape487 = x3d.Shape()
Shape487.USE = "HAnimJointShape"

Transform486.children.append(Shape487)

HAnimSegment485.children.append(Transform486)
Transform488 = x3d.Transform()
Shape489 = x3d.Shape()
LineSet490 = x3d.LineSet()
LineSet490.vertexCount = [2]
Coordinate491 = x3d.Coordinate()

LineSet490.coord = Coordinate491
ColorRGBA492 = x3d.ColorRGBA()
ColorRGBA492.USE = "HAnimSegmentLineColorRGBA"

LineSet490.color = ColorRGBA492

Shape489.geometry = LineSet490

Transform488.children.append(Shape489)

HAnimSegment485.children.append(Transform488)
HAnimSite493 = x3d.HAnimSite()
HAnimSite493.DEF = "STD_Site_r_tarsal_distal_phalanx_1_tip"
HAnimSite493.name = "r_tarsal_distal_phalanx_1_tip"
TouchSensor494 = x3d.TouchSensor()
TouchSensor494.description = "HAnimSite r_tarsal_distal_phalanx_1_tip"

HAnimSite493.children.append(TouchSensor494)
Shape495 = x3d.Shape()
Shape495.USE = "HAnimSiteShape"

HAnimSite493.children.append(Shape495)

HAnimSegment485.children.append(HAnimSite493)

HAnimJoint484.children.append(HAnimSegment485)

HAnimJoint472.children.append(HAnimJoint484)

HAnimJoint463.children.append(HAnimJoint472)

HAnimJoint454.children.append(HAnimJoint463)

HAnimJoint445.children.append(HAnimJoint454)
HAnimJoint496 = x3d.HAnimJoint()
HAnimJoint496.DEF = "STD_Joint_r_cuneonavicular_2"
HAnimJoint496.name = "r_cuneonavicular_2"
HAnimJoint496.center = [0,1,0]
HAnimSegment497 = x3d.HAnimSegment()
HAnimSegment497.DEF = "STD_Segment_r_cuneiform_2"
HAnimSegment497.name = "r_cuneiform_2"
Transform498 = x3d.Transform()
Transform498.translation = [0,1,0]
Shape499 = x3d.Shape()
Shape499.USE = "HAnimJointShape"

Transform498.children.append(Shape499)

HAnimSegment497.children.append(Transform498)
Transform500 = x3d.Transform()
Shape501 = x3d.Shape()
LineSet502 = x3d.LineSet()
LineSet502.vertexCount = [2]
Coordinate503 = x3d.Coordinate()

LineSet502.coord = Coordinate503
ColorRGBA504 = x3d.ColorRGBA()
ColorRGBA504.USE = "HAnimSegmentLineColorRGBA"

LineSet502.color = ColorRGBA504

Shape501.geometry = LineSet502

Transform500.children.append(Shape501)

HAnimSegment497.children.append(Transform500)

HAnimJoint496.children.append(HAnimSegment497)
HAnimJoint505 = x3d.HAnimJoint()
HAnimJoint505.DEF = "STD_Joint_r_tarsometatarsal_2"
HAnimJoint505.name = "r_tarsometatarsal_2"
HAnimJoint505.center = [0,1,0]
HAnimSegment506 = x3d.HAnimSegment()
HAnimSegment506.DEF = "STD_Segment_r_metatarsal_2"
HAnimSegment506.name = "r_metatarsal_2"
Transform507 = x3d.Transform()
Transform507.translation = [0,1,0]
Shape508 = x3d.Shape()
Shape508.USE = "HAnimJointShape"

Transform507.children.append(Shape508)

HAnimSegment506.children.append(Transform507)
Transform509 = x3d.Transform()
Shape510 = x3d.Shape()
LineSet511 = x3d.LineSet()
LineSet511.vertexCount = [2]
Coordinate512 = x3d.Coordinate()

LineSet511.coord = Coordinate512
ColorRGBA513 = x3d.ColorRGBA()
ColorRGBA513.USE = "HAnimSegmentLineColorRGBA"

LineSet511.color = ColorRGBA513

Shape510.geometry = LineSet511

Transform509.children.append(Shape510)

HAnimSegment506.children.append(Transform509)

HAnimJoint505.children.append(HAnimSegment506)
HAnimJoint514 = x3d.HAnimJoint()
HAnimJoint514.DEF = "STD_Joint_r_metatarsophalangeal_2"
HAnimJoint514.name = "r_metatarsophalangeal_2"
HAnimJoint514.center = [0,1,0]
HAnimSegment515 = x3d.HAnimSegment()
HAnimSegment515.DEF = "STD_Segment_r_tarsal_proximal_phalanx_2"
HAnimSegment515.name = "r_tarsal_proximal_phalanx_2"
Transform516 = x3d.Transform()
Transform516.translation = [0,1,0]
Shape517 = x3d.Shape()
Shape517.USE = "HAnimJointShape"

Transform516.children.append(Shape517)

HAnimSegment515.children.append(Transform516)
Transform518 = x3d.Transform()
Shape519 = x3d.Shape()
LineSet520 = x3d.LineSet()
LineSet520.vertexCount = [2]
Coordinate521 = x3d.Coordinate()

LineSet520.coord = Coordinate521
ColorRGBA522 = x3d.ColorRGBA()
ColorRGBA522.USE = "HAnimSegmentLineColorRGBA"

LineSet520.color = ColorRGBA522

Shape519.geometry = LineSet520

Transform518.children.append(Shape519)

HAnimSegment515.children.append(Transform518)

HAnimJoint514.children.append(HAnimSegment515)
HAnimJoint523 = x3d.HAnimJoint()
HAnimJoint523.DEF = "STD_Joint_r_tarsal_proximal_interphalangeal_2"
HAnimJoint523.name = "r_tarsal_proximal_interphalangeal_2"
HAnimJoint523.center = [0,1,0]
HAnimSegment524 = x3d.HAnimSegment()
HAnimSegment524.DEF = "STD_Segment_r_tarsal_middle_phalanx_2"
HAnimSegment524.name = "r_tarsal_middle_phalanx_2"
Transform525 = x3d.Transform()
Transform525.translation = [0,1,0]
Shape526 = x3d.Shape()
Shape526.USE = "HAnimJointShape"

Transform525.children.append(Shape526)

HAnimSegment524.children.append(Transform525)
Transform527 = x3d.Transform()
Shape528 = x3d.Shape()
LineSet529 = x3d.LineSet()
LineSet529.vertexCount = [2]
Coordinate530 = x3d.Coordinate()

LineSet529.coord = Coordinate530
ColorRGBA531 = x3d.ColorRGBA()
ColorRGBA531.USE = "HAnimSegmentLineColorRGBA"

LineSet529.color = ColorRGBA531

Shape528.geometry = LineSet529

Transform527.children.append(Shape528)

HAnimSegment524.children.append(Transform527)

HAnimJoint523.children.append(HAnimSegment524)
HAnimJoint532 = x3d.HAnimJoint()
HAnimJoint532.DEF = "STD_Joint_r_tarsal_distal_interphalangeal_2"
HAnimJoint532.name = "r_tarsal_distal_interphalangeal_2"
HAnimJoint532.center = [0,1,0]
HAnimSegment533 = x3d.HAnimSegment()
HAnimSegment533.DEF = "STD_Segment_r_tarsal_distal_phalanx_2"
HAnimSegment533.name = "r_tarsal_distal_phalanx_2"
Transform534 = x3d.Transform()
Transform534.translation = [0,1,0]
Shape535 = x3d.Shape()
Shape535.USE = "HAnimJointShape"

Transform534.children.append(Shape535)

HAnimSegment533.children.append(Transform534)
Transform536 = x3d.Transform()
Shape537 = x3d.Shape()
LineSet538 = x3d.LineSet()
LineSet538.vertexCount = [2]
Coordinate539 = x3d.Coordinate()

LineSet538.coord = Coordinate539
ColorRGBA540 = x3d.ColorRGBA()
ColorRGBA540.USE = "HAnimSegmentLineColorRGBA"

LineSet538.color = ColorRGBA540

Shape537.geometry = LineSet538

Transform536.children.append(Shape537)

HAnimSegment533.children.append(Transform536)
HAnimSite541 = x3d.HAnimSite()
HAnimSite541.DEF = "STD_Site_r_tarsal_distal_phalanx_2_tip"
HAnimSite541.name = "r_tarsal_distal_phalanx_2_tip"
HAnimSite541.translation = [-0.0883,0.0134,0.1383]
TouchSensor542 = x3d.TouchSensor()
TouchSensor542.description = "HAnimSite r_tarsal_distal_phalanx_2_tip"

HAnimSite541.children.append(TouchSensor542)
Shape543 = x3d.Shape()
Shape543.USE = "HAnimSiteShape"

HAnimSite541.children.append(Shape543)

HAnimSegment533.children.append(HAnimSite541)

HAnimJoint532.children.append(HAnimSegment533)

HAnimJoint523.children.append(HAnimJoint532)

HAnimJoint514.children.append(HAnimJoint523)

HAnimJoint505.children.append(HAnimJoint514)

HAnimJoint496.children.append(HAnimJoint505)

HAnimJoint445.children.append(HAnimJoint496)
HAnimJoint544 = x3d.HAnimJoint()
HAnimJoint544.DEF = "STD_Joint_r_cuneonavicular_3"
HAnimJoint544.name = "r_cuneonavicular_3"
HAnimJoint544.center = [0,1,0]
HAnimSegment545 = x3d.HAnimSegment()
HAnimSegment545.DEF = "STD_Segment_r_cuneiform_3"
HAnimSegment545.name = "r_cuneiform_3"
Transform546 = x3d.Transform()
Transform546.translation = [0,1,0]
Shape547 = x3d.Shape()
Shape547.USE = "HAnimJointShape"

Transform546.children.append(Shape547)

HAnimSegment545.children.append(Transform546)
Transform548 = x3d.Transform()
Shape549 = x3d.Shape()
LineSet550 = x3d.LineSet()
LineSet550.vertexCount = [2]
Coordinate551 = x3d.Coordinate()

LineSet550.coord = Coordinate551
ColorRGBA552 = x3d.ColorRGBA()
ColorRGBA552.USE = "HAnimSegmentLineColorRGBA"

LineSet550.color = ColorRGBA552

Shape549.geometry = LineSet550

Transform548.children.append(Shape549)

HAnimSegment545.children.append(Transform548)

HAnimJoint544.children.append(HAnimSegment545)
HAnimJoint553 = x3d.HAnimJoint()
HAnimJoint553.DEF = "STD_Joint_r_tarsometatarsal_3 "
HAnimJoint553.name = "r_tarsometatarsal_3 "
HAnimJoint553.center = [0,1,0]
HAnimSegment554 = x3d.HAnimSegment()
HAnimSegment554.DEF = "STD_Segment_r_metatarsal_3"
HAnimSegment554.name = "r_metatarsal_3"
Transform555 = x3d.Transform()
Transform555.translation = [0,1,0]
Shape556 = x3d.Shape()
Shape556.USE = "HAnimJointShape"

Transform555.children.append(Shape556)

HAnimSegment554.children.append(Transform555)
Transform557 = x3d.Transform()
Shape558 = x3d.Shape()
LineSet559 = x3d.LineSet()
LineSet559.vertexCount = [2]
Coordinate560 = x3d.Coordinate()

LineSet559.coord = Coordinate560
ColorRGBA561 = x3d.ColorRGBA()
ColorRGBA561.USE = "HAnimSegmentLineColorRGBA"

LineSet559.color = ColorRGBA561

Shape558.geometry = LineSet559

Transform557.children.append(Shape558)

HAnimSegment554.children.append(Transform557)

HAnimJoint553.children.append(HAnimSegment554)
HAnimJoint562 = x3d.HAnimJoint()
HAnimJoint562.DEF = "STD_Joint_r_metatarsophalangeal_3"
HAnimJoint562.name = "r_metatarsophalangeal_3"
HAnimJoint562.center = [0,1,0]
HAnimSegment563 = x3d.HAnimSegment()
HAnimSegment563.DEF = "STD_Segment_r_tarsal_proximal_phalanx_3"
HAnimSegment563.name = "r_tarsal_proximal_phalanx_3"
Transform564 = x3d.Transform()
Transform564.translation = [0,1,0]
Shape565 = x3d.Shape()
Shape565.USE = "HAnimJointShape"

Transform564.children.append(Shape565)

HAnimSegment563.children.append(Transform564)
Transform566 = x3d.Transform()
Shape567 = x3d.Shape()
LineSet568 = x3d.LineSet()
LineSet568.vertexCount = [2]
Coordinate569 = x3d.Coordinate()

LineSet568.coord = Coordinate569
ColorRGBA570 = x3d.ColorRGBA()
ColorRGBA570.USE = "HAnimSegmentLineColorRGBA"

LineSet568.color = ColorRGBA570

Shape567.geometry = LineSet568

Transform566.children.append(Shape567)

HAnimSegment563.children.append(Transform566)

HAnimJoint562.children.append(HAnimSegment563)
HAnimJoint571 = x3d.HAnimJoint()
HAnimJoint571.DEF = "STD_Joint_r_tarsal_proximal_interphalangeal_3"
HAnimJoint571.name = "r_tarsal_proximal_interphalangeal_3"
HAnimJoint571.center = [0,1,0]
HAnimSegment572 = x3d.HAnimSegment()
HAnimSegment572.DEF = "STD_Segment_r_tarsal_middle_phalanx_3"
HAnimSegment572.name = "r_tarsal_middle_phalanx_3"
Transform573 = x3d.Transform()
Transform573.translation = [0,1,0]
Shape574 = x3d.Shape()
Shape574.USE = "HAnimJointShape"

Transform573.children.append(Shape574)

HAnimSegment572.children.append(Transform573)
Transform575 = x3d.Transform()
Shape576 = x3d.Shape()
LineSet577 = x3d.LineSet()
LineSet577.vertexCount = [2]
Coordinate578 = x3d.Coordinate()

LineSet577.coord = Coordinate578
ColorRGBA579 = x3d.ColorRGBA()
ColorRGBA579.USE = "HAnimSegmentLineColorRGBA"

LineSet577.color = ColorRGBA579

Shape576.geometry = LineSet577

Transform575.children.append(Shape576)

HAnimSegment572.children.append(Transform575)

HAnimJoint571.children.append(HAnimSegment572)
HAnimJoint580 = x3d.HAnimJoint()
HAnimJoint580.DEF = "STD_Joint_r_tarsal_distal_interphalangeal_3"
HAnimJoint580.name = "r_tarsal_distal_interphalangeal_3"
HAnimJoint580.center = [0,1,0]
HAnimSegment581 = x3d.HAnimSegment()
HAnimSegment581.DEF = "STD_Segment_r_tarsal_distal_phalanx_3"
HAnimSegment581.name = "r_tarsal_distal_phalanx_3"
Transform582 = x3d.Transform()
Transform582.translation = [0,1,0]
Shape583 = x3d.Shape()
Shape583.USE = "HAnimJointShape"

Transform582.children.append(Shape583)

HAnimSegment581.children.append(Transform582)
Transform584 = x3d.Transform()
Shape585 = x3d.Shape()
LineSet586 = x3d.LineSet()
LineSet586.vertexCount = [2]
Coordinate587 = x3d.Coordinate()

LineSet586.coord = Coordinate587
ColorRGBA588 = x3d.ColorRGBA()
ColorRGBA588.USE = "HAnimSegmentLineColorRGBA"

LineSet586.color = ColorRGBA588

Shape585.geometry = LineSet586

Transform584.children.append(Shape585)

HAnimSegment581.children.append(Transform584)
HAnimSite589 = x3d.HAnimSite()
HAnimSite589.DEF = "STD_Site_r_tarsal_distal_phalanx_3_tip"
HAnimSite589.name = "r_tarsal_distal_phalanx_3_tip"
TouchSensor590 = x3d.TouchSensor()
TouchSensor590.description = "HAnimSite r_tarsal_distal_phalanx_3_tip"

HAnimSite589.children.append(TouchSensor590)
Shape591 = x3d.Shape()
Shape591.USE = "HAnimSiteShape"

HAnimSite589.children.append(Shape591)

HAnimSegment581.children.append(HAnimSite589)

HAnimJoint580.children.append(HAnimSegment581)

HAnimJoint571.children.append(HAnimJoint580)

HAnimJoint562.children.append(HAnimJoint571)

HAnimJoint553.children.append(HAnimJoint562)

HAnimJoint544.children.append(HAnimJoint553)

HAnimJoint445.children.append(HAnimJoint544)

HAnimJoint430.children.append(HAnimJoint445)
HAnimJoint592 = x3d.HAnimJoint()
HAnimJoint592.DEF = "STD_Joint_r_calcaneocuboid"
HAnimJoint592.name = "r_calcaneocuboid"
HAnimJoint592.center = [0,1,0]
HAnimSegment593 = x3d.HAnimSegment()
HAnimSegment593.DEF = "STD_Segment_r_calcaneus"
HAnimSegment593.name = "r_calcaneus"
Transform594 = x3d.Transform()
Transform594.translation = [0,1,0]
Shape595 = x3d.Shape()
Shape595.USE = "HAnimJointShape"

Transform594.children.append(Shape595)

HAnimSegment593.children.append(Transform594)
Transform596 = x3d.Transform()
Shape597 = x3d.Shape()
LineSet598 = x3d.LineSet()
LineSet598.vertexCount = [2]
Coordinate599 = x3d.Coordinate()

LineSet598.coord = Coordinate599
ColorRGBA600 = x3d.ColorRGBA()
ColorRGBA600.USE = "HAnimSegmentLineColorRGBA"

LineSet598.color = ColorRGBA600

Shape597.geometry = LineSet598

Transform596.children.append(Shape597)

HAnimSegment593.children.append(Transform596)

HAnimJoint592.children.append(HAnimSegment593)
HAnimJoint601 = x3d.HAnimJoint()
HAnimJoint601.DEF = "STD_Joint_r_transversetarsal"
HAnimJoint601.name = "r_transversetarsal"
HAnimJoint601.center = [0,1,0]
HAnimSegment602 = x3d.HAnimSegment()
HAnimSegment602.DEF = "STD_Segment_r_cuboid"
HAnimSegment602.name = "r_cuboid"
Transform603 = x3d.Transform()
Transform603.translation = [0,1,0]
Shape604 = x3d.Shape()
Shape604.USE = "HAnimJointShape"

Transform603.children.append(Shape604)

HAnimSegment602.children.append(Transform603)
Transform605 = x3d.Transform()
Shape606 = x3d.Shape()
LineSet607 = x3d.LineSet()
LineSet607.vertexCount = [2]
Coordinate608 = x3d.Coordinate()

LineSet607.coord = Coordinate608
ColorRGBA609 = x3d.ColorRGBA()
ColorRGBA609.USE = "HAnimSegmentLineColorRGBA"

LineSet607.color = ColorRGBA609

Shape606.geometry = LineSet607

Transform605.children.append(Shape606)

HAnimSegment602.children.append(Transform605)

HAnimJoint601.children.append(HAnimSegment602)
HAnimJoint610 = x3d.HAnimJoint()
HAnimJoint610.DEF = "STD_Joint_r_tarsometatarsal_4"
HAnimJoint610.name = "r_tarsometatarsal_4"
HAnimJoint610.center = [0,1,0]
HAnimSegment611 = x3d.HAnimSegment()
HAnimSegment611.DEF = "STD_Segment_r_metatarsal_4"
HAnimSegment611.name = "r_metatarsal_4"
Transform612 = x3d.Transform()
Transform612.translation = [0,1,0]
Shape613 = x3d.Shape()
Shape613.USE = "HAnimJointShape"

Transform612.children.append(Shape613)

HAnimSegment611.children.append(Transform612)
Transform614 = x3d.Transform()
Shape615 = x3d.Shape()
LineSet616 = x3d.LineSet()
LineSet616.vertexCount = [2]
Coordinate617 = x3d.Coordinate()

LineSet616.coord = Coordinate617
ColorRGBA618 = x3d.ColorRGBA()
ColorRGBA618.USE = "HAnimSegmentLineColorRGBA"

LineSet616.color = ColorRGBA618

Shape615.geometry = LineSet616

Transform614.children.append(Shape615)

HAnimSegment611.children.append(Transform614)

HAnimJoint610.children.append(HAnimSegment611)
HAnimJoint619 = x3d.HAnimJoint()
HAnimJoint619.DEF = "STD_Joint_r_metatarsophalangeal_4"
HAnimJoint619.name = "r_metatarsophalangeal_4"
HAnimJoint619.center = [0,1,0]
HAnimSegment620 = x3d.HAnimSegment()
HAnimSegment620.DEF = "STD_Segment_r_tarsal_proximal_phalanx_4"
HAnimSegment620.name = "r_tarsal_proximal_phalanx_4"
Transform621 = x3d.Transform()
Transform621.translation = [0,1,0]
Shape622 = x3d.Shape()
Shape622.USE = "HAnimJointShape"

Transform621.children.append(Shape622)

HAnimSegment620.children.append(Transform621)
Transform623 = x3d.Transform()
Shape624 = x3d.Shape()
LineSet625 = x3d.LineSet()
LineSet625.vertexCount = [2]
Coordinate626 = x3d.Coordinate()

LineSet625.coord = Coordinate626
ColorRGBA627 = x3d.ColorRGBA()
ColorRGBA627.USE = "HAnimSegmentLineColorRGBA"

LineSet625.color = ColorRGBA627

Shape624.geometry = LineSet625

Transform623.children.append(Shape624)

HAnimSegment620.children.append(Transform623)

HAnimJoint619.children.append(HAnimSegment620)
HAnimJoint628 = x3d.HAnimJoint()
HAnimJoint628.DEF = "STD_Joint_r_tarsal_proximal_interphalangeal_4"
HAnimJoint628.name = "r_tarsal_proximal_interphalangeal_4"
HAnimJoint628.center = [0,1,0]
HAnimSegment629 = x3d.HAnimSegment()
HAnimSegment629.DEF = "STD_Segment_r_tarsal_middle_phalanx_4"
HAnimSegment629.name = "r_tarsal_middle_phalanx_4"
Transform630 = x3d.Transform()
Transform630.translation = [0,1,0]
Shape631 = x3d.Shape()
Shape631.USE = "HAnimJointShape"

Transform630.children.append(Shape631)

HAnimSegment629.children.append(Transform630)
Transform632 = x3d.Transform()
Shape633 = x3d.Shape()
LineSet634 = x3d.LineSet()
LineSet634.vertexCount = [2]
Coordinate635 = x3d.Coordinate()

LineSet634.coord = Coordinate635
ColorRGBA636 = x3d.ColorRGBA()
ColorRGBA636.USE = "HAnimSegmentLineColorRGBA"

LineSet634.color = ColorRGBA636

Shape633.geometry = LineSet634

Transform632.children.append(Shape633)

HAnimSegment629.children.append(Transform632)

HAnimJoint628.children.append(HAnimSegment629)
HAnimJoint637 = x3d.HAnimJoint()
HAnimJoint637.DEF = "STD_Joint_r_tarsal_distal_interphalangeal_4"
HAnimJoint637.name = "r_tarsal_distal_interphalangeal_4"
HAnimJoint637.center = [0,1,0]
HAnimSegment638 = x3d.HAnimSegment()
HAnimSegment638.DEF = "STD_Segment_r_tarsal_distal_phalanx_4"
HAnimSegment638.name = "r_tarsal_distal_phalanx_4"
Transform639 = x3d.Transform()
Transform639.translation = [0,1,0]
Shape640 = x3d.Shape()
Shape640.USE = "HAnimJointShape"

Transform639.children.append(Shape640)

HAnimSegment638.children.append(Transform639)
Transform641 = x3d.Transform()
Shape642 = x3d.Shape()
LineSet643 = x3d.LineSet()
LineSet643.vertexCount = [2]
Coordinate644 = x3d.Coordinate()

LineSet643.coord = Coordinate644
ColorRGBA645 = x3d.ColorRGBA()
ColorRGBA645.USE = "HAnimSegmentLineColorRGBA"

LineSet643.color = ColorRGBA645

Shape642.geometry = LineSet643

Transform641.children.append(Shape642)

HAnimSegment638.children.append(Transform641)
HAnimSite646 = x3d.HAnimSite()
HAnimSite646.DEF = "STD_Site_r_tarsal_distal_phalanx_4_tip"
HAnimSite646.name = "r_tarsal_distal_phalanx_4_tip"
TouchSensor647 = x3d.TouchSensor()
TouchSensor647.description = "HAnimSite r_tarsal_distal_phalanx_4_tip"

HAnimSite646.children.append(TouchSensor647)
Shape648 = x3d.Shape()
Shape648.USE = "HAnimSiteShape"

HAnimSite646.children.append(Shape648)

HAnimSegment638.children.append(HAnimSite646)

HAnimJoint637.children.append(HAnimSegment638)

HAnimJoint628.children.append(HAnimJoint637)

HAnimJoint619.children.append(HAnimJoint628)

HAnimJoint610.children.append(HAnimJoint619)

HAnimJoint601.children.append(HAnimJoint610)
HAnimJoint649 = x3d.HAnimJoint()
HAnimJoint649.DEF = "STD_Joint_r_tarsometatarsal_5"
HAnimJoint649.name = "r_tarsometatarsal_5"
HAnimJoint649.center = [0,1,0]
HAnimSegment650 = x3d.HAnimSegment()
HAnimSegment650.DEF = "STD_Segment_r_metatarsal_5"
HAnimSegment650.name = "r_metatarsal_5"
Transform651 = x3d.Transform()
Transform651.translation = [0,1,0]
Shape652 = x3d.Shape()
Shape652.USE = "HAnimJointShape"

Transform651.children.append(Shape652)

HAnimSegment650.children.append(Transform651)
Transform653 = x3d.Transform()
Shape654 = x3d.Shape()
LineSet655 = x3d.LineSet()
LineSet655.vertexCount = [2]
Coordinate656 = x3d.Coordinate()

LineSet655.coord = Coordinate656
ColorRGBA657 = x3d.ColorRGBA()
ColorRGBA657.USE = "HAnimSegmentLineColorRGBA"

LineSet655.color = ColorRGBA657

Shape654.geometry = LineSet655

Transform653.children.append(Shape654)

HAnimSegment650.children.append(Transform653)

HAnimJoint649.children.append(HAnimSegment650)
HAnimJoint658 = x3d.HAnimJoint()
HAnimJoint658.DEF = "STD_Joint_r_metatarsophalangeal_5"
HAnimJoint658.name = "r_metatarsophalangeal_5"
HAnimJoint658.center = [0,1,0]
HAnimSegment659 = x3d.HAnimSegment()
HAnimSegment659.DEF = "STD_Segment_r_tarsal_proximal_phalanx_5"
HAnimSegment659.name = "r_tarsal_proximal_phalanx_5"
Transform660 = x3d.Transform()
Transform660.translation = [0,1,0]
Shape661 = x3d.Shape()
Shape661.USE = "HAnimJointShape"

Transform660.children.append(Shape661)

HAnimSegment659.children.append(Transform660)
Transform662 = x3d.Transform()
Shape663 = x3d.Shape()
LineSet664 = x3d.LineSet()
LineSet664.vertexCount = [2]
Coordinate665 = x3d.Coordinate()

LineSet664.coord = Coordinate665
ColorRGBA666 = x3d.ColorRGBA()
ColorRGBA666.USE = "HAnimSegmentLineColorRGBA"

LineSet664.color = ColorRGBA666

Shape663.geometry = LineSet664

Transform662.children.append(Shape663)

HAnimSegment659.children.append(Transform662)
HAnimSite667 = x3d.HAnimSite()
HAnimSite667.DEF = "STD_Site_r_metatarsal_phalanx_5_pt"
HAnimSite667.name = "r_metatarsal_phalanx_5_pt"
TouchSensor668 = x3d.TouchSensor()
TouchSensor668.description = "HAnimSite r_metatarsal_phalanx_5_pt"

HAnimSite667.children.append(TouchSensor668)
Shape669 = x3d.Shape()
Shape669.USE = "HAnimSiteShape"

HAnimSite667.children.append(Shape669)

HAnimSegment659.children.append(HAnimSite667)

HAnimJoint658.children.append(HAnimSegment659)
HAnimJoint670 = x3d.HAnimJoint()
HAnimJoint670.DEF = "STD_Joint_r_tarsal_proximal_interphalangeal_5"
HAnimJoint670.name = "r_tarsal_proximal_interphalangeal_5"
HAnimJoint670.center = [0,1,0]
HAnimSegment671 = x3d.HAnimSegment()
HAnimSegment671.DEF = "STD_Segment_r_tarsal_middle_phalanx_5"
HAnimSegment671.name = "r_tarsal_middle_phalanx_5"
Transform672 = x3d.Transform()
Transform672.translation = [0,1,0]
Shape673 = x3d.Shape()
Shape673.USE = "HAnimJointShape"

Transform672.children.append(Shape673)

HAnimSegment671.children.append(Transform672)
Transform674 = x3d.Transform()
Shape675 = x3d.Shape()
LineSet676 = x3d.LineSet()
LineSet676.vertexCount = [2]
Coordinate677 = x3d.Coordinate()

LineSet676.coord = Coordinate677
ColorRGBA678 = x3d.ColorRGBA()
ColorRGBA678.USE = "HAnimSegmentLineColorRGBA"

LineSet676.color = ColorRGBA678

Shape675.geometry = LineSet676

Transform674.children.append(Shape675)

HAnimSegment671.children.append(Transform674)

HAnimJoint670.children.append(HAnimSegment671)
HAnimJoint679 = x3d.HAnimJoint()
HAnimJoint679.DEF = "STD_Joint_r_tarsal_distal_interphalangeal_5"
HAnimJoint679.name = "r_tarsal_distal_interphalangeal_5"
HAnimJoint679.center = [0,1,0]
HAnimSegment680 = x3d.HAnimSegment()
HAnimSegment680.DEF = "STD_Segment_r_tarsal_distal_phalanx_5"
HAnimSegment680.name = "r_tarsal_distal_phalanx_5"
Transform681 = x3d.Transform()
Transform681.translation = [0,1,0]
Shape682 = x3d.Shape()
Shape682.USE = "HAnimJointShape"

Transform681.children.append(Shape682)

HAnimSegment680.children.append(Transform681)
Transform683 = x3d.Transform()
Shape684 = x3d.Shape()
LineSet685 = x3d.LineSet()
LineSet685.vertexCount = [2]
Coordinate686 = x3d.Coordinate()

LineSet685.coord = Coordinate686
ColorRGBA687 = x3d.ColorRGBA()
ColorRGBA687.USE = "HAnimSegmentLineColorRGBA"

LineSet685.color = ColorRGBA687

Shape684.geometry = LineSet685

Transform683.children.append(Shape684)

HAnimSegment680.children.append(Transform683)
HAnimSite688 = x3d.HAnimSite()
HAnimSite688.DEF = "STD_Site_r_tarsal_distal_phalanx_5_tip"
HAnimSite688.name = "r_tarsal_distal_phalanx_5_tip"
TouchSensor689 = x3d.TouchSensor()
TouchSensor689.description = "HAnimSite r_tarsal_distal_phalanx_5_tip"

HAnimSite688.children.append(TouchSensor689)
Shape690 = x3d.Shape()
Shape690.USE = "HAnimSiteShape"

HAnimSite688.children.append(Shape690)

HAnimSegment680.children.append(HAnimSite688)

HAnimJoint679.children.append(HAnimSegment680)

HAnimJoint670.children.append(HAnimJoint679)

HAnimJoint658.children.append(HAnimJoint670)

HAnimJoint649.children.append(HAnimJoint658)

HAnimJoint601.children.append(HAnimJoint649)

HAnimJoint592.children.append(HAnimJoint601)

HAnimJoint430.children.append(HAnimJoint592)

HAnimJoint412.children.append(HAnimJoint430)

HAnimJoint391.children.append(HAnimJoint412)

HAnimJoint52.children.append(HAnimJoint391)

HAnimJoint43.children.append(HAnimJoint52)
HAnimJoint691 = x3d.HAnimJoint()
HAnimJoint691.DEF = "STD_Joint_vl5"
HAnimJoint691.name = "vl5"
HAnimJoint691.center = [0.0028,1.0568,-0.0776]
HAnimSegment692 = x3d.HAnimSegment()
HAnimSegment692.DEF = "STD_Segment_l5"
HAnimSegment692.name = "l5"
Transform693 = x3d.Transform()
Transform693.translation = [0.0028,1.0568,-0.0776]
Shape694 = x3d.Shape()
Shape694.USE = "HAnimJointShape"

Transform693.children.append(Shape694)

HAnimSegment692.children.append(Transform693)
Transform695 = x3d.Transform()
Shape696 = x3d.Shape()
LineSet697 = x3d.LineSet()
LineSet697.vertexCount = [2]
Coordinate698 = x3d.Coordinate()

LineSet697.coord = Coordinate698
ColorRGBA699 = x3d.ColorRGBA()
ColorRGBA699.USE = "HAnimSegmentLineColorRGBA"

LineSet697.color = ColorRGBA699

Shape696.geometry = LineSet697

Transform695.children.append(Shape696)

HAnimSegment692.children.append(Transform695)
HAnimSite700 = x3d.HAnimSite()
HAnimSite700.DEF = "STD_Site_navel_pt"
HAnimSite700.name = "navel_pt"
HAnimSite700.translation = [0.0069,1.0966,0.1017]
TouchSensor701 = x3d.TouchSensor()
TouchSensor701.description = "HAnimSite navel_pt"

HAnimSite700.children.append(TouchSensor701)
Shape702 = x3d.Shape()
Shape702.USE = "HAnimSiteShape"

HAnimSite700.children.append(Shape702)

HAnimSegment692.children.append(HAnimSite700)
HAnimSite703 = x3d.HAnimSite()
HAnimSite703.DEF = "STD_Site_waist_preferred_anterior_pt"
HAnimSite703.name = "waist_preferred_anterior_pt"
TouchSensor704 = x3d.TouchSensor()
TouchSensor704.description = "HAnimSite waist_preferred_anterior_pt"

HAnimSite703.children.append(TouchSensor704)
Shape705 = x3d.Shape()
Shape705.USE = "HAnimSiteShape"

HAnimSite703.children.append(Shape705)

HAnimSegment692.children.append(HAnimSite703)
HAnimSite706 = x3d.HAnimSite()
HAnimSite706.DEF = "STD_Site_waist_preferred_posterior_pt"
HAnimSite706.name = "waist_preferred_posterior_pt"
HAnimSite706.translation = [0.2900,1.0915,-0.1091]
TouchSensor707 = x3d.TouchSensor()
TouchSensor707.description = "HAnimSite waist_preferred_posterior_pt"

HAnimSite706.children.append(TouchSensor707)
Shape708 = x3d.Shape()
Shape708.USE = "HAnimSiteShape"

HAnimSite706.children.append(Shape708)

HAnimSegment692.children.append(HAnimSite706)

HAnimJoint691.children.append(HAnimSegment692)
HAnimJoint709 = x3d.HAnimJoint()
HAnimJoint709.DEF = "STD_Joint_vl4"
HAnimJoint709.name = "vl4"
HAnimJoint709.center = [0.0035,1.0925,-0.0787]
HAnimSegment710 = x3d.HAnimSegment()
HAnimSegment710.DEF = "STD_Segment_l4"
HAnimSegment710.name = "l4"
Transform711 = x3d.Transform()
Transform711.translation = [0.0035,1.0925,-0.0787]
Shape712 = x3d.Shape()
Shape712.USE = "HAnimJointShape"

Transform711.children.append(Shape712)

HAnimSegment710.children.append(Transform711)
Transform713 = x3d.Transform()
Shape714 = x3d.Shape()
LineSet715 = x3d.LineSet()
LineSet715.vertexCount = [2]
Coordinate716 = x3d.Coordinate()

LineSet715.coord = Coordinate716
ColorRGBA717 = x3d.ColorRGBA()
ColorRGBA717.USE = "HAnimSegmentLineColorRGBA"

LineSet715.color = ColorRGBA717

Shape714.geometry = LineSet715

Transform713.children.append(Shape714)

HAnimSegment710.children.append(Transform713)

HAnimJoint709.children.append(HAnimSegment710)
HAnimJoint718 = x3d.HAnimJoint()
HAnimJoint718.DEF = "STD_Joint_vl3"
HAnimJoint718.name = "vl3"
HAnimJoint718.center = [0.0041,1.1276,-0.0796]
HAnimSegment719 = x3d.HAnimSegment()
HAnimSegment719.DEF = "STD_Segment_l3"
HAnimSegment719.name = "l3"
Transform720 = x3d.Transform()
Transform720.translation = [0.0041,1.1276,-0.0796]
Shape721 = x3d.Shape()
Shape721.USE = "HAnimJointShape"

Transform720.children.append(Shape721)

HAnimSegment719.children.append(Transform720)
Transform722 = x3d.Transform()
Shape723 = x3d.Shape()
LineSet724 = x3d.LineSet()
LineSet724.vertexCount = [2]
Coordinate725 = x3d.Coordinate()

LineSet724.coord = Coordinate725
ColorRGBA726 = x3d.ColorRGBA()
ColorRGBA726.USE = "HAnimSegmentLineColorRGBA"

LineSet724.color = ColorRGBA726

Shape723.geometry = LineSet724

Transform722.children.append(Shape723)

HAnimSegment719.children.append(Transform722)

HAnimJoint718.children.append(HAnimSegment719)
HAnimJoint727 = x3d.HAnimJoint()
HAnimJoint727.DEF = "STD_Joint_vl2"
HAnimJoint727.name = "vl2"
HAnimJoint727.center = [0.0045,1.1546,-0.0800]
HAnimSegment728 = x3d.HAnimSegment()
HAnimSegment728.DEF = "STD_Segment_l2"
HAnimSegment728.name = "l2"
Transform729 = x3d.Transform()
Transform729.translation = [0.0045,1.1546,-0.0800]
Shape730 = x3d.Shape()
Shape730.USE = "HAnimJointShape"

Transform729.children.append(Shape730)

HAnimSegment728.children.append(Transform729)
Transform731 = x3d.Transform()
Shape732 = x3d.Shape()
LineSet733 = x3d.LineSet()
LineSet733.vertexCount = [2]
Coordinate734 = x3d.Coordinate()

LineSet733.coord = Coordinate734
ColorRGBA735 = x3d.ColorRGBA()
ColorRGBA735.USE = "HAnimSegmentLineColorRGBA"

LineSet733.color = ColorRGBA735

Shape732.geometry = LineSet733

Transform731.children.append(Shape732)

HAnimSegment728.children.append(Transform731)
HAnimSite736 = x3d.HAnimSite()
HAnimSite736.DEF = "STD_Site_l_rib10_pt"
HAnimSite736.name = "l_rib10_pt"
HAnimSite736.translation = [0.0871,1.1925,0.0992]
TouchSensor737 = x3d.TouchSensor()
TouchSensor737.description = "HAnimSite l_rib10_pt"

HAnimSite736.children.append(TouchSensor737)
Shape738 = x3d.Shape()
Shape738.USE = "HAnimSiteShape"

HAnimSite736.children.append(Shape738)

HAnimSegment728.children.append(HAnimSite736)
HAnimSite739 = x3d.HAnimSite()
HAnimSite739.DEF = "STD_Site_r_rib10_pt"
HAnimSite739.name = "r_rib10_pt"
HAnimSite739.translation = [-0.0711,1.1941,0.1016]
TouchSensor740 = x3d.TouchSensor()
TouchSensor740.description = "HAnimSite r_rib10_pt"

HAnimSite739.children.append(TouchSensor740)
Shape741 = x3d.Shape()
Shape741.USE = "HAnimSiteShape"

HAnimSite739.children.append(Shape741)

HAnimSegment728.children.append(HAnimSite739)
HAnimSite742 = x3d.HAnimSite()
HAnimSite742.DEF = "STD_Site_spine_2_middle_back_pt"
HAnimSite742.name = "spine_2_middle_back_pt"
TouchSensor743 = x3d.TouchSensor()
TouchSensor743.description = "HAnimSite spine_2_middle_back_pt"

HAnimSite742.children.append(TouchSensor743)
Shape744 = x3d.Shape()
Shape744.USE = "HAnimSiteShape"

HAnimSite742.children.append(Shape744)

HAnimSegment728.children.append(HAnimSite742)

HAnimJoint727.children.append(HAnimSegment728)
HAnimJoint745 = x3d.HAnimJoint()
HAnimJoint745.DEF = "STD_Joint_vl1"
HAnimJoint745.name = "vl1"
HAnimJoint745.center = [0.0048,1.1912,-0.0805]
HAnimSegment746 = x3d.HAnimSegment()
HAnimSegment746.DEF = "STD_Segment_l1"
HAnimSegment746.name = "l1"
Transform747 = x3d.Transform()
Transform747.translation = [0.0048,1.1912,-0.0805]
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

HAnimJoint745.children.append(HAnimSegment746)
HAnimJoint754 = x3d.HAnimJoint()
HAnimJoint754.DEF = "STD_Joint_vt12"
HAnimJoint754.name = "vt12"
HAnimJoint754.center = [0.0051,1.2278,-0.0808]
HAnimSegment755 = x3d.HAnimSegment()
HAnimSegment755.DEF = "STD_Segment_t12"
HAnimSegment755.name = "t12"
Transform756 = x3d.Transform()
Transform756.translation = [0.0051,1.2278,-0.0808]
Shape757 = x3d.Shape()
Shape757.USE = "HAnimJointShape"

Transform756.children.append(Shape757)

HAnimSegment755.children.append(Transform756)
Transform758 = x3d.Transform()
Shape759 = x3d.Shape()
LineSet760 = x3d.LineSet()
LineSet760.vertexCount = [2]
Coordinate761 = x3d.Coordinate()

LineSet760.coord = Coordinate761
ColorRGBA762 = x3d.ColorRGBA()
ColorRGBA762.USE = "HAnimSegmentLineColorRGBA"

LineSet760.color = ColorRGBA762

Shape759.geometry = LineSet760

Transform758.children.append(Shape759)

HAnimSegment755.children.append(Transform758)

HAnimJoint754.children.append(HAnimSegment755)
HAnimJoint763 = x3d.HAnimJoint()
HAnimJoint763.DEF = "STD_Joint_vt11"
HAnimJoint763.name = "vt11"
HAnimJoint763.center = [0.0053,1.2679,-0.0810]
HAnimSegment764 = x3d.HAnimSegment()
HAnimSegment764.DEF = "STD_Segment_t11"
HAnimSegment764.name = "t11"
Transform765 = x3d.Transform()
Transform765.translation = [0.0053,1.2679,-0.0810]
Shape766 = x3d.Shape()
Shape766.USE = "HAnimJointShape"

Transform765.children.append(Shape766)

HAnimSegment764.children.append(Transform765)
Transform767 = x3d.Transform()
Shape768 = x3d.Shape()
LineSet769 = x3d.LineSet()
LineSet769.vertexCount = [2]
Coordinate770 = x3d.Coordinate()

LineSet769.coord = Coordinate770
ColorRGBA771 = x3d.ColorRGBA()
ColorRGBA771.USE = "HAnimSegmentLineColorRGBA"

LineSet769.color = ColorRGBA771

Shape768.geometry = LineSet769

Transform767.children.append(Shape768)

HAnimSegment764.children.append(Transform767)

HAnimJoint763.children.append(HAnimSegment764)
HAnimJoint772 = x3d.HAnimJoint()
HAnimJoint772.DEF = "STD_Joint_vt10"
HAnimJoint772.name = "vt10"
HAnimJoint772.center = [0.0056,1.2848,-0.0822]
HAnimSegment773 = x3d.HAnimSegment()
HAnimSegment773.DEF = "STD_Segment_t10"
HAnimSegment773.name = "t10"
Transform774 = x3d.Transform()
Transform774.translation = [0.0056,1.2848,-0.0822]
Shape775 = x3d.Shape()
Shape775.USE = "HAnimJointShape"

Transform774.children.append(Shape775)

HAnimSegment773.children.append(Transform774)
Transform776 = x3d.Transform()
Shape777 = x3d.Shape()
LineSet778 = x3d.LineSet()
LineSet778.vertexCount = [2]
Coordinate779 = x3d.Coordinate()

LineSet778.coord = Coordinate779
ColorRGBA780 = x3d.ColorRGBA()
ColorRGBA780.USE = "HAnimSegmentLineColorRGBA"

LineSet778.color = ColorRGBA780

Shape777.geometry = LineSet778

Transform776.children.append(Shape777)

HAnimSegment773.children.append(Transform776)
HAnimSite781 = x3d.HAnimSite()
HAnimSite781.DEF = "STD_Site_substernale_pt"
HAnimSite781.name = "substernale_pt"
HAnimSite781.translation = [0.0085,1.2995,0.1147]
TouchSensor782 = x3d.TouchSensor()
TouchSensor782.description = "HAnimSite substernale_pt"

HAnimSite781.children.append(TouchSensor782)
Shape783 = x3d.Shape()
Shape783.USE = "HAnimSiteShape"

HAnimSite781.children.append(Shape783)

HAnimSegment773.children.append(HAnimSite781)

HAnimJoint772.children.append(HAnimSegment773)
HAnimJoint784 = x3d.HAnimJoint()
HAnimJoint784.DEF = "STD_Joint_vt9"
HAnimJoint784.name = "vt9"
HAnimJoint784.center = [0.0057,1.3126,-0.0838]
HAnimSegment785 = x3d.HAnimSegment()
HAnimSegment785.DEF = "STD_Segment_t9"
HAnimSegment785.name = "t9"
Transform786 = x3d.Transform()
Transform786.translation = [0.0057,1.3126,-0.0838]
Shape787 = x3d.Shape()
Shape787.USE = "HAnimJointShape"

Transform786.children.append(Shape787)

HAnimSegment785.children.append(Transform786)
Transform788 = x3d.Transform()
Shape789 = x3d.Shape()
LineSet790 = x3d.LineSet()
LineSet790.vertexCount = [2]
Coordinate791 = x3d.Coordinate()

LineSet790.coord = Coordinate791
ColorRGBA792 = x3d.ColorRGBA()
ColorRGBA792.USE = "HAnimSegmentLineColorRGBA"

LineSet790.color = ColorRGBA792

Shape789.geometry = LineSet790

Transform788.children.append(Shape789)

HAnimSegment785.children.append(Transform788)
HAnimSite793 = x3d.HAnimSite()
HAnimSite793.DEF = "STD_Site_l_thelion_pt"
HAnimSite793.name = "l_thelion_pt"
HAnimSite793.translation = [0.0918,1.3382,0.1192]
TouchSensor794 = x3d.TouchSensor()
TouchSensor794.description = "HAnimSite l_thelion_pt"

HAnimSite793.children.append(TouchSensor794)
Shape795 = x3d.Shape()
Shape795.USE = "HAnimSiteShape"

HAnimSite793.children.append(Shape795)

HAnimSegment785.children.append(HAnimSite793)
HAnimSite796 = x3d.HAnimSite()
HAnimSite796.DEF = "STD_Site_r_thelion_pt"
HAnimSite796.name = "r_thelion_pt"
HAnimSite796.translation = [-0.0736,1.3385,0.1217]
TouchSensor797 = x3d.TouchSensor()
TouchSensor797.description = "HAnimSite r_thelion_pt"

HAnimSite796.children.append(TouchSensor797)
Shape798 = x3d.Shape()
Shape798.USE = "HAnimSiteShape"

HAnimSite796.children.append(Shape798)

HAnimSegment785.children.append(HAnimSite796)

HAnimJoint784.children.append(HAnimSegment785)
HAnimJoint799 = x3d.HAnimJoint()
HAnimJoint799.DEF = "STD_Joint_vt8"
HAnimJoint799.name = "vt8"
HAnimJoint799.center = [0.0057,1.3382,-0.0845]
HAnimSegment800 = x3d.HAnimSegment()
HAnimSegment800.DEF = "STD_Segment_t8"
HAnimSegment800.name = "t8"
Transform801 = x3d.Transform()
Transform801.translation = [0.0057,1.3382,-0.0845]
Shape802 = x3d.Shape()
Shape802.USE = "HAnimJointShape"

Transform801.children.append(Shape802)

HAnimSegment800.children.append(Transform801)
Transform803 = x3d.Transform()
Shape804 = x3d.Shape()
LineSet805 = x3d.LineSet()
LineSet805.vertexCount = [2]
Coordinate806 = x3d.Coordinate()

LineSet805.coord = Coordinate806
ColorRGBA807 = x3d.ColorRGBA()
ColorRGBA807.USE = "HAnimSegmentLineColorRGBA"

LineSet805.color = ColorRGBA807

Shape804.geometry = LineSet805

Transform803.children.append(Shape804)

HAnimSegment800.children.append(Transform803)

HAnimJoint799.children.append(HAnimSegment800)
HAnimJoint808 = x3d.HAnimJoint()
HAnimJoint808.DEF = "STD_Joint_vt7"
HAnimJoint808.name = "vt7"
HAnimJoint808.center = [0.0058,1.3625,-0.0833]
HAnimSegment809 = x3d.HAnimSegment()
HAnimSegment809.DEF = "STD_Segment_t7"
HAnimSegment809.name = "t7"
Transform810 = x3d.Transform()
Transform810.translation = [0.0058,1.3625,-0.0833]
Shape811 = x3d.Shape()
Shape811.USE = "HAnimJointShape"

Transform810.children.append(Shape811)

HAnimSegment809.children.append(Transform810)
Transform812 = x3d.Transform()
Shape813 = x3d.Shape()
LineSet814 = x3d.LineSet()
LineSet814.vertexCount = [2]
Coordinate815 = x3d.Coordinate()

LineSet814.coord = Coordinate815
ColorRGBA816 = x3d.ColorRGBA()
ColorRGBA816.USE = "HAnimSegmentLineColorRGBA"

LineSet814.color = ColorRGBA816

Shape813.geometry = LineSet814

Transform812.children.append(Shape813)

HAnimSegment809.children.append(Transform812)

HAnimJoint808.children.append(HAnimSegment809)
HAnimJoint817 = x3d.HAnimJoint()
HAnimJoint817.DEF = "STD_Joint_vt6"
HAnimJoint817.name = "vt6"
HAnimJoint817.center = [0.0059,1.3866,-0.0800]
HAnimSegment818 = x3d.HAnimSegment()
HAnimSegment818.DEF = "STD_Segment_t6"
HAnimSegment818.name = "t6"
Transform819 = x3d.Transform()
Transform819.translation = [0.0059,1.3866,-0.0800]
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
HAnimSite826.DEF = "STD_Site_l_chest_midsagittal_plane_pt"
HAnimSite826.name = "l_chest_midsagittal_plane_pt"
TouchSensor827 = x3d.TouchSensor()
TouchSensor827.description = "HAnimSite l_chest_midsagittal_plane_pt"

HAnimSite826.children.append(TouchSensor827)
Shape828 = x3d.Shape()
Shape828.USE = "HAnimSiteShape"

HAnimSite826.children.append(Shape828)

HAnimSegment818.children.append(HAnimSite826)
HAnimSite829 = x3d.HAnimSite()
HAnimSite829.DEF = "STD_Site_mesosternale_pt"
HAnimSite829.name = "mesosternale_pt"
TouchSensor830 = x3d.TouchSensor()
TouchSensor830.description = "HAnimSite mesosternale_pt"

HAnimSite829.children.append(TouchSensor830)
Shape831 = x3d.Shape()
Shape831.USE = "HAnimSiteShape"

HAnimSite829.children.append(Shape831)

HAnimSegment818.children.append(HAnimSite829)
HAnimSite832 = x3d.HAnimSite()
HAnimSite832.DEF = "STD_Site_r_chest_midsagittal_plane_pt"
HAnimSite832.name = "r_chest_midsagittal_plane_pt"
TouchSensor833 = x3d.TouchSensor()
TouchSensor833.description = "HAnimSite r_chest_midsagittal_plane_pt"

HAnimSite832.children.append(TouchSensor833)
Shape834 = x3d.Shape()
Shape834.USE = "HAnimSiteShape"

HAnimSite832.children.append(Shape834)

HAnimSegment818.children.append(HAnimSite832)
HAnimSite835 = x3d.HAnimSite()
HAnimSite835.DEF = "STD_Site_rear_center_midsagittal_plane_pt"
HAnimSite835.name = "rear_center_midsagittal_plane_pt"
TouchSensor836 = x3d.TouchSensor()
TouchSensor836.description = "HAnimSite rear_center_midsagittal_plane_pt"

HAnimSite835.children.append(TouchSensor836)
Shape837 = x3d.Shape()
Shape837.USE = "HAnimSiteShape"

HAnimSite835.children.append(Shape837)

HAnimSegment818.children.append(HAnimSite835)

HAnimJoint817.children.append(HAnimSegment818)
HAnimJoint838 = x3d.HAnimJoint()
HAnimJoint838.DEF = "STD_Joint_vt5"
HAnimJoint838.name = "vt5"
HAnimJoint838.center = [0.0060,1.4102,-0.0745]
HAnimSegment839 = x3d.HAnimSegment()
HAnimSegment839.DEF = "STD_Segment_t5"
HAnimSegment839.name = "t5"
Transform840 = x3d.Transform()
Transform840.translation = [0.0060,1.4102,-0.0745]
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
HAnimSite847 = x3d.HAnimSite()
HAnimSite847.DEF = "STD_Site_spine_1_middle_back_pt"
HAnimSite847.name = "spine_1_middle_back_pt"
TouchSensor848 = x3d.TouchSensor()
TouchSensor848.description = "HAnimSite spine_1_middle_back_pt"

HAnimSite847.children.append(TouchSensor848)
Shape849 = x3d.Shape()
Shape849.USE = "HAnimSiteShape"

HAnimSite847.children.append(Shape849)

HAnimSegment839.children.append(HAnimSite847)

HAnimJoint838.children.append(HAnimSegment839)
HAnimJoint850 = x3d.HAnimJoint()
HAnimJoint850.DEF = "STD_Joint_vt4"
HAnimJoint850.name = "vt4"
HAnimJoint850.center = [0.0061,1.4320,-0.0675]
HAnimSegment851 = x3d.HAnimSegment()
HAnimSegment851.DEF = "STD_Segment_t4"
HAnimSegment851.name = "t4"
Transform852 = x3d.Transform()
Transform852.translation = [0.0061,1.4320,-0.0675]
Shape853 = x3d.Shape()
Shape853.USE = "HAnimJointShape"

Transform852.children.append(Shape853)

HAnimSegment851.children.append(Transform852)
Transform854 = x3d.Transform()
Shape855 = x3d.Shape()
LineSet856 = x3d.LineSet()
LineSet856.vertexCount = [2]
Coordinate857 = x3d.Coordinate()

LineSet856.coord = Coordinate857
ColorRGBA858 = x3d.ColorRGBA()
ColorRGBA858.USE = "HAnimSegmentLineColorRGBA"

LineSet856.color = ColorRGBA858

Shape855.geometry = LineSet856

Transform854.children.append(Shape855)

HAnimSegment851.children.append(Transform854)

HAnimJoint850.children.append(HAnimSegment851)
HAnimJoint859 = x3d.HAnimJoint()
HAnimJoint859.DEF = "STD_Joint_vt3"
HAnimJoint859.name = "vt3"
HAnimJoint859.center = [0.0062,1.4583,-0.0570]
HAnimSegment860 = x3d.HAnimSegment()
HAnimSegment860.DEF = "STD_Segment_t3"
HAnimSegment860.name = "t3"
Transform861 = x3d.Transform()
Transform861.translation = [0.0062,1.4583,-0.0570]
Shape862 = x3d.Shape()
Shape862.USE = "HAnimJointShape"

Transform861.children.append(Shape862)

HAnimSegment860.children.append(Transform861)
Transform863 = x3d.Transform()
Shape864 = x3d.Shape()
LineSet865 = x3d.LineSet()
LineSet865.vertexCount = [2]
Coordinate866 = x3d.Coordinate()

LineSet865.coord = Coordinate866
ColorRGBA867 = x3d.ColorRGBA()
ColorRGBA867.USE = "HAnimSegmentLineColorRGBA"

LineSet865.color = ColorRGBA867

Shape864.geometry = LineSet865

Transform863.children.append(Shape864)

HAnimSegment860.children.append(Transform863)

HAnimJoint859.children.append(HAnimSegment860)
HAnimJoint868 = x3d.HAnimJoint()
HAnimJoint868.DEF = "STD_Joint_vt2"
HAnimJoint868.name = "vt2"
HAnimJoint868.center = [0.0063,1.4761,-0.0484]
HAnimSegment869 = x3d.HAnimSegment()
HAnimSegment869.DEF = "STD_Segment_t2"
HAnimSegment869.name = "t2"
Transform870 = x3d.Transform()
Transform870.translation = [0.0063,1.4761,-0.0484]
Shape871 = x3d.Shape()
Shape871.USE = "HAnimJointShape"

Transform870.children.append(Shape871)

HAnimSegment869.children.append(Transform870)
Transform872 = x3d.Transform()
Shape873 = x3d.Shape()
LineSet874 = x3d.LineSet()
LineSet874.vertexCount = [2]
Coordinate875 = x3d.Coordinate()

LineSet874.coord = Coordinate875
ColorRGBA876 = x3d.ColorRGBA()
ColorRGBA876.USE = "HAnimSegmentLineColorRGBA"

LineSet874.color = ColorRGBA876

Shape873.geometry = LineSet874

Transform872.children.append(Shape873)

HAnimSegment869.children.append(Transform872)

HAnimJoint868.children.append(HAnimSegment869)
HAnimJoint877 = x3d.HAnimJoint()
HAnimJoint877.DEF = "STD_Joint_vt1"
HAnimJoint877.name = "vt1"
HAnimJoint877.center = [0.0065,1.4951,-0.0387]
HAnimSegment878 = x3d.HAnimSegment()
HAnimSegment878.DEF = "STD_Segment_t1"
HAnimSegment878.name = "t1"
Transform879 = x3d.Transform()
Transform879.translation = [0.0065,1.4951,-0.0387]
Shape880 = x3d.Shape()
Shape880.USE = "HAnimJointShape"

Transform879.children.append(Shape880)

HAnimSegment878.children.append(Transform879)
Transform881 = x3d.Transform()
Shape882 = x3d.Shape()
LineSet883 = x3d.LineSet()
LineSet883.vertexCount = [2]
Coordinate884 = x3d.Coordinate()

LineSet883.coord = Coordinate884
ColorRGBA885 = x3d.ColorRGBA()
ColorRGBA885.USE = "HAnimSegmentLineColorRGBA"

LineSet883.color = ColorRGBA885

Shape882.geometry = LineSet883

Transform881.children.append(Shape882)

HAnimSegment878.children.append(Transform881)
HAnimSite886 = x3d.HAnimSite()
HAnimSite886.DEF = "STD_Site_cervicale_pt"
HAnimSite886.name = "cervicale_pt"
HAnimSite886.translation = [0.0064,1.520,-0.0815]
TouchSensor887 = x3d.TouchSensor()
TouchSensor887.description = "HAnimSite cervicale_pt"

HAnimSite886.children.append(TouchSensor887)
Shape888 = x3d.Shape()
Shape888.USE = "HAnimSiteShape"

HAnimSite886.children.append(Shape888)

HAnimSegment878.children.append(HAnimSite886)
HAnimSite889 = x3d.HAnimSite()
HAnimSite889.DEF = "STD_Site_suprasternale_pt"
HAnimSite889.name = "suprasternale_pt"
HAnimSite889.translation = [0.0084,1.4714,0.0551]
TouchSensor890 = x3d.TouchSensor()
TouchSensor890.description = "HAnimSite suprasternale_pt"

HAnimSite889.children.append(TouchSensor890)
Shape891 = x3d.Shape()
Shape891.USE = "HAnimSiteShape"

HAnimSite889.children.append(Shape891)

HAnimSegment878.children.append(HAnimSite889)

HAnimJoint877.children.append(HAnimSegment878)
HAnimJoint892 = x3d.HAnimJoint()
HAnimJoint892.DEF = "STD_Joint_vc7"
HAnimJoint892.name = "vc7"
HAnimJoint892.center = [0.0066,1.5132,-0.0301]
HAnimSegment893 = x3d.HAnimSegment()
HAnimSegment893.DEF = "STD_Segment_c7"
HAnimSegment893.name = "c7"
Transform894 = x3d.Transform()
Transform894.translation = [0.0066,1.5132,-0.0301]
Shape895 = x3d.Shape()
Shape895.USE = "HAnimJointShape"

Transform894.children.append(Shape895)

HAnimSegment893.children.append(Transform894)
Transform896 = x3d.Transform()
Shape897 = x3d.Shape()
LineSet898 = x3d.LineSet()
LineSet898.vertexCount = [2]
Coordinate899 = x3d.Coordinate()

LineSet898.coord = Coordinate899
ColorRGBA900 = x3d.ColorRGBA()
ColorRGBA900.USE = "HAnimSegmentLineColorRGBA"

LineSet898.color = ColorRGBA900

Shape897.geometry = LineSet898

Transform896.children.append(Shape897)

HAnimSegment893.children.append(Transform896)
HAnimSite901 = x3d.HAnimSite()
HAnimSite901.DEF = "STD_Site_l_neck_base_pt"
HAnimSite901.name = "l_neck_base_pt"
HAnimSite901.translation = [0.0646,1.5141,-0.0380]
TouchSensor902 = x3d.TouchSensor()
TouchSensor902.description = "HAnimSite l_neck_base_pt"

HAnimSite901.children.append(TouchSensor902)
Shape903 = x3d.Shape()
Shape903.USE = "HAnimSiteShape"

HAnimSite901.children.append(Shape903)

HAnimSegment893.children.append(HAnimSite901)
HAnimSite904 = x3d.HAnimSite()
HAnimSite904.DEF = "STD_Site_r_neck_base_pt"
HAnimSite904.name = "r_neck_base_pt"
HAnimSite904.translation = [-0.0419,1.5149,-0.0220]
TouchSensor905 = x3d.TouchSensor()
TouchSensor905.description = "HAnimSite r_neck_base_pt"

HAnimSite904.children.append(TouchSensor905)
Shape906 = x3d.Shape()
Shape906.USE = "HAnimSiteShape"

HAnimSite904.children.append(Shape906)

HAnimSegment893.children.append(HAnimSite904)

HAnimJoint892.children.append(HAnimSegment893)
HAnimJoint907 = x3d.HAnimJoint()
HAnimJoint907.DEF = "STD_Joint_vc6"
HAnimJoint907.name = "vc6"
HAnimJoint907.center = [0.0066,1.5357,-0.0143]
HAnimSegment908 = x3d.HAnimSegment()
HAnimSegment908.DEF = "STD_Segment_c6"
HAnimSegment908.name = "c6"
Transform909 = x3d.Transform()
Transform909.translation = [0.0066,1.5357,-0.0143]
Shape910 = x3d.Shape()
Shape910.USE = "HAnimJointShape"

Transform909.children.append(Shape910)

HAnimSegment908.children.append(Transform909)
Transform911 = x3d.Transform()
Shape912 = x3d.Shape()
LineSet913 = x3d.LineSet()
LineSet913.vertexCount = [2]
Coordinate914 = x3d.Coordinate()

LineSet913.coord = Coordinate914
ColorRGBA915 = x3d.ColorRGBA()
ColorRGBA915.USE = "HAnimSegmentLineColorRGBA"

LineSet913.color = ColorRGBA915

Shape912.geometry = LineSet913

Transform911.children.append(Shape912)

HAnimSegment908.children.append(Transform911)

HAnimJoint907.children.append(HAnimSegment908)
HAnimJoint916 = x3d.HAnimJoint()
HAnimJoint916.DEF = "STD_Joint_vc5"
HAnimJoint916.name = "vc5"
HAnimJoint916.center = [0.0066,1.5520,-0.0082]
HAnimSegment917 = x3d.HAnimSegment()
HAnimSegment917.DEF = "STD_Segment_c5"
HAnimSegment917.name = "c5"
Transform918 = x3d.Transform()
Transform918.translation = [0.0066,1.5520,-0.0082]
Shape919 = x3d.Shape()
Shape919.USE = "HAnimJointShape"

Transform918.children.append(Shape919)

HAnimSegment917.children.append(Transform918)
Transform920 = x3d.Transform()
Shape921 = x3d.Shape()
LineSet922 = x3d.LineSet()
LineSet922.vertexCount = [2]
Coordinate923 = x3d.Coordinate()

LineSet922.coord = Coordinate923
ColorRGBA924 = x3d.ColorRGBA()
ColorRGBA924.USE = "HAnimSegmentLineColorRGBA"

LineSet922.color = ColorRGBA924

Shape921.geometry = LineSet922

Transform920.children.append(Shape921)

HAnimSegment917.children.append(Transform920)

HAnimJoint916.children.append(HAnimSegment917)
HAnimJoint925 = x3d.HAnimJoint()
HAnimJoint925.DEF = "STD_Joint_vc4"
HAnimJoint925.name = "vc4"
HAnimJoint925.center = [0.0066,1.5662,-0.0084]
HAnimSegment926 = x3d.HAnimSegment()
HAnimSegment926.DEF = "STD_Segment_c4"
HAnimSegment926.name = "c4"
Transform927 = x3d.Transform()
Transform927.translation = [0.0066,1.5662,-0.0084]
Shape928 = x3d.Shape()
Shape928.USE = "HAnimJointShape"

Transform927.children.append(Shape928)

HAnimSegment926.children.append(Transform927)
Transform929 = x3d.Transform()
Shape930 = x3d.Shape()
LineSet931 = x3d.LineSet()
LineSet931.vertexCount = [2]
Coordinate932 = x3d.Coordinate()

LineSet931.coord = Coordinate932
ColorRGBA933 = x3d.ColorRGBA()
ColorRGBA933.USE = "HAnimSegmentLineColorRGBA"

LineSet931.color = ColorRGBA933

Shape930.geometry = LineSet931

Transform929.children.append(Shape930)

HAnimSegment926.children.append(Transform929)

HAnimJoint925.children.append(HAnimSegment926)
HAnimJoint934 = x3d.HAnimJoint()
HAnimJoint934.DEF = "STD_Joint_vc3"
HAnimJoint934.name = "vc3"
HAnimJoint934.center = [0.0066,1.5800,-0.0103]
HAnimSegment935 = x3d.HAnimSegment()
HAnimSegment935.DEF = "STD_Segment_c3"
HAnimSegment935.name = "c3"
Transform936 = x3d.Transform()
Transform936.translation = [0.0066,1.5800,-0.0103]
Shape937 = x3d.Shape()
Shape937.USE = "HAnimJointShape"

Transform936.children.append(Shape937)

HAnimSegment935.children.append(Transform936)
Transform938 = x3d.Transform()
Shape939 = x3d.Shape()
LineSet940 = x3d.LineSet()
LineSet940.vertexCount = [2]
Coordinate941 = x3d.Coordinate()

LineSet940.coord = Coordinate941
ColorRGBA942 = x3d.ColorRGBA()
ColorRGBA942.USE = "HAnimSegmentLineColorRGBA"

LineSet940.color = ColorRGBA942

Shape939.geometry = LineSet940

Transform938.children.append(Shape939)

HAnimSegment935.children.append(Transform938)

HAnimJoint934.children.append(HAnimSegment935)
HAnimJoint943 = x3d.HAnimJoint()
HAnimJoint943.DEF = "STD_Joint_vc2"
HAnimJoint943.name = "vc2"
HAnimJoint943.center = [0.0066,1.5928,-0.0103]
HAnimSegment944 = x3d.HAnimSegment()
HAnimSegment944.DEF = "STD_Segment_c2"
HAnimSegment944.name = "c2"
Transform945 = x3d.Transform()
Transform945.translation = [0.0066,1.5928,-0.0103]
Shape946 = x3d.Shape()
Shape946.USE = "HAnimJointShape"

Transform945.children.append(Shape946)

HAnimSegment944.children.append(Transform945)
Transform947 = x3d.Transform()
Shape948 = x3d.Shape()
LineSet949 = x3d.LineSet()
LineSet949.vertexCount = [2]
Coordinate950 = x3d.Coordinate()

LineSet949.coord = Coordinate950
ColorRGBA951 = x3d.ColorRGBA()
ColorRGBA951.USE = "HAnimSegmentLineColorRGBA"

LineSet949.color = ColorRGBA951

Shape948.geometry = LineSet949

Transform947.children.append(Shape948)

HAnimSegment944.children.append(Transform947)
HAnimSite952 = x3d.HAnimSite()
HAnimSite952.DEF = "STD_Site_adams_apple_pt"
HAnimSite952.name = "adams_apple_pt"
TouchSensor953 = x3d.TouchSensor()
TouchSensor953.description = "HAnimSite adams_apple_pt"

HAnimSite952.children.append(TouchSensor953)
Shape954 = x3d.Shape()
Shape954.USE = "HAnimSiteShape"

HAnimSite952.children.append(Shape954)

HAnimSegment944.children.append(HAnimSite952)

HAnimJoint943.children.append(HAnimSegment944)
HAnimJoint955 = x3d.HAnimJoint()
HAnimJoint955.DEF = "STD_Joint_vc1"
HAnimJoint955.name = "vc1"
HAnimJoint955.center = [0.0066,1.6144,-0.0034]
HAnimSegment956 = x3d.HAnimSegment()
HAnimSegment956.DEF = "STD_Segment_c1"
HAnimSegment956.name = "c1"
Transform957 = x3d.Transform()
Transform957.translation = [0.0066,1.6144,-0.0034]
Shape958 = x3d.Shape()
Shape958.USE = "HAnimJointShape"

Transform957.children.append(Shape958)

HAnimSegment956.children.append(Transform957)
Transform959 = x3d.Transform()
Shape960 = x3d.Shape()
LineSet961 = x3d.LineSet()
LineSet961.vertexCount = [2]
Coordinate962 = x3d.Coordinate()

LineSet961.coord = Coordinate962
ColorRGBA963 = x3d.ColorRGBA()
ColorRGBA963.USE = "HAnimSegmentLineColorRGBA"

LineSet961.color = ColorRGBA963

Shape960.geometry = LineSet961

Transform959.children.append(Shape960)

HAnimSegment956.children.append(Transform959)

HAnimJoint955.children.append(HAnimSegment956)
HAnimJoint964 = x3d.HAnimJoint()
HAnimJoint964.DEF = "STD_Joint_skullbase"
HAnimJoint964.name = "skullbase"
HAnimJoint964.center = [0.0044,1.6209,0.0236]
HAnimSegment965 = x3d.HAnimSegment()
HAnimSegment965.DEF = "STD_Segment_skull"
HAnimSegment965.name = "skull"
Transform966 = x3d.Transform()
Transform966.translation = [0.0044,1.6209,0.0236]
Shape967 = x3d.Shape()
Shape967.USE = "HAnimJointShape"

Transform966.children.append(Shape967)

HAnimSegment965.children.append(Transform966)
Transform968 = x3d.Transform()
Shape969 = x3d.Shape()
LineSet970 = x3d.LineSet()
LineSet970.vertexCount = [2]
Coordinate971 = x3d.Coordinate()

LineSet970.coord = Coordinate971
ColorRGBA972 = x3d.ColorRGBA()
ColorRGBA972.USE = "HAnimSegmentLineColorRGBA"

LineSet970.color = ColorRGBA972

Shape969.geometry = LineSet970

Transform968.children.append(Shape969)

HAnimSegment965.children.append(Transform968)
HAnimSite973 = x3d.HAnimSite()
HAnimSite973.DEF = "STD_Site_glabella_pt"
HAnimSite973.name = "glabella_pt"
TouchSensor974 = x3d.TouchSensor()
TouchSensor974.description = "HAnimSite glabella_pt"

HAnimSite973.children.append(TouchSensor974)
Shape975 = x3d.Shape()
Shape975.USE = "HAnimSiteShape"

HAnimSite973.children.append(Shape975)

HAnimSegment965.children.append(HAnimSite973)
HAnimSite976 = x3d.HAnimSite()
HAnimSite976.DEF = "STD_Site_l_ectocanthus_pt"
HAnimSite976.name = "l_ectocanthus_pt"
TouchSensor977 = x3d.TouchSensor()
TouchSensor977.description = "HAnimSite l_ectocanthus_pt"

HAnimSite976.children.append(TouchSensor977)
Shape978 = x3d.Shape()
Shape978.USE = "HAnimSiteShape"

HAnimSite976.children.append(Shape978)

HAnimSegment965.children.append(HAnimSite976)
HAnimSite979 = x3d.HAnimSite()
HAnimSite979.DEF = "STD_Site_l_infraorbitale_pt"
HAnimSite979.name = "l_infraorbitale_pt"
HAnimSite979.translation = [0.0341,1.6171,0.0752]
TouchSensor980 = x3d.TouchSensor()
TouchSensor980.description = "HAnimSite l_infraorbitale_pt"

HAnimSite979.children.append(TouchSensor980)
Shape981 = x3d.Shape()
Shape981.USE = "HAnimSiteShape"

HAnimSite979.children.append(Shape981)

HAnimSegment965.children.append(HAnimSite979)
HAnimSite982 = x3d.HAnimSite()
HAnimSite982.DEF = "STD_Site_l_tragion_pt"
HAnimSite982.name = "l_tragion_pt"
HAnimSite982.translation = [0.0739,1.6348,0.0282]
TouchSensor983 = x3d.TouchSensor()
TouchSensor983.description = "HAnimSite l_tragion_pt"

HAnimSite982.children.append(TouchSensor983)
Shape984 = x3d.Shape()
Shape984.USE = "HAnimSiteShape"

HAnimSite982.children.append(Shape984)

HAnimSegment965.children.append(HAnimSite982)
HAnimSite985 = x3d.HAnimSite()
HAnimSite985.DEF = "STD_Site_nuchale_pt"
HAnimSite985.name = "nuchale_pt"
HAnimSite985.translation = [0.0039,1.5972,-0.0796]
TouchSensor986 = x3d.TouchSensor()
TouchSensor986.description = "HAnimSite nuchale_pt"

HAnimSite985.children.append(TouchSensor986)
Shape987 = x3d.Shape()
Shape987.USE = "HAnimSiteShape"

HAnimSite985.children.append(Shape987)

HAnimSegment965.children.append(HAnimSite985)
HAnimSite988 = x3d.HAnimSite()
HAnimSite988.DEF = "STD_Site_opisthocranion_pt"
HAnimSite988.name = "opisthocranion_pt"
TouchSensor989 = x3d.TouchSensor()
TouchSensor989.description = "HAnimSite opisthocranion_pt"

HAnimSite988.children.append(TouchSensor989)
Shape990 = x3d.Shape()
Shape990.USE = "HAnimSiteShape"

HAnimSite988.children.append(Shape990)

HAnimSegment965.children.append(HAnimSite988)
HAnimSite991 = x3d.HAnimSite()
HAnimSite991.DEF = "STD_Site_r_ectocanthus_pt"
HAnimSite991.name = "r_ectocanthus_pt"
TouchSensor992 = x3d.TouchSensor()
TouchSensor992.description = "HAnimSite r_ectocanthus_pt"

HAnimSite991.children.append(TouchSensor992)
Shape993 = x3d.Shape()
Shape993.USE = "HAnimSiteShape"

HAnimSite991.children.append(Shape993)

HAnimSegment965.children.append(HAnimSite991)
HAnimSite994 = x3d.HAnimSite()
HAnimSite994.DEF = "STD_Site_r_infraorbitale_pt"
HAnimSite994.name = "r_infraorbitale_pt"
HAnimSite994.translation = [-0.0237,1.6171,0.0752]
TouchSensor995 = x3d.TouchSensor()
TouchSensor995.description = "HAnimSite r_infraorbitale_pt"

HAnimSite994.children.append(TouchSensor995)
Shape996 = x3d.Shape()
Shape996.USE = "HAnimSiteShape"

HAnimSite994.children.append(Shape996)

HAnimSegment965.children.append(HAnimSite994)
HAnimSite997 = x3d.HAnimSite()
HAnimSite997.DEF = "STD_Site_r_tragion_pt"
HAnimSite997.name = "r_tragion_pt"
HAnimSite997.translation = [-0.0646,1.6347,0.0302]
TouchSensor998 = x3d.TouchSensor()
TouchSensor998.description = "HAnimSite r_tragion_pt"

HAnimSite997.children.append(TouchSensor998)
Shape999 = x3d.Shape()
Shape999.USE = "HAnimSiteShape"

HAnimSite997.children.append(Shape999)

HAnimSegment965.children.append(HAnimSite997)
HAnimSite1000 = x3d.HAnimSite()
HAnimSite1000.DEF = "STD_Site_sellion_pt"
HAnimSite1000.name = "sellion_pt"
HAnimSite1000.translation = [0.0058,1.6316,0.0852]
TouchSensor1001 = x3d.TouchSensor()
TouchSensor1001.description = "HAnimSite sellion_pt"

HAnimSite1000.children.append(TouchSensor1001)
Shape1002 = x3d.Shape()
Shape1002.USE = "HAnimSiteShape"

HAnimSite1000.children.append(Shape1002)

HAnimSegment965.children.append(HAnimSite1000)
HAnimSite1003 = x3d.HAnimSite()
HAnimSite1003.DEF = "STD_Site_skull_vertex_pt"
HAnimSite1003.name = "skull_vertex_pt"
HAnimSite1003.translation = [0.0050,1.7504,0.0055]
TouchSensor1004 = x3d.TouchSensor()
TouchSensor1004.description = "HAnimSite skull_vertex_pt"

HAnimSite1003.children.append(TouchSensor1004)
Shape1005 = x3d.Shape()
Shape1005.USE = "HAnimSiteShape"

HAnimSite1003.children.append(Shape1005)

HAnimSegment965.children.append(HAnimSite1003)

HAnimJoint964.children.append(HAnimSegment965)
HAnimJoint1006 = x3d.HAnimJoint()
HAnimJoint1006.DEF = "STD_Joint_l_eyelid_joint"
HAnimJoint1006.name = "l_eyelid_joint"
HAnimJoint1006.center = [0,1,0]
HAnimSegment1007 = x3d.HAnimSegment()
HAnimSegment1007.DEF = "STD_Segment_l_eyelid"
HAnimSegment1007.name = "l_eyelid"
Transform1008 = x3d.Transform()
Transform1008.translation = [0,1,0]
Shape1009 = x3d.Shape()
Shape1009.USE = "HAnimJointShape"

Transform1008.children.append(Shape1009)

HAnimSegment1007.children.append(Transform1008)
Transform1010 = x3d.Transform()
Shape1011 = x3d.Shape()
LineSet1012 = x3d.LineSet()
LineSet1012.vertexCount = [2]
Coordinate1013 = x3d.Coordinate()

LineSet1012.coord = Coordinate1013
ColorRGBA1014 = x3d.ColorRGBA()
ColorRGBA1014.USE = "HAnimSegmentLineColorRGBA"

LineSet1012.color = ColorRGBA1014

Shape1011.geometry = LineSet1012

Transform1010.children.append(Shape1011)

HAnimSegment1007.children.append(Transform1010)

HAnimJoint1006.children.append(HAnimSegment1007)
HAnimJoint1015 = x3d.HAnimJoint()
HAnimJoint1015.DEF = "STD_Joint_r_eyelid_joint"
HAnimJoint1015.name = "r_eyelid_joint"
HAnimJoint1015.center = [0,1,0]
HAnimSegment1016 = x3d.HAnimSegment()
HAnimSegment1016.DEF = "STD_Segment_r_eyelid"
HAnimSegment1016.name = "r_eyelid"
Transform1017 = x3d.Transform()
Transform1017.translation = [0,1,0]
Shape1018 = x3d.Shape()
Shape1018.USE = "HAnimJointShape"

Transform1017.children.append(Shape1018)

HAnimSegment1016.children.append(Transform1017)
Transform1019 = x3d.Transform()
Shape1020 = x3d.Shape()
LineSet1021 = x3d.LineSet()
LineSet1021.vertexCount = [2]
Coordinate1022 = x3d.Coordinate()

LineSet1021.coord = Coordinate1022
ColorRGBA1023 = x3d.ColorRGBA()
ColorRGBA1023.USE = "HAnimSegmentLineColorRGBA"

LineSet1021.color = ColorRGBA1023

Shape1020.geometry = LineSet1021

Transform1019.children.append(Shape1020)

HAnimSegment1016.children.append(Transform1019)

HAnimJoint1015.children.append(HAnimSegment1016)
HAnimJoint1024 = x3d.HAnimJoint()
HAnimJoint1024.DEF = "STD_Joint_l_eyeball_joint"
HAnimJoint1024.name = "l_eyeball_joint"
HAnimJoint1024.center = [0,1,0]
HAnimSegment1025 = x3d.HAnimSegment()
HAnimSegment1025.DEF = "STD_Segment_l_eyeball"
HAnimSegment1025.name = "l_eyeball"
Transform1026 = x3d.Transform()
Transform1026.translation = [0,1,0]
Shape1027 = x3d.Shape()
Shape1027.USE = "HAnimJointShape"

Transform1026.children.append(Shape1027)

HAnimSegment1025.children.append(Transform1026)
Transform1028 = x3d.Transform()
Shape1029 = x3d.Shape()
LineSet1030 = x3d.LineSet()
LineSet1030.vertexCount = [2]
Coordinate1031 = x3d.Coordinate()

LineSet1030.coord = Coordinate1031
ColorRGBA1032 = x3d.ColorRGBA()
ColorRGBA1032.USE = "HAnimSegmentLineColorRGBA"

LineSet1030.color = ColorRGBA1032

Shape1029.geometry = LineSet1030

Transform1028.children.append(Shape1029)

HAnimSegment1025.children.append(Transform1028)

HAnimJoint1024.children.append(HAnimSegment1025)
HAnimJoint1033 = x3d.HAnimJoint()
HAnimJoint1033.DEF = "STD_Joint_r_eyeball_joint"
HAnimJoint1033.name = "r_eyeball_joint"
HAnimJoint1033.center = [0,1,0]
HAnimSegment1034 = x3d.HAnimSegment()
HAnimSegment1034.DEF = "STD_Segment_r_eyeball"
HAnimSegment1034.name = "r_eyeball"
Transform1035 = x3d.Transform()
Transform1035.translation = [0,1,0]
Shape1036 = x3d.Shape()
Shape1036.USE = "HAnimJointShape"

Transform1035.children.append(Shape1036)

HAnimSegment1034.children.append(Transform1035)
Transform1037 = x3d.Transform()
Shape1038 = x3d.Shape()
LineSet1039 = x3d.LineSet()
LineSet1039.vertexCount = [2]
Coordinate1040 = x3d.Coordinate()

LineSet1039.coord = Coordinate1040
ColorRGBA1041 = x3d.ColorRGBA()
ColorRGBA1041.USE = "HAnimSegmentLineColorRGBA"

LineSet1039.color = ColorRGBA1041

Shape1038.geometry = LineSet1039

Transform1037.children.append(Shape1038)

HAnimSegment1034.children.append(Transform1037)

HAnimJoint1033.children.append(HAnimSegment1034)
HAnimJoint1042 = x3d.HAnimJoint()
HAnimJoint1042.DEF = "STD_Joint_l_eyebrow_joint"
HAnimJoint1042.name = "l_eyebrow_joint"
HAnimJoint1042.center = [0,1,0]
HAnimSegment1043 = x3d.HAnimSegment()
HAnimSegment1043.DEF = "STD_Segment_l_eyebrow"
HAnimSegment1043.name = "l_eyebrow"
Transform1044 = x3d.Transform()
Transform1044.translation = [0,1,0]
Shape1045 = x3d.Shape()
Shape1045.USE = "HAnimJointShape"

Transform1044.children.append(Shape1045)

HAnimSegment1043.children.append(Transform1044)
Transform1046 = x3d.Transform()
Shape1047 = x3d.Shape()
LineSet1048 = x3d.LineSet()
LineSet1048.vertexCount = [2]
Coordinate1049 = x3d.Coordinate()

LineSet1048.coord = Coordinate1049
ColorRGBA1050 = x3d.ColorRGBA()
ColorRGBA1050.USE = "HAnimSegmentLineColorRGBA"

LineSet1048.color = ColorRGBA1050

Shape1047.geometry = LineSet1048

Transform1046.children.append(Shape1047)

HAnimSegment1043.children.append(Transform1046)

HAnimJoint1042.children.append(HAnimSegment1043)
HAnimJoint1051 = x3d.HAnimJoint()
HAnimJoint1051.DEF = "STD_Joint_r_eyebrow_joint"
HAnimJoint1051.name = "r_eyebrow_joint"
HAnimJoint1051.center = [0,1,0]
HAnimSegment1052 = x3d.HAnimSegment()
HAnimSegment1052.DEF = "STD_Segment_r_eyebrow"
HAnimSegment1052.name = "r_eyebrow"
Transform1053 = x3d.Transform()
Transform1053.translation = [0,1,0]
Shape1054 = x3d.Shape()
Shape1054.USE = "HAnimJointShape"

Transform1053.children.append(Shape1054)

HAnimSegment1052.children.append(Transform1053)
Transform1055 = x3d.Transform()
Shape1056 = x3d.Shape()
LineSet1057 = x3d.LineSet()
LineSet1057.vertexCount = [2]
Coordinate1058 = x3d.Coordinate()

LineSet1057.coord = Coordinate1058
ColorRGBA1059 = x3d.ColorRGBA()
ColorRGBA1059.USE = "HAnimSegmentLineColorRGBA"

LineSet1057.color = ColorRGBA1059

Shape1056.geometry = LineSet1057

Transform1055.children.append(Shape1056)

HAnimSegment1052.children.append(Transform1055)

HAnimJoint1051.children.append(HAnimSegment1052)
HAnimJoint1060 = x3d.HAnimJoint()
HAnimJoint1060.DEF = "STD_Joint_temporomandibular"
HAnimJoint1060.name = "temporomandibular"
HAnimJoint1060.center = [0,1,0]
HAnimSegment1061 = x3d.HAnimSegment()
HAnimSegment1061.DEF = "STD_Segment_jaw"
HAnimSegment1061.name = "jaw"
Transform1062 = x3d.Transform()
Transform1062.translation = [0,1,0]
Shape1063 = x3d.Shape()
Shape1063.USE = "HAnimJointShape"

Transform1062.children.append(Shape1063)

HAnimSegment1061.children.append(Transform1062)
Transform1064 = x3d.Transform()
Shape1065 = x3d.Shape()
LineSet1066 = x3d.LineSet()
LineSet1066.vertexCount = [2]
Coordinate1067 = x3d.Coordinate()

LineSet1066.coord = Coordinate1067
ColorRGBA1068 = x3d.ColorRGBA()
ColorRGBA1068.USE = "HAnimSegmentLineColorRGBA"

LineSet1066.color = ColorRGBA1068

Shape1065.geometry = LineSet1066

Transform1064.children.append(Shape1065)

HAnimSegment1061.children.append(Transform1064)
HAnimSite1069 = x3d.HAnimSite()
HAnimSite1069.DEF = "STD_Site_l_gonion_pt"
HAnimSite1069.name = "l_gonion_pt"
HAnimSite1069.translation = [0.0631,1.5530,0.0330]
TouchSensor1070 = x3d.TouchSensor()
TouchSensor1070.description = "HAnimSite l_gonion_pt"

HAnimSite1069.children.append(TouchSensor1070)
Shape1071 = x3d.Shape()
Shape1071.USE = "HAnimSiteShape"

HAnimSite1069.children.append(Shape1071)

HAnimSegment1061.children.append(HAnimSite1069)
HAnimSite1072 = x3d.HAnimSite()
HAnimSite1072.DEF = "STD_Site_menton_pt"
HAnimSite1072.name = "menton_pt"
TouchSensor1073 = x3d.TouchSensor()
TouchSensor1073.description = "HAnimSite menton_pt"

HAnimSite1072.children.append(TouchSensor1073)
Shape1074 = x3d.Shape()
Shape1074.USE = "HAnimSiteShape"

HAnimSite1072.children.append(Shape1074)

HAnimSegment1061.children.append(HAnimSite1072)
HAnimSite1075 = x3d.HAnimSite()
HAnimSite1075.DEF = "STD_Site_r_gonion_pt"
HAnimSite1075.name = "r_gonion_pt"
HAnimSite1075.translation = [-0.0520,1.5529,0.0347]
TouchSensor1076 = x3d.TouchSensor()
TouchSensor1076.description = "HAnimSite r_gonion_pt"

HAnimSite1075.children.append(TouchSensor1076)
Shape1077 = x3d.Shape()
Shape1077.USE = "HAnimSiteShape"

HAnimSite1075.children.append(Shape1077)

HAnimSegment1061.children.append(HAnimSite1075)
HAnimSite1078 = x3d.HAnimSite()
HAnimSite1078.DEF = "STD_Site_supramenton_pt"
HAnimSite1078.name = "supramenton_pt"
HAnimSite1078.translation = [0.0061,1.5410,0.0805]
TouchSensor1079 = x3d.TouchSensor()
TouchSensor1079.description = "HAnimSite supramenton_pt"

HAnimSite1078.children.append(TouchSensor1079)
Shape1080 = x3d.Shape()
Shape1080.USE = "HAnimSiteShape"

HAnimSite1078.children.append(Shape1080)

HAnimSegment1061.children.append(HAnimSite1078)

HAnimJoint1060.children.append(HAnimSegment1061)

HAnimJoint1051.children.append(HAnimJoint1060)

HAnimJoint1042.children.append(HAnimJoint1051)

HAnimJoint1033.children.append(HAnimJoint1042)

HAnimJoint1024.children.append(HAnimJoint1033)

HAnimJoint1015.children.append(HAnimJoint1024)

HAnimJoint1006.children.append(HAnimJoint1015)

HAnimJoint964.children.append(HAnimJoint1006)

HAnimJoint955.children.append(HAnimJoint964)

HAnimJoint943.children.append(HAnimJoint955)

HAnimJoint934.children.append(HAnimJoint943)

HAnimJoint925.children.append(HAnimJoint934)

HAnimJoint916.children.append(HAnimJoint925)

HAnimJoint907.children.append(HAnimJoint916)

HAnimJoint892.children.append(HAnimJoint907)

HAnimJoint877.children.append(HAnimJoint892)
HAnimJoint1081 = x3d.HAnimJoint()
HAnimJoint1081.DEF = "STD_Joint_l_sternoclavicular"
HAnimJoint1081.name = "l_sternoclavicular"
HAnimJoint1081.center = [0.0820,1.4488,-0.0353]
HAnimSegment1082 = x3d.HAnimSegment()
HAnimSegment1082.DEF = "STD_Segment_l_clavicle"
HAnimSegment1082.name = "l_clavicle"
Transform1083 = x3d.Transform()
Transform1083.translation = [0.0820,1.4488,-0.0353]
Shape1084 = x3d.Shape()
Shape1084.USE = "HAnimJointShape"

Transform1083.children.append(Shape1084)

HAnimSegment1082.children.append(Transform1083)
Transform1085 = x3d.Transform()
Shape1086 = x3d.Shape()
LineSet1087 = x3d.LineSet()
LineSet1087.vertexCount = [2]
Coordinate1088 = x3d.Coordinate()

LineSet1087.coord = Coordinate1088
ColorRGBA1089 = x3d.ColorRGBA()
ColorRGBA1089.USE = "HAnimSegmentLineColorRGBA"

LineSet1087.color = ColorRGBA1089

Shape1086.geometry = LineSet1087

Transform1085.children.append(Shape1086)

HAnimSegment1082.children.append(Transform1085)
HAnimSite1090 = x3d.HAnimSite()
HAnimSite1090.DEF = "STD_Site_l_acromion_pt"
HAnimSite1090.name = "l_acromion_pt"
HAnimSite1090.translation = [0.2032,1.4760,-0.0490]
TouchSensor1091 = x3d.TouchSensor()
TouchSensor1091.description = "HAnimSite l_acromion_pt"

HAnimSite1090.children.append(TouchSensor1091)
Shape1092 = x3d.Shape()
Shape1092.USE = "HAnimSiteShape"

HAnimSite1090.children.append(Shape1092)

HAnimSegment1082.children.append(HAnimSite1090)
HAnimSite1093 = x3d.HAnimSite()
HAnimSite1093.DEF = "STD_Site_l_axilla_distal_pt"
HAnimSite1093.name = "l_axilla_distal_pt"
HAnimSite1093.translation = [0.1706,1.4072,-0.0875]
TouchSensor1094 = x3d.TouchSensor()
TouchSensor1094.description = "HAnimSite l_axilla_distal_pt"

HAnimSite1093.children.append(TouchSensor1094)
Shape1095 = x3d.Shape()
Shape1095.USE = "HAnimSiteShape"

HAnimSite1093.children.append(Shape1095)

HAnimSegment1082.children.append(HAnimSite1093)
HAnimSite1096 = x3d.HAnimSite()
HAnimSite1096.DEF = "STD_Site_l_axilla_posterior_folds_pt"
HAnimSite1096.name = "l_axilla_posterior_folds_pt"
TouchSensor1097 = x3d.TouchSensor()
TouchSensor1097.description = "HAnimSite l_axilla_posterior_folds_pt"

HAnimSite1096.children.append(TouchSensor1097)
Shape1098 = x3d.Shape()
Shape1098.USE = "HAnimSiteShape"

HAnimSite1096.children.append(Shape1098)

HAnimSegment1082.children.append(HAnimSite1096)
HAnimSite1099 = x3d.HAnimSite()
HAnimSite1099.DEF = "STD_Site_l_axilla_proximal_pt"
HAnimSite1099.name = "l_axilla_proximal_pt"
HAnimSite1099.translation = [0.1777,1.4065,-0.0075]
TouchSensor1100 = x3d.TouchSensor()
TouchSensor1100.description = "HAnimSite l_axilla_proximal_pt"

HAnimSite1099.children.append(TouchSensor1100)
Shape1101 = x3d.Shape()
Shape1101.USE = "HAnimSiteShape"

HAnimSite1099.children.append(Shape1101)

HAnimSegment1082.children.append(HAnimSite1099)
HAnimSite1102 = x3d.HAnimSite()
HAnimSite1102.DEF = "STD_Site_l_clavicale_pt"
HAnimSite1102.name = "l_clavicale_pt"
HAnimSite1102.translation = [0.0271,1.4943,0.0394]
TouchSensor1103 = x3d.TouchSensor()
TouchSensor1103.description = "HAnimSite l_clavicale_pt"

HAnimSite1102.children.append(TouchSensor1103)
Shape1104 = x3d.Shape()
Shape1104.USE = "HAnimSiteShape"

HAnimSite1102.children.append(Shape1104)

HAnimSegment1082.children.append(HAnimSite1102)

HAnimJoint1081.children.append(HAnimSegment1082)
HAnimJoint1105 = x3d.HAnimJoint()
HAnimJoint1105.DEF = "STD_Joint_l_acromioclavicular"
HAnimJoint1105.name = "l_acromioclavicular"
HAnimJoint1105.center = [0.0962,1.4269,-0.0424]
HAnimSegment1106 = x3d.HAnimSegment()
HAnimSegment1106.DEF = "STD_Segment_l_scapula"
HAnimSegment1106.name = "l_scapula"
Transform1107 = x3d.Transform()
Transform1107.translation = [0.0962,1.4269,-0.0424]
Shape1108 = x3d.Shape()
Shape1108.USE = "HAnimJointShape"

Transform1107.children.append(Shape1108)

HAnimSegment1106.children.append(Transform1107)
Transform1109 = x3d.Transform()
Shape1110 = x3d.Shape()
LineSet1111 = x3d.LineSet()
LineSet1111.vertexCount = [2]
Coordinate1112 = x3d.Coordinate()

LineSet1111.coord = Coordinate1112
ColorRGBA1113 = x3d.ColorRGBA()
ColorRGBA1113.USE = "HAnimSegmentLineColorRGBA"

LineSet1111.color = ColorRGBA1113

Shape1110.geometry = LineSet1111

Transform1109.children.append(Shape1110)

HAnimSegment1106.children.append(Transform1109)

HAnimJoint1105.children.append(HAnimSegment1106)
HAnimJoint1114 = x3d.HAnimJoint()
HAnimJoint1114.DEF = "STD_Joint_l_shoulder"
HAnimJoint1114.name = "l_shoulder"
HAnimJoint1114.center = [0.2029,1.4376,-0.0387]
HAnimSegment1115 = x3d.HAnimSegment()
HAnimSegment1115.DEF = "STD_Segment_l_upperarm"
HAnimSegment1115.name = "l_upperarm"
Transform1116 = x3d.Transform()
Transform1116.translation = [0.2029,1.4376,-0.0387]
Shape1117 = x3d.Shape()
Shape1117.USE = "HAnimJointShape"

Transform1116.children.append(Shape1117)

HAnimSegment1115.children.append(Transform1116)
Transform1118 = x3d.Transform()
Shape1119 = x3d.Shape()
LineSet1120 = x3d.LineSet()
LineSet1120.vertexCount = [2]
Coordinate1121 = x3d.Coordinate()

LineSet1120.coord = Coordinate1121
ColorRGBA1122 = x3d.ColorRGBA()
ColorRGBA1122.USE = "HAnimSegmentLineColorRGBA"

LineSet1120.color = ColorRGBA1122

Shape1119.geometry = LineSet1120

Transform1118.children.append(Shape1119)

HAnimSegment1115.children.append(Transform1118)
HAnimSite1123 = x3d.HAnimSite()
HAnimSite1123.DEF = "STD_Site_l_bideltoid_pt"
HAnimSite1123.name = "l_bideltoid_pt"
TouchSensor1124 = x3d.TouchSensor()
TouchSensor1124.description = "HAnimSite l_bideltoid_pt"

HAnimSite1123.children.append(TouchSensor1124)
Shape1125 = x3d.Shape()
Shape1125.USE = "HAnimSiteShape"

HAnimSite1123.children.append(Shape1125)

HAnimSegment1115.children.append(HAnimSite1123)
HAnimSite1126 = x3d.HAnimSite()
HAnimSite1126.DEF = "STD_Site_l_humeral_lateral_epicondyles_pt"
HAnimSite1126.name = "l_humeral_lateral_epicondyles_pt"
HAnimSite1126.translation = [0.2280,1.1482,-0.1100]
TouchSensor1127 = x3d.TouchSensor()
TouchSensor1127.description = "HAnimSite l_humeral_lateral_epicondyles_pt"

HAnimSite1126.children.append(TouchSensor1127)
Shape1128 = x3d.Shape()
Shape1128.USE = "HAnimSiteShape"

HAnimSite1126.children.append(Shape1128)

HAnimSegment1115.children.append(HAnimSite1126)

HAnimJoint1114.children.append(HAnimSegment1115)
HAnimJoint1129 = x3d.HAnimJoint()
HAnimJoint1129.DEF = "STD_Joint_l_elbow"
HAnimJoint1129.name = "l_elbow"
HAnimJoint1129.center = [0.2014,1.1357,-0.0682]
HAnimSegment1130 = x3d.HAnimSegment()
HAnimSegment1130.DEF = "STD_Segment_l_forearm"
HAnimSegment1130.name = "l_forearm"
Transform1131 = x3d.Transform()
Transform1131.translation = [0.2014,1.1357,-0.0682]
Shape1132 = x3d.Shape()
Shape1132.USE = "HAnimJointShape"

Transform1131.children.append(Shape1132)

HAnimSegment1130.children.append(Transform1131)
Transform1133 = x3d.Transform()
Shape1134 = x3d.Shape()
LineSet1135 = x3d.LineSet()
LineSet1135.vertexCount = [2]
Coordinate1136 = x3d.Coordinate()

LineSet1135.coord = Coordinate1136
ColorRGBA1137 = x3d.ColorRGBA()
ColorRGBA1137.USE = "HAnimSegmentLineColorRGBA"

LineSet1135.color = ColorRGBA1137

Shape1134.geometry = LineSet1135

Transform1133.children.append(Shape1134)

HAnimSegment1130.children.append(Transform1133)
HAnimSite1138 = x3d.HAnimSite()
HAnimSite1138.DEF = "STD_Site_l_humeral_medial_epicondyles_pt"
HAnimSite1138.name = "l_humeral_medial_epicondyles_pt"
HAnimSite1138.translation = [0.1735,1.1272,-0.1113]
TouchSensor1139 = x3d.TouchSensor()
TouchSensor1139.description = "HAnimSite l_humeral_medial_epicondyles_pt"

HAnimSite1138.children.append(TouchSensor1139)
Shape1140 = x3d.Shape()
Shape1140.USE = "HAnimSiteShape"

HAnimSite1138.children.append(Shape1140)

HAnimSegment1130.children.append(HAnimSite1138)
HAnimSite1141 = x3d.HAnimSite()
HAnimSite1141.DEF = "STD_Site_l_olecranon_pt"
HAnimSite1141.name = "l_olecranon_pt"
HAnimSite1141.translation = [-0.1962,1.1375,-0.1123]
TouchSensor1142 = x3d.TouchSensor()
TouchSensor1142.description = "HAnimSite l_olecranon_pt"

HAnimSite1141.children.append(TouchSensor1142)
Shape1143 = x3d.Shape()
Shape1143.USE = "HAnimSiteShape"

HAnimSite1141.children.append(Shape1143)

HAnimSegment1130.children.append(HAnimSite1141)
HAnimSite1144 = x3d.HAnimSite()
HAnimSite1144.DEF = "STD_Site_l_radial_styloid_pt"
HAnimSite1144.name = "l_radial_styloid_pt"
HAnimSite1144.translation = [0.1901,0.8645,-0.0415]
TouchSensor1145 = x3d.TouchSensor()
TouchSensor1145.description = "HAnimSite l_radial_styloid_pt"

HAnimSite1144.children.append(TouchSensor1145)
Shape1146 = x3d.Shape()
Shape1146.USE = "HAnimSiteShape"

HAnimSite1144.children.append(Shape1146)

HAnimSegment1130.children.append(HAnimSite1144)
HAnimSite1147 = x3d.HAnimSite()
HAnimSite1147.DEF = "STD_Site_l_radiale_pt"
HAnimSite1147.name = "l_radiale_pt"
HAnimSite1147.translation = [0.2182,1.1212,-0.1167]
TouchSensor1148 = x3d.TouchSensor()
TouchSensor1148.description = "HAnimSite l_radiale_pt"

HAnimSite1147.children.append(TouchSensor1148)
Shape1149 = x3d.Shape()
Shape1149.USE = "HAnimSiteShape"

HAnimSite1147.children.append(Shape1149)

HAnimSegment1130.children.append(HAnimSite1147)

HAnimJoint1129.children.append(HAnimSegment1130)
HAnimJoint1150 = x3d.HAnimJoint()
HAnimJoint1150.DEF = "STD_Joint_l_radiocarpal"
HAnimJoint1150.name = "l_radiocarpal"
HAnimJoint1150.center = [0.1984,0.8663,-0.0583]
HAnimSegment1151 = x3d.HAnimSegment()
HAnimSegment1151.DEF = "STD_Segment_l_carpal"
HAnimSegment1151.name = "l_carpal"
Transform1152 = x3d.Transform()
Transform1152.translation = [0.1984,0.8663,-0.0583]
Shape1153 = x3d.Shape()
Shape1153.USE = "HAnimJointShape"

Transform1152.children.append(Shape1153)

HAnimSegment1151.children.append(Transform1152)
Transform1154 = x3d.Transform()
Shape1155 = x3d.Shape()
LineSet1156 = x3d.LineSet()
LineSet1156.vertexCount = [2]
Coordinate1157 = x3d.Coordinate()

LineSet1156.coord = Coordinate1157
ColorRGBA1158 = x3d.ColorRGBA()
ColorRGBA1158.USE = "HAnimSegmentLineColorRGBA"

LineSet1156.color = ColorRGBA1158

Shape1155.geometry = LineSet1156

Transform1154.children.append(Shape1155)

HAnimSegment1151.children.append(Transform1154)
HAnimSite1159 = x3d.HAnimSite()
HAnimSite1159.DEF = "STD_Site_l_ulnar_styloid_pt"
HAnimSite1159.name = "l_ulnar_styloid_pt"
HAnimSite1159.translation = [-0.2142,0.8529,-0.0648]
TouchSensor1160 = x3d.TouchSensor()
TouchSensor1160.description = "HAnimSite l_ulnar_styloid_pt"

HAnimSite1159.children.append(TouchSensor1160)
Shape1161 = x3d.Shape()
Shape1161.USE = "HAnimSiteShape"

HAnimSite1159.children.append(Shape1161)

HAnimSegment1151.children.append(HAnimSite1159)

HAnimJoint1150.children.append(HAnimSegment1151)
HAnimJoint1162 = x3d.HAnimJoint()
HAnimJoint1162.DEF = "STD_Joint_l_midcarpal_1"
HAnimJoint1162.name = "l_midcarpal_1"
HAnimJoint1162.center = [0,1,0]
HAnimSegment1163 = x3d.HAnimSegment()
HAnimSegment1163.DEF = "STD_Segment_l_trapezium"
HAnimSegment1163.name = "l_trapezium"
Transform1164 = x3d.Transform()
Transform1164.translation = [0,1,0]
Shape1165 = x3d.Shape()
Shape1165.USE = "HAnimJointShape"

Transform1164.children.append(Shape1165)

HAnimSegment1163.children.append(Transform1164)
Transform1166 = x3d.Transform()
Shape1167 = x3d.Shape()
LineSet1168 = x3d.LineSet()
LineSet1168.vertexCount = [2]
Coordinate1169 = x3d.Coordinate()

LineSet1168.coord = Coordinate1169
ColorRGBA1170 = x3d.ColorRGBA()
ColorRGBA1170.USE = "HAnimSegmentLineColorRGBA"

LineSet1168.color = ColorRGBA1170

Shape1167.geometry = LineSet1168

Transform1166.children.append(Shape1167)

HAnimSegment1163.children.append(Transform1166)

HAnimJoint1162.children.append(HAnimSegment1163)
HAnimJoint1171 = x3d.HAnimJoint()
HAnimJoint1171.DEF = "STD_Joint_l_carpometacarpal_1"
HAnimJoint1171.name = "l_carpometacarpal_1"
HAnimJoint1171.center = [0.1924,0.8472,-0.0534]
HAnimSegment1172 = x3d.HAnimSegment()
HAnimSegment1172.DEF = "STD_Segment_l_metacarpal_1"
HAnimSegment1172.name = "l_metacarpal_1"
Transform1173 = x3d.Transform()
Transform1173.translation = [0.1924,0.8472,-0.0534]
Shape1174 = x3d.Shape()
Shape1174.USE = "HAnimJointShape"

Transform1173.children.append(Shape1174)

HAnimSegment1172.children.append(Transform1173)
Transform1175 = x3d.Transform()
Shape1176 = x3d.Shape()
LineSet1177 = x3d.LineSet()
LineSet1177.vertexCount = [2]
Coordinate1178 = x3d.Coordinate()

LineSet1177.coord = Coordinate1178
ColorRGBA1179 = x3d.ColorRGBA()
ColorRGBA1179.USE = "HAnimSegmentLineColorRGBA"

LineSet1177.color = ColorRGBA1179

Shape1176.geometry = LineSet1177

Transform1175.children.append(Shape1176)

HAnimSegment1172.children.append(Transform1175)

HAnimJoint1171.children.append(HAnimSegment1172)
HAnimJoint1180 = x3d.HAnimJoint()
HAnimJoint1180.DEF = "STD_Joint_l_metacarpophalangeal_1"
HAnimJoint1180.name = "l_metacarpophalangeal_1"
HAnimJoint1180.center = [0.1951,0.8226,0.0246]
HAnimSegment1181 = x3d.HAnimSegment()
HAnimSegment1181.DEF = "STD_Segment_l_carpal_proximal_phalanx_1"
HAnimSegment1181.name = "l_carpal_proximal_phalanx_1"
Transform1182 = x3d.Transform()
Transform1182.translation = [0.1951,0.8226,0.0246]
Shape1183 = x3d.Shape()
Shape1183.USE = "HAnimJointShape"

Transform1182.children.append(Shape1183)

HAnimSegment1181.children.append(Transform1182)
Transform1184 = x3d.Transform()
Shape1185 = x3d.Shape()
LineSet1186 = x3d.LineSet()
LineSet1186.vertexCount = [2]
Coordinate1187 = x3d.Coordinate()

LineSet1186.coord = Coordinate1187
ColorRGBA1188 = x3d.ColorRGBA()
ColorRGBA1188.USE = "HAnimSegmentLineColorRGBA"

LineSet1186.color = ColorRGBA1188

Shape1185.geometry = LineSet1186

Transform1184.children.append(Shape1185)

HAnimSegment1181.children.append(Transform1184)

HAnimJoint1180.children.append(HAnimSegment1181)
HAnimJoint1189 = x3d.HAnimJoint()
HAnimJoint1189.DEF = "STD_Joint_l_carpal_interphalangeal_1"
HAnimJoint1189.name = "l_carpal_interphalangeal_1"
HAnimJoint1189.center = [0.1955,0.8159,0.0464]
HAnimSegment1190 = x3d.HAnimSegment()
HAnimSegment1190.DEF = "STD_Segment_l_carpal_distal_phalanx_1"
HAnimSegment1190.name = "l_carpal_distal_phalanx_1"
Transform1191 = x3d.Transform()
Transform1191.translation = [0.1955,0.8159,0.0464]
Shape1192 = x3d.Shape()
Shape1192.USE = "HAnimJointShape"

Transform1191.children.append(Shape1192)

HAnimSegment1190.children.append(Transform1191)
Transform1193 = x3d.Transform()
Shape1194 = x3d.Shape()
LineSet1195 = x3d.LineSet()
LineSet1195.vertexCount = [2]
Coordinate1196 = x3d.Coordinate()

LineSet1195.coord = Coordinate1196
ColorRGBA1197 = x3d.ColorRGBA()
ColorRGBA1197.USE = "HAnimSegmentLineColorRGBA"

LineSet1195.color = ColorRGBA1197

Shape1194.geometry = LineSet1195

Transform1193.children.append(Shape1194)

HAnimSegment1190.children.append(Transform1193)
HAnimSite1198 = x3d.HAnimSite()
HAnimSite1198.DEF = "STD_Site_l_carpal_distal_phalanx_1_tip"
HAnimSite1198.name = "l_carpal_distal_phalanx_1_tip"
TouchSensor1199 = x3d.TouchSensor()
TouchSensor1199.description = "HAnimSite l_carpal_distal_phalanx_1_tip"

HAnimSite1198.children.append(TouchSensor1199)
Shape1200 = x3d.Shape()
Shape1200.USE = "HAnimSiteShape"

HAnimSite1198.children.append(Shape1200)

HAnimSegment1190.children.append(HAnimSite1198)

HAnimJoint1189.children.append(HAnimSegment1190)

HAnimJoint1180.children.append(HAnimJoint1189)

HAnimJoint1171.children.append(HAnimJoint1180)

HAnimJoint1162.children.append(HAnimJoint1171)

HAnimJoint1150.children.append(HAnimJoint1162)
HAnimJoint1201 = x3d.HAnimJoint()
HAnimJoint1201.DEF = "STD_Joint_l_midcarpal_2"
HAnimJoint1201.name = "l_midcarpal_2"
HAnimJoint1201.center = [0,1,0]
HAnimSegment1202 = x3d.HAnimSegment()
HAnimSegment1202.DEF = "STD_Segment_l_trapezoid"
HAnimSegment1202.name = "l_trapezoid"
Transform1203 = x3d.Transform()
Transform1203.translation = [0,1,0]
Shape1204 = x3d.Shape()
Shape1204.USE = "HAnimJointShape"

Transform1203.children.append(Shape1204)

HAnimSegment1202.children.append(Transform1203)
Transform1205 = x3d.Transform()
Shape1206 = x3d.Shape()
LineSet1207 = x3d.LineSet()
LineSet1207.vertexCount = [2]
Coordinate1208 = x3d.Coordinate()

LineSet1207.coord = Coordinate1208
ColorRGBA1209 = x3d.ColorRGBA()
ColorRGBA1209.USE = "HAnimSegmentLineColorRGBA"

LineSet1207.color = ColorRGBA1209

Shape1206.geometry = LineSet1207

Transform1205.children.append(Shape1206)

HAnimSegment1202.children.append(Transform1205)

HAnimJoint1201.children.append(HAnimSegment1202)
HAnimJoint1210 = x3d.HAnimJoint()
HAnimJoint1210.DEF = "STD_Joint_l_carpometacarpal_2"
HAnimJoint1210.name = "l_carpometacarpal_2"
HAnimJoint1210.center = [0.1983,0.8024,-0.0280]
HAnimSegment1211 = x3d.HAnimSegment()
HAnimSegment1211.DEF = "STD_Segment_l_metacarpal_2"
HAnimSegment1211.name = "l_metacarpal_2"
Transform1212 = x3d.Transform()
Transform1212.translation = [0.1983,0.8024,-0.0280]
Shape1213 = x3d.Shape()
Shape1213.USE = "HAnimJointShape"

Transform1212.children.append(Shape1213)

HAnimSegment1211.children.append(Transform1212)
Transform1214 = x3d.Transform()
Shape1215 = x3d.Shape()
LineSet1216 = x3d.LineSet()
LineSet1216.vertexCount = [2]
Coordinate1217 = x3d.Coordinate()

LineSet1216.coord = Coordinate1217
ColorRGBA1218 = x3d.ColorRGBA()
ColorRGBA1218.USE = "HAnimSegmentLineColorRGBA"

LineSet1216.color = ColorRGBA1218

Shape1215.geometry = LineSet1216

Transform1214.children.append(Shape1215)

HAnimSegment1211.children.append(Transform1214)
HAnimSite1219 = x3d.HAnimSite()
HAnimSite1219.DEF = "STD_Site_l_metacarpal_phalanx_2_pt"
HAnimSite1219.name = "l_metacarpal_phalanx_2_pt"
HAnimSite1219.translation = [0.2009,0.8139,-0.0237]
TouchSensor1220 = x3d.TouchSensor()
TouchSensor1220.description = "HAnimSite l_metacarpal_phalanx_2_pt"

HAnimSite1219.children.append(TouchSensor1220)
Shape1221 = x3d.Shape()
Shape1221.USE = "HAnimSiteShape"

HAnimSite1219.children.append(Shape1221)

HAnimSegment1211.children.append(HAnimSite1219)

HAnimJoint1210.children.append(HAnimSegment1211)
HAnimJoint1222 = x3d.HAnimJoint()
HAnimJoint1222.DEF = "STD_Joint_l_metacarpophalangeal_2"
HAnimJoint1222.name = "l_metacarpophalangeal_2"
HAnimJoint1222.center = [0.1983,0.7815,-0.0280]
HAnimSegment1223 = x3d.HAnimSegment()
HAnimSegment1223.DEF = "STD_Segment_l_carpal_proximal_phalanx_2 "
HAnimSegment1223.name = "l_carpal_proximal_phalanx_2 "
Transform1224 = x3d.Transform()
Transform1224.translation = [0.1983,0.7815,-0.0280]
Shape1225 = x3d.Shape()
Shape1225.USE = "HAnimJointShape"

Transform1224.children.append(Shape1225)

HAnimSegment1223.children.append(Transform1224)
Transform1226 = x3d.Transform()
Shape1227 = x3d.Shape()
LineSet1228 = x3d.LineSet()
LineSet1228.vertexCount = [2]
Coordinate1229 = x3d.Coordinate()

LineSet1228.coord = Coordinate1229
ColorRGBA1230 = x3d.ColorRGBA()
ColorRGBA1230.USE = "HAnimSegmentLineColorRGBA"

LineSet1228.color = ColorRGBA1230

Shape1227.geometry = LineSet1228

Transform1226.children.append(Shape1227)

HAnimSegment1223.children.append(Transform1226)

HAnimJoint1222.children.append(HAnimSegment1223)
HAnimJoint1231 = x3d.HAnimJoint()
HAnimJoint1231.DEF = "STD_Joint_l_carpal_proximal_interphalangeal_2"
HAnimJoint1231.name = "l_carpal_proximal_interphalangeal_2"
HAnimJoint1231.center = [0.2017,0.7363,-0.0248]
HAnimSegment1232 = x3d.HAnimSegment()
HAnimSegment1232.DEF = "STD_Segment_l_carpal_middle_phalanx_2"
HAnimSegment1232.name = "l_carpal_middle_phalanx_2"
Transform1233 = x3d.Transform()
Transform1233.translation = [0.2017,0.7363,-0.0248]
Shape1234 = x3d.Shape()
Shape1234.USE = "HAnimJointShape"

Transform1233.children.append(Shape1234)

HAnimSegment1232.children.append(Transform1233)
Transform1235 = x3d.Transform()
Shape1236 = x3d.Shape()
LineSet1237 = x3d.LineSet()
LineSet1237.vertexCount = [2]
Coordinate1238 = x3d.Coordinate()

LineSet1237.coord = Coordinate1238
ColorRGBA1239 = x3d.ColorRGBA()
ColorRGBA1239.USE = "HAnimSegmentLineColorRGBA"

LineSet1237.color = ColorRGBA1239

Shape1236.geometry = LineSet1237

Transform1235.children.append(Shape1236)

HAnimSegment1232.children.append(Transform1235)

HAnimJoint1231.children.append(HAnimSegment1232)
HAnimJoint1240 = x3d.HAnimJoint()
HAnimJoint1240.DEF = "STD_Joint_l_carpal_distal_interphalangeal_2"
HAnimJoint1240.name = "l_carpal_distal_interphalangeal_2"
HAnimJoint1240.center = [0.2028,0.7139,-0.0236]
HAnimSegment1241 = x3d.HAnimSegment()
HAnimSegment1241.DEF = "STD_Segment_l_carpal_distal_phalanx_2"
HAnimSegment1241.name = "l_carpal_distal_phalanx_2"
Transform1242 = x3d.Transform()
Transform1242.translation = [0.2028,0.7139,-0.0236]
Shape1243 = x3d.Shape()
Shape1243.USE = "HAnimJointShape"

Transform1242.children.append(Shape1243)

HAnimSegment1241.children.append(Transform1242)
Transform1244 = x3d.Transform()
Shape1245 = x3d.Shape()
LineSet1246 = x3d.LineSet()
LineSet1246.vertexCount = [2]
Coordinate1247 = x3d.Coordinate()

LineSet1246.coord = Coordinate1247
ColorRGBA1248 = x3d.ColorRGBA()
ColorRGBA1248.USE = "HAnimSegmentLineColorRGBA"

LineSet1246.color = ColorRGBA1248

Shape1245.geometry = LineSet1246

Transform1244.children.append(Shape1245)

HAnimSegment1241.children.append(Transform1244)
HAnimSite1249 = x3d.HAnimSite()
HAnimSite1249.DEF = "STD_Site_l_carpal_distal_phalanx_2_tip"
HAnimSite1249.name = "l_carpal_distal_phalanx_2_tip"
TouchSensor1250 = x3d.TouchSensor()
TouchSensor1250.description = "HAnimSite l_carpal_distal_phalanx_2_tip"

HAnimSite1249.children.append(TouchSensor1250)
Shape1251 = x3d.Shape()
Shape1251.USE = "HAnimSiteShape"

HAnimSite1249.children.append(Shape1251)

HAnimSegment1241.children.append(HAnimSite1249)
HAnimSite1252 = x3d.HAnimSite()
HAnimSite1252.DEF = "STD_Site_l_dactylion_pt"
HAnimSite1252.name = "l_dactylion_pt"
HAnimSite1252.translation = [0.2056,0.6743,-0.0482]
TouchSensor1253 = x3d.TouchSensor()
TouchSensor1253.description = "HAnimSite l_dactylion_pt"

HAnimSite1252.children.append(TouchSensor1253)
Shape1254 = x3d.Shape()
Shape1254.USE = "HAnimSiteShape"

HAnimSite1252.children.append(Shape1254)

HAnimSegment1241.children.append(HAnimSite1252)

HAnimJoint1240.children.append(HAnimSegment1241)

HAnimJoint1231.children.append(HAnimJoint1240)

HAnimJoint1222.children.append(HAnimJoint1231)

HAnimJoint1210.children.append(HAnimJoint1222)

HAnimJoint1201.children.append(HAnimJoint1210)

HAnimJoint1150.children.append(HAnimJoint1201)
HAnimJoint1255 = x3d.HAnimJoint()
HAnimJoint1255.DEF = "STD_Joint_l_midcarpal_3"
HAnimJoint1255.name = "l_midcarpal_3"
HAnimJoint1255.center = [0,1,0]
HAnimSegment1256 = x3d.HAnimSegment()
HAnimSegment1256.DEF = "STD_Segment_l_capitate"
HAnimSegment1256.name = "l_capitate"
Transform1257 = x3d.Transform()
Transform1257.translation = [0,1,0]
Shape1258 = x3d.Shape()
Shape1258.USE = "HAnimJointShape"

Transform1257.children.append(Shape1258)

HAnimSegment1256.children.append(Transform1257)
Transform1259 = x3d.Transform()
Shape1260 = x3d.Shape()
LineSet1261 = x3d.LineSet()
LineSet1261.vertexCount = [2]
Coordinate1262 = x3d.Coordinate()

LineSet1261.coord = Coordinate1262
ColorRGBA1263 = x3d.ColorRGBA()
ColorRGBA1263.USE = "HAnimSegmentLineColorRGBA"

LineSet1261.color = ColorRGBA1263

Shape1260.geometry = LineSet1261

Transform1259.children.append(Shape1260)

HAnimSegment1256.children.append(Transform1259)

HAnimJoint1255.children.append(HAnimSegment1256)
HAnimJoint1264 = x3d.HAnimJoint()
HAnimJoint1264.DEF = "STD_Joint_l_carpometacarpal_3"
HAnimJoint1264.name = "l_carpometacarpal_3"
HAnimJoint1264.center = [0.1987,0.8029,-0.0530]
HAnimSegment1265 = x3d.HAnimSegment()
HAnimSegment1265.DEF = "STD_Segment_l_metacarpal_3"
HAnimSegment1265.name = "l_metacarpal_3"
Transform1266 = x3d.Transform()
Transform1266.translation = [0.1987,0.8029,-0.0530]
Shape1267 = x3d.Shape()
Shape1267.USE = "HAnimJointShape"

Transform1266.children.append(Shape1267)

HAnimSegment1265.children.append(Transform1266)
Transform1268 = x3d.Transform()
Shape1269 = x3d.Shape()
LineSet1270 = x3d.LineSet()
LineSet1270.vertexCount = [2]
Coordinate1271 = x3d.Coordinate()

LineSet1270.coord = Coordinate1271
ColorRGBA1272 = x3d.ColorRGBA()
ColorRGBA1272.USE = "HAnimSegmentLineColorRGBA"

LineSet1270.color = ColorRGBA1272

Shape1269.geometry = LineSet1270

Transform1268.children.append(Shape1269)

HAnimSegment1265.children.append(Transform1268)
HAnimSite1273 = x3d.HAnimSite()
HAnimSite1273.DEF = "STD_Site_l_metacarpal_phalanx_3_pt"
HAnimSite1273.name = "l_metacarpal_phalanx_3_pt"
TouchSensor1274 = x3d.TouchSensor()
TouchSensor1274.description = "HAnimSite l_metacarpal_phalanx_3_pt"

HAnimSite1273.children.append(TouchSensor1274)
Shape1275 = x3d.Shape()
Shape1275.USE = "HAnimSiteShape"

HAnimSite1273.children.append(Shape1275)

HAnimSegment1265.children.append(HAnimSite1273)

HAnimJoint1264.children.append(HAnimSegment1265)
HAnimJoint1276 = x3d.HAnimJoint()
HAnimJoint1276.DEF = "STD_Joint_l_metacarpophalangeal_3"
HAnimJoint1276.name = "l_metacarpophalangeal_3"
HAnimJoint1276.center = [0.1987,0.7818,-0.0530]
HAnimSegment1277 = x3d.HAnimSegment()
HAnimSegment1277.DEF = "STD_Segment_l_carpal_proximal_phalanx_3"
HAnimSegment1277.name = "l_carpal_proximal_phalanx_3"
Transform1278 = x3d.Transform()
Transform1278.translation = [0.1987,0.7818,-0.0530]
Shape1279 = x3d.Shape()
Shape1279.USE = "HAnimJointShape"

Transform1278.children.append(Shape1279)

HAnimSegment1277.children.append(Transform1278)
Transform1280 = x3d.Transform()
Shape1281 = x3d.Shape()
LineSet1282 = x3d.LineSet()
LineSet1282.vertexCount = [2]
Coordinate1283 = x3d.Coordinate()

LineSet1282.coord = Coordinate1283
ColorRGBA1284 = x3d.ColorRGBA()
ColorRGBA1284.USE = "HAnimSegmentLineColorRGBA"

LineSet1282.color = ColorRGBA1284

Shape1281.geometry = LineSet1282

Transform1280.children.append(Shape1281)

HAnimSegment1277.children.append(Transform1280)

HAnimJoint1276.children.append(HAnimSegment1277)
HAnimJoint1285 = x3d.HAnimJoint()
HAnimJoint1285.DEF = "STD_Joint_l_carpal_proximal_interphalangeal_3"
HAnimJoint1285.name = "l_carpal_proximal_interphalangeal_3"
HAnimJoint1285.center = [0.2013,0.7273,-0.0503]
HAnimSegment1286 = x3d.HAnimSegment()
HAnimSegment1286.DEF = "STD_Segment_l_carpal_middle_phalanx_3"
HAnimSegment1286.name = "l_carpal_middle_phalanx_3"
Transform1287 = x3d.Transform()
Transform1287.translation = [0.2013,0.7273,-0.0503]
Shape1288 = x3d.Shape()
Shape1288.USE = "HAnimJointShape"

Transform1287.children.append(Shape1288)

HAnimSegment1286.children.append(Transform1287)
Transform1289 = x3d.Transform()
Shape1290 = x3d.Shape()
LineSet1291 = x3d.LineSet()
LineSet1291.vertexCount = [2]
Coordinate1292 = x3d.Coordinate()

LineSet1291.coord = Coordinate1292
ColorRGBA1293 = x3d.ColorRGBA()
ColorRGBA1293.USE = "HAnimSegmentLineColorRGBA"

LineSet1291.color = ColorRGBA1293

Shape1290.geometry = LineSet1291

Transform1289.children.append(Shape1290)

HAnimSegment1286.children.append(Transform1289)

HAnimJoint1285.children.append(HAnimSegment1286)
HAnimJoint1294 = x3d.HAnimJoint()
HAnimJoint1294.DEF = "STD_Joint_l_carpal_distal_interphalangeal_3"
HAnimJoint1294.name = "l_carpal_distal_interphalangeal_3"
HAnimJoint1294.center = [0.2026,0.7011,-0.0494]
HAnimSegment1295 = x3d.HAnimSegment()
HAnimSegment1295.DEF = "STD_Segment_l_carpal_distal_phalanx_3"
HAnimSegment1295.name = "l_carpal_distal_phalanx_3"
Transform1296 = x3d.Transform()
Transform1296.translation = [0.2026,0.7011,-0.0494]
Shape1297 = x3d.Shape()
Shape1297.USE = "HAnimJointShape"

Transform1296.children.append(Shape1297)

HAnimSegment1295.children.append(Transform1296)
Transform1298 = x3d.Transform()
Shape1299 = x3d.Shape()
LineSet1300 = x3d.LineSet()
LineSet1300.vertexCount = [2]
Coordinate1301 = x3d.Coordinate()

LineSet1300.coord = Coordinate1301
ColorRGBA1302 = x3d.ColorRGBA()
ColorRGBA1302.USE = "HAnimSegmentLineColorRGBA"

LineSet1300.color = ColorRGBA1302

Shape1299.geometry = LineSet1300

Transform1298.children.append(Shape1299)

HAnimSegment1295.children.append(Transform1298)
HAnimSite1303 = x3d.HAnimSite()
HAnimSite1303.DEF = "STD_Site_l_carpal_distal_phalanx_3_tip"
HAnimSite1303.name = "l_carpal_distal_phalanx_3_tip"
TouchSensor1304 = x3d.TouchSensor()
TouchSensor1304.description = "HAnimSite l_carpal_distal_phalanx_3_tip"

HAnimSite1303.children.append(TouchSensor1304)
Shape1305 = x3d.Shape()
Shape1305.USE = "HAnimSiteShape"

HAnimSite1303.children.append(Shape1305)

HAnimSegment1295.children.append(HAnimSite1303)

HAnimJoint1294.children.append(HAnimSegment1295)

HAnimJoint1285.children.append(HAnimJoint1294)

HAnimJoint1276.children.append(HAnimJoint1285)

HAnimJoint1264.children.append(HAnimJoint1276)

HAnimJoint1255.children.append(HAnimJoint1264)

HAnimJoint1150.children.append(HAnimJoint1255)
HAnimJoint1306 = x3d.HAnimJoint()
HAnimJoint1306.DEF = "STD_Joint_l_midcarpal_4_5"
HAnimJoint1306.name = "l_midcarpal_4_5"
HAnimJoint1306.center = [0,1,0]
HAnimSegment1307 = x3d.HAnimSegment()
HAnimSegment1307.DEF = "STD_Segment_l_hamate"
HAnimSegment1307.name = "l_hamate"
Transform1308 = x3d.Transform()
Transform1308.translation = [0,1,0]
Shape1309 = x3d.Shape()
Shape1309.USE = "HAnimJointShape"

Transform1308.children.append(Shape1309)

HAnimSegment1307.children.append(Transform1308)
Transform1310 = x3d.Transform()
Shape1311 = x3d.Shape()
LineSet1312 = x3d.LineSet()
LineSet1312.vertexCount = [2]
Coordinate1313 = x3d.Coordinate()

LineSet1312.coord = Coordinate1313
ColorRGBA1314 = x3d.ColorRGBA()
ColorRGBA1314.USE = "HAnimSegmentLineColorRGBA"

LineSet1312.color = ColorRGBA1314

Shape1311.geometry = LineSet1312

Transform1310.children.append(Shape1311)

HAnimSegment1307.children.append(Transform1310)

HAnimJoint1306.children.append(HAnimSegment1307)
HAnimJoint1315 = x3d.HAnimJoint()
HAnimJoint1315.DEF = "STD_Joint_l_carpometacarpal_4"
HAnimJoint1315.name = "l_carpometacarpal_4"
HAnimJoint1315.center = [0.1956,0.8019,-0.0794]
HAnimSegment1316 = x3d.HAnimSegment()
HAnimSegment1316.DEF = "STD_Segment_l_metacarpal_4"
HAnimSegment1316.name = "l_metacarpal_4"
Transform1317 = x3d.Transform()
Transform1317.translation = [0.1956,0.8019,-0.0794]
Shape1318 = x3d.Shape()
Shape1318.USE = "HAnimJointShape"

Transform1317.children.append(Shape1318)

HAnimSegment1316.children.append(Transform1317)
Transform1319 = x3d.Transform()
Shape1320 = x3d.Shape()
LineSet1321 = x3d.LineSet()
LineSet1321.vertexCount = [2]
Coordinate1322 = x3d.Coordinate()

LineSet1321.coord = Coordinate1322
ColorRGBA1323 = x3d.ColorRGBA()
ColorRGBA1323.USE = "HAnimSegmentLineColorRGBA"

LineSet1321.color = ColorRGBA1323

Shape1320.geometry = LineSet1321

Transform1319.children.append(Shape1320)

HAnimSegment1316.children.append(Transform1319)

HAnimJoint1315.children.append(HAnimSegment1316)
HAnimJoint1324 = x3d.HAnimJoint()
HAnimJoint1324.DEF = "STD_Joint_l_metacarpophalangeal_4"
HAnimJoint1324.name = "l_metacarpophalangeal_4"
HAnimJoint1324.center = [0.1956,0.7815,-0.0794]
HAnimSegment1325 = x3d.HAnimSegment()
HAnimSegment1325.DEF = "STD_Segment_l_carpal_proximal_phalanx_4"
HAnimSegment1325.name = "l_carpal_proximal_phalanx_4"
Transform1326 = x3d.Transform()
Transform1326.translation = [0.1956,0.7815,-0.0794]
Shape1327 = x3d.Shape()
Shape1327.USE = "HAnimJointShape"

Transform1326.children.append(Shape1327)

HAnimSegment1325.children.append(Transform1326)
Transform1328 = x3d.Transform()
Shape1329 = x3d.Shape()
LineSet1330 = x3d.LineSet()
LineSet1330.vertexCount = [2]
Coordinate1331 = x3d.Coordinate()

LineSet1330.coord = Coordinate1331
ColorRGBA1332 = x3d.ColorRGBA()
ColorRGBA1332.USE = "HAnimSegmentLineColorRGBA"

LineSet1330.color = ColorRGBA1332

Shape1329.geometry = LineSet1330

Transform1328.children.append(Shape1329)

HAnimSegment1325.children.append(Transform1328)

HAnimJoint1324.children.append(HAnimSegment1325)
HAnimJoint1333 = x3d.HAnimJoint()
HAnimJoint1333.DEF = "STD_Joint_l_carpal_proximal_interphalangeal_4"
HAnimJoint1333.name = "l_carpal_proximal_interphalangeal_4"
HAnimJoint1333.center = [0.1973,0.7287,-0.0777]
HAnimSegment1334 = x3d.HAnimSegment()
HAnimSegment1334.DEF = "STD_Segment_l_carpal_middle_phalanx_4"
HAnimSegment1334.name = "l_carpal_middle_phalanx_4"
Transform1335 = x3d.Transform()
Transform1335.translation = [0.1973,0.7287,-0.0777]
Shape1336 = x3d.Shape()
Shape1336.USE = "HAnimJointShape"

Transform1335.children.append(Shape1336)

HAnimSegment1334.children.append(Transform1335)
Transform1337 = x3d.Transform()
Shape1338 = x3d.Shape()
LineSet1339 = x3d.LineSet()
LineSet1339.vertexCount = [2]
Coordinate1340 = x3d.Coordinate()

LineSet1339.coord = Coordinate1340
ColorRGBA1341 = x3d.ColorRGBA()
ColorRGBA1341.USE = "HAnimSegmentLineColorRGBA"

LineSet1339.color = ColorRGBA1341

Shape1338.geometry = LineSet1339

Transform1337.children.append(Shape1338)

HAnimSegment1334.children.append(Transform1337)

HAnimJoint1333.children.append(HAnimSegment1334)
HAnimJoint1342 = x3d.HAnimJoint()
HAnimJoint1342.DEF = "STD_Joint_l_carpal_distal_interphalangeal_4"
HAnimJoint1342.name = "l_carpal_distal_interphalangeal_4"
HAnimJoint1342.center = [0.1983,0.7045,-0.0767]
HAnimSegment1343 = x3d.HAnimSegment()
HAnimSegment1343.DEF = "STD_Segment_l_carpal_distal_phalanx_4"
HAnimSegment1343.name = "l_carpal_distal_phalanx_4"
Transform1344 = x3d.Transform()
Transform1344.translation = [0.1983,0.7045,-0.0767]
Shape1345 = x3d.Shape()
Shape1345.USE = "HAnimJointShape"

Transform1344.children.append(Shape1345)

HAnimSegment1343.children.append(Transform1344)
Transform1346 = x3d.Transform()
Shape1347 = x3d.Shape()
LineSet1348 = x3d.LineSet()
LineSet1348.vertexCount = [2]
Coordinate1349 = x3d.Coordinate()

LineSet1348.coord = Coordinate1349
ColorRGBA1350 = x3d.ColorRGBA()
ColorRGBA1350.USE = "HAnimSegmentLineColorRGBA"

LineSet1348.color = ColorRGBA1350

Shape1347.geometry = LineSet1348

Transform1346.children.append(Shape1347)

HAnimSegment1343.children.append(Transform1346)
HAnimSite1351 = x3d.HAnimSite()
HAnimSite1351.DEF = "STD_Site_l_carpal_distal_phalanx_4_tip"
HAnimSite1351.name = "l_carpal_distal_phalanx_4_tip"
TouchSensor1352 = x3d.TouchSensor()
TouchSensor1352.description = "HAnimSite l_carpal_distal_phalanx_4_tip"

HAnimSite1351.children.append(TouchSensor1352)
Shape1353 = x3d.Shape()
Shape1353.USE = "HAnimSiteShape"

HAnimSite1351.children.append(Shape1353)

HAnimSegment1343.children.append(HAnimSite1351)

HAnimJoint1342.children.append(HAnimSegment1343)

HAnimJoint1333.children.append(HAnimJoint1342)

HAnimJoint1324.children.append(HAnimJoint1333)

HAnimJoint1315.children.append(HAnimJoint1324)

HAnimJoint1306.children.append(HAnimJoint1315)
HAnimJoint1354 = x3d.HAnimJoint()
HAnimJoint1354.DEF = "STD_Joint_l_carpometacarpal_5"
HAnimJoint1354.name = "l_carpometacarpal_5"
HAnimJoint1354.center = [0.1925,0.8066,-0.1036]
HAnimSegment1355 = x3d.HAnimSegment()
HAnimSegment1355.DEF = "STD_Segment_l_metacarpal_5"
HAnimSegment1355.name = "l_metacarpal_5"
Transform1356 = x3d.Transform()
Transform1356.translation = [0.1925,0.8066,-0.1036]
Shape1357 = x3d.Shape()
Shape1357.USE = "HAnimJointShape"

Transform1356.children.append(Shape1357)

HAnimSegment1355.children.append(Transform1356)
Transform1358 = x3d.Transform()
Shape1359 = x3d.Shape()
LineSet1360 = x3d.LineSet()
LineSet1360.vertexCount = [2]
Coordinate1361 = x3d.Coordinate()

LineSet1360.coord = Coordinate1361
ColorRGBA1362 = x3d.ColorRGBA()
ColorRGBA1362.USE = "HAnimSegmentLineColorRGBA"

LineSet1360.color = ColorRGBA1362

Shape1359.geometry = LineSet1360

Transform1358.children.append(Shape1359)

HAnimSegment1355.children.append(Transform1358)
HAnimSite1363 = x3d.HAnimSite()
HAnimSite1363.DEF = "STD_Site_l_metacarpal_phalanx_5_pt"
HAnimSite1363.name = "l_metacarpal_phalanx_5_pt"
HAnimSite1363.translation = [0.1929,0.7860,-0.1122]
TouchSensor1364 = x3d.TouchSensor()
TouchSensor1364.description = "HAnimSite l_metacarpal_phalanx_5_pt"

HAnimSite1363.children.append(TouchSensor1364)
Shape1365 = x3d.Shape()
Shape1365.USE = "HAnimSiteShape"

HAnimSite1363.children.append(Shape1365)

HAnimSegment1355.children.append(HAnimSite1363)

HAnimJoint1354.children.append(HAnimSegment1355)
HAnimJoint1366 = x3d.HAnimJoint()
HAnimJoint1366.DEF = "STD_Joint_l_metacarpophalangeal_5"
HAnimJoint1366.name = "l_metacarpophalangeal_5"
HAnimJoint1366.center = [0.1925,0.7866,-0.1036]
HAnimSegment1367 = x3d.HAnimSegment()
HAnimSegment1367.DEF = "STD_Segment_l_carpal_proximal_phalanx_5"
HAnimSegment1367.name = "l_carpal_proximal_phalanx_5"
Transform1368 = x3d.Transform()
Transform1368.translation = [0.1925,0.7866,-0.1036]
Shape1369 = x3d.Shape()
Shape1369.USE = "HAnimJointShape"

Transform1368.children.append(Shape1369)

HAnimSegment1367.children.append(Transform1368)
Transform1370 = x3d.Transform()
Shape1371 = x3d.Shape()
LineSet1372 = x3d.LineSet()
LineSet1372.vertexCount = [2]
Coordinate1373 = x3d.Coordinate()

LineSet1372.coord = Coordinate1373
ColorRGBA1374 = x3d.ColorRGBA()
ColorRGBA1374.USE = "HAnimSegmentLineColorRGBA"

LineSet1372.color = ColorRGBA1374

Shape1371.geometry = LineSet1372

Transform1370.children.append(Shape1371)

HAnimSegment1367.children.append(Transform1370)

HAnimJoint1366.children.append(HAnimSegment1367)
HAnimJoint1375 = x3d.HAnimJoint()
HAnimJoint1375.DEF = "STD_Joint_l_carpal_proximal_interphalangeal_5"
HAnimJoint1375.name = "l_carpal_proximal_interphalangeal_5"
HAnimJoint1375.center = [0.1938,0.7452,-0.1024]
HAnimSegment1376 = x3d.HAnimSegment()
HAnimSegment1376.DEF = "STD_Segment_l_carpal_middle_phalanx_5"
HAnimSegment1376.name = "l_carpal_middle_phalanx_5"
Transform1377 = x3d.Transform()
Transform1377.translation = [0.1938,0.7452,-0.1024]
Shape1378 = x3d.Shape()
Shape1378.USE = "HAnimJointShape"

Transform1377.children.append(Shape1378)

HAnimSegment1376.children.append(Transform1377)
Transform1379 = x3d.Transform()
Shape1380 = x3d.Shape()
LineSet1381 = x3d.LineSet()
LineSet1381.vertexCount = [2]
Coordinate1382 = x3d.Coordinate()

LineSet1381.coord = Coordinate1382
ColorRGBA1383 = x3d.ColorRGBA()
ColorRGBA1383.USE = "HAnimSegmentLineColorRGBA"

LineSet1381.color = ColorRGBA1383

Shape1380.geometry = LineSet1381

Transform1379.children.append(Shape1380)

HAnimSegment1376.children.append(Transform1379)

HAnimJoint1375.children.append(HAnimSegment1376)
HAnimJoint1384 = x3d.HAnimJoint()
HAnimJoint1384.DEF = "STD_Joint_l_carpal_distal_interphalangeal_5"
HAnimJoint1384.name = "l_carpal_distal_interphalangeal_5"
HAnimJoint1384.center = [0.1948,0.7277,-0.1017]
HAnimSegment1385 = x3d.HAnimSegment()
HAnimSegment1385.DEF = "STD_Segment_l_carpal_distal_phalanx_5"
HAnimSegment1385.name = "l_carpal_distal_phalanx_5"
Transform1386 = x3d.Transform()
Transform1386.translation = [0.1948,0.7277,-0.1017]
Shape1387 = x3d.Shape()
Shape1387.USE = "HAnimJointShape"

Transform1386.children.append(Shape1387)

HAnimSegment1385.children.append(Transform1386)
Transform1388 = x3d.Transform()
Shape1389 = x3d.Shape()
LineSet1390 = x3d.LineSet()
LineSet1390.vertexCount = [2]
Coordinate1391 = x3d.Coordinate()

LineSet1390.coord = Coordinate1391
ColorRGBA1392 = x3d.ColorRGBA()
ColorRGBA1392.USE = "HAnimSegmentLineColorRGBA"

LineSet1390.color = ColorRGBA1392

Shape1389.geometry = LineSet1390

Transform1388.children.append(Shape1389)

HAnimSegment1385.children.append(Transform1388)
HAnimSite1393 = x3d.HAnimSite()
HAnimSite1393.DEF = "STD_Site_l_carpal_distal_phalanx_5_tip"
HAnimSite1393.name = "l_carpal_distal_phalanx_5_tip"
TouchSensor1394 = x3d.TouchSensor()
TouchSensor1394.description = "HAnimSite l_carpal_distal_phalanx_5_tip"

HAnimSite1393.children.append(TouchSensor1394)
Shape1395 = x3d.Shape()
Shape1395.USE = "HAnimSiteShape"

HAnimSite1393.children.append(Shape1395)

HAnimSegment1385.children.append(HAnimSite1393)

HAnimJoint1384.children.append(HAnimSegment1385)

HAnimJoint1375.children.append(HAnimJoint1384)

HAnimJoint1366.children.append(HAnimJoint1375)

HAnimJoint1354.children.append(HAnimJoint1366)

HAnimJoint1306.children.append(HAnimJoint1354)

HAnimJoint1150.children.append(HAnimJoint1306)

HAnimJoint1129.children.append(HAnimJoint1150)

HAnimJoint1114.children.append(HAnimJoint1129)

HAnimJoint1105.children.append(HAnimJoint1114)

HAnimJoint1081.children.append(HAnimJoint1105)

HAnimJoint877.children.append(HAnimJoint1081)
HAnimJoint1396 = x3d.HAnimJoint()
HAnimJoint1396.DEF = "STD_Joint_r_sternoclavicular"
HAnimJoint1396.name = "r_sternoclavicular"
HAnimJoint1396.center = [-0.0694,1.4600,-0.0330]
HAnimSegment1397 = x3d.HAnimSegment()
HAnimSegment1397.DEF = "STD_Segment_r_clavicle"
HAnimSegment1397.name = "r_clavicle"
Transform1398 = x3d.Transform()
Transform1398.translation = [-0.0694,1.4600,-0.0330]
Shape1399 = x3d.Shape()
Shape1399.USE = "HAnimJointShape"

Transform1398.children.append(Shape1399)

HAnimSegment1397.children.append(Transform1398)
Transform1400 = x3d.Transform()
Shape1401 = x3d.Shape()
LineSet1402 = x3d.LineSet()
LineSet1402.vertexCount = [2]
Coordinate1403 = x3d.Coordinate()

LineSet1402.coord = Coordinate1403
ColorRGBA1404 = x3d.ColorRGBA()
ColorRGBA1404.USE = "HAnimSegmentLineColorRGBA"

LineSet1402.color = ColorRGBA1404

Shape1401.geometry = LineSet1402

Transform1400.children.append(Shape1401)

HAnimSegment1397.children.append(Transform1400)
HAnimSite1405 = x3d.HAnimSite()
HAnimSite1405.DEF = "STD_Site_r_acromion_pt"
HAnimSite1405.name = "r_acromion_pt"
HAnimSite1405.translation = [-0.1905,1.4791,-0.0431]
TouchSensor1406 = x3d.TouchSensor()
TouchSensor1406.description = "HAnimSite r_acromion_pt"

HAnimSite1405.children.append(TouchSensor1406)
Shape1407 = x3d.Shape()
Shape1407.USE = "HAnimSiteShape"

HAnimSite1405.children.append(Shape1407)

HAnimSegment1397.children.append(HAnimSite1405)
HAnimSite1408 = x3d.HAnimSite()
HAnimSite1408.DEF = "STD_Site_r_axilla_distal_pt"
HAnimSite1408.name = "r_axilla_distal_pt"
HAnimSite1408.translation = [-0.1603,1.4098,-0.0826]
TouchSensor1409 = x3d.TouchSensor()
TouchSensor1409.description = "HAnimSite r_axilla_distal_pt"

HAnimSite1408.children.append(TouchSensor1409)
Shape1410 = x3d.Shape()
Shape1410.USE = "HAnimSiteShape"

HAnimSite1408.children.append(Shape1410)

HAnimSegment1397.children.append(HAnimSite1408)
HAnimSite1411 = x3d.HAnimSite()
HAnimSite1411.DEF = "STD_Site_r_axilla_posterior_folds_pt"
HAnimSite1411.name = "r_axilla_posterior_folds_pt"
TouchSensor1412 = x3d.TouchSensor()
TouchSensor1412.description = "HAnimSite r_axilla_posterior_folds_pt"

HAnimSite1411.children.append(TouchSensor1412)
Shape1413 = x3d.Shape()
Shape1413.USE = "HAnimSiteShape"

HAnimSite1411.children.append(Shape1413)

HAnimSegment1397.children.append(HAnimSite1411)
HAnimSite1414 = x3d.HAnimSite()
HAnimSite1414.DEF = "STD_Site_r_axilla_proximal_pt"
HAnimSite1414.name = "r_axilla_proximal_pt"
HAnimSite1414.translation = [-0.1626,1.4072,-0.0031]
TouchSensor1415 = x3d.TouchSensor()
TouchSensor1415.description = "HAnimSite r_axilla_proximal_pt"

HAnimSite1414.children.append(TouchSensor1415)
Shape1416 = x3d.Shape()
Shape1416.USE = "HAnimSiteShape"

HAnimSite1414.children.append(Shape1416)

HAnimSegment1397.children.append(HAnimSite1414)
HAnimSite1417 = x3d.HAnimSite()
HAnimSite1417.DEF = "STD_Site_r_clavicale_pt"
HAnimSite1417.name = "r_clavicale_pt"
HAnimSite1417.translation = [-0.0115,1.4943,0.0400]
TouchSensor1418 = x3d.TouchSensor()
TouchSensor1418.description = "HAnimSite r_clavicale_pt"

HAnimSite1417.children.append(TouchSensor1418)
Shape1419 = x3d.Shape()
Shape1419.USE = "HAnimSiteShape"

HAnimSite1417.children.append(Shape1419)

HAnimSegment1397.children.append(HAnimSite1417)

HAnimJoint1396.children.append(HAnimSegment1397)
HAnimJoint1420 = x3d.HAnimJoint()
HAnimJoint1420.DEF = "STD_Joint_r_acromioclavicular"
HAnimJoint1420.name = "r_acromioclavicular"
HAnimJoint1420.center = [-0.0836,1.4281,-0.0401]
HAnimSegment1421 = x3d.HAnimSegment()
HAnimSegment1421.DEF = "STD_Segment_r_scapula"
HAnimSegment1421.name = "r_scapula"
Transform1422 = x3d.Transform()
Transform1422.translation = [-0.0836,1.4281,-0.0401]
Shape1423 = x3d.Shape()
Shape1423.USE = "HAnimJointShape"

Transform1422.children.append(Shape1423)

HAnimSegment1421.children.append(Transform1422)
Transform1424 = x3d.Transform()
Shape1425 = x3d.Shape()
LineSet1426 = x3d.LineSet()
LineSet1426.vertexCount = [2]
Coordinate1427 = x3d.Coordinate()

LineSet1426.coord = Coordinate1427
ColorRGBA1428 = x3d.ColorRGBA()
ColorRGBA1428.USE = "HAnimSegmentLineColorRGBA"

LineSet1426.color = ColorRGBA1428

Shape1425.geometry = LineSet1426

Transform1424.children.append(Shape1425)

HAnimSegment1421.children.append(Transform1424)

HAnimJoint1420.children.append(HAnimSegment1421)
HAnimJoint1429 = x3d.HAnimJoint()
HAnimJoint1429.DEF = "STD_Joint_r_shoulder"
HAnimJoint1429.name = "r_shoulder"
HAnimJoint1429.center = [-0.1907,1.4407,-0.0325]
HAnimSegment1430 = x3d.HAnimSegment()
HAnimSegment1430.DEF = "STD_Segment_r_upperarm"
HAnimSegment1430.name = "r_upperarm"
Transform1431 = x3d.Transform()
Transform1431.translation = [-0.1907,1.4407,-0.0325]
Shape1432 = x3d.Shape()
Shape1432.USE = "HAnimJointShape"

Transform1431.children.append(Shape1432)

HAnimSegment1430.children.append(Transform1431)
Transform1433 = x3d.Transform()
Shape1434 = x3d.Shape()
LineSet1435 = x3d.LineSet()
LineSet1435.vertexCount = [2]
Coordinate1436 = x3d.Coordinate()

LineSet1435.coord = Coordinate1436
ColorRGBA1437 = x3d.ColorRGBA()
ColorRGBA1437.USE = "HAnimSegmentLineColorRGBA"

LineSet1435.color = ColorRGBA1437

Shape1434.geometry = LineSet1435

Transform1433.children.append(Shape1434)

HAnimSegment1430.children.append(Transform1433)
HAnimSite1438 = x3d.HAnimSite()
HAnimSite1438.DEF = "STD_Site_r_bideltoid_pt"
HAnimSite1438.name = "r_bideltoid_pt"
TouchSensor1439 = x3d.TouchSensor()
TouchSensor1439.description = "HAnimSite r_bideltoid_pt"

HAnimSite1438.children.append(TouchSensor1439)
Shape1440 = x3d.Shape()
Shape1440.USE = "HAnimSiteShape"

HAnimSite1438.children.append(Shape1440)

HAnimSegment1430.children.append(HAnimSite1438)
HAnimSite1441 = x3d.HAnimSite()
HAnimSite1441.DEF = "STD_Site_r_humeral_lateral_epicondyles_pt"
HAnimSite1441.name = "r_humeral_lateral_epicondyles_pt"
HAnimSite1441.translation = [-0.2224,1.1517,-0.1033]
TouchSensor1442 = x3d.TouchSensor()
TouchSensor1442.description = "HAnimSite r_humeral_lateral_epicondyles_pt"

HAnimSite1441.children.append(TouchSensor1442)
Shape1443 = x3d.Shape()
Shape1443.USE = "HAnimSiteShape"

HAnimSite1441.children.append(Shape1443)

HAnimSegment1430.children.append(HAnimSite1441)

HAnimJoint1429.children.append(HAnimSegment1430)
HAnimJoint1444 = x3d.HAnimJoint()
HAnimJoint1444.DEF = "STD_Joint_r_elbow"
HAnimJoint1444.name = "r_elbow"
HAnimJoint1444.center = [-0.1949,1.1388,-0.0620]
HAnimSegment1445 = x3d.HAnimSegment()
HAnimSegment1445.DEF = "STD_Segment_r_forearm"
HAnimSegment1445.name = "r_forearm"
Transform1446 = x3d.Transform()
Transform1446.translation = [-0.1949,1.1388,-0.0620]
Shape1447 = x3d.Shape()
Shape1447.USE = "HAnimJointShape"

Transform1446.children.append(Shape1447)

HAnimSegment1445.children.append(Transform1446)
Transform1448 = x3d.Transform()
Shape1449 = x3d.Shape()
LineSet1450 = x3d.LineSet()
LineSet1450.vertexCount = [2]
Coordinate1451 = x3d.Coordinate()

LineSet1450.coord = Coordinate1451
ColorRGBA1452 = x3d.ColorRGBA()
ColorRGBA1452.USE = "HAnimSegmentLineColorRGBA"

LineSet1450.color = ColorRGBA1452

Shape1449.geometry = LineSet1450

Transform1448.children.append(Shape1449)

HAnimSegment1445.children.append(Transform1448)
HAnimSite1453 = x3d.HAnimSite()
HAnimSite1453.DEF = "STD_Site_r_humeral_medial_epicondyles_pt"
HAnimSite1453.name = "r_humeral_medial_epicondyles_pt"
HAnimSite1453.translation = [-0.1680,1.1298,-0.1062]
TouchSensor1454 = x3d.TouchSensor()
TouchSensor1454.description = "HAnimSite r_humeral_medial_epicondyles_pt"

HAnimSite1453.children.append(TouchSensor1454)
Shape1455 = x3d.Shape()
Shape1455.USE = "HAnimSiteShape"

HAnimSite1453.children.append(Shape1455)

HAnimSegment1445.children.append(HAnimSite1453)
HAnimSite1456 = x3d.HAnimSite()
HAnimSite1456.DEF = "STD_Site_r_olecranon_pt"
HAnimSite1456.name = "r_olecranon_pt"
HAnimSite1456.translation = [-0.1907,1.1405,-0.1065]
TouchSensor1457 = x3d.TouchSensor()
TouchSensor1457.description = "HAnimSite r_olecranon_pt"

HAnimSite1456.children.append(TouchSensor1457)
Shape1458 = x3d.Shape()
Shape1458.USE = "HAnimSiteShape"

HAnimSite1456.children.append(Shape1458)

HAnimSegment1445.children.append(HAnimSite1456)
HAnimSite1459 = x3d.HAnimSite()
HAnimSite1459.DEF = "STD_Site_r_radial_styloid_pt"
HAnimSite1459.name = "r_radial_styloid_pt"
HAnimSite1459.translation = [-0.1884,0.8676,-0.0360]
TouchSensor1460 = x3d.TouchSensor()
TouchSensor1460.description = "HAnimSite r_radial_styloid_pt"

HAnimSite1459.children.append(TouchSensor1460)
Shape1461 = x3d.Shape()
Shape1461.USE = "HAnimSiteShape"

HAnimSite1459.children.append(Shape1461)

HAnimSegment1445.children.append(HAnimSite1459)
HAnimSite1462 = x3d.HAnimSite()
HAnimSite1462.DEF = "STD_Site_r_radiale_pt"
HAnimSite1462.name = "r_radiale_pt"
HAnimSite1462.translation = [-0.2130,1.1305,-0.1091]
TouchSensor1463 = x3d.TouchSensor()
TouchSensor1463.description = "HAnimSite r_radiale_pt"

HAnimSite1462.children.append(TouchSensor1463)
Shape1464 = x3d.Shape()
Shape1464.USE = "HAnimSiteShape"

HAnimSite1462.children.append(Shape1464)

HAnimSegment1445.children.append(HAnimSite1462)

HAnimJoint1444.children.append(HAnimSegment1445)
HAnimJoint1465 = x3d.HAnimJoint()
HAnimJoint1465.DEF = "STD_Joint_r_radiocarpal"
HAnimJoint1465.name = "r_radiocarpal"
HAnimJoint1465.center = [-0.1959,0.8694,-0.0521]
HAnimSegment1466 = x3d.HAnimSegment()
HAnimSegment1466.DEF = "STD_Segment_r_carpal"
HAnimSegment1466.name = "r_carpal"
Transform1467 = x3d.Transform()
Transform1467.translation = [-0.1959,0.8694,-0.0521]
Shape1468 = x3d.Shape()
Shape1468.USE = "HAnimJointShape"

Transform1467.children.append(Shape1468)

HAnimSegment1466.children.append(Transform1467)
Transform1469 = x3d.Transform()
Shape1470 = x3d.Shape()
LineSet1471 = x3d.LineSet()
LineSet1471.vertexCount = [2]
Coordinate1472 = x3d.Coordinate()

LineSet1471.coord = Coordinate1472
ColorRGBA1473 = x3d.ColorRGBA()
ColorRGBA1473.USE = "HAnimSegmentLineColorRGBA"

LineSet1471.color = ColorRGBA1473

Shape1470.geometry = LineSet1471

Transform1469.children.append(Shape1470)

HAnimSegment1466.children.append(Transform1469)
HAnimSite1474 = x3d.HAnimSite()
HAnimSite1474.DEF = "STD_Site_r_ulnar_styloid_pt"
HAnimSite1474.name = "r_ulnar_styloid_pt"
HAnimSite1474.translation = [-0.2117,0.8562,-0.0584]
TouchSensor1475 = x3d.TouchSensor()
TouchSensor1475.description = "HAnimSite r_ulnar_styloid_pt"

HAnimSite1474.children.append(TouchSensor1475)
Shape1476 = x3d.Shape()
Shape1476.USE = "HAnimSiteShape"

HAnimSite1474.children.append(Shape1476)

HAnimSegment1466.children.append(HAnimSite1474)

HAnimJoint1465.children.append(HAnimSegment1466)
HAnimJoint1477 = x3d.HAnimJoint()
HAnimJoint1477.DEF = "STD_Joint_r_midcarpal_1"
HAnimJoint1477.name = "r_midcarpal_1"
HAnimJoint1477.center = [0,1,0]
HAnimSegment1478 = x3d.HAnimSegment()
HAnimSegment1478.DEF = "STD_Segment_r_trapezium"
HAnimSegment1478.name = "r_trapezium"
Transform1479 = x3d.Transform()
Transform1479.translation = [0,1,0]
Shape1480 = x3d.Shape()
Shape1480.USE = "HAnimJointShape"

Transform1479.children.append(Shape1480)

HAnimSegment1478.children.append(Transform1479)
Transform1481 = x3d.Transform()
Shape1482 = x3d.Shape()
LineSet1483 = x3d.LineSet()
LineSet1483.vertexCount = [2]
Coordinate1484 = x3d.Coordinate()

LineSet1483.coord = Coordinate1484
ColorRGBA1485 = x3d.ColorRGBA()
ColorRGBA1485.USE = "HAnimSegmentLineColorRGBA"

LineSet1483.color = ColorRGBA1485

Shape1482.geometry = LineSet1483

Transform1481.children.append(Shape1482)

HAnimSegment1478.children.append(Transform1481)

HAnimJoint1477.children.append(HAnimSegment1478)
HAnimJoint1486 = x3d.HAnimJoint()
HAnimJoint1486.DEF = "STD_Joint_r_carpometacarpal_1"
HAnimJoint1486.name = "r_carpometacarpal_1"
HAnimJoint1486.center = [-0.1899,0.8502,-0.0473]
HAnimSegment1487 = x3d.HAnimSegment()
HAnimSegment1487.DEF = "STD_Segment_r_metacarpal_1"
HAnimSegment1487.name = "r_metacarpal_1"
Transform1488 = x3d.Transform()
Transform1488.translation = [-0.1899,0.8502,-0.0473]
Shape1489 = x3d.Shape()
Shape1489.USE = "HAnimJointShape"

Transform1488.children.append(Shape1489)

HAnimSegment1487.children.append(Transform1488)
Transform1490 = x3d.Transform()
Shape1491 = x3d.Shape()
LineSet1492 = x3d.LineSet()
LineSet1492.vertexCount = [2]
Coordinate1493 = x3d.Coordinate()

LineSet1492.coord = Coordinate1493
ColorRGBA1494 = x3d.ColorRGBA()
ColorRGBA1494.USE = "HAnimSegmentLineColorRGBA"

LineSet1492.color = ColorRGBA1494

Shape1491.geometry = LineSet1492

Transform1490.children.append(Shape1491)

HAnimSegment1487.children.append(Transform1490)

HAnimJoint1486.children.append(HAnimSegment1487)
HAnimJoint1495 = x3d.HAnimJoint()
HAnimJoint1495.DEF = "STD_Joint_r_metacarpophalangeal_1"
HAnimJoint1495.name = "r_metacarpophalangeal_1"
HAnimJoint1495.center = [-0.1874,0.8256,0.0306]
HAnimSegment1496 = x3d.HAnimSegment()
HAnimSegment1496.DEF = "STD_Segment_r_carpal_proximal_phalanx_1"
HAnimSegment1496.name = "r_carpal_proximal_phalanx_1"
Transform1497 = x3d.Transform()
Transform1497.translation = [-0.1874,0.8256,0.0306]
Shape1498 = x3d.Shape()
Shape1498.USE = "HAnimJointShape"

Transform1497.children.append(Shape1498)

HAnimSegment1496.children.append(Transform1497)
Transform1499 = x3d.Transform()
Shape1500 = x3d.Shape()
LineSet1501 = x3d.LineSet()
LineSet1501.vertexCount = [2]
Coordinate1502 = x3d.Coordinate()

LineSet1501.coord = Coordinate1502
ColorRGBA1503 = x3d.ColorRGBA()
ColorRGBA1503.USE = "HAnimSegmentLineColorRGBA"

LineSet1501.color = ColorRGBA1503

Shape1500.geometry = LineSet1501

Transform1499.children.append(Shape1500)

HAnimSegment1496.children.append(Transform1499)

HAnimJoint1495.children.append(HAnimSegment1496)
HAnimJoint1504 = x3d.HAnimJoint()
HAnimJoint1504.DEF = "STD_Joint_r_carpal_interphalangeal_1"
HAnimJoint1504.name = "r_carpal_interphalangeal_1"
HAnimJoint1504.center = [-0.1864,0.8190,0.0506]
HAnimSegment1505 = x3d.HAnimSegment()
HAnimSegment1505.DEF = "STD_Segment_r_carpal_distal_phalanx_1"
HAnimSegment1505.name = "r_carpal_distal_phalanx_1"
Transform1506 = x3d.Transform()
Transform1506.translation = [-0.1864,0.8190,0.0506]
Shape1507 = x3d.Shape()
Shape1507.USE = "HAnimJointShape"

Transform1506.children.append(Shape1507)

HAnimSegment1505.children.append(Transform1506)
Transform1508 = x3d.Transform()
Shape1509 = x3d.Shape()
LineSet1510 = x3d.LineSet()
LineSet1510.vertexCount = [2]
Coordinate1511 = x3d.Coordinate()

LineSet1510.coord = Coordinate1511
ColorRGBA1512 = x3d.ColorRGBA()
ColorRGBA1512.USE = "HAnimSegmentLineColorRGBA"

LineSet1510.color = ColorRGBA1512

Shape1509.geometry = LineSet1510

Transform1508.children.append(Shape1509)

HAnimSegment1505.children.append(Transform1508)
HAnimSite1513 = x3d.HAnimSite()
HAnimSite1513.DEF = "STD_Site_r_carpal_distal_phalanx_1_tip"
HAnimSite1513.name = "r_carpal_distal_phalanx_1_tip"
TouchSensor1514 = x3d.TouchSensor()
TouchSensor1514.description = "HAnimSite r_carpal_distal_phalanx_1_tip"

HAnimSite1513.children.append(TouchSensor1514)
Shape1515 = x3d.Shape()
Shape1515.USE = "HAnimSiteShape"

HAnimSite1513.children.append(Shape1515)

HAnimSegment1505.children.append(HAnimSite1513)

HAnimJoint1504.children.append(HAnimSegment1505)

HAnimJoint1495.children.append(HAnimJoint1504)

HAnimJoint1486.children.append(HAnimJoint1495)

HAnimJoint1477.children.append(HAnimJoint1486)

HAnimJoint1465.children.append(HAnimJoint1477)
HAnimJoint1516 = x3d.HAnimJoint()
HAnimJoint1516.DEF = "STD_Joint_r_midcarpal_2"
HAnimJoint1516.name = "r_midcarpal_2"
HAnimJoint1516.center = [0,1,0]
HAnimSegment1517 = x3d.HAnimSegment()
HAnimSegment1517.DEF = "STD_Segment_r_trapezoid"
HAnimSegment1517.name = "r_trapezoid"
Transform1518 = x3d.Transform()
Transform1518.translation = [0,1,0]
Shape1519 = x3d.Shape()
Shape1519.USE = "HAnimJointShape"

Transform1518.children.append(Shape1519)

HAnimSegment1517.children.append(Transform1518)
Transform1520 = x3d.Transform()
Shape1521 = x3d.Shape()
LineSet1522 = x3d.LineSet()
LineSet1522.vertexCount = [2]
Coordinate1523 = x3d.Coordinate()

LineSet1522.coord = Coordinate1523
ColorRGBA1524 = x3d.ColorRGBA()
ColorRGBA1524.USE = "HAnimSegmentLineColorRGBA"

LineSet1522.color = ColorRGBA1524

Shape1521.geometry = LineSet1522

Transform1520.children.append(Shape1521)

HAnimSegment1517.children.append(Transform1520)

HAnimJoint1516.children.append(HAnimSegment1517)
HAnimJoint1525 = x3d.HAnimJoint()
HAnimJoint1525.DEF = "STD_Joint_r_carpometacarpal_2"
HAnimJoint1525.name = "r_carpometacarpal_2"
HAnimJoint1525.center = [-0.1961,0.8055,-0.0218]
HAnimSegment1526 = x3d.HAnimSegment()
HAnimSegment1526.DEF = "STD_Segment_r_metacarpal_2"
HAnimSegment1526.name = "r_metacarpal_2"
Transform1527 = x3d.Transform()
Transform1527.translation = [-0.1961,0.8055,-0.0218]
Shape1528 = x3d.Shape()
Shape1528.USE = "HAnimJointShape"

Transform1527.children.append(Shape1528)

HAnimSegment1526.children.append(Transform1527)
Transform1529 = x3d.Transform()
Shape1530 = x3d.Shape()
LineSet1531 = x3d.LineSet()
LineSet1531.vertexCount = [2]
Coordinate1532 = x3d.Coordinate()

LineSet1531.coord = Coordinate1532
ColorRGBA1533 = x3d.ColorRGBA()
ColorRGBA1533.USE = "HAnimSegmentLineColorRGBA"

LineSet1531.color = ColorRGBA1533

Shape1530.geometry = LineSet1531

Transform1529.children.append(Shape1530)

HAnimSegment1526.children.append(Transform1529)
HAnimSite1534 = x3d.HAnimSite()
HAnimSite1534.DEF = "STD_Site_r_metacarpal_phalanx_2_pt"
HAnimSite1534.name = "r_metacarpal_phalanx_2_pt"
HAnimSite1534.translation = [-0.1977,0.8169,-0.0177]
TouchSensor1535 = x3d.TouchSensor()
TouchSensor1535.description = "HAnimSite r_metacarpal_phalanx_2_pt"

HAnimSite1534.children.append(TouchSensor1535)
Shape1536 = x3d.Shape()
Shape1536.USE = "HAnimSiteShape"

HAnimSite1534.children.append(Shape1536)

HAnimSegment1526.children.append(HAnimSite1534)

HAnimJoint1525.children.append(HAnimSegment1526)
HAnimJoint1537 = x3d.HAnimJoint()
HAnimJoint1537.DEF = "STD_Joint_r_metacarpophalangeal_2"
HAnimJoint1537.name = "r_metacarpophalangeal_2"
HAnimJoint1537.center = [-0.1961,0.7846,-0.0218]
HAnimSegment1538 = x3d.HAnimSegment()
HAnimSegment1538.DEF = "STD_Segment_r_carpal_proximal_phalanx_2 "
HAnimSegment1538.name = "r_carpal_proximal_phalanx_2 "
Transform1539 = x3d.Transform()
Transform1539.translation = [-0.1961,0.7846,-0.0218]
Shape1540 = x3d.Shape()
Shape1540.USE = "HAnimJointShape"

Transform1539.children.append(Shape1540)

HAnimSegment1538.children.append(Transform1539)
Transform1541 = x3d.Transform()
Shape1542 = x3d.Shape()
LineSet1543 = x3d.LineSet()
LineSet1543.vertexCount = [2]
Coordinate1544 = x3d.Coordinate()

LineSet1543.coord = Coordinate1544
ColorRGBA1545 = x3d.ColorRGBA()
ColorRGBA1545.USE = "HAnimSegmentLineColorRGBA"

LineSet1543.color = ColorRGBA1545

Shape1542.geometry = LineSet1543

Transform1541.children.append(Shape1542)

HAnimSegment1538.children.append(Transform1541)

HAnimJoint1537.children.append(HAnimSegment1538)
HAnimJoint1546 = x3d.HAnimJoint()
HAnimJoint1546.DEF = "STD_Joint_r_carpal_proximal_interphalangeal_2"
HAnimJoint1546.name = "r_carpal_proximal_interphalangeal_2"
HAnimJoint1546.center = [-0.1954,0.7393,-0.0185]
HAnimSegment1547 = x3d.HAnimSegment()
HAnimSegment1547.DEF = "STD_Segment_r_carpal_middle_phalanx_2"
HAnimSegment1547.name = "r_carpal_middle_phalanx_2"
Transform1548 = x3d.Transform()
Transform1548.translation = [-0.1954,0.7393,-0.0185]
Shape1549 = x3d.Shape()
Shape1549.USE = "HAnimJointShape"

Transform1548.children.append(Shape1549)

HAnimSegment1547.children.append(Transform1548)
Transform1550 = x3d.Transform()
Shape1551 = x3d.Shape()
LineSet1552 = x3d.LineSet()
LineSet1552.vertexCount = [2]
Coordinate1553 = x3d.Coordinate()

LineSet1552.coord = Coordinate1553
ColorRGBA1554 = x3d.ColorRGBA()
ColorRGBA1554.USE = "HAnimSegmentLineColorRGBA"

LineSet1552.color = ColorRGBA1554

Shape1551.geometry = LineSet1552

Transform1550.children.append(Shape1551)

HAnimSegment1547.children.append(Transform1550)

HAnimJoint1546.children.append(HAnimSegment1547)
HAnimJoint1555 = x3d.HAnimJoint()
HAnimJoint1555.DEF = "STD_Joint_r_carpal_distal_interphalangeal_2"
HAnimJoint1555.name = "r_carpal_distal_interphalangeal_2"
HAnimJoint1555.center = [-0.1945,0.7169,-0.0173]
HAnimSegment1556 = x3d.HAnimSegment()
HAnimSegment1556.DEF = "STD_Segment_r_carpal_distal_phalanx_2"
HAnimSegment1556.name = "r_carpal_distal_phalanx_2"
Transform1557 = x3d.Transform()
Transform1557.translation = [-0.1945,0.7169,-0.0173]
Shape1558 = x3d.Shape()
Shape1558.USE = "HAnimJointShape"

Transform1557.children.append(Shape1558)

HAnimSegment1556.children.append(Transform1557)
Transform1559 = x3d.Transform()
Shape1560 = x3d.Shape()
LineSet1561 = x3d.LineSet()
LineSet1561.vertexCount = [2]
Coordinate1562 = x3d.Coordinate()

LineSet1561.coord = Coordinate1562
ColorRGBA1563 = x3d.ColorRGBA()
ColorRGBA1563.USE = "HAnimSegmentLineColorRGBA"

LineSet1561.color = ColorRGBA1563

Shape1560.geometry = LineSet1561

Transform1559.children.append(Shape1560)

HAnimSegment1556.children.append(Transform1559)
HAnimSite1564 = x3d.HAnimSite()
HAnimSite1564.DEF = "STD_Site_r_carpal_distal_phalanx_2_tip"
HAnimSite1564.name = "r_carpal_distal_phalanx_2_tip"
TouchSensor1565 = x3d.TouchSensor()
TouchSensor1565.description = "HAnimSite r_carpal_distal_phalanx_2_tip"

HAnimSite1564.children.append(TouchSensor1565)
Shape1566 = x3d.Shape()
Shape1566.USE = "HAnimSiteShape"

HAnimSite1564.children.append(Shape1566)

HAnimSegment1556.children.append(HAnimSite1564)
HAnimSite1567 = x3d.HAnimSite()
HAnimSite1567.DEF = "STD_Site_r_dactylion_pt"
HAnimSite1567.name = "r_dactylion_pt"
HAnimSite1567.translation = [-0.1941,0.6772,-0.0423]
TouchSensor1568 = x3d.TouchSensor()
TouchSensor1568.description = "HAnimSite r_dactylion_pt"

HAnimSite1567.children.append(TouchSensor1568)
Shape1569 = x3d.Shape()
Shape1569.USE = "HAnimSiteShape"

HAnimSite1567.children.append(Shape1569)

HAnimSegment1556.children.append(HAnimSite1567)

HAnimJoint1555.children.append(HAnimSegment1556)

HAnimJoint1546.children.append(HAnimJoint1555)

HAnimJoint1537.children.append(HAnimJoint1546)

HAnimJoint1525.children.append(HAnimJoint1537)

HAnimJoint1516.children.append(HAnimJoint1525)

HAnimJoint1465.children.append(HAnimJoint1516)
HAnimJoint1570 = x3d.HAnimJoint()
HAnimJoint1570.DEF = "STD_Joint_r_midcarpal_3"
HAnimJoint1570.name = "r_midcarpal_3"
HAnimJoint1570.center = [0,1,0]
HAnimSegment1571 = x3d.HAnimSegment()
HAnimSegment1571.DEF = "STD_Segment_r_capitate"
HAnimSegment1571.name = "r_capitate"
Transform1572 = x3d.Transform()
Transform1572.translation = [0,1,0]
Shape1573 = x3d.Shape()
Shape1573.USE = "HAnimJointShape"

Transform1572.children.append(Shape1573)

HAnimSegment1571.children.append(Transform1572)
Transform1574 = x3d.Transform()
Shape1575 = x3d.Shape()
LineSet1576 = x3d.LineSet()
LineSet1576.vertexCount = [2]
Coordinate1577 = x3d.Coordinate()

LineSet1576.coord = Coordinate1577
ColorRGBA1578 = x3d.ColorRGBA()
ColorRGBA1578.USE = "HAnimSegmentLineColorRGBA"

LineSet1576.color = ColorRGBA1578

Shape1575.geometry = LineSet1576

Transform1574.children.append(Shape1575)

HAnimSegment1571.children.append(Transform1574)

HAnimJoint1570.children.append(HAnimSegment1571)
HAnimJoint1579 = x3d.HAnimJoint()
HAnimJoint1579.DEF = "STD_Joint_r_carpometacarpal_3"
HAnimJoint1579.name = "r_carpometacarpal_3"
HAnimJoint1579.center = [-0.1972,0.8060,-0.0468]
HAnimSegment1580 = x3d.HAnimSegment()
HAnimSegment1580.DEF = "STD_Segment_r_metacarpal_3"
HAnimSegment1580.name = "r_metacarpal_3"
Transform1581 = x3d.Transform()
Transform1581.translation = [-0.1972,0.8060,-0.0468]
Shape1582 = x3d.Shape()
Shape1582.USE = "HAnimJointShape"

Transform1581.children.append(Shape1582)

HAnimSegment1580.children.append(Transform1581)
Transform1583 = x3d.Transform()
Shape1584 = x3d.Shape()
LineSet1585 = x3d.LineSet()
LineSet1585.vertexCount = [2]
Coordinate1586 = x3d.Coordinate()

LineSet1585.coord = Coordinate1586
ColorRGBA1587 = x3d.ColorRGBA()
ColorRGBA1587.USE = "HAnimSegmentLineColorRGBA"

LineSet1585.color = ColorRGBA1587

Shape1584.geometry = LineSet1585

Transform1583.children.append(Shape1584)

HAnimSegment1580.children.append(Transform1583)
HAnimSite1588 = x3d.HAnimSite()
HAnimSite1588.DEF = "STD_Site_r_metacarpal_phalanx_3_pt"
HAnimSite1588.name = "r_metacarpal_phalanx_3_pt"
TouchSensor1589 = x3d.TouchSensor()
TouchSensor1589.description = "HAnimSite r_metacarpal_phalanx_3_pt"

HAnimSite1588.children.append(TouchSensor1589)
Shape1590 = x3d.Shape()
Shape1590.USE = "HAnimSiteShape"

HAnimSite1588.children.append(Shape1590)

HAnimSegment1580.children.append(HAnimSite1588)

HAnimJoint1579.children.append(HAnimSegment1580)
HAnimJoint1591 = x3d.HAnimJoint()
HAnimJoint1591.DEF = "STD_Joint_r_metacarpophalangeal_3"
HAnimJoint1591.name = "r_metacarpophalangeal_3"
HAnimJoint1591.center = [-0.1972,0.7849,-0.0468]
HAnimSegment1592 = x3d.HAnimSegment()
HAnimSegment1592.DEF = "STD_Segment_r_carpal_proximal_phalanx_3"
HAnimSegment1592.name = "r_carpal_proximal_phalanx_3"
Transform1593 = x3d.Transform()
Transform1593.translation = [-0.1972,0.7849,-0.0468]
Shape1594 = x3d.Shape()
Shape1594.USE = "HAnimJointShape"

Transform1593.children.append(Shape1594)

HAnimSegment1592.children.append(Transform1593)
Transform1595 = x3d.Transform()
Shape1596 = x3d.Shape()
LineSet1597 = x3d.LineSet()
LineSet1597.vertexCount = [2]
Coordinate1598 = x3d.Coordinate()

LineSet1597.coord = Coordinate1598
ColorRGBA1599 = x3d.ColorRGBA()
ColorRGBA1599.USE = "HAnimSegmentLineColorRGBA"

LineSet1597.color = ColorRGBA1599

Shape1596.geometry = LineSet1597

Transform1595.children.append(Shape1596)

HAnimSegment1592.children.append(Transform1595)

HAnimJoint1591.children.append(HAnimSegment1592)
HAnimJoint1600 = x3d.HAnimJoint()
HAnimJoint1600.DEF = "STD_Joint_r_carpal_proximal_interphalangeal_3"
HAnimJoint1600.name = "r_carpal_proximal_interphalangeal_3"
HAnimJoint1600.center = [-0.1950,0.7304,-0.0441]
HAnimSegment1601 = x3d.HAnimSegment()
HAnimSegment1601.DEF = "STD_Segment_r_carpal_middle_phalanx_3"
HAnimSegment1601.name = "r_carpal_middle_phalanx_3"
Transform1602 = x3d.Transform()
Transform1602.translation = [-0.1950,0.7304,-0.0441]
Shape1603 = x3d.Shape()
Shape1603.USE = "HAnimJointShape"

Transform1602.children.append(Shape1603)

HAnimSegment1601.children.append(Transform1602)
Transform1604 = x3d.Transform()
Shape1605 = x3d.Shape()
LineSet1606 = x3d.LineSet()
LineSet1606.vertexCount = [2]
Coordinate1607 = x3d.Coordinate()

LineSet1606.coord = Coordinate1607
ColorRGBA1608 = x3d.ColorRGBA()
ColorRGBA1608.USE = "HAnimSegmentLineColorRGBA"

LineSet1606.color = ColorRGBA1608

Shape1605.geometry = LineSet1606

Transform1604.children.append(Shape1605)

HAnimSegment1601.children.append(Transform1604)

HAnimJoint1600.children.append(HAnimSegment1601)
HAnimJoint1609 = x3d.HAnimJoint()
HAnimJoint1609.DEF = "STD_Joint_r_carpal_distal_interphalangeal_3"
HAnimJoint1609.name = "r_carpal_distal_interphalangeal_3"
HAnimJoint1609.center = [-0.1939,0.7042,-0.0432]
HAnimSegment1610 = x3d.HAnimSegment()
HAnimSegment1610.DEF = "STD_Segment_r_carpal_distal_phalanx_3"
HAnimSegment1610.name = "r_carpal_distal_phalanx_3"
Transform1611 = x3d.Transform()
Transform1611.translation = [-0.1939,0.7042,-0.0432]
Shape1612 = x3d.Shape()
Shape1612.USE = "HAnimJointShape"

Transform1611.children.append(Shape1612)

HAnimSegment1610.children.append(Transform1611)
Transform1613 = x3d.Transform()
Shape1614 = x3d.Shape()
LineSet1615 = x3d.LineSet()
LineSet1615.vertexCount = [2]
Coordinate1616 = x3d.Coordinate()

LineSet1615.coord = Coordinate1616
ColorRGBA1617 = x3d.ColorRGBA()
ColorRGBA1617.USE = "HAnimSegmentLineColorRGBA"

LineSet1615.color = ColorRGBA1617

Shape1614.geometry = LineSet1615

Transform1613.children.append(Shape1614)

HAnimSegment1610.children.append(Transform1613)
HAnimSite1618 = x3d.HAnimSite()
HAnimSite1618.DEF = "STD_Site_r_carpal_distal_phalanx_3_tip"
HAnimSite1618.name = "r_carpal_distal_phalanx_3_tip"
TouchSensor1619 = x3d.TouchSensor()
TouchSensor1619.description = "HAnimSite r_carpal_distal_phalanx_3_tip"

HAnimSite1618.children.append(TouchSensor1619)
Shape1620 = x3d.Shape()
Shape1620.USE = "HAnimSiteShape"

HAnimSite1618.children.append(Shape1620)

HAnimSegment1610.children.append(HAnimSite1618)

HAnimJoint1609.children.append(HAnimSegment1610)

HAnimJoint1600.children.append(HAnimJoint1609)

HAnimJoint1591.children.append(HAnimJoint1600)

HAnimJoint1579.children.append(HAnimJoint1591)

HAnimJoint1570.children.append(HAnimJoint1579)

HAnimJoint1465.children.append(HAnimJoint1570)
HAnimJoint1621 = x3d.HAnimJoint()
HAnimJoint1621.DEF = "STD_Joint_r_midcarpal_4_5"
HAnimJoint1621.name = "r_midcarpal_4_5"
HAnimJoint1621.center = [0,1,0]
HAnimSegment1622 = x3d.HAnimSegment()
HAnimSegment1622.DEF = "STD_Segment_r_hamate"
HAnimSegment1622.name = "r_hamate"
Transform1623 = x3d.Transform()
Transform1623.translation = [0,1,0]
Shape1624 = x3d.Shape()
Shape1624.USE = "HAnimJointShape"

Transform1623.children.append(Shape1624)

HAnimSegment1622.children.append(Transform1623)
Transform1625 = x3d.Transform()
Shape1626 = x3d.Shape()
LineSet1627 = x3d.LineSet()
LineSet1627.vertexCount = [2]
Coordinate1628 = x3d.Coordinate()

LineSet1627.coord = Coordinate1628
ColorRGBA1629 = x3d.ColorRGBA()
ColorRGBA1629.USE = "HAnimSegmentLineColorRGBA"

LineSet1627.color = ColorRGBA1629

Shape1626.geometry = LineSet1627

Transform1625.children.append(Shape1626)

HAnimSegment1622.children.append(Transform1625)

HAnimJoint1621.children.append(HAnimSegment1622)
HAnimJoint1630 = x3d.HAnimJoint()
HAnimJoint1630.DEF = "STD_Joint_r_carpometacarpal_4"
HAnimJoint1630.name = "r_carpometacarpal_4"
HAnimJoint1630.center = [-0.1951,0.8049,-0.0732]
HAnimSegment1631 = x3d.HAnimSegment()
HAnimSegment1631.DEF = "STD_Segment_r_metacarpal_4"
HAnimSegment1631.name = "r_metacarpal_4"
Transform1632 = x3d.Transform()
Transform1632.translation = [-0.1951,0.8049,-0.0732]
Shape1633 = x3d.Shape()
Shape1633.USE = "HAnimJointShape"

Transform1632.children.append(Shape1633)

HAnimSegment1631.children.append(Transform1632)
Transform1634 = x3d.Transform()
Shape1635 = x3d.Shape()
LineSet1636 = x3d.LineSet()
LineSet1636.vertexCount = [2]
Coordinate1637 = x3d.Coordinate()

LineSet1636.coord = Coordinate1637
ColorRGBA1638 = x3d.ColorRGBA()
ColorRGBA1638.USE = "HAnimSegmentLineColorRGBA"

LineSet1636.color = ColorRGBA1638

Shape1635.geometry = LineSet1636

Transform1634.children.append(Shape1635)

HAnimSegment1631.children.append(Transform1634)

HAnimJoint1630.children.append(HAnimSegment1631)
HAnimJoint1639 = x3d.HAnimJoint()
HAnimJoint1639.DEF = "STD_Joint_r_metacarpophalangeal_4"
HAnimJoint1639.name = "r_metacarpophalangeal_4"
HAnimJoint1639.center = [-0.1951,0.7845,-0.0732]
HAnimSegment1640 = x3d.HAnimSegment()
HAnimSegment1640.DEF = "STD_Segment_r_carpal_proximal_phalanx_4"
HAnimSegment1640.name = "r_carpal_proximal_phalanx_4"
Transform1641 = x3d.Transform()
Transform1641.translation = [-0.1951,0.7845,-0.0732]
Shape1642 = x3d.Shape()
Shape1642.USE = "HAnimJointShape"

Transform1641.children.append(Shape1642)

HAnimSegment1640.children.append(Transform1641)
Transform1643 = x3d.Transform()
Shape1644 = x3d.Shape()
LineSet1645 = x3d.LineSet()
LineSet1645.vertexCount = [2]
Coordinate1646 = x3d.Coordinate()

LineSet1645.coord = Coordinate1646
ColorRGBA1647 = x3d.ColorRGBA()
ColorRGBA1647.USE = "HAnimSegmentLineColorRGBA"

LineSet1645.color = ColorRGBA1647

Shape1644.geometry = LineSet1645

Transform1643.children.append(Shape1644)

HAnimSegment1640.children.append(Transform1643)

HAnimJoint1639.children.append(HAnimSegment1640)
HAnimJoint1648 = x3d.HAnimJoint()
HAnimJoint1648.DEF = "STD_Joint_r_carpal_proximal_interphalangeal_4"
HAnimJoint1648.name = "r_carpal_proximal_interphalangeal_4"
HAnimJoint1648.center = [-0.1920,0.7318,-0.0716]
HAnimSegment1649 = x3d.HAnimSegment()
HAnimSegment1649.DEF = "STD_Segment_r_carpal_middle_phalanx_4"
HAnimSegment1649.name = "r_carpal_middle_phalanx_4"
Transform1650 = x3d.Transform()
Transform1650.translation = [-0.1920,0.7318,-0.0716]
Shape1651 = x3d.Shape()
Shape1651.USE = "HAnimJointShape"

Transform1650.children.append(Shape1651)

HAnimSegment1649.children.append(Transform1650)
Transform1652 = x3d.Transform()
Shape1653 = x3d.Shape()
LineSet1654 = x3d.LineSet()
LineSet1654.vertexCount = [2]
Coordinate1655 = x3d.Coordinate()

LineSet1654.coord = Coordinate1655
ColorRGBA1656 = x3d.ColorRGBA()
ColorRGBA1656.USE = "HAnimSegmentLineColorRGBA"

LineSet1654.color = ColorRGBA1656

Shape1653.geometry = LineSet1654

Transform1652.children.append(Shape1653)

HAnimSegment1649.children.append(Transform1652)

HAnimJoint1648.children.append(HAnimSegment1649)
HAnimJoint1657 = x3d.HAnimJoint()
HAnimJoint1657.DEF = "STD_Joint_r_carpal_distal_interphalangeal_4"
HAnimJoint1657.name = "r_carpal_distal_interphalangeal_4"
HAnimJoint1657.center = [-0.1908,0.7077,-0.0706]
HAnimSegment1658 = x3d.HAnimSegment()
HAnimSegment1658.DEF = "STD_Segment_r_carpal_distal_phalanx_4"
HAnimSegment1658.name = "r_carpal_distal_phalanx_4"
Transform1659 = x3d.Transform()
Transform1659.translation = [-0.1908,0.7077,-0.0706]
Shape1660 = x3d.Shape()
Shape1660.USE = "HAnimJointShape"

Transform1659.children.append(Shape1660)

HAnimSegment1658.children.append(Transform1659)
Transform1661 = x3d.Transform()
Shape1662 = x3d.Shape()
LineSet1663 = x3d.LineSet()
LineSet1663.vertexCount = [2]
Coordinate1664 = x3d.Coordinate()

LineSet1663.coord = Coordinate1664
ColorRGBA1665 = x3d.ColorRGBA()
ColorRGBA1665.USE = "HAnimSegmentLineColorRGBA"

LineSet1663.color = ColorRGBA1665

Shape1662.geometry = LineSet1663

Transform1661.children.append(Shape1662)

HAnimSegment1658.children.append(Transform1661)
HAnimSite1666 = x3d.HAnimSite()
HAnimSite1666.DEF = "STD_Site_r_carpal_distal_phalanx_4_tip"
HAnimSite1666.name = "r_carpal_distal_phalanx_4_tip"
TouchSensor1667 = x3d.TouchSensor()
TouchSensor1667.description = "HAnimSite r_carpal_distal_phalanx_4_tip"

HAnimSite1666.children.append(TouchSensor1667)
Shape1668 = x3d.Shape()
Shape1668.USE = "HAnimSiteShape"

HAnimSite1666.children.append(Shape1668)

HAnimSegment1658.children.append(HAnimSite1666)

HAnimJoint1657.children.append(HAnimSegment1658)

HAnimJoint1648.children.append(HAnimJoint1657)

HAnimJoint1639.children.append(HAnimJoint1648)

HAnimJoint1630.children.append(HAnimJoint1639)

HAnimJoint1621.children.append(HAnimJoint1630)
HAnimJoint1669 = x3d.HAnimJoint()
HAnimJoint1669.DEF = "STD_Joint_r_carpometacarpal_5"
HAnimJoint1669.name = "r_carpometacarpal_5"
HAnimJoint1669.center = [-0.1926,0.8096,-0.0975]
HAnimSegment1670 = x3d.HAnimSegment()
HAnimSegment1670.DEF = "STD_Segment_r_metacarpal_5"
HAnimSegment1670.name = "r_metacarpal_5"
Transform1671 = x3d.Transform()
Transform1671.translation = [-0.1926,0.8096,-0.0975]
Shape1672 = x3d.Shape()
Shape1672.USE = "HAnimJointShape"

Transform1671.children.append(Shape1672)

HAnimSegment1670.children.append(Transform1671)
Transform1673 = x3d.Transform()
Shape1674 = x3d.Shape()
LineSet1675 = x3d.LineSet()
LineSet1675.vertexCount = [2]
Coordinate1676 = x3d.Coordinate()

LineSet1675.coord = Coordinate1676
ColorRGBA1677 = x3d.ColorRGBA()
ColorRGBA1677.USE = "HAnimSegmentLineColorRGBA"

LineSet1675.color = ColorRGBA1677

Shape1674.geometry = LineSet1675

Transform1673.children.append(Shape1674)

HAnimSegment1670.children.append(Transform1673)
HAnimSite1678 = x3d.HAnimSite()
HAnimSite1678.DEF = "STD_Site_r_metacarpal_phalanx_5_pt"
HAnimSite1678.name = "r_metacarpal_phalanx_5_pt"
HAnimSite1678.translation = [-0.1929,0.7890,-0.1064]
TouchSensor1679 = x3d.TouchSensor()
TouchSensor1679.description = "HAnimSite r_metacarpal_phalanx_5_pt"

HAnimSite1678.children.append(TouchSensor1679)
Shape1680 = x3d.Shape()
Shape1680.USE = "HAnimSiteShape"

HAnimSite1678.children.append(Shape1680)

HAnimSegment1670.children.append(HAnimSite1678)

HAnimJoint1669.children.append(HAnimSegment1670)
HAnimJoint1681 = x3d.HAnimJoint()
HAnimJoint1681.DEF = "STD_Joint_r_metacarpophalangeal_5"
HAnimJoint1681.name = "r_metacarpophalangeal_5"
HAnimJoint1681.center = [-0.1926,0.7896,-0.0975]
HAnimSegment1682 = x3d.HAnimSegment()
HAnimSegment1682.DEF = "STD_Segment_r_carpal_proximal_phalanx_5"
HAnimSegment1682.name = "r_carpal_proximal_phalanx_5"
Transform1683 = x3d.Transform()
Transform1683.translation = [-0.1926,0.7896,-0.0975]
Shape1684 = x3d.Shape()
Shape1684.USE = "HAnimJointShape"

Transform1683.children.append(Shape1684)

HAnimSegment1682.children.append(Transform1683)
Transform1685 = x3d.Transform()
Shape1686 = x3d.Shape()
LineSet1687 = x3d.LineSet()
LineSet1687.vertexCount = [2]
Coordinate1688 = x3d.Coordinate()

LineSet1687.coord = Coordinate1688
ColorRGBA1689 = x3d.ColorRGBA()
ColorRGBA1689.USE = "HAnimSegmentLineColorRGBA"

LineSet1687.color = ColorRGBA1689

Shape1686.geometry = LineSet1687

Transform1685.children.append(Shape1686)

HAnimSegment1682.children.append(Transform1685)

HAnimJoint1681.children.append(HAnimSegment1682)
HAnimJoint1690 = x3d.HAnimJoint()
HAnimJoint1690.DEF = "STD_Joint_r_carpal_proximal_interphalangeal_5"
HAnimJoint1690.name = "r_carpal_proximal_interphalangeal_5"
HAnimJoint1690.center = [-0.1902,0.7483,-0.0963]
HAnimSegment1691 = x3d.HAnimSegment()
HAnimSegment1691.DEF = "STD_Segment_r_carpal_middle_phalanx_5"
HAnimSegment1691.name = "r_carpal_middle_phalanx_5"
Transform1692 = x3d.Transform()
Transform1692.translation = [-0.1902,0.7483,-0.0963]
Shape1693 = x3d.Shape()
Shape1693.USE = "HAnimJointShape"

Transform1692.children.append(Shape1693)

HAnimSegment1691.children.append(Transform1692)
Transform1694 = x3d.Transform()
Shape1695 = x3d.Shape()
LineSet1696 = x3d.LineSet()
LineSet1696.vertexCount = [2]
Coordinate1697 = x3d.Coordinate()

LineSet1696.coord = Coordinate1697
ColorRGBA1698 = x3d.ColorRGBA()
ColorRGBA1698.USE = "HAnimSegmentLineColorRGBA"

LineSet1696.color = ColorRGBA1698

Shape1695.geometry = LineSet1696

Transform1694.children.append(Shape1695)

HAnimSegment1691.children.append(Transform1694)

HAnimJoint1690.children.append(HAnimSegment1691)
HAnimJoint1699 = x3d.HAnimJoint()
HAnimJoint1699.DEF = "STD_Joint_r_carpal_distal_interphalangeal_5"
HAnimJoint1699.name = "r_carpal_distal_interphalangeal_5"
HAnimJoint1699.center = [-0.1908,0.7540,-0.0960]
HAnimSegment1700 = x3d.HAnimSegment()
HAnimSegment1700.DEF = "STD_Segment_r_carpal_distal_phalanx_5"
HAnimSegment1700.name = "r_carpal_distal_phalanx_5"
Transform1701 = x3d.Transform()
Transform1701.translation = [-0.1908,0.7540,-0.0960]
Shape1702 = x3d.Shape()
Shape1702.USE = "HAnimJointShape"

Transform1701.children.append(Shape1702)

HAnimSegment1700.children.append(Transform1701)
Transform1703 = x3d.Transform()
Shape1704 = x3d.Shape()
LineSet1705 = x3d.LineSet()
LineSet1705.vertexCount = [2]
Coordinate1706 = x3d.Coordinate()

LineSet1705.coord = Coordinate1706
ColorRGBA1707 = x3d.ColorRGBA()
ColorRGBA1707.USE = "HAnimSegmentLineColorRGBA"

LineSet1705.color = ColorRGBA1707

Shape1704.geometry = LineSet1705

Transform1703.children.append(Shape1704)

HAnimSegment1700.children.append(Transform1703)
HAnimSite1708 = x3d.HAnimSite()
HAnimSite1708.DEF = "STD_Site_r_carpal_distal_phalanx_5_tip"
HAnimSite1708.name = "r_carpal_distal_phalanx_5_tip"
TouchSensor1709 = x3d.TouchSensor()
TouchSensor1709.description = "HAnimSite r_carpal_distal_phalanx_5_tip"

HAnimSite1708.children.append(TouchSensor1709)
Shape1710 = x3d.Shape()
Shape1710.USE = "HAnimSiteShape"

HAnimSite1708.children.append(Shape1710)

HAnimSegment1700.children.append(HAnimSite1708)

HAnimJoint1699.children.append(HAnimSegment1700)

HAnimJoint1690.children.append(HAnimJoint1699)

HAnimJoint1681.children.append(HAnimJoint1690)

HAnimJoint1669.children.append(HAnimJoint1681)

HAnimJoint1621.children.append(HAnimJoint1669)

HAnimJoint1465.children.append(HAnimJoint1621)

HAnimJoint1444.children.append(HAnimJoint1465)

HAnimJoint1429.children.append(HAnimJoint1444)

HAnimJoint1420.children.append(HAnimJoint1429)

HAnimJoint1396.children.append(HAnimJoint1420)

HAnimJoint877.children.append(HAnimJoint1396)

HAnimJoint868.children.append(HAnimJoint877)

HAnimJoint859.children.append(HAnimJoint868)

HAnimJoint850.children.append(HAnimJoint859)

HAnimJoint838.children.append(HAnimJoint850)

HAnimJoint817.children.append(HAnimJoint838)

HAnimJoint808.children.append(HAnimJoint817)

HAnimJoint799.children.append(HAnimJoint808)

HAnimJoint784.children.append(HAnimJoint799)

HAnimJoint772.children.append(HAnimJoint784)

HAnimJoint763.children.append(HAnimJoint772)

HAnimJoint754.children.append(HAnimJoint763)

HAnimJoint745.children.append(HAnimJoint754)

HAnimJoint727.children.append(HAnimJoint745)

HAnimJoint718.children.append(HAnimJoint727)

HAnimJoint709.children.append(HAnimJoint718)

HAnimJoint691.children.append(HAnimJoint709)

HAnimJoint43.children.append(HAnimJoint691)

HAnimHumanoid42.joints.append(HAnimJoint43)
HAnimJoint1711 = x3d.HAnimJoint()
HAnimJoint1711.USE = "STD_Joint_humanoid_root"

HAnimHumanoid42.joints.append(HAnimJoint1711)
HAnimSegment1712 = x3d.HAnimSegment()
HAnimSegment1712.USE = "STD_Segment_sacrum"

HAnimHumanoid42.segments.append(HAnimSegment1712)
HAnimJoint1713 = x3d.HAnimJoint()
HAnimJoint1713.USE = "STD_Joint_sacroiliac"

HAnimHumanoid42.joints.append(HAnimJoint1713)
HAnimSite1714 = x3d.HAnimSite()
HAnimSite1714.USE = "STD_Site_buttocks_standing_wall_contact_point_pt"

HAnimHumanoid42.sites.append(HAnimSite1714)
HAnimSite1715 = x3d.HAnimSite()
HAnimSite1715.USE = "STD_Site_crotch_pt"

HAnimHumanoid42.sites.append(HAnimSite1715)
HAnimSite1716 = x3d.HAnimSite()
HAnimSite1716.USE = "STD_Site_l_asis_pt"

HAnimHumanoid42.sites.append(HAnimSite1716)
HAnimSite1717 = x3d.HAnimSite()
HAnimSite1717.USE = "STD_Site_l_iliocristale_pt"

HAnimHumanoid42.sites.append(HAnimSite1717)
HAnimSite1718 = x3d.HAnimSite()
HAnimSite1718.USE = "STD_Site_l_psis_pt"

HAnimHumanoid42.sites.append(HAnimSite1718)
HAnimSite1719 = x3d.HAnimSite()
HAnimSite1719.USE = "STD_Site_l_trochanterion_pt"

HAnimHumanoid42.sites.append(HAnimSite1719)
HAnimSite1720 = x3d.HAnimSite()
HAnimSite1720.USE = "STD_Site_r_asis_pt"

HAnimHumanoid42.sites.append(HAnimSite1720)
HAnimSite1721 = x3d.HAnimSite()
HAnimSite1721.USE = "STD_Site_r_iliocristale_pt"

HAnimHumanoid42.sites.append(HAnimSite1721)
HAnimSite1722 = x3d.HAnimSite()
HAnimSite1722.USE = "STD_Site_r_psis_pt"

HAnimHumanoid42.sites.append(HAnimSite1722)
HAnimSite1723 = x3d.HAnimSite()
HAnimSite1723.USE = "STD_Site_r_trochanterion_pt"

HAnimHumanoid42.sites.append(HAnimSite1723)
HAnimSegment1724 = x3d.HAnimSegment()
HAnimSegment1724.USE = "STD_Segment_pelvis"

HAnimHumanoid42.segments.append(HAnimSegment1724)
HAnimJoint1725 = x3d.HAnimJoint()
HAnimJoint1725.USE = "STD_Joint_l_hip"

HAnimHumanoid42.joints.append(HAnimJoint1725)
HAnimSite1726 = x3d.HAnimSite()
HAnimSite1726.USE = "STD_Site_l_femoral_lateral_epicondyles_pt"

HAnimHumanoid42.sites.append(HAnimSite1726)
HAnimSite1727 = x3d.HAnimSite()
HAnimSite1727.USE = "STD_Site_l_femoral_medial_epicondyles_pt"

HAnimHumanoid42.sites.append(HAnimSite1727)
HAnimSite1728 = x3d.HAnimSite()
HAnimSite1728.USE = "STD_Site_l_knee_crease_pt"

HAnimHumanoid42.sites.append(HAnimSite1728)
HAnimSite1729 = x3d.HAnimSite()
HAnimSite1729.USE = "STD_Site_l_suprapatella_pt"

HAnimHumanoid42.sites.append(HAnimSite1729)
HAnimSegment1730 = x3d.HAnimSegment()
HAnimSegment1730.USE = "STD_Segment_l_thigh"

HAnimHumanoid42.segments.append(HAnimSegment1730)
HAnimJoint1731 = x3d.HAnimJoint()
HAnimJoint1731.USE = "STD_Joint_l_knee"

HAnimHumanoid42.joints.append(HAnimJoint1731)
HAnimSite1732 = x3d.HAnimSite()
HAnimSite1732.USE = "STD_Site_l_lateral_malleolus_pt"

HAnimHumanoid42.sites.append(HAnimSite1732)
HAnimSite1733 = x3d.HAnimSite()
HAnimSite1733.USE = "STD_Site_l_medial_malleolus_pt"

HAnimHumanoid42.sites.append(HAnimSite1733)
HAnimSite1734 = x3d.HAnimSite()
HAnimSite1734.USE = "STD_Site_l_tibiale_pt"

HAnimHumanoid42.sites.append(HAnimSite1734)
HAnimSegment1735 = x3d.HAnimSegment()
HAnimSegment1735.USE = "STD_Segment_l_calf"

HAnimHumanoid42.segments.append(HAnimSegment1735)
HAnimJoint1736 = x3d.HAnimJoint()
HAnimJoint1736.USE = "STD_Joint_l_talocrural"

HAnimHumanoid42.joints.append(HAnimJoint1736)
HAnimSite1737 = x3d.HAnimSite()
HAnimSite1737.USE = "STD_Site_l_calcaneus_posterior_pt"

HAnimHumanoid42.sites.append(HAnimSite1737)
HAnimSite1738 = x3d.HAnimSite()
HAnimSite1738.USE = "STD_Site_l_sphyrion_pt"

HAnimHumanoid42.sites.append(HAnimSite1738)
HAnimSegment1739 = x3d.HAnimSegment()
HAnimSegment1739.USE = "STD_Segment_l_talus"

HAnimHumanoid42.segments.append(HAnimSegment1739)
HAnimJoint1740 = x3d.HAnimJoint()
HAnimJoint1740.USE = "STD_Joint_l_talocalcaneonavicular"

HAnimHumanoid42.joints.append(HAnimJoint1740)
HAnimSegment1741 = x3d.HAnimSegment()
HAnimSegment1741.USE = "STD_Segment_l_navicular"

HAnimHumanoid42.segments.append(HAnimSegment1741)
HAnimJoint1742 = x3d.HAnimJoint()
HAnimJoint1742.USE = "STD_Joint_l_cuneonavicular_1"

HAnimHumanoid42.joints.append(HAnimJoint1742)
HAnimSegment1743 = x3d.HAnimSegment()
HAnimSegment1743.USE = "STD_Segment_l_cuneiform_1"

HAnimHumanoid42.segments.append(HAnimSegment1743)
HAnimJoint1744 = x3d.HAnimJoint()
HAnimJoint1744.USE = "STD_Joint_l_tarsometatarsal_1"

HAnimHumanoid42.joints.append(HAnimJoint1744)
HAnimSegment1745 = x3d.HAnimSegment()
HAnimSegment1745.USE = "STD_Segment_l_metatarsal_1"

HAnimHumanoid42.segments.append(HAnimSegment1745)
HAnimJoint1746 = x3d.HAnimJoint()
HAnimJoint1746.USE = "STD_Joint_l_metatarsophalangeal_1"

HAnimHumanoid42.joints.append(HAnimJoint1746)
HAnimSite1747 = x3d.HAnimSite()
HAnimSite1747.USE = "STD_Site_l_metatarsal_phalanx_1_pt"

HAnimHumanoid42.sites.append(HAnimSite1747)
HAnimSegment1748 = x3d.HAnimSegment()
HAnimSegment1748.USE = "STD_Segment_l_tarsal_proximal_phalanx_1"

HAnimHumanoid42.segments.append(HAnimSegment1748)
HAnimJoint1749 = x3d.HAnimJoint()
HAnimJoint1749.USE = "STD_Joint_l_tarsal_interphalangeal_1"

HAnimHumanoid42.joints.append(HAnimJoint1749)
HAnimSite1750 = x3d.HAnimSite()
HAnimSite1750.USE = "STD_Site_l_tarsal_distal_phalanx_1_tip"

HAnimHumanoid42.sites.append(HAnimSite1750)
HAnimSegment1751 = x3d.HAnimSegment()
HAnimSegment1751.USE = "STD_Segment_l_tarsal_distal_phalanx_1"

HAnimHumanoid42.segments.append(HAnimSegment1751)
HAnimJoint1752 = x3d.HAnimJoint()
HAnimJoint1752.USE = "STD_Joint_l_cuneonavicular_2"

HAnimHumanoid42.joints.append(HAnimJoint1752)
HAnimSegment1753 = x3d.HAnimSegment()
HAnimSegment1753.USE = "STD_Segment_l_cuneiform_2"

HAnimHumanoid42.segments.append(HAnimSegment1753)
HAnimJoint1754 = x3d.HAnimJoint()
HAnimJoint1754.USE = "STD_Joint_l_tarsometatarsal_2"

HAnimHumanoid42.joints.append(HAnimJoint1754)
HAnimSegment1755 = x3d.HAnimSegment()
HAnimSegment1755.USE = "STD_Segment_l_metatarsal_2"

HAnimHumanoid42.segments.append(HAnimSegment1755)
HAnimJoint1756 = x3d.HAnimJoint()
HAnimJoint1756.USE = "STD_Joint_l_metatarsophalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint1756)
HAnimSegment1757 = x3d.HAnimSegment()
HAnimSegment1757.USE = "STD_Segment_l_tarsal_proximal_phalanx_2"

HAnimHumanoid42.segments.append(HAnimSegment1757)
HAnimJoint1758 = x3d.HAnimJoint()
HAnimJoint1758.USE = "STD_Joint_l_tarsal_proximal_interphalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint1758)
HAnimSegment1759 = x3d.HAnimSegment()
HAnimSegment1759.USE = "STD_Segment_l_tarsal_middle_phalanx_2"

HAnimHumanoid42.segments.append(HAnimSegment1759)
HAnimJoint1760 = x3d.HAnimJoint()
HAnimJoint1760.USE = "STD_Joint_l_tarsal_distal_interphalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint1760)
HAnimSite1761 = x3d.HAnimSite()
HAnimSite1761.USE = "STD_Site_l_tarsal_distal_phalanx_2_tip"

HAnimHumanoid42.sites.append(HAnimSite1761)
HAnimSegment1762 = x3d.HAnimSegment()
HAnimSegment1762.USE = "STD_Segment_l_tarsal_distal_phalanx_2"

HAnimHumanoid42.segments.append(HAnimSegment1762)
HAnimJoint1763 = x3d.HAnimJoint()
HAnimJoint1763.USE = "STD_Joint_l_cuneonavicular_3"

HAnimHumanoid42.joints.append(HAnimJoint1763)
HAnimSegment1764 = x3d.HAnimSegment()
HAnimSegment1764.USE = "STD_Segment_l_cuneiform_3"

HAnimHumanoid42.segments.append(HAnimSegment1764)
HAnimJoint1765 = x3d.HAnimJoint()
HAnimJoint1765.USE = "STD_Joint_l_tarsometatarsal_3 "

HAnimHumanoid42.joints.append(HAnimJoint1765)
HAnimSegment1766 = x3d.HAnimSegment()
HAnimSegment1766.USE = "STD_Segment_l_metatarsal_3"

HAnimHumanoid42.segments.append(HAnimSegment1766)
HAnimJoint1767 = x3d.HAnimJoint()
HAnimJoint1767.USE = "STD_Joint_l_metatarsophalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint1767)
HAnimSegment1768 = x3d.HAnimSegment()
HAnimSegment1768.USE = "STD_Segment_l_tarsal_proximal_phalanx_3"

HAnimHumanoid42.segments.append(HAnimSegment1768)
HAnimJoint1769 = x3d.HAnimJoint()
HAnimJoint1769.USE = "STD_Joint_l_tarsal_proximal_interphalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint1769)
HAnimSegment1770 = x3d.HAnimSegment()
HAnimSegment1770.USE = "STD_Segment_l_tarsal_middle_phalanx_3"

HAnimHumanoid42.segments.append(HAnimSegment1770)
HAnimJoint1771 = x3d.HAnimJoint()
HAnimJoint1771.USE = "STD_Joint_l_tarsal_distal_interphalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint1771)
HAnimSite1772 = x3d.HAnimSite()
HAnimSite1772.USE = "STD_Site_l_tarsal_distal_phalanx_3_tip"

HAnimHumanoid42.sites.append(HAnimSite1772)
HAnimSegment1773 = x3d.HAnimSegment()
HAnimSegment1773.USE = "STD_Segment_l_tarsal_distal_phalanx_3"

HAnimHumanoid42.segments.append(HAnimSegment1773)
HAnimJoint1774 = x3d.HAnimJoint()
HAnimJoint1774.USE = "STD_Joint_l_calcaneocuboid"

HAnimHumanoid42.joints.append(HAnimJoint1774)
HAnimSegment1775 = x3d.HAnimSegment()
HAnimSegment1775.USE = "STD_Segment_l_calcaneus"

HAnimHumanoid42.segments.append(HAnimSegment1775)
HAnimJoint1776 = x3d.HAnimJoint()
HAnimJoint1776.USE = "STD_Joint_l_transversetarsal"

HAnimHumanoid42.joints.append(HAnimJoint1776)
HAnimSegment1777 = x3d.HAnimSegment()
HAnimSegment1777.USE = "STD_Segment_l_cuboid"

HAnimHumanoid42.segments.append(HAnimSegment1777)
HAnimJoint1778 = x3d.HAnimJoint()
HAnimJoint1778.USE = "STD_Joint_l_tarsometatarsal_4"

HAnimHumanoid42.joints.append(HAnimJoint1778)
HAnimSegment1779 = x3d.HAnimSegment()
HAnimSegment1779.USE = "STD_Segment_l_metatarsal_4"

HAnimHumanoid42.segments.append(HAnimSegment1779)
HAnimJoint1780 = x3d.HAnimJoint()
HAnimJoint1780.USE = "STD_Joint_l_metatarsophalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint1780)
HAnimSegment1781 = x3d.HAnimSegment()
HAnimSegment1781.USE = "STD_Segment_l_tarsal_proximal_phalanx_4"

HAnimHumanoid42.segments.append(HAnimSegment1781)
HAnimJoint1782 = x3d.HAnimJoint()
HAnimJoint1782.USE = "STD_Joint_l_tarsal_proximal_interphalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint1782)
HAnimSegment1783 = x3d.HAnimSegment()
HAnimSegment1783.USE = "STD_Segment_l_tarsal_middle_phalanx_4"

HAnimHumanoid42.segments.append(HAnimSegment1783)
HAnimJoint1784 = x3d.HAnimJoint()
HAnimJoint1784.USE = "STD_Joint_l_tarsal_distal_interphalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint1784)
HAnimSite1785 = x3d.HAnimSite()
HAnimSite1785.USE = "STD_Site_l_tarsal_distal_phalanx_4_tip"

HAnimHumanoid42.sites.append(HAnimSite1785)
HAnimSegment1786 = x3d.HAnimSegment()
HAnimSegment1786.USE = "STD_Segment_l_tarsal_distal_phalanx_4"

HAnimHumanoid42.segments.append(HAnimSegment1786)
HAnimJoint1787 = x3d.HAnimJoint()
HAnimJoint1787.USE = "STD_Joint_l_tarsometatarsal_5"

HAnimHumanoid42.joints.append(HAnimJoint1787)
HAnimSegment1788 = x3d.HAnimSegment()
HAnimSegment1788.USE = "STD_Segment_l_metatarsal_5"

HAnimHumanoid42.segments.append(HAnimSegment1788)
HAnimJoint1789 = x3d.HAnimJoint()
HAnimJoint1789.USE = "STD_Joint_l_metatarsophalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint1789)
HAnimSite1790 = x3d.HAnimSite()
HAnimSite1790.USE = "STD_Site_l_metatarsal_phalanx_5_pt"

HAnimHumanoid42.sites.append(HAnimSite1790)
HAnimSegment1791 = x3d.HAnimSegment()
HAnimSegment1791.USE = "STD_Segment_l_tarsal_proximal_phalanx_5"

HAnimHumanoid42.segments.append(HAnimSegment1791)
HAnimJoint1792 = x3d.HAnimJoint()
HAnimJoint1792.USE = "STD_Joint_l_tarsal_proximal_interphalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint1792)
HAnimSegment1793 = x3d.HAnimSegment()
HAnimSegment1793.USE = "STD_Segment_l_tarsal_middle_phalanx_5"

HAnimHumanoid42.segments.append(HAnimSegment1793)
HAnimJoint1794 = x3d.HAnimJoint()
HAnimJoint1794.USE = "STD_Joint_l_tarsal_distal_interphalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint1794)
HAnimSite1795 = x3d.HAnimSite()
HAnimSite1795.USE = "STD_Site_l_tarsal_distal_phalanx_5_tip"

HAnimHumanoid42.sites.append(HAnimSite1795)
HAnimSegment1796 = x3d.HAnimSegment()
HAnimSegment1796.USE = "STD_Segment_l_tarsal_distal_phalanx_5"

HAnimHumanoid42.segments.append(HAnimSegment1796)
HAnimJoint1797 = x3d.HAnimJoint()
HAnimJoint1797.USE = "STD_Joint_r_hip"

HAnimHumanoid42.joints.append(HAnimJoint1797)
HAnimSite1798 = x3d.HAnimSite()
HAnimSite1798.USE = "STD_Site_r_femoral_lateral_epicondyles_pt"

HAnimHumanoid42.sites.append(HAnimSite1798)
HAnimSite1799 = x3d.HAnimSite()
HAnimSite1799.USE = "STD_Site_r_femoral_medial_epicondyles_pt"

HAnimHumanoid42.sites.append(HAnimSite1799)
HAnimSite1800 = x3d.HAnimSite()
HAnimSite1800.USE = "STD_Site_r_knee_crease_pt"

HAnimHumanoid42.sites.append(HAnimSite1800)
HAnimSite1801 = x3d.HAnimSite()
HAnimSite1801.USE = "STD_Site_r_suprapatella_pt"

HAnimHumanoid42.sites.append(HAnimSite1801)
HAnimSegment1802 = x3d.HAnimSegment()
HAnimSegment1802.USE = "STD_Segment_r_thigh"

HAnimHumanoid42.segments.append(HAnimSegment1802)
HAnimJoint1803 = x3d.HAnimJoint()
HAnimJoint1803.USE = "STD_Joint_r_knee"

HAnimHumanoid42.joints.append(HAnimJoint1803)
HAnimSite1804 = x3d.HAnimSite()
HAnimSite1804.USE = "STD_Site_r_lateral_malleolus_pt"

HAnimHumanoid42.sites.append(HAnimSite1804)
HAnimSite1805 = x3d.HAnimSite()
HAnimSite1805.USE = "STD_Site_r_medial_malleolus_pt"

HAnimHumanoid42.sites.append(HAnimSite1805)
HAnimSite1806 = x3d.HAnimSite()
HAnimSite1806.USE = "STD_Site_r_tibiale_pt"

HAnimHumanoid42.sites.append(HAnimSite1806)
HAnimSegment1807 = x3d.HAnimSegment()
HAnimSegment1807.USE = "STD_Segment_r_calf"

HAnimHumanoid42.segments.append(HAnimSegment1807)
HAnimJoint1808 = x3d.HAnimJoint()
HAnimJoint1808.USE = "STD_Joint_r_talocrural"

HAnimHumanoid42.joints.append(HAnimJoint1808)
HAnimSite1809 = x3d.HAnimSite()
HAnimSite1809.USE = "STD_Site_r_calcaneus_posterior_pt"

HAnimHumanoid42.sites.append(HAnimSite1809)
HAnimSite1810 = x3d.HAnimSite()
HAnimSite1810.USE = "STD_Site_r_sphyrion_pt"

HAnimHumanoid42.sites.append(HAnimSite1810)
HAnimSegment1811 = x3d.HAnimSegment()
HAnimSegment1811.USE = "STD_Segment_r_talus"

HAnimHumanoid42.segments.append(HAnimSegment1811)
HAnimJoint1812 = x3d.HAnimJoint()
HAnimJoint1812.USE = "STD_Joint_r_talocalcaneonavicular"

HAnimHumanoid42.joints.append(HAnimJoint1812)
HAnimSegment1813 = x3d.HAnimSegment()
HAnimSegment1813.USE = "STD_Segment_r_navicular"

HAnimHumanoid42.segments.append(HAnimSegment1813)
HAnimJoint1814 = x3d.HAnimJoint()
HAnimJoint1814.USE = "STD_Joint_r_cuneonavicular_1"

HAnimHumanoid42.joints.append(HAnimJoint1814)
HAnimSegment1815 = x3d.HAnimSegment()
HAnimSegment1815.USE = "STD_Segment_r_cuneiform_1"

HAnimHumanoid42.segments.append(HAnimSegment1815)
HAnimJoint1816 = x3d.HAnimJoint()
HAnimJoint1816.USE = "STD_Joint_r_tarsometatarsal_1"

HAnimHumanoid42.joints.append(HAnimJoint1816)
HAnimSegment1817 = x3d.HAnimSegment()
HAnimSegment1817.USE = "STD_Segment_r_metatarsal_1"

HAnimHumanoid42.segments.append(HAnimSegment1817)
HAnimJoint1818 = x3d.HAnimJoint()
HAnimJoint1818.USE = "STD_Joint_r_metatarsophalangeal_1"

HAnimHumanoid42.joints.append(HAnimJoint1818)
HAnimSite1819 = x3d.HAnimSite()
HAnimSite1819.USE = "STD_Site_r_metatarsal_phalanx_1_pt"

HAnimHumanoid42.sites.append(HAnimSite1819)
HAnimSegment1820 = x3d.HAnimSegment()
HAnimSegment1820.USE = "STD_Segment_r_tarsal_proximal_phalanx_1"

HAnimHumanoid42.segments.append(HAnimSegment1820)
HAnimJoint1821 = x3d.HAnimJoint()
HAnimJoint1821.USE = "STD_Joint_r_tarsal_interphalangeal_1"

HAnimHumanoid42.joints.append(HAnimJoint1821)
HAnimSite1822 = x3d.HAnimSite()
HAnimSite1822.USE = "STD_Site_r_tarsal_distal_phalanx_1_tip"

HAnimHumanoid42.sites.append(HAnimSite1822)
HAnimSegment1823 = x3d.HAnimSegment()
HAnimSegment1823.USE = "STD_Segment_r_tarsal_distal_phalanx_1"

HAnimHumanoid42.segments.append(HAnimSegment1823)
HAnimJoint1824 = x3d.HAnimJoint()
HAnimJoint1824.USE = "STD_Joint_r_cuneonavicular_2"

HAnimHumanoid42.joints.append(HAnimJoint1824)
HAnimSegment1825 = x3d.HAnimSegment()
HAnimSegment1825.USE = "STD_Segment_r_cuneiform_2"

HAnimHumanoid42.segments.append(HAnimSegment1825)
HAnimJoint1826 = x3d.HAnimJoint()
HAnimJoint1826.USE = "STD_Joint_r_tarsometatarsal_2"

HAnimHumanoid42.joints.append(HAnimJoint1826)
HAnimSegment1827 = x3d.HAnimSegment()
HAnimSegment1827.USE = "STD_Segment_r_metatarsal_2"

HAnimHumanoid42.segments.append(HAnimSegment1827)
HAnimJoint1828 = x3d.HAnimJoint()
HAnimJoint1828.USE = "STD_Joint_r_metatarsophalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint1828)
HAnimSegment1829 = x3d.HAnimSegment()
HAnimSegment1829.USE = "STD_Segment_r_tarsal_proximal_phalanx_2"

HAnimHumanoid42.segments.append(HAnimSegment1829)
HAnimJoint1830 = x3d.HAnimJoint()
HAnimJoint1830.USE = "STD_Joint_r_tarsal_proximal_interphalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint1830)
HAnimSegment1831 = x3d.HAnimSegment()
HAnimSegment1831.USE = "STD_Segment_r_tarsal_middle_phalanx_2"

HAnimHumanoid42.segments.append(HAnimSegment1831)
HAnimJoint1832 = x3d.HAnimJoint()
HAnimJoint1832.USE = "STD_Joint_r_tarsal_distal_interphalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint1832)
HAnimSite1833 = x3d.HAnimSite()
HAnimSite1833.USE = "STD_Site_r_tarsal_distal_phalanx_2_tip"

HAnimHumanoid42.sites.append(HAnimSite1833)
HAnimSegment1834 = x3d.HAnimSegment()
HAnimSegment1834.USE = "STD_Segment_r_tarsal_distal_phalanx_2"

HAnimHumanoid42.segments.append(HAnimSegment1834)
HAnimJoint1835 = x3d.HAnimJoint()
HAnimJoint1835.USE = "STD_Joint_r_cuneonavicular_3"

HAnimHumanoid42.joints.append(HAnimJoint1835)
HAnimSegment1836 = x3d.HAnimSegment()
HAnimSegment1836.USE = "STD_Segment_r_cuneiform_3"

HAnimHumanoid42.segments.append(HAnimSegment1836)
HAnimJoint1837 = x3d.HAnimJoint()
HAnimJoint1837.USE = "STD_Joint_r_tarsometatarsal_3 "

HAnimHumanoid42.joints.append(HAnimJoint1837)
HAnimSegment1838 = x3d.HAnimSegment()
HAnimSegment1838.USE = "STD_Segment_r_metatarsal_3"

HAnimHumanoid42.segments.append(HAnimSegment1838)
HAnimJoint1839 = x3d.HAnimJoint()
HAnimJoint1839.USE = "STD_Joint_r_metatarsophalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint1839)
HAnimSegment1840 = x3d.HAnimSegment()
HAnimSegment1840.USE = "STD_Segment_r_tarsal_proximal_phalanx_3"

HAnimHumanoid42.segments.append(HAnimSegment1840)
HAnimJoint1841 = x3d.HAnimJoint()
HAnimJoint1841.USE = "STD_Joint_r_tarsal_proximal_interphalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint1841)
HAnimSegment1842 = x3d.HAnimSegment()
HAnimSegment1842.USE = "STD_Segment_r_tarsal_middle_phalanx_3"

HAnimHumanoid42.segments.append(HAnimSegment1842)
HAnimJoint1843 = x3d.HAnimJoint()
HAnimJoint1843.USE = "STD_Joint_r_tarsal_distal_interphalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint1843)
HAnimSite1844 = x3d.HAnimSite()
HAnimSite1844.USE = "STD_Site_r_tarsal_distal_phalanx_3_tip"

HAnimHumanoid42.sites.append(HAnimSite1844)
HAnimSegment1845 = x3d.HAnimSegment()
HAnimSegment1845.USE = "STD_Segment_r_tarsal_distal_phalanx_3"

HAnimHumanoid42.segments.append(HAnimSegment1845)
HAnimJoint1846 = x3d.HAnimJoint()
HAnimJoint1846.USE = "STD_Joint_r_calcaneocuboid"

HAnimHumanoid42.joints.append(HAnimJoint1846)
HAnimSegment1847 = x3d.HAnimSegment()
HAnimSegment1847.USE = "STD_Segment_r_calcaneus"

HAnimHumanoid42.segments.append(HAnimSegment1847)
HAnimJoint1848 = x3d.HAnimJoint()
HAnimJoint1848.USE = "STD_Joint_r_transversetarsal"

HAnimHumanoid42.joints.append(HAnimJoint1848)
HAnimSegment1849 = x3d.HAnimSegment()
HAnimSegment1849.USE = "STD_Segment_r_cuboid"

HAnimHumanoid42.segments.append(HAnimSegment1849)
HAnimJoint1850 = x3d.HAnimJoint()
HAnimJoint1850.USE = "STD_Joint_r_tarsometatarsal_4"

HAnimHumanoid42.joints.append(HAnimJoint1850)
HAnimSegment1851 = x3d.HAnimSegment()
HAnimSegment1851.USE = "STD_Segment_r_metatarsal_4"

HAnimHumanoid42.segments.append(HAnimSegment1851)
HAnimJoint1852 = x3d.HAnimJoint()
HAnimJoint1852.USE = "STD_Joint_r_metatarsophalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint1852)
HAnimSegment1853 = x3d.HAnimSegment()
HAnimSegment1853.USE = "STD_Segment_r_tarsal_proximal_phalanx_4"

HAnimHumanoid42.segments.append(HAnimSegment1853)
HAnimJoint1854 = x3d.HAnimJoint()
HAnimJoint1854.USE = "STD_Joint_r_tarsal_proximal_interphalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint1854)
HAnimSegment1855 = x3d.HAnimSegment()
HAnimSegment1855.USE = "STD_Segment_r_tarsal_middle_phalanx_4"

HAnimHumanoid42.segments.append(HAnimSegment1855)
HAnimJoint1856 = x3d.HAnimJoint()
HAnimJoint1856.USE = "STD_Joint_r_tarsal_distal_interphalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint1856)
HAnimSite1857 = x3d.HAnimSite()
HAnimSite1857.USE = "STD_Site_r_tarsal_distal_phalanx_4_tip"

HAnimHumanoid42.sites.append(HAnimSite1857)
HAnimSegment1858 = x3d.HAnimSegment()
HAnimSegment1858.USE = "STD_Segment_r_tarsal_distal_phalanx_4"

HAnimHumanoid42.segments.append(HAnimSegment1858)
HAnimJoint1859 = x3d.HAnimJoint()
HAnimJoint1859.USE = "STD_Joint_r_tarsometatarsal_5"

HAnimHumanoid42.joints.append(HAnimJoint1859)
HAnimSegment1860 = x3d.HAnimSegment()
HAnimSegment1860.USE = "STD_Segment_r_metatarsal_5"

HAnimHumanoid42.segments.append(HAnimSegment1860)
HAnimJoint1861 = x3d.HAnimJoint()
HAnimJoint1861.USE = "STD_Joint_r_metatarsophalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint1861)
HAnimSite1862 = x3d.HAnimSite()
HAnimSite1862.USE = "STD_Site_r_metatarsal_phalanx_5_pt"

HAnimHumanoid42.sites.append(HAnimSite1862)
HAnimSegment1863 = x3d.HAnimSegment()
HAnimSegment1863.USE = "STD_Segment_r_tarsal_proximal_phalanx_5"

HAnimHumanoid42.segments.append(HAnimSegment1863)
HAnimJoint1864 = x3d.HAnimJoint()
HAnimJoint1864.USE = "STD_Joint_r_tarsal_proximal_interphalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint1864)
HAnimSegment1865 = x3d.HAnimSegment()
HAnimSegment1865.USE = "STD_Segment_r_tarsal_middle_phalanx_5"

HAnimHumanoid42.segments.append(HAnimSegment1865)
HAnimJoint1866 = x3d.HAnimJoint()
HAnimJoint1866.USE = "STD_Joint_r_tarsal_distal_interphalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint1866)
HAnimSite1867 = x3d.HAnimSite()
HAnimSite1867.USE = "STD_Site_r_tarsal_distal_phalanx_5_tip"

HAnimHumanoid42.sites.append(HAnimSite1867)
HAnimSegment1868 = x3d.HAnimSegment()
HAnimSegment1868.USE = "STD_Segment_r_tarsal_distal_phalanx_5"

HAnimHumanoid42.segments.append(HAnimSegment1868)
HAnimJoint1869 = x3d.HAnimJoint()
HAnimJoint1869.USE = "STD_Joint_vl5"

HAnimHumanoid42.joints.append(HAnimJoint1869)
HAnimSite1870 = x3d.HAnimSite()
HAnimSite1870.USE = "STD_Site_navel_pt"

HAnimHumanoid42.sites.append(HAnimSite1870)
HAnimSite1871 = x3d.HAnimSite()
HAnimSite1871.USE = "STD_Site_waist_preferred_anterior_pt"

HAnimHumanoid42.sites.append(HAnimSite1871)
HAnimSite1872 = x3d.HAnimSite()
HAnimSite1872.USE = "STD_Site_waist_preferred_posterior_pt"

HAnimHumanoid42.sites.append(HAnimSite1872)
HAnimSegment1873 = x3d.HAnimSegment()
HAnimSegment1873.USE = "STD_Segment_l5"

HAnimHumanoid42.segments.append(HAnimSegment1873)
HAnimJoint1874 = x3d.HAnimJoint()
HAnimJoint1874.USE = "STD_Joint_vl4"

HAnimHumanoid42.joints.append(HAnimJoint1874)
HAnimSegment1875 = x3d.HAnimSegment()
HAnimSegment1875.USE = "STD_Segment_l4"

HAnimHumanoid42.segments.append(HAnimSegment1875)
HAnimJoint1876 = x3d.HAnimJoint()
HAnimJoint1876.USE = "STD_Joint_vl3"

HAnimHumanoid42.joints.append(HAnimJoint1876)
HAnimSegment1877 = x3d.HAnimSegment()
HAnimSegment1877.USE = "STD_Segment_l3"

HAnimHumanoid42.segments.append(HAnimSegment1877)
HAnimJoint1878 = x3d.HAnimJoint()
HAnimJoint1878.USE = "STD_Joint_vl2"

HAnimHumanoid42.joints.append(HAnimJoint1878)
HAnimSite1879 = x3d.HAnimSite()
HAnimSite1879.USE = "STD_Site_l_rib10_pt"

HAnimHumanoid42.sites.append(HAnimSite1879)
HAnimSite1880 = x3d.HAnimSite()
HAnimSite1880.USE = "STD_Site_r_rib10_pt"

HAnimHumanoid42.sites.append(HAnimSite1880)
HAnimSite1881 = x3d.HAnimSite()
HAnimSite1881.USE = "STD_Site_spine_2_middle_back_pt"

HAnimHumanoid42.sites.append(HAnimSite1881)
HAnimSegment1882 = x3d.HAnimSegment()
HAnimSegment1882.USE = "STD_Segment_l2"

HAnimHumanoid42.segments.append(HAnimSegment1882)
HAnimJoint1883 = x3d.HAnimJoint()
HAnimJoint1883.USE = "STD_Joint_vl1"

HAnimHumanoid42.joints.append(HAnimJoint1883)
HAnimSegment1884 = x3d.HAnimSegment()
HAnimSegment1884.USE = "STD_Segment_l1"

HAnimHumanoid42.segments.append(HAnimSegment1884)
HAnimJoint1885 = x3d.HAnimJoint()
HAnimJoint1885.USE = "STD_Joint_vt12"

HAnimHumanoid42.joints.append(HAnimJoint1885)
HAnimSegment1886 = x3d.HAnimSegment()
HAnimSegment1886.USE = "STD_Segment_t12"

HAnimHumanoid42.segments.append(HAnimSegment1886)
HAnimJoint1887 = x3d.HAnimJoint()
HAnimJoint1887.USE = "STD_Joint_vt11"

HAnimHumanoid42.joints.append(HAnimJoint1887)
HAnimSegment1888 = x3d.HAnimSegment()
HAnimSegment1888.USE = "STD_Segment_t11"

HAnimHumanoid42.segments.append(HAnimSegment1888)
HAnimJoint1889 = x3d.HAnimJoint()
HAnimJoint1889.USE = "STD_Joint_vt10"

HAnimHumanoid42.joints.append(HAnimJoint1889)
HAnimSite1890 = x3d.HAnimSite()
HAnimSite1890.USE = "STD_Site_substernale_pt"

HAnimHumanoid42.sites.append(HAnimSite1890)
HAnimSegment1891 = x3d.HAnimSegment()
HAnimSegment1891.USE = "STD_Segment_t10"

HAnimHumanoid42.segments.append(HAnimSegment1891)
HAnimJoint1892 = x3d.HAnimJoint()
HAnimJoint1892.USE = "STD_Joint_vt9"

HAnimHumanoid42.joints.append(HAnimJoint1892)
HAnimSite1893 = x3d.HAnimSite()
HAnimSite1893.USE = "STD_Site_l_thelion_pt"

HAnimHumanoid42.sites.append(HAnimSite1893)
HAnimSite1894 = x3d.HAnimSite()
HAnimSite1894.USE = "STD_Site_r_thelion_pt"

HAnimHumanoid42.sites.append(HAnimSite1894)
HAnimSegment1895 = x3d.HAnimSegment()
HAnimSegment1895.USE = "STD_Segment_t9"

HAnimHumanoid42.segments.append(HAnimSegment1895)
HAnimJoint1896 = x3d.HAnimJoint()
HAnimJoint1896.USE = "STD_Joint_vt8"

HAnimHumanoid42.joints.append(HAnimJoint1896)
HAnimSegment1897 = x3d.HAnimSegment()
HAnimSegment1897.USE = "STD_Segment_t8"

HAnimHumanoid42.segments.append(HAnimSegment1897)
HAnimJoint1898 = x3d.HAnimJoint()
HAnimJoint1898.USE = "STD_Joint_vt7"

HAnimHumanoid42.joints.append(HAnimJoint1898)
HAnimSegment1899 = x3d.HAnimSegment()
HAnimSegment1899.USE = "STD_Segment_t7"

HAnimHumanoid42.segments.append(HAnimSegment1899)
HAnimJoint1900 = x3d.HAnimJoint()
HAnimJoint1900.USE = "STD_Joint_vt6"

HAnimHumanoid42.joints.append(HAnimJoint1900)
HAnimSite1901 = x3d.HAnimSite()
HAnimSite1901.USE = "STD_Site_l_chest_midsagittal_plane_pt"

HAnimHumanoid42.sites.append(HAnimSite1901)
HAnimSite1902 = x3d.HAnimSite()
HAnimSite1902.USE = "STD_Site_mesosternale_pt"

HAnimHumanoid42.sites.append(HAnimSite1902)
HAnimSite1903 = x3d.HAnimSite()
HAnimSite1903.USE = "STD_Site_r_chest_midsagittal_plane_pt"

HAnimHumanoid42.sites.append(HAnimSite1903)
HAnimSite1904 = x3d.HAnimSite()
HAnimSite1904.USE = "STD_Site_rear_center_midsagittal_plane_pt"

HAnimHumanoid42.sites.append(HAnimSite1904)
HAnimSegment1905 = x3d.HAnimSegment()
HAnimSegment1905.USE = "STD_Segment_t6"

HAnimHumanoid42.segments.append(HAnimSegment1905)
HAnimJoint1906 = x3d.HAnimJoint()
HAnimJoint1906.USE = "STD_Joint_vt5"

HAnimHumanoid42.joints.append(HAnimJoint1906)
HAnimSite1907 = x3d.HAnimSite()
HAnimSite1907.USE = "STD_Site_spine_1_middle_back_pt"

HAnimHumanoid42.sites.append(HAnimSite1907)
HAnimSegment1908 = x3d.HAnimSegment()
HAnimSegment1908.USE = "STD_Segment_t5"

HAnimHumanoid42.segments.append(HAnimSegment1908)
HAnimJoint1909 = x3d.HAnimJoint()
HAnimJoint1909.USE = "STD_Joint_vt4"

HAnimHumanoid42.joints.append(HAnimJoint1909)
HAnimSegment1910 = x3d.HAnimSegment()
HAnimSegment1910.USE = "STD_Segment_t4"

HAnimHumanoid42.segments.append(HAnimSegment1910)
HAnimJoint1911 = x3d.HAnimJoint()
HAnimJoint1911.USE = "STD_Joint_vt3"

HAnimHumanoid42.joints.append(HAnimJoint1911)
HAnimSegment1912 = x3d.HAnimSegment()
HAnimSegment1912.USE = "STD_Segment_t3"

HAnimHumanoid42.segments.append(HAnimSegment1912)
HAnimJoint1913 = x3d.HAnimJoint()
HAnimJoint1913.USE = "STD_Joint_vt2"

HAnimHumanoid42.joints.append(HAnimJoint1913)
HAnimSegment1914 = x3d.HAnimSegment()
HAnimSegment1914.USE = "STD_Segment_t2"

HAnimHumanoid42.segments.append(HAnimSegment1914)
HAnimJoint1915 = x3d.HAnimJoint()
HAnimJoint1915.USE = "STD_Joint_vt1"

HAnimHumanoid42.joints.append(HAnimJoint1915)
HAnimSite1916 = x3d.HAnimSite()
HAnimSite1916.USE = "STD_Site_cervicale_pt"

HAnimHumanoid42.sites.append(HAnimSite1916)
HAnimSite1917 = x3d.HAnimSite()
HAnimSite1917.USE = "STD_Site_suprasternale_pt"

HAnimHumanoid42.sites.append(HAnimSite1917)
HAnimSegment1918 = x3d.HAnimSegment()
HAnimSegment1918.USE = "STD_Segment_t1"

HAnimHumanoid42.segments.append(HAnimSegment1918)
HAnimJoint1919 = x3d.HAnimJoint()
HAnimJoint1919.USE = "STD_Joint_vc7"

HAnimHumanoid42.joints.append(HAnimJoint1919)
HAnimSite1920 = x3d.HAnimSite()
HAnimSite1920.USE = "STD_Site_l_neck_base_pt"

HAnimHumanoid42.sites.append(HAnimSite1920)
HAnimSite1921 = x3d.HAnimSite()
HAnimSite1921.USE = "STD_Site_r_neck_base_pt"

HAnimHumanoid42.sites.append(HAnimSite1921)
HAnimSegment1922 = x3d.HAnimSegment()
HAnimSegment1922.USE = "STD_Segment_c7"

HAnimHumanoid42.segments.append(HAnimSegment1922)
HAnimJoint1923 = x3d.HAnimJoint()
HAnimJoint1923.USE = "STD_Joint_vc6"

HAnimHumanoid42.joints.append(HAnimJoint1923)
HAnimSegment1924 = x3d.HAnimSegment()
HAnimSegment1924.USE = "STD_Segment_c6"

HAnimHumanoid42.segments.append(HAnimSegment1924)
HAnimJoint1925 = x3d.HAnimJoint()
HAnimJoint1925.USE = "STD_Joint_vc5"

HAnimHumanoid42.joints.append(HAnimJoint1925)
HAnimSegment1926 = x3d.HAnimSegment()
HAnimSegment1926.USE = "STD_Segment_c5"

HAnimHumanoid42.segments.append(HAnimSegment1926)
HAnimJoint1927 = x3d.HAnimJoint()
HAnimJoint1927.USE = "STD_Joint_vc4"

HAnimHumanoid42.joints.append(HAnimJoint1927)
HAnimSegment1928 = x3d.HAnimSegment()
HAnimSegment1928.USE = "STD_Segment_c4"

HAnimHumanoid42.segments.append(HAnimSegment1928)
HAnimJoint1929 = x3d.HAnimJoint()
HAnimJoint1929.USE = "STD_Joint_vc3"

HAnimHumanoid42.joints.append(HAnimJoint1929)
HAnimSegment1930 = x3d.HAnimSegment()
HAnimSegment1930.USE = "STD_Segment_c3"

HAnimHumanoid42.segments.append(HAnimSegment1930)
HAnimJoint1931 = x3d.HAnimJoint()
HAnimJoint1931.USE = "STD_Joint_vc2"

HAnimHumanoid42.joints.append(HAnimJoint1931)
HAnimSite1932 = x3d.HAnimSite()
HAnimSite1932.USE = "STD_Site_adams_apple_pt"

HAnimHumanoid42.sites.append(HAnimSite1932)
HAnimSegment1933 = x3d.HAnimSegment()
HAnimSegment1933.USE = "STD_Segment_c2"

HAnimHumanoid42.segments.append(HAnimSegment1933)
HAnimJoint1934 = x3d.HAnimJoint()
HAnimJoint1934.USE = "STD_Joint_vc1"

HAnimHumanoid42.joints.append(HAnimJoint1934)
HAnimSegment1935 = x3d.HAnimSegment()
HAnimSegment1935.USE = "STD_Segment_c1"

HAnimHumanoid42.segments.append(HAnimSegment1935)
HAnimJoint1936 = x3d.HAnimJoint()
HAnimJoint1936.USE = "STD_Joint_skullbase"

HAnimHumanoid42.joints.append(HAnimJoint1936)
HAnimSite1937 = x3d.HAnimSite()
HAnimSite1937.USE = "STD_Site_glabella_pt"

HAnimHumanoid42.sites.append(HAnimSite1937)
HAnimSite1938 = x3d.HAnimSite()
HAnimSite1938.USE = "STD_Site_l_ectocanthus_pt"

HAnimHumanoid42.sites.append(HAnimSite1938)
HAnimSite1939 = x3d.HAnimSite()
HAnimSite1939.USE = "STD_Site_l_infraorbitale_pt"

HAnimHumanoid42.sites.append(HAnimSite1939)
HAnimSite1940 = x3d.HAnimSite()
HAnimSite1940.USE = "STD_Site_l_tragion_pt"

HAnimHumanoid42.sites.append(HAnimSite1940)
HAnimSite1941 = x3d.HAnimSite()
HAnimSite1941.USE = "STD_Site_nuchale_pt"

HAnimHumanoid42.sites.append(HAnimSite1941)
HAnimSite1942 = x3d.HAnimSite()
HAnimSite1942.USE = "STD_Site_opisthocranion_pt"

HAnimHumanoid42.sites.append(HAnimSite1942)
HAnimSite1943 = x3d.HAnimSite()
HAnimSite1943.USE = "STD_Site_r_ectocanthus_pt"

HAnimHumanoid42.sites.append(HAnimSite1943)
HAnimSite1944 = x3d.HAnimSite()
HAnimSite1944.USE = "STD_Site_r_infraorbitale_pt"

HAnimHumanoid42.sites.append(HAnimSite1944)
HAnimSite1945 = x3d.HAnimSite()
HAnimSite1945.USE = "STD_Site_r_tragion_pt"

HAnimHumanoid42.sites.append(HAnimSite1945)
HAnimSite1946 = x3d.HAnimSite()
HAnimSite1946.USE = "STD_Site_sellion_pt"

HAnimHumanoid42.sites.append(HAnimSite1946)
HAnimSite1947 = x3d.HAnimSite()
HAnimSite1947.USE = "STD_Site_skull_vertex_pt"

HAnimHumanoid42.sites.append(HAnimSite1947)
HAnimSegment1948 = x3d.HAnimSegment()
HAnimSegment1948.USE = "STD_Segment_skull"

HAnimHumanoid42.segments.append(HAnimSegment1948)
HAnimJoint1949 = x3d.HAnimJoint()
HAnimJoint1949.USE = "STD_Joint_l_eyelid_joint"

HAnimHumanoid42.joints.append(HAnimJoint1949)
HAnimSegment1950 = x3d.HAnimSegment()
HAnimSegment1950.USE = "STD_Segment_l_eyelid"

HAnimHumanoid42.segments.append(HAnimSegment1950)
HAnimJoint1951 = x3d.HAnimJoint()
HAnimJoint1951.USE = "STD_Joint_r_eyelid_joint"

HAnimHumanoid42.joints.append(HAnimJoint1951)
HAnimSegment1952 = x3d.HAnimSegment()
HAnimSegment1952.USE = "STD_Segment_r_eyelid"

HAnimHumanoid42.segments.append(HAnimSegment1952)
HAnimJoint1953 = x3d.HAnimJoint()
HAnimJoint1953.USE = "STD_Joint_l_eyeball_joint"

HAnimHumanoid42.joints.append(HAnimJoint1953)
HAnimSegment1954 = x3d.HAnimSegment()
HAnimSegment1954.USE = "STD_Segment_l_eyeball"

HAnimHumanoid42.segments.append(HAnimSegment1954)
HAnimJoint1955 = x3d.HAnimJoint()
HAnimJoint1955.USE = "STD_Joint_r_eyeball_joint"

HAnimHumanoid42.joints.append(HAnimJoint1955)
HAnimSegment1956 = x3d.HAnimSegment()
HAnimSegment1956.USE = "STD_Segment_r_eyeball"

HAnimHumanoid42.segments.append(HAnimSegment1956)
HAnimJoint1957 = x3d.HAnimJoint()
HAnimJoint1957.USE = "STD_Joint_l_eyebrow_joint"

HAnimHumanoid42.joints.append(HAnimJoint1957)
HAnimSegment1958 = x3d.HAnimSegment()
HAnimSegment1958.USE = "STD_Segment_l_eyebrow"

HAnimHumanoid42.segments.append(HAnimSegment1958)
HAnimJoint1959 = x3d.HAnimJoint()
HAnimJoint1959.USE = "STD_Joint_r_eyebrow_joint"

HAnimHumanoid42.joints.append(HAnimJoint1959)
HAnimSegment1960 = x3d.HAnimSegment()
HAnimSegment1960.USE = "STD_Segment_r_eyebrow"

HAnimHumanoid42.segments.append(HAnimSegment1960)
HAnimJoint1961 = x3d.HAnimJoint()
HAnimJoint1961.USE = "STD_Joint_temporomandibular"

HAnimHumanoid42.joints.append(HAnimJoint1961)
HAnimSite1962 = x3d.HAnimSite()
HAnimSite1962.USE = "STD_Site_l_gonion_pt"

HAnimHumanoid42.sites.append(HAnimSite1962)
HAnimSite1963 = x3d.HAnimSite()
HAnimSite1963.USE = "STD_Site_menton_pt"

HAnimHumanoid42.sites.append(HAnimSite1963)
HAnimSite1964 = x3d.HAnimSite()
HAnimSite1964.USE = "STD_Site_r_gonion_pt"

HAnimHumanoid42.sites.append(HAnimSite1964)
HAnimSite1965 = x3d.HAnimSite()
HAnimSite1965.USE = "STD_Site_supramenton_pt"

HAnimHumanoid42.sites.append(HAnimSite1965)
HAnimSegment1966 = x3d.HAnimSegment()
HAnimSegment1966.USE = "STD_Segment_jaw"

HAnimHumanoid42.segments.append(HAnimSegment1966)
HAnimJoint1967 = x3d.HAnimJoint()
HAnimJoint1967.USE = "STD_Joint_l_sternoclavicular"

HAnimHumanoid42.joints.append(HAnimJoint1967)
HAnimSite1968 = x3d.HAnimSite()
HAnimSite1968.USE = "STD_Site_l_acromion_pt"

HAnimHumanoid42.sites.append(HAnimSite1968)
HAnimSite1969 = x3d.HAnimSite()
HAnimSite1969.USE = "STD_Site_l_axilla_distal_pt"

HAnimHumanoid42.sites.append(HAnimSite1969)
HAnimSite1970 = x3d.HAnimSite()
HAnimSite1970.USE = "STD_Site_l_axilla_posterior_folds_pt"

HAnimHumanoid42.sites.append(HAnimSite1970)
HAnimSite1971 = x3d.HAnimSite()
HAnimSite1971.USE = "STD_Site_l_axilla_proximal_pt"

HAnimHumanoid42.sites.append(HAnimSite1971)
HAnimSite1972 = x3d.HAnimSite()
HAnimSite1972.USE = "STD_Site_l_clavicale_pt"

HAnimHumanoid42.sites.append(HAnimSite1972)
HAnimSegment1973 = x3d.HAnimSegment()
HAnimSegment1973.USE = "STD_Segment_l_clavicle"

HAnimHumanoid42.segments.append(HAnimSegment1973)
HAnimJoint1974 = x3d.HAnimJoint()
HAnimJoint1974.USE = "STD_Joint_l_acromioclavicular"

HAnimHumanoid42.joints.append(HAnimJoint1974)
HAnimSegment1975 = x3d.HAnimSegment()
HAnimSegment1975.USE = "STD_Segment_l_scapula"

HAnimHumanoid42.segments.append(HAnimSegment1975)
HAnimJoint1976 = x3d.HAnimJoint()
HAnimJoint1976.USE = "STD_Joint_l_shoulder"

HAnimHumanoid42.joints.append(HAnimJoint1976)
HAnimSite1977 = x3d.HAnimSite()
HAnimSite1977.USE = "STD_Site_l_bideltoid_pt"

HAnimHumanoid42.sites.append(HAnimSite1977)
HAnimSite1978 = x3d.HAnimSite()
HAnimSite1978.USE = "STD_Site_l_humeral_lateral_epicondyles_pt"

HAnimHumanoid42.sites.append(HAnimSite1978)
HAnimSegment1979 = x3d.HAnimSegment()
HAnimSegment1979.USE = "STD_Segment_l_upperarm"

HAnimHumanoid42.segments.append(HAnimSegment1979)
HAnimJoint1980 = x3d.HAnimJoint()
HAnimJoint1980.USE = "STD_Joint_l_elbow"

HAnimHumanoid42.joints.append(HAnimJoint1980)
HAnimSite1981 = x3d.HAnimSite()
HAnimSite1981.USE = "STD_Site_l_humeral_medial_epicondyles_pt"

HAnimHumanoid42.sites.append(HAnimSite1981)
HAnimSite1982 = x3d.HAnimSite()
HAnimSite1982.USE = "STD_Site_l_olecranon_pt"

HAnimHumanoid42.sites.append(HAnimSite1982)
HAnimSite1983 = x3d.HAnimSite()
HAnimSite1983.USE = "STD_Site_l_radial_styloid_pt"

HAnimHumanoid42.sites.append(HAnimSite1983)
HAnimSite1984 = x3d.HAnimSite()
HAnimSite1984.USE = "STD_Site_l_radiale_pt"

HAnimHumanoid42.sites.append(HAnimSite1984)
HAnimSegment1985 = x3d.HAnimSegment()
HAnimSegment1985.USE = "STD_Segment_l_forearm"

HAnimHumanoid42.segments.append(HAnimSegment1985)
HAnimJoint1986 = x3d.HAnimJoint()
HAnimJoint1986.USE = "STD_Joint_l_radiocarpal"

HAnimHumanoid42.joints.append(HAnimJoint1986)
HAnimSite1987 = x3d.HAnimSite()
HAnimSite1987.USE = "STD_Site_l_ulnar_styloid_pt"

HAnimHumanoid42.sites.append(HAnimSite1987)
HAnimSegment1988 = x3d.HAnimSegment()
HAnimSegment1988.USE = "STD_Segment_l_carpal"

HAnimHumanoid42.segments.append(HAnimSegment1988)
HAnimJoint1989 = x3d.HAnimJoint()
HAnimJoint1989.USE = "STD_Joint_l_midcarpal_1"

HAnimHumanoid42.joints.append(HAnimJoint1989)
HAnimSegment1990 = x3d.HAnimSegment()
HAnimSegment1990.USE = "STD_Segment_l_trapezium"

HAnimHumanoid42.segments.append(HAnimSegment1990)
HAnimJoint1991 = x3d.HAnimJoint()
HAnimJoint1991.USE = "STD_Joint_l_carpometacarpal_1"

HAnimHumanoid42.joints.append(HAnimJoint1991)
HAnimSegment1992 = x3d.HAnimSegment()
HAnimSegment1992.USE = "STD_Segment_l_metacarpal_1"

HAnimHumanoid42.segments.append(HAnimSegment1992)
HAnimJoint1993 = x3d.HAnimJoint()
HAnimJoint1993.USE = "STD_Joint_l_metacarpophalangeal_1"

HAnimHumanoid42.joints.append(HAnimJoint1993)
HAnimSegment1994 = x3d.HAnimSegment()
HAnimSegment1994.USE = "STD_Segment_l_carpal_proximal_phalanx_1"

HAnimHumanoid42.segments.append(HAnimSegment1994)
HAnimJoint1995 = x3d.HAnimJoint()
HAnimJoint1995.USE = "STD_Joint_l_carpal_interphalangeal_1"

HAnimHumanoid42.joints.append(HAnimJoint1995)
HAnimSite1996 = x3d.HAnimSite()
HAnimSite1996.USE = "STD_Site_l_carpal_distal_phalanx_1_tip"

HAnimHumanoid42.sites.append(HAnimSite1996)
HAnimSegment1997 = x3d.HAnimSegment()
HAnimSegment1997.USE = "STD_Segment_l_carpal_distal_phalanx_1"

HAnimHumanoid42.segments.append(HAnimSegment1997)
HAnimJoint1998 = x3d.HAnimJoint()
HAnimJoint1998.USE = "STD_Joint_l_midcarpal_2"

HAnimHumanoid42.joints.append(HAnimJoint1998)
HAnimSegment1999 = x3d.HAnimSegment()
HAnimSegment1999.USE = "STD_Segment_l_trapezoid"

HAnimHumanoid42.segments.append(HAnimSegment1999)
HAnimJoint2000 = x3d.HAnimJoint()
HAnimJoint2000.USE = "STD_Joint_l_carpometacarpal_2"

HAnimHumanoid42.joints.append(HAnimJoint2000)
HAnimSite2001 = x3d.HAnimSite()
HAnimSite2001.USE = "STD_Site_l_metacarpal_phalanx_2_pt"

HAnimHumanoid42.sites.append(HAnimSite2001)
HAnimSegment2002 = x3d.HAnimSegment()
HAnimSegment2002.USE = "STD_Segment_l_metacarpal_2"

HAnimHumanoid42.segments.append(HAnimSegment2002)
HAnimJoint2003 = x3d.HAnimJoint()
HAnimJoint2003.USE = "STD_Joint_l_metacarpophalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint2003)
HAnimSegment2004 = x3d.HAnimSegment()
HAnimSegment2004.USE = "STD_Segment_l_carpal_proximal_phalanx_2 "

HAnimHumanoid42.segments.append(HAnimSegment2004)
HAnimJoint2005 = x3d.HAnimJoint()
HAnimJoint2005.USE = "STD_Joint_l_carpal_proximal_interphalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint2005)
HAnimSegment2006 = x3d.HAnimSegment()
HAnimSegment2006.USE = "STD_Segment_l_carpal_middle_phalanx_2"

HAnimHumanoid42.segments.append(HAnimSegment2006)
HAnimJoint2007 = x3d.HAnimJoint()
HAnimJoint2007.USE = "STD_Joint_l_carpal_distal_interphalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint2007)
HAnimSite2008 = x3d.HAnimSite()
HAnimSite2008.USE = "STD_Site_l_carpal_distal_phalanx_2_tip"

HAnimHumanoid42.sites.append(HAnimSite2008)
HAnimSite2009 = x3d.HAnimSite()
HAnimSite2009.USE = "STD_Site_l_dactylion_pt"

HAnimHumanoid42.sites.append(HAnimSite2009)
HAnimSegment2010 = x3d.HAnimSegment()
HAnimSegment2010.USE = "STD_Segment_l_carpal_distal_phalanx_2"

HAnimHumanoid42.segments.append(HAnimSegment2010)
HAnimJoint2011 = x3d.HAnimJoint()
HAnimJoint2011.USE = "STD_Joint_l_midcarpal_3"

HAnimHumanoid42.joints.append(HAnimJoint2011)
HAnimSegment2012 = x3d.HAnimSegment()
HAnimSegment2012.USE = "STD_Segment_l_capitate"

HAnimHumanoid42.segments.append(HAnimSegment2012)
HAnimJoint2013 = x3d.HAnimJoint()
HAnimJoint2013.USE = "STD_Joint_l_carpometacarpal_3"

HAnimHumanoid42.joints.append(HAnimJoint2013)
HAnimSite2014 = x3d.HAnimSite()
HAnimSite2014.USE = "STD_Site_l_metacarpal_phalanx_3_pt"

HAnimHumanoid42.sites.append(HAnimSite2014)
HAnimSegment2015 = x3d.HAnimSegment()
HAnimSegment2015.USE = "STD_Segment_l_metacarpal_3"

HAnimHumanoid42.segments.append(HAnimSegment2015)
HAnimJoint2016 = x3d.HAnimJoint()
HAnimJoint2016.USE = "STD_Joint_l_metacarpophalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint2016)
HAnimSegment2017 = x3d.HAnimSegment()
HAnimSegment2017.USE = "STD_Segment_l_carpal_proximal_phalanx_3"

HAnimHumanoid42.segments.append(HAnimSegment2017)
HAnimJoint2018 = x3d.HAnimJoint()
HAnimJoint2018.USE = "STD_Joint_l_carpal_proximal_interphalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint2018)
HAnimSegment2019 = x3d.HAnimSegment()
HAnimSegment2019.USE = "STD_Segment_l_carpal_middle_phalanx_3"

HAnimHumanoid42.segments.append(HAnimSegment2019)
HAnimJoint2020 = x3d.HAnimJoint()
HAnimJoint2020.USE = "STD_Joint_l_carpal_distal_interphalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint2020)
HAnimSite2021 = x3d.HAnimSite()
HAnimSite2021.USE = "STD_Site_l_carpal_distal_phalanx_3_tip"

HAnimHumanoid42.sites.append(HAnimSite2021)
HAnimSegment2022 = x3d.HAnimSegment()
HAnimSegment2022.USE = "STD_Segment_l_carpal_distal_phalanx_3"

HAnimHumanoid42.segments.append(HAnimSegment2022)
HAnimJoint2023 = x3d.HAnimJoint()
HAnimJoint2023.USE = "STD_Joint_l_midcarpal_4_5"

HAnimHumanoid42.joints.append(HAnimJoint2023)
HAnimSegment2024 = x3d.HAnimSegment()
HAnimSegment2024.USE = "STD_Segment_l_hamate"

HAnimHumanoid42.segments.append(HAnimSegment2024)
HAnimJoint2025 = x3d.HAnimJoint()
HAnimJoint2025.USE = "STD_Joint_l_carpometacarpal_4"

HAnimHumanoid42.joints.append(HAnimJoint2025)
HAnimSegment2026 = x3d.HAnimSegment()
HAnimSegment2026.USE = "STD_Segment_l_metacarpal_4"

HAnimHumanoid42.segments.append(HAnimSegment2026)
HAnimJoint2027 = x3d.HAnimJoint()
HAnimJoint2027.USE = "STD_Joint_l_metacarpophalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint2027)
HAnimSegment2028 = x3d.HAnimSegment()
HAnimSegment2028.USE = "STD_Segment_l_carpal_proximal_phalanx_4"

HAnimHumanoid42.segments.append(HAnimSegment2028)
HAnimJoint2029 = x3d.HAnimJoint()
HAnimJoint2029.USE = "STD_Joint_l_carpal_proximal_interphalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint2029)
HAnimSegment2030 = x3d.HAnimSegment()
HAnimSegment2030.USE = "STD_Segment_l_carpal_middle_phalanx_4"

HAnimHumanoid42.segments.append(HAnimSegment2030)
HAnimJoint2031 = x3d.HAnimJoint()
HAnimJoint2031.USE = "STD_Joint_l_carpal_distal_interphalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint2031)
HAnimSite2032 = x3d.HAnimSite()
HAnimSite2032.USE = "STD_Site_l_carpal_distal_phalanx_4_tip"

HAnimHumanoid42.sites.append(HAnimSite2032)
HAnimSegment2033 = x3d.HAnimSegment()
HAnimSegment2033.USE = "STD_Segment_l_carpal_distal_phalanx_4"

HAnimHumanoid42.segments.append(HAnimSegment2033)
HAnimJoint2034 = x3d.HAnimJoint()
HAnimJoint2034.USE = "STD_Joint_l_carpometacarpal_5"

HAnimHumanoid42.joints.append(HAnimJoint2034)
HAnimSite2035 = x3d.HAnimSite()
HAnimSite2035.USE = "STD_Site_l_metacarpal_phalanx_5_pt"

HAnimHumanoid42.sites.append(HAnimSite2035)
HAnimSegment2036 = x3d.HAnimSegment()
HAnimSegment2036.USE = "STD_Segment_l_metacarpal_5"

HAnimHumanoid42.segments.append(HAnimSegment2036)
HAnimJoint2037 = x3d.HAnimJoint()
HAnimJoint2037.USE = "STD_Joint_l_metacarpophalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint2037)
HAnimSegment2038 = x3d.HAnimSegment()
HAnimSegment2038.USE = "STD_Segment_l_carpal_proximal_phalanx_5"

HAnimHumanoid42.segments.append(HAnimSegment2038)
HAnimJoint2039 = x3d.HAnimJoint()
HAnimJoint2039.USE = "STD_Joint_l_carpal_proximal_interphalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint2039)
HAnimSegment2040 = x3d.HAnimSegment()
HAnimSegment2040.USE = "STD_Segment_l_carpal_middle_phalanx_5"

HAnimHumanoid42.segments.append(HAnimSegment2040)
HAnimJoint2041 = x3d.HAnimJoint()
HAnimJoint2041.USE = "STD_Joint_l_carpal_distal_interphalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint2041)
HAnimSite2042 = x3d.HAnimSite()
HAnimSite2042.USE = "STD_Site_l_carpal_distal_phalanx_5_tip"

HAnimHumanoid42.sites.append(HAnimSite2042)
HAnimSegment2043 = x3d.HAnimSegment()
HAnimSegment2043.USE = "STD_Segment_l_carpal_distal_phalanx_5"

HAnimHumanoid42.segments.append(HAnimSegment2043)
HAnimJoint2044 = x3d.HAnimJoint()
HAnimJoint2044.USE = "STD_Joint_r_sternoclavicular"

HAnimHumanoid42.joints.append(HAnimJoint2044)
HAnimSite2045 = x3d.HAnimSite()
HAnimSite2045.USE = "STD_Site_r_acromion_pt"

HAnimHumanoid42.sites.append(HAnimSite2045)
HAnimSite2046 = x3d.HAnimSite()
HAnimSite2046.USE = "STD_Site_r_axilla_distal_pt"

HAnimHumanoid42.sites.append(HAnimSite2046)
HAnimSite2047 = x3d.HAnimSite()
HAnimSite2047.USE = "STD_Site_r_axilla_posterior_folds_pt"

HAnimHumanoid42.sites.append(HAnimSite2047)
HAnimSite2048 = x3d.HAnimSite()
HAnimSite2048.USE = "STD_Site_r_axilla_proximal_pt"

HAnimHumanoid42.sites.append(HAnimSite2048)
HAnimSite2049 = x3d.HAnimSite()
HAnimSite2049.USE = "STD_Site_r_clavicale_pt"

HAnimHumanoid42.sites.append(HAnimSite2049)
HAnimSegment2050 = x3d.HAnimSegment()
HAnimSegment2050.USE = "STD_Segment_r_clavicle"

HAnimHumanoid42.segments.append(HAnimSegment2050)
HAnimJoint2051 = x3d.HAnimJoint()
HAnimJoint2051.USE = "STD_Joint_r_acromioclavicular"

HAnimHumanoid42.joints.append(HAnimJoint2051)
HAnimSegment2052 = x3d.HAnimSegment()
HAnimSegment2052.USE = "STD_Segment_r_scapula"

HAnimHumanoid42.segments.append(HAnimSegment2052)
HAnimJoint2053 = x3d.HAnimJoint()
HAnimJoint2053.USE = "STD_Joint_r_shoulder"

HAnimHumanoid42.joints.append(HAnimJoint2053)
HAnimSite2054 = x3d.HAnimSite()
HAnimSite2054.USE = "STD_Site_r_bideltoid_pt"

HAnimHumanoid42.sites.append(HAnimSite2054)
HAnimSite2055 = x3d.HAnimSite()
HAnimSite2055.USE = "STD_Site_r_humeral_lateral_epicondyles_pt"

HAnimHumanoid42.sites.append(HAnimSite2055)
HAnimSegment2056 = x3d.HAnimSegment()
HAnimSegment2056.USE = "STD_Segment_r_upperarm"

HAnimHumanoid42.segments.append(HAnimSegment2056)
HAnimJoint2057 = x3d.HAnimJoint()
HAnimJoint2057.USE = "STD_Joint_r_elbow"

HAnimHumanoid42.joints.append(HAnimJoint2057)
HAnimSite2058 = x3d.HAnimSite()
HAnimSite2058.USE = "STD_Site_r_humeral_medial_epicondyles_pt"

HAnimHumanoid42.sites.append(HAnimSite2058)
HAnimSite2059 = x3d.HAnimSite()
HAnimSite2059.USE = "STD_Site_r_olecranon_pt"

HAnimHumanoid42.sites.append(HAnimSite2059)
HAnimSite2060 = x3d.HAnimSite()
HAnimSite2060.USE = "STD_Site_r_radial_styloid_pt"

HAnimHumanoid42.sites.append(HAnimSite2060)
HAnimSite2061 = x3d.HAnimSite()
HAnimSite2061.USE = "STD_Site_r_radiale_pt"

HAnimHumanoid42.sites.append(HAnimSite2061)
HAnimSegment2062 = x3d.HAnimSegment()
HAnimSegment2062.USE = "STD_Segment_r_forearm"

HAnimHumanoid42.segments.append(HAnimSegment2062)
HAnimJoint2063 = x3d.HAnimJoint()
HAnimJoint2063.USE = "STD_Joint_r_radiocarpal"

HAnimHumanoid42.joints.append(HAnimJoint2063)
HAnimSite2064 = x3d.HAnimSite()
HAnimSite2064.USE = "STD_Site_r_ulnar_styloid_pt"

HAnimHumanoid42.sites.append(HAnimSite2064)
HAnimSegment2065 = x3d.HAnimSegment()
HAnimSegment2065.USE = "STD_Segment_r_carpal"

HAnimHumanoid42.segments.append(HAnimSegment2065)
HAnimJoint2066 = x3d.HAnimJoint()
HAnimJoint2066.USE = "STD_Joint_r_midcarpal_1"

HAnimHumanoid42.joints.append(HAnimJoint2066)
HAnimSegment2067 = x3d.HAnimSegment()
HAnimSegment2067.USE = "STD_Segment_r_trapezium"

HAnimHumanoid42.segments.append(HAnimSegment2067)
HAnimJoint2068 = x3d.HAnimJoint()
HAnimJoint2068.USE = "STD_Joint_r_carpometacarpal_1"

HAnimHumanoid42.joints.append(HAnimJoint2068)
HAnimSegment2069 = x3d.HAnimSegment()
HAnimSegment2069.USE = "STD_Segment_r_metacarpal_1"

HAnimHumanoid42.segments.append(HAnimSegment2069)
HAnimJoint2070 = x3d.HAnimJoint()
HAnimJoint2070.USE = "STD_Joint_r_metacarpophalangeal_1"

HAnimHumanoid42.joints.append(HAnimJoint2070)
HAnimSegment2071 = x3d.HAnimSegment()
HAnimSegment2071.USE = "STD_Segment_r_carpal_proximal_phalanx_1"

HAnimHumanoid42.segments.append(HAnimSegment2071)
HAnimJoint2072 = x3d.HAnimJoint()
HAnimJoint2072.USE = "STD_Joint_r_carpal_interphalangeal_1"

HAnimHumanoid42.joints.append(HAnimJoint2072)
HAnimSite2073 = x3d.HAnimSite()
HAnimSite2073.USE = "STD_Site_r_carpal_distal_phalanx_1_tip"

HAnimHumanoid42.sites.append(HAnimSite2073)
HAnimSegment2074 = x3d.HAnimSegment()
HAnimSegment2074.USE = "STD_Segment_r_carpal_distal_phalanx_1"

HAnimHumanoid42.segments.append(HAnimSegment2074)
HAnimJoint2075 = x3d.HAnimJoint()
HAnimJoint2075.USE = "STD_Joint_r_midcarpal_2"

HAnimHumanoid42.joints.append(HAnimJoint2075)
HAnimSegment2076 = x3d.HAnimSegment()
HAnimSegment2076.USE = "STD_Segment_r_trapezoid"

HAnimHumanoid42.segments.append(HAnimSegment2076)
HAnimJoint2077 = x3d.HAnimJoint()
HAnimJoint2077.USE = "STD_Joint_r_carpometacarpal_2"

HAnimHumanoid42.joints.append(HAnimJoint2077)
HAnimSite2078 = x3d.HAnimSite()
HAnimSite2078.USE = "STD_Site_r_metacarpal_phalanx_2_pt"

HAnimHumanoid42.sites.append(HAnimSite2078)
HAnimSegment2079 = x3d.HAnimSegment()
HAnimSegment2079.USE = "STD_Segment_r_metacarpal_2"

HAnimHumanoid42.segments.append(HAnimSegment2079)
HAnimJoint2080 = x3d.HAnimJoint()
HAnimJoint2080.USE = "STD_Joint_r_metacarpophalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint2080)
HAnimSegment2081 = x3d.HAnimSegment()
HAnimSegment2081.USE = "STD_Segment_r_carpal_proximal_phalanx_2 "

HAnimHumanoid42.segments.append(HAnimSegment2081)
HAnimJoint2082 = x3d.HAnimJoint()
HAnimJoint2082.USE = "STD_Joint_r_carpal_proximal_interphalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint2082)
HAnimSegment2083 = x3d.HAnimSegment()
HAnimSegment2083.USE = "STD_Segment_r_carpal_middle_phalanx_2"

HAnimHumanoid42.segments.append(HAnimSegment2083)
HAnimJoint2084 = x3d.HAnimJoint()
HAnimJoint2084.USE = "STD_Joint_r_carpal_distal_interphalangeal_2"

HAnimHumanoid42.joints.append(HAnimJoint2084)
HAnimSite2085 = x3d.HAnimSite()
HAnimSite2085.USE = "STD_Site_r_carpal_distal_phalanx_2_tip"

HAnimHumanoid42.sites.append(HAnimSite2085)
HAnimSite2086 = x3d.HAnimSite()
HAnimSite2086.USE = "STD_Site_r_dactylion_pt"

HAnimHumanoid42.sites.append(HAnimSite2086)
HAnimSegment2087 = x3d.HAnimSegment()
HAnimSegment2087.USE = "STD_Segment_r_carpal_distal_phalanx_2"

HAnimHumanoid42.segments.append(HAnimSegment2087)
HAnimJoint2088 = x3d.HAnimJoint()
HAnimJoint2088.USE = "STD_Joint_r_midcarpal_3"

HAnimHumanoid42.joints.append(HAnimJoint2088)
HAnimSegment2089 = x3d.HAnimSegment()
HAnimSegment2089.USE = "STD_Segment_r_capitate"

HAnimHumanoid42.segments.append(HAnimSegment2089)
HAnimJoint2090 = x3d.HAnimJoint()
HAnimJoint2090.USE = "STD_Joint_r_carpometacarpal_3"

HAnimHumanoid42.joints.append(HAnimJoint2090)
HAnimSite2091 = x3d.HAnimSite()
HAnimSite2091.USE = "STD_Site_r_metacarpal_phalanx_3_pt"

HAnimHumanoid42.sites.append(HAnimSite2091)
HAnimSegment2092 = x3d.HAnimSegment()
HAnimSegment2092.USE = "STD_Segment_r_metacarpal_3"

HAnimHumanoid42.segments.append(HAnimSegment2092)
HAnimJoint2093 = x3d.HAnimJoint()
HAnimJoint2093.USE = "STD_Joint_r_metacarpophalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint2093)
HAnimSegment2094 = x3d.HAnimSegment()
HAnimSegment2094.USE = "STD_Segment_r_carpal_proximal_phalanx_3"

HAnimHumanoid42.segments.append(HAnimSegment2094)
HAnimJoint2095 = x3d.HAnimJoint()
HAnimJoint2095.USE = "STD_Joint_r_carpal_proximal_interphalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint2095)
HAnimSegment2096 = x3d.HAnimSegment()
HAnimSegment2096.USE = "STD_Segment_r_carpal_middle_phalanx_3"

HAnimHumanoid42.segments.append(HAnimSegment2096)
HAnimJoint2097 = x3d.HAnimJoint()
HAnimJoint2097.USE = "STD_Joint_r_carpal_distal_interphalangeal_3"

HAnimHumanoid42.joints.append(HAnimJoint2097)
HAnimSite2098 = x3d.HAnimSite()
HAnimSite2098.USE = "STD_Site_r_carpal_distal_phalanx_3_tip"

HAnimHumanoid42.sites.append(HAnimSite2098)
HAnimSegment2099 = x3d.HAnimSegment()
HAnimSegment2099.USE = "STD_Segment_r_carpal_distal_phalanx_3"

HAnimHumanoid42.segments.append(HAnimSegment2099)
HAnimJoint2100 = x3d.HAnimJoint()
HAnimJoint2100.USE = "STD_Joint_r_midcarpal_4_5"

HAnimHumanoid42.joints.append(HAnimJoint2100)
HAnimSegment2101 = x3d.HAnimSegment()
HAnimSegment2101.USE = "STD_Segment_r_hamate"

HAnimHumanoid42.segments.append(HAnimSegment2101)
HAnimJoint2102 = x3d.HAnimJoint()
HAnimJoint2102.USE = "STD_Joint_r_carpometacarpal_4"

HAnimHumanoid42.joints.append(HAnimJoint2102)
HAnimSegment2103 = x3d.HAnimSegment()
HAnimSegment2103.USE = "STD_Segment_r_metacarpal_4"

HAnimHumanoid42.segments.append(HAnimSegment2103)
HAnimJoint2104 = x3d.HAnimJoint()
HAnimJoint2104.USE = "STD_Joint_r_metacarpophalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint2104)
HAnimSegment2105 = x3d.HAnimSegment()
HAnimSegment2105.USE = "STD_Segment_r_carpal_proximal_phalanx_4"

HAnimHumanoid42.segments.append(HAnimSegment2105)
HAnimJoint2106 = x3d.HAnimJoint()
HAnimJoint2106.USE = "STD_Joint_r_carpal_proximal_interphalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint2106)
HAnimSegment2107 = x3d.HAnimSegment()
HAnimSegment2107.USE = "STD_Segment_r_carpal_middle_phalanx_4"

HAnimHumanoid42.segments.append(HAnimSegment2107)
HAnimJoint2108 = x3d.HAnimJoint()
HAnimJoint2108.USE = "STD_Joint_r_carpal_distal_interphalangeal_4"

HAnimHumanoid42.joints.append(HAnimJoint2108)
HAnimSite2109 = x3d.HAnimSite()
HAnimSite2109.USE = "STD_Site_r_carpal_distal_phalanx_4_tip"

HAnimHumanoid42.sites.append(HAnimSite2109)
HAnimSegment2110 = x3d.HAnimSegment()
HAnimSegment2110.USE = "STD_Segment_r_carpal_distal_phalanx_4"

HAnimHumanoid42.segments.append(HAnimSegment2110)
HAnimJoint2111 = x3d.HAnimJoint()
HAnimJoint2111.USE = "STD_Joint_r_carpometacarpal_5"

HAnimHumanoid42.joints.append(HAnimJoint2111)
HAnimSite2112 = x3d.HAnimSite()
HAnimSite2112.USE = "STD_Site_r_metacarpal_phalanx_5_pt"

HAnimHumanoid42.sites.append(HAnimSite2112)
HAnimSegment2113 = x3d.HAnimSegment()
HAnimSegment2113.USE = "STD_Segment_r_metacarpal_5"

HAnimHumanoid42.segments.append(HAnimSegment2113)
HAnimJoint2114 = x3d.HAnimJoint()
HAnimJoint2114.USE = "STD_Joint_r_metacarpophalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint2114)
HAnimSegment2115 = x3d.HAnimSegment()
HAnimSegment2115.USE = "STD_Segment_r_carpal_proximal_phalanx_5"

HAnimHumanoid42.segments.append(HAnimSegment2115)
HAnimJoint2116 = x3d.HAnimJoint()
HAnimJoint2116.USE = "STD_Joint_r_carpal_proximal_interphalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint2116)
HAnimSegment2117 = x3d.HAnimSegment()
HAnimSegment2117.USE = "STD_Segment_r_carpal_middle_phalanx_5"

HAnimHumanoid42.segments.append(HAnimSegment2117)
HAnimJoint2118 = x3d.HAnimJoint()
HAnimJoint2118.USE = "STD_Joint_r_carpal_distal_interphalangeal_5"

HAnimHumanoid42.joints.append(HAnimJoint2118)
HAnimSite2119 = x3d.HAnimSite()
HAnimSite2119.USE = "STD_Site_r_carpal_distal_phalanx_5_tip"

HAnimHumanoid42.sites.append(HAnimSite2119)
HAnimSegment2120 = x3d.HAnimSegment()
HAnimSegment2120.USE = "STD_Segment_r_carpal_distal_phalanx_5"

HAnimHumanoid42.segments.append(HAnimSegment2120)

HAnimHumanoid10.skeleton.append(HAnimHumanoid10)

X3D0.Scene = Scene10
f = open("skeleton3_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
