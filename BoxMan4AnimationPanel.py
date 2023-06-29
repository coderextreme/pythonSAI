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
meta3.content = "BoxMan4AnimationPanel.x3d"

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.name = "description"
meta4.content = "A Seamless VRML Human, demonstrating the HAnim 2001 Specification, animation panel shows multiple behaviors."

head1.children.append(meta4)
meta5 = x3d.meta()
meta5.name = "creator"
meta5.content = "Joe Williams and James Smith - james@vapourtech.com"

head1.children.append(meta5)
meta6 = x3d.meta()
meta6.name = "translator"
meta6.content = "Joe Williams and Don Brutzman"

head1.children.append(meta6)
meta7 = x3d.meta()
meta7.name = "generator"
meta7.content = ".x3d to .x3d translation used BS Contact Geo 8.203"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.name = "created"
meta8.content = "1 March 2001"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "revision"
meta9.content = "12 January 2017"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "translated"
meta10.content = "14 January 2017"

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.name = "modified"
meta11.content = "8 January 2023"

head1.children.append(meta11)
meta12 = x3d.meta()
meta12.name = "Image"
meta12.content = "BoxManAnimationPanelInclined.png"

head1.children.append(meta12)
meta13 = x3d.meta()
meta13.name = "MovingImage"
meta13.content = "BoxManAnimationPanel.mp4"

head1.children.append(meta13)
meta14 = x3d.meta()
meta14.name = "MovingImage"
meta14.content = "https://www.youtube.com/watch?v=8tI83Rtg_DU"

head1.children.append(meta14)
meta15 = x3d.meta()
meta15.name = "reference"
meta15.content = "https://twitter.com/Web3DConsortium/status/820638047523913728"

head1.children.append(meta15)
meta16 = x3d.meta()
meta16.name = "reference"
meta16.content = "https://twitter.com/Web3DConsortium/status/820642726009978881"

head1.children.append(meta16)
meta17 = x3d.meta()
meta17.name = "reference"
meta17.content = "http://HAnim.org"

head1.children.append(meta17)
meta18 = x3d.meta()
meta18.name = "reference"
meta18.content = "../Legacy/originals/boxman.wrl"

head1.children.append(meta18)
meta19 = x3d.meta()
meta19.name = "TODO"
meta19.content = "InstantReality Forum Issue: InstantReality is ignoring the Viewpoint nodes in the topmost HAnimSite. http://forum.instantreality.org"

head1.children.append(meta19)
meta20 = x3d.meta()
meta20.name = "reference"
meta20.content = "BoxMan4.x3d"

head1.children.append(meta20)
meta21 = x3d.meta()
meta21.name = "reference"
meta21.content = "http://HAnim.org/Models/HAnim2001/boxman"

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
meta31.content = "https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Legacy/BoxMan4AnimationPanel.x3d"

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
WorldInfo35.title = "BoxMan - A Seamless VRML Human"

Scene34.children.append(WorldInfo35)
Background36 = x3d.Background()
Background36.groundColor = [0.6,0.6,0.6]
Background36.skyColor = [0.75,0.75,0.75]

Scene34.children.append(Background36)
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
#Coordinate DEF='SKINCOORD2' containerField='skinCoord' point='-0.05 1 0.05 0.05 1 0.05 0.03 0.97 -0.1 -0.03 0.97 -0.1 0.03 0.94 -0.075 -0.03 0.94 -0.075 0 0.92 0 0 0.94 0.03 -0.12 1.06 0.05 0.12 1.06 0.05 0.12 1.06 -0.1 -0.12 1.06 -0.1 0.0456 0.9364 0.05 0.1456 0.9364 0.05 0.1456 0.9364 -0.05 0.0456 0.9364 -0.05 0.0456 0.9 0.05 0.1456 0.9 0.05 0.1456 0.9 -0.05 0.0456 0.9 -0.05 0.0456 0.8 0.05 0.1456 0.8 0.05 0.1456 0.8 -0.05 0.0456 0.8 -0.05 0.0456 0.7 0.05 0.1456 0.7 0.05 0.1456 0.7 -0.05 0.0456 0.7 -0.05 0.0456 0.6 0.05 0.1456 0.6 0.05 0.1456 0.6 -0.05 0.0456 0.6 -0.05 0.0456 0.55 0.05 0.1456 0.55 0.05 0.1456 0.55 -0.05 0.0456 0.55 -0.05 0.0456 0.52 0.05 0.1456 0.52 0.05 0.1456 0.52 -0.05 0.0456 0.52 -0.05 0.0456 0.5 0.05 0.1456 0.5 0.05 0.1456 0.5 -0.05 0.0456 0.5 -0.05 0.0454 0.43 0.045 0.1454 0.43 0.045 0.1454 0.43 -0.055 0.0454 0.43 -0.055 0.0452 0.36 0.04 0.1452 0.36 0.04 0.1452 0.36 -0.06 0.0452 0.36 -0.06 0.045 0.29 0.035 0.145 0.29 0.035 0.145 0.29 -0.065 0.045 0.29 -0.065 0.0448 0.21 0.03 0.1448 0.21 0.03 0.1448 0.21 -0.07 0.0448 0.21 -0.07 0.0446 0.1262 0.025 0.1446 0.1262 0.025 0.1446 0.1262 -0.075 0.0446 0.1262 -0.075 0.0446 0.0702038 0.02464698 0.1446 0.0702038 0.02464698 0.1446 0.006264479 -0.08360368 0.0446 0.006264479 -0.08360368 0.0446 0.046587 0.05407905 0.1446 0.046587 0.05407905 0.1446 -0.009224742 0.0474844 0.0446 -0.009224742 0.0474844 0.0446 0.04306673 0.0838718 0.1446 0.04306673 0.0838718 0.1446 -0.01274502 0.07727715 0.0446 -0.01274502 0.07727715 0.0446 0.03069882 0.1885436 0.1446 0.03069882 0.1885436 0.1446 -0.02511293 0.181949 0.0446 -0.02511293 0.181949 -0.0456 0.9861611 0.004881433 -0.1456 0.9861611 0.004881433 -0.1456 0.8866388 -0.004881474 -0.0456 0.8866388 -0.004881474 -0.0456 0.9826074 0.04110757 -0.1456 0.9826074 0.04110757 -0.1456 0.8830851 0.03134466 -0.0456 0.8830851 0.03134466 -0.0456 0.9728445 0.1406298 -0.1456 0.9728445 0.1406298 -0.1456 0.8733222 0.1308669 -0.0456 0.8733222 0.1308669 -0.0456 0.9630816 0.2401521 -0.1456 0.9630816 0.2401521 -0.1456 0.8635593 0.2303892 -0.0456 0.8635593 0.2303892 -0.0456 0.9533187 0.3396744 -0.1456 0.9533187 0.3396744 -0.1456 0.8537964 0.3299115 -0.0456 0.8537964 0.3299115 -0.0456 0.9484373 0.3894355 -0.1456 0.9484373 0.3894355 -0.1456 0.848915 0.3796726 -0.0456 0.848915 0.3796726 -0.0456 0.94468 0.4147483 -0.1456 0.94468 0.4147483 -0.1456 0.8450468 0.4134411 -0.0456 0.8450468 0.4134411 -0.0456 0.9444185 0.4346749 -0.1456 0.9444185 0.4346749 -0.1456 0.8447853 0.4333678 -0.0456 0.8447853 0.4333678 -0.0454 0.9452982 0.5003315 -0.1454 0.9452982 0.5003315 -0.1454 0.8455541 0.5074801 -0.0454 0.8455541 0.5074801 -0.0452 0.945315 0.5705098 -0.1452 0.945315 0.5705098 -0.1452 0.8455709 0.5776584 -0.0452 0.8455709 0.5776584 -0.045 0.9453319 0.6406881 -0.145 0.9453319 0.6406881 -0.145 0.8455877 0.6478368 -0.045 0.8455877 0.6478368 -0.0448 0.9460636 0.7208409 -0.1448 0.9460636 0.7208409 -0.1448 0.8463194 0.7279896 -0.0448 0.8463194 0.7279896 -0.0446 0.947067 0.8047839 -0.1446 0.947067 0.8047839 -0.1446 0.8473228 0.8119326 -0.0446 0.8473228 0.8119326 -0.0446 0.9507178 0.8606621 -0.1446 0.9507178 0.8606621 -0.1446 0.847315 0.9321763 -0.0446 0.847315 0.9321763 -0.0446 0.9817629 0.8821145 -0.1446 0.9817629 0.8821145 -0.1446 0.9791749 0.9382548 -0.0446 0.9791749 0.9382548 -0.0446 1.011731 0.883496 -0.1446 1.011731 0.883496 -0.1446 1.009143 0.9396363 -0.0446 1.009143 0.9396363 -0.0446 1.117019 0.8883496 -0.1446 1.117019 0.8883496 -0.1446 1.114431 0.94449 -0.0446 1.114431 0.94449 -0.12 1.1 0.05 0.12 1.1 0.05 0.12 1.1 -0.1 -0.12 1.1 -0.1 -0.14 1.42 0.045 0.14 1.42 0.045 0.14 1.42 -0.09 -0.14 1.42 -0.09 -0.24 1.52 0.035 0.24 1.52 0.035 0.24 1.52 -0.09 -0.24 1.52 -0.09 -0.05 1.56 0.03 0.05 1.56 0.03 0.05 1.56 -0.06 -0.05 1.56 -0.06 -0.05 1.6 0.06 0.05 1.6 0.06 0.05 1.62 -0.03 -0.05 1.62 -0.03 -0.07 1.781247 0.1236818 0.07 1.781247 0.1236818 0.07 1.77377 -0.03614335 -0.07 1.77377 -0.03614335 -0.07 1.604441 0.1319535 0.07 1.604441 0.1319535 0.07 1.656898 -0.03067561 -0.07 1.656898 -0.03067561 0.2016854 1.406894 0.015 0.2023709 1.520029 0.015 0.2023709 1.520029 -0.075 0.2016854 1.406894 -0.075 0.3774735 1.243191 -0.025 0.4201562 1.28536 -0.025 0.4201562 1.28536 -0.085 0.3774735 1.243191 -0.085 0.4055858 1.214736 -0.025 0.4482685 1.256904 -0.025 0.4482685 1.256904 -0.085 0.4055858 1.214736 -0.085 0.5743457 1.058147 -0.05 0.6028008 1.086259 -0.05 0.6028008 1.086259 -0.09 0.5743457 1.058147 -0.09 0.6024581 1.029692 -0.02 0.6309132 1.057804 -0.02 0.6309132 1.057804 -0.1 0.6024581 1.029692 -0.1 0.7236224 0.9070502 -0.02 0.7520775 0.9351625 -0.02 0.7520775 0.9351625 -0.1 0.7236224 0.9070502 -0.1 -0.2016854 1.406894 0.015 -0.2023709 1.520029 0.015 -0.2023709 1.520029 -0.075 -0.2016854 1.406894 -0.075 -0.3774735 1.243191 -0.025 -0.4201562 1.28536 -0.025 -0.4201562 1.28536 -0.085 -0.3774735 1.243191 -0.085 -0.4055858 1.214736 -0.025 -0.4482685 1.256904 -0.025 -0.4482685 1.256904 -0.085 -0.4055858 1.214736 -0.085 -0.5743457 1.058147 -0.05 -0.6028008 1.086259 -0.05 -0.6028008 1.086259 -0.09 -0.5743457 1.058147 -0.09 -0.6024581 1.029692 -0.02 -0.6309132 1.057804 -0.02 -0.6309132 1.057804 -0.1 -0.6024581 1.029692 -0.1 -0.7236224 0.9070502 -0.02 -0.7520775 0.9351625 -0.02 -0.7520775 0.9351625 -0.1 -0.7236224 0.9070502 -0.1'/
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
Viewpoint152.DEF = "Best_View"
Viewpoint152.description = "Right-side View"
Viewpoint152.orientation = [0,1,0,-1.57]
Viewpoint152.position = [-3,1,0]

HAnimSite149.children.append(Viewpoint152)
Viewpoint153 = x3d.Viewpoint()
Viewpoint153.DEF = "Side_View"
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
HAnimJoint158.USE = "boxman_r_ankle"

HAnimHumanoid37.joints.append(HAnimJoint158)
HAnimJoint159 = x3d.HAnimJoint()
HAnimJoint159.USE = "boxman_l_ankle"

HAnimHumanoid37.joints.append(HAnimJoint159)
HAnimJoint160 = x3d.HAnimJoint()
HAnimJoint160.USE = "boxman_r_elbow"

HAnimHumanoid37.joints.append(HAnimJoint160)
HAnimJoint161 = x3d.HAnimJoint()
HAnimJoint161.USE = "boxman_l_elbow"

HAnimHumanoid37.joints.append(HAnimJoint161)
HAnimJoint162 = x3d.HAnimJoint()
HAnimJoint162.USE = "boxman_r_hip"

HAnimHumanoid37.joints.append(HAnimJoint162)
HAnimJoint163 = x3d.HAnimJoint()
HAnimJoint163.USE = "boxman_l_hip"

HAnimHumanoid37.joints.append(HAnimJoint163)
HAnimJoint164 = x3d.HAnimJoint()
HAnimJoint164.USE = "boxman_r_knee"

HAnimHumanoid37.joints.append(HAnimJoint164)
HAnimJoint165 = x3d.HAnimJoint()
HAnimJoint165.USE = "boxman_l_knee"

HAnimHumanoid37.joints.append(HAnimJoint165)
HAnimJoint166 = x3d.HAnimJoint()
HAnimJoint166.USE = "boxman_r_midtarsal"

HAnimHumanoid37.joints.append(HAnimJoint166)
HAnimJoint167 = x3d.HAnimJoint()
HAnimJoint167.USE = "boxman_l_midtarsal"

HAnimHumanoid37.joints.append(HAnimJoint167)
HAnimJoint168 = x3d.HAnimJoint()
HAnimJoint168.USE = "boxman_r_shoulder"

HAnimHumanoid37.joints.append(HAnimJoint168)
HAnimJoint169 = x3d.HAnimJoint()
HAnimJoint169.USE = "boxman_l_shoulder"

HAnimHumanoid37.joints.append(HAnimJoint169)
HAnimJoint170 = x3d.HAnimJoint()
HAnimJoint170.USE = "boxman_r_wrist"

HAnimHumanoid37.joints.append(HAnimJoint170)
HAnimJoint171 = x3d.HAnimJoint()
HAnimJoint171.USE = "boxman_l_wrist"

HAnimHumanoid37.joints.append(HAnimJoint171)
HAnimSegment172 = x3d.HAnimSegment()
HAnimSegment172.USE = "boxman_sacrum"

HAnimHumanoid37.segments.append(HAnimSegment172)
HAnimSegment173 = x3d.HAnimSegment()
HAnimSegment173.USE = "boxman_l5"

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
Group194 = x3d.Group()
Group194.DEF = "StopAnimation"
TimeSensor195 = x3d.TimeSensor()
TimeSensor195.DEF = "StopTimer"
TimeSensor195.cycleInterval = 5.73
TimeSensor195.loop = True

Group194.children.append(TimeSensor195)
PositionInterpolator196 = x3d.PositionInterpolator()
PositionInterpolator196.DEF = "Stop_humanoid_root_TranslationInterpolator"
PositionInterpolator196.key = [0,0.5,1]
PositionInterpolator196.keyValue = (0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000)

Group194.children.append(PositionInterpolator196)
OrientationInterpolator197 = x3d.OrientationInterpolator()
OrientationInterpolator197.DEF = "Stop_humanoid_root_RotationInterpolator"
OrientationInterpolator197.key = [0,0.5,1]
OrientationInterpolator197.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator197)
OrientationInterpolator198 = x3d.OrientationInterpolator()
OrientationInterpolator198.DEF = "Stop_sacroiliac_RotationInterpolator"
OrientationInterpolator198.key = [0,0.5,1]
OrientationInterpolator198.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator198)
OrientationInterpolator199 = x3d.OrientationInterpolator()
OrientationInterpolator199.DEF = "Stop_l_hip_RotationInterpolator"
OrientationInterpolator199.key = [0,0.5,1]
OrientationInterpolator199.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator199)
OrientationInterpolator200 = x3d.OrientationInterpolator()
OrientationInterpolator200.DEF = "Stop_l_knee_RotationInterpolator"
OrientationInterpolator200.key = [0,0.5,1]
OrientationInterpolator200.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator200)
OrientationInterpolator201 = x3d.OrientationInterpolator()
OrientationInterpolator201.DEF = "Stop_l_ankle_RotationInterpolator"
OrientationInterpolator201.key = [0,0.5,1]
OrientationInterpolator201.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator201)
OrientationInterpolator202 = x3d.OrientationInterpolator()
OrientationInterpolator202.DEF = "Stop_l_subtalar_RotationInterpolator"
OrientationInterpolator202.key = [0,0.5,1]
OrientationInterpolator202.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator202)
OrientationInterpolator203 = x3d.OrientationInterpolator()
OrientationInterpolator203.DEF = "Stop_l_midtarsal_RotationInterpolator"
OrientationInterpolator203.key = [0,0.5,1]
OrientationInterpolator203.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator203)
OrientationInterpolator204 = x3d.OrientationInterpolator()
OrientationInterpolator204.DEF = "Stop_l_metatarsal_RotationInterpolator"
OrientationInterpolator204.key = [0,0.5,1]
OrientationInterpolator204.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator204)
OrientationInterpolator205 = x3d.OrientationInterpolator()
OrientationInterpolator205.DEF = "Stop_r_hip_RotationInterpolator"
OrientationInterpolator205.key = [0,0.5,1]
OrientationInterpolator205.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator205)
OrientationInterpolator206 = x3d.OrientationInterpolator()
OrientationInterpolator206.DEF = "Stop_r_knee_RotationInterpolator"
OrientationInterpolator206.key = [0,0.5,1]
OrientationInterpolator206.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator206)
OrientationInterpolator207 = x3d.OrientationInterpolator()
OrientationInterpolator207.DEF = "Stop_r_ankle_RotationInterpolator"
OrientationInterpolator207.key = [0,0.5,1]
OrientationInterpolator207.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator207)
OrientationInterpolator208 = x3d.OrientationInterpolator()
OrientationInterpolator208.DEF = "Stop_r_subtalar_RotationInterpolator"
OrientationInterpolator208.key = [0,0.5,1]
OrientationInterpolator208.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator208)
OrientationInterpolator209 = x3d.OrientationInterpolator()
OrientationInterpolator209.DEF = "Stop_r_midtarsal_RotationInterpolator"
OrientationInterpolator209.key = [0,0.5,1]
OrientationInterpolator209.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator209)
OrientationInterpolator210 = x3d.OrientationInterpolator()
OrientationInterpolator210.DEF = "Stop_r_metatarsal_RotationInterpolator"
OrientationInterpolator210.key = [0,0.5,1]
OrientationInterpolator210.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator210)
OrientationInterpolator211 = x3d.OrientationInterpolator()
OrientationInterpolator211.DEF = "Stop_vl5_RotationInterpolator"
OrientationInterpolator211.key = [0,0.5,1]
OrientationInterpolator211.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator211)
OrientationInterpolator212 = x3d.OrientationInterpolator()
OrientationInterpolator212.DEF = "Stop_vl4_RotationInterpolator"
OrientationInterpolator212.key = [0,0.5,1]
OrientationInterpolator212.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator212)
OrientationInterpolator213 = x3d.OrientationInterpolator()
OrientationInterpolator213.DEF = "Stop_vl3_RotationInterpolator"
OrientationInterpolator213.key = [0,0.5,1]
OrientationInterpolator213.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator213)
OrientationInterpolator214 = x3d.OrientationInterpolator()
OrientationInterpolator214.DEF = "Stop_vl2_RotationInterpolator"
OrientationInterpolator214.key = [0,0.5,1]
OrientationInterpolator214.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator214)
OrientationInterpolator215 = x3d.OrientationInterpolator()
OrientationInterpolator215.DEF = "Stop_vl1_RotationInterpolator"
OrientationInterpolator215.key = [0,0.5,1]
OrientationInterpolator215.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator215)
OrientationInterpolator216 = x3d.OrientationInterpolator()
OrientationInterpolator216.DEF = "Stop_vt12_RotationInterpolator"
OrientationInterpolator216.key = [0,0.5,1]
OrientationInterpolator216.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator216)
OrientationInterpolator217 = x3d.OrientationInterpolator()
OrientationInterpolator217.DEF = "Stop_vt11_RotationInterpolator"
OrientationInterpolator217.key = [0,0.5,1]
OrientationInterpolator217.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator217)
OrientationInterpolator218 = x3d.OrientationInterpolator()
OrientationInterpolator218.DEF = "Stop_vt10_RotationInterpolator"
OrientationInterpolator218.key = [0,0.5,1]
OrientationInterpolator218.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator218)
OrientationInterpolator219 = x3d.OrientationInterpolator()
OrientationInterpolator219.DEF = "Stop_vt9_RotationInterpolator"
OrientationInterpolator219.key = [0,0.5,1]
OrientationInterpolator219.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator219)
OrientationInterpolator220 = x3d.OrientationInterpolator()
OrientationInterpolator220.DEF = "Stop_vt8_RotationInterpolator"
OrientationInterpolator220.key = [0,0.5,1]
OrientationInterpolator220.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator220)
OrientationInterpolator221 = x3d.OrientationInterpolator()
OrientationInterpolator221.DEF = "Stop_vt7_RotationInterpolator"
OrientationInterpolator221.key = [0,0.5,1]
OrientationInterpolator221.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator221)
OrientationInterpolator222 = x3d.OrientationInterpolator()
OrientationInterpolator222.DEF = "Stop_vt6_RotationInterpolator"
OrientationInterpolator222.key = [0,0.5,1]
OrientationInterpolator222.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator222)
OrientationInterpolator223 = x3d.OrientationInterpolator()
OrientationInterpolator223.DEF = "Stop_vt5_RotationInterpolator"
OrientationInterpolator223.key = [0,0.5,1]
OrientationInterpolator223.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator223)
OrientationInterpolator224 = x3d.OrientationInterpolator()
OrientationInterpolator224.DEF = "Stop_vt4_RotationInterpolator"
OrientationInterpolator224.key = [0,0.5,1]
OrientationInterpolator224.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator224)
OrientationInterpolator225 = x3d.OrientationInterpolator()
OrientationInterpolator225.DEF = "Stop_vt3_RotationInterpolator"
OrientationInterpolator225.key = [0,0.5,1]
OrientationInterpolator225.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator225)
OrientationInterpolator226 = x3d.OrientationInterpolator()
OrientationInterpolator226.DEF = "Stop_vt2_RotationInterpolator"
OrientationInterpolator226.key = [0,0.5,1]
OrientationInterpolator226.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator226)
OrientationInterpolator227 = x3d.OrientationInterpolator()
OrientationInterpolator227.DEF = "Stop_vt1_RotationInterpolator"
OrientationInterpolator227.key = [0,0.5,1]
OrientationInterpolator227.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator227)
OrientationInterpolator228 = x3d.OrientationInterpolator()
OrientationInterpolator228.DEF = "Stop_vc7_RotationInterpolator"
OrientationInterpolator228.key = [0,0.5,1]
OrientationInterpolator228.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator228)
OrientationInterpolator229 = x3d.OrientationInterpolator()
OrientationInterpolator229.DEF = "Stop_vc6_RotationInterpolator"
OrientationInterpolator229.key = [0,0.5,1]
OrientationInterpolator229.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator229)
OrientationInterpolator230 = x3d.OrientationInterpolator()
OrientationInterpolator230.DEF = "Stop_vc5_RotationInterpolator"
OrientationInterpolator230.key = [0,0.5,1]
OrientationInterpolator230.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator230)
OrientationInterpolator231 = x3d.OrientationInterpolator()
OrientationInterpolator231.DEF = "Stop_vc4_RotationInterpolator"
OrientationInterpolator231.key = [0,0.5,1]
OrientationInterpolator231.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator231)
OrientationInterpolator232 = x3d.OrientationInterpolator()
OrientationInterpolator232.DEF = "Stop_vc3_RotationInterpolator"
OrientationInterpolator232.key = [0,0.5,1]
OrientationInterpolator232.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator232)
OrientationInterpolator233 = x3d.OrientationInterpolator()
OrientationInterpolator233.DEF = "Stop_vc2_RotationInterpolator"
OrientationInterpolator233.key = [0,0.5,1]
OrientationInterpolator233.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator233)
OrientationInterpolator234 = x3d.OrientationInterpolator()
OrientationInterpolator234.DEF = "Stop_vc1_RotationInterpolator"
OrientationInterpolator234.key = [0,0.5,1]
OrientationInterpolator234.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator234)
OrientationInterpolator235 = x3d.OrientationInterpolator()
OrientationInterpolator235.DEF = "Stop_skullbase_RotationInterpolator"
OrientationInterpolator235.key = [0,0.5,1]
OrientationInterpolator235.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator235)
OrientationInterpolator236 = x3d.OrientationInterpolator()
OrientationInterpolator236.DEF = "Stop_l_eyeball_joint_RotationInterpolator"
OrientationInterpolator236.key = [0,0.5,1]
OrientationInterpolator236.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator236)
OrientationInterpolator237 = x3d.OrientationInterpolator()
OrientationInterpolator237.DEF = "Stop_r_eyeball_joint_RotationInterpolator"
OrientationInterpolator237.key = [0,0.5,1]
OrientationInterpolator237.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator237)
OrientationInterpolator238 = x3d.OrientationInterpolator()
OrientationInterpolator238.DEF = "Stop_l_sternoclavicular_RotationInterpolator"
OrientationInterpolator238.key = [0,0.5,1]
OrientationInterpolator238.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator238)
OrientationInterpolator239 = x3d.OrientationInterpolator()
OrientationInterpolator239.DEF = "Stop_l_acromioclavicular_RotationInterpolator"
OrientationInterpolator239.key = [0,0.5,1]
OrientationInterpolator239.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator239)
OrientationInterpolator240 = x3d.OrientationInterpolator()
OrientationInterpolator240.DEF = "Stop_l_shoulder_RotationInterpolator"
OrientationInterpolator240.key = [0,0.5,1]
OrientationInterpolator240.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator240)
OrientationInterpolator241 = x3d.OrientationInterpolator()
OrientationInterpolator241.DEF = "Stop_l_elbow_RotationInterpolator"
OrientationInterpolator241.key = [0,0.5,1]
OrientationInterpolator241.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator241)
OrientationInterpolator242 = x3d.OrientationInterpolator()
OrientationInterpolator242.DEF = "Stop_l_wrist_RotationInterpolator"
OrientationInterpolator242.key = [0,0.5,1]
OrientationInterpolator242.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator242)
OrientationInterpolator243 = x3d.OrientationInterpolator()
OrientationInterpolator243.DEF = "Stop_l_thumb1_RotationInterpolator"
OrientationInterpolator243.key = [0,0.5,1]
OrientationInterpolator243.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator243)
OrientationInterpolator244 = x3d.OrientationInterpolator()
OrientationInterpolator244.DEF = "Stop_l_thumb2_RotationInterpolator"
OrientationInterpolator244.key = [0,0.5,1]
OrientationInterpolator244.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator244)
OrientationInterpolator245 = x3d.OrientationInterpolator()
OrientationInterpolator245.DEF = "Stop_l_thumb3_RotationInterpolator"
OrientationInterpolator245.key = [0,0.5,1]
OrientationInterpolator245.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator245)
OrientationInterpolator246 = x3d.OrientationInterpolator()
OrientationInterpolator246.DEF = "Stop_l_index0_RotationInterpolator"
OrientationInterpolator246.key = [0,0.5,1]
OrientationInterpolator246.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator246)
OrientationInterpolator247 = x3d.OrientationInterpolator()
OrientationInterpolator247.DEF = "Stop_l_index1_RotationInterpolator"
OrientationInterpolator247.key = [0,0.5,1]
OrientationInterpolator247.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator247)
OrientationInterpolator248 = x3d.OrientationInterpolator()
OrientationInterpolator248.DEF = "Stop_l_index2_RotationInterpolator"
OrientationInterpolator248.key = [0,0.5,1]
OrientationInterpolator248.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator248)
OrientationInterpolator249 = x3d.OrientationInterpolator()
OrientationInterpolator249.DEF = "Stop_l_index3_RotationInterpolator"
OrientationInterpolator249.key = [0,0.5,1]
OrientationInterpolator249.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator249)
OrientationInterpolator250 = x3d.OrientationInterpolator()
OrientationInterpolator250.DEF = "Stop_l_middle0_RotationInterpolator"
OrientationInterpolator250.key = [0,0.5,1]
OrientationInterpolator250.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator250)
OrientationInterpolator251 = x3d.OrientationInterpolator()
OrientationInterpolator251.DEF = "Stop_l_middle1_RotationInterpolator"
OrientationInterpolator251.key = [0,0.5,1]
OrientationInterpolator251.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator251)
OrientationInterpolator252 = x3d.OrientationInterpolator()
OrientationInterpolator252.DEF = "Stop_l_middle2_RotationInterpolator"
OrientationInterpolator252.key = [0,0.5,1]
OrientationInterpolator252.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator252)
OrientationInterpolator253 = x3d.OrientationInterpolator()
OrientationInterpolator253.DEF = "Stop_l_middle3_RotationInterpolator"
OrientationInterpolator253.key = [0,0.5,1]
OrientationInterpolator253.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator253)
OrientationInterpolator254 = x3d.OrientationInterpolator()
OrientationInterpolator254.DEF = "Stop_l_ring0_RotationInterpolator"
OrientationInterpolator254.key = [0,0.5,1]
OrientationInterpolator254.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator254)
OrientationInterpolator255 = x3d.OrientationInterpolator()
OrientationInterpolator255.DEF = "Stop_l_ring1_RotationInterpolator"
OrientationInterpolator255.key = [0,0.5,1]
OrientationInterpolator255.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator255)
OrientationInterpolator256 = x3d.OrientationInterpolator()
OrientationInterpolator256.DEF = "Stop_l_ring2_RotationInterpolator"
OrientationInterpolator256.key = [0,0.5,1]
OrientationInterpolator256.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator256)
OrientationInterpolator257 = x3d.OrientationInterpolator()
OrientationInterpolator257.DEF = "Stop_l_ring3_RotationInterpolator"
OrientationInterpolator257.key = [0,0.5,1]
OrientationInterpolator257.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator257)
OrientationInterpolator258 = x3d.OrientationInterpolator()
OrientationInterpolator258.DEF = "Stop_l_pinky0_RotationInterpolator"
OrientationInterpolator258.key = [0,0.5,1]
OrientationInterpolator258.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator258)
OrientationInterpolator259 = x3d.OrientationInterpolator()
OrientationInterpolator259.DEF = "Stop_l_pinky1_RotationInterpolator"
OrientationInterpolator259.key = [0,0.5,1]
OrientationInterpolator259.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator259)
OrientationInterpolator260 = x3d.OrientationInterpolator()
OrientationInterpolator260.DEF = "Stop_l_pinky2_RotationInterpolator"
OrientationInterpolator260.key = [0,0.5,1]
OrientationInterpolator260.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator260)
OrientationInterpolator261 = x3d.OrientationInterpolator()
OrientationInterpolator261.DEF = "Stop_l_pinky3_RotationInterpolator"
OrientationInterpolator261.key = [0,0.5,1]
OrientationInterpolator261.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator261)
OrientationInterpolator262 = x3d.OrientationInterpolator()
OrientationInterpolator262.DEF = "Stop_r_sternoclavicular_RotationInterpolator"
OrientationInterpolator262.key = [0,0.5,1]
OrientationInterpolator262.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator262)
OrientationInterpolator263 = x3d.OrientationInterpolator()
OrientationInterpolator263.DEF = "Stop_r_acromioclavicular_RotationInterpolator"
OrientationInterpolator263.key = [0,0.5,1]
OrientationInterpolator263.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator263)
OrientationInterpolator264 = x3d.OrientationInterpolator()
OrientationInterpolator264.DEF = "Stop_r_shoulder_RotationInterpolator"
OrientationInterpolator264.key = [0,0.5,1]
OrientationInterpolator264.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator264)
OrientationInterpolator265 = x3d.OrientationInterpolator()
OrientationInterpolator265.DEF = "Stop_r_elbow_RotationInterpolator"
OrientationInterpolator265.key = [0,0.5,1]
OrientationInterpolator265.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator265)
OrientationInterpolator266 = x3d.OrientationInterpolator()
OrientationInterpolator266.DEF = "Stop_r_wrist_RotationInterpolator"
OrientationInterpolator266.key = [0,0.5,1]
OrientationInterpolator266.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator266)
OrientationInterpolator267 = x3d.OrientationInterpolator()
OrientationInterpolator267.DEF = "Stop_r_thumb1_RotationInterpolator"
OrientationInterpolator267.key = [0,0.5,1]
OrientationInterpolator267.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator267)
OrientationInterpolator268 = x3d.OrientationInterpolator()
OrientationInterpolator268.DEF = "Stop_r_thumb2_RotationInterpolator"
OrientationInterpolator268.key = [0,0.5,1]
OrientationInterpolator268.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator268)
OrientationInterpolator269 = x3d.OrientationInterpolator()
OrientationInterpolator269.DEF = "Stop_r_thumb3_RotationInterpolator"
OrientationInterpolator269.key = [0,0.5,1]
OrientationInterpolator269.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator269)
OrientationInterpolator270 = x3d.OrientationInterpolator()
OrientationInterpolator270.DEF = "Stop_r_index0_RotationInterpolator"
OrientationInterpolator270.key = [0,0.5,1]
OrientationInterpolator270.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator270)
OrientationInterpolator271 = x3d.OrientationInterpolator()
OrientationInterpolator271.DEF = "Stop_r_index1_RotationInterpolator"
OrientationInterpolator271.key = [0,0.5,1]
OrientationInterpolator271.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator271)
OrientationInterpolator272 = x3d.OrientationInterpolator()
OrientationInterpolator272.DEF = "Stop_r_index2_RotationInterpolator"
OrientationInterpolator272.key = [0,0.5,1]
OrientationInterpolator272.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator272)
OrientationInterpolator273 = x3d.OrientationInterpolator()
OrientationInterpolator273.DEF = "Stop_r_index3_RotationInterpolator"
OrientationInterpolator273.key = [0,0.5,1]
OrientationInterpolator273.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator273)
OrientationInterpolator274 = x3d.OrientationInterpolator()
OrientationInterpolator274.DEF = "Stop_r_middle0_RotationInterpolator"
OrientationInterpolator274.key = [0,0.5,1]
OrientationInterpolator274.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator274)
OrientationInterpolator275 = x3d.OrientationInterpolator()
OrientationInterpolator275.DEF = "Stop_r_middle1_RotationInterpolator"
OrientationInterpolator275.key = [0,0.5,1]
OrientationInterpolator275.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator275)
OrientationInterpolator276 = x3d.OrientationInterpolator()
OrientationInterpolator276.DEF = "Stop_r_middle2_RotationInterpolator"
OrientationInterpolator276.key = [0,0.5,1]
OrientationInterpolator276.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator276)
OrientationInterpolator277 = x3d.OrientationInterpolator()
OrientationInterpolator277.DEF = "Stop_r_middle3_RotationInterpolator"
OrientationInterpolator277.key = [0,0.5,1]
OrientationInterpolator277.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator277)
OrientationInterpolator278 = x3d.OrientationInterpolator()
OrientationInterpolator278.DEF = "Stop_r_ring0_RotationInterpolator"
OrientationInterpolator278.key = [0,0.5,1]
OrientationInterpolator278.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator278)
OrientationInterpolator279 = x3d.OrientationInterpolator()
OrientationInterpolator279.DEF = "Stop_r_ring1_RotationInterpolator"
OrientationInterpolator279.key = [0,0.5,1]
OrientationInterpolator279.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator279)
OrientationInterpolator280 = x3d.OrientationInterpolator()
OrientationInterpolator280.DEF = "Stop_r_ring2_RotationInterpolator"
OrientationInterpolator280.key = [0,0.5,1]
OrientationInterpolator280.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator280)
OrientationInterpolator281 = x3d.OrientationInterpolator()
OrientationInterpolator281.DEF = "Stop_r_ring3_RotationInterpolator"
OrientationInterpolator281.key = [0,0.5,1]
OrientationInterpolator281.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator281)
OrientationInterpolator282 = x3d.OrientationInterpolator()
OrientationInterpolator282.DEF = "Stop_r_pinky0_RotationInterpolator"
OrientationInterpolator282.key = [0,0.5,1]
OrientationInterpolator282.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator282)
OrientationInterpolator283 = x3d.OrientationInterpolator()
OrientationInterpolator283.DEF = "Stop_r_pinky1_RotationInterpolator"
OrientationInterpolator283.key = [0,0.5,1]
OrientationInterpolator283.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator283)
OrientationInterpolator284 = x3d.OrientationInterpolator()
OrientationInterpolator284.DEF = "Stop_r_pinky2_RotationInterpolator"
OrientationInterpolator284.key = [0,0.5,1]
OrientationInterpolator284.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator284)
OrientationInterpolator285 = x3d.OrientationInterpolator()
OrientationInterpolator285.DEF = "Stop_r_pinky3_RotationInterpolator"
OrientationInterpolator285.key = [0,0.5,1]
OrientationInterpolator285.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group194.children.append(OrientationInterpolator285)

Scene34.children.append(Group194)
Group286 = x3d.Group()
Group286.DEF = "StandAnimation"
TimeSensor287 = x3d.TimeSensor()
TimeSensor287.DEF = "StandTimer"
TimeSensor287.cycleInterval = 5.73
TimeSensor287.loop = True

Group286.children.append(TimeSensor287)
OrientationInterpolator288 = x3d.OrientationInterpolator()
OrientationInterpolator288.DEF = "Stand_r_metatarsal_PitchInterpolator"
OrientationInterpolator288.key = [0,0.2,0.4,0.6,0.7,1]
OrientationInterpolator288.keyValue = (1.0000,0.0000,0.0000,0.0000,-1.0000,0.0000,0.0000,0.0150,1.0000,0.0000,0.0000,0.1700,-1.0000,0.0000,0.0000,0.0250,1.0000,0.0000,0.0000,0.0100,1.0000,0.0000,0.0000,0.0000)

Group286.children.append(OrientationInterpolator288)
OrientationInterpolator289 = x3d.OrientationInterpolator()
OrientationInterpolator289.DEF = "Stand_r_ankle_RotationInterpolator"
OrientationInterpolator289.key = [0,0.5,1]
OrientationInterpolator289.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group286.children.append(OrientationInterpolator289)
OrientationInterpolator290 = x3d.OrientationInterpolator()
OrientationInterpolator290.DEF = "Stand_r_knee_RotationInterpolator"
OrientationInterpolator290.key = [0,0.5,1]
OrientationInterpolator290.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group286.children.append(OrientationInterpolator290)
OrientationInterpolator291 = x3d.OrientationInterpolator()
OrientationInterpolator291.DEF = "Stand_r_hip_RotationInterpolator"
OrientationInterpolator291.key = [0,0.5,1]
OrientationInterpolator291.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group286.children.append(OrientationInterpolator291)
OrientationInterpolator292 = x3d.OrientationInterpolator()
OrientationInterpolator292.DEF = "Stand_l_ankle_RotationInterpolator"
OrientationInterpolator292.key = [0,0.5,1]
OrientationInterpolator292.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group286.children.append(OrientationInterpolator292)
OrientationInterpolator293 = x3d.OrientationInterpolator()
OrientationInterpolator293.DEF = "Stand_l_knee_RotationInterpolator"
OrientationInterpolator293.key = [0,0.5,1]
OrientationInterpolator293.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group286.children.append(OrientationInterpolator293)
OrientationInterpolator294 = x3d.OrientationInterpolator()
OrientationInterpolator294.DEF = "Stand_l_hip_RotationInterpolator"
OrientationInterpolator294.key = [0,0.5,1]
OrientationInterpolator294.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group286.children.append(OrientationInterpolator294)
OrientationInterpolator295 = x3d.OrientationInterpolator()
OrientationInterpolator295.DEF = "Stand_r_wrist_RotationInterpolator"
OrientationInterpolator295.key = [0,0.5,1]
OrientationInterpolator295.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,-1.0000,0.2500,0.0000,0.0000,1.0000,0.0000)

