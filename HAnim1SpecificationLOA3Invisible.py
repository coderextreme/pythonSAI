print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"
head1 = x3d.head()
component2 = x3d.component()
component2.name = "H-Anim"
component2.level = 1

head1.children.append(component2)
meta3 = x3d.meta()
meta3.name = "title"
meta3.content = "HAnim1SpecificationLOA3Invisible.x3d"

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
meta7.content = "19 February 2021"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.name = "creator"
meta8.content = "Matthew T. Beitler, Joe D. Williams, Don Brutzman"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "reference"
meta9.content = "HAnim1SpecificationLOA3Illustrated.x3d"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "reference"
meta10.content = "HAnim1SpecificationLOA3Animation.x3d"

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
meta27.content = "https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Legacy/HAnim1SpecificationLOA3Invisible.x3d"

head1.children.append(meta27)
meta28 = x3d.meta()
meta28.name = "license"
meta28.content = "../license.html"

head1.children.append(meta28)

X3D0.head = head1
Scene29 = x3d.Scene()
Background30 = x3d.Background()

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
HAnimHumanoid43.info = ["authorName=Matthew T. Beitler Joe D. Williams Don Brutzman","authorEmail=HAnim@web3D.org","copyright=none","creationDate=12 May 1999","usageRestrictions=none","humanoidVersion=2.0","height=1.7504"]
HAnimHumanoid43.version = "2.0"
#Only one root HAnimJoint is expected
#USE nodes go here for access by inverse kinematics (IK) engines and other tools
#Top-level HAnimSite/Viewpoint nodes that move with the human center but are unaffected by body animation
#TODO move relevant HAnimSite/Viewpoint pairs into skeleton at appropriate locations, if so also revert containerField to default
#right between the eyes, stationary position not animating except with body itself
HAnimJoint44 = x3d.HAnimJoint()
HAnimJoint44.name = "humanoid_root"
HAnimJoint44.DEF = "hanim_humanoid_root"
HAnimJoint44.center = [0,0.824,0.0277]
HAnimJoint44.ulimit = [0,0,0]
HAnimJoint44.llimit = [0,0,0]
HAnimSegment45 = x3d.HAnimSegment()
HAnimSegment45.name = "sacrum"
HAnimSegment45.DEF = "hanim_sacrum"

HAnimJoint44.children.append(HAnimSegment45)
HAnimJoint46 = x3d.HAnimJoint()
HAnimJoint46.name = "sacroiliac"
HAnimJoint46.DEF = "hanim_sacroiliac"
HAnimJoint46.center = [0,0.9149,0.0016]
HAnimJoint46.ulimit = [0,0,0]
HAnimJoint46.llimit = [0,0,0]
HAnimSegment47 = x3d.HAnimSegment()
HAnimSegment47.name = "pelvis"
HAnimSegment47.DEF = "hanim_pelvis"
HAnimSite48 = x3d.HAnimSite()
HAnimSite48.name = "r_iliocristale_pt"
HAnimSite48.DEF = "hanim_r_iliocristale_pt"
HAnimSite48.translation = [-0.1525,1.0628,0.0035]

HAnimSegment47.children.append(HAnimSite48)
HAnimSite49 = x3d.HAnimSite()
HAnimSite49.name = "r_trochanterion_pt"
HAnimSite49.DEF = "hanim_r_trochanterion_pt"
HAnimSite49.translation = [-0.1689,0.8419,0.0352]

HAnimSegment47.children.append(HAnimSite49)
HAnimSite50 = x3d.HAnimSite()
HAnimSite50.name = "l_iliocristale_pt"
HAnimSite50.DEF = "hanim_l_iliocristale_pt"
HAnimSite50.translation = [0.1612,1.0537,0.0008]

HAnimSegment47.children.append(HAnimSite50)
HAnimSite51 = x3d.HAnimSite()
HAnimSite51.name = "l_trochanterion_pt"
HAnimSite51.DEF = "hanim_l_trochanterion_pt"
HAnimSite51.translation = [0.1677,0.8336,0.0303]

HAnimSegment47.children.append(HAnimSite51)
HAnimSite52 = x3d.HAnimSite()
HAnimSite52.name = "r_asis_pt"
HAnimSite52.DEF = "hanim_r_asis_pt"
HAnimSite52.translation = [-0.0887,1.0021,0.1112]

HAnimSegment47.children.append(HAnimSite52)
HAnimSite53 = x3d.HAnimSite()
HAnimSite53.name = "l_asis_pt"
HAnimSite53.DEF = "hanim_l_asis_pt"
HAnimSite53.translation = [0.0925,0.9983,0.1052]

HAnimSegment47.children.append(HAnimSite53)
HAnimSite54 = x3d.HAnimSite()
HAnimSite54.name = "r_psis_pt"
HAnimSite54.DEF = "hanim_r_psis_pt"
HAnimSite54.translation = [-0.0716,1.019,-0.1138]

HAnimSegment47.children.append(HAnimSite54)
HAnimSite55 = x3d.HAnimSite()
HAnimSite55.name = "l_psis_pt"
HAnimSite55.DEF = "hanim_l_psis_pt"
HAnimSite55.translation = [0.0774,1.019,-0.1151]

HAnimSegment47.children.append(HAnimSite55)
HAnimSite56 = x3d.HAnimSite()
HAnimSite56.name = "crotch_pt"
HAnimSite56.DEF = "hanim_crotch_pt"
HAnimSite56.translation = [0.0034,0.8266,0.0257]

HAnimSegment47.children.append(HAnimSite56)

HAnimJoint46.children.append(HAnimSegment47)
HAnimJoint57 = x3d.HAnimJoint()
HAnimJoint57.name = "l_hip"
HAnimJoint57.DEF = "hanim_l_hip"
HAnimJoint57.center = [0.0961,0.9124,-0.0001]
HAnimJoint57.ulimit = [0,0,0]
HAnimJoint57.llimit = [0,0,0]
HAnimSegment58 = x3d.HAnimSegment()
HAnimSegment58.name = "l_thigh"
HAnimSegment58.DEF = "hanim_l_thigh"
HAnimSite59 = x3d.HAnimSite()
HAnimSite59.name = "l_knee_crease_pt"
HAnimSite59.DEF = "hanim_l_knee_crease_pt"
HAnimSite59.translation = [0.0993,0.4881,-0.0309]

HAnimSegment58.children.append(HAnimSite59)
HAnimSite60 = x3d.HAnimSite()
HAnimSite60.name = "l_femoral_lateral_epicn_pt"
HAnimSite60.DEF = "hanim_l_femoral_lateral_epicn_pt"
HAnimSite60.translation = [0.1598,0.4967,0.0297]

HAnimSegment58.children.append(HAnimSite60)
HAnimSite61 = x3d.HAnimSite()
HAnimSite61.name = "l_femoral_medial_epicn_pt"
HAnimSite61.DEF = "hanim_l_femoral_medial_epicn_pt"
HAnimSite61.translation = [0.0398,0.4946,0.0303]

HAnimSegment58.children.append(HAnimSite61)

HAnimJoint57.children.append(HAnimSegment58)
HAnimJoint62 = x3d.HAnimJoint()
HAnimJoint62.name = "l_knee"
HAnimJoint62.DEF = "hanim_l_knee"
HAnimJoint62.center = [0.104,0.4867,0.0308]
HAnimJoint62.ulimit = [0,0,0]
HAnimJoint62.llimit = [0,0,0]
HAnimSegment63 = x3d.HAnimSegment()
HAnimSegment63.name = "l_calf"
HAnimSegment63.DEF = "hanim_l_calf"

HAnimJoint62.children.append(HAnimSegment63)
HAnimJoint64 = x3d.HAnimJoint()
HAnimJoint64.name = "l_ankle"
HAnimJoint64.DEF = "hanim_l_ankle"
HAnimJoint64.center = [0.1101,0.0656,-0.0736]
HAnimJoint64.ulimit = [0,0,0]
HAnimJoint64.llimit = [0,0,0]
HAnimSegment65 = x3d.HAnimSegment()
HAnimSegment65.name = "l_hindfoot"
HAnimSegment65.DEF = "hanim_l_hindfoot"
HAnimSite66 = x3d.HAnimSite()
HAnimSite66.name = "l_lateral_malleolus_pt"
HAnimSite66.DEF = "hanim_l_lateral_malleolus_pt"
HAnimSite66.translation = [0.1308,0.0597,-0.1032]

HAnimSegment65.children.append(HAnimSite66)
HAnimSite67 = x3d.HAnimSite()
HAnimSite67.name = "l_medial_malleolus_pt"
HAnimSite67.DEF = "hanim_l_medial_malleolus_pt"
HAnimSite67.translation = [0.089,0.0716,-0.0881]

HAnimSegment65.children.append(HAnimSite67)
HAnimSite68 = x3d.HAnimSite()
HAnimSite68.name = "l_sphyrion_pt"
HAnimSite68.DEF = "hanim_l_sphyrion_pt"
HAnimSite68.translation = [0.089,0.0575,-0.0943]

HAnimSegment65.children.append(HAnimSite68)
HAnimSite69 = x3d.HAnimSite()
HAnimSite69.name = "l_calcaneous_post_pt"
HAnimSite69.DEF = "hanim_l_calcaneous_post_pt"
HAnimSite69.translation = [0.0974,0.0259,-0.1171]

HAnimSegment65.children.append(HAnimSite69)

HAnimJoint64.children.append(HAnimSegment65)
HAnimJoint70 = x3d.HAnimJoint()
HAnimJoint70.name = "l_subtalar"
HAnimJoint70.DEF = "hanim_l_subtalar"
HAnimJoint70.center = [0.1086,0.0001,-0.0368]
HAnimJoint70.ulimit = [0,0,0]
HAnimJoint70.llimit = [0,0,0]
HAnimSegment71 = x3d.HAnimSegment()
HAnimSegment71.name = "l_midproximal"
HAnimSegment71.DEF = "hanim_l_midproximal"

HAnimJoint70.children.append(HAnimSegment71)
HAnimJoint72 = x3d.HAnimJoint()
HAnimJoint72.name = "l_midtarsal"
HAnimJoint72.DEF = "hanim_l_midtarsal"
HAnimJoint72.center = [0.1086,0.0001,0.0368]
HAnimJoint72.ulimit = [0,0,0]
HAnimJoint72.llimit = [0,0,0]
HAnimSegment73 = x3d.HAnimSegment()
HAnimSegment73.name = "l_middistal"
HAnimSegment73.DEF = "hanim_l_middistal"
HAnimSite74 = x3d.HAnimSite()
HAnimSite74.name = "l_metatarsal_pha1_pt"
HAnimSite74.DEF = "hanim_l_metatarsal_pha1_pt"
HAnimSite74.translation = [0.0816,0.0232,0.0106]

HAnimSegment73.children.append(HAnimSite74)

HAnimJoint72.children.append(HAnimSegment73)
HAnimJoint75 = x3d.HAnimJoint()
HAnimJoint75.name = "l_metatarsal"
HAnimJoint75.DEF = "hanim_l_metatarsal"
HAnimJoint75.center = [0.1086,0,0.0762]
HAnimJoint75.ulimit = [0,0,0]
HAnimJoint75.llimit = [0,0,0]
HAnimSegment76 = x3d.HAnimSegment()
HAnimSegment76.name = "l_forefoot"
HAnimSegment76.DEF = "hanim_l_forefoot"
HAnimSite77 = x3d.HAnimSite()
HAnimSite77.name = "l_forefoot_tip"
HAnimSite77.DEF = "hanim_l_forefoot_tip"
HAnimSite77.translation = [0.1354,0.0016,0.1476]

HAnimSegment76.children.append(HAnimSite77)
HAnimSite78 = x3d.HAnimSite()
HAnimSite78.name = "l_metatarsal_pha5_pt"
HAnimSite78.DEF = "hanim_l_metatarsal_pha5_pt"
HAnimSite78.translation = [0.1825,0.007,0.0928]

HAnimSegment76.children.append(HAnimSite78)
HAnimSite79 = x3d.HAnimSite()
HAnimSite79.name = "l_digit2_pt"
HAnimSite79.DEF = "hanim_l_digit2_pt"
HAnimSite79.translation = [0.1195,0.0079,0.1433]

HAnimSegment76.children.append(HAnimSite79)

HAnimJoint75.children.append(HAnimSegment76)

HAnimJoint72.children.append(HAnimJoint75)

HAnimJoint70.children.append(HAnimJoint72)

HAnimJoint64.children.append(HAnimJoint70)

HAnimJoint62.children.append(HAnimJoint64)

HAnimJoint57.children.append(HAnimJoint62)

HAnimJoint46.children.append(HAnimJoint57)
HAnimJoint80 = x3d.HAnimJoint()
HAnimJoint80.name = "r_hip"
HAnimJoint80.DEF = "hanim_r_hip"
HAnimJoint80.center = [-0.0961,0.9124,-0.0001]
HAnimJoint80.ulimit = [0,0,0]
HAnimJoint80.llimit = [0,0,0]
HAnimSegment81 = x3d.HAnimSegment()
HAnimSegment81.name = "r_thigh"
HAnimSegment81.DEF = "hanim_r_thigh"
HAnimSite82 = x3d.HAnimSite()
HAnimSite82.name = "r_knee_crease_pt"
HAnimSite82.DEF = "hanim_r_knee_crease_pt"
HAnimSite82.translation = [-0.0825,0.4932,-0.0326]

HAnimSegment81.children.append(HAnimSite82)
HAnimSite83 = x3d.HAnimSite()
HAnimSite83.name = "r_femoral_lateral_epicn_pt"
HAnimSite83.DEF = "hanim_r_femoral_lateral_epicn_pt"
HAnimSite83.translation = [-0.1421,0.4992,0.031]

HAnimSegment81.children.append(HAnimSite83)
HAnimSite84 = x3d.HAnimSite()
HAnimSite84.name = "r_femoral_medial_epicn_pt"
HAnimSite84.DEF = "hanim_r_femoral_medial_epicn_pt"
HAnimSite84.translation = [-0.0221,0.5014,0.0289]

HAnimSegment81.children.append(HAnimSite84)

HAnimJoint80.children.append(HAnimSegment81)
HAnimJoint85 = x3d.HAnimJoint()
HAnimJoint85.name = "r_knee"
HAnimJoint85.DEF = "hanim_r_knee"
HAnimJoint85.center = [-0.104,0.4867,0.0308]
HAnimJoint85.ulimit = [0,0,0]
HAnimJoint85.llimit = [0,0,0]
HAnimSegment86 = x3d.HAnimSegment()
HAnimSegment86.name = "r_calf"
HAnimSegment86.DEF = "hanim_r_calf"

HAnimJoint85.children.append(HAnimSegment86)
HAnimJoint87 = x3d.HAnimJoint()
HAnimJoint87.name = "r_ankle"
HAnimJoint87.DEF = "hanim_r_ankle"
HAnimJoint87.center = [-0.1101,0.0656,-0.0736]
HAnimJoint87.ulimit = [0,0,0]
HAnimJoint87.llimit = [0,0,0]
HAnimSegment88 = x3d.HAnimSegment()
HAnimSegment88.name = "r_hindfoot"
HAnimSegment88.DEF = "hanim_r_hindfoot"
HAnimSite89 = x3d.HAnimSite()
HAnimSite89.name = "r_lateral_malleolus_pt"
HAnimSite89.DEF = "hanim_r_lateral_malleolus_pt"
HAnimSite89.translation = [-0.1006,0.0658,-0.1075]

HAnimSegment88.children.append(HAnimSite89)
HAnimSite90 = x3d.HAnimSite()
HAnimSite90.name = "r_medial_malleolus_pt"
HAnimSite90.DEF = "hanim_r_medial_malleolus_pt"
HAnimSite90.translation = [-0.0591,0.076,-0.0928]

HAnimSegment88.children.append(HAnimSite90)
HAnimSite91 = x3d.HAnimSite()
HAnimSite91.name = "r_sphyrion_pt"
HAnimSite91.DEF = "hanim_r_sphyrion_pt"
HAnimSite91.translation = [-0.0603,0.061,-0.1002]

HAnimSegment88.children.append(HAnimSite91)
HAnimSite92 = x3d.HAnimSite()
HAnimSite92.name = "r_calcaneous_post_pt"
HAnimSite92.DEF = "hanim_r_calcaneous_post_pt"
HAnimSite92.translation = [-0.0692,0.0297,-0.1221]

HAnimSegment88.children.append(HAnimSite92)

HAnimJoint87.children.append(HAnimSegment88)
HAnimJoint93 = x3d.HAnimJoint()
HAnimJoint93.name = "r_subtalar"
HAnimJoint93.DEF = "hanim_r_subtalar"
HAnimJoint93.center = [-0.1086,0.0001,-0.0368]
HAnimJoint93.ulimit = [0,0,0]
HAnimJoint93.llimit = [0,0,0]
HAnimSegment94 = x3d.HAnimSegment()
HAnimSegment94.name = "r_midproximal"
HAnimSegment94.DEF = "hanim_r_midproximal"

HAnimJoint93.children.append(HAnimSegment94)
HAnimJoint95 = x3d.HAnimJoint()
HAnimJoint95.name = "r_midtarsal"
HAnimJoint95.DEF = "hanim_r_midtarsal"
HAnimJoint95.center = [-0.1086,0.0001,0.0368]
HAnimJoint95.ulimit = [0,0,0]
HAnimJoint95.llimit = [0,0,0]
HAnimSegment96 = x3d.HAnimSegment()
HAnimSegment96.name = "r_middistal"
HAnimSegment96.DEF = "hanim_r_middistal"
HAnimSite97 = x3d.HAnimSite()
HAnimSite97.name = "r_metatarsal_pha1_pt"
HAnimSite97.DEF = "hanim_r_metatarsal_pha1_pt"
HAnimSite97.translation = [-0.0521,0.026,0.0127]

HAnimSegment96.children.append(HAnimSite97)

HAnimJoint95.children.append(HAnimSegment96)
HAnimJoint98 = x3d.HAnimJoint()
HAnimJoint98.name = "r_metatarsal"
HAnimJoint98.DEF = "hanim_r_metatarsal"
HAnimJoint98.center = [-0.1086,0,0.0762]
HAnimJoint98.ulimit = [0,0,0]
HAnimJoint98.llimit = [0,0,0]
HAnimSegment99 = x3d.HAnimSegment()
HAnimSegment99.name = "r_forefoot"
HAnimSegment99.DEF = "hanim_r_forefoot"
HAnimSite100 = x3d.HAnimSite()
HAnimSite100.name = "r_forefoot_tip"
HAnimSite100.DEF = "hanim_r_forefoot_tip"
HAnimSite100.translation = [-0.1043,0.0227,0.145]

