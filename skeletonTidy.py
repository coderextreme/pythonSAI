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
meta4.content = "http://www.web3d.org/x3d/content/examples/HumanoidAnimation/JohnBoy.x3d"
meta4.name = "identifier"

head1.children.append(meta4)
meta5 = x3d.meta()
meta5.content = "An attempt at a standard LOA-4 skeleton"
meta5.name = "description"

head1.children.append(meta5)
meta6 = x3d.meta()
meta6.content = "h.pl"
meta6.name = "generator"

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
WorldInfo11 = x3d.WorldInfo()
WorldInfo11.title = "JohnBoy.x3d"

Scene10.children.append(WorldInfo11)
NavigationInfo12 = x3d.NavigationInfo()
NavigationInfo12.speed = 1.5

Scene10.children.append(NavigationInfo12)
Viewpoint13 = x3d.Viewpoint()
Viewpoint13.centerOfRotation = [0,1,0]
Viewpoint13.description = "JohnBoy"
Viewpoint13.position = [0,1,3]

Scene10.children.append(Viewpoint13)
HAnimHumanoid14 = x3d.HAnimHumanoid()
HAnimHumanoid14.DEF = "STD_HAnim"
HAnimHumanoid14.bboxDisplay = False
HAnimHumanoid14.name = "HAnim"
HAnimHumanoid14.scale = [0.0225,0.0225,0.0225]
HAnimHumanoid14.visible = True
HAnimHumanoid14.version = "2.0"
"""HAnimHumanoid original info='\"humanoidVersion=2.0\"'"""
MetadataSet15 = x3d.MetadataSet()
MetadataSet15.name = "HAnimHumanoid.info"
MetadataSet15.reference = "https://www.web3d.org/documents/specifications/19774/V2.0/Architecture/ObjectInterfaces.html#Humanoid"
MetadataString16 = x3d.MetadataString()
MetadataString16.name = "humanoidVersion"
MetadataString16.value = ["."]

if MetadataSet15.value is None:
    MetadataSet15.value = []
MetadataSet15.value.append(MetadataString16)

HAnimHumanoid14.metadata = MetadataSet15
HAnimJoint17 = x3d.HAnimJoint()
HAnimJoint17.DEF = "STD_Joint_humanoid_root"
HAnimJoint17.bboxCenter = [0,0,0]
HAnimJoint17.bboxDisplay = False
HAnimJoint17.bboxSize = [-1,-1,-1]
HAnimJoint17.center = [0.0000,0.8240,0.0277]
HAnimJoint17.name = "humanoid_root"
HAnimJoint17.visible = True
HAnimSegment18 = x3d.HAnimSegment()
HAnimSegment18.DEF = "STD_HAnimSegment_HumanoidRoot"
HAnimSegment18.bboxDisplay = False
HAnimSegment18.name = "HAnimSegment_HumanoidRoot"
HAnimSegment18.visible = True
Viewpoint19 = x3d.Viewpoint()
Viewpoint19.description = "View from (0 0 4) towards HAnimHumanoid center"
Viewpoint19.position = [0,0,4]

HAnimSegment18.children.append(Viewpoint19)
Switch20 = x3d.Switch()
Switch20.bboxCenter = [0,0,0]
Switch20.bboxDisplay = False
Switch20.bboxSize = [-1,-1,-1]
Switch20.visible = True
Switch20.whichChoice = 0
Group21 = x3d.Group()
Group21.bboxCenter = [0,0,0]
Group21.bboxDisplay = False
Group21.bboxSize = [-1,-1,-1]
Group21.visible = True
TouchSensor22 = x3d.TouchSensor()
TouchSensor22.description = "HAnimHumanoid HAnimSegment HumanoidRoot"

Group21.children.append(TouchSensor22)
Shape23 = x3d.Shape()
Shape23.DEF = "HAnimRootShape"
Shape23.bboxCenter = [0,0,0]
Shape23.bboxDisplay = False
Shape23.bboxSize = [-1,-1,-1]
Shape23.visible = True
Sphere24 = x3d.Sphere()
Sphere24.DEF = "HAnimJointSphere"

Shape23.geometry = Sphere24
Appearance25 = x3d.Appearance()
Material26 = x3d.Material()
Material26.DEF = "HAnimRootMaterial"
Material26.diffuseColor = [0.8,0,0]
Material26.transparency = 0.3

Appearance25.material = Material26

Shape23.appearance = Appearance25

Group21.children.append(Shape23)

Switch20.children.append(Group21)
Shape27 = x3d.Shape()
Shape27.DEF = "HAnimJointShape"
Shape27.bboxCenter = [0,0,0]
Shape27.bboxDisplay = False
Shape27.bboxSize = [-1,-1,-1]
Shape27.visible = True
Sphere28 = x3d.Sphere()
Sphere28.USE = "HAnimJointSphere"

Shape27.geometry = Sphere28
Appearance29 = x3d.Appearance()
Material30 = x3d.Material()
Material30.DEF = "HAnimJointMaterial"
Material30.diffuseColor = [0,0,0.8]
Material30.transparency = 0.3

Appearance29.material = Material30

Shape27.appearance = Appearance29

Switch20.children.append(Shape27)
Shape31 = x3d.Shape()
Shape31.bboxCenter = [0,0,0]
Shape31.bboxDisplay = False
Shape31.bboxSize = [-1,-1,-1]
Shape31.visible = True
LineSet32 = x3d.LineSet()
LineSet32.vertexCount = [2]
ColorRGBA33 = x3d.ColorRGBA()
ColorRGBA33.DEF = "HAnimSegmentLineColorRGBA"

LineSet32.color = ColorRGBA33
Coordinate34 = x3d.Coordinate()

LineSet32.coord = Coordinate34

Shape31.geometry = LineSet32

Switch20.children.append(Shape31)
Shape35 = x3d.Shape()
Shape35.DEF = "HAnimSiteShape"
Shape35.bboxCenter = [0,0,0]
Shape35.bboxDisplay = False
Shape35.bboxSize = [-1,-1,-1]
Shape35.visible = True
IndexedFaceSet36 = x3d.IndexedFaceSet()
IndexedFaceSet36.DEF = "DiamondIFS"
IndexedFaceSet36.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet36.creaseAngle = 0.5
IndexedFaceSet36.solid = False
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

Switch20.children.append(Shape35)

HAnimSegment18.children.append(Switch20)

HAnimJoint17.children.append(HAnimSegment18)
HAnimSegment41 = x3d.HAnimSegment()
HAnimSegment41.DEF = "STD_Segment_sacrum"
HAnimSegment41.bboxDisplay = False
HAnimSegment41.name = "sacrum"
HAnimSegment41.visible = True

HAnimJoint17.children.append(HAnimSegment41)
HAnimJoint42 = x3d.HAnimJoint()
HAnimJoint42.DEF = "STD_Joint_sacroiliac"
HAnimJoint42.bboxCenter = [0,0,0]
HAnimJoint42.bboxDisplay = False
HAnimJoint42.bboxSize = [-1,-1,-1]
HAnimJoint42.center = [0.0000,0.9149,0.0016]
HAnimJoint42.name = "sacroiliac"
HAnimJoint42.visible = True
HAnimSegment43 = x3d.HAnimSegment()
HAnimSegment43.DEF = "STD_Segment_pelvis"
HAnimSegment43.bboxDisplay = False
HAnimSegment43.name = "pelvis"
HAnimSegment43.visible = True
HAnimSite44 = x3d.HAnimSite()
HAnimSite44.DEF = "STD_Site_l_asis_pt"
HAnimSite44.bboxCenter = [0,0,0]
HAnimSite44.bboxDisplay = False
HAnimSite44.bboxSize = [-1,-1,-1]
HAnimSite44.name = "l_asis_pt"
HAnimSite44.translation = [0.0925,0.9983,0.1052]
HAnimSite44.visible = True
TouchSensor45 = x3d.TouchSensor()
TouchSensor45.description = "HAnimSite l_asis_pt"

HAnimSite44.children.append(TouchSensor45)
Shape46 = x3d.Shape()
Shape46.USE = "HAnimSiteShape"
Shape46.bboxCenter = [0,0,0]
Shape46.bboxDisplay = False
Shape46.bboxSize = [-1,-1,-1]
Shape46.visible = True

HAnimSite44.children.append(Shape46)

HAnimSegment43.children.append(HAnimSite44)
HAnimSite47 = x3d.HAnimSite()
HAnimSite47.DEF = "STD_Site_r_asis_pt"
HAnimSite47.bboxCenter = [0,0,0]
HAnimSite47.bboxDisplay = False
HAnimSite47.bboxSize = [-1,-1,-1]
HAnimSite47.name = "r_asis_pt"
HAnimSite47.translation = [-0.0887,1.0021,0.1112]
HAnimSite47.visible = True
TouchSensor48 = x3d.TouchSensor()
TouchSensor48.description = "HAnimSite r_asis_pt"

HAnimSite47.children.append(TouchSensor48)
Shape49 = x3d.Shape()
Shape49.USE = "HAnimSiteShape"
Shape49.bboxCenter = [0,0,0]
Shape49.bboxDisplay = False
Shape49.bboxSize = [-1,-1,-1]
Shape49.visible = True

HAnimSite47.children.append(Shape49)

HAnimSegment43.children.append(HAnimSite47)
HAnimSite50 = x3d.HAnimSite()
HAnimSite50.DEF = "STD_Site_crotch_pt"
HAnimSite50.bboxCenter = [0,0,0]
HAnimSite50.bboxDisplay = False
HAnimSite50.bboxSize = [-1,-1,-1]
HAnimSite50.name = "crotch_pt"
HAnimSite50.translation = [0.0034,0.8266,0.0257]
HAnimSite50.visible = True
TouchSensor51 = x3d.TouchSensor()
TouchSensor51.description = "HAnimSite crotch_pt"

HAnimSite50.children.append(TouchSensor51)
Shape52 = x3d.Shape()
Shape52.USE = "HAnimSiteShape"
Shape52.bboxCenter = [0,0,0]
Shape52.bboxDisplay = False
Shape52.bboxSize = [-1,-1,-1]
Shape52.visible = True

HAnimSite50.children.append(Shape52)

HAnimSegment43.children.append(HAnimSite50)
HAnimSite53 = x3d.HAnimSite()
HAnimSite53.DEF = "STD_Site_l_psis_pt"
HAnimSite53.bboxCenter = [0,0,0]
HAnimSite53.bboxDisplay = False
HAnimSite53.bboxSize = [-1,-1,-1]
HAnimSite53.name = "l_psis_pt"
HAnimSite53.translation = [0.0774,1.0190,-0.1151]
HAnimSite53.visible = True
TouchSensor54 = x3d.TouchSensor()
TouchSensor54.description = "HAnimSite l_psis_pt"

HAnimSite53.children.append(TouchSensor54)
Shape55 = x3d.Shape()
Shape55.USE = "HAnimSiteShape"
Shape55.bboxCenter = [0,0,0]
Shape55.bboxDisplay = False
Shape55.bboxSize = [-1,-1,-1]
Shape55.visible = True

HAnimSite53.children.append(Shape55)

HAnimSegment43.children.append(HAnimSite53)
HAnimSite56 = x3d.HAnimSite()
HAnimSite56.DEF = "STD_Site_r_trochanterion_pt"
HAnimSite56.bboxCenter = [0,0,0]
HAnimSite56.bboxDisplay = False
HAnimSite56.bboxSize = [-1,-1,-1]
HAnimSite56.name = "r_trochanterion_pt"
HAnimSite56.translation = [-0.1689,0.8419,0.0352]
HAnimSite56.visible = True
TouchSensor57 = x3d.TouchSensor()
TouchSensor57.description = "HAnimSite r_trochanterion_pt"

HAnimSite56.children.append(TouchSensor57)
Shape58 = x3d.Shape()
Shape58.USE = "HAnimSiteShape"
Shape58.bboxCenter = [0,0,0]
Shape58.bboxDisplay = False
Shape58.bboxSize = [-1,-1,-1]
Shape58.visible = True

HAnimSite56.children.append(Shape58)

HAnimSegment43.children.append(HAnimSite56)
HAnimSite59 = x3d.HAnimSite()
HAnimSite59.DEF = "STD_Site_r_iliocristale_pt"
HAnimSite59.bboxCenter = [0,0,0]
HAnimSite59.bboxDisplay = False
HAnimSite59.bboxSize = [-1,-1,-1]
HAnimSite59.name = "r_iliocristale_pt"
HAnimSite59.translation = [-0.1525,1.0628,0.0035]
HAnimSite59.visible = True
TouchSensor60 = x3d.TouchSensor()
TouchSensor60.description = "HAnimSite r_iliocristale_pt"

HAnimSite59.children.append(TouchSensor60)
Shape61 = x3d.Shape()
Shape61.USE = "HAnimSiteShape"
Shape61.bboxCenter = [0,0,0]
Shape61.bboxDisplay = False
Shape61.bboxSize = [-1,-1,-1]
Shape61.visible = True

HAnimSite59.children.append(Shape61)

HAnimSegment43.children.append(HAnimSite59)
HAnimSite62 = x3d.HAnimSite()
HAnimSite62.DEF = "STD_Site_r_psis_pt"
HAnimSite62.bboxCenter = [0,0,0]
HAnimSite62.bboxDisplay = False
HAnimSite62.bboxSize = [-1,-1,-1]
HAnimSite62.name = "r_psis_pt"
HAnimSite62.translation = [-0.0716,1.0190,-0.1138]
HAnimSite62.visible = True
TouchSensor63 = x3d.TouchSensor()
TouchSensor63.description = "HAnimSite r_psis_pt"

HAnimSite62.children.append(TouchSensor63)
Shape64 = x3d.Shape()
Shape64.USE = "HAnimSiteShape"
Shape64.bboxCenter = [0,0,0]
Shape64.bboxDisplay = False
Shape64.bboxSize = [-1,-1,-1]
Shape64.visible = True

HAnimSite62.children.append(Shape64)

HAnimSegment43.children.append(HAnimSite62)
HAnimSite65 = x3d.HAnimSite()
HAnimSite65.DEF = "STD_Site_l_trochanterion_pt"
HAnimSite65.bboxCenter = [0,0,0]
HAnimSite65.bboxDisplay = False
HAnimSite65.bboxSize = [-1,-1,-1]
HAnimSite65.name = "l_trochanterion_pt"
HAnimSite65.translation = [0.1677,0.8336,0.0303]
HAnimSite65.visible = True
TouchSensor66 = x3d.TouchSensor()
TouchSensor66.description = "HAnimSite l_trochanterion_pt"

HAnimSite65.children.append(TouchSensor66)
Shape67 = x3d.Shape()
Shape67.USE = "HAnimSiteShape"
Shape67.bboxCenter = [0,0,0]
Shape67.bboxDisplay = False
Shape67.bboxSize = [-1,-1,-1]
Shape67.visible = True

HAnimSite65.children.append(Shape67)

HAnimSegment43.children.append(HAnimSite65)
HAnimSite68 = x3d.HAnimSite()
HAnimSite68.DEF = "STD_Site_l_iliocristale_pt"
HAnimSite68.bboxCenter = [0,0,0]
HAnimSite68.bboxDisplay = False
HAnimSite68.bboxSize = [-1,-1,-1]
HAnimSite68.name = "l_iliocristale_pt"
HAnimSite68.translation = [0.1612,1.0537,0.0008]
HAnimSite68.visible = True
TouchSensor69 = x3d.TouchSensor()
TouchSensor69.description = "HAnimSite l_iliocristale_pt"

HAnimSite68.children.append(TouchSensor69)
Shape70 = x3d.Shape()
Shape70.USE = "HAnimSiteShape"
Shape70.bboxCenter = [0,0,0]
Shape70.bboxDisplay = False
Shape70.bboxSize = [-1,-1,-1]
Shape70.visible = True

HAnimSite68.children.append(Shape70)

HAnimSegment43.children.append(HAnimSite68)
HAnimSite71 = x3d.HAnimSite()
HAnimSite71.DEF = "STD_Site_buttocks_standing_wall_contact_point_pt"
HAnimSite71.bboxCenter = [0,0,0]
HAnimSite71.bboxDisplay = False
HAnimSite71.bboxSize = [-1,-1,-1]
HAnimSite71.name = "buttocks_standing_wall_contact_point_pt"
HAnimSite71.visible = True
TouchSensor72 = x3d.TouchSensor()
TouchSensor72.description = "HAnimSite buttocks_standing_wall_contact_point_pt"

HAnimSite71.children.append(TouchSensor72)
Shape73 = x3d.Shape()
Shape73.USE = "HAnimSiteShape"
Shape73.bboxCenter = [0,0,0]
Shape73.bboxDisplay = False
Shape73.bboxSize = [-1,-1,-1]
Shape73.visible = True

HAnimSite71.children.append(Shape73)

HAnimSegment43.children.append(HAnimSite71)

HAnimJoint42.children.append(HAnimSegment43)
HAnimJoint74 = x3d.HAnimJoint()
HAnimJoint74.DEF = "STD_Joint_l_hip"
HAnimJoint74.bboxCenter = [0,0,0]
HAnimJoint74.bboxDisplay = False
HAnimJoint74.bboxSize = [-1,-1,-1]
HAnimJoint74.center = [0.0961,0.9124,-0.0001]
HAnimJoint74.name = "l_hip"
HAnimJoint74.visible = True
HAnimSegment75 = x3d.HAnimSegment()
HAnimSegment75.DEF = "STD_Segment_l_thigh"
HAnimSegment75.bboxDisplay = False
HAnimSegment75.name = "l_thigh"
HAnimSegment75.visible = True
HAnimSite76 = x3d.HAnimSite()
HAnimSite76.DEF = "STD_Site_l_suprapatella_pt"
HAnimSite76.bboxCenter = [0,0,0]
HAnimSite76.bboxDisplay = False
HAnimSite76.bboxSize = [-1,-1,-1]
HAnimSite76.name = "l_suprapatella_pt"
HAnimSite76.visible = True
TouchSensor77 = x3d.TouchSensor()
TouchSensor77.description = "HAnimSite l_suprapatella_pt"

HAnimSite76.children.append(TouchSensor77)
Shape78 = x3d.Shape()
Shape78.USE = "HAnimSiteShape"
Shape78.bboxCenter = [0,0,0]
Shape78.bboxDisplay = False
Shape78.bboxSize = [-1,-1,-1]
Shape78.visible = True

HAnimSite76.children.append(Shape78)

HAnimSegment75.children.append(HAnimSite76)
HAnimSite79 = x3d.HAnimSite()
HAnimSite79.DEF = "STD_Site_l_knee_crease_pt"
HAnimSite79.bboxCenter = [0,0,0]
HAnimSite79.bboxDisplay = False
HAnimSite79.bboxSize = [-1,-1,-1]
HAnimSite79.name = "l_knee_crease_pt"
HAnimSite79.translation = [0.0993,0.4881,-0.0309]
HAnimSite79.visible = True
TouchSensor80 = x3d.TouchSensor()
TouchSensor80.description = "HAnimSite l_knee_crease_pt"

HAnimSite79.children.append(TouchSensor80)
Shape81 = x3d.Shape()
Shape81.USE = "HAnimSiteShape"
Shape81.bboxCenter = [0,0,0]
Shape81.bboxDisplay = False
Shape81.bboxSize = [-1,-1,-1]
Shape81.visible = True

HAnimSite79.children.append(Shape81)

HAnimSegment75.children.append(HAnimSite79)
HAnimSite82 = x3d.HAnimSite()
HAnimSite82.DEF = "STD_Site_l_femoral_medial_epicondyles_pt"
HAnimSite82.bboxCenter = [0,0,0]
HAnimSite82.bboxDisplay = False
HAnimSite82.bboxSize = [-1,-1,-1]
HAnimSite82.name = "l_femoral_medial_epicondyles_pt"
HAnimSite82.translation = [0.0398,0.4946,0.0303]
HAnimSite82.visible = True
TouchSensor83 = x3d.TouchSensor()
TouchSensor83.description = "HAnimSite l_femoral_medial_epicondyles_pt"

HAnimSite82.children.append(TouchSensor83)
Shape84 = x3d.Shape()
Shape84.USE = "HAnimSiteShape"
Shape84.bboxCenter = [0,0,0]
Shape84.bboxDisplay = False
Shape84.bboxSize = [-1,-1,-1]
Shape84.visible = True

HAnimSite82.children.append(Shape84)

HAnimSegment75.children.append(HAnimSite82)
HAnimSite85 = x3d.HAnimSite()
HAnimSite85.DEF = "STD_Site_l_femoral_lateral_epicondyles_pt"
HAnimSite85.bboxCenter = [0,0,0]
HAnimSite85.bboxDisplay = False
HAnimSite85.bboxSize = [-1,-1,-1]
HAnimSite85.name = "l_femoral_lateral_epicondyles_pt"
HAnimSite85.translation = [0.1598,0.4967,0.0297]
HAnimSite85.visible = True
TouchSensor86 = x3d.TouchSensor()
TouchSensor86.description = "HAnimSite l_femoral_lateral_epicondyles_pt"

HAnimSite85.children.append(TouchSensor86)
Shape87 = x3d.Shape()
Shape87.USE = "HAnimSiteShape"
Shape87.bboxCenter = [0,0,0]
Shape87.bboxDisplay = False
Shape87.bboxSize = [-1,-1,-1]
Shape87.visible = True

HAnimSite85.children.append(Shape87)

HAnimSegment75.children.append(HAnimSite85)

HAnimJoint74.children.append(HAnimSegment75)
HAnimJoint88 = x3d.HAnimJoint()
HAnimJoint88.DEF = "STD_Joint_l_knee"
HAnimJoint88.bboxCenter = [0,0,0]
HAnimJoint88.bboxDisplay = False
HAnimJoint88.bboxSize = [-1,-1,-1]
HAnimJoint88.center = [0.1040,0.4867,0.0308]
HAnimJoint88.name = "l_knee"
HAnimJoint88.visible = True
HAnimSegment89 = x3d.HAnimSegment()
HAnimSegment89.DEF = "STD_Segment_l_calf"
HAnimSegment89.bboxDisplay = False
HAnimSegment89.name = "l_calf"
HAnimSegment89.visible = True
HAnimSite90 = x3d.HAnimSite()
HAnimSite90.DEF = "STD_Site_l_tibiale_pt"
HAnimSite90.bboxCenter = [0,0,0]
HAnimSite90.bboxDisplay = False
HAnimSite90.bboxSize = [-1,-1,-1]
HAnimSite90.name = "l_tibiale_pt"
HAnimSite90.visible = True
TouchSensor91 = x3d.TouchSensor()
TouchSensor91.description = "HAnimSite l_tibiale_pt"

HAnimSite90.children.append(TouchSensor91)
Shape92 = x3d.Shape()
Shape92.USE = "HAnimSiteShape"
Shape92.bboxCenter = [0,0,0]
Shape92.bboxDisplay = False
Shape92.bboxSize = [-1,-1,-1]
Shape92.visible = True

HAnimSite90.children.append(Shape92)

HAnimSegment89.children.append(HAnimSite90)
HAnimSite93 = x3d.HAnimSite()
HAnimSite93.DEF = "STD_Site_l_lateral_malleolus_pt"
HAnimSite93.bboxCenter = [0,0,0]
HAnimSite93.bboxDisplay = False
HAnimSite93.bboxSize = [-1,-1,-1]
HAnimSite93.name = "l_lateral_malleolus_pt"
HAnimSite93.translation = [0.1308,0.0597,-0.1032]
HAnimSite93.visible = True
TouchSensor94 = x3d.TouchSensor()
TouchSensor94.description = "HAnimSite l_lateral_malleolus_pt"

HAnimSite93.children.append(TouchSensor94)
Shape95 = x3d.Shape()
Shape95.USE = "HAnimSiteShape"
Shape95.bboxCenter = [0,0,0]
Shape95.bboxDisplay = False
Shape95.bboxSize = [-1,-1,-1]
Shape95.visible = True

HAnimSite93.children.append(Shape95)

HAnimSegment89.children.append(HAnimSite93)
HAnimSite96 = x3d.HAnimSite()
HAnimSite96.DEF = "STD_Site_l_medial_malleolus_pt"
HAnimSite96.bboxCenter = [0,0,0]
HAnimSite96.bboxDisplay = False
HAnimSite96.bboxSize = [-1,-1,-1]
HAnimSite96.name = "l_medial_malleolus_pt"
HAnimSite96.translation = [0.0890,0.0716,-0.0881]
HAnimSite96.visible = True
TouchSensor97 = x3d.TouchSensor()
TouchSensor97.description = "HAnimSite l_medial_malleolus_pt"

HAnimSite96.children.append(TouchSensor97)
Shape98 = x3d.Shape()
Shape98.USE = "HAnimSiteShape"
Shape98.bboxCenter = [0,0,0]
Shape98.bboxDisplay = False
Shape98.bboxSize = [-1,-1,-1]
Shape98.visible = True

HAnimSite96.children.append(Shape98)

HAnimSegment89.children.append(HAnimSite96)

HAnimJoint88.children.append(HAnimSegment89)
HAnimJoint99 = x3d.HAnimJoint()
HAnimJoint99.DEF = "STD_Joint_l_talocrural"
HAnimJoint99.bboxCenter = [0,0,0]
HAnimJoint99.bboxDisplay = False
HAnimJoint99.bboxSize = [-1,-1,-1]
HAnimJoint99.center = [0.1101,0.0656,-0.0736]
HAnimJoint99.name = "l_talocrural"
HAnimJoint99.visible = True
HAnimSegment100 = x3d.HAnimSegment()
HAnimSegment100.DEF = "STD_Segment_l_talus"
HAnimSegment100.bboxDisplay = False
HAnimSegment100.name = "l_talus"
HAnimSegment100.visible = True
HAnimSite101 = x3d.HAnimSite()
HAnimSite101.DEF = "STD_Site_l_calcaneus_posterior_pt"
HAnimSite101.bboxCenter = [0,0,0]
HAnimSite101.bboxDisplay = False
HAnimSite101.bboxSize = [-1,-1,-1]
HAnimSite101.name = "l_calcaneus_posterior_pt"
HAnimSite101.translation = [0.0974,0.0259,-0.1171]
HAnimSite101.visible = True
TouchSensor102 = x3d.TouchSensor()
TouchSensor102.description = "HAnimSite l_calcaneus_posterior_pt"

HAnimSite101.children.append(TouchSensor102)
Shape103 = x3d.Shape()
Shape103.USE = "HAnimSiteShape"
Shape103.bboxCenter = [0,0,0]
Shape103.bboxDisplay = False
Shape103.bboxSize = [-1,-1,-1]
Shape103.visible = True

HAnimSite101.children.append(Shape103)

HAnimSegment100.children.append(HAnimSite101)
HAnimSite104 = x3d.HAnimSite()
HAnimSite104.DEF = "STD_Site_l_sphyrion_pt"
HAnimSite104.bboxCenter = [0,0,0]
HAnimSite104.bboxDisplay = False
HAnimSite104.bboxSize = [-1,-1,-1]
HAnimSite104.name = "l_sphyrion_pt"
HAnimSite104.translation = [0.0890,0.0575,-0.0943]
HAnimSite104.visible = True
TouchSensor105 = x3d.TouchSensor()
TouchSensor105.description = "HAnimSite l_sphyrion_pt"

HAnimSite104.children.append(TouchSensor105)
Shape106 = x3d.Shape()
Shape106.USE = "HAnimSiteShape"
Shape106.bboxCenter = [0,0,0]
Shape106.bboxDisplay = False
Shape106.bboxSize = [-1,-1,-1]
Shape106.visible = True

HAnimSite104.children.append(Shape106)

HAnimSegment100.children.append(HAnimSite104)

HAnimJoint99.children.append(HAnimSegment100)
HAnimJoint107 = x3d.HAnimJoint()
HAnimJoint107.DEF = "STD_Joint_l_talocalcaneonavicular"
HAnimJoint107.bboxCenter = [0,0,0]
HAnimJoint107.bboxDisplay = False
HAnimJoint107.bboxSize = [-1,-1,-1]
HAnimJoint107.name = "l_talocalcaneonavicular"
HAnimJoint107.visible = True
HAnimSegment108 = x3d.HAnimSegment()
HAnimSegment108.DEF = "STD_Segment_l_navicular"
HAnimSegment108.bboxDisplay = False
HAnimSegment108.name = "l_navicular"
HAnimSegment108.visible = True

HAnimJoint107.children.append(HAnimSegment108)
HAnimJoint109 = x3d.HAnimJoint()
HAnimJoint109.DEF = "STD_Joint_l_cuneonavicular_1"
HAnimJoint109.bboxCenter = [0,0,0]
HAnimJoint109.bboxDisplay = False
HAnimJoint109.bboxSize = [-1,-1,-1]
HAnimJoint109.name = "l_cuneonavicular_1"
HAnimJoint109.visible = True
HAnimSegment110 = x3d.HAnimSegment()
HAnimSegment110.DEF = "STD_Segment_l_cuneiform_1"
HAnimSegment110.bboxDisplay = False
HAnimSegment110.name = "l_cuneiform_1"
HAnimSegment110.visible = True

HAnimJoint109.children.append(HAnimSegment110)
HAnimJoint111 = x3d.HAnimJoint()
HAnimJoint111.DEF = "STD_Joint_l_tarsometatarsal_1"
HAnimJoint111.bboxCenter = [0,0,0]
HAnimJoint111.bboxDisplay = False
HAnimJoint111.bboxSize = [-1,-1,-1]
HAnimJoint111.name = "l_tarsometatarsal_1"
HAnimJoint111.visible = True
HAnimSegment112 = x3d.HAnimSegment()
HAnimSegment112.DEF = "STD_Segment_l_metatarsal_1"
HAnimSegment112.bboxDisplay = False
HAnimSegment112.name = "l_metatarsal_1"
HAnimSegment112.visible = True

HAnimJoint111.children.append(HAnimSegment112)
HAnimJoint113 = x3d.HAnimJoint()
HAnimJoint113.DEF = "STD_Joint_l_metatarsophalangeal_1"
HAnimJoint113.bboxCenter = [0,0,0]
HAnimJoint113.bboxDisplay = False
HAnimJoint113.bboxSize = [-1,-1,-1]
HAnimJoint113.name = "l_metatarsophalangeal_1"
HAnimJoint113.visible = True
HAnimSegment114 = x3d.HAnimSegment()
HAnimSegment114.DEF = "STD_Segment_l_tarsal_proximal_phalanx_1"
HAnimSegment114.bboxDisplay = False
HAnimSegment114.name = "l_tarsal_proximal_phalanx_1"
HAnimSegment114.visible = True
HAnimSite115 = x3d.HAnimSite()
HAnimSite115.DEF = "STD_Site_l_metatarsal_phalanx_1_pt"
HAnimSite115.bboxCenter = [0,0,0]
HAnimSite115.bboxDisplay = False
HAnimSite115.bboxSize = [-1,-1,-1]
HAnimSite115.name = "l_metatarsal_phalanx_1_pt"
HAnimSite115.visible = True
TouchSensor116 = x3d.TouchSensor()
TouchSensor116.description = "HAnimSite l_metatarsal_phalanx_1_pt"

HAnimSite115.children.append(TouchSensor116)
Shape117 = x3d.Shape()
Shape117.USE = "HAnimSiteShape"
Shape117.bboxCenter = [0,0,0]
Shape117.bboxDisplay = False
Shape117.bboxSize = [-1,-1,-1]
Shape117.visible = True

HAnimSite115.children.append(Shape117)

HAnimSegment114.children.append(HAnimSite115)

HAnimJoint113.children.append(HAnimSegment114)
HAnimJoint118 = x3d.HAnimJoint()
HAnimJoint118.DEF = "STD_Joint_l_tarsal_interphalangeal_1"
HAnimJoint118.bboxCenter = [0,0,0]
HAnimJoint118.bboxDisplay = False
HAnimJoint118.bboxSize = [-1,-1,-1]
HAnimJoint118.name = "l_tarsal_interphalangeal_1"
HAnimJoint118.visible = True
HAnimSegment119 = x3d.HAnimSegment()
HAnimSegment119.DEF = "STD_Segment_l_tarsal_distal_phalanx_1"
HAnimSegment119.bboxDisplay = False
HAnimSegment119.name = "l_tarsal_distal_phalanx_1"
HAnimSegment119.visible = True
HAnimSite120 = x3d.HAnimSite()
HAnimSite120.DEF = "STD_Site_l_tarsal_distal_phalanx_1_pt"
HAnimSite120.bboxCenter = [0,0,0]
HAnimSite120.bboxDisplay = False
HAnimSite120.bboxSize = [-1,-1,-1]
HAnimSite120.name = "l_tarsal_distal_phalanx_1_pt"
HAnimSite120.visible = True
TouchSensor121 = x3d.TouchSensor()
TouchSensor121.description = "HAnimSite l_tarsal_distal_phalanx_1_pt"

HAnimSite120.children.append(TouchSensor121)
Shape122 = x3d.Shape()
Shape122.USE = "HAnimSiteShape"
Shape122.bboxCenter = [0,0,0]
Shape122.bboxDisplay = False
Shape122.bboxSize = [-1,-1,-1]
Shape122.visible = True

HAnimSite120.children.append(Shape122)

HAnimSegment119.children.append(HAnimSite120)

HAnimJoint118.children.append(HAnimSegment119)

HAnimJoint113.children.append(HAnimJoint118)

HAnimJoint111.children.append(HAnimJoint113)

HAnimJoint109.children.append(HAnimJoint111)

HAnimJoint107.children.append(HAnimJoint109)
HAnimJoint123 = x3d.HAnimJoint()
HAnimJoint123.DEF = "STD_Joint_l_cuneonavicular_2"
HAnimJoint123.bboxCenter = [0,0,0]
HAnimJoint123.bboxDisplay = False
HAnimJoint123.bboxSize = [-1,-1,-1]
HAnimJoint123.name = "l_cuneonavicular_2"
HAnimJoint123.visible = True
HAnimSegment124 = x3d.HAnimSegment()
HAnimSegment124.DEF = "STD_Segment_l_cuneiform_2"
HAnimSegment124.bboxDisplay = False
HAnimSegment124.name = "l_cuneiform_2"
HAnimSegment124.visible = True

HAnimJoint123.children.append(HAnimSegment124)
HAnimJoint125 = x3d.HAnimJoint()
HAnimJoint125.DEF = "STD_Joint_l_tarsometatarsal_2"
HAnimJoint125.bboxCenter = [0,0,0]
HAnimJoint125.bboxDisplay = False
HAnimJoint125.bboxSize = [-1,-1,-1]
HAnimJoint125.name = "l_tarsometatarsal_2"
HAnimJoint125.visible = True
HAnimSegment126 = x3d.HAnimSegment()
HAnimSegment126.DEF = "STD_Segment_l_metatarsal_2"
HAnimSegment126.bboxDisplay = False
HAnimSegment126.name = "l_metatarsal_2"
HAnimSegment126.visible = True

HAnimJoint125.children.append(HAnimSegment126)
HAnimJoint127 = x3d.HAnimJoint()
HAnimJoint127.DEF = "STD_Joint_l_metatarsophalangeal_2"
HAnimJoint127.bboxCenter = [0,0,0]
HAnimJoint127.bboxDisplay = False
HAnimJoint127.bboxSize = [-1,-1,-1]
HAnimJoint127.name = "l_metatarsophalangeal_2"
HAnimJoint127.visible = True
HAnimSegment128 = x3d.HAnimSegment()
HAnimSegment128.DEF = "STD_Segment_l_tarsal_proximal_phalanx_2"
HAnimSegment128.bboxDisplay = False
HAnimSegment128.name = "l_tarsal_proximal_phalanx_2"
HAnimSegment128.visible = True

HAnimJoint127.children.append(HAnimSegment128)
HAnimJoint129 = x3d.HAnimJoint()
HAnimJoint129.DEF = "STD_Joint_l_tarsal_proximal_interphalangeal_2"
HAnimJoint129.bboxCenter = [0,0,0]
HAnimJoint129.bboxDisplay = False
HAnimJoint129.bboxSize = [-1,-1,-1]
HAnimJoint129.name = "l_tarsal_proximal_interphalangeal_2"
HAnimJoint129.visible = True
HAnimSegment130 = x3d.HAnimSegment()
HAnimSegment130.DEF = "STD_Segment_l_tarsal_middle_phalanx_2"
HAnimSegment130.bboxDisplay = False
HAnimSegment130.name = "l_tarsal_middle_phalanx_2"
HAnimSegment130.visible = True

HAnimJoint129.children.append(HAnimSegment130)
HAnimJoint131 = x3d.HAnimJoint()
HAnimJoint131.DEF = "STD_Joint_l_tarsal_distal_interphalangeal_2"
HAnimJoint131.bboxCenter = [0,0,0]
HAnimJoint131.bboxDisplay = False
HAnimJoint131.bboxSize = [-1,-1,-1]
HAnimJoint131.name = "l_tarsal_distal_interphalangeal_2"
HAnimJoint131.visible = True
HAnimSegment132 = x3d.HAnimSegment()
HAnimSegment132.DEF = "STD_Segment_l_tarsal_distal_phalanx_2"
HAnimSegment132.bboxDisplay = False
HAnimSegment132.name = "l_tarsal_distal_phalanx_2"
HAnimSegment132.visible = True
HAnimSite133 = x3d.HAnimSite()
HAnimSite133.DEF = "STD_Site_l_tarsal_distal_phalanx_2_pt"
HAnimSite133.bboxCenter = [0,0,0]
HAnimSite133.bboxDisplay = False
HAnimSite133.bboxSize = [-1,-1,-1]
HAnimSite133.name = "l_tarsal_distal_phalanx_2_pt"
HAnimSite133.translation = [0.1195,0.0079,0.1433]
HAnimSite133.visible = True
TouchSensor134 = x3d.TouchSensor()
TouchSensor134.description = "HAnimSite l_tarsal_distal_phalanx_2_pt"

HAnimSite133.children.append(TouchSensor134)
Shape135 = x3d.Shape()
Shape135.USE = "HAnimSiteShape"
Shape135.bboxCenter = [0,0,0]
Shape135.bboxDisplay = False
Shape135.bboxSize = [-1,-1,-1]
Shape135.visible = True

HAnimSite133.children.append(Shape135)

HAnimSegment132.children.append(HAnimSite133)

HAnimJoint131.children.append(HAnimSegment132)

HAnimJoint129.children.append(HAnimJoint131)

HAnimJoint127.children.append(HAnimJoint129)

HAnimJoint125.children.append(HAnimJoint127)

HAnimJoint123.children.append(HAnimJoint125)

HAnimJoint107.children.append(HAnimJoint123)
HAnimJoint136 = x3d.HAnimJoint()
HAnimJoint136.DEF = "STD_Joint_l_cuneonavicular_3"
HAnimJoint136.bboxCenter = [0,0,0]
HAnimJoint136.bboxDisplay = False
HAnimJoint136.bboxSize = [-1,-1,-1]
HAnimJoint136.name = "l_cuneonavicular_3"
HAnimJoint136.visible = True
HAnimSegment137 = x3d.HAnimSegment()
HAnimSegment137.DEF = "STD_Segment_l_cuneiform_3"
HAnimSegment137.bboxDisplay = False
HAnimSegment137.name = "l_cuneiform_3"
HAnimSegment137.visible = True

HAnimJoint136.children.append(HAnimSegment137)
HAnimJoint138 = x3d.HAnimJoint()
HAnimJoint138.DEF = "STD_Joint_l_tarsometatarsal_3"
HAnimJoint138.bboxCenter = [0,0,0]
HAnimJoint138.bboxDisplay = False
HAnimJoint138.bboxSize = [-1,-1,-1]
HAnimJoint138.name = "l_tarsometatarsal_3"
HAnimJoint138.visible = True
HAnimSegment139 = x3d.HAnimSegment()
HAnimSegment139.DEF = "STD_Segment_l_metatarsal_3"
HAnimSegment139.bboxDisplay = False
HAnimSegment139.name = "l_metatarsal_3"
HAnimSegment139.visible = True

HAnimJoint138.children.append(HAnimSegment139)
HAnimJoint140 = x3d.HAnimJoint()
HAnimJoint140.DEF = "STD_Joint_l_metatarsophalangeal_3"
HAnimJoint140.bboxCenter = [0,0,0]
HAnimJoint140.bboxDisplay = False
HAnimJoint140.bboxSize = [-1,-1,-1]
HAnimJoint140.name = "l_metatarsophalangeal_3"
HAnimJoint140.visible = True
HAnimSegment141 = x3d.HAnimSegment()
HAnimSegment141.DEF = "STD_Segment_l_tarsal_proximal_phalanx_3"
HAnimSegment141.bboxDisplay = False
HAnimSegment141.name = "l_tarsal_proximal_phalanx_3"
HAnimSegment141.visible = True

HAnimJoint140.children.append(HAnimSegment141)
HAnimJoint142 = x3d.HAnimJoint()
HAnimJoint142.DEF = "STD_Joint_l_tarsal_proximal_interphalangeal_3"
HAnimJoint142.bboxCenter = [0,0,0]
HAnimJoint142.bboxDisplay = False
HAnimJoint142.bboxSize = [-1,-1,-1]
HAnimJoint142.name = "l_tarsal_proximal_interphalangeal_3"
HAnimJoint142.visible = True
HAnimSegment143 = x3d.HAnimSegment()
HAnimSegment143.DEF = "STD_Segment_l_tarsal_middle_phalanx_3"
HAnimSegment143.bboxDisplay = False
HAnimSegment143.name = "l_tarsal_middle_phalanx_3"
HAnimSegment143.visible = True

HAnimJoint142.children.append(HAnimSegment143)
HAnimJoint144 = x3d.HAnimJoint()
HAnimJoint144.DEF = "STD_Joint_l_tarsal_distal_interphalangeal_3"
HAnimJoint144.bboxCenter = [0,0,0]
HAnimJoint144.bboxDisplay = False
HAnimJoint144.bboxSize = [-1,-1,-1]
HAnimJoint144.name = "l_tarsal_distal_interphalangeal_3"
HAnimJoint144.visible = True
HAnimSegment145 = x3d.HAnimSegment()
HAnimSegment145.DEF = "STD_Segment_l_tarsal_distal_phalanx_3"
HAnimSegment145.bboxDisplay = False
HAnimSegment145.name = "l_tarsal_distal_phalanx_3"
HAnimSegment145.visible = True
HAnimSite146 = x3d.HAnimSite()
HAnimSite146.DEF = "STD_Site_l_tarsal_distal_phalanx_3_pt"
HAnimSite146.bboxCenter = [0,0,0]
HAnimSite146.bboxDisplay = False
HAnimSite146.bboxSize = [-1,-1,-1]
HAnimSite146.name = "l_tarsal_distal_phalanx_3_pt"
HAnimSite146.visible = True
TouchSensor147 = x3d.TouchSensor()
TouchSensor147.description = "HAnimSite l_tarsal_distal_phalanx_3_pt"

HAnimSite146.children.append(TouchSensor147)
Shape148 = x3d.Shape()
Shape148.USE = "HAnimSiteShape"
Shape148.bboxCenter = [0,0,0]
Shape148.bboxDisplay = False
Shape148.bboxSize = [-1,-1,-1]
Shape148.visible = True

HAnimSite146.children.append(Shape148)

HAnimSegment145.children.append(HAnimSite146)

HAnimJoint144.children.append(HAnimSegment145)

HAnimJoint142.children.append(HAnimJoint144)

HAnimJoint140.children.append(HAnimJoint142)

HAnimJoint138.children.append(HAnimJoint140)

HAnimJoint136.children.append(HAnimJoint138)

HAnimJoint107.children.append(HAnimJoint136)

HAnimJoint99.children.append(HAnimJoint107)
HAnimJoint149 = x3d.HAnimJoint()
HAnimJoint149.DEF = "STD_Joint_l_calcaneocuboid"
HAnimJoint149.bboxCenter = [0,0,0]
HAnimJoint149.bboxDisplay = False
HAnimJoint149.bboxSize = [-1,-1,-1]
HAnimJoint149.name = "l_calcaneocuboid"
HAnimJoint149.visible = True
HAnimSegment150 = x3d.HAnimSegment()
HAnimSegment150.DEF = "STD_Segment_l_calcaneus"
HAnimSegment150.bboxDisplay = False
HAnimSegment150.name = "l_calcaneus"
HAnimSegment150.visible = True

HAnimJoint149.children.append(HAnimSegment150)
HAnimJoint151 = x3d.HAnimJoint()
HAnimJoint151.DEF = "STD_Joint_l_transversetarsal"
HAnimJoint151.bboxCenter = [0,0,0]
HAnimJoint151.bboxDisplay = False
HAnimJoint151.bboxSize = [-1,-1,-1]
HAnimJoint151.name = "l_transversetarsal"
HAnimJoint151.visible = True
HAnimSegment152 = x3d.HAnimSegment()
HAnimSegment152.DEF = "STD_Segment_l_cuboid"
HAnimSegment152.bboxDisplay = False
HAnimSegment152.name = "l_cuboid"
HAnimSegment152.visible = True

HAnimJoint151.children.append(HAnimSegment152)
HAnimJoint153 = x3d.HAnimJoint()
HAnimJoint153.DEF = "STD_Joint_l_tarsometatarsal_4"
HAnimJoint153.bboxCenter = [0,0,0]
HAnimJoint153.bboxDisplay = False
HAnimJoint153.bboxSize = [-1,-1,-1]
HAnimJoint153.name = "l_tarsometatarsal_4"
HAnimJoint153.visible = True
HAnimSegment154 = x3d.HAnimSegment()
HAnimSegment154.DEF = "STD_Segment_l_metatarsal_4"
HAnimSegment154.bboxDisplay = False
HAnimSegment154.name = "l_metatarsal_4"
HAnimSegment154.visible = True

HAnimJoint153.children.append(HAnimSegment154)
HAnimJoint155 = x3d.HAnimJoint()
HAnimJoint155.DEF = "STD_Joint_l_metatarsophalangeal_4"
HAnimJoint155.bboxCenter = [0,0,0]
HAnimJoint155.bboxDisplay = False
HAnimJoint155.bboxSize = [-1,-1,-1]
HAnimJoint155.name = "l_metatarsophalangeal_4"
HAnimJoint155.visible = True
HAnimSegment156 = x3d.HAnimSegment()
HAnimSegment156.DEF = "STD_Segment_l_tarsal_proximal_phalanx_4"
HAnimSegment156.bboxDisplay = False
HAnimSegment156.name = "l_tarsal_proximal_phalanx_4"
HAnimSegment156.visible = True

HAnimJoint155.children.append(HAnimSegment156)
HAnimJoint157 = x3d.HAnimJoint()
HAnimJoint157.DEF = "STD_Joint_l_tarsal_proximal_interphalangeal_4"
HAnimJoint157.bboxCenter = [0,0,0]
HAnimJoint157.bboxDisplay = False
HAnimJoint157.bboxSize = [-1,-1,-1]
HAnimJoint157.name = "l_tarsal_proximal_interphalangeal_4"
HAnimJoint157.visible = True
HAnimSegment158 = x3d.HAnimSegment()
HAnimSegment158.DEF = "STD_Segment_l_tarsal_middle_phalanx_4"
HAnimSegment158.bboxDisplay = False
HAnimSegment158.name = "l_tarsal_middle_phalanx_4"
HAnimSegment158.visible = True

HAnimJoint157.children.append(HAnimSegment158)
HAnimJoint159 = x3d.HAnimJoint()
HAnimJoint159.DEF = "STD_Joint_l_tarsal_distal_interphalangeal_4"
HAnimJoint159.bboxCenter = [0,0,0]
HAnimJoint159.bboxDisplay = False
HAnimJoint159.bboxSize = [-1,-1,-1]
HAnimJoint159.name = "l_tarsal_distal_interphalangeal_4"
HAnimJoint159.visible = True
HAnimSegment160 = x3d.HAnimSegment()
HAnimSegment160.DEF = "STD_Segment_l_tarsal_distal_phalanx_4"
HAnimSegment160.bboxDisplay = False
HAnimSegment160.name = "l_tarsal_distal_phalanx_4"
HAnimSegment160.visible = True
HAnimSite161 = x3d.HAnimSite()
HAnimSite161.DEF = "STD_Site_l_tarsal_distal_phalanx_4_pt"
HAnimSite161.bboxCenter = [0,0,0]
HAnimSite161.bboxDisplay = False
HAnimSite161.bboxSize = [-1,-1,-1]
HAnimSite161.name = "l_tarsal_distal_phalanx_4_pt"
HAnimSite161.visible = True
TouchSensor162 = x3d.TouchSensor()
TouchSensor162.description = "HAnimSite l_tarsal_distal_phalanx_4_pt"

HAnimSite161.children.append(TouchSensor162)
Shape163 = x3d.Shape()
Shape163.USE = "HAnimSiteShape"
Shape163.bboxCenter = [0,0,0]
Shape163.bboxDisplay = False
Shape163.bboxSize = [-1,-1,-1]
Shape163.visible = True

HAnimSite161.children.append(Shape163)

HAnimSegment160.children.append(HAnimSite161)

HAnimJoint159.children.append(HAnimSegment160)

HAnimJoint157.children.append(HAnimJoint159)

HAnimJoint155.children.append(HAnimJoint157)

HAnimJoint153.children.append(HAnimJoint155)

HAnimJoint151.children.append(HAnimJoint153)
HAnimJoint164 = x3d.HAnimJoint()
HAnimJoint164.DEF = "STD_Joint_l_tarsometatarsal_5"
HAnimJoint164.bboxCenter = [0,0,0]
HAnimJoint164.bboxDisplay = False
HAnimJoint164.bboxSize = [-1,-1,-1]
HAnimJoint164.name = "l_tarsometatarsal_5"
HAnimJoint164.visible = True
HAnimSegment165 = x3d.HAnimSegment()
HAnimSegment165.DEF = "STD_Segment_l_metatarsal_5"
HAnimSegment165.bboxDisplay = False
HAnimSegment165.name = "l_metatarsal_5"
HAnimSegment165.visible = True

HAnimJoint164.children.append(HAnimSegment165)
HAnimJoint166 = x3d.HAnimJoint()
HAnimJoint166.DEF = "STD_Joint_l_metatarsophalangeal_5"
HAnimJoint166.bboxCenter = [0,0,0]
HAnimJoint166.bboxDisplay = False
HAnimJoint166.bboxSize = [-1,-1,-1]
HAnimJoint166.name = "l_metatarsophalangeal_5"
HAnimJoint166.visible = True
HAnimSegment167 = x3d.HAnimSegment()
HAnimSegment167.DEF = "STD_Segment_l_tarsal_proximal_phalanx_5"
HAnimSegment167.bboxDisplay = False
HAnimSegment167.name = "l_tarsal_proximal_phalanx_5"
HAnimSegment167.visible = True
HAnimSite168 = x3d.HAnimSite()
HAnimSite168.DEF = "STD_Site_l_metatarsal_phalanx_5_pt"
HAnimSite168.bboxCenter = [0,0,0]
HAnimSite168.bboxDisplay = False
HAnimSite168.bboxSize = [-1,-1,-1]
HAnimSite168.name = "l_metatarsal_phalanx_5_pt"
HAnimSite168.visible = True
TouchSensor169 = x3d.TouchSensor()
TouchSensor169.description = "HAnimSite l_metatarsal_phalanx_5_pt"

HAnimSite168.children.append(TouchSensor169)
Shape170 = x3d.Shape()
Shape170.USE = "HAnimSiteShape"
Shape170.bboxCenter = [0,0,0]
Shape170.bboxDisplay = False
Shape170.bboxSize = [-1,-1,-1]
Shape170.visible = True

HAnimSite168.children.append(Shape170)

HAnimSegment167.children.append(HAnimSite168)

HAnimJoint166.children.append(HAnimSegment167)
HAnimJoint171 = x3d.HAnimJoint()
HAnimJoint171.DEF = "STD_Joint_l_tarsal_proximal_interphalangeal_5"
HAnimJoint171.bboxCenter = [0,0,0]
HAnimJoint171.bboxDisplay = False
HAnimJoint171.bboxSize = [-1,-1,-1]
HAnimJoint171.name = "l_tarsal_proximal_interphalangeal_5"
HAnimJoint171.visible = True
HAnimSegment172 = x3d.HAnimSegment()
HAnimSegment172.DEF = "STD_Segment_l_tarsal_middle_phalanx_5"
HAnimSegment172.bboxDisplay = False
HAnimSegment172.name = "l_tarsal_middle_phalanx_5"
HAnimSegment172.visible = True

HAnimJoint171.children.append(HAnimSegment172)
HAnimJoint173 = x3d.HAnimJoint()
HAnimJoint173.DEF = "STD_Joint_l_tarsal_distal_interphalangeal_5"
HAnimJoint173.bboxCenter = [0,0,0]
HAnimJoint173.bboxDisplay = False
HAnimJoint173.bboxSize = [-1,-1,-1]
HAnimJoint173.name = "l_tarsal_distal_interphalangeal_5"
HAnimJoint173.visible = True
HAnimSegment174 = x3d.HAnimSegment()
HAnimSegment174.DEF = "STD_Segment_l_tarsal_distal_phalanx_5"
HAnimSegment174.bboxDisplay = False
HAnimSegment174.name = "l_tarsal_distal_phalanx_5"
HAnimSegment174.visible = True
HAnimSite175 = x3d.HAnimSite()
HAnimSite175.DEF = "STD_Site_l_tarsal_distal_phalanx_5_pt"
HAnimSite175.bboxCenter = [0,0,0]
HAnimSite175.bboxDisplay = False
HAnimSite175.bboxSize = [-1,-1,-1]
HAnimSite175.name = "l_tarsal_distal_phalanx_5_pt"
HAnimSite175.visible = True
TouchSensor176 = x3d.TouchSensor()
TouchSensor176.description = "HAnimSite l_tarsal_distal_phalanx_5_pt"

HAnimSite175.children.append(TouchSensor176)
Shape177 = x3d.Shape()
Shape177.USE = "HAnimSiteShape"
Shape177.bboxCenter = [0,0,0]
Shape177.bboxDisplay = False
Shape177.bboxSize = [-1,-1,-1]
Shape177.visible = True

HAnimSite175.children.append(Shape177)

HAnimSegment174.children.append(HAnimSite175)

HAnimJoint173.children.append(HAnimSegment174)

HAnimJoint171.children.append(HAnimJoint173)

HAnimJoint166.children.append(HAnimJoint171)

HAnimJoint164.children.append(HAnimJoint166)

HAnimJoint151.children.append(HAnimJoint164)

HAnimJoint149.children.append(HAnimJoint151)

HAnimJoint99.children.append(HAnimJoint149)

HAnimJoint88.children.append(HAnimJoint99)

HAnimJoint74.children.append(HAnimJoint88)

HAnimJoint42.children.append(HAnimJoint74)
HAnimJoint178 = x3d.HAnimJoint()
HAnimJoint178.DEF = "STD_Joint_r_hip"
HAnimJoint178.bboxCenter = [0,0,0]
HAnimJoint178.bboxDisplay = False
HAnimJoint178.bboxSize = [-1,-1,-1]
HAnimJoint178.center = [-0.0950,0.9171,0.0029]
HAnimJoint178.name = "r_hip"
HAnimJoint178.visible = True
HAnimSegment179 = x3d.HAnimSegment()
HAnimSegment179.DEF = "STD_Segment_r_thigh"
HAnimSegment179.bboxDisplay = False
HAnimSegment179.name = "r_thigh"
HAnimSegment179.visible = True
HAnimSite180 = x3d.HAnimSite()
HAnimSite180.DEF = "STD_Site_r_knee_crease_pt"
HAnimSite180.bboxCenter = [0,0,0]
HAnimSite180.bboxDisplay = False
HAnimSite180.bboxSize = [-1,-1,-1]
HAnimSite180.name = "r_knee_crease_pt"
HAnimSite180.translation = [-0.0825,0.4932,-0.0326]
HAnimSite180.visible = True
TouchSensor181 = x3d.TouchSensor()
TouchSensor181.description = "HAnimSite r_knee_crease_pt"

HAnimSite180.children.append(TouchSensor181)
Shape182 = x3d.Shape()
Shape182.USE = "HAnimSiteShape"
Shape182.bboxCenter = [0,0,0]
Shape182.bboxDisplay = False
Shape182.bboxSize = [-1,-1,-1]
Shape182.visible = True

HAnimSite180.children.append(Shape182)

HAnimSegment179.children.append(HAnimSite180)
HAnimSite183 = x3d.HAnimSite()
HAnimSite183.DEF = "STD_Site_r_suprapatella_pt"
HAnimSite183.bboxCenter = [0,0,0]
HAnimSite183.bboxDisplay = False
HAnimSite183.bboxSize = [-1,-1,-1]
HAnimSite183.name = "r_suprapatella_pt"
HAnimSite183.visible = True
TouchSensor184 = x3d.TouchSensor()
TouchSensor184.description = "HAnimSite r_suprapatella_pt"

HAnimSite183.children.append(TouchSensor184)
Shape185 = x3d.Shape()
Shape185.USE = "HAnimSiteShape"
Shape185.bboxCenter = [0,0,0]
Shape185.bboxDisplay = False
Shape185.bboxSize = [-1,-1,-1]
Shape185.visible = True

HAnimSite183.children.append(Shape185)

HAnimSegment179.children.append(HAnimSite183)
HAnimSite186 = x3d.HAnimSite()
HAnimSite186.DEF = "STD_Site_r_femoral_lateral_epicondyles_pt"
HAnimSite186.bboxCenter = [0,0,0]
HAnimSite186.bboxDisplay = False
HAnimSite186.bboxSize = [-1,-1,-1]
HAnimSite186.name = "r_femoral_lateral_epicondyles_pt"
HAnimSite186.translation = [-0.1421,0.4992,0.0310]
HAnimSite186.visible = True
TouchSensor187 = x3d.TouchSensor()
TouchSensor187.description = "HAnimSite r_femoral_lateral_epicondyles_pt"

HAnimSite186.children.append(TouchSensor187)
Shape188 = x3d.Shape()
Shape188.USE = "HAnimSiteShape"
Shape188.bboxCenter = [0,0,0]
Shape188.bboxDisplay = False
Shape188.bboxSize = [-1,-1,-1]
Shape188.visible = True

HAnimSite186.children.append(Shape188)

HAnimSegment179.children.append(HAnimSite186)
HAnimSite189 = x3d.HAnimSite()
HAnimSite189.DEF = "STD_Site_r_femoral_medial_epicondyles_pt"
HAnimSite189.bboxCenter = [0,0,0]
HAnimSite189.bboxDisplay = False
HAnimSite189.bboxSize = [-1,-1,-1]
HAnimSite189.name = "r_femoral_medial_epicondyles_pt"
HAnimSite189.translation = [-0.0221,0.5014,0.0289]
HAnimSite189.visible = True
TouchSensor190 = x3d.TouchSensor()
TouchSensor190.description = "HAnimSite r_femoral_medial_epicondyles_pt"

HAnimSite189.children.append(TouchSensor190)
Shape191 = x3d.Shape()
Shape191.USE = "HAnimSiteShape"
Shape191.bboxCenter = [0,0,0]
Shape191.bboxDisplay = False
Shape191.bboxSize = [-1,-1,-1]
Shape191.visible = True

HAnimSite189.children.append(Shape191)

HAnimSegment179.children.append(HAnimSite189)

HAnimJoint178.children.append(HAnimSegment179)
HAnimJoint192 = x3d.HAnimJoint()
HAnimJoint192.DEF = "STD_Joint_r_knee"
HAnimJoint192.bboxCenter = [0,0,0]
HAnimJoint192.bboxDisplay = False
HAnimJoint192.bboxSize = [-1,-1,-1]
HAnimJoint192.center = [-0.0867,0.4913,0.0318]
HAnimJoint192.name = "r_knee"
HAnimJoint192.visible = True
HAnimSegment193 = x3d.HAnimSegment()
HAnimSegment193.DEF = "STD_Segment_r_calf"
HAnimSegment193.bboxDisplay = False
HAnimSegment193.name = "r_calf"
HAnimSegment193.visible = True
HAnimSite194 = x3d.HAnimSite()
HAnimSite194.DEF = "STD_Site_r_tibiale_pt"
HAnimSite194.bboxCenter = [0,0,0]
HAnimSite194.bboxDisplay = False
HAnimSite194.bboxSize = [-1,-1,-1]
HAnimSite194.name = "r_tibiale_pt"
HAnimSite194.visible = True
TouchSensor195 = x3d.TouchSensor()
TouchSensor195.description = "HAnimSite r_tibiale_pt"

HAnimSite194.children.append(TouchSensor195)
Shape196 = x3d.Shape()
Shape196.USE = "HAnimSiteShape"
Shape196.bboxCenter = [0,0,0]
Shape196.bboxDisplay = False
Shape196.bboxSize = [-1,-1,-1]
Shape196.visible = True

HAnimSite194.children.append(Shape196)

HAnimSegment193.children.append(HAnimSite194)
HAnimSite197 = x3d.HAnimSite()
HAnimSite197.DEF = "STD_Site_r_medial_malleolus_pt"
HAnimSite197.bboxCenter = [0,0,0]
HAnimSite197.bboxDisplay = False
HAnimSite197.bboxSize = [-1,-1,-1]
HAnimSite197.name = "r_medial_malleolus_pt"
HAnimSite197.translation = [-0.0591,0.0760,-0.0928]
HAnimSite197.visible = True
TouchSensor198 = x3d.TouchSensor()
TouchSensor198.description = "HAnimSite r_medial_malleolus_pt"

HAnimSite197.children.append(TouchSensor198)
Shape199 = x3d.Shape()
Shape199.USE = "HAnimSiteShape"
Shape199.bboxCenter = [0,0,0]
Shape199.bboxDisplay = False
Shape199.bboxSize = [-1,-1,-1]
Shape199.visible = True

HAnimSite197.children.append(Shape199)

HAnimSegment193.children.append(HAnimSite197)
HAnimSite200 = x3d.HAnimSite()
HAnimSite200.DEF = "STD_Site_r_lateral_malleolus_pt"
HAnimSite200.bboxCenter = [0,0,0]
HAnimSite200.bboxDisplay = False
HAnimSite200.bboxSize = [-1,-1,-1]
HAnimSite200.name = "r_lateral_malleolus_pt"
HAnimSite200.translation = [-0.1006,0.0658,-0.1075]
HAnimSite200.visible = True
TouchSensor201 = x3d.TouchSensor()
TouchSensor201.description = "HAnimSite r_lateral_malleolus_pt"

HAnimSite200.children.append(TouchSensor201)
Shape202 = x3d.Shape()
Shape202.USE = "HAnimSiteShape"
Shape202.bboxCenter = [0,0,0]
Shape202.bboxDisplay = False
Shape202.bboxSize = [-1,-1,-1]
Shape202.visible = True

HAnimSite200.children.append(Shape202)

HAnimSegment193.children.append(HAnimSite200)

HAnimJoint192.children.append(HAnimSegment193)
HAnimJoint203 = x3d.HAnimJoint()
HAnimJoint203.DEF = "STD_Joint_r_talocrural"
HAnimJoint203.bboxCenter = [0,0,0]
HAnimJoint203.bboxDisplay = False
HAnimJoint203.bboxSize = [-1,-1,-1]
HAnimJoint203.center = [-0.0801,0.0712,-0.0766]
HAnimJoint203.name = "r_talocrural"
HAnimJoint203.visible = True
HAnimSegment204 = x3d.HAnimSegment()
HAnimSegment204.DEF = "STD_Segment_r_talus"
HAnimSegment204.bboxDisplay = False
HAnimSegment204.name = "r_talus"
HAnimSegment204.visible = True
HAnimSite205 = x3d.HAnimSite()
HAnimSite205.DEF = "STD_Site_r_calcaneus_posterior_pt"
HAnimSite205.bboxCenter = [0,0,0]
HAnimSite205.bboxDisplay = False
HAnimSite205.bboxSize = [-1,-1,-1]
HAnimSite205.name = "r_calcaneus_posterior_pt"
HAnimSite205.translation = [-0.0692,0.0297,-0.1221]
HAnimSite205.visible = True
TouchSensor206 = x3d.TouchSensor()
TouchSensor206.description = "HAnimSite r_calcaneus_posterior_pt"

HAnimSite205.children.append(TouchSensor206)
Shape207 = x3d.Shape()
Shape207.USE = "HAnimSiteShape"
Shape207.bboxCenter = [0,0,0]
Shape207.bboxDisplay = False
Shape207.bboxSize = [-1,-1,-1]
Shape207.visible = True

HAnimSite205.children.append(Shape207)

HAnimSegment204.children.append(HAnimSite205)
HAnimSite208 = x3d.HAnimSite()
HAnimSite208.DEF = "STD_Site_r_sphyrion_pt"
HAnimSite208.bboxCenter = [0,0,0]
HAnimSite208.bboxDisplay = False
HAnimSite208.bboxSize = [-1,-1,-1]
HAnimSite208.name = "r_sphyrion_pt"
HAnimSite208.translation = [-0.0603,0.0610,-0.1002]
HAnimSite208.visible = True
TouchSensor209 = x3d.TouchSensor()
TouchSensor209.description = "HAnimSite r_sphyrion_pt"

HAnimSite208.children.append(TouchSensor209)
Shape210 = x3d.Shape()
Shape210.USE = "HAnimSiteShape"
Shape210.bboxCenter = [0,0,0]
Shape210.bboxDisplay = False
Shape210.bboxSize = [-1,-1,-1]
Shape210.visible = True

HAnimSite208.children.append(Shape210)

HAnimSegment204.children.append(HAnimSite208)

HAnimJoint203.children.append(HAnimSegment204)
HAnimJoint211 = x3d.HAnimJoint()
HAnimJoint211.DEF = "STD_Joint_r_talocalcaneonavicular"
HAnimJoint211.bboxCenter = [0,0,0]
HAnimJoint211.bboxDisplay = False
HAnimJoint211.bboxSize = [-1,-1,-1]
HAnimJoint211.name = "r_talocalcaneonavicular"
HAnimJoint211.visible = True
HAnimSegment212 = x3d.HAnimSegment()
HAnimSegment212.DEF = "STD_Segment_r_navicular"
HAnimSegment212.bboxDisplay = False
HAnimSegment212.name = "r_navicular"
HAnimSegment212.visible = True

HAnimJoint211.children.append(HAnimSegment212)
HAnimJoint213 = x3d.HAnimJoint()
HAnimJoint213.DEF = "STD_Joint_r_cuneonavicular_1"
HAnimJoint213.bboxCenter = [0,0,0]
HAnimJoint213.bboxDisplay = False
HAnimJoint213.bboxSize = [-1,-1,-1]
HAnimJoint213.name = "r_cuneonavicular_1"
HAnimJoint213.visible = True
HAnimSegment214 = x3d.HAnimSegment()
HAnimSegment214.DEF = "STD_Segment_r_cuneiform_1"
HAnimSegment214.bboxDisplay = False
HAnimSegment214.name = "r_cuneiform_1"
HAnimSegment214.visible = True

HAnimJoint213.children.append(HAnimSegment214)
HAnimJoint215 = x3d.HAnimJoint()
HAnimJoint215.DEF = "STD_Joint_r_tarsometatarsal_1"
HAnimJoint215.bboxCenter = [0,0,0]
HAnimJoint215.bboxDisplay = False
HAnimJoint215.bboxSize = [-1,-1,-1]
HAnimJoint215.name = "r_tarsometatarsal_1"
HAnimJoint215.visible = True
HAnimSegment216 = x3d.HAnimSegment()
HAnimSegment216.DEF = "STD_Segment_r_metatarsal_1"
HAnimSegment216.bboxDisplay = False
HAnimSegment216.name = "r_metatarsal_1"
HAnimSegment216.visible = True

HAnimJoint215.children.append(HAnimSegment216)
HAnimJoint217 = x3d.HAnimJoint()
HAnimJoint217.DEF = "STD_Joint_r_metatarsophalangeal_1"
HAnimJoint217.bboxCenter = [0,0,0]
HAnimJoint217.bboxDisplay = False
HAnimJoint217.bboxSize = [-1,-1,-1]
HAnimJoint217.name = "r_metatarsophalangeal_1"
HAnimJoint217.visible = True
HAnimSegment218 = x3d.HAnimSegment()
HAnimSegment218.DEF = "STD_Segment_r_tarsal_proximal_phalanx_1"
HAnimSegment218.bboxDisplay = False
HAnimSegment218.name = "r_tarsal_proximal_phalanx_1"
HAnimSegment218.visible = True
HAnimSite219 = x3d.HAnimSite()
HAnimSite219.DEF = "STD_Site_r_metatarsal_phalanx_1_pt"
HAnimSite219.bboxCenter = [0,0,0]
HAnimSite219.bboxDisplay = False
HAnimSite219.bboxSize = [-1,-1,-1]
HAnimSite219.name = "r_metatarsal_phalanx_1_pt"
HAnimSite219.visible = True
TouchSensor220 = x3d.TouchSensor()
TouchSensor220.description = "HAnimSite r_metatarsal_phalanx_1_pt"

HAnimSite219.children.append(TouchSensor220)
Shape221 = x3d.Shape()
Shape221.USE = "HAnimSiteShape"
Shape221.bboxCenter = [0,0,0]
Shape221.bboxDisplay = False
Shape221.bboxSize = [-1,-1,-1]
Shape221.visible = True

HAnimSite219.children.append(Shape221)

HAnimSegment218.children.append(HAnimSite219)

HAnimJoint217.children.append(HAnimSegment218)
HAnimJoint222 = x3d.HAnimJoint()
HAnimJoint222.DEF = "STD_Joint_r_tarsal_interphalangeal_1"
HAnimJoint222.bboxCenter = [0,0,0]
HAnimJoint222.bboxDisplay = False
HAnimJoint222.bboxSize = [-1,-1,-1]
HAnimJoint222.name = "r_tarsal_interphalangeal_1"
HAnimJoint222.visible = True
HAnimSegment223 = x3d.HAnimSegment()
HAnimSegment223.DEF = "STD_Segment_r_tarsal_distal_phalanx_1"
HAnimSegment223.bboxDisplay = False
HAnimSegment223.name = "r_tarsal_distal_phalanx_1"
HAnimSegment223.visible = True
HAnimSite224 = x3d.HAnimSite()
HAnimSite224.DEF = "STD_Site_r_tarsal_distal_phalanx_1_pt"
HAnimSite224.bboxCenter = [0,0,0]
HAnimSite224.bboxDisplay = False
HAnimSite224.bboxSize = [-1,-1,-1]
HAnimSite224.name = "r_tarsal_distal_phalanx_1_pt"
HAnimSite224.visible = True
TouchSensor225 = x3d.TouchSensor()
TouchSensor225.description = "HAnimSite r_tarsal_distal_phalanx_1_pt"

HAnimSite224.children.append(TouchSensor225)
Shape226 = x3d.Shape()
Shape226.USE = "HAnimSiteShape"
Shape226.bboxCenter = [0,0,0]
Shape226.bboxDisplay = False
Shape226.bboxSize = [-1,-1,-1]
Shape226.visible = True

HAnimSite224.children.append(Shape226)

HAnimSegment223.children.append(HAnimSite224)

HAnimJoint222.children.append(HAnimSegment223)

HAnimJoint217.children.append(HAnimJoint222)

HAnimJoint215.children.append(HAnimJoint217)

HAnimJoint213.children.append(HAnimJoint215)

HAnimJoint211.children.append(HAnimJoint213)
HAnimJoint227 = x3d.HAnimJoint()
HAnimJoint227.DEF = "STD_Joint_r_cuneonavicular_2"
HAnimJoint227.bboxCenter = [0,0,0]
HAnimJoint227.bboxDisplay = False
HAnimJoint227.bboxSize = [-1,-1,-1]
HAnimJoint227.name = "r_cuneonavicular_2"
HAnimJoint227.visible = True
HAnimSegment228 = x3d.HAnimSegment()
HAnimSegment228.DEF = "STD_Segment_r_cuneiform_2"
HAnimSegment228.bboxDisplay = False
HAnimSegment228.name = "r_cuneiform_2"
HAnimSegment228.visible = True

HAnimJoint227.children.append(HAnimSegment228)
HAnimJoint229 = x3d.HAnimJoint()
HAnimJoint229.DEF = "STD_Joint_r_tarsometatarsal_2"
HAnimJoint229.bboxCenter = [0,0,0]
HAnimJoint229.bboxDisplay = False
HAnimJoint229.bboxSize = [-1,-1,-1]
HAnimJoint229.name = "r_tarsometatarsal_2"
HAnimJoint229.visible = True
HAnimSegment230 = x3d.HAnimSegment()
HAnimSegment230.DEF = "STD_Segment_r_metatarsal_2"
HAnimSegment230.bboxDisplay = False
HAnimSegment230.name = "r_metatarsal_2"
HAnimSegment230.visible = True

HAnimJoint229.children.append(HAnimSegment230)
HAnimJoint231 = x3d.HAnimJoint()
HAnimJoint231.DEF = "STD_Joint_r_metatarsophalangeal_2"
HAnimJoint231.bboxCenter = [0,0,0]
HAnimJoint231.bboxDisplay = False
HAnimJoint231.bboxSize = [-1,-1,-1]
HAnimJoint231.name = "r_metatarsophalangeal_2"
HAnimJoint231.visible = True
HAnimSegment232 = x3d.HAnimSegment()
HAnimSegment232.DEF = "STD_Segment_r_tarsal_proximal_phalanx_2"
HAnimSegment232.bboxDisplay = False
HAnimSegment232.name = "r_tarsal_proximal_phalanx_2"
HAnimSegment232.visible = True

HAnimJoint231.children.append(HAnimSegment232)
HAnimJoint233 = x3d.HAnimJoint()
HAnimJoint233.DEF = "STD_Joint_r_tarsal_proximal_interphalangeal_2"
HAnimJoint233.bboxCenter = [0,0,0]
HAnimJoint233.bboxDisplay = False
HAnimJoint233.bboxSize = [-1,-1,-1]
HAnimJoint233.name = "r_tarsal_proximal_interphalangeal_2"
HAnimJoint233.visible = True
HAnimSegment234 = x3d.HAnimSegment()
HAnimSegment234.DEF = "STD_Segment_r_tarsal_middle_phalanx_2"
HAnimSegment234.bboxDisplay = False
HAnimSegment234.name = "r_tarsal_middle_phalanx_2"
HAnimSegment234.visible = True

HAnimJoint233.children.append(HAnimSegment234)
HAnimJoint235 = x3d.HAnimJoint()
HAnimJoint235.DEF = "STD_Joint_r_tarsal_distal_interphalangeal_2"
HAnimJoint235.bboxCenter = [0,0,0]
HAnimJoint235.bboxDisplay = False
HAnimJoint235.bboxSize = [-1,-1,-1]
HAnimJoint235.name = "r_tarsal_distal_interphalangeal_2"
HAnimJoint235.visible = True
HAnimSegment236 = x3d.HAnimSegment()
HAnimSegment236.DEF = "STD_Segment_r_tarsal_distal_phalanx_2"
HAnimSegment236.bboxDisplay = False
HAnimSegment236.name = "r_tarsal_distal_phalanx_2"
HAnimSegment236.visible = True
HAnimSite237 = x3d.HAnimSite()
HAnimSite237.DEF = "STD_Site_r_tarsal_distal_phalanx_2_pt"
HAnimSite237.bboxCenter = [0,0,0]
HAnimSite237.bboxDisplay = False
HAnimSite237.bboxSize = [-1,-1,-1]
HAnimSite237.name = "r_tarsal_distal_phalanx_2_pt"
HAnimSite237.translation = [-0.0883,0.0134,0.1383]
HAnimSite237.visible = True
TouchSensor238 = x3d.TouchSensor()
TouchSensor238.description = "HAnimSite r_tarsal_distal_phalanx_2_pt"

HAnimSite237.children.append(TouchSensor238)
Shape239 = x3d.Shape()
Shape239.USE = "HAnimSiteShape"
Shape239.bboxCenter = [0,0,0]
Shape239.bboxDisplay = False
Shape239.bboxSize = [-1,-1,-1]
Shape239.visible = True

HAnimSite237.children.append(Shape239)

HAnimSegment236.children.append(HAnimSite237)

HAnimJoint235.children.append(HAnimSegment236)

HAnimJoint233.children.append(HAnimJoint235)

HAnimJoint231.children.append(HAnimJoint233)

HAnimJoint229.children.append(HAnimJoint231)

HAnimJoint227.children.append(HAnimJoint229)

HAnimJoint211.children.append(HAnimJoint227)
HAnimJoint240 = x3d.HAnimJoint()
HAnimJoint240.DEF = "STD_Joint_r_cuneonavicular_3"
HAnimJoint240.bboxCenter = [0,0,0]
HAnimJoint240.bboxDisplay = False
HAnimJoint240.bboxSize = [-1,-1,-1]
HAnimJoint240.name = "r_cuneonavicular_3"
HAnimJoint240.visible = True
HAnimSegment241 = x3d.HAnimSegment()
HAnimSegment241.DEF = "STD_Segment_r_cuneiform_3"
HAnimSegment241.bboxDisplay = False
HAnimSegment241.name = "r_cuneiform_3"
HAnimSegment241.visible = True

HAnimJoint240.children.append(HAnimSegment241)
HAnimJoint242 = x3d.HAnimJoint()
HAnimJoint242.DEF = "STD_Joint_r_tarsometatarsal_3"
HAnimJoint242.bboxCenter = [0,0,0]
HAnimJoint242.bboxDisplay = False
HAnimJoint242.bboxSize = [-1,-1,-1]
HAnimJoint242.name = "r_tarsometatarsal_3"
HAnimJoint242.visible = True
HAnimSegment243 = x3d.HAnimSegment()
HAnimSegment243.DEF = "STD_Segment_r_metatarsal_3"
HAnimSegment243.bboxDisplay = False
HAnimSegment243.name = "r_metatarsal_3"
HAnimSegment243.visible = True

HAnimJoint242.children.append(HAnimSegment243)
HAnimJoint244 = x3d.HAnimJoint()
HAnimJoint244.DEF = "STD_Joint_r_metatarsophalangeal_3"
HAnimJoint244.bboxCenter = [0,0,0]
HAnimJoint244.bboxDisplay = False
HAnimJoint244.bboxSize = [-1,-1,-1]
HAnimJoint244.name = "r_metatarsophalangeal_3"
HAnimJoint244.visible = True
HAnimSegment245 = x3d.HAnimSegment()
HAnimSegment245.DEF = "STD_Segment_r_tarsal_proximal_phalanx_3"
HAnimSegment245.bboxDisplay = False
HAnimSegment245.name = "r_tarsal_proximal_phalanx_3"
HAnimSegment245.visible = True

HAnimJoint244.children.append(HAnimSegment245)
HAnimJoint246 = x3d.HAnimJoint()
HAnimJoint246.DEF = "STD_Joint_r_tarsal_proximal_interphalangeal_3"
HAnimJoint246.bboxCenter = [0,0,0]
HAnimJoint246.bboxDisplay = False
HAnimJoint246.bboxSize = [-1,-1,-1]
HAnimJoint246.name = "r_tarsal_proximal_interphalangeal_3"
HAnimJoint246.visible = True
HAnimSegment247 = x3d.HAnimSegment()
HAnimSegment247.DEF = "STD_Segment_r_tarsal_middle_phalanx_3"
HAnimSegment247.bboxDisplay = False
HAnimSegment247.name = "r_tarsal_middle_phalanx_3"
HAnimSegment247.visible = True

HAnimJoint246.children.append(HAnimSegment247)
HAnimJoint248 = x3d.HAnimJoint()
HAnimJoint248.DEF = "STD_Joint_r_tarsal_distal_interphalangeal_3"
HAnimJoint248.bboxCenter = [0,0,0]
HAnimJoint248.bboxDisplay = False
HAnimJoint248.bboxSize = [-1,-1,-1]
HAnimJoint248.name = "r_tarsal_distal_interphalangeal_3"
HAnimJoint248.visible = True
HAnimSegment249 = x3d.HAnimSegment()
HAnimSegment249.DEF = "STD_Segment_r_tarsal_distal_phalanx_3"
HAnimSegment249.bboxDisplay = False
HAnimSegment249.name = "r_tarsal_distal_phalanx_3"
HAnimSegment249.visible = True
HAnimSite250 = x3d.HAnimSite()
HAnimSite250.DEF = "STD_Site_r_tarsal_distal_phalanx_3_pt"
HAnimSite250.bboxCenter = [0,0,0]
HAnimSite250.bboxDisplay = False
HAnimSite250.bboxSize = [-1,-1,-1]
HAnimSite250.name = "r_tarsal_distal_phalanx_3_pt"
HAnimSite250.visible = True
TouchSensor251 = x3d.TouchSensor()
TouchSensor251.description = "HAnimSite r_tarsal_distal_phalanx_3_pt"

HAnimSite250.children.append(TouchSensor251)
Shape252 = x3d.Shape()
Shape252.USE = "HAnimSiteShape"
Shape252.bboxCenter = [0,0,0]
Shape252.bboxDisplay = False
Shape252.bboxSize = [-1,-1,-1]
Shape252.visible = True

HAnimSite250.children.append(Shape252)

HAnimSegment249.children.append(HAnimSite250)

HAnimJoint248.children.append(HAnimSegment249)

HAnimJoint246.children.append(HAnimJoint248)

HAnimJoint244.children.append(HAnimJoint246)

HAnimJoint242.children.append(HAnimJoint244)

HAnimJoint240.children.append(HAnimJoint242)

HAnimJoint211.children.append(HAnimJoint240)

HAnimJoint203.children.append(HAnimJoint211)
HAnimJoint253 = x3d.HAnimJoint()
HAnimJoint253.DEF = "STD_Joint_r_calcaneocuboid"
HAnimJoint253.bboxCenter = [0,0,0]
HAnimJoint253.bboxDisplay = False
HAnimJoint253.bboxSize = [-1,-1,-1]
HAnimJoint253.name = "r_calcaneocuboid"
HAnimJoint253.visible = True
HAnimSegment254 = x3d.HAnimSegment()
HAnimSegment254.DEF = "STD_Segment_r_calcaneus"
HAnimSegment254.bboxDisplay = False
HAnimSegment254.name = "r_calcaneus"
HAnimSegment254.visible = True

HAnimJoint253.children.append(HAnimSegment254)
HAnimJoint255 = x3d.HAnimJoint()
HAnimJoint255.DEF = "STD_Joint_r_transversetarsal"
HAnimJoint255.bboxCenter = [0,0,0]
HAnimJoint255.bboxDisplay = False
HAnimJoint255.bboxSize = [-1,-1,-1]
HAnimJoint255.name = "r_transversetarsal"
HAnimJoint255.visible = True
HAnimSegment256 = x3d.HAnimSegment()
HAnimSegment256.DEF = "STD_Segment_r_cuboid"
HAnimSegment256.bboxDisplay = False
HAnimSegment256.name = "r_cuboid"
HAnimSegment256.visible = True

HAnimJoint255.children.append(HAnimSegment256)
HAnimJoint257 = x3d.HAnimJoint()
HAnimJoint257.DEF = "STD_Joint_r_tarsometatarsal_4"
HAnimJoint257.bboxCenter = [0,0,0]
HAnimJoint257.bboxDisplay = False
HAnimJoint257.bboxSize = [-1,-1,-1]
HAnimJoint257.name = "r_tarsometatarsal_4"
HAnimJoint257.visible = True
HAnimSegment258 = x3d.HAnimSegment()
HAnimSegment258.DEF = "STD_Segment_r_metatarsal_4"
HAnimSegment258.bboxDisplay = False
HAnimSegment258.name = "r_metatarsal_4"
HAnimSegment258.visible = True

HAnimJoint257.children.append(HAnimSegment258)
HAnimJoint259 = x3d.HAnimJoint()
HAnimJoint259.DEF = "STD_Joint_r_metatarsophalangeal_4"
HAnimJoint259.bboxCenter = [0,0,0]
HAnimJoint259.bboxDisplay = False
HAnimJoint259.bboxSize = [-1,-1,-1]
HAnimJoint259.name = "r_metatarsophalangeal_4"
HAnimJoint259.visible = True
HAnimSegment260 = x3d.HAnimSegment()
HAnimSegment260.DEF = "STD_Segment_r_tarsal_proximal_phalanx_4"
HAnimSegment260.bboxDisplay = False
HAnimSegment260.name = "r_tarsal_proximal_phalanx_4"
HAnimSegment260.visible = True

HAnimJoint259.children.append(HAnimSegment260)
HAnimJoint261 = x3d.HAnimJoint()
HAnimJoint261.DEF = "STD_Joint_r_tarsal_proximal_interphalangeal_4"
HAnimJoint261.bboxCenter = [0,0,0]
HAnimJoint261.bboxDisplay = False
HAnimJoint261.bboxSize = [-1,-1,-1]
HAnimJoint261.name = "r_tarsal_proximal_interphalangeal_4"
HAnimJoint261.visible = True
HAnimSegment262 = x3d.HAnimSegment()
HAnimSegment262.DEF = "STD_Segment_r_tarsal_middle_phalanx_4"
HAnimSegment262.bboxDisplay = False
HAnimSegment262.name = "r_tarsal_middle_phalanx_4"
HAnimSegment262.visible = True

HAnimJoint261.children.append(HAnimSegment262)
HAnimJoint263 = x3d.HAnimJoint()
HAnimJoint263.DEF = "STD_Joint_r_tarsal_distal_interphalangeal_4"
HAnimJoint263.bboxCenter = [0,0,0]
HAnimJoint263.bboxDisplay = False
HAnimJoint263.bboxSize = [-1,-1,-1]
HAnimJoint263.name = "r_tarsal_distal_interphalangeal_4"
HAnimJoint263.visible = True
HAnimSegment264 = x3d.HAnimSegment()
HAnimSegment264.DEF = "STD_Segment_r_tarsal_distal_phalanx_4"
HAnimSegment264.bboxDisplay = False
HAnimSegment264.name = "r_tarsal_distal_phalanx_4"
HAnimSegment264.visible = True
HAnimSite265 = x3d.HAnimSite()
HAnimSite265.DEF = "STD_Site_r_tarsal_distal_phalanx_4_pt"
HAnimSite265.bboxCenter = [0,0,0]
HAnimSite265.bboxDisplay = False
HAnimSite265.bboxSize = [-1,-1,-1]
HAnimSite265.name = "r_tarsal_distal_phalanx_4_pt"
HAnimSite265.visible = True
TouchSensor266 = x3d.TouchSensor()
TouchSensor266.description = "HAnimSite r_tarsal_distal_phalanx_4_pt"

HAnimSite265.children.append(TouchSensor266)
Shape267 = x3d.Shape()
Shape267.USE = "HAnimSiteShape"
Shape267.bboxCenter = [0,0,0]
Shape267.bboxDisplay = False
Shape267.bboxSize = [-1,-1,-1]
Shape267.visible = True

HAnimSite265.children.append(Shape267)

HAnimSegment264.children.append(HAnimSite265)

HAnimJoint263.children.append(HAnimSegment264)

HAnimJoint261.children.append(HAnimJoint263)

HAnimJoint259.children.append(HAnimJoint261)

HAnimJoint257.children.append(HAnimJoint259)

HAnimJoint255.children.append(HAnimJoint257)
HAnimJoint268 = x3d.HAnimJoint()
HAnimJoint268.DEF = "STD_Joint_r_tarsometatarsal_5"
HAnimJoint268.bboxCenter = [0,0,0]
HAnimJoint268.bboxDisplay = False
HAnimJoint268.bboxSize = [-1,-1,-1]
HAnimJoint268.name = "r_tarsometatarsal_5"
HAnimJoint268.visible = True
HAnimSegment269 = x3d.HAnimSegment()
HAnimSegment269.DEF = "STD_Segment_r_metatarsal_5"
HAnimSegment269.bboxDisplay = False
HAnimSegment269.name = "r_metatarsal_5"
HAnimSegment269.visible = True

HAnimJoint268.children.append(HAnimSegment269)
HAnimJoint270 = x3d.HAnimJoint()
HAnimJoint270.DEF = "STD_Joint_r_metatarsophalangeal_5"
HAnimJoint270.bboxCenter = [0,0,0]
HAnimJoint270.bboxDisplay = False
HAnimJoint270.bboxSize = [-1,-1,-1]
HAnimJoint270.name = "r_metatarsophalangeal_5"
HAnimJoint270.visible = True
HAnimSegment271 = x3d.HAnimSegment()
HAnimSegment271.DEF = "STD_Segment_r_tarsal_proximal_phalanx_5"
HAnimSegment271.bboxDisplay = False
HAnimSegment271.name = "r_tarsal_proximal_phalanx_5"
HAnimSegment271.visible = True
HAnimSite272 = x3d.HAnimSite()
HAnimSite272.DEF = "STD_Site_r_metatarsal_phalanx_5_pt"
HAnimSite272.bboxCenter = [0,0,0]
HAnimSite272.bboxDisplay = False
HAnimSite272.bboxSize = [-1,-1,-1]
HAnimSite272.name = "r_metatarsal_phalanx_5_pt"
HAnimSite272.visible = True
TouchSensor273 = x3d.TouchSensor()
TouchSensor273.description = "HAnimSite r_metatarsal_phalanx_5_pt"

HAnimSite272.children.append(TouchSensor273)
Shape274 = x3d.Shape()
Shape274.USE = "HAnimSiteShape"
Shape274.bboxCenter = [0,0,0]
Shape274.bboxDisplay = False
Shape274.bboxSize = [-1,-1,-1]
Shape274.visible = True

HAnimSite272.children.append(Shape274)

HAnimSegment271.children.append(HAnimSite272)

HAnimJoint270.children.append(HAnimSegment271)
HAnimJoint275 = x3d.HAnimJoint()
HAnimJoint275.DEF = "STD_Joint_r_tarsal_proximal_interphalangeal_5"
HAnimJoint275.bboxCenter = [0,0,0]
HAnimJoint275.bboxDisplay = False
HAnimJoint275.bboxSize = [-1,-1,-1]
HAnimJoint275.name = "r_tarsal_proximal_interphalangeal_5"
HAnimJoint275.visible = True
HAnimSegment276 = x3d.HAnimSegment()
HAnimSegment276.DEF = "STD_Segment_r_tarsal_middle_phalanx_5"
HAnimSegment276.bboxDisplay = False
HAnimSegment276.name = "r_tarsal_middle_phalanx_5"
HAnimSegment276.visible = True

HAnimJoint275.children.append(HAnimSegment276)
HAnimJoint277 = x3d.HAnimJoint()
HAnimJoint277.DEF = "STD_Joint_r_tarsal_distal_interphalangeal_5"
HAnimJoint277.bboxCenter = [0,0,0]
HAnimJoint277.bboxDisplay = False
HAnimJoint277.bboxSize = [-1,-1,-1]
HAnimJoint277.name = "r_tarsal_distal_interphalangeal_5"
HAnimJoint277.visible = True
HAnimSegment278 = x3d.HAnimSegment()
HAnimSegment278.DEF = "STD_Segment_r_tarsal_distal_phalanx_5"
HAnimSegment278.bboxDisplay = False
HAnimSegment278.name = "r_tarsal_distal_phalanx_5"
HAnimSegment278.visible = True
HAnimSite279 = x3d.HAnimSite()
HAnimSite279.DEF = "STD_Site_r_tarsal_distal_phalanx_5_pt"
HAnimSite279.bboxCenter = [0,0,0]
HAnimSite279.bboxDisplay = False
HAnimSite279.bboxSize = [-1,-1,-1]
HAnimSite279.name = "r_tarsal_distal_phalanx_5_pt"
HAnimSite279.visible = True
TouchSensor280 = x3d.TouchSensor()
TouchSensor280.description = "HAnimSite r_tarsal_distal_phalanx_5_pt"

HAnimSite279.children.append(TouchSensor280)
Shape281 = x3d.Shape()
Shape281.USE = "HAnimSiteShape"
Shape281.bboxCenter = [0,0,0]
Shape281.bboxDisplay = False
Shape281.bboxSize = [-1,-1,-1]
Shape281.visible = True

HAnimSite279.children.append(Shape281)

HAnimSegment278.children.append(HAnimSite279)

HAnimJoint277.children.append(HAnimSegment278)

HAnimJoint275.children.append(HAnimJoint277)

HAnimJoint270.children.append(HAnimJoint275)

HAnimJoint268.children.append(HAnimJoint270)

HAnimJoint255.children.append(HAnimJoint268)

HAnimJoint253.children.append(HAnimJoint255)

HAnimJoint203.children.append(HAnimJoint253)

HAnimJoint192.children.append(HAnimJoint203)

HAnimJoint178.children.append(HAnimJoint192)

HAnimJoint42.children.append(HAnimJoint178)

HAnimJoint17.children.append(HAnimJoint42)
HAnimJoint282 = x3d.HAnimJoint()
HAnimJoint282.DEF = "STD_Joint_vl5"
HAnimJoint282.bboxCenter = [0,0,0]
HAnimJoint282.bboxDisplay = False
HAnimJoint282.bboxSize = [-1,-1,-1]
HAnimJoint282.center = [0.0028,1.0568,-0.0776]
HAnimJoint282.name = "vl5"
HAnimJoint282.visible = True
HAnimSegment283 = x3d.HAnimSegment()
HAnimSegment283.DEF = "STD_Segment_l5"
HAnimSegment283.bboxDisplay = False
HAnimSegment283.name = "l5"
HAnimSegment283.visible = True
HAnimSite284 = x3d.HAnimSite()
HAnimSite284.DEF = "STD_Site_waist_preferred_posterior_pt"
HAnimSite284.bboxCenter = [0,0,0]
HAnimSite284.bboxDisplay = False
HAnimSite284.bboxSize = [-1,-1,-1]
HAnimSite284.name = "waist_preferred_posterior_pt"
HAnimSite284.translation = [0.2900,1.0915,-0.1091]
HAnimSite284.visible = True
TouchSensor285 = x3d.TouchSensor()
TouchSensor285.description = "HAnimSite waist_preferred_posterior_pt"

HAnimSite284.children.append(TouchSensor285)
Shape286 = x3d.Shape()
Shape286.USE = "HAnimSiteShape"
Shape286.bboxCenter = [0,0,0]
Shape286.bboxDisplay = False
Shape286.bboxSize = [-1,-1,-1]
Shape286.visible = True

HAnimSite284.children.append(Shape286)

HAnimSegment283.children.append(HAnimSite284)
HAnimSite287 = x3d.HAnimSite()
HAnimSite287.DEF = "STD_Site_navel_pt"
HAnimSite287.bboxCenter = [0,0,0]
HAnimSite287.bboxDisplay = False
HAnimSite287.bboxSize = [-1,-1,-1]
HAnimSite287.name = "navel_pt"
HAnimSite287.translation = [0.0069,1.0966,0.1017]
HAnimSite287.visible = True
TouchSensor288 = x3d.TouchSensor()
TouchSensor288.description = "HAnimSite navel_pt"

HAnimSite287.children.append(TouchSensor288)
Shape289 = x3d.Shape()
Shape289.USE = "HAnimSiteShape"
Shape289.bboxCenter = [0,0,0]
Shape289.bboxDisplay = False
Shape289.bboxSize = [-1,-1,-1]
Shape289.visible = True

HAnimSite287.children.append(Shape289)

HAnimSegment283.children.append(HAnimSite287)
HAnimSite290 = x3d.HAnimSite()
HAnimSite290.DEF = "STD_Site_waist_preferred_anterior_pt"
HAnimSite290.bboxCenter = [0,0,0]
HAnimSite290.bboxDisplay = False
HAnimSite290.bboxSize = [-1,-1,-1]
HAnimSite290.name = "waist_preferred_anterior_pt"
HAnimSite290.visible = True
TouchSensor291 = x3d.TouchSensor()
TouchSensor291.description = "HAnimSite waist_preferred_anterior_pt"

HAnimSite290.children.append(TouchSensor291)
Shape292 = x3d.Shape()
Shape292.USE = "HAnimSiteShape"
Shape292.bboxCenter = [0,0,0]
Shape292.bboxDisplay = False
Shape292.bboxSize = [-1,-1,-1]
Shape292.visible = True

HAnimSite290.children.append(Shape292)

HAnimSegment283.children.append(HAnimSite290)

HAnimJoint282.children.append(HAnimSegment283)
HAnimJoint293 = x3d.HAnimJoint()
HAnimJoint293.DEF = "STD_Joint_vl4"
HAnimJoint293.bboxCenter = [0,0,0]
HAnimJoint293.bboxDisplay = False
HAnimJoint293.bboxSize = [-1,-1,-1]
HAnimJoint293.center = [0.0035,1.0925,-0.0787]
HAnimJoint293.name = "vl4"
HAnimJoint293.visible = True
HAnimSegment294 = x3d.HAnimSegment()
HAnimSegment294.DEF = "STD_Segment_l4"
HAnimSegment294.bboxDisplay = False
HAnimSegment294.name = "l4"
HAnimSegment294.visible = True

HAnimJoint293.children.append(HAnimSegment294)
HAnimJoint295 = x3d.HAnimJoint()
HAnimJoint295.DEF = "STD_Joint_vl3"
HAnimJoint295.bboxCenter = [0,0,0]
HAnimJoint295.bboxDisplay = False
HAnimJoint295.bboxSize = [-1,-1,-1]
HAnimJoint295.center = [0.0041,1.1276,-0.0796]
HAnimJoint295.name = "vl3"
HAnimJoint295.visible = True
HAnimSegment296 = x3d.HAnimSegment()
HAnimSegment296.DEF = "STD_Segment_l3"
HAnimSegment296.bboxDisplay = False
HAnimSegment296.name = "l3"
HAnimSegment296.visible = True

HAnimJoint295.children.append(HAnimSegment296)
HAnimJoint297 = x3d.HAnimJoint()
HAnimJoint297.DEF = "STD_Joint_vl2"
HAnimJoint297.bboxCenter = [0,0,0]
HAnimJoint297.bboxDisplay = False
HAnimJoint297.bboxSize = [-1,-1,-1]
HAnimJoint297.center = [0.0045,1.1546,-0.0800]
HAnimJoint297.name = "vl2"
HAnimJoint297.visible = True
HAnimSegment298 = x3d.HAnimSegment()
HAnimSegment298.DEF = "STD_Segment_l2"
HAnimSegment298.bboxDisplay = False
HAnimSegment298.name = "l2"
HAnimSegment298.visible = True
HAnimSite299 = x3d.HAnimSite()
HAnimSite299.DEF = "STD_Site_spine_2_middle_back_pt"
HAnimSite299.bboxCenter = [0,0,0]
HAnimSite299.bboxDisplay = False
HAnimSite299.bboxSize = [-1,-1,-1]
HAnimSite299.name = "spine_2_middle_back_pt"
HAnimSite299.visible = True
TouchSensor300 = x3d.TouchSensor()
TouchSensor300.description = "HAnimSite spine_2_middle_back_pt"

HAnimSite299.children.append(TouchSensor300)
Shape301 = x3d.Shape()
Shape301.USE = "HAnimSiteShape"
Shape301.bboxCenter = [0,0,0]
Shape301.bboxDisplay = False
Shape301.bboxSize = [-1,-1,-1]
Shape301.visible = True

HAnimSite299.children.append(Shape301)

HAnimSegment298.children.append(HAnimSite299)
HAnimSite302 = x3d.HAnimSite()
HAnimSite302.DEF = "STD_Site_l_rib10_pt"
HAnimSite302.bboxCenter = [0,0,0]
HAnimSite302.bboxDisplay = False
HAnimSite302.bboxSize = [-1,-1,-1]
HAnimSite302.name = "l_rib10_pt"
HAnimSite302.translation = [0.0871,1.1925,0.0992]
HAnimSite302.visible = True
TouchSensor303 = x3d.TouchSensor()
TouchSensor303.description = "HAnimSite l_rib10_pt"

HAnimSite302.children.append(TouchSensor303)
Shape304 = x3d.Shape()
Shape304.USE = "HAnimSiteShape"
Shape304.bboxCenter = [0,0,0]
Shape304.bboxDisplay = False
Shape304.bboxSize = [-1,-1,-1]
Shape304.visible = True

HAnimSite302.children.append(Shape304)

HAnimSegment298.children.append(HAnimSite302)
HAnimSite305 = x3d.HAnimSite()
HAnimSite305.DEF = "STD_Site_r_rib10_pt"
HAnimSite305.bboxCenter = [0,0,0]
HAnimSite305.bboxDisplay = False
HAnimSite305.bboxSize = [-1,-1,-1]
HAnimSite305.name = "r_rib10_pt"
HAnimSite305.translation = [-0.0711,1.1941,0.1016]
HAnimSite305.visible = True
TouchSensor306 = x3d.TouchSensor()
TouchSensor306.description = "HAnimSite r_rib10_pt"

HAnimSite305.children.append(TouchSensor306)
Shape307 = x3d.Shape()
Shape307.USE = "HAnimSiteShape"
Shape307.bboxCenter = [0,0,0]
Shape307.bboxDisplay = False
Shape307.bboxSize = [-1,-1,-1]
Shape307.visible = True

HAnimSite305.children.append(Shape307)

HAnimSegment298.children.append(HAnimSite305)

HAnimJoint297.children.append(HAnimSegment298)
HAnimJoint308 = x3d.HAnimJoint()
HAnimJoint308.DEF = "STD_Joint_vl1"
HAnimJoint308.bboxCenter = [0,0,0]
HAnimJoint308.bboxDisplay = False
HAnimJoint308.bboxSize = [-1,-1,-1]
HAnimJoint308.center = [0.0048,1.1912,-0.0805]
HAnimJoint308.name = "vl1"
HAnimJoint308.visible = True
HAnimSegment309 = x3d.HAnimSegment()
HAnimSegment309.DEF = "STD_Segment_l1"
HAnimSegment309.bboxDisplay = False
HAnimSegment309.name = "l1"
HAnimSegment309.visible = True

HAnimJoint308.children.append(HAnimSegment309)
HAnimJoint310 = x3d.HAnimJoint()
HAnimJoint310.DEF = "STD_Joint_vt12"
HAnimJoint310.bboxCenter = [0,0,0]
HAnimJoint310.bboxDisplay = False
HAnimJoint310.bboxSize = [-1,-1,-1]
HAnimJoint310.center = [0.0051,1.2278,-0.0808]
HAnimJoint310.name = "vt12"
HAnimJoint310.visible = True
HAnimSegment311 = x3d.HAnimSegment()
HAnimSegment311.DEF = "STD_Segment_t12"
HAnimSegment311.bboxDisplay = False
HAnimSegment311.name = "t12"
HAnimSegment311.visible = True

HAnimJoint310.children.append(HAnimSegment311)
HAnimJoint312 = x3d.HAnimJoint()
HAnimJoint312.DEF = "STD_Joint_vt11"
HAnimJoint312.bboxCenter = [0,0,0]
HAnimJoint312.bboxDisplay = False
HAnimJoint312.bboxSize = [-1,-1,-1]
HAnimJoint312.center = [0.0053,1.2679,-0.0810]
HAnimJoint312.name = "vt11"
HAnimJoint312.visible = True
HAnimSegment313 = x3d.HAnimSegment()
HAnimSegment313.DEF = "STD_Segment_t11"
HAnimSegment313.bboxDisplay = False
HAnimSegment313.name = "t11"
HAnimSegment313.visible = True

HAnimJoint312.children.append(HAnimSegment313)
HAnimJoint314 = x3d.HAnimJoint()
HAnimJoint314.DEF = "STD_Joint_vt10"
HAnimJoint314.bboxCenter = [0,0,0]
HAnimJoint314.bboxDisplay = False
HAnimJoint314.bboxSize = [-1,-1,-1]
HAnimJoint314.center = [0.0056,1.2848,-0.0822]
HAnimJoint314.name = "vt10"
HAnimJoint314.visible = True
HAnimSegment315 = x3d.HAnimSegment()
HAnimSegment315.DEF = "STD_Segment_t10"
HAnimSegment315.bboxDisplay = False
HAnimSegment315.name = "t10"
HAnimSegment315.visible = True
HAnimSite316 = x3d.HAnimSite()
HAnimSite316.DEF = "STD_Site_substernale_pt"
HAnimSite316.bboxCenter = [0,0,0]
HAnimSite316.bboxDisplay = False
HAnimSite316.bboxSize = [-1,-1,-1]
HAnimSite316.name = "substernale_pt"
HAnimSite316.translation = [0.0085,1.2995,0.1147]
HAnimSite316.visible = True
TouchSensor317 = x3d.TouchSensor()
TouchSensor317.description = "HAnimSite substernale_pt"

HAnimSite316.children.append(TouchSensor317)
Shape318 = x3d.Shape()
Shape318.USE = "HAnimSiteShape"
Shape318.bboxCenter = [0,0,0]
Shape318.bboxDisplay = False
Shape318.bboxSize = [-1,-1,-1]
Shape318.visible = True

HAnimSite316.children.append(Shape318)

HAnimSegment315.children.append(HAnimSite316)

HAnimJoint314.children.append(HAnimSegment315)
HAnimJoint319 = x3d.HAnimJoint()
HAnimJoint319.DEF = "STD_Joint_vt9"
HAnimJoint319.bboxCenter = [0,0,0]
HAnimJoint319.bboxDisplay = False
HAnimJoint319.bboxSize = [-1,-1,-1]
HAnimJoint319.center = [0.0057,1.3126,-0.0838]
HAnimJoint319.name = "vt9"
HAnimJoint319.visible = True
HAnimSegment320 = x3d.HAnimSegment()
HAnimSegment320.DEF = "STD_Segment_t9"
HAnimSegment320.bboxDisplay = False
HAnimSegment320.name = "t9"
HAnimSegment320.visible = True
HAnimSite321 = x3d.HAnimSite()
HAnimSite321.DEF = "STD_Site_l_thelion_pt"
HAnimSite321.bboxCenter = [0,0,0]
HAnimSite321.bboxDisplay = False
HAnimSite321.bboxSize = [-1,-1,-1]
HAnimSite321.name = "l_thelion_pt"
HAnimSite321.translation = [0.0918,1.3382,0.1192]
HAnimSite321.visible = True
TouchSensor322 = x3d.TouchSensor()
TouchSensor322.description = "HAnimSite l_thelion_pt"

HAnimSite321.children.append(TouchSensor322)
Shape323 = x3d.Shape()
Shape323.USE = "HAnimSiteShape"
Shape323.bboxCenter = [0,0,0]
Shape323.bboxDisplay = False
Shape323.bboxSize = [-1,-1,-1]
Shape323.visible = True

HAnimSite321.children.append(Shape323)

HAnimSegment320.children.append(HAnimSite321)
HAnimSite324 = x3d.HAnimSite()
HAnimSite324.DEF = "STD_Site_r_thelion_pt"
HAnimSite324.bboxCenter = [0,0,0]
HAnimSite324.bboxDisplay = False
HAnimSite324.bboxSize = [-1,-1,-1]
HAnimSite324.name = "r_thelion_pt"
HAnimSite324.translation = [-0.0736,1.3385,0.1217]
HAnimSite324.visible = True
TouchSensor325 = x3d.TouchSensor()
TouchSensor325.description = "HAnimSite r_thelion_pt"

HAnimSite324.children.append(TouchSensor325)
Shape326 = x3d.Shape()
Shape326.USE = "HAnimSiteShape"
Shape326.bboxCenter = [0,0,0]
Shape326.bboxDisplay = False
Shape326.bboxSize = [-1,-1,-1]
Shape326.visible = True

HAnimSite324.children.append(Shape326)

HAnimSegment320.children.append(HAnimSite324)

HAnimJoint319.children.append(HAnimSegment320)
HAnimJoint327 = x3d.HAnimJoint()
HAnimJoint327.DEF = "STD_Joint_vt8"
HAnimJoint327.bboxCenter = [0,0,0]
HAnimJoint327.bboxDisplay = False
HAnimJoint327.bboxSize = [-1,-1,-1]
HAnimJoint327.center = [0.0057,1.3382,-0.0845]
HAnimJoint327.name = "vt8"
HAnimJoint327.visible = True
HAnimSegment328 = x3d.HAnimSegment()
HAnimSegment328.DEF = "STD_Segment_t8"
HAnimSegment328.bboxDisplay = False
HAnimSegment328.name = "t8"
HAnimSegment328.visible = True

HAnimJoint327.children.append(HAnimSegment328)
HAnimJoint329 = x3d.HAnimJoint()
HAnimJoint329.DEF = "STD_Joint_vt7"
HAnimJoint329.bboxCenter = [0,0,0]
HAnimJoint329.bboxDisplay = False
HAnimJoint329.bboxSize = [-1,-1,-1]
HAnimJoint329.center = [0.0058,1.3625,-0.0833]
HAnimJoint329.name = "vt7"
HAnimJoint329.visible = True
HAnimSegment330 = x3d.HAnimSegment()
HAnimSegment330.DEF = "STD_Segment_t7"
HAnimSegment330.bboxDisplay = False
HAnimSegment330.name = "t7"
HAnimSegment330.visible = True

HAnimJoint329.children.append(HAnimSegment330)
HAnimJoint331 = x3d.HAnimJoint()
HAnimJoint331.DEF = "STD_Joint_vt6"
HAnimJoint331.bboxCenter = [0,0,0]
HAnimJoint331.bboxDisplay = False
HAnimJoint331.bboxSize = [-1,-1,-1]
HAnimJoint331.center = [0.0059,1.3866,-0.0800]
HAnimJoint331.name = "vt6"
HAnimJoint331.visible = True
HAnimSegment332 = x3d.HAnimSegment()
HAnimSegment332.DEF = "STD_Segment_t6"
HAnimSegment332.bboxDisplay = False
HAnimSegment332.name = "t6"
HAnimSegment332.visible = True
HAnimSite333 = x3d.HAnimSite()
HAnimSite333.DEF = "STD_Site_l_chest_midsagittal_plane_pt"
HAnimSite333.bboxCenter = [0,0,0]
HAnimSite333.bboxDisplay = False
HAnimSite333.bboxSize = [-1,-1,-1]
HAnimSite333.name = "l_chest_midsagittal_plane_pt"
HAnimSite333.visible = True
TouchSensor334 = x3d.TouchSensor()
TouchSensor334.description = "HAnimSite l_chest_midsagittal_plane_pt"

HAnimSite333.children.append(TouchSensor334)
Shape335 = x3d.Shape()
Shape335.USE = "HAnimSiteShape"
Shape335.bboxCenter = [0,0,0]
Shape335.bboxDisplay = False
Shape335.bboxSize = [-1,-1,-1]
Shape335.visible = True

HAnimSite333.children.append(Shape335)

HAnimSegment332.children.append(HAnimSite333)
HAnimSite336 = x3d.HAnimSite()
HAnimSite336.DEF = "STD_Site_mesosternale_pt"
HAnimSite336.bboxCenter = [0,0,0]
HAnimSite336.bboxDisplay = False
HAnimSite336.bboxSize = [-1,-1,-1]
HAnimSite336.name = "mesosternale_pt"
HAnimSite336.visible = True
TouchSensor337 = x3d.TouchSensor()
TouchSensor337.description = "HAnimSite mesosternale_pt"

HAnimSite336.children.append(TouchSensor337)
Shape338 = x3d.Shape()
Shape338.USE = "HAnimSiteShape"
Shape338.bboxCenter = [0,0,0]
Shape338.bboxDisplay = False
Shape338.bboxSize = [-1,-1,-1]
Shape338.visible = True

HAnimSite336.children.append(Shape338)

HAnimSegment332.children.append(HAnimSite336)
HAnimSite339 = x3d.HAnimSite()
HAnimSite339.DEF = "STD_Site_rear_center_midsagittal_plane_pt"
HAnimSite339.bboxCenter = [0,0,0]
HAnimSite339.bboxDisplay = False
HAnimSite339.bboxSize = [-1,-1,-1]
HAnimSite339.name = "rear_center_midsagittal_plane_pt"
HAnimSite339.visible = True
TouchSensor340 = x3d.TouchSensor()
TouchSensor340.description = "HAnimSite rear_center_midsagittal_plane_pt"

HAnimSite339.children.append(TouchSensor340)
Shape341 = x3d.Shape()
Shape341.USE = "HAnimSiteShape"
Shape341.bboxCenter = [0,0,0]
Shape341.bboxDisplay = False
Shape341.bboxSize = [-1,-1,-1]
Shape341.visible = True

HAnimSite339.children.append(Shape341)

HAnimSegment332.children.append(HAnimSite339)
HAnimSite342 = x3d.HAnimSite()
HAnimSite342.DEF = "STD_Site_r_chest_midsagittal_plane_pt"
HAnimSite342.bboxCenter = [0,0,0]
HAnimSite342.bboxDisplay = False
HAnimSite342.bboxSize = [-1,-1,-1]
HAnimSite342.name = "r_chest_midsagittal_plane_pt"
HAnimSite342.visible = True
TouchSensor343 = x3d.TouchSensor()
TouchSensor343.description = "HAnimSite r_chest_midsagittal_plane_pt"

HAnimSite342.children.append(TouchSensor343)
Shape344 = x3d.Shape()
Shape344.USE = "HAnimSiteShape"
Shape344.bboxCenter = [0,0,0]
Shape344.bboxDisplay = False
Shape344.bboxSize = [-1,-1,-1]
Shape344.visible = True

HAnimSite342.children.append(Shape344)

HAnimSegment332.children.append(HAnimSite342)

HAnimJoint331.children.append(HAnimSegment332)
HAnimJoint345 = x3d.HAnimJoint()
HAnimJoint345.DEF = "STD_Joint_vt5"
HAnimJoint345.bboxCenter = [0,0,0]
HAnimJoint345.bboxDisplay = False
HAnimJoint345.bboxSize = [-1,-1,-1]
HAnimJoint345.center = [0.0060,1.4102,-0.0745]
HAnimJoint345.name = "vt5"
HAnimJoint345.visible = True
HAnimSegment346 = x3d.HAnimSegment()
HAnimSegment346.DEF = "STD_Segment_t5"
HAnimSegment346.bboxDisplay = False
HAnimSegment346.name = "t5"
HAnimSegment346.visible = True
HAnimSite347 = x3d.HAnimSite()
HAnimSite347.DEF = "STD_Site_spine_1_middle_back_pt"
HAnimSite347.bboxCenter = [0,0,0]
HAnimSite347.bboxDisplay = False
HAnimSite347.bboxSize = [-1,-1,-1]
HAnimSite347.name = "spine_1_middle_back_pt"
HAnimSite347.visible = True
TouchSensor348 = x3d.TouchSensor()
TouchSensor348.description = "HAnimSite spine_1_middle_back_pt"

HAnimSite347.children.append(TouchSensor348)
Shape349 = x3d.Shape()
Shape349.USE = "HAnimSiteShape"
Shape349.bboxCenter = [0,0,0]
Shape349.bboxDisplay = False
Shape349.bboxSize = [-1,-1,-1]
Shape349.visible = True

HAnimSite347.children.append(Shape349)

HAnimSegment346.children.append(HAnimSite347)

HAnimJoint345.children.append(HAnimSegment346)
HAnimJoint350 = x3d.HAnimJoint()
HAnimJoint350.DEF = "STD_Joint_vt4"
HAnimJoint350.bboxCenter = [0,0,0]
HAnimJoint350.bboxDisplay = False
HAnimJoint350.bboxSize = [-1,-1,-1]
HAnimJoint350.center = [0.0061,1.4320,-0.0675]
HAnimJoint350.name = "vt4"
HAnimJoint350.visible = True
HAnimSegment351 = x3d.HAnimSegment()
HAnimSegment351.DEF = "STD_Segment_t4"
HAnimSegment351.bboxDisplay = False
HAnimSegment351.name = "t4"
HAnimSegment351.visible = True

HAnimJoint350.children.append(HAnimSegment351)
HAnimJoint352 = x3d.HAnimJoint()
HAnimJoint352.DEF = "STD_Joint_vt3"
HAnimJoint352.bboxCenter = [0,0,0]
HAnimJoint352.bboxDisplay = False
HAnimJoint352.bboxSize = [-1,-1,-1]
HAnimJoint352.center = [0.0062,1.4583,-0.0570]
HAnimJoint352.name = "vt3"
HAnimJoint352.visible = True
HAnimSegment353 = x3d.HAnimSegment()
HAnimSegment353.DEF = "STD_Segment_t3"
HAnimSegment353.bboxDisplay = False
HAnimSegment353.name = "t3"
HAnimSegment353.visible = True

HAnimJoint352.children.append(HAnimSegment353)
HAnimJoint354 = x3d.HAnimJoint()
HAnimJoint354.DEF = "STD_Joint_vt2"
HAnimJoint354.bboxCenter = [0,0,0]
HAnimJoint354.bboxDisplay = False
HAnimJoint354.bboxSize = [-1,-1,-1]
HAnimJoint354.center = [0.0063,1.4761,-0.0484]
HAnimJoint354.name = "vt2"
HAnimJoint354.visible = True
HAnimSegment355 = x3d.HAnimSegment()
HAnimSegment355.DEF = "STD_Segment_t2"
HAnimSegment355.bboxDisplay = False
HAnimSegment355.name = "t2"
HAnimSegment355.visible = True

HAnimJoint354.children.append(HAnimSegment355)
HAnimJoint356 = x3d.HAnimJoint()
HAnimJoint356.DEF = "STD_Joint_vt1"
HAnimJoint356.bboxCenter = [0,0,0]
HAnimJoint356.bboxDisplay = False
HAnimJoint356.bboxSize = [-1,-1,-1]
HAnimJoint356.center = [0.0065,1.4951,-0.0387]
HAnimJoint356.name = "vt1"
HAnimJoint356.visible = True
HAnimSegment357 = x3d.HAnimSegment()
HAnimSegment357.DEF = "STD_Segment_t1"
HAnimSegment357.bboxDisplay = False
HAnimSegment357.name = "t1"
HAnimSegment357.visible = True
HAnimSite358 = x3d.HAnimSite()
HAnimSite358.DEF = "STD_Site_suprasternale_pt"
HAnimSite358.bboxCenter = [0,0,0]
HAnimSite358.bboxDisplay = False
HAnimSite358.bboxSize = [-1,-1,-1]
HAnimSite358.name = "suprasternale_pt"
HAnimSite358.translation = [0.0084,1.4714,0.0551]
HAnimSite358.visible = True
TouchSensor359 = x3d.TouchSensor()
TouchSensor359.description = "HAnimSite suprasternale_pt"

HAnimSite358.children.append(TouchSensor359)
Shape360 = x3d.Shape()
Shape360.USE = "HAnimSiteShape"
Shape360.bboxCenter = [0,0,0]
Shape360.bboxDisplay = False
Shape360.bboxSize = [-1,-1,-1]
Shape360.visible = True

HAnimSite358.children.append(Shape360)

HAnimSegment357.children.append(HAnimSite358)
HAnimSite361 = x3d.HAnimSite()
HAnimSite361.DEF = "STD_Site_cervicale_pt"
HAnimSite361.bboxCenter = [0,0,0]
HAnimSite361.bboxDisplay = False
HAnimSite361.bboxSize = [-1,-1,-1]
HAnimSite361.name = "cervicale_pt"
HAnimSite361.translation = [0.0064,1.520,-0.0815]
HAnimSite361.visible = True
TouchSensor362 = x3d.TouchSensor()
TouchSensor362.description = "HAnimSite cervicale_pt"

HAnimSite361.children.append(TouchSensor362)
Shape363 = x3d.Shape()
Shape363.USE = "HAnimSiteShape"
Shape363.bboxCenter = [0,0,0]
Shape363.bboxDisplay = False
Shape363.bboxSize = [-1,-1,-1]
Shape363.visible = True

HAnimSite361.children.append(Shape363)

HAnimSegment357.children.append(HAnimSite361)

HAnimJoint356.children.append(HAnimSegment357)
HAnimJoint364 = x3d.HAnimJoint()
HAnimJoint364.DEF = "STD_Joint_vc7"
HAnimJoint364.bboxCenter = [0,0,0]
HAnimJoint364.bboxDisplay = False
HAnimJoint364.bboxSize = [-1,-1,-1]
HAnimJoint364.center = [0.0066,1.5132,-0.0301]
HAnimJoint364.name = "vc7"
HAnimJoint364.visible = True
HAnimSegment365 = x3d.HAnimSegment()
HAnimSegment365.DEF = "STD_Segment_c7"
HAnimSegment365.bboxDisplay = False
HAnimSegment365.name = "c7"
HAnimSegment365.visible = True
HAnimSite366 = x3d.HAnimSite()
HAnimSite366.DEF = "STD_Site_r_neck_base_pt"
HAnimSite366.bboxCenter = [0,0,0]
HAnimSite366.bboxDisplay = False
HAnimSite366.bboxSize = [-1,-1,-1]
HAnimSite366.name = "r_neck_base_pt"
HAnimSite366.translation = [-0.0419,1.5149,-0.0220]
HAnimSite366.visible = True
TouchSensor367 = x3d.TouchSensor()
TouchSensor367.description = "HAnimSite r_neck_base_pt"

HAnimSite366.children.append(TouchSensor367)
Shape368 = x3d.Shape()
Shape368.USE = "HAnimSiteShape"
Shape368.bboxCenter = [0,0,0]
Shape368.bboxDisplay = False
Shape368.bboxSize = [-1,-1,-1]
Shape368.visible = True

HAnimSite366.children.append(Shape368)

HAnimSegment365.children.append(HAnimSite366)
HAnimSite369 = x3d.HAnimSite()
HAnimSite369.DEF = "STD_Site_l_neck_base_pt"
HAnimSite369.bboxCenter = [0,0,0]
HAnimSite369.bboxDisplay = False
HAnimSite369.bboxSize = [-1,-1,-1]
HAnimSite369.name = "l_neck_base_pt"
HAnimSite369.translation = [0.0646,1.5141,-0.0380]
HAnimSite369.visible = True
TouchSensor370 = x3d.TouchSensor()
TouchSensor370.description = "HAnimSite l_neck_base_pt"

HAnimSite369.children.append(TouchSensor370)
Shape371 = x3d.Shape()
Shape371.USE = "HAnimSiteShape"
Shape371.bboxCenter = [0,0,0]
Shape371.bboxDisplay = False
Shape371.bboxSize = [-1,-1,-1]
Shape371.visible = True

HAnimSite369.children.append(Shape371)

HAnimSegment365.children.append(HAnimSite369)

HAnimJoint364.children.append(HAnimSegment365)
HAnimJoint372 = x3d.HAnimJoint()
HAnimJoint372.DEF = "STD_Joint_vc6"
HAnimJoint372.bboxCenter = [0,0,0]
HAnimJoint372.bboxDisplay = False
HAnimJoint372.bboxSize = [-1,-1,-1]
HAnimJoint372.center = [0.0066,1.5357,-0.0143]
HAnimJoint372.name = "vc6"
HAnimJoint372.visible = True
HAnimSegment373 = x3d.HAnimSegment()
HAnimSegment373.DEF = "STD_Segment_c6"
HAnimSegment373.bboxDisplay = False
HAnimSegment373.name = "c6"
HAnimSegment373.visible = True

HAnimJoint372.children.append(HAnimSegment373)
HAnimJoint374 = x3d.HAnimJoint()
HAnimJoint374.DEF = "STD_Joint_vc5"
HAnimJoint374.bboxCenter = [0,0,0]
HAnimJoint374.bboxDisplay = False
HAnimJoint374.bboxSize = [-1,-1,-1]
HAnimJoint374.center = [0.0066,1.5520,-0.0082]
HAnimJoint374.name = "vc5"
HAnimJoint374.visible = True
HAnimSegment375 = x3d.HAnimSegment()
HAnimSegment375.DEF = "STD_Segment_c5"
HAnimSegment375.bboxDisplay = False
HAnimSegment375.name = "c5"
HAnimSegment375.visible = True

HAnimJoint374.children.append(HAnimSegment375)
HAnimJoint376 = x3d.HAnimJoint()
HAnimJoint376.DEF = "STD_Joint_vc4"
HAnimJoint376.bboxCenter = [0,0,0]
HAnimJoint376.bboxDisplay = False
HAnimJoint376.bboxSize = [-1,-1,-1]
HAnimJoint376.center = [0.0066,1.5662,-0.0084]
HAnimJoint376.name = "vc4"
HAnimJoint376.visible = True
HAnimSegment377 = x3d.HAnimSegment()
HAnimSegment377.DEF = "STD_Segment_c4"
HAnimSegment377.bboxDisplay = False
HAnimSegment377.name = "c4"
HAnimSegment377.visible = True

HAnimJoint376.children.append(HAnimSegment377)
HAnimJoint378 = x3d.HAnimJoint()
HAnimJoint378.DEF = "STD_Joint_vc3"
HAnimJoint378.bboxCenter = [0,0,0]
HAnimJoint378.bboxDisplay = False
HAnimJoint378.bboxSize = [-1,-1,-1]
HAnimJoint378.center = [0.0066,1.5800,-0.0103]
HAnimJoint378.name = "vc3"
HAnimJoint378.visible = True
HAnimSegment379 = x3d.HAnimSegment()
HAnimSegment379.DEF = "STD_Segment_c3"
HAnimSegment379.bboxDisplay = False
HAnimSegment379.name = "c3"
HAnimSegment379.visible = True

HAnimJoint378.children.append(HAnimSegment379)
HAnimJoint380 = x3d.HAnimJoint()
HAnimJoint380.DEF = "STD_Joint_vc2"
HAnimJoint380.bboxCenter = [0,0,0]
HAnimJoint380.bboxDisplay = False
HAnimJoint380.bboxSize = [-1,-1,-1]
HAnimJoint380.center = [0.0066,1.5928,-0.0103]
HAnimJoint380.name = "vc2"
HAnimJoint380.visible = True
HAnimSegment381 = x3d.HAnimSegment()
HAnimSegment381.DEF = "STD_Segment_c2"
HAnimSegment381.bboxDisplay = False
HAnimSegment381.name = "c2"
HAnimSegment381.visible = True
HAnimSite382 = x3d.HAnimSite()
HAnimSite382.DEF = "STD_Site_adams_apple_pt"
HAnimSite382.bboxCenter = [0,0,0]
HAnimSite382.bboxDisplay = False
HAnimSite382.bboxSize = [-1,-1,-1]
HAnimSite382.name = "adams_apple_pt"
HAnimSite382.visible = True
TouchSensor383 = x3d.TouchSensor()
TouchSensor383.description = "HAnimSite adams_apple_pt"

HAnimSite382.children.append(TouchSensor383)
Shape384 = x3d.Shape()
Shape384.USE = "HAnimSiteShape"
Shape384.bboxCenter = [0,0,0]
Shape384.bboxDisplay = False
Shape384.bboxSize = [-1,-1,-1]
Shape384.visible = True

HAnimSite382.children.append(Shape384)

HAnimSegment381.children.append(HAnimSite382)

HAnimJoint380.children.append(HAnimSegment381)
HAnimJoint385 = x3d.HAnimJoint()
HAnimJoint385.DEF = "STD_Joint_vc1"
HAnimJoint385.bboxCenter = [0,0,0]
HAnimJoint385.bboxDisplay = False
HAnimJoint385.bboxSize = [-1,-1,-1]
HAnimJoint385.center = [0.0066,1.6144,-0.0034]
HAnimJoint385.name = "vc1"
HAnimJoint385.visible = True
HAnimSegment386 = x3d.HAnimSegment()
HAnimSegment386.DEF = "STD_Segment_c1"
HAnimSegment386.bboxDisplay = False
HAnimSegment386.name = "c1"
HAnimSegment386.visible = True

HAnimJoint385.children.append(HAnimSegment386)
HAnimJoint387 = x3d.HAnimJoint()
HAnimJoint387.DEF = "STD_Joint_skullbase"
HAnimJoint387.bboxCenter = [0,0,0]
HAnimJoint387.bboxDisplay = False
HAnimJoint387.bboxSize = [-1,-1,-1]
HAnimJoint387.center = [0.0044,1.6209,0.0236]
HAnimJoint387.name = "skullbase"
HAnimJoint387.visible = True
HAnimSegment388 = x3d.HAnimSegment()
HAnimSegment388.DEF = "STD_Segment_skull"
HAnimSegment388.bboxDisplay = False
HAnimSegment388.name = "skull"
HAnimSegment388.visible = True
HAnimSite389 = x3d.HAnimSite()
HAnimSite389.DEF = "STD_Site_l_infraorbitale_pt"
HAnimSite389.bboxCenter = [0,0,0]
HAnimSite389.bboxDisplay = False
HAnimSite389.bboxSize = [-1,-1,-1]
HAnimSite389.name = "l_infraorbitale_pt"
HAnimSite389.translation = [0.0341,1.6171,0.0752]
HAnimSite389.visible = True
TouchSensor390 = x3d.TouchSensor()
TouchSensor390.description = "HAnimSite l_infraorbitale_pt"

HAnimSite389.children.append(TouchSensor390)
Shape391 = x3d.Shape()
Shape391.USE = "HAnimSiteShape"
Shape391.bboxCenter = [0,0,0]
Shape391.bboxDisplay = False
Shape391.bboxSize = [-1,-1,-1]
Shape391.visible = True

HAnimSite389.children.append(Shape391)

HAnimSegment388.children.append(HAnimSite389)
HAnimSite392 = x3d.HAnimSite()
HAnimSite392.DEF = "STD_Site_sellion_pt"
HAnimSite392.bboxCenter = [0,0,0]
HAnimSite392.bboxDisplay = False
HAnimSite392.bboxSize = [-1,-1,-1]
HAnimSite392.name = "sellion_pt"
HAnimSite392.translation = [0.0058,1.6316,0.0852]
HAnimSite392.visible = True
TouchSensor393 = x3d.TouchSensor()
TouchSensor393.description = "HAnimSite sellion_pt"

HAnimSite392.children.append(TouchSensor393)
Shape394 = x3d.Shape()
Shape394.USE = "HAnimSiteShape"
Shape394.bboxCenter = [0,0,0]
Shape394.bboxDisplay = False
Shape394.bboxSize = [-1,-1,-1]
Shape394.visible = True

HAnimSite392.children.append(Shape394)

HAnimSegment388.children.append(HAnimSite392)
HAnimSite395 = x3d.HAnimSite()
HAnimSite395.DEF = "STD_Site_opisthocranion_pt"
HAnimSite395.bboxCenter = [0,0,0]
HAnimSite395.bboxDisplay = False
HAnimSite395.bboxSize = [-1,-1,-1]
HAnimSite395.name = "opisthocranion_pt"
HAnimSite395.visible = True
TouchSensor396 = x3d.TouchSensor()
TouchSensor396.description = "HAnimSite opisthocranion_pt"

HAnimSite395.children.append(TouchSensor396)
Shape397 = x3d.Shape()
Shape397.USE = "HAnimSiteShape"
Shape397.bboxCenter = [0,0,0]
Shape397.bboxDisplay = False
Shape397.bboxSize = [-1,-1,-1]
Shape397.visible = True

HAnimSite395.children.append(Shape397)

HAnimSegment388.children.append(HAnimSite395)
HAnimSite398 = x3d.HAnimSite()
HAnimSite398.DEF = "STD_Site_r_infraorbitale_pt"
HAnimSite398.bboxCenter = [0,0,0]
HAnimSite398.bboxDisplay = False
HAnimSite398.bboxSize = [-1,-1,-1]
HAnimSite398.name = "r_infraorbitale_pt"
HAnimSite398.translation = [-0.0237,1.6171,0.0752]
HAnimSite398.visible = True
TouchSensor399 = x3d.TouchSensor()
TouchSensor399.description = "HAnimSite r_infraorbitale_pt"

HAnimSite398.children.append(TouchSensor399)
Shape400 = x3d.Shape()
Shape400.USE = "HAnimSiteShape"
Shape400.bboxCenter = [0,0,0]
Shape400.bboxDisplay = False
Shape400.bboxSize = [-1,-1,-1]
Shape400.visible = True

HAnimSite398.children.append(Shape400)

HAnimSegment388.children.append(HAnimSite398)
HAnimSite401 = x3d.HAnimSite()
HAnimSite401.DEF = "STD_Site_skull_vertex_pt"
HAnimSite401.bboxCenter = [0,0,0]
HAnimSite401.bboxDisplay = False
HAnimSite401.bboxSize = [-1,-1,-1]
HAnimSite401.name = "skull_vertex_pt"
HAnimSite401.translation = [0.0050,1.7504,0.0055]
HAnimSite401.visible = True
TouchSensor402 = x3d.TouchSensor()
TouchSensor402.description = "HAnimSite skull_vertex_pt"

HAnimSite401.children.append(TouchSensor402)
Shape403 = x3d.Shape()
Shape403.USE = "HAnimSiteShape"
Shape403.bboxCenter = [0,0,0]
Shape403.bboxDisplay = False
Shape403.bboxSize = [-1,-1,-1]
Shape403.visible = True

HAnimSite401.children.append(Shape403)

HAnimSegment388.children.append(HAnimSite401)
HAnimSite404 = x3d.HAnimSite()
HAnimSite404.DEF = "STD_Site_glabella_pt"
HAnimSite404.bboxCenter = [0,0,0]
HAnimSite404.bboxDisplay = False
HAnimSite404.bboxSize = [-1,-1,-1]
HAnimSite404.name = "glabella_pt"
HAnimSite404.visible = True
TouchSensor405 = x3d.TouchSensor()
TouchSensor405.description = "HAnimSite glabella_pt"

HAnimSite404.children.append(TouchSensor405)
Shape406 = x3d.Shape()
Shape406.USE = "HAnimSiteShape"
Shape406.bboxCenter = [0,0,0]
Shape406.bboxDisplay = False
Shape406.bboxSize = [-1,-1,-1]
Shape406.visible = True

HAnimSite404.children.append(Shape406)

HAnimSegment388.children.append(HAnimSite404)
HAnimSite407 = x3d.HAnimSite()
HAnimSite407.DEF = "STD_Site_r_ectocanthus_pt"
HAnimSite407.bboxCenter = [0,0,0]
HAnimSite407.bboxDisplay = False
HAnimSite407.bboxSize = [-1,-1,-1]
HAnimSite407.name = "r_ectocanthus_pt"
HAnimSite407.visible = True
TouchSensor408 = x3d.TouchSensor()
TouchSensor408.description = "HAnimSite r_ectocanthus_pt"

HAnimSite407.children.append(TouchSensor408)
Shape409 = x3d.Shape()
Shape409.USE = "HAnimSiteShape"
Shape409.bboxCenter = [0,0,0]
Shape409.bboxDisplay = False
Shape409.bboxSize = [-1,-1,-1]
Shape409.visible = True

HAnimSite407.children.append(Shape409)

HAnimSegment388.children.append(HAnimSite407)
HAnimSite410 = x3d.HAnimSite()
HAnimSite410.DEF = "STD_Site_r_tragion_pt"
HAnimSite410.bboxCenter = [0,0,0]
HAnimSite410.bboxDisplay = False
HAnimSite410.bboxSize = [-1,-1,-1]
HAnimSite410.name = "r_tragion_pt"
HAnimSite410.translation = [-0.0646,1.6347,0.0302]
HAnimSite410.visible = True
TouchSensor411 = x3d.TouchSensor()
TouchSensor411.description = "HAnimSite r_tragion_pt"

HAnimSite410.children.append(TouchSensor411)
Shape412 = x3d.Shape()
Shape412.USE = "HAnimSiteShape"
Shape412.bboxCenter = [0,0,0]
Shape412.bboxDisplay = False
Shape412.bboxSize = [-1,-1,-1]
Shape412.visible = True

HAnimSite410.children.append(Shape412)

HAnimSegment388.children.append(HAnimSite410)
HAnimSite413 = x3d.HAnimSite()
HAnimSite413.DEF = "STD_Site_l_ectocanthus_pt"
HAnimSite413.bboxCenter = [0,0,0]
HAnimSite413.bboxDisplay = False
HAnimSite413.bboxSize = [-1,-1,-1]
HAnimSite413.name = "l_ectocanthus_pt"
HAnimSite413.visible = True
TouchSensor414 = x3d.TouchSensor()
TouchSensor414.description = "HAnimSite l_ectocanthus_pt"

HAnimSite413.children.append(TouchSensor414)
Shape415 = x3d.Shape()
Shape415.USE = "HAnimSiteShape"
Shape415.bboxCenter = [0,0,0]
Shape415.bboxDisplay = False
Shape415.bboxSize = [-1,-1,-1]
Shape415.visible = True

HAnimSite413.children.append(Shape415)

HAnimSegment388.children.append(HAnimSite413)
HAnimSite416 = x3d.HAnimSite()
HAnimSite416.DEF = "STD_Site_l_tragion_pt"
HAnimSite416.bboxCenter = [0,0,0]
HAnimSite416.bboxDisplay = False
HAnimSite416.bboxSize = [-1,-1,-1]
HAnimSite416.name = "l_tragion_pt"
HAnimSite416.translation = [0.0739,1.6348,0.0282]
HAnimSite416.visible = True
TouchSensor417 = x3d.TouchSensor()
TouchSensor417.description = "HAnimSite l_tragion_pt"

HAnimSite416.children.append(TouchSensor417)
Shape418 = x3d.Shape()
Shape418.USE = "HAnimSiteShape"
Shape418.bboxCenter = [0,0,0]
Shape418.bboxDisplay = False
Shape418.bboxSize = [-1,-1,-1]
Shape418.visible = True

HAnimSite416.children.append(Shape418)

HAnimSegment388.children.append(HAnimSite416)
HAnimSite419 = x3d.HAnimSite()
HAnimSite419.DEF = "STD_Site_nuchale_pt"
HAnimSite419.bboxCenter = [0,0,0]
HAnimSite419.bboxDisplay = False
HAnimSite419.bboxSize = [-1,-1,-1]
HAnimSite419.name = "nuchale_pt"
HAnimSite419.translation = [0.0039,1.5972,-0.0796]
HAnimSite419.visible = True
TouchSensor420 = x3d.TouchSensor()
TouchSensor420.description = "HAnimSite nuchale_pt"

HAnimSite419.children.append(TouchSensor420)
Shape421 = x3d.Shape()
Shape421.USE = "HAnimSiteShape"
Shape421.bboxCenter = [0,0,0]
Shape421.bboxDisplay = False
Shape421.bboxSize = [-1,-1,-1]
Shape421.visible = True

HAnimSite419.children.append(Shape421)

HAnimSegment388.children.append(HAnimSite419)

HAnimJoint387.children.append(HAnimSegment388)
HAnimJoint422 = x3d.HAnimJoint()
HAnimJoint422.DEF = "STD_Joint_l_eyelid_joint"
HAnimJoint422.bboxCenter = [0,0,0]
HAnimJoint422.bboxDisplay = False
HAnimJoint422.bboxSize = [-1,-1,-1]
HAnimJoint422.name = "l_eyelid_joint"
HAnimJoint422.visible = True
HAnimSegment423 = x3d.HAnimSegment()
HAnimSegment423.DEF = "STD_Segment_l_eyelid"
HAnimSegment423.bboxDisplay = False
HAnimSegment423.name = "l_eyelid"
HAnimSegment423.visible = True

HAnimJoint422.children.append(HAnimSegment423)
HAnimJoint424 = x3d.HAnimJoint()
HAnimJoint424.DEF = "STD_Joint_r_eyelid_joint"
HAnimJoint424.bboxCenter = [0,0,0]
HAnimJoint424.bboxDisplay = False
HAnimJoint424.bboxSize = [-1,-1,-1]
HAnimJoint424.name = "r_eyelid_joint"
HAnimJoint424.visible = True
HAnimSegment425 = x3d.HAnimSegment()
HAnimSegment425.DEF = "STD_Segment_r_eyelid"
HAnimSegment425.bboxDisplay = False
HAnimSegment425.name = "r_eyelid"
HAnimSegment425.visible = True

HAnimJoint424.children.append(HAnimSegment425)
HAnimJoint426 = x3d.HAnimJoint()
HAnimJoint426.DEF = "STD_Joint_l_eyeball_joint"
HAnimJoint426.bboxCenter = [0,0,0]
HAnimJoint426.bboxDisplay = False
HAnimJoint426.bboxSize = [-1,-1,-1]
HAnimJoint426.name = "l_eyeball_joint"
HAnimJoint426.visible = True
HAnimSegment427 = x3d.HAnimSegment()
HAnimSegment427.DEF = "STD_Segment_l_eyeball"
HAnimSegment427.bboxDisplay = False
HAnimSegment427.name = "l_eyeball"
HAnimSegment427.visible = True

HAnimJoint426.children.append(HAnimSegment427)
HAnimJoint428 = x3d.HAnimJoint()
HAnimJoint428.DEF = "STD_Joint_r_eyeball_joint"
HAnimJoint428.bboxCenter = [0,0,0]
HAnimJoint428.bboxDisplay = False
HAnimJoint428.bboxSize = [-1,-1,-1]
HAnimJoint428.name = "r_eyeball_joint"
HAnimJoint428.visible = True
HAnimSegment429 = x3d.HAnimSegment()
HAnimSegment429.DEF = "STD_Segment_r_eyeball"
HAnimSegment429.bboxDisplay = False
HAnimSegment429.name = "r_eyeball"
HAnimSegment429.visible = True

HAnimJoint428.children.append(HAnimSegment429)
HAnimJoint430 = x3d.HAnimJoint()
HAnimJoint430.DEF = "STD_Joint_l_eyebrow_joint"
HAnimJoint430.bboxCenter = [0,0,0]
HAnimJoint430.bboxDisplay = False
HAnimJoint430.bboxSize = [-1,-1,-1]
HAnimJoint430.name = "l_eyebrow_joint"
HAnimJoint430.visible = True
HAnimSegment431 = x3d.HAnimSegment()
HAnimSegment431.DEF = "STD_Segment_l_eyebrow"
HAnimSegment431.bboxDisplay = False
HAnimSegment431.name = "l_eyebrow"
HAnimSegment431.visible = True

HAnimJoint430.children.append(HAnimSegment431)
HAnimJoint432 = x3d.HAnimJoint()
HAnimJoint432.DEF = "STD_Joint_r_eyebrow_joint"
HAnimJoint432.bboxCenter = [0,0,0]
HAnimJoint432.bboxDisplay = False
HAnimJoint432.bboxSize = [-1,-1,-1]
HAnimJoint432.name = "r_eyebrow_joint"
HAnimJoint432.visible = True
HAnimSegment433 = x3d.HAnimSegment()
HAnimSegment433.DEF = "STD_Segment_r_eyebrow"
HAnimSegment433.bboxDisplay = False
HAnimSegment433.name = "r_eyebrow"
HAnimSegment433.visible = True

HAnimJoint432.children.append(HAnimSegment433)
HAnimJoint434 = x3d.HAnimJoint()
HAnimJoint434.DEF = "STD_Joint_temporomandibular"
HAnimJoint434.bboxCenter = [0,0,0]
HAnimJoint434.bboxDisplay = False
HAnimJoint434.bboxSize = [-1,-1,-1]
HAnimJoint434.name = "temporomandibular"
HAnimJoint434.visible = True
HAnimSegment435 = x3d.HAnimSegment()
HAnimSegment435.DEF = "STD_Segment_jaw"
HAnimSegment435.bboxDisplay = False
HAnimSegment435.name = "jaw"
HAnimSegment435.visible = True
HAnimSite436 = x3d.HAnimSite()
HAnimSite436.DEF = "STD_Site_menton_pt"
HAnimSite436.bboxCenter = [0,0,0]
HAnimSite436.bboxDisplay = False
HAnimSite436.bboxSize = [-1,-1,-1]
HAnimSite436.name = "menton_pt"
HAnimSite436.visible = True
TouchSensor437 = x3d.TouchSensor()
TouchSensor437.description = "HAnimSite menton_pt"

HAnimSite436.children.append(TouchSensor437)
Shape438 = x3d.Shape()
Shape438.USE = "HAnimSiteShape"
Shape438.bboxCenter = [0,0,0]
Shape438.bboxDisplay = False
Shape438.bboxSize = [-1,-1,-1]
Shape438.visible = True

HAnimSite436.children.append(Shape438)

HAnimSegment435.children.append(HAnimSite436)
HAnimSite439 = x3d.HAnimSite()
HAnimSite439.DEF = "STD_Site_r_gonion_pt"
HAnimSite439.bboxCenter = [0,0,0]
HAnimSite439.bboxDisplay = False
HAnimSite439.bboxSize = [-1,-1,-1]
HAnimSite439.name = "r_gonion_pt"
HAnimSite439.translation = [-0.0520,1.5529,0.0347]
HAnimSite439.visible = True
TouchSensor440 = x3d.TouchSensor()
TouchSensor440.description = "HAnimSite r_gonion_pt"

HAnimSite439.children.append(TouchSensor440)
Shape441 = x3d.Shape()
Shape441.USE = "HAnimSiteShape"
Shape441.bboxCenter = [0,0,0]
Shape441.bboxDisplay = False
Shape441.bboxSize = [-1,-1,-1]
Shape441.visible = True

HAnimSite439.children.append(Shape441)

HAnimSegment435.children.append(HAnimSite439)
HAnimSite442 = x3d.HAnimSite()
HAnimSite442.DEF = "STD_Site_l_gonion_pt"
HAnimSite442.bboxCenter = [0,0,0]
HAnimSite442.bboxDisplay = False
HAnimSite442.bboxSize = [-1,-1,-1]
HAnimSite442.name = "l_gonion_pt"
HAnimSite442.translation = [0.0631,1.5530,0.0330]
HAnimSite442.visible = True
TouchSensor443 = x3d.TouchSensor()
TouchSensor443.description = "HAnimSite l_gonion_pt"

HAnimSite442.children.append(TouchSensor443)
Shape444 = x3d.Shape()
Shape444.USE = "HAnimSiteShape"
Shape444.bboxCenter = [0,0,0]
Shape444.bboxDisplay = False
Shape444.bboxSize = [-1,-1,-1]
Shape444.visible = True

HAnimSite442.children.append(Shape444)

HAnimSegment435.children.append(HAnimSite442)
HAnimSite445 = x3d.HAnimSite()
HAnimSite445.DEF = "STD_Site_supramenton_pt"
HAnimSite445.bboxCenter = [0,0,0]
HAnimSite445.bboxDisplay = False
HAnimSite445.bboxSize = [-1,-1,-1]
HAnimSite445.name = "supramenton_pt"
HAnimSite445.translation = [0.0061,1.5410,0.0805]
HAnimSite445.visible = True
TouchSensor446 = x3d.TouchSensor()
TouchSensor446.description = "HAnimSite supramenton_pt"

HAnimSite445.children.append(TouchSensor446)
Shape447 = x3d.Shape()
Shape447.USE = "HAnimSiteShape"
Shape447.bboxCenter = [0,0,0]
Shape447.bboxDisplay = False
Shape447.bboxSize = [-1,-1,-1]
Shape447.visible = True

HAnimSite445.children.append(Shape447)

HAnimSegment435.children.append(HAnimSite445)

HAnimJoint434.children.append(HAnimSegment435)

HAnimJoint432.children.append(HAnimJoint434)

HAnimJoint430.children.append(HAnimJoint432)

HAnimJoint428.children.append(HAnimJoint430)

HAnimJoint426.children.append(HAnimJoint428)

HAnimJoint424.children.append(HAnimJoint426)

HAnimJoint422.children.append(HAnimJoint424)

HAnimJoint387.children.append(HAnimJoint422)

HAnimJoint385.children.append(HAnimJoint387)

HAnimJoint380.children.append(HAnimJoint385)

HAnimJoint378.children.append(HAnimJoint380)

HAnimJoint376.children.append(HAnimJoint378)

HAnimJoint374.children.append(HAnimJoint376)

HAnimJoint372.children.append(HAnimJoint374)

HAnimJoint364.children.append(HAnimJoint372)

HAnimJoint356.children.append(HAnimJoint364)
HAnimJoint448 = x3d.HAnimJoint()
HAnimJoint448.DEF = "STD_Joint_l_sternoclavicular"
HAnimJoint448.bboxCenter = [0,0,0]
HAnimJoint448.bboxDisplay = False
HAnimJoint448.bboxSize = [-1,-1,-1]
HAnimJoint448.center = [0.0820,1.4488,-0.0353]
HAnimJoint448.name = "l_sternoclavicular"
HAnimJoint448.visible = True
HAnimSegment449 = x3d.HAnimSegment()
HAnimSegment449.DEF = "STD_Segment_l_clavicle"
HAnimSegment449.bboxDisplay = False
HAnimSegment449.name = "l_clavicle"
HAnimSegment449.visible = True
HAnimSite450 = x3d.HAnimSite()
HAnimSite450.DEF = "STD_Site_l_axilla_posterior_folds_pt"
HAnimSite450.bboxCenter = [0,0,0]
HAnimSite450.bboxDisplay = False
HAnimSite450.bboxSize = [-1,-1,-1]
HAnimSite450.name = "l_axilla_posterior_folds_pt"
HAnimSite450.visible = True
TouchSensor451 = x3d.TouchSensor()
TouchSensor451.description = "HAnimSite l_axilla_posterior_folds_pt"

HAnimSite450.children.append(TouchSensor451)
Shape452 = x3d.Shape()
Shape452.USE = "HAnimSiteShape"
Shape452.bboxCenter = [0,0,0]
Shape452.bboxDisplay = False
Shape452.bboxSize = [-1,-1,-1]
Shape452.visible = True

HAnimSite450.children.append(Shape452)

HAnimSegment449.children.append(HAnimSite450)
HAnimSite453 = x3d.HAnimSite()
HAnimSite453.DEF = "STD_Site_l_acromion_pt"
HAnimSite453.bboxCenter = [0,0,0]
HAnimSite453.bboxDisplay = False
HAnimSite453.bboxSize = [-1,-1,-1]
HAnimSite453.name = "l_acromion_pt"
HAnimSite453.translation = [0.2032,1.4760,-0.0490]
HAnimSite453.visible = True
TouchSensor454 = x3d.TouchSensor()
TouchSensor454.description = "HAnimSite l_acromion_pt"

HAnimSite453.children.append(TouchSensor454)
Shape455 = x3d.Shape()
Shape455.USE = "HAnimSiteShape"
Shape455.bboxCenter = [0,0,0]
Shape455.bboxDisplay = False
Shape455.bboxSize = [-1,-1,-1]
Shape455.visible = True

HAnimSite453.children.append(Shape455)

HAnimSegment449.children.append(HAnimSite453)
HAnimSite456 = x3d.HAnimSite()
HAnimSite456.DEF = "STD_Site_l_axilla_distal_pt"
HAnimSite456.bboxCenter = [0,0,0]
HAnimSite456.bboxDisplay = False
HAnimSite456.bboxSize = [-1,-1,-1]
HAnimSite456.name = "l_axilla_distal_pt"
HAnimSite456.translation = [0.1706,1.4072,-0.0875]
HAnimSite456.visible = True
TouchSensor457 = x3d.TouchSensor()
TouchSensor457.description = "HAnimSite l_axilla_distal_pt"

HAnimSite456.children.append(TouchSensor457)
Shape458 = x3d.Shape()
Shape458.USE = "HAnimSiteShape"
Shape458.bboxCenter = [0,0,0]
Shape458.bboxDisplay = False
Shape458.bboxSize = [-1,-1,-1]
Shape458.visible = True

HAnimSite456.children.append(Shape458)

HAnimSegment449.children.append(HAnimSite456)
HAnimSite459 = x3d.HAnimSite()
HAnimSite459.DEF = "STD_Site_l_axilla_proximal_pt"
HAnimSite459.bboxCenter = [0,0,0]
HAnimSite459.bboxDisplay = False
HAnimSite459.bboxSize = [-1,-1,-1]
HAnimSite459.name = "l_axilla_proximal_pt"
HAnimSite459.translation = [0.1777,1.4065,-0.0075]
HAnimSite459.visible = True
TouchSensor460 = x3d.TouchSensor()
TouchSensor460.description = "HAnimSite l_axilla_proximal_pt"

HAnimSite459.children.append(TouchSensor460)
Shape461 = x3d.Shape()
Shape461.USE = "HAnimSiteShape"
Shape461.bboxCenter = [0,0,0]
Shape461.bboxDisplay = False
Shape461.bboxSize = [-1,-1,-1]
Shape461.visible = True

HAnimSite459.children.append(Shape461)

HAnimSegment449.children.append(HAnimSite459)
HAnimSite462 = x3d.HAnimSite()
HAnimSite462.DEF = "STD_Site_l_clavicale_pt"
HAnimSite462.bboxCenter = [0,0,0]
HAnimSite462.bboxDisplay = False
HAnimSite462.bboxSize = [-1,-1,-1]
HAnimSite462.name = "l_clavicale_pt"
HAnimSite462.translation = [0.0271,1.4943,0.0394]
HAnimSite462.visible = True
TouchSensor463 = x3d.TouchSensor()
TouchSensor463.description = "HAnimSite l_clavicale_pt"

HAnimSite462.children.append(TouchSensor463)
Shape464 = x3d.Shape()
Shape464.USE = "HAnimSiteShape"
Shape464.bboxCenter = [0,0,0]
Shape464.bboxDisplay = False
Shape464.bboxSize = [-1,-1,-1]
Shape464.visible = True

HAnimSite462.children.append(Shape464)

HAnimSegment449.children.append(HAnimSite462)

HAnimJoint448.children.append(HAnimSegment449)
HAnimJoint465 = x3d.HAnimJoint()
HAnimJoint465.DEF = "STD_Joint_l_acromioclavicular"
HAnimJoint465.bboxCenter = [0,0,0]
HAnimJoint465.bboxDisplay = False
HAnimJoint465.bboxSize = [-1,-1,-1]
HAnimJoint465.center = [0.0962,1.4269,-0.0424]
HAnimJoint465.name = "l_acromioclavicular"
HAnimJoint465.visible = True
HAnimSegment466 = x3d.HAnimSegment()
HAnimSegment466.DEF = "STD_Segment_l_scapula"
HAnimSegment466.bboxDisplay = False
HAnimSegment466.name = "l_scapula"
HAnimSegment466.visible = True

HAnimJoint465.children.append(HAnimSegment466)
HAnimJoint467 = x3d.HAnimJoint()
HAnimJoint467.DEF = "STD_Joint_l_shoulder"
HAnimJoint467.bboxCenter = [0,0,0]
HAnimJoint467.bboxDisplay = False
HAnimJoint467.bboxSize = [-1,-1,-1]
HAnimJoint467.center = [0.2029,1.4376,-0.0387]
HAnimJoint467.name = "l_shoulder"
HAnimJoint467.visible = True
HAnimSegment468 = x3d.HAnimSegment()
HAnimSegment468.DEF = "STD_Segment_l_upperarm"
HAnimSegment468.bboxDisplay = False
HAnimSegment468.name = "l_upperarm"
HAnimSegment468.visible = True
HAnimSite469 = x3d.HAnimSite()
HAnimSite469.DEF = "STD_Site_l_humeral_lateral_epicondyles_pt"
HAnimSite469.bboxCenter = [0,0,0]
HAnimSite469.bboxDisplay = False
HAnimSite469.bboxSize = [-1,-1,-1]
HAnimSite469.name = "l_humeral_lateral_epicondyles_pt"
HAnimSite469.translation = [0.2280,1.1482,-0.1100]
HAnimSite469.visible = True
TouchSensor470 = x3d.TouchSensor()
TouchSensor470.description = "HAnimSite l_humeral_lateral_epicondyles_pt"

HAnimSite469.children.append(TouchSensor470)
Shape471 = x3d.Shape()
Shape471.USE = "HAnimSiteShape"
Shape471.bboxCenter = [0,0,0]
Shape471.bboxDisplay = False
Shape471.bboxSize = [-1,-1,-1]
Shape471.visible = True

HAnimSite469.children.append(Shape471)

HAnimSegment468.children.append(HAnimSite469)
HAnimSite472 = x3d.HAnimSite()
HAnimSite472.DEF = "STD_Site_l_bideltoid_pt"
HAnimSite472.bboxCenter = [0,0,0]
HAnimSite472.bboxDisplay = False
HAnimSite472.bboxSize = [-1,-1,-1]
HAnimSite472.name = "l_bideltoid_pt"
HAnimSite472.visible = True
TouchSensor473 = x3d.TouchSensor()
TouchSensor473.description = "HAnimSite l_bideltoid_pt"

HAnimSite472.children.append(TouchSensor473)
Shape474 = x3d.Shape()
Shape474.USE = "HAnimSiteShape"
Shape474.bboxCenter = [0,0,0]
Shape474.bboxDisplay = False
Shape474.bboxSize = [-1,-1,-1]
Shape474.visible = True

HAnimSite472.children.append(Shape474)

HAnimSegment468.children.append(HAnimSite472)

HAnimJoint467.children.append(HAnimSegment468)
HAnimJoint475 = x3d.HAnimJoint()
HAnimJoint475.DEF = "STD_Joint_l_elbow"
HAnimJoint475.bboxCenter = [0,0,0]
HAnimJoint475.bboxDisplay = False
HAnimJoint475.bboxSize = [-1,-1,-1]
HAnimJoint475.center = [0.2014,1.1357,-0.0682]
HAnimJoint475.name = "l_elbow"
HAnimJoint475.visible = True
HAnimSegment476 = x3d.HAnimSegment()
HAnimSegment476.DEF = "STD_Segment_l_forearm"
HAnimSegment476.bboxDisplay = False
HAnimSegment476.name = "l_forearm"
HAnimSegment476.visible = True
HAnimSite477 = x3d.HAnimSite()
HAnimSite477.DEF = "STD_Site_l_olecranon_pt"
HAnimSite477.bboxCenter = [0,0,0]
HAnimSite477.bboxDisplay = False
HAnimSite477.bboxSize = [-1,-1,-1]
HAnimSite477.name = "l_olecranon_pt"
HAnimSite477.translation = [-0.1962,1.1375,-0.1123]
HAnimSite477.visible = True
TouchSensor478 = x3d.TouchSensor()
TouchSensor478.description = "HAnimSite l_olecranon_pt"

HAnimSite477.children.append(TouchSensor478)
Shape479 = x3d.Shape()
Shape479.USE = "HAnimSiteShape"
Shape479.bboxCenter = [0,0,0]
Shape479.bboxDisplay = False
Shape479.bboxSize = [-1,-1,-1]
Shape479.visible = True

HAnimSite477.children.append(Shape479)

HAnimSegment476.children.append(HAnimSite477)
HAnimSite480 = x3d.HAnimSite()
HAnimSite480.DEF = "STD_Site_l_radiale_pt"
HAnimSite480.bboxCenter = [0,0,0]
HAnimSite480.bboxDisplay = False
HAnimSite480.bboxSize = [-1,-1,-1]
HAnimSite480.name = "l_radiale_pt"
HAnimSite480.translation = [0.2182,1.1212,-0.1167]
HAnimSite480.visible = True
TouchSensor481 = x3d.TouchSensor()
TouchSensor481.description = "HAnimSite l_radiale_pt"

HAnimSite480.children.append(TouchSensor481)
Shape482 = x3d.Shape()
Shape482.USE = "HAnimSiteShape"
Shape482.bboxCenter = [0,0,0]
Shape482.bboxDisplay = False
Shape482.bboxSize = [-1,-1,-1]
Shape482.visible = True

HAnimSite480.children.append(Shape482)

HAnimSegment476.children.append(HAnimSite480)
HAnimSite483 = x3d.HAnimSite()
HAnimSite483.DEF = "STD_Site_l_radial_styloid_pt"
HAnimSite483.bboxCenter = [0,0,0]
HAnimSite483.bboxDisplay = False
HAnimSite483.bboxSize = [-1,-1,-1]
HAnimSite483.name = "l_radial_styloid_pt"
HAnimSite483.translation = [0.1901,0.8645,-0.0415]
HAnimSite483.visible = True
TouchSensor484 = x3d.TouchSensor()
TouchSensor484.description = "HAnimSite l_radial_styloid_pt"

HAnimSite483.children.append(TouchSensor484)
Shape485 = x3d.Shape()
Shape485.USE = "HAnimSiteShape"
Shape485.bboxCenter = [0,0,0]
Shape485.bboxDisplay = False
Shape485.bboxSize = [-1,-1,-1]
Shape485.visible = True

HAnimSite483.children.append(Shape485)

HAnimSegment476.children.append(HAnimSite483)
HAnimSite486 = x3d.HAnimSite()
HAnimSite486.DEF = "STD_Site_l_humeral_medial_epicondyles_pt"
HAnimSite486.bboxCenter = [0,0,0]
HAnimSite486.bboxDisplay = False
HAnimSite486.bboxSize = [-1,-1,-1]
HAnimSite486.name = "l_humeral_medial_epicondyles_pt"
HAnimSite486.translation = [0.1735,1.1272,-0.1113]
HAnimSite486.visible = True
TouchSensor487 = x3d.TouchSensor()
TouchSensor487.description = "HAnimSite l_humeral_medial_epicondyles_pt"

HAnimSite486.children.append(TouchSensor487)
Shape488 = x3d.Shape()
Shape488.USE = "HAnimSiteShape"
Shape488.bboxCenter = [0,0,0]
Shape488.bboxDisplay = False
Shape488.bboxSize = [-1,-1,-1]
Shape488.visible = True

HAnimSite486.children.append(Shape488)

HAnimSegment476.children.append(HAnimSite486)

HAnimJoint475.children.append(HAnimSegment476)
HAnimJoint489 = x3d.HAnimJoint()
HAnimJoint489.DEF = "STD_Joint_l_radiocarpal"
HAnimJoint489.bboxCenter = [0,0,0]
HAnimJoint489.bboxDisplay = False
HAnimJoint489.bboxSize = [-1,-1,-1]
HAnimJoint489.center = [0.1984,0.8663,-0.0583]
HAnimJoint489.name = "l_radiocarpal"
HAnimJoint489.visible = True
HAnimSegment490 = x3d.HAnimSegment()
HAnimSegment490.DEF = "STD_Segment_l_carpal"
HAnimSegment490.bboxDisplay = False
HAnimSegment490.name = "l_carpal"
HAnimSegment490.visible = True
HAnimSite491 = x3d.HAnimSite()
HAnimSite491.DEF = "STD_Site_l_ulnar_styloid_pt"
HAnimSite491.bboxCenter = [0,0,0]
HAnimSite491.bboxDisplay = False
HAnimSite491.bboxSize = [-1,-1,-1]
HAnimSite491.name = "l_ulnar_styloid_pt"
HAnimSite491.translation = [-0.2142,0.8529,-0.0648]
HAnimSite491.visible = True
TouchSensor492 = x3d.TouchSensor()
TouchSensor492.description = "HAnimSite l_ulnar_styloid_pt"

HAnimSite491.children.append(TouchSensor492)
Shape493 = x3d.Shape()
Shape493.USE = "HAnimSiteShape"
Shape493.bboxCenter = [0,0,0]
Shape493.bboxDisplay = False
Shape493.bboxSize = [-1,-1,-1]
Shape493.visible = True

HAnimSite491.children.append(Shape493)

HAnimSegment490.children.append(HAnimSite491)

HAnimJoint489.children.append(HAnimSegment490)
HAnimJoint494 = x3d.HAnimJoint()
HAnimJoint494.DEF = "STD_Joint_l_midcarpal_1"
HAnimJoint494.bboxCenter = [0,0,0]
HAnimJoint494.bboxDisplay = False
HAnimJoint494.bboxSize = [-1,-1,-1]
HAnimJoint494.name = "l_midcarpal_1"
HAnimJoint494.visible = True
HAnimSegment495 = x3d.HAnimSegment()
HAnimSegment495.DEF = "STD_Segment_l_trapezium"
HAnimSegment495.bboxDisplay = False
HAnimSegment495.name = "l_trapezium"
HAnimSegment495.visible = True

HAnimJoint494.children.append(HAnimSegment495)
HAnimJoint496 = x3d.HAnimJoint()
HAnimJoint496.DEF = "STD_Joint_l_carpometacarpal_1"
HAnimJoint496.bboxCenter = [0,0,0]
HAnimJoint496.bboxDisplay = False
HAnimJoint496.bboxSize = [-1,-1,-1]
HAnimJoint496.center = [0.1924,0.8472,-0.0534]
HAnimJoint496.name = "l_carpometacarpal_1"
HAnimJoint496.visible = True
HAnimSegment497 = x3d.HAnimSegment()
HAnimSegment497.DEF = "STD_Segment_l_metacarpal_1"
HAnimSegment497.bboxDisplay = False
HAnimSegment497.name = "l_metacarpal_1"
HAnimSegment497.visible = True

HAnimJoint496.children.append(HAnimSegment497)
HAnimJoint498 = x3d.HAnimJoint()
HAnimJoint498.DEF = "STD_Joint_l_metacarpophalangeal_1"
HAnimJoint498.bboxCenter = [0,0,0]
HAnimJoint498.bboxDisplay = False
HAnimJoint498.bboxSize = [-1,-1,-1]
HAnimJoint498.center = [0.1951,0.8226,0.0246]
HAnimJoint498.name = "l_metacarpophalangeal_1"
HAnimJoint498.visible = True
HAnimSegment499 = x3d.HAnimSegment()
HAnimSegment499.DEF = "STD_Segment_l_carpal_proximal_phalanx_1"
HAnimSegment499.bboxDisplay = False
HAnimSegment499.name = "l_carpal_proximal_phalanx_1"
HAnimSegment499.visible = True

HAnimJoint498.children.append(HAnimSegment499)
HAnimJoint500 = x3d.HAnimJoint()
HAnimJoint500.DEF = "STD_Joint_l_carpal_interphalangeal_1"
HAnimJoint500.bboxCenter = [0,0,0]
HAnimJoint500.bboxDisplay = False
HAnimJoint500.bboxSize = [-1,-1,-1]
HAnimJoint500.center = [0.1955,0.8159,0.0464]
HAnimJoint500.name = "l_carpal_interphalangeal_1"
HAnimJoint500.visible = True
HAnimSegment501 = x3d.HAnimSegment()
HAnimSegment501.DEF = "STD_Segment_l_carpal_distal_phalanx_1"
HAnimSegment501.bboxDisplay = False
HAnimSegment501.name = "l_carpal_distal_phalanx_1"
HAnimSegment501.visible = True
HAnimSite502 = x3d.HAnimSite()
HAnimSite502.DEF = "STD_Site_l_carpal_distal_phalanx_1_pt"
HAnimSite502.bboxCenter = [0,0,0]
HAnimSite502.bboxDisplay = False
HAnimSite502.bboxSize = [-1,-1,-1]
HAnimSite502.name = "l_carpal_distal_phalanx_1_pt"
HAnimSite502.visible = True
TouchSensor503 = x3d.TouchSensor()
TouchSensor503.description = "HAnimSite l_carpal_distal_phalanx_1_pt"

HAnimSite502.children.append(TouchSensor503)
Shape504 = x3d.Shape()
Shape504.USE = "HAnimSiteShape"
Shape504.bboxCenter = [0,0,0]
Shape504.bboxDisplay = False
Shape504.bboxSize = [-1,-1,-1]
Shape504.visible = True

HAnimSite502.children.append(Shape504)

HAnimSegment501.children.append(HAnimSite502)

HAnimJoint500.children.append(HAnimSegment501)

HAnimJoint498.children.append(HAnimJoint500)

HAnimJoint496.children.append(HAnimJoint498)

HAnimJoint494.children.append(HAnimJoint496)

HAnimJoint489.children.append(HAnimJoint494)
HAnimJoint505 = x3d.HAnimJoint()
HAnimJoint505.DEF = "STD_Joint_l_midcarpal_2"
HAnimJoint505.bboxCenter = [0,0,0]
HAnimJoint505.bboxDisplay = False
HAnimJoint505.bboxSize = [-1,-1,-1]
HAnimJoint505.name = "l_midcarpal_2"
HAnimJoint505.visible = True
HAnimSegment506 = x3d.HAnimSegment()
HAnimSegment506.DEF = "STD_Segment_l_trapezoid"
HAnimSegment506.bboxDisplay = False
HAnimSegment506.name = "l_trapezoid"
HAnimSegment506.visible = True

HAnimJoint505.children.append(HAnimSegment506)
HAnimJoint507 = x3d.HAnimJoint()
HAnimJoint507.DEF = "STD_Joint_l_carpometacarpal_2"
HAnimJoint507.bboxCenter = [0,0,0]
HAnimJoint507.bboxDisplay = False
HAnimJoint507.bboxSize = [-1,-1,-1]
HAnimJoint507.center = [0.1983,0.8024,-0.0280]
HAnimJoint507.name = "l_carpometacarpal_2"
HAnimJoint507.visible = True
HAnimSegment508 = x3d.HAnimSegment()
HAnimSegment508.DEF = "STD_Segment_l_metacarpal_2"
HAnimSegment508.bboxDisplay = False
HAnimSegment508.name = "l_metacarpal_2"
HAnimSegment508.visible = True
HAnimSite509 = x3d.HAnimSite()
HAnimSite509.DEF = "STD_Site_l_metacarpal_phalanx_2_pt"
HAnimSite509.bboxCenter = [0,0,0]
HAnimSite509.bboxDisplay = False
HAnimSite509.bboxSize = [-1,-1,-1]
HAnimSite509.name = "l_metacarpal_phalanx_2_pt"
HAnimSite509.translation = [0.2009,0.8139,-0.0237]
HAnimSite509.visible = True
TouchSensor510 = x3d.TouchSensor()
TouchSensor510.description = "HAnimSite l_metacarpal_phalanx_2_pt"

HAnimSite509.children.append(TouchSensor510)
Shape511 = x3d.Shape()
Shape511.USE = "HAnimSiteShape"
Shape511.bboxCenter = [0,0,0]
Shape511.bboxDisplay = False
Shape511.bboxSize = [-1,-1,-1]
Shape511.visible = True

HAnimSite509.children.append(Shape511)

HAnimSegment508.children.append(HAnimSite509)

HAnimJoint507.children.append(HAnimSegment508)
HAnimJoint512 = x3d.HAnimJoint()
HAnimJoint512.DEF = "STD_Joint_l_metacarpophalangeal_2"
HAnimJoint512.bboxCenter = [0,0,0]
HAnimJoint512.bboxDisplay = False
HAnimJoint512.bboxSize = [-1,-1,-1]
HAnimJoint512.center = [0.1983,0.7815,-0.0280]
HAnimJoint512.name = "l_metacarpophalangeal_2"
HAnimJoint512.visible = True
HAnimSegment513 = x3d.HAnimSegment()
HAnimSegment513.DEF = "STD_Segment_l_carpal_proximal_phalanx_2"
HAnimSegment513.bboxDisplay = False
HAnimSegment513.name = "l_carpal_proximal_phalanx_2"
HAnimSegment513.visible = True

HAnimJoint512.children.append(HAnimSegment513)
HAnimJoint514 = x3d.HAnimJoint()
HAnimJoint514.DEF = "STD_Joint_l_carpal_proximal_interphalangeal_2"
HAnimJoint514.bboxCenter = [0,0,0]
HAnimJoint514.bboxDisplay = False
HAnimJoint514.bboxSize = [-1,-1,-1]
HAnimJoint514.center = [0.2017,0.7363,-0.0248]
HAnimJoint514.name = "l_carpal_proximal_interphalangeal_2"
HAnimJoint514.visible = True
HAnimSegment515 = x3d.HAnimSegment()
HAnimSegment515.DEF = "STD_Segment_l_carpal_middle_phalanx_2"
HAnimSegment515.bboxDisplay = False
HAnimSegment515.name = "l_carpal_middle_phalanx_2"
HAnimSegment515.visible = True

HAnimJoint514.children.append(HAnimSegment515)
HAnimJoint516 = x3d.HAnimJoint()
HAnimJoint516.DEF = "STD_Joint_l_carpal_distal_interphalangeal_2"
HAnimJoint516.bboxCenter = [0,0,0]
HAnimJoint516.bboxDisplay = False
HAnimJoint516.bboxSize = [-1,-1,-1]
HAnimJoint516.center = [0.2028,0.7139,-0.0236]
HAnimJoint516.name = "l_carpal_distal_interphalangeal_2"
HAnimJoint516.visible = True
HAnimSegment517 = x3d.HAnimSegment()
HAnimSegment517.DEF = "STD_Segment_l_carpal_distal_phalanx_2"
HAnimSegment517.bboxDisplay = False
HAnimSegment517.name = "l_carpal_distal_phalanx_2"
HAnimSegment517.visible = True
HAnimSite518 = x3d.HAnimSite()
HAnimSite518.DEF = "STD_Site_l_dactylion_pt"
HAnimSite518.bboxCenter = [0,0,0]
HAnimSite518.bboxDisplay = False
HAnimSite518.bboxSize = [-1,-1,-1]
HAnimSite518.name = "l_dactylion_pt"
HAnimSite518.translation = [0.2056,0.6743,-0.0482]
HAnimSite518.visible = True
TouchSensor519 = x3d.TouchSensor()
TouchSensor519.description = "HAnimSite l_dactylion_pt"

HAnimSite518.children.append(TouchSensor519)
Shape520 = x3d.Shape()
Shape520.USE = "HAnimSiteShape"
Shape520.bboxCenter = [0,0,0]
Shape520.bboxDisplay = False
Shape520.bboxSize = [-1,-1,-1]
Shape520.visible = True

HAnimSite518.children.append(Shape520)

HAnimSegment517.children.append(HAnimSite518)
HAnimSite521 = x3d.HAnimSite()
HAnimSite521.DEF = "STD_Site_l_carpal_distal_phalanx_2_pt"
HAnimSite521.bboxCenter = [0,0,0]
HAnimSite521.bboxDisplay = False
HAnimSite521.bboxSize = [-1,-1,-1]
HAnimSite521.name = "l_carpal_distal_phalanx_2_pt"
HAnimSite521.visible = True
TouchSensor522 = x3d.TouchSensor()
TouchSensor522.description = "HAnimSite l_carpal_distal_phalanx_2_pt"

HAnimSite521.children.append(TouchSensor522)
Shape523 = x3d.Shape()
Shape523.USE = "HAnimSiteShape"
Shape523.bboxCenter = [0,0,0]
Shape523.bboxDisplay = False
Shape523.bboxSize = [-1,-1,-1]
Shape523.visible = True

HAnimSite521.children.append(Shape523)

HAnimSegment517.children.append(HAnimSite521)

HAnimJoint516.children.append(HAnimSegment517)

HAnimJoint514.children.append(HAnimJoint516)

HAnimJoint512.children.append(HAnimJoint514)

HAnimJoint507.children.append(HAnimJoint512)

HAnimJoint505.children.append(HAnimJoint507)

HAnimJoint489.children.append(HAnimJoint505)
HAnimJoint524 = x3d.HAnimJoint()
HAnimJoint524.DEF = "STD_Joint_l_midcarpal_3"
HAnimJoint524.bboxCenter = [0,0,0]
HAnimJoint524.bboxDisplay = False
HAnimJoint524.bboxSize = [-1,-1,-1]
HAnimJoint524.name = "l_midcarpal_3"
HAnimJoint524.visible = True
HAnimSegment525 = x3d.HAnimSegment()
HAnimSegment525.DEF = "STD_Segment_l_capitate"
HAnimSegment525.bboxDisplay = False
HAnimSegment525.name = "l_capitate"
HAnimSegment525.visible = True

HAnimJoint524.children.append(HAnimSegment525)
HAnimJoint526 = x3d.HAnimJoint()
HAnimJoint526.DEF = "STD_Joint_l_carpometacarpal_3"
HAnimJoint526.bboxCenter = [0,0,0]
HAnimJoint526.bboxDisplay = False
HAnimJoint526.bboxSize = [-1,-1,-1]
HAnimJoint526.center = [0.1987,0.8029,-0.0530]
HAnimJoint526.name = "l_carpometacarpal_3"
HAnimJoint526.visible = True
HAnimSegment527 = x3d.HAnimSegment()
HAnimSegment527.DEF = "STD_Segment_l_metacarpal_3"
HAnimSegment527.bboxDisplay = False
HAnimSegment527.name = "l_metacarpal_3"
HAnimSegment527.visible = True
HAnimSite528 = x3d.HAnimSite()
HAnimSite528.DEF = "STD_Site_l_metacarpal_phalanx_3_pt"
HAnimSite528.bboxCenter = [0,0,0]
HAnimSite528.bboxDisplay = False
HAnimSite528.bboxSize = [-1,-1,-1]
HAnimSite528.name = "l_metacarpal_phalanx_3_pt"
HAnimSite528.visible = True
TouchSensor529 = x3d.TouchSensor()
TouchSensor529.description = "HAnimSite l_metacarpal_phalanx_3_pt"

HAnimSite528.children.append(TouchSensor529)
Shape530 = x3d.Shape()
Shape530.USE = "HAnimSiteShape"
Shape530.bboxCenter = [0,0,0]
Shape530.bboxDisplay = False
Shape530.bboxSize = [-1,-1,-1]
Shape530.visible = True

HAnimSite528.children.append(Shape530)

HAnimSegment527.children.append(HAnimSite528)

HAnimJoint526.children.append(HAnimSegment527)
HAnimJoint531 = x3d.HAnimJoint()
HAnimJoint531.DEF = "STD_Joint_l_metacarpophalangeal_3"
HAnimJoint531.bboxCenter = [0,0,0]
HAnimJoint531.bboxDisplay = False
HAnimJoint531.bboxSize = [-1,-1,-1]
HAnimJoint531.center = [0.1987,0.7818,-0.0530]
HAnimJoint531.name = "l_metacarpophalangeal_3"
HAnimJoint531.visible = True
HAnimSegment532 = x3d.HAnimSegment()
HAnimSegment532.DEF = "STD_Segment_l_carpal_proximal_phalanx_3"
HAnimSegment532.bboxDisplay = False
HAnimSegment532.name = "l_carpal_proximal_phalanx_3"
HAnimSegment532.visible = True

HAnimJoint531.children.append(HAnimSegment532)
HAnimJoint533 = x3d.HAnimJoint()
HAnimJoint533.DEF = "STD_Joint_l_carpal_proximal_interphalangeal_3"
HAnimJoint533.bboxCenter = [0,0,0]
HAnimJoint533.bboxDisplay = False
HAnimJoint533.bboxSize = [-1,-1,-1]
HAnimJoint533.center = [0.2013,0.7273,-0.0503]
HAnimJoint533.name = "l_carpal_proximal_interphalangeal_3"
HAnimJoint533.visible = True
HAnimSegment534 = x3d.HAnimSegment()
HAnimSegment534.DEF = "STD_Segment_l_carpal_middle_phalanx_3"
HAnimSegment534.bboxDisplay = False
HAnimSegment534.name = "l_carpal_middle_phalanx_3"
HAnimSegment534.visible = True

HAnimJoint533.children.append(HAnimSegment534)
HAnimJoint535 = x3d.HAnimJoint()
HAnimJoint535.DEF = "STD_Joint_l_carpal_distal_interphalangeal_3"
HAnimJoint535.bboxCenter = [0,0,0]
HAnimJoint535.bboxDisplay = False
HAnimJoint535.bboxSize = [-1,-1,-1]
HAnimJoint535.center = [0.2026,0.7011,-0.0494]
HAnimJoint535.name = "l_carpal_distal_interphalangeal_3"
HAnimJoint535.visible = True
HAnimSegment536 = x3d.HAnimSegment()
HAnimSegment536.DEF = "STD_Segment_l_carpal_distal_phalanx_3"
HAnimSegment536.bboxDisplay = False
HAnimSegment536.name = "l_carpal_distal_phalanx_3"
HAnimSegment536.visible = True
HAnimSite537 = x3d.HAnimSite()
HAnimSite537.DEF = "STD_Site_l_carpal_distal_phalanx_3_pt"
HAnimSite537.bboxCenter = [0,0,0]
HAnimSite537.bboxDisplay = False
HAnimSite537.bboxSize = [-1,-1,-1]
HAnimSite537.name = "l_carpal_distal_phalanx_3_pt"
HAnimSite537.visible = True
TouchSensor538 = x3d.TouchSensor()
TouchSensor538.description = "HAnimSite l_carpal_distal_phalanx_3_pt"

HAnimSite537.children.append(TouchSensor538)
Shape539 = x3d.Shape()
Shape539.USE = "HAnimSiteShape"
Shape539.bboxCenter = [0,0,0]
Shape539.bboxDisplay = False
Shape539.bboxSize = [-1,-1,-1]
Shape539.visible = True

HAnimSite537.children.append(Shape539)

HAnimSegment536.children.append(HAnimSite537)

HAnimJoint535.children.append(HAnimSegment536)

HAnimJoint533.children.append(HAnimJoint535)

HAnimJoint531.children.append(HAnimJoint533)

HAnimJoint526.children.append(HAnimJoint531)

HAnimJoint524.children.append(HAnimJoint526)

HAnimJoint489.children.append(HAnimJoint524)
HAnimJoint540 = x3d.HAnimJoint()
HAnimJoint540.DEF = "STD_Joint_l_midcarpal_4_5"
HAnimJoint540.bboxCenter = [0,0,0]
HAnimJoint540.bboxDisplay = False
HAnimJoint540.bboxSize = [-1,-1,-1]
HAnimJoint540.name = "l_midcarpal_4_5"
HAnimJoint540.visible = True
HAnimSegment541 = x3d.HAnimSegment()
HAnimSegment541.DEF = "STD_Segment_l_hamate"
HAnimSegment541.bboxDisplay = False
HAnimSegment541.name = "l_hamate"
HAnimSegment541.visible = True

HAnimJoint540.children.append(HAnimSegment541)
HAnimJoint542 = x3d.HAnimJoint()
HAnimJoint542.DEF = "STD_Joint_l_carpometacarpal_4"
HAnimJoint542.bboxCenter = [0,0,0]
HAnimJoint542.bboxDisplay = False
HAnimJoint542.bboxSize = [-1,-1,-1]
HAnimJoint542.center = [0.1956,0.8019,-0.0794]
HAnimJoint542.name = "l_carpometacarpal_4"
HAnimJoint542.visible = True
HAnimSegment543 = x3d.HAnimSegment()
HAnimSegment543.DEF = "STD_Segment_l_metacarpal_4"
HAnimSegment543.bboxDisplay = False
HAnimSegment543.name = "l_metacarpal_4"
HAnimSegment543.visible = True

HAnimJoint542.children.append(HAnimSegment543)
HAnimJoint544 = x3d.HAnimJoint()
HAnimJoint544.DEF = "STD_Joint_l_metacarpophalangeal_4"
HAnimJoint544.bboxCenter = [0,0,0]
HAnimJoint544.bboxDisplay = False
HAnimJoint544.bboxSize = [-1,-1,-1]
HAnimJoint544.center = [0.1956,0.7815,-0.0794]
HAnimJoint544.name = "l_metacarpophalangeal_4"
HAnimJoint544.visible = True
HAnimSegment545 = x3d.HAnimSegment()
HAnimSegment545.DEF = "STD_Segment_l_carpal_proximal_phalanx_4"
HAnimSegment545.bboxDisplay = False
HAnimSegment545.name = "l_carpal_proximal_phalanx_4"
HAnimSegment545.visible = True

HAnimJoint544.children.append(HAnimSegment545)
HAnimJoint546 = x3d.HAnimJoint()
HAnimJoint546.DEF = "STD_Joint_l_carpal_proximal_interphalangeal_4"
HAnimJoint546.bboxCenter = [0,0,0]
HAnimJoint546.bboxDisplay = False
HAnimJoint546.bboxSize = [-1,-1,-1]
HAnimJoint546.center = [0.1973,0.7287,-0.0777]
HAnimJoint546.name = "l_carpal_proximal_interphalangeal_4"
HAnimJoint546.visible = True
HAnimSegment547 = x3d.HAnimSegment()
HAnimSegment547.DEF = "STD_Segment_l_carpal_middle_phalanx_4"
HAnimSegment547.bboxDisplay = False
HAnimSegment547.name = "l_carpal_middle_phalanx_4"
HAnimSegment547.visible = True

HAnimJoint546.children.append(HAnimSegment547)
HAnimJoint548 = x3d.HAnimJoint()
HAnimJoint548.DEF = "STD_Joint_l_carpal_distal_interphalangeal_4"
HAnimJoint548.bboxCenter = [0,0,0]
HAnimJoint548.bboxDisplay = False
HAnimJoint548.bboxSize = [-1,-1,-1]
HAnimJoint548.center = [0.1983,0.7045,-0.0767]
HAnimJoint548.name = "l_carpal_distal_interphalangeal_4"
HAnimJoint548.visible = True
HAnimSegment549 = x3d.HAnimSegment()
HAnimSegment549.DEF = "STD_Segment_l_carpal_distal_phalanx_4"
HAnimSegment549.bboxDisplay = False
HAnimSegment549.name = "l_carpal_distal_phalanx_4"
HAnimSegment549.visible = True
HAnimSite550 = x3d.HAnimSite()
HAnimSite550.DEF = "STD_Site_l_carpal_distal_phalanx_4_pt"
HAnimSite550.bboxCenter = [0,0,0]
HAnimSite550.bboxDisplay = False
HAnimSite550.bboxSize = [-1,-1,-1]
HAnimSite550.name = "l_carpal_distal_phalanx_4_pt"
HAnimSite550.visible = True
TouchSensor551 = x3d.TouchSensor()
TouchSensor551.description = "HAnimSite l_carpal_distal_phalanx_4_pt"

HAnimSite550.children.append(TouchSensor551)
Shape552 = x3d.Shape()
Shape552.USE = "HAnimSiteShape"
Shape552.bboxCenter = [0,0,0]
Shape552.bboxDisplay = False
Shape552.bboxSize = [-1,-1,-1]
Shape552.visible = True

HAnimSite550.children.append(Shape552)

HAnimSegment549.children.append(HAnimSite550)

HAnimJoint548.children.append(HAnimSegment549)

HAnimJoint546.children.append(HAnimJoint548)

HAnimJoint544.children.append(HAnimJoint546)

HAnimJoint542.children.append(HAnimJoint544)

HAnimJoint540.children.append(HAnimJoint542)
HAnimJoint553 = x3d.HAnimJoint()
HAnimJoint553.DEF = "STD_Joint_l_carpometacarpal_5"
HAnimJoint553.bboxCenter = [0,0,0]
HAnimJoint553.bboxDisplay = False
HAnimJoint553.bboxSize = [-1,-1,-1]
HAnimJoint553.center = [0.1925,0.8066,-0.1036]
HAnimJoint553.name = "l_carpometacarpal_5"
HAnimJoint553.visible = True
HAnimSegment554 = x3d.HAnimSegment()
HAnimSegment554.DEF = "STD_Segment_l_metacarpal_5"
HAnimSegment554.bboxDisplay = False
HAnimSegment554.name = "l_metacarpal_5"
HAnimSegment554.visible = True
HAnimSite555 = x3d.HAnimSite()
HAnimSite555.DEF = "STD_Site_l_metacarpal_phalanx_5_pt"
HAnimSite555.bboxCenter = [0,0,0]
HAnimSite555.bboxDisplay = False
HAnimSite555.bboxSize = [-1,-1,-1]
HAnimSite555.name = "l_metacarpal_phalanx_5_pt"
HAnimSite555.translation = [0.1929,0.7860,-0.1122]
HAnimSite555.visible = True
TouchSensor556 = x3d.TouchSensor()
TouchSensor556.description = "HAnimSite l_metacarpal_phalanx_5_pt"

HAnimSite555.children.append(TouchSensor556)
Shape557 = x3d.Shape()
Shape557.USE = "HAnimSiteShape"
Shape557.bboxCenter = [0,0,0]
Shape557.bboxDisplay = False
Shape557.bboxSize = [-1,-1,-1]
Shape557.visible = True

HAnimSite555.children.append(Shape557)

HAnimSegment554.children.append(HAnimSite555)

HAnimJoint553.children.append(HAnimSegment554)
HAnimJoint558 = x3d.HAnimJoint()
HAnimJoint558.DEF = "STD_Joint_l_metacarpophalangeal_5"
HAnimJoint558.bboxCenter = [0,0,0]
HAnimJoint558.bboxDisplay = False
HAnimJoint558.bboxSize = [-1,-1,-1]
HAnimJoint558.center = [0.1925,0.7866,-0.1036]
HAnimJoint558.name = "l_metacarpophalangeal_5"
HAnimJoint558.visible = True
HAnimSegment559 = x3d.HAnimSegment()
HAnimSegment559.DEF = "STD_Segment_l_carpal_proximal_phalanx_5"
HAnimSegment559.bboxDisplay = False
HAnimSegment559.name = "l_carpal_proximal_phalanx_5"
HAnimSegment559.visible = True

HAnimJoint558.children.append(HAnimSegment559)
HAnimJoint560 = x3d.HAnimJoint()
HAnimJoint560.DEF = "STD_Joint_l_carpal_proximal_interphalangeal_5"
HAnimJoint560.bboxCenter = [0,0,0]
HAnimJoint560.bboxDisplay = False
HAnimJoint560.bboxSize = [-1,-1,-1]
HAnimJoint560.center = [0.1938,0.7452,-0.1024]
HAnimJoint560.name = "l_carpal_proximal_interphalangeal_5"
HAnimJoint560.visible = True
HAnimSegment561 = x3d.HAnimSegment()
HAnimSegment561.DEF = "STD_Segment_l_carpal_middle_phalanx_5"
HAnimSegment561.bboxDisplay = False
HAnimSegment561.name = "l_carpal_middle_phalanx_5"
HAnimSegment561.visible = True

HAnimJoint560.children.append(HAnimSegment561)
HAnimJoint562 = x3d.HAnimJoint()
HAnimJoint562.DEF = "STD_Joint_l_carpal_distal_interphalangeal_5"
HAnimJoint562.bboxCenter = [0,0,0]
HAnimJoint562.bboxDisplay = False
HAnimJoint562.bboxSize = [-1,-1,-1]
HAnimJoint562.center = [0.1948,0.7277,-0.1017]
HAnimJoint562.name = "l_carpal_distal_interphalangeal_5"
HAnimJoint562.visible = True
HAnimSegment563 = x3d.HAnimSegment()
HAnimSegment563.DEF = "STD_Segment_l_carpal_distal_phalanx_5"
HAnimSegment563.bboxDisplay = False
HAnimSegment563.name = "l_carpal_distal_phalanx_5"
HAnimSegment563.visible = True
HAnimSite564 = x3d.HAnimSite()
HAnimSite564.DEF = "STD_Site_l_carpal_distal_phalanx_5_pt"
HAnimSite564.bboxCenter = [0,0,0]
HAnimSite564.bboxDisplay = False
HAnimSite564.bboxSize = [-1,-1,-1]
HAnimSite564.name = "l_carpal_distal_phalanx_5_pt"
HAnimSite564.visible = True
TouchSensor565 = x3d.TouchSensor()
TouchSensor565.description = "HAnimSite l_carpal_distal_phalanx_5_pt"

HAnimSite564.children.append(TouchSensor565)
Shape566 = x3d.Shape()
Shape566.USE = "HAnimSiteShape"
Shape566.bboxCenter = [0,0,0]
Shape566.bboxDisplay = False
Shape566.bboxSize = [-1,-1,-1]
Shape566.visible = True

HAnimSite564.children.append(Shape566)

HAnimSegment563.children.append(HAnimSite564)

HAnimJoint562.children.append(HAnimSegment563)

HAnimJoint560.children.append(HAnimJoint562)

HAnimJoint558.children.append(HAnimJoint560)

HAnimJoint553.children.append(HAnimJoint558)

HAnimJoint540.children.append(HAnimJoint553)

HAnimJoint489.children.append(HAnimJoint540)

HAnimJoint475.children.append(HAnimJoint489)

HAnimJoint467.children.append(HAnimJoint475)

HAnimJoint465.children.append(HAnimJoint467)

HAnimJoint448.children.append(HAnimJoint465)

HAnimJoint356.children.append(HAnimJoint448)
HAnimJoint567 = x3d.HAnimJoint()
HAnimJoint567.DEF = "STD_Joint_r_sternoclavicular"
HAnimJoint567.bboxCenter = [0,0,0]
HAnimJoint567.bboxDisplay = False
HAnimJoint567.bboxSize = [-1,-1,-1]
HAnimJoint567.center = [-0.0694,1.4600,-0.0330]
HAnimJoint567.name = "r_sternoclavicular"
HAnimJoint567.visible = True
HAnimSegment568 = x3d.HAnimSegment()
HAnimSegment568.DEF = "STD_Segment_r_clavicle"
HAnimSegment568.bboxDisplay = False
HAnimSegment568.name = "r_clavicle"
HAnimSegment568.visible = True
HAnimSite569 = x3d.HAnimSite()
HAnimSite569.DEF = "STD_Site_r_axilla_distal_pt"
HAnimSite569.bboxCenter = [0,0,0]
HAnimSite569.bboxDisplay = False
HAnimSite569.bboxSize = [-1,-1,-1]
HAnimSite569.name = "r_axilla_distal_pt"
HAnimSite569.translation = [-0.1603,1.4098,-0.0826]
HAnimSite569.visible = True
TouchSensor570 = x3d.TouchSensor()
TouchSensor570.description = "HAnimSite r_axilla_distal_pt"

HAnimSite569.children.append(TouchSensor570)
Shape571 = x3d.Shape()
Shape571.USE = "HAnimSiteShape"
Shape571.bboxCenter = [0,0,0]
Shape571.bboxDisplay = False
Shape571.bboxSize = [-1,-1,-1]
Shape571.visible = True

HAnimSite569.children.append(Shape571)

HAnimSegment568.children.append(HAnimSite569)
HAnimSite572 = x3d.HAnimSite()
HAnimSite572.DEF = "STD_Site_r_axilla_posterior_folds_pt"
HAnimSite572.bboxCenter = [0,0,0]
HAnimSite572.bboxDisplay = False
HAnimSite572.bboxSize = [-1,-1,-1]
HAnimSite572.name = "r_axilla_posterior_folds_pt"
HAnimSite572.visible = True
TouchSensor573 = x3d.TouchSensor()
TouchSensor573.description = "HAnimSite r_axilla_posterior_folds_pt"

HAnimSite572.children.append(TouchSensor573)
Shape574 = x3d.Shape()
Shape574.USE = "HAnimSiteShape"
Shape574.bboxCenter = [0,0,0]
Shape574.bboxDisplay = False
Shape574.bboxSize = [-1,-1,-1]
Shape574.visible = True

HAnimSite572.children.append(Shape574)

HAnimSegment568.children.append(HAnimSite572)
HAnimSite575 = x3d.HAnimSite()
HAnimSite575.DEF = "STD_Site_r_acromion_pt"
HAnimSite575.bboxCenter = [0,0,0]
HAnimSite575.bboxDisplay = False
HAnimSite575.bboxSize = [-1,-1,-1]
HAnimSite575.name = "r_acromion_pt"
HAnimSite575.translation = [-0.1905,1.4791,-0.0431]
HAnimSite575.visible = True
TouchSensor576 = x3d.TouchSensor()
TouchSensor576.description = "HAnimSite r_acromion_pt"

HAnimSite575.children.append(TouchSensor576)
Shape577 = x3d.Shape()
Shape577.USE = "HAnimSiteShape"
Shape577.bboxCenter = [0,0,0]
Shape577.bboxDisplay = False
Shape577.bboxSize = [-1,-1,-1]
Shape577.visible = True

HAnimSite575.children.append(Shape577)

HAnimSegment568.children.append(HAnimSite575)
HAnimSite578 = x3d.HAnimSite()
HAnimSite578.DEF = "STD_Site_r_axilla_proximal_pt"
HAnimSite578.bboxCenter = [0,0,0]
HAnimSite578.bboxDisplay = False
HAnimSite578.bboxSize = [-1,-1,-1]
HAnimSite578.name = "r_axilla_proximal_pt"
HAnimSite578.translation = [-0.1626,1.4072,-0.0031]
HAnimSite578.visible = True
TouchSensor579 = x3d.TouchSensor()
TouchSensor579.description = "HAnimSite r_axilla_proximal_pt"

HAnimSite578.children.append(TouchSensor579)
Shape580 = x3d.Shape()
Shape580.USE = "HAnimSiteShape"
Shape580.bboxCenter = [0,0,0]
Shape580.bboxDisplay = False
Shape580.bboxSize = [-1,-1,-1]
Shape580.visible = True

HAnimSite578.children.append(Shape580)

HAnimSegment568.children.append(HAnimSite578)
HAnimSite581 = x3d.HAnimSite()
HAnimSite581.DEF = "STD_Site_r_clavicale_pt"
HAnimSite581.bboxCenter = [0,0,0]
HAnimSite581.bboxDisplay = False
HAnimSite581.bboxSize = [-1,-1,-1]
HAnimSite581.name = "r_clavicale_pt"
HAnimSite581.translation = [-0.0115,1.4943,0.0400]
HAnimSite581.visible = True
TouchSensor582 = x3d.TouchSensor()
TouchSensor582.description = "HAnimSite r_clavicale_pt"

HAnimSite581.children.append(TouchSensor582)
Shape583 = x3d.Shape()
Shape583.USE = "HAnimSiteShape"
Shape583.bboxCenter = [0,0,0]
Shape583.bboxDisplay = False
Shape583.bboxSize = [-1,-1,-1]
Shape583.visible = True

HAnimSite581.children.append(Shape583)

HAnimSegment568.children.append(HAnimSite581)

HAnimJoint567.children.append(HAnimSegment568)
HAnimJoint584 = x3d.HAnimJoint()
HAnimJoint584.DEF = "STD_Joint_r_acromioclavicular"
HAnimJoint584.bboxCenter = [0,0,0]
HAnimJoint584.bboxDisplay = False
HAnimJoint584.bboxSize = [-1,-1,-1]
HAnimJoint584.center = [-0.0836,1.4281,-0.0401]
HAnimJoint584.name = "r_acromioclavicular"
HAnimJoint584.visible = True
HAnimSegment585 = x3d.HAnimSegment()
HAnimSegment585.DEF = "STD_Segment_r_scapula"
HAnimSegment585.bboxDisplay = False
HAnimSegment585.name = "r_scapula"
HAnimSegment585.visible = True

HAnimJoint584.children.append(HAnimSegment585)
HAnimJoint586 = x3d.HAnimJoint()
HAnimJoint586.DEF = "STD_Joint_r_shoulder"
HAnimJoint586.bboxCenter = [0,0,0]
HAnimJoint586.bboxDisplay = False
HAnimJoint586.bboxSize = [-1,-1,-1]
HAnimJoint586.center = [-0.1907,1.4407,-0.0325]
HAnimJoint586.name = "r_shoulder"
HAnimJoint586.visible = True
HAnimSegment587 = x3d.HAnimSegment()
HAnimSegment587.DEF = "STD_Segment_r_upperarm"
HAnimSegment587.bboxDisplay = False
HAnimSegment587.name = "r_upperarm"
HAnimSegment587.visible = True
HAnimSite588 = x3d.HAnimSite()
HAnimSite588.DEF = "STD_Site_r_humeral_lateral_epicondyles_pt"
HAnimSite588.bboxCenter = [0,0,0]
HAnimSite588.bboxDisplay = False
HAnimSite588.bboxSize = [-1,-1,-1]
HAnimSite588.name = "r_humeral_lateral_epicondyles_pt"
HAnimSite588.translation = [-0.2224,1.1517,-0.1033]
HAnimSite588.visible = True
TouchSensor589 = x3d.TouchSensor()
TouchSensor589.description = "HAnimSite r_humeral_lateral_epicondyles_pt"

HAnimSite588.children.append(TouchSensor589)
Shape590 = x3d.Shape()
Shape590.USE = "HAnimSiteShape"
Shape590.bboxCenter = [0,0,0]
Shape590.bboxDisplay = False
Shape590.bboxSize = [-1,-1,-1]
Shape590.visible = True

HAnimSite588.children.append(Shape590)

HAnimSegment587.children.append(HAnimSite588)
HAnimSite591 = x3d.HAnimSite()
HAnimSite591.DEF = "STD_Site_r_bideltoid_pt"
HAnimSite591.bboxCenter = [0,0,0]
HAnimSite591.bboxDisplay = False
HAnimSite591.bboxSize = [-1,-1,-1]
HAnimSite591.name = "r_bideltoid_pt"
HAnimSite591.visible = True
TouchSensor592 = x3d.TouchSensor()
TouchSensor592.description = "HAnimSite r_bideltoid_pt"

HAnimSite591.children.append(TouchSensor592)
Shape593 = x3d.Shape()
Shape593.USE = "HAnimSiteShape"
Shape593.bboxCenter = [0,0,0]
Shape593.bboxDisplay = False
Shape593.bboxSize = [-1,-1,-1]
Shape593.visible = True

HAnimSite591.children.append(Shape593)

HAnimSegment587.children.append(HAnimSite591)

HAnimJoint586.children.append(HAnimSegment587)
HAnimJoint594 = x3d.HAnimJoint()
HAnimJoint594.DEF = "STD_Joint_r_elbow"
HAnimJoint594.bboxCenter = [0,0,0]
HAnimJoint594.bboxDisplay = False
HAnimJoint594.bboxSize = [-1,-1,-1]
HAnimJoint594.center = [-0.1949,1.1388,-0.0620]
HAnimJoint594.name = "r_elbow"
HAnimJoint594.visible = True
HAnimSegment595 = x3d.HAnimSegment()
HAnimSegment595.DEF = "STD_Segment_r_forearm"
HAnimSegment595.bboxDisplay = False
HAnimSegment595.name = "r_forearm"
HAnimSegment595.visible = True
HAnimSite596 = x3d.HAnimSite()
HAnimSite596.DEF = "STD_Site_r_olecranon_pt"
HAnimSite596.bboxCenter = [0,0,0]
HAnimSite596.bboxDisplay = False
HAnimSite596.bboxSize = [-1,-1,-1]
HAnimSite596.name = "r_olecranon_pt"
HAnimSite596.translation = [-0.1907,1.1405,-0.1065]
HAnimSite596.visible = True
TouchSensor597 = x3d.TouchSensor()
TouchSensor597.description = "HAnimSite r_olecranon_pt"

HAnimSite596.children.append(TouchSensor597)
Shape598 = x3d.Shape()
Shape598.USE = "HAnimSiteShape"
Shape598.bboxCenter = [0,0,0]
Shape598.bboxDisplay = False
Shape598.bboxSize = [-1,-1,-1]
Shape598.visible = True

HAnimSite596.children.append(Shape598)

HAnimSegment595.children.append(HAnimSite596)
HAnimSite599 = x3d.HAnimSite()
HAnimSite599.DEF = "STD_Site_r_radial_styloid_pt"
HAnimSite599.bboxCenter = [0,0,0]
HAnimSite599.bboxDisplay = False
HAnimSite599.bboxSize = [-1,-1,-1]
HAnimSite599.name = "r_radial_styloid_pt"
HAnimSite599.translation = [-0.1884,0.8676,-0.0360]
HAnimSite599.visible = True
TouchSensor600 = x3d.TouchSensor()
TouchSensor600.description = "HAnimSite r_radial_styloid_pt"

HAnimSite599.children.append(TouchSensor600)
Shape601 = x3d.Shape()
Shape601.USE = "HAnimSiteShape"
Shape601.bboxCenter = [0,0,0]
Shape601.bboxDisplay = False
Shape601.bboxSize = [-1,-1,-1]
Shape601.visible = True

HAnimSite599.children.append(Shape601)

HAnimSegment595.children.append(HAnimSite599)
HAnimSite602 = x3d.HAnimSite()
HAnimSite602.DEF = "STD_Site_r_humeral_medial_epicondyles_pt"
HAnimSite602.bboxCenter = [0,0,0]
HAnimSite602.bboxDisplay = False
HAnimSite602.bboxSize = [-1,-1,-1]
HAnimSite602.name = "r_humeral_medial_epicondyles_pt"
HAnimSite602.translation = [-0.1680,1.1298,-0.1062]
HAnimSite602.visible = True
TouchSensor603 = x3d.TouchSensor()
TouchSensor603.description = "HAnimSite r_humeral_medial_epicondyles_pt"

HAnimSite602.children.append(TouchSensor603)
Shape604 = x3d.Shape()
Shape604.USE = "HAnimSiteShape"
Shape604.bboxCenter = [0,0,0]
Shape604.bboxDisplay = False
Shape604.bboxSize = [-1,-1,-1]
Shape604.visible = True

HAnimSite602.children.append(Shape604)

HAnimSegment595.children.append(HAnimSite602)
HAnimSite605 = x3d.HAnimSite()
HAnimSite605.DEF = "STD_Site_r_radiale_pt"
HAnimSite605.bboxCenter = [0,0,0]
HAnimSite605.bboxDisplay = False
HAnimSite605.bboxSize = [-1,-1,-1]
HAnimSite605.name = "r_radiale_pt"
HAnimSite605.translation = [-0.2130,1.1305,-0.1091]
HAnimSite605.visible = True
TouchSensor606 = x3d.TouchSensor()
TouchSensor606.description = "HAnimSite r_radiale_pt"

HAnimSite605.children.append(TouchSensor606)
Shape607 = x3d.Shape()
Shape607.USE = "HAnimSiteShape"
Shape607.bboxCenter = [0,0,0]
Shape607.bboxDisplay = False
Shape607.bboxSize = [-1,-1,-1]
Shape607.visible = True

HAnimSite605.children.append(Shape607)

HAnimSegment595.children.append(HAnimSite605)

HAnimJoint594.children.append(HAnimSegment595)
HAnimJoint608 = x3d.HAnimJoint()
HAnimJoint608.DEF = "STD_Joint_r_radiocarpal"
HAnimJoint608.bboxCenter = [0,0,0]
HAnimJoint608.bboxDisplay = False
HAnimJoint608.bboxSize = [-1,-1,-1]
HAnimJoint608.center = [-0.1959,0.8694,-0.0521]
HAnimJoint608.name = "r_radiocarpal"
HAnimJoint608.visible = True
HAnimSegment609 = x3d.HAnimSegment()
HAnimSegment609.DEF = "STD_Segment_r_carpal"
HAnimSegment609.bboxDisplay = False
HAnimSegment609.name = "r_carpal"
HAnimSegment609.visible = True
HAnimSite610 = x3d.HAnimSite()
HAnimSite610.DEF = "STD_Site_r_ulnar_styloid_pt"
HAnimSite610.bboxCenter = [0,0,0]
HAnimSite610.bboxDisplay = False
HAnimSite610.bboxSize = [-1,-1,-1]
HAnimSite610.name = "r_ulnar_styloid_pt"
HAnimSite610.translation = [-0.2117,0.8562,-0.0584]
HAnimSite610.visible = True
TouchSensor611 = x3d.TouchSensor()
TouchSensor611.description = "HAnimSite r_ulnar_styloid_pt"

HAnimSite610.children.append(TouchSensor611)
Shape612 = x3d.Shape()
Shape612.USE = "HAnimSiteShape"
Shape612.bboxCenter = [0,0,0]
Shape612.bboxDisplay = False
Shape612.bboxSize = [-1,-1,-1]
Shape612.visible = True

HAnimSite610.children.append(Shape612)

HAnimSegment609.children.append(HAnimSite610)

HAnimJoint608.children.append(HAnimSegment609)
HAnimJoint613 = x3d.HAnimJoint()
HAnimJoint613.DEF = "STD_Joint_r_midcarpal_1"
HAnimJoint613.bboxCenter = [0,0,0]
HAnimJoint613.bboxDisplay = False
HAnimJoint613.bboxSize = [-1,-1,-1]
HAnimJoint613.name = "r_midcarpal_1"
HAnimJoint613.visible = True
HAnimSegment614 = x3d.HAnimSegment()
HAnimSegment614.DEF = "STD_Segment_r_trapezium"
HAnimSegment614.bboxDisplay = False
HAnimSegment614.name = "r_trapezium"
HAnimSegment614.visible = True

HAnimJoint613.children.append(HAnimSegment614)
HAnimJoint615 = x3d.HAnimJoint()
HAnimJoint615.DEF = "STD_Joint_r_carpometacarpal_1"
HAnimJoint615.bboxCenter = [0,0,0]
HAnimJoint615.bboxDisplay = False
HAnimJoint615.bboxSize = [-1,-1,-1]
HAnimJoint615.center = [-0.1899,0.8502,-0.0473]
HAnimJoint615.name = "r_carpometacarpal_1"
HAnimJoint615.visible = True
HAnimSegment616 = x3d.HAnimSegment()
HAnimSegment616.DEF = "STD_Segment_r_metacarpal_1"
HAnimSegment616.bboxDisplay = False
HAnimSegment616.name = "r_metacarpal_1"
HAnimSegment616.visible = True

HAnimJoint615.children.append(HAnimSegment616)
HAnimJoint617 = x3d.HAnimJoint()
HAnimJoint617.DEF = "STD_Joint_r_metacarpophalangeal_1"
HAnimJoint617.bboxCenter = [0,0,0]
HAnimJoint617.bboxDisplay = False
HAnimJoint617.bboxSize = [-1,-1,-1]
HAnimJoint617.center = [-0.1874,0.8256,0.0306]
HAnimJoint617.name = "r_metacarpophalangeal_1"
HAnimJoint617.visible = True
HAnimSegment618 = x3d.HAnimSegment()
HAnimSegment618.DEF = "STD_Segment_r_carpal_proximal_phalanx_1"
HAnimSegment618.bboxDisplay = False
HAnimSegment618.name = "r_carpal_proximal_phalanx_1"
HAnimSegment618.visible = True

HAnimJoint617.children.append(HAnimSegment618)
HAnimJoint619 = x3d.HAnimJoint()
HAnimJoint619.DEF = "STD_Joint_r_carpal_interphalangeal_1"
HAnimJoint619.bboxCenter = [0,0,0]
HAnimJoint619.bboxDisplay = False
HAnimJoint619.bboxSize = [-1,-1,-1]
HAnimJoint619.center = [-0.1864,0.8190,0.0506]
HAnimJoint619.name = "r_carpal_interphalangeal_1"
HAnimJoint619.visible = True
HAnimSegment620 = x3d.HAnimSegment()
HAnimSegment620.DEF = "STD_Segment_r_carpal_distal_phalanx_1"
HAnimSegment620.bboxDisplay = False
HAnimSegment620.name = "r_carpal_distal_phalanx_1"
HAnimSegment620.visible = True
HAnimSite621 = x3d.HAnimSite()
HAnimSite621.DEF = "STD_Site_r_carpal_distal_phalanx_1_pt"
HAnimSite621.bboxCenter = [0,0,0]
HAnimSite621.bboxDisplay = False
HAnimSite621.bboxSize = [-1,-1,-1]
HAnimSite621.name = "r_carpal_distal_phalanx_1_pt"
HAnimSite621.visible = True
TouchSensor622 = x3d.TouchSensor()
TouchSensor622.description = "HAnimSite r_carpal_distal_phalanx_1_pt"

HAnimSite621.children.append(TouchSensor622)
Shape623 = x3d.Shape()
Shape623.USE = "HAnimSiteShape"
Shape623.bboxCenter = [0,0,0]
Shape623.bboxDisplay = False
Shape623.bboxSize = [-1,-1,-1]
Shape623.visible = True

HAnimSite621.children.append(Shape623)

HAnimSegment620.children.append(HAnimSite621)

HAnimJoint619.children.append(HAnimSegment620)

HAnimJoint617.children.append(HAnimJoint619)

HAnimJoint615.children.append(HAnimJoint617)

HAnimJoint613.children.append(HAnimJoint615)

HAnimJoint608.children.append(HAnimJoint613)
HAnimJoint624 = x3d.HAnimJoint()
HAnimJoint624.DEF = "STD_Joint_r_midcarpal_2"
HAnimJoint624.bboxCenter = [0,0,0]
HAnimJoint624.bboxDisplay = False
HAnimJoint624.bboxSize = [-1,-1,-1]
HAnimJoint624.name = "r_midcarpal_2"
HAnimJoint624.visible = True
HAnimSegment625 = x3d.HAnimSegment()
HAnimSegment625.DEF = "STD_Segment_r_trapezoid"
HAnimSegment625.bboxDisplay = False
HAnimSegment625.name = "r_trapezoid"
HAnimSegment625.visible = True

HAnimJoint624.children.append(HAnimSegment625)
HAnimJoint626 = x3d.HAnimJoint()
HAnimJoint626.DEF = "STD_Joint_r_carpometacarpal_2"
HAnimJoint626.bboxCenter = [0,0,0]
HAnimJoint626.bboxDisplay = False
HAnimJoint626.bboxSize = [-1,-1,-1]
HAnimJoint626.center = [-0.1961,0.8055,-0.0218]
HAnimJoint626.name = "r_carpometacarpal_2"
HAnimJoint626.visible = True
HAnimSegment627 = x3d.HAnimSegment()
HAnimSegment627.DEF = "STD_Segment_r_metacarpal_2"
HAnimSegment627.bboxDisplay = False
HAnimSegment627.name = "r_metacarpal_2"
HAnimSegment627.visible = True
HAnimSite628 = x3d.HAnimSite()
HAnimSite628.DEF = "STD_Site_r_metacarpal_phalanx_2_pt"
HAnimSite628.bboxCenter = [0,0,0]
HAnimSite628.bboxDisplay = False
HAnimSite628.bboxSize = [-1,-1,-1]
HAnimSite628.name = "r_metacarpal_phalanx_2_pt"
HAnimSite628.translation = [-0.1977,0.8169,-0.0177]
HAnimSite628.visible = True
TouchSensor629 = x3d.TouchSensor()
TouchSensor629.description = "HAnimSite r_metacarpal_phalanx_2_pt"

HAnimSite628.children.append(TouchSensor629)
Shape630 = x3d.Shape()
Shape630.USE = "HAnimSiteShape"
Shape630.bboxCenter = [0,0,0]
Shape630.bboxDisplay = False
Shape630.bboxSize = [-1,-1,-1]
Shape630.visible = True

HAnimSite628.children.append(Shape630)

HAnimSegment627.children.append(HAnimSite628)

HAnimJoint626.children.append(HAnimSegment627)
HAnimJoint631 = x3d.HAnimJoint()
HAnimJoint631.DEF = "STD_Joint_r_metacarpophalangeal_2"
HAnimJoint631.bboxCenter = [0,0,0]
HAnimJoint631.bboxDisplay = False
HAnimJoint631.bboxSize = [-1,-1,-1]
HAnimJoint631.center = [-0.1961,0.7846,-0.0218]
HAnimJoint631.name = "r_metacarpophalangeal_2"
HAnimJoint631.visible = True
HAnimSegment632 = x3d.HAnimSegment()
HAnimSegment632.DEF = "STD_Segment_r_carpal_proximal_phalanx_2"
HAnimSegment632.bboxDisplay = False
HAnimSegment632.name = "r_carpal_proximal_phalanx_2"
HAnimSegment632.visible = True

HAnimJoint631.children.append(HAnimSegment632)
HAnimJoint633 = x3d.HAnimJoint()
HAnimJoint633.DEF = "STD_Joint_r_carpal_proximal_interphalangeal_2"
HAnimJoint633.bboxCenter = [0,0,0]
HAnimJoint633.bboxDisplay = False
HAnimJoint633.bboxSize = [-1,-1,-1]
HAnimJoint633.center = [-0.1954,0.7393,-0.0185]
HAnimJoint633.name = "r_carpal_proximal_interphalangeal_2"
HAnimJoint633.visible = True
HAnimSegment634 = x3d.HAnimSegment()
HAnimSegment634.DEF = "STD_Segment_r_carpal_middle_phalanx_2"
HAnimSegment634.bboxDisplay = False
HAnimSegment634.name = "r_carpal_middle_phalanx_2"
HAnimSegment634.visible = True

HAnimJoint633.children.append(HAnimSegment634)
HAnimJoint635 = x3d.HAnimJoint()
HAnimJoint635.DEF = "STD_Joint_r_carpal_distal_interphalangeal_2"
HAnimJoint635.bboxCenter = [0,0,0]
HAnimJoint635.bboxDisplay = False
HAnimJoint635.bboxSize = [-1,-1,-1]
HAnimJoint635.center = [-0.1945,0.7169,-0.0173]
HAnimJoint635.name = "r_carpal_distal_interphalangeal_2"
HAnimJoint635.visible = True
HAnimSegment636 = x3d.HAnimSegment()
HAnimSegment636.DEF = "STD_Segment_r_carpal_distal_phalanx_2"
HAnimSegment636.bboxDisplay = False
HAnimSegment636.name = "r_carpal_distal_phalanx_2"
HAnimSegment636.visible = True
HAnimSite637 = x3d.HAnimSite()
HAnimSite637.DEF = "STD_Site_r_dactylion_pt"
HAnimSite637.bboxCenter = [0,0,0]
HAnimSite637.bboxDisplay = False
HAnimSite637.bboxSize = [-1,-1,-1]
HAnimSite637.name = "r_dactylion_pt"
HAnimSite637.translation = [-0.1941,0.6772,-0.0423]
HAnimSite637.visible = True
TouchSensor638 = x3d.TouchSensor()
TouchSensor638.description = "HAnimSite r_dactylion_pt"

HAnimSite637.children.append(TouchSensor638)
Shape639 = x3d.Shape()
Shape639.USE = "HAnimSiteShape"
Shape639.bboxCenter = [0,0,0]
Shape639.bboxDisplay = False
Shape639.bboxSize = [-1,-1,-1]
Shape639.visible = True

HAnimSite637.children.append(Shape639)

HAnimSegment636.children.append(HAnimSite637)
HAnimSite640 = x3d.HAnimSite()
HAnimSite640.DEF = "STD_Site_r_carpal_distal_phalanx_2_pt"
HAnimSite640.bboxCenter = [0,0,0]
HAnimSite640.bboxDisplay = False
HAnimSite640.bboxSize = [-1,-1,-1]
HAnimSite640.name = "r_carpal_distal_phalanx_2_pt"
HAnimSite640.visible = True
TouchSensor641 = x3d.TouchSensor()
TouchSensor641.description = "HAnimSite r_carpal_distal_phalanx_2_pt"

HAnimSite640.children.append(TouchSensor641)
Shape642 = x3d.Shape()
Shape642.USE = "HAnimSiteShape"
Shape642.bboxCenter = [0,0,0]
Shape642.bboxDisplay = False
Shape642.bboxSize = [-1,-1,-1]
Shape642.visible = True

HAnimSite640.children.append(Shape642)

HAnimSegment636.children.append(HAnimSite640)

HAnimJoint635.children.append(HAnimSegment636)

HAnimJoint633.children.append(HAnimJoint635)

HAnimJoint631.children.append(HAnimJoint633)

HAnimJoint626.children.append(HAnimJoint631)

HAnimJoint624.children.append(HAnimJoint626)

HAnimJoint608.children.append(HAnimJoint624)
HAnimJoint643 = x3d.HAnimJoint()
HAnimJoint643.DEF = "STD_Joint_r_midcarpal_3"
HAnimJoint643.bboxCenter = [0,0,0]
HAnimJoint643.bboxDisplay = False
HAnimJoint643.bboxSize = [-1,-1,-1]
HAnimJoint643.name = "r_midcarpal_3"
HAnimJoint643.visible = True
HAnimSegment644 = x3d.HAnimSegment()
HAnimSegment644.DEF = "STD_Segment_r_capitate"
HAnimSegment644.bboxDisplay = False
HAnimSegment644.name = "r_capitate"
HAnimSegment644.visible = True

HAnimJoint643.children.append(HAnimSegment644)
HAnimJoint645 = x3d.HAnimJoint()
HAnimJoint645.DEF = "STD_Joint_r_carpometacarpal_3"
HAnimJoint645.bboxCenter = [0,0,0]
HAnimJoint645.bboxDisplay = False
HAnimJoint645.bboxSize = [-1,-1,-1]
HAnimJoint645.center = [-0.1972,0.8060,-0.0468]
HAnimJoint645.name = "r_carpometacarpal_3"
HAnimJoint645.visible = True
HAnimSegment646 = x3d.HAnimSegment()
HAnimSegment646.DEF = "STD_Segment_r_metacarpal_3"
HAnimSegment646.bboxDisplay = False
HAnimSegment646.name = "r_metacarpal_3"
HAnimSegment646.visible = True
HAnimSite647 = x3d.HAnimSite()
HAnimSite647.DEF = "STD_Site_r_metacarpal_phalanx_3_pt"
HAnimSite647.bboxCenter = [0,0,0]
HAnimSite647.bboxDisplay = False
HAnimSite647.bboxSize = [-1,-1,-1]
HAnimSite647.name = "r_metacarpal_phalanx_3_pt"
HAnimSite647.visible = True
TouchSensor648 = x3d.TouchSensor()
TouchSensor648.description = "HAnimSite r_metacarpal_phalanx_3_pt"

HAnimSite647.children.append(TouchSensor648)
Shape649 = x3d.Shape()
Shape649.USE = "HAnimSiteShape"
Shape649.bboxCenter = [0,0,0]
Shape649.bboxDisplay = False
Shape649.bboxSize = [-1,-1,-1]
Shape649.visible = True

HAnimSite647.children.append(Shape649)

HAnimSegment646.children.append(HAnimSite647)

HAnimJoint645.children.append(HAnimSegment646)
HAnimJoint650 = x3d.HAnimJoint()
HAnimJoint650.DEF = "STD_Joint_r_metacarpophalangeal_3"
HAnimJoint650.bboxCenter = [0,0,0]
HAnimJoint650.bboxDisplay = False
HAnimJoint650.bboxSize = [-1,-1,-1]
HAnimJoint650.center = [-0.1972,0.7849,-0.0468]
HAnimJoint650.name = "r_metacarpophalangeal_3"
HAnimJoint650.visible = True
HAnimSegment651 = x3d.HAnimSegment()
HAnimSegment651.DEF = "STD_Segment_r_carpal_proximal_phalanx_3"
HAnimSegment651.bboxDisplay = False
HAnimSegment651.name = "r_carpal_proximal_phalanx_3"
HAnimSegment651.visible = True

HAnimJoint650.children.append(HAnimSegment651)
HAnimJoint652 = x3d.HAnimJoint()
HAnimJoint652.DEF = "STD_Joint_r_carpal_proximal_interphalangeal_3"
HAnimJoint652.bboxCenter = [0,0,0]
HAnimJoint652.bboxDisplay = False
HAnimJoint652.bboxSize = [-1,-1,-1]
HAnimJoint652.center = [-0.1950,0.7304,-0.0441]
HAnimJoint652.name = "r_carpal_proximal_interphalangeal_3"
HAnimJoint652.visible = True
HAnimSegment653 = x3d.HAnimSegment()
HAnimSegment653.DEF = "STD_Segment_r_carpal_middle_phalanx_3"
HAnimSegment653.bboxDisplay = False
HAnimSegment653.name = "r_carpal_middle_phalanx_3"
HAnimSegment653.visible = True

HAnimJoint652.children.append(HAnimSegment653)
HAnimJoint654 = x3d.HAnimJoint()
HAnimJoint654.DEF = "STD_Joint_r_carpal_distal_interphalangeal_3"
HAnimJoint654.bboxCenter = [0,0,0]
HAnimJoint654.bboxDisplay = False
HAnimJoint654.bboxSize = [-1,-1,-1]
HAnimJoint654.center = [-0.1939,0.7042,-0.0432]
HAnimJoint654.name = "r_carpal_distal_interphalangeal_3"
HAnimJoint654.visible = True
HAnimSegment655 = x3d.HAnimSegment()
HAnimSegment655.DEF = "STD_Segment_r_carpal_distal_phalanx_3"
HAnimSegment655.bboxDisplay = False
HAnimSegment655.name = "r_carpal_distal_phalanx_3"
HAnimSegment655.visible = True
HAnimSite656 = x3d.HAnimSite()
HAnimSite656.DEF = "STD_Site_r_carpal_distal_phalanx_3_pt"
HAnimSite656.bboxCenter = [0,0,0]
HAnimSite656.bboxDisplay = False
HAnimSite656.bboxSize = [-1,-1,-1]
HAnimSite656.name = "r_carpal_distal_phalanx_3_pt"
HAnimSite656.visible = True
TouchSensor657 = x3d.TouchSensor()
TouchSensor657.description = "HAnimSite r_carpal_distal_phalanx_3_pt"

HAnimSite656.children.append(TouchSensor657)
Shape658 = x3d.Shape()
Shape658.USE = "HAnimSiteShape"
Shape658.bboxCenter = [0,0,0]
Shape658.bboxDisplay = False
Shape658.bboxSize = [-1,-1,-1]
Shape658.visible = True

HAnimSite656.children.append(Shape658)

HAnimSegment655.children.append(HAnimSite656)

HAnimJoint654.children.append(HAnimSegment655)

HAnimJoint652.children.append(HAnimJoint654)

HAnimJoint650.children.append(HAnimJoint652)

HAnimJoint645.children.append(HAnimJoint650)

HAnimJoint643.children.append(HAnimJoint645)

HAnimJoint608.children.append(HAnimJoint643)
HAnimJoint659 = x3d.HAnimJoint()
HAnimJoint659.DEF = "STD_Joint_r_midcarpal_4_5"
HAnimJoint659.bboxCenter = [0,0,0]
HAnimJoint659.bboxDisplay = False
HAnimJoint659.bboxSize = [-1,-1,-1]
HAnimJoint659.name = "r_midcarpal_4_5"
HAnimJoint659.visible = True
HAnimSegment660 = x3d.HAnimSegment()
HAnimSegment660.DEF = "STD_Segment_r_hamate"
HAnimSegment660.bboxDisplay = False
HAnimSegment660.name = "r_hamate"
HAnimSegment660.visible = True

HAnimJoint659.children.append(HAnimSegment660)
HAnimJoint661 = x3d.HAnimJoint()
HAnimJoint661.DEF = "STD_Joint_r_carpometacarpal_4"
HAnimJoint661.bboxCenter = [0,0,0]
HAnimJoint661.bboxDisplay = False
HAnimJoint661.bboxSize = [-1,-1,-1]
HAnimJoint661.center = [-0.1951,0.8049,-0.0732]
HAnimJoint661.name = "r_carpometacarpal_4"
HAnimJoint661.visible = True
HAnimSegment662 = x3d.HAnimSegment()
HAnimSegment662.DEF = "STD_Segment_r_metacarpal_4"
HAnimSegment662.bboxDisplay = False
HAnimSegment662.name = "r_metacarpal_4"
HAnimSegment662.visible = True

HAnimJoint661.children.append(HAnimSegment662)
HAnimJoint663 = x3d.HAnimJoint()
HAnimJoint663.DEF = "STD_Joint_r_metacarpophalangeal_4"
HAnimJoint663.bboxCenter = [0,0,0]
HAnimJoint663.bboxDisplay = False
HAnimJoint663.bboxSize = [-1,-1,-1]
HAnimJoint663.center = [-0.1951,0.7845,-0.0732]
HAnimJoint663.name = "r_metacarpophalangeal_4"
HAnimJoint663.visible = True
HAnimSegment664 = x3d.HAnimSegment()
HAnimSegment664.DEF = "STD_Segment_r_carpal_proximal_phalanx_4"
HAnimSegment664.bboxDisplay = False
HAnimSegment664.name = "r_carpal_proximal_phalanx_4"
HAnimSegment664.visible = True

HAnimJoint663.children.append(HAnimSegment664)
HAnimJoint665 = x3d.HAnimJoint()
HAnimJoint665.DEF = "STD_Joint_r_carpal_proximal_interphalangeal_4"
HAnimJoint665.bboxCenter = [0,0,0]
HAnimJoint665.bboxDisplay = False
HAnimJoint665.bboxSize = [-1,-1,-1]
HAnimJoint665.center = [-0.1920,0.7318,-0.0716]
HAnimJoint665.name = "r_carpal_proximal_interphalangeal_4"
HAnimJoint665.visible = True
HAnimSegment666 = x3d.HAnimSegment()
HAnimSegment666.DEF = "STD_Segment_r_carpal_middle_phalanx_4"
HAnimSegment666.bboxDisplay = False
HAnimSegment666.name = "r_carpal_middle_phalanx_4"
HAnimSegment666.visible = True

HAnimJoint665.children.append(HAnimSegment666)
HAnimJoint667 = x3d.HAnimJoint()
HAnimJoint667.DEF = "STD_Joint_r_carpal_distal_interphalangeal_4"
HAnimJoint667.bboxCenter = [0,0,0]
HAnimJoint667.bboxDisplay = False
HAnimJoint667.bboxSize = [-1,-1,-1]
HAnimJoint667.center = [-0.1908,0.7077,-0.0706]
HAnimJoint667.name = "r_carpal_distal_interphalangeal_4"
HAnimJoint667.visible = True
HAnimSegment668 = x3d.HAnimSegment()
HAnimSegment668.DEF = "STD_Segment_r_carpal_distal_phalanx_4"
HAnimSegment668.bboxDisplay = False
HAnimSegment668.name = "r_carpal_distal_phalanx_4"
HAnimSegment668.visible = True
HAnimSite669 = x3d.HAnimSite()
HAnimSite669.DEF = "STD_Site_r_carpal_distal_phalanx_4_pt"
HAnimSite669.bboxCenter = [0,0,0]
HAnimSite669.bboxDisplay = False
HAnimSite669.bboxSize = [-1,-1,-1]
HAnimSite669.name = "r_carpal_distal_phalanx_4_pt"
HAnimSite669.visible = True
TouchSensor670 = x3d.TouchSensor()
TouchSensor670.description = "HAnimSite r_carpal_distal_phalanx_4_pt"

HAnimSite669.children.append(TouchSensor670)
Shape671 = x3d.Shape()
Shape671.USE = "HAnimSiteShape"
Shape671.bboxCenter = [0,0,0]
Shape671.bboxDisplay = False
Shape671.bboxSize = [-1,-1,-1]
Shape671.visible = True

HAnimSite669.children.append(Shape671)

HAnimSegment668.children.append(HAnimSite669)

HAnimJoint667.children.append(HAnimSegment668)

HAnimJoint665.children.append(HAnimJoint667)

HAnimJoint663.children.append(HAnimJoint665)

HAnimJoint661.children.append(HAnimJoint663)

HAnimJoint659.children.append(HAnimJoint661)
HAnimJoint672 = x3d.HAnimJoint()
HAnimJoint672.DEF = "STD_Joint_r_carpometacarpal_5"
HAnimJoint672.bboxCenter = [0,0,0]
HAnimJoint672.bboxDisplay = False
HAnimJoint672.bboxSize = [-1,-1,-1]
HAnimJoint672.center = [-0.1926,0.8096,-0.0975]
HAnimJoint672.name = "r_carpometacarpal_5"
HAnimJoint672.visible = True
HAnimSegment673 = x3d.HAnimSegment()
HAnimSegment673.DEF = "STD_Segment_r_metacarpal_5"
HAnimSegment673.bboxDisplay = False
HAnimSegment673.name = "r_metacarpal_5"
HAnimSegment673.visible = True
HAnimSite674 = x3d.HAnimSite()
HAnimSite674.DEF = "STD_Site_r_metacarpal_phalanx_5_pt"
HAnimSite674.bboxCenter = [0,0,0]
HAnimSite674.bboxDisplay = False
HAnimSite674.bboxSize = [-1,-1,-1]
HAnimSite674.name = "r_metacarpal_phalanx_5_pt"
HAnimSite674.translation = [-0.1929,0.7890,-0.1064]
HAnimSite674.visible = True
TouchSensor675 = x3d.TouchSensor()
TouchSensor675.description = "HAnimSite r_metacarpal_phalanx_5_pt"

HAnimSite674.children.append(TouchSensor675)
Shape676 = x3d.Shape()
Shape676.USE = "HAnimSiteShape"
Shape676.bboxCenter = [0,0,0]
Shape676.bboxDisplay = False
Shape676.bboxSize = [-1,-1,-1]
Shape676.visible = True

HAnimSite674.children.append(Shape676)

HAnimSegment673.children.append(HAnimSite674)

HAnimJoint672.children.append(HAnimSegment673)
HAnimJoint677 = x3d.HAnimJoint()
HAnimJoint677.DEF = "STD_Joint_r_metacarpophalangeal_5"
HAnimJoint677.bboxCenter = [0,0,0]
HAnimJoint677.bboxDisplay = False
HAnimJoint677.bboxSize = [-1,-1,-1]
HAnimJoint677.center = [-0.1926,0.7896,-0.0975]
HAnimJoint677.name = "r_metacarpophalangeal_5"
HAnimJoint677.visible = True
HAnimSegment678 = x3d.HAnimSegment()
HAnimSegment678.DEF = "STD_Segment_r_carpal_proximal_phalanx_5"
HAnimSegment678.bboxDisplay = False
HAnimSegment678.name = "r_carpal_proximal_phalanx_5"
HAnimSegment678.visible = True

HAnimJoint677.children.append(HAnimSegment678)
HAnimJoint679 = x3d.HAnimJoint()
HAnimJoint679.DEF = "STD_Joint_r_carpal_proximal_interphalangeal_5"
HAnimJoint679.bboxCenter = [0,0,0]
HAnimJoint679.bboxDisplay = False
HAnimJoint679.bboxSize = [-1,-1,-1]
HAnimJoint679.center = [-0.1902,0.7483,-0.0963]
HAnimJoint679.name = "r_carpal_proximal_interphalangeal_5"
HAnimJoint679.visible = True
HAnimSegment680 = x3d.HAnimSegment()
HAnimSegment680.DEF = "STD_Segment_r_carpal_middle_phalanx_5"
HAnimSegment680.bboxDisplay = False
HAnimSegment680.name = "r_carpal_middle_phalanx_5"
HAnimSegment680.visible = True

HAnimJoint679.children.append(HAnimSegment680)
HAnimJoint681 = x3d.HAnimJoint()
HAnimJoint681.DEF = "STD_Joint_r_carpal_distal_interphalangeal_5"
HAnimJoint681.bboxCenter = [0,0,0]
HAnimJoint681.bboxDisplay = False
HAnimJoint681.bboxSize = [-1,-1,-1]
HAnimJoint681.center = [-0.1908,0.7540,-0.0960]
HAnimJoint681.name = "r_carpal_distal_interphalangeal_5"
HAnimJoint681.visible = True
HAnimSegment682 = x3d.HAnimSegment()
HAnimSegment682.DEF = "STD_Segment_r_carpal_distal_phalanx_5"
HAnimSegment682.bboxDisplay = False
HAnimSegment682.name = "r_carpal_distal_phalanx_5"
HAnimSegment682.visible = True
HAnimSite683 = x3d.HAnimSite()
HAnimSite683.DEF = "STD_Site_r_carpal_distal_phalanx_5_pt"
HAnimSite683.bboxCenter = [0,0,0]
HAnimSite683.bboxDisplay = False
HAnimSite683.bboxSize = [-1,-1,-1]
HAnimSite683.name = "r_carpal_distal_phalanx_5_pt"
HAnimSite683.visible = True
TouchSensor684 = x3d.TouchSensor()
TouchSensor684.description = "HAnimSite r_carpal_distal_phalanx_5_pt"

HAnimSite683.children.append(TouchSensor684)
Shape685 = x3d.Shape()
Shape685.USE = "HAnimSiteShape"
Shape685.bboxCenter = [0,0,0]
Shape685.bboxDisplay = False
Shape685.bboxSize = [-1,-1,-1]
Shape685.visible = True

HAnimSite683.children.append(Shape685)

HAnimSegment682.children.append(HAnimSite683)

HAnimJoint681.children.append(HAnimSegment682)

HAnimJoint679.children.append(HAnimJoint681)

HAnimJoint677.children.append(HAnimJoint679)

HAnimJoint672.children.append(HAnimJoint677)

HAnimJoint659.children.append(HAnimJoint672)

HAnimJoint608.children.append(HAnimJoint659)

HAnimJoint594.children.append(HAnimJoint608)

HAnimJoint586.children.append(HAnimJoint594)

HAnimJoint584.children.append(HAnimJoint586)

HAnimJoint567.children.append(HAnimJoint584)

HAnimJoint356.children.append(HAnimJoint567)

HAnimJoint354.children.append(HAnimJoint356)

HAnimJoint352.children.append(HAnimJoint354)

HAnimJoint350.children.append(HAnimJoint352)

HAnimJoint345.children.append(HAnimJoint350)

HAnimJoint331.children.append(HAnimJoint345)

HAnimJoint329.children.append(HAnimJoint331)

HAnimJoint327.children.append(HAnimJoint329)

HAnimJoint319.children.append(HAnimJoint327)

HAnimJoint314.children.append(HAnimJoint319)

HAnimJoint312.children.append(HAnimJoint314)

HAnimJoint310.children.append(HAnimJoint312)

HAnimJoint308.children.append(HAnimJoint310)

HAnimJoint297.children.append(HAnimJoint308)

HAnimJoint295.children.append(HAnimJoint297)

HAnimJoint293.children.append(HAnimJoint295)

HAnimJoint282.children.append(HAnimJoint293)

HAnimJoint17.children.append(HAnimJoint282)

HAnimHumanoid14.joints.append(HAnimJoint17)
HAnimJoint686 = x3d.HAnimJoint()
HAnimJoint686.USE = "STD_Joint_humanoid_root"
HAnimJoint686.bboxCenter = [0,0,0]
HAnimJoint686.bboxDisplay = False
HAnimJoint686.bboxSize = [-1,-1,-1]
HAnimJoint686.visible = True

HAnimHumanoid14.joints.append(HAnimJoint686)
HAnimJoint687 = x3d.HAnimJoint()
HAnimJoint687.USE = "STD_Joint_sacroiliac"
HAnimJoint687.bboxCenter = [0,0,0]
HAnimJoint687.bboxDisplay = False
HAnimJoint687.bboxSize = [-1,-1,-1]
HAnimJoint687.visible = True

HAnimHumanoid14.joints.append(HAnimJoint687)
HAnimJoint688 = x3d.HAnimJoint()
HAnimJoint688.USE = "STD_Joint_vl5"
HAnimJoint688.bboxCenter = [0,0,0]
HAnimJoint688.bboxDisplay = False
HAnimJoint688.bboxSize = [-1,-1,-1]
HAnimJoint688.visible = True

HAnimHumanoid14.joints.append(HAnimJoint688)
HAnimJoint689 = x3d.HAnimJoint()
HAnimJoint689.USE = "STD_Joint_vl4"
HAnimJoint689.bboxCenter = [0,0,0]
HAnimJoint689.bboxDisplay = False
HAnimJoint689.bboxSize = [-1,-1,-1]
HAnimJoint689.visible = True

HAnimHumanoid14.joints.append(HAnimJoint689)
HAnimJoint690 = x3d.HAnimJoint()
HAnimJoint690.USE = "STD_Joint_vl3"
HAnimJoint690.bboxCenter = [0,0,0]
HAnimJoint690.bboxDisplay = False
HAnimJoint690.bboxSize = [-1,-1,-1]
HAnimJoint690.visible = True

HAnimHumanoid14.joints.append(HAnimJoint690)
HAnimJoint691 = x3d.HAnimJoint()
HAnimJoint691.USE = "STD_Joint_vl2"
HAnimJoint691.bboxCenter = [0,0,0]
HAnimJoint691.bboxDisplay = False
HAnimJoint691.bboxSize = [-1,-1,-1]
HAnimJoint691.visible = True

HAnimHumanoid14.joints.append(HAnimJoint691)
HAnimJoint692 = x3d.HAnimJoint()
HAnimJoint692.USE = "STD_Joint_vl1"
HAnimJoint692.bboxCenter = [0,0,0]
HAnimJoint692.bboxDisplay = False
HAnimJoint692.bboxSize = [-1,-1,-1]
HAnimJoint692.visible = True

HAnimHumanoid14.joints.append(HAnimJoint692)
HAnimJoint693 = x3d.HAnimJoint()
HAnimJoint693.USE = "STD_Joint_vt12"
HAnimJoint693.bboxCenter = [0,0,0]
HAnimJoint693.bboxDisplay = False
HAnimJoint693.bboxSize = [-1,-1,-1]
HAnimJoint693.visible = True

HAnimHumanoid14.joints.append(HAnimJoint693)
HAnimJoint694 = x3d.HAnimJoint()
HAnimJoint694.USE = "STD_Joint_vt11"
HAnimJoint694.bboxCenter = [0,0,0]
HAnimJoint694.bboxDisplay = False
HAnimJoint694.bboxSize = [-1,-1,-1]
HAnimJoint694.visible = True

HAnimHumanoid14.joints.append(HAnimJoint694)
HAnimJoint695 = x3d.HAnimJoint()
HAnimJoint695.USE = "STD_Joint_vt10"
HAnimJoint695.bboxCenter = [0,0,0]
HAnimJoint695.bboxDisplay = False
HAnimJoint695.bboxSize = [-1,-1,-1]
HAnimJoint695.visible = True

HAnimHumanoid14.joints.append(HAnimJoint695)
HAnimJoint696 = x3d.HAnimJoint()
HAnimJoint696.USE = "STD_Joint_vt9"
HAnimJoint696.bboxCenter = [0,0,0]
HAnimJoint696.bboxDisplay = False
HAnimJoint696.bboxSize = [-1,-1,-1]
HAnimJoint696.visible = True

HAnimHumanoid14.joints.append(HAnimJoint696)
HAnimJoint697 = x3d.HAnimJoint()
HAnimJoint697.USE = "STD_Joint_vt8"
HAnimJoint697.bboxCenter = [0,0,0]
HAnimJoint697.bboxDisplay = False
HAnimJoint697.bboxSize = [-1,-1,-1]
HAnimJoint697.visible = True

HAnimHumanoid14.joints.append(HAnimJoint697)
HAnimJoint698 = x3d.HAnimJoint()
HAnimJoint698.USE = "STD_Joint_vt7"
HAnimJoint698.bboxCenter = [0,0,0]
HAnimJoint698.bboxDisplay = False
HAnimJoint698.bboxSize = [-1,-1,-1]
HAnimJoint698.visible = True

HAnimHumanoid14.joints.append(HAnimJoint698)
HAnimJoint699 = x3d.HAnimJoint()
HAnimJoint699.USE = "STD_Joint_vt6"
HAnimJoint699.bboxCenter = [0,0,0]
HAnimJoint699.bboxDisplay = False
HAnimJoint699.bboxSize = [-1,-1,-1]
HAnimJoint699.visible = True

HAnimHumanoid14.joints.append(HAnimJoint699)
HAnimJoint700 = x3d.HAnimJoint()
HAnimJoint700.USE = "STD_Joint_vt5"
HAnimJoint700.bboxCenter = [0,0,0]
HAnimJoint700.bboxDisplay = False
HAnimJoint700.bboxSize = [-1,-1,-1]
HAnimJoint700.visible = True

HAnimHumanoid14.joints.append(HAnimJoint700)
HAnimJoint701 = x3d.HAnimJoint()
HAnimJoint701.USE = "STD_Joint_vt4"
HAnimJoint701.bboxCenter = [0,0,0]
HAnimJoint701.bboxDisplay = False
HAnimJoint701.bboxSize = [-1,-1,-1]
HAnimJoint701.visible = True

HAnimHumanoid14.joints.append(HAnimJoint701)
HAnimJoint702 = x3d.HAnimJoint()
HAnimJoint702.USE = "STD_Joint_vt3"
HAnimJoint702.bboxCenter = [0,0,0]
HAnimJoint702.bboxDisplay = False
HAnimJoint702.bboxSize = [-1,-1,-1]
HAnimJoint702.visible = True

HAnimHumanoid14.joints.append(HAnimJoint702)
HAnimJoint703 = x3d.HAnimJoint()
HAnimJoint703.USE = "STD_Joint_vt2"
HAnimJoint703.bboxCenter = [0,0,0]
HAnimJoint703.bboxDisplay = False
HAnimJoint703.bboxSize = [-1,-1,-1]
HAnimJoint703.visible = True

HAnimHumanoid14.joints.append(HAnimJoint703)
HAnimJoint704 = x3d.HAnimJoint()
HAnimJoint704.USE = "STD_Joint_vt1"
HAnimJoint704.bboxCenter = [0,0,0]
HAnimJoint704.bboxDisplay = False
HAnimJoint704.bboxSize = [-1,-1,-1]
HAnimJoint704.visible = True

HAnimHumanoid14.joints.append(HAnimJoint704)
HAnimJoint705 = x3d.HAnimJoint()
HAnimJoint705.USE = "STD_Joint_vc7"
HAnimJoint705.bboxCenter = [0,0,0]
HAnimJoint705.bboxDisplay = False
HAnimJoint705.bboxSize = [-1,-1,-1]
HAnimJoint705.visible = True

HAnimHumanoid14.joints.append(HAnimJoint705)
HAnimJoint706 = x3d.HAnimJoint()
HAnimJoint706.USE = "STD_Joint_vc6"
HAnimJoint706.bboxCenter = [0,0,0]
HAnimJoint706.bboxDisplay = False
HAnimJoint706.bboxSize = [-1,-1,-1]
HAnimJoint706.visible = True

HAnimHumanoid14.joints.append(HAnimJoint706)
HAnimJoint707 = x3d.HAnimJoint()
HAnimJoint707.USE = "STD_Joint_vc5"
HAnimJoint707.bboxCenter = [0,0,0]
HAnimJoint707.bboxDisplay = False
HAnimJoint707.bboxSize = [-1,-1,-1]
HAnimJoint707.visible = True

HAnimHumanoid14.joints.append(HAnimJoint707)
HAnimJoint708 = x3d.HAnimJoint()
HAnimJoint708.USE = "STD_Joint_vc4"
HAnimJoint708.bboxCenter = [0,0,0]
HAnimJoint708.bboxDisplay = False
HAnimJoint708.bboxSize = [-1,-1,-1]
HAnimJoint708.visible = True

HAnimHumanoid14.joints.append(HAnimJoint708)
HAnimJoint709 = x3d.HAnimJoint()
HAnimJoint709.USE = "STD_Joint_vc3"
HAnimJoint709.bboxCenter = [0,0,0]
HAnimJoint709.bboxDisplay = False
HAnimJoint709.bboxSize = [-1,-1,-1]
HAnimJoint709.visible = True

HAnimHumanoid14.joints.append(HAnimJoint709)
HAnimJoint710 = x3d.HAnimJoint()
HAnimJoint710.USE = "STD_Joint_vc2"
HAnimJoint710.bboxCenter = [0,0,0]
HAnimJoint710.bboxDisplay = False
HAnimJoint710.bboxSize = [-1,-1,-1]
HAnimJoint710.visible = True

HAnimHumanoid14.joints.append(HAnimJoint710)
HAnimJoint711 = x3d.HAnimJoint()
HAnimJoint711.USE = "STD_Joint_vc1"
HAnimJoint711.bboxCenter = [0,0,0]
HAnimJoint711.bboxDisplay = False
HAnimJoint711.bboxSize = [-1,-1,-1]
HAnimJoint711.visible = True

HAnimHumanoid14.joints.append(HAnimJoint711)
HAnimJoint712 = x3d.HAnimJoint()
HAnimJoint712.USE = "STD_Joint_skullbase"
HAnimJoint712.bboxCenter = [0,0,0]
HAnimJoint712.bboxDisplay = False
HAnimJoint712.bboxSize = [-1,-1,-1]
HAnimJoint712.visible = True

HAnimHumanoid14.joints.append(HAnimJoint712)
HAnimJoint713 = x3d.HAnimJoint()
HAnimJoint713.USE = "STD_Joint_temporomandibular"
HAnimJoint713.bboxCenter = [0,0,0]
HAnimJoint713.bboxDisplay = False
HAnimJoint713.bboxSize = [-1,-1,-1]
HAnimJoint713.visible = True

HAnimHumanoid14.joints.append(HAnimJoint713)
HAnimJoint714 = x3d.HAnimJoint()
HAnimJoint714.USE = "STD_Joint_l_acromioclavicular"
HAnimJoint714.bboxCenter = [0,0,0]
HAnimJoint714.bboxDisplay = False
HAnimJoint714.bboxSize = [-1,-1,-1]
HAnimJoint714.visible = True

HAnimHumanoid14.joints.append(HAnimJoint714)
HAnimJoint715 = x3d.HAnimJoint()
HAnimJoint715.USE = "STD_Joint_r_acromioclavicular"
HAnimJoint715.bboxCenter = [0,0,0]
HAnimJoint715.bboxDisplay = False
HAnimJoint715.bboxSize = [-1,-1,-1]
HAnimJoint715.visible = True

HAnimHumanoid14.joints.append(HAnimJoint715)
HAnimJoint716 = x3d.HAnimJoint()
HAnimJoint716.USE = "STD_Joint_l_calcaneocuboid"
HAnimJoint716.bboxCenter = [0,0,0]
HAnimJoint716.bboxDisplay = False
HAnimJoint716.bboxSize = [-1,-1,-1]
HAnimJoint716.visible = True

HAnimHumanoid14.joints.append(HAnimJoint716)
HAnimJoint717 = x3d.HAnimJoint()
HAnimJoint717.USE = "STD_Joint_r_calcaneocuboid"
HAnimJoint717.bboxCenter = [0,0,0]
HAnimJoint717.bboxDisplay = False
HAnimJoint717.bboxSize = [-1,-1,-1]
HAnimJoint717.visible = True

HAnimHumanoid14.joints.append(HAnimJoint717)
HAnimJoint718 = x3d.HAnimJoint()
HAnimJoint718.USE = "STD_Joint_l_carpal_distal_interphalangeal_2"
HAnimJoint718.bboxCenter = [0,0,0]
HAnimJoint718.bboxDisplay = False
HAnimJoint718.bboxSize = [-1,-1,-1]
HAnimJoint718.visible = True

HAnimHumanoid14.joints.append(HAnimJoint718)
HAnimJoint719 = x3d.HAnimJoint()
HAnimJoint719.USE = "STD_Joint_r_carpal_distal_interphalangeal_2"
HAnimJoint719.bboxCenter = [0,0,0]
HAnimJoint719.bboxDisplay = False
HAnimJoint719.bboxSize = [-1,-1,-1]
HAnimJoint719.visible = True

HAnimHumanoid14.joints.append(HAnimJoint719)
HAnimJoint720 = x3d.HAnimJoint()
HAnimJoint720.USE = "STD_Joint_l_carpal_distal_interphalangeal_3"
HAnimJoint720.bboxCenter = [0,0,0]
HAnimJoint720.bboxDisplay = False
HAnimJoint720.bboxSize = [-1,-1,-1]
HAnimJoint720.visible = True

HAnimHumanoid14.joints.append(HAnimJoint720)
HAnimJoint721 = x3d.HAnimJoint()
HAnimJoint721.USE = "STD_Joint_r_carpal_distal_interphalangeal_3"
HAnimJoint721.bboxCenter = [0,0,0]
HAnimJoint721.bboxDisplay = False
HAnimJoint721.bboxSize = [-1,-1,-1]
HAnimJoint721.visible = True

HAnimHumanoid14.joints.append(HAnimJoint721)
HAnimJoint722 = x3d.HAnimJoint()
HAnimJoint722.USE = "STD_Joint_l_carpal_distal_interphalangeal_4"
HAnimJoint722.bboxCenter = [0,0,0]
HAnimJoint722.bboxDisplay = False
HAnimJoint722.bboxSize = [-1,-1,-1]
HAnimJoint722.visible = True

HAnimHumanoid14.joints.append(HAnimJoint722)
HAnimJoint723 = x3d.HAnimJoint()
HAnimJoint723.USE = "STD_Joint_r_carpal_distal_interphalangeal_4"
HAnimJoint723.bboxCenter = [0,0,0]
HAnimJoint723.bboxDisplay = False
HAnimJoint723.bboxSize = [-1,-1,-1]
HAnimJoint723.visible = True

HAnimHumanoid14.joints.append(HAnimJoint723)
HAnimJoint724 = x3d.HAnimJoint()
HAnimJoint724.USE = "STD_Joint_l_carpal_distal_interphalangeal_5"
HAnimJoint724.bboxCenter = [0,0,0]
HAnimJoint724.bboxDisplay = False
HAnimJoint724.bboxSize = [-1,-1,-1]
HAnimJoint724.visible = True

HAnimHumanoid14.joints.append(HAnimJoint724)
HAnimJoint725 = x3d.HAnimJoint()
HAnimJoint725.USE = "STD_Joint_r_carpal_distal_interphalangeal_5"
HAnimJoint725.bboxCenter = [0,0,0]
HAnimJoint725.bboxDisplay = False
HAnimJoint725.bboxSize = [-1,-1,-1]
HAnimJoint725.visible = True

HAnimHumanoid14.joints.append(HAnimJoint725)
HAnimJoint726 = x3d.HAnimJoint()
HAnimJoint726.USE = "STD_Joint_l_carpal_interphalangeal_1"
HAnimJoint726.bboxCenter = [0,0,0]
HAnimJoint726.bboxDisplay = False
HAnimJoint726.bboxSize = [-1,-1,-1]
HAnimJoint726.visible = True

HAnimHumanoid14.joints.append(HAnimJoint726)
HAnimJoint727 = x3d.HAnimJoint()
HAnimJoint727.USE = "STD_Joint_r_carpal_interphalangeal_1"
HAnimJoint727.bboxCenter = [0,0,0]
HAnimJoint727.bboxDisplay = False
HAnimJoint727.bboxSize = [-1,-1,-1]
HAnimJoint727.visible = True

HAnimHumanoid14.joints.append(HAnimJoint727)
HAnimJoint728 = x3d.HAnimJoint()
HAnimJoint728.USE = "STD_Joint_l_carpal_proximal_interphalangeal_2"
HAnimJoint728.bboxCenter = [0,0,0]
HAnimJoint728.bboxDisplay = False
HAnimJoint728.bboxSize = [-1,-1,-1]
HAnimJoint728.visible = True

HAnimHumanoid14.joints.append(HAnimJoint728)
HAnimJoint729 = x3d.HAnimJoint()
HAnimJoint729.USE = "STD_Joint_r_carpal_proximal_interphalangeal_2"
HAnimJoint729.bboxCenter = [0,0,0]
HAnimJoint729.bboxDisplay = False
HAnimJoint729.bboxSize = [-1,-1,-1]
HAnimJoint729.visible = True

HAnimHumanoid14.joints.append(HAnimJoint729)
HAnimJoint730 = x3d.HAnimJoint()
HAnimJoint730.USE = "STD_Joint_l_carpal_proximal_interphalangeal_3"
HAnimJoint730.bboxCenter = [0,0,0]
HAnimJoint730.bboxDisplay = False
HAnimJoint730.bboxSize = [-1,-1,-1]
HAnimJoint730.visible = True

HAnimHumanoid14.joints.append(HAnimJoint730)
HAnimJoint731 = x3d.HAnimJoint()
HAnimJoint731.USE = "STD_Joint_r_carpal_proximal_interphalangeal_3"
HAnimJoint731.bboxCenter = [0,0,0]
HAnimJoint731.bboxDisplay = False
HAnimJoint731.bboxSize = [-1,-1,-1]
HAnimJoint731.visible = True

HAnimHumanoid14.joints.append(HAnimJoint731)
HAnimJoint732 = x3d.HAnimJoint()
HAnimJoint732.USE = "STD_Joint_l_carpal_proximal_interphalangeal_4"
HAnimJoint732.bboxCenter = [0,0,0]
HAnimJoint732.bboxDisplay = False
HAnimJoint732.bboxSize = [-1,-1,-1]
HAnimJoint732.visible = True

HAnimHumanoid14.joints.append(HAnimJoint732)
HAnimJoint733 = x3d.HAnimJoint()
HAnimJoint733.USE = "STD_Joint_r_carpal_proximal_interphalangeal_4"
HAnimJoint733.bboxCenter = [0,0,0]
HAnimJoint733.bboxDisplay = False
HAnimJoint733.bboxSize = [-1,-1,-1]
HAnimJoint733.visible = True

HAnimHumanoid14.joints.append(HAnimJoint733)
HAnimJoint734 = x3d.HAnimJoint()
HAnimJoint734.USE = "STD_Joint_l_carpal_proximal_interphalangeal_5"
HAnimJoint734.bboxCenter = [0,0,0]
HAnimJoint734.bboxDisplay = False
HAnimJoint734.bboxSize = [-1,-1,-1]
HAnimJoint734.visible = True

HAnimHumanoid14.joints.append(HAnimJoint734)
HAnimJoint735 = x3d.HAnimJoint()
HAnimJoint735.USE = "STD_Joint_r_carpal_proximal_interphalangeal_5"
HAnimJoint735.bboxCenter = [0,0,0]
HAnimJoint735.bboxDisplay = False
HAnimJoint735.bboxSize = [-1,-1,-1]
HAnimJoint735.visible = True

HAnimHumanoid14.joints.append(HAnimJoint735)
HAnimJoint736 = x3d.HAnimJoint()
HAnimJoint736.USE = "STD_Joint_l_carpometacarpal_1"
HAnimJoint736.bboxCenter = [0,0,0]
HAnimJoint736.bboxDisplay = False
HAnimJoint736.bboxSize = [-1,-1,-1]
HAnimJoint736.visible = True

HAnimHumanoid14.joints.append(HAnimJoint736)
HAnimJoint737 = x3d.HAnimJoint()
HAnimJoint737.USE = "STD_Joint_r_carpometacarpal_1"
HAnimJoint737.bboxCenter = [0,0,0]
HAnimJoint737.bboxDisplay = False
HAnimJoint737.bboxSize = [-1,-1,-1]
HAnimJoint737.visible = True

HAnimHumanoid14.joints.append(HAnimJoint737)
HAnimJoint738 = x3d.HAnimJoint()
HAnimJoint738.USE = "STD_Joint_l_carpometacarpal_2"
HAnimJoint738.bboxCenter = [0,0,0]
HAnimJoint738.bboxDisplay = False
HAnimJoint738.bboxSize = [-1,-1,-1]
HAnimJoint738.visible = True

HAnimHumanoid14.joints.append(HAnimJoint738)
HAnimJoint739 = x3d.HAnimJoint()
HAnimJoint739.USE = "STD_Joint_r_carpometacarpal_2"
HAnimJoint739.bboxCenter = [0,0,0]
HAnimJoint739.bboxDisplay = False
HAnimJoint739.bboxSize = [-1,-1,-1]
HAnimJoint739.visible = True

HAnimHumanoid14.joints.append(HAnimJoint739)
HAnimJoint740 = x3d.HAnimJoint()
HAnimJoint740.USE = "STD_Joint_l_carpometacarpal_3"
HAnimJoint740.bboxCenter = [0,0,0]
HAnimJoint740.bboxDisplay = False
HAnimJoint740.bboxSize = [-1,-1,-1]
HAnimJoint740.visible = True

HAnimHumanoid14.joints.append(HAnimJoint740)
HAnimJoint741 = x3d.HAnimJoint()
HAnimJoint741.USE = "STD_Joint_r_carpometacarpal_3"
HAnimJoint741.bboxCenter = [0,0,0]
HAnimJoint741.bboxDisplay = False
HAnimJoint741.bboxSize = [-1,-1,-1]
HAnimJoint741.visible = True

HAnimHumanoid14.joints.append(HAnimJoint741)
HAnimJoint742 = x3d.HAnimJoint()
HAnimJoint742.USE = "STD_Joint_l_carpometacarpal_4"
HAnimJoint742.bboxCenter = [0,0,0]
HAnimJoint742.bboxDisplay = False
HAnimJoint742.bboxSize = [-1,-1,-1]
HAnimJoint742.visible = True

HAnimHumanoid14.joints.append(HAnimJoint742)
HAnimJoint743 = x3d.HAnimJoint()
HAnimJoint743.USE = "STD_Joint_r_carpometacarpal_4"
HAnimJoint743.bboxCenter = [0,0,0]
HAnimJoint743.bboxDisplay = False
HAnimJoint743.bboxSize = [-1,-1,-1]
HAnimJoint743.visible = True

HAnimHumanoid14.joints.append(HAnimJoint743)
HAnimJoint744 = x3d.HAnimJoint()
HAnimJoint744.USE = "STD_Joint_l_carpometacarpal_5"
HAnimJoint744.bboxCenter = [0,0,0]
HAnimJoint744.bboxDisplay = False
HAnimJoint744.bboxSize = [-1,-1,-1]
HAnimJoint744.visible = True

HAnimHumanoid14.joints.append(HAnimJoint744)
HAnimJoint745 = x3d.HAnimJoint()
HAnimJoint745.USE = "STD_Joint_r_carpometacarpal_5"
HAnimJoint745.bboxCenter = [0,0,0]
HAnimJoint745.bboxDisplay = False
HAnimJoint745.bboxSize = [-1,-1,-1]
HAnimJoint745.visible = True

HAnimHumanoid14.joints.append(HAnimJoint745)
HAnimJoint746 = x3d.HAnimJoint()
HAnimJoint746.USE = "STD_Joint_l_cuneonavicular_1"
HAnimJoint746.bboxCenter = [0,0,0]
HAnimJoint746.bboxDisplay = False
HAnimJoint746.bboxSize = [-1,-1,-1]
HAnimJoint746.visible = True

HAnimHumanoid14.joints.append(HAnimJoint746)
HAnimJoint747 = x3d.HAnimJoint()
HAnimJoint747.USE = "STD_Joint_r_cuneonavicular_1"
HAnimJoint747.bboxCenter = [0,0,0]
HAnimJoint747.bboxDisplay = False
HAnimJoint747.bboxSize = [-1,-1,-1]
HAnimJoint747.visible = True

HAnimHumanoid14.joints.append(HAnimJoint747)
HAnimJoint748 = x3d.HAnimJoint()
HAnimJoint748.USE = "STD_Joint_l_cuneonavicular_2"
HAnimJoint748.bboxCenter = [0,0,0]
HAnimJoint748.bboxDisplay = False
HAnimJoint748.bboxSize = [-1,-1,-1]
HAnimJoint748.visible = True

HAnimHumanoid14.joints.append(HAnimJoint748)
HAnimJoint749 = x3d.HAnimJoint()
HAnimJoint749.USE = "STD_Joint_r_cuneonavicular_2"
HAnimJoint749.bboxCenter = [0,0,0]
HAnimJoint749.bboxDisplay = False
HAnimJoint749.bboxSize = [-1,-1,-1]
HAnimJoint749.visible = True

HAnimHumanoid14.joints.append(HAnimJoint749)
HAnimJoint750 = x3d.HAnimJoint()
HAnimJoint750.USE = "STD_Joint_l_cuneonavicular_3"
HAnimJoint750.bboxCenter = [0,0,0]
HAnimJoint750.bboxDisplay = False
HAnimJoint750.bboxSize = [-1,-1,-1]
HAnimJoint750.visible = True

HAnimHumanoid14.joints.append(HAnimJoint750)
HAnimJoint751 = x3d.HAnimJoint()
HAnimJoint751.USE = "STD_Joint_r_cuneonavicular_3"
HAnimJoint751.bboxCenter = [0,0,0]
HAnimJoint751.bboxDisplay = False
HAnimJoint751.bboxSize = [-1,-1,-1]
HAnimJoint751.visible = True

HAnimHumanoid14.joints.append(HAnimJoint751)
HAnimJoint752 = x3d.HAnimJoint()
HAnimJoint752.USE = "STD_Joint_l_elbow"
HAnimJoint752.bboxCenter = [0,0,0]
HAnimJoint752.bboxDisplay = False
HAnimJoint752.bboxSize = [-1,-1,-1]
HAnimJoint752.visible = True

HAnimHumanoid14.joints.append(HAnimJoint752)
HAnimJoint753 = x3d.HAnimJoint()
HAnimJoint753.USE = "STD_Joint_r_elbow"
HAnimJoint753.bboxCenter = [0,0,0]
HAnimJoint753.bboxDisplay = False
HAnimJoint753.bboxSize = [-1,-1,-1]
HAnimJoint753.visible = True

HAnimHumanoid14.joints.append(HAnimJoint753)
HAnimJoint754 = x3d.HAnimJoint()
HAnimJoint754.USE = "STD_Joint_l_eyeball_joint"
HAnimJoint754.bboxCenter = [0,0,0]
HAnimJoint754.bboxDisplay = False
HAnimJoint754.bboxSize = [-1,-1,-1]
HAnimJoint754.visible = True

HAnimHumanoid14.joints.append(HAnimJoint754)
HAnimJoint755 = x3d.HAnimJoint()
HAnimJoint755.USE = "STD_Joint_r_eyeball_joint"
HAnimJoint755.bboxCenter = [0,0,0]
HAnimJoint755.bboxDisplay = False
HAnimJoint755.bboxSize = [-1,-1,-1]
HAnimJoint755.visible = True

HAnimHumanoid14.joints.append(HAnimJoint755)
HAnimJoint756 = x3d.HAnimJoint()
HAnimJoint756.USE = "STD_Joint_l_eyebrow_joint"
HAnimJoint756.bboxCenter = [0,0,0]
HAnimJoint756.bboxDisplay = False
HAnimJoint756.bboxSize = [-1,-1,-1]
HAnimJoint756.visible = True

HAnimHumanoid14.joints.append(HAnimJoint756)
HAnimJoint757 = x3d.HAnimJoint()
HAnimJoint757.USE = "STD_Joint_r_eyebrow_joint"
HAnimJoint757.bboxCenter = [0,0,0]
HAnimJoint757.bboxDisplay = False
HAnimJoint757.bboxSize = [-1,-1,-1]
HAnimJoint757.visible = True

HAnimHumanoid14.joints.append(HAnimJoint757)
HAnimJoint758 = x3d.HAnimJoint()
HAnimJoint758.USE = "STD_Joint_l_eyelid_joint"
HAnimJoint758.bboxCenter = [0,0,0]
HAnimJoint758.bboxDisplay = False
HAnimJoint758.bboxSize = [-1,-1,-1]
HAnimJoint758.visible = True

HAnimHumanoid14.joints.append(HAnimJoint758)
HAnimJoint759 = x3d.HAnimJoint()
HAnimJoint759.USE = "STD_Joint_r_eyelid_joint"
HAnimJoint759.bboxCenter = [0,0,0]
HAnimJoint759.bboxDisplay = False
HAnimJoint759.bboxSize = [-1,-1,-1]
HAnimJoint759.visible = True

HAnimHumanoid14.joints.append(HAnimJoint759)
HAnimJoint760 = x3d.HAnimJoint()
HAnimJoint760.USE = "STD_Joint_l_hip"
HAnimJoint760.bboxCenter = [0,0,0]
HAnimJoint760.bboxDisplay = False
HAnimJoint760.bboxSize = [-1,-1,-1]
HAnimJoint760.visible = True

HAnimHumanoid14.joints.append(HAnimJoint760)
HAnimJoint761 = x3d.HAnimJoint()
HAnimJoint761.USE = "STD_Joint_r_hip"
HAnimJoint761.bboxCenter = [0,0,0]
HAnimJoint761.bboxDisplay = False
HAnimJoint761.bboxSize = [-1,-1,-1]
HAnimJoint761.visible = True

HAnimHumanoid14.joints.append(HAnimJoint761)
HAnimJoint762 = x3d.HAnimJoint()
HAnimJoint762.USE = "STD_Joint_l_knee"
HAnimJoint762.bboxCenter = [0,0,0]
HAnimJoint762.bboxDisplay = False
HAnimJoint762.bboxSize = [-1,-1,-1]
HAnimJoint762.visible = True

HAnimHumanoid14.joints.append(HAnimJoint762)
HAnimJoint763 = x3d.HAnimJoint()
HAnimJoint763.USE = "STD_Joint_r_knee"
HAnimJoint763.bboxCenter = [0,0,0]
HAnimJoint763.bboxDisplay = False
HAnimJoint763.bboxSize = [-1,-1,-1]
HAnimJoint763.visible = True

HAnimHumanoid14.joints.append(HAnimJoint763)
HAnimJoint764 = x3d.HAnimJoint()
HAnimJoint764.USE = "STD_Joint_l_metacarpophalangeal_1"
HAnimJoint764.bboxCenter = [0,0,0]
HAnimJoint764.bboxDisplay = False
HAnimJoint764.bboxSize = [-1,-1,-1]
HAnimJoint764.visible = True

HAnimHumanoid14.joints.append(HAnimJoint764)
HAnimJoint765 = x3d.HAnimJoint()
HAnimJoint765.USE = "STD_Joint_r_metacarpophalangeal_1"
HAnimJoint765.bboxCenter = [0,0,0]
HAnimJoint765.bboxDisplay = False
HAnimJoint765.bboxSize = [-1,-1,-1]
HAnimJoint765.visible = True

HAnimHumanoid14.joints.append(HAnimJoint765)
HAnimJoint766 = x3d.HAnimJoint()
HAnimJoint766.USE = "STD_Joint_l_metacarpophalangeal_2"
HAnimJoint766.bboxCenter = [0,0,0]
HAnimJoint766.bboxDisplay = False
HAnimJoint766.bboxSize = [-1,-1,-1]
HAnimJoint766.visible = True

HAnimHumanoid14.joints.append(HAnimJoint766)
HAnimJoint767 = x3d.HAnimJoint()
HAnimJoint767.USE = "STD_Joint_r_metacarpophalangeal_2"
HAnimJoint767.bboxCenter = [0,0,0]
HAnimJoint767.bboxDisplay = False
HAnimJoint767.bboxSize = [-1,-1,-1]
HAnimJoint767.visible = True

HAnimHumanoid14.joints.append(HAnimJoint767)
HAnimJoint768 = x3d.HAnimJoint()
HAnimJoint768.USE = "STD_Joint_l_metacarpophalangeal_3"
HAnimJoint768.bboxCenter = [0,0,0]
HAnimJoint768.bboxDisplay = False
HAnimJoint768.bboxSize = [-1,-1,-1]
HAnimJoint768.visible = True

HAnimHumanoid14.joints.append(HAnimJoint768)
HAnimJoint769 = x3d.HAnimJoint()
HAnimJoint769.USE = "STD_Joint_r_metacarpophalangeal_3"
HAnimJoint769.bboxCenter = [0,0,0]
HAnimJoint769.bboxDisplay = False
HAnimJoint769.bboxSize = [-1,-1,-1]
HAnimJoint769.visible = True

HAnimHumanoid14.joints.append(HAnimJoint769)
HAnimJoint770 = x3d.HAnimJoint()
HAnimJoint770.USE = "STD_Joint_l_metacarpophalangeal_4"
HAnimJoint770.bboxCenter = [0,0,0]
HAnimJoint770.bboxDisplay = False
HAnimJoint770.bboxSize = [-1,-1,-1]
HAnimJoint770.visible = True

HAnimHumanoid14.joints.append(HAnimJoint770)
HAnimJoint771 = x3d.HAnimJoint()
HAnimJoint771.USE = "STD_Joint_r_metacarpophalangeal_4"
HAnimJoint771.bboxCenter = [0,0,0]
HAnimJoint771.bboxDisplay = False
HAnimJoint771.bboxSize = [-1,-1,-1]
HAnimJoint771.visible = True

HAnimHumanoid14.joints.append(HAnimJoint771)
HAnimJoint772 = x3d.HAnimJoint()
HAnimJoint772.USE = "STD_Joint_l_metacarpophalangeal_5"
HAnimJoint772.bboxCenter = [0,0,0]
HAnimJoint772.bboxDisplay = False
HAnimJoint772.bboxSize = [-1,-1,-1]
HAnimJoint772.visible = True

HAnimHumanoid14.joints.append(HAnimJoint772)
HAnimJoint773 = x3d.HAnimJoint()
HAnimJoint773.USE = "STD_Joint_r_metacarpophalangeal_5"
HAnimJoint773.bboxCenter = [0,0,0]
HAnimJoint773.bboxDisplay = False
HAnimJoint773.bboxSize = [-1,-1,-1]
HAnimJoint773.visible = True

HAnimHumanoid14.joints.append(HAnimJoint773)
HAnimJoint774 = x3d.HAnimJoint()
HAnimJoint774.USE = "STD_Joint_l_metatarsophalangeal_1"
HAnimJoint774.bboxCenter = [0,0,0]
HAnimJoint774.bboxDisplay = False
HAnimJoint774.bboxSize = [-1,-1,-1]
HAnimJoint774.visible = True

HAnimHumanoid14.joints.append(HAnimJoint774)
HAnimJoint775 = x3d.HAnimJoint()
HAnimJoint775.USE = "STD_Joint_r_metatarsophalangeal_1"
HAnimJoint775.bboxCenter = [0,0,0]
HAnimJoint775.bboxDisplay = False
HAnimJoint775.bboxSize = [-1,-1,-1]
HAnimJoint775.visible = True

HAnimHumanoid14.joints.append(HAnimJoint775)
HAnimJoint776 = x3d.HAnimJoint()
HAnimJoint776.USE = "STD_Joint_l_metatarsophalangeal_2"
HAnimJoint776.bboxCenter = [0,0,0]
HAnimJoint776.bboxDisplay = False
HAnimJoint776.bboxSize = [-1,-1,-1]
HAnimJoint776.visible = True

HAnimHumanoid14.joints.append(HAnimJoint776)
HAnimJoint777 = x3d.HAnimJoint()
HAnimJoint777.USE = "STD_Joint_r_metatarsophalangeal_2"
HAnimJoint777.bboxCenter = [0,0,0]
HAnimJoint777.bboxDisplay = False
HAnimJoint777.bboxSize = [-1,-1,-1]
HAnimJoint777.visible = True

HAnimHumanoid14.joints.append(HAnimJoint777)
HAnimJoint778 = x3d.HAnimJoint()
HAnimJoint778.USE = "STD_Joint_l_metatarsophalangeal_3"
HAnimJoint778.bboxCenter = [0,0,0]
HAnimJoint778.bboxDisplay = False
HAnimJoint778.bboxSize = [-1,-1,-1]
HAnimJoint778.visible = True

HAnimHumanoid14.joints.append(HAnimJoint778)
HAnimJoint779 = x3d.HAnimJoint()
HAnimJoint779.USE = "STD_Joint_r_metatarsophalangeal_3"
HAnimJoint779.bboxCenter = [0,0,0]
HAnimJoint779.bboxDisplay = False
HAnimJoint779.bboxSize = [-1,-1,-1]
HAnimJoint779.visible = True

HAnimHumanoid14.joints.append(HAnimJoint779)
HAnimJoint780 = x3d.HAnimJoint()
HAnimJoint780.USE = "STD_Joint_l_metatarsophalangeal_4"
HAnimJoint780.bboxCenter = [0,0,0]
HAnimJoint780.bboxDisplay = False
HAnimJoint780.bboxSize = [-1,-1,-1]
HAnimJoint780.visible = True

HAnimHumanoid14.joints.append(HAnimJoint780)
HAnimJoint781 = x3d.HAnimJoint()
HAnimJoint781.USE = "STD_Joint_r_metatarsophalangeal_4"
HAnimJoint781.bboxCenter = [0,0,0]
HAnimJoint781.bboxDisplay = False
HAnimJoint781.bboxSize = [-1,-1,-1]
HAnimJoint781.visible = True

HAnimHumanoid14.joints.append(HAnimJoint781)
HAnimJoint782 = x3d.HAnimJoint()
HAnimJoint782.USE = "STD_Joint_l_metatarsophalangeal_5"
HAnimJoint782.bboxCenter = [0,0,0]
HAnimJoint782.bboxDisplay = False
HAnimJoint782.bboxSize = [-1,-1,-1]
HAnimJoint782.visible = True

HAnimHumanoid14.joints.append(HAnimJoint782)
HAnimJoint783 = x3d.HAnimJoint()
HAnimJoint783.USE = "STD_Joint_r_metatarsophalangeal_5"
HAnimJoint783.bboxCenter = [0,0,0]
HAnimJoint783.bboxDisplay = False
HAnimJoint783.bboxSize = [-1,-1,-1]
HAnimJoint783.visible = True

HAnimHumanoid14.joints.append(HAnimJoint783)
HAnimJoint784 = x3d.HAnimJoint()
HAnimJoint784.USE = "STD_Joint_l_midcarpal_1"
HAnimJoint784.bboxCenter = [0,0,0]
HAnimJoint784.bboxDisplay = False
HAnimJoint784.bboxSize = [-1,-1,-1]
HAnimJoint784.visible = True

HAnimHumanoid14.joints.append(HAnimJoint784)
HAnimJoint785 = x3d.HAnimJoint()
HAnimJoint785.USE = "STD_Joint_r_midcarpal_1"
HAnimJoint785.bboxCenter = [0,0,0]
HAnimJoint785.bboxDisplay = False
HAnimJoint785.bboxSize = [-1,-1,-1]
HAnimJoint785.visible = True

HAnimHumanoid14.joints.append(HAnimJoint785)
HAnimJoint786 = x3d.HAnimJoint()
HAnimJoint786.USE = "STD_Joint_l_midcarpal_2"
HAnimJoint786.bboxCenter = [0,0,0]
HAnimJoint786.bboxDisplay = False
HAnimJoint786.bboxSize = [-1,-1,-1]
HAnimJoint786.visible = True

HAnimHumanoid14.joints.append(HAnimJoint786)
HAnimJoint787 = x3d.HAnimJoint()
HAnimJoint787.USE = "STD_Joint_r_midcarpal_2"
HAnimJoint787.bboxCenter = [0,0,0]
HAnimJoint787.bboxDisplay = False
HAnimJoint787.bboxSize = [-1,-1,-1]
HAnimJoint787.visible = True

HAnimHumanoid14.joints.append(HAnimJoint787)
HAnimJoint788 = x3d.HAnimJoint()
HAnimJoint788.USE = "STD_Joint_l_midcarpal_3"
HAnimJoint788.bboxCenter = [0,0,0]
HAnimJoint788.bboxDisplay = False
HAnimJoint788.bboxSize = [-1,-1,-1]
HAnimJoint788.visible = True

HAnimHumanoid14.joints.append(HAnimJoint788)
HAnimJoint789 = x3d.HAnimJoint()
HAnimJoint789.USE = "STD_Joint_r_midcarpal_3"
HAnimJoint789.bboxCenter = [0,0,0]
HAnimJoint789.bboxDisplay = False
HAnimJoint789.bboxSize = [-1,-1,-1]
HAnimJoint789.visible = True

HAnimHumanoid14.joints.append(HAnimJoint789)
HAnimJoint790 = x3d.HAnimJoint()
HAnimJoint790.USE = "STD_Joint_l_midcarpal_4_5"
HAnimJoint790.bboxCenter = [0,0,0]
HAnimJoint790.bboxDisplay = False
HAnimJoint790.bboxSize = [-1,-1,-1]
HAnimJoint790.visible = True

HAnimHumanoid14.joints.append(HAnimJoint790)
HAnimJoint791 = x3d.HAnimJoint()
HAnimJoint791.USE = "STD_Joint_r_midcarpal_4_5"
HAnimJoint791.bboxCenter = [0,0,0]
HAnimJoint791.bboxDisplay = False
HAnimJoint791.bboxSize = [-1,-1,-1]
HAnimJoint791.visible = True

HAnimHumanoid14.joints.append(HAnimJoint791)
HAnimJoint792 = x3d.HAnimJoint()
HAnimJoint792.USE = "STD_Joint_l_radiocarpal"
HAnimJoint792.bboxCenter = [0,0,0]
HAnimJoint792.bboxDisplay = False
HAnimJoint792.bboxSize = [-1,-1,-1]
HAnimJoint792.visible = True

HAnimHumanoid14.joints.append(HAnimJoint792)
HAnimJoint793 = x3d.HAnimJoint()
HAnimJoint793.USE = "STD_Joint_r_radiocarpal"
HAnimJoint793.bboxCenter = [0,0,0]
HAnimJoint793.bboxDisplay = False
HAnimJoint793.bboxSize = [-1,-1,-1]
HAnimJoint793.visible = True

HAnimHumanoid14.joints.append(HAnimJoint793)
HAnimJoint794 = x3d.HAnimJoint()
HAnimJoint794.USE = "STD_Joint_l_shoulder"
HAnimJoint794.bboxCenter = [0,0,0]
HAnimJoint794.bboxDisplay = False
HAnimJoint794.bboxSize = [-1,-1,-1]
HAnimJoint794.visible = True

HAnimHumanoid14.joints.append(HAnimJoint794)
HAnimJoint795 = x3d.HAnimJoint()
HAnimJoint795.USE = "STD_Joint_r_shoulder"
HAnimJoint795.bboxCenter = [0,0,0]
HAnimJoint795.bboxDisplay = False
HAnimJoint795.bboxSize = [-1,-1,-1]
HAnimJoint795.visible = True

HAnimHumanoid14.joints.append(HAnimJoint795)
HAnimJoint796 = x3d.HAnimJoint()
HAnimJoint796.USE = "STD_Joint_l_sternoclavicular"
HAnimJoint796.bboxCenter = [0,0,0]
HAnimJoint796.bboxDisplay = False
HAnimJoint796.bboxSize = [-1,-1,-1]
HAnimJoint796.visible = True

HAnimHumanoid14.joints.append(HAnimJoint796)
HAnimJoint797 = x3d.HAnimJoint()
HAnimJoint797.USE = "STD_Joint_r_sternoclavicular"
HAnimJoint797.bboxCenter = [0,0,0]
HAnimJoint797.bboxDisplay = False
HAnimJoint797.bboxSize = [-1,-1,-1]
HAnimJoint797.visible = True

HAnimHumanoid14.joints.append(HAnimJoint797)
HAnimJoint798 = x3d.HAnimJoint()
HAnimJoint798.USE = "STD_Joint_l_talocalcaneonavicular"
HAnimJoint798.bboxCenter = [0,0,0]
HAnimJoint798.bboxDisplay = False
HAnimJoint798.bboxSize = [-1,-1,-1]
HAnimJoint798.visible = True

HAnimHumanoid14.joints.append(HAnimJoint798)
HAnimJoint799 = x3d.HAnimJoint()
HAnimJoint799.USE = "STD_Joint_r_talocalcaneonavicular"
HAnimJoint799.bboxCenter = [0,0,0]
HAnimJoint799.bboxDisplay = False
HAnimJoint799.bboxSize = [-1,-1,-1]
HAnimJoint799.visible = True

HAnimHumanoid14.joints.append(HAnimJoint799)
HAnimJoint800 = x3d.HAnimJoint()
HAnimJoint800.USE = "STD_Joint_l_talocrural"
HAnimJoint800.bboxCenter = [0,0,0]
HAnimJoint800.bboxDisplay = False
HAnimJoint800.bboxSize = [-1,-1,-1]
HAnimJoint800.visible = True

HAnimHumanoid14.joints.append(HAnimJoint800)
HAnimJoint801 = x3d.HAnimJoint()
HAnimJoint801.USE = "STD_Joint_r_talocrural"
HAnimJoint801.bboxCenter = [0,0,0]
HAnimJoint801.bboxDisplay = False
HAnimJoint801.bboxSize = [-1,-1,-1]
HAnimJoint801.visible = True

HAnimHumanoid14.joints.append(HAnimJoint801)
HAnimJoint802 = x3d.HAnimJoint()
HAnimJoint802.USE = "STD_Joint_l_tarsal_distal_interphalangeal_2"
HAnimJoint802.bboxCenter = [0,0,0]
HAnimJoint802.bboxDisplay = False
HAnimJoint802.bboxSize = [-1,-1,-1]
HAnimJoint802.visible = True

HAnimHumanoid14.joints.append(HAnimJoint802)
HAnimJoint803 = x3d.HAnimJoint()
HAnimJoint803.USE = "STD_Joint_r_tarsal_distal_interphalangeal_2"
HAnimJoint803.bboxCenter = [0,0,0]
HAnimJoint803.bboxDisplay = False
HAnimJoint803.bboxSize = [-1,-1,-1]
HAnimJoint803.visible = True

HAnimHumanoid14.joints.append(HAnimJoint803)
HAnimJoint804 = x3d.HAnimJoint()
HAnimJoint804.USE = "STD_Joint_l_tarsal_distal_interphalangeal_3"
HAnimJoint804.bboxCenter = [0,0,0]
HAnimJoint804.bboxDisplay = False
HAnimJoint804.bboxSize = [-1,-1,-1]
HAnimJoint804.visible = True

HAnimHumanoid14.joints.append(HAnimJoint804)
HAnimJoint805 = x3d.HAnimJoint()
HAnimJoint805.USE = "STD_Joint_r_tarsal_distal_interphalangeal_3"
HAnimJoint805.bboxCenter = [0,0,0]
HAnimJoint805.bboxDisplay = False
HAnimJoint805.bboxSize = [-1,-1,-1]
HAnimJoint805.visible = True

HAnimHumanoid14.joints.append(HAnimJoint805)
HAnimJoint806 = x3d.HAnimJoint()
HAnimJoint806.USE = "STD_Joint_l_tarsal_distal_interphalangeal_4"
HAnimJoint806.bboxCenter = [0,0,0]
HAnimJoint806.bboxDisplay = False
HAnimJoint806.bboxSize = [-1,-1,-1]
HAnimJoint806.visible = True

HAnimHumanoid14.joints.append(HAnimJoint806)
HAnimJoint807 = x3d.HAnimJoint()
HAnimJoint807.USE = "STD_Joint_r_tarsal_distal_interphalangeal_4"
HAnimJoint807.bboxCenter = [0,0,0]
HAnimJoint807.bboxDisplay = False
HAnimJoint807.bboxSize = [-1,-1,-1]
HAnimJoint807.visible = True

HAnimHumanoid14.joints.append(HAnimJoint807)
HAnimJoint808 = x3d.HAnimJoint()
HAnimJoint808.USE = "STD_Joint_l_tarsal_distal_interphalangeal_5"
HAnimJoint808.bboxCenter = [0,0,0]
HAnimJoint808.bboxDisplay = False
HAnimJoint808.bboxSize = [-1,-1,-1]
HAnimJoint808.visible = True

HAnimHumanoid14.joints.append(HAnimJoint808)
HAnimJoint809 = x3d.HAnimJoint()
HAnimJoint809.USE = "STD_Joint_r_tarsal_distal_interphalangeal_5"
HAnimJoint809.bboxCenter = [0,0,0]
HAnimJoint809.bboxDisplay = False
HAnimJoint809.bboxSize = [-1,-1,-1]
HAnimJoint809.visible = True

HAnimHumanoid14.joints.append(HAnimJoint809)
HAnimJoint810 = x3d.HAnimJoint()
HAnimJoint810.USE = "STD_Joint_l_tarsal_interphalangeal_1"
HAnimJoint810.bboxCenter = [0,0,0]
HAnimJoint810.bboxDisplay = False
HAnimJoint810.bboxSize = [-1,-1,-1]
HAnimJoint810.visible = True

HAnimHumanoid14.joints.append(HAnimJoint810)
HAnimJoint811 = x3d.HAnimJoint()
HAnimJoint811.USE = "STD_Joint_r_tarsal_interphalangeal_1"
HAnimJoint811.bboxCenter = [0,0,0]
HAnimJoint811.bboxDisplay = False
HAnimJoint811.bboxSize = [-1,-1,-1]
HAnimJoint811.visible = True

HAnimHumanoid14.joints.append(HAnimJoint811)
HAnimJoint812 = x3d.HAnimJoint()
HAnimJoint812.USE = "STD_Joint_l_tarsal_proximal_interphalangeal_2"
HAnimJoint812.bboxCenter = [0,0,0]
HAnimJoint812.bboxDisplay = False
HAnimJoint812.bboxSize = [-1,-1,-1]
HAnimJoint812.visible = True

HAnimHumanoid14.joints.append(HAnimJoint812)
HAnimJoint813 = x3d.HAnimJoint()
HAnimJoint813.USE = "STD_Joint_r_tarsal_proximal_interphalangeal_2"
HAnimJoint813.bboxCenter = [0,0,0]
HAnimJoint813.bboxDisplay = False
HAnimJoint813.bboxSize = [-1,-1,-1]
HAnimJoint813.visible = True

HAnimHumanoid14.joints.append(HAnimJoint813)
HAnimJoint814 = x3d.HAnimJoint()
HAnimJoint814.USE = "STD_Joint_l_tarsal_proximal_interphalangeal_3"
HAnimJoint814.bboxCenter = [0,0,0]
HAnimJoint814.bboxDisplay = False
HAnimJoint814.bboxSize = [-1,-1,-1]
HAnimJoint814.visible = True

HAnimHumanoid14.joints.append(HAnimJoint814)
HAnimJoint815 = x3d.HAnimJoint()
HAnimJoint815.USE = "STD_Joint_r_tarsal_proximal_interphalangeal_3"
HAnimJoint815.bboxCenter = [0,0,0]
HAnimJoint815.bboxDisplay = False
HAnimJoint815.bboxSize = [-1,-1,-1]
HAnimJoint815.visible = True

HAnimHumanoid14.joints.append(HAnimJoint815)
HAnimJoint816 = x3d.HAnimJoint()
HAnimJoint816.USE = "STD_Joint_l_tarsal_proximal_interphalangeal_4"
HAnimJoint816.bboxCenter = [0,0,0]
HAnimJoint816.bboxDisplay = False
HAnimJoint816.bboxSize = [-1,-1,-1]
HAnimJoint816.visible = True

HAnimHumanoid14.joints.append(HAnimJoint816)
HAnimJoint817 = x3d.HAnimJoint()
HAnimJoint817.USE = "STD_Joint_r_tarsal_proximal_interphalangeal_4"
HAnimJoint817.bboxCenter = [0,0,0]
HAnimJoint817.bboxDisplay = False
HAnimJoint817.bboxSize = [-1,-1,-1]
HAnimJoint817.visible = True

HAnimHumanoid14.joints.append(HAnimJoint817)
HAnimJoint818 = x3d.HAnimJoint()
HAnimJoint818.USE = "STD_Joint_l_tarsal_proximal_interphalangeal_5"
HAnimJoint818.bboxCenter = [0,0,0]
HAnimJoint818.bboxDisplay = False
HAnimJoint818.bboxSize = [-1,-1,-1]
HAnimJoint818.visible = True

HAnimHumanoid14.joints.append(HAnimJoint818)
HAnimJoint819 = x3d.HAnimJoint()
HAnimJoint819.USE = "STD_Joint_r_tarsal_proximal_interphalangeal_5"
HAnimJoint819.bboxCenter = [0,0,0]
HAnimJoint819.bboxDisplay = False
HAnimJoint819.bboxSize = [-1,-1,-1]
HAnimJoint819.visible = True

HAnimHumanoid14.joints.append(HAnimJoint819)
HAnimJoint820 = x3d.HAnimJoint()
HAnimJoint820.USE = "STD_Joint_l_tarsometatarsal_1"
HAnimJoint820.bboxCenter = [0,0,0]
HAnimJoint820.bboxDisplay = False
HAnimJoint820.bboxSize = [-1,-1,-1]
HAnimJoint820.visible = True

HAnimHumanoid14.joints.append(HAnimJoint820)
HAnimJoint821 = x3d.HAnimJoint()
HAnimJoint821.USE = "STD_Joint_r_tarsometatarsal_1"
HAnimJoint821.bboxCenter = [0,0,0]
HAnimJoint821.bboxDisplay = False
HAnimJoint821.bboxSize = [-1,-1,-1]
HAnimJoint821.visible = True

HAnimHumanoid14.joints.append(HAnimJoint821)
HAnimJoint822 = x3d.HAnimJoint()
HAnimJoint822.USE = "STD_Joint_l_tarsometatarsal_2"
HAnimJoint822.bboxCenter = [0,0,0]
HAnimJoint822.bboxDisplay = False
HAnimJoint822.bboxSize = [-1,-1,-1]
HAnimJoint822.visible = True

HAnimHumanoid14.joints.append(HAnimJoint822)
HAnimJoint823 = x3d.HAnimJoint()
HAnimJoint823.USE = "STD_Joint_r_tarsometatarsal_2"
HAnimJoint823.bboxCenter = [0,0,0]
HAnimJoint823.bboxDisplay = False
HAnimJoint823.bboxSize = [-1,-1,-1]
HAnimJoint823.visible = True

HAnimHumanoid14.joints.append(HAnimJoint823)
HAnimJoint824 = x3d.HAnimJoint()
HAnimJoint824.USE = "STD_Joint_l_tarsometatarsal_3"
HAnimJoint824.bboxCenter = [0,0,0]
HAnimJoint824.bboxDisplay = False
HAnimJoint824.bboxSize = [-1,-1,-1]
HAnimJoint824.visible = True

HAnimHumanoid14.joints.append(HAnimJoint824)
HAnimJoint825 = x3d.HAnimJoint()
HAnimJoint825.USE = "STD_Joint_r_tarsometatarsal_3"
HAnimJoint825.bboxCenter = [0,0,0]
HAnimJoint825.bboxDisplay = False
HAnimJoint825.bboxSize = [-1,-1,-1]
HAnimJoint825.visible = True

HAnimHumanoid14.joints.append(HAnimJoint825)
HAnimJoint826 = x3d.HAnimJoint()
HAnimJoint826.USE = "STD_Joint_l_tarsometatarsal_4"
HAnimJoint826.bboxCenter = [0,0,0]
HAnimJoint826.bboxDisplay = False
HAnimJoint826.bboxSize = [-1,-1,-1]
HAnimJoint826.visible = True

HAnimHumanoid14.joints.append(HAnimJoint826)
HAnimJoint827 = x3d.HAnimJoint()
HAnimJoint827.USE = "STD_Joint_r_tarsometatarsal_4"
HAnimJoint827.bboxCenter = [0,0,0]
HAnimJoint827.bboxDisplay = False
HAnimJoint827.bboxSize = [-1,-1,-1]
HAnimJoint827.visible = True

HAnimHumanoid14.joints.append(HAnimJoint827)
HAnimJoint828 = x3d.HAnimJoint()
HAnimJoint828.USE = "STD_Joint_l_tarsometatarsal_5"
HAnimJoint828.bboxCenter = [0,0,0]
HAnimJoint828.bboxDisplay = False
HAnimJoint828.bboxSize = [-1,-1,-1]
HAnimJoint828.visible = True

HAnimHumanoid14.joints.append(HAnimJoint828)
HAnimJoint829 = x3d.HAnimJoint()
HAnimJoint829.USE = "STD_Joint_r_tarsometatarsal_5"
HAnimJoint829.bboxCenter = [0,0,0]
HAnimJoint829.bboxDisplay = False
HAnimJoint829.bboxSize = [-1,-1,-1]
HAnimJoint829.visible = True

HAnimHumanoid14.joints.append(HAnimJoint829)
HAnimJoint830 = x3d.HAnimJoint()
HAnimJoint830.USE = "STD_Joint_l_transversetarsal"
HAnimJoint830.bboxCenter = [0,0,0]
HAnimJoint830.bboxDisplay = False
HAnimJoint830.bboxSize = [-1,-1,-1]
HAnimJoint830.visible = True

HAnimHumanoid14.joints.append(HAnimJoint830)
HAnimJoint831 = x3d.HAnimJoint()
HAnimJoint831.USE = "STD_Joint_r_transversetarsal"
HAnimJoint831.bboxCenter = [0,0,0]
HAnimJoint831.bboxDisplay = False
HAnimJoint831.bboxSize = [-1,-1,-1]
HAnimJoint831.visible = True

HAnimHumanoid14.joints.append(HAnimJoint831)
HAnimSegment832 = x3d.HAnimSegment()
HAnimSegment832.USE = "STD_Segment_sacrum"
HAnimSegment832.bboxDisplay = False
HAnimSegment832.visible = True

HAnimHumanoid14.segments.append(HAnimSegment832)
HAnimSegment833 = x3d.HAnimSegment()
HAnimSegment833.USE = "STD_Segment_pelvis"
HAnimSegment833.bboxDisplay = False
HAnimSegment833.visible = True

HAnimHumanoid14.segments.append(HAnimSegment833)
HAnimSegment834 = x3d.HAnimSegment()
HAnimSegment834.USE = "STD_Segment_l5"
HAnimSegment834.bboxDisplay = False
HAnimSegment834.visible = True

HAnimHumanoid14.segments.append(HAnimSegment834)
HAnimSegment835 = x3d.HAnimSegment()
HAnimSegment835.USE = "STD_Segment_l4"
HAnimSegment835.bboxDisplay = False
HAnimSegment835.visible = True

HAnimHumanoid14.segments.append(HAnimSegment835)
HAnimSegment836 = x3d.HAnimSegment()
HAnimSegment836.USE = "STD_Segment_l3"
HAnimSegment836.bboxDisplay = False
HAnimSegment836.visible = True

HAnimHumanoid14.segments.append(HAnimSegment836)
HAnimSegment837 = x3d.HAnimSegment()
HAnimSegment837.USE = "STD_Segment_l2"
HAnimSegment837.bboxDisplay = False
HAnimSegment837.visible = True

HAnimHumanoid14.segments.append(HAnimSegment837)
HAnimSegment838 = x3d.HAnimSegment()
HAnimSegment838.USE = "STD_Segment_l1"
HAnimSegment838.bboxDisplay = False
HAnimSegment838.visible = True

HAnimHumanoid14.segments.append(HAnimSegment838)
HAnimSegment839 = x3d.HAnimSegment()
HAnimSegment839.USE = "STD_Segment_t12"
HAnimSegment839.bboxDisplay = False
HAnimSegment839.visible = True

HAnimHumanoid14.segments.append(HAnimSegment839)
HAnimSegment840 = x3d.HAnimSegment()
HAnimSegment840.USE = "STD_Segment_t11"
HAnimSegment840.bboxDisplay = False
HAnimSegment840.visible = True

HAnimHumanoid14.segments.append(HAnimSegment840)
HAnimSegment841 = x3d.HAnimSegment()
HAnimSegment841.USE = "STD_Segment_t10"
HAnimSegment841.bboxDisplay = False
HAnimSegment841.visible = True

HAnimHumanoid14.segments.append(HAnimSegment841)
HAnimSegment842 = x3d.HAnimSegment()
HAnimSegment842.USE = "STD_Segment_t9"
HAnimSegment842.bboxDisplay = False
HAnimSegment842.visible = True

HAnimHumanoid14.segments.append(HAnimSegment842)
HAnimSegment843 = x3d.HAnimSegment()
HAnimSegment843.USE = "STD_Segment_t8"
HAnimSegment843.bboxDisplay = False
HAnimSegment843.visible = True

HAnimHumanoid14.segments.append(HAnimSegment843)
HAnimSegment844 = x3d.HAnimSegment()
HAnimSegment844.USE = "STD_Segment_t7"
HAnimSegment844.bboxDisplay = False
HAnimSegment844.visible = True

HAnimHumanoid14.segments.append(HAnimSegment844)
HAnimSegment845 = x3d.HAnimSegment()
HAnimSegment845.USE = "STD_Segment_t6"
HAnimSegment845.bboxDisplay = False
HAnimSegment845.visible = True

HAnimHumanoid14.segments.append(HAnimSegment845)
HAnimSegment846 = x3d.HAnimSegment()
HAnimSegment846.USE = "STD_Segment_t5"
HAnimSegment846.bboxDisplay = False
HAnimSegment846.visible = True

HAnimHumanoid14.segments.append(HAnimSegment846)
HAnimSegment847 = x3d.HAnimSegment()
HAnimSegment847.USE = "STD_Segment_t4"
HAnimSegment847.bboxDisplay = False
HAnimSegment847.visible = True

HAnimHumanoid14.segments.append(HAnimSegment847)
HAnimSegment848 = x3d.HAnimSegment()
HAnimSegment848.USE = "STD_Segment_t3"
HAnimSegment848.bboxDisplay = False
HAnimSegment848.visible = True

HAnimHumanoid14.segments.append(HAnimSegment848)
HAnimSegment849 = x3d.HAnimSegment()
HAnimSegment849.USE = "STD_Segment_t2"
HAnimSegment849.bboxDisplay = False
HAnimSegment849.visible = True

HAnimHumanoid14.segments.append(HAnimSegment849)
HAnimSegment850 = x3d.HAnimSegment()
HAnimSegment850.USE = "STD_Segment_t1"
HAnimSegment850.bboxDisplay = False
HAnimSegment850.visible = True

HAnimHumanoid14.segments.append(HAnimSegment850)
HAnimSegment851 = x3d.HAnimSegment()
HAnimSegment851.USE = "STD_Segment_c7"
HAnimSegment851.bboxDisplay = False
HAnimSegment851.visible = True

HAnimHumanoid14.segments.append(HAnimSegment851)
HAnimSegment852 = x3d.HAnimSegment()
HAnimSegment852.USE = "STD_Segment_c6"
HAnimSegment852.bboxDisplay = False
HAnimSegment852.visible = True

HAnimHumanoid14.segments.append(HAnimSegment852)
HAnimSegment853 = x3d.HAnimSegment()
HAnimSegment853.USE = "STD_Segment_c5"
HAnimSegment853.bboxDisplay = False
HAnimSegment853.visible = True

HAnimHumanoid14.segments.append(HAnimSegment853)
HAnimSegment854 = x3d.HAnimSegment()
HAnimSegment854.USE = "STD_Segment_c4"
HAnimSegment854.bboxDisplay = False
HAnimSegment854.visible = True

HAnimHumanoid14.segments.append(HAnimSegment854)
HAnimSegment855 = x3d.HAnimSegment()
HAnimSegment855.USE = "STD_Segment_c3"
HAnimSegment855.bboxDisplay = False
HAnimSegment855.visible = True

HAnimHumanoid14.segments.append(HAnimSegment855)
HAnimSegment856 = x3d.HAnimSegment()
HAnimSegment856.USE = "STD_Segment_c2"
HAnimSegment856.bboxDisplay = False
HAnimSegment856.visible = True

HAnimHumanoid14.segments.append(HAnimSegment856)
HAnimSegment857 = x3d.HAnimSegment()
HAnimSegment857.USE = "STD_Segment_c1"
HAnimSegment857.bboxDisplay = False
HAnimSegment857.visible = True

HAnimHumanoid14.segments.append(HAnimSegment857)
HAnimSegment858 = x3d.HAnimSegment()
HAnimSegment858.USE = "STD_Segment_skull"
HAnimSegment858.bboxDisplay = False
HAnimSegment858.visible = True

HAnimHumanoid14.segments.append(HAnimSegment858)
HAnimSegment859 = x3d.HAnimSegment()
HAnimSegment859.USE = "STD_Segment_jaw"
HAnimSegment859.bboxDisplay = False
HAnimSegment859.visible = True

HAnimHumanoid14.segments.append(HAnimSegment859)
HAnimSegment860 = x3d.HAnimSegment()
HAnimSegment860.USE = "STD_Segment_l_calcaneus"
HAnimSegment860.bboxDisplay = False
HAnimSegment860.visible = True

HAnimHumanoid14.segments.append(HAnimSegment860)
HAnimSegment861 = x3d.HAnimSegment()
HAnimSegment861.USE = "STD_Segment_r_calcaneus"
HAnimSegment861.bboxDisplay = False
HAnimSegment861.visible = True

HAnimHumanoid14.segments.append(HAnimSegment861)
HAnimSegment862 = x3d.HAnimSegment()
HAnimSegment862.USE = "STD_Segment_l_calf"
HAnimSegment862.bboxDisplay = False
HAnimSegment862.visible = True

HAnimHumanoid14.segments.append(HAnimSegment862)
HAnimSegment863 = x3d.HAnimSegment()
HAnimSegment863.USE = "STD_Segment_r_calf"
HAnimSegment863.bboxDisplay = False
HAnimSegment863.visible = True

HAnimHumanoid14.segments.append(HAnimSegment863)
HAnimSegment864 = x3d.HAnimSegment()
HAnimSegment864.USE = "STD_Segment_l_capitate"
HAnimSegment864.bboxDisplay = False
HAnimSegment864.visible = True

HAnimHumanoid14.segments.append(HAnimSegment864)
HAnimSegment865 = x3d.HAnimSegment()
HAnimSegment865.USE = "STD_Segment_r_capitate"
HAnimSegment865.bboxDisplay = False
HAnimSegment865.visible = True

HAnimHumanoid14.segments.append(HAnimSegment865)
HAnimSegment866 = x3d.HAnimSegment()
HAnimSegment866.USE = "STD_Segment_l_carpal"
HAnimSegment866.bboxDisplay = False
HAnimSegment866.visible = True

HAnimHumanoid14.segments.append(HAnimSegment866)
HAnimSegment867 = x3d.HAnimSegment()
HAnimSegment867.USE = "STD_Segment_r_carpal"
HAnimSegment867.bboxDisplay = False
HAnimSegment867.visible = True

HAnimHumanoid14.segments.append(HAnimSegment867)
HAnimSegment868 = x3d.HAnimSegment()
HAnimSegment868.USE = "STD_Segment_l_carpal_distal_phalanx_1"
HAnimSegment868.bboxDisplay = False
HAnimSegment868.visible = True

HAnimHumanoid14.segments.append(HAnimSegment868)
HAnimSegment869 = x3d.HAnimSegment()
HAnimSegment869.USE = "STD_Segment_r_carpal_distal_phalanx_1"
HAnimSegment869.bboxDisplay = False
HAnimSegment869.visible = True

HAnimHumanoid14.segments.append(HAnimSegment869)
HAnimSegment870 = x3d.HAnimSegment()
HAnimSegment870.USE = "STD_Segment_l_carpal_distal_phalanx_2"
HAnimSegment870.bboxDisplay = False
HAnimSegment870.visible = True

HAnimHumanoid14.segments.append(HAnimSegment870)
HAnimSegment871 = x3d.HAnimSegment()
HAnimSegment871.USE = "STD_Segment_r_carpal_distal_phalanx_2"
HAnimSegment871.bboxDisplay = False
HAnimSegment871.visible = True

HAnimHumanoid14.segments.append(HAnimSegment871)
HAnimSegment872 = x3d.HAnimSegment()
HAnimSegment872.USE = "STD_Segment_l_carpal_distal_phalanx_3"
HAnimSegment872.bboxDisplay = False
HAnimSegment872.visible = True

HAnimHumanoid14.segments.append(HAnimSegment872)
HAnimSegment873 = x3d.HAnimSegment()
HAnimSegment873.USE = "STD_Segment_r_carpal_distal_phalanx_3"
HAnimSegment873.bboxDisplay = False
HAnimSegment873.visible = True

HAnimHumanoid14.segments.append(HAnimSegment873)
HAnimSegment874 = x3d.HAnimSegment()
HAnimSegment874.USE = "STD_Segment_l_carpal_distal_phalanx_4"
HAnimSegment874.bboxDisplay = False
HAnimSegment874.visible = True

HAnimHumanoid14.segments.append(HAnimSegment874)
HAnimSegment875 = x3d.HAnimSegment()
HAnimSegment875.USE = "STD_Segment_r_carpal_distal_phalanx_4"
HAnimSegment875.bboxDisplay = False
HAnimSegment875.visible = True

HAnimHumanoid14.segments.append(HAnimSegment875)
HAnimSegment876 = x3d.HAnimSegment()
HAnimSegment876.USE = "STD_Segment_l_carpal_distal_phalanx_5"
HAnimSegment876.bboxDisplay = False
HAnimSegment876.visible = True

HAnimHumanoid14.segments.append(HAnimSegment876)
HAnimSegment877 = x3d.HAnimSegment()
HAnimSegment877.USE = "STD_Segment_r_carpal_distal_phalanx_5"
HAnimSegment877.bboxDisplay = False
HAnimSegment877.visible = True

HAnimHumanoid14.segments.append(HAnimSegment877)
HAnimSegment878 = x3d.HAnimSegment()
HAnimSegment878.USE = "STD_Segment_l_carpal_middle_phalanx_2"
HAnimSegment878.bboxDisplay = False
HAnimSegment878.visible = True

HAnimHumanoid14.segments.append(HAnimSegment878)
HAnimSegment879 = x3d.HAnimSegment()
HAnimSegment879.USE = "STD_Segment_r_carpal_middle_phalanx_2"
HAnimSegment879.bboxDisplay = False
HAnimSegment879.visible = True

HAnimHumanoid14.segments.append(HAnimSegment879)
HAnimSegment880 = x3d.HAnimSegment()
HAnimSegment880.USE = "STD_Segment_l_carpal_middle_phalanx_3"
HAnimSegment880.bboxDisplay = False
HAnimSegment880.visible = True

HAnimHumanoid14.segments.append(HAnimSegment880)
HAnimSegment881 = x3d.HAnimSegment()
HAnimSegment881.USE = "STD_Segment_r_carpal_middle_phalanx_3"
HAnimSegment881.bboxDisplay = False
HAnimSegment881.visible = True

HAnimHumanoid14.segments.append(HAnimSegment881)
HAnimSegment882 = x3d.HAnimSegment()
HAnimSegment882.USE = "STD_Segment_l_carpal_middle_phalanx_4"
HAnimSegment882.bboxDisplay = False
HAnimSegment882.visible = True

HAnimHumanoid14.segments.append(HAnimSegment882)
HAnimSegment883 = x3d.HAnimSegment()
HAnimSegment883.USE = "STD_Segment_r_carpal_middle_phalanx_4"
HAnimSegment883.bboxDisplay = False
HAnimSegment883.visible = True

HAnimHumanoid14.segments.append(HAnimSegment883)
HAnimSegment884 = x3d.HAnimSegment()
HAnimSegment884.USE = "STD_Segment_l_carpal_middle_phalanx_5"
HAnimSegment884.bboxDisplay = False
HAnimSegment884.visible = True

HAnimHumanoid14.segments.append(HAnimSegment884)
HAnimSegment885 = x3d.HAnimSegment()
HAnimSegment885.USE = "STD_Segment_r_carpal_middle_phalanx_5"
HAnimSegment885.bboxDisplay = False
HAnimSegment885.visible = True

HAnimHumanoid14.segments.append(HAnimSegment885)
HAnimSegment886 = x3d.HAnimSegment()
HAnimSegment886.USE = "STD_Segment_l_carpal_proximal_phalanx_1"
HAnimSegment886.bboxDisplay = False
HAnimSegment886.visible = True

HAnimHumanoid14.segments.append(HAnimSegment886)
HAnimSegment887 = x3d.HAnimSegment()
HAnimSegment887.USE = "STD_Segment_r_carpal_proximal_phalanx_1"
HAnimSegment887.bboxDisplay = False
HAnimSegment887.visible = True

HAnimHumanoid14.segments.append(HAnimSegment887)
HAnimSegment888 = x3d.HAnimSegment()
HAnimSegment888.USE = "STD_Segment_l_carpal_proximal_phalanx_2"
HAnimSegment888.bboxDisplay = False
HAnimSegment888.visible = True

HAnimHumanoid14.segments.append(HAnimSegment888)
HAnimSegment889 = x3d.HAnimSegment()
HAnimSegment889.USE = "STD_Segment_r_carpal_proximal_phalanx_2"
HAnimSegment889.bboxDisplay = False
HAnimSegment889.visible = True

HAnimHumanoid14.segments.append(HAnimSegment889)
HAnimSegment890 = x3d.HAnimSegment()
HAnimSegment890.USE = "STD_Segment_l_carpal_proximal_phalanx_3"
HAnimSegment890.bboxDisplay = False
HAnimSegment890.visible = True

HAnimHumanoid14.segments.append(HAnimSegment890)
HAnimSegment891 = x3d.HAnimSegment()
HAnimSegment891.USE = "STD_Segment_r_carpal_proximal_phalanx_3"
HAnimSegment891.bboxDisplay = False
HAnimSegment891.visible = True

HAnimHumanoid14.segments.append(HAnimSegment891)
HAnimSegment892 = x3d.HAnimSegment()
HAnimSegment892.USE = "STD_Segment_l_carpal_proximal_phalanx_4"
HAnimSegment892.bboxDisplay = False
HAnimSegment892.visible = True

HAnimHumanoid14.segments.append(HAnimSegment892)
HAnimSegment893 = x3d.HAnimSegment()
HAnimSegment893.USE = "STD_Segment_r_carpal_proximal_phalanx_4"
HAnimSegment893.bboxDisplay = False
HAnimSegment893.visible = True

HAnimHumanoid14.segments.append(HAnimSegment893)
HAnimSegment894 = x3d.HAnimSegment()
HAnimSegment894.USE = "STD_Segment_l_carpal_proximal_phalanx_5"
HAnimSegment894.bboxDisplay = False
HAnimSegment894.visible = True

HAnimHumanoid14.segments.append(HAnimSegment894)
HAnimSegment895 = x3d.HAnimSegment()
HAnimSegment895.USE = "STD_Segment_r_carpal_proximal_phalanx_5"
HAnimSegment895.bboxDisplay = False
HAnimSegment895.visible = True

HAnimHumanoid14.segments.append(HAnimSegment895)
HAnimSegment896 = x3d.HAnimSegment()
HAnimSegment896.USE = "STD_Segment_l_clavicle"
HAnimSegment896.bboxDisplay = False
HAnimSegment896.visible = True

HAnimHumanoid14.segments.append(HAnimSegment896)
HAnimSegment897 = x3d.HAnimSegment()
HAnimSegment897.USE = "STD_Segment_r_clavicle"
HAnimSegment897.bboxDisplay = False
HAnimSegment897.visible = True

HAnimHumanoid14.segments.append(HAnimSegment897)
HAnimSegment898 = x3d.HAnimSegment()
HAnimSegment898.USE = "STD_Segment_l_cuboid"
HAnimSegment898.bboxDisplay = False
HAnimSegment898.visible = True

HAnimHumanoid14.segments.append(HAnimSegment898)
HAnimSegment899 = x3d.HAnimSegment()
HAnimSegment899.USE = "STD_Segment_r_cuboid"
HAnimSegment899.bboxDisplay = False
HAnimSegment899.visible = True

HAnimHumanoid14.segments.append(HAnimSegment899)
HAnimSegment900 = x3d.HAnimSegment()
HAnimSegment900.USE = "STD_Segment_l_cuneiform_1"
HAnimSegment900.bboxDisplay = False
HAnimSegment900.visible = True

HAnimHumanoid14.segments.append(HAnimSegment900)
HAnimSegment901 = x3d.HAnimSegment()
HAnimSegment901.USE = "STD_Segment_r_cuneiform_1"
HAnimSegment901.bboxDisplay = False
HAnimSegment901.visible = True

HAnimHumanoid14.segments.append(HAnimSegment901)
HAnimSegment902 = x3d.HAnimSegment()
HAnimSegment902.USE = "STD_Segment_l_cuneiform_2"
HAnimSegment902.bboxDisplay = False
HAnimSegment902.visible = True

HAnimHumanoid14.segments.append(HAnimSegment902)
HAnimSegment903 = x3d.HAnimSegment()
HAnimSegment903.USE = "STD_Segment_r_cuneiform_2"
HAnimSegment903.bboxDisplay = False
HAnimSegment903.visible = True

HAnimHumanoid14.segments.append(HAnimSegment903)
HAnimSegment904 = x3d.HAnimSegment()
HAnimSegment904.USE = "STD_Segment_l_cuneiform_3"
HAnimSegment904.bboxDisplay = False
HAnimSegment904.visible = True

HAnimHumanoid14.segments.append(HAnimSegment904)
HAnimSegment905 = x3d.HAnimSegment()
HAnimSegment905.USE = "STD_Segment_r_cuneiform_3"
HAnimSegment905.bboxDisplay = False
HAnimSegment905.visible = True

HAnimHumanoid14.segments.append(HAnimSegment905)
HAnimSegment906 = x3d.HAnimSegment()
HAnimSegment906.USE = "STD_Segment_l_eyeball"
HAnimSegment906.bboxDisplay = False
HAnimSegment906.visible = True

HAnimHumanoid14.segments.append(HAnimSegment906)
HAnimSegment907 = x3d.HAnimSegment()
HAnimSegment907.USE = "STD_Segment_r_eyeball"
HAnimSegment907.bboxDisplay = False
HAnimSegment907.visible = True

HAnimHumanoid14.segments.append(HAnimSegment907)
HAnimSegment908 = x3d.HAnimSegment()
HAnimSegment908.USE = "STD_Segment_l_eyebrow"
HAnimSegment908.bboxDisplay = False
HAnimSegment908.visible = True

HAnimHumanoid14.segments.append(HAnimSegment908)
HAnimSegment909 = x3d.HAnimSegment()
HAnimSegment909.USE = "STD_Segment_r_eyebrow"
HAnimSegment909.bboxDisplay = False
HAnimSegment909.visible = True

HAnimHumanoid14.segments.append(HAnimSegment909)
HAnimSegment910 = x3d.HAnimSegment()
HAnimSegment910.USE = "STD_Segment_l_eyelid"
HAnimSegment910.bboxDisplay = False
HAnimSegment910.visible = True

HAnimHumanoid14.segments.append(HAnimSegment910)
HAnimSegment911 = x3d.HAnimSegment()
HAnimSegment911.USE = "STD_Segment_r_eyelid"
HAnimSegment911.bboxDisplay = False
HAnimSegment911.visible = True

HAnimHumanoid14.segments.append(HAnimSegment911)
HAnimSegment912 = x3d.HAnimSegment()
HAnimSegment912.USE = "STD_Segment_l_forearm"
HAnimSegment912.bboxDisplay = False
HAnimSegment912.visible = True

HAnimHumanoid14.segments.append(HAnimSegment912)
HAnimSegment913 = x3d.HAnimSegment()
HAnimSegment913.USE = "STD_Segment_r_forearm"
HAnimSegment913.bboxDisplay = False
HAnimSegment913.visible = True

HAnimHumanoid14.segments.append(HAnimSegment913)
HAnimSegment914 = x3d.HAnimSegment()
HAnimSegment914.USE = "STD_Segment_l_hamate"
HAnimSegment914.bboxDisplay = False
HAnimSegment914.visible = True

HAnimHumanoid14.segments.append(HAnimSegment914)
HAnimSegment915 = x3d.HAnimSegment()
HAnimSegment915.USE = "STD_Segment_r_hamate"
HAnimSegment915.bboxDisplay = False
HAnimSegment915.visible = True

HAnimHumanoid14.segments.append(HAnimSegment915)
HAnimSegment916 = x3d.HAnimSegment()
HAnimSegment916.USE = "STD_Segment_l_metacarpal_1"
HAnimSegment916.bboxDisplay = False
HAnimSegment916.visible = True

HAnimHumanoid14.segments.append(HAnimSegment916)
HAnimSegment917 = x3d.HAnimSegment()
HAnimSegment917.USE = "STD_Segment_r_metacarpal_1"
HAnimSegment917.bboxDisplay = False
HAnimSegment917.visible = True

HAnimHumanoid14.segments.append(HAnimSegment917)
HAnimSegment918 = x3d.HAnimSegment()
HAnimSegment918.USE = "STD_Segment_l_metacarpal_2"
HAnimSegment918.bboxDisplay = False
HAnimSegment918.visible = True

HAnimHumanoid14.segments.append(HAnimSegment918)
HAnimSegment919 = x3d.HAnimSegment()
HAnimSegment919.USE = "STD_Segment_r_metacarpal_2"
HAnimSegment919.bboxDisplay = False
HAnimSegment919.visible = True

HAnimHumanoid14.segments.append(HAnimSegment919)
HAnimSegment920 = x3d.HAnimSegment()
HAnimSegment920.USE = "STD_Segment_l_metacarpal_3"
HAnimSegment920.bboxDisplay = False
HAnimSegment920.visible = True

HAnimHumanoid14.segments.append(HAnimSegment920)
HAnimSegment921 = x3d.HAnimSegment()
HAnimSegment921.USE = "STD_Segment_r_metacarpal_3"
HAnimSegment921.bboxDisplay = False
HAnimSegment921.visible = True

HAnimHumanoid14.segments.append(HAnimSegment921)
HAnimSegment922 = x3d.HAnimSegment()
HAnimSegment922.USE = "STD_Segment_l_metacarpal_4"
HAnimSegment922.bboxDisplay = False
HAnimSegment922.visible = True

HAnimHumanoid14.segments.append(HAnimSegment922)
HAnimSegment923 = x3d.HAnimSegment()
HAnimSegment923.USE = "STD_Segment_r_metacarpal_4"
HAnimSegment923.bboxDisplay = False
HAnimSegment923.visible = True

HAnimHumanoid14.segments.append(HAnimSegment923)
HAnimSegment924 = x3d.HAnimSegment()
HAnimSegment924.USE = "STD_Segment_l_metacarpal_5"
HAnimSegment924.bboxDisplay = False
HAnimSegment924.visible = True

HAnimHumanoid14.segments.append(HAnimSegment924)
HAnimSegment925 = x3d.HAnimSegment()
HAnimSegment925.USE = "STD_Segment_r_metacarpal_5"
HAnimSegment925.bboxDisplay = False
HAnimSegment925.visible = True

HAnimHumanoid14.segments.append(HAnimSegment925)
HAnimSegment926 = x3d.HAnimSegment()
HAnimSegment926.USE = "STD_Segment_l_metatarsal_1"
HAnimSegment926.bboxDisplay = False
HAnimSegment926.visible = True

HAnimHumanoid14.segments.append(HAnimSegment926)
HAnimSegment927 = x3d.HAnimSegment()
HAnimSegment927.USE = "STD_Segment_r_metatarsal_1"
HAnimSegment927.bboxDisplay = False
HAnimSegment927.visible = True

HAnimHumanoid14.segments.append(HAnimSegment927)
HAnimSegment928 = x3d.HAnimSegment()
HAnimSegment928.USE = "STD_Segment_l_metatarsal_2"
HAnimSegment928.bboxDisplay = False
HAnimSegment928.visible = True

HAnimHumanoid14.segments.append(HAnimSegment928)
HAnimSegment929 = x3d.HAnimSegment()
HAnimSegment929.USE = "STD_Segment_r_metatarsal_2"
HAnimSegment929.bboxDisplay = False
HAnimSegment929.visible = True

HAnimHumanoid14.segments.append(HAnimSegment929)
HAnimSegment930 = x3d.HAnimSegment()
HAnimSegment930.USE = "STD_Segment_l_metatarsal_3"
HAnimSegment930.bboxDisplay = False
HAnimSegment930.visible = True

HAnimHumanoid14.segments.append(HAnimSegment930)
HAnimSegment931 = x3d.HAnimSegment()
HAnimSegment931.USE = "STD_Segment_r_metatarsal_3"
HAnimSegment931.bboxDisplay = False
HAnimSegment931.visible = True

HAnimHumanoid14.segments.append(HAnimSegment931)
HAnimSegment932 = x3d.HAnimSegment()
HAnimSegment932.USE = "STD_Segment_l_metatarsal_4"
HAnimSegment932.bboxDisplay = False
HAnimSegment932.visible = True

HAnimHumanoid14.segments.append(HAnimSegment932)
HAnimSegment933 = x3d.HAnimSegment()
HAnimSegment933.USE = "STD_Segment_r_metatarsal_4"
HAnimSegment933.bboxDisplay = False
HAnimSegment933.visible = True

HAnimHumanoid14.segments.append(HAnimSegment933)
HAnimSegment934 = x3d.HAnimSegment()
HAnimSegment934.USE = "STD_Segment_l_metatarsal_5"
HAnimSegment934.bboxDisplay = False
HAnimSegment934.visible = True

HAnimHumanoid14.segments.append(HAnimSegment934)
HAnimSegment935 = x3d.HAnimSegment()
HAnimSegment935.USE = "STD_Segment_r_metatarsal_5"
HAnimSegment935.bboxDisplay = False
HAnimSegment935.visible = True

HAnimHumanoid14.segments.append(HAnimSegment935)
HAnimSegment936 = x3d.HAnimSegment()
HAnimSegment936.USE = "STD_Segment_l_navicular"
HAnimSegment936.bboxDisplay = False
HAnimSegment936.visible = True

HAnimHumanoid14.segments.append(HAnimSegment936)
HAnimSegment937 = x3d.HAnimSegment()
HAnimSegment937.USE = "STD_Segment_r_navicular"
HAnimSegment937.bboxDisplay = False
HAnimSegment937.visible = True

HAnimHumanoid14.segments.append(HAnimSegment937)
HAnimSegment938 = x3d.HAnimSegment()
HAnimSegment938.USE = "STD_Segment_l_scapula"
HAnimSegment938.bboxDisplay = False
HAnimSegment938.visible = True

HAnimHumanoid14.segments.append(HAnimSegment938)
HAnimSegment939 = x3d.HAnimSegment()
HAnimSegment939.USE = "STD_Segment_r_scapula"
HAnimSegment939.bboxDisplay = False
HAnimSegment939.visible = True

HAnimHumanoid14.segments.append(HAnimSegment939)
HAnimSegment940 = x3d.HAnimSegment()
HAnimSegment940.USE = "STD_Segment_l_talus"
HAnimSegment940.bboxDisplay = False
HAnimSegment940.visible = True

HAnimHumanoid14.segments.append(HAnimSegment940)
HAnimSegment941 = x3d.HAnimSegment()
HAnimSegment941.USE = "STD_Segment_r_talus"
HAnimSegment941.bboxDisplay = False
HAnimSegment941.visible = True

HAnimHumanoid14.segments.append(HAnimSegment941)
HAnimSegment942 = x3d.HAnimSegment()
HAnimSegment942.USE = "STD_Segment_l_tarsal_distal_phalanx_1"
HAnimSegment942.bboxDisplay = False
HAnimSegment942.visible = True

HAnimHumanoid14.segments.append(HAnimSegment942)
HAnimSegment943 = x3d.HAnimSegment()
HAnimSegment943.USE = "STD_Segment_r_tarsal_distal_phalanx_1"
HAnimSegment943.bboxDisplay = False
HAnimSegment943.visible = True

HAnimHumanoid14.segments.append(HAnimSegment943)
HAnimSegment944 = x3d.HAnimSegment()
HAnimSegment944.USE = "STD_Segment_l_tarsal_distal_phalanx_2"
HAnimSegment944.bboxDisplay = False
HAnimSegment944.visible = True

HAnimHumanoid14.segments.append(HAnimSegment944)
HAnimSegment945 = x3d.HAnimSegment()
HAnimSegment945.USE = "STD_Segment_r_tarsal_distal_phalanx_2"
HAnimSegment945.bboxDisplay = False
HAnimSegment945.visible = True

HAnimHumanoid14.segments.append(HAnimSegment945)
HAnimSegment946 = x3d.HAnimSegment()
HAnimSegment946.USE = "STD_Segment_l_tarsal_distal_phalanx_3"
HAnimSegment946.bboxDisplay = False
HAnimSegment946.visible = True

HAnimHumanoid14.segments.append(HAnimSegment946)
HAnimSegment947 = x3d.HAnimSegment()
HAnimSegment947.USE = "STD_Segment_r_tarsal_distal_phalanx_3"
HAnimSegment947.bboxDisplay = False
HAnimSegment947.visible = True

HAnimHumanoid14.segments.append(HAnimSegment947)
HAnimSegment948 = x3d.HAnimSegment()
HAnimSegment948.USE = "STD_Segment_l_tarsal_distal_phalanx_4"
HAnimSegment948.bboxDisplay = False
HAnimSegment948.visible = True

HAnimHumanoid14.segments.append(HAnimSegment948)
HAnimSegment949 = x3d.HAnimSegment()
HAnimSegment949.USE = "STD_Segment_r_tarsal_distal_phalanx_4"
HAnimSegment949.bboxDisplay = False
HAnimSegment949.visible = True

HAnimHumanoid14.segments.append(HAnimSegment949)
HAnimSegment950 = x3d.HAnimSegment()
HAnimSegment950.USE = "STD_Segment_l_tarsal_distal_phalanx_5"
HAnimSegment950.bboxDisplay = False
HAnimSegment950.visible = True

HAnimHumanoid14.segments.append(HAnimSegment950)
HAnimSegment951 = x3d.HAnimSegment()
HAnimSegment951.USE = "STD_Segment_r_tarsal_distal_phalanx_5"
HAnimSegment951.bboxDisplay = False
HAnimSegment951.visible = True

HAnimHumanoid14.segments.append(HAnimSegment951)
HAnimSegment952 = x3d.HAnimSegment()
HAnimSegment952.USE = "STD_Segment_l_tarsal_middle_phalanx_2"
HAnimSegment952.bboxDisplay = False
HAnimSegment952.visible = True

HAnimHumanoid14.segments.append(HAnimSegment952)
HAnimSegment953 = x3d.HAnimSegment()
HAnimSegment953.USE = "STD_Segment_r_tarsal_middle_phalanx_2"
HAnimSegment953.bboxDisplay = False
HAnimSegment953.visible = True

HAnimHumanoid14.segments.append(HAnimSegment953)
HAnimSegment954 = x3d.HAnimSegment()
HAnimSegment954.USE = "STD_Segment_l_tarsal_middle_phalanx_3"
HAnimSegment954.bboxDisplay = False
HAnimSegment954.visible = True

HAnimHumanoid14.segments.append(HAnimSegment954)
HAnimSegment955 = x3d.HAnimSegment()
HAnimSegment955.USE = "STD_Segment_r_tarsal_middle_phalanx_3"
HAnimSegment955.bboxDisplay = False
HAnimSegment955.visible = True

HAnimHumanoid14.segments.append(HAnimSegment955)
HAnimSegment956 = x3d.HAnimSegment()
HAnimSegment956.USE = "STD_Segment_l_tarsal_middle_phalanx_4"
HAnimSegment956.bboxDisplay = False
HAnimSegment956.visible = True

HAnimHumanoid14.segments.append(HAnimSegment956)
HAnimSegment957 = x3d.HAnimSegment()
HAnimSegment957.USE = "STD_Segment_r_tarsal_middle_phalanx_4"
HAnimSegment957.bboxDisplay = False
HAnimSegment957.visible = True

HAnimHumanoid14.segments.append(HAnimSegment957)
HAnimSegment958 = x3d.HAnimSegment()
HAnimSegment958.USE = "STD_Segment_l_tarsal_middle_phalanx_5"
HAnimSegment958.bboxDisplay = False
HAnimSegment958.visible = True

HAnimHumanoid14.segments.append(HAnimSegment958)
HAnimSegment959 = x3d.HAnimSegment()
HAnimSegment959.USE = "STD_Segment_r_tarsal_middle_phalanx_5"
HAnimSegment959.bboxDisplay = False
HAnimSegment959.visible = True

HAnimHumanoid14.segments.append(HAnimSegment959)
HAnimSegment960 = x3d.HAnimSegment()
HAnimSegment960.USE = "STD_Segment_l_tarsal_proximal_phalanx_1"
HAnimSegment960.bboxDisplay = False
HAnimSegment960.visible = True

HAnimHumanoid14.segments.append(HAnimSegment960)
HAnimSegment961 = x3d.HAnimSegment()
HAnimSegment961.USE = "STD_Segment_r_tarsal_proximal_phalanx_1"
HAnimSegment961.bboxDisplay = False
HAnimSegment961.visible = True

HAnimHumanoid14.segments.append(HAnimSegment961)
HAnimSegment962 = x3d.HAnimSegment()
HAnimSegment962.USE = "STD_Segment_l_tarsal_proximal_phalanx_2"
HAnimSegment962.bboxDisplay = False
HAnimSegment962.visible = True

HAnimHumanoid14.segments.append(HAnimSegment962)
HAnimSegment963 = x3d.HAnimSegment()
HAnimSegment963.USE = "STD_Segment_r_tarsal_proximal_phalanx_2"
HAnimSegment963.bboxDisplay = False
HAnimSegment963.visible = True

HAnimHumanoid14.segments.append(HAnimSegment963)
HAnimSegment964 = x3d.HAnimSegment()
HAnimSegment964.USE = "STD_Segment_l_tarsal_proximal_phalanx_3"
HAnimSegment964.bboxDisplay = False
HAnimSegment964.visible = True

HAnimHumanoid14.segments.append(HAnimSegment964)
HAnimSegment965 = x3d.HAnimSegment()
HAnimSegment965.USE = "STD_Segment_r_tarsal_proximal_phalanx_3"
HAnimSegment965.bboxDisplay = False
HAnimSegment965.visible = True

HAnimHumanoid14.segments.append(HAnimSegment965)
HAnimSegment966 = x3d.HAnimSegment()
HAnimSegment966.USE = "STD_Segment_l_tarsal_proximal_phalanx_4"
HAnimSegment966.bboxDisplay = False
HAnimSegment966.visible = True

HAnimHumanoid14.segments.append(HAnimSegment966)
HAnimSegment967 = x3d.HAnimSegment()
HAnimSegment967.USE = "STD_Segment_r_tarsal_proximal_phalanx_4"
HAnimSegment967.bboxDisplay = False
HAnimSegment967.visible = True

HAnimHumanoid14.segments.append(HAnimSegment967)
HAnimSegment968 = x3d.HAnimSegment()
HAnimSegment968.USE = "STD_Segment_l_tarsal_proximal_phalanx_5"
HAnimSegment968.bboxDisplay = False
HAnimSegment968.visible = True

HAnimHumanoid14.segments.append(HAnimSegment968)
HAnimSegment969 = x3d.HAnimSegment()
HAnimSegment969.USE = "STD_Segment_r_tarsal_proximal_phalanx_5"
HAnimSegment969.bboxDisplay = False
HAnimSegment969.visible = True

HAnimHumanoid14.segments.append(HAnimSegment969)
HAnimSegment970 = x3d.HAnimSegment()
HAnimSegment970.USE = "STD_Segment_l_thigh"
HAnimSegment970.bboxDisplay = False
HAnimSegment970.visible = True

HAnimHumanoid14.segments.append(HAnimSegment970)
HAnimSegment971 = x3d.HAnimSegment()
HAnimSegment971.USE = "STD_Segment_r_thigh"
HAnimSegment971.bboxDisplay = False
HAnimSegment971.visible = True

HAnimHumanoid14.segments.append(HAnimSegment971)
HAnimSegment972 = x3d.HAnimSegment()
HAnimSegment972.USE = "STD_Segment_l_trapezium"
HAnimSegment972.bboxDisplay = False
HAnimSegment972.visible = True

HAnimHumanoid14.segments.append(HAnimSegment972)
HAnimSegment973 = x3d.HAnimSegment()
HAnimSegment973.USE = "STD_Segment_r_trapezium"
HAnimSegment973.bboxDisplay = False
HAnimSegment973.visible = True

HAnimHumanoid14.segments.append(HAnimSegment973)
HAnimSegment974 = x3d.HAnimSegment()
HAnimSegment974.USE = "STD_Segment_l_trapezoid"
HAnimSegment974.bboxDisplay = False
HAnimSegment974.visible = True

HAnimHumanoid14.segments.append(HAnimSegment974)
HAnimSegment975 = x3d.HAnimSegment()
HAnimSegment975.USE = "STD_Segment_r_trapezoid"
HAnimSegment975.bboxDisplay = False
HAnimSegment975.visible = True

HAnimHumanoid14.segments.append(HAnimSegment975)
HAnimSegment976 = x3d.HAnimSegment()
HAnimSegment976.USE = "STD_Segment_l_upperarm"
HAnimSegment976.bboxDisplay = False
HAnimSegment976.visible = True

HAnimHumanoid14.segments.append(HAnimSegment976)
HAnimSegment977 = x3d.HAnimSegment()
HAnimSegment977.USE = "STD_Segment_r_upperarm"
HAnimSegment977.bboxDisplay = False
HAnimSegment977.visible = True

HAnimHumanoid14.segments.append(HAnimSegment977)
HAnimSite978 = x3d.HAnimSite()
HAnimSite978.USE = "STD_Site_crotch_pt"
HAnimSite978.bboxCenter = [0,0,0]
HAnimSite978.bboxDisplay = False
HAnimSite978.bboxSize = [-1,-1,-1]
HAnimSite978.visible = True

HAnimHumanoid14.sites.append(HAnimSite978)
HAnimSite979 = x3d.HAnimSite()
HAnimSite979.USE = "STD_Site_buttocks_standing_wall_contact_point_pt"
HAnimSite979.bboxCenter = [0,0,0]
HAnimSite979.bboxDisplay = False
HAnimSite979.bboxSize = [-1,-1,-1]
HAnimSite979.visible = True

HAnimHumanoid14.sites.append(HAnimSite979)
HAnimSite980 = x3d.HAnimSite()
HAnimSite980.USE = "STD_Site_waist_preferred_posterior_pt"
HAnimSite980.bboxCenter = [0,0,0]
HAnimSite980.bboxDisplay = False
HAnimSite980.bboxSize = [-1,-1,-1]
HAnimSite980.visible = True

HAnimHumanoid14.sites.append(HAnimSite980)
HAnimSite981 = x3d.HAnimSite()
HAnimSite981.USE = "STD_Site_navel_pt"
HAnimSite981.bboxCenter = [0,0,0]
HAnimSite981.bboxDisplay = False
HAnimSite981.bboxSize = [-1,-1,-1]
HAnimSite981.visible = True

HAnimHumanoid14.sites.append(HAnimSite981)
HAnimSite982 = x3d.HAnimSite()
HAnimSite982.USE = "STD_Site_waist_preferred_anterior_pt"
HAnimSite982.bboxCenter = [0,0,0]
HAnimSite982.bboxDisplay = False
HAnimSite982.bboxSize = [-1,-1,-1]
HAnimSite982.visible = True

HAnimHumanoid14.sites.append(HAnimSite982)
HAnimSite983 = x3d.HAnimSite()
HAnimSite983.USE = "STD_Site_spine_2_middle_back_pt"
HAnimSite983.bboxCenter = [0,0,0]
HAnimSite983.bboxDisplay = False
HAnimSite983.bboxSize = [-1,-1,-1]
HAnimSite983.visible = True

HAnimHumanoid14.sites.append(HAnimSite983)
HAnimSite984 = x3d.HAnimSite()
HAnimSite984.USE = "STD_Site_substernale_pt"
HAnimSite984.bboxCenter = [0,0,0]
HAnimSite984.bboxDisplay = False
HAnimSite984.bboxSize = [-1,-1,-1]
HAnimSite984.visible = True

HAnimHumanoid14.sites.append(HAnimSite984)
HAnimSite985 = x3d.HAnimSite()
HAnimSite985.USE = "STD_Site_mesosternale_pt"
HAnimSite985.bboxCenter = [0,0,0]
HAnimSite985.bboxDisplay = False
HAnimSite985.bboxSize = [-1,-1,-1]
HAnimSite985.visible = True

HAnimHumanoid14.sites.append(HAnimSite985)
HAnimSite986 = x3d.HAnimSite()
HAnimSite986.USE = "STD_Site_rear_center_midsagittal_plane_pt"
HAnimSite986.bboxCenter = [0,0,0]
HAnimSite986.bboxDisplay = False
HAnimSite986.bboxSize = [-1,-1,-1]
HAnimSite986.visible = True

HAnimHumanoid14.sites.append(HAnimSite986)
HAnimSite987 = x3d.HAnimSite()
HAnimSite987.USE = "STD_Site_spine_1_middle_back_pt"
HAnimSite987.bboxCenter = [0,0,0]
HAnimSite987.bboxDisplay = False
HAnimSite987.bboxSize = [-1,-1,-1]
HAnimSite987.visible = True

HAnimHumanoid14.sites.append(HAnimSite987)
HAnimSite988 = x3d.HAnimSite()
HAnimSite988.USE = "STD_Site_suprasternale_pt"
HAnimSite988.bboxCenter = [0,0,0]
HAnimSite988.bboxDisplay = False
HAnimSite988.bboxSize = [-1,-1,-1]
HAnimSite988.visible = True

HAnimHumanoid14.sites.append(HAnimSite988)
HAnimSite989 = x3d.HAnimSite()
HAnimSite989.USE = "STD_Site_cervicale_pt"
HAnimSite989.bboxCenter = [0,0,0]
HAnimSite989.bboxDisplay = False
HAnimSite989.bboxSize = [-1,-1,-1]
HAnimSite989.visible = True

HAnimHumanoid14.sites.append(HAnimSite989)
HAnimSite990 = x3d.HAnimSite()
HAnimSite990.USE = "STD_Site_adams_apple_pt"
HAnimSite990.bboxCenter = [0,0,0]
HAnimSite990.bboxDisplay = False
HAnimSite990.bboxSize = [-1,-1,-1]
HAnimSite990.visible = True

HAnimHumanoid14.sites.append(HAnimSite990)
HAnimSite991 = x3d.HAnimSite()
HAnimSite991.USE = "STD_Site_sellion_pt"
HAnimSite991.bboxCenter = [0,0,0]
HAnimSite991.bboxDisplay = False
HAnimSite991.bboxSize = [-1,-1,-1]
HAnimSite991.visible = True

HAnimHumanoid14.sites.append(HAnimSite991)
HAnimSite992 = x3d.HAnimSite()
HAnimSite992.USE = "STD_Site_opisthocranion_pt"
HAnimSite992.bboxCenter = [0,0,0]
HAnimSite992.bboxDisplay = False
HAnimSite992.bboxSize = [-1,-1,-1]
HAnimSite992.visible = True

HAnimHumanoid14.sites.append(HAnimSite992)
HAnimSite993 = x3d.HAnimSite()
HAnimSite993.USE = "STD_Site_skull_vertex_pt"
HAnimSite993.bboxCenter = [0,0,0]
HAnimSite993.bboxDisplay = False
HAnimSite993.bboxSize = [-1,-1,-1]
HAnimSite993.visible = True

HAnimHumanoid14.sites.append(HAnimSite993)
HAnimSite994 = x3d.HAnimSite()
HAnimSite994.USE = "STD_Site_glabella_pt"
HAnimSite994.bboxCenter = [0,0,0]
HAnimSite994.bboxDisplay = False
HAnimSite994.bboxSize = [-1,-1,-1]
HAnimSite994.visible = True

HAnimHumanoid14.sites.append(HAnimSite994)
HAnimSite995 = x3d.HAnimSite()
HAnimSite995.USE = "STD_Site_nuchale_pt"
HAnimSite995.bboxCenter = [0,0,0]
HAnimSite995.bboxDisplay = False
HAnimSite995.bboxSize = [-1,-1,-1]
HAnimSite995.visible = True

HAnimHumanoid14.sites.append(HAnimSite995)
HAnimSite996 = x3d.HAnimSite()
HAnimSite996.USE = "STD_Site_menton_pt"
HAnimSite996.bboxCenter = [0,0,0]
HAnimSite996.bboxDisplay = False
HAnimSite996.bboxSize = [-1,-1,-1]
HAnimSite996.visible = True

HAnimHumanoid14.sites.append(HAnimSite996)
HAnimSite997 = x3d.HAnimSite()
HAnimSite997.USE = "STD_Site_supramenton_pt"
HAnimSite997.bboxCenter = [0,0,0]
HAnimSite997.bboxDisplay = False
HAnimSite997.bboxSize = [-1,-1,-1]
HAnimSite997.visible = True

HAnimHumanoid14.sites.append(HAnimSite997)
HAnimSite998 = x3d.HAnimSite()
HAnimSite998.USE = "STD_Site_l_acromion_pt"
HAnimSite998.bboxCenter = [0,0,0]
HAnimSite998.bboxDisplay = False
HAnimSite998.bboxSize = [-1,-1,-1]
HAnimSite998.visible = True

HAnimHumanoid14.sites.append(HAnimSite998)
HAnimSite999 = x3d.HAnimSite()
HAnimSite999.USE = "STD_Site_r_acromion_pt"
HAnimSite999.bboxCenter = [0,0,0]
HAnimSite999.bboxDisplay = False
HAnimSite999.bboxSize = [-1,-1,-1]
HAnimSite999.visible = True

HAnimHumanoid14.sites.append(HAnimSite999)
HAnimSite1000 = x3d.HAnimSite()
HAnimSite1000.USE = "STD_Site_l_asis_pt"
HAnimSite1000.bboxCenter = [0,0,0]
HAnimSite1000.bboxDisplay = False
HAnimSite1000.bboxSize = [-1,-1,-1]
HAnimSite1000.visible = True

HAnimHumanoid14.sites.append(HAnimSite1000)
HAnimSite1001 = x3d.HAnimSite()
HAnimSite1001.USE = "STD_Site_r_asis_pt"
HAnimSite1001.bboxCenter = [0,0,0]
HAnimSite1001.bboxDisplay = False
HAnimSite1001.bboxSize = [-1,-1,-1]
HAnimSite1001.visible = True

HAnimHumanoid14.sites.append(HAnimSite1001)
HAnimSite1002 = x3d.HAnimSite()
HAnimSite1002.USE = "STD_Site_l_axilla_distal_pt"
HAnimSite1002.bboxCenter = [0,0,0]
HAnimSite1002.bboxDisplay = False
HAnimSite1002.bboxSize = [-1,-1,-1]
HAnimSite1002.visible = True

HAnimHumanoid14.sites.append(HAnimSite1002)
HAnimSite1003 = x3d.HAnimSite()
HAnimSite1003.USE = "STD_Site_r_axilla_distal_pt"
HAnimSite1003.bboxCenter = [0,0,0]
HAnimSite1003.bboxDisplay = False
HAnimSite1003.bboxSize = [-1,-1,-1]
HAnimSite1003.visible = True

HAnimHumanoid14.sites.append(HAnimSite1003)
HAnimSite1004 = x3d.HAnimSite()
HAnimSite1004.USE = "STD_Site_l_axilla_posterior_folds_pt"
HAnimSite1004.bboxCenter = [0,0,0]
HAnimSite1004.bboxDisplay = False
HAnimSite1004.bboxSize = [-1,-1,-1]
HAnimSite1004.visible = True

HAnimHumanoid14.sites.append(HAnimSite1004)
HAnimSite1005 = x3d.HAnimSite()
HAnimSite1005.USE = "STD_Site_r_axilla_posterior_folds_pt"
HAnimSite1005.bboxCenter = [0,0,0]
HAnimSite1005.bboxDisplay = False
HAnimSite1005.bboxSize = [-1,-1,-1]
HAnimSite1005.visible = True

HAnimHumanoid14.sites.append(HAnimSite1005)
HAnimSite1006 = x3d.HAnimSite()
HAnimSite1006.USE = "STD_Site_l_axilla_proximal_pt"
HAnimSite1006.bboxCenter = [0,0,0]
HAnimSite1006.bboxDisplay = False
HAnimSite1006.bboxSize = [-1,-1,-1]
HAnimSite1006.visible = True

HAnimHumanoid14.sites.append(HAnimSite1006)
HAnimSite1007 = x3d.HAnimSite()
HAnimSite1007.USE = "STD_Site_r_axilla_proximal_pt"
HAnimSite1007.bboxCenter = [0,0,0]
HAnimSite1007.bboxDisplay = False
HAnimSite1007.bboxSize = [-1,-1,-1]
HAnimSite1007.visible = True

HAnimHumanoid14.sites.append(HAnimSite1007)
HAnimSite1008 = x3d.HAnimSite()
HAnimSite1008.USE = "STD_Site_l_bideltoid_pt"
HAnimSite1008.bboxCenter = [0,0,0]
HAnimSite1008.bboxDisplay = False
HAnimSite1008.bboxSize = [-1,-1,-1]
HAnimSite1008.visible = True

HAnimHumanoid14.sites.append(HAnimSite1008)
HAnimSite1009 = x3d.HAnimSite()
HAnimSite1009.USE = "STD_Site_r_bideltoid_pt"
HAnimSite1009.bboxCenter = [0,0,0]
HAnimSite1009.bboxDisplay = False
HAnimSite1009.bboxSize = [-1,-1,-1]
HAnimSite1009.visible = True

HAnimHumanoid14.sites.append(HAnimSite1009)
HAnimSite1010 = x3d.HAnimSite()
HAnimSite1010.USE = "STD_Site_l_calcaneus_posterior_pt"
HAnimSite1010.bboxCenter = [0,0,0]
HAnimSite1010.bboxDisplay = False
HAnimSite1010.bboxSize = [-1,-1,-1]
HAnimSite1010.visible = True

HAnimHumanoid14.sites.append(HAnimSite1010)
HAnimSite1011 = x3d.HAnimSite()
HAnimSite1011.USE = "STD_Site_r_calcaneus_posterior_pt"
HAnimSite1011.bboxCenter = [0,0,0]
HAnimSite1011.bboxDisplay = False
HAnimSite1011.bboxSize = [-1,-1,-1]
HAnimSite1011.visible = True

HAnimHumanoid14.sites.append(HAnimSite1011)
HAnimSite1012 = x3d.HAnimSite()
HAnimSite1012.USE = "STD_Site_l_carpal_distal_phalanx_1_pt"
HAnimSite1012.bboxCenter = [0,0,0]
HAnimSite1012.bboxDisplay = False
HAnimSite1012.bboxSize = [-1,-1,-1]
HAnimSite1012.visible = True

HAnimHumanoid14.sites.append(HAnimSite1012)
HAnimSite1013 = x3d.HAnimSite()
HAnimSite1013.USE = "STD_Site_r_carpal_distal_phalanx_1_pt"
HAnimSite1013.bboxCenter = [0,0,0]
HAnimSite1013.bboxDisplay = False
HAnimSite1013.bboxSize = [-1,-1,-1]
HAnimSite1013.visible = True

HAnimHumanoid14.sites.append(HAnimSite1013)
HAnimSite1014 = x3d.HAnimSite()
HAnimSite1014.USE = "STD_Site_l_carpal_distal_phalanx_2_pt"
HAnimSite1014.bboxCenter = [0,0,0]
HAnimSite1014.bboxDisplay = False
HAnimSite1014.bboxSize = [-1,-1,-1]
HAnimSite1014.visible = True

HAnimHumanoid14.sites.append(HAnimSite1014)
HAnimSite1015 = x3d.HAnimSite()
HAnimSite1015.USE = "STD_Site_r_carpal_distal_phalanx_2_pt"
HAnimSite1015.bboxCenter = [0,0,0]
HAnimSite1015.bboxDisplay = False
HAnimSite1015.bboxSize = [-1,-1,-1]
HAnimSite1015.visible = True

HAnimHumanoid14.sites.append(HAnimSite1015)
HAnimSite1016 = x3d.HAnimSite()
HAnimSite1016.USE = "STD_Site_l_carpal_distal_phalanx_3_pt"
HAnimSite1016.bboxCenter = [0,0,0]
HAnimSite1016.bboxDisplay = False
HAnimSite1016.bboxSize = [-1,-1,-1]
HAnimSite1016.visible = True

HAnimHumanoid14.sites.append(HAnimSite1016)
HAnimSite1017 = x3d.HAnimSite()
HAnimSite1017.USE = "STD_Site_r_carpal_distal_phalanx_3_pt"
HAnimSite1017.bboxCenter = [0,0,0]
HAnimSite1017.bboxDisplay = False
HAnimSite1017.bboxSize = [-1,-1,-1]
HAnimSite1017.visible = True

HAnimHumanoid14.sites.append(HAnimSite1017)
HAnimSite1018 = x3d.HAnimSite()
HAnimSite1018.USE = "STD_Site_l_carpal_distal_phalanx_4_pt"
HAnimSite1018.bboxCenter = [0,0,0]
HAnimSite1018.bboxDisplay = False
HAnimSite1018.bboxSize = [-1,-1,-1]
HAnimSite1018.visible = True

HAnimHumanoid14.sites.append(HAnimSite1018)
HAnimSite1019 = x3d.HAnimSite()
HAnimSite1019.USE = "STD_Site_r_carpal_distal_phalanx_4_pt"
HAnimSite1019.bboxCenter = [0,0,0]
HAnimSite1019.bboxDisplay = False
HAnimSite1019.bboxSize = [-1,-1,-1]
HAnimSite1019.visible = True

HAnimHumanoid14.sites.append(HAnimSite1019)
HAnimSite1020 = x3d.HAnimSite()
HAnimSite1020.USE = "STD_Site_l_carpal_distal_phalanx_5_pt"
HAnimSite1020.bboxCenter = [0,0,0]
HAnimSite1020.bboxDisplay = False
HAnimSite1020.bboxSize = [-1,-1,-1]
HAnimSite1020.visible = True

HAnimHumanoid14.sites.append(HAnimSite1020)
HAnimSite1021 = x3d.HAnimSite()
HAnimSite1021.USE = "STD_Site_r_carpal_distal_phalanx_5_pt"
HAnimSite1021.bboxCenter = [0,0,0]
HAnimSite1021.bboxDisplay = False
HAnimSite1021.bboxSize = [-1,-1,-1]
HAnimSite1021.visible = True

HAnimHumanoid14.sites.append(HAnimSite1021)
HAnimSite1022 = x3d.HAnimSite()
HAnimSite1022.USE = "STD_Site_l_chest_midsagittal_plane_pt"
HAnimSite1022.bboxCenter = [0,0,0]
HAnimSite1022.bboxDisplay = False
HAnimSite1022.bboxSize = [-1,-1,-1]
HAnimSite1022.visible = True

HAnimHumanoid14.sites.append(HAnimSite1022)
HAnimSite1023 = x3d.HAnimSite()
HAnimSite1023.USE = "STD_Site_r_chest_midsagittal_plane_pt"
HAnimSite1023.bboxCenter = [0,0,0]
HAnimSite1023.bboxDisplay = False
HAnimSite1023.bboxSize = [-1,-1,-1]
HAnimSite1023.visible = True

HAnimHumanoid14.sites.append(HAnimSite1023)
HAnimSite1024 = x3d.HAnimSite()
HAnimSite1024.USE = "STD_Site_l_clavicale_pt"
HAnimSite1024.bboxCenter = [0,0,0]
HAnimSite1024.bboxDisplay = False
HAnimSite1024.bboxSize = [-1,-1,-1]
HAnimSite1024.visible = True

HAnimHumanoid14.sites.append(HAnimSite1024)
HAnimSite1025 = x3d.HAnimSite()
HAnimSite1025.USE = "STD_Site_r_clavicale_pt"
HAnimSite1025.bboxCenter = [0,0,0]
HAnimSite1025.bboxDisplay = False
HAnimSite1025.bboxSize = [-1,-1,-1]
HAnimSite1025.visible = True

HAnimHumanoid14.sites.append(HAnimSite1025)
HAnimSite1026 = x3d.HAnimSite()
HAnimSite1026.USE = "STD_Site_l_dactylion_pt"
HAnimSite1026.bboxCenter = [0,0,0]
HAnimSite1026.bboxDisplay = False
HAnimSite1026.bboxSize = [-1,-1,-1]
HAnimSite1026.visible = True

HAnimHumanoid14.sites.append(HAnimSite1026)
HAnimSite1027 = x3d.HAnimSite()
HAnimSite1027.USE = "STD_Site_r_dactylion_pt"
HAnimSite1027.bboxCenter = [0,0,0]
HAnimSite1027.bboxDisplay = False
HAnimSite1027.bboxSize = [-1,-1,-1]
HAnimSite1027.visible = True

HAnimHumanoid14.sites.append(HAnimSite1027)
HAnimSite1028 = x3d.HAnimSite()
HAnimSite1028.USE = "STD_Site_r_ectocanthus_pt"
HAnimSite1028.bboxCenter = [0,0,0]
HAnimSite1028.bboxDisplay = False
HAnimSite1028.bboxSize = [-1,-1,-1]
HAnimSite1028.visible = True

HAnimHumanoid14.sites.append(HAnimSite1028)
HAnimSite1029 = x3d.HAnimSite()
HAnimSite1029.USE = "STD_Site_l_ectocanthus_pt"
HAnimSite1029.bboxCenter = [0,0,0]
HAnimSite1029.bboxDisplay = False
HAnimSite1029.bboxSize = [-1,-1,-1]
HAnimSite1029.visible = True

HAnimHumanoid14.sites.append(HAnimSite1029)
HAnimSite1030 = x3d.HAnimSite()
HAnimSite1030.USE = "STD_Site_l_femoral_lateral_epicondyles_pt"
HAnimSite1030.bboxCenter = [0,0,0]
HAnimSite1030.bboxDisplay = False
HAnimSite1030.bboxSize = [-1,-1,-1]
HAnimSite1030.visible = True

HAnimHumanoid14.sites.append(HAnimSite1030)
HAnimSite1031 = x3d.HAnimSite()
HAnimSite1031.USE = "STD_Site_r_femoral_lateral_epicondyles_pt"
HAnimSite1031.bboxCenter = [0,0,0]
HAnimSite1031.bboxDisplay = False
HAnimSite1031.bboxSize = [-1,-1,-1]
HAnimSite1031.visible = True

HAnimHumanoid14.sites.append(HAnimSite1031)
HAnimSite1032 = x3d.HAnimSite()
HAnimSite1032.USE = "STD_Site_l_femoral_medial_epicondyles_pt"
HAnimSite1032.bboxCenter = [0,0,0]
HAnimSite1032.bboxDisplay = False
HAnimSite1032.bboxSize = [-1,-1,-1]
HAnimSite1032.visible = True

HAnimHumanoid14.sites.append(HAnimSite1032)
HAnimSite1033 = x3d.HAnimSite()
HAnimSite1033.USE = "STD_Site_r_femoral_medial_epicondyles_pt"
HAnimSite1033.bboxCenter = [0,0,0]
HAnimSite1033.bboxDisplay = False
HAnimSite1033.bboxSize = [-1,-1,-1]
HAnimSite1033.visible = True

HAnimHumanoid14.sites.append(HAnimSite1033)
HAnimSite1034 = x3d.HAnimSite()
HAnimSite1034.USE = "STD_Site_r_gonion_pt"
HAnimSite1034.bboxCenter = [0,0,0]
HAnimSite1034.bboxDisplay = False
HAnimSite1034.bboxSize = [-1,-1,-1]
HAnimSite1034.visible = True

HAnimHumanoid14.sites.append(HAnimSite1034)
HAnimSite1035 = x3d.HAnimSite()
HAnimSite1035.USE = "STD_Site_l_gonion_pt"
HAnimSite1035.bboxCenter = [0,0,0]
HAnimSite1035.bboxDisplay = False
HAnimSite1035.bboxSize = [-1,-1,-1]
HAnimSite1035.visible = True

HAnimHumanoid14.sites.append(HAnimSite1035)
HAnimSite1036 = x3d.HAnimSite()
HAnimSite1036.USE = "STD_Site_l_humeral_lateral_epicondyles_pt"
HAnimSite1036.bboxCenter = [0,0,0]
HAnimSite1036.bboxDisplay = False
HAnimSite1036.bboxSize = [-1,-1,-1]
HAnimSite1036.visible = True

HAnimHumanoid14.sites.append(HAnimSite1036)
HAnimSite1037 = x3d.HAnimSite()
HAnimSite1037.USE = "STD_Site_r_humeral_lateral_epicondyles_pt"
HAnimSite1037.bboxCenter = [0,0,0]
HAnimSite1037.bboxDisplay = False
HAnimSite1037.bboxSize = [-1,-1,-1]
HAnimSite1037.visible = True

HAnimHumanoid14.sites.append(HAnimSite1037)
HAnimSite1038 = x3d.HAnimSite()
HAnimSite1038.USE = "STD_Site_l_humeral_medial_epicondyles_pt"
HAnimSite1038.bboxCenter = [0,0,0]
HAnimSite1038.bboxDisplay = False
HAnimSite1038.bboxSize = [-1,-1,-1]
HAnimSite1038.visible = True

HAnimHumanoid14.sites.append(HAnimSite1038)
HAnimSite1039 = x3d.HAnimSite()
HAnimSite1039.USE = "STD_Site_r_humeral_medial_epicondyles_pt"
HAnimSite1039.bboxCenter = [0,0,0]
HAnimSite1039.bboxDisplay = False
HAnimSite1039.bboxSize = [-1,-1,-1]
HAnimSite1039.visible = True

HAnimHumanoid14.sites.append(HAnimSite1039)
HAnimSite1040 = x3d.HAnimSite()
HAnimSite1040.USE = "STD_Site_r_iliocristale_pt"
HAnimSite1040.bboxCenter = [0,0,0]
HAnimSite1040.bboxDisplay = False
HAnimSite1040.bboxSize = [-1,-1,-1]
HAnimSite1040.visible = True

HAnimHumanoid14.sites.append(HAnimSite1040)
HAnimSite1041 = x3d.HAnimSite()
HAnimSite1041.USE = "STD_Site_l_iliocristale_pt"
HAnimSite1041.bboxCenter = [0,0,0]
HAnimSite1041.bboxDisplay = False
HAnimSite1041.bboxSize = [-1,-1,-1]
HAnimSite1041.visible = True

HAnimHumanoid14.sites.append(HAnimSite1041)
HAnimSite1042 = x3d.HAnimSite()
HAnimSite1042.USE = "STD_Site_l_infraorbitale_pt"
HAnimSite1042.bboxCenter = [0,0,0]
HAnimSite1042.bboxDisplay = False
HAnimSite1042.bboxSize = [-1,-1,-1]
HAnimSite1042.visible = True

HAnimHumanoid14.sites.append(HAnimSite1042)
HAnimSite1043 = x3d.HAnimSite()
HAnimSite1043.USE = "STD_Site_r_infraorbitale_pt"
HAnimSite1043.bboxCenter = [0,0,0]
HAnimSite1043.bboxDisplay = False
HAnimSite1043.bboxSize = [-1,-1,-1]
HAnimSite1043.visible = True

HAnimHumanoid14.sites.append(HAnimSite1043)
HAnimSite1044 = x3d.HAnimSite()
HAnimSite1044.USE = "STD_Site_l_knee_crease_pt"
HAnimSite1044.bboxCenter = [0,0,0]
HAnimSite1044.bboxDisplay = False
HAnimSite1044.bboxSize = [-1,-1,-1]
HAnimSite1044.visible = True

HAnimHumanoid14.sites.append(HAnimSite1044)
HAnimSite1045 = x3d.HAnimSite()
HAnimSite1045.USE = "STD_Site_r_knee_crease_pt"
HAnimSite1045.bboxCenter = [0,0,0]
HAnimSite1045.bboxDisplay = False
HAnimSite1045.bboxSize = [-1,-1,-1]
HAnimSite1045.visible = True

HAnimHumanoid14.sites.append(HAnimSite1045)
HAnimSite1046 = x3d.HAnimSite()
HAnimSite1046.USE = "STD_Site_l_lateral_malleolus_pt"
HAnimSite1046.bboxCenter = [0,0,0]
HAnimSite1046.bboxDisplay = False
HAnimSite1046.bboxSize = [-1,-1,-1]
HAnimSite1046.visible = True

HAnimHumanoid14.sites.append(HAnimSite1046)
HAnimSite1047 = x3d.HAnimSite()
HAnimSite1047.USE = "STD_Site_r_lateral_malleolus_pt"
HAnimSite1047.bboxCenter = [0,0,0]
HAnimSite1047.bboxDisplay = False
HAnimSite1047.bboxSize = [-1,-1,-1]
HAnimSite1047.visible = True

HAnimHumanoid14.sites.append(HAnimSite1047)
HAnimSite1048 = x3d.HAnimSite()
HAnimSite1048.USE = "STD_Site_l_medial_malleolus_pt"
HAnimSite1048.bboxCenter = [0,0,0]
HAnimSite1048.bboxDisplay = False
HAnimSite1048.bboxSize = [-1,-1,-1]
HAnimSite1048.visible = True

HAnimHumanoid14.sites.append(HAnimSite1048)
HAnimSite1049 = x3d.HAnimSite()
HAnimSite1049.USE = "STD_Site_r_medial_malleolus_pt"
HAnimSite1049.bboxCenter = [0,0,0]
HAnimSite1049.bboxDisplay = False
HAnimSite1049.bboxSize = [-1,-1,-1]
HAnimSite1049.visible = True

HAnimHumanoid14.sites.append(HAnimSite1049)
HAnimSite1050 = x3d.HAnimSite()
HAnimSite1050.USE = "STD_Site_l_metacarpal_phalanx_2_pt"
HAnimSite1050.bboxCenter = [0,0,0]
HAnimSite1050.bboxDisplay = False
HAnimSite1050.bboxSize = [-1,-1,-1]
HAnimSite1050.visible = True

HAnimHumanoid14.sites.append(HAnimSite1050)
HAnimSite1051 = x3d.HAnimSite()
HAnimSite1051.USE = "STD_Site_r_metacarpal_phalanx_2_pt"
HAnimSite1051.bboxCenter = [0,0,0]
HAnimSite1051.bboxDisplay = False
HAnimSite1051.bboxSize = [-1,-1,-1]
HAnimSite1051.visible = True

HAnimHumanoid14.sites.append(HAnimSite1051)
HAnimSite1052 = x3d.HAnimSite()
HAnimSite1052.USE = "STD_Site_l_metacarpal_phalanx_3_pt"
HAnimSite1052.bboxCenter = [0,0,0]
HAnimSite1052.bboxDisplay = False
HAnimSite1052.bboxSize = [-1,-1,-1]
HAnimSite1052.visible = True

HAnimHumanoid14.sites.append(HAnimSite1052)
HAnimSite1053 = x3d.HAnimSite()
HAnimSite1053.USE = "STD_Site_r_metacarpal_phalanx_3_pt"
HAnimSite1053.bboxCenter = [0,0,0]
HAnimSite1053.bboxDisplay = False
HAnimSite1053.bboxSize = [-1,-1,-1]
HAnimSite1053.visible = True

HAnimHumanoid14.sites.append(HAnimSite1053)
HAnimSite1054 = x3d.HAnimSite()
HAnimSite1054.USE = "STD_Site_l_metacarpal_phalanx_5_pt"
HAnimSite1054.bboxCenter = [0,0,0]
HAnimSite1054.bboxDisplay = False
HAnimSite1054.bboxSize = [-1,-1,-1]
HAnimSite1054.visible = True

HAnimHumanoid14.sites.append(HAnimSite1054)
HAnimSite1055 = x3d.HAnimSite()
HAnimSite1055.USE = "STD_Site_r_metacarpal_phalanx_5_pt"
HAnimSite1055.bboxCenter = [0,0,0]
HAnimSite1055.bboxDisplay = False
HAnimSite1055.bboxSize = [-1,-1,-1]
HAnimSite1055.visible = True

HAnimHumanoid14.sites.append(HAnimSite1055)
HAnimSite1056 = x3d.HAnimSite()
HAnimSite1056.USE = "STD_Site_l_metatarsal_phalanx_1_pt"
HAnimSite1056.bboxCenter = [0,0,0]
HAnimSite1056.bboxDisplay = False
HAnimSite1056.bboxSize = [-1,-1,-1]
HAnimSite1056.visible = True

HAnimHumanoid14.sites.append(HAnimSite1056)
HAnimSite1057 = x3d.HAnimSite()
HAnimSite1057.USE = "STD_Site_r_metatarsal_phalanx_1_pt"
HAnimSite1057.bboxCenter = [0,0,0]
HAnimSite1057.bboxDisplay = False
HAnimSite1057.bboxSize = [-1,-1,-1]
HAnimSite1057.visible = True

HAnimHumanoid14.sites.append(HAnimSite1057)
HAnimSite1058 = x3d.HAnimSite()
HAnimSite1058.USE = "STD_Site_l_metatarsal_phalanx_5_pt"
HAnimSite1058.bboxCenter = [0,0,0]
HAnimSite1058.bboxDisplay = False
HAnimSite1058.bboxSize = [-1,-1,-1]
HAnimSite1058.visible = True

HAnimHumanoid14.sites.append(HAnimSite1058)
HAnimSite1059 = x3d.HAnimSite()
HAnimSite1059.USE = "STD_Site_r_metatarsal_phalanx_5_pt"
HAnimSite1059.bboxCenter = [0,0,0]
HAnimSite1059.bboxDisplay = False
HAnimSite1059.bboxSize = [-1,-1,-1]
HAnimSite1059.visible = True

HAnimHumanoid14.sites.append(HAnimSite1059)
HAnimSite1060 = x3d.HAnimSite()
HAnimSite1060.USE = "STD_Site_r_neck_base_pt"
HAnimSite1060.bboxCenter = [0,0,0]
HAnimSite1060.bboxDisplay = False
HAnimSite1060.bboxSize = [-1,-1,-1]
HAnimSite1060.visible = True

HAnimHumanoid14.sites.append(HAnimSite1060)
HAnimSite1061 = x3d.HAnimSite()
HAnimSite1061.USE = "STD_Site_l_neck_base_pt"
HAnimSite1061.bboxCenter = [0,0,0]
HAnimSite1061.bboxDisplay = False
HAnimSite1061.bboxSize = [-1,-1,-1]
HAnimSite1061.visible = True

HAnimHumanoid14.sites.append(HAnimSite1061)
HAnimSite1062 = x3d.HAnimSite()
HAnimSite1062.USE = "STD_Site_l_olecranon_pt"
HAnimSite1062.bboxCenter = [0,0,0]
HAnimSite1062.bboxDisplay = False
HAnimSite1062.bboxSize = [-1,-1,-1]
HAnimSite1062.visible = True

HAnimHumanoid14.sites.append(HAnimSite1062)
HAnimSite1063 = x3d.HAnimSite()
HAnimSite1063.USE = "STD_Site_r_olecranon_pt"
HAnimSite1063.bboxCenter = [0,0,0]
HAnimSite1063.bboxDisplay = False
HAnimSite1063.bboxSize = [-1,-1,-1]
HAnimSite1063.visible = True

HAnimHumanoid14.sites.append(HAnimSite1063)
HAnimSite1064 = x3d.HAnimSite()
HAnimSite1064.USE = "STD_Site_l_psis_pt"
HAnimSite1064.bboxCenter = [0,0,0]
HAnimSite1064.bboxDisplay = False
HAnimSite1064.bboxSize = [-1,-1,-1]
HAnimSite1064.visible = True

HAnimHumanoid14.sites.append(HAnimSite1064)
HAnimSite1065 = x3d.HAnimSite()
HAnimSite1065.USE = "STD_Site_r_psis_pt"
HAnimSite1065.bboxCenter = [0,0,0]
HAnimSite1065.bboxDisplay = False
HAnimSite1065.bboxSize = [-1,-1,-1]
HAnimSite1065.visible = True

HAnimHumanoid14.sites.append(HAnimSite1065)
HAnimSite1066 = x3d.HAnimSite()
HAnimSite1066.USE = "STD_Site_l_radial_styloid_pt"
HAnimSite1066.bboxCenter = [0,0,0]
HAnimSite1066.bboxDisplay = False
HAnimSite1066.bboxSize = [-1,-1,-1]
HAnimSite1066.visible = True

HAnimHumanoid14.sites.append(HAnimSite1066)
HAnimSite1067 = x3d.HAnimSite()
HAnimSite1067.USE = "STD_Site_r_radial_styloid_pt"
HAnimSite1067.bboxCenter = [0,0,0]
HAnimSite1067.bboxDisplay = False
HAnimSite1067.bboxSize = [-1,-1,-1]
HAnimSite1067.visible = True

HAnimHumanoid14.sites.append(HAnimSite1067)
HAnimSite1068 = x3d.HAnimSite()
HAnimSite1068.USE = "STD_Site_l_radiale_pt"
HAnimSite1068.bboxCenter = [0,0,0]
HAnimSite1068.bboxDisplay = False
HAnimSite1068.bboxSize = [-1,-1,-1]
HAnimSite1068.visible = True

HAnimHumanoid14.sites.append(HAnimSite1068)
HAnimSite1069 = x3d.HAnimSite()
HAnimSite1069.USE = "STD_Site_r_radiale_pt"
HAnimSite1069.bboxCenter = [0,0,0]
HAnimSite1069.bboxDisplay = False
HAnimSite1069.bboxSize = [-1,-1,-1]
HAnimSite1069.visible = True

HAnimHumanoid14.sites.append(HAnimSite1069)
HAnimSite1070 = x3d.HAnimSite()
HAnimSite1070.USE = "STD_Site_l_rib10_pt"
HAnimSite1070.bboxCenter = [0,0,0]
HAnimSite1070.bboxDisplay = False
HAnimSite1070.bboxSize = [-1,-1,-1]
HAnimSite1070.visible = True

HAnimHumanoid14.sites.append(HAnimSite1070)
HAnimSite1071 = x3d.HAnimSite()
HAnimSite1071.USE = "STD_Site_r_rib10_pt"
HAnimSite1071.bboxCenter = [0,0,0]
HAnimSite1071.bboxDisplay = False
HAnimSite1071.bboxSize = [-1,-1,-1]
HAnimSite1071.visible = True

HAnimHumanoid14.sites.append(HAnimSite1071)
HAnimSite1072 = x3d.HAnimSite()
HAnimSite1072.USE = "STD_Site_l_sphyrion_pt"
HAnimSite1072.bboxCenter = [0,0,0]
HAnimSite1072.bboxDisplay = False
HAnimSite1072.bboxSize = [-1,-1,-1]
HAnimSite1072.visible = True

HAnimHumanoid14.sites.append(HAnimSite1072)
HAnimSite1073 = x3d.HAnimSite()
HAnimSite1073.USE = "STD_Site_r_sphyrion_pt"
HAnimSite1073.bboxCenter = [0,0,0]
HAnimSite1073.bboxDisplay = False
HAnimSite1073.bboxSize = [-1,-1,-1]
HAnimSite1073.visible = True

HAnimHumanoid14.sites.append(HAnimSite1073)
HAnimSite1074 = x3d.HAnimSite()
HAnimSite1074.USE = "STD_Site_l_suprapatella_pt"
HAnimSite1074.bboxCenter = [0,0,0]
HAnimSite1074.bboxDisplay = False
HAnimSite1074.bboxSize = [-1,-1,-1]
HAnimSite1074.visible = True

HAnimHumanoid14.sites.append(HAnimSite1074)
HAnimSite1075 = x3d.HAnimSite()
HAnimSite1075.USE = "STD_Site_r_suprapatella_pt"
HAnimSite1075.bboxCenter = [0,0,0]
HAnimSite1075.bboxDisplay = False
HAnimSite1075.bboxSize = [-1,-1,-1]
HAnimSite1075.visible = True

HAnimHumanoid14.sites.append(HAnimSite1075)
HAnimSite1076 = x3d.HAnimSite()
HAnimSite1076.USE = "STD_Site_l_tarsal_distal_phalanx_1_pt"
HAnimSite1076.bboxCenter = [0,0,0]
HAnimSite1076.bboxDisplay = False
HAnimSite1076.bboxSize = [-1,-1,-1]
HAnimSite1076.visible = True

HAnimHumanoid14.sites.append(HAnimSite1076)
HAnimSite1077 = x3d.HAnimSite()
HAnimSite1077.USE = "STD_Site_r_tarsal_distal_phalanx_1_pt"
HAnimSite1077.bboxCenter = [0,0,0]
HAnimSite1077.bboxDisplay = False
HAnimSite1077.bboxSize = [-1,-1,-1]
HAnimSite1077.visible = True

HAnimHumanoid14.sites.append(HAnimSite1077)
HAnimSite1078 = x3d.HAnimSite()
HAnimSite1078.USE = "STD_Site_l_tarsal_distal_phalanx_2_pt"
HAnimSite1078.bboxCenter = [0,0,0]
HAnimSite1078.bboxDisplay = False
HAnimSite1078.bboxSize = [-1,-1,-1]
HAnimSite1078.visible = True

HAnimHumanoid14.sites.append(HAnimSite1078)
HAnimSite1079 = x3d.HAnimSite()
HAnimSite1079.USE = "STD_Site_r_tarsal_distal_phalanx_2_pt"
HAnimSite1079.bboxCenter = [0,0,0]
HAnimSite1079.bboxDisplay = False
HAnimSite1079.bboxSize = [-1,-1,-1]
HAnimSite1079.visible = True

HAnimHumanoid14.sites.append(HAnimSite1079)
HAnimSite1080 = x3d.HAnimSite()
HAnimSite1080.USE = "STD_Site_l_tarsal_distal_phalanx_3_pt"
HAnimSite1080.bboxCenter = [0,0,0]
HAnimSite1080.bboxDisplay = False
HAnimSite1080.bboxSize = [-1,-1,-1]
HAnimSite1080.visible = True

HAnimHumanoid14.sites.append(HAnimSite1080)
HAnimSite1081 = x3d.HAnimSite()
HAnimSite1081.USE = "STD_Site_r_tarsal_distal_phalanx_3_pt"
HAnimSite1081.bboxCenter = [0,0,0]
HAnimSite1081.bboxDisplay = False
HAnimSite1081.bboxSize = [-1,-1,-1]
HAnimSite1081.visible = True

HAnimHumanoid14.sites.append(HAnimSite1081)
HAnimSite1082 = x3d.HAnimSite()
HAnimSite1082.USE = "STD_Site_l_tarsal_distal_phalanx_4_pt"
HAnimSite1082.bboxCenter = [0,0,0]
HAnimSite1082.bboxDisplay = False
HAnimSite1082.bboxSize = [-1,-1,-1]
HAnimSite1082.visible = True

HAnimHumanoid14.sites.append(HAnimSite1082)
HAnimSite1083 = x3d.HAnimSite()
HAnimSite1083.USE = "STD_Site_r_tarsal_distal_phalanx_4_pt"
HAnimSite1083.bboxCenter = [0,0,0]
HAnimSite1083.bboxDisplay = False
HAnimSite1083.bboxSize = [-1,-1,-1]
HAnimSite1083.visible = True

HAnimHumanoid14.sites.append(HAnimSite1083)
HAnimSite1084 = x3d.HAnimSite()
HAnimSite1084.USE = "STD_Site_l_tarsal_distal_phalanx_5_pt"
HAnimSite1084.bboxCenter = [0,0,0]
HAnimSite1084.bboxDisplay = False
HAnimSite1084.bboxSize = [-1,-1,-1]
HAnimSite1084.visible = True

HAnimHumanoid14.sites.append(HAnimSite1084)
HAnimSite1085 = x3d.HAnimSite()
HAnimSite1085.USE = "STD_Site_r_tarsal_distal_phalanx_5_pt"
HAnimSite1085.bboxCenter = [0,0,0]
HAnimSite1085.bboxDisplay = False
HAnimSite1085.bboxSize = [-1,-1,-1]
HAnimSite1085.visible = True

HAnimHumanoid14.sites.append(HAnimSite1085)
HAnimSite1086 = x3d.HAnimSite()
HAnimSite1086.USE = "STD_Site_l_thelion_pt"
HAnimSite1086.bboxCenter = [0,0,0]
HAnimSite1086.bboxDisplay = False
HAnimSite1086.bboxSize = [-1,-1,-1]
HAnimSite1086.visible = True

HAnimHumanoid14.sites.append(HAnimSite1086)
HAnimSite1087 = x3d.HAnimSite()
HAnimSite1087.USE = "STD_Site_r_thelion_pt"
HAnimSite1087.bboxCenter = [0,0,0]
HAnimSite1087.bboxDisplay = False
HAnimSite1087.bboxSize = [-1,-1,-1]
HAnimSite1087.visible = True

HAnimHumanoid14.sites.append(HAnimSite1087)
HAnimSite1088 = x3d.HAnimSite()
HAnimSite1088.USE = "STD_Site_l_tibiale_pt"
HAnimSite1088.bboxCenter = [0,0,0]
HAnimSite1088.bboxDisplay = False
HAnimSite1088.bboxSize = [-1,-1,-1]
HAnimSite1088.visible = True

HAnimHumanoid14.sites.append(HAnimSite1088)
HAnimSite1089 = x3d.HAnimSite()
HAnimSite1089.USE = "STD_Site_r_tibiale_pt"
HAnimSite1089.bboxCenter = [0,0,0]
HAnimSite1089.bboxDisplay = False
HAnimSite1089.bboxSize = [-1,-1,-1]
HAnimSite1089.visible = True

HAnimHumanoid14.sites.append(HAnimSite1089)
HAnimSite1090 = x3d.HAnimSite()
HAnimSite1090.USE = "STD_Site_r_tragion_pt"
HAnimSite1090.bboxCenter = [0,0,0]
HAnimSite1090.bboxDisplay = False
HAnimSite1090.bboxSize = [-1,-1,-1]
HAnimSite1090.visible = True

HAnimHumanoid14.sites.append(HAnimSite1090)
HAnimSite1091 = x3d.HAnimSite()
HAnimSite1091.USE = "STD_Site_l_tragion_pt"
HAnimSite1091.bboxCenter = [0,0,0]
HAnimSite1091.bboxDisplay = False
HAnimSite1091.bboxSize = [-1,-1,-1]
HAnimSite1091.visible = True

HAnimHumanoid14.sites.append(HAnimSite1091)
HAnimSite1092 = x3d.HAnimSite()
HAnimSite1092.USE = "STD_Site_r_trochanterion_pt"
HAnimSite1092.bboxCenter = [0,0,0]
HAnimSite1092.bboxDisplay = False
HAnimSite1092.bboxSize = [-1,-1,-1]
HAnimSite1092.visible = True

HAnimHumanoid14.sites.append(HAnimSite1092)
HAnimSite1093 = x3d.HAnimSite()
HAnimSite1093.USE = "STD_Site_l_trochanterion_pt"
HAnimSite1093.bboxCenter = [0,0,0]
HAnimSite1093.bboxDisplay = False
HAnimSite1093.bboxSize = [-1,-1,-1]
HAnimSite1093.visible = True

HAnimHumanoid14.sites.append(HAnimSite1093)
HAnimSite1094 = x3d.HAnimSite()
HAnimSite1094.USE = "STD_Site_l_ulnar_styloid_pt"
HAnimSite1094.bboxCenter = [0,0,0]
HAnimSite1094.bboxDisplay = False
HAnimSite1094.bboxSize = [-1,-1,-1]
HAnimSite1094.visible = True

HAnimHumanoid14.sites.append(HAnimSite1094)
HAnimSite1095 = x3d.HAnimSite()
HAnimSite1095.USE = "STD_Site_r_ulnar_styloid_pt"
HAnimSite1095.bboxCenter = [0,0,0]
HAnimSite1095.bboxDisplay = False
HAnimSite1095.bboxSize = [-1,-1,-1]
HAnimSite1095.visible = True

HAnimHumanoid14.sites.append(HAnimSite1095)
HAnimSegment1096 = x3d.HAnimSegment()
HAnimSegment1096.USE = "STD_HAnimSegment_HumanoidRoot"

HAnimHumanoid14.segments.append(HAnimSegment1096)

HAnimHumanoid10.skeleton.append(HAnimHumanoid10)

X3D0.Scene = Scene10
f = open("skeletonTidy_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
