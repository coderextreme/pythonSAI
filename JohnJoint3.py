print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Immersive"
X3D0.version = "4.0"
head1 = x3d.head()
component2 = x3d.component()
component2.name = "HAnim"
component2.level = 1

head1.children.append(component2)
meta3 = x3d.meta()
meta3.name = "title"
meta3.content = "JohnBoy.x3d"

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
meta7.name = "modified"
meta7.content = "14 Jan 2023"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.name = "creator"
meta8.content = "John Carlson"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "created"
meta9.content = "9 November 2020"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "license"
meta10.content = "../license.html"

head1.children.append(meta10)

X3D0.head = head1
Scene11 = x3d.Scene()
Transform12 = x3d.Transform()
#DEF for markerfor XYZ axes
Shape13 = x3d.Shape()
Shape13.DEF = "AxisLinesShape"
#RGB lines showing XYZ axes
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

Scene11.children.append(Transform12)
Group17 = x3d.Group()
#DEFS for markers of skeleton joints, segments, and sites
Transform18 = x3d.Transform()
#<Transform translation='0 2 0' scale='1 1 1'> <Shape DEF='HAnimRootShape'> <Sphere radius='0.02' /> <Appearance> <Material DEF='HAnimRootMaterial' diffuseColor='0.8 0 0' transparency='0.3'/> </Appearance> </Shape> </Transform>
Transform19 = x3d.Transform()
Transform19.translation = [0,2.1,0]
Shape20 = x3d.Shape()
Shape20.DEF = "HAnimJointShape"
Sphere21 = x3d.Sphere()
Sphere21.radius = 0.02

Shape20.geometry = Sphere21
Appearance22 = x3d.Appearance()
Material23 = x3d.Material()
Material23.DEF = "HAnimJointMaterial"
Material23.diffuseColor = [0,0,0.8]
Material23.transparency = 0.3

Appearance22.material = Material23

Shape20.appearance = Appearance22

Transform19.children.append(Shape20)

Transform18.children.append(Transform19)
Transform24 = x3d.Transform()
Transform24.translation = [0,2.05,0]
Shape25 = x3d.Shape()
Shape25.DEF = "HAnimSegmentLine"
LineSet26 = x3d.LineSet()
LineSet26.vertexCount = [2]
ColorRGBA27 = x3d.ColorRGBA()
ColorRGBA27.DEF = "HAnimSegmentLineColorRGBA"

LineSet26.color = ColorRGBA27
Coordinate28 = x3d.Coordinate()

LineSet26.coord = Coordinate28

Shape25.geometry = LineSet26

Transform24.children.append(Shape25)

Transform18.children.append(Transform24)
#<Transform translation='0 2.1 0' scale='1 1 1'> <Shape DEF='HAnimSiteShape'> <IndexedFaceSet DEF='DiamondIFS' creaseAngle='0.5' solid='false' coordIndex='0 1 2 -1 0 2 3 -1 0 3 4 -1 0 4 1 -1 5 2 1 -1 5 3 2 -1 5 4 3 -1 5 1 4 -1'> <ColorRGBA DEF='HAnimSiteColorRGBA' color='1 1 0 1 1 1 0 0.1'/> <Coordinate point='0 0.01 0 -0.01 0 0 0 0 0.01 0.01 0 0 0 0 -0.01 0 -0.01 0'/> </IndexedFaceSet> <Appearance> <Material diffuseColor='1 1 0' transparency='0.3'/> </Appearance> </Shape> </Transform>

Group17.children.append(Transform18)

Scene11.children.append(Group17)
NavigationInfo29 = x3d.NavigationInfo()
NavigationInfo29.speed = 1.5

Scene11.children.append(NavigationInfo29)
Viewpoint30 = x3d.Viewpoint()
Viewpoint30.description = "default"

Scene11.children.append(Viewpoint30)
HAnimHumanoid31 = x3d.HAnimHumanoid()
HAnimHumanoid31.name = "HAnim"
HAnimHumanoid31.DEF = "hanim_HAnim"
HAnimHumanoid31.info = ["humanoidVersion=2.0"]
HAnimHumanoid31.version = "2.0"
HAnimJoint32 = x3d.HAnimJoint()
HAnimJoint32.name = "humanoid_root"
HAnimJoint32.DEF = "hanim_humanoid_root"
HAnimJoint32.center = [0,0.824,0.0277]
HAnimJoint32.ulimit = [0,0,0]
HAnimJoint32.llimit = [0,0,0]
Shape33 = x3d.Shape()
LineSet34 = x3d.LineSet()
LineSet34.vertexCount = [2]
Coordinate35 = x3d.Coordinate()

LineSet34.coord = Coordinate35
#from humanoid_root to sacroiliac
ColorRGBA36 = x3d.ColorRGBA()
ColorRGBA36.USE = "HAnimSegmentLineColorRGBA"

LineSet34.color = ColorRGBA36

Shape33.geometry = LineSet34

HAnimJoint32.pe.append(Shape33)
HAnimSite37 = x3d.HAnimSite()
HAnimSite37.name = "buttocks_standing_wall_contact_point_pt"
HAnimSite37.DEF = "hanim_buttocks_standing_wall_contact_point_pt"
HAnimSite37.translation = [0,1,0]
TouchSensor38 = x3d.TouchSensor()
TouchSensor38.description = "HAnimSite buttocks_standing_wall_contact_point_pt"

HAnimSite37.children.append(TouchSensor38)
Shape39 = x3d.Shape()
Shape39.USE = "HAnimSiteShape"

HAnimSite37.children.append(Shape39)

HAnimJoint32.HAnimSite.append(HAnimSite37)
HAnimSite40 = x3d.HAnimSite()
HAnimSite40.name = "crotch_pt"
HAnimSite40.DEF = "hanim_crotch_pt"
HAnimSite40.translation = [0.0034,0.8266,0.0257]
TouchSensor41 = x3d.TouchSensor()
TouchSensor41.description = "HAnimSite crotch_pt"

HAnimSite40.children.append(TouchSensor41)
Shape42 = x3d.Shape()
Shape42.USE = "HAnimSiteShape"

HAnimSite40.children.append(Shape42)

HAnimJoint32.HAnimSite.append(HAnimSite40)
HAnimSite43 = x3d.HAnimSite()
HAnimSite43.name = "l_asis_pt"
HAnimSite43.DEF = "hanim_l_asis_pt"
HAnimSite43.translation = [0.0925,0.9983,0.1052]
TouchSensor44 = x3d.TouchSensor()
TouchSensor44.description = "HAnimSite l_asis_pt"

HAnimSite43.children.append(TouchSensor44)
Shape45 = x3d.Shape()
Shape45.USE = "HAnimSiteShape"

HAnimSite43.children.append(Shape45)

HAnimJoint32.HAnimSite.append(HAnimSite43)
HAnimSite46 = x3d.HAnimSite()
HAnimSite46.name = "l_iliocristale_pt"
HAnimSite46.DEF = "hanim_l_iliocristale_pt"
HAnimSite46.translation = [0.1612,1.0537,0.0008]
TouchSensor47 = x3d.TouchSensor()
TouchSensor47.description = "HAnimSite l_iliocristale_pt"

HAnimSite46.children.append(TouchSensor47)
Shape48 = x3d.Shape()
Shape48.USE = "HAnimSiteShape"

HAnimSite46.children.append(Shape48)

HAnimJoint32.HAnimSite.append(HAnimSite46)
HAnimSite49 = x3d.HAnimSite()
HAnimSite49.name = "l_psis_pt"
HAnimSite49.DEF = "hanim_l_psis_pt"
HAnimSite49.translation = [0.0774,1.019,-0.1151]
TouchSensor50 = x3d.TouchSensor()
TouchSensor50.description = "HAnimSite l_psis_pt"

HAnimSite49.children.append(TouchSensor50)
Shape51 = x3d.Shape()
Shape51.USE = "HAnimSiteShape"

HAnimSite49.children.append(Shape51)

HAnimJoint32.HAnimSite.append(HAnimSite49)
HAnimSite52 = x3d.HAnimSite()
HAnimSite52.name = "l_trochanterion_pt"
HAnimSite52.DEF = "hanim_l_trochanterion_pt"
HAnimSite52.translation = [0.1677,0.8336,0.0303]
TouchSensor53 = x3d.TouchSensor()
TouchSensor53.description = "HAnimSite l_trochanterion_pt"

HAnimSite52.children.append(TouchSensor53)
Shape54 = x3d.Shape()
Shape54.USE = "HAnimSiteShape"

HAnimSite52.children.append(Shape54)

HAnimJoint32.HAnimSite.append(HAnimSite52)
HAnimSite55 = x3d.HAnimSite()
HAnimSite55.name = "r_asis_pt"
HAnimSite55.DEF = "hanim_r_asis_pt"
HAnimSite55.translation = [-0.0887,1.0021,0.1112]
TouchSensor56 = x3d.TouchSensor()
TouchSensor56.description = "HAnimSite r_asis_pt"

HAnimSite55.children.append(TouchSensor56)
Shape57 = x3d.Shape()
Shape57.USE = "HAnimSiteShape"

HAnimSite55.children.append(Shape57)

HAnimJoint32.HAnimSite.append(HAnimSite55)
HAnimSite58 = x3d.HAnimSite()
HAnimSite58.name = "r_iliocristale_pt"
HAnimSite58.DEF = "hanim_r_iliocristale_pt"
HAnimSite58.translation = [-0.1525,1.0628,0.0035]
TouchSensor59 = x3d.TouchSensor()
TouchSensor59.description = "HAnimSite r_iliocristale_pt"

HAnimSite58.children.append(TouchSensor59)
Shape60 = x3d.Shape()
Shape60.USE = "HAnimSiteShape"

HAnimSite58.children.append(Shape60)

HAnimJoint32.HAnimSite.append(HAnimSite58)
HAnimSite61 = x3d.HAnimSite()
HAnimSite61.name = "r_psis_pt"
HAnimSite61.DEF = "hanim_r_psis_pt"
HAnimSite61.translation = [-0.0716,1.019,-0.1138]
TouchSensor62 = x3d.TouchSensor()
TouchSensor62.description = "HAnimSite r_psis_pt"

HAnimSite61.children.append(TouchSensor62)
Shape63 = x3d.Shape()
Shape63.USE = "HAnimSiteShape"

HAnimSite61.children.append(Shape63)

HAnimJoint32.HAnimSite.append(HAnimSite61)
HAnimSite64 = x3d.HAnimSite()
HAnimSite64.name = "r_trochanterion_pt"
HAnimSite64.DEF = "hanim_r_trochanterion_pt"
HAnimSite64.translation = [-0.1689,0.8419,0.0352]
TouchSensor65 = x3d.TouchSensor()
TouchSensor65.description = "HAnimSite r_trochanterion_pt"

HAnimSite64.children.append(TouchSensor65)
Shape66 = x3d.Shape()
Shape66.USE = "HAnimSiteShape"

HAnimSite64.children.append(Shape66)

HAnimJoint32.HAnimSite.append(HAnimSite64)
Shape67 = x3d.Shape()
LineSet68 = x3d.LineSet()
LineSet68.vertexCount = [2]
Coordinate69 = x3d.Coordinate()

LineSet68.coord = Coordinate69
#from humanoid_root to vl5
ColorRGBA70 = x3d.ColorRGBA()
ColorRGBA70.USE = "HAnimSegmentLineColorRGBA"

LineSet68.color = ColorRGBA70

Shape67.geometry = LineSet68

HAnimJoint32.pe.append(Shape67)
HAnimSite71 = x3d.HAnimSite()
HAnimSite71.name = "navel_pt"
HAnimSite71.DEF = "hanim_navel_pt"
HAnimSite71.translation = [0.0069,1.0966,0.1017]
TouchSensor72 = x3d.TouchSensor()
TouchSensor72.description = "HAnimSite navel_pt"

HAnimSite71.children.append(TouchSensor72)
Shape73 = x3d.Shape()
Shape73.USE = "HAnimSiteShape"

HAnimSite71.children.append(Shape73)

HAnimJoint32.HAnimSite.append(HAnimSite71)
HAnimSite74 = x3d.HAnimSite()
HAnimSite74.name = "waist_preferred_anterior_pt"
HAnimSite74.DEF = "hanim_waist_preferred_anterior_pt"
HAnimSite74.translation = [0,1,0]
TouchSensor75 = x3d.TouchSensor()
TouchSensor75.description = "HAnimSite waist_preferred_anterior_pt"

HAnimSite74.children.append(TouchSensor75)
Shape76 = x3d.Shape()
Shape76.USE = "HAnimSiteShape"

HAnimSite74.children.append(Shape76)

HAnimJoint32.HAnimSite.append(HAnimSite74)
HAnimSite77 = x3d.HAnimSite()
HAnimSite77.name = "waist_preferred_posterior_pt"
HAnimSite77.DEF = "hanim_waist_preferred_posterior_pt"
HAnimSite77.translation = [0.29,1.0915,-0.1091]
TouchSensor78 = x3d.TouchSensor()
TouchSensor78.description = "HAnimSite waist_preferred_posterior_pt"

HAnimSite77.children.append(TouchSensor78)
Shape79 = x3d.Shape()
Shape79.USE = "HAnimSiteShape"

HAnimSite77.children.append(Shape79)

HAnimJoint32.HAnimSite.append(HAnimSite77)
HAnimJoint80 = x3d.HAnimJoint()
HAnimJoint80.name = "sacroiliac"
HAnimJoint80.DEF = "hanim_sacroiliac"
HAnimJoint80.center = [0,0.9149,0.0016]
HAnimJoint80.ulimit = [0,0,0]
HAnimJoint80.llimit = [0,0,0]
Shape81 = x3d.Shape()
LineSet82 = x3d.LineSet()
LineSet82.vertexCount = [2]
Coordinate83 = x3d.Coordinate()

LineSet82.coord = Coordinate83
#from sacroiliac to l_hip
ColorRGBA84 = x3d.ColorRGBA()
ColorRGBA84.USE = "HAnimSegmentLineColorRGBA"

LineSet82.color = ColorRGBA84

Shape81.geometry = LineSet82

HAnimJoint80.pe.append(Shape81)
HAnimSite85 = x3d.HAnimSite()
HAnimSite85.name = "l_femoral_lateral_epicondyles_pt"
HAnimSite85.DEF = "hanim_l_femoral_lateral_epicondyles_pt"
HAnimSite85.translation = [0.1598,0.4967,0.0297]
TouchSensor86 = x3d.TouchSensor()
TouchSensor86.description = "HAnimSite l_femoral_lateral_epicondyles_pt"

HAnimSite85.children.append(TouchSensor86)
Shape87 = x3d.Shape()
Shape87.USE = "HAnimSiteShape"

HAnimSite85.children.append(Shape87)

HAnimJoint80.HAnimSite.append(HAnimSite85)
HAnimSite88 = x3d.HAnimSite()
HAnimSite88.name = "l_femoral_medial_epicondyles_pt"
HAnimSite88.DEF = "hanim_l_femoral_medial_epicondyles_pt"
HAnimSite88.translation = [0.0398,0.4946,0.0303]
TouchSensor89 = x3d.TouchSensor()
TouchSensor89.description = "HAnimSite l_femoral_medial_epicondyles_pt"

HAnimSite88.children.append(TouchSensor89)
Shape90 = x3d.Shape()
Shape90.USE = "HAnimSiteShape"

HAnimSite88.children.append(Shape90)

HAnimJoint80.HAnimSite.append(HAnimSite88)
HAnimSite91 = x3d.HAnimSite()
HAnimSite91.name = "l_knee_crease_pt"
HAnimSite91.DEF = "hanim_l_knee_crease_pt"
HAnimSite91.translation = [0.0993,0.4881,-0.0309]
TouchSensor92 = x3d.TouchSensor()
TouchSensor92.description = "HAnimSite l_knee_crease_pt"

HAnimSite91.children.append(TouchSensor92)
Shape93 = x3d.Shape()
Shape93.USE = "HAnimSiteShape"

HAnimSite91.children.append(Shape93)

HAnimJoint80.HAnimSite.append(HAnimSite91)
HAnimSite94 = x3d.HAnimSite()
HAnimSite94.name = "l_suprapatella_pt"
HAnimSite94.DEF = "hanim_l_suprapatella_pt"
HAnimSite94.translation = [0,1,0]
TouchSensor95 = x3d.TouchSensor()
TouchSensor95.description = "HAnimSite l_suprapatella_pt"

HAnimSite94.children.append(TouchSensor95)
Shape96 = x3d.Shape()
Shape96.USE = "HAnimSiteShape"

HAnimSite94.children.append(Shape96)

HAnimJoint80.HAnimSite.append(HAnimSite94)
Shape97 = x3d.Shape()
LineSet98 = x3d.LineSet()
LineSet98.vertexCount = [2]
Coordinate99 = x3d.Coordinate()

LineSet98.coord = Coordinate99
#from sacroiliac to r_hip
ColorRGBA100 = x3d.ColorRGBA()
ColorRGBA100.USE = "HAnimSegmentLineColorRGBA"

LineSet98.color = ColorRGBA100

Shape97.geometry = LineSet98

HAnimJoint80.pe.append(Shape97)
HAnimSite101 = x3d.HAnimSite()
HAnimSite101.name = "r_femoral_lateral_epicondyles_pt"
HAnimSite101.DEF = "hanim_r_femoral_lateral_epicondyles_pt"
HAnimSite101.translation = [-0.1421,0.4992,0.031]
TouchSensor102 = x3d.TouchSensor()
TouchSensor102.description = "HAnimSite r_femoral_lateral_epicondyles_pt"

HAnimSite101.children.append(TouchSensor102)
Shape103 = x3d.Shape()
Shape103.USE = "HAnimSiteShape"

HAnimSite101.children.append(Shape103)

HAnimJoint80.HAnimSite.append(HAnimSite101)
HAnimSite104 = x3d.HAnimSite()
HAnimSite104.name = "r_femoral_medial_epicondyles_pt"
HAnimSite104.DEF = "hanim_r_femoral_medial_epicondyles_pt"
HAnimSite104.translation = [-0.0221,0.5014,0.0289]
TouchSensor105 = x3d.TouchSensor()
TouchSensor105.description = "HAnimSite r_femoral_medial_epicondyles_pt"

HAnimSite104.children.append(TouchSensor105)
Shape106 = x3d.Shape()
Shape106.USE = "HAnimSiteShape"

HAnimSite104.children.append(Shape106)

HAnimJoint80.HAnimSite.append(HAnimSite104)
HAnimSite107 = x3d.HAnimSite()
HAnimSite107.name = "r_knee_crease_pt"
HAnimSite107.DEF = "hanim_r_knee_crease_pt"
HAnimSite107.translation = [-0.0825,0.4932,-0.0326]
TouchSensor108 = x3d.TouchSensor()
TouchSensor108.description = "HAnimSite r_knee_crease_pt"

HAnimSite107.children.append(TouchSensor108)
Shape109 = x3d.Shape()
Shape109.USE = "HAnimSiteShape"

HAnimSite107.children.append(Shape109)

HAnimJoint80.HAnimSite.append(HAnimSite107)
HAnimSite110 = x3d.HAnimSite()
HAnimSite110.name = "r_suprapatella_pt"
HAnimSite110.DEF = "hanim_r_suprapatella_pt"
HAnimSite110.translation = [0,1,0]
TouchSensor111 = x3d.TouchSensor()
TouchSensor111.description = "HAnimSite r_suprapatella_pt"

HAnimSite110.children.append(TouchSensor111)
Shape112 = x3d.Shape()
Shape112.USE = "HAnimSiteShape"

HAnimSite110.children.append(Shape112)

HAnimJoint80.HAnimSite.append(HAnimSite110)
HAnimJoint113 = x3d.HAnimJoint()
HAnimJoint113.name = "l_hip"
HAnimJoint113.DEF = "hanim_l_hip"
HAnimJoint113.center = [0.0961,0.9124,-0.0001]
HAnimJoint113.ulimit = [0,0,0]
HAnimJoint113.llimit = [0,0,0]
Shape114 = x3d.Shape()
LineSet115 = x3d.LineSet()
LineSet115.vertexCount = [2]
Coordinate116 = x3d.Coordinate()

LineSet115.coord = Coordinate116
#from l_hip to l_knee
ColorRGBA117 = x3d.ColorRGBA()
ColorRGBA117.USE = "HAnimSegmentLineColorRGBA"

LineSet115.color = ColorRGBA117

Shape114.geometry = LineSet115

HAnimJoint113.pe.append(Shape114)
HAnimSite118 = x3d.HAnimSite()
HAnimSite118.name = "l_lateral_malleolus_pt"
HAnimSite118.DEF = "hanim_l_lateral_malleolus_pt"
HAnimSite118.translation = [0.1308,0.0597,-0.1032]
TouchSensor119 = x3d.TouchSensor()
TouchSensor119.description = "HAnimSite l_lateral_malleolus_pt"

HAnimSite118.children.append(TouchSensor119)
Shape120 = x3d.Shape()
Shape120.USE = "HAnimSiteShape"

HAnimSite118.children.append(Shape120)

HAnimJoint113.HAnimSite.append(HAnimSite118)
HAnimSite121 = x3d.HAnimSite()
HAnimSite121.name = "l_medial_malleolus_pt"
HAnimSite121.DEF = "hanim_l_medial_malleolus_pt"
HAnimSite121.translation = [0.089,0.0716,-0.0881]
TouchSensor122 = x3d.TouchSensor()
TouchSensor122.description = "HAnimSite l_medial_malleolus_pt"

HAnimSite121.children.append(TouchSensor122)
Shape123 = x3d.Shape()
Shape123.USE = "HAnimSiteShape"

HAnimSite121.children.append(Shape123)

HAnimJoint113.HAnimSite.append(HAnimSite121)
HAnimSite124 = x3d.HAnimSite()
HAnimSite124.name = "l_tibiale_pt"
HAnimSite124.DEF = "hanim_l_tibiale_pt"
HAnimSite124.translation = [0,1,0]
TouchSensor125 = x3d.TouchSensor()
TouchSensor125.description = "HAnimSite l_tibiale_pt"

HAnimSite124.children.append(TouchSensor125)
Shape126 = x3d.Shape()
Shape126.USE = "HAnimSiteShape"

HAnimSite124.children.append(Shape126)

HAnimJoint113.HAnimSite.append(HAnimSite124)
HAnimJoint127 = x3d.HAnimJoint()
HAnimJoint127.name = "l_knee"
HAnimJoint127.DEF = "hanim_l_knee"
HAnimJoint127.center = [0.104,0.4867,0.0308]
HAnimJoint127.ulimit = [0,0,0]
HAnimJoint127.llimit = [0,0,0]
Shape128 = x3d.Shape()
LineSet129 = x3d.LineSet()
LineSet129.vertexCount = [2]
Coordinate130 = x3d.Coordinate()

LineSet129.coord = Coordinate130
#from l_knee to l_talocrural
ColorRGBA131 = x3d.ColorRGBA()
ColorRGBA131.USE = "HAnimSegmentLineColorRGBA"

LineSet129.color = ColorRGBA131

Shape128.geometry = LineSet129

HAnimJoint127.pe.append(Shape128)
HAnimSite132 = x3d.HAnimSite()
HAnimSite132.name = "l_calcaneus_posterior_pt"
HAnimSite132.DEF = "hanim_l_calcaneus_posterior_pt"
HAnimSite132.translation = [0.0974,0.0259,-0.1171]
TouchSensor133 = x3d.TouchSensor()
TouchSensor133.description = "HAnimSite l_calcaneus_posterior_pt"

HAnimSite132.children.append(TouchSensor133)
Shape134 = x3d.Shape()
Shape134.USE = "HAnimSiteShape"

HAnimSite132.children.append(Shape134)

HAnimJoint127.HAnimSite.append(HAnimSite132)
HAnimSite135 = x3d.HAnimSite()
HAnimSite135.name = "l_sphyrion_pt"
HAnimSite135.DEF = "hanim_l_sphyrion_pt"
HAnimSite135.translation = [0.089,0.0575,-0.0943]
TouchSensor136 = x3d.TouchSensor()
TouchSensor136.description = "HAnimSite l_sphyrion_pt"

HAnimSite135.children.append(TouchSensor136)
Shape137 = x3d.Shape()
Shape137.USE = "HAnimSiteShape"

HAnimSite135.children.append(Shape137)

HAnimJoint127.HAnimSite.append(HAnimSite135)
HAnimJoint138 = x3d.HAnimJoint()
HAnimJoint138.name = "l_talocrural"
HAnimJoint138.DEF = "hanim_l_talocrural"
HAnimJoint138.center = [0.1101,0.0656,-0.0736]
HAnimJoint138.ulimit = [0,0,0]
HAnimJoint138.llimit = [0,0,0]
Shape139 = x3d.Shape()
LineSet140 = x3d.LineSet()
LineSet140.vertexCount = [2]
Coordinate141 = x3d.Coordinate()

LineSet140.coord = Coordinate141
#from l_talocrural to l_talocalcaneonavicular
ColorRGBA142 = x3d.ColorRGBA()
ColorRGBA142.USE = "HAnimSegmentLineColorRGBA"

LineSet140.color = ColorRGBA142

Shape139.geometry = LineSet140

HAnimJoint138.pe.append(Shape139)
Shape143 = x3d.Shape()
LineSet144 = x3d.LineSet()
LineSet144.vertexCount = [2]
Coordinate145 = x3d.Coordinate()

LineSet144.coord = Coordinate145
#from l_talocrural to l_calcaneocuboid
ColorRGBA146 = x3d.ColorRGBA()
ColorRGBA146.USE = "HAnimSegmentLineColorRGBA"

LineSet144.color = ColorRGBA146

Shape143.geometry = LineSet144

HAnimJoint138.pe.append(Shape143)
HAnimJoint147 = x3d.HAnimJoint()
HAnimJoint147.name = "l_talocalcaneonavicular"
HAnimJoint147.DEF = "hanim_l_talocalcaneonavicular"
HAnimJoint147.center = [0,1,0]
HAnimJoint147.ulimit = [0,0,0]
HAnimJoint147.llimit = [0,0,0]
Shape148 = x3d.Shape()
LineSet149 = x3d.LineSet()
LineSet149.vertexCount = [1]
Coordinate150 = x3d.Coordinate()

LineSet149.coord = Coordinate150
#from l_talocalcaneonavicular to l_cuneonavicular_1
ColorRGBA151 = x3d.ColorRGBA()
ColorRGBA151.USE = "HAnimSegmentLineColorRGBA"

LineSet149.color = ColorRGBA151

Shape148.geometry = LineSet149

HAnimJoint147.pe.append(Shape148)
Shape152 = x3d.Shape()
LineSet153 = x3d.LineSet()
LineSet153.vertexCount = [1]
Coordinate154 = x3d.Coordinate()

LineSet153.coord = Coordinate154
#from l_talocalcaneonavicular to l_cuneonavicular_2
ColorRGBA155 = x3d.ColorRGBA()
ColorRGBA155.USE = "HAnimSegmentLineColorRGBA"

LineSet153.color = ColorRGBA155

Shape152.geometry = LineSet153

HAnimJoint147.pe.append(Shape152)
Shape156 = x3d.Shape()
LineSet157 = x3d.LineSet()
LineSet157.vertexCount = [1]
Coordinate158 = x3d.Coordinate()

LineSet157.coord = Coordinate158
#from l_talocalcaneonavicular to l_cuneonavicular_3
ColorRGBA159 = x3d.ColorRGBA()
ColorRGBA159.USE = "HAnimSegmentLineColorRGBA"

LineSet157.color = ColorRGBA159

Shape156.geometry = LineSet157

HAnimJoint147.pe.append(Shape156)
HAnimJoint160 = x3d.HAnimJoint()
HAnimJoint160.name = "l_cuneonavicular_1"
HAnimJoint160.DEF = "hanim_l_cuneonavicular_1"
HAnimJoint160.center = [0,1,0]
HAnimJoint160.ulimit = [0,0,0]
HAnimJoint160.llimit = [0,0,0]
Shape161 = x3d.Shape()
LineSet162 = x3d.LineSet()
LineSet162.vertexCount = [1]
Coordinate163 = x3d.Coordinate()

LineSet162.coord = Coordinate163
#from l_cuneonavicular_1 to l_tarsometatarsal_1
ColorRGBA164 = x3d.ColorRGBA()
ColorRGBA164.USE = "HAnimSegmentLineColorRGBA"

LineSet162.color = ColorRGBA164

Shape161.geometry = LineSet162

HAnimJoint160.pe.append(Shape161)
HAnimJoint165 = x3d.HAnimJoint()
HAnimJoint165.name = "l_tarsometatarsal_1"
HAnimJoint165.DEF = "hanim_l_tarsometatarsal_1"
HAnimJoint165.center = [0,1,0]
HAnimJoint165.ulimit = [0,0,0]
HAnimJoint165.llimit = [0,0,0]
Shape166 = x3d.Shape()
LineSet167 = x3d.LineSet()
LineSet167.vertexCount = [1]
Coordinate168 = x3d.Coordinate()

LineSet167.coord = Coordinate168
#from l_tarsometatarsal_1 to l_metatarsophalangeal_1
ColorRGBA169 = x3d.ColorRGBA()
ColorRGBA169.USE = "HAnimSegmentLineColorRGBA"

LineSet167.color = ColorRGBA169

Shape166.geometry = LineSet167

HAnimJoint165.pe.append(Shape166)
HAnimSite170 = x3d.HAnimSite()
HAnimSite170.name = "l_metatarsal_phalanx_1_pt"
HAnimSite170.DEF = "hanim_l_metatarsal_phalanx_1_pt"
HAnimSite170.translation = [0,1,0]
TouchSensor171 = x3d.TouchSensor()
TouchSensor171.description = "HAnimSite l_metatarsal_phalanx_1_pt"

HAnimSite170.children.append(TouchSensor171)
Shape172 = x3d.Shape()
Shape172.USE = "HAnimSiteShape"

HAnimSite170.children.append(Shape172)

HAnimJoint165.HAnimSite.append(HAnimSite170)
HAnimJoint173 = x3d.HAnimJoint()
HAnimJoint173.name = "l_metatarsophalangeal_1"
HAnimJoint173.DEF = "hanim_l_metatarsophalangeal_1"
HAnimJoint173.center = [0,1,0]
HAnimJoint173.ulimit = [0,0,0]
HAnimJoint173.llimit = [0,0,0]
Shape174 = x3d.Shape()
LineSet175 = x3d.LineSet()
LineSet175.vertexCount = [1]
Coordinate176 = x3d.Coordinate()

LineSet175.coord = Coordinate176
#from l_metatarsophalangeal_1 to l_tarsal_interphalangeal_1
ColorRGBA177 = x3d.ColorRGBA()
ColorRGBA177.USE = "HAnimSegmentLineColorRGBA"

LineSet175.color = ColorRGBA177

Shape174.geometry = LineSet175

HAnimJoint173.pe.append(Shape174)
HAnimSite178 = x3d.HAnimSite()
HAnimSite178.name = "l_tarsal_distal_phalanx_1_tip"
HAnimSite178.DEF = "hanim_l_tarsal_distal_phalanx_1_tip"
HAnimSite178.translation = [0,1,0]
TouchSensor179 = x3d.TouchSensor()
TouchSensor179.description = "HAnimSite l_tarsal_distal_phalanx_1_tip"

HAnimSite178.children.append(TouchSensor179)
Shape180 = x3d.Shape()
Shape180.USE = "HAnimSiteShape"

HAnimSite178.children.append(Shape180)

HAnimJoint173.HAnimSite.append(HAnimSite178)
HAnimJoint181 = x3d.HAnimJoint()
HAnimJoint181.name = "l_tarsal_interphalangeal_1"
HAnimJoint181.DEF = "hanim_l_tarsal_interphalangeal_1"
HAnimJoint181.center = [0,1,0]
HAnimJoint181.ulimit = [0,0,0]
HAnimJoint181.llimit = [0,0,0]

HAnimJoint173.children.append(HAnimJoint181)

HAnimJoint165.children.append(HAnimJoint173)

HAnimJoint160.children.append(HAnimJoint165)

HAnimJoint147.children.append(HAnimJoint160)
HAnimJoint182 = x3d.HAnimJoint()
HAnimJoint182.name = "l_cuneonavicular_2"
HAnimJoint182.DEF = "hanim_l_cuneonavicular_2"
HAnimJoint182.center = [0,1,0]
HAnimJoint182.ulimit = [0,0,0]
HAnimJoint182.llimit = [0,0,0]
Shape183 = x3d.Shape()
LineSet184 = x3d.LineSet()
LineSet184.vertexCount = [1]
Coordinate185 = x3d.Coordinate()

LineSet184.coord = Coordinate185
#from l_cuneonavicular_2 to l_tarsometatarsal_2
ColorRGBA186 = x3d.ColorRGBA()
ColorRGBA186.USE = "HAnimSegmentLineColorRGBA"

LineSet184.color = ColorRGBA186

Shape183.geometry = LineSet184

HAnimJoint182.pe.append(Shape183)
HAnimJoint187 = x3d.HAnimJoint()
HAnimJoint187.name = "l_tarsometatarsal_2"
HAnimJoint187.DEF = "hanim_l_tarsometatarsal_2"
HAnimJoint187.center = [0,1,0]
HAnimJoint187.ulimit = [0,0,0]
HAnimJoint187.llimit = [0,0,0]
Shape188 = x3d.Shape()
LineSet189 = x3d.LineSet()
LineSet189.vertexCount = [1]
Coordinate190 = x3d.Coordinate()