HAnimSegment99.children.append(HAnimSite100)
HAnimSite101 = x3d.HAnimSite()
HAnimSite101.name = "r_metatarsal_pha5_pt"
HAnimSite101.DEF = "hanim_r_metatarsal_pha5_pt"
HAnimSite101.translation = [-0.1523,0.0166,0.0895]

HAnimSegment99.children.append(HAnimSite101)
HAnimSite102 = x3d.HAnimSite()
HAnimSite102.name = "r_digit2_pt"
HAnimSite102.DEF = "hanim_r_digit2_pt"
HAnimSite102.translation = [-0.0883,0.0134,0.1383]

HAnimSegment99.children.append(HAnimSite102)

HAnimJoint98.children.append(HAnimSegment99)

HAnimJoint95.children.append(HAnimJoint98)

HAnimJoint93.children.append(HAnimJoint95)

HAnimJoint87.children.append(HAnimJoint93)

HAnimJoint85.children.append(HAnimJoint87)

HAnimJoint80.children.append(HAnimJoint85)

HAnimJoint46.children.append(HAnimJoint80)

HAnimJoint44.children.append(HAnimJoint46)
HAnimJoint103 = x3d.HAnimJoint()
HAnimJoint103.name = "vl5"
HAnimJoint103.DEF = "hanim_vl5"
HAnimJoint103.center = [0.0028,1.0568,-0.0776]
HAnimJoint103.ulimit = [0,0,0]
HAnimJoint103.llimit = [0,0,0]
HAnimSegment104 = x3d.HAnimSegment()
HAnimSegment104.name = "l5"
HAnimSegment104.DEF = "hanim_l5"
HAnimSite105 = x3d.HAnimSite()
HAnimSite105.name = "waist_preferred_post_pt"
HAnimSite105.DEF = "hanim_waist_preferred_post_pt"
HAnimSite105.translation = [0,1.0915,-0.1091]

HAnimSegment104.children.append(HAnimSite105)
HAnimSite106 = x3d.HAnimSite()
HAnimSite106.name = "navel_pt"
HAnimSite106.DEF = "hanim_navel_pt"
HAnimSite106.translation = [0.0069,1.0966,0.1017]

HAnimSegment104.children.append(HAnimSite106)

HAnimJoint103.children.append(HAnimSegment104)
HAnimJoint107 = x3d.HAnimJoint()
HAnimJoint107.name = "vl4"
HAnimJoint107.DEF = "hanim_vl4"
HAnimJoint107.center = [0.0035,1.0925,-0.0787]
HAnimJoint107.ulimit = [0,0,0]
HAnimJoint107.llimit = [0,0,0]
HAnimSegment108 = x3d.HAnimSegment()
HAnimSegment108.name = "l4"
HAnimSegment108.DEF = "hanim_l4"

HAnimJoint107.children.append(HAnimSegment108)
HAnimJoint109 = x3d.HAnimJoint()
HAnimJoint109.name = "vl3"
HAnimJoint109.DEF = "hanim_vl3"
HAnimJoint109.center = [0.0041,1.1276,-0.0796]
HAnimJoint109.ulimit = [0,0,0]
HAnimJoint109.llimit = [0,0,0]
HAnimSegment110 = x3d.HAnimSegment()
HAnimSegment110.name = "l3"
HAnimSegment110.DEF = "hanim_l3"

HAnimJoint109.children.append(HAnimSegment110)
HAnimJoint111 = x3d.HAnimJoint()
HAnimJoint111.name = "vl2"
HAnimJoint111.DEF = "hanim_vl2"
HAnimJoint111.center = [0.0045,1.1546,-0.08]
HAnimJoint111.ulimit = [0,0,0]
HAnimJoint111.llimit = [0,0,0]
HAnimSegment112 = x3d.HAnimSegment()
HAnimSegment112.name = "l2"
HAnimSegment112.DEF = "hanim_l2"
HAnimSite113 = x3d.HAnimSite()
HAnimSite113.name = "r_rib10_pt"
HAnimSite113.DEF = "hanim_r_rib10_pt"
HAnimSite113.translation = [-0.0711,1.1941,0.1016]

HAnimSegment112.children.append(HAnimSite113)
HAnimSite114 = x3d.HAnimSite()
HAnimSite114.name = "l_rib10_pt"
HAnimSite114.DEF = "hanim_l_rib10_pt"
HAnimSite114.translation = [0.0871,1.1925,0.0992]

HAnimSegment112.children.append(HAnimSite114)
HAnimSite115 = x3d.HAnimSite()
HAnimSite115.name = "rib10_midspine_pt"
HAnimSite115.DEF = "hanim_rib10_midspine_pt"
HAnimSite115.translation = [0.0049,1.1908,-0.1113]

HAnimSegment112.children.append(HAnimSite115)

HAnimJoint111.children.append(HAnimSegment112)
HAnimJoint116 = x3d.HAnimJoint()
HAnimJoint116.name = "vl1"
HAnimJoint116.DEF = "hanim_vl1"
HAnimJoint116.center = [0.0048,1.1912,-0.0805]
HAnimJoint116.ulimit = [0,0,0]
HAnimJoint116.llimit = [0,0,0]
HAnimSegment117 = x3d.HAnimSegment()
HAnimSegment117.name = "l1"
HAnimSegment117.DEF = "hanim_l1"

HAnimJoint116.children.append(HAnimSegment117)
HAnimJoint118 = x3d.HAnimJoint()
HAnimJoint118.name = "vt12"
HAnimJoint118.DEF = "hanim_vt12"
HAnimJoint118.center = [0.0051,1.2278,-0.0808]
HAnimJoint118.ulimit = [0,0,0]
HAnimJoint118.llimit = [0,0,0]
HAnimSegment119 = x3d.HAnimSegment()
HAnimSegment119.name = "t12"
HAnimSegment119.DEF = "hanim_t12"

HAnimJoint118.children.append(HAnimSegment119)
HAnimJoint120 = x3d.HAnimJoint()
HAnimJoint120.name = "vt11"
HAnimJoint120.DEF = "hanim_vt11"
HAnimJoint120.center = [0.0053,1.2679,-0.081]
HAnimJoint120.ulimit = [0,0,0]
HAnimJoint120.llimit = [0,0,0]
HAnimSegment121 = x3d.HAnimSegment()
HAnimSegment121.name = "t11"
HAnimSegment121.DEF = "hanim_t11"

HAnimJoint120.children.append(HAnimSegment121)
HAnimJoint122 = x3d.HAnimJoint()
HAnimJoint122.name = "vt10"
HAnimJoint122.DEF = "hanim_vt10"
HAnimJoint122.center = [0.0056,1.2848,-0.0822]
HAnimJoint122.ulimit = [0,0,0]
HAnimJoint122.llimit = [0,0,0]
HAnimSegment123 = x3d.HAnimSegment()
HAnimSegment123.name = "t10"
HAnimSegment123.DEF = "hanim_t10"
HAnimSite124 = x3d.HAnimSite()
HAnimSite124.name = "substernale_pt"
HAnimSite124.DEF = "hanim_substernale_pt"
HAnimSite124.translation = [0.0085,1.2995,0.1147]

HAnimSegment123.children.append(HAnimSite124)

HAnimJoint122.children.append(HAnimSegment123)
HAnimJoint125 = x3d.HAnimJoint()
HAnimJoint125.name = "vt9"
HAnimJoint125.DEF = "hanim_vt9"
HAnimJoint125.center = [0.0057,1.3126,-0.0838]
HAnimJoint125.ulimit = [0,0,0]
HAnimJoint125.llimit = [0,0,0]
HAnimSegment126 = x3d.HAnimSegment()
HAnimSegment126.name = "t9"
HAnimSegment126.DEF = "hanim_t9"
HAnimSite127 = x3d.HAnimSite()
HAnimSite127.name = "r_thelion_pt"
HAnimSite127.DEF = "hanim_r_thelion_pt"
HAnimSite127.translation = [-0.0736,1.3385,0.1217]

HAnimSegment126.children.append(HAnimSite127)
HAnimSite128 = x3d.HAnimSite()
HAnimSite128.name = "l_thelion_pt"
HAnimSite128.DEF = "hanim_l_thelion_pt"
HAnimSite128.translation = [0.0918,1.3382,0.1192]

HAnimSegment126.children.append(HAnimSite128)

HAnimJoint125.children.append(HAnimSegment126)
HAnimJoint129 = x3d.HAnimJoint()
HAnimJoint129.name = "vt8"
HAnimJoint129.DEF = "hanim_vt8"
HAnimJoint129.center = [0.0057,1.3382,-0.0845]
HAnimJoint129.ulimit = [0,0,0]
HAnimJoint129.llimit = [0,0,0]
HAnimSegment130 = x3d.HAnimSegment()
HAnimSegment130.name = "t8"
HAnimSegment130.DEF = "hanim_t8"

HAnimJoint129.children.append(HAnimSegment130)
HAnimJoint131 = x3d.HAnimJoint()
HAnimJoint131.name = "vt7"
HAnimJoint131.DEF = "hanim_vt7"
HAnimJoint131.center = [0.0058,1.3625,-0.0833]
HAnimJoint131.ulimit = [0,0,0]
HAnimJoint131.llimit = [0,0,0]
HAnimSegment132 = x3d.HAnimSegment()
HAnimSegment132.name = "t7"
HAnimSegment132.DEF = "hanim_t7"

HAnimJoint131.children.append(HAnimSegment132)
HAnimJoint133 = x3d.HAnimJoint()
HAnimJoint133.name = "vt6"
HAnimJoint133.DEF = "hanim_vt6"
HAnimJoint133.center = [0.0059,1.3866,-0.08]
HAnimJoint133.ulimit = [0,0,0]
HAnimJoint133.llimit = [0,0,0]
HAnimSegment134 = x3d.HAnimSegment()
HAnimSegment134.name = "t6"
HAnimSegment134.DEF = "hanim_t6"

HAnimJoint133.children.append(HAnimSegment134)
HAnimJoint135 = x3d.HAnimJoint()
HAnimJoint135.name = "vt5"
HAnimJoint135.DEF = "hanim_vt5"
HAnimJoint135.center = [0.006,1.4102,-0.0745]
HAnimJoint135.ulimit = [0,0,0]
HAnimJoint135.llimit = [0,0,0]
HAnimSegment136 = x3d.HAnimSegment()
HAnimSegment136.name = "t5"
HAnimSegment136.DEF = "hanim_t5"

HAnimJoint135.children.append(HAnimSegment136)
HAnimJoint137 = x3d.HAnimJoint()
HAnimJoint137.name = "vt4"
HAnimJoint137.DEF = "hanim_vt4"
HAnimJoint137.center = [0.0061,1.432,-0.0675]
HAnimJoint137.ulimit = [0,0,0]
HAnimJoint137.llimit = [0,0,0]
HAnimSegment138 = x3d.HAnimSegment()
HAnimSegment138.name = "t4"
HAnimSegment138.DEF = "hanim_t4"

HAnimJoint137.children.append(HAnimSegment138)
HAnimJoint139 = x3d.HAnimJoint()
HAnimJoint139.name = "vt3"
HAnimJoint139.DEF = "hanim_vt3"
HAnimJoint139.center = [0.0062,1.4583,-0.057]
HAnimJoint139.ulimit = [0,0,0]
HAnimJoint139.llimit = [0,0,0]
HAnimSegment140 = x3d.HAnimSegment()
HAnimSegment140.name = "t3"
HAnimSegment140.DEF = "hanim_t3"

HAnimJoint139.children.append(HAnimSegment140)
HAnimJoint141 = x3d.HAnimJoint()
HAnimJoint141.name = "vt2"
HAnimJoint141.DEF = "hanim_vt2"
HAnimJoint141.center = [0.0063,1.4761,-0.0484]
HAnimJoint141.ulimit = [0,0,0]
HAnimJoint141.llimit = [0,0,0]
HAnimSegment142 = x3d.HAnimSegment()
HAnimSegment142.name = "t2"
HAnimSegment142.DEF = "hanim_t2"

HAnimJoint141.children.append(HAnimSegment142)
HAnimJoint143 = x3d.HAnimJoint()
HAnimJoint143.name = "vt1"
HAnimJoint143.DEF = "hanim_vt1"
HAnimJoint143.center = [0.0065,1.4951,-0.0387]
HAnimJoint143.ulimit = [0,0,0]
HAnimJoint143.llimit = [0,0,0]
HAnimSegment144 = x3d.HAnimSegment()
HAnimSegment144.name = "t1"
HAnimSegment144.DEF = "hanim_t1"
HAnimSite145 = x3d.HAnimSite()
HAnimSite145.name = "suprasternale_pt"
HAnimSite145.DEF = "hanim_suprasternale_pt"
HAnimSite145.translation = [0.0084,1.4714,0.0551]

HAnimSegment144.children.append(HAnimSite145)
HAnimSite146 = x3d.HAnimSite()
HAnimSite146.name = "cervicale_pt"
HAnimSite146.DEF = "hanim_cervicale_pt"
HAnimSite146.translation = [0.0064,1.52,-0.0815]

HAnimSegment144.children.append(HAnimSite146)

HAnimJoint143.children.append(HAnimSegment144)
HAnimJoint147 = x3d.HAnimJoint()
HAnimJoint147.name = "vc7"
HAnimJoint147.DEF = "hanim_vc7"
HAnimJoint147.center = [0.0066,1.5132,-0.0301]
HAnimJoint147.ulimit = [0,0,0]
HAnimJoint147.llimit = [0,0,0]
HAnimSegment148 = x3d.HAnimSegment()
HAnimSegment148.name = "c7"
HAnimSegment148.DEF = "hanim_c7"
HAnimSite149 = x3d.HAnimSite()
HAnimSite149.name = "r_neck_base_pt"
HAnimSite149.DEF = "hanim_r_neck_base_pt"
HAnimSite149.translation = [-0.0419,1.5149,-0.022]

HAnimSegment148.children.append(HAnimSite149)
HAnimSite150 = x3d.HAnimSite()
HAnimSite150.name = "l_neck_base_pt"
HAnimSite150.DEF = "hanim_l_neck_base_pt"
HAnimSite150.translation = [0.0646,1.5141,-0.038]

HAnimSegment148.children.append(HAnimSite150)

HAnimJoint147.children.append(HAnimSegment148)
HAnimJoint151 = x3d.HAnimJoint()
HAnimJoint151.name = "vc6"
HAnimJoint151.DEF = "hanim_vc6"
HAnimJoint151.center = [0.0066,1.5357,-0.0143]
HAnimJoint151.ulimit = [0,0,0]
HAnimJoint151.llimit = [0,0,0]
HAnimSegment152 = x3d.HAnimSegment()
HAnimSegment152.name = "c6"
HAnimSegment152.DEF = "hanim_c6"

HAnimJoint151.children.append(HAnimSegment152)
HAnimJoint153 = x3d.HAnimJoint()
HAnimJoint153.name = "vc5"
HAnimJoint153.DEF = "hanim_vc5"
HAnimJoint153.center = [0.0066,1.552,-0.0082]
HAnimJoint153.ulimit = [0,0,0]
HAnimJoint153.llimit = [0,0,0]
HAnimSegment154 = x3d.HAnimSegment()
HAnimSegment154.name = "c5"
HAnimSegment154.DEF = "hanim_c5"

HAnimJoint153.children.append(HAnimSegment154)
HAnimJoint155 = x3d.HAnimJoint()
HAnimJoint155.name = "vc4"
HAnimJoint155.DEF = "hanim_vc4"
HAnimJoint155.center = [0.0066,1.5662,-0.0084]
HAnimJoint155.ulimit = [0,0,0]
HAnimJoint155.llimit = [0,0,0]
HAnimSegment156 = x3d.HAnimSegment()
HAnimSegment156.name = "c4"
HAnimSegment156.DEF = "hanim_c4"

HAnimJoint155.children.append(HAnimSegment156)
HAnimJoint157 = x3d.HAnimJoint()
HAnimJoint157.name = "vc3"
HAnimJoint157.DEF = "hanim_vc3"
HAnimJoint157.center = [0.0066,1.58,-0.0103]
HAnimJoint157.ulimit = [0,0,0]
HAnimJoint157.llimit = [0,0,0]
HAnimSegment158 = x3d.HAnimSegment()
HAnimSegment158.name = "c3"
HAnimSegment158.DEF = "hanim_c3"

HAnimJoint157.children.append(HAnimSegment158)
HAnimJoint159 = x3d.HAnimJoint()
HAnimJoint159.name = "vc2"
HAnimJoint159.DEF = "hanim_vc2"
HAnimJoint159.center = [0.0066,1.5928,-0.0103]
HAnimJoint159.ulimit = [0,0,0]
HAnimJoint159.llimit = [0,0,0]
HAnimSegment160 = x3d.HAnimSegment()
HAnimSegment160.name = "c2"
HAnimSegment160.DEF = "hanim_c2"

HAnimJoint159.children.append(HAnimSegment160)
HAnimJoint161 = x3d.HAnimJoint()
HAnimJoint161.name = "vc1"
HAnimJoint161.DEF = "hanim_vc1"
HAnimJoint161.center = [0.0066,1.6144,-0.0034]
HAnimJoint161.ulimit = [0,0,0]
HAnimJoint161.llimit = [0,0,0]
HAnimSegment162 = x3d.HAnimSegment()
HAnimSegment162.name = "c1"
HAnimSegment162.DEF = "hanim_c1"

HAnimJoint161.children.append(HAnimSegment162)
HAnimJoint163 = x3d.HAnimJoint()
HAnimJoint163.name = "skullbase"
HAnimJoint163.DEF = "hanim_skullbase"
HAnimJoint163.center = [0.0044,1.6209,0.0236]
HAnimJoint163.ulimit = [0,0,0]
HAnimJoint163.llimit = [0,0,0]
HAnimSegment164 = x3d.HAnimSegment()
HAnimSegment164.name = "skull"
HAnimSegment164.DEF = "hanim_skull"
HAnimSite165 = x3d.HAnimSite()
HAnimSite165.name = "skull_tip"
HAnimSite165.DEF = "hanim_skull_tip"
HAnimSite165.translation = [0.005,1.7504,0.0055]
#TODO move skull_tip x to zero, check others for symmetry

HAnimSegment164.children.append(HAnimSite165)
HAnimSite166 = x3d.HAnimSite()
HAnimSite166.name = "sellion_pt"
HAnimSite166.DEF = "hanim_sellion_pt"
HAnimSite166.translation = [0.0058,1.6316,0.0852]

HAnimSegment164.children.append(HAnimSite166)
HAnimSite167 = x3d.HAnimSite()
HAnimSite167.name = "r_infraorbitale_pt"
HAnimSite167.DEF = "hanim_r_infraorbitale_pt"
HAnimSite167.translation = [-0.0237,1.6171,0.0752]

