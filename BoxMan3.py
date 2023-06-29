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
meta3.content = "BoxMan3.x3d"

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.name = "description"
meta4.content = "A Seamless VRML Human, demonstrating the HAnim 2001 Specification, animation scripting via an external prototype (ExternProtoDeclare)."

head1.children.append(meta4)
meta5 = x3d.meta()
meta5.name = "creator"
meta5.content = "James Smith - james@vapourtech.com"

head1.children.append(meta5)
meta6 = x3d.meta()
meta6.name = "translator"
meta6.content = "Don Brutzman and Matt Beitler"

head1.children.append(meta6)
meta7 = x3d.meta()
meta7.name = "created"
meta7.content = "1 March 2001"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.name = "translated"
meta8.content = "19 October 2001"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "modified"
meta9.content = "6 January 2023"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "reference"
meta10.content = "http://HAnim.org"

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.name = "reference"
meta11.content = "originals/boxman.wrl"

head1.children.append(meta11)
meta12 = x3d.meta()
meta12.name = "reference"
meta12.content = "BoxMan3.js"

head1.children.append(meta12)
meta13 = x3d.meta()
meta13.name = "warning"
meta13.content = "Skin mesh is split across multiple shapes within a Group, should that be allowed?"

head1.children.append(meta13)
meta14 = x3d.meta()
meta14.name = "TODO"
meta14.content = "What does the original animation script accomplish? It is not hooked up, script source contains errors..."

head1.children.append(meta14)
meta15 = x3d.meta()
meta15.name = "TODO"
meta15.content = "InstantReality Forum Issue: InstantReality is ignoring the Viewpoint nodes in the topmost HAnimSite. http://forum.instantreality.org"

head1.children.append(meta15)
meta16 = x3d.meta()
meta16.name = "Image"
meta16.content = "BoxManViewInclined.png"

head1.children.append(meta16)
meta17 = x3d.meta()
meta17.name = "Image"
meta17.content = "BoxManViewFront.png"

head1.children.append(meta17)
meta18 = x3d.meta()
meta18.name = "Image"
meta18.content = "BoxManViewRight.png"

head1.children.append(meta18)
meta19 = x3d.meta()
meta19.name = "Image"
meta19.content = "BoxManViewLeft.png"

head1.children.append(meta19)
meta20 = x3d.meta()
meta20.name = "Image"
meta20.content = "BoxManViewTop.png"

head1.children.append(meta20)
meta21 = x3d.meta()
meta21.name = "reference"
meta21.content = "BoxManAnimationPanel.x3d"

head1.children.append(meta21)
meta22 = x3d.meta()
meta22.name = "reference"
meta22.content = "http://HAnim.org/Models/HAnim2001/boxman/boxman.wrl"

head1.children.append(meta22)
meta23 = x3d.meta()
meta23.name = "reference"
meta23.content = "http://www.vapourtech.com/team/james/boxman.wrl"

head1.children.append(meta23)
meta24 = x3d.meta()
meta24.name = "reference"
meta24.content = "http://HAnim.org/Specifications/HAnim2001"

head1.children.append(meta24)
meta25 = x3d.meta()
meta25.name = "reference"
meta25.content = "http://HAnim.org/Models"

head1.children.append(meta25)
meta26 = x3d.meta()
meta26.name = "reference"
meta26.content = "http://HAnim.org/Nodes"

head1.children.append(meta26)
meta27 = x3d.meta()
meta27.name = "reference"
meta27.content = "https://www.web3d.org/x3d/content/X3dToVrml97.xslt"

head1.children.append(meta27)
meta28 = x3d.meta()
meta28.name = "rights"
meta28.content = "(C) 2000 James Smith - james@vapourtech.com"

head1.children.append(meta28)
meta29 = x3d.meta()
meta29.name = "reference"
meta29.content = "http://www.vapourtech.com"

head1.children.append(meta29)
meta30 = x3d.meta()
meta30.name = "subject"
meta30.content = "BoxMan HAnim 2.0"

head1.children.append(meta30)
meta31 = x3d.meta()
meta31.name = "identifier"
meta31.content = "https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Legacy/BoxMan3.x3d"

head1.children.append(meta31)
meta32 = x3d.meta()
meta32.name = "generator"
meta32.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"

head1.children.append(meta32)
meta33 = x3d.meta()
meta33.name = "license"
meta33.content = "../license.html"

head1.children.append(meta33)

X3D0.head = head1
Scene34 = x3d.Scene()
WorldInfo35 = x3d.WorldInfo()
WorldInfo35.info = ["(C) 2000 James Smith - james@vapourtech.com","http://www.vapourtech.com/team/james/boxman.wrl","Blaxxun compatibility by Tu Lam - TuL@seamless-solutions.com"]
WorldInfo35.title = "BoxMan3 - A Seamless VRML Human"

Scene34.children.append(WorldInfo35)
Background36 = x3d.Background()
Background36.groundColor = [0.6,0.6,0.6]
Background36.skyColor = [0.75,0.75,0.75]

Scene34.children.append(Background36)
#When converting to VRML97 (which didn't include HAnim), HAnim node prototypes are provided automatically by the X3dToVrml97.xslt translation stylesheet
HAnimHumanoid37 = x3d.HAnimHumanoid()
HAnimHumanoid37.name = "Humanoid"
HAnimHumanoid37.DEF = "boxman_Humanoid"
HAnimHumanoid37.info = ["authorName=James Smith","authorEmail=james@vapourtech.com","copyright=(C) 2000 James Smith - james@vapourtech.com","humanoidVersion=2.0"]
HAnimHumanoid37.version = "2.0"
HAnimJoint38 = x3d.HAnimJoint()
HAnimJoint38.name = "humanoid_root"
HAnimJoint38.DEF = "boxman_humanoid_root"
HAnimJoint38.center = [0,0.9723,-0.0728]
HAnimJoint38.skinCoordIndex = [0,1,2,3,4,5,6,7,8,9,10,11]
HAnimJoint38.skinCoordWeight = [1,1,1,1,1,1,1,1,1,1,1,1]
HAnimJoint38.ulimit = [0,0,0]
HAnimJoint38.llimit = [0,0,0]
HAnimSegment39 = x3d.HAnimSegment()
HAnimSegment39.name = "sacrum"
HAnimSegment39.DEF = "boxman_sacrum"
Transform40 = x3d.Transform()
Transform40.translation = [0,0.9723,-0.0728]
Shape41 = x3d.Shape()
Shape41.DEF = "SphereYellow"
Appearance42 = x3d.Appearance()
Material43 = x3d.Material()
Material43.diffuseColor = [1,1,0]

Appearance42.material = Material43

Shape41.appearance = Appearance42
Sphere44 = x3d.Sphere()
Sphere44.radius = 0.02

Shape41.geometry = Sphere44

Transform40.children.append(Shape41)

HAnimSegment39.children.append(Transform40)

HAnimJoint38.children.append(HAnimSegment39)
HAnimJoint45 = x3d.HAnimJoint()
HAnimJoint45.name = "l_hip"
HAnimJoint45.DEF = "boxman_l_hip"
HAnimJoint45.center = [0.0956,0.9364,0]
HAnimJoint45.skinCoordIndex = [12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43]
HAnimJoint45.skinCoordWeight = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]
HAnimJoint45.ulimit = [0,0,0]
HAnimJoint45.llimit = [0,0,0]
HAnimSegment46 = x3d.HAnimSegment()
HAnimSegment46.name = "l_thigh"
HAnimSegment46.DEF = "boxman_l_thigh"
Transform47 = x3d.Transform()
Transform47.translation = [0.0956,0.9364,0]
Shape48 = x3d.Shape()
Shape48.USE = "SphereYellow"

Transform47.children.append(Shape48)

HAnimSegment46.children.append(Transform47)

HAnimJoint45.children.append(HAnimSegment46)
HAnimJoint49 = x3d.HAnimJoint()
HAnimJoint49.name = "l_knee"
HAnimJoint49.DEF = "boxman_l_knee"
HAnimJoint49.center = [0.0956,0.5095,-0.0036]
HAnimJoint49.skinCoordIndex = [36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63]
HAnimJoint49.skinCoordWeight = [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
HAnimJoint49.ulimit = [0,0,0]
HAnimJoint49.llimit = [0,0,0]
HAnimSegment50 = x3d.HAnimSegment()
HAnimSegment50.name = "l_calf"
HAnimSegment50.DEF = "boxman_l_calf"
Transform51 = x3d.Transform()
Transform51.translation = [0.0956,0.5095,-0.0036]
Shape52 = x3d.Shape()
Shape52.USE = "SphereYellow"

Transform51.children.append(Shape52)

HAnimSegment50.children.append(Transform51)

HAnimJoint49.children.append(HAnimSegment50)
HAnimJoint53 = x3d.HAnimJoint()
HAnimJoint53.name = "l_ankle"
HAnimJoint53.DEF = "boxman_l_ankle"
HAnimJoint53.center = [0.0946,0.0762,-0.0261]
HAnimJoint53.skinCoordIndex = [64,65,66,67,68,69,70,71]
HAnimJoint53.skinCoordWeight = [1,1,1,1,1,1,1,1]
HAnimJoint53.ulimit = [0,0,0]
HAnimJoint53.llimit = [0,0,0]
HAnimSegment54 = x3d.HAnimSegment()
HAnimSegment54.name = "l_hindfoot"
HAnimSegment54.DEF = "boxman_l_hindfoot"
Transform55 = x3d.Transform()
Transform55.translation = [0.0946,0.0762,-0.0261]
Shape56 = x3d.Shape()
Shape56.USE = "SphereYellow"

Transform55.children.append(Shape56)

HAnimSegment54.children.append(Transform55)

HAnimJoint53.children.append(HAnimSegment54)
HAnimJoint57 = x3d.HAnimJoint()
HAnimJoint57.name = "l_midtarsal"
HAnimJoint57.DEF = "boxman_l_midtarsal"
HAnimJoint57.center = [0.1079,0.0317,0.067]
HAnimJoint57.skinCoordIndex = [72,73,74,75,76,77,78,79]
HAnimJoint57.skinCoordWeight = [1,1,1,1,1,1,1,1]
HAnimJoint57.ulimit = [0,0,0]
HAnimJoint57.llimit = [0,0,0]
HAnimSegment58 = x3d.HAnimSegment()
HAnimSegment58.name = "l_middistal"
HAnimSegment58.DEF = "boxman_l_middistal"
Transform59 = x3d.Transform()
Transform59.translation = [0.1079,0.0317,0.067]
Shape60 = x3d.Shape()
Shape60.USE = "SphereYellow"

Transform59.children.append(Shape60)

HAnimSegment58.children.append(Transform59)
HAnimSite61 = x3d.HAnimSite()
HAnimSite61.name = "l_middistal_tip"
HAnimSite61.DEF = "boxman_l_middistal_tip"
HAnimSite61.translation = [0.095,0.0005,0.1924]
Shape62 = x3d.Shape()
Shape62.DEF = "SphereRed"
Appearance63 = x3d.Appearance()
Material64 = x3d.Material()
Material64.diffuseColor = [1,0,0]

Appearance63.material = Material64

Shape62.appearance = Appearance63
Sphere65 = x3d.Sphere()
Sphere65.radius = 0.02

Shape62.geometry = Sphere65

HAnimSite61.children.append(Shape62)

HAnimSegment58.children.append(HAnimSite61)

HAnimJoint57.children.append(HAnimSegment58)

HAnimJoint53.children.append(HAnimJoint57)

HAnimJoint49.children.append(HAnimJoint53)

HAnimJoint45.children.append(HAnimJoint49)

HAnimJoint38.children.append(HAnimJoint45)
HAnimJoint66 = x3d.HAnimJoint()
HAnimJoint66.name = "r_hip"
HAnimJoint66.DEF = "boxman_r_hip"
HAnimJoint66.center = [-0.0956,0.9364,0]
HAnimJoint66.skinCoordIndex = [80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111]
HAnimJoint66.skinCoordWeight = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]
HAnimJoint66.ulimit = [0,0,0]
HAnimJoint66.llimit = [0,0,0]
HAnimSegment67 = x3d.HAnimSegment()
HAnimSegment67.name = "r_thigh"
HAnimSegment67.DEF = "boxman_r_thigh"
Transform68 = x3d.Transform()
Transform68.translation = [-0.0956,0.9364,0]
Shape69 = x3d.Shape()
Shape69.USE = "SphereYellow"

