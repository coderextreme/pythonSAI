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
meta3.content = "HAnim2SpecificationLOA3Invisible.x3d"

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.name = "description"
meta4.content = "HAnim Specification reference example providing full coverage (and no illustrated visibility) of all specified HAnim constructs, also suitable for re-use as an authoring template."

head1.children.append(meta4)
meta5 = x3d.meta()
meta5.name = "reference"
meta5.content = "https://www.web3d.org/files/specifications/19774/V1.0/HAnim/BodyDimensionsAndLOAs.html#LOA3ExampleSourceWithDiamonds"

head1.children.append(meta5)
meta6 = x3d.meta()
meta6.name = "created"
meta6.content = "24 April 2013"

head1.children.append(meta6)
meta7 = x3d.meta()
meta7.name = "modified"
meta7.content = "23 December 2021"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.name = "creator"
meta8.content = "Matthew T. Beitler, Joe D. Williams, Don Brutzman"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "reference"
meta9.content = "HAnim2SpecificationLOA3Illustrated.x3d"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "reference"
meta10.content = "HAnim2SpecificationLOA3Animation.x3d"

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.name = "reference"
meta11.content = "HAnimSpecificationExampleChangeLog.txt"

head1.children.append(meta11)
meta12 = x3d.meta()
meta12.name = "Image"
meta12.content = "images/BonesAllSkeletonFrontViewLOA1.png"

head1.children.append(meta12)
meta13 = x3d.meta()
meta13.name = "Image"
meta13.content = "images/BonesAllSkeletonFrontViewLOA2.png"

head1.children.append(meta13)
meta14 = x3d.meta()
meta14.name = "Image"
meta14.content = "images/BonesAllSkeletonFrontViewLOA3.png"

head1.children.append(meta14)
meta15 = x3d.meta()
meta15.name = "TODO"
meta15.content = "move relevant HAnimSite/Viewpoint pairs into skeleton at appropriate locations"

head1.children.append(meta15)
meta16 = x3d.meta()
meta16.name = "TODO"
meta16.content = "insert MetadataInteger nodes indicating LOA for each Joint and Segment"

head1.children.append(meta16)
meta17 = x3d.meta()
meta17.name = "reference"
meta17.content = "Norman Badler et al., ANTHROPOMETRY FOR COMPUTER GRAPHICS HUMAN FIGURES, University of Pennsylvania, 1989."

head1.children.append(meta17)
meta18 = x3d.meta()
meta18.name = "reference"
meta18.content = "http://www.cis.upenn.edu/~badler/anthro/89-71.ps"

head1.children.append(meta18)
meta19 = x3d.meta()
meta19.name = "reference"
meta19.content = "tables/AnthropometryForComputerGraphicsHumanFigures89-71.pdf"

head1.children.append(meta19)
meta20 = x3d.meta()
meta20.name = "translator"
meta20.content = "Don Brutzman and Joe Williams"

head1.children.append(meta20)
meta21 = x3d.meta()
meta21.name = "generator"
meta21.content = "BS Contact Geo 8.001, http://www.bitmanagement.de/en/products/interactive-3d-clients/bs-contact-geo"

head1.children.append(meta21)
meta22 = x3d.meta()
meta22.name = "reference"
meta22.content = "originals/LOA3ExampleSourceWithDiamondsOriginal.wrl"

head1.children.append(meta22)
meta23 = x3d.meta()
meta23.name = "reference"
meta23.content = "originals/LOA3ExampleSourceWithDiamondsOriginal.x3d"

head1.children.append(meta23)
meta24 = x3d.meta()
meta24.name = "reference"
meta24.content = "originals/LOA3ExampleSourceWithDiamondsOriginalBsContactExport.x3d"

head1.children.append(meta24)
meta25 = x3d.meta()
meta25.name = "reference"
meta25.content = "HAnim Specification Table 4.4 - Face Joint object names, https://www.web3d.org/files/specifications/19774/V1.0/HAnim/concepts.html#FaceJointObjectNames"

head1.children.append(meta25)
meta26 = x3d.meta()
meta26.name = "generator"
meta26.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"

head1.children.append(meta26)
meta27 = x3d.meta()
meta27.name = "identifier"
meta27.content = "https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Specifications/HAnim2SpecificationLOA3Invisible.x3d"

head1.children.append(meta27)
meta28 = x3d.meta()
meta28.name = "license"
meta28.content = "../license.html"

head1.children.append(meta28)

X3D0.head = head1
Scene29 = x3d.Scene()
Background30 = x3d.Background()
Background30.skyColor = [0.3,0.3,0.3]

Scene29.children.append(Background30)
NavigationInfo31 = x3d.NavigationInfo()

Scene29.children.append(NavigationInfo31)
Group32 = x3d.Group()
Group32.DEF = "Original_WorldInfo"
WorldInfo33 = x3d.WorldInfo()
WorldInfo33.info = [" HANIM 200x Default Joint Centers, Level-Of-Articulation 3 HANIM 200x (VRML97) Author name: eMpTy (a.k.a. Matthew T. Beitler) HANIM 200x (VRML97) Author email: beitler@cis.upenn.edu or beitler@acm.org HANIM 200x (VRML97) Author homepage: http://www.cis.upenn.edu/~beitler HANIM 200x (VRML97) Compliance Date: August 12, 2003 HANIM 200x Compliance Information: http://HAnim.org/Specifications/HAnim200x Construction Info (joint centers): The joint centers of this figure are based on the work of Norman Badler, director of the Center for Human Modeling and Simulation at the University of Pennsylvania. The original document which these joint centers are based on can be found at: http://www.cis.upenn.edu/~badler/anthro/89-71.ps "]
WorldInfo33.title = "HANIM 200x Default Joint Centers, LOA3"

Group32.children.append(WorldInfo33)

Scene29.children.append(Group32)
#TODO move viewpoints to be internal to HAnimHumanoid
#Viewpoint centerOfRotation=\"0 0.9149 0.0016\" matches initial at-rest locaton of the sacroliac. Note that these viewpoints are external to the HAnimHumanoid and do not move with the human.
Viewpoint34 = x3d.Viewpoint()
Viewpoint34.centerOfRotation = [0,0.9149,0.0016]
Viewpoint34.description = "Humanoid LOA 3 Front"
Viewpoint34.position = [0,0.4,4]

Scene29.children.append(Viewpoint34)
Viewpoint35 = x3d.Viewpoint()
Viewpoint35.centerOfRotation = [0,0.9149,0.0016]
Viewpoint35.description = "Humanoid LOA 3 Front Close"
Viewpoint35.position = [0,0.8,2]

Scene29.children.append(Viewpoint35)
Viewpoint36 = x3d.Viewpoint()
Viewpoint36.centerOfRotation = [0,0.9149,0.0016]
Viewpoint36.description = "Humanoid LOA 3 Front Closer"
Viewpoint36.position = [0,1.2,1]

Scene29.children.append(Viewpoint36)
Viewpoint37 = x3d.Viewpoint()
Viewpoint37.centerOfRotation = [0,1.5,0.0016]
Viewpoint37.description = "Humanoid LOA 3 Front Face"
Viewpoint37.position = [0,1.63,1]

Scene29.children.append(Viewpoint37)
Viewpoint38 = x3d.Viewpoint()
Viewpoint38.centerOfRotation = [0,0.9149,0.0016]
Viewpoint38.description = "Humanoid LOA 3 Right Side"
Viewpoint38.orientation = [0,1,0,1.5708]
Viewpoint38.position = [2.6,0.8,0]

Scene29.children.append(Viewpoint38)
Viewpoint39 = x3d.Viewpoint()
Viewpoint39.centerOfRotation = [0,0.9149,0.0016]
Viewpoint39.description = "Humanoid LOA 3 Right Side Close"
Viewpoint39.orientation = [0,1,0,1.2]
Viewpoint39.position = [1,0.8,0.5]

Scene29.children.append(Viewpoint39)
Viewpoint40 = x3d.Viewpoint()
Viewpoint40.centerOfRotation = [0,0.9149,0.0016]
Viewpoint40.description = "Humanoid LOA 3 Left Side Close"
Viewpoint40.orientation = [0,1,0,-1.2]
Viewpoint40.position = [-1,0.8,0.5]

Scene29.children.append(Viewpoint40)
Viewpoint41 = x3d.Viewpoint()
Viewpoint41.centerOfRotation = [0,0.9149,0.0016]
Viewpoint41.description = "Humanoid LOA 3 Left Side"
Viewpoint41.orientation = [0,1,0,-1.5708]
Viewpoint41.position = [-2.6,0.8,0]

Scene29.children.append(Viewpoint41)
Viewpoint42 = x3d.Viewpoint()
Viewpoint42.centerOfRotation = [0,0.9149,0.0016]
Viewpoint42.description = "Humanoid LOA 3 Top"
Viewpoint42.orientation = [1,0,0,-1.5708]
Viewpoint42.position = [0,3.5,0]

Scene29.children.append(Viewpoint42)
HAnimHumanoid43 = x3d.HAnimHumanoid()
HAnimHumanoid43.name = "humanoid"
HAnimHumanoid43.DEF = "hanim_humanoid"
HAnimHumanoid43.loa = 3
HAnimHumanoid43.version = "2.0"
#original HAnimHumanoid info='\"authorName=Matthew T. Beitler Joe D. Williams Don Brutzman\" \"authorEmail=HAnim@web3D.org\" \"copyright=none\" \"creationDate=12 May 1999\" \"usageRestrictions=none\" \"humanoidVersion=2.0\" \"height=1.7504\"'
#Only one root HAnimJoint is allowed
#USE nodes go here for access by inverse kinematics (IK) engines and other tools
#Top-level HAnimSite/Viewpoint nodes that move with the human center but are unaffected by body animation
#TODO move relevant HAnimSite/Viewpoint pairs into skeleton at appropriate locations, if so also revert containerField to default
#right between the eyes, stationary position not animating except with body itself
MetadataSet44 = x3d.MetadataSet()
MetadataSet44.name = "HAnimHumanoid.info"
MetadataSet44.reference = "https://www.web3d.org/documents/specifications/19774/V2.0/Architecture/ObjectInterfaces.html#Humanoid"
MetadataString45 = x3d.MetadataString()
MetadataString45.name = "authorName"
MetadataString45.value = ["Matthew T. Beitler Joe D. Williams Don Brutzman"]

MetadataSet44.value.append(MetadataString45)
MetadataString46 = x3d.MetadataString()
MetadataString46.name = "authorEmail"
MetadataString46.value = ["HAnim@web3D.org"]

MetadataSet44.value.append(MetadataString46)
MetadataString47 = x3d.MetadataString()
MetadataString47.name = "copyright"
MetadataString47.value = ["none"]

MetadataSet44.value.append(MetadataString47)
MetadataString48 = x3d.MetadataString()
MetadataString48.name = "creationDate"
MetadataString48.value = ["12 May 1999"]

MetadataSet44.value.append(MetadataString48)
MetadataFloat49 = x3d.MetadataFloat()
MetadataFloat49.name = "height"
MetadataFloat49.value = [1.7504]

MetadataSet44.value.append(MetadataFloat49)
MetadataString50 = x3d.MetadataString()
MetadataString50.name = "humanoidVersion"
MetadataString50.value = ["2.0"]

MetadataSet44.value.append(MetadataString50)
MetadataString51 = x3d.MetadataString()
MetadataString51.name = "usageRestrictions"
MetadataString51.value = ["none"]

MetadataSet44.value.append(MetadataString51)

HAnimHumanoid43.metadata.append(MetadataSet44)
HAnimJoint52 = x3d.HAnimJoint()
HAnimJoint52.name = "humanoid_root"
HAnimJoint52.DEF = "hanim_humanoid_root"
HAnimJoint52.center = [0,0.824,0.0277]
HAnimJoint52.ulimit = [0,0,0]
HAnimJoint52.llimit = [0,0,0]
HAnimSegment53 = x3d.HAnimSegment()
HAnimSegment53.name = "sacrum"
HAnimSegment53.DEF = "hanim_sacrum"

HAnimJoint52.children.append(HAnimSegment53)
HAnimJoint54 = x3d.HAnimJoint()
HAnimJoint54.name = "sacroiliac"
HAnimJoint54.DEF = "hanim_sacroiliac"
HAnimJoint54.center = [0,0.9149,0.0016]
HAnimJoint54.ulimit = [0,0,0]
HAnimJoint54.llimit = [0,0,0]
HAnimSegment55 = x3d.HAnimSegment()
HAnimSegment55.name = "pelvis"
HAnimSegment55.DEF = "hanim_pelvis"
HAnimSite56 = x3d.HAnimSite()
HAnimSite56.name = "r_iliocristale_pt"
HAnimSite56.DEF = "hanim_r_iliocristale_pt"
HAnimSite56.translation = [-0.1525,1.0628,0.0035]

HAnimSegment55.children.append(HAnimSite56)
HAnimSite57 = x3d.HAnimSite()
HAnimSite57.name = "r_trochanterion_pt"
HAnimSite57.DEF = "hanim_r_trochanterion_pt"
HAnimSite57.translation = [-0.1689,0.8419,0.0352]

HAnimSegment55.children.append(HAnimSite57)
HAnimSite58 = x3d.HAnimSite()
HAnimSite58.name = "l_iliocristale_pt"
HAnimSite58.DEF = "hanim_l_iliocristale_pt"
HAnimSite58.translation = [0.1612,1.0537,0.0008]

HAnimSegment55.children.append(HAnimSite58)
HAnimSite59 = x3d.HAnimSite()
HAnimSite59.name = "l_trochanterion_pt"
HAnimSite59.DEF = "hanim_l_trochanterion_pt"
HAnimSite59.translation = [0.1677,0.8336,0.0303]

HAnimSegment55.children.append(HAnimSite59)
HAnimSite60 = x3d.HAnimSite()
HAnimSite60.name = "r_asis_pt"
HAnimSite60.DEF = "hanim_r_asis_pt"
HAnimSite60.translation = [-0.0887,1.0021,0.1112]

HAnimSegment55.children.append(HAnimSite60)
HAnimSite61 = x3d.HAnimSite()
HAnimSite61.name = "l_asis_pt"
HAnimSite61.DEF = "hanim_l_asis_pt"
HAnimSite61.translation = [0.0925,0.9983,0.1052]

HAnimSegment55.children.append(HAnimSite61)
HAnimSite62 = x3d.HAnimSite()
HAnimSite62.name = "r_psis_pt"
HAnimSite62.DEF = "hanim_r_psis_pt"
HAnimSite62.translation = [-0.0716,1.019,-0.1138]

HAnimSegment55.children.append(HAnimSite62)
HAnimSite63 = x3d.HAnimSite()
HAnimSite63.name = "l_psis_pt"
HAnimSite63.DEF = "hanim_l_psis_pt"
HAnimSite63.translation = [0.0774,1.019,-0.1151]

HAnimSegment55.children.append(HAnimSite63)
HAnimSite64 = x3d.HAnimSite()
HAnimSite64.name = "crotch_pt"
HAnimSite64.DEF = "hanim_crotch_pt"
HAnimSite64.translation = [0.0034,0.8266,0.0257]

HAnimSegment55.children.append(HAnimSite64)

HAnimJoint54.children.append(HAnimSegment55)
HAnimJoint65 = x3d.HAnimJoint()
HAnimJoint65.name = "l_hip"
HAnimJoint65.DEF = "hanim_l_hip"
HAnimJoint65.center = [0.0961,0.9124,-0.0001]
HAnimJoint65.ulimit = [0,0,0]
HAnimJoint65.llimit = [0,0,0]
HAnimSegment66 = x3d.HAnimSegment()
HAnimSegment66.name = "l_thigh"
HAnimSegment66.DEF = "hanim_l_thigh"
HAnimSite67 = x3d.HAnimSite()
HAnimSite67.name = "l_knee_crease_pt"
HAnimSite67.DEF = "hanim_l_knee_crease_pt"
HAnimSite67.translation = [0.0993,0.4881,-0.0309]

HAnimSegment66.children.append(HAnimSite67)
HAnimSite68 = x3d.HAnimSite()
HAnimSite68.name = "l_femoral_lateral_epicondyle_pt"
HAnimSite68.DEF = "hanim_l_femoral_lateral_epicondyle_pt"
HAnimSite68.translation = [0.1598,0.4967,0.0297]

HAnimSegment66.children.append(HAnimSite68)
HAnimSite69 = x3d.HAnimSite()
HAnimSite69.name = "l_femoral_medial_epicondyle_pt"
HAnimSite69.DEF = "hanim_l_femoral_medial_epicondyle_pt"
HAnimSite69.translation = [0.0398,0.4946,0.0303]

HAnimSegment66.children.append(HAnimSite69)

HAnimJoint65.children.append(HAnimSegment66)
HAnimJoint70 = x3d.HAnimJoint()
HAnimJoint70.name = "l_knee"
HAnimJoint70.DEF = "hanim_l_knee"
HAnimJoint70.center = [0.104,0.4867,0.0308]
HAnimJoint70.ulimit = [0,0,0]
HAnimJoint70.llimit = [0,0,0]
HAnimSegment71 = x3d.HAnimSegment()
HAnimSegment71.name = "l_calf"
HAnimSegment71.DEF = "hanim_l_calf"

HAnimJoint70.children.append(HAnimSegment71)
HAnimJoint72 = x3d.HAnimJoint()
HAnimJoint72.name = "l_talocrural"
HAnimJoint72.DEF = "hanim_l_talocrural"
HAnimJoint72.center = [0.1101,0.0656,-0.0736]
HAnimJoint72.ulimit = [0,0,0]
HAnimJoint72.llimit = [0,0,0]
HAnimSegment73 = x3d.HAnimSegment()
HAnimSegment73.name = "l_talus"
HAnimSegment73.DEF = "hanim_l_talus"
HAnimSite74 = x3d.HAnimSite()
HAnimSite74.name = "l_lateral_malleolus_pt"
HAnimSite74.DEF = "hanim_l_lateral_malleolus_pt"
HAnimSite74.translation = [0.1308,0.0597,-0.1032]

HAnimSegment73.children.append(HAnimSite74)
HAnimSite75 = x3d.HAnimSite()
HAnimSite75.name = "l_medial_malleolus_pt"
HAnimSite75.DEF = "hanim_l_medial_malleolus_pt"
HAnimSite75.translation = [0.089,0.0716,-0.0881]

HAnimSegment73.children.append(HAnimSite75)
HAnimSite76 = x3d.HAnimSite()
HAnimSite76.name = "l_sphyrion_pt"
HAnimSite76.DEF = "hanim_l_sphyrion_pt"
HAnimSite76.translation = [0.089,0.0575,-0.0943]

HAnimSegment73.children.append(HAnimSite76)
HAnimSite77 = x3d.HAnimSite()
HAnimSite77.name = "l_calcaneus_posterior_pt"
HAnimSite77.DEF = "hanim_l_calcaneus_posterior_pt"
HAnimSite77.translation = [0.0974,0.0259,-0.1171]

HAnimSegment73.children.append(HAnimSite77)

HAnimJoint72.children.append(HAnimSegment73)
HAnimJoint78 = x3d.HAnimJoint()
HAnimJoint78.name = "l_tarsometatarsal_2"
HAnimJoint78.DEF = "hanim_l_tarsometatarsal_2"
HAnimJoint78.center = [0.1086,0.0001,-0.0368]
HAnimJoint78.ulimit = [0,0,0]
HAnimJoint78.llimit = [0,0,0]
HAnimSegment79 = x3d.HAnimSegment()
HAnimSegment79.name = "l_metatarsal_2"
HAnimSegment79.DEF = "hanim_l_metatarsal_2"

HAnimJoint78.children.append(HAnimSegment79)
HAnimJoint80 = x3d.HAnimJoint()
HAnimJoint80.name = "l_metatarsophalangeal_2"
HAnimJoint80.DEF = "hanim_l_metatarsophalangeal_2"
HAnimJoint80.center = [0.1086,0.0001,0.0368]
HAnimJoint80.ulimit = [0,0,0]
HAnimJoint80.llimit = [0,0,0]
HAnimSegment81 = x3d.HAnimSegment()
HAnimSegment81.name = "l_tarsal_proximal_phalanx_2"
HAnimSegment81.DEF = "hanim_l_tarsal_proximal_phalanx_2"
HAnimSite82 = x3d.HAnimSite()
HAnimSite82.name = "l_metatarsal_phalanx_1_pt"
HAnimSite82.DEF = "hanim_l_metatarsal_phalanx_1_pt"
HAnimSite82.translation = [0.0816,0.0232,0.0106]