Group286.children.append(OrientationInterpolator295)
OrientationInterpolator296 = x3d.OrientationInterpolator()
OrientationInterpolator296.DEF = "Stand_r_elbow_RotationInterpolator"
OrientationInterpolator296.key = [0,0.5,1]
OrientationInterpolator296.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group286.children.append(OrientationInterpolator296)
OrientationInterpolator297 = x3d.OrientationInterpolator()
OrientationInterpolator297.DEF = "Stand_r_shoulder_RotationInterpolator"
OrientationInterpolator297.key = [0,0.5,1]
OrientationInterpolator297.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group286.children.append(OrientationInterpolator297)
OrientationInterpolator298 = x3d.OrientationInterpolator()
OrientationInterpolator298.DEF = "Stand_l_wrist_RotationInterpolator"
OrientationInterpolator298.key = [0,0.5,1]
OrientationInterpolator298.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group286.children.append(OrientationInterpolator298)
OrientationInterpolator299 = x3d.OrientationInterpolator()
OrientationInterpolator299.DEF = "Stand_l_elbow_RotationInterpolator"
OrientationInterpolator299.key = [0,0.5,1]
OrientationInterpolator299.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group286.children.append(OrientationInterpolator299)
OrientationInterpolator300 = x3d.OrientationInterpolator()
OrientationInterpolator300.DEF = "Stand_l_shoulder_RotationInterpolator"
OrientationInterpolator300.key = [0,0.5,1]
OrientationInterpolator300.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group286.children.append(OrientationInterpolator300)
OrientationInterpolator301 = x3d.OrientationInterpolator()
OrientationInterpolator301.DEF = "Stand_head_RotationInterpolator"
OrientationInterpolator301.key = [0,0.5,1]
OrientationInterpolator301.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group286.children.append(OrientationInterpolator301)
OrientationInterpolator302 = x3d.OrientationInterpolator()
OrientationInterpolator302.DEF = "Stand_neck_RotationInterpolator"
OrientationInterpolator302.key = [0,0.5,1]
OrientationInterpolator302.keyValue = (0.0000,0.0000,1.0000,0.0000,-1.0000,0.0000,0.0000,0.5000,0.0000,0.0000,1.0000,0.0000)

Group286.children.append(OrientationInterpolator302)
OrientationInterpolator303 = x3d.OrientationInterpolator()
OrientationInterpolator303.DEF = "Stand_l_eyeball_RotationInterpolator"
OrientationInterpolator303.key = [0,0.4,0.7,1]
OrientationInterpolator303.keyValue = (0.0000,0.0000,1.0000,0.0000,-1.0000,0.0000,0.0000,0.5000,1.0000,0.0000,0.0000,0.4500,0.0000,0.0000,1.0000,0.0000)

Group286.children.append(OrientationInterpolator303)
OrientationInterpolator304 = x3d.OrientationInterpolator()
OrientationInterpolator304.DEF = "Stand_r_eyeball_RotationInterpolator"
OrientationInterpolator304.key = [0,0.4,0.7,1]
OrientationInterpolator304.keyValue = (0.0000,0.0000,1.0000,0.0000,-1.0000,0.0000,0.0000,0.5000,1.0000,0.0000,0.0000,0.4500,0.0000,0.0000,1.0000,0.0000)

Group286.children.append(OrientationInterpolator304)
OrientationInterpolator305 = x3d.OrientationInterpolator()
OrientationInterpolator305.DEF = "Stand_lower_body_RotationInterpolator"
OrientationInterpolator305.key = [0,0.5,1]
OrientationInterpolator305.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group286.children.append(OrientationInterpolator305)
OrientationInterpolator306 = x3d.OrientationInterpolator()
OrientationInterpolator306.DEF = "Stand_upper_body_RotationInterpolator"
OrientationInterpolator306.key = [0,0.5,1]
OrientationInterpolator306.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group286.children.append(OrientationInterpolator306)
OrientationInterpolator307 = x3d.OrientationInterpolator()
OrientationInterpolator307.DEF = "Stand_whole_body_RotationInterpolator"
OrientationInterpolator307.key = [0,0.5,1]
OrientationInterpolator307.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group286.children.append(OrientationInterpolator307)
PositionInterpolator308 = x3d.PositionInterpolator()
PositionInterpolator308.DEF = "Stand_whole_body_TranslationInterpolator"
PositionInterpolator308.key = [0,0.5,1]
PositionInterpolator308.keyValue = (0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000)

Group286.children.append(PositionInterpolator308)
OrientationInterpolator309 = x3d.OrientationInterpolator()
OrientationInterpolator309.DEF = "Stand_l_sternoclavicular_RollInterpolator"
OrientationInterpolator309.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator309.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group286.children.append(OrientationInterpolator309)
OrientationInterpolator310 = x3d.OrientationInterpolator()
OrientationInterpolator310.DEF = "Stand_l_acromioclavicular_RollInterpolator"
OrientationInterpolator310.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator310.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group286.children.append(OrientationInterpolator310)
OrientationInterpolator311 = x3d.OrientationInterpolator()
OrientationInterpolator311.DEF = "Stand_r_sternoclavicular_RollInterpolator"
OrientationInterpolator311.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator311.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group286.children.append(OrientationInterpolator311)
OrientationInterpolator312 = x3d.OrientationInterpolator()
OrientationInterpolator312.DEF = "Stand_r_acromioclavicular_RollInterpolator"
OrientationInterpolator312.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator312.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group286.children.append(OrientationInterpolator312)
OrientationInterpolator313 = x3d.OrientationInterpolator()
OrientationInterpolator313.DEF = "Stand_sacroiliac_YawInterpolator"
OrientationInterpolator313.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator313.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group286.children.append(OrientationInterpolator313)
OrientationInterpolator314 = x3d.OrientationInterpolator()
OrientationInterpolator314.DEF = "Stand_vl5_YawInterpolator"
OrientationInterpolator314.key = [0,0.2,0.4,0.5,0.6,0.8,1]
OrientationInterpolator314.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group286.children.append(OrientationInterpolator314)
OrientationInterpolator315 = x3d.OrientationInterpolator()
OrientationInterpolator315.DEF = "Stand_vc6_YawInterpolator"
OrientationInterpolator315.key = [0,0.2,0.4,0.5,0.6,0.8,1]
OrientationInterpolator315.keyValue = (0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,-1.0000,0.0000,0.0000,0.0000,0.0000,-1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000)

Group286.children.append(OrientationInterpolator315)
OrientationInterpolator316 = x3d.OrientationInterpolator()
OrientationInterpolator316.DEF = "Stand_l_thumb1_PitchInterpolator"
OrientationInterpolator316.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator316.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group286.children.append(OrientationInterpolator316)
OrientationInterpolator317 = x3d.OrientationInterpolator()
OrientationInterpolator317.DEF = "Stand_r_thumb1_PitchInterpolator"
OrientationInterpolator317.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator317.keyValue = (1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.5000,1.0000,0.0000,0.0000,0.1000,1.0000,0.0000,0.0000,0.2700,1.0000,0.0000,0.0000,0.2000,1.0000,0.0000,0.0000,0.0000)

Group286.children.append(OrientationInterpolator317)
OrientationInterpolator318 = x3d.OrientationInterpolator()
OrientationInterpolator318.DEF = "Stand_r_index1_RollInterpolator"
OrientationInterpolator318.key = [0,0.2,0.4,0.5,0.8,1]
OrientationInterpolator318.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.1000,0.0000,0.0000,1.0000,0.2000,0.0000,0.0000,1.0000,0.3000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group286.children.append(OrientationInterpolator318)
OrientationInterpolator319 = x3d.OrientationInterpolator()
OrientationInterpolator319.DEF = "Stand_r_index2_RollInterpolator"
OrientationInterpolator319.key = [0,0.2,0.4,0.5,0.8,1]
OrientationInterpolator319.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.4000,0.0000,0.0000,1.0000,0.3200,0.0000,0.0000,1.0000,0.2500,0.0000,0.0000,1.0000,0.2000,0.0000,0.0000,1.0000,0.0000)

Group286.children.append(OrientationInterpolator319)
OrientationInterpolator320 = x3d.OrientationInterpolator()
OrientationInterpolator320.DEF = "Stand_r_index3_RollInterpolator"
OrientationInterpolator320.key = [0,0.2,0.4,0.5,0.8,1]
OrientationInterpolator320.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.2000,0.0000,0.0000,1.0000,0.3000,0.0000,0.0000,1.0000,0.3500,0.0000,0.0000,1.0000,0.2000,0.0000,0.0000,1.0000,0.0000)

Group286.children.append(OrientationInterpolator320)

Scene34.children.append(Group286)
Group321 = x3d.Group()
Group321.DEF = "PitchesAnimation"
TimeSensor322 = x3d.TimeSensor()
TimeSensor322.DEF = "PitchTimer"
TimeSensor322.cycleInterval = 5.73
TimeSensor322.loop = True

Group321.children.append(TimeSensor322)
OrientationInterpolator323 = x3d.OrientationInterpolator()
OrientationInterpolator323.DEF = "Pitch_r_metatarsal_PitchInterpolator"
OrientationInterpolator323.key = [0,0.2,0.4,0.6,0.7,1]
OrientationInterpolator323.keyValue = (1.0000,0.0000,0.0000,0.0000,-1.0000,0.0000,0.0000,0.5000,-1.0000,0.0000,0.0000,0.7000,1.0000,0.0000,0.0000,0.7500,-1.0000,0.0000,0.0000,0.2000,1.0000,0.0000,0.0000,0.0000)

Group321.children.append(OrientationInterpolator323)
OrientationInterpolator324 = x3d.OrientationInterpolator()
OrientationInterpolator324.DEF = "Pitches_r_ankle_RotationInterpolator"
OrientationInterpolator324.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator324.keyValue = (0.0000,0.0000,1.0000,0.0000,1.0000,0.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000,-1.0000,0.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000)

Group321.children.append(OrientationInterpolator324)
OrientationInterpolator325 = x3d.OrientationInterpolator()
OrientationInterpolator325.DEF = "Pitches_r_knee_RotationInterpolator"
OrientationInterpolator325.key = [0,0.5,1]
OrientationInterpolator325.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group321.children.append(OrientationInterpolator325)
OrientationInterpolator326 = x3d.OrientationInterpolator()
OrientationInterpolator326.DEF = "Pitches_r_hip_RotationInterpolator"
OrientationInterpolator326.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator326.keyValue = (0.0000,0.0000,1.0000,0.0000,-1.0000,0.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000,1.0000,0.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000)

Group321.children.append(OrientationInterpolator326)
OrientationInterpolator327 = x3d.OrientationInterpolator()
OrientationInterpolator327.DEF = "Pitches_l_ankle_RotationInterpolator"
OrientationInterpolator327.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator327.keyValue = (0.0000,0.0000,1.0000,0.0000,-1.0000,0.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000,1.0000,0.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000)

Group321.children.append(OrientationInterpolator327)
OrientationInterpolator328 = x3d.OrientationInterpolator()
OrientationInterpolator328.DEF = "Pitches_l_knee_RotationInterpolator"
OrientationInterpolator328.key = [0,0.5,1]
OrientationInterpolator328.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group321.children.append(OrientationInterpolator328)
OrientationInterpolator329 = x3d.OrientationInterpolator()
OrientationInterpolator329.DEF = "Pitches_l_hip_RotationInterpolator"
OrientationInterpolator329.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator329.keyValue = (0.0000,0.0000,1.0000,0.0000,1.0000,0.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000,-1.0000,0.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000)

Group321.children.append(OrientationInterpolator329)
OrientationInterpolator330 = x3d.OrientationInterpolator()
OrientationInterpolator330.DEF = "Pitches_r_wrist_RotationInterpolator"
OrientationInterpolator330.key = [0,0.5,1]
OrientationInterpolator330.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group321.children.append(OrientationInterpolator330)
OrientationInterpolator331 = x3d.OrientationInterpolator()
OrientationInterpolator331.DEF = "Pitches_r_elbow_RotationInterpolator"
OrientationInterpolator331.key = [0,0.5,1]
OrientationInterpolator331.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group321.children.append(OrientationInterpolator331)
OrientationInterpolator332 = x3d.OrientationInterpolator()
OrientationInterpolator332.DEF = "Pitches_r_shoulder_RotationInterpolator"
OrientationInterpolator332.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator332.keyValue = (0.0000,0.0000,1.0000,0.0000,1.0000,0.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000,-1.0000,0.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000)

Group321.children.append(OrientationInterpolator332)
OrientationInterpolator333 = x3d.OrientationInterpolator()
OrientationInterpolator333.DEF = "Pitches_l_wrist_RotationInterpolator"
OrientationInterpolator333.key = [0,0.5,1]
OrientationInterpolator333.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group321.children.append(OrientationInterpolator333)
OrientationInterpolator334 = x3d.OrientationInterpolator()
OrientationInterpolator334.DEF = "Pitches_l_elbow_RotationInterpolator"
OrientationInterpolator334.key = [0,0.5,1]
OrientationInterpolator334.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group321.children.append(OrientationInterpolator334)
OrientationInterpolator335 = x3d.OrientationInterpolator()
OrientationInterpolator335.DEF = "Pitches_l_shoulder_RotationInterpolator"
OrientationInterpolator335.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator335.keyValue = (0.0000,0.0000,1.0000,0.0000,-1.0000,0.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000,1.0000,0.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000)

Group321.children.append(OrientationInterpolator335)
OrientationInterpolator336 = x3d.OrientationInterpolator()
OrientationInterpolator336.DEF = "Pitches_head_RotationInterpolator"
OrientationInterpolator336.key = [0,0.5,1]
OrientationInterpolator336.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group321.children.append(OrientationInterpolator336)
OrientationInterpolator337 = x3d.OrientationInterpolator()
OrientationInterpolator337.DEF = "Pitches_neck_RotationInterpolator"
OrientationInterpolator337.key = [0,0.25,0.55,1]
OrientationInterpolator337.keyValue = (0.0000,0.0000,1.0000,0.0000,1.0000,0.0000,0.0000,0.5500,-1.0000,0.0000,0.0000,1.0500,0.0000,0.0000,1.0000,0.0000)

Group321.children.append(OrientationInterpolator337)
OrientationInterpolator338 = x3d.OrientationInterpolator()
OrientationInterpolator338.DEF = "Pitches_lower_body_RotationInterpolator"
OrientationInterpolator338.key = [0,0.5,1]
OrientationInterpolator338.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group321.children.append(OrientationInterpolator338)
OrientationInterpolator339 = x3d.OrientationInterpolator()
OrientationInterpolator339.DEF = "Pitches_upper_body_RotationInterpolator"
OrientationInterpolator339.key = [0,0.5,1]
OrientationInterpolator339.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group321.children.append(OrientationInterpolator339)
OrientationInterpolator340 = x3d.OrientationInterpolator()
OrientationInterpolator340.DEF = "Pitches_whole_body_RotationInterpolator"
OrientationInterpolator340.key = [0,0.5,1]
OrientationInterpolator340.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group321.children.append(OrientationInterpolator340)
PositionInterpolator341 = x3d.PositionInterpolator()
PositionInterpolator341.DEF = "Pitches_whole_body_TranslationInterpolator"
PositionInterpolator341.key = [0,0.125,0.25,0.375,0.5,0.625,0.75,0.875,1]
PositionInterpolator341.keyValue = (0.0000,0.0000,0.0000,0.0000,-0.1500,0.0000,0.0000,-0.7000,0.0000,0.0000,-0.1500,0.0000,0.0000,0.0000,0.0000,0.0000,-0.1500,0.0000,0.0000,-0.7000,0.0000,0.0000,-0.1500,0.0000,0.0000,0.0000,0.0000)

Group321.children.append(PositionInterpolator341)
OrientationInterpolator342 = x3d.OrientationInterpolator()
OrientationInterpolator342.DEF = "Pitch_l_sternoclavicular_RollInterpolator"
OrientationInterpolator342.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator342.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group321.children.append(OrientationInterpolator342)
OrientationInterpolator343 = x3d.OrientationInterpolator()
OrientationInterpolator343.DEF = "Pitch_l_acromioclavicular_RollInterpolator"
OrientationInterpolator343.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator343.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group321.children.append(OrientationInterpolator343)
OrientationInterpolator344 = x3d.OrientationInterpolator()
OrientationInterpolator344.DEF = "Pitch_r_sternoclavicular_RollInterpolator"
OrientationInterpolator344.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator344.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group321.children.append(OrientationInterpolator344)
OrientationInterpolator345 = x3d.OrientationInterpolator()
OrientationInterpolator345.DEF = "Pitch_r_acromioclavicular_RollInterpolator"
OrientationInterpolator345.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator345.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group321.children.append(OrientationInterpolator345)
OrientationInterpolator346 = x3d.OrientationInterpolator()
OrientationInterpolator346.DEF = "Pitch_sacroiliac_YawInterpolator"
OrientationInterpolator346.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator346.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group321.children.append(OrientationInterpolator346)
OrientationInterpolator347 = x3d.OrientationInterpolator()
OrientationInterpolator347.DEF = "Pitch_vl5_YawInterpolator"
OrientationInterpolator347.key = [0,0.2,0.4,0.5,0.6,0.8,1]
OrientationInterpolator347.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group321.children.append(OrientationInterpolator347)
OrientationInterpolator348 = x3d.OrientationInterpolator()
OrientationInterpolator348.DEF = "Pitch_vc6_YawInterpolator"
OrientationInterpolator348.key = [0,0.2,0.4,0.5,0.6,0.8,1]
OrientationInterpolator348.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group321.children.append(OrientationInterpolator348)
OrientationInterpolator349 = x3d.OrientationInterpolator()
OrientationInterpolator349.DEF = "Pitch_l_thumb1_PitchInterpolator"
OrientationInterpolator349.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator349.keyValue = (1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.2500,1.0000,0.0000,0.0000,0.3000,1.0000,0.0000,0.0000,0.2700,1.0000,0.0000,0.0000,0.2000,1.0000,0.0000,0.0000,0.0000)

Group321.children.append(OrientationInterpolator349)
OrientationInterpolator350 = x3d.OrientationInterpolator()
OrientationInterpolator350.DEF = "Pitch_r_thumb1_PitchInterpolator"
OrientationInterpolator350.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator350.keyValue = (1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.2500,1.0000,0.0000,0.0000,0.3000,1.0000,0.0000,0.0000,0.2700,1.0000,0.0000,0.0000,0.2000,1.0000,0.0000,0.0000,0.0000)

Group321.children.append(OrientationInterpolator350)

Scene34.children.append(Group321)
Group351 = x3d.Group()
Group351.DEF = "YawsAnimation"
TimeSensor352 = x3d.TimeSensor()
TimeSensor352.DEF = "YawTimer"
TimeSensor352.cycleInterval = 5.73
TimeSensor352.loop = True

Group351.children.append(TimeSensor352)
OrientationInterpolator353 = x3d.OrientationInterpolator()
OrientationInterpolator353.DEF = "Yaw_r_metatarsal_PitchInterpolator"
OrientationInterpolator353.key = [0,0.2,0.4,0.6,0.7,1]
OrientationInterpolator353.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group351.children.append(OrientationInterpolator353)
OrientationInterpolator354 = x3d.OrientationInterpolator()
OrientationInterpolator354.DEF = "Yaws_r_ankle_RotationInterpolator"
OrientationInterpolator354.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator354.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,-1.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000,0.0000,1.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000)

Group351.children.append(OrientationInterpolator354)
OrientationInterpolator355 = x3d.OrientationInterpolator()
OrientationInterpolator355.DEF = "Yaws_r_knee_RotationInterpolator"
OrientationInterpolator355.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator355.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,1.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000,0.0000,-1.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000)

Group351.children.append(OrientationInterpolator355)
OrientationInterpolator356 = x3d.OrientationInterpolator()
OrientationInterpolator356.DEF = "Yaws_r_hip_RotationInterpolator"
OrientationInterpolator356.key = [0,0.5,1]
OrientationInterpolator356.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group351.children.append(OrientationInterpolator356)
OrientationInterpolator357 = x3d.OrientationInterpolator()
OrientationInterpolator357.DEF = "Yaws_l_ankle_RotationInterpolator"
OrientationInterpolator357.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator357.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,1.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000,0.0000,-1.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000)

Group351.children.append(OrientationInterpolator357)
OrientationInterpolator358 = x3d.OrientationInterpolator()
OrientationInterpolator358.DEF = "Yaws_l_knee_RotationInterpolator"
OrientationInterpolator358.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator358.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,-1.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000,0.0000,1.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000)

Group351.children.append(OrientationInterpolator358)
OrientationInterpolator359 = x3d.OrientationInterpolator()
OrientationInterpolator359.DEF = "Yaws_l_hip_RotationInterpolator"
OrientationInterpolator359.key = [0,0.5,1]
OrientationInterpolator359.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group351.children.append(OrientationInterpolator359)
OrientationInterpolator360 = x3d.OrientationInterpolator()
OrientationInterpolator360.DEF = "Yaws_r_wrist_RotationInterpolator"
OrientationInterpolator360.key = [0,0.5,1]
OrientationInterpolator360.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group351.children.append(OrientationInterpolator360)
OrientationInterpolator361 = x3d.OrientationInterpolator()
OrientationInterpolator361.DEF = "Yaws_r_elbow_RotationInterpolator"
OrientationInterpolator361.key = [0,0.5,1]
OrientationInterpolator361.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group351.children.append(OrientationInterpolator361)
OrientationInterpolator362 = x3d.OrientationInterpolator()
OrientationInterpolator362.DEF = "Yaws_r_shoulder_RotationInterpolator"
OrientationInterpolator362.key = [0,0.5,1]
OrientationInterpolator362.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group351.children.append(OrientationInterpolator362)
OrientationInterpolator363 = x3d.OrientationInterpolator()
OrientationInterpolator363.DEF = "Yaws_l_wrist_RotationInterpolator"
OrientationInterpolator363.key = [0,0.5,1]
OrientationInterpolator363.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group351.children.append(OrientationInterpolator363)
OrientationInterpolator364 = x3d.OrientationInterpolator()
OrientationInterpolator364.DEF = "Yaws_l_elbow_RotationInterpolator"
OrientationInterpolator364.key = [0,0.5,1]
OrientationInterpolator364.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group351.children.append(OrientationInterpolator364)
OrientationInterpolator365 = x3d.OrientationInterpolator()
OrientationInterpolator365.DEF = "Yaws_l_shoulder_RotationInterpolator"
OrientationInterpolator365.key = [0,0.5,1]
OrientationInterpolator365.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group351.children.append(OrientationInterpolator365)
OrientationInterpolator366 = x3d.OrientationInterpolator()
OrientationInterpolator366.DEF = "Yaws_head_RotationInterpolator"
OrientationInterpolator366.key = [0,0.5,1]
OrientationInterpolator366.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group351.children.append(OrientationInterpolator366)
OrientationInterpolator367 = x3d.OrientationInterpolator()
OrientationInterpolator367.DEF = "Yaws_neck_RotationInterpolator"
OrientationInterpolator367.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator367.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,1.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000,0.0000,-1.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000)

Group351.children.append(OrientationInterpolator367)
OrientationInterpolator368 = x3d.OrientationInterpolator()
OrientationInterpolator368.DEF = "Yaws_upper_body_RotationInterpolator"
OrientationInterpolator368.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator368.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,-1.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000,0.0000,1.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000)

Group351.children.append(OrientationInterpolator368)
OrientationInterpolator369 = x3d.OrientationInterpolator()
OrientationInterpolator369.DEF = "Yaws_lower_body_RotationInterpolator"
OrientationInterpolator369.key = [0,0.5,1]
OrientationInterpolator369.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group351.children.append(OrientationInterpolator369)
OrientationInterpolator370 = x3d.OrientationInterpolator()
OrientationInterpolator370.DEF = "Yaws_whole_body_RotationInterpolator"
OrientationInterpolator370.key = [0,0.5,1]
OrientationInterpolator370.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group351.children.append(OrientationInterpolator370)
PositionInterpolator371 = x3d.PositionInterpolator()
PositionInterpolator371.DEF = "Yaws_whole_body_TranslationInterpolator"
PositionInterpolator371.key = [0,0.5,1]
PositionInterpolator371.keyValue = (0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000)

Group351.children.append(PositionInterpolator371)
OrientationInterpolator372 = x3d.OrientationInterpolator()
OrientationInterpolator372.DEF = "Yaw_l_sternoclavicular_RollInterpolator"
OrientationInterpolator372.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator372.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group351.children.append(OrientationInterpolator372)
OrientationInterpolator373 = x3d.OrientationInterpolator()
OrientationInterpolator373.DEF = "Yaw_l_acromioclavicular_RollInterpolator"
OrientationInterpolator373.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator373.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group351.children.append(OrientationInterpolator373)
OrientationInterpolator374 = x3d.OrientationInterpolator()
OrientationInterpolator374.DEF = "Yaw_r_sternoclavicular_RollInterpolator"
OrientationInterpolator374.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator374.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group351.children.append(OrientationInterpolator374)
OrientationInterpolator375 = x3d.OrientationInterpolator()
OrientationInterpolator375.DEF = "Yaw_r_acromioclavicular_RollInterpolator"
OrientationInterpolator375.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator375.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group351.children.append(OrientationInterpolator375)
OrientationInterpolator376 = x3d.OrientationInterpolator()
OrientationInterpolator376.DEF = "Yaw_sacroiliac_YawInterpolator"
OrientationInterpolator376.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator376.keyValue = (0.0000,1.0000,0.0000,0.0000,0.0000,-1.0000,0.0000,0.1000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.2400,0.0000,-1.0000,0.0000,0.4000,0.0000,1.0000,0.0000,0.0000)

Group351.children.append(OrientationInterpolator376)
OrientationInterpolator377 = x3d.OrientationInterpolator()
OrientationInterpolator377.DEF = "Yaw_vl5_YawInterpolator"
OrientationInterpolator377.key = [0,0.2,0.4,0.5,0.6,0.8,1]
OrientationInterpolator377.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group351.children.append(OrientationInterpolator377)
OrientationInterpolator378 = x3d.OrientationInterpolator()
OrientationInterpolator378.DEF = "Yaw_vc6_YawInterpolator"
OrientationInterpolator378.key = [0,0.2,0.4,0.5,0.6,0.8,1]
OrientationInterpolator378.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group351.children.append(OrientationInterpolator378)
OrientationInterpolator379 = x3d.OrientationInterpolator()
OrientationInterpolator379.DEF = "Yaw_l_thumb1_PitchInterpolator"
OrientationInterpolator379.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator379.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group351.children.append(OrientationInterpolator379)
OrientationInterpolator380 = x3d.OrientationInterpolator()
OrientationInterpolator380.DEF = "Yaw_r_thumb1_PitchInterpolator"
OrientationInterpolator380.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator380.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group351.children.append(OrientationInterpolator380)

Scene34.children.append(Group351)
Group381 = x3d.Group()
Group381.DEF = "RollsAnimation"
TimeSensor382 = x3d.TimeSensor()
TimeSensor382.DEF = "RollTimer"
TimeSensor382.cycleInterval = 5.73
TimeSensor382.loop = True

Group381.children.append(TimeSensor382)
OrientationInterpolator383 = x3d.OrientationInterpolator()
OrientationInterpolator383.DEF = "Roll_r_metatarsal_PitchInterpolator"
OrientationInterpolator383.key = [0,0.2,0.4,0.6,0.7,1]
OrientationInterpolator383.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group381.children.append(OrientationInterpolator383)
OrientationInterpolator384 = x3d.OrientationInterpolator()
OrientationInterpolator384.DEF = "Rolls_r_ankle_RotationInterpolator"
OrientationInterpolator384.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator384.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,1.5000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,1.5000,0.0000,0.0000,1.0000,0.0000)

Group381.children.append(OrientationInterpolator384)
OrientationInterpolator385 = x3d.OrientationInterpolator()
OrientationInterpolator385.DEF = "Rolls_r_knee_RotationInterpolator"
OrientationInterpolator385.key = [0,0.5,1]
OrientationInterpolator385.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group381.children.append(OrientationInterpolator385)
OrientationInterpolator386 = x3d.OrientationInterpolator()
OrientationInterpolator386.DEF = "Rolls_r_hip_RotationInterpolator"
OrientationInterpolator386.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator386.keyValue = (0.0000,0.0000,-1.0000,0.0000,0.0000,0.0000,-1.0000,1.5000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,-1.0000,1.5000,0.0000,0.0000,1.0000,0.0000)

Group381.children.append(OrientationInterpolator386)
OrientationInterpolator387 = x3d.OrientationInterpolator()
OrientationInterpolator387.DEF = "Rolls_l_ankle_RotationInterpolator"
OrientationInterpolator387.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator387.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,-1.0000,1.5000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,-1.0000,1.5000,0.0000,0.0000,1.0000,0.0000)

Group381.children.append(OrientationInterpolator387)
OrientationInterpolator388 = x3d.OrientationInterpolator()
OrientationInterpolator388.DEF = "Rolls_l_knee_RotationInterpolator"
OrientationInterpolator388.key = [0,0.5,1]
OrientationInterpolator388.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group381.children.append(OrientationInterpolator388)
OrientationInterpolator389 = x3d.OrientationInterpolator()
OrientationInterpolator389.DEF = "Rolls_l_hip_RotationInterpolator"
OrientationInterpolator389.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator389.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,1.5000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,1.5000,0.0000,0.0000,1.0000,0.0000)

Group381.children.append(OrientationInterpolator389)
OrientationInterpolator390 = x3d.OrientationInterpolator()
OrientationInterpolator390.DEF = "Rolls_r_wrist_RotationInterpolator"
OrientationInterpolator390.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator390.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,-1.0000,1.5000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,1.5000,0.0000,0.0000,1.0000,0.0000)

Group381.children.append(OrientationInterpolator390)
OrientationInterpolator391 = x3d.OrientationInterpolator()
OrientationInterpolator391.DEF = "Rolls_r_elbow_RotationInterpolator"
OrientationInterpolator391.key = [0,0.5,1]
OrientationInterpolator391.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group381.children.append(OrientationInterpolator391)
OrientationInterpolator392 = x3d.OrientationInterpolator()
OrientationInterpolator392.DEF = "Rolls_r_shoulder_RotationInterpolator"
OrientationInterpolator392.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator392.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,-1.0000,1.5000,0.0000,0.0000,-1.0000,3.0000,0.0000,0.0000,-1.0000,1.5000,0.0000,0.0000,1.0000,0.0000)

Group381.children.append(OrientationInterpolator392)
OrientationInterpolator393 = x3d.OrientationInterpolator()
OrientationInterpolator393.DEF = "Rolls_l_wrist_RotationInterpolator"
OrientationInterpolator393.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator393.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,1.5000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,-1.0000,1.5000,0.0000,0.0000,1.0000,0.0000)

Group381.children.append(OrientationInterpolator393)
OrientationInterpolator394 = x3d.OrientationInterpolator()
OrientationInterpolator394.DEF = "Rolls_l_elbow_RotationInterpolator"
OrientationInterpolator394.key = [0,0.5,1]
OrientationInterpolator394.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group381.children.append(OrientationInterpolator394)
OrientationInterpolator395 = x3d.OrientationInterpolator()
OrientationInterpolator395.DEF = "Rolls_l_shoulder_RotationInterpolator"
OrientationInterpolator395.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator395.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,1.5000,0.0000,0.0000,1.0000,3.0000,0.0000,0.0000,1.0000,1.5000,0.0000,0.0000,1.0000,0.0000)

Group381.children.append(OrientationInterpolator395)
OrientationInterpolator396 = x3d.OrientationInterpolator()
OrientationInterpolator396.DEF = "Rolls_head_RotationInterpolator"
OrientationInterpolator396.key = [0,0.5,1]
OrientationInterpolator396.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group381.children.append(OrientationInterpolator396)
OrientationInterpolator397 = x3d.OrientationInterpolator()
OrientationInterpolator397.DEF = "Rolls_neck_RotationInterpolator"
OrientationInterpolator397.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator397.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,1.2500,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,-1.0000,1.2500,0.0000,0.0000,1.0000,0.0000)

Group381.children.append(OrientationInterpolator397)
OrientationInterpolator398 = x3d.OrientationInterpolator()
OrientationInterpolator398.DEF = "Rolls_lower_body_RotationInterpolator"
OrientationInterpolator398.key = [0,0.5,1]
OrientationInterpolator398.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group381.children.append(OrientationInterpolator398)
OrientationInterpolator399 = x3d.OrientationInterpolator()
OrientationInterpolator399.DEF = "Rolls_upper_body_RotationInterpolator"
OrientationInterpolator399.key = [0,0.5,1]
OrientationInterpolator399.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group381.children.append(OrientationInterpolator399)
OrientationInterpolator400 = x3d.OrientationInterpolator()
OrientationInterpolator400.DEF = "Rolls_whole_body_RotationInterpolator"
OrientationInterpolator400.key = [0,0.5,1]
OrientationInterpolator400.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group381.children.append(OrientationInterpolator400)
PositionInterpolator401 = x3d.PositionInterpolator()
PositionInterpolator401.DEF = "Rolls_whole_body_TranslationInterpolator"
PositionInterpolator401.key = [0,0.125,0.25,0.375,0.5,0.625,0.75,0.875,1]
PositionInterpolator401.keyValue = (0.0000,0.0000,0.0000,0.0000,-0.2500,0.0000,0.0000,-0.8000,0.0000,0.0000,-0.2500,0.0000,0.0000,0.0000,0.0000,0.0000,-0.2500,0.0000,0.0000,-0.8000,0.0000,0.0000,-0.2500,0.0000,0.0000,0.0000,0.0000)

Group381.children.append(PositionInterpolator401)
OrientationInterpolator402 = x3d.OrientationInterpolator()
OrientationInterpolator402.DEF = "Roll_l_sternoclavicular_RollInterpolator"
OrientationInterpolator402.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator402.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.2000,0.0000,0.0000,1.0000,0.2200,0.0000,0.0000,1.0000,0.2000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group381.children.append(OrientationInterpolator402)
OrientationInterpolator403 = x3d.OrientationInterpolator()
OrientationInterpolator403.DEF = "Roll_l_acromioclavicular_RollInterpolator"
OrientationInterpolator403.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator403.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0500,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group381.children.append(OrientationInterpolator403)
OrientationInterpolator404 = x3d.OrientationInterpolator()
OrientationInterpolator404.DEF = "Roll_r_sternoclavicular_RollInterpolator"
OrientationInterpolator404.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator404.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,-0.2000,0.0000,0.0000,1.0000,-0.2200,0.0000,0.0000,1.0000,-0.2000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group381.children.append(OrientationInterpolator404)
OrientationInterpolator405 = x3d.OrientationInterpolator()
OrientationInterpolator405.DEF = "Roll_r_acromioclavicular_RollInterpolator"
OrientationInterpolator405.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator405.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,-0.0500,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group381.children.append(OrientationInterpolator405)
OrientationInterpolator406 = x3d.OrientationInterpolator()
OrientationInterpolator406.DEF = "Roll_sacroiliac_YawInterpolator"
OrientationInterpolator406.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator406.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group381.children.append(OrientationInterpolator406)
OrientationInterpolator407 = x3d.OrientationInterpolator()
OrientationInterpolator407.DEF = "Roll_vl5_YawInterpolator"
OrientationInterpolator407.key = [0,0.2,0.4,0.5,0.6,0.8,1]
OrientationInterpolator407.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group381.children.append(OrientationInterpolator407)
OrientationInterpolator408 = x3d.OrientationInterpolator()
OrientationInterpolator408.DEF = "Roll_vc6_YawInterpolator"
OrientationInterpolator408.key = [0,0.2,0.4,0.5,0.6,0.8,1]
OrientationInterpolator408.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group381.children.append(OrientationInterpolator408)
OrientationInterpolator409 = x3d.OrientationInterpolator()
OrientationInterpolator409.DEF = "Roll_l_thumb1_PitchInterpolator"
OrientationInterpolator409.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator409.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group381.children.append(OrientationInterpolator409)
OrientationInterpolator410 = x3d.OrientationInterpolator()
OrientationInterpolator410.DEF = "Roll_r_thumb1_PitchInterpolator"
OrientationInterpolator410.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator410.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group381.children.append(OrientationInterpolator410)

Scene34.children.append(Group381)
Group411 = x3d.Group()
Group411.DEF = "WalkAnimation"
TimeSensor412 = x3d.TimeSensor()
TimeSensor412.DEF = "WalkTimer"
TimeSensor412.cycleInterval = 1.73
TimeSensor412.loop = True

Group411.children.append(TimeSensor412)
OrientationInterpolator413 = x3d.OrientationInterpolator()
OrientationInterpolator413.DEF = "Walk_r_metatarsal_PitchInterpolator"
OrientationInterpolator413.key = [0,0.2,0.4,0.6,0.7,1]
OrientationInterpolator413.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group411.children.append(OrientationInterpolator413)
OrientationInterpolator414 = x3d.OrientationInterpolator()
OrientationInterpolator414.DEF = "Walk_r_ankle_RotationInterpolator"
OrientationInterpolator414.key = [0,0.125,0.2083,0.375,0.4583,0.5,0.6667,0.75,0.7917,0.9167,1]
OrientationInterpolator414.keyValue = (0.0000,0.0000,1.0000,0.0000,-1.0000,0.0000,0.0000,0.3533,-1.0000,0.0000,0.0000,0.1072,1.0000,0.0000,0.0000,0.2612,1.0000,0.0000,0.0000,0.1268,-1.0000,0.0000,0.0000,0.0179,-1.0000,0.0000,0.0000,0.0582,-1.0000,0.0000,0.0000,0.2398,-1.0000,0.0000,0.0000,0.3500,-1.0000,0.0000,0.0000,0.3322,0.0000,0.0000,1.0000,0.0000)

Group411.children.append(OrientationInterpolator414)
OrientationInterpolator415 = x3d.OrientationInterpolator()
OrientationInterpolator415.DEF = "Walk_r_knee_RotationInterpolator"
OrientationInterpolator415.key = [0,0.125,0.2083,0.2917,0.375,0.5,0.6667,0.7917,0.9167,1]
OrientationInterpolator415.keyValue = (1.0000,0.0000,0.0000,0.8573,1.0000,0.0000,0.0000,0.8926,1.0000,0.0000,0.0000,0.5351,1.0000,0.0000,0.0000,0.1756,1.0000,0.0000,0.0000,0.1194,1.0000,0.0000,0.0000,0.3153,1.0000,0.0000,0.0000,0.0935,1.0000,0.0000,0.0000,0.0856,1.0000,0.0000,0.0000,0.2475,1.0000,0.0000,0.0000,0.8573)