HAnimSegment164.children.append(HAnimSite167)
HAnimSite168 = x3d.HAnimSite()
HAnimSite168.name = "l_infraorbitale_pt"
HAnimSite168.DEF = "hanim_l_infraorbitale_pt"
HAnimSite168.translation = [0.0341,1.6171,0.0752]

HAnimSegment164.children.append(HAnimSite168)
HAnimSite169 = x3d.HAnimSite()
HAnimSite169.name = "supramenton_pt"
HAnimSite169.DEF = "hanim_supramenton_pt"
HAnimSite169.translation = [0.0061,1.541,0.0805]

HAnimSegment164.children.append(HAnimSite169)
HAnimSite170 = x3d.HAnimSite()
HAnimSite170.name = "r_tragion_pt"
HAnimSite170.DEF = "hanim_r_tragion_pt"
HAnimSite170.translation = [-0.0646,1.6347,0.0302]

HAnimSegment164.children.append(HAnimSite170)
HAnimSite171 = x3d.HAnimSite()
HAnimSite171.name = "r_gonion_pt"
HAnimSite171.DEF = "hanim_r_gonion_pt"
HAnimSite171.translation = [-0.052,1.5529,0.0347]

HAnimSegment164.children.append(HAnimSite171)
HAnimSite172 = x3d.HAnimSite()
HAnimSite172.name = "l_tragion_pt"
HAnimSite172.DEF = "hanim_l_tragion_pt"
HAnimSite172.translation = [0.0739,1.6348,0.0282]

HAnimSegment164.children.append(HAnimSite172)
HAnimSite173 = x3d.HAnimSite()
HAnimSite173.name = "l_gonion_pt"
HAnimSite173.DEF = "hanim_l_gonion_pt"
HAnimSite173.translation = [0.0631,1.553,0.033]

HAnimSegment164.children.append(HAnimSite173)
HAnimSite174 = x3d.HAnimSite()
HAnimSite174.name = "nuchale_pt"
HAnimSite174.DEF = "hanim_nuchale_pt"
HAnimSite174.translation = [0.0039,1.5972,-0.0796]

HAnimSegment164.children.append(HAnimSite174)

HAnimJoint163.children.append(HAnimSegment164)
HAnimJoint175 = x3d.HAnimJoint()
HAnimJoint175.name = "l_eyeball_joint"
HAnimJoint175.DEF = "hanim_l_eyeball_joint"
HAnimJoint175.center = [0.0336,1.6332,0.0502]
HAnimJoint175.ulimit = [0,0,0]
HAnimJoint175.llimit = [0,0,0]
HAnimSegment176 = x3d.HAnimSegment()
HAnimSegment176.name = "l_eyeball"
HAnimSegment176.DEF = "hanim_l_eyeball"
HAnimSite177 = x3d.HAnimSite()
HAnimSite177.name = "l_eyeball_site_view"
HAnimSite177.DEF = "hanim_l_eyeball_site_view"
HAnimSite177.translation = [0.034,1.64,0.05]
Viewpoint178 = x3d.Viewpoint()
Viewpoint178.DEF = "hanim_l_eyeball_site_viewpoint"
Viewpoint178.description = "l_eyeball_site_viewpoint looking forward"
Viewpoint178.orientation = [0,1,0,3.141593]
Viewpoint178.position = [0,0,0]

HAnimSite177.children.append(Viewpoint178)

HAnimSegment176.children.append(HAnimSite177)

HAnimJoint175.children.append(HAnimSegment176)

HAnimJoint163.children.append(HAnimJoint175)
HAnimJoint179 = x3d.HAnimJoint()
HAnimJoint179.name = "l_eyelid_joint"
HAnimJoint179.DEF = "hanim_l_eyelid_joint"
HAnimJoint179.center = [0.0336,1.6332,0.0502]
HAnimJoint179.ulimit = [0,0,0]
HAnimJoint179.llimit = [0,0,0]
HAnimSegment180 = x3d.HAnimSegment()
HAnimSegment180.name = "l_eyelid"
HAnimSegment180.DEF = "hanim_l_eyelid"

HAnimJoint179.children.append(HAnimSegment180)

HAnimJoint163.children.append(HAnimJoint179)
HAnimJoint181 = x3d.HAnimJoint()
HAnimJoint181.name = "l_eyebrow_joint"
HAnimJoint181.DEF = "hanim_l_eyebrow_joint"
HAnimJoint181.center = [0.0336,1.635,0.0506]
HAnimJoint181.ulimit = [0,0,0]
HAnimJoint181.llimit = [0,0,0]
HAnimSegment182 = x3d.HAnimSegment()
HAnimSegment182.name = "l_eyebrow"
HAnimSegment182.DEF = "hanim_l_eyebrow"

HAnimJoint181.children.append(HAnimSegment182)

HAnimJoint163.children.append(HAnimJoint181)
HAnimJoint183 = x3d.HAnimJoint()
HAnimJoint183.name = "r_eyeball_joint"
HAnimJoint183.DEF = "hanim_r_eyeball_joint"
HAnimJoint183.center = [-0.0336,1.6332,0.0502]
HAnimJoint183.ulimit = [0,0,0]
HAnimJoint183.llimit = [0,0,0]
HAnimSegment184 = x3d.HAnimSegment()
HAnimSegment184.name = "r_eyeball"
HAnimSegment184.DEF = "hanim_r_eyeball"
HAnimSite185 = x3d.HAnimSite()
HAnimSite185.name = "r_eyeball_site_view"
HAnimSite185.DEF = "hanim_r_eyeball_site_view"
HAnimSite185.translation = [-0.034,1.64,0.05]
Viewpoint186 = x3d.Viewpoint()
Viewpoint186.DEF = "hanim_r_eyeball_site_viewpoint"
Viewpoint186.description = "r_eyeball_site_viewpoint looking forward"
Viewpoint186.orientation = [0,1,0,3.141593]
Viewpoint186.position = [0,0,0]

HAnimSite185.children.append(Viewpoint186)

HAnimSegment184.children.append(HAnimSite185)

HAnimJoint183.children.append(HAnimSegment184)

HAnimJoint163.children.append(HAnimJoint183)
HAnimJoint187 = x3d.HAnimJoint()
HAnimJoint187.name = "r_eyelid_joint"
HAnimJoint187.DEF = "hanim_r_eyelid_joint"
HAnimJoint187.center = [-0.0336,1.6332,0.0502]
HAnimJoint187.ulimit = [0,0,0]
HAnimJoint187.llimit = [0,0,0]
HAnimSegment188 = x3d.HAnimSegment()
HAnimSegment188.name = "r_eyelid"
HAnimSegment188.DEF = "hanim_r_eyelid"

HAnimJoint187.children.append(HAnimSegment188)

HAnimJoint163.children.append(HAnimJoint187)
HAnimJoint189 = x3d.HAnimJoint()
HAnimJoint189.name = "r_eyebrow_joint"
HAnimJoint189.DEF = "hanim_r_eyebrow_joint"
HAnimJoint189.center = [-0.0336,1.635,0.0506]
HAnimJoint189.ulimit = [0,0,0]
HAnimJoint189.llimit = [0,0,0]
HAnimSegment190 = x3d.HAnimSegment()
HAnimSegment190.name = "r_eyebrow"
HAnimSegment190.DEF = "hanim_r_eyebrow"

HAnimJoint189.children.append(HAnimSegment190)

HAnimJoint163.children.append(HAnimJoint189)
HAnimJoint191 = x3d.HAnimJoint()
HAnimJoint191.name = "temporomandibular"
HAnimJoint191.DEF = "hanim_temporomandibular"
HAnimJoint191.center = [0,1.63,0.015]
HAnimJoint191.ulimit = [0,0,0]
HAnimJoint191.llimit = [0,0,0]
#Single joint, single segment for jaw, two sites for left/right TMJs https://en.wikipedia.org/wiki/Temporomandibular_joint
HAnimSegment192 = x3d.HAnimSegment()
HAnimSegment192.name = "jaw"
HAnimSegment192.DEF = "hanim_jaw"
HAnimSite193 = x3d.HAnimSite()
HAnimSite193.name = "temporomandibular_l_site_pt"
HAnimSite193.DEF = "hanim_temporomandibular_l_site_pt"
HAnimSite193.translation = [0.045,1.63,0]

HAnimSegment192.children.append(HAnimSite193)
HAnimSite194 = x3d.HAnimSite()
HAnimSite194.name = "temporomandibular_r_site_pt"
HAnimSite194.DEF = "hanim_temporomandibular_r_site_pt"
HAnimSite194.translation = [-0.045,1.63,0]

HAnimSegment192.children.append(HAnimSite194)

HAnimJoint191.children.append(HAnimSegment192)

HAnimJoint163.children.append(HAnimJoint191)

HAnimJoint161.children.append(HAnimJoint163)

HAnimJoint159.children.append(HAnimJoint161)

HAnimJoint157.children.append(HAnimJoint159)

HAnimJoint155.children.append(HAnimJoint157)

HAnimJoint153.children.append(HAnimJoint155)

HAnimJoint151.children.append(HAnimJoint153)

HAnimJoint147.children.append(HAnimJoint151)

HAnimJoint143.children.append(HAnimJoint147)
HAnimJoint195 = x3d.HAnimJoint()
HAnimJoint195.name = "l_sternoclavicular"
HAnimJoint195.DEF = "hanim_l_sternoclavicular"
HAnimJoint195.center = [0.082,1.4488,-0.0353]
HAnimJoint195.ulimit = [0,0,0]
HAnimJoint195.llimit = [0,0,0]
HAnimSegment196 = x3d.HAnimSegment()
HAnimSegment196.name = "l_clavicle"
HAnimSegment196.DEF = "hanim_l_clavicle"
HAnimSite197 = x3d.HAnimSite()
HAnimSite197.name = "l_clavicale_pt"
HAnimSite197.DEF = "hanim_l_clavicale_pt"
HAnimSite197.translation = [0.0271,1.4943,0.0394]

HAnimSegment196.children.append(HAnimSite197)
HAnimSite198 = x3d.HAnimSite()
HAnimSite198.name = "l_acromion_pt"
HAnimSite198.DEF = "hanim_l_acromion_pt"
HAnimSite198.translation = [0.2032,1.476,-0.049]

HAnimSegment196.children.append(HAnimSite198)
HAnimSite199 = x3d.HAnimSite()
HAnimSite199.name = "l_axilla_ant_pt"
HAnimSite199.DEF = "hanim_l_axilla_ant_pt"
HAnimSite199.translation = [0.1777,1.4065,-0.0075]

HAnimSegment196.children.append(HAnimSite199)
HAnimSite200 = x3d.HAnimSite()
HAnimSite200.name = "l_axilla_post_pt"
HAnimSite200.DEF = "hanim_l_axilla_post_pt"
HAnimSite200.translation = [0.1706,1.4072,-0.0875]

HAnimSegment196.children.append(HAnimSite200)

HAnimJoint195.children.append(HAnimSegment196)
HAnimJoint201 = x3d.HAnimJoint()
HAnimJoint201.name = "l_acromioclavicular"
HAnimJoint201.DEF = "hanim_l_acromioclavicular"
HAnimJoint201.center = [0.0962,1.4269,-0.0424]
HAnimJoint201.ulimit = [0,0,0]
HAnimJoint201.llimit = [0,0,0]
HAnimSegment202 = x3d.HAnimSegment()
HAnimSegment202.name = "l_scapula"
HAnimSegment202.DEF = "hanim_l_scapula"

HAnimJoint201.children.append(HAnimSegment202)
HAnimJoint203 = x3d.HAnimJoint()
HAnimJoint203.name = "l_shoulder"
HAnimJoint203.DEF = "hanim_l_shoulder"
HAnimJoint203.center = [0.2029,1.4376,-0.0387]
HAnimJoint203.ulimit = [0,0,0]
HAnimJoint203.llimit = [0,0,0]
HAnimSegment204 = x3d.HAnimSegment()
HAnimSegment204.name = "l_upperarm"
HAnimSegment204.DEF = "hanim_l_upperarm"
HAnimSite205 = x3d.HAnimSite()
HAnimSite205.name = "l_humeral_lateral_epicn_pt"
HAnimSite205.DEF = "hanim_l_humeral_lateral_epicn_pt"
HAnimSite205.translation = [0.228,1.1482,-0.11]

HAnimSegment204.children.append(HAnimSite205)

HAnimJoint203.children.append(HAnimSegment204)
HAnimJoint206 = x3d.HAnimJoint()
HAnimJoint206.name = "l_elbow"
HAnimJoint206.DEF = "hanim_l_elbow"
HAnimJoint206.center = [0.2014,1.1357,-0.0682]
HAnimJoint206.ulimit = [0,0,0]
HAnimJoint206.llimit = [0,0,0]
HAnimSegment207 = x3d.HAnimSegment()
HAnimSegment207.name = "l_forearm"
HAnimSegment207.DEF = "hanim_l_forearm"
HAnimSite208 = x3d.HAnimSite()
HAnimSite208.name = "l_radial_styloid_pt"
HAnimSite208.DEF = "hanim_l_radial_styloid_pt"
HAnimSite208.translation = [0.1901,0.8645,-0.0415]

HAnimSegment207.children.append(HAnimSite208)
HAnimSite209 = x3d.HAnimSite()
HAnimSite209.name = "l_olecranon_pt"
HAnimSite209.DEF = "hanim_l_olecranon_pt"
HAnimSite209.translation = [0.1962,1.1375,-0.1123]

HAnimSegment207.children.append(HAnimSite209)
HAnimSite210 = x3d.HAnimSite()
HAnimSite210.name = "l_humeral_medial_epicn_pt"
HAnimSite210.DEF = "hanim_l_humeral_medial_epicn_pt"
HAnimSite210.translation = [0.1735,1.1272,-0.1113]

HAnimSegment207.children.append(HAnimSite210)
HAnimSite211 = x3d.HAnimSite()
HAnimSite211.name = "l_radiale_pt"
HAnimSite211.DEF = "hanim_l_radiale_pt"
HAnimSite211.translation = [0.2182,1.1212,-0.1167]

HAnimSegment207.children.append(HAnimSite211)

HAnimJoint206.children.append(HAnimSegment207)
HAnimJoint212 = x3d.HAnimJoint()
HAnimJoint212.name = "l_wrist"
HAnimJoint212.DEF = "hanim_l_wrist"
HAnimJoint212.center = [0.1984,0.8663,-0.0583]
HAnimJoint212.ulimit = [0,0,0]
HAnimJoint212.llimit = [0,0,0]
HAnimSegment213 = x3d.HAnimSegment()
HAnimSegment213.name = "l_hand"
HAnimSegment213.DEF = "hanim_l_hand"
HAnimSite214 = x3d.HAnimSite()
HAnimSite214.name = "l_metacarpal_pha2_pt"
HAnimSite214.DEF = "hanim_l_metacarpal_pha2_pt"
HAnimSite214.translation = [0.2009,0.8139,-0.0237]

HAnimSegment213.children.append(HAnimSite214)
HAnimSite215 = x3d.HAnimSite()
HAnimSite215.name = "l_ulnar_styloid_pt"
HAnimSite215.DEF = "hanim_l_ulnar_styloid_pt"
HAnimSite215.translation = [0.2142,0.8529,-0.0648]

HAnimSegment213.children.append(HAnimSite215)
HAnimSite216 = x3d.HAnimSite()
HAnimSite216.name = "l_metacarpal_pha5_pt"
HAnimSite216.DEF = "hanim_l_metacarpal_pha5_pt"
HAnimSite216.translation = [0.1929,0.786,-0.1122]

HAnimSegment213.children.append(HAnimSite216)
HAnimSite217 = x3d.HAnimSite()
HAnimSite217.name = "l_hand_front_view"
HAnimSite217.DEF = "hanim_l_hand_front_view"
HAnimSite217.translation = [0.3,0.75,0.45]
Viewpoint218 = x3d.Viewpoint()
Viewpoint218.DEF = "hanim_l_hand_front_viewpoint"
Viewpoint218.centerOfRotation = [0,0.7,0]
Viewpoint218.description = "left hand front"
Viewpoint218.position = [0,0,0]

HAnimSite217.children.append(Viewpoint218)

HAnimSegment213.children.append(HAnimSite217)

HAnimJoint212.children.append(HAnimSegment213)
HAnimJoint219 = x3d.HAnimJoint()
HAnimJoint219.name = "l_thumb1"
HAnimJoint219.DEF = "hanim_l_thumb1"
HAnimJoint219.center = [0.1924,0.8472,-0.0534]
HAnimJoint219.ulimit = [0,0,0]
HAnimJoint219.llimit = [0,0,0]
HAnimSegment220 = x3d.HAnimSegment()
HAnimSegment220.name = "l_thumb_metacarpal"
HAnimSegment220.DEF = "hanim_l_thumb_metacarpal"

HAnimJoint219.children.append(HAnimSegment220)
HAnimJoint221 = x3d.HAnimJoint()
HAnimJoint221.name = "l_thumb2"
HAnimJoint221.DEF = "hanim_l_thumb2"
HAnimJoint221.center = [0.1951,0.8226,0.0246]
HAnimJoint221.ulimit = [0,0,0]
HAnimJoint221.llimit = [0,0,0]
HAnimSegment222 = x3d.HAnimSegment()
HAnimSegment222.name = "l_thumb_proximal"
HAnimSegment222.DEF = "hanim_l_thumb_proximal"

HAnimJoint221.children.append(HAnimSegment222)
HAnimJoint223 = x3d.HAnimJoint()
HAnimJoint223.name = "l_thumb3"
HAnimJoint223.DEF = "hanim_l_thumb3"
HAnimJoint223.center = [0.1955,0.8159,0.0464]
HAnimJoint223.ulimit = [0,0,0]
HAnimJoint223.llimit = [0,0,0]
HAnimSegment224 = x3d.HAnimSegment()
HAnimSegment224.name = "l_thumb_distal"
HAnimSegment224.DEF = "hanim_l_thumb_distal"
HAnimSite225 = x3d.HAnimSite()
HAnimSite225.name = "l_thumb_distal_tip"
HAnimSite225.DEF = "hanim_l_thumb_distal_tip"
HAnimSite225.translation = [0.1982,0.8061,0.0759]

HAnimSegment224.children.append(HAnimSite225)

HAnimJoint223.children.append(HAnimSegment224)

HAnimJoint221.children.append(HAnimJoint223)

HAnimJoint219.children.append(HAnimJoint221)

HAnimJoint212.children.append(HAnimJoint219)
HAnimJoint226 = x3d.HAnimJoint()
HAnimJoint226.name = "l_index0"
HAnimJoint226.DEF = "hanim_l_index0"
HAnimJoint226.center = [0.1983,0.8024,-0.028]
HAnimJoint226.ulimit = [0,0,0]
HAnimJoint226.llimit = [0,0,0]
HAnimSegment227 = x3d.HAnimSegment()
HAnimSegment227.name = "l_index_metacarpal"
HAnimSegment227.DEF = "hanim_l_index_metacarpal"

