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
NavigationInfo11 = x3d.NavigationInfo()
NavigationInfo11.speed = 1.5
NavigationInfo11.type = ["EXAMINE","ANY"]

Scene10.children.append(NavigationInfo11)
Viewpoint12 = x3d.Viewpoint()
Viewpoint12.centerOfRotation = [0,1,0]
Viewpoint12.description = "JohnBoy"
Viewpoint12.position = [0,1,3]

Scene10.children.append(Viewpoint12)
HAnimHumanoid13 = x3d.HAnimHumanoid()
HAnimHumanoid13.DEF = "STD_HAnim"
HAnimHumanoid13.info = ["humanoidVersion=2.0"]
HAnimHumanoid13.name = "HAnim"
HAnimHumanoid13.version = "2.0"
""" scale='0.0225 0.0225 0.0225' """
HAnimJoint14 = x3d.HAnimJoint()
HAnimJoint14.DEF = "STD_Joint_humanoid_root"
HAnimJoint14.name = "humanoid_root"
HAnimJoint14.center = [0.0000,0.8240,0.0277]
HAnimSegment15 = x3d.HAnimSegment()
HAnimSegment15.DEF = "STD_HAnimSegment_HumanoidRoot"
HAnimSegment15.name = "HAnimSegment_HumanoidRoot"
Viewpoint16 = x3d.Viewpoint()
Viewpoint16.description = "View from (0 0 4) towards HAnimHumanoid center"
Viewpoint16.position = [0,0,4]

HAnimSegment15.children.append(Viewpoint16)
Switch17 = x3d.Switch()
Switch17.whichChoice = 0
Transform18 = x3d.Transform()
Transform18.scale = [0.0225,0.0225,0.0225]
TouchSensor19 = x3d.TouchSensor()
TouchSensor19.description = "HAnimHumanoid HAnimSegment HumanoidRoot"

Transform18.children.append(TouchSensor19)
Shape20 = x3d.Shape()
Shape20.DEF = "HAnimRootShape"
Sphere21 = x3d.Sphere()
Sphere21.DEF = "HAnimJointSphere"

Shape20.geometry = Sphere21
Appearance22 = x3d.Appearance()
Material23 = x3d.Material()
Material23.DEF = "HAnimRootMaterial"
Material23.diffuseColor = [0.8,0,0]
Material23.transparency = 0.3

Appearance22.material = Material23

Shape20.appearance = Appearance22

Transform18.children.append(Shape20)

Switch17.children.append(Transform18)
Shape24 = x3d.Shape()
Shape24.DEF = "HAnimJointShape"
Sphere25 = x3d.Sphere()
Sphere25.USE = "HAnimJointSphere"

Shape24.geometry = Sphere25
Appearance26 = x3d.Appearance()
Material27 = x3d.Material()
Material27.DEF = "HAnimJointMaterial"
Material27.diffuseColor = [0,0,0.8]
Material27.transparency = 0.3

Appearance26.material = Material27

Shape24.appearance = Appearance26

Switch17.children.append(Shape24)
Shape28 = x3d.Shape()
LineSet29 = x3d.LineSet()
LineSet29.vertexCount = [2]
ColorRGBA30 = x3d.ColorRGBA()
ColorRGBA30.DEF = "HAnimSegmentLineColorRGBA"

LineSet29.color = ColorRGBA30
Coordinate31 = x3d.Coordinate()

LineSet29.coord = Coordinate31

Shape28.geometry = LineSet29

Switch17.children.append(Shape28)
Shape32 = x3d.Shape()
Shape32.DEF = "HAnimSiteShape"
IndexedFaceSet33 = x3d.IndexedFaceSet()
IndexedFaceSet33.DEF = "DiamondIFS"
IndexedFaceSet33.creaseAngle = 0.5
IndexedFaceSet33.solid = False
IndexedFaceSet33.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
ColorRGBA34 = x3d.ColorRGBA()
ColorRGBA34.DEF = "HAnimSiteColorRGBA"

IndexedFaceSet33.color = ColorRGBA34
Coordinate35 = x3d.Coordinate()

IndexedFaceSet33.coord = Coordinate35

Shape32.geometry = IndexedFaceSet33
Appearance36 = x3d.Appearance()
Material37 = x3d.Material()
Material37.diffuseColor = [1,1,0]
Material37.transparency = 0.3

Appearance36.material = Material37

Shape32.appearance = Appearance36

Switch17.children.append(Shape32)

HAnimSegment15.children.append(Switch17)

HAnimJoint14.children.append(HAnimSegment15)
HAnimSegment38 = x3d.HAnimSegment()
HAnimSegment38.DEF = "STD_Segment_sacrum"
HAnimSegment38.name = "sacrum"

HAnimJoint14.children.append(HAnimSegment38)
HAnimJoint39 = x3d.HAnimJoint()
HAnimJoint39.DEF = "STD_Joint_sacroiliac"
HAnimJoint39.name = "sacroiliac"
HAnimJoint39.center = [0.0000,0.9149,0.0016]
HAnimSegment40 = x3d.HAnimSegment()
HAnimSegment40.DEF = "STD_Segment_pelvis"
HAnimSegment40.name = "pelvis"
HAnimSite41 = x3d.HAnimSite()
HAnimSite41.DEF = "STD_Site_buttocks_standing_wall_contact_point_pt"
HAnimSite41.name = "buttocks_standing_wall_contact_point_pt"
HAnimSite41.scale = [0.0225,0.0225,0.0225]
TouchSensor42 = x3d.TouchSensor()
TouchSensor42.description = "HAnimSite buttocks_standing_wall_contact_point_pt"

HAnimSite41.children.append(TouchSensor42)
Shape43 = x3d.Shape()
Shape43.USE = "HAnimSiteShape"

HAnimSite41.children.append(Shape43)

HAnimSegment40.children.append(HAnimSite41)
HAnimSite44 = x3d.HAnimSite()
HAnimSite44.DEF = "STD_Site_r_psis_pt"
HAnimSite44.name = "r_psis_pt"
HAnimSite44.scale = [0.0225,0.0225,0.0225]
HAnimSite44.translation = [-0.0716,1.0190,-0.1138]
TouchSensor45 = x3d.TouchSensor()
TouchSensor45.description = "HAnimSite r_psis_pt"

HAnimSite44.children.append(TouchSensor45)
Shape46 = x3d.Shape()
Shape46.USE = "HAnimSiteShape"

HAnimSite44.children.append(Shape46)

HAnimSegment40.children.append(HAnimSite44)
HAnimSite47 = x3d.HAnimSite()
HAnimSite47.DEF = "STD_Site_crotch_pt"
HAnimSite47.name = "crotch_pt"
HAnimSite47.scale = [0.0225,0.0225,0.0225]
HAnimSite47.translation = [0.0034,0.8266,0.0257]
TouchSensor48 = x3d.TouchSensor()
TouchSensor48.description = "HAnimSite crotch_pt"

HAnimSite47.children.append(TouchSensor48)
Shape49 = x3d.Shape()
Shape49.USE = "HAnimSiteShape"

HAnimSite47.children.append(Shape49)

HAnimSegment40.children.append(HAnimSite47)
HAnimSite50 = x3d.HAnimSite()
HAnimSite50.DEF = "STD_Site_l_psis_pt"
HAnimSite50.name = "l_psis_pt"
HAnimSite50.scale = [0.0225,0.0225,0.0225]
HAnimSite50.translation = [0.0774,1.0190,-0.1151]
TouchSensor51 = x3d.TouchSensor()
TouchSensor51.description = "HAnimSite l_psis_pt"

HAnimSite50.children.append(TouchSensor51)
Shape52 = x3d.Shape()
Shape52.USE = "HAnimSiteShape"

HAnimSite50.children.append(Shape52)

HAnimSegment40.children.append(HAnimSite50)
HAnimSite53 = x3d.HAnimSite()
HAnimSite53.DEF = "STD_Site_r_iliocristale_pt"
HAnimSite53.name = "r_iliocristale_pt"
HAnimSite53.scale = [0.0225,0.0225,0.0225]
HAnimSite53.translation = [-0.1525,1.0628,0.0035]
TouchSensor54 = x3d.TouchSensor()
TouchSensor54.description = "HAnimSite r_iliocristale_pt"

HAnimSite53.children.append(TouchSensor54)
Shape55 = x3d.Shape()
Shape55.USE = "HAnimSiteShape"

HAnimSite53.children.append(Shape55)

HAnimSegment40.children.append(HAnimSite53)
HAnimSite56 = x3d.HAnimSite()
HAnimSite56.DEF = "STD_Site_r_asis_pt"
HAnimSite56.name = "r_asis_pt"
HAnimSite56.scale = [0.0225,0.0225,0.0225]
HAnimSite56.translation = [-0.0887,1.0021,0.1112]
TouchSensor57 = x3d.TouchSensor()
TouchSensor57.description = "HAnimSite r_asis_pt"

HAnimSite56.children.append(TouchSensor57)
Shape58 = x3d.Shape()
Shape58.USE = "HAnimSiteShape"

HAnimSite56.children.append(Shape58)

HAnimSegment40.children.append(HAnimSite56)
HAnimSite59 = x3d.HAnimSite()
HAnimSite59.DEF = "STD_Site_l_iliocristale_pt"
HAnimSite59.name = "l_iliocristale_pt"
HAnimSite59.scale = [0.0225,0.0225,0.0225]
HAnimSite59.translation = [0.1612,1.0537,0.0008]
TouchSensor60 = x3d.TouchSensor()
TouchSensor60.description = "HAnimSite l_iliocristale_pt"

HAnimSite59.children.append(TouchSensor60)
Shape61 = x3d.Shape()
Shape61.USE = "HAnimSiteShape"

HAnimSite59.children.append(Shape61)

HAnimSegment40.children.append(HAnimSite59)
HAnimSite62 = x3d.HAnimSite()
HAnimSite62.DEF = "STD_Site_l_asis_pt"
HAnimSite62.name = "l_asis_pt"
HAnimSite62.scale = [0.0225,0.0225,0.0225]
HAnimSite62.translation = [0.0925,0.9983,0.1052]
TouchSensor63 = x3d.TouchSensor()
TouchSensor63.description = "HAnimSite l_asis_pt"

HAnimSite62.children.append(TouchSensor63)
Shape64 = x3d.Shape()
Shape64.USE = "HAnimSiteShape"

HAnimSite62.children.append(Shape64)

HAnimSegment40.children.append(HAnimSite62)
HAnimSite65 = x3d.HAnimSite()
HAnimSite65.DEF = "STD_Site_l_trochanterion_pt"
HAnimSite65.name = "l_trochanterion_pt"
HAnimSite65.scale = [0.0225,0.0225,0.0225]
HAnimSite65.translation = [0.1677,0.8336,0.0303]
TouchSensor66 = x3d.TouchSensor()
TouchSensor66.description = "HAnimSite l_trochanterion_pt"

HAnimSite65.children.append(TouchSensor66)
Shape67 = x3d.Shape()
Shape67.USE = "HAnimSiteShape"

HAnimSite65.children.append(Shape67)

HAnimSegment40.children.append(HAnimSite65)
HAnimSite68 = x3d.HAnimSite()
HAnimSite68.DEF = "STD_Site_r_trochanterion_pt"
HAnimSite68.name = "r_trochanterion_pt"
HAnimSite68.scale = [0.0225,0.0225,0.0225]
HAnimSite68.translation = [-0.1689,0.8419,0.0352]
TouchSensor69 = x3d.TouchSensor()
TouchSensor69.description = "HAnimSite r_trochanterion_pt"

HAnimSite68.children.append(TouchSensor69)
Shape70 = x3d.Shape()
Shape70.USE = "HAnimSiteShape"

HAnimSite68.children.append(Shape70)

HAnimSegment40.children.append(HAnimSite68)

HAnimJoint39.children.append(HAnimSegment40)
HAnimJoint71 = x3d.HAnimJoint()
HAnimJoint71.DEF = "STD_Joint_l_hip"
HAnimJoint71.name = "l_hip"
HAnimJoint71.center = [0.0961,0.9124,-0.0001]
HAnimSegment72 = x3d.HAnimSegment()
HAnimSegment72.DEF = "STD_Segment_l_thigh"
HAnimSegment72.name = "l_thigh"
HAnimSite73 = x3d.HAnimSite()
HAnimSite73.DEF = "STD_Site_l_femoral_medial_epicondyles_pt"
HAnimSite73.name = "l_femoral_medial_epicondyles_pt"
HAnimSite73.scale = [0.0225,0.0225,0.0225]
HAnimSite73.translation = [0.0398,0.4946,0.0303]
TouchSensor74 = x3d.TouchSensor()
TouchSensor74.description = "HAnimSite l_femoral_medial_epicondyles_pt"

HAnimSite73.children.append(TouchSensor74)
Shape75 = x3d.Shape()
Shape75.USE = "HAnimSiteShape"

HAnimSite73.children.append(Shape75)

HAnimSegment72.children.append(HAnimSite73)
HAnimSite76 = x3d.HAnimSite()
HAnimSite76.DEF = "STD_Site_l_knee_crease_pt"
HAnimSite76.name = "l_knee_crease_pt"
HAnimSite76.scale = [0.0225,0.0225,0.0225]
HAnimSite76.translation = [0.0993,0.4881,-0.0309]
TouchSensor77 = x3d.TouchSensor()
TouchSensor77.description = "HAnimSite l_knee_crease_pt"

HAnimSite76.children.append(TouchSensor77)
Shape78 = x3d.Shape()
Shape78.USE = "HAnimSiteShape"

HAnimSite76.children.append(Shape78)

HAnimSegment72.children.append(HAnimSite76)
HAnimSite79 = x3d.HAnimSite()
HAnimSite79.DEF = "STD_Site_l_femoral_lateral_epicondyles_pt"
HAnimSite79.name = "l_femoral_lateral_epicondyles_pt"
HAnimSite79.scale = [0.0225,0.0225,0.0225]
HAnimSite79.translation = [0.1598,0.4967,0.0297]
TouchSensor80 = x3d.TouchSensor()
TouchSensor80.description = "HAnimSite l_femoral_lateral_epicondyles_pt"

HAnimSite79.children.append(TouchSensor80)
Shape81 = x3d.Shape()
Shape81.USE = "HAnimSiteShape"

HAnimSite79.children.append(Shape81)

HAnimSegment72.children.append(HAnimSite79)
HAnimSite82 = x3d.HAnimSite()
HAnimSite82.DEF = "STD_Site_l_suprapatella_pt"
HAnimSite82.name = "l_suprapatella_pt"
HAnimSite82.scale = [0.0225,0.0225,0.0225]
TouchSensor83 = x3d.TouchSensor()
TouchSensor83.description = "HAnimSite l_suprapatella_pt"

HAnimSite82.children.append(TouchSensor83)
Shape84 = x3d.Shape()
Shape84.USE = "HAnimSiteShape"

HAnimSite82.children.append(Shape84)

HAnimSegment72.children.append(HAnimSite82)

HAnimJoint71.children.append(HAnimSegment72)
HAnimJoint85 = x3d.HAnimJoint()
HAnimJoint85.DEF = "STD_Joint_l_knee"
HAnimJoint85.name = "l_knee"
HAnimJoint85.center = [0.1040,0.4867,0.0308]
HAnimSegment86 = x3d.HAnimSegment()
HAnimSegment86.DEF = "STD_Segment_l_calf"
HAnimSegment86.name = "l_calf"
HAnimSite87 = x3d.HAnimSite()
HAnimSite87.DEF = "STD_Site_l_lateral_malleolus_pt"
HAnimSite87.name = "l_lateral_malleolus_pt"
HAnimSite87.scale = [0.0225,0.0225,0.0225]
HAnimSite87.translation = [0.1308,0.0597,-0.1032]
TouchSensor88 = x3d.TouchSensor()
TouchSensor88.description = "HAnimSite l_lateral_malleolus_pt"

HAnimSite87.children.append(TouchSensor88)
Shape89 = x3d.Shape()
Shape89.USE = "HAnimSiteShape"

HAnimSite87.children.append(Shape89)

HAnimSegment86.children.append(HAnimSite87)
HAnimSite90 = x3d.HAnimSite()
HAnimSite90.DEF = "STD_Site_l_medial_malleolus_pt"
HAnimSite90.name = "l_medial_malleolus_pt"
HAnimSite90.scale = [0.0225,0.0225,0.0225]
HAnimSite90.translation = [0.0890,0.0716,-0.0881]
TouchSensor91 = x3d.TouchSensor()
TouchSensor91.description = "HAnimSite l_medial_malleolus_pt"

HAnimSite90.children.append(TouchSensor91)
Shape92 = x3d.Shape()
Shape92.USE = "HAnimSiteShape"

HAnimSite90.children.append(Shape92)

HAnimSegment86.children.append(HAnimSite90)
HAnimSite93 = x3d.HAnimSite()
HAnimSite93.DEF = "STD_Site_l_tibiale_pt"
HAnimSite93.name = "l_tibiale_pt"
HAnimSite93.scale = [0.0225,0.0225,0.0225]
TouchSensor94 = x3d.TouchSensor()
TouchSensor94.description = "HAnimSite l_tibiale_pt"

HAnimSite93.children.append(TouchSensor94)
Shape95 = x3d.Shape()
Shape95.USE = "HAnimSiteShape"

HAnimSite93.children.append(Shape95)

HAnimSegment86.children.append(HAnimSite93)

HAnimJoint85.children.append(HAnimSegment86)
HAnimJoint96 = x3d.HAnimJoint()
HAnimJoint96.DEF = "STD_Joint_l_talocrural"
HAnimJoint96.name = "l_talocrural"
HAnimJoint96.center = [0.1101,0.0656,-0.0736]
HAnimSegment97 = x3d.HAnimSegment()
HAnimSegment97.DEF = "STD_Segment_l_talus"
HAnimSegment97.name = "l_talus"
HAnimSite98 = x3d.HAnimSite()
HAnimSite98.DEF = "STD_Site_l_sphyrion_pt"
HAnimSite98.name = "l_sphyrion_pt"
HAnimSite98.scale = [0.0225,0.0225,0.0225]
HAnimSite98.translation = [0.0890,0.0575,-0.0943]
TouchSensor99 = x3d.TouchSensor()
TouchSensor99.description = "HAnimSite l_sphyrion_pt"

HAnimSite98.children.append(TouchSensor99)
Shape100 = x3d.Shape()
Shape100.USE = "HAnimSiteShape"

HAnimSite98.children.append(Shape100)

HAnimSegment97.children.append(HAnimSite98)
HAnimSite101 = x3d.HAnimSite()
HAnimSite101.DEF = "STD_Site_l_calcaneus_posterior_pt"
HAnimSite101.name = "l_calcaneus_posterior_pt"
HAnimSite101.scale = [0.0225,0.0225,0.0225]
HAnimSite101.translation = [0.0974,0.0259,-0.1171]
TouchSensor102 = x3d.TouchSensor()
TouchSensor102.description = "HAnimSite l_calcaneus_posterior_pt"

HAnimSite101.children.append(TouchSensor102)
Shape103 = x3d.Shape()
Shape103.USE = "HAnimSiteShape"

HAnimSite101.children.append(Shape103)

HAnimSegment97.children.append(HAnimSite101)

HAnimJoint96.children.append(HAnimSegment97)
HAnimJoint104 = x3d.HAnimJoint()
HAnimJoint104.DEF = "STD_Joint_l_talocalcaneonavicular"
HAnimJoint104.name = "l_talocalcaneonavicular"
HAnimJoint104.center = [0,0,0]
HAnimSegment105 = x3d.HAnimSegment()
HAnimSegment105.DEF = "STD_Segment_l_navicular"
HAnimSegment105.name = "l_navicular"

HAnimJoint104.children.append(HAnimSegment105)
HAnimJoint106 = x3d.HAnimJoint()
HAnimJoint106.DEF = "STD_Joint_l_cuneonavicular_1"
HAnimJoint106.name = "l_cuneonavicular_1"
HAnimJoint106.center = [0,0,0]
HAnimSegment107 = x3d.HAnimSegment()
HAnimSegment107.DEF = "STD_Segment_l_cuneiform_1"
HAnimSegment107.name = "l_cuneiform_1"

HAnimJoint106.children.append(HAnimSegment107)
HAnimJoint108 = x3d.HAnimJoint()
HAnimJoint108.DEF = "STD_Joint_l_tarsometatarsal_1"
HAnimJoint108.name = "l_tarsometatarsal_1"
HAnimJoint108.center = [0,0,0]
HAnimSegment109 = x3d.HAnimSegment()
HAnimSegment109.DEF = "STD_Segment_l_metatarsal_1"
HAnimSegment109.name = "l_metatarsal_1"

HAnimJoint108.children.append(HAnimSegment109)
HAnimJoint110 = x3d.HAnimJoint()
HAnimJoint110.DEF = "STD_Joint_l_metatarsophalangeal_1"
HAnimJoint110.name = "l_metatarsophalangeal_1"
HAnimJoint110.center = [0,0,0]
HAnimSegment111 = x3d.HAnimSegment()
HAnimSegment111.DEF = "STD_Segment_l_tarsal_proximal_phalanx_1"
HAnimSegment111.name = "l_tarsal_proximal_phalanx_1"
HAnimSite112 = x3d.HAnimSite()
HAnimSite112.DEF = "STD_Site_l_metatarsal_phalanx_1_pt"
HAnimSite112.name = "l_metatarsal_phalanx_1_pt"
HAnimSite112.scale = [0.0225,0.0225,0.0225]
TouchSensor113 = x3d.TouchSensor()
TouchSensor113.description = "HAnimSite l_metatarsal_phalanx_1_pt"

HAnimSite112.children.append(TouchSensor113)
Shape114 = x3d.Shape()
Shape114.USE = "HAnimSiteShape"

HAnimSite112.children.append(Shape114)

HAnimSegment111.children.append(HAnimSite112)

HAnimJoint110.children.append(HAnimSegment111)
HAnimJoint115 = x3d.HAnimJoint()
HAnimJoint115.DEF = "STD_Joint_l_tarsal_interphalangeal_1"
HAnimJoint115.name = "l_tarsal_interphalangeal_1"
HAnimJoint115.center = [0,0,0]
HAnimSegment116 = x3d.HAnimSegment()
HAnimSegment116.DEF = "STD_Segment_l_tarsal_distal_phalanx_1"
HAnimSegment116.name = "l_tarsal_distal_phalanx_1"
HAnimSite117 = x3d.HAnimSite()
HAnimSite117.DEF = "STD_Site_l_tarsal_distal_phalanx_1_tip"
HAnimSite117.name = "l_tarsal_distal_phalanx_1_tip"
HAnimSite117.scale = [0.0225,0.0225,0.0225]
TouchSensor118 = x3d.TouchSensor()
TouchSensor118.description = "HAnimSite l_tarsal_distal_phalanx_1_tip"

HAnimSite117.children.append(TouchSensor118)
Shape119 = x3d.Shape()
Shape119.USE = "HAnimSiteShape"

HAnimSite117.children.append(Shape119)

HAnimSegment116.children.append(HAnimSite117)

HAnimJoint115.children.append(HAnimSegment116)

HAnimJoint110.children.append(HAnimJoint115)

HAnimJoint108.children.append(HAnimJoint110)

HAnimJoint106.children.append(HAnimJoint108)

HAnimJoint104.children.append(HAnimJoint106)
HAnimJoint120 = x3d.HAnimJoint()
HAnimJoint120.DEF = "STD_Joint_l_cuneonavicular_2"
HAnimJoint120.name = "l_cuneonavicular_2"
HAnimJoint120.center = [0,0,0]
HAnimSegment121 = x3d.HAnimSegment()
HAnimSegment121.DEF = "STD_Segment_l_cuneiform_2"
HAnimSegment121.name = "l_cuneiform_2"

HAnimJoint120.children.append(HAnimSegment121)
HAnimJoint122 = x3d.HAnimJoint()
HAnimJoint122.DEF = "STD_Joint_l_tarsometatarsal_2"
HAnimJoint122.name = "l_tarsometatarsal_2"
HAnimJoint122.center = [0,0,0]
HAnimSegment123 = x3d.HAnimSegment()
HAnimSegment123.DEF = "STD_Segment_l_metatarsal_2"
HAnimSegment123.name = "l_metatarsal_2"

HAnimJoint122.children.append(HAnimSegment123)
HAnimJoint124 = x3d.HAnimJoint()
HAnimJoint124.DEF = "STD_Joint_l_metatarsophalangeal_2"
HAnimJoint124.name = "l_metatarsophalangeal_2"
HAnimJoint124.center = [0,0,0]
HAnimSegment125 = x3d.HAnimSegment()
HAnimSegment125.DEF = "STD_Segment_l_tarsal_proximal_phalanx_2"
HAnimSegment125.name = "l_tarsal_proximal_phalanx_2"

HAnimJoint124.children.append(HAnimSegment125)
HAnimJoint126 = x3d.HAnimJoint()
HAnimJoint126.DEF = "STD_Joint_l_tarsal_proximal_interphalangeal_2"
HAnimJoint126.name = "l_tarsal_proximal_interphalangeal_2"
HAnimJoint126.center = [0,0,0]
HAnimSegment127 = x3d.HAnimSegment()
HAnimSegment127.DEF = "STD_Segment_l_tarsal_middle_phalanx_2"
HAnimSegment127.name = "l_tarsal_middle_phalanx_2"

HAnimJoint126.children.append(HAnimSegment127)
HAnimJoint128 = x3d.HAnimJoint()
HAnimJoint128.DEF = "STD_Joint_l_tarsal_distal_interphalangeal_2"
HAnimJoint128.name = "l_tarsal_distal_interphalangeal_2"
HAnimJoint128.center = [0,0,0]
HAnimSegment129 = x3d.HAnimSegment()
HAnimSegment129.DEF = "STD_Segment_l_tarsal_distal_phalanx_2"
HAnimSegment129.name = "l_tarsal_distal_phalanx_2"
HAnimSite130 = x3d.HAnimSite()
HAnimSite130.DEF = "STD_Site_l_tarsal_distal_phalanx_2_tip"
HAnimSite130.name = "l_tarsal_distal_phalanx_2_tip"
HAnimSite130.scale = [0.0225,0.0225,0.0225]
HAnimSite130.translation = [0.1195,0.0079,0.1433]
TouchSensor131 = x3d.TouchSensor()
TouchSensor131.description = "HAnimSite l_tarsal_distal_phalanx_2_tip"

HAnimSite130.children.append(TouchSensor131)
Shape132 = x3d.Shape()
Shape132.USE = "HAnimSiteShape"

HAnimSite130.children.append(Shape132)

HAnimSegment129.children.append(HAnimSite130)

HAnimJoint128.children.append(HAnimSegment129)

HAnimJoint126.children.append(HAnimJoint128)

HAnimJoint124.children.append(HAnimJoint126)

HAnimJoint122.children.append(HAnimJoint124)

HAnimJoint120.children.append(HAnimJoint122)

HAnimJoint104.children.append(HAnimJoint120)
HAnimJoint133 = x3d.HAnimJoint()
HAnimJoint133.DEF = "STD_Joint_l_cuneonavicular_3"
HAnimJoint133.name = "l_cuneonavicular_3"
HAnimJoint133.center = [0,0,0]
HAnimSegment134 = x3d.HAnimSegment()
HAnimSegment134.DEF = "STD_Segment_l_cuneiform_3"
HAnimSegment134.name = "l_cuneiform_3"

HAnimJoint133.children.append(HAnimSegment134)
HAnimJoint135 = x3d.HAnimJoint()
HAnimJoint135.DEF = "STD_Joint_l_tarsometatarsal_3 "
HAnimJoint135.name = "l_tarsometatarsal_3 "
HAnimJoint135.center = [0,0,0]
HAnimSegment136 = x3d.HAnimSegment()
HAnimSegment136.DEF = "STD_Segment_l_metatarsal_3"
HAnimSegment136.name = "l_metatarsal_3"

HAnimJoint135.children.append(HAnimSegment136)
HAnimJoint137 = x3d.HAnimJoint()
HAnimJoint137.DEF = "STD_Joint_l_metatarsophalangeal_3"
HAnimJoint137.name = "l_metatarsophalangeal_3"
HAnimJoint137.center = [0,0,0]
HAnimSegment138 = x3d.HAnimSegment()
HAnimSegment138.DEF = "STD_Segment_l_tarsal_proximal_phalanx_3"
HAnimSegment138.name = "l_tarsal_proximal_phalanx_3"

HAnimJoint137.children.append(HAnimSegment138)
HAnimJoint139 = x3d.HAnimJoint()
HAnimJoint139.DEF = "STD_Joint_l_tarsal_proximal_interphalangeal_3"
HAnimJoint139.name = "l_tarsal_proximal_interphalangeal_3"
HAnimJoint139.center = [0,0,0]
HAnimSegment140 = x3d.HAnimSegment()
HAnimSegment140.DEF = "STD_Segment_l_tarsal_middle_phalanx_3"
HAnimSegment140.name = "l_tarsal_middle_phalanx_3"

HAnimJoint139.children.append(HAnimSegment140)
HAnimJoint141 = x3d.HAnimJoint()
HAnimJoint141.DEF = "STD_Joint_l_tarsal_distal_interphalangeal_3"
HAnimJoint141.name = "l_tarsal_distal_interphalangeal_3"
HAnimJoint141.center = [0,0,0]
HAnimSegment142 = x3d.HAnimSegment()
HAnimSegment142.DEF = "STD_Segment_l_tarsal_distal_phalanx_3"
HAnimSegment142.name = "l_tarsal_distal_phalanx_3"
HAnimSite143 = x3d.HAnimSite()
HAnimSite143.DEF = "STD_Site_l_tarsal_distal_phalanx_3_tip"
HAnimSite143.name = "l_tarsal_distal_phalanx_3_tip"
HAnimSite143.scale = [0.0225,0.0225,0.0225]
TouchSensor144 = x3d.TouchSensor()
TouchSensor144.description = "HAnimSite l_tarsal_distal_phalanx_3_tip"

HAnimSite143.children.append(TouchSensor144)
Shape145 = x3d.Shape()
Shape145.USE = "HAnimSiteShape"

HAnimSite143.children.append(Shape145)

HAnimSegment142.children.append(HAnimSite143)

HAnimJoint141.children.append(HAnimSegment142)

HAnimJoint139.children.append(HAnimJoint141)

HAnimJoint137.children.append(HAnimJoint139)

HAnimJoint135.children.append(HAnimJoint137)

HAnimJoint133.children.append(HAnimJoint135)

HAnimJoint104.children.append(HAnimJoint133)