HAnimSegment81.children.append(HAnimSite82)

HAnimJoint80.children.append(HAnimSegment81)
HAnimJoint83 = x3d.HAnimJoint()
HAnimJoint83.name = "l_tarsal_distal_interphalangeal_2"
HAnimJoint83.DEF = "hanim_l_tarsal_distal_interphalangeal_2"
HAnimJoint83.center = [0.1086,0,0.0762]
HAnimJoint83.ulimit = [0,0,0]
HAnimJoint83.llimit = [0,0,0]
HAnimSegment84 = x3d.HAnimSegment()
HAnimSegment84.name = "l_tarsal_distal_phalanx_2"
HAnimSegment84.DEF = "hanim_l_tarsal_distal_phalanx_2"
HAnimSite85 = x3d.HAnimSite()
HAnimSite85.name = "l_forefoot_tip"
HAnimSite85.DEF = "hanim_l_forefoot_tip"
HAnimSite85.translation = [0.1354,0.0016,0.1476]

HAnimSegment84.children.append(HAnimSite85)
HAnimSite86 = x3d.HAnimSite()
HAnimSite86.name = "l_metatarsal_phalanx_5_pt"
HAnimSite86.DEF = "hanim_l_metatarsal_phalanx_5_pt"
HAnimSite86.translation = [0.1825,0.007,0.0928]

HAnimSegment84.children.append(HAnimSite86)
HAnimSite87 = x3d.HAnimSite()
HAnimSite87.name = "l_tarsal_distal_phalanx_2_pt"
HAnimSite87.DEF = "hanim_l_tarsal_distal_phalanx_2_pt"
HAnimSite87.translation = [0.1195,0.0079,0.1433]

HAnimSegment84.children.append(HAnimSite87)

HAnimJoint83.children.append(HAnimSegment84)

HAnimJoint80.children.append(HAnimJoint83)

HAnimJoint78.children.append(HAnimJoint80)

HAnimJoint72.children.append(HAnimJoint78)

HAnimJoint70.children.append(HAnimJoint72)

HAnimJoint65.children.append(HAnimJoint70)

HAnimJoint54.children.append(HAnimJoint65)
HAnimJoint88 = x3d.HAnimJoint()
HAnimJoint88.name = "r_hip"
HAnimJoint88.DEF = "hanim_r_hip"
HAnimJoint88.center = [-0.0961,0.9124,-0.0001]
HAnimJoint88.ulimit = [0,0,0]
HAnimJoint88.llimit = [0,0,0]
HAnimSegment89 = x3d.HAnimSegment()
HAnimSegment89.name = "r_thigh"
HAnimSegment89.DEF = "hanim_r_thigh"
HAnimSite90 = x3d.HAnimSite()
HAnimSite90.name = "r_knee_crease_pt"
HAnimSite90.DEF = "hanim_r_knee_crease_pt"
HAnimSite90.translation = [-0.0825,0.4932,-0.0326]

HAnimSegment89.children.append(HAnimSite90)
HAnimSite91 = x3d.HAnimSite()
HAnimSite91.name = "r_femoral_lateral_epicondyle_pt"
HAnimSite91.DEF = "hanim_r_femoral_lateral_epicondyle_pt"
HAnimSite91.translation = [-0.1421,0.4992,0.031]

HAnimSegment89.children.append(HAnimSite91)
HAnimSite92 = x3d.HAnimSite()
HAnimSite92.name = "r_femoral_medial_epicondyle_pt"
HAnimSite92.DEF = "hanim_r_femoral_medial_epicondyle_pt"
HAnimSite92.translation = [-0.0221,0.5014,0.0289]

HAnimSegment89.children.append(HAnimSite92)

HAnimJoint88.children.append(HAnimSegment89)
HAnimJoint93 = x3d.HAnimJoint()
HAnimJoint93.name = "r_knee"
HAnimJoint93.DEF = "hanim_r_knee"
HAnimJoint93.center = [-0.104,0.4867,0.0308]
HAnimJoint93.ulimit = [0,0,0]
HAnimJoint93.llimit = [0,0,0]
HAnimSegment94 = x3d.HAnimSegment()
HAnimSegment94.name = "r_calf"
HAnimSegment94.DEF = "hanim_r_calf"

HAnimJoint93.children.append(HAnimSegment94)
HAnimJoint95 = x3d.HAnimJoint()
HAnimJoint95.name = "r_talocrural"
HAnimJoint95.DEF = "hanim_r_talocrural"
HAnimJoint95.center = [-0.1101,0.0656,-0.0736]
HAnimJoint95.ulimit = [0,0,0]
HAnimJoint95.llimit = [0,0,0]
HAnimSegment96 = x3d.HAnimSegment()
HAnimSegment96.name = "r_talus"
HAnimSegment96.DEF = "hanim_r_talus"
HAnimSite97 = x3d.HAnimSite()
HAnimSite97.name = "r_lateral_malleolus_pt"
HAnimSite97.DEF = "hanim_r_lateral_malleolus_pt"
HAnimSite97.translation = [-0.1006,0.0658,-0.1075]

HAnimSegment96.children.append(HAnimSite97)
HAnimSite98 = x3d.HAnimSite()
HAnimSite98.name = "r_medial_malleolus_pt"
HAnimSite98.DEF = "hanim_r_medial_malleolus_pt"
HAnimSite98.translation = [-0.0591,0.076,-0.0928]

HAnimSegment96.children.append(HAnimSite98)
HAnimSite99 = x3d.HAnimSite()
HAnimSite99.name = "r_sphyrion_pt"
HAnimSite99.DEF = "hanim_r_sphyrion_pt"
HAnimSite99.translation = [-0.0603,0.061,-0.1002]

HAnimSegment96.children.append(HAnimSite99)
HAnimSite100 = x3d.HAnimSite()
HAnimSite100.name = "r_calcaneus_posterior_pt"
HAnimSite100.DEF = "hanim_r_calcaneus_posterior_pt"
HAnimSite100.translation = [-0.0692,0.0297,-0.1221]

HAnimSegment96.children.append(HAnimSite100)

HAnimJoint95.children.append(HAnimSegment96)
HAnimJoint101 = x3d.HAnimJoint()
HAnimJoint101.name = "r_tarsometatarsal_2"
HAnimJoint101.DEF = "hanim_r_tarsometatarsal_2"
HAnimJoint101.center = [-0.1086,0.0001,-0.0368]
HAnimJoint101.ulimit = [0,0,0]
HAnimJoint101.llimit = [0,0,0]
HAnimSegment102 = x3d.HAnimSegment()
HAnimSegment102.name = "r_metatarsal_2"
HAnimSegment102.DEF = "hanim_r_metatarsal_2"

HAnimJoint101.children.append(HAnimSegment102)
HAnimJoint103 = x3d.HAnimJoint()
HAnimJoint103.name = "r_metatarsophalangeal_2"
HAnimJoint103.DEF = "hanim_r_metatarsophalangeal_2"
HAnimJoint103.center = [-0.1086,0.0001,0.0368]
HAnimJoint103.ulimit = [0,0,0]
HAnimJoint103.llimit = [0,0,0]
HAnimSegment104 = x3d.HAnimSegment()
HAnimSegment104.name = "r_tarsal_proximal_phalanx_2"
HAnimSegment104.DEF = "hanim_r_tarsal_proximal_phalanx_2"
HAnimSite105 = x3d.HAnimSite()
HAnimSite105.name = "r_metatarsal_phalanx_1_pt"
HAnimSite105.DEF = "hanim_r_metatarsal_phalanx_1_pt"
HAnimSite105.translation = [-0.0521,0.026,0.0127]

HAnimSegment104.children.append(HAnimSite105)

HAnimJoint103.children.append(HAnimSegment104)
HAnimJoint106 = x3d.HAnimJoint()
HAnimJoint106.name = "r_tarsal_distal_interphalangeal_2"
HAnimJoint106.DEF = "hanim_r_tarsal_distal_interphalangeal_2"
HAnimJoint106.center = [-0.1086,0,0.0762]
HAnimJoint106.ulimit = [0,0,0]
HAnimJoint106.llimit = [0,0,0]
HAnimSegment107 = x3d.HAnimSegment()
HAnimSegment107.name = "r_tarsal_distal_phalanx_2"
HAnimSegment107.DEF = "hanim_r_tarsal_distal_phalanx_2"
HAnimSite108 = x3d.HAnimSite()
HAnimSite108.name = "r_forefoot_tip"
HAnimSite108.DEF = "hanim_r_forefoot_tip"
HAnimSite108.translation = [-0.1043,0.0227,0.145]

HAnimSegment107.children.append(HAnimSite108)
HAnimSite109 = x3d.HAnimSite()
HAnimSite109.name = "r_metatarsal_phalanx_5_pt"
HAnimSite109.DEF = "hanim_r_metatarsal_phalanx_5_pt"
HAnimSite109.translation = [-0.1523,0.0166,0.0895]

HAnimSegment107.children.append(HAnimSite109)
HAnimSite110 = x3d.HAnimSite()
HAnimSite110.name = "r_tarsal_distal_phalanx_2_pt"
HAnimSite110.DEF = "hanim_r_tarsal_distal_phalanx_2_pt"
HAnimSite110.translation = [-0.0883,0.0134,0.1383]

HAnimSegment107.children.append(HAnimSite110)

HAnimJoint106.children.append(HAnimSegment107)

HAnimJoint103.children.append(HAnimJoint106)

HAnimJoint101.children.append(HAnimJoint103)

HAnimJoint95.children.append(HAnimJoint101)

HAnimJoint93.children.append(HAnimJoint95)

HAnimJoint88.children.append(HAnimJoint93)

HAnimJoint54.children.append(HAnimJoint88)

HAnimJoint52.children.append(HAnimJoint54)
HAnimJoint111 = x3d.HAnimJoint()
HAnimJoint111.name = "vl5"
HAnimJoint111.DEF = "hanim_vl5"
HAnimJoint111.center = [0.0028,1.0568,-0.0776]
HAnimJoint111.ulimit = [0,0,0]
HAnimJoint111.llimit = [0,0,0]
HAnimSegment112 = x3d.HAnimSegment()
HAnimSegment112.name = "l5"
HAnimSegment112.DEF = "hanim_l5"
HAnimSite113 = x3d.HAnimSite()
HAnimSite113.name = "waist_preferred_posterior_pt"
HAnimSite113.DEF = "hanim_waist_preferred_posterior_pt"
HAnimSite113.translation = [0,1.0915,-0.1091]

HAnimSegment112.children.append(HAnimSite113)
HAnimSite114 = x3d.HAnimSite()
HAnimSite114.name = "navel_pt"
HAnimSite114.DEF = "hanim_navel_pt"
HAnimSite114.translation = [0.0069,1.0966,0.1017]

HAnimSegment112.children.append(HAnimSite114)

HAnimJoint111.children.append(HAnimSegment112)
HAnimJoint115 = x3d.HAnimJoint()
HAnimJoint115.name = "vl4"
HAnimJoint115.DEF = "hanim_vl4"
HAnimJoint115.center = [0.0035,1.0925,-0.0787]
HAnimJoint115.ulimit = [0,0,0]
HAnimJoint115.llimit = [0,0,0]
HAnimSegment116 = x3d.HAnimSegment()
HAnimSegment116.name = "l4"
HAnimSegment116.DEF = "hanim_l4"

HAnimJoint115.children.append(HAnimSegment116)
HAnimJoint117 = x3d.HAnimJoint()
HAnimJoint117.name = "vl3"
HAnimJoint117.DEF = "hanim_vl3"
HAnimJoint117.center = [0.0041,1.1276,-0.0796]
HAnimJoint117.ulimit = [0,0,0]
HAnimJoint117.llimit = [0,0,0]
HAnimSegment118 = x3d.HAnimSegment()
HAnimSegment118.name = "l3"
HAnimSegment118.DEF = "hanim_l3"

HAnimJoint117.children.append(HAnimSegment118)
HAnimJoint119 = x3d.HAnimJoint()
HAnimJoint119.name = "vl2"
HAnimJoint119.DEF = "hanim_vl2"
HAnimJoint119.center = [0.0045,1.1546,-0.08]
HAnimJoint119.ulimit = [0,0,0]
HAnimJoint119.llimit = [0,0,0]
HAnimSegment120 = x3d.HAnimSegment()
HAnimSegment120.name = "l2"
HAnimSegment120.DEF = "hanim_l2"
HAnimSite121 = x3d.HAnimSite()
HAnimSite121.name = "r_rib10_pt"
HAnimSite121.DEF = "hanim_r_rib10_pt"
HAnimSite121.translation = [-0.0711,1.1941,0.1016]

HAnimSegment120.children.append(HAnimSite121)
HAnimSite122 = x3d.HAnimSite()
HAnimSite122.name = "l_rib10_pt"
HAnimSite122.DEF = "hanim_l_rib10_pt"
HAnimSite122.translation = [0.0871,1.1925,0.0992]

HAnimSegment120.children.append(HAnimSite122)
HAnimSite123 = x3d.HAnimSite()
HAnimSite123.name = "rib10_midspine_pt"
HAnimSite123.DEF = "hanim_rib10_midspine_pt"
HAnimSite123.translation = [0.0049,1.1908,-0.1113]

HAnimSegment120.children.append(HAnimSite123)

HAnimJoint119.children.append(HAnimSegment120)
HAnimJoint124 = x3d.HAnimJoint()
HAnimJoint124.name = "vl1"
HAnimJoint124.DEF = "hanim_vl1"
HAnimJoint124.center = [0.0048,1.1912,-0.0805]
HAnimJoint124.ulimit = [0,0,0]
HAnimJoint124.llimit = [0,0,0]
HAnimSegment125 = x3d.HAnimSegment()
HAnimSegment125.name = "l1"
HAnimSegment125.DEF = "hanim_l1"

HAnimJoint124.children.append(HAnimSegment125)
HAnimJoint126 = x3d.HAnimJoint()
HAnimJoint126.name = "vt12"
HAnimJoint126.DEF = "hanim_vt12"
HAnimJoint126.center = [0.0051,1.2278,-0.0808]
HAnimJoint126.ulimit = [0,0,0]
HAnimJoint126.llimit = [0,0,0]
HAnimSegment127 = x3d.HAnimSegment()
HAnimSegment127.name = "t12"
HAnimSegment127.DEF = "hanim_t12"

HAnimJoint126.children.append(HAnimSegment127)
HAnimJoint128 = x3d.HAnimJoint()
HAnimJoint128.name = "vt11"
HAnimJoint128.DEF = "hanim_vt11"
HAnimJoint128.center = [0.0053,1.2679,-0.081]
HAnimJoint128.ulimit = [0,0,0]
HAnimJoint128.llimit = [0,0,0]
HAnimSegment129 = x3d.HAnimSegment()
HAnimSegment129.name = "t11"
HAnimSegment129.DEF = "hanim_t11"

HAnimJoint128.children.append(HAnimSegment129)
HAnimJoint130 = x3d.HAnimJoint()
HAnimJoint130.name = "vt10"
HAnimJoint130.DEF = "hanim_vt10"
HAnimJoint130.center = [0.0056,1.2848,-0.0822]
HAnimJoint130.ulimit = [0,0,0]
HAnimJoint130.llimit = [0,0,0]
HAnimSegment131 = x3d.HAnimSegment()
HAnimSegment131.name = "t10"
HAnimSegment131.DEF = "hanim_t10"
HAnimSite132 = x3d.HAnimSite()
HAnimSite132.name = "substernale_pt"
HAnimSite132.DEF = "hanim_substernale_pt"
HAnimSite132.translation = [0.0085,1.2995,0.1147]

HAnimSegment131.children.append(HAnimSite132)

HAnimJoint130.children.append(HAnimSegment131)
HAnimJoint133 = x3d.HAnimJoint()
HAnimJoint133.name = "vt9"
HAnimJoint133.DEF = "hanim_vt9"
HAnimJoint133.center = [0.0057,1.3126,-0.0838]
HAnimJoint133.ulimit = [0,0,0]
HAnimJoint133.llimit = [0,0,0]
HAnimSegment134 = x3d.HAnimSegment()
HAnimSegment134.name = "t9"
HAnimSegment134.DEF = "hanim_t9"
HAnimSite135 = x3d.HAnimSite()
HAnimSite135.name = "r_thelion_pt"
HAnimSite135.DEF = "hanim_r_thelion_pt"
HAnimSite135.translation = [-0.0736,1.3385,0.1217]

HAnimSegment134.children.append(HAnimSite135)
HAnimSite136 = x3d.HAnimSite()
HAnimSite136.name = "l_thelion_pt"
HAnimSite136.DEF = "hanim_l_thelion_pt"
HAnimSite136.translation = [0.0918,1.3382,0.1192]

HAnimSegment134.children.append(HAnimSite136)

HAnimJoint133.children.append(HAnimSegment134)
HAnimJoint137 = x3d.HAnimJoint()
HAnimJoint137.name = "vt8"
HAnimJoint137.DEF = "hanim_vt8"
HAnimJoint137.center = [0.0057,1.3382,-0.0845]
HAnimJoint137.ulimit = [0,0,0]
HAnimJoint137.llimit = [0,0,0]
HAnimSegment138 = x3d.HAnimSegment()
HAnimSegment138.name = "t8"
HAnimSegment138.DEF = "hanim_t8"

HAnimJoint137.children.append(HAnimSegment138)
HAnimJoint139 = x3d.HAnimJoint()
HAnimJoint139.name = "vt7"
HAnimJoint139.DEF = "hanim_vt7"
HAnimJoint139.center = [0.0058,1.3625,-0.0833]
HAnimJoint139.ulimit = [0,0,0]
HAnimJoint139.llimit = [0,0,0]
HAnimSegment140 = x3d.HAnimSegment()
HAnimSegment140.name = "t7"
HAnimSegment140.DEF = "hanim_t7"

HAnimJoint139.children.append(HAnimSegment140)
HAnimJoint141 = x3d.HAnimJoint()
HAnimJoint141.name = "vt6"
HAnimJoint141.DEF = "hanim_vt6"
HAnimJoint141.center = [0.0059,1.3866,-0.08]
HAnimJoint141.ulimit = [0,0,0]
HAnimJoint141.llimit = [0,0,0]
HAnimSegment142 = x3d.HAnimSegment()
HAnimSegment142.name = "t6"
HAnimSegment142.DEF = "hanim_t6"

HAnimJoint141.children.append(HAnimSegment142)
HAnimJoint143 = x3d.HAnimJoint()
HAnimJoint143.name = "vt5"
HAnimJoint143.DEF = "hanim_vt5"
HAnimJoint143.center = [0.006,1.4102,-0.0745]
HAnimJoint143.ulimit = [0,0,0]
HAnimJoint143.llimit = [0,0,0]
HAnimSegment144 = x3d.HAnimSegment()
HAnimSegment144.name = "t5"
HAnimSegment144.DEF = "hanim_t5"

HAnimJoint143.children.append(HAnimSegment144)
HAnimJoint145 = x3d.HAnimJoint()
HAnimJoint145.name = "vt4"
HAnimJoint145.DEF = "hanim_vt4"
HAnimJoint145.center = [0.0061,1.432,-0.0675]
HAnimJoint145.ulimit = [0,0,0]
HAnimJoint145.llimit = [0,0,0]
HAnimSegment146 = x3d.HAnimSegment()
HAnimSegment146.name = "t4"
HAnimSegment146.DEF = "hanim_t4"

HAnimJoint145.children.append(HAnimSegment146)
HAnimJoint147 = x3d.HAnimJoint()
HAnimJoint147.name = "vt3"
HAnimJoint147.DEF = "hanim_vt3"
HAnimJoint147.center = [0.0062,1.4583,-0.057]
HAnimJoint147.ulimit = [0,0,0]
HAnimJoint147.llimit = [0,0,0]
HAnimSegment148 = x3d.HAnimSegment()
HAnimSegment148.name = "t3"
HAnimSegment148.DEF = "hanim_t3"