LineSet189.coord = Coordinate190
#from l_tarsometatarsal_2 to l_metatarsophalangeal_2
ColorRGBA191 = x3d.ColorRGBA()
ColorRGBA191.USE = "HAnimSegmentLineColorRGBA"

LineSet189.color = ColorRGBA191

Shape188.geometry = LineSet189

HAnimJoint187.pe.append(Shape188)
HAnimJoint192 = x3d.HAnimJoint()
HAnimJoint192.name = "l_metatarsophalangeal_2"
HAnimJoint192.DEF = "hanim_l_metatarsophalangeal_2"
HAnimJoint192.center = [0,1,0]
HAnimJoint192.ulimit = [0,0,0]
HAnimJoint192.llimit = [0,0,0]
Shape193 = x3d.Shape()
LineSet194 = x3d.LineSet()
LineSet194.vertexCount = [1]
Coordinate195 = x3d.Coordinate()

LineSet194.coord = Coordinate195
#from l_metatarsophalangeal_2 to l_tarsal_proximal_interphalangeal_2
ColorRGBA196 = x3d.ColorRGBA()
ColorRGBA196.USE = "HAnimSegmentLineColorRGBA"

LineSet194.color = ColorRGBA196

Shape193.geometry = LineSet194

HAnimJoint192.pe.append(Shape193)
HAnimJoint197 = x3d.HAnimJoint()
HAnimJoint197.name = "l_tarsal_proximal_interphalangeal_2"
HAnimJoint197.DEF = "hanim_l_tarsal_proximal_interphalangeal_2"
HAnimJoint197.center = [0,1,0]
HAnimJoint197.ulimit = [0,0,0]
HAnimJoint197.llimit = [0,0,0]
Shape198 = x3d.Shape()
LineSet199 = x3d.LineSet()
LineSet199.vertexCount = [1]
Coordinate200 = x3d.Coordinate()

LineSet199.coord = Coordinate200
#from l_tarsal_proximal_interphalangeal_2 to l_tarsal_distal_interphalangeal_2
ColorRGBA201 = x3d.ColorRGBA()
ColorRGBA201.USE = "HAnimSegmentLineColorRGBA"

LineSet199.color = ColorRGBA201

Shape198.geometry = LineSet199

HAnimJoint197.pe.append(Shape198)
HAnimSite202 = x3d.HAnimSite()
HAnimSite202.name = "l_tarsal_distal_phalanx_2_tip"
HAnimSite202.DEF = "hanim_l_tarsal_distal_phalanx_2_tip"
HAnimSite202.translation = [0.1195,0.0079,0.1433]
TouchSensor203 = x3d.TouchSensor()
TouchSensor203.description = "HAnimSite l_tarsal_distal_phalanx_2_tip"

HAnimSite202.children.append(TouchSensor203)
Shape204 = x3d.Shape()
Shape204.USE = "HAnimSiteShape"

HAnimSite202.children.append(Shape204)

HAnimJoint197.HAnimSite.append(HAnimSite202)
HAnimJoint205 = x3d.HAnimJoint()
HAnimJoint205.name = "l_tarsal_distal_interphalangeal_2"
HAnimJoint205.DEF = "hanim_l_tarsal_distal_interphalangeal_2"
HAnimJoint205.center = [0,1,0]
HAnimJoint205.ulimit = [0,0,0]
HAnimJoint205.llimit = [0,0,0]

HAnimJoint197.children.append(HAnimJoint205)

HAnimJoint192.children.append(HAnimJoint197)

HAnimJoint187.children.append(HAnimJoint192)

HAnimJoint182.children.append(HAnimJoint187)

HAnimJoint147.children.append(HAnimJoint182)
HAnimJoint206 = x3d.HAnimJoint()
HAnimJoint206.name = "l_cuneonavicular_3"
HAnimJoint206.DEF = "hanim_l_cuneonavicular_3"
HAnimJoint206.center = [0,1,0]
HAnimJoint206.ulimit = [0,0,0]
HAnimJoint206.llimit = [0,0,0]
Shape207 = x3d.Shape()
LineSet208 = x3d.LineSet()
LineSet208.vertexCount = [1]
Coordinate209 = x3d.Coordinate()

LineSet208.coord = Coordinate209
#from l_cuneonavicular_3 to l_tarsometatarsal_3
ColorRGBA210 = x3d.ColorRGBA()
ColorRGBA210.USE = "HAnimSegmentLineColorRGBA"

LineSet208.color = ColorRGBA210

Shape207.geometry = LineSet208

HAnimJoint206.pe.append(Shape207)
HAnimJoint211 = x3d.HAnimJoint()
HAnimJoint211.name = "l_tarsometatarsal_3"
HAnimJoint211.DEF = "hanim_l_tarsometatarsal_3"
HAnimJoint211.center = [0,1,0]
HAnimJoint211.ulimit = [0,0,0]
HAnimJoint211.llimit = [0,0,0]
Shape212 = x3d.Shape()
LineSet213 = x3d.LineSet()
LineSet213.vertexCount = [1]
Coordinate214 = x3d.Coordinate()

LineSet213.coord = Coordinate214
#from l_tarsometatarsal_3 to l_metatarsophalangeal_3
ColorRGBA215 = x3d.ColorRGBA()
ColorRGBA215.USE = "HAnimSegmentLineColorRGBA"

LineSet213.color = ColorRGBA215

Shape212.geometry = LineSet213

HAnimJoint211.pe.append(Shape212)
HAnimJoint216 = x3d.HAnimJoint()
HAnimJoint216.name = "l_metatarsophalangeal_3"
HAnimJoint216.DEF = "hanim_l_metatarsophalangeal_3"
HAnimJoint216.center = [0,1,0]
HAnimJoint216.ulimit = [0,0,0]
HAnimJoint216.llimit = [0,0,0]
Shape217 = x3d.Shape()
LineSet218 = x3d.LineSet()
LineSet218.vertexCount = [1]
Coordinate219 = x3d.Coordinate()

LineSet218.coord = Coordinate219
#from l_metatarsophalangeal_3 to l_tarsal_proximal_interphalangeal_3
ColorRGBA220 = x3d.ColorRGBA()
ColorRGBA220.USE = "HAnimSegmentLineColorRGBA"

LineSet218.color = ColorRGBA220

Shape217.geometry = LineSet218

HAnimJoint216.pe.append(Shape217)
HAnimJoint221 = x3d.HAnimJoint()
HAnimJoint221.name = "l_tarsal_proximal_interphalangeal_3"
HAnimJoint221.DEF = "hanim_l_tarsal_proximal_interphalangeal_3"
HAnimJoint221.center = [0,1,0]
HAnimJoint221.ulimit = [0,0,0]
HAnimJoint221.llimit = [0,0,0]
Shape222 = x3d.Shape()
LineSet223 = x3d.LineSet()
LineSet223.vertexCount = [1]
Coordinate224 = x3d.Coordinate()

LineSet223.coord = Coordinate224
#from l_tarsal_proximal_interphalangeal_3 to l_tarsal_distal_interphalangeal_3
ColorRGBA225 = x3d.ColorRGBA()
ColorRGBA225.USE = "HAnimSegmentLineColorRGBA"

LineSet223.color = ColorRGBA225

Shape222.geometry = LineSet223

HAnimJoint221.pe.append(Shape222)
HAnimSite226 = x3d.HAnimSite()
HAnimSite226.name = "l_tarsal_distal_phalanx_3_tip"
HAnimSite226.DEF = "hanim_l_tarsal_distal_phalanx_3_tip"
HAnimSite226.translation = [0,1,0]
TouchSensor227 = x3d.TouchSensor()
TouchSensor227.description = "HAnimSite l_tarsal_distal_phalanx_3_tip"

HAnimSite226.children.append(TouchSensor227)
Shape228 = x3d.Shape()
Shape228.USE = "HAnimSiteShape"

HAnimSite226.children.append(Shape228)

HAnimJoint221.HAnimSite.append(HAnimSite226)
HAnimJoint229 = x3d.HAnimJoint()
HAnimJoint229.name = "l_tarsal_distal_interphalangeal_3"
HAnimJoint229.DEF = "hanim_l_tarsal_distal_interphalangeal_3"
HAnimJoint229.center = [0,1,0]
HAnimJoint229.ulimit = [0,0,0]
HAnimJoint229.llimit = [0,0,0]

HAnimJoint221.children.append(HAnimJoint229)

HAnimJoint216.children.append(HAnimJoint221)

HAnimJoint211.children.append(HAnimJoint216)

HAnimJoint206.children.append(HAnimJoint211)

HAnimJoint147.children.append(HAnimJoint206)

HAnimJoint138.children.append(HAnimJoint147)
HAnimJoint230 = x3d.HAnimJoint()
HAnimJoint230.name = "l_calcaneocuboid"
HAnimJoint230.DEF = "hanim_l_calcaneocuboid"
HAnimJoint230.center = [0,1,0]
HAnimJoint230.ulimit = [0,0,0]
HAnimJoint230.llimit = [0,0,0]
Shape231 = x3d.Shape()
LineSet232 = x3d.LineSet()
LineSet232.vertexCount = [1]
Coordinate233 = x3d.Coordinate()

LineSet232.coord = Coordinate233
#from l_calcaneocuboid to l_transversetarsal
ColorRGBA234 = x3d.ColorRGBA()
ColorRGBA234.USE = "HAnimSegmentLineColorRGBA"

LineSet232.color = ColorRGBA234

Shape231.geometry = LineSet232

HAnimJoint230.pe.append(Shape231)
HAnimJoint235 = x3d.HAnimJoint()
HAnimJoint235.name = "l_transversetarsal"
HAnimJoint235.DEF = "hanim_l_transversetarsal"
HAnimJoint235.center = [0,1,0]
HAnimJoint235.ulimit = [0,0,0]
HAnimJoint235.llimit = [0,0,0]
Shape236 = x3d.Shape()
LineSet237 = x3d.LineSet()
LineSet237.vertexCount = [1]
Coordinate238 = x3d.Coordinate()

LineSet237.coord = Coordinate238
#from l_transversetarsal to l_tarsometatarsal_4
ColorRGBA239 = x3d.ColorRGBA()
ColorRGBA239.USE = "HAnimSegmentLineColorRGBA"

LineSet237.color = ColorRGBA239

Shape236.geometry = LineSet237

HAnimJoint235.pe.append(Shape236)
Shape240 = x3d.Shape()
LineSet241 = x3d.LineSet()
LineSet241.vertexCount = [1]
Coordinate242 = x3d.Coordinate()

LineSet241.coord = Coordinate242
#from l_transversetarsal to l_tarsometatarsal_5
ColorRGBA243 = x3d.ColorRGBA()
ColorRGBA243.USE = "HAnimSegmentLineColorRGBA"

LineSet241.color = ColorRGBA243

Shape240.geometry = LineSet241

HAnimJoint235.pe.append(Shape240)
HAnimJoint244 = x3d.HAnimJoint()
HAnimJoint244.name = "l_tarsometatarsal_4"
HAnimJoint244.DEF = "hanim_l_tarsometatarsal_4"
HAnimJoint244.center = [0,1,0]
HAnimJoint244.ulimit = [0,0,0]
HAnimJoint244.llimit = [0,0,0]
Shape245 = x3d.Shape()
LineSet246 = x3d.LineSet()
LineSet246.vertexCount = [1]
Coordinate247 = x3d.Coordinate()

LineSet246.coord = Coordinate247
#from l_tarsometatarsal_4 to l_metatarsophalangeal_4
ColorRGBA248 = x3d.ColorRGBA()
ColorRGBA248.USE = "HAnimSegmentLineColorRGBA"

LineSet246.color = ColorRGBA248

Shape245.geometry = LineSet246

HAnimJoint244.pe.append(Shape245)
HAnimJoint249 = x3d.HAnimJoint()
HAnimJoint249.name = "l_metatarsophalangeal_4"
HAnimJoint249.DEF = "hanim_l_metatarsophalangeal_4"
HAnimJoint249.center = [0,1,0]
HAnimJoint249.ulimit = [0,0,0]
HAnimJoint249.llimit = [0,0,0]
Shape250 = x3d.Shape()
LineSet251 = x3d.LineSet()
LineSet251.vertexCount = [1]
Coordinate252 = x3d.Coordinate()

LineSet251.coord = Coordinate252
#from l_metatarsophalangeal_4 to l_tarsal_proximal_interphalangeal_4
ColorRGBA253 = x3d.ColorRGBA()
ColorRGBA253.USE = "HAnimSegmentLineColorRGBA"

LineSet251.color = ColorRGBA253

Shape250.geometry = LineSet251

HAnimJoint249.pe.append(Shape250)
HAnimJoint254 = x3d.HAnimJoint()
HAnimJoint254.name = "l_tarsal_proximal_interphalangeal_4"
HAnimJoint254.DEF = "hanim_l_tarsal_proximal_interphalangeal_4"
HAnimJoint254.center = [0,1,0]
HAnimJoint254.ulimit = [0,0,0]
HAnimJoint254.llimit = [0,0,0]
Shape255 = x3d.Shape()
LineSet256 = x3d.LineSet()
LineSet256.vertexCount = [1]
Coordinate257 = x3d.Coordinate()

LineSet256.coord = Coordinate257
#from l_tarsal_proximal_interphalangeal_4 to l_tarsal_distal_interphalangeal_4
ColorRGBA258 = x3d.ColorRGBA()
ColorRGBA258.USE = "HAnimSegmentLineColorRGBA"

LineSet256.color = ColorRGBA258

Shape255.geometry = LineSet256

HAnimJoint254.pe.append(Shape255)
HAnimSite259 = x3d.HAnimSite()
HAnimSite259.name = "l_tarsal_distal_phalanx_4_tip"
HAnimSite259.DEF = "hanim_l_tarsal_distal_phalanx_4_tip"
HAnimSite259.translation = [0,1,0]
TouchSensor260 = x3d.TouchSensor()
TouchSensor260.description = "HAnimSite l_tarsal_distal_phalanx_4_tip"

HAnimSite259.children.append(TouchSensor260)
Shape261 = x3d.Shape()
Shape261.USE = "HAnimSiteShape"

HAnimSite259.children.append(Shape261)

HAnimJoint254.HAnimSite.append(HAnimSite259)
HAnimJoint262 = x3d.HAnimJoint()
HAnimJoint262.name = "l_tarsal_distal_interphalangeal_4"
HAnimJoint262.DEF = "hanim_l_tarsal_distal_interphalangeal_4"
HAnimJoint262.center = [0,1,0]
HAnimJoint262.ulimit = [0,0,0]
HAnimJoint262.llimit = [0,0,0]

HAnimJoint254.children.append(HAnimJoint262)

HAnimJoint249.children.append(HAnimJoint254)

HAnimJoint244.children.append(HAnimJoint249)

HAnimJoint235.children.append(HAnimJoint244)
HAnimJoint263 = x3d.HAnimJoint()
HAnimJoint263.name = "l_tarsometatarsal_5"
HAnimJoint263.DEF = "hanim_l_tarsometatarsal_5"
HAnimJoint263.center = [0,1,0]
HAnimJoint263.ulimit = [0,0,0]
HAnimJoint263.llimit = [0,0,0]
Shape264 = x3d.Shape()
LineSet265 = x3d.LineSet()
LineSet265.vertexCount = [1]
Coordinate266 = x3d.Coordinate()

LineSet265.coord = Coordinate266
#from l_tarsometatarsal_5 to l_metatarsophalangeal_5
ColorRGBA267 = x3d.ColorRGBA()
ColorRGBA267.USE = "HAnimSegmentLineColorRGBA"

LineSet265.color = ColorRGBA267

Shape264.geometry = LineSet265

HAnimJoint263.pe.append(Shape264)
HAnimSite268 = x3d.HAnimSite()
HAnimSite268.name = "l_metatarsal_phalanx_5_pt"
HAnimSite268.DEF = "hanim_l_metatarsal_phalanx_5_pt"
HAnimSite268.translation = [0,1,0]
TouchSensor269 = x3d.TouchSensor()
TouchSensor269.description = "HAnimSite l_metatarsal_phalanx_5_pt"

HAnimSite268.children.append(TouchSensor269)
Shape270 = x3d.Shape()
Shape270.USE = "HAnimSiteShape"

HAnimSite268.children.append(Shape270)

HAnimJoint263.HAnimSite.append(HAnimSite268)
HAnimJoint271 = x3d.HAnimJoint()
HAnimJoint271.name = "l_metatarsophalangeal_5"
HAnimJoint271.DEF = "hanim_l_metatarsophalangeal_5"
HAnimJoint271.center = [0,1,0]
HAnimJoint271.ulimit = [0,0,0]
HAnimJoint271.llimit = [0,0,0]
Shape272 = x3d.Shape()
LineSet273 = x3d.LineSet()
LineSet273.vertexCount = [1]
Coordinate274 = x3d.Coordinate()

LineSet273.coord = Coordinate274
#from l_metatarsophalangeal_5 to l_tarsal_proximal_interphalangeal_5
ColorRGBA275 = x3d.ColorRGBA()
ColorRGBA275.USE = "HAnimSegmentLineColorRGBA"

LineSet273.color = ColorRGBA275

Shape272.geometry = LineSet273

HAnimJoint271.pe.append(Shape272)
HAnimJoint276 = x3d.HAnimJoint()
HAnimJoint276.name = "l_tarsal_proximal_interphalangeal_5"
HAnimJoint276.DEF = "hanim_l_tarsal_proximal_interphalangeal_5"
HAnimJoint276.center = [0,1,0]
HAnimJoint276.ulimit = [0,0,0]
HAnimJoint276.llimit = [0,0,0]
Shape277 = x3d.Shape()
LineSet278 = x3d.LineSet()
LineSet278.vertexCount = [1]
Coordinate279 = x3d.Coordinate()

LineSet278.coord = Coordinate279
#from l_tarsal_proximal_interphalangeal_5 to l_tarsal_distal_interphalangeal_5
ColorRGBA280 = x3d.ColorRGBA()
ColorRGBA280.USE = "HAnimSegmentLineColorRGBA"

LineSet278.color = ColorRGBA280

Shape277.geometry = LineSet278

HAnimJoint276.pe.append(Shape277)
HAnimSite281 = x3d.HAnimSite()
HAnimSite281.name = "l_tarsal_distal_phalanx_5_tip"
HAnimSite281.DEF = "hanim_l_tarsal_distal_phalanx_5_tip"
HAnimSite281.translation = [0,1,0]
TouchSensor282 = x3d.TouchSensor()
TouchSensor282.description = "HAnimSite l_tarsal_distal_phalanx_5_tip"

HAnimSite281.children.append(TouchSensor282)
Shape283 = x3d.Shape()
Shape283.USE = "HAnimSiteShape"

HAnimSite281.children.append(Shape283)

HAnimJoint276.HAnimSite.append(HAnimSite281)
HAnimJoint284 = x3d.HAnimJoint()
HAnimJoint284.name = "l_tarsal_distal_interphalangeal_5"
HAnimJoint284.DEF = "hanim_l_tarsal_distal_interphalangeal_5"
HAnimJoint284.center = [0,1,0]
HAnimJoint284.ulimit = [0,0,0]
HAnimJoint284.llimit = [0,0,0]

HAnimJoint276.children.append(HAnimJoint284)

HAnimJoint271.children.append(HAnimJoint276)

HAnimJoint263.children.append(HAnimJoint271)

HAnimJoint235.children.append(HAnimJoint263)

HAnimJoint230.children.append(HAnimJoint235)

HAnimJoint138.children.append(HAnimJoint230)

HAnimJoint127.children.append(HAnimJoint138)

HAnimJoint113.children.append(HAnimJoint127)

HAnimJoint80.children.append(HAnimJoint113)
HAnimJoint285 = x3d.HAnimJoint()
HAnimJoint285.name = "r_hip"
HAnimJoint285.DEF = "hanim_r_hip"
HAnimJoint285.center = [-0.095,0.9171,0.0029]
HAnimJoint285.ulimit = [0,0,0]
HAnimJoint285.llimit = [0,0,0]
Shape286 = x3d.Shape()
LineSet287 = x3d.LineSet()
LineSet287.vertexCount = [2]
Coordinate288 = x3d.Coordinate()

LineSet287.coord = Coordinate288
#from r_hip to r_knee
ColorRGBA289 = x3d.ColorRGBA()
ColorRGBA289.USE = "HAnimSegmentLineColorRGBA"

LineSet287.color = ColorRGBA289

Shape286.geometry = LineSet287

HAnimJoint285.pe.append(Shape286)
HAnimSite290 = x3d.HAnimSite()
HAnimSite290.name = "r_lateral_malleolus_pt"
HAnimSite290.DEF = "hanim_r_lateral_malleolus_pt"
HAnimSite290.translation = [-0.1006,0.0658,-0.1075]
TouchSensor291 = x3d.TouchSensor()
TouchSensor291.description = "HAnimSite r_lateral_malleolus_pt"

HAnimSite290.children.append(TouchSensor291)
Shape292 = x3d.Shape()
Shape292.USE = "HAnimSiteShape"

HAnimSite290.children.append(Shape292)

HAnimJoint285.HAnimSite.append(HAnimSite290)
HAnimSite293 = x3d.HAnimSite()
HAnimSite293.name = "r_medial_malleolus_pt"
HAnimSite293.DEF = "hanim_r_medial_malleolus_pt"
HAnimSite293.translation = [-0.0591,0.076,-0.0928]
TouchSensor294 = x3d.TouchSensor()
TouchSensor294.description = "HAnimSite r_medial_malleolus_pt"

HAnimSite293.children.append(TouchSensor294)
Shape295 = x3d.Shape()
Shape295.USE = "HAnimSiteShape"

HAnimSite293.children.append(Shape295)

HAnimJoint285.HAnimSite.append(HAnimSite293)
HAnimSite296 = x3d.HAnimSite()
HAnimSite296.name = "r_tibiale_pt"
HAnimSite296.DEF = "hanim_r_tibiale_pt"
HAnimSite296.translation = [0,1,0]
TouchSensor297 = x3d.TouchSensor()
TouchSensor297.description = "HAnimSite r_tibiale_pt"

HAnimSite296.children.append(TouchSensor297)
Shape298 = x3d.Shape()
Shape298.USE = "HAnimSiteShape"

HAnimSite296.children.append(Shape298)

HAnimJoint285.HAnimSite.append(HAnimSite296)
HAnimJoint299 = x3d.HAnimJoint()
HAnimJoint299.name = "r_knee"
HAnimJoint299.DEF = "hanim_r_knee"
HAnimJoint299.center = [-0.0867,0.4913,0.0318]
HAnimJoint299.ulimit = [0,0,0]
HAnimJoint299.llimit = [0,0,0]
Shape300 = x3d.Shape()
LineSet301 = x3d.LineSet()
LineSet301.vertexCount = [2]
Coordinate302 = x3d.Coordinate()

LineSet301.coord = Coordinate302
#from r_knee to r_talocrural
ColorRGBA303 = x3d.ColorRGBA()
ColorRGBA303.USE = "HAnimSegmentLineColorRGBA"

LineSet301.color = ColorRGBA303

Shape300.geometry = LineSet301

HAnimJoint299.pe.append(Shape300)
HAnimSite304 = x3d.HAnimSite()
HAnimSite304.name = "r_calcaneus_posterior_pt"
HAnimSite304.DEF = "hanim_r_calcaneus_posterior_pt"
HAnimSite304.translation = [-0.0692,0.0297,-0.1221]
TouchSensor305 = x3d.TouchSensor()
TouchSensor305.description = "HAnimSite r_calcaneus_posterior_pt"

HAnimSite304.children.append(TouchSensor305)
Shape306 = x3d.Shape()
Shape306.USE = "HAnimSiteShape"

HAnimSite304.children.append(Shape306)

HAnimJoint299.HAnimSite.append(HAnimSite304)
HAnimSite307 = x3d.HAnimSite()
HAnimSite307.name = "r_sphyrion_pt"
HAnimSite307.DEF = "hanim_r_sphyrion_pt"
HAnimSite307.translation = [-0.0603,0.061,-0.1002]
TouchSensor308 = x3d.TouchSensor()
TouchSensor308.description = "HAnimSite r_sphyrion_pt"

HAnimSite307.children.append(TouchSensor308)
Shape309 = x3d.Shape()
Shape309.USE = "HAnimSiteShape"

HAnimSite307.children.append(Shape309)

HAnimJoint299.HAnimSite.append(HAnimSite307)
HAnimJoint310 = x3d.HAnimJoint()
HAnimJoint310.name = "r_talocrural"
HAnimJoint310.DEF = "hanim_r_talocrural"
HAnimJoint310.center = [-0.0801,0.0712,-0.0766]
HAnimJoint310.ulimit = [0,0,0]
HAnimJoint310.llimit = [0,0,0]
Shape311 = x3d.Shape()
LineSet312 = x3d.LineSet()
LineSet312.vertexCount = [2]
Coordinate313 = x3d.Coordinate()

LineSet312.coord = Coordinate313
#from r_talocrural to r_talocalcaneonavicular
ColorRGBA314 = x3d.ColorRGBA()
ColorRGBA314.USE = "HAnimSegmentLineColorRGBA"

LineSet312.color = ColorRGBA314

Shape311.geometry = LineSet312

HAnimJoint310.pe.append(Shape311)
Shape315 = x3d.Shape()
LineSet316 = x3d.LineSet()
LineSet316.vertexCount = [2]
Coordinate317 = x3d.Coordinate()

LineSet316.coord = Coordinate317
#from r_talocrural to r_calcaneocuboid
ColorRGBA318 = x3d.ColorRGBA()
ColorRGBA318.USE = "HAnimSegmentLineColorRGBA"

LineSet316.color = ColorRGBA318

Shape315.geometry = LineSet316

HAnimJoint310.pe.append(Shape315)
HAnimJoint319 = x3d.HAnimJoint()
HAnimJoint319.name = "r_talocalcaneonavicular"
HAnimJoint319.DEF = "hanim_r_talocalcaneonavicular"
HAnimJoint319.center = [0,1,0]
HAnimJoint319.ulimit = [0,0,0]
HAnimJoint319.llimit = [0,0,0]
Shape320 = x3d.Shape()
LineSet321 = x3d.LineSet()
LineSet321.vertexCount = [1]
Coordinate322 = x3d.Coordinate()

LineSet321.coord = Coordinate322
#from r_talocalcaneonavicular to r_cuneonavicular_1
ColorRGBA323 = x3d.ColorRGBA()
ColorRGBA323.USE = "HAnimSegmentLineColorRGBA"

LineSet321.color = ColorRGBA323

Shape320.geometry = LineSet321

HAnimJoint319.pe.append(Shape320)
Shape324 = x3d.Shape()
LineSet325 = x3d.LineSet()
LineSet325.vertexCount = [1]
Coordinate326 = x3d.Coordinate()

LineSet325.coord = Coordinate326
#from r_talocalcaneonavicular to r_cuneonavicular_2
ColorRGBA327 = x3d.ColorRGBA()
ColorRGBA327.USE = "HAnimSegmentLineColorRGBA"

LineSet325.color = ColorRGBA327

Shape324.geometry = LineSet325

HAnimJoint319.pe.append(Shape324)
Shape328 = x3d.Shape()
LineSet329 = x3d.LineSet()
LineSet329.vertexCount = [1]
Coordinate330 = x3d.Coordinate()

LineSet329.coord = Coordinate330
#from r_talocalcaneonavicular to r_cuneonavicular_3
ColorRGBA331 = x3d.ColorRGBA()
ColorRGBA331.USE = "HAnimSegmentLineColorRGBA"

LineSet329.color = ColorRGBA331

Shape328.geometry = LineSet329

HAnimJoint319.pe.append(Shape328)
HAnimJoint332 = x3d.HAnimJoint()
HAnimJoint332.name = "r_cuneonavicular_1"
HAnimJoint332.DEF = "hanim_r_cuneonavicular_1"
HAnimJoint332.center = [0,1,0]
HAnimJoint332.ulimit = [0,0,0]
HAnimJoint332.llimit = [0,0,0]
Shape333 = x3d.Shape()
LineSet334 = x3d.LineSet()
LineSet334.vertexCount = [1]
Coordinate335 = x3d.Coordinate()

LineSet334.coord = Coordinate335
#from r_cuneonavicular_1 to r_tarsometatarsal_1
ColorRGBA336 = x3d.ColorRGBA()
ColorRGBA336.USE = "HAnimSegmentLineColorRGBA"

LineSet334.color = ColorRGBA336

Shape333.geometry = LineSet334

HAnimJoint332.pe.append(Shape333)
HAnimJoint337 = x3d.HAnimJoint()
HAnimJoint337.name = "r_tarsometatarsal_1"
HAnimJoint337.DEF = "hanim_r_tarsometatarsal_1"
HAnimJoint337.center = [0,1,0]
HAnimJoint337.ulimit = [0,0,0]
HAnimJoint337.llimit = [0,0,0]
Shape338 = x3d.Shape()
LineSet339 = x3d.LineSet()
LineSet339.vertexCount = [1]
Coordinate340 = x3d.Coordinate()

LineSet339.coord = Coordinate340
#from r_tarsometatarsal_1 to r_metatarsophalangeal_1
ColorRGBA341 = x3d.ColorRGBA()
ColorRGBA341.USE = "HAnimSegmentLineColorRGBA"

LineSet339.color = ColorRGBA341

Shape338.geometry = LineSet339

HAnimJoint337.pe.append(Shape338)
HAnimSite342 = x3d.HAnimSite()
HAnimSite342.name = "r_metatarsal_phalanx_1_pt"
HAnimSite342.DEF = "hanim_r_metatarsal_phalanx_1_pt"
HAnimSite342.translation = [0,1,0]
TouchSensor343 = x3d.TouchSensor()
TouchSensor343.description = "HAnimSite r_metatarsal_phalanx_1_pt"

HAnimSite342.children.append(TouchSensor343)
Shape344 = x3d.Shape()
Shape344.USE = "HAnimSiteShape"

HAnimSite342.children.append(Shape344)

HAnimJoint337.HAnimSite.append(HAnimSite342)
HAnimJoint345 = x3d.HAnimJoint()
HAnimJoint345.name = "r_metatarsophalangeal_1"
HAnimJoint345.DEF = "hanim_r_metatarsophalangeal_1"
HAnimJoint345.center = [0,1,0]
HAnimJoint345.ulimit = [0,0,0]
HAnimJoint345.llimit = [0,0,0]
Shape346 = x3d.Shape()
LineSet347 = x3d.LineSet()
LineSet347.vertexCount = [1]
Coordinate348 = x3d.Coordinate()

LineSet347.coord = Coordinate348
#from r_metatarsophalangeal_1 to r_tarsal_interphalangeal_1
ColorRGBA349 = x3d.ColorRGBA()
ColorRGBA349.USE = "HAnimSegmentLineColorRGBA"

LineSet347.color = ColorRGBA349

Shape346.geometry = LineSet347

HAnimJoint345.pe.append(Shape346)
HAnimSite350 = x3d.HAnimSite()
HAnimSite350.name = "r_tarsal_distal_phalanx_1_tip"
HAnimSite350.DEF = "hanim_r_tarsal_distal_phalanx_1_tip"
HAnimSite350.translation = [0,1,0]
TouchSensor351 = x3d.TouchSensor()
TouchSensor351.description = "HAnimSite r_tarsal_distal_phalanx_1_tip"

HAnimSite350.children.append(TouchSensor351)
Shape352 = x3d.Shape()
Shape352.USE = "HAnimSiteShape"

HAnimSite350.children.append(Shape352)

HAnimJoint345.HAnimSite.append(HAnimSite350)
HAnimJoint353 = x3d.HAnimJoint()
HAnimJoint353.name = "r_tarsal_interphalangeal_1"
HAnimJoint353.DEF = "hanim_r_tarsal_interphalangeal_1"
HAnimJoint353.center = [0,1,0]
HAnimJoint353.ulimit = [0,0,0]
HAnimJoint353.llimit = [0,0,0]

HAnimJoint345.children.append(HAnimJoint353)

HAnimJoint337.children.append(HAnimJoint345)

HAnimJoint332.children.append(HAnimJoint337)

HAnimJoint319.children.append(HAnimJoint332)
HAnimJoint354 = x3d.HAnimJoint()
HAnimJoint354.name = "r_cuneonavicular_2"
HAnimJoint354.DEF = "hanim_r_cuneonavicular_2"
HAnimJoint354.center = [0,1,0]
HAnimJoint354.ulimit = [0,0,0]
HAnimJoint354.llimit = [0,0,0]
Shape355 = x3d.Shape()
LineSet356 = x3d.LineSet()
LineSet356.vertexCount = [1]
Coordinate357 = x3d.Coordinate()

LineSet356.coord = Coordinate357
#from r_cuneonavicular_2 to r_tarsometatarsal_2
ColorRGBA358 = x3d.ColorRGBA()
ColorRGBA358.USE = "HAnimSegmentLineColorRGBA"

LineSet356.color = ColorRGBA358

Shape355.geometry = LineSet356