HAnimJoint96.children.append(HAnimJoint104)
HAnimJoint146 = x3d.HAnimJoint()
HAnimJoint146.DEF = "STD_Joint_l_calcaneocuboid"
HAnimJoint146.name = "l_calcaneocuboid"
HAnimJoint146.center = [0,0,0]
HAnimSegment147 = x3d.HAnimSegment()
HAnimSegment147.DEF = "STD_Segment_l_calcaneus"
HAnimSegment147.name = "l_calcaneus"

HAnimJoint146.children.append(HAnimSegment147)
HAnimJoint148 = x3d.HAnimJoint()
HAnimJoint148.DEF = "STD_Joint_l_transversetarsal"
HAnimJoint148.name = "l_transversetarsal"
HAnimJoint148.center = [0,0,0]
HAnimSegment149 = x3d.HAnimSegment()
HAnimSegment149.DEF = "STD_Segment_l_cuboid"
HAnimSegment149.name = "l_cuboid"

HAnimJoint148.children.append(HAnimSegment149)
HAnimJoint150 = x3d.HAnimJoint()
HAnimJoint150.DEF = "STD_Joint_l_tarsometatarsal_4"
HAnimJoint150.name = "l_tarsometatarsal_4"
HAnimJoint150.center = [0,0,0]
HAnimSegment151 = x3d.HAnimSegment()
HAnimSegment151.DEF = "STD_Segment_l_metatarsal_4"
HAnimSegment151.name = "l_metatarsal_4"

HAnimJoint150.children.append(HAnimSegment151)
HAnimJoint152 = x3d.HAnimJoint()
HAnimJoint152.DEF = "STD_Joint_l_metatarsophalangeal_4"
HAnimJoint152.name = "l_metatarsophalangeal_4"
HAnimJoint152.center = [0,0,0]
HAnimSegment153 = x3d.HAnimSegment()
HAnimSegment153.DEF = "STD_Segment_l_tarsal_proximal_phalanx_4"
HAnimSegment153.name = "l_tarsal_proximal_phalanx_4"

HAnimJoint152.children.append(HAnimSegment153)
HAnimJoint154 = x3d.HAnimJoint()
HAnimJoint154.DEF = "STD_Joint_l_tarsal_proximal_interphalangeal_4"
HAnimJoint154.name = "l_tarsal_proximal_interphalangeal_4"
HAnimJoint154.center = [0,0,0]
HAnimSegment155 = x3d.HAnimSegment()
HAnimSegment155.DEF = "STD_Segment_l_tarsal_middle_phalanx_4"
HAnimSegment155.name = "l_tarsal_middle_phalanx_4"

HAnimJoint154.children.append(HAnimSegment155)
HAnimJoint156 = x3d.HAnimJoint()
HAnimJoint156.DEF = "STD_Joint_l_tarsal_distal_interphalangeal_4"
HAnimJoint156.name = "l_tarsal_distal_interphalangeal_4"
HAnimJoint156.center = [0,0,0]
HAnimSegment157 = x3d.HAnimSegment()
HAnimSegment157.DEF = "STD_Segment_l_tarsal_distal_phalanx_4"
HAnimSegment157.name = "l_tarsal_distal_phalanx_4"
HAnimSite158 = x3d.HAnimSite()
HAnimSite158.DEF = "STD_Site_l_tarsal_distal_phalanx_4_tip"
HAnimSite158.name = "l_tarsal_distal_phalanx_4_tip"
HAnimSite158.scale = [0.0225,0.0225,0.0225]
TouchSensor159 = x3d.TouchSensor()
TouchSensor159.description = "HAnimSite l_tarsal_distal_phalanx_4_tip"

HAnimSite158.children.append(TouchSensor159)
Shape160 = x3d.Shape()
Shape160.USE = "HAnimSiteShape"

HAnimSite158.children.append(Shape160)

HAnimSegment157.children.append(HAnimSite158)

HAnimJoint156.children.append(HAnimSegment157)

HAnimJoint154.children.append(HAnimJoint156)

HAnimJoint152.children.append(HAnimJoint154)

HAnimJoint150.children.append(HAnimJoint152)

HAnimJoint148.children.append(HAnimJoint150)
HAnimJoint161 = x3d.HAnimJoint()
HAnimJoint161.DEF = "STD_Joint_l_tarsometatarsal_5"
HAnimJoint161.name = "l_tarsometatarsal_5"
HAnimJoint161.center = [0,0,0]
HAnimSegment162 = x3d.HAnimSegment()
HAnimSegment162.DEF = "STD_Segment_l_metatarsal_5"
HAnimSegment162.name = "l_metatarsal_5"

HAnimJoint161.children.append(HAnimSegment162)
HAnimJoint163 = x3d.HAnimJoint()
HAnimJoint163.DEF = "STD_Joint_l_metatarsophalangeal_5"
HAnimJoint163.name = "l_metatarsophalangeal_5"
HAnimJoint163.center = [0,0,0]
HAnimSegment164 = x3d.HAnimSegment()
HAnimSegment164.DEF = "STD_Segment_l_tarsal_proximal_phalanx_5"
HAnimSegment164.name = "l_tarsal_proximal_phalanx_5"
HAnimSite165 = x3d.HAnimSite()
HAnimSite165.DEF = "STD_Site_l_metatarsal_phalanx_5_pt"
HAnimSite165.name = "l_metatarsal_phalanx_5_pt"
HAnimSite165.scale = [0.0225,0.0225,0.0225]
TouchSensor166 = x3d.TouchSensor()
TouchSensor166.description = "HAnimSite l_metatarsal_phalanx_5_pt"

HAnimSite165.children.append(TouchSensor166)
Shape167 = x3d.Shape()
Shape167.USE = "HAnimSiteShape"

HAnimSite165.children.append(Shape167)

HAnimSegment164.children.append(HAnimSite165)

HAnimJoint163.children.append(HAnimSegment164)
HAnimJoint168 = x3d.HAnimJoint()
HAnimJoint168.DEF = "STD_Joint_l_tarsal_proximal_interphalangeal_5"
HAnimJoint168.name = "l_tarsal_proximal_interphalangeal_5"
HAnimJoint168.center = [0,0,0]
HAnimSegment169 = x3d.HAnimSegment()
HAnimSegment169.DEF = "STD_Segment_l_tarsal_middle_phalanx_5"
HAnimSegment169.name = "l_tarsal_middle_phalanx_5"

HAnimJoint168.children.append(HAnimSegment169)
HAnimJoint170 = x3d.HAnimJoint()
HAnimJoint170.DEF = "STD_Joint_l_tarsal_distal_interphalangeal_5"
HAnimJoint170.name = "l_tarsal_distal_interphalangeal_5"
HAnimJoint170.center = [0,0,0]
HAnimSegment171 = x3d.HAnimSegment()
HAnimSegment171.DEF = "STD_Segment_l_tarsal_distal_phalanx_5"
HAnimSegment171.name = "l_tarsal_distal_phalanx_5"
HAnimSite172 = x3d.HAnimSite()
HAnimSite172.DEF = "STD_Site_l_tarsal_distal_phalanx_5_tip"
HAnimSite172.name = "l_tarsal_distal_phalanx_5_tip"
HAnimSite172.scale = [0.0225,0.0225,0.0225]
TouchSensor173 = x3d.TouchSensor()
TouchSensor173.description = "HAnimSite l_tarsal_distal_phalanx_5_tip"

HAnimSite172.children.append(TouchSensor173)
Shape174 = x3d.Shape()
Shape174.USE = "HAnimSiteShape"

HAnimSite172.children.append(Shape174)

HAnimSegment171.children.append(HAnimSite172)

HAnimJoint170.children.append(HAnimSegment171)

HAnimJoint168.children.append(HAnimJoint170)

HAnimJoint163.children.append(HAnimJoint168)

HAnimJoint161.children.append(HAnimJoint163)

HAnimJoint148.children.append(HAnimJoint161)

HAnimJoint146.children.append(HAnimJoint148)

HAnimJoint96.children.append(HAnimJoint146)

HAnimJoint85.children.append(HAnimJoint96)

HAnimJoint71.children.append(HAnimJoint85)

HAnimJoint39.children.append(HAnimJoint71)
HAnimJoint175 = x3d.HAnimJoint()
HAnimJoint175.DEF = "STD_Joint_r_hip"
HAnimJoint175.name = "r_hip"
HAnimJoint175.center = [-0.0950,0.9171,0.0029]
HAnimSegment176 = x3d.HAnimSegment()
HAnimSegment176.DEF = "STD_Segment_r_thigh"
HAnimSegment176.name = "r_thigh"
HAnimSite177 = x3d.HAnimSite()
HAnimSite177.DEF = "STD_Site_r_femoral_lateral_epicondyles_pt"
HAnimSite177.name = "r_femoral_lateral_epicondyles_pt"
HAnimSite177.scale = [0.0225,0.0225,0.0225]
HAnimSite177.translation = [-0.1421,0.4992,0.0310]
TouchSensor178 = x3d.TouchSensor()
TouchSensor178.description = "HAnimSite r_femoral_lateral_epicondyles_pt"

HAnimSite177.children.append(TouchSensor178)
Shape179 = x3d.Shape()
Shape179.USE = "HAnimSiteShape"

HAnimSite177.children.append(Shape179)

HAnimSegment176.children.append(HAnimSite177)
HAnimSite180 = x3d.HAnimSite()
HAnimSite180.DEF = "STD_Site_r_femoral_medial_epicondyles_pt"
HAnimSite180.name = "r_femoral_medial_epicondyles_pt"
HAnimSite180.scale = [0.0225,0.0225,0.0225]
HAnimSite180.translation = [-0.0221,0.5014,0.0289]
TouchSensor181 = x3d.TouchSensor()
TouchSensor181.description = "HAnimSite r_femoral_medial_epicondyles_pt"

HAnimSite180.children.append(TouchSensor181)
Shape182 = x3d.Shape()
Shape182.USE = "HAnimSiteShape"

HAnimSite180.children.append(Shape182)

HAnimSegment176.children.append(HAnimSite180)
HAnimSite183 = x3d.HAnimSite()
HAnimSite183.DEF = "STD_Site_r_knee_crease_pt"
HAnimSite183.name = "r_knee_crease_pt"
HAnimSite183.scale = [0.0225,0.0225,0.0225]
HAnimSite183.translation = [-0.0825,0.4932,-0.0326]
TouchSensor184 = x3d.TouchSensor()
TouchSensor184.description = "HAnimSite r_knee_crease_pt"

HAnimSite183.children.append(TouchSensor184)
Shape185 = x3d.Shape()
Shape185.USE = "HAnimSiteShape"

HAnimSite183.children.append(Shape185)

HAnimSegment176.children.append(HAnimSite183)
HAnimSite186 = x3d.HAnimSite()
HAnimSite186.DEF = "STD_Site_r_suprapatella_pt"
HAnimSite186.name = "r_suprapatella_pt"
HAnimSite186.scale = [0.0225,0.0225,0.0225]
TouchSensor187 = x3d.TouchSensor()
TouchSensor187.description = "HAnimSite r_suprapatella_pt"

HAnimSite186.children.append(TouchSensor187)
Shape188 = x3d.Shape()
Shape188.USE = "HAnimSiteShape"

HAnimSite186.children.append(Shape188)

HAnimSegment176.children.append(HAnimSite186)

HAnimJoint175.children.append(HAnimSegment176)
HAnimJoint189 = x3d.HAnimJoint()
HAnimJoint189.DEF = "STD_Joint_r_knee"
HAnimJoint189.name = "r_knee"
HAnimJoint189.center = [-0.0867,0.4913,0.0318]
HAnimSegment190 = x3d.HAnimSegment()
HAnimSegment190.DEF = "STD_Segment_r_calf"
HAnimSegment190.name = "r_calf"
HAnimSite191 = x3d.HAnimSite()
HAnimSite191.DEF = "STD_Site_r_lateral_malleolus_pt"
HAnimSite191.name = "r_lateral_malleolus_pt"
HAnimSite191.scale = [0.0225,0.0225,0.0225]
HAnimSite191.translation = [-0.1006,0.0658,-0.1075]
TouchSensor192 = x3d.TouchSensor()
TouchSensor192.description = "HAnimSite r_lateral_malleolus_pt"

HAnimSite191.children.append(TouchSensor192)
Shape193 = x3d.Shape()
Shape193.USE = "HAnimSiteShape"

HAnimSite191.children.append(Shape193)

HAnimSegment190.children.append(HAnimSite191)
HAnimSite194 = x3d.HAnimSite()
HAnimSite194.DEF = "STD_Site_r_tibiale_pt"
HAnimSite194.name = "r_tibiale_pt"
HAnimSite194.scale = [0.0225,0.0225,0.0225]
TouchSensor195 = x3d.TouchSensor()
TouchSensor195.description = "HAnimSite r_tibiale_pt"

HAnimSite194.children.append(TouchSensor195)
Shape196 = x3d.Shape()
Shape196.USE = "HAnimSiteShape"

HAnimSite194.children.append(Shape196)

HAnimSegment190.children.append(HAnimSite194)
HAnimSite197 = x3d.HAnimSite()
HAnimSite197.DEF = "STD_Site_r_medial_malleolus_pt"
HAnimSite197.name = "r_medial_malleolus_pt"
HAnimSite197.scale = [0.0225,0.0225,0.0225]
HAnimSite197.translation = [-0.0591,0.0760,-0.0928]
TouchSensor198 = x3d.TouchSensor()
TouchSensor198.description = "HAnimSite r_medial_malleolus_pt"

HAnimSite197.children.append(TouchSensor198)
Shape199 = x3d.Shape()
Shape199.USE = "HAnimSiteShape"

HAnimSite197.children.append(Shape199)

HAnimSegment190.children.append(HAnimSite197)

HAnimJoint189.children.append(HAnimSegment190)
HAnimJoint200 = x3d.HAnimJoint()
HAnimJoint200.DEF = "STD_Joint_r_talocrural"
HAnimJoint200.name = "r_talocrural"
HAnimJoint200.center = [-0.0801,0.0712,-0.0766]
HAnimSegment201 = x3d.HAnimSegment()
HAnimSegment201.DEF = "STD_Segment_r_talus"
HAnimSegment201.name = "r_talus"
HAnimSite202 = x3d.HAnimSite()
HAnimSite202.DEF = "STD_Site_r_sphyrion_pt"
HAnimSite202.name = "r_sphyrion_pt"
HAnimSite202.scale = [0.0225,0.0225,0.0225]
HAnimSite202.translation = [-0.0603,0.0610,-0.1002]
TouchSensor203 = x3d.TouchSensor()
TouchSensor203.description = "HAnimSite r_sphyrion_pt"

HAnimSite202.children.append(TouchSensor203)
Shape204 = x3d.Shape()
Shape204.USE = "HAnimSiteShape"

HAnimSite202.children.append(Shape204)

HAnimSegment201.children.append(HAnimSite202)
HAnimSite205 = x3d.HAnimSite()
HAnimSite205.DEF = "STD_Site_r_calcaneus_posterior_pt"
HAnimSite205.name = "r_calcaneus_posterior_pt"
HAnimSite205.scale = [0.0225,0.0225,0.0225]
HAnimSite205.translation = [-0.0692,0.0297,-0.1221]
TouchSensor206 = x3d.TouchSensor()
TouchSensor206.description = "HAnimSite r_calcaneus_posterior_pt"

HAnimSite205.children.append(TouchSensor206)
Shape207 = x3d.Shape()
Shape207.USE = "HAnimSiteShape"

HAnimSite205.children.append(Shape207)

HAnimSegment201.children.append(HAnimSite205)

HAnimJoint200.children.append(HAnimSegment201)
HAnimJoint208 = x3d.HAnimJoint()
HAnimJoint208.DEF = "STD_Joint_r_talocalcaneonavicular"
HAnimJoint208.name = "r_talocalcaneonavicular"
HAnimJoint208.center = [0,0,0]
HAnimSegment209 = x3d.HAnimSegment()
HAnimSegment209.DEF = "STD_Segment_r_navicular"
HAnimSegment209.name = "r_navicular"

HAnimJoint208.children.append(HAnimSegment209)
HAnimJoint210 = x3d.HAnimJoint()
HAnimJoint210.DEF = "STD_Joint_r_cuneonavicular_1"
HAnimJoint210.name = "r_cuneonavicular_1"
HAnimJoint210.center = [0,0,0]
HAnimSegment211 = x3d.HAnimSegment()
HAnimSegment211.DEF = "STD_Segment_r_cuneiform_1"
HAnimSegment211.name = "r_cuneiform_1"

HAnimJoint210.children.append(HAnimSegment211)
HAnimJoint212 = x3d.HAnimJoint()
HAnimJoint212.DEF = "STD_Joint_r_tarsometatarsal_1"
HAnimJoint212.name = "r_tarsometatarsal_1"
HAnimJoint212.center = [0,0,0]
HAnimSegment213 = x3d.HAnimSegment()
HAnimSegment213.DEF = "STD_Segment_r_metatarsal_1"
HAnimSegment213.name = "r_metatarsal_1"

HAnimJoint212.children.append(HAnimSegment213)
HAnimJoint214 = x3d.HAnimJoint()
HAnimJoint214.DEF = "STD_Joint_r_metatarsophalangeal_1"
HAnimJoint214.name = "r_metatarsophalangeal_1"
HAnimJoint214.center = [0,0,0]
HAnimSegment215 = x3d.HAnimSegment()
HAnimSegment215.DEF = "STD_Segment_r_tarsal_proximal_phalanx_1"
HAnimSegment215.name = "r_tarsal_proximal_phalanx_1"
HAnimSite216 = x3d.HAnimSite()
HAnimSite216.DEF = "STD_Site_r_metatarsal_phalanx_1_pt"
HAnimSite216.name = "r_metatarsal_phalanx_1_pt"
HAnimSite216.scale = [0.0225,0.0225,0.0225]
TouchSensor217 = x3d.TouchSensor()
TouchSensor217.description = "HAnimSite r_metatarsal_phalanx_1_pt"

HAnimSite216.children.append(TouchSensor217)
Shape218 = x3d.Shape()
Shape218.USE = "HAnimSiteShape"

HAnimSite216.children.append(Shape218)

HAnimSegment215.children.append(HAnimSite216)

HAnimJoint214.children.append(HAnimSegment215)
HAnimJoint219 = x3d.HAnimJoint()
HAnimJoint219.DEF = "STD_Joint_r_tarsal_interphalangeal_1"
HAnimJoint219.name = "r_tarsal_interphalangeal_1"
HAnimJoint219.center = [0,0,0]
HAnimSegment220 = x3d.HAnimSegment()
HAnimSegment220.DEF = "STD_Segment_r_tarsal_distal_phalanx_1"
HAnimSegment220.name = "r_tarsal_distal_phalanx_1"
HAnimSite221 = x3d.HAnimSite()
HAnimSite221.DEF = "STD_Site_r_tarsal_distal_phalanx_1_tip"
HAnimSite221.name = "r_tarsal_distal_phalanx_1_tip"
HAnimSite221.scale = [0.0225,0.0225,0.0225]
TouchSensor222 = x3d.TouchSensor()
TouchSensor222.description = "HAnimSite r_tarsal_distal_phalanx_1_tip"

HAnimSite221.children.append(TouchSensor222)
Shape223 = x3d.Shape()
Shape223.USE = "HAnimSiteShape"

HAnimSite221.children.append(Shape223)

HAnimSegment220.children.append(HAnimSite221)

HAnimJoint219.children.append(HAnimSegment220)

HAnimJoint214.children.append(HAnimJoint219)

HAnimJoint212.children.append(HAnimJoint214)

HAnimJoint210.children.append(HAnimJoint212)

HAnimJoint208.children.append(HAnimJoint210)
HAnimJoint224 = x3d.HAnimJoint()
HAnimJoint224.DEF = "STD_Joint_r_cuneonavicular_2"
HAnimJoint224.name = "r_cuneonavicular_2"
HAnimJoint224.center = [0,0,0]
HAnimSegment225 = x3d.HAnimSegment()
HAnimSegment225.DEF = "STD_Segment_r_cuneiform_2"
HAnimSegment225.name = "r_cuneiform_2"

HAnimJoint224.children.append(HAnimSegment225)
HAnimJoint226 = x3d.HAnimJoint()
HAnimJoint226.DEF = "STD_Joint_r_tarsometatarsal_2"
HAnimJoint226.name = "r_tarsometatarsal_2"
HAnimJoint226.center = [0,0,0]
HAnimSegment227 = x3d.HAnimSegment()
HAnimSegment227.DEF = "STD_Segment_r_metatarsal_2"
HAnimSegment227.name = "r_metatarsal_2"

HAnimJoint226.children.append(HAnimSegment227)
HAnimJoint228 = x3d.HAnimJoint()
HAnimJoint228.DEF = "STD_Joint_r_metatarsophalangeal_2"
HAnimJoint228.name = "r_metatarsophalangeal_2"
HAnimJoint228.center = [0,0,0]
HAnimSegment229 = x3d.HAnimSegment()
HAnimSegment229.DEF = "STD_Segment_r_tarsal_proximal_phalanx_2"
HAnimSegment229.name = "r_tarsal_proximal_phalanx_2"

HAnimJoint228.children.append(HAnimSegment229)
HAnimJoint230 = x3d.HAnimJoint()
HAnimJoint230.DEF = "STD_Joint_r_tarsal_proximal_interphalangeal_2"
HAnimJoint230.name = "r_tarsal_proximal_interphalangeal_2"
HAnimJoint230.center = [0,0,0]
HAnimSegment231 = x3d.HAnimSegment()
HAnimSegment231.DEF = "STD_Segment_r_tarsal_middle_phalanx_2"
HAnimSegment231.name = "r_tarsal_middle_phalanx_2"

HAnimJoint230.children.append(HAnimSegment231)
HAnimJoint232 = x3d.HAnimJoint()
HAnimJoint232.DEF = "STD_Joint_r_tarsal_distal_interphalangeal_2"
HAnimJoint232.name = "r_tarsal_distal_interphalangeal_2"
HAnimJoint232.center = [0,0,0]
HAnimSegment233 = x3d.HAnimSegment()
HAnimSegment233.DEF = "STD_Segment_r_tarsal_distal_phalanx_2"
HAnimSegment233.name = "r_tarsal_distal_phalanx_2"
HAnimSite234 = x3d.HAnimSite()
HAnimSite234.DEF = "STD_Site_r_tarsal_distal_phalanx_2_tip"
HAnimSite234.name = "r_tarsal_distal_phalanx_2_tip"
HAnimSite234.scale = [0.0225,0.0225,0.0225]
HAnimSite234.translation = [-0.0883,0.0134,0.1383]
TouchSensor235 = x3d.TouchSensor()
TouchSensor235.description = "HAnimSite r_tarsal_distal_phalanx_2_tip"

HAnimSite234.children.append(TouchSensor235)
Shape236 = x3d.Shape()
Shape236.USE = "HAnimSiteShape"

HAnimSite234.children.append(Shape236)

HAnimSegment233.children.append(HAnimSite234)

HAnimJoint232.children.append(HAnimSegment233)

HAnimJoint230.children.append(HAnimJoint232)

HAnimJoint228.children.append(HAnimJoint230)

HAnimJoint226.children.append(HAnimJoint228)

HAnimJoint224.children.append(HAnimJoint226)

HAnimJoint208.children.append(HAnimJoint224)
HAnimJoint237 = x3d.HAnimJoint()
HAnimJoint237.DEF = "STD_Joint_r_cuneonavicular_3"
HAnimJoint237.name = "r_cuneonavicular_3"
HAnimJoint237.center = [0,0,0]
HAnimSegment238 = x3d.HAnimSegment()
HAnimSegment238.DEF = "STD_Segment_r_cuneiform_3"
HAnimSegment238.name = "r_cuneiform_3"

HAnimJoint237.children.append(HAnimSegment238)
HAnimJoint239 = x3d.HAnimJoint()
HAnimJoint239.DEF = "STD_Joint_r_tarsometatarsal_3 "
HAnimJoint239.name = "r_tarsometatarsal_3 "
HAnimJoint239.center = [0,0,0]
HAnimSegment240 = x3d.HAnimSegment()
HAnimSegment240.DEF = "STD_Segment_r_metatarsal_3"
HAnimSegment240.name = "r_metatarsal_3"

HAnimJoint239.children.append(HAnimSegment240)
HAnimJoint241 = x3d.HAnimJoint()
HAnimJoint241.DEF = "STD_Joint_r_metatarsophalangeal_3"
HAnimJoint241.name = "r_metatarsophalangeal_3"
HAnimJoint241.center = [0,0,0]
HAnimSegment242 = x3d.HAnimSegment()
HAnimSegment242.DEF = "STD_Segment_r_tarsal_proximal_phalanx_3"
HAnimSegment242.name = "r_tarsal_proximal_phalanx_3"

HAnimJoint241.children.append(HAnimSegment242)
HAnimJoint243 = x3d.HAnimJoint()
HAnimJoint243.DEF = "STD_Joint_r_tarsal_proximal_interphalangeal_3"
HAnimJoint243.name = "r_tarsal_proximal_interphalangeal_3"
HAnimJoint243.center = [0,0,0]
HAnimSegment244 = x3d.HAnimSegment()
HAnimSegment244.DEF = "STD_Segment_r_tarsal_middle_phalanx_3"
HAnimSegment244.name = "r_tarsal_middle_phalanx_3"

HAnimJoint243.children.append(HAnimSegment244)
HAnimJoint245 = x3d.HAnimJoint()
HAnimJoint245.DEF = "STD_Joint_r_tarsal_distal_interphalangeal_3"
HAnimJoint245.name = "r_tarsal_distal_interphalangeal_3"
HAnimJoint245.center = [0,0,0]
HAnimSegment246 = x3d.HAnimSegment()
HAnimSegment246.DEF = "STD_Segment_r_tarsal_distal_phalanx_3"
HAnimSegment246.name = "r_tarsal_distal_phalanx_3"
HAnimSite247 = x3d.HAnimSite()
HAnimSite247.DEF = "STD_Site_r_tarsal_distal_phalanx_3_tip"
HAnimSite247.name = "r_tarsal_distal_phalanx_3_tip"
HAnimSite247.scale = [0.0225,0.0225,0.0225]
TouchSensor248 = x3d.TouchSensor()
TouchSensor248.description = "HAnimSite r_tarsal_distal_phalanx_3_tip"

HAnimSite247.children.append(TouchSensor248)
Shape249 = x3d.Shape()
Shape249.USE = "HAnimSiteShape"

HAnimSite247.children.append(Shape249)

HAnimSegment246.children.append(HAnimSite247)

HAnimJoint245.children.append(HAnimSegment246)

HAnimJoint243.children.append(HAnimJoint245)

HAnimJoint241.children.append(HAnimJoint243)

HAnimJoint239.children.append(HAnimJoint241)

HAnimJoint237.children.append(HAnimJoint239)

HAnimJoint208.children.append(HAnimJoint237)

HAnimJoint200.children.append(HAnimJoint208)
HAnimJoint250 = x3d.HAnimJoint()
HAnimJoint250.DEF = "STD_Joint_r_calcaneocuboid"
HAnimJoint250.name = "r_calcaneocuboid"
HAnimJoint250.center = [0,0,0]
HAnimSegment251 = x3d.HAnimSegment()
HAnimSegment251.DEF = "STD_Segment_r_calcaneus"
HAnimSegment251.name = "r_calcaneus"

HAnimJoint250.children.append(HAnimSegment251)
HAnimJoint252 = x3d.HAnimJoint()
HAnimJoint252.DEF = "STD_Joint_r_transversetarsal"
HAnimJoint252.name = "r_transversetarsal"
HAnimJoint252.center = [0,0,0]
HAnimSegment253 = x3d.HAnimSegment()
HAnimSegment253.DEF = "STD_Segment_r_cuboid"
HAnimSegment253.name = "r_cuboid"

HAnimJoint252.children.append(HAnimSegment253)
HAnimJoint254 = x3d.HAnimJoint()
HAnimJoint254.DEF = "STD_Joint_r_tarsometatarsal_4"
HAnimJoint254.name = "r_tarsometatarsal_4"
HAnimJoint254.center = [0,0,0]
HAnimSegment255 = x3d.HAnimSegment()
HAnimSegment255.DEF = "STD_Segment_r_metatarsal_4"
HAnimSegment255.name = "r_metatarsal_4"

HAnimJoint254.children.append(HAnimSegment255)
HAnimJoint256 = x3d.HAnimJoint()
HAnimJoint256.DEF = "STD_Joint_r_metatarsophalangeal_4"
HAnimJoint256.name = "r_metatarsophalangeal_4"
HAnimJoint256.center = [0,0,0]
HAnimSegment257 = x3d.HAnimSegment()
HAnimSegment257.DEF = "STD_Segment_r_tarsal_proximal_phalanx_4"
HAnimSegment257.name = "r_tarsal_proximal_phalanx_4"

HAnimJoint256.children.append(HAnimSegment257)
HAnimJoint258 = x3d.HAnimJoint()
HAnimJoint258.DEF = "STD_Joint_r_tarsal_proximal_interphalangeal_4"
HAnimJoint258.name = "r_tarsal_proximal_interphalangeal_4"
HAnimJoint258.center = [0,0,0]
HAnimSegment259 = x3d.HAnimSegment()
HAnimSegment259.DEF = "STD_Segment_r_tarsal_middle_phalanx_4"
HAnimSegment259.name = "r_tarsal_middle_phalanx_4"

HAnimJoint258.children.append(HAnimSegment259)
HAnimJoint260 = x3d.HAnimJoint()
HAnimJoint260.DEF = "STD_Joint_r_tarsal_distal_interphalangeal_4"
HAnimJoint260.name = "r_tarsal_distal_interphalangeal_4"
HAnimJoint260.center = [0,0,0]
HAnimSegment261 = x3d.HAnimSegment()
HAnimSegment261.DEF = "STD_Segment_r_tarsal_distal_phalanx_4"
HAnimSegment261.name = "r_tarsal_distal_phalanx_4"
HAnimSite262 = x3d.HAnimSite()
HAnimSite262.DEF = "STD_Site_r_tarsal_distal_phalanx_4_tip"
HAnimSite262.name = "r_tarsal_distal_phalanx_4_tip"
HAnimSite262.scale = [0.0225,0.0225,0.0225]
TouchSensor263 = x3d.TouchSensor()
TouchSensor263.description = "HAnimSite r_tarsal_distal_phalanx_4_tip"

HAnimSite262.children.append(TouchSensor263)
Shape264 = x3d.Shape()
Shape264.USE = "HAnimSiteShape"

HAnimSite262.children.append(Shape264)

HAnimSegment261.children.append(HAnimSite262)

HAnimJoint260.children.append(HAnimSegment261)

HAnimJoint258.children.append(HAnimJoint260)

HAnimJoint256.children.append(HAnimJoint258)

HAnimJoint254.children.append(HAnimJoint256)

