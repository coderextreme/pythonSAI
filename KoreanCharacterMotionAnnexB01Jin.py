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
meta3.content = "KoreanCharacterAnnexB01Jin.x3d"

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.name = "creator"
meta4.content = "Jin Hoon Lee and Min Joo Lee"

head1.children.append(meta4)
meta5 = x3d.meta()
meta5.name = "translator"
meta5.content = "Chul Hee Jung and Myeong Won Lee"

head1.children.append(meta5)
meta6 = x3d.meta()
meta6.name = "created"
meta6.content = "31 March 2011"

head1.children.append(meta6)
meta7 = x3d.meta()
meta7.name = "translated"
meta7.content = "1 November 2014"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.name = "modified"
meta8.content = "8 January 2023"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "description"
meta9.content = "Articulated 3D game character designed with a general graphics tool, then converted into an X3D HAnim model."

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "reference"
meta10.content = "KoreanCharacter00ReadMe.txt"

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.name = "reference"
meta11.content = "KoreanCharacterHumanMotion_Infotech2014_140706.pdf"

head1.children.append(meta11)
meta12 = x3d.meta()
meta12.name = "reference"
meta12.content = "KoreanCharactersIllustrated.pdf"

head1.children.append(meta12)
meta13 = x3d.meta()
meta13.name = "specificationSection"
meta13.content = "HAnim 2.0 Part 2: Humanoid animation (HAnim) motion data animation, Annex D (informative) Examples of HAnim motion data animation using a Motion object"

head1.children.append(meta13)
meta14 = x3d.meta()
meta14.name = "specificationUrl"
meta14.content = "https://www.web3d.org/documents/specifications/19774/V2.0/MotionDataAnimation/ExampleKeyframeAnimation.html"

head1.children.append(meta14)
meta15 = x3d.meta()
meta15.name = "identifier"
meta15.content = "https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Specifications/KoreanCharacterAnnexB01Jin.x3d"

head1.children.append(meta15)
meta16 = x3d.meta()
meta16.name = "generator"
meta16.content = "3DS MAX, http://www.autodesk.com/products/autodesk-3ds-max/overview"

head1.children.append(meta16)
meta17 = x3d.meta()
meta17.name = "generator"
meta17.content = "Suwon HAnim Converter"

head1.children.append(meta17)
meta18 = x3d.meta()
meta18.name = "generator"
meta18.content = "Gnu Image Manipulation Program, http://www.gimp.org"

head1.children.append(meta18)
meta19 = x3d.meta()
meta19.name = "generator"
meta19.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"

head1.children.append(meta19)
meta20 = x3d.meta()
meta20.name = "license"
meta20.content = "../license.html"

head1.children.append(meta20)

X3D0.head = head1
Scene21 = x3d.Scene()
NavigationInfo22 = x3d.NavigationInfo()
NavigationInfo22.speed = 1.5

Scene21.children.append(NavigationInfo22)
Viewpoint23 = x3d.Viewpoint()
Viewpoint23.centerOfRotation = [0,1,0]
Viewpoint23.description = "AnnexB01Jin"
Viewpoint23.position = [0,1,3]

Scene21.children.append(Viewpoint23)
Group24 = x3d.Group()
Group24.DEF = "KeyframeAnimation"
TimeSensor25 = x3d.TimeSensor()
TimeSensor25.DEF = "KeyframeTimer"
TimeSensor25.cycleInterval = 8.033494
TimeSensor25.loop = True

Group24.children.append(TimeSensor25)
PositionInterpolator26 = x3d.PositionInterpolator()
PositionInterpolator26.DEF = "Keyframe_HumanoidRoot"
PositionInterpolator26.key = [0,1]
PositionInterpolator26.keyValue = (0.0000,0.0000,0.0000,0.0000,0.0000,0.0000)

Group24.children.append(PositionInterpolator26)
OrientationInterpolator27 = x3d.OrientationInterpolator()
OrientationInterpolator27.DEF = "Keyframe_HumanoidRoot"
OrientationInterpolator27.key = [0,1]
OrientationInterpolator27.keyValue = (0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000)

Group24.children.append(OrientationInterpolator27)
OrientationInterpolator28 = x3d.OrientationInterpolator()
OrientationInterpolator28.DEF = "Keyframe_sacroiliac"
OrientationInterpolator28.key = [0,1]
OrientationInterpolator28.keyValue = (0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000)