HAnimJoint147.children.append(HAnimSegment148)
HAnimJoint149 = x3d.HAnimJoint()
HAnimJoint149.name = "vt2"
HAnimJoint149.DEF = "hanim_vt2"
HAnimJoint149.center = [0.0063,1.4761,-0.0484]
HAnimJoint149.ulimit = [0,0,0]
HAnimJoint149.llimit = [0,0,0]
HAnimSegment150 = x3d.HAnimSegment()
HAnimSegment150.name = "t2"
HAnimSegment150.DEF = "hanim_t2"

HAnimJoint149.children.append(HAnimSegment150)
HAnimJoint151 = x3d.HAnimJoint()
HAnimJoint151.name = "vt1"
HAnimJoint151.DEF = "hanim_vt1"
HAnimJoint151.center = [0.0065,1.4951,-0.0387]
HAnimJoint151.ulimit = [0,0,0]
HAnimJoint151.llimit = [0,0,0]
HAnimSegment152 = x3d.HAnimSegment()
HAnimSegment152.name = "t1"
HAnimSegment152.DEF = "hanim_t1"
HAnimSite153 = x3d.HAnimSite()
HAnimSite153.name = "suprasternale_pt"
HAnimSite153.DEF = "hanim_suprasternale_pt"
HAnimSite153.translation = [0.0084,1.4714,0.0551]

HAnimSegment152.children.append(HAnimSite153)
HAnimSite154 = x3d.HAnimSite()
HAnimSite154.name = "cervicale_pt"
HAnimSite154.DEF = "hanim_cervicale_pt"
HAnimSite154.translation = [0.0064,1.52,-0.0815]

HAnimSegment152.children.append(HAnimSite154)

HAnimJoint151.children.append(HAnimSegment152)
HAnimJoint155 = x3d.HAnimJoint()
HAnimJoint155.name = "vc7"
HAnimJoint155.DEF = "hanim_vc7"
HAnimJoint155.center = [0.0066,1.5132,-0.0301]
HAnimJoint155.ulimit = [0,0,0]
HAnimJoint155.llimit = [0,0,0]
HAnimSegment156 = x3d.HAnimSegment()
HAnimSegment156.name = "c7"
HAnimSegment156.DEF = "hanim_c7"
HAnimSite157 = x3d.HAnimSite()
HAnimSite157.name = "r_neck_base_pt"
HAnimSite157.DEF = "hanim_r_neck_base_pt"
HAnimSite157.translation = [-0.0419,1.5149,-0.022]

HAnimSegment156.children.append(HAnimSite157)
HAnimSite158 = x3d.HAnimSite()
HAnimSite158.name = "l_neck_base_pt"
HAnimSite158.DEF = "hanim_l_neck_base_pt"
HAnimSite158.translation = [0.0646,1.5141,-0.038]

HAnimSegment156.children.append(HAnimSite158)

HAnimJoint155.children.append(HAnimSegment156)
HAnimJoint159 = x3d.HAnimJoint()
HAnimJoint159.name = "vc6"
HAnimJoint159.DEF = "hanim_vc6"
HAnimJoint159.center = [0.0066,1.5357,-0.0143]
HAnimJoint159.ulimit = [0,0,0]
HAnimJoint159.llimit = [0,0,0]
HAnimSegment160 = x3d.HAnimSegment()
HAnimSegment160.name = "c6"
HAnimSegment160.DEF = "hanim_c6"

HAnimJoint159.children.append(HAnimSegment160)
HAnimJoint161 = x3d.HAnimJoint()
HAnimJoint161.name = "vc5"
HAnimJoint161.DEF = "hanim_vc5"
HAnimJoint161.center = [0.0066,1.552,-0.0082]
HAnimJoint161.ulimit = [0,0,0]
HAnimJoint161.llimit = [0,0,0]
HAnimSegment162 = x3d.HAnimSegment()
HAnimSegment162.name = "c5"
HAnimSegment162.DEF = "hanim_c5"

HAnimJoint161.children.append(HAnimSegment162)
HAnimJoint163 = x3d.HAnimJoint()
HAnimJoint163.name = "vc4"
HAnimJoint163.DEF = "hanim_vc4"
HAnimJoint163.center = [0.0066,1.5662,-0.0084]
HAnimJoint163.ulimit = [0,0,0]
HAnimJoint163.llimit = [0,0,0]
HAnimSegment164 = x3d.HAnimSegment()
HAnimSegment164.name = "c4"
HAnimSegment164.DEF = "hanim_c4"

HAnimJoint163.children.append(HAnimSegment164)
HAnimJoint165 = x3d.HAnimJoint()
HAnimJoint165.name = "vc3"
HAnimJoint165.DEF = "hanim_vc3"
HAnimJoint165.center = [0.0066,1.58,-0.0103]
HAnimJoint165.ulimit = [0,0,0]
HAnimJoint165.llimit = [0,0,0]
HAnimSegment166 = x3d.HAnimSegment()
HAnimSegment166.name = "c3"
HAnimSegment166.DEF = "hanim_c3"

HAnimJoint165.children.append(HAnimSegment166)
HAnimJoint167 = x3d.HAnimJoint()
HAnimJoint167.name = "vc2"
HAnimJoint167.DEF = "hanim_vc2"
HAnimJoint167.center = [0.0066,1.5928,-0.0103]
HAnimJoint167.ulimit = [0,0,0]
HAnimJoint167.llimit = [0,0,0]
HAnimSegment168 = x3d.HAnimSegment()
HAnimSegment168.name = "c2"
HAnimSegment168.DEF = "hanim_c2"

HAnimJoint167.children.append(HAnimSegment168)
HAnimJoint169 = x3d.HAnimJoint()
HAnimJoint169.name = "vc1"
HAnimJoint169.DEF = "hanim_vc1"
HAnimJoint169.center = [0.0066,1.6144,-0.0034]
HAnimJoint169.ulimit = [0,0,0]
HAnimJoint169.llimit = [0,0,0]
HAnimSegment170 = x3d.HAnimSegment()
HAnimSegment170.name = "c1"
HAnimSegment170.DEF = "hanim_c1"

HAnimJoint169.children.append(HAnimSegment170)
HAnimJoint171 = x3d.HAnimJoint()
HAnimJoint171.name = "skullbase"
HAnimJoint171.DEF = "hanim_skullbase"
HAnimJoint171.center = [0.0044,1.6209,0.0236]
HAnimJoint171.ulimit = [0,0,0]
HAnimJoint171.llimit = [0,0,0]
HAnimSegment172 = x3d.HAnimSegment()
HAnimSegment172.name = "skull"
HAnimSegment172.DEF = "hanim_skull"
HAnimSite173 = x3d.HAnimSite()
HAnimSite173.name = "skull_vertex_tip"
HAnimSite173.DEF = "hanim_skull_vertex_tip"
HAnimSite173.translation = [0.005,1.7504,0.0055]
#TODO move skull_tip x to zero, check others for symmetry

HAnimSegment172.children.append(HAnimSite173)
HAnimSite174 = x3d.HAnimSite()
HAnimSite174.name = "sellion_pt"
HAnimSite174.DEF = "hanim_sellion_pt"
HAnimSite174.translation = [0.0058,1.6316,0.0852]

HAnimSegment172.children.append(HAnimSite174)
HAnimSite175 = x3d.HAnimSite()
HAnimSite175.name = "r_infraorbitale_pt"
HAnimSite175.DEF = "hanim_r_infraorbitale_pt"
HAnimSite175.translation = [-0.0237,1.6171,0.0752]

HAnimSegment172.children.append(HAnimSite175)
HAnimSite176 = x3d.HAnimSite()
HAnimSite176.name = "l_infraorbitale_pt"
HAnimSite176.DEF = "hanim_l_infraorbitale_pt"
HAnimSite176.translation = [0.0341,1.6171,0.0752]

HAnimSegment172.children.append(HAnimSite176)
HAnimSite177 = x3d.HAnimSite()
HAnimSite177.name = "supramenton_pt"
HAnimSite177.DEF = "hanim_supramenton_pt"
HAnimSite177.translation = [0.0061,1.541,0.0805]

HAnimSegment172.children.append(HAnimSite177)
HAnimSite178 = x3d.HAnimSite()
HAnimSite178.name = "r_tragion_pt"
HAnimSite178.DEF = "hanim_r_tragion_pt"
HAnimSite178.translation = [-0.0646,1.6347,0.0302]

HAnimSegment172.children.append(HAnimSite178)
HAnimSite179 = x3d.HAnimSite()
HAnimSite179.name = "r_gonion_pt"
HAnimSite179.DEF = "hanim_r_gonion_pt"
HAnimSite179.translation = [-0.052,1.5529,0.0347]

HAnimSegment172.children.append(HAnimSite179)
HAnimSite180 = x3d.HAnimSite()
HAnimSite180.name = "l_tragion_pt"
HAnimSite180.DEF = "hanim_l_tragion_pt"
HAnimSite180.translation = [0.0739,1.6348,0.0282]

HAnimSegment172.children.append(HAnimSite180)
HAnimSite181 = x3d.HAnimSite()
HAnimSite181.name = "l_gonion_pt"
HAnimSite181.DEF = "hanim_l_gonion_pt"
HAnimSite181.translation = [0.0631,1.553,0.033]

HAnimSegment172.children.append(HAnimSite181)
HAnimSite182 = x3d.HAnimSite()
HAnimSite182.name = "nuchale_pt"
HAnimSite182.DEF = "hanim_nuchale_pt"
HAnimSite182.translation = [0.0039,1.5972,-0.0796]

HAnimSegment172.children.append(HAnimSite182)

HAnimJoint171.children.append(HAnimSegment172)
HAnimJoint183 = x3d.HAnimJoint()
HAnimJoint183.name = "l_eyeball_joint"
HAnimJoint183.DEF = "hanim_l_eyeball_joint"
HAnimJoint183.center = [0.0336,1.6332,0.0502]
HAnimJoint183.ulimit = [0,0,0]
HAnimJoint183.llimit = [0,0,0]
HAnimSegment184 = x3d.HAnimSegment()
HAnimSegment184.name = "l_eyeball"
HAnimSegment184.DEF = "hanim_l_eyeball"
HAnimSite185 = x3d.HAnimSite()
HAnimSite185.name = "l_eyeball_site_view"
HAnimSite185.DEF = "hanim_l_eyeball_site_view"
HAnimSite185.translation = [0.034,1.64,0.05]
Viewpoint186 = x3d.Viewpoint()
Viewpoint186.DEF = "hanim_l_eyeball_site_viewpoint"
Viewpoint186.description = "l_eyeball_site_viewpoint looking forward"
Viewpoint186.orientation = [0,1,0,3.141593]
Viewpoint186.position = [0,0,0]

HAnimSite185.children.append(Viewpoint186)

HAnimSegment184.children.append(HAnimSite185)

HAnimJoint183.children.append(HAnimSegment184)

HAnimJoint171.children.append(HAnimJoint183)
HAnimJoint187 = x3d.HAnimJoint()
HAnimJoint187.name = "l_eyelid_joint"
HAnimJoint187.DEF = "hanim_l_eyelid_joint"
HAnimJoint187.center = [0.0336,1.6332,0.0502]
HAnimJoint187.ulimit = [0,0,0]
HAnimJoint187.llimit = [0,0,0]
HAnimSegment188 = x3d.HAnimSegment()
HAnimSegment188.name = "l_eyelid"
HAnimSegment188.DEF = "hanim_l_eyelid"

HAnimJoint187.children.append(HAnimSegment188)

HAnimJoint171.children.append(HAnimJoint187)
HAnimJoint189 = x3d.HAnimJoint()
HAnimJoint189.name = "l_eyebrow_joint"
HAnimJoint189.DEF = "hanim_l_eyebrow_joint"
HAnimJoint189.center = [0.0336,1.635,0.0506]
HAnimJoint189.ulimit = [0,0,0]
HAnimJoint189.llimit = [0,0,0]
HAnimSegment190 = x3d.HAnimSegment()
HAnimSegment190.name = "l_eyebrow"
HAnimSegment190.DEF = "hanim_l_eyebrow"

HAnimJoint189.children.append(HAnimSegment190)

HAnimJoint171.children.append(HAnimJoint189)
HAnimJoint191 = x3d.HAnimJoint()
HAnimJoint191.name = "r_eyeball_joint"
HAnimJoint191.DEF = "hanim_r_eyeball_joint"
HAnimJoint191.center = [-0.0336,1.6332,0.0502]
HAnimJoint191.ulimit = [0,0,0]
HAnimJoint191.llimit = [0,0,0]
HAnimSegment192 = x3d.HAnimSegment()
HAnimSegment192.name = "r_eyeball"
HAnimSegment192.DEF = "hanim_r_eyeball"
HAnimSite193 = x3d.HAnimSite()
HAnimSite193.name = "r_eyeball_site_view"
HAnimSite193.DEF = "hanim_r_eyeball_site_view"
HAnimSite193.translation = [-0.034,1.64,0.05]
Viewpoint194 = x3d.Viewpoint()
Viewpoint194.DEF = "hanim_r_eyeball_site_viewpoint"
Viewpoint194.description = "r_eyeball_site_viewpoint looking forward"
Viewpoint194.orientation = [0,1,0,3.141593]
Viewpoint194.position = [0,0,0]

HAnimSite193.children.append(Viewpoint194)

HAnimSegment192.children.append(HAnimSite193)

HAnimJoint191.children.append(HAnimSegment192)

HAnimJoint171.children.append(HAnimJoint191)
HAnimJoint195 = x3d.HAnimJoint()
HAnimJoint195.name = "r_eyelid_joint"
HAnimJoint195.DEF = "hanim_r_eyelid_joint"
HAnimJoint195.center = [-0.0336,1.6332,0.0502]
HAnimJoint195.ulimit = [0,0,0]
HAnimJoint195.llimit = [0,0,0]
HAnimSegment196 = x3d.HAnimSegment()
HAnimSegment196.name = "r_eyelid"
HAnimSegment196.DEF = "hanim_r_eyelid"

HAnimJoint195.children.append(HAnimSegment196)

HAnimJoint171.children.append(HAnimJoint195)
HAnimJoint197 = x3d.HAnimJoint()
HAnimJoint197.name = "r_eyebrow_joint"
HAnimJoint197.DEF = "hanim_r_eyebrow_joint"
HAnimJoint197.center = [-0.0336,1.635,0.0506]
HAnimJoint197.ulimit = [0,0,0]
HAnimJoint197.llimit = [0,0,0]
HAnimSegment198 = x3d.HAnimSegment()
HAnimSegment198.name = "r_eyebrow"
HAnimSegment198.DEF = "hanim_r_eyebrow"

HAnimJoint197.children.append(HAnimSegment198)

HAnimJoint171.children.append(HAnimJoint197)
HAnimJoint199 = x3d.HAnimJoint()
HAnimJoint199.name = "temporomandibular"
HAnimJoint199.DEF = "hanim_temporomandibular"
HAnimJoint199.center = [0,1.63,0.015]
HAnimJoint199.ulimit = [0,0,0]
HAnimJoint199.llimit = [0,0,0]
#Single joint, single segment for jaw, two sites for left/right TMJs https://en.wikipedia.org/wiki/Temporomandibular_joint
HAnimSegment200 = x3d.HAnimSegment()
HAnimSegment200.name = "jaw"
HAnimSegment200.DEF = "hanim_jaw"
HAnimSite201 = x3d.HAnimSite()
HAnimSite201.name = "temporomandibular_l_site_pt"
HAnimSite201.DEF = "hanim_temporomandibular_l_site_pt"
HAnimSite201.translation = [0.045,1.63,0]

HAnimSegment200.children.append(HAnimSite201)
HAnimSite202 = x3d.HAnimSite()
HAnimSite202.name = "temporomandibular_r_site_pt"
HAnimSite202.DEF = "hanim_temporomandibular_r_site_pt"
HAnimSite202.translation = [-0.045,1.63,0]

HAnimSegment200.children.append(HAnimSite202)

HAnimJoint199.children.append(HAnimSegment200)

HAnimJoint171.children.append(HAnimJoint199)

HAnimJoint169.children.append(HAnimJoint171)

HAnimJoint167.children.append(HAnimJoint169)

HAnimJoint165.children.append(HAnimJoint167)

HAnimJoint163.children.append(HAnimJoint165)

HAnimJoint161.children.append(HAnimJoint163)

HAnimJoint159.children.append(HAnimJoint161)

HAnimJoint155.children.append(HAnimJoint159)

HAnimJoint151.children.append(HAnimJoint155)
HAnimJoint203 = x3d.HAnimJoint()
HAnimJoint203.name = "l_sternoclavicular"
HAnimJoint203.DEF = "hanim_l_sternoclavicular"
HAnimJoint203.center = [0.082,1.4488,-0.0353]
HAnimJoint203.ulimit = [0,0,0]
HAnimJoint203.llimit = [0,0,0]
HAnimSegment204 = x3d.HAnimSegment()
HAnimSegment204.name = "l_clavicle"
HAnimSegment204.DEF = "hanim_l_clavicle"
HAnimSite205 = x3d.HAnimSite()
HAnimSite205.name = "l_clavicle_pt"
HAnimSite205.DEF = "hanim_l_clavicle_pt"
HAnimSite205.translation = [0.0271,1.4943,0.0394]

HAnimSegment204.children.append(HAnimSite205)
HAnimSite206 = x3d.HAnimSite()
HAnimSite206.name = "l_acromion_pt"
HAnimSite206.DEF = "hanim_l_acromion_pt"
HAnimSite206.translation = [0.2032,1.476,-0.049]

HAnimSegment204.children.append(HAnimSite206)
HAnimSite207 = x3d.HAnimSite()
HAnimSite207.name = "l_axilla_proximal_pt"
HAnimSite207.DEF = "hanim_l_axilla_proximal_pt"
HAnimSite207.translation = [0.1777,1.4065,-0.0075]

HAnimSegment204.children.append(HAnimSite207)
HAnimSite208 = x3d.HAnimSite()
HAnimSite208.name = "l_axilla_distal_pt"
HAnimSite208.DEF = "hanim_l_axilla_distal_pt"
HAnimSite208.translation = [0.1706,1.4072,-0.0875]

HAnimSegment204.children.append(HAnimSite208)

HAnimJoint203.children.append(HAnimSegment204)
HAnimJoint209 = x3d.HAnimJoint()
HAnimJoint209.name = "l_acromioclavicular"
HAnimJoint209.DEF = "hanim_l_acromioclavicular"
HAnimJoint209.center = [0.0962,1.4269,-0.0424]
HAnimJoint209.ulimit = [0,0,0]
HAnimJoint209.llimit = [0,0,0]
HAnimSegment210 = x3d.HAnimSegment()
HAnimSegment210.name = "l_scapula"
HAnimSegment210.DEF = "hanim_l_scapula"

HAnimJoint209.children.append(HAnimSegment210)
HAnimJoint211 = x3d.HAnimJoint()
HAnimJoint211.name = "l_shoulder"
HAnimJoint211.DEF = "hanim_l_shoulder"
HAnimJoint211.center = [0.2029,1.4376,-0.0387]
HAnimJoint211.ulimit = [0,0,0]
HAnimJoint211.llimit = [0,0,0]
HAnimSegment212 = x3d.HAnimSegment()
HAnimSegment212.name = "l_upperarm"
HAnimSegment212.DEF = "hanim_l_upperarm"
HAnimSite213 = x3d.HAnimSite()
HAnimSite213.name = "l_humeral_lateral_epicondyle_pt"
HAnimSite213.DEF = "hanim_l_humeral_lateral_epicondyle_pt"
HAnimSite213.translation = [0.228,1.1482,-0.11]

HAnimSegment212.children.append(HAnimSite213)

HAnimJoint211.children.append(HAnimSegment212)
HAnimJoint214 = x3d.HAnimJoint()
HAnimJoint214.name = "l_elbow"
HAnimJoint214.DEF = "hanim_l_elbow"
HAnimJoint214.center = [0.2014,1.1357,-0.0682]
HAnimJoint214.ulimit = [0,0,0]
HAnimJoint214.llimit = [0,0,0]
HAnimSegment215 = x3d.HAnimSegment()
HAnimSegment215.name = "l_forearm"
HAnimSegment215.DEF = "hanim_l_forearm"
HAnimSite216 = x3d.HAnimSite()
HAnimSite216.name = "l_radial_styloid_pt"
HAnimSite216.DEF = "hanim_l_radial_styloid_pt"
HAnimSite216.translation = [0.1901,0.8645,-0.0415]