HAnimJoint252.children.append(HAnimJoint254)
HAnimJoint265 = x3d.HAnimJoint()
HAnimJoint265.DEF = "STD_Joint_r_tarsometatarsal_5"
HAnimJoint265.name = "r_tarsometatarsal_5"
HAnimJoint265.center = [0,0,0]
HAnimSegment266 = x3d.HAnimSegment()
HAnimSegment266.DEF = "STD_Segment_r_metatarsal_5"
HAnimSegment266.name = "r_metatarsal_5"

HAnimJoint265.children.append(HAnimSegment266)
HAnimJoint267 = x3d.HAnimJoint()
HAnimJoint267.DEF = "STD_Joint_r_metatarsophalangeal_5"
HAnimJoint267.name = "r_metatarsophalangeal_5"
HAnimJoint267.center = [0,0,0]
HAnimSegment268 = x3d.HAnimSegment()
HAnimSegment268.DEF = "STD_Segment_r_tarsal_proximal_phalanx_5"
HAnimSegment268.name = "r_tarsal_proximal_phalanx_5"
HAnimSite269 = x3d.HAnimSite()
HAnimSite269.DEF = "STD_Site_r_metatarsal_phalanx_5_pt"
HAnimSite269.name = "r_metatarsal_phalanx_5_pt"
HAnimSite269.scale = [0.0225,0.0225,0.0225]
TouchSensor270 = x3d.TouchSensor()
TouchSensor270.description = "HAnimSite r_metatarsal_phalanx_5_pt"

HAnimSite269.children.append(TouchSensor270)
Shape271 = x3d.Shape()
Shape271.USE = "HAnimSiteShape"

HAnimSite269.children.append(Shape271)

HAnimSegment268.children.append(HAnimSite269)

HAnimJoint267.children.append(HAnimSegment268)
HAnimJoint272 = x3d.HAnimJoint()
HAnimJoint272.DEF = "STD_Joint_r_tarsal_proximal_interphalangeal_5"
HAnimJoint272.name = "r_tarsal_proximal_interphalangeal_5"
HAnimJoint272.center = [0,0,0]
HAnimSegment273 = x3d.HAnimSegment()
HAnimSegment273.DEF = "STD_Segment_r_tarsal_middle_phalanx_5"
HAnimSegment273.name = "r_tarsal_middle_phalanx_5"

HAnimJoint272.children.append(HAnimSegment273)
HAnimJoint274 = x3d.HAnimJoint()
HAnimJoint274.DEF = "STD_Joint_r_tarsal_distal_interphalangeal_5"
HAnimJoint274.name = "r_tarsal_distal_interphalangeal_5"
HAnimJoint274.center = [0,0,0]
HAnimSegment275 = x3d.HAnimSegment()
HAnimSegment275.DEF = "STD_Segment_r_tarsal_distal_phalanx_5"
HAnimSegment275.name = "r_tarsal_distal_phalanx_5"
HAnimSite276 = x3d.HAnimSite()
HAnimSite276.DEF = "STD_Site_r_tarsal_distal_phalanx_5_tip"
HAnimSite276.name = "r_tarsal_distal_phalanx_5_tip"
HAnimSite276.scale = [0.0225,0.0225,0.0225]
TouchSensor277 = x3d.TouchSensor()
TouchSensor277.description = "HAnimSite r_tarsal_distal_phalanx_5_tip"

HAnimSite276.children.append(TouchSensor277)
Shape278 = x3d.Shape()
Shape278.USE = "HAnimSiteShape"

HAnimSite276.children.append(Shape278)

HAnimSegment275.children.append(HAnimSite276)

HAnimJoint274.children.append(HAnimSegment275)

HAnimJoint272.children.append(HAnimJoint274)

HAnimJoint267.children.append(HAnimJoint272)

HAnimJoint265.children.append(HAnimJoint267)

HAnimJoint252.children.append(HAnimJoint265)

HAnimJoint250.children.append(HAnimJoint252)

HAnimJoint200.children.append(HAnimJoint250)

HAnimJoint189.children.append(HAnimJoint200)

HAnimJoint175.children.append(HAnimJoint189)

HAnimJoint39.children.append(HAnimJoint175)

HAnimJoint14.children.append(HAnimJoint39)
HAnimJoint279 = x3d.HAnimJoint()
HAnimJoint279.DEF = "STD_Joint_vl5"
HAnimJoint279.name = "vl5"
HAnimJoint279.center = [0.0028,1.0568,-0.0776]
HAnimSegment280 = x3d.HAnimSegment()
HAnimSegment280.DEF = "STD_Segment_l5"
HAnimSegment280.name = "l5"
HAnimSite281 = x3d.HAnimSite()
HAnimSite281.DEF = "STD_Site_waist_preferred_posterior_pt"
HAnimSite281.name = "waist_preferred_posterior_pt"
HAnimSite281.scale = [0.0225,0.0225,0.0225]
HAnimSite281.translation = [0.2900,1.0915,-0.1091]
TouchSensor282 = x3d.TouchSensor()
TouchSensor282.description = "HAnimSite waist_preferred_posterior_pt"

HAnimSite281.children.append(TouchSensor282)
Shape283 = x3d.Shape()
Shape283.USE = "HAnimSiteShape"

HAnimSite281.children.append(Shape283)

HAnimSegment280.children.append(HAnimSite281)
HAnimSite284 = x3d.HAnimSite()
HAnimSite284.DEF = "STD_Site_waist_preferred_anterior_pt"
HAnimSite284.name = "waist_preferred_anterior_pt"
HAnimSite284.scale = [0.0225,0.0225,0.0225]
TouchSensor285 = x3d.TouchSensor()
TouchSensor285.description = "HAnimSite waist_preferred_anterior_pt"

HAnimSite284.children.append(TouchSensor285)
Shape286 = x3d.Shape()
Shape286.USE = "HAnimSiteShape"

HAnimSite284.children.append(Shape286)

HAnimSegment280.children.append(HAnimSite284)
HAnimSite287 = x3d.HAnimSite()
HAnimSite287.DEF = "STD_Site_navel_pt"
HAnimSite287.name = "navel_pt"
HAnimSite287.scale = [0.0225,0.0225,0.0225]
HAnimSite287.translation = [0.0069,1.0966,0.1017]
TouchSensor288 = x3d.TouchSensor()
TouchSensor288.description = "HAnimSite navel_pt"

HAnimSite287.children.append(TouchSensor288)
Shape289 = x3d.Shape()
Shape289.USE = "HAnimSiteShape"

HAnimSite287.children.append(Shape289)

HAnimSegment280.children.append(HAnimSite287)

HAnimJoint279.children.append(HAnimSegment280)
HAnimJoint290 = x3d.HAnimJoint()
HAnimJoint290.DEF = "STD_Joint_vl4"
HAnimJoint290.name = "vl4"
HAnimJoint290.center = [0.0035,1.0925,-0.0787]
HAnimSegment291 = x3d.HAnimSegment()
HAnimSegment291.DEF = "STD_Segment_l4"
HAnimSegment291.name = "l4"

HAnimJoint290.children.append(HAnimSegment291)
HAnimJoint292 = x3d.HAnimJoint()
HAnimJoint292.DEF = "STD_Joint_vl3"
HAnimJoint292.name = "vl3"
HAnimJoint292.center = [0.0041,1.1276,-0.0796]
HAnimSegment293 = x3d.HAnimSegment()
HAnimSegment293.DEF = "STD_Segment_l3"
HAnimSegment293.name = "l3"

HAnimJoint292.children.append(HAnimSegment293)
HAnimJoint294 = x3d.HAnimJoint()
HAnimJoint294.DEF = "STD_Joint_vl2"
HAnimJoint294.name = "vl2"
HAnimJoint294.center = [0.0045,1.1546,-0.0800]
HAnimSegment295 = x3d.HAnimSegment()
HAnimSegment295.DEF = "STD_Segment_l2"
HAnimSegment295.name = "l2"
HAnimSite296 = x3d.HAnimSite()
HAnimSite296.DEF = "STD_Site_spine_2_middle_back_pt"
HAnimSite296.name = "spine_2_middle_back_pt"
HAnimSite296.scale = [0.0225,0.0225,0.0225]
TouchSensor297 = x3d.TouchSensor()
TouchSensor297.description = "HAnimSite spine_2_middle_back_pt"

HAnimSite296.children.append(TouchSensor297)
Shape298 = x3d.Shape()
Shape298.USE = "HAnimSiteShape"

HAnimSite296.children.append(Shape298)

HAnimSegment295.children.append(HAnimSite296)
HAnimSite299 = x3d.HAnimSite()
HAnimSite299.DEF = "STD_Site_r_rib10_pt"
HAnimSite299.name = "r_rib10_pt"
HAnimSite299.scale = [0.0225,0.0225,0.0225]
HAnimSite299.translation = [-0.0711,1.1941,0.1016]
TouchSensor300 = x3d.TouchSensor()
TouchSensor300.description = "HAnimSite r_rib10_pt"

HAnimSite299.children.append(TouchSensor300)
Shape301 = x3d.Shape()
Shape301.USE = "HAnimSiteShape"

HAnimSite299.children.append(Shape301)

HAnimSegment295.children.append(HAnimSite299)
HAnimSite302 = x3d.HAnimSite()
HAnimSite302.DEF = "STD_Site_l_rib10_pt"
HAnimSite302.name = "l_rib10_pt"
HAnimSite302.scale = [0.0225,0.0225,0.0225]
HAnimSite302.translation = [0.0871,1.1925,0.0992]
TouchSensor303 = x3d.TouchSensor()
TouchSensor303.description = "HAnimSite l_rib10_pt"

HAnimSite302.children.append(TouchSensor303)
Shape304 = x3d.Shape()
Shape304.USE = "HAnimSiteShape"

HAnimSite302.children.append(Shape304)

HAnimSegment295.children.append(HAnimSite302)

HAnimJoint294.children.append(HAnimSegment295)
HAnimJoint305 = x3d.HAnimJoint()
HAnimJoint305.DEF = "STD_Joint_vl1"
HAnimJoint305.name = "vl1"
HAnimJoint305.center = [0.0048,1.1912,-0.0805]
HAnimSegment306 = x3d.HAnimSegment()
HAnimSegment306.DEF = "STD_Segment_l1"
HAnimSegment306.name = "l1"

HAnimJoint305.children.append(HAnimSegment306)
HAnimJoint307 = x3d.HAnimJoint()
HAnimJoint307.DEF = "STD_Joint_vt12"
HAnimJoint307.name = "vt12"
HAnimJoint307.center = [0.0051,1.2278,-0.0808]
HAnimSegment308 = x3d.HAnimSegment()
HAnimSegment308.DEF = "STD_Segment_t12"
HAnimSegment308.name = "t12"

HAnimJoint307.children.append(HAnimSegment308)
HAnimJoint309 = x3d.HAnimJoint()
HAnimJoint309.DEF = "STD_Joint_vt11"
HAnimJoint309.name = "vt11"
HAnimJoint309.center = [0.0053,1.2679,-0.0810]
HAnimSegment310 = x3d.HAnimSegment()
HAnimSegment310.DEF = "STD_Segment_t11"
HAnimSegment310.name = "t11"

HAnimJoint309.children.append(HAnimSegment310)
HAnimJoint311 = x3d.HAnimJoint()
HAnimJoint311.DEF = "STD_Joint_vt10"
HAnimJoint311.name = "vt10"
HAnimJoint311.center = [0.0056,1.2848,-0.0822]
HAnimSegment312 = x3d.HAnimSegment()
HAnimSegment312.DEF = "STD_Segment_t10"
HAnimSegment312.name = "t10"
HAnimSite313 = x3d.HAnimSite()
HAnimSite313.DEF = "STD_Site_substernale_pt"
HAnimSite313.name = "substernale_pt"
HAnimSite313.scale = [0.0225,0.0225,0.0225]
HAnimSite313.translation = [0.0085,1.2995,0.1147]
TouchSensor314 = x3d.TouchSensor()
TouchSensor314.description = "HAnimSite substernale_pt"

HAnimSite313.children.append(TouchSensor314)
Shape315 = x3d.Shape()
Shape315.USE = "HAnimSiteShape"

HAnimSite313.children.append(Shape315)

HAnimSegment312.children.append(HAnimSite313)

HAnimJoint311.children.append(HAnimSegment312)
HAnimJoint316 = x3d.HAnimJoint()
HAnimJoint316.DEF = "STD_Joint_vt9"
HAnimJoint316.name = "vt9"
HAnimJoint316.center = [0.0057,1.3126,-0.0838]
HAnimSegment317 = x3d.HAnimSegment()
HAnimSegment317.DEF = "STD_Segment_t9"
HAnimSegment317.name = "t9"
HAnimSite318 = x3d.HAnimSite()
HAnimSite318.DEF = "STD_Site_l_thelion_pt"
HAnimSite318.name = "l_thelion_pt"
HAnimSite318.scale = [0.0225,0.0225,0.0225]
HAnimSite318.translation = [0.0918,1.3382,0.1192]
TouchSensor319 = x3d.TouchSensor()
TouchSensor319.description = "HAnimSite l_thelion_pt"

HAnimSite318.children.append(TouchSensor319)
Shape320 = x3d.Shape()
Shape320.USE = "HAnimSiteShape"

HAnimSite318.children.append(Shape320)

HAnimSegment317.children.append(HAnimSite318)
HAnimSite321 = x3d.HAnimSite()
HAnimSite321.DEF = "STD_Site_r_thelion_pt"
HAnimSite321.name = "r_thelion_pt"
HAnimSite321.scale = [0.0225,0.0225,0.0225]
HAnimSite321.translation = [-0.0736,1.3385,0.1217]
TouchSensor322 = x3d.TouchSensor()
TouchSensor322.description = "HAnimSite r_thelion_pt"

HAnimSite321.children.append(TouchSensor322)
Shape323 = x3d.Shape()
Shape323.USE = "HAnimSiteShape"

HAnimSite321.children.append(Shape323)

HAnimSegment317.children.append(HAnimSite321)

HAnimJoint316.children.append(HAnimSegment317)
HAnimJoint324 = x3d.HAnimJoint()
HAnimJoint324.DEF = "STD_Joint_vt8"
HAnimJoint324.name = "vt8"
HAnimJoint324.center = [0.0057,1.3382,-0.0845]
HAnimSegment325 = x3d.HAnimSegment()
HAnimSegment325.DEF = "STD_Segment_t8"
HAnimSegment325.name = "t8"

HAnimJoint324.children.append(HAnimSegment325)
HAnimJoint326 = x3d.HAnimJoint()
HAnimJoint326.DEF = "STD_Joint_vt7"
HAnimJoint326.name = "vt7"
HAnimJoint326.center = [0.0058,1.3625,-0.0833]
HAnimSegment327 = x3d.HAnimSegment()
HAnimSegment327.DEF = "STD_Segment_t7"
HAnimSegment327.name = "t7"

HAnimJoint326.children.append(HAnimSegment327)
HAnimJoint328 = x3d.HAnimJoint()
HAnimJoint328.DEF = "STD_Joint_vt6"
HAnimJoint328.name = "vt6"
HAnimJoint328.center = [0.0059,1.3866,-0.0800]
HAnimSegment329 = x3d.HAnimSegment()
HAnimSegment329.DEF = "STD_Segment_t6"
HAnimSegment329.name = "t6"
HAnimSite330 = x3d.HAnimSite()
HAnimSite330.DEF = "STD_Site_l_chest_midsagittal_plane_pt"
HAnimSite330.name = "l_chest_midsagittal_plane_pt"
HAnimSite330.scale = [0.0225,0.0225,0.0225]
TouchSensor331 = x3d.TouchSensor()
TouchSensor331.description = "HAnimSite l_chest_midsagittal_plane_pt"

HAnimSite330.children.append(TouchSensor331)
Shape332 = x3d.Shape()
Shape332.USE = "HAnimSiteShape"

HAnimSite330.children.append(Shape332)

HAnimSegment329.children.append(HAnimSite330)
HAnimSite333 = x3d.HAnimSite()
HAnimSite333.DEF = "STD_Site_rear_center_midsagittal_plane_pt"
HAnimSite333.name = "rear_center_midsagittal_plane_pt"
HAnimSite333.scale = [0.0225,0.0225,0.0225]
TouchSensor334 = x3d.TouchSensor()
TouchSensor334.description = "HAnimSite rear_center_midsagittal_plane_pt"

HAnimSite333.children.append(TouchSensor334)
Shape335 = x3d.Shape()
Shape335.USE = "HAnimSiteShape"

HAnimSite333.children.append(Shape335)

HAnimSegment329.children.append(HAnimSite333)
HAnimSite336 = x3d.HAnimSite()
HAnimSite336.DEF = "STD_Site_mesosternale_pt"
HAnimSite336.name = "mesosternale_pt"
HAnimSite336.scale = [0.0225,0.0225,0.0225]
TouchSensor337 = x3d.TouchSensor()
TouchSensor337.description = "HAnimSite mesosternale_pt"

HAnimSite336.children.append(TouchSensor337)
Shape338 = x3d.Shape()
Shape338.USE = "HAnimSiteShape"

HAnimSite336.children.append(Shape338)

HAnimSegment329.children.append(HAnimSite336)
HAnimSite339 = x3d.HAnimSite()
HAnimSite339.DEF = "STD_Site_r_chest_midsagittal_plane_pt"
HAnimSite339.name = "r_chest_midsagittal_plane_pt"
HAnimSite339.scale = [0.0225,0.0225,0.0225]
TouchSensor340 = x3d.TouchSensor()
TouchSensor340.description = "HAnimSite r_chest_midsagittal_plane_pt"

HAnimSite339.children.append(TouchSensor340)
Shape341 = x3d.Shape()
Shape341.USE = "HAnimSiteShape"

HAnimSite339.children.append(Shape341)

HAnimSegment329.children.append(HAnimSite339)

HAnimJoint328.children.append(HAnimSegment329)
HAnimJoint342 = x3d.HAnimJoint()
HAnimJoint342.DEF = "STD_Joint_vt5"
HAnimJoint342.name = "vt5"
HAnimJoint342.center = [0.0060,1.4102,-0.0745]
HAnimSegment343 = x3d.HAnimSegment()
HAnimSegment343.DEF = "STD_Segment_t5"
HAnimSegment343.name = "t5"
HAnimSite344 = x3d.HAnimSite()
HAnimSite344.DEF = "STD_Site_spine_1_middle_back_pt"
HAnimSite344.name = "spine_1_middle_back_pt"
HAnimSite344.scale = [0.0225,0.0225,0.0225]
TouchSensor345 = x3d.TouchSensor()
TouchSensor345.description = "HAnimSite spine_1_middle_back_pt"

HAnimSite344.children.append(TouchSensor345)
Shape346 = x3d.Shape()
Shape346.USE = "HAnimSiteShape"

HAnimSite344.children.append(Shape346)

HAnimSegment343.children.append(HAnimSite344)

HAnimJoint342.children.append(HAnimSegment343)
HAnimJoint347 = x3d.HAnimJoint()
HAnimJoint347.DEF = "STD_Joint_vt4"
HAnimJoint347.name = "vt4"
HAnimJoint347.center = [0.0061,1.4320,-0.0675]
HAnimSegment348 = x3d.HAnimSegment()
HAnimSegment348.DEF = "STD_Segment_t4"
HAnimSegment348.name = "t4"

HAnimJoint347.children.append(HAnimSegment348)
HAnimJoint349 = x3d.HAnimJoint()
HAnimJoint349.DEF = "STD_Joint_vt3"
HAnimJoint349.name = "vt3"
HAnimJoint349.center = [0.0062,1.4583,-0.0570]
HAnimSegment350 = x3d.HAnimSegment()
HAnimSegment350.DEF = "STD_Segment_t3"
HAnimSegment350.name = "t3"

HAnimJoint349.children.append(HAnimSegment350)
HAnimJoint351 = x3d.HAnimJoint()
HAnimJoint351.DEF = "STD_Joint_vt2"
HAnimJoint351.name = "vt2"
HAnimJoint351.center = [0.0063,1.4761,-0.0484]
HAnimSegment352 = x3d.HAnimSegment()
HAnimSegment352.DEF = "STD_Segment_t2"
HAnimSegment352.name = "t2"

HAnimJoint351.children.append(HAnimSegment352)
HAnimJoint353 = x3d.HAnimJoint()
HAnimJoint353.DEF = "STD_Joint_vt1"
HAnimJoint353.name = "vt1"
HAnimJoint353.center = [0.0065,1.4951,-0.0387]
HAnimSegment354 = x3d.HAnimSegment()
HAnimSegment354.DEF = "STD_Segment_t1"
HAnimSegment354.name = "t1"
HAnimSite355 = x3d.HAnimSite()
HAnimSite355.DEF = "STD_Site_suprasternale_pt"
HAnimSite355.name = "suprasternale_pt"
HAnimSite355.scale = [0.0225,0.0225,0.0225]
HAnimSite355.translation = [0.0084,1.4714,0.0551]
TouchSensor356 = x3d.TouchSensor()
TouchSensor356.description = "HAnimSite suprasternale_pt"

HAnimSite355.children.append(TouchSensor356)
Shape357 = x3d.Shape()
Shape357.USE = "HAnimSiteShape"

HAnimSite355.children.append(Shape357)

HAnimSegment354.children.append(HAnimSite355)
HAnimSite358 = x3d.HAnimSite()
HAnimSite358.DEF = "STD_Site_cervicale_pt"
HAnimSite358.name = "cervicale_pt"
HAnimSite358.scale = [0.0225,0.0225,0.0225]
HAnimSite358.translation = [0.0064,1.520,-0.0815]
TouchSensor359 = x3d.TouchSensor()
TouchSensor359.description = "HAnimSite cervicale_pt"

HAnimSite358.children.append(TouchSensor359)
Shape360 = x3d.Shape()
Shape360.USE = "HAnimSiteShape"

HAnimSite358.children.append(Shape360)

HAnimSegment354.children.append(HAnimSite358)

HAnimJoint353.children.append(HAnimSegment354)
HAnimJoint361 = x3d.HAnimJoint()
HAnimJoint361.DEF = "STD_Joint_vc7"
HAnimJoint361.name = "vc7"
HAnimJoint361.center = [0.0066,1.5132,-0.0301]
HAnimSegment362 = x3d.HAnimSegment()
HAnimSegment362.DEF = "STD_Segment_c7"
HAnimSegment362.name = "c7"
HAnimSite363 = x3d.HAnimSite()
HAnimSite363.DEF = "STD_Site_r_neck_base_pt"
HAnimSite363.name = "r_neck_base_pt"
HAnimSite363.scale = [0.0225,0.0225,0.0225]
HAnimSite363.translation = [-0.0419,1.5149,-0.0220]
TouchSensor364 = x3d.TouchSensor()
TouchSensor364.description = "HAnimSite r_neck_base_pt"

HAnimSite363.children.append(TouchSensor364)
Shape365 = x3d.Shape()
Shape365.USE = "HAnimSiteShape"

HAnimSite363.children.append(Shape365)

HAnimSegment362.children.append(HAnimSite363)
HAnimSite366 = x3d.HAnimSite()
HAnimSite366.DEF = "STD_Site_l_neck_base_pt"
HAnimSite366.name = "l_neck_base_pt"
HAnimSite366.scale = [0.0225,0.0225,0.0225]
HAnimSite366.translation = [0.0646,1.5141,-0.0380]
TouchSensor367 = x3d.TouchSensor()
TouchSensor367.description = "HAnimSite l_neck_base_pt"

HAnimSite366.children.append(TouchSensor367)
Shape368 = x3d.Shape()
Shape368.USE = "HAnimSiteShape"

HAnimSite366.children.append(Shape368)

HAnimSegment362.children.append(HAnimSite366)

HAnimJoint361.children.append(HAnimSegment362)
HAnimJoint369 = x3d.HAnimJoint()
HAnimJoint369.DEF = "STD_Joint_vc6"
HAnimJoint369.name = "vc6"
HAnimJoint369.center = [0.0066,1.5357,-0.0143]
HAnimSegment370 = x3d.HAnimSegment()
HAnimSegment370.DEF = "STD_Segment_c6"
HAnimSegment370.name = "c6"

HAnimJoint369.children.append(HAnimSegment370)
HAnimJoint371 = x3d.HAnimJoint()
HAnimJoint371.DEF = "STD_Joint_vc5"
HAnimJoint371.name = "vc5"
HAnimJoint371.center = [0.0066,1.5520,-0.0082]
HAnimSegment372 = x3d.HAnimSegment()
HAnimSegment372.DEF = "STD_Segment_c5"
HAnimSegment372.name = "c5"

HAnimJoint371.children.append(HAnimSegment372)
HAnimJoint373 = x3d.HAnimJoint()
HAnimJoint373.DEF = "STD_Joint_vc4"
HAnimJoint373.name = "vc4"
HAnimJoint373.center = [0.0066,1.5662,-0.0084]
HAnimSegment374 = x3d.HAnimSegment()
HAnimSegment374.DEF = "STD_Segment_c4"
HAnimSegment374.name = "c4"

HAnimJoint373.children.append(HAnimSegment374)
HAnimJoint375 = x3d.HAnimJoint()
HAnimJoint375.DEF = "STD_Joint_vc3"
HAnimJoint375.name = "vc3"
HAnimJoint375.center = [0.0066,1.5800,-0.0103]
HAnimSegment376 = x3d.HAnimSegment()
HAnimSegment376.DEF = "STD_Segment_c3"
HAnimSegment376.name = "c3"

HAnimJoint375.children.append(HAnimSegment376)
HAnimJoint377 = x3d.HAnimJoint()
HAnimJoint377.DEF = "STD_Joint_vc2"
HAnimJoint377.name = "vc2"
HAnimJoint377.center = [0.0066,1.5928,-0.0103]
HAnimSegment378 = x3d.HAnimSegment()
HAnimSegment378.DEF = "STD_Segment_c2"
HAnimSegment378.name = "c2"
HAnimSite379 = x3d.HAnimSite()
HAnimSite379.DEF = "STD_Site_adams_apple_pt"
HAnimSite379.name = "adams_apple_pt"
HAnimSite379.scale = [0.0225,0.0225,0.0225]
TouchSensor380 = x3d.TouchSensor()
TouchSensor380.description = "HAnimSite adams_apple_pt"

HAnimSite379.children.append(TouchSensor380)
Shape381 = x3d.Shape()
Shape381.USE = "HAnimSiteShape"

HAnimSite379.children.append(Shape381)

HAnimSegment378.children.append(HAnimSite379)

HAnimJoint377.children.append(HAnimSegment378)
HAnimJoint382 = x3d.HAnimJoint()
HAnimJoint382.DEF = "STD_Joint_vc1"
HAnimJoint382.name = "vc1"
HAnimJoint382.center = [0.0066,1.6144,-0.0034]
HAnimSegment383 = x3d.HAnimSegment()
HAnimSegment383.DEF = "STD_Segment_c1"
HAnimSegment383.name = "c1"

HAnimJoint382.children.append(HAnimSegment383)
HAnimJoint384 = x3d.HAnimJoint()
HAnimJoint384.DEF = "STD_Joint_skullbase"
HAnimJoint384.name = "skullbase"
HAnimJoint384.center = [0.0044,1.6209,0.0236]
HAnimSegment385 = x3d.HAnimSegment()
HAnimSegment385.DEF = "STD_Segment_skull"
HAnimSegment385.name = "skull"
HAnimSite386 = x3d.HAnimSite()
HAnimSite386.DEF = "STD_Site_l_ectocanthus_pt"
HAnimSite386.name = "l_ectocanthus_pt"
HAnimSite386.scale = [0.0225,0.0225,0.0225]
TouchSensor387 = x3d.TouchSensor()
TouchSensor387.description = "HAnimSite l_ectocanthus_pt"

HAnimSite386.children.append(TouchSensor387)
Shape388 = x3d.Shape()
Shape388.USE = "HAnimSiteShape"

HAnimSite386.children.append(Shape388)

HAnimSegment385.children.append(HAnimSite386)
HAnimSite389 = x3d.HAnimSite()
HAnimSite389.DEF = "STD_Site_skull_vertex_pt"
HAnimSite389.name = "skull_vertex_pt"
HAnimSite389.scale = [0.0225,0.0225,0.0225]
HAnimSite389.translation = [0.0050,1.7504,0.0055]
TouchSensor390 = x3d.TouchSensor()
TouchSensor390.description = "HAnimSite skull_vertex_pt"

HAnimSite389.children.append(TouchSensor390)
Shape391 = x3d.Shape()
Shape391.USE = "HAnimSiteShape"

HAnimSite389.children.append(Shape391)

HAnimSegment385.children.append(HAnimSite389)
HAnimSite392 = x3d.HAnimSite()
HAnimSite392.DEF = "STD_Site_r_ectocanthus_pt"
HAnimSite392.name = "r_ectocanthus_pt"
HAnimSite392.scale = [0.0225,0.0225,0.0225]
TouchSensor393 = x3d.TouchSensor()
TouchSensor393.description = "HAnimSite r_ectocanthus_pt"

HAnimSite392.children.append(TouchSensor393)
Shape394 = x3d.Shape()
Shape394.USE = "HAnimSiteShape"

HAnimSite392.children.append(Shape394)

HAnimSegment385.children.append(HAnimSite392)
HAnimSite395 = x3d.HAnimSite()
HAnimSite395.DEF = "STD_Site_nuchale_pt"
HAnimSite395.name = "nuchale_pt"
HAnimSite395.scale = [0.0225,0.0225,0.0225]
HAnimSite395.translation = [0.0039,1.5972,-0.0796]
TouchSensor396 = x3d.TouchSensor()
TouchSensor396.description = "HAnimSite nuchale_pt"

HAnimSite395.children.append(TouchSensor396)
Shape397 = x3d.Shape()
Shape397.USE = "HAnimSiteShape"

HAnimSite395.children.append(Shape397)

HAnimSegment385.children.append(HAnimSite395)
HAnimSite398 = x3d.HAnimSite()
HAnimSite398.DEF = "STD_Site_opisthocranion_pt"
HAnimSite398.name = "opisthocranion_pt"
HAnimSite398.scale = [0.0225,0.0225,0.0225]
TouchSensor399 = x3d.TouchSensor()
TouchSensor399.description = "HAnimSite opisthocranion_pt"

HAnimSite398.children.append(TouchSensor399)
Shape400 = x3d.Shape()
Shape400.USE = "HAnimSiteShape"

HAnimSite398.children.append(Shape400)