HAnimJoint354.pe.append(Shape355)
HAnimJoint359 = x3d.HAnimJoint()
HAnimJoint359.name = "r_tarsometatarsal_2"
HAnimJoint359.DEF = "hanim_r_tarsometatarsal_2"
HAnimJoint359.center = [0,1,0]
HAnimJoint359.ulimit = [0,0,0]
HAnimJoint359.llimit = [0,0,0]
Shape360 = x3d.Shape()
LineSet361 = x3d.LineSet()
LineSet361.vertexCount = [1]
Coordinate362 = x3d.Coordinate()

LineSet361.coord = Coordinate362
#from r_tarsometatarsal_2 to r_metatarsophalangeal_2
ColorRGBA363 = x3d.ColorRGBA()
ColorRGBA363.USE = "HAnimSegmentLineColorRGBA"

LineSet361.color = ColorRGBA363

Shape360.geometry = LineSet361

HAnimJoint359.pe.append(Shape360)
HAnimJoint364 = x3d.HAnimJoint()
HAnimJoint364.name = "r_metatarsophalangeal_2"
HAnimJoint364.DEF = "hanim_r_metatarsophalangeal_2"
HAnimJoint364.center = [0,1,0]
HAnimJoint364.ulimit = [0,0,0]
HAnimJoint364.llimit = [0,0,0]
Shape365 = x3d.Shape()
LineSet366 = x3d.LineSet()
LineSet366.vertexCount = [1]
Coordinate367 = x3d.Coordinate()

LineSet366.coord = Coordinate367
#from r_metatarsophalangeal_2 to r_tarsal_proximal_interphalangeal_2
ColorRGBA368 = x3d.ColorRGBA()
ColorRGBA368.USE = "HAnimSegmentLineColorRGBA"

LineSet366.color = ColorRGBA368

Shape365.geometry = LineSet366

HAnimJoint364.pe.append(Shape365)
HAnimJoint369 = x3d.HAnimJoint()
HAnimJoint369.name = "r_tarsal_proximal_interphalangeal_2"
HAnimJoint369.DEF = "hanim_r_tarsal_proximal_interphalangeal_2"
HAnimJoint369.center = [0,1,0]
HAnimJoint369.ulimit = [0,0,0]
HAnimJoint369.llimit = [0,0,0]
Shape370 = x3d.Shape()
LineSet371 = x3d.LineSet()
LineSet371.vertexCount = [1]
Coordinate372 = x3d.Coordinate()

LineSet371.coord = Coordinate372
#from r_tarsal_proximal_interphalangeal_2 to r_tarsal_distal_interphalangeal_2
ColorRGBA373 = x3d.ColorRGBA()
ColorRGBA373.USE = "HAnimSegmentLineColorRGBA"

LineSet371.color = ColorRGBA373

Shape370.geometry = LineSet371

HAnimJoint369.pe.append(Shape370)
HAnimSite374 = x3d.HAnimSite()
HAnimSite374.name = "r_tarsal_distal_phalanx_2_tip"
HAnimSite374.DEF = "hanim_r_tarsal_distal_phalanx_2_tip"
HAnimSite374.translation = [-0.0883,0.0134,0.1383]
TouchSensor375 = x3d.TouchSensor()
TouchSensor375.description = "HAnimSite r_tarsal_distal_phalanx_2_tip"

HAnimSite374.children.append(TouchSensor375)
Shape376 = x3d.Shape()
Shape376.USE = "HAnimSiteShape"

HAnimSite374.children.append(Shape376)

HAnimJoint369.HAnimSite.append(HAnimSite374)
HAnimJoint377 = x3d.HAnimJoint()
HAnimJoint377.name = "r_tarsal_distal_interphalangeal_2"
HAnimJoint377.DEF = "hanim_r_tarsal_distal_interphalangeal_2"
HAnimJoint377.center = [0,1,0]
HAnimJoint377.ulimit = [0,0,0]
HAnimJoint377.llimit = [0,0,0]

HAnimJoint369.children.append(HAnimJoint377)

HAnimJoint364.children.append(HAnimJoint369)

HAnimJoint359.children.append(HAnimJoint364)

HAnimJoint354.children.append(HAnimJoint359)

HAnimJoint319.children.append(HAnimJoint354)
HAnimJoint378 = x3d.HAnimJoint()
HAnimJoint378.name = "r_cuneonavicular_3"
HAnimJoint378.DEF = "hanim_r_cuneonavicular_3"
HAnimJoint378.center = [0,1,0]
HAnimJoint378.ulimit = [0,0,0]
HAnimJoint378.llimit = [0,0,0]
Shape379 = x3d.Shape()
LineSet380 = x3d.LineSet()
LineSet380.vertexCount = [1]
Coordinate381 = x3d.Coordinate()

LineSet380.coord = Coordinate381
#from r_cuneonavicular_3 to r_tarsometatarsal_3
ColorRGBA382 = x3d.ColorRGBA()
ColorRGBA382.USE = "HAnimSegmentLineColorRGBA"

LineSet380.color = ColorRGBA382

Shape379.geometry = LineSet380

HAnimJoint378.pe.append(Shape379)
HAnimJoint383 = x3d.HAnimJoint()
HAnimJoint383.name = "r_tarsometatarsal_3"
HAnimJoint383.DEF = "hanim_r_tarsometatarsal_3"
HAnimJoint383.center = [0,1,0]
HAnimJoint383.ulimit = [0,0,0]
HAnimJoint383.llimit = [0,0,0]
Shape384 = x3d.Shape()
LineSet385 = x3d.LineSet()
LineSet385.vertexCount = [1]
Coordinate386 = x3d.Coordinate()

LineSet385.coord = Coordinate386
#from r_tarsometatarsal_3 to r_metatarsophalangeal_3
ColorRGBA387 = x3d.ColorRGBA()
ColorRGBA387.USE = "HAnimSegmentLineColorRGBA"

LineSet385.color = ColorRGBA387

Shape384.geometry = LineSet385

HAnimJoint383.pe.append(Shape384)
HAnimJoint388 = x3d.HAnimJoint()
HAnimJoint388.name = "r_metatarsophalangeal_3"
HAnimJoint388.DEF = "hanim_r_metatarsophalangeal_3"
HAnimJoint388.center = [0,1,0]
HAnimJoint388.ulimit = [0,0,0]
HAnimJoint388.llimit = [0,0,0]
Shape389 = x3d.Shape()
LineSet390 = x3d.LineSet()
LineSet390.vertexCount = [1]
Coordinate391 = x3d.Coordinate()

LineSet390.coord = Coordinate391
#from r_metatarsophalangeal_3 to r_tarsal_proximal_interphalangeal_3
ColorRGBA392 = x3d.ColorRGBA()
ColorRGBA392.USE = "HAnimSegmentLineColorRGBA"

LineSet390.color = ColorRGBA392

Shape389.geometry = LineSet390

HAnimJoint388.pe.append(Shape389)
HAnimJoint393 = x3d.HAnimJoint()
HAnimJoint393.name = "r_tarsal_proximal_interphalangeal_3"
HAnimJoint393.DEF = "hanim_r_tarsal_proximal_interphalangeal_3"
HAnimJoint393.center = [0,1,0]
HAnimJoint393.ulimit = [0,0,0]
HAnimJoint393.llimit = [0,0,0]
Shape394 = x3d.Shape()
LineSet395 = x3d.LineSet()
LineSet395.vertexCount = [1]
Coordinate396 = x3d.Coordinate()

LineSet395.coord = Coordinate396
#from r_tarsal_proximal_interphalangeal_3 to r_tarsal_distal_interphalangeal_3
ColorRGBA397 = x3d.ColorRGBA()
ColorRGBA397.USE = "HAnimSegmentLineColorRGBA"

LineSet395.color = ColorRGBA397

Shape394.geometry = LineSet395

HAnimJoint393.pe.append(Shape394)
HAnimSite398 = x3d.HAnimSite()
HAnimSite398.name = "r_tarsal_distal_phalanx_3_tip"
HAnimSite398.DEF = "hanim_r_tarsal_distal_phalanx_3_tip"
HAnimSite398.translation = [0,1,0]
TouchSensor399 = x3d.TouchSensor()
TouchSensor399.description = "HAnimSite r_tarsal_distal_phalanx_3_tip"

HAnimSite398.children.append(TouchSensor399)
Shape400 = x3d.Shape()
Shape400.USE = "HAnimSiteShape"

HAnimSite398.children.append(Shape400)

HAnimJoint393.HAnimSite.append(HAnimSite398)
HAnimJoint401 = x3d.HAnimJoint()
HAnimJoint401.name = "r_tarsal_distal_interphalangeal_3"
HAnimJoint401.DEF = "hanim_r_tarsal_distal_interphalangeal_3"
HAnimJoint401.center = [0,1,0]
HAnimJoint401.ulimit = [0,0,0]
HAnimJoint401.llimit = [0,0,0]

HAnimJoint393.children.append(HAnimJoint401)

HAnimJoint388.children.append(HAnimJoint393)

HAnimJoint383.children.append(HAnimJoint388)

HAnimJoint378.children.append(HAnimJoint383)

HAnimJoint319.children.append(HAnimJoint378)

HAnimJoint310.children.append(HAnimJoint319)
HAnimJoint402 = x3d.HAnimJoint()
HAnimJoint402.name = "r_calcaneocuboid"
HAnimJoint402.DEF = "hanim_r_calcaneocuboid"
HAnimJoint402.center = [0,1,0]
HAnimJoint402.ulimit = [0,0,0]
HAnimJoint402.llimit = [0,0,0]
Shape403 = x3d.Shape()
LineSet404 = x3d.LineSet()
LineSet404.vertexCount = [1]
Coordinate405 = x3d.Coordinate()

LineSet404.coord = Coordinate405
#from r_calcaneocuboid to r_transversetarsal
ColorRGBA406 = x3d.ColorRGBA()
ColorRGBA406.USE = "HAnimSegmentLineColorRGBA"

LineSet404.color = ColorRGBA406

Shape403.geometry = LineSet404

HAnimJoint402.pe.append(Shape403)
HAnimJoint407 = x3d.HAnimJoint()
HAnimJoint407.name = "r_transversetarsal"
HAnimJoint407.DEF = "hanim_r_transversetarsal"
HAnimJoint407.center = [0,1,0]
HAnimJoint407.ulimit = [0,0,0]
HAnimJoint407.llimit = [0,0,0]
Shape408 = x3d.Shape()
LineSet409 = x3d.LineSet()
LineSet409.vertexCount = [1]
Coordinate410 = x3d.Coordinate()

LineSet409.coord = Coordinate410
#from r_transversetarsal to r_tarsometatarsal_4
ColorRGBA411 = x3d.ColorRGBA()
ColorRGBA411.USE = "HAnimSegmentLineColorRGBA"

LineSet409.color = ColorRGBA411

Shape408.geometry = LineSet409

HAnimJoint407.pe.append(Shape408)
Shape412 = x3d.Shape()
LineSet413 = x3d.LineSet()
LineSet413.vertexCount = [1]
Coordinate414 = x3d.Coordinate()

LineSet413.coord = Coordinate414
#from r_transversetarsal to r_tarsometatarsal_5
ColorRGBA415 = x3d.ColorRGBA()
ColorRGBA415.USE = "HAnimSegmentLineColorRGBA"

LineSet413.color = ColorRGBA415

Shape412.geometry = LineSet413

HAnimJoint407.pe.append(Shape412)
HAnimJoint416 = x3d.HAnimJoint()
HAnimJoint416.name = "r_tarsometatarsal_4"
HAnimJoint416.DEF = "hanim_r_tarsometatarsal_4"
HAnimJoint416.center = [0,1,0]
HAnimJoint416.ulimit = [0,0,0]
HAnimJoint416.llimit = [0,0,0]
Shape417 = x3d.Shape()
LineSet418 = x3d.LineSet()
LineSet418.vertexCount = [1]
Coordinate419 = x3d.Coordinate()

LineSet418.coord = Coordinate419
#from r_tarsometatarsal_4 to r_metatarsophalangeal_4
ColorRGBA420 = x3d.ColorRGBA()
ColorRGBA420.USE = "HAnimSegmentLineColorRGBA"

LineSet418.color = ColorRGBA420

Shape417.geometry = LineSet418

HAnimJoint416.pe.append(Shape417)
HAnimJoint421 = x3d.HAnimJoint()
HAnimJoint421.name = "r_metatarsophalangeal_4"
HAnimJoint421.DEF = "hanim_r_metatarsophalangeal_4"
HAnimJoint421.center = [0,1,0]
HAnimJoint421.ulimit = [0,0,0]
HAnimJoint421.llimit = [0,0,0]
Shape422 = x3d.Shape()
LineSet423 = x3d.LineSet()
LineSet423.vertexCount = [1]
Coordinate424 = x3d.Coordinate()

LineSet423.coord = Coordinate424
#from r_metatarsophalangeal_4 to r_tarsal_proximal_interphalangeal_4
ColorRGBA425 = x3d.ColorRGBA()
ColorRGBA425.USE = "HAnimSegmentLineColorRGBA"

LineSet423.color = ColorRGBA425

Shape422.geometry = LineSet423

HAnimJoint421.pe.append(Shape422)
HAnimJoint426 = x3d.HAnimJoint()
HAnimJoint426.name = "r_tarsal_proximal_interphalangeal_4"
HAnimJoint426.DEF = "hanim_r_tarsal_proximal_interphalangeal_4"
HAnimJoint426.center = [0,1,0]
HAnimJoint426.ulimit = [0,0,0]
HAnimJoint426.llimit = [0,0,0]
Shape427 = x3d.Shape()
LineSet428 = x3d.LineSet()
LineSet428.vertexCount = [1]
Coordinate429 = x3d.Coordinate()

LineSet428.coord = Coordinate429
#from r_tarsal_proximal_interphalangeal_4 to r_tarsal_distal_interphalangeal_4
ColorRGBA430 = x3d.ColorRGBA()
ColorRGBA430.USE = "HAnimSegmentLineColorRGBA"

LineSet428.color = ColorRGBA430

Shape427.geometry = LineSet428

HAnimJoint426.pe.append(Shape427)
HAnimSite431 = x3d.HAnimSite()
HAnimSite431.name = "r_tarsal_distal_phalanx_4_tip"
HAnimSite431.DEF = "hanim_r_tarsal_distal_phalanx_4_tip"
HAnimSite431.translation = [0,1,0]
TouchSensor432 = x3d.TouchSensor()
TouchSensor432.description = "HAnimSite r_tarsal_distal_phalanx_4_tip"

HAnimSite431.children.append(TouchSensor432)
Shape433 = x3d.Shape()
Shape433.USE = "HAnimSiteShape"

HAnimSite431.children.append(Shape433)

HAnimJoint426.HAnimSite.append(HAnimSite431)
HAnimJoint434 = x3d.HAnimJoint()
HAnimJoint434.name = "r_tarsal_distal_interphalangeal_4"
HAnimJoint434.DEF = "hanim_r_tarsal_distal_interphalangeal_4"
HAnimJoint434.center = [0,1,0]
HAnimJoint434.ulimit = [0,0,0]
HAnimJoint434.llimit = [0,0,0]

HAnimJoint426.children.append(HAnimJoint434)

HAnimJoint421.children.append(HAnimJoint426)

HAnimJoint416.children.append(HAnimJoint421)

HAnimJoint407.children.append(HAnimJoint416)
HAnimJoint435 = x3d.HAnimJoint()
HAnimJoint435.name = "r_tarsometatarsal_5"
HAnimJoint435.DEF = "hanim_r_tarsometatarsal_5"
HAnimJoint435.center = [0,1,0]
HAnimJoint435.ulimit = [0,0,0]
HAnimJoint435.llimit = [0,0,0]
Shape436 = x3d.Shape()
LineSet437 = x3d.LineSet()
LineSet437.vertexCount = [1]
Coordinate438 = x3d.Coordinate()

LineSet437.coord = Coordinate438
#from r_tarsometatarsal_5 to r_metatarsophalangeal_5
ColorRGBA439 = x3d.ColorRGBA()
ColorRGBA439.USE = "HAnimSegmentLineColorRGBA"

LineSet437.color = ColorRGBA439

Shape436.geometry = LineSet437

HAnimJoint435.pe.append(Shape436)
HAnimSite440 = x3d.HAnimSite()
HAnimSite440.name = "r_metatarsal_phalanx_5_pt"
HAnimSite440.DEF = "hanim_r_metatarsal_phalanx_5_pt"
HAnimSite440.translation = [0,1,0]
TouchSensor441 = x3d.TouchSensor()
TouchSensor441.description = "HAnimSite r_metatarsal_phalanx_5_pt"

HAnimSite440.children.append(TouchSensor441)
Shape442 = x3d.Shape()
Shape442.USE = "HAnimSiteShape"

HAnimSite440.children.append(Shape442)

HAnimJoint435.HAnimSite.append(HAnimSite440)
HAnimJoint443 = x3d.HAnimJoint()
HAnimJoint443.name = "r_metatarsophalangeal_5"
HAnimJoint443.DEF = "hanim_r_metatarsophalangeal_5"
HAnimJoint443.center = [0,1,0]
HAnimJoint443.ulimit = [0,0,0]
HAnimJoint443.llimit = [0,0,0]
Shape444 = x3d.Shape()
LineSet445 = x3d.LineSet()
LineSet445.vertexCount = [1]
Coordinate446 = x3d.Coordinate()

LineSet445.coord = Coordinate446
#from r_metatarsophalangeal_5 to r_tarsal_proximal_interphalangeal_5
ColorRGBA447 = x3d.ColorRGBA()
ColorRGBA447.USE = "HAnimSegmentLineColorRGBA"

LineSet445.color = ColorRGBA447

Shape444.geometry = LineSet445

HAnimJoint443.pe.append(Shape444)
HAnimJoint448 = x3d.HAnimJoint()
HAnimJoint448.name = "r_tarsal_proximal_interphalangeal_5"
HAnimJoint448.DEF = "hanim_r_tarsal_proximal_interphalangeal_5"
HAnimJoint448.center = [0,1,0]
HAnimJoint448.ulimit = [0,0,0]
HAnimJoint448.llimit = [0,0,0]
Shape449 = x3d.Shape()
LineSet450 = x3d.LineSet()
LineSet450.vertexCount = [1]
Coordinate451 = x3d.Coordinate()

LineSet450.coord = Coordinate451
#from r_tarsal_proximal_interphalangeal_5 to r_tarsal_distal_interphalangeal_5
ColorRGBA452 = x3d.ColorRGBA()
ColorRGBA452.USE = "HAnimSegmentLineColorRGBA"

LineSet450.color = ColorRGBA452

Shape449.geometry = LineSet450

HAnimJoint448.pe.append(Shape449)
HAnimSite453 = x3d.HAnimSite()
HAnimSite453.name = "r_tarsal_distal_phalanx_5_tip"
HAnimSite453.DEF = "hanim_r_tarsal_distal_phalanx_5_tip"
HAnimSite453.translation = [0,1,0]
TouchSensor454 = x3d.TouchSensor()
TouchSensor454.description = "HAnimSite r_tarsal_distal_phalanx_5_tip"

HAnimSite453.children.append(TouchSensor454)
Shape455 = x3d.Shape()
Shape455.USE = "HAnimSiteShape"

HAnimSite453.children.append(Shape455)

HAnimJoint448.HAnimSite.append(HAnimSite453)
HAnimJoint456 = x3d.HAnimJoint()
HAnimJoint456.name = "r_tarsal_distal_interphalangeal_5"
HAnimJoint456.DEF = "hanim_r_tarsal_distal_interphalangeal_5"
HAnimJoint456.center = [0,1,0]
HAnimJoint456.ulimit = [0,0,0]
HAnimJoint456.llimit = [0,0,0]

HAnimJoint448.children.append(HAnimJoint456)

HAnimJoint443.children.append(HAnimJoint448)

HAnimJoint435.children.append(HAnimJoint443)

HAnimJoint407.children.append(HAnimJoint435)

HAnimJoint402.children.append(HAnimJoint407)

HAnimJoint310.children.append(HAnimJoint402)

HAnimJoint299.children.append(HAnimJoint310)

HAnimJoint285.children.append(HAnimJoint299)

HAnimJoint80.children.append(HAnimJoint285)

HAnimJoint32.children.append(HAnimJoint80)
HAnimJoint457 = x3d.HAnimJoint()
HAnimJoint457.name = "vl5"
HAnimJoint457.DEF = "hanim_vl5"
HAnimJoint457.center = [0.0028,1.0568,-0.0776]
HAnimJoint457.ulimit = [0,0,0]
HAnimJoint457.llimit = [0,0,0]
Shape458 = x3d.Shape()
LineSet459 = x3d.LineSet()
LineSet459.vertexCount = [2]
Coordinate460 = x3d.Coordinate()

LineSet459.coord = Coordinate460
#from vl5 to vl4
ColorRGBA461 = x3d.ColorRGBA()
ColorRGBA461.USE = "HAnimSegmentLineColorRGBA"

LineSet459.color = ColorRGBA461

Shape458.geometry = LineSet459

HAnimJoint457.pe.append(Shape458)
HAnimJoint462 = x3d.HAnimJoint()
HAnimJoint462.name = "vl4"
HAnimJoint462.DEF = "hanim_vl4"
HAnimJoint462.center = [0.0035,1.0925,-0.0787]
HAnimJoint462.ulimit = [0,0,0]
HAnimJoint462.llimit = [0,0,0]
Shape463 = x3d.Shape()
LineSet464 = x3d.LineSet()
LineSet464.vertexCount = [2]
Coordinate465 = x3d.Coordinate()

LineSet464.coord = Coordinate465
#from vl4 to vl3
ColorRGBA466 = x3d.ColorRGBA()
ColorRGBA466.USE = "HAnimSegmentLineColorRGBA"

LineSet464.color = ColorRGBA466

Shape463.geometry = LineSet464

HAnimJoint462.pe.append(Shape463)
HAnimJoint467 = x3d.HAnimJoint()
HAnimJoint467.name = "vl3"
HAnimJoint467.DEF = "hanim_vl3"
HAnimJoint467.center = [0.0041,1.1276,-0.0796]
HAnimJoint467.ulimit = [0,0,0]
HAnimJoint467.llimit = [0,0,0]
Shape468 = x3d.Shape()
LineSet469 = x3d.LineSet()
LineSet469.vertexCount = [2]
Coordinate470 = x3d.Coordinate()

LineSet469.coord = Coordinate470
#from vl3 to vl2
ColorRGBA471 = x3d.ColorRGBA()
ColorRGBA471.USE = "HAnimSegmentLineColorRGBA"

LineSet469.color = ColorRGBA471

Shape468.geometry = LineSet469

HAnimJoint467.pe.append(Shape468)
HAnimSite472 = x3d.HAnimSite()
HAnimSite472.name = "l_rib10_pt"
HAnimSite472.DEF = "hanim_l_rib10_pt"
HAnimSite472.translation = [0.0871,1.1925,0.0992]
TouchSensor473 = x3d.TouchSensor()
TouchSensor473.description = "HAnimSite l_rib10_pt"

HAnimSite472.children.append(TouchSensor473)
Shape474 = x3d.Shape()
Shape474.USE = "HAnimSiteShape"

HAnimSite472.children.append(Shape474)

HAnimJoint467.HAnimSite.append(HAnimSite472)
HAnimSite475 = x3d.HAnimSite()
HAnimSite475.name = "r_rib10_pt"
HAnimSite475.DEF = "hanim_r_rib10_pt"
HAnimSite475.translation = [-0.0711,1.1941,0.1016]
TouchSensor476 = x3d.TouchSensor()
TouchSensor476.description = "HAnimSite r_rib10_pt"

HAnimSite475.children.append(TouchSensor476)
Shape477 = x3d.Shape()
Shape477.USE = "HAnimSiteShape"

HAnimSite475.children.append(Shape477)

HAnimJoint467.HAnimSite.append(HAnimSite475)
HAnimSite478 = x3d.HAnimSite()
HAnimSite478.name = "spine_2_middle_back_pt"
HAnimSite478.DEF = "hanim_spine_2_middle_back_pt"
HAnimSite478.translation = [0,1,0]
TouchSensor479 = x3d.TouchSensor()
TouchSensor479.description = "HAnimSite spine_2_middle_back_pt"

HAnimSite478.children.append(TouchSensor479)
Shape480 = x3d.Shape()
Shape480.USE = "HAnimSiteShape"

HAnimSite478.children.append(Shape480)

HAnimJoint467.HAnimSite.append(HAnimSite478)
HAnimJoint481 = x3d.HAnimJoint()
HAnimJoint481.name = "vl2"
HAnimJoint481.DEF = "hanim_vl2"
HAnimJoint481.center = [0.0045,1.1546,-0.08]
HAnimJoint481.ulimit = [0,0,0]
HAnimJoint481.llimit = [0,0,0]
Shape482 = x3d.Shape()
LineSet483 = x3d.LineSet()
LineSet483.vertexCount = [2]
Coordinate484 = x3d.Coordinate()

LineSet483.coord = Coordinate484
#from vl2 to vl1
ColorRGBA485 = x3d.ColorRGBA()
ColorRGBA485.USE = "HAnimSegmentLineColorRGBA"

LineSet483.color = ColorRGBA485

Shape482.geometry = LineSet483

HAnimJoint481.pe.append(Shape482)
HAnimJoint486 = x3d.HAnimJoint()
HAnimJoint486.name = "vl1"
HAnimJoint486.DEF = "hanim_vl1"
HAnimJoint486.center = [0.0048,1.1912,-0.0805]
HAnimJoint486.ulimit = [0,0,0]
HAnimJoint486.llimit = [0,0,0]
Shape487 = x3d.Shape()
LineSet488 = x3d.LineSet()
LineSet488.vertexCount = [2]
Coordinate489 = x3d.Coordinate()

LineSet488.coord = Coordinate489
#from vl1 to vt12
ColorRGBA490 = x3d.ColorRGBA()
ColorRGBA490.USE = "HAnimSegmentLineColorRGBA"

LineSet488.color = ColorRGBA490

Shape487.geometry = LineSet488

HAnimJoint486.pe.append(Shape487)
HAnimJoint491 = x3d.HAnimJoint()
HAnimJoint491.name = "vt12"
HAnimJoint491.DEF = "hanim_vt12"
HAnimJoint491.center = [0.0051,1.2278,-0.0808]
HAnimJoint491.ulimit = [0,0,0]
HAnimJoint491.llimit = [0,0,0]
Shape492 = x3d.Shape()
LineSet493 = x3d.LineSet()
LineSet493.vertexCount = [2]
Coordinate494 = x3d.Coordinate()

LineSet493.coord = Coordinate494
#from vt12 to vt11
ColorRGBA495 = x3d.ColorRGBA()
ColorRGBA495.USE = "HAnimSegmentLineColorRGBA"

LineSet493.color = ColorRGBA495

Shape492.geometry = LineSet493

HAnimJoint491.pe.append(Shape492)
HAnimJoint496 = x3d.HAnimJoint()
HAnimJoint496.name = "vt11"
HAnimJoint496.DEF = "hanim_vt11"
HAnimJoint496.center = [0.0053,1.2679,-0.081]
HAnimJoint496.ulimit = [0,0,0]
HAnimJoint496.llimit = [0,0,0]
Shape497 = x3d.Shape()
LineSet498 = x3d.LineSet()
LineSet498.vertexCount = [2]
Coordinate499 = x3d.Coordinate()

LineSet498.coord = Coordinate499
#from vt11 to vt10
ColorRGBA500 = x3d.ColorRGBA()
ColorRGBA500.USE = "HAnimSegmentLineColorRGBA"

LineSet498.color = ColorRGBA500

Shape497.geometry = LineSet498

HAnimJoint496.pe.append(Shape497)
HAnimSite501 = x3d.HAnimSite()
HAnimSite501.name = "substernale_pt"
HAnimSite501.DEF = "hanim_substernale_pt"
HAnimSite501.translation = [0.0085,1.2995,0.1147]
TouchSensor502 = x3d.TouchSensor()
TouchSensor502.description = "HAnimSite substernale_pt"

HAnimSite501.children.append(TouchSensor502)
Shape503 = x3d.Shape()
Shape503.USE = "HAnimSiteShape"

HAnimSite501.children.append(Shape503)

HAnimJoint496.HAnimSite.append(HAnimSite501)
HAnimJoint504 = x3d.HAnimJoint()
HAnimJoint504.name = "vt10"
HAnimJoint504.DEF = "hanim_vt10"
HAnimJoint504.center = [0.0056,1.2848,-0.0822]
HAnimJoint504.ulimit = [0,0,0]
HAnimJoint504.llimit = [0,0,0]
Shape505 = x3d.Shape()
LineSet506 = x3d.LineSet()
LineSet506.vertexCount = [2]
Coordinate507 = x3d.Coordinate()

LineSet506.coord = Coordinate507
#from vt10 to vt9
ColorRGBA508 = x3d.ColorRGBA()
ColorRGBA508.USE = "HAnimSegmentLineColorRGBA"

LineSet506.color = ColorRGBA508

Shape505.geometry = LineSet506

HAnimJoint504.pe.append(Shape505)
HAnimSite509 = x3d.HAnimSite()
HAnimSite509.name = "l_thelion_pt"
HAnimSite509.DEF = "hanim_l_thelion_pt"
HAnimSite509.translation = [0.0918,1.3382,0.1192]
TouchSensor510 = x3d.TouchSensor()
TouchSensor510.description = "HAnimSite l_thelion_pt"

HAnimSite509.children.append(TouchSensor510)
Shape511 = x3d.Shape()
Shape511.USE = "HAnimSiteShape"

HAnimSite509.children.append(Shape511)

HAnimJoint504.HAnimSite.append(HAnimSite509)
HAnimSite512 = x3d.HAnimSite()
HAnimSite512.name = "r_thelion_pt"
HAnimSite512.DEF = "hanim_r_thelion_pt"
HAnimSite512.translation = [-0.0736,1.3385,0.1217]
TouchSensor513 = x3d.TouchSensor()
TouchSensor513.description = "HAnimSite r_thelion_pt"

HAnimSite512.children.append(TouchSensor513)
Shape514 = x3d.Shape()
Shape514.USE = "HAnimSiteShape"

HAnimSite512.children.append(Shape514)

HAnimJoint504.HAnimSite.append(HAnimSite512)
HAnimJoint515 = x3d.HAnimJoint()
HAnimJoint515.name = "vt9"
HAnimJoint515.DEF = "hanim_vt9"
HAnimJoint515.center = [0.0057,1.3126,-0.0838]
HAnimJoint515.ulimit = [0,0,0]
HAnimJoint515.llimit = [0,0,0]
Shape516 = x3d.Shape()
LineSet517 = x3d.LineSet()
LineSet517.vertexCount = [2]
Coordinate518 = x3d.Coordinate()

LineSet517.coord = Coordinate518
#from vt9 to vt8
ColorRGBA519 = x3d.ColorRGBA()
ColorRGBA519.USE = "HAnimSegmentLineColorRGBA"

LineSet517.color = ColorRGBA519

Shape516.geometry = LineSet517

HAnimJoint515.pe.append(Shape516)
HAnimJoint520 = x3d.HAnimJoint()
HAnimJoint520.name = "vt8"
HAnimJoint520.DEF = "hanim_vt8"
HAnimJoint520.center = [0.0057,1.3382,-0.0845]
HAnimJoint520.ulimit = [0,0,0]
HAnimJoint520.llimit = [0,0,0]
Shape521 = x3d.Shape()
LineSet522 = x3d.LineSet()
LineSet522.vertexCount = [2]
Coordinate523 = x3d.Coordinate()

LineSet522.coord = Coordinate523
#from vt8 to vt7
ColorRGBA524 = x3d.ColorRGBA()
ColorRGBA524.USE = "HAnimSegmentLineColorRGBA"

LineSet522.color = ColorRGBA524

Shape521.geometry = LineSet522

HAnimJoint520.pe.append(Shape521)
HAnimJoint525 = x3d.HAnimJoint()
HAnimJoint525.name = "vt7"
HAnimJoint525.DEF = "hanim_vt7"
HAnimJoint525.center = [0.0058,1.3625,-0.0833]
HAnimJoint525.ulimit = [0,0,0]
HAnimJoint525.llimit = [0,0,0]
Shape526 = x3d.Shape()
LineSet527 = x3d.LineSet()
LineSet527.vertexCount = [2]
Coordinate528 = x3d.Coordinate()

LineSet527.coord = Coordinate528
#from vt7 to vt6
ColorRGBA529 = x3d.ColorRGBA()
ColorRGBA529.USE = "HAnimSegmentLineColorRGBA"

LineSet527.color = ColorRGBA529

Shape526.geometry = LineSet527

HAnimJoint525.pe.append(Shape526)
HAnimSite530 = x3d.HAnimSite()
HAnimSite530.name = "l_chest_midsagittal_plane_pt"
HAnimSite530.DEF = "hanim_l_chest_midsagittal_plane_pt"
HAnimSite530.translation = [0,1,0]
TouchSensor531 = x3d.TouchSensor()
TouchSensor531.description = "HAnimSite l_chest_midsagittal_plane_pt"

HAnimSite530.children.append(TouchSensor531)
Shape532 = x3d.Shape()
Shape532.USE = "HAnimSiteShape"

