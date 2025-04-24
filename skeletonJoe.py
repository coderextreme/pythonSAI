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
Viewpoint11 = x3d.Viewpoint()
Viewpoint11.centerOfRotation = [0,0,0]
Viewpoint11.description = "default"

Scene10.children.append(Viewpoint11)
Transform12 = x3d.Transform()
Transform12.scale = [1,1,1]
""" DEF for markerfor XYZ axes """
Shape13 = x3d.Shape()
Shape13.DEF = "AxisLinesShape"
""" RGB lines showing XYZ axes """
IndexedLineSet14 = x3d.IndexedLineSet()
IndexedLineSet14.colorIndex = [0,1,2]
IndexedLineSet14.colorPerVertex = False
IndexedLineSet14.coordIndex = [0,1,-1,0,2,-1,0,3,-1]
Coordinate15 = x3d.Coordinate()

IndexedLineSet14.coord = Coordinate15
Color16 = x3d.Color()

IndexedLineSet14.color = Color16

Shape13.geometry = IndexedLineSet14

Transform12.children.append(Shape13)

Scene10.children.append(Transform12)
Group17 = x3d.Group()
""" DEFS for markers of skeleton joints, segments, and sites """
Transform18 = x3d.Transform()
Transform18.translation = [0,0,0]
Transform18.scale = [1,1,1]
Transform19 = x3d.Transform()
Transform19.translation = [0,2,0]
Transform19.scale = [1,1,1]
Shape20 = x3d.Shape()
Shape20.DEF = "HAnimRootShape"
Sphere21 = x3d.Sphere()
Sphere21.radius = 0.02

Shape20.geometry = Sphere21
Appearance22 = x3d.Appearance()
Material23 = x3d.Material()
Material23.DEF = "HAnimRootMaterial"
Material23.diffuseColor = [0.8,0,0]
Material23.transparency = 0.3

Appearance22.material = Material23

Shape20.appearance = Appearance22

Transform19.children.append(Shape20)

Transform18.children.append(Transform19)
Transform24 = x3d.Transform()
Transform24.translation = [0,2.1,0]
Transform24.scale = [1,1,1]
Shape25 = x3d.Shape()
Shape25.DEF = "HAnimJointShape"
Sphere26 = x3d.Sphere()
Sphere26.radius = 0.02

Shape25.geometry = Sphere26
Appearance27 = x3d.Appearance()
Material28 = x3d.Material()
Material28.DEF = "HAnimJointMaterial"
Material28.diffuseColor = [0,0,0.8]
Material28.transparency = 0.3

Appearance27.material = Material28

Shape25.appearance = Appearance27

Transform24.children.append(Shape25)

Transform18.children.append(Transform24)
Transform29 = x3d.Transform()
Transform29.translation = [0,2.05,0]
Transform29.scale = [1,1,1]
Shape30 = x3d.Shape()
Shape30.DEF = "HAnimSegmentLine"
LineSet31 = x3d.LineSet()
LineSet31.vertexCount = [2]
ColorRGBA32 = x3d.ColorRGBA()
ColorRGBA32.DEF = "HAnimSegmentLineColorRGBA"

LineSet31.color = ColorRGBA32
Coordinate33 = x3d.Coordinate()

LineSet31.coord = Coordinate33

Shape30.geometry = LineSet31

Transform29.children.append(Shape30)

Transform18.children.append(Transform29)
Transform34 = x3d.Transform()
Transform34.translation = [0,2.1,0]
Transform34.scale = [1,1,1]
Shape35 = x3d.Shape()
Shape35.DEF = "HAnimSiteShape"
IndexedFaceSet36 = x3d.IndexedFaceSet()
IndexedFaceSet36.DEF = "DiamondIFS"
IndexedFaceSet36.creaseAngle = 0.5
IndexedFaceSet36.solid = False
IndexedFaceSet36.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
ColorRGBA37 = x3d.ColorRGBA()
ColorRGBA37.DEF = "HAnimSiteColorRGBA"

IndexedFaceSet36.color = ColorRGBA37
Coordinate38 = x3d.Coordinate()

IndexedFaceSet36.coord = Coordinate38

Shape35.geometry = IndexedFaceSet36
Appearance39 = x3d.Appearance()
Material40 = x3d.Material()
Material40.diffuseColor = [1,1,0]
Material40.transparency = 0.3

Appearance39.material = Material40

Shape35.appearance = Appearance39

Transform34.children.append(Shape35)

Transform18.children.append(Transform34)

Group17.children.append(Transform18)

Scene10.children.append(Group17)
NavigationInfo41 = x3d.NavigationInfo()
NavigationInfo41.speed = 1.5
NavigationInfo41.type = ["EXAMINE","ANY"]

Scene10.children.append(NavigationInfo41)
Viewpoint42 = x3d.Viewpoint()
Viewpoint42.centerOfRotation = [0,1,0]
Viewpoint42.description = "JohnBoy"
Viewpoint42.position = [0,1,3]

Scene10.children.append(Viewpoint42)
HAnimHumanoid43 = x3d.HAnimHumanoid()
HAnimHumanoid43.DEF = "STD_HAnim"
HAnimHumanoid43.info = ["humanoidVersion=2.0"]
HAnimHumanoid43.name = "HAnim"
HAnimHumanoid43.scale = [1,1,1]
HAnimHumanoid43.translation = [0,0,0]
HAnimHumanoid43.version = "2.0"
HAnimJoint44 = x3d.HAnimJoint()
HAnimJoint44.DEF = "STD_Joint_humanoid_root"
HAnimJoint44.name = "humanoid_root"
HAnimJoint44.center = [0.0000,0.8240,0.0277]
HAnimSegment45 = x3d.HAnimSegment()
HAnimSegment45.DEF = "STD_Segment_sacrum"
HAnimSegment45.name = "sacrum"

HAnimJoint44.children.append(HAnimSegment45)
HAnimJoint46 = x3d.HAnimJoint()
HAnimJoint46.DEF = "STD_Joint_sacroiliac"
HAnimJoint46.name = "sacroiliac"
HAnimJoint46.center = [0.0000,0.9149,0.0016]
HAnimSegment47 = x3d.HAnimSegment()
HAnimSegment47.DEF = "STD_Segment_pelvis"
HAnimSegment47.name = "pelvis"
HAnimSite48 = x3d.HAnimSite()
HAnimSite48.DEF = "STD_Site_r_iliocristale_pt"
HAnimSite48.name = "r_iliocristale_pt"
HAnimSite48.translation = [-0.1525,1.0628,0.0035]
TouchSensor49 = x3d.TouchSensor()
TouchSensor49.description = "HAnimSite r_iliocristale_pt"

HAnimSite48.children.append(TouchSensor49)
Shape50 = x3d.Shape()
Shape50.USE = "HAnimSiteShape"

HAnimSite48.children.append(Shape50)

HAnimSegment47.children.append(HAnimSite48)
HAnimSite51 = x3d.HAnimSite()
HAnimSite51.DEF = "STD_Site_l_iliocristale_pt"
HAnimSite51.name = "l_iliocristale_pt"
HAnimSite51.translation = [0.1612,1.0537,0.0008]
TouchSensor52 = x3d.TouchSensor()
TouchSensor52.description = "HAnimSite l_iliocristale_pt"

HAnimSite51.children.append(TouchSensor52)
Shape53 = x3d.Shape()
Shape53.USE = "HAnimSiteShape"

HAnimSite51.children.append(Shape53)

HAnimSegment47.children.append(HAnimSite51)
HAnimSite54 = x3d.HAnimSite()
HAnimSite54.DEF = "STD_Site_buttocks_standing_wall_contact_point_pt"
HAnimSite54.name = "buttocks_standing_wall_contact_point_pt"
TouchSensor55 = x3d.TouchSensor()
TouchSensor55.description = "HAnimSite buttocks_standing_wall_contact_point_pt"

HAnimSite54.children.append(TouchSensor55)
Shape56 = x3d.Shape()
Shape56.USE = "HAnimSiteShape"

HAnimSite54.children.append(Shape56)

HAnimSegment47.children.append(HAnimSite54)
HAnimSite57 = x3d.HAnimSite()
HAnimSite57.DEF = "STD_Site_crotch_pt"
HAnimSite57.name = "crotch_pt"
HAnimSite57.translation = [0.0034,0.8266,0.0257]
TouchSensor58 = x3d.TouchSensor()
TouchSensor58.description = "HAnimSite crotch_pt"

HAnimSite57.children.append(TouchSensor58)
Shape59 = x3d.Shape()
Shape59.USE = "HAnimSiteShape"

HAnimSite57.children.append(Shape59)

HAnimSegment47.children.append(HAnimSite57)
HAnimSite60 = x3d.HAnimSite()
HAnimSite60.DEF = "STD_Site_l_asis_pt"
HAnimSite60.name = "l_asis_pt"
HAnimSite60.translation = [0.0925,0.9983,0.1052]
TouchSensor61 = x3d.TouchSensor()
TouchSensor61.description = "HAnimSite l_asis_pt"

HAnimSite60.children.append(TouchSensor61)
Shape62 = x3d.Shape()
Shape62.USE = "HAnimSiteShape"

HAnimSite60.children.append(Shape62)

HAnimSegment47.children.append(HAnimSite60)
HAnimSite63 = x3d.HAnimSite()
HAnimSite63.DEF = "STD_Site_r_asis_pt"
HAnimSite63.name = "r_asis_pt"
HAnimSite63.translation = [-0.0887,1.0021,0.1112]
TouchSensor64 = x3d.TouchSensor()
TouchSensor64.description = "HAnimSite r_asis_pt"

HAnimSite63.children.append(TouchSensor64)
Shape65 = x3d.Shape()
Shape65.USE = "HAnimSiteShape"

HAnimSite63.children.append(Shape65)

HAnimSegment47.children.append(HAnimSite63)
HAnimSite66 = x3d.HAnimSite()
HAnimSite66.DEF = "STD_Site_l_trochanterion_pt"
HAnimSite66.name = "l_trochanterion_pt"
HAnimSite66.translation = [0.1677,0.8336,0.0303]
TouchSensor67 = x3d.TouchSensor()
TouchSensor67.description = "HAnimSite l_trochanterion_pt"

HAnimSite66.children.append(TouchSensor67)
Shape68 = x3d.Shape()
Shape68.USE = "HAnimSiteShape"

HAnimSite66.children.append(Shape68)

HAnimSegment47.children.append(HAnimSite66)
HAnimSite69 = x3d.HAnimSite()
HAnimSite69.DEF = "STD_Site_r_trochanterion_pt"
HAnimSite69.name = "r_trochanterion_pt"
HAnimSite69.translation = [-0.1689,0.8419,0.0352]
TouchSensor70 = x3d.TouchSensor()
TouchSensor70.description = "HAnimSite r_trochanterion_pt"

HAnimSite69.children.append(TouchSensor70)
Shape71 = x3d.Shape()
Shape71.USE = "HAnimSiteShape"

HAnimSite69.children.append(Shape71)

HAnimSegment47.children.append(HAnimSite69)
HAnimSite72 = x3d.HAnimSite()
HAnimSite72.DEF = "STD_Site_l_psis_pt"
HAnimSite72.name = "l_psis_pt"
HAnimSite72.translation = [0.0774,1.0190,-0.1151]
TouchSensor73 = x3d.TouchSensor()
TouchSensor73.description = "HAnimSite l_psis_pt"

HAnimSite72.children.append(TouchSensor73)
Shape74 = x3d.Shape()
Shape74.USE = "HAnimSiteShape"

HAnimSite72.children.append(Shape74)

HAnimSegment47.children.append(HAnimSite72)
HAnimSite75 = x3d.HAnimSite()
HAnimSite75.DEF = "STD_Site_r_psis_pt"
HAnimSite75.name = "r_psis_pt"
HAnimSite75.translation = [-0.0716,1.0190,-0.1138]
TouchSensor76 = x3d.TouchSensor()
TouchSensor76.description = "HAnimSite r_psis_pt"

HAnimSite75.children.append(TouchSensor76)
Shape77 = x3d.Shape()
Shape77.USE = "HAnimSiteShape"

HAnimSite75.children.append(Shape77)

HAnimSegment47.children.append(HAnimSite75)

HAnimJoint46.children.append(HAnimSegment47)
HAnimJoint78 = x3d.HAnimJoint()
HAnimJoint78.DEF = "STD_Joint_l_hip"
HAnimJoint78.name = "l_hip"
HAnimJoint78.center = [0.0961,0.9124,-0.0001]
HAnimSegment79 = x3d.HAnimSegment()
HAnimSegment79.DEF = "STD_Segment_l_thigh"
HAnimSegment79.name = "l_thigh"
HAnimSite80 = x3d.HAnimSite()
HAnimSite80.DEF = "STD_Site_l_suprapatella_pt"
HAnimSite80.name = "l_suprapatella_pt"
TouchSensor81 = x3d.TouchSensor()
TouchSensor81.description = "HAnimSite l_suprapatella_pt"

HAnimSite80.children.append(TouchSensor81)
Shape82 = x3d.Shape()
Shape82.USE = "HAnimSiteShape"

HAnimSite80.children.append(Shape82)

HAnimSegment79.children.append(HAnimSite80)
HAnimSite83 = x3d.HAnimSite()
HAnimSite83.DEF = "STD_Site_l_femoral_lateral_epicondyles_pt"
HAnimSite83.name = "l_femoral_lateral_epicondyles_pt"
HAnimSite83.translation = [0.1598,0.4967,0.0297]
TouchSensor84 = x3d.TouchSensor()
TouchSensor84.description = "HAnimSite l_femoral_lateral_epicondyles_pt"

HAnimSite83.children.append(TouchSensor84)
Shape85 = x3d.Shape()
Shape85.USE = "HAnimSiteShape"

HAnimSite83.children.append(Shape85)

HAnimSegment79.children.append(HAnimSite83)
HAnimSite86 = x3d.HAnimSite()
HAnimSite86.DEF = "STD_Site_l_femoral_medial_epicondyles_pt"
HAnimSite86.name = "l_femoral_medial_epicondyles_pt"
HAnimSite86.translation = [0.0398,0.4946,0.0303]
TouchSensor87 = x3d.TouchSensor()
TouchSensor87.description = "HAnimSite l_femoral_medial_epicondyles_pt"

HAnimSite86.children.append(TouchSensor87)
Shape88 = x3d.Shape()
Shape88.USE = "HAnimSiteShape"

HAnimSite86.children.append(Shape88)

HAnimSegment79.children.append(HAnimSite86)
HAnimSite89 = x3d.HAnimSite()
HAnimSite89.DEF = "STD_Site_l_knee_crease_pt"
HAnimSite89.name = "l_knee_crease_pt"
HAnimSite89.translation = [0.0993,0.4881,-0.0309]
TouchSensor90 = x3d.TouchSensor()
TouchSensor90.description = "HAnimSite l_knee_crease_pt"

HAnimSite89.children.append(TouchSensor90)
Shape91 = x3d.Shape()
Shape91.USE = "HAnimSiteShape"

HAnimSite89.children.append(Shape91)

HAnimSegment79.children.append(HAnimSite89)

HAnimJoint78.children.append(HAnimSegment79)
HAnimJoint92 = x3d.HAnimJoint()
HAnimJoint92.DEF = "STD_Joint_l_knee"
HAnimJoint92.name = "l_knee"
HAnimJoint92.center = [0.1040,0.4867,0.0308]
HAnimSegment93 = x3d.HAnimSegment()
HAnimSegment93.DEF = "STD_Segment_l_calf"
HAnimSegment93.name = "l_calf"
HAnimSite94 = x3d.HAnimSite()
HAnimSite94.DEF = "STD_Site_l_tibiale_pt"
HAnimSite94.name = "l_tibiale_pt"
TouchSensor95 = x3d.TouchSensor()
TouchSensor95.description = "HAnimSite l_tibiale_pt"

HAnimSite94.children.append(TouchSensor95)
Shape96 = x3d.Shape()
Shape96.USE = "HAnimSiteShape"

HAnimSite94.children.append(Shape96)

HAnimSegment93.children.append(HAnimSite94)
HAnimSite97 = x3d.HAnimSite()
HAnimSite97.DEF = "STD_Site_l_medial_malleolus_pt"
HAnimSite97.name = "l_medial_malleolus_pt"
HAnimSite97.translation = [0.0890,0.0716,-0.0881]
TouchSensor98 = x3d.TouchSensor()
TouchSensor98.description = "HAnimSite l_medial_malleolus_pt"

HAnimSite97.children.append(TouchSensor98)
Shape99 = x3d.Shape()
Shape99.USE = "HAnimSiteShape"

HAnimSite97.children.append(Shape99)

HAnimSegment93.children.append(HAnimSite97)
HAnimSite100 = x3d.HAnimSite()
HAnimSite100.DEF = "STD_Site_l_lateral_malleolus_pt"
HAnimSite100.name = "l_lateral_malleolus_pt"
HAnimSite100.translation = [0.1308,0.0597,-0.1032]
TouchSensor101 = x3d.TouchSensor()
TouchSensor101.description = "HAnimSite l_lateral_malleolus_pt"

HAnimSite100.children.append(TouchSensor101)
Shape102 = x3d.Shape()
Shape102.USE = "HAnimSiteShape"

HAnimSite100.children.append(Shape102)

HAnimSegment93.children.append(HAnimSite100)

HAnimJoint92.children.append(HAnimSegment93)
HAnimJoint103 = x3d.HAnimJoint()
HAnimJoint103.DEF = "STD_Joint_l_talocrural"
HAnimJoint103.name = "l_talocrural"
HAnimJoint103.center = [0.1101,0.0656,-0.0736]
HAnimSegment104 = x3d.HAnimSegment()
HAnimSegment104.DEF = "STD_Segment_l_talus"
HAnimSegment104.name = "l_talus"
HAnimSite105 = x3d.HAnimSite()
HAnimSite105.DEF = "STD_Site_l_sphyrion_pt"
HAnimSite105.name = "l_sphyrion_pt"
HAnimSite105.translation = [0.0890,0.0575,-0.0943]
TouchSensor106 = x3d.TouchSensor()
TouchSensor106.description = "HAnimSite l_sphyrion_pt"

HAnimSite105.children.append(TouchSensor106)
Shape107 = x3d.Shape()
Shape107.USE = "HAnimSiteShape"

HAnimSite105.children.append(Shape107)

HAnimSegment104.children.append(HAnimSite105)
HAnimSite108 = x3d.HAnimSite()
HAnimSite108.DEF = "STD_Site_l_calcaneus_posterior_pt"
HAnimSite108.name = "l_calcaneus_posterior_pt"
HAnimSite108.translation = [0.0974,0.0259,-0.1171]
TouchSensor109 = x3d.TouchSensor()
TouchSensor109.description = "HAnimSite l_calcaneus_posterior_pt"

HAnimSite108.children.append(TouchSensor109)
Shape110 = x3d.Shape()
Shape110.USE = "HAnimSiteShape"

HAnimSite108.children.append(Shape110)

HAnimSegment104.children.append(HAnimSite108)

HAnimJoint103.children.append(HAnimSegment104)
HAnimJoint111 = x3d.HAnimJoint()
HAnimJoint111.DEF = "STD_Joint_l_talocalcaneonavicular"
HAnimJoint111.name = "l_talocalcaneonavicular"
HAnimJoint111.center = [0,0,0]
HAnimSegment112 = x3d.HAnimSegment()
HAnimSegment112.DEF = "STD_Segment_l_navicular"
HAnimSegment112.name = "l_navicular"

HAnimJoint111.children.append(HAnimSegment112)
HAnimJoint113 = x3d.HAnimJoint()
HAnimJoint113.DEF = "STD_Joint_l_cuneonavicular_1"
HAnimJoint113.name = "l_cuneonavicular_1"
HAnimJoint113.center = [0,0,0]
HAnimSegment114 = x3d.HAnimSegment()
HAnimSegment114.DEF = "STD_Segment_l_cuneiform_1"
HAnimSegment114.name = "l_cuneiform_1"

HAnimJoint113.children.append(HAnimSegment114)
HAnimJoint115 = x3d.HAnimJoint()
HAnimJoint115.DEF = "STD_Joint_l_tarsometatarsal_1"
HAnimJoint115.name = "l_tarsometatarsal_1"
HAnimJoint115.center = [0,0,0]
HAnimSegment116 = x3d.HAnimSegment()
HAnimSegment116.DEF = "STD_Segment_l_metatarsal_1"
HAnimSegment116.name = "l_metatarsal_1"

HAnimJoint115.children.append(HAnimSegment116)
HAnimJoint117 = x3d.HAnimJoint()
HAnimJoint117.DEF = "STD_Joint_l_metatarsophalangeal_1"
HAnimJoint117.name = "l_metatarsophalangeal_1"
HAnimJoint117.center = [0,0,0]
HAnimSegment118 = x3d.HAnimSegment()
HAnimSegment118.DEF = "STD_Segment_l_tarsal_proximal_phalanx_1"
HAnimSegment118.name = "l_tarsal_proximal_phalanx_1"
HAnimSite119 = x3d.HAnimSite()
HAnimSite119.DEF = "STD_Site_l_metatarsal_phalanx_1_pt"
HAnimSite119.name = "l_metatarsal_phalanx_1_pt"
TouchSensor120 = x3d.TouchSensor()
TouchSensor120.description = "HAnimSite l_metatarsal_phalanx_1_pt"

HAnimSite119.children.append(TouchSensor120)
Shape121 = x3d.Shape()
Shape121.USE = "HAnimSiteShape"

HAnimSite119.children.append(Shape121)

HAnimSegment118.children.append(HAnimSite119)

HAnimJoint117.children.append(HAnimSegment118)
HAnimJoint122 = x3d.HAnimJoint()
HAnimJoint122.DEF = "STD_Joint_l_tarsal_interphalangeal_1"
HAnimJoint122.name = "l_tarsal_interphalangeal_1"
HAnimJoint122.center = [0,0,0]
HAnimSegment123 = x3d.HAnimSegment()
HAnimSegment123.DEF = "STD_Segment_l_tarsal_distal_phalanx_1"
HAnimSegment123.name = "l_tarsal_distal_phalanx_1"
HAnimSite124 = x3d.HAnimSite()
HAnimSite124.DEF = "STD_Site_l_tarsal_distal_phalanx_1_tip"
HAnimSite124.name = "l_tarsal_distal_phalanx_1_tip"
TouchSensor125 = x3d.TouchSensor()
TouchSensor125.description = "HAnimSite l_tarsal_distal_phalanx_1_tip"

HAnimSite124.children.append(TouchSensor125)
Shape126 = x3d.Shape()
Shape126.USE = "HAnimSiteShape"

HAnimSite124.children.append(Shape126)

HAnimSegment123.children.append(HAnimSite124)

HAnimJoint122.children.append(HAnimSegment123)

HAnimJoint117.children.append(HAnimJoint122)

HAnimJoint115.children.append(HAnimJoint117)

HAnimJoint113.children.append(HAnimJoint115)

HAnimJoint111.children.append(HAnimJoint113)
HAnimJoint127 = x3d.HAnimJoint()
HAnimJoint127.DEF = "STD_Joint_l_cuneonavicular_2"
HAnimJoint127.name = "l_cuneonavicular_2"
HAnimJoint127.center = [0,0,0]
HAnimSegment128 = x3d.HAnimSegment()
HAnimSegment128.DEF = "STD_Segment_l_cuneiform_2"
HAnimSegment128.name = "l_cuneiform_2"

HAnimJoint127.children.append(HAnimSegment128)
HAnimJoint129 = x3d.HAnimJoint()
HAnimJoint129.DEF = "STD_Joint_l_tarsometatarsal_2"
HAnimJoint129.name = "l_tarsometatarsal_2"
HAnimJoint129.center = [0,0,0]
HAnimSegment130 = x3d.HAnimSegment()
HAnimSegment130.DEF = "STD_Segment_l_metatarsal_2"
HAnimSegment130.name = "l_metatarsal_2"

HAnimJoint129.children.append(HAnimSegment130)
HAnimJoint131 = x3d.HAnimJoint()
HAnimJoint131.DEF = "STD_Joint_l_metatarsophalangeal_2"
HAnimJoint131.name = "l_metatarsophalangeal_2"
HAnimJoint131.center = [0,0,0]
HAnimSegment132 = x3d.HAnimSegment()
HAnimSegment132.DEF = "STD_Segment_l_tarsal_proximal_phalanx_2"
HAnimSegment132.name = "l_tarsal_proximal_phalanx_2"

HAnimJoint131.children.append(HAnimSegment132)
HAnimJoint133 = x3d.HAnimJoint()
HAnimJoint133.DEF = "STD_Joint_l_tarsal_proximal_interphalangeal_2"
HAnimJoint133.name = "l_tarsal_proximal_interphalangeal_2"
HAnimJoint133.center = [0,0,0]
HAnimSegment134 = x3d.HAnimSegment()
HAnimSegment134.DEF = "STD_Segment_l_tarsal_middle_phalanx_2"
HAnimSegment134.name = "l_tarsal_middle_phalanx_2"

HAnimJoint133.children.append(HAnimSegment134)
HAnimJoint135 = x3d.HAnimJoint()
HAnimJoint135.DEF = "STD_Joint_l_tarsal_distal_interphalangeal_2"
HAnimJoint135.name = "l_tarsal_distal_interphalangeal_2"
HAnimJoint135.center = [0,0,0]
HAnimSegment136 = x3d.HAnimSegment()
HAnimSegment136.DEF = "STD_Segment_l_tarsal_distal_phalanx_2"
HAnimSegment136.name = "l_tarsal_distal_phalanx_2"
HAnimSite137 = x3d.HAnimSite()
HAnimSite137.DEF = "STD_Site_l_tarsal_distal_phalanx_2_tip"
HAnimSite137.name = "l_tarsal_distal_phalanx_2_tip"
HAnimSite137.translation = [0.1195,0.0079,0.1433]
TouchSensor138 = x3d.TouchSensor()
TouchSensor138.description = "HAnimSite l_tarsal_distal_phalanx_2_tip"

HAnimSite137.children.append(TouchSensor138)
Shape139 = x3d.Shape()
Shape139.USE = "HAnimSiteShape"

HAnimSite137.children.append(Shape139)

HAnimSegment136.children.append(HAnimSite137)

HAnimJoint135.children.append(HAnimSegment136)

HAnimJoint133.children.append(HAnimJoint135)

HAnimJoint131.children.append(HAnimJoint133)

HAnimJoint129.children.append(HAnimJoint131)

HAnimJoint127.children.append(HAnimJoint129)

HAnimJoint111.children.append(HAnimJoint127)
HAnimJoint140 = x3d.HAnimJoint()
HAnimJoint140.DEF = "STD_Joint_l_cuneonavicular_3"
HAnimJoint140.name = "l_cuneonavicular_3"
HAnimJoint140.center = [0,0,0]
HAnimSegment141 = x3d.HAnimSegment()
HAnimSegment141.DEF = "STD_Segment_l_cuneiform_3"
HAnimSegment141.name = "l_cuneiform_3"

HAnimJoint140.children.append(HAnimSegment141)
HAnimJoint142 = x3d.HAnimJoint()
HAnimJoint142.DEF = "STD_Joint_l_tarsometatarsal_3 "
HAnimJoint142.name = "l_tarsometatarsal_3 "
HAnimJoint142.center = [0,0,0]
HAnimSegment143 = x3d.HAnimSegment()
HAnimSegment143.DEF = "STD_Segment_l_metatarsal_3"
HAnimSegment143.name = "l_metatarsal_3"

HAnimJoint142.children.append(HAnimSegment143)
HAnimJoint144 = x3d.HAnimJoint()
HAnimJoint144.DEF = "STD_Joint_l_metatarsophalangeal_3"
HAnimJoint144.name = "l_metatarsophalangeal_3"
HAnimJoint144.center = [0,0,0]
HAnimSegment145 = x3d.HAnimSegment()
HAnimSegment145.DEF = "STD_Segment_l_tarsal_proximal_phalanx_3"
HAnimSegment145.name = "l_tarsal_proximal_phalanx_3"

HAnimJoint144.children.append(HAnimSegment145)
HAnimJoint146 = x3d.HAnimJoint()
HAnimJoint146.DEF = "STD_Joint_l_tarsal_proximal_interphalangeal_3"
HAnimJoint146.name = "l_tarsal_proximal_interphalangeal_3"
HAnimJoint146.center = [0,0,0]
HAnimSegment147 = x3d.HAnimSegment()
HAnimSegment147.DEF = "STD_Segment_l_tarsal_middle_phalanx_3"
HAnimSegment147.name = "l_tarsal_middle_phalanx_3"