Transform68.children.append(Shape69)

HAnimSegment67.children.append(Transform68)

HAnimJoint66.children.append(HAnimSegment67)
HAnimJoint70 = x3d.HAnimJoint()
HAnimJoint70.name = "r_knee"
HAnimJoint70.DEF = "boxman_r_knee"
HAnimJoint70.center = [-0.0956,0.5095,-0.0036]
HAnimJoint70.skinCoordIndex = [104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131]
HAnimJoint70.skinCoordWeight = [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
HAnimJoint70.ulimit = [0,0,0]
HAnimJoint70.llimit = [0,0,0]
HAnimSegment71 = x3d.HAnimSegment()
HAnimSegment71.name = "r_calf"
HAnimSegment71.DEF = "boxman_r_calf"
Transform72 = x3d.Transform()
Transform72.translation = [-0.0956,0.5095,-0.0036]
Shape73 = x3d.Shape()
Shape73.USE = "SphereYellow"

Transform72.children.append(Shape73)

HAnimSegment71.children.append(Transform72)

HAnimJoint70.children.append(HAnimSegment71)
HAnimJoint74 = x3d.HAnimJoint()
HAnimJoint74.name = "r_ankle"
HAnimJoint74.DEF = "boxman_r_ankle"
HAnimJoint74.center = [-0.0946,0.0762,-0.0261]
HAnimJoint74.skinCoordIndex = [132,133,134,135,136,137,138,139]
HAnimJoint74.skinCoordWeight = [1,1,1,1,1,1,1,1]
HAnimJoint74.ulimit = [0,0,0]
HAnimJoint74.llimit = [0,0,0]
HAnimSegment75 = x3d.HAnimSegment()
HAnimSegment75.name = "r_hindfoot"
HAnimSegment75.DEF = "boxman_r_hindfoot"
Transform76 = x3d.Transform()
Transform76.translation = [-0.0946,0.0762,-0.0261]
Shape77 = x3d.Shape()
Shape77.USE = "SphereYellow"

Transform76.children.append(Shape77)

HAnimSegment75.children.append(Transform76)

HAnimJoint74.children.append(HAnimSegment75)
HAnimJoint78 = x3d.HAnimJoint()
HAnimJoint78.name = "r_midtarsal"
HAnimJoint78.DEF = "boxman_r_midtarsal"
HAnimJoint78.center = [-0.1079,0.0317,0.067]
HAnimJoint78.skinCoordIndex = [140,141,142,143,144,145,146,147]
HAnimJoint78.skinCoordWeight = [1,1,1,1,1,1,1,1]
HAnimJoint78.ulimit = [0,0,0]
HAnimJoint78.llimit = [0,0,0]
HAnimSegment79 = x3d.HAnimSegment()
HAnimSegment79.name = "r_middistal"
HAnimSegment79.DEF = "boxman_r_middistal"
Transform80 = x3d.Transform()
Transform80.translation = [-0.1079,0.0317,0.067]
Shape81 = x3d.Shape()
Shape81.USE = "SphereYellow"

Transform80.children.append(Shape81)

HAnimSegment79.children.append(Transform80)
HAnimSite82 = x3d.HAnimSite()
HAnimSite82.name = "r_middistal_tip"
HAnimSite82.DEF = "boxman_r_middistal_tip"
HAnimSite82.translation = [-0.095,0.0005,0.1924]
Shape83 = x3d.Shape()
Shape83.USE = "SphereRed"

HAnimSite82.children.append(Shape83)

HAnimSegment79.children.append(HAnimSite82)

HAnimJoint78.children.append(HAnimSegment79)

HAnimJoint74.children.append(HAnimJoint78)

HAnimJoint70.children.append(HAnimJoint74)

HAnimJoint66.children.append(HAnimJoint70)

HAnimJoint38.children.append(HAnimJoint66)
HAnimJoint84 = x3d.HAnimJoint()
HAnimJoint84.name = "vl5"
HAnimJoint84.DEF = "boxman_vl5"
HAnimJoint84.center = [0,1.0817,-0.0728]
HAnimJoint84.skinCoordIndex = [148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167]
HAnimJoint84.skinCoordWeight = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
HAnimJoint84.ulimit = [0,0,0]
HAnimJoint84.llimit = [0,0,0]
HAnimSegment85 = x3d.HAnimSegment()
HAnimSegment85.name = "l5"
HAnimSegment85.DEF = "boxman_l5"
Transform86 = x3d.Transform()
Transform86.translation = [0,1.0817,-0.0728]
Shape87 = x3d.Shape()
Shape87.USE = "SphereYellow"

Transform86.children.append(Shape87)

HAnimSegment85.children.append(Transform86)

HAnimJoint84.children.append(HAnimSegment85)
HAnimJoint88 = x3d.HAnimJoint()
HAnimJoint88.name = "skullbase"
HAnimJoint88.DEF = "boxman_skullbase"
HAnimJoint88.center = [0,1.644,0.036]
HAnimJoint88.skinCoordIndex = [168,169,170,171,172,173,174,175]
HAnimJoint88.skinCoordWeight = [1,1,1,1,1,1,1,1]
HAnimJoint88.ulimit = [0,0,0]
HAnimJoint88.llimit = [0,0,0]
HAnimSegment89 = x3d.HAnimSegment()
HAnimSegment89.name = "skull"
HAnimSegment89.DEF = "boxman_skull"
Transform90 = x3d.Transform()
Transform90.translation = [0,1.644,0.036]
Shape91 = x3d.Shape()
Shape91.USE = "SphereYellow"

Transform90.children.append(Shape91)

HAnimSegment89.children.append(Transform90)
HAnimSite92 = x3d.HAnimSite()
HAnimSite92.name = "skull_tip"
HAnimSite92.DEF = "boxman_skull_tip"
HAnimSite92.translation = [-0.0029,1.7771,0.0274]
Shape93 = x3d.Shape()
Shape93.USE = "SphereYellow"

HAnimSite92.children.append(Shape93)

HAnimSegment89.children.append(HAnimSite92)

HAnimJoint88.children.append(HAnimSegment89)

HAnimJoint84.children.append(HAnimJoint88)
HAnimJoint94 = x3d.HAnimJoint()
HAnimJoint94.name = "l_shoulder"
HAnimJoint94.DEF = "boxman_l_shoulder"
HAnimJoint94.center = [0.1968,1.4642,-0.0265]
HAnimJoint94.skinCoordIndex = [176,177,178,179,180,181,182,183]
HAnimJoint94.skinCoordWeight = [1,1,1,1,1,1,1,1]
HAnimJoint94.ulimit = [0,0,0]
HAnimJoint94.llimit = [0,0,0]
HAnimSegment95 = x3d.HAnimSegment()
HAnimSegment95.name = "l_upperarm"
HAnimSegment95.DEF = "boxman_l_upperarm"
Transform96 = x3d.Transform()
Transform96.translation = [0.1968,1.4642,-0.0265]
Shape97 = x3d.Shape()
Shape97.USE = "SphereYellow"

Transform96.children.append(Shape97)

HAnimSegment95.children.append(Transform96)

HAnimJoint94.children.append(HAnimSegment95)
HAnimJoint98 = x3d.HAnimJoint()
HAnimJoint98.name = "l_elbow"
HAnimJoint98.DEF = "boxman_l_elbow"
HAnimJoint98.center = [0.1982,1.1622,-0.0557]
HAnimJoint98.skinCoordIndex = [184,185,186,187,188,189,190,191]
HAnimJoint98.skinCoordWeight = [1,1,1,1,1,1,1,1]
HAnimJoint98.ulimit = [0,0,0]
HAnimJoint98.llimit = [0,0,0]
HAnimSegment99 = x3d.HAnimSegment()
HAnimSegment99.name = "l_forearm"
HAnimSegment99.DEF = "boxman_l_forearm"
Transform100 = x3d.Transform()
Transform100.translation = [0.1982,1.1622,-0.0557]
Shape101 = x3d.Shape()
Shape101.USE = "SphereYellow"

Transform100.children.append(Shape101)

HAnimSegment99.children.append(Transform100)

HAnimJoint98.children.append(HAnimSegment99)
HAnimJoint102 = x3d.HAnimJoint()
HAnimJoint102.name = "l_wrist"
HAnimJoint102.DEF = "boxman_l_wrist"
HAnimJoint102.center = [0.1972,0.8929,-0.069]
HAnimJoint102.skinCoordIndex = [192,193,194,195,196,197,198,199]
HAnimJoint102.skinCoordWeight = [1,1,1,1,1,1,1,1]
HAnimJoint102.ulimit = [0,0,0]
HAnimJoint102.llimit = [0,0,0]
HAnimSegment103 = x3d.HAnimSegment()
HAnimSegment103.name = "l_hand"
HAnimSegment103.DEF = "boxman_l_hand"
Transform104 = x3d.Transform()
Transform104.translation = [0.1972,0.8929,-0.069]
Shape105 = x3d.Shape()
Shape105.USE = "SphereYellow"

Transform104.children.append(Shape105)

HAnimSegment103.children.append(Transform104)
HAnimSite106 = x3d.HAnimSite()
HAnimSite106.name = "l_hand_tip"
HAnimSite106.DEF = "boxman_l_hand_tip"
HAnimSite106.translation = [0.1912,0.6976,-0.071]
Shape107 = x3d.Shape()
Shape107.USE = "SphereRed"

HAnimSite106.children.append(Shape107)

HAnimSegment103.children.append(HAnimSite106)

HAnimJoint102.children.append(HAnimSegment103)

HAnimJoint98.children.append(HAnimJoint102)

HAnimJoint94.children.append(HAnimJoint98)

HAnimJoint84.children.append(HAnimJoint94)
HAnimJoint108 = x3d.HAnimJoint()
HAnimJoint108.name = "r_shoulder"
HAnimJoint108.DEF = "boxman_r_shoulder"
HAnimJoint108.center = [-0.1968,1.4642,-0.0265]
HAnimJoint108.skinCoordIndex = [200,201,202,203,204,205,206,207]
HAnimJoint108.skinCoordWeight = [1,1,1,1,1,1,1,1]
HAnimJoint108.ulimit = [0,0,0]
HAnimJoint108.llimit = [0,0,0]
HAnimSegment109 = x3d.HAnimSegment()
HAnimSegment109.name = "r_upperarm"
HAnimSegment109.DEF = "boxman_r_upperarm"
Transform110 = x3d.Transform()
Transform110.translation = [-0.1968,1.4642,-0.0265]
Shape111 = x3d.Shape()
Shape111.USE = "SphereYellow"

Transform110.children.append(Shape111)

HAnimSegment109.children.append(Transform110)

HAnimJoint108.children.append(HAnimSegment109)
HAnimJoint112 = x3d.HAnimJoint()
HAnimJoint112.name = "r_elbow"
HAnimJoint112.DEF = "boxman_r_elbow"
HAnimJoint112.center = [-0.1982,1.1622,-0.0557]
HAnimJoint112.skinCoordIndex = [208,209,210,211,212,213,214,215]
HAnimJoint112.skinCoordWeight = [1,1,1,1,1,1,1,1]
HAnimJoint112.ulimit = [0,0,0]
HAnimJoint112.llimit = [0,0,0]
HAnimSegment113 = x3d.HAnimSegment()
HAnimSegment113.name = "r_forearm"
HAnimSegment113.DEF = "boxman_r_forearm"
Transform114 = x3d.Transform()
Transform114.translation = [-0.1982,1.1622,-0.0557]
Shape115 = x3d.Shape()
Shape115.USE = "SphereYellow"

Transform114.children.append(Shape115)

HAnimSegment113.children.append(Transform114)

HAnimJoint112.children.append(HAnimSegment113)
HAnimJoint116 = x3d.HAnimJoint()
HAnimJoint116.name = "r_wrist"
HAnimJoint116.DEF = "boxman_r_wrist"
HAnimJoint116.center = [-0.1972,0.8929,-0.069]
HAnimJoint116.skinCoordIndex = [216,217,218,219,220,221,222,223]
HAnimJoint116.skinCoordWeight = [1,1,1,1,1,1,1,1]
HAnimJoint116.ulimit = [0,0,0]
HAnimJoint116.llimit = [0,0,0]
HAnimSegment117 = x3d.HAnimSegment()
HAnimSegment117.name = "r_hand"
HAnimSegment117.DEF = "boxman_r_hand"
Transform118 = x3d.Transform()
Transform118.translation = [-0.1972,0.8929,-0.069]
Shape119 = x3d.Shape()
Shape119.USE = "SphereYellow"

Transform118.children.append(Shape119)

HAnimSegment117.children.append(Transform118)
HAnimSite120 = x3d.HAnimSite()
HAnimSite120.name = "r_hand_tip"
HAnimSite120.DEF = "boxman_r_hand_tip"
HAnimSite120.translation = [-0.1912,0.6976,-0.071]
Shape121 = x3d.Shape()
Shape121.USE = "SphereRed"

HAnimSite120.children.append(Shape121)

HAnimSegment117.children.append(HAnimSite120)

HAnimJoint116.children.append(HAnimSegment117)

HAnimJoint112.children.append(HAnimJoint116)

HAnimJoint108.children.append(HAnimJoint112)

HAnimJoint84.children.append(HAnimJoint108)

HAnimJoint38.children.append(HAnimJoint84)

HAnimHumanoid37.skeleton.append(HAnimJoint38)
## sacrum (12) # l_thigh (28) # l_calf (24) # l_hindfoot (8) # l_middistal (8) # r_thigh (28) # r_calf (24) # r_hindfoot (8) # r_middistal (8) # l5 (20) # skull (8) # l_upperarm (8) # l_forearm (8) # l_hand (8) # r_upperarm (8) # r_forearm (8) # r_hand (8)
#top-level joint references
#top-level segment references
#top-level site references
Coordinate122 = x3d.Coordinate()
Coordinate122.DEF = "SKINCOORD"
Coordinate122.point = (-0.0500,1.0000,0.0500,0.0500,1.0000,0.0500,0.0300,0.9700,-0.1000,-0.0300,0.9700,-0.1000,0.0300,0.9400,-0.0750,-0.0300,0.9400,-0.0750,0.0000,0.9200,0.0000,0.0000,0.9400,0.0300,-0.1200,1.0600,0.0500,0.1200,1.0600,0.0500,0.1200,1.0600,-0.1000,-0.1200,1.0600,-0.1000,0.0456,0.9364,0.0500,0.1456,0.9364,0.0500,0.1456,0.9364,-0.0500,0.0456,0.9364,-0.0500,0.0456,0.9000,0.0500,0.1456,0.9000,0.0500,0.1456,0.9000,-0.0500,0.0456,0.9000,-0.0500,0.0456,0.8000,0.0500,0.1456,0.8000,0.0500,0.1456,0.8000,-0.0500,0.0456,0.8000,-0.0500,0.0456,0.7000,0.0500,0.1456,0.7000,0.0500,0.1456,0.7000,-0.0500,0.0456,0.7000,-0.0500,0.0456,0.6000,0.0500,0.1456,0.6000,0.0500,0.1456,0.6000,-0.0500,0.0456,0.6000,-0.0500,0.0456,0.5500,0.0500,0.1456,0.5500,0.0500,0.1456,0.5500,-0.0500,0.0456,0.5500,-0.0500,0.0456,0.5200,0.0500,0.1456,0.5200,0.0500,0.1456,0.5200,-0.0500,0.0456,0.5200,-0.0500,0.0456,0.5000,0.0500,0.1456,0.5000,0.0500,0.1456,0.5000,-0.0500,0.0456,0.5000,-0.0500,0.0454,0.4300,0.0450,0.1454,0.4300,0.0450,0.1454,0.4300,-0.0550,0.0454,0.4300,-0.0550,0.0452,0.3600,0.0400,0.1452,0.3600,0.0400,0.1452,0.3600,-0.0600,0.0452,0.3600,-0.0600,0.0450,0.2900,0.0350,0.1450,0.2900,0.0350,0.1450,0.2900,-0.0650,0.0450,0.2900,-0.0650,0.0448,0.2100,0.0300,0.1448,0.2100,0.0300,0.1448,0.2100,-0.0700,0.0448,0.2100,-0.0700,0.0446,0.1262,0.0250,0.1446,0.1262,0.0250,0.1446,0.1262,-0.0750,0.0446,0.1262,-0.0750,0.0446,0.0762,0.0250,0.1446,0.0762,0.0250,0.1446,0.0000,-0.0750,0.0446,0.0000,-0.0750,0.0446,0.0562,0.0570,0.1446,0.0562,0.0570,0.1446,0.0000,0.0570,0.0446,0.0000,0.0570,0.0446,0.0562,0.0870,0.1446,0.0562,0.0870,0.1446,0.0000,0.0870,0.0446,0.0000,0.0870,0.0446,0.0562,0.1924,0.1446,0.0562,0.1924,0.1446,0.0000,0.1924,0.0446,0.0000,0.1924,-0.0456,0.9364,0.0500,-0.1456,0.9364,0.0500,-0.1456,0.9364,-0.0500,-0.0456,0.9364,-0.0500,-0.0456,0.9000,0.0500,-0.1456,0.9000,0.0500,-0.1456,0.9000,-0.0500,-0.0456,0.9000,-0.0500,-0.0456,0.8000,0.0500,-0.1456,0.8000,0.0500,-0.1456,0.8000,-0.0500,-0.0456,0.8000,-0.0500,-0.0456,0.7000,0.0500,-0.1456,0.7000,0.0500,-0.1456,0.7000,-0.0500,-0.0456,0.7000,-0.0500,-0.0456,0.6000,0.0500,-0.1456,0.6000,0.0500,-0.1456,0.6000,-0.0500,-0.0456,0.6000,-0.0500,-0.0456,0.5500,0.0500,-0.1456,0.5500,0.0500,-0.1456,0.5500,-0.0500,-0.0456,0.5500,-0.0500,-0.0456,0.5200,0.0500,-0.1456,0.5200,0.0500,-0.1456,0.5200,-0.0500,-0.0456,0.5200,-0.0500,-0.0456,0.5000,0.0500,-0.1456,0.5000,0.0500,-0.1456,0.5000,-0.0500,-0.0456,0.5000,-0.0500,-0.0454,0.4300,0.0450,-0.1454,0.4300,0.0450,-0.1454,0.4300,-0.0550,-0.0454,0.4300,-0.0550,-0.0452,0.3600,0.0400,-0.1452,0.3600,0.0400,-0.1452,0.3600,-0.0600,-0.0452,0.3600,-0.0600,-0.0450,0.2900,0.0350,-0.1450,0.2900,0.0350,-0.1450,0.2900,-0.0650,-0.0450,0.2900,-0.0650,-0.0448,0.2100,0.0300,-0.1448,0.2100,0.0300,-0.1448,0.2100,-0.0700,-0.0448,0.2100,-0.0700,-0.0446,0.1262,0.0250,-0.1446,0.1262,0.0250,-0.1446,0.1262,-0.0750,-0.0446,0.1262,-0.0750,-0.0446,0.0762,0.0250,-0.1446,0.0762,0.0250,-0.1446,0.0000,-0.0750,-0.0446,0.0000,-0.0750,-0.0446,0.0562,0.0570,-0.1446,0.0562,0.0570,-0.1446,0.0000,0.0570,-0.0446,0.0000,0.0570,-0.0446,0.0562,0.0870,-0.1446,0.0562,0.0870,-0.1446,0.0000,0.0870,-0.0446,0.0000,0.0870,-0.0446,0.0562,0.1924,-0.1446,0.0562,0.1924,-0.1446,0.0000,0.1924,-0.0446,0.0000,0.1924,-0.1200,1.1000,0.0500,0.1200,1.1000,0.0500,0.1200,1.1000,-0.1000,-0.1200,1.1000,-0.1000,-0.1400,1.4200,0.0450,0.1400,1.4200,0.0450,0.1400,1.4200,-0.0900,-0.1400,1.4200,-0.0900,-0.2400,1.5200,0.0350,0.2400,1.5200,0.0350,0.2400,1.5200,-0.0900,-0.2400,1.5200,-0.0900,-0.0500,1.5600,0.0300,0.0500,1.5600,0.0300,0.0500,1.5600,-0.0600,-0.0500,1.5600,-0.0600,-0.0500,1.6000,0.0600,0.0500,1.6000,0.0600,0.0500,1.6200,-0.0300,-0.0500,1.6200,-0.0300,-0.0700,1.7770,0.1300,0.0700,1.7770,0.1300,0.0700,1.7770,-0.0300,-0.0700,1.7770,-0.0300,-0.0700,1.6000,0.1300,0.0700,1.6000,0.1300,0.0700,1.6600,-0.0300,-0.0700,1.6600,-0.0300,0.1600,1.4200,0.0150,0.2400,1.5000,0.0150,0.2400,1.5000,-0.0750,0.1600,1.4200,-0.0750,0.1700,1.1800,-0.0250,0.2300,1.1800,-0.0250,0.2300,1.1800,-0.0850,0.1700,1.1800,-0.0850,0.1700,1.1400,-0.0250,0.2300,1.1400,-0.0250,0.2300,1.1400,-0.0850,0.1700,1.1400,-0.0850,0.1800,0.9100,-0.0500,0.2200,0.9100,-0.0500,0.2200,0.9100,-0.0900,0.1800,0.9100,-0.0900,0.1800,0.8700,-0.0200,0.2200,0.8700,-0.0200,0.2200,0.8700,-0.1000,0.1800,0.8700,-0.1000,0.1800,0.6976,-0.0200,0.2200,0.6976,-0.0200,0.2200,0.6976,-0.1000,0.1800,0.6976,-0.1000,-0.1600,1.4200,0.0150,-0.2400,1.5000,0.0150,-0.2400,1.5000,-0.0750,-0.1600,1.4200,-0.0750,-0.1700,1.1800,-0.0250,-0.2300,1.1800,-0.0250,-0.2300,1.1800,-0.0850,-0.1700,1.1800,-0.0850,-0.1700,1.1400,-0.0250,-0.2300,1.1400,-0.0250,-0.2300,1.1400,-0.0850,-0.1700,1.1400,-0.0850,-0.1800,0.9100,-0.0500,-0.2200,0.9100,-0.0500,-0.2200,0.9100,-0.0900,-0.1800,0.9100,-0.0900,-0.1800,0.8700,-0.0200,-0.2200,0.8700,-0.0200,-0.2200,0.8700,-0.1000,-0.1800,0.8700,-0.1000,-0.1800,0.6976,-0.0200,-0.2200,0.6976,-0.0200,-0.2200,0.6976,-0.1000,-0.1800,0.6976,-0.1000)

HAnimHumanoid37.skinCoord = Coordinate122
Group123 = x3d.Group()
Shape124 = x3d.Shape()
Shape124.DEF = "TrouserSkin"
Appearance125 = x3d.Appearance()
Material126 = x3d.Material()
Material126.diffuseColor = [0,0,1]
Material126.transparency = 0.5

Appearance125.material = Material126

Shape124.appearance = Appearance125
## 0: sacrum (8) # 1: l_hip joint (8) # 2: r_hip joint (8) # 3: l_thigh (48) # 4: l_knee joint (8) # 5: l_calf (40) # 10: r_thigh (48) # 11: r_knee joint (8) # 12: r_calf (40)
IndexedFaceSet127 = x3d.IndexedFaceSet()
IndexedFaceSet127.coordIndex = [0,7,1,-1,8,0,1,-1,1,9,8,-1,10,2,3,-1,3,11,10,-1,2,4,5,-1,5,3,2,-1,4,6,5,-1,7,12,1,-1,1,12,13,-1,13,9,1,-1,9,13,14,-1,14,10,9,-1,10,14,15,-1,15,2,10,-1,12,7,6,-1,6,15,12,-1,15,6,4,-1,4,2,15,-1,0,80,7,-1,81,80,0,-1,0,8,81,-1,82,81,8,-1,8,11,82,-1,83,82,11,-1,11,3,83,-1,6,7,80,-1,80,83,6,-1,5,6,83,-1,83,3,5,-1,12,16,17,-1,17,13,12,-1,13,17,18,-1,18,14,13,-1,14,18,19,-1,19,15,14,-1,15,19,16,-1,16,12,15,-1,16,20,21,-1,21,17,16,-1,17,21,22,-1,22,18,17,-1,18,22,23,-1,23,19,18,-1,19,23,20,-1,20,16,19,-1,20,24,25,-1,25,21,20,-1,21,25,26,-1,26,22,21,-1,22,26,27,-1,27,23,22,-1,23,27,24,-1,24,20,23,-1,24,28,29,-1,29,25,24,-1,25,29,30,-1,30,26,25,-1,26,30,31,-1,31,27,26,-1,27,31,28,-1,28,24,27,-1,28,32,33,-1,33,29,28,-1,29,33,34,-1,34,30,29,-1,30,34,35,-1,35,31,30,-1,31,35,32,-1,32,28,31,-1,32,36,37,-1,37,33,32,-1,33,37,38,-1,38,34,33,-1,34,38,39,-1,39,35,34,-1,35,39,36,-1,36,32,35,-1,36,40,41,-1,41,37,36,-1,37,41,42,-1,42,38,37,-1,38,42,43,-1,43,39,38,-1,39,43,40,-1,40,36,39,-1,40,44,45,-1,45,41,40,-1,41,45,46,-1,46,42,41,-1,42,46,47,-1,47,43,42,-1,43,47,44,-1,44,40,43,-1,44,48,49,-1,49,45,44,-1,45,49,50,-1,50,46,45,-1,46,50,51,-1,51,47,46,-1,47,51,48,-1,48,44,47,-1,48,52,53,-1,53,49,48,-1,49,53,54,-1,54,50,49,-1,50,54,55,-1,55,51,50,-1,51,55,52,-1,52,48,51,-1,52,56,57,-1,57,53,52,-1,53,57,58,-1,58,54,53,-1,54,58,59,-1,59,55,54,-1,55,59,56,-1,56,52,55,-1,56,60,61,-1,61,57,56,-1,57,61,62,-1,62,58,57,-1,58,62,63,-1,63,59,58,-1,59,63,60,-1,60,56,59,-1,81,85,84,-1,84,80,81,-1,82,86,85,-1,85,81,82,-1,83,87,86,-1,86,82,83,-1,80,84,87,-1,87,83,80,-1,85,89,88,-1,88,84,85,-1,86,90,89,-1,89,85,86,-1,87,91,90,-1,90,86,87,-1,84,88,91,-1,91,87,84,-1,89,93,92,-1,92,88,89,-1,90,94,93,-1,93,89,90,-1,91,95,94,-1,94,90,91,-1,88,92,95,-1,95,91,88,-1,93,97,96,-1,96,92,93,-1,94,98,97,-1,97,93,94,-1,95,99,98,-1,98,94,95,-1,92,96,99,-1,99,95,92,-1,97,101,100,-1,100,96,97,-1,98,102,101,-1,101,97,98,-1,99,103,102,-1,102,98,99,-1,96,100,103,-1,103,99,96,-1,101,105,104,-1,104,100,101,-1,102,106,105,-1,105,101,102,-1,103,107,106,-1,106,102,103,-1,100,104,107,-1,107,103,100,-1,105,109,108,-1,108,104,105,-1,106,110,109,-1,109,105,106,-1,107,111,110,-1,110,106,107,-1,104,108,111,-1,111,107,104,-1,109,113,112,-1,112,108,109,-1,110,114,113,-1,113,109,110,-1,111,115,114,-1,114,110,111,-1,108,112,115,-1,115,111,108,-1,113,117,116,-1,116,112,113,-1,114,118,117,-1,117,113,114,-1,115,119,118,-1,118,114,115,-1,112,116,119,-1,119,115,112,-1,117,121,120,-1,120,116,117,-1,118,122,121,-1,121,117,118,-1,119,123,122,-1,122,118,119,-1,116,120,123,-1,123,119,116,-1,121,125,124,-1,124,120,121,-1,122,126,125,-1,125,121,122,-1,123,127,126,-1,126,122,123,-1,120,124,127,-1,127,123,120,-1,125,129,128,-1,128,124,125,-1,126,130,129,-1,129,125,126,-1,127,131,130,-1,130,126,127,-1,124,128,131,-1,131,127,124,-1]
Coordinate128 = x3d.Coordinate()
Coordinate128.USE = "SKINCOORD"

IndexedFaceSet127.coord = Coordinate128

Shape124.geometry = IndexedFaceSet127

Group123.children.append(Shape124)
Shape129 = x3d.Shape()
Shape129.DEF = "ShoeSkin"
Appearance130 = x3d.Appearance()
Material131 = x3d.Material()
Material131.diffuseColor = [0,0,0]
Material131.transparency = 0.5

Appearance130.material = Material131

Shape129.appearance = Appearance130
## 6: l_ankle joint (8) # 7: l_hindfoot (8) # 8: l_midtarsal joint (8) # 9: l_middistal (10) # 13: r_ankle joint (8) # 14: r_hindfoot (8) # 15: r_midtarsal joint (8) # 16: r_middistal (10)
IndexedFaceSet132 = x3d.IndexedFaceSet()
IndexedFaceSet132.coordIndex = [60,64,65,-1,65,61,60,-1,61,65,66,-1,66,62,61,-1,62,66,67,-1,67,63,62,-1,63,67,64,-1,64,60,63,-1,64,68,69,-1,69,65,64,-1,65,69,70,-1,70,66,65,-1,66,70,71,-1,71,67,66,-1,67,71,68,-1,68,64,67,-1,68,72,73,-1,73,69,68,-1,69,73,74,-1,74,70,69,-1,70,74,75,-1,75,71,70,-1,71,75,72,-1,72,68,71,-1,72,76,77,-1,77,73,72,-1,73,77,78,-1,78,74,73,-1,74,78,79,-1,79,75,74,-1,75,79,76,-1,76,72,75,-1,76,79,78,-1,78,77,76,-1,129,133,132,-1,132,128,129,-1,130,134,133,-1,133,129,130,-1,131,135,134,-1,134,130,131,-1,128,132,135,-1,135,131,128,-1,133,137,136,-1,136,132,133,-1,134,138,137,-1,137,133,134,-1,135,139,138,-1,138,134,135,-1,132,136,139,-1,139,135,132,-1,137,141,140,-1,140,136,137,-1,138,142,141,-1,141,137,138,-1,139,143,142,-1,142,138,139,-1,136,140,143,-1,143,139,136,-1,141,145,144,-1,144,140,141,-1,142,146,145,-1,145,141,142,-1,143,147,146,-1,146,142,143,-1,140,144,147,-1,147,143,140,-1,145,146,147,-1,147,144,145,-1]
Coordinate133 = x3d.Coordinate()
Coordinate133.USE = "SKINCOORD"

IndexedFaceSet132.coord = Coordinate133

Shape129.geometry = IndexedFaceSet132

Group123.children.append(Shape129)
Shape134 = x3d.Shape()
Shape134.DEF = "ShirtSkin"
Appearance135 = x3d.Appearance()
Material136 = x3d.Material()
Material136.diffuseColor = [1,1,0]
Material136.transparency = 0.5

Appearance135.material = Material136

Shape134.appearance = Appearance135
## 17: vl5_joint (8) # 18: l5 (28) # 21: l_shoulder joint (8) # 22: l_upperarm (8) # 23: l_elbow joint (8) # 24: l_forearm (8) # 27: r_shoulder joint (8) # 28: r_upperarm (8) # 29: r_elbow joint (8) # 30: r_forearm (8)
IndexedFaceSet137 = x3d.IndexedFaceSet()
IndexedFaceSet137.coordIndex = [148,8,9,-1,9,149,148,-1,149,9,10,-1,10,150,149,-1,150,10,11,-1,11,151,150,-1,151,11,8,-1,8,148,151,-1,152,148,149,-1,149,153,152,-1,153,149,150,-1,150,154,153,-1,154,150,151,-1,151,155,154,-1,155,151,148,-1,148,152,155,-1,156,152,153,-1,153,157,156,-1,158,154,155,-1,155,159,158,-1,160,156,157,-1,157,161,160,-1,161,157,158,-1,158,162,161,-1,162,158,159,-1,159,163,162,-1,163,159,156,-1,156,160,163,-1,164,160,161,-1,161,165,164,-1,165,161,162,-1,162,166,165,-1,166,162,163,-1,163,167,166,-1,167,163,160,-1,160,164,167,-1,153,176,177,-1,177,157,153,-1,157,177,178,-1,178,158,157,-1,158,178,179,-1,179,154,158,-1,154,179,176,-1,176,153,154,-1,176,180,181,-1,181,177,176,-1,177,181,182,-1,182,178,177,-1,178,182,183,-1,183,179,178,-1,179,183,180,-1,180,176,179,-1,180,184,185,-1,185,181,180,-1,181,185,186,-1,186,182,181,-1,182,186,187,-1,187,183,182,-1,183,187,184,-1,184,180,183,-1,184,188,189,-1,189,185,184,-1,185,189,190,-1,190,186,185,-1,186,190,191,-1,191,187,186,-1,187,191,188,-1,188,184,187,-1,152,156,201,-1,201,200,152,-1,156,159,202,-1,202,201,156,-1,159,155,203,-1,203,202,159,-1,155,152,200,-1,200,203,155,-1,201,205,204,-1,204,200,201,-1,202,206,205,-1,205,201,202,-1,203,207,206,-1,206,202,203,-1,200,204,207,-1,207,203,200,-1,205,209,208,-1,208,204,205,-1,206,210,209,-1,209,205,206,-1,207,211,210,-1,210,206,207,-1,204,208,211,-1,211,207,204,-1,209,213,212,-1,212,208,209,-1,210,214,213,-1,213,209,210,-1,211,215,214,-1,214,210,211,-1,208,212,215,-1,215,211,208,-1]
Coordinate138 = x3d.Coordinate()
Coordinate138.USE = "SKINCOORD"

IndexedFaceSet137.coord = Coordinate138

Shape134.geometry = IndexedFaceSet137

Group123.children.append(Shape134)
Shape139 = x3d.Shape()
Shape139.DEF = "HeadHandsFleshToneSkin"
Appearance140 = x3d.Appearance()
Material141 = x3d.Material()
Material141.diffuseColor = [1,0.75,0.75]
Material141.transparency = 0.5

Appearance140.material = Material141

Shape139.appearance = Appearance140
## 19: skullbase joint (8) # 20: skull (10) # 25: l_wrist joint (8) # 26: l_hand (10) # 31: r_wrist joint (8) # 32: r_hand (10)
IndexedFaceSet142 = x3d.IndexedFaceSet()
IndexedFaceSet142.coordIndex = [172,164,165,-1,165,173,172,-1,173,165,166,-1,166,174,173,-1,174,166,167,-1,167,175,174,-1,175,167,164,-1,164,172,175,-1,168,172,173,-1,173,169,168,-1,169,173,174,-1,174,170,169,-1,170,174,175,-1,175,171,170,-1,171,175,172,-1,172,168,171,-1,171,168,169,-1,169,170,171,-1,188,192,193,-1,193,189,188,-1,189,193,194,-1,194,190,189,-1,190,194,195,-1,195,191,190,-1,191,195,192,-1,192,188,191,-1,192,196,197,-1,197,193,192,-1,193,197,198,-1,198,194,193,-1,194,198,199,-1,199,195,194,-1,195,199,196,-1,196,192,195,-1,196,199,198,-1,198,197,196,-1,213,217,216,-1,216,212,213,-1,214,218,217,-1,217,213,214,-1,215,219,218,-1,218,214,215,-1,212,216,219,-1,219,215,212,-1,217,221,220,-1,220,216,217,-1,218,222,221,-1,221,217,218,-1,219,223,222,-1,222,218,219,-1,216,220,223,-1,223,219,216,-1,221,222,223,-1,223,220,221,-1]
Coordinate143 = x3d.Coordinate()
Coordinate143.USE = "SKINCOORD"

IndexedFaceSet142.coord = Coordinate143

Shape139.geometry = IndexedFaceSet142

Group123.children.append(Shape139)
Shape144 = x3d.Shape()
Shape144.DEF = "SkinLines"
Appearance145 = x3d.Appearance()
Material146 = x3d.Material()
Material146.diffuseColor = [0,0,0]

Appearance145.material = Material146

Shape144.appearance = Appearance145
#Combined set of prior IFS coordIndex values
IndexedLineSet147 = x3d.IndexedLineSet()
IndexedLineSet147.coordIndex = [0,7,1,-1,8,0,1,-1,1,9,8,-1,10,2,3,-1,3,11,10,-1,2,4,5,-1,5,3,2,-1,4,6,5,-1,7,12,1,-1,1,12,13,-1,13,9,1,-1,9,13,14,-1,14,10,9,-1,10,14,15,-1,15,2,10,-1,12,7,6,-1,6,15,12,-1,15,6,4,-1,4,2,15,-1,0,80,7,-1,81,80,0,-1,0,8,81,-1,82,81,8,-1,8,11,82,-1,83,82,11,-1,11,3,83,-1,6,7,80,-1,80,83,6,-1,5,6,83,-1,83,3,5,-1,12,16,17,-1,17,13,12,-1,13,17,18,-1,18,14,13,-1,14,18,19,-1,19,15,14,-1,15,19,16,-1,16,12,15,-1,16,20,21,-1,21,17,16,-1,17,21,22,-1,22,18,17,-1,18,22,23,-1,23,19,18,-1,19,23,20,-1,20,16,19,-1,20,24,25,-1,25,21,20,-1,21,25,26,-1,26,22,21,-1,22,26,27,-1,27,23,22,-1,23,27,24,-1,24,20,23,-1,24,28,29,-1,29,25,24,-1,25,29,30,-1,30,26,25,-1,26,30,31,-1,31,27,26,-1,27,31,28,-1,28,24,27,-1,28,32,33,-1,33,29,28,-1,29,33,34,-1,34,30,29,-1,30,34,35,-1,35,31,30,-1,31,35,32,-1,32,28,31,-1,32,36,37,-1,37,33,32,-1,33,37,38,-1,38,34,33,-1,34,38,39,-1,39,35,34,-1,35,39,36,-1,36,32,35,-1,36,40,41,-1,41,37,36,-1,37,41,42,-1,42,38,37,-1,38,42,43,-1,43,39,38,-1,39,43,40,-1,40,36,39,-1,40,44,45,-1,45,41,40,-1,41,45,46,-1,46,42,41,-1,42,46,47,-1,47,43,42,-1,43,47,44,-1,44,40,43,-1,44,48,49,-1,49,45,44,-1,45,49,50,-1,50,46,45,-1,46,50,51,-1,51,47,46,-1,47,51,48,-1,48,44,47,-1,48,52,53,-1,53,49,48,-1,49,53,54,-1,54,50,49,-1,50,54,55,-1,55,51,50,-1,51,55,52,-1,52,48,51,-1,52,56,57,-1,57,53,52,-1,53,57,58,-1,58,54,53,-1,54,58,59,-1,59,55,54,-1,55,59,56,-1,56,52,55,-1,56,60,61,-1,61,57,56,-1,57,61,62,-1,62,58,57,-1,58,62,63,-1,63,59,58,-1,59,63,60,-1,60,56,59,-1,81,85,84,-1,84,80,81,-1,82,86,85,-1,85,81,82,-1,83,87,86,-1,86,82,83,-1,80,84,87,-1,87,83,80,-1,85,89,88,-1,88,84,85,-1,86,90,89,-1,89,85,86,-1,87,91,90,-1,90,86,87,-1,84,88,91,-1,91,87,84,-1,89,93,92,-1,92,88,89,-1,90,94,93,-1,93,89,90,-1,91,95,94,-1,94,90,91,-1,88,92,95,-1,95,91,88,-1,93,97,96,-1,96,92,93,-1,94,98,97,-1,97,93,94,-1,95,99,98,-1,98,94,95,-1,92,96,99,-1,99,95,92,-1,97,101,100,-1,100,96,97,-1,98,102,101,-1,101,97,98,-1,99,103,102,-1,102,98,99,-1,96,100,103,-1,103,99,96,-1,101,105,104,-1,104,100,101,-1,102,106,105,-1,105,101,102,-1,103,107,106,-1,106,102,103,-1,100,104,107,-1,107,103,100,-1,105,109,108,-1,108,104,105,-1,106,110,109,-1,109,105,106,-1,107,111,110,-1,110,106,107,-1,104,108,111,-1,111,107,104,-1,109,113,112,-1,112,108,109,-1,110,114,113,-1,113,109,110,-1,111,115,114,-1,114,110,111,-1,108,112,115,-1,115,111,108,-1,113,117,116,-1,116,112,113,-1,114,118,117,-1,117,113,114,-1,115,119,118,-1,118,114,115,-1,112,116,119,-1,119,115,112,-1,117,121,120,-1,120,116,117,-1,118,122,121,-1,121,117,118,-1,119,123,122,-1,122,118,119,-1,116,120,123,-1,123,119,116,-1,121,125,124,-1,124,120,121,-1,122,126,125,-1,125,121,122,-1,123,127,126,-1,126,122,123,-1,120,124,127,-1,127,123,120,-1,125,129,128,-1,128,124,125,-1,126,130,129,-1,129,125,126,-1,127,131,130,-1,130,126,127,-1,124,128,131,-1,131,127,124,-1,60,64,65,-1,65,61,60,-1,61,65,66,-1,66,62,61,-1,62,66,67,-1,67,63,62,-1,63,67,64,-1,64,60,63,-1,64,68,69,-1,69,65,64,-1,65,69,70,-1,70,66,65,-1,66,70,71,-1,71,67,66,-1,67,71,68,-1,68,64,67,-1,68,72,73,-1,73,69,68,-1,69,73,74,-1,74,70,69,-1,70,74,75,-1,75,71,70,-1,71,75,72,-1,72,68,71,-1,72,76,77,-1,77,73,72,-1,73,77,78,-1,78,74,73,-1,74,78,79,-1,79,75,74,-1,75,79,76,-1,76,72,75,-1,76,79,78,-1,78,77,76,-1,129,133,132,-1,132,128,129,-1,130,134,133,-1,133,129,130,-1,131,135,134,-1,134,130,131,-1,128,132,135,-1,135,131,128,-1,133,137,136,-1,136,132,133,-1,134,138,137,-1,137,133,134,-1,135,139,138,-1,138,134,135,-1,132,136,139,-1,139,135,132,-1,137,141,140,-1,140,136,137,-1,138,142,141,-1,141,137,138,-1,139,143,142,-1,142,138,139,-1,136,140,143,-1,143,139,136,-1,141,145,144,-1,144,140,141,-1,142,146,145,-1,145,141,142,-1,143,147,146,-1,146,142,143,-1,140,144,147,-1,147,143,140,-1,145,146,147,-1,147,144,145,-1,148,8,9,-1,9,149,148,-1,149,9,10,-1,10,150,149,-1,150,10,11,-1,11,151,150,-1,151,11,8,-1,8,148,151,-1,152,148,149,-1,149,153,152,-1,153,149,150,-1,150,154,153,-1,154,150,151,-1,151,155,154,-1,155,151,148,-1,148,152,155,-1,156,152,153,-1,153,157,156,-1,158,154,155,-1,155,159,158,-1,160,156,157,-1,157,161,160,-1,161,157,158,-1,158,162,161,-1,162,158,159,-1,159,163,162,-1,163,159,156,-1,156,160,163,-1,164,160,161,-1,161,165,164,-1,165,161,162,-1,162,166,165,-1,166,162,163,-1,163,167,166,-1,167,163,160,-1,160,164,167,-1,153,176,177,-1,177,157,153,-1,157,177,178,-1,178,158,157,-1,158,178,179,-1,179,154,158,-1,154,179,176,-1,176,153,154,-1,176,180,181,-1,181,177,176,-1,177,181,182,-1,182,178,177,-1,178,182,183,-1,183,179,178,-1,179,183,180,-1,180,176,179,-1,180,184,185,-1,185,181,180,-1,181,185,186,-1,186,182,181,-1,182,186,187,-1,187,183,182,-1,183,187,184,-1,184,180,183,-1,184,188,189,-1,189,185,184,-1,185,189,190,-1,190,186,185,-1,186,190,191,-1,191,187,186,-1,187,191,188,-1,188,184,187,-1,152,156,201,-1,201,200,152,-1,156,159,202,-1,202,201,156,-1,159,155,203,-1,203,202,159,-1,155,152,200,-1,200,203,155,-1,201,205,204,-1,204,200,201,-1,202,206,205,-1,205,201,202,-1,203,207,206,-1,206,202,203,-1,200,204,207,-1,207,203,200,-1,205,209,208,-1,208,204,205,-1,206,210,209,-1,209,205,206,-1,207,211,210,-1,210,206,207,-1,204,208,211,-1,211,207,204,-1,209,213,212,-1,212,208,209,-1,210,214,213,-1,213,209,210,-1,211,215,214,-1,214,210,211,-1,208,212,215,-1,215,211,208,-1,172,164,165,-1,165,173,172,-1,173,165,166,-1,166,174,173,-1,174,166,167,-1,167,175,174,-1,175,167,164,-1,164,172,175,-1,168,172,173,-1,173,169,168,-1,169,173,174,-1,174,170,169,-1,170,174,175,-1,175,171,170,-1,171,175,172,-1,172,168,171,-1,171,168,169,-1,169,170,171,-1,188,192,193,-1,193,189,188,-1,189,193,194,-1,194,190,189,-1,190,194,195,-1,195,191,190,-1,191,195,192,-1,192,188,191,-1,192,196,197,-1,197,193,192,-1,193,197,198,-1,198,194,193,-1,194,198,199,-1,199,195,194,-1,195,199,196,-1,196,192,195,-1,196,199,198,-1,198,197,196,-1,213,217,216,-1,216,212,213,-1,214,218,217,-1,217,213,214,-1,215,219,218,-1,218,214,215,-1,212,216,219,-1,219,215,212,-1,217,221,220,-1,220,216,217,-1,218,222,221,-1,221,217,218,-1,219,223,222,-1,222,218,219,-1,216,220,223,-1,223,219,216,-1,221,222,223,-1,223,220,221,-1]
Coordinate148 = x3d.Coordinate()
Coordinate148.USE = "SKINCOORD"

IndexedLineSet147.coord = Coordinate148

Shape144.geometry = IndexedLineSet147

Group123.children.append(Shape144)

HAnimHumanoid37.skin.append(Group123)
HAnimSite149 = x3d.HAnimSite()
HAnimSite149.name = "BoxMan_view"
HAnimSite149.DEF = "boxman_BoxMan_view"
Viewpoint150 = x3d.Viewpoint()
Viewpoint150.DEF = "Inclined_View"
Viewpoint150.description = "Inclined View"
Viewpoint150.orientation = [0,1,0,0.78]
Viewpoint150.position = [2,0.9,2]

HAnimSite149.children.append(Viewpoint150)
Viewpoint151 = x3d.Viewpoint()
Viewpoint151.DEF = "Front_View"
Viewpoint151.description = "Front View"
Viewpoint151.position = [0,1,3]

HAnimSite149.children.append(Viewpoint151)
Viewpoint152 = x3d.Viewpoint()
Viewpoint152.DEF = "Right_View"
Viewpoint152.description = "Right-side View"
Viewpoint152.orientation = [0,1,0,-1.57]
Viewpoint152.position = [-3,1,0]

HAnimSite149.children.append(Viewpoint152)
Viewpoint153 = x3d.Viewpoint()
Viewpoint153.DEF = "Left_View"
Viewpoint153.description = "Left-side View"
Viewpoint153.orientation = [0,1,0,1.57]
Viewpoint153.position = [3,1,0]

HAnimSite149.children.append(Viewpoint153)
Viewpoint154 = x3d.Viewpoint()
Viewpoint154.DEF = "Top_View"
Viewpoint154.description = "Top View"
Viewpoint154.orientation = [1,0,0,-1.57]
Viewpoint154.position = [0,3,0]

HAnimSite149.children.append(Viewpoint154)

HAnimHumanoid37.viewpoints.append(HAnimSite149)
HAnimJoint155 = x3d.HAnimJoint()
HAnimJoint155.USE = "boxman_humanoid_root"

HAnimHumanoid37.joints.append(HAnimJoint155)
HAnimJoint156 = x3d.HAnimJoint()
HAnimJoint156.USE = "boxman_skullbase"

HAnimHumanoid37.joints.append(HAnimJoint156)
HAnimJoint157 = x3d.HAnimJoint()
HAnimJoint157.USE = "boxman_vl5"

HAnimHumanoid37.joints.append(HAnimJoint157)
HAnimJoint158 = x3d.HAnimJoint()
HAnimJoint158.USE = "boxman_l_ankle"

HAnimHumanoid37.joints.append(HAnimJoint158)
HAnimJoint159 = x3d.HAnimJoint()
HAnimJoint159.USE = "boxman_r_ankle"

HAnimHumanoid37.joints.append(HAnimJoint159)
HAnimJoint160 = x3d.HAnimJoint()
HAnimJoint160.USE = "boxman_l_elbow"

HAnimHumanoid37.joints.append(HAnimJoint160)
HAnimJoint161 = x3d.HAnimJoint()
HAnimJoint161.USE = "boxman_r_elbow"

HAnimHumanoid37.joints.append(HAnimJoint161)
HAnimJoint162 = x3d.HAnimJoint()
HAnimJoint162.USE = "boxman_l_hip"

HAnimHumanoid37.joints.append(HAnimJoint162)
HAnimJoint163 = x3d.HAnimJoint()
HAnimJoint163.USE = "boxman_r_hip"

HAnimHumanoid37.joints.append(HAnimJoint163)
HAnimJoint164 = x3d.HAnimJoint()
HAnimJoint164.USE = "boxman_l_knee"

HAnimHumanoid37.joints.append(HAnimJoint164)
HAnimJoint165 = x3d.HAnimJoint()
HAnimJoint165.USE = "boxman_r_knee"

HAnimHumanoid37.joints.append(HAnimJoint165)
HAnimJoint166 = x3d.HAnimJoint()
HAnimJoint166.USE = "boxman_l_midtarsal"

HAnimHumanoid37.joints.append(HAnimJoint166)
HAnimJoint167 = x3d.HAnimJoint()
HAnimJoint167.USE = "boxman_r_midtarsal"

HAnimHumanoid37.joints.append(HAnimJoint167)
HAnimJoint168 = x3d.HAnimJoint()
HAnimJoint168.USE = "boxman_l_shoulder"

HAnimHumanoid37.joints.append(HAnimJoint168)
HAnimJoint169 = x3d.HAnimJoint()
HAnimJoint169.USE = "boxman_r_shoulder"

HAnimHumanoid37.joints.append(HAnimJoint169)
HAnimJoint170 = x3d.HAnimJoint()
HAnimJoint170.USE = "boxman_l_wrist"

HAnimHumanoid37.joints.append(HAnimJoint170)
HAnimJoint171 = x3d.HAnimJoint()
HAnimJoint171.USE = "boxman_r_wrist"

HAnimHumanoid37.joints.append(HAnimJoint171)
HAnimSegment172 = x3d.HAnimSegment()
HAnimSegment172.USE = "boxman_l5"

HAnimHumanoid37.segments.append(HAnimSegment172)
HAnimSegment173 = x3d.HAnimSegment()
HAnimSegment173.USE = "boxman_sacrum"

HAnimHumanoid37.segments.append(HAnimSegment173)
HAnimSegment174 = x3d.HAnimSegment()
HAnimSegment174.USE = "boxman_skull"

HAnimHumanoid37.segments.append(HAnimSegment174)
HAnimSegment175 = x3d.HAnimSegment()
HAnimSegment175.USE = "boxman_l_calf"

HAnimHumanoid37.segments.append(HAnimSegment175)
HAnimSegment176 = x3d.HAnimSegment()
HAnimSegment176.USE = "boxman_r_calf"

HAnimHumanoid37.segments.append(HAnimSegment176)
HAnimSegment177 = x3d.HAnimSegment()
HAnimSegment177.USE = "boxman_l_forearm"

HAnimHumanoid37.segments.append(HAnimSegment177)
HAnimSegment178 = x3d.HAnimSegment()
HAnimSegment178.USE = "boxman_r_forearm"

HAnimHumanoid37.segments.append(HAnimSegment178)
HAnimSegment179 = x3d.HAnimSegment()
HAnimSegment179.USE = "boxman_l_hand"

HAnimHumanoid37.segments.append(HAnimSegment179)
HAnimSegment180 = x3d.HAnimSegment()
HAnimSegment180.USE = "boxman_r_hand"

HAnimHumanoid37.segments.append(HAnimSegment180)
HAnimSegment181 = x3d.HAnimSegment()
HAnimSegment181.USE = "boxman_l_hindfoot"

HAnimHumanoid37.segments.append(HAnimSegment181)
HAnimSegment182 = x3d.HAnimSegment()
HAnimSegment182.USE = "boxman_r_hindfoot"

HAnimHumanoid37.segments.append(HAnimSegment182)
HAnimSegment183 = x3d.HAnimSegment()
HAnimSegment183.USE = "boxman_l_middistal"

HAnimHumanoid37.segments.append(HAnimSegment183)
HAnimSegment184 = x3d.HAnimSegment()
HAnimSegment184.USE = "boxman_r_middistal"

HAnimHumanoid37.segments.append(HAnimSegment184)
HAnimSegment185 = x3d.HAnimSegment()
HAnimSegment185.USE = "boxman_l_thigh"

HAnimHumanoid37.segments.append(HAnimSegment185)
HAnimSegment186 = x3d.HAnimSegment()
HAnimSegment186.USE = "boxman_r_thigh"

HAnimHumanoid37.segments.append(HAnimSegment186)
HAnimSegment187 = x3d.HAnimSegment()
HAnimSegment187.USE = "boxman_l_upperarm"

HAnimHumanoid37.segments.append(HAnimSegment187)
HAnimSegment188 = x3d.HAnimSegment()
HAnimSegment188.USE = "boxman_r_upperarm"

HAnimHumanoid37.segments.append(HAnimSegment188)
HAnimSite189 = x3d.HAnimSite()
HAnimSite189.USE = "boxman_skull_tip"

HAnimHumanoid37.sites.append(HAnimSite189)
HAnimSite190 = x3d.HAnimSite()
HAnimSite190.USE = "boxman_l_hand_tip"

HAnimHumanoid37.sites.append(HAnimSite190)
HAnimSite191 = x3d.HAnimSite()
HAnimSite191.USE = "boxman_r_hand_tip"

HAnimHumanoid37.sites.append(HAnimSite191)
HAnimSite192 = x3d.HAnimSite()
HAnimSite192.USE = "boxman_l_middistal_tip"

HAnimHumanoid37.sites.append(HAnimSite192)
HAnimSite193 = x3d.HAnimSite()
HAnimSite193.USE = "boxman_r_middistal_tip"

HAnimHumanoid37.sites.append(HAnimSite193)

Scene34.children.append(HAnimHumanoid37)
ExternProtoDeclare194 = x3d.ExternProtoDeclare()
ExternProtoDeclare194.name = "LOA1_WalkAnimation"
ExternProtoDeclare194.url = ["LOA1_WalkAnimation.wrl#LOA1_WalkAnimation","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Legacy/LOA1_WalkAnimation.wrl#LOA1_WalkAnimation","http://HAnim.org/Models/HAnim2001/boxman/protos/LOA1WalkAnimation.wrl#LOA1WalkAnimation","LOA1_WalkAnimation.x3d#LOA1_WalkAnimation","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Legacy/LOA1_WalkAnimation.x3d#LOA1_WalkAnimation","http://HAnim.org/Models/HAnim2001/boxman/protos/LOA1WalkAnimation.x3d#LOA1WalkAnimation"]
field195 = x3d.field()
field195.name = "cycleInterval"
field195.accessType = "inputOutput"
field195.type = "SFTime"

ExternProtoDeclare194.field.append(field195)
field196 = x3d.field()
field196.name = "enabled"
field196.accessType = "inputOutput"
field196.type = "SFBool"

ExternProtoDeclare194.field.append(field196)
field197 = x3d.field()
field197.name = "loop"
field197.accessType = "inputOutput"
field197.type = "SFBool"

ExternProtoDeclare194.field.append(field197)
field198 = x3d.field()
field198.name = "startTime"
field198.accessType = "inputOutput"
field198.type = "SFTime"

ExternProtoDeclare194.field.append(field198)
field199 = x3d.field()
field199.name = "stopTime"
field199.accessType = "inputOutput"
field199.type = "SFTime"

ExternProtoDeclare194.field.append(field199)
field200 = x3d.field()
field200.name = "fraction_changed"
field200.accessType = "outputOnly"
field200.type = "SFFloat"

ExternProtoDeclare194.field.append(field200)
field201 = x3d.field()
field201.name = "HumanoidRoot_translation_changed"
field201.accessType = "outputOnly"
field201.type = "SFVec3f"

ExternProtoDeclare194.field.append(field201)
field202 = x3d.field()
field202.name = "HumanoidRoot_rotation_changed"
field202.accessType = "outputOnly"
field202.type = "SFRotation"

ExternProtoDeclare194.field.append(field202)
field203 = x3d.field()
field203.name = "l_hip_rotation_changed"
field203.accessType = "outputOnly"
field203.type = "SFRotation"

ExternProtoDeclare194.field.append(field203)
field204 = x3d.field()
field204.name = "l_knee_rotation_changed"
field204.accessType = "outputOnly"
field204.type = "SFRotation"

ExternProtoDeclare194.field.append(field204)
field205 = x3d.field()
field205.name = "l_ankle_rotation_changed"
field205.accessType = "outputOnly"
field205.type = "SFRotation"

ExternProtoDeclare194.field.append(field205)
field206 = x3d.field()
field206.name = "l_midtarsal_rotation_changed"
field206.accessType = "outputOnly"
field206.type = "SFRotation"

ExternProtoDeclare194.field.append(field206)
field207 = x3d.field()
field207.name = "r_hip_rotation_changed"
field207.accessType = "outputOnly"
field207.type = "SFRotation"

ExternProtoDeclare194.field.append(field207)
field208 = x3d.field()
field208.name = "r_knee_rotation_changed"
field208.accessType = "outputOnly"
field208.type = "SFRotation"

ExternProtoDeclare194.field.append(field208)
field209 = x3d.field()
field209.name = "r_ankle_rotation_changed"
field209.accessType = "outputOnly"
field209.type = "SFRotation"

ExternProtoDeclare194.field.append(field209)
field210 = x3d.field()
field210.name = "r_midtarsal_rotation_changed"
field210.accessType = "outputOnly"
field210.type = "SFRotation"

ExternProtoDeclare194.field.append(field210)
field211 = x3d.field()
field211.name = "vl5_rotation_changed"
field211.accessType = "outputOnly"
field211.type = "SFRotation"

ExternProtoDeclare194.field.append(field211)
field212 = x3d.field()
field212.name = "skullbase_rotation_changed"
field212.accessType = "outputOnly"
field212.type = "SFRotation"

ExternProtoDeclare194.field.append(field212)
field213 = x3d.field()
field213.name = "l_shoulder_rotation_changed"
field213.accessType = "outputOnly"
field213.type = "SFRotation"

ExternProtoDeclare194.field.append(field213)
field214 = x3d.field()
field214.name = "l_elbow_rotation_changed"
field214.accessType = "outputOnly"
field214.type = "SFRotation"

ExternProtoDeclare194.field.append(field214)
field215 = x3d.field()
field215.name = "l_wrist_rotation_changed"
field215.accessType = "outputOnly"
field215.type = "SFRotation"

ExternProtoDeclare194.field.append(field215)
field216 = x3d.field()
field216.name = "r_shoulder_rotation_changed"
field216.accessType = "outputOnly"
field216.type = "SFRotation"

ExternProtoDeclare194.field.append(field216)
field217 = x3d.field()
field217.name = "r_elbow_rotation_changed"
field217.accessType = "outputOnly"
field217.type = "SFRotation"

ExternProtoDeclare194.field.append(field217)
field218 = x3d.field()
field218.name = "r_wrist_rotation_changed"
field218.accessType = "outputOnly"
field218.type = "SFRotation"

ExternProtoDeclare194.field.append(field218)
field219 = x3d.field()
field219.name = "isActive"
field219.accessType = "outputOnly"
field219.type = "SFBool"

ExternProtoDeclare194.field.append(field219)

Scene34.children.append(ExternProtoDeclare194)
ProtoInstance220 = x3d.ProtoInstance()
ProtoInstance220.name = "LOA1_WalkAnimation"
ProtoInstance220.DEF = "ANIMATOR"

Scene34.children.append(ProtoInstance220)
#Animation ROUTEs
ROUTE221 = x3d.ROUTE()
ROUTE221.fromField = "HumanoidRoot_translation_changed"
ROUTE221.fromNode = "ANIMATOR"
ROUTE221.toField = "set_translation"
ROUTE221.toNode = "boxman_humanoid_root"

Scene34.children.append(ROUTE221)
ROUTE222 = x3d.ROUTE()
ROUTE222.fromField = "HumanoidRoot_rotation_changed"
ROUTE222.fromNode = "ANIMATOR"
ROUTE222.toField = "set_rotation"
ROUTE222.toNode = "boxman_humanoid_root"

Scene34.children.append(ROUTE222)
ROUTE223 = x3d.ROUTE()
ROUTE223.fromField = "l_hip_rotation_changed"
ROUTE223.fromNode = "ANIMATOR"
ROUTE223.toField = "set_rotation"
ROUTE223.toNode = "boxman_l_hip"

Scene34.children.append(ROUTE223)
ROUTE224 = x3d.ROUTE()
ROUTE224.fromField = "l_knee_rotation_changed"
ROUTE224.fromNode = "ANIMATOR"
ROUTE224.toField = "set_rotation"
ROUTE224.toNode = "boxman_l_knee"

Scene34.children.append(ROUTE224)
ROUTE225 = x3d.ROUTE()
ROUTE225.fromField = "l_ankle_rotation_changed"
ROUTE225.fromNode = "ANIMATOR"
ROUTE225.toField = "set_rotation"
ROUTE225.toNode = "boxman_l_ankle"

Scene34.children.append(ROUTE225)
ROUTE226 = x3d.ROUTE()
ROUTE226.fromField = "l_midtarsal_rotation_changed"
ROUTE226.fromNode = "ANIMATOR"
ROUTE226.toField = "set_rotation"
ROUTE226.toNode = "boxman_l_midtarsal"

Scene34.children.append(ROUTE226)
ROUTE227 = x3d.ROUTE()
ROUTE227.fromField = "r_hip_rotation_changed"
ROUTE227.fromNode = "ANIMATOR"
ROUTE227.toField = "set_rotation"
ROUTE227.toNode = "boxman_r_hip"

Scene34.children.append(ROUTE227)
ROUTE228 = x3d.ROUTE()
ROUTE228.fromField = "r_knee_rotation_changed"
ROUTE228.fromNode = "ANIMATOR"
ROUTE228.toField = "set_rotation"
ROUTE228.toNode = "boxman_r_knee"

Scene34.children.append(ROUTE228)
ROUTE229 = x3d.ROUTE()
ROUTE229.fromField = "r_ankle_rotation_changed"
ROUTE229.fromNode = "ANIMATOR"
ROUTE229.toField = "set_rotation"
ROUTE229.toNode = "boxman_r_ankle"

Scene34.children.append(ROUTE229)
ROUTE230 = x3d.ROUTE()
ROUTE230.fromField = "r_midtarsal_rotation_changed"
ROUTE230.fromNode = "ANIMATOR"
ROUTE230.toField = "set_rotation"
ROUTE230.toNode = "boxman_r_midtarsal"

Scene34.children.append(ROUTE230)
ROUTE231 = x3d.ROUTE()
ROUTE231.fromField = "vl5_rotation_changed"
ROUTE231.fromNode = "ANIMATOR"
ROUTE231.toField = "set_rotation"
ROUTE231.toNode = "boxman_vl5"

Scene34.children.append(ROUTE231)
ROUTE232 = x3d.ROUTE()
ROUTE232.fromField = "skullbase_rotation_changed"
ROUTE232.fromNode = "ANIMATOR"
ROUTE232.toField = "set_rotation"
ROUTE232.toNode = "boxman_skullbase"

Scene34.children.append(ROUTE232)
ROUTE233 = x3d.ROUTE()
ROUTE233.fromField = "l_shoulder_rotation_changed"
ROUTE233.fromNode = "ANIMATOR"
ROUTE233.toField = "set_rotation"
ROUTE233.toNode = "boxman_l_shoulder"

Scene34.children.append(ROUTE233)
ROUTE234 = x3d.ROUTE()
ROUTE234.fromField = "l_elbow_rotation_changed"
ROUTE234.fromNode = "ANIMATOR"
ROUTE234.toField = "set_rotation"
ROUTE234.toNode = "boxman_l_elbow"

Scene34.children.append(ROUTE234)
ROUTE235 = x3d.ROUTE()
ROUTE235.fromField = "l_wrist_rotation_changed"
ROUTE235.fromNode = "ANIMATOR"
ROUTE235.toField = "set_rotation"
ROUTE235.toNode = "boxman_l_wrist"

Scene34.children.append(ROUTE235)
ROUTE236 = x3d.ROUTE()
ROUTE236.fromField = "r_shoulder_rotation_changed"
ROUTE236.fromNode = "ANIMATOR"
ROUTE236.toField = "set_rotation"
ROUTE236.toNode = "boxman_r_shoulder"

Scene34.children.append(ROUTE236)
ROUTE237 = x3d.ROUTE()
ROUTE237.fromField = "r_elbow_rotation_changed"
ROUTE237.fromNode = "ANIMATOR"
ROUTE237.toField = "set_rotation"
ROUTE237.toNode = "boxman_r_elbow"

Scene34.children.append(ROUTE237)
ROUTE238 = x3d.ROUTE()
ROUTE238.fromField = "r_wrist_rotation_changed"
ROUTE238.fromNode = "ANIMATOR"
ROUTE238.toField = "set_rotation"
ROUTE238.toNode = "boxman_r_wrist"

Scene34.children.append(ROUTE238)
Script239 = x3d.Script()
Script239.DEF = "ENGINE"
Script239.directOutput = True
Script239.url = ["BoxMan3.js","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Legacy/BoxMan3.js"]
field240 = x3d.field()
field240.name = "update"
field240.accessType = "inputOnly"
field240.type = "SFRotation"

Script239.field.append(field240)
field241 = x3d.field()
field241.name = "humanoid"
field241.accessType = "initializeOnly"
field241.type = "SFNode"
HAnimHumanoid242 = x3d.HAnimHumanoid()
HAnimHumanoid242.USE = "boxman_Humanoid"

field241.children.append(HAnimHumanoid242)

Script239.field.append(field241)
field243 = x3d.field()
field243.name = "coordList"
field243.accessType = "initializeOnly"
field243.type = "MFVec3f"

Script239.field.append(field243)
field244 = x3d.field()
field244.name = "joint"
field244.accessType = "initializeOnly"
field244.type = "SFNode"
#initialization node (if any) goes here

Script239.field.append(field244)
field245 = x3d.field()
field245.name = "translation"
field245.accessType = "initializeOnly"
field245.type = "SFVec3f"
field245.value = [0,0,0]

Script239.field.append(field245)
field246 = x3d.field()
field246.name = "rotation"
field246.accessType = "initializeOnly"
field246.type = "SFRotation"
field246.value = [1,0,0,0]

Script239.field.append(field246)
field247 = x3d.field()
field247.name = "scale"
field247.accessType = "initializeOnly"
field247.type = "SFVec3f"
field247.value = [1,1,1]

Script239.field.append(field247)

Scene34.children.append(Script239)
#Trigger calculation after each animation change
#<ROUTE fromField='rotation_changed' fromNode='boxman_r_wrist' toField='update' toNode='ENGINE'/>

X3D0.Scene = Scene34
f = open("././BoxMan3_RoundTrip.x3d", "w")
f.write(X3D0.XML())
f.close()