HAnimSite530.children.append(Shape532)

HAnimJoint525.HAnimSite.append(HAnimSite530)
HAnimSite533 = x3d.HAnimSite()
HAnimSite533.name = "mesosternale_pt"
HAnimSite533.DEF = "hanim_mesosternale_pt"
HAnimSite533.translation = [0,1,0]
TouchSensor534 = x3d.TouchSensor()
TouchSensor534.description = "HAnimSite mesosternale_pt"

HAnimSite533.children.append(TouchSensor534)
Shape535 = x3d.Shape()
Shape535.USE = "HAnimSiteShape"

HAnimSite533.children.append(Shape535)

HAnimJoint525.HAnimSite.append(HAnimSite533)
HAnimSite536 = x3d.HAnimSite()
HAnimSite536.name = "r_chest_midsagittal_plane_pt"
HAnimSite536.DEF = "hanim_r_chest_midsagittal_plane_pt"
HAnimSite536.translation = [0,1,0]
TouchSensor537 = x3d.TouchSensor()
TouchSensor537.description = "HAnimSite r_chest_midsagittal_plane_pt"

HAnimSite536.children.append(TouchSensor537)
Shape538 = x3d.Shape()
Shape538.USE = "HAnimSiteShape"

HAnimSite536.children.append(Shape538)

HAnimJoint525.HAnimSite.append(HAnimSite536)
HAnimSite539 = x3d.HAnimSite()
HAnimSite539.name = "rear_center_midsagittal_plane_pt"
HAnimSite539.DEF = "hanim_rear_center_midsagittal_plane_pt"
HAnimSite539.translation = [0,1,0]
TouchSensor540 = x3d.TouchSensor()
TouchSensor540.description = "HAnimSite rear_center_midsagittal_plane_pt"

HAnimSite539.children.append(TouchSensor540)
Shape541 = x3d.Shape()
Shape541.USE = "HAnimSiteShape"

HAnimSite539.children.append(Shape541)

HAnimJoint525.HAnimSite.append(HAnimSite539)
HAnimJoint542 = x3d.HAnimJoint()
HAnimJoint542.name = "vt6"
HAnimJoint542.DEF = "hanim_vt6"
HAnimJoint542.center = [0.0059,1.3866,-0.08]
HAnimJoint542.ulimit = [0,0,0]
HAnimJoint542.llimit = [0,0,0]
Shape543 = x3d.Shape()
LineSet544 = x3d.LineSet()
LineSet544.vertexCount = [2]
Coordinate545 = x3d.Coordinate()

LineSet544.coord = Coordinate545
#from vt6 to vt5
ColorRGBA546 = x3d.ColorRGBA()
ColorRGBA546.USE = "HAnimSegmentLineColorRGBA"

LineSet544.color = ColorRGBA546

Shape543.geometry = LineSet544

HAnimJoint542.pe.append(Shape543)
HAnimSite547 = x3d.HAnimSite()
HAnimSite547.name = "spine_1_middle_back_pt"
HAnimSite547.DEF = "hanim_spine_1_middle_back_pt"
HAnimSite547.translation = [0,1,0]
TouchSensor548 = x3d.TouchSensor()
TouchSensor548.description = "HAnimSite spine_1_middle_back_pt"

HAnimSite547.children.append(TouchSensor548)
Shape549 = x3d.Shape()
Shape549.USE = "HAnimSiteShape"

HAnimSite547.children.append(Shape549)

HAnimJoint542.HAnimSite.append(HAnimSite547)
HAnimJoint550 = x3d.HAnimJoint()
HAnimJoint550.name = "vt5"
HAnimJoint550.DEF = "hanim_vt5"
HAnimJoint550.center = [0.006,1.4102,-0.0745]
HAnimJoint550.ulimit = [0,0,0]
HAnimJoint550.llimit = [0,0,0]
Shape551 = x3d.Shape()
LineSet552 = x3d.LineSet()
LineSet552.vertexCount = [2]
Coordinate553 = x3d.Coordinate()

LineSet552.coord = Coordinate553
#from vt5 to vt4
ColorRGBA554 = x3d.ColorRGBA()
ColorRGBA554.USE = "HAnimSegmentLineColorRGBA"

LineSet552.color = ColorRGBA554

Shape551.geometry = LineSet552

HAnimJoint550.pe.append(Shape551)
HAnimJoint555 = x3d.HAnimJoint()
HAnimJoint555.name = "vt4"
HAnimJoint555.DEF = "hanim_vt4"
HAnimJoint555.center = [0.0061,1.432,-0.0675]
HAnimJoint555.ulimit = [0,0,0]
HAnimJoint555.llimit = [0,0,0]
Shape556 = x3d.Shape()
LineSet557 = x3d.LineSet()
LineSet557.vertexCount = [2]
Coordinate558 = x3d.Coordinate()

LineSet557.coord = Coordinate558
#from vt4 to vt3
ColorRGBA559 = x3d.ColorRGBA()
ColorRGBA559.USE = "HAnimSegmentLineColorRGBA"

LineSet557.color = ColorRGBA559

Shape556.geometry = LineSet557

HAnimJoint555.pe.append(Shape556)
HAnimJoint560 = x3d.HAnimJoint()
HAnimJoint560.name = "vt3"
HAnimJoint560.DEF = "hanim_vt3"
HAnimJoint560.center = [0.0062,1.4583,-0.057]
HAnimJoint560.ulimit = [0,0,0]
HAnimJoint560.llimit = [0,0,0]
Shape561 = x3d.Shape()
LineSet562 = x3d.LineSet()
LineSet562.vertexCount = [2]
Coordinate563 = x3d.Coordinate()

LineSet562.coord = Coordinate563
#from vt3 to vt2
ColorRGBA564 = x3d.ColorRGBA()
ColorRGBA564.USE = "HAnimSegmentLineColorRGBA"

LineSet562.color = ColorRGBA564

Shape561.geometry = LineSet562

HAnimJoint560.pe.append(Shape561)
HAnimJoint565 = x3d.HAnimJoint()
HAnimJoint565.name = "vt2"
HAnimJoint565.DEF = "hanim_vt2"
HAnimJoint565.center = [0.0063,1.4761,-0.0484]
HAnimJoint565.ulimit = [0,0,0]
HAnimJoint565.llimit = [0,0,0]
Shape566 = x3d.Shape()
LineSet567 = x3d.LineSet()
LineSet567.vertexCount = [2]
Coordinate568 = x3d.Coordinate()

LineSet567.coord = Coordinate568
#from vt2 to vt1
ColorRGBA569 = x3d.ColorRGBA()
ColorRGBA569.USE = "HAnimSegmentLineColorRGBA"

LineSet567.color = ColorRGBA569

Shape566.geometry = LineSet567

HAnimJoint565.pe.append(Shape566)
HAnimSite570 = x3d.HAnimSite()
HAnimSite570.name = "cervicale_pt"
HAnimSite570.DEF = "hanim_cervicale_pt"
HAnimSite570.translation = [0.0064,1.52,-0.0815]
TouchSensor571 = x3d.TouchSensor()
TouchSensor571.description = "HAnimSite cervicale_pt"

HAnimSite570.children.append(TouchSensor571)
Shape572 = x3d.Shape()
Shape572.USE = "HAnimSiteShape"

HAnimSite570.children.append(Shape572)

HAnimJoint565.HAnimSite.append(HAnimSite570)
HAnimSite573 = x3d.HAnimSite()
HAnimSite573.name = "suprasternale_pt"
HAnimSite573.DEF = "hanim_suprasternale_pt"
HAnimSite573.translation = [0.0084,1.4714,0.0551]
TouchSensor574 = x3d.TouchSensor()
TouchSensor574.description = "HAnimSite suprasternale_pt"

HAnimSite573.children.append(TouchSensor574)
Shape575 = x3d.Shape()
Shape575.USE = "HAnimSiteShape"

HAnimSite573.children.append(Shape575)

HAnimJoint565.HAnimSite.append(HAnimSite573)
HAnimJoint576 = x3d.HAnimJoint()
HAnimJoint576.name = "vt1"
HAnimJoint576.DEF = "hanim_vt1"
HAnimJoint576.center = [0.0065,1.4951,-0.0387]
HAnimJoint576.ulimit = [0,0,0]
HAnimJoint576.llimit = [0,0,0]
Shape577 = x3d.Shape()
LineSet578 = x3d.LineSet()
LineSet578.vertexCount = [2]
Coordinate579 = x3d.Coordinate()

LineSet578.coord = Coordinate579
#from vt1 to vc7
ColorRGBA580 = x3d.ColorRGBA()
ColorRGBA580.USE = "HAnimSegmentLineColorRGBA"

LineSet578.color = ColorRGBA580

Shape577.geometry = LineSet578

HAnimJoint576.pe.append(Shape577)
HAnimSite581 = x3d.HAnimSite()
HAnimSite581.name = "l_neck_base_pt"
HAnimSite581.DEF = "hanim_l_neck_base_pt"
HAnimSite581.translation = [0.0646,1.5141,-0.038]
TouchSensor582 = x3d.TouchSensor()
TouchSensor582.description = "HAnimSite l_neck_base_pt"

HAnimSite581.children.append(TouchSensor582)
Shape583 = x3d.Shape()
Shape583.USE = "HAnimSiteShape"

HAnimSite581.children.append(Shape583)

HAnimJoint576.HAnimSite.append(HAnimSite581)
HAnimSite584 = x3d.HAnimSite()
HAnimSite584.name = "r_neck_base_pt"
HAnimSite584.DEF = "hanim_r_neck_base_pt"
HAnimSite584.translation = [-0.0419,1.5149,-0.022]
TouchSensor585 = x3d.TouchSensor()
TouchSensor585.description = "HAnimSite r_neck_base_pt"

HAnimSite584.children.append(TouchSensor585)
Shape586 = x3d.Shape()
Shape586.USE = "HAnimSiteShape"

HAnimSite584.children.append(Shape586)

HAnimJoint576.HAnimSite.append(HAnimSite584)
Shape587 = x3d.Shape()
LineSet588 = x3d.LineSet()
LineSet588.vertexCount = [2]
Coordinate589 = x3d.Coordinate()

LineSet588.coord = Coordinate589
#from vt1 to l_sternoclavicular
ColorRGBA590 = x3d.ColorRGBA()
ColorRGBA590.USE = "HAnimSegmentLineColorRGBA"

LineSet588.color = ColorRGBA590

Shape587.geometry = LineSet588

HAnimJoint576.pe.append(Shape587)
HAnimSite591 = x3d.HAnimSite()
HAnimSite591.name = "l_acromion_pt"
HAnimSite591.DEF = "hanim_l_acromion_pt"
HAnimSite591.translation = [0.2032,1.476,-0.049]
TouchSensor592 = x3d.TouchSensor()
TouchSensor592.description = "HAnimSite l_acromion_pt"

HAnimSite591.children.append(TouchSensor592)
Shape593 = x3d.Shape()
Shape593.USE = "HAnimSiteShape"

HAnimSite591.children.append(Shape593)

HAnimJoint576.HAnimSite.append(HAnimSite591)
HAnimSite594 = x3d.HAnimSite()
HAnimSite594.name = "l_axilla_distal_pt"
HAnimSite594.DEF = "hanim_l_axilla_distal_pt"
HAnimSite594.translation = [0.1706,1.4072,-0.0875]
TouchSensor595 = x3d.TouchSensor()
TouchSensor595.description = "HAnimSite l_axilla_distal_pt"

HAnimSite594.children.append(TouchSensor595)
Shape596 = x3d.Shape()
Shape596.USE = "HAnimSiteShape"

HAnimSite594.children.append(Shape596)

HAnimJoint576.HAnimSite.append(HAnimSite594)
HAnimSite597 = x3d.HAnimSite()
HAnimSite597.name = "l_axilla_posterior_folds_pt"
HAnimSite597.DEF = "hanim_l_axilla_posterior_folds_pt"
HAnimSite597.translation = [0,1,0]
TouchSensor598 = x3d.TouchSensor()
TouchSensor598.description = "HAnimSite l_axilla_posterior_folds_pt"

HAnimSite597.children.append(TouchSensor598)
Shape599 = x3d.Shape()
Shape599.USE = "HAnimSiteShape"

HAnimSite597.children.append(Shape599)

HAnimJoint576.HAnimSite.append(HAnimSite597)
HAnimSite600 = x3d.HAnimSite()
HAnimSite600.name = "l_axilla_proximal_pt"
HAnimSite600.DEF = "hanim_l_axilla_proximal_pt"
HAnimSite600.translation = [0.1777,1.4065,-0.0075]
TouchSensor601 = x3d.TouchSensor()
TouchSensor601.description = "HAnimSite l_axilla_proximal_pt"

HAnimSite600.children.append(TouchSensor601)
Shape602 = x3d.Shape()
Shape602.USE = "HAnimSiteShape"

HAnimSite600.children.append(Shape602)

HAnimJoint576.HAnimSite.append(HAnimSite600)
HAnimSite603 = x3d.HAnimSite()
HAnimSite603.name = "l_clavicale_pt"
HAnimSite603.DEF = "hanim_l_clavicale_pt"
HAnimSite603.translation = [0.0271,1.4943,0.0394]
TouchSensor604 = x3d.TouchSensor()
TouchSensor604.description = "HAnimSite l_clavicale_pt"

HAnimSite603.children.append(TouchSensor604)
Shape605 = x3d.Shape()
Shape605.USE = "HAnimSiteShape"

HAnimSite603.children.append(Shape605)

HAnimJoint576.HAnimSite.append(HAnimSite603)
Shape606 = x3d.Shape()
LineSet607 = x3d.LineSet()
LineSet607.vertexCount = [2]
Coordinate608 = x3d.Coordinate()

LineSet607.coord = Coordinate608
#from vt1 to r_sternoclavicular
ColorRGBA609 = x3d.ColorRGBA()
ColorRGBA609.USE = "HAnimSegmentLineColorRGBA"

LineSet607.color = ColorRGBA609

Shape606.geometry = LineSet607

HAnimJoint576.pe.append(Shape606)
HAnimSite610 = x3d.HAnimSite()
HAnimSite610.name = "r_acromion_pt"
HAnimSite610.DEF = "hanim_r_acromion_pt"
HAnimSite610.translation = [-0.1905,1.4791,-0.0431]
TouchSensor611 = x3d.TouchSensor()
TouchSensor611.description = "HAnimSite r_acromion_pt"

HAnimSite610.children.append(TouchSensor611)
Shape612 = x3d.Shape()
Shape612.USE = "HAnimSiteShape"

HAnimSite610.children.append(Shape612)

HAnimJoint576.HAnimSite.append(HAnimSite610)
HAnimSite613 = x3d.HAnimSite()
HAnimSite613.name = "r_axilla_distal_pt"
HAnimSite613.DEF = "hanim_r_axilla_distal_pt"
HAnimSite613.translation = [-0.1603,1.4098,-0.0826]
TouchSensor614 = x3d.TouchSensor()
TouchSensor614.description = "HAnimSite r_axilla_distal_pt"

HAnimSite613.children.append(TouchSensor614)
Shape615 = x3d.Shape()
Shape615.USE = "HAnimSiteShape"

HAnimSite613.children.append(Shape615)

HAnimJoint576.HAnimSite.append(HAnimSite613)
HAnimSite616 = x3d.HAnimSite()
HAnimSite616.name = "r_axilla_posterior_folds_pt"
HAnimSite616.DEF = "hanim_r_axilla_posterior_folds_pt"
HAnimSite616.translation = [0,1,0]
TouchSensor617 = x3d.TouchSensor()
TouchSensor617.description = "HAnimSite r_axilla_posterior_folds_pt"

HAnimSite616.children.append(TouchSensor617)
Shape618 = x3d.Shape()
Shape618.USE = "HAnimSiteShape"

HAnimSite616.children.append(Shape618)

HAnimJoint576.HAnimSite.append(HAnimSite616)
HAnimSite619 = x3d.HAnimSite()
HAnimSite619.name = "r_axilla_proximal_pt"
HAnimSite619.DEF = "hanim_r_axilla_proximal_pt"
HAnimSite619.translation = [-0.1626,1.4072,-0.0031]
TouchSensor620 = x3d.TouchSensor()
TouchSensor620.description = "HAnimSite r_axilla_proximal_pt"

HAnimSite619.children.append(TouchSensor620)
Shape621 = x3d.Shape()
Shape621.USE = "HAnimSiteShape"

HAnimSite619.children.append(Shape621)

HAnimJoint576.HAnimSite.append(HAnimSite619)
HAnimSite622 = x3d.HAnimSite()
HAnimSite622.name = "r_clavicale_pt"
HAnimSite622.DEF = "hanim_r_clavicale_pt"
HAnimSite622.translation = [-0.0115,1.4943,0.04]
TouchSensor623 = x3d.TouchSensor()
TouchSensor623.description = "HAnimSite r_clavicale_pt"

HAnimSite622.children.append(TouchSensor623)
Shape624 = x3d.Shape()
Shape624.USE = "HAnimSiteShape"

HAnimSite622.children.append(Shape624)

HAnimJoint576.HAnimSite.append(HAnimSite622)
HAnimJoint625 = x3d.HAnimJoint()
HAnimJoint625.name = "vc7"
HAnimJoint625.DEF = "hanim_vc7"
HAnimJoint625.center = [0.0066,1.5132,-0.0301]
HAnimJoint625.ulimit = [0,0,0]
HAnimJoint625.llimit = [0,0,0]
Shape626 = x3d.Shape()
LineSet627 = x3d.LineSet()
LineSet627.vertexCount = [2]
Coordinate628 = x3d.Coordinate()

LineSet627.coord = Coordinate628
#from vc7 to vc6
ColorRGBA629 = x3d.ColorRGBA()
ColorRGBA629.USE = "HAnimSegmentLineColorRGBA"

LineSet627.color = ColorRGBA629

Shape626.geometry = LineSet627

HAnimJoint625.pe.append(Shape626)
HAnimJoint630 = x3d.HAnimJoint()
HAnimJoint630.name = "vc6"
HAnimJoint630.DEF = "hanim_vc6"
HAnimJoint630.center = [0.0066,1.5357,-0.0143]
HAnimJoint630.ulimit = [0,0,0]
HAnimJoint630.llimit = [0,0,0]
Shape631 = x3d.Shape()
LineSet632 = x3d.LineSet()
LineSet632.vertexCount = [2]
Coordinate633 = x3d.Coordinate()

LineSet632.coord = Coordinate633
#from vc6 to vc5
ColorRGBA634 = x3d.ColorRGBA()
ColorRGBA634.USE = "HAnimSegmentLineColorRGBA"

LineSet632.color = ColorRGBA634

Shape631.geometry = LineSet632

HAnimJoint630.pe.append(Shape631)
HAnimJoint635 = x3d.HAnimJoint()
HAnimJoint635.name = "vc5"
HAnimJoint635.DEF = "hanim_vc5"
HAnimJoint635.center = [0.0066,1.552,-0.0082]
HAnimJoint635.ulimit = [0,0,0]
HAnimJoint635.llimit = [0,0,0]
Shape636 = x3d.Shape()
LineSet637 = x3d.LineSet()
LineSet637.vertexCount = [2]
Coordinate638 = x3d.Coordinate()

LineSet637.coord = Coordinate638
#from vc5 to vc4
ColorRGBA639 = x3d.ColorRGBA()
ColorRGBA639.USE = "HAnimSegmentLineColorRGBA"

LineSet637.color = ColorRGBA639

Shape636.geometry = LineSet637

HAnimJoint635.pe.append(Shape636)
HAnimJoint640 = x3d.HAnimJoint()
HAnimJoint640.name = "vc4"
HAnimJoint640.DEF = "hanim_vc4"
HAnimJoint640.center = [0.0066,1.5662,-0.0084]
HAnimJoint640.ulimit = [0,0,0]
HAnimJoint640.llimit = [0,0,0]
Shape641 = x3d.Shape()
LineSet642 = x3d.LineSet()
LineSet642.vertexCount = [2]
Coordinate643 = x3d.Coordinate()

LineSet642.coord = Coordinate643
#from vc4 to vc3
ColorRGBA644 = x3d.ColorRGBA()
ColorRGBA644.USE = "HAnimSegmentLineColorRGBA"

LineSet642.color = ColorRGBA644

Shape641.geometry = LineSet642

HAnimJoint640.pe.append(Shape641)
HAnimJoint645 = x3d.HAnimJoint()
HAnimJoint645.name = "vc3"
HAnimJoint645.DEF = "hanim_vc3"
HAnimJoint645.center = [0.0066,1.58,-0.0103]
HAnimJoint645.ulimit = [0,0,0]
HAnimJoint645.llimit = [0,0,0]
Shape646 = x3d.Shape()
LineSet647 = x3d.LineSet()
LineSet647.vertexCount = [2]
Coordinate648 = x3d.Coordinate()

LineSet647.coord = Coordinate648
#from vc3 to vc2
ColorRGBA649 = x3d.ColorRGBA()
ColorRGBA649.USE = "HAnimSegmentLineColorRGBA"

LineSet647.color = ColorRGBA649

Shape646.geometry = LineSet647

HAnimJoint645.pe.append(Shape646)
HAnimSite650 = x3d.HAnimSite()
HAnimSite650.name = "adams_apple_pt"
HAnimSite650.DEF = "hanim_adams_apple_pt"
HAnimSite650.translation = [0,1,0]
TouchSensor651 = x3d.TouchSensor()
TouchSensor651.description = "HAnimSite adams_apple_pt"

HAnimSite650.children.append(TouchSensor651)
Shape652 = x3d.Shape()
Shape652.USE = "HAnimSiteShape"

HAnimSite650.children.append(Shape652)

HAnimJoint645.HAnimSite.append(HAnimSite650)
HAnimJoint653 = x3d.HAnimJoint()
HAnimJoint653.name = "vc2"
HAnimJoint653.DEF = "hanim_vc2"
HAnimJoint653.center = [0.0066,1.5928,-0.0103]
HAnimJoint653.ulimit = [0,0,0]
HAnimJoint653.llimit = [0,0,0]
Shape654 = x3d.Shape()
LineSet655 = x3d.LineSet()
LineSet655.vertexCount = [2]
Coordinate656 = x3d.Coordinate()

LineSet655.coord = Coordinate656
#from vc2 to vc1
ColorRGBA657 = x3d.ColorRGBA()
ColorRGBA657.USE = "HAnimSegmentLineColorRGBA"

LineSet655.color = ColorRGBA657

Shape654.geometry = LineSet655

HAnimJoint653.pe.append(Shape654)
HAnimJoint658 = x3d.HAnimJoint()
HAnimJoint658.name = "vc1"
HAnimJoint658.DEF = "hanim_vc1"
HAnimJoint658.center = [0.0066,1.6144,-0.0034]
HAnimJoint658.ulimit = [0,0,0]
HAnimJoint658.llimit = [0,0,0]
Shape659 = x3d.Shape()
LineSet660 = x3d.LineSet()
LineSet660.vertexCount = [2]
Coordinate661 = x3d.Coordinate()

LineSet660.coord = Coordinate661
#from vc1 to skullbase
ColorRGBA662 = x3d.ColorRGBA()
ColorRGBA662.USE = "HAnimSegmentLineColorRGBA"

LineSet660.color = ColorRGBA662

Shape659.geometry = LineSet660

HAnimJoint658.pe.append(Shape659)
HAnimSite663 = x3d.HAnimSite()
HAnimSite663.name = "glabella_pt"
HAnimSite663.DEF = "hanim_glabella_pt"
HAnimSite663.translation = [0,1,0]
TouchSensor664 = x3d.TouchSensor()
TouchSensor664.description = "HAnimSite glabella_pt"

HAnimSite663.children.append(TouchSensor664)
Shape665 = x3d.Shape()
Shape665.USE = "HAnimSiteShape"

HAnimSite663.children.append(Shape665)

HAnimJoint658.HAnimSite.append(HAnimSite663)
HAnimSite666 = x3d.HAnimSite()
HAnimSite666.name = "l_ectocanthus_pt"
HAnimSite666.DEF = "hanim_l_ectocanthus_pt"
HAnimSite666.translation = [0,1,0]
TouchSensor667 = x3d.TouchSensor()
TouchSensor667.description = "HAnimSite l_ectocanthus_pt"

HAnimSite666.children.append(TouchSensor667)
Shape668 = x3d.Shape()
Shape668.USE = "HAnimSiteShape"

HAnimSite666.children.append(Shape668)

HAnimJoint658.HAnimSite.append(HAnimSite666)
HAnimSite669 = x3d.HAnimSite()
HAnimSite669.name = "l_infraorbitale_pt"
HAnimSite669.DEF = "hanim_l_infraorbitale_pt"
HAnimSite669.translation = [0.0341,1.6171,0.0752]
TouchSensor670 = x3d.TouchSensor()
TouchSensor670.description = "HAnimSite l_infraorbitale_pt"

HAnimSite669.children.append(TouchSensor670)
Shape671 = x3d.Shape()
Shape671.USE = "HAnimSiteShape"

HAnimSite669.children.append(Shape671)

HAnimJoint658.HAnimSite.append(HAnimSite669)
HAnimSite672 = x3d.HAnimSite()
HAnimSite672.name = "l_tragion_pt"
HAnimSite672.DEF = "hanim_l_tragion_pt"
HAnimSite672.translation = [0.0739,1.6348,0.0282]
TouchSensor673 = x3d.TouchSensor()
TouchSensor673.description = "HAnimSite l_tragion_pt"

HAnimSite672.children.append(TouchSensor673)
Shape674 = x3d.Shape()
Shape674.USE = "HAnimSiteShape"

HAnimSite672.children.append(Shape674)

HAnimJoint658.HAnimSite.append(HAnimSite672)
HAnimSite675 = x3d.HAnimSite()
HAnimSite675.name = "nuchale_pt"
HAnimSite675.DEF = "hanim_nuchale_pt"
HAnimSite675.translation = [0.0039,1.5972,-0.0796]
TouchSensor676 = x3d.TouchSensor()
TouchSensor676.description = "HAnimSite nuchale_pt"

HAnimSite675.children.append(TouchSensor676)
Shape677 = x3d.Shape()
Shape677.USE = "HAnimSiteShape"

HAnimSite675.children.append(Shape677)

HAnimJoint658.HAnimSite.append(HAnimSite675)
HAnimSite678 = x3d.HAnimSite()
HAnimSite678.name = "opisthocranion_pt"
HAnimSite678.DEF = "hanim_opisthocranion_pt"
HAnimSite678.translation = [0,1,0]
TouchSensor679 = x3d.TouchSensor()
TouchSensor679.description = "HAnimSite opisthocranion_pt"

HAnimSite678.children.append(TouchSensor679)
Shape680 = x3d.Shape()
Shape680.USE = "HAnimSiteShape"

HAnimSite678.children.append(Shape680)

HAnimJoint658.HAnimSite.append(HAnimSite678)
HAnimSite681 = x3d.HAnimSite()
HAnimSite681.name = "r_ectocanthus_pt"
HAnimSite681.DEF = "hanim_r_ectocanthus_pt"
HAnimSite681.translation = [0,1,0]
TouchSensor682 = x3d.TouchSensor()
TouchSensor682.description = "HAnimSite r_ectocanthus_pt"

HAnimSite681.children.append(TouchSensor682)
Shape683 = x3d.Shape()
Shape683.USE = "HAnimSiteShape"

HAnimSite681.children.append(Shape683)

HAnimJoint658.HAnimSite.append(HAnimSite681)
HAnimSite684 = x3d.HAnimSite()
HAnimSite684.name = "r_infraorbitale_pt"
HAnimSite684.DEF = "hanim_r_infraorbitale_pt"
HAnimSite684.translation = [-0.0237,1.6171,0.0752]
TouchSensor685 = x3d.TouchSensor()
TouchSensor685.description = "HAnimSite r_infraorbitale_pt"

HAnimSite684.children.append(TouchSensor685)
Shape686 = x3d.Shape()
Shape686.USE = "HAnimSiteShape"

HAnimSite684.children.append(Shape686)

HAnimJoint658.HAnimSite.append(HAnimSite684)
HAnimSite687 = x3d.HAnimSite()
HAnimSite687.name = "r_tragion_pt"
HAnimSite687.DEF = "hanim_r_tragion_pt"
HAnimSite687.translation = [-0.0646,1.6347,0.0302]
TouchSensor688 = x3d.TouchSensor()
TouchSensor688.description = "HAnimSite r_tragion_pt"

HAnimSite687.children.append(TouchSensor688)
Shape689 = x3d.Shape()
Shape689.USE = "HAnimSiteShape"

HAnimSite687.children.append(Shape689)

HAnimJoint658.HAnimSite.append(HAnimSite687)
HAnimSite690 = x3d.HAnimSite()
HAnimSite690.name = "sellion_pt"
HAnimSite690.DEF = "hanim_sellion_pt"
HAnimSite690.translation = [0.0058,1.6316,0.0852]
TouchSensor691 = x3d.TouchSensor()
TouchSensor691.description = "HAnimSite sellion_pt"

HAnimSite690.children.append(TouchSensor691)
Shape692 = x3d.Shape()
Shape692.USE = "HAnimSiteShape"

HAnimSite690.children.append(Shape692)

HAnimJoint658.HAnimSite.append(HAnimSite690)
HAnimSite693 = x3d.HAnimSite()
HAnimSite693.name = "skull_vertex_pt"
HAnimSite693.DEF = "hanim_skull_vertex_pt"
HAnimSite693.translation = [0.005,1.7504,0.0055]
TouchSensor694 = x3d.TouchSensor()
TouchSensor694.description = "HAnimSite skull_vertex_pt"

HAnimSite693.children.append(TouchSensor694)
Shape695 = x3d.Shape()
Shape695.USE = "HAnimSiteShape"

HAnimSite693.children.append(Shape695)

HAnimJoint658.HAnimSite.append(HAnimSite693)
HAnimJoint696 = x3d.HAnimJoint()
HAnimJoint696.name = "skullbase"
HAnimJoint696.DEF = "hanim_skullbase"
HAnimJoint696.center = [0.0044,1.6209,0.0236]
HAnimJoint696.ulimit = [0,0,0]
HAnimJoint696.llimit = [0,0,0]
Shape697 = x3d.Shape()
LineSet698 = x3d.LineSet()
LineSet698.vertexCount = [2]
Coordinate699 = x3d.Coordinate()

LineSet698.coord = Coordinate699
#from skullbase to l_eyelid_joint
ColorRGBA700 = x3d.ColorRGBA()
ColorRGBA700.USE = "HAnimSegmentLineColorRGBA"

LineSet698.color = ColorRGBA700

Shape697.geometry = LineSet698

HAnimJoint696.pe.append(Shape697)
Shape701 = x3d.Shape()
LineSet702 = x3d.LineSet()
LineSet702.vertexCount = [2]
Coordinate703 = x3d.Coordinate()

LineSet702.coord = Coordinate703
#from skullbase to r_eyelid_joint
ColorRGBA704 = x3d.ColorRGBA()
ColorRGBA704.USE = "HAnimSegmentLineColorRGBA"

LineSet702.color = ColorRGBA704

Shape701.geometry = LineSet702

HAnimJoint696.pe.append(Shape701)
Shape705 = x3d.Shape()
LineSet706 = x3d.LineSet()
LineSet706.vertexCount = [2]
Coordinate707 = x3d.Coordinate()

LineSet706.coord = Coordinate707
#from skullbase to l_eyeball_joint
ColorRGBA708 = x3d.ColorRGBA()
ColorRGBA708.USE = "HAnimSegmentLineColorRGBA"

LineSet706.color = ColorRGBA708

Shape705.geometry = LineSet706

HAnimJoint696.pe.append(Shape705)
Shape709 = x3d.Shape()
LineSet710 = x3d.LineSet()
LineSet710.vertexCount = [2]
Coordinate711 = x3d.Coordinate()

LineSet710.coord = Coordinate711
#from skullbase to r_eyeball_joint
ColorRGBA712 = x3d.ColorRGBA()
ColorRGBA712.USE = "HAnimSegmentLineColorRGBA"

LineSet710.color = ColorRGBA712

Shape709.geometry = LineSet710

HAnimJoint696.pe.append(Shape709)
Shape713 = x3d.Shape()
LineSet714 = x3d.LineSet()
LineSet714.vertexCount = [2]
Coordinate715 = x3d.Coordinate()

LineSet714.coord = Coordinate715
#from skullbase to l_eyebrow_joint
ColorRGBA716 = x3d.ColorRGBA()
ColorRGBA716.USE = "HAnimSegmentLineColorRGBA"

LineSet714.color = ColorRGBA716

Shape713.geometry = LineSet714

HAnimJoint696.pe.append(Shape713)
Shape717 = x3d.Shape()
LineSet718 = x3d.LineSet()
LineSet718.vertexCount = [2]
Coordinate719 = x3d.Coordinate()

LineSet718.coord = Coordinate719
#from skullbase to r_eyebrow_joint
ColorRGBA720 = x3d.ColorRGBA()
ColorRGBA720.USE = "HAnimSegmentLineColorRGBA"

LineSet718.color = ColorRGBA720

Shape717.geometry = LineSet718