Group24.children.append(OrientationInterpolator28)
OrientationInterpolator29 = x3d.OrientationInterpolator()
OrientationInterpolator29.DEF = "Keyframe_l_shoulder"
OrientationInterpolator29.key = [0,0.5,1]
OrientationInterpolator29.keyValue = (0.0000,0.0000,0.0000,0.0000,-1.0000,0.0000,0.0000,3.0000,0.0000,0.0000,0.0000,0.0000)

Group24.children.append(OrientationInterpolator29)
OrientationInterpolator30 = x3d.OrientationInterpolator()
OrientationInterpolator30.DEF = "Keyframe_l_elbow"
OrientationInterpolator30.key = [0,1]
OrientationInterpolator30.keyValue = (0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000)

Group24.children.append(OrientationInterpolator30)
OrientationInterpolator31 = x3d.OrientationInterpolator()
OrientationInterpolator31.DEF = "Keyframe_l_radiocarpal"
OrientationInterpolator31.key = [0,1]
OrientationInterpolator31.keyValue = (0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000)

Group24.children.append(OrientationInterpolator31)
OrientationInterpolator32 = x3d.OrientationInterpolator()
OrientationInterpolator32.DEF = "Keyframe_r_shoulder"
OrientationInterpolator32.key = [0,0.5,1]
OrientationInterpolator32.keyValue = (0.0000,0.0000,0.0000,0.0000,-1.0000,0.0000,0.0000,3.0000,0.0000,0.0000,0.0000,0.0000)

Group24.children.append(OrientationInterpolator32)
OrientationInterpolator33 = x3d.OrientationInterpolator()
OrientationInterpolator33.DEF = "Keyframe_r_elbow"
OrientationInterpolator33.key = [0,1]
OrientationInterpolator33.keyValue = (0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000)

Group24.children.append(OrientationInterpolator33)
OrientationInterpolator34 = x3d.OrientationInterpolator()
OrientationInterpolator34.DEF = "Keyframe_r_radiocarpal"
OrientationInterpolator34.key = [0,1]
OrientationInterpolator34.keyValue = (0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000)

Group24.children.append(OrientationInterpolator34)
OrientationInterpolator35 = x3d.OrientationInterpolator()
OrientationInterpolator35.DEF = "Keyframe_vl5"
OrientationInterpolator35.key = [0,1]
OrientationInterpolator35.keyValue = (0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000)

Group24.children.append(OrientationInterpolator35)
OrientationInterpolator36 = x3d.OrientationInterpolator()
OrientationInterpolator36.DEF = "Keyframe_skullbase"
OrientationInterpolator36.key = [0,1]
OrientationInterpolator36.keyValue = (0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000)

Group24.children.append(OrientationInterpolator36)
OrientationInterpolator37 = x3d.OrientationInterpolator()
OrientationInterpolator37.DEF = "Keyframe_l_hip"
OrientationInterpolator37.key = [0,1]
OrientationInterpolator37.keyValue = (0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000)

Group24.children.append(OrientationInterpolator37)
OrientationInterpolator38 = x3d.OrientationInterpolator()
OrientationInterpolator38.DEF = "Keyframe_l_knee"
OrientationInterpolator38.key = [0,1]
OrientationInterpolator38.keyValue = (0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000)

Group24.children.append(OrientationInterpolator38)
OrientationInterpolator39 = x3d.OrientationInterpolator()
OrientationInterpolator39.DEF = "Keyframe_l_talocrural"
OrientationInterpolator39.key = [0,1]
OrientationInterpolator39.keyValue = (0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000)

Group24.children.append(OrientationInterpolator39)
OrientationInterpolator40 = x3d.OrientationInterpolator()
OrientationInterpolator40.DEF = "Keyframe_l_metatarsophalangeal"
OrientationInterpolator40.key = [0,1]
OrientationInterpolator40.keyValue = (0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000)

Group24.children.append(OrientationInterpolator40)
OrientationInterpolator41 = x3d.OrientationInterpolator()
OrientationInterpolator41.DEF = "Keyframe_r_hip"
OrientationInterpolator41.key = [0,1]
OrientationInterpolator41.keyValue = (0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000)

