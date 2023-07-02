print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Immersive"
X3D0.version = "4.0"
head1 = x3d.head()
component2 = x3d.component()
component2.name = "HAnim"
component2.level = 3

head1.children.append(component2)
meta3 = x3d.meta()
meta3.name = "title"
meta3.content = "BvhConversion1Illustrated.x3d"

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.name = "description"
meta4.content = "BVH file conversion: test case showing current BVH-to-X3D conversion results of \"invisible\" skeleton, with node visualization geometry later applied from X3dToXhtml stylesheet-produced HumanoidRootHAnimHumanoidReport."

head1.children.append(meta4)
meta5 = x3d.meta()
meta5.name = "creator"
meta5.content = "TODO unknown original creator of file 1.bvh, please advise if known"

head1.children.append(meta5)
meta6 = x3d.meta()
meta6.name = "translator"
meta6.content = "Don Brutzman"

head1.children.append(meta6)
meta7 = x3d.meta()
meta7.name = "created"
meta7.content = "1 January 2016"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.name = "translated"
meta8.content = "30 October 2022"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "modified"
meta9.content = "29 December 2022"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "warning"
meta10.content = "under development, TODO fix transcription of HAnimSite nodes. A few further improvements needed in X3dToXhhtml.xslt HAnim report stylesheet"

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.name = "Image"
meta11.content = "BvhConversion1Illustrated.png"

head1.children.append(meta11)
meta12 = x3d.meta()
meta12.name = "reference"
meta12.content = "BvhConversion1Invisible.html#HumanoidRootHAnimHumanoidReport"

head1.children.append(meta12)
meta13 = x3d.meta()
meta13.name = "Image"
meta13.content = "BvhConversion1.png"

head1.children.append(meta13)
meta14 = x3d.meta()
meta14.name = "MovingImage"
meta14.content = "BvhConversion1.mp4"

head1.children.append(meta14)
meta15 = x3d.meta()
meta15.name = "reference"
meta15.content = "1.bvh"

head1.children.append(meta15)
meta16 = x3d.meta()
meta16.name = "reference"
meta16.content = "1.bvh.txt"

head1.children.append(meta16)
meta17 = x3d.meta()
meta17.name = "Image"
meta17.content = "1.bvhacker.png"

head1.children.append(meta17)
meta18 = x3d.meta()
meta18.name = "reference"
meta18.content = "http://www.bvhacker.com"

head1.children.append(meta18)
meta19 = x3d.meta()
meta19.name = "reference"
meta19.content = "BvhSeamless3dExport1.x3d"

head1.children.append(meta19)
meta20 = x3d.meta()
meta20.name = "reference"
meta20.content = "BvhConversion1Index.html"

head1.children.append(meta20)
meta21 = x3d.meta()
meta21.name = "reference"
meta21.content = "BvhConversion1InvisibleIndex.html"

head1.children.append(meta21)
meta22 = x3d.meta()
meta22.name = "reference"
meta22.content = "http://www.character-studio.net/bvh_file_specification.htm"

head1.children.append(meta22)
meta23 = x3d.meta()
meta23.name = "reference"
meta23.content = "https://www.web3d.org/x3d/content/examples/X3dSceneAuthoringHints.html#MOCAP"

head1.children.append(meta23)
meta24 = x3d.meta()
meta24.name = "generator"
meta24.content = "Java BVH to X3D Converter, org.web3d.x3d.hanim.bvh package"

head1.children.append(meta24)
meta25 = x3d.meta()
meta25.name = "generator"
meta25.content = "X3D-Edit 4.0, https://savage.nps.edu/X3D-Edit"

head1.children.append(meta25)
meta26 = x3d.meta()
meta26.name = "identifier"
meta26.content = "https://www.web3d.org/x3d/content/examples/HumanoidAnimation/MotionAnimation/BvhConversion1Illustrated.x3d"

head1.children.append(meta26)
meta27 = x3d.meta()
meta27.name = "license"
meta27.content = "../license.html"

head1.children.append(meta27)

X3D0.head = head1
Scene28 = x3d.Scene()
WorldInfo29 = x3d.WorldInfo()
WorldInfo29.title = "BvhConversion1Illustrated.x3d"

Scene28.children.append(WorldInfo29)
NavigationInfo30 = x3d.NavigationInfo()

Scene28.children.append(NavigationInfo30)
Group31 = x3d.Group()
Group31.DEF = "BvhConversion1_BvhToX3dConversionImportInformation"
#20 BVH JOINT definitions found, following a single HIERARCHY ROOT
#BVH HIERARCHY model size computations: minX=0.0, maxX=0.0, width=0.0; minY=-17.78, maxY=10.16, height=27.94; minZ=0.0, maxZ=15.24, depth=15.24
#Estimated rescaling to meters based on height: scaleFactor=0.0254 for modified height of 0.710m
#Vertical offset to move bottom of BVH figure to ground plane (adjusted in HAnimJoint containerField='skeleton'): heightOffset=0.451612m
MetadataSet32 = x3d.MetadataSet()
MetadataSet32.name = "BvhToHAnimConversionNameTable"
#key: MetadataString name='bvhName' reference='bvhType' value='\"name\" \"segmentName\"' (no segmentName for HAnimSite nodes)
MetadataString33 = x3d.MetadataString()
MetadataString33.name = "ROOT_Hips"
MetadataString33.reference = "ROOT"
MetadataString33.value = ["humanoid_root","sacrum"]

if MetadataSet32.value is None:
    MetadataSet32.value = []
MetadataSet32.value.append(MetadataString33)
MetadataString34 = x3d.MetadataString()
MetadataString34.name = "LeftHip"
MetadataString34.reference = "JOINT"
MetadataString34.value = ["l_hip","l_thigh"]

if MetadataSet32.value is None:
    MetadataSet32.value = []
MetadataSet32.value.append(MetadataString34)
MetadataString35 = x3d.MetadataString()
MetadataString35.name = "LeftKnee"
MetadataString35.reference = "JOINT"
MetadataString35.value = ["l_knee","l_calf"]

if MetadataSet32.value is None:
    MetadataSet32.value = []
MetadataSet32.value.append(MetadataString35)
MetadataString36 = x3d.MetadataString()
MetadataString36.name = "LeftAnkle"
MetadataString36.reference = "JOINT"
MetadataString36.value = ["l_ankle","l_hindfoot"]

if MetadataSet32.value is None:
    MetadataSet32.value = []
MetadataSet32.value.append(MetadataString36)
MetadataString37 = x3d.MetadataString()
MetadataString37.name = "LeftAnkleEnd"
MetadataString37.reference = "JOINT"
MetadataString37.value = ["l_midtarsal","l_middistal"]

if MetadataSet32.value is None:
    MetadataSet32.value = []
MetadataSet32.value.append(MetadataString37)
MetadataString38 = x3d.MetadataString()
MetadataString38.name = "LeftAnkleEndSite"
MetadataString38.reference = "Site"
MetadataString38.value = ["l_midtarsal_tip"]

if MetadataSet32.value is None:
    MetadataSet32.value = []
MetadataSet32.value.append(MetadataString38)
MetadataString39 = x3d.MetadataString()
MetadataString39.name = "RightHip"
MetadataString39.reference = "JOINT"
MetadataString39.value = ["r_hip","r_thigh"]

if MetadataSet32.value is None:
    MetadataSet32.value = []
MetadataSet32.value.append(MetadataString39)
MetadataString40 = x3d.MetadataString()
MetadataString40.name = "RightKnee"
MetadataString40.reference = "JOINT"
MetadataString40.value = ["r_knee","r_calf"]

if MetadataSet32.value is None:
    MetadataSet32.value = []
MetadataSet32.value.append(MetadataString40)
MetadataString41 = x3d.MetadataString()
MetadataString41.name = "RightAnkle"
MetadataString41.reference = "JOINT"
MetadataString41.value = ["r_ankle","r_hindfoot"]

if MetadataSet32.value is None:
    MetadataSet32.value = []
MetadataSet32.value.append(MetadataString41)
MetadataString42 = x3d.MetadataString()
MetadataString42.name = "RightAnkleEnd"
MetadataString42.reference = "JOINT"
MetadataString42.value = ["r_midtarsal","r_middistal"]

if MetadataSet32.value is None:
    MetadataSet32.value = []
MetadataSet32.value.append(MetadataString42)
MetadataString43 = x3d.MetadataString()
MetadataString43.name = "RightAnkleEndSite"
MetadataString43.reference = "Site"
MetadataString43.value = ["r_midtarsal_tip"]

if MetadataSet32.value is None:
    MetadataSet32.value = []
MetadataSet32.value.append(MetadataString43)
MetadataString44 = x3d.MetadataString()
MetadataString44.name = "Chest"
MetadataString44.reference = "JOINT"
MetadataString44.value = ["vl5","l5"]

if MetadataSet32.value is None:
    MetadataSet32.value = []
MetadataSet32.value.append(MetadataString44)
MetadataString45 = x3d.MetadataString()
MetadataString45.name = "Chest2"
MetadataString45.reference = "JOINT"
MetadataString45.value = ["Chest2","vl5_to_Chest2"]

if MetadataSet32.value is None:
    MetadataSet32.value = []
MetadataSet32.value.append(MetadataString45)
MetadataString46 = x3d.MetadataString()
MetadataString46.name = "LeftCollar"
MetadataString46.reference = "JOINT"
MetadataString46.value = ["LeftCollar","Chest2_to_LeftCollar"]

if MetadataSet32.value is None:
    MetadataSet32.value = []
MetadataSet32.value.append(MetadataString46)
MetadataString47 = x3d.MetadataString()
MetadataString47.name = "LeftShoulder"
MetadataString47.reference = "JOINT"
MetadataString47.value = ["l_shoulder","l_upperarm"]

if MetadataSet32.value is None:
    MetadataSet32.value = []
MetadataSet32.value.append(MetadataString47)
MetadataString48 = x3d.MetadataString()
MetadataString48.name = "LeftElbow"
MetadataString48.reference = "JOINT"
MetadataString48.value = ["l_elbow","l_forearm"]

if MetadataSet32.value is None:
    MetadataSet32.value = []
MetadataSet32.value.append(MetadataString48)
MetadataString49 = x3d.MetadataString()
MetadataString49.name = "LeftWrist"
MetadataString49.reference = "JOINT"
MetadataString49.value = ["l_wrist","l_hand"]

if MetadataSet32.value is None:
    MetadataSet32.value = []
MetadataSet32.value.append(MetadataString49)
MetadataString50 = x3d.MetadataString()
MetadataString50.name = "LeftWristSite"
MetadataString50.reference = "Site"
MetadataString50.value = ["l_wrist_tip"]

if MetadataSet32.value is None:
    MetadataSet32.value = []
MetadataSet32.value.append(MetadataString50)
MetadataString51 = x3d.MetadataString()
MetadataString51.name = "RightCollar"
MetadataString51.reference = "JOINT"
MetadataString51.value = ["RightCollar","Chest2_to_RightCollar"]

if MetadataSet32.value is None:
    MetadataSet32.value = []
MetadataSet32.value.append(MetadataString51)
MetadataString52 = x3d.MetadataString()
MetadataString52.name = "RightShoulder"
MetadataString52.reference = "JOINT"
MetadataString52.value = ["r_shoulder","r_upperarm"]

if MetadataSet32.value is None:
    MetadataSet32.value = []
MetadataSet32.value.append(MetadataString52)
MetadataString53 = x3d.MetadataString()
MetadataString53.name = "RightElbow"
MetadataString53.reference = "JOINT"
MetadataString53.value = ["r_elbow","r_forearm"]

if MetadataSet32.value is None:
    MetadataSet32.value = []
MetadataSet32.value.append(MetadataString53)
MetadataString54 = x3d.MetadataString()
MetadataString54.name = "RightWrist"
MetadataString54.reference = "JOINT"
MetadataString54.value = ["r_wrist","r_hand"]

if MetadataSet32.value is None:
    MetadataSet32.value = []
MetadataSet32.value.append(MetadataString54)
MetadataString55 = x3d.MetadataString()
MetadataString55.name = "RightWristSite"
MetadataString55.reference = "Site"
MetadataString55.value = ["r_wrist_tip"]

if MetadataSet32.value is None:
    MetadataSet32.value = []
MetadataSet32.value.append(MetadataString55)
MetadataString56 = x3d.MetadataString()
MetadataString56.name = "Neck"
MetadataString56.reference = "JOINT"
MetadataString56.value = ["Neck","Chest2_to_Neck"]

if MetadataSet32.value is None:
    MetadataSet32.value = []
MetadataSet32.value.append(MetadataString56)
MetadataString57 = x3d.MetadataString()
MetadataString57.name = "Head"
MetadataString57.reference = "JOINT"
MetadataString57.value = ["skullbase","skull"]

if MetadataSet32.value is None:
    MetadataSet32.value = []
MetadataSet32.value.append(MetadataString57)
MetadataString58 = x3d.MetadataString()
MetadataString58.name = "HeadSite"
MetadataString58.reference = "Site"
MetadataString58.value = ["skullbase_tip"]

if MetadataSet32.value is None:
    MetadataSet32.value = []
MetadataSet32.value.append(MetadataString58)

Group31.metadata = MetadataSet32

Scene28.children.append(Group31)
#initialPositionOffset computation: 0.000 14.422 7.620, initialPositionScaled computation: 0.000 0.806 0.194
Transform59 = x3d.Transform()
Transform59.DEF = "InitialPositionScaled"
Transform59.translation = [0,0.806,0.194]
Viewpoint60 = x3d.Viewpoint()
Viewpoint60.description = "BvhConversion1Invisible model BVH to X3D conversion, from 8m"
Viewpoint60.position = [0,0,8]

Transform59.children.append(Viewpoint60)
Viewpoint61 = x3d.Viewpoint()
Viewpoint61.description = "BvhConversion1Invisible initial motion position"
Viewpoint61.position = [0.039,2.423,7.987]

Transform59.children.append(Viewpoint61)
Viewpoint62 = x3d.Viewpoint()
Viewpoint62.description = "BvhConversion1Invisible final motion position"
Viewpoint62.position = [2.697,2.404,15.107]

Transform59.children.append(Viewpoint62)

Scene28.children.append(Transform59)
HAnimHumanoid63 = x3d.HAnimHumanoid()
HAnimHumanoid63.name = "ROOT_Hips"
HAnimHumanoid63.DEF = "BvhConversion1_ROOT_Hips"
HAnimHumanoid63.version = "2.0"
#info='\"authorEmail=*TODO*\" \"authorName=*TODO*\" \"copyright=Copyright (c) 2022\" \"humanoidVersion=*TODO*\" \"usageRestrictions=*TODO*\"'
#Top-level HAnimSite/Viewpoint attached to HAnimHumanoid is unaffected by motion animation
#insert pseudo Joint for humanoid_root skeleton (matching root HIERARCHY in original BVH mocap model, but appearing as skeleton field in X3D HAnimHumanoid)
#top-level USE nodes follow DEF declarations and can be employed by inverse-kinematics (IK) engines or other HAnim tools
#TODO missing <HAnimSite USE='BvhConversion1_l_middistal_tip' containerField='sites'/> <HAnimSite USE='BvhConversion1_r_middistal_tip' containerField='sites'/> <HAnimSite USE='BvhConversion1_l_hand_tip' containerField='sites'/> <HAnimSite USE='BvhConversion1_r_hand_tip' containerField='sites'/> <HAnimSite USE='BvhConversion1_skull_tip' containerField='sites'/>
MetadataSet64 = x3d.MetadataSet()
MetadataSet64.name = "HAnimHumanoid.info"
MetadataSet64.reference = "https://www.web3d.org/documents/specifications/19774/V2.0/Architecture/ObjectInterfaces.html#Humanoid"
MetadataString65 = x3d.MetadataString()
MetadataString65.name = "authorEmail"
MetadataString65.value = ["*TODO*"]

if MetadataSet64.value is None:
    MetadataSet64.value = []
MetadataSet64.value.append(MetadataString65)
MetadataString66 = x3d.MetadataString()
MetadataString66.name = "authorName"
MetadataString66.value = ["*TODO*"]

if MetadataSet64.value is None:
    MetadataSet64.value = []
MetadataSet64.value.append(MetadataString66)
MetadataString67 = x3d.MetadataString()
MetadataString67.name = "copyright"
MetadataString67.value = ["Copyright (c) 2022"]

if MetadataSet64.value is None:
    MetadataSet64.value = []
MetadataSet64.value.append(MetadataString67)
MetadataString68 = x3d.MetadataString()
MetadataString68.name = "humanoidVersion"
MetadataString68.value = ["*TODO*"]

if MetadataSet64.value is None:
    MetadataSet64.value = []
MetadataSet64.value.append(MetadataString68)
MetadataString69 = x3d.MetadataString()
MetadataString69.name = "usageDescription"
MetadataString69.value = ["*TODO*"]

if MetadataSet64.value is None:
    MetadataSet64.value = []
MetadataSet64.value.append(MetadataString69)

HAnimHumanoid63.metadata = MetadataSet64
HAnimSite70 = x3d.HAnimSite()
HAnimSite70.name = "humanoid_root_view"
HAnimSite70.DEF = "BvhConversion1_humanoid_root_view"
#HAnimSite visualization shape
TouchSensor71 = x3d.TouchSensor()
TouchSensor71.description = "HAnimSite humanoid_root_view"

HAnimSite70.children.append(TouchSensor71)
Shape72 = x3d.Shape()
Shape72.USE = "HAnimSiteShape"

HAnimSite70.children.append(Shape72)
Viewpoint73 = x3d.Viewpoint()
Viewpoint73.DEF = "BvhConversion1_humanoid_root_viewpoint"
Viewpoint73.description = "BvhConversion1 front view towards HAnimHumanoid center"
Viewpoint73.position = [0,0,314.96062992125985]

HAnimSite70.children.append(Viewpoint73)
#HAnimSite/Viewpoint visualization shape
Anchor74 = x3d.Anchor()
Anchor74.description = "HAnimSite BvhConversion1_humanoid_root_view Viewpoint"
Anchor74.url = ["#BvhConversion1_humanoid_root_viewpoint"]
LOD75 = x3d.LOD()
LOD75.forceTransitions = True
LOD75.range = [0.04]
WorldInfo76 = x3d.WorldInfo()
WorldInfo76.info = ["hide diamond when close"]

LOD75.children.append(WorldInfo76)
Shape77 = x3d.Shape()
Shape77.DEF = "HAnimSiteViewpointShape"
IndexedFaceSet78 = x3d.IndexedFaceSet()
IndexedFaceSet78.DEF = "SiteViewpointDiamondIFS"
IndexedFaceSet78.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet78.creaseAngle = 0.5
Coordinate79 = x3d.Coordinate()

IndexedFaceSet78.coord = Coordinate79

Shape77.geometry = IndexedFaceSet78
Appearance80 = x3d.Appearance()
Material81 = x3d.Material()
Material81.diffuseColor = [0,0,1]
Material81.transparency = 0.6

Appearance80.material = Material81

Shape77.appearance = Appearance80

LOD75.children.append(Shape77)

Anchor74.children.append(LOD75)

HAnimSite70.children.append(Anchor74)

HAnimHumanoid63.viewpoints.append(HAnimSite70)
HAnimJoint82 = x3d.HAnimJoint()
HAnimJoint82.name = "humanoid_root"
HAnimJoint82.DEF = "BvhConversion1_humanoid_root"
HAnimJoint82.llimit = [0,0,0]
HAnimJoint82.scale = [0.0254,0.0254,0.0254]
HAnimJoint82.translation = [0,0.806,0.194]
HAnimJoint82.ulimit = [0,0,0]
#BVH ROOT_Hips, OFFSET 7.62 0.0 0.0, CHANNELS 6 Xposition Yposition Zposition Zrotation Xrotation Yrotation
HAnimSegment83 = x3d.HAnimSegment()
HAnimSegment83.name = "sacrum"
HAnimSegment83.DEF = "BvhConversion1_sacrum"
#<HAnimJoint name='humanoid_root'/> visualization sphere is placed within <HAnimSegment name='sacrum'/>
TouchSensor84 = x3d.TouchSensor()
TouchSensor84.description = "HAnimJoint humanoid_root, HAnimSegment sacrum"

HAnimSegment83.children.append(TouchSensor84)
Transform85 = x3d.Transform()
Shape86 = x3d.Shape()
Shape86.DEF = "HAnimJointShape"
Sphere87 = x3d.Sphere()
Sphere87.radius = 0.006

Shape86.geometry = Sphere87
Appearance88 = x3d.Appearance()
Appearance88.DEF = "HAnimJointAppearance"
Material89 = x3d.Material()
Material89.diffuseColor = [1,0.5,0]
Material89.transparency = 0.5

Appearance88.material = Material89

Shape86.appearance = Appearance88

Transform85.children.append(Shape86)

HAnimSegment83.children.append(Transform85)
#humanoid_root child HAnimSegment with visualization root shape plus hidden DEF geometry for later use (radius 1 inch)
#HAnimSegment OFFSET visualization line from current <HAnimJoint name='humanoid_root'/> to child <HAnimJoint name='l_hip'/>
#HAnimSegment OFFSET visualization line from current <HAnimJoint name='humanoid_root'/> to child <HAnimJoint name='r_hip'/>
#HAnimSegment OFFSET visualization line from current <HAnimJoint name='humanoid_root'/> to child <HAnimJoint name='vl5'/>
#HAnimSegment visualization line segment from parent <HAnimJoint name='humanoid_root'/> to <HAnimJoint name='l_hip'/>
Shape90 = x3d.Shape()
LineSet91 = x3d.LineSet()
LineSet91.vertexCount = [2]
Coordinate92 = x3d.Coordinate()

LineSet91.coord = Coordinate92
ColorRGBA93 = x3d.ColorRGBA()
ColorRGBA93.DEF = "HAnimSegmentLineColorRGBA"

LineSet91.color = ColorRGBA93

Shape90.geometry = LineSet91

HAnimSegment83.children.append(Shape90)
#HAnimSegment visualization line segment from parent <HAnimJoint name='humanoid_root'/> to <HAnimJoint name='r_hip'/>
Shape94 = x3d.Shape()
LineSet95 = x3d.LineSet()
LineSet95.vertexCount = [2]
Coordinate96 = x3d.Coordinate()

LineSet95.coord = Coordinate96
ColorRGBA97 = x3d.ColorRGBA()
ColorRGBA97.USE = "HAnimSegmentLineColorRGBA"

LineSet95.color = ColorRGBA97

Shape94.geometry = LineSet95

HAnimSegment83.children.append(Shape94)
#HAnimSegment visualization line segment from parent <HAnimJoint name='humanoid_root'/> to <HAnimJoint name='vl5'/>
Shape98 = x3d.Shape()
LineSet99 = x3d.LineSet()
LineSet99.vertexCount = [2]
Coordinate100 = x3d.Coordinate()

LineSet99.coord = Coordinate100
ColorRGBA101 = x3d.ColorRGBA()
ColorRGBA101.USE = "HAnimSegmentLineColorRGBA"

LineSet99.color = ColorRGBA101

Shape98.geometry = LineSet99

HAnimSegment83.children.append(Shape98)

HAnimJoint82.children.append(HAnimSegment83)
HAnimJoint102 = x3d.HAnimJoint()
HAnimJoint102.name = "l_hip"
HAnimJoint102.DEF = "BvhConversion1_l_hip"
HAnimJoint102.center = [7.62,0,0]
HAnimJoint102.llimit = [0,0,0]
HAnimJoint102.ulimit = [0,0,0]
#BVH JOINT LeftHip, OFFSET 7.62 0.0 0.0, CHANNELS 3 Zrotation Xrotation Yrotation
HAnimSegment103 = x3d.HAnimSegment()
HAnimSegment103.name = "l_thigh"
HAnimSegment103.DEF = "BvhConversion1_l_thigh"
#<HAnimJoint name='l_hip'/> visualization sphere is placed within <HAnimSegment name='l_thigh'/>
TouchSensor104 = x3d.TouchSensor()
TouchSensor104.description = "HAnimJoint l_hip, HAnimSegment l_thigh"

HAnimSegment103.children.append(TouchSensor104)
Transform105 = x3d.Transform()
Transform105.translation = [7.62,0,0]
Shape106 = x3d.Shape()
Shape106.USE = "HAnimJointShape"

Transform105.children.append(Shape106)

HAnimSegment103.children.append(Transform105)
#Transform to establish local-origin reference frame at center of current Joint
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_hip'/> to <HAnimJoint name='l_knee'/>
Shape107 = x3d.Shape()
LineSet108 = x3d.LineSet()
LineSet108.vertexCount = [2]
Coordinate109 = x3d.Coordinate()

LineSet108.coord = Coordinate109
ColorRGBA110 = x3d.ColorRGBA()
ColorRGBA110.USE = "HAnimSegmentLineColorRGBA"

LineSet108.color = ColorRGBA110

Shape107.geometry = LineSet108

HAnimSegment103.children.append(Shape107)

HAnimJoint102.children.append(HAnimSegment103)
HAnimJoint111 = x3d.HAnimJoint()
HAnimJoint111.name = "l_knee"
HAnimJoint111.DEF = "BvhConversion1_l_knee"
HAnimJoint111.center = [7.62,-44.449999,0]
HAnimJoint111.llimit = [0,0,0]
HAnimJoint111.ulimit = [0,0,0]
#BVH JOINT LeftKnee, OFFSET 0.0 -44.449999 0.0, CHANNELS 3 Zrotation Xrotation Yrotation
HAnimSegment112 = x3d.HAnimSegment()
HAnimSegment112.name = "l_calf"
HAnimSegment112.DEF = "BvhConversion1_l_calf"
#<HAnimJoint name='l_knee'/> visualization sphere is placed within <HAnimSegment name='l_calf'/>
TouchSensor113 = x3d.TouchSensor()
TouchSensor113.description = "HAnimJoint l_knee, HAnimSegment l_calf"

HAnimSegment112.children.append(TouchSensor113)
Transform114 = x3d.Transform()
Transform114.translation = [7.62,-44.449999,0]
Shape115 = x3d.Shape()
Shape115.USE = "HAnimJointShape"

Transform114.children.append(Shape115)

HAnimSegment112.children.append(Transform114)
#Transform to establish local-origin reference frame at center of current Joint
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_knee'/> to <HAnimJoint name='l_talocrural'/>
Shape116 = x3d.Shape()
LineSet117 = x3d.LineSet()
LineSet117.vertexCount = [2]
Coordinate118 = x3d.Coordinate()

LineSet117.coord = Coordinate118
ColorRGBA119 = x3d.ColorRGBA()
ColorRGBA119.USE = "HAnimSegmentLineColorRGBA"

LineSet117.color = ColorRGBA119

Shape116.geometry = LineSet117

HAnimSegment112.children.append(Shape116)

HAnimJoint111.children.append(HAnimSegment112)
HAnimJoint120 = x3d.HAnimJoint()
HAnimJoint120.name = "l_talocrural"
HAnimJoint120.DEF = "BvhConversion1_l_talocrural"
HAnimJoint120.center = [7.62,-83.819998,0]
HAnimJoint120.llimit = [0,0,0]
HAnimJoint120.ulimit = [0,0,0]
#BVH JOINT LeftAnkle, OFFSET 0.0 -39.369999 0.0, CHANNELS 3 Zrotation Xrotation Yrotation
HAnimSegment121 = x3d.HAnimSegment()
HAnimSegment121.name = "l_talus"
HAnimSegment121.DEF = "BvhConversion1_l_talus"
#<HAnimJoint name='l_talocrural'/> visualization sphere is placed within <HAnimSegment name='l_talus'/>
TouchSensor122 = x3d.TouchSensor()
TouchSensor122.description = "HAnimJoint l_talocrural, HAnimSegment l_talus"

HAnimSegment121.children.append(TouchSensor122)
Transform123 = x3d.Transform()
Transform123.translation = [7.62,-83.819998,0]
Shape124 = x3d.Shape()
Shape124.USE = "HAnimJointShape"

Transform123.children.append(Shape124)

HAnimSegment121.children.append(Transform123)
#Transform to establish local-origin reference frame at center of current Joint
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_talocrural'/> to <HAnimJoint name='l_metatarsophalangeal_2'/>
Shape125 = x3d.Shape()
LineSet126 = x3d.LineSet()
LineSet126.vertexCount = [2]
Coordinate127 = x3d.Coordinate()

LineSet126.coord = Coordinate127
ColorRGBA128 = x3d.ColorRGBA()
ColorRGBA128.USE = "HAnimSegmentLineColorRGBA"

LineSet126.color = ColorRGBA128

Shape125.geometry = LineSet126

HAnimSegment121.children.append(Shape125)

HAnimJoint120.children.append(HAnimSegment121)
HAnimJoint129 = x3d.HAnimJoint()
HAnimJoint129.name = "l_metatarsophalangeal_2"
HAnimJoint129.DEF = "BvhConversion1_l_metatarsophalangeal_2"
HAnimJoint129.center = [7.62,-92.709998,-3.81]
HAnimJoint129.llimit = [0,0,0]
HAnimJoint129.ulimit = [0,0,0]
#BVH JOINT LeftAnkleEnd, OFFSET 0.0 -8.89 -3.81, CHANNELS 3 Zrotation Xrotation Yrotation
HAnimSegment130 = x3d.HAnimSegment()
HAnimSegment130.name = "l_tarsal_proximal_phalanx_2"
HAnimSegment130.DEF = "BvhConversion1_l_tarsal_proximal_phalanx_2"
#<HAnimJoint name='l_metatarsophalangeal_2'/> visualization sphere is placed within <HAnimSegment name='l_tarsal_proximal_phalanx_2'/>
TouchSensor131 = x3d.TouchSensor()
TouchSensor131.description = "HAnimJoint l_metatarsophalangeal_2, HAnimSegment l_tarsal_proximal_phalanx_2"

HAnimSegment130.children.append(TouchSensor131)
Transform132 = x3d.Transform()
Transform132.translation = [7.62,-92.709998,-3.81]
Shape133 = x3d.Shape()
Shape133.USE = "HAnimJointShape"

Transform132.children.append(Shape133)

HAnimSegment130.children.append(Transform132)
#Transform to establish local-origin reference frame at center of current Joint

HAnimJoint129.children.append(HAnimSegment130)

HAnimJoint120.children.append(HAnimJoint129)

HAnimJoint111.children.append(HAnimJoint120)

HAnimJoint102.children.append(HAnimJoint111)

HAnimJoint82.children.append(HAnimJoint102)
HAnimJoint134 = x3d.HAnimJoint()
HAnimJoint134.name = "r_hip"
HAnimJoint134.DEF = "BvhConversion1_r_hip"
HAnimJoint134.center = [-7.62,0,0]
HAnimJoint134.llimit = [0,0,0]
HAnimJoint134.ulimit = [0,0,0]
#BVH JOINT RightHip, OFFSET -7.62 0.0 0.0, CHANNELS 3 Zrotation Xrotation Yrotation
HAnimSegment135 = x3d.HAnimSegment()
HAnimSegment135.name = "r_thigh"
HAnimSegment135.DEF = "BvhConversion1_r_thigh"
#<HAnimJoint name='r_hip'/> visualization sphere is placed within <HAnimSegment name='r_thigh'/>
TouchSensor136 = x3d.TouchSensor()
TouchSensor136.description = "HAnimJoint r_hip, HAnimSegment r_thigh"

HAnimSegment135.children.append(TouchSensor136)
Transform137 = x3d.Transform()
Transform137.translation = [-7.62,0,0]
Shape138 = x3d.Shape()
Shape138.USE = "HAnimJointShape"

Transform137.children.append(Shape138)

HAnimSegment135.children.append(Transform137)
#Transform to establish local-origin reference frame at center of current Joint
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_hip'/> to <HAnimJoint name='r_knee'/>
Shape139 = x3d.Shape()
LineSet140 = x3d.LineSet()
LineSet140.vertexCount = [2]
Coordinate141 = x3d.Coordinate()

LineSet140.coord = Coordinate141
ColorRGBA142 = x3d.ColorRGBA()
ColorRGBA142.USE = "HAnimSegmentLineColorRGBA"

LineSet140.color = ColorRGBA142

Shape139.geometry = LineSet140

HAnimSegment135.children.append(Shape139)

HAnimJoint134.children.append(HAnimSegment135)
HAnimJoint143 = x3d.HAnimJoint()
HAnimJoint143.name = "r_knee"
HAnimJoint143.DEF = "BvhConversion1_r_knee"
HAnimJoint143.center = [-7.62,-44.449999,0]
HAnimJoint143.llimit = [0,0,0]
HAnimJoint143.ulimit = [0,0,0]
#BVH JOINT RightKnee, OFFSET 0.0 -44.449999 0.0, CHANNELS 3 Zrotation Xrotation Yrotation
HAnimSegment144 = x3d.HAnimSegment()
HAnimSegment144.name = "r_calf"
HAnimSegment144.DEF = "BvhConversion1_r_calf"
#<HAnimJoint name='r_knee'/> visualization sphere is placed within <HAnimSegment name='r_calf'/>
TouchSensor145 = x3d.TouchSensor()
TouchSensor145.description = "HAnimJoint r_knee, HAnimSegment r_calf"

HAnimSegment144.children.append(TouchSensor145)
Transform146 = x3d.Transform()
Transform146.translation = [-7.62,-44.449999,0]
Shape147 = x3d.Shape()
Shape147.USE = "HAnimJointShape"

Transform146.children.append(Shape147)

HAnimSegment144.children.append(Transform146)
#Transform to establish local-origin reference frame at center of current Joint
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_knee'/> to <HAnimJoint name='r_talocrural'/>
Shape148 = x3d.Shape()
LineSet149 = x3d.LineSet()
LineSet149.vertexCount = [2]
Coordinate150 = x3d.Coordinate()

LineSet149.coord = Coordinate150
ColorRGBA151 = x3d.ColorRGBA()
ColorRGBA151.USE = "HAnimSegmentLineColorRGBA"

LineSet149.color = ColorRGBA151

Shape148.geometry = LineSet149

HAnimSegment144.children.append(Shape148)

HAnimJoint143.children.append(HAnimSegment144)
HAnimJoint152 = x3d.HAnimJoint()
HAnimJoint152.name = "r_talocrural"
HAnimJoint152.DEF = "BvhConversion1_r_talocrural"
HAnimJoint152.center = [-7.62,-83.819998,0]
HAnimJoint152.llimit = [0,0,0]
HAnimJoint152.ulimit = [0,0,0]
#BVH JOINT RightAnkle, OFFSET 0.0 -39.369999 0.0, CHANNELS 3 Zrotation Xrotation Yrotation
HAnimSegment153 = x3d.HAnimSegment()
HAnimSegment153.name = "r_talus"
HAnimSegment153.DEF = "BvhConversion1_r_talus"
#<HAnimJoint name='r_talocrural'/> visualization sphere is placed within <HAnimSegment name='r_talus'/>
TouchSensor154 = x3d.TouchSensor()
TouchSensor154.description = "HAnimJoint r_talocrural, HAnimSegment r_talus"

HAnimSegment153.children.append(TouchSensor154)
Transform155 = x3d.Transform()
Transform155.translation = [-7.62,-83.819998,0]
Shape156 = x3d.Shape()
Shape156.USE = "HAnimJointShape"

Transform155.children.append(Shape156)

HAnimSegment153.children.append(Transform155)
#Transform to establish local-origin reference frame at center of current Joint
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_talocrural'/> to <HAnimJoint name='r_metatarsophalangeal_2'/>
Shape157 = x3d.Shape()
LineSet158 = x3d.LineSet()
LineSet158.vertexCount = [2]
Coordinate159 = x3d.Coordinate()

LineSet158.coord = Coordinate159
ColorRGBA160 = x3d.ColorRGBA()
ColorRGBA160.USE = "HAnimSegmentLineColorRGBA"

LineSet158.color = ColorRGBA160

Shape157.geometry = LineSet158

HAnimSegment153.children.append(Shape157)

HAnimJoint152.children.append(HAnimSegment153)
HAnimJoint161 = x3d.HAnimJoint()
HAnimJoint161.name = "r_metatarsophalangeal_2"
HAnimJoint161.DEF = "BvhConversion1_r_metatarsophalangeal_2"
HAnimJoint161.center = [-7.62,-92.709998,-3.81]
HAnimJoint161.llimit = [0,0,0]
HAnimJoint161.ulimit = [0,0,0]
#BVH JOINT RightAnkleEnd, OFFSET 0.0 -8.89 -3.81, CHANNELS 3 Zrotation Xrotation Yrotation
HAnimSegment162 = x3d.HAnimSegment()
HAnimSegment162.name = "r_tarsal_proximal_phalanx_2"
HAnimSegment162.DEF = "BvhConversion1_r_tarsal_proximal_phalanx_2"
#<HAnimJoint name='r_metatarsophalangeal_2'/> visualization sphere is placed within <HAnimSegment name='r_tarsal_proximal_phalanx_2'/>
TouchSensor163 = x3d.TouchSensor()
TouchSensor163.description = "HAnimJoint r_metatarsophalangeal_2, HAnimSegment r_tarsal_proximal_phalanx_2"

HAnimSegment162.children.append(TouchSensor163)
Transform164 = x3d.Transform()
Transform164.translation = [-7.62,-92.709998,-3.81]
Shape165 = x3d.Shape()
Shape165.USE = "HAnimJointShape"

Transform164.children.append(Shape165)

HAnimSegment162.children.append(Transform164)
#Transform to establish local-origin reference frame at center of current Joint

HAnimJoint161.children.append(HAnimSegment162)

HAnimJoint152.children.append(HAnimJoint161)

HAnimJoint143.children.append(HAnimJoint152)

HAnimJoint134.children.append(HAnimJoint143)

HAnimJoint82.children.append(HAnimJoint134)
HAnimJoint166 = x3d.HAnimJoint()
HAnimJoint166.name = "vl5"
HAnimJoint166.DEF = "BvhConversion1_vl5"
HAnimJoint166.center = [0,7.62,-2.54]
HAnimJoint166.llimit = [0,0,0]
HAnimJoint166.ulimit = [0,0,0]
#BVH JOINT Chest, OFFSET 0.0 7.62 -2.54, CHANNELS 3 Zrotation Xrotation Yrotation
HAnimSegment167 = x3d.HAnimSegment()
HAnimSegment167.name = "l5"
HAnimSegment167.DEF = "BvhConversion1_l5"
#<HAnimJoint name='vl5'/> visualization sphere is placed within <HAnimSegment name='l5'/>
TouchSensor168 = x3d.TouchSensor()
TouchSensor168.description = "HAnimJoint vl5, HAnimSegment l5"

HAnimSegment167.children.append(TouchSensor168)
Transform169 = x3d.Transform()
Transform169.translation = [0,7.62,-2.54]
Shape170 = x3d.Shape()
Shape170.USE = "HAnimJointShape"

Transform169.children.append(Shape170)

HAnimSegment167.children.append(Transform169)
#Transform to establish local-origin reference frame at center of current Joint
#HAnimSegment visualization line segment from parent <HAnimJoint name='vl5'/> to <HAnimJoint name='Chest2'/>
Shape171 = x3d.Shape()
LineSet172 = x3d.LineSet()
LineSet172.vertexCount = [2]
Coordinate173 = x3d.Coordinate()

LineSet172.coord = Coordinate173
ColorRGBA174 = x3d.ColorRGBA()
ColorRGBA174.USE = "HAnimSegmentLineColorRGBA"

LineSet172.color = ColorRGBA174

Shape171.geometry = LineSet172

HAnimSegment167.children.append(Shape171)

HAnimJoint166.children.append(HAnimSegment167)
HAnimJoint175 = x3d.HAnimJoint()
HAnimJoint175.name = "Chest2"
HAnimJoint175.DEF = "BvhConversion1_Chest2"
HAnimJoint175.center = [0,15.24,-2.54]
HAnimJoint175.llimit = [0,0,0]
HAnimJoint175.ulimit = [0,0,0]
#BVH JOINT Chest2, OFFSET 0.0 7.62 0.0, CHANNELS 3 Zrotation Xrotation Yrotation
HAnimSegment176 = x3d.HAnimSegment()
HAnimSegment176.name = "vl5_to_Chest2"
HAnimSegment176.DEF = "BvhConversion1_vl5_to_Chest2"
#<HAnimJoint name='Chest2'/> visualization sphere is placed within <HAnimSegment name='vl5_to_Chest2'/>
TouchSensor177 = x3d.TouchSensor()
TouchSensor177.description = "HAnimJoint Chest2, HAnimSegment vl5_to_Chest2"

HAnimSegment176.children.append(TouchSensor177)
Transform178 = x3d.Transform()
Transform178.translation = [0,15.24,-2.54]
Shape179 = x3d.Shape()
Shape179.USE = "HAnimJointShape"

Transform178.children.append(Shape179)

HAnimSegment176.children.append(Transform178)
#Transform to establish local-origin reference frame at center of current Joint
#HAnimSegment visualization line segment from parent <HAnimJoint name='Chest2'/> to <HAnimJoint name='LeftCollar'/>
Shape180 = x3d.Shape()
LineSet181 = x3d.LineSet()
LineSet181.vertexCount = [2]
Coordinate182 = x3d.Coordinate()

LineSet181.coord = Coordinate182
ColorRGBA183 = x3d.ColorRGBA()
ColorRGBA183.USE = "HAnimSegmentLineColorRGBA"

LineSet181.color = ColorRGBA183

Shape180.geometry = LineSet181

HAnimSegment176.children.append(Shape180)
#HAnimSegment visualization line segment from parent <HAnimJoint name='Chest2'/> to <HAnimJoint name='RightCollar'/>
Shape184 = x3d.Shape()
LineSet185 = x3d.LineSet()
LineSet185.vertexCount = [2]
Coordinate186 = x3d.Coordinate()

LineSet185.coord = Coordinate186
ColorRGBA187 = x3d.ColorRGBA()
ColorRGBA187.USE = "HAnimSegmentLineColorRGBA"

LineSet185.color = ColorRGBA187

Shape184.geometry = LineSet185

HAnimSegment176.children.append(Shape184)
#HAnimSegment visualization line segment from parent <HAnimJoint name='Chest2'/> to <HAnimJoint name='Neck'/>
Shape188 = x3d.Shape()
LineSet189 = x3d.LineSet()
LineSet189.vertexCount = [2]
Coordinate190 = x3d.Coordinate()

LineSet189.coord = Coordinate190
ColorRGBA191 = x3d.ColorRGBA()
ColorRGBA191.USE = "HAnimSegmentLineColorRGBA"

LineSet189.color = ColorRGBA191

Shape188.geometry = LineSet189

HAnimSegment176.children.append(Shape188)

HAnimJoint175.children.append(HAnimSegment176)
HAnimJoint192 = x3d.HAnimJoint()
HAnimJoint192.name = "LeftCollar"
HAnimJoint192.DEF = "BvhConversion1_LeftCollar"
HAnimJoint192.center = [7.62,48.260000000000005,0]
HAnimJoint192.llimit = [0,0,0]
HAnimJoint192.ulimit = [0,0,0]
#BVH JOINT LeftCollar, OFFSET 7.62 33.02 2.54, CHANNELS 3 Zrotation Xrotation Yrotation
HAnimSegment193 = x3d.HAnimSegment()
HAnimSegment193.name = "Chest2_to_LeftCollar"
HAnimSegment193.DEF = "BvhConversion1_Chest2_to_LeftCollar"
#<HAnimJoint name='LeftCollar'/> visualization sphere is placed within <HAnimSegment name='Chest2_to_LeftCollar'/>
TouchSensor194 = x3d.TouchSensor()
TouchSensor194.description = "HAnimJoint LeftCollar, HAnimSegment Chest2_to_LeftCollar"

HAnimSegment193.children.append(TouchSensor194)
Transform195 = x3d.Transform()
Transform195.translation = [7.62,48.260000000000005,0]
Shape196 = x3d.Shape()
Shape196.USE = "HAnimJointShape"

Transform195.children.append(Shape196)

HAnimSegment193.children.append(Transform195)
#Transform to establish local-origin reference frame at center of current Joint
#HAnimSegment visualization line segment from parent <HAnimJoint name='LeftCollar'/> to <HAnimJoint name='l_shoulder'/>
Shape197 = x3d.Shape()
LineSet198 = x3d.LineSet()
LineSet198.vertexCount = [2]
Coordinate199 = x3d.Coordinate()

LineSet198.coord = Coordinate199
ColorRGBA200 = x3d.ColorRGBA()
ColorRGBA200.USE = "HAnimSegmentLineColorRGBA"

LineSet198.color = ColorRGBA200

Shape197.geometry = LineSet198

HAnimSegment193.children.append(Shape197)

HAnimJoint192.children.append(HAnimSegment193)
HAnimJoint201 = x3d.HAnimJoint()
HAnimJoint201.name = "l_shoulder"
HAnimJoint201.DEF = "BvhConversion1_l_shoulder"
HAnimJoint201.center = [20.32,48.260000000000005,0]
HAnimJoint201.llimit = [0,0,0]
HAnimJoint201.ulimit = [0,0,0]
#BVH JOINT LeftShoulder, OFFSET 12.7 0.0 0.0, CHANNELS 3 Zrotation Xrotation Yrotation
HAnimSegment202 = x3d.HAnimSegment()
HAnimSegment202.name = "l_upperarm"
HAnimSegment202.DEF = "BvhConversion1_l_upperarm"
#<HAnimJoint name='l_shoulder'/> visualization sphere is placed within <HAnimSegment name='l_upperarm'/>
TouchSensor203 = x3d.TouchSensor()
TouchSensor203.description = "HAnimJoint l_shoulder, HAnimSegment l_upperarm"

HAnimSegment202.children.append(TouchSensor203)
Transform204 = x3d.Transform()
Transform204.translation = [20.32,48.260000000000005,0]
Shape205 = x3d.Shape()
Shape205.USE = "HAnimJointShape"

Transform204.children.append(Shape205)

HAnimSegment202.children.append(Transform204)
#Transform to establish local-origin reference frame at center of current Joint
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_shoulder'/> to <HAnimJoint name='l_elbow'/>
Shape206 = x3d.Shape()
LineSet207 = x3d.LineSet()
LineSet207.vertexCount = [2]
Coordinate208 = x3d.Coordinate()

LineSet207.coord = Coordinate208
ColorRGBA209 = x3d.ColorRGBA()
ColorRGBA209.USE = "HAnimSegmentLineColorRGBA"

LineSet207.color = ColorRGBA209

Shape206.geometry = LineSet207

HAnimSegment202.children.append(Shape206)

HAnimJoint201.children.append(HAnimSegment202)
HAnimJoint210 = x3d.HAnimJoint()
HAnimJoint210.name = "l_elbow"
HAnimJoint210.DEF = "BvhConversion1_l_elbow"
HAnimJoint210.center = [20.32,17.780000000000005,0]
HAnimJoint210.llimit = [0,0,0]
HAnimJoint210.ulimit = [0,0,0]
#BVH JOINT LeftElbow, OFFSET 0.0 -30.48 0.0, CHANNELS 3 Zrotation Xrotation Yrotation
HAnimSegment211 = x3d.HAnimSegment()
HAnimSegment211.name = "l_forearm"
HAnimSegment211.DEF = "BvhConversion1_l_forearm"
#<HAnimJoint name='l_elbow'/> visualization sphere is placed within <HAnimSegment name='l_forearm'/>
TouchSensor212 = x3d.TouchSensor()
TouchSensor212.description = "HAnimJoint l_elbow, HAnimSegment l_forearm"

HAnimSegment211.children.append(TouchSensor212)
Transform213 = x3d.Transform()
Transform213.translation = [20.32,17.780000000000005,0]
Shape214 = x3d.Shape()
Shape214.USE = "HAnimJointShape"

Transform213.children.append(Shape214)

HAnimSegment211.children.append(Transform213)
#Transform to establish local-origin reference frame at center of current Joint
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_elbow'/> to <HAnimJoint name='l_radiocarpal'/>
Shape215 = x3d.Shape()
LineSet216 = x3d.LineSet()
LineSet216.vertexCount = [2]
Coordinate217 = x3d.Coordinate()

LineSet216.coord = Coordinate217
ColorRGBA218 = x3d.ColorRGBA()
ColorRGBA218.USE = "HAnimSegmentLineColorRGBA"

LineSet216.color = ColorRGBA218

Shape215.geometry = LineSet216

HAnimSegment211.children.append(Shape215)

HAnimJoint210.children.append(HAnimSegment211)
HAnimJoint219 = x3d.HAnimJoint()
HAnimJoint219.name = "l_radiocarpal"
HAnimJoint219.DEF = "BvhConversion1_l_radiocarpal"
HAnimJoint219.center = [20.32,-6.349999999999994,0]
HAnimJoint219.llimit = [0,0,0]
HAnimJoint219.ulimit = [0,0,0]
#BVH JOINT LeftWrist, OFFSET 0.0 -24.13 0.0, CHANNELS 3 Zrotation Xrotation Yrotation
HAnimSegment220 = x3d.HAnimSegment()
HAnimSegment220.name = "l_carpal"
HAnimSegment220.DEF = "BvhConversion1_l_carpal"
#<HAnimJoint name='l_radiocarpal'/> visualization sphere is placed within <HAnimSegment name='l_carpal'/>
TouchSensor221 = x3d.TouchSensor()
TouchSensor221.description = "HAnimJoint l_radiocarpal, HAnimSegment l_carpal"

HAnimSegment220.children.append(TouchSensor221)
Transform222 = x3d.Transform()
Transform222.translation = [20.32,-6.349999999999994,0]
Shape223 = x3d.Shape()
Shape223.USE = "HAnimJointShape"

Transform222.children.append(Shape223)

HAnimSegment220.children.append(Transform222)
#Transform to establish local-origin reference frame at center of current Joint

HAnimJoint219.children.append(HAnimSegment220)

HAnimJoint210.children.append(HAnimJoint219)

HAnimJoint201.children.append(HAnimJoint210)

HAnimJoint192.children.append(HAnimJoint201)

HAnimJoint175.children.append(HAnimJoint192)
HAnimJoint224 = x3d.HAnimJoint()
HAnimJoint224.name = "RightCollar"
HAnimJoint224.DEF = "BvhConversion1_RightCollar"
HAnimJoint224.center = [-7.62,48.260000000000005,0]
HAnimJoint224.llimit = [0,0,0]
HAnimJoint224.ulimit = [0,0,0]
#BVH JOINT RightCollar, OFFSET -7.62 33.02 2.54, CHANNELS 3 Zrotation Xrotation Yrotation
HAnimSegment225 = x3d.HAnimSegment()
HAnimSegment225.name = "Chest2_to_RightCollar"
HAnimSegment225.DEF = "BvhConversion1_Chest2_to_RightCollar"
#<HAnimJoint name='RightCollar'/> visualization sphere is placed within <HAnimSegment name='Chest2_to_RightCollar'/>
TouchSensor226 = x3d.TouchSensor()
TouchSensor226.description = "HAnimJoint RightCollar, HAnimSegment Chest2_to_RightCollar"

HAnimSegment225.children.append(TouchSensor226)
Transform227 = x3d.Transform()
Transform227.translation = [-7.62,48.260000000000005,0]
Shape228 = x3d.Shape()
Shape228.USE = "HAnimJointShape"

Transform227.children.append(Shape228)

HAnimSegment225.children.append(Transform227)
#Transform to establish local-origin reference frame at center of current Joint
#HAnimSegment visualization line segment from parent <HAnimJoint name='RightCollar'/> to <HAnimJoint name='r_shoulder'/>
Shape229 = x3d.Shape()
LineSet230 = x3d.LineSet()
LineSet230.vertexCount = [2]
Coordinate231 = x3d.Coordinate()

LineSet230.coord = Coordinate231
ColorRGBA232 = x3d.ColorRGBA()
ColorRGBA232.USE = "HAnimSegmentLineColorRGBA"

LineSet230.color = ColorRGBA232

Shape229.geometry = LineSet230

HAnimSegment225.children.append(Shape229)

HAnimJoint224.children.append(HAnimSegment225)
HAnimJoint233 = x3d.HAnimJoint()
HAnimJoint233.name = "r_shoulder"
HAnimJoint233.DEF = "BvhConversion1_r_shoulder"
HAnimJoint233.center = [-20.32,48.260000000000005,0]
HAnimJoint233.llimit = [0,0,0]
HAnimJoint233.ulimit = [0,0,0]
#BVH JOINT RightShoulder, OFFSET -12.7 0.0 0.0, CHANNELS 3 Zrotation Xrotation Yrotation
HAnimSegment234 = x3d.HAnimSegment()
HAnimSegment234.name = "r_upperarm"
HAnimSegment234.DEF = "BvhConversion1_r_upperarm"
#<HAnimJoint name='r_shoulder'/> visualization sphere is placed within <HAnimSegment name='r_upperarm'/>
TouchSensor235 = x3d.TouchSensor()
TouchSensor235.description = "HAnimJoint r_shoulder, HAnimSegment r_upperarm"

HAnimSegment234.children.append(TouchSensor235)
Transform236 = x3d.Transform()
Transform236.translation = [-20.32,48.260000000000005,0]
Shape237 = x3d.Shape()
Shape237.USE = "HAnimJointShape"

Transform236.children.append(Shape237)

HAnimSegment234.children.append(Transform236)
#Transform to establish local-origin reference frame at center of current Joint
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_shoulder'/> to <HAnimJoint name='r_elbow'/>
Shape238 = x3d.Shape()
LineSet239 = x3d.LineSet()
LineSet239.vertexCount = [2]
Coordinate240 = x3d.Coordinate()

LineSet239.coord = Coordinate240
ColorRGBA241 = x3d.ColorRGBA()
ColorRGBA241.USE = "HAnimSegmentLineColorRGBA"

LineSet239.color = ColorRGBA241

Shape238.geometry = LineSet239

HAnimSegment234.children.append(Shape238)

HAnimJoint233.children.append(HAnimSegment234)
HAnimJoint242 = x3d.HAnimJoint()
HAnimJoint242.name = "r_elbow"
HAnimJoint242.DEF = "BvhConversion1_r_elbow"
HAnimJoint242.center = [-20.32,17.780000000000005,0]
HAnimJoint242.llimit = [0,0,0]
HAnimJoint242.ulimit = [0,0,0]
#BVH JOINT RightElbow, OFFSET 0.0 -30.48 0.0, CHANNELS 3 Zrotation Xrotation Yrotation
HAnimSegment243 = x3d.HAnimSegment()
HAnimSegment243.name = "r_forearm"
HAnimSegment243.DEF = "BvhConversion1_r_forearm"
#<HAnimJoint name='r_elbow'/> visualization sphere is placed within <HAnimSegment name='r_forearm'/>
TouchSensor244 = x3d.TouchSensor()
TouchSensor244.description = "HAnimJoint r_elbow, HAnimSegment r_forearm"

HAnimSegment243.children.append(TouchSensor244)
Transform245 = x3d.Transform()
Transform245.translation = [-20.32,17.780000000000005,0]
Shape246 = x3d.Shape()
Shape246.USE = "HAnimJointShape"

Transform245.children.append(Shape246)

HAnimSegment243.children.append(Transform245)
#Transform to establish local-origin reference frame at center of current Joint
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_elbow'/> to <HAnimJoint name='r_radiocarpal'/>
Shape247 = x3d.Shape()
LineSet248 = x3d.LineSet()
LineSet248.vertexCount = [2]
Coordinate249 = x3d.Coordinate()

LineSet248.coord = Coordinate249
ColorRGBA250 = x3d.ColorRGBA()
ColorRGBA250.USE = "HAnimSegmentLineColorRGBA"

LineSet248.color = ColorRGBA250

Shape247.geometry = LineSet248

HAnimSegment243.children.append(Shape247)

HAnimJoint242.children.append(HAnimSegment243)
HAnimJoint251 = x3d.HAnimJoint()
HAnimJoint251.name = "r_radiocarpal"
HAnimJoint251.DEF = "BvhConversion1_r_radiocarpal"
HAnimJoint251.center = [-20.32,-6.349999999999994,0]
HAnimJoint251.llimit = [0,0,0]
HAnimJoint251.ulimit = [0,0,0]
#BVH JOINT RightWrist, OFFSET 0.0 -24.13 0.0, CHANNELS 3 Zrotation Xrotation Yrotation
HAnimSegment252 = x3d.HAnimSegment()
HAnimSegment252.name = "r_carpal"
HAnimSegment252.DEF = "BvhConversion1_r_carpal"
#<HAnimJoint name='r_radiocarpal'/> visualization sphere is placed within <HAnimSegment name='r_carpal'/>
TouchSensor253 = x3d.TouchSensor()
TouchSensor253.description = "HAnimJoint r_radiocarpal, HAnimSegment r_carpal"

HAnimSegment252.children.append(TouchSensor253)
Transform254 = x3d.Transform()
Transform254.translation = [-20.32,-6.349999999999994,0]
Shape255 = x3d.Shape()
Shape255.USE = "HAnimJointShape"

Transform254.children.append(Shape255)

HAnimSegment252.children.append(Transform254)
#Transform to establish local-origin reference frame at center of current Joint

HAnimJoint251.children.append(HAnimSegment252)

HAnimJoint242.children.append(HAnimJoint251)

HAnimJoint233.children.append(HAnimJoint242)

HAnimJoint224.children.append(HAnimJoint233)

HAnimJoint175.children.append(HAnimJoint224)
HAnimJoint256 = x3d.HAnimJoint()
HAnimJoint256.name = "Neck"
HAnimJoint256.DEF = "BvhConversion1_Neck"
HAnimJoint256.center = [0,53.339999,0]
HAnimJoint256.llimit = [0,0,0]
HAnimJoint256.ulimit = [0,0,0]
#BVH JOINT Neck, OFFSET 0.0 38.099999 2.54, CHANNELS 3 Zrotation Xrotation Yrotation
HAnimSegment257 = x3d.HAnimSegment()
HAnimSegment257.name = "Chest2_to_Neck"
HAnimSegment257.DEF = "BvhConversion1_Chest2_to_Neck"
#<HAnimJoint name='Neck'/> visualization sphere is placed within <HAnimSegment name='Chest2_to_Neck'/>
TouchSensor258 = x3d.TouchSensor()
TouchSensor258.description = "HAnimJoint Neck, HAnimSegment Chest2_to_Neck"

HAnimSegment257.children.append(TouchSensor258)
Transform259 = x3d.Transform()
Transform259.translation = [0,53.339999,0]
Shape260 = x3d.Shape()
Shape260.USE = "HAnimJointShape"

Transform259.children.append(Shape260)

HAnimSegment257.children.append(Transform259)
#Transform to establish local-origin reference frame at center of current Joint
#HAnimSegment visualization line segment from parent <HAnimJoint name='Neck'/> to <HAnimJoint name='skullbase'/>
Shape261 = x3d.Shape()
LineSet262 = x3d.LineSet()
LineSet262.vertexCount = [2]
Coordinate263 = x3d.Coordinate()

LineSet262.coord = Coordinate263
ColorRGBA264 = x3d.ColorRGBA()
ColorRGBA264.USE = "HAnimSegmentLineColorRGBA"

LineSet262.color = ColorRGBA264

Shape261.geometry = LineSet262

HAnimSegment257.children.append(Shape261)

HAnimJoint256.children.append(HAnimSegment257)
HAnimJoint265 = x3d.HAnimJoint()
HAnimJoint265.name = "skullbase"
HAnimJoint265.DEF = "BvhConversion1_skullbase"
HAnimJoint265.center = [0,69.849999,0]
HAnimJoint265.llimit = [0,0,0]
HAnimJoint265.ulimit = [0,0,0]
#BVH JOINT Head, OFFSET 0.0 16.51 0.0, CHANNELS 3 Zrotation Xrotation Yrotation
HAnimSegment266 = x3d.HAnimSegment()
HAnimSegment266.name = "skull"
HAnimSegment266.DEF = "BvhConversion1_skull"
#<HAnimJoint name='skullbase'/> visualization sphere is placed within <HAnimSegment name='skull'/>
TouchSensor267 = x3d.TouchSensor()
TouchSensor267.description = "HAnimJoint skullbase, HAnimSegment skull"

HAnimSegment266.children.append(TouchSensor267)
Transform268 = x3d.Transform()
Transform268.translation = [0,69.849999,0]
Shape269 = x3d.Shape()
Shape269.USE = "HAnimJointShape"

Transform268.children.append(Shape269)

HAnimSegment266.children.append(Transform268)
#Transform to establish local-origin reference frame at center of current Joint

HAnimJoint265.children.append(HAnimSegment266)

HAnimJoint256.children.append(HAnimJoint265)

HAnimJoint175.children.append(HAnimJoint256)

HAnimJoint166.children.append(HAnimJoint175)

HAnimJoint82.children.append(HAnimJoint166)

HAnimHumanoid63.skeleton.append(HAnimJoint82)
HAnimJoint270 = x3d.HAnimJoint()
HAnimJoint270.USE = "BvhConversion1_humanoid_root"

HAnimHumanoid63.joints.append(HAnimJoint270)
HAnimJoint271 = x3d.HAnimJoint()
HAnimJoint271.USE = "BvhConversion1_vl5"

HAnimHumanoid63.joints.append(HAnimJoint271)
HAnimJoint272 = x3d.HAnimJoint()
HAnimJoint272.USE = "BvhConversion1_Chest2"

HAnimHumanoid63.joints.append(HAnimJoint272)
HAnimJoint273 = x3d.HAnimJoint()
HAnimJoint273.USE = "BvhConversion1_LeftCollar"

HAnimHumanoid63.joints.append(HAnimJoint273)
HAnimJoint274 = x3d.HAnimJoint()
HAnimJoint274.USE = "BvhConversion1_RightCollar"

HAnimHumanoid63.joints.append(HAnimJoint274)
HAnimJoint275 = x3d.HAnimJoint()
HAnimJoint275.USE = "BvhConversion1_Neck"

HAnimHumanoid63.joints.append(HAnimJoint275)
HAnimJoint276 = x3d.HAnimJoint()
HAnimJoint276.USE = "BvhConversion1_skullbase"

HAnimHumanoid63.joints.append(HAnimJoint276)
HAnimJoint277 = x3d.HAnimJoint()
HAnimJoint277.USE = "BvhConversion1_l_talocrural"

HAnimHumanoid63.joints.append(HAnimJoint277)
HAnimJoint278 = x3d.HAnimJoint()
HAnimJoint278.USE = "BvhConversion1_r_talocrural"

HAnimHumanoid63.joints.append(HAnimJoint278)
HAnimJoint279 = x3d.HAnimJoint()
HAnimJoint279.USE = "BvhConversion1_l_elbow"

HAnimHumanoid63.joints.append(HAnimJoint279)
HAnimJoint280 = x3d.HAnimJoint()
HAnimJoint280.USE = "BvhConversion1_r_elbow"

HAnimHumanoid63.joints.append(HAnimJoint280)
HAnimJoint281 = x3d.HAnimJoint()
HAnimJoint281.USE = "BvhConversion1_l_hip"

HAnimHumanoid63.joints.append(HAnimJoint281)
HAnimJoint282 = x3d.HAnimJoint()
HAnimJoint282.USE = "BvhConversion1_r_hip"

HAnimHumanoid63.joints.append(HAnimJoint282)
HAnimJoint283 = x3d.HAnimJoint()
HAnimJoint283.USE = "BvhConversion1_l_knee"

HAnimHumanoid63.joints.append(HAnimJoint283)
HAnimJoint284 = x3d.HAnimJoint()
HAnimJoint284.USE = "BvhConversion1_r_knee"

HAnimHumanoid63.joints.append(HAnimJoint284)
HAnimJoint285 = x3d.HAnimJoint()
HAnimJoint285.USE = "BvhConversion1_l_metatarsophalangeal_2"

HAnimHumanoid63.joints.append(HAnimJoint285)
HAnimJoint286 = x3d.HAnimJoint()
HAnimJoint286.USE = "BvhConversion1_r_metatarsophalangeal_2"

HAnimHumanoid63.joints.append(HAnimJoint286)
HAnimJoint287 = x3d.HAnimJoint()
HAnimJoint287.USE = "BvhConversion1_l_shoulder"

HAnimHumanoid63.joints.append(HAnimJoint287)
HAnimJoint288 = x3d.HAnimJoint()
HAnimJoint288.USE = "BvhConversion1_r_shoulder"

HAnimHumanoid63.joints.append(HAnimJoint288)
HAnimJoint289 = x3d.HAnimJoint()
HAnimJoint289.USE = "BvhConversion1_l_radiocarpal"

HAnimHumanoid63.joints.append(HAnimJoint289)
HAnimJoint290 = x3d.HAnimJoint()
HAnimJoint290.USE = "BvhConversion1_r_radiocarpal"

HAnimHumanoid63.joints.append(HAnimJoint290)
HAnimSegment291 = x3d.HAnimSegment()
HAnimSegment291.USE = "BvhConversion1_sacrum"

HAnimHumanoid63.segments.append(HAnimSegment291)
HAnimSegment292 = x3d.HAnimSegment()
HAnimSegment292.USE = "BvhConversion1_l5"

HAnimHumanoid63.segments.append(HAnimSegment292)
HAnimSegment293 = x3d.HAnimSegment()
HAnimSegment293.USE = "BvhConversion1_vl5_to_Chest2"

HAnimHumanoid63.segments.append(HAnimSegment293)
HAnimSegment294 = x3d.HAnimSegment()
HAnimSegment294.USE = "BvhConversion1_Chest2_to_LeftCollar"

HAnimHumanoid63.segments.append(HAnimSegment294)
HAnimSegment295 = x3d.HAnimSegment()
HAnimSegment295.USE = "BvhConversion1_Chest2_to_RightCollar"

HAnimHumanoid63.segments.append(HAnimSegment295)
HAnimSegment296 = x3d.HAnimSegment()
HAnimSegment296.USE = "BvhConversion1_Chest2_to_Neck"

HAnimHumanoid63.segments.append(HAnimSegment296)
HAnimSegment297 = x3d.HAnimSegment()
HAnimSegment297.USE = "BvhConversion1_skull"

HAnimHumanoid63.segments.append(HAnimSegment297)
HAnimSegment298 = x3d.HAnimSegment()
HAnimSegment298.USE = "BvhConversion1_l_calf"

HAnimHumanoid63.segments.append(HAnimSegment298)
HAnimSegment299 = x3d.HAnimSegment()
HAnimSegment299.USE = "BvhConversion1_r_calf"

HAnimHumanoid63.segments.append(HAnimSegment299)
HAnimSegment300 = x3d.HAnimSegment()
HAnimSegment300.USE = "BvhConversion1_l_forearm"

HAnimHumanoid63.segments.append(HAnimSegment300)
HAnimSegment301 = x3d.HAnimSegment()
HAnimSegment301.USE = "BvhConversion1_r_forearm"

HAnimHumanoid63.segments.append(HAnimSegment301)
HAnimSegment302 = x3d.HAnimSegment()
HAnimSegment302.USE = "BvhConversion1_l_carpal"

HAnimHumanoid63.segments.append(HAnimSegment302)
HAnimSegment303 = x3d.HAnimSegment()
HAnimSegment303.USE = "BvhConversion1_r_carpal"

HAnimHumanoid63.segments.append(HAnimSegment303)
HAnimSegment304 = x3d.HAnimSegment()
HAnimSegment304.USE = "BvhConversion1_l_talus"

HAnimHumanoid63.segments.append(HAnimSegment304)
HAnimSegment305 = x3d.HAnimSegment()
HAnimSegment305.USE = "BvhConversion1_r_talus"

HAnimHumanoid63.segments.append(HAnimSegment305)
HAnimSegment306 = x3d.HAnimSegment()
HAnimSegment306.USE = "BvhConversion1_l_tarsal_proximal_phalanx_2"

HAnimHumanoid63.segments.append(HAnimSegment306)
HAnimSegment307 = x3d.HAnimSegment()
HAnimSegment307.USE = "BvhConversion1_r_tarsal_proximal_phalanx_2"

HAnimHumanoid63.segments.append(HAnimSegment307)
HAnimSegment308 = x3d.HAnimSegment()
HAnimSegment308.USE = "BvhConversion1_l_thigh"

HAnimHumanoid63.segments.append(HAnimSegment308)
HAnimSegment309 = x3d.HAnimSegment()
HAnimSegment309.USE = "BvhConversion1_r_thigh"

HAnimHumanoid63.segments.append(HAnimSegment309)
HAnimSegment310 = x3d.HAnimSegment()
HAnimSegment310.USE = "BvhConversion1_l_upperarm"

HAnimHumanoid63.segments.append(HAnimSegment310)
HAnimSegment311 = x3d.HAnimSegment()
HAnimSegment311.USE = "BvhConversion1_r_upperarm"

HAnimHumanoid63.segments.append(HAnimSegment311)
HAnimSite312 = x3d.HAnimSite()
HAnimSite312.USE = "BvhConversion1_humanoid_root_view"

HAnimHumanoid63.sites.append(HAnimSite312)

Scene28.children.append(HAnimHumanoid63)
#=============================================================
#testAxisAngleRotation() results compared to RotationTests.x3d
#getAxisAngleRotation(-4.40030,-0.38161,-1.82953) = (0.4067064033441406, -0.7164490591980798, -0.566825058596618, 2.6752961450535095), expected rotation: 0.40671 -0.71645 -0.56683 2.6753
#getAxisAngleRotation(5.80115,2.55377,2.83223) = (-0.9645827419506009, 0.07774106101143803, 0.2520643992393143, 2.59673649727989), expected rotation: -0.96458 0.07774 0.25206 2.59674
#getAxisAngleRotation(-3.76620,-3.47408,-3.93998) = (0.4075772844419879, -0.491492223290994, -0.7696207843161272, 1.1286216623422884), expected rotation: 0.40758 -0.49149 -0.76962 1.12862
#=============================================================
Group313 = x3d.Group()
Group313.DEF = "BvhConversion1_MotionGroup"
#BVH MOTION
#BVH Frames: 286
#BVH Frame Time: 0.016667 seconds (60.00 frames per second)
#Expected frame count: 286, actual frame count: 286, animation total duration: 4.767 seconds
#Frame width: 22 triplet values
#Total count: 66 * 286 = 18876 recorded motion values
#Animation playback: enable RealTimer for continuous motion at 60.000 frames/second (fps)
TimeSensor314 = x3d.TimeSensor()
TimeSensor314.DEF = "RealTimer"
TimeSensor314.cycleInterval = 4.767
TimeSensor314.loop = True

Group313.children.append(TimeSensor314)
#Alternative replay: enable StepTimer for discrete time-step motion at 1 fps
TimeSensor315 = x3d.TimeSensor()
TimeSensor315.DEF = "StepTimer"
TimeSensor315.cycleInterval = 286
TimeSensor315.enabled = False
TimeSensor315.loop = True

Group313.children.append(TimeSensor315)
ScalarInterpolator316 = x3d.ScalarInterpolator()
ScalarInterpolator316.DEF = "FrameStepper"
ScalarInterpolator316.key = [0,0.0035,0.0035,0.007,0.007,0.0105,0.0105,0.014,0.014,0.0175,0.0175,0.0211,0.0211,0.0246,0.0246,0.0281,0.0281,0.0316,0.0316,0.0351,0.0351,0.0386,0.0386,0.0421,0.0421,0.0456,0.0456,0.0491,0.0491,0.0526,0.0526,0.0561,0.0561,0.0596,0.0596,0.0632,0.0632,0.0667,0.0667,0.0702,0.0702,0.0737,0.0737,0.0772,0.0772,0.0807,0.0807,0.0842,0.0842,0.0877,0.0877,0.0912,0.0912,0.0947,0.0947,0.0982,0.0982,0.1018,0.1018,0.1053,0.1053,0.1088,0.1088,0.1123,0.1123,0.1158,0.1158,0.1193,0.1193,0.1228,0.1228,0.1263,0.1263,0.1298,0.1298,0.1333,0.1333,0.1368,0.1368,0.1404,0.1404,0.1439,0.1439,0.1474,0.1474,0.1509,0.1509,0.1544,0.1544,0.1579,0.1579,0.1614,0.1614,0.1649,0.1649,0.1684,0.1684,0.1719,0.1719,0.1754,0.1754,0.1789,0.1789,0.1825,0.1825,0.186,0.186,0.1895,0.1895,0.193,0.193,0.1965,0.1965,0.2,0.2,0.2035,0.2035,0.207,0.207,0.2105,0.2105,0.214,0.214,0.2175,0.2175,0.2211,0.2211,0.2246,0.2246,0.2281,0.2281,0.2316,0.2316,0.2351,0.2351,0.2386,0.2386,0.2421,0.2421,0.2456,0.2456,0.2491,0.2491,0.2526,0.2526,0.2561,0.2561,0.2596,0.2596,0.2632,0.2632,0.2667,0.2667,0.2702,0.2702,0.2737,0.2737,0.2772,0.2772,0.2807,0.2807,0.2842,0.2842,0.2877,0.2877,0.2912,0.2912,0.2947,0.2947,0.2982,0.2982,0.3018,0.3018,0.3053,0.3053,0.3088,0.3088,0.3123,0.3123,0.3158,0.3158,0.3193,0.3193,0.3228,0.3228,0.3263,0.3263,0.3298,0.3298,0.3333,0.3333,0.3368,0.3368,0.3404,0.3404,0.3439,0.3439,0.3474,0.3474,0.3509,0.3509,0.3544,0.3544,0.3579,0.3579,0.3614,0.3614,0.3649,0.3649,0.3684,0.3684,0.3719,0.3719,0.3754,0.3754,0.3789,0.3789,0.3825,0.3825,0.386,0.386,0.3895,0.3895,0.393,0.393,0.3965,0.3965,0.4,0.4,0.4035,0.4035,0.407,0.407,0.4105,0.4105,0.414,0.414,0.4175,0.4175,0.4211,0.4211,0.4246,0.4246,0.4281,0.4281,0.4316,0.4316,0.4351,0.4351,0.4386,0.4386,0.4421,0.4421,0.4456,0.4456,0.4491,0.4491,0.4526,0.4526,0.4561,0.4561,0.4596,0.4596,0.4632,0.4632,0.4667,0.4667,0.4702,0.4702,0.4737,0.4737,0.4772,0.4772,0.4807,0.4807,0.4842,0.4842,0.4877,0.4877,0.4912,0.4912,0.4947,0.4947,0.4982,0.4982,0.5018,0.5018,0.5053,0.5053,0.5088,0.5088,0.5123,0.5123,0.5158,0.5158,0.5193,0.5193,0.5228,0.5228,0.5263,0.5263,0.5298,0.5298,0.5333,0.5333,0.5368,0.5368,0.5404,0.5404,0.5439,0.5439,0.5474,0.5474,0.5509,0.5509,0.5544,0.5544,0.5579,0.5579,0.5614,0.5614,0.5649,0.5649,0.5684,0.5684,0.5719,0.5719,0.5754,0.5754,0.5789,0.5789,0.5825,0.5825,0.586,0.586,0.5895,0.5895,0.593,0.593,0.5965,0.5965,0.6,0.6,0.6035,0.6035,0.607,0.607,0.6105,0.6105,0.614,0.614,0.6175,0.6175,0.6211,0.6211,0.6246,0.6246,0.6281,0.6281,0.6316,0.6316,0.6351,0.6351,0.6386,0.6386,0.6421,0.6421,0.6456,0.6456,0.6491,0.6491,0.6526,0.6526,0.6561,0.6561,0.6596,0.6596,0.6632,0.6632,0.6667,0.6667,0.6702,0.6702,0.6737,0.6737,0.6772,0.6772,0.6807,0.6807,0.6842,0.6842,0.6877,0.6877,0.6912,0.6912,0.6947,0.6947,0.6982,0.6982,0.7018,0.7018,0.7053,0.7053,0.7088,0.7088,0.7123,0.7123,0.7158,0.7158,0.7193,0.7193,0.7228,0.7228,0.7263,0.7263,0.7298,0.7298,0.7333,0.7333,0.7368,0.7368,0.7404,0.7404,0.7439,0.7439,0.7474,0.7474,0.7509,0.7509,0.7544,0.7544,0.7579,0.7579,0.7614,0.7614,0.7649,0.7649,0.7684,0.7684,0.7719,0.7719,0.7754,0.7754,0.7789,0.7789,0.7825,0.7825,0.786,0.786,0.7895,0.7895,0.793,0.793,0.7965,0.7965,0.8,0.8,0.8035,0.8035,0.807,0.807,0.8105,0.8105,0.814,0.814,0.8175,0.8175,0.8211,0.8211,0.8246,0.8246,0.8281,0.8281,0.8316,0.8316,0.8351,0.8351,0.8386,0.8386,0.8421,0.8421,0.8456,0.8456,0.8491,0.8491,0.8526,0.8526,0.8561,0.8561,0.8596,0.8596,0.8632,0.8632,0.8667,0.8667,0.8702,0.8702,0.8737,0.8737,0.8772,0.8772,0.8807,0.8807,0.8842,0.8842,0.8877,0.8877,0.8912,0.8912,0.8947,0.8947,0.8982,0.8982,0.9018,0.9018,0.9053,0.9053,0.9088,0.9088,0.9123,0.9123,0.9158,0.9158,0.9193,0.9193,0.9228,0.9228,0.9263,0.9263,0.9298,0.9298,0.9333,0.9333,0.9368,0.9368,0.9404,0.9404,0.9439,0.9439,0.9474,0.9474,0.9509,0.9509,0.9544,0.9544,0.9579,0.9579,0.9614,0.9614,0.9649,0.9649,0.9684,0.9684,0.9719,0.9719,0.9754,0.9754,0.9789,0.9789,0.9825,0.9825,0.986,0.986,0.9895,0.9895,0.993,0.993,0.9965,0.9965,1,1]
ScalarInterpolator316.keyValue = [0,0,0.0035,0.0035,0.007,0.007,0.0105,0.0105,0.014,0.014,0.0175,0.0175,0.0211,0.0211,0.0246,0.0246,0.0281,0.0281,0.0316,0.0316,0.0351,0.0351,0.0386,0.0386,0.0421,0.0421,0.0456,0.0456,0.0491,0.0491,0.0526,0.0526,0.0561,0.0561,0.0596,0.0596,0.0632,0.0632,0.0667,0.0667,0.0702,0.0702,0.0737,0.0737,0.0772,0.0772,0.0807,0.0807,0.0842,0.0842,0.0877,0.0877,0.0912,0.0912,0.0947,0.0947,0.0982,0.0982,0.1018,0.1018,0.1053,0.1053,0.1088,0.1088,0.1123,0.1123,0.1158,0.1158,0.1193,0.1193,0.1228,0.1228,0.1263,0.1263,0.1298,0.1298,0.1333,0.1333,0.1368,0.1368,0.1404,0.1404,0.1439,0.1439,0.1474,0.1474,0.1509,0.1509,0.1544,0.1544,0.1579,0.1579,0.1614,0.1614,0.1649,0.1649,0.1684,0.1684,0.1719,0.1719,0.1754,0.1754,0.1789,0.1789,0.1825,0.1825,0.186,0.186,0.1895,0.1895,0.193,0.193,0.1965,0.1965,0.2,0.2,0.2035,0.2035,0.207,0.207,0.2105,0.2105,0.214,0.214,0.2175,0.2175,0.2211,0.2211,0.2246,0.2246,0.2281,0.2281,0.2316,0.2316,0.2351,0.2351,0.2386,0.2386,0.2421,0.2421,0.2456,0.2456,0.2491,0.2491,0.2526,0.2526,0.2561,0.2561,0.2596,0.2596,0.2632,0.2632,0.2667,0.2667,0.2702,0.2702,0.2737,0.2737,0.2772,0.2772,0.2807,0.2807,0.2842,0.2842,0.2877,0.2877,0.2912,0.2912,0.2947,0.2947,0.2982,0.2982,0.3018,0.3018,0.3053,0.3053,0.3088,0.3088,0.3123,0.3123,0.3158,0.3158,0.3193,0.3193,0.3228,0.3228,0.3263,0.3263,0.3298,0.3298,0.3333,0.3333,0.3368,0.3368,0.3404,0.3404,0.3439,0.3439,0.3474,0.3474,0.3509,0.3509,0.3544,0.3544,0.3579,0.3579,0.3614,0.3614,0.3649,0.3649,0.3684,0.3684,0.3719,0.3719,0.3754,0.3754,0.3789,0.3789,0.3825,0.3825,0.386,0.386,0.3895,0.3895,0.393,0.393,0.3965,0.3965,0.4,0.4,0.4035,0.4035,0.407,0.407,0.4105,0.4105,0.414,0.414,0.4175,0.4175,0.4211,0.4211,0.4246,0.4246,0.4281,0.4281,0.4316,0.4316,0.4351,0.4351,0.4386,0.4386,0.4421,0.4421,0.4456,0.4456,0.4491,0.4491,0.4526,0.4526,0.4561,0.4561,0.4596,0.4596,0.4632,0.4632,0.4667,0.4667,0.4702,0.4702,0.4737,0.4737,0.4772,0.4772,0.4807,0.4807,0.4842,0.4842,0.4877,0.4877,0.4912,0.4912,0.4947,0.4947,0.4982,0.4982,0.5018,0.5018,0.5053,0.5053,0.5088,0.5088,0.5123,0.5123,0.5158,0.5158,0.5193,0.5193,0.5228,0.5228,0.5263,0.5263,0.5298,0.5298,0.5333,0.5333,0.5368,0.5368,0.5404,0.5404,0.5439,0.5439,0.5474,0.5474,0.5509,0.5509,0.5544,0.5544,0.5579,0.5579,0.5614,0.5614,0.5649,0.5649,0.5684,0.5684,0.5719,0.5719,0.5754,0.5754,0.5789,0.5789,0.5825,0.5825,0.586,0.586,0.5895,0.5895,0.593,0.593,0.5965,0.5965,0.6,0.6,0.6035,0.6035,0.607,0.607,0.6105,0.6105,0.614,0.614,0.6175,0.6175,0.6211,0.6211,0.6246,0.6246,0.6281,0.6281,0.6316,0.6316,0.6351,0.6351,0.6386,0.6386,0.6421,0.6421,0.6456,0.6456,0.6491,0.6491,0.6526,0.6526,0.6561,0.6561,0.6596,0.6596,0.6632,0.6632,0.6667,0.6667,0.6702,0.6702,0.6737,0.6737,0.6772,0.6772,0.6807,0.6807,0.6842,0.6842,0.6877,0.6877,0.6912,0.6912,0.6947,0.6947,0.6982,0.6982,0.7018,0.7018,0.7053,0.7053,0.7088,0.7088,0.7123,0.7123,0.7158,0.7158,0.7193,0.7193,0.7228,0.7228,0.7263,0.7263,0.7298,0.7298,0.7333,0.7333,0.7368,0.7368,0.7404,0.7404,0.7439,0.7439,0.7474,0.7474,0.7509,0.7509,0.7544,0.7544,0.7579,0.7579,0.7614,0.7614,0.7649,0.7649,0.7684,0.7684,0.7719,0.7719,0.7754,0.7754,0.7789,0.7789,0.7825,0.7825,0.786,0.786,0.7895,0.7895,0.793,0.793,0.7965,0.7965,0.8,0.8,0.8035,0.8035,0.807,0.807,0.8105,0.8105,0.814,0.814,0.8175,0.8175,0.8211,0.8211,0.8246,0.8246,0.8281,0.8281,0.8316,0.8316,0.8351,0.8351,0.8386,0.8386,0.8421,0.8421,0.8456,0.8456,0.8491,0.8491,0.8526,0.8526,0.8561,0.8561,0.8596,0.8596,0.8632,0.8632,0.8667,0.8667,0.8702,0.8702,0.8737,0.8737,0.8772,0.8772,0.8807,0.8807,0.8842,0.8842,0.8877,0.8877,0.8912,0.8912,0.8947,0.8947,0.8982,0.8982,0.9018,0.9018,0.9053,0.9053,0.9088,0.9088,0.9123,0.9123,0.9158,0.9158,0.9193,0.9193,0.9228,0.9228,0.9263,0.9263,0.9298,0.9298,0.9333,0.9333,0.9368,0.9368,0.9404,0.9404,0.9439,0.9439,0.9474,0.9474,0.9509,0.9509,0.9544,0.9544,0.9579,0.9579,0.9614,0.9614,0.9649,0.9649,0.9684,0.9684,0.9719,0.9719,0.9754,0.9754,0.9789,0.9789,0.9825,0.9825,0.986,0.986,0.9895,0.9895,0.993,0.993,0.9965,0.9965,1]

Group313.children.append(ScalarInterpolator316)
ROUTE317 = x3d.ROUTE()
ROUTE317.fromField = "fraction_changed"
ROUTE317.fromNode = "StepTimer"
ROUTE317.toField = "set_fraction"
ROUTE317.toNode = "FrameStepper"

Group313.children.append(ROUTE317)
#Interpolator0_humanoid_root channels [0..2] sends animation values to BVH JOINT ROOT_Hips, DEF BvhConversion1_ROOT_Hips, <HAnimJoint name=humanoid_root/>
PositionInterpolator318 = x3d.PositionInterpolator()
PositionInterpolator318.DEF = "Interpolator0_humanoid_root"
PositionInterpolator318.key = [0,0.0035,0.007,0.0105,0.014,0.0175,0.0211,0.0246,0.0281,0.0316,0.0351,0.0386,0.0421,0.0456,0.0491,0.0526,0.0561,0.0596,0.0632,0.0667,0.0702,0.0737,0.0772,0.0807,0.0842,0.0877,0.0912,0.0947,0.0982,0.1018,0.1053,0.1088,0.1123,0.1158,0.1193,0.1228,0.1263,0.1298,0.1333,0.1368,0.1404,0.1439,0.1474,0.1509,0.1544,0.1579,0.1614,0.1649,0.1684,0.1719,0.1754,0.1789,0.1825,0.186,0.1895,0.193,0.1965,0.2,0.2035,0.207,0.2105,0.214,0.2175,0.2211,0.2246,0.2281,0.2316,0.2351,0.2386,0.2421,0.2456,0.2491,0.2526,0.2561,0.2596,0.2632,0.2667,0.2702,0.2737,0.2772,0.2807,0.2842,0.2877,0.2912,0.2947,0.2982,0.3018,0.3053,0.3088,0.3123,0.3158,0.3193,0.3228,0.3263,0.3298,0.3333,0.3368,0.3404,0.3439,0.3474,0.3509,0.3544,0.3579,0.3614,0.3649,0.3684,0.3719,0.3754,0.3789,0.3825,0.386,0.3895,0.393,0.3965,0.4,0.4035,0.407,0.4105,0.414,0.4175,0.4211,0.4246,0.4281,0.4316,0.4351,0.4386,0.4421,0.4456,0.4491,0.4526,0.4561,0.4596,0.4632,0.4667,0.4702,0.4737,0.4772,0.4807,0.4842,0.4877,0.4912,0.4947,0.4982,0.5018,0.5053,0.5088,0.5123,0.5158,0.5193,0.5228,0.5263,0.5298,0.5333,0.5368,0.5404,0.5439,0.5474,0.5509,0.5544,0.5579,0.5614,0.5649,0.5684,0.5719,0.5754,0.5789,0.5825,0.586,0.5895,0.593,0.5965,0.6,0.6035,0.607,0.6105,0.614,0.6175,0.6211,0.6246,0.6281,0.6316,0.6351,0.6386,0.6421,0.6456,0.6491,0.6526,0.6561,0.6596,0.6632,0.6667,0.6702,0.6737,0.6772,0.6807,0.6842,0.6877,0.6912,0.6947,0.6982,0.7018,0.7053,0.7088,0.7123,0.7158,0.7193,0.7228,0.7263,0.7298,0.7333,0.7368,0.7404,0.7439,0.7474,0.7509,0.7544,0.7579,0.7614,0.7649,0.7684,0.7719,0.7754,0.7789,0.7825,0.786,0.7895,0.793,0.7965,0.8,0.8035,0.807,0.8105,0.814,0.8175,0.8211,0.8246,0.8281,0.8316,0.8351,0.8386,0.8421,0.8456,0.8491,0.8526,0.8561,0.8596,0.8632,0.8667,0.8702,0.8737,0.8772,0.8807,0.8842,0.8877,0.8912,0.8947,0.8982,0.9018,0.9053,0.9088,0.9123,0.9158,0.9193,0.9228,0.9263,0.9298,0.9333,0.9368,0.9404,0.9439,0.9474,0.9509,0.9544,0.9579,0.9614,0.9649,0.9684,0.9719,0.9754,0.9789,0.9825,0.986,0.9895,0.993,0.9965,1]

Group313.children.append(PositionInterpolator318)
#Position triplet values, CHANNELS Xposition Yposition Zposition Zrotation Xrotation Yrotation, with min/max ranges [1.7976931348623157E308,4.9E-324], [1.7976931348623157E308,4.9E-324], [1.7976931348623157E308,4.9E-324] degrees
#1.524644 95.397761 -0.507247, 1.524644 95.397761 -0.507247, 1.531642 95.392907 -0.455451, 1.536651 95.390310 -0.353990, 1.635970 95.393905 -0.422713, 1.613231 95.393798 -0.530394, 1.701452 95.394980 -0.705016, 1.694725 95.398042 -0.875051, 1.795072 95.393808 -0.967489, 1.911313 95.402179 -1.052076, 2.101843 95.402557 -1.090820, 2.209312 95.398333 -1.003293, 2.343692 95.406375 -0.986640, 2.541407 95.411161 -1.019877, 2.670940 95.416849 -0.996071, 2.849001 95.433108 -0.938466, 2.978657 95.442254 -0.815843, 3.103978 95.456294 -0.699048, 3.108427 95.483947 -0.577880, 3.063617 95.508510 -0.361170, 2.987453 95.525253 -0.159291, 2.963545 95.545291 0.154905, 2.882266 95.537878 0.361733, 2.795358 95.525708 0.423056, 2.736351 95.503927 0.360759, 2.679144 95.474597 0.279759, 2.688164 95.452176 0.164168, 2.726807 95.422614 0.154911, 2.749113 95.427517 0.219507, 2.748040 95.439861 0.325306, 2.801936 95.452806 0.373057, 2.915216 95.488918 0.621190, 3.068299 95.526716 0.772324, 3.326345 95.553778 1.040487, 3.522513 95.570027 1.299668, 3.664174 95.572808 1.566910, 3.794184 95.563700 1.906918, 3.912936 95.538789 2.286155, 3.997214 95.610926 2.653914, 4.086375 95.684856 3.027425, 4.126404 95.736529 3.427126, 4.229044 95.755065 3.817114, 4.324466 95.748495 4.154011, 4.685616 95.797853 4.288347, 5.025683 95.796942 4.410415, 5.385478 95.799200 4.540750, 5.727035 95.773348 4.700784, 5.975542 95.747895 4.883212, 6.094952 95.678141 5.148433, 6.236034 95.595375 5.446863, 6.390408 95.491050 5.716755, 6.537691 95.352502 6.001115, 6.765692 95.202317 6.284258, 6.955140 95.129473 6.687456, 7.076889 95.043509 7.052399, 7.278605 94.997068 7.453431, 7.431958 94.971081 7.766989, 7.607177 94.925135 8.138173, 7.857586 94.893828 8.535513, 8.080230 94.861631 9.050066, 8.325060 94.784833 9.670038, 8.607172 94.679374 10.344639, 8.942562 94.586696 11.057101, 9.283855 94.493184 11.716877, 9.713364 94.400506 12.495485, 10.169141 94.289611 13.364058, 10.624406 94.188145 14.229451, 11.111318 94.118207 15.173661, 11.681664 94.036022 16.128606, 12.302880 93.983206 17.182784, 13.006071 93.963517 18.225621, 13.788966 93.950281 19.249553, 14.805500 93.930380 20.276559, 15.911036 93.921591 21.354990, 17.041059 93.876933 22.414244, 18.130399 93.756873 23.436871, 19.222698 93.559840 24.458042, 20.325261 93.282735 25.461781, 21.036642 93.129440 26.450435, 20.928158 93.380365 27.433180, 21.001634 93.613529 28.371289, 21.021309 93.814243 29.287349, 21.086193 94.007507 30.122560, 21.133509 94.192805 30.975994, 21.103869 94.397415 31.880612, 21.123909 94.606530 32.833766, 21.151792 94.792333 33.781566, 21.173107 94.973901 34.688965, 21.201334 95.168424 35.658380, 21.162395 95.320702 36.627262, 21.139681 95.448552 37.542577, 21.115213 95.546541 38.412398, 21.135054 95.634413 39.284980, 21.117323 95.691764 40.110211, 21.107544 95.740337 40.859327, 21.117960 95.750734 41.664133, 21.206205 95.764812 42.503645, 21.243843 95.771633 43.276529, 21.395620 95.775625 44.184730, 21.586109 95.771372 45.058528, 21.734698 95.766663 46.096924, 21.891381 95.757477 47.177628, 22.107669 95.732866 48.305767, 22.261383 95.667764 49.544436, 22.544295 95.606295 50.717533, 22.850926 95.540223 51.908652, 23.175487 95.438708 53.120013, 23.367919 95.331515 54.358595, 23.673702 95.198432 55.675496, 23.999448 95.041872 57.111009, 24.351037 94.900117 58.480480, 24.688200 94.766753 59.899744, 25.122749 94.601046 61.410548, 25.520191 94.468099 62.941690, 26.100805 94.391582 64.491920, 26.738523 94.326131 66.114452, 27.447161 94.245971 67.778468, 28.380491 94.129505 69.473413, 29.321640 93.984872 71.165447, 30.265720 93.771852 72.849772, 31.229438 93.476677 74.489173, 31.881183 93.461232 75.887930, 32.271680 93.747542 76.946344, 32.625777 93.981200 77.922723, 33.056569 94.198105 78.871541, 33.513404 94.389392 79.776907, 33.977741 94.583964 80.653511, 34.392910 94.753546 81.549818, 34.744267 94.898780 82.425520, 35.083258 95.032260 83.265885, 35.420272 95.149646 84.146413, 35.800377 95.263428 85.025187, 36.184719 95.381793 85.940238, 36.626603 95.480798 86.845851, 37.013360 95.580802 87.726272, 37.368741 95.667638 88.649442, 37.746484 95.753195 89.755634, 38.083375 95.812629 90.894228, 38.461671 95.838635 92.020835, 38.789606 95.859467 93.091564, 39.078145 95.858721 94.293080, 39.389141 95.800236 95.592778, 39.676848 95.717170 96.951038, 40.022724 95.586054 98.383024, 40.480239 95.420424 99.884948, 40.912468 95.245919 101.244594, 41.466184 95.048722 102.638462, 42.153066 94.806867 104.020791, 42.932422 94.512175 105.443378, 43.702133 94.187234 106.878320, 44.565627 93.987295 108.430841, 45.541653 93.798120 110.032119, 46.694310 93.633808 111.735368, 47.923310 93.449159 113.517895, 49.333674 93.291058 115.260831, 50.857239 93.107038 116.942318, 52.586644 92.872925 118.527996, 54.302557 92.617310 120.091912, 55.976258 92.300934 121.657010, 57.625668 91.918952 123.235858, 59.263702 91.462255 124.797875, 59.840872 91.667640 126.553911, 60.018002 92.046502 128.267208, 60.227360 92.378081 129.950438, 60.411336 92.665505 131.565998, 60.602768 92.918620 133.149584, 60.775412 93.182576 134.464416, 60.970129 93.414694 135.720774, 61.192010 93.621222 136.968139, 61.367726 93.837120 138.309899, 61.539712 94.029017 139.678594, 61.665392 94.230245 141.112741, 61.755348 94.388433 142.493907, 61.827257 94.511923 143.913617, 61.893130 94.600203 145.330652, 61.954076 94.627537 146.767929, 62.027841 94.618574 148.228460, 62.081597 94.606259 149.727806, 62.199483 94.595571 151.023338, 62.272022 94.555661 152.386597, 62.448232 94.492487 153.775980, 62.621671 94.410903 155.187473, 62.767616 94.301578 156.624207, 62.960143 94.181294 158.106393, 63.194940 94.059064 159.709522, 63.524130 93.915545 161.406812, 63.760720 93.750575 163.130428, 64.103170 93.586118 164.797671, 64.460144 93.423502 166.453151, 64.911240 93.240800 168.133010, 65.404810 93.058243 169.847072, 65.990642 92.878041 171.598845, 66.639618 92.710745 173.477374, 67.292897 92.545222 175.445761, 68.100009 92.362704 177.468855, 69.042994 92.156980 179.451524, 69.987568 91.917266 181.391542, 70.920089 91.637942 183.244180, 71.693782 92.041173 184.507320, 72.391593 92.468046 185.892100, 72.950062 92.892778 187.329260, 73.512726 93.272949 188.734698, 74.044845 93.622278 190.110777, 74.538380 93.907794 191.473407, 74.998149 94.115785 192.769529, 75.465577 94.295813 194.017476, 75.854594 94.495558 194.927343, 76.236436 94.701524 195.921430, 76.540865 94.924156 196.989969, 76.824026 95.115007 198.069128, 77.060784 95.283533 199.066858, 77.157692 95.417430 200.044608, 77.179488 95.562092 201.112353, 77.314437 95.663597 202.098243, 77.494804 95.741422 203.090081, 77.631108 95.800382 204.082443, 77.830544 95.839207 204.973241, 77.950304 95.873982 205.934869, 78.138383 95.886374 206.825396, 78.416947 95.862442 207.733538, 78.776373 95.838945 208.785877, 79.143947 95.780470 209.869900, 79.643776 95.687675 211.020469, 80.219070 95.574175 212.248786, 80.837497 95.443049 213.473750, 81.456296 95.279251 214.716852, 82.090230 95.088293 215.941661, 82.697742 94.878258 217.119593, 83.319283 94.629048 218.347347, 83.984950 94.436046 219.618103, 84.714634 94.247482 220.920000, 85.395561 94.072725 222.227537, 86.079057 93.955630 223.632044, 86.901216 93.820706 225.154819, 87.796985 93.699841 226.831926, 88.858625 93.620709 228.423767, 89.997451 93.520831 229.985067, 91.245049 93.404685 231.587973, 92.569242 93.269654 233.046392, 93.851189 93.094200 234.450221, 95.116489 92.852035 235.851376, 96.396712 92.528362 237.209122, 97.657526 92.115578 238.517182, 97.858589 92.381346 240.012924, 97.976470 92.682820 241.451557, 98.080252 92.946108 242.837674, 98.192212 93.140922 244.195110, 98.309172 93.263967 245.496659, 98.430802 93.330697 246.751233, 98.545049 93.444179 247.843841, 98.715339 93.575731 248.578951, 98.894699 93.719869 249.364000, 99.048207 93.866188 250.286870, 99.159169 94.005675 251.353666, 99.271991 94.128381 252.443560, 99.383322 94.255253 253.547020, 99.560007 94.335839 254.370206, 99.737951 94.406155 255.193547, 99.764268 94.451249 256.033961, 99.785962 94.477071 256.889200, 99.803558 94.496827 257.753294, 99.867798 94.489347 258.581674, 99.958839 94.487594 259.446970, 100.081060 94.480588 260.376293, 100.230237 94.469416 261.322650, 100.405546 94.454970 262.303365, 100.550159 94.430456 263.218096, 100.763848 94.382910 264.139106, 100.957034 94.325123 265.105152, 101.108604 94.269826 266.073678, 101.267083 94.183242 267.061079, 101.521098 94.099458 268.089369, 101.757809 93.996693 269.130022, 102.035999 93.909460 270.151684, 102.347995 93.875829 271.144356, 102.636001 93.869463 272.136253, 102.917476 93.857293 273.114333, 103.263676 93.861663 274.037649, 103.721972 93.862254 274.998249, 104.259536 93.848166 276.054309, 104.867018 93.976879 277.034249, 105.140926 94.179667 277.807225, 105.410667 94.342225 278.533382, 105.667647 94.485694 279.130768, 105.919260 94.572763 279.516946, 106.171861 94.636160 279.802413
#Interpolator1_humanoid_root channels [3..5] sends animation values to BVH JOINT ROOT_Hips, DEF BvhConversion1_ROOT_Hips, <HAnimJoint name=humanoid_root/>
OrientationInterpolator319 = x3d.OrientationInterpolator()
OrientationInterpolator319.DEF = "Interpolator1_humanoid_root"
OrientationInterpolator319.key = [0,0.0035,0.007,0.0105,0.014,0.0175,0.0211,0.0246,0.0281,0.0316,0.0351,0.0386,0.0421,0.0456,0.0491,0.0526,0.0561,0.0596,0.0632,0.0667,0.0702,0.0737,0.0772,0.0807,0.0842,0.0877,0.0912,0.0947,0.0982,0.1018,0.1053,0.1088,0.1123,0.1158,0.1193,0.1228,0.1263,0.1298,0.1333,0.1368,0.1404,0.1439,0.1474,0.1509,0.1544,0.1579,0.1614,0.1649,0.1684,0.1719,0.1754,0.1789,0.1825,0.186,0.1895,0.193,0.1965,0.2,0.2035,0.207,0.2105,0.214,0.2175,0.2211,0.2246,0.2281,0.2316,0.2351,0.2386,0.2421,0.2456,0.2491,0.2526,0.2561,0.2596,0.2632,0.2667,0.2702,0.2737,0.2772,0.2807,0.2842,0.2877,0.2912,0.2947,0.2982,0.3018,0.3053,0.3088,0.3123,0.3158,0.3193,0.3228,0.3263,0.3298,0.3333,0.3368,0.3404,0.3439,0.3474,0.3509,0.3544,0.3579,0.3614,0.3649,0.3684,0.3719,0.3754,0.3789,0.3825,0.386,0.3895,0.393,0.3965,0.4,0.4035,0.407,0.4105,0.414,0.4175,0.4211,0.4246,0.4281,0.4316,0.4351,0.4386,0.4421,0.4456,0.4491,0.4526,0.4561,0.4596,0.4632,0.4667,0.4702,0.4737,0.4772,0.4807,0.4842,0.4877,0.4912,0.4947,0.4982,0.5018,0.5053,0.5088,0.5123,0.5158,0.5193,0.5228,0.5263,0.5298,0.5333,0.5368,0.5404,0.5439,0.5474,0.5509,0.5544,0.5579,0.5614,0.5649,0.5684,0.5719,0.5754,0.5789,0.5825,0.586,0.5895,0.593,0.5965,0.6,0.6035,0.607,0.6105,0.614,0.6175,0.6211,0.6246,0.6281,0.6316,0.6351,0.6386,0.6421,0.6456,0.6491,0.6526,0.6561,0.6596,0.6632,0.6667,0.6702,0.6737,0.6772,0.6807,0.6842,0.6877,0.6912,0.6947,0.6982,0.7018,0.7053,0.7088,0.7123,0.7158,0.7193,0.7228,0.7263,0.7298,0.7333,0.7368,0.7404,0.7439,0.7474,0.7509,0.7544,0.7579,0.7614,0.7649,0.7684,0.7719,0.7754,0.7789,0.7825,0.786,0.7895,0.793,0.7965,0.8,0.8035,0.807,0.8105,0.814,0.8175,0.8211,0.8246,0.8281,0.8316,0.8351,0.8386,0.8421,0.8456,0.8491,0.8526,0.8561,0.8596,0.8632,0.8667,0.8702,0.8737,0.8772,0.8807,0.8842,0.8877,0.8912,0.8947,0.8982,0.9018,0.9053,0.9088,0.9123,0.9158,0.9193,0.9228,0.9263,0.9298,0.9333,0.9368,0.9404,0.9439,0.9474,0.9509,0.9544,0.9579,0.9614,0.9649,0.9684,0.9719,0.9754,0.9789,0.9825,0.986,0.9895,0.993,0.9965,1]

Group313.children.append(OrientationInterpolator319)
#Euler angle triplet values, CHANNELS Xposition Yposition Zposition Zrotation Xrotation Yrotation, with min/max ranges [-4.411866,0.010186], [-10.242768,4.9E-324], [-4.974968,11.925271] degrees
#-1.829527 -4.400301 -0.381611, -1.829527 -4.400301 -0.381611, -1.829527 -4.400301 -0.381611, -1.829527 -4.400301 -0.381611, -1.829527 -4.400301 -0.381611, -1.788088 -4.320133 -0.425375, -1.788088 -4.320133 -0.425375, -1.788088 -4.320133 -0.425375, -1.728913 -4.276426 -0.345031, -1.669766 -4.232606 -0.264662, -1.685525 -4.145720 -0.129650, -1.652053 -4.113320 0.048212, -1.609415 -3.982305 0.263455, -1.517751 -3.905375 0.521242, -1.467091 -3.908291 0.823506, -1.456708 -3.991359 1.170824, -1.471413 -4.086321 1.614424, -1.535673 -4.127849 2.015931, -1.675475 -4.128628 2.471004, -1.826812 -3.996097 2.839420, -1.902912 -3.905024 3.154643, -2.112926 -3.819734 3.442007, -2.259367 -3.640699 3.590316, -2.367132 -3.380561 3.693366, -2.410912 -3.025221 3.657587, -2.307748 -2.596693 3.696661, -2.184056 -2.253902 3.599807, -2.041469 -2.197795 3.405301, -1.997309 -2.168679 3.097270, -2.016934 -2.150796 2.701221, -2.022475 -2.067209 2.353890, -2.194512 -1.968233 2.067374, -2.366086 -1.868372 1.781071, -2.598501 -1.762160 1.675914, -2.857023 -1.671104 1.667144, -3.080900 -1.700232 1.647672, -3.330402 -1.745331 1.723969, -3.489516 -1.866317 1.869079, -3.724264 -1.948238 2.069781, -3.907512 -2.086627 2.309540, -3.958720 -2.220398 2.574254, -3.912702 -2.228696 2.875660, -3.790715 -2.275653 3.121986, -3.800008 -2.328235 3.342237, -3.692726 -2.338173 3.462473, -3.637202 -2.293115 3.543880, -3.509365 -2.386682 3.527902, -3.381620 -2.480235 3.512142, -3.177843 -2.612885 3.442053, -3.050264 -2.706512 3.426829, -2.962620 -2.881371 3.457208, -2.778823 -2.929527 3.523834, -2.722559 -2.884000 3.605225, -2.786968 -2.979980 3.744315, -2.770202 -3.015797 3.871498, -2.834207 -3.111912 4.010355, -2.893595 -3.108783 4.191570, -2.880861 -3.244102 4.276380, -2.863720 -3.280172 4.404058, -2.926913 -3.376542 4.542418, -2.857359 -3.466013 4.709269, -2.843753 -3.601161 4.794092, -2.843753 -3.601161 4.794092, -2.787526 -3.555302 4.876284, -2.787526 -3.555302 4.876284, -2.769375 -3.388591 4.965569, -2.783012 -3.253494 4.880746, -2.852387 -3.164270 4.713966, -2.901063 -3.159456 4.411880, -2.981556 -3.185251 3.934991, -3.067171 -3.309579 3.415278, -3.097131 -3.388279 2.977283, -3.059598 -3.557727 2.705670, -3.041132 -3.642530 2.569862, -2.932659 -3.651984 2.691736, -2.824239 -3.661196 2.813556, -2.640189 -3.710383 2.881434, -2.531805 -3.719085 3.003250, -2.417602 -3.628699 3.166242, -2.264106 -3.456534 3.283660, -2.128356 -3.248565 3.273570, -2.032154 -3.121779 3.308902, -1.859576 -3.034984 3.290117, -1.743659 -2.994268 3.190140, -1.627707 -2.953763 3.090093, -1.395604 -2.873361 2.889806, -1.202800 -2.874118 2.735520, -0.970309 -2.795164 2.534762, -0.737611 -2.717040 2.333742, -0.601820 -2.765985 2.099027, -0.426459 -2.735801 1.818054, -0.339741 -2.731774 1.541740, -0.164262 -2.703094 1.260876, -0.095080 -2.667067 0.858616, 0.010186 -2.753225 0.447858, -0.019921 -2.842906 0.012374, -0.050695 -2.932342 -0.423079, -0.141199 -3.066584 -0.937309, -0.215214 -3.233839 -1.327795, -0.350017 -3.445031 -1.797627, -0.426700 -3.611152 -2.189156, -0.504572 -3.776845 -2.581229, -0.536385 -3.997451 -2.928499, -0.690760 -4.116915 -3.265727, -0.785166 -4.192702 -3.524448, -0.879977 -4.268097 -3.783478, -0.940760 -4.310611 -3.862243, -1.048757 -4.297316 -3.986858, -1.109568 -4.339586 -4.065626, -1.109568 -4.339586 -4.065626, -1.109568 -4.339586 -4.065626, -1.109568 -4.339586 -4.065626, -1.122320 -4.251632 -3.930945, -1.135275 -4.163697 -3.796252, -1.040683 -4.088952 -3.537298, -0.929185 -4.049552 -3.156774, -0.878108 -4.052577 -2.854900, -0.826985 -4.055335 -2.552895, -0.896105 -4.144703 -2.409206, -1.012853 -4.179078 -2.310513, -1.135121 -4.079315 -2.299888, -1.331787 -3.935126 -2.233524, -1.411478 -3.756261 -2.265616, -1.431557 -3.534168 -2.218302, -1.403903 -3.367791 -2.126827, -1.419258 -3.280401 -1.991948, -1.536603 -3.315573 -1.892552, -1.531100 -3.450300 -1.805181, -1.573682 -3.529463 -1.761651, -1.690803 -3.565035 -1.662490, -1.765342 -3.521446 -1.606843, -1.823401 -3.513934 -1.428172, -1.956216 -3.463367 -1.193725, -2.040265 -3.468781 -0.916128, -2.166223 -3.554380 -0.595195, -2.275035 -3.677063 -0.150523, -2.449350 -3.893910 0.435604, -2.570926 -4.166828 1.063031, -2.654828 -4.563269 1.679435, -2.849200 -5.001401 2.393433, -2.980011 -5.397781 3.189302, -2.955989 -5.720922 4.064415, -2.980344 -5.992032 4.899459, -2.889023 -6.269107 5.858841, -2.793034 -6.544525 6.818833, -2.747144 -6.768757 7.740730, -2.720510 -6.954337 8.531729, -2.614780 -7.176875 9.273687, -2.542405 -7.434660 9.844651, -2.512619 -7.664474 10.368456, -2.402983 -7.835724 10.893099, -2.373446 -7.921570 11.246732, -2.420542 -7.970830 11.647726, -2.472330 -7.972330 11.829858, -2.581027 -8.022026 11.925271, -2.694926 -8.117733 11.751631, -2.846250 -8.250303 11.407296, -3.023136 -8.249192 10.977660, -3.143356 -8.293914 10.584957, -3.263840 -8.337790 10.192293, -3.326771 -8.334619 9.886428, -3.298343 -8.199272 9.620469, -3.327093 -8.110147 9.268167, -3.255594 -8.098228 9.000278, -3.249253 -7.923811 8.601842, -3.142641 -7.827216 8.287056, -3.000608 -7.646248 7.925707, -2.892550 -7.550795 7.610201, -2.729043 -7.505020 7.333610, -2.620035 -7.410803 7.017589, -2.531775 -7.327227 6.790732, -2.420496 -7.282453 6.694836, -2.309160 -7.237870 6.598867, -2.197752 -7.193463 6.502812, -2.198766 -7.145436 6.282249, -2.145806 -7.147140 6.101692, -2.070855 -7.139194 5.830737, -2.060396 -7.272480 5.431556, -2.044901 -7.310510 5.075964, -2.089138 -7.393617 4.636014, -2.134027 -7.476377 4.195898, -2.179568 -7.558798 3.755647, -2.270955 -7.818559 3.317973, -2.282360 -8.025312 2.870398, -2.391908 -8.149839 2.345553, -2.555128 -8.222192 1.777455, -2.731162 -8.207470 1.344469, -2.854720 -8.243043 0.955119, -2.969296 -8.184175 0.605681, -3.104194 -8.133051 0.352608, -3.206620 -8.207551 0.089090, -3.268701 -8.199076 -0.216379, -3.206394 -8.286676 -0.530176, -3.010383 -8.377973 -0.813450, -2.752369 -8.429312 -1.013579, -2.474169 -8.406960 -1.157143, -2.247378 -8.333099 -1.346081, -2.020426 -8.259995 -1.535226, -1.843790 -8.135219 -1.770469, -1.687853 -7.971228 -2.130128, -1.539096 -7.674539 -2.577899, -1.388122 -7.379049 -3.026058, -1.270670 -7.298710 -3.344683, -1.267604 -7.252576 -3.567891, -1.225183 -7.172469 -3.609401, -1.273940 -7.118751 -3.656250, -1.530148 -7.013199 -3.675171, -1.834952 -6.853510 -3.740089, -2.254985 -6.727648 -3.708374, -2.553768 -6.702308 -3.684730, -2.852508 -6.677087 -3.660945, -3.039843 -6.666620 -3.510273, -3.348859 -6.556761 -3.349950, -3.590333 -6.543370 -3.022331, -3.781369 -6.586067 -2.649847, -3.943133 -6.755381 -2.292293, -4.103956 -6.925786 -1.934909, -4.254793 -7.233204 -1.493048, -4.331428 -7.585374 -1.105719, -4.311476 -7.908836 -0.714936, -4.383454 -8.261798 -0.327459, -4.338515 -8.627381 0.188131, -4.228634 -8.951911 0.789131, -4.147720 -9.148852 1.402116, -4.064705 -9.344744 2.015155, -3.961312 -9.531525 2.534343, -3.879220 -9.674967 2.926623, -3.812869 -9.683474 3.233868, -3.708647 -9.607100 3.498333, -3.697260 -9.565199 3.763205, -3.704581 -9.531253 4.120766, -3.633227 -9.588596 4.649239, -3.727131 -9.640581 5.229541, -3.894536 -9.653186 5.859632, -3.987679 -9.707486 6.440492, -4.104880 -9.720654 6.890254, -4.133226 -9.857194 7.154995, -4.242627 -9.903733 7.248058, -4.337797 -10.033408 7.204977, -4.383971 -10.159811 6.981487, -4.370337 -10.242768 6.845367, -4.317763 -10.148513 6.712233, -4.316989 -9.845343 6.720018, -4.411866 -9.671497 6.684850, -4.376048 -9.585706 6.640844, -4.376048 -9.585706 6.640844, -4.376048 -9.585706 6.640844, -4.382447 -9.534406 6.420510, -4.256351 -9.268641 6.198946, -4.129318 -9.003385 5.976985, -3.979504 -8.570233 5.846439, -3.846492 -8.212560 5.668837, -3.731894 -7.864828 5.581016, -3.712765 -7.645802 5.451993, -3.693152 -7.426872 5.323010, -3.560992 -7.163845 5.098509, -3.524129 -7.029308 4.833653, -3.374152 -6.851545 4.472998, -3.335311 -6.667322 3.987462, -3.294895 -6.483348 3.501762, -3.311835 -6.343237 2.932606, -3.426060 -6.328801 2.324237, -3.453977 -6.490132 1.748088, -3.483545 -6.651154 1.171740, -3.514741 -6.811846 0.595230, -3.487171 -6.930540 0.101290, -3.585094 -6.952864 -0.382913, -3.662472 -6.902582 -0.811213, -3.729971 -6.757144 -1.200275, -3.847547 -6.556993 -1.633167, -3.942009 -6.285167 -2.007685, -3.945343 -6.097701 -2.314166, -3.947664 -5.910049 -2.620815, -3.970932 -5.733502 -2.827471, -3.905054 -5.641560 -2.968133, -3.788904 -5.605283 -3.064509, -3.666748 -5.705165 -3.075675, -3.550683 -5.669202 -3.172033, -3.440216 -5.497645 -3.353974, -3.462000 -5.322189 -3.560606, -3.427523 -4.970641 -3.772186, -3.368148 -4.607542 -4.085361, -3.330748 -4.256041 -4.297379, -3.292059 -3.904738 -4.509504, -3.206619 -3.474988 -4.762572, -3.165136 -3.124392 -4.974968
#Interpolator2_l_hip channels [6..8] sends animation values to BVH JOINT LeftHip, DEF BvhConversion1_l_hip, <HAnimJoint name=l_hip/>
OrientationInterpolator320 = x3d.OrientationInterpolator()
OrientationInterpolator320.DEF = "Interpolator2_l_hip"
OrientationInterpolator320.key = [0,0.0035,0.007,0.0105,0.014,0.0175,0.0211,0.0246,0.0281,0.0316,0.0351,0.0386,0.0421,0.0456,0.0491,0.0526,0.0561,0.0596,0.0632,0.0667,0.0702,0.0737,0.0772,0.0807,0.0842,0.0877,0.0912,0.0947,0.0982,0.1018,0.1053,0.1088,0.1123,0.1158,0.1193,0.1228,0.1263,0.1298,0.1333,0.1368,0.1404,0.1439,0.1474,0.1509,0.1544,0.1579,0.1614,0.1649,0.1684,0.1719,0.1754,0.1789,0.1825,0.186,0.1895,0.193,0.1965,0.2,0.2035,0.207,0.2105,0.214,0.2175,0.2211,0.2246,0.2281,0.2316,0.2351,0.2386,0.2421,0.2456,0.2491,0.2526,0.2561,0.2596,0.2632,0.2667,0.2702,0.2737,0.2772,0.2807,0.2842,0.2877,0.2912,0.2947,0.2982,0.3018,0.3053,0.3088,0.3123,0.3158,0.3193,0.3228,0.3263,0.3298,0.3333,0.3368,0.3404,0.3439,0.3474,0.3509,0.3544,0.3579,0.3614,0.3649,0.3684,0.3719,0.3754,0.3789,0.3825,0.386,0.3895,0.393,0.3965,0.4,0.4035,0.407,0.4105,0.414,0.4175,0.4211,0.4246,0.4281,0.4316,0.4351,0.4386,0.4421,0.4456,0.4491,0.4526,0.4561,0.4596,0.4632,0.4667,0.4702,0.4737,0.4772,0.4807,0.4842,0.4877,0.4912,0.4947,0.4982,0.5018,0.5053,0.5088,0.5123,0.5158,0.5193,0.5228,0.5263,0.5298,0.5333,0.5368,0.5404,0.5439,0.5474,0.5509,0.5544,0.5579,0.5614,0.5649,0.5684,0.5719,0.5754,0.5789,0.5825,0.586,0.5895,0.593,0.5965,0.6,0.6035,0.607,0.6105,0.614,0.6175,0.6211,0.6246,0.6281,0.6316,0.6351,0.6386,0.6421,0.6456,0.6491,0.6526,0.6561,0.6596,0.6632,0.6667,0.6702,0.6737,0.6772,0.6807,0.6842,0.6877,0.6912,0.6947,0.6982,0.7018,0.7053,0.7088,0.7123,0.7158,0.7193,0.7228,0.7263,0.7298,0.7333,0.7368,0.7404,0.7439,0.7474,0.7509,0.7544,0.7579,0.7614,0.7649,0.7684,0.7719,0.7754,0.7789,0.7825,0.786,0.7895,0.793,0.7965,0.8,0.8035,0.807,0.8105,0.814,0.8175,0.8211,0.8246,0.8281,0.8316,0.8351,0.8386,0.8421,0.8456,0.8491,0.8526,0.8561,0.8596,0.8632,0.8667,0.8702,0.8737,0.8772,0.8807,0.8842,0.8877,0.8912,0.8947,0.8982,0.9018,0.9053,0.9088,0.9123,0.9158,0.9193,0.9228,0.9263,0.9298,0.9333,0.9368,0.9404,0.9439,0.9474,0.9509,0.9544,0.9579,0.9614,0.9649,0.9684,0.9719,0.9754,0.9789,0.9825,0.986,0.9895,0.993,0.9965,1]

Group313.children.append(OrientationInterpolator320)
#Euler angle triplet values, CHANNELS Zrotation Xrotation Yrotation, with min/max ranges [-2.07709,7.74649], [-23.242655,20.162275], [-2.82819,17.87174] degrees
#2.832229 5.801149 2.553770, 2.832229 5.801149 2.553770, 2.893268 5.869187 2.613585, 2.886478 6.000001 2.699244, 2.757954 5.911017 2.707608, 2.671466 5.700300 2.764938, 2.563605 5.546554 2.839046, 2.503336 5.395139 2.820716, 2.329124 5.211887 2.625725, 2.154138 5.029144 2.430089, 2.038072 4.867472 2.109035, 2.004529 4.847241 1.739820, 1.834637 4.641002 1.343288, 1.636777 4.423985 0.970761, 1.479116 4.333948 0.676835, 1.382096 4.387193 0.484949, 1.380085 4.562369 0.384830, 1.424597 4.683239 0.324424, 1.630335 4.756027 0.332913, 1.914505 4.823192 0.646326, 2.249224 4.935641 1.052710, 2.712964 5.176470 1.565353, 3.156771 5.269109 2.200086, 3.490622 5.175544 2.703977, 3.644308 4.934379 3.073523, 3.663468 4.532536 3.132416, 3.625192 4.224030 3.096808, 3.565495 4.356757 3.033947, 3.596890 4.516984 3.079280, 3.666362 4.754819 3.140256, 3.739552 4.861400 3.226387, 3.908872 5.054255 3.397689, 4.034752 5.117296 3.577705, 4.209808 5.269904 3.631968, 4.371542 5.431460 3.683026, 4.510505 5.697347 3.931649, 4.674832 6.015391 4.207866, 4.768012 6.474186 4.567344, 5.027681 6.757952 4.914306, 5.243429 7.094718 5.218116, 5.400640 7.452162 5.436618, 5.450805 7.615705 5.475396, 5.420737 7.827277 5.567975, 5.151124 7.796432 5.733640, 4.869335 7.759462 5.843816, 4.623693 7.687126 5.802298, 4.278740 7.847598 5.586888, 4.055679 8.029014 5.208513, 3.881389 8.347087 4.880706, 3.797085 8.686701 4.655683, 3.815585 9.210081 4.559852, 3.817612 9.684537 4.725433, 3.800367 10.010423 5.008277, 3.921535 10.484694 5.023202, 3.968370 10.863517 4.933724, 4.031518 11.291982 4.696630, 4.170718 11.417600 4.302324, 4.245632 11.631557 4.068994, 4.175780 11.789265 3.899434, 4.328813 12.067161 3.892931, 4.414634 12.410997 3.920547, 4.475957 12.870954 4.057196, 4.586023 13.132854 4.257065, 4.594031 13.283576 4.324063, 4.643834 13.481508 4.468195, 4.681195 13.528196 4.340896, 4.712275 13.617700 4.387710, 4.771180 13.814596 4.441391, 4.799826 14.069101 4.503335, 4.815863 14.292030 4.581263, 4.782811 14.398184 4.745988, 4.736263 14.262715 4.814431, 4.579834 13.863674 4.772534, 4.423285 13.129302 4.841889, 4.490148 11.993941 4.926150, 4.642351 10.621325 5.282381, 4.847876 9.122188 6.035493, 5.190194 7.483083 7.198329, 5.518437 5.651601 8.665732, 5.622439 3.661852 10.405171, 5.590827 1.420251 12.059477, 5.551896 -0.941485 13.426015, 5.449883 -3.511261 14.588489, 5.314196 -6.117500 15.630031, 5.090293 -8.600213 16.428646, 4.768567 -11.103746 17.145111, 4.385863 -13.270555 17.536860, 4.022193 -15.224087 17.812460, 3.644212 -17.029942 17.871740, 3.370986 -18.412497 17.719542, 3.142739 -19.776531 17.444628, 3.043082 -20.817665 17.128246, 2.795460 -21.758997 16.706587, 2.595528 -22.524221 16.455637, 2.386870 -22.896303 16.287270, 2.327955 -23.065458 16.096937, 2.148184 -23.242655 15.742593, 2.013536 -23.215712 15.249210, 1.828479 -23.122025 14.522050, 1.666708 -22.855043 13.759366, 1.487845 -22.553154 12.996436, 1.383245 -22.052752 12.404510, 1.349219 -21.426388 12.054583, 1.480272 -20.850464 11.858182, 1.542556 -20.371794 11.622407, 1.579255 -20.044142 11.391354, 1.299053 -19.956358 10.966695, 1.014279 -20.111464 10.422645, 0.618548 -20.020414 9.844428, 0.211559 -19.896366 9.266111, -0.130370 -19.664928 8.987178, -0.573707 -19.224682 9.000589, -1.024465 -18.575506 9.186677, -1.313609 -17.831934 9.569765, -1.659942 -17.229168 9.501938, -1.885092 -16.578993 8.675566, -2.016473 -15.970876 7.582511, -2.077090 -15.125435 6.370121, -1.991632 -14.001677 5.341220, -1.829999 -12.728888 4.796271, -1.581400 -11.612572 4.537875, -1.331816 -10.487686 4.233605, -1.211003 -9.548136 4.033661, -1.154760 -8.773225 3.667611, -1.146919 -7.944105 3.261767, -1.163624 -7.103045 2.741724, -1.068763 -6.136926 2.255621, -1.028374 -5.058967 1.729463, -1.051783 -4.120789 1.237512, -0.971978 -3.293972 0.750339, -0.917125 -2.499330 0.440429, -0.856614 -1.738582 0.073417, -0.690100 -1.041631 -0.159160, -0.615017 -0.300364 -0.346711, -0.422905 0.507765 -0.469786, -0.201424 1.385306 -0.371191, 0.096753 2.481500 -0.332834, 0.507878 3.608437 -0.103818, 0.846517 4.850883 0.219704, 1.386757 6.104817 0.528019, 1.890013 7.393109 0.708072, 2.399279 8.690373 0.803861, 2.957360 9.991704 0.857054, 3.383058 11.363266 0.813295, 3.770791 12.665697 0.701306, 4.233838 13.711538 0.595547, 4.560273 14.662127 0.440509, 4.754183 15.602407 0.283707, 5.021220 16.509916 0.254737, 5.331733 17.321573 0.337827, 5.629994 17.952202 0.464234, 5.862180 18.480577 0.838351, 6.127396 18.853811 0.985565, 6.310817 19.067993 1.279504, 6.464346 19.000109 1.428744, 6.540294 18.738163 1.678070, 6.547938 18.137476 1.944973, 6.610426 16.947029 2.239718, 6.929051 15.525990 2.573191, 7.287074 13.985853 3.054616, 7.651628 12.261320 3.801455, 7.746490 10.398503 4.782916, 7.745063 8.426219 5.986492, 7.698053 6.292410 7.081097, 7.532519 3.906659 8.382342, 7.183016 1.457888 9.590134, 6.695642 -1.144690 10.657774, 6.280996 -3.672315 11.463290, 5.764982 -6.156411 12.082637, 5.261804 -8.554473 12.435684, 4.655063 -10.765365 12.550171, 3.981673 -12.858058 12.187481, 3.293444 -14.727556 11.709354, 2.534302 -16.409212 11.080534, 1.845000 -17.881065 10.502579, 1.151728 -18.944704 9.829328, 0.566200 -19.739803 9.284315, 0.232276 -20.096167 8.802554, -0.061775 -20.198736 8.240182, -0.039521 -20.163565 7.891159, 0.092465 -19.858990 7.587718, 0.265139 -19.435440 7.057597, 0.686002 -18.805832 6.519338, 0.962674 -18.177488 6.019915, 1.389061 -17.450853 5.808390, 1.753299 -16.732788 5.706532, 2.000497 -16.139769 5.612278, 1.996072 -15.803757 5.593822, 1.837309 -15.866412 5.597595, 1.558683 -15.918087 5.352021, 1.202826 -15.711389 5.008601, 0.850277 -15.296737 4.780139, 0.341709 -14.539001 4.565547, -0.191583 -13.932732 4.175399, -0.780728 -13.533186 3.429988, -1.235455 -13.348140 2.398373, -1.462597 -13.104679 1.330924, -1.575411 -12.620260 0.563556, -1.731100 -11.781775 0.165907, -1.893373 -10.735291 0.351250, -1.893536 -9.689223 0.759807, -1.944445 -8.685539 1.011434, -1.989842 -7.593464 1.062987, -1.943539 -6.456947 1.003845, -1.966106 -5.524487 0.544196, -1.998428 -4.606179 -0.183423, -1.756662 -3.829282 -1.117947, -1.445437 -2.981599 -1.925464, -0.994383 -1.989619 -2.569871, -0.670793 -0.822153 -2.828190, -0.307093 0.371347 -2.756933, 0.060449 1.543605 -2.482729, 0.704931 2.684592 -2.048531, 1.174483 3.760175 -1.710948, 1.531036 4.819514 -1.479337, 1.855846 6.001740 -1.236497, 2.189172 7.054068 -1.084568, 2.675948 8.254451 -0.980543, 3.058443 9.260207 -0.580406, 3.298804 10.233540 -0.083824, 3.550740 11.281109 0.408696, 3.785609 12.353469 0.707212, 3.975314 13.400192 0.731661, 4.145034 14.252640 0.689339, 4.247539 15.102928 0.525763, 4.388748 15.972947 0.382671, 4.514685 16.738729 0.213828, 4.638931 17.333302 0.009449, 4.708764 17.849300 -0.139078, 4.806458 18.371044 -0.229656, 4.970265 18.828703 -0.356659, 5.204412 19.234266 -0.632217, 5.631539 19.589071 -0.796189, 6.095309 19.897947 -0.916614, 6.463166 20.162275 -0.936754, 6.677623 20.058683 -0.735518, 6.820518 19.900309 -0.465742, 6.982131 19.333364 -0.123137, 7.054181 18.417225 0.268508, 7.114507 17.063616 0.778944, 7.238667 15.335371 1.225137, 7.341827 13.178058 1.750551, 7.460561 10.756817 2.417192, 7.564530 8.299118 3.476920, 7.483237 5.932747 4.718340, 7.352686 3.487230 6.076504, 7.019080 0.948082 7.405816, 6.615777 -1.762581 8.827506, 6.037679 -4.611503 10.117277, 5.459861 -7.265746 11.214539, 4.805209 -10.020116 11.951391, 4.101614 -12.426932 12.448965, 3.458267 -14.551555 12.666535, 2.946317 -16.253349 12.670041, 2.560053 -17.649853 12.594315, 2.146204 -18.709940 12.339437, 1.907851 -19.467741 11.992743, 1.576638 -19.979761 11.649097, 1.565475 -20.275463 11.445477, 1.525808 -20.378031 11.259027, 1.602482 -20.403070 11.053254, 1.738583 -20.210068 10.541636, 1.795934 -19.751081 9.871426, 1.787890 -19.277788 8.996215, 1.764751 -18.658545 8.174740, 1.653305 -18.050352 7.502786, 1.781834 -17.426825 7.053306, 1.979575 -16.849291 6.920408, 2.125033 -16.312094 6.936576, 2.213819 -15.674872 7.160229, 2.278126 -15.024364 7.200164, 2.208691 -14.249763 6.886278, 2.055068 -13.580343 6.114401, 1.889059 -12.972301 4.862382, 1.577350 -12.486387 3.420280, 1.340714 -11.979342 1.863340, 1.139961 -11.235892 0.509811, 1.019736 -10.676725 -0.288038, 0.991014 -10.033175 -0.620850, 1.160437 -9.230432 -0.520799, 1.243653 -8.627681 -0.328339, 1.295994 -8.027895 -0.047980, 1.366214 -7.545083 0.056705, 1.396847 -7.164520 -0.122879, 1.345077 -7.058871 -0.397547, 1.270130 -7.010466 -0.739485
#Interpolator3_l_knee channels [9..11] sends animation values to BVH JOINT LeftKnee, DEF BvhConversion1_l_knee, <HAnimJoint name=l_knee/>
OrientationInterpolator321 = x3d.OrientationInterpolator()
OrientationInterpolator321.DEF = "Interpolator3_l_knee"
OrientationInterpolator321.key = [0,0.0035,0.007,0.0105,0.014,0.0175,0.0211,0.0246,0.0281,0.0316,0.0351,0.0386,0.0421,0.0456,0.0491,0.0526,0.0561,0.0596,0.0632,0.0667,0.0702,0.0737,0.0772,0.0807,0.0842,0.0877,0.0912,0.0947,0.0982,0.1018,0.1053,0.1088,0.1123,0.1158,0.1193,0.1228,0.1263,0.1298,0.1333,0.1368,0.1404,0.1439,0.1474,0.1509,0.1544,0.1579,0.1614,0.1649,0.1684,0.1719,0.1754,0.1789,0.1825,0.186,0.1895,0.193,0.1965,0.2,0.2035,0.207,0.2105,0.214,0.2175,0.2211,0.2246,0.2281,0.2316,0.2351,0.2386,0.2421,0.2456,0.2491,0.2526,0.2561,0.2596,0.2632,0.2667,0.2702,0.2737,0.2772,0.2807,0.2842,0.2877,0.2912,0.2947,0.2982,0.3018,0.3053,0.3088,0.3123,0.3158,0.3193,0.3228,0.3263,0.3298,0.3333,0.3368,0.3404,0.3439,0.3474,0.3509,0.3544,0.3579,0.3614,0.3649,0.3684,0.3719,0.3754,0.3789,0.3825,0.386,0.3895,0.393,0.3965,0.4,0.4035,0.407,0.4105,0.414,0.4175,0.4211,0.4246,0.4281,0.4316,0.4351,0.4386,0.4421,0.4456,0.4491,0.4526,0.4561,0.4596,0.4632,0.4667,0.4702,0.4737,0.4772,0.4807,0.4842,0.4877,0.4912,0.4947,0.4982,0.5018,0.5053,0.5088,0.5123,0.5158,0.5193,0.5228,0.5263,0.5298,0.5333,0.5368,0.5404,0.5439,0.5474,0.5509,0.5544,0.5579,0.5614,0.5649,0.5684,0.5719,0.5754,0.5789,0.5825,0.586,0.5895,0.593,0.5965,0.6,0.6035,0.607,0.6105,0.614,0.6175,0.6211,0.6246,0.6281,0.6316,0.6351,0.6386,0.6421,0.6456,0.6491,0.6526,0.6561,0.6596,0.6632,0.6667,0.6702,0.6737,0.6772,0.6807,0.6842,0.6877,0.6912,0.6947,0.6982,0.7018,0.7053,0.7088,0.7123,0.7158,0.7193,0.7228,0.7263,0.7298,0.7333,0.7368,0.7404,0.7439,0.7474,0.7509,0.7544,0.7579,0.7614,0.7649,0.7684,0.7719,0.7754,0.7789,0.7825,0.786,0.7895,0.793,0.7965,0.8,0.8035,0.807,0.8105,0.814,0.8175,0.8211,0.8246,0.8281,0.8316,0.8351,0.8386,0.8421,0.8456,0.8491,0.8526,0.8561,0.8596,0.8632,0.8667,0.8702,0.8737,0.8772,0.8807,0.8842,0.8877,0.8912,0.8947,0.8982,0.9018,0.9053,0.9088,0.9123,0.9158,0.9193,0.9228,0.9263,0.9298,0.9333,0.9368,0.9404,0.9439,0.9474,0.9509,0.9544,0.9579,0.9614,0.9649,0.9684,0.9719,0.9754,0.9789,0.9825,0.986,0.9895,0.993,0.9965,1]

Group313.children.append(OrientationInterpolator321)
#Euler angle triplet values, CHANNELS Zrotation Xrotation Yrotation, with min/max ranges [-34.92207,19.195293], [-6.526618,57.245258], [-17.028704,12.703618] degrees
#-3.939975 -3.766201 -3.474078, -3.939975 -3.766201 -3.474078, -4.087531 -3.824402 -3.466879, -4.093241 -3.948997 -3.561182, -3.960619 -3.866694 -3.550377, -3.834370 -3.738754 -3.621544, -3.733652 -3.667324 -3.838453, -3.589555 -3.601340 -4.046555, -3.461005 -3.476283 -4.231246, -3.332685 -3.350797 -4.416099, -3.266505 -3.290072 -4.620756, -3.331850 -3.232222 -4.834424, -3.179870 -3.090900 -5.115561, -3.134691 -2.879325 -5.384120, -3.003442 -2.709592 -5.697166, -2.981100 -2.594460 -6.091019, -3.026685 -2.662159 -6.522533, -3.069262 -2.731425 -6.791653, -3.114120 -2.800296 -6.948999, -3.249367 -2.986074 -7.172327, -3.594525 -3.161520 -7.201317, -4.032129 -3.447166 -7.411406, -4.625803 -3.725826 -7.847285, -5.088897 -3.983961 -8.491629, -5.372149 -4.290939 -8.918939, -5.630632 -4.444394 -9.088295, -5.838985 -4.620029 -9.029859, -6.027059 -4.960439 -8.716910, -6.115529 -5.148654 -8.475998, -6.099472 -5.420537 -8.085193, -6.181458 -5.613129 -7.681916, -6.189431 -5.747969 -7.267530, -6.147818 -5.755021 -6.843904, -6.255480 -5.851282 -6.498271, -6.253995 -6.034492 -6.158106, -6.269282 -6.180486 -5.850351, -6.302267 -6.361139 -5.670412, -6.354571 -6.514375 -5.490971, -6.570467 -6.517792 -5.438235, -6.789512 -6.514420 -5.548758, -7.076112 -6.526618 -5.768890, -7.408134 -6.390126 -6.067214, -7.745207 -6.324413 -6.534191, -7.691460 -6.044915 -7.136610, -7.822977 -5.769712 -7.841972, -7.927781 -5.536735 -8.354908, -7.910833 -5.437178 -8.525034, -8.001611 -5.373817 -8.387547, -8.145371 -5.328479 -8.017870, -8.307655 -5.338922 -7.658227, -8.661688 -5.578624 -7.437864, -9.277953 -5.737038 -7.540685, -9.698742 -5.924809 -7.826411, -9.999862 -6.089008 -7.994178, -10.215347 -6.237994 -8.108297, -10.422400 -6.397584 -8.174664, -10.669665 -6.291948 -8.091794, -10.996106 -6.028053 -7.992971, -11.114440 -5.739970 -7.876284, -11.451788 -5.384835 -7.900877, -11.935874 -4.984858 -7.923724, -12.334879 -4.490746 -7.964097, -12.866072 -3.907377 -8.058410, -13.250233 -3.297686 -7.980925, -13.683358 -2.508712 -7.973041, -14.109074 -1.699534 -7.766320, -14.538452 -0.891067 -7.556117, -14.963526 -0.160992 -7.286780, -15.473159 0.648736 -6.808437, -15.991401 1.655376 -6.125971, -16.447624 3.029521 -5.395289, -17.038933 4.665825 -4.491837, -17.731054 6.864288 -3.312119, -18.405849 9.472552 -2.057152, -19.537600 12.644535 -0.736564, -20.874128 16.042168 0.583533, -22.456200 19.847546 1.638013, -24.094213 23.915976 2.136521, -25.612638 28.165661 2.267411, -26.857290 32.484062 2.245345, -27.852926 36.589249 2.581597, -28.684603 40.378040 3.424374, -29.285950 43.810497 4.877421, -29.439875 46.732677 6.548551, -28.858059 49.062382 7.980522, -27.568747 50.896484 8.984966, -25.615826 52.112766 9.347354, -22.959755 52.546753 8.670194, -19.739666 52.333656 7.110879, -16.154879 51.355556 4.934896, -12.590123 49.914364 2.477232, -9.165704 47.850990 -0.204507, -5.829761 45.448902 -2.821702, -2.478240 42.722332 -5.636001, 0.668505 39.589931 -8.559116, 3.421243 36.293816 -11.095500, 5.946341 32.938625 -13.049797, 8.161756 29.437809 -14.208281, 10.127060 25.971972 -14.641338, 11.744483 22.531145 -14.220431, 13.244369 19.216454 -13.247885, 14.416320 16.009758 -11.967554, 15.565923 12.927683 -10.789451, 16.512854 10.238226 -9.828478, 17.148540 8.059446 -9.069825, 17.673113 6.668108 -8.787449, 18.202393 6.049401 -8.952033, 18.523430 6.106709 -9.189127, 18.672489 6.336034 -9.306707, 18.635103 6.692642 -9.283475, 18.458456 6.867680 -8.969679, 18.247967 6.904797 -8.558421, 17.941015 6.707598 -8.434866, 17.530581 6.453153 -8.702065, 16.869535 6.539927 -8.814102, 15.933082 6.751630 -8.424598, 14.835796 6.949809 -7.922245, 13.683020 6.902159 -7.488574, 12.537408 6.541054 -7.044241, 11.512815 5.775104 -6.944696, 10.494855 4.932518 -6.741942, 9.597046 4.051138 -6.111510, 8.769696 3.302735 -5.374659, 8.036599 2.671685 -4.520710, 7.208016 2.004367 -3.917926, 6.521704 1.402388 -3.371747, 5.826421 0.782313 -3.004404, 5.151680 0.214437 -2.676588, 4.781635 -0.277601 -2.224233, 4.315220 -0.707148 -1.763667, 3.841243 -1.201668 -1.440767, 3.258109 -1.550754 -1.275537, 2.642500 -1.814142 -1.318911, 2.071136 -2.070072 -1.458391, 1.434001 -2.313149 -1.556014, 0.751414 -2.592101 -1.848135, 0.069603 -2.905336 -2.239288, -0.780232 -3.189277 -2.887095, -1.745952 -3.519694 -3.642198, -2.699433 -3.805180 -4.438111, -3.567453 -4.077834 -5.126541, -4.718138 -4.397607 -5.694162, -5.781164 -4.773260 -6.134012, -6.787304 -5.190460 -6.622773, -7.787150 -5.356984 -7.135412, -8.788046 -5.308338 -7.619725, -9.602497 -5.056894 -7.885675, -10.416606 -4.655948 -7.997668, -11.415977 -3.987782 -8.081615, -12.382151 -2.985920 -8.195743, -13.527860 -1.635356 -8.322394, -14.570342 -0.151864 -8.462132, -15.578365 1.573353 -8.443415, -16.554119 3.637314 -8.082532, -17.547707 6.141714 -7.404226, -18.659086 8.951082 -6.481070, -19.944935 12.186837 -5.326556, -21.408230 15.832149 -4.006531, -23.359873 19.912144 -2.584796, -25.417456 24.048876 -1.238330, -27.549919 28.392221 -0.089850, -29.532516 32.672783 0.748944, -31.233725 36.807732 1.644393, -32.842697 40.794899 2.780060, -33.995316 44.425201 4.106742, -34.689724 47.764820 5.626235, -34.922070 50.579426 7.149245, -34.554394 53.025978 8.381177, -33.212452 54.976620 8.937463, -30.950056 56.288948 8.655535, -27.633541 57.025135 7.312683, -23.712614 57.245258 5.483645, -18.946463 56.897671 2.810928, -13.842920 55.981941 -0.207533, -8.623897 54.443554 -3.332947, -3.718814 52.122662 -6.514160, 0.891989 49.221615 -9.640932, 4.739643 45.741348 -12.292856, 7.799412 41.610870 -14.347097, 10.126727 37.299500 -15.947546, 12.026262 32.582626 -17.018156, 13.326240 27.836344 -17.028704, 14.227730 23.300753 -16.364185, 15.114910 18.916754 -15.185034, 16.005224 14.669018 -13.681065, 16.886806 10.990486 -11.939180, 17.673098 8.127779 -10.323455, 18.302038 6.345594 -9.318274, 18.836460 5.633483 -9.026444, 19.139187 5.603265 -8.871451, 19.195293 5.889776 -8.987277, 19.009691 5.892982 -9.175154, 18.607635 5.844045 -9.324980, 18.141371 6.322053 -9.389671, 17.422213 7.240291 -9.110630, 16.428471 8.469862 -8.506667, 15.118213 9.506368 -7.784500, 13.686287 10.126665 -7.236768, 12.387758 10.058430 -6.932853, 11.323479 9.579226 -6.680845, 10.188030 8.890215 -5.912348, 9.090088 8.266467 -4.722108, 7.958160 7.584525 -3.664634, 6.981262 6.867752 -2.832175, 6.060039 6.226485 -2.242952, 5.379089 5.635438 -1.614063, 4.650719 5.154063 -0.531760, 3.943882 4.523850 0.618039, 3.331857 3.761120 1.556167, 2.847616 2.809937 2.031168, 2.441680 1.650509 2.231561, 2.003389 0.515210 2.011342, 1.328842 -0.614924 1.827664, 0.743837 -1.580206 1.556455, 0.205530 -2.390968 1.333050, -0.258781 -3.183863 1.015578, -0.815626 -3.852218 0.850361, -1.531057 -4.448983 0.604133, -2.331881 -4.628253 0.028659, -3.171337 -4.783138 -0.726456, -3.922614 -4.799909 -1.486444, -4.809152 -4.822401 -2.119582, -5.829910 -4.778097 -2.577636, -6.770525 -4.496989 -2.962266, -7.535018 -4.217787 -3.289692, -8.358459 -3.955629 -3.567377, -9.234919 -3.629437 -3.773475, -10.033749 -3.202851 -3.756367, -10.818011 -2.696127 -3.736872, -11.533575 -2.069666 -3.760307, -12.346911 -1.279258 -3.754648, -13.215220 -0.267569 -3.761704, -14.002190 0.890158 -3.847023, -14.863503 2.240021 -4.001281, -15.633396 3.864088 -4.039954, -16.351839 5.988516 -3.903659, -17.240421 8.373788 -3.476746, -18.267332 11.282914 -2.678101, -19.286901 14.646504 -1.460235, -20.748188 18.572023 0.305994, -22.487539 22.863523 2.372995, -24.479866 27.420935 4.603004, -26.542624 31.844118 6.589016, -28.492496 36.290810 8.114017, -30.411554 40.487072 9.437781, -31.895235 44.405396 10.568786, -32.737694 47.865753 11.667150, -32.923698 50.899216 12.462738, -32.447273 53.443703 12.703618, -30.887066 55.322247 12.093710, -28.255590 56.602875 10.648288, -24.529251 57.080936 8.205296, -20.146025 56.773754 5.016072, -15.407351 55.705070 1.346170, -10.557292 53.977562 -2.665480, -6.402997 51.430992 -6.025434, -2.563802 48.323372 -9.105699, 0.843890 44.727917 -11.672470, 3.659465 40.875282 -13.782959, 6.260497 36.804825 -15.509439, 8.293514 32.929943 -16.443687, 9.877722 29.331856 -16.485388, 10.979002 26.254133 -15.619828, 11.984180 23.630465 -14.221028, 12.767410 21.333775 -12.479837, 13.453741 19.306690 -10.871564, 13.875176 17.619938 -9.544771, 13.893015 16.324497 -8.601796, 13.862700 15.160343 -8.136711, 13.876287 13.909965 -8.380249, 13.710710 12.594725 -8.844252, 13.426375 11.363462 -9.243920, 13.050978 10.517782 -9.060328, 12.613075 9.918784 -8.286085, 12.201921 9.654469 -7.034683, 11.677664 9.531848 -5.540803, 10.994650 9.251282 -4.110190, 10.348771 8.972024 -3.319894, 9.705316 8.235996 -2.851919, 9.063526 7.269543 -2.784306, 8.576174 6.326198 -2.599717, 7.953456 5.468631 -2.231707, 7.405807 4.662607 -1.756797, 6.864078 4.062303 -1.193797, 6.451123 3.574063 -0.618832, 6.175721 3.217674 -0.142123
#Interpolator4_l_ankle channels [12..14] sends animation values to BVH JOINT LeftAnkle, DEF BvhConversion1_l_ankle, <HAnimJoint name=l_ankle/>
OrientationInterpolator322 = x3d.OrientationInterpolator()
OrientationInterpolator322.DEF = "Interpolator4_l_ankle"
OrientationInterpolator322.key = [0,0.0035,0.007,0.0105,0.014,0.0175,0.0211,0.0246,0.0281,0.0316,0.0351,0.0386,0.0421,0.0456,0.0491,0.0526,0.0561,0.0596,0.0632,0.0667,0.0702,0.0737,0.0772,0.0807,0.0842,0.0877,0.0912,0.0947,0.0982,0.1018,0.1053,0.1088,0.1123,0.1158,0.1193,0.1228,0.1263,0.1298,0.1333,0.1368,0.1404,0.1439,0.1474,0.1509,0.1544,0.1579,0.1614,0.1649,0.1684,0.1719,0.1754,0.1789,0.1825,0.186,0.1895,0.193,0.1965,0.2,0.2035,0.207,0.2105,0.214,0.2175,0.2211,0.2246,0.2281,0.2316,0.2351,0.2386,0.2421,0.2456,0.2491,0.2526,0.2561,0.2596,0.2632,0.2667,0.2702,0.2737,0.2772,0.2807,0.2842,0.2877,0.2912,0.2947,0.2982,0.3018,0.3053,0.3088,0.3123,0.3158,0.3193,0.3228,0.3263,0.3298,0.3333,0.3368,0.3404,0.3439,0.3474,0.3509,0.3544,0.3579,0.3614,0.3649,0.3684,0.3719,0.3754,0.3789,0.3825,0.386,0.3895,0.393,0.3965,0.4,0.4035,0.407,0.4105,0.414,0.4175,0.4211,0.4246,0.4281,0.4316,0.4351,0.4386,0.4421,0.4456,0.4491,0.4526,0.4561,0.4596,0.4632,0.4667,0.4702,0.4737,0.4772,0.4807,0.4842,0.4877,0.4912,0.4947,0.4982,0.5018,0.5053,0.5088,0.5123,0.5158,0.5193,0.5228,0.5263,0.5298,0.5333,0.5368,0.5404,0.5439,0.5474,0.5509,0.5544,0.5579,0.5614,0.5649,0.5684,0.5719,0.5754,0.5789,0.5825,0.586,0.5895,0.593,0.5965,0.6,0.6035,0.607,0.6105,0.614,0.6175,0.6211,0.6246,0.6281,0.6316,0.6351,0.6386,0.6421,0.6456,0.6491,0.6526,0.6561,0.6596,0.6632,0.6667,0.6702,0.6737,0.6772,0.6807,0.6842,0.6877,0.6912,0.6947,0.6982,0.7018,0.7053,0.7088,0.7123,0.7158,0.7193,0.7228,0.7263,0.7298,0.7333,0.7368,0.7404,0.7439,0.7474,0.7509,0.7544,0.7579,0.7614,0.7649,0.7684,0.7719,0.7754,0.7789,0.7825,0.786,0.7895,0.793,0.7965,0.8,0.8035,0.807,0.8105,0.814,0.8175,0.8211,0.8246,0.8281,0.8316,0.8351,0.8386,0.8421,0.8456,0.8491,0.8526,0.8561,0.8596,0.8632,0.8667,0.8702,0.8737,0.8772,0.8807,0.8842,0.8877,0.8912,0.8947,0.8982,0.9018,0.9053,0.9088,0.9123,0.9158,0.9193,0.9228,0.9263,0.9298,0.9333,0.9368,0.9404,0.9439,0.9474,0.9509,0.9544,0.9579,0.9614,0.9649,0.9684,0.9719,0.9754,0.9789,0.9825,0.986,0.9895,0.993,0.9965,1]

Group313.children.append(OrientationInterpolator322)
#Euler angle triplet values, CHANNELS Zrotation Xrotation Yrotation, with min/max ranges [-23.619896,7.722682], [-9.093368,13.668425], [-6.728483,7.403621] degrees
#2.425202 2.584131 0.862019, 2.425202 2.584131 0.862019, 2.507924 2.583092 0.778887, 2.507924 2.583092 0.778887, 2.507924 2.583092 0.778887, 2.425202 2.584131 0.862019, 2.423151 2.672199 1.021105, 2.331845 2.757493 1.264444, 2.324676 2.767895 1.588864, 2.219845 2.825402 1.914622, 2.147104 2.788701 2.358574, 2.043523 2.666124 2.756536, 1.845469 2.442871 3.322897, 1.701275 2.216076 3.758269, 1.516805 2.077536 4.072685, 1.423512 1.814161 4.296466, 1.323453 1.756366 4.364845, 1.263316 1.702997 4.319884, 1.123673 1.644183 4.033422, 0.939131 1.615444 3.632405, 0.738429 1.509712 2.975586, 0.714545 1.493644 2.408378, 1.136336 1.636020 2.008490, 1.476841 1.857568 2.014554, 1.692564 2.191121 2.149876, 1.767853 2.356368 2.227104, 1.647455 2.406780 2.478721, 1.432222 2.502295 2.570813, 0.911024 2.277973 2.775821, 0.172392 2.093017 2.854671, -0.622351 1.828009 2.787702, -1.413738 1.411840 2.547649, -2.256546 1.031254 2.350314, -2.711773 0.718547 2.203094, -3.011640 0.745669 1.879156, -3.086140 0.935855 1.376735, -2.961441 1.307315 0.903848, -2.639648 1.622627 0.177630, -2.228441 1.924794 -0.470068, -1.812047 2.209719 -0.956298, -1.393627 2.480125 -1.280955, -0.796149 2.567468 -1.472320, -0.114666 2.672522 -1.495068, 0.615512 2.869852 -1.389345, 1.367952 2.936934 -1.103553, 2.078010 3.013291 -0.864071, 2.509998 2.955920 -0.631222, 2.795570 2.891051 -0.425056, 2.765944 2.506295 -0.356560, 2.490947 1.980154 -0.427704, 2.250733 1.555493 -0.455848, 2.117086 0.920921 -0.552645, 2.103763 0.508132 -0.638698, 2.148133 0.206115 -0.659964, 2.161341 -0.149437 -0.649195, 2.397282 -0.282166 -0.472345, 2.596385 -0.476399 -0.350118, 2.724742 -0.813723 -0.276890, 2.873708 -1.134987 -0.270375, 3.001080 -1.482456 -0.346130, 3.214745 -1.911450 -0.505587, 3.329103 -2.598218 -0.690572, 3.484975 -3.137272 -0.827606, 3.411432 -3.715842 -1.031346, 3.335580 -4.304617 -1.247071, 3.176093 -4.922218 -1.485297, 3.018499 -5.406498 -1.710445, 2.837440 -5.591376 -1.953514, 2.602935 -5.678675 -2.417490, 2.231601 -5.546670 -2.877692, 1.707146 -5.215414 -3.426120, 1.139465 -4.567967 -4.028709, 0.564360 -3.572576 -4.691836, -0.225312 -2.053906 -5.264689, -1.028463 -0.040582 -5.811797, -1.958845 2.744969 -6.141535, -2.850835 5.680039 -6.153817, -3.607931 8.454725 -5.699182, -3.802645 10.511350 -4.837614, -3.131095 11.508204 -3.628534, -1.823082 11.856555 -2.117942, 0.102901 11.497493 -0.294553, 2.209850 10.980565 1.385456, 4.131631 10.308961 2.789449, 5.669469 9.169767 3.526323, 6.692408 7.875071 3.706229, 7.377176 6.308747 3.329604, 7.722682 4.964311 2.605814, 7.634739 3.709096 1.899904, 7.219032 2.586866 1.312547, 6.452985 1.436670 1.048864, 5.612273 0.293318 1.013939, 4.486987 -0.799598 0.952553, 2.917699 -1.831618 0.875518, 1.076203 -2.657840 0.751543, -0.894876 -3.435911 0.619365, -2.932677 -4.189389 0.531615, -5.114984 -4.925286 0.542316, -7.464610 -5.537964 0.669507, -9.753782 -6.032449 0.739431, -12.152410 -6.349151 0.760042, -14.364840 -6.624610 0.800302, -16.496368 -6.773037 0.861199, -18.291426 -6.841619 0.927909, -19.526117 -6.771546 0.809087, -20.375408 -6.602769 0.660624, -20.807184 -6.318341 0.699890, -21.018391 -5.835792 0.789529, -21.007202 -5.153993 0.942987, -20.804256 -4.134989 1.359953, -20.359850 -2.537633 1.533395, -19.731369 -0.687919 1.430441, -19.205669 1.005236 1.194781, -18.809288 2.581347 1.111985, -18.189281 3.749157 1.174697, -17.647547 4.572639 1.385036, -17.119471 5.037562 1.911568, -16.719404 5.168798 2.613010, -16.316854 4.954871 3.280085, -15.818650 4.806251 3.972400, -15.143521 4.950146 4.278693, -14.231320 5.100270 4.131271, -13.220236 5.228276 3.814876, -12.427890 5.303133 3.474980, -11.648831 5.245377 3.366304, -11.087652 5.104040 3.391272, -10.566739 4.809288 3.516150, -10.124657 4.425951 3.718104, -9.746976 4.012103 3.762206, -9.245358 3.713213 3.687502, -8.749837 3.442718 3.714241, -8.207246 2.950294 3.744063, -7.800241 2.327383 3.809307, -7.486339 1.625862 3.960786, -7.214705 0.813421 3.884326, -6.953074 0.020067 3.644695, -6.792846 -0.809382 3.394863, -6.589338 -1.531509 3.111508, -6.143826 -2.192420 2.928502, -5.839762 -2.698032 2.638642, -5.573421 -3.269875 2.308733, -5.179349 -3.700901 1.837189, -4.860403 -3.993556 1.208354, -4.405800 -4.216228 0.655791, -3.815252 -4.515814 0.142070, -3.124770 -4.722589 -0.338998, -2.439898 -5.072422 -0.729393, -1.812852 -5.448676 -1.257809, -1.206467 -5.883669 -1.801237, -0.741169 -6.482183 -2.324724, -0.239776 -7.038072 -2.887120, 0.100473 -7.436812 -3.447225, 0.256184 -7.443763 -4.033586, 0.149506 -7.206019 -4.838401, -0.152114 -6.377877 -5.652634, -0.708606 -4.925940 -6.329010, -1.519338 -2.663972 -6.721354, -2.913324 0.466047 -6.728483, -4.473157 4.106512 -6.459960, -5.936733 7.529457 -5.898586, -6.797662 10.148153 -5.029838, -6.808119 11.832380 -3.843851, -6.025159 12.574698 -2.484786, -4.594378 12.767045 -0.945567, -2.637407 12.586160 0.456446, -0.494612 11.761012 1.707199, 1.651142 10.696146 2.703041, 3.563990 9.365761 3.189348, 5.143148 8.051891 3.223851, 6.138376 6.639955 2.806978, 6.604680 5.163795 2.265436, 6.513486 3.430048 1.750065, 5.901102 1.666885 1.253722, 5.095525 -0.111966 0.854268, 4.069852 -1.668368 0.464407, 2.910332 -3.006828 0.248049, 1.290655 -4.270497 0.028403, -0.690184 -5.405442 -0.005224, -2.902789 -6.382324 0.015564, -5.405581 -7.307895 0.044292, -8.253334 -8.174847 0.106334, -11.141315 -8.752104 0.227021, -13.891227 -9.068383 0.523654, -16.480547 -8.854589 0.684619, -18.937206 -8.411026 0.832167, -21.042263 -8.001430 1.030714, -22.646334 -7.656353 1.050493, -23.412756 -7.068203 1.150484, -23.619896 -6.158003 1.401605, -23.431641 -5.072293 1.580363, -23.019081 -3.920513 1.990800, -22.257782 -2.244141 2.786906, -21.267128 -0.346976 3.592521, -20.611868 1.314144 4.269357, -19.742203 2.609430 4.890854, -18.638042 3.378566 5.408951, -17.401072 3.810946 6.034092, -15.956229 3.967694 6.639023, -14.562157 4.026348 7.222071, -13.049326 4.025506 7.403621, -11.631183 4.086900 6.964666, -10.105343 4.038039 6.290307, -8.768139 4.044128 5.803460, -7.627457 3.880099 5.434517, -6.577711 3.759186 5.489887, -5.738364 3.645665 5.772319, -4.890085 3.428263 5.722960, -4.180766 3.251988 5.474356, -3.593595 2.971204 5.189721, -3.240815 2.733730 5.132963, -3.157389 2.598490 5.003756, -3.215949 2.499932 5.005891, -3.131891 2.289375 4.707678, -3.147826 2.124732 4.412086, -3.020215 1.844726 4.155404, -3.022264 1.546497 3.932713, -2.898591 1.267551 3.673257, -2.961832 0.848121 3.395640, -2.800933 0.318125 3.147584, -2.471157 -0.111235 2.992525, -2.184409 -0.707181 2.779421, -1.778916 -1.293042 2.533600, -1.395565 -2.011003 2.261255, -0.967401 -2.792706 1.948325, -0.767956 -3.600317 1.839066, -0.711969 -4.358867 1.668260, -0.661366 -5.098137 1.466050, -0.698915 -5.884237 1.261600, -0.889653 -6.692768 0.978101, -1.118983 -7.428358 0.637012, -1.277700 -8.207983 0.290958, -1.437689 -8.805524 -0.125139, -1.694507 -9.067228 -0.726956, -1.818096 -9.093368 -1.410890, -2.095885 -8.785511 -2.193850, -2.368146 -7.995113 -3.009614, -2.782512 -6.673240 -3.890692, -3.440862 -4.718197 -4.625148, -4.660296 -1.960986 -5.237294, -6.136866 1.390005 -5.721274, -7.726320 5.037798 -5.931162, -9.023488 8.331597 -5.711163, -9.628318 10.991716 -5.063140, -9.632290 12.803564 -3.975198, -8.730656 13.609695 -2.543628, -7.308375 13.668425 -0.981103, -5.584240 13.382105 0.504925, -4.025872 12.844546 1.746810, -2.672488 11.682527 2.741932, -1.436343 10.108156 3.157586, -0.373351 8.326473 3.155502, 0.563753 6.481862 2.839645, 1.374276 4.816467 2.490752, 1.776961 3.110854 2.386279, 1.697292 1.344978 2.461921, 0.991262 -0.205933 2.511175, -0.428352 -1.397347 2.476832, -2.320460 -2.429916 2.467374, -4.293278 -3.350758 2.355840, -6.208375 -3.854999 2.287564, -8.063935 -3.993778 2.229733, -9.796467 -3.681733 2.368032, -11.120317 -3.322241 2.329207, -12.517402 -2.978958 2.433282, -13.810494 -2.575547 2.497977, -15.018430 -1.873932 2.550983, -16.212374 -1.355580 2.588228, -17.092428 -1.097446 2.533878, -17.793930 -0.878919 2.308613, -18.191196 -0.572380 2.374650, -17.970158 0.163688 2.772251, -17.135996 1.177077 3.615283, -16.126371 1.980729 4.373848, -15.115627 2.713382 5.001661, -14.258899 3.283153 5.237583, -13.578729 3.640943 5.377181, -12.919566 3.875061 5.428818, -12.343954 3.904756 5.625055, -11.744227 4.137942 5.987854, -11.220801 4.232614 6.244277, -10.642786 4.351938 6.400125, -9.846327 4.484324 6.236682, -9.224895 4.625284 6.098688, -8.549911 4.639210 6.059036, -7.965559 4.725864 6.115324, -7.504282 4.793661 6.211139
#Interpolator5_l_midtarsal channels [15..17] sends animation values to BVH JOINT LeftAnkleEnd, DEF BvhConversion1_l_midtarsal, <HAnimJoint name=l_midtarsal/>
OrientationInterpolator323 = x3d.OrientationInterpolator()
OrientationInterpolator323.DEF = "Interpolator5_l_midtarsal"
OrientationInterpolator323.key = [0,0.0035,0.007,0.0105,0.014,0.0175,0.0211,0.0246,0.0281,0.0316,0.0351,0.0386,0.0421,0.0456,0.0491,0.0526,0.0561,0.0596,0.0632,0.0667,0.0702,0.0737,0.0772,0.0807,0.0842,0.0877,0.0912,0.0947,0.0982,0.1018,0.1053,0.1088,0.1123,0.1158,0.1193,0.1228,0.1263,0.1298,0.1333,0.1368,0.1404,0.1439,0.1474,0.1509,0.1544,0.1579,0.1614,0.1649,0.1684,0.1719,0.1754,0.1789,0.1825,0.186,0.1895,0.193,0.1965,0.2,0.2035,0.207,0.2105,0.214,0.2175,0.2211,0.2246,0.2281,0.2316,0.2351,0.2386,0.2421,0.2456,0.2491,0.2526,0.2561,0.2596,0.2632,0.2667,0.2702,0.2737,0.2772,0.2807,0.2842,0.2877,0.2912,0.2947,0.2982,0.3018,0.3053,0.3088,0.3123,0.3158,0.3193,0.3228,0.3263,0.3298,0.3333,0.3368,0.3404,0.3439,0.3474,0.3509,0.3544,0.3579,0.3614,0.3649,0.3684,0.3719,0.3754,0.3789,0.3825,0.386,0.3895,0.393,0.3965,0.4,0.4035,0.407,0.4105,0.414,0.4175,0.4211,0.4246,0.4281,0.4316,0.4351,0.4386,0.4421,0.4456,0.4491,0.4526,0.4561,0.4596,0.4632,0.4667,0.4702,0.4737,0.4772,0.4807,0.4842,0.4877,0.4912,0.4947,0.4982,0.5018,0.5053,0.5088,0.5123,0.5158,0.5193,0.5228,0.5263,0.5298,0.5333,0.5368,0.5404,0.5439,0.5474,0.5509,0.5544,0.5579,0.5614,0.5649,0.5684,0.5719,0.5754,0.5789,0.5825,0.586,0.5895,0.593,0.5965,0.6,0.6035,0.607,0.6105,0.614,0.6175,0.6211,0.6246,0.6281,0.6316,0.6351,0.6386,0.6421,0.6456,0.6491,0.6526,0.6561,0.6596,0.6632,0.6667,0.6702,0.6737,0.6772,0.6807,0.6842,0.6877,0.6912,0.6947,0.6982,0.7018,0.7053,0.7088,0.7123,0.7158,0.7193,0.7228,0.7263,0.7298,0.7333,0.7368,0.7404,0.7439,0.7474,0.7509,0.7544,0.7579,0.7614,0.7649,0.7684,0.7719,0.7754,0.7789,0.7825,0.786,0.7895,0.793,0.7965,0.8,0.8035,0.807,0.8105,0.814,0.8175,0.8211,0.8246,0.8281,0.8316,0.8351,0.8386,0.8421,0.8456,0.8491,0.8526,0.8561,0.8596,0.8632,0.8667,0.8702,0.8737,0.8772,0.8807,0.8842,0.8877,0.8912,0.8947,0.8982,0.9018,0.9053,0.9088,0.9123,0.9158,0.9193,0.9228,0.9263,0.9298,0.9333,0.9368,0.9404,0.9439,0.9474,0.9509,0.9544,0.9579,0.9614,0.9649,0.9684,0.9719,0.9754,0.9789,0.9825,0.986,0.9895,0.993,0.9965,1]

Group313.children.append(OrientationInterpolator323)
#Unchanging Euler angle triplet values, CHANNELS Zrotation Xrotation Yrotation, with min/max ranges [0.0,4.9E-324], [0.0,4.9E-324], [0.0,4.9E-324] degrees
#0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000
#Interpolator6_r_hip channels [18..20] sends animation values to BVH JOINT RightHip, DEF BvhConversion1_r_hip, <HAnimJoint name=r_hip/>
OrientationInterpolator324 = x3d.OrientationInterpolator()
OrientationInterpolator324.DEF = "Interpolator6_r_hip"
OrientationInterpolator324.key = [0,0.0035,0.007,0.0105,0.014,0.0175,0.0211,0.0246,0.0281,0.0316,0.0351,0.0386,0.0421,0.0456,0.0491,0.0526,0.0561,0.0596,0.0632,0.0667,0.0702,0.0737,0.0772,0.0807,0.0842,0.0877,0.0912,0.0947,0.0982,0.1018,0.1053,0.1088,0.1123,0.1158,0.1193,0.1228,0.1263,0.1298,0.1333,0.1368,0.1404,0.1439,0.1474,0.1509,0.1544,0.1579,0.1614,0.1649,0.1684,0.1719,0.1754,0.1789,0.1825,0.186,0.1895,0.193,0.1965,0.2,0.2035,0.207,0.2105,0.214,0.2175,0.2211,0.2246,0.2281,0.2316,0.2351,0.2386,0.2421,0.2456,0.2491,0.2526,0.2561,0.2596,0.2632,0.2667,0.2702,0.2737,0.2772,0.2807,0.2842,0.2877,0.2912,0.2947,0.2982,0.3018,0.3053,0.3088,0.3123,0.3158,0.3193,0.3228,0.3263,0.3298,0.3333,0.3368,0.3404,0.3439,0.3474,0.3509,0.3544,0.3579,0.3614,0.3649,0.3684,0.3719,0.3754,0.3789,0.3825,0.386,0.3895,0.393,0.3965,0.4,0.4035,0.407,0.4105,0.414,0.4175,0.4211,0.4246,0.4281,0.4316,0.4351,0.4386,0.4421,0.4456,0.4491,0.4526,0.4561,0.4596,0.4632,0.4667,0.4702,0.4737,0.4772,0.4807,0.4842,0.4877,0.4912,0.4947,0.4982,0.5018,0.5053,0.5088,0.5123,0.5158,0.5193,0.5228,0.5263,0.5298,0.5333,0.5368,0.5404,0.5439,0.5474,0.5509,0.5544,0.5579,0.5614,0.5649,0.5684,0.5719,0.5754,0.5789,0.5825,0.586,0.5895,0.593,0.5965,0.6,0.6035,0.607,0.6105,0.614,0.6175,0.6211,0.6246,0.6281,0.6316,0.6351,0.6386,0.6421,0.6456,0.6491,0.6526,0.6561,0.6596,0.6632,0.6667,0.6702,0.6737,0.6772,0.6807,0.6842,0.6877,0.6912,0.6947,0.6982,0.7018,0.7053,0.7088,0.7123,0.7158,0.7193,0.7228,0.7263,0.7298,0.7333,0.7368,0.7404,0.7439,0.7474,0.7509,0.7544,0.7579,0.7614,0.7649,0.7684,0.7719,0.7754,0.7789,0.7825,0.786,0.7895,0.793,0.7965,0.8,0.8035,0.807,0.8105,0.814,0.8175,0.8211,0.8246,0.8281,0.8316,0.8351,0.8386,0.8421,0.8456,0.8491,0.8526,0.8561,0.8596,0.8632,0.8667,0.8702,0.8737,0.8772,0.8807,0.8842,0.8877,0.8912,0.8947,0.8982,0.9018,0.9053,0.9088,0.9123,0.9158,0.9193,0.9228,0.9263,0.9298,0.9333,0.9368,0.9404,0.9439,0.9474,0.9509,0.9544,0.9579,0.9614,0.9649,0.9684,0.9719,0.9754,0.9789,0.9825,0.986,0.9895,0.993,0.9965,1]

Group313.children.append(OrientationInterpolator324)
#Euler angle triplet values, CHANNELS Zrotation Xrotation Yrotation, with min/max ranges [-4.157261,6.750121], [-29.20495,17.635117], [-17.819462,1.117753] degrees
#-0.463647 5.886320 -1.013938, -0.457973 5.955936 -0.952109, -0.472793 6.027548 -0.889615, -0.665969 6.096365 -0.810241, -0.870313 6.026208 -0.854687, -1.113930 5.745759 -0.780209, -1.311787 5.546465 -0.752326, -1.369681 5.281392 -0.732511, -1.429278 4.982326 -0.662568, -1.482513 4.752792 -0.530477, -1.449486 4.551945 -0.397918, -1.470868 4.347774 -0.167059, -1.571716 4.038394 -0.102584, -1.785921 3.847450 -0.141724, -1.883015 3.735377 -0.297418, -1.936328 3.705180 -0.498352, -1.892994 3.626591 -0.731540, -1.808667 3.292837 -0.917364, -1.588066 2.841102 -1.295890, -1.383252 2.179703 -1.652080, -1.239107 1.563532 -1.951524, -0.925871 0.874250 -2.159603, -0.768206 -0.053329 -2.478601, -0.547427 -1.477904 -3.061992, -0.326667 -3.357264 -3.742706, -0.101292 -5.526819 -4.866435, 0.234320 -7.669518 -6.232724, 0.461297 -9.543160 -7.630078, 0.701795 -11.269773 -9.123387, 1.083134 -12.808705 -10.407759, 1.534882 -14.278560 -11.470045, 2.117400 -15.795771 -12.185031, 2.654253 -17.134100 -12.441459, 3.066722 -18.434092 -12.499436, 3.388619 -19.657310 -12.067257, 3.733262 -20.693235 -11.137940, 4.111614 -21.689083 -9.835261, 4.536672 -22.466307 -8.315687, 5.097023 -23.281029 -6.895510, 5.639353 -23.814924 -5.735267, 5.962579 -24.189854 -5.032736, 6.007799 -24.616217 -4.861295, 5.955014 -25.033178 -5.055720, 5.950693 -25.594276 -5.570896, 5.717373 -26.311792 -5.989933, 5.531695 -27.105438 -6.157423, 5.393551 -27.537914 -6.029875, 5.285458 -27.884010 -5.832609, 5.059349 -28.082926 -5.605918, 4.894954 -28.279188 -5.433496, 4.760615 -28.366486 -5.258080, 4.479827 -28.507729 -5.256432, 4.312781 -28.751268 -5.270215, 4.076246 -28.998310 -5.393849, 3.851585 -29.204950 -5.480572, 3.711441 -29.167879 -5.606119, 3.610655 -29.193022 -5.761967, 3.498630 -28.911566 -5.892942, 3.369718 -28.541307 -6.079056, 3.349475 -28.031677 -6.214269, 3.290246 -27.394953 -6.292204, 3.331900 -26.712570 -6.284389, 3.508061 -26.058996 -5.890000, 3.552973 -25.368921 -5.460135, 3.783094 -24.505535 -4.876289, 3.936068 -23.810205 -4.383720, 4.221247 -23.154421 -3.834478, 4.748349 -22.484440 -3.382954, 5.428765 -21.664371 -2.853463, 6.089560 -20.813793 -2.305517, 6.605723 -19.838264 -1.829423, 6.750121 -18.754608 -1.497699, 6.643376 -17.600946 -1.229919, 6.459007 -16.660398 -0.950322, 6.002895 -15.738651 -0.738355, 5.639166 -14.793545 -0.379958, 5.212533 -13.800171 0.037337, 4.828225 -12.938966 0.342959, 4.485624 -12.178822 0.554227, 4.221767 -11.520246 0.700612, 3.859385 -10.884043 0.897993, 3.716600 -10.258261 0.998645, 3.360383 -9.660075 1.019226, 3.074944 -9.015380 1.117753, 2.841785 -8.254423 1.076442, 2.432330 -7.462487 1.069395, 2.057575 -6.595348 1.012978, 1.568497 -5.686317 0.795890, 1.062052 -4.733721 0.449166, 0.729567 -3.660034 0.066964, 0.350556 -2.739143 -0.321271, 0.070376 -1.860759 -0.778128, -0.306883 -1.138149 -1.144540, -0.579319 -0.484952 -1.255065, -0.876170 0.236495 -1.215063, -1.051389 0.885046 -1.214768, -1.098649 1.607574 -1.089470, -1.090433 2.247508 -0.810580, -1.116042 2.992103 -0.592501, -1.154498 3.714391 -0.287497, -1.262548 4.518425 -0.131846, -1.304290 5.318889 -0.043744, -1.464701 6.231959 -0.059220, -1.377744 7.060910 -0.040106, -1.400815 7.775869 -0.084577, -1.502751 8.493948 -0.054776, -1.544973 9.191073 -0.077002, -1.478779 9.775628 0.005775, -1.523585 10.404763 -0.078392, -1.676420 11.048604 -0.300093, -1.748250 11.621850 -0.659893, -1.752449 12.136559 -0.958755, -1.762879 12.496050 -1.384550, -1.642777 12.736542 -1.688950, -1.741087 12.855229 -2.087424, -1.906742 12.888752 -2.456828, -2.011202 12.690244 -2.796060, -2.385841 12.224241 -3.286139, -2.730122 11.568026 -3.795554, -3.094247 10.518070 -4.509542, -3.604671 9.124733 -5.595598, -3.779162 7.618917 -7.115694, -3.854045 5.994053 -8.691518, -3.761798 4.124072 -10.220773, -3.459478 2.090429 -11.733425, -3.031996 0.062712 -13.071626, -2.441271 -2.050382 -14.098674, -1.959504 -4.211298 -14.893917, -1.286351 -6.429687 -15.350651, -0.478198 -8.695275 -15.534271, 0.211168 -11.004461 -15.309449, 0.881029 -13.107648 -14.785451, 1.690489 -15.108415 -13.977064, 2.416154 -16.807724 -12.861652, 3.116418 -18.144270 -11.610748, 3.756861 -19.212727 -10.412024, 4.301610 -19.933638 -9.409688, 4.747635 -20.257902 -8.480508, 5.030520 -20.392735 -7.575719, 5.270149 -20.394142 -6.807278, 5.331741 -20.421822 -6.210309, 5.278721 -20.516788 -5.732181, 5.322324 -20.744593 -5.334225, 5.150934 -20.877686 -5.348425, 4.804814 -20.917683 -5.597732, 4.487149 -20.833452 -6.033696, 4.186182 -20.793715 -6.538296, 3.877923 -20.742929 -7.041483, 3.581530 -20.618643 -7.518840, 3.468884 -20.488411 -8.005243, 3.327722 -20.296400 -8.617578, 3.399545 -20.007603 -9.128187, 3.522944 -19.775534 -9.696836, 3.757460 -19.497318 -9.966290, 4.097724 -19.225155 -9.738769, 4.263249 -18.969984 -8.910983, 4.412739 -18.665823 -7.784949, 4.520356 -18.166620 -6.803941, 4.689763 -17.215788 -6.234726, 4.863308 -16.027906 -6.022487, 5.024212 -14.800842 -5.896482, 5.129777 -13.647424 -5.788636, 5.308755 -12.560731 -5.532104, 5.314611 -11.384269 -5.292693, 5.453815 -10.494841 -4.698837, 5.378489 -9.542732 -3.919442, 5.213875 -8.641736 -2.815875, 5.087012 -7.648619 -1.574076, 4.879580 -6.605193 -0.371917, 4.746145 -5.445519 0.577225, 4.626693 -4.273258 1.035020, 4.441142 -2.913353 0.948103, 4.241659 -1.634031 0.595797, 4.100333 -0.374560 0.186840, 4.011729 0.697272 -0.031530, 3.860321 1.754820 -0.129542, 3.691031 2.763736 -0.003784, 3.584299 3.912417 0.235801, 3.445764 4.889366 0.385799, 3.424094 5.902555 0.535967, 3.255823 6.966758 0.503870, 3.150817 8.148797 0.323724, 3.165222 9.425735 -0.007766, 2.960749 10.652176 -0.362968, 2.881762 11.807482 -0.516929, 2.709460 12.906066 -0.673665, 2.630348 13.781452 -0.960311, 2.506705 14.577859 -1.207686, 2.360642 15.159471 -1.407366, 2.183453 15.691246 -1.489409, 1.906119 16.279266 -1.539339, 1.568499 16.718784 -1.594183, 1.175865 17.178127 -1.766173, 0.731185 17.562960 -2.092832, 0.182876 17.635117 -2.462072, -0.372652 17.236496 -2.861568, -1.101940 16.325605 -3.219931, -1.950349 14.802380 -3.794124, -2.750351 12.946177 -4.801467, -3.424177 10.895785 -6.184981, -3.881728 8.630133 -7.881871, -4.105083 6.352144 -9.682067, -4.157261 4.218960 -11.689063, -3.948370 2.124501 -13.617095, -3.787050 -0.196837 -15.401984, -3.507659 -2.675207 -16.646437, -3.140734 -5.155109 -17.400879, -2.699046 -7.676798 -17.721062, -2.185551 -10.070715 -17.819462, -1.802923 -12.293236 -17.560360, -1.382921 -14.395090 -17.179588, -0.950256 -16.137039 -16.813040, -0.382363 -17.661182 -16.556826, 0.258302 -18.739738 -16.663462, 0.926987 -19.421955 -16.915390, 1.555242 -19.717329 -17.030552, 2.050861 -19.791441 -16.970638, 2.458752 -19.691887 -16.663542, 2.606148 -19.392775 -15.894265, 2.797546 -19.025570 -14.627461, 3.117550 -18.608395 -12.908180, 3.423256 -18.080263 -11.089259, 3.540972 -17.561430 -9.451152, 3.557288 -17.106382 -8.109180, 3.522011 -16.558163 -7.324380, 3.390974 -16.127211 -7.185462, 3.401210 -15.860987 -7.381222, 3.651670 -15.910362 -7.665988, 3.924821 -16.191498 -7.881756, 4.339554 -16.281445 -7.982944, 4.714711 -16.293037 -8.055700, 4.836370 -15.991734 -8.124286, 5.024116 -15.484343 -8.160383, 5.210375 -14.864449 -8.002171, 5.296193 -14.300697 -7.641986, 5.429678 -14.027777 -6.990834, 5.609048 -13.670386 -6.073062, 5.829651 -13.282688 -4.996759, 5.912680 -12.708654 -4.007614, 6.013404 -11.939031 -3.116405, 5.976576 -10.863632 -2.739347, 5.820282 -9.801188 -2.759179, 5.624299 -8.920067 -3.249668, 5.609976 -7.921388 -3.790775, 5.537173 -6.848904 -4.369917, 5.564547 -5.961347 -4.918029, 5.607047 -5.252285 -5.249875, 5.640219 -4.729235 -4.873546, 5.548913 -4.562819 -4.041572, 5.410915 -4.374331 -2.942324, 5.284744 -4.306036 -1.921776, 5.102231 -4.036222 -1.076814, 4.894138 -3.666281 -0.807980, 4.826862 -2.960758 -0.939140, 4.808983 -2.277413 -1.339410, 4.603314 -1.631924 -1.753800, 4.496749 -1.062432 -2.132121, 4.347103 -0.704714 -2.254283, 4.370907 -0.355380 -2.131359, 4.326640 -0.121804 -1.862022, 4.339124 0.157666 -1.519199, 4.464204 0.513727 -1.022893, 4.420378 1.099448 -0.626069, 4.376482 1.816472 -0.309278, 4.322760 2.532227 0.008877, 4.257355 3.188894 0.187650, 4.316024 3.822310 0.407717, 4.287640 4.297883 0.393731, 4.240575 4.744157 0.411672, 4.245694 5.269475 0.393869, 4.229390 5.646245 0.267282, 4.057909 6.175666 0.210660, 3.884034 6.704000 0.155517, 3.742094 7.236833 -0.001850, 3.509140 7.791162 -0.083761, 3.236142 8.268278 -0.130473, 3.033978 8.731081 -0.466509, 2.711394 8.855350 -0.742982, 2.333648 8.694297 -1.174541, 2.088072 8.384262 -1.920870, 1.744212 7.616653 -2.824636, 1.433588 6.568992 -3.750380, 1.080521 5.328060 -4.902299, 0.713508 3.894096 -6.049717, 0.278969 2.115276 -7.218181, 0.001921 0.356889 -8.438903
#Interpolator7_r_knee channels [21..23] sends animation values to BVH JOINT RightKnee, DEF BvhConversion1_r_knee, <HAnimJoint name=r_knee/>
OrientationInterpolator325 = x3d.OrientationInterpolator()
OrientationInterpolator325.DEF = "Interpolator7_r_knee"
OrientationInterpolator325.key = [0,0.0035,0.007,0.0105,0.014,0.0175,0.0211,0.0246,0.0281,0.0316,0.0351,0.0386,0.0421,0.0456,0.0491,0.0526,0.0561,0.0596,0.0632,0.0667,0.0702,0.0737,0.0772,0.0807,0.0842,0.0877,0.0912,0.0947,0.0982,0.1018,0.1053,0.1088,0.1123,0.1158,0.1193,0.1228,0.1263,0.1298,0.1333,0.1368,0.1404,0.1439,0.1474,0.1509,0.1544,0.1579,0.1614,0.1649,0.1684,0.1719,0.1754,0.1789,0.1825,0.186,0.1895,0.193,0.1965,0.2,0.2035,0.207,0.2105,0.214,0.2175,0.2211,0.2246,0.2281,0.2316,0.2351,0.2386,0.2421,0.2456,0.2491,0.2526,0.2561,0.2596,0.2632,0.2667,0.2702,0.2737,0.2772,0.2807,0.2842,0.2877,0.2912,0.2947,0.2982,0.3018,0.3053,0.3088,0.3123,0.3158,0.3193,0.3228,0.3263,0.3298,0.3333,0.3368,0.3404,0.3439,0.3474,0.3509,0.3544,0.3579,0.3614,0.3649,0.3684,0.3719,0.3754,0.3789,0.3825,0.386,0.3895,0.393,0.3965,0.4,0.4035,0.407,0.4105,0.414,0.4175,0.4211,0.4246,0.4281,0.4316,0.4351,0.4386,0.4421,0.4456,0.4491,0.4526,0.4561,0.4596,0.4632,0.4667,0.4702,0.4737,0.4772,0.4807,0.4842,0.4877,0.4912,0.4947,0.4982,0.5018,0.5053,0.5088,0.5123,0.5158,0.5193,0.5228,0.5263,0.5298,0.5333,0.5368,0.5404,0.5439,0.5474,0.5509,0.5544,0.5579,0.5614,0.5649,0.5684,0.5719,0.5754,0.5789,0.5825,0.586,0.5895,0.593,0.5965,0.6,0.6035,0.607,0.6105,0.614,0.6175,0.6211,0.6246,0.6281,0.6316,0.6351,0.6386,0.6421,0.6456,0.6491,0.6526,0.6561,0.6596,0.6632,0.6667,0.6702,0.6737,0.6772,0.6807,0.6842,0.6877,0.6912,0.6947,0.6982,0.7018,0.7053,0.7088,0.7123,0.7158,0.7193,0.7228,0.7263,0.7298,0.7333,0.7368,0.7404,0.7439,0.7474,0.7509,0.7544,0.7579,0.7614,0.7649,0.7684,0.7719,0.7754,0.7789,0.7825,0.786,0.7895,0.793,0.7965,0.8,0.8035,0.807,0.8105,0.814,0.8175,0.8211,0.8246,0.8281,0.8316,0.8351,0.8386,0.8421,0.8456,0.8491,0.8526,0.8561,0.8596,0.8632,0.8667,0.8702,0.8737,0.8772,0.8807,0.8842,0.8877,0.8912,0.8947,0.8982,0.9018,0.9053,0.9088,0.9123,0.9158,0.9193,0.9228,0.9263,0.9298,0.9333,0.9368,0.9404,0.9439,0.9474,0.9509,0.9544,0.9579,0.9614,0.9649,0.9684,0.9719,0.9754,0.9789,0.9825,0.986,0.9895,0.993,0.9965,1]

Group313.children.append(OrientationInterpolator325)
#Euler angle triplet values, CHANNELS Zrotation Xrotation Yrotation, with min/max ranges [-46.181885,3.916524], [-0.300555,52.181007], [-8.439433,42.513977] degrees
#2.001732 -0.162876 3.639678, 1.974982 -0.155333 3.605519, 1.963410 -0.153872 3.527220, 2.156318 -0.221908 3.470656, 2.407975 -0.300555 3.527844, 2.574924 -0.281542 3.582581, 2.719984 -0.183522 3.662675, 2.825301 -0.080024 3.784698, 2.859258 0.087116 3.800880, 2.888186 0.181490 3.757687, 2.884585 0.278321 3.635533, 2.966480 0.454083 3.295805, 3.100296 0.723090 3.113770, 3.197531 0.982386 3.063685, 3.219869 1.255035 2.924692, 3.042033 1.637554 2.798402, 2.782180 2.160292 2.629052, 2.423636 2.940365 2.350888, 1.952588 3.957536 2.216810, 1.363797 5.177670 2.248248, 0.709036 6.560304 2.158115, -0.147177 8.306978 1.975717, -1.141260 10.495391 2.053399, -2.312393 13.173897 2.620381, -3.755092 16.235859 3.737742, -5.427441 19.328680 5.344125, -7.364349 22.065035 7.519727, -9.183669 24.383806 9.752104, -10.832458 26.083900 12.059031, -12.305082 27.107157 14.091288, -13.444748 27.513578 15.496689, -14.087172 27.611904 16.102276, -14.284027 27.350363 16.004265, -13.783643 26.779451 15.333961, -12.847063 26.030251 13.999450, -11.560117 25.105005 12.156238, -10.216016 24.071886 9.994284, -8.861128 22.791538 7.758323, -7.833241 21.461786 5.844345, -6.995211 19.823187 4.354496, -6.361458 18.178997 3.537765, -5.900111 16.546497 3.190256, -5.609516 15.136958 3.343760, -5.433230 14.156156 3.884638, -5.214726 13.565488 4.260231, -5.065650 13.212629 4.577106, -4.875842 12.773151 4.590578, -4.722577 12.335842 4.532638, -4.541140 11.871283 4.349079, -4.342463 11.465203 4.052843, -4.226254 11.176047 3.573049, -4.109262 11.010650 3.108115, -4.137017 10.970811 2.622897, -4.021383 11.346258 2.157773, -4.071828 11.724965 1.877884, -4.238874 12.067057 1.699150, -4.391355 12.452980 1.616738, -4.529897 12.742439 1.782779, -4.663151 12.840938 1.955540, -4.739670 12.967589 2.101578, -4.788178 12.901465 2.104247, -4.840108 12.921306 2.248766, -4.871541 12.765905 2.137377, -4.771135 12.569151 1.776082, -4.624113 12.111097 1.243305, -4.395478 11.605447 0.581202, -4.291938 11.388247 0.120887, -4.428962 11.153741 0.154855, -4.720733 11.011622 0.454882, -5.028743 10.934873 0.999584, -5.210986 10.845778 1.582379, -5.063566 10.637801 2.019915, -4.823518 10.274761 2.230628, -4.476573 10.143163 2.187402, -3.762183 10.013012 1.790621, -3.088616 9.773967 1.298253, -2.486484 9.504086 0.914024, -1.865461 9.231792 0.569619, -1.318339 8.949812 0.313394, -0.979632 8.664416 0.199851, -0.595666 8.281788 0.011285, -0.429651 8.064204 -0.216372, -0.125844 7.844276 -0.511486, 0.172016 7.626734 -0.956572, 0.410056 7.215672 -1.274670, 0.712747 6.742887 -1.521036, 0.881426 6.155397 -1.719298, 1.194639 5.392572 -1.820056, 1.514584 4.593886 -1.936393, 1.770030 3.802256 -1.974764, 2.039700 3.090366 -1.951738, 2.306379 2.449230 -1.863045, 2.552228 2.098439 -1.849017, 2.928946 1.663244 -1.903092, 3.205907 1.332726 -1.986195, 3.530823 1.254429 -1.773233, 3.581253 1.050651 -1.475416, 3.692049 0.985614 -1.223700, 3.703293 0.987747 -1.060776, 3.761990 1.051775 -0.945427, 3.886820 1.098065 -0.804597, 3.837694 1.208559 -0.497884, 3.916524 1.277627 -0.075999, 3.827524 1.494297 0.320931, 3.708334 1.752540 0.787973, 3.657741 2.001651 1.193619, 3.488535 2.384713 1.467024, 3.261390 2.828017 1.505921, 2.956108 3.411001 1.764432, 2.748426 4.041200 2.202509, 2.287110 4.690989 2.762583, 1.725519 5.473937 3.271918, 1.051802 6.518163 3.693568, 0.157653 7.734126 3.919037, -0.801515 9.112915 4.192769, -1.732773 10.738519 4.328813, -2.859763 12.820394 4.577426, -3.784103 15.321237 5.005706, -4.910165 18.177420 5.728527, -6.274833 21.467522 6.895541, -8.019513 24.934141 8.738546, -10.438185 28.353037 11.308995, -13.268949 31.448097 14.358880, -16.241367 34.301811 17.373274, -19.488073 36.748940 20.380249, -22.573000 38.717522 23.101353, -25.530777 40.309803 25.426582, -28.100498 41.444080 27.388176, -30.117334 42.125404 28.788298, -31.523581 42.299782 29.575430, -31.981863 42.171753 29.635563, -31.598112 41.594021 28.991955, -30.569090 40.655361 27.774494, -28.768600 39.316132 26.071680, -26.439220 37.516926 24.126627, -23.821323 35.332893 22.126793, -21.092897 32.745098 20.290514, -18.360378 29.735144 18.279501, -15.699046 26.631901 16.202709, -13.144069 23.414566 13.789204, -10.873873 20.311642 11.428522, -8.943020 17.383356 8.892623, -7.355667 14.783790 6.208544, -6.126102 12.291492 3.653885, -4.978260 10.125965 1.464131, -4.098389 8.082958 -0.295917, -3.369165 6.381420 -1.361425, -2.938743 5.992514 -2.192422, -2.539734 5.869695 -2.622740, -2.430053 6.139540 -2.809393, -2.526030 6.679293 -2.725214, -2.811104 7.246716 -2.440792, -3.138203 7.967907 -2.140275, -3.554841 8.914914 -1.864912, -4.007148 10.068663 -1.733689, -4.130911 11.514149 -1.802776, -4.003350 12.999018 -1.988013, -3.631406 14.257830 -1.846859, -3.274170 14.849031 -1.111226, -2.926384 15.120211 -0.099571, -2.680452 15.162329 0.583471, -2.539057 15.163374 0.985910, -2.394097 15.206486 1.136488, -2.180790 15.259028 1.056802, -1.872298 15.294940 0.962587, -1.527063 15.245147 0.795224, -1.025722 15.013369 0.536808, -0.569391 14.661027 0.000102, -0.115072 14.300466 -0.527326, 0.224691 13.685206 -0.927246, 0.442070 13.060209 -1.061357, 0.683586 12.215458 -0.890073, 0.885394 11.456342 -0.438846, 0.932354 10.791257 0.046647, 1.040845 10.386720 0.276284, 1.270650 10.061666 0.414335, 1.406082 9.835327 0.492636, 1.547264 9.620447 0.624740, 1.687050 9.481987 0.814276, 1.731036 9.433089 0.899568, 1.875499 9.338115 1.190558, 1.847519 9.115906 1.562926, 1.775944 9.155837 1.980120, 1.738134 9.185627 2.398256, 1.570036 9.248766 2.582848, 1.487954 9.405267 2.867562, 1.363377 9.859189 3.214803, 1.056762 10.480704 3.520538, 0.717987 11.291559 3.935695, 0.382407 12.224399 4.107880, 0.068922 13.286814 4.268035, -0.460080 14.452376 4.542985, -1.270127 15.793427 5.061834, -2.327500 17.259752 5.694455, -3.516834 19.142199 6.359796, -4.917336 21.499426 6.753368, -6.328342 24.523106 7.030566, -8.064460 28.205963 7.477740, -10.604738 32.128986 8.639803, -14.118433 36.001942 10.989956, -18.484821 39.411350 14.908314, -23.323460 42.200218 19.801580, -28.336290 44.340679 24.968285, -33.148495 45.934048 29.804996, -37.560745 47.203293 34.130848, -41.336960 48.439526 37.757168, -43.977448 49.509918 40.417171, -45.637043 50.454739 41.944248, -46.181885 51.239594 42.513977, -45.702866 51.880955 42.097313, -44.222252 52.181007 40.865089, -41.891033 51.981968 38.814335, -38.658604 50.999298 36.037281, -35.297382 49.199417 33.240112, -31.866846 46.623466 30.461588, -28.225664 43.571461 27.579420, -24.387226 40.148876 24.649954, -20.729425 36.624245 21.580458, -16.865290 32.868908 18.140509, -13.371744 28.919968 14.536125, -10.129426 24.792709 10.576402, -7.446207 20.560509 6.508485, -5.149621 16.423386 2.445040, -3.388072 12.458154 -1.430448, -2.201015 8.902619 -4.750215, -1.386421 6.247604 -7.080207, -1.097278 4.564311 -8.277807, -1.203241 3.878125 -8.439433, -1.524437 3.986209 -7.705368, -1.932659 4.313298 -6.508325, -2.353320 4.680636 -5.158072, -2.522150 4.911699 -4.410331, -2.573926 5.211461 -4.305818, -2.634416 5.609536 -4.781474, -2.720031 6.111180 -5.466411, -2.711425 7.052791 -6.076879, -2.796978 8.106204 -6.471006, -2.747562 9.036945 -6.690616, -2.395322 9.928328 -6.812799, -1.994368 10.468567 -6.723036, -1.526165 10.587839 -6.330739, -1.002279 10.477650 -5.757119, -0.518567 10.262691 -5.048285, -0.208833 10.033872 -4.419474, -0.041884 9.748567 -3.797436, 0.059617 9.722675 -3.253833, 0.179499 9.797924 -2.951916, 0.307931 10.088033 -3.022049, 0.415573 10.434112 -3.401065, 0.577896 10.580239 -3.971809, 0.683402 10.668882 -4.532686, 0.919943 10.575810 -5.159387, 1.081762 10.470474 -5.467131, 1.133850 10.160913 -5.499030, 1.009883 9.865846 -5.318605, 0.896696 9.414899 -5.088644, 0.793863 9.154288 -4.725331, 0.604199 9.226269 -4.344578, 0.455389 9.312288 -3.993660, 0.363349 9.584834 -3.650240, 0.266303 9.855857 -3.306264, 0.179131 10.180693 -3.058557, 0.231367 10.460989 -2.718511, 0.184382 10.604227 -2.320899, 0.203327 10.751811 -1.896314, 0.078993 10.906775 -1.430359, -0.135063 10.949221 -0.975157, -0.337028 11.162957 -0.457326, -0.524769 11.305873 -0.002015, -0.696708 11.160870 0.519612, -0.892883 11.165123 0.928230, -1.072793 11.075237 1.135248, -1.253799 10.983347 1.339870, -1.521119 10.859595 1.628786, -1.768602 10.890636 1.645828, -2.119739 11.086560 1.657222, -2.591458 11.519073 1.732975, -3.057875 12.203814 1.788592, -3.687214 13.222310 2.054907, -4.470952 14.550350 2.585019, -5.376544 16.271599 3.378662, -6.627742 18.370691 4.367634, -7.920386 20.717602 5.498173, -9.414497 23.290794 6.790174, -11.190895 26.133850 8.374302, -13.263932 28.851444 10.092083
#Interpolator8_r_ankle channels [24..26] sends animation values to BVH JOINT RightAnkle, DEF BvhConversion1_r_ankle, <HAnimJoint name=r_ankle/>
OrientationInterpolator326 = x3d.OrientationInterpolator()
OrientationInterpolator326.DEF = "Interpolator8_r_ankle"
OrientationInterpolator326.key = [0,0.0035,0.007,0.0105,0.014,0.0175,0.0211,0.0246,0.0281,0.0316,0.0351,0.0386,0.0421,0.0456,0.0491,0.0526,0.0561,0.0596,0.0632,0.0667,0.0702,0.0737,0.0772,0.0807,0.0842,0.0877,0.0912,0.0947,0.0982,0.1018,0.1053,0.1088,0.1123,0.1158,0.1193,0.1228,0.1263,0.1298,0.1333,0.1368,0.1404,0.1439,0.1474,0.1509,0.1544,0.1579,0.1614,0.1649,0.1684,0.1719,0.1754,0.1789,0.1825,0.186,0.1895,0.193,0.1965,0.2,0.2035,0.207,0.2105,0.214,0.2175,0.2211,0.2246,0.2281,0.2316,0.2351,0.2386,0.2421,0.2456,0.2491,0.2526,0.2561,0.2596,0.2632,0.2667,0.2702,0.2737,0.2772,0.2807,0.2842,0.2877,0.2912,0.2947,0.2982,0.3018,0.3053,0.3088,0.3123,0.3158,0.3193,0.3228,0.3263,0.3298,0.3333,0.3368,0.3404,0.3439,0.3474,0.3509,0.3544,0.3579,0.3614,0.3649,0.3684,0.3719,0.3754,0.3789,0.3825,0.386,0.3895,0.393,0.3965,0.4,0.4035,0.407,0.4105,0.414,0.4175,0.4211,0.4246,0.4281,0.4316,0.4351,0.4386,0.4421,0.4456,0.4491,0.4526,0.4561,0.4596,0.4632,0.4667,0.4702,0.4737,0.4772,0.4807,0.4842,0.4877,0.4912,0.4947,0.4982,0.5018,0.5053,0.5088,0.5123,0.5158,0.5193,0.5228,0.5263,0.5298,0.5333,0.5368,0.5404,0.5439,0.5474,0.5509,0.5544,0.5579,0.5614,0.5649,0.5684,0.5719,0.5754,0.5789,0.5825,0.586,0.5895,0.593,0.5965,0.6,0.6035,0.607,0.6105,0.614,0.6175,0.6211,0.6246,0.6281,0.6316,0.6351,0.6386,0.6421,0.6456,0.6491,0.6526,0.6561,0.6596,0.6632,0.6667,0.6702,0.6737,0.6772,0.6807,0.6842,0.6877,0.6912,0.6947,0.6982,0.7018,0.7053,0.7088,0.7123,0.7158,0.7193,0.7228,0.7263,0.7298,0.7333,0.7368,0.7404,0.7439,0.7474,0.7509,0.7544,0.7579,0.7614,0.7649,0.7684,0.7719,0.7754,0.7789,0.7825,0.786,0.7895,0.793,0.7965,0.8,0.8035,0.807,0.8105,0.814,0.8175,0.8211,0.8246,0.8281,0.8316,0.8351,0.8386,0.8421,0.8456,0.8491,0.8526,0.8561,0.8596,0.8632,0.8667,0.8702,0.8737,0.8772,0.8807,0.8842,0.8877,0.8912,0.8947,0.8982,0.9018,0.9053,0.9088,0.9123,0.9158,0.9193,0.9228,0.9263,0.9298,0.9333,0.9368,0.9404,0.9439,0.9474,0.9509,0.9544,0.9579,0.9614,0.9649,0.9684,0.9719,0.9754,0.9789,0.9825,0.986,0.9895,0.993,0.9965,1]

Group313.children.append(OrientationInterpolator326)
#Euler angle triplet values, CHANNELS Zrotation Xrotation Yrotation, with min/max ranges [-4.885964,17.54318], [-13.573542,13.69133], [-5.606315,10.062532] degrees
#-1.317750 -1.286104 -0.673492, -1.301316 -1.366098 -0.701196, -1.470395 -1.454794 -0.724041, -1.470395 -1.454794 -0.724041, -1.509849 -1.297974 -0.713856, -1.472780 -1.115783 -0.781199, -1.419042 -1.013363 -0.876688, -1.461995 -0.845389 -1.021629, -1.409099 -0.827931 -1.236261, -1.356436 -0.810885 -1.451107, -1.051746 -0.936286 -1.733474, -0.749921 -1.117671 -2.045724, -0.279234 -1.417705 -2.359331, 0.285132 -1.735062 -2.795323, 0.894825 -1.949656 -2.883907, 1.626820 -2.362706 -2.969104, 2.369530 -2.706624 -3.036180, 3.110428 -3.068982 -2.940533, 3.842908 -3.478372 -2.814568, 4.538624 -4.029786 -2.715255, 5.354771 -4.616504 -2.513999, 6.407552 -5.413402 -2.201791, 7.620510 -6.301512 -1.799806, 8.407479 -6.964830 -1.502154, 8.889326 -7.622513 -1.208806, 9.170975 -8.122870 -0.999575, 9.449203 -8.477419 -0.949279, 9.726587 -8.784123 -0.848442, 9.900585 -8.907694 -0.704670, 10.197036 -8.752707 -0.635539, 10.463896 -8.448426 -0.464976, 10.804849 -8.169545 -0.122982, 11.260267 -7.960663 0.240736, 11.639968 -7.608035 0.281475, 12.080660 -7.138828 0.272176, 12.360570 -6.480808 0.108157, 12.754566 -5.587594 -0.038693, 13.122949 -4.719154 -0.127954, 13.683297 -3.983242 -0.074007, 14.256371 -3.189939 -0.018042, 14.725115 -2.523887 -0.057812, 15.164227 -1.653351 -0.009166, 15.455572 -0.618176 -0.112255, 15.764572 0.204643 -0.206643, 16.046377 0.719395 -0.078635, 16.320629 1.095314 -0.131712, 16.493528 1.409999 -0.206781, 16.630131 1.658316 -0.391475, 16.595665 2.045549 -0.492775, 16.314447 2.605448 -0.614835, 15.888074 3.305167 -0.704329, 15.231986 4.013544 -0.661347, 14.490420 4.750102 -0.497663, 13.513572 5.455311 -0.455753, 12.540332 6.193209 -0.416238, 11.617925 6.889326 -0.371693, 10.723685 7.668816 -0.293911, 9.883469 8.482862 -0.208570, 9.351080 9.287950 0.080379, 8.889342 9.874573 0.424272, 8.374214 10.506554 0.977674, 7.802840 10.978165 1.361279, 7.154949 11.528626 1.650022, 6.450048 12.024899 1.835587, 5.432131 12.794387 1.894085, 4.139839 13.562000 1.887544, 3.029183 13.691330 1.788305, 2.306018 13.478493 1.546627, 1.770693 13.049044 1.141016, 1.431640 12.465671 0.616305, 0.880265 11.605193 0.209509, 0.505662 10.826180 -0.144145, 0.356421 10.238907 -0.424859, 0.518413 9.644545 -0.766174, 0.671140 9.002534 -0.919672, 0.873507 8.521063 -1.101667, 1.431693 7.992437 -1.404773, 1.847027 7.602446 -1.695277, 2.114698 7.053100 -1.944912, 2.300323 6.522215 -2.099638, 2.504880 6.078806 -2.183403, 2.718434 5.561996 -2.131409, 2.911888 5.168576 -1.964713, 3.172235 4.820767 -1.584038, 3.612932 4.606969 -1.225020, 4.134538 4.327429 -0.905039, 4.940413 4.139500 -0.603500, 5.819566 3.974660 -0.078068, 6.680144 3.994943 0.633699, 7.620382 3.966140 1.306709, 8.498429 3.916367 1.927404, 9.242581 3.907996 2.581699, 9.970401 3.717489 3.205885, 10.444104 3.680554 3.770159, 11.008425 3.552119 4.270124, 11.306034 3.129151 4.542667, 11.378166 2.681438 4.488688, 11.297236 2.275906 4.436393, 11.047242 1.741632 4.522133, 10.858277 1.271034 4.648258, 10.618443 0.737370 4.823961, 10.383893 0.165068 4.963023, 9.844585 -0.483513 4.935708, 9.199865 -1.318277 4.922706, 8.500084 -2.090997 4.754916, 7.904191 -2.760776 4.642013, 7.443771 -3.648649 4.500817, 7.089857 -4.422847 4.579883, 6.903844 -5.319279 4.672275, 6.675500 -6.262482 4.571021, 6.617200 -6.994934 4.576626, 6.552776 -7.585517 4.446744, 6.809133 -8.183872 4.535035, 7.174241 -8.424410 4.684320, 7.861928 -8.131747 4.949130, 8.576159 -7.393561 5.402057, 9.246359 -6.236637 5.954513, 9.507273 -4.599198 6.548679, 9.498481 -2.353955 6.982546, 9.319865 0.478314 7.241063, 9.419635 3.419379 7.271118, 9.925582 5.534717 7.104541, 10.114864 6.466743 6.703916, 9.681649 6.330032 6.330076, 8.896881 5.618188 5.814156, 7.962525 4.458812 5.127316, 7.013669 3.060812 4.241195, 6.171081 1.507370 3.115254, 5.390015 -0.107223 1.894620, 4.740378 -1.646376 0.731115, 4.173450 -2.960495 -0.318324, 3.786493 -4.002096 -1.134783, 3.613938 -4.626791 -1.591173, 3.818410 -4.863667 -1.749537, 4.298348 -4.781960 -1.672569, 4.963531 -4.341569 -1.550394, 5.784306 -3.600552 -1.447909, 6.638031 -2.704159 -1.199341, 7.434775 -1.554422 -0.973503, 8.227912 -0.119353 -0.536070, 9.055745 1.278209 -0.222259, 9.863111 2.744109 -0.000429, 10.498290 4.330005 0.326086, 11.171907 5.988620 0.549250, 11.577847 7.440228 0.626547, 11.914284 8.714038 0.807428, 12.251301 9.672551 0.756265, 12.637959 9.612482 1.007672, 12.809380 9.505831 1.201641, 12.687813 9.219806 1.378329, 12.175011 8.890397 1.490046, 11.471625 8.812018 1.127861, 10.375776 9.104897 0.658446, 9.123167 9.446597 0.460066, 8.215046 9.907144 0.148232, 7.559227 10.196490 -0.306956, 6.838316 10.239646 -0.776556, 6.019483 9.790719 -1.343534, 5.035826 9.180264 -2.242138, 4.039029 8.363939 -3.061777, 3.119660 7.513804 -3.566264, 2.228949 6.495920 -3.679926, 1.349195 5.440307 -3.703081, 0.511199 4.234894 -3.559468, -0.392168 3.177160 -3.589142, -1.123112 2.277934 -3.846636, -1.858735 1.448142 -4.342416, -2.536751 0.676912 -4.681822, -3.339742 -0.157818 -5.116310, -3.890090 -0.848718 -5.345763, -4.251044 -1.513370 -5.458125, -4.664247 -2.046347 -5.551929, -4.885964 -2.584211 -5.606315, -4.823501 -3.201179 -5.572124, -4.700454 -3.988425 -5.487072, -4.538981 -4.710719 -5.387578, -4.278247 -5.482764 -5.334987, -4.028649 -6.260990 -5.327360, -3.853309 -6.919966 -5.345525, -3.606238 -7.637842 -5.197511, -3.393920 -8.385533 -5.027195, -3.133918 -9.123260 -4.855946, -2.908099 -9.890314 -4.576361, -2.549343 -10.644463 -4.113063, -2.116698 -11.262376 -3.652643, -1.593019 -11.886368 -3.196653, -1.079651 -12.473793 -2.757426, -0.315335 -12.986735 -2.361969, 0.517664 -13.344446 -2.078495, 1.485644 -13.573542 -1.645152, 2.452726 -13.558006 -1.097401, 3.479110 -13.230721 -0.342357, 4.316785 -12.424053 0.338495, 5.050070 -11.149442 1.151996, 5.665052 -9.262166 1.979836, 6.085854 -6.545461 3.110768, 6.129504 -3.029195 4.318870, 5.807889 1.305168 5.822650, 5.287465 6.043375 7.598718, 4.585683 10.110108 9.298064, 3.957167 12.598308 10.062532, 3.378385 13.521317 9.831505, 2.914748 13.413976 8.835750, 2.332890 12.508270 7.341935, 1.517504 11.234125 5.733371, 0.651414 9.627780 4.001714, 0.228014 7.971572 2.215487, 0.141780 6.143533 0.809635, 0.299285 4.342711 -0.190321, 0.669612 2.492214 -0.753489, 1.178723 0.833233 -0.989867, 1.706523 -0.705873 -0.992464, 2.337172 -1.632025 -0.955941, 3.083950 -2.188865 -0.906695, 3.861870 -2.467827 -0.978689, 4.679349 -2.523208 -0.990469, 5.387169 -2.171344 -1.033294, 6.339836 -1.542066 -0.845114, 7.396822 -0.447090 -0.396716, 8.545075 0.844467 0.128434, 9.753472 2.202303 0.682547, 11.181789 3.552458 1.048301, 12.674907 4.946613 1.214100, 14.274346 6.537369 1.152441, 15.699834 8.147604 1.303106, 16.742702 9.412205 1.764866, 17.402830 10.136873 2.253747, 17.543180 10.462035 2.499675, 17.277468 10.364061 2.274741, 16.705217 10.234032 1.819370, 16.020954 10.164732 0.974725, 14.906523 10.599236 0.100861, 13.315224 11.150566 -0.404945, 11.470420 11.656442 -0.704190, 9.485150 12.241196 -0.747093, 7.499157 12.358516 -0.883603, 5.932466 12.112839 -1.270013, 4.735602 11.667559 -1.859331, 3.758507 11.074418 -2.547009, 2.947488 10.411109 -3.238325, 2.323493 9.571927 -3.863721, 1.587483 8.659679 -4.319242, 0.906702 7.712152 -4.552758, 0.409680 6.730122 -4.593793, -0.030807 5.844223 -4.552019, -0.390870 4.885818 -4.570259, -0.697199 4.083123 -4.582325, -0.934505 3.153200 -4.624654, -1.167557 2.434355 -4.737428, -1.248823 1.869413 -4.968577, -1.939281 1.163576 -5.135688, -2.463104 0.632156 -5.099645, -2.730061 -0.054328 -4.989577, -2.726495 -0.665604 -4.695340, -2.639529 -1.260933 -4.322954, -2.511816 -1.683985 -3.860152, -2.386370 -2.094701 -3.552798, -2.140466 -2.718519 -3.450499, -2.064105 -3.293092 -3.427168, -1.969081 -3.931649 -3.544216, -1.988227 -4.652641 -3.745245, -2.098744 -5.309823 -3.953784, -2.243910 -5.972004 -4.123403, -2.013474 -6.609069 -4.312143, -1.889931 -7.330645 -4.460405, -1.814851 -7.978594 -4.617666, -1.775134 -8.668216 -4.898819, -1.743260 -9.381310 -4.933229, -1.601035 -10.088511 -5.073495, -1.459099 -10.639513 -5.119811, -1.281313 -11.081793 -5.019835, -1.013646 -11.509042 -4.831505, -0.670544 -11.855889 -4.626600, -0.183342 -12.093885 -4.475757, 0.452800 -12.304103 -4.153394, 1.248503 -12.319628 -3.821081, 2.148047 -12.304000 -3.397958, 3.255216 -12.090082 -2.713717, 4.530641 -11.855759 -1.849761, 5.767203 -11.449569 -0.931998, 6.884411 -10.986089 0.067133, 7.923868 -10.224658 1.000889, 8.651861 -9.168123 1.964750, 9.196260 -7.910711 2.750803, 9.459954 -6.447221 3.540138, 9.337306 -4.615580 4.261023
#Interpolator9_r_midtarsal channels [27..29] sends animation values to BVH JOINT RightAnkleEnd, DEF BvhConversion1_r_midtarsal, <HAnimJoint name=r_midtarsal/>
OrientationInterpolator327 = x3d.OrientationInterpolator()
OrientationInterpolator327.DEF = "Interpolator9_r_midtarsal"
OrientationInterpolator327.key = [0,0.0035,0.007,0.0105,0.014,0.0175,0.0211,0.0246,0.0281,0.0316,0.0351,0.0386,0.0421,0.0456,0.0491,0.0526,0.0561,0.0596,0.0632,0.0667,0.0702,0.0737,0.0772,0.0807,0.0842,0.0877,0.0912,0.0947,0.0982,0.1018,0.1053,0.1088,0.1123,0.1158,0.1193,0.1228,0.1263,0.1298,0.1333,0.1368,0.1404,0.1439,0.1474,0.1509,0.1544,0.1579,0.1614,0.1649,0.1684,0.1719,0.1754,0.1789,0.1825,0.186,0.1895,0.193,0.1965,0.2,0.2035,0.207,0.2105,0.214,0.2175,0.2211,0.2246,0.2281,0.2316,0.2351,0.2386,0.2421,0.2456,0.2491,0.2526,0.2561,0.2596,0.2632,0.2667,0.2702,0.2737,0.2772,0.2807,0.2842,0.2877,0.2912,0.2947,0.2982,0.3018,0.3053,0.3088,0.3123,0.3158,0.3193,0.3228,0.3263,0.3298,0.3333,0.3368,0.3404,0.3439,0.3474,0.3509,0.3544,0.3579,0.3614,0.3649,0.3684,0.3719,0.3754,0.3789,0.3825,0.386,0.3895,0.393,0.3965,0.4,0.4035,0.407,0.4105,0.414,0.4175,0.4211,0.4246,0.4281,0.4316,0.4351,0.4386,0.4421,0.4456,0.4491,0.4526,0.4561,0.4596,0.4632,0.4667,0.4702,0.4737,0.4772,0.4807,0.4842,0.4877,0.4912,0.4947,0.4982,0.5018,0.5053,0.5088,0.5123,0.5158,0.5193,0.5228,0.5263,0.5298,0.5333,0.5368,0.5404,0.5439,0.5474,0.5509,0.5544,0.5579,0.5614,0.5649,0.5684,0.5719,0.5754,0.5789,0.5825,0.586,0.5895,0.593,0.5965,0.6,0.6035,0.607,0.6105,0.614,0.6175,0.6211,0.6246,0.6281,0.6316,0.6351,0.6386,0.6421,0.6456,0.6491,0.6526,0.6561,0.6596,0.6632,0.6667,0.6702,0.6737,0.6772,0.6807,0.6842,0.6877,0.6912,0.6947,0.6982,0.7018,0.7053,0.7088,0.7123,0.7158,0.7193,0.7228,0.7263,0.7298,0.7333,0.7368,0.7404,0.7439,0.7474,0.7509,0.7544,0.7579,0.7614,0.7649,0.7684,0.7719,0.7754,0.7789,0.7825,0.786,0.7895,0.793,0.7965,0.8,0.8035,0.807,0.8105,0.814,0.8175,0.8211,0.8246,0.8281,0.8316,0.8351,0.8386,0.8421,0.8456,0.8491,0.8526,0.8561,0.8596,0.8632,0.8667,0.8702,0.8737,0.8772,0.8807,0.8842,0.8877,0.8912,0.8947,0.8982,0.9018,0.9053,0.9088,0.9123,0.9158,0.9193,0.9228,0.9263,0.9298,0.9333,0.9368,0.9404,0.9439,0.9474,0.9509,0.9544,0.9579,0.9614,0.9649,0.9684,0.9719,0.9754,0.9789,0.9825,0.986,0.9895,0.993,0.9965,1]

Group313.children.append(OrientationInterpolator327)
#Unchanging Euler angle triplet values, CHANNELS Zrotation Xrotation Yrotation, with min/max ranges [0.0,4.9E-324], [0.0,4.9E-324], [0.0,4.9E-324] degrees
#0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000, 0.000000 0.000000 0.000000
#Interpolator10_vl5 channels [30..32] sends animation values to BVH JOINT Chest, DEF BvhConversion1_vl5, <HAnimJoint name=vl5/>
OrientationInterpolator328 = x3d.OrientationInterpolator()
OrientationInterpolator328.DEF = "Interpolator10_vl5"
OrientationInterpolator328.key = [0,0.0035,0.007,0.0105,0.014,0.0175,0.0211,0.0246,0.0281,0.0316,0.0351,0.0386,0.0421,0.0456,0.0491,0.0526,0.0561,0.0596,0.0632,0.0667,0.0702,0.0737,0.0772,0.0807,0.0842,0.0877,0.0912,0.0947,0.0982,0.1018,0.1053,0.1088,0.1123,0.1158,0.1193,0.1228,0.1263,0.1298,0.1333,0.1368,0.1404,0.1439,0.1474,0.1509,0.1544,0.1579,0.1614,0.1649,0.1684,0.1719,0.1754,0.1789,0.1825,0.186,0.1895,0.193,0.1965,0.2,0.2035,0.207,0.2105,0.214,0.2175,0.2211,0.2246,0.2281,0.2316,0.2351,0.2386,0.2421,0.2456,0.2491,0.2526,0.2561,0.2596,0.2632,0.2667,0.2702,0.2737,0.2772,0.2807,0.2842,0.2877,0.2912,0.2947,0.2982,0.3018,0.3053,0.3088,0.3123,0.3158,0.3193,0.3228,0.3263,0.3298,0.3333,0.3368,0.3404,0.3439,0.3474,0.3509,0.3544,0.3579,0.3614,0.3649,0.3684,0.3719,0.3754,0.3789,0.3825,0.386,0.3895,0.393,0.3965,0.4,0.4035,0.407,0.4105,0.414,0.4175,0.4211,0.4246,0.4281,0.4316,0.4351,0.4386,0.4421,0.4456,0.4491,0.4526,0.4561,0.4596,0.4632,0.4667,0.4702,0.4737,0.4772,0.4807,0.4842,0.4877,0.4912,0.4947,0.4982,0.5018,0.5053,0.5088,0.5123,0.5158,0.5193,0.5228,0.5263,0.5298,0.5333,0.5368,0.5404,0.5439,0.5474,0.5509,0.5544,0.5579,0.5614,0.5649,0.5684,0.5719,0.5754,0.5789,0.5825,0.586,0.5895,0.593,0.5965,0.6,0.6035,0.607,0.6105,0.614,0.6175,0.6211,0.6246,0.6281,0.6316,0.6351,0.6386,0.6421,0.6456,0.6491,0.6526,0.6561,0.6596,0.6632,0.6667,0.6702,0.6737,0.6772,0.6807,0.6842,0.6877,0.6912,0.6947,0.6982,0.7018,0.7053,0.7088,0.7123,0.7158,0.7193,0.7228,0.7263,0.7298,0.7333,0.7368,0.7404,0.7439,0.7474,0.7509,0.7544,0.7579,0.7614,0.7649,0.7684,0.7719,0.7754,0.7789,0.7825,0.786,0.7895,0.793,0.7965,0.8,0.8035,0.807,0.8105,0.814,0.8175,0.8211,0.8246,0.8281,0.8316,0.8351,0.8386,0.8421,0.8456,0.8491,0.8526,0.8561,0.8596,0.8632,0.8667,0.8702,0.8737,0.8772,0.8807,0.8842,0.8877,0.8912,0.8947,0.8982,0.9018,0.9053,0.9088,0.9123,0.9158,0.9193,0.9228,0.9263,0.9298,0.9333,0.9368,0.9404,0.9439,0.9474,0.9509,0.9544,0.9579,0.9614,0.9649,0.9684,0.9719,0.9754,0.9789,0.9825,0.986,0.9895,0.993,0.9965,1]

Group313.children.append(OrientationInterpolator328)
#Jittery Euler angle triplet values, CHANNELS Zrotation Xrotation Yrotation, with min/max ranges [-3.0E-6,2.0E-6], [-2.0E-6,1.0E-6], [-2.0E-6,2.0E-6] degrees
#0.000000 -0.000000 -0.000001, 0.000000 -0.000000 -0.000001, 0.000000 -0.000000 -0.000001, 0.000000 -0.000000 -0.000001, 0.000000 -0.000000 -0.000001, 0.000000 -0.000000 -0.000001, 0.000000 -0.000000 -0.000001, 0.000000 -0.000000 -0.000001, 0.000000 -0.000000 0.000001, 0.000000 0.000000 0.000000, -0.000000 0.000000 0.000000, -0.000001 -0.000001 0.000000, -0.000000 -0.000001 -0.000000, -0.000002 -0.000001 0.000001, -0.000001 -0.000001 0.000001, 0.000001 -0.000001 -0.000000, -0.000000 -0.000000 0.000000, -0.000000 -0.000001 -0.000000, 0.000000 -0.000000 -0.000000, -0.000000 -0.000000 -0.000000, 0.000002 -0.000000 -0.000000, -0.000002 -0.000000 0.000000, 0.000000 -0.000000 0.000001, -0.000001 -0.000001 0.000000, -0.000000 -0.000000 -0.000001, -0.000002 -0.000001 0.000000, -0.000000 -0.000000 0.000001, -0.000002 -0.000000 -0.000000, -0.000002 -0.000000 -0.000000, 0.000000 -0.000000 0.000000, 0.000001 -0.000000 0.000001, -0.000003 -0.000001 0.000002, -0.000001 -0.000001 0.000001, 0.000001 -0.000000 0.000000, 0.000001 -0.000001 0.000002, -0.000001 0.000000 0.000000, -0.000000 -0.000001 0.000001, -0.000000 -0.000000 0.000001, -0.000002 0.000000 -0.000001, -0.000001 -0.000001 0.000001, -0.000001 -0.000000 0.000000, -0.000001 0.000000 -0.000001, 0.000000 -0.000001 0.000000, 0.000000 -0.000000 0.000001, -0.000001 -0.000000 -0.000000, 0.000001 -0.000000 0.000000, 0.000002 -0.000001 -0.000000, 0.000001 -0.000001 -0.000000, -0.000000 -0.000001 -0.000001, -0.000002 -0.000000 -0.000000, -0.000000 -0.000000 -0.000001, -0.000001 -0.000001 0.000001, -0.000001 -0.000000 0.000001, -0.000000 -0.000001 0.000001, 0.000001 -0.000000 -0.000000, -0.000002 -0.000000 -0.000001, -0.000002 0.000000 -0.000001, -0.000000 -0.000000 0.000001, 0.000000 -0.000000 -0.000000, 0.000001 -0.000001 -0.000001, -0.000000 -0.000001 0.000001, 0.000001 -0.000001 0.000001, 0.000001 -0.000001 0.000001, -0.000001 -0.000001 -0.000001, -0.000001 -0.000001 -0.000001, 0.000000 0.000000 -0.000001, 0.000001 -0.000000 -0.000001, -0.000000 -0.000001 0.000001, -0.000001 0.000000 -0.000001, 0.000001 -0.000001 0.000001, -0.000001 0.000000 0.000001, 0.000001 0.000000 -0.000000, -0.000002 -0.000001 0.000000, 0.000001 -0.000000 -0.000000, -0.000001 -0.000001 0.000001, -0.000000 -0.000000 0.000001, -0.000001 -0.000001 0.000000, 0.000000 -0.000001 -0.000000, -0.000000 -0.000000 0.000001, -0.000002 -0.000001 0.000001, 0.000001 -0.000001 0.000001, -0.000001 -0.000001 0.000000, 0.000001 -0.000000 0.000000, -0.000000 -0.000001 0.000000, -0.000002 -0.000001 0.000000, -0.000001 -0.000000 0.000001, 0.000001 -0.000000 -0.000000, -0.000002 -0.000000 -0.000000, 0.000002 -0.000000 -0.000000, -0.000001 -0.000001 -0.000000, -0.000001 -0.000000 -0.000000, -0.000002 -0.000000 0.000001, -0.000000 -0.000001 -0.000000, -0.000001 -0.000000 -0.000001, -0.000001 -0.000001 0.000001, -0.000001 -0.000000 -0.000000, 0.000000 -0.000000 -0.000001, -0.000001 -0.000000 -0.000000, -0.000001 -0.000000 -0.000000, -0.000001 -0.000000 0.000000, -0.000002 0.000000 -0.000001, 0.000000 -0.000000 -0.000000, -0.000000 -0.000000 0.000000, -0.000001 -0.000001 0.000002, 0.000000 0.000000 -0.000000, 0.000001 -0.000000 -0.000001, -0.000001 -0.000000 0.000000, -0.000000 -0.000001 0.000000, -0.000000 -0.000001 -0.000001, -0.000000 -0.000001 -0.000001, -0.000000 -0.000001 -0.000001, -0.000000 -0.000001 -0.000001, -0.000001 -0.000001 -0.000000, 0.000000 -0.000000 0.000001, -0.000002 -0.000000 -0.000000, 0.000000 -0.000001 0.000001, 0.000000 -0.000000 0.000000, 0.000001 0.000000 -0.000000, -0.000002 -0.000000 0.000000, -0.000000 -0.000001 0.000001, -0.000000 -0.000001 0.000000, 0.000000 -0.000000 -0.000001, 0.000001 -0.000001 -0.000000, -0.000002 0.000000 -0.000001, -0.000002 -0.000001 0.000000, -0.000001 -0.000001 0.000000, 0.000001 0.000000 -0.000001, -0.000000 -0.000001 0.000000, 0.000001 -0.000000 0.000000, -0.000001 -0.000001 0.000002, -0.000000 -0.000001 0.000000, 0.000000 -0.000000 0.000000, -0.000002 -0.000001 0.000001, 0.000000 0.000001 -0.000000, -0.000001 -0.000001 0.000001, -0.000000 0.000000 -0.000000, -0.000001 -0.000001 -0.000000, -0.000000 -0.000000 0.000000, -0.000002 -0.000000 0.000001, -0.000001 -0.000001 0.000000, 0.000000 -0.000001 0.000001, -0.000000 0.000000 -0.000000, -0.000000 -0.000001 0.000000, -0.000001 -0.000000 -0.000000, -0.000000 -0.000001 -0.000001, 0.000001 -0.000000 0.000001, -0.000000 0.000000 0.000001, -0.000003 -0.000000 0.000001, -0.000001 -0.000001 0.000001, 0.000001 -0.000000 0.000000, -0.000001 -0.000000 0.000001, -0.000000 -0.000001 0.000000, 0.000000 0.000000 -0.000001, -0.000000 -0.000001 0.000001, -0.000001 -0.000001 0.000001, -0.000003 -0.000001 0.000000, 0.000000 -0.000001 0.000000, -0.000001 -0.000000 0.000001, -0.000001 -0.000001 0.000000, 0.000000 -0.000001 -0.000001, -0.000003 -0.000002 0.000001, 0.000001 -0.000002 0.000000, -0.000001 -0.000001 -0.000002, 0.000001 -0.000000 0.000001, -0.000000 -0.000001 -0.000000, -0.000001 -0.000000 -0.000001, -0.000001 -0.000001 -0.000000, 0.000000 -0.000000 -0.000001, -0.000000 -0.000000 -0.000001, -0.000002 -0.000001 0.000000, 0.000000 0.000001 -0.000001, -0.000001 -0.000000 0.000000, -0.000000 -0.000000 0.000001, 0.000000 0.000000 0.000001, -0.000002 -0.000001 0.000001, -0.000001 0.000001 -0.000001, -0.000001 -0.000001 0.000000, 0.000002 -0.000001 0.000001, -0.000000 0.000000 -0.000001, 0.000000 -0.000001 0.000001, -0.000001 -0.000001 -0.000000, 0.000000 0.000000 -0.000001, -0.000001 -0.000001 0.000001, -0.000000 -0.000000 0.000000, -0.000000 0.000001 -0.000000, -0.000001 -0.000000 0.000001, -0.000002 -0.000001 0.000000, 0.000000 0.000001 0.000000, -0.000001 -0.000001 0.000001, -0.000002 -0.000001 0.000001, -0.000000 -0.000001 0.000001, -0.000000 -0.000000 0.000000, -0.000001 -0.000001 -0.000001, 0.000001 0.000000 0.000001, -0.000000 -0.000000 0.000002, -0.000001 -0.000001 0.000001, 0.000000 0.000000 0.000000, -0.000001 -0.000001 0.000000, 0.000000 -0.000001 0.000001, -0.000002 -0.000001 0.000002, -0.000001 -0.000001 0.000001, 0.000001 -0.000001 0.000001, 0.000001 0.000000 0.000001, -0.000002 -0.000001 -0.000000, -0.000002 -0.000001 0.000001, 0.000000 -0.000001 0.000001, -0.000002 -0.000001 -0.000000, 0.000001 0.000000 -0.000000, 0.000001 0.000001 0.000002, 0.000000 -0.000001 -0.000000, -0.000001 -0.000000 0.000001, -0.000000 0.000001 -0.000000, -0.000001 -0.000000 -0.000001, -0.000002 -0.000001 0.000001, 0.000001 -0.000001 -0.000000, -0.000001 -0.000001 0.000001, -0.000001 -0.000001 -0.000000, 0.000001 0.000001 -0.000002, 0.000001 -0.000001 -0.000000, -0.000002 0.000000 -0.000000, 0.000000 -0.000001 0.000001, -0.000001 0.000001 -0.000000, 0.000001 -0.000001 -0.000000, -0.000001 -0.000000 -0.000001, 0.000000 -0.000000 0.000000, -0.000001 -0.000002 0.000002, 0.000001 0.000001 -0.000000, 0.000000 0.000000 -0.000001, 0.000001 0.000000 0.000000, -0.000000 -0.000000 0.000001, -0.000002 -0.000001 0.000000, 0.000001 -0.000001 -0.000002, -0.000000 -0.000000 0.000000, -0.000000 0.000001 -0.000001, -0.000000 -0.000001 0.000000, -0.000002 -0.000000 0.000000, -0.000000 -0.000001 -0.000000, -0.000001 0.000000 0.000000, -0.000003 -0.000002 -0.000000, -0.000002 -0.000001 0.000001, -0.000002 -0.000000 0.000000, -0.000000 -0.000001 0.000001, -0.000002 -0.000001 -0.000001, 0.000001 -0.000001 0.000001, 0.000002 -0.000000 0.000000, 0.000002 -0.000000 0.000000, 0.000002 -0.000000 0.000000, 0.000000 -0.000001 0.000001, -0.000000 0.000000 0.000001, -0.000000 0.000000 -0.000001, 0.000001 -0.000001 0.000000, -0.000001 -0.000002 -0.000001, -0.000001 -0.000000 0.000000, 0.000001 -0.000000 -0.000001, -0.000001 -0.000001 0.000001, -0.000001 -0.000001 0.000002, -0.000001 -0.000001 -0.000000, -0.000000 -0.000001 0.000001, 0.000000 -0.000000 -0.000000, -0.000001 -0.000002 0.000002, -0.000000 -0.000000 0.000002, -0.000001 -0.000000 0.000000, 0.000000 0.000000 -0.000001, -0.000001 -0.000001 -0.000000, -0.000002 -0.000001 0.000001, -0.000001 -0.000001 0.000001, 0.000000 -0.000001 -0.000000, -0.000001 -0.000001 -0.000000, 0.000001 -0.000000 -0.000000, -0.000001 0.000000 -0.000001, -0.000000 0.000001 0.000000, -0.000000 -0.000001 -0.000001, -0.000001 -0.000001 -0.000000, -0.000000 -0.000001 0.000001, -0.000001 -0.000001 0.000001, -0.000001 0.000000 -0.000001, -0.000001 -0.000000 0.000000, -0.000000 0.000000 -0.000000, 0.000001 -0.000000 -0.000000, 0.000000 -0.000002 0.000002, -0.000000 -0.000000 0.000000, 0.000001 -0.000001 0.000001, 0.000001 0.000000 0.000001, -0.000001 -0.000000 -0.000000, -0.000000 -0.000001 -0.000000, -0.000001 0.000000 0.000000
#Interpolator11_Chest2 channels [33..35] sends animation values to BVH JOINT Chest2, DEF BvhConversion1_Chest2, <HAnimJoint name=Chest2/>
OrientationInterpolator329 = x3d.OrientationInterpolator()
OrientationInterpolator329.DEF = "Interpolator11_Chest2"
OrientationInterpolator329.key = [0,0.0035,0.007,0.0105,0.014,0.0175,0.0211,0.0246,0.0281,0.0316,0.0351,0.0386,0.0421,0.0456,0.0491,0.0526,0.0561,0.0596,0.0632,0.0667,0.0702,0.0737,0.0772,0.0807,0.0842,0.0877,0.0912,0.0947,0.0982,0.1018,0.1053,0.1088,0.1123,0.1158,0.1193,0.1228,0.1263,0.1298,0.1333,0.1368,0.1404,0.1439,0.1474,0.1509,0.1544,0.1579,0.1614,0.1649,0.1684,0.1719,0.1754,0.1789,0.1825,0.186,0.1895,0.193,0.1965,0.2,0.2035,0.207,0.2105,0.214,0.2175,0.2211,0.2246,0.2281,0.2316,0.2351,0.2386,0.2421,0.2456,0.2491,0.2526,0.2561,0.2596,0.2632,0.2667,0.2702,0.2737,0.2772,0.2807,0.2842,0.2877,0.2912,0.2947,0.2982,0.3018,0.3053,0.3088,0.3123,0.3158,0.3193,0.3228,0.3263,0.3298,0.3333,0.3368,0.3404,0.3439,0.3474,0.3509,0.3544,0.3579,0.3614,0.3649,0.3684,0.3719,0.3754,0.3789,0.3825,0.386,0.3895,0.393,0.3965,0.4,0.4035,0.407,0.4105,0.414,0.4175,0.4211,0.4246,0.4281,0.4316,0.4351,0.4386,0.4421,0.4456,0.4491,0.4526,0.4561,0.4596,0.4632,0.4667,0.4702,0.4737,0.4772,0.4807,0.4842,0.4877,0.4912,0.4947,0.4982,0.5018,0.5053,0.5088,0.5123,0.5158,0.5193,0.5228,0.5263,0.5298,0.5333,0.5368,0.5404,0.5439,0.5474,0.5509,0.5544,0.5579,0.5614,0.5649,0.5684,0.5719,0.5754,0.5789,0.5825,0.586,0.5895,0.593,0.5965,0.6,0.6035,0.607,0.6105,0.614,0.6175,0.6211,0.6246,0.6281,0.6316,0.6351,0.6386,0.6421,0.6456,0.6491,0.6526,0.6561,0.6596,0.6632,0.6667,0.6702,0.6737,0.6772,0.6807,0.6842,0.6877,0.6912,0.6947,0.6982,0.7018,0.7053,0.7088,0.7123,0.7158,0.7193,0.7228,0.7263,0.7298,0.7333,0.7368,0.7404,0.7439,0.7474,0.7509,0.7544,0.7579,0.7614,0.7649,0.7684,0.7719,0.7754,0.7789,0.7825,0.786,0.7895,0.793,0.7965,0.8,0.8035,0.807,0.8105,0.814,0.8175,0.8211,0.8246,0.8281,0.8316,0.8351,0.8386,0.8421,0.8456,0.8491,0.8526,0.8561,0.8596,0.8632,0.8667,0.8702,0.8737,0.8772,0.8807,0.8842,0.8877,0.8912,0.8947,0.8982,0.9018,0.9053,0.9088,0.9123,0.9158,0.9193,0.9228,0.9263,0.9298,0.9333,0.9368,0.9404,0.9439,0.9474,0.9509,0.9544,0.9579,0.9614,0.9649,0.9684,0.9719,0.9754,0.9789,0.9825,0.986,0.9895,0.993,0.9965,1]

Group313.children.append(OrientationInterpolator329)
#Euler angle triplet values, CHANNELS Zrotation Xrotation Yrotation, with min/max ranges [2.218203,9.295252], [-5.744765,0.519277], [-5.795249,1.398932] degrees
#4.402057 -0.186171 0.790177, 4.478723 -0.156879 0.863166, 4.629217 -0.097192 0.858014, 4.703200 -0.066964 0.779875, 4.703200 -0.066964 0.779875, 4.662544 -0.143323 0.833202, 4.662544 -0.143323 0.833202, 4.588589 -0.173620 0.911243, 4.438109 -0.433936 0.838519, 4.363862 -0.664650 0.838554, 4.414059 -0.840527 0.736381, 4.339954 -0.995229 0.668329, 4.319120 -1.214313 0.585343, 4.334266 -1.359754 0.441576, 4.392553 -1.430067 0.395552, 4.525755 -1.504707 0.323657, 4.572873 -1.525474 0.201755, 4.682803 -1.606527 0.183530, 4.908304 -1.629847 0.155552, 4.988880 -1.836351 0.227820, 4.996583 -1.993829 0.354594, 5.133520 -2.152471 0.351046, 5.114036 -2.407550 0.361169, 5.052392 -2.736780 0.425251, 4.849618 -3.171196 0.563263, 4.434484 -3.521762 0.490232, 3.905134 -3.722769 0.585218, 3.354459 -3.559441 0.641505, 3.009123 -3.417158 0.848907, 2.828121 -3.308028 1.034619, 2.622634 -3.264796 1.026205, 2.612677 -3.327057 0.980406, 2.647847 -3.282472 0.982958, 2.743388 -3.262069 0.865142, 2.855068 -3.226981 0.738408, 2.945652 -3.078419 0.679441, 2.950887 -2.870348 0.569262, 2.874322 -2.595147 0.451221, 2.820196 -2.466802 0.316997, 2.794547 -2.257284 0.219549, 2.668799 -2.128093 0.129003, 2.439979 -2.120088 0.011523, 2.218203 -2.041799 0.026637, 2.282044 -1.909660 0.065231, 2.257226 -1.882756 0.087335, 2.353553 -1.880437 0.161370, 2.463776 -1.701009 0.255761, 2.498967 -1.551251 0.423088, 2.391425 -1.386788 0.634468, 2.348241 -1.260619 0.726233, 2.477405 -1.180052 0.684153, 2.427799 -1.251290 0.690339, 2.582294 -1.402518 0.669298, 2.912531 -1.573686 0.656071, 3.057584 -1.751684 0.623301, 3.329560 -1.767431 0.468958, 3.513710 -1.913962 0.352663, 3.691090 -2.064779 0.321091, 3.838665 -2.503850 0.237199, 4.057460 -2.882351 0.070797, 4.171732 -3.341086 -0.086294, 4.396468 -3.646924 -0.121208, 4.603673 -4.009476 -0.174863, 4.793758 -4.312085 -0.257014, 5.122385 -4.541892 -0.336029, 5.299591 -4.887645 -0.593202, 5.507306 -5.118281 -0.645519, 5.749367 -5.217555 -0.652918, 5.982884 -5.217809 -0.681968, 6.323870 -5.133309 -0.678476, 6.612999 -4.981400 -0.658060, 6.881445 -4.768289 -0.667058, 6.871167 -4.378755 -0.700042, 6.772778 -4.045362 -0.752499, 6.677915 -3.865822 -0.941610, 6.476491 -3.630388 -1.085051, 6.239554 -3.425707 -1.144981, 6.185827 -3.325063 -1.153787, 6.104430 -3.317146 -1.253989, 5.997278 -3.392029 -1.237197, 5.913113 -3.489936 -1.091211, 5.854334 -3.505438 -1.062992, 5.661108 -3.506752 -0.995556, 5.497770 -3.377229 -0.884617, 5.378716 -3.140320 -0.728068, 5.157421 -2.937123 -0.551346, 4.885974 -2.679604 -0.416292, 4.569622 -2.498065 -0.376399, 4.177638 -2.345068 -0.261277, 3.961977 -2.042051 -0.201002, 3.738576 -1.894365 -0.057973, 3.624170 -1.798378 0.042809, 3.495099 -1.697002 0.077933, 3.496558 -1.672023 0.198320, 3.515640 -1.422693 0.276569, 3.667777 -1.169140 0.371975, 3.765724 -1.016806 0.512581, 3.920341 -0.812769 0.573961, 4.030273 -0.510004 0.539783, 4.145746 -0.258177 0.624665, 4.201211 -0.057150 0.637865, 4.329480 0.175448 0.572664, 4.370716 0.350090 0.565730, 4.537511 0.429834 0.546687, 4.721831 0.489953 0.529886, 4.832225 0.519277 0.592507, 4.912196 0.499248 0.480834, 5.082906 0.354567 0.593511, 5.179077 0.330482 0.688141, 5.242682 0.181607 0.684424, 5.233088 0.001126 0.760357, 5.338518 -0.223579 0.934989, 5.462363 -0.547332 0.983271, 5.576736 -1.051315 1.108504, 5.483441 -1.520470 1.224878, 5.289041 -1.999123 1.143354, 5.135651 -2.416131 1.074881, 4.995796 -2.840353 1.061556, 5.033209 -3.120394 1.055494, 5.155205 -3.531426 0.970621, 5.371727 -4.035640 1.061469, 5.542555 -4.540000 0.992469, 5.662943 -4.971137 1.139785, 5.658018 -5.305999 1.217189, 5.488254 -5.541042 1.293880, 5.330250 -5.631423 1.345136, 5.342037 -5.563563 1.339422, 5.212753 -5.387269 1.285955, 5.176992 -5.341320 1.307355, 5.329654 -5.390109 1.378040, 5.478923 -5.404552 1.398802, 5.505744 -5.356523 1.398932, 5.602993 -5.355840 1.342947, 5.646310 -5.305116 1.241658, 5.595007 -5.058480 1.162838, 5.525700 -4.785227 1.109946, 5.550429 -4.513914 0.931911, 5.525831 -4.191284 0.711230, 5.474535 -3.744097 0.493140, 5.520125 -3.449616 0.237017, 5.657898 -3.149689 -0.094114, 5.522863 -3.057105 -0.452485, 5.438924 -3.014384 -0.769541, 5.255813 -3.034200 -1.234387, 5.054962 -2.979579 -1.663094, 4.918183 -3.045109 -2.089749, 4.889932 -3.130440 -2.393942, 4.779879 -3.147252 -2.709745, 4.792907 -3.098903 -2.936939, 4.847289 -3.082189 -3.119649, 4.972471 -3.069002 -3.293398, 5.096990 -3.231999 -3.407823, 5.372615 -3.449912 -3.581756, 5.714266 -3.663921 -3.677143, 6.109418 -3.820156 -3.766061, 6.531622 -3.925422 -3.816352, 7.075651 -4.018960 -3.888094, 7.625281 -4.232808 -3.861474, 8.117542 -4.320102 -3.834175, 8.526807 -4.426292 -3.879082, 8.877321 -4.571868 -3.848541, 8.950728 -4.802744 -3.787304, 8.993618 -4.916131 -3.610522, 8.915234 -4.863470 -3.550111, 8.867402 -4.897415 -3.457015, 8.623735 -4.784697 -3.403749, 8.338463 -4.744702 -3.287909, 8.093285 -4.635686 -3.233956, 7.796551 -4.477564 -3.219040, 7.464719 -4.321651 -3.054358, 7.177411 -4.257331 -2.951286, 6.771517 -4.174781 -2.968420, 6.455653 -4.087351 -2.997811, 6.132526 -3.981930 -2.941145, 5.934195 -3.900283 -2.858441, 5.668583 -3.753207 -2.877625, 5.489099 -3.668459 -2.850046, 5.392918 -3.439897 -2.715072, 5.247714 -3.225771 -2.642065, 5.271165 -3.027111 -2.544789, 5.309134 -2.898151 -2.480929, 5.346152 -2.768960 -2.416963, 5.436082 -2.466350 -2.378137, 5.441107 -2.209118 -2.314255, 5.643582 -2.090184 -2.231609, 5.896869 -2.018351 -2.109601, 6.182817 -2.110676 -1.996040, 6.433427 -2.166632 -1.866282, 6.691852 -2.387234 -1.795649, 6.959707 -2.537551 -1.641164, 7.196839 -2.559272 -1.487007, 7.415610 -2.724001 -1.305868, 7.412840 -2.751299 -1.152641, 7.263327 -2.956017 -0.934682, 7.121138 -3.185543 -0.863880, 6.921338 -3.413514 -0.862911, 6.777133 -3.688155 -0.817894, 6.615073 -3.895984 -0.743125, 6.458181 -4.073265 -0.803296, 6.333712 -4.276905 -0.738781, 6.193375 -4.521794 -0.600074, 5.995072 -4.618899 -0.460037, 5.786554 -4.450161 -0.449080, 5.679955 -4.252769 -0.552148, 5.346255 -4.084150 -0.695206, 5.220811 -3.932833 -0.746891, 5.301045 -3.824624 -0.847871, 5.505827 -3.733725 -0.981913, 5.865232 -3.690484 -1.050060, 6.099125 -3.553282 -1.104480, 6.333254 -3.416208 -1.158672, 6.449774 -3.284521 -1.326833, 6.702696 -3.245079 -1.353850, 6.874091 -3.134524 -1.549652, 7.028601 -3.059713 -1.766010, 7.079490 -2.888471 -1.900556, 7.131717 -2.717318 -2.035092, 7.168347 -2.422119 -2.269503, 7.137736 -2.077061 -2.445766, 7.036667 -1.829638 -2.638465, 7.216371 -1.581371 -2.828041, 7.315426 -1.420081 -3.106580, 7.331500 -1.487704 -3.380696, 7.445872 -1.660243 -3.734898, 7.485161 -1.858811 -4.007570, 7.592699 -2.099391 -4.293893, 7.738723 -2.384583 -4.394373, 7.878698 -2.777434 -4.450738, 7.963329 -3.176705 -4.414506, 8.107144 -3.464062 -4.423725, 8.249045 -3.690606 -4.496744, 8.236495 -3.865059 -4.660498, 8.378910 -4.070444 -4.900025, 8.582920 -4.333920 -5.193913, 8.690132 -4.456332 -5.462017, 8.896700 -4.587132 -5.675740, 8.950214 -4.511830 -5.751550, 9.138797 -4.474470 -5.795249, 9.295252 -4.176188 -5.711937, 9.292179 -3.711156 -5.510511, 9.146390 -3.311964 -5.299591, 9.025323 -3.059313 -4.985888, 8.810046 -2.978467 -4.886987, 8.720442 -2.794694 -4.718201, 8.495645 -2.489004 -4.595787, 8.312654 -2.111255 -4.534008, 8.157905 -1.819558 -4.443178, 8.082167 -1.528365 -4.206567, 7.852209 -1.431674 -3.919532, 7.634152 -1.406958 -3.667405, 7.360437 -1.488465 -3.448609, 7.126264 -1.564124 -3.231678, 6.857116 -1.752551 -3.152920, 6.665640 -1.736408 -3.090013, 6.503744 -1.804815 -2.999997, 6.135383 -1.906622 -2.931878, 5.977570 -1.948863 -2.899751, 5.709022 -2.015229 -2.755878, 5.597874 -1.980319 -2.604991, 5.405196 -1.971581 -2.527001, 5.275399 -1.917414 -2.376544, 5.267339 -1.811810 -2.241513, 5.157399 -1.459494 -2.111982, 5.096413 -1.261243 -1.988797, 5.106020 -1.036104 -1.944117, 5.106460 -1.011206 -1.978775, 5.272214 -1.166571 -1.853562, 5.440166 -1.466968 -1.805965, 5.615829 -1.876326 -1.731301, 5.834872 -2.320533 -1.666905, 6.014890 -2.770764 -1.618493, 6.102346 -3.145177 -1.635248, 6.063274 -3.398108 -1.568036, 6.040443 -3.649932 -1.604125, 5.979887 -3.729775 -1.601091, 5.779100 -3.777425 -1.618032, 5.492800 -3.742582 -1.756076, 5.306452 -3.804505 -1.720576, 5.152643 -4.062173 -1.770902, 5.132722 -4.315338 -1.810155, 5.012444 -4.596441 -1.819182, 4.879487 -4.882478 -1.724971, 4.761608 -5.165064 -1.736394, 4.607664 -5.366444 -1.772395, 4.420866 -5.646972 -1.759458, 4.140108 -5.744765 -1.824507
#Interpolator12_LeftCollar channels [36..38] sends animation values to BVH JOINT LeftCollar, DEF BvhConversion1_LeftCollar, <HAnimJoint name=LeftCollar/>
OrientationInterpolator330 = x3d.OrientationInterpolator()
OrientationInterpolator330.DEF = "Interpolator12_LeftCollar"
OrientationInterpolator330.key = [0,0.0035,0.007,0.0105,0.014,0.0175,0.0211,0.0246,0.0281,0.0316,0.0351,0.0386,0.0421,0.0456,0.0491,0.0526,0.0561,0.0596,0.0632,0.0667,0.0702,0.0737,0.0772,0.0807,0.0842,0.0877,0.0912,0.0947,0.0982,0.1018,0.1053,0.1088,0.1123,0.1158,0.1193,0.1228,0.1263,0.1298,0.1333,0.1368,0.1404,0.1439,0.1474,0.1509,0.1544,0.1579,0.1614,0.1649,0.1684,0.1719,0.1754,0.1789,0.1825,0.186,0.1895,0.193,0.1965,0.2,0.2035,0.207,0.2105,0.214,0.2175,0.2211,0.2246,0.2281,0.2316,0.2351,0.2386,0.2421,0.2456,0.2491,0.2526,0.2561,0.2596,0.2632,0.2667,0.2702,0.2737,0.2772,0.2807,0.2842,0.2877,0.2912,0.2947,0.2982,0.3018,0.3053,0.3088,0.3123,0.3158,0.3193,0.3228,0.3263,0.3298,0.3333,0.3368,0.3404,0.3439,0.3474,0.3509,0.3544,0.3579,0.3614,0.3649,0.3684,0.3719,0.3754,0.3789,0.3825,0.386,0.3895,0.393,0.3965,0.4,0.4035,0.407,0.4105,0.414,0.4175,0.4211,0.4246,0.4281,0.4316,0.4351,0.4386,0.4421,0.4456,0.4491,0.4526,0.4561,0.4596,0.4632,0.4667,0.4702,0.4737,0.4772,0.4807,0.4842,0.4877,0.4912,0.4947,0.4982,0.5018,0.5053,0.5088,0.5123,0.5158,0.5193,0.5228,0.5263,0.5298,0.5333,0.5368,0.5404,0.5439,0.5474,0.5509,0.5544,0.5579,0.5614,0.5649,0.5684,0.5719,0.5754,0.5789,0.5825,0.586,0.5895,0.593,0.5965,0.6,0.6035,0.607,0.6105,0.614,0.6175,0.6211,0.6246,0.6281,0.6316,0.6351,0.6386,0.6421,0.6456,0.6491,0.6526,0.6561,0.6596,0.6632,0.6667,0.6702,0.6737,0.6772,0.6807,0.6842,0.6877,0.6912,0.6947,0.6982,0.7018,0.7053,0.7088,0.7123,0.7158,0.7193,0.7228,0.7263,0.7298,0.7333,0.7368,0.7404,0.7439,0.7474,0.7509,0.7544,0.7579,0.7614,0.7649,0.7684,0.7719,0.7754,0.7789,0.7825,0.786,0.7895,0.793,0.7965,0.8,0.8035,0.807,0.8105,0.814,0.8175,0.8211,0.8246,0.8281,0.8316,0.8351,0.8386,0.8421,0.8456,0.8491,0.8526,0.8561,0.8596,0.8632,0.8667,0.8702,0.8737,0.8772,0.8807,0.8842,0.8877,0.8912,0.8947,0.8982,0.9018,0.9053,0.9088,0.9123,0.9158,0.9193,0.9228,0.9263,0.9298,0.9333,0.9368,0.9404,0.9439,0.9474,0.9509,0.9544,0.9579,0.9614,0.9649,0.9684,0.9719,0.9754,0.9789,0.9825,0.986,0.9895,0.993,0.9965,1]

Group313.children.append(OrientationInterpolator330)
#Euler angle triplet values, CHANNELS Zrotation Xrotation Yrotation, with min/max ranges [-1.0E-6,4.9E-324], [-2.0E-6,1.0E-6], [-6.0E-6,4.0E-6] degrees
#-0.000000 -0.000000 0.000001, -0.000000 -0.000001 0.000004, -0.000000 0.000000 -0.000003, -0.000000 -0.000000 -0.000006, -0.000000 -0.000000 -0.000006, -0.000000 -0.000000 -0.000006, -0.000000 -0.000000 -0.000006, -0.000000 0.000000 -0.000003, -0.000000 -0.000000 -0.000001, -0.000000 0.000001 -0.000001, -0.000000 -0.000001 0.000003, -0.000000 0.000000 0.000001, -0.000000 -0.000000 -0.000004, -0.000001 0.000000 -0.000005, -0.000001 0.000000 -0.000003, -0.000001 0.000000 -0.000000, -0.000001 0.000001 -0.000003, -0.000000 -0.000000 0.000002, -0.000001 -0.000000 -0.000001, 0.000000 0.000000 -0.000002, -0.000001 -0.000000 0.000003, -0.000000 0.000001 -0.000005, -0.000000 -0.000000 -0.000005, -0.000001 0.000000 -0.000001, -0.000001 -0.000001 0.000003, -0.000001 -0.000000 -0.000001, -0.000000 -0.000000 -0.000003, -0.000001 0.000000 -0.000001, -0.000000 0.000000 0.000003, -0.000001 -0.000000 -0.000001, -0.000001 -0.000000 0.000002, -0.000000 0.000000 -0.000001, -0.000001 -0.000001 0.000001, -0.000000 -0.000000 -0.000002, 0.000000 0.000000 -0.000003, -0.000000 -0.000001 0.000002, -0.000000 -0.000000 -0.000002, -0.000000 -0.000000 -0.000003, -0.000000 -0.000000 -0.000002, -0.000000 -0.000000 -0.000001, -0.000000 -0.000000 0.000003, -0.000000 -0.000000 0.000002, -0.000001 -0.000000 -0.000000, -0.000000 -0.000000 -0.000004, -0.000001 -0.000000 -0.000001, -0.000000 -0.000000 -0.000002, -0.000000 -0.000000 -0.000000, -0.000001 -0.000000 0.000003, -0.000001 0.000000 -0.000002, -0.000000 -0.000000 -0.000000, -0.000001 -0.000001 0.000003, -0.000001 -0.000000 0.000001, -0.000000 -0.000000 0.000002, -0.000000 -0.000000 -0.000001, -0.000000 -0.000000 -0.000001, -0.000000 0.000000 -0.000002, -0.000001 -0.000000 -0.000001, 0.000000 -0.000000 -0.000002, -0.000001 0.000000 -0.000005, -0.000000 0.000001 -0.000003, -0.000001 -0.000000 -0.000001, -0.000000 0.000000 -0.000002, -0.000000 -0.000001 -0.000002, -0.000000 0.000000 -0.000001, -0.000000 -0.000001 -0.000000, -0.000001 0.000001 -0.000002, -0.000000 -0.000000 0.000001, -0.000000 -0.000001 0.000001, 0.000000 -0.000000 -0.000000, 0.000000 -0.000000 -0.000003, -0.000001 -0.000000 0.000000, -0.000001 -0.000001 0.000000, -0.000001 0.000000 0.000000, 0.000000 0.000001 -0.000003, -0.000000 -0.000000 -0.000001, -0.000000 -0.000000 -0.000001, -0.000001 -0.000000 -0.000000, -0.000001 -0.000000 0.000002, -0.000000 -0.000001 -0.000002, -0.000000 -0.000001 -0.000004, -0.000000 0.000000 0.000002, -0.000000 -0.000000 -0.000002, 0.000000 0.000000 -0.000003, -0.000001 -0.000000 -0.000003, -0.000000 -0.000000 -0.000001, -0.000000 -0.000000 -0.000002, 0.000000 0.000000 -0.000003, -0.000001 -0.000000 0.000000, -0.000000 -0.000001 -0.000001, -0.000001 0.000000 0.000000, -0.000000 0.000000 -0.000000, -0.000000 0.000000 -0.000006, -0.000001 -0.000000 -0.000005, -0.000001 0.000000 -0.000001, -0.000000 -0.000000 -0.000002, -0.000000 -0.000000 -0.000003, -0.000000 0.000000 0.000002, -0.000001 0.000000 -0.000003, 0.000000 -0.000000 -0.000002, -0.000000 -0.000000 0.000002, -0.000001 0.000000 0.000000, -0.000000 0.000000 -0.000001, -0.000000 -0.000000 -0.000003, -0.000000 -0.000000 -0.000000, -0.000000 0.000000 -0.000002, 0.000000 -0.000000 -0.000002, -0.000001 -0.000000 0.000001, -0.000001 -0.000000 0.000002, -0.000000 0.000000 0.000002, -0.000000 0.000000 -0.000003, 0.000000 0.000001 -0.000002, -0.000001 -0.000000 -0.000003, -0.000001 -0.000000 -0.000003, -0.000001 0.000000 -0.000004, -0.000000 0.000000 -0.000004, -0.000001 -0.000000 -0.000004, -0.000000 0.000000 -0.000001, -0.000001 0.000000 -0.000001, -0.000001 -0.000001 -0.000002, -0.000000 0.000001 -0.000003, -0.000001 -0.000001 0.000000, -0.000000 -0.000001 0.000000, 0.000000 0.000001 -0.000003, -0.000001 -0.000000 0.000002, -0.000000 -0.000001 0.000001, -0.000000 0.000000 -0.000001, -0.000000 0.000000 -0.000003, -0.000001 -0.000000 -0.000001, -0.000001 0.000000 -0.000000, -0.000000 0.000000 -0.000003, -0.000000 -0.000001 -0.000003, -0.000001 -0.000000 -0.000002, -0.000001 0.000000 -0.000001, -0.000001 -0.000001 -0.000000, -0.000001 -0.000001 0.000001, 0.000000 -0.000000 -0.000004, 0.000000 -0.000000 -0.000002, -0.000001 0.000001 -0.000002, -0.000000 0.000000 -0.000005, 0.000000 -0.000001 0.000002, 0.000000 0.000001 -0.000003, -0.000000 -0.000001 -0.000002, -0.000000 0.000000 -0.000001, -0.000001 0.000001 -0.000002, -0.000001 0.000000 -0.000001, 0.000000 -0.000000 -0.000003, -0.000001 0.000000 -0.000003, -0.000000 -0.000001 0.000002, -0.000000 -0.000000 -0.000001, 0.000000 0.000001 -0.000003, 0.000000 -0.000000 -0.000003, -0.000001 0.000000 0.000003, -0.000001 -0.000000 0.000001, 0.000000 -0.000001 -0.000004, -0.000001 -0.000001 0.000001, 0.000000 -0.000001 -0.000003, -0.000001 -0.000001 -0.000001, -0.000000 0.000000 -0.000003, -0.000001 -0.000001 -0.000002, -0.000001 0.000000 -0.000002, -0.000001 0.000000 0.000000, -0.000000 -0.000001 0.000001, 0.000000 0.000000 -0.000002, -0.000000 -0.000000 -0.000002, -0.000001 0.000000 -0.000001, -0.000001 0.000001 0.000000, -0.000000 0.000000 -0.000001, -0.000000 -0.000000 -0.000004, -0.000001 0.000001 -0.000001, -0.000001 0.000000 -0.000000, 0.000000 -0.000002 -0.000001, 0.000000 -0.000001 -0.000003, -0.000001 -0.000001 -0.000001, -0.000001 -0.000000 -0.000004, -0.000000 -0.000001 -0.000003, -0.000001 -0.000001 0.000001, -0.000000 -0.000000 0.000001, -0.000000 -0.000000 -0.000001, 0.000000 0.000000 0.000001, -0.000000 0.000001 -0.000003, -0.000001 0.000000 -0.000004, -0.000001 0.000000 -0.000001, -0.000001 0.000000 -0.000002, -0.000001 0.000000 -0.000002, -0.000000 0.000001 -0.000004, 0.000000 0.000001 -0.000003, -0.000001 0.000000 -0.000002, -0.000001 0.000000 -0.000001, -0.000001 -0.000000 -0.000003, 0.000000 -0.000000 -0.000003, -0.000001 -0.000000 -0.000000, -0.000001 0.000000 -0.000001, -0.000000 -0.000001 -0.000002, -0.000000 -0.000000 -0.000002, 0.000000 0.000000 -0.000004, -0.000001 -0.000000 0.000001, -0.000001 -0.000000 -0.000004, -0.000000 0.000000 0.000001, -0.000001 -0.000002 0.000001, -0.000000 0.000000 -0.000003, -0.000000 0.000001 -0.000000, -0.000001 -0.000000 0.000004, -0.000000 -0.000001 -0.000002, -0.000001 0.000001 0.000002, -0.000001 0.000000 -0.000001, 0.000000 -0.000001 -0.000002, -0.000000 -0.000001 -0.000001, -0.000000 -0.000000 0.000002, -0.000000 -0.000000 -0.000003, 0.000000 -0.000000 -0.000003, -0.000000 -0.000001 0.000003, -0.000000 -0.000001 -0.000003, -0.000001 -0.000000 0.000000, -0.000000 0.000000 0.000001, -0.000000 -0.000001 -0.000000, -0.000000 -0.000000 0.000001, 0.000000 -0.000000 -0.000002, 0.000000 -0.000001 -0.000003, 0.000000 -0.000000 0.000001, -0.000001 0.000000 0.000002, -0.000001 0.000000 -0.000002, -0.000000 0.000000 -0.000003, -0.000000 -0.000000 -0.000000, -0.000001 -0.000001 0.000001, -0.000001 0.000001 -0.000001, -0.000000 -0.000000 -0.000002, -0.000001 0.000001 -0.000005, -0.000001 -0.000000 -0.000002, -0.000001 -0.000001 -0.000002, -0.000001 0.000000 -0.000004, -0.000000 -0.000000 0.000001, -0.000001 0.000000 -0.000003, -0.000001 -0.000000 -0.000002, -0.000001 0.000001 -0.000001, 0.000000 0.000000 -0.000001, -0.000000 0.000000 0.000001, -0.000000 -0.000001 -0.000002, -0.000001 0.000001 -0.000003, -0.000000 -0.000000 0.000002, -0.000000 -0.000001 -0.000000, -0.000000 -0.000001 0.000003, -0.000001 -0.000001 0.000003, -0.000001 -0.000001 -0.000001, 0.000000 -0.000001 -0.000000, -0.000000 0.000001 -0.000001, -0.000000 0.000000 -0.000001, -0.000001 0.000000 0.000004, -0.000001 0.000001 -0.000001, 0.000000 -0.000000 -0.000001, -0.000001 -0.000001 0.000001, -0.000000 0.000001 -0.000001, -0.000001 -0.000000 -0.000001, 0.000000 0.000000 0.000001, -0.000001 -0.000002 -0.000003, -0.000000 0.000001 -0.000001, -0.000001 0.000000 0.000002, -0.000000 0.000000 -0.000003, 0.000000 -0.000000 -0.000000, 0.000000 -0.000000 -0.000001, -0.000001 -0.000000 0.000001, -0.000000 -0.000001 -0.000002, -0.000001 -0.000001 0.000001, -0.000000 0.000001 -0.000001, -0.000001 -0.000000 -0.000003, -0.000000 -0.000000 -0.000003, -0.000000 0.000001 -0.000000, -0.000001 -0.000001 -0.000000, -0.000000 -0.000001 0.000000, -0.000001 -0.000001 -0.000003, -0.000000 -0.000001 -0.000001, -0.000001 -0.000001 -0.000002, 0.000000 -0.000001 -0.000002, 0.000000 -0.000000 0.000001, -0.000001 -0.000000 -0.000001, -0.000000 -0.000000 -0.000004, -0.000001 -0.000001 0.000004, -0.000000 -0.000002 -0.000000, 0.000000 0.000000 -0.000002, -0.000001 -0.000001 -0.000002, -0.000000 -0.000001 -0.000000, -0.000000 0.000000 0.000002, 0.000000 -0.000001 -0.000002, -0.000001 0.000001 -0.000005, -0.000001 0.000001 0.000001, 0.000000 -0.000001 -0.000003, 0.000000 0.000001 -0.000002
#Interpolator13_l_shoulder channels [39..41] sends animation values to BVH JOINT LeftShoulder, DEF BvhConversion1_l_shoulder, <HAnimJoint name=l_shoulder/>
OrientationInterpolator331 = x3d.OrientationInterpolator()
OrientationInterpolator331.DEF = "Interpolator13_l_shoulder"
OrientationInterpolator331.key = [0,0.0035,0.007,0.0105,0.014,0.0175,0.0211,0.0246,0.0281,0.0316,0.0351,0.0386,0.0421,0.0456,0.0491,0.0526,0.0561,0.0596,0.0632,0.0667,0.0702,0.0737,0.0772,0.0807,0.0842,0.0877,0.0912,0.0947,0.0982,0.1018,0.1053,0.1088,0.1123,0.1158,0.1193,0.1228,0.1263,0.1298,0.1333,0.1368,0.1404,0.1439,0.1474,0.1509,0.1544,0.1579,0.1614,0.1649,0.1684,0.1719,0.1754,0.1789,0.1825,0.186,0.1895,0.193,0.1965,0.2,0.2035,0.207,0.2105,0.214,0.2175,0.2211,0.2246,0.2281,0.2316,0.2351,0.2386,0.2421,0.2456,0.2491,0.2526,0.2561,0.2596,0.2632,0.2667,0.2702,0.2737,0.2772,0.2807,0.2842,0.2877,0.2912,0.2947,0.2982,0.3018,0.3053,0.3088,0.3123,0.3158,0.3193,0.3228,0.3263,0.3298,0.3333,0.3368,0.3404,0.3439,0.3474,0.3509,0.3544,0.3579,0.3614,0.3649,0.3684,0.3719,0.3754,0.3789,0.3825,0.386,0.3895,0.393,0.3965,0.4,0.4035,0.407,0.4105,0.414,0.4175,0.4211,0.4246,0.4281,0.4316,0.4351,0.4386,0.4421,0.4456,0.4491,0.4526,0.4561,0.4596,0.4632,0.4667,0.4702,0.4737,0.4772,0.4807,0.4842,0.4877,0.4912,0.4947,0.4982,0.5018,0.5053,0.5088,0.5123,0.5158,0.5193,0.5228,0.5263,0.5298,0.5333,0.5368,0.5404,0.5439,0.5474,0.5509,0.5544,0.5579,0.5614,0.5649,0.5684,0.5719,0.5754,0.5789,0.5825,0.586,0.5895,0.593,0.5965,0.6,0.6035,0.607,0.6105,0.614,0.6175,0.6211,0.6246,0.6281,0.6316,0.6351,0.6386,0.6421,0.6456,0.6491,0.6526,0.6561,0.6596,0.6632,0.6667,0.6702,0.6737,0.6772,0.6807,0.6842,0.6877,0.6912,0.6947,0.6982,0.7018,0.7053,0.7088,0.7123,0.7158,0.7193,0.7228,0.7263,0.7298,0.7333,0.7368,0.7404,0.7439,0.7474,0.7509,0.7544,0.7579,0.7614,0.7649,0.7684,0.7719,0.7754,0.7789,0.7825,0.786,0.7895,0.793,0.7965,0.8,0.8035,0.807,0.8105,0.814,0.8175,0.8211,0.8246,0.8281,0.8316,0.8351,0.8386,0.8421,0.8456,0.8491,0.8526,0.8561,0.8596,0.8632,0.8667,0.8702,0.8737,0.8772,0.8807,0.8842,0.8877,0.8912,0.8947,0.8982,0.9018,0.9053,0.9088,0.9123,0.9158,0.9193,0.9228,0.9263,0.9298,0.9333,0.9368,0.9404,0.9439,0.9474,0.9509,0.9544,0.9579,0.9614,0.9649,0.9684,0.9719,0.9754,0.9789,0.9825,0.986,0.9895,0.993,0.9965,1]

Group313.children.append(OrientationInterpolator331)
#Euler angle triplet values, CHANNELS Zrotation Xrotation Yrotation, with min/max ranges [-9.387506,2.305873], [-9.412142,10.268742], [-21.255741,4.9E-324] degrees
#-3.044958 2.073855 -11.594578, -3.034865 2.054907 -11.710495, -3.241454 2.104472 -11.923323, -3.288924 2.183270 -12.103689, -3.298266 2.229691 -12.444087, -3.267601 2.341883 -12.701078, -3.274577 2.428410 -12.766608, -3.203674 2.548425 -12.908639, -3.031522 2.848173 -13.005631, -2.977609 3.184350 -13.051184, -3.037540 3.367566 -12.979206, -2.952636 3.547034 -12.995814, -2.930911 3.691416 -13.027780, -2.951313 3.792785 -12.893161, -2.899162 3.865137 -12.921764, -2.899467 4.035412 -12.812999, -2.912050 4.086954 -12.796653, -2.887900 4.128922 -12.692170, -2.879447 3.962058 -12.732851, -2.738386 3.866985 -12.615643, -2.597700 3.770831 -12.497939, -2.553573 3.751033 -12.255336, -2.299378 3.811129 -11.839067, -2.045170 3.871180 -11.423052, -1.722959 4.040985 -11.003507, -1.275263 4.142782 -10.556090, -0.672923 4.130442 -10.281590, -0.035877 4.026489 -10.057885, 0.464645 3.904207 -9.948834, 0.751247 3.884190 -9.858994, 0.992885 3.797625 -9.700407, 1.080012 3.720547 -9.610147, 1.077539 3.554980 -9.713577, 0.958262 3.452191 -10.013822, 0.993874 3.398245 -10.526814, 0.959401 3.390013 -11.087187, 1.014387 3.290275 -11.670405, 1.131263 3.221537 -12.193494, 1.407624 3.282308 -12.690172, 1.695965 3.361434 -13.027176, 1.874681 3.430093 -13.282827, 2.102483 3.392086 -13.322164, 2.296537 3.392012 -13.351357, 2.295662 3.314781 -13.183971, 2.305873 3.296190 -12.746310, 2.244937 3.246313 -12.317895, 2.064892 3.104784 -11.894423, 1.964205 2.990759 -11.547964, 1.888998 2.928120 -11.343236, 1.777853 2.367349 -11.131145, 1.456911 1.800665 -11.002416, 1.272597 1.309327 -11.032833, 1.018241 0.923514 -11.142959, 0.746404 0.925537 -11.384513, 0.545372 0.938922 -11.764384, 0.233371 0.740976 -12.096395, -0.025197 0.674090 -12.408784, -0.272469 0.724002 -12.724458, -0.562685 0.911360 -12.940438, -0.849568 1.176776 -13.157176, -1.099117 1.400172 -13.343926, -1.505434 1.490325 -13.641071, -1.850734 1.657252 -13.809486, -2.134161 1.745484 -13.953410, -2.512011 1.904995 -13.921693, -2.729796 1.979981 -13.645653, -2.927417 1.985130 -13.407908, -3.175800 1.906740 -13.103116, -3.421330 1.819728 -12.649565, -3.652028 1.773151 -12.165737, -3.884034 1.797017 -11.657226, -4.155064 1.787419 -11.427326, -4.189151 1.713662 -11.562064, -4.094838 1.628316 -12.004236, -4.204506 1.558453 -12.770753, -4.202672 1.440001 -13.593976, -4.155036 1.194428 -14.319252, -4.169705 0.984530 -14.989929, -4.185528 0.773067 -15.442711, -4.184811 0.515612 -15.773163, -4.217707 0.235111 -15.911489, -4.184987 -0.082117 -15.841219, -4.147254 -0.415632 -15.683357, -4.053545 -0.713122 -15.451437, -4.030497 -1.146008 -15.386662, -3.959105 -1.523133 -15.306087, -3.915753 -1.820912 -15.383133, -3.916800 -2.104247 -15.460607, -3.769369 -2.267716 -15.720489, -3.692990 -2.463622 -15.903625, -3.605469 -2.514154 -16.023909, -3.536959 -2.493915 -16.106842, -3.487656 -2.530164 -15.962946, -3.458153 -2.495108 -15.782564, -3.532727 -2.540983 -15.712835, -3.562775 -2.522129 -15.557800, -3.534289 -2.486169 -15.378162, -3.550485 -2.437078 -15.198223, -3.503273 -2.392961 -14.968110, -3.406770 -2.242889 -14.779643, -3.354129 -2.158494 -14.676541, -3.383672 -2.021441 -14.562230, -3.436462 -1.824519 -14.476516, -3.467610 -1.597682 -14.268381, -3.567390 -1.484751 -14.070638, -3.544492 -1.356080 -13.800237, -3.522333 -1.227171 -13.530066, -3.616445 -1.102360 -13.325771, -3.753788 -1.015640 -13.149265, -3.808070 -0.823512 -12.860054, -3.844555 -0.650188 -12.576937, -4.012863 -0.462107 -12.352064, -4.235071 -0.328816 -12.054316, -4.500610 -0.115342 -11.866139, -4.652457 0.103163 -11.822692, -4.809642 0.342403 -11.659942, -4.866854 0.574250 -11.484165, -4.882844 0.875147 -11.437001, -5.035021 1.245404 -11.309993, -5.099963 1.505728 -11.122296, -5.252772 1.829173 -11.071297, -5.209503 2.100334 -10.973913, -5.190055 2.306407 -11.178873, -5.085031 2.265442 -11.499004, -4.762163 2.082603 -12.021273, -4.409181 1.742790 -12.515231, -4.093843 1.302309 -13.056742, -3.773586 0.721607 -13.441149, -3.504803 0.231679 -13.685265, -3.392759 -0.137938 -13.892022, -3.316873 -0.623760 -13.997720, -3.310924 -1.024869 -14.228924, -3.307656 -1.425849 -14.460252, -3.236046 -1.739447 -14.801023, -3.141050 -2.073414 -15.100701, -3.047803 -2.291173 -15.808543, -3.026188 -2.358311 -16.410795, -2.955800 -2.361053 -16.929569, -2.947878 -2.330798 -17.440506, -2.859209 -2.151447 -18.022627, -2.814138 -1.991106 -18.364861, -2.674809 -1.714573 -18.546370, -2.446549 -1.535760 -18.707869, -2.271093 -1.540204 -18.941063, -2.132188 -1.677517 -19.296432, -2.115988 -1.959916 -19.712883, -2.182925 -2.440749 -20.142923, -2.241583 -2.936510 -20.508316, -2.373594 -3.548272 -20.729713, -2.509871 -4.249084 -20.885994, -2.806214 -4.997395 -21.031887, -3.034326 -5.564407 -21.133289, -3.333303 -6.119946 -21.255741, -3.694474 -6.739315 -21.198273, -4.030061 -7.377348 -21.072388, -4.322578 -8.010102 -20.558661, -4.730327 -8.519249 -19.877848, -5.055167 -8.956087 -19.301590, -5.301996 -9.293395 -18.939430, -5.460378 -9.412142 -18.832911, -5.549767 -9.218116 -18.835825, -5.490839 -8.947426 -18.960333, -5.216247 -8.610525 -18.973219, -4.984900 -8.254458 -18.831274, -4.667513 -7.815197 -18.565203, -4.316731 -7.401927 -18.350285, -4.126024 -6.856118 -18.312523, -3.938340 -6.309916 -18.274521, -3.823502 -5.643348 -18.294920, -3.625784 -5.103850 -18.367519, -3.491300 -4.405032 -18.335850, -3.261996 -3.784894 -18.255047, -3.265533 -3.134979 -18.101357, -3.268107 -2.498721 -18.032606, -3.276966 -1.849833 -17.874018, -3.213025 -1.245051 -17.504210, -3.342927 -0.580858 -17.029602, -3.544692 0.113628 -16.540846, -3.705549 0.622723 -16.120468, -4.045189 1.214400 -15.626913, -4.368543 1.931272 -15.008426, -4.712505 2.731411 -14.449440, -5.069759 3.525449 -13.885185, -5.432257 4.224469 -13.252036, -5.919944 4.965570 -12.551833, -6.373174 5.674312 -11.700415, -6.850924 6.365691 -10.890823, -7.271768 6.949390 -10.086547, -7.647027 7.470294 -9.193872, -7.947875 7.884908 -8.621955, -8.289232 8.232164 -8.129413, -8.541259 8.554208 -7.745832, -8.711765 8.921842 -7.391368, -8.901354 9.410193 -7.165750, -9.080611 9.781924 -6.847609, -9.260572 10.032321 -6.323062, -9.368829 10.251036 -5.821846, -9.387506 10.268742 -5.433249, -9.357605 10.174235 -5.048729, -9.277029 10.028883 -4.796269, -9.254098 9.840482 -4.819190, -9.163494 9.475294 -5.148085, -8.986751 9.076620 -5.875787, -8.713162 8.571762 -6.866428, -8.133613 7.938206 -8.123498, -7.704853 7.092192 -9.532252, -7.289905 6.111494 -10.838983, -6.878291 5.130288 -11.833037, -6.532898 4.123590 -12.729178, -6.094930 3.067343 -13.331042, -5.706879 2.067441 -13.792476, -5.309616 1.104420 -13.970418, -4.906435 0.312517 -14.120933, -4.507226 -0.481739 -14.265531, -4.040748 -1.157403 -14.344855, -3.576717 -1.771337 -14.492719, -3.050090 -2.299023 -14.746712, -2.655045 -2.898245 -15.033571, -2.265627 -3.500641 -15.317142, -2.028528 -3.989343 -15.707569, -1.936526 -4.393927 -16.023539, -1.969158 -4.714924 -16.314053, -2.159360 -4.733823 -16.688417, -2.572454 -4.658047 -16.841946, -2.939093 -4.570482 -17.034208, -3.450158 -4.419283 -17.101330, -3.943962 -4.092371 -17.200796, -4.506532 -3.684474 -17.103901, -4.999256 -3.275378 -16.955956, -5.451652 -2.949992 -16.786236, -5.926335 -2.527813 -16.585445, -6.330361 -1.954969 -16.563194, -6.727497 -1.380915 -16.692297, -7.185153 -0.774645 -16.805960, -7.541569 -0.280458 -16.754862, -8.044259 0.183711 -16.571295, -8.418431 0.644117 -16.082649, -8.863223 1.132443 -15.359181, -9.122657 1.527717 -14.789063, -9.250097 1.913360 -14.273238, -9.227627 2.424386 -14.104543, -9.224277 2.974536 -14.083397, -9.106703 3.365515 -14.221620, -8.887671 3.810462 -14.351173, -8.532238 4.167579 -14.294529, -8.165396 4.343503 -14.112166, -7.864990 4.575883 -13.750803, -7.639065 4.682081 -13.248361, -7.416630 4.788873 -12.744734, -7.155435 4.803731 -12.426048, -6.941824 4.789548 -12.130846, -6.774914 4.769210 -12.037991, -6.567299 4.853852 -11.890024, -6.361548 4.918823 -11.897600, -6.244677 4.966275 -11.977062, -5.997178 4.867736 -11.988696, -5.984957 4.751479 -11.977785, -5.889725 4.639770 -12.012531, -5.921333 4.403740 -11.906936, -5.877171 4.188404 -11.728953, -5.789853 3.915028 -11.679750, -5.773612 3.733564 -11.737062, -5.702929 3.389049 -11.933737, -5.758724 3.227769 -12.092546, -5.929702 2.964466 -12.259266, -6.159350 2.848577 -12.402455, -6.415570 2.862462 -12.434653, -6.646872 2.913961 -12.280888, -6.647454 2.996428 -12.009553, -6.787520 3.083948 -11.625485, -6.722947 3.238304 -11.317805, -6.740069 3.385339 -10.962743, -6.648649 3.399617 -10.829926, -6.557105 3.414344 -10.697407, -6.562384 3.237964 -10.725780, -6.471952 3.121385 -10.817434, -6.380458 3.034398 -10.994202, -6.302236 2.937070 -11.136127, -6.342291 2.967563 -11.100213, -6.249361 2.983246 -10.968664, -6.171173 2.843913 -10.813951, -6.054072 2.770585 -10.575155, -5.951966 2.786934 -10.396441, -5.768618 2.666011 -10.338457, -5.557788 2.579636 -10.473218, -5.196756 2.388356 -10.759043
#Interpolator14_l_elbow channels [42..44] sends animation values to BVH JOINT LeftElbow, DEF BvhConversion1_l_elbow, <HAnimJoint name=l_elbow/>
OrientationInterpolator332 = x3d.OrientationInterpolator()
OrientationInterpolator332.DEF = "Interpolator14_l_elbow"
OrientationInterpolator332.key = [0,0.0035,0.007,0.0105,0.014,0.0175,0.0211,0.0246,0.0281,0.0316,0.0351,0.0386,0.0421,0.0456,0.0491,0.0526,0.0561,0.0596,0.0632,0.0667,0.0702,0.0737,0.0772,0.0807,0.0842,0.0877,0.0912,0.0947,0.0982,0.1018,0.1053,0.1088,0.1123,0.1158,0.1193,0.1228,0.1263,0.1298,0.1333,0.1368,0.1404,0.1439,0.1474,0.1509,0.1544,0.1579,0.1614,0.1649,0.1684,0.1719,0.1754,0.1789,0.1825,0.186,0.1895,0.193,0.1965,0.2,0.2035,0.207,0.2105,0.214,0.2175,0.2211,0.2246,0.2281,0.2316,0.2351,0.2386,0.2421,0.2456,0.2491,0.2526,0.2561,0.2596,0.2632,0.2667,0.2702,0.2737,0.2772,0.2807,0.2842,0.2877,0.2912,0.2947,0.2982,0.3018,0.3053,0.3088,0.3123,0.3158,0.3193,0.3228,0.3263,0.3298,0.3333,0.3368,0.3404,0.3439,0.3474,0.3509,0.3544,0.3579,0.3614,0.3649,0.3684,0.3719,0.3754,0.3789,0.3825,0.386,0.3895,0.393,0.3965,0.4,0.4035,0.407,0.4105,0.414,0.4175,0.4211,0.4246,0.4281,0.4316,0.4351,0.4386,0.4421,0.4456,0.4491,0.4526,0.4561,0.4596,0.4632,0.4667,0.4702,0.4737,0.4772,0.4807,0.4842,0.4877,0.4912,0.4947,0.4982,0.5018,0.5053,0.5088,0.5123,0.5158,0.5193,0.5228,0.5263,0.5298,0.5333,0.5368,0.5404,0.5439,0.5474,0.5509,0.5544,0.5579,0.5614,0.5649,0.5684,0.5719,0.5754,0.5789,0.5825,0.586,0.5895,0.593,0.5965,0.6,0.6035,0.607,0.6105,0.614,0.6175,0.6211,0.6246,0.6281,0.6316,0.6351,0.6386,0.6421,0.6456,0.6491,0.6526,0.6561,0.6596,0.6632,0.6667,0.6702,0.6737,0.6772,0.6807,0.6842,0.6877,0.6912,0.6947,0.6982,0.7018,0.7053,0.7088,0.7123,0.7158,0.7193,0.7228,0.7263,0.7298,0.7333,0.7368,0.7404,0.7439,0.7474,0.7509,0.7544,0.7579,0.7614,0.7649,0.7684,0.7719,0.7754,0.7789,0.7825,0.786,0.7895,0.793,0.7965,0.8,0.8035,0.807,0.8105,0.814,0.8175,0.8211,0.8246,0.8281,0.8316,0.8351,0.8386,0.8421,0.8456,0.8491,0.8526,0.8561,0.8596,0.8632,0.8667,0.8702,0.8737,0.8772,0.8807,0.8842,0.8877,0.8912,0.8947,0.8982,0.9018,0.9053,0.9088,0.9123,0.9158,0.9193,0.9228,0.9263,0.9298,0.9333,0.9368,0.9404,0.9439,0.9474,0.9509,0.9544,0.9579,0.9614,0.9649,0.9684,0.9719,0.9754,0.9789,0.9825,0.986,0.9895,0.993,0.9965,1]

Group313.children.append(OrientationInterpolator332)
#Euler angle triplet values, CHANNELS Zrotation Xrotation Yrotation, with min/max ranges [-13.882767,10.133185], [-1.735815,23.780594], [9.550971,19.809969] degrees
#-4.209171 -0.956767 15.542125, -4.459375 -0.830590 15.608989, -4.476139 -0.775092 15.764439, -4.553674 -0.842833 16.093493, -4.698999 -0.847590 16.460310, -4.872755 -0.836375 16.735620, -4.928457 -0.864238 16.899836, -5.065824 -0.881759 16.966072, -5.289596 -0.933467 17.090935, -5.365664 -1.020011 17.140644, -5.475568 -1.062598 17.227947, -5.562577 -1.165336 17.378244, -5.658044 -1.191625 17.550426, -5.797744 -1.269387 17.550930, -5.930939 -1.253531 17.659334, -6.036566 -1.309102 17.586447, -5.955359 -1.202155 17.667650, -5.918179 -1.146635 17.577909, -5.843574 -1.018329 17.685450, -5.656076 -0.885500 17.688231, -5.466358 -0.837841 17.687351, -5.083170 -0.779445 17.787874, -4.735620 -0.882076 17.745825, -4.470139 -1.059863 17.611347, -4.189794 -1.251557 17.556625, -3.975331 -1.531844 17.426308, -3.996085 -1.677718 17.283699, -4.127633 -1.735815 17.245644, -4.561687 -1.634529 17.152985, -4.957360 -1.489763 17.124262, -5.491736 -1.207605 17.209818, -6.082725 -0.769623 17.380705, -6.782347 -0.446813 17.698597, -7.366393 -0.186329 18.156824, -8.003438 -0.175855 18.612537, -8.581265 -0.176606 18.893654, -8.991168 -0.177254 18.966280, -9.300286 -0.185315 18.900526, -9.453194 -0.310359 18.813715, -9.502047 -0.547178 18.612331, -9.315676 -0.761112 18.472830, -9.032214 -0.863056 18.285244, -8.678535 -1.057144 18.238876, -8.127527 -1.132103 18.186089, -7.611537 -1.280606 18.123507, -7.102710 -1.358855 18.081436, -6.561292 -1.456617 18.113340, -6.020236 -1.558718 18.145536, -5.439682 -1.670151 18.168884, -5.005928 -1.216900 18.232254, -4.594167 -0.704705 18.374510, -4.316419 -0.250715 18.509298, -4.201699 0.165169 18.576675, -4.005128 0.345610 18.604012, -3.849675 0.472896 18.715967, -3.824566 0.780989 18.922544, -3.757487 0.999956 19.027016, -3.835992 1.227140 19.232571, -3.877246 1.681101 19.381929, -3.974991 1.889236 19.503635, -4.168779 2.288737 19.581636, -4.277148 2.727554 19.751133, -4.468053 3.019456 19.809969, -4.691412 3.355788 19.723595, -4.941257 3.590881 19.625395, -5.149311 3.846945 19.449001, -5.518249 4.091561 19.295052, -5.802319 4.359990 19.104815, -6.160785 4.613844 19.007309, -6.581861 4.755011 19.007168, -6.930963 4.877897 18.992970, -7.299025 4.919416 19.039633, -7.724164 5.011712 19.116959, -8.203210 5.067221 19.219921, -8.556305 5.187823 19.314568, -8.851434 5.432342 19.165398, -9.114920 5.916742 18.745882, -9.334521 6.428803 18.248915, -9.248812 6.787251 17.767183, -9.004655 7.104473 17.399529, -8.606471 7.344441 17.222944, -8.058151 7.511931 17.159761, -7.354538 7.557034 17.249926, -6.621694 7.469048 17.428129, -5.971743 7.406592 17.660318, -5.369191 7.216309 17.779671, -4.765512 7.167944 17.834131, -4.206584 7.043469 17.790636, -3.818351 6.900747 17.648430, -3.592147 6.769305 17.350552, -3.381538 6.568497 16.964777, -3.267299 6.356989 16.540892, -3.183041 6.171250 15.942126, -3.174823 5.969551 15.434334, -3.299578 5.812798 15.122505, -3.515888 5.571836 14.812185, -3.844260 5.478601 14.555556, -4.207500 5.437722 14.529812, -4.670587 5.243613 14.351428, -5.210903 5.118947 14.253291, -5.745653 5.134905 14.269896, -6.318861 4.968243 14.401862, -6.766427 4.858554 14.567904, -7.213177 4.791287 14.758533, -7.672348 4.704995 15.053877, -8.094817 4.726953 15.266988, -8.603125 4.750376 15.411119, -9.064714 4.968787 15.493136, -9.376055 5.193043 15.480665, -9.764377 5.363197 15.509413, -10.107094 5.598915 15.510505, -10.436650 5.882998 15.484701, -10.709711 6.221446 15.558580, -10.934103 6.479756 15.831849, -11.168912 6.691561 16.134851, -11.154889 6.948442 16.379087, -11.145953 7.195793 16.571669, -11.178375 7.277179 16.821804, -11.037157 7.283193 16.992092, -10.912533 7.540355 17.108328, -10.680483 7.651520 17.153492, -10.454957 7.754982 17.144592, -10.200117 7.813901 17.227530, -9.849169 7.988004 17.236147, -9.566648 8.229592 17.298761, -9.313190 8.604066 17.125658, -9.065071 9.103384 17.016672, -8.835649 9.823728 16.821247, -8.564953 10.524556 16.641405, -8.036058 11.111852 16.411766, -7.498885 11.677749 16.327095, -6.766594 12.060432 16.389269, -6.016947 12.284911 16.419006, -5.242659 12.340746 16.421825, -4.312412 12.253509 16.278143, -3.414839 11.978571 16.208630, -2.516546 11.643206 16.107079, -1.716726 11.233594 15.865287, -0.760790 10.725159 15.688431, 0.146052 10.144019 15.666552, 1.022553 9.391048 15.749197, 2.118312 8.664248 15.774732, 3.112027 7.988774 15.952493, 3.867852 7.557136 16.110594, 4.603578 7.456813 16.028215, 5.315589 7.920386 15.871456, 5.858576 8.633121 15.480124, 6.469305 9.505488 14.978026, 6.985815 10.602186 14.479682, 7.583831 11.768528 13.938344, 8.125725 12.843476 13.643888, 8.710976 13.842742 13.560955, 9.225446 14.825740 13.754625, 9.675375 15.907891 14.007954, 9.969776 17.063601 14.124324, 10.133185 18.265089 14.135760, 10.124131 19.462622 14.038130, 9.859505 20.655910 13.812223, 9.413152 21.695112 13.615335, 8.719193 22.675032 13.541964, 7.891953 23.235268 13.327739, 6.995933 23.638725 13.141107, 6.070464 23.780594 12.829035, 5.155535 23.675032 12.590035, 4.342409 23.249857 12.385584, 3.530252 22.654036 12.259220, 2.836408 21.903408 12.305445, 2.071643 21.147402 12.440242, 1.419769 20.221979 12.586562, 0.751407 19.446598 12.659112, 0.119909 18.526358 12.656977, -0.453634 17.675842 12.651535, -0.919135 16.751354 12.641153, -1.460240 15.819456 12.712205, -1.999994 14.799702 12.770612, -2.550905 13.869830 12.802065, -3.092126 12.864836 12.871896, -3.636950 11.923761 12.995268, -4.333068 11.039539 13.324360, -4.941827 10.150488 13.583951, -5.647548 9.165474 13.851786, -6.237635 8.095215 14.180084, -6.827014 7.072165 14.663619, -7.416586 6.000070 15.378827, -7.899324 4.859103 16.447224, -8.324320 3.703049 17.569603, -8.702048 2.732254 18.537712, -9.223924 2.110599 19.012161, -9.903196 1.819121 18.800875, -10.609579 1.790293 18.027016, -11.314376 1.909543 17.018436, -11.993101 2.133825 15.987415, -12.559577 2.263109 15.073343, -13.008528 2.401032 14.486806, -13.456431 2.547442 14.136783, -13.695181 2.637401 13.881462, -13.830696 2.702403 13.806053, -13.882767 2.777306 13.932421, -13.806030 2.823957 14.205081, -13.698832 2.896905 14.543669, -13.440144 2.903685 15.063564, -13.049117 2.964599 15.532318, -12.582395 3.006806 16.008930, -12.185318 3.206030 16.332266, -11.960507 3.760663 16.347935, -11.710421 4.709547 16.253475, -11.436913 5.916440 15.996597, -11.064242 7.071280 15.768641, -10.506244 8.315563 15.762149, -9.749377 9.422051 15.907364, -8.733082 10.361988 16.348814, -7.377421 11.069993 16.747402, -5.860786 11.568916 16.976484, -4.159358 12.025715 17.107235, -2.522868 12.364349 16.941208, -0.827394 12.787610 16.416218, 0.708919 13.172513 15.752969, 2.089611 13.699724 14.910072, 3.384781 14.281545 13.810833, 4.610054 14.977067 12.873751, 5.498202 15.459451 11.947922, 6.330312 15.931559 11.153659, 7.096742 16.225086 10.530219, 7.918955 16.491299 9.980167, 8.434252 16.680573 9.656838, 8.855320 16.773500 9.550971, 9.033079 16.783869 9.784859, 9.091599 16.693583 10.083716, 8.885856 16.423336 10.489127, 8.547802 16.071053 11.074666, 7.958511 15.628088 11.728759, 7.172847 15.149816 12.406691, 6.094202 14.666093 13.222463, 4.931275 14.318007 13.869642, 3.459772 14.024971 14.209665, 1.996659 13.830787 14.414717, 0.497845 13.680631 14.259167, -0.935290 13.471660 13.990609, -2.414020 13.117090 13.856963, -3.718766 12.638750 13.933881, -4.868982 11.986049 14.207788, -5.913978 11.252207 14.511347, -6.865771 10.626214 14.823124, -7.738748 9.960899 14.996495, -8.476386 9.378256 14.891519, -9.007651 8.950191 14.521791, -9.402910 8.571769 14.049887, -9.650097 8.202990 13.624310, -9.813382 7.796931 13.417549, -10.021760 7.465520 13.545949, -9.987944 7.021313 13.760652, -9.983622 6.638350 14.078608, -9.900344 6.274251 14.307397, -9.797681 5.813008 14.361516, -9.595609 5.500843 14.249359, -9.487720 5.427943 14.069005, -9.201013 5.528785 13.890007, -8.996124 5.529988 13.718266, -8.702696 5.529769 13.667620, -8.320672 5.433749 13.681541, -8.002837 5.370070 13.827699, -7.645149 5.274691 14.121141, -7.266457 5.279308 14.434305, -6.982258 5.300949 14.571355, -6.693873 5.486518 14.673789, -6.407830 5.676010 14.775290, -6.104132 5.952167 14.595583, -5.833138 6.221560 14.453097, -5.844730 6.400421 14.366108, -5.675450 6.469025 14.509668, -5.656924 6.359528 14.694358, -5.547674 6.254079 14.994569, -5.513400 6.174387 15.351606, -5.562623 6.110967 15.613249, -5.607419 6.250768 15.810017, -5.667704 6.372327 15.881334, -5.606840 6.528724 15.977761, -5.599769 6.756353 15.958705, -5.479019 6.836749 15.951333, -5.384267 6.839868 15.876088, -5.131411 6.942599 15.853076, -4.789719 6.819990 15.774738, -4.423537 6.607477 15.751765, -4.131451 6.517969 15.862647, -3.901722 6.475040 16.036787, -3.880312 6.426272 16.235306
#Interpolator15_l_wrist channels [45..47] sends animation values to BVH JOINT LeftWrist, DEF BvhConversion1_l_wrist, <HAnimJoint name=l_wrist/>
OrientationInterpolator333 = x3d.OrientationInterpolator()
OrientationInterpolator333.DEF = "Interpolator15_l_wrist"
OrientationInterpolator333.key = [0,0.0035,0.007,0.0105,0.014,0.0175,0.0211,0.0246,0.0281,0.0316,0.0351,0.0386,0.0421,0.0456,0.0491,0.0526,0.0561,0.0596,0.0632,0.0667,0.0702,0.0737,0.0772,0.0807,0.0842,0.0877,0.0912,0.0947,0.0982,0.1018,0.1053,0.1088,0.1123,0.1158,0.1193,0.1228,0.1263,0.1298,0.1333,0.1368,0.1404,0.1439,0.1474,0.1509,0.1544,0.1579,0.1614,0.1649,0.1684,0.1719,0.1754,0.1789,0.1825,0.186,0.1895,0.193,0.1965,0.2,0.2035,0.207,0.2105,0.214,0.2175,0.2211,0.2246,0.2281,0.2316,0.2351,0.2386,0.2421,0.2456,0.2491,0.2526,0.2561,0.2596,0.2632,0.2667,0.2702,0.2737,0.2772,0.2807,0.2842,0.2877,0.2912,0.2947,0.2982,0.3018,0.3053,0.3088,0.3123,0.3158,0.3193,0.3228,0.3263,0.3298,0.3333,0.3368,0.3404,0.3439,0.3474,0.3509,0.3544,0.3579,0.3614,0.3649,0.3684,0.3719,0.3754,0.3789,0.3825,0.386,0.3895,0.393,0.3965,0.4,0.4035,0.407,0.4105,0.414,0.4175,0.4211,0.4246,0.4281,0.4316,0.4351,0.4386,0.4421,0.4456,0.4491,0.4526,0.4561,0.4596,0.4632,0.4667,0.4702,0.4737,0.4772,0.4807,0.4842,0.4877,0.4912,0.4947,0.4982,0.5018,0.5053,0.5088,0.5123,0.5158,0.5193,0.5228,0.5263,0.5298,0.5333,0.5368,0.5404,0.5439,0.5474,0.5509,0.5544,0.5579,0.5614,0.5649,0.5684,0.5719,0.5754,0.5789,0.5825,0.586,0.5895,0.593,0.5965,0.6,0.6035,0.607,0.6105,0.614,0.6175,0.6211,0.6246,0.6281,0.6316,0.6351,0.6386,0.6421,0.6456,0.6491,0.6526,0.6561,0.6596,0.6632,0.6667,0.6702,0.6737,0.6772,0.6807,0.6842,0.6877,0.6912,0.6947,0.6982,0.7018,0.7053,0.7088,0.7123,0.7158,0.7193,0.7228,0.7263,0.7298,0.7333,0.7368,0.7404,0.7439,0.7474,0.7509,0.7544,0.7579,0.7614,0.7649,0.7684,0.7719,0.7754,0.7789,0.7825,0.786,0.7895,0.793,0.7965,0.8,0.8035,0.807,0.8105,0.814,0.8175,0.8211,0.8246,0.8281,0.8316,0.8351,0.8386,0.8421,0.8456,0.8491,0.8526,0.8561,0.8596,0.8632,0.8667,0.8702,0.8737,0.8772,0.8807,0.8842,0.8877,0.8912,0.8947,0.8982,0.9018,0.9053,0.9088,0.9123,0.9158,0.9193,0.9228,0.9263,0.9298,0.9333,0.9368,0.9404,0.9439,0.9474,0.9509,0.9544,0.9579,0.9614,0.9649,0.9684,0.9719,0.9754,0.9789,0.9825,0.986,0.9895,0.993,0.9965,1]

Group313.children.append(OrientationInterpolator333)
#Euler angle triplet values, CHANNELS Zrotation Xrotation Yrotation, with min/max ranges [-25.808823,28.885216], [-19.734434,9.765475], [-1.893683,5.558785] degrees
#4.620726 8.767239 2.816781, 4.875600 8.477571 2.801267, 5.042766 8.200990 2.872262, 5.259824 8.193152 2.844685, 5.576401 8.157900 2.784464, 5.926369 7.997870 2.778819, 6.097806 8.035483 2.684623, 6.445376 8.072772 2.669499, 6.798725 8.099038 2.683844, 7.015496 8.088227 2.659138, 7.312119 8.170278 2.553663, 7.606586 8.303685 2.428225, 7.700098 8.388991 2.353513, 7.861967 8.506024 2.336178, 7.924347 8.672566 2.254587, 7.956888 8.742134 2.226346, 7.844638 8.688625 2.176867, 7.800100 8.666793 2.182888, 7.507773 8.704259 2.154918, 7.127421 8.651467 2.180640, 6.656054 8.664115 2.224817, 6.071107 8.632622 2.281117, 5.442282 8.697379 2.336358, 4.913029 8.711118 2.451399, 4.274776 8.640910 2.442828, 3.676760 8.507605 2.573990, 3.350749 8.146338 2.705052, 3.252988 7.748227 2.866765, 3.622089 7.246763 2.998524, 4.293136 6.781305 2.970351, 5.434257 6.341100 2.950962, 6.816708 5.906898 2.938832, 8.473284 5.633001 2.956011, 10.137950 5.473197 2.880136, 11.711172 5.544520 2.850253, 13.076478 5.718525 2.715529, 14.095562 6.115538 2.472556, 14.793044 6.599702 2.141587, 15.000972 7.136200 1.762866, 14.939879 7.661156 1.443180, 14.566185 7.999672 1.270827, 13.945295 8.314679 1.231654, 13.114498 8.409328 1.293227, 12.128458 8.237076 1.340159, 11.102587 7.969378 1.417113, 10.085241 7.586093 1.677043, 8.980842 7.162271 1.940603, 7.916407 6.806740 2.278299, 6.971710 6.461987 2.676120, 6.113612 6.135380 2.891786, 5.450493 6.220343 3.057244, 4.884509 6.382152 3.116131, 4.510855 6.607057 3.089900, 4.142714 6.907024 2.991646, 3.937205 7.301610 2.989913, 3.963002 7.524080 2.788505, 4.083537 7.757822 2.701741, 4.289783 7.973776 2.528921, 4.500170 7.971835 2.454756, 4.837687 7.993029 2.432399, 5.147330 7.936154 2.414962, 5.428708 7.822081 2.310754, 5.839411 7.625803 2.262836, 6.108890 7.313129 2.219027, 6.452726 7.089595 2.122387, 6.707889 6.899481 2.029534, 7.191120 6.611099 1.896950, 7.767786 6.337697 1.885586, 8.470172 6.105494 1.868444, 9.162922 5.763969 1.969792, 9.916862 5.487909 2.008574, 10.638151 5.145813 2.060763, 11.344402 4.735063 2.151609, 12.031893 4.372763 2.141499, 12.640953 3.870553 2.060377, 13.130677 3.363044 1.968518, 13.384215 2.783679 1.894829, 13.402261 2.145105 1.769360, 13.107335 1.563695 1.652807, 12.517855 0.962207 1.631302, 11.641868 0.358543 1.704922, 10.497449 -0.200647 1.971367, 9.000372 -0.678273 2.218765, 7.542405 -1.195140 2.497348, 6.109685 -1.680728 2.805229, 4.820708 -1.965640 3.085061, 3.837854 -2.267471 3.249453, 3.036231 -2.349053 3.277229, 2.306485 -2.323654 3.305002, 1.863751 -2.214744 3.170766, 1.361109 -2.040790 2.939258, 1.056890 -1.772715 2.688401, 0.777564 -1.454773 2.539138, 0.559147 -1.130816 2.398931, 0.608028 -1.019426 2.378818, 0.769179 -0.854414 2.349063, 1.148162 -0.674673 2.280957, 1.634566 -0.507836 2.079897, 2.260693 -0.216017 2.019564, 3.032943 0.123792 1.899781, 3.849300 0.463458 1.700418, 4.788741 0.935637 1.512582, 5.620234 1.545159 1.324352, 6.403686 2.079957 1.215486, 7.192437 2.691314 1.063133, 7.933629 3.006164 0.852103, 8.775698 3.199569 0.706722, 9.631068 3.191464 0.569163, 10.480242 3.035489 0.593736, 11.252699 2.917785 0.536009, 12.162734 2.710446 0.469593, 12.977405 2.548441 0.578295, 13.721233 2.424192 0.570749, 14.430466 2.479424 0.471995, 15.120250 2.646660 0.349173, 15.520801 2.824703 0.321298, 15.915130 2.969158 0.335698, 16.118317 3.049783 0.288980, 16.258596 3.135296 0.255994, 16.137142 3.063133 0.231835, 15.855867 3.068965 0.165038, 15.468962 2.916501 0.134498, 14.958249 2.723601 0.111103, 14.131956 2.490070 0.180438, 13.272406 2.050380 0.207110, 12.386274 1.533289 0.258710, 11.424575 0.848657 0.362794, 10.471356 -0.048381 0.507190, 9.518579 -0.956222 0.590680, 8.403514 -1.860515 0.729107, 7.182344 -2.620378 0.884132, 5.956905 -3.279521 0.954133, 4.650367 -3.808397 1.029208, 3.149436 -4.155130 1.181871, 1.558625 -4.422453 1.293027, -0.030825 -4.423519 1.500457, -1.606763 -4.367359 1.544098, -3.061541 -4.170847 1.642856, -4.578485 -3.590831 1.757656, -6.229995 -2.506581 1.791688, -7.788054 -0.867184 1.651815, -9.639607 1.233199 1.587350, -11.524076 3.728822 1.340977, -13.265940 6.116955 1.233482, -14.871373 8.002426 1.092433, -16.337273 9.232847 0.795219, -17.525732 9.765475 0.442410, -18.418291 9.598929 0.209807, -19.203876 8.704074 0.125388, -20.015265 7.537626 0.263158, -20.827839 6.254766 0.494169, -21.781200 4.867110 0.917780, -22.966192 3.429062 1.282292, -24.073215 1.826754 1.612325, -25.073244 0.038875 2.168858, -25.717354 -1.963256 2.466931, -25.808823 -4.303303 2.763247, -25.270954 -6.778835 3.029007, -24.322388 -9.246679 3.307162, -23.031250 -11.583159 3.418690, -21.531094 -13.491312 3.554604, -19.992138 -15.041576 3.541208, -18.598125 -15.932427 3.441245, -17.145519 -16.362297 3.283456, -15.781125 -16.371035 3.119052, -14.476338 -16.008780 3.001365, -13.140723 -15.551912 2.893258, -11.872144 -15.099747 2.780610, -10.597892 -14.567264 2.699757, -9.335052 -14.096886 2.587105, -7.964919 -13.491632 2.500794, -6.656513 -12.650269 2.359221, -5.285237 -11.733049 2.156366, -3.996275 -10.745983 1.964187, -2.600123 -9.515615 1.875355, -1.320075 -8.318119 1.561880, 0.086707 -6.965930 1.320131, 1.528474 -5.616585 1.010922, 3.166210 -4.250791 0.713805, 4.845451 -2.842324 0.509039, 6.680282 -1.486946 0.239104, 8.523042 -0.232424 0.281521, 10.349913 0.813008 0.386058, 12.252968 1.827176 0.745127, 14.098040 2.661243 1.223395, 15.813285 3.385173 1.652863, 17.505552 3.774270 1.967399, 19.174446 3.859797 1.976747, 20.867069 3.938329 1.766261, 22.381105 3.951263 1.506327, 24.019802 4.056929 1.080149, 25.322742 4.280541 0.716051, 26.417431 4.514408 0.369701, 27.344090 4.790527 0.086664, 28.079300 5.221510 -0.194938, 28.588633 5.757869 -0.548461, 28.850204 6.249621 -0.804202, 28.885216 6.688611 -1.098673, 28.697378 6.887233 -1.222120, 28.316261 7.000937 -1.296413, 27.726971 6.840428 -1.303107, 26.814863 6.586393 -1.206700, 25.735020 6.233004 -1.063734, 24.495438 5.731321 -1.020283, 23.194256 4.950009 -0.774443, 21.964586 3.922781 -0.633007, 20.733459 2.567836 -0.467455, 19.360138 1.166836 -0.403090, 17.704533 -0.221543 -0.244527, 15.602649 -1.561792 -0.068799, 13.092027 -2.801173 0.162622, 10.011459 -3.770286 0.336201, 6.544158 -4.615162 0.536949, 2.923383 -5.324854 0.771610, -0.739094 -6.078850 0.971988, -4.397464 -7.039455 1.257864, -7.841941 -8.294875 1.514206, -10.816671 -9.753691 1.734054, -13.545111 -11.373587 2.077692, -15.919448 -13.050215 2.286958, -17.825626 -14.720860 2.502021, -19.392822 -16.209805 2.808225, -20.622746 -17.537746 3.182724, -21.483521 -18.683931 3.705218, -21.947649 -19.415085 4.166543, -22.095625 -19.734434 4.647760, -21.967199 -19.660522 4.888289, -21.429985 -19.280357 5.166523, -20.632910 -18.480015 5.393541, -19.543308 -17.256512 5.518304, -18.047758 -15.871251 5.558785, -16.283701 -14.371198 5.470643, -14.186600 -12.677977 5.209732, -11.789869 -11.024081 4.815240, -8.939701 -9.322451 4.210220, -5.892527 -7.625653 3.474303, -2.567857 -5.987220 2.578479, 0.795667 -4.375169 1.685920, 3.973447 -2.615374 0.847807, 7.075397 -0.889950 0.003065, 9.755356 0.641926 -0.648580, 12.215673 1.948186 -1.232310, 14.267735 2.838712 -1.468818, 16.079765 3.212817 -1.741001, 17.399956 3.313691 -1.882475, 18.347416 3.244535 -1.893683, 19.103045 2.953984 -1.766370, 19.661901 2.577345 -1.612315, 19.979565 2.185236 -1.375020, 20.088381 1.791231 -1.151553, 20.024801 1.600054 -0.989127, 19.902586 1.475175 -0.726921, 19.627733 1.458248 -0.768719, 19.397228 1.549124 -0.713304, 19.076544 1.609861 -0.714507, 18.747389 1.609138 -0.665342, 18.302849 1.477974 -0.702418, 17.870676 1.314101 -0.615304, 17.388840 1.062937 -0.623808, 16.809483 0.911922 -0.512228, 16.231375 0.758996 -0.399057, 15.600908 0.644100 -0.341089, 14.944809 0.509224 -0.146401, 14.480840 0.336597 0.016611, 13.964165 0.138066 0.142826, 13.538626 -0.114702 0.102399, 13.140038 -0.390212 0.151931, 12.933104 -0.515529 0.147818, 12.754726 -0.558689 0.141563, 12.476332 -0.478629 0.091232, 12.245532 -0.437340 0.197140, 11.937628 -0.348882 0.181626, 11.747863 -0.099107 0.198749, 11.669934 0.019006 0.219649, 11.648956 0.142596 0.196154, 11.682013 0.140273 0.131031, 11.632658 0.263233 0.027905, 11.530915 0.133038 -0.009244, 11.445556 0.084607 -0.064783, 11.110202 0.037738 -0.027838, 10.630076 -0.146873 -0.023565, 10.025872 -0.215680 0.054052, 9.422285 -0.284748 0.133496, 8.894746 -0.303637 0.241074, 8.429388 -0.345042 0.337556, 8.177369 -0.520231 0.352241
#Interpolator16_RightCollar channels [48..50] sends animation values to BVH JOINT RightCollar, DEF BvhConversion1_RightCollar, <HAnimJoint name=RightCollar/>
OrientationInterpolator334 = x3d.OrientationInterpolator()
OrientationInterpolator334.DEF = "Interpolator16_RightCollar"
OrientationInterpolator334.key = [0,0.0035,0.007,0.0105,0.014,0.0175,0.0211,0.0246,0.0281,0.0316,0.0351,0.0386,0.0421,0.0456,0.0491,0.0526,0.0561,0.0596,0.0632,0.0667,0.0702,0.0737,0.0772,0.0807,0.0842,0.0877,0.0912,0.0947,0.0982,0.1018,0.1053,0.1088,0.1123,0.1158,0.1193,0.1228,0.1263,0.1298,0.1333,0.1368,0.1404,0.1439,0.1474,0.1509,0.1544,0.1579,0.1614,0.1649,0.1684,0.1719,0.1754,0.1789,0.1825,0.186,0.1895,0.193,0.1965,0.2,0.2035,0.207,0.2105,0.214,0.2175,0.2211,0.2246,0.2281,0.2316,0.2351,0.2386,0.2421,0.2456,0.2491,0.2526,0.2561,0.2596,0.2632,0.2667,0.2702,0.2737,0.2772,0.2807,0.2842,0.2877,0.2912,0.2947,0.2982,0.3018,0.3053,0.3088,0.3123,0.3158,0.3193,0.3228,0.3263,0.3298,0.3333,0.3368,0.3404,0.3439,0.3474,0.3509,0.3544,0.3579,0.3614,0.3649,0.3684,0.3719,0.3754,0.3789,0.3825,0.386,0.3895,0.393,0.3965,0.4,0.4035,0.407,0.4105,0.414,0.4175,0.4211,0.4246,0.4281,0.4316,0.4351,0.4386,0.4421,0.4456,0.4491,0.4526,0.4561,0.4596,0.4632,0.4667,0.4702,0.4737,0.4772,0.4807,0.4842,0.4877,0.4912,0.4947,0.4982,0.5018,0.5053,0.5088,0.5123,0.5158,0.5193,0.5228,0.5263,0.5298,0.5333,0.5368,0.5404,0.5439,0.5474,0.5509,0.5544,0.5579,0.5614,0.5649,0.5684,0.5719,0.5754,0.5789,0.5825,0.586,0.5895,0.593,0.5965,0.6,0.6035,0.607,0.6105,0.614,0.6175,0.6211,0.6246,0.6281,0.6316,0.6351,0.6386,0.6421,0.6456,0.6491,0.6526,0.6561,0.6596,0.6632,0.6667,0.6702,0.6737,0.6772,0.6807,0.6842,0.6877,0.6912,0.6947,0.6982,0.7018,0.7053,0.7088,0.7123,0.7158,0.7193,0.7228,0.7263,0.7298,0.7333,0.7368,0.7404,0.7439,0.7474,0.7509,0.7544,0.7579,0.7614,0.7649,0.7684,0.7719,0.7754,0.7789,0.7825,0.786,0.7895,0.793,0.7965,0.8,0.8035,0.807,0.8105,0.814,0.8175,0.8211,0.8246,0.8281,0.8316,0.8351,0.8386,0.8421,0.8456,0.8491,0.8526,0.8561,0.8596,0.8632,0.8667,0.8702,0.8737,0.8772,0.8807,0.8842,0.8877,0.8912,0.8947,0.8982,0.9018,0.9053,0.9088,0.9123,0.9158,0.9193,0.9228,0.9263,0.9298,0.9333,0.9368,0.9404,0.9439,0.9474,0.9509,0.9544,0.9579,0.9614,0.9649,0.9684,0.9719,0.9754,0.9789,0.9825,0.986,0.9895,0.993,0.9965,1]

Group313.children.append(OrientationInterpolator334)
#Euler angle triplet values, CHANNELS Zrotation Xrotation Yrotation, with min/max ranges [-1.0E-6,4.9E-324], [-2.0E-6,1.0E-6], [-6.0E-6,4.0E-6] degrees
#-0.000000 -0.000000 0.000001, -0.000000 -0.000001 0.000004, -0.000000 0.000000 -0.000003, -0.000000 -0.000000 -0.000006, -0.000000 -0.000000 -0.000006, -0.000000 -0.000000 -0.000006, -0.000000 -0.000000 -0.000006, -0.000000 0.000000 -0.000003, -0.000000 -0.000000 -0.000001, -0.000000 0.000001 -0.000001, -0.000000 -0.000001 0.000003, -0.000000 0.000000 0.000001, -0.000000 -0.000000 -0.000004, -0.000001 0.000000 -0.000005, -0.000001 0.000000 -0.000003, -0.000001 0.000000 -0.000000, -0.000001 0.000001 -0.000003, -0.000000 -0.000000 0.000002, -0.000001 -0.000000 -0.000001, 0.000000 0.000000 -0.000002, -0.000001 -0.000000 0.000003, -0.000000 0.000001 -0.000005, -0.000000 -0.000000 -0.000005, -0.000001 0.000000 -0.000001, -0.000001 -0.000001 0.000003, -0.000001 -0.000000 -0.000001, -0.000000 -0.000000 -0.000003, -0.000001 0.000000 -0.000001, -0.000000 0.000000 0.000003, -0.000001 -0.000000 -0.000001, -0.000001 -0.000000 0.000002, -0.000000 0.000000 -0.000001, -0.000001 -0.000001 0.000001, -0.000000 -0.000000 -0.000002, 0.000000 0.000000 -0.000003, -0.000000 -0.000001 0.000002, -0.000000 -0.000000 -0.000002, -0.000000 -0.000000 -0.000003, -0.000000 -0.000000 -0.000002, -0.000000 -0.000000 -0.000001, -0.000000 -0.000000 0.000003, -0.000000 -0.000000 0.000002, -0.000001 -0.000000 -0.000000, -0.000000 -0.000000 -0.000004, -0.000001 -0.000000 -0.000001, -0.000000 -0.000000 -0.000002, -0.000000 -0.000000 -0.000000, -0.000001 -0.000000 0.000003, -0.000001 0.000000 -0.000002, -0.000000 -0.000000 -0.000000, -0.000001 -0.000001 0.000003, -0.000001 -0.000000 0.000001, -0.000000 -0.000000 0.000002, -0.000000 -0.000000 -0.000001, -0.000000 -0.000000 -0.000001, -0.000000 0.000000 -0.000002, -0.000001 -0.000000 -0.000001, 0.000000 -0.000000 -0.000002, -0.000001 0.000000 -0.000005, -0.000000 0.000001 -0.000003, -0.000001 -0.000000 -0.000001, -0.000000 0.000000 -0.000002, -0.000000 -0.000001 -0.000002, -0.000000 0.000000 -0.000001, -0.000000 -0.000001 -0.000000, -0.000001 0.000001 -0.000002, -0.000000 -0.000000 0.000001, -0.000000 -0.000001 0.000001, 0.000000 -0.000000 -0.000000, 0.000000 -0.000000 -0.000003, -0.000001 -0.000000 0.000000, -0.000001 -0.000001 0.000000, -0.000001 0.000000 0.000000, 0.000000 0.000001 -0.000003, -0.000000 -0.000000 -0.000001, -0.000000 -0.000000 -0.000001, -0.000001 -0.000000 -0.000000, -0.000001 -0.000000 0.000002, -0.000000 -0.000001 -0.000002, -0.000000 -0.000001 -0.000004, -0.000000 0.000000 0.000002, -0.000000 -0.000000 -0.000002, 0.000000 0.000000 -0.000003, -0.000001 -0.000000 -0.000003, -0.000000 -0.000000 -0.000001, -0.000000 -0.000000 -0.000002, 0.000000 0.000000 -0.000003, -0.000001 -0.000000 0.000000, -0.000000 -0.000001 -0.000001, -0.000001 0.000000 0.000000, -0.000000 0.000000 -0.000000, -0.000000 0.000000 -0.000006, -0.000001 -0.000000 -0.000005, -0.000001 0.000000 -0.000001, -0.000000 -0.000000 -0.000002, -0.000000 -0.000000 -0.000003, -0.000000 0.000000 0.000002, -0.000001 0.000000 -0.000003, 0.000000 -0.000000 -0.000002, -0.000000 -0.000000 0.000002, -0.000001 0.000000 0.000000, -0.000000 0.000000 -0.000001, -0.000000 -0.000000 -0.000003, -0.000000 -0.000000 -0.000000, -0.000000 0.000000 -0.000002, 0.000000 -0.000000 -0.000002, -0.000001 -0.000000 0.000001, -0.000001 -0.000000 0.000002, -0.000000 0.000000 0.000002, -0.000000 0.000000 -0.000003, 0.000000 0.000001 -0.000002, -0.000001 -0.000000 -0.000003, -0.000001 -0.000000 -0.000003, -0.000001 0.000000 -0.000004, -0.000000 0.000000 -0.000004, -0.000001 -0.000000 -0.000004, -0.000000 0.000000 -0.000001, -0.000001 0.000000 -0.000001, -0.000001 -0.000001 -0.000002, -0.000000 0.000001 -0.000003, -0.000001 -0.000001 0.000000, -0.000000 -0.000001 0.000000, 0.000000 0.000001 -0.000003, -0.000001 -0.000000 0.000002, -0.000000 -0.000001 0.000001, -0.000000 0.000000 -0.000001, -0.000000 0.000000 -0.000003, -0.000001 -0.000000 -0.000001, -0.000001 0.000000 -0.000000, -0.000000 0.000000 -0.000003, -0.000000 -0.000001 -0.000003, -0.000001 -0.000000 -0.000002, -0.000001 0.000000 -0.000001, -0.000001 -0.000001 -0.000000, -0.000001 -0.000001 0.000001, 0.000000 -0.000000 -0.000004, 0.000000 -0.000000 -0.000002, -0.000001 0.000001 -0.000002, -0.000000 0.000000 -0.000005, 0.000000 -0.000001 0.000002, 0.000000 0.000001 -0.000003, -0.000000 -0.000001 -0.000002, -0.000000 0.000000 -0.000001, -0.000001 0.000001 -0.000002, -0.000001 0.000000 -0.000001, 0.000000 -0.000000 -0.000003, -0.000001 0.000000 -0.000003, -0.000000 -0.000001 0.000002, -0.000000 -0.000000 -0.000001, 0.000000 0.000001 -0.000003, 0.000000 -0.000000 -0.000003, -0.000001 0.000000 0.000003, -0.000001 -0.000000 0.000001, 0.000000 -0.000001 -0.000004, -0.000001 -0.000001 0.000001, 0.000000 -0.000001 -0.000003, -0.000001 -0.000001 -0.000001, -0.000000 0.000000 -0.000003, -0.000001 -0.000001 -0.000002, -0.000001 0.000000 -0.000002, -0.000001 0.000000 0.000000, -0.000000 -0.000001 0.000001, 0.000000 0.000000 -0.000002, -0.000000 -0.000000 -0.000002, -0.000001 0.000000 -0.000001, -0.000001 0.000001 0.000000, -0.000000 0.000000 -0.000001, -0.000000 -0.000000 -0.000004, -0.000001 0.000001 -0.000001, -0.000001 0.000000 -0.000000, 0.000000 -0.000002 -0.000001, 0.000000 -0.000001 -0.000003, -0.000001 -0.000001 -0.000001, -0.000001 -0.000000 -0.000004, -0.000000 -0.000001 -0.000003, -0.000001 -0.000001 0.000001, -0.000000 -0.000000 0.000001, -0.000000 -0.000000 -0.000001, 0.000000 0.000000 0.000001, -0.000000 0.000001 -0.000003, -0.000001 0.000000 -0.000004, -0.000001 0.000000 -0.000001, -0.000001 0.000000 -0.000002, -0.000001 0.000000 -0.000002, -0.000000 0.000001 -0.000004, 0.000000 0.000001 -0.000003, -0.000001 0.000000 -0.000002, -0.000001 0.000000 -0.000001, -0.000001 -0.000000 -0.000003, 0.000000 -0.000000 -0.000003, -0.000001 -0.000000 -0.000000, -0.000001 0.000000 -0.000001, -0.000000 -0.000001 -0.000002, -0.000000 -0.000000 -0.000002, 0.000000 0.000000 -0.000004, -0.000001 -0.000000 0.000001, -0.000001 -0.000000 -0.000004, -0.000000 0.000000 0.000001, -0.000001 -0.000002 0.000001, -0.000000 0.000000 -0.000003, -0.000000 0.000001 -0.000000, -0.000001 -0.000000 0.000004, -0.000000 -0.000001 -0.000002, -0.000001 0.000001 0.000002, -0.000001 0.000000 -0.000001, 0.000000 -0.000001 -0.000002, -0.000000 -0.000001 -0.000001, -0.000000 -0.000000 0.000002, -0.000000 -0.000000 -0.000003, 0.000000 -0.000000 -0.000003, -0.000000 -0.000001 0.000003, -0.000000 -0.000001 -0.000003, -0.000001 -0.000000 0.000000, -0.000000 0.000000 0.000001, -0.000000 -0.000001 -0.000000, -0.000000 -0.000000 0.000001, 0.000000 -0.000000 -0.000002, 0.000000 -0.000001 -0.000003, 0.000000 -0.000000 0.000001, -0.000001 0.000000 0.000002, -0.000001 0.000000 -0.000002, -0.000000 0.000000 -0.000003, -0.000000 -0.000000 -0.000000, -0.000001 -0.000001 0.000001, -0.000001 0.000001 -0.000001, -0.000000 -0.000000 -0.000002, -0.000001 0.000001 -0.000005, -0.000001 -0.000000 -0.000002, -0.000001 -0.000001 -0.000002, -0.000001 0.000000 -0.000004, -0.000000 -0.000000 0.000001, -0.000001 0.000000 -0.000003, -0.000001 -0.000000 -0.000002, -0.000001 0.000001 -0.000001, 0.000000 0.000000 -0.000001, -0.000000 0.000000 0.000001, -0.000000 -0.000001 -0.000002, -0.000001 0.000001 -0.000003, -0.000000 -0.000000 0.000002, -0.000000 -0.000001 -0.000000, -0.000000 -0.000001 0.000003, -0.000001 -0.000001 0.000003, -0.000001 -0.000001 -0.000001, 0.000000 -0.000001 -0.000000, -0.000000 0.000001 -0.000001, -0.000000 0.000000 -0.000001, -0.000001 0.000000 0.000004, -0.000001 0.000001 -0.000001, 0.000000 -0.000000 -0.000001, -0.000001 -0.000001 0.000001, -0.000000 0.000001 -0.000001, -0.000001 -0.000000 -0.000001, 0.000000 0.000000 0.000001, -0.000001 -0.000002 -0.000003, -0.000000 0.000001 -0.000001, -0.000001 0.000000 0.000002, -0.000000 0.000000 -0.000003, 0.000000 -0.000000 -0.000000, 0.000000 -0.000000 -0.000001, -0.000001 -0.000000 0.000001, -0.000000 -0.000001 -0.000002, -0.000001 -0.000001 0.000001, -0.000000 0.000001 -0.000001, -0.000001 -0.000000 -0.000003, -0.000000 -0.000000 -0.000003, -0.000000 0.000001 -0.000000, -0.000001 -0.000001 -0.000000, -0.000000 -0.000001 0.000000, -0.000001 -0.000001 -0.000003, -0.000000 -0.000001 -0.000001, -0.000001 -0.000001 -0.000002, 0.000000 -0.000001 -0.000002, 0.000000 -0.000000 0.000001, -0.000001 -0.000000 -0.000001, -0.000000 -0.000000 -0.000004, -0.000001 -0.000001 0.000004, -0.000000 -0.000002 -0.000000, 0.000000 0.000000 -0.000002, -0.000001 -0.000001 -0.000002, -0.000000 -0.000001 -0.000000, -0.000000 0.000000 0.000002, 0.000000 -0.000001 -0.000002, -0.000001 0.000001 -0.000005, -0.000001 0.000001 0.000001, 0.000000 -0.000001 -0.000003, 0.000000 0.000001 -0.000002
#Interpolator17_r_shoulder channels [51..53] sends animation values to BVH JOINT RightShoulder, DEF BvhConversion1_r_shoulder, <HAnimJoint name=r_shoulder/>
OrientationInterpolator335 = x3d.OrientationInterpolator()
OrientationInterpolator335.DEF = "Interpolator17_r_shoulder"
OrientationInterpolator335.key = [0,0.0035,0.007,0.0105,0.014,0.0175,0.0211,0.0246,0.0281,0.0316,0.0351,0.0386,0.0421,0.0456,0.0491,0.0526,0.0561,0.0596,0.0632,0.0667,0.0702,0.0737,0.0772,0.0807,0.0842,0.0877,0.0912,0.0947,0.0982,0.1018,0.1053,0.1088,0.1123,0.1158,0.1193,0.1228,0.1263,0.1298,0.1333,0.1368,0.1404,0.1439,0.1474,0.1509,0.1544,0.1579,0.1614,0.1649,0.1684,0.1719,0.1754,0.1789,0.1825,0.186,0.1895,0.193,0.1965,0.2,0.2035,0.207,0.2105,0.214,0.2175,0.2211,0.2246,0.2281,0.2316,0.2351,0.2386,0.2421,0.2456,0.2491,0.2526,0.2561,0.2596,0.2632,0.2667,0.2702,0.2737,0.2772,0.2807,0.2842,0.2877,0.2912,0.2947,0.2982,0.3018,0.3053,0.3088,0.3123,0.3158,0.3193,0.3228,0.3263,0.3298,0.3333,0.3368,0.3404,0.3439,0.3474,0.3509,0.3544,0.3579,0.3614,0.3649,0.3684,0.3719,0.3754,0.3789,0.3825,0.386,0.3895,0.393,0.3965,0.4,0.4035,0.407,0.4105,0.414,0.4175,0.4211,0.4246,0.4281,0.4316,0.4351,0.4386,0.4421,0.4456,0.4491,0.4526,0.4561,0.4596,0.4632,0.4667,0.4702,0.4737,0.4772,0.4807,0.4842,0.4877,0.4912,0.4947,0.4982,0.5018,0.5053,0.5088,0.5123,0.5158,0.5193,0.5228,0.5263,0.5298,0.5333,0.5368,0.5404,0.5439,0.5474,0.5509,0.5544,0.5579,0.5614,0.5649,0.5684,0.5719,0.5754,0.5789,0.5825,0.586,0.5895,0.593,0.5965,0.6,0.6035,0.607,0.6105,0.614,0.6175,0.6211,0.6246,0.6281,0.6316,0.6351,0.6386,0.6421,0.6456,0.6491,0.6526,0.6561,0.6596,0.6632,0.6667,0.6702,0.6737,0.6772,0.6807,0.6842,0.6877,0.6912,0.6947,0.6982,0.7018,0.7053,0.7088,0.7123,0.7158,0.7193,0.7228,0.7263,0.7298,0.7333,0.7368,0.7404,0.7439,0.7474,0.7509,0.7544,0.7579,0.7614,0.7649,0.7684,0.7719,0.7754,0.7789,0.7825,0.786,0.7895,0.793,0.7965,0.8,0.8035,0.807,0.8105,0.814,0.8175,0.8211,0.8246,0.8281,0.8316,0.8351,0.8386,0.8421,0.8456,0.8491,0.8526,0.8561,0.8596,0.8632,0.8667,0.8702,0.8737,0.8772,0.8807,0.8842,0.8877,0.8912,0.8947,0.8982,0.9018,0.9053,0.9088,0.9123,0.9158,0.9193,0.9228,0.9263,0.9298,0.9333,0.9368,0.9404,0.9439,0.9474,0.9509,0.9544,0.9579,0.9614,0.9649,0.9684,0.9719,0.9754,0.9789,0.9825,0.986,0.9895,0.993,0.9965,1]

Group313.children.append(OrientationInterpolator335)
#Euler angle triplet values, CHANNELS Zrotation Xrotation Yrotation, with min/max ranges [-4.308793,6.108548], [0.028064,11.981505], [-7.903096,13.444084] degrees
#1.539841 2.825439 5.415902, 1.659198 2.753919 5.354541, 1.625498 2.669958 5.420823, 1.635851 2.710081 5.517717, 1.709246 2.751279 5.498542, 1.784128 2.736570 5.450369, 1.890162 2.572632 5.415076, 1.999269 2.449772 5.348680, 2.139033 2.591124 5.419775, 2.250012 2.633984 5.497386, 2.291157 2.606829 5.817527, 2.470241 2.565995 6.171932, 2.585234 2.544601 6.543992, 2.612884 2.503433 6.936684, 2.656961 2.539271 7.243045, 2.667868 2.709070 7.550754, 2.790483 2.770228 7.776845, 2.902675 2.836037 7.941399, 2.972895 2.791735 8.066810, 3.122263 2.815632 8.233824, 3.317151 2.772131 8.480510, 3.374153 2.794408 9.007363, 3.516791 2.842327 9.666446, 3.527120 2.886672 10.238727, 3.612417 2.904853 10.841058, 3.808820 2.735540 11.519359, 4.130212 2.477762 11.956823, 4.498990 2.207664 12.379446, 4.712445 1.963622 12.622948, 4.852257 1.880785 12.883872, 4.993766 1.753587 13.251352, 5.118576 1.729687 13.432649, 5.223372 1.650766 13.444084, 5.271639 1.639933 13.314195, 5.269379 1.598588 12.955299, 5.275953 1.532345 12.339832, 5.315741 1.423947 11.730162, 5.407961 1.337053 11.200869, 5.612225 1.365543 10.763661, 5.740685 1.362724 10.256515, 5.896593 1.507919 9.897114, 6.039891 1.626244 9.694221, 6.091292 1.741280 9.615250, 6.108548 1.777709 9.611070, 5.960849 1.954654 9.850123, 5.786687 2.032180 10.161457, 5.564275 2.141125 10.419526, 5.331964 2.204646 10.588397, 5.233246 2.204957 10.648883, 5.157654 2.175082 10.578238, 5.015079 2.180710 10.466765, 5.040973 2.221691 10.069785, 4.864235 2.267448 9.620588, 4.673319 2.565467 8.990757, 4.507741 2.776731 8.415347, 4.291955 2.944167 7.990723, 4.156141 3.077573 7.450298, 3.969330 3.421023 6.944750, 3.800106 3.895494 6.407286, 3.680072 4.353392 6.049390, 3.572792 4.765178 5.701854, 3.537423 5.036597 5.377108, 3.516724 5.241601 5.168880, 3.389826 5.267253 4.751217, 3.256528 5.307953 4.394653, 3.151973 5.315391 4.192788, 3.159031 5.312814 3.969057, 3.164854 5.178929 3.908918, 3.151274 5.086535 4.191673, 3.128397 4.980465 4.759638, 3.095225 4.877620 5.355340, 3.038961 4.686393 5.753066, 3.180666 4.505731 5.781435, 3.364690 4.258335 5.559049, 3.294290 4.034218 5.309987, 3.335736 3.753568 5.011118, 3.343917 3.552269 4.680160, 3.231652 3.430023 4.440219, 3.146148 3.385720 4.324314, 2.900862 3.325940 4.218502, 2.759282 3.214887 4.333297, 2.556682 3.114451 4.558411, 2.460793 2.983402 4.870402, 2.367981 2.666538 5.312231, 2.382555 2.262095 5.645256, 2.265176 1.952483 6.037054, 2.311145 1.646034 6.360004, 2.311090 1.413178 6.753007, 2.462139 1.243958 7.049155, 2.449759 0.927281 7.377811, 2.358125 0.754491 7.594779, 2.272150 0.761979 7.744729, 2.063609 0.756198 7.861013, 1.893547 0.781141 7.926217, 1.683758 0.675934 7.847624, 1.474561 0.569533 7.768697, 1.319386 0.562995 7.639850, 1.236512 0.601127 7.645232, 1.309789 0.570698 7.719815, 1.472613 0.493709 7.758840, 1.695318 0.435949 7.943337, 1.843556 0.352589 8.207355, 1.988597 0.577498 8.376950, 2.060283 0.759999 8.563943, 2.105997 0.845526 8.758120, 2.176740 1.023211 8.791803, 2.296736 1.137690 8.905041, 2.380599 1.321913 8.836703, 2.488762 1.432628 8.742267, 2.557031 1.647719 8.864279, 2.629366 1.845502 8.924725, 2.713435 2.065946 8.943919, 2.741401 2.210066 8.790573, 2.736133 2.593024 8.472451, 2.823940 2.898843 8.010077, 2.849713 3.237589 7.724328, 2.952813 3.529531 7.408338, 2.959594 3.700424 6.994677, 2.900391 3.840819 6.719944, 2.726928 4.028975 6.592043, 2.601432 4.159382 6.450484, 2.559361 4.139420 6.508563, 2.454687 3.982234 6.433605, 2.455359 3.556897 6.408954, 2.566662 3.076496 6.329539, 2.697830 2.525296 6.221654, 2.766888 2.034380 6.260426, 2.778461 1.545180 6.406199, 2.769111 1.220695 6.586525, 2.589489 1.037459 6.783438, 2.323725 0.815493 7.013365, 2.223831 0.585443 7.110412, 2.071923 0.374639 7.098576, 1.941470 0.268589 6.987932, 1.888927 0.104129 6.714764, 1.923086 0.028064 6.143245, 1.922718 0.033475 5.543188, 1.943688 0.171336 5.038196, 1.919272 0.331167 4.424983, 2.058617 0.717184 3.856963, 2.031932 0.965127 3.236427, 2.202439 1.331844 2.523175, 2.389669 1.716919 1.645444, 2.538263 2.039088 0.705599, 2.787350 2.317533 -0.289975, 3.047571 2.744570 -1.189415, 3.227982 3.156201 -2.076316, 3.393687 3.502913 -2.771553, 3.492766 3.797110 -3.578935, 3.517079 4.061381 -4.362130, 3.440013 4.223393 -5.219701, 3.315510 4.378778 -6.015869, 3.102353 4.527208 -6.799446, 2.701454 4.728346 -7.290344, 2.261339 4.850821 -7.415062, 1.765894 5.107989 -7.200192, 1.147201 5.350907 -6.669604, 0.433984 5.868917 -6.129395, -0.208987 6.102906 -5.703598, -0.709043 6.334280 -5.260380, -1.195441 6.403401 -4.952821, -1.613637 6.342876 -4.732400, -1.946252 6.139285 -4.630992, -2.284751 5.745710 -4.400836, -2.566453 5.207935 -3.989599, -2.654719 4.636758 -3.665329, -2.598872 4.050777 -3.254033, -2.461914 3.494283 -2.870508, -2.365506 3.036685 -2.370260, -2.190458 2.645703 -2.020924, -2.044405 2.386040 -1.672496, -1.806243 2.136882 -1.342669, -1.772130 1.966045 -1.019295, -1.672569 1.917788 -0.840526, -1.583862 1.884591 -0.574792, -1.552768 1.850197 -0.197349, -1.557191 1.856274 0.185883, -1.489060 1.893858 0.546103, -1.364708 1.929209 0.998751, -1.204258 2.040278 1.434860, -1.066379 2.221556 1.906642, -0.785329 2.426634 2.304550, -0.453607 2.540488 2.584233, -0.123354 2.657879 2.863242, 0.048837 2.903327 3.122849, 0.272679 3.105040 3.291274, 0.416843 3.420251 3.429887, 0.545781 3.749540 3.509463, 0.577116 4.160682 3.669850, 0.630882 4.498604 3.646070, 0.731767 4.768635 3.695891, 0.726295 5.097736 3.993843, 0.790838 5.286163 4.430202, 0.921510 5.635983 4.886602, 0.925345 5.977057 5.325645, 0.963962 6.237135 5.789543, 0.914775 6.424888 6.242757, 0.962084 6.534754 6.611441, 0.831744 6.522065 7.102596, 0.690237 6.423434 7.529771, 0.526641 6.171502 7.815439, 0.435730 5.791489 7.929120, 0.433454 5.251531 7.893014, 0.422588 4.626759 7.790867, 0.675379 3.971329 7.489743, 0.896302 3.488851 7.137039, 1.063474 3.071782 6.710490, 1.220587 2.693421 6.534095, 1.277549 2.433432 6.272878, 1.274875 2.265517 6.127219, 1.201453 2.057799 6.006757, 1.141561 1.935118 5.952320, 1.009097 1.835118 5.625164, 0.819902 1.781654 5.389270, 0.663021 1.849666 5.104369, 0.652524 1.940477 4.688197, 0.608456 2.183239 4.264184, 0.639023 2.465538 3.815193, 0.664872 2.773503 3.557142, 0.671515 3.101393 3.306823, 0.444170 3.566520 2.993821, 0.242243 4.020555 2.541180, 0.127226 4.584747 1.727443, -0.120776 5.057913 0.833752, -0.201914 5.571814 -0.361316, -0.303451 6.159817 -1.471791, -0.557985 6.743077 -2.558703, -0.794591 7.312361 -3.588281, -1.129012 7.881477 -4.498874, -1.496181 8.389862 -5.334077, -1.886650 8.883523 -6.098204, -2.223527 9.358481 -6.822636, -2.681435 9.907380 -7.389225, -3.146455 10.488713 -7.762302, -3.486883 11.070706 -7.903096, -3.837596 11.475283 -7.817317, -3.998698 11.769812 -7.491693, -4.256133 11.981505 -6.845989, -4.308793 11.925361 -6.116582, -4.141274 11.672716 -5.127547, -3.887588 11.394709 -4.239806, -3.763989 11.143174 -3.538801, -3.601629 10.827950 -2.882778, -3.523323 10.494513 -2.254569, -3.536868 10.082382 -1.578667, -3.568114 9.534146 -0.997120, -3.438276 9.013334 -0.452506, -3.333298 8.365539 0.050015, -3.132158 7.603348 0.530259, -2.914954 6.964976 0.925065, -2.596121 6.243224 1.230830, -2.321784 5.565041 1.539007, -1.949505 5.132383 1.838022, -1.691550 4.597380 2.238838, -1.390545 4.183148 2.594195, -1.117559 3.818260 3.029668, -0.954387 3.559994 3.550543, -0.766372 3.332531 4.108601, -0.640401 2.965731 4.735943, -0.458969 2.729020 5.394960, -0.220335 2.451936 5.967710, 0.014559 2.329088 6.641727, 0.262680 2.399180 7.179081, 0.361503 2.891956 7.672117, 0.431204 3.237390 8.289264, 0.436771 3.628849 8.653377, 0.463122 4.061896 8.753965, 0.426688 4.607890 8.616160, 0.328956 5.231747 8.348691, 0.227031 5.761292 8.069072, 0.041215 6.325610 7.776369, -0.104384 6.876001 7.587522, -0.178945 7.263827 7.333302, -0.243991 7.732790 7.148040, -0.438410 8.030734 6.847092, -0.455722 8.418845 6.530881, -0.498692 8.782389 6.220225, -0.598981 9.195501 5.907287, -0.892859 9.639155 5.865096, -1.188982 10.081673 5.826207, -1.429893 10.296177 5.707324, -1.669778 10.373792 5.494705, -1.848853 10.419980 5.182458, -1.991358 10.385781 4.887197, -2.133324 10.352474 4.590765, -2.063855 10.208699 4.250721
#Interpolator18_r_elbow channels [54..56] sends animation values to BVH JOINT RightElbow, DEF BvhConversion1_r_elbow, <HAnimJoint name=r_elbow/>
OrientationInterpolator336 = x3d.OrientationInterpolator()
OrientationInterpolator336.DEF = "Interpolator18_r_elbow"
OrientationInterpolator336.key = [0,0.0035,0.007,0.0105,0.014,0.0175,0.0211,0.0246,0.0281,0.0316,0.0351,0.0386,0.0421,0.0456,0.0491,0.0526,0.0561,0.0596,0.0632,0.0667,0.0702,0.0737,0.0772,0.0807,0.0842,0.0877,0.0912,0.0947,0.0982,0.1018,0.1053,0.1088,0.1123,0.1158,0.1193,0.1228,0.1263,0.1298,0.1333,0.1368,0.1404,0.1439,0.1474,0.1509,0.1544,0.1579,0.1614,0.1649,0.1684,0.1719,0.1754,0.1789,0.1825,0.186,0.1895,0.193,0.1965,0.2,0.2035,0.207,0.2105,0.214,0.2175,0.2211,0.2246,0.2281,0.2316,0.2351,0.2386,0.2421,0.2456,0.2491,0.2526,0.2561,0.2596,0.2632,0.2667,0.2702,0.2737,0.2772,0.2807,0.2842,0.2877,0.2912,0.2947,0.2982,0.3018,0.3053,0.3088,0.3123,0.3158,0.3193,0.3228,0.3263,0.3298,0.3333,0.3368,0.3404,0.3439,0.3474,0.3509,0.3544,0.3579,0.3614,0.3649,0.3684,0.3719,0.3754,0.3789,0.3825,0.386,0.3895,0.393,0.3965,0.4,0.4035,0.407,0.4105,0.414,0.4175,0.4211,0.4246,0.4281,0.4316,0.4351,0.4386,0.4421,0.4456,0.4491,0.4526,0.4561,0.4596,0.4632,0.4667,0.4702,0.4737,0.4772,0.4807,0.4842,0.4877,0.4912,0.4947,0.4982,0.5018,0.5053,0.5088,0.5123,0.5158,0.5193,0.5228,0.5263,0.5298,0.5333,0.5368,0.5404,0.5439,0.5474,0.5509,0.5544,0.5579,0.5614,0.5649,0.5684,0.5719,0.5754,0.5789,0.5825,0.586,0.5895,0.593,0.5965,0.6,0.6035,0.607,0.6105,0.614,0.6175,0.6211,0.6246,0.6281,0.6316,0.6351,0.6386,0.6421,0.6456,0.6491,0.6526,0.6561,0.6596,0.6632,0.6667,0.6702,0.6737,0.6772,0.6807,0.6842,0.6877,0.6912,0.6947,0.6982,0.7018,0.7053,0.7088,0.7123,0.7158,0.7193,0.7228,0.7263,0.7298,0.7333,0.7368,0.7404,0.7439,0.7474,0.7509,0.7544,0.7579,0.7614,0.7649,0.7684,0.7719,0.7754,0.7789,0.7825,0.786,0.7895,0.793,0.7965,0.8,0.8035,0.807,0.8105,0.814,0.8175,0.8211,0.8246,0.8281,0.8316,0.8351,0.8386,0.8421,0.8456,0.8491,0.8526,0.8561,0.8596,0.8632,0.8667,0.8702,0.8737,0.8772,0.8807,0.8842,0.8877,0.8912,0.8947,0.8982,0.9018,0.9053,0.9088,0.9123,0.9158,0.9193,0.9228,0.9263,0.9298,0.9333,0.9368,0.9404,0.9439,0.9474,0.9509,0.9544,0.9579,0.9614,0.9649,0.9684,0.9719,0.9754,0.9789,0.9825,0.986,0.9895,0.993,0.9965,1]

Group313.children.append(OrientationInterpolator336)
#Euler angle triplet values, CHANNELS Zrotation Xrotation Yrotation, with min/max ranges [-8.160302,4.9E-324], [-10.282856,5.709675], [-18.069595,4.9E-324] degrees
#-3.038276 -2.695683 -17.044260, -3.173039 -2.685500 -16.975225, -3.236759 -2.694288 -16.951908, -3.278201 -2.801277 -16.891127, -3.354454 -2.836097 -16.877422, -3.425246 -2.816996 -16.831570, -3.513221 -2.645918 -16.790714, -3.435343 -2.459249 -16.666903, -3.381774 -2.348616 -16.614628, -3.279579 -2.031565 -16.627829, -3.207361 -1.611960 -16.738003, -3.355053 -1.024369 -16.777802, -3.476483 -0.548868 -16.622627, -3.632224 0.051148 -16.368502, -3.857817 0.529835 -16.152891, -4.076652 0.825428 -15.927710, -4.259197 1.184264 -15.810665, -4.350909 1.468075 -15.821504, -4.533524 1.624662 -15.840855, -4.563967 1.719429 -15.970753, -4.747699 1.855510 -16.153070, -4.804778 1.829579 -16.352146, -4.859013 1.672150 -16.502810, -4.715123 1.345039 -16.511299, -4.612236 0.987203 -16.513512, -4.488900 0.496315 -16.452084, -4.277091 -0.014433 -16.404318, -4.152136 -0.661875 -16.263243, -3.935186 -1.345443 -16.187069, -3.641361 -2.098724 -16.049826, -3.380809 -2.788617 -16.011442, -3.108384 -3.592112 -15.856604, -2.932581 -4.310992 -15.619919, -2.817217 -5.092356 -15.370347, -2.493457 -5.877699 -15.055402, -2.149905 -6.544142 -14.651957, -1.797365 -7.041009 -14.439983, -1.420419 -7.410280 -14.353994, -1.308529 -7.635469 -14.538056, -1.126749 -7.608803 -14.611930, -1.020082 -7.425097 -14.737721, -1.016794 -7.048173 -14.871422, -1.007247 -6.486712 -15.067690, -1.189975 -5.746553 -15.391425, -1.229824 -5.161088 -15.871852, -1.192246 -4.511606 -16.365561, -1.318885 -4.118335 -16.781076, -1.342288 -3.766446 -17.067190, -1.448619 -3.486931 -17.161886, -1.601565 -3.262657 -17.099051, -1.793190 -2.936534 -16.919312, -1.964202 -2.786063 -16.687321, -1.938324 -2.768300 -16.505754, -1.931621 -2.942194 -16.268528, -1.813756 -3.211833 -16.135675, -1.673150 -3.500592 -15.921735, -1.645820 -3.893785 -15.801250, -1.701528 -4.206222 -15.777701, -1.701863 -4.380197 -15.677043, -1.753378 -4.440660 -15.808029, -1.890803 -4.320504 -16.070265, -2.103883 -4.072744 -16.359219, -2.266168 -3.782611 -16.674627, -2.360082 -3.396589 -16.739115, -2.548197 -3.093726 -16.716755, -2.732032 -2.723082 -16.759661, -2.959556 -2.459800 -16.735064, -3.290191 -2.053090 -16.865265, -3.616567 -1.668126 -17.187088, -4.029756 -1.291964 -17.510679, -4.285402 -0.922668 -17.902458, -4.596975 -0.763990 -18.057606, -4.823849 -0.781917 -18.069595, -4.977468 -0.936215 -17.891865, -4.850467 -1.167652 -17.747738, -4.721468 -1.398168 -17.603384, -4.585950 -1.722516 -17.341312, -4.521121 -2.025128 -17.216402, -4.479328 -2.404128 -17.162111, -4.312415 -2.779205 -17.028156, -4.172729 -2.908540 -17.032942, -3.986545 -3.068475 -16.943409, -3.983059 -3.023073 -16.888325, -3.970985 -2.785855 -16.898561, -4.137971 -2.438227 -16.747780, -4.170830 -2.174591 -16.711040, -4.368653 -1.924734 -16.751036, -4.448112 -1.791273 -16.772465, -4.501572 -1.696519 -16.725254, -4.423375 -1.578365 -16.648880, -4.348835 -1.622044 -16.538143, -4.175269 -1.905891 -16.382244, -3.978975 -2.248515 -16.228172, -3.825432 -2.586305 -16.060329, -3.605387 -2.808180 -15.799911, -3.403504 -3.100324 -15.722653, -3.227839 -3.308984 -15.617292, -3.141369 -3.413703 -15.542647, -3.208451 -3.364660 -15.611465, -3.281017 -2.995975 -15.619033, -3.430947 -2.534379 -15.890022, -3.666496 -1.995761 -16.032291, -3.842694 -1.616750 -16.232506, -3.949810 -1.165554 -16.374557, -4.072503 -0.603533 -16.483177, -4.071422 -0.251453 -16.456547, -4.189995 0.214822 -16.449043, -4.309131 0.681010 -16.441822, -4.428824 1.147060 -16.434889, -4.571921 1.511583 -16.662092, -4.712132 1.853672 -16.728462, -4.936398 2.150735 -16.879774, -5.168016 2.504873 -16.866949, -5.332204 2.595946 -16.686460, -5.432518 2.554886 -16.640411, -5.362354 2.417797 -16.720587, -5.379704 2.108207 -16.712255, -5.384888 1.679484 -16.536917, -5.387121 1.250719 -16.362545, -5.294126 0.722933 -16.162024, -5.403421 0.105981 -16.029760, -5.561680 -0.531403 -15.996744, -5.618670 -1.217334 -16.057964, -5.666011 -1.993023 -16.145769, -5.669467 -2.724350 -16.267532, -5.556999 -3.404562 -16.406202, -5.552644 -4.125546 -16.560493, -5.502465 -4.878236 -16.624048, -5.398194 -5.532483 -16.675850, -5.233820 -6.257142 -16.741028, -5.051181 -6.890786 -16.559603, -5.016611 -7.521632 -16.304754, -4.826764 -8.061856 -15.930412, -4.609095 -8.621869 -15.422084, -4.280745 -9.201862 -15.011819, -4.068963 -9.642343 -14.616755, -3.802355 -10.024055 -14.392312, -3.624519 -10.242434 -14.361278, -3.428979 -10.282856 -14.237968, -3.375526 -10.175319 -14.316247, -3.378019 -9.816749 -14.313488, -3.493426 -9.231596 -14.278891, -3.606248 -8.516576 -14.270102, -3.686031 -7.426723 -14.204406, -3.793452 -6.261422 -14.222913, -3.953795 -5.083272 -14.429641, -4.229689 -3.850737 -14.880258, -4.523220 -2.600339 -15.418481, -4.929790 -1.388736 -15.744285, -5.331033 -0.205299 -15.907869, -5.865220 0.953404 -15.799833, -6.427789 2.067583 -15.492693, -6.989959 3.040758 -15.137938, -7.475790 3.906011 -14.878198, -7.753129 4.665461 -14.837188, -7.961443 5.239381 -14.800323, -8.157948 5.697874 -14.804476, -8.160302 5.709675 -14.729602, -8.108832 5.656813 -14.607107, -8.062877 5.198779 -14.584909, -8.034842 4.724060 -14.626186, -7.714232 4.030589 -14.662586, -7.420038 3.356771 -14.586955, -7.070675 2.668756 -14.563965, -6.743892 1.926469 -14.577709, -6.494870 1.181460 -14.496901, -6.422644 0.533110 -14.489091, -6.426718 -0.114196 -14.384882, -6.421210 -0.766008 -14.378004, -6.354543 -1.441554 -14.305281, -6.190893 -2.166905 -14.214726, -6.088057 -2.799737 -14.126286, -5.726153 -3.441199 -13.923828, -5.409429 -4.067279 -13.604625, -5.049684 -4.605231 -13.237341, -4.578748 -5.064677 -12.871148, -4.197196 -5.418097 -12.566969, -3.908481 -5.663916 -12.281560, -3.492779 -5.881174 -12.112642, -3.342621 -6.064600 -12.115916, -3.096595 -6.094299 -12.246515, -3.001761 -6.191358 -12.638146, -2.843435 -6.094708 -13.110293, -2.709600 -6.070873 -13.768378, -2.523210 -6.127499 -14.351709, -2.439274 -6.092661 -14.929269, -2.208709 -6.068038 -15.467223, -1.990504 -6.064586 -15.863581, -1.855038 -6.013410 -16.197268, -1.783591 -5.973846 -16.280436, -1.838669 -5.828228 -16.386497, -1.912972 -5.591213 -16.574574, -1.989810 -5.171443 -16.839060, -2.240697 -4.734076 -17.119286, -2.496378 -4.375818 -17.120008, -2.784879 -3.893279 -17.021999, -3.065461 -3.477067 -16.907904, -3.520414 -3.188282 -16.612190, -3.789351 -3.061322 -16.158243, -4.036616 -3.067680 -15.773149, -4.225785 -3.099444 -15.394328, -4.342393 -3.408832 -15.052974, -4.437232 -3.776436 -14.908484, -4.466722 -4.032012 -14.975649, -4.482490 -4.350502 -15.127823, -4.617665 -4.686294 -15.451461, -4.723429 -4.960260 -15.743101, -4.888343 -5.210808 -16.024220, -5.044889 -5.385431 -16.297741, -5.171616 -5.461156 -16.407885, -5.156779 -5.346757 -16.308485, -5.206849 -5.190795 -16.181595, -5.198350 -5.056809 -15.717059, -5.127759 -4.783499 -15.418278, -5.050268 -4.413500 -15.087887, -5.106794 -3.983332 -14.792031, -5.023747 -3.691200 -14.591442, -4.959146 -3.324800 -14.465294, -4.937855 -2.893326 -14.507779, -4.913650 -2.414562 -14.523329, -4.806451 -1.972258 -14.448750, -4.706628 -1.560109 -14.355755, -4.725446 -1.050610 -14.058448, -4.656411 -0.513013 -13.806784, -4.599262 -0.136076 -13.666937, -4.663968 0.151719 -13.472824, -4.494621 0.405155 -13.479307, -4.401703 0.521072 -13.494617, -4.177505 0.592830 -13.647253, -3.999979 0.701447 -13.562801, -3.690526 0.635654 -13.375665, -3.436717 0.662739 -13.244077, -3.047838 0.718211 -13.065136, -2.641462 0.760650 -13.071710, -2.374731 0.865120 -13.115138, -2.326155 1.223751 -13.234367, -2.415203 1.665728 -13.355845, -2.579600 2.205733 -13.506387, -2.791139 2.866711 -13.738086, -3.099147 3.421233 -14.122196, -3.388671 3.866669 -14.549656, -3.447136 3.883948 -14.860752, -3.346375 3.636161 -14.930720, -3.106962 3.182895 -15.085898, -2.775019 2.682554 -15.091341, -2.518915 2.171450 -15.007937, -2.492671 1.629894 -14.987034, -2.484140 1.061870 -14.950997, -2.579654 0.540425 -15.085224, -2.765895 -0.022803 -15.259145, -2.969134 -0.637610 -15.553392, -3.107171 -1.212788 -15.910526, -3.275892 -2.007213 -16.246847, -3.288092 -2.752848 -16.533842, -3.341343 -3.410985 -16.683447, -3.259386 -4.085835 -16.663784, -3.216225 -4.691795 -16.574009, -3.157616 -5.238605 -16.477602, -3.105029 -5.639218 -16.239717, -3.001349 -5.962741 -16.035425, -2.996213 -6.189526 -15.828755, -3.010047 -6.329943 -15.621245, -3.048723 -6.594464 -15.363843, -3.045230 -7.045184 -15.178311, -3.054850 -7.142027 -15.029889, -3.050027 -7.072591 -14.585212, -3.163747 -6.768710 -14.185226, -3.161337 -6.466885 -13.685386, -3.077846 -6.248502 -13.467278, -2.983431 -5.858132 -13.291263, -2.783285 -5.565953 -13.269973, -2.552565 -5.115181 -13.338671, -2.331740 -4.594043 -13.368472, -2.228406 -4.076259 -13.343527, -2.114330 -3.298835 -13.166446, -2.150629 -2.629865 -12.988220, -2.111004 -1.804738 -12.894673, -2.122947 -1.239660 -12.800999, -2.024437 -0.737047 -12.807662, -1.919426 -0.333254 -12.696501, -1.834022 0.062192 -12.554565, -1.764251 0.336037 -12.426515, -1.786777 0.560324 -12.253061, -1.723755 0.683519 -12.317791, -1.635900 0.609710 -12.529258, -1.505791 0.536854 -12.893166
#Interpolator19_r_wrist channels [57..59] sends animation values to BVH JOINT RightWrist, DEF BvhConversion1_r_wrist, <HAnimJoint name=r_wrist/>
OrientationInterpolator337 = x3d.OrientationInterpolator()
OrientationInterpolator337.DEF = "Interpolator19_r_wrist"
OrientationInterpolator337.key = [0,0.0035,0.007,0.0105,0.014,0.0175,0.0211,0.0246,0.0281,0.0316,0.0351,0.0386,0.0421,0.0456,0.0491,0.0526,0.0561,0.0596,0.0632,0.0667,0.0702,0.0737,0.0772,0.0807,0.0842,0.0877,0.0912,0.0947,0.0982,0.1018,0.1053,0.1088,0.1123,0.1158,0.1193,0.1228,0.1263,0.1298,0.1333,0.1368,0.1404,0.1439,0.1474,0.1509,0.1544,0.1579,0.1614,0.1649,0.1684,0.1719,0.1754,0.1789,0.1825,0.186,0.1895,0.193,0.1965,0.2,0.2035,0.207,0.2105,0.214,0.2175,0.2211,0.2246,0.2281,0.2316,0.2351,0.2386,0.2421,0.2456,0.2491,0.2526,0.2561,0.2596,0.2632,0.2667,0.2702,0.2737,0.2772,0.2807,0.2842,0.2877,0.2912,0.2947,0.2982,0.3018,0.3053,0.3088,0.3123,0.3158,0.3193,0.3228,0.3263,0.3298,0.3333,0.3368,0.3404,0.3439,0.3474,0.3509,0.3544,0.3579,0.3614,0.3649,0.3684,0.3719,0.3754,0.3789,0.3825,0.386,0.3895,0.393,0.3965,0.4,0.4035,0.407,0.4105,0.414,0.4175,0.4211,0.4246,0.4281,0.4316,0.4351,0.4386,0.4421,0.4456,0.4491,0.4526,0.4561,0.4596,0.4632,0.4667,0.4702,0.4737,0.4772,0.4807,0.4842,0.4877,0.4912,0.4947,0.4982,0.5018,0.5053,0.5088,0.5123,0.5158,0.5193,0.5228,0.5263,0.5298,0.5333,0.5368,0.5404,0.5439,0.5474,0.5509,0.5544,0.5579,0.5614,0.5649,0.5684,0.5719,0.5754,0.5789,0.5825,0.586,0.5895,0.593,0.5965,0.6,0.6035,0.607,0.6105,0.614,0.6175,0.6211,0.6246,0.6281,0.6316,0.6351,0.6386,0.6421,0.6456,0.6491,0.6526,0.6561,0.6596,0.6632,0.6667,0.6702,0.6737,0.6772,0.6807,0.6842,0.6877,0.6912,0.6947,0.6982,0.7018,0.7053,0.7088,0.7123,0.7158,0.7193,0.7228,0.7263,0.7298,0.7333,0.7368,0.7404,0.7439,0.7474,0.7509,0.7544,0.7579,0.7614,0.7649,0.7684,0.7719,0.7754,0.7789,0.7825,0.786,0.7895,0.793,0.7965,0.8,0.8035,0.807,0.8105,0.814,0.8175,0.8211,0.8246,0.8281,0.8316,0.8351,0.8386,0.8421,0.8456,0.8491,0.8526,0.8561,0.8596,0.8632,0.8667,0.8702,0.8737,0.8772,0.8807,0.8842,0.8877,0.8912,0.8947,0.8982,0.9018,0.9053,0.9088,0.9123,0.9158,0.9193,0.9228,0.9263,0.9298,0.9333,0.9368,0.9404,0.9439,0.9474,0.9509,0.9544,0.9579,0.9614,0.9649,0.9684,0.9719,0.9754,0.9789,0.9825,0.986,0.9895,0.993,0.9965,1]

Group313.children.append(OrientationInterpolator337)
#Euler angle triplet values, CHANNELS Zrotation Xrotation Yrotation, with min/max ranges [2.456646,7.178621], [-1.486638,8.788413], [-1.029227,3.571787] degrees
#2.609710 1.766516 -0.656470, 2.591541 1.745618 -0.651706, 2.573301 1.724784 -0.647000, 2.509591 1.753153 -0.731789, 2.509591 1.753153 -0.731789, 2.509591 1.753153 -0.731789, 2.509591 1.753153 -0.731789, 2.456646 1.818346 -0.782432, 2.497362 1.956090 -0.724531, 2.547518 1.985646 -0.655483, 2.638535 1.992728 -0.622024, 2.822679 2.022872 -0.528548, 2.783255 2.154312 -0.378447, 2.827835 2.211573 -0.174673, 2.966454 2.367945 0.011768, 3.061421 2.644875 0.148318, 3.060796 2.831178 0.267117, 3.066253 3.013679 0.411704, 3.159835 3.256714 0.502920, 3.144267 3.317638 0.581686, 3.262764 3.431193 0.575882, 3.389136 3.411379 0.615320, 3.487574 3.329128 0.611571, 3.491598 3.101521 0.568892, 3.541601 2.875596 0.504479, 3.497271 2.524889 0.400633, 3.341896 2.141649 0.298143, 3.375993 1.824663 0.150344, 3.468760 1.655123 0.098415, 3.468958 1.587139 -0.001426, 3.617346 1.641407 -0.070653, 3.721347 1.772506 -0.108926, 3.824912 1.862581 0.006109, 4.032639 1.917917 -0.032100, 3.992694 1.974164 -0.015752, 3.867841 1.964866 0.013598, 3.911627 1.779103 0.000452, 3.702141 1.611857 -0.078364, 3.651941 1.492803 -0.149983, 3.562690 1.208382 -0.187226, 3.394138 1.036159 -0.271922, 3.357769 1.036099 -0.336150, 3.295940 1.015112 -0.349175, 3.449153 0.824696 -0.405887, 3.565457 0.531763 -0.413232, 3.658690 -0.062138 -0.633820, 3.715758 -0.571864 -0.855765, 3.537050 -1.046493 -0.988707, 3.286674 -1.327173 -1.029227, 3.155375 -1.443082 -0.940426, 3.150302 -1.486638 -0.812448, 3.190036 -1.424879 -0.671186, 3.338912 -1.248655 -0.616267, 3.468783 -1.085750 -0.586551, 3.605629 -0.945630 -0.431275, 3.658360 -0.890390 -0.411479, 3.736752 -0.759408 -0.289796, 3.898445 -0.640889 -0.055670, 3.996348 -0.567845 0.057673, 4.015692 -0.565568 0.183632, 4.089818 -0.412534 0.377172, 4.146720 -0.407018 0.336773, 4.198324 -0.323280 0.401580, 4.236970 -0.189247 0.454345, 4.347973 0.076507 0.588716, 4.323826 0.340251 0.733516, 4.292437 0.670870 0.807026, 4.348366 0.913239 0.894975, 4.436174 1.065549 0.928852, 4.440114 1.058259 0.791183, 4.297723 1.028319 0.696289, 4.165938 1.137442 0.656905, 3.966641 1.085614 0.695216, 3.821973 1.149549 0.786012, 3.710192 1.287091 0.912316, 3.758895 1.322547 1.031811, 3.778157 1.439755 1.028016, 3.804880 1.504585 1.007598, 3.772261 1.526406 0.974293, 3.787666 1.518317 0.942191, 3.761770 1.229793 0.920513, 3.607916 1.095199 0.910055, 3.591836 0.965124 0.911397, 3.572788 0.859712 1.002569, 3.543512 0.776950 0.967856, 3.527230 0.766862 0.945530, 3.592711 0.824003 1.042235, 3.606554 0.981228 1.066815, 3.520762 1.112436 1.041098, 3.462283 1.179569 1.072517, 3.498291 1.203131 1.169989, 3.488258 1.176765 1.212472, 3.548696 1.268652 1.174410, 3.653401 1.221396 1.091068, 3.644977 0.987682 0.960030, 3.587633 0.888106 0.918511, 3.502422 0.853340 0.820066, 3.495017 0.824862 0.844745, 3.431740 0.851256 0.741975, 3.304274 0.853369 0.605805, 3.222446 0.986675 0.661551, 3.191320 1.157573 0.700467, 3.194075 1.527976 0.862452, 3.178567 1.947787 1.011074, 3.194157 2.272527 1.143861, 3.067826 2.708904 1.266654, 3.014899 3.034764 1.409054, 2.996991 3.272868 1.494379, 3.020661 3.462350 1.669930, 3.053185 3.744555 1.882853, 3.153502 4.093783 1.918935, 3.157214 4.438551 2.105475, 3.264934 4.713367 2.252724, 3.420915 5.134163 2.346133, 3.546325 5.528796 2.487097, 3.679927 5.731876 2.605094, 3.860155 6.013876 2.737916, 4.136775 6.262952 2.702362, 4.257153 6.128742 2.696179, 4.413658 5.980105 2.667713, 4.498665 5.680610 2.537950, 4.623168 5.323748 2.333003, 4.606783 4.890638 2.187691, 4.532002 4.341436 1.828472, 4.444507 3.650190 1.454080, 4.302584 2.918533 1.123233, 4.202941 2.258538 0.794406, 4.105155 1.829636 0.451094, 3.987128 1.469597 0.317206, 3.845129 1.294009 0.206231, 3.940210 1.071800 0.033911, 4.043222 1.013302 -0.031399, 4.195504 0.894460 0.005893, 4.336459 0.749749 -0.064048, 4.380551 0.767012 -0.111951, 4.476020 0.632756 -0.134787, 4.490328 0.561642 -0.133104, 4.466521 0.515244 -0.144245, 4.527095 0.447300 -0.152167, 4.579456 0.477261 -0.092139, 4.531847 0.600354 -0.054204, 4.605219 0.757764 0.071504, 4.653720 0.991235 0.291282, 4.644312 1.171796 0.403046, 4.692876 1.578039 0.631508, 4.741666 2.256210 0.886786, 4.981188 2.828020 1.136423, 5.307639 3.272872 1.241454, 5.481036 3.821904 1.610268, 5.437832 4.715100 1.989678, 5.322356 5.759709 2.448527, 5.262897 6.956882 2.777122, 5.045299 7.930885 3.116274, 5.007168 8.557764 3.410101, 4.711544 8.788413 3.532429, 4.425086 8.618318 3.533709, 4.157495 8.143188 3.447216, 3.830289 7.465457 3.295743, 3.550007 6.769403 3.173775, 3.292316 6.288131 3.085796, 3.323904 5.881514 2.958260, 3.416953 5.649967 2.753599, 3.718779 5.341076 2.637790, 4.088656 5.006107 2.446630, 4.363964 4.499816 2.253824, 4.461232 3.823933 2.003320, 4.562994 2.954117 1.715938, 4.455107 2.011667 1.355090, 4.348244 1.173957 1.046626, 4.159241 0.416373 0.744220, 3.878191 -0.146459 0.483840, 3.802101 -0.492538 0.335120, 3.681212 -0.702899 0.201115, 3.753507 -0.957291 0.120798, 3.751885 -1.048348 0.052433, 3.838710 -1.075086 -0.023061, 3.941370 -0.913584 0.007368, 4.077155 -0.710841 0.067974, 4.021138 -0.493783 0.113109, 4.192567 -0.090379 0.191119, 4.265887 0.381359 0.199195, 4.396726 0.996866 0.260430, 4.637878 1.569224 0.308649, 4.819003 2.232227 0.240338, 5.083901 2.841405 0.116490, 5.348825 3.389904 0.061128, 5.484107 3.788867 0.078171, 5.671214 4.071801 0.117036, 5.778224 4.302830 0.179695, 5.984050 4.416688 0.206002, 6.164649 4.571058 0.275744, 6.330037 4.630530 0.401026, 6.359154 4.588037 0.465473, 6.399112 4.633233 0.529274, 6.432635 4.745173 0.598181, 6.476054 4.753545 0.771733, 6.575794 4.958569 1.076699, 6.717582 5.236322 1.361264, 6.884017 5.591733 1.493165, 7.019921 5.758934 1.644916, 7.178621 5.659254 1.647058, 7.114531 5.268462 1.486865, 7.033399 4.715368 1.258053, 6.785652 3.886451 0.957835, 6.448216 2.986852 0.587559, 6.095248 2.056996 0.253951, 5.716551 1.136121 -0.059571, 5.303021 0.434514 -0.368557, 5.039319 -0.079251 -0.499075, 4.827057 -0.437709 -0.572066, 4.689123 -0.676466 -0.626956, 4.640162 -0.762470 -0.507007, 4.652785 -0.536442 -0.463485, 4.724301 -0.359404 -0.265021, 4.795363 -0.200408 -0.040887, 4.829113 0.020305 0.089064, 4.727686 0.157978 0.175518, 4.674071 0.223846 0.326485, 4.645977 0.398000 0.437760, 4.615845 0.571808 0.549512, 4.699035 0.641097 0.673296, 4.764174 0.861556 0.903415, 5.006110 1.008186 1.117992, 5.270810 1.184520 1.364237, 5.430277 1.547521 1.645999, 5.655989 1.973009 1.749372, 5.749415 2.323365 1.917190, 5.860627 2.695108 2.011161, 5.802779 2.895799 2.263206, 5.896626 2.884801 2.311376, 5.768037 2.924230 2.327038, 5.622861 2.826566 2.452531, 5.447722 2.591182 2.392977, 5.229531 2.439090 2.391254, 5.089054 2.060736 2.338355, 5.015532 1.766368 2.340999, 4.834675 1.708341 2.346365, 4.901945 1.734669 2.347052, 4.844102 1.936747 2.436603, 4.810528 2.268255 2.534630, 4.860759 2.688789 2.733017, 4.736041 3.166318 2.863721, 4.649082 3.283733 2.877078, 4.645667 3.279725 2.936363, 4.692152 3.098269 2.826031, 4.767061 2.767752 2.709860, 4.918048 2.261921 2.588167, 4.846825 1.842797 2.359103, 4.769948 1.459683 2.109476, 4.684646 1.135207 1.932150, 4.587901 0.793034 1.727886, 4.548129 0.460378 1.542455, 4.592036 0.195497 1.350232, 4.717709 -0.036784 1.160607, 4.805299 -0.493930 0.992772, 4.867844 -0.776893 0.852458, 5.019173 -1.047115 0.689119, 5.088356 -1.235900 0.609737, 5.159803 -1.357874 0.552079, 5.231793 -1.483777 0.565409, 5.267893 -1.408280 0.688241, 5.202056 -1.313708 0.636508, 5.238701 -1.215977 0.647841, 5.264812 -1.149316 0.691081, 5.215518 -1.076591 0.782431, 5.058992 -0.968773 0.861934, 5.050659 -0.933754 0.943135, 5.053639 -0.967311 1.017240, 4.869430 -0.832179 1.186766, 4.826537 -0.658884 1.298053, 4.795041 -0.413694 1.422978, 4.639856 -0.269186 1.521027, 4.628968 0.025500 1.718026, 4.518999 0.448081 1.853044, 4.518989 0.731057 2.077240, 4.426625 1.292210 2.291998, 4.353678 1.767168 2.631521, 4.347259 2.377491 2.846277, 4.288334 3.032555 3.086150, 4.319291 3.552707 3.180204, 4.387262 3.814030 3.399403, 4.399560 4.001153 3.560441, 4.305292 3.842644 3.571787, 4.163692 3.448258 3.469280, 3.931834 2.950572 3.194955, 3.692430 2.274818 2.937333
#Interpolator20_Neck channels [60..62] sends animation values to BVH JOINT Neck, DEF BvhConversion1_Neck, <HAnimJoint name=Neck/>
OrientationInterpolator338 = x3d.OrientationInterpolator()
OrientationInterpolator338.DEF = "Interpolator20_Neck"
OrientationInterpolator338.key = [0,0.0035,0.007,0.0105,0.014,0.0175,0.0211,0.0246,0.0281,0.0316,0.0351,0.0386,0.0421,0.0456,0.0491,0.0526,0.0561,0.0596,0.0632,0.0667,0.0702,0.0737,0.0772,0.0807,0.0842,0.0877,0.0912,0.0947,0.0982,0.1018,0.1053,0.1088,0.1123,0.1158,0.1193,0.1228,0.1263,0.1298,0.1333,0.1368,0.1404,0.1439,0.1474,0.1509,0.1544,0.1579,0.1614,0.1649,0.1684,0.1719,0.1754,0.1789,0.1825,0.186,0.1895,0.193,0.1965,0.2,0.2035,0.207,0.2105,0.214,0.2175,0.2211,0.2246,0.2281,0.2316,0.2351,0.2386,0.2421,0.2456,0.2491,0.2526,0.2561,0.2596,0.2632,0.2667,0.2702,0.2737,0.2772,0.2807,0.2842,0.2877,0.2912,0.2947,0.2982,0.3018,0.3053,0.3088,0.3123,0.3158,0.3193,0.3228,0.3263,0.3298,0.3333,0.3368,0.3404,0.3439,0.3474,0.3509,0.3544,0.3579,0.3614,0.3649,0.3684,0.3719,0.3754,0.3789,0.3825,0.386,0.3895,0.393,0.3965,0.4,0.4035,0.407,0.4105,0.414,0.4175,0.4211,0.4246,0.4281,0.4316,0.4351,0.4386,0.4421,0.4456,0.4491,0.4526,0.4561,0.4596,0.4632,0.4667,0.4702,0.4737,0.4772,0.4807,0.4842,0.4877,0.4912,0.4947,0.4982,0.5018,0.5053,0.5088,0.5123,0.5158,0.5193,0.5228,0.5263,0.5298,0.5333,0.5368,0.5404,0.5439,0.5474,0.5509,0.5544,0.5579,0.5614,0.5649,0.5684,0.5719,0.5754,0.5789,0.5825,0.586,0.5895,0.593,0.5965,0.6,0.6035,0.607,0.6105,0.614,0.6175,0.6211,0.6246,0.6281,0.6316,0.6351,0.6386,0.6421,0.6456,0.6491,0.6526,0.6561,0.6596,0.6632,0.6667,0.6702,0.6737,0.6772,0.6807,0.6842,0.6877,0.6912,0.6947,0.6982,0.7018,0.7053,0.7088,0.7123,0.7158,0.7193,0.7228,0.7263,0.7298,0.7333,0.7368,0.7404,0.7439,0.7474,0.7509,0.7544,0.7579,0.7614,0.7649,0.7684,0.7719,0.7754,0.7789,0.7825,0.786,0.7895,0.793,0.7965,0.8,0.8035,0.807,0.8105,0.814,0.8175,0.8211,0.8246,0.8281,0.8316,0.8351,0.8386,0.8421,0.8456,0.8491,0.8526,0.8561,0.8596,0.8632,0.8667,0.8702,0.8737,0.8772,0.8807,0.8842,0.8877,0.8912,0.8947,0.8982,0.9018,0.9053,0.9088,0.9123,0.9158,0.9193,0.9228,0.9263,0.9298,0.9333,0.9368,0.9404,0.9439,0.9474,0.9509,0.9544,0.9579,0.9614,0.9649,0.9684,0.9719,0.9754,0.9789,0.9825,0.986,0.9895,0.993,0.9965,1]

Group313.children.append(OrientationInterpolator338)
#Euler angle triplet values, CHANNELS Zrotation Xrotation Yrotation, with min/max ranges [0.525157,6.785662], [2.15166,7.200243], [-7.137212,0.208419] degrees
#1.121967 2.219361 -1.735443, 0.994213 2.177388 -1.744496, 0.805579 2.151660 -1.742254, 0.679111 2.172901 -1.728260, 0.624755 2.231911 -1.723264, 0.570379 2.290937 -1.718213, 0.542117 2.381536 -1.738034, 0.531580 2.517337 -1.823594, 0.549149 2.713147 -1.843520, 0.563941 2.917109 -1.870919, 0.525157 2.987144 -1.912269, 0.574892 3.124177 -1.928076, 0.604275 3.245084 -2.011184, 0.637937 3.354579 -2.084006, 0.650356 3.431784 -2.207296, 0.678749 3.519181 -2.378441, 0.764590 3.580735 -2.573580, 0.820652 3.735475 -2.819216, 0.885168 3.743572 -3.067144, 1.020983 3.839287 -3.309463, 1.110384 3.935837 -3.553521, 1.222308 4.063597 -3.748524, 1.439352 4.196218 -3.880000, 1.669704 4.302683 -4.038571, 1.922543 4.450010 -4.134351, 2.225290 4.554186 -4.179887, 2.604203 4.599705 -4.218820, 3.021413 4.583255 -4.230084, 3.363619 4.558637 -4.236283, 3.669826 4.527610 -4.161393, 3.907995 4.451849 -4.014188, 4.070285 4.363519 -3.887729, 4.232954 4.188039 -3.751403, 4.368740 3.984702 -3.620764, 4.460617 3.835886 -3.528611, 4.516739 3.664460 -3.496188, 4.630396 3.519294 -3.423211, 4.801372 3.374806 -3.438747, 5.005436 3.219751 -3.488132, 5.166541 3.105643 -3.565322, 5.225718 3.067404 -3.685314, 5.258659 2.999334 -3.780756, 5.161829 2.890709 -3.884197, 4.988655 2.753767 -3.984895, 4.815460 2.629791 -4.001894, 4.596022 2.512689 -3.997213, 4.382665 2.382444 -3.950492, 4.189481 2.296196 -3.970605, 4.044883 2.255866 -3.951368, 3.922498 2.209013 -3.906116, 3.697614 2.204157 -3.855239, 3.561283 2.261600 -3.777339, 3.395647 2.309676 -3.752599, 3.206938 2.428936 -3.772364, 3.095091 2.557358 -3.795466, 2.959238 2.634999 -3.762555, 2.875158 2.726652 -3.827821, 2.782374 2.862325 -3.867569, 2.702516 3.153645 -3.958011, 2.679650 3.432902 -3.959859, 2.691986 3.689050 -3.985434, 2.668870 3.861099 -4.064580, 2.633969 4.007509 -4.078988, 2.583006 4.037689 -4.118862, 2.460515 4.086601 -4.086070, 2.451801 4.164371 -3.999287, 2.459995 4.145962 -3.934731, 2.515107 4.171011 -3.818515, 2.565297 4.202494 -3.627770, 2.604961 4.250229 -3.392543, 2.716678 4.283073 -3.132860, 2.822358 4.290907 -2.857396, 3.050277 4.248170 -2.717778, 3.350400 4.151248 -2.602729, 3.554236 4.076006 -2.540025, 3.771785 4.009378 -2.520070, 3.947884 3.951471 -2.490594, 4.072014 3.912941 -2.514076, 4.088645 3.879888 -2.502822, 4.065389 3.823904 -2.550086, 4.008912 3.798303 -2.565249, 3.967706 3.766166 -2.494790, 3.913248 3.789639 -2.443016, 3.831576 3.775483 -2.373734, 3.774690 3.703874 -2.320594, 3.682917 3.611171 -2.197264, 3.669453 3.497859 -2.114641, 3.650600 3.391930 -1.957353, 3.672305 3.296346 -1.839647, 3.619061 3.165519 -1.711801, 3.549732 3.072154 -1.602406, 3.468586 3.015953 -1.480698, 3.347339 2.948084 -1.319930, 3.248112 2.887884 -1.178212, 3.121271 2.778113 -1.010004, 2.995025 2.667553 -0.841937, 2.930910 2.630493 -0.671421, 2.910887 2.660889 -0.477876, 2.878702 2.622730 -0.270328, 2.874407 2.633903 -0.089965, 2.895421 2.622609 0.003438, 2.864997 2.622983 0.163912, 2.870944 2.710242 0.187032, 2.831824 2.795150 0.208419, 2.801772 2.864128 0.195168, 2.823434 2.886235 0.136674, 2.842561 2.962234 0.138566, 2.893312 3.072339 0.050230, 2.945305 3.169060 -0.023143, 3.005831 3.273773 -0.057508, 3.162764 3.448209 -0.129872, 3.265800 3.580472 -0.201568, 3.336217 3.800370 -0.296559, 3.394892 4.075130 -0.411788, 3.566574 4.326088 -0.638243, 3.773851 4.594940 -0.830563, 3.986839 4.861224 -0.996433, 4.196639 5.127308 -1.192622, 4.335627 5.354418 -1.348316, 4.461762 5.569838 -1.453400, 4.484824 5.767971 -1.587985, 4.627941 5.944586 -1.677220, 4.734748 6.008432 -1.811444, 4.828501 5.997575 -1.938207, 5.000063 5.927755 -2.059490, 5.110590 5.765995 -2.127880, 5.214641 5.620038 -2.129691, 5.263880 5.417058 -2.100317, 5.278436 5.336792 -2.058230, 5.205811 5.248875 -2.095545, 5.074884 5.143584 -2.039731, 5.020385 5.041563 -2.063550, 4.958733 4.964071 -2.061371, 4.886445 4.946845 -2.053667, 4.941013 4.864229 -2.140177, 4.982014 4.800811 -2.329307, 5.006756 4.776033 -2.537315, 5.055949 4.781100 -2.772777, 5.054300 4.847237 -3.002801, 5.063600 4.944117 -3.340253, 4.947315 5.075078 -3.666343, 4.926049 5.243894 -4.050424, 4.924683 5.382538 -4.406769, 4.858048 5.568107 -4.803947, 4.891586 5.677371 -5.193464, 4.913520 5.823771 -5.569452, 4.909664 5.931338 -5.912029, 4.939444 6.004642 -6.254594, 4.947734 5.976500 -6.536708, 5.009287 5.936408 -6.765096, 5.009553 5.835185 -6.959681, 5.069421 5.809821 -7.080280, 5.092628 5.831748 -7.137212, 5.076943 5.842960 -7.119306, 5.103021 5.872524 -7.040459, 5.139680 5.954930 -6.879501, 5.099820 6.038476 -6.601801, 5.094427 6.205256 -6.294451, 5.066425 6.255492 -6.031429, 5.067838 6.387685 -5.730882, 5.050860 6.481575 -5.475390, 5.121757 6.567684 -5.240494, 5.195881 6.631392 -5.077236, 5.285515 6.656700 -4.892548, 5.402668 6.687206 -4.676085, 5.560857 6.717559 -4.505943, 5.712650 6.692956 -4.393644, 5.826403 6.645817 -4.305961, 5.899515 6.602479 -4.216831, 5.997004 6.535294 -4.172551, 6.070932 6.477442 -4.181934, 6.153448 6.401458 -4.224249, 6.190146 6.320432 -4.258923, 6.255227 6.193134 -4.307052, 6.292486 6.112446 -4.342071, 6.350712 5.999720 -4.316694, 6.365455 5.913200 -4.218665, 6.404545 5.854970 -4.148852, 6.436221 5.730218 -4.030023, 6.401908 5.696128 -3.885944, 6.388363 5.666929 -3.764602, 6.342019 5.668909 -3.609772, 6.305824 5.610315 -3.460790, 6.259981 5.611590 -3.306132, 6.138210 5.672222 -3.158503, 6.034617 5.702318 -2.982360, 5.939776 5.753873 -2.932646, 5.859556 5.777474 -2.884587, 5.825406 5.891505 -2.828929, 5.788124 5.926635 -2.830882, 5.773235 5.991357 -2.860719, 5.781990 6.116875 -2.856061, 5.803662 6.259250 -2.793832, 5.817612 6.513426 -2.811190, 5.842685 6.699522 -2.793706, 5.884733 6.847353 -2.757272, 5.926550 6.995278 -2.721423, 6.000015 7.078974 -2.667575, 6.041647 7.139030 -2.518409, 6.123828 7.200243 -2.369924, 6.236646 7.164196 -2.208372, 6.330174 7.089306 -2.053289, 6.338223 6.863811 -1.844780, 6.368562 6.668103 -1.664789, 6.445898 6.508529 -1.543903, 6.435922 6.337021 -1.500197, 6.371397 6.223042 -1.450800, 6.266108 6.100069 -1.359976, 6.150122 6.000335 -1.364588, 5.963686 5.903139 -1.359952, 5.792620 5.860641 -1.359650, 5.641956 5.789619 -1.331859, 5.512465 5.705617 -1.443485, 5.425068 5.679785 -1.495452, 5.334359 5.692273 -1.628024, 5.305103 5.686473 -1.774199, 5.298005 5.711830 -1.947498, 5.249020 5.736053 -2.121912, 5.254843 5.702528 -2.302683, 5.235199 5.764686 -2.465753, 5.116291 5.858353 -2.616261, 4.964920 5.936147 -2.781522, 4.877709 6.039678 -3.001555, 4.726244 6.103532 -3.152932, 4.618213 6.233101 -3.285571, 4.473096 6.303749 -3.396552, 4.339934 6.433206 -3.539791, 4.254469 6.558940 -3.652740, 4.251443 6.643472 -3.788367, 4.265951 6.688307 -3.906008, 4.316734 6.727159 -4.063531, 4.478499 6.767388 -4.274158, 4.640405 6.805776 -4.485302, 4.770236 6.874077 -4.661956, 4.955268 6.925325 -4.796188, 5.084912 6.971805 -4.940805, 5.275376 6.998700 -5.012406, 5.358766 7.022005 -4.999310, 5.509097 6.994455 -4.953899, 5.660580 6.862809 -4.860301, 5.853637 6.738662 -4.807108, 6.011951 6.592316 -4.785834, 6.220697 6.429327 -4.709391, 6.386676 6.244808 -4.687921, 6.556545 6.058082 -4.633515, 6.702460 5.843174 -4.550026, 6.784825 5.703144 -4.507080, 6.785296 5.557930 -4.423665, 6.785662 5.412468 -4.340472, 6.703413 5.312208 -4.239413, 6.616308 5.204996 -4.178151, 6.566818 5.072318 -4.111481, 6.482061 5.005240 -4.087447, 6.430917 4.869764 -4.014484, 6.400962 4.795224 -3.936776, 6.425333 4.739654 -3.855288, 6.373913 4.659579 -3.752172, 6.359676 4.602726 -3.622799, 6.308774 4.505087 -3.486145, 6.340040 4.391499 -3.295312, 6.326101 4.314097 -3.125158, 6.327478 4.266879 -2.952693, 6.350692 4.213058 -2.756204, 6.325289 4.263146 -2.597311, 6.278732 4.274085 -2.369063, 6.182423 4.388198 -2.177923, 5.961627 4.530185 -2.075093, 5.679456 4.741871 -1.980013, 5.405350 4.947844 -1.858092, 5.190454 5.152098 -1.766727, 5.100632 5.317797 -1.691794, 5.079194 5.480155 -1.625165, 5.151311 5.610374 -1.619597, 5.292251 5.738371 -1.623514, 5.398982 5.754697 -1.669949, 5.598575 5.805493 -1.768344, 5.779796 5.854524 -1.821636, 5.884558 5.879720 -1.911338, 5.988735 5.923640 -1.887455, 6.037120 5.970644 -1.916898, 6.138525 5.915803 -1.909365, 6.219069 5.944880 -1.870393, 6.320747 5.890897 -1.862698, 6.454471 5.854898 -1.841251, 6.574531 5.764344 -1.815874, 6.738384 5.595616 -1.745892
#Interpolator21_skullbase channels [63..65] sends animation values to BVH JOINT Head, DEF BvhConversion1_skullbase, <HAnimJoint name=skullbase/>
OrientationInterpolator339 = x3d.OrientationInterpolator()
OrientationInterpolator339.DEF = "Interpolator21_skullbase"
OrientationInterpolator339.key = [0,0.0035,0.007,0.0105,0.014,0.0175,0.0211,0.0246,0.0281,0.0316,0.0351,0.0386,0.0421,0.0456,0.0491,0.0526,0.0561,0.0596,0.0632,0.0667,0.0702,0.0737,0.0772,0.0807,0.0842,0.0877,0.0912,0.0947,0.0982,0.1018,0.1053,0.1088,0.1123,0.1158,0.1193,0.1228,0.1263,0.1298,0.1333,0.1368,0.1404,0.1439,0.1474,0.1509,0.1544,0.1579,0.1614,0.1649,0.1684,0.1719,0.1754,0.1789,0.1825,0.186,0.1895,0.193,0.1965,0.2,0.2035,0.207,0.2105,0.214,0.2175,0.2211,0.2246,0.2281,0.2316,0.2351,0.2386,0.2421,0.2456,0.2491,0.2526,0.2561,0.2596,0.2632,0.2667,0.2702,0.2737,0.2772,0.2807,0.2842,0.2877,0.2912,0.2947,0.2982,0.3018,0.3053,0.3088,0.3123,0.3158,0.3193,0.3228,0.3263,0.3298,0.3333,0.3368,0.3404,0.3439,0.3474,0.3509,0.3544,0.3579,0.3614,0.3649,0.3684,0.3719,0.3754,0.3789,0.3825,0.386,0.3895,0.393,0.3965,0.4,0.4035,0.407,0.4105,0.414,0.4175,0.4211,0.4246,0.4281,0.4316,0.4351,0.4386,0.4421,0.4456,0.4491,0.4526,0.4561,0.4596,0.4632,0.4667,0.4702,0.4737,0.4772,0.4807,0.4842,0.4877,0.4912,0.4947,0.4982,0.5018,0.5053,0.5088,0.5123,0.5158,0.5193,0.5228,0.5263,0.5298,0.5333,0.5368,0.5404,0.5439,0.5474,0.5509,0.5544,0.5579,0.5614,0.5649,0.5684,0.5719,0.5754,0.5789,0.5825,0.586,0.5895,0.593,0.5965,0.6,0.6035,0.607,0.6105,0.614,0.6175,0.6211,0.6246,0.6281,0.6316,0.6351,0.6386,0.6421,0.6456,0.6491,0.6526,0.6561,0.6596,0.6632,0.6667,0.6702,0.6737,0.6772,0.6807,0.6842,0.6877,0.6912,0.6947,0.6982,0.7018,0.7053,0.7088,0.7123,0.7158,0.7193,0.7228,0.7263,0.7298,0.7333,0.7368,0.7404,0.7439,0.7474,0.7509,0.7544,0.7579,0.7614,0.7649,0.7684,0.7719,0.7754,0.7789,0.7825,0.786,0.7895,0.793,0.7965,0.8,0.8035,0.807,0.8105,0.814,0.8175,0.8211,0.8246,0.8281,0.8316,0.8351,0.8386,0.8421,0.8456,0.8491,0.8526,0.8561,0.8596,0.8632,0.8667,0.8702,0.8737,0.8772,0.8807,0.8842,0.8877,0.8912,0.8947,0.8982,0.9018,0.9053,0.9088,0.9123,0.9158,0.9193,0.9228,0.9263,0.9298,0.9333,0.9368,0.9404,0.9439,0.9474,0.9509,0.9544,0.9579,0.9614,0.9649,0.9684,0.9719,0.9754,0.9789,0.9825,0.986,0.9895,0.993,0.9965,1]

Group313.children.append(OrientationInterpolator339)
#Euler angle triplet values, CHANNELS Zrotation Xrotation Yrotation, with min/max ranges [0.525157,6.785663], [2.151661,7.200242], [-7.137212,0.208419] degrees
#1.121968 2.219362 -1.735443, 0.994214 2.177389 -1.744499, 0.805580 2.151661 -1.742253, 0.679112 2.172901 -1.728257, 0.624756 2.231911 -1.723261, 0.570379 2.290936 -1.718210, 0.542118 2.381536 -1.738031, 0.531580 2.517336 -1.823592, 0.549150 2.713146 -1.843520, 0.563942 2.917109 -1.870919, 0.525157 2.987144 -1.912271, 0.574892 3.124176 -1.928075, 0.604276 3.245085 -2.011183, 0.637938 3.354579 -2.084004, 0.650357 3.431783 -2.207294, 0.678750 3.519181 -2.378441, 0.764591 3.580734 -2.573579, 0.820653 3.735476 -2.819217, 0.885170 3.743571 -3.067142, 1.020983 3.839285 -3.309462, 1.110384 3.935837 -3.553522, 1.222309 4.063596 -3.748522, 1.439353 4.196218 -3.880000, 1.669705 4.302684 -4.038571, 1.922543 4.450009 -4.134351, 2.225290 4.554185 -4.179886, 2.604204 4.599705 -4.218818, 3.021413 4.583254 -4.230084, 3.363620 4.558637 -4.236286, 3.669827 4.527610 -4.161391, 3.907995 4.451848 -4.014190, 4.070286 4.363518 -3.887728, 4.232955 4.188039 -3.751404, 4.368741 3.984702 -3.620764, 4.460616 3.835885 -3.528610, 4.516741 3.664461 -3.496190, 4.630397 3.519294 -3.423210, 4.801373 3.374806 -3.438746, 5.005439 3.219753 -3.488131, 5.166542 3.105644 -3.565322, 5.225718 3.067405 -3.685316, 5.258657 2.999334 -3.780757, 5.161830 2.890710 -3.884197, 4.988657 2.753769 -3.984893, 4.815463 2.629792 -4.001895, 4.596023 2.512689 -3.997211, 4.382665 2.382445 -3.950494, 4.189481 2.296196 -3.970606, 4.044885 2.255867 -3.951368, 3.922498 2.209013 -3.906116, 3.697616 2.204158 -3.855241, 3.561284 2.261600 -3.777339, 3.395648 2.309676 -3.752601, 3.206939 2.428936 -3.772364, 3.095092 2.557358 -3.795466, 2.959238 2.634998 -3.762554, 2.875159 2.726652 -3.827822, 2.782374 2.862324 -3.867569, 2.702517 3.153645 -3.958009, 2.679651 3.432902 -3.959859, 2.691988 3.689050 -3.985434, 2.668869 3.861097 -4.064579, 2.633970 4.007509 -4.078988, 2.583007 4.037688 -4.118861, 2.460516 4.086602 -4.086070, 2.451802 4.164371 -3.999286, 2.459996 4.145961 -3.934731, 2.515108 4.171012 -3.818516, 2.565297 4.202493 -3.627770, 2.604960 4.250229 -3.392541, 2.716679 4.283072 -3.132860, 2.822358 4.290907 -2.857396, 3.050278 4.248169 -2.717778, 3.350401 4.151247 -2.602727, 3.554237 4.076007 -2.540025, 3.771786 4.009379 -2.520070, 3.947884 3.951470 -2.490595, 4.072014 3.912941 -2.514077, 4.088646 3.879889 -2.502821, 4.065391 3.823903 -2.550084, 4.008910 3.798303 -2.565250, 3.967707 3.766166 -2.494788, 3.913249 3.789639 -2.443015, 3.831576 3.775483 -2.373732, 3.774691 3.703875 -2.320593, 3.682918 3.611171 -2.197264, 3.669453 3.497859 -2.114639, 3.650602 3.391930 -1.957353, 3.672305 3.296346 -1.839647, 3.619062 3.165519 -1.711801, 3.549731 3.072154 -1.602406, 3.468588 3.015954 -1.480696, 3.347338 2.948084 -1.319927, 3.248112 2.887884 -1.178211, 3.121273 2.778113 -1.010003, 2.995027 2.667554 -0.841936, 2.930909 2.630492 -0.671422, 2.910887 2.660887 -0.477875, 2.878703 2.622730 -0.270327, 2.874408 2.633903 -0.089965, 2.895421 2.622608 0.003438, 2.864998 2.622983 0.163912, 2.870945 2.710242 0.187034, 2.831825 2.795151 0.208419, 2.801772 2.864126 0.195169, 2.823434 2.886234 0.136675, 2.842562 2.962234 0.138565, 2.893312 3.072339 0.050229, 2.945305 3.169060 -0.023144, 3.005832 3.273774 -0.057507, 3.162763 3.448209 -0.129871, 3.265799 3.580472 -0.201566, 3.336219 3.800371 -0.296558, 3.394891 4.075129 -0.411786, 3.566575 4.326088 -0.638240, 3.773850 4.594939 -0.830561, 3.986840 4.861226 -0.996433, 4.196641 5.127310 -1.192622, 4.335626 5.354416 -1.348315, 4.461763 5.569838 -1.453398, 4.484824 5.767971 -1.587985, 4.627942 5.944585 -1.677220, 4.734749 6.008432 -1.811443, 4.828503 5.997575 -1.938208, 5.000065 5.927756 -2.059492, 5.110590 5.765995 -2.127881, 5.214641 5.620038 -2.129689, 5.263881 5.417058 -2.100316, 5.278437 5.336792 -2.058229, 5.205814 5.248875 -2.095544, 5.074886 5.143584 -2.039730, 5.020388 5.041564 -2.063550, 4.958734 4.964072 -2.061371, 4.886446 4.946846 -2.053668, 4.941012 4.864229 -2.140177, 4.982015 4.800812 -2.329305, 5.006757 4.776033 -2.537314, 5.055951 4.781098 -2.772775, 5.054302 4.847236 -3.002798, 5.063601 4.944117 -3.340254, 4.947315 5.075077 -3.666342, 4.926049 5.243895 -4.050423, 4.924682 5.382537 -4.406768, 4.858049 5.568107 -4.803946, 4.891587 5.677370 -5.193464, 4.913520 5.823771 -5.569451, 4.909666 5.931338 -5.912027, 4.939443 6.004642 -6.254594, 4.947735 5.976501 -6.536708, 5.009288 5.936407 -6.765095, 5.009553 5.835184 -6.959678, 5.069421 5.809823 -7.080284, 5.092631 5.831747 -7.137212, 5.076942 5.842959 -7.119304, 5.103021 5.872524 -7.040458, 5.139678 5.954929 -6.879497, 5.099822 6.038477 -6.601801, 5.094428 6.205256 -6.294448, 5.066426 6.255492 -6.031428, 5.067841 6.387686 -5.730884, 5.050860 6.481573 -5.475389, 5.121757 6.567682 -5.240493, 5.195880 6.631391 -5.077233, 5.285515 6.656700 -4.892548, 5.402668 6.687203 -4.676083, 5.560857 6.717558 -4.505942, 5.712650 6.692956 -4.393645, 5.826404 6.645818 -4.305959, 5.899516 6.602478 -4.216830, 5.997005 6.535293 -4.172551, 6.070933 6.477443 -4.181935, 6.153450 6.401459 -4.224248, 6.190148 6.320433 -4.258923, 6.255226 6.193135 -4.307050, 6.292487 6.112446 -4.342071, 6.350713 5.999720 -4.316694, 6.365457 5.913199 -4.218667, 6.404547 5.854970 -4.148851, 6.436219 5.730216 -4.030024, 6.401911 5.696128 -3.885943, 6.388365 5.666929 -3.764600, 6.342019 5.668908 -3.609772, 6.305825 5.610314 -3.460789, 6.259981 5.611588 -3.306130, 6.138212 5.672223 -3.158502, 6.034620 5.702318 -2.982359, 5.939776 5.753873 -2.932644, 5.859556 5.777474 -2.884586, 5.825408 5.891508 -2.828928, 5.788125 5.926635 -2.830881, 5.773238 5.991358 -2.860720, 5.781990 6.116874 -2.856060, 5.803664 6.259252 -2.793831, 5.817613 6.513426 -2.811190, 5.842687 6.699522 -2.793705, 5.884734 6.847353 -2.757274, 5.926556 6.995281 -2.721422, 6.000017 7.078972 -2.667575, 6.041648 7.139030 -2.518409, 6.123828 7.200242 -2.369922, 6.236650 7.164197 -2.208372, 6.330173 7.089305 -2.053290, 6.338224 6.863811 -1.844779, 6.368562 6.668104 -1.664789, 6.445900 6.508528 -1.543901, 6.435922 6.337022 -1.500195, 6.371398 6.223038 -1.450798, 6.266109 6.100068 -1.359977, 6.150121 6.000334 -1.364586, 5.963688 5.903139 -1.359951, 5.792621 5.860641 -1.359651, 5.641957 5.789619 -1.331858, 5.512467 5.705617 -1.443485, 5.425067 5.679782 -1.495453, 5.334360 5.692272 -1.628023, 5.305102 5.686472 -1.774199, 5.298004 5.711830 -1.947496, 5.249021 5.736053 -2.121910, 5.254845 5.702529 -2.302684, 5.235200 5.764687 -2.465754, 5.116293 5.858355 -2.616260, 4.964920 5.936147 -2.781520, 4.877709 6.039677 -3.001555, 4.726248 6.103535 -3.152933, 4.618215 6.233102 -3.285571, 4.473095 6.303747 -3.396551, 4.339934 6.433202 -3.539787, 4.254471 6.558941 -3.652739, 4.251446 6.643472 -3.788364, 4.265953 6.688306 -3.906005, 4.316737 6.727159 -4.063532, 4.478499 6.767388 -4.274158, 4.640405 6.805777 -4.485301, 4.770237 6.874076 -4.661955, 4.955266 6.925325 -4.796187, 5.084915 6.971806 -4.940806, 5.275376 6.998701 -5.012405, 5.358768 7.022003 -4.999309, 5.509097 6.994456 -4.953900, 5.660579 6.862808 -4.860299, 5.853638 6.738661 -4.807111, 6.011951 6.592316 -4.785834, 6.220698 6.429327 -4.709389, 6.386676 6.244809 -4.687921, 6.556547 6.058082 -4.633515, 6.702461 5.843174 -4.550026, 6.784828 5.703144 -4.507082, 6.785297 5.557929 -4.423664, 6.785663 5.412467 -4.340471, 6.703413 5.312209 -4.239413, 6.616308 5.204994 -4.178151, 6.566821 5.072319 -4.111482, 6.482061 5.005239 -4.087448, 6.430918 4.869767 -4.014484, 6.400961 4.795223 -3.936775, 6.425335 4.739654 -3.855289, 6.373913 4.659577 -3.752170, 6.359679 4.602726 -3.622799, 6.308773 4.505087 -3.486145, 6.340040 4.391499 -3.295312, 6.326103 4.314099 -3.125156, 6.327482 4.266880 -2.952694, 6.350694 4.213058 -2.756203, 6.325289 4.263146 -2.597310, 6.278733 4.274085 -2.369062, 6.182424 4.388197 -2.177922, 5.961628 4.530185 -2.075092, 5.679456 4.741871 -1.980013, 5.405353 4.947844 -1.858091, 5.190453 5.152099 -1.766727, 5.100633 5.317797 -1.691793, 5.079195 5.480154 -1.625164, 5.151312 5.610374 -1.619598, 5.292252 5.738370 -1.623514, 5.398982 5.754696 -1.669947, 5.598574 5.805494 -1.768346, 5.779798 5.854526 -1.821636, 5.884559 5.879719 -1.911337, 5.988737 5.923642 -1.887455, 6.037117 5.970643 -1.916897, 6.138524 5.915802 -1.909366, 6.219070 5.944880 -1.870393, 6.320748 5.890896 -1.862695, 6.454473 5.854898 -1.841251, 6.574532 5.764346 -1.815873, 6.738384 5.595615 -1.745891
#Overall angle min/max range [-46.181885,57.245258] degrees
#Corresponding ROUTE statements to send animation values
ROUTE340 = x3d.ROUTE()
ROUTE340.fromField = "fraction_changed"
ROUTE340.fromNode = "RealTimer"
ROUTE340.toField = "set_fraction"
ROUTE340.toNode = "Interpolator0_humanoid_root"

Group313.children.append(ROUTE340)
ROUTE341 = x3d.ROUTE()
ROUTE341.fromField = "value_changed"
ROUTE341.fromNode = "FrameStepper"
ROUTE341.toField = "set_fraction"
ROUTE341.toNode = "Interpolator0_humanoid_root"

Group313.children.append(ROUTE341)
ROUTE342 = x3d.ROUTE()
ROUTE342.fromField = "value_changed"
ROUTE342.fromNode = "Interpolator0_humanoid_root"
ROUTE342.toField = "set_translation"
ROUTE342.toNode = "BvhConversion1_humanoid_root"

Group313.children.append(ROUTE342)
ROUTE343 = x3d.ROUTE()
ROUTE343.fromField = "fraction_changed"
ROUTE343.fromNode = "RealTimer"
ROUTE343.toField = "set_fraction"
ROUTE343.toNode = "Interpolator1_humanoid_root"

Group313.children.append(ROUTE343)
ROUTE344 = x3d.ROUTE()
ROUTE344.fromField = "value_changed"
ROUTE344.fromNode = "FrameStepper"
ROUTE344.toField = "set_fraction"
ROUTE344.toNode = "Interpolator1_humanoid_root"

Group313.children.append(ROUTE344)
ROUTE345 = x3d.ROUTE()
ROUTE345.fromField = "value_changed"
ROUTE345.fromNode = "Interpolator1_humanoid_root"
ROUTE345.toField = "set_rotation"
ROUTE345.toNode = "BvhConversion1_humanoid_root"

Group313.children.append(ROUTE345)
ROUTE346 = x3d.ROUTE()
ROUTE346.fromField = "fraction_changed"
ROUTE346.fromNode = "RealTimer"
ROUTE346.toField = "set_fraction"
ROUTE346.toNode = "Interpolator2_l_hip"

Group313.children.append(ROUTE346)
ROUTE347 = x3d.ROUTE()
ROUTE347.fromField = "value_changed"
ROUTE347.fromNode = "FrameStepper"
ROUTE347.toField = "set_fraction"
ROUTE347.toNode = "Interpolator2_l_hip"

Group313.children.append(ROUTE347)
ROUTE348 = x3d.ROUTE()
ROUTE348.fromField = "value_changed"
ROUTE348.fromNode = "Interpolator2_l_hip"
ROUTE348.toField = "set_rotation"
ROUTE348.toNode = "BvhConversion1_l_hip"

Group313.children.append(ROUTE348)
ROUTE349 = x3d.ROUTE()
ROUTE349.fromField = "fraction_changed"
ROUTE349.fromNode = "RealTimer"
ROUTE349.toField = "set_fraction"
ROUTE349.toNode = "Interpolator3_l_knee"

Group313.children.append(ROUTE349)
ROUTE350 = x3d.ROUTE()
ROUTE350.fromField = "value_changed"
ROUTE350.fromNode = "FrameStepper"
ROUTE350.toField = "set_fraction"
ROUTE350.toNode = "Interpolator3_l_knee"

Group313.children.append(ROUTE350)
ROUTE351 = x3d.ROUTE()
ROUTE351.fromField = "value_changed"
ROUTE351.fromNode = "Interpolator3_l_knee"
ROUTE351.toField = "set_rotation"
ROUTE351.toNode = "BvhConversion1_l_knee"

Group313.children.append(ROUTE351)
ROUTE352 = x3d.ROUTE()
ROUTE352.fromField = "fraction_changed"
ROUTE352.fromNode = "RealTimer"
ROUTE352.toField = "set_fraction"
ROUTE352.toNode = "Interpolator4_l_ankle"

Group313.children.append(ROUTE352)
ROUTE353 = x3d.ROUTE()
ROUTE353.fromField = "value_changed"
ROUTE353.fromNode = "FrameStepper"
ROUTE353.toField = "set_fraction"
ROUTE353.toNode = "Interpolator4_l_ankle"

Group313.children.append(ROUTE353)
ROUTE354 = x3d.ROUTE()
ROUTE354.fromField = "value_changed"
ROUTE354.fromNode = "Interpolator4_l_ankle"
ROUTE354.toField = "set_rotation"
ROUTE354.toNode = "BvhConversion1_l_ankle"

Group313.children.append(ROUTE354)
ROUTE355 = x3d.ROUTE()
ROUTE355.fromField = "fraction_changed"
ROUTE355.fromNode = "RealTimer"
ROUTE355.toField = "set_fraction"
ROUTE355.toNode = "Interpolator5_l_midtarsal"

Group313.children.append(ROUTE355)
ROUTE356 = x3d.ROUTE()
ROUTE356.fromField = "value_changed"
ROUTE356.fromNode = "FrameStepper"
ROUTE356.toField = "set_fraction"
ROUTE356.toNode = "Interpolator5_l_midtarsal"

Group313.children.append(ROUTE356)
ROUTE357 = x3d.ROUTE()
ROUTE357.fromField = "value_changed"
ROUTE357.fromNode = "Interpolator5_l_midtarsal"
ROUTE357.toField = "set_rotation"
ROUTE357.toNode = "BvhConversion1_l_midtarsal"

Group313.children.append(ROUTE357)
ROUTE358 = x3d.ROUTE()
ROUTE358.fromField = "fraction_changed"
ROUTE358.fromNode = "RealTimer"
ROUTE358.toField = "set_fraction"
ROUTE358.toNode = "Interpolator6_r_hip"

Group313.children.append(ROUTE358)
ROUTE359 = x3d.ROUTE()
ROUTE359.fromField = "value_changed"
ROUTE359.fromNode = "FrameStepper"
ROUTE359.toField = "set_fraction"
ROUTE359.toNode = "Interpolator6_r_hip"

Group313.children.append(ROUTE359)
ROUTE360 = x3d.ROUTE()
ROUTE360.fromField = "value_changed"
ROUTE360.fromNode = "Interpolator6_r_hip"
ROUTE360.toField = "set_rotation"
ROUTE360.toNode = "BvhConversion1_r_hip"

Group313.children.append(ROUTE360)
ROUTE361 = x3d.ROUTE()
ROUTE361.fromField = "fraction_changed"
ROUTE361.fromNode = "RealTimer"
ROUTE361.toField = "set_fraction"
ROUTE361.toNode = "Interpolator7_r_knee"

Group313.children.append(ROUTE361)
ROUTE362 = x3d.ROUTE()
ROUTE362.fromField = "value_changed"
ROUTE362.fromNode = "FrameStepper"
ROUTE362.toField = "set_fraction"
ROUTE362.toNode = "Interpolator7_r_knee"

Group313.children.append(ROUTE362)
ROUTE363 = x3d.ROUTE()
ROUTE363.fromField = "value_changed"
ROUTE363.fromNode = "Interpolator7_r_knee"
ROUTE363.toField = "set_rotation"
ROUTE363.toNode = "BvhConversion1_r_knee"

Group313.children.append(ROUTE363)
ROUTE364 = x3d.ROUTE()
ROUTE364.fromField = "fraction_changed"
ROUTE364.fromNode = "RealTimer"
ROUTE364.toField = "set_fraction"
ROUTE364.toNode = "Interpolator8_r_ankle"

Group313.children.append(ROUTE364)
ROUTE365 = x3d.ROUTE()
ROUTE365.fromField = "value_changed"
ROUTE365.fromNode = "FrameStepper"
ROUTE365.toField = "set_fraction"
ROUTE365.toNode = "Interpolator8_r_ankle"

Group313.children.append(ROUTE365)
ROUTE366 = x3d.ROUTE()
ROUTE366.fromField = "value_changed"
ROUTE366.fromNode = "Interpolator8_r_ankle"
ROUTE366.toField = "set_rotation"
ROUTE366.toNode = "BvhConversion1_r_ankle"

Group313.children.append(ROUTE366)
ROUTE367 = x3d.ROUTE()
ROUTE367.fromField = "fraction_changed"
ROUTE367.fromNode = "RealTimer"
ROUTE367.toField = "set_fraction"
ROUTE367.toNode = "Interpolator9_r_midtarsal"

Group313.children.append(ROUTE367)
ROUTE368 = x3d.ROUTE()
ROUTE368.fromField = "value_changed"
ROUTE368.fromNode = "FrameStepper"
ROUTE368.toField = "set_fraction"
ROUTE368.toNode = "Interpolator9_r_midtarsal"

Group313.children.append(ROUTE368)
ROUTE369 = x3d.ROUTE()
ROUTE369.fromField = "value_changed"
ROUTE369.fromNode = "Interpolator9_r_midtarsal"
ROUTE369.toField = "set_rotation"
ROUTE369.toNode = "BvhConversion1_r_midtarsal"

Group313.children.append(ROUTE369)
ROUTE370 = x3d.ROUTE()
ROUTE370.fromField = "fraction_changed"
ROUTE370.fromNode = "RealTimer"
ROUTE370.toField = "set_fraction"
ROUTE370.toNode = "Interpolator10_vl5"

Group313.children.append(ROUTE370)
ROUTE371 = x3d.ROUTE()
ROUTE371.fromField = "value_changed"
ROUTE371.fromNode = "FrameStepper"
ROUTE371.toField = "set_fraction"
ROUTE371.toNode = "Interpolator10_vl5"

Group313.children.append(ROUTE371)
ROUTE372 = x3d.ROUTE()
ROUTE372.fromField = "value_changed"
ROUTE372.fromNode = "Interpolator10_vl5"
ROUTE372.toField = "set_rotation"
ROUTE372.toNode = "BvhConversion1_vl5"

Group313.children.append(ROUTE372)
ROUTE373 = x3d.ROUTE()
ROUTE373.fromField = "fraction_changed"
ROUTE373.fromNode = "RealTimer"
ROUTE373.toField = "set_fraction"
ROUTE373.toNode = "Interpolator11_Chest2"

Group313.children.append(ROUTE373)
ROUTE374 = x3d.ROUTE()
ROUTE374.fromField = "value_changed"
ROUTE374.fromNode = "FrameStepper"
ROUTE374.toField = "set_fraction"
ROUTE374.toNode = "Interpolator11_Chest2"

Group313.children.append(ROUTE374)
ROUTE375 = x3d.ROUTE()
ROUTE375.fromField = "value_changed"
ROUTE375.fromNode = "Interpolator11_Chest2"
ROUTE375.toField = "set_rotation"
ROUTE375.toNode = "BvhConversion1_Chest2"

Group313.children.append(ROUTE375)
ROUTE376 = x3d.ROUTE()
ROUTE376.fromField = "fraction_changed"
ROUTE376.fromNode = "RealTimer"
ROUTE376.toField = "set_fraction"
ROUTE376.toNode = "Interpolator12_LeftCollar"

Group313.children.append(ROUTE376)
ROUTE377 = x3d.ROUTE()
ROUTE377.fromField = "value_changed"
ROUTE377.fromNode = "FrameStepper"
ROUTE377.toField = "set_fraction"
ROUTE377.toNode = "Interpolator12_LeftCollar"

Group313.children.append(ROUTE377)
ROUTE378 = x3d.ROUTE()
ROUTE378.fromField = "value_changed"
ROUTE378.fromNode = "Interpolator12_LeftCollar"
ROUTE378.toField = "set_rotation"
ROUTE378.toNode = "BvhConversion1_LeftCollar"

Group313.children.append(ROUTE378)
ROUTE379 = x3d.ROUTE()
ROUTE379.fromField = "fraction_changed"
ROUTE379.fromNode = "RealTimer"
ROUTE379.toField = "set_fraction"
ROUTE379.toNode = "Interpolator13_l_shoulder"

Group313.children.append(ROUTE379)
ROUTE380 = x3d.ROUTE()
ROUTE380.fromField = "value_changed"
ROUTE380.fromNode = "FrameStepper"
ROUTE380.toField = "set_fraction"
ROUTE380.toNode = "Interpolator13_l_shoulder"

Group313.children.append(ROUTE380)
ROUTE381 = x3d.ROUTE()
ROUTE381.fromField = "value_changed"
ROUTE381.fromNode = "Interpolator13_l_shoulder"
ROUTE381.toField = "set_rotation"
ROUTE381.toNode = "BvhConversion1_l_shoulder"

Group313.children.append(ROUTE381)
ROUTE382 = x3d.ROUTE()
ROUTE382.fromField = "fraction_changed"
ROUTE382.fromNode = "RealTimer"
ROUTE382.toField = "set_fraction"
ROUTE382.toNode = "Interpolator14_l_elbow"

Group313.children.append(ROUTE382)
ROUTE383 = x3d.ROUTE()
ROUTE383.fromField = "value_changed"
ROUTE383.fromNode = "FrameStepper"
ROUTE383.toField = "set_fraction"
ROUTE383.toNode = "Interpolator14_l_elbow"

Group313.children.append(ROUTE383)
ROUTE384 = x3d.ROUTE()
ROUTE384.fromField = "value_changed"
ROUTE384.fromNode = "Interpolator14_l_elbow"
ROUTE384.toField = "set_rotation"
ROUTE384.toNode = "BvhConversion1_l_elbow"

Group313.children.append(ROUTE384)
ROUTE385 = x3d.ROUTE()
ROUTE385.fromField = "fraction_changed"
ROUTE385.fromNode = "RealTimer"
ROUTE385.toField = "set_fraction"
ROUTE385.toNode = "Interpolator15_l_wrist"

Group313.children.append(ROUTE385)
ROUTE386 = x3d.ROUTE()
ROUTE386.fromField = "value_changed"
ROUTE386.fromNode = "FrameStepper"
ROUTE386.toField = "set_fraction"
ROUTE386.toNode = "Interpolator15_l_wrist"

Group313.children.append(ROUTE386)
ROUTE387 = x3d.ROUTE()
ROUTE387.fromField = "value_changed"
ROUTE387.fromNode = "Interpolator15_l_wrist"
ROUTE387.toField = "set_rotation"
ROUTE387.toNode = "BvhConversion1_l_wrist"

Group313.children.append(ROUTE387)
ROUTE388 = x3d.ROUTE()
ROUTE388.fromField = "fraction_changed"
ROUTE388.fromNode = "RealTimer"
ROUTE388.toField = "set_fraction"
ROUTE388.toNode = "Interpolator16_RightCollar"

Group313.children.append(ROUTE388)
ROUTE389 = x3d.ROUTE()
ROUTE389.fromField = "value_changed"
ROUTE389.fromNode = "FrameStepper"
ROUTE389.toField = "set_fraction"
ROUTE389.toNode = "Interpolator16_RightCollar"

Group313.children.append(ROUTE389)
ROUTE390 = x3d.ROUTE()
ROUTE390.fromField = "value_changed"
ROUTE390.fromNode = "Interpolator16_RightCollar"
ROUTE390.toField = "set_rotation"
ROUTE390.toNode = "BvhConversion1_RightCollar"

Group313.children.append(ROUTE390)
ROUTE391 = x3d.ROUTE()
ROUTE391.fromField = "fraction_changed"
ROUTE391.fromNode = "RealTimer"
ROUTE391.toField = "set_fraction"
ROUTE391.toNode = "Interpolator17_r_shoulder"

Group313.children.append(ROUTE391)
ROUTE392 = x3d.ROUTE()
ROUTE392.fromField = "value_changed"
ROUTE392.fromNode = "FrameStepper"
ROUTE392.toField = "set_fraction"
ROUTE392.toNode = "Interpolator17_r_shoulder"

Group313.children.append(ROUTE392)
ROUTE393 = x3d.ROUTE()
ROUTE393.fromField = "value_changed"
ROUTE393.fromNode = "Interpolator17_r_shoulder"
ROUTE393.toField = "set_rotation"
ROUTE393.toNode = "BvhConversion1_r_shoulder"

Group313.children.append(ROUTE393)
ROUTE394 = x3d.ROUTE()
ROUTE394.fromField = "fraction_changed"
ROUTE394.fromNode = "RealTimer"
ROUTE394.toField = "set_fraction"
ROUTE394.toNode = "Interpolator18_r_elbow"

Group313.children.append(ROUTE394)
ROUTE395 = x3d.ROUTE()
ROUTE395.fromField = "value_changed"
ROUTE395.fromNode = "FrameStepper"
ROUTE395.toField = "set_fraction"
ROUTE395.toNode = "Interpolator18_r_elbow"

Group313.children.append(ROUTE395)
ROUTE396 = x3d.ROUTE()
ROUTE396.fromField = "value_changed"
ROUTE396.fromNode = "Interpolator18_r_elbow"
ROUTE396.toField = "set_rotation"
ROUTE396.toNode = "BvhConversion1_r_elbow"

Group313.children.append(ROUTE396)
ROUTE397 = x3d.ROUTE()
ROUTE397.fromField = "fraction_changed"
ROUTE397.fromNode = "RealTimer"
ROUTE397.toField = "set_fraction"
ROUTE397.toNode = "Interpolator19_r_wrist"

Group313.children.append(ROUTE397)
ROUTE398 = x3d.ROUTE()
ROUTE398.fromField = "value_changed"
ROUTE398.fromNode = "FrameStepper"
ROUTE398.toField = "set_fraction"
ROUTE398.toNode = "Interpolator19_r_wrist"

Group313.children.append(ROUTE398)
ROUTE399 = x3d.ROUTE()
ROUTE399.fromField = "value_changed"
ROUTE399.fromNode = "Interpolator19_r_wrist"
ROUTE399.toField = "set_rotation"
ROUTE399.toNode = "BvhConversion1_r_wrist"

Group313.children.append(ROUTE399)
ROUTE400 = x3d.ROUTE()
ROUTE400.fromField = "fraction_changed"
ROUTE400.fromNode = "RealTimer"
ROUTE400.toField = "set_fraction"
ROUTE400.toNode = "Interpolator20_Neck"

Group313.children.append(ROUTE400)
ROUTE401 = x3d.ROUTE()
ROUTE401.fromField = "value_changed"
ROUTE401.fromNode = "FrameStepper"
ROUTE401.toField = "set_fraction"
ROUTE401.toNode = "Interpolator20_Neck"

Group313.children.append(ROUTE401)
ROUTE402 = x3d.ROUTE()
ROUTE402.fromField = "value_changed"
ROUTE402.fromNode = "Interpolator20_Neck"
ROUTE402.toField = "set_rotation"
ROUTE402.toNode = "BvhConversion1_Neck"

Group313.children.append(ROUTE402)
ROUTE403 = x3d.ROUTE()
ROUTE403.fromField = "fraction_changed"
ROUTE403.fromNode = "RealTimer"
ROUTE403.toField = "set_fraction"
ROUTE403.toNode = "Interpolator21_skullbase"

Group313.children.append(ROUTE403)
ROUTE404 = x3d.ROUTE()
ROUTE404.fromField = "value_changed"
ROUTE404.fromNode = "FrameStepper"
ROUTE404.toField = "set_fraction"
ROUTE404.toNode = "Interpolator21_skullbase"

Group313.children.append(ROUTE404)
ROUTE405 = x3d.ROUTE()
ROUTE405.fromField = "value_changed"
ROUTE405.fromNode = "Interpolator21_skullbase"
ROUTE405.toField = "set_rotation"
ROUTE405.toNode = "BvhConversion1_skullbase"

Group313.children.append(ROUTE405)

Scene28.children.append(Group313)
#All frame data: 1.525 95.398 -0.507 -1.830 -4.400 -0.382 2.832 5.801 2.554 -3.940 -3.766 -3.474 2.425 2.584 0.862 0.000 0.000 0.000 -0.464 5.886 -1.014 2.002 -0.163 3.640 -1.318 -1.286 -0.673 0.000 0.000 0.000 0.000 -0.000 -0.000 4.402 -0.186 0.790 -0.000 -0.000 0.000 -3.045 2.074 -11.595 -4.209 -0.957 15.542 4.621 8.767 2.817 -0.000 -0.000 0.000 1.540 2.825 5.416 -3.038 -2.696 -17.044 2.610 1.767 -0.656 1.122 2.219 -1.735 1.122 2.219 -1.735 1.525 95.398 -0.507 -1.830 -4.400 -0.382 2.832 5.801 2.554 -3.940 -3.766 -3.474 2.425 2.584 0.862 0.000 0.000 0.000 -0.458 5.956 -0.952 1.975 -0.155 3.606 -1.301 -1.366 -0.701 0.000 0.000 0.000 0.000 -0.000 -0.000 4.479 -0.157 0.863 -0.000 -0.000 0.000 -3.035 2.055 -11.710 -4.459 -0.831 15.609 4.876 8.478 2.801 -0.000 -0.000 0.000 1.659 2.754 5.355 -3.173 -2.686 -16.975 2.592 1.746 -0.652 0.994 2.177 -1.744 0.994 2.177 -1.744 1.532 95.393 -0.455 -1.830 -4.400 -0.382 2.893 5.869 2.614 -4.088 -3.824 -3.467 2.508 2.583 0.779 0.000 0.000 0.000 -0.473 6.028 -0.890 1.963 -0.154 3.527 -1.470 -1.455 -0.724 0.000 0.000 0.000 0.000 -0.000 -0.000 4.629 -0.097 0.858 -0.000 0.000 -0.000 -3.241 2.104 -11.923 -4.476 -0.775 15.764 5.043 8.201 2.872 -0.000 0.000 -0.000 1.625 2.670 5.421 -3.237 -2.694 -16.952 2.573 1.725 -0.647 0.806 2.152 -1.742 0.806 2.152 -1.742 1.537 95.390 -0.354 -1.830 -4.400 -0.382 2.886 6.000 2.699 -4.093 -3.949 -3.561 2.508 2.583 0.779 0.000 0.000 0.000 -0.666 6.096 -0.810 2.156 -0.222 3.471 -1.470 -1.455 -0.724 0.000 0.000 0.000 0.000 -0.000 -0.000 4.703 -0.067 0.780 -0.000 -0.000 -0.000 -3.289 2.183 -12.104 -4.554 -0.843 16.093 5.260 8.193 2.845 -0.000 -0.000 -0.000 1.636 2.710 5.518 -3.278 -2.801 -16.891 2.510 1.753 -0.732 0.679 2.173 -1.728 0.679 2.173 -1.728 1.636 95.394 -0.423 -1.830 -4.400 -0.382 2.758 5.911 2.708 -3.961 -3.867 -3.550 2.508 2.583 0.779 0.000 0.000 0.000 -0.870 6.026 -0.855 2.408 -0.301 3.528 -1.510 -1.298 -0.714 0.000 0.000 0.000 0.000 -0.000 -0.000 4.703 -0.067 0.780 -0.000 -0.000 -0.000 -3.298 2.230 -12.444 -4.699 -0.848 16.460 5.576 8.158 2.784 -0.000 -0.000 -0.000 1.709 2.751 5.499 -3.354 -2.836 -16.877 2.510 1.753 -0.732 0.625 2.232 -1.723 0.625 2.232 -1.723 1.613 95.394 -0.530 -1.788 -4.320 -0.425 2.671 5.700 2.765 -3.834 -3.739 -3.622 2.425 2.584 0.862 0.000 0.000 0.000 -1.114 5.746 -0.780 2.575 -0.282 3.583 -1.473 -1.116 -0.781 0.000 0.000 0.000 0.000 -0.000 -0.000 4.663 -0.143 0.833 -0.000 -0.000 -0.000 -3.268 2.342 -12.701 -4.873 -0.836 16.736 5.926 7.998 2.779 -0.000 -0.000 -0.000 1.784 2.737 5.450 -3.425 -2.817 -16.832 2.510 1.753 -0.732 0.570 2.291 -1.718 0.570 2.291 -1.718 1.701 95.395 -0.705 -1.788 -4.320 -0.425 2.564 5.547 2.839 -3.734 -3.667 -3.838 2.423 2.672 1.021 0.000 0.000 0.000 -1.312 5.546 -0.752 2.720 -0.184 3.663 -1.419 -1.013 -0.877 0.000 0.000 0.000 0.000 -0.000 -0.000 4.663 -0.143 0.833 -0.000 -0.000 -0.000 -3.275 2.428 -12.767 -4.928 -0.864 16.900 6.098 8.035 2.685 -0.000 -0.000 -0.000 1.890 2.573 5.415 -3.513 -2.646 -16.791 2.510 1.753 -0.732 0.542 2.382 -1.738 0.542 2.382 -1.738 1.695 95.398 -0.875 -1.788 -4.320 -0.425 2.503 5.395 2.821 -3.590 -3.601 -4.047 2.332 2.757 1.264 0.000 0.000 0.000 -1.370 5.281 -0.733 2.825 -0.080 3.785 -1.462 -0.845 -1.022 0.000 0.000 0.000 0.000 -0.000 -0.000 4.589 -0.174 0.911 -0.000 0.000 -0.000 -3.204 2.548 -12.909 -5.066 -0.882 16.966 6.445 8.073 2.669 -0.000 0.000 -0.000 1.999 2.450 5.349 -3.435 -2.459 -16.667 2.457 1.818 -0.782 0.532 2.517 -1.824 0.532 2.517 -1.824 1.795 95.394 -0.967 -1.729 -4.276 -0.345 2.329 5.212 2.626 -3.461 -3.476 -4.231 2.325 2.768 1.589 0.000 0.000 0.000 -1.429 4.982 -0.663 2.859 0.087 3.801 -1.409 -0.828 -1.236 0.000 0.000 0.000 0.000 -0.000 0.000 4.438 -0.434 0.839 -0.000 -0.000 -0.000 -3.032 2.848 -13.006 -5.290 -0.933 17.091 6.799 8.099 2.684 -0.000 -0.000 -0.000 2.139 2.591 5.420 -3.382 -2.349 -16.615 2.497 1.956 -0.725 0.549 2.713 -1.844 0.549 2.713 -1.844 1.911 95.402 -1.052 -1.670 -4.233 -0.265 2.154 5.029 2.430 -3.333 -3.351 -4.416 2.220 2.825 1.915 0.000 0.000 0.000 -1.483 4.753 -0.530 2.888 0.181 3.758 -1.356 -0.811 -1.451 0.000 0.000 0.000 0.000 0.000 0.000 4.364 -0.665 0.839 -0.000 0.000 -0.000 -2.978 3.184 -13.051 -5.366 -1.020 17.141 7.015 8.088 2.659 -0.000 0.000 -0.000 2.250 2.634 5.497 -3.280 -2.032 -16.628 2.548 1.986 -0.655 0.564 2.917 -1.871 0.564 2.917 -1.871 2.102 95.403 -1.091 -1.686 -4.146 -0.130 2.038 4.867 2.109 -3.267 -3.290 -4.621 2.147 2.789 2.359 0.000 0.000 0.000 -1.449 4.552 -0.398 2.885 0.278 3.636 -1.052 -0.936 -1.733 0.000 0.000 0.000 -0.000 0.000 0.000 4.414 -0.841 0.736 -0.000 -0.000 0.000 -3.038 3.368 -12.979 -5.476 -1.063 17.228 7.312 8.170 2.554 -0.000 -0.000 0.000 2.291 2.607 5.818 -3.207 -1.612 -16.738 2.639 1.993 -0.622 0.525 2.987 -1.912 0.525 2.987 -1.912 2.209 95.398 -1.003 -1.652 -4.113 0.048 2.005 4.847 1.740 -3.332 -3.232 -4.834 2.044 2.666 2.757 0.000 0.000 0.000 -1.471 4.348 -0.167 2.966 0.454 3.296 -0.750 -1.118 -2.046 0.000 0.000 0.000 -0.000 -0.000 0.000 4.340 -0.995 0.668 -0.000 0.000 0.000 -2.953 3.547 -12.996 -5.563 -1.165 17.378 7.607 8.304 2.428 -0.000 0.000 0.000 2.470 2.566 6.172 -3.355 -1.024 -16.778 2.823 2.023 -0.529 0.575 3.124 -1.928 0.575 3.124 -1.928 2.344 95.406 -0.987 -1.609 -3.982 0.263 1.835 4.641 1.343 -3.180 -3.091 -5.116 1.845 2.443 3.323 0.000 0.000 0.000 -1.572 4.038 -0.103 3.100 0.723 3.114 -0.279 -1.418 -2.359 0.000 0.000 0.000 -0.000 -0.000 -0.000 4.319 -1.214 0.585 -0.000 -0.000 -0.000 -2.931 3.691 -13.028 -5.658 -1.192 17.550 7.700 8.389 2.354 -0.000 -0.000 -0.000 2.585 2.545 6.544 -3.476 -0.549 -16.623 2.783 2.154 -0.378 0.604 3.245 -2.011 0.604 3.245 -2.011 2.541 95.411 -1.020 -1.518 -3.905 0.521 1.637 4.424 0.971 -3.135 -2.879 -5.384 1.701 2.216 3.758 0.000 0.000 0.000 -1.786 3.847 -0.142 3.198 0.982 3.064 0.285 -1.735 -2.795 0.000 0.000 0.000 -0.000 -0.000 0.000 4.334 -1.360 0.442 -0.000 0.000 -0.000 -2.951 3.793 -12.893 -5.798 -1.269 17.551 7.862 8.506 2.336 -0.000 0.000 -0.000 2.613 2.503 6.937 -3.632 0.051 -16.369 2.828 2.212 -0.175 0.638 3.355 -2.084 0.638 3.355 -2.084 2.671 95.417 -0.996 -1.467 -3.908 0.824 1.479 4.334 0.677 -3.003 -2.710 -5.697 1.517 2.078 4.073 0.000 0.000 0.000 -1.883 3.735 -0.297 3.220 1.255 2.925 0.895 -1.950 -2.884 0.000 0.000 0.000 -0.000 -0.000 0.000 4.393 -1.430 0.396 -0.000 0.000 -0.000 -2.899 3.865 -12.922 -5.931 -1.254 17.659 7.924 8.673 2.255 -0.000 0.000 -0.000 2.657 2.539 7.243 -3.858 0.530 -16.153 2.966 2.368 0.012 0.650 3.432 -2.207 0.650 3.432 -2.207 2.849 95.433 -0.938 -1.457 -3.991 1.171 1.382 4.387 0.485 -2.981 -2.594 -6.091 1.424 1.814 4.296 0.000 0.000 0.000 -1.936 3.705 -0.498 3.042 1.638 2.798 1.627 -2.363 -2.969 0.000 0.000 0.000 0.000 -0.000 -0.000 4.526 -1.505 0.324 -0.000 0.000 -0.000 -2.899 4.035 -12.813 -6.037 -1.309 17.586 7.957 8.742 2.226 -0.000 0.000 -0.000 2.668 2.709 7.551 -4.077 0.825 -15.928 3.061 2.645 0.148 0.679 3.519 -2.378 0.679 3.519 -2.378 2.979 95.442 -0.816 -1.471 -4.086 1.614 1.380 4.562 0.385 -3.027 -2.662 -6.523 1.323 1.756 4.365 0.000 0.000 0.000 -1.893 3.627 -0.732 2.782 2.160 2.629 2.370 -2.707 -3.036 0.000 0.000 0.000 -0.000 -0.000 0.000 4.573 -1.525 0.202 -0.000 0.000 -0.000 -2.912 4.087 -12.797 -5.955 -1.202 17.668 7.845 8.689 2.177 -0.000 0.000 -0.000 2.790 2.770 7.777 -4.259 1.184 -15.811 3.061 2.831 0.267 0.765 3.581 -2.574 0.765 3.581 -2.574 3.104 95.456 -0.699 -1.536 -4.128 2.016 1.425 4.683 0.324 -3.069 -2.731 -6.792 1.263 1.703 4.320 0.000 0.000 0.000 -1.809 3.293 -0.917 2.424 2.940 2.351 3.110 -3.069 -2.941 0.000 0.000 0.000 -0.000 -0.000 -0.000 4.683 -1.607 0.184 -0.000 -0.000 0.000 -2.888 4.129 -12.692 -5.918 -1.147 17.578 7.800 8.667 2.183 -0.000 -0.000 0.000 2.903 2.836 7.941 -4.351 1.468 -15.822 3.066 3.014 0.412 0.821 3.735 -2.819 0.821 3.735 -2.819 3.108 95.484 -0.578 -1.675 -4.129 2.471 1.630 4.756 0.333 -3.114 -2.800 -6.949 1.124 1.644 4.033 0.000 0.000 0.000 -1.588 2.841 -1.296 1.953 3.958 2.217 3.843 -3.478 -2.815 0.000 0.000 0.000 0.000 -0.000 -0.000 4.908 -1.630 0.156 -0.000 -0.000 -0.000 -2.879 3.962 -12.733 -5.844 -1.018 17.685 7.508 8.704 2.155 -0.000 -0.000 -0.000 2.973 2.792 8.067 -4.534 1.625 -15.841 3.160 3.257 0.503 0.885 3.744 -3.067 0.885 3.744 -3.067 3.064 95.509 -0.361 -1.827 -3.996 2.839 1.915 4.823 0.646 -3.249 -2.986 -7.172 0.939 1.615 3.632 0.000 0.000 0.000 -1.383 2.180 -1.652 1.364 5.178 2.248 4.539 -4.030 -2.715 0.000 0.000 0.000 -0.000 -0.000 -0.000 4.989 -1.836 0.228 0.000 0.000 -0.000 -2.738 3.867 -12.616 -5.656 -0.885 17.688 7.127 8.651 2.181 0.000 0.000 -0.000 3.122 2.816 8.234 -4.564 1.719 -15.971 3.144 3.318 0.582 1.021 3.839 -3.309 1.021 3.839 -3.309 2.987 95.525 -0.159 -1.903 -3.905 3.155 2.249 4.936 1.053 -3.595 -3.162 -7.201 0.738 1.510 2.976 0.000 0.000 0.000 -1.239 1.564 -1.952 0.709 6.560 2.158 5.355 -4.617 -2.514 0.000 0.000 0.000 0.000 -0.000 -0.000 4.997 -1.994 0.355 -0.000 -0.000 0.000 -2.598 3.771 -12.498 -5.466 -0.838 17.687 6.656 8.664 2.225 -0.000 -0.000 0.000 3.317 2.772 8.481 -4.748 1.856 -16.153 3.263 3.431 0.576 1.110 3.936 -3.554 1.110 3.936 -3.554 2.964 95.545 0.155 -2.113 -3.820 3.442 2.713 5.176 1.565 -4.032 -3.447 -7.411 0.715 1.494 2.408 0.000 0.000 0.000 -0.926 0.874 -2.160 -0.147 8.307 1.976 6.408 -5.413 -2.202 0.000 0.000 0.000 -0.000 -0.000 0.000 5.134 -2.152 0.351 -0.000 0.000 -0.000 -2.554 3.751 -12.255 -5.083 -0.779 17.788 6.071 8.633 2.281 -0.000 0.000 -0.000 3.374 2.794 9.007 -4.805 1.830 -16.352 3.389 3.411 0.615 1.222 4.064 -3.749 1.222 4.064 -3.749 2.882 95.538 0.362 -2.259 -3.641 3.590 3.157 5.269 2.200 -4.626 -3.726 -7.847 1.136 1.636 2.008 0.000 0.000 0.000 -0.768 -0.053 -2.479 -1.141 10.495 2.053 7.621 -6.302 -1.800 0.000 0.000 0.000 0.000 -0.000 0.000 5.114 -2.408 0.361 -0.000 -0.000 -0.000 -2.299 3.811 -11.839 -4.736 -0.882 17.746 5.442 8.697 2.336 -0.000 -0.000 -0.000 3.517 2.842 9.666 -4.859 1.672 -16.503 3.488 3.329 0.612 1.439 4.196 -3.880 1.439 4.196 -3.880 2.795 95.526 0.423 -2.367 -3.381 3.693 3.491 5.176 2.704 -5.089 -3.984 -8.492 1.477 1.858 2.015 0.000 0.000 0.000 -0.547 -1.478 -3.062 -2.312 13.174 2.620 8.407 -6.965 -1.502 0.000 0.000 0.000 -0.000 -0.000 0.000 5.052 -2.737 0.425 -0.000 0.000 -0.000 -2.045 3.871 -11.423 -4.470 -1.060 17.611 4.913 8.711 2.451 -0.000 0.000 -0.000 3.527 2.887 10.239 -4.715 1.345 -16.511 3.492 3.102 0.569 1.670 4.303 -4.039 1.670 4.303 -4.039 2.736 95.504 0.361 -2.411 -3.025 3.658 3.644 4.934 3.074 -5.372 -4.291 -8.919 1.693 2.191 2.150 0.000 0.000 0.000 -0.327 -3.357 -3.743 -3.755 16.236 3.738 8.889 -7.623 -1.209 0.000 0.000 0.000 -0.000 -0.000 -0.000 4.850 -3.171 0.563 -0.000 -0.000 0.000 -1.723 4.041 -11.004 -4.190 -1.252 17.557 4.275 8.641 2.443 -0.000 -0.000 0.000 3.612 2.905 10.841 -4.612 0.987 -16.514 3.542 2.876 0.504 1.923 4.450 -4.134 1.923 4.450 -4.134 2.679 95.475 0.280 -2.308 -2.597 3.697 3.663 4.533 3.132 -5.631 -4.444 -9.088 1.768 2.356 2.227 0.000 0.000 0.000 -0.101 -5.527 -4.866 -5.427 19.329 5.344 9.171 -8.123 -1.000 0.000 0.000 0.000 -0.000 -0.000 0.000 4.434 -3.522 0.490 -0.000 -0.000 -0.000 -1.275 4.143 -10.556 -3.975 -1.532 17.426 3.677 8.508 2.574 -0.000 -0.000 -0.000 3.809 2.736 11.519 -4.489 0.496 -16.452 3.497 2.525 0.401 2.225 4.554 -4.180 2.225 4.554 -4.180 2.688 95.452 0.164 -2.184 -2.254 3.600 3.625 4.224 3.097 -5.839 -4.620 -9.030 1.647 2.407 2.479 0.000 0.000 0.000 0.234 -7.670 -6.233 -7.364 22.065 7.520 9.449 -8.477 -0.949 0.000 0.000 0.000 -0.000 -0.000 0.000 3.905 -3.723 0.585 -0.000 -0.000 -0.000 -0.673 4.130 -10.282 -3.996 -1.678 17.284 3.351 8.146 2.705 -0.000 -0.000 -0.000 4.130 2.478 11.957 -4.277 -0.014 -16.404 3.342 2.142 0.298 2.604 4.600 -4.219 2.604 4.600 -4.219 2.727 95.423 0.155 -2.041 -2.198 3.405 3.565 4.357 3.034 -6.027 -4.960 -8.717 1.432 2.502 2.571 0.000 0.000 0.000 0.461 -9.543 -7.630 -9.184 24.384 9.752 9.727 -8.784 -0.848 0.000 0.000 0.000 -0.000 -0.000 -0.000 3.354 -3.559 0.642 -0.000 0.000 -0.000 -0.036 4.026 -10.058 -4.128 -1.736 17.246 3.253 7.748 2.867 -0.000 0.000 -0.000 4.499 2.208 12.379 -4.152 -0.662 -16.263 3.376 1.825 0.150 3.021 4.583 -4.230 3.021 4.583 -4.230 2.749 95.428 0.220 -1.997 -2.169 3.097 3.597 4.517 3.079 -6.116 -5.149 -8.476 0.911 2.278 2.776 0.000 0.000 0.000 0.702 -11.270 -9.123 -10.832 26.084 12.059 9.901 -8.908 -0.705 0.000 0.000 0.000 -0.000 -0.000 -0.000 3.009 -3.417 0.849 -0.000 0.000 0.000 0.465 3.904 -9.949 -4.562 -1.635 17.153 3.622 7.247 2.999 -0.000 0.000 0.000 4.712 1.964 12.623 -3.935 -1.345 -16.187 3.469 1.655 0.098 3.364 4.559 -4.236 3.364 4.559 -4.236 2.748 95.440 0.325 -2.017 -2.151 2.701 3.666 4.755 3.140 -6.099 -5.421 -8.085 0.172 2.093 2.855 0.000 0.000 0.000 1.083 -12.809 -10.408 -12.305 27.107 14.091 10.197 -8.753 -0.636 0.000 0.000 0.000 0.000 -0.000 0.000 2.828 -3.308 1.035 -0.000 -0.000 -0.000 0.751 3.884 -9.859 -4.957 -1.490 17.124 4.293 6.781 2.970 -0.000 -0.000 -0.000 4.852 1.881 12.884 -3.641 -2.099 -16.050 3.469 1.587 -0.001 3.670 4.528 -4.161 3.670 4.528 -4.161 2.802 95.453 0.373 -2.022 -2.067 2.354 3.740 4.861 3.226 -6.181 -5.613 -7.682 -0.622 1.828 2.788 0.000 0.000 0.000 1.535 -14.279 -11.470 -13.445 27.514 15.497 10.464 -8.448 -0.465 0.000 0.000 0.000 0.000 -0.000 0.000 2.623 -3.265 1.026 -0.000 -0.000 0.000 0.993 3.798 -9.700 -5.492 -1.208 17.210 5.434 6.341 2.951 -0.000 -0.000 0.000 4.994 1.754 13.251 -3.381 -2.789 -16.011 3.617 1.641 -0.071 3.908 4.452 -4.014 3.908 4.452 -4.014 2.915 95.489 0.621 -2.195 -1.968 2.067 3.909 5.054 3.398 -6.189 -5.748 -7.268 -1.414 1.412 2.548 0.000 0.000 0.000 2.117 -15.796 -12.185 -14.087 27.612 16.102 10.805 -8.170 -0.123 0.000 0.000 0.000 -0.000 -0.000 0.000 2.613 -3.327 0.980 -0.000 0.000 -0.000 1.080 3.721 -9.610 -6.083 -0.770 17.381 6.817 5.907 2.939 -0.000 0.000 -0.000 5.119 1.730 13.433 -3.108 -3.592 -15.857 3.721 1.773 -0.109 4.070 4.364 -3.888 4.070 4.364 -3.888 3.068 95.527 0.772 -2.366 -1.868 1.781 4.035 5.117 3.578 -6.148 -5.755 -6.844 -2.257 1.031 2.350 0.000 0.000 0.000 2.654 -17.134 -12.441 -14.284 27.350 16.004 11.260 -7.961 0.241 0.000 0.000 0.000 -0.000 -0.000 0.000 2.648 -3.282 0.983 -0.000 -0.000 0.000 1.078 3.555 -9.714 -6.782 -0.447 17.699 8.473 5.633 2.956 -0.000 -0.000 0.000 5.223 1.651 13.444 -2.933 -4.311 -15.620 3.825 1.863 0.006 4.233 4.188 -3.751 4.233 4.188 -3.751 3.326 95.554 1.040 -2.599 -1.762 1.676 4.210 5.270 3.632 -6.255 -5.851 -6.498 -2.712 0.719 2.203 0.000 0.000 0.000 3.067 -18.434 -12.499 -13.784 26.779 15.334 11.640 -7.608 0.281 0.000 0.000 0.000 0.000 -0.000 0.000 2.743 -3.262 0.865 -0.000 -0.000 -0.000 0.958 3.452 -10.014 -7.366 -0.186 18.157 10.138 5.473 2.880 -0.000 -0.000 -0.000 5.272 1.640 13.314 -2.817 -5.092 -15.370 4.033 1.918 -0.032 4.369 3.985 -3.621 4.369 3.985 -3.621 3.523 95.570 1.300 -2.857 -1.671 1.667 4.372 5.431 3.683 -6.254 -6.034 -6.158 -3.012 0.746 1.879 0.000 0.000 0.000 3.389 -19.657 -12.067 -12.847 26.030 13.999 12.081 -7.139 0.272 0.000 0.000 0.000 0.000 -0.000 0.000 2.855 -3.227 0.738 0.000 0.000 -0.000 0.994 3.398 -10.527 -8.003 -0.176 18.613 11.711 5.545 2.850 0.000 0.000 -0.000 5.269 1.599 12.955 -2.493 -5.878 -15.055 3.993 1.974 -0.016 4.461 3.836 -3.529 4.461 3.836 -3.529 3.664 95.573 1.567 -3.081 -1.700 1.648 4.511 5.697 3.932 -6.269 -6.180 -5.850 -3.086 0.936 1.377 0.000 0.000 0.000 3.733 -20.693 -11.138 -11.560 25.105 12.156 12.361 -6.481 0.108 0.000 0.000 0.000 -0.000 0.000 0.000 2.946 -3.078 0.679 -0.000 -0.000 0.000 0.959 3.390 -11.087 -8.581 -0.177 18.894 13.076 5.719 2.716 -0.000 -0.000 0.000 5.276 1.532 12.340 -2.150 -6.544 -14.652 3.868 1.965 0.014 4.517 3.664 -3.496 4.517 3.664 -3.496 3.794 95.564 1.907 -3.330 -1.745 1.724 4.675 6.015 4.208 -6.302 -6.361 -5.670 -2.961 1.307 0.904 0.000 0.000 0.000 4.112 -21.689 -9.835 -10.216 24.072 9.994 12.755 -5.588 -0.039 0.000 0.000 0.000 -0.000 -0.000 0.000 2.951 -2.870 0.569 -0.000 -0.000 -0.000 1.014 3.290 -11.670 -8.991 -0.177 18.966 14.096 6.116 2.473 -0.000 -0.000 -0.000 5.316 1.424 11.730 -1.797 -7.041 -14.440 3.912 1.779 0.000 4.630 3.519 -3.423 4.630 3.519 -3.423 3.913 95.539 2.286 -3.490 -1.866 1.869 4.768 6.474 4.567 -6.355 -6.514 -5.491 -2.640 1.623 0.178 0.000 0.000 0.000 4.537 -22.466 -8.316 -8.861 22.792 7.758 13.123 -4.719 -0.128 0.000 0.000 0.000 -0.000 -0.000 0.000 2.874 -2.595 0.451 -0.000 -0.000 -0.000 1.131 3.222 -12.193 -9.300 -0.185 18.901 14.793 6.600 2.142 -0.000 -0.000 -0.000 5.408 1.337 11.201 -1.420 -7.410 -14.354 3.702 1.612 -0.078 4.801 3.375 -3.439 4.801 3.375 -3.439 3.997 95.611 2.654 -3.724 -1.948 2.070 5.028 6.758 4.914 -6.570 -6.518 -5.438 -2.228 1.925 -0.470 0.000 0.000 0.000 5.097 -23.281 -6.896 -7.833 21.462 5.844 13.683 -3.983 -0.074 0.000 0.000 0.000 -0.000 0.000 -0.000 2.820 -2.467 0.317 -0.000 -0.000 -0.000 1.408 3.282 -12.690 -9.453 -0.310 18.814 15.001 7.136 1.763 -0.000 -0.000 -0.000 5.612 1.366 10.764 -1.309 -7.635 -14.538 3.652 1.493 -0.150 5.005 3.220 -3.488 5.005 3.220 -3.488 4.086 95.685 3.027 -3.908 -2.087 2.310 5.243 7.095 5.218 -6.790 -6.514 -5.549 -1.812 2.210 -0.956 0.000 0.000 0.000 5.639 -23.815 -5.735 -6.995 19.823 4.354 14.256 -3.190 -0.018 0.000 0.000 0.000 -0.000 -0.000 0.000 2.795 -2.257 0.220 -0.000 -0.000 -0.000 1.696 3.361 -13.027 -9.502 -0.547 18.612 14.940 7.661 1.443 -0.000 -0.000 -0.000 5.741 1.363 10.257 -1.127 -7.609 -14.612 3.563 1.208 -0.187 5.167 3.106 -3.565 5.167 3.106 -3.565 4.126 95.737 3.427 -3.959 -2.220 2.574 5.401 7.452 5.437 -7.076 -6.527 -5.769 -1.394 2.480 -1.281 0.000 0.000 0.000 5.963 -24.190 -5.033 -6.361 18.179 3.538 14.725 -2.524 -0.058 0.000 0.000 0.000 -0.000 -0.000 0.000 2.669 -2.128 0.129 -0.000 -0.000 0.000 1.875 3.430 -13.283 -9.316 -0.761 18.473 14.566 8.000 1.271 -0.000 -0.000 0.000 5.897 1.508 9.897 -1.020 -7.425 -14.738 3.394 1.036 -0.272 5.226 3.067 -3.685 5.226 3.067 -3.685 4.229 95.755 3.817 -3.913 -2.229 2.876 5.451 7.616 5.475 -7.408 -6.390 -6.067 -0.796 2.567 -1.472 0.000 0.000 0.000 6.008 -24.616 -4.861 -5.900 16.546 3.190 15.164 -1.653 -0.009 0.000 0.000 0.000 -0.000 0.000 -0.000 2.440 -2.120 0.012 -0.000 -0.000 0.000 2.102 3.392 -13.322 -9.032 -0.863 18.285 13.945 8.315 1.232 -0.000 -0.000 0.000 6.040 1.626 9.694 -1.017 -7.048 -14.871 3.358 1.036 -0.336 5.259 2.999 -3.781 5.259 2.999 -3.781 4.324 95.748 4.154 -3.791 -2.276 3.122 5.421 7.827 5.568 -7.745 -6.324 -6.534 -0.115 2.673 -1.495 0.000 0.000 0.000 5.955 -25.033 -5.056 -5.610 15.137 3.344 15.456 -0.618 -0.112 0.000 0.000 0.000 0.000 -0.000 0.000 2.218 -2.042 0.027 -0.000 -0.000 -0.000 2.297 3.392 -13.351 -8.679 -1.057 18.239 13.114 8.409 1.293 -0.000 -0.000 -0.000 6.091 1.741 9.615 -1.007 -6.487 -15.068 3.296 1.015 -0.349 5.162 2.891 -3.884 5.162 2.891 -3.884 4.686 95.798 4.288 -3.800 -2.328 3.342 5.151 7.796 5.734 -7.691 -6.045 -7.137 0.616 2.870 -1.389 0.000 0.000 0.000 5.951 -25.594 -5.571 -5.433 14.156 3.885 15.765 0.205 -0.207 0.000 0.000 0.000 0.000 -0.000 0.000 2.282 -1.910 0.065 -0.000 -0.000 -0.000 2.296 3.315 -13.184 -8.128 -1.132 18.186 12.128 8.237 1.340 -0.000 -0.000 -0.000 6.109 1.778 9.611 -1.190 -5.747 -15.391 3.449 0.825 -0.406 4.989 2.754 -3.985 4.989 2.754 -3.985 5.026 95.797 4.410 -3.693 -2.338 3.462 4.869 7.759 5.844 -7.823 -5.770 -7.842 1.368 2.937 -1.104 0.000 0.000 0.000 5.717 -26.312 -5.990 -5.215 13.565 4.260 16.046 0.719 -0.079 0.000 0.000 0.000 -0.000 -0.000 -0.000 2.257 -1.883 0.087 -0.000 -0.000 -0.000 2.306 3.296 -12.746 -7.612 -1.281 18.124 11.103 7.969 1.417 -0.000 -0.000 -0.000 5.961 1.955 9.850 -1.230 -5.161 -15.872 3.565 0.532 -0.413 4.815 2.630 -4.002 4.815 2.630 -4.002 5.385 95.799 4.541 -3.637 -2.293 3.544 4.624 7.687 5.802 -7.928 -5.537 -8.355 2.078 3.013 -0.864 0.000 0.000 0.000 5.532 -27.105 -6.157 -5.066 13.213 4.577 16.321 1.095 -0.132 0.000 0.000 0.000 0.000 -0.000 0.000 2.354 -1.880 0.161 -0.000 -0.000 -0.000 2.245 3.246 -12.318 -7.103 -1.359 18.081 10.085 7.586 1.677 -0.000 -0.000 -0.000 5.787 2.032 10.161 -1.192 -4.512 -16.366 3.659 -0.062 -0.634 4.596 2.513 -3.997 4.596 2.513 -3.997 5.727 95.773 4.701 -3.509 -2.387 3.528 4.279 7.848 5.587 -7.911 -5.437 -8.525 2.510 2.956 -0.631 0.000 0.000 0.000 5.394 -27.538 -6.030 -4.876 12.773 4.591 16.494 1.410 -0.207 0.000 0.000 0.000 0.000 -0.000 -0.000 2.464 -1.701 0.256 -0.000 -0.000 -0.000 2.065 3.105 -11.894 -6.561 -1.457 18.113 8.981 7.162 1.941 -0.000 -0.000 -0.000 5.564 2.141 10.420 -1.319 -4.118 -16.781 3.716 -0.572 -0.856 4.383 2.382 -3.950 4.383 2.382 -3.950 5.976 95.748 4.883 -3.382 -2.480 3.512 4.056 8.029 5.209 -8.002 -5.374 -8.388 2.796 2.891 -0.425 0.000 0.000 0.000 5.285 -27.884 -5.833 -4.723 12.336 4.533 16.630 1.658 -0.391 0.000 0.000 0.000 0.000 -0.000 -0.000 2.499 -1.551 0.423 -0.000 -0.000 0.000 1.964 2.991 -11.548 -6.020 -1.559 18.146 7.916 6.807 2.278 -0.000 -0.000 0.000 5.332 2.205 10.588 -1.342 -3.766 -17.067 3.537 -1.046 -0.989 4.189 2.296 -3.971 4.189 2.296 -3.971 6.095 95.678 5.148 -3.178 -2.613 3.442 3.881 8.347 4.881 -8.145 -5.328 -8.018 2.766 2.506 -0.357 0.000 0.000 0.000 5.059 -28.083 -5.606 -4.541 11.871 4.349 16.596 2.046 -0.493 0.000 0.000 0.000 -0.000 -0.000 -0.000 2.391 -1.387 0.634 -0.000 0.000 -0.000 1.889 2.928 -11.343 -5.440 -1.670 18.169 6.972 6.462 2.676 -0.000 0.000 -0.000 5.233 2.205 10.649 -1.449 -3.487 -17.162 3.287 -1.327 -1.029 4.045 2.256 -3.951 4.045 2.256 -3.951 6.236 95.595 5.447 -3.050 -2.707 3.427 3.797 8.687 4.656 -8.308 -5.339 -7.658 2.491 1.980 -0.428 0.000 0.000 0.000 4.895 -28.279 -5.433 -4.342 11.465 4.053 16.314 2.605 -0.615 0.000 0.000 0.000 -0.000 -0.000 -0.000 2.348 -1.261 0.726 -0.000 -0.000 -0.000 1.778 2.367 -11.131 -5.006 -1.217 18.232 6.114 6.135 2.892 -0.000 -0.000 -0.000 5.158 2.175 10.578 -1.602 -3.263 -17.099 3.155 -1.443 -0.940 3.922 2.209 -3.906 3.922 2.209 -3.906 6.390 95.491 5.717 -2.963 -2.881 3.457 3.816 9.210 4.560 -8.662 -5.579 -7.438 2.251 1.555 -0.456 0.000 0.000 0.000 4.761 -28.366 -5.258 -4.226 11.176 3.573 15.888 3.305 -0.704 0.000 0.000 0.000 -0.000 -0.000 -0.000 2.477 -1.180 0.684 -0.000 -0.000 0.000 1.457 1.801 -11.002 -4.594 -0.705 18.375 5.450 6.220 3.057 -0.000 -0.000 0.000 5.015 2.181 10.467 -1.793 -2.937 -16.919 3.150 -1.487 -0.812 3.698 2.204 -3.855 3.698 2.204 -3.855 6.538 95.353 6.001 -2.779 -2.930 3.524 3.818 9.685 4.725 -9.278 -5.737 -7.541 2.117 0.921 -0.553 0.000 0.000 0.000 4.480 -28.508 -5.256 -4.109 11.011 3.108 15.232 4.014 -0.661 0.000 0.000 0.000 -0.000 -0.000 0.000 2.428 -1.251 0.690 -0.000 -0.000 0.000 1.273 1.309 -11.033 -4.316 -0.251 18.509 4.885 6.382 3.116 -0.000 -0.000 0.000 5.041 2.222 10.070 -1.964 -2.786 -16.687 3.190 -1.425 -0.671 3.561 2.262 -3.777 3.561 2.262 -3.777 6.766 95.202 6.284 -2.723 -2.884 3.605 3.800 10.010 5.008 -9.699 -5.925 -7.826 2.104 0.508 -0.639 0.000 0.000 0.000 4.313 -28.751 -5.270 -4.137 10.971 2.623 14.490 4.750 -0.498 0.000 0.000 0.000 -0.000 -0.000 0.000 2.582 -1.403 0.669 -0.000 -0.000 0.000 1.018 0.924 -11.143 -4.202 0.165 18.577 4.511 6.607 3.090 -0.000 -0.000 0.000 4.864 2.267 9.621 -1.938 -2.768 -16.506 3.339 -1.249 -0.616 3.396 2.310 -3.753 3.396 2.310 -3.753 6.955 95.129 6.687 -2.787 -2.980 3.744 3.922 10.485 5.023 -10.000 -6.089 -7.994 2.148 0.206 -0.660 0.000 0.000 0.000 4.076 -28.998 -5.394 -4.021 11.346 2.158 13.514 5.455 -0.456 0.000 0.000 0.000 -0.000 -0.000 0.000 2.913 -1.574 0.656 -0.000 -0.000 -0.000 0.746 0.926 -11.385 -4.005 0.346 18.604 4.143 6.907 2.992 -0.000 -0.000 -0.000 4.673 2.565 8.991 -1.932 -2.942 -16.269 3.469 -1.086 -0.587 3.207 2.429 -3.772 3.207 2.429 -3.772 7.077 95.044 7.052 -2.770 -3.016 3.871 3.968 10.864 4.934 -10.215 -6.238 -8.108 2.161 -0.149 -0.649 0.000 0.000 0.000 3.852 -29.205 -5.481 -4.072 11.725 1.878 12.540 6.193 -0.416 0.000 0.000 0.000 0.000 -0.000 -0.000 3.058 -1.752 0.623 -0.000 -0.000 -0.000 0.545 0.939 -11.764 -3.850 0.473 18.716 3.937 7.302 2.990 -0.000 -0.000 -0.000 4.508 2.777 8.415 -1.814 -3.212 -16.136 3.606 -0.946 -0.431 3.095 2.557 -3.795 3.095 2.557 -3.795 7.279 94.997 7.453 -2.834 -3.112 4.010 4.032 11.292 4.697 -10.422 -6.398 -8.175 2.397 -0.282 -0.472 0.000 0.000 0.000 3.711 -29.168 -5.606 -4.239 12.067 1.699 11.618 6.889 -0.372 0.000 0.000 0.000 -0.000 -0.000 -0.000 3.330 -1.767 0.469 -0.000 0.000 -0.000 0.233 0.741 -12.096 -3.825 0.781 18.923 3.963 7.524 2.789 -0.000 0.000 -0.000 4.292 2.944 7.991 -1.673 -3.501 -15.922 3.658 -0.890 -0.411 2.959 2.635 -3.763 2.959 2.635 -3.763 7.432 94.971 7.767 -2.894 -3.109 4.192 4.171 11.418 4.302 -10.670 -6.292 -8.092 2.596 -0.476 -0.350 0.000 0.000 0.000 3.611 -29.193 -5.762 -4.391 12.453 1.617 10.724 7.669 -0.294 0.000 0.000 0.000 -0.000 0.000 -0.000 3.514 -1.914 0.353 -0.000 -0.000 -0.000 -0.025 0.674 -12.409 -3.757 1.000 19.027 4.084 7.758 2.702 -0.000 -0.000 -0.000 4.156 3.078 7.450 -1.646 -3.894 -15.801 3.737 -0.759 -0.290 2.875 2.727 -3.828 2.875 2.727 -3.828 7.607 94.925 8.138 -2.881 -3.244 4.276 4.246 11.632 4.069 -10.996 -6.028 -7.993 2.725 -0.814 -0.277 0.000 0.000 0.000 3.499 -28.912 -5.893 -4.530 12.742 1.783 9.883 8.483 -0.209 0.000 0.000 0.000 -0.000 -0.000 0.000 3.691 -2.065 0.321 0.000 -0.000 -0.000 -0.272 0.724 -12.724 -3.836 1.227 19.233 4.290 7.974 2.529 0.000 -0.000 -0.000 3.969 3.421 6.945 -1.702 -4.206 -15.778 3.898 -0.641 -0.056 2.782 2.862 -3.868 2.782 2.862 -3.868 7.858 94.894 8.536 -2.864 -3.280 4.404 4.176 11.789 3.899 -11.114 -5.740 -7.876 2.874 -1.135 -0.270 0.000 0.000 0.000 3.370 -28.541 -6.079 -4.663 12.841 1.956 9.351 9.288 0.080 0.000 0.000 0.000 0.000 -0.000 -0.000 3.839 -2.504 0.237 -0.000 0.000 -0.000 -0.563 0.911 -12.940 -3.877 1.681 19.382 4.500 7.972 2.455 -0.000 0.000 -0.000 3.800 3.895 6.407 -1.702 -4.380 -15.677 3.996 -0.568 0.058 2.703 3.154 -3.958 2.703 3.154 -3.958 8.080 94.862 9.050 -2.927 -3.377 4.542 4.329 12.067 3.893 -11.452 -5.385 -7.901 3.001 -1.482 -0.346 0.000 0.000 0.000 3.349 -28.032 -6.214 -4.740 12.968 2.102 8.889 9.875 0.424 0.000 0.000 0.000 0.000 -0.000 -0.000 4.057 -2.882 0.071 -0.000 0.000 -0.000 -0.850 1.177 -13.157 -3.975 1.889 19.504 4.838 7.993 2.432 -0.000 0.000 -0.000 3.680 4.353 6.049 -1.753 -4.441 -15.808 4.016 -0.566 0.184 2.680 3.433 -3.960 2.680 3.433 -3.960 8.325 94.785 9.670 -2.857 -3.466 4.709 4.415 12.411 3.921 -11.936 -4.985 -7.924 3.215 -1.911 -0.506 0.000 0.000 0.000 3.290 -27.395 -6.292 -4.788 12.901 2.104 8.374 10.507 0.978 0.000 0.000 0.000 -0.000 -0.000 0.000 4.172 -3.341 -0.086 -0.000 -0.000 -0.000 -1.099 1.400 -13.344 -4.169 2.289 19.582 5.147 7.936 2.415 -0.000 -0.000 -0.000 3.573 4.765 5.702 -1.891 -4.321 -16.070 4.090 -0.413 0.377 2.692 3.689 -3.985 2.692 3.689 -3.985 8.607 94.679 10.345 -2.844 -3.601 4.794 4.476 12.871 4.057 -12.335 -4.491 -7.964 3.329 -2.598 -0.691 0.000 0.000 0.000 3.332 -26.713 -6.284 -4.840 12.921 2.249 7.803 10.978 1.361 0.000 0.000 0.000 0.000 -0.000 0.000 4.396 -3.647 -0.121 -0.000 0.000 -0.000 -1.505 1.490 -13.641 -4.277 2.728 19.751 5.429 7.822 2.311 -0.000 0.000 -0.000 3.537 5.037 5.377 -2.104 -4.073 -16.359 4.147 -0.407 0.337 2.669 3.861 -4.065 2.669 3.861 -4.065 8.943 94.587 11.057 -2.844 -3.601 4.794 4.586 13.133 4.257 -12.866 -3.907 -8.058 3.485 -3.137 -0.828 0.000 0.000 0.000 3.508 -26.059 -5.890 -4.872 12.766 2.137 7.155 11.529 1.650 0.000 0.000 0.000 0.000 -0.000 0.000 4.604 -4.009 -0.175 -0.000 -0.000 -0.000 -1.851 1.657 -13.809 -4.468 3.019 19.810 5.839 7.626 2.263 -0.000 -0.000 -0.000 3.517 5.242 5.169 -2.266 -3.783 -16.675 4.198 -0.323 0.402 2.634 4.008 -4.079 2.634 4.008 -4.079 9.284 94.493 11.717 -2.788 -3.555 4.876 4.594 13.284 4.324 -13.250 -3.298 -7.981 3.411 -3.716 -1.031 0.000 0.000 0.000 3.553 -25.369 -5.460 -4.771 12.569 1.776 6.450 12.025 1.836 0.000 0.000 0.000 -0.000 -0.000 -0.000 4.794 -4.312 -0.257 -0.000 0.000 -0.000 -2.134 1.745 -13.953 -4.691 3.356 19.724 6.109 7.313 2.219 -0.000 0.000 -0.000 3.390 5.267 4.751 -2.360 -3.397 -16.739 4.237 -0.189 0.454 2.583 4.038 -4.119 2.583 4.038 -4.119 9.713 94.401 12.495 -2.788 -3.555 4.876 4.644 13.482 4.468 -13.683 -2.509 -7.973 3.336 -4.305 -1.247 0.000 0.000 0.000 3.783 -24.506 -4.876 -4.624 12.111 1.243 5.432 12.794 1.894 0.000 0.000 0.000 -0.000 -0.000 -0.000 5.122 -4.542 -0.336 -0.000 -0.000 -0.000 -2.512 1.905 -13.922 -4.941 3.591 19.625 6.453 7.090 2.122 -0.000 -0.000 -0.000 3.257 5.308 4.395 -2.548 -3.094 -16.717 4.348 0.077 0.589 2.461 4.087 -4.086 2.461 4.087 -4.086 10.169 94.290 13.364 -2.769 -3.389 4.966 4.681 13.528 4.341 -14.109 -1.700 -7.766 3.176 -4.922 -1.485 0.000 0.000 0.000 3.936 -23.810 -4.384 -4.395 11.605 0.581 4.140 13.562 1.888 0.000 0.000 0.000 0.000 0.000 -0.000 5.300 -4.888 -0.593 -0.000 0.000 -0.000 -2.730 1.980 -13.646 -5.149 3.847 19.449 6.708 6.899 2.030 -0.000 0.000 -0.000 3.152 5.315 4.193 -2.732 -2.723 -16.760 4.324 0.340 0.734 2.452 4.164 -3.999 2.452 4.164 -3.999 10.624 94.188 14.229 -2.783 -3.253 4.881 4.712 13.618 4.388 -14.538 -0.891 -7.556 3.018 -5.406 -1.710 0.000 0.000 0.000 4.221 -23.154 -3.834 -4.292 11.388 0.121 3.029 13.691 1.788 0.000 0.000 0.000 0.000 -0.000 -0.000 5.507 -5.118 -0.646 -0.000 -0.000 0.000 -2.927 1.985 -13.408 -5.518 4.092 19.295 7.191 6.611 1.897 -0.000 -0.000 0.000 3.159 5.313 3.969 -2.960 -2.460 -16.735 4.292 0.671 0.807 2.460 4.146 -3.935 2.460 4.146 -3.935 11.111 94.118 15.174 -2.852 -3.164 4.714 4.771 13.815 4.441 -14.964 -0.161 -7.287 2.837 -5.591 -1.954 0.000 0.000 0.000 4.748 -22.484 -3.383 -4.429 11.154 0.155 2.306 13.478 1.547 0.000 0.000 0.000 -0.000 -0.000 0.000 5.749 -5.218 -0.653 -0.000 -0.000 0.000 -3.176 1.907 -13.103 -5.802 4.360 19.105 7.768 6.338 1.886 -0.000 -0.000 0.000 3.165 5.179 3.909 -3.290 -2.053 -16.865 4.348 0.913 0.895 2.515 4.171 -3.819 2.515 4.171 -3.819 11.682 94.036 16.129 -2.901 -3.159 4.412 4.800 14.069 4.503 -15.473 0.649 -6.808 2.603 -5.679 -2.417 0.000 0.000 0.000 5.429 -21.664 -2.853 -4.721 11.012 0.455 1.771 13.049 1.141 0.000 0.000 0.000 -0.000 0.000 -0.000 5.983 -5.218 -0.682 0.000 -0.000 -0.000 -3.421 1.820 -12.650 -6.161 4.614 19.007 8.470 6.105 1.868 0.000 -0.000 -0.000 3.151 5.087 4.192 -3.617 -1.668 -17.187 4.436 1.066 0.929 2.565 4.202 -3.628 2.565 4.202 -3.628 12.303 93.983 17.183 -2.982 -3.185 3.935 4.816 14.292 4.581 -15.991 1.655 -6.126 2.232 -5.547 -2.878 0.000 0.000 0.000 6.090 -20.814 -2.306 -5.029 10.935 1.000 1.432 12.466 0.616 0.000 0.000 0.000 0.000 -0.000 0.000 6.324 -5.133 -0.678 0.000 -0.000 -0.000 -3.652 1.773 -12.166 -6.582 4.755 19.007 9.163 5.764 1.970 0.000 -0.000 -0.000 3.128 4.980 4.760 -4.030 -1.292 -17.511 4.440 1.058 0.791 2.605 4.250 -3.393 2.605 4.250 -3.393 13.006 93.964 18.226 -3.067 -3.310 3.415 4.783 14.398 4.746 -16.448 3.030 -5.395 1.707 -5.215 -3.426 0.000 0.000 0.000 6.606 -19.838 -1.829 -5.211 10.846 1.582 0.880 11.605 0.210 0.000 0.000 0.000 -0.000 0.000 0.000 6.613 -4.981 -0.658 -0.000 -0.000 0.000 -3.884 1.797 -11.657 -6.931 4.878 18.993 9.917 5.488 2.009 -0.000 -0.000 0.000 3.095 4.878 5.355 -4.285 -0.923 -17.902 4.298 1.028 0.696 2.717 4.283 -3.133 2.717 4.283 -3.133 13.789 93.950 19.250 -3.097 -3.388 2.977 4.736 14.263 4.814 -17.039 4.666 -4.492 1.139 -4.568 -4.029 0.000 0.000 0.000 6.750 -18.755 -1.498 -5.064 10.638 2.020 0.506 10.826 -0.144 0.000 0.000 0.000 0.000 0.000 -0.000 6.881 -4.768 -0.667 -0.000 -0.000 0.000 -4.155 1.787 -11.427 -7.299 4.919 19.040 10.638 5.146 2.061 -0.000 -0.000 0.000 3.039 4.686 5.753 -4.597 -0.764 -18.058 4.166 1.137 0.657 2.822 4.291 -2.857 2.822 4.291 -2.857 14.806 93.930 20.277 -3.060 -3.558 2.706 4.580 13.864 4.773 -17.731 6.864 -3.312 0.564 -3.573 -4.692 0.000 0.000 0.000 6.643 -17.601 -1.230 -4.824 10.275 2.231 0.356 10.239 -0.425 0.000 0.000 0.000 -0.000 -0.000 0.000 6.871 -4.379 -0.700 -0.000 0.000 0.000 -4.189 1.714 -11.562 -7.724 5.012 19.117 11.344 4.735 2.152 -0.000 0.000 0.000 3.181 4.506 5.781 -4.824 -0.782 -18.070 3.967 1.086 0.695 3.050 4.248 -2.718 3.050 4.248 -2.718 15.911 93.922 21.355 -3.041 -3.643 2.570 4.423 13.129 4.842 -18.406 9.473 -2.057 -0.225 -2.054 -5.265 0.000 0.000 0.000 6.459 -16.660 -0.950 -4.477 10.143 2.187 0.518 9.645 -0.766 0.000 0.000 0.000 0.000 -0.000 -0.000 6.773 -4.045 -0.752 0.000 0.000 -0.000 -4.095 1.628 -12.004 -8.203 5.067 19.220 12.032 4.373 2.141 0.000 0.000 -0.000 3.365 4.258 5.559 -4.977 -0.936 -17.892 3.822 1.150 0.786 3.350 4.151 -2.603 3.350 4.151 -2.603 17.041 93.877 22.414 -2.933 -3.652 2.692 4.490 11.994 4.926 -19.538 12.645 -0.737 -1.028 -0.041 -5.812 0.000 0.000 0.000 6.003 -15.739 -0.738 -3.762 10.013 1.791 0.671 9.003 -0.920 0.000 0.000 0.000 -0.000 -0.000 0.000 6.678 -3.866 -0.942 -0.000 -0.000 -0.000 -4.205 1.558 -12.771 -8.556 5.188 19.315 12.641 3.871 2.060 -0.000 -0.000 -0.000 3.294 4.034 5.310 -4.850 -1.168 -17.748 3.710 1.287 0.912 3.554 4.076 -2.540 3.554 4.076 -2.540 18.130 93.757 23.437 -2.824 -3.661 2.814 4.642 10.621 5.282 -20.874 16.042 0.584 -1.959 2.745 -6.142 0.000 0.000 0.000 5.639 -14.794 -0.380 -3.089 9.774 1.298 0.874 8.521 -1.102 0.000 0.000 0.000 -0.000 -0.000 0.000 6.476 -3.630 -1.085 -0.000 -0.000 -0.000 -4.203 1.440 -13.594 -8.851 5.432 19.165 13.131 3.363 1.969 -0.000 -0.000 -0.000 3.336 3.754 5.011 -4.721 -1.398 -17.603 3.759 1.323 1.032 3.772 4.009 -2.520 3.772 4.009 -2.520 19.223 93.560 24.458 -2.640 -3.710 2.881 4.848 9.122 6.035 -22.456 19.848 1.638 -2.851 5.680 -6.154 0.000 0.000 0.000 5.213 -13.800 0.037 -2.486 9.504 0.914 1.432 7.992 -1.405 0.000 0.000 0.000 -0.000 -0.000 0.000 6.240 -3.426 -1.145 -0.000 -0.000 -0.000 -4.155 1.194 -14.319 -9.115 5.917 18.746 13.384 2.784 1.895 -0.000 -0.000 -0.000 3.344 3.552 4.680 -4.586 -1.723 -17.341 3.778 1.440 1.028 3.948 3.951 -2.491 3.948 3.951 -2.491 20.325 93.283 25.462 -2.532 -3.719 3.003 5.190 7.483 7.198 -24.094 23.916 2.137 -3.608 8.455 -5.699 0.000 0.000 0.000 4.828 -12.939 0.343 -1.865 9.232 0.570 1.847 7.602 -1.695 0.000 0.000 0.000 0.000 -0.000 -0.000 6.186 -3.325 -1.154 -0.000 -0.000 0.000 -4.170 0.985 -14.990 -9.335 6.429 18.249 13.402 2.145 1.769 -0.000 -0.000 0.000 3.232 3.430 4.440 -4.521 -2.025 -17.216 3.805 1.505 1.008 4.072 3.913 -2.514 4.072 3.913 -2.514 21.037 93.129 26.450 -2.418 -3.629 3.166 5.518 5.652 8.666 -25.613 28.166 2.267 -3.803 10.511 -4.838 0.000 0.000 0.000 4.486 -12.179 0.554 -1.318 8.950 0.313 2.115 7.053 -1.945 0.000 0.000 0.000 -0.000 -0.000 0.000 6.104 -3.317 -1.254 -0.000 -0.000 -0.000 -4.186 0.773 -15.443 -9.249 6.787 17.767 13.107 1.564 1.653 -0.000 -0.000 -0.000 3.146 3.386 4.324 -4.479 -2.404 -17.162 3.772 1.526 0.974 4.089 3.880 -2.503 4.089 3.880 -2.503 20.928 93.380 27.433 -2.264 -3.457 3.284 5.622 3.662 10.405 -26.857 32.484 2.245 -3.131 11.508 -3.629 0.000 0.000 0.000 4.222 -11.520 0.701 -0.980 8.664 0.200 2.300 6.522 -2.100 0.000 0.000 0.000 -0.000 -0.000 0.000 5.997 -3.392 -1.237 -0.000 -0.000 -0.000 -4.185 0.516 -15.773 -9.005 7.104 17.400 12.518 0.962 1.631 -0.000 -0.000 -0.000 2.901 3.326 4.219 -4.312 -2.779 -17.028 3.788 1.518 0.942 4.065 3.824 -2.550 4.065 3.824 -2.550 21.002 93.614 28.371 -2.128 -3.249 3.274 5.591 1.420 12.059 -27.853 36.589 2.582 -1.823 11.857 -2.118 0.000 0.000 0.000 3.859 -10.884 0.898 -0.596 8.282 0.011 2.505 6.079 -2.183 0.000 0.000 0.000 0.000 -0.000 0.000 5.913 -3.490 -1.091 -0.000 0.000 0.000 -4.218 0.235 -15.911 -8.606 7.344 17.223 11.642 0.359 1.705 -0.000 0.000 0.000 2.759 3.215 4.333 -4.173 -2.909 -17.033 3.762 1.230 0.921 4.009 3.798 -2.565 4.009 3.798 -2.565 21.021 93.814 29.287 -2.032 -3.122 3.309 5.552 -0.941 13.426 -28.685 40.378 3.424 0.103 11.497 -0.295 0.000 0.000 0.000 3.717 -10.258 0.999 -0.430 8.064 -0.216 2.718 5.562 -2.131 0.000 0.000 0.000 -0.000 -0.000 0.000 5.854 -3.505 -1.063 -0.000 -0.000 -0.000 -4.185 -0.082 -15.841 -8.058 7.512 17.160 10.497 -0.201 1.971 -0.000 -0.000 -0.000 2.557 3.114 4.558 -3.987 -3.068 -16.943 3.608 1.095 0.910 3.968 3.766 -2.495 3.968 3.766 -2.495 21.086 94.008 30.123 -1.860 -3.035 3.290 5.450 -3.511 14.588 -29.286 43.810 4.877 2.210 10.981 1.385 0.000 0.000 0.000 3.360 -9.660 1.019 -0.126 7.844 -0.511 2.912 5.169 -1.965 0.000 0.000 0.000 0.000 -0.000 0.000 5.661 -3.507 -0.996 0.000 0.000 -0.000 -4.147 -0.416 -15.683 -7.355 7.557 17.250 9.000 -0.678 2.219 0.000 0.000 -0.000 2.461 2.983 4.870 -3.983 -3.023 -16.888 3.592 0.965 0.911 3.913 3.790 -2.443 3.913 3.790 -2.443 21.134 94.193 30.976 -1.744 -2.994 3.190 5.314 -6.117 15.630 -29.440 46.733 6.549 4.132 10.309 2.789 0.000 0.000 0.000 3.075 -9.015 1.118 0.172 7.627 -0.957 3.172 4.821 -1.584 0.000 0.000 0.000 -0.000 -0.000 0.000 5.498 -3.377 -0.885 -0.000 -0.000 -0.000 -4.054 -0.713 -15.451 -6.622 7.469 17.428 7.542 -1.195 2.497 -0.000 -0.000 -0.000 2.368 2.667 5.312 -3.971 -2.786 -16.899 3.573 0.860 1.003 3.832 3.775 -2.374 3.832 3.775 -2.374 21.104 94.397 31.881 -1.628 -2.954 3.090 5.090 -8.600 16.429 -28.858 49.062 7.981 5.669 9.170 3.526 0.000 0.000 0.000 2.842 -8.254 1.076 0.410 7.216 -1.275 3.613 4.607 -1.225 0.000 0.000 0.000 -0.000 -0.000 0.000 5.379 -3.140 -0.728 -0.000 -0.000 -0.000 -4.030 -1.146 -15.387 -5.972 7.407 17.660 6.110 -1.681 2.805 -0.000 -0.000 -0.000 2.383 2.262 5.645 -4.138 -2.438 -16.748 3.544 0.777 0.968 3.775 3.704 -2.321 3.775 3.704 -2.321 21.124 94.607 32.834 -1.396 -2.873 2.890 4.769 -11.104 17.145 -27.569 50.896 8.985 6.692 7.875 3.706 0.000 0.000 0.000 2.432 -7.462 1.069 0.713 6.743 -1.521 4.135 4.327 -0.905 0.000 0.000 0.000 -0.000 -0.000 0.000 5.157 -2.937 -0.551 -0.000 -0.000 -0.000 -3.959 -1.523 -15.306 -5.369 7.216 17.780 4.821 -1.966 3.085 -0.000 -0.000 -0.000 2.265 1.952 6.037 -4.171 -2.175 -16.711 3.527 0.767 0.946 3.683 3.611 -2.197 3.683 3.611 -2.197 21.152 94.792 33.782 -1.203 -2.874 2.736 4.386 -13.271 17.537 -25.616 52.113 9.347 7.377 6.309 3.330 0.000 0.000 0.000 2.058 -6.595 1.013 0.881 6.155 -1.719 4.940 4.139 -0.604 0.000 0.000 0.000 0.000 -0.000 -0.000 4.886 -2.680 -0.416 0.000 0.000 -0.000 -3.916 -1.821 -15.383 -4.766 7.168 17.834 3.838 -2.267 3.249 0.000 0.000 -0.000 2.311 1.646 6.360 -4.369 -1.925 -16.751 3.593 0.824 1.042 3.669 3.498 -2.115 3.669 3.498 -2.115 21.173 94.974 34.689 -0.970 -2.795 2.535 4.022 -15.224 17.812 -22.960 52.547 8.670 7.723 4.964 2.606 0.000 0.000 0.000 1.568 -5.686 0.796 1.195 5.393 -1.820 5.820 3.975 -0.078 0.000 0.000 0.000 -0.000 -0.000 -0.000 4.570 -2.498 -0.376 -0.000 -0.000 0.000 -3.917 -2.104 -15.461 -4.207 7.043 17.791 3.036 -2.349 3.277 -0.000 -0.000 0.000 2.311 1.413 6.753 -4.448 -1.791 -16.772 3.607 0.981 1.067 3.651 3.392 -1.957 3.651 3.392 -1.957 21.201 95.168 35.658 -0.738 -2.717 2.334 3.644 -17.030 17.872 -19.740 52.334 7.111 7.635 3.709 1.900 0.000 0.000 0.000 1.062 -4.734 0.449 1.515 4.594 -1.936 6.680 3.995 0.634 0.000 0.000 0.000 0.000 -0.000 -0.000 4.178 -2.345 -0.261 -0.000 -0.000 -0.000 -3.769 -2.268 -15.720 -3.818 6.901 17.648 2.306 -2.324 3.305 -0.000 -0.000 -0.000 2.462 1.244 7.049 -4.502 -1.697 -16.725 3.521 1.112 1.041 3.672 3.296 -1.840 3.672 3.296 -1.840 21.162 95.321 36.627 -0.602 -2.766 2.099 3.371 -18.412 17.720 -16.155 51.356 4.935 7.219 2.587 1.313 0.000 0.000 0.000 0.730 -3.660 0.067 1.770 3.802 -1.975 7.620 3.966 1.307 0.000 0.000 0.000 -0.000 -0.000 -0.000 3.962 -2.042 -0.201 -0.000 0.000 0.000 -3.693 -2.464 -15.904 -3.592 6.769 17.351 1.864 -2.215 3.171 -0.000 0.000 0.000 2.450 0.927 7.378 -4.423 -1.578 -16.649 3.462 1.180 1.073 3.619 3.166 -1.712 3.619 3.166 -1.712 21.140 95.449 37.543 -0.426 -2.736 1.818 3.143 -19.777 17.445 -12.590 49.914 2.477 6.453 1.437 1.049 0.000 0.000 0.000 0.351 -2.739 -0.321 2.040 3.090 -1.952 8.498 3.916 1.927 0.000 0.000 0.000 -0.000 -0.000 -0.000 3.739 -1.894 -0.058 -0.000 0.000 -0.000 -3.605 -2.514 -16.024 -3.382 6.568 16.965 1.361 -2.041 2.939 -0.000 0.000 -0.000 2.358 0.754 7.595 -4.349 -1.622 -16.538 3.498 1.203 1.170 3.550 3.072 -1.602 3.550 3.072 -1.602 21.115 95.547 38.412 -0.340 -2.732 1.542 3.043 -20.818 17.128 -9.166 47.851 -0.205 5.612 0.293 1.014 0.000 0.000 0.000 0.070 -1.861 -0.778 2.306 2.449 -1.863 9.243 3.908 2.582 0.000 0.000 0.000 -0.000 -0.000 0.000 3.624 -1.798 0.043 -0.000 0.000 -0.000 -3.537 -2.494 -16.107 -3.267 6.357 16.541 1.057 -1.773 2.688 -0.000 0.000 -0.000 2.272 0.762 7.745 -4.175 -1.906 -16.382 3.488 1.177 1.212 3.469 3.016 -1.481 3.469 3.016 -1.481 21.135 95.634 39.285 -0.164 -2.703 1.261 2.795 -21.759 16.707 -5.830 45.449 -2.822 4.487 -0.800 0.953 0.000 0.000 0.000 -0.307 -1.138 -1.145 2.552 2.098 -1.849 9.970 3.717 3.206 0.000 0.000 0.000 -0.000 -0.000 -0.000 3.495 -1.697 0.078 -0.000 -0.000 -0.000 -3.488 -2.530 -15.963 -3.183 6.171 15.942 0.778 -1.455 2.539 -0.000 -0.000 -0.000 2.064 0.756 7.861 -3.979 -2.249 -16.228 3.549 1.269 1.174 3.347 2.948 -1.320 3.347 2.948 -1.320 21.117 95.692 40.110 -0.095 -2.667 0.859 2.596 -22.524 16.456 -2.478 42.722 -5.636 2.918 -1.832 0.876 0.000 0.000 0.000 -0.579 -0.485 -1.255 2.929 1.663 -1.903 10.444 3.681 3.770 0.000 0.000 0.000 -0.000 -0.000 -0.000 3.497 -1.672 0.198 -0.000 0.000 -0.000 -3.458 -2.495 -15.783 -3.175 5.970 15.434 0.559 -1.131 2.399 -0.000 0.000 -0.000 1.894 0.781 7.926 -3.825 -2.586 -16.060 3.653 1.221 1.091 3.248 2.888 -1.178 3.248 2.888 -1.178 21.108 95.740 40.859 0.010 -2.753 0.448 2.387 -22.896 16.287 0.669 39.590 -8.559 1.076 -2.658 0.752 0.000 0.000 0.000 -0.876 0.236 -1.215 3.206 1.333 -1.986 11.008 3.552 4.270 0.000 0.000 0.000 -0.000 -0.000 0.000 3.516 -1.423 0.277 -0.000 -0.000 -0.000 -3.533 -2.541 -15.713 -3.300 5.813 15.123 0.608 -1.019 2.379 -0.000 -0.000 -0.000 1.684 0.676 7.848 -3.605 -2.808 -15.800 3.645 0.988 0.960 3.121 2.778 -1.010 3.121 2.778 -1.010 21.118 95.751 41.664 -0.020 -2.843 0.012 2.328 -23.065 16.097 3.421 36.294 -11.095 -0.895 -3.436 0.619 0.000 0.000 0.000 -1.051 0.885 -1.215 3.531 1.254 -1.773 11.306 3.129 4.543 0.000 0.000 0.000 -0.000 -0.000 -0.000 3.668 -1.169 0.372 -0.000 -0.000 -0.000 -3.563 -2.522 -15.558 -3.516 5.572 14.812 0.769 -0.854 2.349 -0.000 -0.000 -0.000 1.475 0.570 7.769 -3.404 -3.100 -15.723 3.588 0.888 0.919 2.995 2.668 -0.842 2.995 2.668 -0.842 21.206 95.765 42.504 -0.051 -2.932 -0.423 2.148 -23.243 15.743 5.946 32.939 -13.050 -2.933 -4.189 0.532 0.000 0.000 0.000 -1.099 1.608 -1.089 3.581 1.051 -1.475 11.378 2.681 4.489 0.000 0.000 0.000 0.000 -0.000 -0.000 3.766 -1.017 0.513 -0.000 0.000 0.000 -3.534 -2.486 -15.378 -3.844 5.479 14.556 1.148 -0.675 2.281 -0.000 0.000 0.000 1.319 0.563 7.640 -3.228 -3.309 -15.617 3.502 0.853 0.820 2.931 2.630 -0.671 2.931 2.630 -0.671 21.244 95.772 43.277 -0.141 -3.067 -0.937 2.014 -23.216 15.249 8.162 29.438 -14.208 -5.115 -4.925 0.542 0.000 0.000 0.000 -1.090 2.248 -0.811 3.692 0.986 -1.224 11.297 2.276 4.436 0.000 0.000 0.000 -0.000 -0.000 -0.000 3.920 -0.813 0.574 -0.000 0.000 -0.000 -3.550 -2.437 -15.198 -4.207 5.438 14.530 1.635 -0.508 2.080 -0.000 0.000 -0.000 1.237 0.601 7.645 -3.141 -3.414 -15.543 3.495 0.825 0.845 2.911 2.661 -0.478 2.911 2.661 -0.478 21.396 95.776 44.185 -0.215 -3.234 -1.328 1.828 -23.122 14.522 10.127 25.972 -14.641 -7.465 -5.538 0.670 0.000 0.000 0.000 -1.116 2.992 -0.593 3.703 0.988 -1.061 11.047 1.742 4.522 0.000 0.000 0.000 -0.000 -0.000 -0.000 4.030 -0.510 0.540 0.000 -0.000 -0.000 -3.503 -2.393 -14.968 -4.671 5.244 14.351 2.261 -0.216 2.020 0.000 -0.000 -0.000 1.310 0.571 7.720 -3.208 -3.365 -15.611 3.432 0.851 0.742 2.879 2.623 -0.270 2.879 2.623 -0.270 21.586 95.771 45.059 -0.350 -3.445 -1.798 1.667 -22.855 13.759 11.744 22.531 -14.220 -9.754 -6.032 0.739 0.000 0.000 0.000 -1.154 3.714 -0.287 3.762 1.052 -0.945 10.858 1.271 4.648 0.000 0.000 0.000 -0.000 -0.000 0.000 4.146 -0.258 0.625 -0.000 -0.000 0.000 -3.407 -2.243 -14.780 -5.211 5.119 14.253 3.033 0.124 1.900 -0.000 -0.000 0.000 1.473 0.494 7.759 -3.281 -2.996 -15.619 3.304 0.853 0.606 2.874 2.634 -0.090 2.874 2.634 -0.090 21.735 95.767 46.097 -0.427 -3.611 -2.189 1.488 -22.553 12.996 13.244 19.216 -13.248 -12.152 -6.349 0.760 0.000 0.000 0.000 -1.263 4.518 -0.132 3.887 1.098 -0.805 10.618 0.737 4.824 0.000 0.000 0.000 -0.000 0.000 -0.000 4.201 -0.057 0.638 -0.000 0.000 0.000 -3.354 -2.158 -14.677 -5.746 5.135 14.270 3.849 0.463 1.700 -0.000 0.000 0.000 1.695 0.436 7.943 -3.431 -2.534 -15.890 3.222 0.987 0.662 2.895 2.623 0.003 2.895 2.623 0.003 21.891 95.757 47.178 -0.505 -3.777 -2.581 1.383 -22.053 12.405 14.416 16.010 -11.968 -14.365 -6.625 0.800 0.000 0.000 0.000 -1.304 5.319 -0.044 3.838 1.209 -0.498 10.384 0.165 4.963 0.000 0.000 0.000 0.000 -0.000 -0.000 4.329 0.175 0.573 -0.000 0.000 -0.000 -3.384 -2.021 -14.562 -6.319 4.968 14.402 4.789 0.936 1.513 -0.000 0.000 -0.000 1.844 0.353 8.207 -3.666 -1.996 -16.032 3.191 1.158 0.700 2.865 2.623 0.164 2.865 2.623 0.164 22.108 95.733 48.306 -0.536 -3.997 -2.928 1.349 -21.426 12.055 15.566 12.928 -10.789 -16.496 -6.773 0.861 0.000 0.000 0.000 -1.465 6.232 -0.059 3.917 1.278 -0.076 9.845 -0.484 4.936 0.000 0.000 0.000 -0.000 -0.000 0.000 4.371 0.350 0.566 -0.000 -0.000 -0.000 -3.436 -1.825 -14.477 -6.766 4.859 14.568 5.620 1.545 1.324 -0.000 -0.000 -0.000 1.989 0.577 8.377 -3.843 -1.617 -16.233 3.194 1.528 0.862 2.871 2.710 0.187 2.871 2.710 0.187 22.261 95.668 49.544 -0.691 -4.117 -3.266 1.480 -20.850 11.858 16.513 10.238 -9.828 -18.291 -6.842 0.928 0.000 0.000 0.000 -1.378 7.061 -0.040 3.828 1.494 0.321 9.200 -1.318 4.923 0.000 0.000 0.000 -0.000 -0.000 0.000 4.538 0.430 0.547 -0.000 -0.000 -0.000 -3.468 -1.598 -14.268 -7.213 4.791 14.759 6.404 2.080 1.215 -0.000 -0.000 -0.000 2.060 0.760 8.564 -3.950 -1.166 -16.375 3.179 1.948 1.011 2.832 2.795 0.208 2.832 2.795 0.208 22.544 95.606 50.718 -0.785 -4.193 -3.524 1.543 -20.372 11.622 17.149 8.059 -9.070 -19.526 -6.772 0.809 0.000 0.000 0.000 -1.401 7.776 -0.085 3.708 1.753 0.788 8.500 -2.091 4.755 0.000 0.000 0.000 0.000 0.000 -0.000 4.722 0.490 0.530 -0.000 0.000 -0.000 -3.567 -1.485 -14.071 -7.672 4.705 15.054 7.192 2.691 1.063 -0.000 0.000 -0.000 2.106 0.846 8.758 -4.073 -0.604 -16.483 3.194 2.273 1.144 2.802 2.864 0.195 2.802 2.864 0.195 22.851 95.540 51.909 -0.880 -4.268 -3.783 1.579 -20.044 11.391 17.673 6.668 -8.787 -20.375 -6.603 0.661 0.000 0.000 0.000 -1.503 8.494 -0.055 3.658 2.002 1.194 7.904 -2.761 4.642 0.000 0.000 0.000 0.000 -0.000 -0.000 4.832 0.519 0.593 0.000 -0.000 -0.000 -3.544 -1.356 -13.800 -8.095 4.727 15.267 7.934 3.006 0.852 0.000 -0.000 -0.000 2.177 1.023 8.792 -4.071 -0.251 -16.457 3.068 2.709 1.267 2.823 2.886 0.137 2.823 2.886 0.137 23.175 95.439 53.120 -0.941 -4.311 -3.862 1.299 -19.956 10.967 18.202 6.049 -8.952 -20.807 -6.318 0.700 0.000 0.000 0.000 -1.545 9.191 -0.077 3.489 2.385 1.467 7.444 -3.649 4.501 0.000 0.000 0.000 -0.000 -0.000 0.000 4.912 0.499 0.481 -0.000 -0.000 0.000 -3.522 -1.227 -13.530 -8.603 4.750 15.411 8.776 3.200 0.707 -0.000 -0.000 0.000 2.297 1.138 8.905 -4.190 0.215 -16.449 3.015 3.035 1.409 2.843 2.962 0.139 2.843 2.962 0.139 23.368 95.332 54.359 -1.049 -4.297 -3.987 1.014 -20.111 10.423 18.523 6.107 -9.189 -21.018 -5.836 0.790 0.000 0.000 0.000 -1.479 9.776 0.006 3.261 2.828 1.506 7.090 -4.423 4.580 0.000 0.000 0.000 -0.000 -0.000 0.000 5.083 0.355 0.594 -0.000 -0.000 0.000 -3.616 -1.102 -13.326 -9.065 4.969 15.493 9.631 3.191 0.569 -0.000 -0.000 0.000 2.381 1.322 8.837 -4.309 0.681 -16.442 2.997 3.273 1.494 2.893 3.072 0.050 2.893 3.072 0.050 23.674 95.198 55.675 -1.110 -4.340 -4.066 0.619 -20.020 9.844 18.672 6.336 -9.307 -21.007 -5.154 0.943 0.000 0.000 0.000 -1.524 10.405 -0.078 2.956 3.411 1.764 6.904 -5.319 4.672 0.000 0.000 0.000 -0.000 -0.000 -0.000 5.179 0.330 0.688 -0.000 0.000 0.000 -3.754 -1.016 -13.149 -9.376 5.193 15.481 10.480 3.035 0.594 -0.000 0.000 0.000 2.489 1.433 8.742 -4.429 1.147 -16.435 3.021 3.462 1.670 2.945 3.169 -0.023 2.945 3.169 -0.023 23.999 95.042 57.111 -1.110 -4.340 -4.066 0.212 -19.896 9.266 18.635 6.693 -9.283 -20.804 -4.135 1.360 0.000 0.000 0.000 -1.676 11.049 -0.300 2.748 4.041 2.203 6.676 -6.262 4.571 0.000 0.000 0.000 -0.000 -0.000 -0.000 5.243 0.182 0.684 -0.000 0.000 -0.000 -3.808 -0.824 -12.860 -9.764 5.363 15.509 11.253 2.918 0.536 -0.000 0.000 -0.000 2.557 1.648 8.864 -4.572 1.512 -16.662 3.053 3.745 1.883 3.006 3.274 -0.058 3.006 3.274 -0.058 24.351 94.900 58.480 -1.110 -4.340 -4.066 -0.130 -19.665 8.987 18.458 6.868 -8.970 -20.360 -2.538 1.533 0.000 0.000 0.000 -1.748 11.622 -0.660 2.287 4.691 2.763 6.617 -6.995 4.577 0.000 0.000 0.000 -0.000 -0.000 -0.000 5.233 0.001 0.760 0.000 0.000 -0.000 -3.845 -0.650 -12.577 -10.107 5.599 15.511 12.163 2.710 0.470 0.000 0.000 -0.000 2.629 1.846 8.925 -4.712 1.854 -16.728 3.154 4.094 1.919 3.163 3.448 -0.130 3.163 3.448 -0.130 24.688 94.767 59.900 -1.110 -4.340 -4.066 -0.574 -19.225 9.001 18.248 6.905 -8.558 -19.731 -0.688 1.430 0.000 0.000 0.000 -1.752 12.137 -0.959 1.726 5.474 3.272 6.553 -7.586 4.447 0.000 0.000 0.000 -0.000 -0.000 -0.000 5.339 -0.224 0.935 -0.000 -0.000 -0.000 -4.013 -0.462 -12.352 -10.437 5.883 15.485 12.977 2.548 0.578 -0.000 -0.000 -0.000 2.713 2.066 8.944 -4.936 2.151 -16.880 3.157 4.439 2.105 3.266 3.580 -0.202 3.266 3.580 -0.202 25.123 94.601 61.411 -1.122 -4.252 -3.931 -1.024 -18.576 9.187 17.941 6.708 -8.435 -19.206 1.005 1.195 0.000 0.000 0.000 -1.763 12.496 -1.385 1.052 6.518 3.694 6.809 -8.184 4.535 0.000 0.000 0.000 -0.000 -0.000 -0.000 5.462 -0.547 0.983 -0.000 -0.000 -0.000 -4.235 -0.329 -12.054 -10.710 6.221 15.559 13.721 2.424 0.571 -0.000 -0.000 -0.000 2.741 2.210 8.791 -5.168 2.505 -16.867 3.265 4.713 2.253 3.336 3.800 -0.297 3.336 3.800 -0.297 25.520 94.468 62.942 -1.135 -4.164 -3.796 -1.314 -17.832 9.570 17.531 6.453 -8.702 -18.809 2.581 1.112 0.000 0.000 0.000 -1.643 12.737 -1.689 0.158 7.734 3.919 7.174 -8.424 4.684 0.000 0.000 0.000 0.000 -0.000 0.000 5.577 -1.051 1.109 -0.000 0.000 -0.000 -4.501 -0.115 -11.866 -10.934 6.480 15.832 14.430 2.479 0.472 -0.000 0.000 -0.000 2.736 2.593 8.472 -5.332 2.596 -16.686 3.421 5.134 2.346 3.395 4.075 -0.412 3.395 4.075 -0.412 26.101 94.392 64.492 -1.041 -4.089 -3.537 -1.660 -17.229 9.502 16.870 6.540 -8.814 -18.189 3.749 1.175 0.000 0.000 0.000 -1.741 12.855 -2.087 -0.802 9.113 4.193 7.862 -8.132 4.949 0.000 0.000 0.000 -0.000 -0.000 -0.000 5.483 -1.520 1.225 -0.000 0.000 -0.000 -4.652 0.103 -11.823 -11.169 6.692 16.135 15.120 2.647 0.349 -0.000 0.000 -0.000 2.824 2.899 8.010 -5.433 2.555 -16.640 3.546 5.529 2.487 3.567 4.326 -0.638 3.567 4.326 -0.638 26.739 94.326 66.114 -0.929 -4.050 -3.157 -1.885 -16.579 8.676 15.933 6.752 -8.425 -17.648 4.573 1.385 0.000 0.000 0.000 -1.907 12.889 -2.457 -1.733 10.739 4.329 8.576 -7.394 5.402 0.000 0.000 0.000 0.000 -0.000 0.000 5.289 -1.999 1.143 -0.000 -0.000 -0.000 -4.810 0.342 -11.660 -11.155 6.948 16.379 15.521 2.825 0.321 -0.000 -0.000 -0.000 2.850 3.238 7.724 -5.362 2.418 -16.721 3.680 5.732 2.605 3.774 4.595 -0.831 3.774 4.595 -0.831 27.447 94.246 67.778 -0.878 -4.053 -2.855 -2.016 -15.971 7.583 14.836 6.950 -7.922 -17.119 5.038 1.912 0.000 0.000 0.000 -2.011 12.690 -2.796 -2.860 12.820 4.577 9.246 -6.237 5.955 0.000 0.000 0.000 0.000 -0.000 0.000 5.136 -2.416 1.075 -0.000 0.000 -0.000 -4.867 0.574 -11.484 -11.146 7.196 16.572 15.915 2.969 0.336 -0.000 0.000 -0.000 2.953 3.530 7.408 -5.380 2.108 -16.712 3.860 6.014 2.738 3.987 4.861 -0.996 3.987 4.861 -0.996 28.380 94.130 69.473 -0.827 -4.055 -2.553 -2.077 -15.125 6.370 13.683 6.902 -7.489 -16.719 5.169 2.613 0.000 0.000 0.000 -2.386 12.224 -3.286 -3.784 15.321 5.006 9.507 -4.599 6.549 0.000 0.000 0.000 0.000 0.000 -0.000 4.996 -2.840 1.062 -0.000 0.000 -0.000 -4.883 0.875 -11.437 -11.178 7.277 16.822 16.118 3.050 0.289 -0.000 0.000 -0.000 2.960 3.700 6.995 -5.385 1.679 -16.537 4.137 6.263 2.702 4.197 5.127 -1.193 4.197 5.127 -1.193 29.322 93.985 71.165 -0.896 -4.145 -2.409 -1.992 -14.002 5.341 12.537 6.541 -7.044 -16.317 4.955 3.280 0.000 0.000 0.000 -2.730 11.568 -3.796 -4.910 18.177 5.729 9.498 -2.354 6.983 0.000 0.000 0.000 -0.000 -0.000 0.000 5.033 -3.120 1.055 -0.000 -0.000 -0.000 -5.035 1.245 -11.310 -11.037 7.283 16.992 16.259 3.135 0.256 -0.000 -0.000 -0.000 2.900 3.841 6.720 -5.387 1.251 -16.363 4.257 6.129 2.696 4.336 5.354 -1.348 4.336 5.354 -1.348 30.266 93.772 72.850 -1.013 -4.179 -2.311 -1.830 -12.729 4.796 11.513 5.775 -6.945 -15.819 4.806 3.972 0.000 0.000 0.000 -3.094 10.518 -4.510 -6.275 21.468 6.896 9.320 0.478 7.241 0.000 0.000 0.000 -0.000 -0.000 0.000 5.155 -3.531 0.971 -0.000 0.000 -0.000 -5.100 1.506 -11.122 -10.913 7.540 17.108 16.137 3.063 0.232 -0.000 0.000 -0.000 2.727 4.029 6.592 -5.294 0.723 -16.162 4.414 5.980 2.668 4.462 5.570 -1.453 4.462 5.570 -1.453 31.229 93.477 74.489 -1.135 -4.079 -2.300 -1.581 -11.613 4.538 10.495 4.933 -6.742 -15.144 4.950 4.279 0.000 0.000 0.000 -3.605 9.125 -5.596 -8.020 24.934 8.739 9.420 3.419 7.271 0.000 0.000 0.000 -0.000 -0.000 0.000 5.372 -4.036 1.061 -0.000 -0.000 0.000 -5.253 1.829 -11.071 -10.680 7.652 17.153 15.856 3.069 0.165 -0.000 -0.000 0.000 2.601 4.159 6.450 -5.403 0.106 -16.030 4.499 5.681 2.538 4.485 5.768 -1.588 4.485 5.768 -1.588 31.881 93.461 75.888 -1.332 -3.935 -2.234 -1.332 -10.488 4.234 9.597 4.051 -6.112 -14.231 5.100 4.131 0.000 0.000 0.000 -3.779 7.619 -7.116 -10.438 28.353 11.309 9.926 5.535 7.105 0.000 0.000 0.000 0.000 -0.000 -0.000 5.543 -4.540 0.992 -0.000 -0.000 0.000 -5.210 2.100 -10.974 -10.455 7.755 17.145 15.469 2.917 0.134 -0.000 -0.000 0.000 2.559 4.139 6.509 -5.562 -0.531 -15.997 4.623 5.324 2.333 4.628 5.945 -1.677 4.628 5.945 -1.677 32.272 93.748 76.946 -1.411 -3.756 -2.266 -1.211 -9.548 4.034 8.770 3.303 -5.375 -13.220 5.228 3.815 0.000 0.000 0.000 -3.854 5.994 -8.692 -13.269 31.448 14.359 10.115 6.467 6.704 0.000 0.000 0.000 0.000 -0.000 -0.000 5.663 -4.971 1.140 0.000 0.000 -0.000 -5.190 2.306 -11.179 -10.200 7.814 17.228 14.958 2.724 0.111 0.000 0.000 -0.000 2.455 3.982 6.434 -5.619 -1.217 -16.058 4.607 4.891 2.188 4.735 6.008 -1.811 4.735 6.008 -1.811 32.626 93.981 77.923 -1.432 -3.534 -2.218 -1.155 -8.773 3.668 8.037 2.672 -4.521 -12.428 5.303 3.475 0.000 0.000 0.000 -3.762 4.124 -10.221 -16.241 34.302 17.373 9.682 6.330 6.330 0.000 0.000 0.000 -0.000 0.000 -0.000 5.658 -5.306 1.217 -0.000 -0.000 0.000 -5.085 2.265 -11.499 -9.849 7.988 17.236 14.132 2.490 0.180 -0.000 -0.000 0.000 2.455 3.557 6.409 -5.666 -1.993 -16.146 4.532 4.341 1.828 4.829 5.998 -1.938 4.829 5.998 -1.938 33.057 94.198 78.872 -1.404 -3.368 -2.127 -1.147 -7.944 3.262 7.208 2.004 -3.918 -11.649 5.245 3.366 0.000 0.000 0.000 -3.459 2.090 -11.733 -19.488 36.749 20.380 8.897 5.618 5.814 0.000 0.000 0.000 -0.000 -0.000 0.000 5.488 -5.541 1.294 -0.000 -0.000 0.000 -4.762 2.083 -12.021 -9.567 8.230 17.299 13.272 2.050 0.207 -0.000 -0.000 0.000 2.567 3.076 6.330 -5.669 -2.724 -16.268 4.445 3.650 1.454 5.000 5.928 -2.059 5.000 5.928 -2.059 33.513 94.389 79.777 -1.419 -3.280 -1.992 -1.164 -7.103 2.742 6.522 1.402 -3.372 -11.088 5.104 3.391 0.000 0.000 0.000 -3.032 0.063 -13.072 -22.573 38.718 23.101 7.963 4.459 5.127 0.000 0.000 0.000 -0.000 -0.000 0.000 5.330 -5.631 1.345 -0.000 0.000 -0.000 -4.409 1.743 -12.515 -9.313 8.604 17.126 12.386 1.533 0.259 -0.000 0.000 -0.000 2.698 2.525 6.222 -5.557 -3.405 -16.406 4.303 2.919 1.123 5.111 5.766 -2.128 5.111 5.766 -2.128 33.978 94.584 80.654 -1.537 -3.316 -1.893 -1.069 -6.137 2.256 5.826 0.782 -3.004 -10.567 4.809 3.516 0.000 0.000 0.000 -2.441 -2.050 -14.099 -25.531 40.310 25.427 7.014 3.061 4.241 0.000 0.000 0.000 0.000 0.000 -0.000 5.342 -5.564 1.339 -0.000 0.000 -0.000 -4.094 1.302 -13.057 -9.065 9.103 17.017 11.425 0.849 0.363 -0.000 0.000 -0.000 2.767 2.034 6.260 -5.553 -4.126 -16.560 4.203 2.259 0.794 5.215 5.620 -2.130 5.215 5.620 -2.130 34.393 94.754 81.550 -1.531 -3.450 -1.805 -1.028 -5.059 1.729 5.152 0.214 -2.677 -10.125 4.426 3.718 0.000 0.000 0.000 -1.960 -4.211 -14.894 -28.100 41.444 27.388 6.171 1.507 3.115 0.000 0.000 0.000 -0.000 -0.000 0.000 5.213 -5.387 1.286 -0.000 -0.000 -0.000 -3.774 0.722 -13.441 -8.836 9.824 16.821 10.471 -0.048 0.507 -0.000 -0.000 -0.000 2.778 1.545 6.406 -5.502 -4.878 -16.624 4.105 1.830 0.451 5.264 5.417 -2.100 5.264 5.417 -2.100 34.744 94.899 82.426 -1.574 -3.529 -1.762 -1.052 -4.121 1.238 4.782 -0.278 -2.224 -9.747 4.012 3.762 0.000 0.000 0.000 -1.286 -6.430 -15.351 -30.117 42.125 28.788 5.390 -0.107 1.895 0.000 0.000 0.000 0.000 -0.000 0.000 5.177 -5.341 1.307 -0.000 0.000 -0.000 -3.505 0.232 -13.685 -8.565 10.525 16.641 9.519 -0.956 0.591 -0.000 0.000 -0.000 2.769 1.221 6.587 -5.398 -5.532 -16.676 3.987 1.470 0.317 5.278 5.337 -2.058 5.278 5.337 -2.058 35.083 95.032 83.266 -1.691 -3.565 -1.662 -0.972 -3.294 0.750 4.315 -0.707 -1.764 -9.245 3.713 3.688 0.000 0.000 0.000 -0.478 -8.695 -15.534 -31.524 42.300 29.575 4.740 -1.646 0.731 0.000 0.000 0.000 -0.000 -0.000 0.000 5.330 -5.390 1.378 -0.000 0.000 -0.000 -3.393 -0.138 -13.892 -8.036 11.112 16.412 8.404 -1.861 0.729 -0.000 0.000 -0.000 2.589 1.037 6.783 -5.234 -6.257 -16.741 3.845 1.294 0.206 5.206 5.249 -2.096 5.206 5.249 -2.096 35.420 95.150 84.146 -1.765 -3.521 -1.607 -0.917 -2.499 0.440 3.841 -1.202 -1.441 -8.750 3.443 3.714 0.000 0.000 0.000 0.211 -11.004 -15.309 -31.982 42.172 29.636 4.173 -2.960 -0.318 0.000 0.000 0.000 -0.000 -0.000 0.000 5.479 -5.405 1.399 -0.000 -0.000 -0.000 -3.317 -0.624 -13.998 -7.499 11.678 16.327 7.182 -2.620 0.884 -0.000 -0.000 -0.000 2.324 0.815 7.013 -5.051 -6.891 -16.560 3.940 1.072 0.034 5.075 5.144 -2.040 5.075 5.144 -2.040 35.800 95.263 85.025 -1.823 -3.514 -1.428 -0.857 -1.739 0.073 3.258 -1.551 -1.276 -8.207 2.950 3.744 0.000 0.000 0.000 0.881 -13.108 -14.785 -31.598 41.594 28.992 3.786 -4.002 -1.135 0.000 0.000 0.000 0.000 -0.000 0.000 5.506 -5.357 1.399 -0.000 -0.000 -0.000 -3.311 -1.025 -14.229 -6.767 12.060 16.389 5.957 -3.280 0.954 -0.000 -0.000 -0.000 2.224 0.585 7.110 -5.017 -7.522 -16.305 4.043 1.013 -0.031 5.020 5.042 -2.064 5.020 5.042 -2.064 36.185 95.382 85.940 -1.956 -3.463 -1.194 -0.690 -1.042 -0.159 2.643 -1.814 -1.319 -7.800 2.327 3.809 0.000 0.000 0.000 1.690 -15.108 -13.977 -30.569 40.655 27.774 3.614 -4.627 -1.591 0.000 0.000 0.000 -0.000 -0.000 0.000 5.603 -5.356 1.343 -0.000 0.000 -0.000 -3.308 -1.426 -14.460 -6.017 12.285 16.419 4.650 -3.808 1.029 -0.000 0.000 -0.000 2.072 0.375 7.099 -4.827 -8.062 -15.930 4.196 0.894 0.006 4.959 4.964 -2.061 4.959 4.964 -2.061 36.627 95.481 86.846 -2.040 -3.469 -0.916 -0.615 -0.300 -0.347 2.071 -2.070 -1.458 -7.486 1.626 3.961 0.000 0.000 0.000 2.416 -16.808 -12.862 -28.769 39.316 26.072 3.818 -4.864 -1.750 0.000 0.000 0.000 0.000 0.000 -0.000 5.646 -5.305 1.242 -0.000 -0.000 -0.000 -3.236 -1.739 -14.801 -5.243 12.341 16.422 3.149 -4.155 1.182 -0.000 -0.000 -0.000 1.941 0.269 6.988 -4.609 -8.622 -15.422 4.336 0.750 -0.064 4.886 4.947 -2.054 4.886 4.947 -2.054 37.013 95.581 87.726 -2.166 -3.554 -0.595 -0.423 0.508 -0.470 1.434 -2.313 -1.556 -7.215 0.813 3.884 0.000 0.000 0.000 3.116 -18.144 -11.611 -26.439 37.517 24.127 4.298 -4.782 -1.673 0.000 0.000 0.000 -0.000 -0.000 0.000 5.595 -5.058 1.163 -0.000 -0.000 0.000 -3.141 -2.073 -15.101 -4.312 12.254 16.278 1.559 -4.422 1.293 -0.000 -0.000 0.000 1.889 0.104 6.715 -4.281 -9.202 -15.012 4.381 0.767 -0.112 4.941 4.864 -2.140 4.941 4.864 -2.140 37.369 95.668 88.649 -2.275 -3.677 -0.151 -0.201 1.385 -0.371 0.751 -2.592 -1.848 -6.953 0.020 3.645 0.000 0.000 0.000 3.757 -19.213 -10.412 -23.821 35.333 22.127 4.964 -4.342 -1.550 0.000 0.000 0.000 -0.000 0.000 -0.000 5.526 -4.785 1.110 0.000 -0.000 -0.000 -3.048 -2.291 -15.809 -3.415 11.979 16.209 -0.031 -4.424 1.500 0.000 -0.000 -0.000 1.923 0.028 6.143 -4.069 -9.642 -14.617 4.476 0.633 -0.135 4.982 4.801 -2.329 4.982 4.801 -2.329 37.746 95.753 89.756 -2.449 -3.894 0.436 0.097 2.482 -0.333 0.070 -2.905 -2.239 -6.793 -0.809 3.395 0.000 0.000 0.000 4.302 -19.934 -9.410 -21.093 32.745 20.291 5.784 -3.601 -1.448 0.000 0.000 0.000 -0.000 -0.000 -0.000 5.550 -4.514 0.932 0.000 -0.000 -0.000 -3.026 -2.358 -16.411 -2.517 11.643 16.107 -1.607 -4.367 1.544 0.000 -0.000 -0.000 1.923 0.033 5.543 -3.802 -10.024 -14.392 4.490 0.562 -0.133 5.007 4.776 -2.537 5.007 4.776 -2.537 38.083 95.813 90.894 -2.571 -4.167 1.063 0.508 3.608 -0.104 -0.780 -3.189 -2.887 -6.589 -1.532 3.112 0.000 0.000 0.000 4.748 -20.258 -8.481 -18.360 29.735 18.280 6.638 -2.704 -1.199 0.000 0.000 0.000 -0.000 -0.000 0.000 5.526 -4.191 0.711 -0.000 0.000 -0.000 -2.956 -2.361 -16.930 -1.717 11.234 15.865 -3.062 -4.171 1.643 -0.000 0.000 -0.000 1.944 0.171 5.038 -3.625 -10.242 -14.361 4.467 0.515 -0.144 5.056 4.781 -2.773 5.056 4.781 -2.773 38.462 95.839 92.021 -2.655 -4.563 1.679 0.847 4.851 0.220 -1.746 -3.520 -3.642 -6.144 -2.192 2.929 0.000 0.000 0.000 5.031 -20.393 -7.576 -15.699 26.632 16.203 7.435 -1.554 -0.974 0.000 0.000 0.000 -0.000 -0.000 0.000 5.475 -3.744 0.493 -0.000 0.000 -0.000 -2.948 -2.331 -17.441 -0.761 10.725 15.688 -4.578 -3.591 1.758 -0.000 0.000 -0.000 1.919 0.331 4.425 -3.429 -10.283 -14.238 4.527 0.447 -0.152 5.054 4.847 -3.003 5.054 4.847 -3.003 38.790 95.859 93.092 -2.849 -5.001 2.393 1.387 6.105 0.528 -2.699 -3.805 -4.438 -5.840 -2.698 2.639 0.000 0.000 0.000 5.270 -20.394 -6.807 -13.144 23.415 13.789 8.228 -0.119 -0.536 0.000 0.000 0.000 -0.000 -0.000 0.000 5.520 -3.450 0.237 0.000 -0.000 0.000 -2.859 -2.151 -18.023 0.146 10.144 15.667 -6.230 -2.507 1.792 0.000 -0.000 0.000 2.059 0.717 3.857 -3.376 -10.175 -14.316 4.579 0.477 -0.092 5.064 4.944 -3.340 5.064 4.944 -3.340 39.078 95.859 94.293 -2.980 -5.398 3.189 1.890 7.393 0.708 -3.567 -4.078 -5.127 -5.573 -3.270 2.309 0.000 0.000 0.000 5.332 -20.422 -6.210 -10.874 20.312 11.429 9.056 1.278 -0.222 0.000 0.000 0.000 0.000 -0.000 0.000 5.658 -3.150 -0.094 0.000 0.000 -0.000 -2.814 -1.991 -18.365 1.023 9.391 15.749 -7.788 -0.867 1.652 0.000 0.000 -0.000 2.032 0.965 3.236 -3.378 -9.817 -14.313 4.532 0.600 -0.054 4.947 5.075 -3.666 4.947 5.075 -3.666 39.389 95.800 95.593 -2.956 -5.721 4.064 2.399 8.690 0.804 -4.718 -4.398 -5.694 -5.179 -3.701 1.837 0.000 0.000 0.000 5.279 -20.517 -5.732 -8.943 17.383 8.893 9.863 2.744 -0.000 0.000 0.000 0.000 -0.000 0.000 -0.000 5.523 -3.057 -0.452 -0.000 -0.000 -0.000 -2.675 -1.715 -18.546 2.118 8.664 15.775 -9.640 1.233 1.587 -0.000 -0.000 -0.000 2.202 1.332 2.523 -3.493 -9.232 -14.279 4.605 0.758 0.072 4.926 5.244 -4.050 4.926 5.244 -4.050 39.677 95.717 96.951 -2.980 -5.992 4.899 2.957 9.992 0.857 -5.781 -4.773 -6.134 -4.860 -3.994 1.208 0.000 0.000 0.000 5.322 -20.745 -5.334 -7.356 14.784 6.209 10.498 4.330 0.326 0.000 0.000 0.000 -0.000 -0.000 0.000 5.439 -3.014 -0.770 -0.000 0.000 -0.000 -2.447 -1.536 -18.708 3.112 7.989 15.952 -11.524 3.729 1.341 -0.000 0.000 -0.000 2.390 1.717 1.645 -3.606 -8.517 -14.270 4.654 0.991 0.291 4.925 5.383 -4.407 4.925 5.383 -4.407 40.023 95.586 98.383 -2.889 -6.269 5.859 3.383 11.363 0.813 -6.787 -5.190 -6.623 -4.406 -4.216 0.656 0.000 0.000 0.000 5.151 -20.878 -5.348 -6.126 12.291 3.654 11.172 5.989 0.549 0.000 0.000 0.000 -0.000 -0.000 -0.000 5.256 -3.034 -1.234 -0.000 0.000 -0.000 -2.271 -1.540 -18.941 3.868 7.557 16.111 -13.266 6.117 1.233 -0.000 0.000 -0.000 2.538 2.039 0.706 -3.686 -7.427 -14.204 4.644 1.172 0.403 4.858 5.568 -4.804 4.858 5.568 -4.804 40.480 95.420 99.885 -2.793 -6.545 6.819 3.771 12.666 0.701 -7.787 -5.357 -7.135 -3.815 -4.516 0.142 0.000 0.000 0.000 4.805 -20.918 -5.598 -4.978 10.126 1.464 11.578 7.440 0.627 0.000 0.000 0.000 -0.000 -0.000 -0.000 5.055 -2.980 -1.663 -0.000 0.000 -0.000 -2.132 -1.678 -19.296 4.604 7.457 16.028 -14.871 8.002 1.092 -0.000 0.000 -0.000 2.787 2.318 -0.290 -3.793 -6.261 -14.223 4.693 1.578 0.632 4.892 5.677 -5.193 4.892 5.677 -5.193 40.912 95.246 101.245 -2.747 -6.769 7.741 4.234 13.712 0.596 -8.788 -5.308 -7.620 -3.125 -4.723 -0.339 0.000 0.000 0.000 4.487 -20.833 -6.034 -4.098 8.083 -0.296 11.914 8.714 0.807 0.000 0.000 0.000 0.000 -0.000 0.000 4.918 -3.045 -2.090 0.000 -0.000 -0.000 -2.116 -1.960 -19.713 5.316 7.920 15.871 -16.337 9.233 0.795 0.000 -0.000 -0.000 3.048 2.745 -1.189 -3.954 -5.083 -14.430 4.742 2.256 0.887 4.914 5.824 -5.569 4.914 5.824 -5.569 41.466 95.049 102.638 -2.721 -6.954 8.532 4.560 14.662 0.441 -9.602 -5.057 -7.886 -2.440 -5.072 -0.729 0.000 0.000 0.000 4.186 -20.794 -6.538 -3.369 6.381 -1.361 12.251 9.673 0.756 0.000 0.000 0.000 -0.000 0.000 0.000 4.890 -3.130 -2.394 -0.000 0.000 -0.000 -2.183 -2.441 -20.143 5.859 8.633 15.480 -17.526 9.765 0.442 -0.000 0.000 -0.000 3.228 3.156 -2.076 -4.230 -3.851 -14.880 4.981 2.828 1.136 4.910 5.931 -5.912 4.910 5.931 -5.912 42.153 94.807 104.021 -2.615 -7.177 9.274 4.754 15.602 0.284 -10.417 -4.656 -7.998 -1.813 -5.449 -1.258 0.000 0.000 0.000 3.878 -20.743 -7.041 -2.939 5.993 -2.192 12.638 9.612 1.008 0.000 0.000 0.000 -0.000 -0.000 0.000 4.780 -3.147 -2.710 -0.000 -0.000 0.000 -2.242 -2.937 -20.508 6.469 9.505 14.978 -18.418 9.599 0.210 -0.000 -0.000 0.000 3.394 3.503 -2.772 -4.523 -2.600 -15.418 5.308 3.273 1.241 4.939 6.005 -6.255 4.939 6.005 -6.255 42.932 94.512 105.443 -2.542 -7.435 9.845 5.021 16.510 0.255 -11.416 -3.988 -8.082 -1.206 -5.884 -1.801 0.000 0.000 0.000 3.582 -20.619 -7.519 -2.540 5.870 -2.623 12.809 9.506 1.202 0.000 0.000 0.000 -0.000 -0.000 0.000 4.793 -3.099 -2.937 -0.000 -0.000 -0.000 -2.374 -3.548 -20.730 6.986 10.602 14.480 -19.204 8.704 0.125 -0.000 -0.000 -0.000 3.493 3.797 -3.579 -4.930 -1.389 -15.744 5.481 3.822 1.610 4.948 5.976 -6.537 4.948 5.977 -6.537 43.702 94.187 106.878 -2.513 -7.664 10.368 5.332 17.322 0.338 -12.382 -2.986 -8.196 -0.741 -6.482 -2.325 0.000 0.000 0.000 3.469 -20.488 -8.005 -2.430 6.140 -2.809 12.688 9.220 1.378 0.000 0.000 0.000 0.000 -0.000 0.000 4.847 -3.082 -3.120 0.000 0.000 -0.000 -2.510 -4.249 -20.886 7.584 11.769 13.938 -20.015 7.538 0.263 0.000 0.000 -0.000 3.517 4.061 -4.362 -5.331 -0.205 -15.908 5.438 4.715 1.990 5.009 5.936 -6.765 5.009 5.936 -6.765 44.566 93.987 108.431 -2.403 -7.836 10.893 5.630 17.952 0.464 -13.528 -1.635 -8.322 -0.240 -7.038 -2.887 0.000 0.000 0.000 3.328 -20.296 -8.618 -2.526 6.679 -2.725 12.175 8.890 1.490 0.000 0.000 0.000 -0.000 -0.000 0.000 4.972 -3.069 -3.293 0.000 -0.000 -0.000 -2.806 -4.997 -21.032 8.126 12.843 13.644 -20.828 6.255 0.494 0.000 -0.000 -0.000 3.440 4.223 -5.220 -5.865 0.953 -15.800 5.322 5.760 2.449 5.010 5.835 -6.960 5.010 5.835 -6.960 45.542 93.798 110.032 -2.373 -7.922 11.247 5.862 18.481 0.838 -14.570 -0.152 -8.462 0.100 -7.437 -3.447 0.000 0.000 0.000 3.400 -20.008 -9.128 -2.811 7.247 -2.441 11.472 8.812 1.128 0.000 0.000 0.000 -0.000 -0.000 0.000 5.097 -3.232 -3.408 -0.000 0.000 0.000 -3.034 -5.564 -21.133 8.711 13.843 13.561 -21.781 4.867 0.918 -0.000 0.000 0.000 3.316 4.379 -6.016 -6.428 2.068 -15.493 5.263 6.957 2.777 5.069 5.810 -7.080 5.069 5.810 -7.080 46.694 93.634 111.735 -2.421 -7.971 11.648 6.127 18.854 0.986 -15.578 1.573 -8.443 0.256 -7.444 -4.034 0.000 0.000 0.000 3.523 -19.776 -9.697 -3.138 7.968 -2.140 10.376 9.105 0.658 0.000 0.000 0.000 0.000 0.000 -0.000 5.373 -3.450 -3.582 -0.000 -0.000 0.000 -3.333 -6.120 -21.256 9.225 14.826 13.755 -22.966 3.429 1.282 -0.000 -0.000 0.000 3.102 4.527 -6.799 -6.990 3.041 -15.138 5.045 7.931 3.116 5.093 5.832 -7.137 5.093 5.832 -7.137 47.923 93.449 113.518 -2.472 -7.972 11.830 6.311 19.068 1.280 -16.554 3.637 -8.083 0.150 -7.206 -4.838 0.000 0.000 0.000 3.757 -19.497 -9.966 -3.555 8.915 -1.865 9.123 9.447 0.460 0.000 0.000 0.000 -0.000 -0.000 0.000 5.714 -3.664 -3.677 0.000 -0.000 -0.000 -3.694 -6.739 -21.198 9.675 15.908 14.008 -24.073 1.827 1.612 0.000 -0.000 -0.000 2.701 4.728 -7.290 -7.476 3.906 -14.878 5.007 8.558 3.410 5.077 5.843 -7.119 5.077 5.843 -7.119 49.334 93.291 115.261 -2.581 -8.022 11.925 6.464 19.000 1.429 -17.548 6.142 -7.404 -0.152 -6.378 -5.653 0.000 0.000 0.000 4.098 -19.225 -9.739 -4.007 10.069 -1.734 8.215 9.907 0.148 0.000 0.000 0.000 -0.000 -0.000 0.000 6.109 -3.820 -3.766 -0.000 -0.000 0.000 -4.030 -7.377 -21.072 9.970 17.064 14.124 -25.073 0.039 2.169 -0.000 -0.000 0.000 2.261 4.851 -7.415 -7.753 4.665 -14.837 4.712 8.788 3.532 5.103 5.873 -7.040 5.103 5.873 -7.040 50.857 93.107 116.942 -2.695 -8.118 11.752 6.540 18.738 1.678 -18.659 8.951 -6.481 -0.709 -4.926 -6.329 0.000 0.000 0.000 4.263 -18.970 -8.911 -4.131 11.514 -1.803 7.559 10.196 -0.307 0.000 0.000 0.000 -0.000 -0.000 0.000 6.532 -3.925 -3.816 0.000 -0.000 -0.000 -4.323 -8.010 -20.559 10.133 18.265 14.136 -25.717 -1.963 2.467 0.000 -0.000 -0.000 1.766 5.108 -7.200 -7.961 5.239 -14.800 4.425 8.618 3.534 5.140 5.955 -6.880 5.140 5.955 -6.879 52.587 92.873 118.528 -2.846 -8.250 11.407 6.548 18.137 1.945 -19.945 12.187 -5.327 -1.519 -2.664 -6.721 0.000 0.000 0.000 4.413 -18.666 -7.785 -4.003 12.999 -1.988 6.838 10.240 -0.777 0.000 0.000 0.000 0.000 -0.000 0.000 7.076 -4.019 -3.888 -0.000 -0.000 -0.000 -4.730 -8.519 -19.878 10.124 19.463 14.038 -25.809 -4.303 2.763 -0.000 -0.000 -0.000 1.147 5.351 -6.670 -8.158 5.698 -14.804 4.157 8.143 3.447 5.100 6.038 -6.602 5.100 6.038 -6.602 54.303 92.617 120.092 -3.023 -8.249 10.978 6.610 16.947 2.240 -21.408 15.832 -4.007 -2.913 0.466 -6.728 0.000 0.000 0.000 4.520 -18.167 -6.804 -3.631 14.258 -1.847 6.019 9.791 -1.344 0.000 0.000 0.000 -0.000 -0.000 0.000 7.625 -4.233 -3.861 -0.000 0.000 -0.000 -5.055 -8.956 -19.302 9.860 20.656 13.812 -25.271 -6.779 3.029 -0.000 0.000 -0.000 0.434 5.869 -6.129 -8.160 5.710 -14.730 3.830 7.465 3.296 5.094 6.205 -6.294 5.094 6.205 -6.294 55.976 92.301 121.657 -3.143 -8.294 10.585 6.929 15.526 2.573 -23.360 19.912 -2.585 -4.473 4.107 -6.460 0.000 0.000 0.000 4.690 -17.216 -6.235 -3.274 14.849 -1.111 5.036 9.180 -2.242 0.000 0.000 0.000 -0.000 -0.000 0.000 8.118 -4.320 -3.834 -0.000 -0.000 -0.000 -5.302 -9.293 -18.939 9.413 21.695 13.615 -24.322 -9.247 3.307 -0.000 -0.000 -0.000 -0.209 6.103 -5.704 -8.109 5.657 -14.607 3.550 6.769 3.174 5.066 6.255 -6.031 5.066 6.255 -6.031 57.626 91.919 123.236 -3.264 -8.338 10.192 7.287 13.986 3.055 -25.417 24.049 -1.238 -5.937 7.529 -5.899 0.000 0.000 0.000 4.863 -16.028 -6.022 -2.926 15.120 -0.100 4.039 8.364 -3.062 0.000 0.000 0.000 0.000 -0.000 -0.000 8.527 -4.426 -3.879 -0.000 0.000 -0.000 -5.460 -9.412 -18.833 8.719 22.675 13.542 -23.031 -11.583 3.419 -0.000 0.000 -0.000 -0.709 6.334 -5.260 -8.063 5.199 -14.585 3.292 6.288 3.086 5.068 6.388 -5.731 5.068 6.388 -5.731 59.264 91.462 124.798 -3.327 -8.335 9.886 7.652 12.261 3.801 -27.550 28.392 -0.090 -6.798 10.148 -5.030 0.000 0.000 0.000 5.024 -14.801 -5.896 -2.680 15.162 0.583 3.120 7.514 -3.566 0.000 0.000 0.000 -0.000 -0.000 0.000 8.877 -4.572 -3.849 -0.000 0.000 0.000 -5.550 -9.218 -18.836 7.892 23.235 13.328 -21.531 -13.491 3.555 -0.000 0.000 0.000 -1.195 6.403 -4.953 -8.035 4.724 -14.626 3.324 5.882 2.958 5.051 6.482 -5.475 5.051 6.482 -5.475 59.841 91.668 126.554 -3.298 -8.199 9.620 7.746 10.399 4.783 -29.533 32.673 0.749 -6.808 11.832 -3.844 0.000 0.000 0.000 5.130 -13.647 -5.789 -2.539 15.163 0.986 2.229 6.496 -3.680 0.000 0.000 0.000 0.000 -0.000 0.000 8.951 -4.803 -3.787 -0.000 -0.000 0.000 -5.491 -8.947 -18.960 6.996 23.639 13.141 -19.992 -15.042 3.541 -0.000 -0.000 0.000 -1.614 6.343 -4.732 -7.714 4.031 -14.663 3.417 5.650 2.754 5.122 6.568 -5.240 5.122 6.568 -5.240 60.018 92.047 128.267 -3.327 -8.110 9.268 7.745 8.426 5.986 -31.234 36.808 1.644 -6.025 12.575 -2.485 0.000 0.000 0.000 5.309 -12.561 -5.532 -2.394 15.206 1.136 1.349 5.440 -3.703 0.000 0.000 0.000 -0.000 -0.000 -0.000 8.994 -4.916 -3.611 0.000 0.000 -0.000 -5.216 -8.611 -18.973 6.070 23.781 12.829 -18.598 -15.932 3.441 0.000 0.000 -0.000 -1.946 6.139 -4.631 -7.420 3.357 -14.587 3.719 5.341 2.638 5.196 6.631 -5.077 5.196 6.631 -5.077 60.227 92.378 129.950 -3.256 -8.098 9.000 7.698 6.292 7.081 -32.843 40.795 2.780 -4.594 12.767 -0.946 0.000 0.000 0.000 5.315 -11.384 -5.293 -2.181 15.259 1.057 0.511 4.235 -3.559 0.000 0.000 0.000 0.000 -0.000 0.000 8.915 -4.863 -3.550 -0.000 -0.000 -0.000 -4.985 -8.254 -18.831 5.156 23.675 12.590 -17.146 -16.362 3.283 -0.000 -0.000 -0.000 -2.285 5.746 -4.401 -7.071 2.669 -14.564 4.089 5.006 2.447 5.286 6.657 -4.893 5.286 6.657 -4.893 60.411 92.666 131.566 -3.249 -7.924 8.602 7.533 3.907 8.382 -33.995 44.425 4.107 -2.637 12.586 0.456 0.000 0.000 0.000 5.454 -10.495 -4.699 -1.872 15.295 0.963 -0.392 3.177 -3.589 0.000 0.000 0.000 -0.000 -0.000 -0.000 8.867 -4.897 -3.457 -0.000 0.000 -0.000 -4.668 -7.815 -18.565 4.342 23.250 12.386 -15.781 -16.371 3.119 -0.000 0.000 -0.000 -2.566 5.208 -3.990 -6.744 1.926 -14.578 4.364 4.500 2.254 5.403 6.687 -4.676 5.403 6.687 -4.676 60.603 92.919 133.150 -3.143 -7.827 8.287 7.183 1.458 9.590 -34.690 47.765 5.626 -0.495 11.761 1.707 0.000 0.000 0.000 5.378 -9.543 -3.919 -1.527 15.245 0.795 -1.123 2.278 -3.847 0.000 0.000 0.000 -0.000 -0.000 -0.000 8.624 -4.785 -3.404 -0.000 0.000 0.000 -4.317 -7.402 -18.350 3.530 22.654 12.259 -14.476 -16.009 3.001 -0.000 0.000 0.000 -2.655 4.637 -3.665 -6.495 1.181 -14.497 4.461 3.824 2.003 5.561 6.718 -4.506 5.561 6.718 -4.506 60.775 93.183 134.464 -3.001 -7.646 7.926 6.696 -1.145 10.658 -34.922 50.579 7.149 1.651 10.696 2.703 0.000 0.000 0.000 5.214 -8.642 -2.816 -1.026 15.013 0.537 -1.859 1.448 -4.342 0.000 0.000 0.000 -0.000 -0.000 -0.000 8.338 -4.745 -3.288 -0.000 0.000 -0.000 -4.126 -6.856 -18.313 2.836 21.903 12.305 -13.141 -15.552 2.893 -0.000 0.000 -0.000 -2.599 4.051 -3.254 -6.423 0.533 -14.489 4.563 2.954 1.716 5.713 6.693 -4.394 5.713 6.693 -4.394 60.970 93.415 135.721 -2.893 -7.551 7.610 6.281 -3.672 11.463 -34.554 53.026 8.381 3.564 9.366 3.189 0.000 0.000 0.000 5.087 -7.649 -1.574 -0.569 14.661 0.000 -2.537 0.677 -4.682 0.000 0.000 0.000 0.000 -0.000 -0.000 8.093 -4.636 -3.234 -0.000 -0.000 -0.000 -3.938 -6.310 -18.275 2.072 21.147 12.440 -11.872 -15.100 2.781 -0.000 -0.000 -0.000 -2.462 3.494 -2.871 -6.427 -0.114 -14.385 4.455 2.012 1.355 5.826 6.646 -4.306 5.826 6.646 -4.306 61.192 93.621 136.968 -2.729 -7.505 7.334 5.765 -6.156 12.083 -33.212 54.977 8.937 5.143 8.052 3.224 0.000 0.000 0.000 4.880 -6.605 -0.372 -0.115 14.300 -0.527 -3.340 -0.158 -5.116 0.000 0.000 0.000 -0.000 -0.000 -0.000 7.797 -4.478 -3.219 -0.000 0.000 -0.000 -3.824 -5.643 -18.295 1.420 20.222 12.587 -10.598 -14.567 2.700 -0.000 0.000 -0.000 -2.366 3.037 -2.370 -6.421 -0.766 -14.378 4.348 1.174 1.047 5.900 6.602 -4.217 5.900 6.602 -4.217 61.368 93.837 138.310 -2.620 -7.411 7.018 5.262 -8.554 12.436 -30.950 56.289 8.656 6.138 6.640 2.807 0.000 0.000 0.000 4.746 -5.446 0.577 0.225 13.685 -0.927 -3.890 -0.849 -5.346 0.000 0.000 0.000 -0.000 -0.000 0.000 7.465 -4.322 -3.054 -0.000 0.000 -0.000 -3.626 -5.104 -18.368 0.751 19.447 12.659 -9.335 -14.097 2.587 -0.000 0.000 -0.000 -2.190 2.646 -2.021 -6.355 -1.442 -14.305 4.159 0.416 0.744 5.997 6.535 -4.173 5.997 6.535 -4.173 61.540 94.029 139.679 -2.532 -7.327 6.791 4.655 -10.765 12.550 -27.634 57.025 7.313 6.605 5.164 2.265 0.000 0.000 0.000 4.627 -4.273 1.035 0.442 13.060 -1.061 -4.251 -1.513 -5.458 0.000 0.000 0.000 0.000 0.000 -0.000 7.177 -4.257 -2.951 0.000 -0.000 -0.000 -3.491 -4.405 -18.336 0.120 18.526 12.657 -7.965 -13.492 2.501 0.000 -0.000 -0.000 -2.044 2.386 -1.672 -6.191 -2.167 -14.215 3.878 -0.146 0.484 6.071 6.477 -4.182 6.071 6.477 -4.182 61.665 94.230 141.113 -2.420 -7.282 6.695 3.982 -12.858 12.187 -23.713 57.245 5.484 6.513 3.430 1.750 0.000 0.000 0.000 4.441 -2.913 0.948 0.684 12.215 -0.890 -4.664 -2.046 -5.552 0.000 0.000 0.000 -0.000 -0.000 0.000 6.772 -4.175 -2.968 0.000 -0.000 -0.000 -3.262 -3.785 -18.255 -0.454 17.676 12.652 -6.657 -12.650 2.359 0.000 -0.000 -0.000 -1.806 2.137 -1.343 -6.088 -2.800 -14.126 3.802 -0.493 0.335 6.153 6.401 -4.224 6.153 6.401 -4.224 61.755 94.388 142.494 -2.309 -7.238 6.599 3.293 -14.728 11.709 -18.946 56.898 2.811 5.901 1.667 1.254 0.000 0.000 0.000 4.242 -1.634 0.596 0.885 11.456 -0.439 -4.886 -2.584 -5.606 0.000 0.000 0.000 -0.000 -0.000 0.000 6.456 -4.087 -2.998 -0.000 -0.000 -0.000 -3.266 -3.135 -18.101 -0.919 16.751 12.641 -5.285 -11.733 2.156 -0.000 -0.000 -0.000 -1.772 1.966 -1.019 -5.726 -3.441 -13.924 3.681 -0.703 0.201 6.190 6.320 -4.259 6.190 6.320 -4.259 61.827 94.512 143.914 -2.198 -7.193 6.503 2.534 -16.409 11.081 -13.843 55.982 -0.208 5.096 -0.112 0.854 0.000 0.000 0.000 4.100 -0.375 0.187 0.932 10.791 0.047 -4.824 -3.201 -5.572 0.000 0.000 0.000 0.000 0.000 0.000 6.133 -3.982 -2.941 -0.000 -0.000 -0.000 -3.268 -2.499 -18.033 -1.460 15.819 12.712 -3.996 -10.746 1.964 -0.000 -0.000 -0.000 -1.673 1.918 -0.841 -5.409 -4.067 -13.605 3.754 -0.957 0.121 6.255 6.193 -4.307 6.255 6.193 -4.307 61.893 94.600 145.331 -2.199 -7.145 6.282 1.845 -17.881 10.503 -8.624 54.444 -3.333 4.070 -1.668 0.464 0.000 0.000 0.000 4.012 0.697 -0.032 1.041 10.387 0.276 -4.700 -3.988 -5.487 0.000 0.000 0.000 -0.000 -0.000 0.000 5.934 -3.900 -2.858 -0.000 -0.000 -0.000 -3.277 -1.850 -17.874 -2.000 14.800 12.771 -2.600 -9.516 1.875 -0.000 -0.000 -0.000 -1.584 1.885 -0.575 -5.050 -4.605 -13.237 3.752 -1.048 0.052 6.292 6.112 -4.342 6.292 6.112 -4.342 61.954 94.628 146.768 -2.146 -7.147 6.102 1.152 -18.945 9.829 -3.719 52.123 -6.514 2.910 -3.007 0.248 0.000 0.000 0.000 3.860 1.755 -0.130 1.271 10.062 0.414 -4.539 -4.711 -5.388 0.000 0.000 0.000 -0.000 0.000 -0.000 5.669 -3.753 -2.878 -0.000 -0.000 0.000 -3.213 -1.245 -17.504 -2.551 13.870 12.802 -1.320 -8.318 1.562 -0.000 -0.000 0.000 -1.553 1.850 -0.197 -4.579 -5.065 -12.871 3.839 -1.075 -0.023 6.351 6.000 -4.317 6.351 6.000 -4.317 62.028 94.619 148.228 -2.071 -7.139 5.831 0.566 -19.740 9.284 0.892 49.222 -9.641 1.291 -4.270 0.028 0.000 0.000 0.000 3.691 2.764 -0.004 1.406 9.835 0.493 -4.278 -5.483 -5.335 0.000 0.000 0.000 -0.000 -0.000 0.000 5.489 -3.668 -2.850 -0.000 -0.000 0.000 -3.343 -0.581 -17.030 -3.092 12.865 12.872 0.087 -6.966 1.320 -0.000 -0.000 0.000 -1.557 1.856 0.186 -4.197 -5.418 -12.567 3.941 -0.914 0.007 6.365 5.913 -4.219 6.365 5.913 -4.219 62.082 94.606 149.728 -2.060 -7.272 5.432 0.232 -20.096 8.803 4.740 45.741 -12.293 -0.690 -5.405 -0.005 0.000 0.000 0.000 3.584 3.912 0.236 1.547 9.620 0.625 -4.029 -6.261 -5.327 0.000 0.000 0.000 0.000 -0.000 0.000 5.393 -3.440 -2.715 -0.000 -0.000 -0.000 -3.545 0.114 -16.541 -3.637 11.924 12.995 1.528 -5.617 1.011 -0.000 -0.000 -0.000 -1.489 1.894 0.546 -3.908 -5.664 -12.282 4.077 -0.711 0.068 6.405 5.855 -4.149 6.405 5.855 -4.149 62.199 94.596 151.023 -2.045 -7.311 5.076 -0.062 -20.199 8.240 7.799 41.611 -14.347 -2.903 -6.382 0.016 0.000 0.000 0.000 3.446 4.889 0.386 1.687 9.482 0.814 -3.853 -6.920 -5.346 0.000 0.000 0.000 -0.000 0.000 -0.000 5.248 -3.226 -2.642 0.000 0.000 0.000 -3.706 0.623 -16.120 -4.333 11.040 13.324 3.166 -4.251 0.714 0.000 0.000 0.000 -1.365 1.929 0.999 -3.493 -5.881 -12.113 4.021 -0.494 0.113 6.436 5.730 -4.030 6.436 5.730 -4.030 62.272 94.556 152.387 -2.089 -7.394 4.636 -0.040 -20.164 7.891 10.127 37.300 -15.948 -5.406 -7.308 0.044 0.000 0.000 0.000 3.424 5.903 0.536 1.731 9.433 0.900 -3.606 -7.638 -5.198 0.000 0.000 0.000 0.000 -0.000 0.000 5.271 -3.027 -2.545 -0.000 0.000 -0.000 -4.045 1.214 -15.627 -4.942 10.150 13.584 4.845 -2.842 0.509 -0.000 0.000 -0.000 -1.204 2.040 1.435 -3.343 -6.065 -12.116 4.193 -0.090 0.191 6.402 5.696 -3.886 6.402 5.696 -3.886 62.448 94.492 153.776 -2.134 -7.476 4.196 0.092 -19.859 7.588 12.026 32.583 -17.018 -8.253 -8.175 0.106 0.000 0.000 0.000 3.256 6.967 0.504 1.875 9.338 1.191 -3.394 -8.386 -5.027 0.000 0.000 0.000 -0.000 -0.000 -0.000 5.309 -2.898 -2.481 -0.000 0.000 -0.000 -4.369 1.931 -15.008 -5.648 9.165 13.852 6.680 -1.487 0.239 -0.000 0.000 -0.000 -1.066 2.222 1.907 -3.097 -6.094 -12.247 4.266 0.381 0.199 6.388 5.667 -3.765 6.388 5.667 -3.765 62.622 94.411 155.187 -2.180 -7.559 3.756 0.265 -19.435 7.058 13.326 27.836 -17.029 -11.141 -8.752 0.227 0.000 0.000 0.000 3.151 8.149 0.324 1.848 9.116 1.563 -3.134 -9.123 -4.856 0.000 0.000 0.000 0.000 0.000 -0.000 5.346 -2.769 -2.417 -0.000 0.000 -0.000 -4.713 2.731 -14.449 -6.238 8.095 14.180 8.523 -0.232 0.282 -0.000 0.000 -0.000 -0.785 2.427 2.305 -3.002 -6.191 -12.638 4.397 0.997 0.260 6.342 5.669 -3.610 6.342 5.669 -3.610 62.768 94.302 156.624 -2.271 -7.819 3.318 0.686 -18.806 6.519 14.228 23.301 -16.364 -13.891 -9.068 0.524 0.000 0.000 0.000 3.165 9.426 -0.008 1.776 9.156 1.980 -2.908 -9.890 -4.576 0.000 0.000 0.000 -0.000 -0.000 0.000 5.436 -2.466 -2.378 -0.000 0.000 -0.000 -5.070 3.525 -13.885 -6.827 7.072 14.664 10.350 0.813 0.386 -0.000 0.000 -0.000 -0.454 2.540 2.584 -2.843 -6.095 -13.110 4.638 1.569 0.309 6.306 5.610 -3.461 6.306 5.610 -3.461 62.960 94.181 158.106 -2.282 -8.025 2.870 0.963 -18.177 6.020 15.115 18.917 -15.185 -16.481 -8.855 0.685 0.000 0.000 0.000 2.961 10.652 -0.363 1.738 9.186 2.398 -2.549 -10.644 -4.113 0.000 0.000 0.000 -0.000 -0.000 0.000 5.441 -2.209 -2.314 -0.000 0.000 -0.000 -5.432 4.224 -13.252 -7.417 6.000 15.379 12.253 1.827 0.745 -0.000 0.000 -0.000 -0.123 2.658 2.863 -2.710 -6.071 -13.768 4.819 2.232 0.240 6.260 5.612 -3.306 6.260 5.612 -3.306 63.195 94.059 159.710 -2.392 -8.150 2.346 1.389 -17.451 5.808 16.005 14.669 -13.681 -18.937 -8.411 0.832 0.000 0.000 0.000 2.882 11.807 -0.517 1.570 9.249 2.583 -2.117 -11.262 -3.653 0.000 0.000 0.000 -0.000 0.000 -0.000 5.644 -2.090 -2.232 -0.000 0.000 -0.000 -5.920 4.966 -12.552 -7.899 4.859 16.447 14.098 2.661 1.223 -0.000 0.000 -0.000 0.049 2.903 3.123 -2.523 -6.127 -14.352 5.084 2.841 0.116 6.138 5.672 -3.159 6.138 5.672 -3.159 63.524 93.916 161.407 -2.555 -8.222 1.777 1.753 -16.733 5.707 16.887 10.990 -11.939 -21.042 -8.001 1.031 0.000 0.000 0.000 2.709 12.906 -0.674 1.488 9.405 2.868 -1.593 -11.886 -3.197 0.000 0.000 0.000 -0.000 -0.000 0.000 5.897 -2.018 -2.110 0.000 0.000 -0.000 -6.373 5.674 -11.700 -8.324 3.703 17.570 15.813 3.385 1.653 0.000 0.000 -0.000 0.273 3.105 3.291 -2.439 -6.093 -14.929 5.349 3.390 0.061 6.035 5.702 -2.982 6.035 5.702 -2.982 63.761 93.751 163.130 -2.731 -8.207 1.344 2.000 -16.140 5.612 17.673 8.128 -10.323 -22.646 -7.656 1.050 0.000 0.000 0.000 2.630 13.781 -0.960 1.363 9.859 3.215 -1.080 -12.474 -2.757 0.000 0.000 0.000 -0.000 -0.000 0.000 6.183 -2.111 -1.996 -0.000 0.000 -0.000 -6.851 6.366 -10.891 -8.702 2.732 18.538 17.506 3.774 1.967 -0.000 0.000 -0.000 0.417 3.420 3.430 -2.209 -6.068 -15.467 5.484 3.789 0.078 5.940 5.754 -2.933 5.940 5.754 -2.933 64.103 93.586 164.798 -2.855 -8.243 0.955 1.996 -15.804 5.594 18.302 6.346 -9.318 -23.413 -7.068 1.150 0.000 0.000 0.000 2.507 14.578 -1.208 1.057 10.481 3.521 -0.315 -12.987 -2.362 0.000 0.000 0.000 0.000 0.000 0.000 6.433 -2.167 -1.866 -0.000 0.000 -0.000 -7.272 6.949 -10.087 -9.224 2.111 19.012 19.174 3.860 1.977 -0.000 0.000 -0.000 0.546 3.750 3.509 -1.991 -6.065 -15.864 5.671 4.072 0.117 5.860 5.777 -2.885 5.860 5.777 -2.885 64.460 93.424 166.453 -2.969 -8.184 0.606 1.837 -15.866 5.598 18.836 5.633 -9.026 -23.620 -6.158 1.402 0.000 0.000 0.000 2.361 15.159 -1.407 0.718 11.292 3.936 0.518 -13.344 -2.078 0.000 0.000 0.000 -0.000 -0.000 0.000 6.692 -2.387 -1.796 -0.000 -0.000 -0.000 -7.647 7.470 -9.194 -9.903 1.819 18.801 20.867 3.938 1.766 -0.000 -0.000 -0.000 0.577 4.161 3.670 -1.855 -6.013 -16.197 5.778 4.303 0.180 5.825 5.892 -2.829 5.825 5.892 -2.829 64.911 93.241 168.133 -3.104 -8.133 0.353 1.559 -15.918 5.352 19.139 5.603 -8.871 -23.432 -5.072 1.580 0.000 0.000 0.000 2.183 15.691 -1.489 0.382 12.224 4.108 1.486 -13.574 -1.645 0.000 0.000 0.000 -0.000 -0.000 0.000 6.960 -2.538 -1.641 0.000 -0.000 -0.000 -7.948 7.885 -8.622 -10.610 1.790 18.027 22.381 3.951 1.506 0.000 -0.000 -0.000 0.631 4.499 3.646 -1.784 -5.974 -16.280 5.984 4.417 0.206 5.788 5.927 -2.831 5.788 5.927 -2.831 65.405 93.058 169.847 -3.207 -8.208 0.089 1.203 -15.711 5.009 19.195 5.890 -8.987 -23.019 -3.921 1.991 0.000 0.000 0.000 1.906 16.279 -1.539 0.069 13.287 4.268 2.453 -13.558 -1.097 0.000 0.000 0.000 -0.000 -0.000 0.000 7.197 -2.559 -1.487 -0.000 -0.000 -0.000 -8.289 8.232 -8.129 -11.314 1.910 17.018 24.020 4.057 1.080 -0.000 -0.000 -0.000 0.732 4.769 3.696 -1.839 -5.828 -16.386 6.165 4.571 0.276 5.773 5.991 -2.861 5.773 5.991 -2.861 65.991 92.878 171.599 -3.269 -8.199 -0.216 0.850 -15.297 4.780 19.010 5.893 -9.175 -22.258 -2.244 2.787 0.000 0.000 0.000 1.568 16.719 -1.594 -0.460 14.452 4.543 3.479 -13.231 -0.342 0.000 0.000 0.000 -0.000 -0.000 0.000 7.416 -2.724 -1.306 -0.000 0.000 -0.000 -8.541 8.554 -7.746 -11.993 2.134 15.987 25.323 4.281 0.716 -0.000 0.000 -0.000 0.726 5.098 3.994 -1.913 -5.591 -16.575 6.330 4.631 0.401 5.782 6.117 -2.856 5.782 6.117 -2.856 66.640 92.711 173.477 -3.206 -8.287 -0.530 0.342 -14.539 4.566 18.608 5.844 -9.325 -21.267 -0.347 3.593 0.000 0.000 0.000 1.176 17.178 -1.766 -1.270 15.793 5.062 4.317 -12.424 0.338 0.000 0.000 0.000 -0.000 -0.000 -0.000 7.413 -2.751 -1.153 -0.000 -0.000 -0.000 -8.712 8.922 -7.391 -12.560 2.263 15.073 26.417 4.514 0.370 -0.000 -0.000 -0.000 0.791 5.286 4.430 -1.990 -5.171 -16.839 6.359 4.588 0.465 5.804 6.259 -2.794 5.804 6.259 -2.794 67.293 92.545 175.446 -3.010 -8.378 -0.813 -0.192 -13.933 4.175 18.141 6.322 -9.390 -20.612 1.314 4.269 0.000 0.000 0.000 0.731 17.563 -2.093 -2.328 17.260 5.694 5.050 -11.149 1.152 0.000 0.000 0.000 0.000 0.000 0.000 7.263 -2.956 -0.935 -0.000 -0.000 -0.000 -8.901 9.410 -7.166 -13.009 2.401 14.487 27.344 4.791 0.087 -0.000 -0.000 -0.000 0.922 5.636 4.887 -2.241 -4.734 -17.119 6.399 4.633 0.529 5.818 6.513 -2.811 5.818 6.513 -2.811 68.100 92.363 177.469 -2.752 -8.429 -1.014 -0.781 -13.533 3.430 17.422 7.240 -9.111 -19.742 2.609 4.891 0.000 0.000 0.000 0.183 17.635 -2.462 -3.517 19.142 6.360 5.665 -9.262 1.980 0.000 0.000 0.000 -0.000 -0.000 0.000 7.121 -3.186 -0.864 0.000 0.000 -0.000 -9.081 9.782 -6.848 -13.456 2.547 14.137 28.079 5.222 -0.195 0.000 0.000 -0.000 0.925 5.977 5.326 -2.496 -4.376 -17.120 6.433 4.745 0.598 5.843 6.700 -2.794 5.843 6.700 -2.794 69.043 92.157 179.452 -2.474 -8.407 -1.157 -1.235 -13.348 2.398 16.428 8.470 -8.507 -18.638 3.379 5.409 0.000 0.000 0.000 -0.373 17.236 -2.862 -4.917 21.499 6.753 6.086 -6.545 3.111 0.000 0.000 0.000 -0.000 -0.000 0.000 6.921 -3.414 -0.863 -0.000 -0.000 0.000 -9.261 10.032 -6.323 -13.695 2.637 13.881 28.589 5.758 -0.548 -0.000 -0.000 0.000 0.964 6.237 5.790 -2.785 -3.893 -17.022 6.476 4.754 0.772 5.885 6.847 -2.757 5.885 6.847 -2.757 69.988 91.917 181.392 -2.247 -8.333 -1.346 -1.463 -13.105 1.331 15.118 9.506 -7.785 -17.401 3.811 6.034 0.000 0.000 0.000 -1.102 16.326 -3.220 -6.328 24.523 7.031 6.130 -3.029 4.319 0.000 0.000 0.000 0.000 0.000 0.000 6.777 -3.688 -0.818 -0.000 -0.000 -0.000 -9.369 10.251 -5.822 -13.831 2.702 13.806 28.850 6.250 -0.804 -0.000 -0.000 -0.000 0.915 6.425 6.243 -3.065 -3.477 -16.908 6.576 4.959 1.077 5.927 6.995 -2.721 5.927 6.995 -2.721 70.920 91.638 183.244 -2.020 -8.260 -1.535 -1.575 -12.620 0.564 13.686 10.127 -7.237 -15.956 3.968 6.639 0.000 0.000 0.000 -1.950 14.802 -3.794 -8.064 28.206 7.478 5.808 1.305 5.823 0.000 0.000 0.000 -0.000 -0.000 0.000 6.615 -3.896 -0.743 -0.000 0.000 0.000 -9.388 10.269 -5.433 -13.883 2.777 13.932 28.885 6.689 -1.099 -0.000 0.000 0.000 0.962 6.535 6.611 -3.520 -3.188 -16.612 6.718 5.236 1.361 6.000 7.079 -2.668 6.000 7.079 -2.668 71.694 92.041 184.507 -1.844 -8.135 -1.770 -1.731 -11.782 0.166 12.388 10.058 -6.933 -14.562 4.026 7.222 0.000 0.000 0.000 -2.750 12.946 -4.801 -10.605 32.129 8.640 5.287 6.043 7.599 0.000 0.000 0.000 0.000 -0.000 0.000 6.458 -4.073 -0.803 -0.000 -0.000 0.000 -9.358 10.174 -5.049 -13.806 2.824 14.205 28.697 6.887 -1.222 -0.000 -0.000 0.000 0.832 6.522 7.103 -3.789 -3.061 -16.158 6.884 5.592 1.493 6.042 7.139 -2.518 6.042 7.139 -2.518 72.392 92.468 185.892 -1.688 -7.971 -2.130 -1.893 -10.735 0.351 11.323 9.579 -6.681 -13.049 4.026 7.404 0.000 0.000 0.000 -3.424 10.896 -6.185 -14.118 36.002 10.990 4.586 10.110 9.298 0.000 0.000 0.000 -0.000 -0.000 0.000 6.334 -4.277 -0.739 -0.000 0.000 -0.000 -9.277 10.029 -4.796 -13.699 2.897 14.544 28.316 7.001 -1.296 -0.000 0.000 -0.000 0.690 6.423 7.530 -4.037 -3.068 -15.773 7.020 5.759 1.645 6.124 7.200 -2.370 6.124 7.200 -2.370 72.950 92.893 187.329 -1.539 -7.675 -2.578 -1.894 -9.689 0.760 10.188 8.890 -5.912 -11.631 4.087 6.965 0.000 0.000 0.000 -3.882 8.630 -7.882 -18.485 39.411 14.908 3.957 12.598 10.063 0.000 0.000 0.000 -0.000 -0.000 0.000 6.193 -4.522 -0.600 -0.000 0.000 -0.000 -9.254 9.840 -4.819 -13.440 2.904 15.064 27.727 6.840 -1.303 -0.000 0.000 -0.000 0.527 6.172 7.815 -4.226 -3.099 -15.394 7.179 5.659 1.647 6.237 7.164 -2.208 6.237 7.164 -2.208 73.513 93.273 188.735 -1.388 -7.379 -3.026 -1.944 -8.686 1.011 9.090 8.266 -4.722 -10.105 4.038 6.290 0.000 0.000 0.000 -4.105 6.352 -9.682 -23.323 42.200 19.802 3.378 13.521 9.832 0.000 0.000 0.000 0.000 -0.000 0.000 5.995 -4.619 -0.460 -0.000 -0.000 0.000 -9.163 9.475 -5.148 -13.049 2.965 15.532 26.815 6.586 -1.207 -0.000 -0.000 0.000 0.436 5.791 7.929 -4.342 -3.409 -15.053 7.115 5.268 1.487 6.330 7.089 -2.053 6.330 7.089 -2.053 74.045 93.622 190.111 -1.271 -7.299 -3.345 -1.990 -7.593 1.063 7.958 7.585 -3.665 -8.768 4.044 5.803 0.000 0.000 0.000 -4.157 4.219 -11.689 -28.336 44.341 24.968 2.915 13.414 8.836 0.000 0.000 0.000 0.000 0.000 0.000 5.787 -4.450 -0.449 -0.000 -0.000 -0.000 -8.987 9.077 -5.876 -12.582 3.007 16.009 25.735 6.233 -1.064 -0.000 -0.000 -0.000 0.433 5.252 7.893 -4.437 -3.776 -14.908 7.033 4.715 1.258 6.338 6.864 -1.845 6.338 6.864 -1.845 74.538 93.908 191.473 -1.268 -7.253 -3.568 -1.944 -6.457 1.004 6.981 6.868 -2.832 -7.627 3.880 5.435 0.000 0.000 0.000 -3.948 2.125 -13.617 -33.148 45.934 29.805 2.333 12.508 7.342 0.000 0.000 0.000 -0.000 -0.000 -0.000 5.680 -4.253 -0.552 -0.000 0.000 0.000 -8.713 8.572 -6.866 -12.185 3.206 16.332 24.495 5.731 -1.020 -0.000 0.000 0.000 0.423 4.627 7.791 -4.467 -4.032 -14.976 6.786 3.886 0.958 6.369 6.668 -1.665 6.369 6.668 -1.665 74.998 94.116 192.770 -1.225 -7.172 -3.609 -1.966 -5.524 0.544 6.060 6.226 -2.243 -6.578 3.759 5.490 0.000 0.000 0.000 -3.787 -0.197 -15.402 -37.561 47.203 34.131 1.518 11.234 5.733 0.000 0.000 0.000 -0.000 -0.000 0.000 5.346 -4.084 -0.695 -0.000 0.000 -0.000 -8.134 7.938 -8.123 -11.961 3.761 16.348 23.194 4.950 -0.774 -0.000 0.000 -0.000 0.675 3.971 7.490 -4.482 -4.351 -15.128 6.448 2.987 0.588 6.446 6.509 -1.544 6.446 6.509 -1.544 75.466 94.296 194.017 -1.274 -7.119 -3.656 -1.998 -4.606 -0.183 5.379 5.635 -1.614 -5.738 3.646 5.772 0.000 0.000 0.000 -3.508 -2.675 -16.646 -41.337 48.440 37.757 0.651 9.628 4.002 0.000 0.000 0.000 0.000 -0.000 0.000 5.221 -3.933 -0.747 0.000 -0.000 -0.000 -7.705 7.092 -9.532 -11.710 4.710 16.253 21.965 3.923 -0.633 0.000 -0.000 -0.000 0.896 3.489 7.137 -4.618 -4.686 -15.451 6.095 2.057 0.254 6.436 6.337 -1.500 6.436 6.337 -1.500 75.855 94.496 194.927 -1.530 -7.013 -3.675 -1.757 -3.829 -1.118 4.651 5.154 -0.532 -4.890 3.428 5.723 0.000 0.000 0.000 -3.141 -5.155 -17.401 -43.977 49.510 40.417 0.228 7.972 2.215 0.000 0.000 0.000 -0.000 -0.000 -0.000 5.301 -3.825 -0.848 -0.000 -0.000 -0.000 -7.290 6.111 -10.839 -11.437 5.916 15.997 20.733 2.568 -0.467 -0.000 -0.000 -0.000 1.063 3.072 6.710 -4.723 -4.960 -15.743 5.717 1.136 -0.060 6.371 6.223 -1.451 6.371 6.223 -1.451 76.236 94.702 195.921 -1.835 -6.854 -3.740 -1.445 -2.982 -1.925 3.944 4.524 0.618 -4.181 3.252 5.474 0.000 0.000 0.000 -2.699 -7.677 -17.721 -45.637 50.455 41.944 0.142 6.144 0.810 0.000 0.000 0.000 0.000 0.000 -0.000 5.506 -3.734 -0.982 -0.000 -0.000 0.000 -6.878 5.130 -11.833 -11.064 7.071 15.769 19.360 1.167 -0.403 -0.000 -0.000 0.000 1.221 2.693 6.534 -4.888 -5.211 -16.024 5.303 0.435 -0.369 6.266 6.100 -1.360 6.266 6.100 -1.360 76.541 94.924 196.990 -2.255 -6.728 -3.708 -0.994 -1.990 -2.570 3.332 3.761 1.556 -3.594 2.971 5.190 0.000 0.000 0.000 -2.186 -10.071 -17.819 -46.182 51.240 42.514 0.299 4.343 -0.190 0.000 0.000 0.000 0.000 0.000 0.000 5.865 -3.690 -1.050 -0.000 -0.000 -0.000 -6.533 4.124 -12.729 -10.506 8.316 15.762 17.705 -0.222 -0.245 -0.000 -0.000 -0.000 1.278 2.433 6.273 -5.045 -5.385 -16.298 5.039 -0.079 -0.499 6.150 6.000 -1.365 6.150 6.000 -1.365 76.824 95.115 198.069 -2.554 -6.702 -3.685 -0.671 -0.822 -2.828 2.848 2.810 2.031 -3.241 2.734 5.133 0.000 0.000 0.000 -1.803 -12.293 -17.560 -45.703 51.881 42.097 0.670 2.492 -0.753 0.000 0.000 0.000 0.000 -0.000 -0.000 6.099 -3.553 -1.104 0.000 -0.000 -0.000 -6.095 3.067 -13.331 -9.749 9.422 15.907 15.603 -1.562 -0.069 0.000 -0.000 -0.000 1.275 2.266 6.127 -5.172 -5.461 -16.408 4.827 -0.438 -0.572 5.964 5.903 -1.360 5.964 5.903 -1.360 77.061 95.284 199.067 -2.853 -6.677 -3.661 -0.307 0.371 -2.757 2.442 1.651 2.232 -3.157 2.598 5.004 0.000 0.000 0.000 -1.383 -14.395 -17.180 -44.222 52.181 40.865 1.179 0.833 -0.990 0.000 0.000 0.000 -0.000 -0.000 0.000 6.333 -3.416 -1.159 -0.000 -0.000 0.000 -5.707 2.067 -13.792 -8.733 10.362 16.349 13.092 -2.801 0.163 -0.000 -0.000 0.000 1.201 2.058 6.007 -5.157 -5.347 -16.308 4.689 -0.676 -0.627 5.793 5.861 -1.360 5.793 5.861 -1.360 77.158 95.417 200.045 -3.040 -6.667 -3.510 0.060 1.544 -2.483 2.003 0.515 2.011 -3.216 2.500 5.006 0.000 0.000 0.000 -0.950 -16.137 -16.813 -41.891 51.982 38.814 1.707 -0.706 -0.992 0.000 0.000 0.000 -0.000 0.000 -0.000 6.450 -3.285 -1.327 -0.000 -0.000 -0.000 -5.310 1.104 -13.970 -7.377 11.070 16.747 10.011 -3.770 0.336 -0.000 -0.000 -0.000 1.142 1.935 5.952 -5.207 -5.191 -16.182 4.640 -0.762 -0.507 5.642 5.790 -1.332 5.642 5.790 -1.332 77.179 95.562 201.112 -3.349 -6.557 -3.350 0.705 2.685 -2.049 1.329 -0.615 1.828 -3.132 2.289 4.708 0.000 0.000 0.000 -0.382 -17.661 -16.557 -38.659 50.999 36.037 2.337 -1.632 -0.956 0.000 0.000 0.000 -0.000 -0.000 -0.000 6.703 -3.245 -1.354 -0.000 -0.000 0.000 -4.906 0.313 -14.121 -5.861 11.569 16.976 6.544 -4.615 0.537 -0.000 -0.000 0.000 1.009 1.835 5.625 -5.198 -5.057 -15.717 4.653 -0.536 -0.463 5.512 5.706 -1.443 5.512 5.706 -1.443 77.314 95.664 202.098 -3.590 -6.543 -3.022 1.174 3.760 -1.711 0.744 -1.580 1.556 -3.148 2.125 4.412 0.000 0.000 0.000 0.258 -18.740 -16.663 -35.297 49.199 33.240 3.084 -2.189 -0.907 0.000 0.000 0.000 -0.000 -0.000 0.000 6.874 -3.135 -1.550 -0.000 0.000 0.000 -4.507 -0.482 -14.266 -4.159 12.026 17.107 2.923 -5.325 0.772 -0.000 0.000 0.000 0.820 1.782 5.389 -5.128 -4.783 -15.418 4.724 -0.359 -0.265 5.425 5.680 -1.495 5.425 5.680 -1.495 77.495 95.741 203.090 -3.781 -6.586 -2.650 1.531 4.820 -1.479 0.206 -2.391 1.333 -3.020 1.845 4.155 0.000 0.000 0.000 0.927 -19.422 -16.915 -31.867 46.623 30.462 3.862 -2.468 -0.979 0.000 0.000 0.000 0.000 -0.000 -0.000 7.029 -3.060 -1.766 -0.000 -0.000 -0.000 -4.041 -1.157 -14.345 -2.523 12.364 16.941 -0.739 -6.079 0.972 -0.000 -0.000 -0.000 0.663 1.850 5.104 -5.050 -4.413 -15.088 4.795 -0.200 -0.041 5.334 5.692 -1.628 5.334 5.692 -1.628 77.631 95.800 204.082 -3.943 -6.755 -2.292 1.856 6.002 -1.236 -0.259 -3.184 1.016 -3.022 1.546 3.933 0.000 0.000 0.000 1.555 -19.717 -17.031 -28.226 43.571 27.579 4.679 -2.523 -0.990 0.000 0.000 0.000 -0.000 -0.000 0.000 7.079 -2.888 -1.901 -0.000 -0.000 0.000 -3.577 -1.771 -14.493 -0.827 12.788 16.416 -4.397 -7.039 1.258 -0.000 -0.000 0.000 0.653 1.940 4.688 -5.107 -3.983 -14.792 4.829 0.020 0.089 5.305 5.686 -1.774 5.305 5.686 -1.774 77.831 95.839 204.973 -4.104 -6.926 -1.935 2.189 7.054 -1.085 -0.816 -3.852 0.850 -2.899 1.268 3.673 0.000 0.000 0.000 2.051 -19.791 -16.971 -24.387 40.149 24.650 5.387 -2.171 -1.033 0.000 0.000 0.000 -0.000 -0.000 -0.000 7.132 -2.717 -2.035 0.000 -0.000 -0.000 -3.050 -2.299 -14.747 0.709 13.173 15.753 -7.842 -8.295 1.514 0.000 -0.000 -0.000 0.608 2.183 4.264 -5.024 -3.691 -14.591 4.728 0.158 0.176 5.298 5.712 -1.947 5.298 5.712 -1.947 77.950 95.874 205.935 -4.255 -7.233 -1.493 2.676 8.254 -0.981 -1.531 -4.449 0.604 -2.962 0.848 3.396 0.000 0.000 0.000 2.459 -19.692 -16.664 -20.729 36.624 21.580 6.340 -1.542 -0.845 0.000 0.000 0.000 0.000 0.000 -0.000 7.168 -2.422 -2.270 0.000 -0.000 -0.000 -2.655 -2.898 -15.034 2.090 13.700 14.910 -10.817 -9.754 1.734 0.000 -0.000 -0.000 0.639 2.466 3.815 -4.959 -3.325 -14.465 4.674 0.224 0.326 5.249 5.736 -2.122 5.249 5.736 -2.122 78.138 95.886 206.825 -4.331 -7.585 -1.106 3.058 9.260 -0.580 -2.332 -4.628 0.029 -2.801 0.318 3.148 0.000 0.000 0.000 2.606 -19.393 -15.894 -16.865 32.869 18.141 7.397 -0.447 -0.397 0.000 0.000 0.000 0.000 -0.000 -0.000 7.138 -2.077 -2.446 0.000 -0.000 0.000 -2.266 -3.501 -15.317 3.385 14.282 13.811 -13.545 -11.374 2.078 0.000 -0.000 0.000 0.665 2.774 3.557 -4.938 -2.893 -14.508 4.646 0.398 0.438 5.255 5.703 -2.303 5.255 5.703 -2.303 78.417 95.862 207.734 -4.311 -7.909 -0.715 3.299 10.234 -0.084 -3.171 -4.783 -0.726 -2.471 -0.111 2.993 0.000 0.000 0.000 2.798 -19.026 -14.627 -13.372 28.920 14.536 8.545 0.844 0.128 0.000 0.000 0.000 -0.000 0.000 -0.000 7.037 -1.830 -2.638 -0.000 0.000 0.000 -2.029 -3.989 -15.708 4.610 14.977 12.874 -15.919 -13.050 2.287 -0.000 0.000 0.000 0.672 3.101 3.307 -4.914 -2.415 -14.523 4.616 0.572 0.550 5.235 5.765 -2.466 5.235 5.765 -2.466 78.776 95.839 208.786 -4.383 -8.262 -0.327 3.551 11.281 0.409 -3.923 -4.800 -1.486 -2.184 -0.707 2.779 0.000 0.000 0.000 3.118 -18.608 -12.908 -10.129 24.793 10.576 9.753 2.202 0.683 0.000 0.000 0.000 0.000 -0.000 0.000 7.216 -1.581 -2.828 -0.000 0.000 -0.000 -1.937 -4.394 -16.024 5.498 15.459 11.948 -17.826 -14.721 2.502 -0.000 0.000 -0.000 0.444 3.567 2.994 -4.806 -1.972 -14.449 4.699 0.641 0.673 5.116 5.858 -2.616 5.116 5.858 -2.616 79.144 95.780 209.870 -4.339 -8.627 0.188 3.786 12.353 0.707 -4.809 -4.822 -2.120 -1.779 -1.293 2.534 0.000 0.000 0.000 3.423 -18.080 -11.089 -7.446 20.561 6.508 11.182 3.552 1.048 0.000 0.000 0.000 -0.000 0.000 -0.000 7.315 -1.420 -3.107 -0.000 0.000 -0.000 -1.969 -4.715 -16.314 6.330 15.932 11.154 -19.393 -16.210 2.808 -0.000 0.000 -0.000 0.242 4.021 2.541 -4.707 -1.560 -14.356 4.764 0.862 0.903 4.965 5.936 -2.782 4.965 5.936 -2.782 79.644 95.688 211.020 -4.229 -8.952 0.789 3.975 13.400 0.732 -5.830 -4.778 -2.578 -1.396 -2.011 2.261 0.000 0.000 0.000 3.541 -17.561 -9.451 -5.150 16.423 2.445 12.675 4.947 1.214 0.000 0.000 0.000 0.000 -0.000 -0.000 7.332 -1.488 -3.381 -0.000 -0.000 -0.000 -2.159 -4.734 -16.688 7.097 16.225 10.530 -20.623 -17.538 3.183 -0.000 -0.000 -0.000 0.127 4.585 1.727 -4.725 -1.051 -14.058 5.006 1.008 1.118 4.878 6.040 -3.002 4.878 6.040 -3.002 80.219 95.574 212.249 -4.148 -9.149 1.402 4.145 14.253 0.689 -6.771 -4.497 -2.962 -0.967 -2.793 1.948 0.000 0.000 0.000 3.557 -17.106 -8.109 -3.388 12.458 -1.430 14.274 6.537 1.152 0.000 0.000 0.000 -0.000 -0.000 -0.000 7.446 -1.660 -3.735 -0.000 -0.000 0.000 -2.572 -4.658 -16.842 7.919 16.491 9.980 -21.484 -18.684 3.705 -0.000 -0.000 0.000 -0.121 5.058 0.834 -4.656 -0.513 -13.807 5.271 1.185 1.364 4.726 6.104 -3.153 4.726 6.104 -3.153 80.837 95.443 213.474 -4.065 -9.345 2.015 4.248 15.103 0.526 -7.535 -4.218 -3.290 -0.768 -3.600 1.839 0.000 0.000 0.000 3.522 -16.558 -7.324 -2.201 8.903 -4.750 15.700 8.148 1.303 0.000 0.000 0.000 0.000 -0.000 0.000 7.485 -1.859 -4.008 -0.000 0.000 -0.000 -2.939 -4.570 -17.034 8.434 16.681 9.657 -21.948 -19.415 4.167 -0.000 0.000 -0.000 -0.202 5.572 -0.361 -4.599 -0.136 -13.667 5.430 1.548 1.646 4.618 6.233 -3.286 4.618 6.233 -3.286 81.456 95.279 214.717 -3.961 -9.532 2.534 4.389 15.973 0.383 -8.358 -3.956 -3.567 -0.712 -4.359 1.668 0.000 0.000 0.000 3.391 -16.127 -7.185 -1.386 6.248 -7.080 16.743 9.412 1.765 0.000 0.000 0.000 -0.000 -0.000 0.000 7.593 -2.099 -4.294 -0.000 -0.000 -0.000 -3.450 -4.419 -17.101 8.855 16.773 9.551 -22.096 -19.734 4.648 -0.000 -0.000 -0.000 -0.303 6.160 -1.472 -4.664 0.152 -13.473 5.656 1.973 1.749 4.473 6.304 -3.397 4.473 6.304 -3.397 82.090 95.088 215.942 -3.879 -9.675 2.927 4.515 16.739 0.214 -9.235 -3.629 -3.773 -0.661 -5.098 1.466 0.000 0.000 0.000 3.401 -15.861 -7.381 -1.097 4.564 -8.278 17.403 10.137 2.254 0.000 0.000 0.000 0.000 0.000 -0.000 7.739 -2.385 -4.394 -0.000 0.000 -0.000 -3.944 -4.092 -17.201 9.033 16.784 9.785 -21.967 -19.661 4.888 -0.000 0.000 -0.000 -0.558 6.743 -2.559 -4.495 0.405 -13.479 5.749 2.323 1.917 4.340 6.433 -3.540 4.340 6.433 -3.540 82.698 94.878 217.120 -3.813 -9.683 3.234 4.639 17.333 0.009 -10.034 -3.203 -3.756 -0.699 -5.884 1.262 0.000 0.000 0.000 3.652 -15.910 -7.666 -1.203 3.878 -8.439 17.543 10.462 2.500 0.000 0.000 0.000 0.000 0.000 -0.000 7.879 -2.777 -4.451 -0.000 -0.000 -0.000 -4.507 -3.684 -17.104 9.092 16.694 10.084 -21.430 -19.280 5.167 -0.000 -0.000 -0.000 -0.795 7.312 -3.588 -4.402 0.521 -13.495 5.861 2.695 2.011 4.254 6.559 -3.653 4.254 6.559 -3.653 83.319 94.629 218.347 -3.709 -9.607 3.498 4.709 17.849 -0.139 -10.818 -2.696 -3.737 -0.890 -6.693 0.978 0.000 0.000 0.000 3.925 -16.191 -7.882 -1.524 3.986 -7.705 17.277 10.364 2.275 0.000 0.000 0.000 0.000 0.000 0.000 7.963 -3.177 -4.415 -0.000 -0.000 -0.000 -4.999 -3.275 -16.956 8.886 16.423 10.489 -20.633 -18.480 5.394 -0.000 -0.000 -0.000 -1.129 7.881 -4.499 -4.178 0.593 -13.647 5.803 2.896 2.263 4.251 6.643 -3.788 4.251 6.643 -3.788 83.985 94.436 219.618 -3.697 -9.565 3.763 4.806 18.371 -0.230 -11.534 -2.070 -3.760 -1.119 -7.428 0.637 0.000 0.000 0.000 4.340 -16.281 -7.983 -1.933 4.313 -6.508 16.705 10.234 1.819 0.000 0.000 0.000 -0.000 -0.000 0.000 8.107 -3.464 -4.424 -0.000 0.000 -0.000 -5.452 -2.950 -16.786 8.548 16.071 11.075 -19.543 -17.257 5.518 -0.000 0.000 -0.000 -1.496 8.390 -5.334 -4.000 0.701 -13.563 5.897 2.885 2.311 4.266 6.688 -3.906 4.266 6.688 -3.906 84.715 94.247 220.920 -3.705 -9.531 4.121 4.970 18.829 -0.357 -12.347 -1.279 -3.755 -1.278 -8.208 0.291 0.000 0.000 0.000 4.715 -16.293 -8.056 -2.353 4.681 -5.158 16.021 10.165 0.975 0.000 0.000 0.000 -0.000 -0.000 0.000 8.249 -3.691 -4.497 -0.000 -0.000 0.000 -5.926 -2.528 -16.585 7.959 15.628 11.729 -18.048 -15.871 5.559 -0.000 -0.000 0.000 -1.887 8.884 -6.098 -3.691 0.636 -13.376 5.768 2.924 2.327 4.317 6.727 -4.064 4.317 6.727 -4.064 85.396 94.073 222.228 -3.633 -9.589 4.649 5.204 19.234 -0.632 -13.215 -0.268 -3.762 -1.438 -8.806 -0.125 0.000 0.000 0.000 4.836 -15.992 -8.124 -2.522 4.912 -4.410 14.907 10.599 0.101 0.000 0.000 0.000 0.000 -0.000 -0.000 8.236 -3.865 -4.660 -0.000 0.000 -0.000 -6.330 -1.955 -16.563 7.173 15.150 12.407 -16.284 -14.371 5.471 -0.000 0.000 -0.000 -2.224 9.358 -6.823 -3.437 0.663 -13.244 5.623 2.827 2.453 4.478 6.767 -4.274 4.478 6.767 -4.274 86.079 93.956 223.632 -3.727 -9.641 5.230 5.632 19.589 -0.796 -14.002 0.890 -3.847 -1.695 -9.067 -0.727 0.000 0.000 0.000 5.024 -15.484 -8.160 -2.574 5.211 -4.306 13.315 11.151 -0.405 0.000 0.000 0.000 -0.000 -0.000 0.000 8.379 -4.070 -4.900 -0.000 -0.000 -0.000 -6.727 -1.381 -16.692 6.094 14.666 13.222 -14.187 -12.678 5.210 -0.000 -0.000 -0.000 -2.681 9.907 -7.389 -3.048 0.718 -13.065 5.448 2.591 2.393 4.640 6.806 -4.485 4.640 6.806 -4.485 86.901 93.821 225.155 -3.895 -9.653 5.860 6.095 19.898 -0.917 -14.864 2.240 -4.001 -1.818 -9.093 -1.411 0.000 0.000 0.000 5.210 -14.864 -8.002 -2.634 5.610 -4.781 11.470 11.656 -0.704 0.000 0.000 0.000 -0.000 0.000 -0.000 8.583 -4.334 -5.194 -0.000 0.000 -0.000 -7.185 -0.775 -16.806 4.931 14.318 13.870 -11.790 -11.024 4.815 -0.000 0.000 -0.000 -3.146 10.489 -7.762 -2.641 0.761 -13.072 5.230 2.439 2.391 4.770 6.874 -4.662 4.770 6.874 -4.662 87.797 93.700 226.832 -3.988 -9.707 6.440 6.463 20.162 -0.937 -15.633 3.864 -4.040 -2.096 -8.786 -2.194 0.000 0.000 0.000 5.296 -14.301 -7.642 -2.720 6.111 -5.466 9.485 12.241 -0.747 0.000 0.000 0.000 -0.000 -0.000 0.000 8.690 -4.456 -5.462 0.000 0.000 -0.000 -7.542 -0.280 -16.755 3.460 14.025 14.210 -8.940 -9.322 4.210 0.000 0.000 -0.000 -3.487 11.071 -7.903 -2.375 0.865 -13.115 5.089 2.061 2.338 4.955 6.925 -4.796 4.955 6.925 -4.796 88.859 93.621 228.424 -4.105 -9.721 6.890 6.678 20.059 -0.736 -16.352 5.989 -3.904 -2.368 -7.995 -3.010 0.000 0.000 0.000 5.430 -14.028 -6.991 -2.711 7.053 -6.077 7.499 12.359 -0.884 0.000 0.000 0.000 -0.000 -0.000 0.000 8.897 -4.587 -5.676 -0.000 0.000 0.000 -8.044 0.184 -16.571 1.997 13.831 14.415 -5.893 -7.626 3.474 -0.000 0.000 0.000 -3.838 11.475 -7.817 -2.326 1.224 -13.234 5.016 1.766 2.341 5.085 6.972 -4.941 5.085 6.972 -4.941 89.997 93.521 229.985 -4.133 -9.857 7.155 6.821 19.900 -0.466 -17.240 8.374 -3.477 -2.783 -6.673 -3.891 0.000 0.000 0.000 5.609 -13.670 -6.073 -2.797 8.106 -6.471 5.932 12.113 -1.270 0.000 0.000 0.000 -0.000 -0.000 -0.000 8.950 -4.512 -5.752 -0.000 -0.000 -0.000 -8.418 0.644 -16.083 0.498 13.681 14.259 -2.568 -5.987 2.578 -0.000 -0.000 -0.000 -3.999 11.770 -7.492 -2.415 1.666 -13.356 4.835 1.708 2.346 5.275 6.999 -5.012 5.275 6.999 -5.012 91.245 93.405 231.588 -4.243 -9.904 7.248 6.982 19.333 -0.123 -18.267 11.283 -2.678 -3.441 -4.718 -4.625 0.000 0.000 0.000 5.830 -13.283 -4.997 -2.748 9.037 -6.691 4.736 11.668 -1.859 0.000 0.000 0.000 -0.000 0.000 0.000 9.139 -4.474 -5.795 -0.000 0.000 -0.000 -8.863 1.132 -15.359 -0.935 13.472 13.991 0.796 -4.375 1.686 -0.000 0.000 -0.000 -4.256 11.982 -6.846 -2.580 2.206 -13.506 4.902 1.735 2.347 5.359 7.022 -4.999 5.359 7.022 -4.999 92.569 93.270 233.046 -4.338 -10.033 7.205 7.054 18.417 0.269 -19.287 14.647 -1.460 -4.660 -1.961 -5.237 0.000 0.000 0.000 5.913 -12.709 -4.008 -2.395 9.928 -6.813 3.759 11.074 -2.547 0.000 0.000 0.000 -0.000 -0.000 -0.000 9.295 -4.176 -5.712 -0.000 -0.000 0.000 -9.123 1.528 -14.789 -2.414 13.117 13.857 3.973 -2.615 0.848 -0.000 -0.000 0.000 -4.309 11.925 -6.117 -2.791 2.867 -13.738 4.844 1.937 2.437 5.509 6.994 -4.954 5.509 6.994 -4.954 93.851 93.094 234.450 -4.384 -10.160 6.981 7.115 17.064 0.779 -20.748 18.572 0.306 -6.137 1.390 -5.721 0.000 0.000 0.000 6.013 -11.939 -3.116 -1.994 10.469 -6.723 2.947 10.411 -3.238 0.000 0.000 0.000 -0.000 -0.000 0.000 9.292 -3.711 -5.511 -0.000 -0.000 -0.000 -9.250 1.913 -14.273 -3.719 12.639 13.934 7.075 -0.890 0.003 -0.000 -0.000 -0.000 -4.141 11.673 -5.128 -3.099 3.421 -14.122 4.811 2.268 2.535 5.661 6.863 -4.860 5.661 6.863 -4.860 95.116 92.852 235.851 -4.370 -10.243 6.845 7.239 15.335 1.225 -22.488 22.864 2.373 -7.726 5.038 -5.931 0.000 0.000 0.000 5.977 -10.864 -2.739 -1.526 10.588 -6.331 2.323 9.572 -3.864 0.000 0.000 0.000 -0.000 -0.000 0.000 9.146 -3.312 -5.300 -0.000 -0.000 0.000 -9.228 2.424 -14.105 -4.869 11.986 14.208 9.755 0.642 -0.649 -0.000 -0.000 0.000 -3.888 11.395 -4.240 -3.389 3.867 -14.550 4.861 2.689 2.733 5.854 6.739 -4.807 5.854 6.739 -4.807 96.397 92.528 237.209 -4.318 -10.149 6.712 7.342 13.178 1.751 -24.480 27.421 4.603 -9.023 8.332 -5.711 0.000 0.000 0.000 5.820 -9.801 -2.759 -1.002 10.478 -5.757 1.587 8.660 -4.319 0.000 0.000 0.000 -0.000 -0.000 0.000 9.025 -3.059 -4.986 -0.000 -0.000 0.000 -9.224 2.975 -14.083 -5.914 11.252 14.511 12.216 1.948 -1.232 -0.000 -0.000 0.000 -3.764 11.143 -3.539 -3.447 3.884 -14.861 4.736 3.166 2.864 6.012 6.592 -4.786 6.012 6.592 -4.786 97.658 92.116 238.517 -4.317 -9.845 6.720 7.461 10.757 2.417 -26.543 31.844 6.589 -9.628 10.992 -5.063 0.000 0.000 0.000 5.624 -8.920 -3.250 -0.519 10.263 -5.048 0.907 7.712 -4.553 0.000 0.000 0.000 -0.000 -0.000 -0.000 8.810 -2.978 -4.887 -0.000 -0.000 -0.000 -9.107 3.366 -14.222 -6.866 10.626 14.823 14.268 2.839 -1.469 -0.000 -0.000 -0.000 -3.602 10.828 -2.883 -3.346 3.636 -14.931 4.649 3.284 2.877 6.221 6.429 -4.709 6.221 6.429 -4.709 97.859 92.381 240.013 -4.412 -9.671 6.685 7.565 8.299 3.477 -28.492 36.291 8.114 -9.632 12.804 -3.975 0.000 0.000 0.000 5.610 -7.921 -3.791 -0.209 10.034 -4.419 0.410 6.730 -4.594 0.000 0.000 0.000 0.000 -0.000 0.000 8.720 -2.795 -4.718 0.000 -0.000 -0.000 -8.888 3.810 -14.351 -7.739 9.961 14.996 16.080 3.213 -1.741 0.000 -0.000 -0.000 -3.523 10.495 -2.255 -3.107 3.183 -15.086 4.646 3.280 2.936 6.387 6.245 -4.688 6.387 6.245 -4.688 97.976 92.683 241.452 -4.376 -9.586 6.641 7.483 5.933 4.718 -30.412 40.487 9.438 -8.731 13.610 -2.544 0.000 0.000 0.000 5.537 -6.849 -4.370 -0.042 9.749 -3.797 -0.031 5.844 -4.552 0.000 0.000 0.000 0.000 -0.000 0.000 8.496 -2.489 -4.596 -0.000 0.000 -0.000 -8.532 4.168 -14.295 -8.476 9.378 14.892 17.400 3.314 -1.882 -0.000 0.000 -0.000 -3.537 10.082 -1.579 -2.775 2.683 -15.091 4.692 3.098 2.826 6.557 6.058 -4.634 6.557 6.058 -4.634 98.080 92.946 242.838 -4.376 -9.586 6.641 7.353 3.487 6.077 -31.895 44.405 10.569 -7.308 13.668 -0.981 0.000 0.000 0.000 5.565 -5.961 -4.918 0.060 9.723 -3.254 -0.391 4.886 -4.570 0.000 0.000 0.000 0.000 -0.000 0.000 8.313 -2.111 -4.534 -0.000 0.000 -0.000 -8.165 4.344 -14.112 -9.008 8.950 14.522 18.347 3.245 -1.894 -0.000 0.000 -0.000 -3.568 9.534 -0.997 -2.519 2.171 -15.008 4.767 2.768 2.710 6.702 5.843 -4.550 6.702 5.843 -4.550 98.192 93.141 244.195 -4.376 -9.586 6.641 7.019 0.948 7.406 -32.738 47.866 11.667 -5.584 13.382 0.505 0.000 0.000 0.000 5.607 -5.252 -5.250 0.179 9.798 -2.952 -0.697 4.083 -4.582 0.000 0.000 0.000 0.000 -0.000 0.000 8.158 -1.820 -4.443 -0.000 0.000 0.000 -7.865 4.576 -13.751 -9.403 8.572 14.050 19.103 2.954 -1.766 -0.000 0.000 0.000 -3.438 9.013 -0.453 -2.493 1.630 -14.987 4.918 2.262 2.588 6.785 5.703 -4.507 6.785 5.703 -4.507 98.309 93.264 245.497 -4.382 -9.534 6.421 6.616 -1.763 8.828 -32.924 50.899 12.463 -4.026 12.845 1.747 0.000 0.000 0.000 5.640 -4.729 -4.874 0.308 10.088 -3.022 -0.935 3.153 -4.625 0.000 0.000 0.000 0.000 -0.000 0.000 8.082 -1.528 -4.207 -0.000 0.000 -0.000 -7.639 4.682 -13.248 -9.650 8.203 13.624 19.662 2.577 -1.612 -0.000 0.000 -0.000 -3.333 8.366 0.050 -2.484 1.062 -14.951 4.847 1.843 2.359 6.785 5.558 -4.424 6.785 5.558 -4.424 98.431 93.331 246.751 -4.256 -9.269 6.199 6.038 -4.612 10.117 -32.447 53.444 12.704 -2.672 11.683 2.742 0.000 0.000 0.000 5.549 -4.563 -4.042 0.416 10.434 -3.401 -1.168 2.434 -4.737 0.000 0.000 0.000 -0.000 0.000 0.000 7.852 -1.432 -3.920 0.000 -0.000 -0.000 -7.417 4.789 -12.745 -9.813 7.797 13.418 19.980 2.185 -1.375 0.000 -0.000 -0.000 -3.132 7.603 0.530 -2.580 0.540 -15.085 4.770 1.460 2.109 6.786 5.412 -4.340 6.786 5.412 -4.340 98.545 93.444 247.844 -4.129 -9.003 5.977 5.460 -7.266 11.215 -30.887 55.322 12.094 -1.436 10.108 3.158 0.000 0.000 0.000 5.411 -4.374 -2.942 0.578 10.580 -3.972 -1.249 1.869 -4.969 0.000 0.000 0.000 -0.000 0.000 -0.000 7.634 -1.407 -3.667 -0.000 -0.000 0.000 -7.155 4.804 -12.426 -10.022 7.466 13.546 20.088 1.791 -1.152 -0.000 -0.000 0.000 -2.915 6.965 0.925 -2.766 -0.023 -15.259 4.685 1.135 1.932 6.703 5.312 -4.239 6.703 5.312 -4.239 98.715 93.576 248.579 -3.980 -8.570 5.846 4.805 -10.020 11.951 -28.256 56.603 10.648 -0.373 8.326 3.156 0.000 0.000 0.000 5.285 -4.306 -1.922 0.683 10.669 -4.533 -1.939 1.164 -5.136 0.000 0.000 0.000 0.000 -0.000 0.000 7.360 -1.488 -3.449 -0.000 0.000 -0.000 -6.942 4.790 -12.131 -9.988 7.021 13.761 20.025 1.600 -0.989 -0.000 0.000 -0.000 -2.596 6.243 1.231 -2.969 -0.638 -15.553 4.588 0.793 1.728 6.616 5.205 -4.178 6.616 5.205 -4.178 98.895 93.720 249.364 -3.846 -8.213 5.669 4.102 -12.427 12.449 -24.529 57.081 8.205 0.564 6.482 2.840 0.000 0.000 0.000 5.102 -4.036 -1.077 0.920 10.576 -5.159 -2.463 0.632 -5.100 0.000 0.000 0.000 -0.000 -0.000 -0.000 7.126 -1.564 -3.232 -0.000 -0.000 -0.000 -6.775 4.769 -12.038 -9.984 6.638 14.079 19.903 1.475 -0.727 -0.000 -0.000 -0.000 -2.322 5.565 1.539 -3.107 -1.213 -15.911 4.548 0.460 1.542 6.567 5.072 -4.111 6.567 5.072 -4.111 99.048 93.866 250.287 -3.732 -7.865 5.581 3.458 -14.552 12.667 -20.146 56.774 5.016 1.374 4.816 2.491 0.000 0.000 0.000 4.894 -3.666 -0.808 1.082 10.470 -5.467 -2.730 -0.054 -4.990 0.000 0.000 0.000 -0.000 -0.000 0.000 6.857 -1.753 -3.153 0.000 0.000 0.000 -6.567 4.854 -11.890 -9.900 6.274 14.307 19.628 1.458 -0.769 0.000 0.000 0.000 -1.950 5.132 1.838 -3.276 -2.007 -16.247 4.592 0.195 1.350 6.482 5.005 -4.087 6.482 5.005 -4.087 99.159 94.006 251.354 -3.713 -7.646 5.452 2.946 -16.253 12.670 -15.407 55.705 1.346 1.777 3.111 2.386 0.000 0.000 0.000 4.827 -2.961 -0.939 1.134 10.161 -5.499 -2.726 -0.666 -4.695 0.000 0.000 0.000 0.000 -0.000 -0.000 6.666 -1.736 -3.090 -0.000 -0.000 -0.000 -6.362 4.919 -11.898 -9.798 5.813 14.362 19.397 1.549 -0.713 -0.000 -0.000 -0.000 -1.692 4.597 2.239 -3.288 -2.753 -16.534 4.718 -0.037 1.161 6.431 4.870 -4.014 6.431 4.870 -4.014 99.272 94.128 252.444 -3.693 -7.427 5.323 2.560 -17.650 12.594 -10.557 53.978 -2.665 1.697 1.345 2.462 0.000 0.000 0.000 4.809 -2.277 -1.339 1.010 9.866 -5.319 -2.640 -1.261 -4.323 0.000 0.000 0.000 -0.000 -0.000 0.000 6.504 -1.805 -3.000 -0.000 0.000 -0.000 -6.245 4.966 -11.977 -9.596 5.501 14.249 19.077 1.610 -0.715 -0.000 0.000 -0.000 -1.391 4.183 2.594 -3.341 -3.411 -16.683 4.805 -0.494 0.993 6.401 4.795 -3.937 6.401 4.795 -3.937 99.383 94.255 253.547 -3.561 -7.164 5.099 2.146 -18.710 12.339 -6.403 51.431 -6.025 0.991 -0.206 2.511 0.000 0.000 0.000 4.603 -1.632 -1.754 0.897 9.415 -5.089 -2.512 -1.684 -3.860 0.000 0.000 0.000 -0.000 -0.000 0.000 6.135 -1.907 -2.932 -0.000 0.000 0.000 -5.997 4.868 -11.989 -9.488 5.428 14.069 18.747 1.609 -0.665 -0.000 0.000 0.000 -1.118 3.818 3.030 -3.259 -4.086 -16.664 4.868 -0.777 0.852 6.425 4.740 -3.855 6.425 4.740 -3.855 99.560 94.336 254.370 -3.524 -7.029 4.834 1.908 -19.468 11.993 -2.564 48.323 -9.106 -0.428 -1.397 2.477 0.000 0.000 0.000 4.497 -1.062 -2.132 0.794 9.154 -4.725 -2.386 -2.095 -3.553 0.000 0.000 0.000 -0.000 -0.000 -0.000 5.978 -1.949 -2.900 -0.000 0.000 -0.000 -5.985 4.751 -11.978 -9.201 5.529 13.890 18.303 1.478 -0.702 -0.000 0.000 -0.000 -0.954 3.560 3.551 -3.216 -4.692 -16.574 5.019 -1.047 0.689 6.374 4.660 -3.752 6.374 4.660 -3.752 99.738 94.406 255.194 -3.374 -6.852 4.473 1.577 -19.980 11.649 0.844 44.728 -11.672 -2.320 -2.430 2.467 0.000 0.000 0.000 4.347 -0.705 -2.254 0.604 9.226 -4.345 -2.140 -2.719 -3.450 0.000 0.000 0.000 -0.000 -0.000 0.000 5.709 -2.015 -2.756 0.000 -0.000 -0.000 -5.890 4.640 -12.013 -8.996 5.530 13.718 17.871 1.314 -0.615 0.000 -0.000 -0.000 -0.766 3.333 4.109 -3.158 -5.239 -16.478 5.088 -1.236 0.610 6.360 4.603 -3.623 6.360 4.603 -3.623 99.764 94.451 256.034 -3.335 -6.667 3.987 1.565 -20.275 11.445 3.659 40.875 -13.783 -4.293 -3.351 2.356 0.000 0.000 0.000 4.371 -0.355 -2.131 0.455 9.312 -3.994 -2.064 -3.293 -3.427 0.000 0.000 0.000 0.000 -0.000 -0.000 5.598 -1.980 -2.605 0.000 -0.000 -0.000 -5.921 4.404 -11.907 -8.703 5.530 13.668 17.389 1.063 -0.624 0.000 -0.000 -0.000 -0.640 2.966 4.736 -3.105 -5.639 -16.240 5.160 -1.358 0.552 6.309 4.505 -3.486 6.309 4.505 -3.486 99.786 94.477 256.889 -3.295 -6.483 3.502 1.526 -20.378 11.259 6.260 36.805 -15.509 -6.208 -3.855 2.288 0.000 0.000 0.000 4.327 -0.122 -1.862 0.363 9.585 -3.650 -1.969 -3.932 -3.544 0.000 0.000 0.000 -0.000 -0.000 0.000 5.405 -1.972 -2.527 -0.000 -0.000 0.000 -5.877 4.188 -11.729 -8.321 5.434 13.682 16.809 0.912 -0.512 -0.000 -0.000 0.000 -0.459 2.729 5.395 -3.001 -5.963 -16.035 5.232 -1.484 0.565 6.340 4.391 -3.295 6.340 4.391 -3.295 99.804 94.497 257.753 -3.312 -6.343 2.933 1.602 -20.403 11.053 8.294 32.930 -16.444 -8.064 -3.994 2.230 0.000 0.000 0.000 4.339 0.158 -1.519 0.266 9.856 -3.306 -1.988 -4.653 -3.745 0.000 0.000 0.000 -0.000 -0.000 0.000 5.275 -1.917 -2.377 -0.000 -0.000 -0.000 -5.790 3.915 -11.680 -8.003 5.370 13.828 16.231 0.759 -0.399 -0.000 -0.000 -0.000 -0.220 2.452 5.968 -2.996 -6.190 -15.829 5.268 -1.408 0.688 6.326 4.314 -3.125 6.326 4.314 -3.125 99.868 94.489 258.582 -3.426 -6.329 2.324 1.739 -20.210 10.542 9.878 29.332 -16.485 -9.796 -3.682 2.368 0.000 0.000 0.000 4.464 0.514 -1.023 0.179 10.181 -3.059 -2.099 -5.310 -3.954 0.000 0.000 0.000 -0.000 -0.000 0.000 5.267 -1.812 -2.242 -0.000 -0.000 0.000 -5.774 3.734 -11.737 -7.645 5.275 14.121 15.601 0.644 -0.341 -0.000 -0.000 0.000 0.015 2.329 6.642 -3.010 -6.330 -15.621 5.202 -1.314 0.637 6.327 4.267 -2.953 6.327 4.267 -2.953 99.959 94.488 259.447 -3.454 -6.490 1.748 1.796 -19.751 9.871 10.979 26.254 -15.620 -11.120 -3.322 2.329 0.000 0.000 0.000 4.420 1.099 -0.626 0.231 10.461 -2.719 -2.244 -5.972 -4.123 0.000 0.000 0.000 0.000 0.000 -0.000 5.157 -1.459 -2.112 -0.000 0.000 -0.000 -5.703 3.389 -11.934 -7.266 5.279 14.434 14.945 0.509 -0.146 -0.000 0.000 -0.000 0.263 2.399 7.179 -3.049 -6.594 -15.364 5.239 -1.216 0.648 6.351 4.213 -2.756 6.351 4.213 -2.756 100.081 94.481 260.376 -3.484 -6.651 1.172 1.788 -19.278 8.996 11.984 23.630 -14.221 -12.517 -2.979 2.433 0.000 0.000 0.000 4.376 1.816 -0.309 0.184 10.604 -2.321 -2.013 -6.609 -4.312 0.000 0.000 0.000 -0.000 -0.000 -0.000 5.096 -1.261 -1.989 -0.000 -0.000 -0.000 -5.759 3.228 -12.093 -6.982 5.301 14.571 14.481 0.337 0.017 -0.000 -0.000 -0.000 0.362 2.892 7.672 -3.045 -7.045 -15.178 5.265 -1.149 0.691 6.325 4.263 -2.597 6.325 4.263 -2.597 100.230 94.469 261.323 -3.515 -6.812 0.595 1.765 -18.659 8.175 12.767 21.334 -12.480 -13.810 -2.576 2.498 0.000 0.000 0.000 4.323 2.532 0.009 0.203 10.752 -1.896 -1.890 -7.331 -4.460 0.000 0.000 0.000 -0.000 -0.000 0.000 5.106 -1.036 -1.944 -0.000 -0.000 -0.000 -5.930 2.964 -12.259 -6.694 5.487 14.674 13.964 0.138 0.143 -0.000 -0.000 -0.000 0.431 3.237 8.289 -3.055 -7.142 -15.030 5.216 -1.077 0.782 6.279 4.274 -2.369 6.279 4.274 -2.369 100.406 94.455 262.303 -3.487 -6.931 0.101 1.653 -18.050 7.503 13.454 19.307 -10.872 -15.018 -1.874 2.551 0.000 0.000 0.000 4.257 3.189 0.188 0.079 10.907 -1.430 -1.815 -7.979 -4.618 0.000 0.000 0.000 -0.000 -0.000 0.000 5.106 -1.011 -1.979 -0.000 0.000 -0.000 -6.159 2.849 -12.402 -6.408 5.676 14.775 13.539 -0.115 0.102 -0.000 0.000 -0.000 0.437 3.629 8.653 -3.050 -7.073 -14.585 5.059 -0.969 0.862 6.182 4.388 -2.178 6.182 4.388 -2.178 100.550 94.430 263.218 -3.585 -6.953 -0.383 1.782 -17.427 7.053 13.875 17.620 -9.545 -16.212 -1.356 2.588 0.000 0.000 0.000 4.316 3.822 0.408 -0.135 10.949 -0.975 -1.775 -8.668 -4.899 0.000 0.000 0.000 0.000 -0.000 -0.000 5.272 -1.167 -1.854 -0.000 -0.000 -0.000 -6.416 2.862 -12.435 -6.104 5.952 14.596 13.140 -0.390 0.152 -0.000 -0.000 -0.000 0.463 4.062 8.754 -3.164 -6.769 -14.185 5.051 -0.934 0.943 5.962 4.530 -2.075 5.962 4.530 -2.075 100.764 94.383 264.139 -3.662 -6.903 -0.811 1.980 -16.849 6.920 13.893 16.324 -8.602 -17.092 -1.097 2.534 0.000 0.000 0.000 4.288 4.298 0.394 -0.337 11.163 -0.457 -1.743 -9.381 -4.933 0.000 0.000 0.000 -0.000 -0.000 -0.000 5.440 -1.467 -1.806 -0.000 -0.000 0.000 -6.647 2.914 -12.281 -5.833 6.222 14.453 12.933 -0.516 0.148 -0.000 -0.000 0.000 0.427 4.608 8.616 -3.161 -6.467 -13.685 5.054 -0.967 1.017 5.679 4.742 -1.980 5.679 4.742 -1.980 100.957 94.325 265.105 -3.730 -6.757 -1.200 2.125 -16.312 6.937 13.863 15.160 -8.137 -17.794 -0.879 2.309 0.000 0.000 0.000 4.241 4.744 0.412 -0.525 11.306 -0.002 -1.601 -10.089 -5.073 0.000 0.000 0.000 0.000 -0.000 -0.000 5.616 -1.876 -1.731 -0.000 -0.000 -0.000 -6.647 2.996 -12.010 -5.845 6.400 14.366 12.755 -0.559 0.142 -0.000 -0.000 -0.000 0.329 5.232 8.349 -3.078 -6.249 -13.467 4.869 -0.832 1.187 5.405 4.948 -1.858 5.405 4.948 -1.858 101.109 94.270 266.074 -3.848 -6.557 -1.633 2.214 -15.675 7.160 13.876 13.910 -8.380 -18.191 -0.572 2.375 0.000 0.000 0.000 4.246 5.269 0.394 -0.697 11.161 0.520 -1.459 -10.640 -5.120 0.000 0.000 0.000 -0.000 0.000 -0.000 5.835 -2.321 -1.667 -0.000 -0.000 -0.000 -6.788 3.084 -11.625 -5.675 6.469 14.510 12.476 -0.479 0.091 -0.000 -0.000 -0.000 0.227 5.761 8.069 -2.983 -5.858 -13.291 4.827 -0.659 1.298 5.190 5.152 -1.767 5.190 5.152 -1.767 101.267 94.183 267.061 -3.942 -6.285 -2.008 2.278 -15.024 7.200 13.711 12.595 -8.844 -17.970 0.164 2.772 0.000 0.000 0.000 4.229 5.646 0.267 -0.893 11.165 0.928 -1.281 -11.082 -5.020 0.000 0.000 0.000 -0.000 0.000 0.000 6.015 -2.771 -1.618 -0.000 -0.000 -0.000 -6.723 3.238 -11.318 -5.657 6.360 14.694 12.246 -0.437 0.197 -0.000 -0.000 -0.000 0.041 6.326 7.776 -2.783 -5.566 -13.270 4.795 -0.414 1.423 5.101 5.318 -1.692 5.101 5.318 -1.692 101.521 94.099 268.089 -3.945 -6.098 -2.314 2.209 -14.250 6.886 13.426 11.363 -9.244 -17.136 1.177 3.615 0.000 0.000 0.000 4.058 6.176 0.211 -1.073 11.075 1.135 -1.014 -11.509 -4.832 0.000 0.000 0.000 -0.000 -0.000 -0.000 6.102 -3.145 -1.635 0.000 -0.000 -0.000 -6.740 3.385 -10.963 -5.548 6.254 14.995 11.938 -0.349 0.182 0.000 -0.000 -0.000 -0.104 6.876 7.588 -2.553 -5.115 -13.339 4.640 -0.269 1.521 5.079 5.480 -1.625 5.079 5.480 -1.625 101.758 93.997 269.130 -3.948 -5.910 -2.621 2.055 -13.580 6.114 13.051 10.518 -9.060 -16.126 1.981 4.374 0.000 0.000 0.000 3.884 6.704 0.156 -1.254 10.983 1.340 -0.671 -11.856 -4.627 0.000 0.000 0.000 -0.000 -0.000 -0.000 6.063 -3.398 -1.568 0.000 -0.000 0.000 -6.649 3.400 -10.830 -5.513 6.174 15.352 11.748 -0.099 0.199 0.000 -0.000 0.000 -0.179 7.264 7.333 -2.332 -4.594 -13.368 4.629 0.025 1.718 5.151 5.610 -1.620 5.151 5.610 -1.620 102.036 93.909 270.152 -3.971 -5.734 -2.827 1.889 -12.972 4.862 12.613 9.919 -8.286 -15.116 2.713 5.002 0.000 0.000 0.000 3.742 7.237 -0.002 -1.521 10.860 1.629 -0.183 -12.094 -4.476 0.000 0.000 0.000 -0.000 -0.000 0.000 6.040 -3.650 -1.604 -0.000 -0.000 -0.000 -6.557 3.414 -10.697 -5.563 6.111 15.613 11.670 0.019 0.220 -0.000 -0.000 -0.000 -0.244 7.733 7.148 -2.228 -4.076 -13.344 4.519 0.448 1.853 5.292 5.738 -1.624 5.292 5.738 -1.624 102.348 93.876 271.144 -3.905 -5.642 -2.968 1.577 -12.486 3.420 12.202 9.654 -7.035 -14.259 3.283 5.238 0.000 0.000 0.000 3.509 7.791 -0.084 -1.769 10.891 1.646 0.453 -12.304 -4.153 0.000 0.000 0.000 -0.000 -0.000 0.000 5.980 -3.730 -1.601 -0.000 -0.000 -0.000 -6.562 3.238 -10.726 -5.607 6.251 15.810 11.649 0.143 0.196 -0.000 -0.000 -0.000 -0.438 8.031 6.847 -2.114 -3.299 -13.166 4.519 0.731 2.077 5.399 5.755 -1.670 5.399 5.755 -1.670 102.636 93.869 272.136 -3.789 -5.605 -3.065 1.341 -11.979 1.863 11.678 9.532 -5.541 -13.579 3.641 5.377 0.000 0.000 0.000 3.236 8.268 -0.130 -2.120 11.087 1.657 1.249 -12.320 -3.821 0.000 0.000 0.000 -0.000 0.000 -0.000 5.779 -3.777 -1.618 -0.000 -0.000 0.000 -6.472 3.121 -10.817 -5.668 6.372 15.881 11.682 0.140 0.131 -0.000 -0.000 0.000 -0.456 8.419 6.531 -2.151 -2.630 -12.988 4.427 1.292 2.292 5.599 5.805 -1.768 5.599 5.805 -1.768 102.917 93.857 273.114 -3.667 -5.705 -3.076 1.140 -11.236 0.510 10.995 9.251 -4.110 -12.920 3.875 5.429 0.000 0.000 0.000 3.034 8.731 -0.467 -2.591 11.519 1.733 2.148 -12.304 -3.398 0.000 0.000 0.000 -0.000 -0.000 0.000 5.493 -3.743 -1.756 -0.000 -0.000 -0.000 -6.380 3.034 -10.994 -5.607 6.529 15.978 11.633 0.263 0.028 -0.000 -0.000 -0.000 -0.499 8.782 6.220 -2.111 -1.805 -12.895 4.354 1.767 2.632 5.780 5.855 -1.822 5.780 5.855 -1.822 103.264 93.862 274.038 -3.551 -5.669 -3.172 1.020 -10.677 -0.288 10.349 8.972 -3.320 -12.344 3.905 5.625 0.000 0.000 0.000 2.711 8.855 -0.743 -3.058 12.204 1.789 3.255 -12.090 -2.714 0.000 0.000 0.000 -0.000 0.000 -0.000 5.306 -3.805 -1.721 0.000 0.000 -0.000 -6.302 2.937 -11.136 -5.600 6.756 15.959 11.531 0.133 -0.009 0.000 0.000 -0.000 -0.599 9.196 5.907 -2.123 -1.240 -12.801 4.347 2.377 2.846 5.885 5.880 -1.911 5.885 5.880 -1.911 103.722 93.862 274.998 -3.440 -5.498 -3.354 0.991 -10.033 -0.621 9.705 8.236 -2.852 -11.744 4.138 5.988 0.000 0.000 0.000 2.334 8.694 -1.175 -3.687 13.222 2.055 4.531 -11.856 -1.850 0.000 0.000 0.000 0.000 -0.000 -0.000 5.153 -4.062 -1.771 -0.000 -0.000 -0.000 -6.342 2.968 -11.100 -5.479 6.837 15.951 11.446 0.085 -0.065 -0.000 -0.000 -0.000 -0.893 9.639 5.865 -2.024 -0.737 -12.808 4.288 3.033 3.086 5.989 5.924 -1.887 5.989 5.924 -1.887 104.260 93.848 276.054 -3.462 -5.322 -3.561 1.160 -9.230 -0.521 9.064 7.270 -2.784 -11.221 4.233 6.244 0.000 0.000 0.000 2.088 8.384 -1.921 -4.471 14.550 2.585 5.767 -11.450 -0.932 0.000 0.000 0.000 0.000 -0.000 0.000 5.133 -4.315 -1.810 -0.000 -0.000 -0.000 -6.249 2.983 -10.969 -5.384 6.840 15.876 11.110 0.038 -0.028 -0.000 -0.000 -0.000 -1.189 10.082 5.826 -1.919 -0.333 -12.697 4.319 3.553 3.180 6.037 5.971 -1.917 6.037 5.971 -1.917 104.867 93.977 277.034 -3.428 -4.971 -3.772 1.244 -8.628 -0.328 8.576 6.326 -2.600 -10.643 4.352 6.400 0.000 0.000 0.000 1.744 7.617 -2.825 -5.377 16.272 3.379 6.884 -10.986 0.067 0.000 0.000 0.000 -0.000 -0.000 0.000 5.012 -4.596 -1.819 -0.000 0.000 0.000 -6.171 2.844 -10.814 -5.131 6.943 15.853 10.630 -0.147 -0.024 -0.000 0.000 0.000 -1.430 10.296 5.707 -1.834 0.062 -12.555 4.387 3.814 3.399 6.139 5.916 -1.909 6.139 5.916 -1.909 105.141 94.180 277.807 -3.368 -4.608 -4.085 1.296 -8.028 -0.048 7.953 5.469 -2.232 -9.846 4.484 6.237 0.000 0.000 0.000 1.434 6.569 -3.750 -6.628 18.371 4.368 7.924 -10.225 1.001 0.000 0.000 0.000 0.000 -0.000 0.000 4.879 -4.882 -1.725 0.000 -0.000 -0.000 -6.054 2.771 -10.575 -4.790 6.820 15.775 10.026 -0.216 0.054 0.000 -0.000 -0.000 -1.670 10.374 5.495 -1.764 0.336 -12.427 4.400 4.001 3.560 6.219 5.945 -1.870 6.219 5.945 -1.870 105.411 94.342 278.533 -3.331 -4.256 -4.297 1.366 -7.545 0.057 7.406 4.663 -1.757 -9.225 4.625 6.099 0.000 0.000 0.000 1.081 5.328 -4.902 -7.920 20.718 5.498 8.652 -9.168 1.965 0.000 0.000 0.000 0.000 0.000 0.000 4.762 -5.165 -1.736 -0.000 0.000 -0.000 -5.952 2.787 -10.396 -4.424 6.607 15.752 9.422 -0.285 0.133 -0.000 0.000 -0.000 -1.849 10.420 5.182 -1.787 0.560 -12.253 4.305 3.843 3.572 6.321 5.891 -1.863 6.321 5.891 -1.863 105.668 94.486 279.131 -3.292 -3.905 -4.510 1.397 -7.165 -0.123 6.864 4.062 -1.194 -8.550 4.639 6.059 0.000 0.000 0.000 0.714 3.894 -6.050 -9.414 23.291 6.790 9.196 -7.911 2.751 0.000 0.000 0.000 -0.000 -0.000 -0.000 4.608 -5.366 -1.772 -0.000 0.000 0.000 -5.769 2.666 -10.338 -4.131 6.518 15.863 8.895 -0.304 0.241 -0.000 0.000 0.000 -1.991 10.386 4.887 -1.724 0.684 -12.318 4.164 3.448 3.469 6.454 5.855 -1.841 6.454 5.855 -1.841 105.919 94.573 279.517 -3.207 -3.475 -4.763 1.345 -7.059 -0.398 6.451 3.574 -0.619 -7.966 4.726 6.115 0.000 0.000 0.000 0.279 2.115 -7.218 -11.191 26.134 8.374 9.460 -6.447 3.540 0.000 0.000 0.000 -0.000 -0.000 -0.000 4.421 -5.647 -1.759 0.000 -0.000 -0.000 -5.558 2.580 -10.473 -3.902 6.475 16.037 8.429 -0.345 0.338 0.000 -0.000 -0.000 -2.133 10.352 4.591 -1.636 0.610 -12.529 3.932 2.951 3.195 6.575 5.764 -1.816 6.575 5.764 -1.816 106.172 94.636 279.802 -3.165 -3.124 -4.975 1.270 -7.010 -0.739 6.176 3.218 -0.142 -7.504 4.794 6.211 0.000 0.000 0.000 0.002 0.357 -8.439 -13.264 28.851 10.092 9.337 -4.616 4.261 0.000 0.000 0.000 -0.000 0.000 0.000 4.140 -5.745 -1.825 0.000 0.000 -0.000 -5.197 2.388 -10.759 -3.880 6.426 16.235 8.177 -0.520 0.352 0.000 0.000 -0.000 -2.064 10.209 4.251 -1.506 0.537 -12.893 3.692 2.275 2.937 6.738 5.596 -1.746 6.738 5.596 -1.746

X3D0.Scene = Scene28
f = open("././BvhConversion1Illustrated_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