HAnimJoint226.children.append(HAnimSegment227)
HAnimJoint228 = x3d.HAnimJoint()
HAnimJoint228.name = "l_index1"
HAnimJoint228.DEF = "hanim_l_index1"
HAnimJoint228.center = [0.1983,0.7815,-0.028]
HAnimJoint228.ulimit = [0,0,0]
HAnimJoint228.llimit = [0,0,0]
HAnimSegment229 = x3d.HAnimSegment()
HAnimSegment229.name = "l_index_proximal"
HAnimSegment229.DEF = "hanim_l_index_proximal"

HAnimJoint228.children.append(HAnimSegment229)
HAnimJoint230 = x3d.HAnimJoint()
HAnimJoint230.name = "l_index2"
HAnimJoint230.DEF = "hanim_l_index2"
HAnimJoint230.center = [0.2017,0.7363,-0.0248]
HAnimJoint230.ulimit = [0,0,0]
HAnimJoint230.llimit = [0,0,0]
HAnimSegment231 = x3d.HAnimSegment()
HAnimSegment231.name = "l_index_middle"
HAnimSegment231.DEF = "hanim_l_index_middle"

HAnimJoint230.children.append(HAnimSegment231)
HAnimJoint232 = x3d.HAnimJoint()
HAnimJoint232.name = "l_index3"
HAnimJoint232.DEF = "hanim_l_index3"
HAnimJoint232.center = [0.2028,0.7139,-0.0236]
HAnimJoint232.ulimit = [0,0,0]
HAnimJoint232.llimit = [0,0,0]
HAnimSegment233 = x3d.HAnimSegment()
HAnimSegment233.name = "l_index_distal"
HAnimSegment233.DEF = "hanim_l_index_distal"
HAnimSite234 = x3d.HAnimSite()
HAnimSite234.name = "l_index_distal_tip"
HAnimSite234.DEF = "hanim_l_index_distal_tip"
HAnimSite234.translation = [0.2089,0.6858,-0.0245]

HAnimSegment233.children.append(HAnimSite234)
HAnimSite235 = x3d.HAnimSite()
HAnimSite235.name = "l_dactylion_pt"
HAnimSite235.DEF = "hanim_l_dactylion_pt"
HAnimSite235.translation = [0.2056,0.6743,-0.0482]

HAnimSegment233.children.append(HAnimSite235)

HAnimJoint232.children.append(HAnimSegment233)

HAnimJoint230.children.append(HAnimJoint232)

HAnimJoint228.children.append(HAnimJoint230)

HAnimJoint226.children.append(HAnimJoint228)

HAnimJoint212.children.append(HAnimJoint226)
HAnimJoint236 = x3d.HAnimJoint()
HAnimJoint236.name = "l_middle0"
HAnimJoint236.DEF = "hanim_l_middle0"
HAnimJoint236.center = [0.1987,0.8029,-0.053]
HAnimJoint236.ulimit = [0,0,0]
HAnimJoint236.llimit = [0,0,0]
HAnimSegment237 = x3d.HAnimSegment()
HAnimSegment237.name = "l_middle_metacarpal"
HAnimSegment237.DEF = "hanim_l_middle_metacarpal"

HAnimJoint236.children.append(HAnimSegment237)
HAnimJoint238 = x3d.HAnimJoint()
HAnimJoint238.name = "l_middle1"
HAnimJoint238.DEF = "hanim_l_middle1"
HAnimJoint238.center = [0.1987,0.7818,-0.053]
HAnimJoint238.ulimit = [0,0,0]
HAnimJoint238.llimit = [0,0,0]
HAnimSegment239 = x3d.HAnimSegment()
HAnimSegment239.name = "l_middle_proximal"
HAnimSegment239.DEF = "hanim_l_middle_proximal"

HAnimJoint238.children.append(HAnimSegment239)
HAnimJoint240 = x3d.HAnimJoint()
HAnimJoint240.name = "l_middle2"
HAnimJoint240.DEF = "hanim_l_middle2"
HAnimJoint240.center = [0.2013,0.7273,-0.0503]
HAnimJoint240.ulimit = [0,0,0]
HAnimJoint240.llimit = [0,0,0]
HAnimSegment241 = x3d.HAnimSegment()
HAnimSegment241.name = "l_middle_middle"
HAnimSegment241.DEF = "hanim_l_middle_middle"

HAnimJoint240.children.append(HAnimSegment241)
HAnimJoint242 = x3d.HAnimJoint()
HAnimJoint242.name = "l_middle3"
HAnimJoint242.DEF = "hanim_l_middle3"
HAnimJoint242.center = [0.2026,0.7011,-0.0494]
HAnimJoint242.ulimit = [0,0,0]
HAnimJoint242.llimit = [0,0,0]
HAnimSegment243 = x3d.HAnimSegment()
HAnimSegment243.name = "l_middle_distal"
HAnimSegment243.DEF = "hanim_l_middle_distal"
HAnimSite244 = x3d.HAnimSite()
HAnimSite244.name = "l_middle_distal_tip"
HAnimSite244.DEF = "hanim_l_middle_distal_tip"
HAnimSite244.translation = [0.208,0.6731,-0.0491]

HAnimSegment243.children.append(HAnimSite244)

HAnimJoint242.children.append(HAnimSegment243)

HAnimJoint240.children.append(HAnimJoint242)

HAnimJoint238.children.append(HAnimJoint240)

HAnimJoint236.children.append(HAnimJoint238)

HAnimJoint212.children.append(HAnimJoint236)
HAnimJoint245 = x3d.HAnimJoint()
HAnimJoint245.name = "l_ring0"
HAnimJoint245.DEF = "hanim_l_ring0"
HAnimJoint245.center = [0.1956,0.8019,-0.0794]
HAnimJoint245.ulimit = [0,0,0]
HAnimJoint245.llimit = [0,0,0]
HAnimSegment246 = x3d.HAnimSegment()
HAnimSegment246.name = "l_ring_metacarpal"
HAnimSegment246.DEF = "hanim_l_ring_metacarpal"

HAnimJoint245.children.append(HAnimSegment246)
HAnimJoint247 = x3d.HAnimJoint()
HAnimJoint247.name = "l_ring1"
HAnimJoint247.DEF = "hanim_l_ring1"
HAnimJoint247.center = [0.1956,0.7815,-0.0794]
HAnimJoint247.ulimit = [0,0,0]
HAnimJoint247.llimit = [0,0,0]
HAnimSegment248 = x3d.HAnimSegment()
HAnimSegment248.name = "l_ring_proximal"
HAnimSegment248.DEF = "hanim_l_ring_proximal"

HAnimJoint247.children.append(HAnimSegment248)
HAnimJoint249 = x3d.HAnimJoint()
HAnimJoint249.name = "l_ring2"
HAnimJoint249.DEF = "hanim_l_ring2"
HAnimJoint249.center = [0.1973,0.7287,-0.0777]
HAnimJoint249.ulimit = [0,0,0]
HAnimJoint249.llimit = [0,0,0]
HAnimSegment250 = x3d.HAnimSegment()
HAnimSegment250.name = "l_ring_middle"
HAnimSegment250.DEF = "hanim_l_ring_middle"

HAnimJoint249.children.append(HAnimSegment250)
HAnimJoint251 = x3d.HAnimJoint()
HAnimJoint251.name = "l_ring3"
HAnimJoint251.DEF = "hanim_l_ring3"
HAnimJoint251.center = [0.1983,0.7045,-0.0767]
HAnimJoint251.ulimit = [0,0,0]
HAnimJoint251.llimit = [0,0,0]
HAnimSegment252 = x3d.HAnimSegment()
HAnimSegment252.name = "l_ring_distal"
HAnimSegment252.DEF = "hanim_l_ring_distal"
HAnimSite253 = x3d.HAnimSite()
HAnimSite253.name = "l_ring_distal_tip"
HAnimSite253.DEF = "hanim_l_ring_distal_tip"
HAnimSite253.translation = [0.2035,0.675,-0.0756]

HAnimSegment252.children.append(HAnimSite253)

HAnimJoint251.children.append(HAnimSegment252)

HAnimJoint249.children.append(HAnimJoint251)

HAnimJoint247.children.append(HAnimJoint249)

HAnimJoint245.children.append(HAnimJoint247)

HAnimJoint212.children.append(HAnimJoint245)
HAnimJoint254 = x3d.HAnimJoint()
HAnimJoint254.name = "l_pinky0"
HAnimJoint254.DEF = "hanim_l_pinky0"
HAnimJoint254.center = [0.1925,0.8066,-0.1036]
HAnimJoint254.ulimit = [0,0,0]
HAnimJoint254.llimit = [0,0,0]
HAnimSegment255 = x3d.HAnimSegment()
HAnimSegment255.name = "l_pinky_metacarpal"
HAnimSegment255.DEF = "hanim_l_pinky_metacarpal"

HAnimJoint254.children.append(HAnimSegment255)
HAnimJoint256 = x3d.HAnimJoint()
HAnimJoint256.name = "l_pinky1"
HAnimJoint256.DEF = "hanim_l_pinky1"
HAnimJoint256.center = [0.1925,0.7866,-0.1036]
HAnimJoint256.ulimit = [0,0,0]
HAnimJoint256.llimit = [0,0,0]
HAnimSegment257 = x3d.HAnimSegment()
HAnimSegment257.name = "l_pinky_proximal"
HAnimSegment257.DEF = "hanim_l_pinky_proximal"

HAnimJoint256.children.append(HAnimSegment257)
HAnimJoint258 = x3d.HAnimJoint()
HAnimJoint258.name = "l_pinky2"
HAnimJoint258.DEF = "hanim_l_pinky2"
HAnimJoint258.center = [0.1938,0.7452,-0.1024]
HAnimJoint258.ulimit = [0,0,0]
HAnimJoint258.llimit = [0,0,0]
HAnimSegment259 = x3d.HAnimSegment()
HAnimSegment259.name = "l_pinky_middle"
HAnimSegment259.DEF = "hanim_l_pinky_middle"

HAnimJoint258.children.append(HAnimSegment259)
HAnimJoint260 = x3d.HAnimJoint()
HAnimJoint260.name = "l_pinky3"
HAnimJoint260.DEF = "hanim_l_pinky3"
HAnimJoint260.center = [0.1948,0.7277,-0.1017]
HAnimJoint260.ulimit = [0,0,0]
HAnimJoint260.llimit = [0,0,0]
HAnimSegment261 = x3d.HAnimSegment()
HAnimSegment261.name = "l_pinky_distal"
HAnimSegment261.DEF = "hanim_l_pinky_distal"
HAnimSite262 = x3d.HAnimSite()
HAnimSite262.name = "l_pinky_distal_tip"
HAnimSite262.DEF = "hanim_l_pinky_distal_tip"
HAnimSite262.translation = [0.2014,0.7009,-0.1012]

HAnimSegment261.children.append(HAnimSite262)

HAnimJoint260.children.append(HAnimSegment261)

HAnimJoint258.children.append(HAnimJoint260)

HAnimJoint256.children.append(HAnimJoint258)

HAnimJoint254.children.append(HAnimJoint256)

HAnimJoint212.children.append(HAnimJoint254)

HAnimJoint206.children.append(HAnimJoint212)

HAnimJoint203.children.append(HAnimJoint206)

HAnimJoint201.children.append(HAnimJoint203)

HAnimJoint195.children.append(HAnimJoint201)

HAnimJoint143.children.append(HAnimJoint195)
HAnimJoint263 = x3d.HAnimJoint()
HAnimJoint263.name = "r_sternoclavicular"
HAnimJoint263.DEF = "hanim_r_sternoclavicular"
HAnimJoint263.center = [-0.082,1.4488,-0.0353]
HAnimJoint263.ulimit = [0,0,0]
HAnimJoint263.llimit = [0,0,0]
HAnimSegment264 = x3d.HAnimSegment()
HAnimSegment264.name = "r_clavicle"
HAnimSegment264.DEF = "hanim_r_clavicle"
HAnimSite265 = x3d.HAnimSite()
HAnimSite265.name = "r_clavicale_pt"
HAnimSite265.DEF = "hanim_r_clavicale_pt"
HAnimSite265.translation = [-0.0115,1.4943,0.04]

HAnimSegment264.children.append(HAnimSite265)
HAnimSite266 = x3d.HAnimSite()
HAnimSite266.name = "r_acromion_pt"
HAnimSite266.DEF = "hanim_r_acromion_pt"
HAnimSite266.translation = [-0.1905,1.4791,-0.0431]

HAnimSegment264.children.append(HAnimSite266)
HAnimSite267 = x3d.HAnimSite()
HAnimSite267.name = "r_axilla_ant_pt"
HAnimSite267.DEF = "hanim_r_axilla_ant_pt"
HAnimSite267.translation = [-0.1626,1.4072,-0.0031]

HAnimSegment264.children.append(HAnimSite267)
HAnimSite268 = x3d.HAnimSite()
HAnimSite268.name = "r_axilla_post_pt"
HAnimSite268.DEF = "hanim_r_axilla_post_pt"
HAnimSite268.translation = [-0.1603,1.4098,-0.0826]

HAnimSegment264.children.append(HAnimSite268)

HAnimJoint263.children.append(HAnimSegment264)
HAnimJoint269 = x3d.HAnimJoint()
HAnimJoint269.name = "r_acromioclavicular"
HAnimJoint269.DEF = "hanim_r_acromioclavicular"
HAnimJoint269.center = [-0.0962,1.4269,-0.0424]
HAnimJoint269.ulimit = [0,0,0]
HAnimJoint269.llimit = [0,0,0]
HAnimSegment270 = x3d.HAnimSegment()
HAnimSegment270.name = "r_scapula"
HAnimSegment270.DEF = "hanim_r_scapula"

HAnimJoint269.children.append(HAnimSegment270)
HAnimJoint271 = x3d.HAnimJoint()
HAnimJoint271.name = "r_shoulder"
HAnimJoint271.DEF = "hanim_r_shoulder"
HAnimJoint271.center = [-0.2029,1.4376,-0.0387]
HAnimJoint271.ulimit = [0,0,0]
HAnimJoint271.llimit = [0,0,0]
HAnimSegment272 = x3d.HAnimSegment()
HAnimSegment272.name = "r_upperarm"
HAnimSegment272.DEF = "hanim_r_upperarm"
HAnimSite273 = x3d.HAnimSite()
HAnimSite273.name = "r_humeral_lateral_epicn_pt"
HAnimSite273.DEF = "hanim_r_humeral_lateral_epicn_pt"
HAnimSite273.translation = [-0.2224,1.1517,-0.1033]

HAnimSegment272.children.append(HAnimSite273)

HAnimJoint271.children.append(HAnimSegment272)
HAnimJoint274 = x3d.HAnimJoint()
HAnimJoint274.name = "r_elbow"
HAnimJoint274.DEF = "hanim_r_elbow"
HAnimJoint274.center = [-0.2014,1.1357,-0.0682]
HAnimJoint274.ulimit = [0,0,0]
HAnimJoint274.llimit = [0,0,0]
HAnimSegment275 = x3d.HAnimSegment()
HAnimSegment275.name = "r_forearm"
HAnimSegment275.DEF = "hanim_r_forearm"
HAnimSite276 = x3d.HAnimSite()
HAnimSite276.name = "r_radial_styloid_pt"
HAnimSite276.DEF = "hanim_r_radial_styloid_pt"
HAnimSite276.translation = [-0.1884,0.8676,-0.036]

HAnimSegment275.children.append(HAnimSite276)
HAnimSite277 = x3d.HAnimSite()
HAnimSite277.name = "r_olecranon_pt"
HAnimSite277.DEF = "hanim_r_olecranon_pt"
HAnimSite277.translation = [-0.1907,1.1405,-0.1065]

HAnimSegment275.children.append(HAnimSite277)
HAnimSite278 = x3d.HAnimSite()
HAnimSite278.name = "r_humeral_medial_epicn_pt"
HAnimSite278.DEF = "hanim_r_humeral_medial_epicn_pt"
HAnimSite278.translation = [-0.168,1.1298,-0.1062]

HAnimSegment275.children.append(HAnimSite278)
HAnimSite279 = x3d.HAnimSite()
HAnimSite279.name = "r_radiale_pt"
HAnimSite279.DEF = "hanim_r_radiale_pt"
HAnimSite279.translation = [-0.213,1.1305,-0.1091]

HAnimSegment275.children.append(HAnimSite279)

HAnimJoint274.children.append(HAnimSegment275)
HAnimJoint280 = x3d.HAnimJoint()
HAnimJoint280.name = "r_wrist"
HAnimJoint280.DEF = "hanim_r_wrist"
HAnimJoint280.center = [-0.1984,0.8663,-0.0583]
HAnimJoint280.ulimit = [0,0,0]
HAnimJoint280.llimit = [0,0,0]
HAnimSegment281 = x3d.HAnimSegment()
HAnimSegment281.name = "r_hand"
HAnimSegment281.DEF = "hanim_r_hand"
HAnimSite282 = x3d.HAnimSite()
HAnimSite282.name = "r_metacarpal_pha2_pt"
HAnimSite282.DEF = "hanim_r_metacarpal_pha2_pt"
HAnimSite282.translation = [-0.1977,0.8169,-0.0177]

HAnimSegment281.children.append(HAnimSite282)
HAnimSite283 = x3d.HAnimSite()
HAnimSite283.name = "r_ulnar_styloid_pt"
HAnimSite283.DEF = "hanim_r_ulnar_styloid_pt"
HAnimSite283.translation = [-0.2117,0.8562,-0.0584]

HAnimSegment281.children.append(HAnimSite283)
HAnimSite284 = x3d.HAnimSite()
HAnimSite284.name = "r_metacarpal_pha5_pt"
HAnimSite284.DEF = "hanim_r_metacarpal_pha5_pt"
HAnimSite284.translation = [-0.1929,0.789,-0.1064]

HAnimSegment281.children.append(HAnimSite284)
HAnimSite285 = x3d.HAnimSite()
HAnimSite285.name = "r_hand_front_view"
HAnimSite285.DEF = "hanim_r_hand_front_view"
HAnimSite285.translation = [-0.3,0.75,0.45]
Viewpoint286 = x3d.Viewpoint()
Viewpoint286.DEF = "hanim_r_hand_front_viewpoint"
Viewpoint286.centerOfRotation = [0,0.7,0]
Viewpoint286.description = "right hand front"
Viewpoint286.position = [0,0,0]

HAnimSite285.children.append(Viewpoint286)

HAnimSegment281.children.append(HAnimSite285)