HAnimJoint146.children.append(HAnimSegment147)
HAnimJoint148 = x3d.HAnimJoint()
HAnimJoint148.DEF = "STD_Joint_l_tarsal_distal_interphalangeal_3"
HAnimJoint148.name = "l_tarsal_distal_interphalangeal_3"
HAnimJoint148.center = [0,0,0]
HAnimSegment149 = x3d.HAnimSegment()
HAnimSegment149.DEF = "STD_Segment_l_tarsal_distal_phalanx_3"
HAnimSegment149.name = "l_tarsal_distal_phalanx_3"
HAnimSite150 = x3d.HAnimSite()
HAnimSite150.DEF = "STD_Site_l_tarsal_distal_phalanx_3_tip"
HAnimSite150.name = "l_tarsal_distal_phalanx_3_tip"
TouchSensor151 = x3d.TouchSensor()
TouchSensor151.description = "HAnimSite l_tarsal_distal_phalanx_3_tip"

HAnimSite150.children.append(TouchSensor151)
Shape152 = x3d.Shape()
Shape152.USE = "HAnimSiteShape"

HAnimSite150.children.append(Shape152)

HAnimSegment149.children.append(HAnimSite150)

HAnimJoint148.children.append(HAnimSegment149)

HAnimJoint146.children.append(HAnimJoint148)

HAnimJoint144.children.append(HAnimJoint146)

HAnimJoint142.children.append(HAnimJoint144)

HAnimJoint140.children.append(HAnimJoint142)

HAnimJoint111.children.append(HAnimJoint140)

HAnimJoint103.children.append(HAnimJoint111)
HAnimJoint153 = x3d.HAnimJoint()
HAnimJoint153.DEF = "STD_Joint_l_calcaneocuboid"
HAnimJoint153.name = "l_calcaneocuboid"
HAnimJoint153.center = [0,0,0]
HAnimSegment154 = x3d.HAnimSegment()
HAnimSegment154.DEF = "STD_Segment_l_calcaneus"
HAnimSegment154.name = "l_calcaneus"

HAnimJoint153.children.append(HAnimSegment154)
HAnimJoint155 = x3d.HAnimJoint()
HAnimJoint155.DEF = "STD_Joint_l_transversetarsal"
HAnimJoint155.name = "l_transversetarsal"
HAnimJoint155.center = [0,0,0]
HAnimSegment156 = x3d.HAnimSegment()
HAnimSegment156.DEF = "STD_Segment_l_cuboid"
HAnimSegment156.name = "l_cuboid"

HAnimJoint155.children.append(HAnimSegment156)
HAnimJoint157 = x3d.HAnimJoint()
HAnimJoint157.DEF = "STD_Joint_l_tarsometatarsal_4"
HAnimJoint157.name = "l_tarsometatarsal_4"
HAnimJoint157.center = [0,0,0]
HAnimSegment158 = x3d.HAnimSegment()
HAnimSegment158.DEF = "STD_Segment_l_metatarsal_4"
HAnimSegment158.name = "l_metatarsal_4"

HAnimJoint157.children.append(HAnimSegment158)
HAnimJoint159 = x3d.HAnimJoint()
HAnimJoint159.DEF = "STD_Joint_l_metatarsophalangeal_4"
HAnimJoint159.name = "l_metatarsophalangeal_4"
HAnimJoint159.center = [0,0,0]
HAnimSegment160 = x3d.HAnimSegment()
HAnimSegment160.DEF = "STD_Segment_l_tarsal_proximal_phalanx_4"
HAnimSegment160.name = "l_tarsal_proximal_phalanx_4"

HAnimJoint159.children.append(HAnimSegment160)
HAnimJoint161 = x3d.HAnimJoint()
HAnimJoint161.DEF = "STD_Joint_l_tarsal_proximal_interphalangeal_4"
HAnimJoint161.name = "l_tarsal_proximal_interphalangeal_4"
HAnimJoint161.center = [0,0,0]
HAnimSegment162 = x3d.HAnimSegment()
HAnimSegment162.DEF = "STD_Segment_l_tarsal_middle_phalanx_4"
HAnimSegment162.name = "l_tarsal_middle_phalanx_4"

HAnimJoint161.children.append(HAnimSegment162)
HAnimJoint163 = x3d.HAnimJoint()
HAnimJoint163.DEF = "STD_Joint_l_tarsal_distal_interphalangeal_4"
HAnimJoint163.name = "l_tarsal_distal_interphalangeal_4"
HAnimJoint163.center = [0,0,0]
HAnimSegment164 = x3d.HAnimSegment()
HAnimSegment164.DEF = "STD_Segment_l_tarsal_distal_phalanx_4"
HAnimSegment164.name = "l_tarsal_distal_phalanx_4"
HAnimSite165 = x3d.HAnimSite()
HAnimSite165.DEF = "STD_Site_l_tarsal_distal_phalanx_4_tip"
HAnimSite165.name = "l_tarsal_distal_phalanx_4_tip"
TouchSensor166 = x3d.TouchSensor()
TouchSensor166.description = "HAnimSite l_tarsal_distal_phalanx_4_tip"

HAnimSite165.children.append(TouchSensor166)
Shape167 = x3d.Shape()
Shape167.USE = "HAnimSiteShape"

HAnimSite165.children.append(Shape167)

HAnimSegment164.children.append(HAnimSite165)

HAnimJoint163.children.append(HAnimSegment164)

HAnimJoint161.children.append(HAnimJoint163)

HAnimJoint159.children.append(HAnimJoint161)

HAnimJoint157.children.append(HAnimJoint159)

HAnimJoint155.children.append(HAnimJoint157)
HAnimJoint168 = x3d.HAnimJoint()
HAnimJoint168.DEF = "STD_Joint_l_tarsometatarsal_5"
HAnimJoint168.name = "l_tarsometatarsal_5"
HAnimJoint168.center = [0,0,0]
HAnimSegment169 = x3d.HAnimSegment()
HAnimSegment169.DEF = "STD_Segment_l_metatarsal_5"
HAnimSegment169.name = "l_metatarsal_5"

HAnimJoint168.children.append(HAnimSegment169)
HAnimJoint170 = x3d.HAnimJoint()
HAnimJoint170.DEF = "STD_Joint_l_metatarsophalangeal_5"
HAnimJoint170.name = "l_metatarsophalangeal_5"
HAnimJoint170.center = [0,0,0]
HAnimSegment171 = x3d.HAnimSegment()
HAnimSegment171.DEF = "STD_Segment_l_tarsal_proximal_phalanx_5"
HAnimSegment171.name = "l_tarsal_proximal_phalanx_5"
HAnimSite172 = x3d.HAnimSite()
HAnimSite172.DEF = "STD_Site_l_metatarsal_phalanx_5_pt"
HAnimSite172.name = "l_metatarsal_phalanx_5_pt"
TouchSensor173 = x3d.TouchSensor()
TouchSensor173.description = "HAnimSite l_metatarsal_phalanx_5_pt"

HAnimSite172.children.append(TouchSensor173)
Shape174 = x3d.Shape()
Shape174.USE = "HAnimSiteShape"

HAnimSite172.children.append(Shape174)

HAnimSegment171.children.append(HAnimSite172)

HAnimJoint170.children.append(HAnimSegment171)
HAnimJoint175 = x3d.HAnimJoint()
HAnimJoint175.DEF = "STD_Joint_l_tarsal_proximal_interphalangeal_5"
HAnimJoint175.name = "l_tarsal_proximal_interphalangeal_5"
HAnimJoint175.center = [0,0,0]
HAnimSegment176 = x3d.HAnimSegment()
HAnimSegment176.DEF = "STD_Segment_l_tarsal_middle_phalanx_5"
HAnimSegment176.name = "l_tarsal_middle_phalanx_5"

HAnimJoint175.children.append(HAnimSegment176)
HAnimJoint177 = x3d.HAnimJoint()
HAnimJoint177.DEF = "STD_Joint_l_tarsal_distal_interphalangeal_5"
HAnimJoint177.name = "l_tarsal_distal_interphalangeal_5"
HAnimJoint177.center = [0,0,0]
HAnimSegment178 = x3d.HAnimSegment()
HAnimSegment178.DEF = "STD_Segment_l_tarsal_distal_phalanx_5"
HAnimSegment178.name = "l_tarsal_distal_phalanx_5"
HAnimSite179 = x3d.HAnimSite()
HAnimSite179.DEF = "STD_Site_l_tarsal_distal_phalanx_5_tip"
HAnimSite179.name = "l_tarsal_distal_phalanx_5_tip"
TouchSensor180 = x3d.TouchSensor()
TouchSensor180.description = "HAnimSite l_tarsal_distal_phalanx_5_tip"

HAnimSite179.children.append(TouchSensor180)
Shape181 = x3d.Shape()
Shape181.USE = "HAnimSiteShape"

HAnimSite179.children.append(Shape181)

HAnimSegment178.children.append(HAnimSite179)

HAnimJoint177.children.append(HAnimSegment178)

HAnimJoint175.children.append(HAnimJoint177)

HAnimJoint170.children.append(HAnimJoint175)

HAnimJoint168.children.append(HAnimJoint170)

HAnimJoint155.children.append(HAnimJoint168)

HAnimJoint153.children.append(HAnimJoint155)

HAnimJoint103.children.append(HAnimJoint153)

HAnimJoint92.children.append(HAnimJoint103)

HAnimJoint78.children.append(HAnimJoint92)

HAnimJoint46.children.append(HAnimJoint78)
HAnimJoint182 = x3d.HAnimJoint()
HAnimJoint182.DEF = "STD_Joint_r_hip"
HAnimJoint182.name = "r_hip"
HAnimJoint182.center = [-0.0950,0.9171,0.0029]
HAnimSegment183 = x3d.HAnimSegment()
HAnimSegment183.DEF = "STD_Segment_r_thigh"
HAnimSegment183.name = "r_thigh"
HAnimSite184 = x3d.HAnimSite()
HAnimSite184.DEF = "STD_Site_r_femoral_lateral_epicondyles_pt"
HAnimSite184.name = "r_femoral_lateral_epicondyles_pt"
HAnimSite184.translation = [-0.1421,0.4992,0.0310]
TouchSensor185 = x3d.TouchSensor()
TouchSensor185.description = "HAnimSite r_femoral_lateral_epicondyles_pt"

HAnimSite184.children.append(TouchSensor185)
Shape186 = x3d.Shape()
Shape186.USE = "HAnimSiteShape"

HAnimSite184.children.append(Shape186)

HAnimSegment183.children.append(HAnimSite184)
HAnimSite187 = x3d.HAnimSite()
HAnimSite187.DEF = "STD_Site_r_femoral_medial_epicondyles_pt"
HAnimSite187.name = "r_femoral_medial_epicondyles_pt"
HAnimSite187.translation = [-0.0221,0.5014,0.0289]
TouchSensor188 = x3d.TouchSensor()
TouchSensor188.description = "HAnimSite r_femoral_medial_epicondyles_pt"

HAnimSite187.children.append(TouchSensor188)
Shape189 = x3d.Shape()
Shape189.USE = "HAnimSiteShape"

HAnimSite187.children.append(Shape189)

HAnimSegment183.children.append(HAnimSite187)
HAnimSite190 = x3d.HAnimSite()
HAnimSite190.DEF = "STD_Site_r_suprapatella_pt"
HAnimSite190.name = "r_suprapatella_pt"
TouchSensor191 = x3d.TouchSensor()
TouchSensor191.description = "HAnimSite r_suprapatella_pt"

HAnimSite190.children.append(TouchSensor191)
Shape192 = x3d.Shape()
Shape192.USE = "HAnimSiteShape"

HAnimSite190.children.append(Shape192)

HAnimSegment183.children.append(HAnimSite190)
HAnimSite193 = x3d.HAnimSite()
HAnimSite193.DEF = "STD_Site_r_knee_crease_pt"
HAnimSite193.name = "r_knee_crease_pt"
HAnimSite193.translation = [-0.0825,0.4932,-0.0326]
TouchSensor194 = x3d.TouchSensor()
TouchSensor194.description = "HAnimSite r_knee_crease_pt"

HAnimSite193.children.append(TouchSensor194)
Shape195 = x3d.Shape()
Shape195.USE = "HAnimSiteShape"

HAnimSite193.children.append(Shape195)

HAnimSegment183.children.append(HAnimSite193)

HAnimJoint182.children.append(HAnimSegment183)
HAnimJoint196 = x3d.HAnimJoint()
HAnimJoint196.DEF = "STD_Joint_r_knee"
HAnimJoint196.name = "r_knee"
HAnimJoint196.center = [-0.0867,0.4913,0.0318]
HAnimSegment197 = x3d.HAnimSegment()
HAnimSegment197.DEF = "STD_Segment_r_calf"
HAnimSegment197.name = "r_calf"
HAnimSite198 = x3d.HAnimSite()
HAnimSite198.DEF = "STD_Site_r_tibiale_pt"
HAnimSite198.name = "r_tibiale_pt"
TouchSensor199 = x3d.TouchSensor()
TouchSensor199.description = "HAnimSite r_tibiale_pt"

HAnimSite198.children.append(TouchSensor199)
Shape200 = x3d.Shape()
Shape200.USE = "HAnimSiteShape"

HAnimSite198.children.append(Shape200)

HAnimSegment197.children.append(HAnimSite198)
HAnimSite201 = x3d.HAnimSite()
HAnimSite201.DEF = "STD_Site_r_medial_malleolus_pt"
HAnimSite201.name = "r_medial_malleolus_pt"
HAnimSite201.translation = [-0.0591,0.0760,-0.0928]
TouchSensor202 = x3d.TouchSensor()
TouchSensor202.description = "HAnimSite r_medial_malleolus_pt"

HAnimSite201.children.append(TouchSensor202)
Shape203 = x3d.Shape()
Shape203.USE = "HAnimSiteShape"

HAnimSite201.children.append(Shape203)

HAnimSegment197.children.append(HAnimSite201)
HAnimSite204 = x3d.HAnimSite()
HAnimSite204.DEF = "STD_Site_r_lateral_malleolus_pt"
HAnimSite204.name = "r_lateral_malleolus_pt"
HAnimSite204.translation = [-0.1006,0.0658,-0.1075]
TouchSensor205 = x3d.TouchSensor()
TouchSensor205.description = "HAnimSite r_lateral_malleolus_pt"

HAnimSite204.children.append(TouchSensor205)
Shape206 = x3d.Shape()
Shape206.USE = "HAnimSiteShape"

HAnimSite204.children.append(Shape206)

HAnimSegment197.children.append(HAnimSite204)

HAnimJoint196.children.append(HAnimSegment197)
HAnimJoint207 = x3d.HAnimJoint()
HAnimJoint207.DEF = "STD_Joint_r_talocrural"
HAnimJoint207.name = "r_talocrural"
HAnimJoint207.center = [-0.0801,0.0712,-0.0766]
HAnimSegment208 = x3d.HAnimSegment()
HAnimSegment208.DEF = "STD_Segment_r_talus"
HAnimSegment208.name = "r_talus"
HAnimSite209 = x3d.HAnimSite()
HAnimSite209.DEF = "STD_Site_r_sphyrion_pt"
HAnimSite209.name = "r_sphyrion_pt"
HAnimSite209.translation = [-0.0603,0.0610,-0.1002]
TouchSensor210 = x3d.TouchSensor()
TouchSensor210.description = "HAnimSite r_sphyrion_pt"

HAnimSite209.children.append(TouchSensor210)
Shape211 = x3d.Shape()
Shape211.USE = "HAnimSiteShape"

HAnimSite209.children.append(Shape211)

HAnimSegment208.children.append(HAnimSite209)
HAnimSite212 = x3d.HAnimSite()
HAnimSite212.DEF = "STD_Site_r_calcaneus_posterior_pt"
HAnimSite212.name = "r_calcaneus_posterior_pt"
HAnimSite212.translation = [-0.0692,0.0297,-0.1221]
TouchSensor213 = x3d.TouchSensor()
TouchSensor213.description = "HAnimSite r_calcaneus_posterior_pt"

HAnimSite212.children.append(TouchSensor213)
Shape214 = x3d.Shape()
Shape214.USE = "HAnimSiteShape"

HAnimSite212.children.append(Shape214)

HAnimSegment208.children.append(HAnimSite212)

HAnimJoint207.children.append(HAnimSegment208)
HAnimJoint215 = x3d.HAnimJoint()
HAnimJoint215.DEF = "STD_Joint_r_talocalcaneonavicular"
HAnimJoint215.name = "r_talocalcaneonavicular"
HAnimJoint215.center = [0,0,0]
HAnimSegment216 = x3d.HAnimSegment()
HAnimSegment216.DEF = "STD_Segment_r_navicular"
HAnimSegment216.name = "r_navicular"

HAnimJoint215.children.append(HAnimSegment216)
HAnimJoint217 = x3d.HAnimJoint()
HAnimJoint217.DEF = "STD_Joint_r_cuneonavicular_1"
HAnimJoint217.name = "r_cuneonavicular_1"
HAnimJoint217.center = [0,0,0]
HAnimSegment218 = x3d.HAnimSegment()
HAnimSegment218.DEF = "STD_Segment_r_cuneiform_1"
HAnimSegment218.name = "r_cuneiform_1"

HAnimJoint217.children.append(HAnimSegment218)
HAnimJoint219 = x3d.HAnimJoint()
HAnimJoint219.DEF = "STD_Joint_r_tarsometatarsal_1"
HAnimJoint219.name = "r_tarsometatarsal_1"
HAnimJoint219.center = [0,0,0]
HAnimSegment220 = x3d.HAnimSegment()
HAnimSegment220.DEF = "STD_Segment_r_metatarsal_1"
HAnimSegment220.name = "r_metatarsal_1"

HAnimJoint219.children.append(HAnimSegment220)
HAnimJoint221 = x3d.HAnimJoint()
HAnimJoint221.DEF = "STD_Joint_r_metatarsophalangeal_1"
HAnimJoint221.name = "r_metatarsophalangeal_1"
HAnimJoint221.center = [0,0,0]
HAnimSegment222 = x3d.HAnimSegment()
HAnimSegment222.DEF = "STD_Segment_r_tarsal_proximal_phalanx_1"
HAnimSegment222.name = "r_tarsal_proximal_phalanx_1"
HAnimSite223 = x3d.HAnimSite()
HAnimSite223.DEF = "STD_Site_r_metatarsal_phalanx_1_pt"
HAnimSite223.name = "r_metatarsal_phalanx_1_pt"
TouchSensor224 = x3d.TouchSensor()
TouchSensor224.description = "HAnimSite r_metatarsal_phalanx_1_pt"

HAnimSite223.children.append(TouchSensor224)
Shape225 = x3d.Shape()
Shape225.USE = "HAnimSiteShape"

HAnimSite223.children.append(Shape225)

HAnimSegment222.children.append(HAnimSite223)

HAnimJoint221.children.append(HAnimSegment222)
HAnimJoint226 = x3d.HAnimJoint()
HAnimJoint226.DEF = "STD_Joint_r_tarsal_interphalangeal_1"
HAnimJoint226.name = "r_tarsal_interphalangeal_1"
HAnimJoint226.center = [0,0,0]
HAnimSegment227 = x3d.HAnimSegment()
HAnimSegment227.DEF = "STD_Segment_r_tarsal_distal_phalanx_1"
HAnimSegment227.name = "r_tarsal_distal_phalanx_1"
HAnimSite228 = x3d.HAnimSite()
HAnimSite228.DEF = "STD_Site_r_tarsal_distal_phalanx_1_tip"
HAnimSite228.name = "r_tarsal_distal_phalanx_1_tip"
TouchSensor229 = x3d.TouchSensor()
TouchSensor229.description = "HAnimSite r_tarsal_distal_phalanx_1_tip"

HAnimSite228.children.append(TouchSensor229)
Shape230 = x3d.Shape()
Shape230.USE = "HAnimSiteShape"

HAnimSite228.children.append(Shape230)

HAnimSegment227.children.append(HAnimSite228)

HAnimJoint226.children.append(HAnimSegment227)

HAnimJoint221.children.append(HAnimJoint226)

HAnimJoint219.children.append(HAnimJoint221)

HAnimJoint217.children.append(HAnimJoint219)

HAnimJoint215.children.append(HAnimJoint217)
HAnimJoint231 = x3d.HAnimJoint()
HAnimJoint231.DEF = "STD_Joint_r_cuneonavicular_2"
HAnimJoint231.name = "r_cuneonavicular_2"
HAnimJoint231.center = [0,0,0]
HAnimSegment232 = x3d.HAnimSegment()
HAnimSegment232.DEF = "STD_Segment_r_cuneiform_2"
HAnimSegment232.name = "r_cuneiform_2"

HAnimJoint231.children.append(HAnimSegment232)
HAnimJoint233 = x3d.HAnimJoint()
HAnimJoint233.DEF = "STD_Joint_r_tarsometatarsal_2"
HAnimJoint233.name = "r_tarsometatarsal_2"
HAnimJoint233.center = [0,0,0]
HAnimSegment234 = x3d.HAnimSegment()
HAnimSegment234.DEF = "STD_Segment_r_metatarsal_2"
HAnimSegment234.name = "r_metatarsal_2"

HAnimJoint233.children.append(HAnimSegment234)
HAnimJoint235 = x3d.HAnimJoint()
HAnimJoint235.DEF = "STD_Joint_r_metatarsophalangeal_2"
HAnimJoint235.name = "r_metatarsophalangeal_2"
HAnimJoint235.center = [0,0,0]
HAnimSegment236 = x3d.HAnimSegment()
HAnimSegment236.DEF = "STD_Segment_r_tarsal_proximal_phalanx_2"
HAnimSegment236.name = "r_tarsal_proximal_phalanx_2"

HAnimJoint235.children.append(HAnimSegment236)
HAnimJoint237 = x3d.HAnimJoint()
HAnimJoint237.DEF = "STD_Joint_r_tarsal_proximal_interphalangeal_2"
HAnimJoint237.name = "r_tarsal_proximal_interphalangeal_2"
HAnimJoint237.center = [0,0,0]
HAnimSegment238 = x3d.HAnimSegment()
HAnimSegment238.DEF = "STD_Segment_r_tarsal_middle_phalanx_2"
HAnimSegment238.name = "r_tarsal_middle_phalanx_2"

HAnimJoint237.children.append(HAnimSegment238)
HAnimJoint239 = x3d.HAnimJoint()
HAnimJoint239.DEF = "STD_Joint_r_tarsal_distal_interphalangeal_2"
HAnimJoint239.name = "r_tarsal_distal_interphalangeal_2"
HAnimJoint239.center = [0,0,0]
HAnimSegment240 = x3d.HAnimSegment()
HAnimSegment240.DEF = "STD_Segment_r_tarsal_distal_phalanx_2"
HAnimSegment240.name = "r_tarsal_distal_phalanx_2"
HAnimSite241 = x3d.HAnimSite()
HAnimSite241.DEF = "STD_Site_r_tarsal_distal_phalanx_2_tip"
HAnimSite241.name = "r_tarsal_distal_phalanx_2_tip"
HAnimSite241.translation = [-0.0883,0.0134,0.1383]
TouchSensor242 = x3d.TouchSensor()
TouchSensor242.description = "HAnimSite r_tarsal_distal_phalanx_2_tip"

HAnimSite241.children.append(TouchSensor242)
Shape243 = x3d.Shape()
Shape243.USE = "HAnimSiteShape"

HAnimSite241.children.append(Shape243)

HAnimSegment240.children.append(HAnimSite241)

HAnimJoint239.children.append(HAnimSegment240)

HAnimJoint237.children.append(HAnimJoint239)

HAnimJoint235.children.append(HAnimJoint237)

HAnimJoint233.children.append(HAnimJoint235)

HAnimJoint231.children.append(HAnimJoint233)

HAnimJoint215.children.append(HAnimJoint231)
HAnimJoint244 = x3d.HAnimJoint()
HAnimJoint244.DEF = "STD_Joint_r_cuneonavicular_3"
HAnimJoint244.name = "r_cuneonavicular_3"
HAnimJoint244.center = [0,0,0]
HAnimSegment245 = x3d.HAnimSegment()
HAnimSegment245.DEF = "STD_Segment_r_cuneiform_3"
HAnimSegment245.name = "r_cuneiform_3"

HAnimJoint244.children.append(HAnimSegment245)
HAnimJoint246 = x3d.HAnimJoint()
HAnimJoint246.DEF = "STD_Joint_r_tarsometatarsal_3 "
HAnimJoint246.name = "r_tarsometatarsal_3 "
HAnimJoint246.center = [0,0,0]
HAnimSegment247 = x3d.HAnimSegment()
HAnimSegment247.DEF = "STD_Segment_r_metatarsal_3"
HAnimSegment247.name = "r_metatarsal_3"

HAnimJoint246.children.append(HAnimSegment247)
HAnimJoint248 = x3d.HAnimJoint()
HAnimJoint248.DEF = "STD_Joint_r_metatarsophalangeal_3"
HAnimJoint248.name = "r_metatarsophalangeal_3"
HAnimJoint248.center = [0,0,0]
HAnimSegment249 = x3d.HAnimSegment()
HAnimSegment249.DEF = "STD_Segment_r_tarsal_proximal_phalanx_3"
HAnimSegment249.name = "r_tarsal_proximal_phalanx_3"

HAnimJoint248.children.append(HAnimSegment249)
HAnimJoint250 = x3d.HAnimJoint()
HAnimJoint250.DEF = "STD_Joint_r_tarsal_proximal_interphalangeal_3"
HAnimJoint250.name = "r_tarsal_proximal_interphalangeal_3"
HAnimJoint250.center = [0,0,0]
HAnimSegment251 = x3d.HAnimSegment()
HAnimSegment251.DEF = "STD_Segment_r_tarsal_middle_phalanx_3"
HAnimSegment251.name = "r_tarsal_middle_phalanx_3"

HAnimJoint250.children.append(HAnimSegment251)
HAnimJoint252 = x3d.HAnimJoint()
HAnimJoint252.DEF = "STD_Joint_r_tarsal_distal_interphalangeal_3"
HAnimJoint252.name = "r_tarsal_distal_interphalangeal_3"
HAnimJoint252.center = [0,0,0]
HAnimSegment253 = x3d.HAnimSegment()
HAnimSegment253.DEF = "STD_Segment_r_tarsal_distal_phalanx_3"
HAnimSegment253.name = "r_tarsal_distal_phalanx_3"
HAnimSite254 = x3d.HAnimSite()
HAnimSite254.DEF = "STD_Site_r_tarsal_distal_phalanx_3_tip"
HAnimSite254.name = "r_tarsal_distal_phalanx_3_tip"
TouchSensor255 = x3d.TouchSensor()
TouchSensor255.description = "HAnimSite r_tarsal_distal_phalanx_3_tip"

HAnimSite254.children.append(TouchSensor255)
Shape256 = x3d.Shape()
Shape256.USE = "HAnimSiteShape"

HAnimSite254.children.append(Shape256)

HAnimSegment253.children.append(HAnimSite254)

HAnimJoint252.children.append(HAnimSegment253)

HAnimJoint250.children.append(HAnimJoint252)

HAnimJoint248.children.append(HAnimJoint250)

HAnimJoint246.children.append(HAnimJoint248)

HAnimJoint244.children.append(HAnimJoint246)

HAnimJoint215.children.append(HAnimJoint244)

HAnimJoint207.children.append(HAnimJoint215)
HAnimJoint257 = x3d.HAnimJoint()
HAnimJoint257.DEF = "STD_Joint_r_calcaneocuboid"
HAnimJoint257.name = "r_calcaneocuboid"
HAnimJoint257.center = [0,0,0]
HAnimSegment258 = x3d.HAnimSegment()
HAnimSegment258.DEF = "STD_Segment_r_calcaneus"
HAnimSegment258.name = "r_calcaneus"

HAnimJoint257.children.append(HAnimSegment258)
HAnimJoint259 = x3d.HAnimJoint()
HAnimJoint259.DEF = "STD_Joint_r_transversetarsal"
HAnimJoint259.name = "r_transversetarsal"
HAnimJoint259.center = [0,0,0]
HAnimSegment260 = x3d.HAnimSegment()
HAnimSegment260.DEF = "STD_Segment_r_cuboid"
HAnimSegment260.name = "r_cuboid"

HAnimJoint259.children.append(HAnimSegment260)
HAnimJoint261 = x3d.HAnimJoint()
HAnimJoint261.DEF = "STD_Joint_r_tarsometatarsal_4"
HAnimJoint261.name = "r_tarsometatarsal_4"
HAnimJoint261.center = [0,0,0]
HAnimSegment262 = x3d.HAnimSegment()
HAnimSegment262.DEF = "STD_Segment_r_metatarsal_4"
HAnimSegment262.name = "r_metatarsal_4"

HAnimJoint261.children.append(HAnimSegment262)
HAnimJoint263 = x3d.HAnimJoint()
HAnimJoint263.DEF = "STD_Joint_r_metatarsophalangeal_4"
HAnimJoint263.name = "r_metatarsophalangeal_4"
HAnimJoint263.center = [0,0,0]
HAnimSegment264 = x3d.HAnimSegment()
HAnimSegment264.DEF = "STD_Segment_r_tarsal_proximal_phalanx_4"
HAnimSegment264.name = "r_tarsal_proximal_phalanx_4"