Group411.children.append(OrientationInterpolator415)
OrientationInterpolator416 = x3d.OrientationInterpolator()
OrientationInterpolator416.DEF = "Walk_r_hip_RotationInterpolator"
OrientationInterpolator416.key = [0,0.125,0.2083,0.2917,0.375,0.5,0.6667,0.7917,0.9167,1]
OrientationInterpolator416.keyValue = (-0.5831,0.0351,0.8116,0.1481,-0.9950,0.0230,0.0967,0.4683,-1.0000,0.0019,0.0080,0.4732,-0.9980,-0.0158,-0.0610,0.5079,-0.9911,-0.0354,-0.1286,0.5419,-0.9131,-0.0624,-0.4030,0.3361,-0.4306,-0.0796,-0.8990,0.0704,1.0000,0.0000,0.0000,0.2571,0.9891,-0.0280,0.1444,0.3879,-0.5831,0.0351,0.8116,0.1481)

Group411.children.append(OrientationInterpolator416)
OrientationInterpolator417 = x3d.OrientationInterpolator()
OrientationInterpolator417.DEF = "Walk_l_ankle_RotationInterpolator"
OrientationInterpolator417.key = [0,0.125,0.2083,0.375,0.6667,0.9167,1]
OrientationInterpolator417.keyValue = (-1.0000,0.0000,0.0000,0.0671,-1.0000,0.0000,0.0000,0.2152,-1.0000,0.0000,0.0000,0.3184,-1.0000,0.0000,0.0000,0.4717,-1.0000,0.0000,0.0000,0.2912,1.0000,0.0000,0.0000,0.1222,-1.0000,0.0000,0.0000,0.0671)

Group411.children.append(OrientationInterpolator417)
OrientationInterpolator418 = x3d.OrientationInterpolator()
OrientationInterpolator418.DEF = "Walk_l_knee_RotationInterpolator"
OrientationInterpolator418.key = [0,0.2083,0.375,0.5,0.6667,0.7917,0.9167,1]
OrientationInterpolator418.keyValue = (1.0000,0.0000,0.0000,0.3226,1.0000,0.0000,0.0000,0.1556,1.0000,0.0000,0.0000,0.0868,1.0000,0.0000,0.0000,0.8751,1.0000,0.0000,0.0000,1.1310,1.0000,0.0000,0.0000,0.0996,1.0000,0.0000,0.0000,0.3942,1.0000,0.0000,0.0000,0.3226)

Group411.children.append(OrientationInterpolator418)
OrientationInterpolator419 = x3d.OrientationInterpolator()
OrientationInterpolator419.DEF = "Walk_l_hip_RotationInterpolator"
OrientationInterpolator419.key = [0,0.25,0.375,0.5,0.6667,0.7917,0.9167,1]
OrientationInterpolator419.keyValue = (-0.8730,0.0609,0.4840,0.2865,0.9963,-0.0106,0.0848,0.2488,0.9965,0.0159,-0.0822,0.3836,-0.7018,-0.0322,-0.7117,0.1289,-1.0000,0.0000,0.0000,0.5518,-0.9964,0.0223,0.0817,0.5351,-0.9809,0.0491,0.1881,0.5204,-0.8730,0.0609,0.4840,0.2865)

Group411.children.append(OrientationInterpolator419)
OrientationInterpolator420 = x3d.OrientationInterpolator()
OrientationInterpolator420.DEF = "Walk_lower_body_RotationInterpolator"
OrientationInterpolator420.key = [0,0.5,1]
OrientationInterpolator420.keyValue = (0.0000,0.0000,-1.0000,0.1056,0.0000,0.0000,1.0000,0.0902,0.0000,0.0000,-1.0000,0.1056)

Group411.children.append(OrientationInterpolator420)
OrientationInterpolator421 = x3d.OrientationInterpolator()
OrientationInterpolator421.DEF = "Walk_r_wrist_RotationInterpolator"
OrientationInterpolator421.key = [0,0.375,0.9167,1]
OrientationInterpolator421.keyValue = (-0.8129,0.4759,-0.3357,0.1346,0.1533,-0.9878,0.0258,0.3902,-0.5701,0.7604,-0.3110,0.3660,-0.8129,0.4759,-0.3357,0.1346)

Group411.children.append(OrientationInterpolator421)
OrientationInterpolator422 = x3d.OrientationInterpolator()
OrientationInterpolator422.DEF = "Walk_r_elbow_RotationInterpolator"
OrientationInterpolator422.key = [0,0.375,0.9167,1]
OrientationInterpolator422.keyValue = (-1.0000,0.0000,0.0000,0.4115,-1.0000,0.0000,0.0000,0.0925,-1.0000,0.0000,0.0000,0.5726,-1.0000,0.0000,0.0000,0.4115)

Group411.children.append(OrientationInterpolator422)
OrientationInterpolator423 = x3d.OrientationInterpolator()
OrientationInterpolator423.DEF = "Walk_r_shoulder_RotationInterpolator"
OrientationInterpolator423.key = [0,0.375,0.9167,1]
OrientationInterpolator423.keyValue = (-1.0000,0.0000,0.0000,0.0935,1.0000,0.0000,0.0000,0.3197,-1.0000,0.0000,0.0000,0.1564,-1.0000,0.0000,0.0000,0.0935)

Group411.children.append(OrientationInterpolator423)
OrientationInterpolator424 = x3d.OrientationInterpolator()
OrientationInterpolator424.DEF = "Walk_l_wrist_RotationInterpolator"
OrientationInterpolator424.key = [0,0.375,0.9167,1]
OrientationInterpolator424.keyValue = (0.0000,-1.0000,0.0000,0.4611,-0.3302,-0.9275,0.1755,0.5389,0.0328,-0.9993,-0.0172,0.4920,0.0000,-1.0000,0.0000,0.4611)

Group411.children.append(OrientationInterpolator424)
OrientationInterpolator425 = x3d.OrientationInterpolator()
OrientationInterpolator425.DEF = "Walk_l_elbow_RotationInterpolator"
OrientationInterpolator425.key = [0,0.375,0.9167,1]
OrientationInterpolator425.keyValue = (-1.0000,0.0000,0.0000,0.0660,-1.0000,0.0000,0.0000,0.4884,-1.0000,0.0000,0.0000,0.0178,-1.0000,0.0000,0.0000,0.0660)

Group411.children.append(OrientationInterpolator425)
OrientationInterpolator426 = x3d.OrientationInterpolator()
OrientationInterpolator426.DEF = "Walk_l_shoulder_RotationInterpolator"
OrientationInterpolator426.key = [0,0.375,0.9167,1]
OrientationInterpolator426.keyValue = (1.0000,0.0000,0.0000,0.1189,-1.0000,0.0000,0.0000,0.1861,1.0000,0.0000,0.0000,0.3357,1.0000,0.0000,0.0000,0.1189)

Group411.children.append(OrientationInterpolator426)
OrientationInterpolator427 = x3d.OrientationInterpolator()
OrientationInterpolator427.DEF = "Walk_head_RotationInterpolator"
OrientationInterpolator427.key = [0,0.375,0.4167,0.5,0.5833,0.6667,0.75,0.8333,0.9167,1]
OrientationInterpolator427.keyValue = (0.0000,-1.0000,0.0000,0.0864,0.0000,1.0000,0.0000,0.1825,0.0000,1.0000,0.0000,0.1505,0.0000,1.0000,0.0000,0.1053,0.0000,1.0000,0.0000,0.0439,0.0000,-1.0000,0.0000,0.0312,0.0000,-1.0000,0.0000,0.0794,0.0000,-1.0000,0.0000,0.1616,0.0000,-1.0000,0.0000,0.1550,0.0000,-1.0000,0.0000,0.0864)

Group411.children.append(OrientationInterpolator427)
OrientationInterpolator428 = x3d.OrientationInterpolator()
OrientationInterpolator428.DEF = "Walk_neck_RotationInterpolator"
OrientationInterpolator428.key = [0,1]
OrientationInterpolator428.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group411.children.append(OrientationInterpolator428)
OrientationInterpolator429 = x3d.OrientationInterpolator()
OrientationInterpolator429.DEF = "Walk_upper_body_RotationInterpolator"
OrientationInterpolator429.key = [0,0.2083,0.375,0.75,0.8333,1]
OrientationInterpolator429.keyValue = (0.0000,1.0000,0.0000,0.0826,-0.0197,-0.5974,0.8017,0.0823,0.0093,-0.9648,0.2627,0.1734,-0.0124,0.9549,-0.2968,0.0873,-0.0081,0.9691,-0.2463,0.1580,0.0000,1.0000,0.0000,0.0826)

Group411.children.append(OrientationInterpolator429)
OrientationInterpolator430 = x3d.OrientationInterpolator()
OrientationInterpolator430.DEF = "Walk_whole_body_RotationInterpolator"
OrientationInterpolator430.key = [0,1]
OrientationInterpolator430.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group411.children.append(OrientationInterpolator430)
PositionInterpolator431 = x3d.PositionInterpolator()
PositionInterpolator431.DEF = "Walk_whole_body_TranslationInterpolator"
PositionInterpolator431.key = [0,0.04167,0.125,0.1667,0.2083,0.25,0.2917,0.375,0.4583,0.5,0.5417,0.5833,0.625,0.7083,0.75,0.7917,0.875,0.9167,1]
PositionInterpolator431.keyValue = (0.0000,-0.0093,0.0000,0.0000,-0.0039,0.0000,0.0000,-0.0088,0.0000,0.0000,-0.0149,0.0000,0.0000,-0.0264,0.0000,0.0000,-0.0393,0.0000,0.0000,-0.0502,0.0000,0.0000,-0.0747,0.0000,0.0000,-0.0273,0.0000,0.0000,-0.0161,0.0000,0.0000,-0.0113,0.0000,0.0000,-0.0058,0.0000,0.0000,-0.0020,0.0000,0.0000,-0.0026,0.0000,0.0000,-0.0143,0.0000,0.0000,-0.0380,0.0000,0.0000,-0.0565,0.0000,0.0000,-0.0450,0.0000,0.0000,-0.0093,0.0000)

Group411.children.append(PositionInterpolator431)
OrientationInterpolator432 = x3d.OrientationInterpolator()
OrientationInterpolator432.DEF = "Walk_l_sternoclavicular_RollInterpolator"
OrientationInterpolator432.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator432.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group411.children.append(OrientationInterpolator432)
OrientationInterpolator433 = x3d.OrientationInterpolator()
OrientationInterpolator433.DEF = "Walk_l_acromioclavicular_RollInterpolator"
OrientationInterpolator433.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator433.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group411.children.append(OrientationInterpolator433)
OrientationInterpolator434 = x3d.OrientationInterpolator()
OrientationInterpolator434.DEF = "Walk_r_sternoclavicular_RollInterpolator"
OrientationInterpolator434.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator434.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group411.children.append(OrientationInterpolator434)
OrientationInterpolator435 = x3d.OrientationInterpolator()
OrientationInterpolator435.DEF = "Walk_r_acromioclavicular_RollInterpolator"
OrientationInterpolator435.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator435.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group411.children.append(OrientationInterpolator435)
OrientationInterpolator436 = x3d.OrientationInterpolator()
OrientationInterpolator436.DEF = "Walk_sacroiliac_YawInterpolator"
OrientationInterpolator436.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator436.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group411.children.append(OrientationInterpolator436)
OrientationInterpolator437 = x3d.OrientationInterpolator()
OrientationInterpolator437.DEF = "Walk_vl5_YawInterpolator"
OrientationInterpolator437.key = [0,0.2,0.4,0.5,0.6,0.8,1]
OrientationInterpolator437.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group411.children.append(OrientationInterpolator437)
OrientationInterpolator438 = x3d.OrientationInterpolator()
OrientationInterpolator438.DEF = "Walk_vc6_YawInterpolator"
OrientationInterpolator438.key = [0,0.2,0.4,0.5,0.6,0.8,1]
OrientationInterpolator438.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group411.children.append(OrientationInterpolator438)
OrientationInterpolator439 = x3d.OrientationInterpolator()
OrientationInterpolator439.DEF = "Walk_l_thumb1_PitchInterpolator"
OrientationInterpolator439.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator439.keyValue = (1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.2500,1.0000,0.0000,0.0000,0.5000,1.0000,0.0000,0.0000,0.7000,1.0000,0.0000,0.0000,0.2000,1.0000,0.0000,0.0000,0.0000)

Group411.children.append(OrientationInterpolator439)
OrientationInterpolator440 = x3d.OrientationInterpolator()
OrientationInterpolator440.DEF = "Walk_r_thumb1_PitchInterpolator"
OrientationInterpolator440.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator440.keyValue = (1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.2500,1.0000,0.0000,0.0000,0.5000,1.0000,0.0000,0.0000,0.7000,1.0000,0.0000,0.0000,0.2000,1.0000,0.0000,0.0000,0.0000)

Group411.children.append(OrientationInterpolator440)

Scene34.children.append(Group411)
Group441 = x3d.Group()
Group441.DEF = "RunAnimation"
TimeSensor442 = x3d.TimeSensor()
TimeSensor442.DEF = "RunTimer"
TimeSensor442.cycleInterval = 0.9
TimeSensor442.loop = True

Group441.children.append(TimeSensor442)
OrientationInterpolator443 = x3d.OrientationInterpolator()
OrientationInterpolator443.DEF = "Run_r_metatarsal_PitchInterpolator"
OrientationInterpolator443.key = [0,0.2,0.4,0.6,0.7,1]
OrientationInterpolator443.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group441.children.append(OrientationInterpolator443)
OrientationInterpolator444 = x3d.OrientationInterpolator()
OrientationInterpolator444.DEF = "Run_l_hip_RotationInterpolator_Run"
OrientationInterpolator444.key = [0,0.2182,0.4909,0.7455,1]
OrientationInterpolator444.keyValue = (-0.9900,0.0330,0.0400,1.4200,-0.9900,0.1328,0.0670,0.4200,0.9900,0.0140,0.0090,0.9000,-0.9900,0.0703,0.0500,0.7000,-0.9900,0.0330,0.0400,1.4200)

Group441.children.append(OrientationInterpolator444)
OrientationInterpolator445 = x3d.OrientationInterpolator()
OrientationInterpolator445.DEF = "Run_l_knee_RotationInterpolator_Run"
OrientationInterpolator445.key = [0,0.2182,0.4909,0.7455,1]
OrientationInterpolator445.keyValue = (1.0000,0.0000,0.0000,1.0100,1.0000,0.0000,0.0000,0.4260,1.0000,0.0000,0.0000,0.7050,1.0000,0.0000,0.0000,2.1790,1.0000,0.0000,0.0000,1.0100)

Group441.children.append(OrientationInterpolator445)
OrientationInterpolator446 = x3d.OrientationInterpolator()
OrientationInterpolator446.DEF = "Run_l_ankle_RotationInterpolator_Run"
OrientationInterpolator446.key = [0,0.22,0.3,0.4,1]
OrientationInterpolator446.keyValue = (1.0000,0.0000,0.0000,0.0374,-1.0000,0.0000,0.0000,0.1037,-1.0000,0.0000,0.0000,0.4328,1.0000,0.0000,0.0000,0.1929,1.0000,0.0000,0.0000,0.0357)

Group441.children.append(OrientationInterpolator446)
OrientationInterpolator447 = x3d.OrientationInterpolator()
OrientationInterpolator447.DEF = "Run_r_hip_RotationInterpolator_Run"
OrientationInterpolator447.key = [0,0.2545,0.4909,0.7091,1]
OrientationInterpolator447.keyValue = (0.9900,-0.0140,0.0090,0.9000,-0.9900,-0.0703,-0.0500,0.7000,-0.9900,-0.0330,0.0400,1.4200,-0.9900,-0.1328,-0.0670,0.4200,0.9900,-0.0140,0.0090,0.9000)

Group441.children.append(OrientationInterpolator447)
OrientationInterpolator448 = x3d.OrientationInterpolator()
OrientationInterpolator448.DEF = "Run_r_knee_RotationInterpolator_Run"
OrientationInterpolator448.key = [0,0.2545,0.4909,0.7091,1]
OrientationInterpolator448.keyValue = (1.0000,0.0000,0.0000,0.7050,1.0000,0.0000,0.0000,2.1790,1.0000,0.0000,0.0000,1.0100,1.0000,0.0000,0.0000,0.4260,1.0000,0.0000,0.0000,0.7050)

Group441.children.append(OrientationInterpolator448)
OrientationInterpolator449 = x3d.OrientationInterpolator()
OrientationInterpolator449.DEF = "Run_r_ankle_RotationInterpolator_Run"
OrientationInterpolator449.key = [0,0.4,0.71,0.8,0.82,1]
OrientationInterpolator449.keyValue = (1.0000,0.0000,0.0000,0.2323,-1.0000,0.0000,0.0000,0.0784,-1.0000,0.0000,0.0000,0.3200,-1.0000,0.0000,0.0000,0.3740,-1.0000,0.0000,0.0000,0.3478,1.0000,0.0000,0.0000,0.2323)

Group441.children.append(OrientationInterpolator449)
OrientationInterpolator450 = x3d.OrientationInterpolator()
OrientationInterpolator450.DEF = "Run_l_shoulder_RotationInterpolator_Run"
OrientationInterpolator450.key = [0,0.2182,0.4909,0.7455,1]
OrientationInterpolator450.keyValue = (0.9900,-0.0740,0.2500,1.5000,0.9900,-0.0920,0.4400,0.3000,-0.9900,0.1360,0.2500,0.8500,0.9900,-0.0810,0.3800,0.4000,0.9900,-0.0740,0.2500,1.5000)

Group441.children.append(OrientationInterpolator450)
OrientationInterpolator451 = x3d.OrientationInterpolator()
OrientationInterpolator451.DEF = "Run_l_elbow_RotationInterpolator_Run"
OrientationInterpolator451.key = [0,0.2182,0.4909,0.7455,1]
OrientationInterpolator451.keyValue = (-1.0000,0.0000,0.0000,1.8500,-0.9900,-0.1900,0.1800,1.3500,-1.0000,0.0000,0.0000,0.9750,-0.9900,-0.0900,-0.0200,1.5500,-1.0000,0.0000,0.0000,1.8500)

Group441.children.append(OrientationInterpolator451)
OrientationInterpolator452 = x3d.OrientationInterpolator()
OrientationInterpolator452.DEF = "Run_l_wrist_RotationInterpolator_Run"
OrientationInterpolator452.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator452.keyValue = (-0.2500,-1.0000,0.0800,0.1400,0.2500,1.0000,0.0800,0.1400,0.0000,0.0000,1.0000,0.0000,-0.2500,1.0000,0.0800,-0.1400,-0.2500,1.0000,0.0800,0.1400)

Group441.children.append(OrientationInterpolator452)
OrientationInterpolator453 = x3d.OrientationInterpolator()
OrientationInterpolator453.DEF = "Run_r_shoulder_RotationInterpolator_Run"
OrientationInterpolator453.key = [0,0.2545,0.4909,0.7091,1]
OrientationInterpolator453.keyValue = (-0.9900,-0.1360,-0.2500,0.8500,0.9900,0.0810,-0.3800,0.4000,0.9900,0.0740,-0.2500,1.5000,0.9900,0.0810,-0.3800,0.4000,-0.9900,-0.1360,-0.2500,0.8500)

Group441.children.append(OrientationInterpolator453)
OrientationInterpolator454 = x3d.OrientationInterpolator()
OrientationInterpolator454.DEF = "Run_r_elbow_RotationInterpolator_Run"
OrientationInterpolator454.key = [0,0.2545,0.4909,0.7091,1]
OrientationInterpolator454.keyValue = (-1.0000,0.0000,0.0000,0.9750,-0.9900,0.0900,0.0200,1.5500,-1.0000,0.0000,0.0000,1.8500,-0.9900,0.1900,-0.1800,1.3500,-1.0000,0.0000,0.0000,0.9750)

Group441.children.append(OrientationInterpolator454)
OrientationInterpolator455 = x3d.OrientationInterpolator()
OrientationInterpolator455.DEF = "Run_r_wrist_RotationInterpolator_Run"
OrientationInterpolator455.key = [0,1]
OrientationInterpolator455.keyValue = (-0.9177,-0.2372,-0.3185,0.2143,-0.9177,-0.2372,-0.3185,0.2143)

Group441.children.append(OrientationInterpolator455)
OrientationInterpolator456 = x3d.OrientationInterpolator()
OrientationInterpolator456.DEF = "Run_lower_body_RotationInterpolator_Run"
OrientationInterpolator456.key = [0,0.2182,0.4909,0.7455,1]
OrientationInterpolator456.keyValue = (0.0000,-1.0000,0.0000,0.1250,0.0000,0.0000,1.0000,0.0000,0.0000,1.0000,0.0000,0.1250,0.0000,0.0000,1.0000,0.0000,0.0000,-1.0000,0.0000,0.1250)

Group441.children.append(OrientationInterpolator456)
OrientationInterpolator457 = x3d.OrientationInterpolator()
OrientationInterpolator457.DEF = "Run_head_RotationInterpolator_Run"
OrientationInterpolator457.key = [0,0.2545,0.4909,0.7091,1]
OrientationInterpolator457.keyValue = (1.0000,0.0000,0.0000,0.0800,1.0000,0.0000,0.0000,0.1200,1.0000,0.0000,0.0000,0.3000,1.0000,0.0000,0.0000,0.3000,1.0000,0.0000,0.0000,0.0800)

Group441.children.append(OrientationInterpolator457)
OrientationInterpolator458 = x3d.OrientationInterpolator()
OrientationInterpolator458.DEF = "Run_neck_RotationInterpolator_Run"
OrientationInterpolator458.key = [0,0.2545,0.4909,0.7091,1]
OrientationInterpolator458.keyValue = (0.7000,0.0000,0.0000,0.4000,-0.7000,-0.7000,0.0000,0.4000,0.0000,0.0000,0.0000,0.4000,-0.7000,0.7000,0.0000,0.4000,0.7000,0.0000,0.0000,0.4000)

Group441.children.append(OrientationInterpolator458)
OrientationInterpolator459 = x3d.OrientationInterpolator()
OrientationInterpolator459.DEF = "Run_upper_body_RotationInterpolator_Run"
OrientationInterpolator459.key = [0,0.2545,0.4909,0.7636,1]
OrientationInterpolator459.keyValue = (0.9700,0.6500,0.0860,0.5000,0.9000,0.0030,-0.0200,0.3800,0.9500,-0.6800,-0.0860,0.5000,0.9000,0.0040,-0.0250,0.4000,0.9700,0.6500,0.0860,0.5000)

Group441.children.append(OrientationInterpolator459)
OrientationInterpolator460 = x3d.OrientationInterpolator()
OrientationInterpolator460.DEF = "Run_whole_body_RotationInterpolator_Run"
OrientationInterpolator460.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator460.keyValue = (1.0000,0.0000,0.0000,0.0600,1.0000,0.0000,0.0000,0.1670,1.0000,0.0000,0.0000,0.0600,1.0000,0.0000,0.0000,0.1680,1.0000,0.0000,0.0000,0.0600)

Group441.children.append(OrientationInterpolator460)
PositionInterpolator461 = x3d.PositionInterpolator()
PositionInterpolator461.DEF = "Run_whole_body_TranslationInterpolator_Run"
PositionInterpolator461.key = [0,0.22,0.3,0.31,0.5,0.69,0.7,0.78,1]
PositionInterpolator461.keyValue = (0.0000,-0.0100,0.0000,0.0000,-0.0370,0.0000,0.0000,-0.0490,0.0000,0.0000,-0.0370,0.0000,0.0000,-0.0100,0.0000,0.0000,-0.0370,0.0000,0.0000,-0.0490,0.0000,0.0000,-0.0370,0.0000,0.0000,-0.0100,0.0000)

Group441.children.append(PositionInterpolator461)
OrientationInterpolator462 = x3d.OrientationInterpolator()
OrientationInterpolator462.DEF = "Run_l_sternoclavicular_RollInterpolator"
OrientationInterpolator462.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator462.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group441.children.append(OrientationInterpolator462)
OrientationInterpolator463 = x3d.OrientationInterpolator()
OrientationInterpolator463.DEF = "Run_l_acromioclavicular_RollInterpolator"
OrientationInterpolator463.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator463.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group441.children.append(OrientationInterpolator463)
OrientationInterpolator464 = x3d.OrientationInterpolator()
OrientationInterpolator464.DEF = "Run_r_sternoclavicular_RollInterpolator"
OrientationInterpolator464.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator464.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group441.children.append(OrientationInterpolator464)
OrientationInterpolator465 = x3d.OrientationInterpolator()
OrientationInterpolator465.DEF = "Run_r_acromioclavicular_RollInterpolator"
OrientationInterpolator465.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator465.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group441.children.append(OrientationInterpolator465)
OrientationInterpolator466 = x3d.OrientationInterpolator()
OrientationInterpolator466.DEF = "Run_sacroiliac_YawInterpolator"
OrientationInterpolator466.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator466.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group441.children.append(OrientationInterpolator466)
OrientationInterpolator467 = x3d.OrientationInterpolator()
OrientationInterpolator467.DEF = "Run_vl5_YawInterpolator"
OrientationInterpolator467.key = [0,0.2,0.4,0.5,0.6,0.8,1]
OrientationInterpolator467.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group441.children.append(OrientationInterpolator467)
OrientationInterpolator468 = x3d.OrientationInterpolator()
OrientationInterpolator468.DEF = "Run_vc6_YawInterpolator"
OrientationInterpolator468.key = [0,0.2,0.4,0.5,0.6,0.8,1]
OrientationInterpolator468.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group441.children.append(OrientationInterpolator468)
OrientationInterpolator469 = x3d.OrientationInterpolator()
OrientationInterpolator469.DEF = "Run_l_thumb1_PitchInterpolator"
OrientationInterpolator469.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator469.keyValue = (1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.2500,1.0000,0.0000,0.0000,0.7000,1.0000,0.0000,0.0000,0.2700,1.0000,0.0000,0.0000,0.2000,1.0000,0.0000,0.0000,0.0000)

Group441.children.append(OrientationInterpolator469)
OrientationInterpolator470 = x3d.OrientationInterpolator()
OrientationInterpolator470.DEF = "Run_r_thumb1_PitchInterpolator"
OrientationInterpolator470.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator470.keyValue = (1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.2500,1.0000,0.0000,0.0000,0.7000,1.0000,0.0000,0.0000,0.2700,1.0000,0.0000,0.0000,0.2000,1.0000,0.0000,0.0000,0.0000)

Group441.children.append(OrientationInterpolator470)

Scene34.children.append(Group441)
Group471 = x3d.Group()
Group471.DEF = "JumpAnimation"
TimeSensor472 = x3d.TimeSensor()
TimeSensor472.DEF = "JumpTimer"
TimeSensor472.cycleInterval = 3.73
TimeSensor472.loop = True

Group471.children.append(TimeSensor472)
OrientationInterpolator473 = x3d.OrientationInterpolator()
OrientationInterpolator473.DEF = "Jump_r_metatarsal_PitchInterpolator"
OrientationInterpolator473.key = [0,0.2,0.4,0.6,0.7,1]
OrientationInterpolator473.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group471.children.append(OrientationInterpolator473)
OrientationInterpolator474 = x3d.OrientationInterpolator()
OrientationInterpolator474.DEF = "Jump_r_ankle_RotationInterpolator"
OrientationInterpolator474.key = [0,0.1,0.15,0.25,0.28,0.32,0.35,0.64,0.76,0.84,0.88,0.92,0.96,1]
OrientationInterpolator474.keyValue = (0.0000,0.0000,1.0000,0.0000,-1.0000,0.0000,0.0000,0.6735,-1.0000,0.0000,0.0000,0.6735,-1.0000,0.0000,0.0000,0.3527,-1.0000,0.0000,0.0000,0.3038,-1.0000,0.0000,0.0000,0.0796,1.0000,0.0000,0.0000,1.3000,1.0000,0.0000,0.0000,0.6509,1.0000,0.0000,0.0000,0.3001,-1.0000,0.0000,0.0000,0.2087,-1.0000,0.0000,0.0000,0.3756,-1.0000,0.0000,0.0000,0.3279,-1.0000,0.0000,0.0000,0.1193,0.0000,0.0000,1.0000,0.0000)

Group471.children.append(OrientationInterpolator474)
OrientationInterpolator475 = x3d.OrientationInterpolator()
OrientationInterpolator475.DEF = "Jump_r_knee_RotationInterpolator"
OrientationInterpolator475.key = [0,0.2,0.25,0.3,0.64,0.76,0.88,1]
OrientationInterpolator475.keyValue = (0.0000,0.0000,1.0000,0.0000,1.0000,0.0000,0.0000,2.5000,1.0000,0.0000,0.0000,1.7000,0.0000,0.0000,1.0000,0.0000,1.0000,0.0000,0.0000,0.9507,1.0000,0.0000,0.0000,0.5845,1.0000,0.0000,0.0000,0.9054,0.0000,0.0000,1.0000,0.0000)

Group471.children.append(OrientationInterpolator475)
OrientationInterpolator476 = x3d.OrientationInterpolator()
OrientationInterpolator476.DEF = "Jump_r_hip_RotationInterpolator"
OrientationInterpolator476.key = [0,0.18,0.24,0.26,0.28,0.32,0.48,0.64,0.76,0.88,1]
OrientationInterpolator476.keyValue = (0.0000,0.0000,1.0000,0.0000,-1.0000,0.0000,0.0000,1.6300,-1.0000,0.0000,0.0000,1.7000,-1.0000,0.0000,0.0000,1.5500,-1.0000,0.0000,0.0000,0.8943,-1.0000,0.0000,0.0000,0.3698,0.0000,0.0000,1.0000,0.0000,-1.0000,0.0000,0.0000,0.4963,-1.0000,0.0000,0.0000,0.3829,-1.0000,0.0000,0.0000,0.5169,0.0000,0.0000,1.0000,0.0000)

Group471.children.append(OrientationInterpolator476)
OrientationInterpolator477 = x3d.OrientationInterpolator()
OrientationInterpolator477.DEF = "Jump_l_ankle_RotationInterpolator"
OrientationInterpolator477.key = [0,0.28,0.32,0.36,0.4,0.44,0.48,0.64,0.76,0.84,0.88,0.92,0.96,1]
OrientationInterpolator477.keyValue = (0.0000,0.0000,1.0000,0.0000,-1.0000,0.0000,0.0000,0.6250,-1.0000,0.0000,0.0000,0.6250,-1.0000,0.0000,0.0000,0.3364,-1.0000,0.0000,0.0000,0.2742,-1.0000,0.0000,0.0000,0.0508,1.0000,0.0000,0.0000,0.2833,1.0000,0.0000,0.0000,0.6667,1.0000,0.0000,0.0000,0.2833,-1.0000,0.0000,0.0000,0.2108,-1.0000,0.0000,0.0000,0.3750,-1.0000,0.0000,0.0000,0.3146,-1.0000,0.0000,0.0000,0.1174,0.0000,0.0000,1.0000,0.0000)

Group471.children.append(OrientationInterpolator477)
OrientationInterpolator478 = x3d.OrientationInterpolator()
OrientationInterpolator478.DEF = "Jump_l_knee_RotationInterpolator"
OrientationInterpolator478.key = [0,0.28,0.32,0.48,0.64,0.76,0.88,1]
OrientationInterpolator478.keyValue = (0.0000,0.0000,1.0000,0.0000,1.0000,0.0000,0.0000,2.0470,1.0000,0.0000,0.0000,2.0470,0.0000,0.0000,1.0000,0.0000,1.0000,0.0000,0.0000,1.5660,1.0000,0.0000,0.0000,0.5913,1.0000,0.0000,0.0000,0.9235,0.0000,0.0000,1.0000,0.0000)

Group471.children.append(OrientationInterpolator478)
OrientationInterpolator479 = x3d.OrientationInterpolator()
OrientationInterpolator479.DEF = "Jump_l_hip_RotationInterpolator"
OrientationInterpolator479.key = [0,0.28,0.32,0.36,0.4,0.44,0.48,0.64,0.76,0.88,1]
OrientationInterpolator479.keyValue = (0.0000,0.0000,1.0000,0.0000,1.0000,0.0000,0.0000,4.3490,1.0000,0.0000,0.0000,4.3490,1.0000,0.0000,0.0000,4.6150,-1.0000,0.0000,0.0000,0.9136,-1.0000,0.0000,0.0000,0.3614,0.0000,0.0000,1.0000,0.0000,-1.0000,0.0000,0.0000,0.7869,-1.0000,0.0000,0.0000,0.3918,-1.0000,0.0000,0.0000,0.5433,0.0000,0.0000,1.0000,0.0000)

Group471.children.append(OrientationInterpolator479)
OrientationInterpolator480 = x3d.OrientationInterpolator()
OrientationInterpolator480.DEF = "Jump_lower_body_RotationInterpolator"
OrientationInterpolator480.key = [0,0.28,0.32,0.48,0.76,1]
OrientationInterpolator480.keyValue = (0.0000,0.0000,1.0000,0.0000,1.0000,0.0000,0.0000,0.1892,1.0000,0.0000,0.0000,0.1892,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group471.children.append(OrientationInterpolator480)
OrientationInterpolator481 = x3d.OrientationInterpolator()
OrientationInterpolator481.DEF = "Jump_r_wrist_RotationInterpolator"
OrientationInterpolator481.key = [0,0.28,0.32,0.64,0.76,1]
OrientationInterpolator481.keyValue = (0.0000,0.0000,1.0000,0.0000,-0.0585,0.9839,-0.1688,1.8596,-0.0585,0.9839,-0.1688,1.8596,-0.0022,0.9980,-0.0630,1.4607,0.0000,1.0000,0.0000,0.4973,0.0000,0.0000,1.0000,0.0000)

Group471.children.append(OrientationInterpolator481)
OrientationInterpolator482 = x3d.OrientationInterpolator()
OrientationInterpolator482.DEF = "Jump_r_elbow_RotationInterpolator"
OrientationInterpolator482.key = [0,0.28,0.32,0.64,0.76,1]
OrientationInterpolator482.keyValue = (0.0000,0.0000,1.0000,0.0000,-1.0000,0.0000,0.0000,0.0415,-1.0000,0.0000,0.0000,0.0415,-1.0000,0.0000,0.0000,0.5855,-1.0000,0.0000,0.0000,0.5852,0.0000,0.0000,1.0000,0.0000)

Group471.children.append(OrientationInterpolator482)
OrientationInterpolator483 = x3d.OrientationInterpolator()
OrientationInterpolator483.DEF = "Jump_r_shoulder_RotationInterpolator"
OrientationInterpolator483.key = [0,0.28,0.32,0.64,0.76,0.88,1]
OrientationInterpolator483.keyValue = (0.0000,0.0000,1.0000,0.0000,0.9992,0.0204,0.0356,4.6880,0.9992,0.0204,0.0356,4.6880,0.9989,-0.0462,0.0052,4.0790,-0.8687,-0.2525,-0.4261,1.5010,-0.9410,-0.2893,-0.1754,0.4788,0.0000,0.0000,1.0000,0.0000)

Group471.children.append(OrientationInterpolator483)
OrientationInterpolator484 = x3d.OrientationInterpolator()
OrientationInterpolator484.DEF = "Jump_l_wrist_RotationInterpolator"
OrientationInterpolator484.key = [0,0.48,0.52,0.64,0.76,0.88,1]
OrientationInterpolator484.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0673,0.9895,-0.1281,4.1557,0.0673,0.9895,-0.1281,4.1557,0.0036,0.9999,0.0136,4.5822,0.0000,-1.0000,0.0000,0.6559,-0.0005,-1.0000,0.0013,1.2840,0.0000,0.0000,1.0000,0.0000)

Group471.children.append(OrientationInterpolator484)
OrientationInterpolator485 = x3d.OrientationInterpolator()
OrientationInterpolator485.DEF = "Jump_l_elbow_RotationInterpolator"
OrientationInterpolator485.key = [0,0.28,0.32,0.58,0.72,1]
OrientationInterpolator485.keyValue = (0.0000,0.0000,1.0000,0.0000,-1.0000,0.0000,0.0000,1.1300,-1.0000,0.0000,0.0000,1.7000,-1.0000,0.0000,0.0000,1.7000,-1.0000,0.0000,0.0000,0.4000,0.0000,0.0000,1.0000,0.0000)

Group471.children.append(OrientationInterpolator485)
OrientationInterpolator486 = x3d.OrientationInterpolator()
OrientationInterpolator486.DEF = "Jump_l_shoulder_RotationInterpolator"
OrientationInterpolator486.key = [0,0.28,0.32,0.64,0.76,0.88,1]
OrientationInterpolator486.keyValue = (0.0000,0.0000,1.0000,0.0000,-0.9987,0.0255,0.0450,1.5700,-0.9987,0.0255,0.0450,1.5700,1.0000,0.0004,0.0031,4.1140,-0.8413,0.3238,0.4329,1.4530,-0.8770,0.4198,0.2337,0.6009,0.0000,0.0000,1.0000,0.0000)

Group471.children.append(OrientationInterpolator486)
OrientationInterpolator487 = x3d.OrientationInterpolator()
OrientationInterpolator487.DEF = "Jump_head_RotationInterpolator"
OrientationInterpolator487.key = [0,0.28,0.32,0.48,0.76,1]
OrientationInterpolator487.keyValue = (0.0000,0.0000,1.0000,0.0000,-1.0000,0.0000,0.0000,0.5989,-1.0000,0.0000,0.0000,0.5989,-1.0000,0.0000,0.0000,0.3216,1.0000,0.0000,0.0000,0.0650,0.0000,0.0000,1.0000,0.0000)

Group471.children.append(OrientationInterpolator487)
OrientationInterpolator488 = x3d.OrientationInterpolator()
OrientationInterpolator488.DEF = "Jump_neck_RotationInterpolator"
OrientationInterpolator488.key = [0,0.28,0.32,0.48,0.76,1]
OrientationInterpolator488.keyValue = (0.0000,0.0000,1.0000,0.0000,-1.0000,0.0000,0.0000,0.1942,-1.0000,0.0000,0.0000,0.1942,0.0000,0.0000,1.0000,0.0000,1.0000,0.0000,0.0000,0.2284,0.0000,0.0000,1.0000,0.0000)

Group471.children.append(OrientationInterpolator488)
OrientationInterpolator489 = x3d.OrientationInterpolator()
OrientationInterpolator489.DEF = "Jump_upper_body_RotationInterpolator"
OrientationInterpolator489.key = [0,0.22,0.28,0.34,0.71,0.88,1]
OrientationInterpolator489.keyValue = (0.0000,0.0000,1.0000,0.0000,1.0000,0.0000,0.0000,1.0500,1.0000,0.0000,0.0000,1.0510,-1.0000,0.0000,0.0000,0.2570,1.0000,0.0000,0.0000,0.2171,1.0000,0.0000,0.0000,0.3465,0.0000,0.0000,1.0000,0.0000)