HAnimSegment385.children.append(HAnimSite398)
HAnimSite401 = x3d.HAnimSite()
HAnimSite401.DEF = "STD_Site_r_infraorbitale_pt"
HAnimSite401.name = "r_infraorbitale_pt"
HAnimSite401.scale = [0.0225,0.0225,0.0225]
HAnimSite401.translation = [-0.0237,1.6171,0.0752]
TouchSensor402 = x3d.TouchSensor()
TouchSensor402.description = "HAnimSite r_infraorbitale_pt"

HAnimSite401.children.append(TouchSensor402)
Shape403 = x3d.Shape()
Shape403.USE = "HAnimSiteShape"

HAnimSite401.children.append(Shape403)

HAnimSegment385.children.append(HAnimSite401)
HAnimSite404 = x3d.HAnimSite()
HAnimSite404.DEF = "STD_Site_r_tragion_pt"
HAnimSite404.name = "r_tragion_pt"
HAnimSite404.scale = [0.0225,0.0225,0.0225]
HAnimSite404.translation = [-0.0646,1.6347,0.0302]
TouchSensor405 = x3d.TouchSensor()
TouchSensor405.description = "HAnimSite r_tragion_pt"

HAnimSite404.children.append(TouchSensor405)
Shape406 = x3d.Shape()
Shape406.USE = "HAnimSiteShape"

HAnimSite404.children.append(Shape406)

HAnimSegment385.children.append(HAnimSite404)
HAnimSite407 = x3d.HAnimSite()
HAnimSite407.DEF = "STD_Site_l_tragion_pt"
HAnimSite407.name = "l_tragion_pt"
HAnimSite407.scale = [0.0225,0.0225,0.0225]
HAnimSite407.translation = [0.0739,1.6348,0.0282]
TouchSensor408 = x3d.TouchSensor()
TouchSensor408.description = "HAnimSite l_tragion_pt"

HAnimSite407.children.append(TouchSensor408)
Shape409 = x3d.Shape()
Shape409.USE = "HAnimSiteShape"

HAnimSite407.children.append(Shape409)

HAnimSegment385.children.append(HAnimSite407)
HAnimSite410 = x3d.HAnimSite()
HAnimSite410.DEF = "STD_Site_sellion_pt"
HAnimSite410.name = "sellion_pt"
HAnimSite410.scale = [0.0225,0.0225,0.0225]
HAnimSite410.translation = [0.0058,1.6316,0.0852]
TouchSensor411 = x3d.TouchSensor()
TouchSensor411.description = "HAnimSite sellion_pt"

HAnimSite410.children.append(TouchSensor411)
Shape412 = x3d.Shape()
Shape412.USE = "HAnimSiteShape"

HAnimSite410.children.append(Shape412)

HAnimSegment385.children.append(HAnimSite410)
HAnimSite413 = x3d.HAnimSite()
HAnimSite413.DEF = "STD_Site_l_infraorbitale_pt"
HAnimSite413.name = "l_infraorbitale_pt"
HAnimSite413.scale = [0.0225,0.0225,0.0225]
HAnimSite413.translation = [0.0341,1.6171,0.0752]
TouchSensor414 = x3d.TouchSensor()
TouchSensor414.description = "HAnimSite l_infraorbitale_pt"

HAnimSite413.children.append(TouchSensor414)
Shape415 = x3d.Shape()
Shape415.USE = "HAnimSiteShape"

HAnimSite413.children.append(Shape415)

HAnimSegment385.children.append(HAnimSite413)
HAnimSite416 = x3d.HAnimSite()
HAnimSite416.DEF = "STD_Site_glabella_pt"
HAnimSite416.name = "glabella_pt"
HAnimSite416.scale = [0.0225,0.0225,0.0225]
TouchSensor417 = x3d.TouchSensor()
TouchSensor417.description = "HAnimSite glabella_pt"

HAnimSite416.children.append(TouchSensor417)
Shape418 = x3d.Shape()
Shape418.USE = "HAnimSiteShape"

HAnimSite416.children.append(Shape418)

HAnimSegment385.children.append(HAnimSite416)

HAnimJoint384.children.append(HAnimSegment385)
HAnimJoint419 = x3d.HAnimJoint()
HAnimJoint419.DEF = "STD_Joint_l_eyelid_joint"
HAnimJoint419.name = "l_eyelid_joint"
HAnimJoint419.center = [0,0,0]
HAnimSegment420 = x3d.HAnimSegment()
HAnimSegment420.DEF = "STD_Segment_l_eyelid"
HAnimSegment420.name = "l_eyelid"

HAnimJoint419.children.append(HAnimSegment420)
HAnimJoint421 = x3d.HAnimJoint()
HAnimJoint421.DEF = "STD_Joint_r_eyelid_joint"
HAnimJoint421.name = "r_eyelid_joint"
HAnimJoint421.center = [0,0,0]
HAnimSegment422 = x3d.HAnimSegment()
HAnimSegment422.DEF = "STD_Segment_r_eyelid"
HAnimSegment422.name = "r_eyelid"

HAnimJoint421.children.append(HAnimSegment422)
HAnimJoint423 = x3d.HAnimJoint()
HAnimJoint423.DEF = "STD_Joint_l_eyeball_joint"
HAnimJoint423.name = "l_eyeball_joint"
HAnimJoint423.center = [0,0,0]
HAnimSegment424 = x3d.HAnimSegment()
HAnimSegment424.DEF = "STD_Segment_l_eyeball"
HAnimSegment424.name = "l_eyeball"

HAnimJoint423.children.append(HAnimSegment424)
HAnimJoint425 = x3d.HAnimJoint()
HAnimJoint425.DEF = "STD_Joint_r_eyeball_joint"
HAnimJoint425.name = "r_eyeball_joint"
HAnimJoint425.center = [0,0,0]
HAnimSegment426 = x3d.HAnimSegment()
HAnimSegment426.DEF = "STD_Segment_r_eyeball"
HAnimSegment426.name = "r_eyeball"

HAnimJoint425.children.append(HAnimSegment426)
HAnimJoint427 = x3d.HAnimJoint()
HAnimJoint427.DEF = "STD_Joint_l_eyebrow_joint"
HAnimJoint427.name = "l_eyebrow_joint"
HAnimJoint427.center = [0,0,0]
HAnimSegment428 = x3d.HAnimSegment()
HAnimSegment428.DEF = "STD_Segment_l_eyebrow"
HAnimSegment428.name = "l_eyebrow"

HAnimJoint427.children.append(HAnimSegment428)
HAnimJoint429 = x3d.HAnimJoint()
HAnimJoint429.DEF = "STD_Joint_r_eyebrow_joint"
HAnimJoint429.name = "r_eyebrow_joint"
HAnimJoint429.center = [0,0,0]
HAnimSegment430 = x3d.HAnimSegment()
HAnimSegment430.DEF = "STD_Segment_r_eyebrow"
HAnimSegment430.name = "r_eyebrow"

HAnimJoint429.children.append(HAnimSegment430)
HAnimJoint431 = x3d.HAnimJoint()
HAnimJoint431.DEF = "STD_Joint_temporomandibular"
HAnimJoint431.name = "temporomandibular"
HAnimJoint431.center = [0,0,0]
HAnimSegment432 = x3d.HAnimSegment()
HAnimSegment432.DEF = "STD_Segment_jaw"
HAnimSegment432.name = "jaw"
HAnimSite433 = x3d.HAnimSite()
HAnimSite433.DEF = "STD_Site_menton_pt"
HAnimSite433.name = "menton_pt"
HAnimSite433.scale = [0.0225,0.0225,0.0225]
TouchSensor434 = x3d.TouchSensor()
TouchSensor434.description = "HAnimSite menton_pt"

HAnimSite433.children.append(TouchSensor434)
Shape435 = x3d.Shape()
Shape435.USE = "HAnimSiteShape"

HAnimSite433.children.append(Shape435)

HAnimSegment432.children.append(HAnimSite433)
HAnimSite436 = x3d.HAnimSite()
HAnimSite436.DEF = "STD_Site_l_gonion_pt"
HAnimSite436.name = "l_gonion_pt"
HAnimSite436.scale = [0.0225,0.0225,0.0225]
HAnimSite436.translation = [0.0631,1.5530,0.0330]
TouchSensor437 = x3d.TouchSensor()
TouchSensor437.description = "HAnimSite l_gonion_pt"

HAnimSite436.children.append(TouchSensor437)
Shape438 = x3d.Shape()
Shape438.USE = "HAnimSiteShape"

HAnimSite436.children.append(Shape438)

HAnimSegment432.children.append(HAnimSite436)
HAnimSite439 = x3d.HAnimSite()
HAnimSite439.DEF = "STD_Site_supramenton_pt"
HAnimSite439.name = "supramenton_pt"
HAnimSite439.scale = [0.0225,0.0225,0.0225]
HAnimSite439.translation = [0.0061,1.5410,0.0805]
TouchSensor440 = x3d.TouchSensor()
TouchSensor440.description = "HAnimSite supramenton_pt"

HAnimSite439.children.append(TouchSensor440)
Shape441 = x3d.Shape()
Shape441.USE = "HAnimSiteShape"

HAnimSite439.children.append(Shape441)

HAnimSegment432.children.append(HAnimSite439)
HAnimSite442 = x3d.HAnimSite()
HAnimSite442.DEF = "STD_Site_r_gonion_pt"
HAnimSite442.name = "r_gonion_pt"
HAnimSite442.scale = [0.0225,0.0225,0.0225]
HAnimSite442.translation = [-0.0520,1.5529,0.0347]
TouchSensor443 = x3d.TouchSensor()
TouchSensor443.description = "HAnimSite r_gonion_pt"

HAnimSite442.children.append(TouchSensor443)
Shape444 = x3d.Shape()
Shape444.USE = "HAnimSiteShape"

HAnimSite442.children.append(Shape444)

HAnimSegment432.children.append(HAnimSite442)

HAnimJoint431.children.append(HAnimSegment432)

HAnimJoint429.children.append(HAnimJoint431)

HAnimJoint427.children.append(HAnimJoint429)

HAnimJoint425.children.append(HAnimJoint427)

HAnimJoint423.children.append(HAnimJoint425)

HAnimJoint421.children.append(HAnimJoint423)

HAnimJoint419.children.append(HAnimJoint421)

HAnimJoint384.children.append(HAnimJoint419)

HAnimJoint382.children.append(HAnimJoint384)

HAnimJoint377.children.append(HAnimJoint382)

HAnimJoint375.children.append(HAnimJoint377)

HAnimJoint373.children.append(HAnimJoint375)

HAnimJoint371.children.append(HAnimJoint373)

HAnimJoint369.children.append(HAnimJoint371)

HAnimJoint361.children.append(HAnimJoint369)

HAnimJoint353.children.append(HAnimJoint361)
HAnimJoint445 = x3d.HAnimJoint()
HAnimJoint445.DEF = "STD_Joint_l_sternoclavicular"
HAnimJoint445.name = "l_sternoclavicular"
HAnimJoint445.center = [0.0820,1.4488,-0.0353]
HAnimSegment446 = x3d.HAnimSegment()
HAnimSegment446.DEF = "STD_Segment_l_clavicle"
HAnimSegment446.name = "l_clavicle"
HAnimSite447 = x3d.HAnimSite()
HAnimSite447.DEF = "STD_Site_l_axilla_posterior_folds_pt"
HAnimSite447.name = "l_axilla_posterior_folds_pt"
HAnimSite447.scale = [0.0225,0.0225,0.0225]
TouchSensor448 = x3d.TouchSensor()
TouchSensor448.description = "HAnimSite l_axilla_posterior_folds_pt"

HAnimSite447.children.append(TouchSensor448)
Shape449 = x3d.Shape()
Shape449.USE = "HAnimSiteShape"

HAnimSite447.children.append(Shape449)

HAnimSegment446.children.append(HAnimSite447)
HAnimSite450 = x3d.HAnimSite()
HAnimSite450.DEF = "STD_Site_l_acromion_pt"
HAnimSite450.name = "l_acromion_pt"
HAnimSite450.scale = [0.0225,0.0225,0.0225]
HAnimSite450.translation = [0.2032,1.4760,-0.0490]
TouchSensor451 = x3d.TouchSensor()
TouchSensor451.description = "HAnimSite l_acromion_pt"

HAnimSite450.children.append(TouchSensor451)
Shape452 = x3d.Shape()
Shape452.USE = "HAnimSiteShape"

HAnimSite450.children.append(Shape452)

HAnimSegment446.children.append(HAnimSite450)
HAnimSite453 = x3d.HAnimSite()
HAnimSite453.DEF = "STD_Site_l_axilla_distal_pt"
HAnimSite453.name = "l_axilla_distal_pt"
HAnimSite453.scale = [0.0225,0.0225,0.0225]
HAnimSite453.translation = [0.1706,1.4072,-0.0875]
TouchSensor454 = x3d.TouchSensor()
TouchSensor454.description = "HAnimSite l_axilla_distal_pt"

HAnimSite453.children.append(TouchSensor454)
Shape455 = x3d.Shape()
Shape455.USE = "HAnimSiteShape"

HAnimSite453.children.append(Shape455)

HAnimSegment446.children.append(HAnimSite453)
HAnimSite456 = x3d.HAnimSite()
HAnimSite456.DEF = "STD_Site_l_axilla_proximal_pt"
HAnimSite456.name = "l_axilla_proximal_pt"
HAnimSite456.scale = [0.0225,0.0225,0.0225]
HAnimSite456.translation = [0.1777,1.4065,-0.0075]
TouchSensor457 = x3d.TouchSensor()
TouchSensor457.description = "HAnimSite l_axilla_proximal_pt"

HAnimSite456.children.append(TouchSensor457)
Shape458 = x3d.Shape()
Shape458.USE = "HAnimSiteShape"

HAnimSite456.children.append(Shape458)

HAnimSegment446.children.append(HAnimSite456)
HAnimSite459 = x3d.HAnimSite()
HAnimSite459.DEF = "STD_Site_l_clavicale_pt"
HAnimSite459.name = "l_clavicale_pt"
HAnimSite459.scale = [0.0225,0.0225,0.0225]
HAnimSite459.translation = [0.0271,1.4943,0.0394]
TouchSensor460 = x3d.TouchSensor()
TouchSensor460.description = "HAnimSite l_clavicale_pt"

HAnimSite459.children.append(TouchSensor460)
Shape461 = x3d.Shape()
Shape461.USE = "HAnimSiteShape"

HAnimSite459.children.append(Shape461)

HAnimSegment446.children.append(HAnimSite459)

HAnimJoint445.children.append(HAnimSegment446)
HAnimJoint462 = x3d.HAnimJoint()
HAnimJoint462.DEF = "STD_Joint_l_acromioclavicular"
HAnimJoint462.name = "l_acromioclavicular"
HAnimJoint462.center = [0.0962,1.4269,-0.0424]
HAnimSegment463 = x3d.HAnimSegment()
HAnimSegment463.DEF = "STD_Segment_l_scapula"
HAnimSegment463.name = "l_scapula"

HAnimJoint462.children.append(HAnimSegment463)
HAnimJoint464 = x3d.HAnimJoint()
HAnimJoint464.DEF = "STD_Joint_l_shoulder"
HAnimJoint464.name = "l_shoulder"
HAnimJoint464.center = [0.2029,1.4376,-0.0387]
HAnimSegment465 = x3d.HAnimSegment()
HAnimSegment465.DEF = "STD_Segment_l_upperarm"
HAnimSegment465.name = "l_upperarm"
HAnimSite466 = x3d.HAnimSite()
HAnimSite466.DEF = "STD_Site_l_humeral_lateral_epicondyles_pt"
HAnimSite466.name = "l_humeral_lateral_epicondyles_pt"
HAnimSite466.scale = [0.0225,0.0225,0.0225]
HAnimSite466.translation = [0.2280,1.1482,-0.1100]
TouchSensor467 = x3d.TouchSensor()
TouchSensor467.description = "HAnimSite l_humeral_lateral_epicondyles_pt"

HAnimSite466.children.append(TouchSensor467)
Shape468 = x3d.Shape()
Shape468.USE = "HAnimSiteShape"

HAnimSite466.children.append(Shape468)

HAnimSegment465.children.append(HAnimSite466)
HAnimSite469 = x3d.HAnimSite()
HAnimSite469.DEF = "STD_Site_l_bideltoid_pt"
HAnimSite469.name = "l_bideltoid_pt"
HAnimSite469.scale = [0.0225,0.0225,0.0225]
TouchSensor470 = x3d.TouchSensor()
TouchSensor470.description = "HAnimSite l_bideltoid_pt"

HAnimSite469.children.append(TouchSensor470)
Shape471 = x3d.Shape()
Shape471.USE = "HAnimSiteShape"

HAnimSite469.children.append(Shape471)

HAnimSegment465.children.append(HAnimSite469)

HAnimJoint464.children.append(HAnimSegment465)
HAnimJoint472 = x3d.HAnimJoint()
HAnimJoint472.DEF = "STD_Joint_l_elbow"
HAnimJoint472.name = "l_elbow"
HAnimJoint472.center = [0.2014,1.1357,-0.0682]
HAnimSegment473 = x3d.HAnimSegment()
HAnimSegment473.DEF = "STD_Segment_l_forearm"
HAnimSegment473.name = "l_forearm"
HAnimSite474 = x3d.HAnimSite()
HAnimSite474.DEF = "STD_Site_l_olecranon_pt"
HAnimSite474.name = "l_olecranon_pt"
HAnimSite474.scale = [0.0225,0.0225,0.0225]
HAnimSite474.translation = [-0.1962,1.1375,-0.1123]
TouchSensor475 = x3d.TouchSensor()
TouchSensor475.description = "HAnimSite l_olecranon_pt"

HAnimSite474.children.append(TouchSensor475)
Shape476 = x3d.Shape()
Shape476.USE = "HAnimSiteShape"

HAnimSite474.children.append(Shape476)

HAnimSegment473.children.append(HAnimSite474)
HAnimSite477 = x3d.HAnimSite()
HAnimSite477.DEF = "STD_Site_l_radiale_pt"
HAnimSite477.name = "l_radiale_pt"
HAnimSite477.scale = [0.0225,0.0225,0.0225]
HAnimSite477.translation = [0.2182,1.1212,-0.1167]
TouchSensor478 = x3d.TouchSensor()
TouchSensor478.description = "HAnimSite l_radiale_pt"

HAnimSite477.children.append(TouchSensor478)
Shape479 = x3d.Shape()
Shape479.USE = "HAnimSiteShape"

HAnimSite477.children.append(Shape479)

HAnimSegment473.children.append(HAnimSite477)
HAnimSite480 = x3d.HAnimSite()
HAnimSite480.DEF = "STD_Site_l_humeral_medial_epicondyles_pt"
HAnimSite480.name = "l_humeral_medial_epicondyles_pt"
HAnimSite480.scale = [0.0225,0.0225,0.0225]
HAnimSite480.translation = [0.1735,1.1272,-0.1113]
TouchSensor481 = x3d.TouchSensor()
TouchSensor481.description = "HAnimSite l_humeral_medial_epicondyles_pt"

HAnimSite480.children.append(TouchSensor481)
Shape482 = x3d.Shape()
Shape482.USE = "HAnimSiteShape"

HAnimSite480.children.append(Shape482)

HAnimSegment473.children.append(HAnimSite480)
HAnimSite483 = x3d.HAnimSite()
HAnimSite483.DEF = "STD_Site_l_radial_styloid_pt"
HAnimSite483.name = "l_radial_styloid_pt"
HAnimSite483.scale = [0.0225,0.0225,0.0225]
HAnimSite483.translation = [0.1901,0.8645,-0.0415]
TouchSensor484 = x3d.TouchSensor()
TouchSensor484.description = "HAnimSite l_radial_styloid_pt"

HAnimSite483.children.append(TouchSensor484)
Shape485 = x3d.Shape()
Shape485.USE = "HAnimSiteShape"

HAnimSite483.children.append(Shape485)

HAnimSegment473.children.append(HAnimSite483)

HAnimJoint472.children.append(HAnimSegment473)
HAnimJoint486 = x3d.HAnimJoint()
HAnimJoint486.DEF = "STD_Joint_l_radiocarpal"
HAnimJoint486.name = "l_radiocarpal"
HAnimJoint486.center = [0.1984,0.8663,-0.0583]
HAnimSegment487 = x3d.HAnimSegment()
HAnimSegment487.DEF = "STD_Segment_l_carpal"
HAnimSegment487.name = "l_carpal"
HAnimSite488 = x3d.HAnimSite()
HAnimSite488.DEF = "STD_Site_l_ulnar_styloid_pt"
HAnimSite488.name = "l_ulnar_styloid_pt"
HAnimSite488.scale = [0.0225,0.0225,0.0225]
HAnimSite488.translation = [-0.2142,0.8529,-0.0648]
TouchSensor489 = x3d.TouchSensor()
TouchSensor489.description = "HAnimSite l_ulnar_styloid_pt"

HAnimSite488.children.append(TouchSensor489)
Shape490 = x3d.Shape()
Shape490.USE = "HAnimSiteShape"

HAnimSite488.children.append(Shape490)

HAnimSegment487.children.append(HAnimSite488)

HAnimJoint486.children.append(HAnimSegment487)
HAnimJoint491 = x3d.HAnimJoint()
HAnimJoint491.DEF = "STD_Joint_l_midcarpal_1"
HAnimJoint491.name = "l_midcarpal_1"
HAnimJoint491.center = [0,0,0]
HAnimSegment492 = x3d.HAnimSegment()
HAnimSegment492.DEF = "STD_Segment_l_trapezium"
HAnimSegment492.name = "l_trapezium"

HAnimJoint491.children.append(HAnimSegment492)
HAnimJoint493 = x3d.HAnimJoint()
HAnimJoint493.DEF = "STD_Joint_l_carpometacarpal_1"
HAnimJoint493.name = "l_carpometacarpal_1"
HAnimJoint493.center = [0.1924,0.8472,-0.0534]
HAnimSegment494 = x3d.HAnimSegment()
HAnimSegment494.DEF = "STD_Segment_l_metacarpal_1"
HAnimSegment494.name = "l_metacarpal_1"

HAnimJoint493.children.append(HAnimSegment494)
HAnimJoint495 = x3d.HAnimJoint()
HAnimJoint495.DEF = "STD_Joint_l_metacarpophalangeal_1"
HAnimJoint495.name = "l_metacarpophalangeal_1"
HAnimJoint495.center = [0.1951,0.8226,0.0246]
HAnimSegment496 = x3d.HAnimSegment()
HAnimSegment496.DEF = "STD_Segment_l_carpal_proximal_phalanx_1"
HAnimSegment496.name = "l_carpal_proximal_phalanx_1"

HAnimJoint495.children.append(HAnimSegment496)
HAnimJoint497 = x3d.HAnimJoint()
HAnimJoint497.DEF = "STD_Joint_l_carpal_interphalangeal_1"
HAnimJoint497.name = "l_carpal_interphalangeal_1"
HAnimJoint497.center = [0.1955,0.8159,0.0464]
HAnimSegment498 = x3d.HAnimSegment()
HAnimSegment498.DEF = "STD_Segment_l_carpal_distal_phalanx_1"
HAnimSegment498.name = "l_carpal_distal_phalanx_1"
HAnimSite499 = x3d.HAnimSite()
HAnimSite499.DEF = "STD_Site_l_carpal_distal_phalanx_1_tip"
HAnimSite499.name = "l_carpal_distal_phalanx_1_tip"
HAnimSite499.scale = [0.0225,0.0225,0.0225]
TouchSensor500 = x3d.TouchSensor()
TouchSensor500.description = "HAnimSite l_carpal_distal_phalanx_1_tip"

HAnimSite499.children.append(TouchSensor500)
Shape501 = x3d.Shape()
Shape501.USE = "HAnimSiteShape"

HAnimSite499.children.append(Shape501)

HAnimSegment498.children.append(HAnimSite499)

HAnimJoint497.children.append(HAnimSegment498)

HAnimJoint495.children.append(HAnimJoint497)

HAnimJoint493.children.append(HAnimJoint495)

HAnimJoint491.children.append(HAnimJoint493)

HAnimJoint486.children.append(HAnimJoint491)
HAnimJoint502 = x3d.HAnimJoint()
HAnimJoint502.DEF = "STD_Joint_l_midcarpal_2"
HAnimJoint502.name = "l_midcarpal_2"
HAnimJoint502.center = [0,0,0]
HAnimSegment503 = x3d.HAnimSegment()
HAnimSegment503.DEF = "STD_Segment_l_trapezoid"
HAnimSegment503.name = "l_trapezoid"

HAnimJoint502.children.append(HAnimSegment503)
HAnimJoint504 = x3d.HAnimJoint()
HAnimJoint504.DEF = "STD_Joint_l_carpometacarpal_2"
HAnimJoint504.name = "l_carpometacarpal_2"
HAnimJoint504.center = [0.1983,0.8024,-0.0280]
HAnimSegment505 = x3d.HAnimSegment()
HAnimSegment505.DEF = "STD_Segment_l_metacarpal_2"
HAnimSegment505.name = "l_metacarpal_2"
HAnimSite506 = x3d.HAnimSite()
HAnimSite506.DEF = "STD_Site_l_metacarpal_phalanx_2_pt"
HAnimSite506.name = "l_metacarpal_phalanx_2_pt"
HAnimSite506.scale = [0.0225,0.0225,0.0225]
HAnimSite506.translation = [0.2009,0.8139,-0.0237]
TouchSensor507 = x3d.TouchSensor()
TouchSensor507.description = "HAnimSite l_metacarpal_phalanx_2_pt"

HAnimSite506.children.append(TouchSensor507)
Shape508 = x3d.Shape()
Shape508.USE = "HAnimSiteShape"

HAnimSite506.children.append(Shape508)

HAnimSegment505.children.append(HAnimSite506)

HAnimJoint504.children.append(HAnimSegment505)
HAnimJoint509 = x3d.HAnimJoint()
HAnimJoint509.DEF = "STD_Joint_l_metacarpophalangeal_2"
HAnimJoint509.name = "l_metacarpophalangeal_2"
HAnimJoint509.center = [0.1983,0.7815,-0.0280]
HAnimSegment510 = x3d.HAnimSegment()
HAnimSegment510.DEF = "STD_Segment_l_carpal_proximal_phalanx_2 "
HAnimSegment510.name = "l_carpal_proximal_phalanx_2 "

HAnimJoint509.children.append(HAnimSegment510)
HAnimJoint511 = x3d.HAnimJoint()
HAnimJoint511.DEF = "STD_Joint_l_carpal_proximal_interphalangeal_2"
HAnimJoint511.name = "l_carpal_proximal_interphalangeal_2"
HAnimJoint511.center = [0.2017,0.7363,-0.0248]
HAnimSegment512 = x3d.HAnimSegment()
HAnimSegment512.DEF = "STD_Segment_l_carpal_middle_phalanx_2"
HAnimSegment512.name = "l_carpal_middle_phalanx_2"

HAnimJoint511.children.append(HAnimSegment512)
HAnimJoint513 = x3d.HAnimJoint()
HAnimJoint513.DEF = "STD_Joint_l_carpal_distal_interphalangeal_2"
HAnimJoint513.name = "l_carpal_distal_interphalangeal_2"
HAnimJoint513.center = [0.2028,0.7139,-0.0236]
HAnimSegment514 = x3d.HAnimSegment()
HAnimSegment514.DEF = "STD_Segment_l_carpal_distal_phalanx_2"
HAnimSegment514.name = "l_carpal_distal_phalanx_2"
HAnimSite515 = x3d.HAnimSite()
HAnimSite515.DEF = "STD_Site_l_carpal_distal_phalanx_2_tip"
HAnimSite515.name = "l_carpal_distal_phalanx_2_tip"
HAnimSite515.scale = [0.0225,0.0225,0.0225]
TouchSensor516 = x3d.TouchSensor()
TouchSensor516.description = "HAnimSite l_carpal_distal_phalanx_2_tip"

HAnimSite515.children.append(TouchSensor516)
Shape517 = x3d.Shape()
Shape517.USE = "HAnimSiteShape"

HAnimSite515.children.append(Shape517)

HAnimSegment514.children.append(HAnimSite515)
HAnimSite518 = x3d.HAnimSite()
HAnimSite518.DEF = "STD_Site_l_dactylion_pt"
HAnimSite518.name = "l_dactylion_pt"
HAnimSite518.scale = [0.0225,0.0225,0.0225]
HAnimSite518.translation = [0.2056,0.6743,-0.0482]
TouchSensor519 = x3d.TouchSensor()
TouchSensor519.description = "HAnimSite l_dactylion_pt"

HAnimSite518.children.append(TouchSensor519)
Shape520 = x3d.Shape()
Shape520.USE = "HAnimSiteShape"

HAnimSite518.children.append(Shape520)

HAnimSegment514.children.append(HAnimSite518)

HAnimJoint513.children.append(HAnimSegment514)

HAnimJoint511.children.append(HAnimJoint513)

HAnimJoint509.children.append(HAnimJoint511)

HAnimJoint504.children.append(HAnimJoint509)

HAnimJoint502.children.append(HAnimJoint504)

HAnimJoint486.children.append(HAnimJoint502)
HAnimJoint521 = x3d.HAnimJoint()
HAnimJoint521.DEF = "STD_Joint_l_midcarpal_3"
HAnimJoint521.name = "l_midcarpal_3"
HAnimJoint521.center = [0,0,0]
HAnimSegment522 = x3d.HAnimSegment()
HAnimSegment522.DEF = "STD_Segment_l_capitate"
HAnimSegment522.name = "l_capitate"

HAnimJoint521.children.append(HAnimSegment522)
HAnimJoint523 = x3d.HAnimJoint()
HAnimJoint523.DEF = "STD_Joint_l_carpometacarpal_3"
HAnimJoint523.name = "l_carpometacarpal_3"
HAnimJoint523.center = [0.1987,0.8029,-0.0530]
HAnimSegment524 = x3d.HAnimSegment()
HAnimSegment524.DEF = "STD_Segment_l_metacarpal_3"
HAnimSegment524.name = "l_metacarpal_3"
HAnimSite525 = x3d.HAnimSite()
HAnimSite525.DEF = "STD_Site_l_metacarpal_phalanx_3_pt"
HAnimSite525.name = "l_metacarpal_phalanx_3_pt"
HAnimSite525.scale = [0.0225,0.0225,0.0225]
TouchSensor526 = x3d.TouchSensor()
TouchSensor526.description = "HAnimSite l_metacarpal_phalanx_3_pt"

HAnimSite525.children.append(TouchSensor526)
Shape527 = x3d.Shape()
Shape527.USE = "HAnimSiteShape"

HAnimSite525.children.append(Shape527)

HAnimSegment524.children.append(HAnimSite525)