HAnimJoint263.children.append(HAnimSegment264)
HAnimJoint265 = x3d.HAnimJoint()
HAnimJoint265.DEF = "STD_Joint_r_tarsal_proximal_interphalangeal_4"
HAnimJoint265.name = "r_tarsal_proximal_interphalangeal_4"
HAnimJoint265.center = [0,0,0]
HAnimSegment266 = x3d.HAnimSegment()
HAnimSegment266.DEF = "STD_Segment_r_tarsal_middle_phalanx_4"
HAnimSegment266.name = "r_tarsal_middle_phalanx_4"

HAnimJoint265.children.append(HAnimSegment266)
HAnimJoint267 = x3d.HAnimJoint()
HAnimJoint267.DEF = "STD_Joint_r_tarsal_distal_interphalangeal_4"
HAnimJoint267.name = "r_tarsal_distal_interphalangeal_4"
HAnimJoint267.center = [0,0,0]
HAnimSegment268 = x3d.HAnimSegment()
HAnimSegment268.DEF = "STD_Segment_r_tarsal_distal_phalanx_4"
HAnimSegment268.name = "r_tarsal_distal_phalanx_4"
HAnimSite269 = x3d.HAnimSite()
HAnimSite269.DEF = "STD_Site_r_tarsal_distal_phalanx_4_tip"
HAnimSite269.name = "r_tarsal_distal_phalanx_4_tip"
TouchSensor270 = x3d.TouchSensor()
TouchSensor270.description = "HAnimSite r_tarsal_distal_phalanx_4_tip"

HAnimSite269.children.append(TouchSensor270)
Shape271 = x3d.Shape()
Shape271.USE = "HAnimSiteShape"

HAnimSite269.children.append(Shape271)

HAnimSegment268.children.append(HAnimSite269)

HAnimJoint267.children.append(HAnimSegment268)

HAnimJoint265.children.append(HAnimJoint267)

HAnimJoint263.children.append(HAnimJoint265)

HAnimJoint261.children.append(HAnimJoint263)

HAnimJoint259.children.append(HAnimJoint261)
HAnimJoint272 = x3d.HAnimJoint()
HAnimJoint272.DEF = "STD_Joint_r_tarsometatarsal_5"
HAnimJoint272.name = "r_tarsometatarsal_5"
HAnimJoint272.center = [0,0,0]
HAnimSegment273 = x3d.HAnimSegment()
HAnimSegment273.DEF = "STD_Segment_r_metatarsal_5"
HAnimSegment273.name = "r_metatarsal_5"

HAnimJoint272.children.append(HAnimSegment273)
HAnimJoint274 = x3d.HAnimJoint()
HAnimJoint274.DEF = "STD_Joint_r_metatarsophalangeal_5"
HAnimJoint274.name = "r_metatarsophalangeal_5"
HAnimJoint274.center = [0,0,0]
HAnimSegment275 = x3d.HAnimSegment()
HAnimSegment275.DEF = "STD_Segment_r_tarsal_proximal_phalanx_5"
HAnimSegment275.name = "r_tarsal_proximal_phalanx_5"
HAnimSite276 = x3d.HAnimSite()
HAnimSite276.DEF = "STD_Site_r_metatarsal_phalanx_5_pt"
HAnimSite276.name = "r_metatarsal_phalanx_5_pt"
TouchSensor277 = x3d.TouchSensor()
TouchSensor277.description = "HAnimSite r_metatarsal_phalanx_5_pt"

HAnimSite276.children.append(TouchSensor277)
Shape278 = x3d.Shape()
Shape278.USE = "HAnimSiteShape"

HAnimSite276.children.append(Shape278)

HAnimSegment275.children.append(HAnimSite276)

HAnimJoint274.children.append(HAnimSegment275)
HAnimJoint279 = x3d.HAnimJoint()
HAnimJoint279.DEF = "STD_Joint_r_tarsal_proximal_interphalangeal_5"
HAnimJoint279.name = "r_tarsal_proximal_interphalangeal_5"
HAnimJoint279.center = [0,0,0]
HAnimSegment280 = x3d.HAnimSegment()
HAnimSegment280.DEF = "STD_Segment_r_tarsal_middle_phalanx_5"
HAnimSegment280.name = "r_tarsal_middle_phalanx_5"

HAnimJoint279.children.append(HAnimSegment280)
HAnimJoint281 = x3d.HAnimJoint()
HAnimJoint281.DEF = "STD_Joint_r_tarsal_distal_interphalangeal_5"
HAnimJoint281.name = "r_tarsal_distal_interphalangeal_5"
HAnimJoint281.center = [0,0,0]
HAnimSegment282 = x3d.HAnimSegment()
HAnimSegment282.DEF = "STD_Segment_r_tarsal_distal_phalanx_5"
HAnimSegment282.name = "r_tarsal_distal_phalanx_5"
HAnimSite283 = x3d.HAnimSite()
HAnimSite283.DEF = "STD_Site_r_tarsal_distal_phalanx_5_tip"
HAnimSite283.name = "r_tarsal_distal_phalanx_5_tip"
TouchSensor284 = x3d.TouchSensor()
TouchSensor284.description = "HAnimSite r_tarsal_distal_phalanx_5_tip"

HAnimSite283.children.append(TouchSensor284)
Shape285 = x3d.Shape()
Shape285.USE = "HAnimSiteShape"

HAnimSite283.children.append(Shape285)

HAnimSegment282.children.append(HAnimSite283)

HAnimJoint281.children.append(HAnimSegment282)

HAnimJoint279.children.append(HAnimJoint281)

HAnimJoint274.children.append(HAnimJoint279)

HAnimJoint272.children.append(HAnimJoint274)

HAnimJoint259.children.append(HAnimJoint272)

HAnimJoint257.children.append(HAnimJoint259)

HAnimJoint207.children.append(HAnimJoint257)

HAnimJoint196.children.append(HAnimJoint207)

HAnimJoint182.children.append(HAnimJoint196)

HAnimJoint46.children.append(HAnimJoint182)

HAnimJoint44.children.append(HAnimJoint46)
HAnimJoint286 = x3d.HAnimJoint()
HAnimJoint286.DEF = "STD_Joint_vl5"
HAnimJoint286.name = "vl5"
HAnimJoint286.center = [0.0028,1.0568,-0.0776]
HAnimSegment287 = x3d.HAnimSegment()
HAnimSegment287.DEF = "STD_Segment_l5"
HAnimSegment287.name = "l5"
HAnimSite288 = x3d.HAnimSite()
HAnimSite288.DEF = "STD_Site_waist_preferred_anterior_pt"
HAnimSite288.name = "waist_preferred_anterior_pt"
TouchSensor289 = x3d.TouchSensor()
TouchSensor289.description = "HAnimSite waist_preferred_anterior_pt"

HAnimSite288.children.append(TouchSensor289)
Shape290 = x3d.Shape()
Shape290.USE = "HAnimSiteShape"

HAnimSite288.children.append(Shape290)

HAnimSegment287.children.append(HAnimSite288)
HAnimSite291 = x3d.HAnimSite()
HAnimSite291.DEF = "STD_Site_waist_preferred_posterior_pt"
HAnimSite291.name = "waist_preferred_posterior_pt"
HAnimSite291.translation = [0.2900,1.0915,-0.1091]
TouchSensor292 = x3d.TouchSensor()
TouchSensor292.description = "HAnimSite waist_preferred_posterior_pt"

HAnimSite291.children.append(TouchSensor292)
Shape293 = x3d.Shape()
Shape293.USE = "HAnimSiteShape"

HAnimSite291.children.append(Shape293)

HAnimSegment287.children.append(HAnimSite291)
HAnimSite294 = x3d.HAnimSite()
HAnimSite294.DEF = "STD_Site_navel_pt"
HAnimSite294.name = "navel_pt"
HAnimSite294.translation = [0.0069,1.0966,0.1017]
TouchSensor295 = x3d.TouchSensor()
TouchSensor295.description = "HAnimSite navel_pt"

HAnimSite294.children.append(TouchSensor295)
Shape296 = x3d.Shape()
Shape296.USE = "HAnimSiteShape"

HAnimSite294.children.append(Shape296)

HAnimSegment287.children.append(HAnimSite294)

HAnimJoint286.children.append(HAnimSegment287)
HAnimJoint297 = x3d.HAnimJoint()
HAnimJoint297.DEF = "STD_Joint_vl4"
HAnimJoint297.name = "vl4"
HAnimJoint297.center = [0.0035,1.0925,-0.0787]
HAnimSegment298 = x3d.HAnimSegment()
HAnimSegment298.DEF = "STD_Segment_l4"
HAnimSegment298.name = "l4"

HAnimJoint297.children.append(HAnimSegment298)
HAnimJoint299 = x3d.HAnimJoint()
HAnimJoint299.DEF = "STD_Joint_vl3"
HAnimJoint299.name = "vl3"
HAnimJoint299.center = [0.0041,1.1276,-0.0796]
HAnimSegment300 = x3d.HAnimSegment()
HAnimSegment300.DEF = "STD_Segment_l3"
HAnimSegment300.name = "l3"

HAnimJoint299.children.append(HAnimSegment300)
HAnimJoint301 = x3d.HAnimJoint()
HAnimJoint301.DEF = "STD_Joint_vl2"
HAnimJoint301.name = "vl2"
HAnimJoint301.center = [0.0045,1.1546,-0.0800]
HAnimSegment302 = x3d.HAnimSegment()
HAnimSegment302.DEF = "STD_Segment_l2"
HAnimSegment302.name = "l2"
HAnimSite303 = x3d.HAnimSite()
HAnimSite303.DEF = "STD_Site_spine_2_middle_back_pt"
HAnimSite303.name = "spine_2_middle_back_pt"
TouchSensor304 = x3d.TouchSensor()
TouchSensor304.description = "HAnimSite spine_2_middle_back_pt"

HAnimSite303.children.append(TouchSensor304)
Shape305 = x3d.Shape()
Shape305.USE = "HAnimSiteShape"

HAnimSite303.children.append(Shape305)

HAnimSegment302.children.append(HAnimSite303)
HAnimSite306 = x3d.HAnimSite()
HAnimSite306.DEF = "STD_Site_r_rib10_pt"
HAnimSite306.name = "r_rib10_pt"
HAnimSite306.translation = [-0.0711,1.1941,0.1016]
TouchSensor307 = x3d.TouchSensor()
TouchSensor307.description = "HAnimSite r_rib10_pt"

HAnimSite306.children.append(TouchSensor307)
Shape308 = x3d.Shape()
Shape308.USE = "HAnimSiteShape"

HAnimSite306.children.append(Shape308)

HAnimSegment302.children.append(HAnimSite306)
HAnimSite309 = x3d.HAnimSite()
HAnimSite309.DEF = "STD_Site_l_rib10_pt"
HAnimSite309.name = "l_rib10_pt"
HAnimSite309.translation = [0.0871,1.1925,0.0992]
TouchSensor310 = x3d.TouchSensor()
TouchSensor310.description = "HAnimSite l_rib10_pt"

HAnimSite309.children.append(TouchSensor310)
Shape311 = x3d.Shape()
Shape311.USE = "HAnimSiteShape"

HAnimSite309.children.append(Shape311)

HAnimSegment302.children.append(HAnimSite309)

HAnimJoint301.children.append(HAnimSegment302)
HAnimJoint312 = x3d.HAnimJoint()
HAnimJoint312.DEF = "STD_Joint_vl1"
HAnimJoint312.name = "vl1"
HAnimJoint312.center = [0.0048,1.1912,-0.0805]
HAnimSegment313 = x3d.HAnimSegment()
HAnimSegment313.DEF = "STD_Segment_l1"
HAnimSegment313.name = "l1"

HAnimJoint312.children.append(HAnimSegment313)
HAnimJoint314 = x3d.HAnimJoint()
HAnimJoint314.DEF = "STD_Joint_vt12"
HAnimJoint314.name = "vt12"
HAnimJoint314.center = [0.0051,1.2278,-0.0808]
HAnimSegment315 = x3d.HAnimSegment()
HAnimSegment315.DEF = "STD_Segment_t12"
HAnimSegment315.name = "t12"

HAnimJoint314.children.append(HAnimSegment315)
HAnimJoint316 = x3d.HAnimJoint()
HAnimJoint316.DEF = "STD_Joint_vt11"
HAnimJoint316.name = "vt11"
HAnimJoint316.center = [0.0053,1.2679,-0.0810]
HAnimSegment317 = x3d.HAnimSegment()
HAnimSegment317.DEF = "STD_Segment_t11"
HAnimSegment317.name = "t11"

HAnimJoint316.children.append(HAnimSegment317)
HAnimJoint318 = x3d.HAnimJoint()
HAnimJoint318.DEF = "STD_Joint_vt10"
HAnimJoint318.name = "vt10"
HAnimJoint318.center = [0.0056,1.2848,-0.0822]
HAnimSegment319 = x3d.HAnimSegment()
HAnimSegment319.DEF = "STD_Segment_t10"
HAnimSegment319.name = "t10"
HAnimSite320 = x3d.HAnimSite()
HAnimSite320.DEF = "STD_Site_substernale_pt"
HAnimSite320.name = "substernale_pt"
HAnimSite320.translation = [0.0085,1.2995,0.1147]
TouchSensor321 = x3d.TouchSensor()
TouchSensor321.description = "HAnimSite substernale_pt"

HAnimSite320.children.append(TouchSensor321)
Shape322 = x3d.Shape()
Shape322.USE = "HAnimSiteShape"

HAnimSite320.children.append(Shape322)

HAnimSegment319.children.append(HAnimSite320)

HAnimJoint318.children.append(HAnimSegment319)
HAnimJoint323 = x3d.HAnimJoint()
HAnimJoint323.DEF = "STD_Joint_vt9"
HAnimJoint323.name = "vt9"
HAnimJoint323.center = [0.0057,1.3126,-0.0838]
HAnimSegment324 = x3d.HAnimSegment()
HAnimSegment324.DEF = "STD_Segment_t9"
HAnimSegment324.name = "t9"
HAnimSite325 = x3d.HAnimSite()
HAnimSite325.DEF = "STD_Site_r_thelion_pt"
HAnimSite325.name = "r_thelion_pt"
HAnimSite325.translation = [-0.0736,1.3385,0.1217]
TouchSensor326 = x3d.TouchSensor()
TouchSensor326.description = "HAnimSite r_thelion_pt"

HAnimSite325.children.append(TouchSensor326)
Shape327 = x3d.Shape()
Shape327.USE = "HAnimSiteShape"

HAnimSite325.children.append(Shape327)

HAnimSegment324.children.append(HAnimSite325)
HAnimSite328 = x3d.HAnimSite()
HAnimSite328.DEF = "STD_Site_l_thelion_pt"
HAnimSite328.name = "l_thelion_pt"
HAnimSite328.translation = [0.0918,1.3382,0.1192]
TouchSensor329 = x3d.TouchSensor()
TouchSensor329.description = "HAnimSite l_thelion_pt"

HAnimSite328.children.append(TouchSensor329)
Shape330 = x3d.Shape()
Shape330.USE = "HAnimSiteShape"

HAnimSite328.children.append(Shape330)

HAnimSegment324.children.append(HAnimSite328)

HAnimJoint323.children.append(HAnimSegment324)
HAnimJoint331 = x3d.HAnimJoint()
HAnimJoint331.DEF = "STD_Joint_vt8"
HAnimJoint331.name = "vt8"
HAnimJoint331.center = [0.0057,1.3382,-0.0845]
HAnimSegment332 = x3d.HAnimSegment()
HAnimSegment332.DEF = "STD_Segment_t8"
HAnimSegment332.name = "t8"

HAnimJoint331.children.append(HAnimSegment332)
HAnimJoint333 = x3d.HAnimJoint()
HAnimJoint333.DEF = "STD_Joint_vt7"
HAnimJoint333.name = "vt7"
HAnimJoint333.center = [0.0058,1.3625,-0.0833]
HAnimSegment334 = x3d.HAnimSegment()
HAnimSegment334.DEF = "STD_Segment_t7"
HAnimSegment334.name = "t7"

HAnimJoint333.children.append(HAnimSegment334)
HAnimJoint335 = x3d.HAnimJoint()
HAnimJoint335.DEF = "STD_Joint_vt6"
HAnimJoint335.name = "vt6"
HAnimJoint335.center = [0.0059,1.3866,-0.0800]
HAnimSegment336 = x3d.HAnimSegment()
HAnimSegment336.DEF = "STD_Segment_t6"
HAnimSegment336.name = "t6"
HAnimSite337 = x3d.HAnimSite()
HAnimSite337.DEF = "STD_Site_r_chest_midsagittal_plane_pt"
HAnimSite337.name = "r_chest_midsagittal_plane_pt"
TouchSensor338 = x3d.TouchSensor()
TouchSensor338.description = "HAnimSite r_chest_midsagittal_plane_pt"

HAnimSite337.children.append(TouchSensor338)
Shape339 = x3d.Shape()
Shape339.USE = "HAnimSiteShape"

HAnimSite337.children.append(Shape339)

HAnimSegment336.children.append(HAnimSite337)
HAnimSite340 = x3d.HAnimSite()
HAnimSite340.DEF = "STD_Site_l_chest_midsagittal_plane_pt"
HAnimSite340.name = "l_chest_midsagittal_plane_pt"
TouchSensor341 = x3d.TouchSensor()
TouchSensor341.description = "HAnimSite l_chest_midsagittal_plane_pt"

HAnimSite340.children.append(TouchSensor341)
Shape342 = x3d.Shape()
Shape342.USE = "HAnimSiteShape"

HAnimSite340.children.append(Shape342)

HAnimSegment336.children.append(HAnimSite340)
HAnimSite343 = x3d.HAnimSite()
HAnimSite343.DEF = "STD_Site_rear_center_midsagittal_plane_pt"
HAnimSite343.name = "rear_center_midsagittal_plane_pt"
TouchSensor344 = x3d.TouchSensor()
TouchSensor344.description = "HAnimSite rear_center_midsagittal_plane_pt"

HAnimSite343.children.append(TouchSensor344)
Shape345 = x3d.Shape()
Shape345.USE = "HAnimSiteShape"

HAnimSite343.children.append(Shape345)

HAnimSegment336.children.append(HAnimSite343)
HAnimSite346 = x3d.HAnimSite()
HAnimSite346.DEF = "STD_Site_mesosternale_pt"
HAnimSite346.name = "mesosternale_pt"
TouchSensor347 = x3d.TouchSensor()
TouchSensor347.description = "HAnimSite mesosternale_pt"

HAnimSite346.children.append(TouchSensor347)
Shape348 = x3d.Shape()
Shape348.USE = "HAnimSiteShape"

HAnimSite346.children.append(Shape348)

HAnimSegment336.children.append(HAnimSite346)

HAnimJoint335.children.append(HAnimSegment336)
HAnimJoint349 = x3d.HAnimJoint()
HAnimJoint349.DEF = "STD_Joint_vt5"
HAnimJoint349.name = "vt5"
HAnimJoint349.center = [0.0060,1.4102,-0.0745]
HAnimSegment350 = x3d.HAnimSegment()
HAnimSegment350.DEF = "STD_Segment_t5"
HAnimSegment350.name = "t5"
HAnimSite351 = x3d.HAnimSite()
HAnimSite351.DEF = "STD_Site_spine_1_middle_back_pt"
HAnimSite351.name = "spine_1_middle_back_pt"
TouchSensor352 = x3d.TouchSensor()
TouchSensor352.description = "HAnimSite spine_1_middle_back_pt"

HAnimSite351.children.append(TouchSensor352)
Shape353 = x3d.Shape()
Shape353.USE = "HAnimSiteShape"

HAnimSite351.children.append(Shape353)

HAnimSegment350.children.append(HAnimSite351)

HAnimJoint349.children.append(HAnimSegment350)
HAnimJoint354 = x3d.HAnimJoint()
HAnimJoint354.DEF = "STD_Joint_vt4"
HAnimJoint354.name = "vt4"
HAnimJoint354.center = [0.0061,1.4320,-0.0675]
HAnimSegment355 = x3d.HAnimSegment()
HAnimSegment355.DEF = "STD_Segment_t4"
HAnimSegment355.name = "t4"

HAnimJoint354.children.append(HAnimSegment355)
HAnimJoint356 = x3d.HAnimJoint()
HAnimJoint356.DEF = "STD_Joint_vt3"
HAnimJoint356.name = "vt3"
HAnimJoint356.center = [0.0062,1.4583,-0.0570]
HAnimSegment357 = x3d.HAnimSegment()
HAnimSegment357.DEF = "STD_Segment_t3"
HAnimSegment357.name = "t3"

HAnimJoint356.children.append(HAnimSegment357)
HAnimJoint358 = x3d.HAnimJoint()
HAnimJoint358.DEF = "STD_Joint_vt2"
HAnimJoint358.name = "vt2"
HAnimJoint358.center = [0.0063,1.4761,-0.0484]
HAnimSegment359 = x3d.HAnimSegment()
HAnimSegment359.DEF = "STD_Segment_t2"
HAnimSegment359.name = "t2"

HAnimJoint358.children.append(HAnimSegment359)
HAnimJoint360 = x3d.HAnimJoint()
HAnimJoint360.DEF = "STD_Joint_vt1"
HAnimJoint360.name = "vt1"
HAnimJoint360.center = [0.0065,1.4951,-0.0387]
HAnimSegment361 = x3d.HAnimSegment()
HAnimSegment361.DEF = "STD_Segment_t1"
HAnimSegment361.name = "t1"
HAnimSite362 = x3d.HAnimSite()
HAnimSite362.DEF = "STD_Site_cervicale_pt"
HAnimSite362.name = "cervicale_pt"
HAnimSite362.translation = [0.0064,1.520,-0.0815]
TouchSensor363 = x3d.TouchSensor()
TouchSensor363.description = "HAnimSite cervicale_pt"

HAnimSite362.children.append(TouchSensor363)
Shape364 = x3d.Shape()
Shape364.USE = "HAnimSiteShape"

HAnimSite362.children.append(Shape364)

HAnimSegment361.children.append(HAnimSite362)
HAnimSite365 = x3d.HAnimSite()
HAnimSite365.DEF = "STD_Site_suprasternale_pt"
HAnimSite365.name = "suprasternale_pt"
HAnimSite365.translation = [0.0084,1.4714,0.0551]
TouchSensor366 = x3d.TouchSensor()
TouchSensor366.description = "HAnimSite suprasternale_pt"

HAnimSite365.children.append(TouchSensor366)
Shape367 = x3d.Shape()
Shape367.USE = "HAnimSiteShape"

HAnimSite365.children.append(Shape367)

HAnimSegment361.children.append(HAnimSite365)

HAnimJoint360.children.append(HAnimSegment361)
HAnimJoint368 = x3d.HAnimJoint()
HAnimJoint368.DEF = "STD_Joint_vc7"
HAnimJoint368.name = "vc7"
HAnimJoint368.center = [0.0066,1.5132,-0.0301]
HAnimSegment369 = x3d.HAnimSegment()
HAnimSegment369.DEF = "STD_Segment_c7"
HAnimSegment369.name = "c7"
HAnimSite370 = x3d.HAnimSite()
HAnimSite370.DEF = "STD_Site_l_neck_base_pt"
HAnimSite370.name = "l_neck_base_pt"
HAnimSite370.translation = [0.0646,1.5141,-0.0380]
TouchSensor371 = x3d.TouchSensor()
TouchSensor371.description = "HAnimSite l_neck_base_pt"

HAnimSite370.children.append(TouchSensor371)
Shape372 = x3d.Shape()
Shape372.USE = "HAnimSiteShape"

HAnimSite370.children.append(Shape372)

HAnimSegment369.children.append(HAnimSite370)
HAnimSite373 = x3d.HAnimSite()
HAnimSite373.DEF = "STD_Site_r_neck_base_pt"
HAnimSite373.name = "r_neck_base_pt"
HAnimSite373.translation = [-0.0419,1.5149,-0.0220]
TouchSensor374 = x3d.TouchSensor()
TouchSensor374.description = "HAnimSite r_neck_base_pt"

HAnimSite373.children.append(TouchSensor374)
Shape375 = x3d.Shape()
Shape375.USE = "HAnimSiteShape"

HAnimSite373.children.append(Shape375)

HAnimSegment369.children.append(HAnimSite373)

HAnimJoint368.children.append(HAnimSegment369)
HAnimJoint376 = x3d.HAnimJoint()
HAnimJoint376.DEF = "STD_Joint_vc6"
HAnimJoint376.name = "vc6"
HAnimJoint376.center = [0.0066,1.5357,-0.0143]
HAnimSegment377 = x3d.HAnimSegment()
HAnimSegment377.DEF = "STD_Segment_c6"
HAnimSegment377.name = "c6"

HAnimJoint376.children.append(HAnimSegment377)
HAnimJoint378 = x3d.HAnimJoint()
HAnimJoint378.DEF = "STD_Joint_vc5"
HAnimJoint378.name = "vc5"
HAnimJoint378.center = [0.0066,1.5520,-0.0082]
HAnimSegment379 = x3d.HAnimSegment()
HAnimSegment379.DEF = "STD_Segment_c5"
HAnimSegment379.name = "c5"

HAnimJoint378.children.append(HAnimSegment379)
HAnimJoint380 = x3d.HAnimJoint()
HAnimJoint380.DEF = "STD_Joint_vc4"
HAnimJoint380.name = "vc4"
HAnimJoint380.center = [0.0066,1.5662,-0.0084]
HAnimSegment381 = x3d.HAnimSegment()
HAnimSegment381.DEF = "STD_Segment_c4"
HAnimSegment381.name = "c4"

HAnimJoint380.children.append(HAnimSegment381)
HAnimJoint382 = x3d.HAnimJoint()
HAnimJoint382.DEF = "STD_Joint_vc3"
HAnimJoint382.name = "vc3"
HAnimJoint382.center = [0.0066,1.5800,-0.0103]
HAnimSegment383 = x3d.HAnimSegment()
HAnimSegment383.DEF = "STD_Segment_c3"
HAnimSegment383.name = "c3"

HAnimJoint382.children.append(HAnimSegment383)
HAnimJoint384 = x3d.HAnimJoint()
HAnimJoint384.DEF = "STD_Joint_vc2"
HAnimJoint384.name = "vc2"
HAnimJoint384.center = [0.0066,1.5928,-0.0103]
HAnimSegment385 = x3d.HAnimSegment()
HAnimSegment385.DEF = "STD_Segment_c2"
HAnimSegment385.name = "c2"
HAnimSite386 = x3d.HAnimSite()
HAnimSite386.DEF = "STD_Site_adams_apple_pt"
HAnimSite386.name = "adams_apple_pt"
TouchSensor387 = x3d.TouchSensor()
TouchSensor387.description = "HAnimSite adams_apple_pt"

HAnimSite386.children.append(TouchSensor387)
Shape388 = x3d.Shape()
Shape388.USE = "HAnimSiteShape"

HAnimSite386.children.append(Shape388)

HAnimSegment385.children.append(HAnimSite386)

HAnimJoint384.children.append(HAnimSegment385)
HAnimJoint389 = x3d.HAnimJoint()
HAnimJoint389.DEF = "STD_Joint_vc1"
HAnimJoint389.name = "vc1"
HAnimJoint389.center = [0.0066,1.6144,-0.0034]
HAnimSegment390 = x3d.HAnimSegment()
HAnimSegment390.DEF = "STD_Segment_c1"
HAnimSegment390.name = "c1"

HAnimJoint389.children.append(HAnimSegment390)
HAnimJoint391 = x3d.HAnimJoint()
HAnimJoint391.DEF = "STD_Joint_skullbase"
HAnimJoint391.name = "skullbase"
HAnimJoint391.center = [0.0044,1.6209,0.0236]
HAnimSegment392 = x3d.HAnimSegment()
HAnimSegment392.DEF = "STD_Segment_skull"
HAnimSegment392.name = "skull"
HAnimSite393 = x3d.HAnimSite()
HAnimSite393.DEF = "STD_Site_glabella_pt"
HAnimSite393.name = "glabella_pt"
TouchSensor394 = x3d.TouchSensor()
TouchSensor394.description = "HAnimSite glabella_pt"

HAnimSite393.children.append(TouchSensor394)
Shape395 = x3d.Shape()
Shape395.USE = "HAnimSiteShape"

HAnimSite393.children.append(Shape395)

HAnimSegment392.children.append(HAnimSite393)
HAnimSite396 = x3d.HAnimSite()
HAnimSite396.DEF = "STD_Site_sellion_pt"
HAnimSite396.name = "sellion_pt"
HAnimSite396.translation = [0.0058,1.6316,0.0852]
TouchSensor397 = x3d.TouchSensor()
TouchSensor397.description = "HAnimSite sellion_pt"

HAnimSite396.children.append(TouchSensor397)
Shape398 = x3d.Shape()
Shape398.USE = "HAnimSiteShape"

HAnimSite396.children.append(Shape398)