Group471.children.append(OrientationInterpolator489)
OrientationInterpolator490 = x3d.OrientationInterpolator()
OrientationInterpolator490.DEF = "Jump_whole_body_RotationInterpolator"
OrientationInterpolator490.key = [0,0.28,0.32,0.48,0.64,0.76,1]
OrientationInterpolator490.keyValue = (0.0000,0.0000,1.0000,0.0000,1.0000,0.0000,0.0000,0.3273,1.0000,0.0000,0.0000,0.3273,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group471.children.append(OrientationInterpolator490)
PositionInterpolator491 = x3d.PositionInterpolator()
PositionInterpolator491.DEF = "Jump_whole_body_TranslationInterpolator"
PositionInterpolator491.key = [0,0.04,0.07,0.11,0.15,0.19,0.22,0.25,0.27,0.31,0.33,0.35,0.38,0.53,0.544,0.76,0.8,0.84,0.88,0.92,0.96,1]
PositionInterpolator491.keyValue = (0.0000,0.0000,0.0000,0.0000,-0.0126,-0.0129,0.0000,-0.0471,-0.0374,-0.0003,-0.1049,-0.0535,-0.0006,-0.1892,-0.0656,-0.0008,-0.2860,-0.0628,-0.0010,-0.3795,-0.0515,-0.0011,-0.4484,-0.0366,-0.0011,-0.4484,-0.0366,-0.0011,-0.2500,-0.1499,-0.0009,-0.0500,-0.0636,-0.0005,0.1500,-0.0549,0.0005,0.5500,0.0273,0.0002,1.3850,0.0069,0.0002,1.3950,0.0069,0.0000,0.3500,0.0215,0.0000,-0.0130,-0.0106,0.0000,-0.0693,-0.0106,0.0001,-0.1037,-0.0051,0.0001,-0.0720,-0.0076,0.0001,-0.0163,-0.0049,0.0000,0.0000,0.0000)

Group471.children.append(PositionInterpolator491)
OrientationInterpolator492 = x3d.OrientationInterpolator()
OrientationInterpolator492.DEF = "Jump_l_sternoclavicular_RollInterpolator"
OrientationInterpolator492.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator492.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.2000,0.0000,0.0000,1.0000,0.2200,0.0000,0.0000,1.0000,0.2000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group471.children.append(OrientationInterpolator492)
OrientationInterpolator493 = x3d.OrientationInterpolator()
OrientationInterpolator493.DEF = "Jump_l_acromioclavicular_RollInterpolator"
OrientationInterpolator493.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator493.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0500,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group471.children.append(OrientationInterpolator493)
OrientationInterpolator494 = x3d.OrientationInterpolator()
OrientationInterpolator494.DEF = "Jump_r_sternoclavicular_RollInterpolator"
OrientationInterpolator494.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator494.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,-0.2000,0.0000,0.0000,1.0000,-0.2200,0.0000,0.0000,1.0000,-0.2000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group471.children.append(OrientationInterpolator494)
OrientationInterpolator495 = x3d.OrientationInterpolator()
OrientationInterpolator495.DEF = "Jump_r_acromioclavicular_RollInterpolator"
OrientationInterpolator495.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator495.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,-0.0500,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group471.children.append(OrientationInterpolator495)
OrientationInterpolator496 = x3d.OrientationInterpolator()
OrientationInterpolator496.DEF = "Jump_sacroiliac_YawInterpolator"
OrientationInterpolator496.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator496.keyValue = (0.0000,1.0000,0.0000,0.0000,0.0000,-1.0000,0.0000,0.1000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,-1.0000,0.2400,0.0000,-1.0000,0.0000,0.4000,0.0000,1.0000,0.0000,0.0000)

Group471.children.append(OrientationInterpolator496)
OrientationInterpolator497 = x3d.OrientationInterpolator()
OrientationInterpolator497.DEF = "Jump_vl5_YawInterpolator"
OrientationInterpolator497.key = [0,0.2,0.4,0.5,0.6,0.8,1]
OrientationInterpolator497.keyValue = (0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,-0.1000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.6000,0.0000,1.0000,0.0000,0.1000,0.0000,1.0000,0.0000,0.0000)

Group471.children.append(OrientationInterpolator497)
OrientationInterpolator498 = x3d.OrientationInterpolator()
OrientationInterpolator498.DEF = "Jump_vc6_YawInterpolator"
OrientationInterpolator498.key = [0,0.2,0.4,0.5,0.6,0.8,1]
OrientationInterpolator498.keyValue = (0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.8000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,-1.0000,0.0000,0.0000,0.6000,0.0000,-1.0000,0.0000,0.8000,0.0000,1.0000,0.0000,0.0000)

Group471.children.append(OrientationInterpolator498)
OrientationInterpolator499 = x3d.OrientationInterpolator()
OrientationInterpolator499.DEF = "Jump_l_thumb1_PitchInterpolator"
OrientationInterpolator499.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator499.keyValue = (1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.5000,1.0000,0.0000,0.0000,1.1000,1.0000,0.0000,0.0000,0.7000,1.0000,0.0000,0.0000,0.2000,1.0000,0.0000,0.0000,0.0000)

Group471.children.append(OrientationInterpolator499)
OrientationInterpolator500 = x3d.OrientationInterpolator()
OrientationInterpolator500.DEF = "Jump_r_thumb1_PitchInterpolator"
OrientationInterpolator500.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator500.keyValue = (1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.5000,1.0000,0.0000,0.0000,1.1000,1.0000,0.0000,0.0000,0.7000,1.0000,0.0000,0.0000,0.2000,1.0000,0.0000,0.0000,0.0000)

Group471.children.append(OrientationInterpolator500)

Scene34.children.append(Group471)
Group501 = x3d.Group()
Group501.DEF = "KickAnimation"
TimeSensor502 = x3d.TimeSensor()
TimeSensor502.DEF = "KickTimer"
TimeSensor502.cycleInterval = 3.73
TimeSensor502.loop = True

Group501.children.append(TimeSensor502)
OrientationInterpolator503 = x3d.OrientationInterpolator()
OrientationInterpolator503.DEF = "Kick_l_sternoclavicular_RollInterpolator"
OrientationInterpolator503.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator503.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.2000,0.0000,0.0000,1.0000,0.2200,0.0000,0.0000,1.0000,0.2000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group501.children.append(OrientationInterpolator503)
OrientationInterpolator504 = x3d.OrientationInterpolator()
OrientationInterpolator504.DEF = "Kick_l_acromioclavicular_RollInterpolator"
OrientationInterpolator504.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator504.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0500,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group501.children.append(OrientationInterpolator504)
OrientationInterpolator505 = x3d.OrientationInterpolator()
OrientationInterpolator505.DEF = "Kick_l_shoulder_RollInterpolator"
OrientationInterpolator505.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator505.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,1.7600,-0.2500,0.0000,1.0000,1.7600,0.0000,0.0000,1.0000,1.2560,0.0000,0.0000,1.0000,0.0500,0.0000,0.0000,1.0000,0.0000)

Group501.children.append(OrientationInterpolator505)
OrientationInterpolator506 = x3d.OrientationInterpolator()
OrientationInterpolator506.DEF = "Kick_l_ForeArm_PitchInterpolator"
OrientationInterpolator506.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator506.keyValue = (1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,-0.5500,-1.0000,0.2500,0.0000,2.5500,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000)

Group501.children.append(OrientationInterpolator506)
OrientationInterpolator507 = x3d.OrientationInterpolator()
OrientationInterpolator507.DEF = "Kick_l_wrist_RollInterpolator"
OrientationInterpolator507.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator507.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,1.0000,0.0000,0.5500,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group501.children.append(OrientationInterpolator507)
OrientationInterpolator508 = x3d.OrientationInterpolator()
OrientationInterpolator508.DEF = "Kick_l_thumb1_PitchInterpolator"
OrientationInterpolator508.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator508.keyValue = (1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.5000,1.0000,0.0000,0.0000,1.1000,1.0000,0.0000,0.0000,0.7000,1.0000,0.0000,0.0000,0.2000,1.0000,0.0000,0.0000,0.0000)

Group501.children.append(OrientationInterpolator508)
OrientationInterpolator509 = x3d.OrientationInterpolator()
OrientationInterpolator509.DEF = "Kick_r_sternoclavicular_RollInterpolator"
OrientationInterpolator509.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator509.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,-0.2000,0.0000,0.0000,1.0000,-0.2200,0.0000,0.0000,1.0000,-0.2000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group501.children.append(OrientationInterpolator509)
OrientationInterpolator510 = x3d.OrientationInterpolator()
OrientationInterpolator510.DEF = "Kick_r_acromioclavicular_RollInterpolator"
OrientationInterpolator510.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator510.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,-0.0500,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group501.children.append(OrientationInterpolator510)
OrientationInterpolator511 = x3d.OrientationInterpolator()
OrientationInterpolator511.DEF = "Kick_r_shoulder_RollInterpolator"
OrientationInterpolator511.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator511.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,-1.7600,0.2500,0.0000,1.0000,-1.7600,0.0000,0.0000,1.0000,-1.2560,0.0000,0.0000,1.0000,-0.0500,0.0000,0.0000,1.0000,0.0000)

Group501.children.append(OrientationInterpolator511)
OrientationInterpolator512 = x3d.OrientationInterpolator()
OrientationInterpolator512.DEF = "Kick_r_ForeArm_PitchInterpolator"
OrientationInterpolator512.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator512.keyValue = (1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,-0.5500,1.0000,0.2500,0.0000,-2.5500,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000)

Group501.children.append(OrientationInterpolator512)
OrientationInterpolator513 = x3d.OrientationInterpolator()
OrientationInterpolator513.DEF = "Kick_r_wrist_RollInterpolator"
OrientationInterpolator513.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator513.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,1.0000,0.0000,-0.5500,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group501.children.append(OrientationInterpolator513)
OrientationInterpolator514 = x3d.OrientationInterpolator()
OrientationInterpolator514.DEF = "Kick_r_thumb1_PitchInterpolator"
OrientationInterpolator514.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator514.keyValue = (1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.5000,1.0000,0.0000,0.0000,1.1000,1.0000,0.0000,0.0000,0.7000,1.0000,0.0000,0.0000,0.2000,1.0000,0.0000,0.0000,0.0000)

Group501.children.append(OrientationInterpolator514)
OrientationInterpolator515 = x3d.OrientationInterpolator()
OrientationInterpolator515.DEF = "Kick_r_hip_PitchInterpolator"
OrientationInterpolator515.key = [0,0.2,0.3,0.5,0.6,0.9,1]
OrientationInterpolator515.keyValue = (1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.9000,-1.0000,0.0000,0.0000,1.7500,-1.0000,0.0000,0.0000,2.2500,-1.0000,0.0000,0.0000,2.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000)

Group501.children.append(OrientationInterpolator515)
OrientationInterpolator516 = x3d.OrientationInterpolator()
OrientationInterpolator516.DEF = "Kick_r_knee_PitchInterpolator"
OrientationInterpolator516.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator516.keyValue = (0.0000,0.0000,1.0000,0.0000,1.0000,0.0000,0.0000,1.9500,1.0000,0.0000,0.0000,1.7500,-1.0000,0.0000,0.0000,0.2800,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000)

Group501.children.append(OrientationInterpolator516)
OrientationInterpolator517 = x3d.OrientationInterpolator()
OrientationInterpolator517.DEF = "Kick_l_hip_PitchInterpolator"
OrientationInterpolator517.key = [0,0.2,0.3,0.5,0.6,0.9,1]
OrientationInterpolator517.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group501.children.append(OrientationInterpolator517)
OrientationInterpolator518 = x3d.OrientationInterpolator()
OrientationInterpolator518.DEF = "Kick_l_knee_PitchInterpolator"
OrientationInterpolator518.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator518.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group501.children.append(OrientationInterpolator518)
OrientationInterpolator519 = x3d.OrientationInterpolator()
OrientationInterpolator519.DEF = "Kick_r_ankle_PitchInterpolator"
OrientationInterpolator519.key = [0,0.2,0.4,0.6,0.7,1]
OrientationInterpolator519.keyValue = (0.0000,0.0000,1.0000,0.0000,-1.0000,0.0000,0.0000,0.9000,-1.0000,0.0000,0.0000,0.9500,1.0000,0.0000,0.0000,0.7500,-1.0000,0.0000,0.0000,0.0500,1.0000,0.0000,0.0000,0.0000)

Group501.children.append(OrientationInterpolator519)
OrientationInterpolator520 = x3d.OrientationInterpolator()
OrientationInterpolator520.DEF = "Kick_r_metatarsal_PitchInterpolator"
OrientationInterpolator520.key = [0,0.2,0.4,0.6,0.7,1]
OrientationInterpolator520.keyValue = (1.0000,0.0000,0.0000,0.0000,-1.0000,0.0000,0.0000,0.5000,-1.0000,0.0000,0.0000,0.7000,1.0000,0.0000,0.0000,0.7500,-1.0000,0.0000,0.0000,0.2000,1.0000,0.0000,0.0000,0.0000)

Group501.children.append(OrientationInterpolator520)
OrientationInterpolator521 = x3d.OrientationInterpolator()
OrientationInterpolator521.DEF = "Kick_sacroiliac_YawInterpolator"
OrientationInterpolator521.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator521.keyValue = (0.0000,1.0000,0.0000,0.0000,0.0000,-1.0000,0.0000,0.1000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,-1.0000,0.2400,0.0000,-1.0000,0.0000,0.4000,0.0000,1.0000,0.0000,0.0000)

Group501.children.append(OrientationInterpolator521)
OrientationInterpolator522 = x3d.OrientationInterpolator()
OrientationInterpolator522.DEF = "Kick_vl5_YawInterpolator"
OrientationInterpolator522.key = [0,0.2,0.4,0.5,0.6,0.8,1]
OrientationInterpolator522.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group501.children.append(OrientationInterpolator522)
OrientationInterpolator523 = x3d.OrientationInterpolator()
OrientationInterpolator523.DEF = "Kick_vc6_YawInterpolator"
OrientationInterpolator523.key = [0,0.2,0.4,0.5,0.6,0.8,1]
OrientationInterpolator523.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group501.children.append(OrientationInterpolator523)
OrientationInterpolator524 = x3d.OrientationInterpolator()
OrientationInterpolator524.DEF = "Kick_lower_body_RotationInterpolator"
OrientationInterpolator524.key = [0,0.5,1]
OrientationInterpolator524.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group501.children.append(OrientationInterpolator524)
OrientationInterpolator525 = x3d.OrientationInterpolator()
OrientationInterpolator525.DEF = "Kick_upper_body_RotationInterpolator"
OrientationInterpolator525.key = [0,0.5,1]
OrientationInterpolator525.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group501.children.append(OrientationInterpolator525)
OrientationInterpolator526 = x3d.OrientationInterpolator()
OrientationInterpolator526.DEF = "Kick_whole_body_RotationInterpolator"
OrientationInterpolator526.key = [0,0.5,1]
OrientationInterpolator526.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group501.children.append(OrientationInterpolator526)
PositionInterpolator527 = x3d.PositionInterpolator()
PositionInterpolator527.DEF = "Kick_whole_body_TranslationInterpolator"
PositionInterpolator527.key = [0,0.5,1]
PositionInterpolator527.keyValue = (0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000)

Group501.children.append(PositionInterpolator527)
OrientationInterpolator528 = x3d.OrientationInterpolator()
OrientationInterpolator528.DEF = "Kick_neck_RotationInterpolator"
OrientationInterpolator528.key = [0,0.25,0.55,1]
OrientationInterpolator528.keyValue = (0.0000,0.0000,1.0000,0.0000,1.0000,0.0000,0.0000,0.7000,1.0000,0.0000,0.0000,0.5000,0.0000,0.0000,1.0000,0.0000)

Group501.children.append(OrientationInterpolator528)

Scene34.children.append(Group501)
Group529 = x3d.Group()
Group529.DEF = "Interface"
Transform530 = x3d.Transform()
Transform530.DEF = "CoordinateSystemFloor"
Transform530.scale = [0.1,0.1,0.1]
Shape531 = x3d.Shape()
Shape531.DEF = "AxisLinesShape"
#RGB lines showing XYZ axes
IndexedLineSet532 = x3d.IndexedLineSet()
IndexedLineSet532.colorIndex = [0,1,2]
IndexedLineSet532.colorPerVertex = False
IndexedLineSet532.coordIndex = [0,1,-1,0,2,-1,0,3,-1]
Coordinate533 = x3d.Coordinate()
Coordinate533.point = (0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000)

IndexedLineSet532.coord = Coordinate533
Color534 = x3d.Color()
Color534.color = [1,0,0,0,0.6,0,0,0,1]

IndexedLineSet532.color = Color534

Shape531.geometry = IndexedLineSet532

Transform530.children.append(Shape531)

Group529.children.append(Transform530)
ProximitySensor535 = x3d.ProximitySensor()
ProximitySensor535.DEF = "HudProx"
ProximitySensor535.size = [50,50,50]

Group529.children.append(ProximitySensor535)
Transform536 = x3d.Transform()
Transform536.DEF = "HudXform"
Transform536.rotation = [0,1,0,0.78]
Transform536.translation = [2,1,2]
Transform537 = x3d.Transform()
Transform537.scale = [0.02,0.02,0.02]
Transform537.translation = [-0.4,-0.01,-0.75]
Transform538 = x3d.Transform()
Transform538.DEF = "Stand_Text"
Transform538.translation = [0,-0.9,0]
TouchSensor539 = x3d.TouchSensor()
TouchSensor539.DEF = "Stand_Touch"

Transform538.children.append(TouchSensor539)
Shape540 = x3d.Shape()
Shape540.DEF = "StandText"
Appearance541 = x3d.Appearance()
Material542 = x3d.Material()
Material542.DEF = "text_color"
Material542.ambientIntensity = 1
Material542.diffuseColor = [0.819,0.521,0.169]
Material542.emissiveColor = [0.819,0.521,0.169]
Material542.specularColor = [0.819,0.521,0.169]

Appearance541.material = Material542

Shape540.appearance = Appearance541
Text543 = x3d.Text()
Text543.string = ["Stand"]
FontStyle544 = x3d.FontStyle()
FontStyle544.family = ["SANS"]

Text543.fontStyle = FontStyle544

Shape540.geometry = Text543

Transform538.children.append(Shape540)
Shape545 = x3d.Shape()
Shape545.DEF = "Stand_Back"
Appearance546 = x3d.Appearance()
Material547 = x3d.Material()
Material547.DEF = "Clear"
Material547.ambientIntensity = 1
Material547.diffuseColor = [0,0.5,0]
Material547.emissiveColor = [0,0.5,0]
Material547.transparency = 0.8

Appearance546.material = Material547

Shape545.appearance = Appearance546
IndexedFaceSet548 = x3d.IndexedFaceSet()
IndexedFaceSet548.DEF = "Backing"
IndexedFaceSet548.coordIndex = [0,1,2,3,-1]
Coordinate549 = x3d.Coordinate()
Coordinate549.point = (-0.2000,-0.2500,-0.0100,3.0000,-0.2500,-0.0100,3.0000,1.0000,-0.0100,-0.2000,1.0000,-0.0100)

IndexedFaceSet548.coord = Coordinate549

Shape545.geometry = IndexedFaceSet548

Transform538.children.append(Shape545)

Transform537.children.append(Transform538)
Transform550 = x3d.Transform()
Transform550.DEF = "Pitch_Text"
Transform550.translation = [0,-2.4,0]
TouchSensor551 = x3d.TouchSensor()
TouchSensor551.DEF = "Pitch_Touch"

Transform550.children.append(TouchSensor551)
Shape552 = x3d.Shape()
Shape552.DEF = "PitchText"
Appearance553 = x3d.Appearance()
Material554 = x3d.Material()
Material554.USE = "text_color"

Appearance553.material = Material554

Shape552.appearance = Appearance553
Text555 = x3d.Text()
Text555.string = ["Pitch"]
FontStyle556 = x3d.FontStyle()
FontStyle556.family = ["SANS"]

Text555.fontStyle = FontStyle556

Shape552.geometry = Text555

Transform550.children.append(Shape552)
Shape557 = x3d.Shape()
Shape557.DEF = "Pitch_Back"
Appearance558 = x3d.Appearance()
Material559 = x3d.Material()
Material559.USE = "Clear"

Appearance558.material = Material559

Shape557.appearance = Appearance558
IndexedFaceSet560 = x3d.IndexedFaceSet()
IndexedFaceSet560.USE = "Backing"

Shape557.geometry = IndexedFaceSet560

Transform550.children.append(Shape557)

Transform537.children.append(Transform550)
Transform561 = x3d.Transform()
Transform561.DEF = "Yaw_Text"
Transform561.translation = [0,-3.8,0]
TouchSensor562 = x3d.TouchSensor()
TouchSensor562.DEF = "Yaw_Touch"

Transform561.children.append(TouchSensor562)
Shape563 = x3d.Shape()
Shape563.DEF = "YawText"
Appearance564 = x3d.Appearance()
Material565 = x3d.Material()
Material565.USE = "text_color"

Appearance564.material = Material565

Shape563.appearance = Appearance564
Text566 = x3d.Text()
Text566.string = ["Yaw"]
FontStyle567 = x3d.FontStyle()
FontStyle567.family = ["SANS"]

Text566.fontStyle = FontStyle567

Shape563.geometry = Text566

Transform561.children.append(Shape563)
Shape568 = x3d.Shape()
Shape568.DEF = "Yaw_Back"
Appearance569 = x3d.Appearance()
Material570 = x3d.Material()
Material570.USE = "Clear"

Appearance569.material = Material570

Shape568.appearance = Appearance569
IndexedFaceSet571 = x3d.IndexedFaceSet()
IndexedFaceSet571.USE = "Backing"

Shape568.geometry = IndexedFaceSet571

Transform561.children.append(Shape568)

Transform537.children.append(Transform561)
Transform572 = x3d.Transform()
Transform572.DEF = "Roll_Text"
Transform572.translation = [0,-5.2,0]
TouchSensor573 = x3d.TouchSensor()
TouchSensor573.DEF = "Roll_Touch"

Transform572.children.append(TouchSensor573)
Shape574 = x3d.Shape()
Shape574.DEF = "RollText"
Appearance575 = x3d.Appearance()
Material576 = x3d.Material()
Material576.USE = "text_color"

Appearance575.material = Material576

Shape574.appearance = Appearance575
Text577 = x3d.Text()
Text577.string = ["Roll"]
FontStyle578 = x3d.FontStyle()
FontStyle578.family = ["SANS"]

Text577.fontStyle = FontStyle578

Shape574.geometry = Text577

Transform572.children.append(Shape574)
Shape579 = x3d.Shape()
Shape579.DEF = "Roll_Back"
Appearance580 = x3d.Appearance()
Material581 = x3d.Material()
Material581.USE = "Clear"

Appearance580.material = Material581

Shape579.appearance = Appearance580
IndexedFaceSet582 = x3d.IndexedFaceSet()
IndexedFaceSet582.USE = "Backing"

Shape579.geometry = IndexedFaceSet582

Transform572.children.append(Shape579)

Transform537.children.append(Transform572)
Transform583 = x3d.Transform()
Transform583.DEF = "Walk_Text"
Transform583.translation = [0,-6.6,0]
TouchSensor584 = x3d.TouchSensor()
TouchSensor584.DEF = "Walk_Touch"

Transform583.children.append(TouchSensor584)
Shape585 = x3d.Shape()
Shape585.DEF = "WalkText"
Appearance586 = x3d.Appearance()
Material587 = x3d.Material()
Material587.USE = "text_color"

Appearance586.material = Material587

Shape585.appearance = Appearance586
Text588 = x3d.Text()
Text588.string = ["Walk"]
FontStyle589 = x3d.FontStyle()
FontStyle589.family = ["SANS"]

Text588.fontStyle = FontStyle589

Shape585.geometry = Text588

Transform583.children.append(Shape585)
Shape590 = x3d.Shape()
Shape590.DEF = "Walk_Back"
Appearance591 = x3d.Appearance()
Material592 = x3d.Material()
Material592.USE = "Clear"

Appearance591.material = Material592

Shape590.appearance = Appearance591
IndexedFaceSet593 = x3d.IndexedFaceSet()
IndexedFaceSet593.USE = "Backing"

Shape590.geometry = IndexedFaceSet593

Transform583.children.append(Shape590)

Transform537.children.append(Transform583)
Transform594 = x3d.Transform()
Transform594.DEF = "Run_Text"
Transform594.translation = [0,-8,0]
TouchSensor595 = x3d.TouchSensor()
TouchSensor595.DEF = "Run_Touch"

Transform594.children.append(TouchSensor595)
Shape596 = x3d.Shape()
Shape596.DEF = "RunText"
Appearance597 = x3d.Appearance()
Material598 = x3d.Material()
Material598.USE = "text_color"

Appearance597.material = Material598

Shape596.appearance = Appearance597
Text599 = x3d.Text()
Text599.string = ["Run"]
FontStyle600 = x3d.FontStyle()
FontStyle600.family = ["SANS"]

Text599.fontStyle = FontStyle600

Shape596.geometry = Text599

Transform594.children.append(Shape596)
Shape601 = x3d.Shape()
Shape601.DEF = "Run_Back"
Appearance602 = x3d.Appearance()
Material603 = x3d.Material()
Material603.USE = "Clear"

Appearance602.material = Material603

Shape601.appearance = Appearance602
IndexedFaceSet604 = x3d.IndexedFaceSet()
IndexedFaceSet604.USE = "Backing"

Shape601.geometry = IndexedFaceSet604

Transform594.children.append(Shape601)

Transform537.children.append(Transform594)
Transform605 = x3d.Transform()
Transform605.DEF = "Jump_Text"
Transform605.translation = [0,-9.4,0]
TouchSensor606 = x3d.TouchSensor()
TouchSensor606.DEF = "Jump_Touch"

Transform605.children.append(TouchSensor606)
Shape607 = x3d.Shape()
Shape607.DEF = "JumpText"
Appearance608 = x3d.Appearance()
Material609 = x3d.Material()
Material609.USE = "text_color"

Appearance608.material = Material609

Shape607.appearance = Appearance608
Text610 = x3d.Text()
Text610.string = ["Jump"]
FontStyle611 = x3d.FontStyle()
FontStyle611.family = ["SANS"]

Text610.fontStyle = FontStyle611

Shape607.geometry = Text610

Transform605.children.append(Shape607)
Shape612 = x3d.Shape()
Shape612.DEF = "Jump_Back"
Appearance613 = x3d.Appearance()
Material614 = x3d.Material()
Material614.USE = "Clear"

Appearance613.material = Material614

Shape612.appearance = Appearance613
IndexedFaceSet615 = x3d.IndexedFaceSet()
IndexedFaceSet615.USE = "Backing"

Shape612.geometry = IndexedFaceSet615

Transform605.children.append(Shape612)

Transform537.children.append(Transform605)
Transform616 = x3d.Transform()
Transform616.DEF = "Kick_Text"
Transform616.translation = [0,-10.8,0]
TouchSensor617 = x3d.TouchSensor()
TouchSensor617.DEF = "Kick_Touch"

Transform616.children.append(TouchSensor617)
Shape618 = x3d.Shape()
Shape618.DEF = "KickText"
Appearance619 = x3d.Appearance()
Material620 = x3d.Material()
Material620.USE = "text_color"

Appearance619.material = Material620

Shape618.appearance = Appearance619
Text621 = x3d.Text()
Text621.string = ["Kick"]
FontStyle622 = x3d.FontStyle()
FontStyle622.family = ["SANS"]

Text621.fontStyle = FontStyle622

Shape618.geometry = Text621

Transform616.children.append(Shape618)
Shape623 = x3d.Shape()
Shape623.DEF = "Kick_Back"
Appearance624 = x3d.Appearance()
Material625 = x3d.Material()
Material625.USE = "Clear"

Appearance624.material = Material625

Shape623.appearance = Appearance624
IndexedFaceSet626 = x3d.IndexedFaceSet()
IndexedFaceSet626.USE = "Backing"

Shape623.geometry = IndexedFaceSet626

Transform616.children.append(Shape623)

Transform537.children.append(Transform616)
Transform627 = x3d.Transform()
Transform627.DEF = "Stop_Text"
Transform627.translation = [0,0.4,0]
TouchSensor628 = x3d.TouchSensor()
TouchSensor628.DEF = "Stop_Touch"

Transform627.children.append(TouchSensor628)
Shape629 = x3d.Shape()
Shape629.DEF = "StopText"
Appearance630 = x3d.Appearance()
Material631 = x3d.Material()
Material631.USE = "text_color"

Appearance630.material = Material631

Shape629.appearance = Appearance630
Text632 = x3d.Text()
Text632.string = ["Default"]
FontStyle633 = x3d.FontStyle()
FontStyle633.family = ["SANS"]

Text632.fontStyle = FontStyle633

Shape629.geometry = Text632

Transform627.children.append(Shape629)
Shape634 = x3d.Shape()
Shape634.DEF = "Stop_Back"
Appearance635 = x3d.Appearance()
Material636 = x3d.Material()
Material636.USE = "Clear"

Appearance635.material = Material636

Shape634.appearance = Appearance635
IndexedFaceSet637 = x3d.IndexedFaceSet()
IndexedFaceSet637.USE = "Backing"

Shape634.geometry = IndexedFaceSet637

Transform627.children.append(Shape634)

Transform537.children.append(Transform627)
Transform638 = x3d.Transform()
Transform638.DEF = "SceneLabel"
Transform638.translation = [1.3,3,0]
Shape639 = x3d.Shape()
Shape639.DEF = "SceneLabelText"
Appearance640 = x3d.Appearance()
Material641 = x3d.Material()
Material641.USE = "text_color"

Appearance640.material = Material641

Shape639.appearance = Appearance640
Text642 = x3d.Text()
Text642.string = ["BoxMan4","Animation"]
FontStyle643 = x3d.FontStyle()
FontStyle643.family = ["SANS"]
FontStyle643.justify = ["MIDDLE","MIDDLE"]

Text642.fontStyle = FontStyle643

Shape639.geometry = Text642

Transform638.children.append(Shape639)

Transform537.children.append(Transform638)

Transform536.children.append(Transform537)

Group529.children.append(Transform536)

Scene34.children.append(Group529)
ROUTE644 = x3d.ROUTE()
ROUTE644.fromField = "fraction_changed"
ROUTE644.fromNode = "StopTimer"
ROUTE644.toField = "set_fraction"
ROUTE644.toNode = "Stop_humanoid_root_TranslationInterpolator"

Scene34.children.append(ROUTE644)
ROUTE645 = x3d.ROUTE()
ROUTE645.fromField = "fraction_changed"
ROUTE645.fromNode = "StopTimer"
ROUTE645.toField = "set_fraction"
ROUTE645.toNode = "Stop_humanoid_root_RotationInterpolator"

Scene34.children.append(ROUTE645)
ROUTE646 = x3d.ROUTE()
ROUTE646.fromField = "fraction_changed"
ROUTE646.fromNode = "StopTimer"
ROUTE646.toField = "set_fraction"
ROUTE646.toNode = "Stop_sacroiliac_RotationInterpolator"

Scene34.children.append(ROUTE646)
ROUTE647 = x3d.ROUTE()
ROUTE647.fromField = "fraction_changed"
ROUTE647.fromNode = "StopTimer"
ROUTE647.toField = "set_fraction"
ROUTE647.toNode = "Stop_l_hip_RotationInterpolator"

Scene34.children.append(ROUTE647)
ROUTE648 = x3d.ROUTE()
ROUTE648.fromField = "fraction_changed"
ROUTE648.fromNode = "StopTimer"
ROUTE648.toField = "set_fraction"
ROUTE648.toNode = "Stop_l_knee_RotationInterpolator"

Scene34.children.append(ROUTE648)
ROUTE649 = x3d.ROUTE()
ROUTE649.fromField = "fraction_changed"
ROUTE649.fromNode = "StopTimer"
ROUTE649.toField = "set_fraction"
ROUTE649.toNode = "Stop_l_ankle_RotationInterpolator"

Scene34.children.append(ROUTE649)
ROUTE650 = x3d.ROUTE()
ROUTE650.fromField = "fraction_changed"
ROUTE650.fromNode = "StopTimer"
ROUTE650.toField = "set_fraction"
ROUTE650.toNode = "Stop_l_subtalar_RotationInterpolator"

Scene34.children.append(ROUTE650)
ROUTE651 = x3d.ROUTE()
ROUTE651.fromField = "fraction_changed"
ROUTE651.fromNode = "StopTimer"
ROUTE651.toField = "set_fraction"
ROUTE651.toNode = "Stop_l_midtarsal_RotationInterpolator"

Scene34.children.append(ROUTE651)
ROUTE652 = x3d.ROUTE()
ROUTE652.fromField = "fraction_changed"
ROUTE652.fromNode = "StopTimer"
ROUTE652.toField = "set_fraction"
ROUTE652.toNode = "Stop_l_metatarsal_RotationInterpolator"

Scene34.children.append(ROUTE652)
ROUTE653 = x3d.ROUTE()
ROUTE653.fromField = "fraction_changed"
ROUTE653.fromNode = "StopTimer"
ROUTE653.toField = "set_fraction"
ROUTE653.toNode = "Stop_r_hip_RotationInterpolator"

Scene34.children.append(ROUTE653)
ROUTE654 = x3d.ROUTE()
ROUTE654.fromField = "fraction_changed"
ROUTE654.fromNode = "StopTimer"
ROUTE654.toField = "set_fraction"
ROUTE654.toNode = "Stop_r_knee_RotationInterpolator"

Scene34.children.append(ROUTE654)
ROUTE655 = x3d.ROUTE()
ROUTE655.fromField = "fraction_changed"
ROUTE655.fromNode = "StopTimer"
ROUTE655.toField = "set_fraction"
ROUTE655.toNode = "Stop_r_ankle_RotationInterpolator"

Scene34.children.append(ROUTE655)
ROUTE656 = x3d.ROUTE()
ROUTE656.fromField = "fraction_changed"
ROUTE656.fromNode = "StopTimer"
ROUTE656.toField = "set_fraction"
ROUTE656.toNode = "Stop_r_subtalar_RotationInterpolator"

Scene34.children.append(ROUTE656)
ROUTE657 = x3d.ROUTE()
ROUTE657.fromField = "fraction_changed"
ROUTE657.fromNode = "StopTimer"
ROUTE657.toField = "set_fraction"
ROUTE657.toNode = "Stop_r_midtarsal_RotationInterpolator"

Scene34.children.append(ROUTE657)
ROUTE658 = x3d.ROUTE()
ROUTE658.fromField = "fraction_changed"
ROUTE658.fromNode = "StopTimer"
ROUTE658.toField = "set_fraction"
ROUTE658.toNode = "Stop_r_metatarsal_RotationInterpolator"

Scene34.children.append(ROUTE658)
ROUTE659 = x3d.ROUTE()
ROUTE659.fromField = "fraction_changed"
ROUTE659.fromNode = "StopTimer"
ROUTE659.toField = "set_fraction"
ROUTE659.toNode = "Stop_vl5_RotationInterpolator"

Scene34.children.append(ROUTE659)
ROUTE660 = x3d.ROUTE()
ROUTE660.fromField = "fraction_changed"
ROUTE660.fromNode = "StopTimer"
ROUTE660.toField = "set_fraction"
ROUTE660.toNode = "Stop_vl4_RotationInterpolator"

Scene34.children.append(ROUTE660)
ROUTE661 = x3d.ROUTE()
ROUTE661.fromField = "fraction_changed"
ROUTE661.fromNode = "StopTimer"
ROUTE661.toField = "set_fraction"
ROUTE661.toNode = "Stop_vl3_RotationInterpolator"

Scene34.children.append(ROUTE661)
ROUTE662 = x3d.ROUTE()
ROUTE662.fromField = "fraction_changed"
ROUTE662.fromNode = "StopTimer"
ROUTE662.toField = "set_fraction"
ROUTE662.toNode = "Stop_vl2_RotationInterpolator"

Scene34.children.append(ROUTE662)
ROUTE663 = x3d.ROUTE()
ROUTE663.fromField = "fraction_changed"
ROUTE663.fromNode = "StopTimer"
ROUTE663.toField = "set_fraction"
ROUTE663.toNode = "Stop_vl1_RotationInterpolator"

Scene34.children.append(ROUTE663)
ROUTE664 = x3d.ROUTE()
ROUTE664.fromField = "fraction_changed"
ROUTE664.fromNode = "StopTimer"
ROUTE664.toField = "set_fraction"
ROUTE664.toNode = "Stop_vt12_RotationInterpolator"

Scene34.children.append(ROUTE664)
ROUTE665 = x3d.ROUTE()
ROUTE665.fromField = "fraction_changed"
ROUTE665.fromNode = "StopTimer"
ROUTE665.toField = "set_fraction"
ROUTE665.toNode = "Stop_vt11_RotationInterpolator"

Scene34.children.append(ROUTE665)
ROUTE666 = x3d.ROUTE()
ROUTE666.fromField = "fraction_changed"
ROUTE666.fromNode = "StopTimer"
ROUTE666.toField = "set_fraction"
ROUTE666.toNode = "Stop_vt10_RotationInterpolator"

Scene34.children.append(ROUTE666)
ROUTE667 = x3d.ROUTE()
ROUTE667.fromField = "fraction_changed"
ROUTE667.fromNode = "StopTimer"
ROUTE667.toField = "set_fraction"
ROUTE667.toNode = "Stop_vt9_RotationInterpolator"

Scene34.children.append(ROUTE667)
ROUTE668 = x3d.ROUTE()
ROUTE668.fromField = "fraction_changed"
ROUTE668.fromNode = "StopTimer"
ROUTE668.toField = "set_fraction"
ROUTE668.toNode = "Stop_vt8_RotationInterpolator"

Scene34.children.append(ROUTE668)
ROUTE669 = x3d.ROUTE()
ROUTE669.fromField = "fraction_changed"
ROUTE669.fromNode = "StopTimer"
ROUTE669.toField = "set_fraction"
ROUTE669.toNode = "Stop_vt7_RotationInterpolator"

Scene34.children.append(ROUTE669)
ROUTE670 = x3d.ROUTE()
ROUTE670.fromField = "fraction_changed"
ROUTE670.fromNode = "StopTimer"
ROUTE670.toField = "set_fraction"
ROUTE670.toNode = "Stop_vt6_RotationInterpolator"

Scene34.children.append(ROUTE670)
ROUTE671 = x3d.ROUTE()
ROUTE671.fromField = "fraction_changed"
ROUTE671.fromNode = "StopTimer"
ROUTE671.toField = "set_fraction"
ROUTE671.toNode = "Stop_vt5_RotationInterpolator"

Scene34.children.append(ROUTE671)
ROUTE672 = x3d.ROUTE()
ROUTE672.fromField = "fraction_changed"
ROUTE672.fromNode = "StopTimer"
ROUTE672.toField = "set_fraction"
ROUTE672.toNode = "Stop_vt4_RotationInterpolator"

Scene34.children.append(ROUTE672)
ROUTE673 = x3d.ROUTE()
ROUTE673.fromField = "fraction_changed"
ROUTE673.fromNode = "StopTimer"
ROUTE673.toField = "set_fraction"
ROUTE673.toNode = "Stop_vt3_RotationInterpolator"

Scene34.children.append(ROUTE673)
ROUTE674 = x3d.ROUTE()
ROUTE674.fromField = "fraction_changed"
ROUTE674.fromNode = "StopTimer"
ROUTE674.toField = "set_fraction"
ROUTE674.toNode = "Stop_vt2_RotationInterpolator"

Scene34.children.append(ROUTE674)
ROUTE675 = x3d.ROUTE()
ROUTE675.fromField = "fraction_changed"
ROUTE675.fromNode = "StopTimer"
ROUTE675.toField = "set_fraction"
ROUTE675.toNode = "Stop_vt1_RotationInterpolator"

Scene34.children.append(ROUTE675)
ROUTE676 = x3d.ROUTE()
ROUTE676.fromField = "fraction_changed"
ROUTE676.fromNode = "StopTimer"
ROUTE676.toField = "set_fraction"
ROUTE676.toNode = "Stop_vc7_RotationInterpolator"