HAnimJoint696.pe.append(Shape717)
Shape721 = x3d.Shape()
LineSet722 = x3d.LineSet()
LineSet722.vertexCount = [2]
Coordinate723 = x3d.Coordinate()

LineSet722.coord = Coordinate723
#from skullbase to temporomandibular
ColorRGBA724 = x3d.ColorRGBA()
ColorRGBA724.USE = "HAnimSegmentLineColorRGBA"

LineSet722.color = ColorRGBA724

Shape721.geometry = LineSet722

HAnimJoint696.pe.append(Shape721)
HAnimSite725 = x3d.HAnimSite()
HAnimSite725.name = "l_gonion_pt"
HAnimSite725.DEF = "hanim_l_gonion_pt"
HAnimSite725.translation = [0.0631,1.553,0.033]
TouchSensor726 = x3d.TouchSensor()
TouchSensor726.description = "HAnimSite l_gonion_pt"

HAnimSite725.children.append(TouchSensor726)
Shape727 = x3d.Shape()
Shape727.USE = "HAnimSiteShape"

HAnimSite725.children.append(Shape727)

HAnimJoint696.HAnimSite.append(HAnimSite725)
HAnimSite728 = x3d.HAnimSite()
HAnimSite728.name = "menton_pt"
HAnimSite728.DEF = "hanim_menton_pt"
HAnimSite728.translation = [0,1,0]
TouchSensor729 = x3d.TouchSensor()
TouchSensor729.description = "HAnimSite menton_pt"

HAnimSite728.children.append(TouchSensor729)
Shape730 = x3d.Shape()
Shape730.USE = "HAnimSiteShape"

HAnimSite728.children.append(Shape730)

HAnimJoint696.HAnimSite.append(HAnimSite728)
HAnimSite731 = x3d.HAnimSite()
HAnimSite731.name = "r_gonion_pt"
HAnimSite731.DEF = "hanim_r_gonion_pt"
HAnimSite731.translation = [-0.052,1.5529,0.0347]
TouchSensor732 = x3d.TouchSensor()
TouchSensor732.description = "HAnimSite r_gonion_pt"

HAnimSite731.children.append(TouchSensor732)
Shape733 = x3d.Shape()
Shape733.USE = "HAnimSiteShape"

HAnimSite731.children.append(Shape733)

HAnimJoint696.HAnimSite.append(HAnimSite731)
HAnimSite734 = x3d.HAnimSite()
HAnimSite734.name = "supramenton_pt"
HAnimSite734.DEF = "hanim_supramenton_pt"
HAnimSite734.translation = [0.0061,1.541,0.0805]
TouchSensor735 = x3d.TouchSensor()
TouchSensor735.description = "HAnimSite supramenton_pt"

HAnimSite734.children.append(TouchSensor735)
Shape736 = x3d.Shape()
Shape736.USE = "HAnimSiteShape"

HAnimSite734.children.append(Shape736)

HAnimJoint696.HAnimSite.append(HAnimSite734)
HAnimJoint737 = x3d.HAnimJoint()
HAnimJoint737.name = "l_eyelid_joint"
HAnimJoint737.DEF = "hanim_l_eyelid_joint"
HAnimJoint737.center = [0,1,0]
HAnimJoint737.ulimit = [0,0,0]
HAnimJoint737.llimit = [0,0,0]

HAnimJoint696.children.append(HAnimJoint737)
HAnimJoint738 = x3d.HAnimJoint()
HAnimJoint738.name = "r_eyelid_joint"
HAnimJoint738.DEF = "hanim_r_eyelid_joint"
HAnimJoint738.center = [0,1,0]
HAnimJoint738.ulimit = [0,0,0]
HAnimJoint738.llimit = [0,0,0]

HAnimJoint696.children.append(HAnimJoint738)
HAnimJoint739 = x3d.HAnimJoint()
HAnimJoint739.name = "l_eyeball_joint"
HAnimJoint739.DEF = "hanim_l_eyeball_joint"
HAnimJoint739.center = [0,1,0]
HAnimJoint739.ulimit = [0,0,0]
HAnimJoint739.llimit = [0,0,0]

HAnimJoint696.children.append(HAnimJoint739)
HAnimJoint740 = x3d.HAnimJoint()
HAnimJoint740.name = "r_eyeball_joint"
HAnimJoint740.DEF = "hanim_r_eyeball_joint"
HAnimJoint740.center = [0,1,0]
HAnimJoint740.ulimit = [0,0,0]
HAnimJoint740.llimit = [0,0,0]

HAnimJoint696.children.append(HAnimJoint740)
HAnimJoint741 = x3d.HAnimJoint()
HAnimJoint741.name = "l_eyebrow_joint"
HAnimJoint741.DEF = "hanim_l_eyebrow_joint"
HAnimJoint741.center = [0,1,0]
HAnimJoint741.ulimit = [0,0,0]
HAnimJoint741.llimit = [0,0,0]

HAnimJoint696.children.append(HAnimJoint741)
HAnimJoint742 = x3d.HAnimJoint()
HAnimJoint742.name = "r_eyebrow_joint"
HAnimJoint742.DEF = "hanim_r_eyebrow_joint"
HAnimJoint742.center = [0,1,0]
HAnimJoint742.ulimit = [0,0,0]
HAnimJoint742.llimit = [0,0,0]

HAnimJoint696.children.append(HAnimJoint742)
HAnimJoint743 = x3d.HAnimJoint()
HAnimJoint743.name = "temporomandibular"
HAnimJoint743.DEF = "hanim_temporomandibular"
HAnimJoint743.center = [0,1,0]
HAnimJoint743.ulimit = [0,0,0]
HAnimJoint743.llimit = [0,0,0]

HAnimJoint696.children.append(HAnimJoint743)

HAnimJoint658.children.append(HAnimJoint696)

HAnimJoint653.children.append(HAnimJoint658)

HAnimJoint645.children.append(HAnimJoint653)

HAnimJoint640.children.append(HAnimJoint645)

HAnimJoint635.children.append(HAnimJoint640)

HAnimJoint630.children.append(HAnimJoint635)

HAnimJoint625.children.append(HAnimJoint630)

HAnimJoint576.children.append(HAnimJoint625)
HAnimJoint744 = x3d.HAnimJoint()
HAnimJoint744.name = "l_sternoclavicular"
HAnimJoint744.DEF = "hanim_l_sternoclavicular"
HAnimJoint744.center = [0.082,1.4488,-0.0353]
HAnimJoint744.ulimit = [0,0,0]
HAnimJoint744.llimit = [0,0,0]
Shape745 = x3d.Shape()
LineSet746 = x3d.LineSet()
LineSet746.vertexCount = [2]
Coordinate747 = x3d.Coordinate()

LineSet746.coord = Coordinate747
#from l_sternoclavicular to l_acromioclavicular
ColorRGBA748 = x3d.ColorRGBA()
ColorRGBA748.USE = "HAnimSegmentLineColorRGBA"

LineSet746.color = ColorRGBA748

Shape745.geometry = LineSet746

HAnimJoint744.pe.append(Shape745)
HAnimJoint749 = x3d.HAnimJoint()
HAnimJoint749.name = "l_acromioclavicular"
HAnimJoint749.DEF = "hanim_l_acromioclavicular"
HAnimJoint749.center = [0.0962,1.4269,-0.0424]
HAnimJoint749.ulimit = [0,0,0]
HAnimJoint749.llimit = [0,0,0]
Shape750 = x3d.Shape()
LineSet751 = x3d.LineSet()
LineSet751.vertexCount = [2]
Coordinate752 = x3d.Coordinate()

LineSet751.coord = Coordinate752
#from l_acromioclavicular to l_shoulder
ColorRGBA753 = x3d.ColorRGBA()
ColorRGBA753.USE = "HAnimSegmentLineColorRGBA"

LineSet751.color = ColorRGBA753

Shape750.geometry = LineSet751

HAnimJoint749.pe.append(Shape750)
HAnimSite754 = x3d.HAnimSite()
HAnimSite754.name = "l_bideltoid_pt"
HAnimSite754.DEF = "hanim_l_bideltoid_pt"
HAnimSite754.translation = [0,1,0]
TouchSensor755 = x3d.TouchSensor()
TouchSensor755.description = "HAnimSite l_bideltoid_pt"

HAnimSite754.children.append(TouchSensor755)
Shape756 = x3d.Shape()
Shape756.USE = "HAnimSiteShape"

HAnimSite754.children.append(Shape756)

HAnimJoint749.HAnimSite.append(HAnimSite754)
HAnimSite757 = x3d.HAnimSite()
HAnimSite757.name = "l_humeral_lateral_epicondyles_pt"
HAnimSite757.DEF = "hanim_l_humeral_lateral_epicondyles_pt"
HAnimSite757.translation = [0.228,1.1482,-0.11]
TouchSensor758 = x3d.TouchSensor()
TouchSensor758.description = "HAnimSite l_humeral_lateral_epicondyles_pt"

HAnimSite757.children.append(TouchSensor758)
Shape759 = x3d.Shape()
Shape759.USE = "HAnimSiteShape"

HAnimSite757.children.append(Shape759)

HAnimJoint749.HAnimSite.append(HAnimSite757)
HAnimJoint760 = x3d.HAnimJoint()
HAnimJoint760.name = "l_shoulder"
HAnimJoint760.DEF = "hanim_l_shoulder"
HAnimJoint760.center = [0.2029,1.4376,-0.0387]
HAnimJoint760.ulimit = [0,0,0]
HAnimJoint760.llimit = [0,0,0]
Shape761 = x3d.Shape()
LineSet762 = x3d.LineSet()
LineSet762.vertexCount = [2]
Coordinate763 = x3d.Coordinate()

LineSet762.coord = Coordinate763
#from l_shoulder to l_elbow
ColorRGBA764 = x3d.ColorRGBA()
ColorRGBA764.USE = "HAnimSegmentLineColorRGBA"

LineSet762.color = ColorRGBA764

Shape761.geometry = LineSet762

HAnimJoint760.pe.append(Shape761)
HAnimSite765 = x3d.HAnimSite()
HAnimSite765.name = "l_humeral_medial_epicondyles_pt"
HAnimSite765.DEF = "hanim_l_humeral_medial_epicondyles_pt"
HAnimSite765.translation = [0.1735,1.1272,-0.1113]
TouchSensor766 = x3d.TouchSensor()
TouchSensor766.description = "HAnimSite l_humeral_medial_epicondyles_pt"

HAnimSite765.children.append(TouchSensor766)
Shape767 = x3d.Shape()
Shape767.USE = "HAnimSiteShape"

HAnimSite765.children.append(Shape767)

HAnimJoint760.HAnimSite.append(HAnimSite765)
HAnimSite768 = x3d.HAnimSite()
HAnimSite768.name = "l_olecranon_pt"
HAnimSite768.DEF = "hanim_l_olecranon_pt"
HAnimSite768.translation = [-0.1962,1.1375,-0.1123]
TouchSensor769 = x3d.TouchSensor()
TouchSensor769.description = "HAnimSite l_olecranon_pt"

HAnimSite768.children.append(TouchSensor769)
Shape770 = x3d.Shape()
Shape770.USE = "HAnimSiteShape"

HAnimSite768.children.append(Shape770)

HAnimJoint760.HAnimSite.append(HAnimSite768)
HAnimSite771 = x3d.HAnimSite()
HAnimSite771.name = "l_radial_styloid_pt"
HAnimSite771.DEF = "hanim_l_radial_styloid_pt"
HAnimSite771.translation = [0.1901,0.8645,-0.0415]
TouchSensor772 = x3d.TouchSensor()
TouchSensor772.description = "HAnimSite l_radial_styloid_pt"

HAnimSite771.children.append(TouchSensor772)
Shape773 = x3d.Shape()
Shape773.USE = "HAnimSiteShape"

HAnimSite771.children.append(Shape773)

HAnimJoint760.HAnimSite.append(HAnimSite771)
HAnimSite774 = x3d.HAnimSite()
HAnimSite774.name = "l_radiale_pt"
HAnimSite774.DEF = "hanim_l_radiale_pt"
HAnimSite774.translation = [0.2182,1.1212,-0.1167]
TouchSensor775 = x3d.TouchSensor()
TouchSensor775.description = "HAnimSite l_radiale_pt"

HAnimSite774.children.append(TouchSensor775)
Shape776 = x3d.Shape()
Shape776.USE = "HAnimSiteShape"

HAnimSite774.children.append(Shape776)

HAnimJoint760.HAnimSite.append(HAnimSite774)
HAnimJoint777 = x3d.HAnimJoint()
HAnimJoint777.name = "l_elbow"
HAnimJoint777.DEF = "hanim_l_elbow"
HAnimJoint777.center = [0.2014,1.1357,-0.0682]
HAnimJoint777.ulimit = [0,0,0]
HAnimJoint777.llimit = [0,0,0]
Shape778 = x3d.Shape()
LineSet779 = x3d.LineSet()
LineSet779.vertexCount = [2]
Coordinate780 = x3d.Coordinate()

LineSet779.coord = Coordinate780
#from l_elbow to l_radiocarpal
ColorRGBA781 = x3d.ColorRGBA()
ColorRGBA781.USE = "HAnimSegmentLineColorRGBA"

LineSet779.color = ColorRGBA781

Shape778.geometry = LineSet779

HAnimJoint777.pe.append(Shape778)
HAnimSite782 = x3d.HAnimSite()
HAnimSite782.name = "l_ulnar_styloid_pt"
HAnimSite782.DEF = "hanim_l_ulnar_styloid_pt"
HAnimSite782.translation = [-0.2142,0.8529,-0.0648]
TouchSensor783 = x3d.TouchSensor()
TouchSensor783.description = "HAnimSite l_ulnar_styloid_pt"

HAnimSite782.children.append(TouchSensor783)
Shape784 = x3d.Shape()
Shape784.USE = "HAnimSiteShape"

HAnimSite782.children.append(Shape784)

HAnimJoint777.HAnimSite.append(HAnimSite782)
HAnimJoint785 = x3d.HAnimJoint()
HAnimJoint785.name = "l_radiocarpal"
HAnimJoint785.DEF = "hanim_l_radiocarpal"
HAnimJoint785.center = [0.1984,0.8663,-0.0583]
HAnimJoint785.ulimit = [0,0,0]
HAnimJoint785.llimit = [0,0,0]
Shape786 = x3d.Shape()
LineSet787 = x3d.LineSet()
LineSet787.vertexCount = [2]
Coordinate788 = x3d.Coordinate()

LineSet787.coord = Coordinate788
#from l_radiocarpal to l_midcarpal_1
ColorRGBA789 = x3d.ColorRGBA()
ColorRGBA789.USE = "HAnimSegmentLineColorRGBA"

LineSet787.color = ColorRGBA789

Shape786.geometry = LineSet787

HAnimJoint785.pe.append(Shape786)
Shape790 = x3d.Shape()
LineSet791 = x3d.LineSet()
LineSet791.vertexCount = [2]
Coordinate792 = x3d.Coordinate()

LineSet791.coord = Coordinate792
#from l_radiocarpal to l_midcarpal_2
ColorRGBA793 = x3d.ColorRGBA()
ColorRGBA793.USE = "HAnimSegmentLineColorRGBA"

LineSet791.color = ColorRGBA793

Shape790.geometry = LineSet791

HAnimJoint785.pe.append(Shape790)
Shape794 = x3d.Shape()
LineSet795 = x3d.LineSet()
LineSet795.vertexCount = [2]
Coordinate796 = x3d.Coordinate()

LineSet795.coord = Coordinate796
#from l_radiocarpal to l_midcarpal_3
ColorRGBA797 = x3d.ColorRGBA()
ColorRGBA797.USE = "HAnimSegmentLineColorRGBA"

LineSet795.color = ColorRGBA797

Shape794.geometry = LineSet795

HAnimJoint785.pe.append(Shape794)
Shape798 = x3d.Shape()
LineSet799 = x3d.LineSet()
LineSet799.vertexCount = [2]
Coordinate800 = x3d.Coordinate()

LineSet799.coord = Coordinate800
#from l_radiocarpal to l_midcarpal_4_5
ColorRGBA801 = x3d.ColorRGBA()
ColorRGBA801.USE = "HAnimSegmentLineColorRGBA"

LineSet799.color = ColorRGBA801

Shape798.geometry = LineSet799

HAnimJoint785.pe.append(Shape798)
HAnimJoint802 = x3d.HAnimJoint()
HAnimJoint802.name = "l_midcarpal_1"
HAnimJoint802.DEF = "hanim_l_midcarpal_1"
HAnimJoint802.center = [0,1,0]
HAnimJoint802.ulimit = [0,0,0]
HAnimJoint802.llimit = [0,0,0]
Shape803 = x3d.Shape()
LineSet804 = x3d.LineSet()
LineSet804.vertexCount = [1]
Coordinate805 = x3d.Coordinate()

LineSet804.coord = Coordinate805
#from l_midcarpal_1 to l_carpometacarpal_1
ColorRGBA806 = x3d.ColorRGBA()
ColorRGBA806.USE = "HAnimSegmentLineColorRGBA"

LineSet804.color = ColorRGBA806

Shape803.geometry = LineSet804

HAnimJoint802.pe.append(Shape803)
HAnimJoint807 = x3d.HAnimJoint()
HAnimJoint807.name = "l_carpometacarpal_1"
HAnimJoint807.DEF = "hanim_l_carpometacarpal_1"
HAnimJoint807.center = [0.1924,0.8472,-0.0534]
HAnimJoint807.ulimit = [0,0,0]
HAnimJoint807.llimit = [0,0,0]
Shape808 = x3d.Shape()
LineSet809 = x3d.LineSet()
LineSet809.vertexCount = [2]
Coordinate810 = x3d.Coordinate()

LineSet809.coord = Coordinate810
#from l_carpometacarpal_1 to l_metacarpophalangeal_1
ColorRGBA811 = x3d.ColorRGBA()
ColorRGBA811.USE = "HAnimSegmentLineColorRGBA"

LineSet809.color = ColorRGBA811

Shape808.geometry = LineSet809

HAnimJoint807.pe.append(Shape808)
HAnimJoint812 = x3d.HAnimJoint()
HAnimJoint812.name = "l_metacarpophalangeal_1"
HAnimJoint812.DEF = "hanim_l_metacarpophalangeal_1"
HAnimJoint812.center = [0.1951,0.8226,0.0246]
HAnimJoint812.ulimit = [0,0,0]
HAnimJoint812.llimit = [0,0,0]
Shape813 = x3d.Shape()
LineSet814 = x3d.LineSet()
LineSet814.vertexCount = [2]
Coordinate815 = x3d.Coordinate()

LineSet814.coord = Coordinate815
#from l_metacarpophalangeal_1 to l_carpal_interphalangeal_1
ColorRGBA816 = x3d.ColorRGBA()
ColorRGBA816.USE = "HAnimSegmentLineColorRGBA"

LineSet814.color = ColorRGBA816

Shape813.geometry = LineSet814

HAnimJoint812.pe.append(Shape813)
HAnimSite817 = x3d.HAnimSite()
HAnimSite817.name = "l_carpal_distal_phalanx_1_tip"
HAnimSite817.DEF = "hanim_l_carpal_distal_phalanx_1_tip"
HAnimSite817.translation = [0,1,0]
TouchSensor818 = x3d.TouchSensor()
TouchSensor818.description = "HAnimSite l_carpal_distal_phalanx_1_tip"

HAnimSite817.children.append(TouchSensor818)
Shape819 = x3d.Shape()
Shape819.USE = "HAnimSiteShape"

HAnimSite817.children.append(Shape819)

HAnimJoint812.HAnimSite.append(HAnimSite817)
HAnimJoint820 = x3d.HAnimJoint()
HAnimJoint820.name = "l_carpal_interphalangeal_1"
HAnimJoint820.DEF = "hanim_l_carpal_interphalangeal_1"
HAnimJoint820.center = [0.1955,0.8159,0.0464]
HAnimJoint820.ulimit = [0,0,0]
HAnimJoint820.llimit = [0,0,0]

HAnimJoint812.children.append(HAnimJoint820)

HAnimJoint807.children.append(HAnimJoint812)

HAnimJoint802.children.append(HAnimJoint807)

HAnimJoint785.children.append(HAnimJoint802)
HAnimJoint821 = x3d.HAnimJoint()
HAnimJoint821.name = "l_midcarpal_2"
HAnimJoint821.DEF = "hanim_l_midcarpal_2"
HAnimJoint821.center = [0,1,0]
HAnimJoint821.ulimit = [0,0,0]
HAnimJoint821.llimit = [0,0,0]
Shape822 = x3d.Shape()
LineSet823 = x3d.LineSet()
LineSet823.vertexCount = [1]
Coordinate824 = x3d.Coordinate()

LineSet823.coord = Coordinate824
#from l_midcarpal_2 to l_carpometacarpal_2
ColorRGBA825 = x3d.ColorRGBA()
ColorRGBA825.USE = "HAnimSegmentLineColorRGBA"

LineSet823.color = ColorRGBA825

Shape822.geometry = LineSet823

HAnimJoint821.pe.append(Shape822)
HAnimSite826 = x3d.HAnimSite()
HAnimSite826.name = "l_metacarpal_phalanx_2_pt"
HAnimSite826.DEF = "hanim_l_metacarpal_phalanx_2_pt"
HAnimSite826.translation = [0.2009,0.8139,-0.0237]
TouchSensor827 = x3d.TouchSensor()
TouchSensor827.description = "HAnimSite l_metacarpal_phalanx_2_pt"

HAnimSite826.children.append(TouchSensor827)
Shape828 = x3d.Shape()
Shape828.USE = "HAnimSiteShape"

HAnimSite826.children.append(Shape828)

HAnimJoint821.HAnimSite.append(HAnimSite826)
HAnimJoint829 = x3d.HAnimJoint()
HAnimJoint829.name = "l_carpometacarpal_2"
HAnimJoint829.DEF = "hanim_l_carpometacarpal_2"
HAnimJoint829.center = [0.1983,0.8024,-0.028]
HAnimJoint829.ulimit = [0,0,0]
HAnimJoint829.llimit = [0,0,0]
Shape830 = x3d.Shape()
LineSet831 = x3d.LineSet()
LineSet831.vertexCount = [2]
Coordinate832 = x3d.Coordinate()

LineSet831.coord = Coordinate832
#from l_carpometacarpal_2 to l_metacarpophalangeal_2
ColorRGBA833 = x3d.ColorRGBA()
ColorRGBA833.USE = "HAnimSegmentLineColorRGBA"

LineSet831.color = ColorRGBA833

Shape830.geometry = LineSet831

HAnimJoint829.pe.append(Shape830)
HAnimJoint834 = x3d.HAnimJoint()
HAnimJoint834.name = "l_metacarpophalangeal_2"
HAnimJoint834.DEF = "hanim_l_metacarpophalangeal_2"
HAnimJoint834.center = [0.1983,0.7815,-0.028]
HAnimJoint834.ulimit = [0,0,0]
HAnimJoint834.llimit = [0,0,0]
Shape835 = x3d.Shape()
LineSet836 = x3d.LineSet()
LineSet836.vertexCount = [2]
Coordinate837 = x3d.Coordinate()

LineSet836.coord = Coordinate837
#from l_metacarpophalangeal_2 to l_carpal_proximal_interphalangeal_2
ColorRGBA838 = x3d.ColorRGBA()
ColorRGBA838.USE = "HAnimSegmentLineColorRGBA"

LineSet836.color = ColorRGBA838

Shape835.geometry = LineSet836

HAnimJoint834.pe.append(Shape835)
HAnimJoint839 = x3d.HAnimJoint()
HAnimJoint839.name = "l_carpal_proximal_interphalangeal_2"
HAnimJoint839.DEF = "hanim_l_carpal_proximal_interphalangeal_2"
HAnimJoint839.center = [0.2017,0.7363,-0.0248]
HAnimJoint839.ulimit = [0,0,0]
HAnimJoint839.llimit = [0,0,0]
Shape840 = x3d.Shape()
LineSet841 = x3d.LineSet()
LineSet841.vertexCount = [2]
Coordinate842 = x3d.Coordinate()

LineSet841.coord = Coordinate842
#from l_carpal_proximal_interphalangeal_2 to l_carpal_distal_interphalangeal_2
ColorRGBA843 = x3d.ColorRGBA()
ColorRGBA843.USE = "HAnimSegmentLineColorRGBA"

LineSet841.color = ColorRGBA843

Shape840.geometry = LineSet841

HAnimJoint839.pe.append(Shape840)
HAnimSite844 = x3d.HAnimSite()
HAnimSite844.name = "l_carpal_distal_phalanx_2_tip"
HAnimSite844.DEF = "hanim_l_carpal_distal_phalanx_2_tip"
HAnimSite844.translation = [0,1,0]
TouchSensor845 = x3d.TouchSensor()
TouchSensor845.description = "HAnimSite l_carpal_distal_phalanx_2_tip"

HAnimSite844.children.append(TouchSensor845)
Shape846 = x3d.Shape()
Shape846.USE = "HAnimSiteShape"

HAnimSite844.children.append(Shape846)

HAnimJoint839.HAnimSite.append(HAnimSite844)
HAnimSite847 = x3d.HAnimSite()
HAnimSite847.name = "l_dactylion_pt"
HAnimSite847.DEF = "hanim_l_dactylion_pt"
HAnimSite847.translation = [0.2056,0.6743,-0.0482]
TouchSensor848 = x3d.TouchSensor()
TouchSensor848.description = "HAnimSite l_dactylion_pt"

HAnimSite847.children.append(TouchSensor848)
Shape849 = x3d.Shape()
Shape849.USE = "HAnimSiteShape"

HAnimSite847.children.append(Shape849)

HAnimJoint839.HAnimSite.append(HAnimSite847)
HAnimJoint850 = x3d.HAnimJoint()
HAnimJoint850.name = "l_carpal_distal_interphalangeal_2"
HAnimJoint850.DEF = "hanim_l_carpal_distal_interphalangeal_2"
HAnimJoint850.center = [0.2028,0.7139,-0.0236]
HAnimJoint850.ulimit = [0,0,0]
HAnimJoint850.llimit = [0,0,0]

HAnimJoint839.children.append(HAnimJoint850)

HAnimJoint834.children.append(HAnimJoint839)

HAnimJoint829.children.append(HAnimJoint834)

HAnimJoint821.children.append(HAnimJoint829)

HAnimJoint785.children.append(HAnimJoint821)
HAnimJoint851 = x3d.HAnimJoint()
HAnimJoint851.name = "l_midcarpal_3"
HAnimJoint851.DEF = "hanim_l_midcarpal_3"
HAnimJoint851.center = [0,1,0]
HAnimJoint851.ulimit = [0,0,0]
HAnimJoint851.llimit = [0,0,0]
Shape852 = x3d.Shape()
LineSet853 = x3d.LineSet()
LineSet853.vertexCount = [1]
Coordinate854 = x3d.Coordinate()

LineSet853.coord = Coordinate854
#from l_midcarpal_3 to l_carpometacarpal_3
ColorRGBA855 = x3d.ColorRGBA()
ColorRGBA855.USE = "HAnimSegmentLineColorRGBA"

LineSet853.color = ColorRGBA855

Shape852.geometry = LineSet853

HAnimJoint851.pe.append(Shape852)
HAnimSite856 = x3d.HAnimSite()
HAnimSite856.name = "l_metacarpal_phalanx_3_pt"
HAnimSite856.DEF = "hanim_l_metacarpal_phalanx_3_pt"
HAnimSite856.translation = [0,1,0]
TouchSensor857 = x3d.TouchSensor()
TouchSensor857.description = "HAnimSite l_metacarpal_phalanx_3_pt"

HAnimSite856.children.append(TouchSensor857)
Shape858 = x3d.Shape()
Shape858.USE = "HAnimSiteShape"

HAnimSite856.children.append(Shape858)

HAnimJoint851.HAnimSite.append(HAnimSite856)
HAnimJoint859 = x3d.HAnimJoint()
HAnimJoint859.name = "l_carpometacarpal_3"
HAnimJoint859.DEF = "hanim_l_carpometacarpal_3"
HAnimJoint859.center = [0.1987,0.8029,-0.053]
HAnimJoint859.ulimit = [0,0,0]
HAnimJoint859.llimit = [0,0,0]
Shape860 = x3d.Shape()
LineSet861 = x3d.LineSet()
LineSet861.vertexCount = [2]
Coordinate862 = x3d.Coordinate()

LineSet861.coord = Coordinate862
#from l_carpometacarpal_3 to l_metacarpophalangeal_3
ColorRGBA863 = x3d.ColorRGBA()
ColorRGBA863.USE = "HAnimSegmentLineColorRGBA"

LineSet861.color = ColorRGBA863

Shape860.geometry = LineSet861

HAnimJoint859.pe.append(Shape860)
HAnimJoint864 = x3d.HAnimJoint()
HAnimJoint864.name = "l_metacarpophalangeal_3"
HAnimJoint864.DEF = "hanim_l_metacarpophalangeal_3"
HAnimJoint864.center = [0.1987,0.7818,-0.053]
HAnimJoint864.ulimit = [0,0,0]
HAnimJoint864.llimit = [0,0,0]
Shape865 = x3d.Shape()
LineSet866 = x3d.LineSet()
LineSet866.vertexCount = [2]
Coordinate867 = x3d.Coordinate()

LineSet866.coord = Coordinate867
#from l_metacarpophalangeal_3 to l_carpal_proximal_interphalangeal_3
ColorRGBA868 = x3d.ColorRGBA()
ColorRGBA868.USE = "HAnimSegmentLineColorRGBA"

LineSet866.color = ColorRGBA868

Shape865.geometry = LineSet866

HAnimJoint864.pe.append(Shape865)
HAnimJoint869 = x3d.HAnimJoint()
HAnimJoint869.name = "l_carpal_proximal_interphalangeal_3"
HAnimJoint869.DEF = "hanim_l_carpal_proximal_interphalangeal_3"
HAnimJoint869.center = [0.2013,0.7273,-0.0503]
HAnimJoint869.ulimit = [0,0,0]
HAnimJoint869.llimit = [0,0,0]
Shape870 = x3d.Shape()
LineSet871 = x3d.LineSet()
LineSet871.vertexCount = [2]
Coordinate872 = x3d.Coordinate()

LineSet871.coord = Coordinate872
#from l_carpal_proximal_interphalangeal_3 to l_carpal_distal_interphalangeal_3
ColorRGBA873 = x3d.ColorRGBA()
ColorRGBA873.USE = "HAnimSegmentLineColorRGBA"

LineSet871.color = ColorRGBA873

Shape870.geometry = LineSet871

HAnimJoint869.pe.append(Shape870)
HAnimSite874 = x3d.HAnimSite()
HAnimSite874.name = "l_carpal_distal_phalanx_3_tip"
HAnimSite874.DEF = "hanim_l_carpal_distal_phalanx_3_tip"
HAnimSite874.translation = [0,1,0]
TouchSensor875 = x3d.TouchSensor()
TouchSensor875.description = "HAnimSite l_carpal_distal_phalanx_3_tip"

HAnimSite874.children.append(TouchSensor875)
Shape876 = x3d.Shape()
Shape876.USE = "HAnimSiteShape"

HAnimSite874.children.append(Shape876)

HAnimJoint869.HAnimSite.append(HAnimSite874)
HAnimJoint877 = x3d.HAnimJoint()
HAnimJoint877.name = "l_carpal_distal_interphalangeal_3"
HAnimJoint877.DEF = "hanim_l_carpal_distal_interphalangeal_3"
HAnimJoint877.center = [0.2026,0.7011,-0.0494]
HAnimJoint877.ulimit = [0,0,0]
HAnimJoint877.llimit = [0,0,0]

HAnimJoint869.children.append(HAnimJoint877)

HAnimJoint864.children.append(HAnimJoint869)

HAnimJoint859.children.append(HAnimJoint864)

HAnimJoint851.children.append(HAnimJoint859)

HAnimJoint785.children.append(HAnimJoint851)
HAnimJoint878 = x3d.HAnimJoint()
HAnimJoint878.name = "l_midcarpal_4_5"
HAnimJoint878.DEF = "hanim_l_midcarpal_4_5"
HAnimJoint878.center = [0,1,0]
HAnimJoint878.ulimit = [0,0,0]
HAnimJoint878.llimit = [0,0,0]
Shape879 = x3d.Shape()
LineSet880 = x3d.LineSet()
LineSet880.vertexCount = [1]
Coordinate881 = x3d.Coordinate()

LineSet880.coord = Coordinate881
#from l_midcarpal_4_5 to l_carpometacarpal_4
ColorRGBA882 = x3d.ColorRGBA()
ColorRGBA882.USE = "HAnimSegmentLineColorRGBA"

LineSet880.color = ColorRGBA882

Shape879.geometry = LineSet880

HAnimJoint878.pe.append(Shape879)
Shape883 = x3d.Shape()
LineSet884 = x3d.LineSet()
LineSet884.vertexCount = [1]
Coordinate885 = x3d.Coordinate()

LineSet884.coord = Coordinate885
#from l_midcarpal_4_5 to l_carpometacarpal_5
ColorRGBA886 = x3d.ColorRGBA()
ColorRGBA886.USE = "HAnimSegmentLineColorRGBA"

LineSet884.color = ColorRGBA886

Shape883.geometry = LineSet884