HAnimSegment392.children.append(HAnimSite396)
HAnimSite399 = x3d.HAnimSite()
HAnimSite399.DEF = "STD_Site_r_tragion_pt"
HAnimSite399.name = "r_tragion_pt"
HAnimSite399.translation = [-0.0646,1.6347,0.0302]
TouchSensor400 = x3d.TouchSensor()
TouchSensor400.description = "HAnimSite r_tragion_pt"

HAnimSite399.children.append(TouchSensor400)
Shape401 = x3d.Shape()
Shape401.USE = "HAnimSiteShape"

HAnimSite399.children.append(Shape401)

HAnimSegment392.children.append(HAnimSite399)
HAnimSite402 = x3d.HAnimSite()
HAnimSite402.DEF = "STD_Site_l_tragion_pt"
HAnimSite402.name = "l_tragion_pt"
HAnimSite402.translation = [0.0739,1.6348,0.0282]
TouchSensor403 = x3d.TouchSensor()
TouchSensor403.description = "HAnimSite l_tragion_pt"

HAnimSite402.children.append(TouchSensor403)
Shape404 = x3d.Shape()
Shape404.USE = "HAnimSiteShape"

HAnimSite402.children.append(Shape404)

HAnimSegment392.children.append(HAnimSite402)
HAnimSite405 = x3d.HAnimSite()
HAnimSite405.DEF = "STD_Site_l_infraorbitale_pt"
HAnimSite405.name = "l_infraorbitale_pt"
HAnimSite405.translation = [0.0341,1.6171,0.0752]
TouchSensor406 = x3d.TouchSensor()
TouchSensor406.description = "HAnimSite l_infraorbitale_pt"

HAnimSite405.children.append(TouchSensor406)
Shape407 = x3d.Shape()
Shape407.USE = "HAnimSiteShape"

HAnimSite405.children.append(Shape407)

HAnimSegment392.children.append(HAnimSite405)
HAnimSite408 = x3d.HAnimSite()
HAnimSite408.DEF = "STD_Site_r_infraorbitale_pt"
HAnimSite408.name = "r_infraorbitale_pt"
HAnimSite408.translation = [-0.0237,1.6171,0.0752]
TouchSensor409 = x3d.TouchSensor()
TouchSensor409.description = "HAnimSite r_infraorbitale_pt"

HAnimSite408.children.append(TouchSensor409)
Shape410 = x3d.Shape()
Shape410.USE = "HAnimSiteShape"

HAnimSite408.children.append(Shape410)

HAnimSegment392.children.append(HAnimSite408)
HAnimSite411 = x3d.HAnimSite()
HAnimSite411.DEF = "STD_Site_l_ectocanthus_pt"
HAnimSite411.name = "l_ectocanthus_pt"
TouchSensor412 = x3d.TouchSensor()
TouchSensor412.description = "HAnimSite l_ectocanthus_pt"

HAnimSite411.children.append(TouchSensor412)
Shape413 = x3d.Shape()
Shape413.USE = "HAnimSiteShape"

HAnimSite411.children.append(Shape413)

HAnimSegment392.children.append(HAnimSite411)
HAnimSite414 = x3d.HAnimSite()
HAnimSite414.DEF = "STD_Site_nuchale_pt"
HAnimSite414.name = "nuchale_pt"
HAnimSite414.translation = [0.0039,1.5972,-0.0796]
TouchSensor415 = x3d.TouchSensor()
TouchSensor415.description = "HAnimSite nuchale_pt"

HAnimSite414.children.append(TouchSensor415)
Shape416 = x3d.Shape()
Shape416.USE = "HAnimSiteShape"

HAnimSite414.children.append(Shape416)

HAnimSegment392.children.append(HAnimSite414)
HAnimSite417 = x3d.HAnimSite()
HAnimSite417.DEF = "STD_Site_r_ectocanthus_pt"
HAnimSite417.name = "r_ectocanthus_pt"
TouchSensor418 = x3d.TouchSensor()
TouchSensor418.description = "HAnimSite r_ectocanthus_pt"

HAnimSite417.children.append(TouchSensor418)
Shape419 = x3d.Shape()
Shape419.USE = "HAnimSiteShape"

HAnimSite417.children.append(Shape419)

HAnimSegment392.children.append(HAnimSite417)
HAnimSite420 = x3d.HAnimSite()
HAnimSite420.DEF = "STD_Site_skull_vertex_pt"
HAnimSite420.name = "skull_vertex_pt"
HAnimSite420.translation = [0.0050,1.7504,0.0055]
TouchSensor421 = x3d.TouchSensor()
TouchSensor421.description = "HAnimSite skull_vertex_pt"

HAnimSite420.children.append(TouchSensor421)
Shape422 = x3d.Shape()
Shape422.USE = "HAnimSiteShape"

HAnimSite420.children.append(Shape422)

HAnimSegment392.children.append(HAnimSite420)
HAnimSite423 = x3d.HAnimSite()
HAnimSite423.DEF = "STD_Site_opisthocranion_pt"
HAnimSite423.name = "opisthocranion_pt"
TouchSensor424 = x3d.TouchSensor()
TouchSensor424.description = "HAnimSite opisthocranion_pt"

HAnimSite423.children.append(TouchSensor424)
Shape425 = x3d.Shape()
Shape425.USE = "HAnimSiteShape"

HAnimSite423.children.append(Shape425)

HAnimSegment392.children.append(HAnimSite423)

HAnimJoint391.children.append(HAnimSegment392)
HAnimJoint426 = x3d.HAnimJoint()
HAnimJoint426.DEF = "STD_Joint_l_eyelid_joint"
HAnimJoint426.name = "l_eyelid_joint"
HAnimJoint426.center = [0,0,0]
HAnimSegment427 = x3d.HAnimSegment()
HAnimSegment427.DEF = "STD_Segment_l_eyelid"
HAnimSegment427.name = "l_eyelid"

HAnimJoint426.children.append(HAnimSegment427)
HAnimJoint428 = x3d.HAnimJoint()
HAnimJoint428.DEF = "STD_Joint_r_eyelid_joint"
HAnimJoint428.name = "r_eyelid_joint"
HAnimJoint428.center = [0,0,0]
HAnimSegment429 = x3d.HAnimSegment()
HAnimSegment429.DEF = "STD_Segment_r_eyelid"
HAnimSegment429.name = "r_eyelid"

HAnimJoint428.children.append(HAnimSegment429)
HAnimJoint430 = x3d.HAnimJoint()
HAnimJoint430.DEF = "STD_Joint_l_eyeball_joint"
HAnimJoint430.name = "l_eyeball_joint"
HAnimJoint430.center = [0,0,0]
HAnimSegment431 = x3d.HAnimSegment()
HAnimSegment431.DEF = "STD_Segment_l_eyeball"
HAnimSegment431.name = "l_eyeball"

HAnimJoint430.children.append(HAnimSegment431)
HAnimJoint432 = x3d.HAnimJoint()
HAnimJoint432.DEF = "STD_Joint_r_eyeball_joint"
HAnimJoint432.name = "r_eyeball_joint"
HAnimJoint432.center = [0,0,0]
HAnimSegment433 = x3d.HAnimSegment()
HAnimSegment433.DEF = "STD_Segment_r_eyeball"
HAnimSegment433.name = "r_eyeball"

HAnimJoint432.children.append(HAnimSegment433)
HAnimJoint434 = x3d.HAnimJoint()
HAnimJoint434.DEF = "STD_Joint_l_eyebrow_joint"
HAnimJoint434.name = "l_eyebrow_joint"
HAnimJoint434.center = [0,0,0]
HAnimSegment435 = x3d.HAnimSegment()
HAnimSegment435.DEF = "STD_Segment_l_eyebrow"
HAnimSegment435.name = "l_eyebrow"

HAnimJoint434.children.append(HAnimSegment435)
HAnimJoint436 = x3d.HAnimJoint()
HAnimJoint436.DEF = "STD_Joint_r_eyebrow_joint"
HAnimJoint436.name = "r_eyebrow_joint"
HAnimJoint436.center = [0,0,0]
HAnimSegment437 = x3d.HAnimSegment()
HAnimSegment437.DEF = "STD_Segment_r_eyebrow"
HAnimSegment437.name = "r_eyebrow"

HAnimJoint436.children.append(HAnimSegment437)
HAnimJoint438 = x3d.HAnimJoint()
HAnimJoint438.DEF = "STD_Joint_temporomandibular"
HAnimJoint438.name = "temporomandibular"
HAnimJoint438.center = [0,0,0]
HAnimSegment439 = x3d.HAnimSegment()
HAnimSegment439.DEF = "STD_Segment_jaw"
HAnimSegment439.name = "jaw"
HAnimSite440 = x3d.HAnimSite()
HAnimSite440.DEF = "STD_Site_supramenton_pt"
HAnimSite440.name = "supramenton_pt"
HAnimSite440.translation = [0.0061,1.5410,0.0805]
TouchSensor441 = x3d.TouchSensor()
TouchSensor441.description = "HAnimSite supramenton_pt"

HAnimSite440.children.append(TouchSensor441)
Shape442 = x3d.Shape()
Shape442.USE = "HAnimSiteShape"

HAnimSite440.children.append(Shape442)

HAnimSegment439.children.append(HAnimSite440)
HAnimSite443 = x3d.HAnimSite()
HAnimSite443.DEF = "STD_Site_menton_pt"
HAnimSite443.name = "menton_pt"
TouchSensor444 = x3d.TouchSensor()
TouchSensor444.description = "HAnimSite menton_pt"

HAnimSite443.children.append(TouchSensor444)
Shape445 = x3d.Shape()
Shape445.USE = "HAnimSiteShape"

HAnimSite443.children.append(Shape445)

HAnimSegment439.children.append(HAnimSite443)
HAnimSite446 = x3d.HAnimSite()
HAnimSite446.DEF = "STD_Site_r_gonion_pt"
HAnimSite446.name = "r_gonion_pt"
HAnimSite446.translation = [-0.0520,1.5529,0.0347]
TouchSensor447 = x3d.TouchSensor()
TouchSensor447.description = "HAnimSite r_gonion_pt"

HAnimSite446.children.append(TouchSensor447)
Shape448 = x3d.Shape()
Shape448.USE = "HAnimSiteShape"

HAnimSite446.children.append(Shape448)

HAnimSegment439.children.append(HAnimSite446)
HAnimSite449 = x3d.HAnimSite()
HAnimSite449.DEF = "STD_Site_l_gonion_pt"
HAnimSite449.name = "l_gonion_pt"
HAnimSite449.translation = [0.0631,1.5530,0.0330]
TouchSensor450 = x3d.TouchSensor()
TouchSensor450.description = "HAnimSite l_gonion_pt"

HAnimSite449.children.append(TouchSensor450)
Shape451 = x3d.Shape()
Shape451.USE = "HAnimSiteShape"

HAnimSite449.children.append(Shape451)

HAnimSegment439.children.append(HAnimSite449)

HAnimJoint438.children.append(HAnimSegment439)

HAnimJoint436.children.append(HAnimJoint438)

HAnimJoint434.children.append(HAnimJoint436)

HAnimJoint432.children.append(HAnimJoint434)

HAnimJoint430.children.append(HAnimJoint432)

HAnimJoint428.children.append(HAnimJoint430)

HAnimJoint426.children.append(HAnimJoint428)

HAnimJoint391.children.append(HAnimJoint426)

HAnimJoint389.children.append(HAnimJoint391)

HAnimJoint384.children.append(HAnimJoint389)

HAnimJoint382.children.append(HAnimJoint384)

HAnimJoint380.children.append(HAnimJoint382)

HAnimJoint378.children.append(HAnimJoint380)

HAnimJoint376.children.append(HAnimJoint378)

HAnimJoint368.children.append(HAnimJoint376)

HAnimJoint360.children.append(HAnimJoint368)
HAnimJoint452 = x3d.HAnimJoint()
HAnimJoint452.DEF = "STD_Joint_l_sternoclavicular"
HAnimJoint452.name = "l_sternoclavicular"
HAnimJoint452.center = [0.0820,1.4488,-0.0353]
HAnimSegment453 = x3d.HAnimSegment()
HAnimSegment453.DEF = "STD_Segment_l_clavicle"
HAnimSegment453.name = "l_clavicle"
HAnimSite454 = x3d.HAnimSite()
HAnimSite454.DEF = "STD_Site_l_axilla_distal_pt"
HAnimSite454.name = "l_axilla_distal_pt"
HAnimSite454.translation = [0.1706,1.4072,-0.0875]
TouchSensor455 = x3d.TouchSensor()
TouchSensor455.description = "HAnimSite l_axilla_distal_pt"

HAnimSite454.children.append(TouchSensor455)
Shape456 = x3d.Shape()
Shape456.USE = "HAnimSiteShape"

HAnimSite454.children.append(Shape456)

HAnimSegment453.children.append(HAnimSite454)
HAnimSite457 = x3d.HAnimSite()
HAnimSite457.DEF = "STD_Site_l_axilla_posterior_folds_pt"
HAnimSite457.name = "l_axilla_posterior_folds_pt"
TouchSensor458 = x3d.TouchSensor()
TouchSensor458.description = "HAnimSite l_axilla_posterior_folds_pt"

HAnimSite457.children.append(TouchSensor458)
Shape459 = x3d.Shape()
Shape459.USE = "HAnimSiteShape"

HAnimSite457.children.append(Shape459)

HAnimSegment453.children.append(HAnimSite457)
HAnimSite460 = x3d.HAnimSite()
HAnimSite460.DEF = "STD_Site_l_axilla_proximal_pt"
HAnimSite460.name = "l_axilla_proximal_pt"
HAnimSite460.translation = [0.1777,1.4065,-0.0075]
TouchSensor461 = x3d.TouchSensor()
TouchSensor461.description = "HAnimSite l_axilla_proximal_pt"

HAnimSite460.children.append(TouchSensor461)
Shape462 = x3d.Shape()
Shape462.USE = "HAnimSiteShape"

HAnimSite460.children.append(Shape462)

HAnimSegment453.children.append(HAnimSite460)
HAnimSite463 = x3d.HAnimSite()
HAnimSite463.DEF = "STD_Site_l_acromion_pt"
HAnimSite463.name = "l_acromion_pt"
HAnimSite463.translation = [0.2032,1.4760,-0.0490]
TouchSensor464 = x3d.TouchSensor()
TouchSensor464.description = "HAnimSite l_acromion_pt"

HAnimSite463.children.append(TouchSensor464)
Shape465 = x3d.Shape()
Shape465.USE = "HAnimSiteShape"

HAnimSite463.children.append(Shape465)

HAnimSegment453.children.append(HAnimSite463)
HAnimSite466 = x3d.HAnimSite()
HAnimSite466.DEF = "STD_Site_l_clavicale_pt"
HAnimSite466.name = "l_clavicale_pt"
HAnimSite466.translation = [0.0271,1.4943,0.0394]
TouchSensor467 = x3d.TouchSensor()
TouchSensor467.description = "HAnimSite l_clavicale_pt"

HAnimSite466.children.append(TouchSensor467)
Shape468 = x3d.Shape()
Shape468.USE = "HAnimSiteShape"

HAnimSite466.children.append(Shape468)

HAnimSegment453.children.append(HAnimSite466)

HAnimJoint452.children.append(HAnimSegment453)
HAnimJoint469 = x3d.HAnimJoint()
HAnimJoint469.DEF = "STD_Joint_l_acromioclavicular"
HAnimJoint469.name = "l_acromioclavicular"
HAnimJoint469.center = [0.0962,1.4269,-0.0424]
HAnimSegment470 = x3d.HAnimSegment()
HAnimSegment470.DEF = "STD_Segment_l_scapula"
HAnimSegment470.name = "l_scapula"

HAnimJoint469.children.append(HAnimSegment470)
HAnimJoint471 = x3d.HAnimJoint()
HAnimJoint471.DEF = "STD_Joint_l_shoulder"
HAnimJoint471.name = "l_shoulder"
HAnimJoint471.center = [0.2029,1.4376,-0.0387]
HAnimSegment472 = x3d.HAnimSegment()
HAnimSegment472.DEF = "STD_Segment_l_upperarm"
HAnimSegment472.name = "l_upperarm"
HAnimSite473 = x3d.HAnimSite()
HAnimSite473.DEF = "STD_Site_l_bideltoid_pt"
HAnimSite473.name = "l_bideltoid_pt"
TouchSensor474 = x3d.TouchSensor()
TouchSensor474.description = "HAnimSite l_bideltoid_pt"

HAnimSite473.children.append(TouchSensor474)
Shape475 = x3d.Shape()
Shape475.USE = "HAnimSiteShape"

HAnimSite473.children.append(Shape475)

HAnimSegment472.children.append(HAnimSite473)
HAnimSite476 = x3d.HAnimSite()
HAnimSite476.DEF = "STD_Site_l_humeral_lateral_epicondyles_pt"
HAnimSite476.name = "l_humeral_lateral_epicondyles_pt"
HAnimSite476.translation = [0.2280,1.1482,-0.1100]
TouchSensor477 = x3d.TouchSensor()
TouchSensor477.description = "HAnimSite l_humeral_lateral_epicondyles_pt"

HAnimSite476.children.append(TouchSensor477)
Shape478 = x3d.Shape()
Shape478.USE = "HAnimSiteShape"

HAnimSite476.children.append(Shape478)

HAnimSegment472.children.append(HAnimSite476)

HAnimJoint471.children.append(HAnimSegment472)
HAnimJoint479 = x3d.HAnimJoint()
HAnimJoint479.DEF = "STD_Joint_l_elbow"
HAnimJoint479.name = "l_elbow"
HAnimJoint479.center = [0.2014,1.1357,-0.0682]
HAnimSegment480 = x3d.HAnimSegment()
HAnimSegment480.DEF = "STD_Segment_l_forearm"
HAnimSegment480.name = "l_forearm"
HAnimSite481 = x3d.HAnimSite()
HAnimSite481.DEF = "STD_Site_l_olecranon_pt"
HAnimSite481.name = "l_olecranon_pt"
HAnimSite481.translation = [-0.1962,1.1375,-0.1123]
TouchSensor482 = x3d.TouchSensor()
TouchSensor482.description = "HAnimSite l_olecranon_pt"

HAnimSite481.children.append(TouchSensor482)
Shape483 = x3d.Shape()
Shape483.USE = "HAnimSiteShape"

HAnimSite481.children.append(Shape483)

HAnimSegment480.children.append(HAnimSite481)
HAnimSite484 = x3d.HAnimSite()
HAnimSite484.DEF = "STD_Site_l_humeral_medial_epicondyles_pt"
HAnimSite484.name = "l_humeral_medial_epicondyles_pt"
HAnimSite484.translation = [0.1735,1.1272,-0.1113]
TouchSensor485 = x3d.TouchSensor()
TouchSensor485.description = "HAnimSite l_humeral_medial_epicondyles_pt"

HAnimSite484.children.append(TouchSensor485)
Shape486 = x3d.Shape()
Shape486.USE = "HAnimSiteShape"

HAnimSite484.children.append(Shape486)

HAnimSegment480.children.append(HAnimSite484)
HAnimSite487 = x3d.HAnimSite()
HAnimSite487.DEF = "STD_Site_l_radiale_pt"
HAnimSite487.name = "l_radiale_pt"
HAnimSite487.translation = [0.2182,1.1212,-0.1167]
TouchSensor488 = x3d.TouchSensor()
TouchSensor488.description = "HAnimSite l_radiale_pt"

HAnimSite487.children.append(TouchSensor488)
Shape489 = x3d.Shape()
Shape489.USE = "HAnimSiteShape"

HAnimSite487.children.append(Shape489)

HAnimSegment480.children.append(HAnimSite487)
HAnimSite490 = x3d.HAnimSite()
HAnimSite490.DEF = "STD_Site_l_radial_styloid_pt"
HAnimSite490.name = "l_radial_styloid_pt"
HAnimSite490.translation = [0.1901,0.8645,-0.0415]
TouchSensor491 = x3d.TouchSensor()
TouchSensor491.description = "HAnimSite l_radial_styloid_pt"

HAnimSite490.children.append(TouchSensor491)
Shape492 = x3d.Shape()
Shape492.USE = "HAnimSiteShape"

HAnimSite490.children.append(Shape492)

HAnimSegment480.children.append(HAnimSite490)

HAnimJoint479.children.append(HAnimSegment480)
HAnimJoint493 = x3d.HAnimJoint()
HAnimJoint493.DEF = "STD_Joint_l_radiocarpal"
HAnimJoint493.name = "l_radiocarpal"
HAnimJoint493.center = [0.1984,0.8663,-0.0583]
HAnimSegment494 = x3d.HAnimSegment()
HAnimSegment494.DEF = "STD_Segment_l_carpal"
HAnimSegment494.name = "l_carpal"
HAnimSite495 = x3d.HAnimSite()
HAnimSite495.DEF = "STD_Site_l_ulnar_styloid_pt"
HAnimSite495.name = "l_ulnar_styloid_pt"
HAnimSite495.translation = [-0.2142,0.8529,-0.0648]
TouchSensor496 = x3d.TouchSensor()
TouchSensor496.description = "HAnimSite l_ulnar_styloid_pt"

HAnimSite495.children.append(TouchSensor496)
Shape497 = x3d.Shape()
Shape497.USE = "HAnimSiteShape"

HAnimSite495.children.append(Shape497)

HAnimSegment494.children.append(HAnimSite495)

HAnimJoint493.children.append(HAnimSegment494)
HAnimJoint498 = x3d.HAnimJoint()
HAnimJoint498.DEF = "STD_Joint_l_midcarpal_1"
HAnimJoint498.name = "l_midcarpal_1"
HAnimJoint498.center = [0,0,0]
HAnimSegment499 = x3d.HAnimSegment()
HAnimSegment499.DEF = "STD_Segment_l_trapezium"
HAnimSegment499.name = "l_trapezium"

HAnimJoint498.children.append(HAnimSegment499)
HAnimJoint500 = x3d.HAnimJoint()
HAnimJoint500.DEF = "STD_Joint_l_carpometacarpal_1"
HAnimJoint500.name = "l_carpometacarpal_1"
HAnimJoint500.center = [0.1924,0.8472,-0.0534]
HAnimSegment501 = x3d.HAnimSegment()
HAnimSegment501.DEF = "STD_Segment_l_metacarpal_1"
HAnimSegment501.name = "l_metacarpal_1"

HAnimJoint500.children.append(HAnimSegment501)
HAnimJoint502 = x3d.HAnimJoint()
HAnimJoint502.DEF = "STD_Joint_l_metacarpophalangeal_1"
HAnimJoint502.name = "l_metacarpophalangeal_1"
HAnimJoint502.center = [0.1951,0.8226,0.0246]
HAnimSegment503 = x3d.HAnimSegment()
HAnimSegment503.DEF = "STD_Segment_l_carpal_proximal_phalanx_1"
HAnimSegment503.name = "l_carpal_proximal_phalanx_1"

HAnimJoint502.children.append(HAnimSegment503)
HAnimJoint504 = x3d.HAnimJoint()
HAnimJoint504.DEF = "STD_Joint_l_carpal_interphalangeal_1"
HAnimJoint504.name = "l_carpal_interphalangeal_1"
HAnimJoint504.center = [0.1955,0.8159,0.0464]
HAnimSegment505 = x3d.HAnimSegment()
HAnimSegment505.DEF = "STD_Segment_l_carpal_distal_phalanx_1"
HAnimSegment505.name = "l_carpal_distal_phalanx_1"
HAnimSite506 = x3d.HAnimSite()
HAnimSite506.DEF = "STD_Site_l_carpal_distal_phalanx_1_tip"
HAnimSite506.name = "l_carpal_distal_phalanx_1_tip"
TouchSensor507 = x3d.TouchSensor()
TouchSensor507.description = "HAnimSite l_carpal_distal_phalanx_1_tip"

HAnimSite506.children.append(TouchSensor507)
Shape508 = x3d.Shape()
Shape508.USE = "HAnimSiteShape"

HAnimSite506.children.append(Shape508)

HAnimSegment505.children.append(HAnimSite506)

HAnimJoint504.children.append(HAnimSegment505)

HAnimJoint502.children.append(HAnimJoint504)

HAnimJoint500.children.append(HAnimJoint502)

HAnimJoint498.children.append(HAnimJoint500)

HAnimJoint493.children.append(HAnimJoint498)
HAnimJoint509 = x3d.HAnimJoint()
HAnimJoint509.DEF = "STD_Joint_l_midcarpal_2"
HAnimJoint509.name = "l_midcarpal_2"
HAnimJoint509.center = [0,0,0]
HAnimSegment510 = x3d.HAnimSegment()
HAnimSegment510.DEF = "STD_Segment_l_trapezoid"
HAnimSegment510.name = "l_trapezoid"

HAnimJoint509.children.append(HAnimSegment510)
HAnimJoint511 = x3d.HAnimJoint()
HAnimJoint511.DEF = "STD_Joint_l_carpometacarpal_2"
HAnimJoint511.name = "l_carpometacarpal_2"
HAnimJoint511.center = [0.1983,0.8024,-0.0280]
HAnimSegment512 = x3d.HAnimSegment()
HAnimSegment512.DEF = "STD_Segment_l_metacarpal_2"
HAnimSegment512.name = "l_metacarpal_2"
HAnimSite513 = x3d.HAnimSite()
HAnimSite513.DEF = "STD_Site_l_metacarpal_phalanx_2_pt"
HAnimSite513.name = "l_metacarpal_phalanx_2_pt"
HAnimSite513.translation = [0.2009,0.8139,-0.0237]
TouchSensor514 = x3d.TouchSensor()
TouchSensor514.description = "HAnimSite l_metacarpal_phalanx_2_pt"

HAnimSite513.children.append(TouchSensor514)
Shape515 = x3d.Shape()
Shape515.USE = "HAnimSiteShape"

HAnimSite513.children.append(Shape515)

HAnimSegment512.children.append(HAnimSite513)

HAnimJoint511.children.append(HAnimSegment512)
HAnimJoint516 = x3d.HAnimJoint()
HAnimJoint516.DEF = "STD_Joint_l_metacarpophalangeal_2"
HAnimJoint516.name = "l_metacarpophalangeal_2"
HAnimJoint516.center = [0.1983,0.7815,-0.0280]
HAnimSegment517 = x3d.HAnimSegment()
HAnimSegment517.DEF = "STD_Segment_l_carpal_proximal_phalanx_2 "
HAnimSegment517.name = "l_carpal_proximal_phalanx_2 "

HAnimJoint516.children.append(HAnimSegment517)
HAnimJoint518 = x3d.HAnimJoint()
HAnimJoint518.DEF = "STD_Joint_l_carpal_proximal_interphalangeal_2"
HAnimJoint518.name = "l_carpal_proximal_interphalangeal_2"
HAnimJoint518.center = [0.2017,0.7363,-0.0248]
HAnimSegment519 = x3d.HAnimSegment()
HAnimSegment519.DEF = "STD_Segment_l_carpal_middle_phalanx_2"
HAnimSegment519.name = "l_carpal_middle_phalanx_2"

HAnimJoint518.children.append(HAnimSegment519)
HAnimJoint520 = x3d.HAnimJoint()
HAnimJoint520.DEF = "STD_Joint_l_carpal_distal_interphalangeal_2"
HAnimJoint520.name = "l_carpal_distal_interphalangeal_2"
HAnimJoint520.center = [0.2028,0.7139,-0.0236]
HAnimSegment521 = x3d.HAnimSegment()
HAnimSegment521.DEF = "STD_Segment_l_carpal_distal_phalanx_2"
HAnimSegment521.name = "l_carpal_distal_phalanx_2"
HAnimSite522 = x3d.HAnimSite()
HAnimSite522.DEF = "STD_Site_l_dactylion_pt"
HAnimSite522.name = "l_dactylion_pt"
HAnimSite522.translation = [0.2056,0.6743,-0.0482]
TouchSensor523 = x3d.TouchSensor()
TouchSensor523.description = "HAnimSite l_dactylion_pt"

HAnimSite522.children.append(TouchSensor523)
Shape524 = x3d.Shape()
Shape524.USE = "HAnimSiteShape"

HAnimSite522.children.append(Shape524)

HAnimSegment521.children.append(HAnimSite522)
HAnimSite525 = x3d.HAnimSite()
HAnimSite525.DEF = "STD_Site_l_carpal_distal_phalanx_2_tip"
HAnimSite525.name = "l_carpal_distal_phalanx_2_tip"
TouchSensor526 = x3d.TouchSensor()
TouchSensor526.description = "HAnimSite l_carpal_distal_phalanx_2_tip"

HAnimSite525.children.append(TouchSensor526)
Shape527 = x3d.Shape()
Shape527.USE = "HAnimSiteShape"

HAnimSite525.children.append(Shape527)

HAnimSegment521.children.append(HAnimSite525)

HAnimJoint520.children.append(HAnimSegment521)

HAnimJoint518.children.append(HAnimJoint520)

HAnimJoint516.children.append(HAnimJoint518)

HAnimJoint511.children.append(HAnimJoint516)

HAnimJoint509.children.append(HAnimJoint511)