Scene34.children.append(ROUTE676)
ROUTE677 = x3d.ROUTE()
ROUTE677.fromField = "fraction_changed"
ROUTE677.fromNode = "StopTimer"
ROUTE677.toField = "set_fraction"
ROUTE677.toNode = "Stop_vc6_RotationInterpolator"

Scene34.children.append(ROUTE677)
ROUTE678 = x3d.ROUTE()
ROUTE678.fromField = "fraction_changed"
ROUTE678.fromNode = "StopTimer"
ROUTE678.toField = "set_fraction"
ROUTE678.toNode = "Stop_vc5_RotationInterpolator"

Scene34.children.append(ROUTE678)
ROUTE679 = x3d.ROUTE()
ROUTE679.fromField = "fraction_changed"
ROUTE679.fromNode = "StopTimer"
ROUTE679.toField = "set_fraction"
ROUTE679.toNode = "Stop_vc4_RotationInterpolator"

Scene34.children.append(ROUTE679)
ROUTE680 = x3d.ROUTE()
ROUTE680.fromField = "fraction_changed"
ROUTE680.fromNode = "StopTimer"
ROUTE680.toField = "set_fraction"
ROUTE680.toNode = "Stop_vc3_RotationInterpolator"

Scene34.children.append(ROUTE680)
ROUTE681 = x3d.ROUTE()
ROUTE681.fromField = "fraction_changed"
ROUTE681.fromNode = "StopTimer"
ROUTE681.toField = "set_fraction"
ROUTE681.toNode = "Stop_vc2_RotationInterpolator"

Scene34.children.append(ROUTE681)
ROUTE682 = x3d.ROUTE()
ROUTE682.fromField = "fraction_changed"
ROUTE682.fromNode = "StopTimer"
ROUTE682.toField = "set_fraction"
ROUTE682.toNode = "Stop_vc1_RotationInterpolator"

Scene34.children.append(ROUTE682)
ROUTE683 = x3d.ROUTE()
ROUTE683.fromField = "fraction_changed"
ROUTE683.fromNode = "StopTimer"
ROUTE683.toField = "set_fraction"
ROUTE683.toNode = "Stop_skullbase_RotationInterpolator"

Scene34.children.append(ROUTE683)
ROUTE684 = x3d.ROUTE()
ROUTE684.fromField = "fraction_changed"
ROUTE684.fromNode = "StopTimer"
ROUTE684.toField = "set_fraction"
ROUTE684.toNode = "Stop_l_eyeball_joint_RotationInterpolator"

Scene34.children.append(ROUTE684)
ROUTE685 = x3d.ROUTE()
ROUTE685.fromField = "fraction_changed"
ROUTE685.fromNode = "StopTimer"
ROUTE685.toField = "set_fraction"
ROUTE685.toNode = "Stop_r_eyeball_joint_RotationInterpolator"

Scene34.children.append(ROUTE685)
ROUTE686 = x3d.ROUTE()
ROUTE686.fromField = "fraction_changed"
ROUTE686.fromNode = "StopTimer"
ROUTE686.toField = "set_fraction"
ROUTE686.toNode = "Stop_l_sternoclavicular_RotationInterpolator"

Scene34.children.append(ROUTE686)
ROUTE687 = x3d.ROUTE()
ROUTE687.fromField = "fraction_changed"
ROUTE687.fromNode = "StopTimer"
ROUTE687.toField = "set_fraction"
ROUTE687.toNode = "Stop_l_acromioclavicular_RotationInterpolator"

Scene34.children.append(ROUTE687)
ROUTE688 = x3d.ROUTE()
ROUTE688.fromField = "fraction_changed"
ROUTE688.fromNode = "StopTimer"
ROUTE688.toField = "set_fraction"
ROUTE688.toNode = "Stop_l_shoulder_RotationInterpolator"

Scene34.children.append(ROUTE688)
ROUTE689 = x3d.ROUTE()
ROUTE689.fromField = "fraction_changed"
ROUTE689.fromNode = "StopTimer"
ROUTE689.toField = "set_fraction"
ROUTE689.toNode = "Stop_l_elbow_RotationInterpolator"

Scene34.children.append(ROUTE689)
ROUTE690 = x3d.ROUTE()
ROUTE690.fromField = "fraction_changed"
ROUTE690.fromNode = "StopTimer"
ROUTE690.toField = "set_fraction"
ROUTE690.toNode = "Stop_l_wrist_RotationInterpolator"

Scene34.children.append(ROUTE690)
ROUTE691 = x3d.ROUTE()
ROUTE691.fromField = "fraction_changed"
ROUTE691.fromNode = "StopTimer"
ROUTE691.toField = "set_fraction"
ROUTE691.toNode = "Stop_l_thumb1_RotationInterpolator"

Scene34.children.append(ROUTE691)
ROUTE692 = x3d.ROUTE()
ROUTE692.fromField = "fraction_changed"
ROUTE692.fromNode = "StopTimer"
ROUTE692.toField = "set_fraction"
ROUTE692.toNode = "Stop_l_thumb2_RotationInterpolator"

Scene34.children.append(ROUTE692)
ROUTE693 = x3d.ROUTE()
ROUTE693.fromField = "fraction_changed"
ROUTE693.fromNode = "StopTimer"
ROUTE693.toField = "set_fraction"
ROUTE693.toNode = "Stop_l_thumb3_RotationInterpolator"

Scene34.children.append(ROUTE693)
ROUTE694 = x3d.ROUTE()
ROUTE694.fromField = "fraction_changed"
ROUTE694.fromNode = "StopTimer"
ROUTE694.toField = "set_fraction"
ROUTE694.toNode = "Stop_l_index0_RotationInterpolator"

Scene34.children.append(ROUTE694)
ROUTE695 = x3d.ROUTE()
ROUTE695.fromField = "fraction_changed"
ROUTE695.fromNode = "StopTimer"
ROUTE695.toField = "set_fraction"
ROUTE695.toNode = "Stop_l_index1_RotationInterpolator"

Scene34.children.append(ROUTE695)
ROUTE696 = x3d.ROUTE()
ROUTE696.fromField = "fraction_changed"
ROUTE696.fromNode = "StopTimer"
ROUTE696.toField = "set_fraction"
ROUTE696.toNode = "Stop_l_index2_RotationInterpolator"

Scene34.children.append(ROUTE696)
ROUTE697 = x3d.ROUTE()
ROUTE697.fromField = "fraction_changed"
ROUTE697.fromNode = "StopTimer"
ROUTE697.toField = "set_fraction"
ROUTE697.toNode = "Stop_l_index3_RotationInterpolator"

Scene34.children.append(ROUTE697)
ROUTE698 = x3d.ROUTE()
ROUTE698.fromField = "fraction_changed"
ROUTE698.fromNode = "StopTimer"
ROUTE698.toField = "set_fraction"
ROUTE698.toNode = "Stop_l_middle0_RotationInterpolator"

Scene34.children.append(ROUTE698)
ROUTE699 = x3d.ROUTE()
ROUTE699.fromField = "fraction_changed"
ROUTE699.fromNode = "StopTimer"
ROUTE699.toField = "set_fraction"
ROUTE699.toNode = "Stop_l_middle1_RotationInterpolator"

Scene34.children.append(ROUTE699)
ROUTE700 = x3d.ROUTE()
ROUTE700.fromField = "fraction_changed"
ROUTE700.fromNode = "StopTimer"
ROUTE700.toField = "set_fraction"
ROUTE700.toNode = "Stop_l_middle2_RotationInterpolator"

Scene34.children.append(ROUTE700)
ROUTE701 = x3d.ROUTE()
ROUTE701.fromField = "fraction_changed"
ROUTE701.fromNode = "StopTimer"
ROUTE701.toField = "set_fraction"
ROUTE701.toNode = "Stop_l_middle3_RotationInterpolator"

Scene34.children.append(ROUTE701)
ROUTE702 = x3d.ROUTE()
ROUTE702.fromField = "fraction_changed"
ROUTE702.fromNode = "StopTimer"
ROUTE702.toField = "set_fraction"
ROUTE702.toNode = "Stop_l_ring0_RotationInterpolator"

Scene34.children.append(ROUTE702)
ROUTE703 = x3d.ROUTE()
ROUTE703.fromField = "fraction_changed"
ROUTE703.fromNode = "StopTimer"
ROUTE703.toField = "set_fraction"
ROUTE703.toNode = "Stop_l_ring1_RotationInterpolator"

Scene34.children.append(ROUTE703)
ROUTE704 = x3d.ROUTE()
ROUTE704.fromField = "fraction_changed"
ROUTE704.fromNode = "StopTimer"
ROUTE704.toField = "set_fraction"
ROUTE704.toNode = "Stop_l_ring2_RotationInterpolator"

Scene34.children.append(ROUTE704)
ROUTE705 = x3d.ROUTE()
ROUTE705.fromField = "fraction_changed"
ROUTE705.fromNode = "StopTimer"
ROUTE705.toField = "set_fraction"
ROUTE705.toNode = "Stop_l_ring3_RotationInterpolator"

Scene34.children.append(ROUTE705)
ROUTE706 = x3d.ROUTE()
ROUTE706.fromField = "fraction_changed"
ROUTE706.fromNode = "StopTimer"
ROUTE706.toField = "set_fraction"
ROUTE706.toNode = "Stop_l_pinky0_RotationInterpolator"

Scene34.children.append(ROUTE706)
ROUTE707 = x3d.ROUTE()
ROUTE707.fromField = "fraction_changed"
ROUTE707.fromNode = "StopTimer"
ROUTE707.toField = "set_fraction"
ROUTE707.toNode = "Stop_l_pinky1_RotationInterpolator"

Scene34.children.append(ROUTE707)
ROUTE708 = x3d.ROUTE()
ROUTE708.fromField = "fraction_changed"
ROUTE708.fromNode = "StopTimer"
ROUTE708.toField = "set_fraction"
ROUTE708.toNode = "Stop_l_pinky2_RotationInterpolator"

Scene34.children.append(ROUTE708)
ROUTE709 = x3d.ROUTE()
ROUTE709.fromField = "fraction_changed"
ROUTE709.fromNode = "StopTimer"
ROUTE709.toField = "set_fraction"
ROUTE709.toNode = "Stop_l_pinky3_RotationInterpolator"

Scene34.children.append(ROUTE709)
ROUTE710 = x3d.ROUTE()
ROUTE710.fromField = "fraction_changed"
ROUTE710.fromNode = "StopTimer"
ROUTE710.toField = "set_fraction"
ROUTE710.toNode = "Stop_r_sternoclavicular_RotationInterpolator"

Scene34.children.append(ROUTE710)
ROUTE711 = x3d.ROUTE()
ROUTE711.fromField = "fraction_changed"
ROUTE711.fromNode = "StopTimer"
ROUTE711.toField = "set_fraction"
ROUTE711.toNode = "Stop_r_acromioclavicular_RotationInterpolator"

Scene34.children.append(ROUTE711)
ROUTE712 = x3d.ROUTE()
ROUTE712.fromField = "fraction_changed"
ROUTE712.fromNode = "StopTimer"
ROUTE712.toField = "set_fraction"
ROUTE712.toNode = "Stop_r_shoulder_RotationInterpolator"

Scene34.children.append(ROUTE712)
ROUTE713 = x3d.ROUTE()
ROUTE713.fromField = "fraction_changed"
ROUTE713.fromNode = "StopTimer"
ROUTE713.toField = "set_fraction"
ROUTE713.toNode = "Stop_r_elbow_RotationInterpolator"

Scene34.children.append(ROUTE713)
ROUTE714 = x3d.ROUTE()
ROUTE714.fromField = "fraction_changed"
ROUTE714.fromNode = "StopTimer"
ROUTE714.toField = "set_fraction"
ROUTE714.toNode = "Stop_r_wrist_RotationInterpolator"

Scene34.children.append(ROUTE714)
ROUTE715 = x3d.ROUTE()
ROUTE715.fromField = "fraction_changed"
ROUTE715.fromNode = "StopTimer"
ROUTE715.toField = "set_fraction"
ROUTE715.toNode = "Stop_r_thumb1_RotationInterpolator"

Scene34.children.append(ROUTE715)
ROUTE716 = x3d.ROUTE()
ROUTE716.fromField = "fraction_changed"
ROUTE716.fromNode = "StopTimer"
ROUTE716.toField = "set_fraction"
ROUTE716.toNode = "Stop_r_thumb2_RotationInterpolator"

Scene34.children.append(ROUTE716)
ROUTE717 = x3d.ROUTE()
ROUTE717.fromField = "fraction_changed"
ROUTE717.fromNode = "StopTimer"
ROUTE717.toField = "set_fraction"
ROUTE717.toNode = "Stop_r_thumb3_RotationInterpolator"

Scene34.children.append(ROUTE717)
ROUTE718 = x3d.ROUTE()
ROUTE718.fromField = "fraction_changed"
ROUTE718.fromNode = "StopTimer"
ROUTE718.toField = "set_fraction"
ROUTE718.toNode = "Stop_r_index0_RotationInterpolator"

Scene34.children.append(ROUTE718)
ROUTE719 = x3d.ROUTE()
ROUTE719.fromField = "fraction_changed"
ROUTE719.fromNode = "StopTimer"
ROUTE719.toField = "set_fraction"
ROUTE719.toNode = "Stop_r_index1_RotationInterpolator"

Scene34.children.append(ROUTE719)
ROUTE720 = x3d.ROUTE()
ROUTE720.fromField = "fraction_changed"
ROUTE720.fromNode = "StopTimer"
ROUTE720.toField = "set_fraction"
ROUTE720.toNode = "Stop_r_index2_RotationInterpolator"

Scene34.children.append(ROUTE720)
ROUTE721 = x3d.ROUTE()
ROUTE721.fromField = "fraction_changed"
ROUTE721.fromNode = "StopTimer"
ROUTE721.toField = "set_fraction"
ROUTE721.toNode = "Stop_r_index3_RotationInterpolator"

Scene34.children.append(ROUTE721)
ROUTE722 = x3d.ROUTE()
ROUTE722.fromField = "fraction_changed"
ROUTE722.fromNode = "StopTimer"
ROUTE722.toField = "set_fraction"
ROUTE722.toNode = "Stop_r_middle0_RotationInterpolator"

Scene34.children.append(ROUTE722)
ROUTE723 = x3d.ROUTE()
ROUTE723.fromField = "fraction_changed"
ROUTE723.fromNode = "StopTimer"
ROUTE723.toField = "set_fraction"
ROUTE723.toNode = "Stop_r_middle1_RotationInterpolator"

Scene34.children.append(ROUTE723)
ROUTE724 = x3d.ROUTE()
ROUTE724.fromField = "fraction_changed"
ROUTE724.fromNode = "StopTimer"
ROUTE724.toField = "set_fraction"
ROUTE724.toNode = "Stop_r_middle2_RotationInterpolator"

Scene34.children.append(ROUTE724)
ROUTE725 = x3d.ROUTE()
ROUTE725.fromField = "fraction_changed"
ROUTE725.fromNode = "StopTimer"
ROUTE725.toField = "set_fraction"
ROUTE725.toNode = "Stop_r_middle3_RotationInterpolator"

Scene34.children.append(ROUTE725)
ROUTE726 = x3d.ROUTE()
ROUTE726.fromField = "fraction_changed"
ROUTE726.fromNode = "StopTimer"
ROUTE726.toField = "set_fraction"
ROUTE726.toNode = "Stop_r_ring0_RotationInterpolator"

Scene34.children.append(ROUTE726)
ROUTE727 = x3d.ROUTE()
ROUTE727.fromField = "fraction_changed"
ROUTE727.fromNode = "StopTimer"
ROUTE727.toField = "set_fraction"
ROUTE727.toNode = "Stop_r_ring1_RotationInterpolator"

Scene34.children.append(ROUTE727)
ROUTE728 = x3d.ROUTE()
ROUTE728.fromField = "fraction_changed"
ROUTE728.fromNode = "StopTimer"
ROUTE728.toField = "set_fraction"
ROUTE728.toNode = "Stop_r_ring2_RotationInterpolator"

Scene34.children.append(ROUTE728)
ROUTE729 = x3d.ROUTE()
ROUTE729.fromField = "fraction_changed"
ROUTE729.fromNode = "StopTimer"
ROUTE729.toField = "set_fraction"
ROUTE729.toNode = "Stop_r_ring3_RotationInterpolator"

Scene34.children.append(ROUTE729)
ROUTE730 = x3d.ROUTE()
ROUTE730.fromField = "fraction_changed"
ROUTE730.fromNode = "StopTimer"
ROUTE730.toField = "set_fraction"
ROUTE730.toNode = "Stop_r_pinky0_RotationInterpolator"

Scene34.children.append(ROUTE730)
ROUTE731 = x3d.ROUTE()
ROUTE731.fromField = "fraction_changed"
ROUTE731.fromNode = "StopTimer"
ROUTE731.toField = "set_fraction"
ROUTE731.toNode = "Stop_r_pinky1_RotationInterpolator"

Scene34.children.append(ROUTE731)
ROUTE732 = x3d.ROUTE()
ROUTE732.fromField = "fraction_changed"
ROUTE732.fromNode = "StopTimer"
ROUTE732.toField = "set_fraction"
ROUTE732.toNode = "Stop_r_pinky2_RotationInterpolator"

Scene34.children.append(ROUTE732)
ROUTE733 = x3d.ROUTE()
ROUTE733.fromField = "fraction_changed"
ROUTE733.fromNode = "StopTimer"
ROUTE733.toField = "set_fraction"
ROUTE733.toNode = "Stop_r_pinky3_RotationInterpolator"

Scene34.children.append(ROUTE733)
ROUTE734 = x3d.ROUTE()
ROUTE734.fromField = "value_changed"
ROUTE734.fromNode = "Stop_humanoid_root_TranslationInterpolator"
ROUTE734.toField = "set_translation"
ROUTE734.toNode = "boxman_humanoid_root"

Scene34.children.append(ROUTE734)
ROUTE735 = x3d.ROUTE()
ROUTE735.fromField = "value_changed"
ROUTE735.fromNode = "Stop_humanoid_root_RotationInterpolator"
ROUTE735.toField = "set_rotation"
ROUTE735.toNode = "boxman_humanoid_root"

Scene34.children.append(ROUTE735)
ROUTE736 = x3d.ROUTE()
ROUTE736.fromField = "value_changed"
ROUTE736.fromNode = "Stop_l_hip_RotationInterpolator"
ROUTE736.toField = "set_rotation"
ROUTE736.toNode = "boxman_l_hip"

Scene34.children.append(ROUTE736)
ROUTE737 = x3d.ROUTE()
ROUTE737.fromField = "value_changed"
ROUTE737.fromNode = "Stop_l_knee_RotationInterpolator"
ROUTE737.toField = "set_rotation"
ROUTE737.toNode = "boxman_l_knee"

Scene34.children.append(ROUTE737)
ROUTE738 = x3d.ROUTE()
ROUTE738.fromField = "value_changed"
ROUTE738.fromNode = "Stop_l_ankle_RotationInterpolator"
ROUTE738.toField = "set_rotation"
ROUTE738.toNode = "boxman_l_ankle"

Scene34.children.append(ROUTE738)
ROUTE739 = x3d.ROUTE()
ROUTE739.fromField = "value_changed"
ROUTE739.fromNode = "Stop_l_midtarsal_RotationInterpolator"
ROUTE739.toField = "set_rotation"
ROUTE739.toNode = "boxman_l_midtarsal"

Scene34.children.append(ROUTE739)
ROUTE740 = x3d.ROUTE()
ROUTE740.fromField = "value_changed"
ROUTE740.fromNode = "Stop_r_hip_RotationInterpolator"
ROUTE740.toField = "set_rotation"
ROUTE740.toNode = "boxman_r_hip"

Scene34.children.append(ROUTE740)
ROUTE741 = x3d.ROUTE()
ROUTE741.fromField = "value_changed"
ROUTE741.fromNode = "Stop_r_knee_RotationInterpolator"
ROUTE741.toField = "set_rotation"
ROUTE741.toNode = "boxman_r_knee"

Scene34.children.append(ROUTE741)
ROUTE742 = x3d.ROUTE()
ROUTE742.fromField = "value_changed"
ROUTE742.fromNode = "Stop_r_ankle_RotationInterpolator"
ROUTE742.toField = "set_rotation"
ROUTE742.toNode = "boxman_r_ankle"

Scene34.children.append(ROUTE742)
ROUTE743 = x3d.ROUTE()
ROUTE743.fromField = "value_changed"
ROUTE743.fromNode = "Stop_r_midtarsal_RotationInterpolator"
ROUTE743.toField = "set_rotation"
ROUTE743.toNode = "boxman_r_midtarsal"

Scene34.children.append(ROUTE743)
ROUTE744 = x3d.ROUTE()
ROUTE744.fromField = "value_changed"
ROUTE744.fromNode = "Stop_vl5_RotationInterpolator"
ROUTE744.toField = "set_rotation"
ROUTE744.toNode = "boxman_vl5"

Scene34.children.append(ROUTE744)
ROUTE745 = x3d.ROUTE()
ROUTE745.fromField = "value_changed"
ROUTE745.fromNode = "Stop_skullbase_RotationInterpolator"
ROUTE745.toField = "set_rotation"
ROUTE745.toNode = "boxman_skullbase"

Scene34.children.append(ROUTE745)
ROUTE746 = x3d.ROUTE()
ROUTE746.fromField = "value_changed"
ROUTE746.fromNode = "Stop_l_shoulder_RotationInterpolator"
ROUTE746.toField = "set_rotation"
ROUTE746.toNode = "boxman_l_shoulder"

Scene34.children.append(ROUTE746)
ROUTE747 = x3d.ROUTE()
ROUTE747.fromField = "value_changed"
ROUTE747.fromNode = "Stop_l_elbow_RotationInterpolator"
ROUTE747.toField = "set_rotation"
ROUTE747.toNode = "boxman_l_elbow"

Scene34.children.append(ROUTE747)
ROUTE748 = x3d.ROUTE()
ROUTE748.fromField = "value_changed"
ROUTE748.fromNode = "Stop_l_wrist_RotationInterpolator"
ROUTE748.toField = "set_rotation"
ROUTE748.toNode = "boxman_l_wrist"

Scene34.children.append(ROUTE748)
ROUTE749 = x3d.ROUTE()
ROUTE749.fromField = "value_changed"
ROUTE749.fromNode = "Stop_r_shoulder_RotationInterpolator"
ROUTE749.toField = "set_rotation"
ROUTE749.toNode = "boxman_r_shoulder"

Scene34.children.append(ROUTE749)
ROUTE750 = x3d.ROUTE()
ROUTE750.fromField = "value_changed"
ROUTE750.fromNode = "Stop_r_elbow_RotationInterpolator"
ROUTE750.toField = "set_rotation"
ROUTE750.toNode = "boxman_r_elbow"

Scene34.children.append(ROUTE750)
ROUTE751 = x3d.ROUTE()
ROUTE751.fromField = "value_changed"
ROUTE751.fromNode = "Stop_r_wrist_RotationInterpolator"
ROUTE751.toField = "set_rotation"
ROUTE751.toNode = "boxman_r_wrist"

Scene34.children.append(ROUTE751)
ROUTE752 = x3d.ROUTE()
ROUTE752.fromField = "fraction_changed"
ROUTE752.fromNode = "StandTimer"
ROUTE752.toField = "set_fraction"
ROUTE752.toNode = "Stand_r_ankle_RotationInterpolator"

Scene34.children.append(ROUTE752)
ROUTE753 = x3d.ROUTE()
ROUTE753.fromField = "fraction_changed"
ROUTE753.fromNode = "StandTimer"
ROUTE753.toField = "set_fraction"
ROUTE753.toNode = "Stand_r_knee_RotationInterpolator"

Scene34.children.append(ROUTE753)
ROUTE754 = x3d.ROUTE()
ROUTE754.fromField = "fraction_changed"
ROUTE754.fromNode = "StandTimer"
ROUTE754.toField = "set_fraction"
ROUTE754.toNode = "Stand_r_hip_RotationInterpolator"

Scene34.children.append(ROUTE754)
ROUTE755 = x3d.ROUTE()
ROUTE755.fromField = "fraction_changed"
ROUTE755.fromNode = "StandTimer"
ROUTE755.toField = "set_fraction"
ROUTE755.toNode = "Stand_l_ankle_RotationInterpolator"

Scene34.children.append(ROUTE755)
ROUTE756 = x3d.ROUTE()
ROUTE756.fromField = "fraction_changed"
ROUTE756.fromNode = "StandTimer"
ROUTE756.toField = "set_fraction"
ROUTE756.toNode = "Stand_l_knee_RotationInterpolator"

Scene34.children.append(ROUTE756)
ROUTE757 = x3d.ROUTE()
ROUTE757.fromField = "fraction_changed"
ROUTE757.fromNode = "StandTimer"
ROUTE757.toField = "set_fraction"
ROUTE757.toNode = "Stand_l_hip_RotationInterpolator"

Scene34.children.append(ROUTE757)
ROUTE758 = x3d.ROUTE()
ROUTE758.fromField = "fraction_changed"
ROUTE758.fromNode = "StandTimer"
ROUTE758.toField = "set_fraction"
ROUTE758.toNode = "Stand_lower_body_RotationInterpolator"

Scene34.children.append(ROUTE758)
ROUTE759 = x3d.ROUTE()
ROUTE759.fromField = "fraction_changed"
ROUTE759.fromNode = "StandTimer"
ROUTE759.toField = "set_fraction"
ROUTE759.toNode = "Stand_r_wrist_RotationInterpolator"

Scene34.children.append(ROUTE759)
ROUTE760 = x3d.ROUTE()
ROUTE760.fromField = "fraction_changed"
ROUTE760.fromNode = "StandTimer"
ROUTE760.toField = "set_fraction"
ROUTE760.toNode = "Stand_r_elbow_RotationInterpolator"

Scene34.children.append(ROUTE760)
ROUTE761 = x3d.ROUTE()
ROUTE761.fromField = "fraction_changed"
ROUTE761.fromNode = "StandTimer"
ROUTE761.toField = "set_fraction"
ROUTE761.toNode = "Stand_r_shoulder_RotationInterpolator"

Scene34.children.append(ROUTE761)
ROUTE762 = x3d.ROUTE()
ROUTE762.fromField = "fraction_changed"
ROUTE762.fromNode = "StandTimer"
ROUTE762.toField = "set_fraction"
ROUTE762.toNode = "Stand_l_wrist_RotationInterpolator"

Scene34.children.append(ROUTE762)
ROUTE763 = x3d.ROUTE()
ROUTE763.fromField = "fraction_changed"
ROUTE763.fromNode = "StandTimer"
ROUTE763.toField = "set_fraction"
ROUTE763.toNode = "Stand_l_elbow_RotationInterpolator"

Scene34.children.append(ROUTE763)
ROUTE764 = x3d.ROUTE()
ROUTE764.fromField = "fraction_changed"
ROUTE764.fromNode = "StandTimer"
ROUTE764.toField = "set_fraction"
ROUTE764.toNode = "Stand_l_shoulder_RotationInterpolator"

Scene34.children.append(ROUTE764)
ROUTE765 = x3d.ROUTE()
ROUTE765.fromField = "fraction_changed"
ROUTE765.fromNode = "StandTimer"
ROUTE765.toField = "set_fraction"
ROUTE765.toNode = "Stand_head_RotationInterpolator"

Scene34.children.append(ROUTE765)
ROUTE766 = x3d.ROUTE()
ROUTE766.fromField = "fraction_changed"
ROUTE766.fromNode = "StandTimer"
ROUTE766.toField = "set_fraction"
ROUTE766.toNode = "Stand_neck_RotationInterpolator"

Scene34.children.append(ROUTE766)
ROUTE767 = x3d.ROUTE()
ROUTE767.fromField = "fraction_changed"
ROUTE767.fromNode = "StandTimer"
ROUTE767.toField = "set_fraction"
ROUTE767.toNode = "Stand_l_eyeball_RotationInterpolator"

Scene34.children.append(ROUTE767)
ROUTE768 = x3d.ROUTE()
ROUTE768.fromField = "fraction_changed"
ROUTE768.fromNode = "StandTimer"
ROUTE768.toField = "set_fraction"
ROUTE768.toNode = "Stand_r_eyeball_RotationInterpolator"

Scene34.children.append(ROUTE768)
ROUTE769 = x3d.ROUTE()
ROUTE769.fromField = "fraction_changed"
ROUTE769.fromNode = "StandTimer"
ROUTE769.toField = "set_fraction"
ROUTE769.toNode = "Stand_upper_body_RotationInterpolator"

Scene34.children.append(ROUTE769)
ROUTE770 = x3d.ROUTE()
ROUTE770.fromField = "fraction_changed"
ROUTE770.fromNode = "StandTimer"
ROUTE770.toField = "set_fraction"
ROUTE770.toNode = "Stand_whole_body_RotationInterpolator"

Scene34.children.append(ROUTE770)
ROUTE771 = x3d.ROUTE()
ROUTE771.fromField = "fraction_changed"
ROUTE771.fromNode = "StandTimer"
ROUTE771.toField = "set_fraction"
ROUTE771.toNode = "Stand_whole_body_TranslationInterpolator"

Scene34.children.append(ROUTE771)
ROUTE772 = x3d.ROUTE()
ROUTE772.fromField = "fraction_changed"
ROUTE772.fromNode = "StandTimer"
ROUTE772.toField = "set_fraction"
ROUTE772.toNode = "Stand_l_sternoclavicular_RollInterpolator"

Scene34.children.append(ROUTE772)
ROUTE773 = x3d.ROUTE()
ROUTE773.fromField = "fraction_changed"
ROUTE773.fromNode = "StandTimer"
ROUTE773.toField = "set_fraction"
ROUTE773.toNode = "Stand_l_acromioclavicular_RollInterpolator"

Scene34.children.append(ROUTE773)
ROUTE774 = x3d.ROUTE()
ROUTE774.fromField = "fraction_changed"
ROUTE774.fromNode = "StandTimer"
ROUTE774.toField = "set_fraction"
ROUTE774.toNode = "Stand_r_sternoclavicular_RollInterpolator"

Scene34.children.append(ROUTE774)
ROUTE775 = x3d.ROUTE()
ROUTE775.fromField = "fraction_changed"
ROUTE775.fromNode = "StandTimer"
ROUTE775.toField = "set_fraction"
ROUTE775.toNode = "Stand_r_acromioclavicular_RollInterpolator"

Scene34.children.append(ROUTE775)
ROUTE776 = x3d.ROUTE()
ROUTE776.fromField = "fraction_changed"
ROUTE776.fromNode = "StandTimer"
ROUTE776.toField = "set_fraction"
ROUTE776.toNode = "Stand_r_metatarsal_PitchInterpolator"

Scene34.children.append(ROUTE776)
ROUTE777 = x3d.ROUTE()
ROUTE777.fromField = "fraction_changed"
ROUTE777.fromNode = "StandTimer"
ROUTE777.toField = "set_fraction"
ROUTE777.toNode = "Stand_sacroiliac_YawInterpolator"

Scene34.children.append(ROUTE777)
ROUTE778 = x3d.ROUTE()
ROUTE778.fromField = "fraction_changed"
ROUTE778.fromNode = "StandTimer"
ROUTE778.toField = "set_fraction"
ROUTE778.toNode = "Stand_vl5_YawInterpolator"

Scene34.children.append(ROUTE778)
ROUTE779 = x3d.ROUTE()
ROUTE779.fromField = "fraction_changed"
ROUTE779.fromNode = "StandTimer"
ROUTE779.toField = "set_fraction"
ROUTE779.toNode = "Stand_vc6_YawInterpolator"

Scene34.children.append(ROUTE779)
ROUTE780 = x3d.ROUTE()
ROUTE780.fromField = "fraction_changed"
ROUTE780.fromNode = "StandTimer"
ROUTE780.toField = "set_fraction"
ROUTE780.toNode = "Stand_l_thumb1_PitchInterpolator"

Scene34.children.append(ROUTE780)
ROUTE781 = x3d.ROUTE()
ROUTE781.fromField = "fraction_changed"
ROUTE781.fromNode = "StandTimer"
ROUTE781.toField = "set_fraction"
ROUTE781.toNode = "Stand_r_thumb1_PitchInterpolator"

Scene34.children.append(ROUTE781)
ROUTE782 = x3d.ROUTE()
ROUTE782.fromField = "fraction_changed"
ROUTE782.fromNode = "StandTimer"
ROUTE782.toField = "set_fraction"
ROUTE782.toNode = "Stand_r_index1_RollInterpolator"

Scene34.children.append(ROUTE782)
ROUTE783 = x3d.ROUTE()
ROUTE783.fromField = "fraction_changed"
ROUTE783.fromNode = "StandTimer"
ROUTE783.toField = "set_fraction"
ROUTE783.toNode = "Stand_r_index2_RollInterpolator"

Scene34.children.append(ROUTE783)
ROUTE784 = x3d.ROUTE()
ROUTE784.fromField = "fraction_changed"
ROUTE784.fromNode = "StandTimer"
ROUTE784.toField = "set_fraction"
ROUTE784.toNode = "Stand_r_index3_RollInterpolator"

Scene34.children.append(ROUTE784)
ROUTE785 = x3d.ROUTE()
ROUTE785.fromField = "value_changed"
ROUTE785.fromNode = "Stand_r_ankle_RotationInterpolator"
ROUTE785.toField = "set_rotation"
ROUTE785.toNode = "boxman_r_ankle"

Scene34.children.append(ROUTE785)
ROUTE786 = x3d.ROUTE()
ROUTE786.fromField = "value_changed"
ROUTE786.fromNode = "Stand_r_knee_RotationInterpolator"
ROUTE786.toField = "set_rotation"
ROUTE786.toNode = "boxman_r_knee"

Scene34.children.append(ROUTE786)
ROUTE787 = x3d.ROUTE()
ROUTE787.fromField = "value_changed"
ROUTE787.fromNode = "Stand_r_hip_RotationInterpolator"
ROUTE787.toField = "set_rotation"
ROUTE787.toNode = "boxman_r_hip"

Scene34.children.append(ROUTE787)
ROUTE788 = x3d.ROUTE()
ROUTE788.fromField = "value_changed"
ROUTE788.fromNode = "Stand_l_ankle_RotationInterpolator"
ROUTE788.toField = "set_rotation"
ROUTE788.toNode = "boxman_l_ankle"

Scene34.children.append(ROUTE788)
ROUTE789 = x3d.ROUTE()
ROUTE789.fromField = "value_changed"
ROUTE789.fromNode = "Stand_l_knee_RotationInterpolator"
ROUTE789.toField = "set_rotation"
ROUTE789.toNode = "boxman_l_knee"

Scene34.children.append(ROUTE789)
ROUTE790 = x3d.ROUTE()
ROUTE790.fromField = "value_changed"
ROUTE790.fromNode = "Stand_l_hip_RotationInterpolator"
ROUTE790.toField = "set_rotation"
ROUTE790.toNode = "boxman_l_hip"

Scene34.children.append(ROUTE790)
ROUTE791 = x3d.ROUTE()
ROUTE791.fromField = "value_changed"
ROUTE791.fromNode = "Stand_r_wrist_RotationInterpolator"
ROUTE791.toField = "set_rotation"
ROUTE791.toNode = "boxman_r_wrist"

Scene34.children.append(ROUTE791)
ROUTE792 = x3d.ROUTE()
ROUTE792.fromField = "value_changed"
ROUTE792.fromNode = "Stand_r_elbow_RotationInterpolator"
ROUTE792.toField = "set_rotation"
ROUTE792.toNode = "boxman_r_elbow"

Scene34.children.append(ROUTE792)
ROUTE793 = x3d.ROUTE()
ROUTE793.fromField = "value_changed"
ROUTE793.fromNode = "Stand_r_shoulder_RotationInterpolator"
ROUTE793.toField = "set_rotation"
ROUTE793.toNode = "boxman_r_shoulder"

Scene34.children.append(ROUTE793)
ROUTE794 = x3d.ROUTE()
ROUTE794.fromField = "value_changed"
ROUTE794.fromNode = "Stand_l_wrist_RotationInterpolator"
ROUTE794.toField = "set_rotation"
ROUTE794.toNode = "boxman_l_wrist"

Scene34.children.append(ROUTE794)
ROUTE795 = x3d.ROUTE()
ROUTE795.fromField = "value_changed"
ROUTE795.fromNode = "Stand_l_elbow_RotationInterpolator"
ROUTE795.toField = "set_rotation"
ROUTE795.toNode = "boxman_l_elbow"

Scene34.children.append(ROUTE795)
ROUTE796 = x3d.ROUTE()
ROUTE796.fromField = "value_changed"
ROUTE796.fromNode = "Stand_l_shoulder_RotationInterpolator"
ROUTE796.toField = "set_rotation"
ROUTE796.toNode = "boxman_l_shoulder"

Scene34.children.append(ROUTE796)
ROUTE797 = x3d.ROUTE()
ROUTE797.fromField = "value_changed"
ROUTE797.fromNode = "Stand_head_RotationInterpolator"
ROUTE797.toField = "set_rotation"
ROUTE797.toNode = "boxman_skullbase"

Scene34.children.append(ROUTE797)
ROUTE798 = x3d.ROUTE()
ROUTE798.fromField = "value_changed"
ROUTE798.fromNode = "Stand_whole_body_RotationInterpolator"
ROUTE798.toField = "set_rotation"
ROUTE798.toNode = "boxman_humanoid_root"

Scene34.children.append(ROUTE798)
ROUTE799 = x3d.ROUTE()
ROUTE799.fromField = "value_changed"
ROUTE799.fromNode = "Stand_whole_body_TranslationInterpolator"
ROUTE799.toField = "set_translation"
ROUTE799.toNode = "boxman_humanoid_root"

Scene34.children.append(ROUTE799)
ROUTE800 = x3d.ROUTE()
ROUTE800.fromField = "value_changed"
ROUTE800.fromNode = "Stand_vl5_YawInterpolator"
ROUTE800.toField = "set_rotation"
ROUTE800.toNode = "boxman_vl5"

Scene34.children.append(ROUTE800)
ROUTE801 = x3d.ROUTE()
ROUTE801.fromField = "fraction_changed"
ROUTE801.fromNode = "PitchTimer"
ROUTE801.toField = "set_fraction"
ROUTE801.toNode = "Pitches_r_ankle_RotationInterpolator"

Scene34.children.append(ROUTE801)
ROUTE802 = x3d.ROUTE()
ROUTE802.fromField = "fraction_changed"
ROUTE802.fromNode = "PitchTimer"
ROUTE802.toField = "set_fraction"
ROUTE802.toNode = "Pitches_r_knee_RotationInterpolator"

Scene34.children.append(ROUTE802)
ROUTE803 = x3d.ROUTE()
ROUTE803.fromField = "fraction_changed"
ROUTE803.fromNode = "PitchTimer"
ROUTE803.toField = "set_fraction"
ROUTE803.toNode = "Pitches_r_hip_RotationInterpolator"

Scene34.children.append(ROUTE803)
ROUTE804 = x3d.ROUTE()
ROUTE804.fromField = "fraction_changed"
ROUTE804.fromNode = "PitchTimer"
ROUTE804.toField = "set_fraction"
ROUTE804.toNode = "Pitches_l_ankle_RotationInterpolator"