HAnimJoint523.children.append(HAnimSegment524)
HAnimJoint528 = x3d.HAnimJoint()
HAnimJoint528.DEF = "STD_Joint_l_metacarpophalangeal_3"
HAnimJoint528.name = "l_metacarpophalangeal_3"
HAnimJoint528.center = [0.1987,0.7818,-0.0530]
HAnimSegment529 = x3d.HAnimSegment()
HAnimSegment529.DEF = "STD_Segment_l_carpal_proximal_phalanx_3"
HAnimSegment529.name = "l_carpal_proximal_phalanx_3"

HAnimJoint528.children.append(HAnimSegment529)
HAnimJoint530 = x3d.HAnimJoint()
HAnimJoint530.DEF = "STD_Joint_l_carpal_proximal_interphalangeal_3"
HAnimJoint530.name = "l_carpal_proximal_interphalangeal_3"
HAnimJoint530.center = [0.2013,0.7273,-0.0503]
HAnimSegment531 = x3d.HAnimSegment()
HAnimSegment531.DEF = "STD_Segment_l_carpal_middle_phalanx_3"
HAnimSegment531.name = "l_carpal_middle_phalanx_3"

HAnimJoint530.children.append(HAnimSegment531)
HAnimJoint532 = x3d.HAnimJoint()
HAnimJoint532.DEF = "STD_Joint_l_carpal_distal_interphalangeal_3"
HAnimJoint532.name = "l_carpal_distal_interphalangeal_3"
HAnimJoint532.center = [0.2026,0.7011,-0.0494]
HAnimSegment533 = x3d.HAnimSegment()
HAnimSegment533.DEF = "STD_Segment_l_carpal_distal_phalanx_3"
HAnimSegment533.name = "l_carpal_distal_phalanx_3"
HAnimSite534 = x3d.HAnimSite()
HAnimSite534.DEF = "STD_Site_l_carpal_distal_phalanx_3_tip"
HAnimSite534.name = "l_carpal_distal_phalanx_3_tip"
HAnimSite534.scale = [0.0225,0.0225,0.0225]
TouchSensor535 = x3d.TouchSensor()
TouchSensor535.description = "HAnimSite l_carpal_distal_phalanx_3_tip"

HAnimSite534.children.append(TouchSensor535)
Shape536 = x3d.Shape()
Shape536.USE = "HAnimSiteShape"

HAnimSite534.children.append(Shape536)

HAnimSegment533.children.append(HAnimSite534)

HAnimJoint532.children.append(HAnimSegment533)

HAnimJoint530.children.append(HAnimJoint532)

HAnimJoint528.children.append(HAnimJoint530)

HAnimJoint523.children.append(HAnimJoint528)

HAnimJoint521.children.append(HAnimJoint523)

HAnimJoint486.children.append(HAnimJoint521)
HAnimJoint537 = x3d.HAnimJoint()
HAnimJoint537.DEF = "STD_Joint_l_midcarpal_4_5"
HAnimJoint537.name = "l_midcarpal_4_5"
HAnimJoint537.center = [0,0,0]
HAnimSegment538 = x3d.HAnimSegment()
HAnimSegment538.DEF = "STD_Segment_l_hamate"
HAnimSegment538.name = "l_hamate"

HAnimJoint537.children.append(HAnimSegment538)
HAnimJoint539 = x3d.HAnimJoint()
HAnimJoint539.DEF = "STD_Joint_l_carpometacarpal_4"
HAnimJoint539.name = "l_carpometacarpal_4"
HAnimJoint539.center = [0.1956,0.8019,-0.0794]
HAnimSegment540 = x3d.HAnimSegment()
HAnimSegment540.DEF = "STD_Segment_l_metacarpal_4"
HAnimSegment540.name = "l_metacarpal_4"

HAnimJoint539.children.append(HAnimSegment540)
HAnimJoint541 = x3d.HAnimJoint()
HAnimJoint541.DEF = "STD_Joint_l_metacarpophalangeal_4"
HAnimJoint541.name = "l_metacarpophalangeal_4"
HAnimJoint541.center = [0.1956,0.7815,-0.0794]
HAnimSegment542 = x3d.HAnimSegment()
HAnimSegment542.DEF = "STD_Segment_l_carpal_proximal_phalanx_4"
HAnimSegment542.name = "l_carpal_proximal_phalanx_4"

HAnimJoint541.children.append(HAnimSegment542)
HAnimJoint543 = x3d.HAnimJoint()
HAnimJoint543.DEF = "STD_Joint_l_carpal_proximal_interphalangeal_4"
HAnimJoint543.name = "l_carpal_proximal_interphalangeal_4"
HAnimJoint543.center = [0.1973,0.7287,-0.0777]
HAnimSegment544 = x3d.HAnimSegment()
HAnimSegment544.DEF = "STD_Segment_l_carpal_middle_phalanx_4"
HAnimSegment544.name = "l_carpal_middle_phalanx_4"

HAnimJoint543.children.append(HAnimSegment544)
HAnimJoint545 = x3d.HAnimJoint()
HAnimJoint545.DEF = "STD_Joint_l_carpal_distal_interphalangeal_4"
HAnimJoint545.name = "l_carpal_distal_interphalangeal_4"
HAnimJoint545.center = [0.1983,0.7045,-0.0767]
HAnimSegment546 = x3d.HAnimSegment()
HAnimSegment546.DEF = "STD_Segment_l_carpal_distal_phalanx_4"
HAnimSegment546.name = "l_carpal_distal_phalanx_4"
HAnimSite547 = x3d.HAnimSite()
HAnimSite547.DEF = "STD_Site_l_carpal_distal_phalanx_4_tip"
HAnimSite547.name = "l_carpal_distal_phalanx_4_tip"
HAnimSite547.scale = [0.0225,0.0225,0.0225]
TouchSensor548 = x3d.TouchSensor()
TouchSensor548.description = "HAnimSite l_carpal_distal_phalanx_4_tip"

HAnimSite547.children.append(TouchSensor548)
Shape549 = x3d.Shape()
Shape549.USE = "HAnimSiteShape"

HAnimSite547.children.append(Shape549)

HAnimSegment546.children.append(HAnimSite547)

HAnimJoint545.children.append(HAnimSegment546)

HAnimJoint543.children.append(HAnimJoint545)

HAnimJoint541.children.append(HAnimJoint543)

HAnimJoint539.children.append(HAnimJoint541)

HAnimJoint537.children.append(HAnimJoint539)
HAnimJoint550 = x3d.HAnimJoint()
HAnimJoint550.DEF = "STD_Joint_l_carpometacarpal_5"
HAnimJoint550.name = "l_carpometacarpal_5"
HAnimJoint550.center = [0.1925,0.8066,-0.1036]
HAnimSegment551 = x3d.HAnimSegment()
HAnimSegment551.DEF = "STD_Segment_l_metacarpal_5"
HAnimSegment551.name = "l_metacarpal_5"
HAnimSite552 = x3d.HAnimSite()
HAnimSite552.DEF = "STD_Site_l_metacarpal_phalanx_5_pt"
HAnimSite552.name = "l_metacarpal_phalanx_5_pt"
HAnimSite552.scale = [0.0225,0.0225,0.0225]
HAnimSite552.translation = [0.1929,0.7860,-0.1122]
TouchSensor553 = x3d.TouchSensor()
TouchSensor553.description = "HAnimSite l_metacarpal_phalanx_5_pt"

HAnimSite552.children.append(TouchSensor553)
Shape554 = x3d.Shape()
Shape554.USE = "HAnimSiteShape"

HAnimSite552.children.append(Shape554)

HAnimSegment551.children.append(HAnimSite552)

HAnimJoint550.children.append(HAnimSegment551)
HAnimJoint555 = x3d.HAnimJoint()
HAnimJoint555.DEF = "STD_Joint_l_metacarpophalangeal_5"
HAnimJoint555.name = "l_metacarpophalangeal_5"
HAnimJoint555.center = [0.1925,0.7866,-0.1036]
HAnimSegment556 = x3d.HAnimSegment()
HAnimSegment556.DEF = "STD_Segment_l_carpal_proximal_phalanx_5"
HAnimSegment556.name = "l_carpal_proximal_phalanx_5"

HAnimJoint555.children.append(HAnimSegment556)
HAnimJoint557 = x3d.HAnimJoint()
HAnimJoint557.DEF = "STD_Joint_l_carpal_proximal_interphalangeal_5"
HAnimJoint557.name = "l_carpal_proximal_interphalangeal_5"
HAnimJoint557.center = [0.1938,0.7452,-0.1024]
HAnimSegment558 = x3d.HAnimSegment()
HAnimSegment558.DEF = "STD_Segment_l_carpal_middle_phalanx_5"
HAnimSegment558.name = "l_carpal_middle_phalanx_5"

HAnimJoint557.children.append(HAnimSegment558)
HAnimJoint559 = x3d.HAnimJoint()
HAnimJoint559.DEF = "STD_Joint_l_carpal_distal_interphalangeal_5"
HAnimJoint559.name = "l_carpal_distal_interphalangeal_5"
HAnimJoint559.center = [0.1948,0.7277,-0.1017]
HAnimSegment560 = x3d.HAnimSegment()
HAnimSegment560.DEF = "STD_Segment_l_carpal_distal_phalanx_5"
HAnimSegment560.name = "l_carpal_distal_phalanx_5"
HAnimSite561 = x3d.HAnimSite()
HAnimSite561.DEF = "STD_Site_l_carpal_distal_phalanx_5_tip"
HAnimSite561.name = "l_carpal_distal_phalanx_5_tip"
HAnimSite561.scale = [0.0225,0.0225,0.0225]
TouchSensor562 = x3d.TouchSensor()
TouchSensor562.description = "HAnimSite l_carpal_distal_phalanx_5_tip"

HAnimSite561.children.append(TouchSensor562)
Shape563 = x3d.Shape()
Shape563.USE = "HAnimSiteShape"

HAnimSite561.children.append(Shape563)

HAnimSegment560.children.append(HAnimSite561)

HAnimJoint559.children.append(HAnimSegment560)

HAnimJoint557.children.append(HAnimJoint559)

HAnimJoint555.children.append(HAnimJoint557)

HAnimJoint550.children.append(HAnimJoint555)

HAnimJoint537.children.append(HAnimJoint550)

HAnimJoint486.children.append(HAnimJoint537)

HAnimJoint472.children.append(HAnimJoint486)

HAnimJoint464.children.append(HAnimJoint472)

HAnimJoint462.children.append(HAnimJoint464)

HAnimJoint445.children.append(HAnimJoint462)

HAnimJoint353.children.append(HAnimJoint445)
HAnimJoint564 = x3d.HAnimJoint()
HAnimJoint564.DEF = "STD_Joint_r_sternoclavicular"
HAnimJoint564.name = "r_sternoclavicular"
HAnimJoint564.center = [-0.0694,1.4600,-0.0330]
HAnimSegment565 = x3d.HAnimSegment()
HAnimSegment565.DEF = "STD_Segment_r_clavicle"
HAnimSegment565.name = "r_clavicle"
HAnimSite566 = x3d.HAnimSite()
HAnimSite566.DEF = "STD_Site_r_axilla_posterior_folds_pt"
HAnimSite566.name = "r_axilla_posterior_folds_pt"
HAnimSite566.scale = [0.0225,0.0225,0.0225]
TouchSensor567 = x3d.TouchSensor()
TouchSensor567.description = "HAnimSite r_axilla_posterior_folds_pt"

HAnimSite566.children.append(TouchSensor567)
Shape568 = x3d.Shape()
Shape568.USE = "HAnimSiteShape"

HAnimSite566.children.append(Shape568)

HAnimSegment565.children.append(HAnimSite566)
HAnimSite569 = x3d.HAnimSite()
HAnimSite569.DEF = "STD_Site_r_axilla_distal_pt"
HAnimSite569.name = "r_axilla_distal_pt"
HAnimSite569.scale = [0.0225,0.0225,0.0225]
HAnimSite569.translation = [-0.1603,1.4098,-0.0826]
TouchSensor570 = x3d.TouchSensor()
TouchSensor570.description = "HAnimSite r_axilla_distal_pt"

HAnimSite569.children.append(TouchSensor570)
Shape571 = x3d.Shape()
Shape571.USE = "HAnimSiteShape"

HAnimSite569.children.append(Shape571)

HAnimSegment565.children.append(HAnimSite569)
HAnimSite572 = x3d.HAnimSite()
HAnimSite572.DEF = "STD_Site_r_acromion_pt"
HAnimSite572.name = "r_acromion_pt"
HAnimSite572.scale = [0.0225,0.0225,0.0225]
HAnimSite572.translation = [-0.1905,1.4791,-0.0431]
TouchSensor573 = x3d.TouchSensor()
TouchSensor573.description = "HAnimSite r_acromion_pt"

HAnimSite572.children.append(TouchSensor573)
Shape574 = x3d.Shape()
Shape574.USE = "HAnimSiteShape"

HAnimSite572.children.append(Shape574)

HAnimSegment565.children.append(HAnimSite572)
HAnimSite575 = x3d.HAnimSite()
HAnimSite575.DEF = "STD_Site_r_clavicale_pt"
HAnimSite575.name = "r_clavicale_pt"
HAnimSite575.scale = [0.0225,0.0225,0.0225]
HAnimSite575.translation = [-0.0115,1.4943,0.0400]
TouchSensor576 = x3d.TouchSensor()
TouchSensor576.description = "HAnimSite r_clavicale_pt"

HAnimSite575.children.append(TouchSensor576)
Shape577 = x3d.Shape()
Shape577.USE = "HAnimSiteShape"

HAnimSite575.children.append(Shape577)

HAnimSegment565.children.append(HAnimSite575)
HAnimSite578 = x3d.HAnimSite()
HAnimSite578.DEF = "STD_Site_r_axilla_proximal_pt"
HAnimSite578.name = "r_axilla_proximal_pt"
HAnimSite578.scale = [0.0225,0.0225,0.0225]
HAnimSite578.translation = [-0.1626,1.4072,-0.0031]
TouchSensor579 = x3d.TouchSensor()
TouchSensor579.description = "HAnimSite r_axilla_proximal_pt"

HAnimSite578.children.append(TouchSensor579)
Shape580 = x3d.Shape()
Shape580.USE = "HAnimSiteShape"

HAnimSite578.children.append(Shape580)

HAnimSegment565.children.append(HAnimSite578)

HAnimJoint564.children.append(HAnimSegment565)
HAnimJoint581 = x3d.HAnimJoint()
HAnimJoint581.DEF = "STD_Joint_r_acromioclavicular"
HAnimJoint581.name = "r_acromioclavicular"
HAnimJoint581.center = [-0.0836,1.4281,-0.0401]
HAnimSegment582 = x3d.HAnimSegment()
HAnimSegment582.DEF = "STD_Segment_r_scapula"
HAnimSegment582.name = "r_scapula"

HAnimJoint581.children.append(HAnimSegment582)
HAnimJoint583 = x3d.HAnimJoint()
HAnimJoint583.DEF = "STD_Joint_r_shoulder"
HAnimJoint583.name = "r_shoulder"
HAnimJoint583.center = [-0.1907,1.4407,-0.0325]
HAnimSegment584 = x3d.HAnimSegment()
HAnimSegment584.DEF = "STD_Segment_r_upperarm"
HAnimSegment584.name = "r_upperarm"
HAnimSite585 = x3d.HAnimSite()
HAnimSite585.DEF = "STD_Site_r_humeral_lateral_epicondyles_pt"
HAnimSite585.name = "r_humeral_lateral_epicondyles_pt"
HAnimSite585.scale = [0.0225,0.0225,0.0225]
HAnimSite585.translation = [-0.2224,1.1517,-0.1033]
TouchSensor586 = x3d.TouchSensor()
TouchSensor586.description = "HAnimSite r_humeral_lateral_epicondyles_pt"

HAnimSite585.children.append(TouchSensor586)
Shape587 = x3d.Shape()
Shape587.USE = "HAnimSiteShape"

HAnimSite585.children.append(Shape587)

HAnimSegment584.children.append(HAnimSite585)
HAnimSite588 = x3d.HAnimSite()
HAnimSite588.DEF = "STD_Site_r_bideltoid_pt"
HAnimSite588.name = "r_bideltoid_pt"
HAnimSite588.scale = [0.0225,0.0225,0.0225]
TouchSensor589 = x3d.TouchSensor()
TouchSensor589.description = "HAnimSite r_bideltoid_pt"

HAnimSite588.children.append(TouchSensor589)
Shape590 = x3d.Shape()
Shape590.USE = "HAnimSiteShape"

HAnimSite588.children.append(Shape590)

HAnimSegment584.children.append(HAnimSite588)

HAnimJoint583.children.append(HAnimSegment584)
HAnimJoint591 = x3d.HAnimJoint()
HAnimJoint591.DEF = "STD_Joint_r_elbow"
HAnimJoint591.name = "r_elbow"
HAnimJoint591.center = [-0.1949,1.1388,-0.0620]
HAnimSegment592 = x3d.HAnimSegment()
HAnimSegment592.DEF = "STD_Segment_r_forearm"
HAnimSegment592.name = "r_forearm"
HAnimSite593 = x3d.HAnimSite()
HAnimSite593.DEF = "STD_Site_r_radiale_pt"
HAnimSite593.name = "r_radiale_pt"
HAnimSite593.scale = [0.0225,0.0225,0.0225]
HAnimSite593.translation = [-0.2130,1.1305,-0.1091]
TouchSensor594 = x3d.TouchSensor()
TouchSensor594.description = "HAnimSite r_radiale_pt"

HAnimSite593.children.append(TouchSensor594)
Shape595 = x3d.Shape()
Shape595.USE = "HAnimSiteShape"

HAnimSite593.children.append(Shape595)

HAnimSegment592.children.append(HAnimSite593)
HAnimSite596 = x3d.HAnimSite()
HAnimSite596.DEF = "STD_Site_r_humeral_medial_epicondyles_pt"
HAnimSite596.name = "r_humeral_medial_epicondyles_pt"
HAnimSite596.scale = [0.0225,0.0225,0.0225]
HAnimSite596.translation = [-0.1680,1.1298,-0.1062]
TouchSensor597 = x3d.TouchSensor()
TouchSensor597.description = "HAnimSite r_humeral_medial_epicondyles_pt"

HAnimSite596.children.append(TouchSensor597)
Shape598 = x3d.Shape()
Shape598.USE = "HAnimSiteShape"

HAnimSite596.children.append(Shape598)

HAnimSegment592.children.append(HAnimSite596)
HAnimSite599 = x3d.HAnimSite()
HAnimSite599.DEF = "STD_Site_r_olecranon_pt"
HAnimSite599.name = "r_olecranon_pt"
HAnimSite599.scale = [0.0225,0.0225,0.0225]
HAnimSite599.translation = [-0.1907,1.1405,-0.1065]
TouchSensor600 = x3d.TouchSensor()
TouchSensor600.description = "HAnimSite r_olecranon_pt"

HAnimSite599.children.append(TouchSensor600)
Shape601 = x3d.Shape()
Shape601.USE = "HAnimSiteShape"

HAnimSite599.children.append(Shape601)

HAnimSegment592.children.append(HAnimSite599)
HAnimSite602 = x3d.HAnimSite()
HAnimSite602.DEF = "STD_Site_r_radial_styloid_pt"
HAnimSite602.name = "r_radial_styloid_pt"
HAnimSite602.scale = [0.0225,0.0225,0.0225]
HAnimSite602.translation = [-0.1884,0.8676,-0.0360]
TouchSensor603 = x3d.TouchSensor()
TouchSensor603.description = "HAnimSite r_radial_styloid_pt"

HAnimSite602.children.append(TouchSensor603)
Shape604 = x3d.Shape()
Shape604.USE = "HAnimSiteShape"

HAnimSite602.children.append(Shape604)

HAnimSegment592.children.append(HAnimSite602)

HAnimJoint591.children.append(HAnimSegment592)
HAnimJoint605 = x3d.HAnimJoint()
HAnimJoint605.DEF = "STD_Joint_r_radiocarpal"
HAnimJoint605.name = "r_radiocarpal"
HAnimJoint605.center = [-0.1959,0.8694,-0.0521]
HAnimSegment606 = x3d.HAnimSegment()
HAnimSegment606.DEF = "STD_Segment_r_carpal"
HAnimSegment606.name = "r_carpal"
HAnimSite607 = x3d.HAnimSite()
HAnimSite607.DEF = "STD_Site_r_ulnar_styloid_pt"
HAnimSite607.name = "r_ulnar_styloid_pt"
HAnimSite607.scale = [0.0225,0.0225,0.0225]
HAnimSite607.translation = [-0.2117,0.8562,-0.0584]
TouchSensor608 = x3d.TouchSensor()
TouchSensor608.description = "HAnimSite r_ulnar_styloid_pt"

HAnimSite607.children.append(TouchSensor608)
Shape609 = x3d.Shape()
Shape609.USE = "HAnimSiteShape"

HAnimSite607.children.append(Shape609)

HAnimSegment606.children.append(HAnimSite607)

HAnimJoint605.children.append(HAnimSegment606)
HAnimJoint610 = x3d.HAnimJoint()
HAnimJoint610.DEF = "STD_Joint_r_midcarpal_1"
HAnimJoint610.name = "r_midcarpal_1"
HAnimJoint610.center = [0,0,0]
HAnimSegment611 = x3d.HAnimSegment()
HAnimSegment611.DEF = "STD_Segment_r_trapezium"
HAnimSegment611.name = "r_trapezium"

HAnimJoint610.children.append(HAnimSegment611)
HAnimJoint612 = x3d.HAnimJoint()
HAnimJoint612.DEF = "STD_Joint_r_carpometacarpal_1"
HAnimJoint612.name = "r_carpometacarpal_1"
HAnimJoint612.center = [-0.1899,0.8502,-0.0473]
HAnimSegment613 = x3d.HAnimSegment()
HAnimSegment613.DEF = "STD_Segment_r_metacarpal_1"
HAnimSegment613.name = "r_metacarpal_1"

HAnimJoint612.children.append(HAnimSegment613)
HAnimJoint614 = x3d.HAnimJoint()
HAnimJoint614.DEF = "STD_Joint_r_metacarpophalangeal_1"
HAnimJoint614.name = "r_metacarpophalangeal_1"
HAnimJoint614.center = [-0.1874,0.8256,0.0306]
HAnimSegment615 = x3d.HAnimSegment()
HAnimSegment615.DEF = "STD_Segment_r_carpal_proximal_phalanx_1"
HAnimSegment615.name = "r_carpal_proximal_phalanx_1"

HAnimJoint614.children.append(HAnimSegment615)
HAnimJoint616 = x3d.HAnimJoint()
HAnimJoint616.DEF = "STD_Joint_r_carpal_interphalangeal_1"
HAnimJoint616.name = "r_carpal_interphalangeal_1"
HAnimJoint616.center = [-0.1864,0.8190,0.0506]
HAnimSegment617 = x3d.HAnimSegment()
HAnimSegment617.DEF = "STD_Segment_r_carpal_distal_phalanx_1"
HAnimSegment617.name = "r_carpal_distal_phalanx_1"
HAnimSite618 = x3d.HAnimSite()
HAnimSite618.DEF = "STD_Site_r_carpal_distal_phalanx_1_tip"
HAnimSite618.name = "r_carpal_distal_phalanx_1_tip"
HAnimSite618.scale = [0.0225,0.0225,0.0225]
TouchSensor619 = x3d.TouchSensor()
TouchSensor619.description = "HAnimSite r_carpal_distal_phalanx_1_tip"

HAnimSite618.children.append(TouchSensor619)
Shape620 = x3d.Shape()
Shape620.USE = "HAnimSiteShape"

HAnimSite618.children.append(Shape620)

HAnimSegment617.children.append(HAnimSite618)

HAnimJoint616.children.append(HAnimSegment617)

HAnimJoint614.children.append(HAnimJoint616)

HAnimJoint612.children.append(HAnimJoint614)

HAnimJoint610.children.append(HAnimJoint612)

HAnimJoint605.children.append(HAnimJoint610)
HAnimJoint621 = x3d.HAnimJoint()
HAnimJoint621.DEF = "STD_Joint_r_midcarpal_2"
HAnimJoint621.name = "r_midcarpal_2"
HAnimJoint621.center = [0,0,0]
HAnimSegment622 = x3d.HAnimSegment()
HAnimSegment622.DEF = "STD_Segment_r_trapezoid"
HAnimSegment622.name = "r_trapezoid"

HAnimJoint621.children.append(HAnimSegment622)
HAnimJoint623 = x3d.HAnimJoint()
HAnimJoint623.DEF = "STD_Joint_r_carpometacarpal_2"
HAnimJoint623.name = "r_carpometacarpal_2"
HAnimJoint623.center = [-0.1961,0.8055,-0.0218]
HAnimSegment624 = x3d.HAnimSegment()
HAnimSegment624.DEF = "STD_Segment_r_metacarpal_2"
HAnimSegment624.name = "r_metacarpal_2"
HAnimSite625 = x3d.HAnimSite()
HAnimSite625.DEF = "STD_Site_r_metacarpal_phalanx_2_pt"
HAnimSite625.name = "r_metacarpal_phalanx_2_pt"
HAnimSite625.scale = [0.0225,0.0225,0.0225]
HAnimSite625.translation = [-0.1977,0.8169,-0.0177]
TouchSensor626 = x3d.TouchSensor()
TouchSensor626.description = "HAnimSite r_metacarpal_phalanx_2_pt"

HAnimSite625.children.append(TouchSensor626)
Shape627 = x3d.Shape()
Shape627.USE = "HAnimSiteShape"

HAnimSite625.children.append(Shape627)

HAnimSegment624.children.append(HAnimSite625)

HAnimJoint623.children.append(HAnimSegment624)
HAnimJoint628 = x3d.HAnimJoint()
HAnimJoint628.DEF = "STD_Joint_r_metacarpophalangeal_2"
HAnimJoint628.name = "r_metacarpophalangeal_2"
HAnimJoint628.center = [-0.1961,0.7846,-0.0218]
HAnimSegment629 = x3d.HAnimSegment()
HAnimSegment629.DEF = "STD_Segment_r_carpal_proximal_phalanx_2 "
HAnimSegment629.name = "r_carpal_proximal_phalanx_2 "

HAnimJoint628.children.append(HAnimSegment629)
HAnimJoint630 = x3d.HAnimJoint()
HAnimJoint630.DEF = "STD_Joint_r_carpal_proximal_interphalangeal_2"
HAnimJoint630.name = "r_carpal_proximal_interphalangeal_2"
HAnimJoint630.center = [-0.1954,0.7393,-0.0185]
HAnimSegment631 = x3d.HAnimSegment()
HAnimSegment631.DEF = "STD_Segment_r_carpal_middle_phalanx_2"
HAnimSegment631.name = "r_carpal_middle_phalanx_2"

HAnimJoint630.children.append(HAnimSegment631)
HAnimJoint632 = x3d.HAnimJoint()
HAnimJoint632.DEF = "STD_Joint_r_carpal_distal_interphalangeal_2"
HAnimJoint632.name = "r_carpal_distal_interphalangeal_2"
HAnimJoint632.center = [-0.1945,0.7169,-0.0173]
HAnimSegment633 = x3d.HAnimSegment()
HAnimSegment633.DEF = "STD_Segment_r_carpal_distal_phalanx_2"
HAnimSegment633.name = "r_carpal_distal_phalanx_2"
HAnimSite634 = x3d.HAnimSite()
HAnimSite634.DEF = "STD_Site_r_carpal_distal_phalanx_2_tip"
HAnimSite634.name = "r_carpal_distal_phalanx_2_tip"
HAnimSite634.scale = [0.0225,0.0225,0.0225]
TouchSensor635 = x3d.TouchSensor()
TouchSensor635.description = "HAnimSite r_carpal_distal_phalanx_2_tip"

HAnimSite634.children.append(TouchSensor635)
Shape636 = x3d.Shape()
Shape636.USE = "HAnimSiteShape"

HAnimSite634.children.append(Shape636)

HAnimSegment633.children.append(HAnimSite634)
HAnimSite637 = x3d.HAnimSite()
HAnimSite637.DEF = "STD_Site_r_dactylion_pt"
HAnimSite637.name = "r_dactylion_pt"
HAnimSite637.scale = [0.0225,0.0225,0.0225]
HAnimSite637.translation = [-0.1941,0.6772,-0.0423]
TouchSensor638 = x3d.TouchSensor()
TouchSensor638.description = "HAnimSite r_dactylion_pt"

HAnimSite637.children.append(TouchSensor638)
Shape639 = x3d.Shape()
Shape639.USE = "HAnimSiteShape"

HAnimSite637.children.append(Shape639)

HAnimSegment633.children.append(HAnimSite637)

HAnimJoint632.children.append(HAnimSegment633)

HAnimJoint630.children.append(HAnimJoint632)

HAnimJoint628.children.append(HAnimJoint630)

HAnimJoint623.children.append(HAnimJoint628)

HAnimJoint621.children.append(HAnimJoint623)

HAnimJoint605.children.append(HAnimJoint621)
HAnimJoint640 = x3d.HAnimJoint()
HAnimJoint640.DEF = "STD_Joint_r_midcarpal_3"
HAnimJoint640.name = "r_midcarpal_3"
HAnimJoint640.center = [0,0,0]
HAnimSegment641 = x3d.HAnimSegment()
HAnimSegment641.DEF = "STD_Segment_r_capitate"
HAnimSegment641.name = "r_capitate"

HAnimJoint640.children.append(HAnimSegment641)
HAnimJoint642 = x3d.HAnimJoint()
HAnimJoint642.DEF = "STD_Joint_r_carpometacarpal_3"
HAnimJoint642.name = "r_carpometacarpal_3"
HAnimJoint642.center = [-0.1972,0.8060,-0.0468]
HAnimSegment643 = x3d.HAnimSegment()
HAnimSegment643.DEF = "STD_Segment_r_metacarpal_3"
HAnimSegment643.name = "r_metacarpal_3"
HAnimSite644 = x3d.HAnimSite()
HAnimSite644.DEF = "STD_Site_r_metacarpal_phalanx_3_pt"
HAnimSite644.name = "r_metacarpal_phalanx_3_pt"
HAnimSite644.scale = [0.0225,0.0225,0.0225]
TouchSensor645 = x3d.TouchSensor()
TouchSensor645.description = "HAnimSite r_metacarpal_phalanx_3_pt"

HAnimSite644.children.append(TouchSensor645)
Shape646 = x3d.Shape()
Shape646.USE = "HAnimSiteShape"

HAnimSite644.children.append(Shape646)

HAnimSegment643.children.append(HAnimSite644)

