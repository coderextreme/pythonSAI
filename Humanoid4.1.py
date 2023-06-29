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
Coordinate15.point = (0.0000,0.0000,0.0000,0.1000,0.0000,0.0000,0.0000,0.1000,0.0000,0.0000,0.0000,0.1000)

IndexedLineSet14.coord = Coordinate15
Color16 = x3d.Color()
Color16.color = [1,0,0,0,0.6,0,0,0,1]

IndexedLineSet14.color = Color16

Shape13.geometry = IndexedLineSet14

Transform12.children.append(Shape13)

Scene11.children.append(Transform12)
Group17 = x3d.Group()
#DEFS for markers of skeleton joints, segments, and sites
Transform18 = x3d.Transform()
Transform19 = x3d.Transform()
Transform19.translation = [0,2,0]
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
Shape30 = x3d.Shape()
Shape30.DEF = "HAnimSegmentLine"
LineSet31 = x3d.LineSet()
LineSet31.vertexCount = [2]
ColorRGBA32 = x3d.ColorRGBA()
ColorRGBA32.DEF = "HAnimSegmentLineColorRGBA"
ColorRGBA32.color = [1,1,0,1,1,1,0,0.1]

LineSet31.color = ColorRGBA32
Coordinate33 = x3d.Coordinate()
Coordinate33.point = (-0.0500,0.0000,0.0000,0.0500,0.0000,0.0000)

LineSet31.coord = Coordinate33

Shape30.geometry = LineSet31

Transform29.children.append(Shape30)

Transform18.children.append(Transform29)
Transform34 = x3d.Transform()
Transform34.translation = [0,2.1,0]
Shape35 = x3d.Shape()
Shape35.DEF = "HAnimSiteShape"
IndexedFaceSet36 = x3d.IndexedFaceSet()
IndexedFaceSet36.DEF = "DiamondIFS"
IndexedFaceSet36.creaseAngle = 0.5
IndexedFaceSet36.solid = False
IndexedFaceSet36.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
ColorRGBA37 = x3d.ColorRGBA()
ColorRGBA37.DEF = "HAnimSiteColorRGBA"
ColorRGBA37.color = [1,1,0,1,1,1,0,0.1,1,1,0,1,1,1,0,0.1,1,1,0,1,1,1,0,0.1]

IndexedFaceSet36.color = ColorRGBA37
Coordinate38 = x3d.Coordinate()
Coordinate38.point = (0.0000,0.0100,0.0000,-0.0100,0.0000,0.0000,0.0000,0.0000,0.0100,0.0100,0.0000,0.0000,0.0000,0.0000,-0.0100,0.0000,-0.0100,0.0000)

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

Scene11.children.append(Group17)
NavigationInfo41 = x3d.NavigationInfo()
NavigationInfo41.speed = 1.5

Scene11.children.append(NavigationInfo41)
Viewpoint42 = x3d.Viewpoint()
Viewpoint42.description = "default"

Scene11.children.append(Viewpoint42)
HAnimHumanoid43 = x3d.HAnimHumanoid()
HAnimHumanoid43.name = "HAnim"
HAnimHumanoid43.DEF = "hanim_HAnim"
HAnimHumanoid43.info = ["humanoidVersion=2.0"]
HAnimHumanoid43.version = "2.0"
HAnimJoint44 = x3d.HAnimJoint()
HAnimJoint44.name = "humanoid_root"
HAnimJoint44.DEF = "hanim_humanoid_root"
HAnimJoint44.center = [0,0.824,0.0277]
HAnimJoint44.ulimit = [0,0,0]
HAnimJoint44.llimit = [0,0,0]
HAnimSegment45 = x3d.HAnimSegment()
HAnimSegment45.name = "sacrum"
HAnimSegment45.DEF = "hanim_sacrum"
Transform46 = x3d.Transform()
Transform46.translation = [0,0.824,0.0277]
Transform47 = x3d.Transform()
#Empty Transform
Shape48 = x3d.Shape()
Shape48.USE = "HAnimJointShape"

Transform47.children.append(Shape48)

Transform46.children.append(Transform47)

HAnimSegment45.children.append(Transform46)
Shape49 = x3d.Shape()
LineSet50 = x3d.LineSet()
LineSet50.vertexCount = [2]
Coordinate51 = x3d.Coordinate()
Coordinate51.point = (0.0000,0.8240,0.0277,0.0000,0.9149,0.0016)

LineSet50.coord = Coordinate51
#from humanoid_root to sacroiliac vertices 2
ColorRGBA52 = x3d.ColorRGBA()
ColorRGBA52.USE = "HAnimSegmentLineColorRGBA"

LineSet50.color = ColorRGBA52

Shape49.geometry = LineSet50

HAnimSegment45.children.append(Shape49)
HAnimSite53 = x3d.HAnimSite()
HAnimSite53.name = "buttocks_standing_wall_contact_point_pt"
HAnimSite53.DEF = "hanim_buttocks_standing_wall_contact_point_pt"
TouchSensor54 = x3d.TouchSensor()
TouchSensor54.description = "HAnimSite buttocks_standing_wall_contact_point_pt"

HAnimSite53.children.append(TouchSensor54)
Shape55 = x3d.Shape()
Shape55.USE = "HAnimSiteShape"

HAnimSite53.children.append(Shape55)

HAnimSegment45.children.append(HAnimSite53)
HAnimSite56 = x3d.HAnimSite()
HAnimSite56.name = "crotch_pt"
HAnimSite56.DEF = "hanim_crotch_pt"
HAnimSite56.translation = [0.0034,0.8266,0.0257]
TouchSensor57 = x3d.TouchSensor()
TouchSensor57.description = "HAnimSite crotch_pt"

HAnimSite56.children.append(TouchSensor57)
Shape58 = x3d.Shape()
Shape58.USE = "HAnimSiteShape"

HAnimSite56.children.append(Shape58)

HAnimSegment45.children.append(HAnimSite56)
HAnimSite59 = x3d.HAnimSite()
HAnimSite59.name = "l_asis_pt"
HAnimSite59.DEF = "hanim_l_asis_pt"
HAnimSite59.translation = [0.0925,0.9983,0.1052]
TouchSensor60 = x3d.TouchSensor()
TouchSensor60.description = "HAnimSite l_asis_pt"

HAnimSite59.children.append(TouchSensor60)
Shape61 = x3d.Shape()
Shape61.USE = "HAnimSiteShape"

HAnimSite59.children.append(Shape61)

HAnimSegment45.children.append(HAnimSite59)
HAnimSite62 = x3d.HAnimSite()
HAnimSite62.name = "l_iliocristale_pt"
HAnimSite62.DEF = "hanim_l_iliocristale_pt"
HAnimSite62.translation = [0.1612,1.0537,0.0008]
TouchSensor63 = x3d.TouchSensor()
TouchSensor63.description = "HAnimSite l_iliocristale_pt"

HAnimSite62.children.append(TouchSensor63)
Shape64 = x3d.Shape()
Shape64.USE = "HAnimSiteShape"

HAnimSite62.children.append(Shape64)

HAnimSegment45.children.append(HAnimSite62)
HAnimSite65 = x3d.HAnimSite()
HAnimSite65.name = "l_psis_pt"
HAnimSite65.DEF = "hanim_l_psis_pt"
HAnimSite65.translation = [0.0774,1.019,-0.1151]
TouchSensor66 = x3d.TouchSensor()
TouchSensor66.description = "HAnimSite l_psis_pt"

HAnimSite65.children.append(TouchSensor66)
Shape67 = x3d.Shape()
Shape67.USE = "HAnimSiteShape"

HAnimSite65.children.append(Shape67)

HAnimSegment45.children.append(HAnimSite65)
HAnimSite68 = x3d.HAnimSite()
HAnimSite68.name = "l_trochanterion_pt"
HAnimSite68.DEF = "hanim_l_trochanterion_pt"
HAnimSite68.translation = [0.1677,0.8336,0.0303]
TouchSensor69 = x3d.TouchSensor()
TouchSensor69.description = "HAnimSite l_trochanterion_pt"

HAnimSite68.children.append(TouchSensor69)
Shape70 = x3d.Shape()
Shape70.USE = "HAnimSiteShape"

HAnimSite68.children.append(Shape70)

HAnimSegment45.children.append(HAnimSite68)
HAnimSite71 = x3d.HAnimSite()
HAnimSite71.name = "r_asis_pt"
HAnimSite71.DEF = "hanim_r_asis_pt"
HAnimSite71.translation = [-0.0887,1.0021,0.1112]
TouchSensor72 = x3d.TouchSensor()
TouchSensor72.description = "HAnimSite r_asis_pt"

HAnimSite71.children.append(TouchSensor72)
Shape73 = x3d.Shape()
Shape73.USE = "HAnimSiteShape"

HAnimSite71.children.append(Shape73)

HAnimSegment45.children.append(HAnimSite71)
HAnimSite74 = x3d.HAnimSite()
HAnimSite74.name = "r_iliocristale_pt"
HAnimSite74.DEF = "hanim_r_iliocristale_pt"
HAnimSite74.translation = [-0.1525,1.0628,0.0035]
TouchSensor75 = x3d.TouchSensor()
TouchSensor75.description = "HAnimSite r_iliocristale_pt"

HAnimSite74.children.append(TouchSensor75)
Shape76 = x3d.Shape()
Shape76.USE = "HAnimSiteShape"

HAnimSite74.children.append(Shape76)

HAnimSegment45.children.append(HAnimSite74)
HAnimSite77 = x3d.HAnimSite()
HAnimSite77.name = "r_psis_pt"
HAnimSite77.DEF = "hanim_r_psis_pt"
HAnimSite77.translation = [-0.0716,1.019,-0.1138]
TouchSensor78 = x3d.TouchSensor()
TouchSensor78.description = "HAnimSite r_psis_pt"

HAnimSite77.children.append(TouchSensor78)
Shape79 = x3d.Shape()
Shape79.USE = "HAnimSiteShape"

HAnimSite77.children.append(Shape79)

HAnimSegment45.children.append(HAnimSite77)
HAnimSite80 = x3d.HAnimSite()
HAnimSite80.name = "r_trochanterion_pt"
HAnimSite80.DEF = "hanim_r_trochanterion_pt"
HAnimSite80.translation = [-0.1689,0.8419,0.0352]
TouchSensor81 = x3d.TouchSensor()
TouchSensor81.description = "HAnimSite r_trochanterion_pt"

HAnimSite80.children.append(TouchSensor81)
Shape82 = x3d.Shape()
Shape82.USE = "HAnimSiteShape"

HAnimSite80.children.append(Shape82)

HAnimSegment45.children.append(HAnimSite80)
Shape83 = x3d.Shape()
LineSet84 = x3d.LineSet()
LineSet84.vertexCount = [2]
Coordinate85 = x3d.Coordinate()
Coordinate85.point = (0.0000,0.8240,0.0277,0.0028,1.0568,-0.0776)

LineSet84.coord = Coordinate85
#from humanoid_root to vl5 vertices 2
ColorRGBA86 = x3d.ColorRGBA()
ColorRGBA86.USE = "HAnimSegmentLineColorRGBA"

LineSet84.color = ColorRGBA86

Shape83.geometry = LineSet84

HAnimSegment45.children.append(Shape83)
HAnimSite87 = x3d.HAnimSite()
HAnimSite87.name = "navel_pt"
HAnimSite87.DEF = "hanim_navel_pt"
HAnimSite87.translation = [0.0069,1.0966,0.1017]
TouchSensor88 = x3d.TouchSensor()
TouchSensor88.description = "HAnimSite navel_pt"

HAnimSite87.children.append(TouchSensor88)
Shape89 = x3d.Shape()
Shape89.USE = "HAnimSiteShape"

HAnimSite87.children.append(Shape89)

HAnimSegment45.children.append(HAnimSite87)
HAnimSite90 = x3d.HAnimSite()
HAnimSite90.name = "waist_preferred_anterior_pt"
HAnimSite90.DEF = "hanim_waist_preferred_anterior_pt"
TouchSensor91 = x3d.TouchSensor()
TouchSensor91.description = "HAnimSite waist_preferred_anterior_pt"

HAnimSite90.children.append(TouchSensor91)
Shape92 = x3d.Shape()
Shape92.USE = "HAnimSiteShape"

HAnimSite90.children.append(Shape92)

HAnimSegment45.children.append(HAnimSite90)
HAnimSite93 = x3d.HAnimSite()
HAnimSite93.name = "waist_preferred_posterior_pt"
HAnimSite93.DEF = "hanim_waist_preferred_posterior_pt"
HAnimSite93.translation = [0.29,1.0915,-0.1091]
TouchSensor94 = x3d.TouchSensor()
TouchSensor94.description = "HAnimSite waist_preferred_posterior_pt"

HAnimSite93.children.append(TouchSensor94)
Shape95 = x3d.Shape()
Shape95.USE = "HAnimSiteShape"

HAnimSite93.children.append(Shape95)

HAnimSegment45.children.append(HAnimSite93)

HAnimJoint44.children.append(HAnimSegment45)
HAnimJoint96 = x3d.HAnimJoint()
HAnimJoint96.name = "sacroiliac"
HAnimJoint96.DEF = "hanim_sacroiliac"
HAnimJoint96.center = [0,0.9149,0.0016]
HAnimJoint96.ulimit = [0,0,0]
HAnimJoint96.llimit = [0,0,0]
HAnimSegment97 = x3d.HAnimSegment()
HAnimSegment97.name = "pelvis"
HAnimSegment97.DEF = "hanim_pelvis"
Transform98 = x3d.Transform()
Transform98.translation = [0,0.9149,0.0016]
Transform99 = x3d.Transform()
#Empty Transform
Shape100 = x3d.Shape()
Shape100.USE = "HAnimJointShape"

Transform99.children.append(Shape100)

Transform98.children.append(Transform99)

HAnimSegment97.children.append(Transform98)
Shape101 = x3d.Shape()
LineSet102 = x3d.LineSet()
LineSet102.vertexCount = [2]
Coordinate103 = x3d.Coordinate()
Coordinate103.point = (0.0000,0.9149,0.0016,0.0961,0.9124,-0.0001)

LineSet102.coord = Coordinate103
#from sacroiliac to l_hip vertices 2
ColorRGBA104 = x3d.ColorRGBA()
ColorRGBA104.USE = "HAnimSegmentLineColorRGBA"

LineSet102.color = ColorRGBA104

Shape101.geometry = LineSet102

HAnimSegment97.children.append(Shape101)
HAnimSite105 = x3d.HAnimSite()
HAnimSite105.name = "l_femoral_lateral_epicondyles_pt"
HAnimSite105.DEF = "hanim_l_femoral_lateral_epicondyles_pt"
HAnimSite105.translation = [0.1598,0.4967,0.0297]
TouchSensor106 = x3d.TouchSensor()
TouchSensor106.description = "HAnimSite l_femoral_lateral_epicondyles_pt"

HAnimSite105.children.append(TouchSensor106)
Shape107 = x3d.Shape()
Shape107.USE = "HAnimSiteShape"

HAnimSite105.children.append(Shape107)

HAnimSegment97.children.append(HAnimSite105)
HAnimSite108 = x3d.HAnimSite()
HAnimSite108.name = "l_femoral_medial_epicondyles_pt"
HAnimSite108.DEF = "hanim_l_femoral_medial_epicondyles_pt"
HAnimSite108.translation = [0.0398,0.4946,0.0303]
TouchSensor109 = x3d.TouchSensor()
TouchSensor109.description = "HAnimSite l_femoral_medial_epicondyles_pt"

HAnimSite108.children.append(TouchSensor109)
Shape110 = x3d.Shape()
Shape110.USE = "HAnimSiteShape"

HAnimSite108.children.append(Shape110)

HAnimSegment97.children.append(HAnimSite108)
HAnimSite111 = x3d.HAnimSite()
HAnimSite111.name = "l_knee_crease_pt"
HAnimSite111.DEF = "hanim_l_knee_crease_pt"
HAnimSite111.translation = [0.0993,0.4881,-0.0309]
TouchSensor112 = x3d.TouchSensor()
TouchSensor112.description = "HAnimSite l_knee_crease_pt"

HAnimSite111.children.append(TouchSensor112)
Shape113 = x3d.Shape()
Shape113.USE = "HAnimSiteShape"

HAnimSite111.children.append(Shape113)

HAnimSegment97.children.append(HAnimSite111)
HAnimSite114 = x3d.HAnimSite()
HAnimSite114.name = "l_suprapatella_pt"
HAnimSite114.DEF = "hanim_l_suprapatella_pt"
TouchSensor115 = x3d.TouchSensor()
TouchSensor115.description = "HAnimSite l_suprapatella_pt"

HAnimSite114.children.append(TouchSensor115)
Shape116 = x3d.Shape()
Shape116.USE = "HAnimSiteShape"

HAnimSite114.children.append(Shape116)

HAnimSegment97.children.append(HAnimSite114)
Shape117 = x3d.Shape()
LineSet118 = x3d.LineSet()
LineSet118.vertexCount = [2]
Coordinate119 = x3d.Coordinate()
Coordinate119.point = (0.0000,0.9149,0.0016,-0.0950,0.9171,0.0029)

LineSet118.coord = Coordinate119
#from sacroiliac to r_hip vertices 2
ColorRGBA120 = x3d.ColorRGBA()
ColorRGBA120.USE = "HAnimSegmentLineColorRGBA"

LineSet118.color = ColorRGBA120

Shape117.geometry = LineSet118

HAnimSegment97.children.append(Shape117)
HAnimSite121 = x3d.HAnimSite()
HAnimSite121.name = "r_femoral_lateral_epicondyles_pt"
HAnimSite121.DEF = "hanim_r_femoral_lateral_epicondyles_pt"
HAnimSite121.translation = [-0.1421,0.4992,0.031]
TouchSensor122 = x3d.TouchSensor()
TouchSensor122.description = "HAnimSite r_femoral_lateral_epicondyles_pt"

HAnimSite121.children.append(TouchSensor122)
Shape123 = x3d.Shape()
Shape123.USE = "HAnimSiteShape"

HAnimSite121.children.append(Shape123)

HAnimSegment97.children.append(HAnimSite121)
HAnimSite124 = x3d.HAnimSite()
HAnimSite124.name = "r_femoral_medial_epicondyles_pt"
HAnimSite124.DEF = "hanim_r_femoral_medial_epicondyles_pt"
HAnimSite124.translation = [-0.0221,0.5014,0.0289]
TouchSensor125 = x3d.TouchSensor()
TouchSensor125.description = "HAnimSite r_femoral_medial_epicondyles_pt"

HAnimSite124.children.append(TouchSensor125)
Shape126 = x3d.Shape()
Shape126.USE = "HAnimSiteShape"

HAnimSite124.children.append(Shape126)

HAnimSegment97.children.append(HAnimSite124)
HAnimSite127 = x3d.HAnimSite()
HAnimSite127.name = "r_knee_crease_pt"
HAnimSite127.DEF = "hanim_r_knee_crease_pt"
HAnimSite127.translation = [-0.0825,0.4932,-0.0326]
TouchSensor128 = x3d.TouchSensor()
TouchSensor128.description = "HAnimSite r_knee_crease_pt"

HAnimSite127.children.append(TouchSensor128)
Shape129 = x3d.Shape()
Shape129.USE = "HAnimSiteShape"

HAnimSite127.children.append(Shape129)

HAnimSegment97.children.append(HAnimSite127)
HAnimSite130 = x3d.HAnimSite()
HAnimSite130.name = "r_suprapatella_pt"
HAnimSite130.DEF = "hanim_r_suprapatella_pt"
TouchSensor131 = x3d.TouchSensor()
TouchSensor131.description = "HAnimSite r_suprapatella_pt"

HAnimSite130.children.append(TouchSensor131)
Shape132 = x3d.Shape()
Shape132.USE = "HAnimSiteShape"

HAnimSite130.children.append(Shape132)

HAnimSegment97.children.append(HAnimSite130)

HAnimJoint96.children.append(HAnimSegment97)
HAnimJoint133 = x3d.HAnimJoint()
HAnimJoint133.name = "l_hip"
HAnimJoint133.DEF = "hanim_l_hip"
HAnimJoint133.center = [0.0961,0.9124,-0.0001]
HAnimJoint133.ulimit = [0,0,0]
HAnimJoint133.llimit = [0,0,0]
HAnimSegment134 = x3d.HAnimSegment()
HAnimSegment134.name = "l_thigh"
HAnimSegment134.DEF = "hanim_l_thigh"
Transform135 = x3d.Transform()
Transform135.translation = [0.0961,0.9124,-0.0001]
Transform136 = x3d.Transform()
#Empty Transform
Shape137 = x3d.Shape()
Shape137.USE = "HAnimJointShape"

Transform136.children.append(Shape137)

Transform135.children.append(Transform136)

HAnimSegment134.children.append(Transform135)
Shape138 = x3d.Shape()
LineSet139 = x3d.LineSet()
LineSet139.vertexCount = [2]
Coordinate140 = x3d.Coordinate()
Coordinate140.point = (0.0961,0.9124,-0.0001,0.1040,0.4867,0.0308)

LineSet139.coord = Coordinate140
#from l_hip to l_knee vertices 2
ColorRGBA141 = x3d.ColorRGBA()
ColorRGBA141.USE = "HAnimSegmentLineColorRGBA"

LineSet139.color = ColorRGBA141

Shape138.geometry = LineSet139

HAnimSegment134.children.append(Shape138)
HAnimSite142 = x3d.HAnimSite()
HAnimSite142.name = "l_lateral_malleolus_pt"
HAnimSite142.DEF = "hanim_l_lateral_malleolus_pt"
HAnimSite142.translation = [0.1308,0.0597,-0.1032]
TouchSensor143 = x3d.TouchSensor()
TouchSensor143.description = "HAnimSite l_lateral_malleolus_pt"

HAnimSite142.children.append(TouchSensor143)
Shape144 = x3d.Shape()
Shape144.USE = "HAnimSiteShape"

HAnimSite142.children.append(Shape144)

HAnimSegment134.children.append(HAnimSite142)
HAnimSite145 = x3d.HAnimSite()
HAnimSite145.name = "l_medial_malleolus_pt"
HAnimSite145.DEF = "hanim_l_medial_malleolus_pt"
HAnimSite145.translation = [0.089,0.0716,-0.0881]
TouchSensor146 = x3d.TouchSensor()
TouchSensor146.description = "HAnimSite l_medial_malleolus_pt"

HAnimSite145.children.append(TouchSensor146)
Shape147 = x3d.Shape()
Shape147.USE = "HAnimSiteShape"

HAnimSite145.children.append(Shape147)

HAnimSegment134.children.append(HAnimSite145)
HAnimSite148 = x3d.HAnimSite()
HAnimSite148.name = "l_tibiale_pt"
HAnimSite148.DEF = "hanim_l_tibiale_pt"
TouchSensor149 = x3d.TouchSensor()
TouchSensor149.description = "HAnimSite l_tibiale_pt"

HAnimSite148.children.append(TouchSensor149)
Shape150 = x3d.Shape()
Shape150.USE = "HAnimSiteShape"

HAnimSite148.children.append(Shape150)

HAnimSegment134.children.append(HAnimSite148)

HAnimJoint133.children.append(HAnimSegment134)
HAnimJoint151 = x3d.HAnimJoint()
HAnimJoint151.name = "l_knee"
HAnimJoint151.DEF = "hanim_l_knee"
HAnimJoint151.center = [0.104,0.4867,0.0308]
HAnimJoint151.ulimit = [0,0,0]
HAnimJoint151.llimit = [0,0,0]
HAnimSegment152 = x3d.HAnimSegment()
HAnimSegment152.name = "l_calf"
HAnimSegment152.DEF = "hanim_l_calf"
Transform153 = x3d.Transform()
Transform153.translation = [0.104,0.4867,0.0308]
Transform154 = x3d.Transform()
#Empty Transform
Shape155 = x3d.Shape()
Shape155.USE = "HAnimJointShape"

Transform154.children.append(Shape155)

Transform153.children.append(Transform154)

HAnimSegment152.children.append(Transform153)
Shape156 = x3d.Shape()
LineSet157 = x3d.LineSet()
LineSet157.vertexCount = [2]
Coordinate158 = x3d.Coordinate()
Coordinate158.point = (0.1040,0.4867,0.0308,0.1101,0.0656,-0.0736)

LineSet157.coord = Coordinate158
#from l_knee to l_talocrural vertices 2
ColorRGBA159 = x3d.ColorRGBA()
ColorRGBA159.USE = "HAnimSegmentLineColorRGBA"

LineSet157.color = ColorRGBA159

Shape156.geometry = LineSet157

HAnimSegment152.children.append(Shape156)
HAnimSite160 = x3d.HAnimSite()
HAnimSite160.name = "l_calcaneus_posterior_pt"
HAnimSite160.DEF = "hanim_l_calcaneus_posterior_pt"
HAnimSite160.translation = [0.0974,0.0259,-0.1171]
TouchSensor161 = x3d.TouchSensor()
TouchSensor161.description = "HAnimSite l_calcaneus_posterior_pt"

HAnimSite160.children.append(TouchSensor161)
Shape162 = x3d.Shape()
Shape162.USE = "HAnimSiteShape"

HAnimSite160.children.append(Shape162)

HAnimSegment152.children.append(HAnimSite160)
HAnimSite163 = x3d.HAnimSite()
HAnimSite163.name = "l_sphyrion_pt"
HAnimSite163.DEF = "hanim_l_sphyrion_pt"
HAnimSite163.translation = [0.089,0.0575,-0.0943]
TouchSensor164 = x3d.TouchSensor()
TouchSensor164.description = "HAnimSite l_sphyrion_pt"

HAnimSite163.children.append(TouchSensor164)
Shape165 = x3d.Shape()
Shape165.USE = "HAnimSiteShape"

HAnimSite163.children.append(Shape165)

HAnimSegment152.children.append(HAnimSite163)

HAnimJoint151.children.append(HAnimSegment152)
HAnimJoint166 = x3d.HAnimJoint()
HAnimJoint166.name = "l_talocrural"
HAnimJoint166.DEF = "hanim_l_talocrural"
HAnimJoint166.center = [0.1101,0.0656,-0.0736]
HAnimJoint166.ulimit = [0,0,0]
HAnimJoint166.llimit = [0,0,0]
HAnimSegment167 = x3d.HAnimSegment()
HAnimSegment167.name = "l_talus"
HAnimSegment167.DEF = "hanim_l_talus"
Transform168 = x3d.Transform()
Transform168.scale = [0.15,0.15,0.15]
Transform168.translation = [0.08,0.06,-0.025]
Transform168.rotation = [1,0,0,-1.57]
#Transform left foot
Transform169 = x3d.Transform()
#Empty Transform left foot
Shape170 = x3d.Shape()
Shape170.USE = "HAnimJointShape"

Transform169.children.append(Shape170)

Transform168.children.append(Transform169)

HAnimSegment167.children.append(Transform168)
Shape171 = x3d.Shape()
LineSet172 = x3d.LineSet()
LineSet172.vertexCount = [2]
Coordinate173 = x3d.Coordinate()
Coordinate173.point = (0.1101,0.0656,-0.0736,0.1101,0.0656,-0.0736)

LineSet172.coord = Coordinate173
#from l_talocrural to l_talocalcaneonavicular vertices 2
ColorRGBA174 = x3d.ColorRGBA()
ColorRGBA174.USE = "HAnimSegmentLineColorRGBA"

LineSet172.color = ColorRGBA174

Shape171.geometry = LineSet172

HAnimSegment167.children.append(Shape171)
Shape175 = x3d.Shape()
LineSet176 = x3d.LineSet()
LineSet176.vertexCount = [2]
Coordinate177 = x3d.Coordinate()
Coordinate177.point = (0.1101,0.0656,-0.0736,0.1101,0.0656,-0.0736)

LineSet176.coord = Coordinate177
#from l_talocrural to l_calcaneocuboid vertices 2
ColorRGBA178 = x3d.ColorRGBA()
ColorRGBA178.USE = "HAnimSegmentLineColorRGBA"

LineSet176.color = ColorRGBA178

Shape175.geometry = LineSet176

HAnimSegment167.children.append(Shape175)

HAnimJoint166.children.append(HAnimSegment167)
HAnimJoint179 = x3d.HAnimJoint()
HAnimJoint179.name = "l_talocalcaneonavicular"
HAnimJoint179.DEF = "hanim_l_talocalcaneonavicular"
HAnimJoint179.ulimit = [0,0,0]
HAnimJoint179.llimit = [0,0,0]
HAnimSegment180 = x3d.HAnimSegment()
HAnimSegment180.name = "l_navicular"
HAnimSegment180.DEF = "hanim_l_navicular"
Transform181 = x3d.Transform()
Transform181.translation = [0.1101,0.0656,-0.0736]
Transform182 = x3d.Transform()
#Empty Transform
Shape183 = x3d.Shape()
Shape183.USE = "HAnimJointShape"

Transform182.children.append(Shape183)

Transform181.children.append(Transform182)

HAnimSegment180.children.append(Transform181)
Shape184 = x3d.Shape()
LineSet185 = x3d.LineSet()
LineSet185.vertexCount = [2]
Coordinate186 = x3d.Coordinate()
Coordinate186.point = (0.1101,0.0656,-0.0736)

LineSet185.coord = Coordinate186
#from l_talocalcaneonavicular to l_cuneonavicular_1 vertices 1
ColorRGBA187 = x3d.ColorRGBA()
ColorRGBA187.USE = "HAnimSegmentLineColorRGBA"

LineSet185.color = ColorRGBA187

Shape184.geometry = LineSet185

HAnimSegment180.children.append(Shape184)
Shape188 = x3d.Shape()
LineSet189 = x3d.LineSet()
LineSet189.vertexCount = [2]
Coordinate190 = x3d.Coordinate()
Coordinate190.point = (0.1101,0.0656,-0.0736)

LineSet189.coord = Coordinate190
#from l_talocalcaneonavicular to l_cuneonavicular_2 vertices 1
ColorRGBA191 = x3d.ColorRGBA()
ColorRGBA191.USE = "HAnimSegmentLineColorRGBA"

LineSet189.color = ColorRGBA191

Shape188.geometry = LineSet189

HAnimSegment180.children.append(Shape188)
Shape192 = x3d.Shape()
LineSet193 = x3d.LineSet()
LineSet193.vertexCount = [2]
Coordinate194 = x3d.Coordinate()
Coordinate194.point = (0.1101,0.0656,-0.0736)

LineSet193.coord = Coordinate194
#from l_talocalcaneonavicular to l_cuneonavicular_3 vertices 1
ColorRGBA195 = x3d.ColorRGBA()
ColorRGBA195.USE = "HAnimSegmentLineColorRGBA"

LineSet193.color = ColorRGBA195

Shape192.geometry = LineSet193

HAnimSegment180.children.append(Shape192)

HAnimJoint179.children.append(HAnimSegment180)
HAnimJoint196 = x3d.HAnimJoint()
HAnimJoint196.name = "l_cuneonavicular_1"
HAnimJoint196.DEF = "hanim_l_cuneonavicular_1"
HAnimJoint196.ulimit = [0,0,0]
HAnimJoint196.llimit = [0,0,0]
HAnimSegment197 = x3d.HAnimSegment()
HAnimSegment197.name = "l_cuneiform_1"
HAnimSegment197.DEF = "hanim_l_cuneiform_1"
Transform198 = x3d.Transform()
Transform198.translation = [0.1101,0.0656,-0.0736]
Transform199 = x3d.Transform()
#Empty Transform
Shape200 = x3d.Shape()
Shape200.USE = "HAnimJointShape"

Transform199.children.append(Shape200)

Transform198.children.append(Transform199)

HAnimSegment197.children.append(Transform198)
Shape201 = x3d.Shape()
LineSet202 = x3d.LineSet()
LineSet202.vertexCount = [2]
Coordinate203 = x3d.Coordinate()
Coordinate203.point = (0.1101,0.0656,-0.0736)

LineSet202.coord = Coordinate203
#from l_cuneonavicular_1 to l_tarsometatarsal_1 vertices 1
ColorRGBA204 = x3d.ColorRGBA()
ColorRGBA204.USE = "HAnimSegmentLineColorRGBA"

LineSet202.color = ColorRGBA204

Shape201.geometry = LineSet202

HAnimSegment197.children.append(Shape201)

HAnimJoint196.children.append(HAnimSegment197)
HAnimJoint205 = x3d.HAnimJoint()
HAnimJoint205.name = "l_tarsometatarsal_1"
HAnimJoint205.DEF = "hanim_l_tarsometatarsal_1"
HAnimJoint205.ulimit = [0,0,0]
HAnimJoint205.llimit = [0,0,0]
HAnimSegment206 = x3d.HAnimSegment()
HAnimSegment206.name = "l_metatarsal_1"
HAnimSegment206.DEF = "hanim_l_metatarsal_1"
Transform207 = x3d.Transform()
Transform207.translation = [0.1101,0.0656,-0.0736]
Transform208 = x3d.Transform()
#Empty Transform
Shape209 = x3d.Shape()
Shape209.USE = "HAnimJointShape"

Transform208.children.append(Shape209)

Transform207.children.append(Transform208)

HAnimSegment206.children.append(Transform207)
Shape210 = x3d.Shape()
LineSet211 = x3d.LineSet()
LineSet211.vertexCount = [2]
Coordinate212 = x3d.Coordinate()
Coordinate212.point = (0.1101,0.0656,-0.0736)

LineSet211.coord = Coordinate212
#from l_tarsometatarsal_1 to l_metatarsophalangeal_1 vertices 1
ColorRGBA213 = x3d.ColorRGBA()
ColorRGBA213.USE = "HAnimSegmentLineColorRGBA"

LineSet211.color = ColorRGBA213

Shape210.geometry = LineSet211

HAnimSegment206.children.append(Shape210)
HAnimSite214 = x3d.HAnimSite()
HAnimSite214.name = "l_metatarsal_phalanx_1_pt"
HAnimSite214.DEF = "hanim_l_metatarsal_phalanx_1_pt"
TouchSensor215 = x3d.TouchSensor()
TouchSensor215.description = "HAnimSite l_metatarsal_phalanx_1_pt"

HAnimSite214.children.append(TouchSensor215)
Shape216 = x3d.Shape()
Shape216.USE = "HAnimSiteShape"

HAnimSite214.children.append(Shape216)

HAnimSegment206.children.append(HAnimSite214)

HAnimJoint205.children.append(HAnimSegment206)
HAnimJoint217 = x3d.HAnimJoint()
HAnimJoint217.name = "l_metatarsophalangeal_1"
HAnimJoint217.DEF = "hanim_l_metatarsophalangeal_1"
HAnimJoint217.ulimit = [0,0,0]
HAnimJoint217.llimit = [0,0,0]
HAnimSegment218 = x3d.HAnimSegment()
HAnimSegment218.name = "l_tarsal_proximal_phalanx_1"
HAnimSegment218.DEF = "hanim_l_tarsal_proximal_phalanx_1"
Transform219 = x3d.Transform()
Transform219.translation = [0.1101,0.0656,-0.0736]
Transform220 = x3d.Transform()
#Empty Transform
Shape221 = x3d.Shape()
Shape221.USE = "HAnimJointShape"

Transform220.children.append(Shape221)

Transform219.children.append(Transform220)

HAnimSegment218.children.append(Transform219)
Shape222 = x3d.Shape()
LineSet223 = x3d.LineSet()
LineSet223.vertexCount = [2]
Coordinate224 = x3d.Coordinate()
Coordinate224.point = (0.1101,0.0656,-0.0736)

LineSet223.coord = Coordinate224
#from l_metatarsophalangeal_1 to l_tarsal_interphalangeal_1 vertices 1
ColorRGBA225 = x3d.ColorRGBA()
ColorRGBA225.USE = "HAnimSegmentLineColorRGBA"

LineSet223.color = ColorRGBA225

Shape222.geometry = LineSet223

HAnimSegment218.children.append(Shape222)
HAnimSite226 = x3d.HAnimSite()
HAnimSite226.name = "l_tarsal_distal_phalanx_1_tip"
HAnimSite226.DEF = "hanim_l_tarsal_distal_phalanx_1_tip"
TouchSensor227 = x3d.TouchSensor()
TouchSensor227.description = "HAnimSite l_tarsal_distal_phalanx_1_tip"

HAnimSite226.children.append(TouchSensor227)
Shape228 = x3d.Shape()
Shape228.USE = "HAnimSiteShape"

HAnimSite226.children.append(Shape228)

HAnimSegment218.children.append(HAnimSite226)

HAnimJoint217.children.append(HAnimSegment218)
HAnimJoint229 = x3d.HAnimJoint()
HAnimJoint229.name = "l_tarsal_interphalangeal_1"
HAnimJoint229.DEF = "hanim_l_tarsal_interphalangeal_1"
HAnimJoint229.ulimit = [0,0,0]
HAnimJoint229.llimit = [0,0,0]

HAnimJoint217.children.append(HAnimJoint229)

HAnimJoint205.children.append(HAnimJoint217)

HAnimJoint196.children.append(HAnimJoint205)

HAnimJoint179.children.append(HAnimJoint196)
HAnimJoint230 = x3d.HAnimJoint()
HAnimJoint230.name = "l_cuneonavicular_2"
HAnimJoint230.DEF = "hanim_l_cuneonavicular_2"
HAnimJoint230.ulimit = [0,0,0]
HAnimJoint230.llimit = [0,0,0]
HAnimSegment231 = x3d.HAnimSegment()
HAnimSegment231.name = "l_cuneiform_2"
HAnimSegment231.DEF = "hanim_l_cuneiform_2"
Transform232 = x3d.Transform()
Transform232.translation = [0.1101,0.0656,-0.0736]
Transform233 = x3d.Transform()
#Empty Transform
Shape234 = x3d.Shape()
Shape234.USE = "HAnimJointShape"

Transform233.children.append(Shape234)

Transform232.children.append(Transform233)

HAnimSegment231.children.append(Transform232)
Shape235 = x3d.Shape()
LineSet236 = x3d.LineSet()
LineSet236.vertexCount = [2]
Coordinate237 = x3d.Coordinate()
Coordinate237.point = (0.1101,0.0656,-0.0736)

LineSet236.coord = Coordinate237
#from l_cuneonavicular_2 to l_tarsometatarsal_2 vertices 1
ColorRGBA238 = x3d.ColorRGBA()
ColorRGBA238.USE = "HAnimSegmentLineColorRGBA"

LineSet236.color = ColorRGBA238

Shape235.geometry = LineSet236

HAnimSegment231.children.append(Shape235)

HAnimJoint230.children.append(HAnimSegment231)
HAnimJoint239 = x3d.HAnimJoint()
HAnimJoint239.name = "l_tarsometatarsal_2"
HAnimJoint239.DEF = "hanim_l_tarsometatarsal_2"
HAnimJoint239.ulimit = [0,0,0]
HAnimJoint239.llimit = [0,0,0]
HAnimSegment240 = x3d.HAnimSegment()
HAnimSegment240.name = "l_metatarsal_2"
HAnimSegment240.DEF = "hanim_l_metatarsal_2"
Transform241 = x3d.Transform()
Transform241.translation = [0.1101,0.0656,-0.0736]
Transform242 = x3d.Transform()
#Empty Transform
Shape243 = x3d.Shape()
Shape243.USE = "HAnimJointShape"

Transform242.children.append(Shape243)

Transform241.children.append(Transform242)

HAnimSegment240.children.append(Transform241)
Shape244 = x3d.Shape()
LineSet245 = x3d.LineSet()
LineSet245.vertexCount = [2]
Coordinate246 = x3d.Coordinate()
Coordinate246.point = (0.1101,0.0656,-0.0736)

LineSet245.coord = Coordinate246
#from l_tarsometatarsal_2 to l_metatarsophalangeal_2 vertices 1
ColorRGBA247 = x3d.ColorRGBA()
ColorRGBA247.USE = "HAnimSegmentLineColorRGBA"

LineSet245.color = ColorRGBA247

Shape244.geometry = LineSet245

HAnimSegment240.children.append(Shape244)

HAnimJoint239.children.append(HAnimSegment240)
HAnimJoint248 = x3d.HAnimJoint()
HAnimJoint248.name = "l_metatarsophalangeal_2"
HAnimJoint248.DEF = "hanim_l_metatarsophalangeal_2"
HAnimJoint248.ulimit = [0,0,0]
HAnimJoint248.llimit = [0,0,0]
HAnimSegment249 = x3d.HAnimSegment()
HAnimSegment249.name = "l_tarsal_proximal_phalanx_2"
HAnimSegment249.DEF = "hanim_l_tarsal_proximal_phalanx_2"
Transform250 = x3d.Transform()
Transform250.translation = [0.1101,0.0656,-0.0736]
Transform251 = x3d.Transform()
#Empty Transform
Shape252 = x3d.Shape()
Shape252.USE = "HAnimJointShape"

Transform251.children.append(Shape252)

Transform250.children.append(Transform251)

HAnimSegment249.children.append(Transform250)
Shape253 = x3d.Shape()
LineSet254 = x3d.LineSet()
LineSet254.vertexCount = [2]
Coordinate255 = x3d.Coordinate()
Coordinate255.point = (0.1101,0.0656,-0.0736)

LineSet254.coord = Coordinate255
#from l_metatarsophalangeal_2 to l_tarsal_proximal_interphalangeal_2 vertices 1
ColorRGBA256 = x3d.ColorRGBA()
ColorRGBA256.USE = "HAnimSegmentLineColorRGBA"

LineSet254.color = ColorRGBA256

Shape253.geometry = LineSet254

HAnimSegment249.children.append(Shape253)

HAnimJoint248.children.append(HAnimSegment249)
HAnimJoint257 = x3d.HAnimJoint()
HAnimJoint257.name = "l_tarsal_proximal_interphalangeal_2"
HAnimJoint257.DEF = "hanim_l_tarsal_proximal_interphalangeal_2"
HAnimJoint257.ulimit = [0,0,0]
HAnimJoint257.llimit = [0,0,0]
HAnimSegment258 = x3d.HAnimSegment()
HAnimSegment258.name = "l_tarsal_middle_phalanx_2"
HAnimSegment258.DEF = "hanim_l_tarsal_middle_phalanx_2"
Transform259 = x3d.Transform()
Transform259.translation = [0.1101,0.0656,-0.0736]
Transform260 = x3d.Transform()
#Empty Transform
Shape261 = x3d.Shape()
Shape261.USE = "HAnimJointShape"

Transform260.children.append(Shape261)

Transform259.children.append(Transform260)

HAnimSegment258.children.append(Transform259)
Shape262 = x3d.Shape()
LineSet263 = x3d.LineSet()
LineSet263.vertexCount = [2]
Coordinate264 = x3d.Coordinate()
Coordinate264.point = (0.1101,0.0656,-0.0736)

LineSet263.coord = Coordinate264
#from l_tarsal_proximal_interphalangeal_2 to l_tarsal_distal_interphalangeal_2 vertices 1
ColorRGBA265 = x3d.ColorRGBA()
ColorRGBA265.USE = "HAnimSegmentLineColorRGBA"

LineSet263.color = ColorRGBA265

Shape262.geometry = LineSet263

HAnimSegment258.children.append(Shape262)
HAnimSite266 = x3d.HAnimSite()
HAnimSite266.name = "l_tarsal_distal_phalanx_2_tip"
HAnimSite266.DEF = "hanim_l_tarsal_distal_phalanx_2_tip"
HAnimSite266.translation = [0.1195,0.0079,0.1433]
TouchSensor267 = x3d.TouchSensor()
TouchSensor267.description = "HAnimSite l_tarsal_distal_phalanx_2_tip"

HAnimSite266.children.append(TouchSensor267)
Shape268 = x3d.Shape()
Shape268.USE = "HAnimSiteShape"

HAnimSite266.children.append(Shape268)

HAnimSegment258.children.append(HAnimSite266)

HAnimJoint257.children.append(HAnimSegment258)
HAnimJoint269 = x3d.HAnimJoint()
HAnimJoint269.name = "l_tarsal_distal_interphalangeal_2"
HAnimJoint269.DEF = "hanim_l_tarsal_distal_interphalangeal_2"
HAnimJoint269.ulimit = [0,0,0]
HAnimJoint269.llimit = [0,0,0]

HAnimJoint257.children.append(HAnimJoint269)

HAnimJoint248.children.append(HAnimJoint257)

HAnimJoint239.children.append(HAnimJoint248)

HAnimJoint230.children.append(HAnimJoint239)

HAnimJoint179.children.append(HAnimJoint230)
HAnimJoint270 = x3d.HAnimJoint()
HAnimJoint270.name = "l_cuneonavicular_3"
HAnimJoint270.DEF = "hanim_l_cuneonavicular_3"
HAnimJoint270.ulimit = [0,0,0]
HAnimJoint270.llimit = [0,0,0]
HAnimSegment271 = x3d.HAnimSegment()
HAnimSegment271.name = "l_cuneiform_3"
HAnimSegment271.DEF = "hanim_l_cuneiform_3"
Transform272 = x3d.Transform()
Transform272.translation = [0.1101,0.0656,-0.0736]
Transform273 = x3d.Transform()
#Empty Transform
Shape274 = x3d.Shape()
Shape274.USE = "HAnimJointShape"

Transform273.children.append(Shape274)

Transform272.children.append(Transform273)

HAnimSegment271.children.append(Transform272)
Shape275 = x3d.Shape()
LineSet276 = x3d.LineSet()
LineSet276.vertexCount = [2]
Coordinate277 = x3d.Coordinate()
Coordinate277.point = (0.1101,0.0656,-0.0736)

LineSet276.coord = Coordinate277
#from l_cuneonavicular_3 to l_tarsometatarsal_3 vertices 1
ColorRGBA278 = x3d.ColorRGBA()
ColorRGBA278.USE = "HAnimSegmentLineColorRGBA"

LineSet276.color = ColorRGBA278

Shape275.geometry = LineSet276

HAnimSegment271.children.append(Shape275)

HAnimJoint270.children.append(HAnimSegment271)
HAnimJoint279 = x3d.HAnimJoint()
HAnimJoint279.name = "l_tarsometatarsal_3"
HAnimJoint279.DEF = "hanim_l_tarsometatarsal_3"
HAnimJoint279.ulimit = [0,0,0]
HAnimJoint279.llimit = [0,0,0]
HAnimSegment280 = x3d.HAnimSegment()
HAnimSegment280.name = "l_metatarsal_3"
HAnimSegment280.DEF = "hanim_l_metatarsal_3"
Transform281 = x3d.Transform()
Transform281.translation = [0.1101,0.0656,-0.0736]
Transform282 = x3d.Transform()
#Empty Transform
Shape283 = x3d.Shape()
Shape283.USE = "HAnimJointShape"

Transform282.children.append(Shape283)

Transform281.children.append(Transform282)

HAnimSegment280.children.append(Transform281)
Shape284 = x3d.Shape()
LineSet285 = x3d.LineSet()
LineSet285.vertexCount = [2]
Coordinate286 = x3d.Coordinate()
Coordinate286.point = (0.1101,0.0656,-0.0736)

LineSet285.coord = Coordinate286
#from l_tarsometatarsal_3 to l_metatarsophalangeal_3 vertices 1
ColorRGBA287 = x3d.ColorRGBA()
ColorRGBA287.USE = "HAnimSegmentLineColorRGBA"

LineSet285.color = ColorRGBA287

Shape284.geometry = LineSet285

HAnimSegment280.children.append(Shape284)

HAnimJoint279.children.append(HAnimSegment280)
HAnimJoint288 = x3d.HAnimJoint()
HAnimJoint288.name = "l_metatarsophalangeal_3"
HAnimJoint288.DEF = "hanim_l_metatarsophalangeal_3"
HAnimJoint288.ulimit = [0,0,0]
HAnimJoint288.llimit = [0,0,0]
HAnimSegment289 = x3d.HAnimSegment()
HAnimSegment289.name = "l_tarsal_proximal_phalanx_3"
HAnimSegment289.DEF = "hanim_l_tarsal_proximal_phalanx_3"
Transform290 = x3d.Transform()
Transform290.translation = [0.1101,0.0656,-0.0736]
Transform291 = x3d.Transform()
#Empty Transform
Shape292 = x3d.Shape()
Shape292.USE = "HAnimJointShape"

Transform291.children.append(Shape292)

Transform290.children.append(Transform291)

HAnimSegment289.children.append(Transform290)
Shape293 = x3d.Shape()
LineSet294 = x3d.LineSet()
LineSet294.vertexCount = [2]
Coordinate295 = x3d.Coordinate()
Coordinate295.point = (0.1101,0.0656,-0.0736)

LineSet294.coord = Coordinate295
#from l_metatarsophalangeal_3 to l_tarsal_proximal_interphalangeal_3 vertices 1
ColorRGBA296 = x3d.ColorRGBA()
ColorRGBA296.USE = "HAnimSegmentLineColorRGBA"

LineSet294.color = ColorRGBA296

Shape293.geometry = LineSet294

HAnimSegment289.children.append(Shape293)

HAnimJoint288.children.append(HAnimSegment289)
HAnimJoint297 = x3d.HAnimJoint()
HAnimJoint297.name = "l_tarsal_proximal_interphalangeal_3"
HAnimJoint297.DEF = "hanim_l_tarsal_proximal_interphalangeal_3"
HAnimJoint297.ulimit = [0,0,0]
HAnimJoint297.llimit = [0,0,0]
HAnimSegment298 = x3d.HAnimSegment()
HAnimSegment298.name = "l_tarsal_middle_phalanx_3"
HAnimSegment298.DEF = "hanim_l_tarsal_middle_phalanx_3"
Transform299 = x3d.Transform()
Transform299.translation = [0.1101,0.0656,-0.0736]
Transform300 = x3d.Transform()
#Empty Transform
Shape301 = x3d.Shape()
Shape301.USE = "HAnimJointShape"

Transform300.children.append(Shape301)

Transform299.children.append(Transform300)

HAnimSegment298.children.append(Transform299)
Shape302 = x3d.Shape()
LineSet303 = x3d.LineSet()
LineSet303.vertexCount = [2]
Coordinate304 = x3d.Coordinate()
Coordinate304.point = (0.1101,0.0656,-0.0736)

LineSet303.coord = Coordinate304
#from l_tarsal_proximal_interphalangeal_3 to l_tarsal_distal_interphalangeal_3 vertices 1
ColorRGBA305 = x3d.ColorRGBA()
ColorRGBA305.USE = "HAnimSegmentLineColorRGBA"

LineSet303.color = ColorRGBA305

Shape302.geometry = LineSet303

HAnimSegment298.children.append(Shape302)
HAnimSite306 = x3d.HAnimSite()
HAnimSite306.name = "l_tarsal_distal_phalanx_3_tip"
HAnimSite306.DEF = "hanim_l_tarsal_distal_phalanx_3_tip"
TouchSensor307 = x3d.TouchSensor()
TouchSensor307.description = "HAnimSite l_tarsal_distal_phalanx_3_tip"

HAnimSite306.children.append(TouchSensor307)
Shape308 = x3d.Shape()
Shape308.USE = "HAnimSiteShape"

HAnimSite306.children.append(Shape308)

HAnimSegment298.children.append(HAnimSite306)

HAnimJoint297.children.append(HAnimSegment298)
HAnimJoint309 = x3d.HAnimJoint()
HAnimJoint309.name = "l_tarsal_distal_interphalangeal_3"
HAnimJoint309.DEF = "hanim_l_tarsal_distal_interphalangeal_3"
HAnimJoint309.ulimit = [0,0,0]
HAnimJoint309.llimit = [0,0,0]

HAnimJoint297.children.append(HAnimJoint309)

HAnimJoint288.children.append(HAnimJoint297)

HAnimJoint279.children.append(HAnimJoint288)

HAnimJoint270.children.append(HAnimJoint279)

HAnimJoint179.children.append(HAnimJoint270)

HAnimJoint166.children.append(HAnimJoint179)
HAnimJoint310 = x3d.HAnimJoint()
HAnimJoint310.name = "l_calcaneocuboid"
HAnimJoint310.DEF = "hanim_l_calcaneocuboid"
HAnimJoint310.ulimit = [0,0,0]
HAnimJoint310.llimit = [0,0,0]
HAnimSegment311 = x3d.HAnimSegment()
HAnimSegment311.name = "l_calcaneus"
HAnimSegment311.DEF = "hanim_l_calcaneus"
Transform312 = x3d.Transform()
Transform312.translation = [0.1101,0.0656,-0.0736]
Transform313 = x3d.Transform()
#Empty Transform
Shape314 = x3d.Shape()
Shape314.USE = "HAnimJointShape"

Transform313.children.append(Shape314)

Transform312.children.append(Transform313)

HAnimSegment311.children.append(Transform312)
Shape315 = x3d.Shape()
LineSet316 = x3d.LineSet()
LineSet316.vertexCount = [2]
Coordinate317 = x3d.Coordinate()
Coordinate317.point = (0.1101,0.0656,-0.0736)

LineSet316.coord = Coordinate317
#from l_calcaneocuboid to l_transversetarsal vertices 1
ColorRGBA318 = x3d.ColorRGBA()
ColorRGBA318.USE = "HAnimSegmentLineColorRGBA"

LineSet316.color = ColorRGBA318

Shape315.geometry = LineSet316

HAnimSegment311.children.append(Shape315)

HAnimJoint310.children.append(HAnimSegment311)
HAnimJoint319 = x3d.HAnimJoint()
HAnimJoint319.name = "l_transversetarsal"
HAnimJoint319.DEF = "hanim_l_transversetarsal"
HAnimJoint319.ulimit = [0,0,0]
HAnimJoint319.llimit = [0,0,0]
HAnimSegment320 = x3d.HAnimSegment()
HAnimSegment320.name = "l_cuboid"
HAnimSegment320.DEF = "hanim_l_cuboid"
Transform321 = x3d.Transform()
Transform321.translation = [0.1101,0.0656,-0.0736]
Transform322 = x3d.Transform()
#Empty Transform
Shape323 = x3d.Shape()
Shape323.USE = "HAnimJointShape"

Transform322.children.append(Shape323)

Transform321.children.append(Transform322)

HAnimSegment320.children.append(Transform321)
Shape324 = x3d.Shape()
LineSet325 = x3d.LineSet()
LineSet325.vertexCount = [2]
Coordinate326 = x3d.Coordinate()
Coordinate326.point = (0.1101,0.0656,-0.0736)

LineSet325.coord = Coordinate326
#from l_transversetarsal to l_tarsometatarsal_4 vertices 1
ColorRGBA327 = x3d.ColorRGBA()
ColorRGBA327.USE = "HAnimSegmentLineColorRGBA"

LineSet325.color = ColorRGBA327

Shape324.geometry = LineSet325

HAnimSegment320.children.append(Shape324)
Shape328 = x3d.Shape()
LineSet329 = x3d.LineSet()
LineSet329.vertexCount = [2]
Coordinate330 = x3d.Coordinate()
Coordinate330.point = (0.1101,0.0656,-0.0736)

LineSet329.coord = Coordinate330
#from l_transversetarsal to l_tarsometatarsal_5 vertices 1
ColorRGBA331 = x3d.ColorRGBA()
ColorRGBA331.USE = "HAnimSegmentLineColorRGBA"

LineSet329.color = ColorRGBA331

Shape328.geometry = LineSet329

HAnimSegment320.children.append(Shape328)

HAnimJoint319.children.append(HAnimSegment320)
HAnimJoint332 = x3d.HAnimJoint()
HAnimJoint332.name = "l_tarsometatarsal_4"
HAnimJoint332.DEF = "hanim_l_tarsometatarsal_4"
HAnimJoint332.ulimit = [0,0,0]
HAnimJoint332.llimit = [0,0,0]
HAnimSegment333 = x3d.HAnimSegment()
HAnimSegment333.name = "l_metatarsal_4"
HAnimSegment333.DEF = "hanim_l_metatarsal_4"
Transform334 = x3d.Transform()
Transform334.translation = [0.1101,0.0656,-0.0736]
Transform335 = x3d.Transform()
#Empty Transform
Shape336 = x3d.Shape()
Shape336.USE = "HAnimJointShape"

Transform335.children.append(Shape336)

Transform334.children.append(Transform335)

HAnimSegment333.children.append(Transform334)
Shape337 = x3d.Shape()
LineSet338 = x3d.LineSet()
LineSet338.vertexCount = [2]
Coordinate339 = x3d.Coordinate()
Coordinate339.point = (0.1101,0.0656,-0.0736)

LineSet338.coord = Coordinate339
#from l_tarsometatarsal_4 to l_metatarsophalangeal_4 vertices 1
ColorRGBA340 = x3d.ColorRGBA()
ColorRGBA340.USE = "HAnimSegmentLineColorRGBA"

LineSet338.color = ColorRGBA340

Shape337.geometry = LineSet338

HAnimSegment333.children.append(Shape337)

HAnimJoint332.children.append(HAnimSegment333)
HAnimJoint341 = x3d.HAnimJoint()
HAnimJoint341.name = "l_metatarsophalangeal_4"
HAnimJoint341.DEF = "hanim_l_metatarsophalangeal_4"
HAnimJoint341.ulimit = [0,0,0]
HAnimJoint341.llimit = [0,0,0]
HAnimSegment342 = x3d.HAnimSegment()
HAnimSegment342.name = "l_tarsal_proximal_phalanx_4"
HAnimSegment342.DEF = "hanim_l_tarsal_proximal_phalanx_4"
Transform343 = x3d.Transform()
Transform343.translation = [0.1101,0.0656,-0.0736]
Transform344 = x3d.Transform()
#Empty Transform
Shape345 = x3d.Shape()
Shape345.USE = "HAnimJointShape"

Transform344.children.append(Shape345)

Transform343.children.append(Transform344)

HAnimSegment342.children.append(Transform343)
Shape346 = x3d.Shape()
LineSet347 = x3d.LineSet()
LineSet347.vertexCount = [2]
Coordinate348 = x3d.Coordinate()
Coordinate348.point = (0.1101,0.0656,-0.0736)

LineSet347.coord = Coordinate348
#from l_metatarsophalangeal_4 to l_tarsal_proximal_interphalangeal_4 vertices 1
ColorRGBA349 = x3d.ColorRGBA()
ColorRGBA349.USE = "HAnimSegmentLineColorRGBA"

LineSet347.color = ColorRGBA349

Shape346.geometry = LineSet347

HAnimSegment342.children.append(Shape346)

HAnimJoint341.children.append(HAnimSegment342)
HAnimJoint350 = x3d.HAnimJoint()
HAnimJoint350.name = "l_tarsal_proximal_interphalangeal_4"
HAnimJoint350.DEF = "hanim_l_tarsal_proximal_interphalangeal_4"
HAnimJoint350.ulimit = [0,0,0]
HAnimJoint350.llimit = [0,0,0]
HAnimSegment351 = x3d.HAnimSegment()
HAnimSegment351.name = "l_tarsal_middle_phalanx_4"
HAnimSegment351.DEF = "hanim_l_tarsal_middle_phalanx_4"
Transform352 = x3d.Transform()
Transform352.translation = [0.1101,0.0656,-0.0736]
Transform353 = x3d.Transform()
#Empty Transform
Shape354 = x3d.Shape()
Shape354.USE = "HAnimJointShape"

Transform353.children.append(Shape354)

Transform352.children.append(Transform353)

HAnimSegment351.children.append(Transform352)
Shape355 = x3d.Shape()
LineSet356 = x3d.LineSet()
LineSet356.vertexCount = [2]
Coordinate357 = x3d.Coordinate()
Coordinate357.point = (0.1101,0.0656,-0.0736)

LineSet356.coord = Coordinate357
#from l_tarsal_proximal_interphalangeal_4 to l_tarsal_distal_interphalangeal_4 vertices 1
ColorRGBA358 = x3d.ColorRGBA()
ColorRGBA358.USE = "HAnimSegmentLineColorRGBA"

LineSet356.color = ColorRGBA358

Shape355.geometry = LineSet356

HAnimSegment351.children.append(Shape355)
HAnimSite359 = x3d.HAnimSite()
HAnimSite359.name = "l_tarsal_distal_phalanx_4_tip"
HAnimSite359.DEF = "hanim_l_tarsal_distal_phalanx_4_tip"
TouchSensor360 = x3d.TouchSensor()
TouchSensor360.description = "HAnimSite l_tarsal_distal_phalanx_4_tip"

HAnimSite359.children.append(TouchSensor360)
Shape361 = x3d.Shape()
Shape361.USE = "HAnimSiteShape"

HAnimSite359.children.append(Shape361)

HAnimSegment351.children.append(HAnimSite359)

HAnimJoint350.children.append(HAnimSegment351)
HAnimJoint362 = x3d.HAnimJoint()
HAnimJoint362.name = "l_tarsal_distal_interphalangeal_4"
HAnimJoint362.DEF = "hanim_l_tarsal_distal_interphalangeal_4"
HAnimJoint362.ulimit = [0,0,0]
HAnimJoint362.llimit = [0,0,0]

HAnimJoint350.children.append(HAnimJoint362)

HAnimJoint341.children.append(HAnimJoint350)

HAnimJoint332.children.append(HAnimJoint341)

HAnimJoint319.children.append(HAnimJoint332)
HAnimJoint363 = x3d.HAnimJoint()
HAnimJoint363.name = "l_tarsometatarsal_5"
HAnimJoint363.DEF = "hanim_l_tarsometatarsal_5"
HAnimJoint363.ulimit = [0,0,0]
HAnimJoint363.llimit = [0,0,0]
HAnimSegment364 = x3d.HAnimSegment()
HAnimSegment364.name = "l_metatarsal_5"
HAnimSegment364.DEF = "hanim_l_metatarsal_5"
Transform365 = x3d.Transform()
Transform365.translation = [0.1101,0.0656,-0.0736]
Transform366 = x3d.Transform()
#Empty Transform
Shape367 = x3d.Shape()
Shape367.USE = "HAnimJointShape"

Transform366.children.append(Shape367)

Transform365.children.append(Transform366)

HAnimSegment364.children.append(Transform365)
Shape368 = x3d.Shape()
LineSet369 = x3d.LineSet()
LineSet369.vertexCount = [2]
Coordinate370 = x3d.Coordinate()
Coordinate370.point = (0.1101,0.0656,-0.0736)

LineSet369.coord = Coordinate370
#from l_tarsometatarsal_5 to l_metatarsophalangeal_5 vertices 1
ColorRGBA371 = x3d.ColorRGBA()
ColorRGBA371.USE = "HAnimSegmentLineColorRGBA"

LineSet369.color = ColorRGBA371

Shape368.geometry = LineSet369

HAnimSegment364.children.append(Shape368)
HAnimSite372 = x3d.HAnimSite()
HAnimSite372.name = "l_metatarsal_phalanx_5_pt"
HAnimSite372.DEF = "hanim_l_metatarsal_phalanx_5_pt"
TouchSensor373 = x3d.TouchSensor()
TouchSensor373.description = "HAnimSite l_metatarsal_phalanx_5_pt"

HAnimSite372.children.append(TouchSensor373)
Shape374 = x3d.Shape()
Shape374.USE = "HAnimSiteShape"

HAnimSite372.children.append(Shape374)

HAnimSegment364.children.append(HAnimSite372)

HAnimJoint363.children.append(HAnimSegment364)
HAnimJoint375 = x3d.HAnimJoint()
HAnimJoint375.name = "l_metatarsophalangeal_5"
HAnimJoint375.DEF = "hanim_l_metatarsophalangeal_5"
HAnimJoint375.ulimit = [0,0,0]
HAnimJoint375.llimit = [0,0,0]
HAnimSegment376 = x3d.HAnimSegment()
HAnimSegment376.name = "l_tarsal_proximal_phalanx_5"
HAnimSegment376.DEF = "hanim_l_tarsal_proximal_phalanx_5"
Transform377 = x3d.Transform()
Transform377.translation = [0.1101,0.0656,-0.0736]
Transform378 = x3d.Transform()
#Empty Transform
Shape379 = x3d.Shape()
Shape379.USE = "HAnimJointShape"

Transform378.children.append(Shape379)

Transform377.children.append(Transform378)

HAnimSegment376.children.append(Transform377)
Shape380 = x3d.Shape()
LineSet381 = x3d.LineSet()
LineSet381.vertexCount = [2]
Coordinate382 = x3d.Coordinate()
Coordinate382.point = (0.1101,0.0656,-0.0736)

LineSet381.coord = Coordinate382
#from l_metatarsophalangeal_5 to l_tarsal_proximal_interphalangeal_5 vertices 1
ColorRGBA383 = x3d.ColorRGBA()
ColorRGBA383.USE = "HAnimSegmentLineColorRGBA"

LineSet381.color = ColorRGBA383

Shape380.geometry = LineSet381

HAnimSegment376.children.append(Shape380)

HAnimJoint375.children.append(HAnimSegment376)
HAnimJoint384 = x3d.HAnimJoint()
HAnimJoint384.name = "l_tarsal_proximal_interphalangeal_5"
HAnimJoint384.DEF = "hanim_l_tarsal_proximal_interphalangeal_5"
HAnimJoint384.ulimit = [0,0,0]
HAnimJoint384.llimit = [0,0,0]
HAnimSegment385 = x3d.HAnimSegment()
HAnimSegment385.name = "l_tarsal_middle_phalanx_5"
HAnimSegment385.DEF = "hanim_l_tarsal_middle_phalanx_5"
Transform386 = x3d.Transform()
Transform386.translation = [0.1101,0.0656,-0.0736]
Transform387 = x3d.Transform()
#Empty Transform
Shape388 = x3d.Shape()
Shape388.USE = "HAnimJointShape"

Transform387.children.append(Shape388)

Transform386.children.append(Transform387)

HAnimSegment385.children.append(Transform386)
Shape389 = x3d.Shape()
LineSet390 = x3d.LineSet()
LineSet390.vertexCount = [2]
Coordinate391 = x3d.Coordinate()
Coordinate391.point = (0.1101,0.0656,-0.0736)

LineSet390.coord = Coordinate391
#from l_tarsal_proximal_interphalangeal_5 to l_tarsal_distal_interphalangeal_5 vertices 1
ColorRGBA392 = x3d.ColorRGBA()
ColorRGBA392.USE = "HAnimSegmentLineColorRGBA"

LineSet390.color = ColorRGBA392

Shape389.geometry = LineSet390

HAnimSegment385.children.append(Shape389)
HAnimSite393 = x3d.HAnimSite()
HAnimSite393.name = "l_tarsal_distal_phalanx_5_tip"
HAnimSite393.DEF = "hanim_l_tarsal_distal_phalanx_5_tip"
TouchSensor394 = x3d.TouchSensor()
TouchSensor394.description = "HAnimSite l_tarsal_distal_phalanx_5_tip"

HAnimSite393.children.append(TouchSensor394)
Shape395 = x3d.Shape()
Shape395.USE = "HAnimSiteShape"

HAnimSite393.children.append(Shape395)

HAnimSegment385.children.append(HAnimSite393)

HAnimJoint384.children.append(HAnimSegment385)
HAnimJoint396 = x3d.HAnimJoint()
HAnimJoint396.name = "l_tarsal_distal_interphalangeal_5"
HAnimJoint396.DEF = "hanim_l_tarsal_distal_interphalangeal_5"
HAnimJoint396.ulimit = [0,0,0]
HAnimJoint396.llimit = [0,0,0]

HAnimJoint384.children.append(HAnimJoint396)

HAnimJoint375.children.append(HAnimJoint384)

HAnimJoint363.children.append(HAnimJoint375)

HAnimJoint319.children.append(HAnimJoint363)

HAnimJoint310.children.append(HAnimJoint319)

HAnimJoint166.children.append(HAnimJoint310)

HAnimJoint151.children.append(HAnimJoint166)

HAnimJoint133.children.append(HAnimJoint151)

HAnimJoint96.children.append(HAnimJoint133)
HAnimJoint397 = x3d.HAnimJoint()
HAnimJoint397.name = "r_hip"
HAnimJoint397.DEF = "hanim_r_hip"
HAnimJoint397.center = [-0.095,0.9171,0.0029]
HAnimJoint397.ulimit = [0,0,0]
HAnimJoint397.llimit = [0,0,0]
HAnimSegment398 = x3d.HAnimSegment()
HAnimSegment398.name = "r_thigh"
HAnimSegment398.DEF = "hanim_r_thigh"
Transform399 = x3d.Transform()
Transform399.translation = [-0.095,0.9171,0.0029]
Transform400 = x3d.Transform()
#Empty Transform
Shape401 = x3d.Shape()
Shape401.USE = "HAnimJointShape"

Transform400.children.append(Shape401)

Transform399.children.append(Transform400)

HAnimSegment398.children.append(Transform399)
Shape402 = x3d.Shape()
LineSet403 = x3d.LineSet()
LineSet403.vertexCount = [2]
Coordinate404 = x3d.Coordinate()
Coordinate404.point = (-0.0950,0.9171,0.0029,-0.0867,0.4913,0.0318)

LineSet403.coord = Coordinate404
#from r_hip to r_knee vertices 2
ColorRGBA405 = x3d.ColorRGBA()
ColorRGBA405.USE = "HAnimSegmentLineColorRGBA"

LineSet403.color = ColorRGBA405

Shape402.geometry = LineSet403

HAnimSegment398.children.append(Shape402)
HAnimSite406 = x3d.HAnimSite()
HAnimSite406.name = "r_lateral_malleolus_pt"
HAnimSite406.DEF = "hanim_r_lateral_malleolus_pt"
HAnimSite406.translation = [-0.1006,0.0658,-0.1075]
TouchSensor407 = x3d.TouchSensor()
TouchSensor407.description = "HAnimSite r_lateral_malleolus_pt"

HAnimSite406.children.append(TouchSensor407)
Shape408 = x3d.Shape()
Shape408.USE = "HAnimSiteShape"

HAnimSite406.children.append(Shape408)

HAnimSegment398.children.append(HAnimSite406)
HAnimSite409 = x3d.HAnimSite()
HAnimSite409.name = "r_medial_malleolus_pt"
HAnimSite409.DEF = "hanim_r_medial_malleolus_pt"
HAnimSite409.translation = [-0.0591,0.076,-0.0928]
TouchSensor410 = x3d.TouchSensor()
TouchSensor410.description = "HAnimSite r_medial_malleolus_pt"

HAnimSite409.children.append(TouchSensor410)
Shape411 = x3d.Shape()
Shape411.USE = "HAnimSiteShape"

HAnimSite409.children.append(Shape411)

HAnimSegment398.children.append(HAnimSite409)
HAnimSite412 = x3d.HAnimSite()
HAnimSite412.name = "r_tibiale_pt"
HAnimSite412.DEF = "hanim_r_tibiale_pt"
TouchSensor413 = x3d.TouchSensor()
TouchSensor413.description = "HAnimSite r_tibiale_pt"

HAnimSite412.children.append(TouchSensor413)
Shape414 = x3d.Shape()
Shape414.USE = "HAnimSiteShape"

HAnimSite412.children.append(Shape414)

HAnimSegment398.children.append(HAnimSite412)

HAnimJoint397.children.append(HAnimSegment398)
HAnimJoint415 = x3d.HAnimJoint()
HAnimJoint415.name = "r_knee"
HAnimJoint415.DEF = "hanim_r_knee"
HAnimJoint415.center = [-0.0867,0.4913,0.0318]
HAnimJoint415.ulimit = [0,0,0]
HAnimJoint415.llimit = [0,0,0]
HAnimSegment416 = x3d.HAnimSegment()
HAnimSegment416.name = "r_calf"
HAnimSegment416.DEF = "hanim_r_calf"
Transform417 = x3d.Transform()
Transform417.translation = [-0.0867,0.4913,0.0318]
Transform418 = x3d.Transform()
#Empty Transform
Shape419 = x3d.Shape()
Shape419.USE = "HAnimJointShape"

Transform418.children.append(Shape419)

Transform417.children.append(Transform418)

HAnimSegment416.children.append(Transform417)
Shape420 = x3d.Shape()
LineSet421 = x3d.LineSet()
LineSet421.vertexCount = [2]
Coordinate422 = x3d.Coordinate()
Coordinate422.point = (-0.0867,0.4913,0.0318,-0.0801,0.0712,-0.0766)

LineSet421.coord = Coordinate422
#from r_knee to r_talocrural vertices 2
ColorRGBA423 = x3d.ColorRGBA()
ColorRGBA423.USE = "HAnimSegmentLineColorRGBA"

LineSet421.color = ColorRGBA423

Shape420.geometry = LineSet421

HAnimSegment416.children.append(Shape420)
HAnimSite424 = x3d.HAnimSite()
HAnimSite424.name = "r_calcaneus_posterior_pt"
HAnimSite424.DEF = "hanim_r_calcaneus_posterior_pt"
HAnimSite424.translation = [-0.0692,0.0297,-0.1221]
TouchSensor425 = x3d.TouchSensor()
TouchSensor425.description = "HAnimSite r_calcaneus_posterior_pt"

HAnimSite424.children.append(TouchSensor425)
Shape426 = x3d.Shape()
Shape426.USE = "HAnimSiteShape"

HAnimSite424.children.append(Shape426)

HAnimSegment416.children.append(HAnimSite424)
HAnimSite427 = x3d.HAnimSite()
HAnimSite427.name = "r_sphyrion_pt"
HAnimSite427.DEF = "hanim_r_sphyrion_pt"
HAnimSite427.translation = [-0.0603,0.061,-0.1002]
TouchSensor428 = x3d.TouchSensor()
TouchSensor428.description = "HAnimSite r_sphyrion_pt"

HAnimSite427.children.append(TouchSensor428)
Shape429 = x3d.Shape()
Shape429.USE = "HAnimSiteShape"

HAnimSite427.children.append(Shape429)

HAnimSegment416.children.append(HAnimSite427)

HAnimJoint415.children.append(HAnimSegment416)
HAnimJoint430 = x3d.HAnimJoint()
HAnimJoint430.name = "r_talocrural"
HAnimJoint430.DEF = "hanim_r_talocrural"
HAnimJoint430.center = [-0.0801,0.0712,-0.0766]
HAnimJoint430.ulimit = [0,0,0]
HAnimJoint430.llimit = [0,0,0]
HAnimSegment431 = x3d.HAnimSegment()
HAnimSegment431.name = "r_talus"
HAnimSegment431.DEF = "hanim_r_talus"
Transform432 = x3d.Transform()
Transform432.scale = [0.15,0.15,0.15]
Transform432.translation = [-0.05,0.06,-0.025]
Transform432.rotation = [1,0,0,-1.57]
#Transform right foot
Transform433 = x3d.Transform()
#Empty Transform right foot
Shape434 = x3d.Shape()
Shape434.USE = "HAnimJointShape"

Transform433.children.append(Shape434)

Transform432.children.append(Transform433)

HAnimSegment431.children.append(Transform432)
Shape435 = x3d.Shape()
LineSet436 = x3d.LineSet()
LineSet436.vertexCount = [2]
Coordinate437 = x3d.Coordinate()
Coordinate437.point = (-0.0801,0.0712,-0.0766,-0.0801,0.0712,-0.0766)

LineSet436.coord = Coordinate437
#from r_talocrural to r_talocalcaneonavicular vertices 2
ColorRGBA438 = x3d.ColorRGBA()
ColorRGBA438.USE = "HAnimSegmentLineColorRGBA"

LineSet436.color = ColorRGBA438

Shape435.geometry = LineSet436

HAnimSegment431.children.append(Shape435)
Shape439 = x3d.Shape()
LineSet440 = x3d.LineSet()
LineSet440.vertexCount = [2]
Coordinate441 = x3d.Coordinate()
Coordinate441.point = (-0.0801,0.0712,-0.0766,-0.0801,0.0712,-0.0766)

LineSet440.coord = Coordinate441
#from r_talocrural to r_calcaneocuboid vertices 2
ColorRGBA442 = x3d.ColorRGBA()
ColorRGBA442.USE = "HAnimSegmentLineColorRGBA"

LineSet440.color = ColorRGBA442

Shape439.geometry = LineSet440

HAnimSegment431.children.append(Shape439)

HAnimJoint430.children.append(HAnimSegment431)
HAnimJoint443 = x3d.HAnimJoint()
HAnimJoint443.name = "r_talocalcaneonavicular"
HAnimJoint443.DEF = "hanim_r_talocalcaneonavicular"
HAnimJoint443.ulimit = [0,0,0]
HAnimJoint443.llimit = [0,0,0]
HAnimSegment444 = x3d.HAnimSegment()
HAnimSegment444.name = "r_navicular"
HAnimSegment444.DEF = "hanim_r_navicular"
Transform445 = x3d.Transform()
Transform445.translation = [-0.0801,0.0712,-0.0766]
Transform446 = x3d.Transform()
#Empty Transform
Shape447 = x3d.Shape()
Shape447.USE = "HAnimJointShape"

Transform446.children.append(Shape447)

Transform445.children.append(Transform446)

HAnimSegment444.children.append(Transform445)
Shape448 = x3d.Shape()
LineSet449 = x3d.LineSet()
LineSet449.vertexCount = [2]
Coordinate450 = x3d.Coordinate()
Coordinate450.point = (-0.0801,0.0712,-0.0766)

LineSet449.coord = Coordinate450
#from r_talocalcaneonavicular to r_cuneonavicular_1 vertices 1
ColorRGBA451 = x3d.ColorRGBA()
ColorRGBA451.USE = "HAnimSegmentLineColorRGBA"

LineSet449.color = ColorRGBA451

Shape448.geometry = LineSet449

HAnimSegment444.children.append(Shape448)
Shape452 = x3d.Shape()
LineSet453 = x3d.LineSet()
LineSet453.vertexCount = [2]
Coordinate454 = x3d.Coordinate()
Coordinate454.point = (-0.0801,0.0712,-0.0766)

LineSet453.coord = Coordinate454
#from r_talocalcaneonavicular to r_cuneonavicular_2 vertices 1
ColorRGBA455 = x3d.ColorRGBA()
ColorRGBA455.USE = "HAnimSegmentLineColorRGBA"

LineSet453.color = ColorRGBA455

Shape452.geometry = LineSet453

HAnimSegment444.children.append(Shape452)
Shape456 = x3d.Shape()
LineSet457 = x3d.LineSet()
LineSet457.vertexCount = [2]
Coordinate458 = x3d.Coordinate()
Coordinate458.point = (-0.0801,0.0712,-0.0766)

LineSet457.coord = Coordinate458
#from r_talocalcaneonavicular to r_cuneonavicular_3 vertices 1
ColorRGBA459 = x3d.ColorRGBA()
ColorRGBA459.USE = "HAnimSegmentLineColorRGBA"

LineSet457.color = ColorRGBA459

Shape456.geometry = LineSet457

HAnimSegment444.children.append(Shape456)

HAnimJoint443.children.append(HAnimSegment444)
HAnimJoint460 = x3d.HAnimJoint()
HAnimJoint460.name = "r_cuneonavicular_1"
HAnimJoint460.DEF = "hanim_r_cuneonavicular_1"
HAnimJoint460.ulimit = [0,0,0]
HAnimJoint460.llimit = [0,0,0]
HAnimSegment461 = x3d.HAnimSegment()
HAnimSegment461.name = "r_cuneiform_1"
HAnimSegment461.DEF = "hanim_r_cuneiform_1"
Transform462 = x3d.Transform()
Transform462.translation = [-0.0801,0.0712,-0.0766]
Transform463 = x3d.Transform()
#Empty Transform
Shape464 = x3d.Shape()
Shape464.USE = "HAnimJointShape"

Transform463.children.append(Shape464)

Transform462.children.append(Transform463)

HAnimSegment461.children.append(Transform462)
Shape465 = x3d.Shape()
LineSet466 = x3d.LineSet()
LineSet466.vertexCount = [2]
Coordinate467 = x3d.Coordinate()
Coordinate467.point = (-0.0801,0.0712,-0.0766)

LineSet466.coord = Coordinate467
#from r_cuneonavicular_1 to r_tarsometatarsal_1 vertices 1
ColorRGBA468 = x3d.ColorRGBA()
ColorRGBA468.USE = "HAnimSegmentLineColorRGBA"

LineSet466.color = ColorRGBA468

Shape465.geometry = LineSet466

HAnimSegment461.children.append(Shape465)

HAnimJoint460.children.append(HAnimSegment461)
HAnimJoint469 = x3d.HAnimJoint()
HAnimJoint469.name = "r_tarsometatarsal_1"
HAnimJoint469.DEF = "hanim_r_tarsometatarsal_1"
HAnimJoint469.ulimit = [0,0,0]
HAnimJoint469.llimit = [0,0,0]
HAnimSegment470 = x3d.HAnimSegment()
HAnimSegment470.name = "r_metatarsal_1"
HAnimSegment470.DEF = "hanim_r_metatarsal_1"
Transform471 = x3d.Transform()
Transform471.translation = [-0.0801,0.0712,-0.0766]
Transform472 = x3d.Transform()
#Empty Transform
Shape473 = x3d.Shape()
Shape473.USE = "HAnimJointShape"

Transform472.children.append(Shape473)

Transform471.children.append(Transform472)

HAnimSegment470.children.append(Transform471)
Shape474 = x3d.Shape()
LineSet475 = x3d.LineSet()
LineSet475.vertexCount = [2]
Coordinate476 = x3d.Coordinate()
Coordinate476.point = (-0.0801,0.0712,-0.0766)

LineSet475.coord = Coordinate476
#from r_tarsometatarsal_1 to r_metatarsophalangeal_1 vertices 1
ColorRGBA477 = x3d.ColorRGBA()
ColorRGBA477.USE = "HAnimSegmentLineColorRGBA"

LineSet475.color = ColorRGBA477

Shape474.geometry = LineSet475

HAnimSegment470.children.append(Shape474)
HAnimSite478 = x3d.HAnimSite()
HAnimSite478.name = "r_metatarsal_phalanx_1_pt"
HAnimSite478.DEF = "hanim_r_metatarsal_phalanx_1_pt"
TouchSensor479 = x3d.TouchSensor()
TouchSensor479.description = "HAnimSite r_metatarsal_phalanx_1_pt"

HAnimSite478.children.append(TouchSensor479)
Shape480 = x3d.Shape()
Shape480.USE = "HAnimSiteShape"

HAnimSite478.children.append(Shape480)

HAnimSegment470.children.append(HAnimSite478)

HAnimJoint469.children.append(HAnimSegment470)
HAnimJoint481 = x3d.HAnimJoint()
HAnimJoint481.name = "r_metatarsophalangeal_1"
HAnimJoint481.DEF = "hanim_r_metatarsophalangeal_1"
HAnimJoint481.ulimit = [0,0,0]
HAnimJoint481.llimit = [0,0,0]
HAnimSegment482 = x3d.HAnimSegment()
HAnimSegment482.name = "r_tarsal_proximal_phalanx_1"
HAnimSegment482.DEF = "hanim_r_tarsal_proximal_phalanx_1"
Transform483 = x3d.Transform()
Transform483.translation = [-0.0801,0.0712,-0.0766]
Transform484 = x3d.Transform()
#Empty Transform
Shape485 = x3d.Shape()
Shape485.USE = "HAnimJointShape"

Transform484.children.append(Shape485)

Transform483.children.append(Transform484)

HAnimSegment482.children.append(Transform483)
Shape486 = x3d.Shape()
LineSet487 = x3d.LineSet()
LineSet487.vertexCount = [2]
Coordinate488 = x3d.Coordinate()
Coordinate488.point = (-0.0801,0.0712,-0.0766)

LineSet487.coord = Coordinate488
#from r_metatarsophalangeal_1 to r_tarsal_interphalangeal_1 vertices 1
ColorRGBA489 = x3d.ColorRGBA()
ColorRGBA489.USE = "HAnimSegmentLineColorRGBA"

LineSet487.color = ColorRGBA489

Shape486.geometry = LineSet487

HAnimSegment482.children.append(Shape486)
HAnimSite490 = x3d.HAnimSite()
HAnimSite490.name = "r_tarsal_distal_phalanx_1_tip"
HAnimSite490.DEF = "hanim_r_tarsal_distal_phalanx_1_tip"
TouchSensor491 = x3d.TouchSensor()
TouchSensor491.description = "HAnimSite r_tarsal_distal_phalanx_1_tip"

HAnimSite490.children.append(TouchSensor491)
Shape492 = x3d.Shape()
Shape492.USE = "HAnimSiteShape"

HAnimSite490.children.append(Shape492)

HAnimSegment482.children.append(HAnimSite490)

HAnimJoint481.children.append(HAnimSegment482)
HAnimJoint493 = x3d.HAnimJoint()
HAnimJoint493.name = "r_tarsal_interphalangeal_1"
HAnimJoint493.DEF = "hanim_r_tarsal_interphalangeal_1"
HAnimJoint493.ulimit = [0,0,0]
HAnimJoint493.llimit = [0,0,0]

HAnimJoint481.children.append(HAnimJoint493)

HAnimJoint469.children.append(HAnimJoint481)

HAnimJoint460.children.append(HAnimJoint469)

HAnimJoint443.children.append(HAnimJoint460)
HAnimJoint494 = x3d.HAnimJoint()
HAnimJoint494.name = "r_cuneonavicular_2"
HAnimJoint494.DEF = "hanim_r_cuneonavicular_2"
HAnimJoint494.ulimit = [0,0,0]
HAnimJoint494.llimit = [0,0,0]
HAnimSegment495 = x3d.HAnimSegment()
HAnimSegment495.name = "r_cuneiform_2"
HAnimSegment495.DEF = "hanim_r_cuneiform_2"
Transform496 = x3d.Transform()
Transform496.translation = [-0.0801,0.0712,-0.0766]
Transform497 = x3d.Transform()
#Empty Transform
Shape498 = x3d.Shape()
Shape498.USE = "HAnimJointShape"

Transform497.children.append(Shape498)

Transform496.children.append(Transform497)

HAnimSegment495.children.append(Transform496)
Shape499 = x3d.Shape()
LineSet500 = x3d.LineSet()
LineSet500.vertexCount = [2]
Coordinate501 = x3d.Coordinate()
Coordinate501.point = (-0.0801,0.0712,-0.0766)

LineSet500.coord = Coordinate501
#from r_cuneonavicular_2 to r_tarsometatarsal_2 vertices 1
ColorRGBA502 = x3d.ColorRGBA()
ColorRGBA502.USE = "HAnimSegmentLineColorRGBA"

LineSet500.color = ColorRGBA502

Shape499.geometry = LineSet500

HAnimSegment495.children.append(Shape499)

HAnimJoint494.children.append(HAnimSegment495)
HAnimJoint503 = x3d.HAnimJoint()
HAnimJoint503.name = "r_tarsometatarsal_2"
HAnimJoint503.DEF = "hanim_r_tarsometatarsal_2"
HAnimJoint503.ulimit = [0,0,0]
HAnimJoint503.llimit = [0,0,0]
HAnimSegment504 = x3d.HAnimSegment()
HAnimSegment504.name = "r_metatarsal_2"
HAnimSegment504.DEF = "hanim_r_metatarsal_2"
Transform505 = x3d.Transform()
Transform505.translation = [-0.0801,0.0712,-0.0766]
Transform506 = x3d.Transform()
#Empty Transform
Shape507 = x3d.Shape()
Shape507.USE = "HAnimJointShape"

Transform506.children.append(Shape507)

Transform505.children.append(Transform506)

HAnimSegment504.children.append(Transform505)
Shape508 = x3d.Shape()
LineSet509 = x3d.LineSet()
LineSet509.vertexCount = [2]
Coordinate510 = x3d.Coordinate()
Coordinate510.point = (-0.0801,0.0712,-0.0766)

LineSet509.coord = Coordinate510
#from r_tarsometatarsal_2 to r_metatarsophalangeal_2 vertices 1
ColorRGBA511 = x3d.ColorRGBA()
ColorRGBA511.USE = "HAnimSegmentLineColorRGBA"

LineSet509.color = ColorRGBA511

Shape508.geometry = LineSet509

HAnimSegment504.children.append(Shape508)

HAnimJoint503.children.append(HAnimSegment504)
HAnimJoint512 = x3d.HAnimJoint()
HAnimJoint512.name = "r_metatarsophalangeal_2"
HAnimJoint512.DEF = "hanim_r_metatarsophalangeal_2"
HAnimJoint512.ulimit = [0,0,0]
HAnimJoint512.llimit = [0,0,0]
HAnimSegment513 = x3d.HAnimSegment()
HAnimSegment513.name = "r_tarsal_proximal_phalanx_2"
HAnimSegment513.DEF = "hanim_r_tarsal_proximal_phalanx_2"
Transform514 = x3d.Transform()
Transform514.translation = [-0.0801,0.0712,-0.0766]
Transform515 = x3d.Transform()
#Empty Transform
Shape516 = x3d.Shape()
Shape516.USE = "HAnimJointShape"

Transform515.children.append(Shape516)

Transform514.children.append(Transform515)

HAnimSegment513.children.append(Transform514)
Shape517 = x3d.Shape()
LineSet518 = x3d.LineSet()
LineSet518.vertexCount = [2]
Coordinate519 = x3d.Coordinate()
Coordinate519.point = (-0.0801,0.0712,-0.0766)

LineSet518.coord = Coordinate519
#from r_metatarsophalangeal_2 to r_tarsal_proximal_interphalangeal_2 vertices 1
ColorRGBA520 = x3d.ColorRGBA()
ColorRGBA520.USE = "HAnimSegmentLineColorRGBA"

LineSet518.color = ColorRGBA520

Shape517.geometry = LineSet518

HAnimSegment513.children.append(Shape517)

HAnimJoint512.children.append(HAnimSegment513)
HAnimJoint521 = x3d.HAnimJoint()
HAnimJoint521.name = "r_tarsal_proximal_interphalangeal_2"
HAnimJoint521.DEF = "hanim_r_tarsal_proximal_interphalangeal_2"
HAnimJoint521.ulimit = [0,0,0]
HAnimJoint521.llimit = [0,0,0]
HAnimSegment522 = x3d.HAnimSegment()
HAnimSegment522.name = "r_tarsal_middle_phalanx_2"
HAnimSegment522.DEF = "hanim_r_tarsal_middle_phalanx_2"
Transform523 = x3d.Transform()
Transform523.translation = [-0.0801,0.0712,-0.0766]
Transform524 = x3d.Transform()
#Empty Transform
Shape525 = x3d.Shape()
Shape525.USE = "HAnimJointShape"

Transform524.children.append(Shape525)

Transform523.children.append(Transform524)

HAnimSegment522.children.append(Transform523)
Shape526 = x3d.Shape()
LineSet527 = x3d.LineSet()
LineSet527.vertexCount = [2]
Coordinate528 = x3d.Coordinate()
Coordinate528.point = (-0.0801,0.0712,-0.0766)

LineSet527.coord = Coordinate528
#from r_tarsal_proximal_interphalangeal_2 to r_tarsal_distal_interphalangeal_2 vertices 1
ColorRGBA529 = x3d.ColorRGBA()
ColorRGBA529.USE = "HAnimSegmentLineColorRGBA"

LineSet527.color = ColorRGBA529

Shape526.geometry = LineSet527

HAnimSegment522.children.append(Shape526)
HAnimSite530 = x3d.HAnimSite()
HAnimSite530.name = "r_tarsal_distal_phalanx_2_tip"
HAnimSite530.DEF = "hanim_r_tarsal_distal_phalanx_2_tip"
HAnimSite530.translation = [-0.0883,0.0134,0.1383]
TouchSensor531 = x3d.TouchSensor()
TouchSensor531.description = "HAnimSite r_tarsal_distal_phalanx_2_tip"

HAnimSite530.children.append(TouchSensor531)
Shape532 = x3d.Shape()
Shape532.USE = "HAnimSiteShape"

HAnimSite530.children.append(Shape532)

HAnimSegment522.children.append(HAnimSite530)

HAnimJoint521.children.append(HAnimSegment522)
HAnimJoint533 = x3d.HAnimJoint()
HAnimJoint533.name = "r_tarsal_distal_interphalangeal_2"
HAnimJoint533.DEF = "hanim_r_tarsal_distal_interphalangeal_2"
HAnimJoint533.ulimit = [0,0,0]
HAnimJoint533.llimit = [0,0,0]

HAnimJoint521.children.append(HAnimJoint533)

HAnimJoint512.children.append(HAnimJoint521)

HAnimJoint503.children.append(HAnimJoint512)

HAnimJoint494.children.append(HAnimJoint503)

HAnimJoint443.children.append(HAnimJoint494)
HAnimJoint534 = x3d.HAnimJoint()
HAnimJoint534.name = "r_cuneonavicular_3"
HAnimJoint534.DEF = "hanim_r_cuneonavicular_3"
HAnimJoint534.ulimit = [0,0,0]
HAnimJoint534.llimit = [0,0,0]
HAnimSegment535 = x3d.HAnimSegment()
HAnimSegment535.name = "r_cuneiform_3"
HAnimSegment535.DEF = "hanim_r_cuneiform_3"
Transform536 = x3d.Transform()
Transform536.translation = [-0.0801,0.0712,-0.0766]
Transform537 = x3d.Transform()
#Empty Transform
Shape538 = x3d.Shape()
Shape538.USE = "HAnimJointShape"

Transform537.children.append(Shape538)

Transform536.children.append(Transform537)

HAnimSegment535.children.append(Transform536)
Shape539 = x3d.Shape()
LineSet540 = x3d.LineSet()
LineSet540.vertexCount = [2]
Coordinate541 = x3d.Coordinate()
Coordinate541.point = (-0.0801,0.0712,-0.0766)

LineSet540.coord = Coordinate541
#from r_cuneonavicular_3 to r_tarsometatarsal_3 vertices 1
ColorRGBA542 = x3d.ColorRGBA()
ColorRGBA542.USE = "HAnimSegmentLineColorRGBA"

LineSet540.color = ColorRGBA542

Shape539.geometry = LineSet540

HAnimSegment535.children.append(Shape539)

HAnimJoint534.children.append(HAnimSegment535)
HAnimJoint543 = x3d.HAnimJoint()
HAnimJoint543.name = "r_tarsometatarsal_3"
HAnimJoint543.DEF = "hanim_r_tarsometatarsal_3"
HAnimJoint543.ulimit = [0,0,0]
HAnimJoint543.llimit = [0,0,0]
HAnimSegment544 = x3d.HAnimSegment()
HAnimSegment544.name = "r_metatarsal_3"
HAnimSegment544.DEF = "hanim_r_metatarsal_3"
Transform545 = x3d.Transform()
Transform545.translation = [-0.0801,0.0712,-0.0766]
Transform546 = x3d.Transform()
#Empty Transform
Shape547 = x3d.Shape()
Shape547.USE = "HAnimJointShape"

Transform546.children.append(Shape547)

Transform545.children.append(Transform546)

HAnimSegment544.children.append(Transform545)
Shape548 = x3d.Shape()
LineSet549 = x3d.LineSet()
LineSet549.vertexCount = [2]
Coordinate550 = x3d.Coordinate()
Coordinate550.point = (-0.0801,0.0712,-0.0766)

LineSet549.coord = Coordinate550
#from r_tarsometatarsal_3 to r_metatarsophalangeal_3 vertices 1
ColorRGBA551 = x3d.ColorRGBA()
ColorRGBA551.USE = "HAnimSegmentLineColorRGBA"

LineSet549.color = ColorRGBA551

Shape548.geometry = LineSet549

HAnimSegment544.children.append(Shape548)

HAnimJoint543.children.append(HAnimSegment544)
HAnimJoint552 = x3d.HAnimJoint()
HAnimJoint552.name = "r_metatarsophalangeal_3"
HAnimJoint552.DEF = "hanim_r_metatarsophalangeal_3"
HAnimJoint552.ulimit = [0,0,0]
HAnimJoint552.llimit = [0,0,0]
HAnimSegment553 = x3d.HAnimSegment()
HAnimSegment553.name = "r_tarsal_proximal_phalanx_3"
HAnimSegment553.DEF = "hanim_r_tarsal_proximal_phalanx_3"
Transform554 = x3d.Transform()
Transform554.translation = [-0.0801,0.0712,-0.0766]
Transform555 = x3d.Transform()
#Empty Transform
Shape556 = x3d.Shape()
Shape556.USE = "HAnimJointShape"

Transform555.children.append(Shape556)

Transform554.children.append(Transform555)

HAnimSegment553.children.append(Transform554)
Shape557 = x3d.Shape()
LineSet558 = x3d.LineSet()
LineSet558.vertexCount = [2]
Coordinate559 = x3d.Coordinate()
Coordinate559.point = (-0.0801,0.0712,-0.0766)

LineSet558.coord = Coordinate559
#from r_metatarsophalangeal_3 to r_tarsal_proximal_interphalangeal_3 vertices 1
ColorRGBA560 = x3d.ColorRGBA()
ColorRGBA560.USE = "HAnimSegmentLineColorRGBA"

LineSet558.color = ColorRGBA560

Shape557.geometry = LineSet558

HAnimSegment553.children.append(Shape557)

HAnimJoint552.children.append(HAnimSegment553)
HAnimJoint561 = x3d.HAnimJoint()
HAnimJoint561.name = "r_tarsal_proximal_interphalangeal_3"
HAnimJoint561.DEF = "hanim_r_tarsal_proximal_interphalangeal_3"
HAnimJoint561.ulimit = [0,0,0]
HAnimJoint561.llimit = [0,0,0]
HAnimSegment562 = x3d.HAnimSegment()
HAnimSegment562.name = "r_tarsal_middle_phalanx_3"
HAnimSegment562.DEF = "hanim_r_tarsal_middle_phalanx_3"
Transform563 = x3d.Transform()
Transform563.translation = [-0.0801,0.0712,-0.0766]
Transform564 = x3d.Transform()
#Empty Transform
Shape565 = x3d.Shape()
Shape565.USE = "HAnimJointShape"

Transform564.children.append(Shape565)

Transform563.children.append(Transform564)

HAnimSegment562.children.append(Transform563)
Shape566 = x3d.Shape()
LineSet567 = x3d.LineSet()
LineSet567.vertexCount = [2]
Coordinate568 = x3d.Coordinate()
Coordinate568.point = (-0.0801,0.0712,-0.0766)

LineSet567.coord = Coordinate568
#from r_tarsal_proximal_interphalangeal_3 to r_tarsal_distal_interphalangeal_3 vertices 1
ColorRGBA569 = x3d.ColorRGBA()
ColorRGBA569.USE = "HAnimSegmentLineColorRGBA"

LineSet567.color = ColorRGBA569

Shape566.geometry = LineSet567

HAnimSegment562.children.append(Shape566)
HAnimSite570 = x3d.HAnimSite()
HAnimSite570.name = "r_tarsal_distal_phalanx_3_tip"
HAnimSite570.DEF = "hanim_r_tarsal_distal_phalanx_3_tip"
TouchSensor571 = x3d.TouchSensor()
TouchSensor571.description = "HAnimSite r_tarsal_distal_phalanx_3_tip"

HAnimSite570.children.append(TouchSensor571)
Shape572 = x3d.Shape()
Shape572.USE = "HAnimSiteShape"

HAnimSite570.children.append(Shape572)

HAnimSegment562.children.append(HAnimSite570)

HAnimJoint561.children.append(HAnimSegment562)
HAnimJoint573 = x3d.HAnimJoint()
HAnimJoint573.name = "r_tarsal_distal_interphalangeal_3"
HAnimJoint573.DEF = "hanim_r_tarsal_distal_interphalangeal_3"
HAnimJoint573.ulimit = [0,0,0]
HAnimJoint573.llimit = [0,0,0]

HAnimJoint561.children.append(HAnimJoint573)

HAnimJoint552.children.append(HAnimJoint561)

HAnimJoint543.children.append(HAnimJoint552)

HAnimJoint534.children.append(HAnimJoint543)

HAnimJoint443.children.append(HAnimJoint534)

HAnimJoint430.children.append(HAnimJoint443)
HAnimJoint574 = x3d.HAnimJoint()
HAnimJoint574.name = "r_calcaneocuboid"
HAnimJoint574.DEF = "hanim_r_calcaneocuboid"
HAnimJoint574.ulimit = [0,0,0]
HAnimJoint574.llimit = [0,0,0]
HAnimSegment575 = x3d.HAnimSegment()
HAnimSegment575.name = "r_calcaneus"
HAnimSegment575.DEF = "hanim_r_calcaneus"
Transform576 = x3d.Transform()
Transform576.translation = [-0.0801,0.0712,-0.0766]
Transform577 = x3d.Transform()
#Empty Transform
Shape578 = x3d.Shape()
Shape578.USE = "HAnimJointShape"

Transform577.children.append(Shape578)

Transform576.children.append(Transform577)

HAnimSegment575.children.append(Transform576)
Shape579 = x3d.Shape()
LineSet580 = x3d.LineSet()
LineSet580.vertexCount = [2]
Coordinate581 = x3d.Coordinate()
Coordinate581.point = (-0.0801,0.0712,-0.0766)

LineSet580.coord = Coordinate581
#from r_calcaneocuboid to r_transversetarsal vertices 1
ColorRGBA582 = x3d.ColorRGBA()
ColorRGBA582.USE = "HAnimSegmentLineColorRGBA"

LineSet580.color = ColorRGBA582

Shape579.geometry = LineSet580

HAnimSegment575.children.append(Shape579)

HAnimJoint574.children.append(HAnimSegment575)
HAnimJoint583 = x3d.HAnimJoint()
HAnimJoint583.name = "r_transversetarsal"
HAnimJoint583.DEF = "hanim_r_transversetarsal"
HAnimJoint583.ulimit = [0,0,0]
HAnimJoint583.llimit = [0,0,0]
HAnimSegment584 = x3d.HAnimSegment()
HAnimSegment584.name = "r_cuboid"
HAnimSegment584.DEF = "hanim_r_cuboid"
Transform585 = x3d.Transform()
Transform585.translation = [-0.0801,0.0712,-0.0766]
Transform586 = x3d.Transform()
#Empty Transform
Shape587 = x3d.Shape()
Shape587.USE = "HAnimJointShape"

Transform586.children.append(Shape587)

Transform585.children.append(Transform586)

HAnimSegment584.children.append(Transform585)
Shape588 = x3d.Shape()
LineSet589 = x3d.LineSet()
LineSet589.vertexCount = [2]
Coordinate590 = x3d.Coordinate()
Coordinate590.point = (-0.0801,0.0712,-0.0766)

LineSet589.coord = Coordinate590
#from r_transversetarsal to r_tarsometatarsal_4 vertices 1
ColorRGBA591 = x3d.ColorRGBA()
ColorRGBA591.USE = "HAnimSegmentLineColorRGBA"

LineSet589.color = ColorRGBA591

Shape588.geometry = LineSet589

HAnimSegment584.children.append(Shape588)
Shape592 = x3d.Shape()
LineSet593 = x3d.LineSet()
LineSet593.vertexCount = [2]
Coordinate594 = x3d.Coordinate()
Coordinate594.point = (-0.0801,0.0712,-0.0766)

LineSet593.coord = Coordinate594
#from r_transversetarsal to r_tarsometatarsal_5 vertices 1
ColorRGBA595 = x3d.ColorRGBA()
ColorRGBA595.USE = "HAnimSegmentLineColorRGBA"

LineSet593.color = ColorRGBA595

Shape592.geometry = LineSet593

HAnimSegment584.children.append(Shape592)

HAnimJoint583.children.append(HAnimSegment584)
HAnimJoint596 = x3d.HAnimJoint()
HAnimJoint596.name = "r_tarsometatarsal_4"
HAnimJoint596.DEF = "hanim_r_tarsometatarsal_4"
HAnimJoint596.ulimit = [0,0,0]
HAnimJoint596.llimit = [0,0,0]
HAnimSegment597 = x3d.HAnimSegment()
HAnimSegment597.name = "r_metatarsal_4"
HAnimSegment597.DEF = "hanim_r_metatarsal_4"
Transform598 = x3d.Transform()
Transform598.translation = [-0.0801,0.0712,-0.0766]
Transform599 = x3d.Transform()
#Empty Transform
Shape600 = x3d.Shape()
Shape600.USE = "HAnimJointShape"

Transform599.children.append(Shape600)

Transform598.children.append(Transform599)

HAnimSegment597.children.append(Transform598)
Shape601 = x3d.Shape()
LineSet602 = x3d.LineSet()
LineSet602.vertexCount = [2]
Coordinate603 = x3d.Coordinate()
Coordinate603.point = (-0.0801,0.0712,-0.0766)

LineSet602.coord = Coordinate603
#from r_tarsometatarsal_4 to r_metatarsophalangeal_4 vertices 1
ColorRGBA604 = x3d.ColorRGBA()
ColorRGBA604.USE = "HAnimSegmentLineColorRGBA"

LineSet602.color = ColorRGBA604

Shape601.geometry = LineSet602

HAnimSegment597.children.append(Shape601)

HAnimJoint596.children.append(HAnimSegment597)
HAnimJoint605 = x3d.HAnimJoint()
HAnimJoint605.name = "r_metatarsophalangeal_4"
HAnimJoint605.DEF = "hanim_r_metatarsophalangeal_4"
HAnimJoint605.ulimit = [0,0,0]
HAnimJoint605.llimit = [0,0,0]
HAnimSegment606 = x3d.HAnimSegment()
HAnimSegment606.name = "r_tarsal_proximal_phalanx_4"
HAnimSegment606.DEF = "hanim_r_tarsal_proximal_phalanx_4"
Transform607 = x3d.Transform()
Transform607.translation = [-0.0801,0.0712,-0.0766]
Transform608 = x3d.Transform()
#Empty Transform
Shape609 = x3d.Shape()
Shape609.USE = "HAnimJointShape"

Transform608.children.append(Shape609)

Transform607.children.append(Transform608)

HAnimSegment606.children.append(Transform607)
Shape610 = x3d.Shape()
LineSet611 = x3d.LineSet()
LineSet611.vertexCount = [2]
Coordinate612 = x3d.Coordinate()
Coordinate612.point = (-0.0801,0.0712,-0.0766)

LineSet611.coord = Coordinate612
#from r_metatarsophalangeal_4 to r_tarsal_proximal_interphalangeal_4 vertices 1
ColorRGBA613 = x3d.ColorRGBA()
ColorRGBA613.USE = "HAnimSegmentLineColorRGBA"

LineSet611.color = ColorRGBA613

Shape610.geometry = LineSet611

HAnimSegment606.children.append(Shape610)

HAnimJoint605.children.append(HAnimSegment606)
HAnimJoint614 = x3d.HAnimJoint()
HAnimJoint614.name = "r_tarsal_proximal_interphalangeal_4"
HAnimJoint614.DEF = "hanim_r_tarsal_proximal_interphalangeal_4"
HAnimJoint614.ulimit = [0,0,0]
HAnimJoint614.llimit = [0,0,0]
HAnimSegment615 = x3d.HAnimSegment()
HAnimSegment615.name = "r_tarsal_middle_phalanx_4"
HAnimSegment615.DEF = "hanim_r_tarsal_middle_phalanx_4"
Transform616 = x3d.Transform()
Transform616.translation = [-0.0801,0.0712,-0.0766]
Transform617 = x3d.Transform()
#Empty Transform
Shape618 = x3d.Shape()
Shape618.USE = "HAnimJointShape"

Transform617.children.append(Shape618)

Transform616.children.append(Transform617)

HAnimSegment615.children.append(Transform616)
Shape619 = x3d.Shape()
LineSet620 = x3d.LineSet()
LineSet620.vertexCount = [2]
Coordinate621 = x3d.Coordinate()
Coordinate621.point = (-0.0801,0.0712,-0.0766)

LineSet620.coord = Coordinate621
#from r_tarsal_proximal_interphalangeal_4 to r_tarsal_distal_interphalangeal_4 vertices 1
ColorRGBA622 = x3d.ColorRGBA()
ColorRGBA622.USE = "HAnimSegmentLineColorRGBA"

LineSet620.color = ColorRGBA622

Shape619.geometry = LineSet620

HAnimSegment615.children.append(Shape619)
HAnimSite623 = x3d.HAnimSite()
HAnimSite623.name = "r_tarsal_distal_phalanx_4_tip"
HAnimSite623.DEF = "hanim_r_tarsal_distal_phalanx_4_tip"
TouchSensor624 = x3d.TouchSensor()
TouchSensor624.description = "HAnimSite r_tarsal_distal_phalanx_4_tip"

HAnimSite623.children.append(TouchSensor624)
Shape625 = x3d.Shape()
Shape625.USE = "HAnimSiteShape"

HAnimSite623.children.append(Shape625)

HAnimSegment615.children.append(HAnimSite623)

HAnimJoint614.children.append(HAnimSegment615)
HAnimJoint626 = x3d.HAnimJoint()
HAnimJoint626.name = "r_tarsal_distal_interphalangeal_4"
HAnimJoint626.DEF = "hanim_r_tarsal_distal_interphalangeal_4"
HAnimJoint626.ulimit = [0,0,0]
HAnimJoint626.llimit = [0,0,0]

HAnimJoint614.children.append(HAnimJoint626)

HAnimJoint605.children.append(HAnimJoint614)

HAnimJoint596.children.append(HAnimJoint605)

HAnimJoint583.children.append(HAnimJoint596)
HAnimJoint627 = x3d.HAnimJoint()
HAnimJoint627.name = "r_tarsometatarsal_5"
HAnimJoint627.DEF = "hanim_r_tarsometatarsal_5"
HAnimJoint627.ulimit = [0,0,0]
HAnimJoint627.llimit = [0,0,0]
HAnimSegment628 = x3d.HAnimSegment()
HAnimSegment628.name = "r_metatarsal_5"
HAnimSegment628.DEF = "hanim_r_metatarsal_5"
Transform629 = x3d.Transform()
Transform629.translation = [-0.0801,0.0712,-0.0766]
Transform630 = x3d.Transform()
#Empty Transform
Shape631 = x3d.Shape()
Shape631.USE = "HAnimJointShape"

Transform630.children.append(Shape631)

Transform629.children.append(Transform630)

HAnimSegment628.children.append(Transform629)
Shape632 = x3d.Shape()
LineSet633 = x3d.LineSet()
LineSet633.vertexCount = [2]
Coordinate634 = x3d.Coordinate()
Coordinate634.point = (-0.0801,0.0712,-0.0766)

LineSet633.coord = Coordinate634
#from r_tarsometatarsal_5 to r_metatarsophalangeal_5 vertices 1
ColorRGBA635 = x3d.ColorRGBA()
ColorRGBA635.USE = "HAnimSegmentLineColorRGBA"

LineSet633.color = ColorRGBA635

Shape632.geometry = LineSet633

HAnimSegment628.children.append(Shape632)
HAnimSite636 = x3d.HAnimSite()
HAnimSite636.name = "r_metatarsal_phalanx_5_pt"
HAnimSite636.DEF = "hanim_r_metatarsal_phalanx_5_pt"
TouchSensor637 = x3d.TouchSensor()
TouchSensor637.description = "HAnimSite r_metatarsal_phalanx_5_pt"

HAnimSite636.children.append(TouchSensor637)
Shape638 = x3d.Shape()
Shape638.USE = "HAnimSiteShape"

HAnimSite636.children.append(Shape638)

HAnimSegment628.children.append(HAnimSite636)

HAnimJoint627.children.append(HAnimSegment628)
HAnimJoint639 = x3d.HAnimJoint()
HAnimJoint639.name = "r_metatarsophalangeal_5"
HAnimJoint639.DEF = "hanim_r_metatarsophalangeal_5"
HAnimJoint639.ulimit = [0,0,0]
HAnimJoint639.llimit = [0,0,0]
HAnimSegment640 = x3d.HAnimSegment()
HAnimSegment640.name = "r_tarsal_proximal_phalanx_5"
HAnimSegment640.DEF = "hanim_r_tarsal_proximal_phalanx_5"
Transform641 = x3d.Transform()
Transform641.translation = [-0.0801,0.0712,-0.0766]
Transform642 = x3d.Transform()
#Empty Transform
Shape643 = x3d.Shape()
Shape643.USE = "HAnimJointShape"

Transform642.children.append(Shape643)

Transform641.children.append(Transform642)

HAnimSegment640.children.append(Transform641)
Shape644 = x3d.Shape()
LineSet645 = x3d.LineSet()
LineSet645.vertexCount = [2]
Coordinate646 = x3d.Coordinate()
Coordinate646.point = (-0.0801,0.0712,-0.0766)

LineSet645.coord = Coordinate646
#from r_metatarsophalangeal_5 to r_tarsal_proximal_interphalangeal_5 vertices 1
ColorRGBA647 = x3d.ColorRGBA()
ColorRGBA647.USE = "HAnimSegmentLineColorRGBA"

LineSet645.color = ColorRGBA647

Shape644.geometry = LineSet645

HAnimSegment640.children.append(Shape644)

HAnimJoint639.children.append(HAnimSegment640)
HAnimJoint648 = x3d.HAnimJoint()
HAnimJoint648.name = "r_tarsal_proximal_interphalangeal_5"
HAnimJoint648.DEF = "hanim_r_tarsal_proximal_interphalangeal_5"
HAnimJoint648.ulimit = [0,0,0]
HAnimJoint648.llimit = [0,0,0]
HAnimSegment649 = x3d.HAnimSegment()
HAnimSegment649.name = "r_tarsal_middle_phalanx_5"
HAnimSegment649.DEF = "hanim_r_tarsal_middle_phalanx_5"
Transform650 = x3d.Transform()
Transform650.translation = [-0.0801,0.0712,-0.0766]
Transform651 = x3d.Transform()
#Empty Transform
Shape652 = x3d.Shape()
Shape652.USE = "HAnimJointShape"

Transform651.children.append(Shape652)

Transform650.children.append(Transform651)

HAnimSegment649.children.append(Transform650)
Shape653 = x3d.Shape()
LineSet654 = x3d.LineSet()
LineSet654.vertexCount = [2]
Coordinate655 = x3d.Coordinate()
Coordinate655.point = (-0.0801,0.0712,-0.0766)

LineSet654.coord = Coordinate655
#from r_tarsal_proximal_interphalangeal_5 to r_tarsal_distal_interphalangeal_5 vertices 1
ColorRGBA656 = x3d.ColorRGBA()
ColorRGBA656.USE = "HAnimSegmentLineColorRGBA"

LineSet654.color = ColorRGBA656

Shape653.geometry = LineSet654

HAnimSegment649.children.append(Shape653)
HAnimSite657 = x3d.HAnimSite()
HAnimSite657.name = "r_tarsal_distal_phalanx_5_tip"
HAnimSite657.DEF = "hanim_r_tarsal_distal_phalanx_5_tip"
TouchSensor658 = x3d.TouchSensor()
TouchSensor658.description = "HAnimSite r_tarsal_distal_phalanx_5_tip"

HAnimSite657.children.append(TouchSensor658)
Shape659 = x3d.Shape()
Shape659.USE = "HAnimSiteShape"

HAnimSite657.children.append(Shape659)

HAnimSegment649.children.append(HAnimSite657)

HAnimJoint648.children.append(HAnimSegment649)
HAnimJoint660 = x3d.HAnimJoint()
HAnimJoint660.name = "r_tarsal_distal_interphalangeal_5"
HAnimJoint660.DEF = "hanim_r_tarsal_distal_interphalangeal_5"
HAnimJoint660.ulimit = [0,0,0]
HAnimJoint660.llimit = [0,0,0]

HAnimJoint648.children.append(HAnimJoint660)

HAnimJoint639.children.append(HAnimJoint648)

HAnimJoint627.children.append(HAnimJoint639)

HAnimJoint583.children.append(HAnimJoint627)

HAnimJoint574.children.append(HAnimJoint583)

HAnimJoint430.children.append(HAnimJoint574)

HAnimJoint415.children.append(HAnimJoint430)

HAnimJoint397.children.append(HAnimJoint415)

HAnimJoint96.children.append(HAnimJoint397)

HAnimJoint44.children.append(HAnimJoint96)
HAnimJoint661 = x3d.HAnimJoint()
HAnimJoint661.name = "vl5"
HAnimJoint661.DEF = "hanim_vl5"
HAnimJoint661.center = [0.0028,1.0568,-0.0776]
HAnimJoint661.ulimit = [0,0,0]
HAnimJoint661.llimit = [0,0,0]
HAnimSegment662 = x3d.HAnimSegment()
HAnimSegment662.name = "l5"
HAnimSegment662.DEF = "hanim_l5"
Transform663 = x3d.Transform()
Transform663.translation = [0.0028,1.0568,-0.0776]
Transform664 = x3d.Transform()
#Empty Transform
Shape665 = x3d.Shape()
Shape665.USE = "HAnimJointShape"

Transform664.children.append(Shape665)

Transform663.children.append(Transform664)

HAnimSegment662.children.append(Transform663)
Shape666 = x3d.Shape()
LineSet667 = x3d.LineSet()
LineSet667.vertexCount = [2]
Coordinate668 = x3d.Coordinate()
Coordinate668.point = (0.0028,1.0568,-0.0776,0.0035,1.0925,-0.0787)

LineSet667.coord = Coordinate668
#from vl5 to vl4 vertices 2
ColorRGBA669 = x3d.ColorRGBA()
ColorRGBA669.USE = "HAnimSegmentLineColorRGBA"

LineSet667.color = ColorRGBA669

Shape666.geometry = LineSet667

HAnimSegment662.children.append(Shape666)

HAnimJoint661.children.append(HAnimSegment662)
HAnimJoint670 = x3d.HAnimJoint()
HAnimJoint670.name = "vl4"
HAnimJoint670.DEF = "hanim_vl4"
HAnimJoint670.center = [0.0035,1.0925,-0.0787]
HAnimJoint670.ulimit = [0,0,0]
HAnimJoint670.llimit = [0,0,0]
HAnimSegment671 = x3d.HAnimSegment()
HAnimSegment671.name = "l4"
HAnimSegment671.DEF = "hanim_l4"
Transform672 = x3d.Transform()
Transform672.translation = [0.0035,1.0925,-0.0787]
Transform673 = x3d.Transform()
#Empty Transform
Shape674 = x3d.Shape()
Shape674.USE = "HAnimJointShape"

Transform673.children.append(Shape674)

Transform672.children.append(Transform673)

HAnimSegment671.children.append(Transform672)
Shape675 = x3d.Shape()
LineSet676 = x3d.LineSet()
LineSet676.vertexCount = [2]
Coordinate677 = x3d.Coordinate()
Coordinate677.point = (0.0035,1.0925,-0.0787,0.0041,1.1276,-0.0796)

LineSet676.coord = Coordinate677
#from vl4 to vl3 vertices 2
ColorRGBA678 = x3d.ColorRGBA()
ColorRGBA678.USE = "HAnimSegmentLineColorRGBA"

LineSet676.color = ColorRGBA678

Shape675.geometry = LineSet676

HAnimSegment671.children.append(Shape675)

HAnimJoint670.children.append(HAnimSegment671)
HAnimJoint679 = x3d.HAnimJoint()
HAnimJoint679.name = "vl3"
HAnimJoint679.DEF = "hanim_vl3"
HAnimJoint679.center = [0.0041,1.1276,-0.0796]
HAnimJoint679.ulimit = [0,0,0]
HAnimJoint679.llimit = [0,0,0]
HAnimSegment680 = x3d.HAnimSegment()
HAnimSegment680.name = "l3"
HAnimSegment680.DEF = "hanim_l3"
Transform681 = x3d.Transform()
Transform681.translation = [0.0041,1.1276,-0.0796]
Transform682 = x3d.Transform()
#Empty Transform
Shape683 = x3d.Shape()
Shape683.USE = "HAnimJointShape"

Transform682.children.append(Shape683)

Transform681.children.append(Transform682)

HAnimSegment680.children.append(Transform681)
Shape684 = x3d.Shape()
LineSet685 = x3d.LineSet()
LineSet685.vertexCount = [2]
Coordinate686 = x3d.Coordinate()
Coordinate686.point = (0.0041,1.1276,-0.0796,0.0045,1.1546,-0.0800)

LineSet685.coord = Coordinate686
#from vl3 to vl2 vertices 2
ColorRGBA687 = x3d.ColorRGBA()
ColorRGBA687.USE = "HAnimSegmentLineColorRGBA"

LineSet685.color = ColorRGBA687

Shape684.geometry = LineSet685

HAnimSegment680.children.append(Shape684)
HAnimSite688 = x3d.HAnimSite()
HAnimSite688.name = "l_rib10_pt"
HAnimSite688.DEF = "hanim_l_rib10_pt"
HAnimSite688.translation = [0.0871,1.1925,0.0992]
TouchSensor689 = x3d.TouchSensor()
TouchSensor689.description = "HAnimSite l_rib10_pt"

HAnimSite688.children.append(TouchSensor689)
Shape690 = x3d.Shape()
Shape690.USE = "HAnimSiteShape"

HAnimSite688.children.append(Shape690)

HAnimSegment680.children.append(HAnimSite688)
HAnimSite691 = x3d.HAnimSite()
HAnimSite691.name = "r_rib10_pt"
HAnimSite691.DEF = "hanim_r_rib10_pt"
HAnimSite691.translation = [-0.0711,1.1941,0.1016]
TouchSensor692 = x3d.TouchSensor()
TouchSensor692.description = "HAnimSite r_rib10_pt"

HAnimSite691.children.append(TouchSensor692)
Shape693 = x3d.Shape()
Shape693.USE = "HAnimSiteShape"

HAnimSite691.children.append(Shape693)

HAnimSegment680.children.append(HAnimSite691)
HAnimSite694 = x3d.HAnimSite()
HAnimSite694.name = "spine_2_middle_back_pt"
HAnimSite694.DEF = "hanim_spine_2_middle_back_pt"
TouchSensor695 = x3d.TouchSensor()
TouchSensor695.description = "HAnimSite spine_2_middle_back_pt"

HAnimSite694.children.append(TouchSensor695)
Shape696 = x3d.Shape()
Shape696.USE = "HAnimSiteShape"

HAnimSite694.children.append(Shape696)

HAnimSegment680.children.append(HAnimSite694)

HAnimJoint679.children.append(HAnimSegment680)
HAnimJoint697 = x3d.HAnimJoint()
HAnimJoint697.name = "vl2"
HAnimJoint697.DEF = "hanim_vl2"
HAnimJoint697.center = [0.0045,1.1546,-0.08]
HAnimJoint697.ulimit = [0,0,0]
HAnimJoint697.llimit = [0,0,0]
HAnimSegment698 = x3d.HAnimSegment()
HAnimSegment698.name = "l2"
HAnimSegment698.DEF = "hanim_l2"
Transform699 = x3d.Transform()
Transform699.translation = [0.0045,1.1546,-0.08]
Transform700 = x3d.Transform()
#Empty Transform
Shape701 = x3d.Shape()
Shape701.USE = "HAnimJointShape"

Transform700.children.append(Shape701)

Transform699.children.append(Transform700)

HAnimSegment698.children.append(Transform699)
Shape702 = x3d.Shape()
LineSet703 = x3d.LineSet()
LineSet703.vertexCount = [2]
Coordinate704 = x3d.Coordinate()
Coordinate704.point = (0.0045,1.1546,-0.0800,0.0048,1.1912,-0.0805)

LineSet703.coord = Coordinate704
#from vl2 to vl1 vertices 2
ColorRGBA705 = x3d.ColorRGBA()
ColorRGBA705.USE = "HAnimSegmentLineColorRGBA"

LineSet703.color = ColorRGBA705

Shape702.geometry = LineSet703

HAnimSegment698.children.append(Shape702)

HAnimJoint697.children.append(HAnimSegment698)
HAnimJoint706 = x3d.HAnimJoint()
HAnimJoint706.name = "vl1"
HAnimJoint706.DEF = "hanim_vl1"
HAnimJoint706.center = [0.0048,1.1912,-0.0805]
HAnimJoint706.ulimit = [0,0,0]
HAnimJoint706.llimit = [0,0,0]
HAnimSegment707 = x3d.HAnimSegment()
HAnimSegment707.name = "l1"
HAnimSegment707.DEF = "hanim_l1"
Transform708 = x3d.Transform()
Transform708.translation = [0.0048,1.1912,-0.0805]
Transform709 = x3d.Transform()
#Empty Transform
Shape710 = x3d.Shape()
Shape710.USE = "HAnimJointShape"

Transform709.children.append(Shape710)

Transform708.children.append(Transform709)

HAnimSegment707.children.append(Transform708)
Shape711 = x3d.Shape()
LineSet712 = x3d.LineSet()
LineSet712.vertexCount = [2]
Coordinate713 = x3d.Coordinate()
Coordinate713.point = (0.0048,1.1912,-0.0805,0.0051,1.2278,-0.0808)

LineSet712.coord = Coordinate713
#from vl1 to vt12 vertices 2
ColorRGBA714 = x3d.ColorRGBA()
ColorRGBA714.USE = "HAnimSegmentLineColorRGBA"

LineSet712.color = ColorRGBA714

Shape711.geometry = LineSet712

HAnimSegment707.children.append(Shape711)

HAnimJoint706.children.append(HAnimSegment707)
HAnimJoint715 = x3d.HAnimJoint()
HAnimJoint715.name = "vt12"
HAnimJoint715.DEF = "hanim_vt12"
HAnimJoint715.center = [0.0051,1.2278,-0.0808]
HAnimJoint715.ulimit = [0,0,0]
HAnimJoint715.llimit = [0,0,0]
HAnimSegment716 = x3d.HAnimSegment()
HAnimSegment716.name = "t12"
HAnimSegment716.DEF = "hanim_t12"
Transform717 = x3d.Transform()
Transform717.translation = [0.0051,1.2278,-0.0808]
Transform718 = x3d.Transform()
#Empty Transform
Shape719 = x3d.Shape()
Shape719.USE = "HAnimJointShape"

Transform718.children.append(Shape719)

Transform717.children.append(Transform718)

HAnimSegment716.children.append(Transform717)
Shape720 = x3d.Shape()
LineSet721 = x3d.LineSet()
LineSet721.vertexCount = [2]
Coordinate722 = x3d.Coordinate()
Coordinate722.point = (0.0051,1.2278,-0.0808,0.0053,1.2679,-0.0810)

LineSet721.coord = Coordinate722
#from vt12 to vt11 vertices 2
ColorRGBA723 = x3d.ColorRGBA()
ColorRGBA723.USE = "HAnimSegmentLineColorRGBA"

LineSet721.color = ColorRGBA723

Shape720.geometry = LineSet721

HAnimSegment716.children.append(Shape720)

HAnimJoint715.children.append(HAnimSegment716)
HAnimJoint724 = x3d.HAnimJoint()
HAnimJoint724.name = "vt11"
HAnimJoint724.DEF = "hanim_vt11"
HAnimJoint724.center = [0.0053,1.2679,-0.081]
HAnimJoint724.ulimit = [0,0,0]
HAnimJoint724.llimit = [0,0,0]
HAnimSegment725 = x3d.HAnimSegment()
HAnimSegment725.name = "t11"
HAnimSegment725.DEF = "hanim_t11"
Transform726 = x3d.Transform()
Transform726.translation = [0.0053,1.2679,-0.081]
Transform727 = x3d.Transform()
#Empty Transform
Shape728 = x3d.Shape()
Shape728.USE = "HAnimJointShape"

Transform727.children.append(Shape728)

Transform726.children.append(Transform727)

HAnimSegment725.children.append(Transform726)
Shape729 = x3d.Shape()
LineSet730 = x3d.LineSet()
LineSet730.vertexCount = [2]
Coordinate731 = x3d.Coordinate()
Coordinate731.point = (0.0053,1.2679,-0.0810,0.0056,1.2848,-0.0822)

LineSet730.coord = Coordinate731
#from vt11 to vt10 vertices 2
ColorRGBA732 = x3d.ColorRGBA()
ColorRGBA732.USE = "HAnimSegmentLineColorRGBA"

LineSet730.color = ColorRGBA732

Shape729.geometry = LineSet730

HAnimSegment725.children.append(Shape729)
HAnimSite733 = x3d.HAnimSite()
HAnimSite733.name = "substernale_pt"
HAnimSite733.DEF = "hanim_substernale_pt"
HAnimSite733.translation = [0.0085,1.2995,0.1147]
TouchSensor734 = x3d.TouchSensor()
TouchSensor734.description = "HAnimSite substernale_pt"

HAnimSite733.children.append(TouchSensor734)
Shape735 = x3d.Shape()
Shape735.USE = "HAnimSiteShape"

HAnimSite733.children.append(Shape735)

HAnimSegment725.children.append(HAnimSite733)

HAnimJoint724.children.append(HAnimSegment725)
HAnimJoint736 = x3d.HAnimJoint()
HAnimJoint736.name = "vt10"
HAnimJoint736.DEF = "hanim_vt10"
HAnimJoint736.center = [0.0056,1.2848,-0.0822]
HAnimJoint736.ulimit = [0,0,0]
HAnimJoint736.llimit = [0,0,0]
HAnimSegment737 = x3d.HAnimSegment()
HAnimSegment737.name = "t10"
HAnimSegment737.DEF = "hanim_t10"
Transform738 = x3d.Transform()
Transform738.translation = [0.0056,1.2848,-0.0822]
Transform739 = x3d.Transform()
#Empty Transform
Shape740 = x3d.Shape()
Shape740.USE = "HAnimJointShape"

Transform739.children.append(Shape740)

Transform738.children.append(Transform739)

HAnimSegment737.children.append(Transform738)
Shape741 = x3d.Shape()
LineSet742 = x3d.LineSet()
LineSet742.vertexCount = [2]
Coordinate743 = x3d.Coordinate()
Coordinate743.point = (0.0056,1.2848,-0.0822,0.0057,1.3126,-0.0838)

LineSet742.coord = Coordinate743
#from vt10 to vt9 vertices 2
ColorRGBA744 = x3d.ColorRGBA()
ColorRGBA744.USE = "HAnimSegmentLineColorRGBA"

LineSet742.color = ColorRGBA744

Shape741.geometry = LineSet742

HAnimSegment737.children.append(Shape741)
HAnimSite745 = x3d.HAnimSite()
HAnimSite745.name = "l_thelion_pt"
HAnimSite745.DEF = "hanim_l_thelion_pt"
HAnimSite745.translation = [0.0918,1.3382,0.1192]
TouchSensor746 = x3d.TouchSensor()
TouchSensor746.description = "HAnimSite l_thelion_pt"

HAnimSite745.children.append(TouchSensor746)
Shape747 = x3d.Shape()
Shape747.USE = "HAnimSiteShape"

HAnimSite745.children.append(Shape747)

HAnimSegment737.children.append(HAnimSite745)
HAnimSite748 = x3d.HAnimSite()
HAnimSite748.name = "r_thelion_pt"
HAnimSite748.DEF = "hanim_r_thelion_pt"
HAnimSite748.translation = [-0.0736,1.3385,0.1217]
TouchSensor749 = x3d.TouchSensor()
TouchSensor749.description = "HAnimSite r_thelion_pt"

HAnimSite748.children.append(TouchSensor749)
Shape750 = x3d.Shape()
Shape750.USE = "HAnimSiteShape"

HAnimSite748.children.append(Shape750)

HAnimSegment737.children.append(HAnimSite748)

HAnimJoint736.children.append(HAnimSegment737)
HAnimJoint751 = x3d.HAnimJoint()
HAnimJoint751.name = "vt9"
HAnimJoint751.DEF = "hanim_vt9"
HAnimJoint751.center = [0.0057,1.3126,-0.0838]
HAnimJoint751.ulimit = [0,0,0]
HAnimJoint751.llimit = [0,0,0]
HAnimSegment752 = x3d.HAnimSegment()
HAnimSegment752.name = "t9"
HAnimSegment752.DEF = "hanim_t9"
Transform753 = x3d.Transform()
Transform753.translation = [0.0057,1.3126,-0.0838]
Transform754 = x3d.Transform()
#Empty Transform
Shape755 = x3d.Shape()
Shape755.USE = "HAnimJointShape"

Transform754.children.append(Shape755)

Transform753.children.append(Transform754)

HAnimSegment752.children.append(Transform753)
Shape756 = x3d.Shape()
LineSet757 = x3d.LineSet()
LineSet757.vertexCount = [2]
Coordinate758 = x3d.Coordinate()
Coordinate758.point = (0.0057,1.3126,-0.0838,0.0057,1.3382,-0.0845)

LineSet757.coord = Coordinate758
#from vt9 to vt8 vertices 2
ColorRGBA759 = x3d.ColorRGBA()
ColorRGBA759.USE = "HAnimSegmentLineColorRGBA"

LineSet757.color = ColorRGBA759

Shape756.geometry = LineSet757

HAnimSegment752.children.append(Shape756)

HAnimJoint751.children.append(HAnimSegment752)
HAnimJoint760 = x3d.HAnimJoint()
HAnimJoint760.name = "vt8"
HAnimJoint760.DEF = "hanim_vt8"
HAnimJoint760.center = [0.0057,1.3382,-0.0845]
HAnimJoint760.ulimit = [0,0,0]
HAnimJoint760.llimit = [0,0,0]
HAnimSegment761 = x3d.HAnimSegment()
HAnimSegment761.name = "t8"
HAnimSegment761.DEF = "hanim_t8"
Transform762 = x3d.Transform()
Transform762.translation = [0.0057,1.3382,-0.0845]
Transform763 = x3d.Transform()
#Empty Transform
Shape764 = x3d.Shape()
Shape764.USE = "HAnimJointShape"

Transform763.children.append(Shape764)

Transform762.children.append(Transform763)

HAnimSegment761.children.append(Transform762)
Shape765 = x3d.Shape()
LineSet766 = x3d.LineSet()
LineSet766.vertexCount = [2]
Coordinate767 = x3d.Coordinate()
Coordinate767.point = (0.0057,1.3382,-0.0845,0.0058,1.3625,-0.0833)

LineSet766.coord = Coordinate767
#from vt8 to vt7 vertices 2
ColorRGBA768 = x3d.ColorRGBA()
ColorRGBA768.USE = "HAnimSegmentLineColorRGBA"

LineSet766.color = ColorRGBA768

Shape765.geometry = LineSet766

HAnimSegment761.children.append(Shape765)

HAnimJoint760.children.append(HAnimSegment761)
HAnimJoint769 = x3d.HAnimJoint()
HAnimJoint769.name = "vt7"
HAnimJoint769.DEF = "hanim_vt7"
HAnimJoint769.center = [0.0058,1.3625,-0.0833]
HAnimJoint769.ulimit = [0,0,0]
HAnimJoint769.llimit = [0,0,0]
HAnimSegment770 = x3d.HAnimSegment()
HAnimSegment770.name = "t7"
HAnimSegment770.DEF = "hanim_t7"
Transform771 = x3d.Transform()
Transform771.translation = [0.0058,1.3625,-0.0833]
Transform772 = x3d.Transform()
#Empty Transform
Shape773 = x3d.Shape()
Shape773.USE = "HAnimJointShape"

Transform772.children.append(Shape773)

Transform771.children.append(Transform772)

HAnimSegment770.children.append(Transform771)
Shape774 = x3d.Shape()
LineSet775 = x3d.LineSet()
LineSet775.vertexCount = [2]
Coordinate776 = x3d.Coordinate()
Coordinate776.point = (0.0058,1.3625,-0.0833,0.0059,1.3866,-0.0800)

LineSet775.coord = Coordinate776
#from vt7 to vt6 vertices 2
ColorRGBA777 = x3d.ColorRGBA()
ColorRGBA777.USE = "HAnimSegmentLineColorRGBA"

LineSet775.color = ColorRGBA777

Shape774.geometry = LineSet775

HAnimSegment770.children.append(Shape774)
HAnimSite778 = x3d.HAnimSite()
HAnimSite778.name = "l_chest_midsagittal_plane_pt"
HAnimSite778.DEF = "hanim_l_chest_midsagittal_plane_pt"
TouchSensor779 = x3d.TouchSensor()
TouchSensor779.description = "HAnimSite l_chest_midsagittal_plane_pt"

HAnimSite778.children.append(TouchSensor779)
Shape780 = x3d.Shape()
Shape780.USE = "HAnimSiteShape"

HAnimSite778.children.append(Shape780)

HAnimSegment770.children.append(HAnimSite778)
HAnimSite781 = x3d.HAnimSite()
HAnimSite781.name = "mesosternale_pt"
HAnimSite781.DEF = "hanim_mesosternale_pt"
TouchSensor782 = x3d.TouchSensor()
TouchSensor782.description = "HAnimSite mesosternale_pt"

HAnimSite781.children.append(TouchSensor782)
Shape783 = x3d.Shape()
Shape783.USE = "HAnimSiteShape"

HAnimSite781.children.append(Shape783)

HAnimSegment770.children.append(HAnimSite781)
HAnimSite784 = x3d.HAnimSite()
HAnimSite784.name = "r_chest_midsagittal_plane_pt"
HAnimSite784.DEF = "hanim_r_chest_midsagittal_plane_pt"
TouchSensor785 = x3d.TouchSensor()
TouchSensor785.description = "HAnimSite r_chest_midsagittal_plane_pt"

HAnimSite784.children.append(TouchSensor785)
Shape786 = x3d.Shape()
Shape786.USE = "HAnimSiteShape"

HAnimSite784.children.append(Shape786)

HAnimSegment770.children.append(HAnimSite784)
HAnimSite787 = x3d.HAnimSite()
HAnimSite787.name = "rear_center_midsagittal_plane_pt"
HAnimSite787.DEF = "hanim_rear_center_midsagittal_plane_pt"
TouchSensor788 = x3d.TouchSensor()
TouchSensor788.description = "HAnimSite rear_center_midsagittal_plane_pt"

HAnimSite787.children.append(TouchSensor788)
Shape789 = x3d.Shape()
Shape789.USE = "HAnimSiteShape"

HAnimSite787.children.append(Shape789)

HAnimSegment770.children.append(HAnimSite787)

HAnimJoint769.children.append(HAnimSegment770)
HAnimJoint790 = x3d.HAnimJoint()
HAnimJoint790.name = "vt6"
HAnimJoint790.DEF = "hanim_vt6"
HAnimJoint790.center = [0.0059,1.3866,-0.08]
HAnimJoint790.ulimit = [0,0,0]
HAnimJoint790.llimit = [0,0,0]
HAnimSegment791 = x3d.HAnimSegment()
HAnimSegment791.name = "t6"
HAnimSegment791.DEF = "hanim_t6"
Transform792 = x3d.Transform()
Transform792.translation = [0.0059,1.3866,-0.08]
Transform793 = x3d.Transform()
#Empty Transform
Shape794 = x3d.Shape()
Shape794.USE = "HAnimJointShape"

Transform793.children.append(Shape794)

Transform792.children.append(Transform793)

HAnimSegment791.children.append(Transform792)
Shape795 = x3d.Shape()
LineSet796 = x3d.LineSet()
LineSet796.vertexCount = [2]
Coordinate797 = x3d.Coordinate()
Coordinate797.point = (0.0059,1.3866,-0.0800,0.0060,1.4102,-0.0745)

LineSet796.coord = Coordinate797
#from vt6 to vt5 vertices 2
ColorRGBA798 = x3d.ColorRGBA()
ColorRGBA798.USE = "HAnimSegmentLineColorRGBA"

LineSet796.color = ColorRGBA798

Shape795.geometry = LineSet796

HAnimSegment791.children.append(Shape795)
HAnimSite799 = x3d.HAnimSite()
HAnimSite799.name = "spine_1_middle_back_pt"
HAnimSite799.DEF = "hanim_spine_1_middle_back_pt"
TouchSensor800 = x3d.TouchSensor()
TouchSensor800.description = "HAnimSite spine_1_middle_back_pt"

HAnimSite799.children.append(TouchSensor800)
Shape801 = x3d.Shape()
Shape801.USE = "HAnimSiteShape"

HAnimSite799.children.append(Shape801)

HAnimSegment791.children.append(HAnimSite799)

HAnimJoint790.children.append(HAnimSegment791)
HAnimJoint802 = x3d.HAnimJoint()
HAnimJoint802.name = "vt5"
HAnimJoint802.DEF = "hanim_vt5"
HAnimJoint802.center = [0.006,1.4102,-0.0745]
HAnimJoint802.ulimit = [0,0,0]
HAnimJoint802.llimit = [0,0,0]
HAnimSegment803 = x3d.HAnimSegment()
HAnimSegment803.name = "t5"
HAnimSegment803.DEF = "hanim_t5"
Transform804 = x3d.Transform()
Transform804.translation = [0.006,1.4102,-0.0745]
Transform805 = x3d.Transform()
#Empty Transform
Shape806 = x3d.Shape()
Shape806.USE = "HAnimJointShape"

Transform805.children.append(Shape806)

Transform804.children.append(Transform805)

HAnimSegment803.children.append(Transform804)
Shape807 = x3d.Shape()
LineSet808 = x3d.LineSet()
LineSet808.vertexCount = [2]
Coordinate809 = x3d.Coordinate()
Coordinate809.point = (0.0060,1.4102,-0.0745,0.0061,1.4320,-0.0675)

LineSet808.coord = Coordinate809
#from vt5 to vt4 vertices 2
ColorRGBA810 = x3d.ColorRGBA()
ColorRGBA810.USE = "HAnimSegmentLineColorRGBA"

LineSet808.color = ColorRGBA810

Shape807.geometry = LineSet808

HAnimSegment803.children.append(Shape807)

HAnimJoint802.children.append(HAnimSegment803)
HAnimJoint811 = x3d.HAnimJoint()
HAnimJoint811.name = "vt4"
HAnimJoint811.DEF = "hanim_vt4"
HAnimJoint811.center = [0.0061,1.432,-0.0675]
HAnimJoint811.ulimit = [0,0,0]
HAnimJoint811.llimit = [0,0,0]
HAnimSegment812 = x3d.HAnimSegment()
HAnimSegment812.name = "t4"
HAnimSegment812.DEF = "hanim_t4"
Transform813 = x3d.Transform()
Transform813.translation = [0.0061,1.432,-0.0675]
Transform814 = x3d.Transform()
#Empty Transform
Shape815 = x3d.Shape()
Shape815.USE = "HAnimJointShape"

Transform814.children.append(Shape815)

Transform813.children.append(Transform814)

HAnimSegment812.children.append(Transform813)
Shape816 = x3d.Shape()
LineSet817 = x3d.LineSet()
LineSet817.vertexCount = [2]
Coordinate818 = x3d.Coordinate()
Coordinate818.point = (0.0061,1.4320,-0.0675,0.0062,1.4583,-0.0570)

LineSet817.coord = Coordinate818
#from vt4 to vt3 vertices 2
ColorRGBA819 = x3d.ColorRGBA()
ColorRGBA819.USE = "HAnimSegmentLineColorRGBA"

LineSet817.color = ColorRGBA819

Shape816.geometry = LineSet817

HAnimSegment812.children.append(Shape816)

HAnimJoint811.children.append(HAnimSegment812)
HAnimJoint820 = x3d.HAnimJoint()
HAnimJoint820.name = "vt3"
HAnimJoint820.DEF = "hanim_vt3"
HAnimJoint820.center = [0.0062,1.4583,-0.057]
HAnimJoint820.ulimit = [0,0,0]
HAnimJoint820.llimit = [0,0,0]
HAnimSegment821 = x3d.HAnimSegment()
HAnimSegment821.name = "t3"
HAnimSegment821.DEF = "hanim_t3"
Transform822 = x3d.Transform()
Transform822.translation = [0.0062,1.4583,-0.057]
Transform823 = x3d.Transform()
#Empty Transform
Shape824 = x3d.Shape()
Shape824.USE = "HAnimJointShape"

Transform823.children.append(Shape824)

Transform822.children.append(Transform823)

HAnimSegment821.children.append(Transform822)
Shape825 = x3d.Shape()
LineSet826 = x3d.LineSet()
LineSet826.vertexCount = [2]
Coordinate827 = x3d.Coordinate()
Coordinate827.point = (0.0062,1.4583,-0.0570,0.0063,1.4761,-0.0484)

LineSet826.coord = Coordinate827
#from vt3 to vt2 vertices 2
ColorRGBA828 = x3d.ColorRGBA()
ColorRGBA828.USE = "HAnimSegmentLineColorRGBA"

LineSet826.color = ColorRGBA828

Shape825.geometry = LineSet826

HAnimSegment821.children.append(Shape825)

HAnimJoint820.children.append(HAnimSegment821)
HAnimJoint829 = x3d.HAnimJoint()
HAnimJoint829.name = "vt2"
HAnimJoint829.DEF = "hanim_vt2"
HAnimJoint829.center = [0.0063,1.4761,-0.0484]
HAnimJoint829.ulimit = [0,0,0]
HAnimJoint829.llimit = [0,0,0]
HAnimSegment830 = x3d.HAnimSegment()
HAnimSegment830.name = "t2"
HAnimSegment830.DEF = "hanim_t2"
Transform831 = x3d.Transform()
Transform831.translation = [0.0063,1.4761,-0.0484]
Transform832 = x3d.Transform()
#Empty Transform
Shape833 = x3d.Shape()
Shape833.USE = "HAnimJointShape"

Transform832.children.append(Shape833)

Transform831.children.append(Transform832)

HAnimSegment830.children.append(Transform831)
Shape834 = x3d.Shape()
LineSet835 = x3d.LineSet()
LineSet835.vertexCount = [2]
Coordinate836 = x3d.Coordinate()
Coordinate836.point = (0.0063,1.4761,-0.0484,0.0065,1.4951,-0.0387)

LineSet835.coord = Coordinate836
#from vt2 to vt1 vertices 2
ColorRGBA837 = x3d.ColorRGBA()
ColorRGBA837.USE = "HAnimSegmentLineColorRGBA"

LineSet835.color = ColorRGBA837

Shape834.geometry = LineSet835

HAnimSegment830.children.append(Shape834)
HAnimSite838 = x3d.HAnimSite()
HAnimSite838.name = "cervicale_pt"
HAnimSite838.DEF = "hanim_cervicale_pt"
HAnimSite838.translation = [0.0064,1.52,-0.0815]
TouchSensor839 = x3d.TouchSensor()
TouchSensor839.description = "HAnimSite cervicale_pt"

HAnimSite838.children.append(TouchSensor839)
Shape840 = x3d.Shape()
Shape840.USE = "HAnimSiteShape"

HAnimSite838.children.append(Shape840)

HAnimSegment830.children.append(HAnimSite838)
HAnimSite841 = x3d.HAnimSite()
HAnimSite841.name = "suprasternale_pt"
HAnimSite841.DEF = "hanim_suprasternale_pt"
HAnimSite841.translation = [0.0084,1.4714,0.0551]
TouchSensor842 = x3d.TouchSensor()
TouchSensor842.description = "HAnimSite suprasternale_pt"

HAnimSite841.children.append(TouchSensor842)
Shape843 = x3d.Shape()
Shape843.USE = "HAnimSiteShape"

HAnimSite841.children.append(Shape843)

HAnimSegment830.children.append(HAnimSite841)

HAnimJoint829.children.append(HAnimSegment830)
HAnimJoint844 = x3d.HAnimJoint()
HAnimJoint844.name = "vt1"
HAnimJoint844.DEF = "hanim_vt1"
HAnimJoint844.center = [0.0065,1.4951,-0.0387]
HAnimJoint844.ulimit = [0,0,0]
HAnimJoint844.llimit = [0,0,0]
HAnimSegment845 = x3d.HAnimSegment()
HAnimSegment845.name = "t1"
HAnimSegment845.DEF = "hanim_t1"
Transform846 = x3d.Transform()
Transform846.translation = [0.0065,1.4951,-0.0387]
Transform847 = x3d.Transform()
#Empty Transform
Shape848 = x3d.Shape()
Shape848.USE = "HAnimJointShape"

Transform847.children.append(Shape848)

Transform846.children.append(Transform847)

HAnimSegment845.children.append(Transform846)
Shape849 = x3d.Shape()
LineSet850 = x3d.LineSet()
LineSet850.vertexCount = [2]
Coordinate851 = x3d.Coordinate()
Coordinate851.point = (0.0065,1.4951,-0.0387,0.0066,1.5132,-0.0301)

LineSet850.coord = Coordinate851
#from vt1 to vc7 vertices 2
ColorRGBA852 = x3d.ColorRGBA()
ColorRGBA852.USE = "HAnimSegmentLineColorRGBA"

LineSet850.color = ColorRGBA852

Shape849.geometry = LineSet850

HAnimSegment845.children.append(Shape849)
HAnimSite853 = x3d.HAnimSite()
HAnimSite853.name = "l_neck_base_pt"
HAnimSite853.DEF = "hanim_l_neck_base_pt"
HAnimSite853.translation = [0.0646,1.5141,-0.038]
TouchSensor854 = x3d.TouchSensor()
TouchSensor854.description = "HAnimSite l_neck_base_pt"

HAnimSite853.children.append(TouchSensor854)
Shape855 = x3d.Shape()
Shape855.USE = "HAnimSiteShape"

HAnimSite853.children.append(Shape855)

HAnimSegment845.children.append(HAnimSite853)
HAnimSite856 = x3d.HAnimSite()
HAnimSite856.name = "r_neck_base_pt"
HAnimSite856.DEF = "hanim_r_neck_base_pt"
HAnimSite856.translation = [-0.0419,1.5149,-0.022]
TouchSensor857 = x3d.TouchSensor()
TouchSensor857.description = "HAnimSite r_neck_base_pt"

HAnimSite856.children.append(TouchSensor857)
Shape858 = x3d.Shape()
Shape858.USE = "HAnimSiteShape"

HAnimSite856.children.append(Shape858)

HAnimSegment845.children.append(HAnimSite856)
Shape859 = x3d.Shape()
LineSet860 = x3d.LineSet()
LineSet860.vertexCount = [2]
Coordinate861 = x3d.Coordinate()
Coordinate861.point = (0.0065,1.4951,-0.0387,0.0820,1.4488,-0.0353)

LineSet860.coord = Coordinate861
#from vt1 to l_sternoclavicular vertices 2
ColorRGBA862 = x3d.ColorRGBA()
ColorRGBA862.USE = "HAnimSegmentLineColorRGBA"

LineSet860.color = ColorRGBA862

Shape859.geometry = LineSet860

HAnimSegment845.children.append(Shape859)
HAnimSite863 = x3d.HAnimSite()
HAnimSite863.name = "l_acromion_pt"
HAnimSite863.DEF = "hanim_l_acromion_pt"
HAnimSite863.translation = [0.2032,1.476,-0.049]
TouchSensor864 = x3d.TouchSensor()
TouchSensor864.description = "HAnimSite l_acromion_pt"

HAnimSite863.children.append(TouchSensor864)
Shape865 = x3d.Shape()
Shape865.USE = "HAnimSiteShape"

HAnimSite863.children.append(Shape865)

HAnimSegment845.children.append(HAnimSite863)
HAnimSite866 = x3d.HAnimSite()
HAnimSite866.name = "l_axilla_distal_pt"
HAnimSite866.DEF = "hanim_l_axilla_distal_pt"
HAnimSite866.translation = [0.1706,1.4072,-0.0875]
TouchSensor867 = x3d.TouchSensor()
TouchSensor867.description = "HAnimSite l_axilla_distal_pt"

HAnimSite866.children.append(TouchSensor867)
Shape868 = x3d.Shape()
Shape868.USE = "HAnimSiteShape"

HAnimSite866.children.append(Shape868)

HAnimSegment845.children.append(HAnimSite866)
HAnimSite869 = x3d.HAnimSite()
HAnimSite869.name = "l_axilla_posterior_folds_pt"
HAnimSite869.DEF = "hanim_l_axilla_posterior_folds_pt"
TouchSensor870 = x3d.TouchSensor()
TouchSensor870.description = "HAnimSite l_axilla_posterior_folds_pt"

HAnimSite869.children.append(TouchSensor870)
Shape871 = x3d.Shape()
Shape871.USE = "HAnimSiteShape"

HAnimSite869.children.append(Shape871)

HAnimSegment845.children.append(HAnimSite869)
HAnimSite872 = x3d.HAnimSite()
HAnimSite872.name = "l_axilla_proximal_pt"
HAnimSite872.DEF = "hanim_l_axilla_proximal_pt"
HAnimSite872.translation = [0.1777,1.4065,-0.0075]
TouchSensor873 = x3d.TouchSensor()
TouchSensor873.description = "HAnimSite l_axilla_proximal_pt"

HAnimSite872.children.append(TouchSensor873)
Shape874 = x3d.Shape()
Shape874.USE = "HAnimSiteShape"

HAnimSite872.children.append(Shape874)

HAnimSegment845.children.append(HAnimSite872)
HAnimSite875 = x3d.HAnimSite()
HAnimSite875.name = "l_clavicale_pt"
HAnimSite875.DEF = "hanim_l_clavicale_pt"
HAnimSite875.translation = [0.0271,1.4943,0.0394]
TouchSensor876 = x3d.TouchSensor()
TouchSensor876.description = "HAnimSite l_clavicale_pt"

HAnimSite875.children.append(TouchSensor876)
Shape877 = x3d.Shape()
Shape877.USE = "HAnimSiteShape"

HAnimSite875.children.append(Shape877)

HAnimSegment845.children.append(HAnimSite875)
Shape878 = x3d.Shape()
LineSet879 = x3d.LineSet()
LineSet879.vertexCount = [2]
Coordinate880 = x3d.Coordinate()
Coordinate880.point = (0.0065,1.4951,-0.0387,-0.0694,1.4600,-0.0330)

LineSet879.coord = Coordinate880
#from vt1 to r_sternoclavicular vertices 2
ColorRGBA881 = x3d.ColorRGBA()
ColorRGBA881.USE = "HAnimSegmentLineColorRGBA"

LineSet879.color = ColorRGBA881

Shape878.geometry = LineSet879

HAnimSegment845.children.append(Shape878)
HAnimSite882 = x3d.HAnimSite()
HAnimSite882.name = "r_acromion_pt"
HAnimSite882.DEF = "hanim_r_acromion_pt"
HAnimSite882.translation = [-0.1905,1.4791,-0.0431]
TouchSensor883 = x3d.TouchSensor()
TouchSensor883.description = "HAnimSite r_acromion_pt"

HAnimSite882.children.append(TouchSensor883)
Shape884 = x3d.Shape()
Shape884.USE = "HAnimSiteShape"

HAnimSite882.children.append(Shape884)

HAnimSegment845.children.append(HAnimSite882)
HAnimSite885 = x3d.HAnimSite()
HAnimSite885.name = "r_axilla_distal_pt"
HAnimSite885.DEF = "hanim_r_axilla_distal_pt"
HAnimSite885.translation = [-0.1603,1.4098,-0.0826]
TouchSensor886 = x3d.TouchSensor()
TouchSensor886.description = "HAnimSite r_axilla_distal_pt"

HAnimSite885.children.append(TouchSensor886)
Shape887 = x3d.Shape()
Shape887.USE = "HAnimSiteShape"

HAnimSite885.children.append(Shape887)

HAnimSegment845.children.append(HAnimSite885)
HAnimSite888 = x3d.HAnimSite()
HAnimSite888.name = "r_axilla_posterior_folds_pt"
HAnimSite888.DEF = "hanim_r_axilla_posterior_folds_pt"
TouchSensor889 = x3d.TouchSensor()
TouchSensor889.description = "HAnimSite r_axilla_posterior_folds_pt"

HAnimSite888.children.append(TouchSensor889)
Shape890 = x3d.Shape()
Shape890.USE = "HAnimSiteShape"

HAnimSite888.children.append(Shape890)

HAnimSegment845.children.append(HAnimSite888)
HAnimSite891 = x3d.HAnimSite()
HAnimSite891.name = "r_axilla_proximal_pt"
HAnimSite891.DEF = "hanim_r_axilla_proximal_pt"
HAnimSite891.translation = [-0.1626,1.4072,-0.0031]
TouchSensor892 = x3d.TouchSensor()
TouchSensor892.description = "HAnimSite r_axilla_proximal_pt"

HAnimSite891.children.append(TouchSensor892)
Shape893 = x3d.Shape()
Shape893.USE = "HAnimSiteShape"

HAnimSite891.children.append(Shape893)

HAnimSegment845.children.append(HAnimSite891)
HAnimSite894 = x3d.HAnimSite()
HAnimSite894.name = "r_clavicale_pt"
HAnimSite894.DEF = "hanim_r_clavicale_pt"
HAnimSite894.translation = [-0.0115,1.4943,0.04]
TouchSensor895 = x3d.TouchSensor()
TouchSensor895.description = "HAnimSite r_clavicale_pt"

HAnimSite894.children.append(TouchSensor895)
Shape896 = x3d.Shape()
Shape896.USE = "HAnimSiteShape"

HAnimSite894.children.append(Shape896)

HAnimSegment845.children.append(HAnimSite894)

HAnimJoint844.children.append(HAnimSegment845)
HAnimJoint897 = x3d.HAnimJoint()
HAnimJoint897.name = "vc7"
HAnimJoint897.DEF = "hanim_vc7"
HAnimJoint897.center = [0.0066,1.5132,-0.0301]
HAnimJoint897.ulimit = [0,0,0]
HAnimJoint897.llimit = [0,0,0]
HAnimSegment898 = x3d.HAnimSegment()
HAnimSegment898.name = "c7"
HAnimSegment898.DEF = "hanim_c7"
Transform899 = x3d.Transform()
Transform899.translation = [0.0066,1.5132,-0.0301]
Transform900 = x3d.Transform()
#Empty Transform
Shape901 = x3d.Shape()
Shape901.USE = "HAnimJointShape"

Transform900.children.append(Shape901)

Transform899.children.append(Transform900)

HAnimSegment898.children.append(Transform899)
Shape902 = x3d.Shape()
LineSet903 = x3d.LineSet()
LineSet903.vertexCount = [2]
Coordinate904 = x3d.Coordinate()
Coordinate904.point = (0.0066,1.5132,-0.0301,0.0066,1.5357,-0.0143)

LineSet903.coord = Coordinate904
#from vc7 to vc6 vertices 2
ColorRGBA905 = x3d.ColorRGBA()
ColorRGBA905.USE = "HAnimSegmentLineColorRGBA"

LineSet903.color = ColorRGBA905

Shape902.geometry = LineSet903

HAnimSegment898.children.append(Shape902)

HAnimJoint897.children.append(HAnimSegment898)
HAnimJoint906 = x3d.HAnimJoint()
HAnimJoint906.name = "vc6"
HAnimJoint906.DEF = "hanim_vc6"
HAnimJoint906.center = [0.0066,1.5357,-0.0143]
HAnimJoint906.ulimit = [0,0,0]
HAnimJoint906.llimit = [0,0,0]
HAnimSegment907 = x3d.HAnimSegment()
HAnimSegment907.name = "c6"
HAnimSegment907.DEF = "hanim_c6"
Transform908 = x3d.Transform()
Transform908.translation = [0.0066,1.5357,-0.0143]
Transform909 = x3d.Transform()
#Empty Transform
Shape910 = x3d.Shape()
Shape910.USE = "HAnimJointShape"

Transform909.children.append(Shape910)

Transform908.children.append(Transform909)

HAnimSegment907.children.append(Transform908)
Shape911 = x3d.Shape()
LineSet912 = x3d.LineSet()
LineSet912.vertexCount = [2]
Coordinate913 = x3d.Coordinate()
Coordinate913.point = (0.0066,1.5357,-0.0143,0.0066,1.5520,-0.0082)

LineSet912.coord = Coordinate913
#from vc6 to vc5 vertices 2
ColorRGBA914 = x3d.ColorRGBA()
ColorRGBA914.USE = "HAnimSegmentLineColorRGBA"

LineSet912.color = ColorRGBA914

Shape911.geometry = LineSet912

HAnimSegment907.children.append(Shape911)

HAnimJoint906.children.append(HAnimSegment907)
HAnimJoint915 = x3d.HAnimJoint()
HAnimJoint915.name = "vc5"
HAnimJoint915.DEF = "hanim_vc5"
HAnimJoint915.center = [0.0066,1.552,-0.0082]
HAnimJoint915.ulimit = [0,0,0]
HAnimJoint915.llimit = [0,0,0]
HAnimSegment916 = x3d.HAnimSegment()
HAnimSegment916.name = "c5"
HAnimSegment916.DEF = "hanim_c5"
Transform917 = x3d.Transform()
Transform917.translation = [0.0066,1.552,-0.0082]
Transform918 = x3d.Transform()
#Empty Transform
Shape919 = x3d.Shape()
Shape919.USE = "HAnimJointShape"

Transform918.children.append(Shape919)

Transform917.children.append(Transform918)

HAnimSegment916.children.append(Transform917)
Shape920 = x3d.Shape()
LineSet921 = x3d.LineSet()
LineSet921.vertexCount = [2]
Coordinate922 = x3d.Coordinate()
Coordinate922.point = (0.0066,1.5520,-0.0082,0.0066,1.5662,-0.0084)

LineSet921.coord = Coordinate922
#from vc5 to vc4 vertices 2
ColorRGBA923 = x3d.ColorRGBA()
ColorRGBA923.USE = "HAnimSegmentLineColorRGBA"

LineSet921.color = ColorRGBA923

Shape920.geometry = LineSet921

HAnimSegment916.children.append(Shape920)

HAnimJoint915.children.append(HAnimSegment916)
HAnimJoint924 = x3d.HAnimJoint()
HAnimJoint924.name = "vc4"
HAnimJoint924.DEF = "hanim_vc4"
HAnimJoint924.center = [0.0066,1.5662,-0.0084]
HAnimJoint924.ulimit = [0,0,0]
HAnimJoint924.llimit = [0,0,0]
HAnimSegment925 = x3d.HAnimSegment()
HAnimSegment925.name = "c4"
HAnimSegment925.DEF = "hanim_c4"
Transform926 = x3d.Transform()
Transform926.translation = [0.0066,1.5662,-0.0084]
Transform927 = x3d.Transform()
#Empty Transform
Shape928 = x3d.Shape()
Shape928.USE = "HAnimJointShape"

Transform927.children.append(Shape928)

Transform926.children.append(Transform927)

HAnimSegment925.children.append(Transform926)
Shape929 = x3d.Shape()
LineSet930 = x3d.LineSet()
LineSet930.vertexCount = [2]
Coordinate931 = x3d.Coordinate()
Coordinate931.point = (0.0066,1.5662,-0.0084,0.0066,1.5800,-0.0103)

LineSet930.coord = Coordinate931
#from vc4 to vc3 vertices 2
ColorRGBA932 = x3d.ColorRGBA()
ColorRGBA932.USE = "HAnimSegmentLineColorRGBA"

LineSet930.color = ColorRGBA932

Shape929.geometry = LineSet930

HAnimSegment925.children.append(Shape929)

HAnimJoint924.children.append(HAnimSegment925)
HAnimJoint933 = x3d.HAnimJoint()
HAnimJoint933.name = "vc3"
HAnimJoint933.DEF = "hanim_vc3"
HAnimJoint933.center = [0.0066,1.58,-0.0103]
HAnimJoint933.ulimit = [0,0,0]
HAnimJoint933.llimit = [0,0,0]
HAnimSegment934 = x3d.HAnimSegment()
HAnimSegment934.name = "c3"
HAnimSegment934.DEF = "hanim_c3"
Transform935 = x3d.Transform()
Transform935.translation = [0.0066,1.58,-0.0103]
Transform936 = x3d.Transform()
#Empty Transform
Shape937 = x3d.Shape()
Shape937.USE = "HAnimJointShape"

Transform936.children.append(Shape937)

Transform935.children.append(Transform936)

HAnimSegment934.children.append(Transform935)
Shape938 = x3d.Shape()
LineSet939 = x3d.LineSet()
LineSet939.vertexCount = [2]
Coordinate940 = x3d.Coordinate()
Coordinate940.point = (0.0066,1.5800,-0.0103,0.0066,1.5928,-0.0103)

LineSet939.coord = Coordinate940
#from vc3 to vc2 vertices 2
ColorRGBA941 = x3d.ColorRGBA()
ColorRGBA941.USE = "HAnimSegmentLineColorRGBA"

LineSet939.color = ColorRGBA941

Shape938.geometry = LineSet939

HAnimSegment934.children.append(Shape938)
HAnimSite942 = x3d.HAnimSite()
HAnimSite942.name = "adams_apple_pt"
HAnimSite942.DEF = "hanim_adams_apple_pt"
TouchSensor943 = x3d.TouchSensor()
TouchSensor943.description = "HAnimSite adams_apple_pt"

HAnimSite942.children.append(TouchSensor943)
Shape944 = x3d.Shape()
Shape944.USE = "HAnimSiteShape"

HAnimSite942.children.append(Shape944)

HAnimSegment934.children.append(HAnimSite942)

HAnimJoint933.children.append(HAnimSegment934)
HAnimJoint945 = x3d.HAnimJoint()
HAnimJoint945.name = "vc2"
HAnimJoint945.DEF = "hanim_vc2"
HAnimJoint945.center = [0.0066,1.5928,-0.0103]
HAnimJoint945.ulimit = [0,0,0]
HAnimJoint945.llimit = [0,0,0]
HAnimSegment946 = x3d.HAnimSegment()
HAnimSegment946.name = "c2"
HAnimSegment946.DEF = "hanim_c2"
Transform947 = x3d.Transform()
Transform947.translation = [0.0066,1.5928,-0.0103]
Transform948 = x3d.Transform()
#Empty Transform
Shape949 = x3d.Shape()
Shape949.USE = "HAnimJointShape"

Transform948.children.append(Shape949)

Transform947.children.append(Transform948)

HAnimSegment946.children.append(Transform947)
Shape950 = x3d.Shape()
LineSet951 = x3d.LineSet()
LineSet951.vertexCount = [2]
Coordinate952 = x3d.Coordinate()
Coordinate952.point = (0.0066,1.5928,-0.0103,0.0066,1.6144,-0.0034)

LineSet951.coord = Coordinate952
#from vc2 to vc1 vertices 2
ColorRGBA953 = x3d.ColorRGBA()
ColorRGBA953.USE = "HAnimSegmentLineColorRGBA"

LineSet951.color = ColorRGBA953

Shape950.geometry = LineSet951

HAnimSegment946.children.append(Shape950)

HAnimJoint945.children.append(HAnimSegment946)
HAnimJoint954 = x3d.HAnimJoint()
HAnimJoint954.name = "vc1"
HAnimJoint954.DEF = "hanim_vc1"
HAnimJoint954.center = [0.0066,1.6144,-0.0034]
HAnimJoint954.ulimit = [0,0,0]
HAnimJoint954.llimit = [0,0,0]
HAnimSegment955 = x3d.HAnimSegment()
HAnimSegment955.name = "c1"
HAnimSegment955.DEF = "hanim_c1"
Transform956 = x3d.Transform()
Transform956.translation = [0.0066,1.6144,-0.0034]
Transform957 = x3d.Transform()
#Empty Transform
Shape958 = x3d.Shape()
Shape958.USE = "HAnimJointShape"

Transform957.children.append(Shape958)

Transform956.children.append(Transform957)

HAnimSegment955.children.append(Transform956)
Shape959 = x3d.Shape()
LineSet960 = x3d.LineSet()
LineSet960.vertexCount = [2]
Coordinate961 = x3d.Coordinate()
Coordinate961.point = (0.0066,1.6144,-0.0034,0.0044,1.6209,0.0236)

LineSet960.coord = Coordinate961
#from vc1 to skullbase vertices 2
ColorRGBA962 = x3d.ColorRGBA()
ColorRGBA962.USE = "HAnimSegmentLineColorRGBA"

LineSet960.color = ColorRGBA962

Shape959.geometry = LineSet960

HAnimSegment955.children.append(Shape959)
HAnimSite963 = x3d.HAnimSite()
HAnimSite963.name = "glabella_pt"
HAnimSite963.DEF = "hanim_glabella_pt"
TouchSensor964 = x3d.TouchSensor()
TouchSensor964.description = "HAnimSite glabella_pt"

HAnimSite963.children.append(TouchSensor964)
Shape965 = x3d.Shape()
Shape965.USE = "HAnimSiteShape"

HAnimSite963.children.append(Shape965)

HAnimSegment955.children.append(HAnimSite963)
HAnimSite966 = x3d.HAnimSite()
HAnimSite966.name = "l_ectocanthus_pt"
HAnimSite966.DEF = "hanim_l_ectocanthus_pt"
TouchSensor967 = x3d.TouchSensor()
TouchSensor967.description = "HAnimSite l_ectocanthus_pt"

HAnimSite966.children.append(TouchSensor967)
Shape968 = x3d.Shape()
Shape968.USE = "HAnimSiteShape"

HAnimSite966.children.append(Shape968)

HAnimSegment955.children.append(HAnimSite966)
HAnimSite969 = x3d.HAnimSite()
HAnimSite969.name = "l_infraorbitale_pt"
HAnimSite969.DEF = "hanim_l_infraorbitale_pt"
HAnimSite969.translation = [0.0341,1.6171,0.0752]
TouchSensor970 = x3d.TouchSensor()
TouchSensor970.description = "HAnimSite l_infraorbitale_pt"

HAnimSite969.children.append(TouchSensor970)
Shape971 = x3d.Shape()
Shape971.USE = "HAnimSiteShape"

HAnimSite969.children.append(Shape971)

HAnimSegment955.children.append(HAnimSite969)
HAnimSite972 = x3d.HAnimSite()
HAnimSite972.name = "l_tragion_pt"
HAnimSite972.DEF = "hanim_l_tragion_pt"
HAnimSite972.translation = [0.0739,1.6348,0.0282]
TouchSensor973 = x3d.TouchSensor()
TouchSensor973.description = "HAnimSite l_tragion_pt"

HAnimSite972.children.append(TouchSensor973)
Shape974 = x3d.Shape()
Shape974.USE = "HAnimSiteShape"

HAnimSite972.children.append(Shape974)

HAnimSegment955.children.append(HAnimSite972)
HAnimSite975 = x3d.HAnimSite()
HAnimSite975.name = "nuchale_pt"
HAnimSite975.DEF = "hanim_nuchale_pt"
HAnimSite975.translation = [0.0039,1.5972,-0.0796]
TouchSensor976 = x3d.TouchSensor()
TouchSensor976.description = "HAnimSite nuchale_pt"

HAnimSite975.children.append(TouchSensor976)
Shape977 = x3d.Shape()
Shape977.USE = "HAnimSiteShape"

HAnimSite975.children.append(Shape977)

HAnimSegment955.children.append(HAnimSite975)
HAnimSite978 = x3d.HAnimSite()
HAnimSite978.name = "opisthocranion_pt"
HAnimSite978.DEF = "hanim_opisthocranion_pt"
TouchSensor979 = x3d.TouchSensor()
TouchSensor979.description = "HAnimSite opisthocranion_pt"

HAnimSite978.children.append(TouchSensor979)
Shape980 = x3d.Shape()
Shape980.USE = "HAnimSiteShape"

HAnimSite978.children.append(Shape980)

HAnimSegment955.children.append(HAnimSite978)
HAnimSite981 = x3d.HAnimSite()
HAnimSite981.name = "r_ectocanthus_pt"
HAnimSite981.DEF = "hanim_r_ectocanthus_pt"
TouchSensor982 = x3d.TouchSensor()
TouchSensor982.description = "HAnimSite r_ectocanthus_pt"

HAnimSite981.children.append(TouchSensor982)
Shape983 = x3d.Shape()
Shape983.USE = "HAnimSiteShape"

HAnimSite981.children.append(Shape983)

HAnimSegment955.children.append(HAnimSite981)
HAnimSite984 = x3d.HAnimSite()
HAnimSite984.name = "r_infraorbitale_pt"
HAnimSite984.DEF = "hanim_r_infraorbitale_pt"
HAnimSite984.translation = [-0.0237,1.6171,0.0752]
TouchSensor985 = x3d.TouchSensor()
TouchSensor985.description = "HAnimSite r_infraorbitale_pt"

HAnimSite984.children.append(TouchSensor985)
Shape986 = x3d.Shape()
Shape986.USE = "HAnimSiteShape"

HAnimSite984.children.append(Shape986)

HAnimSegment955.children.append(HAnimSite984)
HAnimSite987 = x3d.HAnimSite()
HAnimSite987.name = "r_tragion_pt"
HAnimSite987.DEF = "hanim_r_tragion_pt"
HAnimSite987.translation = [-0.0646,1.6347,0.0302]
TouchSensor988 = x3d.TouchSensor()
TouchSensor988.description = "HAnimSite r_tragion_pt"

HAnimSite987.children.append(TouchSensor988)
Shape989 = x3d.Shape()
Shape989.USE = "HAnimSiteShape"

HAnimSite987.children.append(Shape989)

HAnimSegment955.children.append(HAnimSite987)
HAnimSite990 = x3d.HAnimSite()
HAnimSite990.name = "sellion_pt"
HAnimSite990.DEF = "hanim_sellion_pt"
HAnimSite990.translation = [0.0058,1.6316,0.0852]
TouchSensor991 = x3d.TouchSensor()
TouchSensor991.description = "HAnimSite sellion_pt"

HAnimSite990.children.append(TouchSensor991)
Shape992 = x3d.Shape()
Shape992.USE = "HAnimSiteShape"

HAnimSite990.children.append(Shape992)

HAnimSegment955.children.append(HAnimSite990)
HAnimSite993 = x3d.HAnimSite()
HAnimSite993.name = "skull_vertex_pt"
HAnimSite993.DEF = "hanim_skull_vertex_pt"
HAnimSite993.translation = [0.005,1.7504,0.0055]
TouchSensor994 = x3d.TouchSensor()
TouchSensor994.description = "HAnimSite skull_vertex_pt"

HAnimSite993.children.append(TouchSensor994)
Shape995 = x3d.Shape()
Shape995.USE = "HAnimSiteShape"

HAnimSite993.children.append(Shape995)

HAnimSegment955.children.append(HAnimSite993)

HAnimJoint954.children.append(HAnimSegment955)
HAnimJoint996 = x3d.HAnimJoint()
HAnimJoint996.name = "skullbase"
HAnimJoint996.DEF = "hanim_skullbase"
HAnimJoint996.center = [0.0044,1.6209,0.0236]
HAnimJoint996.ulimit = [0,0,0]
HAnimJoint996.llimit = [0,0,0]
HAnimSegment997 = x3d.HAnimSegment()
HAnimSegment997.name = "skull"
HAnimSegment997.DEF = "hanim_skull"
Transform998 = x3d.Transform()
Transform998.translation = [0.0044,1.6209,0.0236]
Transform999 = x3d.Transform()
#Empty Transform
Shape1000 = x3d.Shape()
Shape1000.USE = "HAnimJointShape"

Transform999.children.append(Shape1000)

Transform998.children.append(Transform999)

HAnimSegment997.children.append(Transform998)
Shape1001 = x3d.Shape()
LineSet1002 = x3d.LineSet()
LineSet1002.vertexCount = [2]
Coordinate1003 = x3d.Coordinate()
Coordinate1003.point = (0.0044,1.6209,0.0236,0.0044,1.6209,0.0236)

LineSet1002.coord = Coordinate1003
#from skullbase to l_eyelid_joint vertices 2
ColorRGBA1004 = x3d.ColorRGBA()
ColorRGBA1004.USE = "HAnimSegmentLineColorRGBA"

LineSet1002.color = ColorRGBA1004

Shape1001.geometry = LineSet1002

HAnimSegment997.children.append(Shape1001)
Shape1005 = x3d.Shape()
LineSet1006 = x3d.LineSet()
LineSet1006.vertexCount = [2]
Coordinate1007 = x3d.Coordinate()
Coordinate1007.point = (0.0044,1.6209,0.0236,0.0044,1.6209,0.0236)

LineSet1006.coord = Coordinate1007
#from skullbase to r_eyelid_joint vertices 2
ColorRGBA1008 = x3d.ColorRGBA()
ColorRGBA1008.USE = "HAnimSegmentLineColorRGBA"

LineSet1006.color = ColorRGBA1008

Shape1005.geometry = LineSet1006

HAnimSegment997.children.append(Shape1005)
Shape1009 = x3d.Shape()
LineSet1010 = x3d.LineSet()
LineSet1010.vertexCount = [2]
Coordinate1011 = x3d.Coordinate()
Coordinate1011.point = (0.0044,1.6209,0.0236,0.0044,1.6209,0.0236)

LineSet1010.coord = Coordinate1011
#from skullbase to l_eyeball_joint vertices 2
ColorRGBA1012 = x3d.ColorRGBA()
ColorRGBA1012.USE = "HAnimSegmentLineColorRGBA"

LineSet1010.color = ColorRGBA1012

Shape1009.geometry = LineSet1010

HAnimSegment997.children.append(Shape1009)
Shape1013 = x3d.Shape()
LineSet1014 = x3d.LineSet()
LineSet1014.vertexCount = [2]
Coordinate1015 = x3d.Coordinate()
Coordinate1015.point = (0.0044,1.6209,0.0236,0.0044,1.6209,0.0236)

LineSet1014.coord = Coordinate1015
#from skullbase to r_eyeball_joint vertices 2
ColorRGBA1016 = x3d.ColorRGBA()
ColorRGBA1016.USE = "HAnimSegmentLineColorRGBA"

LineSet1014.color = ColorRGBA1016

Shape1013.geometry = LineSet1014

HAnimSegment997.children.append(Shape1013)
Shape1017 = x3d.Shape()
LineSet1018 = x3d.LineSet()
LineSet1018.vertexCount = [2]
Coordinate1019 = x3d.Coordinate()
Coordinate1019.point = (0.0044,1.6209,0.0236,0.0044,1.6209,0.0236)

LineSet1018.coord = Coordinate1019
#from skullbase to l_eyebrow_joint vertices 2
ColorRGBA1020 = x3d.ColorRGBA()
ColorRGBA1020.USE = "HAnimSegmentLineColorRGBA"

LineSet1018.color = ColorRGBA1020

Shape1017.geometry = LineSet1018

HAnimSegment997.children.append(Shape1017)
Shape1021 = x3d.Shape()
LineSet1022 = x3d.LineSet()
LineSet1022.vertexCount = [2]
Coordinate1023 = x3d.Coordinate()
Coordinate1023.point = (0.0044,1.6209,0.0236,0.0044,1.6209,0.0236)

LineSet1022.coord = Coordinate1023
#from skullbase to r_eyebrow_joint vertices 2
ColorRGBA1024 = x3d.ColorRGBA()
ColorRGBA1024.USE = "HAnimSegmentLineColorRGBA"

LineSet1022.color = ColorRGBA1024

Shape1021.geometry = LineSet1022

HAnimSegment997.children.append(Shape1021)
Shape1025 = x3d.Shape()
LineSet1026 = x3d.LineSet()
LineSet1026.vertexCount = [2]
Coordinate1027 = x3d.Coordinate()
Coordinate1027.point = (0.0044,1.6209,0.0236,0.0044,1.6209,0.0236)

LineSet1026.coord = Coordinate1027
#from skullbase to temporomandibular vertices 2
ColorRGBA1028 = x3d.ColorRGBA()
ColorRGBA1028.USE = "HAnimSegmentLineColorRGBA"

LineSet1026.color = ColorRGBA1028

Shape1025.geometry = LineSet1026

HAnimSegment997.children.append(Shape1025)
HAnimSite1029 = x3d.HAnimSite()
HAnimSite1029.name = "l_gonion_pt"
HAnimSite1029.DEF = "hanim_l_gonion_pt"
HAnimSite1029.translation = [0.0631,1.553,0.033]
TouchSensor1030 = x3d.TouchSensor()
TouchSensor1030.description = "HAnimSite l_gonion_pt"

HAnimSite1029.children.append(TouchSensor1030)
Shape1031 = x3d.Shape()
Shape1031.USE = "HAnimSiteShape"

HAnimSite1029.children.append(Shape1031)

HAnimSegment997.children.append(HAnimSite1029)
HAnimSite1032 = x3d.HAnimSite()
HAnimSite1032.name = "menton_pt"
HAnimSite1032.DEF = "hanim_menton_pt"
TouchSensor1033 = x3d.TouchSensor()
TouchSensor1033.description = "HAnimSite menton_pt"

HAnimSite1032.children.append(TouchSensor1033)
Shape1034 = x3d.Shape()
Shape1034.USE = "HAnimSiteShape"

HAnimSite1032.children.append(Shape1034)

HAnimSegment997.children.append(HAnimSite1032)
HAnimSite1035 = x3d.HAnimSite()
HAnimSite1035.name = "r_gonion_pt"
HAnimSite1035.DEF = "hanim_r_gonion_pt"
HAnimSite1035.translation = [-0.052,1.5529,0.0347]
TouchSensor1036 = x3d.TouchSensor()
TouchSensor1036.description = "HAnimSite r_gonion_pt"

HAnimSite1035.children.append(TouchSensor1036)
Shape1037 = x3d.Shape()
Shape1037.USE = "HAnimSiteShape"

HAnimSite1035.children.append(Shape1037)

HAnimSegment997.children.append(HAnimSite1035)
HAnimSite1038 = x3d.HAnimSite()
HAnimSite1038.name = "supramenton_pt"
HAnimSite1038.DEF = "hanim_supramenton_pt"
HAnimSite1038.translation = [0.0061,1.541,0.0805]
TouchSensor1039 = x3d.TouchSensor()
TouchSensor1039.description = "HAnimSite supramenton_pt"

HAnimSite1038.children.append(TouchSensor1039)
Shape1040 = x3d.Shape()
Shape1040.USE = "HAnimSiteShape"

HAnimSite1038.children.append(Shape1040)

HAnimSegment997.children.append(HAnimSite1038)

HAnimJoint996.children.append(HAnimSegment997)
HAnimJoint1041 = x3d.HAnimJoint()
HAnimJoint1041.name = "l_eyelid_joint"
HAnimJoint1041.DEF = "hanim_l_eyelid_joint"
HAnimJoint1041.ulimit = [0,0,0]
HAnimJoint1041.llimit = [0,0,0]

HAnimJoint996.children.append(HAnimJoint1041)
HAnimJoint1042 = x3d.HAnimJoint()
HAnimJoint1042.name = "r_eyelid_joint"
HAnimJoint1042.DEF = "hanim_r_eyelid_joint"
HAnimJoint1042.ulimit = [0,0,0]
HAnimJoint1042.llimit = [0,0,0]

HAnimJoint996.children.append(HAnimJoint1042)
HAnimJoint1043 = x3d.HAnimJoint()
HAnimJoint1043.name = "l_eyeball_joint"
HAnimJoint1043.DEF = "hanim_l_eyeball_joint"
HAnimJoint1043.ulimit = [0,0,0]
HAnimJoint1043.llimit = [0,0,0]

HAnimJoint996.children.append(HAnimJoint1043)
HAnimJoint1044 = x3d.HAnimJoint()
HAnimJoint1044.name = "r_eyeball_joint"
HAnimJoint1044.DEF = "hanim_r_eyeball_joint"
HAnimJoint1044.ulimit = [0,0,0]
HAnimJoint1044.llimit = [0,0,0]

HAnimJoint996.children.append(HAnimJoint1044)
HAnimJoint1045 = x3d.HAnimJoint()
HAnimJoint1045.name = "l_eyebrow_joint"
HAnimJoint1045.DEF = "hanim_l_eyebrow_joint"
HAnimJoint1045.ulimit = [0,0,0]
HAnimJoint1045.llimit = [0,0,0]

HAnimJoint996.children.append(HAnimJoint1045)
HAnimJoint1046 = x3d.HAnimJoint()
HAnimJoint1046.name = "r_eyebrow_joint"
HAnimJoint1046.DEF = "hanim_r_eyebrow_joint"
HAnimJoint1046.ulimit = [0,0,0]
HAnimJoint1046.llimit = [0,0,0]

HAnimJoint996.children.append(HAnimJoint1046)
HAnimJoint1047 = x3d.HAnimJoint()
HAnimJoint1047.name = "temporomandibular"
HAnimJoint1047.DEF = "hanim_temporomandibular"
HAnimJoint1047.ulimit = [0,0,0]
HAnimJoint1047.llimit = [0,0,0]

HAnimJoint996.children.append(HAnimJoint1047)

HAnimJoint954.children.append(HAnimJoint996)

HAnimJoint945.children.append(HAnimJoint954)

HAnimJoint933.children.append(HAnimJoint945)

HAnimJoint924.children.append(HAnimJoint933)

HAnimJoint915.children.append(HAnimJoint924)

HAnimJoint906.children.append(HAnimJoint915)

HAnimJoint897.children.append(HAnimJoint906)

HAnimJoint844.children.append(HAnimJoint897)
HAnimJoint1048 = x3d.HAnimJoint()
HAnimJoint1048.name = "l_sternoclavicular"
HAnimJoint1048.DEF = "hanim_l_sternoclavicular"
HAnimJoint1048.center = [0.082,1.4488,-0.0353]
HAnimJoint1048.ulimit = [0,0,0]
HAnimJoint1048.llimit = [0,0,0]
HAnimSegment1049 = x3d.HAnimSegment()
HAnimSegment1049.name = "l_clavicle"
HAnimSegment1049.DEF = "hanim_l_clavicle"
Transform1050 = x3d.Transform()
Transform1050.translation = [0.082,1.4488,-0.0353]
Transform1051 = x3d.Transform()
#Empty Transform
Shape1052 = x3d.Shape()
Shape1052.USE = "HAnimJointShape"

Transform1051.children.append(Shape1052)

Transform1050.children.append(Transform1051)

HAnimSegment1049.children.append(Transform1050)
Shape1053 = x3d.Shape()
LineSet1054 = x3d.LineSet()
LineSet1054.vertexCount = [2]
Coordinate1055 = x3d.Coordinate()
Coordinate1055.point = (0.0820,1.4488,-0.0353,0.0962,1.4269,-0.0424)

LineSet1054.coord = Coordinate1055
#from l_sternoclavicular to l_acromioclavicular vertices 2
ColorRGBA1056 = x3d.ColorRGBA()
ColorRGBA1056.USE = "HAnimSegmentLineColorRGBA"

LineSet1054.color = ColorRGBA1056

Shape1053.geometry = LineSet1054

HAnimSegment1049.children.append(Shape1053)

HAnimJoint1048.children.append(HAnimSegment1049)
HAnimJoint1057 = x3d.HAnimJoint()
HAnimJoint1057.name = "l_acromioclavicular"
HAnimJoint1057.DEF = "hanim_l_acromioclavicular"
HAnimJoint1057.center = [0.0962,1.4269,-0.0424]
HAnimJoint1057.ulimit = [0,0,0]
HAnimJoint1057.llimit = [0,0,0]
HAnimSegment1058 = x3d.HAnimSegment()
HAnimSegment1058.name = "l_scapula"
HAnimSegment1058.DEF = "hanim_l_scapula"
Transform1059 = x3d.Transform()
Transform1059.translation = [0.0962,1.4269,-0.0424]
Transform1060 = x3d.Transform()
#Empty Transform
Shape1061 = x3d.Shape()
Shape1061.USE = "HAnimJointShape"

Transform1060.children.append(Shape1061)

Transform1059.children.append(Transform1060)

HAnimSegment1058.children.append(Transform1059)
Shape1062 = x3d.Shape()
LineSet1063 = x3d.LineSet()
LineSet1063.vertexCount = [2]
Coordinate1064 = x3d.Coordinate()
Coordinate1064.point = (0.0962,1.4269,-0.0424,0.2029,1.4376,-0.0387)

LineSet1063.coord = Coordinate1064
#from l_acromioclavicular to l_shoulder vertices 2
ColorRGBA1065 = x3d.ColorRGBA()
ColorRGBA1065.USE = "HAnimSegmentLineColorRGBA"

LineSet1063.color = ColorRGBA1065

Shape1062.geometry = LineSet1063

HAnimSegment1058.children.append(Shape1062)
HAnimSite1066 = x3d.HAnimSite()
HAnimSite1066.name = "l_bideltoid_pt"
HAnimSite1066.DEF = "hanim_l_bideltoid_pt"
TouchSensor1067 = x3d.TouchSensor()
TouchSensor1067.description = "HAnimSite l_bideltoid_pt"

HAnimSite1066.children.append(TouchSensor1067)
Shape1068 = x3d.Shape()
Shape1068.USE = "HAnimSiteShape"

HAnimSite1066.children.append(Shape1068)

HAnimSegment1058.children.append(HAnimSite1066)
HAnimSite1069 = x3d.HAnimSite()
HAnimSite1069.name = "l_humeral_lateral_epicondyles_pt"
HAnimSite1069.DEF = "hanim_l_humeral_lateral_epicondyles_pt"
HAnimSite1069.translation = [0.228,1.1482,-0.11]
TouchSensor1070 = x3d.TouchSensor()
TouchSensor1070.description = "HAnimSite l_humeral_lateral_epicondyles_pt"

HAnimSite1069.children.append(TouchSensor1070)
Shape1071 = x3d.Shape()
Shape1071.USE = "HAnimSiteShape"

HAnimSite1069.children.append(Shape1071)

HAnimSegment1058.children.append(HAnimSite1069)

HAnimJoint1057.children.append(HAnimSegment1058)
HAnimJoint1072 = x3d.HAnimJoint()
HAnimJoint1072.name = "l_shoulder"
HAnimJoint1072.DEF = "hanim_l_shoulder"
HAnimJoint1072.center = [0.2029,1.4376,-0.0387]
HAnimJoint1072.ulimit = [0,0,0]
HAnimJoint1072.llimit = [0,0,0]
HAnimSegment1073 = x3d.HAnimSegment()
HAnimSegment1073.name = "l_upperarm"
HAnimSegment1073.DEF = "hanim_l_upperarm"
Transform1074 = x3d.Transform()
Transform1074.translation = [0.2029,1.4376,-0.0387]
Transform1075 = x3d.Transform()
#Empty Transform
Shape1076 = x3d.Shape()
Shape1076.USE = "HAnimJointShape"

Transform1075.children.append(Shape1076)

Transform1074.children.append(Transform1075)

HAnimSegment1073.children.append(Transform1074)
Shape1077 = x3d.Shape()
LineSet1078 = x3d.LineSet()
LineSet1078.vertexCount = [2]
Coordinate1079 = x3d.Coordinate()
Coordinate1079.point = (0.2029,1.4376,-0.0387,0.2014,1.1357,-0.0682)

LineSet1078.coord = Coordinate1079
#from l_shoulder to l_elbow vertices 2
ColorRGBA1080 = x3d.ColorRGBA()
ColorRGBA1080.USE = "HAnimSegmentLineColorRGBA"

LineSet1078.color = ColorRGBA1080

Shape1077.geometry = LineSet1078

HAnimSegment1073.children.append(Shape1077)
HAnimSite1081 = x3d.HAnimSite()
HAnimSite1081.name = "l_humeral_medial_epicondyles_pt"
HAnimSite1081.DEF = "hanim_l_humeral_medial_epicondyles_pt"
HAnimSite1081.translation = [0.1735,1.1272,-0.1113]
TouchSensor1082 = x3d.TouchSensor()
TouchSensor1082.description = "HAnimSite l_humeral_medial_epicondyles_pt"

HAnimSite1081.children.append(TouchSensor1082)
Shape1083 = x3d.Shape()
Shape1083.USE = "HAnimSiteShape"

HAnimSite1081.children.append(Shape1083)

HAnimSegment1073.children.append(HAnimSite1081)
HAnimSite1084 = x3d.HAnimSite()
HAnimSite1084.name = "l_olecranon_pt"
HAnimSite1084.DEF = "hanim_l_olecranon_pt"
HAnimSite1084.translation = [-0.1962,1.1375,-0.1123]
TouchSensor1085 = x3d.TouchSensor()
TouchSensor1085.description = "HAnimSite l_olecranon_pt"

HAnimSite1084.children.append(TouchSensor1085)
Shape1086 = x3d.Shape()
Shape1086.USE = "HAnimSiteShape"

HAnimSite1084.children.append(Shape1086)

HAnimSegment1073.children.append(HAnimSite1084)
HAnimSite1087 = x3d.HAnimSite()
HAnimSite1087.name = "l_radial_styloid_pt"
HAnimSite1087.DEF = "hanim_l_radial_styloid_pt"
HAnimSite1087.translation = [0.1901,0.8645,-0.0415]
TouchSensor1088 = x3d.TouchSensor()
TouchSensor1088.description = "HAnimSite l_radial_styloid_pt"

HAnimSite1087.children.append(TouchSensor1088)
Shape1089 = x3d.Shape()
Shape1089.USE = "HAnimSiteShape"

HAnimSite1087.children.append(Shape1089)

HAnimSegment1073.children.append(HAnimSite1087)
HAnimSite1090 = x3d.HAnimSite()
HAnimSite1090.name = "l_radiale_pt"
HAnimSite1090.DEF = "hanim_l_radiale_pt"
HAnimSite1090.translation = [0.2182,1.1212,-0.1167]
TouchSensor1091 = x3d.TouchSensor()
TouchSensor1091.description = "HAnimSite l_radiale_pt"

HAnimSite1090.children.append(TouchSensor1091)
Shape1092 = x3d.Shape()
Shape1092.USE = "HAnimSiteShape"

HAnimSite1090.children.append(Shape1092)

HAnimSegment1073.children.append(HAnimSite1090)

HAnimJoint1072.children.append(HAnimSegment1073)
HAnimJoint1093 = x3d.HAnimJoint()
HAnimJoint1093.name = "l_elbow"
HAnimJoint1093.DEF = "hanim_l_elbow"
HAnimJoint1093.center = [0.2014,1.1357,-0.0682]
HAnimJoint1093.ulimit = [0,0,0]
HAnimJoint1093.llimit = [0,0,0]
HAnimSegment1094 = x3d.HAnimSegment()
HAnimSegment1094.name = "l_forearm"
HAnimSegment1094.DEF = "hanim_l_forearm"
Transform1095 = x3d.Transform()
Transform1095.translation = [0.2014,1.1357,-0.0682]
Transform1096 = x3d.Transform()
#Empty Transform
Shape1097 = x3d.Shape()
Shape1097.USE = "HAnimJointShape"

Transform1096.children.append(Shape1097)

Transform1095.children.append(Transform1096)

HAnimSegment1094.children.append(Transform1095)
Shape1098 = x3d.Shape()
LineSet1099 = x3d.LineSet()
LineSet1099.vertexCount = [2]
Coordinate1100 = x3d.Coordinate()
Coordinate1100.point = (0.2014,1.1357,-0.0682,0.1984,0.8663,-0.0583)

LineSet1099.coord = Coordinate1100
#from l_elbow to l_radiocarpal vertices 2
ColorRGBA1101 = x3d.ColorRGBA()
ColorRGBA1101.USE = "HAnimSegmentLineColorRGBA"

LineSet1099.color = ColorRGBA1101

Shape1098.geometry = LineSet1099

HAnimSegment1094.children.append(Shape1098)
HAnimSite1102 = x3d.HAnimSite()
HAnimSite1102.name = "l_ulnar_styloid_pt"
HAnimSite1102.DEF = "hanim_l_ulnar_styloid_pt"
HAnimSite1102.translation = [-0.2142,0.8529,-0.0648]
TouchSensor1103 = x3d.TouchSensor()
TouchSensor1103.description = "HAnimSite l_ulnar_styloid_pt"

HAnimSite1102.children.append(TouchSensor1103)
Shape1104 = x3d.Shape()
Shape1104.USE = "HAnimSiteShape"

HAnimSite1102.children.append(Shape1104)

HAnimSegment1094.children.append(HAnimSite1102)

HAnimJoint1093.children.append(HAnimSegment1094)
HAnimJoint1105 = x3d.HAnimJoint()
HAnimJoint1105.name = "l_radiocarpal"
HAnimJoint1105.DEF = "hanim_l_radiocarpal"
HAnimJoint1105.center = [0.1984,0.8663,-0.0583]
HAnimJoint1105.ulimit = [0,0,0]
HAnimJoint1105.llimit = [0,0,0]
HAnimSegment1106 = x3d.HAnimSegment()
HAnimSegment1106.name = "l_carpal"
HAnimSegment1106.DEF = "hanim_l_carpal"
Transform1107 = x3d.Transform()
Transform1107.scale = [0.2,0.2,0.2]
Transform1107.translation = [0.2,0.85,-0.05]
Transform1107.rotation = [0,0,1,-3.14]
#Transform left hand
Transform1108 = x3d.Transform()
Transform1108.rotation = [0,1,0,-1.57]
#Transform left hand
Shape1109 = x3d.Shape()
Shape1109.USE = "HAnimJointShape"

Transform1108.children.append(Shape1109)

Transform1107.children.append(Transform1108)

HAnimSegment1106.children.append(Transform1107)
Shape1110 = x3d.Shape()
LineSet1111 = x3d.LineSet()
LineSet1111.vertexCount = [2]
Coordinate1112 = x3d.Coordinate()
Coordinate1112.point = (0.1984,0.8663,-0.0583,0.1984,0.8663,-0.0583)

LineSet1111.coord = Coordinate1112
#from l_radiocarpal to l_midcarpal_1 vertices 2
ColorRGBA1113 = x3d.ColorRGBA()
ColorRGBA1113.USE = "HAnimSegmentLineColorRGBA"

LineSet1111.color = ColorRGBA1113

Shape1110.geometry = LineSet1111

HAnimSegment1106.children.append(Shape1110)
Shape1114 = x3d.Shape()
LineSet1115 = x3d.LineSet()
LineSet1115.vertexCount = [2]
Coordinate1116 = x3d.Coordinate()
Coordinate1116.point = (0.1984,0.8663,-0.0583,0.1984,0.8663,-0.0583)

LineSet1115.coord = Coordinate1116
#from l_radiocarpal to l_midcarpal_2 vertices 2
ColorRGBA1117 = x3d.ColorRGBA()
ColorRGBA1117.USE = "HAnimSegmentLineColorRGBA"

LineSet1115.color = ColorRGBA1117

Shape1114.geometry = LineSet1115

HAnimSegment1106.children.append(Shape1114)
Shape1118 = x3d.Shape()
LineSet1119 = x3d.LineSet()
LineSet1119.vertexCount = [2]
Coordinate1120 = x3d.Coordinate()
Coordinate1120.point = (0.1984,0.8663,-0.0583,0.1984,0.8663,-0.0583)

LineSet1119.coord = Coordinate1120
#from l_radiocarpal to l_midcarpal_3 vertices 2
ColorRGBA1121 = x3d.ColorRGBA()
ColorRGBA1121.USE = "HAnimSegmentLineColorRGBA"

LineSet1119.color = ColorRGBA1121

Shape1118.geometry = LineSet1119

HAnimSegment1106.children.append(Shape1118)
Shape1122 = x3d.Shape()
LineSet1123 = x3d.LineSet()
LineSet1123.vertexCount = [2]
Coordinate1124 = x3d.Coordinate()
Coordinate1124.point = (0.1984,0.8663,-0.0583,0.1984,0.8663,-0.0583)

LineSet1123.coord = Coordinate1124
#from l_radiocarpal to l_midcarpal_4_5 vertices 2
ColorRGBA1125 = x3d.ColorRGBA()
ColorRGBA1125.USE = "HAnimSegmentLineColorRGBA"

LineSet1123.color = ColorRGBA1125

Shape1122.geometry = LineSet1123

HAnimSegment1106.children.append(Shape1122)

HAnimJoint1105.children.append(HAnimSegment1106)
HAnimJoint1126 = x3d.HAnimJoint()
HAnimJoint1126.name = "l_midcarpal_1"
HAnimJoint1126.DEF = "hanim_l_midcarpal_1"
HAnimJoint1126.ulimit = [0,0,0]
HAnimJoint1126.llimit = [0,0,0]
HAnimSegment1127 = x3d.HAnimSegment()
HAnimSegment1127.name = "l_trapezium"
HAnimSegment1127.DEF = "hanim_l_trapezium"
Transform1128 = x3d.Transform()
Transform1128.translation = [0.1984,0.8663,-0.0583]
Transform1129 = x3d.Transform()
#Empty Transform
Shape1130 = x3d.Shape()
Shape1130.USE = "HAnimJointShape"

Transform1129.children.append(Shape1130)

Transform1128.children.append(Transform1129)

HAnimSegment1127.children.append(Transform1128)
Shape1131 = x3d.Shape()
LineSet1132 = x3d.LineSet()
LineSet1132.vertexCount = [2]
Coordinate1133 = x3d.Coordinate()
Coordinate1133.point = (0.1924,0.8472,-0.0534)

LineSet1132.coord = Coordinate1133
#from l_midcarpal_1 to l_carpometacarpal_1 vertices 1
ColorRGBA1134 = x3d.ColorRGBA()
ColorRGBA1134.USE = "HAnimSegmentLineColorRGBA"

LineSet1132.color = ColorRGBA1134

Shape1131.geometry = LineSet1132

HAnimSegment1127.children.append(Shape1131)

HAnimJoint1126.children.append(HAnimSegment1127)
HAnimJoint1135 = x3d.HAnimJoint()
HAnimJoint1135.name = "l_carpometacarpal_1"
HAnimJoint1135.DEF = "hanim_l_carpometacarpal_1"
HAnimJoint1135.center = [0.1924,0.8472,-0.0534]
HAnimJoint1135.ulimit = [0,0,0]
HAnimJoint1135.llimit = [0,0,0]
HAnimSegment1136 = x3d.HAnimSegment()
HAnimSegment1136.name = "l_metacarpal_1"
HAnimSegment1136.DEF = "hanim_l_metacarpal_1"
Transform1137 = x3d.Transform()
Transform1137.translation = [0.1924,0.8472,-0.0534]
Transform1138 = x3d.Transform()
#Empty Transform
Shape1139 = x3d.Shape()
Shape1139.USE = "HAnimJointShape"

Transform1138.children.append(Shape1139)

Transform1137.children.append(Transform1138)

HAnimSegment1136.children.append(Transform1137)
Shape1140 = x3d.Shape()
LineSet1141 = x3d.LineSet()
LineSet1141.vertexCount = [2]
Coordinate1142 = x3d.Coordinate()
Coordinate1142.point = (0.1924,0.8472,-0.0534,0.1951,0.8226,0.0246)

LineSet1141.coord = Coordinate1142
#from l_carpometacarpal_1 to l_metacarpophalangeal_1 vertices 2
ColorRGBA1143 = x3d.ColorRGBA()
ColorRGBA1143.USE = "HAnimSegmentLineColorRGBA"

LineSet1141.color = ColorRGBA1143

Shape1140.geometry = LineSet1141

HAnimSegment1136.children.append(Shape1140)

HAnimJoint1135.children.append(HAnimSegment1136)
HAnimJoint1144 = x3d.HAnimJoint()
HAnimJoint1144.name = "l_metacarpophalangeal_1"
HAnimJoint1144.DEF = "hanim_l_metacarpophalangeal_1"
HAnimJoint1144.center = [0.1951,0.8226,0.0246]
HAnimJoint1144.ulimit = [0,0,0]
HAnimJoint1144.llimit = [0,0,0]
HAnimSegment1145 = x3d.HAnimSegment()
HAnimSegment1145.name = "l_carpal_proximal_phalanx_1"
HAnimSegment1145.DEF = "hanim_l_carpal_proximal_phalanx_1"
Transform1146 = x3d.Transform()
Transform1146.translation = [0.1951,0.8226,0.0246]
Transform1147 = x3d.Transform()
#Empty Transform
Shape1148 = x3d.Shape()
Shape1148.USE = "HAnimJointShape"

Transform1147.children.append(Shape1148)

Transform1146.children.append(Transform1147)

HAnimSegment1145.children.append(Transform1146)
Shape1149 = x3d.Shape()
LineSet1150 = x3d.LineSet()
LineSet1150.vertexCount = [2]
Coordinate1151 = x3d.Coordinate()
Coordinate1151.point = (0.1951,0.8226,0.0246,0.1955,0.8159,0.0464)

LineSet1150.coord = Coordinate1151
#from l_metacarpophalangeal_1 to l_carpal_interphalangeal_1 vertices 2
ColorRGBA1152 = x3d.ColorRGBA()
ColorRGBA1152.USE = "HAnimSegmentLineColorRGBA"

LineSet1150.color = ColorRGBA1152

Shape1149.geometry = LineSet1150

HAnimSegment1145.children.append(Shape1149)
HAnimSite1153 = x3d.HAnimSite()
HAnimSite1153.name = "l_carpal_distal_phalanx_1_tip"
HAnimSite1153.DEF = "hanim_l_carpal_distal_phalanx_1_tip"
TouchSensor1154 = x3d.TouchSensor()
TouchSensor1154.description = "HAnimSite l_carpal_distal_phalanx_1_tip"

HAnimSite1153.children.append(TouchSensor1154)
Shape1155 = x3d.Shape()
Shape1155.USE = "HAnimSiteShape"

HAnimSite1153.children.append(Shape1155)

HAnimSegment1145.children.append(HAnimSite1153)

HAnimJoint1144.children.append(HAnimSegment1145)
HAnimJoint1156 = x3d.HAnimJoint()
HAnimJoint1156.name = "l_carpal_interphalangeal_1"
HAnimJoint1156.DEF = "hanim_l_carpal_interphalangeal_1"
HAnimJoint1156.center = [0.1955,0.8159,0.0464]
HAnimJoint1156.ulimit = [0,0,0]
HAnimJoint1156.llimit = [0,0,0]

HAnimJoint1144.children.append(HAnimJoint1156)

HAnimJoint1135.children.append(HAnimJoint1144)

HAnimJoint1126.children.append(HAnimJoint1135)

HAnimJoint1105.children.append(HAnimJoint1126)
HAnimJoint1157 = x3d.HAnimJoint()
HAnimJoint1157.name = "l_midcarpal_2"
HAnimJoint1157.DEF = "hanim_l_midcarpal_2"
HAnimJoint1157.ulimit = [0,0,0]
HAnimJoint1157.llimit = [0,0,0]
HAnimSegment1158 = x3d.HAnimSegment()
HAnimSegment1158.name = "l_trapezoid"
HAnimSegment1158.DEF = "hanim_l_trapezoid"
Transform1159 = x3d.Transform()
Transform1159.translation = [0.1955,0.8159,0.0464]
Transform1160 = x3d.Transform()
#Empty Transform
Shape1161 = x3d.Shape()
Shape1161.USE = "HAnimJointShape"

Transform1160.children.append(Shape1161)

Transform1159.children.append(Transform1160)

HAnimSegment1158.children.append(Transform1159)
Shape1162 = x3d.Shape()
LineSet1163 = x3d.LineSet()
LineSet1163.vertexCount = [2]
Coordinate1164 = x3d.Coordinate()
Coordinate1164.point = (0.1983,0.8024,-0.0280)

LineSet1163.coord = Coordinate1164
#from l_midcarpal_2 to l_carpometacarpal_2 vertices 1
ColorRGBA1165 = x3d.ColorRGBA()
ColorRGBA1165.USE = "HAnimSegmentLineColorRGBA"

LineSet1163.color = ColorRGBA1165

Shape1162.geometry = LineSet1163

HAnimSegment1158.children.append(Shape1162)
HAnimSite1166 = x3d.HAnimSite()
HAnimSite1166.name = "l_metacarpal_phalanx_2_pt"
HAnimSite1166.DEF = "hanim_l_metacarpal_phalanx_2_pt"
HAnimSite1166.translation = [0.2009,0.8139,-0.0237]
TouchSensor1167 = x3d.TouchSensor()
TouchSensor1167.description = "HAnimSite l_metacarpal_phalanx_2_pt"

HAnimSite1166.children.append(TouchSensor1167)
Shape1168 = x3d.Shape()
Shape1168.USE = "HAnimSiteShape"

HAnimSite1166.children.append(Shape1168)

HAnimSegment1158.children.append(HAnimSite1166)

HAnimJoint1157.children.append(HAnimSegment1158)
HAnimJoint1169 = x3d.HAnimJoint()
HAnimJoint1169.name = "l_carpometacarpal_2"
HAnimJoint1169.DEF = "hanim_l_carpometacarpal_2"
HAnimJoint1169.center = [0.1983,0.8024,-0.028]
HAnimJoint1169.ulimit = [0,0,0]
HAnimJoint1169.llimit = [0,0,0]
HAnimSegment1170 = x3d.HAnimSegment()
HAnimSegment1170.name = "l_metacarpal_2"
HAnimSegment1170.DEF = "hanim_l_metacarpal_2"
Transform1171 = x3d.Transform()
Transform1171.translation = [0.1983,0.8024,-0.028]
Transform1172 = x3d.Transform()
#Empty Transform
Shape1173 = x3d.Shape()
Shape1173.USE = "HAnimJointShape"

Transform1172.children.append(Shape1173)

Transform1171.children.append(Transform1172)

HAnimSegment1170.children.append(Transform1171)
Shape1174 = x3d.Shape()
LineSet1175 = x3d.LineSet()
LineSet1175.vertexCount = [2]
Coordinate1176 = x3d.Coordinate()
Coordinate1176.point = (0.1983,0.8024,-0.0280,0.1983,0.7815,-0.0280)

LineSet1175.coord = Coordinate1176
#from l_carpometacarpal_2 to l_metacarpophalangeal_2 vertices 2
ColorRGBA1177 = x3d.ColorRGBA()
ColorRGBA1177.USE = "HAnimSegmentLineColorRGBA"

LineSet1175.color = ColorRGBA1177

Shape1174.geometry = LineSet1175

HAnimSegment1170.children.append(Shape1174)

HAnimJoint1169.children.append(HAnimSegment1170)
HAnimJoint1178 = x3d.HAnimJoint()
HAnimJoint1178.name = "l_metacarpophalangeal_2"
HAnimJoint1178.DEF = "hanim_l_metacarpophalangeal_2"
HAnimJoint1178.center = [0.1983,0.7815,-0.028]
HAnimJoint1178.ulimit = [0,0,0]
HAnimJoint1178.llimit = [0,0,0]
HAnimSegment1179 = x3d.HAnimSegment()
HAnimSegment1179.name = "l_carpal_proximal_phalanx_2"
HAnimSegment1179.DEF = "hanim_l_carpal_proximal_phalanx_2"
Transform1180 = x3d.Transform()
Transform1180.translation = [0.1983,0.7815,-0.028]
Transform1181 = x3d.Transform()
#Empty Transform
Shape1182 = x3d.Shape()
Shape1182.USE = "HAnimJointShape"

Transform1181.children.append(Shape1182)

Transform1180.children.append(Transform1181)

HAnimSegment1179.children.append(Transform1180)
Shape1183 = x3d.Shape()
LineSet1184 = x3d.LineSet()
LineSet1184.vertexCount = [2]
Coordinate1185 = x3d.Coordinate()
Coordinate1185.point = (0.1983,0.7815,-0.0280,0.2017,0.7363,-0.0248)

LineSet1184.coord = Coordinate1185
#from l_metacarpophalangeal_2 to l_carpal_proximal_interphalangeal_2 vertices 2
ColorRGBA1186 = x3d.ColorRGBA()
ColorRGBA1186.USE = "HAnimSegmentLineColorRGBA"

LineSet1184.color = ColorRGBA1186

Shape1183.geometry = LineSet1184

HAnimSegment1179.children.append(Shape1183)

HAnimJoint1178.children.append(HAnimSegment1179)
HAnimJoint1187 = x3d.HAnimJoint()
HAnimJoint1187.name = "l_carpal_proximal_interphalangeal_2"
HAnimJoint1187.DEF = "hanim_l_carpal_proximal_interphalangeal_2"
HAnimJoint1187.center = [0.2017,0.7363,-0.0248]
HAnimJoint1187.ulimit = [0,0,0]
HAnimJoint1187.llimit = [0,0,0]
HAnimSegment1188 = x3d.HAnimSegment()
HAnimSegment1188.name = "l_carpal_middle_phalanx_2"
HAnimSegment1188.DEF = "hanim_l_carpal_middle_phalanx_2"
Transform1189 = x3d.Transform()
Transform1189.translation = [0.2017,0.7363,-0.0248]
Transform1190 = x3d.Transform()
#Empty Transform
Shape1191 = x3d.Shape()
Shape1191.USE = "HAnimJointShape"

Transform1190.children.append(Shape1191)

Transform1189.children.append(Transform1190)

HAnimSegment1188.children.append(Transform1189)
Shape1192 = x3d.Shape()
LineSet1193 = x3d.LineSet()
LineSet1193.vertexCount = [2]
Coordinate1194 = x3d.Coordinate()
Coordinate1194.point = (0.2017,0.7363,-0.0248,0.2028,0.7139,-0.0236)

LineSet1193.coord = Coordinate1194
#from l_carpal_proximal_interphalangeal_2 to l_carpal_distal_interphalangeal_2 vertices 2
ColorRGBA1195 = x3d.ColorRGBA()
ColorRGBA1195.USE = "HAnimSegmentLineColorRGBA"

LineSet1193.color = ColorRGBA1195

Shape1192.geometry = LineSet1193

HAnimSegment1188.children.append(Shape1192)
HAnimSite1196 = x3d.HAnimSite()
HAnimSite1196.name = "l_carpal_distal_phalanx_2_tip"
HAnimSite1196.DEF = "hanim_l_carpal_distal_phalanx_2_tip"
TouchSensor1197 = x3d.TouchSensor()
TouchSensor1197.description = "HAnimSite l_carpal_distal_phalanx_2_tip"

HAnimSite1196.children.append(TouchSensor1197)
Shape1198 = x3d.Shape()
Shape1198.USE = "HAnimSiteShape"

HAnimSite1196.children.append(Shape1198)

HAnimSegment1188.children.append(HAnimSite1196)
HAnimSite1199 = x3d.HAnimSite()
HAnimSite1199.name = "l_dactylion_pt"
HAnimSite1199.DEF = "hanim_l_dactylion_pt"
HAnimSite1199.translation = [0.2056,0.6743,-0.0482]
TouchSensor1200 = x3d.TouchSensor()
TouchSensor1200.description = "HAnimSite l_dactylion_pt"

HAnimSite1199.children.append(TouchSensor1200)
Shape1201 = x3d.Shape()
Shape1201.USE = "HAnimSiteShape"

HAnimSite1199.children.append(Shape1201)

HAnimSegment1188.children.append(HAnimSite1199)

HAnimJoint1187.children.append(HAnimSegment1188)
HAnimJoint1202 = x3d.HAnimJoint()
HAnimJoint1202.name = "l_carpal_distal_interphalangeal_2"
HAnimJoint1202.DEF = "hanim_l_carpal_distal_interphalangeal_2"
HAnimJoint1202.center = [0.2028,0.7139,-0.0236]
HAnimJoint1202.ulimit = [0,0,0]
HAnimJoint1202.llimit = [0,0,0]

HAnimJoint1187.children.append(HAnimJoint1202)

HAnimJoint1178.children.append(HAnimJoint1187)

HAnimJoint1169.children.append(HAnimJoint1178)

HAnimJoint1157.children.append(HAnimJoint1169)

HAnimJoint1105.children.append(HAnimJoint1157)
HAnimJoint1203 = x3d.HAnimJoint()
HAnimJoint1203.name = "l_midcarpal_3"
HAnimJoint1203.DEF = "hanim_l_midcarpal_3"
HAnimJoint1203.ulimit = [0,0,0]
HAnimJoint1203.llimit = [0,0,0]
HAnimSegment1204 = x3d.HAnimSegment()
HAnimSegment1204.name = "l_capitate"
HAnimSegment1204.DEF = "hanim_l_capitate"
Transform1205 = x3d.Transform()
Transform1205.translation = [0.2028,0.7139,-0.0236]
Transform1206 = x3d.Transform()
#Empty Transform
Shape1207 = x3d.Shape()
Shape1207.USE = "HAnimJointShape"

Transform1206.children.append(Shape1207)

Transform1205.children.append(Transform1206)

HAnimSegment1204.children.append(Transform1205)
Shape1208 = x3d.Shape()
LineSet1209 = x3d.LineSet()
LineSet1209.vertexCount = [2]
Coordinate1210 = x3d.Coordinate()
Coordinate1210.point = (0.1987,0.8029,-0.0530)

LineSet1209.coord = Coordinate1210
#from l_midcarpal_3 to l_carpometacarpal_3 vertices 1
ColorRGBA1211 = x3d.ColorRGBA()
ColorRGBA1211.USE = "HAnimSegmentLineColorRGBA"

LineSet1209.color = ColorRGBA1211

Shape1208.geometry = LineSet1209

HAnimSegment1204.children.append(Shape1208)
HAnimSite1212 = x3d.HAnimSite()
HAnimSite1212.name = "l_metacarpal_phalanx_3_pt"
HAnimSite1212.DEF = "hanim_l_metacarpal_phalanx_3_pt"
TouchSensor1213 = x3d.TouchSensor()
TouchSensor1213.description = "HAnimSite l_metacarpal_phalanx_3_pt"

HAnimSite1212.children.append(TouchSensor1213)
Shape1214 = x3d.Shape()
Shape1214.USE = "HAnimSiteShape"

HAnimSite1212.children.append(Shape1214)

HAnimSegment1204.children.append(HAnimSite1212)

HAnimJoint1203.children.append(HAnimSegment1204)
HAnimJoint1215 = x3d.HAnimJoint()
HAnimJoint1215.name = "l_carpometacarpal_3"
HAnimJoint1215.DEF = "hanim_l_carpometacarpal_3"
HAnimJoint1215.center = [0.1987,0.8029,-0.053]
HAnimJoint1215.ulimit = [0,0,0]
HAnimJoint1215.llimit = [0,0,0]
HAnimSegment1216 = x3d.HAnimSegment()
HAnimSegment1216.name = "l_metacarpal_3"
HAnimSegment1216.DEF = "hanim_l_metacarpal_3"
Transform1217 = x3d.Transform()
Transform1217.translation = [0.1987,0.8029,-0.053]
Transform1218 = x3d.Transform()
#Empty Transform
Shape1219 = x3d.Shape()
Shape1219.USE = "HAnimJointShape"

Transform1218.children.append(Shape1219)

Transform1217.children.append(Transform1218)

HAnimSegment1216.children.append(Transform1217)
Shape1220 = x3d.Shape()
LineSet1221 = x3d.LineSet()
LineSet1221.vertexCount = [2]
Coordinate1222 = x3d.Coordinate()
Coordinate1222.point = (0.1987,0.8029,-0.0530,0.1987,0.7818,-0.0530)

LineSet1221.coord = Coordinate1222
#from l_carpometacarpal_3 to l_metacarpophalangeal_3 vertices 2
ColorRGBA1223 = x3d.ColorRGBA()
ColorRGBA1223.USE = "HAnimSegmentLineColorRGBA"

LineSet1221.color = ColorRGBA1223

Shape1220.geometry = LineSet1221

HAnimSegment1216.children.append(Shape1220)

HAnimJoint1215.children.append(HAnimSegment1216)
HAnimJoint1224 = x3d.HAnimJoint()
HAnimJoint1224.name = "l_metacarpophalangeal_3"
HAnimJoint1224.DEF = "hanim_l_metacarpophalangeal_3"
HAnimJoint1224.center = [0.1987,0.7818,-0.053]
HAnimJoint1224.ulimit = [0,0,0]
HAnimJoint1224.llimit = [0,0,0]
HAnimSegment1225 = x3d.HAnimSegment()
HAnimSegment1225.name = "l_carpal_proximal_phalanx_3"
HAnimSegment1225.DEF = "hanim_l_carpal_proximal_phalanx_3"
Transform1226 = x3d.Transform()
Transform1226.translation = [0.1987,0.7818,-0.053]
Transform1227 = x3d.Transform()
#Empty Transform
Shape1228 = x3d.Shape()
Shape1228.USE = "HAnimJointShape"

Transform1227.children.append(Shape1228)

Transform1226.children.append(Transform1227)

HAnimSegment1225.children.append(Transform1226)
Shape1229 = x3d.Shape()
LineSet1230 = x3d.LineSet()
LineSet1230.vertexCount = [2]
Coordinate1231 = x3d.Coordinate()
Coordinate1231.point = (0.1987,0.7818,-0.0530,0.2013,0.7273,-0.0503)

LineSet1230.coord = Coordinate1231
#from l_metacarpophalangeal_3 to l_carpal_proximal_interphalangeal_3 vertices 2
ColorRGBA1232 = x3d.ColorRGBA()
ColorRGBA1232.USE = "HAnimSegmentLineColorRGBA"

LineSet1230.color = ColorRGBA1232

Shape1229.geometry = LineSet1230

HAnimSegment1225.children.append(Shape1229)

HAnimJoint1224.children.append(HAnimSegment1225)
HAnimJoint1233 = x3d.HAnimJoint()
HAnimJoint1233.name = "l_carpal_proximal_interphalangeal_3"
HAnimJoint1233.DEF = "hanim_l_carpal_proximal_interphalangeal_3"
HAnimJoint1233.center = [0.2013,0.7273,-0.0503]
HAnimJoint1233.ulimit = [0,0,0]
HAnimJoint1233.llimit = [0,0,0]
HAnimSegment1234 = x3d.HAnimSegment()
HAnimSegment1234.name = "l_carpal_middle_phalanx_3"
HAnimSegment1234.DEF = "hanim_l_carpal_middle_phalanx_3"
Transform1235 = x3d.Transform()
Transform1235.translation = [0.2013,0.7273,-0.0503]
Transform1236 = x3d.Transform()
#Empty Transform
Shape1237 = x3d.Shape()
Shape1237.USE = "HAnimJointShape"

Transform1236.children.append(Shape1237)

Transform1235.children.append(Transform1236)

HAnimSegment1234.children.append(Transform1235)
Shape1238 = x3d.Shape()
LineSet1239 = x3d.LineSet()
LineSet1239.vertexCount = [2]
Coordinate1240 = x3d.Coordinate()
Coordinate1240.point = (0.2013,0.7273,-0.0503,0.2026,0.7011,-0.0494)

LineSet1239.coord = Coordinate1240
#from l_carpal_proximal_interphalangeal_3 to l_carpal_distal_interphalangeal_3 vertices 2
ColorRGBA1241 = x3d.ColorRGBA()
ColorRGBA1241.USE = "HAnimSegmentLineColorRGBA"

LineSet1239.color = ColorRGBA1241

Shape1238.geometry = LineSet1239

HAnimSegment1234.children.append(Shape1238)
HAnimSite1242 = x3d.HAnimSite()
HAnimSite1242.name = "l_carpal_distal_phalanx_3_tip"
HAnimSite1242.DEF = "hanim_l_carpal_distal_phalanx_3_tip"
TouchSensor1243 = x3d.TouchSensor()
TouchSensor1243.description = "HAnimSite l_carpal_distal_phalanx_3_tip"

HAnimSite1242.children.append(TouchSensor1243)
Shape1244 = x3d.Shape()
Shape1244.USE = "HAnimSiteShape"

HAnimSite1242.children.append(Shape1244)

HAnimSegment1234.children.append(HAnimSite1242)

HAnimJoint1233.children.append(HAnimSegment1234)
HAnimJoint1245 = x3d.HAnimJoint()
HAnimJoint1245.name = "l_carpal_distal_interphalangeal_3"
HAnimJoint1245.DEF = "hanim_l_carpal_distal_interphalangeal_3"
HAnimJoint1245.center = [0.2026,0.7011,-0.0494]
HAnimJoint1245.ulimit = [0,0,0]
HAnimJoint1245.llimit = [0,0,0]

HAnimJoint1233.children.append(HAnimJoint1245)

HAnimJoint1224.children.append(HAnimJoint1233)

HAnimJoint1215.children.append(HAnimJoint1224)

HAnimJoint1203.children.append(HAnimJoint1215)

HAnimJoint1105.children.append(HAnimJoint1203)
HAnimJoint1246 = x3d.HAnimJoint()
HAnimJoint1246.name = "l_midcarpal_4_5"
HAnimJoint1246.DEF = "hanim_l_midcarpal_4_5"
HAnimJoint1246.ulimit = [0,0,0]
HAnimJoint1246.llimit = [0,0,0]
HAnimSegment1247 = x3d.HAnimSegment()
HAnimSegment1247.name = "l_hamate"
HAnimSegment1247.DEF = "hanim_l_hamate"
Transform1248 = x3d.Transform()
Transform1248.translation = [0.2026,0.7011,-0.0494]
Transform1249 = x3d.Transform()
#Empty Transform
Shape1250 = x3d.Shape()
Shape1250.USE = "HAnimJointShape"

Transform1249.children.append(Shape1250)

Transform1248.children.append(Transform1249)

HAnimSegment1247.children.append(Transform1248)
Shape1251 = x3d.Shape()
LineSet1252 = x3d.LineSet()
LineSet1252.vertexCount = [2]
Coordinate1253 = x3d.Coordinate()
Coordinate1253.point = (0.1956,0.8019,-0.0794)

LineSet1252.coord = Coordinate1253
#from l_midcarpal_4_5 to l_carpometacarpal_4 vertices 1
ColorRGBA1254 = x3d.ColorRGBA()
ColorRGBA1254.USE = "HAnimSegmentLineColorRGBA"

LineSet1252.color = ColorRGBA1254

Shape1251.geometry = LineSet1252

HAnimSegment1247.children.append(Shape1251)
Shape1255 = x3d.Shape()
LineSet1256 = x3d.LineSet()
LineSet1256.vertexCount = [2]
Coordinate1257 = x3d.Coordinate()
Coordinate1257.point = (0.1925,0.8066,-0.1036)

LineSet1256.coord = Coordinate1257
#from l_midcarpal_4_5 to l_carpometacarpal_5 vertices 1
ColorRGBA1258 = x3d.ColorRGBA()
ColorRGBA1258.USE = "HAnimSegmentLineColorRGBA"

LineSet1256.color = ColorRGBA1258

Shape1255.geometry = LineSet1256

HAnimSegment1247.children.append(Shape1255)
HAnimSite1259 = x3d.HAnimSite()
HAnimSite1259.name = "l_metacarpal_phalanx_5_pt"
HAnimSite1259.DEF = "hanim_l_metacarpal_phalanx_5_pt"
HAnimSite1259.translation = [0.1929,0.786,-0.1122]
TouchSensor1260 = x3d.TouchSensor()
TouchSensor1260.description = "HAnimSite l_metacarpal_phalanx_5_pt"

HAnimSite1259.children.append(TouchSensor1260)
Shape1261 = x3d.Shape()
Shape1261.USE = "HAnimSiteShape"

HAnimSite1259.children.append(Shape1261)

HAnimSegment1247.children.append(HAnimSite1259)

HAnimJoint1246.children.append(HAnimSegment1247)
HAnimJoint1262 = x3d.HAnimJoint()
HAnimJoint1262.name = "l_carpometacarpal_4"
HAnimJoint1262.DEF = "hanim_l_carpometacarpal_4"
HAnimJoint1262.center = [0.1956,0.8019,-0.0794]
HAnimJoint1262.ulimit = [0,0,0]
HAnimJoint1262.llimit = [0,0,0]
HAnimSegment1263 = x3d.HAnimSegment()
HAnimSegment1263.name = "l_metacarpal_4"
HAnimSegment1263.DEF = "hanim_l_metacarpal_4"
Transform1264 = x3d.Transform()
Transform1264.translation = [0.1956,0.8019,-0.0794]
Transform1265 = x3d.Transform()
#Empty Transform
Shape1266 = x3d.Shape()
Shape1266.USE = "HAnimJointShape"

Transform1265.children.append(Shape1266)

Transform1264.children.append(Transform1265)

HAnimSegment1263.children.append(Transform1264)
Shape1267 = x3d.Shape()
LineSet1268 = x3d.LineSet()
LineSet1268.vertexCount = [2]
Coordinate1269 = x3d.Coordinate()
Coordinate1269.point = (0.1956,0.8019,-0.0794,0.1956,0.7815,-0.0794)

LineSet1268.coord = Coordinate1269
#from l_carpometacarpal_4 to l_metacarpophalangeal_4 vertices 2
ColorRGBA1270 = x3d.ColorRGBA()
ColorRGBA1270.USE = "HAnimSegmentLineColorRGBA"

LineSet1268.color = ColorRGBA1270

Shape1267.geometry = LineSet1268

HAnimSegment1263.children.append(Shape1267)

HAnimJoint1262.children.append(HAnimSegment1263)
HAnimJoint1271 = x3d.HAnimJoint()
HAnimJoint1271.name = "l_metacarpophalangeal_4"
HAnimJoint1271.DEF = "hanim_l_metacarpophalangeal_4"
HAnimJoint1271.center = [0.1956,0.7815,-0.0794]
HAnimJoint1271.ulimit = [0,0,0]
HAnimJoint1271.llimit = [0,0,0]
HAnimSegment1272 = x3d.HAnimSegment()
HAnimSegment1272.name = "l_carpal_proximal_phalanx_4"
HAnimSegment1272.DEF = "hanim_l_carpal_proximal_phalanx_4"
Transform1273 = x3d.Transform()
Transform1273.translation = [0.1956,0.7815,-0.0794]
Transform1274 = x3d.Transform()
#Empty Transform
Shape1275 = x3d.Shape()
Shape1275.USE = "HAnimJointShape"

Transform1274.children.append(Shape1275)

Transform1273.children.append(Transform1274)

HAnimSegment1272.children.append(Transform1273)
Shape1276 = x3d.Shape()
LineSet1277 = x3d.LineSet()
LineSet1277.vertexCount = [2]
Coordinate1278 = x3d.Coordinate()
Coordinate1278.point = (0.1956,0.7815,-0.0794,0.1973,0.7287,-0.0777)

LineSet1277.coord = Coordinate1278
#from l_metacarpophalangeal_4 to l_carpal_proximal_interphalangeal_4 vertices 2
ColorRGBA1279 = x3d.ColorRGBA()
ColorRGBA1279.USE = "HAnimSegmentLineColorRGBA"

LineSet1277.color = ColorRGBA1279

Shape1276.geometry = LineSet1277

HAnimSegment1272.children.append(Shape1276)

HAnimJoint1271.children.append(HAnimSegment1272)
HAnimJoint1280 = x3d.HAnimJoint()
HAnimJoint1280.name = "l_carpal_proximal_interphalangeal_4"
HAnimJoint1280.DEF = "hanim_l_carpal_proximal_interphalangeal_4"
HAnimJoint1280.center = [0.1973,0.7287,-0.0777]
HAnimJoint1280.ulimit = [0,0,0]
HAnimJoint1280.llimit = [0,0,0]
HAnimSegment1281 = x3d.HAnimSegment()
HAnimSegment1281.name = "l_carpal_middle_phalanx_4"
HAnimSegment1281.DEF = "hanim_l_carpal_middle_phalanx_4"
Transform1282 = x3d.Transform()
Transform1282.translation = [0.1973,0.7287,-0.0777]
Transform1283 = x3d.Transform()
#Empty Transform
Shape1284 = x3d.Shape()
Shape1284.USE = "HAnimJointShape"

Transform1283.children.append(Shape1284)

Transform1282.children.append(Transform1283)

HAnimSegment1281.children.append(Transform1282)
Shape1285 = x3d.Shape()
LineSet1286 = x3d.LineSet()
LineSet1286.vertexCount = [2]
Coordinate1287 = x3d.Coordinate()
Coordinate1287.point = (0.1973,0.7287,-0.0777,0.1983,0.7045,-0.0767)

LineSet1286.coord = Coordinate1287
#from l_carpal_proximal_interphalangeal_4 to l_carpal_distal_interphalangeal_4 vertices 2
ColorRGBA1288 = x3d.ColorRGBA()
ColorRGBA1288.USE = "HAnimSegmentLineColorRGBA"

LineSet1286.color = ColorRGBA1288

Shape1285.geometry = LineSet1286

HAnimSegment1281.children.append(Shape1285)
HAnimSite1289 = x3d.HAnimSite()
HAnimSite1289.name = "l_carpal_distal_phalanx_4_tip"
HAnimSite1289.DEF = "hanim_l_carpal_distal_phalanx_4_tip"
TouchSensor1290 = x3d.TouchSensor()
TouchSensor1290.description = "HAnimSite l_carpal_distal_phalanx_4_tip"

HAnimSite1289.children.append(TouchSensor1290)
Shape1291 = x3d.Shape()
Shape1291.USE = "HAnimSiteShape"

HAnimSite1289.children.append(Shape1291)

HAnimSegment1281.children.append(HAnimSite1289)

HAnimJoint1280.children.append(HAnimSegment1281)
HAnimJoint1292 = x3d.HAnimJoint()
HAnimJoint1292.name = "l_carpal_distal_interphalangeal_4"
HAnimJoint1292.DEF = "hanim_l_carpal_distal_interphalangeal_4"
HAnimJoint1292.center = [0.1983,0.7045,-0.0767]
HAnimJoint1292.ulimit = [0,0,0]
HAnimJoint1292.llimit = [0,0,0]

HAnimJoint1280.children.append(HAnimJoint1292)

HAnimJoint1271.children.append(HAnimJoint1280)

HAnimJoint1262.children.append(HAnimJoint1271)

HAnimJoint1246.children.append(HAnimJoint1262)
HAnimJoint1293 = x3d.HAnimJoint()
HAnimJoint1293.name = "l_carpometacarpal_5"
HAnimJoint1293.DEF = "hanim_l_carpometacarpal_5"
HAnimJoint1293.center = [0.1925,0.8066,-0.1036]
HAnimJoint1293.ulimit = [0,0,0]
HAnimJoint1293.llimit = [0,0,0]
HAnimSegment1294 = x3d.HAnimSegment()
HAnimSegment1294.name = "l_metacarpal_5"
HAnimSegment1294.DEF = "hanim_l_metacarpal_5"
Transform1295 = x3d.Transform()
Transform1295.translation = [0.1925,0.8066,-0.1036]
Transform1296 = x3d.Transform()
#Empty Transform
Shape1297 = x3d.Shape()
Shape1297.USE = "HAnimJointShape"

Transform1296.children.append(Shape1297)

Transform1295.children.append(Transform1296)

HAnimSegment1294.children.append(Transform1295)
Shape1298 = x3d.Shape()
LineSet1299 = x3d.LineSet()
LineSet1299.vertexCount = [2]
Coordinate1300 = x3d.Coordinate()
Coordinate1300.point = (0.1925,0.8066,-0.1036,0.1925,0.7866,-0.1036)

LineSet1299.coord = Coordinate1300
#from l_carpometacarpal_5 to l_metacarpophalangeal_5 vertices 2
ColorRGBA1301 = x3d.ColorRGBA()
ColorRGBA1301.USE = "HAnimSegmentLineColorRGBA"

LineSet1299.color = ColorRGBA1301

Shape1298.geometry = LineSet1299

HAnimSegment1294.children.append(Shape1298)

HAnimJoint1293.children.append(HAnimSegment1294)
HAnimJoint1302 = x3d.HAnimJoint()
HAnimJoint1302.name = "l_metacarpophalangeal_5"
HAnimJoint1302.DEF = "hanim_l_metacarpophalangeal_5"
HAnimJoint1302.center = [0.1925,0.7866,-0.1036]
HAnimJoint1302.ulimit = [0,0,0]
HAnimJoint1302.llimit = [0,0,0]
HAnimSegment1303 = x3d.HAnimSegment()
HAnimSegment1303.name = "l_carpal_proximal_phalanx_5"
HAnimSegment1303.DEF = "hanim_l_carpal_proximal_phalanx_5"
Transform1304 = x3d.Transform()
Transform1304.translation = [0.1925,0.7866,-0.1036]
Transform1305 = x3d.Transform()
#Empty Transform
Shape1306 = x3d.Shape()
Shape1306.USE = "HAnimJointShape"

Transform1305.children.append(Shape1306)

Transform1304.children.append(Transform1305)

HAnimSegment1303.children.append(Transform1304)
Shape1307 = x3d.Shape()
LineSet1308 = x3d.LineSet()
LineSet1308.vertexCount = [2]
Coordinate1309 = x3d.Coordinate()
Coordinate1309.point = (0.1925,0.7866,-0.1036,0.1938,0.7452,-0.1024)

LineSet1308.coord = Coordinate1309
#from l_metacarpophalangeal_5 to l_carpal_proximal_interphalangeal_5 vertices 2
ColorRGBA1310 = x3d.ColorRGBA()
ColorRGBA1310.USE = "HAnimSegmentLineColorRGBA"

LineSet1308.color = ColorRGBA1310

Shape1307.geometry = LineSet1308

HAnimSegment1303.children.append(Shape1307)

HAnimJoint1302.children.append(HAnimSegment1303)
HAnimJoint1311 = x3d.HAnimJoint()
HAnimJoint1311.name = "l_carpal_proximal_interphalangeal_5"
HAnimJoint1311.DEF = "hanim_l_carpal_proximal_interphalangeal_5"
HAnimJoint1311.center = [0.1938,0.7452,-0.1024]
HAnimJoint1311.ulimit = [0,0,0]
HAnimJoint1311.llimit = [0,0,0]
HAnimSegment1312 = x3d.HAnimSegment()
HAnimSegment1312.name = "l_carpal_middle_phalanx_5"
HAnimSegment1312.DEF = "hanim_l_carpal_middle_phalanx_5"
Transform1313 = x3d.Transform()
Transform1313.translation = [0.1938,0.7452,-0.1024]
Transform1314 = x3d.Transform()
#Empty Transform
Shape1315 = x3d.Shape()
Shape1315.USE = "HAnimJointShape"

Transform1314.children.append(Shape1315)

Transform1313.children.append(Transform1314)

HAnimSegment1312.children.append(Transform1313)
Shape1316 = x3d.Shape()
LineSet1317 = x3d.LineSet()
LineSet1317.vertexCount = [2]
Coordinate1318 = x3d.Coordinate()
Coordinate1318.point = (0.1938,0.7452,-0.1024,0.1948,0.7277,-0.1017)

LineSet1317.coord = Coordinate1318
#from l_carpal_proximal_interphalangeal_5 to l_carpal_distal_interphalangeal_5 vertices 2
ColorRGBA1319 = x3d.ColorRGBA()
ColorRGBA1319.USE = "HAnimSegmentLineColorRGBA"

LineSet1317.color = ColorRGBA1319

Shape1316.geometry = LineSet1317

HAnimSegment1312.children.append(Shape1316)
HAnimSite1320 = x3d.HAnimSite()
HAnimSite1320.name = "l_carpal_distal_phalanx_5_tip"
HAnimSite1320.DEF = "hanim_l_carpal_distal_phalanx_5_tip"
TouchSensor1321 = x3d.TouchSensor()
TouchSensor1321.description = "HAnimSite l_carpal_distal_phalanx_5_tip"

HAnimSite1320.children.append(TouchSensor1321)
Shape1322 = x3d.Shape()
Shape1322.USE = "HAnimSiteShape"

HAnimSite1320.children.append(Shape1322)

HAnimSegment1312.children.append(HAnimSite1320)

HAnimJoint1311.children.append(HAnimSegment1312)
HAnimJoint1323 = x3d.HAnimJoint()
HAnimJoint1323.name = "l_carpal_distal_interphalangeal_5"
HAnimJoint1323.DEF = "hanim_l_carpal_distal_interphalangeal_5"
HAnimJoint1323.center = [0.1948,0.7277,-0.1017]
HAnimJoint1323.ulimit = [0,0,0]
HAnimJoint1323.llimit = [0,0,0]

HAnimJoint1311.children.append(HAnimJoint1323)

HAnimJoint1302.children.append(HAnimJoint1311)

HAnimJoint1293.children.append(HAnimJoint1302)

HAnimJoint1246.children.append(HAnimJoint1293)

HAnimJoint1105.children.append(HAnimJoint1246)

HAnimJoint1093.children.append(HAnimJoint1105)

HAnimJoint1072.children.append(HAnimJoint1093)

HAnimJoint1057.children.append(HAnimJoint1072)

HAnimJoint1048.children.append(HAnimJoint1057)

HAnimJoint844.children.append(HAnimJoint1048)
HAnimJoint1324 = x3d.HAnimJoint()
HAnimJoint1324.name = "r_sternoclavicular"
HAnimJoint1324.DEF = "hanim_r_sternoclavicular"
HAnimJoint1324.center = [-0.0694,1.46,-0.033]
HAnimJoint1324.ulimit = [0,0,0]
HAnimJoint1324.llimit = [0,0,0]
HAnimSegment1325 = x3d.HAnimSegment()
HAnimSegment1325.name = "r_clavicle"
HAnimSegment1325.DEF = "hanim_r_clavicle"
Transform1326 = x3d.Transform()
Transform1326.translation = [-0.0694,1.46,-0.033]
Transform1327 = x3d.Transform()
#Empty Transform
Shape1328 = x3d.Shape()
Shape1328.USE = "HAnimJointShape"

Transform1327.children.append(Shape1328)

Transform1326.children.append(Transform1327)

HAnimSegment1325.children.append(Transform1326)
Shape1329 = x3d.Shape()
LineSet1330 = x3d.LineSet()
LineSet1330.vertexCount = [2]
Coordinate1331 = x3d.Coordinate()
Coordinate1331.point = (-0.0694,1.4600,-0.0330,-0.0836,1.4281,-0.0401)

LineSet1330.coord = Coordinate1331
#from r_sternoclavicular to r_acromioclavicular vertices 2
ColorRGBA1332 = x3d.ColorRGBA()
ColorRGBA1332.USE = "HAnimSegmentLineColorRGBA"

LineSet1330.color = ColorRGBA1332

Shape1329.geometry = LineSet1330

HAnimSegment1325.children.append(Shape1329)

HAnimJoint1324.children.append(HAnimSegment1325)
HAnimJoint1333 = x3d.HAnimJoint()
HAnimJoint1333.name = "r_acromioclavicular"
HAnimJoint1333.DEF = "hanim_r_acromioclavicular"
HAnimJoint1333.center = [-0.0836,1.4281,-0.0401]
HAnimJoint1333.ulimit = [0,0,0]
HAnimJoint1333.llimit = [0,0,0]
HAnimSegment1334 = x3d.HAnimSegment()
HAnimSegment1334.name = "r_scapula"
HAnimSegment1334.DEF = "hanim_r_scapula"
Transform1335 = x3d.Transform()
Transform1335.translation = [-0.0836,1.4281,-0.0401]
Transform1336 = x3d.Transform()
#Empty Transform
Shape1337 = x3d.Shape()
Shape1337.USE = "HAnimJointShape"

Transform1336.children.append(Shape1337)

Transform1335.children.append(Transform1336)

HAnimSegment1334.children.append(Transform1335)
Shape1338 = x3d.Shape()
LineSet1339 = x3d.LineSet()
LineSet1339.vertexCount = [2]
Coordinate1340 = x3d.Coordinate()
Coordinate1340.point = (-0.0836,1.4281,-0.0401,-0.1907,1.4407,-0.0325)

LineSet1339.coord = Coordinate1340
#from r_acromioclavicular to r_shoulder vertices 2
ColorRGBA1341 = x3d.ColorRGBA()
ColorRGBA1341.USE = "HAnimSegmentLineColorRGBA"

LineSet1339.color = ColorRGBA1341

Shape1338.geometry = LineSet1339

HAnimSegment1334.children.append(Shape1338)
HAnimSite1342 = x3d.HAnimSite()
HAnimSite1342.name = "r_bideltoid_pt"
HAnimSite1342.DEF = "hanim_r_bideltoid_pt"
TouchSensor1343 = x3d.TouchSensor()
TouchSensor1343.description = "HAnimSite r_bideltoid_pt"

HAnimSite1342.children.append(TouchSensor1343)
Shape1344 = x3d.Shape()
Shape1344.USE = "HAnimSiteShape"

HAnimSite1342.children.append(Shape1344)

HAnimSegment1334.children.append(HAnimSite1342)
HAnimSite1345 = x3d.HAnimSite()
HAnimSite1345.name = "r_humeral_lateral_epicondyles_pt"
HAnimSite1345.DEF = "hanim_r_humeral_lateral_epicondyles_pt"
HAnimSite1345.translation = [-0.2224,1.1517,-0.1033]
TouchSensor1346 = x3d.TouchSensor()
TouchSensor1346.description = "HAnimSite r_humeral_lateral_epicondyles_pt"

HAnimSite1345.children.append(TouchSensor1346)
Shape1347 = x3d.Shape()
Shape1347.USE = "HAnimSiteShape"

HAnimSite1345.children.append(Shape1347)

HAnimSegment1334.children.append(HAnimSite1345)

HAnimJoint1333.children.append(HAnimSegment1334)
HAnimJoint1348 = x3d.HAnimJoint()
HAnimJoint1348.name = "r_shoulder"
HAnimJoint1348.DEF = "hanim_r_shoulder"
HAnimJoint1348.center = [-0.1907,1.4407,-0.0325]
HAnimJoint1348.ulimit = [0,0,0]
HAnimJoint1348.llimit = [0,0,0]
HAnimSegment1349 = x3d.HAnimSegment()
HAnimSegment1349.name = "r_upperarm"
HAnimSegment1349.DEF = "hanim_r_upperarm"
Transform1350 = x3d.Transform()
Transform1350.translation = [-0.1907,1.4407,-0.0325]
Transform1351 = x3d.Transform()
#Empty Transform
Shape1352 = x3d.Shape()
Shape1352.USE = "HAnimJointShape"

Transform1351.children.append(Shape1352)

Transform1350.children.append(Transform1351)

HAnimSegment1349.children.append(Transform1350)
Shape1353 = x3d.Shape()
LineSet1354 = x3d.LineSet()
LineSet1354.vertexCount = [2]
Coordinate1355 = x3d.Coordinate()
Coordinate1355.point = (-0.1907,1.4407,-0.0325,-0.1949,1.1388,-0.0620)

LineSet1354.coord = Coordinate1355
#from r_shoulder to r_elbow vertices 2
ColorRGBA1356 = x3d.ColorRGBA()
ColorRGBA1356.USE = "HAnimSegmentLineColorRGBA"

LineSet1354.color = ColorRGBA1356

Shape1353.geometry = LineSet1354

HAnimSegment1349.children.append(Shape1353)
HAnimSite1357 = x3d.HAnimSite()
HAnimSite1357.name = "r_humeral_medial_epicondyles_pt"
HAnimSite1357.DEF = "hanim_r_humeral_medial_epicondyles_pt"
HAnimSite1357.translation = [-0.168,1.1298,-0.1062]
TouchSensor1358 = x3d.TouchSensor()
TouchSensor1358.description = "HAnimSite r_humeral_medial_epicondyles_pt"

HAnimSite1357.children.append(TouchSensor1358)
Shape1359 = x3d.Shape()
Shape1359.USE = "HAnimSiteShape"

HAnimSite1357.children.append(Shape1359)

HAnimSegment1349.children.append(HAnimSite1357)
HAnimSite1360 = x3d.HAnimSite()
HAnimSite1360.name = "r_olecranon_pt"
HAnimSite1360.DEF = "hanim_r_olecranon_pt"
HAnimSite1360.translation = [-0.1907,1.1405,-0.1065]
TouchSensor1361 = x3d.TouchSensor()
TouchSensor1361.description = "HAnimSite r_olecranon_pt"

HAnimSite1360.children.append(TouchSensor1361)
Shape1362 = x3d.Shape()
Shape1362.USE = "HAnimSiteShape"

HAnimSite1360.children.append(Shape1362)

HAnimSegment1349.children.append(HAnimSite1360)
HAnimSite1363 = x3d.HAnimSite()
HAnimSite1363.name = "r_radial_styloid_pt"
HAnimSite1363.DEF = "hanim_r_radial_styloid_pt"
HAnimSite1363.translation = [-0.1884,0.8676,-0.036]
TouchSensor1364 = x3d.TouchSensor()
TouchSensor1364.description = "HAnimSite r_radial_styloid_pt"

HAnimSite1363.children.append(TouchSensor1364)
Shape1365 = x3d.Shape()
Shape1365.USE = "HAnimSiteShape"

HAnimSite1363.children.append(Shape1365)

HAnimSegment1349.children.append(HAnimSite1363)
HAnimSite1366 = x3d.HAnimSite()
HAnimSite1366.name = "r_radiale_pt"
HAnimSite1366.DEF = "hanim_r_radiale_pt"
HAnimSite1366.translation = [-0.213,1.1305,-0.1091]
TouchSensor1367 = x3d.TouchSensor()
TouchSensor1367.description = "HAnimSite r_radiale_pt"

HAnimSite1366.children.append(TouchSensor1367)
Shape1368 = x3d.Shape()
Shape1368.USE = "HAnimSiteShape"

HAnimSite1366.children.append(Shape1368)

HAnimSegment1349.children.append(HAnimSite1366)

HAnimJoint1348.children.append(HAnimSegment1349)
HAnimJoint1369 = x3d.HAnimJoint()
HAnimJoint1369.name = "r_elbow"
HAnimJoint1369.DEF = "hanim_r_elbow"
HAnimJoint1369.center = [-0.1949,1.1388,-0.062]
HAnimJoint1369.ulimit = [0,0,0]
HAnimJoint1369.llimit = [0,0,0]
HAnimSegment1370 = x3d.HAnimSegment()
HAnimSegment1370.name = "r_forearm"
HAnimSegment1370.DEF = "hanim_r_forearm"
Transform1371 = x3d.Transform()
Transform1371.translation = [-0.1949,1.1388,-0.062]
Transform1372 = x3d.Transform()
#Empty Transform
Shape1373 = x3d.Shape()
Shape1373.USE = "HAnimJointShape"

Transform1372.children.append(Shape1373)

Transform1371.children.append(Transform1372)

HAnimSegment1370.children.append(Transform1371)
Shape1374 = x3d.Shape()
LineSet1375 = x3d.LineSet()
LineSet1375.vertexCount = [2]
Coordinate1376 = x3d.Coordinate()
Coordinate1376.point = (-0.1949,1.1388,-0.0620,-0.1959,0.8694,-0.0521)

LineSet1375.coord = Coordinate1376
#from r_elbow to r_radiocarpal vertices 2
ColorRGBA1377 = x3d.ColorRGBA()
ColorRGBA1377.USE = "HAnimSegmentLineColorRGBA"

LineSet1375.color = ColorRGBA1377

Shape1374.geometry = LineSet1375

HAnimSegment1370.children.append(Shape1374)
HAnimSite1378 = x3d.HAnimSite()
HAnimSite1378.name = "r_ulnar_styloid_pt"
HAnimSite1378.DEF = "hanim_r_ulnar_styloid_pt"
HAnimSite1378.translation = [-0.2117,0.8562,-0.0584]
TouchSensor1379 = x3d.TouchSensor()
TouchSensor1379.description = "HAnimSite r_ulnar_styloid_pt"

HAnimSite1378.children.append(TouchSensor1379)
Shape1380 = x3d.Shape()
Shape1380.USE = "HAnimSiteShape"

HAnimSite1378.children.append(Shape1380)

HAnimSegment1370.children.append(HAnimSite1378)

HAnimJoint1369.children.append(HAnimSegment1370)
HAnimJoint1381 = x3d.HAnimJoint()
HAnimJoint1381.name = "r_radiocarpal"
HAnimJoint1381.DEF = "hanim_r_radiocarpal"
HAnimJoint1381.center = [-0.1959,0.8694,-0.0521]
HAnimJoint1381.ulimit = [0,0,0]
HAnimJoint1381.llimit = [0,0,0]
HAnimSegment1382 = x3d.HAnimSegment()
HAnimSegment1382.name = "r_carpal"
HAnimSegment1382.DEF = "hanim_r_carpal"
Transform1383 = x3d.Transform()
Transform1383.scale = [0.2,0.2,0.2]
Transform1383.translation = [-0.2,0.85,-0.05]
Transform1383.rotation = [0,0,1,-3.14]
#Transform right hand
Transform1384 = x3d.Transform()
Transform1384.rotation = [0,1,0,1.57]
#Transform right hand
Shape1385 = x3d.Shape()
Shape1385.USE = "HAnimJointShape"

Transform1384.children.append(Shape1385)

Transform1383.children.append(Transform1384)

HAnimSegment1382.children.append(Transform1383)
Shape1386 = x3d.Shape()
LineSet1387 = x3d.LineSet()
LineSet1387.vertexCount = [2]
Coordinate1388 = x3d.Coordinate()
Coordinate1388.point = (-0.1959,0.8694,-0.0521,-0.1959,0.8694,-0.0521)

LineSet1387.coord = Coordinate1388
#from r_radiocarpal to r_midcarpal_1 vertices 2
ColorRGBA1389 = x3d.ColorRGBA()
ColorRGBA1389.USE = "HAnimSegmentLineColorRGBA"

LineSet1387.color = ColorRGBA1389

Shape1386.geometry = LineSet1387

HAnimSegment1382.children.append(Shape1386)
Shape1390 = x3d.Shape()
LineSet1391 = x3d.LineSet()
LineSet1391.vertexCount = [2]
Coordinate1392 = x3d.Coordinate()
Coordinate1392.point = (-0.1959,0.8694,-0.0521,-0.1959,0.8694,-0.0521)

LineSet1391.coord = Coordinate1392
#from r_radiocarpal to r_midcarpal_2 vertices 2
ColorRGBA1393 = x3d.ColorRGBA()
ColorRGBA1393.USE = "HAnimSegmentLineColorRGBA"

LineSet1391.color = ColorRGBA1393

Shape1390.geometry = LineSet1391

HAnimSegment1382.children.append(Shape1390)
Shape1394 = x3d.Shape()
LineSet1395 = x3d.LineSet()
LineSet1395.vertexCount = [2]
Coordinate1396 = x3d.Coordinate()
Coordinate1396.point = (-0.1959,0.8694,-0.0521,-0.1959,0.8694,-0.0521)

LineSet1395.coord = Coordinate1396
#from r_radiocarpal to r_midcarpal_3 vertices 2
ColorRGBA1397 = x3d.ColorRGBA()
ColorRGBA1397.USE = "HAnimSegmentLineColorRGBA"

LineSet1395.color = ColorRGBA1397

Shape1394.geometry = LineSet1395

HAnimSegment1382.children.append(Shape1394)
Shape1398 = x3d.Shape()
LineSet1399 = x3d.LineSet()
LineSet1399.vertexCount = [2]
Coordinate1400 = x3d.Coordinate()
Coordinate1400.point = (-0.1959,0.8694,-0.0521,-0.1959,0.8694,-0.0521)

LineSet1399.coord = Coordinate1400
#from r_radiocarpal to r_midcarpal_4_5 vertices 2
ColorRGBA1401 = x3d.ColorRGBA()
ColorRGBA1401.USE = "HAnimSegmentLineColorRGBA"

LineSet1399.color = ColorRGBA1401

Shape1398.geometry = LineSet1399

HAnimSegment1382.children.append(Shape1398)

HAnimJoint1381.children.append(HAnimSegment1382)
HAnimJoint1402 = x3d.HAnimJoint()
HAnimJoint1402.name = "r_midcarpal_1"
HAnimJoint1402.DEF = "hanim_r_midcarpal_1"
HAnimJoint1402.ulimit = [0,0,0]
HAnimJoint1402.llimit = [0,0,0]
HAnimSegment1403 = x3d.HAnimSegment()
HAnimSegment1403.name = "r_trapezium"
HAnimSegment1403.DEF = "hanim_r_trapezium"
Transform1404 = x3d.Transform()
Transform1404.translation = [-0.1959,0.8694,-0.0521]
Transform1405 = x3d.Transform()
#Empty Transform
Shape1406 = x3d.Shape()
Shape1406.USE = "HAnimJointShape"

Transform1405.children.append(Shape1406)

Transform1404.children.append(Transform1405)

HAnimSegment1403.children.append(Transform1404)
Shape1407 = x3d.Shape()
LineSet1408 = x3d.LineSet()
LineSet1408.vertexCount = [2]
Coordinate1409 = x3d.Coordinate()
Coordinate1409.point = (-0.1899,0.8502,-0.0473)

LineSet1408.coord = Coordinate1409
#from r_midcarpal_1 to r_carpometacarpal_1 vertices 1
ColorRGBA1410 = x3d.ColorRGBA()
ColorRGBA1410.USE = "HAnimSegmentLineColorRGBA"

LineSet1408.color = ColorRGBA1410

Shape1407.geometry = LineSet1408

HAnimSegment1403.children.append(Shape1407)

HAnimJoint1402.children.append(HAnimSegment1403)
HAnimJoint1411 = x3d.HAnimJoint()
HAnimJoint1411.name = "r_carpometacarpal_1"
HAnimJoint1411.DEF = "hanim_r_carpometacarpal_1"
HAnimJoint1411.center = [-0.1899,0.8502,-0.0473]
HAnimJoint1411.ulimit = [0,0,0]
HAnimJoint1411.llimit = [0,0,0]
HAnimSegment1412 = x3d.HAnimSegment()
HAnimSegment1412.name = "r_metacarpal_1"
HAnimSegment1412.DEF = "hanim_r_metacarpal_1"
Transform1413 = x3d.Transform()
Transform1413.translation = [-0.1899,0.8502,-0.0473]
Transform1414 = x3d.Transform()
#Empty Transform
Shape1415 = x3d.Shape()
Shape1415.USE = "HAnimJointShape"

Transform1414.children.append(Shape1415)

Transform1413.children.append(Transform1414)

HAnimSegment1412.children.append(Transform1413)
Shape1416 = x3d.Shape()
LineSet1417 = x3d.LineSet()
LineSet1417.vertexCount = [2]
Coordinate1418 = x3d.Coordinate()
Coordinate1418.point = (-0.1899,0.8502,-0.0473,-0.1874,0.8256,0.0306)

LineSet1417.coord = Coordinate1418
#from r_carpometacarpal_1 to r_metacarpophalangeal_1 vertices 2
ColorRGBA1419 = x3d.ColorRGBA()
ColorRGBA1419.USE = "HAnimSegmentLineColorRGBA"

LineSet1417.color = ColorRGBA1419

Shape1416.geometry = LineSet1417

HAnimSegment1412.children.append(Shape1416)

HAnimJoint1411.children.append(HAnimSegment1412)
HAnimJoint1420 = x3d.HAnimJoint()
HAnimJoint1420.name = "r_metacarpophalangeal_1"
HAnimJoint1420.DEF = "hanim_r_metacarpophalangeal_1"
HAnimJoint1420.center = [-0.1874,0.8256,0.0306]
HAnimJoint1420.ulimit = [0,0,0]
HAnimJoint1420.llimit = [0,0,0]
HAnimSegment1421 = x3d.HAnimSegment()
HAnimSegment1421.name = "r_carpal_proximal_phalanx_1"
HAnimSegment1421.DEF = "hanim_r_carpal_proximal_phalanx_1"
Transform1422 = x3d.Transform()
Transform1422.translation = [-0.1874,0.8256,0.0306]
Transform1423 = x3d.Transform()
#Empty Transform
Shape1424 = x3d.Shape()
Shape1424.USE = "HAnimJointShape"

Transform1423.children.append(Shape1424)

Transform1422.children.append(Transform1423)

HAnimSegment1421.children.append(Transform1422)
Shape1425 = x3d.Shape()
LineSet1426 = x3d.LineSet()
LineSet1426.vertexCount = [2]
Coordinate1427 = x3d.Coordinate()
Coordinate1427.point = (-0.1874,0.8256,0.0306,-0.1864,0.8190,0.0506)

LineSet1426.coord = Coordinate1427
#from r_metacarpophalangeal_1 to r_carpal_interphalangeal_1 vertices 2
ColorRGBA1428 = x3d.ColorRGBA()
ColorRGBA1428.USE = "HAnimSegmentLineColorRGBA"

LineSet1426.color = ColorRGBA1428

Shape1425.geometry = LineSet1426

HAnimSegment1421.children.append(Shape1425)
HAnimSite1429 = x3d.HAnimSite()
HAnimSite1429.name = "r_carpal_distal_phalanx_1_tip"
HAnimSite1429.DEF = "hanim_r_carpal_distal_phalanx_1_tip"
TouchSensor1430 = x3d.TouchSensor()
TouchSensor1430.description = "HAnimSite r_carpal_distal_phalanx_1_tip"

HAnimSite1429.children.append(TouchSensor1430)
Shape1431 = x3d.Shape()
Shape1431.USE = "HAnimSiteShape"

HAnimSite1429.children.append(Shape1431)

HAnimSegment1421.children.append(HAnimSite1429)

HAnimJoint1420.children.append(HAnimSegment1421)
HAnimJoint1432 = x3d.HAnimJoint()
HAnimJoint1432.name = "r_carpal_interphalangeal_1"
HAnimJoint1432.DEF = "hanim_r_carpal_interphalangeal_1"
HAnimJoint1432.center = [-0.1864,0.819,0.0506]
HAnimJoint1432.ulimit = [0,0,0]
HAnimJoint1432.llimit = [0,0,0]

HAnimJoint1420.children.append(HAnimJoint1432)

HAnimJoint1411.children.append(HAnimJoint1420)

HAnimJoint1402.children.append(HAnimJoint1411)

HAnimJoint1381.children.append(HAnimJoint1402)
HAnimJoint1433 = x3d.HAnimJoint()
HAnimJoint1433.name = "r_midcarpal_2"
HAnimJoint1433.DEF = "hanim_r_midcarpal_2"
HAnimJoint1433.ulimit = [0,0,0]
HAnimJoint1433.llimit = [0,0,0]
HAnimSegment1434 = x3d.HAnimSegment()
HAnimSegment1434.name = "r_trapezoid"
HAnimSegment1434.DEF = "hanim_r_trapezoid"
Transform1435 = x3d.Transform()
Transform1435.translation = [-0.1864,0.819,0.0506]
Transform1436 = x3d.Transform()
#Empty Transform
Shape1437 = x3d.Shape()
Shape1437.USE = "HAnimJointShape"

Transform1436.children.append(Shape1437)

Transform1435.children.append(Transform1436)

HAnimSegment1434.children.append(Transform1435)
Shape1438 = x3d.Shape()
LineSet1439 = x3d.LineSet()
LineSet1439.vertexCount = [2]
Coordinate1440 = x3d.Coordinate()
Coordinate1440.point = (-0.1961,0.8055,-0.0218)

LineSet1439.coord = Coordinate1440
#from r_midcarpal_2 to r_carpometacarpal_2 vertices 1
ColorRGBA1441 = x3d.ColorRGBA()
ColorRGBA1441.USE = "HAnimSegmentLineColorRGBA"

LineSet1439.color = ColorRGBA1441

Shape1438.geometry = LineSet1439

HAnimSegment1434.children.append(Shape1438)
HAnimSite1442 = x3d.HAnimSite()
HAnimSite1442.name = "r_metacarpal_phalanx_2_pt"
HAnimSite1442.DEF = "hanim_r_metacarpal_phalanx_2_pt"
HAnimSite1442.translation = [-0.1977,0.8169,-0.0177]
TouchSensor1443 = x3d.TouchSensor()
TouchSensor1443.description = "HAnimSite r_metacarpal_phalanx_2_pt"

HAnimSite1442.children.append(TouchSensor1443)
Shape1444 = x3d.Shape()
Shape1444.USE = "HAnimSiteShape"

HAnimSite1442.children.append(Shape1444)

HAnimSegment1434.children.append(HAnimSite1442)

HAnimJoint1433.children.append(HAnimSegment1434)
HAnimJoint1445 = x3d.HAnimJoint()
HAnimJoint1445.name = "r_carpometacarpal_2"
HAnimJoint1445.DEF = "hanim_r_carpometacarpal_2"
HAnimJoint1445.center = [-0.1961,0.8055,-0.0218]
HAnimJoint1445.ulimit = [0,0,0]
HAnimJoint1445.llimit = [0,0,0]
HAnimSegment1446 = x3d.HAnimSegment()
HAnimSegment1446.name = "r_metacarpal_2"
HAnimSegment1446.DEF = "hanim_r_metacarpal_2"
Transform1447 = x3d.Transform()
Transform1447.translation = [-0.1961,0.8055,-0.0218]
Transform1448 = x3d.Transform()
#Empty Transform
Shape1449 = x3d.Shape()
Shape1449.USE = "HAnimJointShape"

Transform1448.children.append(Shape1449)

Transform1447.children.append(Transform1448)

HAnimSegment1446.children.append(Transform1447)
Shape1450 = x3d.Shape()
LineSet1451 = x3d.LineSet()
LineSet1451.vertexCount = [2]
Coordinate1452 = x3d.Coordinate()
Coordinate1452.point = (-0.1961,0.8055,-0.0218,-0.1961,0.7846,-0.0218)

LineSet1451.coord = Coordinate1452
#from r_carpometacarpal_2 to r_metacarpophalangeal_2 vertices 2
ColorRGBA1453 = x3d.ColorRGBA()
ColorRGBA1453.USE = "HAnimSegmentLineColorRGBA"

LineSet1451.color = ColorRGBA1453

Shape1450.geometry = LineSet1451

HAnimSegment1446.children.append(Shape1450)

HAnimJoint1445.children.append(HAnimSegment1446)
HAnimJoint1454 = x3d.HAnimJoint()
HAnimJoint1454.name = "r_metacarpophalangeal_2"
HAnimJoint1454.DEF = "hanim_r_metacarpophalangeal_2"
HAnimJoint1454.center = [-0.1961,0.7846,-0.0218]
HAnimJoint1454.ulimit = [0,0,0]
HAnimJoint1454.llimit = [0,0,0]
HAnimSegment1455 = x3d.HAnimSegment()
HAnimSegment1455.name = "r_carpal_proximal_phalanx_2"
HAnimSegment1455.DEF = "hanim_r_carpal_proximal_phalanx_2"
Transform1456 = x3d.Transform()
Transform1456.translation = [-0.1961,0.7846,-0.0218]
Transform1457 = x3d.Transform()
#Empty Transform
Shape1458 = x3d.Shape()
Shape1458.USE = "HAnimJointShape"

Transform1457.children.append(Shape1458)

Transform1456.children.append(Transform1457)

HAnimSegment1455.children.append(Transform1456)
Shape1459 = x3d.Shape()
LineSet1460 = x3d.LineSet()
LineSet1460.vertexCount = [2]
Coordinate1461 = x3d.Coordinate()
Coordinate1461.point = (-0.1961,0.7846,-0.0218,-0.1954,0.7393,-0.0185)

LineSet1460.coord = Coordinate1461
#from r_metacarpophalangeal_2 to r_carpal_proximal_interphalangeal_2 vertices 2
ColorRGBA1462 = x3d.ColorRGBA()
ColorRGBA1462.USE = "HAnimSegmentLineColorRGBA"

LineSet1460.color = ColorRGBA1462

Shape1459.geometry = LineSet1460

HAnimSegment1455.children.append(Shape1459)

HAnimJoint1454.children.append(HAnimSegment1455)
HAnimJoint1463 = x3d.HAnimJoint()
HAnimJoint1463.name = "r_carpal_proximal_interphalangeal_2"
HAnimJoint1463.DEF = "hanim_r_carpal_proximal_interphalangeal_2"
HAnimJoint1463.center = [-0.1954,0.7393,-0.0185]
HAnimJoint1463.ulimit = [0,0,0]
HAnimJoint1463.llimit = [0,0,0]
HAnimSegment1464 = x3d.HAnimSegment()
HAnimSegment1464.name = "r_carpal_middle_phalanx_2"
HAnimSegment1464.DEF = "hanim_r_carpal_middle_phalanx_2"
Transform1465 = x3d.Transform()
Transform1465.translation = [-0.1954,0.7393,-0.0185]
Transform1466 = x3d.Transform()
#Empty Transform
Shape1467 = x3d.Shape()
Shape1467.USE = "HAnimJointShape"

Transform1466.children.append(Shape1467)

Transform1465.children.append(Transform1466)

HAnimSegment1464.children.append(Transform1465)
Shape1468 = x3d.Shape()
LineSet1469 = x3d.LineSet()
LineSet1469.vertexCount = [2]
Coordinate1470 = x3d.Coordinate()
Coordinate1470.point = (-0.1954,0.7393,-0.0185,-0.1945,0.7169,-0.0173)

LineSet1469.coord = Coordinate1470
#from r_carpal_proximal_interphalangeal_2 to r_carpal_distal_interphalangeal_2 vertices 2
ColorRGBA1471 = x3d.ColorRGBA()
ColorRGBA1471.USE = "HAnimSegmentLineColorRGBA"

LineSet1469.color = ColorRGBA1471

Shape1468.geometry = LineSet1469

HAnimSegment1464.children.append(Shape1468)
HAnimSite1472 = x3d.HAnimSite()
HAnimSite1472.name = "r_carpal_distal_phalanx_2_tip"
HAnimSite1472.DEF = "hanim_r_carpal_distal_phalanx_2_tip"
TouchSensor1473 = x3d.TouchSensor()
TouchSensor1473.description = "HAnimSite r_carpal_distal_phalanx_2_tip"

HAnimSite1472.children.append(TouchSensor1473)
Shape1474 = x3d.Shape()
Shape1474.USE = "HAnimSiteShape"

HAnimSite1472.children.append(Shape1474)

HAnimSegment1464.children.append(HAnimSite1472)
HAnimSite1475 = x3d.HAnimSite()
HAnimSite1475.name = "r_dactylion_pt"
HAnimSite1475.DEF = "hanim_r_dactylion_pt"
HAnimSite1475.translation = [-0.1941,0.6772,-0.0423]
TouchSensor1476 = x3d.TouchSensor()
TouchSensor1476.description = "HAnimSite r_dactylion_pt"

HAnimSite1475.children.append(TouchSensor1476)
Shape1477 = x3d.Shape()
Shape1477.USE = "HAnimSiteShape"

HAnimSite1475.children.append(Shape1477)

HAnimSegment1464.children.append(HAnimSite1475)

HAnimJoint1463.children.append(HAnimSegment1464)
HAnimJoint1478 = x3d.HAnimJoint()
HAnimJoint1478.name = "r_carpal_distal_interphalangeal_2"
HAnimJoint1478.DEF = "hanim_r_carpal_distal_interphalangeal_2"
HAnimJoint1478.center = [-0.1945,0.7169,-0.0173]
HAnimJoint1478.ulimit = [0,0,0]
HAnimJoint1478.llimit = [0,0,0]

HAnimJoint1463.children.append(HAnimJoint1478)

HAnimJoint1454.children.append(HAnimJoint1463)

HAnimJoint1445.children.append(HAnimJoint1454)

HAnimJoint1433.children.append(HAnimJoint1445)

HAnimJoint1381.children.append(HAnimJoint1433)
HAnimJoint1479 = x3d.HAnimJoint()
HAnimJoint1479.name = "r_midcarpal_3"
HAnimJoint1479.DEF = "hanim_r_midcarpal_3"
HAnimJoint1479.ulimit = [0,0,0]
HAnimJoint1479.llimit = [0,0,0]
HAnimSegment1480 = x3d.HAnimSegment()
HAnimSegment1480.name = "r_capitate"
HAnimSegment1480.DEF = "hanim_r_capitate"
Transform1481 = x3d.Transform()
Transform1481.translation = [-0.1945,0.7169,-0.0173]
Transform1482 = x3d.Transform()
#Empty Transform
Shape1483 = x3d.Shape()
Shape1483.USE = "HAnimJointShape"

Transform1482.children.append(Shape1483)

Transform1481.children.append(Transform1482)

HAnimSegment1480.children.append(Transform1481)
Shape1484 = x3d.Shape()
LineSet1485 = x3d.LineSet()
LineSet1485.vertexCount = [2]
Coordinate1486 = x3d.Coordinate()
Coordinate1486.point = (-0.1972,0.8060,-0.0468)

LineSet1485.coord = Coordinate1486
#from r_midcarpal_3 to r_carpometacarpal_3 vertices 1
ColorRGBA1487 = x3d.ColorRGBA()
ColorRGBA1487.USE = "HAnimSegmentLineColorRGBA"

LineSet1485.color = ColorRGBA1487

Shape1484.geometry = LineSet1485

HAnimSegment1480.children.append(Shape1484)
HAnimSite1488 = x3d.HAnimSite()
HAnimSite1488.name = "r_metacarpal_phalanx_3_pt"
HAnimSite1488.DEF = "hanim_r_metacarpal_phalanx_3_pt"
TouchSensor1489 = x3d.TouchSensor()
TouchSensor1489.description = "HAnimSite r_metacarpal_phalanx_3_pt"

HAnimSite1488.children.append(TouchSensor1489)
Shape1490 = x3d.Shape()
Shape1490.USE = "HAnimSiteShape"

HAnimSite1488.children.append(Shape1490)

HAnimSegment1480.children.append(HAnimSite1488)

HAnimJoint1479.children.append(HAnimSegment1480)
HAnimJoint1491 = x3d.HAnimJoint()
HAnimJoint1491.name = "r_carpometacarpal_3"
HAnimJoint1491.DEF = "hanim_r_carpometacarpal_3"
HAnimJoint1491.center = [-0.1972,0.806,-0.0468]
HAnimJoint1491.ulimit = [0,0,0]
HAnimJoint1491.llimit = [0,0,0]
HAnimSegment1492 = x3d.HAnimSegment()
HAnimSegment1492.name = "r_metacarpal_3"
HAnimSegment1492.DEF = "hanim_r_metacarpal_3"
Transform1493 = x3d.Transform()
Transform1493.translation = [-0.1972,0.806,-0.0468]
Transform1494 = x3d.Transform()
#Empty Transform
Shape1495 = x3d.Shape()
Shape1495.USE = "HAnimJointShape"

Transform1494.children.append(Shape1495)

Transform1493.children.append(Transform1494)

HAnimSegment1492.children.append(Transform1493)
Shape1496 = x3d.Shape()
LineSet1497 = x3d.LineSet()
LineSet1497.vertexCount = [2]
Coordinate1498 = x3d.Coordinate()
Coordinate1498.point = (-0.1972,0.8060,-0.0468,-0.1972,0.7849,-0.0468)

LineSet1497.coord = Coordinate1498
#from r_carpometacarpal_3 to r_metacarpophalangeal_3 vertices 2
ColorRGBA1499 = x3d.ColorRGBA()
ColorRGBA1499.USE = "HAnimSegmentLineColorRGBA"

LineSet1497.color = ColorRGBA1499

Shape1496.geometry = LineSet1497

HAnimSegment1492.children.append(Shape1496)

HAnimJoint1491.children.append(HAnimSegment1492)
HAnimJoint1500 = x3d.HAnimJoint()
HAnimJoint1500.name = "r_metacarpophalangeal_3"
HAnimJoint1500.DEF = "hanim_r_metacarpophalangeal_3"
HAnimJoint1500.center = [-0.1972,0.7849,-0.0468]
HAnimJoint1500.ulimit = [0,0,0]
HAnimJoint1500.llimit = [0,0,0]
HAnimSegment1501 = x3d.HAnimSegment()
HAnimSegment1501.name = "r_carpal_proximal_phalanx_3"
HAnimSegment1501.DEF = "hanim_r_carpal_proximal_phalanx_3"
Transform1502 = x3d.Transform()
Transform1502.translation = [-0.1972,0.7849,-0.0468]
Transform1503 = x3d.Transform()
#Empty Transform
Shape1504 = x3d.Shape()
Shape1504.USE = "HAnimJointShape"

Transform1503.children.append(Shape1504)

Transform1502.children.append(Transform1503)

HAnimSegment1501.children.append(Transform1502)
Shape1505 = x3d.Shape()
LineSet1506 = x3d.LineSet()
LineSet1506.vertexCount = [2]
Coordinate1507 = x3d.Coordinate()
Coordinate1507.point = (-0.1972,0.7849,-0.0468,-0.1950,0.7304,-0.0441)

LineSet1506.coord = Coordinate1507
#from r_metacarpophalangeal_3 to r_carpal_proximal_interphalangeal_3 vertices 2
ColorRGBA1508 = x3d.ColorRGBA()
ColorRGBA1508.USE = "HAnimSegmentLineColorRGBA"

LineSet1506.color = ColorRGBA1508

Shape1505.geometry = LineSet1506

HAnimSegment1501.children.append(Shape1505)

HAnimJoint1500.children.append(HAnimSegment1501)
HAnimJoint1509 = x3d.HAnimJoint()
HAnimJoint1509.name = "r_carpal_proximal_interphalangeal_3"
HAnimJoint1509.DEF = "hanim_r_carpal_proximal_interphalangeal_3"
HAnimJoint1509.center = [-0.195,0.7304,-0.0441]
HAnimJoint1509.ulimit = [0,0,0]
HAnimJoint1509.llimit = [0,0,0]
HAnimSegment1510 = x3d.HAnimSegment()
HAnimSegment1510.name = "r_carpal_middle_phalanx_3"
HAnimSegment1510.DEF = "hanim_r_carpal_middle_phalanx_3"
Transform1511 = x3d.Transform()
Transform1511.translation = [-0.195,0.7304,-0.0441]
Transform1512 = x3d.Transform()
#Empty Transform
Shape1513 = x3d.Shape()
Shape1513.USE = "HAnimJointShape"

Transform1512.children.append(Shape1513)

Transform1511.children.append(Transform1512)

HAnimSegment1510.children.append(Transform1511)
Shape1514 = x3d.Shape()
LineSet1515 = x3d.LineSet()
LineSet1515.vertexCount = [2]
Coordinate1516 = x3d.Coordinate()
Coordinate1516.point = (-0.1950,0.7304,-0.0441,-0.1939,0.7042,-0.0432)

LineSet1515.coord = Coordinate1516
#from r_carpal_proximal_interphalangeal_3 to r_carpal_distal_interphalangeal_3 vertices 2
ColorRGBA1517 = x3d.ColorRGBA()
ColorRGBA1517.USE = "HAnimSegmentLineColorRGBA"

LineSet1515.color = ColorRGBA1517

Shape1514.geometry = LineSet1515

HAnimSegment1510.children.append(Shape1514)
HAnimSite1518 = x3d.HAnimSite()
HAnimSite1518.name = "r_carpal_distal_phalanx_3_tip"
HAnimSite1518.DEF = "hanim_r_carpal_distal_phalanx_3_tip"
TouchSensor1519 = x3d.TouchSensor()
TouchSensor1519.description = "HAnimSite r_carpal_distal_phalanx_3_tip"

HAnimSite1518.children.append(TouchSensor1519)
Shape1520 = x3d.Shape()
Shape1520.USE = "HAnimSiteShape"

HAnimSite1518.children.append(Shape1520)

HAnimSegment1510.children.append(HAnimSite1518)

HAnimJoint1509.children.append(HAnimSegment1510)
HAnimJoint1521 = x3d.HAnimJoint()
HAnimJoint1521.name = "r_carpal_distal_interphalangeal_3"
HAnimJoint1521.DEF = "hanim_r_carpal_distal_interphalangeal_3"
HAnimJoint1521.center = [-0.1939,0.7042,-0.0432]
HAnimJoint1521.ulimit = [0,0,0]
HAnimJoint1521.llimit = [0,0,0]

HAnimJoint1509.children.append(HAnimJoint1521)

HAnimJoint1500.children.append(HAnimJoint1509)

HAnimJoint1491.children.append(HAnimJoint1500)

HAnimJoint1479.children.append(HAnimJoint1491)

HAnimJoint1381.children.append(HAnimJoint1479)
HAnimJoint1522 = x3d.HAnimJoint()
HAnimJoint1522.name = "r_midcarpal_4_5"
HAnimJoint1522.DEF = "hanim_r_midcarpal_4_5"
HAnimJoint1522.ulimit = [0,0,0]
HAnimJoint1522.llimit = [0,0,0]
HAnimSegment1523 = x3d.HAnimSegment()
HAnimSegment1523.name = "r_hamate"
HAnimSegment1523.DEF = "hanim_r_hamate"
Transform1524 = x3d.Transform()
Transform1524.translation = [-0.1939,0.7042,-0.0432]
Transform1525 = x3d.Transform()
#Empty Transform
Shape1526 = x3d.Shape()
Shape1526.USE = "HAnimJointShape"

Transform1525.children.append(Shape1526)

Transform1524.children.append(Transform1525)

HAnimSegment1523.children.append(Transform1524)
Shape1527 = x3d.Shape()
LineSet1528 = x3d.LineSet()
LineSet1528.vertexCount = [2]
Coordinate1529 = x3d.Coordinate()
Coordinate1529.point = (-0.1951,0.8049,-0.0732)

LineSet1528.coord = Coordinate1529
#from r_midcarpal_4_5 to r_carpometacarpal_4 vertices 1
ColorRGBA1530 = x3d.ColorRGBA()
ColorRGBA1530.USE = "HAnimSegmentLineColorRGBA"

LineSet1528.color = ColorRGBA1530

Shape1527.geometry = LineSet1528

HAnimSegment1523.children.append(Shape1527)
Shape1531 = x3d.Shape()
LineSet1532 = x3d.LineSet()
LineSet1532.vertexCount = [2]
Coordinate1533 = x3d.Coordinate()
Coordinate1533.point = (-0.1926,0.8096,-0.0975)

LineSet1532.coord = Coordinate1533
#from r_midcarpal_4_5 to r_carpometacarpal_5 vertices 1
ColorRGBA1534 = x3d.ColorRGBA()
ColorRGBA1534.USE = "HAnimSegmentLineColorRGBA"

LineSet1532.color = ColorRGBA1534

Shape1531.geometry = LineSet1532

HAnimSegment1523.children.append(Shape1531)
HAnimSite1535 = x3d.HAnimSite()
HAnimSite1535.name = "r_metacarpal_phalanx_5_pt"
HAnimSite1535.DEF = "hanim_r_metacarpal_phalanx_5_pt"
HAnimSite1535.translation = [-0.1929,0.789,-0.1064]
TouchSensor1536 = x3d.TouchSensor()
TouchSensor1536.description = "HAnimSite r_metacarpal_phalanx_5_pt"

HAnimSite1535.children.append(TouchSensor1536)
Shape1537 = x3d.Shape()
Shape1537.USE = "HAnimSiteShape"

HAnimSite1535.children.append(Shape1537)

HAnimSegment1523.children.append(HAnimSite1535)

HAnimJoint1522.children.append(HAnimSegment1523)
HAnimJoint1538 = x3d.HAnimJoint()
HAnimJoint1538.name = "r_carpometacarpal_4"
HAnimJoint1538.DEF = "hanim_r_carpometacarpal_4"
HAnimJoint1538.center = [-0.1951,0.8049,-0.0732]
HAnimJoint1538.ulimit = [0,0,0]
HAnimJoint1538.llimit = [0,0,0]
HAnimSegment1539 = x3d.HAnimSegment()
HAnimSegment1539.name = "r_metacarpal_4"
HAnimSegment1539.DEF = "hanim_r_metacarpal_4"
Transform1540 = x3d.Transform()
Transform1540.translation = [-0.1951,0.8049,-0.0732]
Transform1541 = x3d.Transform()
#Empty Transform
Shape1542 = x3d.Shape()
Shape1542.USE = "HAnimJointShape"

Transform1541.children.append(Shape1542)

Transform1540.children.append(Transform1541)

HAnimSegment1539.children.append(Transform1540)
Shape1543 = x3d.Shape()
LineSet1544 = x3d.LineSet()
LineSet1544.vertexCount = [2]
Coordinate1545 = x3d.Coordinate()
Coordinate1545.point = (-0.1951,0.8049,-0.0732,-0.1951,0.7845,-0.0732)

LineSet1544.coord = Coordinate1545
#from r_carpometacarpal_4 to r_metacarpophalangeal_4 vertices 2
ColorRGBA1546 = x3d.ColorRGBA()
ColorRGBA1546.USE = "HAnimSegmentLineColorRGBA"

LineSet1544.color = ColorRGBA1546

Shape1543.geometry = LineSet1544

HAnimSegment1539.children.append(Shape1543)

HAnimJoint1538.children.append(HAnimSegment1539)
HAnimJoint1547 = x3d.HAnimJoint()
HAnimJoint1547.name = "r_metacarpophalangeal_4"
HAnimJoint1547.DEF = "hanim_r_metacarpophalangeal_4"
HAnimJoint1547.center = [-0.1951,0.7845,-0.0732]
HAnimJoint1547.ulimit = [0,0,0]
HAnimJoint1547.llimit = [0,0,0]
HAnimSegment1548 = x3d.HAnimSegment()
HAnimSegment1548.name = "r_carpal_proximal_phalanx_4"
HAnimSegment1548.DEF = "hanim_r_carpal_proximal_phalanx_4"
Transform1549 = x3d.Transform()
Transform1549.translation = [-0.1951,0.7845,-0.0732]
Transform1550 = x3d.Transform()
#Empty Transform
Shape1551 = x3d.Shape()
Shape1551.USE = "HAnimJointShape"

Transform1550.children.append(Shape1551)

Transform1549.children.append(Transform1550)

HAnimSegment1548.children.append(Transform1549)
Shape1552 = x3d.Shape()
LineSet1553 = x3d.LineSet()
LineSet1553.vertexCount = [2]
Coordinate1554 = x3d.Coordinate()
Coordinate1554.point = (-0.1951,0.7845,-0.0732,-0.1920,0.7318,-0.0716)

LineSet1553.coord = Coordinate1554
#from r_metacarpophalangeal_4 to r_carpal_proximal_interphalangeal_4 vertices 2
ColorRGBA1555 = x3d.ColorRGBA()
ColorRGBA1555.USE = "HAnimSegmentLineColorRGBA"

LineSet1553.color = ColorRGBA1555

Shape1552.geometry = LineSet1553

HAnimSegment1548.children.append(Shape1552)

HAnimJoint1547.children.append(HAnimSegment1548)
HAnimJoint1556 = x3d.HAnimJoint()
HAnimJoint1556.name = "r_carpal_proximal_interphalangeal_4"
HAnimJoint1556.DEF = "hanim_r_carpal_proximal_interphalangeal_4"
HAnimJoint1556.center = [-0.192,0.7318,-0.0716]
HAnimJoint1556.ulimit = [0,0,0]
HAnimJoint1556.llimit = [0,0,0]
HAnimSegment1557 = x3d.HAnimSegment()
HAnimSegment1557.name = "r_carpal_middle_phalanx_4"
HAnimSegment1557.DEF = "hanim_r_carpal_middle_phalanx_4"
Transform1558 = x3d.Transform()
Transform1558.translation = [-0.192,0.7318,-0.0716]
Transform1559 = x3d.Transform()
#Empty Transform
Shape1560 = x3d.Shape()
Shape1560.USE = "HAnimJointShape"

Transform1559.children.append(Shape1560)

Transform1558.children.append(Transform1559)

HAnimSegment1557.children.append(Transform1558)
Shape1561 = x3d.Shape()
LineSet1562 = x3d.LineSet()
LineSet1562.vertexCount = [2]
Coordinate1563 = x3d.Coordinate()
Coordinate1563.point = (-0.1920,0.7318,-0.0716,-0.1908,0.7077,-0.0706)

LineSet1562.coord = Coordinate1563
#from r_carpal_proximal_interphalangeal_4 to r_carpal_distal_interphalangeal_4 vertices 2
ColorRGBA1564 = x3d.ColorRGBA()
ColorRGBA1564.USE = "HAnimSegmentLineColorRGBA"

LineSet1562.color = ColorRGBA1564

Shape1561.geometry = LineSet1562

HAnimSegment1557.children.append(Shape1561)
HAnimSite1565 = x3d.HAnimSite()
HAnimSite1565.name = "r_carpal_distal_phalanx_4_tip"
HAnimSite1565.DEF = "hanim_r_carpal_distal_phalanx_4_tip"
TouchSensor1566 = x3d.TouchSensor()
TouchSensor1566.description = "HAnimSite r_carpal_distal_phalanx_4_tip"

HAnimSite1565.children.append(TouchSensor1566)
Shape1567 = x3d.Shape()
Shape1567.USE = "HAnimSiteShape"

HAnimSite1565.children.append(Shape1567)

HAnimSegment1557.children.append(HAnimSite1565)

HAnimJoint1556.children.append(HAnimSegment1557)
HAnimJoint1568 = x3d.HAnimJoint()
HAnimJoint1568.name = "r_carpal_distal_interphalangeal_4"
HAnimJoint1568.DEF = "hanim_r_carpal_distal_interphalangeal_4"
HAnimJoint1568.center = [-0.1908,0.7077,-0.0706]
HAnimJoint1568.ulimit = [0,0,0]
HAnimJoint1568.llimit = [0,0,0]

HAnimJoint1556.children.append(HAnimJoint1568)

HAnimJoint1547.children.append(HAnimJoint1556)

HAnimJoint1538.children.append(HAnimJoint1547)

HAnimJoint1522.children.append(HAnimJoint1538)
HAnimJoint1569 = x3d.HAnimJoint()
HAnimJoint1569.name = "r_carpometacarpal_5"
HAnimJoint1569.DEF = "hanim_r_carpometacarpal_5"
HAnimJoint1569.center = [-0.1926,0.8096,-0.0975]
HAnimJoint1569.ulimit = [0,0,0]
HAnimJoint1569.llimit = [0,0,0]
HAnimSegment1570 = x3d.HAnimSegment()
HAnimSegment1570.name = "r_metacarpal_5"
HAnimSegment1570.DEF = "hanim_r_metacarpal_5"
Transform1571 = x3d.Transform()
Transform1571.translation = [-0.1926,0.8096,-0.0975]
Transform1572 = x3d.Transform()
#Empty Transform
Shape1573 = x3d.Shape()
Shape1573.USE = "HAnimJointShape"

Transform1572.children.append(Shape1573)

Transform1571.children.append(Transform1572)

HAnimSegment1570.children.append(Transform1571)
Shape1574 = x3d.Shape()
LineSet1575 = x3d.LineSet()
LineSet1575.vertexCount = [2]
Coordinate1576 = x3d.Coordinate()
Coordinate1576.point = (-0.1926,0.8096,-0.0975,-0.1926,0.7896,-0.0975)

LineSet1575.coord = Coordinate1576
#from r_carpometacarpal_5 to r_metacarpophalangeal_5 vertices 2
ColorRGBA1577 = x3d.ColorRGBA()
ColorRGBA1577.USE = "HAnimSegmentLineColorRGBA"

LineSet1575.color = ColorRGBA1577

Shape1574.geometry = LineSet1575

HAnimSegment1570.children.append(Shape1574)

HAnimJoint1569.children.append(HAnimSegment1570)
HAnimJoint1578 = x3d.HAnimJoint()
HAnimJoint1578.name = "r_metacarpophalangeal_5"
HAnimJoint1578.DEF = "hanim_r_metacarpophalangeal_5"
HAnimJoint1578.center = [-0.1926,0.7896,-0.0975]
HAnimJoint1578.ulimit = [0,0,0]
HAnimJoint1578.llimit = [0,0,0]
HAnimSegment1579 = x3d.HAnimSegment()
HAnimSegment1579.name = "r_carpal_proximal_phalanx_5"
HAnimSegment1579.DEF = "hanim_r_carpal_proximal_phalanx_5"
Transform1580 = x3d.Transform()
Transform1580.translation = [-0.1926,0.7896,-0.0975]
Transform1581 = x3d.Transform()
#Empty Transform
Shape1582 = x3d.Shape()
Shape1582.USE = "HAnimJointShape"

Transform1581.children.append(Shape1582)

Transform1580.children.append(Transform1581)

HAnimSegment1579.children.append(Transform1580)
Shape1583 = x3d.Shape()
LineSet1584 = x3d.LineSet()
LineSet1584.vertexCount = [2]
Coordinate1585 = x3d.Coordinate()
Coordinate1585.point = (-0.1926,0.7896,-0.0975,-0.1902,0.7483,-0.0963)

LineSet1584.coord = Coordinate1585
#from r_metacarpophalangeal_5 to r_carpal_proximal_interphalangeal_5 vertices 2
ColorRGBA1586 = x3d.ColorRGBA()
ColorRGBA1586.USE = "HAnimSegmentLineColorRGBA"

LineSet1584.color = ColorRGBA1586

Shape1583.geometry = LineSet1584

HAnimSegment1579.children.append(Shape1583)

HAnimJoint1578.children.append(HAnimSegment1579)
HAnimJoint1587 = x3d.HAnimJoint()
HAnimJoint1587.name = "r_carpal_proximal_interphalangeal_5"
HAnimJoint1587.DEF = "hanim_r_carpal_proximal_interphalangeal_5"
HAnimJoint1587.center = [-0.1902,0.7483,-0.0963]
HAnimJoint1587.ulimit = [0,0,0]
HAnimJoint1587.llimit = [0,0,0]
HAnimSegment1588 = x3d.HAnimSegment()
HAnimSegment1588.name = "r_carpal_middle_phalanx_5"
HAnimSegment1588.DEF = "hanim_r_carpal_middle_phalanx_5"
Transform1589 = x3d.Transform()
Transform1589.translation = [-0.1902,0.7483,-0.0963]
Transform1590 = x3d.Transform()
#Empty Transform
Shape1591 = x3d.Shape()
Shape1591.USE = "HAnimJointShape"

Transform1590.children.append(Shape1591)

Transform1589.children.append(Transform1590)

HAnimSegment1588.children.append(Transform1589)
Shape1592 = x3d.Shape()
LineSet1593 = x3d.LineSet()
LineSet1593.vertexCount = [2]
Coordinate1594 = x3d.Coordinate()
Coordinate1594.point = (-0.1902,0.7483,-0.0963,-0.1908,0.7540,-0.0960)

LineSet1593.coord = Coordinate1594
#from r_carpal_proximal_interphalangeal_5 to r_carpal_distal_interphalangeal_5 vertices 2
ColorRGBA1595 = x3d.ColorRGBA()
ColorRGBA1595.USE = "HAnimSegmentLineColorRGBA"

LineSet1593.color = ColorRGBA1595

Shape1592.geometry = LineSet1593

HAnimSegment1588.children.append(Shape1592)
HAnimSite1596 = x3d.HAnimSite()
HAnimSite1596.name = "r_carpal_distal_phalanx_5_tip"
HAnimSite1596.DEF = "hanim_r_carpal_distal_phalanx_5_tip"
TouchSensor1597 = x3d.TouchSensor()
TouchSensor1597.description = "HAnimSite r_carpal_distal_phalanx_5_tip"

HAnimSite1596.children.append(TouchSensor1597)
Shape1598 = x3d.Shape()
Shape1598.USE = "HAnimSiteShape"

HAnimSite1596.children.append(Shape1598)

HAnimSegment1588.children.append(HAnimSite1596)

HAnimJoint1587.children.append(HAnimSegment1588)
HAnimJoint1599 = x3d.HAnimJoint()
HAnimJoint1599.name = "r_carpal_distal_interphalangeal_5"
HAnimJoint1599.DEF = "hanim_r_carpal_distal_interphalangeal_5"
HAnimJoint1599.center = [-0.1908,0.754,-0.096]
HAnimJoint1599.ulimit = [0,0,0]
HAnimJoint1599.llimit = [0,0,0]

HAnimJoint1587.children.append(HAnimJoint1599)

HAnimJoint1578.children.append(HAnimJoint1587)

HAnimJoint1569.children.append(HAnimJoint1578)

HAnimJoint1522.children.append(HAnimJoint1569)

HAnimJoint1381.children.append(HAnimJoint1522)

HAnimJoint1369.children.append(HAnimJoint1381)

HAnimJoint1348.children.append(HAnimJoint1369)

HAnimJoint1333.children.append(HAnimJoint1348)

HAnimJoint1324.children.append(HAnimJoint1333)

HAnimJoint844.children.append(HAnimJoint1324)

HAnimJoint829.children.append(HAnimJoint844)

HAnimJoint820.children.append(HAnimJoint829)

HAnimJoint811.children.append(HAnimJoint820)

HAnimJoint802.children.append(HAnimJoint811)

HAnimJoint790.children.append(HAnimJoint802)

HAnimJoint769.children.append(HAnimJoint790)

HAnimJoint760.children.append(HAnimJoint769)

HAnimJoint751.children.append(HAnimJoint760)

HAnimJoint736.children.append(HAnimJoint751)

HAnimJoint724.children.append(HAnimJoint736)

HAnimJoint715.children.append(HAnimJoint724)

HAnimJoint706.children.append(HAnimJoint715)

HAnimJoint697.children.append(HAnimJoint706)

HAnimJoint679.children.append(HAnimJoint697)

HAnimJoint670.children.append(HAnimJoint679)

HAnimJoint661.children.append(HAnimJoint670)

HAnimJoint44.children.append(HAnimJoint661)

HAnimHumanoid43.skeleton.append(HAnimJoint44)
HAnimJoint1600 = x3d.HAnimJoint()
HAnimJoint1600.USE = "hanim_humanoid_root"

HAnimHumanoid43.joints.append(HAnimJoint1600)
HAnimJoint1601 = x3d.HAnimJoint()
HAnimJoint1601.USE = "hanim_sacroiliac"

HAnimHumanoid43.joints.append(HAnimJoint1601)
HAnimJoint1602 = x3d.HAnimJoint()
HAnimJoint1602.USE = "hanim_l_hip"

HAnimHumanoid43.joints.append(HAnimJoint1602)
HAnimJoint1603 = x3d.HAnimJoint()
HAnimJoint1603.USE = "hanim_l_knee"

HAnimHumanoid43.joints.append(HAnimJoint1603)
HAnimJoint1604 = x3d.HAnimJoint()
HAnimJoint1604.USE = "hanim_l_talocrural"

HAnimHumanoid43.joints.append(HAnimJoint1604)
HAnimJoint1605 = x3d.HAnimJoint()
HAnimJoint1605.USE = "hanim_l_talocalcaneonavicular"

HAnimHumanoid43.joints.append(HAnimJoint1605)
HAnimJoint1606 = x3d.HAnimJoint()
HAnimJoint1606.USE = "hanim_l_cuneonavicular_1"

HAnimHumanoid43.joints.append(HAnimJoint1606)
HAnimJoint1607 = x3d.HAnimJoint()
HAnimJoint1607.USE = "hanim_l_tarsometatarsal_1"

HAnimHumanoid43.joints.append(HAnimJoint1607)
HAnimJoint1608 = x3d.HAnimJoint()
HAnimJoint1608.USE = "hanim_l_metatarsophalangeal_1"

HAnimHumanoid43.joints.append(HAnimJoint1608)
HAnimJoint1609 = x3d.HAnimJoint()
HAnimJoint1609.USE = "hanim_l_tarsal_interphalangeal_1"

HAnimHumanoid43.joints.append(HAnimJoint1609)
HAnimJoint1610 = x3d.HAnimJoint()
HAnimJoint1610.USE = "hanim_l_cuneonavicular_2"

HAnimHumanoid43.joints.append(HAnimJoint1610)
HAnimJoint1611 = x3d.HAnimJoint()
HAnimJoint1611.USE = "hanim_l_tarsometatarsal_2"

HAnimHumanoid43.joints.append(HAnimJoint1611)
HAnimJoint1612 = x3d.HAnimJoint()
HAnimJoint1612.USE = "hanim_l_metatarsophalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1612)
HAnimJoint1613 = x3d.HAnimJoint()
HAnimJoint1613.USE = "hanim_l_tarsal_proximal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1613)
HAnimJoint1614 = x3d.HAnimJoint()
HAnimJoint1614.USE = "hanim_l_tarsal_distal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1614)
HAnimJoint1615 = x3d.HAnimJoint()
HAnimJoint1615.USE = "hanim_l_cuneonavicular_3"

HAnimHumanoid43.joints.append(HAnimJoint1615)
HAnimJoint1616 = x3d.HAnimJoint()
HAnimJoint1616.USE = "hanim_l_tarsometatarsal_3"

HAnimHumanoid43.joints.append(HAnimJoint1616)
HAnimJoint1617 = x3d.HAnimJoint()
HAnimJoint1617.USE = "hanim_l_metatarsophalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint1617)
HAnimJoint1618 = x3d.HAnimJoint()
HAnimJoint1618.USE = "hanim_l_tarsal_proximal_interphalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint1618)
HAnimJoint1619 = x3d.HAnimJoint()
HAnimJoint1619.USE = "hanim_l_tarsal_distal_interphalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint1619)
HAnimJoint1620 = x3d.HAnimJoint()
HAnimJoint1620.USE = "hanim_l_calcaneocuboid"

HAnimHumanoid43.joints.append(HAnimJoint1620)
HAnimJoint1621 = x3d.HAnimJoint()
HAnimJoint1621.USE = "hanim_l_transversetarsal"

HAnimHumanoid43.joints.append(HAnimJoint1621)
HAnimJoint1622 = x3d.HAnimJoint()
HAnimJoint1622.USE = "hanim_l_tarsometatarsal_4"

HAnimHumanoid43.joints.append(HAnimJoint1622)
HAnimJoint1623 = x3d.HAnimJoint()
HAnimJoint1623.USE = "hanim_l_metatarsophalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint1623)
HAnimJoint1624 = x3d.HAnimJoint()
HAnimJoint1624.USE = "hanim_l_tarsal_proximal_interphalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint1624)
HAnimJoint1625 = x3d.HAnimJoint()
HAnimJoint1625.USE = "hanim_l_tarsal_distal_interphalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint1625)
HAnimJoint1626 = x3d.HAnimJoint()
HAnimJoint1626.USE = "hanim_l_tarsometatarsal_5"

HAnimHumanoid43.joints.append(HAnimJoint1626)
HAnimJoint1627 = x3d.HAnimJoint()
HAnimJoint1627.USE = "hanim_l_metatarsophalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint1627)
HAnimJoint1628 = x3d.HAnimJoint()
HAnimJoint1628.USE = "hanim_l_tarsal_proximal_interphalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint1628)
HAnimJoint1629 = x3d.HAnimJoint()
HAnimJoint1629.USE = "hanim_l_tarsal_distal_interphalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint1629)
HAnimJoint1630 = x3d.HAnimJoint()
HAnimJoint1630.USE = "hanim_r_hip"

HAnimHumanoid43.joints.append(HAnimJoint1630)
HAnimJoint1631 = x3d.HAnimJoint()
HAnimJoint1631.USE = "hanim_r_knee"

HAnimHumanoid43.joints.append(HAnimJoint1631)
HAnimJoint1632 = x3d.HAnimJoint()
HAnimJoint1632.USE = "hanim_r_talocrural"

HAnimHumanoid43.joints.append(HAnimJoint1632)
HAnimJoint1633 = x3d.HAnimJoint()
HAnimJoint1633.USE = "hanim_r_talocalcaneonavicular"

HAnimHumanoid43.joints.append(HAnimJoint1633)
HAnimJoint1634 = x3d.HAnimJoint()
HAnimJoint1634.USE = "hanim_r_cuneonavicular_1"

HAnimHumanoid43.joints.append(HAnimJoint1634)
HAnimJoint1635 = x3d.HAnimJoint()
HAnimJoint1635.USE = "hanim_r_tarsometatarsal_1"

HAnimHumanoid43.joints.append(HAnimJoint1635)
HAnimJoint1636 = x3d.HAnimJoint()
HAnimJoint1636.USE = "hanim_r_metatarsophalangeal_1"

HAnimHumanoid43.joints.append(HAnimJoint1636)
HAnimJoint1637 = x3d.HAnimJoint()
HAnimJoint1637.USE = "hanim_r_tarsal_interphalangeal_1"

HAnimHumanoid43.joints.append(HAnimJoint1637)
HAnimJoint1638 = x3d.HAnimJoint()
HAnimJoint1638.USE = "hanim_r_cuneonavicular_2"

HAnimHumanoid43.joints.append(HAnimJoint1638)
HAnimJoint1639 = x3d.HAnimJoint()
HAnimJoint1639.USE = "hanim_r_tarsometatarsal_2"

HAnimHumanoid43.joints.append(HAnimJoint1639)
HAnimJoint1640 = x3d.HAnimJoint()
HAnimJoint1640.USE = "hanim_r_metatarsophalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1640)
HAnimJoint1641 = x3d.HAnimJoint()
HAnimJoint1641.USE = "hanim_r_tarsal_proximal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1641)
HAnimJoint1642 = x3d.HAnimJoint()
HAnimJoint1642.USE = "hanim_r_tarsal_distal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1642)
HAnimJoint1643 = x3d.HAnimJoint()
HAnimJoint1643.USE = "hanim_r_cuneonavicular_3"

HAnimHumanoid43.joints.append(HAnimJoint1643)
HAnimJoint1644 = x3d.HAnimJoint()
HAnimJoint1644.USE = "hanim_r_tarsometatarsal_3"

HAnimHumanoid43.joints.append(HAnimJoint1644)
HAnimJoint1645 = x3d.HAnimJoint()
HAnimJoint1645.USE = "hanim_r_metatarsophalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint1645)
HAnimJoint1646 = x3d.HAnimJoint()
HAnimJoint1646.USE = "hanim_r_tarsal_proximal_interphalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint1646)
HAnimJoint1647 = x3d.HAnimJoint()
HAnimJoint1647.USE = "hanim_r_tarsal_distal_interphalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint1647)
HAnimJoint1648 = x3d.HAnimJoint()
HAnimJoint1648.USE = "hanim_r_calcaneocuboid"

HAnimHumanoid43.joints.append(HAnimJoint1648)
HAnimJoint1649 = x3d.HAnimJoint()
HAnimJoint1649.USE = "hanim_r_transversetarsal"

HAnimHumanoid43.joints.append(HAnimJoint1649)
HAnimJoint1650 = x3d.HAnimJoint()
HAnimJoint1650.USE = "hanim_r_tarsometatarsal_4"

HAnimHumanoid43.joints.append(HAnimJoint1650)
HAnimJoint1651 = x3d.HAnimJoint()
HAnimJoint1651.USE = "hanim_r_metatarsophalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint1651)
HAnimJoint1652 = x3d.HAnimJoint()
HAnimJoint1652.USE = "hanim_r_tarsal_proximal_interphalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint1652)
HAnimJoint1653 = x3d.HAnimJoint()
HAnimJoint1653.USE = "hanim_r_tarsal_distal_interphalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint1653)
HAnimJoint1654 = x3d.HAnimJoint()
HAnimJoint1654.USE = "hanim_r_tarsometatarsal_5"

HAnimHumanoid43.joints.append(HAnimJoint1654)
HAnimJoint1655 = x3d.HAnimJoint()
HAnimJoint1655.USE = "hanim_r_metatarsophalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint1655)
HAnimJoint1656 = x3d.HAnimJoint()
HAnimJoint1656.USE = "hanim_r_tarsal_proximal_interphalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint1656)
HAnimJoint1657 = x3d.HAnimJoint()
HAnimJoint1657.USE = "hanim_r_tarsal_distal_interphalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint1657)
HAnimJoint1658 = x3d.HAnimJoint()
HAnimJoint1658.USE = "hanim_vl5"

HAnimHumanoid43.joints.append(HAnimJoint1658)
HAnimJoint1659 = x3d.HAnimJoint()
HAnimJoint1659.USE = "hanim_vl4"

HAnimHumanoid43.joints.append(HAnimJoint1659)
HAnimJoint1660 = x3d.HAnimJoint()
HAnimJoint1660.USE = "hanim_vl3"

HAnimHumanoid43.joints.append(HAnimJoint1660)
HAnimJoint1661 = x3d.HAnimJoint()
HAnimJoint1661.USE = "hanim_vl2"

HAnimHumanoid43.joints.append(HAnimJoint1661)
HAnimJoint1662 = x3d.HAnimJoint()
HAnimJoint1662.USE = "hanim_vl1"

HAnimHumanoid43.joints.append(HAnimJoint1662)
HAnimJoint1663 = x3d.HAnimJoint()
HAnimJoint1663.USE = "hanim_vt12"

HAnimHumanoid43.joints.append(HAnimJoint1663)
HAnimJoint1664 = x3d.HAnimJoint()
HAnimJoint1664.USE = "hanim_vt11"

HAnimHumanoid43.joints.append(HAnimJoint1664)
HAnimJoint1665 = x3d.HAnimJoint()
HAnimJoint1665.USE = "hanim_vt10"

HAnimHumanoid43.joints.append(HAnimJoint1665)
HAnimJoint1666 = x3d.HAnimJoint()
HAnimJoint1666.USE = "hanim_vt9"

HAnimHumanoid43.joints.append(HAnimJoint1666)
HAnimJoint1667 = x3d.HAnimJoint()
HAnimJoint1667.USE = "hanim_vt8"

HAnimHumanoid43.joints.append(HAnimJoint1667)
HAnimJoint1668 = x3d.HAnimJoint()
HAnimJoint1668.USE = "hanim_vt7"

HAnimHumanoid43.joints.append(HAnimJoint1668)
HAnimJoint1669 = x3d.HAnimJoint()
HAnimJoint1669.USE = "hanim_vt6"

HAnimHumanoid43.joints.append(HAnimJoint1669)
HAnimJoint1670 = x3d.HAnimJoint()
HAnimJoint1670.USE = "hanim_vt5"

HAnimHumanoid43.joints.append(HAnimJoint1670)
HAnimJoint1671 = x3d.HAnimJoint()
HAnimJoint1671.USE = "hanim_vt4"

HAnimHumanoid43.joints.append(HAnimJoint1671)
HAnimJoint1672 = x3d.HAnimJoint()
HAnimJoint1672.USE = "hanim_vt3"

HAnimHumanoid43.joints.append(HAnimJoint1672)
HAnimJoint1673 = x3d.HAnimJoint()
HAnimJoint1673.USE = "hanim_vt2"

HAnimHumanoid43.joints.append(HAnimJoint1673)
HAnimJoint1674 = x3d.HAnimJoint()
HAnimJoint1674.USE = "hanim_vt1"

HAnimHumanoid43.joints.append(HAnimJoint1674)
HAnimJoint1675 = x3d.HAnimJoint()
HAnimJoint1675.USE = "hanim_vc7"

HAnimHumanoid43.joints.append(HAnimJoint1675)
HAnimJoint1676 = x3d.HAnimJoint()
HAnimJoint1676.USE = "hanim_vc6"

HAnimHumanoid43.joints.append(HAnimJoint1676)
HAnimJoint1677 = x3d.HAnimJoint()
HAnimJoint1677.USE = "hanim_vc5"

HAnimHumanoid43.joints.append(HAnimJoint1677)
HAnimJoint1678 = x3d.HAnimJoint()
HAnimJoint1678.USE = "hanim_vc4"

HAnimHumanoid43.joints.append(HAnimJoint1678)
HAnimJoint1679 = x3d.HAnimJoint()
HAnimJoint1679.USE = "hanim_vc3"

HAnimHumanoid43.joints.append(HAnimJoint1679)
HAnimJoint1680 = x3d.HAnimJoint()
HAnimJoint1680.USE = "hanim_vc2"

HAnimHumanoid43.joints.append(HAnimJoint1680)
HAnimJoint1681 = x3d.HAnimJoint()
HAnimJoint1681.USE = "hanim_vc1"

HAnimHumanoid43.joints.append(HAnimJoint1681)
HAnimJoint1682 = x3d.HAnimJoint()
HAnimJoint1682.USE = "hanim_skullbase"

HAnimHumanoid43.joints.append(HAnimJoint1682)
HAnimJoint1683 = x3d.HAnimJoint()
HAnimJoint1683.USE = "hanim_l_eyelid_joint"

HAnimHumanoid43.joints.append(HAnimJoint1683)
HAnimJoint1684 = x3d.HAnimJoint()
HAnimJoint1684.USE = "hanim_r_eyelid_joint"

HAnimHumanoid43.joints.append(HAnimJoint1684)
HAnimJoint1685 = x3d.HAnimJoint()
HAnimJoint1685.USE = "hanim_l_eyeball_joint"

HAnimHumanoid43.joints.append(HAnimJoint1685)
HAnimJoint1686 = x3d.HAnimJoint()
HAnimJoint1686.USE = "hanim_r_eyeball_joint"

HAnimHumanoid43.joints.append(HAnimJoint1686)
HAnimJoint1687 = x3d.HAnimJoint()
HAnimJoint1687.USE = "hanim_l_eyebrow_joint"

HAnimHumanoid43.joints.append(HAnimJoint1687)
HAnimJoint1688 = x3d.HAnimJoint()
HAnimJoint1688.USE = "hanim_r_eyebrow_joint"

HAnimHumanoid43.joints.append(HAnimJoint1688)
HAnimJoint1689 = x3d.HAnimJoint()
HAnimJoint1689.USE = "hanim_temporomandibular"

HAnimHumanoid43.joints.append(HAnimJoint1689)
HAnimJoint1690 = x3d.HAnimJoint()
HAnimJoint1690.USE = "hanim_l_sternoclavicular"

HAnimHumanoid43.joints.append(HAnimJoint1690)
HAnimJoint1691 = x3d.HAnimJoint()
HAnimJoint1691.USE = "hanim_l_acromioclavicular"

HAnimHumanoid43.joints.append(HAnimJoint1691)
HAnimJoint1692 = x3d.HAnimJoint()
HAnimJoint1692.USE = "hanim_l_shoulder"

HAnimHumanoid43.joints.append(HAnimJoint1692)
HAnimJoint1693 = x3d.HAnimJoint()
HAnimJoint1693.USE = "hanim_l_elbow"

HAnimHumanoid43.joints.append(HAnimJoint1693)
HAnimJoint1694 = x3d.HAnimJoint()
HAnimJoint1694.USE = "hanim_l_radiocarpal"

HAnimHumanoid43.joints.append(HAnimJoint1694)
HAnimJoint1695 = x3d.HAnimJoint()
HAnimJoint1695.USE = "hanim_l_midcarpal_1"

HAnimHumanoid43.joints.append(HAnimJoint1695)
HAnimJoint1696 = x3d.HAnimJoint()
HAnimJoint1696.USE = "hanim_l_carpometacarpal_1"

HAnimHumanoid43.joints.append(HAnimJoint1696)
HAnimJoint1697 = x3d.HAnimJoint()
HAnimJoint1697.USE = "hanim_l_metacarpophalangeal_1"

HAnimHumanoid43.joints.append(HAnimJoint1697)
HAnimJoint1698 = x3d.HAnimJoint()
HAnimJoint1698.USE = "hanim_l_carpal_interphalangeal_1"

HAnimHumanoid43.joints.append(HAnimJoint1698)
HAnimJoint1699 = x3d.HAnimJoint()
HAnimJoint1699.USE = "hanim_l_midcarpal_2"

HAnimHumanoid43.joints.append(HAnimJoint1699)
HAnimJoint1700 = x3d.HAnimJoint()
HAnimJoint1700.USE = "hanim_l_carpometacarpal_2"

HAnimHumanoid43.joints.append(HAnimJoint1700)
HAnimJoint1701 = x3d.HAnimJoint()
HAnimJoint1701.USE = "hanim_l_metacarpophalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1701)
HAnimJoint1702 = x3d.HAnimJoint()
HAnimJoint1702.USE = "hanim_l_carpal_proximal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1702)
HAnimJoint1703 = x3d.HAnimJoint()
HAnimJoint1703.USE = "hanim_l_carpal_distal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1703)
HAnimJoint1704 = x3d.HAnimJoint()
HAnimJoint1704.USE = "hanim_l_midcarpal_3"

HAnimHumanoid43.joints.append(HAnimJoint1704)
HAnimJoint1705 = x3d.HAnimJoint()
HAnimJoint1705.USE = "hanim_l_carpometacarpal_3"

HAnimHumanoid43.joints.append(HAnimJoint1705)
HAnimJoint1706 = x3d.HAnimJoint()
HAnimJoint1706.USE = "hanim_l_metacarpophalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint1706)
HAnimJoint1707 = x3d.HAnimJoint()
HAnimJoint1707.USE = "hanim_l_carpal_proximal_interphalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint1707)
HAnimJoint1708 = x3d.HAnimJoint()
HAnimJoint1708.USE = "hanim_l_carpal_distal_interphalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint1708)
HAnimJoint1709 = x3d.HAnimJoint()
HAnimJoint1709.USE = "hanim_l_midcarpal_4_5"

HAnimHumanoid43.joints.append(HAnimJoint1709)
HAnimJoint1710 = x3d.HAnimJoint()
HAnimJoint1710.USE = "hanim_l_carpometacarpal_4"

HAnimHumanoid43.joints.append(HAnimJoint1710)
HAnimJoint1711 = x3d.HAnimJoint()
HAnimJoint1711.USE = "hanim_l_metacarpophalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint1711)
HAnimJoint1712 = x3d.HAnimJoint()
HAnimJoint1712.USE = "hanim_l_carpal_proximal_interphalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint1712)
HAnimJoint1713 = x3d.HAnimJoint()
HAnimJoint1713.USE = "hanim_l_carpal_distal_interphalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint1713)
HAnimJoint1714 = x3d.HAnimJoint()
HAnimJoint1714.USE = "hanim_l_carpometacarpal_5"

HAnimHumanoid43.joints.append(HAnimJoint1714)
HAnimJoint1715 = x3d.HAnimJoint()
HAnimJoint1715.USE = "hanim_l_metacarpophalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint1715)
HAnimJoint1716 = x3d.HAnimJoint()
HAnimJoint1716.USE = "hanim_l_carpal_proximal_interphalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint1716)
HAnimJoint1717 = x3d.HAnimJoint()
HAnimJoint1717.USE = "hanim_l_carpal_distal_interphalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint1717)
HAnimJoint1718 = x3d.HAnimJoint()
HAnimJoint1718.USE = "hanim_r_sternoclavicular"

HAnimHumanoid43.joints.append(HAnimJoint1718)
HAnimJoint1719 = x3d.HAnimJoint()
HAnimJoint1719.USE = "hanim_r_acromioclavicular"

HAnimHumanoid43.joints.append(HAnimJoint1719)
HAnimJoint1720 = x3d.HAnimJoint()
HAnimJoint1720.USE = "hanim_r_shoulder"

HAnimHumanoid43.joints.append(HAnimJoint1720)
HAnimJoint1721 = x3d.HAnimJoint()
HAnimJoint1721.USE = "hanim_r_elbow"

HAnimHumanoid43.joints.append(HAnimJoint1721)
HAnimJoint1722 = x3d.HAnimJoint()
HAnimJoint1722.USE = "hanim_r_radiocarpal"

HAnimHumanoid43.joints.append(HAnimJoint1722)
HAnimJoint1723 = x3d.HAnimJoint()
HAnimJoint1723.USE = "hanim_r_midcarpal_1"

HAnimHumanoid43.joints.append(HAnimJoint1723)
HAnimJoint1724 = x3d.HAnimJoint()
HAnimJoint1724.USE = "hanim_r_carpometacarpal_1"

HAnimHumanoid43.joints.append(HAnimJoint1724)
HAnimJoint1725 = x3d.HAnimJoint()
HAnimJoint1725.USE = "hanim_r_metacarpophalangeal_1"

HAnimHumanoid43.joints.append(HAnimJoint1725)
HAnimJoint1726 = x3d.HAnimJoint()
HAnimJoint1726.USE = "hanim_r_carpal_interphalangeal_1"

HAnimHumanoid43.joints.append(HAnimJoint1726)
HAnimJoint1727 = x3d.HAnimJoint()
HAnimJoint1727.USE = "hanim_r_midcarpal_2"

HAnimHumanoid43.joints.append(HAnimJoint1727)
HAnimJoint1728 = x3d.HAnimJoint()
HAnimJoint1728.USE = "hanim_r_carpometacarpal_2"

HAnimHumanoid43.joints.append(HAnimJoint1728)
HAnimJoint1729 = x3d.HAnimJoint()
HAnimJoint1729.USE = "hanim_r_metacarpophalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1729)
HAnimJoint1730 = x3d.HAnimJoint()
HAnimJoint1730.USE = "hanim_r_carpal_proximal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1730)
HAnimJoint1731 = x3d.HAnimJoint()
HAnimJoint1731.USE = "hanim_r_carpal_distal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1731)
HAnimJoint1732 = x3d.HAnimJoint()
HAnimJoint1732.USE = "hanim_r_midcarpal_3"

HAnimHumanoid43.joints.append(HAnimJoint1732)
HAnimJoint1733 = x3d.HAnimJoint()
HAnimJoint1733.USE = "hanim_r_carpometacarpal_3"

HAnimHumanoid43.joints.append(HAnimJoint1733)
HAnimJoint1734 = x3d.HAnimJoint()
HAnimJoint1734.USE = "hanim_r_metacarpophalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint1734)
HAnimJoint1735 = x3d.HAnimJoint()
HAnimJoint1735.USE = "hanim_r_carpal_proximal_interphalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint1735)
HAnimJoint1736 = x3d.HAnimJoint()
HAnimJoint1736.USE = "hanim_r_carpal_distal_interphalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint1736)
HAnimJoint1737 = x3d.HAnimJoint()
HAnimJoint1737.USE = "hanim_r_midcarpal_4_5"

HAnimHumanoid43.joints.append(HAnimJoint1737)
HAnimJoint1738 = x3d.HAnimJoint()
HAnimJoint1738.USE = "hanim_r_carpometacarpal_4"

HAnimHumanoid43.joints.append(HAnimJoint1738)
HAnimJoint1739 = x3d.HAnimJoint()
HAnimJoint1739.USE = "hanim_r_metacarpophalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint1739)
HAnimJoint1740 = x3d.HAnimJoint()
HAnimJoint1740.USE = "hanim_r_carpal_proximal_interphalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint1740)
HAnimJoint1741 = x3d.HAnimJoint()
HAnimJoint1741.USE = "hanim_r_carpal_distal_interphalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint1741)
HAnimJoint1742 = x3d.HAnimJoint()
HAnimJoint1742.USE = "hanim_r_carpometacarpal_5"

HAnimHumanoid43.joints.append(HAnimJoint1742)
HAnimJoint1743 = x3d.HAnimJoint()
HAnimJoint1743.USE = "hanim_r_metacarpophalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint1743)
HAnimJoint1744 = x3d.HAnimJoint()
HAnimJoint1744.USE = "hanim_r_carpal_proximal_interphalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint1744)
HAnimJoint1745 = x3d.HAnimJoint()
HAnimJoint1745.USE = "hanim_r_carpal_distal_interphalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint1745)
HAnimSegment1746 = x3d.HAnimSegment()
HAnimSegment1746.USE = "hanim_sacrum"

HAnimHumanoid43.segments.append(HAnimSegment1746)
HAnimSegment1747 = x3d.HAnimSegment()
HAnimSegment1747.USE = "hanim_pelvis"

HAnimHumanoid43.segments.append(HAnimSegment1747)
HAnimSegment1748 = x3d.HAnimSegment()
HAnimSegment1748.USE = "hanim_l_thigh"

HAnimHumanoid43.segments.append(HAnimSegment1748)
HAnimSegment1749 = x3d.HAnimSegment()
HAnimSegment1749.USE = "hanim_l_calf"

HAnimHumanoid43.segments.append(HAnimSegment1749)
HAnimSegment1750 = x3d.HAnimSegment()
HAnimSegment1750.USE = "hanim_l_talus"

HAnimHumanoid43.segments.append(HAnimSegment1750)
HAnimSegment1751 = x3d.HAnimSegment()
HAnimSegment1751.USE = "hanim_l_navicular"

HAnimHumanoid43.segments.append(HAnimSegment1751)
HAnimSegment1752 = x3d.HAnimSegment()
HAnimSegment1752.USE = "hanim_l_cuneiform_1"

HAnimHumanoid43.segments.append(HAnimSegment1752)
HAnimSegment1753 = x3d.HAnimSegment()
HAnimSegment1753.USE = "hanim_l_metatarsal_1"

HAnimHumanoid43.segments.append(HAnimSegment1753)
HAnimSegment1754 = x3d.HAnimSegment()
HAnimSegment1754.USE = "hanim_l_tarsal_proximal_phalanx_1"

HAnimHumanoid43.segments.append(HAnimSegment1754)
HAnimSegment1755 = x3d.HAnimSegment()
HAnimSegment1755.USE = "hanim_l_cuneiform_2"

HAnimHumanoid43.segments.append(HAnimSegment1755)
HAnimSegment1756 = x3d.HAnimSegment()
HAnimSegment1756.USE = "hanim_l_metatarsal_2"

HAnimHumanoid43.segments.append(HAnimSegment1756)
HAnimSegment1757 = x3d.HAnimSegment()
HAnimSegment1757.USE = "hanim_l_tarsal_proximal_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment1757)
HAnimSegment1758 = x3d.HAnimSegment()
HAnimSegment1758.USE = "hanim_l_tarsal_middle_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment1758)
HAnimSegment1759 = x3d.HAnimSegment()
HAnimSegment1759.USE = "hanim_l_cuneiform_3"

HAnimHumanoid43.segments.append(HAnimSegment1759)
HAnimSegment1760 = x3d.HAnimSegment()
HAnimSegment1760.USE = "hanim_l_metatarsal_3"

HAnimHumanoid43.segments.append(HAnimSegment1760)
HAnimSegment1761 = x3d.HAnimSegment()
HAnimSegment1761.USE = "hanim_l_tarsal_proximal_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment1761)
HAnimSegment1762 = x3d.HAnimSegment()
HAnimSegment1762.USE = "hanim_l_tarsal_middle_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment1762)
HAnimSegment1763 = x3d.HAnimSegment()
HAnimSegment1763.USE = "hanim_l_calcaneus"

HAnimHumanoid43.segments.append(HAnimSegment1763)
HAnimSegment1764 = x3d.HAnimSegment()
HAnimSegment1764.USE = "hanim_l_cuboid"

HAnimHumanoid43.segments.append(HAnimSegment1764)
HAnimSegment1765 = x3d.HAnimSegment()
HAnimSegment1765.USE = "hanim_l_metatarsal_4"

HAnimHumanoid43.segments.append(HAnimSegment1765)
HAnimSegment1766 = x3d.HAnimSegment()
HAnimSegment1766.USE = "hanim_l_tarsal_proximal_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment1766)
HAnimSegment1767 = x3d.HAnimSegment()
HAnimSegment1767.USE = "hanim_l_tarsal_middle_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment1767)
HAnimSegment1768 = x3d.HAnimSegment()
HAnimSegment1768.USE = "hanim_l_metatarsal_5"

HAnimHumanoid43.segments.append(HAnimSegment1768)
HAnimSegment1769 = x3d.HAnimSegment()
HAnimSegment1769.USE = "hanim_l_tarsal_proximal_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment1769)
HAnimSegment1770 = x3d.HAnimSegment()
HAnimSegment1770.USE = "hanim_l_tarsal_middle_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment1770)
HAnimSegment1771 = x3d.HAnimSegment()
HAnimSegment1771.USE = "hanim_r_thigh"

HAnimHumanoid43.segments.append(HAnimSegment1771)
HAnimSegment1772 = x3d.HAnimSegment()
HAnimSegment1772.USE = "hanim_r_calf"

HAnimHumanoid43.segments.append(HAnimSegment1772)
HAnimSegment1773 = x3d.HAnimSegment()
HAnimSegment1773.USE = "hanim_r_talus"

HAnimHumanoid43.segments.append(HAnimSegment1773)
HAnimSegment1774 = x3d.HAnimSegment()
HAnimSegment1774.USE = "hanim_r_navicular"

HAnimHumanoid43.segments.append(HAnimSegment1774)
HAnimSegment1775 = x3d.HAnimSegment()
HAnimSegment1775.USE = "hanim_r_cuneiform_1"

HAnimHumanoid43.segments.append(HAnimSegment1775)
HAnimSegment1776 = x3d.HAnimSegment()
HAnimSegment1776.USE = "hanim_r_metatarsal_1"

HAnimHumanoid43.segments.append(HAnimSegment1776)
HAnimSegment1777 = x3d.HAnimSegment()
HAnimSegment1777.USE = "hanim_r_tarsal_proximal_phalanx_1"

HAnimHumanoid43.segments.append(HAnimSegment1777)
HAnimSegment1778 = x3d.HAnimSegment()
HAnimSegment1778.USE = "hanim_r_cuneiform_2"

HAnimHumanoid43.segments.append(HAnimSegment1778)
HAnimSegment1779 = x3d.HAnimSegment()
HAnimSegment1779.USE = "hanim_r_metatarsal_2"

HAnimHumanoid43.segments.append(HAnimSegment1779)
HAnimSegment1780 = x3d.HAnimSegment()
HAnimSegment1780.USE = "hanim_r_tarsal_proximal_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment1780)
HAnimSegment1781 = x3d.HAnimSegment()
HAnimSegment1781.USE = "hanim_r_tarsal_middle_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment1781)
HAnimSegment1782 = x3d.HAnimSegment()
HAnimSegment1782.USE = "hanim_r_cuneiform_3"

HAnimHumanoid43.segments.append(HAnimSegment1782)
HAnimSegment1783 = x3d.HAnimSegment()
HAnimSegment1783.USE = "hanim_r_metatarsal_3"

HAnimHumanoid43.segments.append(HAnimSegment1783)
HAnimSegment1784 = x3d.HAnimSegment()
HAnimSegment1784.USE = "hanim_r_tarsal_proximal_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment1784)
HAnimSegment1785 = x3d.HAnimSegment()
HAnimSegment1785.USE = "hanim_r_tarsal_middle_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment1785)
HAnimSegment1786 = x3d.HAnimSegment()
HAnimSegment1786.USE = "hanim_r_calcaneus"

HAnimHumanoid43.segments.append(HAnimSegment1786)
HAnimSegment1787 = x3d.HAnimSegment()
HAnimSegment1787.USE = "hanim_r_cuboid"

HAnimHumanoid43.segments.append(HAnimSegment1787)
HAnimSegment1788 = x3d.HAnimSegment()
HAnimSegment1788.USE = "hanim_r_metatarsal_4"

HAnimHumanoid43.segments.append(HAnimSegment1788)
HAnimSegment1789 = x3d.HAnimSegment()
HAnimSegment1789.USE = "hanim_r_tarsal_proximal_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment1789)
HAnimSegment1790 = x3d.HAnimSegment()
HAnimSegment1790.USE = "hanim_r_tarsal_middle_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment1790)
HAnimSegment1791 = x3d.HAnimSegment()
HAnimSegment1791.USE = "hanim_r_metatarsal_5"

HAnimHumanoid43.segments.append(HAnimSegment1791)
HAnimSegment1792 = x3d.HAnimSegment()
HAnimSegment1792.USE = "hanim_r_tarsal_proximal_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment1792)
HAnimSegment1793 = x3d.HAnimSegment()
HAnimSegment1793.USE = "hanim_r_tarsal_middle_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment1793)
HAnimSegment1794 = x3d.HAnimSegment()
HAnimSegment1794.USE = "hanim_l5"

HAnimHumanoid43.segments.append(HAnimSegment1794)
HAnimSegment1795 = x3d.HAnimSegment()
HAnimSegment1795.USE = "hanim_l4"

HAnimHumanoid43.segments.append(HAnimSegment1795)
HAnimSegment1796 = x3d.HAnimSegment()
HAnimSegment1796.USE = "hanim_l3"

HAnimHumanoid43.segments.append(HAnimSegment1796)
HAnimSegment1797 = x3d.HAnimSegment()
HAnimSegment1797.USE = "hanim_l2"

HAnimHumanoid43.segments.append(HAnimSegment1797)
HAnimSegment1798 = x3d.HAnimSegment()
HAnimSegment1798.USE = "hanim_l1"

HAnimHumanoid43.segments.append(HAnimSegment1798)
HAnimSegment1799 = x3d.HAnimSegment()
HAnimSegment1799.USE = "hanim_t12"

HAnimHumanoid43.segments.append(HAnimSegment1799)
HAnimSegment1800 = x3d.HAnimSegment()
HAnimSegment1800.USE = "hanim_t11"

HAnimHumanoid43.segments.append(HAnimSegment1800)
HAnimSegment1801 = x3d.HAnimSegment()
HAnimSegment1801.USE = "hanim_t10"

HAnimHumanoid43.segments.append(HAnimSegment1801)
HAnimSegment1802 = x3d.HAnimSegment()
HAnimSegment1802.USE = "hanim_t9"

HAnimHumanoid43.segments.append(HAnimSegment1802)
HAnimSegment1803 = x3d.HAnimSegment()
HAnimSegment1803.USE = "hanim_t8"

HAnimHumanoid43.segments.append(HAnimSegment1803)
HAnimSegment1804 = x3d.HAnimSegment()
HAnimSegment1804.USE = "hanim_t7"

HAnimHumanoid43.segments.append(HAnimSegment1804)
HAnimSegment1805 = x3d.HAnimSegment()
HAnimSegment1805.USE = "hanim_t6"

HAnimHumanoid43.segments.append(HAnimSegment1805)
HAnimSegment1806 = x3d.HAnimSegment()
HAnimSegment1806.USE = "hanim_t5"

HAnimHumanoid43.segments.append(HAnimSegment1806)
HAnimSegment1807 = x3d.HAnimSegment()
HAnimSegment1807.USE = "hanim_t4"

HAnimHumanoid43.segments.append(HAnimSegment1807)
HAnimSegment1808 = x3d.HAnimSegment()
HAnimSegment1808.USE = "hanim_t3"

HAnimHumanoid43.segments.append(HAnimSegment1808)
HAnimSegment1809 = x3d.HAnimSegment()
HAnimSegment1809.USE = "hanim_t2"

HAnimHumanoid43.segments.append(HAnimSegment1809)
HAnimSegment1810 = x3d.HAnimSegment()
HAnimSegment1810.USE = "hanim_t1"

HAnimHumanoid43.segments.append(HAnimSegment1810)
HAnimSegment1811 = x3d.HAnimSegment()
HAnimSegment1811.USE = "hanim_c7"

HAnimHumanoid43.segments.append(HAnimSegment1811)
HAnimSegment1812 = x3d.HAnimSegment()
HAnimSegment1812.USE = "hanim_c6"

HAnimHumanoid43.segments.append(HAnimSegment1812)
HAnimSegment1813 = x3d.HAnimSegment()
HAnimSegment1813.USE = "hanim_c5"

HAnimHumanoid43.segments.append(HAnimSegment1813)
HAnimSegment1814 = x3d.HAnimSegment()
HAnimSegment1814.USE = "hanim_c4"

HAnimHumanoid43.segments.append(HAnimSegment1814)
HAnimSegment1815 = x3d.HAnimSegment()
HAnimSegment1815.USE = "hanim_c3"

HAnimHumanoid43.segments.append(HAnimSegment1815)
HAnimSegment1816 = x3d.HAnimSegment()
HAnimSegment1816.USE = "hanim_c2"

HAnimHumanoid43.segments.append(HAnimSegment1816)
HAnimSegment1817 = x3d.HAnimSegment()
HAnimSegment1817.USE = "hanim_c1"

HAnimHumanoid43.segments.append(HAnimSegment1817)
HAnimSegment1818 = x3d.HAnimSegment()
HAnimSegment1818.USE = "hanim_skull"

HAnimHumanoid43.segments.append(HAnimSegment1818)
HAnimSegment1819 = x3d.HAnimSegment()
HAnimSegment1819.USE = "hanim_l_clavicle"

HAnimHumanoid43.segments.append(HAnimSegment1819)
HAnimSegment1820 = x3d.HAnimSegment()
HAnimSegment1820.USE = "hanim_l_scapula"

HAnimHumanoid43.segments.append(HAnimSegment1820)
HAnimSegment1821 = x3d.HAnimSegment()
HAnimSegment1821.USE = "hanim_l_upperarm"

HAnimHumanoid43.segments.append(HAnimSegment1821)
HAnimSegment1822 = x3d.HAnimSegment()
HAnimSegment1822.USE = "hanim_l_forearm"

HAnimHumanoid43.segments.append(HAnimSegment1822)
HAnimSegment1823 = x3d.HAnimSegment()
HAnimSegment1823.USE = "hanim_l_carpal"

HAnimHumanoid43.segments.append(HAnimSegment1823)
HAnimSegment1824 = x3d.HAnimSegment()
HAnimSegment1824.USE = "hanim_l_trapezium"

HAnimHumanoid43.segments.append(HAnimSegment1824)
HAnimSegment1825 = x3d.HAnimSegment()
HAnimSegment1825.USE = "hanim_l_metacarpal_1"

HAnimHumanoid43.segments.append(HAnimSegment1825)
HAnimSegment1826 = x3d.HAnimSegment()
HAnimSegment1826.USE = "hanim_l_carpal_proximal_phalanx_1"

HAnimHumanoid43.segments.append(HAnimSegment1826)
HAnimSegment1827 = x3d.HAnimSegment()
HAnimSegment1827.USE = "hanim_l_trapezoid"

HAnimHumanoid43.segments.append(HAnimSegment1827)
HAnimSegment1828 = x3d.HAnimSegment()
HAnimSegment1828.USE = "hanim_l_metacarpal_2"

HAnimHumanoid43.segments.append(HAnimSegment1828)
HAnimSegment1829 = x3d.HAnimSegment()
HAnimSegment1829.USE = "hanim_l_carpal_proximal_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment1829)
HAnimSegment1830 = x3d.HAnimSegment()
HAnimSegment1830.USE = "hanim_l_carpal_middle_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment1830)
HAnimSegment1831 = x3d.HAnimSegment()
HAnimSegment1831.USE = "hanim_l_capitate"

HAnimHumanoid43.segments.append(HAnimSegment1831)
HAnimSegment1832 = x3d.HAnimSegment()
HAnimSegment1832.USE = "hanim_l_metacarpal_3"

HAnimHumanoid43.segments.append(HAnimSegment1832)
HAnimSegment1833 = x3d.HAnimSegment()
HAnimSegment1833.USE = "hanim_l_carpal_proximal_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment1833)
HAnimSegment1834 = x3d.HAnimSegment()
HAnimSegment1834.USE = "hanim_l_carpal_middle_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment1834)
HAnimSegment1835 = x3d.HAnimSegment()
HAnimSegment1835.USE = "hanim_l_hamate"

HAnimHumanoid43.segments.append(HAnimSegment1835)
HAnimSegment1836 = x3d.HAnimSegment()
HAnimSegment1836.USE = "hanim_l_metacarpal_4"

HAnimHumanoid43.segments.append(HAnimSegment1836)
HAnimSegment1837 = x3d.HAnimSegment()
HAnimSegment1837.USE = "hanim_l_carpal_proximal_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment1837)
HAnimSegment1838 = x3d.HAnimSegment()
HAnimSegment1838.USE = "hanim_l_carpal_middle_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment1838)
HAnimSegment1839 = x3d.HAnimSegment()
HAnimSegment1839.USE = "hanim_l_metacarpal_5"

HAnimHumanoid43.segments.append(HAnimSegment1839)
HAnimSegment1840 = x3d.HAnimSegment()
HAnimSegment1840.USE = "hanim_l_carpal_proximal_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment1840)
HAnimSegment1841 = x3d.HAnimSegment()
HAnimSegment1841.USE = "hanim_l_carpal_middle_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment1841)
HAnimSegment1842 = x3d.HAnimSegment()
HAnimSegment1842.USE = "hanim_r_clavicle"

HAnimHumanoid43.segments.append(HAnimSegment1842)
HAnimSegment1843 = x3d.HAnimSegment()
HAnimSegment1843.USE = "hanim_r_scapula"

HAnimHumanoid43.segments.append(HAnimSegment1843)
HAnimSegment1844 = x3d.HAnimSegment()
HAnimSegment1844.USE = "hanim_r_upperarm"

HAnimHumanoid43.segments.append(HAnimSegment1844)
HAnimSegment1845 = x3d.HAnimSegment()
HAnimSegment1845.USE = "hanim_r_forearm"

HAnimHumanoid43.segments.append(HAnimSegment1845)
HAnimSegment1846 = x3d.HAnimSegment()
HAnimSegment1846.USE = "hanim_r_carpal"

HAnimHumanoid43.segments.append(HAnimSegment1846)
HAnimSegment1847 = x3d.HAnimSegment()
HAnimSegment1847.USE = "hanim_r_trapezium"

HAnimHumanoid43.segments.append(HAnimSegment1847)
HAnimSegment1848 = x3d.HAnimSegment()
HAnimSegment1848.USE = "hanim_r_metacarpal_1"

HAnimHumanoid43.segments.append(HAnimSegment1848)
HAnimSegment1849 = x3d.HAnimSegment()
HAnimSegment1849.USE = "hanim_r_carpal_proximal_phalanx_1"

HAnimHumanoid43.segments.append(HAnimSegment1849)
HAnimSegment1850 = x3d.HAnimSegment()
HAnimSegment1850.USE = "hanim_r_trapezoid"

HAnimHumanoid43.segments.append(HAnimSegment1850)
HAnimSegment1851 = x3d.HAnimSegment()
HAnimSegment1851.USE = "hanim_r_metacarpal_2"

HAnimHumanoid43.segments.append(HAnimSegment1851)
HAnimSegment1852 = x3d.HAnimSegment()
HAnimSegment1852.USE = "hanim_r_carpal_proximal_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment1852)
HAnimSegment1853 = x3d.HAnimSegment()
HAnimSegment1853.USE = "hanim_r_carpal_middle_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment1853)
HAnimSegment1854 = x3d.HAnimSegment()
HAnimSegment1854.USE = "hanim_r_capitate"

HAnimHumanoid43.segments.append(HAnimSegment1854)
HAnimSegment1855 = x3d.HAnimSegment()
HAnimSegment1855.USE = "hanim_r_metacarpal_3"

HAnimHumanoid43.segments.append(HAnimSegment1855)
HAnimSegment1856 = x3d.HAnimSegment()
HAnimSegment1856.USE = "hanim_r_carpal_proximal_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment1856)
HAnimSegment1857 = x3d.HAnimSegment()
HAnimSegment1857.USE = "hanim_r_carpal_middle_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment1857)
HAnimSegment1858 = x3d.HAnimSegment()
HAnimSegment1858.USE = "hanim_r_hamate"

HAnimHumanoid43.segments.append(HAnimSegment1858)
HAnimSegment1859 = x3d.HAnimSegment()
HAnimSegment1859.USE = "hanim_r_metacarpal_4"

HAnimHumanoid43.segments.append(HAnimSegment1859)
HAnimSegment1860 = x3d.HAnimSegment()
HAnimSegment1860.USE = "hanim_r_carpal_proximal_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment1860)
HAnimSegment1861 = x3d.HAnimSegment()
HAnimSegment1861.USE = "hanim_r_carpal_middle_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment1861)
HAnimSegment1862 = x3d.HAnimSegment()
HAnimSegment1862.USE = "hanim_r_metacarpal_5"

HAnimHumanoid43.segments.append(HAnimSegment1862)
HAnimSegment1863 = x3d.HAnimSegment()
HAnimSegment1863.USE = "hanim_r_carpal_proximal_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment1863)
HAnimSegment1864 = x3d.HAnimSegment()
HAnimSegment1864.USE = "hanim_r_carpal_middle_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment1864)
HAnimSite1865 = x3d.HAnimSite()
HAnimSite1865.USE = "hanim_buttocks_standing_wall_contact_point_pt"

HAnimHumanoid43.sites.append(HAnimSite1865)
HAnimSite1866 = x3d.HAnimSite()
HAnimSite1866.USE = "hanim_crotch_pt"

HAnimHumanoid43.sites.append(HAnimSite1866)
HAnimSite1867 = x3d.HAnimSite()
HAnimSite1867.USE = "hanim_l_asis_pt"

HAnimHumanoid43.sites.append(HAnimSite1867)
HAnimSite1868 = x3d.HAnimSite()
HAnimSite1868.USE = "hanim_l_iliocristale_pt"

HAnimHumanoid43.sites.append(HAnimSite1868)
HAnimSite1869 = x3d.HAnimSite()
HAnimSite1869.USE = "hanim_l_psis_pt"

HAnimHumanoid43.sites.append(HAnimSite1869)
HAnimSite1870 = x3d.HAnimSite()
HAnimSite1870.USE = "hanim_l_trochanterion_pt"

HAnimHumanoid43.sites.append(HAnimSite1870)
HAnimSite1871 = x3d.HAnimSite()
HAnimSite1871.USE = "hanim_r_asis_pt"

HAnimHumanoid43.sites.append(HAnimSite1871)
HAnimSite1872 = x3d.HAnimSite()
HAnimSite1872.USE = "hanim_r_iliocristale_pt"

HAnimHumanoid43.sites.append(HAnimSite1872)
HAnimSite1873 = x3d.HAnimSite()
HAnimSite1873.USE = "hanim_r_psis_pt"

HAnimHumanoid43.sites.append(HAnimSite1873)
HAnimSite1874 = x3d.HAnimSite()
HAnimSite1874.USE = "hanim_r_trochanterion_pt"

HAnimHumanoid43.sites.append(HAnimSite1874)
HAnimSite1875 = x3d.HAnimSite()
HAnimSite1875.USE = "hanim_navel_pt"

HAnimHumanoid43.sites.append(HAnimSite1875)
HAnimSite1876 = x3d.HAnimSite()
HAnimSite1876.USE = "hanim_waist_preferred_anterior_pt"

HAnimHumanoid43.sites.append(HAnimSite1876)
HAnimSite1877 = x3d.HAnimSite()
HAnimSite1877.USE = "hanim_waist_preferred_posterior_pt"

HAnimHumanoid43.sites.append(HAnimSite1877)
HAnimSite1878 = x3d.HAnimSite()
HAnimSite1878.USE = "hanim_l_femoral_lateral_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite1878)
HAnimSite1879 = x3d.HAnimSite()
HAnimSite1879.USE = "hanim_l_femoral_medial_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite1879)
HAnimSite1880 = x3d.HAnimSite()
HAnimSite1880.USE = "hanim_l_knee_crease_pt"

HAnimHumanoid43.sites.append(HAnimSite1880)
HAnimSite1881 = x3d.HAnimSite()
HAnimSite1881.USE = "hanim_l_suprapatella_pt"

HAnimHumanoid43.sites.append(HAnimSite1881)
HAnimSite1882 = x3d.HAnimSite()
HAnimSite1882.USE = "hanim_r_femoral_lateral_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite1882)
HAnimSite1883 = x3d.HAnimSite()
HAnimSite1883.USE = "hanim_r_femoral_medial_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite1883)
HAnimSite1884 = x3d.HAnimSite()
HAnimSite1884.USE = "hanim_r_knee_crease_pt"

HAnimHumanoid43.sites.append(HAnimSite1884)
HAnimSite1885 = x3d.HAnimSite()
HAnimSite1885.USE = "hanim_r_suprapatella_pt"

HAnimHumanoid43.sites.append(HAnimSite1885)
HAnimSite1886 = x3d.HAnimSite()
HAnimSite1886.USE = "hanim_l_lateral_malleolus_pt"

HAnimHumanoid43.sites.append(HAnimSite1886)
HAnimSite1887 = x3d.HAnimSite()
HAnimSite1887.USE = "hanim_l_medial_malleolus_pt"

HAnimHumanoid43.sites.append(HAnimSite1887)
HAnimSite1888 = x3d.HAnimSite()
HAnimSite1888.USE = "hanim_l_tibiale_pt"

HAnimHumanoid43.sites.append(HAnimSite1888)
HAnimSite1889 = x3d.HAnimSite()
HAnimSite1889.USE = "hanim_l_calcaneus_posterior_pt"

HAnimHumanoid43.sites.append(HAnimSite1889)
HAnimSite1890 = x3d.HAnimSite()
HAnimSite1890.USE = "hanim_l_sphyrion_pt"

HAnimHumanoid43.sites.append(HAnimSite1890)
HAnimSite1891 = x3d.HAnimSite()
HAnimSite1891.USE = "hanim_l_metatarsal_phalanx_1_pt"

HAnimHumanoid43.sites.append(HAnimSite1891)
HAnimSite1892 = x3d.HAnimSite()
HAnimSite1892.USE = "hanim_l_tarsal_distal_phalanx_1_tip"

HAnimHumanoid43.sites.append(HAnimSite1892)
HAnimSite1893 = x3d.HAnimSite()
HAnimSite1893.USE = "hanim_l_tarsal_distal_phalanx_2_tip"

HAnimHumanoid43.sites.append(HAnimSite1893)
HAnimSite1894 = x3d.HAnimSite()
HAnimSite1894.USE = "hanim_l_tarsal_distal_phalanx_3_tip"

HAnimHumanoid43.sites.append(HAnimSite1894)
HAnimSite1895 = x3d.HAnimSite()
HAnimSite1895.USE = "hanim_l_tarsal_distal_phalanx_4_tip"

HAnimHumanoid43.sites.append(HAnimSite1895)
HAnimSite1896 = x3d.HAnimSite()
HAnimSite1896.USE = "hanim_l_metatarsal_phalanx_5_pt"

HAnimHumanoid43.sites.append(HAnimSite1896)
HAnimSite1897 = x3d.HAnimSite()
HAnimSite1897.USE = "hanim_l_tarsal_distal_phalanx_5_tip"

HAnimHumanoid43.sites.append(HAnimSite1897)
HAnimSite1898 = x3d.HAnimSite()
HAnimSite1898.USE = "hanim_r_lateral_malleolus_pt"

HAnimHumanoid43.sites.append(HAnimSite1898)
HAnimSite1899 = x3d.HAnimSite()
HAnimSite1899.USE = "hanim_r_medial_malleolus_pt"

HAnimHumanoid43.sites.append(HAnimSite1899)
HAnimSite1900 = x3d.HAnimSite()
HAnimSite1900.USE = "hanim_r_tibiale_pt"

HAnimHumanoid43.sites.append(HAnimSite1900)
HAnimSite1901 = x3d.HAnimSite()
HAnimSite1901.USE = "hanim_r_calcaneus_posterior_pt"

HAnimHumanoid43.sites.append(HAnimSite1901)
HAnimSite1902 = x3d.HAnimSite()
HAnimSite1902.USE = "hanim_r_sphyrion_pt"

HAnimHumanoid43.sites.append(HAnimSite1902)
HAnimSite1903 = x3d.HAnimSite()
HAnimSite1903.USE = "hanim_r_metatarsal_phalanx_1_pt"

HAnimHumanoid43.sites.append(HAnimSite1903)
HAnimSite1904 = x3d.HAnimSite()
HAnimSite1904.USE = "hanim_r_tarsal_distal_phalanx_1_tip"

HAnimHumanoid43.sites.append(HAnimSite1904)
HAnimSite1905 = x3d.HAnimSite()
HAnimSite1905.USE = "hanim_r_tarsal_distal_phalanx_2_tip"

HAnimHumanoid43.sites.append(HAnimSite1905)
HAnimSite1906 = x3d.HAnimSite()
HAnimSite1906.USE = "hanim_r_tarsal_distal_phalanx_3_tip"

HAnimHumanoid43.sites.append(HAnimSite1906)
HAnimSite1907 = x3d.HAnimSite()
HAnimSite1907.USE = "hanim_r_tarsal_distal_phalanx_4_tip"

HAnimHumanoid43.sites.append(HAnimSite1907)
HAnimSite1908 = x3d.HAnimSite()
HAnimSite1908.USE = "hanim_r_metatarsal_phalanx_5_pt"

HAnimHumanoid43.sites.append(HAnimSite1908)
HAnimSite1909 = x3d.HAnimSite()
HAnimSite1909.USE = "hanim_r_tarsal_distal_phalanx_5_tip"

HAnimHumanoid43.sites.append(HAnimSite1909)
HAnimSite1910 = x3d.HAnimSite()
HAnimSite1910.USE = "hanim_l_rib10_pt"

HAnimHumanoid43.sites.append(HAnimSite1910)
HAnimSite1911 = x3d.HAnimSite()
HAnimSite1911.USE = "hanim_r_rib10_pt"

HAnimHumanoid43.sites.append(HAnimSite1911)
HAnimSite1912 = x3d.HAnimSite()
HAnimSite1912.USE = "hanim_spine_2_middle_back_pt"

HAnimHumanoid43.sites.append(HAnimSite1912)
HAnimSite1913 = x3d.HAnimSite()
HAnimSite1913.USE = "hanim_substernale_pt"

HAnimHumanoid43.sites.append(HAnimSite1913)
HAnimSite1914 = x3d.HAnimSite()
HAnimSite1914.USE = "hanim_l_thelion_pt"

HAnimHumanoid43.sites.append(HAnimSite1914)
HAnimSite1915 = x3d.HAnimSite()
HAnimSite1915.USE = "hanim_r_thelion_pt"

HAnimHumanoid43.sites.append(HAnimSite1915)
HAnimSite1916 = x3d.HAnimSite()
HAnimSite1916.USE = "hanim_l_chest_midsagittal_plane_pt"

HAnimHumanoid43.sites.append(HAnimSite1916)
HAnimSite1917 = x3d.HAnimSite()
HAnimSite1917.USE = "hanim_mesosternale_pt"

HAnimHumanoid43.sites.append(HAnimSite1917)
HAnimSite1918 = x3d.HAnimSite()
HAnimSite1918.USE = "hanim_r_chest_midsagittal_plane_pt"

HAnimHumanoid43.sites.append(HAnimSite1918)
HAnimSite1919 = x3d.HAnimSite()
HAnimSite1919.USE = "hanim_rear_center_midsagittal_plane_pt"

HAnimHumanoid43.sites.append(HAnimSite1919)
HAnimSite1920 = x3d.HAnimSite()
HAnimSite1920.USE = "hanim_spine_1_middle_back_pt"

HAnimHumanoid43.sites.append(HAnimSite1920)
HAnimSite1921 = x3d.HAnimSite()
HAnimSite1921.USE = "hanim_cervicale_pt"

HAnimHumanoid43.sites.append(HAnimSite1921)
HAnimSite1922 = x3d.HAnimSite()
HAnimSite1922.USE = "hanim_suprasternale_pt"

HAnimHumanoid43.sites.append(HAnimSite1922)
HAnimSite1923 = x3d.HAnimSite()
HAnimSite1923.USE = "hanim_l_neck_base_pt"

HAnimHumanoid43.sites.append(HAnimSite1923)
HAnimSite1924 = x3d.HAnimSite()
HAnimSite1924.USE = "hanim_r_neck_base_pt"

HAnimHumanoid43.sites.append(HAnimSite1924)
HAnimSite1925 = x3d.HAnimSite()
HAnimSite1925.USE = "hanim_l_acromion_pt"

HAnimHumanoid43.sites.append(HAnimSite1925)
HAnimSite1926 = x3d.HAnimSite()
HAnimSite1926.USE = "hanim_l_axilla_distal_pt"

HAnimHumanoid43.sites.append(HAnimSite1926)
HAnimSite1927 = x3d.HAnimSite()
HAnimSite1927.USE = "hanim_l_axilla_posterior_folds_pt"

HAnimHumanoid43.sites.append(HAnimSite1927)
HAnimSite1928 = x3d.HAnimSite()
HAnimSite1928.USE = "hanim_l_axilla_proximal_pt"

HAnimHumanoid43.sites.append(HAnimSite1928)
HAnimSite1929 = x3d.HAnimSite()
HAnimSite1929.USE = "hanim_l_clavicale_pt"

HAnimHumanoid43.sites.append(HAnimSite1929)
HAnimSite1930 = x3d.HAnimSite()
HAnimSite1930.USE = "hanim_r_acromion_pt"

HAnimHumanoid43.sites.append(HAnimSite1930)
HAnimSite1931 = x3d.HAnimSite()
HAnimSite1931.USE = "hanim_r_axilla_distal_pt"

HAnimHumanoid43.sites.append(HAnimSite1931)
HAnimSite1932 = x3d.HAnimSite()
HAnimSite1932.USE = "hanim_r_axilla_posterior_folds_pt"

HAnimHumanoid43.sites.append(HAnimSite1932)
HAnimSite1933 = x3d.HAnimSite()
HAnimSite1933.USE = "hanim_r_axilla_proximal_pt"

HAnimHumanoid43.sites.append(HAnimSite1933)
HAnimSite1934 = x3d.HAnimSite()
HAnimSite1934.USE = "hanim_r_clavicale_pt"

HAnimHumanoid43.sites.append(HAnimSite1934)
HAnimSite1935 = x3d.HAnimSite()
HAnimSite1935.USE = "hanim_adams_apple_pt"

HAnimHumanoid43.sites.append(HAnimSite1935)
HAnimSite1936 = x3d.HAnimSite()
HAnimSite1936.USE = "hanim_glabella_pt"

HAnimHumanoid43.sites.append(HAnimSite1936)
HAnimSite1937 = x3d.HAnimSite()
HAnimSite1937.USE = "hanim_l_ectocanthus_pt"

HAnimHumanoid43.sites.append(HAnimSite1937)
HAnimSite1938 = x3d.HAnimSite()
HAnimSite1938.USE = "hanim_l_infraorbitale_pt"

HAnimHumanoid43.sites.append(HAnimSite1938)
HAnimSite1939 = x3d.HAnimSite()
HAnimSite1939.USE = "hanim_l_tragion_pt"

HAnimHumanoid43.sites.append(HAnimSite1939)
HAnimSite1940 = x3d.HAnimSite()
HAnimSite1940.USE = "hanim_nuchale_pt"

HAnimHumanoid43.sites.append(HAnimSite1940)
HAnimSite1941 = x3d.HAnimSite()
HAnimSite1941.USE = "hanim_opisthocranion_pt"

HAnimHumanoid43.sites.append(HAnimSite1941)
HAnimSite1942 = x3d.HAnimSite()
HAnimSite1942.USE = "hanim_r_ectocanthus_pt"

HAnimHumanoid43.sites.append(HAnimSite1942)
HAnimSite1943 = x3d.HAnimSite()
HAnimSite1943.USE = "hanim_r_infraorbitale_pt"

HAnimHumanoid43.sites.append(HAnimSite1943)
HAnimSite1944 = x3d.HAnimSite()
HAnimSite1944.USE = "hanim_r_tragion_pt"

HAnimHumanoid43.sites.append(HAnimSite1944)
HAnimSite1945 = x3d.HAnimSite()
HAnimSite1945.USE = "hanim_sellion_pt"

HAnimHumanoid43.sites.append(HAnimSite1945)
HAnimSite1946 = x3d.HAnimSite()
HAnimSite1946.USE = "hanim_skull_vertex_pt"

HAnimHumanoid43.sites.append(HAnimSite1946)
HAnimSite1947 = x3d.HAnimSite()
HAnimSite1947.USE = "hanim_l_gonion_pt"

HAnimHumanoid43.sites.append(HAnimSite1947)
HAnimSite1948 = x3d.HAnimSite()
HAnimSite1948.USE = "hanim_menton_pt"

HAnimHumanoid43.sites.append(HAnimSite1948)
HAnimSite1949 = x3d.HAnimSite()
HAnimSite1949.USE = "hanim_r_gonion_pt"

HAnimHumanoid43.sites.append(HAnimSite1949)
HAnimSite1950 = x3d.HAnimSite()
HAnimSite1950.USE = "hanim_supramenton_pt"

HAnimHumanoid43.sites.append(HAnimSite1950)
HAnimSite1951 = x3d.HAnimSite()
HAnimSite1951.USE = "hanim_l_bideltoid_pt"

HAnimHumanoid43.sites.append(HAnimSite1951)
HAnimSite1952 = x3d.HAnimSite()
HAnimSite1952.USE = "hanim_l_humeral_lateral_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite1952)
HAnimSite1953 = x3d.HAnimSite()
HAnimSite1953.USE = "hanim_l_humeral_medial_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite1953)
HAnimSite1954 = x3d.HAnimSite()
HAnimSite1954.USE = "hanim_l_olecranon_pt"

HAnimHumanoid43.sites.append(HAnimSite1954)
HAnimSite1955 = x3d.HAnimSite()
HAnimSite1955.USE = "hanim_l_radial_styloid_pt"

HAnimHumanoid43.sites.append(HAnimSite1955)
HAnimSite1956 = x3d.HAnimSite()
HAnimSite1956.USE = "hanim_l_radiale_pt"

HAnimHumanoid43.sites.append(HAnimSite1956)
HAnimSite1957 = x3d.HAnimSite()
HAnimSite1957.USE = "hanim_l_ulnar_styloid_pt"

HAnimHumanoid43.sites.append(HAnimSite1957)
HAnimSite1958 = x3d.HAnimSite()
HAnimSite1958.USE = "hanim_l_carpal_distal_phalanx_1_tip"

HAnimHumanoid43.sites.append(HAnimSite1958)
HAnimSite1959 = x3d.HAnimSite()
HAnimSite1959.USE = "hanim_l_metacarpal_phalanx_2_pt"

HAnimHumanoid43.sites.append(HAnimSite1959)
HAnimSite1960 = x3d.HAnimSite()
HAnimSite1960.USE = "hanim_l_carpal_distal_phalanx_2_tip"

HAnimHumanoid43.sites.append(HAnimSite1960)
HAnimSite1961 = x3d.HAnimSite()
HAnimSite1961.USE = "hanim_l_dactylion_pt"

HAnimHumanoid43.sites.append(HAnimSite1961)
HAnimSite1962 = x3d.HAnimSite()
HAnimSite1962.USE = "hanim_l_metacarpal_phalanx_3_pt"

HAnimHumanoid43.sites.append(HAnimSite1962)
HAnimSite1963 = x3d.HAnimSite()
HAnimSite1963.USE = "hanim_l_carpal_distal_phalanx_3_tip"

HAnimHumanoid43.sites.append(HAnimSite1963)
HAnimSite1964 = x3d.HAnimSite()
HAnimSite1964.USE = "hanim_l_metacarpal_phalanx_5_pt"

HAnimHumanoid43.sites.append(HAnimSite1964)
HAnimSite1965 = x3d.HAnimSite()
HAnimSite1965.USE = "hanim_l_carpal_distal_phalanx_4_tip"

HAnimHumanoid43.sites.append(HAnimSite1965)
HAnimSite1966 = x3d.HAnimSite()
HAnimSite1966.USE = "hanim_l_carpal_distal_phalanx_5_tip"

HAnimHumanoid43.sites.append(HAnimSite1966)
HAnimSite1967 = x3d.HAnimSite()
HAnimSite1967.USE = "hanim_r_bideltoid_pt"

HAnimHumanoid43.sites.append(HAnimSite1967)
HAnimSite1968 = x3d.HAnimSite()
HAnimSite1968.USE = "hanim_r_humeral_lateral_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite1968)
HAnimSite1969 = x3d.HAnimSite()
HAnimSite1969.USE = "hanim_r_humeral_medial_epicondyles_pt"

HAnimHumanoid43.sites.append(HAnimSite1969)
HAnimSite1970 = x3d.HAnimSite()
HAnimSite1970.USE = "hanim_r_olecranon_pt"

HAnimHumanoid43.sites.append(HAnimSite1970)
HAnimSite1971 = x3d.HAnimSite()
HAnimSite1971.USE = "hanim_r_radial_styloid_pt"

HAnimHumanoid43.sites.append(HAnimSite1971)
HAnimSite1972 = x3d.HAnimSite()
HAnimSite1972.USE = "hanim_r_radiale_pt"

HAnimHumanoid43.sites.append(HAnimSite1972)
HAnimSite1973 = x3d.HAnimSite()
HAnimSite1973.USE = "hanim_r_ulnar_styloid_pt"

HAnimHumanoid43.sites.append(HAnimSite1973)
HAnimSite1974 = x3d.HAnimSite()
HAnimSite1974.USE = "hanim_r_carpal_distal_phalanx_1_tip"

HAnimHumanoid43.sites.append(HAnimSite1974)
HAnimSite1975 = x3d.HAnimSite()
HAnimSite1975.USE = "hanim_r_metacarpal_phalanx_2_pt"

HAnimHumanoid43.sites.append(HAnimSite1975)
HAnimSite1976 = x3d.HAnimSite()
HAnimSite1976.USE = "hanim_r_carpal_distal_phalanx_2_tip"

HAnimHumanoid43.sites.append(HAnimSite1976)
HAnimSite1977 = x3d.HAnimSite()
HAnimSite1977.USE = "hanim_r_dactylion_pt"

HAnimHumanoid43.sites.append(HAnimSite1977)
HAnimSite1978 = x3d.HAnimSite()
HAnimSite1978.USE = "hanim_r_metacarpal_phalanx_3_pt"

HAnimHumanoid43.sites.append(HAnimSite1978)
HAnimSite1979 = x3d.HAnimSite()
HAnimSite1979.USE = "hanim_r_carpal_distal_phalanx_3_tip"

HAnimHumanoid43.sites.append(HAnimSite1979)
HAnimSite1980 = x3d.HAnimSite()
HAnimSite1980.USE = "hanim_r_metacarpal_phalanx_5_pt"

HAnimHumanoid43.sites.append(HAnimSite1980)
HAnimSite1981 = x3d.HAnimSite()
HAnimSite1981.USE = "hanim_r_carpal_distal_phalanx_4_tip"

HAnimHumanoid43.sites.append(HAnimSite1981)
HAnimSite1982 = x3d.HAnimSite()
HAnimSite1982.USE = "hanim_r_carpal_distal_phalanx_5_tip"

HAnimHumanoid43.sites.append(HAnimSite1982)

Scene11.children.append(HAnimHumanoid43)

X3D0.Scene = Scene11
f = open("././Humanoid4.1_RoundTrip.x3d", "w")
f.write(X3D0.XML())
f.close()