HAnimJoint493.children.append(HAnimJoint509)
HAnimJoint528 = x3d.HAnimJoint()
HAnimJoint528.DEF = "STD_Joint_l_midcarpal_3"
HAnimJoint528.name = "l_midcarpal_3"
HAnimJoint528.center = [0,0,0]
HAnimSegment529 = x3d.HAnimSegment()
HAnimSegment529.DEF = "STD_Segment_l_capitate"
HAnimSegment529.name = "l_capitate"

HAnimJoint528.children.append(HAnimSegment529)
HAnimJoint530 = x3d.HAnimJoint()
HAnimJoint530.DEF = "STD_Joint_l_carpometacarpal_3"
HAnimJoint530.name = "l_carpometacarpal_3"
HAnimJoint530.center = [0.1987,0.8029,-0.0530]
HAnimSegment531 = x3d.HAnimSegment()
HAnimSegment531.DEF = "STD_Segment_l_metacarpal_3"
HAnimSegment531.name = "l_metacarpal_3"
HAnimSite532 = x3d.HAnimSite()
HAnimSite532.DEF = "STD_Site_l_metacarpal_phalanx_3_pt"
HAnimSite532.name = "l_metacarpal_phalanx_3_pt"
TouchSensor533 = x3d.TouchSensor()
TouchSensor533.description = "HAnimSite l_metacarpal_phalanx_3_pt"

HAnimSite532.children.append(TouchSensor533)
Shape534 = x3d.Shape()
Shape534.USE = "HAnimSiteShape"

HAnimSite532.children.append(Shape534)

HAnimSegment531.children.append(HAnimSite532)

HAnimJoint530.children.append(HAnimSegment531)
HAnimJoint535 = x3d.HAnimJoint()
HAnimJoint535.DEF = "STD_Joint_l_metacarpophalangeal_3"
HAnimJoint535.name = "l_metacarpophalangeal_3"
HAnimJoint535.center = [0.1987,0.7818,-0.0530]
HAnimSegment536 = x3d.HAnimSegment()
HAnimSegment536.DEF = "STD_Segment_l_carpal_proximal_phalanx_3"
HAnimSegment536.name = "l_carpal_proximal_phalanx_3"

HAnimJoint535.children.append(HAnimSegment536)
HAnimJoint537 = x3d.HAnimJoint()
HAnimJoint537.DEF = "STD_Joint_l_carpal_proximal_interphalangeal_3"
HAnimJoint537.name = "l_carpal_proximal_interphalangeal_3"
HAnimJoint537.center = [0.2013,0.7273,-0.0503]
HAnimSegment538 = x3d.HAnimSegment()
HAnimSegment538.DEF = "STD_Segment_l_carpal_middle_phalanx_3"
HAnimSegment538.name = "l_carpal_middle_phalanx_3"

HAnimJoint537.children.append(HAnimSegment538)
HAnimJoint539 = x3d.HAnimJoint()
HAnimJoint539.DEF = "STD_Joint_l_carpal_distal_interphalangeal_3"
HAnimJoint539.name = "l_carpal_distal_interphalangeal_3"
HAnimJoint539.center = [0.2026,0.7011,-0.0494]
HAnimSegment540 = x3d.HAnimSegment()
HAnimSegment540.DEF = "STD_Segment_l_carpal_distal_phalanx_3"
HAnimSegment540.name = "l_carpal_distal_phalanx_3"
HAnimSite541 = x3d.HAnimSite()
HAnimSite541.DEF = "STD_Site_l_carpal_distal_phalanx_3_tip"
HAnimSite541.name = "l_carpal_distal_phalanx_3_tip"
TouchSensor542 = x3d.TouchSensor()
TouchSensor542.description = "HAnimSite l_carpal_distal_phalanx_3_tip"

HAnimSite541.children.append(TouchSensor542)
Shape543 = x3d.Shape()
Shape543.USE = "HAnimSiteShape"

HAnimSite541.children.append(Shape543)

HAnimSegment540.children.append(HAnimSite541)

HAnimJoint539.children.append(HAnimSegment540)

HAnimJoint537.children.append(HAnimJoint539)

HAnimJoint535.children.append(HAnimJoint537)

HAnimJoint530.children.append(HAnimJoint535)

HAnimJoint528.children.append(HAnimJoint530)

HAnimJoint493.children.append(HAnimJoint528)
HAnimJoint544 = x3d.HAnimJoint()
HAnimJoint544.DEF = "STD_Joint_l_midcarpal_4_5"
HAnimJoint544.name = "l_midcarpal_4_5"
HAnimJoint544.center = [0,0,0]
HAnimSegment545 = x3d.HAnimSegment()
HAnimSegment545.DEF = "STD_Segment_l_hamate"
HAnimSegment545.name = "l_hamate"

HAnimJoint544.children.append(HAnimSegment545)
HAnimJoint546 = x3d.HAnimJoint()
HAnimJoint546.DEF = "STD_Joint_l_carpometacarpal_4"
HAnimJoint546.name = "l_carpometacarpal_4"
HAnimJoint546.center = [0.1956,0.8019,-0.0794]
HAnimSegment547 = x3d.HAnimSegment()
HAnimSegment547.DEF = "STD_Segment_l_metacarpal_4"
HAnimSegment547.name = "l_metacarpal_4"

HAnimJoint546.children.append(HAnimSegment547)
HAnimJoint548 = x3d.HAnimJoint()
HAnimJoint548.DEF = "STD_Joint_l_metacarpophalangeal_4"
HAnimJoint548.name = "l_metacarpophalangeal_4"
HAnimJoint548.center = [0.1956,0.7815,-0.0794]
HAnimSegment549 = x3d.HAnimSegment()
HAnimSegment549.DEF = "STD_Segment_l_carpal_proximal_phalanx_4"
HAnimSegment549.name = "l_carpal_proximal_phalanx_4"

HAnimJoint548.children.append(HAnimSegment549)
HAnimJoint550 = x3d.HAnimJoint()
HAnimJoint550.DEF = "STD_Joint_l_carpal_proximal_interphalangeal_4"
HAnimJoint550.name = "l_carpal_proximal_interphalangeal_4"
HAnimJoint550.center = [0.1973,0.7287,-0.0777]
HAnimSegment551 = x3d.HAnimSegment()
HAnimSegment551.DEF = "STD_Segment_l_carpal_middle_phalanx_4"
HAnimSegment551.name = "l_carpal_middle_phalanx_4"

HAnimJoint550.children.append(HAnimSegment551)
HAnimJoint552 = x3d.HAnimJoint()
HAnimJoint552.DEF = "STD_Joint_l_carpal_distal_interphalangeal_4"
HAnimJoint552.name = "l_carpal_distal_interphalangeal_4"
HAnimJoint552.center = [0.1983,0.7045,-0.0767]
HAnimSegment553 = x3d.HAnimSegment()
HAnimSegment553.DEF = "STD_Segment_l_carpal_distal_phalanx_4"
HAnimSegment553.name = "l_carpal_distal_phalanx_4"
HAnimSite554 = x3d.HAnimSite()
HAnimSite554.DEF = "STD_Site_l_carpal_distal_phalanx_4_tip"
HAnimSite554.name = "l_carpal_distal_phalanx_4_tip"
TouchSensor555 = x3d.TouchSensor()
TouchSensor555.description = "HAnimSite l_carpal_distal_phalanx_4_tip"

HAnimSite554.children.append(TouchSensor555)
Shape556 = x3d.Shape()
Shape556.USE = "HAnimSiteShape"

HAnimSite554.children.append(Shape556)

HAnimSegment553.children.append(HAnimSite554)

HAnimJoint552.children.append(HAnimSegment553)

HAnimJoint550.children.append(HAnimJoint552)

HAnimJoint548.children.append(HAnimJoint550)

HAnimJoint546.children.append(HAnimJoint548)

HAnimJoint544.children.append(HAnimJoint546)
HAnimJoint557 = x3d.HAnimJoint()
HAnimJoint557.DEF = "STD_Joint_l_carpometacarpal_5"
HAnimJoint557.name = "l_carpometacarpal_5"
HAnimJoint557.center = [0.1925,0.8066,-0.1036]
HAnimSegment558 = x3d.HAnimSegment()
HAnimSegment558.DEF = "STD_Segment_l_metacarpal_5"
HAnimSegment558.name = "l_metacarpal_5"
HAnimSite559 = x3d.HAnimSite()
HAnimSite559.DEF = "STD_Site_l_metacarpal_phalanx_5_pt"
HAnimSite559.name = "l_metacarpal_phalanx_5_pt"
HAnimSite559.translation = [0.1929,0.7860,-0.1122]
TouchSensor560 = x3d.TouchSensor()
TouchSensor560.description = "HAnimSite l_metacarpal_phalanx_5_pt"

HAnimSite559.children.append(TouchSensor560)
Shape561 = x3d.Shape()
Shape561.USE = "HAnimSiteShape"

HAnimSite559.children.append(Shape561)

HAnimSegment558.children.append(HAnimSite559)

HAnimJoint557.children.append(HAnimSegment558)
HAnimJoint562 = x3d.HAnimJoint()
HAnimJoint562.DEF = "STD_Joint_l_metacarpophalangeal_5"
HAnimJoint562.name = "l_metacarpophalangeal_5"
HAnimJoint562.center = [0.1925,0.7866,-0.1036]
HAnimSegment563 = x3d.HAnimSegment()
HAnimSegment563.DEF = "STD_Segment_l_carpal_proximal_phalanx_5"
HAnimSegment563.name = "l_carpal_proximal_phalanx_5"

HAnimJoint562.children.append(HAnimSegment563)
HAnimJoint564 = x3d.HAnimJoint()
HAnimJoint564.DEF = "STD_Joint_l_carpal_proximal_interphalangeal_5"
HAnimJoint564.name = "l_carpal_proximal_interphalangeal_5"
HAnimJoint564.center = [0.1938,0.7452,-0.1024]
HAnimSegment565 = x3d.HAnimSegment()
HAnimSegment565.DEF = "STD_Segment_l_carpal_middle_phalanx_5"
HAnimSegment565.name = "l_carpal_middle_phalanx_5"

HAnimJoint564.children.append(HAnimSegment565)
HAnimJoint566 = x3d.HAnimJoint()
HAnimJoint566.DEF = "STD_Joint_l_carpal_distal_interphalangeal_5"
HAnimJoint566.name = "l_carpal_distal_interphalangeal_5"
HAnimJoint566.center = [0.1948,0.7277,-0.1017]
HAnimSegment567 = x3d.HAnimSegment()
HAnimSegment567.DEF = "STD_Segment_l_carpal_distal_phalanx_5"
HAnimSegment567.name = "l_carpal_distal_phalanx_5"
HAnimSite568 = x3d.HAnimSite()
HAnimSite568.DEF = "STD_Site_l_carpal_distal_phalanx_5_tip"
HAnimSite568.name = "l_carpal_distal_phalanx_5_tip"
TouchSensor569 = x3d.TouchSensor()
TouchSensor569.description = "HAnimSite l_carpal_distal_phalanx_5_tip"

HAnimSite568.children.append(TouchSensor569)
Shape570 = x3d.Shape()
Shape570.USE = "HAnimSiteShape"

HAnimSite568.children.append(Shape570)

HAnimSegment567.children.append(HAnimSite568)

HAnimJoint566.children.append(HAnimSegment567)

HAnimJoint564.children.append(HAnimJoint566)

HAnimJoint562.children.append(HAnimJoint564)

HAnimJoint557.children.append(HAnimJoint562)

HAnimJoint544.children.append(HAnimJoint557)

HAnimJoint493.children.append(HAnimJoint544)

HAnimJoint479.children.append(HAnimJoint493)

HAnimJoint471.children.append(HAnimJoint479)

HAnimJoint469.children.append(HAnimJoint471)

HAnimJoint452.children.append(HAnimJoint469)

HAnimJoint360.children.append(HAnimJoint452)
HAnimJoint571 = x3d.HAnimJoint()
HAnimJoint571.DEF = "STD_Joint_r_sternoclavicular"
HAnimJoint571.name = "r_sternoclavicular"
HAnimJoint571.center = [-0.0694,1.4600,-0.0330]
HAnimSegment572 = x3d.HAnimSegment()
HAnimSegment572.DEF = "STD_Segment_r_clavicle"
HAnimSegment572.name = "r_clavicle"
HAnimSite573 = x3d.HAnimSite()
HAnimSite573.DEF = "STD_Site_r_axilla_distal_pt"
HAnimSite573.name = "r_axilla_distal_pt"
HAnimSite573.translation = [-0.1603,1.4098,-0.0826]
TouchSensor574 = x3d.TouchSensor()
TouchSensor574.description = "HAnimSite r_axilla_distal_pt"

HAnimSite573.children.append(TouchSensor574)
Shape575 = x3d.Shape()
Shape575.USE = "HAnimSiteShape"

HAnimSite573.children.append(Shape575)

HAnimSegment572.children.append(HAnimSite573)
HAnimSite576 = x3d.HAnimSite()
HAnimSite576.DEF = "STD_Site_r_axilla_posterior_folds_pt"
HAnimSite576.name = "r_axilla_posterior_folds_pt"
TouchSensor577 = x3d.TouchSensor()
TouchSensor577.description = "HAnimSite r_axilla_posterior_folds_pt"

HAnimSite576.children.append(TouchSensor577)
Shape578 = x3d.Shape()
Shape578.USE = "HAnimSiteShape"

HAnimSite576.children.append(Shape578)

HAnimSegment572.children.append(HAnimSite576)
HAnimSite579 = x3d.HAnimSite()
HAnimSite579.DEF = "STD_Site_r_axilla_proximal_pt"
HAnimSite579.name = "r_axilla_proximal_pt"
HAnimSite579.translation = [-0.1626,1.4072,-0.0031]
TouchSensor580 = x3d.TouchSensor()
TouchSensor580.description = "HAnimSite r_axilla_proximal_pt"

HAnimSite579.children.append(TouchSensor580)
Shape581 = x3d.Shape()
Shape581.USE = "HAnimSiteShape"

HAnimSite579.children.append(Shape581)

HAnimSegment572.children.append(HAnimSite579)
HAnimSite582 = x3d.HAnimSite()
HAnimSite582.DEF = "STD_Site_r_acromion_pt"
HAnimSite582.name = "r_acromion_pt"
HAnimSite582.translation = [-0.1905,1.4791,-0.0431]
TouchSensor583 = x3d.TouchSensor()
TouchSensor583.description = "HAnimSite r_acromion_pt"

HAnimSite582.children.append(TouchSensor583)
Shape584 = x3d.Shape()
Shape584.USE = "HAnimSiteShape"

HAnimSite582.children.append(Shape584)

HAnimSegment572.children.append(HAnimSite582)
HAnimSite585 = x3d.HAnimSite()
HAnimSite585.DEF = "STD_Site_r_clavicale_pt"
HAnimSite585.name = "r_clavicale_pt"
HAnimSite585.translation = [-0.0115,1.4943,0.0400]
TouchSensor586 = x3d.TouchSensor()
TouchSensor586.description = "HAnimSite r_clavicale_pt"

HAnimSite585.children.append(TouchSensor586)
Shape587 = x3d.Shape()
Shape587.USE = "HAnimSiteShape"

HAnimSite585.children.append(Shape587)

HAnimSegment572.children.append(HAnimSite585)

HAnimJoint571.children.append(HAnimSegment572)
HAnimJoint588 = x3d.HAnimJoint()
HAnimJoint588.DEF = "STD_Joint_r_acromioclavicular"
HAnimJoint588.name = "r_acromioclavicular"
HAnimJoint588.center = [-0.0836,1.4281,-0.0401]
HAnimSegment589 = x3d.HAnimSegment()
HAnimSegment589.DEF = "STD_Segment_r_scapula"
HAnimSegment589.name = "r_scapula"

HAnimJoint588.children.append(HAnimSegment589)
HAnimJoint590 = x3d.HAnimJoint()
HAnimJoint590.DEF = "STD_Joint_r_shoulder"
HAnimJoint590.name = "r_shoulder"
HAnimJoint590.center = [-0.1907,1.4407,-0.0325]
HAnimSegment591 = x3d.HAnimSegment()
HAnimSegment591.DEF = "STD_Segment_r_upperarm"
HAnimSegment591.name = "r_upperarm"
HAnimSite592 = x3d.HAnimSite()
HAnimSite592.DEF = "STD_Site_r_bideltoid_pt"
HAnimSite592.name = "r_bideltoid_pt"
TouchSensor593 = x3d.TouchSensor()
TouchSensor593.description = "HAnimSite r_bideltoid_pt"

HAnimSite592.children.append(TouchSensor593)
Shape594 = x3d.Shape()
Shape594.USE = "HAnimSiteShape"

HAnimSite592.children.append(Shape594)

HAnimSegment591.children.append(HAnimSite592)
HAnimSite595 = x3d.HAnimSite()
HAnimSite595.DEF = "STD_Site_r_humeral_lateral_epicondyles_pt"
HAnimSite595.name = "r_humeral_lateral_epicondyles_pt"
HAnimSite595.translation = [-0.2224,1.1517,-0.1033]
TouchSensor596 = x3d.TouchSensor()
TouchSensor596.description = "HAnimSite r_humeral_lateral_epicondyles_pt"

HAnimSite595.children.append(TouchSensor596)
Shape597 = x3d.Shape()
Shape597.USE = "HAnimSiteShape"

HAnimSite595.children.append(Shape597)

HAnimSegment591.children.append(HAnimSite595)

HAnimJoint590.children.append(HAnimSegment591)
HAnimJoint598 = x3d.HAnimJoint()
HAnimJoint598.DEF = "STD_Joint_r_elbow"
HAnimJoint598.name = "r_elbow"
HAnimJoint598.center = [-0.1949,1.1388,-0.0620]
HAnimSegment599 = x3d.HAnimSegment()
HAnimSegment599.DEF = "STD_Segment_r_forearm"
HAnimSegment599.name = "r_forearm"
HAnimSite600 = x3d.HAnimSite()
HAnimSite600.DEF = "STD_Site_r_olecranon_pt"
HAnimSite600.name = "r_olecranon_pt"
HAnimSite600.translation = [-0.1907,1.1405,-0.1065]
TouchSensor601 = x3d.TouchSensor()
TouchSensor601.description = "HAnimSite r_olecranon_pt"

HAnimSite600.children.append(TouchSensor601)
Shape602 = x3d.Shape()
Shape602.USE = "HAnimSiteShape"

HAnimSite600.children.append(Shape602)

HAnimSegment599.children.append(HAnimSite600)
HAnimSite603 = x3d.HAnimSite()
HAnimSite603.DEF = "STD_Site_r_radiale_pt"
HAnimSite603.name = "r_radiale_pt"
HAnimSite603.translation = [-0.2130,1.1305,-0.1091]
TouchSensor604 = x3d.TouchSensor()
TouchSensor604.description = "HAnimSite r_radiale_pt"

HAnimSite603.children.append(TouchSensor604)
Shape605 = x3d.Shape()
Shape605.USE = "HAnimSiteShape"

HAnimSite603.children.append(Shape605)

HAnimSegment599.children.append(HAnimSite603)
HAnimSite606 = x3d.HAnimSite()
HAnimSite606.DEF = "STD_Site_r_radial_styloid_pt"
HAnimSite606.name = "r_radial_styloid_pt"
HAnimSite606.translation = [-0.1884,0.8676,-0.0360]
TouchSensor607 = x3d.TouchSensor()
TouchSensor607.description = "HAnimSite r_radial_styloid_pt"

HAnimSite606.children.append(TouchSensor607)
Shape608 = x3d.Shape()
Shape608.USE = "HAnimSiteShape"

HAnimSite606.children.append(Shape608)

HAnimSegment599.children.append(HAnimSite606)
HAnimSite609 = x3d.HAnimSite()
HAnimSite609.DEF = "STD_Site_r_humeral_medial_epicondyles_pt"
HAnimSite609.name = "r_humeral_medial_epicondyles_pt"
HAnimSite609.translation = [-0.1680,1.1298,-0.1062]
TouchSensor610 = x3d.TouchSensor()
TouchSensor610.description = "HAnimSite r_humeral_medial_epicondyles_pt"

HAnimSite609.children.append(TouchSensor610)
Shape611 = x3d.Shape()
Shape611.USE = "HAnimSiteShape"

HAnimSite609.children.append(Shape611)

HAnimSegment599.children.append(HAnimSite609)

HAnimJoint598.children.append(HAnimSegment599)
HAnimJoint612 = x3d.HAnimJoint()
HAnimJoint612.DEF = "STD_Joint_r_radiocarpal"
HAnimJoint612.name = "r_radiocarpal"
HAnimJoint612.center = [-0.1959,0.8694,-0.0521]
HAnimSegment613 = x3d.HAnimSegment()
HAnimSegment613.DEF = "STD_Segment_r_carpal"
HAnimSegment613.name = "r_carpal"
HAnimSite614 = x3d.HAnimSite()
HAnimSite614.DEF = "STD_Site_r_ulnar_styloid_pt"
HAnimSite614.name = "r_ulnar_styloid_pt"
HAnimSite614.translation = [-0.2117,0.8562,-0.0584]
TouchSensor615 = x3d.TouchSensor()
TouchSensor615.description = "HAnimSite r_ulnar_styloid_pt"

HAnimSite614.children.append(TouchSensor615)
Shape616 = x3d.Shape()
Shape616.USE = "HAnimSiteShape"

HAnimSite614.children.append(Shape616)

HAnimSegment613.children.append(HAnimSite614)

HAnimJoint612.children.append(HAnimSegment613)
HAnimJoint617 = x3d.HAnimJoint()
HAnimJoint617.DEF = "STD_Joint_r_midcarpal_1"
HAnimJoint617.name = "r_midcarpal_1"
HAnimJoint617.center = [0,0,0]
HAnimSegment618 = x3d.HAnimSegment()
HAnimSegment618.DEF = "STD_Segment_r_trapezium"
HAnimSegment618.name = "r_trapezium"

HAnimJoint617.children.append(HAnimSegment618)
HAnimJoint619 = x3d.HAnimJoint()
HAnimJoint619.DEF = "STD_Joint_r_carpometacarpal_1"
HAnimJoint619.name = "r_carpometacarpal_1"
HAnimJoint619.center = [-0.1899,0.8502,-0.0473]
HAnimSegment620 = x3d.HAnimSegment()
HAnimSegment620.DEF = "STD_Segment_r_metacarpal_1"
HAnimSegment620.name = "r_metacarpal_1"

HAnimJoint619.children.append(HAnimSegment620)
HAnimJoint621 = x3d.HAnimJoint()
HAnimJoint621.DEF = "STD_Joint_r_metacarpophalangeal_1"
HAnimJoint621.name = "r_metacarpophalangeal_1"
HAnimJoint621.center = [-0.1874,0.8256,0.0306]
HAnimSegment622 = x3d.HAnimSegment()
HAnimSegment622.DEF = "STD_Segment_r_carpal_proximal_phalanx_1"
HAnimSegment622.name = "r_carpal_proximal_phalanx_1"

HAnimJoint621.children.append(HAnimSegment622)
HAnimJoint623 = x3d.HAnimJoint()
HAnimJoint623.DEF = "STD_Joint_r_carpal_interphalangeal_1"
HAnimJoint623.name = "r_carpal_interphalangeal_1"
HAnimJoint623.center = [-0.1864,0.8190,0.0506]
HAnimSegment624 = x3d.HAnimSegment()
HAnimSegment624.DEF = "STD_Segment_r_carpal_distal_phalanx_1"
HAnimSegment624.name = "r_carpal_distal_phalanx_1"
HAnimSite625 = x3d.HAnimSite()
HAnimSite625.DEF = "STD_Site_r_carpal_distal_phalanx_1_tip"
HAnimSite625.name = "r_carpal_distal_phalanx_1_tip"
TouchSensor626 = x3d.TouchSensor()
TouchSensor626.description = "HAnimSite r_carpal_distal_phalanx_1_tip"

HAnimSite625.children.append(TouchSensor626)
Shape627 = x3d.Shape()
Shape627.USE = "HAnimSiteShape"

HAnimSite625.children.append(Shape627)

HAnimSegment624.children.append(HAnimSite625)

HAnimJoint623.children.append(HAnimSegment624)

HAnimJoint621.children.append(HAnimJoint623)

HAnimJoint619.children.append(HAnimJoint621)

HAnimJoint617.children.append(HAnimJoint619)

HAnimJoint612.children.append(HAnimJoint617)
HAnimJoint628 = x3d.HAnimJoint()
HAnimJoint628.DEF = "STD_Joint_r_midcarpal_2"
HAnimJoint628.name = "r_midcarpal_2"
HAnimJoint628.center = [0,0,0]
HAnimSegment629 = x3d.HAnimSegment()
HAnimSegment629.DEF = "STD_Segment_r_trapezoid"
HAnimSegment629.name = "r_trapezoid"

HAnimJoint628.children.append(HAnimSegment629)
HAnimJoint630 = x3d.HAnimJoint()
HAnimJoint630.DEF = "STD_Joint_r_carpometacarpal_2"
HAnimJoint630.name = "r_carpometacarpal_2"
HAnimJoint630.center = [-0.1961,0.8055,-0.0218]
HAnimSegment631 = x3d.HAnimSegment()
HAnimSegment631.DEF = "STD_Segment_r_metacarpal_2"
HAnimSegment631.name = "r_metacarpal_2"
HAnimSite632 = x3d.HAnimSite()
HAnimSite632.DEF = "STD_Site_r_metacarpal_phalanx_2_pt"
HAnimSite632.name = "r_metacarpal_phalanx_2_pt"
HAnimSite632.translation = [-0.1977,0.8169,-0.0177]
TouchSensor633 = x3d.TouchSensor()
TouchSensor633.description = "HAnimSite r_metacarpal_phalanx_2_pt"

HAnimSite632.children.append(TouchSensor633)
Shape634 = x3d.Shape()
Shape634.USE = "HAnimSiteShape"

HAnimSite632.children.append(Shape634)

HAnimSegment631.children.append(HAnimSite632)

HAnimJoint630.children.append(HAnimSegment631)
HAnimJoint635 = x3d.HAnimJoint()
HAnimJoint635.DEF = "STD_Joint_r_metacarpophalangeal_2"
HAnimJoint635.name = "r_metacarpophalangeal_2"
HAnimJoint635.center = [-0.1961,0.7846,-0.0218]
HAnimSegment636 = x3d.HAnimSegment()
HAnimSegment636.DEF = "STD_Segment_r_carpal_proximal_phalanx_2 "
HAnimSegment636.name = "r_carpal_proximal_phalanx_2 "

HAnimJoint635.children.append(HAnimSegment636)
HAnimJoint637 = x3d.HAnimJoint()
HAnimJoint637.DEF = "STD_Joint_r_carpal_proximal_interphalangeal_2"
HAnimJoint637.name = "r_carpal_proximal_interphalangeal_2"
HAnimJoint637.center = [-0.1954,0.7393,-0.0185]
HAnimSegment638 = x3d.HAnimSegment()
HAnimSegment638.DEF = "STD_Segment_r_carpal_middle_phalanx_2"
HAnimSegment638.name = "r_carpal_middle_phalanx_2"

HAnimJoint637.children.append(HAnimSegment638)
HAnimJoint639 = x3d.HAnimJoint()
HAnimJoint639.DEF = "STD_Joint_r_carpal_distal_interphalangeal_2"
HAnimJoint639.name = "r_carpal_distal_interphalangeal_2"
HAnimJoint639.center = [-0.1945,0.7169,-0.0173]
HAnimSegment640 = x3d.HAnimSegment()
HAnimSegment640.DEF = "STD_Segment_r_carpal_distal_phalanx_2"
HAnimSegment640.name = "r_carpal_distal_phalanx_2"
HAnimSite641 = x3d.HAnimSite()
HAnimSite641.DEF = "STD_Site_r_dactylion_pt"
HAnimSite641.name = "r_dactylion_pt"
HAnimSite641.translation = [-0.1941,0.6772,-0.0423]
TouchSensor642 = x3d.TouchSensor()
TouchSensor642.description = "HAnimSite r_dactylion_pt"

HAnimSite641.children.append(TouchSensor642)
Shape643 = x3d.Shape()
Shape643.USE = "HAnimSiteShape"

HAnimSite641.children.append(Shape643)

HAnimSegment640.children.append(HAnimSite641)
HAnimSite644 = x3d.HAnimSite()
HAnimSite644.DEF = "STD_Site_r_carpal_distal_phalanx_2_tip"
HAnimSite644.name = "r_carpal_distal_phalanx_2_tip"
TouchSensor645 = x3d.TouchSensor()
TouchSensor645.description = "HAnimSite r_carpal_distal_phalanx_2_tip"

HAnimSite644.children.append(TouchSensor645)
Shape646 = x3d.Shape()
Shape646.USE = "HAnimSiteShape"

HAnimSite644.children.append(Shape646)

HAnimSegment640.children.append(HAnimSite644)

HAnimJoint639.children.append(HAnimSegment640)