Group24.children.append(OrientationInterpolator41)
OrientationInterpolator42 = x3d.OrientationInterpolator()
OrientationInterpolator42.DEF = "Keyframe_r_knee"
OrientationInterpolator42.key = [0,1]
OrientationInterpolator42.keyValue = (0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000)

Group24.children.append(OrientationInterpolator42)
OrientationInterpolator43 = x3d.OrientationInterpolator()
OrientationInterpolator43.DEF = "Keyframe_r_talocrural"
OrientationInterpolator43.key = [0,1]
OrientationInterpolator43.keyValue = (0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000)

Group24.children.append(OrientationInterpolator43)
OrientationInterpolator44 = x3d.OrientationInterpolator()
OrientationInterpolator44.DEF = "Keyframe_r_metatarsophalangeal"
OrientationInterpolator44.key = [0,1]
OrientationInterpolator44.keyValue = (0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000)

Group24.children.append(OrientationInterpolator44)
ROUTE45 = x3d.ROUTE()
ROUTE45.fromField = "fraction_changed"
ROUTE45.fromNode = "KeyframeTimer"
ROUTE45.toField = "set_fraction"
ROUTE45.toNode = "Keyframe_HumanoidRoot"

Group24.children.append(ROUTE45)
ROUTE46 = x3d.ROUTE()
ROUTE46.fromField = "fraction_changed"
ROUTE46.fromNode = "KeyframeTimer"
ROUTE46.toField = "set_fraction"
ROUTE46.toNode = "Keyframe_HumanoidRoot"

Group24.children.append(ROUTE46)
ROUTE47 = x3d.ROUTE()
ROUTE47.fromField = "fraction_changed"
ROUTE47.fromNode = "KeyframeTimer"
ROUTE47.toField = "set_fraction"
ROUTE47.toNode = "Keyframe_sacroiliac"

Group24.children.append(ROUTE47)
ROUTE48 = x3d.ROUTE()
ROUTE48.fromField = "fraction_changed"
ROUTE48.fromNode = "KeyframeTimer"
ROUTE48.toField = "set_fraction"
ROUTE48.toNode = "Keyframe_l_shoulder"

Group24.children.append(ROUTE48)
ROUTE49 = x3d.ROUTE()
ROUTE49.fromField = "fraction_changed"
ROUTE49.fromNode = "KeyframeTimer"
ROUTE49.toField = "set_fraction"
ROUTE49.toNode = "Keyframe_l_elbow"

Group24.children.append(ROUTE49)
ROUTE50 = x3d.ROUTE()
ROUTE50.fromField = "fraction_changed"
ROUTE50.fromNode = "KeyframeTimer"
ROUTE50.toField = "set_fraction"
ROUTE50.toNode = "Keyframe_l_radiocarpal"

Group24.children.append(ROUTE50)
ROUTE51 = x3d.ROUTE()
ROUTE51.fromField = "fraction_changed"
ROUTE51.fromNode = "KeyframeTimer"
ROUTE51.toField = "set_fraction"
ROUTE51.toNode = "Keyframe_r_shoulder"

Group24.children.append(ROUTE51)
ROUTE52 = x3d.ROUTE()
ROUTE52.fromField = "fraction_changed"
ROUTE52.fromNode = "KeyframeTimer"
ROUTE52.toField = "set_fraction"
ROUTE52.toNode = "Keyframe_r_elbow"

Group24.children.append(ROUTE52)
ROUTE53 = x3d.ROUTE()
ROUTE53.fromField = "fraction_changed"
ROUTE53.fromNode = "KeyframeTimer"
ROUTE53.toField = "set_fraction"
ROUTE53.toNode = "Keyframe_r_radiocarpal"

Group24.children.append(ROUTE53)
ROUTE54 = x3d.ROUTE()
ROUTE54.fromField = "fraction_changed"
ROUTE54.fromNode = "KeyframeTimer"
ROUTE54.toField = "set_fraction"
ROUTE54.toNode = "Keyframe_vl5"

Group24.children.append(ROUTE54)
ROUTE55 = x3d.ROUTE()
ROUTE55.fromField = "fraction_changed"
ROUTE55.fromNode = "KeyframeTimer"
ROUTE55.toField = "set_fraction"
ROUTE55.toNode = "Keyframe_skullbase"