HAnimSegment215.children.append(HAnimSite216)
HAnimSite217 = x3d.HAnimSite()
HAnimSite217.name = "l_olecranon_pt"
HAnimSite217.DEF = "hanim_l_olecranon_pt"
HAnimSite217.translation = [0.1962,1.1375,-0.1123]

HAnimSegment215.children.append(HAnimSite217)
HAnimSite218 = x3d.HAnimSite()
HAnimSite218.name = "l_humeral_medial_epicondyle_pt"
HAnimSite218.DEF = "hanim_l_humeral_medial_epicondyle_pt"
HAnimSite218.translation = [0.1735,1.1272,-0.1113]

HAnimSegment215.children.append(HAnimSite218)
HAnimSite219 = x3d.HAnimSite()
HAnimSite219.name = "l_radiale_pt"
HAnimSite219.DEF = "hanim_l_radiale_pt"
HAnimSite219.translation = [0.2182,1.1212,-0.1167]

HAnimSegment215.children.append(HAnimSite219)

HAnimJoint214.children.append(HAnimSegment215)
HAnimJoint220 = x3d.HAnimJoint()
HAnimJoint220.name = "l_radiocarpal"
HAnimJoint220.DEF = "hanim_l_radiocarpal"
HAnimJoint220.center = [0.1984,0.8663,-0.0583]
HAnimJoint220.ulimit = [0,0,0]
HAnimJoint220.llimit = [0,0,0]
HAnimSegment221 = x3d.HAnimSegment()
HAnimSegment221.name = "l_carpal"
HAnimSegment221.DEF = "hanim_l_carpal"
HAnimSite222 = x3d.HAnimSite()
HAnimSite222.name = "l_metacarpal_phalanx_2_pt"
HAnimSite222.DEF = "hanim_l_metacarpal_phalanx_2_pt"
HAnimSite222.translation = [0.2009,0.8139,-0.0237]

HAnimSegment221.children.append(HAnimSite222)
HAnimSite223 = x3d.HAnimSite()
HAnimSite223.name = "l_ulnar_styloid_pt"
HAnimSite223.DEF = "hanim_l_ulnar_styloid_pt"
HAnimSite223.translation = [0.2142,0.8529,-0.0648]

HAnimSegment221.children.append(HAnimSite223)
HAnimSite224 = x3d.HAnimSite()
HAnimSite224.name = "l_metacarpal_phalanx_5_pt"
HAnimSite224.DEF = "hanim_l_metacarpal_phalanx_5_pt"
HAnimSite224.translation = [0.1929,0.786,-0.1122]

HAnimSegment221.children.append(HAnimSite224)
HAnimSite225 = x3d.HAnimSite()
HAnimSite225.name = "l_hand_front_view"
HAnimSite225.DEF = "hanim_l_hand_front_view"
HAnimSite225.translation = [0.3,0.75,0.45]
Viewpoint226 = x3d.Viewpoint()
Viewpoint226.DEF = "hanim_l_hand_front_viewpoint"
Viewpoint226.centerOfRotation = [0,0.7,0]
Viewpoint226.description = "left hand front"
Viewpoint226.position = [0,0,0]

HAnimSite225.children.append(Viewpoint226)

HAnimSegment221.children.append(HAnimSite225)

HAnimJoint220.children.append(HAnimSegment221)
HAnimJoint227 = x3d.HAnimJoint()
HAnimJoint227.name = "l_carpometacarpal_1"
HAnimJoint227.DEF = "hanim_l_carpometacarpal_1"
HAnimJoint227.center = [0.1924,0.8472,-0.0534]
HAnimJoint227.ulimit = [0,0,0]
HAnimJoint227.llimit = [0,0,0]
HAnimSegment228 = x3d.HAnimSegment()
HAnimSegment228.name = "l_metacarpal_1"
HAnimSegment228.DEF = "hanim_l_metacarpal_1"

HAnimJoint227.children.append(HAnimSegment228)
HAnimJoint229 = x3d.HAnimJoint()
HAnimJoint229.name = "l_metacarpophalangeal_1"
HAnimJoint229.DEF = "hanim_l_metacarpophalangeal_1"
HAnimJoint229.center = [0.1951,0.8226,0.0246]
HAnimJoint229.ulimit = [0,0,0]
HAnimJoint229.llimit = [0,0,0]
HAnimSegment230 = x3d.HAnimSegment()
HAnimSegment230.name = "l_carpal_proximal_phalanx_1"
HAnimSegment230.DEF = "hanim_l_carpal_proximal_phalanx_1"

HAnimJoint229.children.append(HAnimSegment230)
HAnimJoint231 = x3d.HAnimJoint()
HAnimJoint231.name = "l_carpal_interphalangeal_1"
HAnimJoint231.DEF = "hanim_l_carpal_interphalangeal_1"
HAnimJoint231.center = [0.1955,0.8159,0.0464]
HAnimJoint231.ulimit = [0,0,0]
HAnimJoint231.llimit = [0,0,0]
HAnimSegment232 = x3d.HAnimSegment()
HAnimSegment232.name = "l_carpal_distal_phalanx_1"
HAnimSegment232.DEF = "hanim_l_carpal_distal_phalanx_1"
HAnimSite233 = x3d.HAnimSite()
HAnimSite233.name = "l_carpal_distal_phalanx_1_tip"
HAnimSite233.DEF = "hanim_l_carpal_distal_phalanx_1_tip"
HAnimSite233.translation = [0.1982,0.8061,0.0759]

HAnimSegment232.children.append(HAnimSite233)

HAnimJoint231.children.append(HAnimSegment232)

HAnimJoint229.children.append(HAnimJoint231)

HAnimJoint227.children.append(HAnimJoint229)

HAnimJoint220.children.append(HAnimJoint227)
HAnimJoint234 = x3d.HAnimJoint()
HAnimJoint234.name = "l_carpometacarpal_2"
HAnimJoint234.DEF = "hanim_l_carpometacarpal_2"
HAnimJoint234.center = [0.1983,0.8024,-0.028]
HAnimJoint234.ulimit = [0,0,0]
HAnimJoint234.llimit = [0,0,0]
HAnimSegment235 = x3d.HAnimSegment()
HAnimSegment235.name = "l_metacarpal_2"
HAnimSegment235.DEF = "hanim_l_metacarpal_2"

HAnimJoint234.children.append(HAnimSegment235)
HAnimJoint236 = x3d.HAnimJoint()
HAnimJoint236.name = "l_metacarpophalangeal_2"
HAnimJoint236.DEF = "hanim_l_metacarpophalangeal_2"
HAnimJoint236.center = [0.1983,0.7815,-0.028]
HAnimJoint236.ulimit = [0,0,0]
HAnimJoint236.llimit = [0,0,0]
HAnimSegment237 = x3d.HAnimSegment()
HAnimSegment237.name = "l_carpal_proximal_phalanx_2"
HAnimSegment237.DEF = "hanim_l_carpal_proximal_phalanx_2"

HAnimJoint236.children.append(HAnimSegment237)
HAnimJoint238 = x3d.HAnimJoint()
HAnimJoint238.name = "l_carpal_proximal_interphalangeal_2"
HAnimJoint238.DEF = "hanim_l_carpal_proximal_interphalangeal_2"
HAnimJoint238.center = [0.2017,0.7363,-0.0248]
HAnimJoint238.ulimit = [0,0,0]
HAnimJoint238.llimit = [0,0,0]
HAnimSegment239 = x3d.HAnimSegment()
HAnimSegment239.name = "l_carpal_middle_phalanx_2"
HAnimSegment239.DEF = "hanim_l_carpal_middle_phalanx_2"

HAnimJoint238.children.append(HAnimSegment239)
HAnimJoint240 = x3d.HAnimJoint()
HAnimJoint240.name = "l_carpal_distal_interphalangeal_2"
HAnimJoint240.DEF = "hanim_l_carpal_distal_interphalangeal_2"
HAnimJoint240.center = [0.2028,0.7139,-0.0236]
HAnimJoint240.ulimit = [0,0,0]
HAnimJoint240.llimit = [0,0,0]
HAnimSegment241 = x3d.HAnimSegment()
HAnimSegment241.name = "l_carpal_distal_phalanx_2"
HAnimSegment241.DEF = "hanim_l_carpal_distal_phalanx_2"
HAnimSite242 = x3d.HAnimSite()
HAnimSite242.name = "l_carpal_distal_phalanx_2_tip"
HAnimSite242.DEF = "hanim_l_carpal_distal_phalanx_2_tip"
HAnimSite242.translation = [0.2089,0.6858,-0.0245]

HAnimSegment241.children.append(HAnimSite242)
HAnimSite243 = x3d.HAnimSite()
HAnimSite243.name = "l_dactylion_pt"
HAnimSite243.DEF = "hanim_l_dactylion_pt"
HAnimSite243.translation = [0.2056,0.6743,-0.0482]

HAnimSegment241.children.append(HAnimSite243)

HAnimJoint240.children.append(HAnimSegment241)

HAnimJoint238.children.append(HAnimJoint240)

HAnimJoint236.children.append(HAnimJoint238)

HAnimJoint234.children.append(HAnimJoint236)

HAnimJoint220.children.append(HAnimJoint234)
HAnimJoint244 = x3d.HAnimJoint()
HAnimJoint244.name = "l_carpometacarpal_3"
HAnimJoint244.DEF = "hanim_l_carpometacarpal_3"
HAnimJoint244.center = [0.1987,0.8029,-0.053]
HAnimJoint244.ulimit = [0,0,0]
HAnimJoint244.llimit = [0,0,0]
HAnimSegment245 = x3d.HAnimSegment()
HAnimSegment245.name = "l_metacarpal_3"
HAnimSegment245.DEF = "hanim_l_metacarpal_3"

HAnimJoint244.children.append(HAnimSegment245)
HAnimJoint246 = x3d.HAnimJoint()
HAnimJoint246.name = "l_metacarpophalangeal_3"
HAnimJoint246.DEF = "hanim_l_metacarpophalangeal_3"
HAnimJoint246.center = [0.1987,0.7818,-0.053]
HAnimJoint246.ulimit = [0,0,0]
HAnimJoint246.llimit = [0,0,0]
HAnimSegment247 = x3d.HAnimSegment()
HAnimSegment247.name = "l_carpal_proximal_phalanx_3"
HAnimSegment247.DEF = "hanim_l_carpal_proximal_phalanx_3"

HAnimJoint246.children.append(HAnimSegment247)
HAnimJoint248 = x3d.HAnimJoint()
HAnimJoint248.name = "l_carpal_proximal_interphalangeal_3"
HAnimJoint248.DEF = "hanim_l_carpal_proximal_interphalangeal_3"
HAnimJoint248.center = [0.2013,0.7273,-0.0503]
HAnimJoint248.ulimit = [0,0,0]
HAnimJoint248.llimit = [0,0,0]
HAnimSegment249 = x3d.HAnimSegment()
HAnimSegment249.name = "l_carpal_middle_phalanx_3"
HAnimSegment249.DEF = "hanim_l_carpal_middle_phalanx_3"

HAnimJoint248.children.append(HAnimSegment249)
HAnimJoint250 = x3d.HAnimJoint()
HAnimJoint250.name = "l_carpal_distal_interphalangeal_3"
HAnimJoint250.DEF = "hanim_l_carpal_distal_interphalangeal_3"
HAnimJoint250.center = [0.2026,0.7011,-0.0494]
HAnimJoint250.ulimit = [0,0,0]
HAnimJoint250.llimit = [0,0,0]
HAnimSegment251 = x3d.HAnimSegment()
HAnimSegment251.name = "l_carpal_distal_phalanx_3"
HAnimSegment251.DEF = "hanim_l_carpal_distal_phalanx_3"
HAnimSite252 = x3d.HAnimSite()
HAnimSite252.name = "l_carpal_distal_phalanx_3_tip"
HAnimSite252.DEF = "hanim_l_carpal_distal_phalanx_3_tip"
HAnimSite252.translation = [0.208,0.6731,-0.0491]

HAnimSegment251.children.append(HAnimSite252)

HAnimJoint250.children.append(HAnimSegment251)

HAnimJoint248.children.append(HAnimJoint250)

HAnimJoint246.children.append(HAnimJoint248)

HAnimJoint244.children.append(HAnimJoint246)

HAnimJoint220.children.append(HAnimJoint244)
HAnimJoint253 = x3d.HAnimJoint()
HAnimJoint253.name = "l_carpometacarpal_4"
HAnimJoint253.DEF = "hanim_l_carpometacarpal_4"
HAnimJoint253.center = [0.1956,0.8019,-0.0794]
HAnimJoint253.ulimit = [0,0,0]
HAnimJoint253.llimit = [0,0,0]
HAnimSegment254 = x3d.HAnimSegment()
HAnimSegment254.name = "l_metacarpal_4"
HAnimSegment254.DEF = "hanim_l_metacarpal_4"

HAnimJoint253.children.append(HAnimSegment254)
HAnimJoint255 = x3d.HAnimJoint()
HAnimJoint255.name = "l_metacarpophalangeal_4"
HAnimJoint255.DEF = "hanim_l_metacarpophalangeal_4"
HAnimJoint255.center = [0.1956,0.7815,-0.0794]
HAnimJoint255.ulimit = [0,0,0]
HAnimJoint255.llimit = [0,0,0]
HAnimSegment256 = x3d.HAnimSegment()
HAnimSegment256.name = "l_carpal_proximal_phalanx_4"
HAnimSegment256.DEF = "hanim_l_carpal_proximal_phalanx_4"

HAnimJoint255.children.append(HAnimSegment256)
HAnimJoint257 = x3d.HAnimJoint()
HAnimJoint257.name = "l_carpal_proximal_interphalangeal_4"
HAnimJoint257.DEF = "hanim_l_carpal_proximal_interphalangeal_4"
HAnimJoint257.center = [0.1973,0.7287,-0.0777]
HAnimJoint257.ulimit = [0,0,0]
HAnimJoint257.llimit = [0,0,0]
HAnimSegment258 = x3d.HAnimSegment()
HAnimSegment258.name = "l_carpal_middle_phalanx_4"
HAnimSegment258.DEF = "hanim_l_carpal_middle_phalanx_4"

HAnimJoint257.children.append(HAnimSegment258)
HAnimJoint259 = x3d.HAnimJoint()
HAnimJoint259.name = "l_carpal_distal_interphalangeal_4"
HAnimJoint259.DEF = "hanim_l_carpal_distal_interphalangeal_4"
HAnimJoint259.center = [0.1983,0.7045,-0.0767]
HAnimJoint259.ulimit = [0,0,0]
HAnimJoint259.llimit = [0,0,0]
HAnimSegment260 = x3d.HAnimSegment()
HAnimSegment260.name = "l_carpal_distal_phalanx_4"
HAnimSegment260.DEF = "hanim_l_carpal_distal_phalanx_4"
HAnimSite261 = x3d.HAnimSite()
HAnimSite261.name = "l_carpal_distal_phalanx_4_tip"
HAnimSite261.DEF = "hanim_l_carpal_distal_phalanx_4_tip"
HAnimSite261.translation = [0.2035,0.675,-0.0756]

HAnimSegment260.children.append(HAnimSite261)

HAnimJoint259.children.append(HAnimSegment260)

HAnimJoint257.children.append(HAnimJoint259)

HAnimJoint255.children.append(HAnimJoint257)

HAnimJoint253.children.append(HAnimJoint255)

HAnimJoint220.children.append(HAnimJoint253)
HAnimJoint262 = x3d.HAnimJoint()
HAnimJoint262.name = "l_carpometacarpal_5"
HAnimJoint262.DEF = "hanim_l_carpometacarpal_5"
HAnimJoint262.center = [0.1925,0.8066,-0.1036]
HAnimJoint262.ulimit = [0,0,0]
HAnimJoint262.llimit = [0,0,0]
HAnimSegment263 = x3d.HAnimSegment()
HAnimSegment263.name = "l_metacarpal_5"
HAnimSegment263.DEF = "hanim_l_metacarpal_5"

HAnimJoint262.children.append(HAnimSegment263)
HAnimJoint264 = x3d.HAnimJoint()
HAnimJoint264.name = "l_metacarpophalangeal_5"
HAnimJoint264.DEF = "hanim_l_metacarpophalangeal_5"
HAnimJoint264.center = [0.1925,0.7866,-0.1036]
HAnimJoint264.ulimit = [0,0,0]
HAnimJoint264.llimit = [0,0,0]
HAnimSegment265 = x3d.HAnimSegment()
HAnimSegment265.name = "l_carpal_proximal_phalanx_5"
HAnimSegment265.DEF = "hanim_l_carpal_proximal_phalanx_5"

HAnimJoint264.children.append(HAnimSegment265)
HAnimJoint266 = x3d.HAnimJoint()
HAnimJoint266.name = "l_carpal_proximal_interphalangeal_5"
HAnimJoint266.DEF = "hanim_l_carpal_proximal_interphalangeal_5"
HAnimJoint266.center = [0.1938,0.7452,-0.1024]
HAnimJoint266.ulimit = [0,0,0]
HAnimJoint266.llimit = [0,0,0]
HAnimSegment267 = x3d.HAnimSegment()
HAnimSegment267.name = "l_carpal_middle_phalanx_5"
HAnimSegment267.DEF = "hanim_l_carpal_middle_phalanx_5"

HAnimJoint266.children.append(HAnimSegment267)
HAnimJoint268 = x3d.HAnimJoint()
HAnimJoint268.name = "l_carpal_distal_interphalangeal_5"
HAnimJoint268.DEF = "hanim_l_carpal_distal_interphalangeal_5"
HAnimJoint268.center = [0.1948,0.7277,-0.1017]
HAnimJoint268.ulimit = [0,0,0]
HAnimJoint268.llimit = [0,0,0]
HAnimSegment269 = x3d.HAnimSegment()
HAnimSegment269.name = "l_carpal_distal_phalanx_5"
HAnimSegment269.DEF = "hanim_l_carpal_distal_phalanx_5"
HAnimSite270 = x3d.HAnimSite()
HAnimSite270.name = "l_carpal_distal_phalanx_5_tip"
HAnimSite270.DEF = "hanim_l_carpal_distal_phalanx_5_tip"
HAnimSite270.translation = [0.2014,0.7009,-0.1012]

HAnimSegment269.children.append(HAnimSite270)

HAnimJoint268.children.append(HAnimSegment269)

HAnimJoint266.children.append(HAnimJoint268)

HAnimJoint264.children.append(HAnimJoint266)

HAnimJoint262.children.append(HAnimJoint264)

HAnimJoint220.children.append(HAnimJoint262)

HAnimJoint214.children.append(HAnimJoint220)

HAnimJoint211.children.append(HAnimJoint214)

HAnimJoint209.children.append(HAnimJoint211)

HAnimJoint203.children.append(HAnimJoint209)

HAnimJoint151.children.append(HAnimJoint203)
HAnimJoint271 = x3d.HAnimJoint()
HAnimJoint271.name = "r_sternoclavicular"
HAnimJoint271.DEF = "hanim_r_sternoclavicular"
HAnimJoint271.center = [-0.082,1.4488,-0.0353]
HAnimJoint271.ulimit = [0,0,0]
HAnimJoint271.llimit = [0,0,0]
HAnimSegment272 = x3d.HAnimSegment()
HAnimSegment272.name = "r_clavicle"
HAnimSegment272.DEF = "hanim_r_clavicle"
HAnimSite273 = x3d.HAnimSite()
HAnimSite273.name = "r_clavicle_pt"
HAnimSite273.DEF = "hanim_r_clavicle_pt"
HAnimSite273.translation = [-0.0115,1.4943,0.04]

HAnimSegment272.children.append(HAnimSite273)
HAnimSite274 = x3d.HAnimSite()
HAnimSite274.name = "r_acromion_pt"
HAnimSite274.DEF = "hanim_r_acromion_pt"
HAnimSite274.translation = [-0.1905,1.4791,-0.0431]