HAnimJoint878.pe.append(Shape883)
HAnimSite887 = x3d.HAnimSite()
HAnimSite887.name = "l_metacarpal_phalanx_5_pt"
HAnimSite887.DEF = "hanim_l_metacarpal_phalanx_5_pt"
HAnimSite887.translation = [0.1929,0.786,-0.1122]
TouchSensor888 = x3d.TouchSensor()
TouchSensor888.description = "HAnimSite l_metacarpal_phalanx_5_pt"

HAnimSite887.children.append(TouchSensor888)
Shape889 = x3d.Shape()
Shape889.USE = "HAnimSiteShape"

HAnimSite887.children.append(Shape889)

HAnimJoint878.HAnimSite.append(HAnimSite887)
HAnimJoint890 = x3d.HAnimJoint()
HAnimJoint890.name = "l_carpometacarpal_4"
HAnimJoint890.DEF = "hanim_l_carpometacarpal_4"
HAnimJoint890.center = [0.1956,0.8019,-0.0794]
HAnimJoint890.ulimit = [0,0,0]
HAnimJoint890.llimit = [0,0,0]
Shape891 = x3d.Shape()
LineSet892 = x3d.LineSet()
LineSet892.vertexCount = [2]
Coordinate893 = x3d.Coordinate()

LineSet892.coord = Coordinate893
#from l_carpometacarpal_4 to l_metacarpophalangeal_4
ColorRGBA894 = x3d.ColorRGBA()
ColorRGBA894.USE = "HAnimSegmentLineColorRGBA"

LineSet892.color = ColorRGBA894

Shape891.geometry = LineSet892

HAnimJoint890.pe.append(Shape891)
HAnimJoint895 = x3d.HAnimJoint()
HAnimJoint895.name = "l_metacarpophalangeal_4"
HAnimJoint895.DEF = "hanim_l_metacarpophalangeal_4"
HAnimJoint895.center = [0.1956,0.7815,-0.0794]
HAnimJoint895.ulimit = [0,0,0]
HAnimJoint895.llimit = [0,0,0]
Shape896 = x3d.Shape()
LineSet897 = x3d.LineSet()
LineSet897.vertexCount = [2]
Coordinate898 = x3d.Coordinate()

LineSet897.coord = Coordinate898
#from l_metacarpophalangeal_4 to l_carpal_proximal_interphalangeal_4
ColorRGBA899 = x3d.ColorRGBA()
ColorRGBA899.USE = "HAnimSegmentLineColorRGBA"

LineSet897.color = ColorRGBA899

Shape896.geometry = LineSet897

HAnimJoint895.pe.append(Shape896)
HAnimJoint900 = x3d.HAnimJoint()
HAnimJoint900.name = "l_carpal_proximal_interphalangeal_4"
HAnimJoint900.DEF = "hanim_l_carpal_proximal_interphalangeal_4"
HAnimJoint900.center = [0.1973,0.7287,-0.0777]
HAnimJoint900.ulimit = [0,0,0]
HAnimJoint900.llimit = [0,0,0]
Shape901 = x3d.Shape()
LineSet902 = x3d.LineSet()
LineSet902.vertexCount = [2]
Coordinate903 = x3d.Coordinate()

LineSet902.coord = Coordinate903
#from l_carpal_proximal_interphalangeal_4 to l_carpal_distal_interphalangeal_4
ColorRGBA904 = x3d.ColorRGBA()
ColorRGBA904.USE = "HAnimSegmentLineColorRGBA"

LineSet902.color = ColorRGBA904

Shape901.geometry = LineSet902

HAnimJoint900.pe.append(Shape901)
HAnimSite905 = x3d.HAnimSite()
HAnimSite905.name = "l_carpal_distal_phalanx_4_tip"
HAnimSite905.DEF = "hanim_l_carpal_distal_phalanx_4_tip"
HAnimSite905.translation = [0,1,0]
TouchSensor906 = x3d.TouchSensor()
TouchSensor906.description = "HAnimSite l_carpal_distal_phalanx_4_tip"

HAnimSite905.children.append(TouchSensor906)
Shape907 = x3d.Shape()
Shape907.USE = "HAnimSiteShape"

HAnimSite905.children.append(Shape907)

HAnimJoint900.HAnimSite.append(HAnimSite905)
HAnimJoint908 = x3d.HAnimJoint()
HAnimJoint908.name = "l_carpal_distal_interphalangeal_4"
HAnimJoint908.DEF = "hanim_l_carpal_distal_interphalangeal_4"
HAnimJoint908.center = [0.1983,0.7045,-0.0767]
HAnimJoint908.ulimit = [0,0,0]
HAnimJoint908.llimit = [0,0,0]

HAnimJoint900.children.append(HAnimJoint908)

HAnimJoint895.children.append(HAnimJoint900)

HAnimJoint890.children.append(HAnimJoint895)

HAnimJoint878.children.append(HAnimJoint890)
HAnimJoint909 = x3d.HAnimJoint()
HAnimJoint909.name = "l_carpometacarpal_5"
HAnimJoint909.DEF = "hanim_l_carpometacarpal_5"
HAnimJoint909.center = [0.1925,0.8066,-0.1036]
HAnimJoint909.ulimit = [0,0,0]
HAnimJoint909.llimit = [0,0,0]
Shape910 = x3d.Shape()
LineSet911 = x3d.LineSet()
LineSet911.vertexCount = [2]
Coordinate912 = x3d.Coordinate()

LineSet911.coord = Coordinate912
#from l_carpometacarpal_5 to l_metacarpophalangeal_5
ColorRGBA913 = x3d.ColorRGBA()
ColorRGBA913.USE = "HAnimSegmentLineColorRGBA"

LineSet911.color = ColorRGBA913

Shape910.geometry = LineSet911

HAnimJoint909.pe.append(Shape910)
HAnimJoint914 = x3d.HAnimJoint()
HAnimJoint914.name = "l_metacarpophalangeal_5"
HAnimJoint914.DEF = "hanim_l_metacarpophalangeal_5"
HAnimJoint914.center = [0.1925,0.7866,-0.1036]
HAnimJoint914.ulimit = [0,0,0]
HAnimJoint914.llimit = [0,0,0]
Shape915 = x3d.Shape()
LineSet916 = x3d.LineSet()
LineSet916.vertexCount = [2]
Coordinate917 = x3d.Coordinate()

LineSet916.coord = Coordinate917
#from l_metacarpophalangeal_5 to l_carpal_proximal_interphalangeal_5
ColorRGBA918 = x3d.ColorRGBA()
ColorRGBA918.USE = "HAnimSegmentLineColorRGBA"

LineSet916.color = ColorRGBA918

Shape915.geometry = LineSet916

HAnimJoint914.pe.append(Shape915)
HAnimJoint919 = x3d.HAnimJoint()
HAnimJoint919.name = "l_carpal_proximal_interphalangeal_5"
HAnimJoint919.DEF = "hanim_l_carpal_proximal_interphalangeal_5"
HAnimJoint919.center = [0.1938,0.7452,-0.1024]
HAnimJoint919.ulimit = [0,0,0]
HAnimJoint919.llimit = [0,0,0]
Shape920 = x3d.Shape()
LineSet921 = x3d.LineSet()
LineSet921.vertexCount = [2]
Coordinate922 = x3d.Coordinate()

LineSet921.coord = Coordinate922
#from l_carpal_proximal_interphalangeal_5 to l_carpal_distal_interphalangeal_5
ColorRGBA923 = x3d.ColorRGBA()
ColorRGBA923.USE = "HAnimSegmentLineColorRGBA"

LineSet921.color = ColorRGBA923

Shape920.geometry = LineSet921

HAnimJoint919.pe.append(Shape920)
HAnimSite924 = x3d.HAnimSite()
HAnimSite924.name = "l_carpal_distal_phalanx_5_tip"
HAnimSite924.DEF = "hanim_l_carpal_distal_phalanx_5_tip"
HAnimSite924.translation = [0,1,0]
TouchSensor925 = x3d.TouchSensor()
TouchSensor925.description = "HAnimSite l_carpal_distal_phalanx_5_tip"

HAnimSite924.children.append(TouchSensor925)
Shape926 = x3d.Shape()
Shape926.USE = "HAnimSiteShape"

HAnimSite924.children.append(Shape926)

HAnimJoint919.HAnimSite.append(HAnimSite924)
HAnimJoint927 = x3d.HAnimJoint()
HAnimJoint927.name = "l_carpal_distal_interphalangeal_5"
HAnimJoint927.DEF = "hanim_l_carpal_distal_interphalangeal_5"
HAnimJoint927.center = [0.1948,0.7277,-0.1017]
HAnimJoint927.ulimit = [0,0,0]
HAnimJoint927.llimit = [0,0,0]

HAnimJoint919.children.append(HAnimJoint927)

HAnimJoint914.children.append(HAnimJoint919)

HAnimJoint909.children.append(HAnimJoint914)

HAnimJoint878.children.append(HAnimJoint909)

HAnimJoint785.children.append(HAnimJoint878)

HAnimJoint777.children.append(HAnimJoint785)

HAnimJoint760.children.append(HAnimJoint777)

HAnimJoint749.children.append(HAnimJoint760)

HAnimJoint744.children.append(HAnimJoint749)

HAnimJoint576.children.append(HAnimJoint744)
HAnimJoint928 = x3d.HAnimJoint()
HAnimJoint928.name = "r_sternoclavicular"
HAnimJoint928.DEF = "hanim_r_sternoclavicular"
HAnimJoint928.center = [-0.0694,1.46,-0.033]
HAnimJoint928.ulimit = [0,0,0]
HAnimJoint928.llimit = [0,0,0]
Shape929 = x3d.Shape()
LineSet930 = x3d.LineSet()
LineSet930.vertexCount = [2]
Coordinate931 = x3d.Coordinate()

LineSet930.coord = Coordinate931
#from r_sternoclavicular to r_acromioclavicular
ColorRGBA932 = x3d.ColorRGBA()
ColorRGBA932.USE = "HAnimSegmentLineColorRGBA"

LineSet930.color = ColorRGBA932

Shape929.geometry = LineSet930

HAnimJoint928.pe.append(Shape929)
HAnimJoint933 = x3d.HAnimJoint()
HAnimJoint933.name = "r_acromioclavicular"
HAnimJoint933.DEF = "hanim_r_acromioclavicular"
HAnimJoint933.center = [-0.0836,1.4281,-0.0401]
HAnimJoint933.ulimit = [0,0,0]
HAnimJoint933.llimit = [0,0,0]
Shape934 = x3d.Shape()
LineSet935 = x3d.LineSet()
LineSet935.vertexCount = [2]
Coordinate936 = x3d.Coordinate()

LineSet935.coord = Coordinate936
#from r_acromioclavicular to r_shoulder
ColorRGBA937 = x3d.ColorRGBA()
ColorRGBA937.USE = "HAnimSegmentLineColorRGBA"

LineSet935.color = ColorRGBA937

Shape934.geometry = LineSet935

HAnimJoint933.pe.append(Shape934)
HAnimSite938 = x3d.HAnimSite()
HAnimSite938.name = "r_bideltoid_pt"
HAnimSite938.DEF = "hanim_r_bideltoid_pt"
HAnimSite938.translation = [0,1,0]
TouchSensor939 = x3d.TouchSensor()
TouchSensor939.description = "HAnimSite r_bideltoid_pt"

HAnimSite938.children.append(TouchSensor939)
Shape940 = x3d.Shape()
Shape940.USE = "HAnimSiteShape"

HAnimSite938.children.append(Shape940)

HAnimJoint933.HAnimSite.append(HAnimSite938)
HAnimSite941 = x3d.HAnimSite()
HAnimSite941.name = "r_humeral_lateral_epicondyles_pt"
HAnimSite941.DEF = "hanim_r_humeral_lateral_epicondyles_pt"
HAnimSite941.translation = [-0.2224,1.1517,-0.1033]
TouchSensor942 = x3d.TouchSensor()
TouchSensor942.description = "HAnimSite r_humeral_lateral_epicondyles_pt"

HAnimSite941.children.append(TouchSensor942)
Shape943 = x3d.Shape()
Shape943.USE = "HAnimSiteShape"

HAnimSite941.children.append(Shape943)

HAnimJoint933.HAnimSite.append(HAnimSite941)
HAnimJoint944 = x3d.HAnimJoint()
HAnimJoint944.name = "r_shoulder"
HAnimJoint944.DEF = "hanim_r_shoulder"
HAnimJoint944.center = [-0.1907,1.4407,-0.0325]
HAnimJoint944.ulimit = [0,0,0]
HAnimJoint944.llimit = [0,0,0]
Shape945 = x3d.Shape()
LineSet946 = x3d.LineSet()
LineSet946.vertexCount = [2]
Coordinate947 = x3d.Coordinate()

LineSet946.coord = Coordinate947
#from r_shoulder to r_elbow
ColorRGBA948 = x3d.ColorRGBA()
ColorRGBA948.USE = "HAnimSegmentLineColorRGBA"

LineSet946.color = ColorRGBA948

Shape945.geometry = LineSet946

HAnimJoint944.pe.append(Shape945)
HAnimSite949 = x3d.HAnimSite()
HAnimSite949.name = "r_humeral_medial_epicondyles_pt"
HAnimSite949.DEF = "hanim_r_humeral_medial_epicondyles_pt"
HAnimSite949.translation = [-0.168,1.1298,-0.1062]
TouchSensor950 = x3d.TouchSensor()
TouchSensor950.description = "HAnimSite r_humeral_medial_epicondyles_pt"

HAnimSite949.children.append(TouchSensor950)
Shape951 = x3d.Shape()
Shape951.USE = "HAnimSiteShape"

HAnimSite949.children.append(Shape951)

HAnimJoint944.HAnimSite.append(HAnimSite949)
HAnimSite952 = x3d.HAnimSite()
HAnimSite952.name = "r_olecranon_pt"
HAnimSite952.DEF = "hanim_r_olecranon_pt"
HAnimSite952.translation = [-0.1907,1.1405,-0.1065]
TouchSensor953 = x3d.TouchSensor()
TouchSensor953.description = "HAnimSite r_olecranon_pt"

HAnimSite952.children.append(TouchSensor953)
Shape954 = x3d.Shape()
Shape954.USE = "HAnimSiteShape"

HAnimSite952.children.append(Shape954)

HAnimJoint944.HAnimSite.append(HAnimSite952)
HAnimSite955 = x3d.HAnimSite()
HAnimSite955.name = "r_radial_styloid_pt"
HAnimSite955.DEF = "hanim_r_radial_styloid_pt"
HAnimSite955.translation = [-0.1884,0.8676,-0.036]
TouchSensor956 = x3d.TouchSensor()
TouchSensor956.description = "HAnimSite r_radial_styloid_pt"

HAnimSite955.children.append(TouchSensor956)
Shape957 = x3d.Shape()
Shape957.USE = "HAnimSiteShape"

HAnimSite955.children.append(Shape957)

HAnimJoint944.HAnimSite.append(HAnimSite955)
HAnimSite958 = x3d.HAnimSite()
HAnimSite958.name = "r_radiale_pt"
HAnimSite958.DEF = "hanim_r_radiale_pt"
HAnimSite958.translation = [-0.213,1.1305,-0.1091]
TouchSensor959 = x3d.TouchSensor()
TouchSensor959.description = "HAnimSite r_radiale_pt"

HAnimSite958.children.append(TouchSensor959)
Shape960 = x3d.Shape()
Shape960.USE = "HAnimSiteShape"

HAnimSite958.children.append(Shape960)

HAnimJoint944.HAnimSite.append(HAnimSite958)
HAnimJoint961 = x3d.HAnimJoint()
HAnimJoint961.name = "r_elbow"
HAnimJoint961.DEF = "hanim_r_elbow"
HAnimJoint961.center = [-0.1949,1.1388,-0.062]
HAnimJoint961.ulimit = [0,0,0]
HAnimJoint961.llimit = [0,0,0]
Shape962 = x3d.Shape()
LineSet963 = x3d.LineSet()
LineSet963.vertexCount = [2]
Coordinate964 = x3d.Coordinate()

LineSet963.coord = Coordinate964
#from r_elbow to r_radiocarpal
ColorRGBA965 = x3d.ColorRGBA()
ColorRGBA965.USE = "HAnimSegmentLineColorRGBA"

LineSet963.color = ColorRGBA965

Shape962.geometry = LineSet963

HAnimJoint961.pe.append(Shape962)
HAnimSite966 = x3d.HAnimSite()
HAnimSite966.name = "r_ulnar_styloid_pt"
HAnimSite966.DEF = "hanim_r_ulnar_styloid_pt"
HAnimSite966.translation = [-0.2117,0.8562,-0.0584]
TouchSensor967 = x3d.TouchSensor()
TouchSensor967.description = "HAnimSite r_ulnar_styloid_pt"

HAnimSite966.children.append(TouchSensor967)
Shape968 = x3d.Shape()
Shape968.USE = "HAnimSiteShape"

HAnimSite966.children.append(Shape968)

HAnimJoint961.HAnimSite.append(HAnimSite966)
HAnimJoint969 = x3d.HAnimJoint()
HAnimJoint969.name = "r_radiocarpal"
HAnimJoint969.DEF = "hanim_r_radiocarpal"
HAnimJoint969.center = [-0.1959,0.8694,-0.0521]
HAnimJoint969.ulimit = [0,0,0]
HAnimJoint969.llimit = [0,0,0]
Shape970 = x3d.Shape()
LineSet971 = x3d.LineSet()
LineSet971.vertexCount = [2]
Coordinate972 = x3d.Coordinate()

LineSet971.coord = Coordinate972
#from r_radiocarpal to r_midcarpal_1
ColorRGBA973 = x3d.ColorRGBA()
ColorRGBA973.USE = "HAnimSegmentLineColorRGBA"

LineSet971.color = ColorRGBA973

Shape970.geometry = LineSet971

HAnimJoint969.pe.append(Shape970)
Shape974 = x3d.Shape()
LineSet975 = x3d.LineSet()
LineSet975.vertexCount = [2]
Coordinate976 = x3d.Coordinate()

LineSet975.coord = Coordinate976
#from r_radiocarpal to r_midcarpal_2
ColorRGBA977 = x3d.ColorRGBA()
ColorRGBA977.USE = "HAnimSegmentLineColorRGBA"

LineSet975.color = ColorRGBA977

Shape974.geometry = LineSet975

HAnimJoint969.pe.append(Shape974)
Shape978 = x3d.Shape()
LineSet979 = x3d.LineSet()
LineSet979.vertexCount = [2]
Coordinate980 = x3d.Coordinate()

LineSet979.coord = Coordinate980
#from r_radiocarpal to r_midcarpal_3
ColorRGBA981 = x3d.ColorRGBA()
ColorRGBA981.USE = "HAnimSegmentLineColorRGBA"

LineSet979.color = ColorRGBA981

Shape978.geometry = LineSet979

HAnimJoint969.pe.append(Shape978)
Shape982 = x3d.Shape()
LineSet983 = x3d.LineSet()
LineSet983.vertexCount = [2]
Coordinate984 = x3d.Coordinate()

LineSet983.coord = Coordinate984
#from r_radiocarpal to r_midcarpal_4_5
ColorRGBA985 = x3d.ColorRGBA()
ColorRGBA985.USE = "HAnimSegmentLineColorRGBA"

LineSet983.color = ColorRGBA985

Shape982.geometry = LineSet983

HAnimJoint969.pe.append(Shape982)
HAnimJoint986 = x3d.HAnimJoint()
HAnimJoint986.name = "r_midcarpal_1"
HAnimJoint986.DEF = "hanim_r_midcarpal_1"
HAnimJoint986.center = [0,1,0]
HAnimJoint986.ulimit = [0,0,0]
HAnimJoint986.llimit = [0,0,0]
Shape987 = x3d.Shape()
LineSet988 = x3d.LineSet()
LineSet988.vertexCount = [1]
Coordinate989 = x3d.Coordinate()

LineSet988.coord = Coordinate989
#from r_midcarpal_1 to r_carpometacarpal_1
ColorRGBA990 = x3d.ColorRGBA()
ColorRGBA990.USE = "HAnimSegmentLineColorRGBA"

LineSet988.color = ColorRGBA990

Shape987.geometry = LineSet988

HAnimJoint986.pe.append(Shape987)
HAnimJoint991 = x3d.HAnimJoint()
HAnimJoint991.name = "r_carpometacarpal_1"
HAnimJoint991.DEF = "hanim_r_carpometacarpal_1"
HAnimJoint991.center = [-0.1899,0.8502,-0.0473]
HAnimJoint991.ulimit = [0,0,0]
HAnimJoint991.llimit = [0,0,0]
Shape992 = x3d.Shape()
LineSet993 = x3d.LineSet()
LineSet993.vertexCount = [2]
Coordinate994 = x3d.Coordinate()

LineSet993.coord = Coordinate994
#from r_carpometacarpal_1 to r_metacarpophalangeal_1
ColorRGBA995 = x3d.ColorRGBA()
ColorRGBA995.USE = "HAnimSegmentLineColorRGBA"

LineSet993.color = ColorRGBA995

Shape992.geometry = LineSet993

HAnimJoint991.pe.append(Shape992)
HAnimJoint996 = x3d.HAnimJoint()
HAnimJoint996.name = "r_metacarpophalangeal_1"
HAnimJoint996.DEF = "hanim_r_metacarpophalangeal_1"
HAnimJoint996.center = [-0.1874,0.8256,0.0306]
HAnimJoint996.ulimit = [0,0,0]
HAnimJoint996.llimit = [0,0,0]
Shape997 = x3d.Shape()
LineSet998 = x3d.LineSet()
LineSet998.vertexCount = [2]
Coordinate999 = x3d.Coordinate()

LineSet998.coord = Coordinate999
#from r_metacarpophalangeal_1 to r_carpal_interphalangeal_1
ColorRGBA1000 = x3d.ColorRGBA()
ColorRGBA1000.USE = "HAnimSegmentLineColorRGBA"

LineSet998.color = ColorRGBA1000

Shape997.geometry = LineSet998

HAnimJoint996.pe.append(Shape997)
HAnimSite1001 = x3d.HAnimSite()
HAnimSite1001.name = "r_carpal_distal_phalanx_1_tip"
HAnimSite1001.DEF = "hanim_r_carpal_distal_phalanx_1_tip"
HAnimSite1001.translation = [0,1,0]
TouchSensor1002 = x3d.TouchSensor()
TouchSensor1002.description = "HAnimSite r_carpal_distal_phalanx_1_tip"

HAnimSite1001.children.append(TouchSensor1002)
Shape1003 = x3d.Shape()
Shape1003.USE = "HAnimSiteShape"

HAnimSite1001.children.append(Shape1003)

HAnimJoint996.HAnimSite.append(HAnimSite1001)
HAnimJoint1004 = x3d.HAnimJoint()
HAnimJoint1004.name = "r_carpal_interphalangeal_1"
HAnimJoint1004.DEF = "hanim_r_carpal_interphalangeal_1"
HAnimJoint1004.center = [-0.1864,0.819,0.0506]
HAnimJoint1004.ulimit = [0,0,0]
HAnimJoint1004.llimit = [0,0,0]

HAnimJoint996.children.append(HAnimJoint1004)

HAnimJoint991.children.append(HAnimJoint996)

HAnimJoint986.children.append(HAnimJoint991)

HAnimJoint969.children.append(HAnimJoint986)
HAnimJoint1005 = x3d.HAnimJoint()
HAnimJoint1005.name = "r_midcarpal_2"
HAnimJoint1005.DEF = "hanim_r_midcarpal_2"
HAnimJoint1005.center = [0,1,0]
HAnimJoint1005.ulimit = [0,0,0]
HAnimJoint1005.llimit = [0,0,0]
Shape1006 = x3d.Shape()
LineSet1007 = x3d.LineSet()
LineSet1007.vertexCount = [1]
Coordinate1008 = x3d.Coordinate()

LineSet1007.coord = Coordinate1008
#from r_midcarpal_2 to r_carpometacarpal_2
ColorRGBA1009 = x3d.ColorRGBA()
ColorRGBA1009.USE = "HAnimSegmentLineColorRGBA"

LineSet1007.color = ColorRGBA1009

Shape1006.geometry = LineSet1007

HAnimJoint1005.pe.append(Shape1006)
HAnimSite1010 = x3d.HAnimSite()
HAnimSite1010.name = "r_metacarpal_phalanx_2_pt"
HAnimSite1010.DEF = "hanim_r_metacarpal_phalanx_2_pt"
HAnimSite1010.translation = [-0.1977,0.8169,-0.0177]
TouchSensor1011 = x3d.TouchSensor()
TouchSensor1011.description = "HAnimSite r_metacarpal_phalanx_2_pt"

HAnimSite1010.children.append(TouchSensor1011)
Shape1012 = x3d.Shape()
Shape1012.USE = "HAnimSiteShape"

HAnimSite1010.children.append(Shape1012)

HAnimJoint1005.HAnimSite.append(HAnimSite1010)
HAnimJoint1013 = x3d.HAnimJoint()
HAnimJoint1013.name = "r_carpometacarpal_2"
HAnimJoint1013.DEF = "hanim_r_carpometacarpal_2"
HAnimJoint1013.center = [-0.1961,0.8055,-0.0218]
HAnimJoint1013.ulimit = [0,0,0]
HAnimJoint1013.llimit = [0,0,0]
Shape1014 = x3d.Shape()
LineSet1015 = x3d.LineSet()
LineSet1015.vertexCount = [2]
Coordinate1016 = x3d.Coordinate()

LineSet1015.coord = Coordinate1016
#from r_carpometacarpal_2 to r_metacarpophalangeal_2
ColorRGBA1017 = x3d.ColorRGBA()
ColorRGBA1017.USE = "HAnimSegmentLineColorRGBA"

LineSet1015.color = ColorRGBA1017

Shape1014.geometry = LineSet1015

HAnimJoint1013.pe.append(Shape1014)
HAnimJoint1018 = x3d.HAnimJoint()
HAnimJoint1018.name = "r_metacarpophalangeal_2"
HAnimJoint1018.DEF = "hanim_r_metacarpophalangeal_2"
HAnimJoint1018.center = [-0.1961,0.7846,-0.0218]
HAnimJoint1018.ulimit = [0,0,0]
HAnimJoint1018.llimit = [0,0,0]
Shape1019 = x3d.Shape()
LineSet1020 = x3d.LineSet()
LineSet1020.vertexCount = [2]
Coordinate1021 = x3d.Coordinate()

LineSet1020.coord = Coordinate1021
#from r_metacarpophalangeal_2 to r_carpal_proximal_interphalangeal_2
ColorRGBA1022 = x3d.ColorRGBA()
ColorRGBA1022.USE = "HAnimSegmentLineColorRGBA"

LineSet1020.color = ColorRGBA1022

Shape1019.geometry = LineSet1020

HAnimJoint1018.pe.append(Shape1019)
HAnimJoint1023 = x3d.HAnimJoint()
HAnimJoint1023.name = "r_carpal_proximal_interphalangeal_2"
HAnimJoint1023.DEF = "hanim_r_carpal_proximal_interphalangeal_2"
HAnimJoint1023.center = [-0.1954,0.7393,-0.0185]
HAnimJoint1023.ulimit = [0,0,0]
HAnimJoint1023.llimit = [0,0,0]
Shape1024 = x3d.Shape()
LineSet1025 = x3d.LineSet()
LineSet1025.vertexCount = [2]
Coordinate1026 = x3d.Coordinate()

LineSet1025.coord = Coordinate1026
#from r_carpal_proximal_interphalangeal_2 to r_carpal_distal_interphalangeal_2
ColorRGBA1027 = x3d.ColorRGBA()
ColorRGBA1027.USE = "HAnimSegmentLineColorRGBA"

LineSet1025.color = ColorRGBA1027

Shape1024.geometry = LineSet1025

HAnimJoint1023.pe.append(Shape1024)
HAnimSite1028 = x3d.HAnimSite()
HAnimSite1028.name = "r_carpal_distal_phalanx_2_tip"
HAnimSite1028.DEF = "hanim_r_carpal_distal_phalanx_2_tip"
HAnimSite1028.translation = [0,1,0]
TouchSensor1029 = x3d.TouchSensor()
TouchSensor1029.description = "HAnimSite r_carpal_distal_phalanx_2_tip"

HAnimSite1028.children.append(TouchSensor1029)
Shape1030 = x3d.Shape()
Shape1030.USE = "HAnimSiteShape"

HAnimSite1028.children.append(Shape1030)

HAnimJoint1023.HAnimSite.append(HAnimSite1028)
HAnimSite1031 = x3d.HAnimSite()
HAnimSite1031.name = "r_dactylion_pt"
HAnimSite1031.DEF = "hanim_r_dactylion_pt"
HAnimSite1031.translation = [-0.1941,0.6772,-0.0423]
TouchSensor1032 = x3d.TouchSensor()
TouchSensor1032.description = "HAnimSite r_dactylion_pt"

HAnimSite1031.children.append(TouchSensor1032)
Shape1033 = x3d.Shape()
Shape1033.USE = "HAnimSiteShape"

HAnimSite1031.children.append(Shape1033)

HAnimJoint1023.HAnimSite.append(HAnimSite1031)
HAnimJoint1034 = x3d.HAnimJoint()
HAnimJoint1034.name = "r_carpal_distal_interphalangeal_2"
HAnimJoint1034.DEF = "hanim_r_carpal_distal_interphalangeal_2"
HAnimJoint1034.center = [-0.1945,0.7169,-0.0173]
HAnimJoint1034.ulimit = [0,0,0]
HAnimJoint1034.llimit = [0,0,0]

HAnimJoint1023.children.append(HAnimJoint1034)

HAnimJoint1018.children.append(HAnimJoint1023)

HAnimJoint1013.children.append(HAnimJoint1018)

HAnimJoint1005.children.append(HAnimJoint1013)

HAnimJoint969.children.append(HAnimJoint1005)
HAnimJoint1035 = x3d.HAnimJoint()
HAnimJoint1035.name = "r_midcarpal_3"
HAnimJoint1035.DEF = "hanim_r_midcarpal_3"
HAnimJoint1035.center = [0,1,0]
HAnimJoint1035.ulimit = [0,0,0]
HAnimJoint1035.llimit = [0,0,0]
Shape1036 = x3d.Shape()
LineSet1037 = x3d.LineSet()
LineSet1037.vertexCount = [1]
Coordinate1038 = x3d.Coordinate()

LineSet1037.coord = Coordinate1038
#from r_midcarpal_3 to r_carpometacarpal_3
ColorRGBA1039 = x3d.ColorRGBA()
ColorRGBA1039.USE = "HAnimSegmentLineColorRGBA"

LineSet1037.color = ColorRGBA1039

Shape1036.geometry = LineSet1037

HAnimJoint1035.pe.append(Shape1036)
HAnimSite1040 = x3d.HAnimSite()
HAnimSite1040.name = "r_metacarpal_phalanx_3_pt"
HAnimSite1040.DEF = "hanim_r_metacarpal_phalanx_3_pt"
HAnimSite1040.translation = [0,1,0]
TouchSensor1041 = x3d.TouchSensor()
TouchSensor1041.description = "HAnimSite r_metacarpal_phalanx_3_pt"

HAnimSite1040.children.append(TouchSensor1041)
Shape1042 = x3d.Shape()
Shape1042.USE = "HAnimSiteShape"

HAnimSite1040.children.append(Shape1042)

HAnimJoint1035.HAnimSite.append(HAnimSite1040)
HAnimJoint1043 = x3d.HAnimJoint()
HAnimJoint1043.name = "r_carpometacarpal_3"
HAnimJoint1043.DEF = "hanim_r_carpometacarpal_3"
HAnimJoint1043.center = [-0.1972,0.806,-0.0468]
HAnimJoint1043.ulimit = [0,0,0]
HAnimJoint1043.llimit = [0,0,0]
Shape1044 = x3d.Shape()
LineSet1045 = x3d.LineSet()
LineSet1045.vertexCount = [2]
Coordinate1046 = x3d.Coordinate()

LineSet1045.coord = Coordinate1046
#from r_carpometacarpal_3 to r_metacarpophalangeal_3
ColorRGBA1047 = x3d.ColorRGBA()
ColorRGBA1047.USE = "HAnimSegmentLineColorRGBA"

LineSet1045.color = ColorRGBA1047

Shape1044.geometry = LineSet1045

HAnimJoint1043.pe.append(Shape1044)
HAnimJoint1048 = x3d.HAnimJoint()
HAnimJoint1048.name = "r_metacarpophalangeal_3"
HAnimJoint1048.DEF = "hanim_r_metacarpophalangeal_3"
HAnimJoint1048.center = [-0.1972,0.7849,-0.0468]
HAnimJoint1048.ulimit = [0,0,0]
HAnimJoint1048.llimit = [0,0,0]
Shape1049 = x3d.Shape()
LineSet1050 = x3d.LineSet()
LineSet1050.vertexCount = [2]
Coordinate1051 = x3d.Coordinate()

LineSet1050.coord = Coordinate1051
#from r_metacarpophalangeal_3 to r_carpal_proximal_interphalangeal_3
ColorRGBA1052 = x3d.ColorRGBA()
ColorRGBA1052.USE = "HAnimSegmentLineColorRGBA"

LineSet1050.color = ColorRGBA1052