HAnimJoint642.children.append(HAnimSegment643)
HAnimJoint647 = x3d.HAnimJoint()
HAnimJoint647.DEF = "STD_Joint_r_metacarpophalangeal_3"
HAnimJoint647.name = "r_metacarpophalangeal_3"
HAnimJoint647.center = [-0.1972,0.7849,-0.0468]
HAnimSegment648 = x3d.HAnimSegment()
HAnimSegment648.DEF = "STD_Segment_r_carpal_proximal_phalanx_3"
HAnimSegment648.name = "r_carpal_proximal_phalanx_3"

HAnimJoint647.children.append(HAnimSegment648)
HAnimJoint649 = x3d.HAnimJoint()
HAnimJoint649.DEF = "STD_Joint_r_carpal_proximal_interphalangeal_3"
HAnimJoint649.name = "r_carpal_proximal_interphalangeal_3"
HAnimJoint649.center = [-0.1950,0.7304,-0.0441]
HAnimSegment650 = x3d.HAnimSegment()
HAnimSegment650.DEF = "STD_Segment_r_carpal_middle_phalanx_3"
HAnimSegment650.name = "r_carpal_middle_phalanx_3"

HAnimJoint649.children.append(HAnimSegment650)
HAnimJoint651 = x3d.HAnimJoint()
HAnimJoint651.DEF = "STD_Joint_r_carpal_distal_interphalangeal_3"
HAnimJoint651.name = "r_carpal_distal_interphalangeal_3"
HAnimJoint651.center = [-0.1939,0.7042,-0.0432]
HAnimSegment652 = x3d.HAnimSegment()
HAnimSegment652.DEF = "STD_Segment_r_carpal_distal_phalanx_3"
HAnimSegment652.name = "r_carpal_distal_phalanx_3"
HAnimSite653 = x3d.HAnimSite()
HAnimSite653.DEF = "STD_Site_r_carpal_distal_phalanx_3_tip"
HAnimSite653.name = "r_carpal_distal_phalanx_3_tip"
HAnimSite653.scale = [0.0225,0.0225,0.0225]
TouchSensor654 = x3d.TouchSensor()
TouchSensor654.description = "HAnimSite r_carpal_distal_phalanx_3_tip"

HAnimSite653.children.append(TouchSensor654)
Shape655 = x3d.Shape()
Shape655.USE = "HAnimSiteShape"

HAnimSite653.children.append(Shape655)

HAnimSegment652.children.append(HAnimSite653)

HAnimJoint651.children.append(HAnimSegment652)

HAnimJoint649.children.append(HAnimJoint651)

HAnimJoint647.children.append(HAnimJoint649)

HAnimJoint642.children.append(HAnimJoint647)

HAnimJoint640.children.append(HAnimJoint642)

HAnimJoint605.children.append(HAnimJoint640)
HAnimJoint656 = x3d.HAnimJoint()
HAnimJoint656.DEF = "STD_Joint_r_midcarpal_4_5"
HAnimJoint656.name = "r_midcarpal_4_5"
HAnimJoint656.center = [0,0,0]
HAnimSegment657 = x3d.HAnimSegment()
HAnimSegment657.DEF = "STD_Segment_r_hamate"
HAnimSegment657.name = "r_hamate"

HAnimJoint656.children.append(HAnimSegment657)
HAnimJoint658 = x3d.HAnimJoint()
HAnimJoint658.DEF = "STD_Joint_r_carpometacarpal_4"
HAnimJoint658.name = "r_carpometacarpal_4"
HAnimJoint658.center = [-0.1951,0.8049,-0.0732]
HAnimSegment659 = x3d.HAnimSegment()
HAnimSegment659.DEF = "STD_Segment_r_metacarpal_4"
HAnimSegment659.name = "r_metacarpal_4"

HAnimJoint658.children.append(HAnimSegment659)
HAnimJoint660 = x3d.HAnimJoint()
HAnimJoint660.DEF = "STD_Joint_r_metacarpophalangeal_4"
HAnimJoint660.name = "r_metacarpophalangeal_4"
HAnimJoint660.center = [-0.1951,0.7845,-0.0732]
HAnimSegment661 = x3d.HAnimSegment()
HAnimSegment661.DEF = "STD_Segment_r_carpal_proximal_phalanx_4"
HAnimSegment661.name = "r_carpal_proximal_phalanx_4"

HAnimJoint660.children.append(HAnimSegment661)
HAnimJoint662 = x3d.HAnimJoint()
HAnimJoint662.DEF = "STD_Joint_r_carpal_proximal_interphalangeal_4"
HAnimJoint662.name = "r_carpal_proximal_interphalangeal_4"
HAnimJoint662.center = [-0.1920,0.7318,-0.0716]
HAnimSegment663 = x3d.HAnimSegment()
HAnimSegment663.DEF = "STD_Segment_r_carpal_middle_phalanx_4"
HAnimSegment663.name = "r_carpal_middle_phalanx_4"

HAnimJoint662.children.append(HAnimSegment663)
HAnimJoint664 = x3d.HAnimJoint()
HAnimJoint664.DEF = "STD_Joint_r_carpal_distal_interphalangeal_4"
HAnimJoint664.name = "r_carpal_distal_interphalangeal_4"
HAnimJoint664.center = [-0.1908,0.7077,-0.0706]
HAnimSegment665 = x3d.HAnimSegment()
HAnimSegment665.DEF = "STD_Segment_r_carpal_distal_phalanx_4"
HAnimSegment665.name = "r_carpal_distal_phalanx_4"
HAnimSite666 = x3d.HAnimSite()
HAnimSite666.DEF = "STD_Site_r_carpal_distal_phalanx_4_tip"
HAnimSite666.name = "r_carpal_distal_phalanx_4_tip"
HAnimSite666.scale = [0.0225,0.0225,0.0225]
TouchSensor667 = x3d.TouchSensor()
TouchSensor667.description = "HAnimSite r_carpal_distal_phalanx_4_tip"

HAnimSite666.children.append(TouchSensor667)
Shape668 = x3d.Shape()
Shape668.USE = "HAnimSiteShape"

HAnimSite666.children.append(Shape668)

HAnimSegment665.children.append(HAnimSite666)

HAnimJoint664.children.append(HAnimSegment665)

HAnimJoint662.children.append(HAnimJoint664)

HAnimJoint660.children.append(HAnimJoint662)

HAnimJoint658.children.append(HAnimJoint660)

HAnimJoint656.children.append(HAnimJoint658)
HAnimJoint669 = x3d.HAnimJoint()
HAnimJoint669.DEF = "STD_Joint_r_carpometacarpal_5"
HAnimJoint669.name = "r_carpometacarpal_5"
HAnimJoint669.center = [-0.1926,0.8096,-0.0975]
HAnimSegment670 = x3d.HAnimSegment()
HAnimSegment670.DEF = "STD_Segment_r_metacarpal_5"
HAnimSegment670.name = "r_metacarpal_5"
HAnimSite671 = x3d.HAnimSite()
HAnimSite671.DEF = "STD_Site_r_metacarpal_phalanx_5_pt"
HAnimSite671.name = "r_metacarpal_phalanx_5_pt"
HAnimSite671.scale = [0.0225,0.0225,0.0225]
HAnimSite671.translation = [-0.1929,0.7890,-0.1064]
TouchSensor672 = x3d.TouchSensor()
TouchSensor672.description = "HAnimSite r_metacarpal_phalanx_5_pt"

HAnimSite671.children.append(TouchSensor672)
Shape673 = x3d.Shape()
Shape673.USE = "HAnimSiteShape"

HAnimSite671.children.append(Shape673)

HAnimSegment670.children.append(HAnimSite671)

HAnimJoint669.children.append(HAnimSegment670)
HAnimJoint674 = x3d.HAnimJoint()
HAnimJoint674.DEF = "STD_Joint_r_metacarpophalangeal_5"
HAnimJoint674.name = "r_metacarpophalangeal_5"
HAnimJoint674.center = [-0.1926,0.7896,-0.0975]
HAnimSegment675 = x3d.HAnimSegment()
HAnimSegment675.DEF = "STD_Segment_r_carpal_proximal_phalanx_5"
HAnimSegment675.name = "r_carpal_proximal_phalanx_5"

HAnimJoint674.children.append(HAnimSegment675)
HAnimJoint676 = x3d.HAnimJoint()
HAnimJoint676.DEF = "STD_Joint_r_carpal_proximal_interphalangeal_5"
HAnimJoint676.name = "r_carpal_proximal_interphalangeal_5"
HAnimJoint676.center = [-0.1902,0.7483,-0.0963]
HAnimSegment677 = x3d.HAnimSegment()
HAnimSegment677.DEF = "STD_Segment_r_carpal_middle_phalanx_5"
HAnimSegment677.name = "r_carpal_middle_phalanx_5"

HAnimJoint676.children.append(HAnimSegment677)
HAnimJoint678 = x3d.HAnimJoint()
HAnimJoint678.DEF = "STD_Joint_r_carpal_distal_interphalangeal_5"
HAnimJoint678.name = "r_carpal_distal_interphalangeal_5"
HAnimJoint678.center = [-0.1908,0.7540,-0.0960]
HAnimSegment679 = x3d.HAnimSegment()
HAnimSegment679.DEF = "STD_Segment_r_carpal_distal_phalanx_5"
HAnimSegment679.name = "r_carpal_distal_phalanx_5"
HAnimSite680 = x3d.HAnimSite()
HAnimSite680.DEF = "STD_Site_r_carpal_distal_phalanx_5_tip"
HAnimSite680.name = "r_carpal_distal_phalanx_5_tip"
HAnimSite680.scale = [0.0225,0.0225,0.0225]
TouchSensor681 = x3d.TouchSensor()
TouchSensor681.description = "HAnimSite r_carpal_distal_phalanx_5_tip"

HAnimSite680.children.append(TouchSensor681)
Shape682 = x3d.Shape()
Shape682.USE = "HAnimSiteShape"

HAnimSite680.children.append(Shape682)

HAnimSegment679.children.append(HAnimSite680)

HAnimJoint678.children.append(HAnimSegment679)

HAnimJoint676.children.append(HAnimJoint678)

HAnimJoint674.children.append(HAnimJoint676)

HAnimJoint669.children.append(HAnimJoint674)

HAnimJoint656.children.append(HAnimJoint669)

HAnimJoint605.children.append(HAnimJoint656)

HAnimJoint591.children.append(HAnimJoint605)

HAnimJoint583.children.append(HAnimJoint591)

HAnimJoint581.children.append(HAnimJoint583)

HAnimJoint564.children.append(HAnimJoint581)

HAnimJoint353.children.append(HAnimJoint564)

HAnimJoint351.children.append(HAnimJoint353)

HAnimJoint349.children.append(HAnimJoint351)

HAnimJoint347.children.append(HAnimJoint349)

HAnimJoint342.children.append(HAnimJoint347)

HAnimJoint328.children.append(HAnimJoint342)

HAnimJoint326.children.append(HAnimJoint328)

HAnimJoint324.children.append(HAnimJoint326)

HAnimJoint316.children.append(HAnimJoint324)

HAnimJoint311.children.append(HAnimJoint316)

HAnimJoint309.children.append(HAnimJoint311)

HAnimJoint307.children.append(HAnimJoint309)

HAnimJoint305.children.append(HAnimJoint307)

HAnimJoint294.children.append(HAnimJoint305)

HAnimJoint292.children.append(HAnimJoint294)

HAnimJoint290.children.append(HAnimJoint292)

HAnimJoint279.children.append(HAnimJoint290)

HAnimJoint14.children.append(HAnimJoint279)

HAnimHumanoid13.joints.append(HAnimJoint14)
HAnimJoint683 = x3d.HAnimJoint()
HAnimJoint683.USE = "STD_Joint_humanoid_root"

HAnimHumanoid13.joints.append(HAnimJoint683)
HAnimSegment684 = x3d.HAnimSegment()
HAnimSegment684.USE = "STD_Segment_sacrum"

HAnimHumanoid13.segments.append(HAnimSegment684)
HAnimJoint685 = x3d.HAnimJoint()
HAnimJoint685.USE = "STD_Joint_sacroiliac"

HAnimHumanoid13.joints.append(HAnimJoint685)
HAnimSegment686 = x3d.HAnimSegment()
HAnimSegment686.USE = "STD_Segment_pelvis"

HAnimHumanoid13.segments.append(HAnimSegment686)
HAnimSite687 = x3d.HAnimSite()
HAnimSite687.USE = "STD_Site_buttocks_standing_wall_contact_point_pt"

HAnimHumanoid13.sites.append(HAnimSite687)
HAnimSite688 = x3d.HAnimSite()
HAnimSite688.USE = "STD_Site_r_psis_pt"

HAnimHumanoid13.sites.append(HAnimSite688)
HAnimSite689 = x3d.HAnimSite()
HAnimSite689.USE = "STD_Site_crotch_pt"

HAnimHumanoid13.sites.append(HAnimSite689)
HAnimSite690 = x3d.HAnimSite()
HAnimSite690.USE = "STD_Site_l_psis_pt"

HAnimHumanoid13.sites.append(HAnimSite690)
HAnimSite691 = x3d.HAnimSite()
HAnimSite691.USE = "STD_Site_r_iliocristale_pt"

HAnimHumanoid13.sites.append(HAnimSite691)
HAnimSite692 = x3d.HAnimSite()
HAnimSite692.USE = "STD_Site_r_asis_pt"

HAnimHumanoid13.sites.append(HAnimSite692)
HAnimSite693 = x3d.HAnimSite()
HAnimSite693.USE = "STD_Site_l_iliocristale_pt"

HAnimHumanoid13.sites.append(HAnimSite693)
HAnimSite694 = x3d.HAnimSite()
HAnimSite694.USE = "STD_Site_l_asis_pt"

HAnimHumanoid13.sites.append(HAnimSite694)
HAnimSite695 = x3d.HAnimSite()
HAnimSite695.USE = "STD_Site_l_trochanterion_pt"

HAnimHumanoid13.sites.append(HAnimSite695)
HAnimSite696 = x3d.HAnimSite()
HAnimSite696.USE = "STD_Site_r_trochanterion_pt"

HAnimHumanoid13.sites.append(HAnimSite696)
HAnimJoint697 = x3d.HAnimJoint()
HAnimJoint697.USE = "STD_Joint_l_hip"

HAnimHumanoid13.joints.append(HAnimJoint697)
HAnimSegment698 = x3d.HAnimSegment()
HAnimSegment698.USE = "STD_Segment_l_thigh"

HAnimHumanoid13.segments.append(HAnimSegment698)
HAnimSite699 = x3d.HAnimSite()
HAnimSite699.USE = "STD_Site_l_femoral_medial_epicondyles_pt"

HAnimHumanoid13.sites.append(HAnimSite699)
HAnimSite700 = x3d.HAnimSite()
HAnimSite700.USE = "STD_Site_l_knee_crease_pt"

HAnimHumanoid13.sites.append(HAnimSite700)
HAnimSite701 = x3d.HAnimSite()
HAnimSite701.USE = "STD_Site_l_femoral_lateral_epicondyles_pt"

HAnimHumanoid13.sites.append(HAnimSite701)
HAnimSite702 = x3d.HAnimSite()
HAnimSite702.USE = "STD_Site_l_suprapatella_pt"

HAnimHumanoid13.sites.append(HAnimSite702)
HAnimJoint703 = x3d.HAnimJoint()
HAnimJoint703.USE = "STD_Joint_l_knee"

HAnimHumanoid13.joints.append(HAnimJoint703)
HAnimSegment704 = x3d.HAnimSegment()
HAnimSegment704.USE = "STD_Segment_l_calf"

HAnimHumanoid13.segments.append(HAnimSegment704)
HAnimSite705 = x3d.HAnimSite()
HAnimSite705.USE = "STD_Site_l_lateral_malleolus_pt"

HAnimHumanoid13.sites.append(HAnimSite705)
HAnimSite706 = x3d.HAnimSite()
HAnimSite706.USE = "STD_Site_l_medial_malleolus_pt"

HAnimHumanoid13.sites.append(HAnimSite706)
HAnimSite707 = x3d.HAnimSite()
HAnimSite707.USE = "STD_Site_l_tibiale_pt"

HAnimHumanoid13.sites.append(HAnimSite707)
HAnimJoint708 = x3d.HAnimJoint()
HAnimJoint708.USE = "STD_Joint_l_talocrural"

HAnimHumanoid13.joints.append(HAnimJoint708)
HAnimSegment709 = x3d.HAnimSegment()
HAnimSegment709.USE = "STD_Segment_l_talus"

HAnimHumanoid13.segments.append(HAnimSegment709)
HAnimSite710 = x3d.HAnimSite()
HAnimSite710.USE = "STD_Site_l_sphyrion_pt"

HAnimHumanoid13.sites.append(HAnimSite710)
HAnimSite711 = x3d.HAnimSite()
HAnimSite711.USE = "STD_Site_l_calcaneus_posterior_pt"

HAnimHumanoid13.sites.append(HAnimSite711)
HAnimJoint712 = x3d.HAnimJoint()
HAnimJoint712.USE = "STD_Joint_l_talocalcaneonavicular"

HAnimHumanoid13.joints.append(HAnimJoint712)
HAnimSegment713 = x3d.HAnimSegment()
HAnimSegment713.USE = "STD_Segment_l_navicular"

HAnimHumanoid13.segments.append(HAnimSegment713)
HAnimJoint714 = x3d.HAnimJoint()
HAnimJoint714.USE = "STD_Joint_l_cuneonavicular_1"

HAnimHumanoid13.joints.append(HAnimJoint714)
HAnimSegment715 = x3d.HAnimSegment()
HAnimSegment715.USE = "STD_Segment_l_cuneiform_1"

HAnimHumanoid13.segments.append(HAnimSegment715)
HAnimJoint716 = x3d.HAnimJoint()
HAnimJoint716.USE = "STD_Joint_l_tarsometatarsal_1"

HAnimHumanoid13.joints.append(HAnimJoint716)
HAnimSegment717 = x3d.HAnimSegment()
HAnimSegment717.USE = "STD_Segment_l_metatarsal_1"

HAnimHumanoid13.segments.append(HAnimSegment717)
HAnimJoint718 = x3d.HAnimJoint()
HAnimJoint718.USE = "STD_Joint_l_metatarsophalangeal_1"

HAnimHumanoid13.joints.append(HAnimJoint718)
HAnimSegment719 = x3d.HAnimSegment()
HAnimSegment719.USE = "STD_Segment_l_tarsal_proximal_phalanx_1"

HAnimHumanoid13.segments.append(HAnimSegment719)
HAnimSite720 = x3d.HAnimSite()
HAnimSite720.USE = "STD_Site_l_metatarsal_phalanx_1_pt"

HAnimHumanoid13.sites.append(HAnimSite720)
HAnimJoint721 = x3d.HAnimJoint()
HAnimJoint721.USE = "STD_Joint_l_tarsal_interphalangeal_1"

HAnimHumanoid13.joints.append(HAnimJoint721)
HAnimSegment722 = x3d.HAnimSegment()
HAnimSegment722.USE = "STD_Segment_l_tarsal_distal_phalanx_1"

HAnimHumanoid13.segments.append(HAnimSegment722)
HAnimSite723 = x3d.HAnimSite()
HAnimSite723.USE = "STD_Site_l_tarsal_distal_phalanx_1_tip"

HAnimHumanoid13.sites.append(HAnimSite723)
HAnimJoint724 = x3d.HAnimJoint()
HAnimJoint724.USE = "STD_Joint_l_cuneonavicular_2"

HAnimHumanoid13.joints.append(HAnimJoint724)
HAnimSegment725 = x3d.HAnimSegment()
HAnimSegment725.USE = "STD_Segment_l_cuneiform_2"

HAnimHumanoid13.segments.append(HAnimSegment725)
HAnimJoint726 = x3d.HAnimJoint()
HAnimJoint726.USE = "STD_Joint_l_tarsometatarsal_2"

HAnimHumanoid13.joints.append(HAnimJoint726)
HAnimSegment727 = x3d.HAnimSegment()
HAnimSegment727.USE = "STD_Segment_l_metatarsal_2"

HAnimHumanoid13.segments.append(HAnimSegment727)
HAnimJoint728 = x3d.HAnimJoint()
HAnimJoint728.USE = "STD_Joint_l_metatarsophalangeal_2"

HAnimHumanoid13.joints.append(HAnimJoint728)
HAnimSegment729 = x3d.HAnimSegment()
HAnimSegment729.USE = "STD_Segment_l_tarsal_proximal_phalanx_2"

HAnimHumanoid13.segments.append(HAnimSegment729)
HAnimJoint730 = x3d.HAnimJoint()
HAnimJoint730.USE = "STD_Joint_l_tarsal_proximal_interphalangeal_2"

HAnimHumanoid13.joints.append(HAnimJoint730)
HAnimSegment731 = x3d.HAnimSegment()
HAnimSegment731.USE = "STD_Segment_l_tarsal_middle_phalanx_2"

HAnimHumanoid13.segments.append(HAnimSegment731)
HAnimJoint732 = x3d.HAnimJoint()
HAnimJoint732.USE = "STD_Joint_l_tarsal_distal_interphalangeal_2"

HAnimHumanoid13.joints.append(HAnimJoint732)
HAnimSegment733 = x3d.HAnimSegment()
HAnimSegment733.USE = "STD_Segment_l_tarsal_distal_phalanx_2"

HAnimHumanoid13.segments.append(HAnimSegment733)
HAnimSite734 = x3d.HAnimSite()
HAnimSite734.USE = "STD_Site_l_tarsal_distal_phalanx_2_tip"

HAnimHumanoid13.sites.append(HAnimSite734)
HAnimJoint735 = x3d.HAnimJoint()
HAnimJoint735.USE = "STD_Joint_l_cuneonavicular_3"

HAnimHumanoid13.joints.append(HAnimJoint735)
HAnimSegment736 = x3d.HAnimSegment()
HAnimSegment736.USE = "STD_Segment_l_cuneiform_3"

HAnimHumanoid13.segments.append(HAnimSegment736)
HAnimJoint737 = x3d.HAnimJoint()
HAnimJoint737.USE = "STD_Joint_l_tarsometatarsal_3 "

HAnimHumanoid13.joints.append(HAnimJoint737)
HAnimSegment738 = x3d.HAnimSegment()
HAnimSegment738.USE = "STD_Segment_l_metatarsal_3"

HAnimHumanoid13.segments.append(HAnimSegment738)
HAnimJoint739 = x3d.HAnimJoint()
HAnimJoint739.USE = "STD_Joint_l_metatarsophalangeal_3"

HAnimHumanoid13.joints.append(HAnimJoint739)
HAnimSegment740 = x3d.HAnimSegment()
HAnimSegment740.USE = "STD_Segment_l_tarsal_proximal_phalanx_3"

HAnimHumanoid13.segments.append(HAnimSegment740)
HAnimJoint741 = x3d.HAnimJoint()
HAnimJoint741.USE = "STD_Joint_l_tarsal_proximal_interphalangeal_3"

HAnimHumanoid13.joints.append(HAnimJoint741)
HAnimSegment742 = x3d.HAnimSegment()
HAnimSegment742.USE = "STD_Segment_l_tarsal_middle_phalanx_3"

HAnimHumanoid13.segments.append(HAnimSegment742)
HAnimJoint743 = x3d.HAnimJoint()
HAnimJoint743.USE = "STD_Joint_l_tarsal_distal_interphalangeal_3"

HAnimHumanoid13.joints.append(HAnimJoint743)
HAnimSegment744 = x3d.HAnimSegment()
HAnimSegment744.USE = "STD_Segment_l_tarsal_distal_phalanx_3"

HAnimHumanoid13.segments.append(HAnimSegment744)
HAnimSite745 = x3d.HAnimSite()
HAnimSite745.USE = "STD_Site_l_tarsal_distal_phalanx_3_tip"

HAnimHumanoid13.sites.append(HAnimSite745)
HAnimJoint746 = x3d.HAnimJoint()
HAnimJoint746.USE = "STD_Joint_l_calcaneocuboid"

HAnimHumanoid13.joints.append(HAnimJoint746)
HAnimSegment747 = x3d.HAnimSegment()
HAnimSegment747.USE = "STD_Segment_l_calcaneus"

HAnimHumanoid13.segments.append(HAnimSegment747)
HAnimJoint748 = x3d.HAnimJoint()
HAnimJoint748.USE = "STD_Joint_l_transversetarsal"

HAnimHumanoid13.joints.append(HAnimJoint748)
HAnimSegment749 = x3d.HAnimSegment()
HAnimSegment749.USE = "STD_Segment_l_cuboid"

HAnimHumanoid13.segments.append(HAnimSegment749)
HAnimJoint750 = x3d.HAnimJoint()
HAnimJoint750.USE = "STD_Joint_l_tarsometatarsal_4"

HAnimHumanoid13.joints.append(HAnimJoint750)
HAnimSegment751 = x3d.HAnimSegment()
HAnimSegment751.USE = "STD_Segment_l_metatarsal_4"

HAnimHumanoid13.segments.append(HAnimSegment751)
HAnimJoint752 = x3d.HAnimJoint()
HAnimJoint752.USE = "STD_Joint_l_metatarsophalangeal_4"

HAnimHumanoid13.joints.append(HAnimJoint752)
HAnimSegment753 = x3d.HAnimSegment()
HAnimSegment753.USE = "STD_Segment_l_tarsal_proximal_phalanx_4"

HAnimHumanoid13.segments.append(HAnimSegment753)
HAnimJoint754 = x3d.HAnimJoint()
HAnimJoint754.USE = "STD_Joint_l_tarsal_proximal_interphalangeal_4"

HAnimHumanoid13.joints.append(HAnimJoint754)
HAnimSegment755 = x3d.HAnimSegment()
HAnimSegment755.USE = "STD_Segment_l_tarsal_middle_phalanx_4"

HAnimHumanoid13.segments.append(HAnimSegment755)
HAnimJoint756 = x3d.HAnimJoint()
HAnimJoint756.USE = "STD_Joint_l_tarsal_distal_interphalangeal_4"

HAnimHumanoid13.joints.append(HAnimJoint756)
HAnimSegment757 = x3d.HAnimSegment()
HAnimSegment757.USE = "STD_Segment_l_tarsal_distal_phalanx_4"

HAnimHumanoid13.segments.append(HAnimSegment757)
HAnimSite758 = x3d.HAnimSite()
HAnimSite758.USE = "STD_Site_l_tarsal_distal_phalanx_4_tip"

HAnimHumanoid13.sites.append(HAnimSite758)
HAnimJoint759 = x3d.HAnimJoint()
HAnimJoint759.USE = "STD_Joint_l_tarsometatarsal_5"

HAnimHumanoid13.joints.append(HAnimJoint759)
HAnimSegment760 = x3d.HAnimSegment()
HAnimSegment760.USE = "STD_Segment_l_metatarsal_5"

HAnimHumanoid13.segments.append(HAnimSegment760)
HAnimJoint761 = x3d.HAnimJoint()
HAnimJoint761.USE = "STD_Joint_l_metatarsophalangeal_5"

HAnimHumanoid13.joints.append(HAnimJoint761)
HAnimSegment762 = x3d.HAnimSegment()
HAnimSegment762.USE = "STD_Segment_l_tarsal_proximal_phalanx_5"

HAnimHumanoid13.segments.append(HAnimSegment762)
HAnimSite763 = x3d.HAnimSite()
HAnimSite763.USE = "STD_Site_l_metatarsal_phalanx_5_pt"

HAnimHumanoid13.sites.append(HAnimSite763)
HAnimJoint764 = x3d.HAnimJoint()
HAnimJoint764.USE = "STD_Joint_l_tarsal_proximal_interphalangeal_5"

HAnimHumanoid13.joints.append(HAnimJoint764)
HAnimSegment765 = x3d.HAnimSegment()
HAnimSegment765.USE = "STD_Segment_l_tarsal_middle_phalanx_5"

HAnimHumanoid13.segments.append(HAnimSegment765)
HAnimJoint766 = x3d.HAnimJoint()
HAnimJoint766.USE = "STD_Joint_l_tarsal_distal_interphalangeal_5"

HAnimHumanoid13.joints.append(HAnimJoint766)
HAnimSegment767 = x3d.HAnimSegment()
HAnimSegment767.USE = "STD_Segment_l_tarsal_distal_phalanx_5"

HAnimHumanoid13.segments.append(HAnimSegment767)
HAnimSite768 = x3d.HAnimSite()
HAnimSite768.USE = "STD_Site_l_tarsal_distal_phalanx_5_tip"

HAnimHumanoid13.sites.append(HAnimSite768)
HAnimJoint769 = x3d.HAnimJoint()
HAnimJoint769.USE = "STD_Joint_r_hip"

HAnimHumanoid13.joints.append(HAnimJoint769)
HAnimSegment770 = x3d.HAnimSegment()
HAnimSegment770.USE = "STD_Segment_r_thigh"

HAnimHumanoid13.segments.append(HAnimSegment770)
HAnimSite771 = x3d.HAnimSite()
HAnimSite771.USE = "STD_Site_r_femoral_lateral_epicondyles_pt"

HAnimHumanoid13.sites.append(HAnimSite771)
HAnimSite772 = x3d.HAnimSite()
HAnimSite772.USE = "STD_Site_r_femoral_medial_epicondyles_pt"

HAnimHumanoid13.sites.append(HAnimSite772)
HAnimSite773 = x3d.HAnimSite()
HAnimSite773.USE = "STD_Site_r_knee_crease_pt"

HAnimHumanoid13.sites.append(HAnimSite773)
HAnimSite774 = x3d.HAnimSite()
HAnimSite774.USE = "STD_Site_r_suprapatella_pt"

HAnimHumanoid13.sites.append(HAnimSite774)
HAnimJoint775 = x3d.HAnimJoint()
HAnimJoint775.USE = "STD_Joint_r_knee"

HAnimHumanoid13.joints.append(HAnimJoint775)
HAnimSegment776 = x3d.HAnimSegment()
HAnimSegment776.USE = "STD_Segment_r_calf"

HAnimHumanoid13.segments.append(HAnimSegment776)
HAnimSite777 = x3d.HAnimSite()
HAnimSite777.USE = "STD_Site_r_lateral_malleolus_pt"

HAnimHumanoid13.sites.append(HAnimSite777)
HAnimSite778 = x3d.HAnimSite()
HAnimSite778.USE = "STD_Site_r_tibiale_pt"

HAnimHumanoid13.sites.append(HAnimSite778)
HAnimSite779 = x3d.HAnimSite()
HAnimSite779.USE = "STD_Site_r_medial_malleolus_pt"

HAnimHumanoid13.sites.append(HAnimSite779)
HAnimJoint780 = x3d.HAnimJoint()
HAnimJoint780.USE = "STD_Joint_r_talocrural"

HAnimHumanoid13.joints.append(HAnimJoint780)
HAnimSegment781 = x3d.HAnimSegment()
HAnimSegment781.USE = "STD_Segment_r_talus"

