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
meta3.content = "DiamondManLOA1.x3d"

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.name = "description"
meta4.content = "HAnim skeletal structure for Level of Action (LOA) one, with diamonds at the Joint centers. LOA-1 is typical low-end real-time 3D hierarchy."

head1.children.append(meta4)
meta5 = x3d.meta()
meta5.name = "creator"
meta5.content = "Matthew T. Beitler"

head1.children.append(meta5)
meta6 = x3d.meta()
meta6.name = "translator"
meta6.content = "Joel S. Pawloski"

head1.children.append(meta6)
meta7 = x3d.meta()
meta7.name = "created"
meta7.content = "12 November 2001"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.name = "modified"
meta8.content = "23 December 2021"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "Image"
meta9.content = "images/BonesAllSkeletonFrontViewLOA1.png"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "motto"
meta10.content = "(a) \"Diamonds are a girl's best friend.\" (b) \"Gosh, it sure is chilly in here.\""

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.name = "warning"
meta11.content = "Still needs comments on CAESAR feature points inserted"

head1.children.append(meta11)
meta12 = x3d.meta()
meta12.name = "reference"
meta12.content = "HAnim 1.1 specification, Appendix A: Suggested Body Dimensions and Levels of Articulation, Level of Articulation Two"

head1.children.append(meta12)
meta13 = x3d.meta()
meta13.name = "reference"
meta13.content = "http://HAnim.org/Specifications/HAnim1.1/appendices.html#appendixa"

head1.children.append(meta13)
meta14 = x3d.meta()
meta14.name = "reference"
meta14.content = "http://HAnim.org/Specifications/HAnim1.1/JointCenters1_1_LOA1.wrl"

head1.children.append(meta14)
meta15 = x3d.meta()
meta15.name = "reference"
meta15.content = "http://HAnim.org/Specifications/HAnim1.1/JointCenters1_1_LOA1-diamond.wrl"

head1.children.append(meta15)
meta16 = x3d.meta()
meta16.name = "reference"
meta16.content = "http://ece.uwaterloo.ca/~HAnim"

head1.children.append(meta16)
meta17 = x3d.meta()
meta17.name = "reference"
meta17.content = "http://www.cis.upenn.edu/~badler/anthro/89-71.pdf"

head1.children.append(meta17)
meta18 = x3d.meta()
meta18.name = "reference"
meta18.content = "http://www.cis.upenn.edu/~badler/anthro/89-71.ps"

head1.children.append(meta18)
meta19 = x3d.meta()
meta19.name = "reference"
meta19.content = "http://www.cis.upenn.edu/~beitler"

head1.children.append(meta19)
meta20 = x3d.meta()
meta20.name = "Image"
meta20.content = "humanoid_landmark_locations.gif"

head1.children.append(meta20)
meta21 = x3d.meta()
meta21.name = "Image"
meta21.content = "http://HAnim.org/Specifications/HAnim1.1/humanoid_landmark_locations.gif"

head1.children.append(meta21)
meta22 = x3d.meta()
meta22.name = "identifier"
meta22.content = "https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Templates/DiamondManLOA1.x3d"

head1.children.append(meta22)
meta23 = x3d.meta()
meta23.name = "generator"
meta23.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"

head1.children.append(meta23)
meta24 = x3d.meta()
meta24.name = "generator"
meta24.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"

head1.children.append(meta24)
meta25 = x3d.meta()
meta25.name = "license"
meta25.content = "../license.html"

head1.children.append(meta25)

X3D0.head = head1
Scene26 = x3d.Scene()
WorldInfo27 = x3d.WorldInfo()
WorldInfo27.info = ["HAnim 2.0 Default Joint Centers, Level Of Articulation (LOA) 1 -------------------------------------------------------- HANIM 1.1 (VRML 2.0) Author name: eMpTy (a.k.a. Matthew T. Beitler) HANIM 1.1 (VRML 2.0) Author email: beitler@graphics.cis.upenn.edu or beitler@acm.org HANIM 1.1 (VRML 2.0) Author homepage: http://www.cis.upenn.edu/~beitler HANIM 1.1 (VRML 2.0) Compliance Date: May 12, 1999 HANIM 1.1 Compliance Information: http://ece.uwaterloo.ca/~HAnim/ Construction Info (joint centers): The joint centers of this figure are based on the work of Norman Badler, director of the Center for Human Modeling and Simulation at the University of Pennsylvania. The original document which these joint centers are based on can be found at: http://www.cis.upenn.edu/~badler/anthro/89-71.ps, .pdf"]
WorldInfo27.title = "HANIM 1.1 Default Joint Centers, LOA1"

Scene26.children.append(WorldInfo27)
NavigationInfo28 = x3d.NavigationInfo()
NavigationInfo28.speed = 1.5

Scene26.children.append(NavigationInfo28)
Viewpoint29 = x3d.Viewpoint()
Viewpoint29.centerOfRotation = [0,1,0]
Viewpoint29.description = "Diamond Man, LOA 1"
Viewpoint29.position = [0,1,3]

Scene26.children.append(Viewpoint29)
HAnimHumanoid30 = x3d.HAnimHumanoid()
HAnimHumanoid30.name = "humanoid"
HAnimHumanoid30.DEF = "hanim_humanoid"
HAnimHumanoid30.loa = 1
HAnimHumanoid30.version = "2.0"
#original HAnimHumanoid info='\"authorEmail=beitler@graphics.cis.upenn.edu beitler@acm.org\" \"authorName=Matthew T. Beitler\" \"copyright=Copyright 1999 Matthew T. Beitler\" \"humanoidVersion=JointCenters 1.1 LOA1\" \"usageRestrictions=PERMISSION TO FULLY USE THIS SCENE GRAPH IS GRANTED PROVIDED THIS COPYRIGHT INFORMATION AND DOCUMENTATION OF THE ORIGINAL AUTHOR IS INCLUDED. This humanoid scene graph is provided _as-is_ and without warranty of any kind express implied or otherwise including without limitation any warranty of merchantability or fitness for a particular purpose.\"'
MetadataSet31 = x3d.MetadataSet()
MetadataSet31.name = "HAnimHumanoid.info"
MetadataSet31.reference = "https://www.web3d.org/documents/specifications/19774/V2.0/Architecture/ObjectInterfaces.html#Humanoid"
MetadataString32 = x3d.MetadataString()
MetadataString32.name = "authorEmail"
MetadataString32.value = ["beitler@graphics.cis.upenn.edu beitler@acm.org"]

if MetadataSet31.value is None:
    MetadataSet31.value = []
MetadataSet31.value.append(MetadataString32)
MetadataString33 = x3d.MetadataString()
MetadataString33.name = "authorName"
MetadataString33.value = ["Matthew T. Beitler"]

if MetadataSet31.value is None:
    MetadataSet31.value = []
MetadataSet31.value.append(MetadataString33)
MetadataString34 = x3d.MetadataString()
MetadataString34.name = "copyright"
MetadataString34.value = ["Copyright 1999 Matthew T. Beitler"]

if MetadataSet31.value is None:
    MetadataSet31.value = []
MetadataSet31.value.append(MetadataString34)
MetadataString35 = x3d.MetadataString()
MetadataString35.name = "humanoidVersion"
MetadataString35.value = ["JointCenters 1.1 LOA1"]

if MetadataSet31.value is None:
    MetadataSet31.value = []
MetadataSet31.value.append(MetadataString35)
MetadataString36 = x3d.MetadataString()
MetadataString36.name = "usageRestrictions"
MetadataString36.value = ["PERMISSION TO FULLY USE THIS SCENE GRAPH IS GRANTED PROVIDED THIS COPYRIGHT INFORMATION AND DOCUMENTATION OF THE ORIGINAL AUTHOR IS INCLUDED. This humanoid scene graph is provided _as-is_ and without warranty of any kind express implied or otherwise including without limitation any warranty of merchantability or fitness for a particular purpose."]