Group24.children.append(ROUTE55)
ROUTE56 = x3d.ROUTE()
ROUTE56.fromField = "fraction_changed"
ROUTE56.fromNode = "KeyframeTimer"
ROUTE56.toField = "set_fraction"
ROUTE56.toNode = "Keyframe_l_hip"

Group24.children.append(ROUTE56)
ROUTE57 = x3d.ROUTE()
ROUTE57.fromField = "fraction_changed"
ROUTE57.fromNode = "KeyframeTimer"
ROUTE57.toField = "set_fraction"
ROUTE57.toNode = "Keyframe_l_knee"

Group24.children.append(ROUTE57)
ROUTE58 = x3d.ROUTE()
ROUTE58.fromField = "fraction_changed"
ROUTE58.fromNode = "KeyframeTimer"
ROUTE58.toField = "set_fraction"
ROUTE58.toNode = "Keyframe_l_talocrural"

Group24.children.append(ROUTE58)
ROUTE59 = x3d.ROUTE()
ROUTE59.fromField = "fraction_changed"
ROUTE59.fromNode = "KeyframeTimer"
ROUTE59.toField = "set_fraction"
ROUTE59.toNode = "Keyframe_l_metatarsophalangeal"

Group24.children.append(ROUTE59)
ROUTE60 = x3d.ROUTE()
ROUTE60.fromField = "fraction_changed"
ROUTE60.fromNode = "KeyframeTimer"
ROUTE60.toField = "set_fraction"
ROUTE60.toNode = "Keyframe_r_hip"

Group24.children.append(ROUTE60)
ROUTE61 = x3d.ROUTE()
ROUTE61.fromField = "fraction_changed"
ROUTE61.fromNode = "KeyframeTimer"
ROUTE61.toField = "set_fraction"
ROUTE61.toNode = "Keyframe_r_knee"

Group24.children.append(ROUTE61)
ROUTE62 = x3d.ROUTE()
ROUTE62.fromField = "fraction_changed"
ROUTE62.fromNode = "KeyframeTimer"
ROUTE62.toField = "set_fraction"
ROUTE62.toNode = "Keyframe_r_talocrural"

Group24.children.append(ROUTE62)
ROUTE63 = x3d.ROUTE()
ROUTE63.fromField = "fraction_changed"
ROUTE63.fromNode = "KeyframeTimer"
ROUTE63.toField = "set_fraction"
ROUTE63.toNode = "Keyframe_r_metatarsophalangeal"

Group24.children.append(ROUTE63)
ROUTE64 = x3d.ROUTE()
ROUTE64.fromField = "value_changed"
ROUTE64.fromNode = "Keyframe_HumanoidRoot"
ROUTE64.toField = "translation"
ROUTE64.toNode = "hanim_HumanoidRoot"

Group24.children.append(ROUTE64)
ROUTE65 = x3d.ROUTE()
ROUTE65.fromField = "value_changed"
ROUTE65.fromNode = "Keyframe_HumanoidRoot"
ROUTE65.toField = "rotation"
ROUTE65.toNode = "hanim_HumanoidRoot"

Group24.children.append(ROUTE65)
ROUTE66 = x3d.ROUTE()
ROUTE66.fromField = "value_changed"
ROUTE66.fromNode = "Keyframe_sacroiliac"
ROUTE66.toField = "rotation"
ROUTE66.toNode = "hanim_sacroiliac"

Group24.children.append(ROUTE66)
ROUTE67 = x3d.ROUTE()
ROUTE67.fromField = "value_changed"
ROUTE67.fromNode = "Keyframe_l_shoulder"
ROUTE67.toField = "rotation"
ROUTE67.toNode = "hanim_l_shoulder"

Group24.children.append(ROUTE67)
ROUTE68 = x3d.ROUTE()
ROUTE68.fromField = "value_changed"
ROUTE68.fromNode = "Keyframe_l_elbow"
ROUTE68.toField = "rotation"
ROUTE68.toNode = "hanim_l_elbow"

Group24.children.append(ROUTE68)
ROUTE69 = x3d.ROUTE()
ROUTE69.fromField = "value_changed"
ROUTE69.fromNode = "Keyframe_l_radiocarpal"
ROUTE69.toField = "rotation"
ROUTE69.toNode = "hanim_l_radiocarpal"