HAnimSegment272.children.append(HAnimSite274)
HAnimSite275 = x3d.HAnimSite()
HAnimSite275.name = "r_axilla_proximal_pt"
HAnimSite275.DEF = "hanim_r_axilla_proximal_pt"
HAnimSite275.translation = [-0.1626,1.4072,-0.0031]

HAnimSegment272.children.append(HAnimSite275)
HAnimSite276 = x3d.HAnimSite()
HAnimSite276.name = "r_axilla_distal_pt"
HAnimSite276.DEF = "hanim_r_axilla_distal_pt"
HAnimSite276.translation = [-0.1603,1.4098,-0.0826]

HAnimSegment272.children.append(HAnimSite276)

HAnimJoint271.children.append(HAnimSegment272)
HAnimJoint277 = x3d.HAnimJoint()
HAnimJoint277.name = "r_acromioclavicular"
HAnimJoint277.DEF = "hanim_r_acromioclavicular"
HAnimJoint277.center = [-0.0962,1.4269,-0.0424]
HAnimJoint277.ulimit = [0,0,0]
HAnimJoint277.llimit = [0,0,0]
HAnimSegment278 = x3d.HAnimSegment()
HAnimSegment278.name = "r_scapula"
HAnimSegment278.DEF = "hanim_r_scapula"

HAnimJoint277.children.append(HAnimSegment278)
HAnimJoint279 = x3d.HAnimJoint()
HAnimJoint279.name = "r_shoulder"
HAnimJoint279.DEF = "hanim_r_shoulder"
HAnimJoint279.center = [-0.2029,1.4376,-0.0387]
HAnimJoint279.ulimit = [0,0,0]
HAnimJoint279.llimit = [0,0,0]
HAnimSegment280 = x3d.HAnimSegment()
HAnimSegment280.name = "r_upperarm"
HAnimSegment280.DEF = "hanim_r_upperarm"
HAnimSite281 = x3d.HAnimSite()
HAnimSite281.name = "r_humeral_lateral_epicondyle_pt"
HAnimSite281.DEF = "hanim_r_humeral_lateral_epicondyle_pt"
HAnimSite281.translation = [-0.2224,1.1517,-0.1033]

HAnimSegment280.children.append(HAnimSite281)

HAnimJoint279.children.append(HAnimSegment280)
HAnimJoint282 = x3d.HAnimJoint()
HAnimJoint282.name = "r_elbow"
HAnimJoint282.DEF = "hanim_r_elbow"
HAnimJoint282.center = [-0.2014,1.1357,-0.0682]
HAnimJoint282.ulimit = [0,0,0]
HAnimJoint282.llimit = [0,0,0]
HAnimSegment283 = x3d.HAnimSegment()
HAnimSegment283.name = "r_forearm"
HAnimSegment283.DEF = "hanim_r_forearm"
HAnimSite284 = x3d.HAnimSite()
HAnimSite284.name = "r_radial_styloid_pt"
HAnimSite284.DEF = "hanim_r_radial_styloid_pt"
HAnimSite284.translation = [-0.1884,0.8676,-0.036]

HAnimSegment283.children.append(HAnimSite284)
HAnimSite285 = x3d.HAnimSite()
HAnimSite285.name = "r_olecranon_pt"
HAnimSite285.DEF = "hanim_r_olecranon_pt"
HAnimSite285.translation = [-0.1907,1.1405,-0.1065]

HAnimSegment283.children.append(HAnimSite285)
HAnimSite286 = x3d.HAnimSite()
HAnimSite286.name = "r_humeral_medial_epicondyle_pt"
HAnimSite286.DEF = "hanim_r_humeral_medial_epicondyle_pt"
HAnimSite286.translation = [-0.168,1.1298,-0.1062]

HAnimSegment283.children.append(HAnimSite286)
HAnimSite287 = x3d.HAnimSite()
HAnimSite287.name = "r_radiale_pt"
HAnimSite287.DEF = "hanim_r_radiale_pt"
HAnimSite287.translation = [-0.213,1.1305,-0.1091]

HAnimSegment283.children.append(HAnimSite287)

HAnimJoint282.children.append(HAnimSegment283)
HAnimJoint288 = x3d.HAnimJoint()
HAnimJoint288.name = "r_radiocarpal"
HAnimJoint288.DEF = "hanim_r_radiocarpal"
HAnimJoint288.center = [-0.1984,0.8663,-0.0583]
HAnimJoint288.ulimit = [0,0,0]
HAnimJoint288.llimit = [0,0,0]
HAnimSegment289 = x3d.HAnimSegment()
HAnimSegment289.name = "r_carpal"
HAnimSegment289.DEF = "hanim_r_carpal"
HAnimSite290 = x3d.HAnimSite()
HAnimSite290.name = "r_metacarpal_phalanx_2_pt"
HAnimSite290.DEF = "hanim_r_metacarpal_phalanx_2_pt"
HAnimSite290.translation = [-0.1977,0.8169,-0.0177]

HAnimSegment289.children.append(HAnimSite290)
HAnimSite291 = x3d.HAnimSite()
HAnimSite291.name = "r_ulnar_styloid_pt"
HAnimSite291.DEF = "hanim_r_ulnar_styloid_pt"
HAnimSite291.translation = [-0.2117,0.8562,-0.0584]

HAnimSegment289.children.append(HAnimSite291)
HAnimSite292 = x3d.HAnimSite()
HAnimSite292.name = "r_metacarpal_phalanx_5_pt"
HAnimSite292.DEF = "hanim_r_metacarpal_phalanx_5_pt"
HAnimSite292.translation = [-0.1929,0.789,-0.1064]

HAnimSegment289.children.append(HAnimSite292)
HAnimSite293 = x3d.HAnimSite()
HAnimSite293.name = "r_hand_front_view"
HAnimSite293.DEF = "hanim_r_hand_front_view"
HAnimSite293.translation = [-0.3,0.75,0.45]
Viewpoint294 = x3d.Viewpoint()
Viewpoint294.DEF = "hanim_r_hand_front_viewpoint"
Viewpoint294.centerOfRotation = [0,0.7,0]
Viewpoint294.description = "right hand front"
Viewpoint294.position = [0,0,0]

HAnimSite293.children.append(Viewpoint294)

HAnimSegment289.children.append(HAnimSite293)

HAnimJoint288.children.append(HAnimSegment289)
HAnimJoint295 = x3d.HAnimJoint()
HAnimJoint295.name = "r_carpometacarpal_1"
HAnimJoint295.DEF = "hanim_r_carpometacarpal_1"
HAnimJoint295.center = [-0.1924,0.8472,-0.0534]
HAnimJoint295.ulimit = [0,0,0]
HAnimJoint295.llimit = [0,0,0]
HAnimSegment296 = x3d.HAnimSegment()
HAnimSegment296.name = "r_metacarpal_1"
HAnimSegment296.DEF = "hanim_r_metacarpal_1"

HAnimJoint295.children.append(HAnimSegment296)
HAnimJoint297 = x3d.HAnimJoint()
HAnimJoint297.name = "r_metacarpophalangeal_1"
HAnimJoint297.DEF = "hanim_r_metacarpophalangeal_1"
HAnimJoint297.center = [-0.1951,0.8226,0.0246]
HAnimJoint297.ulimit = [0,0,0]
HAnimJoint297.llimit = [0,0,0]
HAnimSegment298 = x3d.HAnimSegment()
HAnimSegment298.name = "r_carpal_proximal_phalanx_1"
HAnimSegment298.DEF = "hanim_r_carpal_proximal_phalanx_1"

HAnimJoint297.children.append(HAnimSegment298)
HAnimJoint299 = x3d.HAnimJoint()
HAnimJoint299.name = "r_carpal_interphalangeal_1"
HAnimJoint299.DEF = "hanim_r_carpal_interphalangeal_1"
HAnimJoint299.center = [-0.1955,0.8159,0.0464]
HAnimJoint299.ulimit = [0,0,0]
HAnimJoint299.llimit = [0,0,0]
HAnimSegment300 = x3d.HAnimSegment()
HAnimSegment300.name = "r_carpal_distal_phalanx_1"
HAnimSegment300.DEF = "hanim_r_carpal_distal_phalanx_1"
HAnimSite301 = x3d.HAnimSite()
HAnimSite301.name = "r_carpal_distal_phalanx_1_tip"
HAnimSite301.DEF = "hanim_r_carpal_distal_phalanx_1_tip"
HAnimSite301.translation = [-0.1869,0.809,0.082]

HAnimSegment300.children.append(HAnimSite301)

HAnimJoint299.children.append(HAnimSegment300)

HAnimJoint297.children.append(HAnimJoint299)

HAnimJoint295.children.append(HAnimJoint297)

HAnimJoint288.children.append(HAnimJoint295)
HAnimJoint302 = x3d.HAnimJoint()
HAnimJoint302.name = "r_carpometacarpal_2"
HAnimJoint302.DEF = "hanim_r_carpometacarpal_2"
HAnimJoint302.center = [-0.1983,0.8024,-0.028]
HAnimJoint302.ulimit = [0,0,0]
HAnimJoint302.llimit = [0,0,0]
HAnimSegment303 = x3d.HAnimSegment()
HAnimSegment303.name = "r_metacarpal_2"
HAnimSegment303.DEF = "hanim_r_metacarpal_2"

HAnimJoint302.children.append(HAnimSegment303)
HAnimJoint304 = x3d.HAnimJoint()
HAnimJoint304.name = "r_metacarpophalangeal_2"
HAnimJoint304.DEF = "hanim_r_metacarpophalangeal_2"
HAnimJoint304.center = [-0.1983,0.7815,-0.028]
HAnimJoint304.ulimit = [0,0,0]
HAnimJoint304.llimit = [0,0,0]
HAnimSegment305 = x3d.HAnimSegment()
HAnimSegment305.name = "r_carpal_proximal_phalanx_2"
HAnimSegment305.DEF = "hanim_r_carpal_proximal_phalanx_2"

HAnimJoint304.children.append(HAnimSegment305)
HAnimJoint306 = x3d.HAnimJoint()
HAnimJoint306.name = "r_carpal_proximal_interphalangeal_2"
HAnimJoint306.DEF = "hanim_r_carpal_proximal_interphalangeal_2"
HAnimJoint306.center = [-0.2017,0.7363,-0.0248]
HAnimJoint306.ulimit = [0,0,0]
HAnimJoint306.llimit = [0,0,0]
HAnimSegment307 = x3d.HAnimSegment()
HAnimSegment307.name = "r_carpal_middle_phalanx_2"
HAnimSegment307.DEF = "hanim_r_carpal_middle_phalanx_2"

HAnimJoint306.children.append(HAnimSegment307)
HAnimJoint308 = x3d.HAnimJoint()
HAnimJoint308.name = "r_carpal_distal_interphalangeal_2"
HAnimJoint308.DEF = "hanim_r_carpal_distal_interphalangeal_2"
HAnimJoint308.center = [-0.2028,0.7139,-0.0236]
HAnimJoint308.ulimit = [0,0,0]
HAnimJoint308.llimit = [0,0,0]
HAnimSegment309 = x3d.HAnimSegment()
HAnimSegment309.name = "r_carpal_distal_phalanx_2"
HAnimSegment309.DEF = "hanim_r_carpal_distal_phalanx_2"
HAnimSite310 = x3d.HAnimSite()
HAnimSite310.name = "r_carpal_distal_phalanx_2_tip"
HAnimSite310.DEF = "hanim_r_carpal_distal_phalanx_2_tip"
HAnimSite310.translation = [-0.198,0.6883,-0.018]

HAnimSegment309.children.append(HAnimSite310)
HAnimSite311 = x3d.HAnimSite()
HAnimSite311.name = "r_dactylion_pt"
HAnimSite311.DEF = "hanim_r_dactylion_pt"
HAnimSite311.translation = [-0.1941,0.6772,-0.0423]

HAnimSegment309.children.append(HAnimSite311)

HAnimJoint308.children.append(HAnimSegment309)

HAnimJoint306.children.append(HAnimJoint308)

HAnimJoint304.children.append(HAnimJoint306)

HAnimJoint302.children.append(HAnimJoint304)

HAnimJoint288.children.append(HAnimJoint302)
HAnimJoint312 = x3d.HAnimJoint()
HAnimJoint312.name = "r_carpometacarpal_3"
HAnimJoint312.DEF = "hanim_r_carpometacarpal_3"
HAnimJoint312.center = [-0.1987,0.8029,-0.053]
HAnimJoint312.ulimit = [0,0,0]
HAnimJoint312.llimit = [0,0,0]
HAnimSegment313 = x3d.HAnimSegment()
HAnimSegment313.name = "r_metacarpal_3"
HAnimSegment313.DEF = "hanim_r_metacarpal_3"

HAnimJoint312.children.append(HAnimSegment313)
HAnimJoint314 = x3d.HAnimJoint()
HAnimJoint314.name = "r_metacarpophalangeal_3"
HAnimJoint314.DEF = "hanim_r_metacarpophalangeal_3"
HAnimJoint314.center = [-0.1987,0.7818,-0.053]
HAnimJoint314.ulimit = [0,0,0]
HAnimJoint314.llimit = [0,0,0]
HAnimSegment315 = x3d.HAnimSegment()
HAnimSegment315.name = "r_carpal_proximal_phalanx_3"
HAnimSegment315.DEF = "hanim_r_carpal_proximal_phalanx_3"

HAnimJoint314.children.append(HAnimSegment315)
HAnimJoint316 = x3d.HAnimJoint()
HAnimJoint316.name = "r_carpal_proximal_interphalangeal_3"
HAnimJoint316.DEF = "hanim_r_carpal_proximal_interphalangeal_3"
HAnimJoint316.center = [-0.2013,0.7273,-0.0503]
HAnimJoint316.ulimit = [0,0,0]
HAnimJoint316.llimit = [0,0,0]
HAnimSegment317 = x3d.HAnimSegment()
HAnimSegment317.name = "r_carpal_middle_phalanx_3"
HAnimSegment317.DEF = "hanim_r_carpal_middle_phalanx_3"

HAnimJoint316.children.append(HAnimSegment317)
HAnimJoint318 = x3d.HAnimJoint()
HAnimJoint318.name = "r_carpal_distal_interphalangeal_3"
HAnimJoint318.DEF = "hanim_r_carpal_distal_interphalangeal_3"
HAnimJoint318.center = [-0.2026,0.7011,-0.0494]
HAnimJoint318.ulimit = [0,0,0]
HAnimJoint318.llimit = [0,0,0]
HAnimSegment319 = x3d.HAnimSegment()
HAnimSegment319.name = "r_carpal_distal_phalanx_3"
HAnimSegment319.DEF = "hanim_r_carpal_distal_phalanx_3"
HAnimSite320 = x3d.HAnimSite()
HAnimSite320.name = "r_carpal_distal_phalanx_3_tip"
HAnimSite320.DEF = "hanim_r_carpal_distal_phalanx_3_tip"
HAnimSite320.translation = [-0.1969,0.6758,-0.0427]

HAnimSegment319.children.append(HAnimSite320)

HAnimJoint318.children.append(HAnimSegment319)

HAnimJoint316.children.append(HAnimJoint318)

HAnimJoint314.children.append(HAnimJoint316)

HAnimJoint312.children.append(HAnimJoint314)

HAnimJoint288.children.append(HAnimJoint312)
HAnimJoint321 = x3d.HAnimJoint()
HAnimJoint321.name = "r_carpometacarpal_4"
HAnimJoint321.DEF = "hanim_r_carpometacarpal_4"
HAnimJoint321.center = [-0.1956,0.8019,-0.0794]
HAnimJoint321.ulimit = [0,0,0]
HAnimJoint321.llimit = [0,0,0]
HAnimSegment322 = x3d.HAnimSegment()
HAnimSegment322.name = "r_metacarpal_4"
HAnimSegment322.DEF = "hanim_r_metacarpal_4"

HAnimJoint321.children.append(HAnimSegment322)
HAnimJoint323 = x3d.HAnimJoint()
HAnimJoint323.name = "r_metacarpophalangeal_4"
HAnimJoint323.DEF = "hanim_r_metacarpophalangeal_4"
HAnimJoint323.center = [-0.1956,0.7815,-0.0794]
HAnimJoint323.ulimit = [0,0,0]
HAnimJoint323.llimit = [0,0,0]
HAnimSegment324 = x3d.HAnimSegment()
HAnimSegment324.name = "r_carpal_proximal_phalanx_4"
HAnimSegment324.DEF = "hanim_r_carpal_proximal_phalanx_4"

HAnimJoint323.children.append(HAnimSegment324)
HAnimJoint325 = x3d.HAnimJoint()
HAnimJoint325.name = "r_carpal_proximal_interphalangeal_4"
HAnimJoint325.DEF = "hanim_r_carpal_proximal_interphalangeal_4"
HAnimJoint325.center = [-0.1973,0.7287,-0.0777]
HAnimJoint325.ulimit = [0,0,0]
HAnimJoint325.llimit = [0,0,0]
HAnimSegment326 = x3d.HAnimSegment()
HAnimSegment326.name = "r_carpal_middle_phalanx_4"
HAnimSegment326.DEF = "hanim_r_carpal_middle_phalanx_4"

HAnimJoint325.children.append(HAnimSegment326)
HAnimJoint327 = x3d.HAnimJoint()
HAnimJoint327.name = "r_carpal_distal_interphalangeal_4"
HAnimJoint327.DEF = "hanim_r_carpal_distal_interphalangeal_4"
HAnimJoint327.center = [-0.1983,0.7045,-0.0767]
HAnimJoint327.ulimit = [0,0,0]
HAnimJoint327.llimit = [0,0,0]
HAnimSegment328 = x3d.HAnimSegment()
HAnimSegment328.name = "r_carpal_distal_phalanx_4"
HAnimSegment328.DEF = "hanim_r_carpal_distal_phalanx_4"
HAnimSite329 = x3d.HAnimSite()
HAnimSite329.name = "r_carpal_distal_phalanx_4_tip"
HAnimSite329.DEF = "hanim_r_carpal_distal_phalanx_4_tip"
HAnimSite329.translation = [-0.1934,0.6778,-0.0693]

HAnimSegment328.children.append(HAnimSite329)

HAnimJoint327.children.append(HAnimSegment328)

HAnimJoint325.children.append(HAnimJoint327)

HAnimJoint323.children.append(HAnimJoint325)

HAnimJoint321.children.append(HAnimJoint323)

HAnimJoint288.children.append(HAnimJoint321)
HAnimJoint330 = x3d.HAnimJoint()
HAnimJoint330.name = "r_carpometacarpal_5"
HAnimJoint330.DEF = "hanim_r_carpometacarpal_5"
HAnimJoint330.center = [-0.1925,0.8066,-0.1036]
HAnimJoint330.ulimit = [0,0,0]
HAnimJoint330.llimit = [0,0,0]
HAnimSegment331 = x3d.HAnimSegment()
HAnimSegment331.name = "r_metacarpal_5"
HAnimSegment331.DEF = "hanim_r_metacarpal_5"

HAnimJoint330.children.append(HAnimSegment331)
HAnimJoint332 = x3d.HAnimJoint()
HAnimJoint332.name = "r_metacarpophalangeal_5"
HAnimJoint332.DEF = "hanim_r_metacarpophalangeal_5"
HAnimJoint332.center = [-0.1925,0.7866,-0.1036]
HAnimJoint332.ulimit = [0,0,0]
HAnimJoint332.llimit = [0,0,0]
HAnimSegment333 = x3d.HAnimSegment()
HAnimSegment333.name = "r_carpal_proximal_phalanx_5"
HAnimSegment333.DEF = "hanim_r_carpal_proximal_phalanx_5"

HAnimJoint332.children.append(HAnimSegment333)
HAnimJoint334 = x3d.HAnimJoint()
HAnimJoint334.name = "r_carpal_proximal_interphalangeal_5"
HAnimJoint334.DEF = "hanim_r_carpal_proximal_interphalangeal_5"
HAnimJoint334.center = [-0.1938,0.7452,-0.1024]
HAnimJoint334.ulimit = [0,0,0]
HAnimJoint334.llimit = [0,0,0]
HAnimSegment335 = x3d.HAnimSegment()
HAnimSegment335.name = "r_carpal_middle_phalanx_5"
HAnimSegment335.DEF = "hanim_r_carpal_middle_phalanx_5"