HAnimJoint280.children.append(HAnimSegment281)
HAnimJoint287 = x3d.HAnimJoint()
HAnimJoint287.name = "r_thumb1"
HAnimJoint287.DEF = "hanim_r_thumb1"
HAnimJoint287.center = [-0.1924,0.8472,-0.0534]
HAnimJoint287.ulimit = [0,0,0]
HAnimJoint287.llimit = [0,0,0]
HAnimSegment288 = x3d.HAnimSegment()
HAnimSegment288.name = "r_thumb_metacarpal"
HAnimSegment288.DEF = "hanim_r_thumb_metacarpal"

HAnimJoint287.children.append(HAnimSegment288)
HAnimJoint289 = x3d.HAnimJoint()
HAnimJoint289.name = "r_thumb2"
HAnimJoint289.DEF = "hanim_r_thumb2"
HAnimJoint289.center = [-0.1951,0.8226,0.0246]
HAnimJoint289.ulimit = [0,0,0]
HAnimJoint289.llimit = [0,0,0]
HAnimSegment290 = x3d.HAnimSegment()
HAnimSegment290.name = "r_thumb_proximal"
HAnimSegment290.DEF = "hanim_r_thumb_proximal"

HAnimJoint289.children.append(HAnimSegment290)
HAnimJoint291 = x3d.HAnimJoint()
HAnimJoint291.name = "r_thumb3"
HAnimJoint291.DEF = "hanim_r_thumb3"
HAnimJoint291.center = [-0.1955,0.8159,0.0464]
HAnimJoint291.ulimit = [0,0,0]
HAnimJoint291.llimit = [0,0,0]
HAnimSegment292 = x3d.HAnimSegment()
HAnimSegment292.name = "r_thumb_distal"
HAnimSegment292.DEF = "hanim_r_thumb_distal"
HAnimSite293 = x3d.HAnimSite()
HAnimSite293.name = "r_thumb_distal_tip"
HAnimSite293.DEF = "hanim_r_thumb_distal_tip"
HAnimSite293.translation = [-0.1869,0.809,0.082]

HAnimSegment292.children.append(HAnimSite293)

HAnimJoint291.children.append(HAnimSegment292)

HAnimJoint289.children.append(HAnimJoint291)

HAnimJoint287.children.append(HAnimJoint289)

HAnimJoint280.children.append(HAnimJoint287)
HAnimJoint294 = x3d.HAnimJoint()
HAnimJoint294.name = "r_index0"
HAnimJoint294.DEF = "hanim_r_index0"
HAnimJoint294.center = [-0.1983,0.8024,-0.028]
HAnimJoint294.ulimit = [0,0,0]
HAnimJoint294.llimit = [0,0,0]
HAnimSegment295 = x3d.HAnimSegment()
HAnimSegment295.name = "r_index_metacarpal"
HAnimSegment295.DEF = "hanim_r_index_metacarpal"

HAnimJoint294.children.append(HAnimSegment295)
HAnimJoint296 = x3d.HAnimJoint()
HAnimJoint296.name = "r_index1"
HAnimJoint296.DEF = "hanim_r_index1"
HAnimJoint296.center = [-0.1983,0.7815,-0.028]
HAnimJoint296.ulimit = [0,0,0]
HAnimJoint296.llimit = [0,0,0]
HAnimSegment297 = x3d.HAnimSegment()
HAnimSegment297.name = "r_index_proximal"
HAnimSegment297.DEF = "hanim_r_index_proximal"

HAnimJoint296.children.append(HAnimSegment297)
HAnimJoint298 = x3d.HAnimJoint()
HAnimJoint298.name = "r_index2"
HAnimJoint298.DEF = "hanim_r_index2"
HAnimJoint298.center = [-0.2017,0.7363,-0.0248]
HAnimJoint298.ulimit = [0,0,0]
HAnimJoint298.llimit = [0,0,0]
HAnimSegment299 = x3d.HAnimSegment()
HAnimSegment299.name = "r_index_middle"
HAnimSegment299.DEF = "hanim_r_index_middle"

HAnimJoint298.children.append(HAnimSegment299)
HAnimJoint300 = x3d.HAnimJoint()
HAnimJoint300.name = "r_index3"
HAnimJoint300.DEF = "hanim_r_index3"
HAnimJoint300.center = [-0.2028,0.7139,-0.0236]
HAnimJoint300.ulimit = [0,0,0]
HAnimJoint300.llimit = [0,0,0]
HAnimSegment301 = x3d.HAnimSegment()
HAnimSegment301.name = "r_index_distal"
HAnimSegment301.DEF = "hanim_r_index_distal"
HAnimSite302 = x3d.HAnimSite()
HAnimSite302.name = "r_index_distal_tip"
HAnimSite302.DEF = "hanim_r_index_distal_tip"
HAnimSite302.translation = [-0.198,0.6883,-0.018]

HAnimSegment301.children.append(HAnimSite302)
HAnimSite303 = x3d.HAnimSite()
HAnimSite303.name = "r_dactylion_pt"
HAnimSite303.DEF = "hanim_r_dactylion_pt"
HAnimSite303.translation = [-0.1941,0.6772,-0.0423]

HAnimSegment301.children.append(HAnimSite303)

HAnimJoint300.children.append(HAnimSegment301)

HAnimJoint298.children.append(HAnimJoint300)

HAnimJoint296.children.append(HAnimJoint298)

HAnimJoint294.children.append(HAnimJoint296)

HAnimJoint280.children.append(HAnimJoint294)
HAnimJoint304 = x3d.HAnimJoint()
HAnimJoint304.name = "r_middle0"
HAnimJoint304.DEF = "hanim_r_middle0"
HAnimJoint304.center = [-0.1987,0.8029,-0.053]
HAnimJoint304.ulimit = [0,0,0]
HAnimJoint304.llimit = [0,0,0]
HAnimSegment305 = x3d.HAnimSegment()
HAnimSegment305.name = "r_middle_metacarpal"
HAnimSegment305.DEF = "hanim_r_middle_metacarpal"

HAnimJoint304.children.append(HAnimSegment305)
HAnimJoint306 = x3d.HAnimJoint()
HAnimJoint306.name = "r_middle1"
HAnimJoint306.DEF = "hanim_r_middle1"
HAnimJoint306.center = [-0.1987,0.7818,-0.053]
HAnimJoint306.ulimit = [0,0,0]
HAnimJoint306.llimit = [0,0,0]
HAnimSegment307 = x3d.HAnimSegment()
HAnimSegment307.name = "r_middle_proximal"
HAnimSegment307.DEF = "hanim_r_middle_proximal"

HAnimJoint306.children.append(HAnimSegment307)
HAnimJoint308 = x3d.HAnimJoint()
HAnimJoint308.name = "r_middle2"
HAnimJoint308.DEF = "hanim_r_middle2"
HAnimJoint308.center = [-0.2013,0.7273,-0.0503]
HAnimJoint308.ulimit = [0,0,0]
HAnimJoint308.llimit = [0,0,0]
HAnimSegment309 = x3d.HAnimSegment()
HAnimSegment309.name = "r_middle_middle"
HAnimSegment309.DEF = "hanim_r_middle_middle"

HAnimJoint308.children.append(HAnimSegment309)
HAnimJoint310 = x3d.HAnimJoint()
HAnimJoint310.name = "r_middle3"
HAnimJoint310.DEF = "hanim_r_middle3"
HAnimJoint310.center = [-0.2026,0.7011,-0.0494]
HAnimJoint310.ulimit = [0,0,0]
HAnimJoint310.llimit = [0,0,0]
HAnimSegment311 = x3d.HAnimSegment()
HAnimSegment311.name = "r_middle_distal"
HAnimSegment311.DEF = "hanim_r_middle_distal"
HAnimSite312 = x3d.HAnimSite()
HAnimSite312.name = "r_middle_distal_tip"
HAnimSite312.DEF = "hanim_r_middle_distal_tip"
HAnimSite312.translation = [-0.1969,0.6758,-0.0427]

HAnimSegment311.children.append(HAnimSite312)

HAnimJoint310.children.append(HAnimSegment311)

HAnimJoint308.children.append(HAnimJoint310)

HAnimJoint306.children.append(HAnimJoint308)

HAnimJoint304.children.append(HAnimJoint306)

HAnimJoint280.children.append(HAnimJoint304)
HAnimJoint313 = x3d.HAnimJoint()
HAnimJoint313.name = "r_ring0"
HAnimJoint313.DEF = "hanim_r_ring0"
HAnimJoint313.center = [-0.1956,0.8019,-0.0794]
HAnimJoint313.ulimit = [0,0,0]
HAnimJoint313.llimit = [0,0,0]
HAnimSegment314 = x3d.HAnimSegment()
HAnimSegment314.name = "r_ring_metacarpal"
HAnimSegment314.DEF = "hanim_r_ring_metacarpal"

HAnimJoint313.children.append(HAnimSegment314)
HAnimJoint315 = x3d.HAnimJoint()
HAnimJoint315.name = "r_ring1"
HAnimJoint315.DEF = "hanim_r_ring1"
HAnimJoint315.center = [-0.1956,0.7815,-0.0794]
HAnimJoint315.ulimit = [0,0,0]
HAnimJoint315.llimit = [0,0,0]
HAnimSegment316 = x3d.HAnimSegment()
HAnimSegment316.name = "r_ring_proximal"
HAnimSegment316.DEF = "hanim_r_ring_proximal"

HAnimJoint315.children.append(HAnimSegment316)
HAnimJoint317 = x3d.HAnimJoint()
HAnimJoint317.name = "r_ring2"
HAnimJoint317.DEF = "hanim_r_ring2"
HAnimJoint317.center = [-0.1973,0.7287,-0.0777]
HAnimJoint317.ulimit = [0,0,0]
HAnimJoint317.llimit = [0,0,0]
HAnimSegment318 = x3d.HAnimSegment()
HAnimSegment318.name = "r_ring_middle"
HAnimSegment318.DEF = "hanim_r_ring_middle"

HAnimJoint317.children.append(HAnimSegment318)
HAnimJoint319 = x3d.HAnimJoint()
HAnimJoint319.name = "r_ring3"
HAnimJoint319.DEF = "hanim_r_ring3"
HAnimJoint319.center = [-0.1983,0.7045,-0.0767]
HAnimJoint319.ulimit = [0,0,0]
HAnimJoint319.llimit = [0,0,0]
HAnimSegment320 = x3d.HAnimSegment()
HAnimSegment320.name = "r_ring_distal"
HAnimSegment320.DEF = "hanim_r_ring_distal"
HAnimSite321 = x3d.HAnimSite()
HAnimSite321.name = "r_ring_distal_tip"
HAnimSite321.DEF = "hanim_r_ring_distal_tip"
HAnimSite321.translation = [-0.1934,0.6778,-0.0693]

HAnimSegment320.children.append(HAnimSite321)

HAnimJoint319.children.append(HAnimSegment320)

HAnimJoint317.children.append(HAnimJoint319)

HAnimJoint315.children.append(HAnimJoint317)

HAnimJoint313.children.append(HAnimJoint315)

HAnimJoint280.children.append(HAnimJoint313)
HAnimJoint322 = x3d.HAnimJoint()
HAnimJoint322.name = "r_pinky0"
HAnimJoint322.DEF = "hanim_r_pinky0"
HAnimJoint322.center = [-0.1925,0.8066,-0.1036]
HAnimJoint322.ulimit = [0,0,0]
HAnimJoint322.llimit = [0,0,0]
HAnimSegment323 = x3d.HAnimSegment()
HAnimSegment323.name = "r_pinky_metacarpal"
HAnimSegment323.DEF = "hanim_r_pinky_metacarpal"

HAnimJoint322.children.append(HAnimSegment323)
HAnimJoint324 = x3d.HAnimJoint()
HAnimJoint324.name = "r_pinky1"
HAnimJoint324.DEF = "hanim_r_pinky1"
HAnimJoint324.center = [-0.1925,0.7866,-0.1036]
HAnimJoint324.ulimit = [0,0,0]
HAnimJoint324.llimit = [0,0,0]
HAnimSegment325 = x3d.HAnimSegment()
HAnimSegment325.name = "r_pinky_proximal"
HAnimSegment325.DEF = "hanim_r_pinky_proximal"

HAnimJoint324.children.append(HAnimSegment325)
HAnimJoint326 = x3d.HAnimJoint()
HAnimJoint326.name = "r_pinky2"
HAnimJoint326.DEF = "hanim_r_pinky2"
HAnimJoint326.center = [-0.1938,0.7452,-0.1024]
HAnimJoint326.ulimit = [0,0,0]
HAnimJoint326.llimit = [0,0,0]
HAnimSegment327 = x3d.HAnimSegment()
HAnimSegment327.name = "r_pinky_middle"
HAnimSegment327.DEF = "hanim_r_pinky_middle"

HAnimJoint326.children.append(HAnimSegment327)
HAnimJoint328 = x3d.HAnimJoint()
HAnimJoint328.name = "r_pinky3"
HAnimJoint328.DEF = "hanim_r_pinky3"
HAnimJoint328.center = [-0.1948,0.7277,-0.1017]
HAnimJoint328.ulimit = [0,0,0]
HAnimJoint328.llimit = [0,0,0]
HAnimSegment329 = x3d.HAnimSegment()
HAnimSegment329.name = "r_pinky_distal"
HAnimSegment329.DEF = "hanim_r_pinky_distal"
HAnimSite330 = x3d.HAnimSite()
HAnimSite330.name = "r_pinky_distal_tip"
HAnimSite330.DEF = "hanim_r_pinky_distal_tip"
HAnimSite330.translation = [-0.1938,0.7035,-0.0949]

HAnimSegment329.children.append(HAnimSite330)

HAnimJoint328.children.append(HAnimSegment329)

HAnimJoint326.children.append(HAnimJoint328)

HAnimJoint324.children.append(HAnimJoint326)

HAnimJoint322.children.append(HAnimJoint324)

HAnimJoint280.children.append(HAnimJoint322)

HAnimJoint274.children.append(HAnimJoint280)

HAnimJoint271.children.append(HAnimJoint274)

HAnimJoint269.children.append(HAnimJoint271)

HAnimJoint263.children.append(HAnimJoint269)

HAnimJoint143.children.append(HAnimJoint263)

HAnimJoint141.children.append(HAnimJoint143)

HAnimJoint139.children.append(HAnimJoint141)

HAnimJoint137.children.append(HAnimJoint139)

HAnimJoint135.children.append(HAnimJoint137)

HAnimJoint133.children.append(HAnimJoint135)

HAnimJoint131.children.append(HAnimJoint133)

HAnimJoint129.children.append(HAnimJoint131)

HAnimJoint125.children.append(HAnimJoint129)

HAnimJoint122.children.append(HAnimJoint125)

HAnimJoint120.children.append(HAnimJoint122)

HAnimJoint118.children.append(HAnimJoint120)

HAnimJoint116.children.append(HAnimJoint118)

HAnimJoint111.children.append(HAnimJoint116)

HAnimJoint109.children.append(HAnimJoint111)

HAnimJoint107.children.append(HAnimJoint109)

HAnimJoint103.children.append(HAnimJoint107)

HAnimJoint44.children.append(HAnimJoint103)

HAnimHumanoid43.skeleton.append(HAnimJoint44)
HAnimSite331 = x3d.HAnimSite()
HAnimSite331.name = "l_inclined_view"
HAnimSite331.DEF = "hanim_l_inclined_view"
HAnimSite331.rotation = [-0.113,0.993,0.0347,0.671]
HAnimSite331.translation = [1.62,1.05,2.06]
Viewpoint332 = x3d.Viewpoint()
Viewpoint332.DEF = "hanim_l_inclined_viewpoint"
Viewpoint332.description = "left inclined"
Viewpoint332.position = [0,0,0]

HAnimSite331.children.append(Viewpoint332)

HAnimHumanoid43.viewpoints.append(HAnimSite331)
HAnimSite333 = x3d.HAnimSite()
HAnimSite333.name = "r_inclined_view"
HAnimSite333.DEF = "hanim_r_inclined_view"
HAnimSite333.rotation = [-0.113,-0.993,0.0347,0.671]
HAnimSite333.translation = [-1.62,1.05,2.06]
Viewpoint334 = x3d.Viewpoint()
Viewpoint334.DEF = "hanim_r_inclined_viewpoint"
Viewpoint334.centerOfRotation = [0,0.9,0]
Viewpoint334.description = "right inclined"
Viewpoint334.position = [0,0,0]

HAnimSite333.children.append(Viewpoint334)

HAnimHumanoid43.viewpoints.append(HAnimSite333)
HAnimSite335 = x3d.HAnimSite()
HAnimSite335.name = "front_view"
HAnimSite335.DEF = "hanim_front_view"
HAnimSite335.translation = [0,0.85,2.58]
Viewpoint336 = x3d.Viewpoint()
Viewpoint336.DEF = "hanim_front_viewpoint"
Viewpoint336.centerOfRotation = [0,0.9,0]
Viewpoint336.description = "front"
Viewpoint336.position = [0,0,0]

HAnimSite335.children.append(Viewpoint336)

HAnimHumanoid43.viewpoints.append(HAnimSite335)
HAnimSite337 = x3d.HAnimSite()
HAnimSite337.name = "back_view"
HAnimSite337.DEF = "hanim_back_view"
HAnimSite337.rotation = [0,1,0,3.14]
HAnimSite337.translation = [0,0.85,-2.58]
Viewpoint338 = x3d.Viewpoint()
Viewpoint338.DEF = "hanim_back_viewpoint"
Viewpoint338.centerOfRotation = [0,0.9,0]
Viewpoint338.description = "back"
Viewpoint338.position = [0,0,0]

HAnimSite337.children.append(Viewpoint338)

HAnimHumanoid43.viewpoints.append(HAnimSite337)
HAnimSite339 = x3d.HAnimSite()
HAnimSite339.name = "l_side_view"
HAnimSite339.DEF = "hanim_l_side_view"
HAnimSite339.rotation = [0,1,0,1.5708]
HAnimSite339.translation = [2.6,0.854,0]
Viewpoint340 = x3d.Viewpoint()
Viewpoint340.DEF = "hanim_l_side_viewpoint"
Viewpoint340.centerOfRotation = [0,0.9,0]
Viewpoint340.description = "left side"
Viewpoint340.position = [0,0,0]

HAnimSite339.children.append(Viewpoint340)

HAnimHumanoid43.viewpoints.append(HAnimSite339)
HAnimSite341 = x3d.HAnimSite()
HAnimSite341.name = "Top_view"
HAnimSite341.DEF = "hanim_Top_view"
HAnimSite341.rotation = [1,0,0,-1.57]
HAnimSite341.translation = [0,3.5,0]
Viewpoint342 = x3d.Viewpoint()
Viewpoint342.DEF = "hanim_Top_viewpoint"
Viewpoint342.centerOfRotation = [0,0.9,0]
Viewpoint342.description = "Top"
Viewpoint342.position = [0,0,0]