Group24.children.append(ROUTE69)
ROUTE70 = x3d.ROUTE()
ROUTE70.fromField = "value_changed"
ROUTE70.fromNode = "Keyframe_r_shoulder"
ROUTE70.toField = "rotation"
ROUTE70.toNode = "hanim_r_shoulder"

Group24.children.append(ROUTE70)
ROUTE71 = x3d.ROUTE()
ROUTE71.fromField = "value_changed"
ROUTE71.fromNode = "Keyframe_r_elbow"
ROUTE71.toField = "rotation"
ROUTE71.toNode = "hanim_r_elbow"

Group24.children.append(ROUTE71)
ROUTE72 = x3d.ROUTE()
ROUTE72.fromField = "value_changed"
ROUTE72.fromNode = "Keyframe_r_radiocarpal"
ROUTE72.toField = "rotation"
ROUTE72.toNode = "hanim_r_radiocarpal"

Group24.children.append(ROUTE72)
ROUTE73 = x3d.ROUTE()
ROUTE73.fromField = "value_changed"
ROUTE73.fromNode = "Keyframe_vl5"
ROUTE73.toField = "rotation"
ROUTE73.toNode = "hanim_vl5"

Group24.children.append(ROUTE73)
ROUTE74 = x3d.ROUTE()
ROUTE74.fromField = "value_changed"
ROUTE74.fromNode = "Keyframe_skullbase"
ROUTE74.toField = "rotation"
ROUTE74.toNode = "hanim_skullbase"

Group24.children.append(ROUTE74)
ROUTE75 = x3d.ROUTE()
ROUTE75.fromField = "value_changed"
ROUTE75.fromNode = "Keyframe_l_hip"
ROUTE75.toField = "rotation"
ROUTE75.toNode = "hanim_l_hip"

Group24.children.append(ROUTE75)
ROUTE76 = x3d.ROUTE()
ROUTE76.fromField = "value_changed"
ROUTE76.fromNode = "Keyframe_l_knee"
ROUTE76.toField = "rotation"
ROUTE76.toNode = "hanim_l_knee"

Group24.children.append(ROUTE76)
ROUTE77 = x3d.ROUTE()
ROUTE77.fromField = "value_changed"
ROUTE77.fromNode = "Keyframe_l_talocrural"
ROUTE77.toField = "rotation"
ROUTE77.toNode = "hanim_l_talocrural"

Group24.children.append(ROUTE77)
ROUTE78 = x3d.ROUTE()
ROUTE78.fromField = "value_changed"
ROUTE78.fromNode = "Keyframe_l_talocrural"
ROUTE78.toField = "rotation"
ROUTE78.toNode = "hanim_l_metatarsophalangeal"

Group24.children.append(ROUTE78)
ROUTE79 = x3d.ROUTE()
ROUTE79.fromField = "value_changed"
ROUTE79.fromNode = "Keyframe_r_hip"
ROUTE79.toField = "rotation"
ROUTE79.toNode = "hanim_r_hip"

Group24.children.append(ROUTE79)
ROUTE80 = x3d.ROUTE()
ROUTE80.fromField = "value_changed"
ROUTE80.fromNode = "Keyframe_r_knee"
ROUTE80.toField = "rotation"
ROUTE80.toNode = "hanim_r_knee"

Group24.children.append(ROUTE80)
ROUTE81 = x3d.ROUTE()
ROUTE81.fromField = "value_changed"
ROUTE81.fromNode = "Keyframe_l_talocrural"
ROUTE81.toField = "rotation"
ROUTE81.toNode = "hanim_r_talocrural"

Group24.children.append(ROUTE81)
ROUTE82 = x3d.ROUTE()
ROUTE82.fromField = "value_changed"
ROUTE82.fromNode = "Keyframe_l_talocrural"
ROUTE82.toField = "rotation"
ROUTE82.toNode = "hanim_r_metatarsophalangeal"

Group24.children.append(ROUTE82)

Scene21.children.append(Group24)

X3D0.Scene = Scene21
f = open("././KoreanCharacterMotionAnnexB01Jin_RoundTrip.x3d", "w")
f.write(X3D0.XML())
f.close()