HAnimJoint334.children.append(HAnimSegment335)
HAnimJoint336 = x3d.HAnimJoint()
HAnimJoint336.name = "r_carpal_distal_interphalangeal_5"
HAnimJoint336.DEF = "hanim_r_carpal_distal_interphalangeal_5"
HAnimJoint336.center = [-0.1948,0.7277,-0.1017]
HAnimJoint336.ulimit = [0,0,0]
HAnimJoint336.llimit = [0,0,0]
HAnimSegment337 = x3d.HAnimSegment()
HAnimSegment337.name = "r_carpal_distal_phalanx_5"
HAnimSegment337.DEF = "hanim_r_carpal_distal_phalanx_5"
HAnimSite338 = x3d.HAnimSite()
HAnimSite338.name = "r_carpal_distal_phalanx_5_tip"
HAnimSite338.DEF = "hanim_r_carpal_distal_phalanx_5_tip"
HAnimSite338.translation = [-0.1938,0.7035,-0.0949]

HAnimSegment337.children.append(HAnimSite338)

HAnimJoint336.children.append(HAnimSegment337)

HAnimJoint334.children.append(HAnimJoint336)

HAnimJoint332.children.append(HAnimJoint334)

HAnimJoint330.children.append(HAnimJoint332)

HAnimJoint288.children.append(HAnimJoint330)

HAnimJoint282.children.append(HAnimJoint288)

HAnimJoint279.children.append(HAnimJoint282)

HAnimJoint277.children.append(HAnimJoint279)

HAnimJoint271.children.append(HAnimJoint277)

HAnimJoint151.children.append(HAnimJoint271)

HAnimJoint149.children.append(HAnimJoint151)

HAnimJoint147.children.append(HAnimJoint149)

HAnimJoint145.children.append(HAnimJoint147)

HAnimJoint143.children.append(HAnimJoint145)

HAnimJoint141.children.append(HAnimJoint143)

HAnimJoint139.children.append(HAnimJoint141)

HAnimJoint137.children.append(HAnimJoint139)

HAnimJoint133.children.append(HAnimJoint137)

HAnimJoint130.children.append(HAnimJoint133)

HAnimJoint128.children.append(HAnimJoint130)

HAnimJoint126.children.append(HAnimJoint128)

HAnimJoint124.children.append(HAnimJoint126)

HAnimJoint119.children.append(HAnimJoint124)

HAnimJoint117.children.append(HAnimJoint119)

HAnimJoint115.children.append(HAnimJoint117)

HAnimJoint111.children.append(HAnimJoint115)

HAnimJoint52.children.append(HAnimJoint111)

HAnimHumanoid43.skeleton.append(HAnimJoint52)
HAnimSite339 = x3d.HAnimSite()
HAnimSite339.name = "l_inclined_view"
HAnimSite339.DEF = "hanim_l_inclined_view"
HAnimSite339.rotation = [-0.113,0.993,0.0347,0.671]
HAnimSite339.translation = [1.62,1.05,2.06]
Viewpoint340 = x3d.Viewpoint()
Viewpoint340.DEF = "hanim_l_inclined_viewpoint"
Viewpoint340.description = "left inclined"
Viewpoint340.position = [0,0,0]

HAnimSite339.children.append(Viewpoint340)

HAnimHumanoid43.viewpoints.append(HAnimSite339)
HAnimSite341 = x3d.HAnimSite()
HAnimSite341.name = "r_inclined_view"
HAnimSite341.DEF = "hanim_r_inclined_view"
HAnimSite341.rotation = [-0.113,-0.993,0.0347,0.671]
HAnimSite341.translation = [-1.62,1.05,2.06]
Viewpoint342 = x3d.Viewpoint()
Viewpoint342.DEF = "hanim_r_inclined_viewpoint"
Viewpoint342.centerOfRotation = [0,0.9,0]
Viewpoint342.description = "right inclined"
Viewpoint342.position = [0,0,0]

HAnimSite341.children.append(Viewpoint342)

HAnimHumanoid43.viewpoints.append(HAnimSite341)
HAnimSite343 = x3d.HAnimSite()
HAnimSite343.name = "front_view"
HAnimSite343.DEF = "hanim_front_view"
HAnimSite343.translation = [0,0.85,2.58]
Viewpoint344 = x3d.Viewpoint()
Viewpoint344.DEF = "hanim_front_viewpoint"
Viewpoint344.centerOfRotation = [0,0.9,0]
Viewpoint344.description = "front"
Viewpoint344.position = [0,0,0]

HAnimSite343.children.append(Viewpoint344)

HAnimHumanoid43.viewpoints.append(HAnimSite343)
HAnimSite345 = x3d.HAnimSite()
HAnimSite345.name = "back_view"
HAnimSite345.DEF = "hanim_back_view"
HAnimSite345.rotation = [0,1,0,3.14]
HAnimSite345.translation = [0,0.85,-2.58]
Viewpoint346 = x3d.Viewpoint()
Viewpoint346.DEF = "hanim_back_viewpoint"
Viewpoint346.centerOfRotation = [0,0.9,0]
Viewpoint346.description = "back"
Viewpoint346.position = [0,0,0]

HAnimSite345.children.append(Viewpoint346)

HAnimHumanoid43.viewpoints.append(HAnimSite345)
HAnimSite347 = x3d.HAnimSite()
HAnimSite347.name = "l_side_view"
HAnimSite347.DEF = "hanim_l_side_view"
HAnimSite347.rotation = [0,1,0,1.5708]
HAnimSite347.translation = [2.6,0.854,0]
Viewpoint348 = x3d.Viewpoint()
Viewpoint348.DEF = "hanim_l_side_viewpoint"
Viewpoint348.centerOfRotation = [0,0.9,0]
Viewpoint348.description = "left side"
Viewpoint348.position = [0,0,0]

HAnimSite347.children.append(Viewpoint348)

HAnimHumanoid43.viewpoints.append(HAnimSite347)
HAnimSite349 = x3d.HAnimSite()
HAnimSite349.name = "Top_view"
HAnimSite349.DEF = "hanim_Top_view"
HAnimSite349.rotation = [1,0,0,-1.57]
HAnimSite349.translation = [0,3.5,0]
Viewpoint350 = x3d.Viewpoint()
Viewpoint350.DEF = "hanim_Top_viewpoint"
Viewpoint350.centerOfRotation = [0,0.9,0]
Viewpoint350.description = "Top"
Viewpoint350.position = [0,0,0]

HAnimSite349.children.append(Viewpoint350)

HAnimHumanoid43.viewpoints.append(HAnimSite349)
HAnimSite351 = x3d.HAnimSite()
HAnimSite351.name = "front_close_view"
HAnimSite351.DEF = "hanim_front_close_view"
HAnimSite351.translation = [0,0.854,1.575]
Viewpoint352 = x3d.Viewpoint()
Viewpoint352.DEF = "hanim_front_close_viewpoint"
Viewpoint352.centerOfRotation = [0,0,1.575]
Viewpoint352.description = "front close"
Viewpoint352.position = [0,0,0]

HAnimSite351.children.append(Viewpoint352)

HAnimHumanoid43.viewpoints.append(HAnimSite351)
HAnimSite353 = x3d.HAnimSite()
HAnimSite353.name = "side_close_view"
HAnimSite353.DEF = "hanim_side_close_view"
HAnimSite353.rotation = [0,1,0,1.5708]
HAnimSite353.translation = [1.56,0.854,0]
Viewpoint354 = x3d.Viewpoint()
Viewpoint354.DEF = "hanim_side_close_viewpoint"
Viewpoint354.centerOfRotation = [1.6,0,0]
Viewpoint354.description = "side close"
Viewpoint354.position = [0,0,0]

HAnimSite353.children.append(Viewpoint354)

HAnimHumanoid43.viewpoints.append(HAnimSite353)
HAnimSite355 = x3d.HAnimSite()
HAnimSite355.name = "head_front_close_view"
HAnimSite355.DEF = "hanim_head_front_close_view"
HAnimSite355.translation = [0,1.5,1]
Viewpoint356 = x3d.Viewpoint()
Viewpoint356.DEF = "hanim_head_front_close_viewpoint"
Viewpoint356.centerOfRotation = [0,0,1]
Viewpoint356.description = "head front close"
Viewpoint356.position = [0,0,0]

HAnimSite355.children.append(Viewpoint356)

HAnimHumanoid43.viewpoints.append(HAnimSite355)
HAnimSite357 = x3d.HAnimSite()
HAnimSite357.name = "chest_front_close_view"
HAnimSite357.DEF = "hanim_chest_front_close_view"
HAnimSite357.translation = [0,1.2,1]
Viewpoint358 = x3d.Viewpoint()
Viewpoint358.DEF = "hanim_chest_front_close_viewpoint"
Viewpoint358.centerOfRotation = [0,0,1]
Viewpoint358.description = "chest front close"
Viewpoint358.position = [0,0,0]

HAnimSite357.children.append(Viewpoint358)

HAnimHumanoid43.viewpoints.append(HAnimSite357)
HAnimSite359 = x3d.HAnimSite()
HAnimSite359.name = "pelvis_front_close_view"
HAnimSite359.DEF = "hanim_pelvis_front_close_view"
HAnimSite359.translation = [0,0.8,1]
Viewpoint360 = x3d.Viewpoint()
Viewpoint360.DEF = "hanim_pelvis_front_close_viewpoint"
Viewpoint360.centerOfRotation = [0,0,1]
Viewpoint360.description = "pelvis front close"
Viewpoint360.position = [0,0,0]

HAnimSite359.children.append(Viewpoint360)

HAnimHumanoid43.viewpoints.append(HAnimSite359)
HAnimSite361 = x3d.HAnimSite()
HAnimSite361.name = "knees_front_close_view"
HAnimSite361.DEF = "hanim_knees_front_close_view"
HAnimSite361.translation = [0,0.4,1]
Viewpoint362 = x3d.Viewpoint()
Viewpoint362.DEF = "hanim_knees_front_close_viewpoint"
Viewpoint362.centerOfRotation = [0,0.4,0]
Viewpoint362.description = "knees front close"
Viewpoint362.position = [0,0,0]

HAnimSite361.children.append(Viewpoint362)

HAnimHumanoid43.viewpoints.append(HAnimSite361)
HAnimSite363 = x3d.HAnimSite()
HAnimSite363.name = "feet_front_close_view"
HAnimSite363.DEF = "hanim_feet_front_close_view"
HAnimSite363.translation = [0,0,1]
Viewpoint364 = x3d.Viewpoint()
Viewpoint364.DEF = "hanim_feet_front_close_viewpoint"
Viewpoint364.description = "feet front close"
Viewpoint364.position = [0,0,0]

HAnimSite363.children.append(Viewpoint364)

HAnimHumanoid43.viewpoints.append(HAnimSite363)
HAnimSite365 = x3d.HAnimSite()
HAnimSite365.name = "eye_level_view"
HAnimSite365.DEF = "hanim_eye_level_view"
HAnimSite365.translation = [0,1.6332,0.0502]
Viewpoint366 = x3d.Viewpoint()
Viewpoint366.DEF = "hanim_eye_level_viewpoint"
Viewpoint366.description = "eye level looking forward"
Viewpoint366.orientation = [0,1,0,3.141593]
Viewpoint366.position = [0,0,0]

HAnimSite365.children.append(Viewpoint366)

HAnimHumanoid43.viewpoints.append(HAnimSite365)
HAnimSite367 = x3d.HAnimSite()
HAnimSite367.USE = "hanim_l_eyeball_site_view"

HAnimHumanoid43.sites.append(HAnimSite367)
HAnimSite368 = x3d.HAnimSite()
HAnimSite368.USE = "hanim_r_eyeball_site_view"

HAnimHumanoid43.sites.append(HAnimSite368)
HAnimSite369 = x3d.HAnimSite()
HAnimSite369.USE = "hanim_l_hand_front_view"

HAnimHumanoid43.sites.append(HAnimSite369)
HAnimSite370 = x3d.HAnimSite()
HAnimSite370.USE = "hanim_r_hand_front_view"

HAnimHumanoid43.sites.append(HAnimSite370)
HAnimJoint371 = x3d.HAnimJoint()
HAnimJoint371.USE = "hanim_humanoid_root"

HAnimHumanoid43.joints.append(HAnimJoint371)
HAnimJoint372 = x3d.HAnimJoint()
HAnimJoint372.USE = "hanim_sacroiliac"

HAnimHumanoid43.joints.append(HAnimJoint372)
HAnimJoint373 = x3d.HAnimJoint()
HAnimJoint373.USE = "hanim_vl5"

HAnimHumanoid43.joints.append(HAnimJoint373)
HAnimJoint374 = x3d.HAnimJoint()
HAnimJoint374.USE = "hanim_vl4"

HAnimHumanoid43.joints.append(HAnimJoint374)
HAnimJoint375 = x3d.HAnimJoint()
HAnimJoint375.USE = "hanim_vl3"

HAnimHumanoid43.joints.append(HAnimJoint375)
HAnimJoint376 = x3d.HAnimJoint()
HAnimJoint376.USE = "hanim_vl2"

HAnimHumanoid43.joints.append(HAnimJoint376)
HAnimJoint377 = x3d.HAnimJoint()
HAnimJoint377.USE = "hanim_vl1"

HAnimHumanoid43.joints.append(HAnimJoint377)
HAnimJoint378 = x3d.HAnimJoint()
HAnimJoint378.USE = "hanim_vt12"

HAnimHumanoid43.joints.append(HAnimJoint378)
HAnimJoint379 = x3d.HAnimJoint()
HAnimJoint379.USE = "hanim_vt11"

HAnimHumanoid43.joints.append(HAnimJoint379)
HAnimJoint380 = x3d.HAnimJoint()
HAnimJoint380.USE = "hanim_vt10"

HAnimHumanoid43.joints.append(HAnimJoint380)
HAnimJoint381 = x3d.HAnimJoint()
HAnimJoint381.USE = "hanim_vt9"

HAnimHumanoid43.joints.append(HAnimJoint381)
HAnimJoint382 = x3d.HAnimJoint()
HAnimJoint382.USE = "hanim_vt8"

HAnimHumanoid43.joints.append(HAnimJoint382)
HAnimJoint383 = x3d.HAnimJoint()
HAnimJoint383.USE = "hanim_vt7"

HAnimHumanoid43.joints.append(HAnimJoint383)
HAnimJoint384 = x3d.HAnimJoint()
HAnimJoint384.USE = "hanim_vt6"

HAnimHumanoid43.joints.append(HAnimJoint384)
HAnimJoint385 = x3d.HAnimJoint()
HAnimJoint385.USE = "hanim_vt5"

HAnimHumanoid43.joints.append(HAnimJoint385)
HAnimJoint386 = x3d.HAnimJoint()
HAnimJoint386.USE = "hanim_vt4"

HAnimHumanoid43.joints.append(HAnimJoint386)
HAnimJoint387 = x3d.HAnimJoint()
HAnimJoint387.USE = "hanim_vt3"

HAnimHumanoid43.joints.append(HAnimJoint387)
HAnimJoint388 = x3d.HAnimJoint()
HAnimJoint388.USE = "hanim_vt2"

HAnimHumanoid43.joints.append(HAnimJoint388)
HAnimJoint389 = x3d.HAnimJoint()
HAnimJoint389.USE = "hanim_vt1"

HAnimHumanoid43.joints.append(HAnimJoint389)
HAnimJoint390 = x3d.HAnimJoint()
HAnimJoint390.USE = "hanim_vc7"

HAnimHumanoid43.joints.append(HAnimJoint390)
HAnimJoint391 = x3d.HAnimJoint()
HAnimJoint391.USE = "hanim_vc6"

HAnimHumanoid43.joints.append(HAnimJoint391)
HAnimJoint392 = x3d.HAnimJoint()
HAnimJoint392.USE = "hanim_vc5"

HAnimHumanoid43.joints.append(HAnimJoint392)
HAnimJoint393 = x3d.HAnimJoint()
HAnimJoint393.USE = "hanim_vc4"

HAnimHumanoid43.joints.append(HAnimJoint393)
HAnimJoint394 = x3d.HAnimJoint()
HAnimJoint394.USE = "hanim_vc3"

HAnimHumanoid43.joints.append(HAnimJoint394)
HAnimJoint395 = x3d.HAnimJoint()
HAnimJoint395.USE = "hanim_vc2"

HAnimHumanoid43.joints.append(HAnimJoint395)
HAnimJoint396 = x3d.HAnimJoint()
HAnimJoint396.USE = "hanim_vc1"

HAnimHumanoid43.joints.append(HAnimJoint396)
HAnimJoint397 = x3d.HAnimJoint()
HAnimJoint397.USE = "hanim_skullbase"

HAnimHumanoid43.joints.append(HAnimJoint397)
HAnimJoint398 = x3d.HAnimJoint()
HAnimJoint398.USE = "hanim_temporomandibular"

HAnimHumanoid43.joints.append(HAnimJoint398)
HAnimJoint399 = x3d.HAnimJoint()
HAnimJoint399.USE = "hanim_l_acromioclavicular"

HAnimHumanoid43.joints.append(HAnimJoint399)
HAnimJoint400 = x3d.HAnimJoint()
HAnimJoint400.USE = "hanim_r_acromioclavicular"

HAnimHumanoid43.joints.append(HAnimJoint400)
HAnimJoint401 = x3d.HAnimJoint()
HAnimJoint401.USE = "hanim_l_carpal_distal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint401)
HAnimJoint402 = x3d.HAnimJoint()
HAnimJoint402.USE = "hanim_r_carpal_distal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint402)
HAnimJoint403 = x3d.HAnimJoint()
HAnimJoint403.USE = "hanim_l_carpal_distal_interphalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint403)
HAnimJoint404 = x3d.HAnimJoint()
HAnimJoint404.USE = "hanim_r_carpal_distal_interphalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint404)
HAnimJoint405 = x3d.HAnimJoint()
HAnimJoint405.USE = "hanim_l_carpal_distal_interphalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint405)
HAnimJoint406 = x3d.HAnimJoint()
HAnimJoint406.USE = "hanim_r_carpal_distal_interphalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint406)
HAnimJoint407 = x3d.HAnimJoint()
HAnimJoint407.USE = "hanim_l_carpal_distal_interphalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint407)
HAnimJoint408 = x3d.HAnimJoint()
HAnimJoint408.USE = "hanim_r_carpal_distal_interphalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint408)
HAnimJoint409 = x3d.HAnimJoint()
HAnimJoint409.USE = "hanim_l_carpal_interphalangeal_1"

HAnimHumanoid43.joints.append(HAnimJoint409)
HAnimJoint410 = x3d.HAnimJoint()
HAnimJoint410.USE = "hanim_r_carpal_interphalangeal_1"

HAnimHumanoid43.joints.append(HAnimJoint410)
HAnimJoint411 = x3d.HAnimJoint()
HAnimJoint411.USE = "hanim_l_carpal_proximal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint411)
HAnimJoint412 = x3d.HAnimJoint()
HAnimJoint412.USE = "hanim_r_carpal_proximal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint412)
HAnimJoint413 = x3d.HAnimJoint()
HAnimJoint413.USE = "hanim_l_carpal_proximal_interphalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint413)
HAnimJoint414 = x3d.HAnimJoint()
HAnimJoint414.USE = "hanim_r_carpal_proximal_interphalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint414)
HAnimJoint415 = x3d.HAnimJoint()
HAnimJoint415.USE = "hanim_l_carpal_proximal_interphalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint415)
HAnimJoint416 = x3d.HAnimJoint()
HAnimJoint416.USE = "hanim_r_carpal_proximal_interphalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint416)
HAnimJoint417 = x3d.HAnimJoint()
HAnimJoint417.USE = "hanim_l_carpal_proximal_interphalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint417)
HAnimJoint418 = x3d.HAnimJoint()
HAnimJoint418.USE = "hanim_r_carpal_proximal_interphalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint418)
HAnimJoint419 = x3d.HAnimJoint()
HAnimJoint419.USE = "hanim_l_carpometacarpal_1"