Shape1049.geometry = LineSet1050

HAnimJoint1048.pe.append(Shape1049)
HAnimJoint1053 = x3d.HAnimJoint()
HAnimJoint1053.name = "r_carpal_proximal_interphalangeal_3"
HAnimJoint1053.DEF = "hanim_r_carpal_proximal_interphalangeal_3"
HAnimJoint1053.center = [-0.195,0.7304,-0.0441]
HAnimJoint1053.ulimit = [0,0,0]
HAnimJoint1053.llimit = [0,0,0]
Shape1054 = x3d.Shape()
LineSet1055 = x3d.LineSet()
LineSet1055.vertexCount = [2]
Coordinate1056 = x3d.Coordinate()

LineSet1055.coord = Coordinate1056
#from r_carpal_proximal_interphalangeal_3 to r_carpal_distal_interphalangeal_3
ColorRGBA1057 = x3d.ColorRGBA()
ColorRGBA1057.USE = "HAnimSegmentLineColorRGBA"

LineSet1055.color = ColorRGBA1057

Shape1054.geometry = LineSet1055

HAnimJoint1053.pe.append(Shape1054)
HAnimSite1058 = x3d.HAnimSite()
HAnimSite1058.name = "r_carpal_distal_phalanx_3_tip"
HAnimSite1058.DEF = "hanim_r_carpal_distal_phalanx_3_tip"
HAnimSite1058.translation = [0,1,0]
TouchSensor1059 = x3d.TouchSensor()
TouchSensor1059.description = "HAnimSite r_carpal_distal_phalanx_3_tip"

HAnimSite1058.children.append(TouchSensor1059)
Shape1060 = x3d.Shape()
Shape1060.USE = "HAnimSiteShape"

HAnimSite1058.children.append(Shape1060)

HAnimJoint1053.HAnimSite.append(HAnimSite1058)
HAnimJoint1061 = x3d.HAnimJoint()
HAnimJoint1061.name = "r_carpal_distal_interphalangeal_3"
HAnimJoint1061.DEF = "hanim_r_carpal_distal_interphalangeal_3"
HAnimJoint1061.center = [-0.1939,0.7042,-0.0432]
HAnimJoint1061.ulimit = [0,0,0]
HAnimJoint1061.llimit = [0,0,0]

HAnimJoint1053.children.append(HAnimJoint1061)

HAnimJoint1048.children.append(HAnimJoint1053)

HAnimJoint1043.children.append(HAnimJoint1048)

HAnimJoint1035.children.append(HAnimJoint1043)

HAnimJoint969.children.append(HAnimJoint1035)
HAnimJoint1062 = x3d.HAnimJoint()
HAnimJoint1062.name = "r_midcarpal_4_5"
HAnimJoint1062.DEF = "hanim_r_midcarpal_4_5"
HAnimJoint1062.center = [0,1,0]
HAnimJoint1062.ulimit = [0,0,0]
HAnimJoint1062.llimit = [0,0,0]
Shape1063 = x3d.Shape()
LineSet1064 = x3d.LineSet()
LineSet1064.vertexCount = [1]
Coordinate1065 = x3d.Coordinate()

LineSet1064.coord = Coordinate1065
#from r_midcarpal_4_5 to r_carpometacarpal_4
ColorRGBA1066 = x3d.ColorRGBA()
ColorRGBA1066.USE = "HAnimSegmentLineColorRGBA"

LineSet1064.color = ColorRGBA1066

Shape1063.geometry = LineSet1064

HAnimJoint1062.pe.append(Shape1063)
Shape1067 = x3d.Shape()
LineSet1068 = x3d.LineSet()
LineSet1068.vertexCount = [1]
Coordinate1069 = x3d.Coordinate()

LineSet1068.coord = Coordinate1069
#from r_midcarpal_4_5 to r_carpometacarpal_5
ColorRGBA1070 = x3d.ColorRGBA()
ColorRGBA1070.USE = "HAnimSegmentLineColorRGBA"

LineSet1068.color = ColorRGBA1070

Shape1067.geometry = LineSet1068

HAnimJoint1062.pe.append(Shape1067)
HAnimSite1071 = x3d.HAnimSite()
HAnimSite1071.name = "r_metacarpal_phalanx_5_pt"
HAnimSite1071.DEF = "hanim_r_metacarpal_phalanx_5_pt"
HAnimSite1071.translation = [-0.1929,0.789,-0.1064]
TouchSensor1072 = x3d.TouchSensor()
TouchSensor1072.description = "HAnimSite r_metacarpal_phalanx_5_pt"

HAnimSite1071.children.append(TouchSensor1072)
Shape1073 = x3d.Shape()
Shape1073.USE = "HAnimSiteShape"

HAnimSite1071.children.append(Shape1073)

HAnimJoint1062.HAnimSite.append(HAnimSite1071)
HAnimJoint1074 = x3d.HAnimJoint()
HAnimJoint1074.name = "r_carpometacarpal_4"
HAnimJoint1074.DEF = "hanim_r_carpometacarpal_4"
HAnimJoint1074.center = [-0.1951,0.8049,-0.0732]
HAnimJoint1074.ulimit = [0,0,0]
HAnimJoint1074.llimit = [0,0,0]
Shape1075 = x3d.Shape()
LineSet1076 = x3d.LineSet()
LineSet1076.vertexCount = [2]
Coordinate1077 = x3d.Coordinate()

LineSet1076.coord = Coordinate1077
#from r_carpometacarpal_4 to r_metacarpophalangeal_4
ColorRGBA1078 = x3d.ColorRGBA()
ColorRGBA1078.USE = "HAnimSegmentLineColorRGBA"

LineSet1076.color = ColorRGBA1078

Shape1075.geometry = LineSet1076

HAnimJoint1074.pe.append(Shape1075)
HAnimJoint1079 = x3d.HAnimJoint()
HAnimJoint1079.name = "r_metacarpophalangeal_4"
HAnimJoint1079.DEF = "hanim_r_metacarpophalangeal_4"
HAnimJoint1079.center = [-0.1951,0.7845,-0.0732]
HAnimJoint1079.ulimit = [0,0,0]
HAnimJoint1079.llimit = [0,0,0]
Shape1080 = x3d.Shape()
LineSet1081 = x3d.LineSet()
LineSet1081.vertexCount = [2]
Coordinate1082 = x3d.Coordinate()

LineSet1081.coord = Coordinate1082
#from r_metacarpophalangeal_4 to r_carpal_proximal_interphalangeal_4
ColorRGBA1083 = x3d.ColorRGBA()
ColorRGBA1083.USE = "HAnimSegmentLineColorRGBA"

LineSet1081.color = ColorRGBA1083

Shape1080.geometry = LineSet1081

HAnimJoint1079.pe.append(Shape1080)
HAnimJoint1084 = x3d.HAnimJoint()
HAnimJoint1084.name = "r_carpal_proximal_interphalangeal_4"
HAnimJoint1084.DEF = "hanim_r_carpal_proximal_interphalangeal_4"
HAnimJoint1084.center = [-0.192,0.7318,-0.0716]
HAnimJoint1084.ulimit = [0,0,0]
HAnimJoint1084.llimit = [0,0,0]
Shape1085 = x3d.Shape()
LineSet1086 = x3d.LineSet()
LineSet1086.vertexCount = [2]
Coordinate1087 = x3d.Coordinate()

LineSet1086.coord = Coordinate1087
#from r_carpal_proximal_interphalangeal_4 to r_carpal_distal_interphalangeal_4
ColorRGBA1088 = x3d.ColorRGBA()
ColorRGBA1088.USE = "HAnimSegmentLineColorRGBA"

LineSet1086.color = ColorRGBA1088

Shape1085.geometry = LineSet1086

HAnimJoint1084.pe.append(Shape1085)
HAnimSite1089 = x3d.HAnimSite()
HAnimSite1089.name = "r_carpal_distal_phalanx_4_tip"
HAnimSite1089.DEF = "hanim_r_carpal_distal_phalanx_4_tip"
HAnimSite1089.translation = [0,1,0]
TouchSensor1090 = x3d.TouchSensor()
TouchSensor1090.description = "HAnimSite r_carpal_distal_phalanx_4_tip"

HAnimSite1089.children.append(TouchSensor1090)
Shape1091 = x3d.Shape()
Shape1091.USE = "HAnimSiteShape"

HAnimSite1089.children.append(Shape1091)

HAnimJoint1084.HAnimSite.append(HAnimSite1089)
HAnimJoint1092 = x3d.HAnimJoint()
HAnimJoint1092.name = "r_carpal_distal_interphalangeal_4"
HAnimJoint1092.DEF = "hanim_r_carpal_distal_interphalangeal_4"
HAnimJoint1092.center = [-0.1908,0.7077,-0.0706]
HAnimJoint1092.ulimit = [0,0,0]
HAnimJoint1092.llimit = [0,0,0]

HAnimJoint1084.children.append(HAnimJoint1092)

HAnimJoint1079.children.append(HAnimJoint1084)

HAnimJoint1074.children.append(HAnimJoint1079)

HAnimJoint1062.children.append(HAnimJoint1074)
HAnimJoint1093 = x3d.HAnimJoint()
HAnimJoint1093.name = "r_carpometacarpal_5"
HAnimJoint1093.DEF = "hanim_r_carpometacarpal_5"
HAnimJoint1093.center = [-0.1926,0.8096,-0.0975]
HAnimJoint1093.ulimit = [0,0,0]
HAnimJoint1093.llimit = [0,0,0]
Shape1094 = x3d.Shape()
LineSet1095 = x3d.LineSet()
LineSet1095.vertexCount = [2]
Coordinate1096 = x3d.Coordinate()

LineSet1095.coord = Coordinate1096
#from r_carpometacarpal_5 to r_metacarpophalangeal_5
ColorRGBA1097 = x3d.ColorRGBA()
ColorRGBA1097.USE = "HAnimSegmentLineColorRGBA"

LineSet1095.color = ColorRGBA1097

Shape1094.geometry = LineSet1095

HAnimJoint1093.pe.append(Shape1094)
HAnimJoint1098 = x3d.HAnimJoint()
HAnimJoint1098.name = "r_metacarpophalangeal_5"
HAnimJoint1098.DEF = "hanim_r_metacarpophalangeal_5"
HAnimJoint1098.center = [-0.1926,0.7896,-0.0975]
HAnimJoint1098.ulimit = [0,0,0]
HAnimJoint1098.llimit = [0,0,0]
Shape1099 = x3d.Shape()
LineSet1100 = x3d.LineSet()
LineSet1100.vertexCount = [2]
Coordinate1101 = x3d.Coordinate()

LineSet1100.coord = Coordinate1101
#from r_metacarpophalangeal_5 to r_carpal_proximal_interphalangeal_5
ColorRGBA1102 = x3d.ColorRGBA()
ColorRGBA1102.USE = "HAnimSegmentLineColorRGBA"

LineSet1100.color = ColorRGBA1102

Shape1099.geometry = LineSet1100

HAnimJoint1098.pe.append(Shape1099)
HAnimJoint1103 = x3d.HAnimJoint()
HAnimJoint1103.name = "r_carpal_proximal_interphalangeal_5"
HAnimJoint1103.DEF = "hanim_r_carpal_proximal_interphalangeal_5"
HAnimJoint1103.center = [-0.1902,0.7483,-0.0963]
HAnimJoint1103.ulimit = [0,0,0]
HAnimJoint1103.llimit = [0,0,0]
Shape1104 = x3d.Shape()
LineSet1105 = x3d.LineSet()
LineSet1105.vertexCount = [2]
Coordinate1106 = x3d.Coordinate()

LineSet1105.coord = Coordinate1106
#from r_carpal_proximal_interphalangeal_5 to r_carpal_distal_interphalangeal_5
ColorRGBA1107 = x3d.ColorRGBA()
ColorRGBA1107.USE = "HAnimSegmentLineColorRGBA"

LineSet1105.color = ColorRGBA1107

Shape1104.geometry = LineSet1105

HAnimJoint1103.pe.append(Shape1104)
HAnimSite1108 = x3d.HAnimSite()
HAnimSite1108.name = "r_carpal_distal_phalanx_5_tip"
HAnimSite1108.DEF = "hanim_r_carpal_distal_phalanx_5_tip"
HAnimSite1108.translation = [0,1,0]
TouchSensor1109 = x3d.TouchSensor()
TouchSensor1109.description = "HAnimSite r_carpal_distal_phalanx_5_tip"

HAnimSite1108.children.append(TouchSensor1109)
Shape1110 = x3d.Shape()
Shape1110.USE = "HAnimSiteShape"

HAnimSite1108.children.append(Shape1110)

HAnimJoint1103.HAnimSite.append(HAnimSite1108)
HAnimJoint1111 = x3d.HAnimJoint()
HAnimJoint1111.name = "r_carpal_distal_interphalangeal_5"
HAnimJoint1111.DEF = "hanim_r_carpal_distal_interphalangeal_5"
HAnimJoint1111.center = [-0.1908,0.754,-0.096]
HAnimJoint1111.ulimit = [0,0,0]
HAnimJoint1111.llimit = [0,0,0]

HAnimJoint1103.children.append(HAnimJoint1111)

HAnimJoint1098.children.append(HAnimJoint1103)

HAnimJoint1093.children.append(HAnimJoint1098)

HAnimJoint1062.children.append(HAnimJoint1093)

HAnimJoint969.children.append(HAnimJoint1062)

HAnimJoint961.children.append(HAnimJoint969)

HAnimJoint944.children.append(HAnimJoint961)

HAnimJoint933.children.append(HAnimJoint944)

HAnimJoint928.children.append(HAnimJoint933)

HAnimJoint576.children.append(HAnimJoint928)

HAnimJoint565.children.append(HAnimJoint576)

HAnimJoint560.children.append(HAnimJoint565)

HAnimJoint555.children.append(HAnimJoint560)

HAnimJoint550.children.append(HAnimJoint555)

HAnimJoint542.children.append(HAnimJoint550)

HAnimJoint525.children.append(HAnimJoint542)

HAnimJoint520.children.append(HAnimJoint525)

HAnimJoint515.children.append(HAnimJoint520)

HAnimJoint504.children.append(HAnimJoint515)

HAnimJoint496.children.append(HAnimJoint504)

HAnimJoint491.children.append(HAnimJoint496)

HAnimJoint486.children.append(HAnimJoint491)

HAnimJoint481.children.append(HAnimJoint486)

HAnimJoint467.children.append(HAnimJoint481)

HAnimJoint462.children.append(HAnimJoint467)

HAnimJoint457.children.append(HAnimJoint462)

HAnimJoint32.children.append(HAnimJoint457)

HAnimHumanoid31.skeleton.append(HAnimJoint32)
HAnimJoint1112 = x3d.HAnimJoint()
HAnimJoint1112.USE = "hanim_humanoid_root"

HAnimHumanoid31.joints.append(HAnimJoint1112)
HAnimJoint1113 = x3d.HAnimJoint()
HAnimJoint1113.USE = "hanim_sacroiliac"

HAnimHumanoid31.joints.append(HAnimJoint1113)
HAnimJoint1114 = x3d.HAnimJoint()
HAnimJoint1114.USE = "hanim_l_hip"

HAnimHumanoid31.joints.append(HAnimJoint1114)
HAnimJoint1115 = x3d.HAnimJoint()
HAnimJoint1115.USE = "hanim_l_knee"

HAnimHumanoid31.joints.append(HAnimJoint1115)
HAnimJoint1116 = x3d.HAnimJoint()
HAnimJoint1116.USE = "hanim_l_talocrural"

HAnimHumanoid31.joints.append(HAnimJoint1116)
HAnimJoint1117 = x3d.HAnimJoint()
HAnimJoint1117.USE = "hanim_l_talocalcaneonavicular"

HAnimHumanoid31.joints.append(HAnimJoint1117)
HAnimJoint1118 = x3d.HAnimJoint()
HAnimJoint1118.USE = "hanim_l_cuneonavicular_1"

HAnimHumanoid31.joints.append(HAnimJoint1118)
HAnimJoint1119 = x3d.HAnimJoint()
HAnimJoint1119.USE = "hanim_l_tarsometatarsal_1"

HAnimHumanoid31.joints.append(HAnimJoint1119)
HAnimJoint1120 = x3d.HAnimJoint()
HAnimJoint1120.USE = "hanim_l_metatarsophalangeal_1"

HAnimHumanoid31.joints.append(HAnimJoint1120)
HAnimJoint1121 = x3d.HAnimJoint()
HAnimJoint1121.USE = "hanim_l_tarsal_interphalangeal_1"

HAnimHumanoid31.joints.append(HAnimJoint1121)
HAnimJoint1122 = x3d.HAnimJoint()
HAnimJoint1122.USE = "hanim_l_cuneonavicular_2"

HAnimHumanoid31.joints.append(HAnimJoint1122)
HAnimJoint1123 = x3d.HAnimJoint()
HAnimJoint1123.USE = "hanim_l_tarsometatarsal_2"

HAnimHumanoid31.joints.append(HAnimJoint1123)
HAnimJoint1124 = x3d.HAnimJoint()
HAnimJoint1124.USE = "hanim_l_metatarsophalangeal_2"

HAnimHumanoid31.joints.append(HAnimJoint1124)
HAnimJoint1125 = x3d.HAnimJoint()
HAnimJoint1125.USE = "hanim_l_tarsal_proximal_interphalangeal_2"

HAnimHumanoid31.joints.append(HAnimJoint1125)
HAnimJoint1126 = x3d.HAnimJoint()
HAnimJoint1126.USE = "hanim_l_tarsal_distal_interphalangeal_2"

HAnimHumanoid31.joints.append(HAnimJoint1126)
HAnimJoint1127 = x3d.HAnimJoint()
HAnimJoint1127.USE = "hanim_l_cuneonavicular_3"

HAnimHumanoid31.joints.append(HAnimJoint1127)
HAnimJoint1128 = x3d.HAnimJoint()
HAnimJoint1128.USE = "hanim_l_tarsometatarsal_3"

HAnimHumanoid31.joints.append(HAnimJoint1128)
HAnimJoint1129 = x3d.HAnimJoint()
HAnimJoint1129.USE = "hanim_l_metatarsophalangeal_3"

HAnimHumanoid31.joints.append(HAnimJoint1129)
HAnimJoint1130 = x3d.HAnimJoint()
HAnimJoint1130.USE = "hanim_l_tarsal_proximal_interphalangeal_3"

HAnimHumanoid31.joints.append(HAnimJoint1130)
HAnimJoint1131 = x3d.HAnimJoint()
HAnimJoint1131.USE = "hanim_l_tarsal_distal_interphalangeal_3"

HAnimHumanoid31.joints.append(HAnimJoint1131)
HAnimJoint1132 = x3d.HAnimJoint()
HAnimJoint1132.USE = "hanim_l_calcaneocuboid"

HAnimHumanoid31.joints.append(HAnimJoint1132)
HAnimJoint1133 = x3d.HAnimJoint()
HAnimJoint1133.USE = "hanim_l_transversetarsal"

HAnimHumanoid31.joints.append(HAnimJoint1133)
HAnimJoint1134 = x3d.HAnimJoint()
HAnimJoint1134.USE = "hanim_l_tarsometatarsal_4"

HAnimHumanoid31.joints.append(HAnimJoint1134)
HAnimJoint1135 = x3d.HAnimJoint()
HAnimJoint1135.USE = "hanim_l_metatarsophalangeal_4"

HAnimHumanoid31.joints.append(HAnimJoint1135)
HAnimJoint1136 = x3d.HAnimJoint()
HAnimJoint1136.USE = "hanim_l_tarsal_proximal_interphalangeal_4"

HAnimHumanoid31.joints.append(HAnimJoint1136)
HAnimJoint1137 = x3d.HAnimJoint()
HAnimJoint1137.USE = "hanim_l_tarsal_distal_interphalangeal_4"

HAnimHumanoid31.joints.append(HAnimJoint1137)
HAnimJoint1138 = x3d.HAnimJoint()
HAnimJoint1138.USE = "hanim_l_tarsometatarsal_5"

HAnimHumanoid31.joints.append(HAnimJoint1138)
HAnimJoint1139 = x3d.HAnimJoint()
HAnimJoint1139.USE = "hanim_l_metatarsophalangeal_5"

HAnimHumanoid31.joints.append(HAnimJoint1139)
HAnimJoint1140 = x3d.HAnimJoint()
HAnimJoint1140.USE = "hanim_l_tarsal_proximal_interphalangeal_5"

HAnimHumanoid31.joints.append(HAnimJoint1140)
HAnimJoint1141 = x3d.HAnimJoint()
HAnimJoint1141.USE = "hanim_l_tarsal_distal_interphalangeal_5"

HAnimHumanoid31.joints.append(HAnimJoint1141)
HAnimJoint1142 = x3d.HAnimJoint()
HAnimJoint1142.USE = "hanim_r_hip"

HAnimHumanoid31.joints.append(HAnimJoint1142)
HAnimJoint1143 = x3d.HAnimJoint()
HAnimJoint1143.USE = "hanim_r_knee"

HAnimHumanoid31.joints.append(HAnimJoint1143)
HAnimJoint1144 = x3d.HAnimJoint()
HAnimJoint1144.USE = "hanim_r_talocrural"

HAnimHumanoid31.joints.append(HAnimJoint1144)
HAnimJoint1145 = x3d.HAnimJoint()
HAnimJoint1145.USE = "hanim_r_talocalcaneonavicular"

HAnimHumanoid31.joints.append(HAnimJoint1145)
HAnimJoint1146 = x3d.HAnimJoint()
HAnimJoint1146.USE = "hanim_r_cuneonavicular_1"

HAnimHumanoid31.joints.append(HAnimJoint1146)
HAnimJoint1147 = x3d.HAnimJoint()
HAnimJoint1147.USE = "hanim_r_tarsometatarsal_1"

HAnimHumanoid31.joints.append(HAnimJoint1147)
HAnimJoint1148 = x3d.HAnimJoint()
HAnimJoint1148.USE = "hanim_r_metatarsophalangeal_1"

HAnimHumanoid31.joints.append(HAnimJoint1148)
HAnimJoint1149 = x3d.HAnimJoint()
HAnimJoint1149.USE = "hanim_r_tarsal_interphalangeal_1"

HAnimHumanoid31.joints.append(HAnimJoint1149)
HAnimJoint1150 = x3d.HAnimJoint()
HAnimJoint1150.USE = "hanim_r_cuneonavicular_2"

HAnimHumanoid31.joints.append(HAnimJoint1150)
HAnimJoint1151 = x3d.HAnimJoint()
HAnimJoint1151.USE = "hanim_r_tarsometatarsal_2"

HAnimHumanoid31.joints.append(HAnimJoint1151)
HAnimJoint1152 = x3d.HAnimJoint()
HAnimJoint1152.USE = "hanim_r_metatarsophalangeal_2"

HAnimHumanoid31.joints.append(HAnimJoint1152)
HAnimJoint1153 = x3d.HAnimJoint()
HAnimJoint1153.USE = "hanim_r_tarsal_proximal_interphalangeal_2"

HAnimHumanoid31.joints.append(HAnimJoint1153)
HAnimJoint1154 = x3d.HAnimJoint()
HAnimJoint1154.USE = "hanim_r_tarsal_distal_interphalangeal_2"

HAnimHumanoid31.joints.append(HAnimJoint1154)
HAnimJoint1155 = x3d.HAnimJoint()
HAnimJoint1155.USE = "hanim_r_cuneonavicular_3"

HAnimHumanoid31.joints.append(HAnimJoint1155)
HAnimJoint1156 = x3d.HAnimJoint()
HAnimJoint1156.USE = "hanim_r_tarsometatarsal_3"

HAnimHumanoid31.joints.append(HAnimJoint1156)
HAnimJoint1157 = x3d.HAnimJoint()
HAnimJoint1157.USE = "hanim_r_metatarsophalangeal_3"

HAnimHumanoid31.joints.append(HAnimJoint1157)
HAnimJoint1158 = x3d.HAnimJoint()
HAnimJoint1158.USE = "hanim_r_tarsal_proximal_interphalangeal_3"

HAnimHumanoid31.joints.append(HAnimJoint1158)
HAnimJoint1159 = x3d.HAnimJoint()
HAnimJoint1159.USE = "hanim_r_tarsal_distal_interphalangeal_3"

HAnimHumanoid31.joints.append(HAnimJoint1159)
HAnimJoint1160 = x3d.HAnimJoint()
HAnimJoint1160.USE = "hanim_r_calcaneocuboid"

HAnimHumanoid31.joints.append(HAnimJoint1160)
HAnimJoint1161 = x3d.HAnimJoint()
HAnimJoint1161.USE = "hanim_r_transversetarsal"

HAnimHumanoid31.joints.append(HAnimJoint1161)
HAnimJoint1162 = x3d.HAnimJoint()
HAnimJoint1162.USE = "hanim_r_tarsometatarsal_4"

HAnimHumanoid31.joints.append(HAnimJoint1162)
HAnimJoint1163 = x3d.HAnimJoint()
HAnimJoint1163.USE = "hanim_r_metatarsophalangeal_4"

HAnimHumanoid31.joints.append(HAnimJoint1163)
HAnimJoint1164 = x3d.HAnimJoint()
HAnimJoint1164.USE = "hanim_r_tarsal_proximal_interphalangeal_4"

HAnimHumanoid31.joints.append(HAnimJoint1164)
HAnimJoint1165 = x3d.HAnimJoint()
HAnimJoint1165.USE = "hanim_r_tarsal_distal_interphalangeal_4"

HAnimHumanoid31.joints.append(HAnimJoint1165)
HAnimJoint1166 = x3d.HAnimJoint()
HAnimJoint1166.USE = "hanim_r_tarsometatarsal_5"

HAnimHumanoid31.joints.append(HAnimJoint1166)
HAnimJoint1167 = x3d.HAnimJoint()
HAnimJoint1167.USE = "hanim_r_metatarsophalangeal_5"

HAnimHumanoid31.joints.append(HAnimJoint1167)
HAnimJoint1168 = x3d.HAnimJoint()
HAnimJoint1168.USE = "hanim_r_tarsal_proximal_interphalangeal_5"

HAnimHumanoid31.joints.append(HAnimJoint1168)
HAnimJoint1169 = x3d.HAnimJoint()
HAnimJoint1169.USE = "hanim_r_tarsal_distal_interphalangeal_5"

HAnimHumanoid31.joints.append(HAnimJoint1169)
HAnimJoint1170 = x3d.HAnimJoint()
HAnimJoint1170.USE = "hanim_vl5"

HAnimHumanoid31.joints.append(HAnimJoint1170)
HAnimJoint1171 = x3d.HAnimJoint()
HAnimJoint1171.USE = "hanim_vl4"

HAnimHumanoid31.joints.append(HAnimJoint1171)
HAnimJoint1172 = x3d.HAnimJoint()
HAnimJoint1172.USE = "hanim_vl3"

HAnimHumanoid31.joints.append(HAnimJoint1172)
HAnimJoint1173 = x3d.HAnimJoint()
HAnimJoint1173.USE = "hanim_vl2"

HAnimHumanoid31.joints.append(HAnimJoint1173)
HAnimJoint1174 = x3d.HAnimJoint()
HAnimJoint1174.USE = "hanim_vl1"

HAnimHumanoid31.joints.append(HAnimJoint1174)
HAnimJoint1175 = x3d.HAnimJoint()
HAnimJoint1175.USE = "hanim_vt12"

HAnimHumanoid31.joints.append(HAnimJoint1175)
HAnimJoint1176 = x3d.HAnimJoint()
HAnimJoint1176.USE = "hanim_vt11"

HAnimHumanoid31.joints.append(HAnimJoint1176)
HAnimJoint1177 = x3d.HAnimJoint()
HAnimJoint1177.USE = "hanim_vt10"

HAnimHumanoid31.joints.append(HAnimJoint1177)
HAnimJoint1178 = x3d.HAnimJoint()
HAnimJoint1178.USE = "hanim_vt9"

HAnimHumanoid31.joints.append(HAnimJoint1178)
HAnimJoint1179 = x3d.HAnimJoint()
HAnimJoint1179.USE = "hanim_vt8"

HAnimHumanoid31.joints.append(HAnimJoint1179)
HAnimJoint1180 = x3d.HAnimJoint()
HAnimJoint1180.USE = "hanim_vt7"

HAnimHumanoid31.joints.append(HAnimJoint1180)
HAnimJoint1181 = x3d.HAnimJoint()
HAnimJoint1181.USE = "hanim_vt6"

HAnimHumanoid31.joints.append(HAnimJoint1181)
HAnimJoint1182 = x3d.HAnimJoint()
HAnimJoint1182.USE = "hanim_vt5"

HAnimHumanoid31.joints.append(HAnimJoint1182)
HAnimJoint1183 = x3d.HAnimJoint()
HAnimJoint1183.USE = "hanim_vt4"

HAnimHumanoid31.joints.append(HAnimJoint1183)
HAnimJoint1184 = x3d.HAnimJoint()
HAnimJoint1184.USE = "hanim_vt3"

HAnimHumanoid31.joints.append(HAnimJoint1184)
HAnimJoint1185 = x3d.HAnimJoint()
HAnimJoint1185.USE = "hanim_vt2"

HAnimHumanoid31.joints.append(HAnimJoint1185)
HAnimJoint1186 = x3d.HAnimJoint()
HAnimJoint1186.USE = "hanim_vt1"

HAnimHumanoid31.joints.append(HAnimJoint1186)
HAnimJoint1187 = x3d.HAnimJoint()
HAnimJoint1187.USE = "hanim_vc7"

HAnimHumanoid31.joints.append(HAnimJoint1187)
HAnimJoint1188 = x3d.HAnimJoint()
HAnimJoint1188.USE = "hanim_vc6"

HAnimHumanoid31.joints.append(HAnimJoint1188)
HAnimJoint1189 = x3d.HAnimJoint()
HAnimJoint1189.USE = "hanim_vc5"

HAnimHumanoid31.joints.append(HAnimJoint1189)
HAnimJoint1190 = x3d.HAnimJoint()
HAnimJoint1190.USE = "hanim_vc4"

HAnimHumanoid31.joints.append(HAnimJoint1190)
HAnimJoint1191 = x3d.HAnimJoint()
HAnimJoint1191.USE = "hanim_vc3"

HAnimHumanoid31.joints.append(HAnimJoint1191)
HAnimJoint1192 = x3d.HAnimJoint()
HAnimJoint1192.USE = "hanim_vc2"

HAnimHumanoid31.joints.append(HAnimJoint1192)
HAnimJoint1193 = x3d.HAnimJoint()
HAnimJoint1193.USE = "hanim_vc1"

HAnimHumanoid31.joints.append(HAnimJoint1193)
HAnimJoint1194 = x3d.HAnimJoint()
HAnimJoint1194.USE = "hanim_skullbase"

HAnimHumanoid31.joints.append(HAnimJoint1194)
HAnimJoint1195 = x3d.HAnimJoint()
HAnimJoint1195.USE = "hanim_l_eyelid_joint"

HAnimHumanoid31.joints.append(HAnimJoint1195)
HAnimJoint1196 = x3d.HAnimJoint()
HAnimJoint1196.USE = "hanim_r_eyelid_joint"

HAnimHumanoid31.joints.append(HAnimJoint1196)
HAnimJoint1197 = x3d.HAnimJoint()
HAnimJoint1197.USE = "hanim_l_eyeball_joint"

HAnimHumanoid31.joints.append(HAnimJoint1197)
HAnimJoint1198 = x3d.HAnimJoint()
HAnimJoint1198.USE = "hanim_r_eyeball_joint"

HAnimHumanoid31.joints.append(HAnimJoint1198)
HAnimJoint1199 = x3d.HAnimJoint()
HAnimJoint1199.USE = "hanim_l_eyebrow_joint"

HAnimHumanoid31.joints.append(HAnimJoint1199)
HAnimJoint1200 = x3d.HAnimJoint()
HAnimJoint1200.USE = "hanim_r_eyebrow_joint"

HAnimHumanoid31.joints.append(HAnimJoint1200)
HAnimJoint1201 = x3d.HAnimJoint()
HAnimJoint1201.USE = "hanim_temporomandibular"

HAnimHumanoid31.joints.append(HAnimJoint1201)
HAnimJoint1202 = x3d.HAnimJoint()
HAnimJoint1202.USE = "hanim_l_sternoclavicular"

HAnimHumanoid31.joints.append(HAnimJoint1202)
HAnimJoint1203 = x3d.HAnimJoint()
HAnimJoint1203.USE = "hanim_l_acromioclavicular"

HAnimHumanoid31.joints.append(HAnimJoint1203)
HAnimJoint1204 = x3d.HAnimJoint()
HAnimJoint1204.USE = "hanim_l_shoulder"

HAnimHumanoid31.joints.append(HAnimJoint1204)
HAnimJoint1205 = x3d.HAnimJoint()
HAnimJoint1205.USE = "hanim_l_elbow"

HAnimHumanoid31.joints.append(HAnimJoint1205)
HAnimJoint1206 = x3d.HAnimJoint()
HAnimJoint1206.USE = "hanim_l_radiocarpal"

HAnimHumanoid31.joints.append(HAnimJoint1206)
HAnimJoint1207 = x3d.HAnimJoint()
HAnimJoint1207.USE = "hanim_l_midcarpal_1"