HAnimSite341.children.append(Viewpoint342)

HAnimHumanoid43.viewpoints.append(HAnimSite341)
HAnimSite343 = x3d.HAnimSite()
HAnimSite343.name = "front_close_view"
HAnimSite343.DEF = "hanim_front_close_view"
HAnimSite343.translation = [0,0.854,1.575]
Viewpoint344 = x3d.Viewpoint()
Viewpoint344.DEF = "hanim_front_close_viewpoint"
Viewpoint344.centerOfRotation = [0,0,1.575]
Viewpoint344.description = "front close"
Viewpoint344.position = [0,0,0]

HAnimSite343.children.append(Viewpoint344)

HAnimHumanoid43.viewpoints.append(HAnimSite343)
HAnimSite345 = x3d.HAnimSite()
HAnimSite345.name = "side_close_view"
HAnimSite345.DEF = "hanim_side_close_view"
HAnimSite345.rotation = [0,1,0,1.5708]
HAnimSite345.translation = [1.56,0.854,0]
Viewpoint346 = x3d.Viewpoint()
Viewpoint346.DEF = "hanim_side_close_viewpoint"
Viewpoint346.centerOfRotation = [1.6,0,0]
Viewpoint346.description = "side close"
Viewpoint346.position = [0,0,0]

HAnimSite345.children.append(Viewpoint346)

HAnimHumanoid43.viewpoints.append(HAnimSite345)
HAnimSite347 = x3d.HAnimSite()
HAnimSite347.name = "head_front_close_view"
HAnimSite347.DEF = "hanim_head_front_close_view"
HAnimSite347.translation = [0,1.5,1]
Viewpoint348 = x3d.Viewpoint()
Viewpoint348.DEF = "hanim_head_front_close_viewpoint"
Viewpoint348.centerOfRotation = [0,0,1]
Viewpoint348.description = "head front close"
Viewpoint348.position = [0,0,0]

HAnimSite347.children.append(Viewpoint348)

HAnimHumanoid43.viewpoints.append(HAnimSite347)
HAnimSite349 = x3d.HAnimSite()
HAnimSite349.name = "chest_front_close_view"
HAnimSite349.DEF = "hanim_chest_front_close_view"
HAnimSite349.translation = [0,1.2,1]
Viewpoint350 = x3d.Viewpoint()
Viewpoint350.DEF = "hanim_chest_front_close_viewpoint"
Viewpoint350.centerOfRotation = [0,0,1]
Viewpoint350.description = "chest front close"
Viewpoint350.position = [0,0,0]

HAnimSite349.children.append(Viewpoint350)

HAnimHumanoid43.viewpoints.append(HAnimSite349)
HAnimSite351 = x3d.HAnimSite()
HAnimSite351.name = "pelvis_front_close_view"
HAnimSite351.DEF = "hanim_pelvis_front_close_view"
HAnimSite351.translation = [0,0.8,1]
Viewpoint352 = x3d.Viewpoint()
Viewpoint352.DEF = "hanim_pelvis_front_close_viewpoint"
Viewpoint352.centerOfRotation = [0,0,1]
Viewpoint352.description = "pelvis front close"
Viewpoint352.position = [0,0,0]

HAnimSite351.children.append(Viewpoint352)

HAnimHumanoid43.viewpoints.append(HAnimSite351)
HAnimSite353 = x3d.HAnimSite()
HAnimSite353.name = "knees_front_close_view"
HAnimSite353.DEF = "hanim_knees_front_close_view"
HAnimSite353.translation = [0,0.4,1]
Viewpoint354 = x3d.Viewpoint()
Viewpoint354.DEF = "hanim_knees_front_close_viewpoint"
Viewpoint354.centerOfRotation = [0,0.4,0]
Viewpoint354.description = "knees front close"
Viewpoint354.position = [0,0,0]

HAnimSite353.children.append(Viewpoint354)

HAnimHumanoid43.viewpoints.append(HAnimSite353)
HAnimSite355 = x3d.HAnimSite()
HAnimSite355.name = "feet_front_close_view"
HAnimSite355.DEF = "hanim_feet_front_close_view"
HAnimSite355.translation = [0,0,1]
Viewpoint356 = x3d.Viewpoint()
Viewpoint356.DEF = "hanim_feet_front_close_viewpoint"
Viewpoint356.description = "feet front close"
Viewpoint356.position = [0,0,0]

HAnimSite355.children.append(Viewpoint356)

HAnimHumanoid43.viewpoints.append(HAnimSite355)
HAnimSite357 = x3d.HAnimSite()
HAnimSite357.name = "eye_level_view"
HAnimSite357.DEF = "hanim_eye_level_view"
HAnimSite357.translation = [0,1.6332,0.0502]
Viewpoint358 = x3d.Viewpoint()
Viewpoint358.DEF = "hanim_eye_level_viewpoint"
Viewpoint358.description = "eye level looking forward"
Viewpoint358.orientation = [0,1,0,3.141593]
Viewpoint358.position = [0,0,0]

HAnimSite357.children.append(Viewpoint358)

HAnimHumanoid43.viewpoints.append(HAnimSite357)
HAnimSite359 = x3d.HAnimSite()
HAnimSite359.USE = "hanim_l_eyeball_site_view"

HAnimHumanoid43.sites.append(HAnimSite359)
HAnimSite360 = x3d.HAnimSite()
HAnimSite360.USE = "hanim_r_eyeball_site_view"

HAnimHumanoid43.sites.append(HAnimSite360)
HAnimSite361 = x3d.HAnimSite()
HAnimSite361.USE = "hanim_l_hand_front_view"

HAnimHumanoid43.sites.append(HAnimSite361)
HAnimSite362 = x3d.HAnimSite()
HAnimSite362.USE = "hanim_r_hand_front_view"

HAnimHumanoid43.sites.append(HAnimSite362)
HAnimJoint363 = x3d.HAnimJoint()
HAnimJoint363.USE = "hanim_humanoid_root"

HAnimHumanoid43.joints.append(HAnimJoint363)
HAnimJoint364 = x3d.HAnimJoint()
HAnimJoint364.USE = "hanim_sacroiliac"

HAnimHumanoid43.joints.append(HAnimJoint364)
HAnimJoint365 = x3d.HAnimJoint()
HAnimJoint365.USE = "hanim_vl5"

HAnimHumanoid43.joints.append(HAnimJoint365)
HAnimJoint366 = x3d.HAnimJoint()
HAnimJoint366.USE = "hanim_vl4"

HAnimHumanoid43.joints.append(HAnimJoint366)
HAnimJoint367 = x3d.HAnimJoint()
HAnimJoint367.USE = "hanim_vl3"

HAnimHumanoid43.joints.append(HAnimJoint367)
HAnimJoint368 = x3d.HAnimJoint()
HAnimJoint368.USE = "hanim_vl2"

HAnimHumanoid43.joints.append(HAnimJoint368)
HAnimJoint369 = x3d.HAnimJoint()
HAnimJoint369.USE = "hanim_vl1"

HAnimHumanoid43.joints.append(HAnimJoint369)
HAnimJoint370 = x3d.HAnimJoint()
HAnimJoint370.USE = "hanim_vt12"

HAnimHumanoid43.joints.append(HAnimJoint370)
HAnimJoint371 = x3d.HAnimJoint()
HAnimJoint371.USE = "hanim_vt11"

HAnimHumanoid43.joints.append(HAnimJoint371)
HAnimJoint372 = x3d.HAnimJoint()
HAnimJoint372.USE = "hanim_vt10"

HAnimHumanoid43.joints.append(HAnimJoint372)
HAnimJoint373 = x3d.HAnimJoint()
HAnimJoint373.USE = "hanim_vt9"

HAnimHumanoid43.joints.append(HAnimJoint373)
HAnimJoint374 = x3d.HAnimJoint()
HAnimJoint374.USE = "hanim_vt8"

HAnimHumanoid43.joints.append(HAnimJoint374)
HAnimJoint375 = x3d.HAnimJoint()
HAnimJoint375.USE = "hanim_vt7"

HAnimHumanoid43.joints.append(HAnimJoint375)
HAnimJoint376 = x3d.HAnimJoint()
HAnimJoint376.USE = "hanim_vt6"

HAnimHumanoid43.joints.append(HAnimJoint376)
HAnimJoint377 = x3d.HAnimJoint()
HAnimJoint377.USE = "hanim_vt5"

HAnimHumanoid43.joints.append(HAnimJoint377)
HAnimJoint378 = x3d.HAnimJoint()
HAnimJoint378.USE = "hanim_vt4"

HAnimHumanoid43.joints.append(HAnimJoint378)
HAnimJoint379 = x3d.HAnimJoint()
HAnimJoint379.USE = "hanim_vt3"

HAnimHumanoid43.joints.append(HAnimJoint379)
HAnimJoint380 = x3d.HAnimJoint()
HAnimJoint380.USE = "hanim_vt2"

HAnimHumanoid43.joints.append(HAnimJoint380)
HAnimJoint381 = x3d.HAnimJoint()
HAnimJoint381.USE = "hanim_vt1"

HAnimHumanoid43.joints.append(HAnimJoint381)
HAnimJoint382 = x3d.HAnimJoint()
HAnimJoint382.USE = "hanim_vc7"

HAnimHumanoid43.joints.append(HAnimJoint382)
HAnimJoint383 = x3d.HAnimJoint()
HAnimJoint383.USE = "hanim_vc6"

HAnimHumanoid43.joints.append(HAnimJoint383)
HAnimJoint384 = x3d.HAnimJoint()
HAnimJoint384.USE = "hanim_vc5"

HAnimHumanoid43.joints.append(HAnimJoint384)
HAnimJoint385 = x3d.HAnimJoint()
HAnimJoint385.USE = "hanim_vc4"

HAnimHumanoid43.joints.append(HAnimJoint385)
HAnimJoint386 = x3d.HAnimJoint()
HAnimJoint386.USE = "hanim_vc3"

HAnimHumanoid43.joints.append(HAnimJoint386)
HAnimJoint387 = x3d.HAnimJoint()
HAnimJoint387.USE = "hanim_vc2"

HAnimHumanoid43.joints.append(HAnimJoint387)
HAnimJoint388 = x3d.HAnimJoint()
HAnimJoint388.USE = "hanim_vc1"

HAnimHumanoid43.joints.append(HAnimJoint388)
HAnimJoint389 = x3d.HAnimJoint()
HAnimJoint389.USE = "hanim_skullbase"

HAnimHumanoid43.joints.append(HAnimJoint389)
HAnimJoint390 = x3d.HAnimJoint()
HAnimJoint390.USE = "hanim_temporomandibular"

HAnimHumanoid43.joints.append(HAnimJoint390)
HAnimJoint391 = x3d.HAnimJoint()
HAnimJoint391.USE = "hanim_l_acromioclavicular"

HAnimHumanoid43.joints.append(HAnimJoint391)
HAnimJoint392 = x3d.HAnimJoint()
HAnimJoint392.USE = "hanim_r_acromioclavicular"

HAnimHumanoid43.joints.append(HAnimJoint392)
HAnimJoint393 = x3d.HAnimJoint()
HAnimJoint393.USE = "hanim_l_ankle"

HAnimHumanoid43.joints.append(HAnimJoint393)
HAnimJoint394 = x3d.HAnimJoint()
HAnimJoint394.USE = "hanim_r_ankle"

HAnimHumanoid43.joints.append(HAnimJoint394)
HAnimJoint395 = x3d.HAnimJoint()
HAnimJoint395.USE = "hanim_l_elbow"

HAnimHumanoid43.joints.append(HAnimJoint395)
HAnimJoint396 = x3d.HAnimJoint()
HAnimJoint396.USE = "hanim_r_elbow"

HAnimHumanoid43.joints.append(HAnimJoint396)
HAnimJoint397 = x3d.HAnimJoint()
HAnimJoint397.USE = "hanim_l_eyeball_joint"

HAnimHumanoid43.joints.append(HAnimJoint397)
HAnimJoint398 = x3d.HAnimJoint()
HAnimJoint398.USE = "hanim_r_eyeball_joint"

HAnimHumanoid43.joints.append(HAnimJoint398)
HAnimJoint399 = x3d.HAnimJoint()
HAnimJoint399.USE = "hanim_l_eyebrow_joint"

HAnimHumanoid43.joints.append(HAnimJoint399)
HAnimJoint400 = x3d.HAnimJoint()
HAnimJoint400.USE = "hanim_r_eyebrow_joint"

HAnimHumanoid43.joints.append(HAnimJoint400)
HAnimJoint401 = x3d.HAnimJoint()
HAnimJoint401.USE = "hanim_l_eyelid_joint"

HAnimHumanoid43.joints.append(HAnimJoint401)
HAnimJoint402 = x3d.HAnimJoint()
HAnimJoint402.USE = "hanim_r_eyelid_joint"

HAnimHumanoid43.joints.append(HAnimJoint402)
HAnimJoint403 = x3d.HAnimJoint()
HAnimJoint403.USE = "hanim_l_hip"

HAnimHumanoid43.joints.append(HAnimJoint403)
HAnimJoint404 = x3d.HAnimJoint()
HAnimJoint404.USE = "hanim_r_hip"

HAnimHumanoid43.joints.append(HAnimJoint404)
HAnimJoint405 = x3d.HAnimJoint()
HAnimJoint405.USE = "hanim_l_index0"

HAnimHumanoid43.joints.append(HAnimJoint405)
HAnimJoint406 = x3d.HAnimJoint()
HAnimJoint406.USE = "hanim_r_index0"

HAnimHumanoid43.joints.append(HAnimJoint406)
HAnimJoint407 = x3d.HAnimJoint()
HAnimJoint407.USE = "hanim_l_index1"

HAnimHumanoid43.joints.append(HAnimJoint407)
HAnimJoint408 = x3d.HAnimJoint()
HAnimJoint408.USE = "hanim_r_index1"

HAnimHumanoid43.joints.append(HAnimJoint408)
HAnimJoint409 = x3d.HAnimJoint()
HAnimJoint409.USE = "hanim_l_index2"

HAnimHumanoid43.joints.append(HAnimJoint409)
HAnimJoint410 = x3d.HAnimJoint()
HAnimJoint410.USE = "hanim_r_index2"

HAnimHumanoid43.joints.append(HAnimJoint410)
HAnimJoint411 = x3d.HAnimJoint()
HAnimJoint411.USE = "hanim_l_index3"

HAnimHumanoid43.joints.append(HAnimJoint411)
HAnimJoint412 = x3d.HAnimJoint()
HAnimJoint412.USE = "hanim_r_index3"

HAnimHumanoid43.joints.append(HAnimJoint412)
HAnimJoint413 = x3d.HAnimJoint()
HAnimJoint413.USE = "hanim_l_knee"

HAnimHumanoid43.joints.append(HAnimJoint413)
HAnimJoint414 = x3d.HAnimJoint()
HAnimJoint414.USE = "hanim_r_knee"

HAnimHumanoid43.joints.append(HAnimJoint414)
HAnimJoint415 = x3d.HAnimJoint()
HAnimJoint415.USE = "hanim_l_metatarsal"

HAnimHumanoid43.joints.append(HAnimJoint415)
HAnimJoint416 = x3d.HAnimJoint()
HAnimJoint416.USE = "hanim_r_metatarsal"

HAnimHumanoid43.joints.append(HAnimJoint416)
HAnimJoint417 = x3d.HAnimJoint()
HAnimJoint417.USE = "hanim_l_middle0"

HAnimHumanoid43.joints.append(HAnimJoint417)
HAnimJoint418 = x3d.HAnimJoint()
HAnimJoint418.USE = "hanim_r_middle0"

HAnimHumanoid43.joints.append(HAnimJoint418)
HAnimJoint419 = x3d.HAnimJoint()
HAnimJoint419.USE = "hanim_l_middle1"

HAnimHumanoid43.joints.append(HAnimJoint419)
HAnimJoint420 = x3d.HAnimJoint()
HAnimJoint420.USE = "hanim_r_middle1"

HAnimHumanoid43.joints.append(HAnimJoint420)
HAnimJoint421 = x3d.HAnimJoint()
HAnimJoint421.USE = "hanim_l_middle2"

HAnimHumanoid43.joints.append(HAnimJoint421)
HAnimJoint422 = x3d.HAnimJoint()
HAnimJoint422.USE = "hanim_r_middle2"

HAnimHumanoid43.joints.append(HAnimJoint422)
HAnimJoint423 = x3d.HAnimJoint()
HAnimJoint423.USE = "hanim_l_middle3"

HAnimHumanoid43.joints.append(HAnimJoint423)
HAnimJoint424 = x3d.HAnimJoint()
HAnimJoint424.USE = "hanim_r_middle3"

HAnimHumanoid43.joints.append(HAnimJoint424)
HAnimJoint425 = x3d.HAnimJoint()
HAnimJoint425.USE = "hanim_l_midtarsal"

HAnimHumanoid43.joints.append(HAnimJoint425)
HAnimJoint426 = x3d.HAnimJoint()
HAnimJoint426.USE = "hanim_r_midtarsal"

HAnimHumanoid43.joints.append(HAnimJoint426)
HAnimJoint427 = x3d.HAnimJoint()
HAnimJoint427.USE = "hanim_l_pinky0"

HAnimHumanoid43.joints.append(HAnimJoint427)
HAnimJoint428 = x3d.HAnimJoint()
HAnimJoint428.USE = "hanim_r_pinky0"

HAnimHumanoid43.joints.append(HAnimJoint428)
HAnimJoint429 = x3d.HAnimJoint()
HAnimJoint429.USE = "hanim_l_pinky1"

HAnimHumanoid43.joints.append(HAnimJoint429)
HAnimJoint430 = x3d.HAnimJoint()
HAnimJoint430.USE = "hanim_r_pinky1"

HAnimHumanoid43.joints.append(HAnimJoint430)
HAnimJoint431 = x3d.HAnimJoint()
HAnimJoint431.USE = "hanim_l_pinky2"

HAnimHumanoid43.joints.append(HAnimJoint431)
HAnimJoint432 = x3d.HAnimJoint()
HAnimJoint432.USE = "hanim_r_pinky2"

HAnimHumanoid43.joints.append(HAnimJoint432)
HAnimJoint433 = x3d.HAnimJoint()
HAnimJoint433.USE = "hanim_l_pinky3"

HAnimHumanoid43.joints.append(HAnimJoint433)
HAnimJoint434 = x3d.HAnimJoint()
HAnimJoint434.USE = "hanim_r_pinky3"

HAnimHumanoid43.joints.append(HAnimJoint434)
HAnimJoint435 = x3d.HAnimJoint()
HAnimJoint435.USE = "hanim_l_ring0"