HAnimHumanoid43.joints.append(HAnimJoint419)
HAnimJoint420 = x3d.HAnimJoint()
HAnimJoint420.USE = "hanim_r_carpometacarpal_1"

HAnimHumanoid43.joints.append(HAnimJoint420)
HAnimJoint421 = x3d.HAnimJoint()
HAnimJoint421.USE = "hanim_l_carpometacarpal_2"

HAnimHumanoid43.joints.append(HAnimJoint421)
HAnimJoint422 = x3d.HAnimJoint()
HAnimJoint422.USE = "hanim_r_carpometacarpal_2"

HAnimHumanoid43.joints.append(HAnimJoint422)
HAnimJoint423 = x3d.HAnimJoint()
HAnimJoint423.USE = "hanim_l_carpometacarpal_3"

HAnimHumanoid43.joints.append(HAnimJoint423)
HAnimJoint424 = x3d.HAnimJoint()
HAnimJoint424.USE = "hanim_r_carpometacarpal_3"

HAnimHumanoid43.joints.append(HAnimJoint424)
HAnimJoint425 = x3d.HAnimJoint()
HAnimJoint425.USE = "hanim_l_carpometacarpal_4"

HAnimHumanoid43.joints.append(HAnimJoint425)
HAnimJoint426 = x3d.HAnimJoint()
HAnimJoint426.USE = "hanim_r_carpometacarpal_4"

HAnimHumanoid43.joints.append(HAnimJoint426)
HAnimJoint427 = x3d.HAnimJoint()
HAnimJoint427.USE = "hanim_l_carpometacarpal_5"

HAnimHumanoid43.joints.append(HAnimJoint427)
HAnimJoint428 = x3d.HAnimJoint()
HAnimJoint428.USE = "hanim_r_carpometacarpal_5"

HAnimHumanoid43.joints.append(HAnimJoint428)
HAnimJoint429 = x3d.HAnimJoint()
HAnimJoint429.USE = "hanim_l_elbow"

HAnimHumanoid43.joints.append(HAnimJoint429)
HAnimJoint430 = x3d.HAnimJoint()
HAnimJoint430.USE = "hanim_r_elbow"

HAnimHumanoid43.joints.append(HAnimJoint430)
HAnimJoint431 = x3d.HAnimJoint()
HAnimJoint431.USE = "hanim_l_eyeball_joint"

HAnimHumanoid43.joints.append(HAnimJoint431)
HAnimJoint432 = x3d.HAnimJoint()
HAnimJoint432.USE = "hanim_r_eyeball_joint"

HAnimHumanoid43.joints.append(HAnimJoint432)
HAnimJoint433 = x3d.HAnimJoint()
HAnimJoint433.USE = "hanim_l_eyebrow_joint"

HAnimHumanoid43.joints.append(HAnimJoint433)
HAnimJoint434 = x3d.HAnimJoint()
HAnimJoint434.USE = "hanim_r_eyebrow_joint"

HAnimHumanoid43.joints.append(HAnimJoint434)
HAnimJoint435 = x3d.HAnimJoint()
HAnimJoint435.USE = "hanim_l_eyelid_joint"

HAnimHumanoid43.joints.append(HAnimJoint435)
HAnimJoint436 = x3d.HAnimJoint()
HAnimJoint436.USE = "hanim_r_eyelid_joint"

HAnimHumanoid43.joints.append(HAnimJoint436)
HAnimJoint437 = x3d.HAnimJoint()
HAnimJoint437.USE = "hanim_l_hip"

HAnimHumanoid43.joints.append(HAnimJoint437)
HAnimJoint438 = x3d.HAnimJoint()
HAnimJoint438.USE = "hanim_r_hip"

HAnimHumanoid43.joints.append(HAnimJoint438)
HAnimJoint439 = x3d.HAnimJoint()
HAnimJoint439.USE = "hanim_l_knee"

HAnimHumanoid43.joints.append(HAnimJoint439)
HAnimJoint440 = x3d.HAnimJoint()
HAnimJoint440.USE = "hanim_r_knee"

HAnimHumanoid43.joints.append(HAnimJoint440)
HAnimJoint441 = x3d.HAnimJoint()
HAnimJoint441.USE = "hanim_l_metacarpophalangeal_1"

HAnimHumanoid43.joints.append(HAnimJoint441)
HAnimJoint442 = x3d.HAnimJoint()
HAnimJoint442.USE = "hanim_r_metacarpophalangeal_1"

HAnimHumanoid43.joints.append(HAnimJoint442)
HAnimJoint443 = x3d.HAnimJoint()
HAnimJoint443.USE = "hanim_l_metacarpophalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint443)
HAnimJoint444 = x3d.HAnimJoint()
HAnimJoint444.USE = "hanim_r_metacarpophalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint444)
HAnimJoint445 = x3d.HAnimJoint()
HAnimJoint445.USE = "hanim_l_metacarpophalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint445)
HAnimJoint446 = x3d.HAnimJoint()
HAnimJoint446.USE = "hanim_r_metacarpophalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint446)
HAnimJoint447 = x3d.HAnimJoint()
HAnimJoint447.USE = "hanim_l_metacarpophalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint447)
HAnimJoint448 = x3d.HAnimJoint()
HAnimJoint448.USE = "hanim_r_metacarpophalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint448)
HAnimJoint449 = x3d.HAnimJoint()
HAnimJoint449.USE = "hanim_l_metacarpophalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint449)
HAnimJoint450 = x3d.HAnimJoint()
HAnimJoint450.USE = "hanim_r_metacarpophalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint450)
HAnimJoint451 = x3d.HAnimJoint()
HAnimJoint451.USE = "hanim_l_metatarsophalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint451)
HAnimJoint452 = x3d.HAnimJoint()
HAnimJoint452.USE = "hanim_r_metatarsophalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint452)
HAnimJoint453 = x3d.HAnimJoint()
HAnimJoint453.USE = "hanim_l_radiocarpal"

HAnimHumanoid43.joints.append(HAnimJoint453)
HAnimJoint454 = x3d.HAnimJoint()
HAnimJoint454.USE = "hanim_r_radiocarpal"

HAnimHumanoid43.joints.append(HAnimJoint454)
HAnimJoint455 = x3d.HAnimJoint()
HAnimJoint455.USE = "hanim_l_shoulder"

HAnimHumanoid43.joints.append(HAnimJoint455)
HAnimJoint456 = x3d.HAnimJoint()
HAnimJoint456.USE = "hanim_r_shoulder"

HAnimHumanoid43.joints.append(HAnimJoint456)
HAnimJoint457 = x3d.HAnimJoint()
HAnimJoint457.USE = "hanim_l_sternoclavicular"

HAnimHumanoid43.joints.append(HAnimJoint457)
HAnimJoint458 = x3d.HAnimJoint()
HAnimJoint458.USE = "hanim_r_sternoclavicular"

HAnimHumanoid43.joints.append(HAnimJoint458)
HAnimJoint459 = x3d.HAnimJoint()
HAnimJoint459.USE = "hanim_l_talocrural"

HAnimHumanoid43.joints.append(HAnimJoint459)
HAnimJoint460 = x3d.HAnimJoint()
HAnimJoint460.USE = "hanim_r_talocrural"

HAnimHumanoid43.joints.append(HAnimJoint460)
HAnimJoint461 = x3d.HAnimJoint()
HAnimJoint461.USE = "hanim_l_tarsal_distal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint461)
HAnimJoint462 = x3d.HAnimJoint()
HAnimJoint462.USE = "hanim_r_tarsal_distal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint462)
HAnimJoint463 = x3d.HAnimJoint()
HAnimJoint463.USE = "hanim_l_tarsometatarsal_2"

HAnimHumanoid43.joints.append(HAnimJoint463)
HAnimJoint464 = x3d.HAnimJoint()
HAnimJoint464.USE = "hanim_r_tarsometatarsal_2"

HAnimHumanoid43.joints.append(HAnimJoint464)
HAnimSegment465 = x3d.HAnimSegment()
HAnimSegment465.USE = "hanim_pelvis"

HAnimHumanoid43.segments.append(HAnimSegment465)
HAnimSegment466 = x3d.HAnimSegment()
HAnimSegment466.USE = "hanim_skull"

HAnimHumanoid43.segments.append(HAnimSegment466)
HAnimSegment467 = x3d.HAnimSegment()
HAnimSegment467.USE = "hanim_jaw"

HAnimHumanoid43.segments.append(HAnimSegment467)
HAnimSegment468 = x3d.HAnimSegment()
HAnimSegment468.USE = "hanim_c1"

HAnimHumanoid43.segments.append(HAnimSegment468)
HAnimSegment469 = x3d.HAnimSegment()
HAnimSegment469.USE = "hanim_c2"

HAnimHumanoid43.segments.append(HAnimSegment469)
HAnimSegment470 = x3d.HAnimSegment()
HAnimSegment470.USE = "hanim_c3"

HAnimHumanoid43.segments.append(HAnimSegment470)
HAnimSegment471 = x3d.HAnimSegment()
HAnimSegment471.USE = "hanim_c4"

HAnimHumanoid43.segments.append(HAnimSegment471)
HAnimSegment472 = x3d.HAnimSegment()
HAnimSegment472.USE = "hanim_c5"

HAnimHumanoid43.segments.append(HAnimSegment472)
HAnimSegment473 = x3d.HAnimSegment()
HAnimSegment473.USE = "hanim_c6"

HAnimHumanoid43.segments.append(HAnimSegment473)
HAnimSegment474 = x3d.HAnimSegment()
HAnimSegment474.USE = "hanim_c7"

HAnimHumanoid43.segments.append(HAnimSegment474)
HAnimSegment475 = x3d.HAnimSegment()
HAnimSegment475.USE = "hanim_t1"

HAnimHumanoid43.segments.append(HAnimSegment475)
HAnimSegment476 = x3d.HAnimSegment()
HAnimSegment476.USE = "hanim_t2"

HAnimHumanoid43.segments.append(HAnimSegment476)
HAnimSegment477 = x3d.HAnimSegment()
HAnimSegment477.USE = "hanim_t3"

HAnimHumanoid43.segments.append(HAnimSegment477)
HAnimSegment478 = x3d.HAnimSegment()
HAnimSegment478.USE = "hanim_t4"

HAnimHumanoid43.segments.append(HAnimSegment478)
HAnimSegment479 = x3d.HAnimSegment()
HAnimSegment479.USE = "hanim_t5"

HAnimHumanoid43.segments.append(HAnimSegment479)
HAnimSegment480 = x3d.HAnimSegment()
HAnimSegment480.USE = "hanim_t6"

HAnimHumanoid43.segments.append(HAnimSegment480)
HAnimSegment481 = x3d.HAnimSegment()
HAnimSegment481.USE = "hanim_t7"

HAnimHumanoid43.segments.append(HAnimSegment481)
HAnimSegment482 = x3d.HAnimSegment()
HAnimSegment482.USE = "hanim_t8"

HAnimHumanoid43.segments.append(HAnimSegment482)
HAnimSegment483 = x3d.HAnimSegment()
HAnimSegment483.USE = "hanim_t9"

HAnimHumanoid43.segments.append(HAnimSegment483)
HAnimSegment484 = x3d.HAnimSegment()
HAnimSegment484.USE = "hanim_t10"

HAnimHumanoid43.segments.append(HAnimSegment484)
HAnimSegment485 = x3d.HAnimSegment()
HAnimSegment485.USE = "hanim_t11"

HAnimHumanoid43.segments.append(HAnimSegment485)
HAnimSegment486 = x3d.HAnimSegment()
HAnimSegment486.USE = "hanim_t12"

HAnimHumanoid43.segments.append(HAnimSegment486)
HAnimSegment487 = x3d.HAnimSegment()
HAnimSegment487.USE = "hanim_l1"

HAnimHumanoid43.segments.append(HAnimSegment487)
HAnimSegment488 = x3d.HAnimSegment()
HAnimSegment488.USE = "hanim_l2"

HAnimHumanoid43.segments.append(HAnimSegment488)
HAnimSegment489 = x3d.HAnimSegment()
HAnimSegment489.USE = "hanim_l3"

HAnimHumanoid43.segments.append(HAnimSegment489)
HAnimSegment490 = x3d.HAnimSegment()
HAnimSegment490.USE = "hanim_l4"

HAnimHumanoid43.segments.append(HAnimSegment490)
HAnimSegment491 = x3d.HAnimSegment()
HAnimSegment491.USE = "hanim_l5"

HAnimHumanoid43.segments.append(HAnimSegment491)
HAnimSegment492 = x3d.HAnimSegment()
HAnimSegment492.USE = "hanim_sacrum"

HAnimHumanoid43.segments.append(HAnimSegment492)
HAnimSegment493 = x3d.HAnimSegment()
HAnimSegment493.USE = "hanim_l_calf"

HAnimHumanoid43.segments.append(HAnimSegment493)
HAnimSegment494 = x3d.HAnimSegment()
HAnimSegment494.USE = "hanim_r_calf"

HAnimHumanoid43.segments.append(HAnimSegment494)
HAnimSegment495 = x3d.HAnimSegment()
HAnimSegment495.USE = "hanim_l_carpal"

HAnimHumanoid43.segments.append(HAnimSegment495)
HAnimSegment496 = x3d.HAnimSegment()
HAnimSegment496.USE = "hanim_r_carpal"

HAnimHumanoid43.segments.append(HAnimSegment496)
HAnimSegment497 = x3d.HAnimSegment()
HAnimSegment497.USE = "hanim_l_carpal_distal_phalanx_1"

HAnimHumanoid43.segments.append(HAnimSegment497)
HAnimSegment498 = x3d.HAnimSegment()
HAnimSegment498.USE = "hanim_r_carpal_distal_phalanx_1"

HAnimHumanoid43.segments.append(HAnimSegment498)
HAnimSegment499 = x3d.HAnimSegment()
HAnimSegment499.USE = "hanim_l_carpal_distal_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment499)
HAnimSegment500 = x3d.HAnimSegment()
HAnimSegment500.USE = "hanim_r_carpal_distal_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment500)
HAnimSegment501 = x3d.HAnimSegment()
HAnimSegment501.USE = "hanim_l_carpal_distal_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment501)
HAnimSegment502 = x3d.HAnimSegment()
HAnimSegment502.USE = "hanim_r_carpal_distal_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment502)
HAnimSegment503 = x3d.HAnimSegment()
HAnimSegment503.USE = "hanim_l_carpal_distal_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment503)
HAnimSegment504 = x3d.HAnimSegment()
HAnimSegment504.USE = "hanim_r_carpal_distal_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment504)
HAnimSegment505 = x3d.HAnimSegment()
HAnimSegment505.USE = "hanim_l_carpal_distal_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment505)
HAnimSegment506 = x3d.HAnimSegment()
HAnimSegment506.USE = "hanim_r_carpal_distal_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment506)
HAnimSegment507 = x3d.HAnimSegment()
HAnimSegment507.USE = "hanim_l_carpal_middle_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment507)
HAnimSegment508 = x3d.HAnimSegment()
HAnimSegment508.USE = "hanim_r_carpal_middle_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment508)
HAnimSegment509 = x3d.HAnimSegment()
HAnimSegment509.USE = "hanim_l_carpal_middle_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment509)
HAnimSegment510 = x3d.HAnimSegment()
HAnimSegment510.USE = "hanim_r_carpal_middle_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment510)
HAnimSegment511 = x3d.HAnimSegment()
HAnimSegment511.USE = "hanim_l_carpal_middle_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment511)
HAnimSegment512 = x3d.HAnimSegment()
HAnimSegment512.USE = "hanim_r_carpal_middle_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment512)
HAnimSegment513 = x3d.HAnimSegment()
HAnimSegment513.USE = "hanim_l_carpal_middle_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment513)
HAnimSegment514 = x3d.HAnimSegment()
HAnimSegment514.USE = "hanim_r_carpal_middle_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment514)
HAnimSegment515 = x3d.HAnimSegment()
HAnimSegment515.USE = "hanim_l_carpal_proximal_phalanx_1"

HAnimHumanoid43.segments.append(HAnimSegment515)
HAnimSegment516 = x3d.HAnimSegment()
HAnimSegment516.USE = "hanim_r_carpal_proximal_phalanx_1"

HAnimHumanoid43.segments.append(HAnimSegment516)
HAnimSegment517 = x3d.HAnimSegment()
HAnimSegment517.USE = "hanim_l_carpal_proximal_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment517)
HAnimSegment518 = x3d.HAnimSegment()
HAnimSegment518.USE = "hanim_r_carpal_proximal_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment518)
HAnimSegment519 = x3d.HAnimSegment()
HAnimSegment519.USE = "hanim_l_carpal_proximal_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment519)
HAnimSegment520 = x3d.HAnimSegment()
HAnimSegment520.USE = "hanim_r_carpal_proximal_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment520)
HAnimSegment521 = x3d.HAnimSegment()
HAnimSegment521.USE = "hanim_l_carpal_proximal_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment521)
HAnimSegment522 = x3d.HAnimSegment()
HAnimSegment522.USE = "hanim_r_carpal_proximal_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment522)
HAnimSegment523 = x3d.HAnimSegment()
HAnimSegment523.USE = "hanim_l_carpal_proximal_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment523)
HAnimSegment524 = x3d.HAnimSegment()
HAnimSegment524.USE = "hanim_r_carpal_proximal_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment524)
HAnimSegment525 = x3d.HAnimSegment()
HAnimSegment525.USE = "hanim_l_clavicle"

HAnimHumanoid43.segments.append(HAnimSegment525)
HAnimSegment526 = x3d.HAnimSegment()
HAnimSegment526.USE = "hanim_r_clavicle"

HAnimHumanoid43.segments.append(HAnimSegment526)
HAnimSegment527 = x3d.HAnimSegment()
HAnimSegment527.USE = "hanim_l_eyeball"

HAnimHumanoid43.segments.append(HAnimSegment527)
HAnimSegment528 = x3d.HAnimSegment()
HAnimSegment528.USE = "hanim_r_eyeball"

HAnimHumanoid43.segments.append(HAnimSegment528)
HAnimSegment529 = x3d.HAnimSegment()
HAnimSegment529.USE = "hanim_l_eyebrow"

HAnimHumanoid43.segments.append(HAnimSegment529)
HAnimSegment530 = x3d.HAnimSegment()
HAnimSegment530.USE = "hanim_r_eyebrow"

HAnimHumanoid43.segments.append(HAnimSegment530)
HAnimSegment531 = x3d.HAnimSegment()
HAnimSegment531.USE = "hanim_l_eyelid"

HAnimHumanoid43.segments.append(HAnimSegment531)
HAnimSegment532 = x3d.HAnimSegment()
HAnimSegment532.USE = "hanim_r_eyelid"

HAnimHumanoid43.segments.append(HAnimSegment532)
HAnimSegment533 = x3d.HAnimSegment()
HAnimSegment533.USE = "hanim_l_forearm"

HAnimHumanoid43.segments.append(HAnimSegment533)
HAnimSegment534 = x3d.HAnimSegment()
HAnimSegment534.USE = "hanim_r_forearm"

HAnimHumanoid43.segments.append(HAnimSegment534)
HAnimSegment535 = x3d.HAnimSegment()
HAnimSegment535.USE = "hanim_l_metacarpal_1"

HAnimHumanoid43.segments.append(HAnimSegment535)
HAnimSegment536 = x3d.HAnimSegment()
HAnimSegment536.USE = "hanim_r_metacarpal_1"

HAnimHumanoid43.segments.append(HAnimSegment536)
HAnimSegment537 = x3d.HAnimSegment()
HAnimSegment537.USE = "hanim_l_metacarpal_2"

HAnimHumanoid43.segments.append(HAnimSegment537)
HAnimSegment538 = x3d.HAnimSegment()
HAnimSegment538.USE = "hanim_r_metacarpal_2"

HAnimHumanoid43.segments.append(HAnimSegment538)
HAnimSegment539 = x3d.HAnimSegment()
HAnimSegment539.USE = "hanim_l_metacarpal_3"

HAnimHumanoid43.segments.append(HAnimSegment539)
HAnimSegment540 = x3d.HAnimSegment()
HAnimSegment540.USE = "hanim_r_metacarpal_3"