if MetadataSet31.value is None:
    MetadataSet31.value = []
MetadataSet31.value.append(MetadataString36)

HAnimHumanoid30.metadata = MetadataSet31
HAnimJoint37 = x3d.HAnimJoint()
HAnimJoint37.name = "humanoid_root"
HAnimJoint37.DEF = "hanim_humanoid_root"
HAnimJoint37.center = [0,0.824,0.0277]
HAnimJoint37.ulimit = [0,0,0]
HAnimJoint37.llimit = [0,0,0]
HAnimJoint38 = x3d.HAnimJoint()
HAnimJoint38.name = "sacroiliac"
HAnimJoint38.DEF = "hanim_sacroiliac"
HAnimJoint38.center = [0,0.9149,0.0016]
HAnimJoint38.ulimit = [0,0,0]
HAnimJoint38.llimit = [0,0,0]
HAnimSegment39 = x3d.HAnimSegment()
HAnimSegment39.name = "pelvis"
HAnimSegment39.DEF = "hanim_pelvis"
Transform40 = x3d.Transform()
Transform40.translation = [0,0.9149,0.0016]
Shape41 = x3d.Shape()
Shape41.DEF = "DiamondShape"
IndexedFaceSet42 = x3d.IndexedFaceSet()
IndexedFaceSet42.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet42.creaseAngle = 0.5
Coordinate43 = x3d.Coordinate()
Coordinate43.DEF = "points"

IndexedFaceSet42.coord = Coordinate43

Shape41.geometry = IndexedFaceSet42
Appearance44 = x3d.Appearance()
Material45 = x3d.Material()
Material45.diffuseColor = [1,1,0]

Appearance44.material = Material45

Shape41.appearance = Appearance44

Transform40.children.append(Shape41)

HAnimSegment39.children.append(Transform40)

HAnimJoint38.children.append(HAnimSegment39)
HAnimJoint46 = x3d.HAnimJoint()
HAnimJoint46.name = "l_hip"
HAnimJoint46.DEF = "hanim_l_hip"
HAnimJoint46.center = [0.0961,0.9124,-0.0001]
HAnimJoint46.ulimit = [0,0,0]
HAnimJoint46.llimit = [0,0,0]
HAnimSegment47 = x3d.HAnimSegment()
HAnimSegment47.name = "l_thigh"
HAnimSegment47.DEF = "hanim_l_thigh"
Transform48 = x3d.Transform()
Transform48.translation = [0.0961,0.9124,-0.0001]
Shape49 = x3d.Shape()
Shape49.USE = "DiamondShape"

Transform48.children.append(Shape49)

HAnimSegment47.children.append(Transform48)
HAnimSite50 = x3d.HAnimSite()
HAnimSite50.name = "l_knee_crease_pt"
HAnimSite50.DEF = "hanim_l_knee_crease_pt"
HAnimSite50.translation = [0.0993,0.4881,-0.0309]

HAnimSegment47.children.append(HAnimSite50)
HAnimSite51 = x3d.HAnimSite()
HAnimSite51.name = "l_femoral_lateral_epicondyle_pt"
HAnimSite51.DEF = "hanim_l_femoral_lateral_epicondyle_pt"
HAnimSite51.translation = [0.1598,0.4967,0.0297]

HAnimSegment47.children.append(HAnimSite51)
HAnimSite52 = x3d.HAnimSite()
HAnimSite52.name = "l_femoral_medial_epicondyle_pt"
HAnimSite52.DEF = "hanim_l_femoral_medial_epicondyle_pt"
HAnimSite52.translation = [0.0398,0.4946,0.0303]

HAnimSegment47.children.append(HAnimSite52)

HAnimJoint46.children.append(HAnimSegment47)
HAnimJoint53 = x3d.HAnimJoint()
HAnimJoint53.name = "l_knee"
HAnimJoint53.DEF = "hanim_l_knee"
HAnimJoint53.center = [0.104,0.4867,0.0308]
HAnimJoint53.ulimit = [0,0,0]
HAnimJoint53.llimit = [0,0,0]
HAnimSegment54 = x3d.HAnimSegment()
HAnimSegment54.name = "l_calf"
HAnimSegment54.DEF = "hanim_l_calf"
Transform55 = x3d.Transform()
Transform55.translation = [0.104,0.4867,0.0308]
Shape56 = x3d.Shape()
Shape56.USE = "DiamondShape"

Transform55.children.append(Shape56)

HAnimSegment54.children.append(Transform55)

HAnimJoint53.children.append(HAnimSegment54)
HAnimJoint57 = x3d.HAnimJoint()
HAnimJoint57.name = "l_talocrural"
HAnimJoint57.DEF = "hanim_l_talocrural"
HAnimJoint57.center = [0.1101,0.0656,-0.0736]
HAnimJoint57.ulimit = [0,0,0]
HAnimJoint57.llimit = [0,0,0]
HAnimSegment58 = x3d.HAnimSegment()
HAnimSegment58.name = "l_talus"
HAnimSegment58.DEF = "hanim_l_talus"
Transform59 = x3d.Transform()
Transform59.translation = [0.1101,0.0656,-0.0736]
Shape60 = x3d.Shape()
Shape60.USE = "DiamondShape"

Transform59.children.append(Shape60)

HAnimSegment58.children.append(Transform59)
HAnimSite61 = x3d.HAnimSite()
HAnimSite61.name = "l_lateral_malleolus_pt"
HAnimSite61.DEF = "hanim_l_lateral_malleolus_pt"
HAnimSite61.translation = [0.1308,0.0597,-0.1032]

HAnimSegment58.children.append(HAnimSite61)
HAnimSite62 = x3d.HAnimSite()
HAnimSite62.name = "l_medial_malleolus_pt"
HAnimSite62.DEF = "hanim_l_medial_malleolus_pt"
HAnimSite62.translation = [0.089,0.0716,-0.0881]

HAnimSegment58.children.append(HAnimSite62)
HAnimSite63 = x3d.HAnimSite()
HAnimSite63.name = "l_sphyrion_pt"
HAnimSite63.DEF = "hanim_l_sphyrion_pt"
HAnimSite63.translation = [0.089,0.0575,-0.0943]

HAnimSegment58.children.append(HAnimSite63)
HAnimSite64 = x3d.HAnimSite()
HAnimSite64.name = "l_calcaneus_posterior_pt"
HAnimSite64.DEF = "hanim_l_calcaneus_posterior_pt"
HAnimSite64.translation = [0.0974,0.0259,-0.1171]

HAnimSegment58.children.append(HAnimSite64)

HAnimJoint57.children.append(HAnimSegment58)
HAnimJoint65 = x3d.HAnimJoint()
HAnimJoint65.name = "l_metatarsophalangeal_2"
HAnimJoint65.DEF = "hanim_l_metatarsophalangeal_2"
HAnimJoint65.center = [0.1086,0.0001,0.0368]
HAnimJoint65.ulimit = [0,0,0]
HAnimJoint65.llimit = [0,0,0]
HAnimSegment66 = x3d.HAnimSegment()
HAnimSegment66.name = "l_tarsal_proximal_phalanx_2"
HAnimSegment66.DEF = "hanim_l_tarsal_proximal_phalanx_2"
HAnimSite67 = x3d.HAnimSite()
HAnimSite67.name = "l_middistal_tip"
HAnimSite67.DEF = "hanim_l_middistal_tip"
HAnimSite67.translation = [0.1354,0.0016,0.1476]