Scene34.children.append(ROUTE804)
ROUTE805 = x3d.ROUTE()
ROUTE805.fromField = "fraction_changed"
ROUTE805.fromNode = "PitchTimer"
ROUTE805.toField = "set_fraction"
ROUTE805.toNode = "Pitches_l_knee_RotationInterpolator"

Scene34.children.append(ROUTE805)
ROUTE806 = x3d.ROUTE()
ROUTE806.fromField = "fraction_changed"
ROUTE806.fromNode = "PitchTimer"
ROUTE806.toField = "set_fraction"
ROUTE806.toNode = "Pitches_l_hip_RotationInterpolator"

Scene34.children.append(ROUTE806)
ROUTE807 = x3d.ROUTE()
ROUTE807.fromField = "fraction_changed"
ROUTE807.fromNode = "PitchTimer"
ROUTE807.toField = "set_fraction"
ROUTE807.toNode = "Pitches_lower_body_RotationInterpolator"

Scene34.children.append(ROUTE807)
ROUTE808 = x3d.ROUTE()
ROUTE808.fromField = "fraction_changed"
ROUTE808.fromNode = "PitchTimer"
ROUTE808.toField = "set_fraction"
ROUTE808.toNode = "Pitches_r_wrist_RotationInterpolator"

Scene34.children.append(ROUTE808)
ROUTE809 = x3d.ROUTE()
ROUTE809.fromField = "fraction_changed"
ROUTE809.fromNode = "PitchTimer"
ROUTE809.toField = "set_fraction"
ROUTE809.toNode = "Pitches_r_elbow_RotationInterpolator"

Scene34.children.append(ROUTE809)
ROUTE810 = x3d.ROUTE()
ROUTE810.fromField = "fraction_changed"
ROUTE810.fromNode = "PitchTimer"
ROUTE810.toField = "set_fraction"
ROUTE810.toNode = "Pitches_r_shoulder_RotationInterpolator"

Scene34.children.append(ROUTE810)
ROUTE811 = x3d.ROUTE()
ROUTE811.fromField = "fraction_changed"
ROUTE811.fromNode = "PitchTimer"
ROUTE811.toField = "set_fraction"
ROUTE811.toNode = "Pitches_l_wrist_RotationInterpolator"

Scene34.children.append(ROUTE811)
ROUTE812 = x3d.ROUTE()
ROUTE812.fromField = "fraction_changed"
ROUTE812.fromNode = "PitchTimer"
ROUTE812.toField = "set_fraction"
ROUTE812.toNode = "Pitches_l_elbow_RotationInterpolator"

Scene34.children.append(ROUTE812)
ROUTE813 = x3d.ROUTE()
ROUTE813.fromField = "fraction_changed"
ROUTE813.fromNode = "PitchTimer"
ROUTE813.toField = "set_fraction"
ROUTE813.toNode = "Pitches_l_shoulder_RotationInterpolator"

Scene34.children.append(ROUTE813)
ROUTE814 = x3d.ROUTE()
ROUTE814.fromField = "fraction_changed"
ROUTE814.fromNode = "PitchTimer"
ROUTE814.toField = "set_fraction"
ROUTE814.toNode = "Pitches_head_RotationInterpolator"

Scene34.children.append(ROUTE814)
ROUTE815 = x3d.ROUTE()
ROUTE815.fromField = "fraction_changed"
ROUTE815.fromNode = "PitchTimer"
ROUTE815.toField = "set_fraction"
ROUTE815.toNode = "Pitches_neck_RotationInterpolator"

Scene34.children.append(ROUTE815)
ROUTE816 = x3d.ROUTE()
ROUTE816.fromField = "fraction_changed"
ROUTE816.fromNode = "PitchTimer"
ROUTE816.toField = "set_fraction"
ROUTE816.toNode = "Pitches_upper_body_RotationInterpolator"

Scene34.children.append(ROUTE816)
ROUTE817 = x3d.ROUTE()
ROUTE817.fromField = "fraction_changed"
ROUTE817.fromNode = "PitchTimer"
ROUTE817.toField = "set_fraction"
ROUTE817.toNode = "Pitches_whole_body_RotationInterpolator"

Scene34.children.append(ROUTE817)
ROUTE818 = x3d.ROUTE()
ROUTE818.fromField = "fraction_changed"
ROUTE818.fromNode = "PitchTimer"
ROUTE818.toField = "set_fraction"
ROUTE818.toNode = "Pitches_whole_body_TranslationInterpolator"

Scene34.children.append(ROUTE818)
ROUTE819 = x3d.ROUTE()
ROUTE819.fromField = "fraction_changed"
ROUTE819.fromNode = "PitchTimer"
ROUTE819.toField = "set_fraction"
ROUTE819.toNode = "Pitch_l_sternoclavicular_RollInterpolator"

Scene34.children.append(ROUTE819)
ROUTE820 = x3d.ROUTE()
ROUTE820.fromField = "fraction_changed"
ROUTE820.fromNode = "PitchTimer"
ROUTE820.toField = "set_fraction"
ROUTE820.toNode = "Pitch_l_acromioclavicular_RollInterpolator"

Scene34.children.append(ROUTE820)
ROUTE821 = x3d.ROUTE()
ROUTE821.fromField = "fraction_changed"
ROUTE821.fromNode = "PitchTimer"
ROUTE821.toField = "set_fraction"
ROUTE821.toNode = "Pitch_r_sternoclavicular_RollInterpolator"

Scene34.children.append(ROUTE821)
ROUTE822 = x3d.ROUTE()
ROUTE822.fromField = "fraction_changed"
ROUTE822.fromNode = "PitchTimer"
ROUTE822.toField = "set_fraction"
ROUTE822.toNode = "Pitch_r_acromioclavicular_RollInterpolator"

Scene34.children.append(ROUTE822)
ROUTE823 = x3d.ROUTE()
ROUTE823.fromField = "fraction_changed"
ROUTE823.fromNode = "PitchTimer"
ROUTE823.toField = "set_fraction"
ROUTE823.toNode = "Pitch_r_metatarsal_PitchInterpolator"

Scene34.children.append(ROUTE823)
ROUTE824 = x3d.ROUTE()
ROUTE824.fromField = "fraction_changed"
ROUTE824.fromNode = "PitchTimer"
ROUTE824.toField = "set_fraction"
ROUTE824.toNode = "Pitch_sacroiliac_YawInterpolator"

Scene34.children.append(ROUTE824)
ROUTE825 = x3d.ROUTE()
ROUTE825.fromField = "fraction_changed"
ROUTE825.fromNode = "PitchTimer"
ROUTE825.toField = "set_fraction"
ROUTE825.toNode = "Pitch_vl5_YawInterpolator"

Scene34.children.append(ROUTE825)
ROUTE826 = x3d.ROUTE()
ROUTE826.fromField = "fraction_changed"
ROUTE826.fromNode = "PitchTimer"
ROUTE826.toField = "set_fraction"
ROUTE826.toNode = "Pitch_vc6_YawInterpolator"

Scene34.children.append(ROUTE826)
ROUTE827 = x3d.ROUTE()
ROUTE827.fromField = "fraction_changed"
ROUTE827.fromNode = "PitchTimer"
ROUTE827.toField = "set_fraction"
ROUTE827.toNode = "Pitch_l_thumb1_PitchInterpolator"

Scene34.children.append(ROUTE827)
ROUTE828 = x3d.ROUTE()
ROUTE828.fromField = "fraction_changed"
ROUTE828.fromNode = "PitchTimer"
ROUTE828.toField = "set_fraction"
ROUTE828.toNode = "Pitch_r_thumb1_PitchInterpolator"

Scene34.children.append(ROUTE828)
ROUTE829 = x3d.ROUTE()
ROUTE829.fromField = "value_changed"
ROUTE829.fromNode = "Pitches_r_ankle_RotationInterpolator"
ROUTE829.toField = "set_rotation"
ROUTE829.toNode = "boxman_r_ankle"

Scene34.children.append(ROUTE829)
ROUTE830 = x3d.ROUTE()
ROUTE830.fromField = "value_changed"
ROUTE830.fromNode = "Pitches_r_knee_RotationInterpolator"
ROUTE830.toField = "set_rotation"
ROUTE830.toNode = "boxman_r_knee"

Scene34.children.append(ROUTE830)
ROUTE831 = x3d.ROUTE()
ROUTE831.fromField = "value_changed"
ROUTE831.fromNode = "Pitches_r_hip_RotationInterpolator"
ROUTE831.toField = "set_rotation"
ROUTE831.toNode = "boxman_r_hip"

Scene34.children.append(ROUTE831)
ROUTE832 = x3d.ROUTE()
ROUTE832.fromField = "value_changed"
ROUTE832.fromNode = "Pitches_l_ankle_RotationInterpolator"
ROUTE832.toField = "set_rotation"
ROUTE832.toNode = "boxman_l_ankle"

Scene34.children.append(ROUTE832)
ROUTE833 = x3d.ROUTE()
ROUTE833.fromField = "value_changed"
ROUTE833.fromNode = "Pitches_l_knee_RotationInterpolator"
ROUTE833.toField = "set_rotation"
ROUTE833.toNode = "boxman_l_knee"

Scene34.children.append(ROUTE833)
ROUTE834 = x3d.ROUTE()
ROUTE834.fromField = "value_changed"
ROUTE834.fromNode = "Pitches_l_hip_RotationInterpolator"
ROUTE834.toField = "set_rotation"
ROUTE834.toNode = "boxman_l_hip"

Scene34.children.append(ROUTE834)
ROUTE835 = x3d.ROUTE()
ROUTE835.fromField = "value_changed"
ROUTE835.fromNode = "Pitches_r_wrist_RotationInterpolator"
ROUTE835.toField = "set_rotation"
ROUTE835.toNode = "boxman_r_wrist"

Scene34.children.append(ROUTE835)
ROUTE836 = x3d.ROUTE()
ROUTE836.fromField = "value_changed"
ROUTE836.fromNode = "Pitches_r_elbow_RotationInterpolator"
ROUTE836.toField = "set_rotation"
ROUTE836.toNode = "boxman_r_elbow"

Scene34.children.append(ROUTE836)
ROUTE837 = x3d.ROUTE()
ROUTE837.fromField = "value_changed"
ROUTE837.fromNode = "Pitches_r_shoulder_RotationInterpolator"
ROUTE837.toField = "set_rotation"
ROUTE837.toNode = "boxman_r_shoulder"

Scene34.children.append(ROUTE837)
ROUTE838 = x3d.ROUTE()
ROUTE838.fromField = "value_changed"
ROUTE838.fromNode = "Pitches_l_wrist_RotationInterpolator"
ROUTE838.toField = "set_rotation"
ROUTE838.toNode = "boxman_l_wrist"

Scene34.children.append(ROUTE838)
ROUTE839 = x3d.ROUTE()
ROUTE839.fromField = "value_changed"
ROUTE839.fromNode = "Pitches_l_elbow_RotationInterpolator"
ROUTE839.toField = "set_rotation"
ROUTE839.toNode = "boxman_l_elbow"

Scene34.children.append(ROUTE839)
ROUTE840 = x3d.ROUTE()
ROUTE840.fromField = "value_changed"
ROUTE840.fromNode = "Pitches_l_shoulder_RotationInterpolator"
ROUTE840.toField = "set_rotation"
ROUTE840.toNode = "boxman_l_shoulder"

Scene34.children.append(ROUTE840)
ROUTE841 = x3d.ROUTE()
ROUTE841.fromField = "value_changed"
ROUTE841.fromNode = "Pitches_head_RotationInterpolator"
ROUTE841.toField = "set_rotation"
ROUTE841.toNode = "boxman_skullbase"

Scene34.children.append(ROUTE841)
ROUTE842 = x3d.ROUTE()
ROUTE842.fromField = "value_changed"
ROUTE842.fromNode = "Pitches_whole_body_RotationInterpolator"
ROUTE842.toField = "set_rotation"
ROUTE842.toNode = "boxman_humanoid_root"

Scene34.children.append(ROUTE842)
ROUTE843 = x3d.ROUTE()
ROUTE843.fromField = "value_changed"
ROUTE843.fromNode = "Pitches_whole_body_TranslationInterpolator"
ROUTE843.toField = "set_translation"
ROUTE843.toNode = "boxman_humanoid_root"

Scene34.children.append(ROUTE843)
ROUTE844 = x3d.ROUTE()
ROUTE844.fromField = "value_changed"
ROUTE844.fromNode = "Pitch_vl5_YawInterpolator"
ROUTE844.toField = "set_rotation"
ROUTE844.toNode = "boxman_vl5"

Scene34.children.append(ROUTE844)
ROUTE845 = x3d.ROUTE()
ROUTE845.fromField = "fraction_changed"
ROUTE845.fromNode = "YawTimer"
ROUTE845.toField = "set_fraction"
ROUTE845.toNode = "Yaws_r_ankle_RotationInterpolator"

Scene34.children.append(ROUTE845)
ROUTE846 = x3d.ROUTE()
ROUTE846.fromField = "fraction_changed"
ROUTE846.fromNode = "YawTimer"
ROUTE846.toField = "set_fraction"
ROUTE846.toNode = "Yaws_r_knee_RotationInterpolator"

Scene34.children.append(ROUTE846)
ROUTE847 = x3d.ROUTE()
ROUTE847.fromField = "fraction_changed"
ROUTE847.fromNode = "YawTimer"
ROUTE847.toField = "set_fraction"
ROUTE847.toNode = "Yaws_r_hip_RotationInterpolator"

Scene34.children.append(ROUTE847)
ROUTE848 = x3d.ROUTE()
ROUTE848.fromField = "fraction_changed"
ROUTE848.fromNode = "YawTimer"
ROUTE848.toField = "set_fraction"
ROUTE848.toNode = "Yaws_l_ankle_RotationInterpolator"

Scene34.children.append(ROUTE848)
ROUTE849 = x3d.ROUTE()
ROUTE849.fromField = "fraction_changed"
ROUTE849.fromNode = "YawTimer"
ROUTE849.toField = "set_fraction"
ROUTE849.toNode = "Yaws_l_knee_RotationInterpolator"

Scene34.children.append(ROUTE849)
ROUTE850 = x3d.ROUTE()
ROUTE850.fromField = "fraction_changed"
ROUTE850.fromNode = "YawTimer"
ROUTE850.toField = "set_fraction"
ROUTE850.toNode = "Yaws_l_hip_RotationInterpolator"

Scene34.children.append(ROUTE850)
ROUTE851 = x3d.ROUTE()
ROUTE851.fromField = "fraction_changed"
ROUTE851.fromNode = "YawTimer"
ROUTE851.toField = "set_fraction"
ROUTE851.toNode = "Yaws_lower_body_RotationInterpolator"

Scene34.children.append(ROUTE851)
ROUTE852 = x3d.ROUTE()
ROUTE852.fromField = "fraction_changed"
ROUTE852.fromNode = "YawTimer"
ROUTE852.toField = "set_fraction"
ROUTE852.toNode = "Yaws_r_wrist_RotationInterpolator"

Scene34.children.append(ROUTE852)
ROUTE853 = x3d.ROUTE()
ROUTE853.fromField = "fraction_changed"
ROUTE853.fromNode = "YawTimer"
ROUTE853.toField = "set_fraction"
ROUTE853.toNode = "Yaws_r_elbow_RotationInterpolator"

Scene34.children.append(ROUTE853)
ROUTE854 = x3d.ROUTE()
ROUTE854.fromField = "fraction_changed"
ROUTE854.fromNode = "YawTimer"
ROUTE854.toField = "set_fraction"
ROUTE854.toNode = "Yaws_r_shoulder_RotationInterpolator"

Scene34.children.append(ROUTE854)
ROUTE855 = x3d.ROUTE()
ROUTE855.fromField = "fraction_changed"
ROUTE855.fromNode = "YawTimer"
ROUTE855.toField = "set_fraction"
ROUTE855.toNode = "Yaws_l_wrist_RotationInterpolator"

Scene34.children.append(ROUTE855)
ROUTE856 = x3d.ROUTE()
ROUTE856.fromField = "fraction_changed"
ROUTE856.fromNode = "YawTimer"
ROUTE856.toField = "set_fraction"
ROUTE856.toNode = "Yaws_l_elbow_RotationInterpolator"

Scene34.children.append(ROUTE856)
ROUTE857 = x3d.ROUTE()
ROUTE857.fromField = "fraction_changed"
ROUTE857.fromNode = "YawTimer"
ROUTE857.toField = "set_fraction"
ROUTE857.toNode = "Yaws_l_shoulder_RotationInterpolator"

Scene34.children.append(ROUTE857)
ROUTE858 = x3d.ROUTE()
ROUTE858.fromField = "fraction_changed"
ROUTE858.fromNode = "YawTimer"
ROUTE858.toField = "set_fraction"
ROUTE858.toNode = "Yaws_head_RotationInterpolator"

Scene34.children.append(ROUTE858)
ROUTE859 = x3d.ROUTE()
ROUTE859.fromField = "fraction_changed"
ROUTE859.fromNode = "YawTimer"
ROUTE859.toField = "set_fraction"
ROUTE859.toNode = "Yaws_neck_RotationInterpolator"

Scene34.children.append(ROUTE859)
ROUTE860 = x3d.ROUTE()
ROUTE860.fromField = "fraction_changed"
ROUTE860.fromNode = "YawTimer"
ROUTE860.toField = "set_fraction"
ROUTE860.toNode = "Yaws_upper_body_RotationInterpolator"

Scene34.children.append(ROUTE860)
ROUTE861 = x3d.ROUTE()
ROUTE861.fromField = "fraction_changed"
ROUTE861.fromNode = "YawTimer"
ROUTE861.toField = "set_fraction"
ROUTE861.toNode = "Yaws_whole_body_RotationInterpolator"

Scene34.children.append(ROUTE861)
ROUTE862 = x3d.ROUTE()
ROUTE862.fromField = "fraction_changed"
ROUTE862.fromNode = "YawTimer"
ROUTE862.toField = "set_fraction"
ROUTE862.toNode = "Yaws_whole_body_TranslationInterpolator"

Scene34.children.append(ROUTE862)
ROUTE863 = x3d.ROUTE()
ROUTE863.fromField = "fraction_changed"
ROUTE863.fromNode = "YawTimer"
ROUTE863.toField = "set_fraction"
ROUTE863.toNode = "Yaw_l_sternoclavicular_RollInterpolator"

Scene34.children.append(ROUTE863)
ROUTE864 = x3d.ROUTE()
ROUTE864.fromField = "fraction_changed"
ROUTE864.fromNode = "YawTimer"
ROUTE864.toField = "set_fraction"
ROUTE864.toNode = "Yaw_l_acromioclavicular_RollInterpolator"

Scene34.children.append(ROUTE864)
ROUTE865 = x3d.ROUTE()
ROUTE865.fromField = "fraction_changed"
ROUTE865.fromNode = "YawTimer"
ROUTE865.toField = "set_fraction"
ROUTE865.toNode = "Yaw_r_sternoclavicular_RollInterpolator"

Scene34.children.append(ROUTE865)
ROUTE866 = x3d.ROUTE()
ROUTE866.fromField = "fraction_changed"
ROUTE866.fromNode = "YawTimer"
ROUTE866.toField = "set_fraction"
ROUTE866.toNode = "Yaw_r_acromioclavicular_RollInterpolator"

Scene34.children.append(ROUTE866)
ROUTE867 = x3d.ROUTE()
ROUTE867.fromField = "fraction_changed"
ROUTE867.fromNode = "YawTimer"
ROUTE867.toField = "set_fraction"
ROUTE867.toNode = "Yaw_r_metatarsal_PitchInterpolator"

Scene34.children.append(ROUTE867)
ROUTE868 = x3d.ROUTE()
ROUTE868.fromField = "fraction_changed"
ROUTE868.fromNode = "YawTimer"
ROUTE868.toField = "set_fraction"
ROUTE868.toNode = "Yaw_sacroiliac_YawInterpolator"

Scene34.children.append(ROUTE868)
ROUTE869 = x3d.ROUTE()
ROUTE869.fromField = "fraction_changed"
ROUTE869.fromNode = "YawTimer"
ROUTE869.toField = "set_fraction"
ROUTE869.toNode = "Yaw_vl5_YawInterpolator"

Scene34.children.append(ROUTE869)
ROUTE870 = x3d.ROUTE()
ROUTE870.fromField = "fraction_changed"
ROUTE870.fromNode = "YawTimer"
ROUTE870.toField = "set_fraction"
ROUTE870.toNode = "Yaw_vc6_YawInterpolator"

Scene34.children.append(ROUTE870)
ROUTE871 = x3d.ROUTE()
ROUTE871.fromField = "fraction_changed"
ROUTE871.fromNode = "YawTimer"
ROUTE871.toField = "set_fraction"
ROUTE871.toNode = "Yaw_l_thumb1_PitchInterpolator"

Scene34.children.append(ROUTE871)
ROUTE872 = x3d.ROUTE()
ROUTE872.fromField = "fraction_changed"
ROUTE872.fromNode = "YawTimer"
ROUTE872.toField = "set_fraction"
ROUTE872.toNode = "Yaw_r_thumb1_PitchInterpolator"

Scene34.children.append(ROUTE872)
ROUTE873 = x3d.ROUTE()
ROUTE873.fromField = "value_changed"
ROUTE873.fromNode = "Yaws_r_ankle_RotationInterpolator"
ROUTE873.toField = "set_rotation"
ROUTE873.toNode = "boxman_r_ankle"

Scene34.children.append(ROUTE873)
ROUTE874 = x3d.ROUTE()
ROUTE874.fromField = "value_changed"
ROUTE874.fromNode = "Yaws_r_knee_RotationInterpolator"
ROUTE874.toField = "set_rotation"
ROUTE874.toNode = "boxman_r_knee"

Scene34.children.append(ROUTE874)
ROUTE875 = x3d.ROUTE()
ROUTE875.fromField = "value_changed"
ROUTE875.fromNode = "Yaws_r_hip_RotationInterpolator"
ROUTE875.toField = "set_rotation"
ROUTE875.toNode = "boxman_r_hip"

Scene34.children.append(ROUTE875)
ROUTE876 = x3d.ROUTE()
ROUTE876.fromField = "value_changed"
ROUTE876.fromNode = "Yaws_l_ankle_RotationInterpolator"
ROUTE876.toField = "set_rotation"
ROUTE876.toNode = "boxman_l_ankle"

Scene34.children.append(ROUTE876)
ROUTE877 = x3d.ROUTE()
ROUTE877.fromField = "value_changed"
ROUTE877.fromNode = "Yaws_l_knee_RotationInterpolator"
ROUTE877.toField = "set_rotation"
ROUTE877.toNode = "boxman_l_knee"

Scene34.children.append(ROUTE877)
ROUTE878 = x3d.ROUTE()
ROUTE878.fromField = "value_changed"
ROUTE878.fromNode = "Yaws_l_hip_RotationInterpolator"
ROUTE878.toField = "set_rotation"
ROUTE878.toNode = "boxman_l_hip"

Scene34.children.append(ROUTE878)
ROUTE879 = x3d.ROUTE()
ROUTE879.fromField = "value_changed"
ROUTE879.fromNode = "Yaws_r_wrist_RotationInterpolator"
ROUTE879.toField = "set_rotation"
ROUTE879.toNode = "boxman_r_wrist"

Scene34.children.append(ROUTE879)
ROUTE880 = x3d.ROUTE()
ROUTE880.fromField = "value_changed"
ROUTE880.fromNode = "Yaws_r_elbow_RotationInterpolator"
ROUTE880.toField = "set_rotation"
ROUTE880.toNode = "boxman_r_elbow"

Scene34.children.append(ROUTE880)
ROUTE881 = x3d.ROUTE()
ROUTE881.fromField = "value_changed"
ROUTE881.fromNode = "Yaws_r_shoulder_RotationInterpolator"
ROUTE881.toField = "set_rotation"
ROUTE881.toNode = "boxman_r_shoulder"

Scene34.children.append(ROUTE881)
ROUTE882 = x3d.ROUTE()
ROUTE882.fromField = "value_changed"
ROUTE882.fromNode = "Yaws_l_wrist_RotationInterpolator"
ROUTE882.toField = "set_rotation"
ROUTE882.toNode = "boxman_l_wrist"

Scene34.children.append(ROUTE882)
ROUTE883 = x3d.ROUTE()
ROUTE883.fromField = "value_changed"
ROUTE883.fromNode = "Yaws_l_elbow_RotationInterpolator"
ROUTE883.toField = "set_rotation"
ROUTE883.toNode = "boxman_l_elbow"

Scene34.children.append(ROUTE883)
ROUTE884 = x3d.ROUTE()
ROUTE884.fromField = "value_changed"
ROUTE884.fromNode = "Yaws_l_shoulder_RotationInterpolator"
ROUTE884.toField = "set_rotation"
ROUTE884.toNode = "boxman_l_shoulder"

Scene34.children.append(ROUTE884)
ROUTE885 = x3d.ROUTE()
ROUTE885.fromField = "value_changed"
ROUTE885.fromNode = "Yaws_head_RotationInterpolator"
ROUTE885.toField = "set_rotation"
ROUTE885.toNode = "boxman_skullbase"

Scene34.children.append(ROUTE885)
ROUTE886 = x3d.ROUTE()
ROUTE886.fromField = "value_changed"
ROUTE886.fromNode = "Yaws_whole_body_RotationInterpolator"
ROUTE886.toField = "set_rotation"
ROUTE886.toNode = "boxman_humanoid_root"

Scene34.children.append(ROUTE886)
ROUTE887 = x3d.ROUTE()
ROUTE887.fromField = "value_changed"
ROUTE887.fromNode = "Yaws_whole_body_TranslationInterpolator"
ROUTE887.toField = "set_translation"
ROUTE887.toNode = "boxman_humanoid_root"

Scene34.children.append(ROUTE887)
ROUTE888 = x3d.ROUTE()
ROUTE888.fromField = "value_changed"
ROUTE888.fromNode = "Yaw_vl5_YawInterpolator"
ROUTE888.toField = "set_rotation"
ROUTE888.toNode = "boxman_vl5"

Scene34.children.append(ROUTE888)
ROUTE889 = x3d.ROUTE()
ROUTE889.fromField = "fraction_changed"
ROUTE889.fromNode = "RollTimer"
ROUTE889.toField = "set_fraction"
ROUTE889.toNode = "Rolls_r_ankle_RotationInterpolator"

Scene34.children.append(ROUTE889)
ROUTE890 = x3d.ROUTE()
ROUTE890.fromField = "fraction_changed"
ROUTE890.fromNode = "RollTimer"
ROUTE890.toField = "set_fraction"
ROUTE890.toNode = "Rolls_r_knee_RotationInterpolator"

Scene34.children.append(ROUTE890)
ROUTE891 = x3d.ROUTE()
ROUTE891.fromField = "fraction_changed"
ROUTE891.fromNode = "RollTimer"
ROUTE891.toField = "set_fraction"
ROUTE891.toNode = "Rolls_r_hip_RotationInterpolator"

Scene34.children.append(ROUTE891)
ROUTE892 = x3d.ROUTE()
ROUTE892.fromField = "fraction_changed"
ROUTE892.fromNode = "RollTimer"
ROUTE892.toField = "set_fraction"
ROUTE892.toNode = "Rolls_l_ankle_RotationInterpolator"

Scene34.children.append(ROUTE892)
ROUTE893 = x3d.ROUTE()
ROUTE893.fromField = "fraction_changed"
ROUTE893.fromNode = "RollTimer"
ROUTE893.toField = "set_fraction"
ROUTE893.toNode = "Rolls_l_knee_RotationInterpolator"

Scene34.children.append(ROUTE893)
ROUTE894 = x3d.ROUTE()
ROUTE894.fromField = "fraction_changed"
ROUTE894.fromNode = "RollTimer"
ROUTE894.toField = "set_fraction"
ROUTE894.toNode = "Rolls_l_hip_RotationInterpolator"

Scene34.children.append(ROUTE894)
ROUTE895 = x3d.ROUTE()
ROUTE895.fromField = "fraction_changed"
ROUTE895.fromNode = "RollTimer"
ROUTE895.toField = "set_fraction"
ROUTE895.toNode = "Rolls_lower_body_RotationInterpolator"

Scene34.children.append(ROUTE895)
ROUTE896 = x3d.ROUTE()
ROUTE896.fromField = "fraction_changed"
ROUTE896.fromNode = "RollTimer"
ROUTE896.toField = "set_fraction"
ROUTE896.toNode = "Rolls_r_wrist_RotationInterpolator"

Scene34.children.append(ROUTE896)
ROUTE897 = x3d.ROUTE()
ROUTE897.fromField = "fraction_changed"
ROUTE897.fromNode = "RollTimer"
ROUTE897.toField = "set_fraction"
ROUTE897.toNode = "Rolls_r_elbow_RotationInterpolator"

Scene34.children.append(ROUTE897)
ROUTE898 = x3d.ROUTE()
ROUTE898.fromField = "fraction_changed"
ROUTE898.fromNode = "RollTimer"
ROUTE898.toField = "set_fraction"
ROUTE898.toNode = "Rolls_r_shoulder_RotationInterpolator"

Scene34.children.append(ROUTE898)
ROUTE899 = x3d.ROUTE()
ROUTE899.fromField = "fraction_changed"
ROUTE899.fromNode = "RollTimer"
ROUTE899.toField = "set_fraction"
ROUTE899.toNode = "Rolls_l_wrist_RotationInterpolator"

Scene34.children.append(ROUTE899)
ROUTE900 = x3d.ROUTE()
ROUTE900.fromField = "fraction_changed"
ROUTE900.fromNode = "RollTimer"
ROUTE900.toField = "set_fraction"
ROUTE900.toNode = "Rolls_l_elbow_RotationInterpolator"

Scene34.children.append(ROUTE900)
ROUTE901 = x3d.ROUTE()
ROUTE901.fromField = "fraction_changed"
ROUTE901.fromNode = "RollTimer"
ROUTE901.toField = "set_fraction"
ROUTE901.toNode = "Rolls_l_shoulder_RotationInterpolator"

Scene34.children.append(ROUTE901)
ROUTE902 = x3d.ROUTE()
ROUTE902.fromField = "fraction_changed"
ROUTE902.fromNode = "RollTimer"
ROUTE902.toField = "set_fraction"
ROUTE902.toNode = "Rolls_head_RotationInterpolator"

Scene34.children.append(ROUTE902)
ROUTE903 = x3d.ROUTE()
ROUTE903.fromField = "fraction_changed"
ROUTE903.fromNode = "RollTimer"
ROUTE903.toField = "set_fraction"
ROUTE903.toNode = "Rolls_neck_RotationInterpolator"

Scene34.children.append(ROUTE903)
ROUTE904 = x3d.ROUTE()
ROUTE904.fromField = "fraction_changed"
ROUTE904.fromNode = "RollTimer"
ROUTE904.toField = "set_fraction"
ROUTE904.toNode = "Rolls_upper_body_RotationInterpolator"

Scene34.children.append(ROUTE904)
ROUTE905 = x3d.ROUTE()
ROUTE905.fromField = "fraction_changed"
ROUTE905.fromNode = "RollTimer"
ROUTE905.toField = "set_fraction"
ROUTE905.toNode = "Rolls_whole_body_RotationInterpolator"

Scene34.children.append(ROUTE905)
ROUTE906 = x3d.ROUTE()
ROUTE906.fromField = "fraction_changed"
ROUTE906.fromNode = "RollTimer"
ROUTE906.toField = "set_fraction"
ROUTE906.toNode = "Rolls_whole_body_TranslationInterpolator"

Scene34.children.append(ROUTE906)
ROUTE907 = x3d.ROUTE()
ROUTE907.fromField = "fraction_changed"
ROUTE907.fromNode = "RollTimer"
ROUTE907.toField = "set_fraction"
ROUTE907.toNode = "Roll_l_sternoclavicular_RollInterpolator"

Scene34.children.append(ROUTE907)
ROUTE908 = x3d.ROUTE()
ROUTE908.fromField = "fraction_changed"
ROUTE908.fromNode = "RollTimer"
ROUTE908.toField = "set_fraction"
ROUTE908.toNode = "Roll_l_acromioclavicular_RollInterpolator"

Scene34.children.append(ROUTE908)
ROUTE909 = x3d.ROUTE()
ROUTE909.fromField = "fraction_changed"
ROUTE909.fromNode = "RollTimer"
ROUTE909.toField = "set_fraction"
ROUTE909.toNode = "Roll_r_sternoclavicular_RollInterpolator"

Scene34.children.append(ROUTE909)
ROUTE910 = x3d.ROUTE()
ROUTE910.fromField = "fraction_changed"
ROUTE910.fromNode = "RollTimer"
ROUTE910.toField = "set_fraction"
ROUTE910.toNode = "Roll_r_acromioclavicular_RollInterpolator"

Scene34.children.append(ROUTE910)
ROUTE911 = x3d.ROUTE()
ROUTE911.fromField = "fraction_changed"
ROUTE911.fromNode = "RollTimer"
ROUTE911.toField = "set_fraction"
ROUTE911.toNode = "Roll_r_metatarsal_PitchInterpolator"

Scene34.children.append(ROUTE911)
ROUTE912 = x3d.ROUTE()
ROUTE912.fromField = "fraction_changed"
ROUTE912.fromNode = "RollTimer"
ROUTE912.toField = "set_fraction"
ROUTE912.toNode = "Roll_sacroiliac_YawInterpolator"

Scene34.children.append(ROUTE912)
ROUTE913 = x3d.ROUTE()
ROUTE913.fromField = "fraction_changed"
ROUTE913.fromNode = "RollTimer"
ROUTE913.toField = "set_fraction"
ROUTE913.toNode = "Roll_vl5_YawInterpolator"

Scene34.children.append(ROUTE913)
ROUTE914 = x3d.ROUTE()
ROUTE914.fromField = "fraction_changed"
ROUTE914.fromNode = "RollTimer"
ROUTE914.toField = "set_fraction"
ROUTE914.toNode = "Roll_vc6_YawInterpolator"

Scene34.children.append(ROUTE914)
ROUTE915 = x3d.ROUTE()
ROUTE915.fromField = "fraction_changed"
ROUTE915.fromNode = "RollTimer"
ROUTE915.toField = "set_fraction"
ROUTE915.toNode = "Roll_l_thumb1_PitchInterpolator"

Scene34.children.append(ROUTE915)
ROUTE916 = x3d.ROUTE()
ROUTE916.fromField = "fraction_changed"
ROUTE916.fromNode = "RollTimer"
ROUTE916.toField = "set_fraction"
ROUTE916.toNode = "Roll_r_thumb1_PitchInterpolator"

Scene34.children.append(ROUTE916)
ROUTE917 = x3d.ROUTE()
ROUTE917.fromField = "value_changed"
ROUTE917.fromNode = "Rolls_r_ankle_RotationInterpolator"
ROUTE917.toField = "set_rotation"
ROUTE917.toNode = "boxman_r_ankle"

Scene34.children.append(ROUTE917)
ROUTE918 = x3d.ROUTE()
ROUTE918.fromField = "value_changed"
ROUTE918.fromNode = "Rolls_r_knee_RotationInterpolator"
ROUTE918.toField = "set_rotation"
ROUTE918.toNode = "boxman_r_knee"

Scene34.children.append(ROUTE918)
ROUTE919 = x3d.ROUTE()
ROUTE919.fromField = "value_changed"
ROUTE919.fromNode = "Rolls_r_hip_RotationInterpolator"
ROUTE919.toField = "set_rotation"
ROUTE919.toNode = "boxman_r_hip"

Scene34.children.append(ROUTE919)
ROUTE920 = x3d.ROUTE()
ROUTE920.fromField = "value_changed"
ROUTE920.fromNode = "Rolls_l_ankle_RotationInterpolator"
ROUTE920.toField = "set_rotation"
ROUTE920.toNode = "boxman_l_ankle"

Scene34.children.append(ROUTE920)
ROUTE921 = x3d.ROUTE()
ROUTE921.fromField = "value_changed"
ROUTE921.fromNode = "Rolls_l_knee_RotationInterpolator"
ROUTE921.toField = "set_rotation"
ROUTE921.toNode = "boxman_l_knee"

Scene34.children.append(ROUTE921)
ROUTE922 = x3d.ROUTE()
ROUTE922.fromField = "value_changed"
ROUTE922.fromNode = "Rolls_l_hip_RotationInterpolator"
ROUTE922.toField = "set_rotation"
ROUTE922.toNode = "boxman_l_hip"

Scene34.children.append(ROUTE922)
ROUTE923 = x3d.ROUTE()
ROUTE923.fromField = "value_changed"
ROUTE923.fromNode = "Rolls_r_wrist_RotationInterpolator"
ROUTE923.toField = "set_rotation"
ROUTE923.toNode = "boxman_r_wrist"

Scene34.children.append(ROUTE923)
ROUTE924 = x3d.ROUTE()
ROUTE924.fromField = "value_changed"
ROUTE924.fromNode = "Rolls_r_elbow_RotationInterpolator"
ROUTE924.toField = "set_rotation"
ROUTE924.toNode = "boxman_r_elbow"

Scene34.children.append(ROUTE924)
ROUTE925 = x3d.ROUTE()
ROUTE925.fromField = "value_changed"
ROUTE925.fromNode = "Rolls_r_shoulder_RotationInterpolator"
ROUTE925.toField = "set_rotation"
ROUTE925.toNode = "boxman_r_shoulder"

Scene34.children.append(ROUTE925)
ROUTE926 = x3d.ROUTE()
ROUTE926.fromField = "value_changed"
ROUTE926.fromNode = "Rolls_l_wrist_RotationInterpolator"
ROUTE926.toField = "set_rotation"
ROUTE926.toNode = "boxman_l_wrist"

Scene34.children.append(ROUTE926)
ROUTE927 = x3d.ROUTE()
ROUTE927.fromField = "value_changed"
ROUTE927.fromNode = "Rolls_l_elbow_RotationInterpolator"
ROUTE927.toField = "set_rotation"
ROUTE927.toNode = "boxman_l_elbow"

Scene34.children.append(ROUTE927)
ROUTE928 = x3d.ROUTE()
ROUTE928.fromField = "value_changed"
ROUTE928.fromNode = "Rolls_l_shoulder_RotationInterpolator"
ROUTE928.toField = "set_rotation"
ROUTE928.toNode = "boxman_l_shoulder"

Scene34.children.append(ROUTE928)
ROUTE929 = x3d.ROUTE()
ROUTE929.fromField = "value_changed"
ROUTE929.fromNode = "Rolls_head_RotationInterpolator"
ROUTE929.toField = "set_rotation"
ROUTE929.toNode = "boxman_skullbase"

Scene34.children.append(ROUTE929)
ROUTE930 = x3d.ROUTE()
ROUTE930.fromField = "value_changed"
ROUTE930.fromNode = "Rolls_whole_body_RotationInterpolator"
ROUTE930.toField = "set_rotation"
ROUTE930.toNode = "boxman_humanoid_root"

Scene34.children.append(ROUTE930)
ROUTE931 = x3d.ROUTE()
ROUTE931.fromField = "value_changed"
ROUTE931.fromNode = "Rolls_whole_body_TranslationInterpolator"
ROUTE931.toField = "set_translation"
ROUTE931.toNode = "boxman_humanoid_root"

Scene34.children.append(ROUTE931)
ROUTE932 = x3d.ROUTE()
ROUTE932.fromField = "value_changed"
ROUTE932.fromNode = "Roll_vl5_YawInterpolator"
ROUTE932.toField = "set_rotation"
ROUTE932.toNode = "boxman_vl5"