HAnimHumanoid43.joints.append(HAnimJoint435)
HAnimJoint436 = x3d.HAnimJoint()
HAnimJoint436.USE = "hanim_r_ring0"

HAnimHumanoid43.joints.append(HAnimJoint436)
HAnimJoint437 = x3d.HAnimJoint()
HAnimJoint437.USE = "hanim_l_ring1"

HAnimHumanoid43.joints.append(HAnimJoint437)
HAnimJoint438 = x3d.HAnimJoint()
HAnimJoint438.USE = "hanim_r_ring1"

HAnimHumanoid43.joints.append(HAnimJoint438)
HAnimJoint439 = x3d.HAnimJoint()
HAnimJoint439.USE = "hanim_l_ring2"

HAnimHumanoid43.joints.append(HAnimJoint439)
HAnimJoint440 = x3d.HAnimJoint()
HAnimJoint440.USE = "hanim_r_ring2"

HAnimHumanoid43.joints.append(HAnimJoint440)
HAnimJoint441 = x3d.HAnimJoint()
HAnimJoint441.USE = "hanim_l_ring3"

HAnimHumanoid43.joints.append(HAnimJoint441)
HAnimJoint442 = x3d.HAnimJoint()
HAnimJoint442.USE = "hanim_r_ring3"

HAnimHumanoid43.joints.append(HAnimJoint442)
HAnimJoint443 = x3d.HAnimJoint()
HAnimJoint443.USE = "hanim_l_shoulder"

HAnimHumanoid43.joints.append(HAnimJoint443)
HAnimJoint444 = x3d.HAnimJoint()
HAnimJoint444.USE = "hanim_r_shoulder"

HAnimHumanoid43.joints.append(HAnimJoint444)
HAnimJoint445 = x3d.HAnimJoint()
HAnimJoint445.USE = "hanim_l_sternoclavicular"

HAnimHumanoid43.joints.append(HAnimJoint445)
HAnimJoint446 = x3d.HAnimJoint()
HAnimJoint446.USE = "hanim_r_sternoclavicular"

HAnimHumanoid43.joints.append(HAnimJoint446)
HAnimJoint447 = x3d.HAnimJoint()
HAnimJoint447.USE = "hanim_l_subtalar"

HAnimHumanoid43.joints.append(HAnimJoint447)
HAnimJoint448 = x3d.HAnimJoint()
HAnimJoint448.USE = "hanim_r_subtalar"

HAnimHumanoid43.joints.append(HAnimJoint448)
HAnimJoint449 = x3d.HAnimJoint()
HAnimJoint449.USE = "hanim_l_thumb1"

HAnimHumanoid43.joints.append(HAnimJoint449)
HAnimJoint450 = x3d.HAnimJoint()
HAnimJoint450.USE = "hanim_r_thumb1"

HAnimHumanoid43.joints.append(HAnimJoint450)
HAnimJoint451 = x3d.HAnimJoint()
HAnimJoint451.USE = "hanim_l_thumb2"

HAnimHumanoid43.joints.append(HAnimJoint451)
HAnimJoint452 = x3d.HAnimJoint()
HAnimJoint452.USE = "hanim_r_thumb2"

HAnimHumanoid43.joints.append(HAnimJoint452)
HAnimJoint453 = x3d.HAnimJoint()
HAnimJoint453.USE = "hanim_l_thumb3"

HAnimHumanoid43.joints.append(HAnimJoint453)
HAnimJoint454 = x3d.HAnimJoint()
HAnimJoint454.USE = "hanim_r_thumb3"

HAnimHumanoid43.joints.append(HAnimJoint454)
HAnimJoint455 = x3d.HAnimJoint()
HAnimJoint455.USE = "hanim_l_wrist"

HAnimHumanoid43.joints.append(HAnimJoint455)
HAnimJoint456 = x3d.HAnimJoint()
HAnimJoint456.USE = "hanim_r_wrist"

HAnimHumanoid43.joints.append(HAnimJoint456)
HAnimSegment457 = x3d.HAnimSegment()
HAnimSegment457.USE = "hanim_pelvis"

HAnimHumanoid43.segments.append(HAnimSegment457)
HAnimSegment458 = x3d.HAnimSegment()
HAnimSegment458.USE = "hanim_skull"

HAnimHumanoid43.segments.append(HAnimSegment458)
HAnimSegment459 = x3d.HAnimSegment()
HAnimSegment459.USE = "hanim_jaw"

HAnimHumanoid43.segments.append(HAnimSegment459)
HAnimSegment460 = x3d.HAnimSegment()
HAnimSegment460.USE = "hanim_c1"

HAnimHumanoid43.segments.append(HAnimSegment460)
HAnimSegment461 = x3d.HAnimSegment()
HAnimSegment461.USE = "hanim_c2"

HAnimHumanoid43.segments.append(HAnimSegment461)
HAnimSegment462 = x3d.HAnimSegment()
HAnimSegment462.USE = "hanim_c3"

HAnimHumanoid43.segments.append(HAnimSegment462)
HAnimSegment463 = x3d.HAnimSegment()
HAnimSegment463.USE = "hanim_c4"

HAnimHumanoid43.segments.append(HAnimSegment463)
HAnimSegment464 = x3d.HAnimSegment()
HAnimSegment464.USE = "hanim_c5"

HAnimHumanoid43.segments.append(HAnimSegment464)
HAnimSegment465 = x3d.HAnimSegment()
HAnimSegment465.USE = "hanim_c6"

HAnimHumanoid43.segments.append(HAnimSegment465)
HAnimSegment466 = x3d.HAnimSegment()
HAnimSegment466.USE = "hanim_c7"

HAnimHumanoid43.segments.append(HAnimSegment466)
HAnimSegment467 = x3d.HAnimSegment()
HAnimSegment467.USE = "hanim_t1"

HAnimHumanoid43.segments.append(HAnimSegment467)
HAnimSegment468 = x3d.HAnimSegment()
HAnimSegment468.USE = "hanim_t2"

HAnimHumanoid43.segments.append(HAnimSegment468)
HAnimSegment469 = x3d.HAnimSegment()
HAnimSegment469.USE = "hanim_t3"

HAnimHumanoid43.segments.append(HAnimSegment469)
HAnimSegment470 = x3d.HAnimSegment()
HAnimSegment470.USE = "hanim_t4"

HAnimHumanoid43.segments.append(HAnimSegment470)
HAnimSegment471 = x3d.HAnimSegment()
HAnimSegment471.USE = "hanim_t5"

HAnimHumanoid43.segments.append(HAnimSegment471)
HAnimSegment472 = x3d.HAnimSegment()
HAnimSegment472.USE = "hanim_t6"

HAnimHumanoid43.segments.append(HAnimSegment472)
HAnimSegment473 = x3d.HAnimSegment()
HAnimSegment473.USE = "hanim_t7"

HAnimHumanoid43.segments.append(HAnimSegment473)
HAnimSegment474 = x3d.HAnimSegment()
HAnimSegment474.USE = "hanim_t8"

HAnimHumanoid43.segments.append(HAnimSegment474)
HAnimSegment475 = x3d.HAnimSegment()
HAnimSegment475.USE = "hanim_t9"

HAnimHumanoid43.segments.append(HAnimSegment475)
HAnimSegment476 = x3d.HAnimSegment()
HAnimSegment476.USE = "hanim_t10"

HAnimHumanoid43.segments.append(HAnimSegment476)
HAnimSegment477 = x3d.HAnimSegment()
HAnimSegment477.USE = "hanim_t11"

HAnimHumanoid43.segments.append(HAnimSegment477)
HAnimSegment478 = x3d.HAnimSegment()
HAnimSegment478.USE = "hanim_t12"

HAnimHumanoid43.segments.append(HAnimSegment478)
HAnimSegment479 = x3d.HAnimSegment()
HAnimSegment479.USE = "hanim_l1"

HAnimHumanoid43.segments.append(HAnimSegment479)
HAnimSegment480 = x3d.HAnimSegment()
HAnimSegment480.USE = "hanim_l2"

HAnimHumanoid43.segments.append(HAnimSegment480)
HAnimSegment481 = x3d.HAnimSegment()
HAnimSegment481.USE = "hanim_l3"

HAnimHumanoid43.segments.append(HAnimSegment481)
HAnimSegment482 = x3d.HAnimSegment()
HAnimSegment482.USE = "hanim_l4"

HAnimHumanoid43.segments.append(HAnimSegment482)
HAnimSegment483 = x3d.HAnimSegment()
HAnimSegment483.USE = "hanim_l5"

HAnimHumanoid43.segments.append(HAnimSegment483)
HAnimSegment484 = x3d.HAnimSegment()
HAnimSegment484.USE = "hanim_sacrum"

HAnimHumanoid43.segments.append(HAnimSegment484)
HAnimSegment485 = x3d.HAnimSegment()
HAnimSegment485.USE = "hanim_l_calf"

HAnimHumanoid43.segments.append(HAnimSegment485)
HAnimSegment486 = x3d.HAnimSegment()
HAnimSegment486.USE = "hanim_r_calf"

HAnimHumanoid43.segments.append(HAnimSegment486)
HAnimSegment487 = x3d.HAnimSegment()
HAnimSegment487.USE = "hanim_l_clavicle"

HAnimHumanoid43.segments.append(HAnimSegment487)
HAnimSegment488 = x3d.HAnimSegment()
HAnimSegment488.USE = "hanim_r_clavicle"

HAnimHumanoid43.segments.append(HAnimSegment488)
HAnimSegment489 = x3d.HAnimSegment()
HAnimSegment489.USE = "hanim_l_eyeball"

HAnimHumanoid43.segments.append(HAnimSegment489)
HAnimSegment490 = x3d.HAnimSegment()
HAnimSegment490.USE = "hanim_r_eyeball"

HAnimHumanoid43.segments.append(HAnimSegment490)
HAnimSegment491 = x3d.HAnimSegment()
HAnimSegment491.USE = "hanim_l_eyebrow"

HAnimHumanoid43.segments.append(HAnimSegment491)
HAnimSegment492 = x3d.HAnimSegment()
HAnimSegment492.USE = "hanim_r_eyebrow"

HAnimHumanoid43.segments.append(HAnimSegment492)
HAnimSegment493 = x3d.HAnimSegment()
HAnimSegment493.USE = "hanim_l_eyelid"

HAnimHumanoid43.segments.append(HAnimSegment493)
HAnimSegment494 = x3d.HAnimSegment()
HAnimSegment494.USE = "hanim_r_eyelid"

HAnimHumanoid43.segments.append(HAnimSegment494)
HAnimSegment495 = x3d.HAnimSegment()
HAnimSegment495.USE = "hanim_l_forearm"

HAnimHumanoid43.segments.append(HAnimSegment495)
HAnimSegment496 = x3d.HAnimSegment()
HAnimSegment496.USE = "hanim_r_forearm"

HAnimHumanoid43.segments.append(HAnimSegment496)
HAnimSegment497 = x3d.HAnimSegment()
HAnimSegment497.USE = "hanim_l_forefoot"

HAnimHumanoid43.segments.append(HAnimSegment497)
HAnimSegment498 = x3d.HAnimSegment()
HAnimSegment498.USE = "hanim_r_forefoot"

HAnimHumanoid43.segments.append(HAnimSegment498)
HAnimSegment499 = x3d.HAnimSegment()
HAnimSegment499.USE = "hanim_l_hand"

HAnimHumanoid43.segments.append(HAnimSegment499)
HAnimSegment500 = x3d.HAnimSegment()
HAnimSegment500.USE = "hanim_r_hand"

HAnimHumanoid43.segments.append(HAnimSegment500)
HAnimSegment501 = x3d.HAnimSegment()
HAnimSegment501.USE = "hanim_l_hindfoot"

HAnimHumanoid43.segments.append(HAnimSegment501)
HAnimSegment502 = x3d.HAnimSegment()
HAnimSegment502.USE = "hanim_r_hindfoot"

HAnimHumanoid43.segments.append(HAnimSegment502)
HAnimSegment503 = x3d.HAnimSegment()
HAnimSegment503.USE = "hanim_l_index_distal"

HAnimHumanoid43.segments.append(HAnimSegment503)
HAnimSegment504 = x3d.HAnimSegment()
HAnimSegment504.USE = "hanim_r_index_distal"

HAnimHumanoid43.segments.append(HAnimSegment504)
HAnimSegment505 = x3d.HAnimSegment()
HAnimSegment505.USE = "hanim_l_index_metacarpal"

HAnimHumanoid43.segments.append(HAnimSegment505)
HAnimSegment506 = x3d.HAnimSegment()
HAnimSegment506.USE = "hanim_r_index_metacarpal"

HAnimHumanoid43.segments.append(HAnimSegment506)
HAnimSegment507 = x3d.HAnimSegment()
HAnimSegment507.USE = "hanim_l_index_middle"

HAnimHumanoid43.segments.append(HAnimSegment507)
HAnimSegment508 = x3d.HAnimSegment()
HAnimSegment508.USE = "hanim_r_index_middle"

HAnimHumanoid43.segments.append(HAnimSegment508)
HAnimSegment509 = x3d.HAnimSegment()
HAnimSegment509.USE = "hanim_l_index_proximal"

HAnimHumanoid43.segments.append(HAnimSegment509)
HAnimSegment510 = x3d.HAnimSegment()
HAnimSegment510.USE = "hanim_r_index_proximal"

HAnimHumanoid43.segments.append(HAnimSegment510)
HAnimSegment511 = x3d.HAnimSegment()
HAnimSegment511.USE = "hanim_l_middistal"

HAnimHumanoid43.segments.append(HAnimSegment511)
HAnimSegment512 = x3d.HAnimSegment()
HAnimSegment512.USE = "hanim_r_middistal"

HAnimHumanoid43.segments.append(HAnimSegment512)
HAnimSegment513 = x3d.HAnimSegment()
HAnimSegment513.USE = "hanim_l_middle_distal"

HAnimHumanoid43.segments.append(HAnimSegment513)
HAnimSegment514 = x3d.HAnimSegment()
HAnimSegment514.USE = "hanim_r_middle_distal"

HAnimHumanoid43.segments.append(HAnimSegment514)
HAnimSegment515 = x3d.HAnimSegment()
HAnimSegment515.USE = "hanim_l_middle_metacarpal"

HAnimHumanoid43.segments.append(HAnimSegment515)
HAnimSegment516 = x3d.HAnimSegment()
HAnimSegment516.USE = "hanim_r_middle_metacarpal"

HAnimHumanoid43.segments.append(HAnimSegment516)
HAnimSegment517 = x3d.HAnimSegment()
HAnimSegment517.USE = "hanim_l_middle_middle"

HAnimHumanoid43.segments.append(HAnimSegment517)
HAnimSegment518 = x3d.HAnimSegment()
HAnimSegment518.USE = "hanim_r_middle_middle"

HAnimHumanoid43.segments.append(HAnimSegment518)
HAnimSegment519 = x3d.HAnimSegment()
HAnimSegment519.USE = "hanim_l_middle_proximal"

HAnimHumanoid43.segments.append(HAnimSegment519)
HAnimSegment520 = x3d.HAnimSegment()
HAnimSegment520.USE = "hanim_r_middle_proximal"

HAnimHumanoid43.segments.append(HAnimSegment520)
HAnimSegment521 = x3d.HAnimSegment()
HAnimSegment521.USE = "hanim_l_midproximal"

HAnimHumanoid43.segments.append(HAnimSegment521)
HAnimSegment522 = x3d.HAnimSegment()
HAnimSegment522.USE = "hanim_r_midproximal"

HAnimHumanoid43.segments.append(HAnimSegment522)
HAnimSegment523 = x3d.HAnimSegment()
HAnimSegment523.USE = "hanim_l_pinky_distal"

HAnimHumanoid43.segments.append(HAnimSegment523)
HAnimSegment524 = x3d.HAnimSegment()
HAnimSegment524.USE = "hanim_r_pinky_distal"

HAnimHumanoid43.segments.append(HAnimSegment524)
HAnimSegment525 = x3d.HAnimSegment()
HAnimSegment525.USE = "hanim_l_pinky_metacarpal"

HAnimHumanoid43.segments.append(HAnimSegment525)
HAnimSegment526 = x3d.HAnimSegment()
HAnimSegment526.USE = "hanim_r_pinky_metacarpal"

HAnimHumanoid43.segments.append(HAnimSegment526)
HAnimSegment527 = x3d.HAnimSegment()
HAnimSegment527.USE = "hanim_l_pinky_middle"

HAnimHumanoid43.segments.append(HAnimSegment527)
HAnimSegment528 = x3d.HAnimSegment()
HAnimSegment528.USE = "hanim_r_pinky_middle"

HAnimHumanoid43.segments.append(HAnimSegment528)
HAnimSegment529 = x3d.HAnimSegment()
HAnimSegment529.USE = "hanim_l_pinky_proximal"

HAnimHumanoid43.segments.append(HAnimSegment529)
HAnimSegment530 = x3d.HAnimSegment()
HAnimSegment530.USE = "hanim_r_pinky_proximal"

HAnimHumanoid43.segments.append(HAnimSegment530)
HAnimSegment531 = x3d.HAnimSegment()
HAnimSegment531.USE = "hanim_l_ring_distal"

HAnimHumanoid43.segments.append(HAnimSegment531)
HAnimSegment532 = x3d.HAnimSegment()
HAnimSegment532.USE = "hanim_r_ring_distal"

HAnimHumanoid43.segments.append(HAnimSegment532)
HAnimSegment533 = x3d.HAnimSegment()
HAnimSegment533.USE = "hanim_l_ring_metacarpal"

HAnimHumanoid43.segments.append(HAnimSegment533)
HAnimSegment534 = x3d.HAnimSegment()
HAnimSegment534.USE = "hanim_r_ring_metacarpal"

HAnimHumanoid43.segments.append(HAnimSegment534)
HAnimSegment535 = x3d.HAnimSegment()
HAnimSegment535.USE = "hanim_l_ring_middle"

HAnimHumanoid43.segments.append(HAnimSegment535)
HAnimSegment536 = x3d.HAnimSegment()
HAnimSegment536.USE = "hanim_r_ring_middle"

HAnimHumanoid43.segments.append(HAnimSegment536)
HAnimSegment537 = x3d.HAnimSegment()
HAnimSegment537.USE = "hanim_l_ring_proximal"

HAnimHumanoid43.segments.append(HAnimSegment537)
HAnimSegment538 = x3d.HAnimSegment()
HAnimSegment538.USE = "hanim_r_ring_proximal"

HAnimHumanoid43.segments.append(HAnimSegment538)
HAnimSegment539 = x3d.HAnimSegment()
HAnimSegment539.USE = "hanim_l_scapula"