HAnimSegment66.children.append(HAnimSite67)
HAnimSite68 = x3d.HAnimSite()
HAnimSite68.name = "l_metatarsal_phalanx_5_pt"
HAnimSite68.DEF = "hanim_l_metatarsal_phalanx_5_pt"
HAnimSite68.translation = [0.1825,0.007,0.0928]

HAnimSegment66.children.append(HAnimSite68)
HAnimSite69 = x3d.HAnimSite()
HAnimSite69.name = "l_metatarsal_phalanx_1_pt"
HAnimSite69.DEF = "hanim_l_metatarsal_phalanx_1_pt"
HAnimSite69.translation = [0.0816,0.0232,0.0106]

HAnimSegment66.children.append(HAnimSite69)
HAnimSite70 = x3d.HAnimSite()
HAnimSite70.name = "l_tarsal_distal_phalanx_2_pt"
HAnimSite70.DEF = "hanim_l_tarsal_distal_phalanx_2_pt"
HAnimSite70.translation = [0.1195,0.0079,0.1433]

HAnimSegment66.children.append(HAnimSite70)

HAnimJoint65.children.append(HAnimSegment66)

HAnimJoint57.children.append(HAnimJoint65)

HAnimJoint53.children.append(HAnimJoint57)

HAnimJoint46.children.append(HAnimJoint53)

HAnimJoint38.children.append(HAnimJoint46)
HAnimJoint71 = x3d.HAnimJoint()
HAnimJoint71.name = "r_hip"
HAnimJoint71.DEF = "hanim_r_hip"
HAnimJoint71.center = [-0.095,0.9171,0.0029]
HAnimJoint71.ulimit = [0,0,0]
HAnimJoint71.llimit = [0,0,0]
HAnimSegment72 = x3d.HAnimSegment()
HAnimSegment72.name = "r_thigh"
HAnimSegment72.DEF = "hanim_r_thigh"
Transform73 = x3d.Transform()
Transform73.translation = [-0.095,0.9171,0.0029]
Shape74 = x3d.Shape()
Shape74.USE = "DiamondShape"

Transform73.children.append(Shape74)

HAnimSegment72.children.append(Transform73)
HAnimSite75 = x3d.HAnimSite()
HAnimSite75.name = "r_knee_crease_pt"
HAnimSite75.DEF = "hanim_r_knee_crease_pt"
HAnimSite75.translation = [-0.0825,0.4932,-0.0326]

HAnimSegment72.children.append(HAnimSite75)
HAnimSite76 = x3d.HAnimSite()
HAnimSite76.name = "r_femoral_lateral_epicondyle_pt"
HAnimSite76.DEF = "hanim_r_femoral_lateral_epicondyle_pt"
HAnimSite76.translation = [-0.1421,0.4992,0.031]

HAnimSegment72.children.append(HAnimSite76)
HAnimSite77 = x3d.HAnimSite()
HAnimSite77.name = "r_femoral_medial_epicondyle_pt"
HAnimSite77.DEF = "hanim_r_femoral_medial_epicondyle_pt"
HAnimSite77.translation = [-0.0221,0.5014,0.0289]

HAnimSegment72.children.append(HAnimSite77)

HAnimJoint71.children.append(HAnimSegment72)
HAnimJoint78 = x3d.HAnimJoint()
HAnimJoint78.name = "r_knee"
HAnimJoint78.DEF = "hanim_r_knee"
HAnimJoint78.center = [-0.0867,0.4913,0.0318]
HAnimJoint78.ulimit = [0,0,0]
HAnimJoint78.llimit = [0,0,0]
HAnimSegment79 = x3d.HAnimSegment()
HAnimSegment79.name = "r_calf"
HAnimSegment79.DEF = "hanim_r_calf"
Transform80 = x3d.Transform()
Transform80.translation = [-0.0867,0.4913,0.0318]
Shape81 = x3d.Shape()
Shape81.USE = "DiamondShape"

Transform80.children.append(Shape81)

HAnimSegment79.children.append(Transform80)

HAnimJoint78.children.append(HAnimSegment79)
HAnimJoint82 = x3d.HAnimJoint()
HAnimJoint82.name = "r_talocrural"
HAnimJoint82.DEF = "hanim_r_talocrural"
HAnimJoint82.center = [-0.0801,0.0712,-0.0766]
HAnimJoint82.ulimit = [0,0,0]
HAnimJoint82.llimit = [0,0,0]
HAnimSegment83 = x3d.HAnimSegment()
HAnimSegment83.name = "r_talus"
HAnimSegment83.DEF = "hanim_r_talus"
Transform84 = x3d.Transform()
Transform84.translation = [-0.0801,0.0712,-0.0766]
Shape85 = x3d.Shape()
Shape85.USE = "DiamondShape"

Transform84.children.append(Shape85)

HAnimSegment83.children.append(Transform84)
HAnimSite86 = x3d.HAnimSite()
HAnimSite86.name = "r_lateral_malleolus_pt"
HAnimSite86.DEF = "hanim_r_lateral_malleolus_pt"
HAnimSite86.translation = [-0.1006,0.0658,-0.1075]

HAnimSegment83.children.append(HAnimSite86)
HAnimSite87 = x3d.HAnimSite()
HAnimSite87.name = "r_medial_malleolus_pt"
HAnimSite87.DEF = "hanim_r_medial_malleolus_pt"
HAnimSite87.translation = [-0.0591,0.076,-0.0928]

HAnimSegment83.children.append(HAnimSite87)
HAnimSite88 = x3d.HAnimSite()
HAnimSite88.name = "r_sphyrion_pt"
HAnimSite88.DEF = "hanim_r_sphyrion_pt"
HAnimSite88.translation = [-0.0603,0.061,-0.1002]

HAnimSegment83.children.append(HAnimSite88)
HAnimSite89 = x3d.HAnimSite()
HAnimSite89.name = "r_calcaneus_posterior_pt"
HAnimSite89.DEF = "hanim_r_calcaneus_posterior_pt"
HAnimSite89.translation = [-0.0692,0.0297,-0.1221]

HAnimSegment83.children.append(HAnimSite89)

HAnimJoint82.children.append(HAnimSegment83)
HAnimJoint90 = x3d.HAnimJoint()
HAnimJoint90.name = "r_metatarsophalangeal_2"
HAnimJoint90.DEF = "hanim_r_metatarsophalangeal_2"
HAnimJoint90.center = [-0.0801,0,0.0368]
HAnimJoint90.ulimit = [0,0,0]
HAnimJoint90.llimit = [0,0,0]
HAnimSegment91 = x3d.HAnimSegment()
HAnimSegment91.name = "r_tarsal_proximal_phalanx_2"
HAnimSegment91.DEF = "hanim_r_tarsal_proximal_phalanx_2"
HAnimSite92 = x3d.HAnimSite()
HAnimSite92.name = "r_middistal_tip"
HAnimSite92.DEF = "hanim_r_middistal_tip"
HAnimSite92.translation = [-0.1043,-0.0227,0.145]

HAnimSegment91.children.append(HAnimSite92)
HAnimSite93 = x3d.HAnimSite()
HAnimSite93.name = "r_metatarsal_phalanx_5_pt"
HAnimSite93.DEF = "hanim_r_metatarsal_phalanx_5_pt"
HAnimSite93.translation = [-0.1523,0.0166,0.0895]

HAnimSegment91.children.append(HAnimSite93)
HAnimSite94 = x3d.HAnimSite()
HAnimSite94.name = "r_metatarsal_phalanx_1_pt"
HAnimSite94.DEF = "hanim_r_metatarsal_phalanx_1_pt"
HAnimSite94.translation = [-0.0521,0.026,0.0127]