Scene34.children.append(ROUTE932)
ROUTE933 = x3d.ROUTE()
ROUTE933.fromField = "fraction_changed"
ROUTE933.fromNode = "WalkTimer"
ROUTE933.toField = "set_fraction"
ROUTE933.toNode = "Walk_r_ankle_RotationInterpolator"

Scene34.children.append(ROUTE933)
ROUTE934 = x3d.ROUTE()
ROUTE934.fromField = "fraction_changed"
ROUTE934.fromNode = "WalkTimer"
ROUTE934.toField = "set_fraction"
ROUTE934.toNode = "Walk_r_knee_RotationInterpolator"

Scene34.children.append(ROUTE934)
ROUTE935 = x3d.ROUTE()
ROUTE935.fromField = "fraction_changed"
ROUTE935.fromNode = "WalkTimer"
ROUTE935.toField = "set_fraction"
ROUTE935.toNode = "Walk_r_hip_RotationInterpolator"

Scene34.children.append(ROUTE935)
ROUTE936 = x3d.ROUTE()
ROUTE936.fromField = "fraction_changed"
ROUTE936.fromNode = "WalkTimer"
ROUTE936.toField = "set_fraction"
ROUTE936.toNode = "Walk_l_ankle_RotationInterpolator"

Scene34.children.append(ROUTE936)
ROUTE937 = x3d.ROUTE()
ROUTE937.fromField = "fraction_changed"
ROUTE937.fromNode = "WalkTimer"
ROUTE937.toField = "set_fraction"
ROUTE937.toNode = "Walk_l_knee_RotationInterpolator"

Scene34.children.append(ROUTE937)
ROUTE938 = x3d.ROUTE()
ROUTE938.fromField = "fraction_changed"
ROUTE938.fromNode = "WalkTimer"
ROUTE938.toField = "set_fraction"
ROUTE938.toNode = "Walk_l_hip_RotationInterpolator"

Scene34.children.append(ROUTE938)
ROUTE939 = x3d.ROUTE()
ROUTE939.fromField = "fraction_changed"
ROUTE939.fromNode = "WalkTimer"
ROUTE939.toField = "set_fraction"
ROUTE939.toNode = "Walk_lower_body_RotationInterpolator"

Scene34.children.append(ROUTE939)
ROUTE940 = x3d.ROUTE()
ROUTE940.fromField = "fraction_changed"
ROUTE940.fromNode = "WalkTimer"
ROUTE940.toField = "set_fraction"
ROUTE940.toNode = "Walk_r_wrist_RotationInterpolator"

Scene34.children.append(ROUTE940)
ROUTE941 = x3d.ROUTE()
ROUTE941.fromField = "fraction_changed"
ROUTE941.fromNode = "WalkTimer"
ROUTE941.toField = "set_fraction"
ROUTE941.toNode = "Walk_r_elbow_RotationInterpolator"

Scene34.children.append(ROUTE941)
ROUTE942 = x3d.ROUTE()
ROUTE942.fromField = "fraction_changed"
ROUTE942.fromNode = "WalkTimer"
ROUTE942.toField = "set_fraction"
ROUTE942.toNode = "Walk_r_shoulder_RotationInterpolator"

Scene34.children.append(ROUTE942)
ROUTE943 = x3d.ROUTE()
ROUTE943.fromField = "fraction_changed"
ROUTE943.fromNode = "WalkTimer"
ROUTE943.toField = "set_fraction"
ROUTE943.toNode = "Walk_l_wrist_RotationInterpolator"

Scene34.children.append(ROUTE943)
ROUTE944 = x3d.ROUTE()
ROUTE944.fromField = "fraction_changed"
ROUTE944.fromNode = "WalkTimer"
ROUTE944.toField = "set_fraction"
ROUTE944.toNode = "Walk_l_elbow_RotationInterpolator"

Scene34.children.append(ROUTE944)
ROUTE945 = x3d.ROUTE()
ROUTE945.fromField = "fraction_changed"
ROUTE945.fromNode = "WalkTimer"
ROUTE945.toField = "set_fraction"
ROUTE945.toNode = "Walk_l_shoulder_RotationInterpolator"

Scene34.children.append(ROUTE945)
ROUTE946 = x3d.ROUTE()
ROUTE946.fromField = "fraction_changed"
ROUTE946.fromNode = "WalkTimer"
ROUTE946.toField = "set_fraction"
ROUTE946.toNode = "Walk_head_RotationInterpolator"

Scene34.children.append(ROUTE946)
ROUTE947 = x3d.ROUTE()
ROUTE947.fromField = "fraction_changed"
ROUTE947.fromNode = "WalkTimer"
ROUTE947.toField = "set_fraction"
ROUTE947.toNode = "Walk_neck_RotationInterpolator"

Scene34.children.append(ROUTE947)
ROUTE948 = x3d.ROUTE()
ROUTE948.fromField = "fraction_changed"
ROUTE948.fromNode = "WalkTimer"
ROUTE948.toField = "set_fraction"
ROUTE948.toNode = "Walk_upper_body_RotationInterpolator"

Scene34.children.append(ROUTE948)
ROUTE949 = x3d.ROUTE()
ROUTE949.fromField = "fraction_changed"
ROUTE949.fromNode = "WalkTimer"
ROUTE949.toField = "set_fraction"
ROUTE949.toNode = "Walk_whole_body_RotationInterpolator"

Scene34.children.append(ROUTE949)
ROUTE950 = x3d.ROUTE()
ROUTE950.fromField = "fraction_changed"
ROUTE950.fromNode = "WalkTimer"
ROUTE950.toField = "set_fraction"
ROUTE950.toNode = "Walk_whole_body_TranslationInterpolator"

Scene34.children.append(ROUTE950)
ROUTE951 = x3d.ROUTE()
ROUTE951.fromField = "fraction_changed"
ROUTE951.fromNode = "WalkTimer"
ROUTE951.toField = "set_fraction"
ROUTE951.toNode = "Walk_l_sternoclavicular_RollInterpolator"

Scene34.children.append(ROUTE951)
ROUTE952 = x3d.ROUTE()
ROUTE952.fromField = "fraction_changed"
ROUTE952.fromNode = "WalkTimer"
ROUTE952.toField = "set_fraction"
ROUTE952.toNode = "Walk_l_acromioclavicular_RollInterpolator"

Scene34.children.append(ROUTE952)
ROUTE953 = x3d.ROUTE()
ROUTE953.fromField = "fraction_changed"
ROUTE953.fromNode = "WalkTimer"
ROUTE953.toField = "set_fraction"
ROUTE953.toNode = "Walk_r_sternoclavicular_RollInterpolator"

Scene34.children.append(ROUTE953)
ROUTE954 = x3d.ROUTE()
ROUTE954.fromField = "fraction_changed"
ROUTE954.fromNode = "WalkTimer"
ROUTE954.toField = "set_fraction"
ROUTE954.toNode = "Walk_r_acromioclavicular_RollInterpolator"

Scene34.children.append(ROUTE954)
ROUTE955 = x3d.ROUTE()
ROUTE955.fromField = "fraction_changed"
ROUTE955.fromNode = "WalkTimer"
ROUTE955.toField = "set_fraction"
ROUTE955.toNode = "Walk_r_metatarsal_PitchInterpolator"

Scene34.children.append(ROUTE955)
ROUTE956 = x3d.ROUTE()
ROUTE956.fromField = "fraction_changed"
ROUTE956.fromNode = "WalkTimer"
ROUTE956.toField = "set_fraction"
ROUTE956.toNode = "Walk_sacroiliac_YawInterpolator"

Scene34.children.append(ROUTE956)
ROUTE957 = x3d.ROUTE()
ROUTE957.fromField = "fraction_changed"
ROUTE957.fromNode = "WalkTimer"
ROUTE957.toField = "set_fraction"
ROUTE957.toNode = "Walk_vl5_YawInterpolator"

Scene34.children.append(ROUTE957)
ROUTE958 = x3d.ROUTE()
ROUTE958.fromField = "fraction_changed"
ROUTE958.fromNode = "WalkTimer"
ROUTE958.toField = "set_fraction"
ROUTE958.toNode = "Walk_vc6_YawInterpolator"

Scene34.children.append(ROUTE958)
ROUTE959 = x3d.ROUTE()
ROUTE959.fromField = "fraction_changed"
ROUTE959.fromNode = "WalkTimer"
ROUTE959.toField = "set_fraction"
ROUTE959.toNode = "Walk_l_thumb1_PitchInterpolator"

Scene34.children.append(ROUTE959)
ROUTE960 = x3d.ROUTE()
ROUTE960.fromField = "fraction_changed"
ROUTE960.fromNode = "WalkTimer"
ROUTE960.toField = "set_fraction"
ROUTE960.toNode = "Walk_r_thumb1_PitchInterpolator"

Scene34.children.append(ROUTE960)
ROUTE961 = x3d.ROUTE()
ROUTE961.fromField = "value_changed"
ROUTE961.fromNode = "Walk_r_ankle_RotationInterpolator"
ROUTE961.toField = "set_rotation"
ROUTE961.toNode = "boxman_r_ankle"

Scene34.children.append(ROUTE961)
ROUTE962 = x3d.ROUTE()
ROUTE962.fromField = "value_changed"
ROUTE962.fromNode = "Walk_r_knee_RotationInterpolator"
ROUTE962.toField = "set_rotation"
ROUTE962.toNode = "boxman_r_knee"

Scene34.children.append(ROUTE962)
ROUTE963 = x3d.ROUTE()
ROUTE963.fromField = "value_changed"
ROUTE963.fromNode = "Walk_r_hip_RotationInterpolator"
ROUTE963.toField = "set_rotation"
ROUTE963.toNode = "boxman_r_hip"

Scene34.children.append(ROUTE963)
ROUTE964 = x3d.ROUTE()
ROUTE964.fromField = "value_changed"
ROUTE964.fromNode = "Walk_l_ankle_RotationInterpolator"
ROUTE964.toField = "set_rotation"
ROUTE964.toNode = "boxman_l_ankle"

Scene34.children.append(ROUTE964)
ROUTE965 = x3d.ROUTE()
ROUTE965.fromField = "value_changed"
ROUTE965.fromNode = "Walk_l_knee_RotationInterpolator"
ROUTE965.toField = "set_rotation"
ROUTE965.toNode = "boxman_l_knee"

Scene34.children.append(ROUTE965)
ROUTE966 = x3d.ROUTE()
ROUTE966.fromField = "value_changed"
ROUTE966.fromNode = "Walk_l_hip_RotationInterpolator"
ROUTE966.toField = "set_rotation"
ROUTE966.toNode = "boxman_l_hip"

Scene34.children.append(ROUTE966)
ROUTE967 = x3d.ROUTE()
ROUTE967.fromField = "value_changed"
ROUTE967.fromNode = "Walk_r_wrist_RotationInterpolator"
ROUTE967.toField = "set_rotation"
ROUTE967.toNode = "boxman_r_wrist"

Scene34.children.append(ROUTE967)
ROUTE968 = x3d.ROUTE()
ROUTE968.fromField = "value_changed"
ROUTE968.fromNode = "Walk_r_elbow_RotationInterpolator"
ROUTE968.toField = "set_rotation"
ROUTE968.toNode = "boxman_r_elbow"

Scene34.children.append(ROUTE968)
ROUTE969 = x3d.ROUTE()
ROUTE969.fromField = "value_changed"
ROUTE969.fromNode = "Walk_r_shoulder_RotationInterpolator"
ROUTE969.toField = "set_rotation"
ROUTE969.toNode = "boxman_r_shoulder"

Scene34.children.append(ROUTE969)
ROUTE970 = x3d.ROUTE()
ROUTE970.fromField = "value_changed"
ROUTE970.fromNode = "Walk_l_wrist_RotationInterpolator"
ROUTE970.toField = "set_rotation"
ROUTE970.toNode = "boxman_l_wrist"

Scene34.children.append(ROUTE970)
ROUTE971 = x3d.ROUTE()
ROUTE971.fromField = "value_changed"
ROUTE971.fromNode = "Walk_l_elbow_RotationInterpolator"
ROUTE971.toField = "set_rotation"
ROUTE971.toNode = "boxman_l_elbow"

Scene34.children.append(ROUTE971)
ROUTE972 = x3d.ROUTE()
ROUTE972.fromField = "value_changed"
ROUTE972.fromNode = "Walk_l_shoulder_RotationInterpolator"
ROUTE972.toField = "set_rotation"
ROUTE972.toNode = "boxman_l_shoulder"

Scene34.children.append(ROUTE972)
ROUTE973 = x3d.ROUTE()
ROUTE973.fromField = "value_changed"
ROUTE973.fromNode = "Walk_head_RotationInterpolator"
ROUTE973.toField = "set_rotation"
ROUTE973.toNode = "boxman_skullbase"

Scene34.children.append(ROUTE973)
ROUTE974 = x3d.ROUTE()
ROUTE974.fromField = "value_changed"
ROUTE974.fromNode = "Walk_whole_body_RotationInterpolator"
ROUTE974.toField = "set_rotation"
ROUTE974.toNode = "boxman_humanoid_root"

Scene34.children.append(ROUTE974)
ROUTE975 = x3d.ROUTE()
ROUTE975.fromField = "value_changed"
ROUTE975.fromNode = "Walk_whole_body_TranslationInterpolator"
ROUTE975.toField = "set_translation"
ROUTE975.toNode = "boxman_humanoid_root"

Scene34.children.append(ROUTE975)
ROUTE976 = x3d.ROUTE()
ROUTE976.fromField = "value_changed"
ROUTE976.fromNode = "Walk_vl5_YawInterpolator"
ROUTE976.toField = "set_rotation"
ROUTE976.toNode = "boxman_vl5"

Scene34.children.append(ROUTE976)
ROUTE977 = x3d.ROUTE()
ROUTE977.fromField = "fraction_changed"
ROUTE977.fromNode = "RunTimer"
ROUTE977.toField = "set_fraction"
ROUTE977.toNode = "Run_r_ankle_RotationInterpolator_Run"

Scene34.children.append(ROUTE977)
ROUTE978 = x3d.ROUTE()
ROUTE978.fromField = "fraction_changed"
ROUTE978.fromNode = "RunTimer"
ROUTE978.toField = "set_fraction"
ROUTE978.toNode = "Run_r_knee_RotationInterpolator_Run"

Scene34.children.append(ROUTE978)
ROUTE979 = x3d.ROUTE()
ROUTE979.fromField = "fraction_changed"
ROUTE979.fromNode = "RunTimer"
ROUTE979.toField = "set_fraction"
ROUTE979.toNode = "Run_r_hip_RotationInterpolator_Run"

Scene34.children.append(ROUTE979)
ROUTE980 = x3d.ROUTE()
ROUTE980.fromField = "fraction_changed"
ROUTE980.fromNode = "RunTimer"
ROUTE980.toField = "set_fraction"
ROUTE980.toNode = "Run_l_ankle_RotationInterpolator_Run"

Scene34.children.append(ROUTE980)
ROUTE981 = x3d.ROUTE()
ROUTE981.fromField = "fraction_changed"
ROUTE981.fromNode = "RunTimer"
ROUTE981.toField = "set_fraction"
ROUTE981.toNode = "Run_l_knee_RotationInterpolator_Run"

Scene34.children.append(ROUTE981)
ROUTE982 = x3d.ROUTE()
ROUTE982.fromField = "fraction_changed"
ROUTE982.fromNode = "RunTimer"
ROUTE982.toField = "set_fraction"
ROUTE982.toNode = "Run_l_hip_RotationInterpolator_Run"

Scene34.children.append(ROUTE982)
ROUTE983 = x3d.ROUTE()
ROUTE983.fromField = "fraction_changed"
ROUTE983.fromNode = "RunTimer"
ROUTE983.toField = "set_fraction"
ROUTE983.toNode = "Run_lower_body_RotationInterpolator_Run"

Scene34.children.append(ROUTE983)
ROUTE984 = x3d.ROUTE()
ROUTE984.fromField = "fraction_changed"
ROUTE984.fromNode = "RunTimer"
ROUTE984.toField = "set_fraction"
ROUTE984.toNode = "Run_r_wrist_RotationInterpolator_Run"

Scene34.children.append(ROUTE984)
ROUTE985 = x3d.ROUTE()
ROUTE985.fromField = "fraction_changed"
ROUTE985.fromNode = "RunTimer"
ROUTE985.toField = "set_fraction"
ROUTE985.toNode = "Run_r_elbow_RotationInterpolator_Run"

Scene34.children.append(ROUTE985)
ROUTE986 = x3d.ROUTE()
ROUTE986.fromField = "fraction_changed"
ROUTE986.fromNode = "RunTimer"
ROUTE986.toField = "set_fraction"
ROUTE986.toNode = "Run_r_shoulder_RotationInterpolator_Run"

Scene34.children.append(ROUTE986)
ROUTE987 = x3d.ROUTE()
ROUTE987.fromField = "fraction_changed"
ROUTE987.fromNode = "RunTimer"
ROUTE987.toField = "set_fraction"
ROUTE987.toNode = "Run_l_wrist_RotationInterpolator_Run"

Scene34.children.append(ROUTE987)
ROUTE988 = x3d.ROUTE()
ROUTE988.fromField = "fraction_changed"
ROUTE988.fromNode = "RunTimer"
ROUTE988.toField = "set_fraction"
ROUTE988.toNode = "Run_l_elbow_RotationInterpolator_Run"

Scene34.children.append(ROUTE988)
ROUTE989 = x3d.ROUTE()
ROUTE989.fromField = "fraction_changed"
ROUTE989.fromNode = "RunTimer"
ROUTE989.toField = "set_fraction"
ROUTE989.toNode = "Run_l_shoulder_RotationInterpolator_Run"

Scene34.children.append(ROUTE989)
ROUTE990 = x3d.ROUTE()
ROUTE990.fromField = "fraction_changed"
ROUTE990.fromNode = "RunTimer"
ROUTE990.toField = "set_fraction"
ROUTE990.toNode = "Run_head_RotationInterpolator_Run"

Scene34.children.append(ROUTE990)
ROUTE991 = x3d.ROUTE()
ROUTE991.fromField = "fraction_changed"
ROUTE991.fromNode = "RunTimer"
ROUTE991.toField = "set_fraction"
ROUTE991.toNode = "Run_neck_RotationInterpolator_Run"

Scene34.children.append(ROUTE991)
ROUTE992 = x3d.ROUTE()
ROUTE992.fromField = "fraction_changed"
ROUTE992.fromNode = "RunTimer"
ROUTE992.toField = "set_fraction"
ROUTE992.toNode = "Run_upper_body_RotationInterpolator_Run"

Scene34.children.append(ROUTE992)
ROUTE993 = x3d.ROUTE()
ROUTE993.fromField = "fraction_changed"
ROUTE993.fromNode = "RunTimer"
ROUTE993.toField = "set_fraction"
ROUTE993.toNode = "Run_whole_body_RotationInterpolator_Run"

Scene34.children.append(ROUTE993)
ROUTE994 = x3d.ROUTE()
ROUTE994.fromField = "fraction_changed"
ROUTE994.fromNode = "RunTimer"
ROUTE994.toField = "set_fraction"
ROUTE994.toNode = "Run_whole_body_TranslationInterpolator_Run"

Scene34.children.append(ROUTE994)
ROUTE995 = x3d.ROUTE()
ROUTE995.fromField = "fraction_changed"
ROUTE995.fromNode = "RunTimer"
ROUTE995.toField = "set_fraction"
ROUTE995.toNode = "Run_l_sternoclavicular_RollInterpolator"

Scene34.children.append(ROUTE995)
ROUTE996 = x3d.ROUTE()
ROUTE996.fromField = "fraction_changed"
ROUTE996.fromNode = "RunTimer"
ROUTE996.toField = "set_fraction"
ROUTE996.toNode = "Run_l_acromioclavicular_RollInterpolator"

Scene34.children.append(ROUTE996)
ROUTE997 = x3d.ROUTE()
ROUTE997.fromField = "fraction_changed"
ROUTE997.fromNode = "RunTimer"
ROUTE997.toField = "set_fraction"
ROUTE997.toNode = "Run_r_sternoclavicular_RollInterpolator"

Scene34.children.append(ROUTE997)
ROUTE998 = x3d.ROUTE()
ROUTE998.fromField = "fraction_changed"
ROUTE998.fromNode = "RunTimer"
ROUTE998.toField = "set_fraction"
ROUTE998.toNode = "Run_r_acromioclavicular_RollInterpolator"

Scene34.children.append(ROUTE998)
ROUTE999 = x3d.ROUTE()
ROUTE999.fromField = "fraction_changed"
ROUTE999.fromNode = "RunTimer"
ROUTE999.toField = "set_fraction"
ROUTE999.toNode = "Run_r_metatarsal_PitchInterpolator"

Scene34.children.append(ROUTE999)
ROUTE1000 = x3d.ROUTE()
ROUTE1000.fromField = "fraction_changed"
ROUTE1000.fromNode = "RunTimer"
ROUTE1000.toField = "set_fraction"
ROUTE1000.toNode = "Run_sacroiliac_YawInterpolator"

Scene34.children.append(ROUTE1000)
ROUTE1001 = x3d.ROUTE()
ROUTE1001.fromField = "fraction_changed"
ROUTE1001.fromNode = "RunTimer"
ROUTE1001.toField = "set_fraction"
ROUTE1001.toNode = "Run_vl5_YawInterpolator"

Scene34.children.append(ROUTE1001)
ROUTE1002 = x3d.ROUTE()
ROUTE1002.fromField = "fraction_changed"
ROUTE1002.fromNode = "RunTimer"
ROUTE1002.toField = "set_fraction"
ROUTE1002.toNode = "Run_vc6_YawInterpolator"

Scene34.children.append(ROUTE1002)
ROUTE1003 = x3d.ROUTE()
ROUTE1003.fromField = "fraction_changed"
ROUTE1003.fromNode = "RunTimer"
ROUTE1003.toField = "set_fraction"
ROUTE1003.toNode = "Run_l_thumb1_PitchInterpolator"

Scene34.children.append(ROUTE1003)
ROUTE1004 = x3d.ROUTE()
ROUTE1004.fromField = "fraction_changed"
ROUTE1004.fromNode = "RunTimer"
ROUTE1004.toField = "set_fraction"
ROUTE1004.toNode = "Run_r_thumb1_PitchInterpolator"

Scene34.children.append(ROUTE1004)
ROUTE1005 = x3d.ROUTE()
ROUTE1005.fromField = "value_changed"
ROUTE1005.fromNode = "Run_r_ankle_RotationInterpolator_Run"
ROUTE1005.toField = "set_rotation"
ROUTE1005.toNode = "boxman_r_ankle"

Scene34.children.append(ROUTE1005)
ROUTE1006 = x3d.ROUTE()
ROUTE1006.fromField = "value_changed"
ROUTE1006.fromNode = "Run_r_knee_RotationInterpolator_Run"
ROUTE1006.toField = "set_rotation"
ROUTE1006.toNode = "boxman_r_knee"

Scene34.children.append(ROUTE1006)
ROUTE1007 = x3d.ROUTE()
ROUTE1007.fromField = "value_changed"
ROUTE1007.fromNode = "Run_r_hip_RotationInterpolator_Run"
ROUTE1007.toField = "set_rotation"
ROUTE1007.toNode = "boxman_r_hip"

Scene34.children.append(ROUTE1007)
ROUTE1008 = x3d.ROUTE()
ROUTE1008.fromField = "value_changed"
ROUTE1008.fromNode = "Run_l_ankle_RotationInterpolator_Run"
ROUTE1008.toField = "set_rotation"
ROUTE1008.toNode = "boxman_l_ankle"

Scene34.children.append(ROUTE1008)
ROUTE1009 = x3d.ROUTE()
ROUTE1009.fromField = "value_changed"
ROUTE1009.fromNode = "Run_l_knee_RotationInterpolator_Run"
ROUTE1009.toField = "set_rotation"
ROUTE1009.toNode = "boxman_l_knee"

Scene34.children.append(ROUTE1009)
ROUTE1010 = x3d.ROUTE()
ROUTE1010.fromField = "value_changed"
ROUTE1010.fromNode = "Run_l_hip_RotationInterpolator_Run"
ROUTE1010.toField = "set_rotation"
ROUTE1010.toNode = "boxman_l_hip"

Scene34.children.append(ROUTE1010)
ROUTE1011 = x3d.ROUTE()
ROUTE1011.fromField = "value_changed"
ROUTE1011.fromNode = "Run_r_wrist_RotationInterpolator_Run"
ROUTE1011.toField = "set_rotation"
ROUTE1011.toNode = "boxman_r_wrist"

Scene34.children.append(ROUTE1011)
ROUTE1012 = x3d.ROUTE()
ROUTE1012.fromField = "value_changed"
ROUTE1012.fromNode = "Run_r_elbow_RotationInterpolator_Run"
ROUTE1012.toField = "set_rotation"
ROUTE1012.toNode = "boxman_r_elbow"

Scene34.children.append(ROUTE1012)
ROUTE1013 = x3d.ROUTE()
ROUTE1013.fromField = "value_changed"
ROUTE1013.fromNode = "Run_r_shoulder_RotationInterpolator_Run"
ROUTE1013.toField = "set_rotation"
ROUTE1013.toNode = "boxman_r_shoulder"

Scene34.children.append(ROUTE1013)
ROUTE1014 = x3d.ROUTE()
ROUTE1014.fromField = "value_changed"
ROUTE1014.fromNode = "Run_l_wrist_RotationInterpolator_Run"
ROUTE1014.toField = "set_rotation"
ROUTE1014.toNode = "boxman_l_wrist"

Scene34.children.append(ROUTE1014)
ROUTE1015 = x3d.ROUTE()
ROUTE1015.fromField = "value_changed"
ROUTE1015.fromNode = "Run_l_elbow_RotationInterpolator_Run"
ROUTE1015.toField = "set_rotation"
ROUTE1015.toNode = "boxman_l_elbow"

Scene34.children.append(ROUTE1015)
ROUTE1016 = x3d.ROUTE()
ROUTE1016.fromField = "value_changed"
ROUTE1016.fromNode = "Run_l_shoulder_RotationInterpolator_Run"
ROUTE1016.toField = "set_rotation"
ROUTE1016.toNode = "boxman_l_shoulder"

Scene34.children.append(ROUTE1016)
ROUTE1017 = x3d.ROUTE()
ROUTE1017.fromField = "value_changed"
ROUTE1017.fromNode = "Run_head_RotationInterpolator_Run"
ROUTE1017.toField = "set_rotation"
ROUTE1017.toNode = "boxman_skullbase"

Scene34.children.append(ROUTE1017)
ROUTE1018 = x3d.ROUTE()
ROUTE1018.fromField = "value_changed"
ROUTE1018.fromNode = "Run_whole_body_RotationInterpolator_Run"
ROUTE1018.toField = "set_rotation"
ROUTE1018.toNode = "boxman_humanoid_root"

Scene34.children.append(ROUTE1018)
ROUTE1019 = x3d.ROUTE()
ROUTE1019.fromField = "value_changed"
ROUTE1019.fromNode = "Run_whole_body_TranslationInterpolator_Run"
ROUTE1019.toField = "set_translation"
ROUTE1019.toNode = "boxman_humanoid_root"

Scene34.children.append(ROUTE1019)
ROUTE1020 = x3d.ROUTE()
ROUTE1020.fromField = "value_changed"
ROUTE1020.fromNode = "Run_vl5_YawInterpolator"
ROUTE1020.toField = "set_rotation"
ROUTE1020.toNode = "boxman_vl5"

Scene34.children.append(ROUTE1020)
ROUTE1021 = x3d.ROUTE()
ROUTE1021.fromField = "fraction_changed"
ROUTE1021.fromNode = "JumpTimer"
ROUTE1021.toField = "set_fraction"
ROUTE1021.toNode = "Jump_r_ankle_RotationInterpolator"

Scene34.children.append(ROUTE1021)
ROUTE1022 = x3d.ROUTE()
ROUTE1022.fromField = "fraction_changed"
ROUTE1022.fromNode = "JumpTimer"
ROUTE1022.toField = "set_fraction"
ROUTE1022.toNode = "Jump_r_knee_RotationInterpolator"

Scene34.children.append(ROUTE1022)
ROUTE1023 = x3d.ROUTE()
ROUTE1023.fromField = "fraction_changed"
ROUTE1023.fromNode = "JumpTimer"
ROUTE1023.toField = "set_fraction"
ROUTE1023.toNode = "Jump_r_hip_RotationInterpolator"

Scene34.children.append(ROUTE1023)
ROUTE1024 = x3d.ROUTE()
ROUTE1024.fromField = "fraction_changed"
ROUTE1024.fromNode = "JumpTimer"
ROUTE1024.toField = "set_fraction"
ROUTE1024.toNode = "Jump_l_ankle_RotationInterpolator"

Scene34.children.append(ROUTE1024)
ROUTE1025 = x3d.ROUTE()
ROUTE1025.fromField = "fraction_changed"
ROUTE1025.fromNode = "JumpTimer"
ROUTE1025.toField = "set_fraction"
ROUTE1025.toNode = "Jump_l_knee_RotationInterpolator"

Scene34.children.append(ROUTE1025)
ROUTE1026 = x3d.ROUTE()
ROUTE1026.fromField = "fraction_changed"
ROUTE1026.fromNode = "JumpTimer"
ROUTE1026.toField = "set_fraction"
ROUTE1026.toNode = "Jump_l_hip_RotationInterpolator"

Scene34.children.append(ROUTE1026)
ROUTE1027 = x3d.ROUTE()
ROUTE1027.fromField = "fraction_changed"
ROUTE1027.fromNode = "JumpTimer"
ROUTE1027.toField = "set_fraction"
ROUTE1027.toNode = "Jump_lower_body_RotationInterpolator"

Scene34.children.append(ROUTE1027)
ROUTE1028 = x3d.ROUTE()
ROUTE1028.fromField = "fraction_changed"
ROUTE1028.fromNode = "JumpTimer"
ROUTE1028.toField = "set_fraction"
ROUTE1028.toNode = "Jump_r_wrist_RotationInterpolator"

Scene34.children.append(ROUTE1028)
ROUTE1029 = x3d.ROUTE()
ROUTE1029.fromField = "fraction_changed"
ROUTE1029.fromNode = "JumpTimer"
ROUTE1029.toField = "set_fraction"
ROUTE1029.toNode = "Jump_r_elbow_RotationInterpolator"

Scene34.children.append(ROUTE1029)
ROUTE1030 = x3d.ROUTE()
ROUTE1030.fromField = "fraction_changed"
ROUTE1030.fromNode = "JumpTimer"
ROUTE1030.toField = "set_fraction"
ROUTE1030.toNode = "Jump_r_shoulder_RotationInterpolator"

Scene34.children.append(ROUTE1030)
ROUTE1031 = x3d.ROUTE()
ROUTE1031.fromField = "fraction_changed"
ROUTE1031.fromNode = "JumpTimer"
ROUTE1031.toField = "set_fraction"
ROUTE1031.toNode = "Jump_l_wrist_RotationInterpolator"

Scene34.children.append(ROUTE1031)
ROUTE1032 = x3d.ROUTE()
ROUTE1032.fromField = "fraction_changed"
ROUTE1032.fromNode = "JumpTimer"
ROUTE1032.toField = "set_fraction"
ROUTE1032.toNode = "Jump_l_elbow_RotationInterpolator"

Scene34.children.append(ROUTE1032)
ROUTE1033 = x3d.ROUTE()
ROUTE1033.fromField = "fraction_changed"
ROUTE1033.fromNode = "JumpTimer"
ROUTE1033.toField = "set_fraction"
ROUTE1033.toNode = "Jump_l_shoulder_RotationInterpolator"

Scene34.children.append(ROUTE1033)
ROUTE1034 = x3d.ROUTE()
ROUTE1034.fromField = "fraction_changed"
ROUTE1034.fromNode = "JumpTimer"
ROUTE1034.toField = "set_fraction"
ROUTE1034.toNode = "Jump_head_RotationInterpolator"

Scene34.children.append(ROUTE1034)
ROUTE1035 = x3d.ROUTE()
ROUTE1035.fromField = "fraction_changed"
ROUTE1035.fromNode = "JumpTimer"
ROUTE1035.toField = "set_fraction"
ROUTE1035.toNode = "Jump_neck_RotationInterpolator"

Scene34.children.append(ROUTE1035)
ROUTE1036 = x3d.ROUTE()
ROUTE1036.fromField = "fraction_changed"
ROUTE1036.fromNode = "JumpTimer"
ROUTE1036.toField = "set_fraction"
ROUTE1036.toNode = "Jump_upper_body_RotationInterpolator"

Scene34.children.append(ROUTE1036)
ROUTE1037 = x3d.ROUTE()
ROUTE1037.fromField = "fraction_changed"
ROUTE1037.fromNode = "JumpTimer"
ROUTE1037.toField = "set_fraction"
ROUTE1037.toNode = "Jump_whole_body_RotationInterpolator"

Scene34.children.append(ROUTE1037)
ROUTE1038 = x3d.ROUTE()
ROUTE1038.fromField = "fraction_changed"
ROUTE1038.fromNode = "JumpTimer"
ROUTE1038.toField = "set_fraction"
ROUTE1038.toNode = "Jump_whole_body_TranslationInterpolator"

Scene34.children.append(ROUTE1038)
ROUTE1039 = x3d.ROUTE()
ROUTE1039.fromField = "fraction_changed"
ROUTE1039.fromNode = "JumpTimer"
ROUTE1039.toField = "set_fraction"
ROUTE1039.toNode = "Jump_l_sternoclavicular_RollInterpolator"

Scene34.children.append(ROUTE1039)
ROUTE1040 = x3d.ROUTE()
ROUTE1040.fromField = "fraction_changed"
ROUTE1040.fromNode = "JumpTimer"
ROUTE1040.toField = "set_fraction"
ROUTE1040.toNode = "Jump_l_acromioclavicular_RollInterpolator"

Scene34.children.append(ROUTE1040)
ROUTE1041 = x3d.ROUTE()
ROUTE1041.fromField = "fraction_changed"
ROUTE1041.fromNode = "JumpTimer"
ROUTE1041.toField = "set_fraction"
ROUTE1041.toNode = "Jump_r_sternoclavicular_RollInterpolator"

Scene34.children.append(ROUTE1041)
ROUTE1042 = x3d.ROUTE()
ROUTE1042.fromField = "fraction_changed"
ROUTE1042.fromNode = "JumpTimer"
ROUTE1042.toField = "set_fraction"
ROUTE1042.toNode = "Jump_r_acromioclavicular_RollInterpolator"

Scene34.children.append(ROUTE1042)
ROUTE1043 = x3d.ROUTE()
ROUTE1043.fromField = "fraction_changed"
ROUTE1043.fromNode = "JumpTimer"
ROUTE1043.toField = "set_fraction"
ROUTE1043.toNode = "Jump_r_metatarsal_PitchInterpolator"

Scene34.children.append(ROUTE1043)
ROUTE1044 = x3d.ROUTE()
ROUTE1044.fromField = "fraction_changed"
ROUTE1044.fromNode = "JumpTimer"
ROUTE1044.toField = "set_fraction"
ROUTE1044.toNode = "Jump_sacroiliac_YawInterpolator"

Scene34.children.append(ROUTE1044)
ROUTE1045 = x3d.ROUTE()
ROUTE1045.fromField = "fraction_changed"
ROUTE1045.fromNode = "JumpTimer"
ROUTE1045.toField = "set_fraction"
ROUTE1045.toNode = "Jump_vl5_YawInterpolator"

Scene34.children.append(ROUTE1045)
ROUTE1046 = x3d.ROUTE()
ROUTE1046.fromField = "fraction_changed"
ROUTE1046.fromNode = "JumpTimer"
ROUTE1046.toField = "set_fraction"
ROUTE1046.toNode = "Jump_vc6_YawInterpolator"

Scene34.children.append(ROUTE1046)
ROUTE1047 = x3d.ROUTE()
ROUTE1047.fromField = "fraction_changed"
ROUTE1047.fromNode = "JumpTimer"
ROUTE1047.toField = "set_fraction"
ROUTE1047.toNode = "Jump_l_thumb1_PitchInterpolator"

Scene34.children.append(ROUTE1047)
ROUTE1048 = x3d.ROUTE()
ROUTE1048.fromField = "fraction_changed"
ROUTE1048.fromNode = "JumpTimer"
ROUTE1048.toField = "set_fraction"
ROUTE1048.toNode = "Jump_r_thumb1_PitchInterpolator"

Scene34.children.append(ROUTE1048)
ROUTE1049 = x3d.ROUTE()
ROUTE1049.fromField = "value_changed"
ROUTE1049.fromNode = "Jump_r_ankle_RotationInterpolator"
ROUTE1049.toField = "set_rotation"
ROUTE1049.toNode = "boxman_r_ankle"

Scene34.children.append(ROUTE1049)
ROUTE1050 = x3d.ROUTE()
ROUTE1050.fromField = "value_changed"
ROUTE1050.fromNode = "Jump_r_knee_RotationInterpolator"
ROUTE1050.toField = "set_rotation"
ROUTE1050.toNode = "boxman_r_knee"

Scene34.children.append(ROUTE1050)
ROUTE1051 = x3d.ROUTE()
ROUTE1051.fromField = "value_changed"
ROUTE1051.fromNode = "Jump_r_hip_RotationInterpolator"
ROUTE1051.toField = "set_rotation"
ROUTE1051.toNode = "boxman_r_hip"

Scene34.children.append(ROUTE1051)
ROUTE1052 = x3d.ROUTE()
ROUTE1052.fromField = "value_changed"
ROUTE1052.fromNode = "Jump_l_ankle_RotationInterpolator"
ROUTE1052.toField = "set_rotation"
ROUTE1052.toNode = "boxman_l_ankle"

Scene34.children.append(ROUTE1052)
ROUTE1053 = x3d.ROUTE()
ROUTE1053.fromField = "value_changed"
ROUTE1053.fromNode = "Jump_l_knee_RotationInterpolator"
ROUTE1053.toField = "set_rotation"
ROUTE1053.toNode = "boxman_l_knee"

Scene34.children.append(ROUTE1053)
ROUTE1054 = x3d.ROUTE()
ROUTE1054.fromField = "value_changed"
ROUTE1054.fromNode = "Jump_l_hip_RotationInterpolator"
ROUTE1054.toField = "set_rotation"
ROUTE1054.toNode = "boxman_l_hip"

Scene34.children.append(ROUTE1054)
ROUTE1055 = x3d.ROUTE()
ROUTE1055.fromField = "value_changed"
ROUTE1055.fromNode = "Jump_r_wrist_RotationInterpolator"
ROUTE1055.toField = "set_rotation"
ROUTE1055.toNode = "boxman_r_wrist"

Scene34.children.append(ROUTE1055)
ROUTE1056 = x3d.ROUTE()
ROUTE1056.fromField = "value_changed"
ROUTE1056.fromNode = "Jump_r_elbow_RotationInterpolator"
ROUTE1056.toField = "set_rotation"
ROUTE1056.toNode = "boxman_r_elbow"

Scene34.children.append(ROUTE1056)
ROUTE1057 = x3d.ROUTE()
ROUTE1057.fromField = "value_changed"
ROUTE1057.fromNode = "Jump_r_shoulder_RotationInterpolator"
ROUTE1057.toField = "set_rotation"
ROUTE1057.toNode = "boxman_r_shoulder"

Scene34.children.append(ROUTE1057)
ROUTE1058 = x3d.ROUTE()
ROUTE1058.fromField = "value_changed"
ROUTE1058.fromNode = "Jump_l_wrist_RotationInterpolator"
ROUTE1058.toField = "set_rotation"
ROUTE1058.toNode = "boxman_l_wrist"