HAnimHumanoid13.segments.append(HAnimSegment781)
HAnimSite782 = x3d.HAnimSite()
HAnimSite782.USE = "STD_Site_r_sphyrion_pt"

HAnimHumanoid13.sites.append(HAnimSite782)
HAnimSite783 = x3d.HAnimSite()
HAnimSite783.USE = "STD_Site_r_calcaneus_posterior_pt"

HAnimHumanoid13.sites.append(HAnimSite783)
HAnimJoint784 = x3d.HAnimJoint()
HAnimJoint784.USE = "STD_Joint_r_talocalcaneonavicular"

HAnimHumanoid13.joints.append(HAnimJoint784)
HAnimSegment785 = x3d.HAnimSegment()
HAnimSegment785.USE = "STD_Segment_r_navicular"

HAnimHumanoid13.segments.append(HAnimSegment785)
HAnimJoint786 = x3d.HAnimJoint()
HAnimJoint786.USE = "STD_Joint_r_cuneonavicular_1"

HAnimHumanoid13.joints.append(HAnimJoint786)
HAnimSegment787 = x3d.HAnimSegment()
HAnimSegment787.USE = "STD_Segment_r_cuneiform_1"

HAnimHumanoid13.segments.append(HAnimSegment787)
HAnimJoint788 = x3d.HAnimJoint()
HAnimJoint788.USE = "STD_Joint_r_tarsometatarsal_1"

HAnimHumanoid13.joints.append(HAnimJoint788)
HAnimSegment789 = x3d.HAnimSegment()
HAnimSegment789.USE = "STD_Segment_r_metatarsal_1"

HAnimHumanoid13.segments.append(HAnimSegment789)
HAnimJoint790 = x3d.HAnimJoint()
HAnimJoint790.USE = "STD_Joint_r_metatarsophalangeal_1"

HAnimHumanoid13.joints.append(HAnimJoint790)
HAnimSegment791 = x3d.HAnimSegment()
HAnimSegment791.USE = "STD_Segment_r_tarsal_proximal_phalanx_1"

HAnimHumanoid13.segments.append(HAnimSegment791)
HAnimSite792 = x3d.HAnimSite()
HAnimSite792.USE = "STD_Site_r_metatarsal_phalanx_1_pt"

HAnimHumanoid13.sites.append(HAnimSite792)
HAnimJoint793 = x3d.HAnimJoint()
HAnimJoint793.USE = "STD_Joint_r_tarsal_interphalangeal_1"

HAnimHumanoid13.joints.append(HAnimJoint793)
HAnimSegment794 = x3d.HAnimSegment()
HAnimSegment794.USE = "STD_Segment_r_tarsal_distal_phalanx_1"

HAnimHumanoid13.segments.append(HAnimSegment794)
HAnimSite795 = x3d.HAnimSite()
HAnimSite795.USE = "STD_Site_r_tarsal_distal_phalanx_1_tip"

HAnimHumanoid13.sites.append(HAnimSite795)
HAnimJoint796 = x3d.HAnimJoint()
HAnimJoint796.USE = "STD_Joint_r_cuneonavicular_2"

HAnimHumanoid13.joints.append(HAnimJoint796)
HAnimSegment797 = x3d.HAnimSegment()
HAnimSegment797.USE = "STD_Segment_r_cuneiform_2"

HAnimHumanoid13.segments.append(HAnimSegment797)
HAnimJoint798 = x3d.HAnimJoint()
HAnimJoint798.USE = "STD_Joint_r_tarsometatarsal_2"

HAnimHumanoid13.joints.append(HAnimJoint798)
HAnimSegment799 = x3d.HAnimSegment()
HAnimSegment799.USE = "STD_Segment_r_metatarsal_2"

HAnimHumanoid13.segments.append(HAnimSegment799)
HAnimJoint800 = x3d.HAnimJoint()
HAnimJoint800.USE = "STD_Joint_r_metatarsophalangeal_2"

HAnimHumanoid13.joints.append(HAnimJoint800)
HAnimSegment801 = x3d.HAnimSegment()
HAnimSegment801.USE = "STD_Segment_r_tarsal_proximal_phalanx_2"

HAnimHumanoid13.segments.append(HAnimSegment801)
HAnimJoint802 = x3d.HAnimJoint()
HAnimJoint802.USE = "STD_Joint_r_tarsal_proximal_interphalangeal_2"

HAnimHumanoid13.joints.append(HAnimJoint802)
HAnimSegment803 = x3d.HAnimSegment()
HAnimSegment803.USE = "STD_Segment_r_tarsal_middle_phalanx_2"

HAnimHumanoid13.segments.append(HAnimSegment803)
HAnimJoint804 = x3d.HAnimJoint()
HAnimJoint804.USE = "STD_Joint_r_tarsal_distal_interphalangeal_2"

HAnimHumanoid13.joints.append(HAnimJoint804)
HAnimSegment805 = x3d.HAnimSegment()
HAnimSegment805.USE = "STD_Segment_r_tarsal_distal_phalanx_2"

HAnimHumanoid13.segments.append(HAnimSegment805)
HAnimSite806 = x3d.HAnimSite()
HAnimSite806.USE = "STD_Site_r_tarsal_distal_phalanx_2_tip"

HAnimHumanoid13.sites.append(HAnimSite806)
HAnimJoint807 = x3d.HAnimJoint()
HAnimJoint807.USE = "STD_Joint_r_cuneonavicular_3"

HAnimHumanoid13.joints.append(HAnimJoint807)
HAnimSegment808 = x3d.HAnimSegment()
HAnimSegment808.USE = "STD_Segment_r_cuneiform_3"

HAnimHumanoid13.segments.append(HAnimSegment808)
HAnimJoint809 = x3d.HAnimJoint()
HAnimJoint809.USE = "STD_Joint_r_tarsometatarsal_3 "

HAnimHumanoid13.joints.append(HAnimJoint809)
HAnimSegment810 = x3d.HAnimSegment()
HAnimSegment810.USE = "STD_Segment_r_metatarsal_3"

HAnimHumanoid13.segments.append(HAnimSegment810)
HAnimJoint811 = x3d.HAnimJoint()
HAnimJoint811.USE = "STD_Joint_r_metatarsophalangeal_3"

HAnimHumanoid13.joints.append(HAnimJoint811)
HAnimSegment812 = x3d.HAnimSegment()
HAnimSegment812.USE = "STD_Segment_r_tarsal_proximal_phalanx_3"

HAnimHumanoid13.segments.append(HAnimSegment812)
HAnimJoint813 = x3d.HAnimJoint()
HAnimJoint813.USE = "STD_Joint_r_tarsal_proximal_interphalangeal_3"

HAnimHumanoid13.joints.append(HAnimJoint813)
HAnimSegment814 = x3d.HAnimSegment()
HAnimSegment814.USE = "STD_Segment_r_tarsal_middle_phalanx_3"

HAnimHumanoid13.segments.append(HAnimSegment814)
HAnimJoint815 = x3d.HAnimJoint()
HAnimJoint815.USE = "STD_Joint_r_tarsal_distal_interphalangeal_3"

HAnimHumanoid13.joints.append(HAnimJoint815)
HAnimSegment816 = x3d.HAnimSegment()
HAnimSegment816.USE = "STD_Segment_r_tarsal_distal_phalanx_3"

HAnimHumanoid13.segments.append(HAnimSegment816)
HAnimSite817 = x3d.HAnimSite()
HAnimSite817.USE = "STD_Site_r_tarsal_distal_phalanx_3_tip"

HAnimHumanoid13.sites.append(HAnimSite817)
HAnimJoint818 = x3d.HAnimJoint()
HAnimJoint818.USE = "STD_Joint_r_calcaneocuboid"

HAnimHumanoid13.joints.append(HAnimJoint818)
HAnimSegment819 = x3d.HAnimSegment()
HAnimSegment819.USE = "STD_Segment_r_calcaneus"

HAnimHumanoid13.segments.append(HAnimSegment819)
HAnimJoint820 = x3d.HAnimJoint()
HAnimJoint820.USE = "STD_Joint_r_transversetarsal"

HAnimHumanoid13.joints.append(HAnimJoint820)
HAnimSegment821 = x3d.HAnimSegment()
HAnimSegment821.USE = "STD_Segment_r_cuboid"

HAnimHumanoid13.segments.append(HAnimSegment821)
HAnimJoint822 = x3d.HAnimJoint()
HAnimJoint822.USE = "STD_Joint_r_tarsometatarsal_4"

HAnimHumanoid13.joints.append(HAnimJoint822)
HAnimSegment823 = x3d.HAnimSegment()
HAnimSegment823.USE = "STD_Segment_r_metatarsal_4"

HAnimHumanoid13.segments.append(HAnimSegment823)
HAnimJoint824 = x3d.HAnimJoint()
HAnimJoint824.USE = "STD_Joint_r_metatarsophalangeal_4"

HAnimHumanoid13.joints.append(HAnimJoint824)
HAnimSegment825 = x3d.HAnimSegment()
HAnimSegment825.USE = "STD_Segment_r_tarsal_proximal_phalanx_4"

HAnimHumanoid13.segments.append(HAnimSegment825)
HAnimJoint826 = x3d.HAnimJoint()
HAnimJoint826.USE = "STD_Joint_r_tarsal_proximal_interphalangeal_4"

HAnimHumanoid13.joints.append(HAnimJoint826)
HAnimSegment827 = x3d.HAnimSegment()
HAnimSegment827.USE = "STD_Segment_r_tarsal_middle_phalanx_4"

HAnimHumanoid13.segments.append(HAnimSegment827)
HAnimJoint828 = x3d.HAnimJoint()
HAnimJoint828.USE = "STD_Joint_r_tarsal_distal_interphalangeal_4"

HAnimHumanoid13.joints.append(HAnimJoint828)
HAnimSegment829 = x3d.HAnimSegment()
HAnimSegment829.USE = "STD_Segment_r_tarsal_distal_phalanx_4"

HAnimHumanoid13.segments.append(HAnimSegment829)
HAnimSite830 = x3d.HAnimSite()
HAnimSite830.USE = "STD_Site_r_tarsal_distal_phalanx_4_tip"

HAnimHumanoid13.sites.append(HAnimSite830)
HAnimJoint831 = x3d.HAnimJoint()
HAnimJoint831.USE = "STD_Joint_r_tarsometatarsal_5"

HAnimHumanoid13.joints.append(HAnimJoint831)
HAnimSegment832 = x3d.HAnimSegment()
HAnimSegment832.USE = "STD_Segment_r_metatarsal_5"

HAnimHumanoid13.segments.append(HAnimSegment832)
HAnimJoint833 = x3d.HAnimJoint()
HAnimJoint833.USE = "STD_Joint_r_metatarsophalangeal_5"

HAnimHumanoid13.joints.append(HAnimJoint833)
HAnimSegment834 = x3d.HAnimSegment()
HAnimSegment834.USE = "STD_Segment_r_tarsal_proximal_phalanx_5"

HAnimHumanoid13.segments.append(HAnimSegment834)
HAnimSite835 = x3d.HAnimSite()
HAnimSite835.USE = "STD_Site_r_metatarsal_phalanx_5_pt"

HAnimHumanoid13.sites.append(HAnimSite835)
HAnimJoint836 = x3d.HAnimJoint()
HAnimJoint836.USE = "STD_Joint_r_tarsal_proximal_interphalangeal_5"

HAnimHumanoid13.joints.append(HAnimJoint836)
HAnimSegment837 = x3d.HAnimSegment()
HAnimSegment837.USE = "STD_Segment_r_tarsal_middle_phalanx_5"

HAnimHumanoid13.segments.append(HAnimSegment837)
HAnimJoint838 = x3d.HAnimJoint()
HAnimJoint838.USE = "STD_Joint_r_tarsal_distal_interphalangeal_5"

HAnimHumanoid13.joints.append(HAnimJoint838)
HAnimSegment839 = x3d.HAnimSegment()
HAnimSegment839.USE = "STD_Segment_r_tarsal_distal_phalanx_5"

HAnimHumanoid13.segments.append(HAnimSegment839)
HAnimSite840 = x3d.HAnimSite()
HAnimSite840.USE = "STD_Site_r_tarsal_distal_phalanx_5_tip"

HAnimHumanoid13.sites.append(HAnimSite840)
HAnimJoint841 = x3d.HAnimJoint()
HAnimJoint841.USE = "STD_Joint_vl5"

HAnimHumanoid13.joints.append(HAnimJoint841)
HAnimSegment842 = x3d.HAnimSegment()
HAnimSegment842.USE = "STD_Segment_l5"

HAnimHumanoid13.segments.append(HAnimSegment842)
HAnimSite843 = x3d.HAnimSite()
HAnimSite843.USE = "STD_Site_waist_preferred_posterior_pt"

HAnimHumanoid13.sites.append(HAnimSite843)
HAnimSite844 = x3d.HAnimSite()
HAnimSite844.USE = "STD_Site_waist_preferred_anterior_pt"

HAnimHumanoid13.sites.append(HAnimSite844)
HAnimSite845 = x3d.HAnimSite()
HAnimSite845.USE = "STD_Site_navel_pt"

HAnimHumanoid13.sites.append(HAnimSite845)
HAnimJoint846 = x3d.HAnimJoint()
HAnimJoint846.USE = "STD_Joint_vl4"

HAnimHumanoid13.joints.append(HAnimJoint846)
HAnimSegment847 = x3d.HAnimSegment()
HAnimSegment847.USE = "STD_Segment_l4"

HAnimHumanoid13.segments.append(HAnimSegment847)
HAnimJoint848 = x3d.HAnimJoint()
HAnimJoint848.USE = "STD_Joint_vl3"

HAnimHumanoid13.joints.append(HAnimJoint848)
HAnimSegment849 = x3d.HAnimSegment()
HAnimSegment849.USE = "STD_Segment_l3"

HAnimHumanoid13.segments.append(HAnimSegment849)
HAnimJoint850 = x3d.HAnimJoint()
HAnimJoint850.USE = "STD_Joint_vl2"

HAnimHumanoid13.joints.append(HAnimJoint850)
HAnimSegment851 = x3d.HAnimSegment()
HAnimSegment851.USE = "STD_Segment_l2"

HAnimHumanoid13.segments.append(HAnimSegment851)
HAnimSite852 = x3d.HAnimSite()
HAnimSite852.USE = "STD_Site_spine_2_middle_back_pt"

HAnimHumanoid13.sites.append(HAnimSite852)
HAnimSite853 = x3d.HAnimSite()
HAnimSite853.USE = "STD_Site_r_rib10_pt"

HAnimHumanoid13.sites.append(HAnimSite853)
HAnimSite854 = x3d.HAnimSite()
HAnimSite854.USE = "STD_Site_l_rib10_pt"

HAnimHumanoid13.sites.append(HAnimSite854)
HAnimJoint855 = x3d.HAnimJoint()
HAnimJoint855.USE = "STD_Joint_vl1"

HAnimHumanoid13.joints.append(HAnimJoint855)
HAnimSegment856 = x3d.HAnimSegment()
HAnimSegment856.USE = "STD_Segment_l1"

HAnimHumanoid13.segments.append(HAnimSegment856)
HAnimJoint857 = x3d.HAnimJoint()
HAnimJoint857.USE = "STD_Joint_vt12"

HAnimHumanoid13.joints.append(HAnimJoint857)
HAnimSegment858 = x3d.HAnimSegment()
HAnimSegment858.USE = "STD_Segment_t12"

HAnimHumanoid13.segments.append(HAnimSegment858)
HAnimJoint859 = x3d.HAnimJoint()
HAnimJoint859.USE = "STD_Joint_vt11"

HAnimHumanoid13.joints.append(HAnimJoint859)
HAnimSegment860 = x3d.HAnimSegment()
HAnimSegment860.USE = "STD_Segment_t11"

HAnimHumanoid13.segments.append(HAnimSegment860)
HAnimJoint861 = x3d.HAnimJoint()
HAnimJoint861.USE = "STD_Joint_vt10"

HAnimHumanoid13.joints.append(HAnimJoint861)
HAnimSegment862 = x3d.HAnimSegment()
HAnimSegment862.USE = "STD_Segment_t10"

HAnimHumanoid13.segments.append(HAnimSegment862)
HAnimSite863 = x3d.HAnimSite()
HAnimSite863.USE = "STD_Site_substernale_pt"

HAnimHumanoid13.sites.append(HAnimSite863)
HAnimJoint864 = x3d.HAnimJoint()
HAnimJoint864.USE = "STD_Joint_vt9"

HAnimHumanoid13.joints.append(HAnimJoint864)
HAnimSegment865 = x3d.HAnimSegment()
HAnimSegment865.USE = "STD_Segment_t9"

HAnimHumanoid13.segments.append(HAnimSegment865)
HAnimSite866 = x3d.HAnimSite()
HAnimSite866.USE = "STD_Site_l_thelion_pt"

HAnimHumanoid13.sites.append(HAnimSite866)
HAnimSite867 = x3d.HAnimSite()
HAnimSite867.USE = "STD_Site_r_thelion_pt"

HAnimHumanoid13.sites.append(HAnimSite867)
HAnimJoint868 = x3d.HAnimJoint()
HAnimJoint868.USE = "STD_Joint_vt8"

HAnimHumanoid13.joints.append(HAnimJoint868)
HAnimSegment869 = x3d.HAnimSegment()
HAnimSegment869.USE = "STD_Segment_t8"

HAnimHumanoid13.segments.append(HAnimSegment869)
HAnimJoint870 = x3d.HAnimJoint()
HAnimJoint870.USE = "STD_Joint_vt7"

HAnimHumanoid13.joints.append(HAnimJoint870)
HAnimSegment871 = x3d.HAnimSegment()
HAnimSegment871.USE = "STD_Segment_t7"

HAnimHumanoid13.segments.append(HAnimSegment871)
HAnimJoint872 = x3d.HAnimJoint()
HAnimJoint872.USE = "STD_Joint_vt6"

HAnimHumanoid13.joints.append(HAnimJoint872)
HAnimSegment873 = x3d.HAnimSegment()
HAnimSegment873.USE = "STD_Segment_t6"

HAnimHumanoid13.segments.append(HAnimSegment873)
HAnimSite874 = x3d.HAnimSite()
HAnimSite874.USE = "STD_Site_l_chest_midsagittal_plane_pt"

HAnimHumanoid13.sites.append(HAnimSite874)
HAnimSite875 = x3d.HAnimSite()
HAnimSite875.USE = "STD_Site_rear_center_midsagittal_plane_pt"

HAnimHumanoid13.sites.append(HAnimSite875)
HAnimSite876 = x3d.HAnimSite()
HAnimSite876.USE = "STD_Site_mesosternale_pt"

HAnimHumanoid13.sites.append(HAnimSite876)
HAnimSite877 = x3d.HAnimSite()
HAnimSite877.USE = "STD_Site_r_chest_midsagittal_plane_pt"

HAnimHumanoid13.sites.append(HAnimSite877)
HAnimJoint878 = x3d.HAnimJoint()
HAnimJoint878.USE = "STD_Joint_vt5"

HAnimHumanoid13.joints.append(HAnimJoint878)
HAnimSegment879 = x3d.HAnimSegment()
HAnimSegment879.USE = "STD_Segment_t5"

HAnimHumanoid13.segments.append(HAnimSegment879)
HAnimSite880 = x3d.HAnimSite()
HAnimSite880.USE = "STD_Site_spine_1_middle_back_pt"

HAnimHumanoid13.sites.append(HAnimSite880)
HAnimJoint881 = x3d.HAnimJoint()
HAnimJoint881.USE = "STD_Joint_vt4"

HAnimHumanoid13.joints.append(HAnimJoint881)
HAnimSegment882 = x3d.HAnimSegment()
HAnimSegment882.USE = "STD_Segment_t4"

HAnimHumanoid13.segments.append(HAnimSegment882)
HAnimJoint883 = x3d.HAnimJoint()
HAnimJoint883.USE = "STD_Joint_vt3"

HAnimHumanoid13.joints.append(HAnimJoint883)
HAnimSegment884 = x3d.HAnimSegment()
HAnimSegment884.USE = "STD_Segment_t3"

HAnimHumanoid13.segments.append(HAnimSegment884)
HAnimJoint885 = x3d.HAnimJoint()
HAnimJoint885.USE = "STD_Joint_vt2"

HAnimHumanoid13.joints.append(HAnimJoint885)
HAnimSegment886 = x3d.HAnimSegment()
HAnimSegment886.USE = "STD_Segment_t2"

HAnimHumanoid13.segments.append(HAnimSegment886)
HAnimJoint887 = x3d.HAnimJoint()
HAnimJoint887.USE = "STD_Joint_vt1"

HAnimHumanoid13.joints.append(HAnimJoint887)
HAnimSegment888 = x3d.HAnimSegment()
HAnimSegment888.USE = "STD_Segment_t1"

HAnimHumanoid13.segments.append(HAnimSegment888)
HAnimSite889 = x3d.HAnimSite()
HAnimSite889.USE = "STD_Site_suprasternale_pt"

HAnimHumanoid13.sites.append(HAnimSite889)
HAnimSite890 = x3d.HAnimSite()
HAnimSite890.USE = "STD_Site_cervicale_pt"

HAnimHumanoid13.sites.append(HAnimSite890)
HAnimJoint891 = x3d.HAnimJoint()
HAnimJoint891.USE = "STD_Joint_vc7"

HAnimHumanoid13.joints.append(HAnimJoint891)
HAnimSegment892 = x3d.HAnimSegment()
HAnimSegment892.USE = "STD_Segment_c7"

HAnimHumanoid13.segments.append(HAnimSegment892)
HAnimSite893 = x3d.HAnimSite()
HAnimSite893.USE = "STD_Site_r_neck_base_pt"

HAnimHumanoid13.sites.append(HAnimSite893)
HAnimSite894 = x3d.HAnimSite()
HAnimSite894.USE = "STD_Site_l_neck_base_pt"

HAnimHumanoid13.sites.append(HAnimSite894)
HAnimJoint895 = x3d.HAnimJoint()
HAnimJoint895.USE = "STD_Joint_vc6"

HAnimHumanoid13.joints.append(HAnimJoint895)
HAnimSegment896 = x3d.HAnimSegment()
HAnimSegment896.USE = "STD_Segment_c6"

HAnimHumanoid13.segments.append(HAnimSegment896)
HAnimJoint897 = x3d.HAnimJoint()
HAnimJoint897.USE = "STD_Joint_vc5"

HAnimHumanoid13.joints.append(HAnimJoint897)
HAnimSegment898 = x3d.HAnimSegment()
HAnimSegment898.USE = "STD_Segment_c5"

HAnimHumanoid13.segments.append(HAnimSegment898)
HAnimJoint899 = x3d.HAnimJoint()
HAnimJoint899.USE = "STD_Joint_vc4"

HAnimHumanoid13.joints.append(HAnimJoint899)
HAnimSegment900 = x3d.HAnimSegment()
HAnimSegment900.USE = "STD_Segment_c4"

HAnimHumanoid13.segments.append(HAnimSegment900)
HAnimJoint901 = x3d.HAnimJoint()
HAnimJoint901.USE = "STD_Joint_vc3"

HAnimHumanoid13.joints.append(HAnimJoint901)
HAnimSegment902 = x3d.HAnimSegment()
HAnimSegment902.USE = "STD_Segment_c3"

HAnimHumanoid13.segments.append(HAnimSegment902)
HAnimJoint903 = x3d.HAnimJoint()
HAnimJoint903.USE = "STD_Joint_vc2"

HAnimHumanoid13.joints.append(HAnimJoint903)
HAnimSegment904 = x3d.HAnimSegment()
HAnimSegment904.USE = "STD_Segment_c2"

HAnimHumanoid13.segments.append(HAnimSegment904)
HAnimSite905 = x3d.HAnimSite()
HAnimSite905.USE = "STD_Site_adams_apple_pt"

HAnimHumanoid13.sites.append(HAnimSite905)
HAnimJoint906 = x3d.HAnimJoint()
HAnimJoint906.USE = "STD_Joint_vc1"

HAnimHumanoid13.joints.append(HAnimJoint906)
HAnimSegment907 = x3d.HAnimSegment()
HAnimSegment907.USE = "STD_Segment_c1"

HAnimHumanoid13.segments.append(HAnimSegment907)
HAnimJoint908 = x3d.HAnimJoint()
HAnimJoint908.USE = "STD_Joint_skullbase"

HAnimHumanoid13.joints.append(HAnimJoint908)
HAnimSegment909 = x3d.HAnimSegment()
HAnimSegment909.USE = "STD_Segment_skull"

HAnimHumanoid13.segments.append(HAnimSegment909)
HAnimSite910 = x3d.HAnimSite()
HAnimSite910.USE = "STD_Site_l_ectocanthus_pt"

HAnimHumanoid13.sites.append(HAnimSite910)
HAnimSite911 = x3d.HAnimSite()
HAnimSite911.USE = "STD_Site_skull_vertex_pt"

HAnimHumanoid13.sites.append(HAnimSite911)
HAnimSite912 = x3d.HAnimSite()
HAnimSite912.USE = "STD_Site_r_ectocanthus_pt"

HAnimHumanoid13.sites.append(HAnimSite912)
HAnimSite913 = x3d.HAnimSite()
HAnimSite913.USE = "STD_Site_nuchale_pt"

HAnimHumanoid13.sites.append(HAnimSite913)
HAnimSite914 = x3d.HAnimSite()
HAnimSite914.USE = "STD_Site_opisthocranion_pt"

HAnimHumanoid13.sites.append(HAnimSite914)
HAnimSite915 = x3d.HAnimSite()
HAnimSite915.USE = "STD_Site_r_infraorbitale_pt"

HAnimHumanoid13.sites.append(HAnimSite915)
HAnimSite916 = x3d.HAnimSite()
HAnimSite916.USE = "STD_Site_r_tragion_pt"

HAnimHumanoid13.sites.append(HAnimSite916)
HAnimSite917 = x3d.HAnimSite()
HAnimSite917.USE = "STD_Site_l_tragion_pt"

HAnimHumanoid13.sites.append(HAnimSite917)
HAnimSite918 = x3d.HAnimSite()
HAnimSite918.USE = "STD_Site_sellion_pt"

HAnimHumanoid13.sites.append(HAnimSite918)
HAnimSite919 = x3d.HAnimSite()
HAnimSite919.USE = "STD_Site_l_infraorbitale_pt"

HAnimHumanoid13.sites.append(HAnimSite919)
HAnimSite920 = x3d.HAnimSite()
HAnimSite920.USE = "STD_Site_glabella_pt"

HAnimHumanoid13.sites.append(HAnimSite920)
HAnimJoint921 = x3d.HAnimJoint()
HAnimJoint921.USE = "STD_Joint_l_eyelid_joint"

HAnimHumanoid13.joints.append(HAnimJoint921)
HAnimSegment922 = x3d.HAnimSegment()
HAnimSegment922.USE = "STD_Segment_l_eyelid"

HAnimHumanoid13.segments.append(HAnimSegment922)
HAnimJoint923 = x3d.HAnimJoint()
HAnimJoint923.USE = "STD_Joint_r_eyelid_joint"

HAnimHumanoid13.joints.append(HAnimJoint923)
HAnimSegment924 = x3d.HAnimSegment()
HAnimSegment924.USE = "STD_Segment_r_eyelid"

HAnimHumanoid13.segments.append(HAnimSegment924)
HAnimJoint925 = x3d.HAnimJoint()
HAnimJoint925.USE = "STD_Joint_l_eyeball_joint"

HAnimHumanoid13.joints.append(HAnimJoint925)
HAnimSegment926 = x3d.HAnimSegment()
HAnimSegment926.USE = "STD_Segment_l_eyeball"

HAnimHumanoid13.segments.append(HAnimSegment926)
HAnimJoint927 = x3d.HAnimJoint()
HAnimJoint927.USE = "STD_Joint_r_eyeball_joint"

HAnimHumanoid13.joints.append(HAnimJoint927)
HAnimSegment928 = x3d.HAnimSegment()
HAnimSegment928.USE = "STD_Segment_r_eyeball"

HAnimHumanoid13.segments.append(HAnimSegment928)
HAnimJoint929 = x3d.HAnimJoint()
HAnimJoint929.USE = "STD_Joint_l_eyebrow_joint"

HAnimHumanoid13.joints.append(HAnimJoint929)
HAnimSegment930 = x3d.HAnimSegment()
HAnimSegment930.USE = "STD_Segment_l_eyebrow"

HAnimHumanoid13.segments.append(HAnimSegment930)
HAnimJoint931 = x3d.HAnimJoint()
HAnimJoint931.USE = "STD_Joint_r_eyebrow_joint"

HAnimHumanoid13.joints.append(HAnimJoint931)
HAnimSegment932 = x3d.HAnimSegment()
HAnimSegment932.USE = "STD_Segment_r_eyebrow"

HAnimHumanoid13.segments.append(HAnimSegment932)
HAnimJoint933 = x3d.HAnimJoint()
HAnimJoint933.USE = "STD_Joint_temporomandibular"

HAnimHumanoid13.joints.append(HAnimJoint933)
HAnimSegment934 = x3d.HAnimSegment()
HAnimSegment934.USE = "STD_Segment_jaw"

HAnimHumanoid13.segments.append(HAnimSegment934)
HAnimSite935 = x3d.HAnimSite()
HAnimSite935.USE = "STD_Site_menton_pt"

HAnimHumanoid13.sites.append(HAnimSite935)
HAnimSite936 = x3d.HAnimSite()
HAnimSite936.USE = "STD_Site_l_gonion_pt"

HAnimHumanoid13.sites.append(HAnimSite936)
HAnimSite937 = x3d.HAnimSite()
HAnimSite937.USE = "STD_Site_supramenton_pt"

HAnimHumanoid13.sites.append(HAnimSite937)
HAnimSite938 = x3d.HAnimSite()
HAnimSite938.USE = "STD_Site_r_gonion_pt"

HAnimHumanoid13.sites.append(HAnimSite938)
HAnimJoint939 = x3d.HAnimJoint()
HAnimJoint939.USE = "STD_Joint_l_sternoclavicular"

HAnimHumanoid13.joints.append(HAnimJoint939)
HAnimSegment940 = x3d.HAnimSegment()
HAnimSegment940.USE = "STD_Segment_l_clavicle"

HAnimHumanoid13.segments.append(HAnimSegment940)
HAnimSite941 = x3d.HAnimSite()
HAnimSite941.USE = "STD_Site_l_axilla_posterior_folds_pt"

HAnimHumanoid13.sites.append(HAnimSite941)
HAnimSite942 = x3d.HAnimSite()
HAnimSite942.USE = "STD_Site_l_acromion_pt"