HAnimSegment91.children.append(HAnimSite94)
HAnimSite95 = x3d.HAnimSite()
HAnimSite95.name = "r_tarsal_distal_phalanx_2_pt"
HAnimSite95.DEF = "hanim_r_tarsal_distal_phalanx_2_pt"
HAnimSite95.translation = [-0.0883,0.0134,0.1383]

HAnimSegment91.children.append(HAnimSite95)

HAnimJoint90.children.append(HAnimSegment91)

HAnimJoint82.children.append(HAnimJoint90)

HAnimJoint78.children.append(HAnimJoint82)

HAnimJoint71.children.append(HAnimJoint78)

HAnimJoint38.children.append(HAnimJoint71)

HAnimJoint37.children.append(HAnimJoint38)
HAnimJoint96 = x3d.HAnimJoint()
HAnimJoint96.name = "vl1"
HAnimJoint96.DEF = "hanim_vl1"
HAnimJoint96.center = [-0.00405,1.07,-0.0275]
HAnimJoint96.ulimit = [0,0,0]
HAnimJoint96.llimit = [0,0,0]
HAnimSegment97 = x3d.HAnimSegment()
HAnimSegment97.name = "l1"
HAnimSegment97.DEF = "hanim_l1"

HAnimJoint96.children.append(HAnimSegment97)
HAnimJoint98 = x3d.HAnimJoint()
HAnimJoint98.name = "l_shoulder"
HAnimJoint98.DEF = "hanim_l_shoulder"
HAnimJoint98.center = [0.2029,1.4376,-0.0387]
HAnimJoint98.ulimit = [0,0,0]
HAnimJoint98.llimit = [0,0,0]
HAnimSegment99 = x3d.HAnimSegment()
HAnimSegment99.name = "l_upperarm"
HAnimSegment99.DEF = "hanim_l_upperarm"
Transform100 = x3d.Transform()
Transform100.translation = [0.2029,1.4376,-0.0387]
Shape101 = x3d.Shape()
Shape101.USE = "DiamondShape"

Transform100.children.append(Shape101)

HAnimSegment99.children.append(Transform100)
Transform102 = x3d.Transform()
Transform102.DEF = "l_upperarm_adjust"
Transform102.center = [0.182,1.22,-0.047]
Transform102.rotation = [1,0,0,0.119]
Transform102.translation = [0.2029,1.4376,-0.0387]

HAnimSegment99.children.append(Transform102)
HAnimSite103 = x3d.HAnimSite()
HAnimSite103.name = "l_humeral_lateral_epicondyle_pt"
HAnimSite103.DEF = "hanim_l_humeral_lateral_epicondyle_pt"
HAnimSite103.translation = [0.228,1.1482,-0.11]

HAnimSegment99.children.append(HAnimSite103)

HAnimJoint98.children.append(HAnimSegment99)
HAnimJoint104 = x3d.HAnimJoint()
HAnimJoint104.name = "l_elbow"
HAnimJoint104.DEF = "hanim_l_elbow"
HAnimJoint104.center = [0.2014,1.1357,-0.0682]
HAnimJoint104.ulimit = [0,0,0]
HAnimJoint104.llimit = [0,0,0]
HAnimSegment105 = x3d.HAnimSegment()
HAnimSegment105.name = "l_forearm"
HAnimSegment105.DEF = "hanim_l_forearm"
Transform106 = x3d.Transform()
Transform106.translation = [0.2014,1.1357,-0.0682]
Shape107 = x3d.Shape()
Shape107.USE = "DiamondShape"

Transform106.children.append(Shape107)

HAnimSegment105.children.append(Transform106)
Transform108 = x3d.Transform()
Transform108.DEF = "l_forearm_adjust"
Transform108.center = [0.198,0.961,-0.0405]
Transform108.rotation = [-1,0,0,0.1]
Transform108.translation = [0.2014,1.1357,-0.0682]

HAnimSegment105.children.append(Transform108)
HAnimSite109 = x3d.HAnimSite()
HAnimSite109.name = "l_radial_styloid_pt"
HAnimSite109.DEF = "hanim_l_radial_styloid_pt"
HAnimSite109.translation = [0.1901,0.8645,-0.0415]

HAnimSegment105.children.append(HAnimSite109)
HAnimSite110 = x3d.HAnimSite()
HAnimSite110.name = "l_olecranon_pt"
HAnimSite110.DEF = "hanim_l_olecranon_pt"
HAnimSite110.translation = [-0.1962,1.1375,-0.1123]

HAnimSegment105.children.append(HAnimSite110)
HAnimSite111 = x3d.HAnimSite()
HAnimSite111.name = "l_humeral_medial_epicondyle_pt"
HAnimSite111.DEF = "hanim_l_humeral_medial_epicondyle_pt"
HAnimSite111.translation = [0.1735,1.1272,-0.1113]

HAnimSegment105.children.append(HAnimSite111)
HAnimSite112 = x3d.HAnimSite()
HAnimSite112.name = "l_radiale_pt"
HAnimSite112.DEF = "hanim_l_radiale_pt"
HAnimSite112.translation = [0.2182,1.1212,-0.1167]

HAnimSegment105.children.append(HAnimSite112)

HAnimJoint104.children.append(HAnimSegment105)
HAnimJoint113 = x3d.HAnimJoint()
HAnimJoint113.name = "l_radiocarpal"
HAnimJoint113.DEF = "hanim_l_radiocarpal"
HAnimJoint113.center = [0.1984,0.8663,-0.0583]
HAnimJoint113.ulimit = [0,0,0]
HAnimJoint113.llimit = [0,0,0]
HAnimSegment114 = x3d.HAnimSegment()
HAnimSegment114.name = "l_carpal"
HAnimSegment114.DEF = "hanim_l_carpal"
Transform115 = x3d.Transform()
Transform115.translation = [0.1984,0.8663,-0.0583]
Shape116 = x3d.Shape()
Shape116.USE = "DiamondShape"

Transform115.children.append(Shape116)

HAnimSegment114.children.append(Transform115)
Transform117 = x3d.Transform()
Transform117.DEF = "l_hand_adjust"
Transform117.center = [0.213,0.811,-0.0338]
Transform117.rotation = [-0.06361,-0.9967,0.04988,1.333]
Transform117.translation = [0.1984,0.8663,-0.0583]

HAnimSegment114.children.append(Transform117)
HAnimSite118 = x3d.HAnimSite()
HAnimSite118.name = "l_hand_tip"
HAnimSite118.DEF = "hanim_l_hand_tip"
HAnimSite118.translation = [0.208,0.6731,-0.0491]

HAnimSegment114.children.append(HAnimSite118)
HAnimSite119 = x3d.HAnimSite()
HAnimSite119.name = "l_metacarpal_phalanx_2_pt"
HAnimSite119.DEF = "hanim_l_metacarpal_phalanx_2_pt"
HAnimSite119.translation = [0.2009,0.8139,-0.0237]

HAnimSegment114.children.append(HAnimSite119)
HAnimSite120 = x3d.HAnimSite()
HAnimSite120.name = "l_dactylion_pt"
HAnimSite120.DEF = "hanim_l_dactylion_pt"
HAnimSite120.translation = [0.2056,0.6743,-0.0482]

HAnimSegment114.children.append(HAnimSite120)
HAnimSite121 = x3d.HAnimSite()
HAnimSite121.name = "l_ulnar_styloid_pt"
HAnimSite121.DEF = "hanim_l_ulnar_styloid_pt"
HAnimSite121.translation = [-0.2142,0.8529,-0.0648]