Scene34.children.append(ROUTE1058)
ROUTE1059 = x3d.ROUTE()
ROUTE1059.fromField = "value_changed"
ROUTE1059.fromNode = "Jump_l_elbow_RotationInterpolator"
ROUTE1059.toField = "set_rotation"
ROUTE1059.toNode = "boxman_l_elbow"

Scene34.children.append(ROUTE1059)
ROUTE1060 = x3d.ROUTE()
ROUTE1060.fromField = "value_changed"
ROUTE1060.fromNode = "Jump_l_shoulder_RotationInterpolator"
ROUTE1060.toField = "set_rotation"
ROUTE1060.toNode = "boxman_l_shoulder"

Scene34.children.append(ROUTE1060)
ROUTE1061 = x3d.ROUTE()
ROUTE1061.fromField = "value_changed"
ROUTE1061.fromNode = "Jump_head_RotationInterpolator"
ROUTE1061.toField = "set_rotation"
ROUTE1061.toNode = "boxman_skullbase"

Scene34.children.append(ROUTE1061)
ROUTE1062 = x3d.ROUTE()
ROUTE1062.fromField = "value_changed"
ROUTE1062.fromNode = "Jump_whole_body_RotationInterpolator"
ROUTE1062.toField = "set_rotation"
ROUTE1062.toNode = "boxman_humanoid_root"

Scene34.children.append(ROUTE1062)
ROUTE1063 = x3d.ROUTE()
ROUTE1063.fromField = "value_changed"
ROUTE1063.fromNode = "Jump_whole_body_TranslationInterpolator"
ROUTE1063.toField = "set_translation"
ROUTE1063.toNode = "boxman_humanoid_root"

Scene34.children.append(ROUTE1063)
ROUTE1064 = x3d.ROUTE()
ROUTE1064.fromField = "value_changed"
ROUTE1064.fromNode = "Jump_vl5_YawInterpolator"
ROUTE1064.toField = "set_rotation"
ROUTE1064.toNode = "boxman_vl5"

Scene34.children.append(ROUTE1064)
ROUTE1065 = x3d.ROUTE()
ROUTE1065.fromField = "fraction_changed"
ROUTE1065.fromNode = "KickTimer"
ROUTE1065.toField = "set_fraction"
ROUTE1065.toNode = "Kick_l_sternoclavicular_RollInterpolator"

Scene34.children.append(ROUTE1065)
ROUTE1066 = x3d.ROUTE()
ROUTE1066.fromField = "fraction_changed"
ROUTE1066.fromNode = "KickTimer"
ROUTE1066.toField = "set_fraction"
ROUTE1066.toNode = "Kick_l_acromioclavicular_RollInterpolator"

Scene34.children.append(ROUTE1066)
ROUTE1067 = x3d.ROUTE()
ROUTE1067.fromField = "fraction_changed"
ROUTE1067.fromNode = "KickTimer"
ROUTE1067.toField = "set_fraction"
ROUTE1067.toNode = "Kick_l_shoulder_RollInterpolator"

Scene34.children.append(ROUTE1067)
ROUTE1068 = x3d.ROUTE()
ROUTE1068.fromField = "fraction_changed"
ROUTE1068.fromNode = "KickTimer"
ROUTE1068.toField = "set_fraction"
ROUTE1068.toNode = "Kick_l_ForeArm_PitchInterpolator"

Scene34.children.append(ROUTE1068)
ROUTE1069 = x3d.ROUTE()
ROUTE1069.fromField = "fraction_changed"
ROUTE1069.fromNode = "KickTimer"
ROUTE1069.toField = "set_fraction"
ROUTE1069.toNode = "Kick_l_wrist_RollInterpolator"

Scene34.children.append(ROUTE1069)
ROUTE1070 = x3d.ROUTE()
ROUTE1070.fromField = "fraction_changed"
ROUTE1070.fromNode = "KickTimer"
ROUTE1070.toField = "set_fraction"
ROUTE1070.toNode = "Kick_l_thumb1_PitchInterpolator"

Scene34.children.append(ROUTE1070)
ROUTE1071 = x3d.ROUTE()
ROUTE1071.fromField = "fraction_changed"
ROUTE1071.fromNode = "KickTimer"
ROUTE1071.toField = "set_fraction"
ROUTE1071.toNode = "Kick_r_sternoclavicular_RollInterpolator"

Scene34.children.append(ROUTE1071)
ROUTE1072 = x3d.ROUTE()
ROUTE1072.fromField = "fraction_changed"
ROUTE1072.fromNode = "KickTimer"
ROUTE1072.toField = "set_fraction"
ROUTE1072.toNode = "Kick_r_acromioclavicular_RollInterpolator"

Scene34.children.append(ROUTE1072)
ROUTE1073 = x3d.ROUTE()
ROUTE1073.fromField = "fraction_changed"
ROUTE1073.fromNode = "KickTimer"
ROUTE1073.toField = "set_fraction"
ROUTE1073.toNode = "Kick_r_shoulder_RollInterpolator"

Scene34.children.append(ROUTE1073)
ROUTE1074 = x3d.ROUTE()
ROUTE1074.fromField = "fraction_changed"
ROUTE1074.fromNode = "KickTimer"
ROUTE1074.toField = "set_fraction"
ROUTE1074.toNode = "Kick_r_ForeArm_PitchInterpolator"

Scene34.children.append(ROUTE1074)
ROUTE1075 = x3d.ROUTE()
ROUTE1075.fromField = "fraction_changed"
ROUTE1075.fromNode = "KickTimer"
ROUTE1075.toField = "set_fraction"
ROUTE1075.toNode = "Kick_r_wrist_RollInterpolator"

Scene34.children.append(ROUTE1075)
ROUTE1076 = x3d.ROUTE()
ROUTE1076.fromField = "fraction_changed"
ROUTE1076.fromNode = "KickTimer"
ROUTE1076.toField = "set_fraction"
ROUTE1076.toNode = "Kick_r_thumb1_PitchInterpolator"

Scene34.children.append(ROUTE1076)
ROUTE1077 = x3d.ROUTE()
ROUTE1077.fromField = "fraction_changed"
ROUTE1077.fromNode = "KickTimer"
ROUTE1077.toField = "set_fraction"
ROUTE1077.toNode = "Kick_r_hip_PitchInterpolator"

Scene34.children.append(ROUTE1077)
ROUTE1078 = x3d.ROUTE()
ROUTE1078.fromField = "fraction_changed"
ROUTE1078.fromNode = "KickTimer"
ROUTE1078.toField = "set_fraction"
ROUTE1078.toNode = "Kick_r_knee_PitchInterpolator"

Scene34.children.append(ROUTE1078)
ROUTE1079 = x3d.ROUTE()
ROUTE1079.fromField = "fraction_changed"
ROUTE1079.fromNode = "KickTimer"
ROUTE1079.toField = "set_fraction"
ROUTE1079.toNode = "Kick_l_hip_PitchInterpolator"

Scene34.children.append(ROUTE1079)
ROUTE1080 = x3d.ROUTE()
ROUTE1080.fromField = "fraction_changed"
ROUTE1080.fromNode = "KickTimer"
ROUTE1080.toField = "set_fraction"
ROUTE1080.toNode = "Kick_l_knee_PitchInterpolator"

Scene34.children.append(ROUTE1080)
ROUTE1081 = x3d.ROUTE()
ROUTE1081.fromField = "fraction_changed"
ROUTE1081.fromNode = "KickTimer"
ROUTE1081.toField = "set_fraction"
ROUTE1081.toNode = "Kick_r_ankle_PitchInterpolator"

Scene34.children.append(ROUTE1081)
ROUTE1082 = x3d.ROUTE()
ROUTE1082.fromField = "fraction_changed"
ROUTE1082.fromNode = "KickTimer"
ROUTE1082.toField = "set_fraction"
ROUTE1082.toNode = "Kick_r_metatarsal_PitchInterpolator"

Scene34.children.append(ROUTE1082)
ROUTE1083 = x3d.ROUTE()
ROUTE1083.fromField = "fraction_changed"
ROUTE1083.fromNode = "KickTimer"
ROUTE1083.toField = "set_fraction"
ROUTE1083.toNode = "Kick_sacroiliac_YawInterpolator"

Scene34.children.append(ROUTE1083)
ROUTE1084 = x3d.ROUTE()
ROUTE1084.fromField = "fraction_changed"
ROUTE1084.fromNode = "KickTimer"
ROUTE1084.toField = "set_fraction"
ROUTE1084.toNode = "Kick_vl5_YawInterpolator"

Scene34.children.append(ROUTE1084)
ROUTE1085 = x3d.ROUTE()
ROUTE1085.fromField = "fraction_changed"
ROUTE1085.fromNode = "KickTimer"
ROUTE1085.toField = "set_fraction"
ROUTE1085.toNode = "Kick_vc6_YawInterpolator"

Scene34.children.append(ROUTE1085)
ROUTE1086 = x3d.ROUTE()
ROUTE1086.fromField = "fraction_changed"
ROUTE1086.fromNode = "KickTimer"
ROUTE1086.toField = "set_fraction"
ROUTE1086.toNode = "Kick_lower_body_RotationInterpolator"

Scene34.children.append(ROUTE1086)
ROUTE1087 = x3d.ROUTE()
ROUTE1087.fromField = "fraction_changed"
ROUTE1087.fromNode = "KickTimer"
ROUTE1087.toField = "set_fraction"
ROUTE1087.toNode = "Kick_upper_body_RotationInterpolator"

Scene34.children.append(ROUTE1087)
ROUTE1088 = x3d.ROUTE()
ROUTE1088.fromField = "fraction_changed"
ROUTE1088.fromNode = "KickTimer"
ROUTE1088.toField = "set_fraction"
ROUTE1088.toNode = "Kick_whole_body_RotationInterpolator"

Scene34.children.append(ROUTE1088)
ROUTE1089 = x3d.ROUTE()
ROUTE1089.fromField = "fraction_changed"
ROUTE1089.fromNode = "KickTimer"
ROUTE1089.toField = "set_fraction"
ROUTE1089.toNode = "Kick_whole_body_TranslationInterpolator"

Scene34.children.append(ROUTE1089)
ROUTE1090 = x3d.ROUTE()
ROUTE1090.fromField = "fraction_changed"
ROUTE1090.fromNode = "KickTimer"
ROUTE1090.toField = "set_fraction"
ROUTE1090.toNode = "Kick_neck_RotationInterpolator"

Scene34.children.append(ROUTE1090)
ROUTE1091 = x3d.ROUTE()
ROUTE1091.fromField = "value_changed"
ROUTE1091.fromNode = "Kick_l_shoulder_RollInterpolator"
ROUTE1091.toField = "set_rotation"
ROUTE1091.toNode = "boxman_l_shoulder"

Scene34.children.append(ROUTE1091)
ROUTE1092 = x3d.ROUTE()
ROUTE1092.fromField = "value_changed"
ROUTE1092.fromNode = "Kick_l_ForeArm_PitchInterpolator"
ROUTE1092.toField = "set_rotation"
ROUTE1092.toNode = "boxman_l_elbow"

Scene34.children.append(ROUTE1092)
ROUTE1093 = x3d.ROUTE()
ROUTE1093.fromField = "value_changed"
ROUTE1093.fromNode = "Kick_l_wrist_RollInterpolator"
ROUTE1093.toField = "set_rotation"
ROUTE1093.toNode = "boxman_l_wrist"

Scene34.children.append(ROUTE1093)
ROUTE1094 = x3d.ROUTE()
ROUTE1094.fromField = "value_changed"
ROUTE1094.fromNode = "Kick_r_shoulder_RollInterpolator"
ROUTE1094.toField = "set_rotation"
ROUTE1094.toNode = "boxman_r_shoulder"

Scene34.children.append(ROUTE1094)
ROUTE1095 = x3d.ROUTE()
ROUTE1095.fromField = "value_changed"
ROUTE1095.fromNode = "Kick_r_ForeArm_PitchInterpolator"
ROUTE1095.toField = "set_rotation"
ROUTE1095.toNode = "boxman_r_elbow"

Scene34.children.append(ROUTE1095)
ROUTE1096 = x3d.ROUTE()
ROUTE1096.fromField = "value_changed"
ROUTE1096.fromNode = "Kick_r_wrist_RollInterpolator"
ROUTE1096.toField = "set_rotation"
ROUTE1096.toNode = "boxman_r_wrist"

Scene34.children.append(ROUTE1096)
ROUTE1097 = x3d.ROUTE()
ROUTE1097.fromField = "value_changed"
ROUTE1097.fromNode = "Kick_r_hip_PitchInterpolator"
ROUTE1097.toField = "set_rotation"
ROUTE1097.toNode = "boxman_r_hip"

Scene34.children.append(ROUTE1097)
ROUTE1098 = x3d.ROUTE()
ROUTE1098.fromField = "value_changed"
ROUTE1098.fromNode = "Kick_r_knee_PitchInterpolator"
ROUTE1098.toField = "set_rotation"
ROUTE1098.toNode = "boxman_r_knee"

Scene34.children.append(ROUTE1098)
ROUTE1099 = x3d.ROUTE()
ROUTE1099.fromField = "value_changed"
ROUTE1099.fromNode = "Kick_r_ankle_PitchInterpolator"
ROUTE1099.toField = "set_rotation"
ROUTE1099.toNode = "boxman_r_ankle"

Scene34.children.append(ROUTE1099)
ROUTE1100 = x3d.ROUTE()
ROUTE1100.fromField = "value_changed"
ROUTE1100.fromNode = "Kick_l_hip_PitchInterpolator"
ROUTE1100.toField = "set_rotation"
ROUTE1100.toNode = "boxman_l_hip"

Scene34.children.append(ROUTE1100)
ROUTE1101 = x3d.ROUTE()
ROUTE1101.fromField = "value_changed"
ROUTE1101.fromNode = "Kick_l_knee_PitchInterpolator"
ROUTE1101.toField = "set_rotation"
ROUTE1101.toNode = "boxman_l_knee"

Scene34.children.append(ROUTE1101)
ROUTE1102 = x3d.ROUTE()
ROUTE1102.fromField = "value_changed"
ROUTE1102.fromNode = "Kick_r_ankle_PitchInterpolator"
ROUTE1102.toField = "set_rotation"
ROUTE1102.toNode = "boxman_l_ankle"

Scene34.children.append(ROUTE1102)
ROUTE1103 = x3d.ROUTE()
ROUTE1103.fromField = "value_changed"
ROUTE1103.fromNode = "Kick_vl5_YawInterpolator"
ROUTE1103.toField = "set_rotation"
ROUTE1103.toNode = "boxman_vl5"

Scene34.children.append(ROUTE1103)
ROUTE1104 = x3d.ROUTE()
ROUTE1104.fromField = "value_changed"
ROUTE1104.fromNode = "Kick_whole_body_RotationInterpolator"
ROUTE1104.toField = "set_rotation"
ROUTE1104.toNode = "boxman_humanoid_root"

Scene34.children.append(ROUTE1104)
ROUTE1105 = x3d.ROUTE()
ROUTE1105.fromField = "value_changed"
ROUTE1105.fromNode = "Kick_whole_body_TranslationInterpolator"
ROUTE1105.toField = "set_translation"
ROUTE1105.toNode = "boxman_humanoid_root"

Scene34.children.append(ROUTE1105)
ROUTE1106 = x3d.ROUTE()
ROUTE1106.fromField = "position_changed"
ROUTE1106.fromNode = "HudProx"
ROUTE1106.toField = "set_translation"
ROUTE1106.toNode = "HudXform"

Scene34.children.append(ROUTE1106)
ROUTE1107 = x3d.ROUTE()
ROUTE1107.fromField = "orientation_changed"
ROUTE1107.fromNode = "HudProx"
ROUTE1107.toField = "set_rotation"
ROUTE1107.toNode = "HudXform"

Scene34.children.append(ROUTE1107)
ROUTE1108 = x3d.ROUTE()
ROUTE1108.fromField = "touchTime"
ROUTE1108.fromNode = "Stand_Touch"
ROUTE1108.toField = "set_stopTime"
ROUTE1108.toNode = "PitchTimer"

Scene34.children.append(ROUTE1108)
ROUTE1109 = x3d.ROUTE()
ROUTE1109.fromField = "touchTime"
ROUTE1109.fromNode = "Stand_Touch"
ROUTE1109.toField = "set_stopTime"
ROUTE1109.toNode = "YawTimer"

Scene34.children.append(ROUTE1109)
ROUTE1110 = x3d.ROUTE()
ROUTE1110.fromField = "touchTime"
ROUTE1110.fromNode = "Stand_Touch"
ROUTE1110.toField = "set_stopTime"
ROUTE1110.toNode = "RollTimer"

Scene34.children.append(ROUTE1110)
ROUTE1111 = x3d.ROUTE()
ROUTE1111.fromField = "touchTime"
ROUTE1111.fromNode = "Stand_Touch"
ROUTE1111.toField = "set_stopTime"
ROUTE1111.toNode = "WalkTimer"

Scene34.children.append(ROUTE1111)
ROUTE1112 = x3d.ROUTE()
ROUTE1112.fromField = "touchTime"
ROUTE1112.fromNode = "Stand_Touch"
ROUTE1112.toField = "set_stopTime"
ROUTE1112.toNode = "RunTimer"

Scene34.children.append(ROUTE1112)
ROUTE1113 = x3d.ROUTE()
ROUTE1113.fromField = "touchTime"
ROUTE1113.fromNode = "Stand_Touch"
ROUTE1113.toField = "set_stopTime"
ROUTE1113.toNode = "JumpTimer"

Scene34.children.append(ROUTE1113)
ROUTE1114 = x3d.ROUTE()
ROUTE1114.fromField = "touchTime"
ROUTE1114.fromNode = "Stand_Touch"
ROUTE1114.toField = "set_stopTime"
ROUTE1114.toNode = "KickTimer"

Scene34.children.append(ROUTE1114)
ROUTE1115 = x3d.ROUTE()
ROUTE1115.fromField = "touchTime"
ROUTE1115.fromNode = "Stand_Touch"
ROUTE1115.toField = "set_stopTime"
ROUTE1115.toNode = "StopTimer"

Scene34.children.append(ROUTE1115)
ROUTE1116 = x3d.ROUTE()
ROUTE1116.fromField = "touchTime"
ROUTE1116.fromNode = "Stand_Touch"
ROUTE1116.toField = "set_startTime"
ROUTE1116.toNode = "StandTimer"

Scene34.children.append(ROUTE1116)
ROUTE1117 = x3d.ROUTE()
ROUTE1117.fromField = "touchTime"
ROUTE1117.fromNode = "Pitch_Touch"
ROUTE1117.toField = "set_stopTime"
ROUTE1117.toNode = "StandTimer"

Scene34.children.append(ROUTE1117)
ROUTE1118 = x3d.ROUTE()
ROUTE1118.fromField = "touchTime"
ROUTE1118.fromNode = "Pitch_Touch"
ROUTE1118.toField = "set_stopTime"
ROUTE1118.toNode = "YawTimer"

Scene34.children.append(ROUTE1118)
ROUTE1119 = x3d.ROUTE()
ROUTE1119.fromField = "touchTime"
ROUTE1119.fromNode = "Pitch_Touch"
ROUTE1119.toField = "set_stopTime"
ROUTE1119.toNode = "RollTimer"

Scene34.children.append(ROUTE1119)
ROUTE1120 = x3d.ROUTE()
ROUTE1120.fromField = "touchTime"
ROUTE1120.fromNode = "Pitch_Touch"
ROUTE1120.toField = "set_stopTime"
ROUTE1120.toNode = "WalkTimer"

Scene34.children.append(ROUTE1120)
ROUTE1121 = x3d.ROUTE()
ROUTE1121.fromField = "touchTime"
ROUTE1121.fromNode = "Pitch_Touch"
ROUTE1121.toField = "set_stopTime"
ROUTE1121.toNode = "RunTimer"

Scene34.children.append(ROUTE1121)
ROUTE1122 = x3d.ROUTE()
ROUTE1122.fromField = "touchTime"
ROUTE1122.fromNode = "Pitch_Touch"
ROUTE1122.toField = "set_stopTime"
ROUTE1122.toNode = "JumpTimer"

Scene34.children.append(ROUTE1122)
ROUTE1123 = x3d.ROUTE()
ROUTE1123.fromField = "touchTime"
ROUTE1123.fromNode = "Pitch_Touch"
ROUTE1123.toField = "set_stopTime"
ROUTE1123.toNode = "KickTimer"

Scene34.children.append(ROUTE1123)
ROUTE1124 = x3d.ROUTE()
ROUTE1124.fromField = "touchTime"
ROUTE1124.fromNode = "Pitch_Touch"
ROUTE1124.toField = "set_stopTime"
ROUTE1124.toNode = "StopTimer"

Scene34.children.append(ROUTE1124)
ROUTE1125 = x3d.ROUTE()
ROUTE1125.fromField = "touchTime"
ROUTE1125.fromNode = "Pitch_Touch"
ROUTE1125.toField = "set_startTime"
ROUTE1125.toNode = "PitchTimer"

Scene34.children.append(ROUTE1125)
ROUTE1126 = x3d.ROUTE()
ROUTE1126.fromField = "touchTime"
ROUTE1126.fromNode = "Yaw_Touch"
ROUTE1126.toField = "set_stopTime"
ROUTE1126.toNode = "StandTimer"

Scene34.children.append(ROUTE1126)
ROUTE1127 = x3d.ROUTE()
ROUTE1127.fromField = "touchTime"
ROUTE1127.fromNode = "Yaw_Touch"
ROUTE1127.toField = "set_stopTime"
ROUTE1127.toNode = "PitchTimer"

Scene34.children.append(ROUTE1127)
ROUTE1128 = x3d.ROUTE()
ROUTE1128.fromField = "touchTime"
ROUTE1128.fromNode = "Yaw_Touch"
ROUTE1128.toField = "set_stopTime"
ROUTE1128.toNode = "RollTimer"

Scene34.children.append(ROUTE1128)
ROUTE1129 = x3d.ROUTE()
ROUTE1129.fromField = "touchTime"
ROUTE1129.fromNode = "Yaw_Touch"
ROUTE1129.toField = "set_stopTime"
ROUTE1129.toNode = "WalkTimer"

Scene34.children.append(ROUTE1129)
ROUTE1130 = x3d.ROUTE()
ROUTE1130.fromField = "touchTime"
ROUTE1130.fromNode = "Yaw_Touch"
ROUTE1130.toField = "set_stopTime"
ROUTE1130.toNode = "RunTimer"

Scene34.children.append(ROUTE1130)
ROUTE1131 = x3d.ROUTE()
ROUTE1131.fromField = "touchTime"
ROUTE1131.fromNode = "Yaw_Touch"
ROUTE1131.toField = "set_stopTime"
ROUTE1131.toNode = "JumpTimer"

Scene34.children.append(ROUTE1131)
ROUTE1132 = x3d.ROUTE()
ROUTE1132.fromField = "touchTime"
ROUTE1132.fromNode = "Yaw_Touch"
ROUTE1132.toField = "set_stopTime"
ROUTE1132.toNode = "KickTimer"

Scene34.children.append(ROUTE1132)
ROUTE1133 = x3d.ROUTE()
ROUTE1133.fromField = "touchTime"
ROUTE1133.fromNode = "Yaw_Touch"
ROUTE1133.toField = "set_stopTime"
ROUTE1133.toNode = "StopTimer"

Scene34.children.append(ROUTE1133)
ROUTE1134 = x3d.ROUTE()
ROUTE1134.fromField = "touchTime"
ROUTE1134.fromNode = "Yaw_Touch"
ROUTE1134.toField = "set_startTime"
ROUTE1134.toNode = "YawTimer"

Scene34.children.append(ROUTE1134)
ROUTE1135 = x3d.ROUTE()
ROUTE1135.fromField = "touchTime"
ROUTE1135.fromNode = "Walk_Touch"
ROUTE1135.toField = "set_stopTime"
ROUTE1135.toNode = "StandTimer"

Scene34.children.append(ROUTE1135)
ROUTE1136 = x3d.ROUTE()
ROUTE1136.fromField = "touchTime"
ROUTE1136.fromNode = "Walk_Touch"
ROUTE1136.toField = "set_stopTime"
ROUTE1136.toNode = "PitchTimer"

Scene34.children.append(ROUTE1136)
ROUTE1137 = x3d.ROUTE()
ROUTE1137.fromField = "touchTime"
ROUTE1137.fromNode = "Walk_Touch"
ROUTE1137.toField = "set_stopTime"
ROUTE1137.toNode = "YawTimer"

Scene34.children.append(ROUTE1137)
ROUTE1138 = x3d.ROUTE()
ROUTE1138.fromField = "touchTime"
ROUTE1138.fromNode = "Walk_Touch"
ROUTE1138.toField = "set_stopTime"
ROUTE1138.toNode = "RollTimer"

Scene34.children.append(ROUTE1138)
ROUTE1139 = x3d.ROUTE()
ROUTE1139.fromField = "touchTime"
ROUTE1139.fromNode = "Walk_Touch"
ROUTE1139.toField = "set_stopTime"
ROUTE1139.toNode = "RunTimer"

Scene34.children.append(ROUTE1139)
ROUTE1140 = x3d.ROUTE()
ROUTE1140.fromField = "touchTime"
ROUTE1140.fromNode = "Walk_Touch"
ROUTE1140.toField = "set_stopTime"
ROUTE1140.toNode = "JumpTimer"

Scene34.children.append(ROUTE1140)
ROUTE1141 = x3d.ROUTE()
ROUTE1141.fromField = "touchTime"
ROUTE1141.fromNode = "Walk_Touch"
ROUTE1141.toField = "set_stopTime"
ROUTE1141.toNode = "KickTimer"

Scene34.children.append(ROUTE1141)
ROUTE1142 = x3d.ROUTE()
ROUTE1142.fromField = "touchTime"
ROUTE1142.fromNode = "Walk_Touch"
ROUTE1142.toField = "set_stopTime"
ROUTE1142.toNode = "StopTimer"

Scene34.children.append(ROUTE1142)
ROUTE1143 = x3d.ROUTE()
ROUTE1143.fromField = "touchTime"
ROUTE1143.fromNode = "Walk_Touch"
ROUTE1143.toField = "set_startTime"
ROUTE1143.toNode = "WalkTimer"

Scene34.children.append(ROUTE1143)
ROUTE1144 = x3d.ROUTE()
ROUTE1144.fromField = "touchTime"
ROUTE1144.fromNode = "Roll_Touch"
ROUTE1144.toField = "set_stopTime"
ROUTE1144.toNode = "StandTimer"

Scene34.children.append(ROUTE1144)
ROUTE1145 = x3d.ROUTE()
ROUTE1145.fromField = "touchTime"
ROUTE1145.fromNode = "Roll_Touch"
ROUTE1145.toField = "set_stopTime"
ROUTE1145.toNode = "PitchTimer"

Scene34.children.append(ROUTE1145)
ROUTE1146 = x3d.ROUTE()
ROUTE1146.fromField = "touchTime"
ROUTE1146.fromNode = "Roll_Touch"
ROUTE1146.toField = "set_stopTime"
ROUTE1146.toNode = "YawTimer"

Scene34.children.append(ROUTE1146)
ROUTE1147 = x3d.ROUTE()
ROUTE1147.fromField = "touchTime"
ROUTE1147.fromNode = "Roll_Touch"
ROUTE1147.toField = "set_stopTime"
ROUTE1147.toNode = "WalkTimer"

Scene34.children.append(ROUTE1147)
ROUTE1148 = x3d.ROUTE()
ROUTE1148.fromField = "touchTime"
ROUTE1148.fromNode = "Roll_Touch"
ROUTE1148.toField = "set_stopTime"
ROUTE1148.toNode = "RunTimer"

Scene34.children.append(ROUTE1148)
ROUTE1149 = x3d.ROUTE()
ROUTE1149.fromField = "touchTime"
ROUTE1149.fromNode = "Roll_Touch"
ROUTE1149.toField = "set_stopTime"
ROUTE1149.toNode = "JumpTimer"

Scene34.children.append(ROUTE1149)
ROUTE1150 = x3d.ROUTE()
ROUTE1150.fromField = "touchTime"
ROUTE1150.fromNode = "Roll_Touch"
ROUTE1150.toField = "set_stopTime"
ROUTE1150.toNode = "KickTimer"

Scene34.children.append(ROUTE1150)
ROUTE1151 = x3d.ROUTE()
ROUTE1151.fromField = "touchTime"
ROUTE1151.fromNode = "Roll_Touch"
ROUTE1151.toField = "set_stopTime"
ROUTE1151.toNode = "StopTimer"

Scene34.children.append(ROUTE1151)
ROUTE1152 = x3d.ROUTE()
ROUTE1152.fromField = "touchTime"
ROUTE1152.fromNode = "Roll_Touch"
ROUTE1152.toField = "set_startTime"
ROUTE1152.toNode = "RollTimer"

Scene34.children.append(ROUTE1152)
ROUTE1153 = x3d.ROUTE()
ROUTE1153.fromField = "touchTime"
ROUTE1153.fromNode = "Run_Touch"
ROUTE1153.toField = "set_stopTime"
ROUTE1153.toNode = "StandTimer"

Scene34.children.append(ROUTE1153)
ROUTE1154 = x3d.ROUTE()
ROUTE1154.fromField = "touchTime"
ROUTE1154.fromNode = "Run_Touch"
ROUTE1154.toField = "set_stopTime"
ROUTE1154.toNode = "PitchTimer"

Scene34.children.append(ROUTE1154)
ROUTE1155 = x3d.ROUTE()
ROUTE1155.fromField = "touchTime"
ROUTE1155.fromNode = "Run_Touch"
ROUTE1155.toField = "set_stopTime"
ROUTE1155.toNode = "YawTimer"

Scene34.children.append(ROUTE1155)
ROUTE1156 = x3d.ROUTE()
ROUTE1156.fromField = "touchTime"
ROUTE1156.fromNode = "Run_Touch"
ROUTE1156.toField = "set_stopTime"
ROUTE1156.toNode = "RollTimer"

Scene34.children.append(ROUTE1156)
ROUTE1157 = x3d.ROUTE()
ROUTE1157.fromField = "touchTime"
ROUTE1157.fromNode = "Run_Touch"
ROUTE1157.toField = "set_stopTime"
ROUTE1157.toNode = "WalkTimer"

Scene34.children.append(ROUTE1157)
ROUTE1158 = x3d.ROUTE()
ROUTE1158.fromField = "touchTime"
ROUTE1158.fromNode = "Run_Touch"
ROUTE1158.toField = "set_stopTime"
ROUTE1158.toNode = "JumpTimer"

Scene34.children.append(ROUTE1158)
ROUTE1159 = x3d.ROUTE()
ROUTE1159.fromField = "touchTime"
ROUTE1159.fromNode = "Run_Touch"
ROUTE1159.toField = "set_stopTime"
ROUTE1159.toNode = "KickTimer"

Scene34.children.append(ROUTE1159)
ROUTE1160 = x3d.ROUTE()
ROUTE1160.fromField = "touchTime"
ROUTE1160.fromNode = "Run_Touch"
ROUTE1160.toField = "set_stopTime"
ROUTE1160.toNode = "StopTimer"

Scene34.children.append(ROUTE1160)
ROUTE1161 = x3d.ROUTE()
ROUTE1161.fromField = "touchTime"
ROUTE1161.fromNode = "Run_Touch"
ROUTE1161.toField = "set_startTime"
ROUTE1161.toNode = "RunTimer"

Scene34.children.append(ROUTE1161)
ROUTE1162 = x3d.ROUTE()
ROUTE1162.fromField = "touchTime"
ROUTE1162.fromNode = "Jump_Touch"
ROUTE1162.toField = "set_stopTime"
ROUTE1162.toNode = "StandTimer"

Scene34.children.append(ROUTE1162)
ROUTE1163 = x3d.ROUTE()
ROUTE1163.fromField = "touchTime"
ROUTE1163.fromNode = "Jump_Touch"
ROUTE1163.toField = "set_stopTime"
ROUTE1163.toNode = "PitchTimer"

Scene34.children.append(ROUTE1163)
ROUTE1164 = x3d.ROUTE()
ROUTE1164.fromField = "touchTime"
ROUTE1164.fromNode = "Jump_Touch"
ROUTE1164.toField = "set_stopTime"
ROUTE1164.toNode = "YawTimer"

Scene34.children.append(ROUTE1164)
ROUTE1165 = x3d.ROUTE()
ROUTE1165.fromField = "touchTime"
ROUTE1165.fromNode = "Jump_Touch"
ROUTE1165.toField = "set_stopTime"
ROUTE1165.toNode = "RollTimer"

Scene34.children.append(ROUTE1165)
ROUTE1166 = x3d.ROUTE()
ROUTE1166.fromField = "touchTime"
ROUTE1166.fromNode = "Jump_Touch"
ROUTE1166.toField = "set_stopTime"
ROUTE1166.toNode = "WalkTimer"

Scene34.children.append(ROUTE1166)
ROUTE1167 = x3d.ROUTE()
ROUTE1167.fromField = "touchTime"
ROUTE1167.fromNode = "Jump_Touch"
ROUTE1167.toField = "set_stopTime"
ROUTE1167.toNode = "RunTimer"

Scene34.children.append(ROUTE1167)
ROUTE1168 = x3d.ROUTE()
ROUTE1168.fromField = "touchTime"
ROUTE1168.fromNode = "Jump_Touch"
ROUTE1168.toField = "set_stopTime"
ROUTE1168.toNode = "KickTimer"

Scene34.children.append(ROUTE1168)
ROUTE1169 = x3d.ROUTE()
ROUTE1169.fromField = "touchTime"
ROUTE1169.fromNode = "Jump_Touch"
ROUTE1169.toField = "set_stopTime"
ROUTE1169.toNode = "StopTimer"

Scene34.children.append(ROUTE1169)
ROUTE1170 = x3d.ROUTE()
ROUTE1170.fromField = "touchTime"
ROUTE1170.fromNode = "Jump_Touch"
ROUTE1170.toField = "set_startTime"
ROUTE1170.toNode = "JumpTimer"

Scene34.children.append(ROUTE1170)
ROUTE1171 = x3d.ROUTE()
ROUTE1171.fromField = "touchTime"
ROUTE1171.fromNode = "Kick_Touch"
ROUTE1171.toField = "set_stopTime"
ROUTE1171.toNode = "StandTimer"

Scene34.children.append(ROUTE1171)
ROUTE1172 = x3d.ROUTE()
ROUTE1172.fromField = "touchTime"
ROUTE1172.fromNode = "Kick_Touch"
ROUTE1172.toField = "set_stopTime"
ROUTE1172.toNode = "PitchTimer"

Scene34.children.append(ROUTE1172)
ROUTE1173 = x3d.ROUTE()
ROUTE1173.fromField = "touchTime"
ROUTE1173.fromNode = "Kick_Touch"
ROUTE1173.toField = "set_stopTime"
ROUTE1173.toNode = "YawTimer"

Scene34.children.append(ROUTE1173)
ROUTE1174 = x3d.ROUTE()
ROUTE1174.fromField = "touchTime"
ROUTE1174.fromNode = "Kick_Touch"
ROUTE1174.toField = "set_stopTime"
ROUTE1174.toNode = "RollTimer"

Scene34.children.append(ROUTE1174)
ROUTE1175 = x3d.ROUTE()
ROUTE1175.fromField = "touchTime"
ROUTE1175.fromNode = "Kick_Touch"
ROUTE1175.toField = "set_stopTime"
ROUTE1175.toNode = "WalkTimer"

Scene34.children.append(ROUTE1175)
ROUTE1176 = x3d.ROUTE()
ROUTE1176.fromField = "touchTime"
ROUTE1176.fromNode = "Kick_Touch"
ROUTE1176.toField = "set_stopTime"
ROUTE1176.toNode = "RunTimer"

Scene34.children.append(ROUTE1176)
ROUTE1177 = x3d.ROUTE()
ROUTE1177.fromField = "touchTime"
ROUTE1177.fromNode = "Kick_Touch"
ROUTE1177.toField = "set_stopTime"
ROUTE1177.toNode = "JumpTimer"

Scene34.children.append(ROUTE1177)
ROUTE1178 = x3d.ROUTE()
ROUTE1178.fromField = "touchTime"
ROUTE1178.fromNode = "Kick_Touch"
ROUTE1178.toField = "set_stopTime"
ROUTE1178.toNode = "StopTimer"

Scene34.children.append(ROUTE1178)
ROUTE1179 = x3d.ROUTE()
ROUTE1179.fromField = "touchTime"
ROUTE1179.fromNode = "Kick_Touch"
ROUTE1179.toField = "set_startTime"
ROUTE1179.toNode = "KickTimer"

Scene34.children.append(ROUTE1179)
ROUTE1180 = x3d.ROUTE()
ROUTE1180.fromField = "touchTime"
ROUTE1180.fromNode = "Stop_Touch"
ROUTE1180.toField = "set_stopTime"
ROUTE1180.toNode = "StandTimer"

Scene34.children.append(ROUTE1180)
ROUTE1181 = x3d.ROUTE()
ROUTE1181.fromField = "touchTime"
ROUTE1181.fromNode = "Stop_Touch"
ROUTE1181.toField = "set_stopTime"
ROUTE1181.toNode = "PitchTimer"

Scene34.children.append(ROUTE1181)
ROUTE1182 = x3d.ROUTE()
ROUTE1182.fromField = "touchTime"
ROUTE1182.fromNode = "Stop_Touch"
ROUTE1182.toField = "set_stopTime"
ROUTE1182.toNode = "YawTimer"

Scene34.children.append(ROUTE1182)
ROUTE1183 = x3d.ROUTE()
ROUTE1183.fromField = "touchTime"
ROUTE1183.fromNode = "Stop_Touch"
ROUTE1183.toField = "set_stopTime"
ROUTE1183.toNode = "RollTimer"

Scene34.children.append(ROUTE1183)
ROUTE1184 = x3d.ROUTE()
ROUTE1184.fromField = "touchTime"
ROUTE1184.fromNode = "Stop_Touch"
ROUTE1184.toField = "set_stopTime"
ROUTE1184.toNode = "WalkTimer"

Scene34.children.append(ROUTE1184)
ROUTE1185 = x3d.ROUTE()
ROUTE1185.fromField = "touchTime"
ROUTE1185.fromNode = "Stop_Touch"
ROUTE1185.toField = "set_stopTime"
ROUTE1185.toNode = "RunTimer"

Scene34.children.append(ROUTE1185)
ROUTE1186 = x3d.ROUTE()
ROUTE1186.fromField = "touchTime"
ROUTE1186.fromNode = "Stop_Touch"
ROUTE1186.toField = "set_stopTime"
ROUTE1186.toNode = "JumpTimer"

Scene34.children.append(ROUTE1186)
ROUTE1187 = x3d.ROUTE()
ROUTE1187.fromField = "touchTime"
ROUTE1187.fromNode = "Stop_Touch"
ROUTE1187.toField = "set_stopTime"
ROUTE1187.toNode = "KickTimer"

Scene34.children.append(ROUTE1187)
ROUTE1188 = x3d.ROUTE()
ROUTE1188.fromField = "touchTime"
ROUTE1188.fromNode = "Stop_Touch"
ROUTE1188.toField = "set_startTime"
ROUTE1188.toNode = "StopTimer"

Scene34.children.append(ROUTE1188)

X3D0.Scene = Scene34
f = open("././BoxMan4AnimationPanel_RoundTrip.x3d", "w")
f.write(X3D0.XML())
f.close()