HAnimHumanoid13.sites.append(HAnimSite942)
HAnimSite943 = x3d.HAnimSite()
HAnimSite943.USE = "STD_Site_l_axilla_distal_pt"

HAnimHumanoid13.sites.append(HAnimSite943)
HAnimSite944 = x3d.HAnimSite()
HAnimSite944.USE = "STD_Site_l_axilla_proximal_pt"

HAnimHumanoid13.sites.append(HAnimSite944)
HAnimSite945 = x3d.HAnimSite()
HAnimSite945.USE = "STD_Site_l_clavicale_pt"

HAnimHumanoid13.sites.append(HAnimSite945)
HAnimJoint946 = x3d.HAnimJoint()
HAnimJoint946.USE = "STD_Joint_l_acromioclavicular"

HAnimHumanoid13.joints.append(HAnimJoint946)
HAnimSegment947 = x3d.HAnimSegment()
HAnimSegment947.USE = "STD_Segment_l_scapula"

HAnimHumanoid13.segments.append(HAnimSegment947)
HAnimJoint948 = x3d.HAnimJoint()
HAnimJoint948.USE = "STD_Joint_l_shoulder"

HAnimHumanoid13.joints.append(HAnimJoint948)
HAnimSegment949 = x3d.HAnimSegment()
HAnimSegment949.USE = "STD_Segment_l_upperarm"

HAnimHumanoid13.segments.append(HAnimSegment949)
HAnimSite950 = x3d.HAnimSite()
HAnimSite950.USE = "STD_Site_l_humeral_lateral_epicondyles_pt"

HAnimHumanoid13.sites.append(HAnimSite950)
HAnimSite951 = x3d.HAnimSite()
HAnimSite951.USE = "STD_Site_l_bideltoid_pt"

HAnimHumanoid13.sites.append(HAnimSite951)
HAnimJoint952 = x3d.HAnimJoint()
HAnimJoint952.USE = "STD_Joint_l_elbow"

HAnimHumanoid13.joints.append(HAnimJoint952)
HAnimSegment953 = x3d.HAnimSegment()
HAnimSegment953.USE = "STD_Segment_l_forearm"

HAnimHumanoid13.segments.append(HAnimSegment953)
HAnimSite954 = x3d.HAnimSite()
HAnimSite954.USE = "STD_Site_l_olecranon_pt"

HAnimHumanoid13.sites.append(HAnimSite954)
HAnimSite955 = x3d.HAnimSite()
HAnimSite955.USE = "STD_Site_l_radiale_pt"

HAnimHumanoid13.sites.append(HAnimSite955)
HAnimSite956 = x3d.HAnimSite()
HAnimSite956.USE = "STD_Site_l_humeral_medial_epicondyles_pt"

HAnimHumanoid13.sites.append(HAnimSite956)
HAnimSite957 = x3d.HAnimSite()
HAnimSite957.USE = "STD_Site_l_radial_styloid_pt"

HAnimHumanoid13.sites.append(HAnimSite957)
HAnimJoint958 = x3d.HAnimJoint()
HAnimJoint958.USE = "STD_Joint_l_radiocarpal"

HAnimHumanoid13.joints.append(HAnimJoint958)
HAnimSegment959 = x3d.HAnimSegment()
HAnimSegment959.USE = "STD_Segment_l_carpal"

HAnimHumanoid13.segments.append(HAnimSegment959)
HAnimSite960 = x3d.HAnimSite()
HAnimSite960.USE = "STD_Site_l_ulnar_styloid_pt"

HAnimHumanoid13.sites.append(HAnimSite960)
HAnimJoint961 = x3d.HAnimJoint()
HAnimJoint961.USE = "STD_Joint_l_midcarpal_1"

HAnimHumanoid13.joints.append(HAnimJoint961)
HAnimSegment962 = x3d.HAnimSegment()
HAnimSegment962.USE = "STD_Segment_l_trapezium"

HAnimHumanoid13.segments.append(HAnimSegment962)
HAnimJoint963 = x3d.HAnimJoint()
HAnimJoint963.USE = "STD_Joint_l_carpometacarpal_1"

HAnimHumanoid13.joints.append(HAnimJoint963)
HAnimSegment964 = x3d.HAnimSegment()
HAnimSegment964.USE = "STD_Segment_l_metacarpal_1"

HAnimHumanoid13.segments.append(HAnimSegment964)
HAnimJoint965 = x3d.HAnimJoint()
HAnimJoint965.USE = "STD_Joint_l_metacarpophalangeal_1"

HAnimHumanoid13.joints.append(HAnimJoint965)
HAnimSegment966 = x3d.HAnimSegment()
HAnimSegment966.USE = "STD_Segment_l_carpal_proximal_phalanx_1"

HAnimHumanoid13.segments.append(HAnimSegment966)
HAnimJoint967 = x3d.HAnimJoint()
HAnimJoint967.USE = "STD_Joint_l_carpal_interphalangeal_1"

HAnimHumanoid13.joints.append(HAnimJoint967)
HAnimSegment968 = x3d.HAnimSegment()
HAnimSegment968.USE = "STD_Segment_l_carpal_distal_phalanx_1"

HAnimHumanoid13.segments.append(HAnimSegment968)
HAnimSite969 = x3d.HAnimSite()
HAnimSite969.USE = "STD_Site_l_carpal_distal_phalanx_1_tip"

HAnimHumanoid13.sites.append(HAnimSite969)
HAnimJoint970 = x3d.HAnimJoint()
HAnimJoint970.USE = "STD_Joint_l_midcarpal_2"

HAnimHumanoid13.joints.append(HAnimJoint970)
HAnimSegment971 = x3d.HAnimSegment()
HAnimSegment971.USE = "STD_Segment_l_trapezoid"

HAnimHumanoid13.segments.append(HAnimSegment971)
HAnimJoint972 = x3d.HAnimJoint()
HAnimJoint972.USE = "STD_Joint_l_carpometacarpal_2"

HAnimHumanoid13.joints.append(HAnimJoint972)
HAnimSegment973 = x3d.HAnimSegment()
HAnimSegment973.USE = "STD_Segment_l_metacarpal_2"

HAnimHumanoid13.segments.append(HAnimSegment973)
HAnimSite974 = x3d.HAnimSite()
HAnimSite974.USE = "STD_Site_l_metacarpal_phalanx_2_pt"

HAnimHumanoid13.sites.append(HAnimSite974)
HAnimJoint975 = x3d.HAnimJoint()
HAnimJoint975.USE = "STD_Joint_l_metacarpophalangeal_2"

HAnimHumanoid13.joints.append(HAnimJoint975)
HAnimSegment976 = x3d.HAnimSegment()
HAnimSegment976.USE = "STD_Segment_l_carpal_proximal_phalanx_2 "

HAnimHumanoid13.segments.append(HAnimSegment976)
HAnimJoint977 = x3d.HAnimJoint()
HAnimJoint977.USE = "STD_Joint_l_carpal_proximal_interphalangeal_2"

HAnimHumanoid13.joints.append(HAnimJoint977)
HAnimSegment978 = x3d.HAnimSegment()
HAnimSegment978.USE = "STD_Segment_l_carpal_middle_phalanx_2"

HAnimHumanoid13.segments.append(HAnimSegment978)
HAnimJoint979 = x3d.HAnimJoint()
HAnimJoint979.USE = "STD_Joint_l_carpal_distal_interphalangeal_2"

HAnimHumanoid13.joints.append(HAnimJoint979)
HAnimSegment980 = x3d.HAnimSegment()
HAnimSegment980.USE = "STD_Segment_l_carpal_distal_phalanx_2"

HAnimHumanoid13.segments.append(HAnimSegment980)
HAnimSite981 = x3d.HAnimSite()
HAnimSite981.USE = "STD_Site_l_carpal_distal_phalanx_2_tip"

HAnimHumanoid13.sites.append(HAnimSite981)
HAnimSite982 = x3d.HAnimSite()
HAnimSite982.USE = "STD_Site_l_dactylion_pt"

HAnimHumanoid13.sites.append(HAnimSite982)
HAnimJoint983 = x3d.HAnimJoint()
HAnimJoint983.USE = "STD_Joint_l_midcarpal_3"

HAnimHumanoid13.joints.append(HAnimJoint983)
HAnimSegment984 = x3d.HAnimSegment()
HAnimSegment984.USE = "STD_Segment_l_capitate"

HAnimHumanoid13.segments.append(HAnimSegment984)
HAnimJoint985 = x3d.HAnimJoint()
HAnimJoint985.USE = "STD_Joint_l_carpometacarpal_3"

HAnimHumanoid13.joints.append(HAnimJoint985)
HAnimSegment986 = x3d.HAnimSegment()
HAnimSegment986.USE = "STD_Segment_l_metacarpal_3"

HAnimHumanoid13.segments.append(HAnimSegment986)
HAnimSite987 = x3d.HAnimSite()
HAnimSite987.USE = "STD_Site_l_metacarpal_phalanx_3_pt"

HAnimHumanoid13.sites.append(HAnimSite987)
HAnimJoint988 = x3d.HAnimJoint()
HAnimJoint988.USE = "STD_Joint_l_metacarpophalangeal_3"

HAnimHumanoid13.joints.append(HAnimJoint988)
HAnimSegment989 = x3d.HAnimSegment()
HAnimSegment989.USE = "STD_Segment_l_carpal_proximal_phalanx_3"

HAnimHumanoid13.segments.append(HAnimSegment989)
HAnimJoint990 = x3d.HAnimJoint()
HAnimJoint990.USE = "STD_Joint_l_carpal_proximal_interphalangeal_3"

HAnimHumanoid13.joints.append(HAnimJoint990)
HAnimSegment991 = x3d.HAnimSegment()
HAnimSegment991.USE = "STD_Segment_l_carpal_middle_phalanx_3"

HAnimHumanoid13.segments.append(HAnimSegment991)
HAnimJoint992 = x3d.HAnimJoint()
HAnimJoint992.USE = "STD_Joint_l_carpal_distal_interphalangeal_3"

HAnimHumanoid13.joints.append(HAnimJoint992)
HAnimSegment993 = x3d.HAnimSegment()
HAnimSegment993.USE = "STD_Segment_l_carpal_distal_phalanx_3"

HAnimHumanoid13.segments.append(HAnimSegment993)
HAnimSite994 = x3d.HAnimSite()
HAnimSite994.USE = "STD_Site_l_carpal_distal_phalanx_3_tip"

HAnimHumanoid13.sites.append(HAnimSite994)
HAnimJoint995 = x3d.HAnimJoint()
HAnimJoint995.USE = "STD_Joint_l_midcarpal_4_5"

HAnimHumanoid13.joints.append(HAnimJoint995)
HAnimSegment996 = x3d.HAnimSegment()
HAnimSegment996.USE = "STD_Segment_l_hamate"

HAnimHumanoid13.segments.append(HAnimSegment996)
HAnimJoint997 = x3d.HAnimJoint()
HAnimJoint997.USE = "STD_Joint_l_carpometacarpal_4"

HAnimHumanoid13.joints.append(HAnimJoint997)
HAnimSegment998 = x3d.HAnimSegment()
HAnimSegment998.USE = "STD_Segment_l_metacarpal_4"

HAnimHumanoid13.segments.append(HAnimSegment998)
HAnimJoint999 = x3d.HAnimJoint()
HAnimJoint999.USE = "STD_Joint_l_metacarpophalangeal_4"

HAnimHumanoid13.joints.append(HAnimJoint999)
HAnimSegment1000 = x3d.HAnimSegment()
HAnimSegment1000.USE = "STD_Segment_l_carpal_proximal_phalanx_4"

HAnimHumanoid13.segments.append(HAnimSegment1000)
HAnimJoint1001 = x3d.HAnimJoint()
HAnimJoint1001.USE = "STD_Joint_l_carpal_proximal_interphalangeal_4"

HAnimHumanoid13.joints.append(HAnimJoint1001)
HAnimSegment1002 = x3d.HAnimSegment()
HAnimSegment1002.USE = "STD_Segment_l_carpal_middle_phalanx_4"

HAnimHumanoid13.segments.append(HAnimSegment1002)
HAnimJoint1003 = x3d.HAnimJoint()
HAnimJoint1003.USE = "STD_Joint_l_carpal_distal_interphalangeal_4"

HAnimHumanoid13.joints.append(HAnimJoint1003)
HAnimSegment1004 = x3d.HAnimSegment()
HAnimSegment1004.USE = "STD_Segment_l_carpal_distal_phalanx_4"

HAnimHumanoid13.segments.append(HAnimSegment1004)
HAnimSite1005 = x3d.HAnimSite()
HAnimSite1005.USE = "STD_Site_l_carpal_distal_phalanx_4_tip"

HAnimHumanoid13.sites.append(HAnimSite1005)
HAnimJoint1006 = x3d.HAnimJoint()
HAnimJoint1006.USE = "STD_Joint_l_carpometacarpal_5"

HAnimHumanoid13.joints.append(HAnimJoint1006)
HAnimSegment1007 = x3d.HAnimSegment()
HAnimSegment1007.USE = "STD_Segment_l_metacarpal_5"

HAnimHumanoid13.segments.append(HAnimSegment1007)
HAnimSite1008 = x3d.HAnimSite()
HAnimSite1008.USE = "STD_Site_l_metacarpal_phalanx_5_pt"

HAnimHumanoid13.sites.append(HAnimSite1008)
HAnimJoint1009 = x3d.HAnimJoint()
HAnimJoint1009.USE = "STD_Joint_l_metacarpophalangeal_5"

HAnimHumanoid13.joints.append(HAnimJoint1009)
HAnimSegment1010 = x3d.HAnimSegment()
HAnimSegment1010.USE = "STD_Segment_l_carpal_proximal_phalanx_5"

HAnimHumanoid13.segments.append(HAnimSegment1010)
HAnimJoint1011 = x3d.HAnimJoint()
HAnimJoint1011.USE = "STD_Joint_l_carpal_proximal_interphalangeal_5"

HAnimHumanoid13.joints.append(HAnimJoint1011)
HAnimSegment1012 = x3d.HAnimSegment()
HAnimSegment1012.USE = "STD_Segment_l_carpal_middle_phalanx_5"

HAnimHumanoid13.segments.append(HAnimSegment1012)
HAnimJoint1013 = x3d.HAnimJoint()
HAnimJoint1013.USE = "STD_Joint_l_carpal_distal_interphalangeal_5"

HAnimHumanoid13.joints.append(HAnimJoint1013)
HAnimSegment1014 = x3d.HAnimSegment()
HAnimSegment1014.USE = "STD_Segment_l_carpal_distal_phalanx_5"

HAnimHumanoid13.segments.append(HAnimSegment1014)
HAnimSite1015 = x3d.HAnimSite()
HAnimSite1015.USE = "STD_Site_l_carpal_distal_phalanx_5_tip"

HAnimHumanoid13.sites.append(HAnimSite1015)
HAnimJoint1016 = x3d.HAnimJoint()
HAnimJoint1016.USE = "STD_Joint_r_sternoclavicular"

HAnimHumanoid13.joints.append(HAnimJoint1016)
HAnimSegment1017 = x3d.HAnimSegment()
HAnimSegment1017.USE = "STD_Segment_r_clavicle"

HAnimHumanoid13.segments.append(HAnimSegment1017)
HAnimSite1018 = x3d.HAnimSite()
HAnimSite1018.USE = "STD_Site_r_axilla_posterior_folds_pt"

HAnimHumanoid13.sites.append(HAnimSite1018)
HAnimSite1019 = x3d.HAnimSite()
HAnimSite1019.USE = "STD_Site_r_axilla_distal_pt"

HAnimHumanoid13.sites.append(HAnimSite1019)
HAnimSite1020 = x3d.HAnimSite()
HAnimSite1020.USE = "STD_Site_r_acromion_pt"

HAnimHumanoid13.sites.append(HAnimSite1020)
HAnimSite1021 = x3d.HAnimSite()
HAnimSite1021.USE = "STD_Site_r_clavicale_pt"

HAnimHumanoid13.sites.append(HAnimSite1021)
HAnimSite1022 = x3d.HAnimSite()
HAnimSite1022.USE = "STD_Site_r_axilla_proximal_pt"

HAnimHumanoid13.sites.append(HAnimSite1022)
HAnimJoint1023 = x3d.HAnimJoint()
HAnimJoint1023.USE = "STD_Joint_r_acromioclavicular"

HAnimHumanoid13.joints.append(HAnimJoint1023)
HAnimSegment1024 = x3d.HAnimSegment()
HAnimSegment1024.USE = "STD_Segment_r_scapula"

HAnimHumanoid13.segments.append(HAnimSegment1024)
HAnimJoint1025 = x3d.HAnimJoint()
HAnimJoint1025.USE = "STD_Joint_r_shoulder"

HAnimHumanoid13.joints.append(HAnimJoint1025)
HAnimSegment1026 = x3d.HAnimSegment()
HAnimSegment1026.USE = "STD_Segment_r_upperarm"

HAnimHumanoid13.segments.append(HAnimSegment1026)
HAnimSite1027 = x3d.HAnimSite()
HAnimSite1027.USE = "STD_Site_r_humeral_lateral_epicondyles_pt"

HAnimHumanoid13.sites.append(HAnimSite1027)
HAnimSite1028 = x3d.HAnimSite()
HAnimSite1028.USE = "STD_Site_r_bideltoid_pt"

HAnimHumanoid13.sites.append(HAnimSite1028)
HAnimJoint1029 = x3d.HAnimJoint()
HAnimJoint1029.USE = "STD_Joint_r_elbow"

HAnimHumanoid13.joints.append(HAnimJoint1029)
HAnimSegment1030 = x3d.HAnimSegment()
HAnimSegment1030.USE = "STD_Segment_r_forearm"

HAnimHumanoid13.segments.append(HAnimSegment1030)
HAnimSite1031 = x3d.HAnimSite()
HAnimSite1031.USE = "STD_Site_r_radiale_pt"

HAnimHumanoid13.sites.append(HAnimSite1031)
HAnimSite1032 = x3d.HAnimSite()
HAnimSite1032.USE = "STD_Site_r_humeral_medial_epicondyles_pt"

HAnimHumanoid13.sites.append(HAnimSite1032)
HAnimSite1033 = x3d.HAnimSite()
HAnimSite1033.USE = "STD_Site_r_olecranon_pt"

HAnimHumanoid13.sites.append(HAnimSite1033)
HAnimSite1034 = x3d.HAnimSite()
HAnimSite1034.USE = "STD_Site_r_radial_styloid_pt"

HAnimHumanoid13.sites.append(HAnimSite1034)
HAnimJoint1035 = x3d.HAnimJoint()
HAnimJoint1035.USE = "STD_Joint_r_radiocarpal"

HAnimHumanoid13.joints.append(HAnimJoint1035)
HAnimSegment1036 = x3d.HAnimSegment()
HAnimSegment1036.USE = "STD_Segment_r_carpal"

HAnimHumanoid13.segments.append(HAnimSegment1036)
HAnimSite1037 = x3d.HAnimSite()
HAnimSite1037.USE = "STD_Site_r_ulnar_styloid_pt"

HAnimHumanoid13.sites.append(HAnimSite1037)
HAnimJoint1038 = x3d.HAnimJoint()
HAnimJoint1038.USE = "STD_Joint_r_midcarpal_1"

HAnimHumanoid13.joints.append(HAnimJoint1038)
HAnimSegment1039 = x3d.HAnimSegment()
HAnimSegment1039.USE = "STD_Segment_r_trapezium"

HAnimHumanoid13.segments.append(HAnimSegment1039)
HAnimJoint1040 = x3d.HAnimJoint()
HAnimJoint1040.USE = "STD_Joint_r_carpometacarpal_1"

HAnimHumanoid13.joints.append(HAnimJoint1040)
HAnimSegment1041 = x3d.HAnimSegment()
HAnimSegment1041.USE = "STD_Segment_r_metacarpal_1"

HAnimHumanoid13.segments.append(HAnimSegment1041)
HAnimJoint1042 = x3d.HAnimJoint()
HAnimJoint1042.USE = "STD_Joint_r_metacarpophalangeal_1"

HAnimHumanoid13.joints.append(HAnimJoint1042)
HAnimSegment1043 = x3d.HAnimSegment()
HAnimSegment1043.USE = "STD_Segment_r_carpal_proximal_phalanx_1"

HAnimHumanoid13.segments.append(HAnimSegment1043)
HAnimJoint1044 = x3d.HAnimJoint()
HAnimJoint1044.USE = "STD_Joint_r_carpal_interphalangeal_1"

HAnimHumanoid13.joints.append(HAnimJoint1044)
HAnimSegment1045 = x3d.HAnimSegment()
HAnimSegment1045.USE = "STD_Segment_r_carpal_distal_phalanx_1"

HAnimHumanoid13.segments.append(HAnimSegment1045)
HAnimSite1046 = x3d.HAnimSite()
HAnimSite1046.USE = "STD_Site_r_carpal_distal_phalanx_1_tip"

HAnimHumanoid13.sites.append(HAnimSite1046)
HAnimJoint1047 = x3d.HAnimJoint()
HAnimJoint1047.USE = "STD_Joint_r_midcarpal_2"

HAnimHumanoid13.joints.append(HAnimJoint1047)
HAnimSegment1048 = x3d.HAnimSegment()
HAnimSegment1048.USE = "STD_Segment_r_trapezoid"

HAnimHumanoid13.segments.append(HAnimSegment1048)
HAnimJoint1049 = x3d.HAnimJoint()
HAnimJoint1049.USE = "STD_Joint_r_carpometacarpal_2"

HAnimHumanoid13.joints.append(HAnimJoint1049)
HAnimSegment1050 = x3d.HAnimSegment()
HAnimSegment1050.USE = "STD_Segment_r_metacarpal_2"

HAnimHumanoid13.segments.append(HAnimSegment1050)
HAnimSite1051 = x3d.HAnimSite()
HAnimSite1051.USE = "STD_Site_r_metacarpal_phalanx_2_pt"

HAnimHumanoid13.sites.append(HAnimSite1051)
HAnimJoint1052 = x3d.HAnimJoint()
HAnimJoint1052.USE = "STD_Joint_r_metacarpophalangeal_2"

HAnimHumanoid13.joints.append(HAnimJoint1052)
HAnimSegment1053 = x3d.HAnimSegment()
HAnimSegment1053.USE = "STD_Segment_r_carpal_proximal_phalanx_2 "

HAnimHumanoid13.segments.append(HAnimSegment1053)
HAnimJoint1054 = x3d.HAnimJoint()
HAnimJoint1054.USE = "STD_Joint_r_carpal_proximal_interphalangeal_2"

HAnimHumanoid13.joints.append(HAnimJoint1054)
HAnimSegment1055 = x3d.HAnimSegment()
HAnimSegment1055.USE = "STD_Segment_r_carpal_middle_phalanx_2"

HAnimHumanoid13.segments.append(HAnimSegment1055)
HAnimJoint1056 = x3d.HAnimJoint()
HAnimJoint1056.USE = "STD_Joint_r_carpal_distal_interphalangeal_2"

HAnimHumanoid13.joints.append(HAnimJoint1056)
HAnimSegment1057 = x3d.HAnimSegment()
HAnimSegment1057.USE = "STD_Segment_r_carpal_distal_phalanx_2"

HAnimHumanoid13.segments.append(HAnimSegment1057)
HAnimSite1058 = x3d.HAnimSite()
HAnimSite1058.USE = "STD_Site_r_carpal_distal_phalanx_2_tip"

HAnimHumanoid13.sites.append(HAnimSite1058)
HAnimSite1059 = x3d.HAnimSite()
HAnimSite1059.USE = "STD_Site_r_dactylion_pt"

HAnimHumanoid13.sites.append(HAnimSite1059)
HAnimJoint1060 = x3d.HAnimJoint()
HAnimJoint1060.USE = "STD_Joint_r_midcarpal_3"

HAnimHumanoid13.joints.append(HAnimJoint1060)
HAnimSegment1061 = x3d.HAnimSegment()
HAnimSegment1061.USE = "STD_Segment_r_capitate"

HAnimHumanoid13.segments.append(HAnimSegment1061)
HAnimJoint1062 = x3d.HAnimJoint()
HAnimJoint1062.USE = "STD_Joint_r_carpometacarpal_3"

HAnimHumanoid13.joints.append(HAnimJoint1062)
HAnimSegment1063 = x3d.HAnimSegment()
HAnimSegment1063.USE = "STD_Segment_r_metacarpal_3"

HAnimHumanoid13.segments.append(HAnimSegment1063)
HAnimSite1064 = x3d.HAnimSite()
HAnimSite1064.USE = "STD_Site_r_metacarpal_phalanx_3_pt"

HAnimHumanoid13.sites.append(HAnimSite1064)
HAnimJoint1065 = x3d.HAnimJoint()
HAnimJoint1065.USE = "STD_Joint_r_metacarpophalangeal_3"

HAnimHumanoid13.joints.append(HAnimJoint1065)
HAnimSegment1066 = x3d.HAnimSegment()
HAnimSegment1066.USE = "STD_Segment_r_carpal_proximal_phalanx_3"

HAnimHumanoid13.segments.append(HAnimSegment1066)
HAnimJoint1067 = x3d.HAnimJoint()
HAnimJoint1067.USE = "STD_Joint_r_carpal_proximal_interphalangeal_3"

HAnimHumanoid13.joints.append(HAnimJoint1067)
HAnimSegment1068 = x3d.HAnimSegment()
HAnimSegment1068.USE = "STD_Segment_r_carpal_middle_phalanx_3"

HAnimHumanoid13.segments.append(HAnimSegment1068)
HAnimJoint1069 = x3d.HAnimJoint()
HAnimJoint1069.USE = "STD_Joint_r_carpal_distal_interphalangeal_3"

HAnimHumanoid13.joints.append(HAnimJoint1069)
HAnimSegment1070 = x3d.HAnimSegment()
HAnimSegment1070.USE = "STD_Segment_r_carpal_distal_phalanx_3"

HAnimHumanoid13.segments.append(HAnimSegment1070)
HAnimSite1071 = x3d.HAnimSite()
HAnimSite1071.USE = "STD_Site_r_carpal_distal_phalanx_3_tip"

HAnimHumanoid13.sites.append(HAnimSite1071)
HAnimJoint1072 = x3d.HAnimJoint()
HAnimJoint1072.USE = "STD_Joint_r_midcarpal_4_5"

HAnimHumanoid13.joints.append(HAnimJoint1072)
HAnimSegment1073 = x3d.HAnimSegment()
HAnimSegment1073.USE = "STD_Segment_r_hamate"

HAnimHumanoid13.segments.append(HAnimSegment1073)
HAnimJoint1074 = x3d.HAnimJoint()
HAnimJoint1074.USE = "STD_Joint_r_carpometacarpal_4"

HAnimHumanoid13.joints.append(HAnimJoint1074)
HAnimSegment1075 = x3d.HAnimSegment()
HAnimSegment1075.USE = "STD_Segment_r_metacarpal_4"

HAnimHumanoid13.segments.append(HAnimSegment1075)
HAnimJoint1076 = x3d.HAnimJoint()
HAnimJoint1076.USE = "STD_Joint_r_metacarpophalangeal_4"

HAnimHumanoid13.joints.append(HAnimJoint1076)
HAnimSegment1077 = x3d.HAnimSegment()
HAnimSegment1077.USE = "STD_Segment_r_carpal_proximal_phalanx_4"

HAnimHumanoid13.segments.append(HAnimSegment1077)
HAnimJoint1078 = x3d.HAnimJoint()
HAnimJoint1078.USE = "STD_Joint_r_carpal_proximal_interphalangeal_4"

HAnimHumanoid13.joints.append(HAnimJoint1078)
HAnimSegment1079 = x3d.HAnimSegment()
HAnimSegment1079.USE = "STD_Segment_r_carpal_middle_phalanx_4"

HAnimHumanoid13.segments.append(HAnimSegment1079)
HAnimJoint1080 = x3d.HAnimJoint()
HAnimJoint1080.USE = "STD_Joint_r_carpal_distal_interphalangeal_4"

HAnimHumanoid13.joints.append(HAnimJoint1080)
HAnimSegment1081 = x3d.HAnimSegment()
HAnimSegment1081.USE = "STD_Segment_r_carpal_distal_phalanx_4"

HAnimHumanoid13.segments.append(HAnimSegment1081)
HAnimSite1082 = x3d.HAnimSite()
HAnimSite1082.USE = "STD_Site_r_carpal_distal_phalanx_4_tip"

HAnimHumanoid13.sites.append(HAnimSite1082)
HAnimJoint1083 = x3d.HAnimJoint()
HAnimJoint1083.USE = "STD_Joint_r_carpometacarpal_5"

HAnimHumanoid13.joints.append(HAnimJoint1083)
HAnimSegment1084 = x3d.HAnimSegment()
HAnimSegment1084.USE = "STD_Segment_r_metacarpal_5"

HAnimHumanoid13.segments.append(HAnimSegment1084)
HAnimSite1085 = x3d.HAnimSite()
HAnimSite1085.USE = "STD_Site_r_metacarpal_phalanx_5_pt"

HAnimHumanoid13.sites.append(HAnimSite1085)
HAnimJoint1086 = x3d.HAnimJoint()
HAnimJoint1086.USE = "STD_Joint_r_metacarpophalangeal_5"

HAnimHumanoid13.joints.append(HAnimJoint1086)
HAnimSegment1087 = x3d.HAnimSegment()
HAnimSegment1087.USE = "STD_Segment_r_carpal_proximal_phalanx_5"

HAnimHumanoid13.segments.append(HAnimSegment1087)
HAnimJoint1088 = x3d.HAnimJoint()
HAnimJoint1088.USE = "STD_Joint_r_carpal_proximal_interphalangeal_5"

HAnimHumanoid13.joints.append(HAnimJoint1088)
HAnimSegment1089 = x3d.HAnimSegment()
HAnimSegment1089.USE = "STD_Segment_r_carpal_middle_phalanx_5"

HAnimHumanoid13.segments.append(HAnimSegment1089)
HAnimJoint1090 = x3d.HAnimJoint()
HAnimJoint1090.USE = "STD_Joint_r_carpal_distal_interphalangeal_5"

HAnimHumanoid13.joints.append(HAnimJoint1090)
HAnimSegment1091 = x3d.HAnimSegment()
HAnimSegment1091.USE = "STD_Segment_r_carpal_distal_phalanx_5"

HAnimHumanoid13.segments.append(HAnimSegment1091)
HAnimSite1092 = x3d.HAnimSite()
HAnimSite1092.USE = "STD_Site_r_carpal_distal_phalanx_5_tip"

HAnimHumanoid13.sites.append(HAnimSite1092)

HAnimHumanoid10.skeleton.append(HAnimHumanoid10)

X3D0.Scene = Scene10
f = open("skeleton_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