HAnimJoint637.children.append(HAnimJoint639)

HAnimJoint635.children.append(HAnimJoint637)

HAnimJoint630.children.append(HAnimJoint635)

HAnimJoint628.children.append(HAnimJoint630)

HAnimJoint612.children.append(HAnimJoint628)
HAnimJoint647 = x3d.HAnimJoint()
HAnimJoint647.DEF = "STD_Joint_r_midcarpal_3"
HAnimJoint647.name = "r_midcarpal_3"
HAnimJoint647.center = [0,0,0]
HAnimSegment648 = x3d.HAnimSegment()
HAnimSegment648.DEF = "STD_Segment_r_capitate"
HAnimSegment648.name = "r_capitate"

HAnimJoint647.children.append(HAnimSegment648)
HAnimJoint649 = x3d.HAnimJoint()
HAnimJoint649.DEF = "STD_Joint_r_carpometacarpal_3"
HAnimJoint649.name = "r_carpometacarpal_3"
HAnimJoint649.center = [-0.1972,0.8060,-0.0468]
HAnimSegment650 = x3d.HAnimSegment()
HAnimSegment650.DEF = "STD_Segment_r_metacarpal_3"
HAnimSegment650.name = "r_metacarpal_3"
HAnimSite651 = x3d.HAnimSite()
HAnimSite651.DEF = "STD_Site_r_metacarpal_phalanx_3_pt"
HAnimSite651.name = "r_metacarpal_phalanx_3_pt"
TouchSensor652 = x3d.TouchSensor()
TouchSensor652.description = "HAnimSite r_metacarpal_phalanx_3_pt"

HAnimSite651.children.append(TouchSensor652)
Shape653 = x3d.Shape()
Shape653.USE = "HAnimSiteShape"

HAnimSite651.children.append(Shape653)

HAnimSegment650.children.append(HAnimSite651)

HAnimJoint649.children.append(HAnimSegment650)
HAnimJoint654 = x3d.HAnimJoint()
HAnimJoint654.DEF = "STD_Joint_r_metacarpophalangeal_3"
HAnimJoint654.name = "r_metacarpophalangeal_3"
HAnimJoint654.center = [-0.1972,0.7849,-0.0468]
HAnimSegment655 = x3d.HAnimSegment()
HAnimSegment655.DEF = "STD_Segment_r_carpal_proximal_phalanx_3"
HAnimSegment655.name = "r_carpal_proximal_phalanx_3"

HAnimJoint654.children.append(HAnimSegment655)
HAnimJoint656 = x3d.HAnimJoint()
HAnimJoint656.DEF = "STD_Joint_r_carpal_proximal_interphalangeal_3"
HAnimJoint656.name = "r_carpal_proximal_interphalangeal_3"
HAnimJoint656.center = [-0.1950,0.7304,-0.0441]
HAnimSegment657 = x3d.HAnimSegment()
HAnimSegment657.DEF = "STD_Segment_r_carpal_middle_phalanx_3"
HAnimSegment657.name = "r_carpal_middle_phalanx_3"

HAnimJoint656.children.append(HAnimSegment657)
HAnimJoint658 = x3d.HAnimJoint()
HAnimJoint658.DEF = "STD_Joint_r_carpal_distal_interphalangeal_3"
HAnimJoint658.name = "r_carpal_distal_interphalangeal_3"
HAnimJoint658.center = [-0.1939,0.7042,-0.0432]
HAnimSegment659 = x3d.HAnimSegment()
HAnimSegment659.DEF = "STD_Segment_r_carpal_distal_phalanx_3"
HAnimSegment659.name = "r_carpal_distal_phalanx_3"
HAnimSite660 = x3d.HAnimSite()
HAnimSite660.DEF = "STD_Site_r_carpal_distal_phalanx_3_tip"
HAnimSite660.name = "r_carpal_distal_phalanx_3_tip"
TouchSensor661 = x3d.TouchSensor()
TouchSensor661.description = "HAnimSite r_carpal_distal_phalanx_3_tip"

HAnimSite660.children.append(TouchSensor661)
Shape662 = x3d.Shape()
Shape662.USE = "HAnimSiteShape"

HAnimSite660.children.append(Shape662)

HAnimSegment659.children.append(HAnimSite660)

HAnimJoint658.children.append(HAnimSegment659)

HAnimJoint656.children.append(HAnimJoint658)

HAnimJoint654.children.append(HAnimJoint656)

HAnimJoint649.children.append(HAnimJoint654)

HAnimJoint647.children.append(HAnimJoint649)

HAnimJoint612.children.append(HAnimJoint647)
HAnimJoint663 = x3d.HAnimJoint()
HAnimJoint663.DEF = "STD_Joint_r_midcarpal_4_5"
HAnimJoint663.name = "r_midcarpal_4_5"
HAnimJoint663.center = [0,0,0]
HAnimSegment664 = x3d.HAnimSegment()
HAnimSegment664.DEF = "STD_Segment_r_hamate"
HAnimSegment664.name = "r_hamate"

HAnimJoint663.children.append(HAnimSegment664)
HAnimJoint665 = x3d.HAnimJoint()
HAnimJoint665.DEF = "STD_Joint_r_carpometacarpal_4"
HAnimJoint665.name = "r_carpometacarpal_4"
HAnimJoint665.center = [-0.1951,0.8049,-0.0732]
HAnimSegment666 = x3d.HAnimSegment()
HAnimSegment666.DEF = "STD_Segment_r_metacarpal_4"
HAnimSegment666.name = "r_metacarpal_4"

HAnimJoint665.children.append(HAnimSegment666)
HAnimJoint667 = x3d.HAnimJoint()
HAnimJoint667.DEF = "STD_Joint_r_metacarpophalangeal_4"
HAnimJoint667.name = "r_metacarpophalangeal_4"
HAnimJoint667.center = [-0.1951,0.7845,-0.0732]
HAnimSegment668 = x3d.HAnimSegment()
HAnimSegment668.DEF = "STD_Segment_r_carpal_proximal_phalanx_4"
HAnimSegment668.name = "r_carpal_proximal_phalanx_4"

HAnimJoint667.children.append(HAnimSegment668)
HAnimJoint669 = x3d.HAnimJoint()
HAnimJoint669.DEF = "STD_Joint_r_carpal_proximal_interphalangeal_4"
HAnimJoint669.name = "r_carpal_proximal_interphalangeal_4"
HAnimJoint669.center = [-0.1920,0.7318,-0.0716]
HAnimSegment670 = x3d.HAnimSegment()
HAnimSegment670.DEF = "STD_Segment_r_carpal_middle_phalanx_4"
HAnimSegment670.name = "r_carpal_middle_phalanx_4"

HAnimJoint669.children.append(HAnimSegment670)
HAnimJoint671 = x3d.HAnimJoint()
HAnimJoint671.DEF = "STD_Joint_r_carpal_distal_interphalangeal_4"
HAnimJoint671.name = "r_carpal_distal_interphalangeal_4"
HAnimJoint671.center = [-0.1908,0.7077,-0.0706]
HAnimSegment672 = x3d.HAnimSegment()
HAnimSegment672.DEF = "STD_Segment_r_carpal_distal_phalanx_4"
HAnimSegment672.name = "r_carpal_distal_phalanx_4"
HAnimSite673 = x3d.HAnimSite()
HAnimSite673.DEF = "STD_Site_r_carpal_distal_phalanx_4_tip"
HAnimSite673.name = "r_carpal_distal_phalanx_4_tip"
TouchSensor674 = x3d.TouchSensor()
TouchSensor674.description = "HAnimSite r_carpal_distal_phalanx_4_tip"

HAnimSite673.children.append(TouchSensor674)
Shape675 = x3d.Shape()
Shape675.USE = "HAnimSiteShape"

HAnimSite673.children.append(Shape675)

HAnimSegment672.children.append(HAnimSite673)

HAnimJoint671.children.append(HAnimSegment672)

HAnimJoint669.children.append(HAnimJoint671)

HAnimJoint667.children.append(HAnimJoint669)

HAnimJoint665.children.append(HAnimJoint667)

HAnimJoint663.children.append(HAnimJoint665)
HAnimJoint676 = x3d.HAnimJoint()
HAnimJoint676.DEF = "STD_Joint_r_carpometacarpal_5"
HAnimJoint676.name = "r_carpometacarpal_5"
HAnimJoint676.center = [-0.1926,0.8096,-0.0975]
HAnimSegment677 = x3d.HAnimSegment()
HAnimSegment677.DEF = "STD_Segment_r_metacarpal_5"
HAnimSegment677.name = "r_metacarpal_5"
HAnimSite678 = x3d.HAnimSite()
HAnimSite678.DEF = "STD_Site_r_metacarpal_phalanx_5_pt"
HAnimSite678.name = "r_metacarpal_phalanx_5_pt"
HAnimSite678.translation = [-0.1929,0.7890,-0.1064]
TouchSensor679 = x3d.TouchSensor()
TouchSensor679.description = "HAnimSite r_metacarpal_phalanx_5_pt"

HAnimSite678.children.append(TouchSensor679)
Shape680 = x3d.Shape()
Shape680.USE = "HAnimSiteShape"

HAnimSite678.children.append(Shape680)

HAnimSegment677.children.append(HAnimSite678)

HAnimJoint676.children.append(HAnimSegment677)
HAnimJoint681 = x3d.HAnimJoint()
HAnimJoint681.DEF = "STD_Joint_r_metacarpophalangeal_5"
HAnimJoint681.name = "r_metacarpophalangeal_5"
HAnimJoint681.center = [-0.1926,0.7896,-0.0975]
HAnimSegment682 = x3d.HAnimSegment()
HAnimSegment682.DEF = "STD_Segment_r_carpal_proximal_phalanx_5"
HAnimSegment682.name = "r_carpal_proximal_phalanx_5"

HAnimJoint681.children.append(HAnimSegment682)
HAnimJoint683 = x3d.HAnimJoint()
HAnimJoint683.DEF = "STD_Joint_r_carpal_proximal_interphalangeal_5"
HAnimJoint683.name = "r_carpal_proximal_interphalangeal_5"
HAnimJoint683.center = [-0.1902,0.7483,-0.0963]
HAnimSegment684 = x3d.HAnimSegment()
HAnimSegment684.DEF = "STD_Segment_r_carpal_middle_phalanx_5"
HAnimSegment684.name = "r_carpal_middle_phalanx_5"

HAnimJoint683.children.append(HAnimSegment684)
HAnimJoint685 = x3d.HAnimJoint()
HAnimJoint685.DEF = "STD_Joint_r_carpal_distal_interphalangeal_5"
HAnimJoint685.name = "r_carpal_distal_interphalangeal_5"
HAnimJoint685.center = [-0.1908,0.7540,-0.0960]
HAnimSegment686 = x3d.HAnimSegment()
HAnimSegment686.DEF = "STD_Segment_r_carpal_distal_phalanx_5"
HAnimSegment686.name = "r_carpal_distal_phalanx_5"
HAnimSite687 = x3d.HAnimSite()
HAnimSite687.DEF = "STD_Site_r_carpal_distal_phalanx_5_tip"
HAnimSite687.name = "r_carpal_distal_phalanx_5_tip"
TouchSensor688 = x3d.TouchSensor()
TouchSensor688.description = "HAnimSite r_carpal_distal_phalanx_5_tip"

HAnimSite687.children.append(TouchSensor688)
Shape689 = x3d.Shape()
Shape689.USE = "HAnimSiteShape"

HAnimSite687.children.append(Shape689)

HAnimSegment686.children.append(HAnimSite687)

HAnimJoint685.children.append(HAnimSegment686)

HAnimJoint683.children.append(HAnimJoint685)

HAnimJoint681.children.append(HAnimJoint683)

HAnimJoint676.children.append(HAnimJoint681)

HAnimJoint663.children.append(HAnimJoint676)

HAnimJoint612.children.append(HAnimJoint663)

HAnimJoint598.children.append(HAnimJoint612)

HAnimJoint590.children.append(HAnimJoint598)

HAnimJoint588.children.append(HAnimJoint590)

HAnimJoint571.children.append(HAnimJoint588)

HAnimJoint360.children.append(HAnimJoint571)

HAnimJoint358.children.append(HAnimJoint360)

HAnimJoint356.children.append(HAnimJoint358)

HAnimJoint354.children.append(HAnimJoint356)

HAnimJoint349.children.append(HAnimJoint354)

HAnimJoint335.children.append(HAnimJoint349)

HAnimJoint333.children.append(HAnimJoint335)

HAnimJoint331.children.append(HAnimJoint333)

HAnimJoint323.children.append(HAnimJoint331)

HAnimJoint318.children.append(HAnimJoint323)

HAnimJoint316.children.append(HAnimJoint318)

HAnimJoint314.children.append(HAnimJoint316)

HAnimJoint312.children.append(HAnimJoint314)

HAnimJoint301.children.append(HAnimJoint312)

HAnimJoint299.children.append(HAnimJoint301)

HAnimJoint297.children.append(HAnimJoint299)

HAnimJoint286.children.append(HAnimJoint297)

HAnimJoint44.children.append(HAnimJoint286)

HAnimHumanoid43.joints.append(HAnimJoint44)
HAnimJoint690 = x3d.HAnimJoint()
HAnimJoint690.USE = "STD_Joint_humanoid_root"

HAnimHumanoid43.joints.append(HAnimJoint690)
HAnimSegment691 = x3d.HAnimSegment()
HAnimSegment691.USE = "STD_Segment_sacrum"

HAnimHumanoid43.segments.append(HAnimSegment691)
HAnimJoint692 = x3d.HAnimJoint()
HAnimJoint692.USE = "STD_Joint_sacroiliac"

HAnimHumanoid43.joints.append(HAnimJoint692)
HAnimSegment693 = x3d.HAnimSegment()
HAnimSegment693.USE = "STD_Segment_pelvis"

HAnimHumanoid43.segments.append(HAnimSegment693)
HAnimSite694 = x3d.HAnimSite()
HAnimSite694.USE = "STD_Site_r_iliocristale_pt"

HAnimHumanoid43.sites.append(HAnimSite694)
HAnimSite695 = x3d.HAnimSite()
HAnimSite695.USE = "STD_Site_l_iliocristale_pt"

HAnimHumanoid43.sites.append(HAnimSite695)
HAnimSite696 = x3d.HAnimSite()
HAnimSite696.USE = "STD_Site_buttocks_standing_wall_contact_point_pt"

HAnimHumanoid43.sites.append(HAnimSite696)
HAnimSite697 = x3d.HAnimSite()
HAnimSite697.USE = "STD_Site_crotch_pt"

HAnimHumanoid43.sites.append(HAnimSite697)
HAnimSite698 = x3d.HAnimSite()
HAnimSite698.USE = "STD_Site_l_asis_pt"

HAnimHumanoid43.sites.append(HAnimSite698)
HAnimSite699 = x3d.HAnimSite()
HAnimSite699.USE = "STD_Site_r_asis_pt"

HAnimHumanoid43.sites.append(HAnimSite699)
HAnimSite700 = x3d.HAnimSite()
HAnimSite700.USE = "STD_Site_l_trochanterion_pt"

HAnimHumanoid43.sites.append(HAnimSite700)
HAnimSite701 = x3d.HAnimSite()
HAnimSite701.USE = "STD_Site_r_trochanterion_pt"

HAnimHumanoid43.sites.append(HAnimSite701)
HAnimSite702 = x3d.HAnimSite()
HAnimSite702.USE = "STD_Site_l_psis_pt"

HAnimHumanoid43.sites.append(HAnimSite702)
HAnimSite703 = x3d.HAnimSite()
HAnimSite703.USE = "STD_Site_r_psis_pt"

HAnimHumanoid43.sites.append(HAnimSite703)
HAnimJoint704 = x3d.HAnimJoint()
HAnimJoint704.USE = "STD_Joint_l_hip"

HAnimHumanoid43.joints.append(HAnimJoint704)
HAnimSegment705 = x3d.HAnimSegment()
HAnimSegment705.USE = "STD_Segment_l_thigh"

HAnimHumanoid43.segments.append(HAnimSegment705)
HAnimSite706 = x3d.HAnimSite()
HAnimSite706.USE = "STD_Site_l_suprapatella_pt"

HAnimHumanoid43.sites.append(HAnimSite706)
HAnimSite707 = x3d.HAnimSite()
HAnimSite707.USE = "STD_Site_l_femoral_lateral_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite707)
HAnimSite708 = x3d.HAnimSite()
HAnimSite708.USE = "STD_Site_l_femoral_medial_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite708)
HAnimSite709 = x3d.HAnimSite()
HAnimSite709.USE = "STD_Site_l_knee_crease_pt"

HAnimHumanoid43.sites.append(HAnimSite709)
HAnimJoint710 = x3d.HAnimJoint()
HAnimJoint710.USE = "STD_Joint_l_knee"

HAnimHumanoid43.joints.append(HAnimJoint710)
HAnimSegment711 = x3d.HAnimSegment()
HAnimSegment711.USE = "STD_Segment_l_calf"

HAnimHumanoid43.segments.append(HAnimSegment711)
HAnimSite712 = x3d.HAnimSite()
HAnimSite712.USE = "STD_Site_l_tibiale_pt"

HAnimHumanoid43.sites.append(HAnimSite712)
HAnimSite713 = x3d.HAnimSite()
HAnimSite713.USE = "STD_Site_l_medial_malleolus_pt"

HAnimHumanoid43.sites.append(HAnimSite713)
HAnimSite714 = x3d.HAnimSite()
HAnimSite714.USE = "STD_Site_l_lateral_malleolus_pt"

HAnimHumanoid43.sites.append(HAnimSite714)
HAnimJoint715 = x3d.HAnimJoint()
HAnimJoint715.USE = "STD_Joint_l_talocrural"

HAnimHumanoid43.joints.append(HAnimJoint715)
HAnimSegment716 = x3d.HAnimSegment()
HAnimSegment716.USE = "STD_Segment_l_talus"

HAnimHumanoid43.segments.append(HAnimSegment716)
HAnimSite717 = x3d.HAnimSite()
HAnimSite717.USE = "STD_Site_l_sphyrion_pt"

HAnimHumanoid43.sites.append(HAnimSite717)
HAnimSite718 = x3d.HAnimSite()
HAnimSite718.USE = "STD_Site_l_calcaneus_posterior_pt"

HAnimHumanoid43.sites.append(HAnimSite718)
HAnimJoint719 = x3d.HAnimJoint()
HAnimJoint719.USE = "STD_Joint_l_talocalcaneonavicular"

HAnimHumanoid43.joints.append(HAnimJoint719)
HAnimSegment720 = x3d.HAnimSegment()
HAnimSegment720.USE = "STD_Segment_l_navicular"

HAnimHumanoid43.segments.append(HAnimSegment720)
HAnimJoint721 = x3d.HAnimJoint()
HAnimJoint721.USE = "STD_Joint_l_cuneonavicular_1"

HAnimHumanoid43.joints.append(HAnimJoint721)
HAnimSegment722 = x3d.HAnimSegment()
HAnimSegment722.USE = "STD_Segment_l_cuneiform_1"

HAnimHumanoid43.segments.append(HAnimSegment722)
HAnimJoint723 = x3d.HAnimJoint()
HAnimJoint723.USE = "STD_Joint_l_tarsometatarsal_1"

HAnimHumanoid43.joints.append(HAnimJoint723)
HAnimSegment724 = x3d.HAnimSegment()
HAnimSegment724.USE = "STD_Segment_l_metatarsal_1"

HAnimHumanoid43.segments.append(HAnimSegment724)
HAnimJoint725 = x3d.HAnimJoint()
HAnimJoint725.USE = "STD_Joint_l_metatarsophalangeal_1"

HAnimHumanoid43.joints.append(HAnimJoint725)
HAnimSegment726 = x3d.HAnimSegment()
HAnimSegment726.USE = "STD_Segment_l_tarsal_proximal_phalanx_1"

HAnimHumanoid43.segments.append(HAnimSegment726)
HAnimSite727 = x3d.HAnimSite()
HAnimSite727.USE = "STD_Site_l_metatarsal_phalanx_1_pt"

HAnimHumanoid43.sites.append(HAnimSite727)
HAnimJoint728 = x3d.HAnimJoint()
HAnimJoint728.USE = "STD_Joint_l_tarsal_interphalangeal_1"

HAnimHumanoid43.joints.append(HAnimJoint728)
HAnimSegment729 = x3d.HAnimSegment()
HAnimSegment729.USE = "STD_Segment_l_tarsal_distal_phalanx_1"

HAnimHumanoid43.segments.append(HAnimSegment729)
HAnimSite730 = x3d.HAnimSite()
HAnimSite730.USE = "STD_Site_l_tarsal_distal_phalanx_1_tip"

HAnimHumanoid43.sites.append(HAnimSite730)
HAnimJoint731 = x3d.HAnimJoint()
HAnimJoint731.USE = "STD_Joint_l_cuneonavicular_2"

HAnimHumanoid43.joints.append(HAnimJoint731)
HAnimSegment732 = x3d.HAnimSegment()
HAnimSegment732.USE = "STD_Segment_l_cuneiform_2"

HAnimHumanoid43.segments.append(HAnimSegment732)
HAnimJoint733 = x3d.HAnimJoint()
HAnimJoint733.USE = "STD_Joint_l_tarsometatarsal_2"

HAnimHumanoid43.joints.append(HAnimJoint733)
HAnimSegment734 = x3d.HAnimSegment()
HAnimSegment734.USE = "STD_Segment_l_metatarsal_2"

HAnimHumanoid43.segments.append(HAnimSegment734)
HAnimJoint735 = x3d.HAnimJoint()
HAnimJoint735.USE = "STD_Joint_l_metatarsophalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint735)
HAnimSegment736 = x3d.HAnimSegment()
HAnimSegment736.USE = "STD_Segment_l_tarsal_proximal_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment736)
HAnimJoint737 = x3d.HAnimJoint()
HAnimJoint737.USE = "STD_Joint_l_tarsal_proximal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint737)
HAnimSegment738 = x3d.HAnimSegment()
HAnimSegment738.USE = "STD_Segment_l_tarsal_middle_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment738)
HAnimJoint739 = x3d.HAnimJoint()
HAnimJoint739.USE = "STD_Joint_l_tarsal_distal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint739)
HAnimSegment740 = x3d.HAnimSegment()
HAnimSegment740.USE = "STD_Segment_l_tarsal_distal_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment740)
HAnimSite741 = x3d.HAnimSite()
HAnimSite741.USE = "STD_Site_l_tarsal_distal_phalanx_2_tip"

HAnimHumanoid43.sites.append(HAnimSite741)
HAnimJoint742 = x3d.HAnimJoint()
HAnimJoint742.USE = "STD_Joint_l_cuneonavicular_3"

HAnimHumanoid43.joints.append(HAnimJoint742)
HAnimSegment743 = x3d.HAnimSegment()
HAnimSegment743.USE = "STD_Segment_l_cuneiform_3"

HAnimHumanoid43.segments.append(HAnimSegment743)
HAnimJoint744 = x3d.HAnimJoint()
HAnimJoint744.USE = "STD_Joint_l_tarsometatarsal_3 "

HAnimHumanoid43.joints.append(HAnimJoint744)
HAnimSegment745 = x3d.HAnimSegment()
HAnimSegment745.USE = "STD_Segment_l_metatarsal_3"

HAnimHumanoid43.segments.append(HAnimSegment745)
HAnimJoint746 = x3d.HAnimJoint()
HAnimJoint746.USE = "STD_Joint_l_metatarsophalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint746)
HAnimSegment747 = x3d.HAnimSegment()
HAnimSegment747.USE = "STD_Segment_l_tarsal_proximal_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment747)
HAnimJoint748 = x3d.HAnimJoint()
HAnimJoint748.USE = "STD_Joint_l_tarsal_proximal_interphalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint748)
HAnimSegment749 = x3d.HAnimSegment()
HAnimSegment749.USE = "STD_Segment_l_tarsal_middle_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment749)
HAnimJoint750 = x3d.HAnimJoint()
HAnimJoint750.USE = "STD_Joint_l_tarsal_distal_interphalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint750)
HAnimSegment751 = x3d.HAnimSegment()
HAnimSegment751.USE = "STD_Segment_l_tarsal_distal_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment751)
HAnimSite752 = x3d.HAnimSite()
HAnimSite752.USE = "STD_Site_l_tarsal_distal_phalanx_3_tip"

HAnimHumanoid43.sites.append(HAnimSite752)
HAnimJoint753 = x3d.HAnimJoint()
HAnimJoint753.USE = "STD_Joint_l_calcaneocuboid"

HAnimHumanoid43.joints.append(HAnimJoint753)
HAnimSegment754 = x3d.HAnimSegment()
HAnimSegment754.USE = "STD_Segment_l_calcaneus"

HAnimHumanoid43.segments.append(HAnimSegment754)
HAnimJoint755 = x3d.HAnimJoint()
HAnimJoint755.USE = "STD_Joint_l_transversetarsal"

HAnimHumanoid43.joints.append(HAnimJoint755)
HAnimSegment756 = x3d.HAnimSegment()
HAnimSegment756.USE = "STD_Segment_l_cuboid"

HAnimHumanoid43.segments.append(HAnimSegment756)
HAnimJoint757 = x3d.HAnimJoint()
HAnimJoint757.USE = "STD_Joint_l_tarsometatarsal_4"

HAnimHumanoid43.joints.append(HAnimJoint757)
HAnimSegment758 = x3d.HAnimSegment()
HAnimSegment758.USE = "STD_Segment_l_metatarsal_4"

HAnimHumanoid43.segments.append(HAnimSegment758)
HAnimJoint759 = x3d.HAnimJoint()
HAnimJoint759.USE = "STD_Joint_l_metatarsophalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint759)
HAnimSegment760 = x3d.HAnimSegment()
HAnimSegment760.USE = "STD_Segment_l_tarsal_proximal_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment760)
HAnimJoint761 = x3d.HAnimJoint()
HAnimJoint761.USE = "STD_Joint_l_tarsal_proximal_interphalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint761)
HAnimSegment762 = x3d.HAnimSegment()
HAnimSegment762.USE = "STD_Segment_l_tarsal_middle_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment762)
HAnimJoint763 = x3d.HAnimJoint()
HAnimJoint763.USE = "STD_Joint_l_tarsal_distal_interphalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint763)
HAnimSegment764 = x3d.HAnimSegment()
HAnimSegment764.USE = "STD_Segment_l_tarsal_distal_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment764)
HAnimSite765 = x3d.HAnimSite()
HAnimSite765.USE = "STD_Site_l_tarsal_distal_phalanx_4_tip"

HAnimHumanoid43.sites.append(HAnimSite765)
HAnimJoint766 = x3d.HAnimJoint()
HAnimJoint766.USE = "STD_Joint_l_tarsometatarsal_5"

HAnimHumanoid43.joints.append(HAnimJoint766)
HAnimSegment767 = x3d.HAnimSegment()
HAnimSegment767.USE = "STD_Segment_l_metatarsal_5"

HAnimHumanoid43.segments.append(HAnimSegment767)
HAnimJoint768 = x3d.HAnimJoint()
HAnimJoint768.USE = "STD_Joint_l_metatarsophalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint768)
HAnimSegment769 = x3d.HAnimSegment()
HAnimSegment769.USE = "STD_Segment_l_tarsal_proximal_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment769)
HAnimSite770 = x3d.HAnimSite()
HAnimSite770.USE = "STD_Site_l_metatarsal_phalanx_5_pt"

HAnimHumanoid43.sites.append(HAnimSite770)
HAnimJoint771 = x3d.HAnimJoint()
HAnimJoint771.USE = "STD_Joint_l_tarsal_proximal_interphalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint771)
HAnimSegment772 = x3d.HAnimSegment()
HAnimSegment772.USE = "STD_Segment_l_tarsal_middle_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment772)
HAnimJoint773 = x3d.HAnimJoint()
HAnimJoint773.USE = "STD_Joint_l_tarsal_distal_interphalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint773)
HAnimSegment774 = x3d.HAnimSegment()
HAnimSegment774.USE = "STD_Segment_l_tarsal_distal_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment774)
HAnimSite775 = x3d.HAnimSite()
HAnimSite775.USE = "STD_Site_l_tarsal_distal_phalanx_5_tip"

HAnimHumanoid43.sites.append(HAnimSite775)
HAnimJoint776 = x3d.HAnimJoint()
HAnimJoint776.USE = "STD_Joint_r_hip"

HAnimHumanoid43.joints.append(HAnimJoint776)
HAnimSegment777 = x3d.HAnimSegment()
HAnimSegment777.USE = "STD_Segment_r_thigh"

HAnimHumanoid43.segments.append(HAnimSegment777)
HAnimSite778 = x3d.HAnimSite()
HAnimSite778.USE = "STD_Site_r_femoral_lateral_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite778)
HAnimSite779 = x3d.HAnimSite()
HAnimSite779.USE = "STD_Site_r_femoral_medial_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite779)
HAnimSite780 = x3d.HAnimSite()
HAnimSite780.USE = "STD_Site_r_suprapatella_pt"