HAnimSegment114.children.append(HAnimSite121)
HAnimSite122 = x3d.HAnimSite()
HAnimSite122.name = "l_metacarpal_phalanx_5_pt"
HAnimSite122.DEF = "hanim_l_metacarpal_phalanx_5_pt"
HAnimSite122.translation = [0.1929,0.786,-0.1122]

HAnimSegment114.children.append(HAnimSite122)

HAnimJoint113.children.append(HAnimSegment114)

HAnimJoint104.children.append(HAnimJoint113)

HAnimJoint98.children.append(HAnimJoint104)

HAnimJoint96.children.append(HAnimJoint98)
HAnimJoint123 = x3d.HAnimJoint()
HAnimJoint123.name = "r_shoulder"
HAnimJoint123.DEF = "hanim_r_shoulder"
HAnimJoint123.center = [-0.1907,1.4407,-0.0325]
HAnimJoint123.ulimit = [0,0,0]
HAnimJoint123.llimit = [0,0,0]
HAnimSegment124 = x3d.HAnimSegment()
HAnimSegment124.name = "r_upperarm"
HAnimSegment124.DEF = "hanim_r_upperarm"
Transform125 = x3d.Transform()
Transform125.translation = [-0.1907,1.4407,-0.0325]
Shape126 = x3d.Shape()
Shape126.USE = "DiamondShape"

Transform125.children.append(Shape126)

HAnimSegment124.children.append(Transform125)
Transform127 = x3d.Transform()
Transform127.DEF = "r_upperarm_adjust"
Transform127.center = [-0.182,1.22,-0.047]
Transform127.rotation = [1,0,0,0.0836]
Transform127.translation = [-0.1907,1.4407,-0.0325]

HAnimSegment124.children.append(Transform127)
HAnimSite128 = x3d.HAnimSite()
HAnimSite128.name = "r_humeral_lateral_epicondyle_pt"
HAnimSite128.DEF = "hanim_r_humeral_lateral_epicondyle_pt"
HAnimSite128.translation = [-0.2224,1.1517,-0.1033]

HAnimSegment124.children.append(HAnimSite128)

HAnimJoint123.children.append(HAnimSegment124)
HAnimJoint129 = x3d.HAnimJoint()
HAnimJoint129.name = "r_elbow"
HAnimJoint129.DEF = "hanim_r_elbow"
HAnimJoint129.center = [-0.1949,1.1388,-0.062]
HAnimJoint129.ulimit = [0,0,0]
HAnimJoint129.llimit = [0,0,0]
HAnimSegment130 = x3d.HAnimSegment()
HAnimSegment130.name = "r_forearm"
HAnimSegment130.DEF = "hanim_r_forearm"
Transform131 = x3d.Transform()
Transform131.translation = [-0.1949,1.1388,-0.062]
Shape132 = x3d.Shape()
Shape132.USE = "DiamondShape"

Transform131.children.append(Shape132)

HAnimSegment130.children.append(Transform131)
Transform133 = x3d.Transform()
Transform133.DEF = "r_forearm_adjust"
Transform133.center = [-0.198,0.961,-0.0397]
Transform133.rotation = [-1,0,0,0.1254]
Transform133.translation = [-0.1949,1.1388,-0.062]

HAnimSegment130.children.append(Transform133)
HAnimSite134 = x3d.HAnimSite()
HAnimSite134.name = "r_radial_styloid_pt"
HAnimSite134.DEF = "hanim_r_radial_styloid_pt"
HAnimSite134.translation = [-0.1884,0.8676,-0.036]

HAnimSegment130.children.append(HAnimSite134)
HAnimSite135 = x3d.HAnimSite()
HAnimSite135.name = "r_olecranon_pt"
HAnimSite135.DEF = "hanim_r_olecranon_pt"
HAnimSite135.translation = [-0.1907,1.1405,-0.1065]

HAnimSegment130.children.append(HAnimSite135)
HAnimSite136 = x3d.HAnimSite()
HAnimSite136.name = "r_humeral_medial_epicondyle_pt"
HAnimSite136.DEF = "hanim_r_humeral_medial_epicondyle_pt"
HAnimSite136.translation = [-0.168,1.1298,-0.1062]

HAnimSegment130.children.append(HAnimSite136)
HAnimSite137 = x3d.HAnimSite()
HAnimSite137.name = "r_radiale_pt"
HAnimSite137.DEF = "hanim_r_radiale_pt"
HAnimSite137.translation = [-0.213,1.1305,-0.1091]

HAnimSegment130.children.append(HAnimSite137)

HAnimJoint129.children.append(HAnimSegment130)
HAnimJoint138 = x3d.HAnimJoint()
HAnimJoint138.name = "r_radiocarpal"
HAnimJoint138.DEF = "hanim_r_radiocarpal"
HAnimJoint138.center = [-0.1959,0.8694,-0.0521]
HAnimJoint138.ulimit = [0,0,0]
HAnimJoint138.llimit = [0,0,0]
HAnimSegment139 = x3d.HAnimSegment()
HAnimSegment139.name = "r_carpal"
HAnimSegment139.DEF = "hanim_r_carpal"
Transform140 = x3d.Transform()
Transform140.translation = [-0.1959,0.8694,-0.0521]
Shape141 = x3d.Shape()
Shape141.USE = "DiamondShape"

Transform140.children.append(Shape141)

HAnimSegment139.children.append(Transform140)
Transform142 = x3d.Transform()
Transform142.DEF = "r_hand_adjust"
Transform142.center = [-0.217,0.811,-0.0338]
Transform142.rotation = [-0.09024,0.994,-0.0624,1.216]

HAnimSegment139.children.append(Transform142)
HAnimSite143 = x3d.HAnimSite()
HAnimSite143.name = "r_hand_tip"
HAnimSite143.DEF = "hanim_r_hand_tip"
HAnimSite143.translation = [-0.1969,0.6758,-0.0427]

HAnimSegment139.children.append(HAnimSite143)
HAnimSite144 = x3d.HAnimSite()
HAnimSite144.name = "r_metacarpal_phalanx_2_pt"
HAnimSite144.DEF = "hanim_r_metacarpal_phalanx_2_pt"
HAnimSite144.translation = [-0.1977,0.8169,-0.0177]

HAnimSegment139.children.append(HAnimSite144)
HAnimSite145 = x3d.HAnimSite()
HAnimSite145.name = "r_dactylion_pt"
HAnimSite145.DEF = "hanim_r_dactylion_pt"
HAnimSite145.translation = [-0.1941,0.6772,-0.0423]

HAnimSegment139.children.append(HAnimSite145)
HAnimSite146 = x3d.HAnimSite()
HAnimSite146.name = "r_ulnar_styloid_pt"
HAnimSite146.DEF = "hanim_r_ulnar_styloid_pt"
HAnimSite146.translation = [-0.2117,0.8562,-0.0584]

HAnimSegment139.children.append(HAnimSite146)
HAnimSite147 = x3d.HAnimSite()
HAnimSite147.name = "r_metacarpal_phalanx_5_pt"
HAnimSite147.DEF = "hanim_r_metacarpal_phalanx_5_pt"
HAnimSite147.translation = [-0.1929,0.789,-0.1064]

HAnimSegment139.children.append(HAnimSite147)

HAnimJoint138.children.append(HAnimSegment139)

HAnimJoint129.children.append(HAnimJoint138)

HAnimJoint123.children.append(HAnimJoint129)

HAnimJoint96.children.append(HAnimJoint123)
HAnimJoint148 = x3d.HAnimJoint()
HAnimJoint148.name = "vc4"
HAnimJoint148.DEF = "hanim_vc4"
HAnimJoint148.center = [0,1.43,-0.0458]
HAnimJoint148.ulimit = [0,0,0]
HAnimJoint148.llimit = [0,0,0]
HAnimSegment149 = x3d.HAnimSegment()
HAnimSegment149.name = "c4"
HAnimSegment149.DEF = "hanim_c4"