HAnimHumanoid43.segments.append(HAnimSegment539)
HAnimSegment540 = x3d.HAnimSegment()
HAnimSegment540.USE = "hanim_r_scapula"

HAnimHumanoid43.segments.append(HAnimSegment540)
HAnimSegment541 = x3d.HAnimSegment()
HAnimSegment541.USE = "hanim_l_thigh"

HAnimHumanoid43.segments.append(HAnimSegment541)
HAnimSegment542 = x3d.HAnimSegment()
HAnimSegment542.USE = "hanim_r_thigh"

HAnimHumanoid43.segments.append(HAnimSegment542)
HAnimSegment543 = x3d.HAnimSegment()
HAnimSegment543.USE = "hanim_l_thumb_distal"

HAnimHumanoid43.segments.append(HAnimSegment543)
HAnimSegment544 = x3d.HAnimSegment()
HAnimSegment544.USE = "hanim_r_thumb_distal"

HAnimHumanoid43.segments.append(HAnimSegment544)
HAnimSegment545 = x3d.HAnimSegment()
HAnimSegment545.USE = "hanim_l_thumb_metacarpal"

HAnimHumanoid43.segments.append(HAnimSegment545)
HAnimSegment546 = x3d.HAnimSegment()
HAnimSegment546.USE = "hanim_r_thumb_metacarpal"

HAnimHumanoid43.segments.append(HAnimSegment546)
HAnimSegment547 = x3d.HAnimSegment()
HAnimSegment547.USE = "hanim_l_thumb_proximal"

HAnimHumanoid43.segments.append(HAnimSegment547)
HAnimSegment548 = x3d.HAnimSegment()
HAnimSegment548.USE = "hanim_r_thumb_proximal"

HAnimHumanoid43.segments.append(HAnimSegment548)
HAnimSegment549 = x3d.HAnimSegment()
HAnimSegment549.USE = "hanim_l_upperarm"

HAnimHumanoid43.segments.append(HAnimSegment549)
HAnimSegment550 = x3d.HAnimSegment()
HAnimSegment550.USE = "hanim_r_upperarm"

HAnimHumanoid43.segments.append(HAnimSegment550)
HAnimSite551 = x3d.HAnimSite()
HAnimSite551.USE = "hanim_crotch_pt"

HAnimHumanoid43.sites.append(HAnimSite551)
HAnimSite552 = x3d.HAnimSite()
HAnimSite552.USE = "hanim_skull_tip"

HAnimHumanoid43.sites.append(HAnimSite552)
HAnimSite553 = x3d.HAnimSite()
HAnimSite553.USE = "hanim_sellion_pt"

HAnimHumanoid43.sites.append(HAnimSite553)
HAnimSite554 = x3d.HAnimSite()
HAnimSite554.USE = "hanim_supramenton_pt"

HAnimHumanoid43.sites.append(HAnimSite554)
HAnimSite555 = x3d.HAnimSite()
HAnimSite555.USE = "hanim_nuchale_pt"

HAnimHumanoid43.sites.append(HAnimSite555)
HAnimSite556 = x3d.HAnimSite()
HAnimSite556.USE = "hanim_suprasternale_pt"

HAnimHumanoid43.sites.append(HAnimSite556)
HAnimSite557 = x3d.HAnimSite()
HAnimSite557.USE = "hanim_cervicale_pt"

HAnimHumanoid43.sites.append(HAnimSite557)
HAnimSite558 = x3d.HAnimSite()
HAnimSite558.USE = "hanim_substernale_pt"

HAnimHumanoid43.sites.append(HAnimSite558)
HAnimSite559 = x3d.HAnimSite()
HAnimSite559.USE = "hanim_rib10_midspine_pt"

HAnimHumanoid43.sites.append(HAnimSite559)
HAnimSite560 = x3d.HAnimSite()
HAnimSite560.USE = "hanim_waist_preferred_post_pt"

HAnimHumanoid43.sites.append(HAnimSite560)
HAnimSite561 = x3d.HAnimSite()
HAnimSite561.USE = "hanim_navel_pt"

HAnimHumanoid43.sites.append(HAnimSite561)
HAnimSite562 = x3d.HAnimSite()
HAnimSite562.USE = "hanim_l_acromion_pt"

HAnimHumanoid43.sites.append(HAnimSite562)
HAnimSite563 = x3d.HAnimSite()
HAnimSite563.USE = "hanim_r_acromion_pt"

HAnimHumanoid43.sites.append(HAnimSite563)
HAnimSite564 = x3d.HAnimSite()
HAnimSite564.USE = "hanim_r_asis_pt"

HAnimHumanoid43.sites.append(HAnimSite564)
HAnimSite565 = x3d.HAnimSite()
HAnimSite565.USE = "hanim_l_asis_pt"

HAnimHumanoid43.sites.append(HAnimSite565)
HAnimSite566 = x3d.HAnimSite()
HAnimSite566.USE = "hanim_l_axilla_ant_pt"

HAnimHumanoid43.sites.append(HAnimSite566)
HAnimSite567 = x3d.HAnimSite()
HAnimSite567.USE = "hanim_r_axilla_ant_pt"

HAnimHumanoid43.sites.append(HAnimSite567)
HAnimSite568 = x3d.HAnimSite()
HAnimSite568.USE = "hanim_l_axilla_post_pt"

HAnimHumanoid43.sites.append(HAnimSite568)
HAnimSite569 = x3d.HAnimSite()
HAnimSite569.USE = "hanim_r_axilla_post_pt"

HAnimHumanoid43.sites.append(HAnimSite569)
HAnimSite570 = x3d.HAnimSite()
HAnimSite570.USE = "hanim_l_calcaneous_post_pt"

HAnimHumanoid43.sites.append(HAnimSite570)
HAnimSite571 = x3d.HAnimSite()
HAnimSite571.USE = "hanim_r_calcaneous_post_pt"

HAnimHumanoid43.sites.append(HAnimSite571)
HAnimSite572 = x3d.HAnimSite()
HAnimSite572.USE = "hanim_l_clavicale_pt"

HAnimHumanoid43.sites.append(HAnimSite572)
HAnimSite573 = x3d.HAnimSite()
HAnimSite573.USE = "hanim_r_clavicale_pt"

HAnimHumanoid43.sites.append(HAnimSite573)
HAnimSite574 = x3d.HAnimSite()
HAnimSite574.USE = "hanim_l_dactylion_pt"

HAnimHumanoid43.sites.append(HAnimSite574)
HAnimSite575 = x3d.HAnimSite()
HAnimSite575.USE = "hanim_r_dactylion_pt"

HAnimHumanoid43.sites.append(HAnimSite575)
HAnimSite576 = x3d.HAnimSite()
HAnimSite576.USE = "hanim_l_digit2_pt"

HAnimHumanoid43.sites.append(HAnimSite576)
HAnimSite577 = x3d.HAnimSite()
HAnimSite577.USE = "hanim_r_digit2_pt"

HAnimHumanoid43.sites.append(HAnimSite577)
HAnimSite578 = x3d.HAnimSite()
HAnimSite578.USE = "hanim_l_femoral_lateral_epicn_pt"

HAnimHumanoid43.sites.append(HAnimSite578)
HAnimSite579 = x3d.HAnimSite()
HAnimSite579.USE = "hanim_r_femoral_lateral_epicn_pt"

HAnimHumanoid43.sites.append(HAnimSite579)
HAnimSite580 = x3d.HAnimSite()
HAnimSite580.USE = "hanim_l_femoral_medial_epicn_pt"

HAnimHumanoid43.sites.append(HAnimSite580)
HAnimSite581 = x3d.HAnimSite()
HAnimSite581.USE = "hanim_r_femoral_medial_epicn_pt"

HAnimHumanoid43.sites.append(HAnimSite581)
HAnimSite582 = x3d.HAnimSite()
HAnimSite582.USE = "hanim_l_forefoot_tip"

HAnimHumanoid43.sites.append(HAnimSite582)
HAnimSite583 = x3d.HAnimSite()
HAnimSite583.USE = "hanim_r_forefoot_tip"

HAnimHumanoid43.sites.append(HAnimSite583)
HAnimSite584 = x3d.HAnimSite()
HAnimSite584.USE = "hanim_r_gonion_pt"

HAnimHumanoid43.sites.append(HAnimSite584)
HAnimSite585 = x3d.HAnimSite()
HAnimSite585.USE = "hanim_l_gonion_pt"

HAnimHumanoid43.sites.append(HAnimSite585)
HAnimSite586 = x3d.HAnimSite()
HAnimSite586.USE = "hanim_l_humeral_lateral_epicn_pt"

HAnimHumanoid43.sites.append(HAnimSite586)
HAnimSite587 = x3d.HAnimSite()
HAnimSite587.USE = "hanim_r_humeral_lateral_epicn_pt"

HAnimHumanoid43.sites.append(HAnimSite587)
HAnimSite588 = x3d.HAnimSite()
HAnimSite588.USE = "hanim_l_humeral_medial_epicn_pt"

HAnimHumanoid43.sites.append(HAnimSite588)
HAnimSite589 = x3d.HAnimSite()
HAnimSite589.USE = "hanim_r_humeral_medial_epicn_pt"

HAnimHumanoid43.sites.append(HAnimSite589)
HAnimSite590 = x3d.HAnimSite()
HAnimSite590.USE = "hanim_r_iliocristale_pt"

HAnimHumanoid43.sites.append(HAnimSite590)
HAnimSite591 = x3d.HAnimSite()
HAnimSite591.USE = "hanim_l_iliocristale_pt"

HAnimHumanoid43.sites.append(HAnimSite591)
HAnimSite592 = x3d.HAnimSite()
HAnimSite592.USE = "hanim_l_index_distal_tip"

HAnimHumanoid43.sites.append(HAnimSite592)
HAnimSite593 = x3d.HAnimSite()
HAnimSite593.USE = "hanim_r_index_distal_tip"

HAnimHumanoid43.sites.append(HAnimSite593)
HAnimSite594 = x3d.HAnimSite()
HAnimSite594.USE = "hanim_r_infraorbitale_pt"

HAnimHumanoid43.sites.append(HAnimSite594)
HAnimSite595 = x3d.HAnimSite()
HAnimSite595.USE = "hanim_l_infraorbitale_pt"

HAnimHumanoid43.sites.append(HAnimSite595)
HAnimSite596 = x3d.HAnimSite()
HAnimSite596.USE = "hanim_l_knee_crease_pt"

HAnimHumanoid43.sites.append(HAnimSite596)
HAnimSite597 = x3d.HAnimSite()
HAnimSite597.USE = "hanim_r_knee_crease_pt"

HAnimHumanoid43.sites.append(HAnimSite597)
HAnimSite598 = x3d.HAnimSite()
HAnimSite598.USE = "hanim_l_lateral_malleolus_pt"

HAnimHumanoid43.sites.append(HAnimSite598)
HAnimSite599 = x3d.HAnimSite()
HAnimSite599.USE = "hanim_r_lateral_malleolus_pt"

HAnimHumanoid43.sites.append(HAnimSite599)
HAnimSite600 = x3d.HAnimSite()
HAnimSite600.USE = "hanim_l_medial_malleolus_pt"

HAnimHumanoid43.sites.append(HAnimSite600)
HAnimSite601 = x3d.HAnimSite()
HAnimSite601.USE = "hanim_r_medial_malleolus_pt"

HAnimHumanoid43.sites.append(HAnimSite601)
HAnimSite602 = x3d.HAnimSite()
HAnimSite602.USE = "hanim_l_metacarpal_pha2_pt"

HAnimHumanoid43.sites.append(HAnimSite602)
HAnimSite603 = x3d.HAnimSite()
HAnimSite603.USE = "hanim_r_metacarpal_pha2_pt"

HAnimHumanoid43.sites.append(HAnimSite603)
HAnimSite604 = x3d.HAnimSite()
HAnimSite604.USE = "hanim_l_metacarpal_pha5_pt"

HAnimHumanoid43.sites.append(HAnimSite604)
HAnimSite605 = x3d.HAnimSite()
HAnimSite605.USE = "hanim_r_metacarpal_pha5_pt"

HAnimHumanoid43.sites.append(HAnimSite605)
HAnimSite606 = x3d.HAnimSite()
HAnimSite606.USE = "hanim_l_metatarsal_pha1_pt"

HAnimHumanoid43.sites.append(HAnimSite606)
HAnimSite607 = x3d.HAnimSite()
HAnimSite607.USE = "hanim_r_metatarsal_pha1_pt"

HAnimHumanoid43.sites.append(HAnimSite607)
HAnimSite608 = x3d.HAnimSite()
HAnimSite608.USE = "hanim_l_metatarsal_pha5_pt"

HAnimHumanoid43.sites.append(HAnimSite608)
HAnimSite609 = x3d.HAnimSite()
HAnimSite609.USE = "hanim_r_metatarsal_pha5_pt"

HAnimHumanoid43.sites.append(HAnimSite609)
HAnimSite610 = x3d.HAnimSite()
HAnimSite610.USE = "hanim_l_middle_distal_tip"

HAnimHumanoid43.sites.append(HAnimSite610)
HAnimSite611 = x3d.HAnimSite()
HAnimSite611.USE = "hanim_r_middle_distal_tip"

HAnimHumanoid43.sites.append(HAnimSite611)
HAnimSite612 = x3d.HAnimSite()
HAnimSite612.USE = "hanim_r_neck_base_pt"

HAnimHumanoid43.sites.append(HAnimSite612)
HAnimSite613 = x3d.HAnimSite()
HAnimSite613.USE = "hanim_l_neck_base_pt"

HAnimHumanoid43.sites.append(HAnimSite613)
HAnimSite614 = x3d.HAnimSite()
HAnimSite614.USE = "hanim_l_olecranon_pt"

HAnimHumanoid43.sites.append(HAnimSite614)
HAnimSite615 = x3d.HAnimSite()
HAnimSite615.USE = "hanim_r_olecranon_pt"

HAnimHumanoid43.sites.append(HAnimSite615)
HAnimSite616 = x3d.HAnimSite()
HAnimSite616.USE = "hanim_l_pinky_distal_tip"

HAnimHumanoid43.sites.append(HAnimSite616)
HAnimSite617 = x3d.HAnimSite()
HAnimSite617.USE = "hanim_r_pinky_distal_tip"

HAnimHumanoid43.sites.append(HAnimSite617)
HAnimSite618 = x3d.HAnimSite()
HAnimSite618.USE = "hanim_r_psis_pt"

HAnimHumanoid43.sites.append(HAnimSite618)
HAnimSite619 = x3d.HAnimSite()
HAnimSite619.USE = "hanim_l_psis_pt"

HAnimHumanoid43.sites.append(HAnimSite619)
HAnimSite620 = x3d.HAnimSite()
HAnimSite620.USE = "hanim_l_radial_styloid_pt"

HAnimHumanoid43.sites.append(HAnimSite620)
HAnimSite621 = x3d.HAnimSite()
HAnimSite621.USE = "hanim_r_radial_styloid_pt"

HAnimHumanoid43.sites.append(HAnimSite621)
HAnimSite622 = x3d.HAnimSite()
HAnimSite622.USE = "hanim_l_radiale_pt"

HAnimHumanoid43.sites.append(HAnimSite622)
HAnimSite623 = x3d.HAnimSite()
HAnimSite623.USE = "hanim_r_radiale_pt"

HAnimHumanoid43.sites.append(HAnimSite623)
HAnimSite624 = x3d.HAnimSite()
HAnimSite624.USE = "hanim_r_rib10_pt"

HAnimHumanoid43.sites.append(HAnimSite624)
HAnimSite625 = x3d.HAnimSite()
HAnimSite625.USE = "hanim_l_rib10_pt"

HAnimHumanoid43.sites.append(HAnimSite625)
HAnimSite626 = x3d.HAnimSite()
HAnimSite626.USE = "hanim_l_ring_distal_tip"

HAnimHumanoid43.sites.append(HAnimSite626)
HAnimSite627 = x3d.HAnimSite()
HAnimSite627.USE = "hanim_r_ring_distal_tip"

HAnimHumanoid43.sites.append(HAnimSite627)
HAnimSite628 = x3d.HAnimSite()
HAnimSite628.USE = "hanim_temporomandibular_l_site_pt"

HAnimHumanoid43.sites.append(HAnimSite628)
HAnimSite629 = x3d.HAnimSite()
HAnimSite629.USE = "hanim_temporomandibular_r_site_pt"

HAnimHumanoid43.sites.append(HAnimSite629)
HAnimSite630 = x3d.HAnimSite()
HAnimSite630.USE = "hanim_l_sphyrion_pt"

HAnimHumanoid43.sites.append(HAnimSite630)
HAnimSite631 = x3d.HAnimSite()
HAnimSite631.USE = "hanim_r_sphyrion_pt"

HAnimHumanoid43.sites.append(HAnimSite631)
HAnimSite632 = x3d.HAnimSite()
HAnimSite632.USE = "hanim_r_thelion_pt"

HAnimHumanoid43.sites.append(HAnimSite632)
HAnimSite633 = x3d.HAnimSite()
HAnimSite633.USE = "hanim_l_thelion_pt"

HAnimHumanoid43.sites.append(HAnimSite633)
HAnimSite634 = x3d.HAnimSite()
HAnimSite634.USE = "hanim_l_thumb_distal_tip"

HAnimHumanoid43.sites.append(HAnimSite634)
HAnimSite635 = x3d.HAnimSite()
HAnimSite635.USE = "hanim_r_thumb_distal_tip"

HAnimHumanoid43.sites.append(HAnimSite635)
HAnimSite636 = x3d.HAnimSite()
HAnimSite636.USE = "hanim_r_tragion_pt"

HAnimHumanoid43.sites.append(HAnimSite636)
HAnimSite637 = x3d.HAnimSite()
HAnimSite637.USE = "hanim_l_tragion_pt"

HAnimHumanoid43.sites.append(HAnimSite637)
HAnimSite638 = x3d.HAnimSite()
HAnimSite638.USE = "hanim_r_trochanterion_pt"

HAnimHumanoid43.sites.append(HAnimSite638)
HAnimSite639 = x3d.HAnimSite()
HAnimSite639.USE = "hanim_l_trochanterion_pt"

HAnimHumanoid43.sites.append(HAnimSite639)
HAnimSite640 = x3d.HAnimSite()
HAnimSite640.USE = "hanim_l_ulnar_styloid_pt"

HAnimHumanoid43.sites.append(HAnimSite640)
HAnimSite641 = x3d.HAnimSite()
HAnimSite641.USE = "hanim_r_ulnar_styloid_pt"

HAnimHumanoid43.sites.append(HAnimSite641)

Scene29.children.append(HAnimHumanoid43)

X3D0.Scene = Scene29
f = open("././HAnim1SpecificationLOA3Invisible_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