HAnimHumanoid43.sites.append(HAnimSite780)
HAnimSite781 = x3d.HAnimSite()
HAnimSite781.USE = "STD_Site_r_knee_crease_pt"

HAnimHumanoid43.sites.append(HAnimSite781)
HAnimJoint782 = x3d.HAnimJoint()
HAnimJoint782.USE = "STD_Joint_r_knee"

HAnimHumanoid43.joints.append(HAnimJoint782)
HAnimSegment783 = x3d.HAnimSegment()
HAnimSegment783.USE = "STD_Segment_r_calf"

HAnimHumanoid43.segments.append(HAnimSegment783)
HAnimSite784 = x3d.HAnimSite()
HAnimSite784.USE = "STD_Site_r_tibiale_pt"

HAnimHumanoid43.sites.append(HAnimSite784)
HAnimSite785 = x3d.HAnimSite()
HAnimSite785.USE = "STD_Site_r_medial_malleolus_pt"

HAnimHumanoid43.sites.append(HAnimSite785)
HAnimSite786 = x3d.HAnimSite()
HAnimSite786.USE = "STD_Site_r_lateral_malleolus_pt"

HAnimHumanoid43.sites.append(HAnimSite786)
HAnimJoint787 = x3d.HAnimJoint()
HAnimJoint787.USE = "STD_Joint_r_talocrural"

HAnimHumanoid43.joints.append(HAnimJoint787)
HAnimSegment788 = x3d.HAnimSegment()
HAnimSegment788.USE = "STD_Segment_r_talus"

HAnimHumanoid43.segments.append(HAnimSegment788)
HAnimSite789 = x3d.HAnimSite()
HAnimSite789.USE = "STD_Site_r_sphyrion_pt"

HAnimHumanoid43.sites.append(HAnimSite789)
HAnimSite790 = x3d.HAnimSite()
HAnimSite790.USE = "STD_Site_r_calcaneus_posterior_pt"

HAnimHumanoid43.sites.append(HAnimSite790)
HAnimJoint791 = x3d.HAnimJoint()
HAnimJoint791.USE = "STD_Joint_r_talocalcaneonavicular"

HAnimHumanoid43.joints.append(HAnimJoint791)
HAnimSegment792 = x3d.HAnimSegment()
HAnimSegment792.USE = "STD_Segment_r_navicular"

HAnimHumanoid43.segments.append(HAnimSegment792)
HAnimJoint793 = x3d.HAnimJoint()
HAnimJoint793.USE = "STD_Joint_r_cuneonavicular_1"

HAnimHumanoid43.joints.append(HAnimJoint793)
HAnimSegment794 = x3d.HAnimSegment()
HAnimSegment794.USE = "STD_Segment_r_cuneiform_1"

HAnimHumanoid43.segments.append(HAnimSegment794)
HAnimJoint795 = x3d.HAnimJoint()
HAnimJoint795.USE = "STD_Joint_r_tarsometatarsal_1"

HAnimHumanoid43.joints.append(HAnimJoint795)
HAnimSegment796 = x3d.HAnimSegment()
HAnimSegment796.USE = "STD_Segment_r_metatarsal_1"

HAnimHumanoid43.segments.append(HAnimSegment796)
HAnimJoint797 = x3d.HAnimJoint()
HAnimJoint797.USE = "STD_Joint_r_metatarsophalangeal_1"

HAnimHumanoid43.joints.append(HAnimJoint797)
HAnimSegment798 = x3d.HAnimSegment()
HAnimSegment798.USE = "STD_Segment_r_tarsal_proximal_phalanx_1"

HAnimHumanoid43.segments.append(HAnimSegment798)
HAnimSite799 = x3d.HAnimSite()
HAnimSite799.USE = "STD_Site_r_metatarsal_phalanx_1_pt"

HAnimHumanoid43.sites.append(HAnimSite799)
HAnimJoint800 = x3d.HAnimJoint()
HAnimJoint800.USE = "STD_Joint_r_tarsal_interphalangeal_1"

HAnimHumanoid43.joints.append(HAnimJoint800)
HAnimSegment801 = x3d.HAnimSegment()
HAnimSegment801.USE = "STD_Segment_r_tarsal_distal_phalanx_1"

HAnimHumanoid43.segments.append(HAnimSegment801)
HAnimSite802 = x3d.HAnimSite()
HAnimSite802.USE = "STD_Site_r_tarsal_distal_phalanx_1_tip"

HAnimHumanoid43.sites.append(HAnimSite802)
HAnimJoint803 = x3d.HAnimJoint()
HAnimJoint803.USE = "STD_Joint_r_cuneonavicular_2"

HAnimHumanoid43.joints.append(HAnimJoint803)
HAnimSegment804 = x3d.HAnimSegment()
HAnimSegment804.USE = "STD_Segment_r_cuneiform_2"

HAnimHumanoid43.segments.append(HAnimSegment804)
HAnimJoint805 = x3d.HAnimJoint()
HAnimJoint805.USE = "STD_Joint_r_tarsometatarsal_2"

HAnimHumanoid43.joints.append(HAnimJoint805)
HAnimSegment806 = x3d.HAnimSegment()
HAnimSegment806.USE = "STD_Segment_r_metatarsal_2"

HAnimHumanoid43.segments.append(HAnimSegment806)
HAnimJoint807 = x3d.HAnimJoint()
HAnimJoint807.USE = "STD_Joint_r_metatarsophalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint807)
HAnimSegment808 = x3d.HAnimSegment()
HAnimSegment808.USE = "STD_Segment_r_tarsal_proximal_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment808)
HAnimJoint809 = x3d.HAnimJoint()
HAnimJoint809.USE = "STD_Joint_r_tarsal_proximal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint809)
HAnimSegment810 = x3d.HAnimSegment()
HAnimSegment810.USE = "STD_Segment_r_tarsal_middle_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment810)
HAnimJoint811 = x3d.HAnimJoint()
HAnimJoint811.USE = "STD_Joint_r_tarsal_distal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint811)
HAnimSegment812 = x3d.HAnimSegment()
HAnimSegment812.USE = "STD_Segment_r_tarsal_distal_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment812)
HAnimSite813 = x3d.HAnimSite()
HAnimSite813.USE = "STD_Site_r_tarsal_distal_phalanx_2_tip"

HAnimHumanoid43.sites.append(HAnimSite813)
HAnimJoint814 = x3d.HAnimJoint()
HAnimJoint814.USE = "STD_Joint_r_cuneonavicular_3"

HAnimHumanoid43.joints.append(HAnimJoint814)
HAnimSegment815 = x3d.HAnimSegment()
HAnimSegment815.USE = "STD_Segment_r_cuneiform_3"

HAnimHumanoid43.segments.append(HAnimSegment815)
HAnimJoint816 = x3d.HAnimJoint()
HAnimJoint816.USE = "STD_Joint_r_tarsometatarsal_3 "

HAnimHumanoid43.joints.append(HAnimJoint816)
HAnimSegment817 = x3d.HAnimSegment()
HAnimSegment817.USE = "STD_Segment_r_metatarsal_3"

HAnimHumanoid43.segments.append(HAnimSegment817)
HAnimJoint818 = x3d.HAnimJoint()
HAnimJoint818.USE = "STD_Joint_r_metatarsophalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint818)
HAnimSegment819 = x3d.HAnimSegment()
HAnimSegment819.USE = "STD_Segment_r_tarsal_proximal_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment819)
HAnimJoint820 = x3d.HAnimJoint()
HAnimJoint820.USE = "STD_Joint_r_tarsal_proximal_interphalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint820)
HAnimSegment821 = x3d.HAnimSegment()
HAnimSegment821.USE = "STD_Segment_r_tarsal_middle_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment821)
HAnimJoint822 = x3d.HAnimJoint()
HAnimJoint822.USE = "STD_Joint_r_tarsal_distal_interphalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint822)
HAnimSegment823 = x3d.HAnimSegment()
HAnimSegment823.USE = "STD_Segment_r_tarsal_distal_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment823)
HAnimSite824 = x3d.HAnimSite()
HAnimSite824.USE = "STD_Site_r_tarsal_distal_phalanx_3_tip"

HAnimHumanoid43.sites.append(HAnimSite824)
HAnimJoint825 = x3d.HAnimJoint()
HAnimJoint825.USE = "STD_Joint_r_calcaneocuboid"

HAnimHumanoid43.joints.append(HAnimJoint825)
HAnimSegment826 = x3d.HAnimSegment()
HAnimSegment826.USE = "STD_Segment_r_calcaneus"

HAnimHumanoid43.segments.append(HAnimSegment826)
HAnimJoint827 = x3d.HAnimJoint()
HAnimJoint827.USE = "STD_Joint_r_transversetarsal"

HAnimHumanoid43.joints.append(HAnimJoint827)
HAnimSegment828 = x3d.HAnimSegment()
HAnimSegment828.USE = "STD_Segment_r_cuboid"

HAnimHumanoid43.segments.append(HAnimSegment828)
HAnimJoint829 = x3d.HAnimJoint()
HAnimJoint829.USE = "STD_Joint_r_tarsometatarsal_4"

HAnimHumanoid43.joints.append(HAnimJoint829)
HAnimSegment830 = x3d.HAnimSegment()
HAnimSegment830.USE = "STD_Segment_r_metatarsal_4"

HAnimHumanoid43.segments.append(HAnimSegment830)
HAnimJoint831 = x3d.HAnimJoint()
HAnimJoint831.USE = "STD_Joint_r_metatarsophalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint831)
HAnimSegment832 = x3d.HAnimSegment()
HAnimSegment832.USE = "STD_Segment_r_tarsal_proximal_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment832)
HAnimJoint833 = x3d.HAnimJoint()
HAnimJoint833.USE = "STD_Joint_r_tarsal_proximal_interphalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint833)
HAnimSegment834 = x3d.HAnimSegment()
HAnimSegment834.USE = "STD_Segment_r_tarsal_middle_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment834)
HAnimJoint835 = x3d.HAnimJoint()
HAnimJoint835.USE = "STD_Joint_r_tarsal_distal_interphalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint835)
HAnimSegment836 = x3d.HAnimSegment()
HAnimSegment836.USE = "STD_Segment_r_tarsal_distal_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment836)
HAnimSite837 = x3d.HAnimSite()
HAnimSite837.USE = "STD_Site_r_tarsal_distal_phalanx_4_tip"

HAnimHumanoid43.sites.append(HAnimSite837)
HAnimJoint838 = x3d.HAnimJoint()
HAnimJoint838.USE = "STD_Joint_r_tarsometatarsal_5"

HAnimHumanoid43.joints.append(HAnimJoint838)
HAnimSegment839 = x3d.HAnimSegment()
HAnimSegment839.USE = "STD_Segment_r_metatarsal_5"

HAnimHumanoid43.segments.append(HAnimSegment839)
HAnimJoint840 = x3d.HAnimJoint()
HAnimJoint840.USE = "STD_Joint_r_metatarsophalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint840)
HAnimSegment841 = x3d.HAnimSegment()
HAnimSegment841.USE = "STD_Segment_r_tarsal_proximal_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment841)
HAnimSite842 = x3d.HAnimSite()
HAnimSite842.USE = "STD_Site_r_metatarsal_phalanx_5_pt"

HAnimHumanoid43.sites.append(HAnimSite842)
HAnimJoint843 = x3d.HAnimJoint()
HAnimJoint843.USE = "STD_Joint_r_tarsal_proximal_interphalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint843)
HAnimSegment844 = x3d.HAnimSegment()
HAnimSegment844.USE = "STD_Segment_r_tarsal_middle_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment844)
HAnimJoint845 = x3d.HAnimJoint()
HAnimJoint845.USE = "STD_Joint_r_tarsal_distal_interphalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint845)
HAnimSegment846 = x3d.HAnimSegment()
HAnimSegment846.USE = "STD_Segment_r_tarsal_distal_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment846)
HAnimSite847 = x3d.HAnimSite()
HAnimSite847.USE = "STD_Site_r_tarsal_distal_phalanx_5_tip"

HAnimHumanoid43.sites.append(HAnimSite847)
HAnimJoint848 = x3d.HAnimJoint()
HAnimJoint848.USE = "STD_Joint_vl5"

HAnimHumanoid43.joints.append(HAnimJoint848)
HAnimSegment849 = x3d.HAnimSegment()
HAnimSegment849.USE = "STD_Segment_l5"

HAnimHumanoid43.segments.append(HAnimSegment849)
HAnimSite850 = x3d.HAnimSite()
HAnimSite850.USE = "STD_Site_waist_preferred_anterior_pt"

HAnimHumanoid43.sites.append(HAnimSite850)
HAnimSite851 = x3d.HAnimSite()
HAnimSite851.USE = "STD_Site_waist_preferred_posterior_pt"

HAnimHumanoid43.sites.append(HAnimSite851)
HAnimSite852 = x3d.HAnimSite()
HAnimSite852.USE = "STD_Site_navel_pt"

HAnimHumanoid43.sites.append(HAnimSite852)
HAnimJoint853 = x3d.HAnimJoint()
HAnimJoint853.USE = "STD_Joint_vl4"

HAnimHumanoid43.joints.append(HAnimJoint853)
HAnimSegment854 = x3d.HAnimSegment()
HAnimSegment854.USE = "STD_Segment_l4"

HAnimHumanoid43.segments.append(HAnimSegment854)
HAnimJoint855 = x3d.HAnimJoint()
HAnimJoint855.USE = "STD_Joint_vl3"

HAnimHumanoid43.joints.append(HAnimJoint855)
HAnimSegment856 = x3d.HAnimSegment()
HAnimSegment856.USE = "STD_Segment_l3"

HAnimHumanoid43.segments.append(HAnimSegment856)
HAnimJoint857 = x3d.HAnimJoint()
HAnimJoint857.USE = "STD_Joint_vl2"

HAnimHumanoid43.joints.append(HAnimJoint857)
HAnimSegment858 = x3d.HAnimSegment()
HAnimSegment858.USE = "STD_Segment_l2"

HAnimHumanoid43.segments.append(HAnimSegment858)
HAnimSite859 = x3d.HAnimSite()
HAnimSite859.USE = "STD_Site_spine_2_middle_back_pt"

HAnimHumanoid43.sites.append(HAnimSite859)
HAnimSite860 = x3d.HAnimSite()
HAnimSite860.USE = "STD_Site_r_rib10_pt"

HAnimHumanoid43.sites.append(HAnimSite860)
HAnimSite861 = x3d.HAnimSite()
HAnimSite861.USE = "STD_Site_l_rib10_pt"

HAnimHumanoid43.sites.append(HAnimSite861)
HAnimJoint862 = x3d.HAnimJoint()
HAnimJoint862.USE = "STD_Joint_vl1"

HAnimHumanoid43.joints.append(HAnimJoint862)
HAnimSegment863 = x3d.HAnimSegment()
HAnimSegment863.USE = "STD_Segment_l1"

HAnimHumanoid43.segments.append(HAnimSegment863)
HAnimJoint864 = x3d.HAnimJoint()
HAnimJoint864.USE = "STD_Joint_vt12"

HAnimHumanoid43.joints.append(HAnimJoint864)
HAnimSegment865 = x3d.HAnimSegment()
HAnimSegment865.USE = "STD_Segment_t12"

HAnimHumanoid43.segments.append(HAnimSegment865)
HAnimJoint866 = x3d.HAnimJoint()
HAnimJoint866.USE = "STD_Joint_vt11"

HAnimHumanoid43.joints.append(HAnimJoint866)
HAnimSegment867 = x3d.HAnimSegment()
HAnimSegment867.USE = "STD_Segment_t11"

HAnimHumanoid43.segments.append(HAnimSegment867)
HAnimJoint868 = x3d.HAnimJoint()
HAnimJoint868.USE = "STD_Joint_vt10"

HAnimHumanoid43.joints.append(HAnimJoint868)
HAnimSegment869 = x3d.HAnimSegment()
HAnimSegment869.USE = "STD_Segment_t10"

HAnimHumanoid43.segments.append(HAnimSegment869)
HAnimSite870 = x3d.HAnimSite()
HAnimSite870.USE = "STD_Site_substernale_pt"

HAnimHumanoid43.sites.append(HAnimSite870)
HAnimJoint871 = x3d.HAnimJoint()
HAnimJoint871.USE = "STD_Joint_vt9"

HAnimHumanoid43.joints.append(HAnimJoint871)
HAnimSegment872 = x3d.HAnimSegment()
HAnimSegment872.USE = "STD_Segment_t9"

HAnimHumanoid43.segments.append(HAnimSegment872)
HAnimSite873 = x3d.HAnimSite()
HAnimSite873.USE = "STD_Site_r_thelion_pt"

HAnimHumanoid43.sites.append(HAnimSite873)
HAnimSite874 = x3d.HAnimSite()
HAnimSite874.USE = "STD_Site_l_thelion_pt"

HAnimHumanoid43.sites.append(HAnimSite874)
HAnimJoint875 = x3d.HAnimJoint()
HAnimJoint875.USE = "STD_Joint_vt8"

HAnimHumanoid43.joints.append(HAnimJoint875)
HAnimSegment876 = x3d.HAnimSegment()
HAnimSegment876.USE = "STD_Segment_t8"

HAnimHumanoid43.segments.append(HAnimSegment876)
HAnimJoint877 = x3d.HAnimJoint()
HAnimJoint877.USE = "STD_Joint_vt7"

HAnimHumanoid43.joints.append(HAnimJoint877)
HAnimSegment878 = x3d.HAnimSegment()
HAnimSegment878.USE = "STD_Segment_t7"

HAnimHumanoid43.segments.append(HAnimSegment878)
HAnimJoint879 = x3d.HAnimJoint()
HAnimJoint879.USE = "STD_Joint_vt6"

HAnimHumanoid43.joints.append(HAnimJoint879)
HAnimSegment880 = x3d.HAnimSegment()
HAnimSegment880.USE = "STD_Segment_t6"

HAnimHumanoid43.segments.append(HAnimSegment880)
HAnimSite881 = x3d.HAnimSite()
HAnimSite881.USE = "STD_Site_r_chest_midsagittal_plane_pt"

HAnimHumanoid43.sites.append(HAnimSite881)
HAnimSite882 = x3d.HAnimSite()
HAnimSite882.USE = "STD_Site_l_chest_midsagittal_plane_pt"

HAnimHumanoid43.sites.append(HAnimSite882)
HAnimSite883 = x3d.HAnimSite()
HAnimSite883.USE = "STD_Site_rear_center_midsagittal_plane_pt"

HAnimHumanoid43.sites.append(HAnimSite883)
HAnimSite884 = x3d.HAnimSite()
HAnimSite884.USE = "STD_Site_mesosternale_pt"

HAnimHumanoid43.sites.append(HAnimSite884)
HAnimJoint885 = x3d.HAnimJoint()
HAnimJoint885.USE = "STD_Joint_vt5"

HAnimHumanoid43.joints.append(HAnimJoint885)
HAnimSegment886 = x3d.HAnimSegment()
HAnimSegment886.USE = "STD_Segment_t5"

HAnimHumanoid43.segments.append(HAnimSegment886)
HAnimSite887 = x3d.HAnimSite()
HAnimSite887.USE = "STD_Site_spine_1_middle_back_pt"

HAnimHumanoid43.sites.append(HAnimSite887)
HAnimJoint888 = x3d.HAnimJoint()
HAnimJoint888.USE = "STD_Joint_vt4"

HAnimHumanoid43.joints.append(HAnimJoint888)
HAnimSegment889 = x3d.HAnimSegment()
HAnimSegment889.USE = "STD_Segment_t4"

HAnimHumanoid43.segments.append(HAnimSegment889)
HAnimJoint890 = x3d.HAnimJoint()
HAnimJoint890.USE = "STD_Joint_vt3"

HAnimHumanoid43.joints.append(HAnimJoint890)
HAnimSegment891 = x3d.HAnimSegment()
HAnimSegment891.USE = "STD_Segment_t3"

HAnimHumanoid43.segments.append(HAnimSegment891)
HAnimJoint892 = x3d.HAnimJoint()
HAnimJoint892.USE = "STD_Joint_vt2"

HAnimHumanoid43.joints.append(HAnimJoint892)
HAnimSegment893 = x3d.HAnimSegment()
HAnimSegment893.USE = "STD_Segment_t2"

HAnimHumanoid43.segments.append(HAnimSegment893)
HAnimJoint894 = x3d.HAnimJoint()
HAnimJoint894.USE = "STD_Joint_vt1"

HAnimHumanoid43.joints.append(HAnimJoint894)
HAnimSegment895 = x3d.HAnimSegment()
HAnimSegment895.USE = "STD_Segment_t1"

HAnimHumanoid43.segments.append(HAnimSegment895)
HAnimSite896 = x3d.HAnimSite()
HAnimSite896.USE = "STD_Site_cervicale_pt"

HAnimHumanoid43.sites.append(HAnimSite896)
HAnimSite897 = x3d.HAnimSite()
HAnimSite897.USE = "STD_Site_suprasternale_pt"

HAnimHumanoid43.sites.append(HAnimSite897)
HAnimJoint898 = x3d.HAnimJoint()
HAnimJoint898.USE = "STD_Joint_vc7"

HAnimHumanoid43.joints.append(HAnimJoint898)
HAnimSegment899 = x3d.HAnimSegment()
HAnimSegment899.USE = "STD_Segment_c7"

HAnimHumanoid43.segments.append(HAnimSegment899)
HAnimSite900 = x3d.HAnimSite()
HAnimSite900.USE = "STD_Site_l_neck_base_pt"

HAnimHumanoid43.sites.append(HAnimSite900)
HAnimSite901 = x3d.HAnimSite()
HAnimSite901.USE = "STD_Site_r_neck_base_pt"

HAnimHumanoid43.sites.append(HAnimSite901)
HAnimJoint902 = x3d.HAnimJoint()
HAnimJoint902.USE = "STD_Joint_vc6"

HAnimHumanoid43.joints.append(HAnimJoint902)
HAnimSegment903 = x3d.HAnimSegment()
HAnimSegment903.USE = "STD_Segment_c6"

HAnimHumanoid43.segments.append(HAnimSegment903)
HAnimJoint904 = x3d.HAnimJoint()
HAnimJoint904.USE = "STD_Joint_vc5"

HAnimHumanoid43.joints.append(HAnimJoint904)
HAnimSegment905 = x3d.HAnimSegment()
HAnimSegment905.USE = "STD_Segment_c5"

HAnimHumanoid43.segments.append(HAnimSegment905)
HAnimJoint906 = x3d.HAnimJoint()
HAnimJoint906.USE = "STD_Joint_vc4"

HAnimHumanoid43.joints.append(HAnimJoint906)
HAnimSegment907 = x3d.HAnimSegment()
HAnimSegment907.USE = "STD_Segment_c4"

HAnimHumanoid43.segments.append(HAnimSegment907)
HAnimJoint908 = x3d.HAnimJoint()
HAnimJoint908.USE = "STD_Joint_vc3"

HAnimHumanoid43.joints.append(HAnimJoint908)
HAnimSegment909 = x3d.HAnimSegment()
HAnimSegment909.USE = "STD_Segment_c3"

HAnimHumanoid43.segments.append(HAnimSegment909)
HAnimJoint910 = x3d.HAnimJoint()
HAnimJoint910.USE = "STD_Joint_vc2"

HAnimHumanoid43.joints.append(HAnimJoint910)
HAnimSegment911 = x3d.HAnimSegment()
HAnimSegment911.USE = "STD_Segment_c2"

HAnimHumanoid43.segments.append(HAnimSegment911)
HAnimSite912 = x3d.HAnimSite()
HAnimSite912.USE = "STD_Site_adams_apple_pt"

HAnimHumanoid43.sites.append(HAnimSite912)
HAnimJoint913 = x3d.HAnimJoint()
HAnimJoint913.USE = "STD_Joint_vc1"

HAnimHumanoid43.joints.append(HAnimJoint913)
HAnimSegment914 = x3d.HAnimSegment()
HAnimSegment914.USE = "STD_Segment_c1"

HAnimHumanoid43.segments.append(HAnimSegment914)
HAnimJoint915 = x3d.HAnimJoint()
HAnimJoint915.USE = "STD_Joint_skullbase"

HAnimHumanoid43.joints.append(HAnimJoint915)
HAnimSegment916 = x3d.HAnimSegment()
HAnimSegment916.USE = "STD_Segment_skull"

HAnimHumanoid43.segments.append(HAnimSegment916)
HAnimSite917 = x3d.HAnimSite()
HAnimSite917.USE = "STD_Site_glabella_pt"

HAnimHumanoid43.sites.append(HAnimSite917)
HAnimSite918 = x3d.HAnimSite()
HAnimSite918.USE = "STD_Site_sellion_pt"

HAnimHumanoid43.sites.append(HAnimSite918)
HAnimSite919 = x3d.HAnimSite()
HAnimSite919.USE = "STD_Site_r_tragion_pt"

HAnimHumanoid43.sites.append(HAnimSite919)
HAnimSite920 = x3d.HAnimSite()
HAnimSite920.USE = "STD_Site_l_tragion_pt"

HAnimHumanoid43.sites.append(HAnimSite920)
HAnimSite921 = x3d.HAnimSite()
HAnimSite921.USE = "STD_Site_l_infraorbitale_pt"

HAnimHumanoid43.sites.append(HAnimSite921)
HAnimSite922 = x3d.HAnimSite()
HAnimSite922.USE = "STD_Site_r_infraorbitale_pt"

HAnimHumanoid43.sites.append(HAnimSite922)
HAnimSite923 = x3d.HAnimSite()
HAnimSite923.USE = "STD_Site_l_ectocanthus_pt"

HAnimHumanoid43.sites.append(HAnimSite923)
HAnimSite924 = x3d.HAnimSite()
HAnimSite924.USE = "STD_Site_nuchale_pt"

HAnimHumanoid43.sites.append(HAnimSite924)
HAnimSite925 = x3d.HAnimSite()
HAnimSite925.USE = "STD_Site_r_ectocanthus_pt"

HAnimHumanoid43.sites.append(HAnimSite925)
HAnimSite926 = x3d.HAnimSite()
HAnimSite926.USE = "STD_Site_skull_vertex_pt"

HAnimHumanoid43.sites.append(HAnimSite926)
HAnimSite927 = x3d.HAnimSite()
HAnimSite927.USE = "STD_Site_opisthocranion_pt"

HAnimHumanoid43.sites.append(HAnimSite927)
HAnimJoint928 = x3d.HAnimJoint()
HAnimJoint928.USE = "STD_Joint_l_eyelid_joint"

HAnimHumanoid43.joints.append(HAnimJoint928)
HAnimSegment929 = x3d.HAnimSegment()
HAnimSegment929.USE = "STD_Segment_l_eyelid"

HAnimHumanoid43.segments.append(HAnimSegment929)
HAnimJoint930 = x3d.HAnimJoint()
HAnimJoint930.USE = "STD_Joint_r_eyelid_joint"

HAnimHumanoid43.joints.append(HAnimJoint930)
HAnimSegment931 = x3d.HAnimSegment()
HAnimSegment931.USE = "STD_Segment_r_eyelid"

HAnimHumanoid43.segments.append(HAnimSegment931)
HAnimJoint932 = x3d.HAnimJoint()
HAnimJoint932.USE = "STD_Joint_l_eyeball_joint"

HAnimHumanoid43.joints.append(HAnimJoint932)
HAnimSegment933 = x3d.HAnimSegment()
HAnimSegment933.USE = "STD_Segment_l_eyeball"

HAnimHumanoid43.segments.append(HAnimSegment933)
HAnimJoint934 = x3d.HAnimJoint()
HAnimJoint934.USE = "STD_Joint_r_eyeball_joint"

HAnimHumanoid43.joints.append(HAnimJoint934)
HAnimSegment935 = x3d.HAnimSegment()
HAnimSegment935.USE = "STD_Segment_r_eyeball"

HAnimHumanoid43.segments.append(HAnimSegment935)
HAnimJoint936 = x3d.HAnimJoint()
HAnimJoint936.USE = "STD_Joint_l_eyebrow_joint"

HAnimHumanoid43.joints.append(HAnimJoint936)
HAnimSegment937 = x3d.HAnimSegment()
HAnimSegment937.USE = "STD_Segment_l_eyebrow"

HAnimHumanoid43.segments.append(HAnimSegment937)
HAnimJoint938 = x3d.HAnimJoint()
HAnimJoint938.USE = "STD_Joint_r_eyebrow_joint"

HAnimHumanoid43.joints.append(HAnimJoint938)
HAnimSegment939 = x3d.HAnimSegment()
HAnimSegment939.USE = "STD_Segment_r_eyebrow"

HAnimHumanoid43.segments.append(HAnimSegment939)
HAnimJoint940 = x3d.HAnimJoint()
HAnimJoint940.USE = "STD_Joint_temporomandibular"