HAnimJoint148.children.append(HAnimSegment149)

HAnimJoint96.children.append(HAnimJoint148)

HAnimJoint37.children.append(HAnimJoint96)
HAnimJoint150 = x3d.HAnimJoint()
HAnimJoint150.name = "vl5"
HAnimJoint150.DEF = "hanim_vl5"
HAnimJoint150.center = [0.0028,1.0568,-0.0776]
HAnimJoint150.ulimit = [0,0,0]
HAnimJoint150.llimit = [0,0,0]
HAnimJoint151 = x3d.HAnimJoint()
HAnimJoint151.name = "skullbase"
HAnimJoint151.DEF = "hanim_skullbase"
HAnimJoint151.center = [0.0044,1.6209,0.0236]
HAnimJoint151.ulimit = [0,0,0]
HAnimJoint151.llimit = [0,0,0]
HAnimSegment152 = x3d.HAnimSegment()
HAnimSegment152.name = "skull"
HAnimSegment152.DEF = "hanim_skull"
Transform153 = x3d.Transform()
Transform153.translation = [0.0044,1.6209,0.0236]
Shape154 = x3d.Shape()
Shape154.USE = "DiamondShape"

Transform153.children.append(Shape154)

HAnimSegment152.children.append(Transform153)
HAnimSite155 = x3d.HAnimSite()
HAnimSite155.name = "skull_vertex_tip"
HAnimSite155.DEF = "hanim_skull_vertex_tip"
HAnimSite155.translation = [0.005,1.7504,0.0055]

HAnimSegment152.children.append(HAnimSite155)
HAnimSite156 = x3d.HAnimSite()
HAnimSite156.name = "sellion_pt"
HAnimSite156.DEF = "hanim_sellion_pt"
HAnimSite156.translation = [0.0058,1.6316,0.0852]

HAnimSegment152.children.append(HAnimSite156)
HAnimSite157 = x3d.HAnimSite()
HAnimSite157.name = "r_infraorbitale_pt"
HAnimSite157.DEF = "hanim_r_infraorbitale_pt"
HAnimSite157.translation = [-0.0237,1.6171,0.0752]

HAnimSegment152.children.append(HAnimSite157)
HAnimSite158 = x3d.HAnimSite()
HAnimSite158.name = "l_infraorbitale_pt"
HAnimSite158.DEF = "hanim_l_infraorbitale_pt"
HAnimSite158.translation = [0.0341,1.6171,0.0752]

HAnimSegment152.children.append(HAnimSite158)
HAnimSite159 = x3d.HAnimSite()
HAnimSite159.name = "supramenton_pt"
HAnimSite159.DEF = "hanim_supramenton_pt"
HAnimSite159.translation = [0.0061,1.541,0.0805]

HAnimSegment152.children.append(HAnimSite159)
HAnimSite160 = x3d.HAnimSite()
HAnimSite160.name = "r_tragion_pt"
HAnimSite160.DEF = "hanim_r_tragion_pt"
HAnimSite160.translation = [-0.0646,1.6347,0.0302]

HAnimSegment152.children.append(HAnimSite160)
HAnimSite161 = x3d.HAnimSite()
HAnimSite161.name = "r_gonion_pt"
HAnimSite161.DEF = "hanim_r_gonion_pt"
HAnimSite161.translation = [-0.052,1.5529,0.0347]

HAnimSegment152.children.append(HAnimSite161)
HAnimSite162 = x3d.HAnimSite()
HAnimSite162.name = "l_tragion_pt"
HAnimSite162.DEF = "hanim_l_tragion_pt"
HAnimSite162.translation = [0.0739,1.6348,0.0282]

HAnimSegment152.children.append(HAnimSite162)
HAnimSite163 = x3d.HAnimSite()
HAnimSite163.name = "l_gonion_pt"
HAnimSite163.DEF = "hanim_l_gonion_pt"
HAnimSite163.translation = [0.0631,1.553,0.033]

HAnimSegment152.children.append(HAnimSite163)
HAnimSite164 = x3d.HAnimSite()
HAnimSite164.name = "nuchale_pt"
HAnimSite164.DEF = "hanim_nuchale_pt"
HAnimSite164.translation = [0.0039,1.5972,-0.0796]

HAnimSegment152.children.append(HAnimSite164)

HAnimJoint151.children.append(HAnimSegment152)

HAnimJoint150.children.append(HAnimJoint151)

HAnimJoint37.children.append(HAnimJoint150)

HAnimHumanoid30.skeleton.append(HAnimJoint37)
HAnimSite165 = x3d.HAnimSite()
HAnimSite165.name = "DiamondManLOA1_view"
HAnimSite165.DEF = "hanim_DiamondManLOA1_view"
Viewpoint166 = x3d.Viewpoint()
Viewpoint166.DEF = "InclinedView"
Viewpoint166.description = "Inclined View"
Viewpoint166.orientation = [-0.113,0.993,0.0347,0.671]
Viewpoint166.position = [1.62,1.05,2.06]

HAnimSite165.children.append(Viewpoint166)
Viewpoint167 = x3d.Viewpoint()
Viewpoint167.DEF = "FrontView"
Viewpoint167.description = "Front View"
Viewpoint167.position = [0,0.854,2.57665]

HAnimSite165.children.append(Viewpoint167)
Viewpoint168 = x3d.Viewpoint()
Viewpoint168.DEF = "SideView"
Viewpoint168.description = "Side View"
Viewpoint168.orientation = [0,1,0,1.57079]
Viewpoint168.position = [2.5929,0.854,0]

HAnimSite165.children.append(Viewpoint168)
Viewpoint169 = x3d.Viewpoint()
Viewpoint169.DEF = "TopView"
Viewpoint169.description = "Top View"
Viewpoint169.orientation = [1,0,0,-1.57079]
Viewpoint169.position = [0,3.4495,0]

HAnimSite165.children.append(Viewpoint169)

HAnimHumanoid30.viewpoints.append(HAnimSite165)
HAnimJoint170 = x3d.HAnimJoint()
HAnimJoint170.USE = "hanim_humanoid_root"

HAnimHumanoid30.joints.append(HAnimJoint170)
HAnimJoint171 = x3d.HAnimJoint()
HAnimJoint171.USE = "hanim_sacroiliac"

HAnimHumanoid30.joints.append(HAnimJoint171)
HAnimJoint172 = x3d.HAnimJoint()
HAnimJoint172.USE = "hanim_vl1"

HAnimHumanoid30.joints.append(HAnimJoint172)
HAnimJoint173 = x3d.HAnimJoint()
HAnimJoint173.USE = "hanim_vc4"

HAnimHumanoid30.joints.append(HAnimJoint173)
HAnimJoint174 = x3d.HAnimJoint()
HAnimJoint174.USE = "hanim_skullbase"

HAnimHumanoid30.joints.append(HAnimJoint174)
HAnimJoint175 = x3d.HAnimJoint()
HAnimJoint175.USE = "hanim_vl5"

HAnimHumanoid30.joints.append(HAnimJoint175)
HAnimJoint176 = x3d.HAnimJoint()
HAnimJoint176.USE = "hanim_l_elbow"

HAnimHumanoid30.joints.append(HAnimJoint176)
HAnimJoint177 = x3d.HAnimJoint()
HAnimJoint177.USE = "hanim_r_elbow"

HAnimHumanoid30.joints.append(HAnimJoint177)
HAnimJoint178 = x3d.HAnimJoint()
HAnimJoint178.USE = "hanim_l_hip"