HAnimHumanoid31.joints.append(HAnimJoint1207)
HAnimJoint1208 = x3d.HAnimJoint()
HAnimJoint1208.USE = "hanim_l_carpometacarpal_1"

HAnimHumanoid31.joints.append(HAnimJoint1208)
HAnimJoint1209 = x3d.HAnimJoint()
HAnimJoint1209.USE = "hanim_l_metacarpophalangeal_1"

HAnimHumanoid31.joints.append(HAnimJoint1209)
HAnimJoint1210 = x3d.HAnimJoint()
HAnimJoint1210.USE = "hanim_l_carpal_interphalangeal_1"

HAnimHumanoid31.joints.append(HAnimJoint1210)
HAnimJoint1211 = x3d.HAnimJoint()
HAnimJoint1211.USE = "hanim_l_midcarpal_2"

HAnimHumanoid31.joints.append(HAnimJoint1211)
HAnimJoint1212 = x3d.HAnimJoint()
HAnimJoint1212.USE = "hanim_l_carpometacarpal_2"

HAnimHumanoid31.joints.append(HAnimJoint1212)
HAnimJoint1213 = x3d.HAnimJoint()
HAnimJoint1213.USE = "hanim_l_metacarpophalangeal_2"

HAnimHumanoid31.joints.append(HAnimJoint1213)
HAnimJoint1214 = x3d.HAnimJoint()
HAnimJoint1214.USE = "hanim_l_carpal_proximal_interphalangeal_2"

HAnimHumanoid31.joints.append(HAnimJoint1214)
HAnimJoint1215 = x3d.HAnimJoint()
HAnimJoint1215.USE = "hanim_l_carpal_distal_interphalangeal_2"

HAnimHumanoid31.joints.append(HAnimJoint1215)
HAnimJoint1216 = x3d.HAnimJoint()
HAnimJoint1216.USE = "hanim_l_midcarpal_3"

HAnimHumanoid31.joints.append(HAnimJoint1216)
HAnimJoint1217 = x3d.HAnimJoint()
HAnimJoint1217.USE = "hanim_l_carpometacarpal_3"

HAnimHumanoid31.joints.append(HAnimJoint1217)
HAnimJoint1218 = x3d.HAnimJoint()
HAnimJoint1218.USE = "hanim_l_metacarpophalangeal_3"

HAnimHumanoid31.joints.append(HAnimJoint1218)
HAnimJoint1219 = x3d.HAnimJoint()
HAnimJoint1219.USE = "hanim_l_carpal_proximal_interphalangeal_3"

HAnimHumanoid31.joints.append(HAnimJoint1219)
HAnimJoint1220 = x3d.HAnimJoint()
HAnimJoint1220.USE = "hanim_l_carpal_distal_interphalangeal_3"

HAnimHumanoid31.joints.append(HAnimJoint1220)
HAnimJoint1221 = x3d.HAnimJoint()
HAnimJoint1221.USE = "hanim_l_midcarpal_4_5"

HAnimHumanoid31.joints.append(HAnimJoint1221)
HAnimJoint1222 = x3d.HAnimJoint()
HAnimJoint1222.USE = "hanim_l_carpometacarpal_4"

HAnimHumanoid31.joints.append(HAnimJoint1222)
HAnimJoint1223 = x3d.HAnimJoint()
HAnimJoint1223.USE = "hanim_l_metacarpophalangeal_4"

HAnimHumanoid31.joints.append(HAnimJoint1223)
HAnimJoint1224 = x3d.HAnimJoint()
HAnimJoint1224.USE = "hanim_l_carpal_proximal_interphalangeal_4"

HAnimHumanoid31.joints.append(HAnimJoint1224)
HAnimJoint1225 = x3d.HAnimJoint()
HAnimJoint1225.USE = "hanim_l_carpal_distal_interphalangeal_4"

HAnimHumanoid31.joints.append(HAnimJoint1225)
HAnimJoint1226 = x3d.HAnimJoint()
HAnimJoint1226.USE = "hanim_l_carpometacarpal_5"

HAnimHumanoid31.joints.append(HAnimJoint1226)
HAnimJoint1227 = x3d.HAnimJoint()
HAnimJoint1227.USE = "hanim_l_metacarpophalangeal_5"

HAnimHumanoid31.joints.append(HAnimJoint1227)
HAnimJoint1228 = x3d.HAnimJoint()
HAnimJoint1228.USE = "hanim_l_carpal_proximal_interphalangeal_5"

HAnimHumanoid31.joints.append(HAnimJoint1228)
HAnimJoint1229 = x3d.HAnimJoint()
HAnimJoint1229.USE = "hanim_l_carpal_distal_interphalangeal_5"

HAnimHumanoid31.joints.append(HAnimJoint1229)
HAnimJoint1230 = x3d.HAnimJoint()
HAnimJoint1230.USE = "hanim_r_sternoclavicular"

HAnimHumanoid31.joints.append(HAnimJoint1230)
HAnimJoint1231 = x3d.HAnimJoint()
HAnimJoint1231.USE = "hanim_r_acromioclavicular"

HAnimHumanoid31.joints.append(HAnimJoint1231)
HAnimJoint1232 = x3d.HAnimJoint()
HAnimJoint1232.USE = "hanim_r_shoulder"

HAnimHumanoid31.joints.append(HAnimJoint1232)
HAnimJoint1233 = x3d.HAnimJoint()
HAnimJoint1233.USE = "hanim_r_elbow"

HAnimHumanoid31.joints.append(HAnimJoint1233)
HAnimJoint1234 = x3d.HAnimJoint()
HAnimJoint1234.USE = "hanim_r_radiocarpal"

HAnimHumanoid31.joints.append(HAnimJoint1234)
HAnimJoint1235 = x3d.HAnimJoint()
HAnimJoint1235.USE = "hanim_r_midcarpal_1"

HAnimHumanoid31.joints.append(HAnimJoint1235)
HAnimJoint1236 = x3d.HAnimJoint()
HAnimJoint1236.USE = "hanim_r_carpometacarpal_1"

HAnimHumanoid31.joints.append(HAnimJoint1236)
HAnimJoint1237 = x3d.HAnimJoint()
HAnimJoint1237.USE = "hanim_r_metacarpophalangeal_1"

HAnimHumanoid31.joints.append(HAnimJoint1237)
HAnimJoint1238 = x3d.HAnimJoint()
HAnimJoint1238.USE = "hanim_r_carpal_interphalangeal_1"

HAnimHumanoid31.joints.append(HAnimJoint1238)
HAnimJoint1239 = x3d.HAnimJoint()
HAnimJoint1239.USE = "hanim_r_midcarpal_2"

HAnimHumanoid31.joints.append(HAnimJoint1239)
HAnimJoint1240 = x3d.HAnimJoint()
HAnimJoint1240.USE = "hanim_r_carpometacarpal_2"

HAnimHumanoid31.joints.append(HAnimJoint1240)
HAnimJoint1241 = x3d.HAnimJoint()
HAnimJoint1241.USE = "hanim_r_metacarpophalangeal_2"

HAnimHumanoid31.joints.append(HAnimJoint1241)
HAnimJoint1242 = x3d.HAnimJoint()
HAnimJoint1242.USE = "hanim_r_carpal_proximal_interphalangeal_2"

HAnimHumanoid31.joints.append(HAnimJoint1242)
HAnimJoint1243 = x3d.HAnimJoint()
HAnimJoint1243.USE = "hanim_r_carpal_distal_interphalangeal_2"

HAnimHumanoid31.joints.append(HAnimJoint1243)
HAnimJoint1244 = x3d.HAnimJoint()
HAnimJoint1244.USE = "hanim_r_midcarpal_3"

HAnimHumanoid31.joints.append(HAnimJoint1244)
HAnimJoint1245 = x3d.HAnimJoint()
HAnimJoint1245.USE = "hanim_r_carpometacarpal_3"

HAnimHumanoid31.joints.append(HAnimJoint1245)
HAnimJoint1246 = x3d.HAnimJoint()
HAnimJoint1246.USE = "hanim_r_metacarpophalangeal_3"

HAnimHumanoid31.joints.append(HAnimJoint1246)
HAnimJoint1247 = x3d.HAnimJoint()
HAnimJoint1247.USE = "hanim_r_carpal_proximal_interphalangeal_3"

HAnimHumanoid31.joints.append(HAnimJoint1247)
HAnimJoint1248 = x3d.HAnimJoint()
HAnimJoint1248.USE = "hanim_r_carpal_distal_interphalangeal_3"

HAnimHumanoid31.joints.append(HAnimJoint1248)
HAnimJoint1249 = x3d.HAnimJoint()
HAnimJoint1249.USE = "hanim_r_midcarpal_4_5"

HAnimHumanoid31.joints.append(HAnimJoint1249)
HAnimJoint1250 = x3d.HAnimJoint()
HAnimJoint1250.USE = "hanim_r_carpometacarpal_4"

HAnimHumanoid31.joints.append(HAnimJoint1250)
HAnimJoint1251 = x3d.HAnimJoint()
HAnimJoint1251.USE = "hanim_r_metacarpophalangeal_4"

HAnimHumanoid31.joints.append(HAnimJoint1251)
HAnimJoint1252 = x3d.HAnimJoint()
HAnimJoint1252.USE = "hanim_r_carpal_proximal_interphalangeal_4"

HAnimHumanoid31.joints.append(HAnimJoint1252)
HAnimJoint1253 = x3d.HAnimJoint()
HAnimJoint1253.USE = "hanim_r_carpal_distal_interphalangeal_4"

HAnimHumanoid31.joints.append(HAnimJoint1253)
HAnimJoint1254 = x3d.HAnimJoint()
HAnimJoint1254.USE = "hanim_r_carpometacarpal_5"

HAnimHumanoid31.joints.append(HAnimJoint1254)
HAnimJoint1255 = x3d.HAnimJoint()
HAnimJoint1255.USE = "hanim_r_metacarpophalangeal_5"

HAnimHumanoid31.joints.append(HAnimJoint1255)
HAnimJoint1256 = x3d.HAnimJoint()
HAnimJoint1256.USE = "hanim_r_carpal_proximal_interphalangeal_5"

HAnimHumanoid31.joints.append(HAnimJoint1256)
HAnimJoint1257 = x3d.HAnimJoint()
HAnimJoint1257.USE = "hanim_r_carpal_distal_interphalangeal_5"

HAnimHumanoid31.joints.append(HAnimJoint1257)
HAnimSite1258 = x3d.HAnimSite()
HAnimSite1258.USE = "hanim_buttocks_standing_wall_contact_point_pt"

HAnimHumanoid31.sites.append(HAnimSite1258)
HAnimSite1259 = x3d.HAnimSite()
HAnimSite1259.USE = "hanim_crotch_pt"

HAnimHumanoid31.sites.append(HAnimSite1259)
HAnimSite1260 = x3d.HAnimSite()
HAnimSite1260.USE = "hanim_l_asis_pt"

HAnimHumanoid31.sites.append(HAnimSite1260)
HAnimSite1261 = x3d.HAnimSite()
HAnimSite1261.USE = "hanim_l_iliocristale_pt"

HAnimHumanoid31.sites.append(HAnimSite1261)
HAnimSite1262 = x3d.HAnimSite()
HAnimSite1262.USE = "hanim_l_psis_pt"

HAnimHumanoid31.sites.append(HAnimSite1262)
HAnimSite1263 = x3d.HAnimSite()
HAnimSite1263.USE = "hanim_l_trochanterion_pt"

HAnimHumanoid31.sites.append(HAnimSite1263)
HAnimSite1264 = x3d.HAnimSite()
HAnimSite1264.USE = "hanim_r_asis_pt"

HAnimHumanoid31.sites.append(HAnimSite1264)
HAnimSite1265 = x3d.HAnimSite()
HAnimSite1265.USE = "hanim_r_iliocristale_pt"

HAnimHumanoid31.sites.append(HAnimSite1265)
HAnimSite1266 = x3d.HAnimSite()
HAnimSite1266.USE = "hanim_r_psis_pt"

HAnimHumanoid31.sites.append(HAnimSite1266)
HAnimSite1267 = x3d.HAnimSite()
HAnimSite1267.USE = "hanim_r_trochanterion_pt"

HAnimHumanoid31.sites.append(HAnimSite1267)
HAnimSite1268 = x3d.HAnimSite()
HAnimSite1268.USE = "hanim_navel_pt"

HAnimHumanoid31.sites.append(HAnimSite1268)
HAnimSite1269 = x3d.HAnimSite()
HAnimSite1269.USE = "hanim_waist_preferred_anterior_pt"

HAnimHumanoid31.sites.append(HAnimSite1269)
HAnimSite1270 = x3d.HAnimSite()
HAnimSite1270.USE = "hanim_waist_preferred_posterior_pt"

HAnimHumanoid31.sites.append(HAnimSite1270)
HAnimSite1271 = x3d.HAnimSite()
HAnimSite1271.USE = "hanim_l_femoral_lateral_epicondyles_pt"

HAnimHumanoid31.sites.append(HAnimSite1271)
HAnimSite1272 = x3d.HAnimSite()
HAnimSite1272.USE = "hanim_l_femoral_medial_epicondyles_pt"

HAnimHumanoid31.sites.append(HAnimSite1272)
HAnimSite1273 = x3d.HAnimSite()
HAnimSite1273.USE = "hanim_l_knee_crease_pt"

HAnimHumanoid31.sites.append(HAnimSite1273)
HAnimSite1274 = x3d.HAnimSite()
HAnimSite1274.USE = "hanim_l_suprapatella_pt"

HAnimHumanoid31.sites.append(HAnimSite1274)
HAnimSite1275 = x3d.HAnimSite()
HAnimSite1275.USE = "hanim_r_femoral_lateral_epicondyles_pt"

HAnimHumanoid31.sites.append(HAnimSite1275)
HAnimSite1276 = x3d.HAnimSite()
HAnimSite1276.USE = "hanim_r_femoral_medial_epicondyles_pt"

HAnimHumanoid31.sites.append(HAnimSite1276)
HAnimSite1277 = x3d.HAnimSite()
HAnimSite1277.USE = "hanim_r_knee_crease_pt"

HAnimHumanoid31.sites.append(HAnimSite1277)
HAnimSite1278 = x3d.HAnimSite()
HAnimSite1278.USE = "hanim_r_suprapatella_pt"

HAnimHumanoid31.sites.append(HAnimSite1278)
HAnimSite1279 = x3d.HAnimSite()
HAnimSite1279.USE = "hanim_l_lateral_malleolus_pt"

HAnimHumanoid31.sites.append(HAnimSite1279)
HAnimSite1280 = x3d.HAnimSite()
HAnimSite1280.USE = "hanim_l_medial_malleolus_pt"

HAnimHumanoid31.sites.append(HAnimSite1280)
HAnimSite1281 = x3d.HAnimSite()
HAnimSite1281.USE = "hanim_l_tibiale_pt"

HAnimHumanoid31.sites.append(HAnimSite1281)
HAnimSite1282 = x3d.HAnimSite()
HAnimSite1282.USE = "hanim_l_calcaneus_posterior_pt"

HAnimHumanoid31.sites.append(HAnimSite1282)
HAnimSite1283 = x3d.HAnimSite()
HAnimSite1283.USE = "hanim_l_sphyrion_pt"

HAnimHumanoid31.sites.append(HAnimSite1283)
HAnimSite1284 = x3d.HAnimSite()
HAnimSite1284.USE = "hanim_l_metatarsal_phalanx_1_pt"

HAnimHumanoid31.sites.append(HAnimSite1284)
HAnimSite1285 = x3d.HAnimSite()
HAnimSite1285.USE = "hanim_l_tarsal_distal_phalanx_1_tip"

HAnimHumanoid31.sites.append(HAnimSite1285)
HAnimSite1286 = x3d.HAnimSite()
HAnimSite1286.USE = "hanim_l_tarsal_distal_phalanx_2_tip"

HAnimHumanoid31.sites.append(HAnimSite1286)
HAnimSite1287 = x3d.HAnimSite()
HAnimSite1287.USE = "hanim_l_tarsal_distal_phalanx_3_tip"

HAnimHumanoid31.sites.append(HAnimSite1287)
HAnimSite1288 = x3d.HAnimSite()
HAnimSite1288.USE = "hanim_l_tarsal_distal_phalanx_4_tip"

HAnimHumanoid31.sites.append(HAnimSite1288)
HAnimSite1289 = x3d.HAnimSite()
HAnimSite1289.USE = "hanim_l_metatarsal_phalanx_5_pt"

HAnimHumanoid31.sites.append(HAnimSite1289)
HAnimSite1290 = x3d.HAnimSite()
HAnimSite1290.USE = "hanim_l_tarsal_distal_phalanx_5_tip"

HAnimHumanoid31.sites.append(HAnimSite1290)
HAnimSite1291 = x3d.HAnimSite()
HAnimSite1291.USE = "hanim_r_lateral_malleolus_pt"

HAnimHumanoid31.sites.append(HAnimSite1291)
HAnimSite1292 = x3d.HAnimSite()
HAnimSite1292.USE = "hanim_r_medial_malleolus_pt"

HAnimHumanoid31.sites.append(HAnimSite1292)
HAnimSite1293 = x3d.HAnimSite()
HAnimSite1293.USE = "hanim_r_tibiale_pt"

HAnimHumanoid31.sites.append(HAnimSite1293)
HAnimSite1294 = x3d.HAnimSite()
HAnimSite1294.USE = "hanim_r_calcaneus_posterior_pt"

HAnimHumanoid31.sites.append(HAnimSite1294)
HAnimSite1295 = x3d.HAnimSite()
HAnimSite1295.USE = "hanim_r_sphyrion_pt"

HAnimHumanoid31.sites.append(HAnimSite1295)
HAnimSite1296 = x3d.HAnimSite()
HAnimSite1296.USE = "hanim_r_metatarsal_phalanx_1_pt"

HAnimHumanoid31.sites.append(HAnimSite1296)
HAnimSite1297 = x3d.HAnimSite()
HAnimSite1297.USE = "hanim_r_tarsal_distal_phalanx_1_tip"

HAnimHumanoid31.sites.append(HAnimSite1297)
HAnimSite1298 = x3d.HAnimSite()
HAnimSite1298.USE = "hanim_r_tarsal_distal_phalanx_2_tip"

HAnimHumanoid31.sites.append(HAnimSite1298)
HAnimSite1299 = x3d.HAnimSite()
HAnimSite1299.USE = "hanim_r_tarsal_distal_phalanx_3_tip"

HAnimHumanoid31.sites.append(HAnimSite1299)
HAnimSite1300 = x3d.HAnimSite()
HAnimSite1300.USE = "hanim_r_tarsal_distal_phalanx_4_tip"

HAnimHumanoid31.sites.append(HAnimSite1300)
HAnimSite1301 = x3d.HAnimSite()
HAnimSite1301.USE = "hanim_r_metatarsal_phalanx_5_pt"

HAnimHumanoid31.sites.append(HAnimSite1301)
HAnimSite1302 = x3d.HAnimSite()
HAnimSite1302.USE = "hanim_r_tarsal_distal_phalanx_5_tip"

HAnimHumanoid31.sites.append(HAnimSite1302)
HAnimSite1303 = x3d.HAnimSite()
HAnimSite1303.USE = "hanim_l_rib10_pt"

HAnimHumanoid31.sites.append(HAnimSite1303)
HAnimSite1304 = x3d.HAnimSite()
HAnimSite1304.USE = "hanim_r_rib10_pt"

HAnimHumanoid31.sites.append(HAnimSite1304)
HAnimSite1305 = x3d.HAnimSite()
HAnimSite1305.USE = "hanim_spine_2_middle_back_pt"

HAnimHumanoid31.sites.append(HAnimSite1305)
HAnimSite1306 = x3d.HAnimSite()
HAnimSite1306.USE = "hanim_substernale_pt"

HAnimHumanoid31.sites.append(HAnimSite1306)
HAnimSite1307 = x3d.HAnimSite()
HAnimSite1307.USE = "hanim_l_thelion_pt"

HAnimHumanoid31.sites.append(HAnimSite1307)
HAnimSite1308 = x3d.HAnimSite()
HAnimSite1308.USE = "hanim_r_thelion_pt"

HAnimHumanoid31.sites.append(HAnimSite1308)
HAnimSite1309 = x3d.HAnimSite()
HAnimSite1309.USE = "hanim_l_chest_midsagittal_plane_pt"

HAnimHumanoid31.sites.append(HAnimSite1309)
HAnimSite1310 = x3d.HAnimSite()
HAnimSite1310.USE = "hanim_mesosternale_pt"

HAnimHumanoid31.sites.append(HAnimSite1310)
HAnimSite1311 = x3d.HAnimSite()
HAnimSite1311.USE = "hanim_r_chest_midsagittal_plane_pt"

HAnimHumanoid31.sites.append(HAnimSite1311)
HAnimSite1312 = x3d.HAnimSite()
HAnimSite1312.USE = "hanim_rear_center_midsagittal_plane_pt"

HAnimHumanoid31.sites.append(HAnimSite1312)
HAnimSite1313 = x3d.HAnimSite()
HAnimSite1313.USE = "hanim_spine_1_middle_back_pt"

HAnimHumanoid31.sites.append(HAnimSite1313)
HAnimSite1314 = x3d.HAnimSite()
HAnimSite1314.USE = "hanim_cervicale_pt"

HAnimHumanoid31.sites.append(HAnimSite1314)
HAnimSite1315 = x3d.HAnimSite()
HAnimSite1315.USE = "hanim_suprasternale_pt"

HAnimHumanoid31.sites.append(HAnimSite1315)
HAnimSite1316 = x3d.HAnimSite()
HAnimSite1316.USE = "hanim_l_neck_base_pt"

HAnimHumanoid31.sites.append(HAnimSite1316)
HAnimSite1317 = x3d.HAnimSite()
HAnimSite1317.USE = "hanim_r_neck_base_pt"

HAnimHumanoid31.sites.append(HAnimSite1317)
HAnimSite1318 = x3d.HAnimSite()
HAnimSite1318.USE = "hanim_l_acromion_pt"

HAnimHumanoid31.sites.append(HAnimSite1318)
HAnimSite1319 = x3d.HAnimSite()
HAnimSite1319.USE = "hanim_l_axilla_distal_pt"

HAnimHumanoid31.sites.append(HAnimSite1319)
HAnimSite1320 = x3d.HAnimSite()
HAnimSite1320.USE = "hanim_l_axilla_posterior_folds_pt"

HAnimHumanoid31.sites.append(HAnimSite1320)
HAnimSite1321 = x3d.HAnimSite()
HAnimSite1321.USE = "hanim_l_axilla_proximal_pt"

HAnimHumanoid31.sites.append(HAnimSite1321)
HAnimSite1322 = x3d.HAnimSite()
HAnimSite1322.USE = "hanim_l_clavicale_pt"

HAnimHumanoid31.sites.append(HAnimSite1322)
HAnimSite1323 = x3d.HAnimSite()
HAnimSite1323.USE = "hanim_r_acromion_pt"

HAnimHumanoid31.sites.append(HAnimSite1323)
HAnimSite1324 = x3d.HAnimSite()
HAnimSite1324.USE = "hanim_r_axilla_distal_pt"

HAnimHumanoid31.sites.append(HAnimSite1324)
HAnimSite1325 = x3d.HAnimSite()
HAnimSite1325.USE = "hanim_r_axilla_posterior_folds_pt"

HAnimHumanoid31.sites.append(HAnimSite1325)
HAnimSite1326 = x3d.HAnimSite()
HAnimSite1326.USE = "hanim_r_axilla_proximal_pt"

HAnimHumanoid31.sites.append(HAnimSite1326)
HAnimSite1327 = x3d.HAnimSite()
HAnimSite1327.USE = "hanim_r_clavicale_pt"

HAnimHumanoid31.sites.append(HAnimSite1327)
HAnimSite1328 = x3d.HAnimSite()
HAnimSite1328.USE = "hanim_adams_apple_pt"

HAnimHumanoid31.sites.append(HAnimSite1328)
HAnimSite1329 = x3d.HAnimSite()
HAnimSite1329.USE = "hanim_glabella_pt"

HAnimHumanoid31.sites.append(HAnimSite1329)
HAnimSite1330 = x3d.HAnimSite()
HAnimSite1330.USE = "hanim_l_ectocanthus_pt"

HAnimHumanoid31.sites.append(HAnimSite1330)
HAnimSite1331 = x3d.HAnimSite()
HAnimSite1331.USE = "hanim_l_infraorbitale_pt"

HAnimHumanoid31.sites.append(HAnimSite1331)
HAnimSite1332 = x3d.HAnimSite()
HAnimSite1332.USE = "hanim_l_tragion_pt"

HAnimHumanoid31.sites.append(HAnimSite1332)
HAnimSite1333 = x3d.HAnimSite()
HAnimSite1333.USE = "hanim_nuchale_pt"

HAnimHumanoid31.sites.append(HAnimSite1333)
HAnimSite1334 = x3d.HAnimSite()
HAnimSite1334.USE = "hanim_opisthocranion_pt"

HAnimHumanoid31.sites.append(HAnimSite1334)
HAnimSite1335 = x3d.HAnimSite()
HAnimSite1335.USE = "hanim_r_ectocanthus_pt"

HAnimHumanoid31.sites.append(HAnimSite1335)
HAnimSite1336 = x3d.HAnimSite()
HAnimSite1336.USE = "hanim_r_infraorbitale_pt"

HAnimHumanoid31.sites.append(HAnimSite1336)
HAnimSite1337 = x3d.HAnimSite()
HAnimSite1337.USE = "hanim_r_tragion_pt"

HAnimHumanoid31.sites.append(HAnimSite1337)
HAnimSite1338 = x3d.HAnimSite()
HAnimSite1338.USE = "hanim_sellion_pt"

HAnimHumanoid31.sites.append(HAnimSite1338)
HAnimSite1339 = x3d.HAnimSite()
HAnimSite1339.USE = "hanim_skull_vertex_pt"

HAnimHumanoid31.sites.append(HAnimSite1339)
HAnimSite1340 = x3d.HAnimSite()
HAnimSite1340.USE = "hanim_l_gonion_pt"

HAnimHumanoid31.sites.append(HAnimSite1340)
HAnimSite1341 = x3d.HAnimSite()
HAnimSite1341.USE = "hanim_menton_pt"

HAnimHumanoid31.sites.append(HAnimSite1341)
HAnimSite1342 = x3d.HAnimSite()
HAnimSite1342.USE = "hanim_r_gonion_pt"

HAnimHumanoid31.sites.append(HAnimSite1342)
HAnimSite1343 = x3d.HAnimSite()
HAnimSite1343.USE = "hanim_supramenton_pt"

HAnimHumanoid31.sites.append(HAnimSite1343)
HAnimSite1344 = x3d.HAnimSite()
HAnimSite1344.USE = "hanim_l_bideltoid_pt"

HAnimHumanoid31.sites.append(HAnimSite1344)
HAnimSite1345 = x3d.HAnimSite()
HAnimSite1345.USE = "hanim_l_humeral_lateral_epicondyles_pt"

HAnimHumanoid31.sites.append(HAnimSite1345)
HAnimSite1346 = x3d.HAnimSite()
HAnimSite1346.USE = "hanim_l_humeral_medial_epicondyles_pt"

HAnimHumanoid31.sites.append(HAnimSite1346)
HAnimSite1347 = x3d.HAnimSite()
HAnimSite1347.USE = "hanim_l_olecranon_pt"

HAnimHumanoid31.sites.append(HAnimSite1347)
HAnimSite1348 = x3d.HAnimSite()
HAnimSite1348.USE = "hanim_l_radial_styloid_pt"

HAnimHumanoid31.sites.append(HAnimSite1348)
HAnimSite1349 = x3d.HAnimSite()
HAnimSite1349.USE = "hanim_l_radiale_pt"

HAnimHumanoid31.sites.append(HAnimSite1349)
HAnimSite1350 = x3d.HAnimSite()
HAnimSite1350.USE = "hanim_l_ulnar_styloid_pt"

HAnimHumanoid31.sites.append(HAnimSite1350)
HAnimSite1351 = x3d.HAnimSite()
HAnimSite1351.USE = "hanim_l_carpal_distal_phalanx_1_tip"

HAnimHumanoid31.sites.append(HAnimSite1351)
HAnimSite1352 = x3d.HAnimSite()
HAnimSite1352.USE = "hanim_l_metacarpal_phalanx_2_pt"

HAnimHumanoid31.sites.append(HAnimSite1352)
HAnimSite1353 = x3d.HAnimSite()
HAnimSite1353.USE = "hanim_l_carpal_distal_phalanx_2_tip"

HAnimHumanoid31.sites.append(HAnimSite1353)
HAnimSite1354 = x3d.HAnimSite()
HAnimSite1354.USE = "hanim_l_dactylion_pt"

HAnimHumanoid31.sites.append(HAnimSite1354)
HAnimSite1355 = x3d.HAnimSite()
HAnimSite1355.USE = "hanim_l_metacarpal_phalanx_3_pt"

HAnimHumanoid31.sites.append(HAnimSite1355)
HAnimSite1356 = x3d.HAnimSite()
HAnimSite1356.USE = "hanim_l_carpal_distal_phalanx_3_tip"

HAnimHumanoid31.sites.append(HAnimSite1356)
HAnimSite1357 = x3d.HAnimSite()
HAnimSite1357.USE = "hanim_l_metacarpal_phalanx_5_pt"

HAnimHumanoid31.sites.append(HAnimSite1357)
HAnimSite1358 = x3d.HAnimSite()
HAnimSite1358.USE = "hanim_l_carpal_distal_phalanx_4_tip"

HAnimHumanoid31.sites.append(HAnimSite1358)
HAnimSite1359 = x3d.HAnimSite()
HAnimSite1359.USE = "hanim_l_carpal_distal_phalanx_5_tip"

HAnimHumanoid31.sites.append(HAnimSite1359)
HAnimSite1360 = x3d.HAnimSite()
HAnimSite1360.USE = "hanim_r_bideltoid_pt"

HAnimHumanoid31.sites.append(HAnimSite1360)
HAnimSite1361 = x3d.HAnimSite()
HAnimSite1361.USE = "hanim_r_humeral_lateral_epicondyles_pt"

HAnimHumanoid31.sites.append(HAnimSite1361)
HAnimSite1362 = x3d.HAnimSite()
HAnimSite1362.USE = "hanim_r_humeral_medial_epicondyles_pt"

HAnimHumanoid31.sites.append(HAnimSite1362)
HAnimSite1363 = x3d.HAnimSite()
HAnimSite1363.USE = "hanim_r_olecranon_pt"

HAnimHumanoid31.sites.append(HAnimSite1363)
HAnimSite1364 = x3d.HAnimSite()
HAnimSite1364.USE = "hanim_r_radial_styloid_pt"

HAnimHumanoid31.sites.append(HAnimSite1364)
HAnimSite1365 = x3d.HAnimSite()
HAnimSite1365.USE = "hanim_r_radiale_pt"

HAnimHumanoid31.sites.append(HAnimSite1365)
HAnimSite1366 = x3d.HAnimSite()
HAnimSite1366.USE = "hanim_r_ulnar_styloid_pt"

HAnimHumanoid31.sites.append(HAnimSite1366)
HAnimSite1367 = x3d.HAnimSite()
HAnimSite1367.USE = "hanim_r_carpal_distal_phalanx_1_tip"

HAnimHumanoid31.sites.append(HAnimSite1367)
HAnimSite1368 = x3d.HAnimSite()
HAnimSite1368.USE = "hanim_r_metacarpal_phalanx_2_pt"

HAnimHumanoid31.sites.append(HAnimSite1368)
HAnimSite1369 = x3d.HAnimSite()
HAnimSite1369.USE = "hanim_r_carpal_distal_phalanx_2_tip"

HAnimHumanoid31.sites.append(HAnimSite1369)
HAnimSite1370 = x3d.HAnimSite()
HAnimSite1370.USE = "hanim_r_dactylion_pt"

HAnimHumanoid31.sites.append(HAnimSite1370)
HAnimSite1371 = x3d.HAnimSite()
HAnimSite1371.USE = "hanim_r_metacarpal_phalanx_3_pt"

HAnimHumanoid31.sites.append(HAnimSite1371)
HAnimSite1372 = x3d.HAnimSite()
HAnimSite1372.USE = "hanim_r_carpal_distal_phalanx_3_tip"

HAnimHumanoid31.sites.append(HAnimSite1372)
HAnimSite1373 = x3d.HAnimSite()
HAnimSite1373.USE = "hanim_r_metacarpal_phalanx_5_pt"

HAnimHumanoid31.sites.append(HAnimSite1373)
HAnimSite1374 = x3d.HAnimSite()
HAnimSite1374.USE = "hanim_r_carpal_distal_phalanx_4_tip"

HAnimHumanoid31.sites.append(HAnimSite1374)
HAnimSite1375 = x3d.HAnimSite()
HAnimSite1375.USE = "hanim_r_carpal_distal_phalanx_5_tip"

HAnimHumanoid31.sites.append(HAnimSite1375)

Scene11.children.append(HAnimHumanoid31)

X3D0.Scene = Scene11
f = open("././JohnJoint3_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