HAnimHumanoid43.joints.append(HAnimJoint940)
HAnimSegment941 = x3d.HAnimSegment()
HAnimSegment941.USE = "STD_Segment_jaw"

HAnimHumanoid43.segments.append(HAnimSegment941)
HAnimSite942 = x3d.HAnimSite()
HAnimSite942.USE = "STD_Site_supramenton_pt"

HAnimHumanoid43.sites.append(HAnimSite942)
HAnimSite943 = x3d.HAnimSite()
HAnimSite943.USE = "STD_Site_menton_pt"

HAnimHumanoid43.sites.append(HAnimSite943)
HAnimSite944 = x3d.HAnimSite()
HAnimSite944.USE = "STD_Site_r_gonion_pt"

HAnimHumanoid43.sites.append(HAnimSite944)
HAnimSite945 = x3d.HAnimSite()
HAnimSite945.USE = "STD_Site_l_gonion_pt"

HAnimHumanoid43.sites.append(HAnimSite945)
HAnimJoint946 = x3d.HAnimJoint()
HAnimJoint946.USE = "STD_Joint_l_sternoclavicular"

HAnimHumanoid43.joints.append(HAnimJoint946)
HAnimSegment947 = x3d.HAnimSegment()
HAnimSegment947.USE = "STD_Segment_l_clavicle"

HAnimHumanoid43.segments.append(HAnimSegment947)
HAnimSite948 = x3d.HAnimSite()
HAnimSite948.USE = "STD_Site_l_axilla_distal_pt"

HAnimHumanoid43.sites.append(HAnimSite948)
HAnimSite949 = x3d.HAnimSite()
HAnimSite949.USE = "STD_Site_l_axilla_posterior_folds_pt"

HAnimHumanoid43.sites.append(HAnimSite949)
HAnimSite950 = x3d.HAnimSite()
HAnimSite950.USE = "STD_Site_l_axilla_proximal_pt"

HAnimHumanoid43.sites.append(HAnimSite950)
HAnimSite951 = x3d.HAnimSite()
HAnimSite951.USE = "STD_Site_l_acromion_pt"

HAnimHumanoid43.sites.append(HAnimSite951)
HAnimSite952 = x3d.HAnimSite()
HAnimSite952.USE = "STD_Site_l_clavicale_pt"

HAnimHumanoid43.sites.append(HAnimSite952)
HAnimJoint953 = x3d.HAnimJoint()
HAnimJoint953.USE = "STD_Joint_l_acromioclavicular"

HAnimHumanoid43.joints.append(HAnimJoint953)
HAnimSegment954 = x3d.HAnimSegment()
HAnimSegment954.USE = "STD_Segment_l_scapula"

HAnimHumanoid43.segments.append(HAnimSegment954)
HAnimJoint955 = x3d.HAnimJoint()
HAnimJoint955.USE = "STD_Joint_l_shoulder"

HAnimHumanoid43.joints.append(HAnimJoint955)
HAnimSegment956 = x3d.HAnimSegment()
HAnimSegment956.USE = "STD_Segment_l_upperarm"

HAnimHumanoid43.segments.append(HAnimSegment956)
HAnimSite957 = x3d.HAnimSite()
HAnimSite957.USE = "STD_Site_l_bideltoid_pt"

HAnimHumanoid43.sites.append(HAnimSite957)
HAnimSite958 = x3d.HAnimSite()
HAnimSite958.USE = "STD_Site_l_humeral_lateral_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite958)
HAnimJoint959 = x3d.HAnimJoint()
HAnimJoint959.USE = "STD_Joint_l_elbow"

HAnimHumanoid43.joints.append(HAnimJoint959)
HAnimSegment960 = x3d.HAnimSegment()
HAnimSegment960.USE = "STD_Segment_l_forearm"

HAnimHumanoid43.segments.append(HAnimSegment960)
HAnimSite961 = x3d.HAnimSite()
HAnimSite961.USE = "STD_Site_l_olecranon_pt"

HAnimHumanoid43.sites.append(HAnimSite961)
HAnimSite962 = x3d.HAnimSite()
HAnimSite962.USE = "STD_Site_l_humeral_medial_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite962)
HAnimSite963 = x3d.HAnimSite()
HAnimSite963.USE = "STD_Site_l_radiale_pt"

HAnimHumanoid43.sites.append(HAnimSite963)
HAnimSite964 = x3d.HAnimSite()
HAnimSite964.USE = "STD_Site_l_radial_styloid_pt"

HAnimHumanoid43.sites.append(HAnimSite964)
HAnimJoint965 = x3d.HAnimJoint()
HAnimJoint965.USE = "STD_Joint_l_radiocarpal"

HAnimHumanoid43.joints.append(HAnimJoint965)
HAnimSegment966 = x3d.HAnimSegment()
HAnimSegment966.USE = "STD_Segment_l_carpal"

HAnimHumanoid43.segments.append(HAnimSegment966)
HAnimSite967 = x3d.HAnimSite()
HAnimSite967.USE = "STD_Site_l_ulnar_styloid_pt"

HAnimHumanoid43.sites.append(HAnimSite967)
HAnimJoint968 = x3d.HAnimJoint()
HAnimJoint968.USE = "STD_Joint_l_midcarpal_1"

HAnimHumanoid43.joints.append(HAnimJoint968)
HAnimSegment969 = x3d.HAnimSegment()
HAnimSegment969.USE = "STD_Segment_l_trapezium"

HAnimHumanoid43.segments.append(HAnimSegment969)
HAnimJoint970 = x3d.HAnimJoint()
HAnimJoint970.USE = "STD_Joint_l_carpometacarpal_1"

HAnimHumanoid43.joints.append(HAnimJoint970)
HAnimSegment971 = x3d.HAnimSegment()
HAnimSegment971.USE = "STD_Segment_l_metacarpal_1"

HAnimHumanoid43.segments.append(HAnimSegment971)
HAnimJoint972 = x3d.HAnimJoint()
HAnimJoint972.USE = "STD_Joint_l_metacarpophalangeal_1"

HAnimHumanoid43.joints.append(HAnimJoint972)
HAnimSegment973 = x3d.HAnimSegment()
HAnimSegment973.USE = "STD_Segment_l_carpal_proximal_phalanx_1"

HAnimHumanoid43.segments.append(HAnimSegment973)
HAnimJoint974 = x3d.HAnimJoint()
HAnimJoint974.USE = "STD_Joint_l_carpal_interphalangeal_1"

HAnimHumanoid43.joints.append(HAnimJoint974)
HAnimSegment975 = x3d.HAnimSegment()
HAnimSegment975.USE = "STD_Segment_l_carpal_distal_phalanx_1"

HAnimHumanoid43.segments.append(HAnimSegment975)
HAnimSite976 = x3d.HAnimSite()
HAnimSite976.USE = "STD_Site_l_carpal_distal_phalanx_1_tip"

HAnimHumanoid43.sites.append(HAnimSite976)
HAnimJoint977 = x3d.HAnimJoint()
HAnimJoint977.USE = "STD_Joint_l_midcarpal_2"

HAnimHumanoid43.joints.append(HAnimJoint977)
HAnimSegment978 = x3d.HAnimSegment()
HAnimSegment978.USE = "STD_Segment_l_trapezoid"

HAnimHumanoid43.segments.append(HAnimSegment978)
HAnimJoint979 = x3d.HAnimJoint()
HAnimJoint979.USE = "STD_Joint_l_carpometacarpal_2"

HAnimHumanoid43.joints.append(HAnimJoint979)
HAnimSegment980 = x3d.HAnimSegment()
HAnimSegment980.USE = "STD_Segment_l_metacarpal_2"

HAnimHumanoid43.segments.append(HAnimSegment980)
HAnimSite981 = x3d.HAnimSite()
HAnimSite981.USE = "STD_Site_l_metacarpal_phalanx_2_pt"

HAnimHumanoid43.sites.append(HAnimSite981)
HAnimJoint982 = x3d.HAnimJoint()
HAnimJoint982.USE = "STD_Joint_l_metacarpophalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint982)
HAnimSegment983 = x3d.HAnimSegment()
HAnimSegment983.USE = "STD_Segment_l_carpal_proximal_phalanx_2 "

HAnimHumanoid43.segments.append(HAnimSegment983)
HAnimJoint984 = x3d.HAnimJoint()
HAnimJoint984.USE = "STD_Joint_l_carpal_proximal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint984)
HAnimSegment985 = x3d.HAnimSegment()
HAnimSegment985.USE = "STD_Segment_l_carpal_middle_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment985)
HAnimJoint986 = x3d.HAnimJoint()
HAnimJoint986.USE = "STD_Joint_l_carpal_distal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint986)
HAnimSegment987 = x3d.HAnimSegment()
HAnimSegment987.USE = "STD_Segment_l_carpal_distal_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment987)
HAnimSite988 = x3d.HAnimSite()
HAnimSite988.USE = "STD_Site_l_dactylion_pt"

HAnimHumanoid43.sites.append(HAnimSite988)
HAnimSite989 = x3d.HAnimSite()
HAnimSite989.USE = "STD_Site_l_carpal_distal_phalanx_2_tip"

HAnimHumanoid43.sites.append(HAnimSite989)
HAnimJoint990 = x3d.HAnimJoint()
HAnimJoint990.USE = "STD_Joint_l_midcarpal_3"

HAnimHumanoid43.joints.append(HAnimJoint990)
HAnimSegment991 = x3d.HAnimSegment()
HAnimSegment991.USE = "STD_Segment_l_capitate"

HAnimHumanoid43.segments.append(HAnimSegment991)
HAnimJoint992 = x3d.HAnimJoint()
HAnimJoint992.USE = "STD_Joint_l_carpometacarpal_3"

HAnimHumanoid43.joints.append(HAnimJoint992)
HAnimSegment993 = x3d.HAnimSegment()
HAnimSegment993.USE = "STD_Segment_l_metacarpal_3"

HAnimHumanoid43.segments.append(HAnimSegment993)
HAnimSite994 = x3d.HAnimSite()
HAnimSite994.USE = "STD_Site_l_metacarpal_phalanx_3_pt"

HAnimHumanoid43.sites.append(HAnimSite994)
HAnimJoint995 = x3d.HAnimJoint()
HAnimJoint995.USE = "STD_Joint_l_metacarpophalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint995)
HAnimSegment996 = x3d.HAnimSegment()
HAnimSegment996.USE = "STD_Segment_l_carpal_proximal_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment996)
HAnimJoint997 = x3d.HAnimJoint()
HAnimJoint997.USE = "STD_Joint_l_carpal_proximal_interphalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint997)
HAnimSegment998 = x3d.HAnimSegment()
HAnimSegment998.USE = "STD_Segment_l_carpal_middle_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment998)
HAnimJoint999 = x3d.HAnimJoint()
HAnimJoint999.USE = "STD_Joint_l_carpal_distal_interphalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint999)
HAnimSegment1000 = x3d.HAnimSegment()
HAnimSegment1000.USE = "STD_Segment_l_carpal_distal_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment1000)
HAnimSite1001 = x3d.HAnimSite()
HAnimSite1001.USE = "STD_Site_l_carpal_distal_phalanx_3_tip"

HAnimHumanoid43.sites.append(HAnimSite1001)
HAnimJoint1002 = x3d.HAnimJoint()
HAnimJoint1002.USE = "STD_Joint_l_midcarpal_4_5"

HAnimHumanoid43.joints.append(HAnimJoint1002)
HAnimSegment1003 = x3d.HAnimSegment()
HAnimSegment1003.USE = "STD_Segment_l_hamate"

HAnimHumanoid43.segments.append(HAnimSegment1003)
HAnimJoint1004 = x3d.HAnimJoint()
HAnimJoint1004.USE = "STD_Joint_l_carpometacarpal_4"

HAnimHumanoid43.joints.append(HAnimJoint1004)
HAnimSegment1005 = x3d.HAnimSegment()
HAnimSegment1005.USE = "STD_Segment_l_metacarpal_4"

HAnimHumanoid43.segments.append(HAnimSegment1005)
HAnimJoint1006 = x3d.HAnimJoint()
HAnimJoint1006.USE = "STD_Joint_l_metacarpophalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint1006)
HAnimSegment1007 = x3d.HAnimSegment()
HAnimSegment1007.USE = "STD_Segment_l_carpal_proximal_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment1007)
HAnimJoint1008 = x3d.HAnimJoint()
HAnimJoint1008.USE = "STD_Joint_l_carpal_proximal_interphalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint1008)
HAnimSegment1009 = x3d.HAnimSegment()
HAnimSegment1009.USE = "STD_Segment_l_carpal_middle_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment1009)
HAnimJoint1010 = x3d.HAnimJoint()
HAnimJoint1010.USE = "STD_Joint_l_carpal_distal_interphalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint1010)
HAnimSegment1011 = x3d.HAnimSegment()
HAnimSegment1011.USE = "STD_Segment_l_carpal_distal_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment1011)
HAnimSite1012 = x3d.HAnimSite()
HAnimSite1012.USE = "STD_Site_l_carpal_distal_phalanx_4_tip"

HAnimHumanoid43.sites.append(HAnimSite1012)
HAnimJoint1013 = x3d.HAnimJoint()
HAnimJoint1013.USE = "STD_Joint_l_carpometacarpal_5"

HAnimHumanoid43.joints.append(HAnimJoint1013)
HAnimSegment1014 = x3d.HAnimSegment()
HAnimSegment1014.USE = "STD_Segment_l_metacarpal_5"

HAnimHumanoid43.segments.append(HAnimSegment1014)
HAnimSite1015 = x3d.HAnimSite()
HAnimSite1015.USE = "STD_Site_l_metacarpal_phalanx_5_pt"

HAnimHumanoid43.sites.append(HAnimSite1015)
HAnimJoint1016 = x3d.HAnimJoint()
HAnimJoint1016.USE = "STD_Joint_l_metacarpophalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint1016)
HAnimSegment1017 = x3d.HAnimSegment()
HAnimSegment1017.USE = "STD_Segment_l_carpal_proximal_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment1017)
HAnimJoint1018 = x3d.HAnimJoint()
HAnimJoint1018.USE = "STD_Joint_l_carpal_proximal_interphalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint1018)
HAnimSegment1019 = x3d.HAnimSegment()
HAnimSegment1019.USE = "STD_Segment_l_carpal_middle_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment1019)
HAnimJoint1020 = x3d.HAnimJoint()
HAnimJoint1020.USE = "STD_Joint_l_carpal_distal_interphalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint1020)
HAnimSegment1021 = x3d.HAnimSegment()
HAnimSegment1021.USE = "STD_Segment_l_carpal_distal_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment1021)
HAnimSite1022 = x3d.HAnimSite()
HAnimSite1022.USE = "STD_Site_l_carpal_distal_phalanx_5_tip"

HAnimHumanoid43.sites.append(HAnimSite1022)
HAnimJoint1023 = x3d.HAnimJoint()
HAnimJoint1023.USE = "STD_Joint_r_sternoclavicular"

HAnimHumanoid43.joints.append(HAnimJoint1023)
HAnimSegment1024 = x3d.HAnimSegment()
HAnimSegment1024.USE = "STD_Segment_r_clavicle"

HAnimHumanoid43.segments.append(HAnimSegment1024)
HAnimSite1025 = x3d.HAnimSite()
HAnimSite1025.USE = "STD_Site_r_axilla_distal_pt"

HAnimHumanoid43.sites.append(HAnimSite1025)
HAnimSite1026 = x3d.HAnimSite()
HAnimSite1026.USE = "STD_Site_r_axilla_posterior_folds_pt"

HAnimHumanoid43.sites.append(HAnimSite1026)
HAnimSite1027 = x3d.HAnimSite()
HAnimSite1027.USE = "STD_Site_r_axilla_proximal_pt"

HAnimHumanoid43.sites.append(HAnimSite1027)
HAnimSite1028 = x3d.HAnimSite()
HAnimSite1028.USE = "STD_Site_r_acromion_pt"

HAnimHumanoid43.sites.append(HAnimSite1028)
HAnimSite1029 = x3d.HAnimSite()
HAnimSite1029.USE = "STD_Site_r_clavicale_pt"

HAnimHumanoid43.sites.append(HAnimSite1029)
HAnimJoint1030 = x3d.HAnimJoint()
HAnimJoint1030.USE = "STD_Joint_r_acromioclavicular"

HAnimHumanoid43.joints.append(HAnimJoint1030)
HAnimSegment1031 = x3d.HAnimSegment()
HAnimSegment1031.USE = "STD_Segment_r_scapula"

HAnimHumanoid43.segments.append(HAnimSegment1031)
HAnimJoint1032 = x3d.HAnimJoint()
HAnimJoint1032.USE = "STD_Joint_r_shoulder"

HAnimHumanoid43.joints.append(HAnimJoint1032)
HAnimSegment1033 = x3d.HAnimSegment()
HAnimSegment1033.USE = "STD_Segment_r_upperarm"

HAnimHumanoid43.segments.append(HAnimSegment1033)
HAnimSite1034 = x3d.HAnimSite()
HAnimSite1034.USE = "STD_Site_r_bideltoid_pt"

HAnimHumanoid43.sites.append(HAnimSite1034)
HAnimSite1035 = x3d.HAnimSite()
HAnimSite1035.USE = "STD_Site_r_humeral_lateral_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite1035)
HAnimJoint1036 = x3d.HAnimJoint()
HAnimJoint1036.USE = "STD_Joint_r_elbow"

HAnimHumanoid43.joints.append(HAnimJoint1036)
HAnimSegment1037 = x3d.HAnimSegment()
HAnimSegment1037.USE = "STD_Segment_r_forearm"

HAnimHumanoid43.segments.append(HAnimSegment1037)
HAnimSite1038 = x3d.HAnimSite()
HAnimSite1038.USE = "STD_Site_r_olecranon_pt"

HAnimHumanoid43.sites.append(HAnimSite1038)
HAnimSite1039 = x3d.HAnimSite()
HAnimSite1039.USE = "STD_Site_r_radiale_pt"

HAnimHumanoid43.sites.append(HAnimSite1039)
HAnimSite1040 = x3d.HAnimSite()
HAnimSite1040.USE = "STD_Site_r_radial_styloid_pt"

HAnimHumanoid43.sites.append(HAnimSite1040)
HAnimSite1041 = x3d.HAnimSite()
HAnimSite1041.USE = "STD_Site_r_humeral_medial_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite1041)
HAnimJoint1042 = x3d.HAnimJoint()
HAnimJoint1042.USE = "STD_Joint_r_radiocarpal"

HAnimHumanoid43.joints.append(HAnimJoint1042)
HAnimSegment1043 = x3d.HAnimSegment()
HAnimSegment1043.USE = "STD_Segment_r_carpal"

HAnimHumanoid43.segments.append(HAnimSegment1043)
HAnimSite1044 = x3d.HAnimSite()
HAnimSite1044.USE = "STD_Site_r_ulnar_styloid_pt"

HAnimHumanoid43.sites.append(HAnimSite1044)
HAnimJoint1045 = x3d.HAnimJoint()
HAnimJoint1045.USE = "STD_Joint_r_midcarpal_1"

HAnimHumanoid43.joints.append(HAnimJoint1045)
HAnimSegment1046 = x3d.HAnimSegment()
HAnimSegment1046.USE = "STD_Segment_r_trapezium"

HAnimHumanoid43.segments.append(HAnimSegment1046)
HAnimJoint1047 = x3d.HAnimJoint()
HAnimJoint1047.USE = "STD_Joint_r_carpometacarpal_1"

HAnimHumanoid43.joints.append(HAnimJoint1047)
HAnimSegment1048 = x3d.HAnimSegment()
HAnimSegment1048.USE = "STD_Segment_r_metacarpal_1"

HAnimHumanoid43.segments.append(HAnimSegment1048)
HAnimJoint1049 = x3d.HAnimJoint()
HAnimJoint1049.USE = "STD_Joint_r_metacarpophalangeal_1"

HAnimHumanoid43.joints.append(HAnimJoint1049)
HAnimSegment1050 = x3d.HAnimSegment()
HAnimSegment1050.USE = "STD_Segment_r_carpal_proximal_phalanx_1"

HAnimHumanoid43.segments.append(HAnimSegment1050)
HAnimJoint1051 = x3d.HAnimJoint()
HAnimJoint1051.USE = "STD_Joint_r_carpal_interphalangeal_1"

HAnimHumanoid43.joints.append(HAnimJoint1051)
HAnimSegment1052 = x3d.HAnimSegment()
HAnimSegment1052.USE = "STD_Segment_r_carpal_distal_phalanx_1"

HAnimHumanoid43.segments.append(HAnimSegment1052)
HAnimSite1053 = x3d.HAnimSite()
HAnimSite1053.USE = "STD_Site_r_carpal_distal_phalanx_1_tip"

HAnimHumanoid43.sites.append(HAnimSite1053)
HAnimJoint1054 = x3d.HAnimJoint()
HAnimJoint1054.USE = "STD_Joint_r_midcarpal_2"

HAnimHumanoid43.joints.append(HAnimJoint1054)
HAnimSegment1055 = x3d.HAnimSegment()
HAnimSegment1055.USE = "STD_Segment_r_trapezoid"

HAnimHumanoid43.segments.append(HAnimSegment1055)
HAnimJoint1056 = x3d.HAnimJoint()
HAnimJoint1056.USE = "STD_Joint_r_carpometacarpal_2"

HAnimHumanoid43.joints.append(HAnimJoint1056)
HAnimSegment1057 = x3d.HAnimSegment()
HAnimSegment1057.USE = "STD_Segment_r_metacarpal_2"

HAnimHumanoid43.segments.append(HAnimSegment1057)
HAnimSite1058 = x3d.HAnimSite()
HAnimSite1058.USE = "STD_Site_r_metacarpal_phalanx_2_pt"

HAnimHumanoid43.sites.append(HAnimSite1058)
HAnimJoint1059 = x3d.HAnimJoint()
HAnimJoint1059.USE = "STD_Joint_r_metacarpophalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1059)
HAnimSegment1060 = x3d.HAnimSegment()
HAnimSegment1060.USE = "STD_Segment_r_carpal_proximal_phalanx_2 "

HAnimHumanoid43.segments.append(HAnimSegment1060)
HAnimJoint1061 = x3d.HAnimJoint()
HAnimJoint1061.USE = "STD_Joint_r_carpal_proximal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1061)
HAnimSegment1062 = x3d.HAnimSegment()
HAnimSegment1062.USE = "STD_Segment_r_carpal_middle_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment1062)
HAnimJoint1063 = x3d.HAnimJoint()
HAnimJoint1063.USE = "STD_Joint_r_carpal_distal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1063)
HAnimSegment1064 = x3d.HAnimSegment()
HAnimSegment1064.USE = "STD_Segment_r_carpal_distal_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment1064)
HAnimSite1065 = x3d.HAnimSite()
HAnimSite1065.USE = "STD_Site_r_dactylion_pt"

HAnimHumanoid43.sites.append(HAnimSite1065)
HAnimSite1066 = x3d.HAnimSite()
HAnimSite1066.USE = "STD_Site_r_carpal_distal_phalanx_2_tip"

HAnimHumanoid43.sites.append(HAnimSite1066)
HAnimJoint1067 = x3d.HAnimJoint()
HAnimJoint1067.USE = "STD_Joint_r_midcarpal_3"

HAnimHumanoid43.joints.append(HAnimJoint1067)
HAnimSegment1068 = x3d.HAnimSegment()
HAnimSegment1068.USE = "STD_Segment_r_capitate"

HAnimHumanoid43.segments.append(HAnimSegment1068)
HAnimJoint1069 = x3d.HAnimJoint()
HAnimJoint1069.USE = "STD_Joint_r_carpometacarpal_3"

HAnimHumanoid43.joints.append(HAnimJoint1069)
HAnimSegment1070 = x3d.HAnimSegment()
HAnimSegment1070.USE = "STD_Segment_r_metacarpal_3"

HAnimHumanoid43.segments.append(HAnimSegment1070)
HAnimSite1071 = x3d.HAnimSite()
HAnimSite1071.USE = "STD_Site_r_metacarpal_phalanx_3_pt"

HAnimHumanoid43.sites.append(HAnimSite1071)
HAnimJoint1072 = x3d.HAnimJoint()
HAnimJoint1072.USE = "STD_Joint_r_metacarpophalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint1072)
HAnimSegment1073 = x3d.HAnimSegment()
HAnimSegment1073.USE = "STD_Segment_r_carpal_proximal_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment1073)
HAnimJoint1074 = x3d.HAnimJoint()
HAnimJoint1074.USE = "STD_Joint_r_carpal_proximal_interphalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint1074)
HAnimSegment1075 = x3d.HAnimSegment()
HAnimSegment1075.USE = "STD_Segment_r_carpal_middle_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment1075)
HAnimJoint1076 = x3d.HAnimJoint()
HAnimJoint1076.USE = "STD_Joint_r_carpal_distal_interphalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint1076)
HAnimSegment1077 = x3d.HAnimSegment()
HAnimSegment1077.USE = "STD_Segment_r_carpal_distal_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment1077)
HAnimSite1078 = x3d.HAnimSite()
HAnimSite1078.USE = "STD_Site_r_carpal_distal_phalanx_3_tip"

HAnimHumanoid43.sites.append(HAnimSite1078)
HAnimJoint1079 = x3d.HAnimJoint()
HAnimJoint1079.USE = "STD_Joint_r_midcarpal_4_5"

HAnimHumanoid43.joints.append(HAnimJoint1079)
HAnimSegment1080 = x3d.HAnimSegment()
HAnimSegment1080.USE = "STD_Segment_r_hamate"

HAnimHumanoid43.segments.append(HAnimSegment1080)
HAnimJoint1081 = x3d.HAnimJoint()
HAnimJoint1081.USE = "STD_Joint_r_carpometacarpal_4"

HAnimHumanoid43.joints.append(HAnimJoint1081)
HAnimSegment1082 = x3d.HAnimSegment()
HAnimSegment1082.USE = "STD_Segment_r_metacarpal_4"

HAnimHumanoid43.segments.append(HAnimSegment1082)
HAnimJoint1083 = x3d.HAnimJoint()
HAnimJoint1083.USE = "STD_Joint_r_metacarpophalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint1083)
HAnimSegment1084 = x3d.HAnimSegment()
HAnimSegment1084.USE = "STD_Segment_r_carpal_proximal_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment1084)
HAnimJoint1085 = x3d.HAnimJoint()
HAnimJoint1085.USE = "STD_Joint_r_carpal_proximal_interphalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint1085)
HAnimSegment1086 = x3d.HAnimSegment()
HAnimSegment1086.USE = "STD_Segment_r_carpal_middle_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment1086)
HAnimJoint1087 = x3d.HAnimJoint()
HAnimJoint1087.USE = "STD_Joint_r_carpal_distal_interphalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint1087)
HAnimSegment1088 = x3d.HAnimSegment()
HAnimSegment1088.USE = "STD_Segment_r_carpal_distal_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment1088)
HAnimSite1089 = x3d.HAnimSite()
HAnimSite1089.USE = "STD_Site_r_carpal_distal_phalanx_4_tip"

HAnimHumanoid43.sites.append(HAnimSite1089)
HAnimJoint1090 = x3d.HAnimJoint()
HAnimJoint1090.USE = "STD_Joint_r_carpometacarpal_5"

HAnimHumanoid43.joints.append(HAnimJoint1090)
HAnimSegment1091 = x3d.HAnimSegment()
HAnimSegment1091.USE = "STD_Segment_r_metacarpal_5"

HAnimHumanoid43.segments.append(HAnimSegment1091)
HAnimSite1092 = x3d.HAnimSite()
HAnimSite1092.USE = "STD_Site_r_metacarpal_phalanx_5_pt"

HAnimHumanoid43.sites.append(HAnimSite1092)
HAnimJoint1093 = x3d.HAnimJoint()
HAnimJoint1093.USE = "STD_Joint_r_metacarpophalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint1093)
HAnimSegment1094 = x3d.HAnimSegment()
HAnimSegment1094.USE = "STD_Segment_r_carpal_proximal_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment1094)
HAnimJoint1095 = x3d.HAnimJoint()
HAnimJoint1095.USE = "STD_Joint_r_carpal_proximal_interphalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint1095)
HAnimSegment1096 = x3d.HAnimSegment()
HAnimSegment1096.USE = "STD_Segment_r_carpal_middle_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment1096)
HAnimJoint1097 = x3d.HAnimJoint()
HAnimJoint1097.USE = "STD_Joint_r_carpal_distal_interphalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint1097)
HAnimSegment1098 = x3d.HAnimSegment()
HAnimSegment1098.USE = "STD_Segment_r_carpal_distal_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment1098)
HAnimSite1099 = x3d.HAnimSite()
HAnimSite1099.USE = "STD_Site_r_carpal_distal_phalanx_5_tip"

HAnimHumanoid43.sites.append(HAnimSite1099)

HAnimHumanoid10.skeleton.append(HAnimHumanoid10)

X3D0.Scene = Scene10
f = open("skeletonJoe_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