HAnimHumanoid30.joints.append(HAnimJoint178)
HAnimJoint179 = x3d.HAnimJoint()
HAnimJoint179.USE = "hanim_r_hip"

HAnimHumanoid30.joints.append(HAnimJoint179)
HAnimJoint180 = x3d.HAnimJoint()
HAnimJoint180.USE = "hanim_l_knee"

HAnimHumanoid30.joints.append(HAnimJoint180)
HAnimJoint181 = x3d.HAnimJoint()
HAnimJoint181.USE = "hanim_r_knee"

HAnimHumanoid30.joints.append(HAnimJoint181)
HAnimJoint182 = x3d.HAnimJoint()
HAnimJoint182.USE = "hanim_l_metatarsophalangeal_2"

HAnimHumanoid30.joints.append(HAnimJoint182)
HAnimJoint183 = x3d.HAnimJoint()
HAnimJoint183.USE = "hanim_r_metatarsophalangeal_2"

HAnimHumanoid30.joints.append(HAnimJoint183)
HAnimJoint184 = x3d.HAnimJoint()
HAnimJoint184.USE = "hanim_l_radiocarpal"

HAnimHumanoid30.joints.append(HAnimJoint184)
HAnimJoint185 = x3d.HAnimJoint()
HAnimJoint185.USE = "hanim_r_radiocarpal"

HAnimHumanoid30.joints.append(HAnimJoint185)
HAnimJoint186 = x3d.HAnimJoint()
HAnimJoint186.USE = "hanim_l_shoulder"

HAnimHumanoid30.joints.append(HAnimJoint186)
HAnimJoint187 = x3d.HAnimJoint()
HAnimJoint187.USE = "hanim_r_shoulder"

HAnimHumanoid30.joints.append(HAnimJoint187)
HAnimJoint188 = x3d.HAnimJoint()
HAnimJoint188.USE = "hanim_l_talocrural"

HAnimHumanoid30.joints.append(HAnimJoint188)
HAnimJoint189 = x3d.HAnimJoint()
HAnimJoint189.USE = "hanim_r_talocrural"

HAnimHumanoid30.joints.append(HAnimJoint189)
HAnimSegment190 = x3d.HAnimSegment()
HAnimSegment190.USE = "hanim_pelvis"

HAnimHumanoid30.segments.append(HAnimSegment190)
HAnimSegment191 = x3d.HAnimSegment()
HAnimSegment191.USE = "hanim_l1"

HAnimHumanoid30.segments.append(HAnimSegment191)
HAnimSegment192 = x3d.HAnimSegment()
HAnimSegment192.USE = "hanim_c4"

HAnimHumanoid30.segments.append(HAnimSegment192)
HAnimSegment193 = x3d.HAnimSegment()
HAnimSegment193.USE = "hanim_skull"

HAnimHumanoid30.segments.append(HAnimSegment193)
HAnimSegment194 = x3d.HAnimSegment()
HAnimSegment194.USE = "hanim_l_calf"

HAnimHumanoid30.segments.append(HAnimSegment194)
HAnimSegment195 = x3d.HAnimSegment()
HAnimSegment195.USE = "hanim_r_calf"

HAnimHumanoid30.segments.append(HAnimSegment195)
HAnimSegment196 = x3d.HAnimSegment()
HAnimSegment196.USE = "hanim_l_carpal"

HAnimHumanoid30.segments.append(HAnimSegment196)
HAnimSegment197 = x3d.HAnimSegment()
HAnimSegment197.USE = "hanim_r_carpal"

HAnimHumanoid30.segments.append(HAnimSegment197)
HAnimSegment198 = x3d.HAnimSegment()
HAnimSegment198.USE = "hanim_l_forearm"

HAnimHumanoid30.segments.append(HAnimSegment198)
HAnimSegment199 = x3d.HAnimSegment()
HAnimSegment199.USE = "hanim_r_forearm"

HAnimHumanoid30.segments.append(HAnimSegment199)
HAnimSegment200 = x3d.HAnimSegment()
HAnimSegment200.USE = "hanim_l_talus"

HAnimHumanoid30.segments.append(HAnimSegment200)
HAnimSegment201 = x3d.HAnimSegment()
HAnimSegment201.USE = "hanim_r_talus"

HAnimHumanoid30.segments.append(HAnimSegment201)
HAnimSegment202 = x3d.HAnimSegment()
HAnimSegment202.USE = "hanim_l_tarsal_proximal_phalanx_2"

HAnimHumanoid30.segments.append(HAnimSegment202)
HAnimSegment203 = x3d.HAnimSegment()
HAnimSegment203.USE = "hanim_r_tarsal_proximal_phalanx_2"

HAnimHumanoid30.segments.append(HAnimSegment203)
HAnimSegment204 = x3d.HAnimSegment()
HAnimSegment204.USE = "hanim_l_thigh"

HAnimHumanoid30.segments.append(HAnimSegment204)
HAnimSegment205 = x3d.HAnimSegment()
HAnimSegment205.USE = "hanim_r_thigh"

HAnimHumanoid30.segments.append(HAnimSegment205)
HAnimSegment206 = x3d.HAnimSegment()
HAnimSegment206.USE = "hanim_l_upperarm"

HAnimHumanoid30.segments.append(HAnimSegment206)
HAnimSegment207 = x3d.HAnimSegment()
HAnimSegment207.USE = "hanim_r_upperarm"

HAnimHumanoid30.segments.append(HAnimSegment207)
HAnimSite208 = x3d.HAnimSite()
HAnimSite208.USE = "hanim_skull_vertex_tip"

HAnimHumanoid30.sites.append(HAnimSite208)
HAnimSite209 = x3d.HAnimSite()
HAnimSite209.USE = "hanim_sellion_pt"

HAnimHumanoid30.sites.append(HAnimSite209)
HAnimSite210 = x3d.HAnimSite()
HAnimSite210.USE = "hanim_supramenton_pt"

HAnimHumanoid30.sites.append(HAnimSite210)
HAnimSite211 = x3d.HAnimSite()
HAnimSite211.USE = "hanim_nuchale_pt"

HAnimHumanoid30.sites.append(HAnimSite211)
HAnimSite212 = x3d.HAnimSite()
HAnimSite212.USE = "hanim_l_calcaneus_posterior_pt"

HAnimHumanoid30.sites.append(HAnimSite212)
HAnimSite213 = x3d.HAnimSite()
HAnimSite213.USE = "hanim_r_calcaneus_posterior_pt"

HAnimHumanoid30.sites.append(HAnimSite213)
HAnimSite214 = x3d.HAnimSite()
HAnimSite214.USE = "hanim_l_dactylion_pt"

HAnimHumanoid30.sites.append(HAnimSite214)
HAnimSite215 = x3d.HAnimSite()
HAnimSite215.USE = "hanim_r_dactylion_pt"

HAnimHumanoid30.sites.append(HAnimSite215)
HAnimSite216 = x3d.HAnimSite()
HAnimSite216.USE = "hanim_l_femoral_lateral_epicondyle_pt"

HAnimHumanoid30.sites.append(HAnimSite216)
HAnimSite217 = x3d.HAnimSite()
HAnimSite217.USE = "hanim_r_femoral_lateral_epicondyle_pt"

HAnimHumanoid30.sites.append(HAnimSite217)
HAnimSite218 = x3d.HAnimSite()
HAnimSite218.USE = "hanim_l_femoral_medial_epicondyle_pt"

HAnimHumanoid30.sites.append(HAnimSite218)
HAnimSite219 = x3d.HAnimSite()
HAnimSite219.USE = "hanim_r_femoral_medial_epicondyle_pt"

HAnimHumanoid30.sites.append(HAnimSite219)
HAnimSite220 = x3d.HAnimSite()
HAnimSite220.USE = "hanim_r_gonion_pt"