HAnimHumanoid43.segments.append(HAnimSegment540)
HAnimSegment541 = x3d.HAnimSegment()
HAnimSegment541.USE = "hanim_l_metacarpal_4"

HAnimHumanoid43.segments.append(HAnimSegment541)
HAnimSegment542 = x3d.HAnimSegment()
HAnimSegment542.USE = "hanim_r_metacarpal_4"

HAnimHumanoid43.segments.append(HAnimSegment542)
HAnimSegment543 = x3d.HAnimSegment()
HAnimSegment543.USE = "hanim_l_metacarpal_5"

HAnimHumanoid43.segments.append(HAnimSegment543)
HAnimSegment544 = x3d.HAnimSegment()
HAnimSegment544.USE = "hanim_r_metacarpal_5"

HAnimHumanoid43.segments.append(HAnimSegment544)
HAnimSegment545 = x3d.HAnimSegment()
HAnimSegment545.USE = "hanim_l_metatarsal_2"

HAnimHumanoid43.segments.append(HAnimSegment545)
HAnimSegment546 = x3d.HAnimSegment()
HAnimSegment546.USE = "hanim_r_metatarsal_2"

HAnimHumanoid43.segments.append(HAnimSegment546)
HAnimSegment547 = x3d.HAnimSegment()
HAnimSegment547.USE = "hanim_l_scapula"

HAnimHumanoid43.segments.append(HAnimSegment547)
HAnimSegment548 = x3d.HAnimSegment()
HAnimSegment548.USE = "hanim_r_scapula"

HAnimHumanoid43.segments.append(HAnimSegment548)
HAnimSegment549 = x3d.HAnimSegment()
HAnimSegment549.USE = "hanim_l_talus"

HAnimHumanoid43.segments.append(HAnimSegment549)
HAnimSegment550 = x3d.HAnimSegment()
HAnimSegment550.USE = "hanim_r_talus"

HAnimHumanoid43.segments.append(HAnimSegment550)
HAnimSegment551 = x3d.HAnimSegment()
HAnimSegment551.USE = "hanim_l_tarsal_distal_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment551)
HAnimSegment552 = x3d.HAnimSegment()
HAnimSegment552.USE = "hanim_r_tarsal_distal_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment552)
HAnimSegment553 = x3d.HAnimSegment()
HAnimSegment553.USE = "hanim_l_tarsal_proximal_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment553)
HAnimSegment554 = x3d.HAnimSegment()
HAnimSegment554.USE = "hanim_r_tarsal_proximal_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment554)
HAnimSegment555 = x3d.HAnimSegment()
HAnimSegment555.USE = "hanim_l_thigh"

HAnimHumanoid43.segments.append(HAnimSegment555)
HAnimSegment556 = x3d.HAnimSegment()
HAnimSegment556.USE = "hanim_r_thigh"

HAnimHumanoid43.segments.append(HAnimSegment556)
HAnimSegment557 = x3d.HAnimSegment()
HAnimSegment557.USE = "hanim_l_upperarm"

HAnimHumanoid43.segments.append(HAnimSegment557)
HAnimSegment558 = x3d.HAnimSegment()
HAnimSegment558.USE = "hanim_r_upperarm"

HAnimHumanoid43.segments.append(HAnimSegment558)
HAnimSite559 = x3d.HAnimSite()
HAnimSite559.USE = "hanim_crotch_pt"

HAnimHumanoid43.sites.append(HAnimSite559)
HAnimSite560 = x3d.HAnimSite()
HAnimSite560.USE = "hanim_skull_vertex_tip"

HAnimHumanoid43.sites.append(HAnimSite560)
HAnimSite561 = x3d.HAnimSite()
HAnimSite561.USE = "hanim_sellion_pt"

HAnimHumanoid43.sites.append(HAnimSite561)
HAnimSite562 = x3d.HAnimSite()
HAnimSite562.USE = "hanim_supramenton_pt"

HAnimHumanoid43.sites.append(HAnimSite562)
HAnimSite563 = x3d.HAnimSite()
HAnimSite563.USE = "hanim_nuchale_pt"

HAnimHumanoid43.sites.append(HAnimSite563)
HAnimSite564 = x3d.HAnimSite()
HAnimSite564.USE = "hanim_suprasternale_pt"

HAnimHumanoid43.sites.append(HAnimSite564)
HAnimSite565 = x3d.HAnimSite()
HAnimSite565.USE = "hanim_cervicale_pt"

HAnimHumanoid43.sites.append(HAnimSite565)
HAnimSite566 = x3d.HAnimSite()
HAnimSite566.USE = "hanim_substernale_pt"

HAnimHumanoid43.sites.append(HAnimSite566)
HAnimSite567 = x3d.HAnimSite()
HAnimSite567.USE = "hanim_rib10_midspine_pt"

HAnimHumanoid43.sites.append(HAnimSite567)
HAnimSite568 = x3d.HAnimSite()
HAnimSite568.USE = "hanim_waist_preferred_posterior_pt"

HAnimHumanoid43.sites.append(HAnimSite568)
HAnimSite569 = x3d.HAnimSite()
HAnimSite569.USE = "hanim_navel_pt"

HAnimHumanoid43.sites.append(HAnimSite569)
HAnimSite570 = x3d.HAnimSite()
HAnimSite570.USE = "hanim_l_acromion_pt"

HAnimHumanoid43.sites.append(HAnimSite570)
HAnimSite571 = x3d.HAnimSite()
HAnimSite571.USE = "hanim_r_acromion_pt"

HAnimHumanoid43.sites.append(HAnimSite571)
HAnimSite572 = x3d.HAnimSite()
HAnimSite572.USE = "hanim_r_asis_pt"

HAnimHumanoid43.sites.append(HAnimSite572)
HAnimSite573 = x3d.HAnimSite()
HAnimSite573.USE = "hanim_l_asis_pt"

HAnimHumanoid43.sites.append(HAnimSite573)
HAnimSite574 = x3d.HAnimSite()
HAnimSite574.USE = "hanim_l_axilla_distal_pt"

HAnimHumanoid43.sites.append(HAnimSite574)
HAnimSite575 = x3d.HAnimSite()
HAnimSite575.USE = "hanim_r_axilla_distal_pt"

HAnimHumanoid43.sites.append(HAnimSite575)
HAnimSite576 = x3d.HAnimSite()
HAnimSite576.USE = "hanim_l_axilla_proximal_pt"

HAnimHumanoid43.sites.append(HAnimSite576)
HAnimSite577 = x3d.HAnimSite()
HAnimSite577.USE = "hanim_r_axilla_proximal_pt"

HAnimHumanoid43.sites.append(HAnimSite577)
HAnimSite578 = x3d.HAnimSite()
HAnimSite578.USE = "hanim_l_calcaneus_posterior_pt"

HAnimHumanoid43.sites.append(HAnimSite578)
HAnimSite579 = x3d.HAnimSite()
HAnimSite579.USE = "hanim_r_calcaneus_posterior_pt"

HAnimHumanoid43.sites.append(HAnimSite579)
HAnimSite580 = x3d.HAnimSite()
HAnimSite580.USE = "hanim_l_carpal_distal_phalanx_1_tip"

HAnimHumanoid43.sites.append(HAnimSite580)
HAnimSite581 = x3d.HAnimSite()
HAnimSite581.USE = "hanim_r_carpal_distal_phalanx_1_tip"

HAnimHumanoid43.sites.append(HAnimSite581)
HAnimSite582 = x3d.HAnimSite()
HAnimSite582.USE = "hanim_l_carpal_distal_phalanx_2_tip"

HAnimHumanoid43.sites.append(HAnimSite582)
HAnimSite583 = x3d.HAnimSite()
HAnimSite583.USE = "hanim_r_carpal_distal_phalanx_2_tip"

HAnimHumanoid43.sites.append(HAnimSite583)
HAnimSite584 = x3d.HAnimSite()
HAnimSite584.USE = "hanim_l_carpal_distal_phalanx_3_tip"

HAnimHumanoid43.sites.append(HAnimSite584)
HAnimSite585 = x3d.HAnimSite()
HAnimSite585.USE = "hanim_r_carpal_distal_phalanx_3_tip"

HAnimHumanoid43.sites.append(HAnimSite585)
HAnimSite586 = x3d.HAnimSite()
HAnimSite586.USE = "hanim_l_carpal_distal_phalanx_4_tip"

HAnimHumanoid43.sites.append(HAnimSite586)
HAnimSite587 = x3d.HAnimSite()
HAnimSite587.USE = "hanim_r_carpal_distal_phalanx_4_tip"

HAnimHumanoid43.sites.append(HAnimSite587)
HAnimSite588 = x3d.HAnimSite()
HAnimSite588.USE = "hanim_l_carpal_distal_phalanx_5_tip"

HAnimHumanoid43.sites.append(HAnimSite588)
HAnimSite589 = x3d.HAnimSite()
HAnimSite589.USE = "hanim_r_carpal_distal_phalanx_5_tip"

HAnimHumanoid43.sites.append(HAnimSite589)
HAnimSite590 = x3d.HAnimSite()
HAnimSite590.USE = "hanim_l_clavicle_pt"

HAnimHumanoid43.sites.append(HAnimSite590)
HAnimSite591 = x3d.HAnimSite()
HAnimSite591.USE = "hanim_r_clavicle_pt"

HAnimHumanoid43.sites.append(HAnimSite591)
HAnimSite592 = x3d.HAnimSite()
HAnimSite592.USE = "hanim_l_dactylion_pt"

HAnimHumanoid43.sites.append(HAnimSite592)
HAnimSite593 = x3d.HAnimSite()
HAnimSite593.USE = "hanim_r_dactylion_pt"

HAnimHumanoid43.sites.append(HAnimSite593)
HAnimSite594 = x3d.HAnimSite()
HAnimSite594.USE = "hanim_l_femoral_lateral_epicondyle_pt"

HAnimHumanoid43.sites.append(HAnimSite594)
HAnimSite595 = x3d.HAnimSite()
HAnimSite595.USE = "hanim_r_femoral_lateral_epicondyle_pt"

HAnimHumanoid43.sites.append(HAnimSite595)
HAnimSite596 = x3d.HAnimSite()
HAnimSite596.USE = "hanim_l_femoral_medial_epicondyle_pt"

HAnimHumanoid43.sites.append(HAnimSite596)
HAnimSite597 = x3d.HAnimSite()
HAnimSite597.USE = "hanim_r_femoral_medial_epicondyle_pt"

HAnimHumanoid43.sites.append(HAnimSite597)
HAnimSite598 = x3d.HAnimSite()
HAnimSite598.USE = "hanim_l_forefoot_tip"

HAnimHumanoid43.sites.append(HAnimSite598)
HAnimSite599 = x3d.HAnimSite()
HAnimSite599.USE = "hanim_r_forefoot_tip"

HAnimHumanoid43.sites.append(HAnimSite599)
HAnimSite600 = x3d.HAnimSite()
HAnimSite600.USE = "hanim_r_gonion_pt"

HAnimHumanoid43.sites.append(HAnimSite600)
HAnimSite601 = x3d.HAnimSite()
HAnimSite601.USE = "hanim_l_gonion_pt"

HAnimHumanoid43.sites.append(HAnimSite601)
HAnimSite602 = x3d.HAnimSite()
HAnimSite602.USE = "hanim_l_humeral_lateral_epicondyle_pt"

HAnimHumanoid43.sites.append(HAnimSite602)
HAnimSite603 = x3d.HAnimSite()
HAnimSite603.USE = "hanim_r_humeral_lateral_epicondyle_pt"

HAnimHumanoid43.sites.append(HAnimSite603)
HAnimSite604 = x3d.HAnimSite()
HAnimSite604.USE = "hanim_l_humeral_medial_epicondyle_pt"

HAnimHumanoid43.sites.append(HAnimSite604)
HAnimSite605 = x3d.HAnimSite()
HAnimSite605.USE = "hanim_r_humeral_medial_epicondyle_pt"

HAnimHumanoid43.sites.append(HAnimSite605)
HAnimSite606 = x3d.HAnimSite()
HAnimSite606.USE = "hanim_r_iliocristale_pt"

HAnimHumanoid43.sites.append(HAnimSite606)
HAnimSite607 = x3d.HAnimSite()
HAnimSite607.USE = "hanim_l_iliocristale_pt"

HAnimHumanoid43.sites.append(HAnimSite607)
HAnimSite608 = x3d.HAnimSite()
HAnimSite608.USE = "hanim_r_infraorbitale_pt"

HAnimHumanoid43.sites.append(HAnimSite608)
HAnimSite609 = x3d.HAnimSite()
HAnimSite609.USE = "hanim_l_infraorbitale_pt"

HAnimHumanoid43.sites.append(HAnimSite609)
HAnimSite610 = x3d.HAnimSite()
HAnimSite610.USE = "hanim_l_knee_crease_pt"

HAnimHumanoid43.sites.append(HAnimSite610)
HAnimSite611 = x3d.HAnimSite()
HAnimSite611.USE = "hanim_r_knee_crease_pt"

HAnimHumanoid43.sites.append(HAnimSite611)
HAnimSite612 = x3d.HAnimSite()
HAnimSite612.USE = "hanim_l_lateral_malleolus_pt"

HAnimHumanoid43.sites.append(HAnimSite612)
HAnimSite613 = x3d.HAnimSite()
HAnimSite613.USE = "hanim_r_lateral_malleolus_pt"

HAnimHumanoid43.sites.append(HAnimSite613)
HAnimSite614 = x3d.HAnimSite()
HAnimSite614.USE = "hanim_l_medial_malleolus_pt"

HAnimHumanoid43.sites.append(HAnimSite614)
HAnimSite615 = x3d.HAnimSite()
HAnimSite615.USE = "hanim_r_medial_malleolus_pt"

HAnimHumanoid43.sites.append(HAnimSite615)
HAnimSite616 = x3d.HAnimSite()
HAnimSite616.USE = "hanim_l_metacarpal_phalanx_2_pt"

HAnimHumanoid43.sites.append(HAnimSite616)
HAnimSite617 = x3d.HAnimSite()
HAnimSite617.USE = "hanim_r_metacarpal_phalanx_2_pt"

HAnimHumanoid43.sites.append(HAnimSite617)
HAnimSite618 = x3d.HAnimSite()
HAnimSite618.USE = "hanim_l_metacarpal_phalanx_5_pt"

HAnimHumanoid43.sites.append(HAnimSite618)
HAnimSite619 = x3d.HAnimSite()
HAnimSite619.USE = "hanim_r_metacarpal_phalanx_5_pt"

HAnimHumanoid43.sites.append(HAnimSite619)
HAnimSite620 = x3d.HAnimSite()
HAnimSite620.USE = "hanim_l_metatarsal_phalanx_1_pt"

HAnimHumanoid43.sites.append(HAnimSite620)
HAnimSite621 = x3d.HAnimSite()
HAnimSite621.USE = "hanim_r_metatarsal_phalanx_1_pt"

HAnimHumanoid43.sites.append(HAnimSite621)
HAnimSite622 = x3d.HAnimSite()
HAnimSite622.USE = "hanim_l_metatarsal_phalanx_5_pt"

HAnimHumanoid43.sites.append(HAnimSite622)
HAnimSite623 = x3d.HAnimSite()
HAnimSite623.USE = "hanim_r_metatarsal_phalanx_5_pt"

HAnimHumanoid43.sites.append(HAnimSite623)
HAnimSite624 = x3d.HAnimSite()
HAnimSite624.USE = "hanim_r_neck_base_pt"

HAnimHumanoid43.sites.append(HAnimSite624)
HAnimSite625 = x3d.HAnimSite()
HAnimSite625.USE = "hanim_l_neck_base_pt"

HAnimHumanoid43.sites.append(HAnimSite625)
HAnimSite626 = x3d.HAnimSite()
HAnimSite626.USE = "hanim_l_olecranon_pt"

HAnimHumanoid43.sites.append(HAnimSite626)
HAnimSite627 = x3d.HAnimSite()
HAnimSite627.USE = "hanim_r_olecranon_pt"

HAnimHumanoid43.sites.append(HAnimSite627)
HAnimSite628 = x3d.HAnimSite()
HAnimSite628.USE = "hanim_r_psis_pt"

HAnimHumanoid43.sites.append(HAnimSite628)
HAnimSite629 = x3d.HAnimSite()
HAnimSite629.USE = "hanim_l_psis_pt"

HAnimHumanoid43.sites.append(HAnimSite629)
HAnimSite630 = x3d.HAnimSite()
HAnimSite630.USE = "hanim_l_radial_styloid_pt"

HAnimHumanoid43.sites.append(HAnimSite630)
HAnimSite631 = x3d.HAnimSite()
HAnimSite631.USE = "hanim_r_radial_styloid_pt"

HAnimHumanoid43.sites.append(HAnimSite631)
HAnimSite632 = x3d.HAnimSite()
HAnimSite632.USE = "hanim_l_radiale_pt"

HAnimHumanoid43.sites.append(HAnimSite632)
HAnimSite633 = x3d.HAnimSite()
HAnimSite633.USE = "hanim_r_radiale_pt"

HAnimHumanoid43.sites.append(HAnimSite633)
HAnimSite634 = x3d.HAnimSite()
HAnimSite634.USE = "hanim_r_rib10_pt"

HAnimHumanoid43.sites.append(HAnimSite634)
HAnimSite635 = x3d.HAnimSite()
HAnimSite635.USE = "hanim_l_rib10_pt"

HAnimHumanoid43.sites.append(HAnimSite635)
HAnimSite636 = x3d.HAnimSite()
HAnimSite636.USE = "hanim_temporomandibular_l_site_pt"

HAnimHumanoid43.sites.append(HAnimSite636)
HAnimSite637 = x3d.HAnimSite()
HAnimSite637.USE = "hanim_temporomandibular_r_site_pt"

HAnimHumanoid43.sites.append(HAnimSite637)
HAnimSite638 = x3d.HAnimSite()
HAnimSite638.USE = "hanim_l_sphyrion_pt"

HAnimHumanoid43.sites.append(HAnimSite638)
HAnimSite639 = x3d.HAnimSite()
HAnimSite639.USE = "hanim_r_sphyrion_pt"

HAnimHumanoid43.sites.append(HAnimSite639)
HAnimSite640 = x3d.HAnimSite()
HAnimSite640.USE = "hanim_l_tarsal_distal_phalanx_2_pt"

HAnimHumanoid43.sites.append(HAnimSite640)
HAnimSite641 = x3d.HAnimSite()
HAnimSite641.USE = "hanim_r_tarsal_distal_phalanx_2_pt"

HAnimHumanoid43.sites.append(HAnimSite641)
HAnimSite642 = x3d.HAnimSite()
HAnimSite642.USE = "hanim_r_thelion_pt"

HAnimHumanoid43.sites.append(HAnimSite642)
HAnimSite643 = x3d.HAnimSite()
HAnimSite643.USE = "hanim_l_thelion_pt"

HAnimHumanoid43.sites.append(HAnimSite643)
HAnimSite644 = x3d.HAnimSite()
HAnimSite644.USE = "hanim_r_tragion_pt"

HAnimHumanoid43.sites.append(HAnimSite644)
HAnimSite645 = x3d.HAnimSite()
HAnimSite645.USE = "hanim_l_tragion_pt"

HAnimHumanoid43.sites.append(HAnimSite645)
HAnimSite646 = x3d.HAnimSite()
HAnimSite646.USE = "hanim_r_trochanterion_pt"

HAnimHumanoid43.sites.append(HAnimSite646)
HAnimSite647 = x3d.HAnimSite()
HAnimSite647.USE = "hanim_l_trochanterion_pt"

HAnimHumanoid43.sites.append(HAnimSite647)
HAnimSite648 = x3d.HAnimSite()
HAnimSite648.USE = "hanim_l_ulnar_styloid_pt"

HAnimHumanoid43.sites.append(HAnimSite648)
HAnimSite649 = x3d.HAnimSite()
HAnimSite649.USE = "hanim_r_ulnar_styloid_pt"

HAnimHumanoid43.sites.append(HAnimSite649)

Scene29.children.append(HAnimHumanoid43)

X3D0.Scene = Scene29
f = open("././HAnim2SpecificationLOA3Invisible_RoundTrip.x3d", "w")
f.write(X3D0.XML())
f.close()