HAnimHumanoid30.sites.append(HAnimSite220)
HAnimSite221 = x3d.HAnimSite()
HAnimSite221.USE = "hanim_l_gonion_pt"

HAnimHumanoid30.sites.append(HAnimSite221)
HAnimSite222 = x3d.HAnimSite()
HAnimSite222.USE = "hanim_l_hand_tip"

HAnimHumanoid30.sites.append(HAnimSite222)
HAnimSite223 = x3d.HAnimSite()
HAnimSite223.USE = "hanim_r_hand_tip"

HAnimHumanoid30.sites.append(HAnimSite223)
HAnimSite224 = x3d.HAnimSite()
HAnimSite224.USE = "hanim_l_humeral_lateral_epicondyle_pt"

HAnimHumanoid30.sites.append(HAnimSite224)
HAnimSite225 = x3d.HAnimSite()
HAnimSite225.USE = "hanim_r_humeral_lateral_epicondyle_pt"

HAnimHumanoid30.sites.append(HAnimSite225)
HAnimSite226 = x3d.HAnimSite()
HAnimSite226.USE = "hanim_l_humeral_medial_epicondyle_pt"

HAnimHumanoid30.sites.append(HAnimSite226)
HAnimSite227 = x3d.HAnimSite()
HAnimSite227.USE = "hanim_r_humeral_medial_epicondyle_pt"

HAnimHumanoid30.sites.append(HAnimSite227)
HAnimSite228 = x3d.HAnimSite()
HAnimSite228.USE = "hanim_r_infraorbitale_pt"

HAnimHumanoid30.sites.append(HAnimSite228)
HAnimSite229 = x3d.HAnimSite()
HAnimSite229.USE = "hanim_l_infraorbitale_pt"

HAnimHumanoid30.sites.append(HAnimSite229)
HAnimSite230 = x3d.HAnimSite()
HAnimSite230.USE = "hanim_l_knee_crease_pt"

HAnimHumanoid30.sites.append(HAnimSite230)
HAnimSite231 = x3d.HAnimSite()
HAnimSite231.USE = "hanim_r_knee_crease_pt"

HAnimHumanoid30.sites.append(HAnimSite231)
HAnimSite232 = x3d.HAnimSite()
HAnimSite232.USE = "hanim_l_lateral_malleolus_pt"

HAnimHumanoid30.sites.append(HAnimSite232)
HAnimSite233 = x3d.HAnimSite()
HAnimSite233.USE = "hanim_r_lateral_malleolus_pt"

HAnimHumanoid30.sites.append(HAnimSite233)
HAnimSite234 = x3d.HAnimSite()
HAnimSite234.USE = "hanim_l_medial_malleolus_pt"

HAnimHumanoid30.sites.append(HAnimSite234)
HAnimSite235 = x3d.HAnimSite()
HAnimSite235.USE = "hanim_r_medial_malleolus_pt"

HAnimHumanoid30.sites.append(HAnimSite235)
HAnimSite236 = x3d.HAnimSite()
HAnimSite236.USE = "hanim_l_metacarpal_phalanx_2_pt"

HAnimHumanoid30.sites.append(HAnimSite236)
HAnimSite237 = x3d.HAnimSite()
HAnimSite237.USE = "hanim_r_metacarpal_phalanx_2_pt"

HAnimHumanoid30.sites.append(HAnimSite237)
HAnimSite238 = x3d.HAnimSite()
HAnimSite238.USE = "hanim_l_metacarpal_phalanx_5_pt"

HAnimHumanoid30.sites.append(HAnimSite238)
HAnimSite239 = x3d.HAnimSite()
HAnimSite239.USE = "hanim_r_metacarpal_phalanx_5_pt"

HAnimHumanoid30.sites.append(HAnimSite239)
HAnimSite240 = x3d.HAnimSite()
HAnimSite240.USE = "hanim_l_metatarsal_phalanx_1_pt"

HAnimHumanoid30.sites.append(HAnimSite240)
HAnimSite241 = x3d.HAnimSite()
HAnimSite241.USE = "hanim_r_metatarsal_phalanx_1_pt"

HAnimHumanoid30.sites.append(HAnimSite241)
HAnimSite242 = x3d.HAnimSite()
HAnimSite242.USE = "hanim_l_metatarsal_phalanx_5_pt"

HAnimHumanoid30.sites.append(HAnimSite242)
HAnimSite243 = x3d.HAnimSite()
HAnimSite243.USE = "hanim_r_metatarsal_phalanx_5_pt"

HAnimHumanoid30.sites.append(HAnimSite243)
HAnimSite244 = x3d.HAnimSite()
HAnimSite244.USE = "hanim_l_middistal_tip"

HAnimHumanoid30.sites.append(HAnimSite244)
HAnimSite245 = x3d.HAnimSite()
HAnimSite245.USE = "hanim_r_middistal_tip"

HAnimHumanoid30.sites.append(HAnimSite245)
HAnimSite246 = x3d.HAnimSite()
HAnimSite246.USE = "hanim_l_olecranon_pt"

HAnimHumanoid30.sites.append(HAnimSite246)
HAnimSite247 = x3d.HAnimSite()
HAnimSite247.USE = "hanim_r_olecranon_pt"

HAnimHumanoid30.sites.append(HAnimSite247)
HAnimSite248 = x3d.HAnimSite()
HAnimSite248.USE = "hanim_l_radial_styloid_pt"

HAnimHumanoid30.sites.append(HAnimSite248)
HAnimSite249 = x3d.HAnimSite()
HAnimSite249.USE = "hanim_r_radial_styloid_pt"

HAnimHumanoid30.sites.append(HAnimSite249)
HAnimSite250 = x3d.HAnimSite()
HAnimSite250.USE = "hanim_l_radiale_pt"

HAnimHumanoid30.sites.append(HAnimSite250)
HAnimSite251 = x3d.HAnimSite()
HAnimSite251.USE = "hanim_r_radiale_pt"

HAnimHumanoid30.sites.append(HAnimSite251)
HAnimSite252 = x3d.HAnimSite()
HAnimSite252.USE = "hanim_l_sphyrion_pt"

HAnimHumanoid30.sites.append(HAnimSite252)
HAnimSite253 = x3d.HAnimSite()
HAnimSite253.USE = "hanim_r_sphyrion_pt"

HAnimHumanoid30.sites.append(HAnimSite253)
HAnimSite254 = x3d.HAnimSite()
HAnimSite254.USE = "hanim_l_tarsal_distal_phalanx_2_pt"

HAnimHumanoid30.sites.append(HAnimSite254)
HAnimSite255 = x3d.HAnimSite()
HAnimSite255.USE = "hanim_r_tarsal_distal_phalanx_2_pt"

HAnimHumanoid30.sites.append(HAnimSite255)
HAnimSite256 = x3d.HAnimSite()
HAnimSite256.USE = "hanim_r_tragion_pt"

HAnimHumanoid30.sites.append(HAnimSite256)
HAnimSite257 = x3d.HAnimSite()
HAnimSite257.USE = "hanim_l_tragion_pt"

HAnimHumanoid30.sites.append(HAnimSite257)
HAnimSite258 = x3d.HAnimSite()
HAnimSite258.USE = "hanim_l_ulnar_styloid_pt"

HAnimHumanoid30.sites.append(HAnimSite258)
HAnimSite259 = x3d.HAnimSite()
HAnimSite259.USE = "hanim_r_ulnar_styloid_pt"

HAnimHumanoid30.sites.append(HAnimSite259)

Scene26.children.append(HAnimHumanoid30)

X3D0.Scene = Scene26
f = open("././DiamondManLOA1_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
