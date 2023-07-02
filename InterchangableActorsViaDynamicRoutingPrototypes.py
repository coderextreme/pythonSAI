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
meta3.content = "InterchangableActorsViaDynamicRoutingPrototypes.x3d"

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.name = "description"
meta4.content = "This example demonstrates interchangeability of avatars (Nancy, Allen, Boxman) and animation behaviors (Stand, Run, Jump, Walk) via dynamic routing."

head1.children.append(meta4)
meta5 = x3d.meta()
meta5.name = "warning"
meta5.content = "this example needs to be converted from HAnim Prototypes to HAnim native tags."

head1.children.append(meta5)
meta6 = x3d.meta()
meta6.name = "creator"
meta6.content = "Ozan APAYDIN"

head1.children.append(meta6)
meta7 = x3d.meta()
meta7.name = "translator"
meta7.content = "Ozan APAYDIN"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.name = "created"
meta8.content = "15 November 2001"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "modified"
meta9.content = "9 July 2020"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "TODO"
meta10.content = "replace usages of original Boxman .wrl fragments, fix numerous warnings"

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.name = "TODO"
meta11.content = "Inconsistent validation problem with HAnimJoint, ProtoInstance USE nodes: required @name attribute must also be present"

head1.children.append(meta11)
meta12 = x3d.meta()
meta12.name = "reference"
meta12.content = "http://www.movesinstitute.org/Theses/ApaydinThesis.pdf"

head1.children.append(meta12)
meta13 = x3d.meta()
meta13.name = "MovingImage"
meta13.content = "VoiceActivated/ApaydinOzanThesisPresentation.ppt"

head1.children.append(meta13)
meta14 = x3d.meta()
meta14.name = "MovingImage"
meta14.content = "https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/VoiceActivated/ApaydinOzanThesisFinalVideo.mpg"

head1.children.append(meta14)
meta15 = x3d.meta()
meta15.name = "MovingImage"
meta15.content = "https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/VoiceActivated/NancyVUI.wmv"

head1.children.append(meta15)
meta16 = x3d.meta()
meta16.name = "reference"
meta16.content = "http://HAnim.org/Models/HAnim2001/boxman/boxman.wrl"

head1.children.append(meta16)
meta17 = x3d.meta()
meta17.name = "reference"
meta17.content = "http://HAnim.org/Specifications/HAnim2001"

head1.children.append(meta17)
meta18 = x3d.meta()
meta18.name = "reference"
meta18.content = "http://www.HAnim.org"

head1.children.append(meta18)
meta19 = x3d.meta()
meta19.name = "reference"
meta19.content = "http://HAnim.org/Models"

head1.children.append(meta19)
meta20 = x3d.meta()
meta20.name = "reference"
meta20.content = "http://HAnim.org/Specifications"

head1.children.append(meta20)
meta21 = x3d.meta()
meta21.name = "identifier"
meta21.content = "https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Prototypes/InterchangableActorsViaDynamicRoutingPrototypes.x3d"

head1.children.append(meta21)
meta22 = x3d.meta()
meta22.name = "generator"
meta22.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"

head1.children.append(meta22)
meta23 = x3d.meta()
meta23.name = "license"
meta23.content = "../license.html"

head1.children.append(meta23)

X3D0.head = head1
Scene24 = x3d.Scene()
#************Behavior Prototypes***************
ExternProtoDeclare25 = x3d.ExternProtoDeclare()
ExternProtoDeclare25.name = "LOA1_StandAnimation"
ExternProtoDeclare25.url = ["LOA1_StandAnimation.x3d#LOA1_StandAnimation","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/LOA1_StandAnimation.x3d#LOA1_StandAnimation","LOA1_StandAnimation.wrl#LOA1_StandAnimation","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/LOA1_StandAnimation.wrl#LOA1_StandAnimation"]
field26 = x3d.field()
field26.name = "cycleInterval"
field26.accessType = "inputOutput"
field26.type = "SFTime"

ExternProtoDeclare25.field.append(field26)
field27 = x3d.field()
field27.name = "enabled"
field27.accessType = "inputOutput"
field27.type = "SFBool"

ExternProtoDeclare25.field.append(field27)
field28 = x3d.field()
field28.name = "loop"
field28.accessType = "inputOutput"
field28.type = "SFBool"

ExternProtoDeclare25.field.append(field28)
field29 = x3d.field()
field29.name = "startTime"
field29.accessType = "inputOutput"
field29.type = "SFTime"

ExternProtoDeclare25.field.append(field29)
field30 = x3d.field()
field30.name = "stopTime"
field30.accessType = "inputOutput"
field30.type = "SFTime"

ExternProtoDeclare25.field.append(field30)
field31 = x3d.field()
field31.name = "fraction_changed"
field31.accessType = "outputOnly"
field31.type = "SFFloat"

ExternProtoDeclare25.field.append(field31)
field32 = x3d.field()
field32.name = "humanoid_root_translation_changed"
field32.accessType = "outputOnly"
field32.type = "SFVec3f"

ExternProtoDeclare25.field.append(field32)
field33 = x3d.field()
field33.name = "humanoid_root_rotation_changed"
field33.accessType = "outputOnly"
field33.type = "SFRotation"

ExternProtoDeclare25.field.append(field33)
field34 = x3d.field()
field34.name = "lower_body_rotation_changed"
field34.accessType = "outputOnly"
field34.type = "SFRotation"

ExternProtoDeclare25.field.append(field34)
field35 = x3d.field()
field35.name = "l_hip_rotation_changed"
field35.accessType = "outputOnly"
field35.type = "SFRotation"

ExternProtoDeclare25.field.append(field35)
field36 = x3d.field()
field36.name = "l_knee_rotation_changed"
field36.accessType = "outputOnly"
field36.type = "SFRotation"

ExternProtoDeclare25.field.append(field36)
field37 = x3d.field()
field37.name = "l_ankle_rotation_changed"
field37.accessType = "outputOnly"
field37.type = "SFRotation"

ExternProtoDeclare25.field.append(field37)
field38 = x3d.field()
field38.name = "l_midtarsal_rotation_changed"
field38.accessType = "outputOnly"
field38.type = "SFRotation"

ExternProtoDeclare25.field.append(field38)
field39 = x3d.field()
field39.name = "r_hip_rotation_changed"
field39.accessType = "outputOnly"
field39.type = "SFRotation"

ExternProtoDeclare25.field.append(field39)
field40 = x3d.field()
field40.name = "r_knee_rotation_changed"
field40.accessType = "outputOnly"
field40.type = "SFRotation"

ExternProtoDeclare25.field.append(field40)
field41 = x3d.field()
field41.name = "r_ankle_rotation_changed"
field41.accessType = "outputOnly"
field41.type = "SFRotation"

ExternProtoDeclare25.field.append(field41)
field42 = x3d.field()
field42.name = "r_midtarsal_rotation_changed"
field42.accessType = "outputOnly"
field42.type = "SFRotation"

ExternProtoDeclare25.field.append(field42)
field43 = x3d.field()
field43.name = "vl5_rotation_changed"
field43.accessType = "outputOnly"
field43.type = "SFRotation"

ExternProtoDeclare25.field.append(field43)
field44 = x3d.field()
field44.name = "skullbase_rotation_changed"
field44.accessType = "outputOnly"
field44.type = "SFRotation"

ExternProtoDeclare25.field.append(field44)
field45 = x3d.field()
field45.name = "l_shoulder_rotation_changed"
field45.accessType = "outputOnly"
field45.type = "SFRotation"

ExternProtoDeclare25.field.append(field45)
field46 = x3d.field()
field46.name = "l_elbow_rotation_changed"
field46.accessType = "outputOnly"
field46.type = "SFRotation"

ExternProtoDeclare25.field.append(field46)
field47 = x3d.field()
field47.name = "l_wrist_rotation_changed"
field47.accessType = "outputOnly"
field47.type = "SFRotation"

ExternProtoDeclare25.field.append(field47)
field48 = x3d.field()
field48.name = "r_shoulder_rotation_changed"
field48.accessType = "outputOnly"
field48.type = "SFRotation"

ExternProtoDeclare25.field.append(field48)
field49 = x3d.field()
field49.name = "r_elbow_rotation_changed"
field49.accessType = "outputOnly"
field49.type = "SFRotation"

ExternProtoDeclare25.field.append(field49)
field50 = x3d.field()
field50.name = "r_wrist_rotation_changed"
field50.accessType = "outputOnly"
field50.type = "SFRotation"

ExternProtoDeclare25.field.append(field50)
field51 = x3d.field()
field51.name = "isActive"
field51.accessType = "outputOnly"
field51.type = "SFBool"

ExternProtoDeclare25.field.append(field51)

Scene24.children.append(ExternProtoDeclare25)
ExternProtoDeclare52 = x3d.ExternProtoDeclare()
ExternProtoDeclare52.name = "LOA1_WalkAnimation"
ExternProtoDeclare52.url = ["LOA1_WalkAnimation.x3d#LOA1_WalkAnimation","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/LOA1_WalkAnimation.x3d#LOA1_WalkAnimation","LOA1_WalkAnimation.wrl#LOA1_WalkAnimation","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/LOA1_WalkAnimation.wrl#LOA1_WalkAnimation"]
field53 = x3d.field()
field53.name = "cycleInterval"
field53.accessType = "inputOutput"
field53.type = "SFTime"

ExternProtoDeclare52.field.append(field53)
field54 = x3d.field()
field54.name = "enabled"
field54.accessType = "inputOutput"
field54.type = "SFBool"

ExternProtoDeclare52.field.append(field54)
field55 = x3d.field()
field55.name = "loop"
field55.accessType = "inputOutput"
field55.type = "SFBool"

ExternProtoDeclare52.field.append(field55)
field56 = x3d.field()
field56.name = "startTime"
field56.accessType = "inputOutput"
field56.type = "SFTime"

ExternProtoDeclare52.field.append(field56)
field57 = x3d.field()
field57.name = "stopTime"
field57.accessType = "inputOutput"
field57.type = "SFTime"

ExternProtoDeclare52.field.append(field57)
field58 = x3d.field()
field58.name = "fraction_changed"
field58.accessType = "outputOnly"
field58.type = "SFFloat"

ExternProtoDeclare52.field.append(field58)
field59 = x3d.field()
field59.name = "humanoid_root_translation_changed"
field59.accessType = "outputOnly"
field59.type = "SFVec3f"

ExternProtoDeclare52.field.append(field59)
field60 = x3d.field()
field60.name = "humanoid_root_rotation_changed"
field60.accessType = "outputOnly"
field60.type = "SFRotation"

ExternProtoDeclare52.field.append(field60)
field61 = x3d.field()
field61.name = "lower_body_rotation_changed"
field61.accessType = "outputOnly"
field61.type = "SFRotation"

ExternProtoDeclare52.field.append(field61)
field62 = x3d.field()
field62.name = "l_hip_rotation_changed"
field62.accessType = "outputOnly"
field62.type = "SFRotation"

ExternProtoDeclare52.field.append(field62)
field63 = x3d.field()
field63.name = "l_knee_rotation_changed"
field63.accessType = "outputOnly"
field63.type = "SFRotation"

ExternProtoDeclare52.field.append(field63)
field64 = x3d.field()
field64.name = "l_ankle_rotation_changed"
field64.accessType = "outputOnly"
field64.type = "SFRotation"

ExternProtoDeclare52.field.append(field64)
field65 = x3d.field()
field65.name = "l_midtarsal_rotation_changed"
field65.accessType = "outputOnly"
field65.type = "SFRotation"

ExternProtoDeclare52.field.append(field65)
field66 = x3d.field()
field66.name = "r_hip_rotation_changed"
field66.accessType = "outputOnly"
field66.type = "SFRotation"

ExternProtoDeclare52.field.append(field66)
field67 = x3d.field()
field67.name = "r_knee_rotation_changed"
field67.accessType = "outputOnly"
field67.type = "SFRotation"

ExternProtoDeclare52.field.append(field67)
field68 = x3d.field()
field68.name = "r_ankle_rotation_changed"
field68.accessType = "outputOnly"
field68.type = "SFRotation"

ExternProtoDeclare52.field.append(field68)
field69 = x3d.field()
field69.name = "r_midtarsal_rotation_changed"
field69.accessType = "outputOnly"
field69.type = "SFRotation"

ExternProtoDeclare52.field.append(field69)
field70 = x3d.field()
field70.name = "vl5_rotation_changed"
field70.accessType = "outputOnly"
field70.type = "SFRotation"

ExternProtoDeclare52.field.append(field70)
field71 = x3d.field()
field71.name = "skullbase_rotation_changed"
field71.accessType = "outputOnly"
field71.type = "SFRotation"

ExternProtoDeclare52.field.append(field71)
field72 = x3d.field()
field72.name = "l_shoulder_rotation_changed"
field72.accessType = "outputOnly"
field72.type = "SFRotation"

ExternProtoDeclare52.field.append(field72)
field73 = x3d.field()
field73.name = "l_elbow_rotation_changed"
field73.accessType = "outputOnly"
field73.type = "SFRotation"

ExternProtoDeclare52.field.append(field73)
field74 = x3d.field()
field74.name = "l_wrist_rotation_changed"
field74.accessType = "outputOnly"
field74.type = "SFRotation"

ExternProtoDeclare52.field.append(field74)
field75 = x3d.field()
field75.name = "r_shoulder_rotation_changed"
field75.accessType = "outputOnly"
field75.type = "SFRotation"

ExternProtoDeclare52.field.append(field75)
field76 = x3d.field()
field76.name = "r_elbow_rotation_changed"
field76.accessType = "outputOnly"
field76.type = "SFRotation"

ExternProtoDeclare52.field.append(field76)
field77 = x3d.field()
field77.name = "r_wrist_rotation_changed"
field77.accessType = "outputOnly"
field77.type = "SFRotation"

ExternProtoDeclare52.field.append(field77)
field78 = x3d.field()
field78.name = "isActive"
field78.accessType = "outputOnly"
field78.type = "SFBool"

ExternProtoDeclare52.field.append(field78)

Scene24.children.append(ExternProtoDeclare52)
ExternProtoDeclare79 = x3d.ExternProtoDeclare()
ExternProtoDeclare79.name = "LOA1_RunAnimation"
ExternProtoDeclare79.url = ["LOA1_RunAnimation.x3d#LOA1_RunAnimation","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/LOA1_RunAnimation.x3d#LOA1_RunAnimation","LOA1_RunAnimation.wrl#LOA1_RunAnimation","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/LOA1_RunAnimation.wrl#LOA1_RunAnimation"]
field80 = x3d.field()
field80.name = "cycleInterval"
field80.accessType = "inputOutput"
field80.type = "SFTime"

ExternProtoDeclare79.field.append(field80)
field81 = x3d.field()
field81.name = "enabled"
field81.accessType = "inputOutput"
field81.type = "SFBool"

ExternProtoDeclare79.field.append(field81)
field82 = x3d.field()
field82.name = "loop"
field82.accessType = "inputOutput"
field82.type = "SFBool"

ExternProtoDeclare79.field.append(field82)
field83 = x3d.field()
field83.name = "startTime"
field83.accessType = "inputOutput"
field83.type = "SFTime"

ExternProtoDeclare79.field.append(field83)
field84 = x3d.field()
field84.name = "stopTime"
field84.accessType = "inputOutput"
field84.type = "SFTime"

ExternProtoDeclare79.field.append(field84)
field85 = x3d.field()
field85.name = "fraction_changed"
field85.accessType = "outputOnly"
field85.type = "SFFloat"

ExternProtoDeclare79.field.append(field85)
field86 = x3d.field()
field86.name = "humanoid_root_translation_changed"
field86.accessType = "outputOnly"
field86.type = "SFVec3f"

ExternProtoDeclare79.field.append(field86)
field87 = x3d.field()
field87.name = "humanoid_root_rotation_changed"
field87.accessType = "outputOnly"
field87.type = "SFRotation"

ExternProtoDeclare79.field.append(field87)
field88 = x3d.field()
field88.name = "lower_body_rotation_changed"
field88.accessType = "outputOnly"
field88.type = "SFRotation"

ExternProtoDeclare79.field.append(field88)
field89 = x3d.field()
field89.name = "l_hip_rotation_changed"
field89.accessType = "outputOnly"
field89.type = "SFRotation"

ExternProtoDeclare79.field.append(field89)
field90 = x3d.field()
field90.name = "l_knee_rotation_changed"
field90.accessType = "outputOnly"
field90.type = "SFRotation"

ExternProtoDeclare79.field.append(field90)
field91 = x3d.field()
field91.name = "l_ankle_rotation_changed"
field91.accessType = "outputOnly"
field91.type = "SFRotation"

ExternProtoDeclare79.field.append(field91)
field92 = x3d.field()
field92.name = "l_midtarsal_rotation_changed"
field92.accessType = "outputOnly"
field92.type = "SFRotation"

ExternProtoDeclare79.field.append(field92)
field93 = x3d.field()
field93.name = "r_hip_rotation_changed"
field93.accessType = "outputOnly"
field93.type = "SFRotation"

ExternProtoDeclare79.field.append(field93)
field94 = x3d.field()
field94.name = "r_knee_rotation_changed"
field94.accessType = "outputOnly"
field94.type = "SFRotation"

ExternProtoDeclare79.field.append(field94)
field95 = x3d.field()
field95.name = "r_ankle_rotation_changed"
field95.accessType = "outputOnly"
field95.type = "SFRotation"

ExternProtoDeclare79.field.append(field95)
field96 = x3d.field()
field96.name = "r_midtarsal_rotation_changed"
field96.accessType = "outputOnly"
field96.type = "SFRotation"

ExternProtoDeclare79.field.append(field96)
field97 = x3d.field()
field97.name = "vl5_rotation_changed"
field97.accessType = "outputOnly"
field97.type = "SFRotation"

ExternProtoDeclare79.field.append(field97)
field98 = x3d.field()
field98.name = "skullbase_rotation_changed"
field98.accessType = "outputOnly"
field98.type = "SFRotation"

ExternProtoDeclare79.field.append(field98)
field99 = x3d.field()
field99.name = "l_shoulder_rotation_changed"
field99.accessType = "outputOnly"
field99.type = "SFRotation"

ExternProtoDeclare79.field.append(field99)
field100 = x3d.field()
field100.name = "l_elbow_rotation_changed"
field100.accessType = "outputOnly"
field100.type = "SFRotation"

ExternProtoDeclare79.field.append(field100)
field101 = x3d.field()
field101.name = "l_wrist_rotation_changed"
field101.accessType = "outputOnly"
field101.type = "SFRotation"

ExternProtoDeclare79.field.append(field101)
field102 = x3d.field()
field102.name = "r_shoulder_rotation_changed"
field102.accessType = "outputOnly"
field102.type = "SFRotation"

ExternProtoDeclare79.field.append(field102)
field103 = x3d.field()
field103.name = "r_elbow_rotation_changed"
field103.accessType = "outputOnly"
field103.type = "SFRotation"

ExternProtoDeclare79.field.append(field103)
field104 = x3d.field()
field104.name = "r_wrist_rotation_changed"
field104.accessType = "outputOnly"
field104.type = "SFRotation"

ExternProtoDeclare79.field.append(field104)
field105 = x3d.field()
field105.name = "isActive"
field105.accessType = "outputOnly"
field105.type = "SFBool"

ExternProtoDeclare79.field.append(field105)

Scene24.children.append(ExternProtoDeclare79)
ExternProtoDeclare106 = x3d.ExternProtoDeclare()
ExternProtoDeclare106.name = "LOA1_JumpAnimation"
ExternProtoDeclare106.url = ["LOA1_JumpAnimation.x3d#LOA1_JumpAnimation","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/LOA1_JumpAnimation.x3d#LOA1_JumpAnimation","LOA1_JumpAnimation.wrl#LOA1_JumpAnimation","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/LOA1_JumpAnimation.wrl#LOA1_JumpAnimation"]
field107 = x3d.field()
field107.name = "cycleInterval"
field107.accessType = "inputOutput"
field107.type = "SFTime"

ExternProtoDeclare106.field.append(field107)
field108 = x3d.field()
field108.name = "enabled"
field108.accessType = "inputOutput"
field108.type = "SFBool"

ExternProtoDeclare106.field.append(field108)
field109 = x3d.field()
field109.name = "loop"
field109.accessType = "inputOutput"
field109.type = "SFBool"

ExternProtoDeclare106.field.append(field109)
field110 = x3d.field()
field110.name = "startTime"
field110.accessType = "inputOutput"
field110.type = "SFTime"

ExternProtoDeclare106.field.append(field110)
field111 = x3d.field()
field111.name = "stopTime"
field111.accessType = "inputOutput"
field111.type = "SFTime"

ExternProtoDeclare106.field.append(field111)
field112 = x3d.field()
field112.name = "fraction_changed"
field112.accessType = "outputOnly"
field112.type = "SFFloat"

ExternProtoDeclare106.field.append(field112)
field113 = x3d.field()
field113.name = "humanoid_root_translation_changed"
field113.accessType = "outputOnly"
field113.type = "SFVec3f"

ExternProtoDeclare106.field.append(field113)
field114 = x3d.field()
field114.name = "humanoid_root_rotation_changed"
field114.accessType = "outputOnly"
field114.type = "SFRotation"

ExternProtoDeclare106.field.append(field114)
field115 = x3d.field()
field115.name = "lower_body_rotation_changed"
field115.accessType = "outputOnly"
field115.type = "SFRotation"

ExternProtoDeclare106.field.append(field115)
field116 = x3d.field()
field116.name = "l_hip_rotation_changed"
field116.accessType = "outputOnly"
field116.type = "SFRotation"

ExternProtoDeclare106.field.append(field116)
field117 = x3d.field()
field117.name = "l_knee_rotation_changed"
field117.accessType = "outputOnly"
field117.type = "SFRotation"

ExternProtoDeclare106.field.append(field117)
field118 = x3d.field()
field118.name = "l_ankle_rotation_changed"
field118.accessType = "outputOnly"
field118.type = "SFRotation"

ExternProtoDeclare106.field.append(field118)
field119 = x3d.field()
field119.name = "l_midtarsal_rotation_changed"
field119.accessType = "outputOnly"
field119.type = "SFRotation"

ExternProtoDeclare106.field.append(field119)
field120 = x3d.field()
field120.name = "r_hip_rotation_changed"
field120.accessType = "outputOnly"
field120.type = "SFRotation"

ExternProtoDeclare106.field.append(field120)
field121 = x3d.field()
field121.name = "r_knee_rotation_changed"
field121.accessType = "outputOnly"
field121.type = "SFRotation"

ExternProtoDeclare106.field.append(field121)
field122 = x3d.field()
field122.name = "r_ankle_rotation_changed"
field122.accessType = "outputOnly"
field122.type = "SFRotation"

ExternProtoDeclare106.field.append(field122)
field123 = x3d.field()
field123.name = "r_midtarsal_rotation_changed"
field123.accessType = "outputOnly"
field123.type = "SFRotation"

ExternProtoDeclare106.field.append(field123)
field124 = x3d.field()
field124.name = "vl5_rotation_changed"
field124.accessType = "outputOnly"
field124.type = "SFRotation"

ExternProtoDeclare106.field.append(field124)
field125 = x3d.field()
field125.name = "skullbase_rotation_changed"
field125.accessType = "outputOnly"
field125.type = "SFRotation"

ExternProtoDeclare106.field.append(field125)
field126 = x3d.field()
field126.name = "l_shoulder_rotation_changed"
field126.accessType = "outputOnly"
field126.type = "SFRotation"

ExternProtoDeclare106.field.append(field126)
field127 = x3d.field()
field127.name = "l_elbow_rotation_changed"
field127.accessType = "outputOnly"
field127.type = "SFRotation"

ExternProtoDeclare106.field.append(field127)
field128 = x3d.field()
field128.name = "l_wrist_rotation_changed"
field128.accessType = "outputOnly"
field128.type = "SFRotation"

ExternProtoDeclare106.field.append(field128)
field129 = x3d.field()
field129.name = "r_shoulder_rotation_changed"
field129.accessType = "outputOnly"
field129.type = "SFRotation"

ExternProtoDeclare106.field.append(field129)
field130 = x3d.field()
field130.name = "r_elbow_rotation_changed"
field130.accessType = "outputOnly"
field130.type = "SFRotation"

ExternProtoDeclare106.field.append(field130)
field131 = x3d.field()
field131.name = "r_wrist_rotation_changed"
field131.accessType = "outputOnly"
field131.type = "SFRotation"

ExternProtoDeclare106.field.append(field131)
field132 = x3d.field()
field132.name = "isActive"
field132.accessType = "outputOnly"
field132.type = "SFBool"

ExternProtoDeclare106.field.append(field132)

Scene24.children.append(ExternProtoDeclare106)
ExternProtoDeclare133 = x3d.ExternProtoDeclare()
ExternProtoDeclare133.name = "LOA1_KneelAnimation"
ExternProtoDeclare133.url = ["LOA1_KneelAnimation.x3d#LOA1_KneelAnimation","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/LOA1_KneelAnimation.x3d#LOA1_KneelAnimation","LOA1_KneelAnimation.wrl#LOA1_KneelAnimation","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/LOA1_KneelAnimation.wrl#LOA1_KneelAnimation"]
field134 = x3d.field()
field134.name = "cycleInterval"
field134.accessType = "inputOutput"
field134.type = "SFTime"

ExternProtoDeclare133.field.append(field134)
field135 = x3d.field()
field135.name = "enabled"
field135.accessType = "inputOutput"
field135.type = "SFBool"

ExternProtoDeclare133.field.append(field135)
field136 = x3d.field()
field136.name = "loop"
field136.accessType = "inputOutput"
field136.type = "SFBool"

ExternProtoDeclare133.field.append(field136)
field137 = x3d.field()
field137.name = "startTime"
field137.accessType = "inputOutput"
field137.type = "SFTime"

ExternProtoDeclare133.field.append(field137)
field138 = x3d.field()
field138.name = "stopTime"
field138.accessType = "inputOutput"
field138.type = "SFTime"

ExternProtoDeclare133.field.append(field138)
field139 = x3d.field()
field139.name = "fraction_changed"
field139.accessType = "outputOnly"
field139.type = "SFFloat"

ExternProtoDeclare133.field.append(field139)
field140 = x3d.field()
field140.name = "isActive"
field140.accessType = "outputOnly"
field140.type = "SFBool"

ExternProtoDeclare133.field.append(field140)
field141 = x3d.field()
field141.name = "humanoid_root_translation_changed"
field141.accessType = "outputOnly"
field141.type = "SFVec3f"

ExternProtoDeclare133.field.append(field141)
field142 = x3d.field()
field142.name = "humanoid_root_rotation_changed"
field142.accessType = "outputOnly"
field142.type = "SFRotation"

ExternProtoDeclare133.field.append(field142)
field143 = x3d.field()
field143.name = "lower_body_rotation_changed"
field143.accessType = "outputOnly"
field143.type = "SFRotation"

ExternProtoDeclare133.field.append(field143)
field144 = x3d.field()
field144.name = "l_hip_rotation_changed"
field144.accessType = "outputOnly"
field144.type = "SFRotation"

ExternProtoDeclare133.field.append(field144)
field145 = x3d.field()
field145.name = "l_knee_rotation_changed"
field145.accessType = "outputOnly"
field145.type = "SFRotation"

ExternProtoDeclare133.field.append(field145)
field146 = x3d.field()
field146.name = "l_ankle_rotation_changed"
field146.accessType = "outputOnly"
field146.type = "SFRotation"

ExternProtoDeclare133.field.append(field146)
field147 = x3d.field()
field147.name = "l_midtarsal_rotation_changed"
field147.accessType = "outputOnly"
field147.type = "SFRotation"

ExternProtoDeclare133.field.append(field147)
field148 = x3d.field()
field148.name = "r_hip_rotation_changed"
field148.accessType = "outputOnly"
field148.type = "SFRotation"

ExternProtoDeclare133.field.append(field148)
field149 = x3d.field()
field149.name = "r_knee_rotation_changed"
field149.accessType = "outputOnly"
field149.type = "SFRotation"

ExternProtoDeclare133.field.append(field149)
field150 = x3d.field()
field150.name = "r_ankle_rotation_changed"
field150.accessType = "outputOnly"
field150.type = "SFRotation"

ExternProtoDeclare133.field.append(field150)
field151 = x3d.field()
field151.name = "r_midtarsal_rotation_changed"
field151.accessType = "outputOnly"
field151.type = "SFRotation"

ExternProtoDeclare133.field.append(field151)
field152 = x3d.field()
field152.name = "vl5_rotation_changed"
field152.accessType = "outputOnly"
field152.type = "SFRotation"

ExternProtoDeclare133.field.append(field152)
field153 = x3d.field()
field153.name = "skullbase_rotation_changed"
field153.accessType = "outputOnly"
field153.type = "SFRotation"

ExternProtoDeclare133.field.append(field153)
field154 = x3d.field()
field154.name = "l_shoulder_rotation_changed"
field154.accessType = "outputOnly"
field154.type = "SFRotation"

ExternProtoDeclare133.field.append(field154)
field155 = x3d.field()
field155.name = "l_elbow_rotation_changed"
field155.accessType = "outputOnly"
field155.type = "SFRotation"

ExternProtoDeclare133.field.append(field155)
field156 = x3d.field()
field156.name = "l_wrist_rotation_changed"
field156.accessType = "outputOnly"
field156.type = "SFRotation"

ExternProtoDeclare133.field.append(field156)
field157 = x3d.field()
field157.name = "r_shoulder_rotation_changed"
field157.accessType = "outputOnly"
field157.type = "SFRotation"

ExternProtoDeclare133.field.append(field157)
field158 = x3d.field()
field158.name = "r_elbow_rotation_changed"
field158.accessType = "outputOnly"
field158.type = "SFRotation"

ExternProtoDeclare133.field.append(field158)
field159 = x3d.field()
field159.name = "r_wrist_rotation_changed"
field159.accessType = "outputOnly"
field159.type = "SFRotation"

ExternProtoDeclare133.field.append(field159)

Scene24.children.append(ExternProtoDeclare133)
#**********Human Model Protypes*********
ProtoDeclare160 = x3d.ProtoDeclare()
ProtoDeclare160.name = "Humanoid1_1"
ProtoDeclare160.appinfo = "The Humanoid node serves as overall container for the Joint Segment Site and Viewpoint nodes which define the skeleton geometry and landmarks of the humanoid figure. Additionally the node provides a means for defining information about the author copyright and usage restrictions of the model."
ProtoDeclare160.documentation = "http://HAnim.org/Specifications/HAnim2001/part1/Humanoid.html"
ProtoInterface161 = x3d.ProtoInterface()
#HAnim v1.1 field definitions
field162 = x3d.field()
field162.name = "name"
field162.accessType = "inputOutput"
field162.type = "SFString"

ProtoInterface161.field.append(field162)
field163 = x3d.field()
field163.name = "version"
field163.accessType = "inputOutput"
field163.appinfo = "legal values: 1.1 or 2.0"
field163.type = "SFString"
field163.value = "1.1"

ProtoInterface161.field.append(field163)
field164 = x3d.field()
field164.name = "humanoidVersion"
field164.accessType = "inputOutput"
field164.appinfo = "Version of the humanoid being modeled. Hint: HAnim version 2.0"
field164.type = "SFString"

ProtoInterface161.field.append(field164)
field165 = x3d.field()
field165.name = "info"
field165.accessType = "inputOutput"
field165.type = "MFString"

ProtoInterface161.field.append(field165)
field166 = x3d.field()
field166.name = "translation"
field166.accessType = "inputOutput"
field166.type = "SFVec3f"
field166.value = [0,0,0]

ProtoInterface161.field.append(field166)
field167 = x3d.field()
field167.name = "rotation"
field167.accessType = "inputOutput"
field167.type = "SFRotation"
field167.value = [0,0,1,0]

ProtoInterface161.field.append(field167)
field168 = x3d.field()
field168.name = "center"
field168.accessType = "inputOutput"
field168.type = "SFVec3f"
field168.value = [0,0,0]

ProtoInterface161.field.append(field168)
field169 = x3d.field()
field169.name = "scale"
field169.accessType = "inputOutput"
field169.type = "SFVec3f"
field169.value = [1,1,1]

ProtoInterface161.field.append(field169)
field170 = x3d.field()
field170.name = "scaleOrientation"
field170.accessType = "inputOutput"
field170.type = "SFRotation"
field170.value = [0,0,1,0]

ProtoInterface161.field.append(field170)
field171 = x3d.field()
field171.name = "bboxCenter"
field171.accessType = "initializeOnly"
field171.type = "SFVec3f"
field171.value = [0,0,0]

ProtoInterface161.field.append(field171)
field172 = x3d.field()
field172.name = "bboxSize"
field172.accessType = "initializeOnly"
field172.type = "SFVec3f"
field172.value = [-1,-1,-1]

ProtoInterface161.field.append(field172)
field173 = x3d.field()
field173.name = "humanoidBody"
field173.accessType = "inputOutput"
field173.appinfo = "HAnim 1.1 field container for body head. Hint: replaced by 2.0 skeleton."
field173.documentation = "http://HAnim.org/Specifications/HAnim1.1/#humanoid"
field173.type = "MFNode"

ProtoInterface161.field.append(field173)
field174 = x3d.field()
field174.name = "skeleton"
field174.accessType = "inputOutput"
field174.appinfo = "HAnim 2.0 field container for body geometry Hint: replaces 1.1 humanoidBody"
field174.documentation = "http://HAnim.org/Specifications/HAnim2001/part1/Humanoid.html"
field174.type = "MFNode"

ProtoInterface161.field.append(field174)
field175 = x3d.field()
field175.name = "joints"
field175.accessType = "inputOutput"
field175.appinfo = "Container field for Joint nodes"
field175.type = "MFNode"

ProtoInterface161.field.append(field175)
field176 = x3d.field()
field176.name = "segments"
field176.accessType = "inputOutput"
field176.appinfo = "Container field for Segment nodes"
field176.type = "MFNode"

ProtoInterface161.field.append(field176)
field177 = x3d.field()
field177.name = "sites"
field177.accessType = "inputOutput"
field177.appinfo = "Container field for Site nodes"
field177.type = "MFNode"

ProtoInterface161.field.append(field177)
field178 = x3d.field()
field178.name = "viewpoints"
field178.accessType = "inputOutput"
field178.appinfo = "Container field for Viewpoint nodes"
field178.type = "MFNode"

ProtoInterface161.field.append(field178)
field179 = x3d.field()
field179.name = "skinCoord"
field179.accessType = "inputOutput"
field179.appinfo = "Hint: HAnim version 2.0"
field179.type = "SFNode"
#NULL node

ProtoInterface161.field.append(field179)
field180 = x3d.field()
field180.name = "skinNormal"
field180.accessType = "inputOutput"
field180.appinfo = "Hint: HAnim version 2.0"
field180.type = "SFNode"
#NULL node

ProtoInterface161.field.append(field180)

ProtoDeclare160.ProtoInterface = ProtoInterface161
ProtoBody181 = x3d.ProtoBody()
Transform182 = x3d.Transform()
Transform182.DEF = "HumanoidTransform"
IS183 = x3d.IS()
connect184 = x3d.connect()
connect184.nodeField = "translation"
connect184.protoField = "translation"

IS183.connect.append(connect184)
connect185 = x3d.connect()
connect185.nodeField = "rotation"
connect185.protoField = "rotation"

IS183.connect.append(connect185)
connect186 = x3d.connect()
connect186.nodeField = "center"
connect186.protoField = "center"

IS183.connect.append(connect186)
connect187 = x3d.connect()
connect187.nodeField = "scale"
connect187.protoField = "scale"

IS183.connect.append(connect187)
connect188 = x3d.connect()
connect188.nodeField = "scaleOrientation"
connect188.protoField = "scaleOrientation"

IS183.connect.append(connect188)
connect189 = x3d.connect()
connect189.nodeField = "bboxCenter"
connect189.protoField = "bboxCenter"

IS183.connect.append(connect189)
connect190 = x3d.connect()
connect190.nodeField = "bboxSize"
connect190.protoField = "bboxSize"

IS183.connect.append(connect190)

Transform182.IS = IS183
Group191 = x3d.Group()
Group191.DEF = "HumanoidGroup1"
IS192 = x3d.IS()
connect193 = x3d.connect()
connect193.nodeField = "children"
connect193.protoField = "humanoidBody"

IS192.connect.append(connect193)

Group191.IS = IS192

Transform182.children.append(Group191)
Group194 = x3d.Group()
Group194.DEF = "HumanoidGroup2"
IS195 = x3d.IS()
connect196 = x3d.connect()
connect196.nodeField = "children"
connect196.protoField = "skeleton"

IS195.connect.append(connect196)

Group194.IS = IS195

Transform182.children.append(Group194)
Group197 = x3d.Group()
Group197.DEF = "HumanoidGroup3"
IS198 = x3d.IS()
connect199 = x3d.connect()
connect199.nodeField = "children"
connect199.protoField = "viewpoints"

IS198.connect.append(connect199)

Group197.IS = IS198

Transform182.children.append(Group197)

ProtoBody181.children.append(Transform182)

ProtoDeclare160.ProtoBody = ProtoBody181

Scene24.children.append(ProtoDeclare160)
ProtoDeclare200 = x3d.ProtoDeclare()
ProtoDeclare200.name = "Joint"
ProtoDeclare200.appinfo = "The Joint node is used as a building block to describe the articulations of the humanoid figure. Each articulation of the humanoid figure is represented by a Joint node each of which is organized into a hierarchy that describes the overall skeleton of the humanoid."
ProtoDeclare200.documentation = "http://HAnim.org/Specifications/HAnim2001/part1/Joint.html"
ProtoInterface201 = x3d.ProtoInterface()
field202 = x3d.field()
field202.name = "name"
field202.accessType = "inputOutput"
field202.type = "SFString"

ProtoInterface201.field.append(field202)
field203 = x3d.field()
field203.name = "ulimit"
field203.accessType = "inputOutput"
field203.type = "MFFloat"

ProtoInterface201.field.append(field203)
field204 = x3d.field()
field204.name = "llimit"
field204.accessType = "inputOutput"
field204.type = "MFFloat"

ProtoInterface201.field.append(field204)
field205 = x3d.field()
field205.name = "limitOrientation"
field205.accessType = "inputOutput"
field205.type = "SFRotation"
field205.value = [0,0,1,0]

ProtoInterface201.field.append(field205)
field206 = x3d.field()
field206.name = "skinCoordIndex"
field206.accessType = "inputOutput"
field206.type = "MFInt32"

ProtoInterface201.field.append(field206)
field207 = x3d.field()
field207.name = "skinCoordWeight"
field207.accessType = "inputOutput"
field207.type = "MFFloat"

ProtoInterface201.field.append(field207)
field208 = x3d.field()
field208.name = "stiffness"
field208.accessType = "inputOutput"
field208.type = "MFFloat"
field208.value = [0,0,0]

ProtoInterface201.field.append(field208)
field209 = x3d.field()
field209.name = "translation"
field209.accessType = "inputOutput"
field209.type = "SFVec3f"
field209.value = [0,0,0]

ProtoInterface201.field.append(field209)
field210 = x3d.field()
field210.name = "rotation"
field210.accessType = "inputOutput"
field210.type = "SFRotation"
field210.value = [0,0,1,0]

ProtoInterface201.field.append(field210)
field211 = x3d.field()
field211.name = "scale"
field211.accessType = "inputOutput"
field211.type = "SFVec3f"
field211.value = [1,1,1]

ProtoInterface201.field.append(field211)
field212 = x3d.field()
field212.name = "scaleOrientation"
field212.accessType = "inputOutput"
field212.type = "SFRotation"
field212.value = [0,0,1,0]

ProtoInterface201.field.append(field212)
field213 = x3d.field()
field213.name = "center"
field213.accessType = "inputOutput"
field213.type = "SFVec3f"
field213.value = [0,0,0]

ProtoInterface201.field.append(field213)
field214 = x3d.field()
field214.name = "bboxCenter"
field214.accessType = "initializeOnly"
field214.type = "SFVec3f"
field214.value = [0,0,0]

ProtoInterface201.field.append(field214)
field215 = x3d.field()
field215.name = "bboxSize"
field215.accessType = "initializeOnly"
field215.type = "SFVec3f"
field215.value = [-1,-1,-1]

ProtoInterface201.field.append(field215)
field216 = x3d.field()
field216.name = "children"
field216.accessType = "inputOutput"
field216.type = "MFNode"

ProtoInterface201.field.append(field216)
field217 = x3d.field()
field217.name = "addChildren"
field217.accessType = "inputOnly"
field217.type = "MFNode"

ProtoInterface201.field.append(field217)
field218 = x3d.field()
field218.name = "removeChildren"
field218.accessType = "inputOnly"
field218.type = "MFNode"

ProtoInterface201.field.append(field218)

ProtoDeclare200.ProtoInterface = ProtoInterface201
ProtoBody219 = x3d.ProtoBody()
Transform220 = x3d.Transform()
Transform220.DEF = "JointTransform"
IS221 = x3d.IS()
connect222 = x3d.connect()
connect222.nodeField = "translation"
connect222.protoField = "translation"

IS221.connect.append(connect222)
connect223 = x3d.connect()
connect223.nodeField = "rotation"
connect223.protoField = "rotation"

IS221.connect.append(connect223)
connect224 = x3d.connect()
connect224.nodeField = "center"
connect224.protoField = "center"

IS221.connect.append(connect224)
connect225 = x3d.connect()
connect225.nodeField = "scale"
connect225.protoField = "scale"

IS221.connect.append(connect225)
connect226 = x3d.connect()
connect226.nodeField = "scaleOrientation"
connect226.protoField = "scaleOrientation"

IS221.connect.append(connect226)
connect227 = x3d.connect()
connect227.nodeField = "bboxCenter"
connect227.protoField = "bboxCenter"

IS221.connect.append(connect227)
connect228 = x3d.connect()
connect228.nodeField = "bboxSize"
connect228.protoField = "bboxSize"

IS221.connect.append(connect228)
connect229 = x3d.connect()
connect229.nodeField = "children"
connect229.protoField = "children"

IS221.connect.append(connect229)
connect230 = x3d.connect()
connect230.nodeField = "addChildren"
connect230.protoField = "addChildren"

IS221.connect.append(connect230)
connect231 = x3d.connect()
connect231.nodeField = "removeChildren"
connect231.protoField = "removeChildren"

IS221.connect.append(connect231)

Transform220.IS = IS221

ProtoBody219.children.append(Transform220)

ProtoDeclare200.ProtoBody = ProtoBody219

Scene24.children.append(ProtoDeclare200)
ProtoDeclare232 = x3d.ProtoDeclare()
ProtoDeclare232.name = "Segment"
ProtoDeclare232.appinfo = "The Segment node is used describe the attributes of the physical links between the joints of the humanoid figure. Each body part (pelvis thigh calf etc.) of the humanoid figure is represented by a Segment node."
ProtoDeclare232.documentation = "http://HAnim.org/Specifications/HAnim2001/part1/Segment.html"
ProtoInterface233 = x3d.ProtoInterface()
field234 = x3d.field()
field234.name = "name"
field234.accessType = "inputOutput"
field234.type = "SFString"

ProtoInterface233.field.append(field234)
field235 = x3d.field()
field235.name = "mass"
field235.accessType = "inputOutput"
field235.type = "SFFloat"
field235.value = 0

ProtoInterface233.field.append(field235)
field236 = x3d.field()
field236.name = "centerOfMass"
field236.accessType = "inputOutput"
field236.type = "SFVec3f"
field236.value = [0,0,0]

ProtoInterface233.field.append(field236)
field237 = x3d.field()
field237.name = "momentsOfInertia"
field237.accessType = "inputOutput"
field237.type = "MFFloat"
field237.value = [0,0,0,0,0,0,0,0,0]

ProtoInterface233.field.append(field237)
field238 = x3d.field()
field238.name = "bboxCenter"
field238.accessType = "initializeOnly"
field238.type = "SFVec3f"
field238.value = [0,0,0]

ProtoInterface233.field.append(field238)
field239 = x3d.field()
field239.name = "bboxSize"
field239.accessType = "initializeOnly"
field239.type = "SFVec3f"
field239.value = [-1,-1,-1]

ProtoInterface233.field.append(field239)
field240 = x3d.field()
field240.name = "children"
field240.accessType = "inputOutput"
field240.type = "MFNode"

ProtoInterface233.field.append(field240)
field241 = x3d.field()
field241.name = "addChildren"
field241.accessType = "inputOnly"
field241.type = "MFNode"

ProtoInterface233.field.append(field241)
field242 = x3d.field()
field242.name = "removeChildren"
field242.accessType = "inputOnly"
field242.type = "MFNode"

ProtoInterface233.field.append(field242)
field243 = x3d.field()
field243.name = "coord"
field243.accessType = "inputOutput"
field243.appinfo = "contains Coordinate nodes"
field243.type = "SFNode"
#NULL node

ProtoInterface233.field.append(field243)
field244 = x3d.field()
field244.name = "displacers"
field244.accessType = "inputOutput"
field244.appinfo = "contains Displacer nodes"
field244.type = "MFNode"

ProtoInterface233.field.append(field244)

ProtoDeclare232.ProtoInterface = ProtoInterface233
ProtoBody245 = x3d.ProtoBody()
Group246 = x3d.Group()
Group246.DEF = "SegmentGroup"
IS247 = x3d.IS()
connect248 = x3d.connect()
connect248.nodeField = "bboxCenter"
connect248.protoField = "bboxCenter"

IS247.connect.append(connect248)
connect249 = x3d.connect()
connect249.nodeField = "bboxSize"
connect249.protoField = "bboxSize"

IS247.connect.append(connect249)
connect250 = x3d.connect()
connect250.nodeField = "children"
connect250.protoField = "children"

IS247.connect.append(connect250)
connect251 = x3d.connect()
connect251.nodeField = "addChildren"
connect251.protoField = "addChildren"

IS247.connect.append(connect251)
connect252 = x3d.connect()
connect252.nodeField = "removeChildren"
connect252.protoField = "removeChildren"

IS247.connect.append(connect252)

Group246.IS = IS247

ProtoBody245.children.append(Group246)

ProtoDeclare232.ProtoBody = ProtoBody245

Scene24.children.append(ProtoDeclare232)
ProtoDeclare253 = x3d.ProtoDeclare()
ProtoDeclare253.name = "Site"
ProtoDeclare253.appinfo = "The Site node can be used for three purposes: (a) to define an \"end effector\" location which can be used by an inverse kinematics system (b) to define an attachment point for accessories such as jewelry and clothing and (c) to define a location for a virtual camera in the reference frame of a Segment node (such as a view \"through the eyes\" of the humanoid for use in multi-user worlds)."
ProtoDeclare253.documentation = "http://HAnim.org/Specifications/HAnim2001/part1/Site.html"
ProtoInterface254 = x3d.ProtoInterface()
field255 = x3d.field()
field255.name = "name"
field255.accessType = "inputOutput"
field255.type = "SFString"

ProtoInterface254.field.append(field255)
field256 = x3d.field()
field256.name = "translation"
field256.accessType = "inputOutput"
field256.type = "SFVec3f"
field256.value = [0,0,0]

ProtoInterface254.field.append(field256)
field257 = x3d.field()
field257.name = "rotation"
field257.accessType = "inputOutput"
field257.type = "SFRotation"
field257.value = [0,0,1,0]

ProtoInterface254.field.append(field257)
field258 = x3d.field()
field258.name = "scale"
field258.accessType = "inputOutput"
field258.type = "SFVec3f"
field258.value = [1,1,1]

ProtoInterface254.field.append(field258)
field259 = x3d.field()
field259.name = "scaleOrientation"
field259.accessType = "inputOutput"
field259.type = "SFRotation"
field259.value = [0,0,1,0]

ProtoInterface254.field.append(field259)
field260 = x3d.field()
field260.name = "center"
field260.accessType = "inputOutput"
field260.type = "SFVec3f"
field260.value = [0,0,0]

ProtoInterface254.field.append(field260)
field261 = x3d.field()
field261.name = "bboxCenter"
field261.accessType = "initializeOnly"
field261.type = "SFVec3f"
field261.value = [0,0,0]

ProtoInterface254.field.append(field261)
field262 = x3d.field()
field262.name = "bboxSize"
field262.accessType = "initializeOnly"
field262.type = "SFVec3f"
field262.value = [-1,-1,-1]

ProtoInterface254.field.append(field262)
field263 = x3d.field()
field263.name = "children"
field263.accessType = "inputOutput"
field263.type = "MFNode"

ProtoInterface254.field.append(field263)
field264 = x3d.field()
field264.name = "addChildren"
field264.accessType = "inputOnly"
field264.type = "MFNode"

ProtoInterface254.field.append(field264)
field265 = x3d.field()
field265.name = "removeChildren"
field265.accessType = "inputOnly"
field265.type = "MFNode"

ProtoInterface254.field.append(field265)

ProtoDeclare253.ProtoInterface = ProtoInterface254
ProtoBody266 = x3d.ProtoBody()
Transform267 = x3d.Transform()
Transform267.DEF = "SiteTransform"
IS268 = x3d.IS()
connect269 = x3d.connect()
connect269.nodeField = "translation"
connect269.protoField = "translation"

IS268.connect.append(connect269)
connect270 = x3d.connect()
connect270.nodeField = "rotation"
connect270.protoField = "rotation"

IS268.connect.append(connect270)
connect271 = x3d.connect()
connect271.nodeField = "center"
connect271.protoField = "center"

IS268.connect.append(connect271)
connect272 = x3d.connect()
connect272.nodeField = "scale"
connect272.protoField = "scale"

IS268.connect.append(connect272)
connect273 = x3d.connect()
connect273.nodeField = "scaleOrientation"
connect273.protoField = "scaleOrientation"

IS268.connect.append(connect273)
connect274 = x3d.connect()
connect274.nodeField = "bboxCenter"
connect274.protoField = "bboxCenter"

IS268.connect.append(connect274)
connect275 = x3d.connect()
connect275.nodeField = "bboxSize"
connect275.protoField = "bboxSize"

IS268.connect.append(connect275)
connect276 = x3d.connect()
connect276.nodeField = "children"
connect276.protoField = "children"

IS268.connect.append(connect276)
connect277 = x3d.connect()
connect277.nodeField = "addChildren"
connect277.protoField = "addChildren"

IS268.connect.append(connect277)
connect278 = x3d.connect()
connect278.nodeField = "removeChildren"
connect278.protoField = "removeChildren"

IS268.connect.append(connect278)

Transform267.IS = IS268

ProtoBody266.children.append(Transform267)

ProtoDeclare253.ProtoBody = ProtoBody266

Scene24.children.append(ProtoDeclare253)
ProtoDeclare279 = x3d.ProtoDeclare()
ProtoDeclare279.name = "Displacer"
ProtoDeclare279.appinfo = "A Displacer can be used in three different ways: (a) identify the vertices corresponding to a particular feature on a Segment (b) represent a particular muscular action which displaces the vertices in various directions (linearly or radially) and (c) represent a complete configuration of the vertices in a Segment."
ProtoDeclare279.documentation = "http://HAnim.org/Specifications/HAnim2001/part1/Displacer.html"
ProtoInterface280 = x3d.ProtoInterface()
field281 = x3d.field()
field281.name = "name"
field281.accessType = "inputOutput"
field281.type = "SFString"

ProtoInterface280.field.append(field281)
field282 = x3d.field()
field282.name = "coordIndex"
field282.accessType = "inputOutput"
field282.type = "MFInt32"

ProtoInterface280.field.append(field282)
field283 = x3d.field()
field283.name = "displacements"
field283.accessType = "inputOutput"
field283.type = "MFVec3f"

ProtoInterface280.field.append(field283)

ProtoDeclare279.ProtoInterface = ProtoInterface280
ProtoBody284 = x3d.ProtoBody()
WorldInfo285 = x3d.WorldInfo()
WorldInfo285.info = ["null body node"]

ProtoBody284.children.append(WorldInfo285)

ProtoDeclare279.ProtoBody = ProtoBody284

Scene24.children.append(ProtoDeclare279)
#***********ViewPoints*************
Viewpoint286 = x3d.Viewpoint()
Viewpoint286.DEF = "InclinedView"
Viewpoint286.description = "Inclined View"
Viewpoint286.orientation = [-0.113,0.993,0.0347,0.671]
Viewpoint286.position = [1.62,1.05,2.06]

Scene24.children.append(Viewpoint286)
Viewpoint287 = x3d.Viewpoint()
Viewpoint287.DEF = "FrontView"
Viewpoint287.description = "Front View"
Viewpoint287.position = [0,0.854,2.57665]

Scene24.children.append(Viewpoint287)
Viewpoint288 = x3d.Viewpoint()
Viewpoint288.DEF = "SideView"
Viewpoint288.description = "Side View"
Viewpoint288.orientation = [0,1,0,1.57079]
Viewpoint288.position = [2.5929,0.854,0]

Scene24.children.append(Viewpoint288)
Viewpoint289 = x3d.Viewpoint()
Viewpoint289.DEF = "TopView"
Viewpoint289.description = "Top View"
Viewpoint289.orientation = [1,0,0,-1.57079]
Viewpoint289.position = [0,3.4495,0]

Scene24.children.append(Viewpoint289)
NavigationInfo290 = x3d.NavigationInfo()
NavigationInfo290.avatarSize = [0.15,1.53,0.75]
NavigationInfo290.speed = 0.5
NavigationInfo290.type = ["EXAMINE"]

Scene24.children.append(NavigationInfo290)
#**********Avatar Proto Instances***********
Switch291 = x3d.Switch()
Switch291.DEF = "AvatarSwitch"
Switch291.whichChoice = 0
#Humanoid1 used for v1.1 humanoid, which is what Allen and Nancy are. Boxman is HAnim 2001. Can't have identically named prototypes for Humanoid in each version since prototype signatures are different.
ProtoInstance292 = x3d.ProtoInstance()
ProtoInstance292.name = "Humanoid1_1"
ProtoInstance292.DEF = "Allen"
fieldValue293 = x3d.fieldValue()
fieldValue293.name = "humanoidBody"
ProtoInstance294 = x3d.ProtoInstance()
ProtoInstance294.name = "Joint"
ProtoInstance294.DEF = "Allen_hanim_humanoid_root"
fieldValue295 = x3d.fieldValue()
fieldValue295.name = "name"
fieldValue295.value = "humanoid_root"

ProtoInstance294.fieldValue.append(fieldValue295)
fieldValue296 = x3d.fieldValue()
fieldValue296.name = "center"
fieldValue296.value = "-0.00405 0.855 -0.000113"

ProtoInstance294.fieldValue.append(fieldValue296)
fieldValue297 = x3d.fieldValue()
fieldValue297.name = "children"
ProtoInstance298 = x3d.ProtoInstance()
ProtoInstance298.name = "Joint"
ProtoInstance298.DEF = "Allen_hanim_sacroiliac"
fieldValue299 = x3d.fieldValue()
fieldValue299.name = "name"
fieldValue299.value = "sacroiliac"

ProtoInstance298.fieldValue.append(fieldValue299)
fieldValue300 = x3d.fieldValue()
fieldValue300.name = "center"
fieldValue300.value = "0 1.01 -0.0204"

ProtoInstance298.fieldValue.append(fieldValue300)
fieldValue301 = x3d.fieldValue()
fieldValue301.name = "children"
ProtoInstance302 = x3d.ProtoInstance()
ProtoInstance302.name = "Segment"
ProtoInstance302.DEF = "Allen_hanim_pelvis"
fieldValue303 = x3d.fieldValue()
fieldValue303.name = "name"
fieldValue303.value = "pelvis"

ProtoInstance302.fieldValue.append(fieldValue303)
fieldValue304 = x3d.fieldValue()
fieldValue304.name = "children"
Transform305 = x3d.Transform()
Transform305.center = [-0.7455,1,0.058]
Transform305.rotation = [0,1,0,1.570796]
Transform305.scale = [0.1,0.1,0.1]
Shape306 = x3d.Shape()
Appearance307 = x3d.Appearance()
Material308 = x3d.Material()
Material308.DEF = "Pants_Color"
Material308.ambientIntensity = 0.25
Material308.diffuseColor = [0.054,0.233,0.39]

Appearance307.material = Material308
ImageTexture309 = x3d.ImageTexture()
ImageTexture309.DEF = "camo"
ImageTexture309.repeatS = False
ImageTexture309.repeatT = False
ImageTexture309.url = ["greenCamo.gif","greenCamo.jpg","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/greenCamo.gif","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/greenCamo.jpg"]

Appearance307.texture = ImageTexture309

Shape306.appearance = Appearance307
IndexedFaceSet310 = x3d.IndexedFaceSet()
IndexedFaceSet310.coordIndex = [0,1,2,-1,3,4,5,-1,6,7,8,-1,9,10,11,-1,12,13,14,-1,15,16,17,-1,18,19,20,-1,21,22,23,-1,24,25,26,-1,27,28,29,-1,30,31,32,-1,33,34,35,-1,36,37,38,-1,39,40,41,-1,42,43,44,-1,45,46,47,-1,48,49,50,-1,51,52,53,-1,54,55,56,-1,57,58,59,-1,60,61,62,-1,63,64,65,-1,66,67,68,-1,69,70,71,-1,72,73,74,-1,75,76,77,-1,78,79,80,-1,81,82,83,-1,84,85,86,-1,87,88,89,-1,90,91,92,-1,93,94,95,-1,96,97,98,-1,99,100,101,-1,102,103,104,-1,105,106,107,-1,108,109,110,-1,111,112,113,-1,114,115,116,-1,117,118,119,-1,120,121,122,-1,123,124,125,-1,126,127,128,-1,129,130,131,-1,132,133,134,-1,135,136,137,-1,138,139,140,-1,141,142,143,-1,144,145,146,-1,147,148,149,-1,150,151,152,-1,153,154,155,-1,156,157,158,-1,159,160,161,-1,162,163,164,-1,165,166,167,-1,168,169,170,-1,171,172,173,-1,174,175,176,-1,177,178,179,-1,180,181,182,-1,183,184,185,-1,186,187,188,-1,189,190,191,-1,192,193,194,-1,195,196,197,-1,198,199,200,-1,201,202,203,-1,204,205,206,-1,207,208,209,-1,210,211,212,-1,213,214,215,-1,216,217,218,-1,219,220,221,-1,222,223,224,-1,225,226,227,-1,228,229,230,-1,231,232,233,-1,234,235,236,-1,237,238,239,-1,240,241,242,-1,243,244,245,-1,246,247,248,-1,249,250,251,-1,252,253,254,-1,255,256,257,-1,258,259,260,-1,261,262,263,-1,264,265,266,-1,267,268,269,-1,270,271,272,-1,273,274,275,-1,276,277,278,-1,279,280,281,-1,282,283,284,-1,285,286,287,-1,288,289,290,-1,291,292,293,-1,294,295,296,-1,297,298,299,-1,300,301,302,-1,303,304,305,-1,306,307,308,-1,309,310,311,-1,312,313,314,-1,315,316,317,-1,318,319,320,-1,321,322,323,-1,324,325,326,-1,327,328,329,-1,330,331,332,-1,333,334,335,-1,336,337,338,-1,339,340,341,-1,342,343,344,-1,345,346,347,-1,348,349,350,-1,351,352,353,-1,354,355,356,-1,357,358,359,-1,360,361,362,-1,363,364,365,-1,366,367,368,-1,369,370,371,-1,372,373,374,-1,375,376,377,-1,378,379,380,-1,381,382,383,-1,384,385,386,-1,387,388,389,-1,390,391,392,-1,393,394,395,-1,396,397,398,-1,399,400,401,-1,402,403,404,-1,405,406,407,-1,408,409,410,-1,411,412,413,-1,414,415,416,-1,417,418,419,-1,420,421,422,-1,423,424,425,-1,426,427,428,-1,429,430,431,-1,432,433,434,-1,435,436,437,-1,438,439,440,-1,441,442,443,-1,444,445,446,-1,447,448,449,-1,450,451,452,-1,453,454,455,-1,456,457,458,-1,459,460,461,-1,462,463,464,-1,465,466,467,-1,468,469,470,-1,471,472,473,-1,474,475,476,-1,477,478,479,-1,480,481,482,-1,483,484,485,-1,486,487,488,-1,489,490,491,-1,492,493,494,-1,495,496,497,-1,498,499,500,-1,501,502,503,-1,504,505,506,-1,507,508,509,-1,510,511,512,-1,513,514,515,-1,516,517,518,-1,519,520,521,-1,522,523,524,-1,525,526,527,-1,528,529,530,-1,531,532,533,-1,534,535,536,-1,537,538,539,-1,540,541,542,-1,543,544,545,-1,546,547,548,-1,549,550,551,-1,552,553,554,-1,555,556,557,-1,558,559,560,-1,561,562,563,-1,564,565,566,-1,567,568,569,-1,570,571,572,-1,573,574,575,-1,576,577,578,-1,579,580,581,-1,582,583,584,-1,585,586,587,-1,588,589,590,-1,591,592,593,-1,594,595,596,-1,597,598,599,-1,600,601,602,-1,603,604,605,-1,606,607,608,-1,609,610,611,-1,612,613,614,-1,615,616,617,-1,618,619,620,-1,621,622,623,-1,624,625,626,-1,627,628,629,-1,630,631,632,-1,633,634,635,-1,636,637,638,-1,639,640,641,-1,642,643,644,-1,645,646,647,-1,648,649,650,-1,651,652,653,-1,654,655,656,-1,657,658,659,-1,660,661,662,-1,663,664,665,-1,666,667,668,-1,669,670,671,-1,672,673,674,-1,675,676,677,-1,678,679,680,-1,681,682,683,-1,684,685,686,-1,687,688,689,-1,690,691,692,-1,693,694,695,-1,696,697,698,-1,699,700,701,-1,702,703,704,-1,705,706,707,-1,708,709,710,-1,711,712,713,-1,714,715,716,-1,717,718,719,-1,720,721,722,-1,723,724,725,-1,726,727,728,-1,729,730,731,-1,732,733,734,-1,735,736,737,-1,738,739,740,-1,741,742,743,-1,744,745,746,-1,747,748,749,-1,750,751,752,-1,753,754,755,-1,756,757,758,-1,759,760,761,-1,762,763,764,-1,765,766,767,-1,768,769,770,-1,771,772,773,-1,774,775,776,-1,777,778,779,-1,780,781,782,-1,783,784,785,-1,786,787,788,-1,789,790,791,-1,792,793,794,-1,795,796,797,-1,798,799,800,-1,801,802,803,-1,804,805,806,-1,807,808,809,-1,810,811,812,-1,813,814,815,-1,816,817,818,-1,819,820,821,-1,822,823,824,-1,825,826,827,-1,828,829,830,-1,831,832,833,-1,834,835,836,-1,837,838,839,-1,840,841,842,-1,843,844,845,-1,846,847,848,-1,849,850,851,-1,852,853,854,-1,855,856,857,-1,858,859,860,-1,861,862,863,-1,864,865,866,-1,867,868,869,-1,870,871,872,-1,873,874,875,-1,876,877,878,-1,879,880,881,-1,882,883,884,-1,885,886,887,-1,888,889,890,-1,891,892,893,-1,894,895,896,-1,897,898,899,-1,900,901,902,-1,903,904,905,-1,906,907,908,-1,909,910,911,-1,912,913,914,-1,915,916,917,-1,918,919,920,-1,921,922,923,-1,924,925,926,-1,927,928,929,-1,930,931,932,-1,933,934,935,-1,936,937,938,-1,939,940,941,-1,942,943,944,-1,945,946,947,-1,948,949,950,-1,951,952,953,-1,954,955,956,-1,957,958,959,-1,960,961,962,-1,963,964,965,-1,966,967,968,-1,969,970,971,-1,972,973,974,-1,975,976,977,-1,978,979,980,-1,981,982,983,-1,984,985,986,-1,987,988,989,-1,990,991,992,-1,993,994,995,-1,996,997,998,-1,999,1000,1001,-1,1002,1003,1004,-1,1005,1006,1007,-1,1008,1009,1010,-1,1011,1012,1013,-1,1014,1015,1016,-1,1017,1018,1019,-1,1020,1021,1022,-1,1023,1024,1025,-1,1026,1027,1028,-1,1029,1030,1031,-1,1032,1033,1034,-1,1035,1036,1037,-1,1038,1039,1040,-1,1041,1042,1043,-1,1044,1045,1046,-1,1047,1048,1049,-1,1050,1051,1052,-1,1053,1054,1055,-1,1056,1057,1058,-1,1059,1060,1061,-1,1062,1063,1064,-1,1065,1066,1067,-1,1068,1069,1070,-1,1071,1072,1073,-1,1074,1075,1076,-1,1077,1078,1079,-1,1080,1081,1082,-1,1083,1084,1085,-1,1086,1087,1088,-1,1089,1090,1091,-1,1092,1093,1094,-1,1095,1096,1097,-1,1098,1099,1100,-1,1101,1102,1103,-1,1104,1105,1106,-1,1107,1108,1109,-1,1110,1111,1112,-1,1113,1114,1115,-1,1116,1117,1118,-1,1119,1120,1121,-1,1122,1123,1124,-1,1125,1126,1127,-1,1128,1129,1130,-1,1131,1132,1133,-1,1134,1135,1136,-1,1137,1138,1139,-1,1140,1141,1142,-1,1143,1144,1145,-1,1146,1147,1148,-1,1149,1150,1151,-1,1152,1153,1154,-1,1155,1156,1157,-1,1158,1159,1160,-1,1161,1162,1163,-1,1164,1165,1166,-1,1167,1168,1169,-1,1170,1171,1172,-1,1173,1174,1175,-1,1176,1177,1178,-1,1179,1180,1181,-1,1182,1183,1184,-1,1185,1186,1187,-1,1188,1189,1190,-1,1191,1192,1193,-1,1194,1195,1196,-1,1197,1198,1199,-1,1200,1201,1202,-1,1203,1204,1205,-1,1206,1207,1208,-1,1209,1210,1211,-1,1212,1213,1214,-1,1215,1216,1217,-1,1218,1219,1220,-1,1221,1222,1223,-1,1224,1225,1226,-1,1227,1228,1229,-1,1230,1231,1232,-1,1233,1234,1235,-1,1236,1237,1238,-1,1239,1240,1241,-1,1242,1243,1244,-1,1245,1246,1247,-1,1248,1249,1250,-1,1251,1252,1253,-1,1254,1255,1256,-1,1257,1258,1259,-1,1260,1261,1262,-1,1263,1264,1265,-1,1266,1267,1268,-1,1269,1270,1271,-1,1272,1273,1274,-1,1275,1276,1277,-1,1278,1279,1280,-1,1281,1282,1283,-1,1284,1285,1286,-1,1287,1288,1289,-1,1290,1291,1292,-1,1293,1294,1295,-1,1296,1297,1298,-1,1299,1300,1301,-1,1302,1303,1304,-1,1305,1306,1307,-1,1308,1309,1310,-1,1311,1312,1313,-1,1314,1315,1316,-1,1317,1318,1319,-1,1320,1321,1322,-1,1323,1324,1325,-1,1326,1327,1328,-1,1329,1330,1331,-1,1332,1333,1334,-1,1335,1336,1337,-1,1338,1339,1340,-1,1341,1342,1343,-1,1344,1345,1346,-1,1347,1348,1349,-1,1350,1351,1352,-1,1353,1354,1355,-1,1356,1357,1358,-1,1359,1360,1361,-1,1362,1363,1364,-1,1365,1366,1367,-1,1368,1369,1370,-1,1371,1372,1373,-1,1374,1375,1376,-1,1377,1378,1379,-1,1380,1381,1382,-1,1383,1384,1385,-1,1386,1387,1388,-1,1389,1390,1391,-1,1392,1393,1394,-1,1395,1396,1397,-1,1398,1399,1400,-1,1401,1402,1403,-1,1404,1405,1406,-1,1407,1408,1409,-1,1410,1411,1412,-1,1413,1414,1415,-1,1416,1417,1418,-1,1419,1420,1421,-1,1422,1423,1424,-1,1425,1426,1427,-1,1428,1429,1430,-1,1431,1432,1433,-1,1434,1435,1436,-1,1437,1438,1439,-1,1440,1441,1442,-1,1443,1444,1445,-1,1446,1447,1448,-1,1449,1450,1451,-1,1452,1453,1454,-1,1455,1456,1457,-1,1458,1459,1460,-1,1461,1462,1463,-1,1464,1465,1466,-1,1467,1468,1469,-1,1470,1471,1472,-1,1473,1474,1475,-1,1476,1477,1478,-1,1479,1480,1481,-1,1482,1483,1484,-1,1485,1486,1487,-1,1488,1489,1490,-1,1491,1492,1493,-1,1494,1495,1496,-1,1497,1498,1499,-1,1500,1501,1502,-1,1503,1504,1505,-1,1506,1507,1508,-1,1509,1510,1511,-1,1512,1513,1514,-1,1515,1516,1517,-1,1518,1519,1520,-1,1521,1522,1523,-1,1524,1525,1526,-1,1527,1528,1529,-1,1530,1531,1532,-1,1533,1534,1535,-1,1536,1537,1538,-1,1539,1540,1541,-1,1542,1543,1544,-1,1545,1546,1547,-1,1548,1549,1550,-1,1551,1552,1553,-1,1554,1555,1556,-1,1557,1558,1559,-1,1560,1561,1562,-1,1563,1564,1565,-1,1566,1567,1568,-1,1569,1570,1571,-1,1572,1573,1574,-1,1575,1576,1577,-1,1578,1579,1580,-1,1581,1582,1583,-1,1584,1585,1586,-1,1587,1588,1589,-1,1590,1591,1592,-1,1593,1594,1595,-1,1596,1597,1598,-1,1599,1600,1601,-1,1602,1603,1604,-1,1605,1606,1607,-1,1608,1609,1610,-1,1611,1612,1613,-1,1614,1615,1616,-1,1617,1618,1619,-1,1620,1621,1622,-1,1623,1624,1625,-1,1626,1627,1628,-1,1629,1630,1631,-1,1632,1633,1634,-1,1635,1636,1637,-1,1638,1639,1640,-1,1641,1642,1643,-1,1644,1645,1646,-1,1647,1648,1649,-1,1650,1651,1652,-1,1653,1654,1655,-1,1656,1657,1658,-1,1659,1660,1661,-1,1662,1663,1664,-1,1665,1666,1667,-1,1668,1669,1670,-1,1671,1672,1673,-1,1674,1675,1676,-1,1677,1678,1679,-1,1680,1681,1682,-1,1683,1684,1685,-1,1686,1687,1688,-1,1689,1690,1691,-1,1692,1693,1694,-1,1695,1696,1697,-1,1698,1699,1700,-1,1701,1702,1703,-1,1704,1705,1706,-1,1707,1708,1709,-1,1710,1711,1712,-1,1713,1714,1715,-1,1716,1717,1718,-1,1719,1720,1721,-1,1722,1723,1724,-1,1725,1726,1727,-1,1728,1729,1730,-1,1731,1732,1733,-1,1734,1735,1736,-1,1737,1738,1739,-1,1740,1741,1742,-1,1743,1744,1745,-1,1746,1747,1748,-1,1749,1750,1751,-1,1752,1753,1754,-1,1755,1756,1757,-1,1758,1759,1760,-1,1761,1762,1763,-1,1764,1765,1766,-1,1767,1768,1769,-1,1770,1771,1772,-1,1773,1774,1775,-1,1776,1777,1778,-1,1779,1780,1781,-1,1782,1783,1784,-1,1785,1786,1787,-1,1788,1789,1790,-1,1791,1792,1793,-1,1794,1795,1796,-1,1797,1798,1799,-1,1800,1801,1802,-1,1803,1804,1805,-1,1806,1807,1808,-1,1809,1810,1811,-1,1812,1813,1814,-1,1815,1816,1817,-1,1818,1819,1820,-1,1821,1822,1823,-1,1824,1825,1826,-1,1827,1828,1829,-1,1830,1831,1832,-1,1833,1834,1835,-1,1836,1837,1838,-1,1839,1840,1841,-1,1842,1843,1844,-1,1845,1846,1847,-1,1848,1849,1850,-1,1851,1852,1853,-1,1854,1855,1856,-1,1857,1858,1859,-1,1860,1861,1862,-1,1863,1864,1865,-1,1866,1867,1868,-1,1869,1870,1871,-1,1872,1873,1874,-1,1875,1876,1877,-1,1878,1879,1880,-1,1881,1882,1883,-1,1884,1885,1886,-1,1887,1888,1889,-1,1890,1891,1892,-1,1893,1894,1895,-1,1896,1897,1898,-1,1899,1900,1901,-1,1902,1903,1904,-1,1905,1906,1907,-1,1908,1909,1910,-1,1911,1912,1913,-1,1914,1915,1916,-1,1917,1918,1919,-1,1920,1921,1922,-1,1923,1924,1925,-1,1926,1927,1928,-1,1929,1930,1931,-1,1932,1933,1934,-1,1935,1936,1937,-1,1938,1939,1940,-1,1941,1942,1943,-1,1944,1945,1946,-1,1947,1948,1949,-1,1950,1951,1952,-1,1953,1954,1955,-1,1956,1957,1958,-1,1959,1960,1961,-1,1962,1963,1964,-1,1965,1966,1967,-1,1968,1969,1970,-1,1971,1972,1973,-1,1974,1975,1976,-1,1977,1978,1979,-1,1980,1981,1982,-1,1983,1984,1985,-1,1986,1987,1988,-1,1989,1990,1991,-1,1992,1993,1994,-1,1995,1996,1997,-1,1998,1999,2000,-1,2001,2002,2003,-1,2004,2005,2006,-1,2007,2008,2009,-1,2010,2011,2012,-1,2013,2014,2015,-1,2016,2017,2018,-1,2019,2020,2021,-1,2022,2023,2024,-1,2025,2026,2027,-1,2028,2029,2030,-1,2031,2032,2033,-1,2034,2035,2036,-1,2037,2038,2039,-1,2040,2041,2042,-1,2043,2044,2045,-1,2046,2047,2048,-1,2049,2050,2051,-1,2052,2053,2054,-1,2055,2056,2057,-1,2058,2059,2060,-1,2061,2062,2063,-1,2064,2065,2066,-1,2067,2068,2069,-1,2070,2071,2072,-1,2073,2074,2075,-1,2076,2077,2078,-1,2079,2080,2081,-1,2082,2083,2084,-1,2085,2086,2087,-1,2088,2089,2090,-1,2091,2092,2093,-1,2094,2095,2096,-1,2097,2098,2099,-1,2100,2101,2102,-1,2103,2104,2105,-1,2106,2107,2108,-1,2109,2110,2111,-1,2112,2113,2114,-1,2115,2116,2117,-1,2118,2119,2120,-1,2121,2122,2123,-1,2124,2125,2126,-1,2127,2128,2129,-1,2130,2131,2132,-1,2133,2134,2135,-1,2136,2137,2138,-1,2139,2140,2141,-1,2142,2143,2144,-1,2145,2146,2147,-1,2148,2149,2150,-1,2151,2152,2153,-1,2154,2155,2156,-1,2157,2158,2159,-1,2160,2161,2162,-1,2163,2164,2165,-1,2166,2167,2168,-1,2169,2170,2171,-1,2172,2173,2174,-1,2175,2176,2177,-1,2178,2179,2180,-1,2181,2182,2183,-1,2184,2185,2186,-1,2187,2188,2189,-1,2190,2191,2192,-1,2193,2194,2195,-1,2196,2197,2198,-1,2199,2200,2201,-1,2202,2203,2204,-1,2205,2206,2207,-1,2208,2209,2210,-1,2211,2212,2213,-1,2214,2215,2216,-1,2217,2218,2219,-1,2220,2221,2222,-1,2223,2224,2225,-1,2226,2227,2228,-1,2229,2230,2231,-1,2232,2233,2234,-1,2235,2236,2237,-1,2238,2239,2240,-1,2241,2242,2243,-1,2244,2245,2246,-1,2247,2248,2249,-1,2250,2251,2252,-1,2253,2254,2255,-1,2256,2257,2258,-1,2259,2260,2261,-1,2262,2263,2264,-1,2265,2266,2267,-1,2268,2269,2270,-1,2271,2272,2273,-1,2274,2275,2276,-1,2277,2278,2279,-1,2280,2281,2282,-1,2283,2284,2285,-1,2286,2287,2288,-1,2289,2290,2291,-1,2292,2293,2294,-1,2295,2296,2297,-1,2298,2299,2300,-1,2301,2302,2303,-1,2304,2305,2306,-1,2307,2308,2309,-1,2310,2311,2312,-1,2313,2314,2315,-1,2316,2317,2318,-1,2319,2320,2321,-1,2322,2323,2324,-1,2325,2326,2327,-1,2328,2329,2330,-1,2331,2332,2333,-1,2334,2335,2336,-1,2337,2338,2339,-1,2340,2341,2342,-1,2343,2344,2345,-1,2346,2347,2348,-1,2349,2350,2351,-1,2352,2353,2354,-1,2355,2356,2357,-1,2358,2359,2360,-1,2361,2362,2363,-1,2364,2365,2366,-1,2367,2368,2369,-1,2370,2371,2372,-1,2373,2374,2375,-1,2376,2377,2378,-1,2379,2380,2381,-1,2382,2383,2384,-1,2385,2386,2387,-1,2388,2389,2390,-1,2391,2392,2393,-1,2394,2395,2396,-1,2397,2398,2399,-1,2400,2401,2402,-1,2403,2404,2405,-1,2406,2407,2408,-1,2409,2410,2411,-1,2412,2413,2414,-1,2415,2416,2417,-1,2418,2419,2420,-1,2421,2422,2423,-1,2424,2425,2426,-1,2427,2428,2429,-1,2430,2431,2432,-1,2433,2434,2435,-1,2436,2437,2438,-1,2439,2440,2441,-1,2442,2443,2444,-1,2445,2446,2447,-1,2448,2449,2450,-1,2451,2452,2453,-1,2454,2455,2456,-1,2457,2458,2459,-1,2460,2461,2462,-1,2463,2464,2465,-1,2466,2467,2468,-1,2469,2470,2471,-1,2472,2473,2474,-1,2475,2476,2477,-1,2478,2479,2480,-1,2481,2482,2483,-1,2484,2485,2486,-1,2487,2488,2489,-1,2490,2491,2492,-1,2493,2494,2495,-1,2496,2497,2498,-1,2499,2500,2501,-1,2502,2503,2504,-1,2505,2506,2507,-1,2508,2509,2510,-1,2511,2512,2513,-1,2514,2515,2516,-1,2517,2518,2519,-1,2520,2521,2522,-1,2523,2524,2525,-1,2526,2527,2528,-1,2529,2530,2531,-1,2532,2533,2534,-1,2535,2536,2537,-1,2538,2539,2540,-1,2541,2542,2543,-1,2544,2545,2546,-1,2547,2548,2549,-1,2550,2551,2552,-1,2553,2554,2555,-1,2556,2557,2558,-1,2559,2560,2561,-1,2562,2563,2564,-1,2565,2566,2567,-1,2568,2569,2570,-1,2571,2572,2573,-1,2574,2575,2576,-1,2577,2578,2579,-1,2580,2581,2582,-1,2583,2584,2585,-1,2586,2587,2588,-1,2589,2590,2591,-1,2592,2593,2594,-1,2595,2596,2597,-1,2598,2599,2600,-1,2601,2602,2603,-1,2604,2605,2606,-1,2607,2608,2609,-1,2610,2611,2612,-1,2613,2614,2615,-1,2616,2617,2618,-1,2619,2620,2621,-1,2622,2623,2624,-1,2625,2626,2627,-1,2628,2629,2630,-1,2631,2632,2633,-1,2634,2635,2636,-1,2637,2638,2639,-1,2640,2641,2642,-1,2643,2644,2645,-1,2646,2647,2648,-1,2649,2650,2651,-1,2652,2653,2654,-1,2655,2656,2657,-1,2658,2659,2660,-1,2661,2662,2663,-1,2664,2665,2666,-1,2667,2668,2669,-1,2670,2671,2672,-1,2673,2674,2675,-1,2676,2677,2678,-1,2679,2680,2681,-1,2682,2683,2684,-1,2685,2686,2687,-1,2688,2689,2690,-1,2691,2692,2693,-1,2694,2695,2696,-1,2697,2698,2699,-1,2700,2701,2702,-1,2703,2704,2705,-1,2706,2707,2708,-1,2709,2710,2711,-1,2712,2713,2714,-1,2715,2716,2717,-1,2718,2719,2720,-1,2721,2722,2723,-1,2724,2725,2726,-1,2727,2728,2729,-1,2730,2731,2732,-1,2733,2734,2735,-1,2736,2737,2738,-1,2739,2740,2741,-1,2742,2743,2744,-1,2745,2746,2747,-1,2748,2749,2750,-1,2751,2752,2753,-1,2754,2755,2756,-1,2757,2758,2759,-1,2760,2761,2762,-1,2763,2764,2765,-1,2766,2767,2768,-1,2769,2770,2771,-1,2772,2773,2774,-1,2775,2776,2777,-1,2778,2779,2780,-1,2781,2782,2783,-1,2784,2785,2786,-1,2787,2788,2789,-1,2790,2791,2792,-1,2793,2794,2795,-1,2796,2797,2798,-1,2799,2800,2801,-1,2802,2803,2804,-1,2805,2806,2807,-1,2808,2809,2810,-1,2811,2812,2813,-1,2814,2815,2816,-1,2817,2818,2819,-1,2820,2821,2822,-1,2823,2824,2825,-1,2826,2827,2828,-1,2829,2830,2831,-1,2832,2833,2834,-1,2835,2836,2837,-1,2838,2839,2840,-1,2841,2842,2843,-1,2844,2845,2846,-1,2847,2848,2849,-1,2850,2851,2852,-1,2853,2854,2855,-1,2856,2857,2858,-1,2859,2860,2861,-1,2862,2863,2864,-1,2865,2866,2867,-1,2868,2869,2870,-1,2871,2872,2873,-1,2874,2875,2876,-1,2877,2878,2879,-1,2880,2881,2882,-1,2883,2884,2885,-1,2886,2887,2888,-1,2889,2890,2891,-1,2892,2893,2894,-1,2895,2896,2897,-1,2898,2899,2900,-1,2901,2902,2903,-1,2904,2905,2906,-1,2907,2908,2909,-1,2910,2911,2912,-1,2913,2914,2915,-1,2916,2917,2918,-1,2919,2920,2921,-1,2922,2923,2924,-1,2925,2926,2927,-1,2928,2929,2930,-1,2931,2932,2933,-1,2934,2935,2936,-1,2937,2938,2939,-1,2940,2941,2942,-1,2943,2944,2945,-1,2946,2947,2948,-1,2949,2950,2951,-1,2952,2953,2954,-1,2955,2956,2957,-1,2958,2959,2960,-1,2961,2962,2963,-1,2964,2965,2966,-1,2967,2968,2969,-1,2970,2971,2972,-1,2973,2974,2975,-1,2976,2977,2978,-1,2979,2980,2981,-1,2982,2983,2984,-1,2985,2986,2987,-1,2988,2989,2990,-1,2991,2992,2993,-1,2994,2995,2996,-1,2997,2998,2999,-1]
IndexedFaceSet310.creaseAngle = 1.14
Coordinate311 = x3d.Coordinate()

IndexedFaceSet310.coord = Coordinate311

Shape306.geometry = IndexedFaceSet310

Transform305.children.append(Shape306)

fieldValue304.children.append(Transform305)

ProtoInstance302.fieldValue.append(fieldValue304)

fieldValue301.children.append(ProtoInstance302)
ProtoInstance312 = x3d.ProtoInstance()
ProtoInstance312.name = "Joint"
ProtoInstance312.DEF = "Allen_hanim_l_hip"
fieldValue313 = x3d.fieldValue()
fieldValue313.name = "name"
fieldValue313.value = "l_hip"

ProtoInstance312.fieldValue.append(fieldValue313)
fieldValue314 = x3d.fieldValue()
fieldValue314.name = "center"
fieldValue314.value = "0.122 0.888271 -0.0693267"

ProtoInstance312.fieldValue.append(fieldValue314)
fieldValue315 = x3d.fieldValue()
fieldValue315.name = "children"
ProtoInstance316 = x3d.ProtoInstance()
ProtoInstance316.name = "Segment"
ProtoInstance316.DEF = "Allen_hanim_l_thigh"
fieldValue317 = x3d.fieldValue()
fieldValue317.name = "name"
fieldValue317.value = "l_thigh"

ProtoInstance316.fieldValue.append(fieldValue317)
fieldValue318 = x3d.fieldValue()
fieldValue318.name = "children"
Transform319 = x3d.Transform()
Transform319.DEF = "l_thigh_adjust"
Transform319.center = [-0.7,1.1,0.04]
Transform319.rotation = [0,1,0,1.570796]
Transform319.scale = [0.1,0.1,0.1]
Shape320 = x3d.Shape()
Appearance321 = x3d.Appearance()
Material322 = x3d.Material()
Material322.USE = "Pants_Color"

Appearance321.material = Material322
ImageTexture323 = x3d.ImageTexture()
ImageTexture323.USE = "camo"

Appearance321.texture = ImageTexture323

Shape320.appearance = Appearance321
IndexedFaceSet324 = x3d.IndexedFaceSet()
IndexedFaceSet324.coordIndex = [0,1,2,-1,3,4,5,-1,6,7,8,-1,9,10,11,-1,12,13,14,-1,15,16,17,-1,18,19,20,-1,21,22,23,-1,24,25,26,-1,27,28,29,-1,30,31,32,-1,33,34,35,-1,36,37,38,-1,39,40,41,-1,42,43,44,-1,45,46,47,-1,48,49,50,-1,51,52,53,-1,54,55,56,-1,57,58,59,-1,60,61,62,-1,63,64,65,-1,66,67,68,-1,69,70,71,-1,72,73,74,-1,75,76,77,-1,78,79,80,-1,81,82,83,-1,84,85,86,-1,87,88,89,-1,90,91,92,-1,93,94,95,-1,96,97,98,-1,99,100,101,-1,102,103,104,-1,105,106,107,-1,108,109,110,-1,111,112,113,-1,114,115,116,-1,117,118,119,-1,120,121,122,-1,123,124,125,-1,126,127,128,-1,129,130,131,-1,132,133,134,-1,135,136,137,-1,138,139,140,-1,141,142,143,-1,144,145,146,-1,147,148,149,-1,150,151,152,-1,153,154,155,-1,156,157,158,-1,159,160,161,-1,162,163,164,-1,165,166,167,-1,168,169,170,-1,171,172,173,-1,174,175,176,-1,177,178,179,-1,180,181,182,-1,183,184,185,-1,181,183,182,-1,183,185,182,-1,183,158,184,-1,157,159,158,-1,164,165,162,-1,167,168,165,-1,165,168,162,-1,172,174,173,-1,176,179,174,-1,174,179,173,-1,179,178,173,-1,182,185,178,-1,178,185,173,-1,185,184,173,-1,184,158,173,-1,158,159,173,-1,170,173,168,-1,159,161,173,-1,173,161,168,-1,162,168,161,-1,186,187,188,-1,189,190,191,-1,192,193,194,-1,195,196,197,-1,198,199,200,-1,201,202,203,-1,204,205,206,-1,207,208,209,-1,210,211,212,-1,213,214,215,-1,216,217,218,-1,219,220,221,-1,222,223,224,-1,225,226,227,-1,228,229,230,-1,231,232,233,-1,234,235,236,-1,237,238,239,-1,240,241,242,-1,243,244,245,-1,246,247,248,-1,249,250,251,-1,252,253,254,-1,255,256,257,-1,258,259,260,-1,261,262,263,-1,264,265,266,-1,267,268,269,-1,270,271,272,-1,273,274,275,-1,276,277,278,-1,279,280,281,-1,282,283,284,-1,285,286,287,-1,288,289,290,-1,291,292,293,-1,294,295,296,-1,297,298,299,-1,300,301,302,-1,303,304,305,-1,306,307,308,-1,309,310,311,-1,312,313,314,-1,315,316,317,-1,318,319,320,-1,321,322,323,-1,324,325,326,-1,327,328,329,-1,330,331,332,-1,333,334,335,-1,336,337,338,-1,339,340,341,-1,342,343,344,-1,345,346,347,-1,348,349,350,-1,351,352,353,-1,354,355,356,-1,357,358,359,-1,360,361,362,-1,363,364,365,-1,366,367,368,-1,369,370,371,-1,372,373,374,-1,375,376,377,-1,378,379,380,-1,381,382,383,-1,384,385,386,-1,387,388,389,-1,390,391,392,-1,393,394,395,-1,396,397,398,-1,399,400,401,-1,402,403,404,-1,405,406,407,-1,408,409,410,-1,411,412,413,-1,414,415,416,-1,417,418,419,-1,420,421,422,-1,423,424,425,-1,426,427,428,-1,429,430,431,-1,432,433,434,-1,435,436,437,-1,438,439,440,-1,441,442,443,-1,444,445,446,-1,447,448,449,-1,450,451,452,-1,453,454,455,-1,456,457,458,-1,459,460,461,-1,462,463,464,-1,465,466,467,-1,468,469,470,-1,471,472,473,-1,474,475,476,-1,477,478,479,-1,480,481,482,-1,483,484,485,-1,486,487,488,-1,489,490,491,-1,492,493,494,-1,495,496,497,-1,498,499,500,-1,501,502,503,-1,504,505,506,-1,507,508,509,-1,510,511,512,-1,513,514,515,-1,516,517,518,-1,519,520,521,-1,522,523,524,-1,525,526,527,-1,528,529,530,-1,531,532,533,-1,534,535,536,-1,537,538,539,-1,540,541,542,-1,543,544,545,-1,546,547,548,-1,549,550,551,-1,552,553,554,-1,555,556,557,-1,558,559,560,-1,561,562,563,-1,564,565,566,-1,567,568,569,-1,570,571,572,-1,573,574,575,-1,576,577,578,-1,579,580,581,-1,582,583,584,-1,585,586,587,-1,588,589,590,-1,591,592,593,-1,594,595,596,-1,597,598,599,-1,600,601,602,-1,603,604,605,-1,606,607,608,-1,609,610,611,-1,612,613,614,-1,615,616,617,-1,618,619,620,-1,621,622,623,-1,624,625,626,-1,627,628,629,-1,630,631,632,-1,633,634,635,-1,636,637,638,-1,639,640,641,-1,642,643,644,-1,645,646,647,-1,648,649,650,-1,651,652,653,-1,654,655,656,-1,657,658,659,-1,660,661,662,-1,663,664,665,-1,666,667,668,-1,669,670,671,-1,672,673,674,-1,675,676,677,-1,678,679,680,-1,681,682,683,-1,684,685,686,-1,687,688,689,-1,690,691,692,-1,693,694,695,-1,696,697,698,-1,699,700,701,-1,702,703,704,-1,705,706,707,-1,708,709,710,-1,711,712,713,-1,714,715,716,-1,717,718,719,-1,720,721,722,-1,723,724,725,-1,726,727,728,-1,729,730,731,-1,732,733,734,-1,735,736,737,-1,738,739,740,-1,741,742,743,-1,744,745,746,-1,747,748,749,-1,750,751,752,-1,753,754,755,-1,756,757,758,-1,759,760,761,-1,762,763,764,-1,765,766,767,-1,768,769,770,-1,771,772,773,-1,774,775,776,-1,777,778,779,-1,780,781,782,-1,783,784,785,-1,786,787,788,-1,789,790,791,-1,792,793,794,-1,795,796,797,-1,798,799,800,-1,801,802,803,-1,804,805,806,-1,807,808,809,-1,810,811,812,-1,813,814,815,-1,816,817,818,-1,819,820,821,-1,822,823,824,-1,825,826,827,-1,828,829,830,-1,831,832,833,-1,834,835,836,-1,837,838,839,-1,840,841,842,-1,843,844,845,-1,846,847,848,-1,849,850,851,-1,852,853,854,-1,855,856,857,-1,858,859,860,-1,861,862,863,-1,864,865,866,-1,867,868,869,-1,870,871,872,-1,873,874,875,-1,876,877,878,-1,879,880,881,-1,882,883,884,-1,885,886,887,-1,888,889,890,-1,891,892,893,-1,894,895,896,-1,897,898,899,-1,900,901,902,-1,903,904,905,-1,906,907,908,-1,909,910,911,-1,912,913,914,-1,915,916,917,-1,918,919,920,-1,921,922,923,-1,924,925,926,-1,927,928,929,-1,930,931,932,-1,933,934,935,-1,936,937,938,-1,939,940,941,-1,942,943,944,-1,945,946,947,-1,948,949,950,-1,951,952,953,-1,954,955,956,-1,957,958,959,-1,960,961,962,-1,963,964,965,-1,966,967,968,-1,969,970,971,-1,972,973,974,-1,975,976,977,-1,978,979,980,-1,981,982,983,-1,984,985,986,-1,987,988,989,-1,990,991,992,-1,993,994,995,-1,996,997,998,-1,999,1000,1001,-1,1002,1003,1004,-1,1005,1006,1007,-1,1008,1009,1010,-1,1011,1012,1013,-1,1014,1015,1016,-1,1017,1018,1019,-1,1020,1021,1022,-1,1023,1024,1025,-1,1026,1027,1028,-1,1029,1030,1031,-1,1032,1033,1034,-1,1035,1036,1037,-1,1038,1039,1040,-1,1041,1042,1043,-1,1044,1045,1046,-1,1047,1048,1049,-1,1050,1051,1052,-1,1053,1054,1055,-1,1056,1057,1058,-1,1059,1060,1061,-1,1062,1063,1064,-1,1065,1066,1067,-1,1068,1069,1070,-1,1071,1072,1073,-1,1074,1075,1076,-1,1077,1078,1079,-1,1080,1081,1082,-1,1083,1084,1085,-1,1086,1087,1088,-1,1089,1090,1091,-1,1092,1093,1094,-1,1095,1096,1097,-1,1098,1099,1100,-1,1101,1102,1103,-1,1104,1105,1106,-1,1107,1108,1109,-1,1110,1111,1112,-1,1113,1114,1115,-1,1116,1117,1118,-1,1119,1120,1121,-1,1122,1123,1124,-1,1125,1126,1127,-1,1128,1129,1130,-1,1131,1132,1133,-1,1134,1135,1136,-1,1137,1138,1139,-1,1140,1141,1142,-1,1143,1144,1145,-1,1146,1147,1148,-1,1149,1150,1151,-1,1152,1153,1154,-1,1155,1156,1157,-1,1158,1159,1160,-1,1161,1162,1163,-1,1164,1165,1166,-1,1167,1168,1169,-1,1170,1171,1172,-1,1173,1174,1175,-1,1176,1177,1178,-1,1179,1180,1181,-1,1182,1183,1184,-1,1185,1186,1187,-1,1188,1189,1190,-1,1191,1192,1193,-1,1194,1195,1196,-1,1197,1198,1199,-1,1200,1201,1202,-1,1203,1204,1205,-1,1206,1207,1208,-1,1209,1210,1211,-1,1212,1213,1214,-1,1215,1216,1217,-1,1218,1219,1220,-1,1221,1222,1223,-1,1224,1225,1226,-1,1227,1228,1229,-1,1230,1231,1232,-1,1233,1234,1235,-1,1236,1237,1238,-1,1239,1240,1241,-1,1242,1243,1244,-1,1245,1246,1247,-1,1248,1249,1250,-1,1251,1252,1253,-1,1254,1255,1256,-1,1257,1258,1259,-1,1260,1261,1262,-1,1263,1264,1265,-1,1266,1267,1268,-1,1269,1270,1271,-1,1272,1273,1274,-1,1275,1276,1277,-1,1278,1279,1280,-1,1281,1282,1283,-1,1284,1285,1286,-1,1287,1288,1289,-1,1290,1291,1292,-1,1293,1294,1295,-1,1296,1297,1298,-1,1299,1300,1301,-1,1302,1303,1304,-1,1305,1306,1307,-1,1308,1309,1310,-1,1311,1312,1313,-1,1314,1315,1316,-1,1317,1318,1319,-1,1320,1321,1322,-1,1323,1324,1325,-1,1326,1327,1328,-1,1329,1330,1331,-1,1332,1333,1334,-1,1335,1336,1337,-1,1338,1339,1340,-1,1341,1342,1343,-1,1344,1345,1346,-1,1347,1348,1349,-1,1350,1351,1352,-1,1353,1354,1355,-1,1356,1357,1358,-1,1359,1360,1361,-1,1362,1363,1364,-1,1365,1366,1367,-1,1368,1369,1370,-1,1371,1372,1373,-1,1374,1375,1376,-1,1377,1378,1379,-1,1380,1381,1382,-1,1383,1384,1385,-1,1386,1387,1388,-1,1389,1390,1391,-1,1392,1393,1394,-1,1395,1396,1397,-1,1398,1399,1400,-1,1401,1402,1403,-1,1404,1405,1406,-1,1407,1408,1409,-1,1410,1411,1412,-1,1413,1414,1415,-1,1416,1417,1418,-1,1419,1420,1421,-1,1422,1423,1424,-1,1425,1426,1427,-1,1428,1429,1430,-1,1431,1432,1433,-1,1434,1435,1436,-1,1437,1438,1439,-1,1440,1441,1442,-1,1443,1444,1445,-1,1446,1447,1448,-1,1449,1450,1451,-1,1452,1453,1454,-1,1455,1456,1457,-1,1458,1459,1460,-1,1461,1462,1463,-1,1464,1465,1466,-1,1467,1468,1469,-1,1470,1471,1472,-1,1473,1474,1475,-1,1476,1477,1478,-1,1479,1480,1481,-1,1482,1483,1484,-1,1485,1486,1487,-1,1488,1489,1490,-1,1491,1492,1493,-1,1494,1495,1496,-1,1497,1498,1499,-1,1500,1501,1502,-1,1503,1504,1505,-1,1506,1507,1508,-1,1509,1510,1511,-1,1512,1513,1514,-1,1515,1516,1517,-1,1518,1519,1520,-1,1521,1522,1523,-1,1524,1525,1526,-1,1527,1528,1529,-1,1530,1531,1532,-1,1533,1534,1535,-1,1536,1537,1538,-1,1539,1540,1541,-1,1542,1543,1544,-1,1545,1546,1547,-1,1548,1549,1550,-1]
IndexedFaceSet324.creaseAngle = 1.32
Coordinate325 = x3d.Coordinate()

IndexedFaceSet324.coord = Coordinate325

Shape320.geometry = IndexedFaceSet324

Transform319.children.append(Shape320)

fieldValue318.children.append(Transform319)

ProtoInstance316.fieldValue.append(fieldValue318)

fieldValue315.children.append(ProtoInstance316)
ProtoInstance326 = x3d.ProtoInstance()
ProtoInstance326.name = "Joint"
ProtoInstance326.DEF = "Allen_hanim_l_knee"
fieldValue327 = x3d.fieldValue()
fieldValue327.name = "name"
fieldValue327.value = "l_knee"

ProtoInstance326.fieldValue.append(fieldValue327)
fieldValue328 = x3d.fieldValue()
fieldValue328.name = "center"
fieldValue328.value = "0.0738 0.517 -0.0284"

ProtoInstance326.fieldValue.append(fieldValue328)
fieldValue329 = x3d.fieldValue()
fieldValue329.name = "children"
ProtoInstance330 = x3d.ProtoInstance()
ProtoInstance330.name = "Segment"
ProtoInstance330.DEF = "Allen_hanim_l_calf"
fieldValue331 = x3d.fieldValue()
fieldValue331.name = "name"
fieldValue331.value = "l_calf"

ProtoInstance330.fieldValue.append(fieldValue331)
fieldValue332 = x3d.fieldValue()
fieldValue332.name = "children"
Transform333 = x3d.Transform()
Transform333.DEF = "l_calf_adjust"
Transform333.center = [-0.012,1.1,-0.01]
Transform333.rotation = [0,1,0,1.570796]
Transform333.scale = [0.1,0.1,0.1]
Shape334 = x3d.Shape()
Appearance335 = x3d.Appearance()
Material336 = x3d.Material()
Material336.USE = "Pants_Color"

Appearance335.material = Material336
ImageTexture337 = x3d.ImageTexture()
ImageTexture337.USE = "camo"

Appearance335.texture = ImageTexture337

Shape334.appearance = Appearance335
IndexedFaceSet338 = x3d.IndexedFaceSet()
IndexedFaceSet338.coordIndex = [4,5,2,-1,19,13,20,-1,20,13,12,-1,14,21,9,-1,22,23,24,-1,4,0,28,-1,29,15,6,-1,30,6,16,-1,30,29,6,-1,18,17,31,-1,11,27,26,-1,27,10,3,-1,33,34,23,-1,22,33,23,-1,35,36,37,-1,38,39,40,-1,38,18,39,-1,18,31,41,-1,42,13,19,-1,43,44,19,-1,9,45,46,-1,23,47,24,-1,29,30,48,-1,16,49,30,-1,50,51,52,-1,51,50,53,-1,35,37,54,-1,36,55,56,-1,36,35,55,-1,57,55,35,-1,39,57,40,-1,39,58,55,-1,59,41,60,-1,3,2,5,-1,61,22,24,-1,34,62,23,-1,48,63,62,-1,16,8,49,-1,7,25,52,-1,7,52,64,-1,65,64,51,-1,53,37,36,-1,50,37,53,-1,56,55,58,-1,66,56,58,-1,41,27,60,-1,39,18,41,-1,31,26,27,-1,59,60,67,-1,4,68,5,-1,69,68,4,-1,32,44,28,-1,43,19,20,-1,61,21,14,-1,47,70,21,-1,47,23,70,-1,62,63,23,-1,8,71,49,-1,57,39,55,-1,72,43,20,-1,22,61,14,-1,61,24,47,-1,63,73,23,-1,29,48,62,-1,52,51,64,-1,74,66,58,-1,58,59,67,-1,1,46,20,-1,75,70,76,-1,61,47,21,-1,70,73,77,-1,8,7,71,-1,71,7,64,-1,65,51,78,-1,51,79,78,-1,49,71,80,-1,81,51,53,-1,74,82,66,-1,66,83,56,-1,59,58,39,-1,9,21,45,-1,49,80,84,-1,85,86,74,-1,60,27,3,-1,69,4,28,-1,43,72,87,-1,88,89,75,-1,90,63,91,-1,78,84,80,-1,65,78,80,-1,51,81,79,-1,92,79,81,-1,93,92,81,-1,94,84,78,-1,94,78,79,-1,94,95,96,-1,94,92,95,-1,94,79,92,-1,92,93,95,-1,93,74,86,-1,97,60,3,-1,98,99,100,-1,45,21,70,-1,101,77,90,-1,23,73,70,-1,84,102,49,-1,95,93,86,-1,97,68,103,-1,68,3,5,-1,1,9,46,-1,104,98,89,-1,75,89,100,-1,75,45,70,-1,84,105,102,-1,106,323,107,-1,39,41,59,-1,58,67,108,-1,68,97,3,-1,100,99,46,-1,76,77,101,-1,63,48,91,-1,49,102,109,-1,110,98,104,-1,87,111,112,-1,104,89,112,-1,77,73,90,-1,113,102,105,-1,113,105,106,-1,106,107,113,-1,68,69,103,-1,46,99,20,-1,114,86,115,-1,115,85,116,-1,69,28,43,-1,99,72,20,-1,72,111,87,-1,117,112,89,-1,88,118,119,-1,45,100,46,-1,120,101,90,-1,109,48,30,-1,113,107,121,-1,113,121,122,-1,115,121,107,-1,122,121,123,-1,121,115,123,-1,123,115,116,-1,115,86,85,-1,28,44,43,-1,98,100,89,-1,117,89,88,-1,118,124,125,-1,88,75,76,-1,45,75,100,-1,73,63,90,-1,126,90,91,-1,91,127,128,-1,127,129,128,-1,49,109,30,-1,127,122,130,-1,130,122,123,-1,131,108,132,-1,133,131,134,-1,85,74,58,-1,131,133,108,-1,133,135,116,-1,111,104,112,-1,76,101,124,-1,136,126,91,-1,137,116,135,-1,133,116,85,-1,138,139,140,-1,141,87,112,-1,142,69,87,-1,70,77,76,-1,120,90,126,-1,101,120,124,-1,48,109,91,-1,102,143,109,-1,109,143,127,-1,144,135,145,-1,134,145,133,-1,108,85,58,-1,133,85,108,-1,41,31,27,-1,67,60,97,-1,143,122,127,-1,146,130,324,-1,146,127,130,-1,145,135,133,-1,67,140,147,-1,141,112,117,-1,120,148,125,-1,149,150,128,-1,151,134,152,-1,152,131,153,-1,103,67,97,-1,87,69,43,-1,126,148,120,-1,91,109,127,-1,154,129,146,-1,154,146,153,-1,129,149,128,-1,129,127,146,-1,147,155,132,-1,156,157,103,-1,156,103,69,-1,119,158,141,-1,120,125,124,-1,126,136,148,-1,136,150,159,-1,146,152,153,-1,142,156,69,-1,125,160,161,-1,160,136,159,-1,131,152,134,-1,147,132,108,-1,132,162,163,-1,138,140,67,-1,156,164,157,-1,165,118,125,-1,125,148,160,-1,160,166,161,-1,136,128,150,-1,162,167,163,-1,139,168,169,-1,142,170,156,-1,141,142,87,-1,88,119,117,-1,91,128,136,-1,159,150,171,-1,163,172,153,-1,163,153,131,-1,131,132,163,-1,140,155,147,-1,117,119,141,-1,148,136,160,-1,154,171,149,-1,172,173,154,-1,167,172,163,-1,174,175,162,-1,138,67,157,-1,170,164,156,-1,118,76,124,-1,160,159,176,-1,171,177,178,-1,154,173,171,-1,172,154,153,-1,179,162,180,-1,67,147,108,-1,138,157,164,-1,119,118,158,-1,165,161,181,-1,165,125,161,-1,165,181,182,-1,171,150,149,-1,183,167,184,-1,162,184,167,-1,159,185,176,-1,171,173,186,-1,187,184,188,-1,188,162,179,-1,188,179,189,-1,162,175,180,-1,139,138,168,-1,190,170,142,-1,171,186,189,-1,186,188,189,-1,178,159,171,-1,191,189,179,-1,191,177,189,-1,171,189,177,-1,132,174,162,-1,175,174,192,-1,139,169,193,-1,178,185,159,-1,160,176,166,-1,191,194,177,-1,191,179,195,-1,188,184,162,-1,140,139,155,-1,103,157,67,-1,164,170,168,-1,190,141,158,-1,196,158,118,-1,194,191,195,-1,180,197,198,-1,174,193,192,-1,170,199,200,-1,190,158,201,-1,202,176,185,-1,203,185,178,-1,203,204,202,-1,205,204,195,-1,204,203,195,-1,175,192,206,-1,174,155,193,-1,161,207,181,-1,208,195,198,-1,195,179,198,-1,169,200,209,-1,202,185,203,-1,208,205,195,-1,205,208,210,-1,198,179,180,-1,211,212,197,-1,166,207,161,-1,213,176,202,-1,202,204,213,-1,210,214,205,-1,210,208,212,-1,207,215,181,-1,176,216,166,-1,212,217,197,-1,211,197,180,-1,174,132,155,-1,139,193,155,-1,138,164,168,-1,182,218,165,-1,219,214,210,-1,219,212,211,-1,141,190,142,-1,170,200,168,-1,190,199,170,-1,216,220,166,-1,213,214,216,-1,221,222,223,-1,222,219,211,-1,219,210,212,-1,180,175,211,-1,201,224,225,-1,226,227,228,-1,196,201,158,-1,201,196,226,-1,220,215,207,-1,176,213,216,-1,220,216,219,-1,175,206,211,-1,193,229,192,-1,169,168,200,-1,196,118,165,-1,230,231,232,-1,118,88,76,-1,231,220,221,-1,166,220,207,-1,220,219,221,-1,225,233,234,-1,235,224,236,-1,231,215,220,-1,199,234,200,-1,201,226,224,-1,237,192,229,-1,218,196,165,-1,222,211,238,-1,190,201,225,-1,239,240,206,-1,229,193,169,-1,199,225,234,-1,224,241,225,-1,226,218,227,-1,226,196,218,-1,218,182,227,-1,230,242,243,-1,230,181,215,-1,221,219,222,-1,231,221,244,-1,182,243,227,-1,216,214,219,-1,192,237,206,-1,182,181,230,-1,245,223,246,-1,232,231,244,-1,209,229,169,-1,209,247,229,-1,200,234,209,-1,233,225,241,-1,230,232,242,-1,230,215,231,-1,232,244,248,-1,223,222,246,-1,249,239,229,-1,234,247,209,-1,235,250,251,-1,235,236,250,-1,243,182,230,-1,206,238,211,-1,226,228,252,-1,228,253,254,-1,190,225,199,-1,255,256,242,-1,244,255,248,-1,223,245,257,-1,234,233,247,-1,224,226,252,-1,232,248,242,-1,258,229,247,-1,223,244,221,-1,222,238,246,-1,259,260,240,-1,238,240,246,-1,240,239,261,-1,256,255,257,-1,260,246,240,-1,238,206,240,-1,239,237,229,-1,235,233,241,-1,239,206,237,-1,243,262,263,-1,249,229,264,-1,258,264,229,-1,258,251,264,-1,235,258,247,-1,242,262,243,-1,265,266,267,-1,268,245,267,-1,249,269,261,-1,268,256,257,-1,260,270,245,-1,243,263,227,-1,228,263,253,-1,255,242,248,-1,251,271,264,-1,233,235,247,-1,228,254,272,-1,268,267,262,-1,223,257,255,-1,273,274,271,-1,275,276,252,-1,256,268,262,-1,223,255,244,-1,259,240,261,-1,261,269,277,-1,278,249,264,-1,279,280,236,-1,280,250,236,-1,236,224,252,-1,261,277,259,-1,264,271,278,-1,274,278,271,-1,235,251,258,-1,273,271,281,-1,276,236,252,-1,262,282,283,-1,260,245,246,-1,274,284,278,-1,235,241,224,-1,228,227,263,-1,284,274,285,-1,273,285,274,-1,279,236,276,-1,286,287,276,-1,272,252,228,-1,268,257,245,-1,288,266,265,-1,284,249,278,-1,285,273,289,-1,250,280,251,-1,290,281,291,-1,292,253,262,-1,242,256,262,-1,293,294,270,-1,260,293,270,-1,269,284,285,-1,269,285,289,-1,269,289,290,-1,291,280,279,-1,271,251,281,-1,292,262,283,-1,265,267,270,-1,265,294,295,-1,281,280,291,-1,294,265,270,-1,296,259,297,-1,273,281,289,-1,282,267,266,-1,293,298,294,-1,249,284,269,-1,299,254,253,-1,253,263,262,-1,239,249,261,-1,290,289,281,-1,262,267,282,-1,302,288,295,-1,260,259,293,-1,296,298,293,-1,280,281,251,-1,275,252,303,-1,298,304,295,-1,296,297,301,-1,305,272,254,-1,299,306,254,-1,307,253,292,-1,288,265,295,-1,288,308,266,-1,277,269,290,-1,300,310,311,-1,277,297,259,-1,286,276,275,-1,299,309,312,-1,307,299,253,-1,313,314,302,-1,304,302,295,-1,311,304,300,-1,311,302,304,-1,302,311,313,-1,311,315,313,-1,302,308,288,-1,296,293,259,-1,308,316,266,-1,316,317,318,-1,302,314,308,-1,298,295,294,-1,317,319,315,-1,316,319,317,-1,314,313,308,-1,313,319,308,-1,287,279,276,-1,267,245,270,-1,316,308,319,-1,317,315,318,-1,313,315,319,-1,305,303,252,-1,299,312,306,-1,320,316,318,-1,282,321,283,-1,322,282,316,-1,287,291,279,-1,305,252,272,-1,316,282,266,-1,306,305,254,-1]
IndexedFaceSet338.creaseAngle = 1.57
Coordinate339 = x3d.Coordinate()

IndexedFaceSet338.coord = Coordinate339

Shape334.geometry = IndexedFaceSet338

Transform333.children.append(Shape334)

fieldValue332.children.append(Transform333)

ProtoInstance330.fieldValue.append(fieldValue332)

fieldValue329.children.append(ProtoInstance330)
ProtoInstance340 = x3d.ProtoInstance()
ProtoInstance340.name = "Joint"
ProtoInstance340.DEF = "Allen_hanim_l_ankle"
fieldValue341 = x3d.fieldValue()
fieldValue341.name = "name"
fieldValue341.value = "l_ankle"

ProtoInstance340.fieldValue.append(fieldValue341)
fieldValue342 = x3d.fieldValue()
fieldValue342.name = "center"
fieldValue342.value = "0.0645 0.0719 -0.048"

ProtoInstance340.fieldValue.append(fieldValue342)
fieldValue343 = x3d.fieldValue()
fieldValue343.name = "children"
ProtoInstance344 = x3d.ProtoInstance()
ProtoInstance344.name = "Segment"
ProtoInstance344.DEF = "Allen_hanim_l_hindfoot"
fieldValue345 = x3d.fieldValue()
fieldValue345.name = "name"
fieldValue345.value = "l_hindfoot"

ProtoInstance344.fieldValue.append(fieldValue345)
fieldValue346 = x3d.fieldValue()
fieldValue346.name = "children"
Transform347 = x3d.Transform()
Transform347.DEF = "l_foot_adjust"
Transform347.center = [-0.32,1.1,0.021]
Transform347.rotation = [0,1,0,1.570796]
Transform347.scale = [0.1,0.1,0.1]
Shape348 = x3d.Shape()
Appearance349 = x3d.Appearance()
Material350 = x3d.Material()
Material350.DEF = "Shoe_Color"
Material350.ambientIntensity = 0.25

Appearance349.material = Material350

Shape348.appearance = Appearance349
IndexedFaceSet351 = x3d.IndexedFaceSet()
IndexedFaceSet351.coordIndex = [0,1,2,-1,3,4,5,-1,6,7,8,-1,9,10,11,-1,12,13,14,-1,15,16,17,-1,18,19,20,-1,21,22,23,-1,24,25,26,-1,27,28,29,-1,30,31,32,-1,33,34,35,-1,36,37,38,-1,39,40,41,-1,42,43,44,-1,45,46,47,-1,48,49,50,-1,51,52,53,-1,54,55,56,-1,57,58,59,-1,60,61,62,-1,63,64,65,-1,66,67,68,-1,69,70,71,-1,72,73,74,-1,75,76,77,-1,78,79,80,-1,81,82,83,-1,84,85,86,-1,87,88,89,-1,90,91,92,-1,93,94,95,-1,96,97,98,-1,99,100,101,-1,102,103,104,-1,105,106,107,-1,108,109,110,-1,111,112,113,-1,114,115,116,-1,117,118,119,-1,120,121,122,-1,123,124,125,-1,126,127,128,-1,129,130,131,-1,132,133,134,-1,135,136,137,-1,138,139,140,-1,141,142,143,-1,144,145,146,-1,147,148,149,-1,150,151,152,-1,153,154,155,-1,156,157,158,-1,159,160,161,-1,162,163,164,-1,165,166,167,-1,168,169,170,-1,171,172,173,-1,174,175,176,-1,177,178,179,-1,180,181,182,-1,183,184,185,-1,186,187,188,-1,189,190,191,-1,192,193,194,-1,195,196,197,-1,198,199,200,-1,201,202,203,-1,204,205,206,-1,207,208,209,-1,210,211,212,-1,213,214,215,-1,216,217,218,-1,219,220,221,-1,222,223,224,-1,225,226,227,-1,228,229,230,-1,231,232,233,-1,234,235,236,-1,237,238,239,-1,240,241,242,-1,243,244,245,-1,246,247,248,-1,249,250,251,-1,252,253,254,-1,255,256,257,-1,258,259,260,-1,261,262,263,-1,264,265,266,-1,267,268,269,-1,270,271,272,-1,273,274,275,-1,276,277,278,-1,279,280,281,-1,282,283,284,-1,285,286,287,-1,288,289,290,-1,291,292,293,-1,294,295,296,-1,297,298,299,-1,300,301,302,-1,303,304,305,-1,306,307,308,-1,309,310,311,-1,312,313,314,-1,315,316,317,-1,318,319,320,-1,321,322,323,-1,324,325,326,-1,327,328,329,-1,330,331,332,-1,333,334,335,-1,336,337,338,-1,339,340,341,-1,342,343,344,-1,345,346,347,-1,348,349,350,-1,351,352,353,-1,354,355,356,-1,357,358,359,-1,360,361,362,-1,363,364,365,-1,366,367,368,-1,369,370,371,-1,372,373,374,-1,375,376,377,-1,378,379,380,-1,381,382,383,-1,384,385,386,-1,387,388,389,-1,390,391,392,-1,393,394,395,-1,396,397,398,-1,399,400,401,-1,402,403,404,-1,405,406,407,-1,408,409,410,-1,411,412,413,-1,414,415,416,-1,417,418,419,-1,420,421,422,-1,423,424,425,-1,426,427,428,-1,429,430,431,-1,432,433,434,-1,435,436,437,-1,438,439,440,-1,441,442,443,-1,444,445,446,-1,447,448,449,-1,450,451,452,-1,453,454,455,-1,456,457,458,-1,459,460,461,-1,462,463,464,-1,465,466,467,-1,468,469,470,-1,471,472,473,-1,474,475,476,-1,477,478,479,-1,480,481,482,-1,483,484,485,-1,486,487,488,-1,489,490,491,-1,492,493,494,-1,495,496,497,-1,498,499,500,-1,501,502,503,-1,504,505,506,-1,507,508,509,-1,510,511,512,-1,513,514,515,-1,516,517,518,-1,519,520,521,-1,522,523,524,-1,525,526,527,-1,528,529,530,-1,531,532,533,-1,534,535,536,-1,537,538,539,-1,540,541,542,-1,543,544,545,-1,546,547,548,-1,549,550,551,-1,552,553,554,-1,555,556,557,-1,558,559,560,-1,561,562,563,-1,564,565,566,-1,567,568,569,-1,570,571,572,-1,573,574,575,-1,576,577,578,-1,579,580,581,-1,582,583,584,-1,585,586,587,-1,588,589,590,-1,591,592,593,-1,594,595,596,-1,597,598,599,-1,600,601,602,-1,603,604,605,-1,606,607,608,-1,609,610,611,-1,612,613,614,-1,615,616,617,-1,618,619,620,-1,621,622,623,-1,624,625,626,-1,627,628,629,-1,630,631,632,-1,633,634,635,-1,636,637,638,-1,639,640,641,-1,642,643,644,-1,645,646,647,-1,648,649,650,-1,651,652,653,-1,654,655,656,-1,657,658,659,-1,660,661,662,-1,663,664,665,-1,666,667,668,-1,669,670,671,-1,672,673,674,-1,675,676,677,-1,678,679,680,-1,681,682,683,-1,684,685,686,-1,687,688,689,-1,690,691,692,-1,693,694,695,-1,696,697,698,-1,699,700,701,-1,702,703,704,-1,705,706,707,-1,708,709,710,-1,711,712,713,-1,714,715,716,-1,717,718,719,-1,720,721,722,-1,723,724,725,-1,726,727,728,-1,729,730,731,-1,732,733,734,-1,735,736,737,-1,738,739,740,-1,741,742,743,-1,744,745,746,-1,747,748,749,-1,750,751,752,-1,753,754,755,-1,756,757,758,-1,759,760,761,-1,762,763,764,-1,765,766,767,-1,768,769,770,-1,771,772,773,-1,774,775,776,-1,777,778,779,-1,780,781,782,-1,783,784,785,-1,786,787,788,-1,789,790,791,-1,792,793,794,-1,795,796,797,-1,798,799,800,-1,801,802,803,-1,804,805,806,-1,807,808,809,-1,810,811,812,-1,813,814,815,-1,816,817,818,-1,819,820,821,-1,822,823,824,-1,825,826,827,-1,828,829,830,-1,831,832,833,-1,834,835,836,-1,837,838,839,-1,840,841,842,-1,843,844,845,-1,846,847,848,-1,849,850,851,-1,852,853,854,-1,855,856,857,-1,858,859,860,-1,861,862,863,-1,864,865,866,-1,867,868,869,-1,870,871,872,-1,873,874,875,-1,876,877,878,-1,879,880,881,-1,882,883,884,-1,885,886,887,-1,888,889,890,-1,891,892,893,-1,894,895,896,-1,897,898,899,-1,900,901,902,-1,903,904,905,-1,906,907,908,-1,909,910,911,-1,912,913,914,-1,915,916,917,-1,918,919,920,-1,921,922,923,-1,924,925,926,-1,927,928,929,-1,930,931,932,-1,933,934,935,-1,936,937,938,-1,939,940,941,-1,942,943,944,-1,945,946,947,-1,948,949,950,-1,951,952,953,-1,954,955,956,-1,957,958,959,-1,960,961,962,-1,963,964,965,-1,966,967,968,-1,969,970,971,-1,972,973,974,-1,975,976,977,-1,978,979,980,-1,981,982,983,-1,984,985,986,-1,987,988,989,-1,990,991,992,-1,993,994,995,-1,996,997,998,-1,999,1000,1001,-1,1002,1003,1004,-1,1005,1006,1007,-1,1008,1009,1010,-1,1011,1012,1013,-1,1014,1015,1016,-1,1017,1018,1019,-1,1020,1021,1022,-1,1023,1024,1025,-1,1026,1027,1028,-1,1029,1030,1031,-1,1032,1033,1034,-1,1035,1036,1037,-1,1038,1039,1040,-1,1041,1042,1043,-1,1044,1045,1046,-1,1047,1048,1049,-1,1050,1051,1052,-1,1053,1054,1055,-1,1056,1057,1058,-1,1059,1060,1061,-1,1062,1063,1064,-1,1065,1066,1067,-1,1068,1069,1070,-1,1071,1072,1073,-1,1074,1075,1076,-1,1077,1078,1079,-1,1080,1081,1082,-1,1083,1084,1085,-1,1086,1087,1088,-1,1089,1090,1091,-1,1092,1093,1094,-1,1095,1096,1097,-1,1098,1099,1100,-1,1101,1102,1103,-1,1104,1105,1106,-1,1107,1108,1109,-1,1110,1111,1112,-1,1113,1114,1115,-1,1116,1117,1118,-1,1119,1120,1121,-1,1122,1123,1124,-1,1125,1126,1127,-1,1128,1129,1130,-1,1131,1132,1133,-1,1134,1135,1136,-1,1137,1138,1139,-1,1140,1141,1142,-1,1143,1144,1145,-1,1146,1147,1148,-1,1149,1150,1151,-1,1152,1153,1154,-1,1155,1156,1157,-1,1158,1159,1160,-1,1161,1162,1163,-1,1164,1165,1166,-1,1167,1168,1169,-1,1170,1171,1172,-1,1173,1174,1175,-1,1176,1177,1178,-1,1179,1180,1181,-1,1182,1183,1184,-1,1185,1186,1187,-1,1188,1189,1190,-1,1191,1192,1193,-1,1194,1195,1196,-1,1197,1198,1199,-1,1200,1201,1202,-1,1203,1204,1205,-1,1206,1207,1208,-1,1209,1210,1211,-1,1212,1213,1214,-1,1215,1216,1217,-1,1218,1219,1220,-1,1221,1222,1223,-1,1224,1225,1226,-1,1227,1228,1229,-1,1230,1231,1232,-1,1233,1234,1235,-1,1236,1237,1238,-1,1239,1240,1241,-1,1242,1243,1244,-1,1245,1246,1247,-1,1248,1249,1250,-1,1251,1252,1253,-1,1254,1255,1256,-1,1257,1258,1259,-1,1260,1261,1262,-1,1263,1264,1265,-1,1266,1267,1268,-1,1269,1270,1271,-1,1272,1273,1274,-1,1275,1276,1277,-1,1278,1279,1280,-1,1281,1282,1283,-1,1284,1285,1286,-1,1287,1288,1289,-1,1290,1291,1292,-1,1293,1294,1295,-1,1296,1297,1298,-1,1299,1300,1301,-1,1302,1303,1304,-1,1305,1306,1307,-1,1308,1309,1310,-1,1311,1312,1313,-1,1314,1315,1316,-1,1317,1318,1319,-1,1320,1321,1322,-1,1323,1324,1325,-1,1326,1327,1328,-1,1329,1330,1331,-1,1332,1333,1334,-1,1335,1336,1337,-1,1338,1339,1340,-1,1341,1342,1343,-1,1344,1345,1346,-1,1347,1348,1349,-1,1350,1351,1352,-1,1353,1354,1355,-1,1356,1357,1358,-1,1359,1360,1361,-1,1362,1363,1364,-1,1365,1366,1367,-1,1368,1369,1370,-1,1371,1372,1373,-1,1374,1375,1376,-1,1377,1378,1379,-1,1380,1381,1382,-1,1383,1384,1385,-1,1386,1387,1388,-1,1389,1390,1391,-1,1392,1393,1394,-1,1395,1396,1397,-1,1398,1399,1400,-1,1401,1402,1403,-1,1404,1405,1406,-1,1407,1408,1409,-1,1410,1411,1412,-1,1413,1414,1415,-1,1416,1417,1418,-1,1419,1420,1421,-1,1422,1423,1424,-1,1425,1426,1427,-1,1428,1429,1430,-1,1431,1432,1433,-1,1434,1435,1436,-1,1437,1438,1439,-1,1440,1441,1442,-1,1443,1444,1445,-1,1446,1447,1448,-1,1449,1450,1451,-1,1452,1453,1454,-1,1455,1456,1457,-1,1458,1459,1460,-1,1461,1462,1463,-1,1464,1465,1466,-1,1467,1468,1469,-1,1470,1471,1472,-1,1473,1474,1475,-1,1476,1477,1478,-1,1479,1480,1481,-1,1482,1483,1484,-1,1485,1486,1487,-1,1488,1489,1490,-1,1491,1492,1493,-1,1494,1495,1496,-1,1497,1498,1499,-1,1500,1501,1502,-1,1503,1504,1505,-1,1506,1507,1508,-1,1509,1510,1511,-1,1512,1513,1514,-1,1515,1516,1517,-1,1518,1519,1520,-1,1521,1522,1523,-1,1524,1525,1526,-1,1527,1528,1529,-1,1530,1531,1532,-1,1533,1534,1535,-1,1536,1537,1538,-1,1539,1540,1541,-1,1542,1543,1544,-1,1545,1546,1547,-1,1548,1549,1550,-1,1551,1552,1553,-1,1554,1555,1556,-1,1557,1558,1559,-1,1560,1561,1562,-1,1563,1564,1565,-1,1566,1567,1568,-1,1569,1570,1571,-1,1572,1573,1574,-1,1575,1576,1577,-1,1578,1579,1580,-1,1581,1582,1583,-1,1584,1585,1586,-1,1587,1588,1589,-1,1590,1591,1592,-1,1593,1594,1595,-1,1596,1597,1598,-1,1599,1600,1601,-1,1602,1603,1604,-1,1605,1606,1607,-1,1608,1609,1610,-1,1611,1612,1613,-1,1614,1615,1616,-1,1617,1618,1619,-1,1620,1621,1622,-1,1623,1624,1625,-1,1626,1627,1628,-1,1629,1630,1631,-1,1632,1633,1634,-1,1635,1636,1637,-1,1638,1639,1640,-1,1641,1642,1643,-1,1644,1645,1646,-1,1647,1648,1649,-1,1650,1651,1652,-1,1653,1654,1655,-1,1656,1657,1658,-1,1659,1660,1661,-1,1662,1663,1664,-1,1665,1666,1667,-1,1668,1669,1670,-1,1671,1672,1673,-1,1674,1675,1676,-1,1677,1678,1679,-1,1680,1681,1682,-1,1683,1684,1685,-1,1686,1687,1688,-1,1689,1690,1691,-1,1692,1693,1694,-1,1695,1696,1697,-1,1698,1699,1700,-1,1701,1702,1703,-1,1704,1705,1706,-1,1707,1708,1709,-1,1710,1711,1712,-1,1713,1714,1715,-1,1716,1717,1718,-1,1719,1720,1721,-1,1722,1723,1724,-1,1725,1726,1727,-1,1728,1729,1730,-1,1731,1732,1733,-1,1734,1735,1736,-1,1737,1738,1739,-1,1740,1741,1742,-1,1743,1744,1745,-1,1746,1747,1748,-1,1749,1750,1751,-1,1752,1753,1754,-1,1755,1756,1757,-1,1758,1759,1760,-1,1761,1762,1763,-1,1764,1765,1766,-1,1767,1768,1769,-1,1770,1771,1772,-1,1773,1774,1775,-1,1776,1777,1778,-1,1779,1780,1781,-1,1782,1783,1784,-1,1785,1786,1787,-1,1788,1789,1790,-1,1791,1792,1793,-1,1794,1795,1796,-1,1797,1798,1799,-1,1800,1801,1802,-1,1803,1804,1805,-1,1806,1807,1808,-1,1809,1810,1811,-1,1812,1813,1814,-1,1815,1816,1817,-1,1818,1819,1820,-1,1821,1822,1823,-1,1824,1825,1826,-1,1827,1828,1829,-1,1830,1831,1832,-1,1833,1834,1835,-1,1836,1837,1838,-1,1839,1840,1841,-1,1842,1843,1844,-1,1845,1846,1847,-1,1848,1849,1850,-1,1851,1852,1853,-1,1854,1855,1856,-1,1857,1858,1859,-1,1860,1861,1862,-1,1863,1864,1865,-1,1866,1867,1868,-1,1869,1870,1871,-1,1872,1873,1874,-1,1875,1876,1877,-1,1878,1879,1880,-1,1881,1882,1883,-1,1884,1885,1886,-1,1887,1888,1889,-1,1890,1891,1892,-1,1893,1894,1895,-1,1896,1897,1898,-1,1899,1900,1901,-1,1902,1903,1904,-1,1905,1906,1907,-1,1908,1909,1910,-1,1911,1912,1913,-1,1914,1915,1916,-1,1917,1918,1919,-1,1920,1921,1922,-1,1923,1924,1925,-1,1926,1927,1928,-1,1929,1930,1931,-1,1932,1933,1934,-1,1935,1936,1937,-1,1938,1939,1940,-1,1941,1942,1943,-1,1944,1945,1946,-1,1947,1948,1949,-1]
IndexedFaceSet351.creaseAngle = 1.57
Coordinate352 = x3d.Coordinate()

IndexedFaceSet351.coord = Coordinate352

Shape348.geometry = IndexedFaceSet351

Transform347.children.append(Shape348)

fieldValue346.children.append(Transform347)

ProtoInstance344.fieldValue.append(fieldValue346)

fieldValue343.children.append(ProtoInstance344)

ProtoInstance340.fieldValue.append(fieldValue343)

fieldValue329.children.append(ProtoInstance340)

ProtoInstance326.fieldValue.append(fieldValue329)

fieldValue315.children.append(ProtoInstance326)

ProtoInstance312.fieldValue.append(fieldValue315)

fieldValue301.children.append(ProtoInstance312)
ProtoInstance353 = x3d.ProtoInstance()
ProtoInstance353.name = "Joint"
ProtoInstance353.DEF = "Allen_hanim_r_hip"
fieldValue354 = x3d.fieldValue()
fieldValue354.name = "name"
fieldValue354.value = "r_hip"

ProtoInstance353.fieldValue.append(fieldValue354)
fieldValue355 = x3d.fieldValue()
fieldValue355.name = "center"
fieldValue355.value = "-0.11 0.892362 -0.0732533"

ProtoInstance353.fieldValue.append(fieldValue355)
fieldValue356 = x3d.fieldValue()
fieldValue356.name = "children"
ProtoInstance357 = x3d.ProtoInstance()
ProtoInstance357.name = "Segment"
ProtoInstance357.DEF = "Allen_hanim_r_thigh"
fieldValue358 = x3d.fieldValue()
fieldValue358.name = "name"
fieldValue358.value = "r_thigh"

ProtoInstance357.fieldValue.append(fieldValue358)
fieldValue359 = x3d.fieldValue()
fieldValue359.name = "children"
Transform360 = x3d.Transform()
Transform360.DEF = "r_thigh_adjust"
Transform360.center = [0.43,1.1,-0.05]
Transform360.rotation = [0,1,0,1.570796]
Transform360.scale = [0.1,0.1,0.1]
Shape361 = x3d.Shape()
Appearance362 = x3d.Appearance()
Material363 = x3d.Material()
Material363.USE = "Pants_Color"

Appearance362.material = Material363
ImageTexture364 = x3d.ImageTexture()
ImageTexture364.USE = "camo"

Appearance362.texture = ImageTexture364

Shape361.appearance = Appearance362
IndexedFaceSet365 = x3d.IndexedFaceSet()
IndexedFaceSet365.coordIndex = [0,1,2,-1,3,4,5,-1,6,7,8,-1,9,10,11,-1,12,13,14,-1,15,16,17,-1,18,19,20,-1,21,22,23,-1,24,25,26,-1,27,28,29,-1,30,31,32,-1,33,34,35,-1,36,37,38,-1,39,40,41,-1,42,43,44,-1,45,46,47,-1,48,49,50,-1,51,52,53,-1,54,55,56,-1,57,58,59,-1,60,61,62,-1,63,64,65,-1,66,67,68,-1,69,70,71,-1,72,73,74,-1,75,76,77,-1,78,79,80,-1,81,82,83,-1,84,85,86,-1,87,88,89,-1,90,91,92,-1,93,94,95,-1,96,97,98,-1,99,100,101,-1,102,103,104,-1,105,106,107,-1,108,109,110,-1,111,112,113,-1,114,115,116,-1,117,118,119,-1,120,121,122,-1,123,124,125,-1,126,127,128,-1,129,130,131,-1,132,133,134,-1,135,136,137,-1,138,139,140,-1,141,142,143,-1,144,145,146,-1,147,148,149,-1,150,151,152,-1,153,154,155,-1,156,157,158,-1,159,160,161,-1,162,163,164,-1,165,166,167,-1,168,169,170,-1,171,172,173,-1,174,175,176,-1,177,178,179,-1,180,181,182,-1,183,184,185,-1,186,187,188,-1,189,190,191,-1,192,193,194,-1,195,196,197,-1,198,199,200,-1,201,202,203,-1,204,205,206,-1,207,208,209,-1,210,211,212,-1,213,214,215,-1,216,217,218,-1,219,220,221,-1,222,223,224,-1,225,226,227,-1,228,229,230,-1,231,232,233,-1,234,235,236,-1,237,238,239,-1,240,241,242,-1,243,244,245,-1,246,247,248,-1,217,220,218,-1,222,226,223,-1,195,198,196,-1,198,200,196,-1,249,202,200,-1,200,202,196,-1,201,205,202,-1,218,220,214,-1,219,223,220,-1,202,205,196,-1,220,223,214,-1,215,214,212,-1,212,214,210,-1,214,223,210,-1,223,226,210,-1,204,208,205,-1,207,210,208,-1,210,226,208,-1,205,208,196,-1,208,226,196,-1,250,251,252,-1,253,254,255,-1,256,257,258,-1,259,260,261,-1,262,263,264,-1,265,266,267,-1,268,269,270,-1,271,272,273,-1,274,275,276,-1,277,278,279,-1,280,281,282,-1,283,284,285,-1,286,287,288,-1,289,290,291,-1,292,293,294,-1,295,296,297,-1,298,299,300,-1,301,302,303,-1,304,305,306,-1,307,308,309,-1,310,311,312,-1,313,314,315,-1,316,317,318,-1,319,320,321,-1,322,323,324,-1,325,326,327,-1,328,329,330,-1,331,332,333,-1,334,335,336,-1,337,338,339,-1,340,341,342,-1,343,344,345,-1,346,347,348,-1,349,350,351,-1,352,353,354,-1,355,356,357,-1,358,359,360,-1,361,362,363,-1,364,365,366,-1,367,368,369,-1,370,371,372,-1,373,374,375,-1,376,377,378,-1,379,380,381,-1,382,383,384,-1,383,382,384,-1,385,386,387,-1,388,389,390,-1,391,392,393,-1,394,395,396,-1,397,398,399,-1,400,401,402,-1,403,404,405,-1,406,407,408,-1,407,406,408,-1,409,410,411,-1,409,411,410,-1,412,413,414,-1,415,416,417,-1,418,419,420,-1,421,422,423,-1,424,425,426,-1,427,428,429,-1,428,427,429,-1,430,431,432,-1,433,434,435,-1,436,437,438,-1,439,440,441,-1,442,443,444,-1,445,446,447,-1,448,449,450,-1,451,452,453,-1,454,455,456,-1,455,454,456,-1,457,458,459,-1,460,461,462,-1,463,464,465,-1,466,467,468,-1,469,470,471,-1,472,473,474,-1,475,476,477,-1,478,479,480,-1,481,482,483,-1,484,485,486,-1,487,488,489,-1,490,491,492,-1,493,494,495,-1,496,497,498,-1,498,497,496,-1,499,500,501,-1,502,503,504,-1,505,506,507,-1,508,509,510,-1,511,512,513,-1,514,515,516,-1,517,518,519,-1,520,521,522,-1,523,524,525,-1,526,527,528,-1,529,530,531,-1,532,533,534,-1,533,532,534,-1,535,536,537,-1,538,539,540,-1,538,540,539,-1,541,542,543,-1,544,545,546,-1,547,548,549,-1,550,551,552,-1,553,554,555,-1,556,557,558,-1,559,560,561,-1,562,563,564,-1,565,566,567,-1,566,565,567,-1,568,569,570,-1,571,572,573,-1,574,575,576,-1,577,578,579,-1,580,581,582,-1,583,584,585,-1,586,587,588,-1,589,590,591,-1,590,589,591,-1,592,593,594,-1,595,596,597,-1,598,599,600,-1,601,602,603,-1,604,605,606,-1,607,608,609,-1,607,609,608,-1,610,611,612,-1,613,614,615,-1,613,615,614,-1,616,617,618,-1,619,620,621,-1,622,623,624,-1,625,626,627,-1,628,629,630,-1,631,632,633,-1,632,631,633,-1,634,635,636,-1,634,636,635,-1,637,638,639,-1,639,638,637,-1,640,641,642,-1,643,644,645,-1,646,647,648,-1,649,650,651,-1,652,653,654,-1,655,656,657,-1,656,655,657,-1,658,659,660,-1,660,659,658,-1,661,662,663,-1,664,665,666,-1,666,665,664,-1,667,668,669,-1,670,671,672,-1,673,674,675,-1,676,677,678,-1,679,680,681,-1,680,679,681,-1,682,683,684,-1,685,686,687,-1,688,689,690,-1,691,692,693,-1,694,695,696,-1,697,698,699,-1,700,701,702,-1,703,704,705,-1,706,707,708,-1,707,706,708,-1,709,710,711,-1,710,709,711,-1,712,713,714,-1,715,716,717,-1,718,719,720,-1,721,722,723,-1,724,725,726,-1,727,728,729,-1,728,727,729,-1,730,731,732,-1,733,734,735,-1,736,737,738,-1,739,740,741,-1,742,743,744,-1,745,746,747,-1,748,749,750,-1,751,752,753,-1,754,755,756,-1,757,758,759,-1,760,761,762,-1,763,764,765,-1,766,767,768,-1,769,770,771,-1,772,773,774,-1,775,776,777,-1,778,779,780,-1,781,782,783,-1,784,785,786,-1,787,788,789,-1,790,791,792,-1,793,794,795,-1,796,797,798,-1,799,800,801,-1,800,799,801,-1,802,803,804,-1,803,802,804,-1,805,806,807,-1,808,809,810,-1,811,812,813,-1,814,815,816,-1,817,818,819,-1,820,821,822,-1,823,824,825,-1,826,827,828,-1,829,830,831,-1,832,833,834,-1,835,836,837,-1,838,839,840,-1,841,842,843,-1,844,845,846,-1,847,848,849,-1,850,851,852,-1,853,854,855,-1,853,855,854,-1,856,857,858,-1,859,860,861,-1,862,863,864,-1,865,866,867,-1,868,869,870,-1,871,872,873,-1,874,875,876,-1,877,878,879,-1,880,881,882,-1,880,882,881,-1,883,884,885,-1,886,887,888,-1,889,890,891,-1,892,893,894,-1,895,896,897,-1,898,899,900,-1,901,902,903,-1,904,905,906,-1,907,908,909,-1,910,911,912,-1,913,914,915,-1,916,917,918,-1,919,920,921,-1,922,923,924,-1,925,926,927,-1,925,927,926,-1,928,929,930,-1,931,932,933,-1,934,935,936,-1,937,938,939,-1,940,941,942,-1,943,944,945,-1,946,947,948,-1,949,950,951,-1,952,953,954,-1,955,956,957,-1,958,959,960,-1,961,962,963,-1,964,965,966,-1,967,968,969,-1,970,971,972,-1,973,974,975,-1,976,977,978,-1,979,980,981,-1,982,983,984,-1,985,986,987,-1,988,989,990,-1,991,992,993,-1,994,995,996,-1,997,998,999,-1,1000,1001,1002,-1,1003,1004,1005,-1,1006,1007,1008,-1,1009,1010,1011,-1,1012,1013,1014,-1,1015,1016,1017,-1,1018,1019,1020,-1,1021,1022,1023,-1,1024,1025,1026,-1,1027,1028,1029,-1,1030,1031,1032,-1,1033,1034,1035,-1,1036,1037,1038,-1,1039,1040,1041,-1,1042,1043,1044,-1,1045,1046,1047,-1,1048,1049,1050,-1,1051,1052,1053,-1,1054,1055,1056,-1,1057,1058,1059,-1,1060,1061,1062,-1,1063,1064,1065,-1,1066,1067,1068,-1,1069,1070,1071,-1,1072,1073,1074,-1,1075,1076,1077,-1,1078,1079,1080,-1,1081,1082,1083,-1,1084,1085,1086,-1,1087,1088,1089,-1,1090,1091,1092,-1,1093,1094,1095,-1,1096,1097,1098,-1,1099,1100,1101,-1,1102,1103,1104,-1,1105,1106,1107,-1,1108,1109,1110,-1,1111,1112,1113,-1,1114,1115,1116,-1,1117,1118,1119,-1,1120,1121,1122,-1,1123,1124,1125,-1,1126,1127,1128,-1,1129,1130,1131,-1,1132,1133,1134,-1,1135,1136,1137,-1,1138,1139,1140,-1,1141,1142,1143,-1,1144,1145,1146,-1,1147,1148,1149,-1,1150,1151,1152,-1,1153,1154,1155,-1,1156,1157,1158,-1,1159,1160,1161,-1,1162,1163,1164,-1,1165,1166,1167,-1,1168,1169,1170,-1,1171,1172,1173,-1,1174,1175,1176,-1,1177,1178,1179,-1,1180,1181,1182,-1,1183,1184,1185,-1,1186,1187,1188,-1,1189,1190,1191,-1,1192,1193,1194,-1,1195,1196,1197,-1,1198,1199,1200,-1,1201,1202,1203,-1,1204,1205,1206,-1,1207,1208,1209,-1,1210,1211,1212,-1,1213,1214,1215,-1,1216,1217,1218,-1,1219,1220,1221,-1,1222,1223,1224,-1,1225,1226,1227,-1,1228,1229,1230,-1,1231,1232,1233,-1,1234,1235,1236,-1,1237,1238,1239,-1,1240,1241,1242,-1,1243,1244,1245,-1,1246,1247,1248,-1,1249,1250,1251,-1,1252,1253,1254,-1,1255,1256,1257,-1,1258,1259,1260,-1,1261,1262,1263,-1,1264,1265,1266,-1,1267,1268,1269,-1,1270,1271,1272,-1,1273,1274,1275,-1,1276,1277,1278,-1,1279,1280,1281,-1,1282,1283,1284,-1,1285,1286,1287,-1,1288,1289,1290,-1,1291,1292,1293,-1,1294,1295,1296,-1,1297,1298,1299,-1,1300,1301,1302,-1,1303,1304,1305,-1,1306,1307,1308,-1,1309,1310,1311,-1,1312,1313,1314,-1,1315,1316,1317,-1,1318,1319,1320,-1,1321,1322,1323,-1,1324,1325,1326,-1,1327,1328,1329,-1,1330,1331,1332,-1,1333,1334,1335,-1,1336,1337,1338,-1,1339,1340,1341,-1,1342,1343,1344,-1,1345,1346,1347,-1,1348,1349,1350,-1,1351,1352,1353,-1,1354,1355,1356,-1,1357,1358,1359,-1,1360,1361,1362,-1,1363,1364,1365,-1,1366,1367,1368,-1,1369,1370,1371,-1,1372,1373,1374,-1,1375,1376,1377,-1,1378,1379,1380,-1,1381,1382,1383,-1,1384,1385,1386,-1,1387,1388,1389,-1,1390,1391,1392,-1,1393,1394,1395,-1,1396,1397,1398,-1,1399,1400,1401,-1,1402,1403,1404,-1,1405,1406,1407,-1,1408,1409,1410,-1,1411,1412,1413,-1,1414,1415,1416,-1,1417,1418,1419,-1,1420,1421,1422,-1,1423,1424,1425,-1,1426,1427,1428,-1,1429,1430,1431,-1,1432,1433,1434,-1,1435,1436,1437,-1,1438,1439,1440,-1,1441,1442,1443,-1,1444,1445,1446,-1,1447,1448,1449,-1,1450,1451,1452,-1,1453,1454,1455,-1,1456,1457,1458,-1,1459,1460,1461,-1,1462,1463,1464,-1,1465,1466,1467,-1,1468,1469,1470,-1,1471,1472,1473,-1,1474,1475,1476,-1,1477,1478,1479,-1,1480,1481,1482,-1,1483,1484,1485,-1,1486,1487,1488,-1,1489,1490,1491,-1,1492,1493,1494,-1,1495,1496,1497,-1,1498,1499,1500,-1,1501,1502,1503,-1,1504,1505,1506,-1,1507,1508,1509,-1,1510,1511,1512,-1,1513,1514,1515,-1,1516,1517,1518,-1,1519,1520,1521,-1,1522,1523,1524,-1,1525,1526,1527,-1,1528,1529,1530,-1,1531,1532,1533,-1,1534,1535,1536,-1,1537,1538,1539,-1,1540,1541,1542,-1,1543,1544,1545,-1,1546,1547,1548,-1,1549,1550,1551,-1,1552,1553,1554,-1,1555,1556,1557,-1,1558,1559,1560,-1,1561,1562,1563,-1,1564,1565,1566,-1,1567,1568,1569,-1,1570,1571,1572,-1,1573,1574,1575,-1,1576,1577,1578,-1,1579,1580,1581,-1,1582,1583,1584,-1,1585,1586,1587,-1,1588,1589,1590,-1,1591,1592,1593,-1,1594,1595,1596,-1,1597,1598,1599,-1,1600,1601,1602,-1,1603,1604,1605,-1,1606,1607,1608,-1,1609,1610,1611,-1,1612,1613,1614,-1,1615,1616,1617,-1,1618,1619,1620,-1,1621,1622,1623,-1,1624,1625,1626,-1,1627,1628,1629,-1,1630,1631,1632,-1,1633,1634,1635,-1,1636,1637,1638,-1,1639,1640,1641,-1,1642,1643,1644,-1,1645,1646,1647,-1,1648,1649,1650,-1,1651,1652,1653,-1,1654,1655,1656,-1,1657,1658,1659,-1,1660,1661,1662,-1,1663,1664,1665,-1,1666,1667,1668,-1,1669,1670,1671,-1,1672,1673,1674,-1,1675,1676,1677,-1,1678,1679,1680,-1,1681,1682,1683,-1,1684,1685,1686,-1,1687,1688,1689,-1,1690,1691,1692,-1,1693,1694,1695,-1,1696,1697,1698,-1,1699,1700,1701,-1,1702,1703,1704,-1,1705,1706,1707,-1,1708,1709,1710,-1,1711,1712,1713,-1,1714,1715,1716,-1,1717,1718,1719,-1,1720,1721,1722,-1,1723,1724,1725,-1,1726,1727,1728,-1,1729,1730,1731,-1,1732,1733,1734,-1,1735,1736,1737,-1,1738,1739,1740,-1,1741,1742,1743,-1,1744,1745,1746,-1,1747,1748,1749,-1,1750,1751,1752,-1,1753,1754,1755,-1,1756,1757,1758,-1,1759,1760,1761,-1,1762,1763,1764,-1,1765,1766,1767,-1,1768,1769,1770,-1,1771,1772,1773,-1,1774,1775,1776,-1,1777,1778,1779,-1,1780,1781,1782,-1,1783,1784,1785,-1,1786,1787,1788,-1,1789,1790,1791,-1,1792,1793,1794,-1,1795,1796,1797,-1,1798,1799,1800,-1,1801,1802,1803,-1,1804,1805,1806,-1,1807,1808,1809,-1,1810,1811,1812,-1,1813,1814,1815,-1,1816,1817,1818,-1,1819,1820,1821,-1,1822,1823,1824,-1,1825,1826,1827,-1,1828,1829,1830,-1,1831,1832,1833,-1,1834,1835,1836,-1,1837,1838,1839,-1,1840,1841,1842,-1,1843,1844,1845,-1,1846,1847,1848,-1,1849,1850,1851,-1,1852,1853,1854,-1,1855,1856,1857,-1,1858,1859,1860,-1,1861,1862,1863,-1,1864,1865,1866,-1,1867,1868,1869,-1,1870,1871,1872,-1,1873,1874,1875,-1,1876,1877,1878,-1,1879,1880,1881,-1,1882,1883,1884,-1,1885,1886,1887,-1,1888,1889,1890,-1,1891,1892,1893,-1,1894,1895,1896,-1,1897,1898,1899,-1,1900,1901,1902,-1,1903,1904,1905,-1,1906,1907,1908,-1,1909,1910,1911,-1,1912,1913,1914,-1,1915,1916,1917,-1,1918,1919,1920,-1,1921,1922,1923,-1,1924,1925,1926,-1,1927,1928,1929,-1,1930,1931,1932,-1,1933,1934,1935,-1,1936,1937,1938,-1,1939,1940,1941,-1,1942,1943,1944,-1,1945,1946,1947,-1,1948,1949,1950,-1,1951,1952,1953,-1,1954,1955,1956,-1,1957,1958,1959,-1,1960,1961,1962,-1,1963,1964,1965,-1,1966,1967,1968,-1,1969,1970,1971,-1,1972,1973,1974,-1,1975,1976,1977,-1,1978,1979,1980,-1,1981,1982,1983,-1,1984,1985,1986,-1,1987,1988,1989,-1,1990,1991,1992,-1,1993,1994,1995,-1,1996,1997,1998,-1,1999,2000,2001,-1,2002,2003,2004,-1,2005,2006,2007,-1,2008,2009,2010,-1,2011,2012,2013,-1,2014,2015,2016,-1,2017,2018,2019,-1,2020,2021,2022,-1,2023,2024,2025,-1,2026,2027,2028,-1,2029,2030,2031,-1,2032,2033,2034,-1,2035,2036,2037,-1,2038,2039,2040,-1,2041,2042,2043,-1,2044,2045,2046,-1,2047,2048,2049,-1,2050,2051,2052,-1,2053,2054,2055,-1,2056,2057,2058,-1,2059,2060,2061,-1,2062,2063,2064,-1,2065,2066,2067,-1,2068,2069,2070,-1,2071,2072,2073,-1,2074,2075,2076,-1,2077,2078,2079,-1,2080,2081,2082,-1,2083,2084,2085,-1,2086,2087,2088,-1,2089,2090,2091,-1,2092,2093,2094,-1,2095,2096,2097,-1,2098,2099,2100,-1,2101,2102,2103,-1,2104,2105,2106,-1,2107,2108,2109,-1,2110,2111,2112,-1,2113,2114,2115,-1,2116,2117,2118,-1,2119,2120,2121,-1,2122,2123,2124,-1,2125,2126,2127,-1,2128,2129,2130,-1,2131,2132,2133,-1,2134,2135,2136,-1,2137,2138,2139,-1,2140,2141,2142,-1,2143,2144,2145,-1,2146,2147,2148,-1,2149,2150,2151,-1,2152,2153,2154,-1,2155,2156,2157,-1,2158,2159,2160,-1,2161,2162,2163,-1,2164,2165,2166,-1,2167,2168,2169,-1,2170,2171,2172,-1,2173,2174,2175,-1,2176,2177,2178,-1,2179,2180,2181,-1,2182,2183,2184,-1,2185,2186,2187,-1,2188,2189,2190,-1,2191,2192,2193,-1,2194,2195,2196,-1,2197,2198,2199,-1,2200,2201,2202,-1,2203,2204,2205,-1,2206,2207,2208,-1,2209,2210,2211,-1,2212,2213,2214,-1,2215,2216,2217,-1,2218,2219,2220,-1,2221,2222,2223,-1,2224,2225,2226,-1,2227,2228,2229,-1,2230,2231,2232,-1,2233,2234,2235,-1,2236,2237,2238,-1,2239,2240,2241,-1,2242,2243,2244,-1,2245,2246,2247,-1,2248,2249,2250,-1,2251,2252,2253,-1,2254,2255,2256,-1,2257,2258,2259,-1,2260,2261,2262,-1,2263,2264,2265,-1,2266,2267,2268,-1,2269,2270,2271,-1,2272,2273,2274,-1,2275,2276,2277,-1,2278,2279,2280,-1,2281,2282,2283,-1,2284,2285,2286,-1,2287,2288,2289,-1,2290,2291,2292,-1,2293,2294,2295,-1,2296,2297,2298,-1,2299,2300,2301,-1,2302,2303,2304,-1,2305,2306,2307,-1,2308,2309,2310,-1,2311,2312,2313,-1,2314,2315,2316,-1,2317,2318,2319,-1,2320,2321,2322,-1,2323,2324,2325,-1,2326,2327,2328,-1,2329,2330,2331,-1,2332,2333,2334,-1,2335,2336,2337,-1,2338,2339,2340,-1,2341,2342,2343,-1,2344,2345,2346,-1,2347,2348,2349,-1,2350,2351,2352,-1,2353,2354,2355,-1,2356,2357,2358,-1,2359,2360,2361,-1,2362,2363,2364,-1,2365,2366,2367,-1,2368,2369,2370,-1,2371,2372,2373,-1,2374,2375,2376,-1,2377,2378,2379,-1,2380,2381,2382,-1,2383,2384,2385,-1,2386,2387,2388,-1,2389,2390,2391,-1,2392,2393,2394,-1,2395,2396,2397,-1,2398,2399,2400,-1,2401,2402,2403,-1,2404,2405,2406,-1,2407,2408,2409,-1,2410,2411,2412,-1,2413,2414,2415,-1,2416,2417,2418,-1,2419,2420,2421,-1,2422,2423,2424,-1,2425,2426,2427,-1,2428,2429,2430,-1,2431,2432,2433,-1,2434,2435,2436,-1,2434,2436,2437,-1]
IndexedFaceSet365.creaseAngle = 1.61
Coordinate366 = x3d.Coordinate()

IndexedFaceSet365.coord = Coordinate366

Shape361.geometry = IndexedFaceSet365

Transform360.children.append(Shape361)

fieldValue359.children.append(Transform360)

ProtoInstance357.fieldValue.append(fieldValue359)

fieldValue356.children.append(ProtoInstance357)
ProtoInstance367 = x3d.ProtoInstance()
ProtoInstance367.name = "Joint"
ProtoInstance367.DEF = "Allen_hanim_r_knee"
fieldValue368 = x3d.fieldValue()
fieldValue368.name = "name"
fieldValue368.value = "r_knee"

ProtoInstance367.fieldValue.append(fieldValue368)
fieldValue369 = x3d.fieldValue()
fieldValue369.name = "center"
fieldValue369.value = "-0.0699 0.51 -0.0166"

ProtoInstance367.fieldValue.append(fieldValue369)
fieldValue370 = x3d.fieldValue()
fieldValue370.name = "children"
ProtoInstance371 = x3d.ProtoInstance()
ProtoInstance371.name = "Segment"
ProtoInstance371.DEF = "Allen_hanim_r_calf"
fieldValue372 = x3d.fieldValue()
fieldValue372.name = "name"
fieldValue372.value = "r_calf"

ProtoInstance371.fieldValue.append(fieldValue372)
fieldValue373 = x3d.fieldValue()
fieldValue373.name = "children"
Transform374 = x3d.Transform()
Transform374.DEF = "r_calf_adjust"
Transform374.center = [0.43,1.1,-0.05]
Transform374.rotation = [0,1,0,1.570796]
Transform374.scale = [0.1,0.1,0.1]
Shape375 = x3d.Shape()
Appearance376 = x3d.Appearance()
Material377 = x3d.Material()
Material377.USE = "Pants_Color"

Appearance376.material = Material377
ImageTexture378 = x3d.ImageTexture()
ImageTexture378.USE = "camo"

Appearance376.texture = ImageTexture378

Shape375.appearance = Appearance376
IndexedFaceSet379 = x3d.IndexedFaceSet()
IndexedFaceSet379.coordIndex = [0,1,2,-1,3,4,5,-1,6,7,8,-1,9,10,11,-1,12,13,14,-1,15,16,17,-1,18,19,20,-1,21,22,23,-1,24,25,26,-1,27,28,29,-1,30,31,32,-1,33,34,35,-1,36,37,38,-1,39,40,41,-1,42,43,44,-1,45,46,47,-1,48,49,50,-1,51,52,53,-1,54,55,56,-1,57,58,59,-1,60,61,62,-1,63,64,65,-1,66,67,68,-1,69,70,71,-1,72,73,74,-1,75,76,77,-1,78,79,80,-1,81,82,83,-1,84,85,86,-1,87,88,89,-1,90,91,92,-1,93,94,95,-1,96,97,98,-1,99,100,101,-1,102,103,104,-1,105,106,107,-1,108,109,110,-1,111,112,113,-1,114,115,116,-1,117,118,119,-1,120,121,122,-1,123,124,125,-1,126,127,128,-1,129,130,131,-1,132,133,134,-1,135,136,137,-1,138,139,140,-1,141,142,143,-1,144,145,146,-1,147,148,149,-1,150,151,152,-1,153,154,155,-1,156,157,158,-1,159,160,161,-1,162,163,164,-1,165,166,167,-1,168,169,170,-1,171,172,173,-1,174,175,176,-1,177,178,179,-1,180,181,182,-1,183,184,185,-1,186,187,188,-1,189,190,191,-1,192,193,194,-1,195,196,197,-1,198,199,200,-1,201,202,203,-1,204,205,206,-1,207,208,209,-1,210,211,212,-1,213,214,215,-1,216,217,218,-1,219,220,221,-1,222,223,224,-1,225,226,227,-1,228,229,230,-1,231,232,233,-1,234,235,236,-1,237,238,239,-1,240,241,242,-1,243,244,245,-1,246,247,248,-1,249,250,251,-1,252,253,254,-1,255,256,257,-1,258,259,260,-1,261,262,263,-1,264,265,266,-1,267,268,269,-1,270,271,272,-1,273,274,275,-1,276,277,278,-1,279,280,281,-1,282,283,284,-1,285,286,287,-1,288,289,290,-1,291,292,293,-1,294,295,296,-1,297,298,299,-1,300,301,302,-1,303,304,305,-1,306,307,308,-1,309,310,311,-1,312,313,314,-1,315,316,317,-1,318,319,320,-1,321,322,323,-1,324,325,326,-1,327,328,329,-1,330,331,332,-1,333,334,335,-1,336,337,338,-1,339,340,341,-1,342,343,344,-1,345,346,347,-1,348,349,350,-1,351,352,353,-1,354,355,356,-1,357,358,359,-1,360,361,362,-1,363,364,365,-1,366,367,368,-1,369,370,371,-1,372,373,374,-1,375,376,377,-1,378,379,380,-1,381,382,383,-1,384,385,386,-1,387,388,389,-1,390,391,392,-1,393,394,395,-1,396,397,398,-1,399,400,401,-1,402,403,404,-1,405,406,407,-1,408,409,410,-1,411,412,413,-1,414,415,416,-1,417,418,419,-1,420,421,422,-1,423,424,425,-1,426,427,428,-1,429,430,431,-1,432,433,434,-1,435,436,437,-1,438,439,440,-1,441,442,443,-1,444,445,446,-1,447,448,449,-1,450,451,452,-1,453,454,455,-1,456,457,458,-1,459,460,461,-1,462,463,464,-1,465,466,467,-1,468,469,470,-1,471,472,473,-1,474,475,476,-1,477,478,479,-1,480,481,482,-1,483,484,485,-1,486,487,488,-1,489,490,491,-1,492,493,494,-1,495,496,497,-1,498,499,500,-1,501,502,503,-1,504,505,506,-1,507,508,509,-1,510,511,512,-1,513,514,515,-1,516,517,518,-1,519,520,521,-1,522,523,524,-1,525,526,527,-1,528,529,530,-1,531,532,533,-1,534,535,536,-1,537,538,539,-1,540,541,542,-1,543,544,545,-1,546,547,548,-1,549,550,551,-1,552,553,554,-1,555,556,557,-1,558,559,560,-1,561,562,563,-1,564,565,566,-1,567,568,569,-1,570,571,572,-1,573,574,575,-1,576,577,578,-1,579,580,581,-1,582,583,584,-1,585,586,587,-1,588,589,590,-1,591,592,593,-1,594,595,596,-1,597,598,599,-1,600,601,602,-1,603,604,605,-1,606,607,608,-1,609,610,611,-1,612,613,614,-1,615,616,617,-1,618,619,620,-1,621,622,623,-1,624,625,626,-1,627,628,629,-1,630,631,632,-1,633,634,635,-1,636,637,638,-1,639,640,641,-1,642,643,644,-1,645,646,647,-1,648,649,650,-1,651,652,653,-1,654,655,656,-1,657,658,659,-1,660,661,662,-1,663,664,665,-1,666,667,668,-1,669,670,671,-1,672,673,674,-1,675,676,677,-1,678,679,680,-1,681,682,683,-1,684,685,686,-1,687,688,689,-1,690,691,692,-1,693,694,695,-1,696,697,698,-1,699,700,701,-1,702,703,704,-1,705,706,707,-1,708,709,710,-1,711,712,713,-1,714,715,716,-1,717,718,719,-1,720,721,722,-1,723,724,725,-1,726,727,728,-1,729,730,731,-1,732,733,734,-1,735,736,737,-1,738,739,740,-1,741,742,743,-1,744,745,746,-1,747,748,749,-1,750,751,752,-1,753,754,755,-1,756,757,758,-1,759,760,761,-1,762,763,764,-1,765,766,767,-1,768,769,770,-1,771,772,773,-1,774,775,776,-1,777,778,779,-1,780,781,782,-1,783,784,785,-1,786,787,788,-1,789,790,791,-1,792,793,794,-1,795,796,797,-1,798,799,800,-1,801,802,803,-1,804,805,806,-1,807,808,809,-1,810,811,812,-1,813,814,815,-1,816,817,818,-1,819,820,821,-1,822,823,824,-1,825,826,827,-1,828,829,830,-1,831,832,833,-1,834,835,836,-1,837,838,839,-1,840,841,842,-1,843,844,845,-1,846,847,848,-1,849,850,851,-1,852,853,854,-1,855,856,857,-1,858,859,860,-1,861,862,863,-1,864,865,866,-1,867,868,869,-1,870,871,872,-1,873,874,875,-1,876,877,878,-1,879,880,881,-1,882,883,884,-1,885,886,887,-1,888,889,890,-1,891,892,893,-1,894,895,896,-1,897,898,899,-1,900,901,902,-1,903,904,905,-1,906,907,908,-1,909,910,911,-1,912,913,914,-1,915,916,917,-1,918,919,920,-1,921,922,923,-1,924,925,926,-1,927,928,929,-1,930,931,932,-1,933,934,935,-1,936,937,938,-1,939,940,941,-1,942,943,944,-1,945,946,947,-1,948,949,950,-1,951,952,953,-1,954,955,956,-1,957,958,959,-1,960,961,962,-1,963,964,965,-1,966,967,968,-1,969,970,971,-1,972,973,974,-1,975,976,977,-1,978,979,980,-1,981,982,983,-1,984,985,986,-1,987,988,989,-1,990,991,992,-1,993,994,995,-1,996,997,998,-1,999,1000,1001,-1,1002,1003,1004,-1,1005,1006,1007,-1,1008,1009,1010,-1,1011,1012,1013,-1,1014,1015,1016,-1,1017,1018,1019,-1,1020,1021,1022,-1,1023,1024,1025,-1,1026,1027,1028,-1,1029,1030,1031,-1,1032,1033,1034,-1,1035,1036,1037,-1,1038,1039,1040,-1,1041,1042,1043,-1,1044,1045,1046,-1,1047,1048,1049,-1,1050,1051,1052,-1,1053,1054,1055,-1,1056,1057,1058,-1,1059,1060,1061,-1,1062,1063,1064,-1,1065,1066,1067,-1,1068,1069,1070,-1,1071,1072,1073,-1,1074,1075,1076,-1,1077,1078,1079,-1,1080,1081,1082,-1,1083,1084,1085,-1,1086,1087,1088,-1,1089,1090,1091,-1,1092,1093,1094,-1,1095,1096,1097,-1,1098,1099,1100,-1,1101,1102,1103,-1,1104,1105,1106,-1,1107,1108,1109,-1,1110,1111,1112,-1,1113,1114,1115,-1,1116,1117,1118,-1,1119,1120,1121,-1,1122,1123,1124,-1,1125,1126,1127,-1,1128,1129,1130,-1,1131,1132,1133,-1,1134,1135,1136,-1,1137,1138,1139,-1,1140,1141,1142,-1,1143,1144,1145,-1,1146,1147,1148,-1,1149,1150,1151,-1,1152,1153,1154,-1,1155,1156,1157,-1,1158,1159,1160,-1,1161,1162,1163,-1,1164,1165,1166,-1,1167,1168,1169,-1,1170,1171,1172,-1,1173,1174,1175,-1,1176,1177,1178,-1,1179,1180,1181,-1,1182,1183,1184,-1,1185,1186,1187,-1,1188,1189,1190,-1,1191,1192,1193,-1,1194,1195,1196,-1,1197,1198,1199,-1,1200,1201,1202,-1,1203,1204,1205,-1,1206,1207,1208,-1,1209,1210,1211,-1,1212,1213,1214,-1,1215,1216,1217,-1,1218,1219,1220,-1,1221,1222,1223,-1,1224,1225,1226,-1,1227,1228,1229,-1,1230,1231,1232,-1,1233,1234,1235,-1,1236,1237,1238,-1,1239,1240,1241,-1,1242,1243,1244,-1,1245,1246,1247,-1,1248,1249,1250,-1,1251,1252,1253,-1,1254,1255,1256,-1,1257,1258,1259,-1,1260,1261,1262,-1,1263,1264,1265,-1,1266,1267,1268,-1,1269,1270,1271,-1,1272,1273,1274,-1,1275,1276,1277,-1,1278,1279,1280,-1,1281,1282,1283,-1,1284,1285,1286,-1,1287,1288,1289,-1,1290,1291,1292,-1,1293,1294,1295,-1,1296,1297,1298,-1,1299,1300,1301,-1,1302,1303,1304,-1,1305,1306,1307,-1,1308,1309,1310,-1,1311,1312,1313,-1,1314,1315,1316,-1,1317,1318,1319,-1,1320,1321,1322,-1,1323,1324,1325,-1,1326,1327,1328,-1,1329,1330,1331,-1,1332,1333,1334,-1,1335,1336,1337,-1,1338,1339,1340,-1,1341,1342,1343,-1,1344,1345,1346,-1,1347,1348,1349,-1,1350,1351,1352,-1,1353,1354,1355,-1,1356,1357,1358,-1,1359,1360,1361,-1,1362,1363,1364,-1,1365,1366,1367,-1,1368,1369,1370,-1,1371,1372,1373,-1,1374,1375,1376,-1,1377,1378,1379,-1,1380,1381,1382,-1,1383,1384,1385,-1,1386,1387,1388,-1,1389,1390,1391,-1,1392,1393,1394,-1,1395,1396,1397,-1,1398,1399,1400,-1,1401,1402,1403,-1,1404,1405,1406,-1,1407,1408,1409,-1,1410,1411,1412,-1,1413,1414,1415,-1,1416,1417,1418,-1,1419,1420,1421,-1,1422,1423,1424,-1,1425,1426,1427,-1,1428,1429,1430,-1,1431,1432,1433,-1,1434,1435,1436,-1,1437,1438,1439,-1,1440,1441,1442,-1,1443,1444,1445,-1,1446,1447,1448,-1,1449,1450,1451,-1,1452,1453,1454,-1,1455,1456,1457,-1,1458,1459,1460,-1,1461,1462,1463,-1,1464,1465,1466,-1,1467,1468,1469,-1,1470,1471,1472,-1,1473,1474,1475,-1,1476,1477,1478,-1,1479,1480,1481,-1,1482,1483,1484,-1,1485,1486,1487,-1,1488,1489,1490,-1,1491,1492,1493,-1,1494,1495,1496,-1,1497,1498,1499,-1,1500,1501,1502,-1,1503,1504,1505,-1,1506,1507,1508,-1,1509,1510,1511,-1,1512,1513,1514,-1,1515,1516,1517,-1,1518,1519,1520,-1,1521,1522,1523,-1,1524,1525,1526,-1,1527,1528,1529,-1,1530,1531,1532,-1,1533,1534,1535,-1,1536,1537,1538,-1,1539,1540,1541,-1,1542,1543,1544,-1,1545,1546,1547,-1,1548,1549,1550,-1,1551,1552,1553,-1,1554,1555,1556,-1,1557,1558,1559,-1,1560,1561,1562,-1,1563,1564,1565,-1,1566,1567,1568,-1,1569,1570,1571,-1,1572,1573,1574,-1,1575,1576,1577,-1,1578,1579,1580,-1,1581,1582,1583,-1,1584,1585,1586,-1,1587,1588,1589,-1,1590,1591,1592,-1,1593,1594,1595,-1,1596,1597,1598,-1,1599,1600,1601,-1,1602,1603,1604,-1,1605,1606,1607,-1,1608,1609,1610,-1,1611,1612,1613,-1,1614,1615,1616,-1,1617,1618,1619,-1,1620,1621,1622,-1,1623,1624,1625,-1,1626,1627,1628,-1,1629,1630,1631,-1,1632,1633,1634,-1,1635,1636,1637,-1,1638,1639,1640,-1,1641,1642,1643,-1,1644,1645,1646,-1,1647,1648,1649,-1,1650,1651,1652,-1,1653,1654,1655,-1,1656,1657,1658,-1,1659,1660,1661,-1,1662,1663,1664,-1,1665,1666,1667,-1,1668,1669,1670,-1,1671,1672,1673,-1,1674,1675,1676,-1,1677,1678,1679,-1,1680,1681,1682,-1,1683,1684,1685,-1,1686,1687,1688,-1,1689,1690,1691,-1,1692,1693,1694,-1,1695,1696,1697,-1,1698,1699,1700,-1,1701,1702,1703,-1,1704,1705,1706,-1,1707,1708,1709,-1,1710,1711,1712,-1,1713,1714,1715,-1,1716,1717,1718,-1,1719,1720,1721,-1,1722,1723,1724,-1,1725,1726,1727,-1,1728,1729,1730,-1,1731,1732,1733,-1,1734,1735,1736,-1,1737,1738,1739,-1,1740,1741,1742,-1,1743,1744,1745,-1,1746,1747,1748,-1,1749,1750,1751,-1,1752,1753,1754,-1,1755,1756,1757,-1,1758,1759,1760,-1,1761,1762,1763,-1,1764,1765,1766,-1,1767,1768,1769,-1,1770,1771,1772,-1,1773,1774,1775,-1,1776,1777,1778,-1,1779,1780,1781,-1,1782,1783,1784,-1,1785,1786,1787,-1,1788,1789,1790,-1,1791,1792,1793,-1,1794,1795,1796,-1,1797,1798,1799,-1,1800,1801,1802,-1,1803,1804,1805,-1,1806,1807,1808,-1,1809,1810,1811,-1,1812,1813,1814,-1,1815,1816,1817,-1,1818,1819,1820,-1,1821,1822,1823,-1,1824,1825,1826,-1,1827,1828,1829,-1,1830,1831,1832,-1,1830,1832,1833,-1]
IndexedFaceSet379.creaseAngle = 1.57
Coordinate380 = x3d.Coordinate()

IndexedFaceSet379.coord = Coordinate380

Shape375.geometry = IndexedFaceSet379

Transform374.children.append(Shape375)

fieldValue373.children.append(Transform374)

ProtoInstance371.fieldValue.append(fieldValue373)

fieldValue370.children.append(ProtoInstance371)
ProtoInstance381 = x3d.ProtoInstance()
ProtoInstance381.name = "Joint"
ProtoInstance381.DEF = "Allen_hanim_r_ankle"
fieldValue382 = x3d.fieldValue()
fieldValue382.name = "name"
fieldValue382.value = "r_ankle"

ProtoInstance381.fieldValue.append(fieldValue382)
fieldValue383 = x3d.fieldValue()
fieldValue383.name = "center"
fieldValue383.value = "-0.064 0.0753 -0.0412"

ProtoInstance381.fieldValue.append(fieldValue383)
fieldValue384 = x3d.fieldValue()
fieldValue384.name = "children"
ProtoInstance385 = x3d.ProtoInstance()
ProtoInstance385.name = "Segment"
ProtoInstance385.DEF = "Allen_hanim_r_hindfoot"
fieldValue386 = x3d.fieldValue()
fieldValue386.name = "name"
fieldValue386.value = "r_hindfoot"

ProtoInstance385.fieldValue.append(fieldValue386)
fieldValue387 = x3d.fieldValue()
fieldValue387.name = "children"
Transform388 = x3d.Transform()
Transform388.DEF = "r_foot_adjust"
Transform388.center = [0.3319,1.1,-0.04]
Transform388.rotation = [0,1,0,1.570796]
Transform388.scale = [0.1,0.1,0.1]
Shape389 = x3d.Shape()
Appearance390 = x3d.Appearance()
Material391 = x3d.Material()
Material391.USE = "Shoe_Color"

Appearance390.material = Material391

Shape389.appearance = Appearance390
IndexedFaceSet392 = x3d.IndexedFaceSet()
IndexedFaceSet392.coordIndex = [0,1,2,-1,3,4,5,-1,6,7,8,-1,9,10,11,-1,12,13,14,-1,15,16,17,-1,18,19,20,-1,21,22,23,-1,24,25,26,-1,27,28,29,-1,30,31,32,-1,33,34,35,-1,36,37,38,-1,39,40,41,-1,42,43,44,-1,45,46,47,-1,48,49,50,-1,51,52,53,-1,54,55,56,-1,57,58,59,-1,60,61,62,-1,63,64,65,-1,66,67,68,-1,69,70,71,-1,72,73,74,-1,75,76,77,-1,78,79,80,-1,81,82,83,-1,84,85,86,-1,87,88,89,-1,90,91,92,-1,93,94,95,-1,96,97,98,-1,99,100,101,-1,102,103,104,-1,105,106,107,-1,108,109,110,-1,111,112,113,-1,114,115,116,-1,117,118,119,-1,120,121,122,-1,123,124,125,-1,126,127,128,-1,129,130,131,-1,132,133,134,-1,135,136,137,-1,138,139,140,-1,141,142,143,-1,144,145,146,-1,147,148,149,-1,150,151,152,-1,153,154,155,-1,156,157,158,-1,159,160,161,-1,162,163,164,-1,165,166,167,-1,168,169,170,-1,171,172,173,-1,174,175,176,-1,177,178,179,-1,180,181,182,-1,183,184,185,-1,186,187,188,-1,189,190,191,-1,192,193,194,-1,195,196,197,-1,198,199,200,-1,201,202,203,-1,204,205,206,-1,207,208,209,-1,210,211,212,-1,213,214,215,-1,216,217,218,-1,219,220,221,-1,222,223,224,-1,225,226,227,-1,228,229,230,-1,231,232,233,-1,234,235,236,-1,237,238,239,-1,240,241,242,-1,243,244,245,-1,246,247,248,-1,249,250,251,-1,252,253,254,-1,255,256,257,-1,258,259,260,-1,261,262,263,-1,264,265,266,-1,267,268,269,-1,270,271,272,-1,273,274,275,-1,276,277,278,-1,279,280,281,-1,282,283,284,-1,285,286,287,-1,288,289,290,-1,291,292,293,-1,294,295,296,-1,297,298,299,-1,300,301,302,-1,303,304,305,-1,306,307,308,-1,309,310,311,-1,312,313,314,-1,315,316,317,-1,318,319,320,-1,321,322,323,-1,324,325,326,-1,327,328,329,-1,330,331,332,-1,333,334,335,-1,336,337,338,-1,339,340,341,-1,342,343,344,-1,345,346,347,-1,348,349,350,-1,351,352,353,-1,354,355,356,-1,357,358,359,-1,360,361,362,-1,363,364,365,-1,366,367,368,-1,369,370,371,-1,372,373,374,-1,375,376,377,-1,378,379,380,-1,381,382,383,-1,384,385,386,-1,387,388,389,-1,390,391,392,-1,393,394,395,-1,396,397,398,-1,399,400,401,-1,402,403,404,-1,405,406,407,-1,408,409,410,-1,411,412,413,-1,414,415,416,-1,417,418,419,-1,420,421,422,-1,423,424,425,-1,426,427,428,-1,429,430,431,-1,432,433,434,-1,435,436,437,-1,438,439,440,-1,441,442,443,-1,444,445,446,-1,447,448,449,-1,450,451,452,-1,453,454,455,-1,456,457,458,-1,459,460,461,-1,462,463,464,-1,465,466,467,-1,468,469,470,-1,471,472,473,-1,474,475,476,-1,477,478,479,-1,480,481,482,-1,483,484,485,-1,486,487,488,-1,489,490,491,-1,492,493,494,-1,495,496,497,-1,498,499,500,-1,501,502,503,-1,504,505,506,-1,507,508,509,-1,510,511,512,-1,513,514,515,-1,516,517,518,-1,519,520,521,-1,522,523,524,-1,525,526,527,-1,528,529,530,-1,531,532,533,-1,534,535,536,-1,537,538,539,-1,540,541,542,-1,543,544,545,-1,546,547,548,-1,549,550,551,-1,552,553,554,-1,555,556,557,-1,558,559,560,-1,561,562,563,-1,564,565,566,-1,567,568,569,-1,570,571,572,-1,573,574,575,-1,576,577,578,-1,579,580,581,-1,582,583,584,-1,585,586,587,-1,588,589,590,-1,591,592,593,-1,594,595,596,-1,597,598,599,-1,600,601,602,-1,603,604,605,-1,606,607,608,-1,609,610,611,-1,612,613,614,-1,615,616,617,-1,618,619,620,-1,621,622,623,-1,624,625,626,-1,627,628,629,-1,630,631,632,-1,633,634,635,-1,636,637,638,-1,639,640,641,-1,642,643,644,-1,645,646,647,-1,648,649,650,-1,651,652,653,-1,654,655,656,-1,657,658,659,-1,660,661,662,-1,663,664,665,-1,666,667,668,-1,669,670,671,-1,672,673,674,-1,675,676,677,-1,678,679,680,-1,681,682,683,-1,684,685,686,-1,687,688,689,-1,690,691,692,-1,693,694,695,-1,696,697,698,-1,699,700,701,-1,702,703,704,-1,705,706,707,-1,708,709,710,-1,711,712,713,-1,714,715,716,-1,717,718,719,-1,720,721,722,-1,723,724,725,-1,726,727,728,-1,729,730,731,-1,732,733,734,-1,735,736,737,-1,738,739,740,-1,741,742,743,-1,744,745,746,-1,747,748,749,-1,750,751,752,-1,753,754,755,-1,756,757,758,-1,759,760,761,-1,762,763,764,-1,765,766,767,-1,768,769,770,-1,771,772,773,-1,774,775,776,-1,777,778,779,-1,780,781,782,-1,783,784,785,-1,786,787,788,-1,789,790,791,-1,792,793,794,-1,795,796,797,-1,798,799,800,-1,801,802,803,-1,804,805,806,-1,807,808,809,-1,810,811,812,-1,813,814,815,-1,816,817,818,-1,819,820,821,-1,822,823,824,-1,825,826,827,-1,828,829,830,-1,831,832,833,-1,834,835,836,-1,837,838,839,-1,840,841,842,-1,843,844,845,-1,846,847,848,-1,849,850,851,-1,852,853,854,-1,855,856,857,-1,858,859,860,-1,861,862,863,-1,864,865,866,-1,867,868,869,-1,870,871,872,-1,873,874,875,-1,876,877,878,-1,879,880,881,-1,882,883,884,-1,885,886,887,-1,888,889,890,-1,891,892,893,-1,894,895,896,-1,897,898,899,-1,900,901,902,-1,903,904,905,-1,906,907,908,-1,909,910,911,-1,912,913,914,-1,915,916,917,-1,918,919,920,-1,921,922,923,-1,924,925,926,-1,927,928,929,-1,930,931,932,-1,933,934,935,-1,936,937,938,-1,939,940,941,-1,942,943,944,-1,945,946,947,-1,948,949,950,-1,951,952,953,-1,954,955,956,-1,957,958,959,-1,960,961,962,-1,963,964,965,-1,966,967,968,-1,969,970,971,-1,972,973,974,-1,975,976,977,-1,978,979,980,-1,981,982,983,-1,984,985,986,-1,987,988,989,-1,990,991,992,-1,993,994,995,-1,996,997,998,-1,999,1000,1001,-1,1002,1003,1004,-1,1005,1006,1007,-1,1008,1009,1010,-1,1011,1012,1013,-1,1014,1015,1016,-1,1017,1018,1019,-1,1020,1021,1022,-1,1023,1024,1025,-1,1026,1027,1028,-1,1029,1030,1031,-1,1032,1033,1034,-1,1035,1036,1037,-1,1038,1039,1040,-1,1041,1042,1043,-1,1044,1045,1046,-1,1047,1048,1049,-1,1050,1051,1052,-1,1053,1054,1055,-1,1056,1057,1058,-1,1059,1060,1061,-1,1062,1063,1064,-1,1065,1066,1067,-1,1068,1069,1070,-1,1071,1072,1073,-1,1074,1075,1076,-1,1077,1078,1079,-1,1080,1081,1082,-1,1083,1084,1085,-1,1086,1087,1088,-1,1089,1090,1091,-1,1092,1093,1094,-1,1095,1096,1097,-1,1098,1099,1100,-1,1101,1102,1103,-1,1104,1105,1106,-1,1107,1108,1109,-1,1110,1111,1112,-1,1113,1114,1115,-1,1116,1117,1118,-1,1119,1120,1121,-1,1122,1123,1124,-1,1125,1126,1127,-1,1128,1129,1130,-1,1131,1132,1133,-1,1134,1135,1136,-1,1137,1138,1139,-1,1140,1141,1142,-1,1143,1144,1145,-1,1146,1147,1148,-1,1149,1150,1151,-1,1152,1153,1154,-1,1155,1156,1157,-1,1158,1159,1160,-1,1161,1162,1163,-1,1164,1165,1166,-1,1167,1168,1169,-1,1170,1171,1172,-1,1173,1174,1175,-1,1176,1177,1178,-1,1179,1180,1181,-1,1182,1183,1184,-1,1185,1186,1187,-1,1188,1189,1190,-1,1191,1192,1193,-1,1194,1195,1196,-1,1197,1198,1199,-1,1200,1201,1202,-1,1203,1204,1205,-1,1206,1207,1208,-1,1209,1210,1211,-1,1212,1213,1214,-1,1215,1216,1217,-1,1218,1219,1220,-1,1221,1222,1223,-1,1224,1225,1226,-1,1227,1228,1229,-1,1230,1231,1232,-1,1233,1234,1235,-1,1236,1237,1238,-1,1239,1240,1241,-1,1242,1243,1244,-1,1245,1246,1247,-1,1248,1249,1250,-1,1251,1252,1253,-1,1254,1255,1256,-1,1257,1258,1259,-1,1260,1261,1262,-1,1263,1264,1265,-1,1266,1267,1268,-1,1269,1270,1271,-1,1272,1273,1274,-1,1275,1276,1277,-1,1278,1279,1280,-1,1281,1282,1283,-1,1284,1285,1286,-1,1287,1288,1289,-1,1290,1291,1292,-1,1293,1294,1295,-1,1296,1297,1298,-1,1299,1300,1301,-1,1302,1303,1304,-1,1305,1306,1307,-1,1308,1309,1310,-1,1311,1312,1313,-1,1314,1315,1316,-1,1317,1318,1319,-1,1320,1321,1322,-1,1323,1324,1325,-1,1326,1327,1328,-1,1329,1330,1331,-1,1332,1333,1334,-1,1335,1336,1337,-1,1338,1339,1340,-1,1341,1342,1343,-1,1344,1345,1346,-1,1347,1348,1349,-1,1350,1351,1352,-1,1353,1354,1355,-1,1356,1357,1358,-1,1359,1360,1361,-1,1362,1363,1364,-1,1365,1366,1367,-1,1368,1369,1370,-1,1371,1372,1373,-1,1374,1375,1376,-1,1377,1378,1379,-1,1380,1381,1382,-1,1383,1384,1385,-1,1386,1387,1388,-1,1389,1390,1391,-1,1392,1393,1394,-1,1395,1396,1397,-1,1398,1399,1400,-1,1401,1402,1403,-1,1404,1405,1406,-1,1407,1408,1409,-1,1410,1411,1412,-1,1413,1414,1415,-1,1416,1417,1418,-1,1419,1420,1421,-1,1422,1423,1424,-1,1425,1426,1427,-1,1428,1429,1430,-1,1431,1432,1433,-1,1434,1435,1436,-1,1437,1438,1439,-1,1440,1441,1442,-1,1443,1444,1445,-1,1446,1447,1448,-1,1449,1450,1451,-1,1452,1453,1454,-1,1455,1456,1457,-1,1458,1459,1460,-1,1461,1462,1463,-1,1464,1465,1466,-1,1467,1468,1469,-1,1470,1471,1472,-1,1473,1474,1475,-1,1476,1477,1478,-1,1479,1480,1481,-1,1482,1483,1484,-1,1485,1486,1487,-1,1488,1489,1490,-1,1491,1492,1493,-1,1494,1495,1496,-1,1497,1498,1499,-1,1500,1501,1502,-1,1503,1504,1505,-1,1506,1507,1508,-1,1509,1510,1511,-1,1512,1513,1514,-1,1515,1516,1517,-1,1518,1519,1520,-1,1521,1522,1523,-1,1524,1525,1526,-1,1527,1528,1529,-1,1530,1531,1532,-1,1533,1534,1535,-1,1536,1537,1538,-1,1539,1540,1541,-1,1542,1543,1544,-1,1545,1546,1547,-1,1548,1549,1550,-1,1551,1552,1553,-1,1554,1555,1556,-1,1557,1558,1559,-1,1560,1561,1562,-1,1563,1564,1565,-1,1566,1567,1568,-1,1569,1570,1571,-1,1572,1573,1574,-1,1575,1576,1577,-1,1578,1579,1580,-1,1581,1582,1583,-1,1584,1585,1586,-1,1587,1588,1589,-1,1590,1591,1592,-1,1593,1594,1595,-1,1596,1597,1598,-1,1599,1600,1601,-1,1602,1603,1604,-1,1605,1606,1607,-1,1608,1609,1610,-1,1611,1612,1613,-1,1614,1615,1616,-1,1617,1618,1619,-1,1620,1621,1622,-1,1623,1624,1625,-1,1626,1627,1628,-1,1629,1630,1631,-1,1632,1633,1634,-1,1635,1636,1637,-1,1638,1639,1640,-1,1641,1642,1643,-1,1644,1645,1646,-1,1647,1648,1649,-1,1650,1651,1652,-1,1653,1654,1655,-1,1656,1657,1658,-1,1659,1660,1661,-1,1662,1663,1664,-1,1665,1666,1667,-1,1668,1669,1670,-1,1671,1672,1673,-1,1674,1675,1676,-1,1677,1678,1679,-1,1680,1681,1682,-1,1683,1684,1685,-1,1686,1687,1688,-1,1689,1690,1691,-1,1692,1693,1694,-1,1695,1696,1697,-1,1698,1699,1700,-1,1701,1702,1703,-1,1704,1705,1706,-1,1707,1708,1709,-1,1710,1711,1712,-1]
IndexedFaceSet392.creaseAngle = 1.57
Coordinate393 = x3d.Coordinate()

IndexedFaceSet392.coord = Coordinate393

Shape389.geometry = IndexedFaceSet392

Transform388.children.append(Shape389)

fieldValue387.children.append(Transform388)

ProtoInstance385.fieldValue.append(fieldValue387)

fieldValue384.children.append(ProtoInstance385)

ProtoInstance381.fieldValue.append(fieldValue384)

fieldValue370.children.append(ProtoInstance381)

ProtoInstance367.fieldValue.append(fieldValue370)

fieldValue356.children.append(ProtoInstance367)

ProtoInstance353.fieldValue.append(fieldValue356)

fieldValue301.children.append(ProtoInstance353)

ProtoInstance298.fieldValue.append(fieldValue301)

fieldValue297.children.append(ProtoInstance298)
ProtoInstance394 = x3d.ProtoInstance()
ProtoInstance394.name = "Joint"
ProtoInstance394.DEF = "Allen_hanim_vl1"
fieldValue395 = x3d.fieldValue()
fieldValue395.name = "name"
fieldValue395.value = "vl1"

ProtoInstance394.fieldValue.append(fieldValue395)
fieldValue396 = x3d.fieldValue()
fieldValue396.name = "center"
fieldValue396.value = "-0.00405 1.07 -0.0275"

ProtoInstance394.fieldValue.append(fieldValue396)
fieldValue397 = x3d.fieldValue()
fieldValue397.name = "children"
ProtoInstance398 = x3d.ProtoInstance()
ProtoInstance398.name = "Segment"
ProtoInstance398.DEF = "Allen_hanim_c7"
fieldValue399 = x3d.fieldValue()
fieldValue399.name = "name"
fieldValue399.value = "l1"

ProtoInstance398.fieldValue.append(fieldValue399)
fieldValue400 = x3d.fieldValue()
fieldValue400.name = "children"
Transform401 = x3d.Transform()
Transform401.DEF = "torso_adjust"
Transform401.center = [0,1,0]
Transform401.rotation = [0,1,0,1.570796]
Transform401.scale = [0.1,0.1,0.1]
Shape402 = x3d.Shape()
Appearance403 = x3d.Appearance()
Material404 = x3d.Material()
Material404.DEF = "Shirt_Color"
Material404.ambientIntensity = 0.25
Material404.diffuseColor = [0.6,0.0745,0.1137]

Appearance403.material = Material404
ImageTexture405 = x3d.ImageTexture()
ImageTexture405.USE = "camo"

Appearance403.texture = ImageTexture405

Shape402.appearance = Appearance403
IndexedFaceSet406 = x3d.IndexedFaceSet()
IndexedFaceSet406.coordIndex = [0,1,2,-1,3,4,5,-1,6,7,8,-1,9,10,11,-1,12,13,14,-1,15,16,17,-1,18,19,20,-1,21,22,23,-1,24,25,26,-1,27,28,29,-1,30,31,32,-1,33,34,35,-1,36,37,38,-1,39,40,41,-1,42,43,44,-1,45,46,47,-1,48,49,50,-1,53,57,58,-1,62,59,60,-1,67,68,69,-1,70,65,71,-1,76,77,78,-1,77,73,54,-1,79,55,80,-1,55,56,80,-1,59,62,52,-1,78,77,75,-1,64,79,80,-1,51,52,82,-1,83,84,82,-1,62,60,85,-1,86,87,88,-1,88,69,68,-1,89,76,78,-1,77,54,75,-1,78,75,66,-1,89,58,57,-1,53,90,57,-1,90,64,91,-1,63,79,64,-1,80,92,93,-1,92,80,56,-1,94,95,62,-1,85,69,88,-1,71,96,67,-1,97,71,65,-1,54,73,72,-1,58,89,78,-1,83,82,52,-1,98,62,87,-1,99,68,67,-1,70,67,69,-1,100,71,97,-1,438,101,74,-1,102,103,435,-1,53,64,90,-1,91,64,93,-1,81,104,56,-1,84,105,82,-1,106,83,107,-1,106,84,83,-1,95,107,52,-1,98,94,62,-1,86,88,108,-1,85,88,87,-1,68,108,88,-1,68,99,108,-1,99,67,96,-1,71,67,70,-1,100,96,71,-1,100,97,109,-1,110,109,111,-1,438,112,101,-1,103,112,435,-1,101,103,113,-1,102,114,115,-1,116,113,115,-1,117,90,91,-1,64,80,93,-1,92,56,104,-1,61,118,81,-1,105,119,51,-1,120,119,121,-1,107,83,52,-1,62,95,52,-1,95,94,122,-1,62,85,87,-1,123,98,87,-1,123,87,86,-1,86,108,124,-1,108,99,124,-1,110,100,109,-1,103,115,113,-1,103,102,115,-1,125,91,93,-1,104,81,126,-1,118,127,126,-1,120,121,128,-1,121,84,106,-1,121,105,84,-1,95,129,107,-1,129,95,122,-1,130,122,94,-1,130,94,131,-1,94,98,131,-1,132,110,133,-1,110,111,133,-1,134,135,136,-1,101,112,103,-1,135,101,113,-1,116,115,114,-1,137,138,116,-1,104,126,139,-1,139,126,127,-1,127,118,140,-1,118,126,81,-1,140,61,51,-1,140,118,61,-1,119,140,51,-1,119,120,140,-1,105,121,119,-1,82,105,51,-1,128,121,106,-1,141,142,133,-1,143,133,111,-1,101,135,74,-1,144,145,146,-1,144,146,147,-1,148,149,150,-1,151,150,149,-1,152,151,149,-1,153,154,155,-1,156,157,158,-1,159,160,154,-1,137,161,138,-1,162,163,145,-1,164,165,163,-1,166,167,168,-1,168,169,162,-1,168,164,169,-1,170,160,157,-1,156,170,157,-1,159,143,160,-1,143,141,133,-1,143,157,160,-1,136,138,161,-1,171,136,163,-1,164,167,158,-1,170,155,154,-1,156,151,155,-1,157,143,111,-1,146,163,136,-1,167,166,158,-1,168,167,164,-1,164,158,173,-1,156,155,170,-1,160,170,154,-1,159,141,143,-1,156,150,151,-1,136,161,147,-1,163,162,169,-1,166,150,156,-1,165,164,173,-1,138,113,116,-1,113,138,136,-1,163,146,145,-1,166,156,158,-1,175,176,157,-1,178,173,179,-1,135,113,136,-1,146,136,147,-1,157,111,172,-1,180,135,181,-1,164,163,169,-1,165,182,163,-1,183,175,157,-1,135,134,181,-1,157,176,158,-1,178,182,165,-1,180,184,185,-1,184,186,187,-1,134,188,186,-1,171,188,136,-1,182,171,163,-1,184,180,181,-1,134,186,181,-1,182,190,171,-1,187,191,192,-1,188,134,136,-1,193,194,183,-1,181,186,184,-1,195,190,182,-1,195,182,178,-1,196,197,198,-1,199,200,179,-1,199,158,176,-1,174,183,157,-1,183,177,193,-1,188,187,186,-1,190,201,171,-1,195,178,197,-1,178,165,173,-1,171,201,188,-1,203,190,195,-1,204,205,206,-1,206,175,194,-1,175,183,194,-1,189,193,177,-1,203,195,207,-1,203,201,190,-1,203,207,196,-1,197,207,195,-1,185,184,187,-1,207,197,196,-1,196,198,208,-1,192,185,187,-1,208,209,210,-1,201,211,188,-1,197,178,198,-1,175,206,176,-1,205,176,206,-1,201,203,196,-1,187,188,211,-1,172,174,157,-1,198,178,179,-1,187,211,191,-1,201,196,211,-1,173,158,199,-1,213,214,215,-1,196,208,211,-1,204,206,194,-1,216,205,204,-1,217,194,212,-1,193,212,194,-1,205,218,199,-1,205,216,218,-1,217,219,214,-1,204,217,214,-1,220,215,219,-1,198,179,222,-1,205,199,176,-1,193,202,212,-1,191,221,192,-1,179,173,199,-1,217,204,194,-1,213,216,214,-1,217,212,219,-1,219,215,214,-1,213,215,223,-1,218,213,225,-1,215,226,223,-1,223,225,213,-1,227,221,191,-1,179,200,222,-1,210,228,229,-1,218,216,213,-1,227,191,210,-1,227,210,229,-1,209,230,231,-1,230,208,198,-1,232,230,198,-1,200,218,225,-1,199,218,200,-1,226,233,234,-1,210,235,228,-1,230,209,208,-1,236,237,225,-1,235,238,239,-1,240,200,225,-1,241,228,242,-1,211,210,191,-1,211,208,210,-1,243,240,237,-1,238,235,210,-1,209,238,210,-1,209,231,238,-1,238,231,239,-1,232,245,246,-1,198,222,232,-1,222,240,245,-1,226,215,220,-1,247,248,232,-1,248,239,231,-1,226,220,233,-1,248,231,230,-1,216,204,214,-1,242,228,235,-1,247,235,239,-1,236,225,223,-1,223,234,236,-1,223,226,234,-1,234,233,251,-1,236,252,237,-1,253,252,236,-1,224,249,251,-1,254,241,242,-1,247,239,248,-1,255,256,257,-1,243,258,245,-1,240,222,200,-1,237,240,225,-1,234,259,236,-1,254,260,250,-1,246,245,261,-1,240,243,245,-1,247,242,235,-1,255,247,256,-1,234,251,259,-1,262,251,249,-1,248,230,232,-1,233,224,251,-1,255,257,264,-1,252,243,237,-1,242,255,254,-1,265,253,236,-1,224,244,249,-1,255,260,254,-1,232,222,245,-1,252,266,267,-1,265,268,253,-1,259,269,265,-1,255,264,260,-1,243,267,258,-1,259,265,236,-1,270,253,268,-1,251,262,259,-1,262,269,259,-1,243,252,267,-1,252,253,266,-1,267,272,258,-1,261,258,272,-1,269,268,265,-1,269,273,268,-1,273,269,262,-1,264,257,274,-1,246,247,232,-1,275,267,266,-1,273,262,271,-1,246,261,276,-1,255,242,247,-1,253,270,266,-1,275,266,273,-1,273,270,268,-1,262,249,263,-1,256,246,277,-1,245,258,261,-1,261,272,278,-1,273,266,270,-1,279,280,281,-1,256,282,257,-1,246,256,247,-1,267,283,272,-1,267,275,283,-1,261,278,284,-1,272,285,278,-1,286,277,287,-1,288,282,256,-1,279,289,275,-1,274,290,291,-1,288,256,277,-1,286,288,277,-1,292,279,281,-1,274,257,290,-1,288,293,282,-1,286,293,288,-1,294,286,287,-1,272,283,285,-1,282,293,290,-1,294,290,293,-1,293,286,294,-1,294,287,295,-1,246,287,277,-1,246,276,287,-1,279,275,273,-1,261,297,276,-1,279,273,280,-1,289,283,275,-1,273,271,280,-1,290,294,295,-1,289,285,283,-1,298,299,300,-1,297,261,284,-1,301,292,281,-1,291,300,302,-1,257,282,290,-1,295,291,290,-1,303,276,297,-1,279,304,289,-1,305,302,300,-1,285,289,304,-1,306,304,307,-1,276,298,287,-1,278,285,306,-1,299,309,300,-1,279,292,304,-1,305,300,309,-1,295,300,291,-1,285,304,306,-1,310,304,292,-1,309,308,305,-1,307,311,306,-1,278,306,284,-1,295,298,300,-1,310,292,301,-1,307,304,310,-1,312,309,313,-1,299,313,309,-1,311,314,306,-1,315,316,313,-1,306,314,284,-1,301,317,310,-1,314,311,318,-1,319,307,310,-1,314,321,284,-1,314,318,321,-1,307,318,311,-1,298,295,287,-1,321,318,319,-1,318,307,319,-1,322,297,284,-1,323,324,319,-1,320,312,313,-1,316,325,313,-1,301,296,317,-1,303,297,322,-1,326,303,322,-1,321,322,284,-1,327,325,316,-1,325,328,329,-1,316,315,330,-1,322,319,324,-1,331,326,332,-1,313,299,298,-1,303,315,313,-1,333,317,334,-1,335,336,337,-1,326,315,303,-1,317,333,310,-1,325,320,313,-1,338,323,319,-1,303,298,276,-1,326,331,315,-1,323,339,340,-1,326,322,324,-1,303,313,298,-1,322,321,319,-1,342,339,343,-1,344,328,345,-1,346,327,316,-1,347,348,330,-1,315,331,349,-1,324,323,350,-1,328,327,351,-1,315,349,330,-1,352,331,332,-1,350,323,340,-1,353,337,354,-1,330,349,347,-1,349,355,347,-1,355,349,352,-1,349,331,352,-1,352,332,356,-1,357,324,350,-1,358,357,350,-1,353,335,337,-1,335,316,336,-1,336,359,360,-1,359,330,348,-1,436,356,361,-1,332,326,324,-1,357,332,324,-1,357,362,363,-1,364,350,365,-1,366,365,340,-1,333,319,310,-1,336,360,337,-1,348,361,360,-1,356,369,361,-1,332,369,356,-1,363,332,357,-1,357,358,362,-1,358,350,364,-1,358,364,370,-1,365,350,340,-1,333,338,319,-1,329,328,344,-1,371,372,351,-1,335,346,316,-1,330,359,336,-1,359,348,360,-1,369,373,360,-1,369,360,361,-1,374,369,332,-1,370,375,376,-1,376,375,374,-1,376,358,370,-1,376,362,358,-1,376,363,362,-1,325,327,328,-1,351,377,378,-1,353,379,335,-1,316,330,336,-1,360,373,380,-1,374,373,369,-1,363,376,374,-1,363,374,332,-1,343,381,382,-1,383,384,385,-1,329,344,386,-1,387,371,346,-1,374,437,373,-1,390,370,365,-1,370,364,365,-1,366,340,391,-1,392,340,339,-1,340,392,391,-1,323,338,339,-1,328,393,345,-1,346,351,327,-1,351,372,377,-1,346,371,351,-1,387,394,395,-1,395,372,371,-1,387,395,371,-1,396,394,387,-1,337,380,354,-1,370,397,389,-1,390,397,370,-1,365,366,390,-1,398,391,342,-1,391,392,342,-1,338,343,339,-1,338,383,381,-1,386,368,329,-1,386,400,401,-1,386,344,400,-1,402,344,403,-1,402,400,344,-1,378,393,328,-1,378,328,351,-1,404,378,405,-1,377,405,378,-1,395,377,372,-1,439,395,394,-1,335,387,346,-1,380,337,360,-1,366,407,390,-1,407,366,391,-1,342,392,339,-1,402,408,400,-1,387,335,379,-1,353,409,379,-1,354,409,353,-1,410,391,398,-1,384,411,385,-1,412,413,384,-1,399,333,341,-1,402,403,414,-1,344,345,403,-1,393,404,415,-1,378,404,393,-1,406,416,415,-1,417,396,379,-1,417,409,418,-1,396,419,394,-1,417,379,409,-1,409,354,418,-1,407,391,410,-1,398,342,420,-1,421,342,343,-1,421,343,382,-1,399,383,338,-1,399,367,422,-1,343,338,381,-1,412,399,422,-1,399,338,333,-1,423,413,412,-1,415,416,393,-1,416,345,393,-1,396,387,379,-1,354,380,388,-1,385,411,426,-1,411,427,426,-1,383,385,428,-1,411,384,413,-1,412,384,399,-1,424,423,425,-1,414,429,431,-1,430,414,403,-1,429,414,430,-1,439,394,419,-1,426,428,385,-1,399,384,383,-1,432,433,424,-1,433,423,424,-1,433,413,423,-1,396,417,419,-1,354,388,418,-1,434,403,345,-1,70,440,65,-1,440,441,65,-1,441,442,65,-1,442,443,65,-1,443,444,65,-1,444,445,65,-1,445,446,65,-1,446,447,65,-1,447,448,65,-1,448,449,65,-1,449,450,65,-1,450,451,65,-1,451,452,65,-1,452,453,65,-1,453,454,65,-1,454,455,65,-1,455,456,65,-1,456,457,65,-1,457,458,65,-1,458,459,65,-1,462,463,461,-1,461,463,460,-1,460,463,459,-1,459,463,65,-1,329,368,325,-1,368,254,325,-1,325,254,320,-1,260,264,250,-1,274,291,264,-1,264,291,250,-1,291,302,250,-1,302,305,250,-1,305,312,250,-1,320,254,312,-1,250,312,254,-1,479,480,481,-1,482,483,484,-1,485,486,487,-1,483,480,484,-1,488,483,485,-1,488,485,487,-1,480,489,481,-1,490,480,491,-1,492,493,494,-1,486,485,482,-1,495,496,497,-1,495,497,498,-1,490,499,484,-1,483,489,480,-1,481,489,500,-1,479,491,480,-1,501,493,502,-1,494,493,501,-1,503,498,497,-1,504,497,505,-1,504,505,506,-1,485,483,482,-1,495,486,496,-1,492,494,507,-1,492,508,493,-1,509,510,507,-1,511,509,507,-1,504,506,512,-1,484,513,514,-1,507,510,515,-1,516,517,509,-1,509,511,516,-1,518,506,505,-1,506,518,519,-1,496,505,497,-1,492,507,515,-1,521,522,520,-1,522,517,520,-1,520,516,523,-1,520,517,516,-1,524,525,526,-1,525,527,528,-1,518,524,519,-1,514,529,482,-1,483,488,489,-1,502,491,501,-1,515,530,531,-1,533,534,535,-1,534,533,536,-1,486,482,496,-1,495,537,486,-1,484,499,513,-1,515,510,530,-1,533,539,536,-1,493,490,502,-1,492,540,508,-1,534,536,538,-1,542,527,543,-1,543,525,524,-1,544,536,545,-1,546,545,547,-1,542,543,505,-1,518,543,524,-1,490,484,480,-1,540,548,490,-1,493,508,490,-1,549,499,548,-1,550,540,541,-1,545,536,539,-1,542,539,527,-1,499,490,548,-1,502,490,491,-1,541,492,531,-1,527,539,533,-1,505,552,553,-1,549,548,554,-1,492,515,531,-1,544,538,536,-1,496,529,505,-1,496,482,529,-1,541,540,492,-1,551,544,545,-1,508,540,490,-1,545,539,542,-1,543,527,525,-1,514,482,484,-1,555,551,546,-1,514,556,529,-1,557,556,514,-1,513,557,514,-1,558,559,499,-1,549,554,560,-1,559,557,513,-1,559,513,499,-1,499,549,558,-1,542,505,553,-1,529,552,505,-1,557,559,563,-1,558,563,559,-1,560,554,564,-1,557,563,556,-1,554,550,565,-1,563,558,566,-1,541,532,562,-1,567,564,554,-1,568,550,541,-1,563,566,556,-1,569,570,561,-1,571,570,569,-1,556,573,529,-1,566,574,573,-1,548,540,554,-1,568,541,562,-1,850,561,570,-1,545,542,553,-1,549,560,558,-1,554,565,567,-1,568,565,550,-1,547,545,553,-1,569,575,576,-1,545,546,551,-1,543,518,505,-1,568,571,565,-1,556,566,573,-1,573,577,578,-1,560,566,558,-1,579,572,546,-1,579,547,580,-1,553,552,578,-1,574,581,573,-1,567,574,564,-1,573,581,577,-1,582,583,553,-1,529,573,552,-1,554,540,550,-1,569,565,571,-1,564,574,560,-1,576,567,565,-1,547,579,546,-1,584,585,586,-1,567,587,574,-1,572,579,591,-1,553,583,547,-1,592,553,578,-1,552,573,578,-1,592,582,553,-1,582,593,594,-1,566,560,574,-1,595,596,587,-1,569,576,565,-1,577,597,578,-1,584,581,574,-1,547,583,580,-1,577,581,599,-1,598,591,600,-1,580,600,591,-1,602,603,604,-1,577,599,597,-1,587,605,585,-1,597,606,592,-1,603,602,583,-1,583,582,603,-1,588,590,607,-1,604,594,608,-1,582,594,603,-1,593,609,610,-1,611,606,599,-1,579,580,591,-1,580,602,612,-1,610,613,593,-1,582,592,593,-1,578,597,592,-1,606,597,599,-1,601,595,587,-1,604,603,594,-1,596,605,587,-1,851,601,589,-1,593,611,609,-1,593,606,611,-1,574,587,585,-1,583,602,580,-1,593,608,594,-1,599,581,584,-1,584,611,599,-1,601,587,567,-1,600,580,612,-1,604,608,613,-1,584,574,585,-1,614,590,615,-1,586,617,618,-1,614,619,607,-1,614,607,590,-1,620,621,584,-1,586,605,617,-1,601,851,595,-1,576,601,567,-1,622,596,595,-1,623,614,615,-1,624,615,590,-1,625,616,612,-1,626,596,622,-1,627,623,628,-1,614,623,629,-1,628,623,615,-1,630,631,632,-1,633,628,630,-1,630,615,634,-1,625,612,602,-1,604,625,602,-1,586,620,584,-1,596,626,617,-1,632,635,626,-1,630,632,636,-1,630,628,615,-1,596,617,605,-1,638,639,631,-1,637,624,590,-1,625,641,616,-1,593,613,608,-1,634,615,624,-1,631,634,642,-1,631,630,634,-1,643,642,644,-1,646,625,604,-1,609,647,610,-1,626,648,617,-1,635,631,639,-1,632,631,635,-1,641,625,646,-1,646,649,650,-1,626,635,648,-1,651,638,652,-1,638,651,639,-1,653,643,644,-1,634,645,644,-1,644,642,634,-1,638,631,642,-1,652,654,655,-1,634,624,645,-1,641,656,657,-1,656,658,657,-1,648,659,618,-1,660,648,635,-1,660,659,648,-1,659,660,661,-1,643,662,663,-1,643,653,662,-1,849,655,665,-1,666,655,654,-1,651,652,655,-1,638,662,652,-1,655,667,665,-1,666,667,655,-1,662,668,652,-1,641,657,640,-1,669,670,649,-1,671,659,667,-1,659,671,672,-1,648,618,617,-1,672,673,620,-1,656,641,650,-1,674,656,650,-1,610,646,613,-1,586,618,620,-1,675,654,676,-1,849,651,655,-1,652,668,654,-1,668,664,677,-1,662,653,668,-1,641,640,616,-1,650,641,646,-1,669,678,670,-1,610,647,669,-1,646,669,649,-1,618,672,620,-1,671,667,666,-1,679,671,666,-1,675,666,654,-1,668,653,664,-1,610,669,646,-1,646,604,613,-1,679,666,675,-1,680,677,681,-1,675,676,682,-1,649,684,650,-1,685,686,647,-1,584,621,611,-1,585,605,586,-1,659,672,618,-1,676,687,680,-1,676,654,687,-1,688,683,656,-1,688,656,689,-1,656,674,689,-1,684,674,650,-1,678,686,685,-1,671,673,672,-1,690,691,692,-1,693,677,664,-1,692,682,676,-1,695,680,687,-1,674,696,689,-1,669,647,686,-1,621,697,609,-1,621,609,611,-1,621,620,697,-1,698,620,673,-1,699,700,670,-1,697,685,609,-1,682,692,679,-1,692,676,680,-1,680,695,677,-1,690,692,680,-1,693,681,677,-1,593,592,606,-1,671,702,673,-1,703,690,680,-1,674,684,696,-1,649,705,684,-1,702,671,679,-1,706,707,703,-1,703,707,708,-1,709,710,711,-1,670,712,649,-1,713,678,685,-1,714,715,716,-1,703,680,704,-1,694,696,701,-1,694,689,696,-1,685,647,609,-1,691,717,702,-1,706,703,704,-1,696,710,701,-1,700,699,718,-1,649,712,705,-1,670,713,719,-1,698,673,702,-1,698,702,717,-1,707,720,708,-1,710,696,711,-1,705,712,700,-1,669,686,678,-1,692,702,679,-1,680,681,704,-1,721,722,711,-1,709,711,722,-1,700,718,705,-1,711,696,684,-1,700,712,670,-1,692,691,702,-1,691,690,723,-1,724,708,725,-1,726,727,711,-1,713,728,719,-1,620,729,697,-1,690,703,708,-1,730,727,719,-1,718,726,711,-1,718,684,705,-1,721,711,727,-1,699,726,718,-1,719,699,670,-1,678,713,670,-1,729,685,697,-1,725,708,720,-1,718,711,684,-1,731,717,723,-1,690,732,723,-1,733,713,685,-1,734,698,717,-1,731,735,736,-1,691,723,717,-1,690,708,724,-1,728,739,719,-1,733,741,728,-1,733,742,741,-1,698,714,743,-1,744,715,745,-1,714,698,715,-1,734,736,745,-1,731,736,734,-1,731,723,735,-1,726,699,719,-1,717,731,734,-1,724,738,732,-1,740,746,747,-1,722,721,740,-1,726,719,727,-1,729,733,685,-1,742,743,714,-1,620,698,729,-1,715,734,745,-1,748,744,745,-1,749,750,732,-1,740,721,746,-1,751,746,721,-1,735,748,736,-1,751,721,727,-1,752,730,753,-1,730,754,753,-1,748,745,736,-1,749,732,738,-1,727,730,752,-1,739,730,719,-1,713,733,728,-1,756,716,744,-1,723,750,735,-1,690,724,732,-1,746,757,758,-1,759,751,752,-1,751,727,752,-1,739,728,741,-1,714,716,756,-1,715,698,734,-1,723,732,750,-1,738,737,755,-1,733,743,742,-1,760,742,714,-1,759,752,763,-1,735,750,749,-1,759,762,757,-1,746,751,757,-1,751,759,757,-1,754,764,753,-1,733,729,743,-1,744,748,765,-1,749,738,755,-1,730,739,754,-1,698,743,729,-1,766,735,749,-1,763,752,753,-1,739,767,754,-1,765,768,756,-1,759,769,762,-1,770,771,754,-1,742,760,741,-1,756,744,765,-1,766,768,765,-1,765,748,735,-1,766,755,761,-1,772,770,760,-1,744,716,715,-1,755,766,749,-1,766,765,735,-1,760,770,741,-1,764,754,773,-1,774,773,775,-1,773,754,775,-1,739,741,767,-1,770,767,741,-1,767,770,754,-1,769,776,777,-1,761,778,779,-1,766,779,768,-1,774,780,776,-1,753,764,763,-1,775,771,781,-1,756,760,714,-1,759,763,769,-1,771,775,754,-1,774,776,769,-1,780,774,775,-1,772,771,770,-1,768,782,756,-1,779,782,768,-1,761,783,778,-1,764,773,774,-1,763,774,769,-1,778,783,785,-1,763,764,774,-1,756,786,760,-1,761,779,766,-1,784,776,787,-1,786,771,772,-1,788,789,790,-1,791,779,792,-1,793,792,778,-1,792,779,778,-1,776,780,787,-1,780,775,794,-1,795,786,782,-1,778,785,796,-1,796,797,793,-1,796,793,778,-1,799,787,780,-1,782,786,756,-1,791,800,782,-1,801,787,802,-1,791,803,800,-1,793,803,792,-1,779,791,782,-1,791,792,803,-1,803,793,797,-1,796,785,798,-1,806,807,808,-1,787,799,802,-1,788,810,811,-1,788,811,812,-1,812,807,806,-1,794,799,780,-1,802,806,809,-1,794,806,799,-1,812,794,789,-1,786,813,781,-1,814,795,800,-1,800,803,797,-1,794,775,815,-1,786,772,760,-1,795,813,786,-1,816,817,818,-1,806,802,799,-1,794,812,806,-1,794,815,789,-1,775,781,815,-1,813,819,781,-1,813,820,819,-1,800,795,782,-1,798,821,816,-1,812,811,822,-1,812,822,804,-1,786,781,771,-1,821,823,816,-1,824,825,805,-1,796,798,816,-1,812,804,807,-1,816,814,800,-1,800,797,816,-1,788,812,789,-1,826,827,828,-1,824,805,822,-1,829,810,788,-1,795,814,813,-1,811,831,822,-1,788,790,832,-1,789,781,819,-1,835,825,824,-1,824,831,829,-1,811,810,831,-1,789,819,830,-1,831,824,822,-1,831,810,829,-1,827,826,817,-1,817,816,823,-1,836,834,825,-1,824,837,838,-1,816,818,814,-1,826,839,840,-1,797,796,816,-1,835,836,825,-1,835,824,838,-1,837,824,829,-1,837,829,788,-1,833,841,842,-1,835,843,836,-1,844,845,838,-1,789,815,781,-1,814,818,813,-1,842,827,817,-1,842,817,823,-1,817,826,840,-1,837,844,838,-1,789,830,790,-1,842,823,833,-1,846,844,837,-1,832,846,837,-1,832,837,788,-1,839,826,828,-1,847,820,818,-1,817,840,818,-1,818,820,813,-1,840,848,818,-1,848,847,818,-1,854,852,853,-1,855,856,857,-1,858,859,860,-1,861,862,863,-1,866,867,865,-1,865,867,864,-1,867,868,864,-1,874,875,873,-1,869,870,877,-1,870,871,877,-1,876,877,875,-1,875,877,873,-1,871,872,877,-1,873,877,872,-1,879,880,878,-1,878,880,882,-1,881,882,880,-1,883,884,885,-1,886,887,888,-1,889,890,891,-1,892,893,894,-1,895,896,897,-1,898,899,900,-1,901,902,903,-1,904,905,906,-1,907,908,909,-1,910,911,912,-1,913,914,915,-1,916,917,918,-1,919,920,921,-1,922,923,924,-1,925,926,927,-1,928,929,930,-1,931,932,933,-1,934,935,936,-1,937,938,939,-1,940,941,942,-1,943,944,945,-1,946,947,948,-1,949,950,951,-1,952,953,954,-1,955,956,957,-1,958,959,960,-1,961,962,963,-1,964,965,966,-1,967,968,969,-1,970,971,972,-1,973,974,975,-1,976,977,978,-1,979,980,981,-1,982,983,984,-1,985,986,987,-1,988,989,990,-1,991,992,993,-1,994,995,996,-1,997,998,999,-1,1000,1001,1002,-1,1003,1004,1005,-1,1006,1007,1008,-1,1009,1010,1011,-1,1012,1013,1014,-1,1015,1016,1017,-1,1018,1019,1020,-1,1021,1022,1023,-1,1024,1025,1026,-1,1027,1028,1029,-1,1030,1031,1032,-1,1033,1034,1035,-1,1036,1037,1038,-1,1039,1040,1041,-1,1042,1043,1044,-1,1045,1046,1047,-1,1048,1049,1050,-1,1051,1052,1053,-1,1054,1055,1056,-1,1057,1058,1059,-1,1060,1061,1062,-1,1063,1064,1065,-1,1066,1067,1068,-1,1069,1070,1071,-1,1072,1073,1074,-1,1075,1076,1077,-1,1078,1079,1080,-1,1081,1082,1083,-1,1084,1085,1086,-1,1087,1088,1089,-1,1090,1091,1092,-1,1093,1094,1095,-1,1096,1097,1098,-1,1099,1100,1101,-1,1102,1103,1104,-1,1105,1106,1107,-1,1108,1109,1110,-1,1111,1112,1113,-1,1114,1115,1116,-1,1117,1118,1119,-1,1120,1121,1122,-1,1123,1124,1125,-1,1126,1127,1128,-1,1129,1130,1131,-1,1132,1133,1134,-1,1135,1136,1137,-1,1138,1139,1140,-1,1141,1142,1143,-1,1144,1145,1146,-1,1147,1148,1149,-1,1150,1151,1152,-1,1153,1154,1155,-1,1156,1157,1158,-1,1159,1160,1161,-1,1162,1163,1164,-1,1165,1166,1167,-1,1168,1169,1170,-1,1171,1172,1173,-1,1174,1175,1176,-1,1177,1178,1179,-1,1180,1181,1182,-1,1183,1184,1185,-1,1186,1187,1188,-1,1189,1190,1191,-1,1192,1193,1194,-1,1195,1196,1197,-1,1198,1199,1200,-1,1201,1202,1203,-1,1204,1205,1206,-1,1207,1208,1209,-1,1210,1211,1212,-1,1213,1214,1215,-1,1216,1217,1218,-1,1219,1220,1221,-1,1222,1223,1224,-1,1225,1226,1227,-1,1228,1229,1230,-1,1231,1232,1233,-1,1234,1235,1236,-1,1237,1238,1239,-1,1240,1241,1242,-1,1243,1244,1245,-1,1246,1247,1248,-1,1249,1250,1251,-1,1252,1253,1254,-1,1255,1256,1257,-1,1258,1259,1260,-1,1261,1262,1263,-1,1264,1265,1266,-1,1267,1268,1269,-1,1270,1271,1272,-1,1273,1274,1275,-1,1276,1277,1278,-1,1279,1280,1281,-1,1282,1283,1284,-1,1285,1286,1287,-1,1288,1289,1290,-1,1291,1292,1293,-1,1294,1295,1296,-1,1297,1298,1299,-1,1300,1301,1302,-1,1303,1304,1305,-1,1306,1307,1308,-1,1309,1310,1311,-1,1312,1313,1314,-1,1315,1316,1317,-1,1318,1319,1320,-1,1321,1322,1323,-1,1324,1325,1326,-1,1327,1328,1329,-1,1330,1331,1332,-1,1333,1334,1335,-1,1336,1337,1338,-1,1339,1340,1341,-1,1342,1343,1344,-1,1345,1346,1347,-1,1348,1349,1350,-1,1351,1352,1353,-1,1354,1355,1356,-1,1357,1358,1359,-1,1360,1361,1362,-1,1363,1364,1365,-1,1366,1367,1368,-1,1369,1370,1371,-1,1372,1373,1374,-1,1375,1376,1377,-1,1378,1379,1380,-1,1381,1382,1383,-1,1384,1385,1386,-1,1387,1388,1389,-1,1390,1391,1392,-1,1393,1394,1395,-1,1396,1397,1398,-1,1399,1400,1401,-1,1402,1403,1404,-1,1405,1406,1407,-1,1408,1409,1410,-1,1411,1412,1413,-1,1414,1415,1416,-1,1417,1418,1419,-1,1420,1421,1422,-1,1423,1424,1425,-1,1426,1427,1428,-1,1429,1430,1431,-1,1432,1433,1434,-1,1435,1436,1437,-1,1438,1439,1440,-1,1441,1442,1443,-1,1444,1445,1446,-1,1447,1448,1449,-1,1450,1451,1452,-1,1453,1454,1455,-1,1456,1457,1458,-1,1459,1460,1461,-1,1462,1463,1464,-1,1465,1466,1467,-1,1468,1469,1470,-1,1471,1472,1473,-1,1474,1475,1476,-1,1477,1478,1479,-1,1480,1481,1482,-1,1483,1484,1485,-1,1486,1487,1488,-1,1489,1490,1491,-1,1492,1493,1494,-1,1495,1496,1497,-1,1498,1499,1500,-1,1501,1502,1503,-1,1504,1505,1506,-1,1507,1508,1509,-1,1510,1511,1512,-1,1513,1514,1515,-1,1516,1517,1518,-1,1519,1520,1521,-1,1522,1523,1524,-1,1525,1526,1527,-1,1528,1529,1530,-1,1531,1532,1533,-1,1534,1535,1536,-1,1537,1538,1539,-1,1540,1541,1542,-1,1543,1544,1545,-1,1546,1547,1548,-1,1549,1550,1551,-1,1552,1553,1554,-1,1555,1556,1557,-1,1558,1559,1560,-1,1561,1562,1563,-1,1564,1565,1566,-1,1567,1568,1569,-1,1570,1571,1572,-1,1573,1574,1575,-1,1576,1577,1578,-1,1579,1580,1581,-1,1582,1583,1584,-1,1585,1586,1587,-1,1588,1589,1590,-1,1591,1592,1593,-1,1594,1595,1596,-1,1597,1598,1599,-1,1600,1601,1602,-1,1603,1604,1605,-1,1606,1607,1608,-1,1609,1610,1611,-1,1612,1613,1614,-1,1615,1616,1617,-1,1618,1619,1620,-1,1621,1622,1623,-1,1624,1625,1626,-1,1627,1628,1629,-1,1630,1631,1632,-1,1633,1634,1635,-1,1636,1637,1638,-1,1639,1640,1641,-1,1642,1643,1644,-1,1645,1646,1647,-1,1648,1649,1650,-1,1651,1652,1653,-1,1654,1655,1656,-1,1657,1658,1659,-1,1660,1661,1662,-1,1663,1664,1665,-1,1666,1667,1668,-1,1669,1670,1671,-1,1672,1673,1674,-1,1675,1676,1677,-1,1678,1679,1680,-1,1681,1682,1683,-1,1684,1685,1686,-1,1687,1688,1689,-1,1690,1691,1692,-1,1693,1694,1695,-1,1696,1697,1698,-1,1699,1700,1701,-1,1702,1703,1704,-1,1705,1706,1707,-1,1708,1709,1710,-1,1711,1712,1713,-1,1714,1715,1716,-1,1717,1718,1719,-1,1720,1721,1722,-1,1723,1724,1725,-1,1726,1727,1728,-1,1729,1730,1731,-1,1732,1733,1734,-1,1735,1736,1737,-1,1738,1739,1740,-1,1741,1742,1743,-1,1744,1745,1746,-1,1747,1748,1749,-1,1750,1751,1752,-1,1753,1754,1755,-1,1756,1757,1758,-1,1759,1760,1761,-1,1762,1763,1764,-1,1765,1766,1767,-1,1768,1769,1770,-1,1771,1772,1773,-1,1774,1775,1776,-1,1777,1778,1779,-1,1780,1781,1782,-1,1783,1784,1785,-1,1786,1787,1788,-1,1789,1790,1791,-1,1792,1793,1794,-1,1795,1796,1797,-1,1798,1799,1800,-1,1801,1802,1803,-1,1804,1805,1806,-1,1807,1808,1809,-1,1810,1811,1812,-1,1813,1814,1815,-1,1816,1817,1818,-1,1819,1820,1821,-1,1822,1823,1824,-1,1825,1826,1827,-1,1828,1829,1830,-1,1831,1832,1833,-1,1834,1835,1836,-1,1837,1838,1839,-1,1840,1841,1842,-1,1843,1844,1845,-1,1846,1847,1848,-1,1849,1850,1851,-1,1852,1853,1854,-1,1855,1856,1857,-1,1858,1859,1860,-1,1861,1862,1863,-1,1864,1865,1866,-1,1867,1868,1869,-1,1870,1871,1872,-1,1873,1874,1875,-1,1876,1877,1878,-1,1879,1880,1881,-1,1882,1883,1884,-1,1885,1886,1887,-1,1888,1889,1890,-1,1891,1892,1893,-1,1894,1895,1896,-1,1897,1898,1899,-1,1900,1901,1902,-1,1903,1904,1905,-1,1906,1907,1908,-1,1909,1910,1911,-1,1912,1913,1914,-1,1915,1916,1917,-1,1918,1919,1920,-1,1921,1922,1923,-1,1924,1925,1926,-1,1927,1928,1929,-1,1930,1931,1932,-1,1933,1934,1935,-1,1936,1937,1938,-1,1939,1940,1941,-1,1942,1943,1944,-1,1945,1946,1947,-1,1948,1949,1950,-1,1951,1952,1953,-1,1954,1955,1956,-1,1957,1958,1959,-1,1960,1961,1962,-1,1963,1964,1965,-1,1966,1967,1968,-1,1969,1970,1971,-1,1972,1973,1974,-1,1975,1976,1977,-1,1978,1979,1980,-1,1981,1982,1983,-1,1984,1985,1986,-1,1987,1988,1989,-1,1990,1991,1992,-1,1993,1994,1995,-1,1996,1997,1998,-1,1999,2000,2001,-1,2002,2003,2004,-1,2005,2006,2007,-1,2008,2009,2010,-1,2011,2012,2013,-1,2014,2015,2016,-1,2017,2018,2019,-1,2020,2021,2022,-1,2023,2024,2025,-1,2026,2027,2028,-1,2029,2030,2031,-1,2032,2033,2034,-1,2035,2036,2037,-1,2038,2039,2040,-1,2041,2042,2043,-1,2044,2045,2046,-1,2047,2048,2049,-1,2050,2051,2052,-1,2053,2054,2055,-1,2056,2057,2058,-1,2059,2060,2061,-1,2062,2063,2064,-1,2065,2066,2067,-1,2068,2069,2070,-1,2071,2072,2073,-1,2074,2075,2076,-1,2077,2078,2079,-1,2080,2081,2082,-1,2083,2084,2085,-1,2086,2087,2088,-1,2089,2090,2091,-1,2092,2093,2094,-1,2095,2096,2097,-1,2098,2099,2100,-1,2101,2102,2103,-1,2104,2105,2106,-1,2107,2108,2109,-1,2110,2111,2112,-1,2113,2114,2115,-1,2116,2117,2118,-1,2119,2120,2121,-1,2122,2123,2124,-1,2125,2126,2127,-1,2128,2129,2130,-1,2131,2132,2133,-1,2134,2135,2136,-1,2137,2138,2139,-1,2140,2141,2142,-1,2143,2144,2145,-1,2146,2147,2148,-1,2149,2150,2151,-1,2152,2153,2154,-1,2155,2156,2157,-1,2158,2159,2160,-1,2161,2162,2163,-1,2164,2165,2166,-1,2167,2168,2169,-1,2170,2171,2172,-1,2173,2174,2175,-1,2176,2177,2178,-1,2179,2180,2181,-1,2182,2183,2184,-1,2185,2186,2187,-1,2188,2189,2190,-1,2191,2192,2193,-1,2194,2195,2196,-1,2197,2198,2199,-1,2200,2201,2202,-1,2203,2204,2205,-1,2206,2207,2208,-1,2209,2210,2211,-1,2212,2213,2214,-1,2215,2216,2217,-1,2218,2219,2220,-1,2221,2222,2223,-1,2224,2225,2226,-1,2227,2228,2229,-1,2230,2231,2232,-1,2233,2234,2235,-1,2236,2237,2238,-1,2239,2240,2241,-1,2242,2243,2244,-1,2245,2246,2247,-1,2248,2249,2250,-1,2251,2252,2253,-1,2254,2255,2256,-1,2257,2258,2259,-1,2260,2261,2262,-1,2263,2264,2265,-1,2266,2267,2268,-1,2269,2270,2271,-1,2272,2273,2274,-1,2275,2276,2277,-1,2278,2279,2280,-1,2281,2282,2283,-1,2284,2285,2286,-1,2287,2288,2289,-1,2290,2291,2292,-1,2293,2294,2295,-1,2296,2297,2298,-1,2299,2300,2301,-1,2302,2303,2304,-1,2305,2306,2307,-1,2308,2309,2310,-1,2311,2312,2313,-1,2314,2315,2316,-1,2317,2318,2319,-1,2320,2321,2322,-1,2323,2324,2325,-1,2326,2327,2328,-1,2329,2330,2331,-1,2332,2333,2334,-1,2335,2336,2337,-1,2338,2339,2340,-1,2341,2342,2343,-1,2344,2345,2346,-1,2347,2348,2349,-1,2350,2351,2352,-1,2353,2354,2355,-1,2356,2357,2358,-1,2359,2360,2361,-1,2362,2363,2364,-1,2365,2366,2367,-1,2368,2369,2370,-1,2371,2372,2373,-1,2374,2375,2376,-1,2377,2378,2379,-1,2380,2381,2382,-1,2383,2384,2385,-1,2386,2387,2388,-1,2389,2390,2391,-1,2392,2393,2394,-1,2395,2396,2397,-1,2398,2399,2400,-1,2401,2402,2403,-1,2404,2405,2406,-1,2407,2408,2409,-1,2410,2411,2412,-1,2413,2414,2415,-1,2416,2417,2418,-1,2419,2420,2421,-1,2422,2423,2424,-1,2425,2426,2427,-1,2428,2429,2430,-1,2431,2432,2433,-1,2434,2435,2436,-1,2437,2438,2439,-1,2440,2441,2442,-1,2443,2444,2445,-1,2446,2447,2448,-1,2449,2450,2451,-1,2452,2453,2454,-1,2455,2456,2457,-1,2458,2459,2460,-1,2461,2462,2463,-1,2464,2465,2466,-1,2467,2468,2469,-1,2470,2471,2472,-1,2473,2474,2475,-1,2476,2477,2478,-1,2479,2480,2481,-1,2482,2483,2484,-1,2485,2486,2487,-1,2488,2489,2490,-1,2491,2492,2493,-1,2494,2495,2496,-1,2497,2498,2499,-1,2500,2501,2502,-1,2503,2504,2505,-1,2506,2507,2508,-1,2509,2510,2511,-1,2512,2513,2514,-1,2515,2516,2517,-1,2518,2519,2520,-1,2521,2522,2523,-1,2524,2525,2526,-1,2527,2528,2529,-1,2530,2531,2532,-1,2533,2534,2535,-1,2536,2537,2538,-1,2539,2540,2541,-1,2542,2543,2544,-1,2545,2546,2551,-1,2550,2551,2549,-1,2551,2546,2549,-1,2549,2546,2548,-1,2547,2548,2546,-1,2555,2552,2554,-1,2553,2554,2552,-1,2567,2568,2566,-1,2568,2556,2566,-1,2566,2556,2565,-1,2558,2559,2557,-1,2560,2561,2559,-1,2559,2561,2557,-1,2561,2562,2557,-1,2562,2563,2557,-1,2563,2564,2557,-1,2565,2556,2564,-1,2557,2564,2556,-1,2570,2571,2569,-1,2571,2572,2569,-1,2572,2573,2569,-1,2573,2574,2569,-1,2574,2575,2569,-1,2575,2576,2569,-1,2576,2577,2569,-1,2577,2578,2569,-1,2578,2579,2569,-1,2579,2580,2569,-1,2580,2581,2569,-1,2581,2582,2569,-1,2582,2583,2569,-1,2583,2584,2569,-1,2584,2585,2569,-1,2585,2586,2569,-1,2586,2587,2569,-1,2587,2588,2569,-1,2612,2613,2614,-1,2615,2616,2617,-1,2618,2619,2620,-1,2633,2634,2632,-1,2634,2635,2632,-1,2636,2637,2635,-1,2638,2639,2637,-1,2639,2640,2637,-1,2642,2643,2641,-1,2623,2624,2622,-1,2628,2629,2627,-1,2630,2631,2629,-1,2631,2632,2629,-1,2629,2632,2627,-1,2632,2635,2627,-1,2627,2635,2626,-1,2635,2637,2626,-1,2637,2640,2626,-1,2643,2621,2641,-1,2626,2640,2625,-1,2640,2641,2625,-1,2641,2621,2625,-1,2624,2625,2622,-1,2622,2625,2621,-1,2656,2657,2658,-1,2659,2660,2661,-1,2662,2663,2664,-1,2665,2666,2667,-1,2668,2669,2670,-1,2671,2672,2673,-1,2674,2675,2676,-1,2677,2678,2679,-1,2682,2683,2681,-1,2685,2686,2684,-1,2686,2687,2684,-1,2687,2688,2684,-1,2689,2690,2688,-1,2694,2695,2693,-1,2695,2696,2693,-1,2696,2697,2693,-1,2701,2702,2700,-1,2680,2681,2702,-1,2684,2688,2683,-1,2688,2690,2683,-1,2683,2690,2681,-1,2690,2691,2681,-1,2691,2692,2681,-1,2692,2693,2681,-1,2697,2698,2693,-1,2681,2693,2702,-1,2698,2699,2693,-1,2702,2693,2700,-1,2699,2700,2693,-1,2860,2861,2862,-1,2872,2873,2871,-1,2871,2873,2870,-1,2870,2873,2869,-1,2875,2876,2874,-1,2878,2879,2877,-1,2880,2881,2879,-1,2882,2883,2881,-1,2885,2863,2884,-1,2864,2865,2863,-1,2866,2867,2865,-1,2868,2869,2867,-1,2869,2873,2867,-1,2876,2877,2874,-1,2879,2881,2877,-1,2881,2883,2877,-1,2883,2884,2877,-1,2865,2867,2863,-1,2867,2873,2863,-1,2873,2874,2863,-1,2863,2874,2884,-1,2877,2884,2874,-1,2926,2677,2927,-1,2679,2858,2677,-1,2858,2857,2677,-1,2677,2857,2927,-1,2857,2852,2927,-1,2852,2851,2927,-1,2851,2850,2927,-1,2848,2861,2849,-1,2848,2847,2860,-1,2846,2789,2847,-1,2789,2788,2847,-1,2849,2861,2850,-1,2860,2847,2861,-1,2788,2927,2847,-1,2850,2861,2927,-1,2847,2927,2861,-1,3021,3022,3023,-1,3024,3025,3026,-1,3027,3028,3029,-1,3030,3031,3032,-1,3033,3034,3035,-1,3036,3037,3038,-1,3039,3040,3041,-1,3042,3043,3044,-1,3045,3046,3047,-1,3048,3049,3050,-1,3051,3052,3053,-1,3054,3055,3056,-1,3057,3058,3059,-1,3060,3061,3062,-1,3063,3064,3065,-1,3066,3067,3068,-1,3069,3070,3071,-1,3072,3073,3074,-1,3025,3024,3023,-1,2,2859,3040,-1,2858,2679,2859,-1,3023,3024,3021,-1,3021,3024,3022,-1,3022,3024,3023,-1,3023,3024,2679,-1,2679,3024,2859,-1,3040,2859,3037,-1,3037,2859,3038,-1,3035,3038,3033,-1,3038,2859,3033,-1,3033,2859,3031,-1,3031,2859,3032,-1,2859,3024,3032,-1,3024,3028,3032,-1,3027,3032,3028,-1,3075,3076,3077,-1,3078,3079,3080,-1,3081,3082,3083,-1,3084,3085,3086,-1,3087,3088,3089,-1,3090,3091,3092,-1,2614,2616,2612,-1,2618,2654,2619,-1,2657,2656,2653,-1,2653,2652,2656,-1,2651,2650,2652,-1,2649,2661,2650,-1,2612,2616,2569,-1,2619,2654,2615,-1,2653,2656,2654,-1,2652,2650,2656,-1,2661,1,2650,-1,1,2570,2650,-1,2569,2616,2570,-1,2654,2656,2615,-1,2656,2650,2615,-1,2570,2616,2650,-1,2615,2650,2616,-1,2675,2671,2611,-1,2672,2670,2671,-1,2611,2671,2569,-1,2671,2670,2569,-1,2569,2670,2614,-1,2670,3091,2614,-1,2614,3091,2616,-1,3091,3087,2616,-1,3093,3094,3095,-1,3096,3097,3098,-1,3099,3100,3101,-1,3102,3103,3104,-1,3105,3106,3107,-1,3108,3109,3110,-1,3111,3112,3113,-1,3114,3115,3116,-1,3117,3118,3119,-1,3120,3121,3122,-1,3123,3124,3125,-1,3126,3127,3128,-1,3129,3130,3131,-1,3132,3133,3134,-1,3135,3136,3137,-1,3138,3139,3140,-1,3141,3142,3143,-1,3144,3145,3146,-1,3147,3148,3149,-1,3150,3151,3152,-1,3153,3154,3155,-1,3156,3157,3158,-1,3159,3160,3161,-1,3162,3163,3164,-1,3165,3166,3167,-1,3168,3169,3170,-1,3171,3172,3173,-1,3174,3175,3176,-1,3177,3178,3179,-1,3180,3181,3182,-1,3183,3184,3185,-1,3186,3187,3188,-1,3189,3190,3191,-1,3192,3193,3194,-1,3195,3196,3197,-1,3198,3199,3200,-1,3201,3202,3203,-1,3204,3205,3206,-1,3207,3208,3209,-1,3210,3211,3212,-1,3213,3214,3215,-1,3216,3217,3218,-1,3219,3220,3221,-1,3222,3223,3224,-1,3225,3226,3227,-1,3228,3229,3230,-1,3231,3232,3233,-1,3234,3235,3236,-1,3237,3238,3239,-1,3240,3241,3242,-1,3243,3244,3245,-1,3246,3247,3248,-1,3249,3250,3251,-1,3252,3253,3254,-1,3255,3256,3257,-1,3258,3259,3260,-1,3261,3262,3263,-1,3264,3265,3266,-1,3267,3268,3269,-1,3270,3271,3272,-1,3273,3274,3275,-1,3276,3277,3278,-1,3279,3280,3281,-1,3282,3283,3284,-1,3285,3286,3287,-1,3288,3289,3290,-1,3291,3292,3293,-1,3294,3295,3296,-1,3297,3298,3299,-1,3300,3301,3302,-1,3303,3304,3305,-1,3306,3307,3308,-1,3309,3310,3311,-1,3312,3313,3314,-1,3315,3316,3317,-1,3318,3319,3320,-1,3321,3322,3323,-1,3324,3325,3326,-1,3327,3328,3329,-1,3330,3331,3332,-1,3333,3334,3335,-1,3336,3337,3338,-1,3339,3340,3341,-1,3342,3343,3344,-1,3345,3346,3347,-1,3348,3349,3350,-1,3351,3352,3353,-1,3354,3355,3356,-1,3357,3358,3359,-1,3360,3361,3362,-1,3363,3364,3365,-1,3366,3367,3368,-1,3369,3370,3371,-1,3372,3373,3374,-1,3375,3376,3377,-1,3378,3379,3380,-1,3381,3382,3383,-1,3384,3385,3386,-1,3387,3388,3389,-1,3390,3391,3392,-1,3393,3394,3395,-1,3396,3397,3398,-1,3399,3400,3401,-1,3402,3403,3404,-1,3405,3406,3407,-1,3408,3409,3410,-1,3411,3412,3413,-1,3414,3415,3416,-1,3417,3418,3419,-1,3420,3421,3422,-1,3423,3424,3425,-1,3426,3427,3428,-1,3429,3430,3431,-1,3432,3433,3434,-1,3435,3436,3437,-1,3438,3439,3440,-1,3441,3442,3443,-1,3444,3445,3446,-1,3447,3448,3449,-1,3450,3451,3452,-1,3453,3454,3455,-1,3456,3457,3458,-1,3459,3460,3461,-1,3462,3463,3464,-1,3465,3466,3467,-1,3468,3469,3470,-1,3471,3472,3473,-1,3474,3475,3476,-1,3477,3478,3479,-1,3480,3481,3482,-1,3483,3484,3485,-1,3486,3487,3488,-1,3489,3490,3491,-1,3492,3493,3494,-1,3495,3496,3497,-1,3498,3499,3500,-1,3501,3502,3503,-1,3504,3505,3506,-1,3507,3508,3509,-1,3510,3511,3512,-1,3513,3514,3515,-1,3516,3517,3518,-1,3519,3520,3521,-1,3522,3523,3524,-1,3525,3526,3527,-1,3528,3529,3530,-1,3531,3532,3533,-1,3534,3535,3536,-1,3537,3538,3539,-1,3540,3541,3542,-1,3543,3544,3545,-1,3546,3547,3548,-1,3549,3550,3551,-1,3552,3553,3554,-1,3555,3556,3557,-1,3558,3559,3560,-1,3561,3562,3563,-1,3564,3565,3566,-1,3567,3568,3569,-1,3570,3571,3572,-1,3573,3574,3575,-1,3576,3577,3578,-1,3579,3580,3581,-1,3582,3583,3584,-1,3585,3586,3587,-1,3588,3589,3590,-1,3591,3592,3593,-1,3594,3595,3596,-1,3597,3598,3599,-1,3600,3601,3602,-1,3603,3604,3605,-1,3606,3607,3608,-1,3609,3610,3611,-1,3612,3613,3614,-1,3615,3616,3617,-1,3618,3619,3620,-1,3621,3622,3623,-1,3624,3625,3626,-1,3627,3628,3629,-1,3630,3631,3632,-1,3633,3634,3635,-1,3636,3637,3638,-1,3639,3640,3641,-1,3642,3643,3644,-1,3645,3646,3647,-1,3648,3649,3650,-1,3651,3652,3653,-1,3654,3655,3656,-1,3657,3658,3659,-1,3660,3661,3662,-1,3663,3664,3665,-1,3666,3667,3668,-1,3669,3670,3671,-1,3672,3673,3674,-1,3675,3676,3677,-1,3678,3679,3680,-1,3681,3682,3683,-1,3684,3685,3686,-1,3687,3688,3689,-1,3690,3691,3692,-1,3693,3694,3695,-1,3696,3697,3698,-1,3699,3700,3701,-1,3702,3703,3704,-1,3705,3706,3707,-1,3708,3709,3710,-1,3711,3712,3713,-1,3714,3715,3716,-1,3717,3718,3719,-1,3720,3721,3722,-1,3723,3724,3725,-1,3726,3727,3728,-1,3729,3730,3731,-1,3732,3733,3734,-1,3735,3736,3737,-1,3738,3739,3740,-1,3741,3742,3743,-1,3744,3745,3746,-1,3747,3748,3749,-1,3750,3751,3752,-1,3753,3754,3755,-1,3756,3757,3758,-1,3759,3760,3761,-1,3762,3763,3764,-1,3765,3766,3767,-1,3768,3769,3770,-1,3771,3772,3773,-1,3774,3775,3776,-1,3777,3778,3779,-1,3780,3781,3782,-1,3783,3784,3785,-1,3786,3787,3788,-1,3789,3790,3791,-1,3792,3793,3794,-1,3795,3796,3797,-1,3798,3799,3800,-1,3801,3802,3803,-1,3804,3805,3806,-1,3807,3808,3809,-1,3810,3811,3812,-1,3813,3814,3815,-1,3816,3817,3818,-1,3819,3820,3821,-1,3822,3823,3824,-1,3825,3826,3827,-1,3828,3829,3830,-1,3831,3832,3833,-1,3834,3835,3836,-1,3837,3838,3839,-1,3840,3841,3842,-1,3843,3844,3845,-1,3846,3847,3848,-1,3849,3850,3851,-1,3852,3853,3854,-1,3855,3856,3857,-1,3858,3859,3860,-1,3861,3862,3863,-1,3864,3865,3866,-1,3867,3868,3869,-1,3870,3871,3872,-1,3873,3874,3875,-1,3876,3877,3878,-1,3879,3880,3881,-1,3882,3883,3884,-1,3885,3886,3887,-1,3888,3889,3890,-1,3891,3892,3893,-1,3894,3895,3896,-1,3897,3898,3899,-1,3900,3901,3902,-1,3903,3904,3905,-1,3906,3907,3908,-1,3909,3910,3911,-1,3912,3913,3914,-1,3915,3916,3917,-1,3918,3919,3920,-1,3921,3922,3923,-1,3924,3925,3926,-1,3927,3928,3929,-1,3930,3931,3932,-1,3933,3934,3935,-1,3936,3937,3938,-1,3939,3940,3941,-1,3942,3943,3944,-1,3945,3946,3947,-1,3948,3949,3950,-1,3951,3952,3953,-1,3954,3955,3956,-1,3957,3958,3959,-1,3960,3961,3962,-1,3963,3964,3965,-1,3966,3967,3968,-1,3969,3970,3971,-1,3972,3973,3974,-1,3975,3976,3977,-1,3978,3979,3980,-1,3981,3982,3983,-1,3984,3985,3986,-1,3987,3988,3989,-1,3990,3991,3992,-1,3993,3994,3995,-1,3996,3997,3998,-1,3999,4000,4001,-1,4002,4003,4004,-1,4005,4006,4007,-1,4008,4009,4010,-1,4011,4012,4013,-1,4014,4015,4016,-1,4017,4018,4019,-1,4020,4021,4022,-1,4023,4024,4025,-1,4026,4027,4028,-1,4029,4030,4031,-1,4032,4033,4034,-1,4035,4036,4037,-1,4038,4039,4040,-1,4041,4042,4043,-1,4044,4045,4046,-1,4047,4048,4049,-1,4050,4051,4052,-1,4053,4054,4055,-1,4056,4057,4058,-1,4059,4060,4061,-1,4062,4063,4064,-1,4065,4066,4067,-1,4068,4069,4070,-1,4071,4072,4073,-1,4074,4075,4076,-1,4077,4078,4079,-1,4080,4081,4082,-1,4083,4084,4085,-1,4086,4087,4088,-1,4089,4090,4091,-1,4092,4093,4094,-1,4095,4096,4097,-1,4098,4099,4100,-1,4101,4102,4103,-1,4104,4105,4106,-1,4107,4108,4109,-1,4110,4111,4112,-1,4113,4114,4115,-1,4116,4117,4118,-1,4119,4120,4121,-1,4122,4123,4124,-1,4125,4126,4127,-1,4128,4129,4130,-1,4131,4132,4133,-1,4134,4135,4136,-1,4137,4138,4139,-1,4140,4141,4142,-1,4143,4144,4145,-1,4146,4147,4148,-1,4149,4150,4151,-1,4152,4153,4154,-1,4155,4156,4157,-1,4158,4159,4160,-1,4161,4162,4163,-1,4164,4165,4166,-1,4167,4168,4169,-1,4170,4171,4172,-1,4173,4174,4175,-1,4176,4177,4178,-1,4179,4180,4181,-1,4182,4183,4184,-1,4185,4186,4187,-1,4188,4189,4190,-1,4191,4192,4193,-1,4194,4195,4196,-1,4197,4198,4199,-1,4200,4201,4202,-1,4203,4204,4205,-1,4206,4207,4208,-1,4209,4210,4211,-1,4212,4213,4214,-1,4215,4216,4217,-1,4218,4219,4220,-1,4221,4222,4223,-1,4224,4225,4226,-1,4227,4228,4229,-1,4230,4231,4232,-1,4233,4234,4235,-1,4236,4237,4238,-1,4239,4240,4241,-1,4242,4243,4244,-1,4245,4246,4247,-1,4248,4249,4250,-1,4251,4252,4253,-1,4254,4255,4256,-1,4257,4258,4259,-1,4260,4261,4262,-1,4263,4264,4265,-1,4266,4267,4268,-1,4269,4270,4271,-1,4272,4273,4274,-1,4275,4276,4277,-1,4278,4279,4280,-1,4281,4282,4283,-1,4284,4285,4286,-1,4287,4288,4289,-1,4290,4291,4292,-1,4293,4294,4295,-1,4296,4297,4298,-1,4299,4300,4301,-1,4302,4303,4304,-1,4305,4306,4307,-1,4308,4309,4310,-1,4311,4312,4313,-1,4314,4315,4316,-1,4317,4318,4319,-1,4320,4321,4322,-1,4323,4324,4325,-1,4326,4327,4328,-1,4329,4330,4331,-1,4332,4333,4334,-1,4335,4336,4337,-1,4338,4339,4340,-1,4341,4342,4343,-1,4344,4345,4346,-1,4347,4348,4349,-1,4350,4351,4352,-1,4353,4354,4355,-1,4356,4357,4358,-1,4359,4360,4361,-1,4362,4363,4364,-1,4365,4366,4367,-1,4368,4369,4370,-1,4371,4372,4373,-1,4374,4375,4376,-1,4377,4378,4379,-1,4380,4381,4382,-1,4383,4384,4385,-1,4386,4387,4388,-1,4389,4390,4391,-1,4392,4393,4394,-1,4395,4396,4397,-1,4398,4399,4400,-1,4401,4402,4403,-1,4404,4405,4406,-1,4407,4408,4409,-1,4410,4411,4412,-1,4413,4414,4415,-1,4416,4417,4418,-1,4419,4420,4421,-1,4422,4423,4424,-1,4425,4426,4427,-1,4428,4429,4430,-1,4431,4432,4433,-1,4434,4435,4436,-1,4437,4438,4439,-1,4440,4441,4442,-1,4443,4444,4445,-1,4446,4447,4448,-1,4449,4450,4451,-1,4452,4453,4454,-1,4455,4456,4457,-1,4458,4459,4460,-1,4461,4462,4463,-1,4464,4465,4466,-1,4467,4468,4469,-1,4470,4471,4472,-1,4473,4474,4475,-1,4476,4477,4478,-1,4479,4480,4481,-1,4482,4483,4484,-1,4485,4486,4487,-1,4488,4489,4490,-1,4491,4492,4493,-1,4494,4495,4496,-1,4497,4498,4499,-1,4500,4501,4502,-1,4503,4504,4505,-1,4506,4507,4508,-1,4509,4510,4511,-1,4512,4513,4514,-1,4515,4516,4517,-1,4518,4519,4520,-1,4521,4522,4523,-1,4524,4525,4526,-1,4527,4528,4529,-1,4530,4531,4532,-1,4533,4534,4535,-1,4536,4537,4538,-1,4539,4540,4541,-1,4542,4543,4544,-1,4545,4546,4547,-1,4548,4549,4550,-1,4551,4552,4553,-1,4554,4555,4556,-1,4557,4558,4559,-1,4560,4561,4562,-1,4563,4564,4565,-1,4566,4567,4568,-1,4569,4570,4571,-1,4572,4573,4574,-1,4575,4576,4577,-1,4578,4579,4580,-1,4581,4582,4583,-1,4584,4585,4586,-1,4587,4588,4589,-1,4590,4591,4592,-1,4593,4594,4595,-1,4596,4597,4598,-1,4599,4600,4601,-1,4602,4603,4604,-1,4605,4606,4607,-1,4608,4609,4610,-1,4611,4612,4613,-1,4614,4615,4616,-1,4617,4618,4619,-1,4620,4621,4622,-1,4623,4624,4625,-1,4626,4627,4628,-1,4629,4630,4631,-1,4632,4633,4634,-1,4635,4636,4637,-1,4638,4639,4640,-1,4641,4642,4643,-1,4644,4645,4646,-1,4647,4648,4649,-1,4650,4651,4652,-1,4653,4654,4655,-1,4656,4657,4658,-1,4659,4660,4661,-1,4662,4663,4664,-1,4665,4666,4667,-1,4668,4669,4670,-1,4671,4672,4673,-1,4674,4675,4676,-1,4677,4678,4679,-1,4680,4681,4682,-1,4683,4684,4685,-1,4686,4687,4688,-1,4689,4690,4691,-1,4692,4693,4694,-1,4695,4696,4697,-1,4698,4699,4700,-1,4701,4702,4703,-1,4704,4705,4706,-1,4707,4708,4709,-1,4710,4711,4712,-1,4713,4714,4715,-1,4716,4717,4718,-1,4719,4720,4721,-1,4722,4723,4724,-1,4725,4726,4727,-1,4728,4729,4730,-1,4731,4732,4733,-1,4734,4735,4736,-1,4737,4738,4739,-1,4740,4741,4742,-1,4743,4744,4745,-1,4746,4747,4748,-1,4749,4750,4751,-1,4752,4753,4754,-1,4755,4756,4757,-1,4758,4759,4760,-1,4761,4762,4763,-1,4764,4765,4766,-1,4767,4768,4769,-1,4770,4771,4772,-1,4773,4774,4775,-1,4776,4777,4778,-1,4779,4780,4781,-1,4782,4783,4784,-1,4785,4786,4787,-1,4788,4789,4790,-1,4791,4792,4793,-1,4794,4795,4796,-1,4797,4798,4799,-1,4800,4801,4802,-1,4803,4804,4805,-1,4806,4807,4808,-1,4809,4810,4811,-1,4812,4813,4814,-1,4815,4816,4817,-1,4818,4819,4820,-1,4821,4822,4823,-1,4824,4825,4826,-1,4827,4828,4829,-1,4830,4831,4832,-1,4833,4834,4835,-1,4836,4837,4838,-1,4839,4840,4841,-1,4842,4843,4844,-1,4845,4846,4847,-1,4848,4849,4850,-1,4851,4852,4853,-1,4854,4855,4856,-1,4857,4858,4859,-1,4860,4861,4862,-1,4863,4864,4865,-1,4866,4867,4868,-1,4869,4870,4871,-1,4872,4873,4874,-1,4875,4876,4877,-1,4878,4879,4880,-1,4881,4882,4883,-1,4884,4885,4886,-1]
IndexedFaceSet406.creaseAngle = 1.59
Coordinate407 = x3d.Coordinate()

IndexedFaceSet406.coord = Coordinate407

Shape402.geometry = IndexedFaceSet406

Transform401.children.append(Shape402)

fieldValue400.children.append(Transform401)

ProtoInstance398.fieldValue.append(fieldValue400)

fieldValue397.children.append(ProtoInstance398)
ProtoInstance408 = x3d.ProtoInstance()
ProtoInstance408.name = "Joint"
ProtoInstance408.DEF = "Allen_hanim_l_shoulder"
fieldValue409 = x3d.fieldValue()
fieldValue409.name = "name"
fieldValue409.value = "l_shoulder"

ProtoInstance408.fieldValue.append(fieldValue409)
fieldValue410 = x3d.fieldValue()
fieldValue410.name = "center"
fieldValue410.value = "0.167 1.36 -0.0518"

ProtoInstance408.fieldValue.append(fieldValue410)
fieldValue411 = x3d.fieldValue()
fieldValue411.name = "children"
ProtoInstance412 = x3d.ProtoInstance()
ProtoInstance412.name = "Segment"
ProtoInstance412.DEF = "Allen_hanim_l_upperarm"
fieldValue413 = x3d.fieldValue()
fieldValue413.name = "name"
fieldValue413.value = "l_upperarm"

ProtoInstance412.fieldValue.append(fieldValue413)
fieldValue414 = x3d.fieldValue()
fieldValue414.name = "children"
Transform415 = x3d.Transform()
Transform415.DEF = "Allen_l_upperarm_adjust"
Transform415.center = [-0.435,1,0.06]
Transform415.rotation = [0,1,0,1.570796]
Transform415.scale = [0.1,0.1,0.1]
Shape416 = x3d.Shape()
Appearance417 = x3d.Appearance()
Material418 = x3d.Material()
Material418.DEF = "Skin_Color"
Material418.ambientIntensity = 0.25
Material418.diffuseColor = [0.749,0.601,0.462]

Appearance417.material = Material418
ImageTexture419 = x3d.ImageTexture()
ImageTexture419.USE = "camo"

Appearance417.texture = ImageTexture419

Shape416.appearance = Appearance417
IndexedFaceSet420 = x3d.IndexedFaceSet()
IndexedFaceSet420.coordIndex = [0,1,2,-1,3,4,5,-1,6,7,8,-1,9,10,11,-1,12,13,14,-1,15,16,17,-1,18,19,20,-1,21,22,23,-1,24,25,26,-1,27,28,29,-1,30,31,32,-1,33,34,35,-1,36,37,38,-1,39,40,41,-1,42,43,44,-1,45,46,47,-1,48,49,50,-1,51,52,53,-1,54,55,56,-1,57,58,59,-1,60,61,62,-1,63,64,65,-1,66,67,68,-1,69,70,71,-1,72,73,74,-1,75,76,77,-1,78,79,80,-1,81,82,83,-1,84,85,86,-1,87,88,89,-1,90,91,92,-1,93,94,95,-1,96,97,98,-1,99,100,101,-1,102,103,104,-1,105,106,107,-1,108,109,110,-1,111,112,113,-1,114,115,116,-1,117,118,119,-1,120,121,122,-1,123,124,125,-1,126,127,128,-1,129,130,131,-1,132,133,134,-1,135,136,137,-1,138,139,140,-1,141,142,143,-1,144,145,146,-1,147,148,149,-1,150,151,152,-1,153,154,155,-1,156,157,158,-1,159,160,161,-1,162,163,164,-1,165,166,167,-1,168,169,170,-1,171,172,173,-1,174,175,176,-1,177,178,179,-1,180,181,182,-1,183,184,185,-1,186,187,188,-1,189,190,191,-1,192,193,194,-1,195,196,197,-1,198,199,200,-1,201,202,203,-1,204,205,206,-1,207,208,209,-1,210,211,212,-1,213,214,215,-1,216,217,218,-1,219,220,221,-1,222,223,224,-1,225,226,227,-1,228,229,230,-1,231,232,233,-1,234,235,236,-1,237,238,239,-1,240,241,242,-1,243,244,245,-1,246,247,248,-1,249,250,251,-1,252,253,254,-1,255,256,257,-1,258,259,260,-1,261,262,263,-1,264,265,266,-1,267,268,269,-1,270,271,272,-1,273,274,275,-1,276,277,278,-1,279,280,281,-1,282,283,284,-1,285,286,287,-1,288,289,290,-1,291,292,293,-1,294,295,296,-1,297,298,299,-1,300,301,302,-1,303,304,305,-1,306,307,308,-1,309,310,311,-1,312,313,314,-1,315,316,317,-1,318,319,320,-1,321,322,323,-1,324,325,326,-1,327,328,329,-1,330,331,332,-1,333,334,335,-1,336,337,338,-1,339,340,341,-1,342,343,344,-1,345,346,347,-1,348,349,350,-1,351,352,353,-1,354,355,356,-1,357,358,359,-1,360,361,362,-1,363,364,365,-1,366,367,368,-1,369,370,371,-1,372,373,374,-1,375,376,377,-1,378,379,380,-1,381,382,383,-1,384,385,386,-1,387,388,389,-1,390,391,392,-1,393,394,395,-1,396,397,398,-1,399,400,401,-1,402,403,404,-1,405,406,407,-1,408,409,410,-1,411,412,413,-1,414,415,416,-1,417,418,419,-1,420,421,422,-1,423,424,425,-1,426,427,428,-1,429,430,431,-1,432,433,434,-1,435,436,437,-1,438,439,440,-1,441,442,443,-1,444,445,446,-1,447,448,449,-1,450,451,452,-1,453,454,455,-1,456,457,458,-1,459,460,461,-1,462,463,464,-1,465,466,467,-1,468,469,470,-1,471,472,473,-1,474,475,476,-1,477,478,479,-1,480,481,482,-1,483,484,485,-1,486,487,488,-1,489,490,491,-1,492,493,494,-1,495,496,497,-1,498,499,500,-1,501,502,503,-1,504,505,506,-1,507,508,509,-1,510,511,512,-1,513,514,515,-1,516,517,518,-1,519,520,521,-1,522,523,524,-1,525,526,527,-1,528,529,530,-1,531,532,533,-1,534,535,536,-1,537,538,539,-1,540,541,542,-1,543,544,545,-1,546,547,548,-1,549,550,551,-1,552,553,554,-1,555,556,557,-1,558,559,560,-1,561,562,563,-1,564,565,566,-1,567,568,569,-1,570,571,572,-1,573,574,575,-1,576,577,578,-1,579,580,581,-1,582,583,584,-1,585,586,587,-1,588,589,590,-1,591,592,593,-1,594,595,596,-1,597,598,599,-1,600,601,602,-1,603,604,605,-1,606,607,608,-1,609,610,611,-1,612,613,614,-1,615,616,617,-1,618,619,620,-1,621,622,623,-1,624,625,626,-1,627,628,629,-1,630,631,632,-1,633,634,635,-1,636,637,638,-1,639,640,641,-1,642,643,644,-1,645,646,647,-1,648,649,650,-1,651,652,653,-1,654,655,656,-1,657,658,659,-1,660,661,662,-1,663,664,665,-1,666,667,668,-1,669,670,671,-1,672,673,674,-1,675,676,677,-1,678,679,680,-1,681,682,683,-1,684,685,686,-1,687,688,689,-1,690,691,692,-1,693,694,695,-1,696,697,698,-1,699,700,701,-1,702,703,704,-1,705,706,707,-1,708,709,710,-1,711,712,713,-1,714,715,716,-1,717,718,719,-1,720,721,722,-1,723,724,725,-1,726,727,728,-1,729,730,731,-1,732,733,734,-1,735,736,737,-1,738,739,740,-1,741,742,743,-1,744,745,746,-1,747,748,749,-1,750,751,752,-1,753,754,755,-1,756,757,758,-1,759,760,761,-1,762,763,764,-1,765,766,767,-1,768,769,770,-1,771,772,773,-1,774,775,776,-1,777,778,779,-1,780,781,782,-1,783,784,785,-1,786,787,788,-1,789,790,791,-1,792,793,794,-1,795,796,797,-1,798,799,800,-1,801,802,803,-1,804,805,806,-1,807,808,809,-1,810,811,812,-1,813,814,815,-1,816,817,818,-1,819,820,821,-1,822,823,824,-1,825,826,827,-1,828,829,830,-1,831,832,833,-1,834,835,836,-1,837,838,839,-1,840,841,842,-1,843,844,845,-1,846,847,848,-1,849,850,851,-1,852,853,854,-1,855,856,857,-1,858,859,860,-1,861,862,863,-1,864,865,866,-1,867,868,869,-1,870,871,872,-1,873,874,875,-1,876,877,878,-1,879,880,881,-1,882,883,884,-1,885,886,887,-1,888,889,890,-1,891,892,893,-1,894,895,896,-1,897,898,899,-1,900,901,902,-1,903,904,905,-1,906,907,908,-1,909,910,911,-1,912,913,914,-1,915,916,917,-1,918,919,920,-1,921,922,923,-1,924,925,926,-1,927,928,929,-1,930,931,932,-1,933,934,935,-1,936,937,938,-1,939,940,941,-1,942,943,944,-1,945,946,947,-1,948,949,950,-1,951,952,953,-1,954,955,956,-1,957,958,959,-1,960,961,962,-1,963,964,965,-1,966,967,968,-1,969,970,971,-1,972,973,974,-1,975,976,977,-1,978,979,980,-1,981,982,983,-1,984,985,986,-1,987,988,989,-1,990,991,992,-1,993,994,995,-1,996,997,998,-1,999,1000,1001,-1,1002,1003,1004,-1,1005,1006,1007,-1,1008,1009,1010,-1,1011,1012,1013,-1,1014,1015,1016,-1,1017,1018,1019,-1,1020,1021,1022,-1,1023,1024,1025,-1,1026,1027,1028,-1,1029,1030,1031,-1,1032,1033,1034,-1,1035,1036,1037,-1,1038,1039,1040,-1,1041,1042,1043,-1,1044,1045,1046,-1,1047,1048,1049,-1,1050,1051,1052,-1,1053,1054,1055,-1,1056,1057,1058,-1,1059,1060,1061,-1,1062,1063,1064,-1,1065,1066,1067,-1,1068,1069,1070,-1,1071,1072,1073,-1,1074,1075,1076,-1,1077,1078,1079,-1,1080,1081,1082,-1,1083,1084,1085,-1,1086,1087,1088,-1,1089,1090,1091,-1,1092,1093,1094,-1,1095,1096,1097,-1,1098,1099,1100,-1,1101,1102,1103,-1,1104,1105,1106,-1,1107,1108,1109,-1,1110,1111,1112,-1,1113,1114,1115,-1,1116,1117,1118,-1,1119,1120,1121,-1,1122,1123,1124,-1,1125,1126,1127,-1,1128,1129,1130,-1,1131,1132,1133,-1,1134,1135,1136,-1,1137,1138,1139,-1,1140,1141,1142,-1,1143,1144,1145,-1,1146,1147,1148,-1,1149,1150,1151,-1,1152,1153,1154,-1,1155,1156,1157,-1,1158,1159,1160,-1,1161,1162,1163,-1,1164,1165,1166,-1,1167,1168,1169,-1,1170,1171,1172,-1,1173,1174,1175,-1,1176,1177,1178,-1,1179,1180,1181,-1,1182,1183,1184,-1,1185,1186,1187,-1,1188,1189,1190,-1,1191,1192,1193,-1,1194,1195,1196,-1,1197,1198,1199,-1,1200,1201,1202,-1,1203,1204,1205,-1,1206,1207,1208,-1,1209,1210,1211,-1,1212,1213,1214,-1,1215,1216,1217,-1,1218,1219,1220,-1,1221,1222,1223,-1,1224,1225,1226,-1,1227,1228,1229,-1,1230,1231,1232,-1,1233,1234,1235,-1,1236,1237,1238,-1,1239,1240,1241,-1,1242,1243,1244,-1,1245,1246,1247,-1,1248,1249,1250,-1,1251,1252,1253,-1,1254,1255,1256,-1,1257,1258,1259,-1,1260,1261,1262,-1,1263,1264,1265,-1,1266,1267,1268,-1,1269,1270,1271,-1,1272,1273,1274,-1,1275,1276,1277,-1,1278,1279,1280,-1,1281,1282,1283,-1,1284,1285,1286,-1,1287,1288,1289,-1,1290,1291,1292,-1,1293,1294,1295,-1,1296,1297,1298,-1,1299,1300,1301,-1,1302,1303,1304,-1,1305,1306,1307,-1,1308,1309,1310,-1,1311,1312,1313,-1,1314,1315,1316,-1,1317,1318,1319,-1,1320,1321,1322,-1,1323,1324,1325,-1,1326,1327,1328,-1,1329,1330,1331,-1,1332,1333,1334,-1,1335,1336,1337,-1,1338,1339,1340,-1,1341,1342,1343,-1,1344,1345,1346,-1,1347,1348,1349,-1,1350,1351,1352,-1,1353,1354,1355,-1,1356,1357,1358,-1,1359,1360,1361,-1,1362,1363,1364,-1,1365,1366,1367,-1,1368,1369,1370,-1,1371,1372,1373,-1,1374,1375,1376,-1,1377,1378,1379,-1,1380,1381,1382,-1,1383,1384,1385,-1,1386,1387,1388,-1,1389,1390,1391,-1,1392,1393,1394,-1,1395,1396,1397,-1,1398,1399,1400,-1,1401,1402,1403,-1,1404,1405,1406,-1,1407,1408,1409,-1,1410,1411,1412,-1,1413,1414,1415,-1,1416,1417,1418,-1,1419,1420,1421,-1,1422,1423,1424,-1,1425,1426,1427,-1,1428,1429,1430,-1,1431,1432,1433,-1,1434,1435,1436,-1,1437,1438,1439,-1,1440,1441,1442,-1,1443,1444,1445,-1,1446,1447,1448,-1,1449,1450,1451,-1,1452,1453,1454,-1,1455,1456,1457,-1,1458,1459,1460,-1,1461,1462,1463,-1,1464,1465,1466,-1,1467,1468,1469,-1,1470,1471,1472,-1,1473,1474,1475,-1,1476,1477,1478,-1,1479,1480,1481,-1,1482,1483,1484,-1,1485,1486,1487,-1,1488,1489,1490,-1,1491,1492,1493,-1,1494,1495,1496,-1,1497,1498,1499,-1,1500,1501,1502,-1,1503,1504,1505,-1,1506,1507,1508,-1,1509,1510,1511,-1,1512,1513,1514,-1,1515,1516,1517,-1,1518,1519,1520,-1,1521,1522,1523,-1,1524,1525,1526,-1,1527,1528,1529,-1,1530,1529,1528,-1,1528,1531,1530,-1,1532,1530,1531,-1,1535,1533,1534,-1]
IndexedFaceSet420.creaseAngle = 1.65
Coordinate421 = x3d.Coordinate()

IndexedFaceSet420.coord = Coordinate421

Shape416.geometry = IndexedFaceSet420

Transform415.children.append(Shape416)

fieldValue414.children.append(Transform415)

ProtoInstance412.fieldValue.append(fieldValue414)

fieldValue411.children.append(ProtoInstance412)
ProtoInstance422 = x3d.ProtoInstance()
ProtoInstance422.name = "Joint"
ProtoInstance422.DEF = "Allen_hanim_l_elbow"
fieldValue423 = x3d.fieldValue()
fieldValue423.name = "name"
fieldValue423.value = "l_elbow"

ProtoInstance422.fieldValue.append(fieldValue423)
fieldValue424 = x3d.fieldValue()
fieldValue424.name = "center"
fieldValue424.value = "0.196 1.07 -0.0518"

ProtoInstance422.fieldValue.append(fieldValue424)
fieldValue425 = x3d.fieldValue()
fieldValue425.name = "children"
ProtoInstance426 = x3d.ProtoInstance()
ProtoInstance426.name = "Segment"
ProtoInstance426.DEF = "Allen_hanim_l_forearm"
fieldValue427 = x3d.fieldValue()
fieldValue427.name = "name"
fieldValue427.value = "l_forearm"

ProtoInstance426.fieldValue.append(fieldValue427)
fieldValue428 = x3d.fieldValue()
fieldValue428.name = "children"
Transform429 = x3d.Transform()
Transform429.DEF = "Allen_l_forearm_adjust"
Transform429.center = [-0.634,1.01,0.0799]
Transform429.rotation = [0,1,0,1.570796]
Transform429.scale = [0.1,0.1,0.1]
Shape430 = x3d.Shape()
Appearance431 = x3d.Appearance()
Material432 = x3d.Material()
Material432.USE = "Skin_Color"

Appearance431.material = Material432
ImageTexture433 = x3d.ImageTexture()
ImageTexture433.USE = "camo"

Appearance431.texture = ImageTexture433

Shape430.appearance = Appearance431
IndexedFaceSet434 = x3d.IndexedFaceSet()
IndexedFaceSet434.coordIndex = [0,1,2,-1,3,4,5,-1,6,7,8,-1,9,10,11,-1,12,13,14,-1,15,16,17,-1,18,19,20,-1,21,22,23,-1,24,25,26,-1,27,28,29,-1,30,31,32,-1,33,34,35,-1,36,37,38,-1,39,40,41,-1,42,43,44,-1,45,46,47,-1,48,49,50,-1,51,52,53,-1,54,55,56,-1,57,58,59,-1,60,61,62,-1,63,64,65,-1,66,67,68,-1,69,70,71,-1,72,73,74,-1,75,76,77,-1,78,79,80,-1,81,82,83,-1,84,85,86,-1,87,88,89,-1,90,91,92,-1,93,94,95,-1,96,97,98,-1,99,100,101,-1,102,103,104,-1,105,106,107,-1,108,109,110,-1,111,112,113,-1,114,115,116,-1,117,118,119,-1,120,121,122,-1,123,124,125,-1,126,127,128,-1,129,130,131,-1,132,133,134,-1,135,136,137,-1,138,139,140,-1,141,142,143,-1,144,145,146,-1,147,148,149,-1,150,151,152,-1,153,154,155,-1,156,157,158,-1,159,160,161,-1,162,163,164,-1,165,166,167,-1,168,169,170,-1,171,172,173,-1,174,175,176,-1,177,178,179,-1,180,181,182,-1,183,184,185,-1,186,187,188,-1,189,190,191,-1,192,193,194,-1,195,196,197,-1,198,199,200,-1,201,202,203,-1,204,205,206,-1,207,208,209,-1,210,211,212,-1,213,214,215,-1,216,217,218,-1,219,220,221,-1,222,223,224,-1,225,226,227,-1,228,229,230,-1,231,232,233,-1,234,235,236,-1,237,238,239,-1,240,241,242,-1,243,244,245,-1,246,247,248,-1,249,250,251,-1,252,253,254,-1,255,256,257,-1,258,259,260,-1,261,262,263,-1,264,265,266,-1,267,268,269,-1,270,271,272,-1,273,274,275,-1,276,277,278,-1,279,280,281,-1,282,283,284,-1,285,286,287,-1,288,289,290,-1,291,292,293,-1,294,295,296,-1,297,298,299,-1,300,301,302,-1,303,304,305,-1,306,307,308,-1,309,310,311,-1,312,313,314,-1,315,316,317,-1,318,319,320,-1,321,322,323,-1,324,325,326,-1,327,328,329,-1,330,331,332,-1,333,334,335,-1,336,337,338,-1,339,340,341,-1,342,343,344,-1,345,346,347,-1,348,349,350,-1,351,352,353,-1,354,355,356,-1,357,358,359,-1,360,361,362,-1,363,364,365,-1,366,367,368,-1,369,370,371,-1,372,373,374,-1,375,376,377,-1,378,379,380,-1,381,382,383,-1,384,385,386,-1,387,388,389,-1,390,391,392,-1,393,394,395,-1,396,397,398,-1,399,400,401,-1,402,403,404,-1,405,406,407,-1,408,409,410,-1,411,412,413,-1,414,415,416,-1,417,418,419,-1,420,421,422,-1,423,424,425,-1,426,427,428,-1,429,430,431,-1,432,433,434,-1,435,436,437,-1,438,439,440,-1,441,442,443,-1,444,445,446,-1,447,448,449,-1,450,451,452,-1,453,454,455,-1,456,457,458,-1,459,460,461,-1,462,463,464,-1,465,466,467,-1,468,469,470,-1,471,472,473,-1,474,475,476,-1,477,478,479,-1,480,481,482,-1,483,484,485,-1,486,487,488,-1,489,490,491,-1,492,493,494,-1,495,496,497,-1,498,499,500,-1,501,502,503,-1,504,505,506,-1,507,508,509,-1,510,511,512,-1,513,514,515,-1,516,517,518,-1,519,520,521,-1,522,523,524,-1,525,526,527,-1,528,529,530,-1,531,532,533,-1,534,535,536,-1,537,538,539,-1,540,541,542,-1,543,544,545,-1,546,547,548,-1,549,550,551,-1,552,553,554,-1,555,556,557,-1,558,559,560,-1,561,562,563,-1,564,565,566,-1,567,568,569,-1,570,571,572,-1,573,574,575,-1,576,577,578,-1,579,580,581,-1,582,583,584,-1,585,586,587,-1,588,589,590,-1,591,592,593,-1,594,595,596,-1,597,598,599,-1,600,601,602,-1,603,604,605,-1,606,607,608,-1,609,610,611,-1,612,613,614,-1,615,616,617,-1,618,619,620,-1,621,622,623,-1,624,625,626,-1,627,628,629,-1,630,631,632,-1,633,634,635,-1,636,637,638,-1,639,640,641,-1,642,643,644,-1,645,646,647,-1,648,649,650,-1,651,652,653,-1,654,655,656,-1,657,658,659,-1,660,661,662,-1,663,664,665,-1,666,667,668,-1,669,670,671,-1,672,673,674,-1,675,676,677,-1,678,679,680,-1,681,682,683,-1,684,685,686,-1,687,688,689,-1,690,691,692,-1,693,694,695,-1,696,697,698,-1,699,700,701,-1,702,703,704,-1,705,706,707,-1,708,709,710,-1,711,712,713,-1,714,715,716,-1,717,718,719,-1,720,721,722,-1,723,724,725,-1,726,727,728,-1,729,730,731,-1,732,733,734,-1,735,736,737,-1,738,739,740,-1,741,742,743,-1,744,745,746,-1,747,748,749,-1,750,751,752,-1,753,754,755,-1,756,757,758,-1,759,760,761,-1,762,763,764,-1,765,766,767,-1,768,769,770,-1,771,772,773,-1,774,775,776,-1,777,778,779,-1,780,781,782,-1,783,784,785,-1,786,787,788,-1,789,790,791,-1,792,793,794,-1,795,796,797,-1,798,799,800,-1,801,802,803,-1,804,805,806,-1,807,808,809,-1,810,811,812,-1,813,814,815,-1,816,817,818,-1,819,820,821,-1,822,823,824,-1,825,826,827,-1,828,829,830,-1,831,832,833,-1,834,835,836,-1,837,838,839,-1,840,841,842,-1,843,844,845,-1,846,847,848,-1,849,850,851,-1,852,853,854,-1,855,856,857,-1,858,859,860,-1,861,862,863,-1,864,865,866,-1,867,868,869,-1,870,871,872,-1,873,874,875,-1,876,877,878,-1,879,880,881,-1,882,883,884,-1,885,886,887,-1,888,889,890,-1,891,892,893,-1,894,895,896,-1,897,898,899,-1,900,901,902,-1,903,904,905,-1,906,907,908,-1,909,910,911,-1,912,913,914,-1,915,916,917,-1,918,919,920,-1,921,922,923,-1,924,925,926,-1,927,928,929,-1,930,931,932,-1,933,934,935,-1,936,937,938,-1,939,940,941,-1,942,943,944,-1,945,946,947,-1,948,949,950,-1,951,952,953,-1,954,955,956,-1,957,958,959,-1,960,961,962,-1,963,964,965,-1,966,967,968,-1,969,970,971,-1,972,973,974,-1,975,976,977,-1,978,979,980,-1,981,982,983,-1,984,985,986,-1,987,988,989,-1,990,991,992,-1,993,994,995,-1,996,997,998,-1,999,1000,1001,-1,1002,1003,1004,-1,1005,1006,1007,-1,1008,1009,1010,-1,1011,1012,1013,-1,1014,1015,1016,-1,1017,1018,1019,-1,1020,1021,1022,-1,1023,1024,1025,-1,1026,1027,1028,-1,1029,1030,1031,-1,1032,1033,1034,-1,1035,1036,1037,-1,1038,1039,1040,-1,1041,1042,1043,-1,1044,1045,1046,-1,1047,1048,1049,-1,1050,1051,1052,-1,1053,1054,1055,-1,1056,1057,1058,-1,1059,1060,1061,-1,1062,1063,1064,-1,1065,1066,1067,-1,1068,1069,1070,-1,1071,1072,1073,-1,1074,1075,1076,-1,1077,1078,1079,-1,1080,1081,1082,-1,1083,1084,1085,-1,1086,1087,1088,-1,1089,1090,1091,-1,1092,1093,1094,-1,1095,1096,1097,-1,1098,1099,1100,-1,1101,1102,1103,-1,1104,1105,1106,-1,1107,1108,1109,-1,1110,1111,1112,-1,1113,1114,1115,-1,1116,1117,1118,-1,1119,1120,1121,-1,1122,1123,1124,-1,1125,1126,1127,-1,1128,1129,1130,-1,1131,1132,1133,-1,1134,1135,1136,-1,1137,1138,1139,-1,1140,1141,1142,-1,1143,1144,1145,-1,1146,1147,1148,-1,1149,1150,1151,-1,1152,1153,1154,-1,1155,1156,1157,-1,1158,1159,1160,-1,1161,1162,1163,-1,1164,1165,1166,-1,1167,1168,1169,-1,1170,1171,1172,-1,1173,1174,1175,-1,1176,1177,1178,-1,1179,1180,1181,-1,1182,1183,1184,-1,1185,1186,1187,-1,1188,1189,1190,-1,1191,1192,1193,-1,1194,1195,1196,-1,1197,1198,1199,-1,1200,1201,1202,-1,1203,1204,1205,-1,1206,1207,1208,-1,1209,1210,1211,-1,1212,1213,1214,-1,1215,1216,1217,-1,1218,1219,1220,-1,1221,1222,1223,-1,1224,1225,1226,-1,1227,1228,1229,-1,1230,1231,1232,-1,1233,1234,1235,-1,1236,1237,1238,-1,1239,1240,1241,-1,1242,1243,1244,-1,1245,1246,1247,-1,1248,1249,1250,-1,1251,1252,1253,-1,1254,1255,1256,-1,1257,1258,1259,-1,1260,1261,1262,-1,1263,1264,1265,-1,1266,1267,1268,-1,1269,1270,1271,-1,1272,1273,1274,-1,1275,1276,1277,-1,1278,1279,1280,-1,1281,1282,1283,-1,1284,1285,1286,-1,1287,1288,1289,-1,1290,1291,1292,-1,1293,1294,1295,-1,1296,1297,1298,-1,1299,1300,1301,-1,1302,1303,1304,-1,1305,1306,1307,-1,1308,1309,1310,-1,1311,1312,1313,-1,1314,1315,1316,-1,1317,1318,1319,-1,1320,1321,1322,-1,1323,1324,1325,-1,1326,1327,1328,-1,1329,1330,1331,-1,1332,1333,1334,-1,1335,1336,1337,-1,1338,1339,1340,-1,1341,1342,1343,-1,1344,1345,1346,-1,1347,1348,1349,-1,1350,1351,1352,-1,1353,1354,1355,-1,1356,1357,1358,-1,1359,1360,1361,-1,1362,1363,1364,-1,1365,1366,1367,-1,1368,1369,1370,-1,1371,1372,1373,-1,1374,1375,1376,-1,1377,1378,1379,-1,1380,1381,1382,-1,1383,1384,1385,-1,1386,1387,1388,-1,1389,1390,1391,-1,1392,1393,1394,-1,1395,1396,1397,-1,1398,1399,1400,-1,1401,1402,1403,-1,1404,1405,1406,-1,1407,1408,1409,-1,1410,1411,1412,-1,1413,1414,1415,-1,1416,1417,1418,-1,1419,1420,1421,-1,1422,1423,1424,-1,1425,1426,1427,-1,1428,1429,1430,-1,1431,1432,1433,-1,1434,1435,1436,-1,1437,1438,1439,-1,1440,1441,1442,-1,1443,1444,1445,-1,1446,1447,1448,-1,1449,1450,1451,-1,1452,1453,1454,-1,1455,1456,1457,-1,1458,1459,1460,-1,1461,1462,1463,-1,1464,1465,1466,-1,1467,1468,1469,-1,1470,1471,1472,-1,1473,1474,1475,-1,1476,1477,1478,-1,1479,1480,1481,-1,1482,1483,1484,-1,1485,1486,1487,-1]
IndexedFaceSet434.creaseAngle = 1.75
Coordinate435 = x3d.Coordinate()

IndexedFaceSet434.coord = Coordinate435

Shape430.geometry = IndexedFaceSet434

Transform429.children.append(Shape430)

fieldValue428.children.append(Transform429)

ProtoInstance426.fieldValue.append(fieldValue428)

fieldValue425.children.append(ProtoInstance426)
ProtoInstance436 = x3d.ProtoInstance()
ProtoInstance436.name = "Joint"
ProtoInstance436.DEF = "Allen_hanim_l_wrist"
fieldValue437 = x3d.fieldValue()
fieldValue437.name = "name"
fieldValue437.value = "l_wrist"

ProtoInstance436.fieldValue.append(fieldValue437)
fieldValue438 = x3d.fieldValue()
fieldValue438.name = "center"
fieldValue438.value = "0.213 0.811 -0.0338"

ProtoInstance436.fieldValue.append(fieldValue438)
fieldValue439 = x3d.fieldValue()
fieldValue439.name = "children"
ProtoInstance440 = x3d.ProtoInstance()
ProtoInstance440.name = "Segment"
ProtoInstance440.DEF = "Allen_hanim_l_hand"
fieldValue441 = x3d.fieldValue()
fieldValue441.name = "name"
fieldValue441.value = "l_hand"

ProtoInstance440.fieldValue.append(fieldValue441)
fieldValue442 = x3d.fieldValue()
fieldValue442.name = "children"
Transform443 = x3d.Transform()
Transform443.DEF = "Allen_l_hand_adjust"
Transform443.center = [-0.8355,1.015,0.1]
Transform443.rotation = [0,1,0,1.570796]
Transform443.scale = [0.1,0.1,0.1]
Shape444 = x3d.Shape()
Appearance445 = x3d.Appearance()
Material446 = x3d.Material()
Material446.USE = "Skin_Color"

Appearance445.material = Material446

Shape444.appearance = Appearance445
IndexedFaceSet447 = x3d.IndexedFaceSet()
IndexedFaceSet447.coordIndex = [0,1,2,-1,3,4,5,-1,6,7,8,-1,9,10,11,-1,12,13,14,-1,15,16,17,-1,18,19,20,-1,21,22,23,-1,24,25,26,-1,27,28,29,-1,30,31,32,-1,33,34,35,-1,36,37,38,-1,39,40,41,-1,42,43,44,-1,45,46,47,-1,48,49,50,-1,51,52,53,-1,54,55,56,-1,57,58,59,-1,60,61,62,-1,63,64,65,-1,66,67,68,-1,69,70,71,-1,72,73,74,-1,75,76,77,-1,78,79,80,-1,81,82,83,-1,84,85,86,-1,87,88,89,-1,90,91,92,-1,93,94,95,-1,96,97,98,-1,99,100,101,-1,102,103,104,-1,105,106,107,-1,108,109,110,-1,111,112,113,-1,114,115,116,-1,117,118,119,-1,120,121,122,-1,123,124,125,-1,126,127,128,-1,129,130,131,-1,132,133,134,-1,135,136,137,-1,138,139,140,-1,141,142,143,-1,144,145,146,-1,147,148,149,-1,150,151,152,-1,153,154,155,-1,156,157,158,-1,159,160,161,-1,162,163,164,-1,165,166,167,-1,168,169,170,-1,171,172,173,-1,174,175,176,-1,177,178,179,-1,180,181,182,-1,183,184,185,-1,186,187,188,-1,189,190,191,-1,192,193,194,-1,195,196,197,-1,198,199,200,-1,201,202,203,-1,204,205,206,-1,207,208,209,-1,210,211,212,-1,213,214,215,-1,216,217,218,-1,219,220,221,-1,222,223,224,-1,225,226,227,-1,228,229,230,-1,231,232,233,-1,234,235,236,-1,237,238,239,-1,240,241,242,-1,243,244,245,-1,246,247,248,-1,249,250,251,-1,252,253,254,-1,255,256,257,-1,258,259,260,-1,261,262,263,-1,264,265,266,-1,267,268,269,-1,270,271,272,-1,273,274,275,-1,276,277,278,-1,279,280,281,-1,282,283,284,-1,285,286,287,-1,288,289,290,-1,291,292,293,-1,294,295,296,-1,297,298,299,-1,300,301,302,-1,303,304,305,-1,306,307,308,-1,309,310,311,-1,312,313,314,-1,315,316,317,-1,318,319,320,-1,321,322,323,-1,324,325,326,-1,327,328,329,-1,330,331,332,-1,333,334,335,-1,336,337,338,-1,339,340,341,-1,342,343,344,-1,345,346,347,-1,348,349,350,-1,351,352,353,-1,354,355,356,-1,357,358,359,-1,360,361,362,-1,363,364,365,-1,366,367,368,-1,369,370,371,-1,372,373,374,-1,375,376,377,-1,378,379,380,-1,381,382,383,-1,384,385,386,-1,387,388,389,-1,390,391,392,-1,393,394,395,-1,396,397,398,-1,399,400,401,-1,402,403,404,-1,405,406,407,-1,408,409,410,-1,411,412,413,-1,414,415,416,-1,417,418,419,-1,420,421,422,-1,423,424,425,-1,426,427,428,-1,429,430,431,-1,432,433,434,-1,435,436,437,-1,438,439,440,-1,441,442,443,-1,444,445,446,-1,447,448,449,-1,450,451,452,-1,453,454,455,-1,456,457,458,-1,459,460,461,-1,462,463,464,-1,465,466,467,-1,468,469,470,-1,471,472,473,-1,474,475,476,-1,477,478,479,-1,480,481,482,-1,483,484,485,-1,486,487,488,-1,489,490,491,-1,492,493,494,-1,495,496,497,-1,498,499,500,-1,501,502,503,-1,504,505,506,-1,507,508,509,-1,510,511,512,-1,513,514,515,-1,516,517,518,-1,519,520,521,-1,522,523,524,-1,525,526,527,-1,528,529,530,-1,531,532,533,-1,534,535,536,-1,537,538,539,-1,540,541,542,-1,543,544,545,-1,546,547,548,-1,549,550,551,-1,552,553,554,-1,555,556,557,-1,558,559,560,-1,561,562,563,-1,564,565,566,-1,567,568,569,-1,570,571,572,-1,573,574,575,-1,576,577,578,-1,579,580,581,-1,582,583,584,-1,585,586,587,-1,588,589,590,-1,591,592,593,-1,594,595,596,-1,597,598,599,-1,600,601,602,-1,603,604,605,-1,606,607,608,-1,609,610,611,-1,612,613,614,-1,615,616,617,-1,618,619,620,-1,621,622,623,-1,624,625,626,-1,627,628,629,-1,630,631,632,-1,633,634,635,-1,636,637,638,-1,639,640,641,-1,642,643,644,-1,645,646,647,-1,648,649,650,-1,651,652,653,-1,654,655,656,-1,657,658,659,-1,660,661,662,-1,663,664,665,-1,666,667,668,-1,669,670,671,-1]
IndexedFaceSet447.creaseAngle = 1.48
Coordinate448 = x3d.Coordinate()

IndexedFaceSet447.coord = Coordinate448

Shape444.geometry = IndexedFaceSet447

Transform443.children.append(Shape444)

fieldValue442.children.append(Transform443)

ProtoInstance440.fieldValue.append(fieldValue442)

fieldValue439.children.append(ProtoInstance440)

ProtoInstance436.fieldValue.append(fieldValue439)

fieldValue425.children.append(ProtoInstance436)

ProtoInstance422.fieldValue.append(fieldValue425)

fieldValue411.children.append(ProtoInstance422)

ProtoInstance408.fieldValue.append(fieldValue411)

fieldValue397.children.append(ProtoInstance408)
ProtoInstance449 = x3d.ProtoInstance()
ProtoInstance449.name = "Joint"
ProtoInstance449.DEF = "Allen_hanim_r_shoulder"
fieldValue450 = x3d.fieldValue()
fieldValue450.name = "name"
fieldValue450.value = "r_shoulder"

ProtoInstance449.fieldValue.append(fieldValue450)
fieldValue451 = x3d.fieldValue()
fieldValue451.name = "center"
fieldValue451.value = "-0.167 1.36 -0.0458"

ProtoInstance449.fieldValue.append(fieldValue451)
fieldValue452 = x3d.fieldValue()
fieldValue452.name = "children"
ProtoInstance453 = x3d.ProtoInstance()
ProtoInstance453.name = "Segment"
ProtoInstance453.DEF = "Allen_hanim_r_upperarm"
fieldValue454 = x3d.fieldValue()
fieldValue454.name = "name"
fieldValue454.value = "r_upperarm"

ProtoInstance453.fieldValue.append(fieldValue454)
fieldValue455 = x3d.fieldValue()
fieldValue455.name = "children"
Transform456 = x3d.Transform()
Transform456.DEF = "Allen_r_upperarm_adjust"
Transform456.center = [0.27,1,-0.025]
Transform456.rotation = [0,1,0,1.570796]
Transform456.scale = [0.1,0.1,0.1]
Shape457 = x3d.Shape()
Appearance458 = x3d.Appearance()
Material459 = x3d.Material()
Material459.USE = "Skin_Color"

Appearance458.material = Material459
ImageTexture460 = x3d.ImageTexture()
ImageTexture460.USE = "camo"

Appearance458.texture = ImageTexture460

Shape457.appearance = Appearance458
IndexedFaceSet461 = x3d.IndexedFaceSet()
IndexedFaceSet461.coordIndex = [0,1,2,-1,3,4,5,-1,6,7,8,-1,9,10,11,-1,12,13,14,-1,15,16,17,-1,18,19,20,-1,21,22,23,-1,24,25,26,-1,27,28,29,-1,30,31,32,-1,33,34,35,-1,36,37,38,-1,39,40,41,-1,42,43,44,-1,45,46,47,-1,48,49,50,-1,51,52,53,-1,54,55,56,-1,57,58,59,-1,60,61,62,-1,63,64,65,-1,66,67,68,-1,69,70,71,-1,72,73,74,-1,75,76,77,-1,78,79,80,-1,81,82,83,-1,84,85,86,-1,87,88,89,-1,90,91,92,-1,93,94,95,-1,96,97,98,-1,99,100,101,-1,102,103,104,-1,105,106,107,-1,108,109,110,-1,111,112,113,-1,114,115,116,-1,117,118,119,-1,120,121,122,-1,123,124,125,-1,126,127,128,-1,129,130,131,-1,132,133,134,-1,135,136,137,-1,138,139,140,-1,141,142,143,-1,144,145,146,-1,147,148,149,-1,150,151,152,-1,153,154,155,-1,156,157,158,-1,159,160,161,-1,162,163,164,-1,165,166,167,-1,168,169,170,-1,171,172,173,-1,174,175,176,-1,177,178,179,-1,180,181,182,-1,183,184,185,-1,186,187,188,-1,189,190,191,-1,192,193,194,-1,195,196,197,-1,198,199,200,-1,201,202,203,-1,204,205,206,-1,207,208,209,-1,210,211,212,-1,213,214,215,-1,216,217,218,-1,219,220,221,-1,222,223,224,-1,225,226,227,-1,228,229,230,-1,231,232,233,-1,234,235,236,-1,237,238,239,-1,240,241,242,-1,243,244,245,-1,246,247,248,-1,249,250,251,-1,252,253,254,-1,255,256,257,-1,258,259,260,-1,261,262,263,-1,264,265,266,-1,267,268,269,-1,270,271,272,-1,273,274,275,-1,276,277,278,-1,279,280,281,-1,282,283,284,-1,285,286,287,-1,288,289,290,-1,291,292,293,-1,294,295,296,-1,297,298,299,-1,300,301,302,-1,303,304,305,-1,306,307,308,-1,309,310,311,-1,312,313,314,-1,315,316,317,-1,318,319,320,-1,321,322,323,-1,324,325,326,-1,327,328,329,-1,330,331,332,-1,333,334,335,-1,336,337,338,-1,339,340,341,-1,342,343,344,-1,345,346,347,-1,348,349,350,-1,351,352,353,-1,354,355,356,-1,357,358,359,-1,360,361,362,-1,363,364,365,-1,366,367,368,-1,369,370,371,-1,372,373,374,-1,375,376,377,-1,378,379,380,-1,381,382,383,-1,384,385,386,-1,387,388,389,-1,390,391,392,-1,393,394,395,-1,396,397,398,-1,399,400,401,-1,402,403,404,-1,405,406,407,-1,408,409,410,-1,411,412,413,-1,414,415,416,-1,417,418,419,-1,420,421,422,-1,423,424,425,-1,426,427,428,-1,429,430,431,-1,432,433,434,-1,435,436,437,-1,438,439,440,-1,441,442,443,-1,444,445,446,-1,447,448,449,-1,450,451,452,-1,453,454,455,-1,456,457,458,-1,459,460,461,-1,462,463,464,-1,465,466,467,-1,468,469,470,-1,471,472,473,-1,474,475,476,-1,477,478,479,-1,480,481,482,-1,483,484,485,-1,486,487,488,-1,489,490,491,-1,492,493,494,-1,495,496,497,-1,498,499,500,-1,501,502,503,-1,504,505,506,-1,507,508,509,-1,510,511,512,-1,513,514,515,-1,516,517,518,-1,519,520,521,-1,522,523,524,-1,525,526,527,-1,528,529,530,-1,531,532,533,-1,534,535,536,-1,537,538,539,-1,540,541,542,-1,543,544,545,-1,546,547,548,-1,549,550,551,-1,552,553,554,-1,555,556,557,-1,558,559,560,-1,561,562,563,-1,564,565,566,-1,567,568,569,-1,570,571,572,-1,573,574,575,-1,576,577,578,-1,579,580,581,-1,582,583,584,-1,585,586,587,-1,588,589,590,-1,591,592,593,-1,594,595,596,-1,597,598,599,-1,600,601,602,-1,603,604,605,-1,606,607,608,-1,609,610,611,-1,612,613,614,-1,615,616,617,-1,618,619,620,-1,621,622,623,-1,624,625,626,-1,627,628,629,-1,630,631,632,-1,633,634,635,-1,636,637,638,-1,639,640,641,-1,642,643,644,-1,645,646,647,-1,648,649,650,-1,651,652,653,-1,654,655,656,-1,657,658,659,-1,660,661,662,-1,663,664,665,-1,666,667,668,-1,669,670,671,-1,672,673,674,-1,675,676,677,-1,678,679,680,-1,681,682,683,-1,684,685,686,-1,687,688,689,-1,690,691,692,-1,693,694,695,-1,696,697,698,-1,699,700,701,-1,702,703,704,-1,705,706,707,-1,708,709,710,-1,711,712,713,-1,714,715,716,-1,717,718,719,-1,720,721,722,-1,723,724,725,-1,726,727,728,-1,729,730,731,-1,732,733,734,-1,735,736,737,-1,738,739,740,-1,741,742,743,-1,744,745,746,-1,747,748,749,-1,750,751,752,-1,753,754,755,-1,756,757,758,-1,759,760,761,-1,762,763,764,-1,765,766,767,-1,768,769,770,-1,771,772,773,-1,774,775,776,-1,777,778,779,-1,780,781,782,-1,783,784,785,-1,786,787,788,-1,789,790,791,-1,792,793,794,-1,795,796,797,-1,798,799,800,-1,801,802,803,-1,804,805,806,-1,807,808,809,-1,810,811,812,-1,813,814,815,-1,816,817,818,-1,819,820,821,-1,822,823,824,-1,825,826,827,-1,828,829,830,-1,831,832,833,-1,834,835,836,-1,837,838,839,-1,840,841,842,-1,843,844,845,-1,846,847,848,-1,849,850,851,-1,852,853,854,-1,855,856,857,-1,858,859,860,-1,861,862,863,-1,864,865,866,-1,867,868,869,-1,870,871,872,-1,873,874,875,-1,876,877,878,-1,879,880,881,-1,882,883,884,-1,885,886,887,-1,888,889,890,-1,891,892,893,-1,894,895,896,-1,897,898,899,-1,900,901,902,-1,903,904,905,-1,906,907,908,-1,909,910,911,-1,912,913,914,-1,915,916,917,-1,918,919,920,-1,921,922,923,-1,924,925,926,-1,927,928,929,-1,930,931,932,-1,933,934,935,-1,936,937,938,-1,939,940,941,-1,942,943,944,-1,945,946,947,-1,948,949,950,-1,951,952,953,-1,954,955,956,-1,957,958,959,-1,960,961,962,-1,963,964,965,-1,966,967,968,-1,969,970,971,-1,972,973,974,-1,975,976,977,-1,978,979,980,-1,981,982,983,-1,984,985,986,-1,987,988,989,-1,990,991,992,-1,993,994,995,-1,996,997,998,-1,999,1000,1001,-1,1002,1003,1004,-1,1005,1006,1007,-1,1008,1009,1010,-1,1011,1012,1013,-1,1014,1015,1016,-1,1017,1018,1019,-1,1020,1021,1022,-1,1023,1024,1025,-1,1026,1027,1028,-1,1029,1030,1031,-1,1032,1033,1034,-1,1035,1036,1037,-1,1038,1039,1040,-1,1041,1042,1043,-1,1044,1045,1046,-1,1047,1048,1049,-1,1050,1051,1052,-1,1053,1054,1055,-1,1056,1057,1058,-1,1059,1060,1061,-1,1062,1063,1064,-1,1065,1066,1067,-1,1068,1069,1070,-1,1071,1072,1073,-1,1074,1075,1076,-1,1077,1078,1079,-1,1080,1081,1082,-1,1083,1084,1085,-1,1086,1087,1088,-1,1089,1090,1091,-1,1092,1093,1094,-1,1095,1096,1097,-1,1098,1099,1100,-1,1101,1102,1103,-1,1104,1105,1106,-1,1107,1108,1109,-1,1110,1111,1112,-1,1113,1114,1115,-1,1116,1117,1118,-1,1119,1120,1121,-1,1122,1123,1124,-1,1125,1126,1127,-1,1128,1129,1130,-1,1131,1132,1133,-1,1134,1135,1136,-1,1137,1138,1139,-1,1140,1141,1142,-1,1143,1144,1145,-1,1146,1147,1148,-1,1149,1150,1151,-1,1152,1153,1154,-1,1155,1156,1157,-1,1158,1159,1160,-1,1161,1162,1163,-1,1164,1165,1166,-1,1167,1168,1169,-1,1170,1171,1172,-1,1173,1174,1175,-1,1176,1177,1178,-1,1179,1180,1181,-1,1182,1183,1184,-1,1185,1186,1187,-1,1188,1189,1190,-1,1191,1192,1193,-1,1194,1195,1196,-1,1197,1198,1199,-1,1200,1201,1202,-1,1203,1204,1205,-1,1206,1207,1208,-1,1209,1210,1211,-1,1212,1213,1214,-1,1215,1216,1217,-1,1218,1219,1220,-1,1221,1222,1223,-1,1224,1225,1226,-1,1227,1228,1229,-1,1230,1231,1232,-1,1233,1234,1235,-1,1236,1237,1238,-1,1239,1240,1241,-1,1242,1243,1244,-1,1245,1246,1247,-1,1248,1249,1250,-1,1251,1252,1253,-1,1254,1255,1256,-1,1257,1258,1259,-1,1260,1261,1262,-1,1263,1264,1265,-1,1266,1267,1268,-1,1269,1270,1271,-1,1272,1273,1274,-1,1275,1276,1277,-1,1278,1279,1280,-1,1281,1282,1283,-1,1284,1285,1286,-1,1287,1288,1289,-1,1290,1291,1292,-1,1293,1294,1295,-1,1296,1297,1298,-1,1299,1300,1301,-1,1302,1303,1304,-1,1305,1306,1307,-1,1308,1309,1310,-1,1311,1312,1313,-1,1314,1315,1316,-1,1317,1318,1319,-1,1320,1321,1322,-1,1323,1324,1325,-1,1326,1327,1328,-1,1329,1330,1331,-1,1332,1333,1334,-1,1335,1336,1337,-1,1338,1339,1340,-1,1341,1342,1343,-1,1344,1345,1346,-1,1347,1348,1349,-1,1350,1351,1352,-1,1353,1354,1355,-1,1356,1357,1358,-1,1359,1360,1361,-1,1362,1363,1364,-1,1365,1366,1367,-1,1368,1369,1370,-1,1371,1372,1373,-1,1374,1375,1376,-1,1377,1378,1379,-1,1380,1381,1382,-1,1383,1384,1385,-1,1386,1387,1388,-1,1389,1390,1391,-1,1392,1393,1394,-1,1395,1396,1397,-1,1398,1399,1400,-1,1401,1402,1403,-1,1404,1405,1406,-1,1407,1408,1409,-1,1410,1411,1412,-1,1413,1414,1415,-1,1416,1417,1418,-1,1419,1420,1421,-1,1422,1423,1424,-1,1425,1426,1427,-1,1428,1429,1430,-1,1431,1432,1433,-1,1434,1435,1436,-1,1437,1438,1439,-1,1440,1441,1442,-1,1443,1444,1445,-1,1446,1447,1448,-1,1449,1450,1451,-1,1452,1453,1454,-1,1455,1456,1457,-1,1458,1459,1460,-1,1461,1462,1463,-1,1464,1465,1466,-1,1467,1468,1469,-1,1470,1471,1472,-1,1473,1474,1475,-1,1476,1477,1478,-1,1479,1480,1481,-1,1482,1483,1484,-1,1485,1486,1487,-1,1488,1489,1490,-1,1491,1492,1493,-1,1494,1495,1496,-1,1497,1498,1499,-1,1500,1501,1502,-1,1503,1504,1505,-1,1506,1507,1508,-1,1509,1510,1511,-1,1512,1513,1514,-1,1515,1516,1517,-1,1518,1519,1520,-1,1521,1522,1523,-1,1524,1525,1526,-1,1527,1528,1529,-1,1530,1531,1532,-1,1533,1534,1535,-1,1536,1537,1538,-1,1539,1540,1541,-1,1542,1543,1544,-1,1545,1546,1547,-1,1548,1549,1550,-1,1551,1552,1553,-1,1554,1555,1556,-1,1557,1558,1559,-1,1560,1561,1562,-1,1563,1564,1565,-1,1566,1567,1568,-1,1569,1570,1571,-1,1572,1573,1574,-1,1575,1576,1577,-1,1578,1579,1580,-1,1581,1582,1583,-1,1584,1585,1586,-1,1587,1588,1589,-1,1590,1591,1592,-1,1593,1594,1595,-1,1596,1597,1598,-1,1599,1600,1601,-1,1602,1603,1604,-1,1605,1606,1607,-1,1608,1609,1610,-1,1611,1612,1613,-1,1614,1615,1616,-1,1617,1618,1619,-1,1620,1621,1622,-1,1623,1624,1625,-1,1626,1627,1628,-1,1629,1630,1631,-1,1632,1633,1634,-1,1635,1636,1637,-1,1638,1639,1640,-1,1641,1642,1643,-1,1644,1645,1646,-1,1647,1648,1649,-1,1650,1651,1652,-1,1653,1654,1655,-1,1656,1657,1658,-1,1659,1660,1661,-1,1662,1663,1664,-1,1665,1666,1667,-1,1668,1669,1670,-1,1671,1672,1673,-1,1674,1675,1676,-1,1677,1678,1679,-1,1680,1681,1682,-1,1683,1684,1685,-1,1686,1687,1688,-1,1689,1690,1691,-1,1692,1693,1694,-1,1695,1696,1697,-1,1698,1699,1700,-1,1701,1702,1703,-1,1704,1705,1706,-1,1707,1708,1709,-1,1710,1711,1712,-1,1713,1714,1715,-1,1716,1717,1718,-1,1719,1720,1721,-1,1722,1723,1724,-1,1725,1726,1727,-1,1728,1729,1730,-1,1731,1732,1733,-1,1734,1735,1736,-1,1737,1738,1739,-1,1740,1741,1742,-1,1743,1744,1745,-1,1746,1747,1748,-1,1749,1750,1751,-1,1752,1753,1754,-1,1755,1756,1757,-1,1758,1759,1760,-1,1761,1762,1763,-1,1764,1765,1766,-1,1767,1768,1769,-1,1770,1771,1772,-1,1773,1774,1775,-1,1776,1777,1778,-1,1779,1780,1781,-1,1782,1783,1784,-1,1785,1786,1787,-1,1788,1789,1790,-1,1791,1792,1793,-1,1794,1795,1796,-1,1797,1798,1799,-1,1800,1801,1802,-1,1803,1804,1805,-1,1806,1807,1808,-1,1809,1810,1811,-1,1812,1813,1814,-1]
IndexedFaceSet461.creaseAngle = 1.53
Coordinate462 = x3d.Coordinate()

IndexedFaceSet461.coord = Coordinate462

Shape457.geometry = IndexedFaceSet461

Transform456.children.append(Shape457)

fieldValue455.children.append(Transform456)

ProtoInstance453.fieldValue.append(fieldValue455)

fieldValue452.children.append(ProtoInstance453)
ProtoInstance463 = x3d.ProtoInstance()
ProtoInstance463.name = "Joint"
ProtoInstance463.DEF = "Allen_hanim_r_elbow"
fieldValue464 = x3d.fieldValue()
fieldValue464.name = "name"
fieldValue464.value = "r_elbow"

ProtoInstance463.fieldValue.append(fieldValue464)
fieldValue465 = x3d.fieldValue()
fieldValue465.name = "center"
fieldValue465.value = "-0.192 1.07 -0.0498"

ProtoInstance463.fieldValue.append(fieldValue465)
fieldValue466 = x3d.fieldValue()
fieldValue466.name = "children"
ProtoInstance467 = x3d.ProtoInstance()
ProtoInstance467.name = "Segment"
ProtoInstance467.DEF = "Allen_hanim_r_forearm"
fieldValue468 = x3d.fieldValue()
fieldValue468.name = "name"
fieldValue468.value = "r_forearm"

ProtoInstance467.fieldValue.append(fieldValue468)
fieldValue469 = x3d.fieldValue()
fieldValue469.name = "children"
Transform470 = x3d.Transform()
Transform470.DEF = "Allen_r_forearm_adjust"
Transform470.center = [0.7641,1.01,-0.07438]
Transform470.rotation = [0,1,0,1.570796]
Transform470.scale = [0.1,0.1,0.1]
Shape471 = x3d.Shape()
Appearance472 = x3d.Appearance()
Material473 = x3d.Material()
Material473.USE = "Skin_Color"

Appearance472.material = Material473
ImageTexture474 = x3d.ImageTexture()
ImageTexture474.USE = "camo"

Appearance472.texture = ImageTexture474

Shape471.appearance = Appearance472
IndexedFaceSet475 = x3d.IndexedFaceSet()
IndexedFaceSet475.coordIndex = [0,1,2,-1,3,4,5,-1,6,7,8,-1,9,10,11,-1,12,13,14,-1,15,16,17,-1,18,19,20,-1,21,22,23,-1,24,25,26,-1,27,28,29,-1,30,31,32,-1,33,34,35,-1,36,37,38,-1,39,40,41,-1,42,43,44,-1,45,46,47,-1,48,49,50,-1,51,52,53,-1,54,55,56,-1,57,58,59,-1,60,61,62,-1,63,64,65,-1,66,67,68,-1,69,70,71,-1,72,73,74,-1,75,76,77,-1,78,79,80,-1,81,82,83,-1,84,85,86,-1,87,88,89,-1,90,91,92,-1,93,94,95,-1,96,97,98,-1,99,100,101,-1,102,103,104,-1,105,106,107,-1,108,109,110,-1,111,112,113,-1,114,115,116,-1,117,118,119,-1,120,121,122,-1,123,124,125,-1,126,127,128,-1,129,130,131,-1,132,133,134,-1,135,136,137,-1,138,139,140,-1,141,142,143,-1,144,145,146,-1,147,148,149,-1,150,151,152,-1,153,154,155,-1,156,157,158,-1,159,160,161,-1,162,163,164,-1,165,166,167,-1,168,169,170,-1,171,172,173,-1,174,175,176,-1,177,178,179,-1,180,181,182,-1,183,184,185,-1,186,187,188,-1,189,190,191,-1,192,193,194,-1,195,196,197,-1,198,199,200,-1,201,202,203,-1,204,205,206,-1,207,208,209,-1,210,211,212,-1,213,214,215,-1,216,217,218,-1,219,220,221,-1,222,223,224,-1,225,226,227,-1,228,229,230,-1,231,232,233,-1,234,235,236,-1,237,238,239,-1,240,241,242,-1,243,244,245,-1,246,247,248,-1,249,250,251,-1,252,253,254,-1,255,256,257,-1,258,259,260,-1,261,262,263,-1,264,265,266,-1,267,268,269,-1,270,271,272,-1,273,274,275,-1,276,277,278,-1,279,280,281,-1,282,283,284,-1,285,286,287,-1,288,289,290,-1,291,292,293,-1,294,295,296,-1,297,298,299,-1,300,301,302,-1,63,65,60,-1,36,40,37,-1,40,39,37,-1,39,43,37,-1,43,42,37,-1,48,51,49,-1,60,65,61,-1,49,51,50,-1,51,53,50,-1,50,53,48,-1,48,53,47,-1,47,53,45,-1,45,53,42,-1,42,53,37,-1,53,54,37,-1,54,56,37,-1,65,37,61,-1,37,56,61,-1,62,61,60,-1,59,58,56,-1,56,58,61,-1,60,61,58,-1,303,304,305,-1,306,307,308,-1,309,310,311,-1,312,313,314,-1,315,316,317,-1,318,319,320,-1,321,322,323,-1,324,325,326,-1,327,328,329,-1,330,331,332,-1,333,334,335,-1,336,337,338,-1,339,340,341,-1,342,343,344,-1,345,346,347,-1,348,349,350,-1,351,352,353,-1,354,355,356,-1,357,358,359,-1,360,361,362,-1,363,364,365,-1,366,367,368,-1,369,370,371,-1,372,373,374,-1,375,376,377,-1,378,379,380,-1,381,382,383,-1,384,385,386,-1,387,388,389,-1,390,391,392,-1,393,394,395,-1,396,397,398,-1,399,400,401,-1,402,403,404,-1,405,406,407,-1,408,409,410,-1,411,412,413,-1,414,415,416,-1,417,418,419,-1,420,421,422,-1,423,424,425,-1,426,427,428,-1,429,430,431,-1,432,433,434,-1,435,436,437,-1,438,439,440,-1,441,442,443,-1,444,445,446,-1,447,448,449,-1,450,451,452,-1,453,454,455,-1,456,457,458,-1,459,460,461,-1,462,463,464,-1,465,466,467,-1,468,469,470,-1,471,472,473,-1,474,475,476,-1,477,478,479,-1,480,481,482,-1,483,484,485,-1,486,487,488,-1,489,490,491,-1,492,493,494,-1,495,496,497,-1,498,499,500,-1,501,502,503,-1,504,505,506,-1,507,508,509,-1,510,511,512,-1,513,514,515,-1,516,517,518,-1,519,520,521,-1,522,523,524,-1,525,526,527,-1,528,529,530,-1,531,532,533,-1,534,535,536,-1,537,538,539,-1,540,541,542,-1,543,544,545,-1,546,547,548,-1,549,550,551,-1,552,553,554,-1,555,556,557,-1,558,559,560,-1,561,562,563,-1,564,565,566,-1,567,568,569,-1,570,571,572,-1,573,574,575,-1,576,577,578,-1,579,580,581,-1,582,583,584,-1,585,586,587,-1,588,589,590,-1,591,592,593,-1,594,595,596,-1,597,598,599,-1,600,601,602,-1,603,604,605,-1,606,607,608,-1,609,610,611,-1,612,613,614,-1,615,616,617,-1,618,619,620,-1,621,622,623,-1,624,625,626,-1,627,628,629,-1,630,631,632,-1,633,634,635,-1,636,637,638,-1,639,640,641,-1,642,643,644,-1,645,646,647,-1,648,649,650,-1,651,652,653,-1,654,655,656,-1,657,658,659,-1,660,661,662,-1,663,664,665,-1,666,667,668,-1,669,670,671,-1,672,673,674,-1,675,676,677,-1,678,679,680,-1,681,682,683,-1,684,685,686,-1,687,688,689,-1,690,691,692,-1,693,694,695,-1,696,697,698,-1,699,700,701,-1,702,703,704,-1,705,706,707,-1,708,709,710,-1,711,712,713,-1,714,715,716,-1,717,718,719,-1,720,721,722,-1,723,724,725,-1,726,727,728,-1,729,730,731,-1,732,733,734,-1,735,736,737,-1,738,739,740,-1,741,742,743,-1,744,745,746,-1,747,748,749,-1,750,751,752,-1,753,754,755,-1,756,757,758,-1,759,760,761,-1,762,763,764,-1,765,766,767,-1,768,769,770,-1,771,772,773,-1,774,775,776,-1,777,778,779,-1,780,781,782,-1,783,784,785,-1,786,787,788,-1,789,790,791,-1,792,793,794,-1,795,796,797,-1,798,799,800,-1,801,802,803,-1,804,805,806,-1,807,808,809,-1,810,811,812,-1,813,814,815,-1,816,817,818,-1,819,820,821,-1,822,823,824,-1,825,826,827,-1,828,829,830,-1,831,832,833,-1,834,835,836,-1,837,838,839,-1,840,841,842,-1,843,844,845,-1,846,847,848,-1,849,850,851,-1,852,853,854,-1,855,856,857,-1,858,859,860,-1,861,862,863,-1,864,865,866,-1,867,868,869,-1,870,871,872,-1,873,874,875,-1,876,877,878,-1,879,880,881,-1,882,883,884,-1,885,886,887,-1,888,889,890,-1,891,892,893,-1,894,895,896,-1,897,898,899,-1,900,901,902,-1,903,904,905,-1,906,907,908,-1,909,910,911,-1,912,913,914,-1,915,916,917,-1,918,919,920,-1,921,922,923,-1,924,925,926,-1,927,928,929,-1,930,931,932,-1,933,934,935,-1,936,937,938,-1,939,940,941,-1,942,943,944,-1,945,946,947,-1,948,949,950,-1,951,952,953,-1,954,955,956,-1,957,958,959,-1,960,961,962,-1,963,964,965,-1,966,967,968,-1,969,970,971,-1,972,973,974,-1,975,976,977,-1,978,979,980,-1,981,982,983,-1,984,985,986,-1,987,988,989,-1,990,991,992,-1,993,994,995,-1,996,997,998,-1,999,1000,1001,-1,1002,1003,1004,-1,1005,1006,1007,-1,1008,1009,1010,-1,1011,1012,1013,-1,1014,1015,1016,-1,1017,1018,1019,-1,1020,1021,1022,-1,1023,1024,1025,-1,1026,1027,1028,-1,1029,1030,1031,-1,1032,1033,1034,-1,1035,1036,1037,-1,1038,1039,1040,-1,1041,1042,1043,-1,1044,1045,1046,-1,1047,1048,1049,-1,1050,1051,1052,-1,1053,1054,1055,-1,1056,1057,1058,-1,1059,1060,1061,-1,1062,1063,1064,-1,1065,1066,1067,-1,1068,1069,1070,-1,1071,1072,1073,-1,1074,1075,1076,-1,1077,1078,1079,-1,1080,1081,1082,-1,1083,1084,1085,-1,1086,1087,1088,-1,1089,1090,1091,-1,1092,1093,1094,-1,1095,1096,1097,-1,1098,1099,1100,-1,1101,1102,1103,-1,1104,1105,1106,-1,1107,1108,1109,-1,1110,1111,1112,-1,1113,1114,1115,-1,1116,1117,1118,-1,1119,1120,1121,-1,1122,1123,1124,-1,1125,1126,1127,-1,1128,1129,1130,-1,1131,1132,1133,-1,1134,1135,1136,-1,1137,1138,1139,-1,1140,1141,1142,-1,1143,1144,1145,-1,1146,1147,1148,-1,1149,1150,1151,-1,1152,1153,1154,-1,1155,1156,1157,-1,1158,1159,1160,-1,1161,1162,1163,-1,1164,1165,1166,-1,1167,1168,1169,-1,1170,1171,1172,-1,1173,1174,1175,-1,1176,1177,1178,-1,1179,1180,1181,-1,1182,1183,1184,-1,1185,1186,1187,-1,1188,1189,1190,-1,1191,1192,1193,-1,1194,1195,1196,-1,1197,1198,1199,-1,1200,1201,1202,-1,1203,1204,1205,-1,1206,1207,1208,-1,1209,1210,1211,-1,1212,1213,1214,-1,1215,1216,1217,-1,1218,1219,1220,-1,1221,1222,1223,-1,1224,1225,1226,-1,1227,1228,1229,-1,1230,1231,1232,-1,1233,1234,1235,-1,1236,1237,1238,-1,1239,1240,1241,-1,1242,1243,1244,-1,1245,1246,1247,-1,1248,1249,1250,-1,1251,1252,1253,-1,1254,1255,1256,-1,1257,1258,1259,-1,1260,1261,1262,-1,1263,1264,1265,-1,1266,1267,1268,-1,1269,1270,1271,-1,1272,1273,1274,-1,1275,1276,1277,-1,1278,1279,1280,-1,1281,1282,1283,-1,1284,1285,1286,-1,1287,1288,1289,-1,1290,1291,1292,-1,1293,1294,1295,-1,1296,1297,1298,-1,1299,1300,1301,-1,1302,1303,1304,-1,1305,1306,1307,-1,1308,1309,1310,-1,1311,1312,1313,-1,1314,1315,1316,-1,1317,1318,1319,-1,1320,1321,1322,-1,1323,1324,1325,-1,1326,1327,1328,-1,1329,1330,1331,-1,1332,1333,1334,-1,1335,1336,1337,-1,1338,1339,1340,-1,1341,1342,1343,-1,1344,1345,1346,-1,1347,1348,1349,-1,1350,1351,1352,-1,1353,1354,1355,-1,1356,1357,1358,-1,1359,1360,1361,-1,1362,1363,1364,-1,1365,1366,1367,-1,1368,1369,1370,-1,1371,1372,1373,-1,1374,1375,1376,-1,1377,1378,1379,-1,1380,1381,1382,-1,1383,1384,1385,-1,1386,1387,1388,-1,1389,1390,1391,-1,1392,1393,1394,-1,1395,1396,1397,-1,1398,1399,1400,-1,1401,1402,1403,-1,1404,1405,1406,-1,1407,1408,1409,-1,1410,1411,1412,-1,1413,1414,1415,-1,1416,1417,1418,-1,1419,1420,1421,-1,1422,1423,1424,-1,1425,1426,1427,-1,1428,1429,1430,-1,1431,1432,1433,-1,1434,1435,1436,-1,1437,1438,1439,-1,1440,1441,1442,-1,1443,1444,1445,-1,1446,1447,1448,-1,1449,1450,1451,-1,1452,1453,1454,-1,1455,1456,1457,-1,1458,1459,1460,-1,1461,1462,1463,-1,1464,1465,1466,-1,1467,1468,1469,-1,1470,1471,1472,-1,1473,1474,1475,-1,1476,1477,1478,-1,1479,1480,1481,-1,1482,1483,1484,-1,1485,1486,1487,-1,1488,1489,1490,-1,1491,1492,1493,-1,1494,1495,1496,-1,1497,1498,1499,-1,1500,1501,1502,-1,1503,1504,1505,-1,1506,1507,1508,-1,1509,1510,1511,-1,1512,1513,1514,-1,1515,1516,1517,-1,1518,1519,1520,-1,1521,1522,1523,-1,1524,1525,1526,-1,1527,1528,1529,-1,1530,1531,1532,-1,1533,1534,1535,-1,1536,1537,1538,-1,1539,1540,1541,-1,1542,1543,1544,-1,1545,1546,1547,-1,1548,1549,1550,-1,1551,1552,1553,-1,1554,1555,1556,-1,1557,1558,1559,-1,1560,1561,1562,-1,1563,1564,1565,-1,1566,1567,1568,-1,1569,1570,1571,-1,1572,1573,1574,-1,1575,1576,1577,-1,1578,1579,1580,-1,1581,1582,1583,-1,1584,1585,1586,-1,1587,1588,1589,-1,1590,1591,1592,-1,1593,1594,1595,-1,1596,1597,1598,-1,1599,1600,1601,-1,1602,1603,1604,-1,1605,1606,1607,-1,1608,1609,1610,-1,1611,1612,1613,-1,1614,1615,1616,-1,1617,1618,1619,-1,1620,1621,1622,-1,1623,1624,1625,-1,1626,1627,1628,-1,1629,1630,1631,-1,1632,1633,1634,-1,1635,1636,1637,-1,1638,1639,1640,-1,1641,1642,1643,-1,1644,1645,1646,-1,1647,1648,1649,-1,1650,1651,1652,-1,1653,1654,1655,-1,1656,1657,1658,-1,1659,1660,1661,-1,1662,1663,1664,-1,1665,1666,1667,-1,1668,1669,1670,-1,1671,1672,1673,-1,1674,1675,1676,-1,1677,1678,1679,-1,1680,1681,1682,-1,1683,1684,1685,-1,1686,1687,1688,-1,1689,1690,1691,-1,1692,1693,1694,-1,1695,1696,1697,-1,1698,1699,1700,-1,1701,1702,1703,-1,1704,1705,1706,-1,1707,1708,1709,-1,1710,1711,1712,-1,1713,1714,1715,-1,1716,1717,1718,-1,1719,1720,1721,-1]
IndexedFaceSet475.creaseAngle = 1.73
Coordinate476 = x3d.Coordinate()

IndexedFaceSet475.coord = Coordinate476

Shape471.geometry = IndexedFaceSet475

Transform470.children.append(Shape471)

fieldValue469.children.append(Transform470)

ProtoInstance467.fieldValue.append(fieldValue469)

fieldValue466.children.append(ProtoInstance467)
ProtoInstance477 = x3d.ProtoInstance()
ProtoInstance477.name = "Joint"
ProtoInstance477.DEF = "Allen_hanim_r_wrist"
fieldValue478 = x3d.fieldValue()
fieldValue478.name = "name"
fieldValue478.value = "r_wrist"

ProtoInstance477.fieldValue.append(fieldValue478)
fieldValue479 = x3d.fieldValue()
fieldValue479.name = "center"
fieldValue479.value = "-0.217 0.811 -0.0338"

ProtoInstance477.fieldValue.append(fieldValue479)
fieldValue480 = x3d.fieldValue()
fieldValue480.name = "children"
ProtoInstance481 = x3d.ProtoInstance()
ProtoInstance481.name = "Segment"
ProtoInstance481.DEF = "Allen_hanim_r_hand"
fieldValue482 = x3d.fieldValue()
fieldValue482.name = "name"
fieldValue482.value = "r_hand"

ProtoInstance481.fieldValue.append(fieldValue482)
fieldValue483 = x3d.fieldValue()
fieldValue483.name = "children"
Transform484 = x3d.Transform()
Transform484.DEF = "Allen_r_hand_adjust"
Transform484.center = [0.2693,1.011,-0.0248]
Transform484.rotation = [0,1,0,1.570796]
Transform484.scale = [0.1,0.1,0.1]
Shape485 = x3d.Shape()
Appearance486 = x3d.Appearance()
Material487 = x3d.Material()
Material487.USE = "Skin_Color"

Appearance486.material = Material487

Shape485.appearance = Appearance486
IndexedFaceSet488 = x3d.IndexedFaceSet()
IndexedFaceSet488.coordIndex = [0,1,2,-1,3,4,5,-1,6,7,8,-1,9,10,11,-1,12,13,14,-1,15,16,17,-1,18,19,20,-1,21,22,23,-1,24,25,26,-1,27,28,29,-1,30,31,32,-1,33,34,35,-1,36,37,38,-1,39,40,41,-1,42,43,44,-1,45,46,47,-1,48,49,50,-1,51,52,53,-1,54,55,56,-1,57,58,59,-1,60,61,62,-1,63,64,65,-1,66,67,68,-1,69,70,71,-1,72,73,74,-1,75,76,77,-1,78,79,80,-1,81,82,83,-1,84,85,86,-1,87,88,89,-1,90,91,92,-1,93,94,95,-1,96,97,98,-1,99,100,101,-1,102,103,104,-1,105,106,107,-1,108,109,110,-1,111,112,113,-1,114,115,116,-1,117,118,119,-1,120,121,122,-1,123,124,125,-1,126,127,128,-1,129,130,131,-1,132,133,134,-1,135,136,137,-1,138,139,140,-1,141,142,143,-1,144,145,146,-1,147,148,149,-1,150,151,152,-1,153,154,155,-1,156,157,158,-1,159,160,161,-1,162,163,164,-1,165,166,167,-1,168,169,170,-1,171,172,173,-1,174,175,176,-1,177,178,179,-1,180,181,182,-1,183,184,185,-1,186,187,188,-1,189,190,191,-1,192,193,194,-1,195,196,197,-1,198,199,200,-1,201,202,203,-1,204,205,206,-1,207,208,209,-1,210,211,212,-1,213,214,215,-1,216,217,218,-1,219,220,221,-1,222,223,224,-1,225,226,227,-1,228,229,230,-1,231,232,233,-1,234,235,236,-1,237,238,239,-1,240,241,242,-1,243,244,245,-1,246,247,248,-1,249,250,251,-1,252,253,254,-1,255,256,257,-1,258,259,260,-1,261,262,263,-1,264,265,266,-1,267,268,269,-1,270,271,272,-1,273,274,275,-1,276,277,278,-1,279,280,281,-1,282,283,284,-1,285,286,287,-1,288,289,290,-1,291,292,293,-1,294,295,296,-1,297,298,299,-1,300,301,302,-1,303,304,305,-1,306,307,308,-1,309,310,311,-1,312,313,314,-1,315,316,317,-1,318,319,320,-1,321,322,323,-1,324,325,326,-1,327,328,329,-1,330,331,332,-1,333,334,335,-1,336,337,338,-1,339,340,341,-1,342,343,344,-1,345,346,347,-1,348,349,350,-1,351,352,353,-1,354,355,356,-1,357,358,359,-1,360,361,362,-1,363,364,365,-1,366,367,368,-1,369,370,371,-1,372,373,374,-1,375,376,377,-1,378,379,380,-1,381,382,383,-1,384,385,386,-1,387,388,389,-1,390,391,392,-1,393,394,395,-1,396,397,398,-1,399,400,401,-1,402,403,404,-1,405,406,407,-1,408,409,410,-1,411,412,413,-1,414,415,416,-1,417,418,419,-1,420,421,422,-1,423,424,425,-1,426,427,428,-1,429,430,431,-1,432,433,434,-1,435,436,437,-1,438,439,440,-1,441,442,443,-1,444,445,446,-1,447,448,449,-1,450,451,452,-1,453,454,455,-1,456,457,458,-1,459,460,461,-1,462,463,464,-1,465,466,467,-1,468,469,470,-1,471,472,473,-1,474,475,476,-1,477,478,479,-1,480,481,482,-1,483,484,485,-1,486,487,488,-1,489,490,491,-1,492,493,494,-1,495,496,497,-1,498,499,500,-1,501,502,503,-1,504,505,506,-1,507,508,509,-1,510,511,512,-1,513,514,515,-1,516,517,518,-1,519,520,521,-1,522,523,524,-1,525,526,527,-1,528,529,530,-1,531,532,533,-1,534,535,536,-1,537,538,539,-1,540,541,542,-1,543,544,545,-1,546,547,548,-1,549,550,551,-1,552,553,554,-1,555,556,557,-1,558,559,560,-1,561,562,563,-1,564,565,566,-1,567,568,569,-1,570,571,572,-1,573,574,575,-1,576,577,578,-1,579,580,581,-1,582,583,584,-1,585,586,587,-1,588,589,590,-1,591,592,593,-1,594,595,596,-1,597,598,599,-1,600,601,602,-1,603,604,605,-1,606,607,608,-1,609,610,611,-1,612,613,614,-1,615,616,617,-1,618,619,620,-1,621,622,623,-1,624,625,626,-1,627,628,629,-1,630,631,632,-1,633,634,635,-1,636,637,638,-1,639,640,641,-1,642,643,644,-1,645,646,647,-1,648,649,650,-1,651,652,653,-1,654,655,656,-1,657,658,659,-1,660,661,662,-1,663,664,665,-1,666,667,668,-1,669,670,671,-1,672,673,674,-1,675,676,677,-1,678,679,680,-1,681,682,683,-1,684,685,686,-1,687,688,689,-1,690,691,692,-1,694,695,693,-1]
IndexedFaceSet488.creaseAngle = 1.57
Coordinate489 = x3d.Coordinate()

IndexedFaceSet488.coord = Coordinate489

Shape485.geometry = IndexedFaceSet488

Transform484.children.append(Shape485)

fieldValue483.children.append(Transform484)

ProtoInstance481.fieldValue.append(fieldValue483)

fieldValue480.children.append(ProtoInstance481)

ProtoInstance477.fieldValue.append(fieldValue480)

fieldValue466.children.append(ProtoInstance477)

ProtoInstance463.fieldValue.append(fieldValue466)

fieldValue452.children.append(ProtoInstance463)

ProtoInstance449.fieldValue.append(fieldValue452)

fieldValue397.children.append(ProtoInstance449)
ProtoInstance490 = x3d.ProtoInstance()
ProtoInstance490.name = "Joint"
ProtoInstance490.DEF = "Allen_hanim_vc4"
fieldValue491 = x3d.fieldValue()
fieldValue491.name = "name"
fieldValue491.value = "vc4"

ProtoInstance490.fieldValue.append(fieldValue491)
fieldValue492 = x3d.fieldValue()
fieldValue492.name = "center"
fieldValue492.value = "0 1.43 -0.0458"

ProtoInstance490.fieldValue.append(fieldValue492)
fieldValue493 = x3d.fieldValue()
fieldValue493.name = "children"
ProtoInstance494 = x3d.ProtoInstance()
ProtoInstance494.name = "Segment"
ProtoInstance494.DEF = "Allen_hanim_c4"
fieldValue495 = x3d.fieldValue()
fieldValue495.name = "name"
fieldValue495.value = "c4"

ProtoInstance494.fieldValue.append(fieldValue495)
fieldValue496 = x3d.fieldValue()
fieldValue496.name = "children"
Transform497 = x3d.Transform()
Transform497.DEF = "neck_adjust"
Transform497.center = [-0.36,1.03,0.04]
Transform497.rotation = [0,1,0,1.570796]
Transform497.scale = [0.1,0.1,0.1]
Shape498 = x3d.Shape()
Appearance499 = x3d.Appearance()
Material500 = x3d.Material()
Material500.USE = "Skin_Color"

Appearance499.material = Material500
ImageTexture501 = x3d.ImageTexture()
ImageTexture501.USE = "camo"

Appearance499.texture = ImageTexture501

Shape498.appearance = Appearance499
IndexedFaceSet502 = x3d.IndexedFaceSet()
IndexedFaceSet502.coordIndex = [0,1,2,-1,3,4,5,-1,6,7,8,-1,9,10,11,-1,12,13,14,-1,15,16,17,-1,18,19,20,-1,21,22,23,-1,24,25,26,-1,27,28,29,-1,30,31,32,-1,33,34,35,-1,36,37,38,-1,39,40,41,-1,42,43,44,-1,45,46,47,-1,48,49,50,-1,51,52,53,-1,54,55,56,-1,57,58,59,-1,60,61,62,-1,63,64,65,-1,66,67,68,-1,69,70,71,-1,72,73,74,-1,75,76,77,-1,78,79,80,-1,81,82,83,-1,84,85,86,-1,87,88,89,-1,90,91,92,-1,93,94,95,-1,96,97,98,-1,99,100,101,-1,102,103,104,-1,105,106,107,-1,108,109,110,-1,111,112,113,-1,114,115,116,-1,117,118,119,-1,120,121,122,-1,123,124,125,-1,126,127,128,-1,129,130,131,-1,132,133,134,-1,135,136,137,-1,138,139,140,-1,141,142,143,-1,144,145,146,-1,147,148,149,-1,150,151,152,-1,153,154,155,-1,156,157,158,-1,159,160,161,-1,162,163,164,-1,165,166,167,-1,168,169,170,-1,171,172,173,-1,174,175,176,-1,177,178,179,-1,180,181,182,-1,183,184,185,-1,186,187,188,-1,189,190,191,-1,192,193,194,-1,195,196,197,-1,198,199,200,-1,201,202,203,-1,204,205,206,-1,207,208,209,-1,210,211,212,-1,213,214,215,-1,216,217,218,-1,219,220,221,-1,222,223,224,-1,225,226,227,-1,228,229,230,-1,231,232,233,-1,234,235,236,-1,237,238,239,-1,240,241,242,-1,243,244,245,-1,246,247,248,-1,249,250,251,-1,252,253,254,-1,255,256,257,-1,258,259,260,-1,261,262,263,-1,264,265,266,-1,267,268,269,-1,270,271,272,-1,273,274,275,-1,276,277,278,-1,279,280,281,-1,282,283,284,-1,285,286,287,-1,288,289,290,-1,291,292,293,-1,294,295,296,-1,297,298,299,-1,300,301,302,-1,303,304,305,-1,306,307,308,-1,309,310,311,-1,312,313,314,-1,315,316,317,-1,318,319,320,-1,321,322,323,-1,324,325,326,-1,327,328,329,-1,330,331,332,-1,333,334,335,-1,336,337,338,-1,339,340,341,-1,342,343,344,-1,345,346,347,-1,348,349,350,-1,351,352,353,-1,354,355,356,-1,357,358,359,-1,360,361,362,-1,363,364,365,-1,366,367,368,-1,369,370,371,-1,372,373,374,-1,375,376,377,-1,378,379,380,-1,381,382,383,-1,384,385,386,-1,387,388,389,-1,390,391,392,-1,393,394,395,-1,396,397,398,-1,399,400,401,-1,402,403,404,-1,405,406,407,-1,408,409,410,-1,411,412,413,-1,414,415,416,-1,417,418,419,-1,420,421,422,-1,423,424,425,-1,426,427,428,-1,429,430,431,-1,432,433,434,-1,435,436,437,-1,438,439,440,-1,441,442,443,-1,444,445,446,-1,447,448,449,-1,450,451,452,-1,453,454,455,-1,456,457,458,-1,459,460,461,-1,462,463,464,-1,465,466,467,-1,468,469,470,-1,471,472,473,-1,474,475,476,-1,477,478,479,-1,480,481,482,-1,483,484,485,-1,486,487,488,-1,489,490,491,-1,492,493,494,-1,495,496,497,-1,498,499,500,-1,501,502,503,-1,504,505,506,-1,507,508,509,-1,510,511,512,-1,513,514,515,-1,516,517,518,-1,519,520,521,-1,522,523,524,-1,525,526,527,-1,528,529,530,-1,531,532,533,-1,534,535,536,-1,537,538,539,-1,540,541,542,-1,543,544,545,-1,546,547,548,-1,549,550,551,-1,552,553,554,-1,555,556,557,-1,558,559,560,-1,561,562,563,-1,564,565,566,-1,567,568,569,-1,570,571,572,-1,573,574,575,-1,576,577,578,-1,579,580,581,-1,582,583,584,-1]
IndexedFaceSet502.creaseAngle = 1.91
Coordinate503 = x3d.Coordinate()

IndexedFaceSet502.coord = Coordinate503

Shape498.geometry = IndexedFaceSet502

Transform497.children.append(Shape498)

fieldValue496.children.append(Transform497)

ProtoInstance494.fieldValue.append(fieldValue496)

fieldValue493.children.append(ProtoInstance494)
ProtoInstance504 = x3d.ProtoInstance()
ProtoInstance504.name = "Joint"
ProtoInstance504.DEF = "Allen_hanim_skullbase"
fieldValue505 = x3d.fieldValue()
fieldValue505.name = "name"
fieldValue505.value = "skullbase"

ProtoInstance504.fieldValue.append(fieldValue505)
fieldValue506 = x3d.fieldValue()
fieldValue506.name = "rotation"
fieldValue506.value = "0 1 0 0"

ProtoInstance504.fieldValue.append(fieldValue506)
fieldValue507 = x3d.fieldValue()
fieldValue507.name = "center"
fieldValue507.value = "0 1.4 0"

ProtoInstance504.fieldValue.append(fieldValue507)
fieldValue508 = x3d.fieldValue()
fieldValue508.name = "children"
ProtoInstance509 = x3d.ProtoInstance()
ProtoInstance509.name = "Segment"
ProtoInstance509.DEF = "Allen_hanim_skull"
fieldValue510 = x3d.fieldValue()
fieldValue510.name = "name"
fieldValue510.value = "skull"

ProtoInstance509.fieldValue.append(fieldValue510)
fieldValue511 = x3d.fieldValue()
fieldValue511.name = "children"
Transform512 = x3d.Transform()
Transform512.DEF = "skull_adjust"
Transform512.center = [-0.07,1.33,-0.035]
Transform512.scale = [0.001,0.001,0.001]
Shape513 = x3d.Shape()
Appearance514 = x3d.Appearance()
Material515 = x3d.Material()
Material515.USE = "Skin_Color"

Appearance514.material = Material515
ImageTexture516 = x3d.ImageTexture()
ImageTexture516.DEF = "CLONE"
ImageTexture516.url = ["clone.gif","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/clone.gif"]

Appearance514.texture = ImageTexture516

Shape513.appearance = Appearance514
IndexedFaceSet517 = x3d.IndexedFaceSet()
IndexedFaceSet517.coordIndex = [0,1,2,-1,2,3,0,-1,4,0,3,-1,3,5,4,-1,6,4,5,-1,5,7,6,-1,8,6,7,-1,9,10,11,-1,11,12,9,-1,13,9,12,-1,12,14,13,-1,15,13,14,-1,14,16,15,-1,17,15,16,-1,16,18,17,-1,19,17,18,-1,20,21,1,-1,1,0,20,-1,22,20,0,-1,0,4,22,-1,23,22,4,-1,4,6,23,-1,24,23,6,-1,6,8,24,-1,25,24,8,-1,26,27,28,-1,28,29,26,-1,30,26,29,-1,29,31,30,-1,32,30,31,-1,31,33,32,-1,34,32,33,-1,33,35,34,-1,36,34,35,-1,35,37,36,-1,38,36,37,-1,37,10,38,-1,39,38,10,-1,10,9,39,-1,40,39,9,-1,9,13,40,-1,41,40,13,-1,13,15,41,-1,42,41,15,-1,15,17,42,-1,43,42,17,-1,17,19,43,-1,44,43,19,-1,19,45,44,-1,46,44,45,-1,45,47,46,-1,48,46,47,-1,47,49,48,-1,50,48,49,-1,49,51,50,-1,52,50,51,-1,51,53,52,-1,54,52,53,-1,55,56,21,-1,21,20,55,-1,57,55,20,-1,20,22,57,-1,58,57,22,-1,22,23,58,-1,59,58,23,-1,23,24,59,-1,60,59,24,-1,24,25,60,-1,61,60,25,-1,62,63,64,-1,64,65,62,-1,66,62,65,-1,67,68,69,-1,69,27,67,-1,70,67,27,-1,27,26,70,-1,71,70,26,-1,26,30,71,-1,72,71,30,-1,30,32,72,-1,73,72,32,-1,32,34,73,-1,74,73,34,-1,34,36,74,-1,75,74,36,-1,36,38,75,-1,76,75,38,-1,38,39,76,-1,77,76,39,-1,39,40,77,-1,78,77,40,-1,40,41,78,-1,79,78,41,-1,41,42,79,-1,80,79,42,-1,42,43,80,-1,81,80,43,-1,43,44,81,-1,82,81,44,-1,44,46,82,-1,83,82,46,-1,46,48,83,-1,84,83,48,-1,48,50,84,-1,85,84,50,-1,50,52,85,-1,86,85,52,-1,52,54,86,-1,87,86,54,-1,54,88,87,-1,89,87,88,-1,88,56,89,-1,90,89,56,-1,56,55,90,-1,91,90,55,-1,55,57,91,-1,92,91,57,-1,57,58,92,-1,93,92,58,-1,58,59,93,-1,94,93,59,-1,59,60,94,-1,95,94,60,-1,60,61,95,-1,96,95,61,-1,61,97,96,-1,98,96,97,-1,97,63,98,-1,99,98,63,-1,63,62,99,-1,100,99,62,-1,62,66,100,-1,101,102,68,-1,68,67,101,-1,103,101,67,-1,67,70,103,-1,104,103,70,-1,70,71,104,-1,105,104,71,-1,71,72,105,-1,106,105,72,-1,72,73,106,-1,107,106,73,-1,73,74,107,-1,108,107,74,-1,74,75,108,-1,109,108,75,-1,75,76,109,-1,110,109,76,-1,76,77,110,-1,111,110,77,-1,77,78,111,-1,112,111,78,-1,78,79,112,-1,113,112,79,-1,79,80,113,-1,114,113,80,-1,80,81,114,-1,115,114,81,-1,81,82,115,-1,116,115,82,-1,82,83,116,-1,117,116,83,-1,83,84,117,-1,118,117,84,-1,84,85,118,-1,119,118,85,-1,85,86,119,-1,120,119,86,-1,86,87,120,-1,121,120,87,-1,87,89,121,-1,122,121,89,-1,89,90,122,-1,123,122,90,-1,90,91,123,-1,124,123,91,-1,91,92,124,-1,125,124,92,-1,92,93,125,-1,126,125,93,-1,93,94,126,-1,127,126,94,-1,94,95,127,-1,128,127,95,-1,95,96,128,-1,129,128,96,-1,96,98,129,-1,130,129,98,-1,98,99,130,-1,131,130,99,-1,99,100,131,-1,132,133,102,-1,102,101,132,-1,134,132,101,-1,101,103,134,-1,135,134,103,-1,103,104,135,-1,136,135,104,-1,104,105,136,-1,137,136,105,-1,105,106,137,-1,138,137,106,-1,106,107,138,-1,139,138,107,-1,107,108,139,-1,140,139,108,-1,108,109,140,-1,141,140,109,-1,109,110,141,-1,142,141,110,-1,110,111,142,-1,143,142,111,-1,111,112,143,-1,144,143,112,-1,112,113,144,-1,145,144,113,-1,113,114,145,-1,146,145,114,-1,114,115,146,-1,147,146,115,-1,115,116,147,-1,148,147,116,-1,116,117,148,-1,149,148,117,-1,117,118,149,-1,150,149,118,-1,118,119,150,-1,151,150,119,-1,119,120,151,-1,152,151,120,-1,120,121,152,-1,153,152,121,-1,121,122,153,-1,154,153,122,-1,122,123,154,-1,155,154,123,-1,123,124,155,-1,156,155,124,-1,124,125,156,-1,157,156,125,-1,125,126,157,-1,158,157,126,-1,126,127,158,-1,159,158,127,-1,127,128,159,-1,160,159,128,-1,128,129,160,-1,161,160,129,-1,129,130,161,-1,162,161,130,-1,130,131,162,-1,163,164,165,-1,165,166,163,-1,167,163,166,-1,166,168,167,-1,169,167,168,-1,168,133,169,-1,170,169,133,-1,133,132,170,-1,171,170,132,-1,132,134,171,-1,172,171,134,-1,134,135,172,-1,173,172,135,-1,135,136,173,-1,174,173,136,-1,136,137,174,-1,175,174,137,-1,137,138,175,-1,176,175,138,-1,138,139,176,-1,177,176,139,-1,139,140,177,-1,178,177,140,-1,140,141,178,-1,179,178,141,-1,141,142,179,-1,180,179,142,-1,142,143,180,-1,181,180,143,-1,143,144,181,-1,182,181,144,-1,144,145,182,-1,183,182,145,-1,145,146,183,-1,184,183,146,-1,146,147,184,-1,185,184,147,-1,147,148,185,-1,186,185,148,-1,148,149,186,-1,187,186,149,-1,149,150,187,-1,188,187,150,-1,150,151,188,-1,189,188,151,-1,151,152,189,-1,190,189,152,-1,152,153,190,-1,191,190,153,-1,153,154,191,-1,192,191,154,-1,154,155,192,-1,193,192,155,-1,155,156,193,-1,194,193,156,-1,156,157,194,-1,195,194,157,-1,157,158,195,-1,196,195,158,-1,158,159,196,-1,197,196,159,-1,159,160,197,-1,198,197,160,-1,160,161,198,-1,199,198,161,-1,161,162,199,-1,200,199,162,-1,164,163,201,-1,202,201,163,-1,163,167,202,-1,203,202,167,-1,167,169,203,-1,204,203,169,-1,169,170,204,-1,205,204,170,-1,170,171,205,-1,206,205,171,-1,171,172,206,-1,207,206,172,-1,172,173,207,-1,208,207,173,-1,173,174,208,-1,209,208,174,-1,174,175,209,-1,210,209,175,-1,175,176,210,-1,211,210,176,-1,176,177,211,-1,212,211,177,-1,177,178,212,-1,213,212,178,-1,178,179,213,-1,214,213,179,-1,179,180,214,-1,215,214,180,-1,180,181,215,-1,216,215,181,-1,181,182,216,-1,217,216,182,-1,182,183,217,-1,218,217,183,-1,183,184,218,-1,219,218,184,-1,184,185,219,-1,220,219,185,-1,185,186,220,-1,221,220,186,-1,186,187,221,-1,222,221,187,-1,187,188,222,-1,223,222,188,-1,188,189,223,-1,224,223,189,-1,189,190,224,-1,225,224,190,-1,190,191,225,-1,226,225,191,-1,191,192,226,-1,227,226,192,-1,192,193,227,-1,228,227,193,-1,193,194,228,-1,229,228,194,-1,194,195,229,-1,230,229,195,-1,195,196,230,-1,231,230,196,-1,196,197,231,-1,232,231,197,-1,197,198,232,-1,233,232,198,-1,198,199,233,-1,234,233,199,-1,199,200,234,-1,202,203,235,-1,236,235,203,-1,203,204,236,-1,237,236,204,-1,204,205,237,-1,238,237,205,-1,205,206,238,-1,239,238,206,-1,206,207,239,-1,240,239,207,-1,207,208,240,-1,241,240,208,-1,208,209,241,-1,242,241,209,-1,209,210,242,-1,243,242,210,-1,210,211,243,-1,244,243,211,-1,211,212,244,-1,245,244,212,-1,212,213,245,-1,246,245,213,-1,213,214,246,-1,247,246,214,-1,214,215,247,-1,248,247,215,-1,215,216,248,-1,249,248,216,-1,216,217,249,-1,250,249,217,-1,217,218,250,-1,251,250,218,-1,218,219,251,-1,252,251,219,-1,219,220,252,-1,253,252,220,-1,220,221,253,-1,254,253,221,-1,221,222,254,-1,255,254,222,-1,222,223,255,-1,256,255,223,-1,223,224,256,-1,257,256,224,-1,224,225,257,-1,258,257,225,-1,225,226,258,-1,259,258,226,-1,226,227,259,-1,260,259,227,-1,227,228,260,-1,261,260,228,-1,228,229,261,-1,262,261,229,-1,229,230,262,-1,263,262,230,-1,230,231,263,-1,264,263,231,-1,231,232,264,-1,265,264,232,-1,232,233,265,-1,266,265,233,-1,233,234,266,-1,267,266,234,-1,235,236,268,-1,269,268,236,-1,236,237,269,-1,270,269,237,-1,237,238,270,-1,271,270,238,-1,238,239,271,-1,272,271,239,-1,239,240,272,-1,273,272,240,-1,240,241,273,-1,274,273,241,-1,241,242,274,-1,275,274,242,-1,242,243,275,-1,276,275,243,-1,243,244,276,-1,277,276,244,-1,244,245,277,-1,278,277,245,-1,245,246,278,-1,279,278,246,-1,246,247,279,-1,280,279,247,-1,247,248,280,-1,281,280,248,-1,248,249,281,-1,282,281,249,-1,249,250,282,-1,283,282,250,-1,250,251,283,-1,284,283,251,-1,251,252,284,-1,285,284,252,-1,252,253,285,-1,286,285,253,-1,253,254,286,-1,287,286,254,-1,254,255,287,-1,288,287,255,-1,255,256,288,-1,289,288,256,-1,256,257,289,-1,290,289,257,-1,257,258,290,-1,291,290,258,-1,258,259,291,-1,292,291,259,-1,259,260,292,-1,293,292,260,-1,260,261,293,-1,294,293,261,-1,261,262,294,-1,295,294,262,-1,262,263,295,-1,296,295,263,-1,263,264,296,-1,297,296,264,-1,264,265,297,-1,298,297,265,-1,265,266,298,-1,299,298,266,-1,266,267,299,-1,300,301,268,-1,268,269,300,-1,302,300,269,-1,269,270,302,-1,303,302,270,-1,270,271,303,-1,304,303,271,-1,271,272,304,-1,305,304,272,-1,272,273,305,-1,306,305,273,-1,273,274,306,-1,307,306,274,-1,274,275,307,-1,308,307,275,-1,275,276,308,-1,309,308,276,-1,276,277,309,-1,310,309,277,-1,277,278,310,-1,311,310,278,-1,278,279,311,-1,312,311,279,-1,279,280,312,-1,313,312,280,-1,280,281,313,-1,314,313,281,-1,281,282,314,-1,315,314,282,-1,282,283,315,-1,316,315,283,-1,283,284,316,-1,317,316,284,-1,284,285,317,-1,318,317,285,-1,285,286,318,-1,319,318,286,-1,286,287,319,-1,320,319,287,-1,287,288,320,-1,321,320,288,-1,288,289,321,-1,322,321,289,-1,289,290,322,-1,323,322,290,-1,290,291,323,-1,324,323,291,-1,291,292,324,-1,325,324,292,-1,292,293,325,-1,326,325,293,-1,293,294,326,-1,327,326,294,-1,294,295,327,-1,328,327,295,-1,295,296,328,-1,329,328,296,-1,296,297,329,-1,330,329,297,-1,297,298,330,-1,331,330,298,-1,298,299,331,-1,332,333,301,-1,301,300,332,-1,334,332,300,-1,300,302,334,-1,335,334,302,-1,302,303,335,-1,336,335,303,-1,303,304,336,-1,337,336,304,-1,304,305,337,-1,338,337,305,-1,305,306,338,-1,339,338,306,-1,306,307,339,-1,340,339,307,-1,307,308,340,-1,341,340,308,-1,308,309,341,-1,342,341,309,-1,309,310,342,-1,343,342,310,-1,310,311,343,-1,344,343,311,-1,311,312,344,-1,345,344,312,-1,312,313,345,-1,346,345,313,-1,313,314,346,-1,347,346,314,-1,314,315,347,-1,348,347,315,-1,315,316,348,-1,349,348,316,-1,316,317,349,-1,350,349,317,-1,317,318,350,-1,351,350,318,-1,318,319,351,-1,352,351,319,-1,319,320,352,-1,353,352,320,-1,320,321,353,-1,354,353,321,-1,321,322,354,-1,355,354,322,-1,322,323,355,-1,356,355,323,-1,323,324,356,-1,357,356,324,-1,324,325,357,-1,358,357,325,-1,325,326,358,-1,359,358,326,-1,326,327,359,-1,360,359,327,-1,327,328,360,-1,361,360,328,-1,328,329,361,-1,362,361,329,-1,329,330,362,-1,363,362,330,-1,330,331,363,-1,364,363,331,-1,333,332,365,-1,366,365,332,-1,332,334,366,-1,367,366,334,-1,334,335,367,-1,368,367,335,-1,335,336,368,-1,369,368,336,-1,336,337,369,-1,370,369,337,-1,337,338,370,-1,371,370,338,-1,338,339,371,-1,372,371,339,-1,339,340,372,-1,373,372,340,-1,340,341,373,-1,374,373,341,-1,341,342,374,-1,375,374,342,-1,342,343,375,-1,376,375,343,-1,343,344,376,-1,377,376,344,-1,344,345,377,-1,378,377,345,-1,345,346,378,-1,379,378,346,-1,346,347,379,-1,380,379,347,-1,347,348,380,-1,381,380,348,-1,348,349,381,-1,382,381,349,-1,349,350,382,-1,383,382,350,-1,350,351,383,-1,384,383,351,-1,351,352,384,-1,385,384,352,-1,352,353,385,-1,386,385,353,-1,353,354,386,-1,387,386,354,-1,354,355,387,-1,388,387,355,-1,355,356,388,-1,389,388,356,-1,356,357,389,-1,390,389,357,-1,357,358,390,-1,391,390,358,-1,358,359,391,-1,392,391,359,-1,359,360,392,-1,393,392,360,-1,360,361,393,-1,394,393,361,-1,361,362,394,-1,395,394,362,-1,362,363,395,-1,396,395,363,-1,363,364,396,-1,397,398,365,-1,365,366,397,-1,399,397,366,-1,366,367,399,-1,400,399,367,-1,367,368,400,-1,401,400,368,-1,368,369,401,-1,402,401,369,-1,369,370,402,-1,403,402,370,-1,370,371,403,-1,404,403,371,-1,371,372,404,-1,405,404,372,-1,372,373,405,-1,406,405,373,-1,373,374,406,-1,407,406,374,-1,374,375,407,-1,408,407,375,-1,375,376,408,-1,409,408,376,-1,376,377,409,-1,410,409,377,-1,377,378,410,-1,411,410,378,-1,378,379,411,-1,412,411,379,-1,379,380,412,-1,413,412,380,-1,380,381,413,-1,414,413,381,-1,381,382,414,-1,415,414,382,-1,382,383,415,-1,416,415,383,-1,383,384,416,-1,417,416,384,-1,384,385,417,-1,418,417,385,-1,385,386,418,-1,419,418,386,-1,386,387,419,-1,420,419,387,-1,387,388,420,-1,421,420,388,-1,388,389,421,-1,422,421,389,-1,389,390,422,-1,423,422,390,-1,390,391,423,-1,424,423,391,-1,391,392,424,-1,425,424,392,-1,392,393,425,-1,426,425,393,-1,393,394,426,-1,427,426,394,-1,394,395,427,-1,428,427,395,-1,395,396,428,-1,429,430,398,-1,398,397,429,-1,431,429,397,-1,397,399,431,-1,432,431,399,-1,399,400,432,-1,433,432,400,-1,400,401,433,-1,434,433,401,-1,401,402,434,-1,435,434,402,-1,402,403,435,-1,436,435,403,-1,403,404,436,-1,437,436,404,-1,404,405,437,-1,438,437,405,-1,405,406,438,-1,439,438,406,-1,406,407,439,-1,440,439,407,-1,407,408,440,-1,441,440,408,-1,408,409,441,-1,442,441,409,-1,409,410,442,-1,443,442,410,-1,410,411,443,-1,444,443,411,-1,411,412,444,-1,445,444,412,-1,412,413,445,-1,446,445,413,-1,413,414,446,-1,447,446,414,-1,414,415,447,-1,448,447,415,-1,415,416,448,-1,449,448,416,-1,416,417,449,-1,450,449,417,-1,417,418,450,-1,451,450,418,-1,418,419,451,-1,452,451,419,-1,419,420,452,-1,453,452,420,-1,420,421,453,-1,454,453,421,-1,421,422,454,-1,455,454,422,-1,422,423,455,-1,456,455,423,-1,423,424,456,-1,457,456,424,-1,424,425,457,-1,458,457,425,-1,425,426,458,-1,459,458,426,-1,426,427,459,-1,460,459,427,-1,427,428,460,-1,430,429,461,-1,462,461,429,-1,429,431,462,-1,463,462,431,-1,431,432,463,-1,464,463,432,-1,432,433,464,-1,465,464,433,-1,433,434,465,-1,466,465,434,-1,434,435,466,-1,467,466,435,-1,435,436,467,-1,468,467,436,-1,436,437,468,-1,469,468,437,-1,437,438,469,-1,470,469,438,-1,438,439,470,-1,471,470,439,-1,439,440,471,-1,472,471,440,-1,440,441,472,-1,473,472,441,-1,441,442,473,-1,474,473,442,-1,442,443,474,-1,475,474,443,-1,443,444,475,-1,476,475,444,-1,444,445,476,-1,477,476,445,-1,445,446,477,-1,478,477,446,-1,446,447,478,-1,479,478,447,-1,447,448,479,-1,480,479,448,-1,448,449,480,-1,481,480,449,-1,449,450,481,-1,482,481,450,-1,450,451,482,-1,483,482,451,-1,451,452,483,-1,484,483,452,-1,452,453,484,-1,485,484,453,-1,453,454,485,-1,486,485,454,-1,454,455,486,-1,487,486,455,-1,455,456,487,-1,488,487,456,-1,456,457,488,-1,489,488,457,-1,457,458,489,-1,490,489,458,-1,458,459,490,-1,491,490,459,-1,459,460,491,-1,492,493,461,-1,461,462,492,-1,494,492,462,-1,462,463,494,-1,495,494,463,-1,463,464,495,-1,496,495,464,-1,464,465,496,-1,497,496,465,-1,465,466,497,-1,498,497,466,-1,466,467,498,-1,499,498,467,-1,467,468,499,-1,500,499,468,-1,468,469,500,-1,501,500,469,-1,469,470,501,-1,502,501,470,-1,470,471,502,-1,503,502,471,-1,471,472,503,-1,504,503,472,-1,472,473,504,-1,505,504,473,-1,473,474,505,-1,506,505,474,-1,474,475,506,-1,507,506,475,-1,475,476,507,-1,508,507,476,-1,476,477,508,-1,509,508,477,-1,477,478,509,-1,510,509,478,-1,478,479,510,-1,511,510,479,-1,479,480,511,-1,512,511,480,-1,480,481,512,-1,513,512,481,-1,481,482,513,-1,514,513,482,-1,482,483,514,-1,515,514,483,-1,483,484,515,-1,516,515,484,-1,484,485,516,-1,517,516,485,-1,485,486,517,-1,518,517,486,-1,486,487,518,-1,519,518,487,-1,487,488,519,-1,520,519,488,-1,488,489,520,-1,521,520,489,-1,489,490,521,-1,493,492,522,-1,523,522,492,-1,492,494,523,-1,524,523,494,-1,494,495,524,-1,525,524,495,-1,495,496,525,-1,526,525,496,-1,496,497,526,-1,527,526,497,-1,497,498,527,-1,528,527,498,-1,498,499,528,-1,529,528,499,-1,499,500,529,-1,530,529,500,-1,500,501,530,-1,531,530,501,-1,501,502,531,-1,532,531,502,-1,502,503,532,-1,533,532,503,-1,503,504,533,-1,534,533,504,-1,504,505,534,-1,535,534,505,-1,505,506,535,-1,536,535,506,-1,506,507,536,-1,537,536,507,-1,507,508,537,-1,538,537,508,-1,508,509,538,-1,539,538,509,-1,509,510,539,-1,540,539,510,-1,510,511,540,-1,541,540,511,-1,511,512,541,-1,542,541,512,-1,512,513,542,-1,543,542,513,-1,513,514,543,-1,544,543,514,-1,514,515,544,-1,545,544,515,-1,515,516,545,-1,546,545,516,-1,516,517,546,-1,547,546,517,-1,517,518,547,-1,548,547,518,-1,518,519,548,-1,549,548,519,-1,519,520,549,-1,550,549,520,-1,520,521,550,-1,551,550,521,-1,523,524,552,-1,553,552,524,-1,524,525,553,-1,554,553,525,-1,525,526,554,-1,555,554,526,-1,526,527,555,-1,556,555,527,-1,527,528,556,-1,557,556,528,-1,528,529,557,-1,558,557,529,-1,529,530,558,-1,559,558,530,-1,530,531,559,-1,560,559,531,-1,531,532,560,-1,561,560,532,-1,532,533,561,-1,562,561,533,-1,533,534,562,-1,563,562,534,-1,534,535,563,-1,564,563,535,-1,535,536,564,-1,565,564,536,-1,536,537,565,-1,566,565,537,-1,537,538,566,-1,567,566,538,-1,538,539,567,-1,568,567,539,-1,539,540,568,-1,569,568,540,-1,540,541,569,-1,570,569,541,-1,541,542,570,-1,571,570,542,-1,542,543,571,-1,572,571,543,-1,543,544,572,-1,573,572,544,-1,544,545,573,-1,574,573,545,-1,545,546,574,-1,575,574,546,-1,546,547,575,-1,576,575,547,-1,547,548,576,-1,577,576,548,-1,548,549,577,-1,578,577,549,-1,549,550,578,-1,579,578,550,-1,550,551,579,-1,580,581,552,-1,552,553,580,-1,582,580,553,-1,553,554,582,-1,583,582,554,-1,554,555,583,-1,584,583,555,-1,555,556,584,-1,585,584,556,-1,556,557,585,-1,586,585,557,-1,557,558,586,-1,587,586,558,-1,558,559,587,-1,588,587,559,-1,559,560,588,-1,589,588,560,-1,560,561,589,-1,590,589,561,-1,561,562,590,-1,591,590,562,-1,562,563,591,-1,592,591,563,-1,563,564,592,-1,593,592,564,-1,564,565,593,-1,594,593,565,-1,565,566,594,-1,595,594,566,-1,566,567,595,-1,596,595,567,-1,567,568,596,-1,597,596,568,-1,568,569,597,-1,598,597,569,-1,569,570,598,-1,599,598,570,-1,570,571,599,-1,600,599,571,-1,571,572,600,-1,601,600,572,-1,572,573,601,-1,602,601,573,-1,573,574,602,-1,603,602,574,-1,574,575,603,-1,604,603,575,-1,575,576,604,-1,605,604,576,-1,576,577,605,-1,606,605,577,-1,577,578,606,-1,607,608,581,-1,581,580,607,-1,609,607,580,-1,580,582,609,-1,610,609,582,-1,582,583,610,-1,611,610,583,-1,583,584,611,-1,612,611,584,-1,584,585,612,-1,613,612,585,-1,585,586,613,-1,614,613,586,-1,586,587,614,-1,615,614,587,-1,587,588,615,-1,616,615,588,-1,588,589,616,-1,617,616,589,-1,589,590,617,-1,618,617,590,-1,590,591,618,-1,619,618,591,-1,591,592,619,-1,620,619,592,-1,592,593,620,-1,621,620,593,-1,593,594,621,-1,622,621,594,-1,594,595,622,-1,623,622,595,-1,595,596,623,-1,624,623,596,-1,596,597,624,-1,625,624,597,-1,597,598,625,-1,626,625,598,-1,598,599,626,-1,627,626,599,-1,599,600,627,-1,628,627,600,-1,600,601,628,-1,629,628,601,-1,601,602,629,-1,630,629,602,-1,602,603,630,-1,631,630,603,-1,603,604,631,-1,632,631,604,-1,604,605,632,-1,633,632,605,-1,605,606,633,-1,634,635,608,-1,608,607,634,-1,636,634,607,-1,607,609,636,-1,637,636,609,-1,609,610,637,-1,638,637,610,-1,610,611,638,-1,639,638,611,-1,611,612,639,-1,640,639,612,-1,612,613,640,-1,641,640,613,-1,613,614,641,-1,642,641,614,-1,614,615,642,-1,643,642,615,-1,615,616,643,-1,644,643,616,-1,616,617,644,-1,645,644,617,-1,617,618,645,-1,646,645,618,-1,618,619,646,-1,647,646,619,-1,619,620,647,-1,648,647,620,-1,620,621,648,-1,649,648,621,-1,621,622,649,-1,650,649,622,-1,622,623,650,-1,651,650,623,-1,623,624,651,-1,652,651,624,-1,624,625,652,-1,653,652,625,-1,625,626,653,-1,654,653,626,-1,626,627,654,-1,655,654,627,-1,627,628,655,-1,656,655,628,-1,628,629,656,-1,657,656,629,-1,629,630,657,-1,658,657,630,-1,630,631,658,-1,659,658,631,-1,631,632,659,-1,660,659,632,-1,632,633,660,-1,661,660,633,-1,662,663,664,-1,664,665,662,-1,666,662,665,-1,665,635,666,-1,667,666,635,-1,635,634,667,-1,668,667,634,-1,634,636,668,-1,669,668,636,-1,636,637,669,-1,670,669,637,-1,637,638,670,-1,671,670,638,-1,638,639,671,-1,672,671,639,-1,639,640,672,-1,673,672,640,-1,640,641,673,-1,674,673,641,-1,641,642,674,-1,675,674,642,-1,642,643,675,-1,676,675,643,-1,643,644,676,-1,677,676,644,-1,644,645,677,-1,678,677,645,-1,645,646,678,-1,679,678,646,-1,646,647,679,-1,680,679,647,-1,647,648,680,-1,681,680,648,-1,648,649,681,-1,682,681,649,-1,649,650,682,-1,683,682,650,-1,650,651,683,-1,684,683,651,-1,651,652,684,-1,685,684,652,-1,652,653,685,-1,686,685,653,-1,653,654,686,-1,687,686,654,-1,654,655,687,-1,688,687,655,-1,655,656,688,-1,689,688,656,-1,656,657,689,-1,690,689,657,-1,657,658,690,-1,691,690,658,-1,658,659,691,-1,692,691,659,-1,659,660,692,-1,693,692,660,-1,660,661,693,-1,694,693,661,-1,695,696,663,-1,663,662,695,-1,697,695,662,-1,662,666,697,-1,698,697,666,-1,666,667,698,-1,699,698,667,-1,667,668,699,-1,700,699,668,-1,668,669,700,-1,701,700,669,-1,669,670,701,-1,702,701,670,-1,670,671,702,-1,703,702,671,-1,671,672,703,-1,704,703,672,-1,672,673,704,-1,705,704,673,-1,673,674,705,-1,706,705,674,-1,674,675,706,-1,707,706,675,-1,675,676,707,-1,708,707,676,-1,676,677,708,-1,709,708,677,-1,677,678,709,-1,710,709,678,-1,678,679,710,-1,711,710,679,-1,679,680,711,-1,712,711,680,-1,680,681,712,-1,713,712,681,-1,681,682,713,-1,714,713,682,-1,682,683,714,-1,715,714,683,-1,683,684,715,-1,716,715,684,-1,684,685,716,-1,717,716,685,-1,685,686,717,-1,718,717,686,-1,686,687,718,-1,719,718,687,-1,687,688,719,-1,720,719,688,-1,688,689,720,-1,721,720,689,-1,689,690,721,-1,722,721,690,-1,690,691,722,-1,723,722,691,-1,691,692,723,-1,724,723,692,-1,692,693,724,-1,725,724,693,-1,693,694,725,-1,726,725,694,-1,727,728,696,-1,696,695,727,-1,729,727,695,-1,695,697,729,-1,730,729,697,-1,697,698,730,-1,731,730,698,-1,698,699,731,-1,732,731,699,-1,699,700,732,-1,733,732,700,-1,700,701,733,-1,734,733,701,-1,701,702,734,-1,735,734,702,-1,702,703,735,-1,736,735,703,-1,703,704,736,-1,737,736,704,-1,704,705,737,-1,738,737,705,-1,705,706,738,-1,739,738,706,-1,706,707,739,-1,740,739,707,-1,707,708,740,-1,741,740,708,-1,708,709,741,-1,742,741,709,-1,709,710,742,-1,743,742,710,-1,710,711,743,-1,744,743,711,-1,711,712,744,-1,745,744,712,-1,712,713,745,-1,746,745,713,-1,713,714,746,-1,747,746,714,-1,714,715,747,-1,748,747,715,-1,715,716,748,-1,749,748,716,-1,716,717,749,-1,750,749,717,-1,717,718,750,-1,751,750,718,-1,718,719,751,-1,752,751,719,-1,719,720,752,-1,753,752,720,-1,720,721,753,-1,754,753,721,-1,721,722,754,-1,755,754,722,-1,722,723,755,-1,756,755,723,-1,723,724,756,-1,757,756,724,-1,724,725,757,-1,758,757,725,-1,725,726,758,-1,759,758,726,-1,728,727,760,-1,761,760,727,-1,727,729,761,-1,762,761,729,-1,729,730,762,-1,763,762,730,-1,730,731,763,-1,764,763,731,-1,731,732,764,-1,765,764,732,-1,732,733,765,-1,766,765,733,-1,733,734,766,-1,767,766,734,-1,734,735,767,-1,768,767,735,-1,735,736,768,-1,769,768,736,-1,736,737,769,-1,770,769,737,-1,737,738,770,-1,771,770,738,-1,738,739,771,-1,772,771,739,-1,739,740,772,-1,773,772,740,-1,740,741,773,-1,774,773,741,-1,741,742,774,-1,775,774,742,-1,742,743,775,-1,776,775,743,-1,743,744,776,-1,777,776,744,-1,744,745,777,-1,778,777,745,-1,745,746,778,-1,779,778,746,-1,746,747,779,-1,780,779,747,-1,747,748,780,-1,781,780,748,-1,748,749,781,-1,782,781,749,-1,749,750,782,-1,783,782,750,-1,750,751,783,-1,784,783,751,-1,751,752,784,-1,785,784,752,-1,752,753,785,-1,786,785,753,-1,753,754,786,-1,787,786,754,-1,754,755,787,-1,788,787,755,-1,755,756,788,-1,789,788,756,-1,756,757,789,-1,790,789,757,-1,757,758,790,-1,791,790,758,-1,758,759,791,-1,792,791,759,-1,793,794,760,-1,760,761,793,-1,795,793,761,-1,761,762,795,-1,796,795,762,-1,762,763,796,-1,797,796,763,-1,763,764,797,-1,798,797,764,-1,764,765,798,-1,799,798,765,-1,765,766,799,-1,800,799,766,-1,766,767,800,-1,801,800,767,-1,767,768,801,-1,802,801,768,-1,768,769,802,-1,803,802,769,-1,769,770,803,-1,804,803,770,-1,770,771,804,-1,805,804,771,-1,771,772,805,-1,806,805,772,-1,772,773,806,-1,807,806,773,-1,773,774,807,-1,808,807,774,-1,774,775,808,-1,809,808,775,-1,775,776,809,-1,810,809,776,-1,776,777,810,-1,811,810,777,-1,777,778,811,-1,812,811,778,-1,778,779,812,-1,813,812,779,-1,779,780,813,-1,814,813,780,-1,780,781,814,-1,815,814,781,-1,781,782,815,-1,816,815,782,-1,782,783,816,-1,817,816,783,-1,783,784,817,-1,818,817,784,-1,784,785,818,-1,819,818,785,-1,785,786,819,-1,820,819,786,-1,786,787,820,-1,821,820,787,-1,787,788,821,-1,822,821,788,-1,788,789,822,-1,823,822,789,-1,789,790,823,-1,824,823,790,-1,790,791,824,-1,825,824,791,-1,791,792,825,-1,826,825,792,-1,827,828,829,-1,829,794,827,-1,830,827,794,-1,794,793,830,-1,831,830,793,-1,793,795,831,-1,832,831,795,-1,795,796,832,-1,833,832,796,-1,796,797,833,-1,834,833,797,-1,797,798,834,-1,835,834,798,-1,798,799,835,-1,836,835,799,-1,799,800,836,-1,837,836,800,-1,800,801,837,-1,838,837,801,-1,801,802,838,-1,839,838,802,-1,802,803,839,-1,840,839,803,-1,803,804,840,-1,841,840,804,-1,804,805,841,-1,842,841,805,-1,805,806,842,-1,843,842,806,-1,806,807,843,-1,844,843,807,-1,807,808,844,-1,845,844,808,-1,808,809,845,-1,846,845,809,-1,809,810,846,-1,847,846,810,-1,810,811,847,-1,848,847,811,-1,811,812,848,-1,849,848,812,-1,812,813,849,-1,850,849,813,-1,813,814,850,-1,851,850,814,-1,814,815,851,-1,852,851,815,-1,815,816,852,-1,853,852,816,-1,816,817,853,-1,854,853,817,-1,817,818,854,-1,855,854,818,-1,818,819,855,-1,856,855,819,-1,819,820,856,-1,857,856,820,-1,820,821,857,-1,858,857,821,-1,821,822,858,-1,859,858,822,-1,822,823,859,-1,860,859,823,-1,823,824,860,-1,861,860,824,-1,824,825,861,-1,862,861,825,-1,825,826,862,-1,863,862,826,-1,864,865,828,-1,828,827,864,-1,866,864,827,-1,827,830,866,-1,867,866,830,-1,830,831,867,-1,868,867,831,-1,831,832,868,-1,869,868,832,-1,832,833,869,-1,870,869,833,-1,833,834,870,-1,871,870,834,-1,834,835,871,-1,872,871,835,-1,835,836,872,-1,873,872,836,-1,836,837,873,-1,874,873,837,-1,837,838,874,-1,875,874,838,-1,838,839,875,-1,876,875,839,-1,839,840,876,-1,877,876,840,-1,840,841,877,-1,878,877,841,-1,841,842,878,-1,879,878,842,-1,842,843,879,-1,880,879,843,-1,843,844,880,-1,881,880,844,-1,844,845,881,-1,882,881,845,-1,845,846,882,-1,883,882,846,-1,846,847,883,-1,884,883,847,-1,847,848,884,-1,885,884,848,-1,848,849,885,-1,886,885,849,-1,849,850,886,-1,887,886,850,-1,850,851,887,-1,888,887,851,-1,851,852,888,-1,889,888,852,-1,852,853,889,-1,890,889,853,-1,853,854,890,-1,891,890,854,-1,854,855,891,-1,892,891,855,-1,855,856,892,-1,893,892,856,-1,856,857,893,-1,894,893,857,-1,857,858,894,-1,895,894,858,-1,858,859,895,-1,896,895,859,-1,859,860,896,-1,897,896,860,-1,860,861,897,-1,898,897,861,-1,861,862,898,-1,899,898,862,-1,862,863,899,-1,900,899,863,-1,901,902,865,-1,865,864,901,-1,903,901,864,-1,864,866,903,-1,904,903,866,-1,866,867,904,-1,905,904,867,-1,867,868,905,-1,906,905,868,-1,868,869,906,-1,907,906,869,-1,869,870,907,-1,908,907,870,-1,870,871,908,-1,909,908,871,-1,871,872,909,-1,910,909,872,-1,872,873,910,-1,911,910,873,-1,873,874,911,-1,912,911,874,-1,874,875,912,-1,913,912,875,-1,875,876,913,-1,914,913,876,-1,876,877,914,-1,915,914,877,-1,877,878,915,-1,916,915,878,-1,878,879,916,-1,917,916,879,-1,879,880,917,-1,918,917,880,-1,880,881,918,-1,919,918,881,-1,881,882,919,-1,920,919,882,-1,882,883,920,-1,921,920,883,-1,883,884,921,-1,922,921,884,-1,884,885,922,-1,923,922,885,-1,885,886,923,-1,924,923,886,-1,886,887,924,-1,925,924,887,-1,887,888,925,-1,926,925,888,-1,888,889,926,-1,927,926,889,-1,889,890,927,-1,928,927,890,-1,890,891,928,-1,929,928,891,-1,891,892,929,-1,930,929,892,-1,892,893,930,-1,931,930,893,-1,893,894,931,-1,932,931,894,-1,894,895,932,-1,933,932,895,-1,895,896,933,-1,934,933,896,-1,896,897,934,-1,935,934,897,-1,897,898,935,-1,936,935,898,-1,898,899,936,-1,937,936,899,-1,899,900,937,-1,938,937,900,-1,939,940,941,-1,941,902,939,-1,942,939,902,-1,902,901,942,-1,943,942,901,-1,901,903,943,-1,944,943,903,-1,903,904,944,-1,945,944,904,-1,904,905,945,-1,946,945,905,-1,905,906,946,-1,947,946,906,-1,906,907,947,-1,948,947,907,-1,907,908,948,-1,949,948,908,-1,908,909,949,-1,950,949,909,-1,909,910,950,-1,951,950,910,-1,910,911,951,-1,952,951,911,-1,911,912,952,-1,953,952,912,-1,912,913,953,-1,954,953,913,-1,913,914,954,-1,955,954,914,-1,914,915,955,-1,956,955,915,-1,915,916,956,-1,957,956,916,-1,916,917,957,-1,958,957,917,-1,917,918,958,-1,959,958,918,-1,918,919,959,-1,960,959,919,-1,919,920,960,-1,961,960,920,-1,920,921,961,-1,962,961,921,-1,921,922,962,-1,963,962,922,-1,922,923,963,-1,964,963,923,-1,923,924,964,-1,965,964,924,-1,924,925,965,-1,966,965,925,-1,925,926,966,-1,967,966,926,-1,926,927,967,-1,968,967,927,-1,927,928,968,-1,969,968,928,-1,928,929,969,-1,970,969,929,-1,929,930,970,-1,971,970,930,-1,930,931,971,-1,972,971,931,-1,931,932,972,-1,973,972,932,-1,932,933,973,-1,974,973,933,-1,933,934,974,-1,975,974,934,-1,934,935,975,-1,976,975,935,-1,935,936,976,-1,977,976,936,-1,936,937,977,-1,978,977,937,-1,937,938,978,-1,940,939,979,-1,980,979,939,-1,939,942,980,-1,981,980,942,-1,942,943,981,-1,982,981,943,-1,943,944,982,-1,983,982,944,-1,944,945,983,-1,984,983,945,-1,945,946,984,-1,985,984,946,-1,946,947,985,-1,986,985,947,-1,947,948,986,-1,987,986,948,-1,948,949,987,-1,988,987,949,-1,949,950,988,-1,989,988,950,-1,950,951,989,-1,990,989,951,-1,951,952,990,-1,991,990,952,-1,952,953,991,-1,992,991,953,-1,953,954,992,-1,993,992,954,-1,954,955,993,-1,994,993,955,-1,955,956,994,-1,995,994,956,-1,956,957,995,-1,996,995,957,-1,957,958,996,-1,997,996,958,-1,958,959,997,-1,998,997,959,-1,959,960,998,-1,999,998,960,-1,960,961,999,-1,1000,999,961,-1,961,962,1000,-1,1001,1000,962,-1,962,963,1001,-1,1002,1001,963,-1,963,964,1002,-1,1003,1002,964,-1,964,965,1003,-1,1004,1003,965,-1,965,966,1004,-1,1005,1004,966,-1,966,967,1005,-1,1006,1005,967,-1,967,968,1006,-1,1007,1006,968,-1,968,969,1007,-1,1008,1007,969,-1,969,970,1008,-1,1009,1008,970,-1,970,971,1009,-1,1010,1009,971,-1,971,972,1010,-1,1011,1010,972,-1,972,973,1011,-1,1012,1011,973,-1,973,974,1012,-1,1013,1012,974,-1,974,975,1013,-1,1014,1013,975,-1,975,976,1014,-1,1015,1014,976,-1,976,977,1015,-1,1016,1015,977,-1,977,978,1016,-1,1017,1016,978,-1,1018,1019,979,-1,979,980,1018,-1,1020,1018,980,-1,980,981,1020,-1,1021,1020,981,-1,981,982,1021,-1,1022,1021,982,-1,982,983,1022,-1,1023,1022,983,-1,983,984,1023,-1,1024,1023,984,-1,984,985,1024,-1,1025,1024,985,-1,985,986,1025,-1,1026,1025,986,-1,986,987,1026,-1,1027,1026,987,-1,987,988,1027,-1,1028,1027,988,-1,988,989,1028,-1,1029,1028,989,-1,989,990,1029,-1,1030,1029,990,-1,990,991,1030,-1,1031,1030,991,-1,991,992,1031,-1,1032,1031,992,-1,992,993,1032,-1,1033,1032,993,-1,993,994,1033,-1,1034,1033,994,-1,994,995,1034,-1,1035,1034,995,-1,995,996,1035,-1,1036,1035,996,-1,996,997,1036,-1,1037,1036,997,-1,997,998,1037,-1,1038,1037,998,-1,998,999,1038,-1,1039,1038,999,-1,999,1000,1039,-1,1040,1039,1000,-1,1000,1001,1040,-1,1041,1040,1001,-1,1001,1002,1041,-1,1042,1041,1002,-1,1002,1003,1042,-1,1043,1042,1003,-1,1003,1004,1043,-1,1044,1043,1004,-1,1004,1005,1044,-1,1045,1044,1005,-1,1005,1006,1045,-1,1046,1045,1006,-1,1006,1007,1046,-1,1047,1046,1007,-1,1007,1008,1047,-1,1048,1047,1008,-1,1008,1009,1048,-1,1049,1048,1009,-1,1009,1010,1049,-1,1050,1049,1010,-1,1010,1011,1050,-1,1051,1050,1011,-1,1011,1012,1051,-1,1052,1051,1012,-1,1012,1013,1052,-1,1053,1052,1013,-1,1013,1014,1053,-1,1054,1053,1014,-1,1014,1015,1054,-1,1055,1054,1015,-1,1015,1016,1055,-1,1056,1055,1016,-1,1016,1017,1056,-1,1057,1056,1017,-1,1058,1059,1019,-1,1019,1018,1058,-1,1060,1058,1018,-1,1018,1020,1060,-1,1061,1060,1020,-1,1020,1021,1061,-1,1062,1061,1021,-1,1021,1022,1062,-1,1063,1062,1022,-1,1022,1023,1063,-1,1064,1063,1023,-1,1023,1024,1064,-1,1065,1064,1024,-1,1024,1025,1065,-1,1066,1065,1025,-1,1025,1026,1066,-1,1067,1066,1026,-1,1026,1027,1067,-1,1068,1067,1027,-1,1027,1028,1068,-1,1069,1068,1028,-1,1028,1029,1069,-1,1070,1069,1029,-1,1029,1030,1070,-1,1071,1070,1030,-1,1030,1031,1071,-1,1072,1071,1031,-1,1031,1032,1072,-1,1073,1072,1032,-1,1032,1033,1073,-1,1074,1073,1033,-1,1033,1034,1074,-1,1075,1074,1034,-1,1034,1035,1075,-1,1076,1075,1035,-1,1035,1036,1076,-1,1077,1076,1036,-1,1036,1037,1077,-1,1078,1077,1037,-1,1037,1038,1078,-1,1079,1078,1038,-1,1038,1039,1079,-1,1080,1079,1039,-1,1039,1040,1080,-1,1081,1080,1040,-1,1040,1041,1081,-1,1082,1081,1041,-1,1041,1042,1082,-1,1083,1082,1042,-1,1042,1043,1083,-1,1084,1083,1043,-1,1043,1044,1084,-1,1085,1084,1044,-1,1044,1045,1085,-1,1086,1085,1045,-1,1045,1046,1086,-1,1087,1086,1046,-1,1046,1047,1087,-1,1088,1087,1047,-1,1047,1048,1088,-1,1089,1088,1048,-1,1048,1049,1089,-1,1090,1089,1049,-1,1049,1050,1090,-1,1091,1090,1050,-1,1050,1051,1091,-1,1092,1091,1051,-1,1051,1052,1092,-1,1093,1092,1052,-1,1052,1053,1093,-1,1094,1093,1053,-1,1053,1054,1094,-1,1095,1094,1054,-1,1054,1055,1095,-1,1096,1095,1055,-1,1055,1056,1096,-1,1097,1096,1056,-1,1056,1057,1097,-1,1098,1097,1057,-1,1059,1058,1099,-1,1100,1099,1058,-1,1058,1060,1100,-1,1101,1100,1060,-1,1060,1061,1101,-1,1102,1101,1061,-1,1061,1062,1102,-1,1103,1102,1062,-1,1062,1063,1103,-1,1104,1103,1063,-1,1063,1064,1104,-1,1105,1104,1064,-1,1064,1065,1105,-1,1106,1105,1065,-1,1065,1066,1106,-1,1107,1106,1066,-1,1066,1067,1107,-1,1108,1107,1067,-1,1067,1068,1108,-1,1109,1108,1068,-1,1068,1069,1109,-1,1110,1109,1069,-1,1069,1070,1110,-1,1111,1110,1070,-1,1070,1071,1111,-1,1112,1111,1071,-1,1071,1072,1112,-1,1113,1112,1072,-1,1072,1073,1113,-1,1114,1113,1073,-1,1073,1074,1114,-1,1115,1114,1074,-1,1074,1075,1115,-1,1116,1115,1075,-1,1075,1076,1116,-1,1117,1116,1076,-1,1076,1077,1117,-1,1118,1117,1077,-1,1077,1078,1118,-1,1119,1118,1078,-1,1078,1079,1119,-1,1120,1119,1079,-1,1079,1080,1120,-1,1121,1120,1080,-1,1080,1081,1121,-1,1122,1121,1081,-1,1081,1082,1122,-1,1123,1122,1082,-1,1082,1083,1123,-1,1124,1123,1083,-1,1083,1084,1124,-1,1125,1124,1084,-1,1084,1085,1125,-1,1126,1125,1085,-1,1085,1086,1126,-1,1127,1126,1086,-1,1086,1087,1127,-1,1128,1127,1087,-1,1087,1088,1128,-1,1129,1128,1088,-1,1088,1089,1129,-1,1130,1129,1089,-1,1089,1090,1130,-1,1131,1130,1090,-1,1090,1091,1131,-1,1132,1131,1091,-1,1091,1092,1132,-1,1133,1132,1092,-1,1092,1093,1133,-1,1134,1133,1093,-1,1093,1094,1134,-1,1135,1134,1094,-1,1094,1095,1135,-1,1136,1135,1095,-1,1095,1096,1136,-1,1137,1136,1096,-1,1096,1097,1137,-1,1138,1137,1097,-1,1097,1098,1138,-1,1139,1138,1098,-1,1140,1141,1099,-1,1099,1100,1140,-1,1142,1140,1100,-1,1100,1101,1142,-1,1143,1142,1101,-1,1101,1102,1143,-1,1144,1143,1102,-1,1102,1103,1144,-1,1145,1144,1103,-1,1103,1104,1145,-1,1146,1145,1104,-1,1104,1105,1146,-1,1147,1146,1105,-1,1105,1106,1147,-1,1148,1147,1106,-1,1106,1107,1148,-1,1149,1148,1107,-1,1107,1108,1149,-1,1150,1149,1108,-1,1108,1109,1150,-1,1151,1150,1109,-1,1109,1110,1151,-1,1152,1151,1110,-1,1110,1111,1152,-1,1153,1152,1111,-1,1111,1112,1153,-1,1154,1153,1112,-1,1112,1113,1154,-1,1155,1154,1113,-1,1113,1114,1155,-1,1156,1155,1114,-1,1114,1115,1156,-1,1157,1156,1115,-1,1115,1116,1157,-1,1158,1157,1116,-1,1116,1117,1158,-1,1159,1158,1117,-1,1117,1118,1159,-1,1160,1159,1118,-1,1118,1119,1160,-1,1161,1160,1119,-1,1119,1120,1161,-1,1162,1161,1120,-1,1120,1121,1162,-1,1163,1162,1121,-1,1121,1122,1163,-1,1164,1163,1122,-1,1122,1123,1164,-1,1165,1164,1123,-1,1123,1124,1165,-1,1166,1165,1124,-1,1124,1125,1166,-1,1167,1166,1125,-1,1125,1126,1167,-1,1168,1167,1126,-1,1126,1127,1168,-1,1169,1168,1127,-1,1127,1128,1169,-1,1170,1169,1128,-1,1128,1129,1170,-1,1171,1170,1129,-1,1129,1130,1171,-1,1172,1171,1130,-1,1130,1131,1172,-1,1173,1172,1131,-1,1131,1132,1173,-1,1174,1173,1132,-1,1132,1133,1174,-1,1175,1174,1133,-1,1133,1134,1175,-1,1176,1175,1134,-1,1134,1135,1176,-1,1177,1176,1135,-1,1135,1136,1177,-1,1178,1177,1136,-1,1136,1137,1178,-1,1179,1178,1137,-1,1137,1138,1179,-1,1180,1179,1138,-1,1138,1139,1180,-1,1141,1140,1181,-1,1182,1181,1140,-1,1140,1142,1182,-1,1183,1182,1142,-1,1142,1143,1183,-1,1184,1183,1143,-1,1143,1144,1184,-1,1185,1184,1144,-1,1144,1145,1185,-1,1186,1185,1145,-1,1145,1146,1186,-1,1187,1186,1146,-1,1146,1147,1187,-1,1188,1187,1147,-1,1147,1148,1188,-1,1189,1188,1148,-1,1148,1149,1189,-1,1190,1189,1149,-1,1149,1150,1190,-1,1191,1190,1150,-1,1150,1151,1191,-1,1192,1191,1151,-1,1151,1152,1192,-1,1193,1192,1152,-1,1152,1153,1193,-1,1194,1193,1153,-1,1153,1154,1194,-1,1195,1194,1154,-1,1154,1155,1195,-1,1196,1195,1155,-1,1155,1156,1196,-1,1197,1196,1156,-1,1156,1157,1197,-1,1198,1197,1157,-1,1157,1158,1198,-1,1199,1198,1158,-1,1158,1159,1199,-1,1200,1199,1159,-1,1159,1160,1200,-1,1201,1200,1160,-1,1160,1161,1201,-1,1202,1201,1161,-1,1161,1162,1202,-1,1203,1202,1162,-1,1162,1163,1203,-1,1204,1203,1163,-1,1163,1164,1204,-1,1205,1204,1164,-1,1164,1165,1205,-1,1206,1205,1165,-1,1165,1166,1206,-1,1207,1206,1166,-1,1166,1167,1207,-1,1208,1207,1167,-1,1167,1168,1208,-1,1209,1208,1168,-1,1168,1169,1209,-1,1210,1209,1169,-1,1169,1170,1210,-1,1211,1210,1170,-1,1170,1171,1211,-1,1212,1211,1171,-1,1171,1172,1212,-1,1213,1212,1172,-1,1172,1173,1213,-1,1214,1213,1173,-1,1173,1174,1214,-1,1215,1214,1174,-1,1174,1175,1215,-1,1216,1215,1175,-1,1175,1176,1216,-1,1217,1216,1176,-1,1176,1177,1217,-1,1218,1217,1177,-1,1177,1178,1218,-1,1219,1218,1178,-1,1178,1179,1219,-1,1220,1221,1181,-1,1181,1182,1220,-1,1222,1220,1182,-1,1182,1183,1222,-1,1223,1222,1183,-1,1183,1184,1223,-1,1224,1223,1184,-1,1184,1185,1224,-1,1225,1224,1185,-1,1185,1186,1225,-1,1226,1225,1186,-1,1186,1187,1226,-1,1227,1226,1187,-1,1187,1188,1227,-1,1228,1227,1188,-1,1188,1189,1228,-1,1229,1228,1189,-1,1189,1190,1229,-1,1230,1229,1190,-1,1190,1191,1230,-1,1231,1230,1191,-1,1191,1192,1231,-1,1232,1231,1192,-1,1192,1193,1232,-1,1233,1232,1193,-1,1193,1194,1233,-1,1234,1233,1194,-1,1194,1195,1234,-1,1235,1234,1195,-1,1195,1196,1235,-1,1236,1235,1196,-1,1196,1197,1236,-1,1237,1236,1197,-1,1197,1198,1237,-1,1238,1237,1198,-1,1198,1199,1238,-1,1239,1238,1199,-1,1199,1200,1239,-1,1240,1239,1200,-1,1200,1201,1240,-1,1241,1240,1201,-1,1201,1202,1241,-1,1242,1241,1202,-1,1202,1203,1242,-1,1243,1242,1203,-1,1203,1204,1243,-1,1244,1243,1204,-1,1204,1205,1244,-1,1245,1244,1205,-1,1205,1206,1245,-1,1246,1245,1206,-1,1206,1207,1246,-1,1247,1246,1207,-1,1207,1208,1247,-1,1248,1247,1208,-1,1208,1209,1248,-1,1249,1248,1209,-1,1209,1210,1249,-1,1250,1249,1210,-1,1210,1211,1250,-1,1251,1250,1211,-1,1211,1212,1251,-1,1252,1251,1212,-1,1212,1213,1252,-1,1253,1252,1213,-1,1213,1214,1253,-1,1254,1253,1214,-1,1214,1215,1254,-1,1255,1254,1215,-1,1215,1216,1255,-1,1256,1255,1216,-1,1216,1217,1256,-1,1257,1256,1217,-1,1217,1218,1257,-1,1221,1220,1258,-1,1259,1258,1220,-1,1220,1222,1259,-1,1260,1259,1222,-1,1222,1223,1260,-1,1261,1260,1223,-1,1223,1224,1261,-1,1262,1261,1224,-1,1224,1225,1262,-1,1263,1262,1225,-1,1225,1226,1263,-1,1264,1263,1226,-1,1226,1227,1264,-1,1265,1264,1227,-1,1227,1228,1265,-1,1266,1265,1228,-1,1228,1229,1266,-1,1267,1266,1229,-1,1229,1230,1267,-1,1268,1267,1230,-1,1230,1231,1268,-1,1269,1268,1231,-1,1231,1232,1269,-1,1270,1269,1232,-1,1232,1233,1270,-1,1271,1270,1233,-1,1233,1234,1271,-1,1272,1271,1234,-1,1234,1235,1272,-1,1273,1272,1235,-1,1235,1236,1273,-1,1274,1273,1236,-1,1236,1237,1274,-1,1275,1274,1237,-1,1237,1238,1275,-1,1276,1275,1238,-1,1238,1239,1276,-1,1277,1276,1239,-1,1239,1240,1277,-1,1278,1277,1240,-1,1240,1241,1278,-1,1279,1278,1241,-1,1241,1242,1279,-1,1280,1279,1242,-1,1242,1243,1280,-1,1281,1280,1243,-1,1243,1244,1281,-1,1282,1281,1244,-1,1244,1245,1282,-1,1283,1282,1245,-1,1245,1246,1283,-1,1284,1283,1246,-1,1246,1247,1284,-1,1285,1284,1247,-1,1247,1248,1285,-1,1286,1285,1248,-1,1248,1249,1286,-1,1287,1286,1249,-1,1249,1250,1287,-1,1288,1287,1250,-1,1250,1251,1288,-1,1289,1288,1251,-1,1251,1252,1289,-1,1290,1289,1252,-1,1252,1253,1290,-1,1291,1290,1253,-1,1253,1254,1291,-1,1292,1291,1254,-1,1254,1255,1292,-1,1293,1292,1255,-1,1255,1256,1293,-1,1294,1293,1256,-1,1256,1257,1294,-1,1295,1294,1257,-1,1296,1297,1258,-1,1258,1259,1296,-1,1298,1296,1259,-1,1259,1260,1298,-1,1299,1298,1260,-1,1260,1261,1299,-1,1300,1299,1261,-1,1261,1262,1300,-1,1301,1300,1262,-1,1262,1263,1301,-1,1302,1301,1263,-1,1263,1264,1302,-1,1303,1302,1264,-1,1264,1265,1303,-1,1304,1303,1265,-1,1265,1266,1304,-1,1305,1304,1266,-1,1266,1267,1305,-1,1306,1305,1267,-1,1267,1268,1306,-1,1307,1306,1268,-1,1268,1269,1307,-1,1308,1307,1269,-1,1269,1270,1308,-1,1309,1308,1270,-1,1270,1271,1309,-1,1310,1309,1271,-1,1271,1272,1310,-1,1311,1310,1272,-1,1272,1273,1311,-1,1312,1311,1273,-1,1273,1274,1312,-1,1313,1312,1274,-1,1274,1275,1313,-1,1314,1313,1275,-1,1275,1276,1314,-1,1315,1314,1276,-1,1276,1277,1315,-1,1316,1315,1277,-1,1277,1278,1316,-1,1317,1316,1278,-1,1278,1279,1317,-1,1318,1317,1279,-1,1279,1280,1318,-1,1319,1318,1280,-1,1280,1281,1319,-1,1320,1319,1281,-1,1281,1282,1320,-1,1321,1320,1282,-1,1282,1283,1321,-1,1322,1321,1283,-1,1283,1284,1322,-1,1323,1322,1284,-1,1284,1285,1323,-1,1324,1323,1285,-1,1285,1286,1324,-1,1325,1324,1286,-1,1286,1287,1325,-1,1326,1325,1287,-1,1287,1288,1326,-1,1327,1326,1288,-1,1288,1289,1327,-1,1328,1327,1289,-1,1289,1290,1328,-1,1329,1328,1290,-1,1290,1291,1329,-1,1330,1329,1291,-1,1291,1292,1330,-1,1331,1330,1292,-1,1292,1293,1331,-1,1332,1331,1293,-1,1293,1294,1332,-1,1333,1332,1294,-1,1294,1295,1333,-1,1334,1333,1295,-1,1297,1296,1335,-1,1336,1335,1296,-1,1296,1298,1336,-1,1337,1336,1298,-1,1298,1299,1337,-1,1338,1337,1299,-1,1299,1300,1338,-1,1339,1338,1300,-1,1300,1301,1339,-1,1340,1339,1301,-1,1301,1302,1340,-1,1341,1340,1302,-1,1302,1303,1341,-1,1342,1341,1303,-1,1303,1304,1342,-1,1343,1342,1304,-1,1304,1305,1343,-1,1344,1343,1305,-1,1305,1306,1344,-1,1345,1344,1306,-1,1306,1307,1345,-1,1346,1345,1307,-1,1307,1308,1346,-1,1347,1346,1308,-1,1308,1309,1347,-1,1348,1347,1309,-1,1309,1310,1348,-1,1349,1348,1310,-1,1310,1311,1349,-1,1350,1349,1311,-1,1311,1312,1350,-1,1351,1350,1312,-1,1312,1313,1351,-1,1352,1351,1313,-1,1313,1314,1352,-1,1353,1352,1314,-1,1314,1315,1353,-1,1354,1353,1315,-1,1315,1316,1354,-1,1355,1354,1316,-1,1316,1317,1355,-1,1356,1355,1317,-1,1317,1318,1356,-1,1357,1356,1318,-1,1318,1319,1357,-1,1358,1357,1319,-1,1319,1320,1358,-1,1359,1358,1320,-1,1320,1321,1359,-1,1360,1359,1321,-1,1321,1322,1360,-1,1361,1360,1322,-1,1322,1323,1361,-1,1362,1361,1323,-1,1323,1324,1362,-1,1363,1362,1324,-1,1324,1325,1363,-1,1364,1363,1325,-1,1325,1326,1364,-1,1365,1364,1326,-1,1326,1327,1365,-1,1366,1365,1327,-1,1327,1328,1366,-1,1367,1366,1328,-1,1328,1329,1367,-1,1368,1367,1329,-1,1329,1330,1368,-1,1369,1368,1330,-1,1330,1331,1369,-1,1370,1369,1331,-1,1331,1332,1370,-1,1371,1370,1332,-1,1332,1333,1371,-1,1372,1371,1333,-1,1333,1334,1372,-1,1373,1374,1335,-1,1335,1336,1373,-1,1375,1373,1336,-1,1336,1337,1375,-1,1376,1375,1337,-1,1337,1338,1376,-1,1377,1376,1338,-1,1338,1339,1377,-1,1378,1377,1339,-1,1339,1340,1378,-1,1379,1378,1340,-1,1340,1341,1379,-1,1380,1379,1341,-1,1341,1342,1380,-1,1381,1380,1342,-1,1342,1343,1381,-1,1382,1381,1343,-1,1343,1344,1382,-1,1383,1382,1344,-1,1344,1345,1383,-1,1384,1383,1345,-1,1345,1346,1384,-1,1385,1384,1346,-1,1346,1347,1385,-1,1386,1385,1347,-1,1347,1348,1386,-1,1387,1386,1348,-1,1348,1349,1387,-1,1388,1387,1349,-1,1349,1350,1388,-1,1389,1388,1350,-1,1350,1351,1389,-1,1390,1389,1351,-1,1351,1352,1390,-1,1391,1390,1352,-1,1352,1353,1391,-1,1392,1391,1353,-1,1353,1354,1392,-1,1393,1392,1354,-1,1354,1355,1393,-1,1394,1393,1355,-1,1355,1356,1394,-1,1395,1394,1356,-1,1356,1357,1395,-1,1396,1395,1357,-1,1357,1358,1396,-1,1397,1396,1358,-1,1358,1359,1397,-1,1398,1397,1359,-1,1359,1360,1398,-1,1399,1398,1360,-1,1360,1361,1399,-1,1400,1399,1361,-1,1361,1362,1400,-1,1401,1400,1362,-1,1362,1363,1401,-1,1402,1401,1363,-1,1363,1364,1402,-1,1403,1402,1364,-1,1364,1365,1403,-1,1404,1403,1365,-1,1365,1366,1404,-1,1405,1404,1366,-1,1366,1367,1405,-1,1406,1405,1367,-1,1367,1368,1406,-1,1407,1406,1368,-1,1368,1369,1407,-1,1408,1407,1369,-1,1369,1370,1408,-1,1409,1408,1370,-1,1370,1371,1409,-1,1410,1409,1371,-1,1371,1372,1410,-1,1411,1410,1372,-1,1374,1373,1412,-1,1413,1412,1373,-1,1373,1375,1413,-1,1414,1413,1375,-1,1375,1376,1414,-1,1415,1414,1376,-1,1376,1377,1415,-1,1416,1415,1377,-1,1377,1378,1416,-1,1417,1416,1378,-1,1378,1379,1417,-1,1418,1417,1379,-1,1379,1380,1418,-1,1419,1418,1380,-1,1380,1381,1419,-1,1420,1419,1381,-1,1381,1382,1420,-1,1421,1420,1382,-1,1382,1383,1421,-1,1422,1421,1383,-1,1383,1384,1422,-1,1423,1422,1384,-1,1384,1385,1423,-1,1424,1423,1385,-1,1385,1386,1424,-1,1425,1424,1386,-1,1386,1387,1425,-1,1426,1425,1387,-1,1387,1388,1426,-1,1427,1426,1388,-1,1388,1389,1427,-1,1428,1427,1389,-1,1389,1390,1428,-1,1429,1428,1390,-1,1390,1391,1429,-1,1430,1429,1391,-1,1391,1392,1430,-1,1431,1430,1392,-1,1392,1393,1431,-1,1432,1431,1393,-1,1393,1394,1432,-1,1433,1432,1394,-1,1394,1395,1433,-1,1434,1433,1395,-1,1395,1396,1434,-1,1435,1434,1396,-1,1396,1397,1435,-1,1436,1435,1397,-1,1397,1398,1436,-1,1437,1436,1398,-1,1398,1399,1437,-1,1438,1437,1399,-1,1399,1400,1438,-1,1439,1438,1400,-1,1400,1401,1439,-1,1440,1439,1401,-1,1401,1402,1440,-1,1441,1440,1402,-1,1402,1403,1441,-1,1442,1441,1403,-1,1403,1404,1442,-1,1443,1442,1404,-1,1404,1405,1443,-1,1444,1443,1405,-1,1405,1406,1444,-1,1445,1444,1406,-1,1406,1407,1445,-1,1446,1445,1407,-1,1407,1408,1446,-1,1447,1446,1408,-1,1408,1409,1447,-1,1448,1447,1409,-1,1409,1410,1448,-1,1449,1448,1410,-1,1410,1411,1449,-1,1450,1451,1412,-1,1412,1413,1450,-1,1452,1450,1413,-1,1413,1414,1452,-1,1453,1452,1414,-1,1414,1415,1453,-1,1454,1453,1415,-1,1415,1416,1454,-1,1455,1454,1416,-1,1416,1417,1455,-1,1456,1455,1417,-1,1417,1418,1456,-1,1457,1456,1418,-1,1418,1419,1457,-1,1458,1457,1419,-1,1419,1420,1458,-1,1459,1458,1420,-1,1420,1421,1459,-1,1460,1459,1421,-1,1421,1422,1460,-1,1461,1460,1422,-1,1422,1423,1461,-1,1462,1461,1423,-1,1423,1424,1462,-1,1463,1462,1424,-1,1424,1425,1463,-1,1464,1463,1425,-1,1425,1426,1464,-1,1465,1464,1426,-1,1426,1427,1465,-1,1466,1465,1427,-1,1427,1428,1466,-1,1467,1466,1428,-1,1428,1429,1467,-1,1468,1467,1429,-1,1429,1430,1468,-1,1469,1468,1430,-1,1430,1431,1469,-1,1470,1469,1431,-1,1431,1432,1470,-1,1471,1470,1432,-1,1432,1433,1471,-1,1472,1471,1433,-1,1433,1434,1472,-1,1473,1472,1434,-1,1434,1435,1473,-1,1474,1473,1435,-1,1435,1436,1474,-1,1475,1474,1436,-1,1436,1437,1475,-1,1476,1475,1437,-1,1437,1438,1476,-1,1477,1476,1438,-1,1438,1439,1477,-1,1478,1477,1439,-1,1439,1440,1478,-1,1479,1478,1440,-1,1440,1441,1479,-1,1480,1479,1441,-1,1441,1442,1480,-1,1481,1480,1442,-1,1442,1443,1481,-1,1482,1481,1443,-1,1443,1444,1482,-1,1483,1482,1444,-1,1444,1445,1483,-1,1484,1483,1445,-1,1445,1446,1484,-1,1485,1484,1446,-1,1446,1447,1485,-1,1486,1485,1447,-1,1447,1448,1486,-1,1487,1486,1448,-1,1448,1449,1487,-1,1488,1487,1449,-1,1451,1450,1489,-1,1490,1489,1450,-1,1450,1452,1490,-1,1491,1490,1452,-1,1452,1453,1491,-1,1492,1491,1453,-1,1453,1454,1492,-1,1493,1492,1454,-1,1454,1455,1493,-1,1494,1493,1455,-1,1455,1456,1494,-1,1495,1494,1456,-1,1456,1457,1495,-1,1496,1495,1457,-1,1457,1458,1496,-1,1497,1496,1458,-1,1458,1459,1497,-1,1498,1497,1459,-1,1459,1460,1498,-1,1499,1498,1460,-1,1460,1461,1499,-1,1500,1499,1461,-1,1461,1462,1500,-1,1501,1500,1462,-1,1462,1463,1501,-1,1502,1501,1463,-1,1463,1464,1502,-1,1503,1502,1464,-1,1464,1465,1503,-1,1504,1503,1465,-1,1465,1466,1504,-1,1505,1504,1466,-1,1466,1467,1505,-1,1506,1505,1467,-1,1467,1468,1506,-1,1507,1506,1468,-1,1468,1469,1507,-1,1508,1507,1469,-1,1469,1470,1508,-1,1509,1508,1470,-1,1470,1471,1509,-1,1510,1509,1471,-1,1471,1472,1510,-1,1511,1510,1472,-1,1472,1473,1511,-1,1512,1511,1473,-1,1473,1474,1512,-1,1513,1512,1474,-1,1474,1475,1513,-1,1514,1513,1475,-1,1475,1476,1514,-1,1515,1514,1476,-1,1476,1477,1515,-1,1516,1515,1477,-1,1477,1478,1516,-1,1517,1516,1478,-1,1478,1479,1517,-1,1518,1517,1479,-1,1479,1480,1518,-1,1519,1518,1480,-1,1480,1481,1519,-1,1520,1519,1481,-1,1481,1482,1520,-1,1521,1520,1482,-1,1482,1483,1521,-1,1522,1521,1483,-1,1483,1484,1522,-1,1523,1522,1484,-1,1484,1485,1523,-1,1524,1523,1485,-1,1485,1486,1524,-1,1525,1524,1486,-1,1486,1487,1525,-1,1526,1525,1487,-1,1487,1488,1526,-1,1489,1490,1527,-1,1528,1527,1490,-1,1490,1491,1528,-1,1529,1528,1491,-1,1491,1492,1529,-1,1530,1529,1492,-1,1492,1493,1530,-1,1531,1530,1493,-1,1493,1494,1531,-1,1532,1531,1494,-1,1494,1495,1532,-1,1533,1532,1495,-1,1495,1496,1533,-1,1534,1533,1496,-1,1496,1497,1534,-1,1535,1534,1497,-1,1497,1498,1535,-1,1536,1535,1498,-1,1498,1499,1536,-1,1537,1536,1499,-1,1499,1500,1537,-1,1538,1537,1500,-1,1500,1501,1538,-1,1539,1538,1501,-1,1501,1502,1539,-1,1540,1539,1502,-1,1502,1503,1540,-1,1541,1540,1503,-1,1503,1504,1541,-1,1542,1541,1504,-1,1504,1505,1542,-1,1543,1542,1505,-1,1505,1506,1543,-1,1544,1543,1506,-1,1506,1507,1544,-1,1545,1544,1507,-1,1507,1508,1545,-1,1546,1545,1508,-1,1508,1509,1546,-1,1547,1546,1509,-1,1509,1510,1547,-1,1548,1547,1510,-1,1510,1511,1548,-1,1549,1548,1511,-1,1511,1512,1549,-1,1550,1549,1512,-1,1512,1513,1550,-1,1551,1550,1513,-1,1513,1514,1551,-1,1552,1551,1514,-1,1514,1515,1552,-1,1553,1552,1515,-1,1515,1516,1553,-1,1554,1553,1516,-1,1516,1517,1554,-1,1555,1554,1517,-1,1517,1518,1555,-1,1556,1555,1518,-1,1518,1519,1556,-1,1557,1556,1519,-1,1519,1520,1557,-1,1558,1557,1520,-1,1520,1521,1558,-1,1559,1558,1521,-1,1521,1522,1559,-1,1560,1559,1522,-1,1522,1523,1560,-1,1561,1560,1523,-1,1523,1524,1561,-1,1562,1561,1524,-1,1524,1525,1562,-1,1563,1562,1525,-1,1525,1526,1563,-1,1564,1563,1526,-1,1528,1529,1565,-1,1566,1565,1529,-1,1529,1530,1566,-1,1567,1566,1530,-1,1530,1531,1567,-1,1568,1567,1531,-1,1531,1532,1568,-1,1569,1568,1532,-1,1532,1533,1569,-1,1570,1569,1533,-1,1533,1534,1570,-1,1571,1570,1534,-1,1534,1535,1571,-1,1572,1571,1535,-1,1535,1536,1572,-1,1573,1572,1536,-1,1536,1537,1573,-1,1574,1573,1537,-1,1537,1538,1574,-1,1575,1574,1538,-1,1538,1539,1575,-1,1576,1575,1539,-1,1539,1540,1576,-1,1577,1576,1540,-1,1540,1541,1577,-1,1578,1577,1541,-1,1541,1542,1578,-1,1579,1578,1542,-1,1542,1543,1579,-1,1580,1579,1543,-1,1543,1544,1580,-1,1581,1580,1544,-1,1544,1545,1581,-1,1582,1581,1545,-1,1545,1546,1582,-1,1583,1582,1546,-1,1546,1547,1583,-1,1584,1583,1547,-1,1547,1548,1584,-1,1585,1584,1548,-1,1548,1549,1585,-1,1586,1585,1549,-1,1549,1550,1586,-1,1587,1586,1550,-1,1550,1551,1587,-1,1588,1587,1551,-1,1551,1552,1588,-1,1589,1588,1552,-1,1552,1553,1589,-1,1590,1589,1553,-1,1553,1554,1590,-1,1591,1590,1554,-1,1554,1555,1591,-1,1592,1591,1555,-1,1555,1556,1592,-1,1593,1592,1556,-1,1556,1557,1593,-1,1594,1593,1557,-1,1557,1558,1594,-1,1595,1594,1558,-1,1558,1559,1595,-1,1596,1595,1559,-1,1559,1560,1596,-1,1597,1596,1560,-1,1560,1561,1597,-1,1598,1597,1561,-1,1561,1562,1598,-1,1599,1598,1562,-1,1562,1563,1599,-1,1600,1599,1563,-1,1563,1564,1600,-1,1601,1600,1564,-1,1564,1602,1601,-1,1603,1601,1602,-1,1602,1604,1603,-1,1605,1603,1604,-1,1606,1607,1565,-1,1565,1566,1606,-1,1608,1606,1566,-1,1566,1567,1608,-1,1609,1608,1567,-1,1567,1568,1609,-1,1610,1609,1568,-1,1568,1569,1610,-1,1611,1610,1569,-1,1569,1570,1611,-1,1612,1611,1570,-1,1570,1571,1612,-1,1613,1612,1571,-1,1571,1572,1613,-1,1614,1613,1572,-1,1572,1573,1614,-1,1615,1614,1573,-1,1573,1574,1615,-1,1616,1615,1574,-1,1574,1575,1616,-1,1617,1616,1575,-1,1575,1576,1617,-1,1618,1617,1576,-1,1576,1577,1618,-1,1619,1618,1577,-1,1577,1578,1619,-1,1620,1619,1578,-1,1578,1579,1620,-1,1621,1620,1579,-1,1579,1580,1621,-1,1622,1621,1580,-1,1580,1581,1622,-1,1623,1622,1581,-1,1581,1582,1623,-1,1624,1623,1582,-1,1582,1583,1624,-1,1625,1624,1583,-1,1583,1584,1625,-1,1626,1625,1584,-1,1584,1585,1626,-1,1627,1626,1585,-1,1585,1586,1627,-1,1628,1627,1586,-1,1586,1587,1628,-1,1629,1628,1587,-1,1587,1588,1629,-1,1630,1629,1588,-1,1588,1589,1630,-1,1631,1630,1589,-1,1589,1590,1631,-1,1632,1631,1590,-1,1590,1591,1632,-1,1633,1632,1591,-1,1591,1592,1633,-1,1634,1633,1592,-1,1592,1593,1634,-1,1635,1634,1593,-1,1593,1594,1635,-1,1636,1635,1594,-1,1594,1595,1636,-1,1637,1636,1595,-1,1595,1596,1637,-1,1638,1637,1596,-1,1596,1597,1638,-1,1639,1638,1597,-1,1597,1598,1639,-1,1640,1639,1598,-1,1598,1599,1640,-1,1641,1640,1599,-1,1599,1600,1641,-1,1642,1641,1600,-1,1600,1601,1642,-1,1643,1642,1601,-1,1601,1603,1643,-1,1644,1643,1603,-1,1603,1605,1644,-1,1645,1644,1605,-1,1646,1647,1607,-1,1607,1606,1646,-1,1648,1646,1606,-1,1606,1608,1648,-1,1649,1648,1608,-1,1608,1609,1649,-1,1650,1649,1609,-1,1609,1610,1650,-1,1651,1650,1610,-1,1610,1611,1651,-1,1652,1651,1611,-1,1611,1612,1652,-1,1653,1652,1612,-1,1612,1613,1653,-1,1654,1653,1613,-1,1613,1614,1654,-1,1655,1654,1614,-1,1614,1615,1655,-1,1656,1655,1615,-1,1615,1616,1656,-1,1657,1656,1616,-1,1616,1617,1657,-1,1658,1657,1617,-1,1617,1618,1658,-1,1659,1658,1618,-1,1618,1619,1659,-1,1660,1659,1619,-1,1619,1620,1660,-1,1661,1660,1620,-1,1620,1621,1661,-1,1662,1661,1621,-1,1621,1622,1662,-1,1663,1662,1622,-1,1622,1623,1663,-1,1664,1663,1623,-1,1623,1624,1664,-1,1665,1664,1624,-1,1624,1625,1665,-1,1666,1665,1625,-1,1625,1626,1666,-1,1667,1666,1626,-1,1626,1627,1667,-1,1668,1667,1627,-1,1627,1628,1668,-1,1669,1668,1628,-1,1628,1629,1669,-1,1670,1669,1629,-1,1629,1630,1670,-1,1671,1670,1630,-1,1630,1631,1671,-1,1672,1671,1631,-1,1631,1632,1672,-1,1673,1672,1632,-1,1632,1633,1673,-1,1674,1673,1633,-1,1633,1634,1674,-1,1675,1674,1634,-1,1634,1635,1675,-1,1676,1675,1635,-1,1635,1636,1676,-1,1677,1676,1636,-1,1636,1637,1677,-1,1678,1677,1637,-1,1637,1638,1678,-1,1679,1678,1638,-1,1638,1639,1679,-1,1680,1679,1639,-1,1639,1640,1680,-1,1681,1680,1640,-1,1640,1641,1681,-1,1682,1681,1641,-1,1641,1642,1682,-1,1683,1682,1642,-1,1642,1643,1683,-1,1684,1683,1643,-1,1643,1644,1684,-1,1685,1684,1644,-1,1644,1645,1685,-1,1686,1687,1647,-1,1647,1646,1686,-1,1688,1686,1646,-1,1646,1648,1688,-1,1689,1688,1648,-1,1648,1649,1689,-1,1690,1689,1649,-1,1649,1650,1690,-1,1691,1690,1650,-1,1650,1651,1691,-1,1692,1691,1651,-1,1651,1652,1692,-1,1693,1692,1652,-1,1652,1653,1693,-1,1694,1693,1653,-1,1653,1654,1694,-1,1695,1694,1654,-1,1654,1655,1695,-1,1696,1695,1655,-1,1655,1656,1696,-1,1697,1696,1656,-1,1656,1657,1697,-1,1698,1697,1657,-1,1657,1658,1698,-1,1699,1698,1658,-1,1658,1659,1699,-1,1700,1699,1659,-1,1659,1660,1700,-1,1701,1700,1660,-1,1660,1661,1701,-1,1702,1701,1661,-1,1661,1662,1702,-1,1703,1702,1662,-1,1662,1663,1703,-1,1704,1703,1663,-1,1663,1664,1704,-1,1705,1704,1664,-1,1664,1665,1705,-1,1706,1705,1665,-1,1665,1666,1706,-1,1707,1706,1666,-1,1666,1667,1707,-1,1708,1707,1667,-1,1667,1668,1708,-1,1709,1708,1668,-1,1668,1669,1709,-1,1710,1709,1669,-1,1669,1670,1710,-1,1711,1710,1670,-1,1670,1671,1711,-1,1712,1711,1671,-1,1671,1672,1712,-1,1713,1712,1672,-1,1672,1673,1713,-1,1714,1713,1673,-1,1673,1674,1714,-1,1715,1714,1674,-1,1674,1675,1715,-1,1716,1715,1675,-1,1675,1676,1716,-1,1717,1716,1676,-1,1676,1677,1717,-1,1718,1717,1677,-1,1677,1678,1718,-1,1719,1718,1678,-1,1678,1679,1719,-1,1720,1719,1679,-1,1679,1680,1720,-1,1721,1720,1680,-1,1680,1681,1721,-1,1722,1721,1681,-1,1681,1682,1722,-1,1723,1722,1682,-1,1682,1683,1723,-1,1724,1723,1683,-1,1683,1684,1724,-1,1687,1686,1725,-1,1726,1725,1686,-1,1686,1688,1726,-1,1727,1726,1688,-1,1688,1689,1727,-1,1728,1727,1689,-1,1689,1690,1728,-1,1729,1728,1690,-1,1690,1691,1729,-1,1730,1729,1691,-1,1691,1692,1730,-1,1731,1730,1692,-1,1692,1693,1731,-1,1732,1731,1693,-1,1693,1694,1732,-1,1733,1732,1694,-1,1694,1695,1733,-1,1734,1733,1695,-1,1695,1696,1734,-1,1735,1734,1696,-1,1696,1697,1735,-1,1736,1735,1697,-1,1697,1698,1736,-1,1737,1736,1698,-1,1698,1699,1737,-1,1738,1737,1699,-1,1699,1700,1738,-1,1739,1738,1700,-1,1700,1701,1739,-1,1740,1739,1701,-1,1701,1702,1740,-1,1741,1740,1702,-1,1702,1703,1741,-1,1742,1741,1703,-1,1703,1704,1742,-1,1743,1742,1704,-1,1704,1705,1743,-1,1744,1743,1705,-1,1705,1706,1744,-1,1745,1744,1706,-1,1706,1707,1745,-1,1746,1745,1707,-1,1707,1708,1746,-1,1747,1746,1708,-1,1708,1709,1747,-1,1748,1747,1709,-1,1709,1710,1748,-1,1749,1748,1710,-1,1710,1711,1749,-1,1750,1749,1711,-1,1711,1712,1750,-1,1751,1750,1712,-1,1712,1713,1751,-1,1752,1751,1713,-1,1713,1714,1752,-1,1753,1752,1714,-1,1714,1715,1753,-1,1754,1753,1715,-1,1715,1716,1754,-1,1755,1754,1716,-1,1716,1717,1755,-1,1756,1755,1717,-1,1717,1718,1756,-1,1757,1756,1718,-1,1718,1719,1757,-1,1758,1757,1719,-1,1719,1720,1758,-1,1759,1758,1720,-1,1720,1721,1759,-1,1760,1759,1721,-1,1721,1722,1760,-1,1761,1760,1722,-1,1722,1723,1761,-1,1762,1761,1723,-1,1723,1724,1762,-1,1763,1762,1724,-1,1725,1726,1764,-1,1765,1764,1726,-1,1726,1727,1765,-1,1766,1765,1727,-1,1727,1728,1766,-1,1767,1766,1728,-1,1728,1729,1767,-1,1768,1767,1729,-1,1729,1730,1768,-1,1769,1768,1730,-1,1730,1731,1769,-1,1770,1769,1731,-1,1731,1732,1770,-1,1771,1770,1732,-1,1732,1733,1771,-1,1772,1771,1733,-1,1733,1734,1772,-1,1773,1772,1734,-1,1734,1735,1773,-1,1774,1773,1735,-1,1735,1736,1774,-1,1775,1774,1736,-1,1736,1737,1775,-1,1776,1775,1737,-1,1737,1738,1776,-1,1777,1776,1738,-1,1738,1739,1777,-1,1778,1777,1739,-1,1739,1740,1778,-1,1779,1778,1740,-1,1740,1741,1779,-1,1780,1779,1741,-1,1741,1742,1780,-1,1781,1780,1742,-1,1742,1743,1781,-1,1782,1781,1743,-1,1743,1744,1782,-1,1783,1782,1744,-1,1744,1745,1783,-1,1784,1783,1745,-1,1745,1746,1784,-1,1785,1784,1746,-1,1746,1747,1785,-1,1786,1785,1747,-1,1747,1748,1786,-1,1787,1786,1748,-1,1748,1749,1787,-1,1788,1787,1749,-1,1749,1750,1788,-1,1789,1788,1750,-1,1750,1751,1789,-1,1790,1789,1751,-1,1751,1752,1790,-1,1791,1790,1752,-1,1752,1753,1791,-1,1792,1791,1753,-1,1753,1754,1792,-1,1793,1792,1754,-1,1754,1755,1793,-1,1794,1793,1755,-1,1755,1756,1794,-1,1795,1794,1756,-1,1756,1757,1795,-1,1796,1795,1757,-1,1757,1758,1796,-1,1797,1796,1758,-1,1758,1759,1797,-1,1798,1797,1759,-1,1759,1760,1798,-1,1799,1798,1760,-1,1760,1761,1799,-1,1800,1799,1761,-1,1761,1762,1800,-1,1801,1800,1762,-1,1762,1763,1801,-1,1802,1801,1763,-1,1803,1804,1764,-1,1764,1765,1803,-1,1805,1803,1765,-1,1765,1766,1805,-1,1806,1805,1766,-1,1766,1767,1806,-1,1807,1806,1767,-1,1767,1768,1807,-1,1808,1807,1768,-1,1768,1769,1808,-1,1809,1808,1769,-1,1769,1770,1809,-1,1810,1809,1770,-1,1770,1771,1810,-1,1811,1810,1771,-1,1771,1772,1811,-1,1812,1811,1772,-1,1772,1773,1812,-1,1813,1812,1773,-1,1773,1774,1813,-1,1814,1813,1774,-1,1774,1775,1814,-1,1815,1814,1775,-1,1775,1776,1815,-1,1816,1815,1776,-1,1776,1777,1816,-1,1817,1816,1777,-1,1777,1778,1817,-1,1818,1817,1778,-1,1778,1779,1818,-1,1819,1818,1779,-1,1779,1780,1819,-1,1820,1819,1780,-1,1780,1781,1820,-1,1821,1820,1781,-1,1781,1782,1821,-1,1822,1821,1782,-1,1782,1783,1822,-1,1823,1822,1783,-1,1783,1784,1823,-1,1824,1823,1784,-1,1784,1785,1824,-1,1825,1824,1785,-1,1785,1786,1825,-1,1826,1825,1786,-1,1786,1787,1826,-1,1827,1826,1787,-1,1787,1788,1827,-1,1828,1827,1788,-1,1788,1789,1828,-1,1829,1828,1789,-1,1789,1790,1829,-1,1830,1829,1790,-1,1790,1791,1830,-1,1831,1830,1791,-1,1791,1792,1831,-1,1832,1831,1792,-1,1792,1793,1832,-1,1833,1832,1793,-1,1793,1794,1833,-1,1834,1833,1794,-1,1794,1795,1834,-1,1835,1834,1795,-1,1795,1796,1835,-1,1836,1835,1796,-1,1796,1797,1836,-1,1837,1836,1797,-1,1797,1798,1837,-1,1838,1837,1798,-1,1798,1799,1838,-1,1839,1838,1799,-1,1799,1800,1839,-1,1840,1839,1800,-1,1800,1801,1840,-1,1841,1840,1801,-1,1801,1802,1841,-1,1842,1843,1804,-1,1804,1803,1842,-1,1844,1842,1803,-1,1803,1805,1844,-1,1845,1844,1805,-1,1805,1806,1845,-1,1846,1845,1806,-1,1806,1807,1846,-1,1847,1846,1807,-1,1807,1808,1847,-1,1848,1847,1808,-1,1808,1809,1848,-1,1849,1848,1809,-1,1809,1810,1849,-1,1850,1849,1810,-1,1810,1811,1850,-1,1851,1850,1811,-1,1811,1812,1851,-1,1852,1851,1812,-1,1812,1813,1852,-1,1853,1852,1813,-1,1813,1814,1853,-1,1854,1853,1814,-1,1814,1815,1854,-1,1855,1854,1815,-1,1815,1816,1855,-1,1856,1855,1816,-1,1816,1817,1856,-1,1857,1856,1817,-1,1817,1818,1857,-1,1858,1857,1818,-1,1818,1819,1858,-1,1859,1858,1819,-1,1819,1820,1859,-1,1860,1859,1820,-1,1820,1821,1860,-1,1861,1860,1821,-1,1821,1822,1861,-1,1862,1861,1822,-1,1822,1823,1862,-1,1863,1862,1823,-1,1823,1824,1863,-1,1864,1863,1824,-1,1824,1825,1864,-1,1865,1864,1825,-1,1825,1826,1865,-1,1866,1865,1826,-1,1826,1827,1866,-1,1867,1866,1827,-1,1827,1828,1867,-1,1868,1867,1828,-1,1828,1829,1868,-1,1869,1868,1829,-1,1829,1830,1869,-1,1870,1869,1830,-1,1830,1831,1870,-1,1871,1870,1831,-1,1831,1832,1871,-1,1872,1871,1832,-1,1832,1833,1872,-1,1873,1872,1833,-1,1833,1834,1873,-1,1874,1873,1834,-1,1834,1835,1874,-1,1875,1874,1835,-1,1835,1836,1875,-1,1876,1875,1836,-1,1836,1837,1876,-1,1877,1876,1837,-1,1837,1838,1877,-1,1878,1877,1838,-1,1838,1839,1878,-1,1879,1878,1839,-1,1839,1840,1879,-1,1880,1879,1840,-1,1840,1841,1880,-1,1881,1880,1841,-1,1843,1842,1882,-1,1883,1882,1842,-1,1842,1844,1883,-1,1884,1883,1844,-1,1844,1845,1884,-1,1885,1884,1845,-1,1845,1846,1885,-1,1886,1885,1846,-1,1846,1847,1886,-1,1887,1886,1847,-1,1847,1848,1887,-1,1888,1887,1848,-1,1848,1849,1888,-1,1889,1888,1849,-1,1849,1850,1889,-1,1890,1889,1850,-1,1850,1851,1890,-1,1891,1890,1851,-1,1851,1852,1891,-1,1892,1891,1852,-1,1852,1853,1892,-1,1893,1892,1853,-1,1853,1854,1893,-1,1894,1893,1854,-1,1854,1855,1894,-1,1895,1894,1855,-1,1855,1856,1895,-1,1896,1895,1856,-1,1856,1857,1896,-1,1897,1896,1857,-1,1857,1858,1897,-1,1898,1897,1858,-1,1858,1859,1898,-1,1899,1898,1859,-1,1859,1860,1899,-1,1900,1899,1860,-1,1860,1861,1900,-1,1901,1900,1861,-1,1861,1862,1901,-1,1902,1901,1862,-1,1862,1863,1902,-1,1903,1902,1863,-1,1863,1864,1903,-1,1904,1903,1864,-1,1864,1865,1904,-1,1905,1904,1865,-1,1865,1866,1905,-1,1906,1905,1866,-1,1866,1867,1906,-1,1907,1906,1867,-1,1867,1868,1907,-1,1908,1907,1868,-1,1868,1869,1908,-1,1909,1908,1869,-1,1869,1870,1909,-1,1910,1909,1870,-1,1870,1871,1910,-1,1911,1910,1871,-1,1871,1872,1911,-1,1912,1911,1872,-1,1872,1873,1912,-1,1913,1912,1873,-1,1873,1874,1913,-1,1914,1913,1874,-1,1874,1875,1914,-1,1915,1914,1875,-1,1875,1876,1915,-1,1916,1915,1876,-1,1876,1877,1916,-1,1917,1916,1877,-1,1877,1878,1917,-1,1918,1917,1878,-1,1878,1879,1918,-1,1919,1918,1879,-1,1879,1880,1919,-1,1920,1919,1880,-1,1880,1881,1920,-1,1921,1920,1881,-1,1922,1923,1882,-1,1882,1883,1922,-1,1924,1922,1883,-1,1883,1884,1924,-1,1925,1924,1884,-1,1884,1885,1925,-1,1926,1925,1885,-1,1885,1886,1926,-1,1927,1926,1886,-1,1886,1887,1927,-1,1928,1927,1887,-1,1887,1888,1928,-1,1929,1928,1888,-1,1888,1889,1929,-1,1930,1929,1889,-1,1889,1890,1930,-1,1931,1930,1890,-1,1890,1891,1931,-1,1932,1931,1891,-1,1891,1892,1932,-1,1933,1932,1892,-1,1892,1893,1933,-1,1934,1933,1893,-1,1893,1894,1934,-1,1935,1934,1894,-1,1894,1895,1935,-1,1936,1935,1895,-1,1895,1896,1936,-1,1937,1936,1896,-1,1896,1897,1937,-1,1938,1937,1897,-1,1897,1898,1938,-1,1939,1938,1898,-1,1898,1899,1939,-1,1940,1939,1899,-1,1899,1900,1940,-1,1941,1940,1900,-1,1900,1901,1941,-1,1942,1941,1901,-1,1901,1902,1942,-1,1943,1942,1902,-1,1902,1903,1943,-1,1944,1943,1903,-1,1903,1904,1944,-1,1945,1944,1904,-1,1904,1905,1945,-1,1946,1945,1905,-1,1905,1906,1946,-1,1947,1946,1906,-1,1906,1907,1947,-1,1948,1947,1907,-1,1907,1908,1948,-1,1949,1948,1908,-1,1908,1909,1949,-1,1950,1949,1909,-1,1909,1910,1950,-1,1951,1950,1910,-1,1910,1911,1951,-1,1952,1951,1911,-1,1911,1912,1952,-1,1953,1952,1912,-1,1912,1913,1953,-1,1954,1953,1913,-1,1913,1914,1954,-1,1955,1954,1914,-1,1914,1915,1955,-1,1956,1955,1915,-1,1915,1916,1956,-1,1957,1956,1916,-1,1916,1917,1957,-1,1958,1957,1917,-1,1917,1918,1958,-1,1959,1958,1918,-1,1918,1919,1959,-1,1960,1959,1919,-1,1919,1920,1960,-1,1961,1960,1920,-1,1920,1921,1961,-1,1923,1922,1962,-1,1963,1962,1922,-1,1922,1924,1963,-1,1964,1963,1924,-1,1924,1925,1964,-1,1965,1964,1925,-1,1925,1926,1965,-1,1966,1965,1926,-1,1926,1927,1966,-1,1967,1966,1927,-1,1927,1928,1967,-1,1968,1967,1928,-1,1928,1929,1968,-1,1969,1968,1929,-1,1929,1930,1969,-1,1970,1969,1930,-1,1930,1931,1970,-1,1971,1970,1931,-1,1931,1932,1971,-1,1972,1971,1932,-1,1932,1933,1972,-1,1973,1972,1933,-1,1933,1934,1973,-1,1974,1973,1934,-1,1934,1935,1974,-1,1975,1974,1935,-1,1935,1936,1975,-1,1976,1975,1936,-1,1936,1937,1976,-1,1977,1976,1937,-1,1937,1938,1977,-1,1978,1977,1938,-1,1938,1939,1978,-1,1979,1978,1939,-1,1939,1940,1979,-1,1980,1979,1940,-1,1940,1941,1980,-1,1981,1980,1941,-1,1941,1942,1981,-1,1982,1981,1942,-1,1942,1943,1982,-1,1983,1982,1943,-1,1943,1944,1983,-1,1984,1983,1944,-1,1944,1945,1984,-1,1985,1984,1945,-1,1945,1946,1985,-1,1986,1985,1946,-1,1946,1947,1986,-1,1987,1986,1947,-1,1947,1948,1987,-1,1988,1987,1948,-1,1948,1949,1988,-1,1989,1988,1949,-1,1949,1950,1989,-1,1990,1989,1950,-1,1950,1951,1990,-1,1991,1990,1951,-1,1951,1952,1991,-1,1992,1991,1952,-1,1952,1953,1992,-1,1993,1992,1953,-1,1953,1954,1993,-1,1994,1993,1954,-1,1954,1955,1994,-1,1995,1994,1955,-1,1955,1956,1995,-1,1996,1995,1956,-1,1956,1957,1996,-1,1997,1996,1957,-1,1957,1958,1997,-1,1998,1997,1958,-1,1958,1959,1998,-1,1962,1963,1999,-1,2000,1999,1963,-1,1963,1964,2000,-1,2001,2000,1964,-1,1964,1965,2001,-1,2002,2001,1965,-1,1965,1966,2002,-1,2003,2002,1966,-1,1966,1967,2003,-1,2004,2003,1967,-1,1967,1968,2004,-1,2005,2004,1968,-1,1968,1969,2005,-1,2006,2005,1969,-1,1969,1970,2006,-1,2007,2006,1970,-1,1970,1971,2007,-1,2008,2007,1971,-1,1971,1972,2008,-1,2009,2008,1972,-1,1972,1973,2009,-1,2010,2009,1973,-1,1973,1974,2010,-1,2011,2010,1974,-1,1974,1975,2011,-1,2012,2011,1975,-1,1975,1976,2012,-1,2013,2012,1976,-1,1976,1977,2013,-1,2014,2013,1977,-1,1977,1978,2014,-1,2015,2014,1978,-1,1978,1979,2015,-1,2016,2015,1979,-1,1979,1980,2016,-1,2017,2016,1980,-1,1980,1981,2017,-1,2018,2017,1981,-1,1981,1982,2018,-1,2019,2018,1982,-1,1982,1983,2019,-1,2020,2019,1983,-1,1983,1984,2020,-1,2021,2020,1984,-1,1984,1985,2021,-1,2022,2021,1985,-1,1985,1986,2022,-1,2023,2022,1986,-1,1986,1987,2023,-1,2024,2023,1987,-1,1987,1988,2024,-1,2025,2024,1988,-1,1988,1989,2025,-1,2026,2025,1989,-1,1989,1990,2026,-1,2027,2026,1990,-1,1990,1991,2027,-1,2028,2027,1991,-1,1991,1992,2028,-1,2029,2028,1992,-1,1992,1993,2029,-1,2030,2029,1993,-1,1993,1994,2030,-1,2031,2030,1994,-1,1994,1995,2031,-1,2032,2031,1995,-1,1995,1996,2032,-1,2033,2032,1996,-1,1996,1997,2033,-1,2034,2033,1997,-1,1997,1998,2034,-1,2035,2036,1999,-1,1999,2000,2035,-1,2037,2035,2000,-1,2000,2001,2037,-1,2038,2037,2001,-1,2001,2002,2038,-1,2039,2038,2002,-1,2002,2003,2039,-1,2040,2039,2003,-1,2003,2004,2040,-1,2041,2040,2004,-1,2004,2005,2041,-1,2042,2041,2005,-1,2005,2006,2042,-1,2043,2042,2006,-1,2006,2007,2043,-1,2044,2043,2007,-1,2007,2008,2044,-1,2045,2044,2008,-1,2008,2009,2045,-1,2046,2045,2009,-1,2009,2010,2046,-1,2047,2046,2010,-1,2010,2011,2047,-1,2048,2047,2011,-1,2011,2012,2048,-1,2049,2048,2012,-1,2012,2013,2049,-1,2050,2049,2013,-1,2013,2014,2050,-1,2051,2050,2014,-1,2014,2015,2051,-1,2052,2051,2015,-1,2015,2016,2052,-1,2053,2052,2016,-1,2016,2017,2053,-1,2054,2053,2017,-1,2017,2018,2054,-1,2055,2054,2018,-1,2018,2019,2055,-1,2056,2055,2019,-1,2019,2020,2056,-1,2057,2056,2020,-1,2020,2021,2057,-1,2058,2057,2021,-1,2021,2022,2058,-1,2059,2058,2022,-1,2022,2023,2059,-1,2060,2059,2023,-1,2023,2024,2060,-1,2061,2060,2024,-1,2024,2025,2061,-1,2062,2061,2025,-1,2025,2026,2062,-1,2063,2062,2026,-1,2026,2027,2063,-1,2064,2063,2027,-1,2027,2028,2064,-1,2065,2064,2028,-1,2028,2029,2065,-1,2066,2065,2029,-1,2029,2030,2066,-1,2067,2066,2030,-1,2030,2031,2067,-1,2068,2067,2031,-1,2031,2032,2068,-1,2069,2068,2032,-1,2032,2033,2069,-1,2070,2069,2033,-1,2033,2034,2070,-1,2036,2035,2071,-1,2072,2071,2035,-1,2035,2037,2072,-1,2073,2072,2037,-1,2037,2038,2073,-1,2074,2073,2038,-1,2038,2039,2074,-1,2075,2074,2039,-1,2039,2040,2075,-1,2076,2075,2040,-1,2040,2041,2076,-1,2077,2076,2041,-1,2041,2042,2077,-1,2078,2077,2042,-1,2042,2043,2078,-1,2079,2078,2043,-1,2043,2044,2079,-1,2080,2079,2044,-1,2044,2045,2080,-1,2081,2080,2045,-1,2045,2046,2081,-1,2082,2081,2046,-1,2046,2047,2082,-1,2083,2082,2047,-1,2047,2048,2083,-1,2084,2083,2048,-1,2048,2049,2084,-1,2085,2084,2049,-1,2049,2050,2085,-1,2086,2085,2050,-1,2050,2051,2086,-1,2087,2086,2051,-1,2051,2052,2087,-1,2088,2087,2052,-1,2052,2053,2088,-1,2089,2088,2053,-1,2053,2054,2089,-1,2090,2089,2054,-1,2054,2055,2090,-1,2091,2090,2055,-1,2055,2056,2091,-1,2092,2091,2056,-1,2056,2057,2092,-1,2093,2092,2057,-1,2057,2058,2093,-1,2094,2093,2058,-1,2058,2059,2094,-1,2095,2094,2059,-1,2059,2060,2095,-1,2096,2095,2060,-1,2060,2061,2096,-1,2097,2096,2061,-1,2061,2062,2097,-1,2098,2097,2062,-1,2062,2063,2098,-1,2099,2098,2063,-1,2063,2064,2099,-1,2100,2099,2064,-1,2064,2065,2100,-1,2101,2100,2065,-1,2065,2066,2101,-1,2102,2101,2066,-1,2066,2067,2102,-1,2103,2102,2067,-1,2067,2068,2103,-1,2104,2103,2068,-1,2068,2069,2104,-1,2071,2072,2105,-1,2106,2105,2072,-1,2072,2073,2106,-1,2107,2106,2073,-1,2073,2074,2107,-1,2108,2107,2074,-1,2074,2075,2108,-1,2109,2108,2075,-1,2075,2076,2109,-1,2110,2109,2076,-1,2076,2077,2110,-1,2111,2110,2077,-1,2077,2078,2111,-1,2112,2111,2078,-1,2078,2079,2112,-1,2113,2112,2079,-1,2079,2080,2113,-1,2114,2113,2080,-1,2080,2081,2114,-1,2115,2114,2081,-1,2081,2082,2115,-1,2116,2115,2082,-1,2082,2083,2116,-1,2117,2116,2083,-1,2083,2084,2117,-1,2118,2117,2084,-1,2084,2085,2118,-1,2119,2118,2085,-1,2085,2086,2119,-1,2120,2119,2086,-1,2086,2087,2120,-1,2121,2120,2087,-1,2087,2088,2121,-1,2122,2121,2088,-1,2088,2089,2122,-1,2123,2122,2089,-1,2089,2090,2123,-1,2124,2123,2090,-1,2090,2091,2124,-1,2125,2124,2091,-1,2091,2092,2125,-1,2126,2125,2092,-1,2092,2093,2126,-1,2127,2126,2093,-1,2093,2094,2127,-1,2128,2127,2094,-1,2094,2095,2128,-1,2129,2128,2095,-1,2095,2096,2129,-1,2130,2129,2096,-1,2096,2097,2130,-1,2131,2130,2097,-1,2097,2098,2131,-1,2132,2131,2098,-1,2098,2099,2132,-1,2133,2132,2099,-1,2099,2100,2133,-1,2134,2133,2100,-1,2100,2101,2134,-1,2135,2134,2101,-1,2101,2102,2135,-1,2136,2135,2102,-1,2102,2103,2136,-1,2137,2136,2103,-1,2103,2104,2137,-1,2138,2139,2105,-1,2105,2106,2138,-1,2140,2138,2106,-1,2106,2107,2140,-1,2141,2140,2107,-1,2107,2108,2141,-1,2142,2141,2108,-1,2108,2109,2142,-1,2143,2142,2109,-1,2109,2110,2143,-1,2144,2143,2110,-1,2110,2111,2144,-1,2145,2144,2111,-1,2111,2112,2145,-1,2146,2145,2112,-1,2112,2113,2146,-1,2147,2146,2113,-1,2113,2114,2147,-1,2148,2147,2114,-1,2114,2115,2148,-1,2149,2148,2115,-1,2115,2116,2149,-1,2150,2149,2116,-1,2116,2117,2150,-1,2151,2150,2117,-1,2117,2118,2151,-1,2152,2151,2118,-1,2118,2119,2152,-1,2153,2152,2119,-1,2119,2120,2153,-1,2154,2153,2120,-1,2120,2121,2154,-1,2155,2154,2121,-1,2121,2122,2155,-1,2156,2155,2122,-1,2122,2123,2156,-1,2157,2156,2123,-1,2123,2124,2157,-1,2158,2157,2124,-1,2124,2125,2158,-1,2159,2158,2125,-1,2125,2126,2159,-1,2160,2159,2126,-1,2126,2127,2160,-1,2161,2160,2127,-1,2127,2128,2161,-1,2162,2161,2128,-1,2128,2129,2162,-1,2163,2162,2129,-1,2129,2130,2163,-1,2164,2163,2130,-1,2130,2131,2164,-1,2165,2164,2131,-1,2131,2132,2165,-1,2166,2165,2132,-1,2132,2133,2166,-1,2167,2166,2133,-1,2133,2134,2167,-1,2168,2167,2134,-1,2134,2135,2168,-1,2169,2168,2135,-1,2135,2136,2169,-1,2170,2169,2136,-1,2136,2137,2170,-1,2139,2138,2171,-1,2172,2171,2138,-1,2138,2140,2172,-1,2173,2172,2140,-1,2140,2141,2173,-1,2174,2173,2141,-1,2141,2142,2174,-1,2175,2174,2142,-1,2142,2143,2175,-1,2176,2175,2143,-1,2143,2144,2176,-1,2177,2176,2144,-1,2144,2145,2177,-1,2178,2177,2145,-1,2145,2146,2178,-1,2179,2178,2146,-1,2146,2147,2179,-1,2180,2179,2147,-1,2147,2148,2180,-1,2181,2180,2148,-1,2148,2149,2181,-1,2182,2181,2149,-1,2149,2150,2182,-1,2183,2182,2150,-1,2150,2151,2183,-1,2184,2183,2151,-1,2151,2152,2184,-1,2185,2184,2152,-1,2152,2153,2185,-1,2186,2185,2153,-1,2153,2154,2186,-1,2187,2186,2154,-1,2154,2155,2187,-1,2188,2187,2155,-1,2155,2156,2188,-1,2189,2188,2156,-1,2156,2157,2189,-1,2190,2189,2157,-1,2157,2158,2190,-1,2191,2190,2158,-1,2158,2159,2191,-1,2192,2191,2159,-1,2159,2160,2192,-1,2193,2192,2160,-1,2160,2161,2193,-1,2194,2193,2161,-1,2161,2162,2194,-1,2195,2194,2162,-1,2162,2163,2195,-1,2196,2195,2163,-1,2163,2164,2196,-1,2197,2196,2164,-1,2164,2165,2197,-1,2198,2197,2165,-1,2165,2166,2198,-1,2199,2198,2166,-1,2166,2167,2199,-1,2200,2199,2167,-1,2167,2168,2200,-1,2201,2200,2168,-1,2168,2169,2201,-1,2202,2201,2169,-1,2169,2170,2202,-1,2203,2202,2170,-1,2204,2205,2171,-1,2171,2172,2204,-1,2206,2204,2172,-1,2172,2173,2206,-1,2207,2206,2173,-1,2173,2174,2207,-1,2208,2207,2174,-1,2174,2175,2208,-1,2176,2177,2209,-1,2210,2209,2177,-1,2177,2178,2210,-1,2211,2210,2178,-1,2178,2179,2211,-1,2212,2211,2179,-1,2179,2180,2212,-1,2213,2212,2180,-1,2180,2181,2213,-1,2214,2213,2181,-1,2181,2182,2214,-1,2215,2214,2182,-1,2182,2183,2215,-1,2216,2215,2183,-1,2183,2184,2216,-1,2217,2216,2184,-1,2184,2185,2217,-1,2218,2217,2185,-1,2185,2186,2218,-1,2219,2218,2186,-1,2186,2187,2219,-1,2220,2219,2187,-1,2187,2188,2220,-1,2221,2220,2188,-1,2188,2189,2221,-1,2222,2221,2189,-1,2189,2190,2222,-1,2223,2222,2190,-1,2190,2191,2223,-1,2224,2223,2191,-1,2191,2192,2224,-1,2225,2224,2192,-1,2192,2193,2225,-1,2226,2225,2193,-1,2193,2194,2226,-1,2227,2226,2194,-1,2194,2195,2227,-1,2228,2227,2195,-1,2195,2196,2228,-1,2229,2228,2196,-1,2196,2197,2229,-1,2230,2229,2197,-1,2197,2198,2230,-1,2231,2230,2198,-1,2198,2199,2231,-1,2232,2231,2199,-1,2199,2200,2232,-1,2233,2232,2200,-1,2200,2201,2233,-1,2234,2233,2201,-1,2201,2202,2234,-1,2235,2234,2202,-1,2202,2203,2235,-1,2205,2204,2236,-1,2237,2236,2204,-1,2204,2206,2237,-1,2238,2237,2206,-1,2206,2207,2238,-1,2239,2238,2207,-1,2207,2208,2239,-1,2210,2211,2240,-1,2241,2240,2211,-1,2211,2212,2241,-1,2242,2241,2212,-1,2212,2213,2242,-1,2243,2242,2213,-1,2213,2214,2243,-1,2244,2243,2214,-1,2214,2215,2244,-1,2245,2244,2215,-1,2215,2216,2245,-1,2246,2245,2216,-1,2216,2217,2246,-1,2247,2246,2217,-1,2217,2218,2247,-1,2248,2247,2218,-1,2218,2219,2248,-1,2249,2248,2219,-1,2219,2220,2249,-1,2250,2249,2220,-1,2220,2221,2250,-1,2251,2250,2221,-1,2221,2222,2251,-1,2252,2251,2222,-1,2222,2223,2252,-1,2253,2252,2223,-1,2223,2224,2253,-1,2254,2253,2224,-1,2224,2225,2254,-1,2255,2254,2225,-1,2225,2226,2255,-1,2256,2255,2226,-1,2226,2227,2256,-1,2257,2256,2227,-1,2227,2228,2257,-1,2258,2257,2228,-1,2228,2229,2258,-1,2259,2258,2229,-1,2229,2230,2259,-1,2260,2259,2230,-1,2230,2231,2260,-1,2261,2260,2231,-1,2231,2232,2261,-1,2262,2261,2232,-1,2232,2233,2262,-1,2263,2262,2233,-1,2233,2234,2263,-1,2264,2263,2234,-1,2234,2235,2264,-1]
IndexedFaceSet517.creaseAngle = 1.57
IndexedFaceSet517.solid = False
Coordinate518 = x3d.Coordinate()

IndexedFaceSet517.coord = Coordinate518
TextureCoordinate519 = x3d.TextureCoordinate()

IndexedFaceSet517.texCoord = TextureCoordinate519

Shape513.geometry = IndexedFaceSet517

Transform512.children.append(Shape513)

fieldValue511.children.append(Transform512)

ProtoInstance509.fieldValue.append(fieldValue511)

fieldValue508.children.append(ProtoInstance509)

ProtoInstance504.fieldValue.append(fieldValue508)

fieldValue493.children.append(ProtoInstance504)

ProtoInstance490.fieldValue.append(fieldValue493)

fieldValue397.children.append(ProtoInstance490)

ProtoInstance394.fieldValue.append(fieldValue397)

fieldValue297.children.append(ProtoInstance394)

ProtoInstance294.fieldValue.append(fieldValue297)

fieldValue293.children.append(ProtoInstance294)
Group520 = x3d.Group()

fieldValue293.children.append(Group520)

ProtoInstance292.fieldValue.append(fieldValue293)
fieldValue521 = x3d.fieldValue()
fieldValue521.name = "joints"
ProtoInstance522 = x3d.ProtoInstance()
ProtoInstance522.USE = "Allen_hanim_humanoid_root"

fieldValue521.children.append(ProtoInstance522)
ProtoInstance523 = x3d.ProtoInstance()
ProtoInstance523.USE = "Allen_hanim_sacroiliac"

fieldValue521.children.append(ProtoInstance523)
ProtoInstance524 = x3d.ProtoInstance()
ProtoInstance524.USE = "Allen_hanim_l_hip"

fieldValue521.children.append(ProtoInstance524)
ProtoInstance525 = x3d.ProtoInstance()
ProtoInstance525.USE = "Allen_hanim_l_knee"

fieldValue521.children.append(ProtoInstance525)
ProtoInstance526 = x3d.ProtoInstance()
ProtoInstance526.USE = "Allen_hanim_l_ankle"

fieldValue521.children.append(ProtoInstance526)
ProtoInstance527 = x3d.ProtoInstance()
ProtoInstance527.USE = "Allen_hanim_r_hip"

fieldValue521.children.append(ProtoInstance527)
ProtoInstance528 = x3d.ProtoInstance()
ProtoInstance528.USE = "Allen_hanim_r_knee"

fieldValue521.children.append(ProtoInstance528)
ProtoInstance529 = x3d.ProtoInstance()
ProtoInstance529.USE = "Allen_hanim_r_ankle"

fieldValue521.children.append(ProtoInstance529)
ProtoInstance530 = x3d.ProtoInstance()
ProtoInstance530.USE = "Allen_hanim_vl1"

fieldValue521.children.append(ProtoInstance530)
ProtoInstance531 = x3d.ProtoInstance()
ProtoInstance531.USE = "Allen_hanim_l_shoulder"

fieldValue521.children.append(ProtoInstance531)
ProtoInstance532 = x3d.ProtoInstance()
ProtoInstance532.USE = "Allen_hanim_l_elbow"

fieldValue521.children.append(ProtoInstance532)
ProtoInstance533 = x3d.ProtoInstance()
ProtoInstance533.USE = "Allen_hanim_l_wrist"

fieldValue521.children.append(ProtoInstance533)
ProtoInstance534 = x3d.ProtoInstance()
ProtoInstance534.USE = "Allen_hanim_r_shoulder"

fieldValue521.children.append(ProtoInstance534)
ProtoInstance535 = x3d.ProtoInstance()
ProtoInstance535.USE = "Allen_hanim_r_elbow"

fieldValue521.children.append(ProtoInstance535)
ProtoInstance536 = x3d.ProtoInstance()
ProtoInstance536.USE = "Allen_hanim_r_wrist"

fieldValue521.children.append(ProtoInstance536)
ProtoInstance537 = x3d.ProtoInstance()
ProtoInstance537.USE = "Allen_hanim_vc4"

fieldValue521.children.append(ProtoInstance537)
ProtoInstance538 = x3d.ProtoInstance()
ProtoInstance538.USE = "Allen_hanim_skullbase"

fieldValue521.children.append(ProtoInstance538)

ProtoInstance292.fieldValue.append(fieldValue521)
fieldValue539 = x3d.fieldValue()
fieldValue539.name = "segments"
ProtoInstance540 = x3d.ProtoInstance()
ProtoInstance540.USE = "Allen_hanim_pelvis"

fieldValue539.children.append(ProtoInstance540)
ProtoInstance541 = x3d.ProtoInstance()
ProtoInstance541.USE = "Allen_hanim_l_thigh"

fieldValue539.children.append(ProtoInstance541)
ProtoInstance542 = x3d.ProtoInstance()
ProtoInstance542.USE = "Allen_hanim_l_calf"

fieldValue539.children.append(ProtoInstance542)
ProtoInstance543 = x3d.ProtoInstance()
ProtoInstance543.USE = "Allen_hanim_l_hindfoot"

fieldValue539.children.append(ProtoInstance543)
ProtoInstance544 = x3d.ProtoInstance()
ProtoInstance544.USE = "Allen_hanim_r_thigh"

fieldValue539.children.append(ProtoInstance544)
ProtoInstance545 = x3d.ProtoInstance()
ProtoInstance545.USE = "Allen_hanim_r_calf"

fieldValue539.children.append(ProtoInstance545)
ProtoInstance546 = x3d.ProtoInstance()
ProtoInstance546.USE = "Allen_hanim_r_hindfoot"

fieldValue539.children.append(ProtoInstance546)
ProtoInstance547 = x3d.ProtoInstance()
ProtoInstance547.USE = "Allen_hanim_c7"

fieldValue539.children.append(ProtoInstance547)
ProtoInstance548 = x3d.ProtoInstance()
ProtoInstance548.USE = "Allen_hanim_l_upperarm"

fieldValue539.children.append(ProtoInstance548)
ProtoInstance549 = x3d.ProtoInstance()
ProtoInstance549.USE = "Allen_hanim_l_forearm"

fieldValue539.children.append(ProtoInstance549)
ProtoInstance550 = x3d.ProtoInstance()
ProtoInstance550.USE = "Allen_hanim_l_hand"

fieldValue539.children.append(ProtoInstance550)
ProtoInstance551 = x3d.ProtoInstance()
ProtoInstance551.USE = "Allen_hanim_r_upperarm"

fieldValue539.children.append(ProtoInstance551)
ProtoInstance552 = x3d.ProtoInstance()
ProtoInstance552.USE = "Allen_hanim_r_forearm"

fieldValue539.children.append(ProtoInstance552)
ProtoInstance553 = x3d.ProtoInstance()
ProtoInstance553.USE = "Allen_hanim_r_hand"

fieldValue539.children.append(ProtoInstance553)
ProtoInstance554 = x3d.ProtoInstance()
ProtoInstance554.USE = "Allen_hanim_c4"

fieldValue539.children.append(ProtoInstance554)
ProtoInstance555 = x3d.ProtoInstance()
ProtoInstance555.USE = "Allen_hanim_skull"

fieldValue539.children.append(ProtoInstance555)

ProtoInstance292.fieldValue.append(fieldValue539)

Switch291.children.append(ProtoInstance292)
ProtoInstance556 = x3d.ProtoInstance()
ProtoInstance556.name = "Humanoid1_1"
ProtoInstance556.DEF = "Nancy"
fieldValue557 = x3d.fieldValue()
fieldValue557.name = "name"
fieldValue557.value = "nancy"

ProtoInstance556.fieldValue.append(fieldValue557)
fieldValue558 = x3d.fieldValue()
fieldValue558.name = "version"
fieldValue558.value = "1.1"

ProtoInstance556.fieldValue.append(fieldValue558)
fieldValue559 = x3d.fieldValue()
fieldValue559.name = "info"
fieldValue559.value = "\"humanoidVersion=Nancy V1.2b\" \"authorName=Cindy Ballreich\" \"authorEmail=cindy@ballreich.net\" \"copyright=1997 3Name3D / Yglesias Wallock Divekar Inc. all rights reserved.\" \"creationDate=Tue Dec 30 08:30:08 PST 1997\" \"usageRestrictions=Noncommercial usage is ok if 3Name3D name and logo www.ballreich.net/vrml/HAnim/small_logo.gif is present and proper credit is given.\""

ProtoInstance556.fieldValue.append(fieldValue559)
fieldValue560 = x3d.fieldValue()
fieldValue560.name = "humanoidBody"
ProtoInstance561 = x3d.ProtoInstance()
ProtoInstance561.name = "Joint"
ProtoInstance561.DEF = "Nancy_hanim_humanoid_root"
fieldValue562 = x3d.fieldValue()
fieldValue562.name = "name"
fieldValue562.value = "humanoid_root"

ProtoInstance561.fieldValue.append(fieldValue562)
fieldValue563 = x3d.fieldValue()
fieldValue563.name = "center"
fieldValue563.value = "-0.00405 0.855 -0.000113"

ProtoInstance561.fieldValue.append(fieldValue563)
fieldValue564 = x3d.fieldValue()
fieldValue564.name = "children"
ProtoInstance565 = x3d.ProtoInstance()
ProtoInstance565.name = "Joint"
ProtoInstance565.DEF = "Nancy_hanim_sacroiliac"
fieldValue566 = x3d.fieldValue()
fieldValue566.name = "name"
fieldValue566.value = "sacroiliac"

ProtoInstance565.fieldValue.append(fieldValue566)
fieldValue567 = x3d.fieldValue()
fieldValue567.name = "center"
fieldValue567.value = "0 1.01 -0.0204"

ProtoInstance565.fieldValue.append(fieldValue567)
fieldValue568 = x3d.fieldValue()
fieldValue568.name = "children"
ProtoInstance569 = x3d.ProtoInstance()
ProtoInstance569.name = "Segment"
ProtoInstance569.DEF = "Nancy_hanim_pelvis"
fieldValue570 = x3d.fieldValue()
fieldValue570.name = "name"
fieldValue570.value = "pelvis"

ProtoInstance569.fieldValue.append(fieldValue570)
fieldValue571 = x3d.fieldValue()
fieldValue571.name = "children"
Shape572 = x3d.Shape()
Appearance573 = x3d.Appearance()
Material574 = x3d.Material()
Material574.USE = "Pants_Color"

Appearance573.material = Material574

Shape572.appearance = Appearance573
IndexedFaceSet575 = x3d.IndexedFaceSet()
IndexedFaceSet575.coordIndex = [0,1,40,-1,1,2,40,-1,2,3,40,-1,3,4,40,-1,4,5,40,-1,5,4,9,-1,4,3,8,-1,3,2,8,-1,2,1,6,-1,0,7,1,-1,7,6,1,-1,6,8,2,-1,9,4,10,-1,4,8,10,-1,8,6,12,-1,7,0,47,-1,50,5,9,-1,7,47,55,-1,55,13,7,-1,50,9,56,-1,9,10,14,-1,10,11,15,-1,11,12,16,-1,12,13,19,-1,13,55,17,-1,60,17,55,-1,17,19,13,-1,19,16,12,-1,16,15,11,-1,15,18,10,-1,14,56,9,-1,56,14,64,-1,17,60,20,-1,20,19,17,-1,21,64,14,-1,14,22,21,-1,15,16,24,-1,16,19,24,-1,19,20,26,-1,24,23,15,-1,64,21,69,-1,21,22,29,-1,19,26,25,-1,20,63,27,-1,27,26,20,-1,25,24,19,-1,30,29,22,-1,29,28,21,-1,28,69,21,-1,27,34,26,-1,69,28,79,-1,29,30,32,-1,30,23,33,-1,23,24,37,-1,25,26,34,-1,83,27,77,-1,37,33,23,-1,33,32,30,-1,31,79,28,-1,79,31,84,-1,32,33,36,-1,24,25,37,-1,34,27,83,-1,83,38,34,-1,34,37,25,-1,37,36,33,-1,36,35,32,-1,84,31,89,-1,31,35,89,-1,35,36,39,-1,36,37,39,-1,38,83,89,-1,89,39,38,-1,39,89,35,-1,40,41,0,-1,40,42,41,-1,40,43,42,-1,40,44,43,-1,40,45,44,-1,49,44,45,-1,48,43,44,-1,48,42,43,-1,46,41,42,-1,41,47,0,-1,41,46,47,-1,42,48,46,-1,51,44,49,-1,51,48,44,-1,48,52,53,-1,49,45,50,-1,56,49,50,-1,57,51,49,-1,58,53,52,-1,59,54,53,-1,62,55,54,-1,55,62,60,-1,54,59,62,-1,53,58,59,-1,51,61,58,-1,49,56,57,-1,64,57,56,-1,67,59,58,-1,68,62,59,-1,60,63,20,-1,60,62,63,-1,59,67,68,-1,58,61,67,-1,57,64,65,-1,65,66,57,-1,71,63,62,-1,69,65,64,-1,74,66,65,-1,78,68,67,-1,70,71,62,-1,63,72,27,-1,63,71,72,-1,68,78,76,-1,67,75,78,-1,66,74,75,-1,65,73,74,-1,65,69,73,-1,77,27,72,-1,71,82,72,-1,79,73,69,-1,81,75,74,-1,82,71,70,-1,77,72,83,-1,73,79,80,-1,84,80,79,-1,86,75,81,-1,83,72,82,-1,82,88,83,-1,70,87,82,-1,81,85,86,-1,89,80,84,-1,89,85,80,-1,90,86,85,-1,90,87,86,-1,89,83,88,-1,88,90,89,-1,85,89,90,-1,50,45,5,-1,45,40,5,-1,10,8,11,-1,8,12,11,-1,18,22,10,-1,22,14,10,-1,57,66,51,-1,66,61,51,-1,51,58,48,-1,58,52,48,-1,48,53,46,-1,53,54,46,-1,76,70,68,-1,70,62,68,-1,29,32,28,-1,28,32,31,-1,32,35,31,-1,85,81,80,-1,81,73,80,-1,81,74,73,-1,39,37,38,-1,37,34,38,-1,82,87,88,-1,87,90,88,-1,87,78,86,-1,78,75,86,-1,61,66,67,-1,66,75,67,-1,22,18,15,-1,23,30,15,-1,30,22,15,-1,13,12,7,-1,12,6,7,-1,46,54,47,-1,54,55,47,-1,87,76,78,-1,87,70,76,-1]
IndexedFaceSet575.creaseAngle = 1.14
Coordinate576 = x3d.Coordinate()

IndexedFaceSet575.coord = Coordinate576

Shape572.geometry = IndexedFaceSet575

fieldValue571.children.append(Shape572)

ProtoInstance569.fieldValue.append(fieldValue571)

fieldValue568.children.append(ProtoInstance569)
ProtoInstance577 = x3d.ProtoInstance()
ProtoInstance577.name = "Joint"
ProtoInstance577.DEF = "Nancy_hanim_l_hip"
fieldValue578 = x3d.fieldValue()
fieldValue578.name = "name"
fieldValue578.value = "l_hip"

ProtoInstance577.fieldValue.append(fieldValue578)
fieldValue579 = x3d.fieldValue()
fieldValue579.name = "center"
fieldValue579.value = "0.122 0.888271 -0.0693267"

ProtoInstance577.fieldValue.append(fieldValue579)
fieldValue580 = x3d.fieldValue()
fieldValue580.name = "children"
ProtoInstance581 = x3d.ProtoInstance()
ProtoInstance581.name = "Segment"
ProtoInstance581.DEF = "Nancy_hanim_l_thigh"
fieldValue582 = x3d.fieldValue()
fieldValue582.name = "name"
fieldValue582.value = "l_thigh"

ProtoInstance581.fieldValue.append(fieldValue582)
fieldValue583 = x3d.fieldValue()
fieldValue583.name = "children"
Shape584 = x3d.Shape()
Appearance585 = x3d.Appearance()
Material586 = x3d.Material()
Material586.USE = "Pants_Color"

Appearance585.material = Material586

Shape584.appearance = Appearance585
IndexedFaceSet587 = x3d.IndexedFaceSet()
IndexedFaceSet587.coordIndex = [0,4,5,-1,3,4,0,-1,0,7,1,-1,0,8,7,-1,0,6,8,-1,0,5,6,-1,0,2,3,-1,0,1,2,-1,9,2,1,-1,10,3,2,-1,11,4,3,-1,12,5,4,-1,13,6,5,-1,15,7,8,-1,9,1,7,-1,7,15,9,-1,8,14,15,-1,5,16,13,-1,5,12,16,-1,4,11,12,-1,3,10,11,-1,2,9,10,-1,20,13,16,-1,18,11,10,-1,19,12,11,-1,20,16,12,-1,23,15,14,-1,15,23,24,-1,12,19,20,-1,11,18,19,-1,10,17,18,-1,26,18,17,-1,27,19,18,-1,27,20,19,-1,28,21,20,-1,29,23,22,-1,23,29,30,-1,20,32,28,-1,20,27,32,-1,18,26,27,-1,17,25,26,-1,25,31,30,-1,30,29,26,-1,30,26,25,-1,29,28,27,-1,29,27,26,-1,28,32,27,-1,22,23,14,-1,20,21,13,-1,21,22,13,-1,22,14,13,-1,9,15,24,-1,10,9,17,-1,9,24,17,-1,6,13,8,-1,13,14,8,-1,28,29,21,-1,29,22,21,-1,24,31,17,-1,31,25,17,-1,30,31,23,-1,31,24,23,-1]
IndexedFaceSet587.creaseAngle = 1.32
Coordinate588 = x3d.Coordinate()

IndexedFaceSet587.coord = Coordinate588

Shape584.geometry = IndexedFaceSet587

fieldValue583.children.append(Shape584)

ProtoInstance581.fieldValue.append(fieldValue583)

fieldValue580.children.append(ProtoInstance581)
ProtoInstance589 = x3d.ProtoInstance()
ProtoInstance589.name = "Joint"
ProtoInstance589.DEF = "Nancy_hanim_l_knee"
fieldValue590 = x3d.fieldValue()
fieldValue590.name = "name"
fieldValue590.value = "l_knee"

ProtoInstance589.fieldValue.append(fieldValue590)
fieldValue591 = x3d.fieldValue()
fieldValue591.name = "center"
fieldValue591.value = "0.0738 0.517 -0.0284"

ProtoInstance589.fieldValue.append(fieldValue591)
fieldValue592 = x3d.fieldValue()
fieldValue592.name = "children"
ProtoInstance593 = x3d.ProtoInstance()
ProtoInstance593.name = "Segment"
ProtoInstance593.DEF = "Nancy_hanim_l_calf"
fieldValue594 = x3d.fieldValue()
fieldValue594.name = "name"
fieldValue594.value = "l_calf"

ProtoInstance593.fieldValue.append(fieldValue594)
fieldValue595 = x3d.fieldValue()
fieldValue595.name = "children"
Shape596 = x3d.Shape()
Appearance597 = x3d.Appearance()
Material598 = x3d.Material()
Material598.USE = "Pants_Color"

Appearance597.material = Material598

Shape596.appearance = Appearance597
IndexedFaceSet599 = x3d.IndexedFaceSet()
IndexedFaceSet599.coordIndex = [2,1,0,-1,2,3,1,-1,2,4,3,-1,2,5,4,-1,2,6,5,-1,2,7,6,-1,2,8,7,-1,2,0,8,-1,9,8,0,-1,10,6,7,-1,11,5,6,-1,12,4,5,-1,12,3,4,-1,13,1,3,-1,1,13,14,-1,3,12,13,-1,5,11,12,-1,6,10,11,-1,8,9,15,-1,22,13,12,-1,13,22,14,-1,17,15,9,-1,20,12,11,-1,21,22,12,-1,23,9,14,-1,9,23,16,-1,14,22,23,-1,12,20,21,-1,15,17,18,-1,9,16,17,-1,24,17,16,-1,25,18,17,-1,26,19,18,-1,27,20,19,-1,28,21,20,-1,29,22,21,-1,30,23,22,-1,31,16,23,-1,23,30,31,-1,22,29,30,-1,21,28,29,-1,20,27,28,-1,19,26,27,-1,18,25,26,-1,17,24,25,-1,16,31,24,-1,33,26,25,-1,36,29,28,-1,37,31,30,-1,29,36,30,-1,25,24,33,-1,31,37,24,-1,32,33,24,-1,24,37,32,-1,38,37,30,-1,30,36,38,-1,41,33,32,-1,42,39,34,-1,44,36,35,-1,45,38,36,-1,46,37,38,-1,38,45,46,-1,36,44,45,-1,35,43,44,-1,39,42,47,-1,32,40,41,-1,40,46,45,-1,41,40,45,-1,41,45,44,-1,44,43,42,-1,44,42,41,-1,43,47,42,-1,39,35,28,-1,35,36,28,-1,34,39,27,-1,39,28,27,-1,33,34,26,-1,34,27,26,-1,33,41,34,-1,41,42,34,-1,40,32,46,-1,32,37,46,-1,10,19,11,-1,19,20,11,-1,14,9,1,-1,9,0,1,-1,8,15,7,-1,7,15,10,-1,15,19,10,-1,15,18,19,-1,43,35,47,-1,35,39,47,-1]
IndexedFaceSet599.creaseAngle = 1.57
Coordinate600 = x3d.Coordinate()

IndexedFaceSet599.coord = Coordinate600

Shape596.geometry = IndexedFaceSet599

fieldValue595.children.append(Shape596)

ProtoInstance593.fieldValue.append(fieldValue595)

fieldValue592.children.append(ProtoInstance593)
ProtoInstance601 = x3d.ProtoInstance()
ProtoInstance601.name = "Joint"
ProtoInstance601.DEF = "Nancy_hanim_l_ankle"
fieldValue602 = x3d.fieldValue()
fieldValue602.name = "name"
fieldValue602.value = "l_ankle"

ProtoInstance601.fieldValue.append(fieldValue602)
fieldValue603 = x3d.fieldValue()
fieldValue603.name = "center"
fieldValue603.value = "0.0645 0.0719 -0.048"

ProtoInstance601.fieldValue.append(fieldValue603)
fieldValue604 = x3d.fieldValue()
fieldValue604.name = "children"
ProtoInstance605 = x3d.ProtoInstance()
ProtoInstance605.name = "Segment"
ProtoInstance605.DEF = "Nancy_hanim_l_hindfoot"
fieldValue606 = x3d.fieldValue()
fieldValue606.name = "name"
fieldValue606.value = "l_hindfoot"

ProtoInstance605.fieldValue.append(fieldValue606)
fieldValue607 = x3d.fieldValue()
fieldValue607.name = "children"
Shape608 = x3d.Shape()
Appearance609 = x3d.Appearance()
Material610 = x3d.Material()
Material610.USE = "Shoe_Color"

Appearance609.material = Material610

Shape608.appearance = Appearance609
IndexedFaceSet611 = x3d.IndexedFaceSet()
IndexedFaceSet611.coordIndex = [2,1,0,-1,4,3,1,-1,2,4,1,-1,3,6,5,-1,1,3,5,-1,6,8,7,-1,5,6,7,-1,8,10,9,-1,7,8,9,-1,10,12,11,-1,9,10,11,-1,12,14,13,-1,11,12,13,-1,14,16,15,-1,13,14,15,-1,16,18,17,-1,15,16,17,-1,18,20,19,-1,17,18,19,-1,20,22,21,-1,19,20,21,-1,22,24,23,-1,21,22,23,-1,24,25,0,-1,23,24,0,-1,25,4,2,-1,0,25,2,-1,18,26,20,-1,16,26,18,-1,27,26,16,-1,14,27,16,-1,12,27,14,-1,28,27,12,-1,29,28,12,-1,10,29,12,-1,8,29,10,-1,6,37,8,-1,24,30,25,-1,31,30,24,-1,22,31,24,-1,32,31,22,-1,20,32,22,-1,33,32,20,-1,26,33,20,-1,34,33,26,-1,27,34,26,-1,35,34,27,-1,28,35,27,-1,29,35,28,-1,36,35,29,-1,8,36,29,-1,37,36,8,-1,6,38,37,-1,3,38,6,-1,39,38,3,-1,30,39,25,-1,41,40,30,-1,31,41,30,-1,42,41,31,-1,32,42,31,-1,43,42,32,-1,33,43,32,-1,44,43,33,-1,34,44,33,-1,45,44,34,-1,35,45,34,-1,46,45,35,-1,36,46,35,-1,47,46,36,-1,37,47,36,-1,38,47,37,-1,48,47,38,-1,49,48,38,-1,39,49,38,-1,40,49,39,-1,30,40,39,-1,48,49,50,-1,47,48,50,-1,46,47,50,-1,45,46,50,-1,44,45,50,-1,43,44,50,-1,42,43,50,-1,41,42,50,-1,40,41,50,-1,49,40,50,-1,11,13,15,-1,11,15,17,-1,9,11,17,-1,9,17,19,-1,7,9,19,-1,7,19,21,-1,5,7,21,-1,5,21,23,-1,5,23,0,-1,1,5,0,-1,3,4,39,-1,4,25,39,-1]
IndexedFaceSet611.creaseAngle = 1.57
Coordinate612 = x3d.Coordinate()

IndexedFaceSet611.coord = Coordinate612

Shape608.geometry = IndexedFaceSet611

fieldValue607.children.append(Shape608)

ProtoInstance605.fieldValue.append(fieldValue607)

fieldValue604.children.append(ProtoInstance605)

ProtoInstance601.fieldValue.append(fieldValue604)

fieldValue592.children.append(ProtoInstance601)

ProtoInstance589.fieldValue.append(fieldValue592)

fieldValue580.children.append(ProtoInstance589)

ProtoInstance577.fieldValue.append(fieldValue580)

fieldValue568.children.append(ProtoInstance577)
ProtoInstance613 = x3d.ProtoInstance()
ProtoInstance613.name = "Joint"
ProtoInstance613.DEF = "Nancy_hanim_r_hip"
fieldValue614 = x3d.fieldValue()
fieldValue614.name = "name"
fieldValue614.value = "r_hip"

ProtoInstance613.fieldValue.append(fieldValue614)
fieldValue615 = x3d.fieldValue()
fieldValue615.name = "center"
fieldValue615.value = "-0.11 0.892362 -0.0732533"

ProtoInstance613.fieldValue.append(fieldValue615)
fieldValue616 = x3d.fieldValue()
fieldValue616.name = "children"
ProtoInstance617 = x3d.ProtoInstance()
ProtoInstance617.name = "Segment"
ProtoInstance617.DEF = "Nancy_hanim_r_thigh"
fieldValue618 = x3d.fieldValue()
fieldValue618.name = "name"
fieldValue618.value = "r_thigh"

ProtoInstance617.fieldValue.append(fieldValue618)
fieldValue619 = x3d.fieldValue()
fieldValue619.name = "children"
Shape620 = x3d.Shape()
Appearance621 = x3d.Appearance()
Material622 = x3d.Material()
Material622.USE = "Pants_Color"

Appearance621.material = Material622

Shape620.appearance = Appearance621
IndexedFaceSet623 = x3d.IndexedFaceSet()
IndexedFaceSet623.coordIndex = [5,4,0,-1,0,4,3,-1,1,7,0,-1,7,8,0,-1,8,6,0,-1,6,5,0,-1,3,2,0,-1,2,1,0,-1,1,2,9,-1,2,3,10,-1,3,4,11,-1,4,5,12,-1,5,6,13,-1,8,7,15,-1,7,1,9,-1,9,15,7,-1,15,14,8,-1,13,16,5,-1,16,12,5,-1,12,11,4,-1,11,10,3,-1,10,9,2,-1,12,16,20,-1,13,14,22,-1,14,15,23,-1,24,23,15,-1,23,22,14,-1,20,19,12,-1,17,18,26,-1,18,19,27,-1,19,20,27,-1,20,21,28,-1,22,23,29,-1,30,29,23,-1,27,26,18,-1,26,25,17,-1,30,31,25,-1,25,26,29,-1,25,29,30,-1,26,27,28,-1,26,28,29,-1,27,20,28,-1,24,15,9,-1,22,21,13,-1,29,28,22,-1,28,21,22,-1,24,31,23,-1,31,30,23,-1,25,31,17,-1,31,24,17,-1,17,24,10,-1,24,9,10,-1,18,10,11,-1,18,17,10,-1,18,12,19,-1,18,11,12,-1,21,20,13,-1,20,16,13,-1,14,13,8,-1,13,6,8,-1]
IndexedFaceSet623.creaseAngle = 1.61
Coordinate624 = x3d.Coordinate()

IndexedFaceSet623.coord = Coordinate624

Shape620.geometry = IndexedFaceSet623

fieldValue619.children.append(Shape620)

ProtoInstance617.fieldValue.append(fieldValue619)

fieldValue616.children.append(ProtoInstance617)
ProtoInstance625 = x3d.ProtoInstance()
ProtoInstance625.name = "Joint"
ProtoInstance625.DEF = "Nancy_hanim_r_knee"
fieldValue626 = x3d.fieldValue()
fieldValue626.name = "name"
fieldValue626.value = "r_knee"

ProtoInstance625.fieldValue.append(fieldValue626)
fieldValue627 = x3d.fieldValue()
fieldValue627.name = "center"
fieldValue627.value = "-0.0699 0.51 -0.0166"

ProtoInstance625.fieldValue.append(fieldValue627)
fieldValue628 = x3d.fieldValue()
fieldValue628.name = "children"
ProtoInstance629 = x3d.ProtoInstance()
ProtoInstance629.name = "Segment"
ProtoInstance629.DEF = "Nancy_hanim_r_calf"
fieldValue630 = x3d.fieldValue()
fieldValue630.name = "name"
fieldValue630.value = "r_calf"

ProtoInstance629.fieldValue.append(fieldValue630)
fieldValue631 = x3d.fieldValue()
fieldValue631.name = "children"
Shape632 = x3d.Shape()
Appearance633 = x3d.Appearance()
Material634 = x3d.Material()
Material634.USE = "Pants_Color"

Appearance633.material = Material634

Shape632.appearance = Appearance633
IndexedFaceSet635 = x3d.IndexedFaceSet()
IndexedFaceSet635.coordIndex = [14,25,18,-1,25,32,18,-1,32,27,18,-1,27,22,18,-1,22,10,18,-1,10,6,18,-1,6,8,18,-1,8,14,18,-1,14,8,17,-1,6,10,9,-1,10,22,24,-1,22,27,39,-1,27,32,39,-1,32,25,42,-1,25,14,30,-1,17,30,14,-1,30,42,25,-1,42,39,32,-1,39,24,22,-1,24,9,10,-1,4,17,8,-1,39,42,43,-1,30,43,42,-1,17,4,1,-1,24,39,26,-1,39,43,44,-1,30,17,34,-1,16,34,17,-1,34,43,30,-1,44,26,39,-1,0,1,4,-1,1,16,17,-1,16,1,3,-1,1,0,2,-1,0,5,7,-1,5,26,28,-1,26,44,45,-1,44,43,46,-1,43,34,36,-1,34,16,15,-1,15,36,34,-1,36,46,43,-1,46,45,44,-1,45,28,26,-1,28,7,5,-1,7,2,0,-1,2,3,1,-1,3,15,16,-1,45,46,37,-1,36,15,20,-1,36,37,46,-1,13,2,7,-1,3,20,15,-1,3,2,13,-1,36,20,29,-1,29,37,36,-1,13,21,23,-1,21,33,23,-1,41,37,40,-1,37,29,31,-1,29,20,19,-1,19,31,29,-1,31,40,37,-1,40,38,41,-1,35,23,33,-1,23,12,13,-1,12,11,13,-1,31,19,11,-1,40,31,11,-1,40,11,12,-1,12,23,38,-1,12,38,40,-1,23,35,38,-1,28,21,7,-1,21,13,7,-1,45,33,28,-1,33,21,28,-1,33,45,41,-1,45,37,41,-1,33,41,35,-1,41,38,35,-1,20,3,47,-1,11,19,47,-1,19,20,47,-1,13,47,3,-1,13,11,47,-1,4,8,6,-1,26,5,24,-1,5,9,24,-1,6,9,4,-1,9,0,4,-1,9,5,0,-1]
IndexedFaceSet635.creaseAngle = 1.57
Coordinate636 = x3d.Coordinate()

IndexedFaceSet635.coord = Coordinate636

Shape632.geometry = IndexedFaceSet635

fieldValue631.children.append(Shape632)

ProtoInstance629.fieldValue.append(fieldValue631)

fieldValue628.children.append(ProtoInstance629)
ProtoInstance637 = x3d.ProtoInstance()
ProtoInstance637.name = "Joint"
ProtoInstance637.DEF = "Nancy_hanim_r_ankle"
fieldValue638 = x3d.fieldValue()
fieldValue638.name = "name"
fieldValue638.value = "r_ankle"

ProtoInstance637.fieldValue.append(fieldValue638)
fieldValue639 = x3d.fieldValue()
fieldValue639.name = "center"
fieldValue639.value = "-0.064 0.0753 -0.0412"

ProtoInstance637.fieldValue.append(fieldValue639)
fieldValue640 = x3d.fieldValue()
fieldValue640.name = "children"
ProtoInstance641 = x3d.ProtoInstance()
ProtoInstance641.name = "Segment"
ProtoInstance641.DEF = "Nancy_hanim_r_hindfoot"
fieldValue642 = x3d.fieldValue()
fieldValue642.name = "name"
fieldValue642.value = "r_hindfoot"

ProtoInstance641.fieldValue.append(fieldValue642)
fieldValue643 = x3d.fieldValue()
fieldValue643.name = "children"
Shape644 = x3d.Shape()
Appearance645 = x3d.Appearance()
Material646 = x3d.Material()
Material646.USE = "Shoe_Color"

Appearance645.material = Material646

Shape644.appearance = Appearance645
IndexedFaceSet647 = x3d.IndexedFaceSet()
IndexedFaceSet647.coordIndex = [6,50,0,-1,50,8,7,-1,50,7,0,-1,1,9,8,-1,1,8,50,-1,49,10,9,-1,49,9,1,-1,46,11,10,-1,46,10,49,-1,2,12,11,-1,2,11,46,-1,3,13,12,-1,3,12,2,-1,4,14,13,-1,4,13,3,-1,45,14,4,-1,47,15,45,-1,19,15,47,-1,48,18,19,-1,5,16,18,-1,5,18,48,-1,6,17,16,-1,6,16,5,-1,0,7,17,-1,0,17,6,-1,14,20,21,-1,14,21,13,-1,13,21,12,-1,12,21,22,-1,12,22,11,-1,11,22,10,-1,17,23,16,-1,16,23,24,-1,16,24,18,-1,18,24,25,-1,18,25,19,-1,19,25,26,-1,19,26,15,-1,15,26,20,-1,20,26,27,-1,20,27,21,-1,21,27,28,-1,21,28,22,-1,22,28,29,-1,10,30,9,-1,9,30,31,-1,9,31,8,-1,8,31,32,-1,17,32,23,-1,23,33,34,-1,23,34,35,-1,23,35,24,-1,24,35,36,-1,24,36,25,-1,25,36,37,-1,25,37,26,-1,26,37,38,-1,26,38,27,-1,27,38,39,-1,27,39,28,-1,28,39,40,-1,28,40,29,-1,29,40,41,-1,29,41,30,-1,30,41,42,-1,30,42,31,-1,31,42,43,-1,31,43,32,-1,32,43,33,-1,32,33,23,-1,44,43,42,-1,44,42,41,-1,44,41,40,-1,44,40,39,-1,44,39,38,-1,44,38,37,-1,44,37,36,-1,44,36,35,-1,44,35,34,-1,44,34,33,-1,44,33,43,-1,4,3,2,-1,45,4,2,-1,45,2,46,-1,47,45,46,-1,48,46,49,-1,5,48,49,-1,5,49,1,-1,6,5,1,-1,6,1,50,-1,30,10,29,-1,10,22,29,-1,17,7,32,-1,7,8,32,-1,19,47,48,-1,47,46,48,-1,20,14,15,-1,14,45,15,-1]
IndexedFaceSet647.creaseAngle = 1.57
Coordinate648 = x3d.Coordinate()

IndexedFaceSet647.coord = Coordinate648

Shape644.geometry = IndexedFaceSet647

fieldValue643.children.append(Shape644)

ProtoInstance641.fieldValue.append(fieldValue643)

fieldValue640.children.append(ProtoInstance641)

ProtoInstance637.fieldValue.append(fieldValue640)

fieldValue628.children.append(ProtoInstance637)

ProtoInstance625.fieldValue.append(fieldValue628)

fieldValue616.children.append(ProtoInstance625)

ProtoInstance613.fieldValue.append(fieldValue616)

fieldValue568.children.append(ProtoInstance613)

ProtoInstance565.fieldValue.append(fieldValue568)

fieldValue564.children.append(ProtoInstance565)
ProtoInstance649 = x3d.ProtoInstance()
ProtoInstance649.name = "Joint"
ProtoInstance649.DEF = "Nancy_hanim_vl1"
fieldValue650 = x3d.fieldValue()
fieldValue650.name = "name"
fieldValue650.value = "vl1"

ProtoInstance649.fieldValue.append(fieldValue650)
fieldValue651 = x3d.fieldValue()
fieldValue651.name = "center"
fieldValue651.value = "-0.00405 1.07 -0.0275"

ProtoInstance649.fieldValue.append(fieldValue651)
fieldValue652 = x3d.fieldValue()
fieldValue652.name = "children"
ProtoInstance653 = x3d.ProtoInstance()
ProtoInstance653.name = "Segment"
ProtoInstance653.DEF = "Nancy_hanim_c7"
fieldValue654 = x3d.fieldValue()
fieldValue654.name = "name"
fieldValue654.value = "l1"

ProtoInstance653.fieldValue.append(fieldValue654)
fieldValue655 = x3d.fieldValue()
fieldValue655.name = "children"
Shape656 = x3d.Shape()
Appearance657 = x3d.Appearance()
Material658 = x3d.Material()
Material658.USE = "Shirt_Color"

Appearance657.material = Material658
ImageTexture659 = x3d.ImageTexture()
ImageTexture659.DEF = "small_logo_Tex"
ImageTexture659.url = ["small_logo.gif","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/small_logo.gif"]

Appearance657.texture = ImageTexture659

Shape656.appearance = Appearance657
IndexedFaceSet660 = x3d.IndexedFaceSet()
IndexedFaceSet660.coordIndex = [0,1,2,-1,3,0,2,-1,4,5,6,-1,6,7,4,-1,8,7,6,-1,6,9,8,-1,9,10,8,-1,6,5,11,-1,9,6,12,-1,11,12,6,-1,12,10,9,-1,7,8,13,-1,13,4,7,-1,14,15,16,-1,15,17,13,-1,4,13,17,-1,17,15,18,-1,13,19,15,-1,19,13,8,-1,19,16,15,-1,16,19,8,-1,17,20,4,-1,5,4,20,-1,18,21,17,-1,20,17,21,-1,16,22,14,-1,22,16,23,-1,8,23,16,-1,23,8,10,-1,24,25,26,-1,26,27,24,-1,25,28,26,-1,28,29,30,-1,30,26,28,-1,31,32,33,-1,32,25,33,-1,25,24,34,-1,33,25,34,-1,24,35,34,-1,27,35,24,-1,33,36,31,-1,27,26,37,-1,37,26,30,-1,38,37,30,-1,33,34,39,-1,39,34,35,-1,39,35,40,-1,41,38,30,-1,35,27,42,-1,37,42,27,-1,40,35,42,-1,42,37,43,-1,37,38,44,-1,44,43,37,-1,36,45,46,-1,36,33,45,-1,40,42,47,-1,43,47,42,-1,47,48,40,-1,39,40,48,-1,47,43,49,-1,43,44,49,-1,50,49,44,-1,51,46,52,-1,46,45,52,-1,52,45,53,-1,33,53,45,-1,33,39,53,-1,49,54,47,-1,48,47,54,-1,55,56,52,-1,57,52,53,-1,57,55,52,-1,58,57,53,-1,59,58,53,-1,53,39,59,-1,39,48,59,-1,59,48,54,-1,58,59,60,-1,54,49,61,-1,59,54,61,-1,60,59,61,-1,49,50,62,-1,63,62,50,-1,62,61,49,-1,64,63,50,-1,63,64,65,-1,65,62,63,-1,66,60,61,-1,62,65,67,-1,68,67,65,-1,64,69,70,-1,64,70,65,-1,70,68,65,-1,69,71,72,-1,72,70,69,-1,73,74,75,-1,66,76,60,-1,67,77,62,-1,62,77,61,-1,77,66,61,-1,66,77,78,-1,77,67,79,-1,79,67,68,-1,79,78,77,-1,68,70,80,-1,70,72,80,-1,80,79,68,-1,74,73,81,-1,73,76,82,-1,82,81,73,-1,76,66,83,-1,78,83,66,-1,83,82,76,-1,78,79,84,-1,79,80,84,-1,84,85,78,-1,86,84,80,-1,81,82,87,-1,87,88,81,-1,82,83,89,-1,83,78,89,-1,89,87,82,-1,78,85,89,-1,90,91,92,-1,92,93,90,-1,90,94,91,-1,95,96,94,-1,94,90,95,-1,29,96,97,-1,96,95,97,-1,97,30,29,-1,30,97,41,-1,41,97,95,-1,98,99,100,-1,98,91,99,-1,101,92,91,-1,98,101,91,-1,101,102,92,-1,92,102,93,-1,36,103,31,-1,51,103,36,46,-1,103,100,31,-1,100,103,98,-1,104,90,93,-1,90,104,95,-1,95,105,41,-1,104,105,95,-1,106,101,98,-1,102,101,106,-1,107,93,102,-1,93,107,104,-1,108,104,107,-1,107,109,108,-1,110,105,104,-1,104,108,110,-1,109,107,111,-1,107,102,111,-1,111,102,106,-1,111,112,109,-1,106,112,111,-1,113,110,108,-1,110,113,114,-1,51,52,115,-1,116,115,117,-1,117,106,116,-1,118,109,112,-1,119,108,109,-1,108,119,113,-1,109,118,119,-1,120,113,119,-1,119,121,120,-1,52,56,122,-1,122,115,52,-1,115,122,123,-1,117,124,125,-1,106,117,125,-1,118,112,106,125,-1,119,118,125,-1,121,119,125,-1,126,124,123,-1,127,114,113,-1,114,127,128,-1,113,120,127,-1,114,128,129,-1,130,126,123,-1,122,130,123,-1,131,120,121,-1,131,127,120,-1,132,129,128,-1,128,127,132,-1,74,81,133,-1,81,134,133,-1,121,135,131,-1,136,132,127,-1,132,136,137,-1,138,71,129,-1,138,129,132,-1,137,138,132,-1,139,72,71,-1,72,139,80,-1,71,138,139,-1,140,135,121,-1,140,121,125,-1,141,127,131,-1,127,141,136,-1,131,135,141,-1,142,141,135,-1,143,136,141,-1,136,143,137,-1,141,142,143,-1,144,138,137,-1,144,139,138,-1,143,144,137,-1,145,146,134,-1,145,140,146,-1,134,81,145,-1,147,135,140,-1,135,147,142,-1,140,145,147,-1,148,80,139,-1,80,148,86,-1,139,144,148,-1,149,143,142,-1,149,144,143,-1,142,150,149,-1,151,148,144,-1,144,149,151,-1,152,145,81,-1,81,88,152,-1,153,147,145,-1,153,142,147,-1,145,152,153,-1,153,150,142,-1,154,86,148,-1,148,151,154,-1,155,28,25,-1,155,29,28,-1,155,25,32,-1,155,32,31,-1,155,31,100,-1,155,100,99,-1,155,99,91,-1,155,91,94,-1,155,94,96,-1,155,96,29,-1,156,151,149,-1,156,154,151,-1,156,149,150,-1,156,150,153,-1,156,153,152,-1,156,152,88,-1,156,88,87,-1,156,87,89,-1,156,89,85,-1,156,85,84,-1,156,84,86,-1,156,86,154,-1,76,157,60,-1,76,73,158,157,-1,159,158,73,75,160,-1,161,56,55,-1,60,162,58,-1,162,60,157,-1,161,55,163,-1,57,164,163,55,-1,160,163,164,-1,160,164,159,-1,164,57,165,-1,164,165,159,-1,57,58,166,165,-1,166,58,162,-1,165,166,159,-1,166,162,157,158,159,-1,140,125,167,-1,124,168,125,-1,168,167,125,-1,124,169,168,-1,146,140,167,170,-1,168,170,167,-1,168,169,170,-1,146,170,171,-1,169,171,170,-1,172,134,146,171,-1,134,172,130,-1,169,124,126,173,-1,173,126,130,-1,169,173,172,171,-1,173,130,172,-1,122,74,133,174,-1,133,134,174,-1,130,122,174,-1,134,130,174,-1,122,56,175,74,-1,74,175,176,-1,175,56,161,176,-1,74,176,75,-1,176,161,163,-1,176,160,75,-1,176,163,160,-1,115,116,177,51,-1,106,98,177,116,-1,51,177,103,-1,177,98,103,-1]
IndexedFaceSet660.creaseAngle = 1.59
Coordinate661 = x3d.Coordinate()

IndexedFaceSet660.coord = Coordinate661
TextureCoordinate662 = x3d.TextureCoordinate()

IndexedFaceSet660.texCoord = TextureCoordinate662

Shape656.geometry = IndexedFaceSet660

fieldValue655.children.append(Shape656)

ProtoInstance653.fieldValue.append(fieldValue655)

fieldValue652.children.append(ProtoInstance653)
ProtoInstance663 = x3d.ProtoInstance()
ProtoInstance663.name = "Joint"
ProtoInstance663.DEF = "Nancy_hanim_l_shoulder"
fieldValue664 = x3d.fieldValue()
fieldValue664.name = "name"
fieldValue664.value = "l_shoulder"

ProtoInstance663.fieldValue.append(fieldValue664)
fieldValue665 = x3d.fieldValue()
fieldValue665.name = "center"
fieldValue665.value = "0.167 1.36 -0.0518"

ProtoInstance663.fieldValue.append(fieldValue665)
fieldValue666 = x3d.fieldValue()
fieldValue666.name = "children"
ProtoInstance667 = x3d.ProtoInstance()
ProtoInstance667.name = "Segment"
ProtoInstance667.DEF = "Nancy_hanim_l_upperarm"
fieldValue668 = x3d.fieldValue()
fieldValue668.name = "name"
fieldValue668.value = "l_upperarm"

ProtoInstance667.fieldValue.append(fieldValue668)
fieldValue669 = x3d.fieldValue()
fieldValue669.name = "children"
Transform670 = x3d.Transform()
Transform670.DEF = "l_upperarm_adjust"
Transform670.center = [0.182,1.22,-0.047]
Transform670.rotation = [1,0,0,0.119]
Transform670.translation = [0,0.0004203,-0.01665]
Shape671 = x3d.Shape()
Appearance672 = x3d.Appearance()
Material673 = x3d.Material()
Material673.USE = "Skin_Color"

Appearance672.material = Material673

Shape671.appearance = Appearance672
IndexedFaceSet674 = x3d.IndexedFaceSet()
IndexedFaceSet674.coordIndex = [2,1,0,-1,2,3,1,-1,2,4,3,-1,2,0,5,-1,6,5,0,-1,7,2,5,-1,8,4,2,-1,8,3,4,-1,9,1,3,-1,10,0,1,-1,0,10,6,-1,1,9,10,-1,3,8,9,-1,2,7,8,-1,5,6,7,-1,11,7,6,-1,14,9,8,-1,15,10,9,-1,11,6,10,-1,10,15,11,-1,9,14,15,-1,8,13,14,-1,8,16,13,-1,7,11,12,-1,21,15,14,-1,15,17,11,-1,15,21,17,-1,16,19,13,-1,13,19,20,-1,21,14,20,-1,14,13,20,-1,12,17,18,-1,12,11,17,-1,12,18,16,-1,18,19,16,-1,12,16,7,-1,16,8,7,-1,19,18,17,-1,20,19,21,-1,19,17,21,-1]
IndexedFaceSet674.creaseAngle = 1.65
Coordinate675 = x3d.Coordinate()

IndexedFaceSet674.coord = Coordinate675

Shape671.geometry = IndexedFaceSet674

Transform670.children.append(Shape671)

fieldValue669.children.append(Transform670)

ProtoInstance667.fieldValue.append(fieldValue669)

fieldValue666.children.append(ProtoInstance667)
ProtoInstance676 = x3d.ProtoInstance()
ProtoInstance676.name = "Joint"
ProtoInstance676.DEF = "Nancy_hanim_l_elbow"
fieldValue677 = x3d.fieldValue()
fieldValue677.name = "name"
fieldValue677.value = "l_elbow"

ProtoInstance676.fieldValue.append(fieldValue677)
fieldValue678 = x3d.fieldValue()
fieldValue678.name = "center"
fieldValue678.value = "0.196 1.07 -0.0518"

ProtoInstance676.fieldValue.append(fieldValue678)
fieldValue679 = x3d.fieldValue()
fieldValue679.name = "children"
ProtoInstance680 = x3d.ProtoInstance()
ProtoInstance680.name = "Segment"
ProtoInstance680.DEF = "Nancy_hanim_l_forearm"
fieldValue681 = x3d.fieldValue()
fieldValue681.name = "name"
fieldValue681.value = "l_forearm"

ProtoInstance680.fieldValue.append(fieldValue681)
fieldValue682 = x3d.fieldValue()
fieldValue682.name = "children"
Transform683 = x3d.Transform()
Transform683.DEF = "l_forearm_adjust"
Transform683.center = [0.198,0.961,-0.0405]
Transform683.rotation = [-1,0,0,0.1]
Transform683.translation = [0,0.003724,-0.0236]
Shape684 = x3d.Shape()
Appearance685 = x3d.Appearance()
Material686 = x3d.Material()
Material686.USE = "Skin_Color"

Appearance685.material = Material686

Shape684.appearance = Appearance685
IndexedFaceSet687 = x3d.IndexedFaceSet()
IndexedFaceSet687.coordIndex = [2,1,0,-1,2,3,1,-1,2,4,3,-1,2,5,4,-1,2,6,5,-1,2,0,6,-1,7,6,0,-1,8,5,6,-1,9,4,5,-1,9,3,4,-1,10,1,3,-1,11,0,1,-1,0,11,7,-1,1,10,11,-1,3,9,10,-1,5,12,9,-1,5,8,12,-1,6,7,8,-1,17,16,15,-1,14,17,15,-1,14,18,17,-1,13,18,14,-1,16,17,10,-1,16,10,9,-1,15,16,9,-1,15,9,12,-1,18,13,7,-1,18,7,11,-1,13,14,8,-1,13,8,7,-1,14,15,8,-1,15,12,8,-1,17,18,10,-1,18,11,10,-1]
IndexedFaceSet687.creaseAngle = 1.75
Coordinate688 = x3d.Coordinate()

IndexedFaceSet687.coord = Coordinate688

Shape684.geometry = IndexedFaceSet687

Transform683.children.append(Shape684)

fieldValue682.children.append(Transform683)

ProtoInstance680.fieldValue.append(fieldValue682)

fieldValue679.children.append(ProtoInstance680)
ProtoInstance689 = x3d.ProtoInstance()
ProtoInstance689.name = "Joint"
ProtoInstance689.DEF = "Nancy_hanim_l_wrist"
fieldValue690 = x3d.fieldValue()
fieldValue690.name = "name"
fieldValue690.value = "l_wrist"

ProtoInstance689.fieldValue.append(fieldValue690)
fieldValue691 = x3d.fieldValue()
fieldValue691.name = "center"
fieldValue691.value = "0.213 0.811 -0.0338"

ProtoInstance689.fieldValue.append(fieldValue691)
fieldValue692 = x3d.fieldValue()
fieldValue692.name = "children"
ProtoInstance693 = x3d.ProtoInstance()
ProtoInstance693.name = "Segment"
ProtoInstance693.DEF = "Nancy_hanim_l_hand"
fieldValue694 = x3d.fieldValue()
fieldValue694.name = "name"
fieldValue694.value = "l_hand"

ProtoInstance693.fieldValue.append(fieldValue694)
fieldValue695 = x3d.fieldValue()
fieldValue695.name = "children"
Transform696 = x3d.Transform()
Transform696.DEF = "l_hand_adjust"
Transform696.center = [0.213,0.811,-0.0338]
Transform696.rotation = [-0.06361,-0.9967,0.04988,1.333]
Transform696.translation = [0,0.005142,-0.008662]
Shape697 = x3d.Shape()
Appearance698 = x3d.Appearance()
Material699 = x3d.Material()
Material699.USE = "Skin_Color"

Appearance698.material = Material699

Shape697.appearance = Appearance698
IndexedFaceSet700 = x3d.IndexedFaceSet()
IndexedFaceSet700.coordIndex = [2,1,0,-1,5,4,3,-1,3,7,6,-1,2,3,6,-1,7,9,8,-1,6,7,8,-1,9,11,10,-1,8,9,10,-1,11,13,12,-1,10,11,12,-1,13,15,14,-1,12,13,14,-1,15,17,16,-1,14,15,16,-1,17,19,18,-1,16,17,18,-1,19,21,20,-1,18,19,20,-1,31,4,1,-1,4,5,0,-1,1,4,0,-1,5,3,2,-1,0,5,2,-1,26,25,24,-1,26,24,23,-1,27,26,23,-1,28,27,23,-1,28,23,22,-1,29,28,22,-1,29,22,21,-1,30,29,21,-1,15,13,11,-1,17,15,11,-1,19,17,11,-1,19,11,9,-1,31,19,9,-1,31,9,7,-1,4,31,7,-1,4,7,3,-1,30,21,19,-1,31,30,19,-1,12,14,16,-1,10,12,16,-1,10,16,18,-1,8,10,18,-1,6,8,1,-1,2,6,1,-1,39,38,37,-1,37,38,40,-1,37,40,36,-1,36,40,41,-1,36,41,35,-1,35,41,42,-1,35,42,34,-1,34,42,43,-1,34,43,33,-1,33,43,44,-1,33,44,32,-1,20,32,44,-1,20,44,45,-1,20,45,46,-1,47,8,18,-1,47,18,20,-1,47,20,46,-1,8,47,1,-1,22,33,32,-1,23,35,34,-1,23,36,35,-1,37,24,25,-1,40,38,27,-1,29,43,42,-1,45,44,30,-1,47,31,1,-1,47,46,31,-1,29,30,43,-1,30,44,43,-1,45,31,46,-1,45,30,31,-1,28,29,41,-1,29,42,41,-1,28,40,27,-1,28,41,40,-1,26,27,39,-1,27,38,39,-1,25,39,37,-1,25,26,39,-1,24,36,23,-1,24,37,36,-1,23,34,22,-1,34,33,22,-1,22,32,21,-1,32,20,21,-1]
IndexedFaceSet700.creaseAngle = 1.48
Coordinate701 = x3d.Coordinate()

IndexedFaceSet700.coord = Coordinate701

Shape697.geometry = IndexedFaceSet700

Transform696.children.append(Shape697)

fieldValue695.children.append(Transform696)

ProtoInstance693.fieldValue.append(fieldValue695)

fieldValue692.children.append(ProtoInstance693)

ProtoInstance689.fieldValue.append(fieldValue692)

fieldValue679.children.append(ProtoInstance689)

ProtoInstance676.fieldValue.append(fieldValue679)

fieldValue666.children.append(ProtoInstance676)

ProtoInstance663.fieldValue.append(fieldValue666)

fieldValue652.children.append(ProtoInstance663)
ProtoInstance702 = x3d.ProtoInstance()
ProtoInstance702.name = "Joint"
ProtoInstance702.DEF = "Nancy_hanim_r_shoulder"
fieldValue703 = x3d.fieldValue()
fieldValue703.name = "name"
fieldValue703.value = "r_shoulder"

ProtoInstance702.fieldValue.append(fieldValue703)
fieldValue704 = x3d.fieldValue()
fieldValue704.name = "center"
fieldValue704.value = "-0.167 1.36 -0.0458"

ProtoInstance702.fieldValue.append(fieldValue704)
fieldValue705 = x3d.fieldValue()
fieldValue705.name = "children"
ProtoInstance706 = x3d.ProtoInstance()
ProtoInstance706.name = "Segment"
ProtoInstance706.DEF = "Nancy_hanim_r_upperarm"
fieldValue707 = x3d.fieldValue()
fieldValue707.name = "name"
fieldValue707.value = "r_upperarm"

ProtoInstance706.fieldValue.append(fieldValue707)
fieldValue708 = x3d.fieldValue()
fieldValue708.name = "children"
Transform709 = x3d.Transform()
Transform709.DEF = "r_upperarm_adjust"
Transform709.center = [-0.182,1.22,-0.047]
Transform709.rotation = [1,0,0,0.0836]
Transform709.translation = [0,0.000589,-0.01169]
Shape710 = x3d.Shape()
Appearance711 = x3d.Appearance()
Material712 = x3d.Material()
Material712.USE = "Skin_Color"

Appearance711.material = Material712

Shape710.appearance = Appearance711
IndexedFaceSet713 = x3d.IndexedFaceSet()
IndexedFaceSet713.coordIndex = [14,10,20,-1,10,13,20,-1,13,22,20,-1,19,14,20,-1,14,19,12,-1,19,20,24,-1,20,22,25,-1,22,13,25,-1,13,10,11,-1,10,14,5,-1,12,5,14,-1,5,11,10,-1,11,25,13,-1,25,24,20,-1,24,12,19,-1,12,24,9,-1,25,11,8,-1,11,5,2,-1,5,12,9,-1,9,2,5,-1,2,8,11,-1,8,23,25,-1,23,27,25,-1,21,9,24,-1,9,21,7,-1,27,23,18,-1,23,8,18,-1,8,2,6,-1,2,9,7,-1,7,1,2,-1,1,6,2,-1,6,18,8,-1,18,26,27,-1,16,7,21,-1,7,16,4,-1,16,26,17,-1,26,18,15,-1,18,6,3,-1,6,1,0,-1,1,7,0,-1,4,0,7,-1,0,3,6,-1,3,15,18,-1,15,17,26,-1,17,4,16,-1,3,0,15,-1,15,0,4,-1,15,4,17,-1,25,27,24,-1,27,21,24,-1,27,26,21,-1,26,16,21,-1]
IndexedFaceSet713.creaseAngle = 1.53
Coordinate714 = x3d.Coordinate()

IndexedFaceSet713.coord = Coordinate714

Shape710.geometry = IndexedFaceSet713

Transform709.children.append(Shape710)

fieldValue708.children.append(Transform709)

ProtoInstance706.fieldValue.append(fieldValue708)

fieldValue705.children.append(ProtoInstance706)
ProtoInstance715 = x3d.ProtoInstance()
ProtoInstance715.name = "Joint"
ProtoInstance715.DEF = "Nancy_hanim_r_elbow"
fieldValue716 = x3d.fieldValue()
fieldValue716.name = "name"
fieldValue716.value = "r_elbow"

ProtoInstance715.fieldValue.append(fieldValue716)
fieldValue717 = x3d.fieldValue()
fieldValue717.name = "center"
fieldValue717.value = "-0.192 1.07 -0.0498"

ProtoInstance715.fieldValue.append(fieldValue717)
fieldValue718 = x3d.fieldValue()
fieldValue718.name = "children"
ProtoInstance719 = x3d.ProtoInstance()
ProtoInstance719.name = "Segment"
ProtoInstance719.DEF = "Nancy_hanim_r_forearm"
fieldValue720 = x3d.fieldValue()
fieldValue720.name = "name"
fieldValue720.value = "r_forearm"

ProtoInstance719.fieldValue.append(fieldValue720)
fieldValue721 = x3d.fieldValue()
fieldValue721.name = "children"
Transform722 = x3d.Transform()
Transform722.DEF = "r_forearm_adjust"
Transform722.center = [-0.198,0.961,-0.0397]
Transform722.rotation = [-1,0,0,0.1254]
Transform722.translation = [0,0.003466,-0.01065]
Shape723 = x3d.Shape()
Appearance724 = x3d.Appearance()
Material725 = x3d.Material()
Material725.USE = "Skin_Color"

Appearance724.material = Material725

Shape723.appearance = Appearance724
IndexedFaceSet726 = x3d.IndexedFaceSet()
IndexedFaceSet726.coordIndex = [20,13,15,-1,13,8,15,-1,8,12,15,-1,12,18,15,-1,18,22,15,-1,22,20,15,-1,20,22,21,-1,22,18,24,-1,18,12,7,-1,12,8,7,-1,8,13,3,-1,13,20,10,-1,21,10,20,-1,10,3,13,-1,3,7,8,-1,7,19,18,-1,19,24,18,-1,24,21,22,-1,21,24,23,-1,24,19,16,-1,19,7,6,-1,7,3,1,-1,3,10,5,-1,10,21,17,-1,17,5,10,-1,5,1,3,-1,1,6,7,-1,6,16,19,-1,16,23,24,-1,23,17,21,-1,1,5,2,-1,5,17,9,-1,9,2,5,-1,1,4,6,-1,4,16,6,-1,23,9,17,-1,9,23,14,-1,23,16,11,-1,4,11,16,-1,11,14,23,-1,11,4,0,-1,11,0,14,-1,0,2,14,-1,14,2,9,-1,2,0,1,-1,0,4,1,-1]
IndexedFaceSet726.creaseAngle = 1.73
Coordinate727 = x3d.Coordinate()

IndexedFaceSet726.coord = Coordinate727

Shape723.geometry = IndexedFaceSet726

Transform722.children.append(Shape723)

fieldValue721.children.append(Transform722)

ProtoInstance719.fieldValue.append(fieldValue721)

fieldValue718.children.append(ProtoInstance719)
ProtoInstance728 = x3d.ProtoInstance()
ProtoInstance728.name = "Joint"
ProtoInstance728.DEF = "Nancy_hanim_r_wrist"
fieldValue729 = x3d.fieldValue()
fieldValue729.name = "name"
fieldValue729.value = "r_wrist"

ProtoInstance728.fieldValue.append(fieldValue729)
fieldValue730 = x3d.fieldValue()
fieldValue730.name = "center"
fieldValue730.value = "-0.217 0.811 -0.0338"

ProtoInstance728.fieldValue.append(fieldValue730)
fieldValue731 = x3d.fieldValue()
fieldValue731.name = "children"
ProtoInstance732 = x3d.ProtoInstance()
ProtoInstance732.name = "Segment"
ProtoInstance732.DEF = "Nancy_hanim_r_hand"
fieldValue733 = x3d.fieldValue()
fieldValue733.name = "name"
fieldValue733.value = "r_hand"

ProtoInstance732.fieldValue.append(fieldValue733)
fieldValue734 = x3d.fieldValue()
fieldValue734.name = "children"
Transform735 = x3d.Transform()
Transform735.DEF = "r_hand_adjust"
Transform735.center = [-0.217,0.811,-0.0338]
Transform735.rotation = [-0.09024,0.994,-0.0624,1.216]
Shape736 = x3d.Shape()
Appearance737 = x3d.Appearance()
Material738 = x3d.Material()
Material738.USE = "Skin_Color"

Appearance737.material = Material738

Shape736.appearance = Appearance737
IndexedFaceSet739 = x3d.IndexedFaceSet()
IndexedFaceSet739.coordIndex = [10,9,0,-1,11,30,31,-1,1,12,11,-1,1,11,0,-1,2,13,12,-1,2,12,1,-1,3,14,13,-1,3,13,2,-1,4,15,14,-1,4,14,3,-1,5,16,15,-1,5,15,4,-1,6,17,16,-1,6,16,5,-1,7,18,17,-1,7,17,6,-1,8,19,18,-1,8,18,7,-1,10,31,30,-1,10,30,9,-1,0,11,31,-1,0,31,10,-1,22,23,24,-1,21,22,24,-1,21,24,25,-1,21,25,26,-1,20,21,26,-1,20,26,27,-1,19,20,27,-1,19,27,28,-1,14,15,16,-1,14,16,17,-1,14,17,18,-1,13,14,18,-1,13,18,29,-1,12,13,29,-1,12,29,30,-1,11,12,30,-1,18,19,28,-1,18,28,29,-1,6,5,4,-1,6,4,3,-1,7,6,3,-1,7,3,2,-1,9,2,1,-1,9,1,0,-1,32,38,33,-1,33,38,39,-1,33,39,34,-1,34,39,40,-1,34,40,35,-1,35,40,41,-1,35,41,36,-1,36,41,42,-1,36,42,37,-1,37,42,43,-1,37,43,44,-1,44,43,8,-1,44,8,45,-1,45,8,46,-1,46,8,7,-1,46,7,2,-1,46,2,47,-1,9,47,2,-1,25,34,35,-1,25,33,34,-1,25,24,33,-1,24,32,33,-1,32,24,23,-1,40,39,21,-1,41,40,21,-1,43,19,8,-1,43,20,19,-1,43,42,20,-1,21,20,41,-1,20,42,41,-1,38,22,39,-1,22,21,39,-1,32,23,38,-1,23,22,38,-1,26,25,35,-1,27,36,37,-1,27,37,28,-1,37,44,28,-1,26,35,27,-1,35,36,27,-1,28,44,45,-1,29,46,47,-1,29,9,30,-1,29,47,9,-1,28,45,29,-1,45,46,29,-1]
IndexedFaceSet739.creaseAngle = 1.57
Coordinate740 = x3d.Coordinate()

IndexedFaceSet739.coord = Coordinate740

Shape736.geometry = IndexedFaceSet739

Transform735.children.append(Shape736)

fieldValue734.children.append(Transform735)

ProtoInstance732.fieldValue.append(fieldValue734)

fieldValue731.children.append(ProtoInstance732)

ProtoInstance728.fieldValue.append(fieldValue731)

fieldValue718.children.append(ProtoInstance728)

ProtoInstance715.fieldValue.append(fieldValue718)

fieldValue705.children.append(ProtoInstance715)

ProtoInstance702.fieldValue.append(fieldValue705)

fieldValue652.children.append(ProtoInstance702)
ProtoInstance741 = x3d.ProtoInstance()
ProtoInstance741.name = "Joint"
ProtoInstance741.DEF = "Nancy_hanim_vc4"
fieldValue742 = x3d.fieldValue()
fieldValue742.name = "name"
fieldValue742.value = "vc4"

ProtoInstance741.fieldValue.append(fieldValue742)
fieldValue743 = x3d.fieldValue()
fieldValue743.name = "center"
fieldValue743.value = "0 1.43 -0.0458"

ProtoInstance741.fieldValue.append(fieldValue743)
fieldValue744 = x3d.fieldValue()
fieldValue744.name = "children"
ProtoInstance745 = x3d.ProtoInstance()
ProtoInstance745.name = "Segment"
ProtoInstance745.DEF = "Nancy_hanim_c4"
fieldValue746 = x3d.fieldValue()
fieldValue746.name = "name"
fieldValue746.value = "c4"

ProtoInstance745.fieldValue.append(fieldValue746)
fieldValue747 = x3d.fieldValue()
fieldValue747.name = "children"
Shape748 = x3d.Shape()
Appearance749 = x3d.Appearance()
Material750 = x3d.Material()
Material750.USE = "Skin_Color"

Appearance749.material = Material750

Shape748.appearance = Appearance749
IndexedFaceSet751 = x3d.IndexedFaceSet()
IndexedFaceSet751.DEF = "neck"
IndexedFaceSet751.coordIndex = [6,5,2,-1,6,2,3,-1,5,4,1,-1,5,1,2,-1,4,7,0,-1,4,0,1,-1,11,10,9,-1,11,9,8,-1,10,13,12,-1,10,12,9,-1,13,15,14,-1,13,14,12,-1,6,3,11,-1,6,11,8,-1,7,14,15,-1,7,15,0,-1,2,10,11,-1,2,11,3,-1,2,1,13,-1,2,13,10,-1,1,0,15,-1,1,15,13,-1,9,5,6,-1,9,6,8,-1,9,12,4,-1,9,4,5,-1,12,14,7,-1,12,7,4,-1]
IndexedFaceSet751.creaseAngle = 1.91
Coordinate752 = x3d.Coordinate()

IndexedFaceSet751.coord = Coordinate752

Shape748.geometry = IndexedFaceSet751

fieldValue747.children.append(Shape748)

ProtoInstance745.fieldValue.append(fieldValue747)

fieldValue744.children.append(ProtoInstance745)
ProtoInstance753 = x3d.ProtoInstance()
ProtoInstance753.name = "Joint"
ProtoInstance753.DEF = "Nancy_hanim_skullbase"
fieldValue754 = x3d.fieldValue()
fieldValue754.name = "name"
fieldValue754.value = "skullbase"

ProtoInstance753.fieldValue.append(fieldValue754)
fieldValue755 = x3d.fieldValue()
fieldValue755.name = "center"
fieldValue755.value = "0 1.54 -0.0409"

ProtoInstance753.fieldValue.append(fieldValue755)
fieldValue756 = x3d.fieldValue()
fieldValue756.name = "children"
ProtoInstance757 = x3d.ProtoInstance()
ProtoInstance757.name = "Segment"
ProtoInstance757.DEF = "Nancy_hanim_skull"
fieldValue758 = x3d.fieldValue()
fieldValue758.name = "name"
fieldValue758.value = "skull"

ProtoInstance757.fieldValue.append(fieldValue758)
fieldValue759 = x3d.fieldValue()
fieldValue759.name = "children"
Shape760 = x3d.Shape()
Appearance761 = x3d.Appearance()
Material762 = x3d.Material()
Material762.USE = "Skin_Color"

Appearance761.material = Material762

Shape760.appearance = Appearance761
IndexedFaceSet763 = x3d.IndexedFaceSet()
IndexedFaceSet763.DEF = "headIFS"
IndexedFaceSet763.colorIndex = [1,1,1,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,1,1,1,-1,1,1,1,-1,0,0,0,-1,1,1,1,-1,1,1,1,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,2,2,2,-1,2,2,2,-1,2,2,2,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,2,2,2,-1,2,2,2,-1,2,2,2,-1,0,0,0,-1,0,0,0,-1,2,2,2,-1,2,2,2,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,1,1,1,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,2,2,2,-1,2,2,2,-1,2,2,2,-1,2,2,2,-1,2,2,2,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,2,2,2,-1,2,2,2,-1,2,2,2,-1,0,0,0,-1,0,0,0,-1,2,2,2,-1,2,2,2,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,3,3,3,-1,3,3,3,-1,0,0,0,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,3,3,3,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,3,3,3,-1,3,3,3,-1,0,0,0,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,3,3,3,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1]
IndexedFaceSet763.coordIndex = [48,87,58,-1,91,92,59,-1,59,92,88,-1,88,93,231,-1,232,86,233,-1,86,89,233,-1,89,57,56,-1,49,55,57,-1,102,86,96,-1,86,90,96,-1,97,95,96,-1,97,127,95,-1,41,96,154,-1,41,102,96,-1,99,102,41,-1,153,99,41,-1,102,40,86,-1,234,235,236,-1,87,237,58,-1,56,57,91,-1,87,234,237,-1,234,236,237,-1,89,49,57,-1,49,50,55,-1,40,89,86,-1,89,56,233,-1,232,90,86,-1,90,97,96,-1,92,93,88,-1,93,94,231,-1,232,231,94,-1,97,90,232,-1,96,42,154,-1,95,42,96,-1,53,46,45,-1,53,45,51,-1,53,51,92,-1,92,51,52,-1,92,52,93,-1,94,93,52,-1,94,52,4,-1,97,232,94,-1,54,47,46,-1,54,46,53,-1,55,47,54,-1,50,47,55,-1,34,33,50,-1,34,50,49,-1,35,34,49,-1,35,49,89,-1,35,89,40,-1,99,39,102,-1,39,35,40,-1,31,34,35,-1,31,35,32,-1,14,32,35,-1,14,35,39,-1,14,39,98,-1,137,38,153,-1,38,99,153,-1,38,98,99,-1,37,238,239,-1,11,238,37,-1,101,37,36,-1,241,141,242,-1,10,12,242,-1,12,13,14,-1,12,14,243,-1,13,15,32,-1,13,32,14,-1,15,16,31,-1,15,31,32,-1,2,70,10,-1,2,10,141,-1,70,69,12,-1,70,12,10,-1,69,68,13,-1,69,13,12,-1,68,67,15,-1,68,15,13,-1,67,66,16,-1,67,16,15,-1,98,39,99,-1,101,11,37,-1,100,101,36,-1,36,244,240,-1,141,10,242,-1,12,243,242,-1,36,37,239,-1,36,239,244,-1,57,55,91,-1,55,54,91,-1,39,40,102,-1,123,103,120,-1,114,122,104,-1,115,122,114,-1,208,105,115,-1,210,119,211,-1,210,106,119,-1,116,107,106,-1,107,108,117,-1,126,119,109,-1,126,110,119,-1,126,95,125,-1,95,127,125,-1,154,126,111,-1,126,109,111,-1,111,109,112,-1,111,112,153,-1,119,113,109,-1,207,213,214,-1,123,209,103,-1,213,212,214,-1,209,214,103,-1,209,207,214,-1,107,117,106,-1,108,118,117,-1,119,106,113,-1,210,116,106,-1,119,110,211,-1,126,125,110,-1,115,105,122,-1,208,124,105,-1,124,208,211,-1,211,110,125,-1,154,42,126,-1,126,42,95,-1,168,128,121,-1,170,168,121,-1,122,170,121,-1,172,170,122,-1,105,172,122,-1,172,105,124,-1,4,172,124,-1,124,211,125,-1,128,130,129,-1,121,128,129,-1,129,130,108,-1,108,130,118,-1,118,131,132,-1,117,118,132,-1,117,132,133,-1,106,117,133,-1,113,106,133,-1,109,152,112,-1,113,133,152,-1,133,132,134,-1,135,133,134,-1,133,135,136,-1,152,133,136,-1,148,152,136,-1,153,138,137,-1,153,112,138,-1,112,148,138,-1,219,217,139,-1,36,240,149,-1,139,217,140,-1,149,139,151,-1,36,149,100,-1,220,141,241,-1,220,150,142,-1,136,143,150,-1,221,136,150,-1,135,144,143,-1,136,135,143,-1,134,158,144,-1,135,134,144,-1,142,161,2,-1,141,142,2,-1,150,145,161,-1,142,150,161,-1,143,146,145,-1,150,143,145,-1,144,147,146,-1,143,144,146,-1,158,160,147,-1,144,158,147,-1,112,152,148,-1,139,140,151,-1,149,151,100,-1,240,218,149,-1,220,142,141,-1,220,221,150,-1,219,139,149,-1,218,219,149,-1,104,108,107,-1,104,129,108,-1,109,113,152,-1,153,41,111,-1,129,104,122,-1,129,122,121,-1,91,54,92,-1,54,53,92,-1,97,94,127,-1,127,94,4,-1,125,127,124,-1,127,4,124,-1,154,111,41,-1,31,30,33,-1,31,33,34,-1,16,17,30,-1,16,30,31,-1,66,65,17,-1,66,17,16,-1,2,73,156,-1,2,156,70,-1,156,72,66,-1,156,66,67,-1,156,67,68,-1,156,68,69,-1,156,69,70,-1,72,71,65,-1,72,65,66,-1,17,18,30,-1,45,44,51,-1,51,44,43,-1,51,43,52,-1,52,43,1,-1,52,1,4,-1,245,246,27,-1,245,27,3,-1,246,247,28,-1,246,28,27,-1,248,22,29,-1,248,29,28,-1,248,28,247,-1,27,26,0,-1,27,0,3,-1,27,28,25,-1,27,25,26,-1,29,24,25,-1,29,25,28,-1,22,23,24,-1,22,24,29,-1,249,250,22,-1,249,22,248,-1,250,60,23,-1,250,23,22,-1,17,254,18,-1,65,254,17,-1,71,64,65,-1,63,74,75,-1,63,75,61,-1,64,255,254,-1,75,62,61,-1,62,76,60,-1,76,77,23,-1,76,23,60,-1,77,24,23,-1,77,78,25,-1,77,25,24,-1,78,84,26,-1,78,26,25,-1,84,192,0,-1,84,0,26,-1,84,83,193,-1,84,193,192,-1,79,83,84,-1,79,84,78,-1,76,79,78,-1,76,78,77,-1,80,83,79,-1,80,204,83,-1,75,81,80,-1,81,85,204,-1,81,204,80,-1,74,81,75,-1,74,82,81,-1,82,5,85,-1,82,85,81,-1,155,8,71,-1,155,71,72,-1,8,6,64,-1,8,64,71,-1,6,7,255,-1,6,255,64,-1,7,9,256,-1,7,256,255,-1,9,257,256,-1,73,155,156,-1,155,72,156,-1,204,193,83,-1,64,254,65,-1,131,157,134,-1,132,131,134,-1,157,159,158,-1,134,157,158,-1,159,206,160,-1,158,159,160,-1,203,73,2,-1,161,203,2,-1,160,162,203,-1,147,160,203,-1,146,147,203,-1,145,146,203,-1,161,145,203,-1,206,163,162,-1,160,206,162,-1,157,164,159,-1,170,169,168,-1,171,169,170,-1,172,171,170,-1,1,171,172,-1,4,1,172,-1,173,227,245,-1,3,173,245,-1,174,226,227,-1,173,174,227,-1,176,175,215,-1,174,176,215,-1,226,174,215,-1,0,177,173,-1,3,0,173,-1,178,174,173,-1,177,178,173,-1,178,179,176,-1,174,178,176,-1,179,180,175,-1,176,179,175,-1,175,225,216,-1,215,175,216,-1,180,181,225,-1,175,180,225,-1,164,228,159,-1,159,228,206,-1,206,185,163,-1,187,186,184,-1,183,187,184,-1,228,229,185,-1,183,182,187,-1,181,188,182,-1,180,189,188,-1,181,180,188,-1,180,179,189,-1,178,190,189,-1,179,178,189,-1,177,191,190,-1,178,177,190,-1,0,192,191,-1,177,0,191,-1,193,205,191,-1,192,193,191,-1,191,205,194,-1,190,191,194,-1,190,194,188,-1,189,190,188,-1,194,205,195,-1,205,204,195,-1,195,196,187,-1,204,85,196,-1,195,204,196,-1,187,196,186,-1,196,197,186,-1,85,5,197,-1,196,85,197,-1,163,198,202,-1,162,163,202,-1,185,199,198,-1,163,185,198,-1,229,200,199,-1,185,229,199,-1,230,201,200,-1,229,230,200,-1,230,257,201,-1,203,202,73,-1,203,162,202,-1,205,193,204,-1,206,228,185,-1,198,8,155,-1,198,155,202,-1,155,73,202,-1,199,6,8,-1,199,8,198,-1,7,6,199,-1,7,199,200,-1,201,9,7,-1,201,7,200,-1,201,257,9,-1,188,194,195,-1,188,195,182,-1,195,187,182,-1,80,79,76,-1,80,62,75,-1,80,76,62,-1,47,50,33,-1,131,118,130,-1,20,21,47,-1,21,46,47,-1,20,33,19,-1,20,47,33,-1,33,30,19,-1,30,18,19,-1,62,60,251,-1,60,250,251,-1,252,61,251,-1,61,62,251,-1,252,63,61,-1,252,253,63,-1,166,130,167,-1,130,128,167,-1,166,131,130,-1,166,165,131,-1,165,157,131,-1,165,164,157,-1,224,181,182,-1,224,225,181,-1,224,183,223,-1,224,182,183,-1,183,184,223,-1,184,222,223,-1]
IndexedFaceSet763.creaseAngle = 0.7854
Coordinate764 = x3d.Coordinate()
Coordinate764.DEF = "Face"

IndexedFaceSet763.coord = Coordinate764
Color765 = x3d.Color()

IndexedFaceSet763.color = Color765

Shape760.geometry = IndexedFaceSet763

fieldValue759.children.append(Shape760)

ProtoInstance757.fieldValue.append(fieldValue759)

fieldValue756.children.append(ProtoInstance757)

ProtoInstance753.fieldValue.append(fieldValue756)

fieldValue744.children.append(ProtoInstance753)

ProtoInstance741.fieldValue.append(fieldValue744)

fieldValue652.children.append(ProtoInstance741)

ProtoInstance649.fieldValue.append(fieldValue652)

fieldValue564.children.append(ProtoInstance649)

ProtoInstance561.fieldValue.append(fieldValue564)

fieldValue560.children.append(ProtoInstance561)
Group766 = x3d.Group()

fieldValue560.children.append(Group766)

ProtoInstance556.fieldValue.append(fieldValue560)
fieldValue767 = x3d.fieldValue()
fieldValue767.name = "joints"
ProtoInstance768 = x3d.ProtoInstance()
ProtoInstance768.USE = "Nancy_hanim_humanoid_root"

fieldValue767.children.append(ProtoInstance768)
ProtoInstance769 = x3d.ProtoInstance()
ProtoInstance769.USE = "Nancy_hanim_sacroiliac"

fieldValue767.children.append(ProtoInstance769)
ProtoInstance770 = x3d.ProtoInstance()
ProtoInstance770.USE = "Nancy_hanim_l_hip"

fieldValue767.children.append(ProtoInstance770)
ProtoInstance771 = x3d.ProtoInstance()
ProtoInstance771.USE = "Nancy_hanim_l_knee"

fieldValue767.children.append(ProtoInstance771)
ProtoInstance772 = x3d.ProtoInstance()
ProtoInstance772.USE = "Nancy_hanim_l_ankle"

fieldValue767.children.append(ProtoInstance772)
ProtoInstance773 = x3d.ProtoInstance()
ProtoInstance773.USE = "Nancy_hanim_r_hip"

fieldValue767.children.append(ProtoInstance773)
ProtoInstance774 = x3d.ProtoInstance()
ProtoInstance774.USE = "Nancy_hanim_r_knee"

fieldValue767.children.append(ProtoInstance774)
ProtoInstance775 = x3d.ProtoInstance()
ProtoInstance775.USE = "Nancy_hanim_r_ankle"

fieldValue767.children.append(ProtoInstance775)
ProtoInstance776 = x3d.ProtoInstance()
ProtoInstance776.USE = "Nancy_hanim_vl1"

fieldValue767.children.append(ProtoInstance776)
ProtoInstance777 = x3d.ProtoInstance()
ProtoInstance777.USE = "Nancy_hanim_l_shoulder"

fieldValue767.children.append(ProtoInstance777)
ProtoInstance778 = x3d.ProtoInstance()
ProtoInstance778.USE = "Nancy_hanim_l_elbow"

fieldValue767.children.append(ProtoInstance778)
ProtoInstance779 = x3d.ProtoInstance()
ProtoInstance779.USE = "Nancy_hanim_l_wrist"

fieldValue767.children.append(ProtoInstance779)
ProtoInstance780 = x3d.ProtoInstance()
ProtoInstance780.USE = "Nancy_hanim_r_shoulder"

fieldValue767.children.append(ProtoInstance780)
ProtoInstance781 = x3d.ProtoInstance()
ProtoInstance781.USE = "Nancy_hanim_r_elbow"

fieldValue767.children.append(ProtoInstance781)
ProtoInstance782 = x3d.ProtoInstance()
ProtoInstance782.USE = "Nancy_hanim_r_wrist"

fieldValue767.children.append(ProtoInstance782)
ProtoInstance783 = x3d.ProtoInstance()
ProtoInstance783.USE = "Nancy_hanim_vc4"

fieldValue767.children.append(ProtoInstance783)
ProtoInstance784 = x3d.ProtoInstance()
ProtoInstance784.USE = "Nancy_hanim_skullbase"

fieldValue767.children.append(ProtoInstance784)

ProtoInstance556.fieldValue.append(fieldValue767)
fieldValue785 = x3d.fieldValue()
fieldValue785.name = "segments"
ProtoInstance786 = x3d.ProtoInstance()
ProtoInstance786.USE = "Nancy_hanim_pelvis"

fieldValue785.children.append(ProtoInstance786)
ProtoInstance787 = x3d.ProtoInstance()
ProtoInstance787.USE = "Nancy_hanim_l_thigh"

fieldValue785.children.append(ProtoInstance787)
ProtoInstance788 = x3d.ProtoInstance()
ProtoInstance788.USE = "Nancy_hanim_l_calf"

fieldValue785.children.append(ProtoInstance788)
ProtoInstance789 = x3d.ProtoInstance()
ProtoInstance789.USE = "Nancy_hanim_l_hindfoot"

fieldValue785.children.append(ProtoInstance789)
ProtoInstance790 = x3d.ProtoInstance()
ProtoInstance790.USE = "Nancy_hanim_r_thigh"

fieldValue785.children.append(ProtoInstance790)
ProtoInstance791 = x3d.ProtoInstance()
ProtoInstance791.USE = "Nancy_hanim_r_calf"

fieldValue785.children.append(ProtoInstance791)
ProtoInstance792 = x3d.ProtoInstance()
ProtoInstance792.USE = "Nancy_hanim_r_hindfoot"

fieldValue785.children.append(ProtoInstance792)
ProtoInstance793 = x3d.ProtoInstance()
ProtoInstance793.USE = "Nancy_hanim_c7"

fieldValue785.children.append(ProtoInstance793)
ProtoInstance794 = x3d.ProtoInstance()
ProtoInstance794.USE = "Nancy_hanim_l_upperarm"

fieldValue785.children.append(ProtoInstance794)
ProtoInstance795 = x3d.ProtoInstance()
ProtoInstance795.USE = "Nancy_hanim_l_forearm"

fieldValue785.children.append(ProtoInstance795)
ProtoInstance796 = x3d.ProtoInstance()
ProtoInstance796.USE = "Nancy_hanim_l_hand"

fieldValue785.children.append(ProtoInstance796)
ProtoInstance797 = x3d.ProtoInstance()
ProtoInstance797.USE = "Nancy_hanim_r_upperarm"

fieldValue785.children.append(ProtoInstance797)
ProtoInstance798 = x3d.ProtoInstance()
ProtoInstance798.USE = "Nancy_hanim_r_forearm"

fieldValue785.children.append(ProtoInstance798)
ProtoInstance799 = x3d.ProtoInstance()
ProtoInstance799.USE = "Nancy_hanim_r_hand"

fieldValue785.children.append(ProtoInstance799)
ProtoInstance800 = x3d.ProtoInstance()
ProtoInstance800.USE = "Nancy_hanim_c4"

fieldValue785.children.append(ProtoInstance800)
ProtoInstance801 = x3d.ProtoInstance()
ProtoInstance801.USE = "Nancy_hanim_skull"

fieldValue785.children.append(ProtoInstance801)

ProtoInstance556.fieldValue.append(fieldValue785)

Switch291.children.append(ProtoInstance556)
HAnimHumanoid802 = x3d.HAnimHumanoid()
HAnimHumanoid802.name = "Humanoid"
HAnimHumanoid802.DEF = "Boxman_Humanoid"
HAnimHumanoid802.version = "2.0"
HAnimJoint803 = x3d.HAnimJoint()
HAnimJoint803.name = "humanoid_root"
HAnimJoint803.DEF = "Boxman_humanoid_root"
HAnimJoint803.center = [0,0.9723,-0.0728]
HAnimJoint803.skinCoordIndex = [0,1,2,3,4,5,6,7,8,9,10,11]
HAnimJoint803.skinCoordWeight = [1,1,1,1,1,1,1,1,1,1,1,1]
HAnimJoint803.ulimit = [0,0,0]
HAnimJoint803.llimit = [0,0,0]
HAnimSegment804 = x3d.HAnimSegment()
HAnimSegment804.name = "sacrum"
HAnimSegment804.DEF = "Boxman_sacrum"
Inline805 = x3d.Inline()
Inline805.url = ["centres/sacrum.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/centres/sacrum.wrl"]

HAnimSegment804.children.append(Inline805)

HAnimJoint803.children.append(HAnimSegment804)
HAnimJoint806 = x3d.HAnimJoint()
HAnimJoint806.name = "l_hip"
HAnimJoint806.DEF = "Boxman_l_hip"
HAnimJoint806.center = [0.0956,0.9364,0]
HAnimJoint806.skinCoordIndex = [12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43]
HAnimJoint806.skinCoordWeight = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]
HAnimJoint806.ulimit = [0,0,0]
HAnimJoint806.llimit = [0,0,0]
HAnimSegment807 = x3d.HAnimSegment()
HAnimSegment807.name = "l_thigh"
HAnimSegment807.DEF = "Boxman_l_thigh"
Inline808 = x3d.Inline()
Inline808.url = ["centres/l_thigh.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/centres/l_thigh.wrl"]

HAnimSegment807.children.append(Inline808)

HAnimJoint806.children.append(HAnimSegment807)
HAnimJoint809 = x3d.HAnimJoint()
HAnimJoint809.name = "l_knee"
HAnimJoint809.DEF = "Boxman_l_knee"
HAnimJoint809.center = [0.0956,0.5095,-0.0036]
HAnimJoint809.skinCoordIndex = [36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63]
HAnimJoint809.skinCoordWeight = [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
HAnimJoint809.ulimit = [0,0,0]
HAnimJoint809.llimit = [0,0,0]
HAnimSegment810 = x3d.HAnimSegment()
HAnimSegment810.name = "l_calf"
HAnimSegment810.DEF = "Boxman_l_calf"
Inline811 = x3d.Inline()
Inline811.url = ["centres/l_calf.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/centres/l_calf.wrl"]

HAnimSegment810.children.append(Inline811)

HAnimJoint809.children.append(HAnimSegment810)
HAnimJoint812 = x3d.HAnimJoint()
HAnimJoint812.name = "l_ankle"
HAnimJoint812.DEF = "Boxman_l_ankle"
HAnimJoint812.center = [0.0946,0.0762,-0.0261]
HAnimJoint812.skinCoordIndex = [64,65,66,67,68,69,70,71]
HAnimJoint812.skinCoordWeight = [1,1,1,1,1,1,1,1]
HAnimJoint812.ulimit = [0,0,0]
HAnimJoint812.llimit = [0,0,0]
HAnimSegment813 = x3d.HAnimSegment()
HAnimSegment813.name = "l_hindfoot"
HAnimSegment813.DEF = "Boxman_l_hindfoot"
Inline814 = x3d.Inline()
Inline814.url = ["centres/l_hindfoot.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/centres/l_hindfoot.wrl"]

HAnimSegment813.children.append(Inline814)

HAnimJoint812.children.append(HAnimSegment813)
HAnimJoint815 = x3d.HAnimJoint()
HAnimJoint815.name = "l_midtarsal"
HAnimJoint815.DEF = "Boxman_l_midtarsal"
HAnimJoint815.center = [0.1079,0.0317,0.067]
HAnimJoint815.skinCoordIndex = [72,73,74,75,76,77,78,79]
HAnimJoint815.skinCoordWeight = [1,1,1,1,1,1,1,1]
HAnimJoint815.ulimit = [0,0,0]
HAnimJoint815.llimit = [0,0,0]
HAnimSegment816 = x3d.HAnimSegment()
HAnimSegment816.name = "l_middistal"
HAnimSegment816.DEF = "Boxman_l_middistal"
Inline817 = x3d.Inline()
Inline817.url = ["centres/l_middistal.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/centres/l_middistal.wrl"]

HAnimSegment816.children.append(Inline817)
HAnimSite818 = x3d.HAnimSite()
HAnimSite818.name = "l_middistal_tip"
HAnimSite818.DEF = "Boxman_l_middistal_tip"
HAnimSite818.translation = [0.095,0.0005,0.1924]

HAnimSegment816.children.append(HAnimSite818)
Inline819 = x3d.Inline()
Inline819.url = ["centres/l_middistal_tip.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/centres/l_middistal_tip.wrl"]

HAnimSegment816.children.append(Inline819)

HAnimJoint815.children.append(HAnimSegment816)

HAnimJoint812.children.append(HAnimJoint815)

HAnimJoint809.children.append(HAnimJoint812)

HAnimJoint806.children.append(HAnimJoint809)

HAnimJoint803.children.append(HAnimJoint806)
HAnimJoint820 = x3d.HAnimJoint()
HAnimJoint820.name = "r_hip"
HAnimJoint820.DEF = "Boxman_r_hip"
HAnimJoint820.center = [-0.0956,0.9364,0]
HAnimJoint820.skinCoordIndex = [80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111]
HAnimJoint820.skinCoordWeight = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]
HAnimJoint820.ulimit = [0,0,0]
HAnimJoint820.llimit = [0,0,0]
HAnimSegment821 = x3d.HAnimSegment()
HAnimSegment821.name = "r_thigh"
HAnimSegment821.DEF = "Boxman_r_thigh"
Inline822 = x3d.Inline()
Inline822.url = ["centres/r_thigh.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/centres/r_thigh.wrl"]

HAnimSegment821.children.append(Inline822)

HAnimJoint820.children.append(HAnimSegment821)
HAnimJoint823 = x3d.HAnimJoint()
HAnimJoint823.name = "r_knee"
HAnimJoint823.DEF = "Boxman_r_knee"
HAnimJoint823.center = [-0.0956,0.5095,-0.0036]
HAnimJoint823.skinCoordIndex = [104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131]
HAnimJoint823.skinCoordWeight = [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
HAnimJoint823.ulimit = [0,0,0]
HAnimJoint823.llimit = [0,0,0]
HAnimSegment824 = x3d.HAnimSegment()
HAnimSegment824.name = "r_calf"
HAnimSegment824.DEF = "Boxman_r_calf"
Inline825 = x3d.Inline()
Inline825.url = ["centres/r_calf.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/centres/r_calf.wrl"]

HAnimSegment824.children.append(Inline825)

HAnimJoint823.children.append(HAnimSegment824)
HAnimJoint826 = x3d.HAnimJoint()
HAnimJoint826.name = "r_ankle"
HAnimJoint826.DEF = "Boxman_r_ankle"
HAnimJoint826.center = [-0.0946,0.0762,-0.0261]
HAnimJoint826.skinCoordIndex = [132,133,134,135,136,137,138,139]
HAnimJoint826.skinCoordWeight = [1,1,1,1,1,1,1,1]
HAnimJoint826.ulimit = [0,0,0]
HAnimJoint826.llimit = [0,0,0]
HAnimSegment827 = x3d.HAnimSegment()
HAnimSegment827.name = "r_hindfoot"
HAnimSegment827.DEF = "Boxman_r_hindfoot"
Inline828 = x3d.Inline()
Inline828.url = ["centres/r_hindfoot.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/centres/r_hindfoot.wrl"]

HAnimSegment827.children.append(Inline828)

HAnimJoint826.children.append(HAnimSegment827)
HAnimJoint829 = x3d.HAnimJoint()
HAnimJoint829.name = "r_midtarsal"
HAnimJoint829.DEF = "Boxman_r_midtarsal"
HAnimJoint829.center = [-0.1079,0.0317,0.067]
HAnimJoint829.skinCoordIndex = [140,141,142,143,144,145,146,147]
HAnimJoint829.skinCoordWeight = [1,1,1,1,1,1,1,1]
HAnimJoint829.ulimit = [0,0,0]
HAnimJoint829.llimit = [0,0,0]
HAnimSegment830 = x3d.HAnimSegment()
HAnimSegment830.name = "r_middistal"
HAnimSegment830.DEF = "Boxman_r_middistal"
Inline831 = x3d.Inline()
Inline831.url = ["centres/r_middistal.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/centres/r_middistal.wrl"]

HAnimSegment830.children.append(Inline831)
HAnimSite832 = x3d.HAnimSite()
HAnimSite832.name = "r_middistal_tip"
HAnimSite832.DEF = "Boxman_r_middistal_tip"
HAnimSite832.translation = [-0.095,0.0005,0.1924]

HAnimSegment830.children.append(HAnimSite832)
Inline833 = x3d.Inline()
Inline833.url = ["centres/r_middistal_tip.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/centres/r_middistal_tip.wrl"]

HAnimSegment830.children.append(Inline833)

HAnimJoint829.children.append(HAnimSegment830)

HAnimJoint826.children.append(HAnimJoint829)

HAnimJoint823.children.append(HAnimJoint826)

HAnimJoint820.children.append(HAnimJoint823)

HAnimJoint803.children.append(HAnimJoint820)
HAnimJoint834 = x3d.HAnimJoint()
HAnimJoint834.name = "vl5"
HAnimJoint834.DEF = "Boxman_vl5"
HAnimJoint834.center = [0,1.0817,-0.0728]
HAnimJoint834.skinCoordIndex = [148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167]
HAnimJoint834.skinCoordWeight = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
HAnimJoint834.ulimit = [0,0,0]
HAnimJoint834.llimit = [0,0,0]
HAnimSegment835 = x3d.HAnimSegment()
HAnimSegment835.name = "l5"
HAnimSegment835.DEF = "Boxman_l5"
Inline836 = x3d.Inline()
Inline836.url = ["centres/l5.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/centres/l5.wrl"]

HAnimSegment835.children.append(Inline836)

HAnimJoint834.children.append(HAnimSegment835)
HAnimJoint837 = x3d.HAnimJoint()
HAnimJoint837.name = "skullbase"
HAnimJoint837.DEF = "Boxman_skullbase"
HAnimJoint837.center = [0,1.644,0.036]
HAnimJoint837.skinCoordIndex = [168,169,170,171,172,173,174,175]
HAnimJoint837.skinCoordWeight = [1,1,1,1,1,1,1,1]
HAnimJoint837.ulimit = [0,0,0]
HAnimJoint837.llimit = [0,0,0]
HAnimSegment838 = x3d.HAnimSegment()
HAnimSegment838.name = "skull"
HAnimSegment838.DEF = "Boxman_skull"
Inline839 = x3d.Inline()
Inline839.url = ["centres/skull.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/centres/skull.wrl"]

HAnimSegment838.children.append(Inline839)
HAnimSite840 = x3d.HAnimSite()
HAnimSite840.name = "skull_tip"
HAnimSite840.DEF = "Boxman_skull_tip"
HAnimSite840.translation = [-0.0029,1.7771,0.0274]

HAnimSegment838.children.append(HAnimSite840)
Inline841 = x3d.Inline()
Inline841.url = ["centres/skull_tip.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/centres/skull_tip.wrl"]

HAnimSegment838.children.append(Inline841)

HAnimJoint837.children.append(HAnimSegment838)

HAnimJoint834.children.append(HAnimJoint837)
HAnimJoint842 = x3d.HAnimJoint()
HAnimJoint842.name = "l_shoulder"
HAnimJoint842.DEF = "Boxman_l_shoulder"
HAnimJoint842.center = [0.1968,1.4642,-0.0265]
HAnimJoint842.skinCoordIndex = [176,177,178,179,180,181,182,183]
HAnimJoint842.skinCoordWeight = [1,1,1,1,1,1,1,1]
HAnimJoint842.ulimit = [0,0,0]
HAnimJoint842.llimit = [0,0,0]
HAnimSegment843 = x3d.HAnimSegment()
HAnimSegment843.name = "l_upperarm"
HAnimSegment843.DEF = "Boxman_l_upperarm"
Inline844 = x3d.Inline()
Inline844.url = ["centres/l_upperarm.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/centres/l_upperarm.wrl"]

HAnimSegment843.children.append(Inline844)

HAnimJoint842.children.append(HAnimSegment843)
HAnimJoint845 = x3d.HAnimJoint()
HAnimJoint845.name = "l_elbow"
HAnimJoint845.DEF = "Boxman_l_elbow"
HAnimJoint845.center = [0.1982,1.1622,-0.0557]
HAnimJoint845.skinCoordIndex = [184,185,186,187,188,189,190,191]
HAnimJoint845.skinCoordWeight = [1,1,1,1,1,1,1,1]
HAnimJoint845.ulimit = [0,0,0]
HAnimJoint845.llimit = [0,0,0]
HAnimSegment846 = x3d.HAnimSegment()
HAnimSegment846.name = "l_forearm"
HAnimSegment846.DEF = "Boxman_l_forearm"
Inline847 = x3d.Inline()
Inline847.url = ["centres/l_forearm.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/centres/l_forearm.wrl"]

HAnimSegment846.children.append(Inline847)

HAnimJoint845.children.append(HAnimSegment846)
HAnimJoint848 = x3d.HAnimJoint()
HAnimJoint848.name = "l_wrist"
HAnimJoint848.DEF = "Boxman_l_wrist"
HAnimJoint848.center = [0.1972,0.8929,-0.069]
HAnimJoint848.skinCoordIndex = [192,193,194,195,196,197,198,199]
HAnimJoint848.skinCoordWeight = [1,1,1,1,1,1,1,1]
HAnimJoint848.ulimit = [0,0,0]
HAnimJoint848.llimit = [0,0,0]
HAnimSegment849 = x3d.HAnimSegment()
HAnimSegment849.name = "l_hand"
HAnimSegment849.DEF = "Boxman_l_hand"
Inline850 = x3d.Inline()
Inline850.url = ["centres/l_hand.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/centres/l_hand.wrl"]

HAnimSegment849.children.append(Inline850)
HAnimSite851 = x3d.HAnimSite()
HAnimSite851.name = "l_hand_tip"
HAnimSite851.DEF = "Boxman_l_hand_tip"
HAnimSite851.translation = [0.1912,0.6976,-0.071]

HAnimSegment849.children.append(HAnimSite851)
Inline852 = x3d.Inline()
Inline852.url = ["centres/l_hand_tip.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/centres/l_hand_tip.wrl"]

HAnimSegment849.children.append(Inline852)

HAnimJoint848.children.append(HAnimSegment849)

HAnimJoint845.children.append(HAnimJoint848)

HAnimJoint842.children.append(HAnimJoint845)

HAnimJoint834.children.append(HAnimJoint842)
HAnimJoint853 = x3d.HAnimJoint()
HAnimJoint853.name = "r_shoulder"
HAnimJoint853.DEF = "Boxman_r_shoulder"
HAnimJoint853.center = [-0.1968,1.4642,-0.0265]
HAnimJoint853.skinCoordIndex = [200,201,202,203,204,205,206,207]
HAnimJoint853.skinCoordWeight = [1,1,1,1,1,1,1,1]
HAnimJoint853.ulimit = [0,0,0]
HAnimJoint853.llimit = [0,0,0]
HAnimSegment854 = x3d.HAnimSegment()
HAnimSegment854.name = "r_upperarm"
HAnimSegment854.DEF = "Boxman_r_upperarm"
Inline855 = x3d.Inline()
Inline855.url = ["centres/r_upperarm.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/centres/r_upperarm.wrl"]

HAnimSegment854.children.append(Inline855)

HAnimJoint853.children.append(HAnimSegment854)
HAnimJoint856 = x3d.HAnimJoint()
HAnimJoint856.name = "r_elbow"
HAnimJoint856.DEF = "Boxman_r_elbow"
HAnimJoint856.center = [-0.1982,1.1622,-0.0557]
HAnimJoint856.skinCoordIndex = [208,209,210,211,212,213,214,215]
HAnimJoint856.skinCoordWeight = [1,1,1,1,1,1,1,1]
HAnimJoint856.ulimit = [0,0,0]
HAnimJoint856.llimit = [0,0,0]
HAnimSegment857 = x3d.HAnimSegment()
HAnimSegment857.name = "r_forearm"
HAnimSegment857.DEF = "Boxman_r_forearm"
Inline858 = x3d.Inline()
Inline858.url = ["centres/r_forearm.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/centres/r_forearm.wrl"]

HAnimSegment857.children.append(Inline858)

HAnimJoint856.children.append(HAnimSegment857)
HAnimJoint859 = x3d.HAnimJoint()
HAnimJoint859.name = "r_wrist"
HAnimJoint859.DEF = "Boxman_r_wrist"
HAnimJoint859.center = [-0.1972,0.8929,-0.069]
HAnimJoint859.skinCoordIndex = [216,217,218,219,220,221,222,223]
HAnimJoint859.skinCoordWeight = [1,1,1,1,1,1,1,1]
HAnimJoint859.ulimit = [0,0,0]
HAnimJoint859.llimit = [0,0,0]
HAnimSegment860 = x3d.HAnimSegment()
HAnimSegment860.name = "r_hand"
HAnimSegment860.DEF = "Boxman_r_hand"
Inline861 = x3d.Inline()
Inline861.url = ["centres/r_hand.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/centres/r_hand.wrl"]

HAnimSegment860.children.append(Inline861)
HAnimSite862 = x3d.HAnimSite()
HAnimSite862.name = "r_hand_tip"
HAnimSite862.DEF = "Boxman_r_hand_tip"
HAnimSite862.translation = [-0.1912,0.6976,-0.071]

HAnimSegment860.children.append(HAnimSite862)
Inline863 = x3d.Inline()
Inline863.url = ["centres/r_hand_tip.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/centres/r_hand_tip.wrl"]

HAnimSegment860.children.append(Inline863)

HAnimJoint859.children.append(HAnimSegment860)

HAnimJoint856.children.append(HAnimJoint859)

HAnimJoint853.children.append(HAnimJoint856)

HAnimJoint834.children.append(HAnimJoint853)

HAnimJoint803.children.append(HAnimJoint834)

HAnimHumanoid802.skeleton.append(HAnimJoint803)
## sacrum (12) # l_thigh (28) # l_calf (24) # l_hindfoot (8) # l_middistal (8) # r_thigh (28) # r_calf (24) # r_hindfoot (8) # r_middistal (8) # l5 (20) # skull (8) # l_upperarm (8) # l_forearm (8) # l_hand (8) # r_upperarm (8) # r_forearm (8) # r_hand (8)
Coordinate864 = x3d.Coordinate()
Coordinate864.DEF = "SKINCOORD"

HAnimHumanoid802.skinCoord = Coordinate864
Group865 = x3d.Group()
Shape866 = x3d.Shape()
Shape866.DEF = "TrouserSkin"
Appearance867 = x3d.Appearance()
Material868 = x3d.Material()
Material868.diffuseColor = [0,0,1]
Material868.transparency = 0.5

Appearance867.material = Material868

Shape866.appearance = Appearance867
## 0: sacrum (8) # 1: l_hip joint (8) # 2: r_hip joint (8) # 3: l_thigh (48) # 4: l_knee joint (8) # 5: l_calf (40) # 10: r_thigh (48) # 11: r_knee joint (8) # 12: r_calf (40)
IndexedFaceSet869 = x3d.IndexedFaceSet()
IndexedFaceSet869.coordIndex = [0,7,1,-1,8,0,1,-1,1,9,8,-1,10,2,3,-1,3,11,10,-1,2,4,5,-1,5,3,2,-1,4,6,5,-1,7,12,1,-1,1,12,13,-1,13,9,1,-1,9,13,14,-1,14,10,9,-1,10,14,15,-1,15,2,10,-1,12,7,6,-1,6,15,12,-1,15,6,4,-1,4,2,15,-1,0,80,7,-1,81,80,0,-1,0,8,81,-1,82,81,8,-1,8,11,82,-1,83,82,11,-1,11,3,83,-1,6,7,80,-1,80,83,6,-1,5,6,83,-1,83,3,5,-1,12,16,17,-1,17,13,12,-1,13,17,18,-1,18,14,13,-1,14,18,19,-1,19,15,14,-1,15,19,16,-1,16,12,15,-1,16,20,21,-1,21,17,16,-1,17,21,22,-1,22,18,17,-1,18,22,23,-1,23,19,18,-1,19,23,20,-1,20,16,19,-1,20,24,25,-1,25,21,20,-1,21,25,26,-1,26,22,21,-1,22,26,27,-1,27,23,22,-1,23,27,24,-1,24,20,23,-1,24,28,29,-1,29,25,24,-1,25,29,30,-1,30,26,25,-1,26,30,31,-1,31,27,26,-1,27,31,28,-1,28,24,27,-1,28,32,33,-1,33,29,28,-1,29,33,34,-1,34,30,29,-1,30,34,35,-1,35,31,30,-1,31,35,32,-1,32,28,31,-1,32,36,37,-1,37,33,32,-1,33,37,38,-1,38,34,33,-1,34,38,39,-1,39,35,34,-1,35,39,36,-1,36,32,35,-1,36,40,41,-1,41,37,36,-1,37,41,42,-1,42,38,37,-1,38,42,43,-1,43,39,38,-1,39,43,40,-1,40,36,39,-1,40,44,45,-1,45,41,40,-1,41,45,46,-1,46,42,41,-1,42,46,47,-1,47,43,42,-1,43,47,44,-1,44,40,43,-1,44,48,49,-1,49,45,44,-1,45,49,50,-1,50,46,45,-1,46,50,51,-1,51,47,46,-1,47,51,48,-1,48,44,47,-1,48,52,53,-1,53,49,48,-1,49,53,54,-1,54,50,49,-1,50,54,55,-1,55,51,50,-1,51,55,52,-1,52,48,51,-1,52,56,57,-1,57,53,52,-1,53,57,58,-1,58,54,53,-1,54,58,59,-1,59,55,54,-1,55,59,56,-1,56,52,55,-1,56,60,61,-1,61,57,56,-1,57,61,62,-1,62,58,57,-1,58,62,63,-1,63,59,58,-1,59,63,60,-1,60,56,59,-1,81,85,84,-1,84,80,81,-1,82,86,85,-1,85,81,82,-1,83,87,86,-1,86,82,83,-1,80,84,87,-1,87,83,80,-1,85,89,88,-1,88,84,85,-1,86,90,89,-1,89,85,86,-1,87,91,90,-1,90,86,87,-1,84,88,91,-1,91,87,84,-1,89,93,92,-1,92,88,89,-1,90,94,93,-1,93,89,90,-1,91,95,94,-1,94,90,91,-1,88,92,95,-1,95,91,88,-1,93,97,96,-1,96,92,93,-1,94,98,97,-1,97,93,94,-1,95,99,98,-1,98,94,95,-1,92,96,99,-1,99,95,92,-1,97,101,100,-1,100,96,97,-1,98,102,101,-1,101,97,98,-1,99,103,102,-1,102,98,99,-1,96,100,103,-1,103,99,96,-1,101,105,104,-1,104,100,101,-1,102,106,105,-1,105,101,102,-1,103,107,106,-1,106,102,103,-1,100,104,107,-1,107,103,100,-1,105,109,108,-1,108,104,105,-1,106,110,109,-1,109,105,106,-1,107,111,110,-1,110,106,107,-1,104,108,111,-1,111,107,104,-1,109,113,112,-1,112,108,109,-1,110,114,113,-1,113,109,110,-1,111,115,114,-1,114,110,111,-1,108,112,115,-1,115,111,108,-1,113,117,116,-1,116,112,113,-1,114,118,117,-1,117,113,114,-1,115,119,118,-1,118,114,115,-1,112,116,119,-1,119,115,112,-1,117,121,120,-1,120,116,117,-1,118,122,121,-1,121,117,118,-1,119,123,122,-1,122,118,119,-1,116,120,123,-1,123,119,116,-1,121,125,124,-1,124,120,121,-1,122,126,125,-1,125,121,122,-1,123,127,126,-1,126,122,123,-1,120,124,127,-1,127,123,120,-1,125,129,128,-1,128,124,125,-1,126,130,129,-1,129,125,126,-1,127,131,130,-1,130,126,127,-1,124,128,131,-1,131,127,124,-1]
Coordinate870 = x3d.Coordinate()
Coordinate870.USE = "SKINCOORD"

IndexedFaceSet869.coord = Coordinate870

Shape866.geometry = IndexedFaceSet869

Group865.children.append(Shape866)
Shape871 = x3d.Shape()
Shape871.DEF = "ShoeSkin"
Appearance872 = x3d.Appearance()
Material873 = x3d.Material()
Material873.diffuseColor = [0,0,0]
Material873.transparency = 0.5

Appearance872.material = Material873

Shape871.appearance = Appearance872
## 6: l_ankle joint (8) # 7: l_hindfoot (8) # 8: l_midtarsal joint (8) # 9: l_middistal (10) # 13: r_ankle joint (8) # 14: r_hindfoot (8) # 15: r_midtarsal joint (8) # 16: r_middistal (10)
IndexedFaceSet874 = x3d.IndexedFaceSet()
IndexedFaceSet874.coordIndex = [60,64,65,-1,65,61,60,-1,61,65,66,-1,66,62,61,-1,62,66,67,-1,67,63,62,-1,63,67,64,-1,64,60,63,-1,64,68,69,-1,69,65,64,-1,65,69,70,-1,70,66,65,-1,66,70,71,-1,71,67,66,-1,67,71,68,-1,68,64,67,-1,68,72,73,-1,73,69,68,-1,69,73,74,-1,74,70,69,-1,70,74,75,-1,75,71,70,-1,71,75,72,-1,72,68,71,-1,72,76,77,-1,77,73,72,-1,73,77,78,-1,78,74,73,-1,74,78,79,-1,79,75,74,-1,75,79,76,-1,76,72,75,-1,76,79,78,-1,78,77,76,-1,129,133,132,-1,132,128,129,-1,130,134,133,-1,133,129,130,-1,131,135,134,-1,134,130,131,-1,128,132,135,-1,135,131,128,-1,133,137,136,-1,136,132,133,-1,134,138,137,-1,137,133,134,-1,135,139,138,-1,138,134,135,-1,132,136,139,-1,139,135,132,-1,137,141,140,-1,140,136,137,-1,138,142,141,-1,141,137,138,-1,139,143,142,-1,142,138,139,-1,136,140,143,-1,143,139,136,-1,141,145,144,-1,144,140,141,-1,142,146,145,-1,145,141,142,-1,143,147,146,-1,146,142,143,-1,140,144,147,-1,147,143,140,-1,145,146,147,-1,147,144,145,-1]
Coordinate875 = x3d.Coordinate()
Coordinate875.USE = "SKINCOORD"

IndexedFaceSet874.coord = Coordinate875

Shape871.geometry = IndexedFaceSet874

Group865.children.append(Shape871)
Shape876 = x3d.Shape()
Shape876.DEF = "ShirtSkin"
Appearance877 = x3d.Appearance()
Material878 = x3d.Material()
Material878.diffuseColor = [1,1,0]
Material878.transparency = 0.5

Appearance877.material = Material878

Shape876.appearance = Appearance877
## 17: vl5_joint (8) # 18: l5 (28) # 21: l_shoulder joint (8) # 22: l_upperarm (8) # 23: l_elbow joint (8) # 24: l_forearm (8) # 27: r_shoulder joint (8) # 28: r_upperarm (8) # 29: r_elbow joint (8) # 30: r_forearm (8)
IndexedFaceSet879 = x3d.IndexedFaceSet()
IndexedFaceSet879.coordIndex = [148,8,9,-1,9,149,148,-1,149,9,10,-1,10,150,149,-1,150,10,11,-1,11,151,150,-1,151,11,8,-1,8,148,151,-1,152,148,149,-1,149,153,152,-1,153,149,150,-1,150,154,153,-1,154,150,151,-1,151,155,154,-1,155,151,148,-1,148,152,155,-1,156,152,153,-1,153,157,156,-1,158,154,155,-1,155,159,158,-1,160,156,157,-1,157,161,160,-1,161,157,158,-1,158,162,161,-1,162,158,159,-1,159,163,162,-1,163,159,156,-1,156,160,163,-1,164,160,161,-1,161,165,164,-1,165,161,162,-1,162,166,165,-1,166,162,163,-1,163,167,166,-1,167,163,160,-1,160,164,167,-1,153,176,177,-1,177,157,153,-1,157,177,178,-1,178,158,157,-1,158,178,179,-1,179,154,158,-1,154,179,176,-1,176,153,154,-1,176,180,181,-1,181,177,176,-1,177,181,182,-1,182,178,177,-1,178,182,183,-1,183,179,178,-1,179,183,180,-1,180,176,179,-1,180,184,185,-1,185,181,180,-1,181,185,186,-1,186,182,181,-1,182,186,187,-1,187,183,182,-1,183,187,184,-1,184,180,183,-1,184,188,189,-1,189,185,184,-1,185,189,190,-1,190,186,185,-1,186,190,191,-1,191,187,186,-1,187,191,188,-1,188,184,187,-1,152,156,201,-1,201,200,152,-1,156,159,202,-1,202,201,156,-1,159,155,203,-1,203,202,159,-1,155,152,200,-1,200,203,155,-1,201,205,204,-1,204,200,201,-1,202,206,205,-1,205,201,202,-1,203,207,206,-1,206,202,203,-1,200,204,207,-1,207,203,200,-1,205,209,208,-1,208,204,205,-1,206,210,209,-1,209,205,206,-1,207,211,210,-1,210,206,207,-1,204,208,211,-1,211,207,204,-1,209,213,212,-1,212,208,209,-1,210,214,213,-1,213,209,210,-1,211,215,214,-1,214,210,211,-1,208,212,215,-1,215,211,208,-1]
Coordinate880 = x3d.Coordinate()
Coordinate880.USE = "SKINCOORD"

IndexedFaceSet879.coord = Coordinate880

Shape876.geometry = IndexedFaceSet879

Group865.children.append(Shape876)
Shape881 = x3d.Shape()
Shape881.DEF = "HeadHandsFleshToneSkin"
Appearance882 = x3d.Appearance()
Material883 = x3d.Material()
Material883.diffuseColor = [1,0.75,0.75]
Material883.transparency = 0.5

Appearance882.material = Material883

Shape881.appearance = Appearance882
## 19: skullbase joint (8) # 20: skull (10) # 25: l_wrist joint (8) # 26: l_hand (10) # 31: r_wrist joint (8) # 32: r_hand (10)
IndexedFaceSet884 = x3d.IndexedFaceSet()
IndexedFaceSet884.coordIndex = [172,164,165,-1,165,173,172,-1,173,165,166,-1,166,174,173,-1,174,166,167,-1,167,175,174,-1,175,167,164,-1,164,172,175,-1,168,172,173,-1,173,169,168,-1,169,173,174,-1,174,170,169,-1,170,174,175,-1,175,171,170,-1,171,175,172,-1,172,168,171,-1,171,168,169,-1,169,170,171,-1,188,192,193,-1,193,189,188,-1,189,193,194,-1,194,190,189,-1,190,194,195,-1,195,191,190,-1,191,195,192,-1,192,188,191,-1,192,196,197,-1,197,193,192,-1,193,197,198,-1,198,194,193,-1,194,198,199,-1,199,195,194,-1,195,199,196,-1,196,192,195,-1,196,199,198,-1,198,197,196,-1,213,217,216,-1,216,212,213,-1,214,218,217,-1,217,213,214,-1,215,219,218,-1,218,214,215,-1,212,216,219,-1,219,215,212,-1,217,221,220,-1,220,216,217,-1,218,222,221,-1,221,217,218,-1,219,223,222,-1,222,218,219,-1,216,220,223,-1,223,219,216,-1,221,222,223,-1,223,220,221,-1]
Coordinate885 = x3d.Coordinate()
Coordinate885.USE = "SKINCOORD"

IndexedFaceSet884.coord = Coordinate885

Shape881.geometry = IndexedFaceSet884

Group865.children.append(Shape881)
Shape886 = x3d.Shape()
Shape886.DEF = "SkinLines"
Appearance887 = x3d.Appearance()
Material888 = x3d.Material()
Material888.diffuseColor = [0,0,0]

Appearance887.material = Material888

Shape886.appearance = Appearance887
#Combined set of prior IFS coordIndex values
IndexedLineSet889 = x3d.IndexedLineSet()
IndexedLineSet889.coordIndex = [0,7,1,-1,8,0,1,-1,1,9,8,-1,10,2,3,-1,3,11,10,-1,2,4,5,-1,5,3,2,-1,4,6,5,-1,7,12,1,-1,1,12,13,-1,13,9,1,-1,9,13,14,-1,14,10,9,-1,10,14,15,-1,15,2,10,-1,12,7,6,-1,6,15,12,-1,15,6,4,-1,4,2,15,-1,0,80,7,-1,81,80,0,-1,0,8,81,-1,82,81,8,-1,8,11,82,-1,83,82,11,-1,11,3,83,-1,6,7,80,-1,80,83,6,-1,5,6,83,-1,83,3,5,-1,12,16,17,-1,17,13,12,-1,13,17,18,-1,18,14,13,-1,14,18,19,-1,19,15,14,-1,15,19,16,-1,16,12,15,-1,16,20,21,-1,21,17,16,-1,17,21,22,-1,22,18,17,-1,18,22,23,-1,23,19,18,-1,19,23,20,-1,20,16,19,-1,20,24,25,-1,25,21,20,-1,21,25,26,-1,26,22,21,-1,22,26,27,-1,27,23,22,-1,23,27,24,-1,24,20,23,-1,24,28,29,-1,29,25,24,-1,25,29,30,-1,30,26,25,-1,26,30,31,-1,31,27,26,-1,27,31,28,-1,28,24,27,-1,28,32,33,-1,33,29,28,-1,29,33,34,-1,34,30,29,-1,30,34,35,-1,35,31,30,-1,31,35,32,-1,32,28,31,-1,32,36,37,-1,37,33,32,-1,33,37,38,-1,38,34,33,-1,34,38,39,-1,39,35,34,-1,35,39,36,-1,36,32,35,-1,36,40,41,-1,41,37,36,-1,37,41,42,-1,42,38,37,-1,38,42,43,-1,43,39,38,-1,39,43,40,-1,40,36,39,-1,40,44,45,-1,45,41,40,-1,41,45,46,-1,46,42,41,-1,42,46,47,-1,47,43,42,-1,43,47,44,-1,44,40,43,-1,44,48,49,-1,49,45,44,-1,45,49,50,-1,50,46,45,-1,46,50,51,-1,51,47,46,-1,47,51,48,-1,48,44,47,-1,48,52,53,-1,53,49,48,-1,49,53,54,-1,54,50,49,-1,50,54,55,-1,55,51,50,-1,51,55,52,-1,52,48,51,-1,52,56,57,-1,57,53,52,-1,53,57,58,-1,58,54,53,-1,54,58,59,-1,59,55,54,-1,55,59,56,-1,56,52,55,-1,56,60,61,-1,61,57,56,-1,57,61,62,-1,62,58,57,-1,58,62,63,-1,63,59,58,-1,59,63,60,-1,60,56,59,-1,81,85,84,-1,84,80,81,-1,82,86,85,-1,85,81,82,-1,83,87,86,-1,86,82,83,-1,80,84,87,-1,87,83,80,-1,85,89,88,-1,88,84,85,-1,86,90,89,-1,89,85,86,-1,87,91,90,-1,90,86,87,-1,84,88,91,-1,91,87,84,-1,89,93,92,-1,92,88,89,-1,90,94,93,-1,93,89,90,-1,91,95,94,-1,94,90,91,-1,88,92,95,-1,95,91,88,-1,93,97,96,-1,96,92,93,-1,94,98,97,-1,97,93,94,-1,95,99,98,-1,98,94,95,-1,92,96,99,-1,99,95,92,-1,97,101,100,-1,100,96,97,-1,98,102,101,-1,101,97,98,-1,99,103,102,-1,102,98,99,-1,96,100,103,-1,103,99,96,-1,101,105,104,-1,104,100,101,-1,102,106,105,-1,105,101,102,-1,103,107,106,-1,106,102,103,-1,100,104,107,-1,107,103,100,-1,105,109,108,-1,108,104,105,-1,106,110,109,-1,109,105,106,-1,107,111,110,-1,110,106,107,-1,104,108,111,-1,111,107,104,-1,109,113,112,-1,112,108,109,-1,110,114,113,-1,113,109,110,-1,111,115,114,-1,114,110,111,-1,108,112,115,-1,115,111,108,-1,113,117,116,-1,116,112,113,-1,114,118,117,-1,117,113,114,-1,115,119,118,-1,118,114,115,-1,112,116,119,-1,119,115,112,-1,117,121,120,-1,120,116,117,-1,118,122,121,-1,121,117,118,-1,119,123,122,-1,122,118,119,-1,116,120,123,-1,123,119,116,-1,121,125,124,-1,124,120,121,-1,122,126,125,-1,125,121,122,-1,123,127,126,-1,126,122,123,-1,120,124,127,-1,127,123,120,-1,125,129,128,-1,128,124,125,-1,126,130,129,-1,129,125,126,-1,127,131,130,-1,130,126,127,-1,124,128,131,-1,131,127,124,-1,60,64,65,-1,65,61,60,-1,61,65,66,-1,66,62,61,-1,62,66,67,-1,67,63,62,-1,63,67,64,-1,64,60,63,-1,64,68,69,-1,69,65,64,-1,65,69,70,-1,70,66,65,-1,66,70,71,-1,71,67,66,-1,67,71,68,-1,68,64,67,-1,68,72,73,-1,73,69,68,-1,69,73,74,-1,74,70,69,-1,70,74,75,-1,75,71,70,-1,71,75,72,-1,72,68,71,-1,72,76,77,-1,77,73,72,-1,73,77,78,-1,78,74,73,-1,74,78,79,-1,79,75,74,-1,75,79,76,-1,76,72,75,-1,76,79,78,-1,78,77,76,-1,129,133,132,-1,132,128,129,-1,130,134,133,-1,133,129,130,-1,131,135,134,-1,134,130,131,-1,128,132,135,-1,135,131,128,-1,133,137,136,-1,136,132,133,-1,134,138,137,-1,137,133,134,-1,135,139,138,-1,138,134,135,-1,132,136,139,-1,139,135,132,-1,137,141,140,-1,140,136,137,-1,138,142,141,-1,141,137,138,-1,139,143,142,-1,142,138,139,-1,136,140,143,-1,143,139,136,-1,141,145,144,-1,144,140,141,-1,142,146,145,-1,145,141,142,-1,143,147,146,-1,146,142,143,-1,140,144,147,-1,147,143,140,-1,145,146,147,-1,147,144,145,-1,148,8,9,-1,9,149,148,-1,149,9,10,-1,10,150,149,-1,150,10,11,-1,11,151,150,-1,151,11,8,-1,8,148,151,-1,152,148,149,-1,149,153,152,-1,153,149,150,-1,150,154,153,-1,154,150,151,-1,151,155,154,-1,155,151,148,-1,148,152,155,-1,156,152,153,-1,153,157,156,-1,158,154,155,-1,155,159,158,-1,160,156,157,-1,157,161,160,-1,161,157,158,-1,158,162,161,-1,162,158,159,-1,159,163,162,-1,163,159,156,-1,156,160,163,-1,164,160,161,-1,161,165,164,-1,165,161,162,-1,162,166,165,-1,166,162,163,-1,163,167,166,-1,167,163,160,-1,160,164,167,-1,153,176,177,-1,177,157,153,-1,157,177,178,-1,178,158,157,-1,158,178,179,-1,179,154,158,-1,154,179,176,-1,176,153,154,-1,176,180,181,-1,181,177,176,-1,177,181,182,-1,182,178,177,-1,178,182,183,-1,183,179,178,-1,179,183,180,-1,180,176,179,-1,180,184,185,-1,185,181,180,-1,181,185,186,-1,186,182,181,-1,182,186,187,-1,187,183,182,-1,183,187,184,-1,184,180,183,-1,184,188,189,-1,189,185,184,-1,185,189,190,-1,190,186,185,-1,186,190,191,-1,191,187,186,-1,187,191,188,-1,188,184,187,-1,152,156,201,-1,201,200,152,-1,156,159,202,-1,202,201,156,-1,159,155,203,-1,203,202,159,-1,155,152,200,-1,200,203,155,-1,201,205,204,-1,204,200,201,-1,202,206,205,-1,205,201,202,-1,203,207,206,-1,206,202,203,-1,200,204,207,-1,207,203,200,-1,205,209,208,-1,208,204,205,-1,206,210,209,-1,209,205,206,-1,207,211,210,-1,210,206,207,-1,204,208,211,-1,211,207,204,-1,209,213,212,-1,212,208,209,-1,210,214,213,-1,213,209,210,-1,211,215,214,-1,214,210,211,-1,208,212,215,-1,215,211,208,-1,172,164,165,-1,165,173,172,-1,173,165,166,-1,166,174,173,-1,174,166,167,-1,167,175,174,-1,175,167,164,-1,164,172,175,-1,168,172,173,-1,173,169,168,-1,169,173,174,-1,174,170,169,-1,170,174,175,-1,175,171,170,-1,171,175,172,-1,172,168,171,-1,171,168,169,-1,169,170,171,-1,188,192,193,-1,193,189,188,-1,189,193,194,-1,194,190,189,-1,190,194,195,-1,195,191,190,-1,191,195,192,-1,192,188,191,-1,192,196,197,-1,197,193,192,-1,193,197,198,-1,198,194,193,-1,194,198,199,-1,199,195,194,-1,195,199,196,-1,196,192,195,-1,196,199,198,-1,198,197,196,-1,213,217,216,-1,216,212,213,-1,214,218,217,-1,217,213,214,-1,215,219,218,-1,218,214,215,-1,212,216,219,-1,219,215,212,-1,217,221,220,-1,220,216,217,-1,218,222,221,-1,221,217,218,-1,219,223,222,-1,222,218,219,-1,216,220,223,-1,223,219,216,-1,221,222,223,-1,223,220,221,-1]
Coordinate890 = x3d.Coordinate()
Coordinate890.USE = "SKINCOORD"

IndexedLineSet889.coord = Coordinate890

Shape886.geometry = IndexedLineSet889

Group865.children.append(Shape886)

HAnimHumanoid802.skin.append(Group865)
HAnimJoint891 = x3d.HAnimJoint()
HAnimJoint891.USE = "Boxman_humanoid_root"

HAnimHumanoid802.joints.append(HAnimJoint891)
HAnimJoint892 = x3d.HAnimJoint()
HAnimJoint892.USE = "Boxman_skullbase"

HAnimHumanoid802.joints.append(HAnimJoint892)
HAnimJoint893 = x3d.HAnimJoint()
HAnimJoint893.USE = "Boxman_vl5"

HAnimHumanoid802.joints.append(HAnimJoint893)
HAnimJoint894 = x3d.HAnimJoint()
HAnimJoint894.USE = "Boxman_r_ankle"

HAnimHumanoid802.joints.append(HAnimJoint894)
HAnimJoint895 = x3d.HAnimJoint()
HAnimJoint895.USE = "Boxman_l_ankle"

HAnimHumanoid802.joints.append(HAnimJoint895)
HAnimJoint896 = x3d.HAnimJoint()
HAnimJoint896.USE = "Boxman_r_elbow"

HAnimHumanoid802.joints.append(HAnimJoint896)
HAnimJoint897 = x3d.HAnimJoint()
HAnimJoint897.USE = "Boxman_l_elbow"

HAnimHumanoid802.joints.append(HAnimJoint897)
HAnimJoint898 = x3d.HAnimJoint()
HAnimJoint898.USE = "Boxman_r_hip"

HAnimHumanoid802.joints.append(HAnimJoint898)
HAnimJoint899 = x3d.HAnimJoint()
HAnimJoint899.USE = "Boxman_l_hip"

HAnimHumanoid802.joints.append(HAnimJoint899)
HAnimJoint900 = x3d.HAnimJoint()
HAnimJoint900.USE = "Boxman_l_knee"

HAnimHumanoid802.joints.append(HAnimJoint900)
HAnimJoint901 = x3d.HAnimJoint()
HAnimJoint901.USE = "Boxman_r_knee"

HAnimHumanoid802.joints.append(HAnimJoint901)
HAnimJoint902 = x3d.HAnimJoint()
HAnimJoint902.USE = "Boxman_r_midtarsal"

HAnimHumanoid802.joints.append(HAnimJoint902)
HAnimJoint903 = x3d.HAnimJoint()
HAnimJoint903.USE = "Boxman_l_midtarsal"

HAnimHumanoid802.joints.append(HAnimJoint903)
HAnimJoint904 = x3d.HAnimJoint()
HAnimJoint904.USE = "Boxman_r_shoulder"

HAnimHumanoid802.joints.append(HAnimJoint904)
HAnimJoint905 = x3d.HAnimJoint()
HAnimJoint905.USE = "Boxman_l_shoulder"

HAnimHumanoid802.joints.append(HAnimJoint905)
HAnimJoint906 = x3d.HAnimJoint()
HAnimJoint906.USE = "Boxman_r_wrist"

HAnimHumanoid802.joints.append(HAnimJoint906)
HAnimJoint907 = x3d.HAnimJoint()
HAnimJoint907.USE = "Boxman_l_wrist"

HAnimHumanoid802.joints.append(HAnimJoint907)
HAnimSegment908 = x3d.HAnimSegment()
HAnimSegment908.USE = "Boxman_sacrum"

HAnimHumanoid802.segments.append(HAnimSegment908)
HAnimSegment909 = x3d.HAnimSegment()
HAnimSegment909.USE = "Boxman_l5"

HAnimHumanoid802.segments.append(HAnimSegment909)
HAnimSegment910 = x3d.HAnimSegment()
HAnimSegment910.USE = "Boxman_skull"

HAnimHumanoid802.segments.append(HAnimSegment910)
HAnimSegment911 = x3d.HAnimSegment()
HAnimSegment911.USE = "Boxman_l_calf"

HAnimHumanoid802.segments.append(HAnimSegment911)
HAnimSegment912 = x3d.HAnimSegment()
HAnimSegment912.USE = "Boxman_r_calf"

HAnimHumanoid802.segments.append(HAnimSegment912)
HAnimSegment913 = x3d.HAnimSegment()
HAnimSegment913.USE = "Boxman_l_forearm"

HAnimHumanoid802.segments.append(HAnimSegment913)
HAnimSegment914 = x3d.HAnimSegment()
HAnimSegment914.USE = "Boxman_r_forearm"

HAnimHumanoid802.segments.append(HAnimSegment914)
HAnimSegment915 = x3d.HAnimSegment()
HAnimSegment915.USE = "Boxman_l_hand"

HAnimHumanoid802.segments.append(HAnimSegment915)
HAnimSegment916 = x3d.HAnimSegment()
HAnimSegment916.USE = "Boxman_r_hand"

HAnimHumanoid802.segments.append(HAnimSegment916)
HAnimSegment917 = x3d.HAnimSegment()
HAnimSegment917.USE = "Boxman_l_hindfoot"

HAnimHumanoid802.segments.append(HAnimSegment917)
HAnimSegment918 = x3d.HAnimSegment()
HAnimSegment918.USE = "Boxman_r_hindfoot"

HAnimHumanoid802.segments.append(HAnimSegment918)
HAnimSegment919 = x3d.HAnimSegment()
HAnimSegment919.USE = "Boxman_l_middistal"

HAnimHumanoid802.segments.append(HAnimSegment919)
HAnimSegment920 = x3d.HAnimSegment()
HAnimSegment920.USE = "Boxman_r_middistal"

HAnimHumanoid802.segments.append(HAnimSegment920)
HAnimSegment921 = x3d.HAnimSegment()
HAnimSegment921.USE = "Boxman_l_thigh"

HAnimHumanoid802.segments.append(HAnimSegment921)
HAnimSegment922 = x3d.HAnimSegment()
HAnimSegment922.USE = "Boxman_r_thigh"

HAnimHumanoid802.segments.append(HAnimSegment922)
HAnimSegment923 = x3d.HAnimSegment()
HAnimSegment923.USE = "Boxman_l_upperarm"

HAnimHumanoid802.segments.append(HAnimSegment923)
HAnimSegment924 = x3d.HAnimSegment()
HAnimSegment924.USE = "Boxman_r_upperarm"

HAnimHumanoid802.segments.append(HAnimSegment924)
HAnimSite925 = x3d.HAnimSite()
HAnimSite925.USE = "Boxman_skull_tip"

HAnimHumanoid802.sites.append(HAnimSite925)
HAnimSite926 = x3d.HAnimSite()
HAnimSite926.USE = "Boxman_l_hand_tip"

HAnimHumanoid802.sites.append(HAnimSite926)
HAnimSite927 = x3d.HAnimSite()
HAnimSite927.USE = "Boxman_r_hand_tip"

HAnimHumanoid802.sites.append(HAnimSite927)
HAnimSite928 = x3d.HAnimSite()
HAnimSite928.USE = "Boxman_l_middistal_tip"

HAnimHumanoid802.sites.append(HAnimSite928)
HAnimSite929 = x3d.HAnimSite()
HAnimSite929.USE = "Boxman_r_middistal_tip"

HAnimHumanoid802.sites.append(HAnimSite929)

Switch291.children.append(HAnimHumanoid802)
Script930 = x3d.Script()
Script930.DEF = "ENGINE"
Script930.directOutput = True
field931 = x3d.field()
field931.name = "update"
field931.accessType = "inputOnly"
field931.type = "SFRotation"

Script930.field.append(field931)
field932 = x3d.field()
field932.name = "humanoid"
field932.accessType = "initializeOnly"
field932.type = "SFNode"
HAnimHumanoid933 = x3d.HAnimHumanoid()
HAnimHumanoid933.USE = "Boxman_Humanoid"

field932.children.append(HAnimHumanoid933)

Script930.field.append(field932)
field934 = x3d.field()
field934.name = "coordList"
field934.accessType = "initializeOnly"
field934.type = "MFVec3f"

Script930.field.append(field934)
field935 = x3d.field()
field935.name = "joint"
field935.accessType = "initializeOnly"
field935.type = "SFNode"
#NULL node

Script930.field.append(field935)
field936 = x3d.field()
field936.name = "translation"
field936.accessType = "initializeOnly"
field936.type = "SFVec3f"
field936.value = [0,0,0]

Script930.field.append(field936)
field937 = x3d.field()
field937.name = "rotation"
field937.accessType = "initializeOnly"
field937.type = "SFRotation"
field937.value = [1,0,0,0]

Script930.field.append(field937)
field938 = x3d.field()
field938.name = "scale"
field938.accessType = "initializeOnly"
field938.type = "SFVec3f"
field938.value = [1,1,1]

Script930.field.append(field938)

Script930.sourceCode = '''ecmascript:\n"+
"      // Initialises the script\n"+
"      function initialize() {\n"+
"         // Copy coord list into local storage\n"+
"         coordList = humanoid.skinCoord.point;\n"+
"      }\n"+
"      // Transforms the vertices related to a joint\n"+
"      function Transform() {\n"+
"         // Make sure that this is a joint\n"+
"         var iNumJoints = humanoid.joints.length;\n"+
"         var bIsJoint = false;\n"+
"         var j;\n"+
"         for (j=0; (j<iNumJoints) && (bIsJoint==false); j++) {\n"+
"            if (humanoid.joints[j].name == joint.name) bIsJoint = true;\n"+
"         }\n"+
"         // If it is, we process the data\n"+
"         if (bIsJoint) {\n"+
"            // Read in current joint\n"+
"            var currentJoint = joint;\n"+
"            // Read in current matrix\n"+
"            var currentMatrix = new VrmlMatrix();\n"+
"            currentMatrix.setTransform(translation,\n"+
"                                       rotation,\n"+
"                                       scale,\n"+
"                                       new SFRotation(1,0,0,0),\n"+
"                                       new SFVec3f(0,0,0));\n"+
"            // Create matrix corresponding to this joints transform\n"+
"            var newMatrix = new VrmlMatrix();\n"+
"            newMatrix.setTransform(currentJoint.translation,\n"+
"                                   currentJoint.rotation,\n"+
"                                   currentJoint.scale,\n"+
"                                   currentJoint.scaleOrientation,\n"+
"                                   currentJoint.center);\n"+
"            // Update current matrix with matrix from this joint\n"+
"            currentMatrix = newMatrix.multRight(currentMatrix);\n"+
"            // Transform all vertices associated with this joint\n"+
"//          var iNumAffectedVertices = currentJoint.affectedVertices.length;\n"+
"            var iNumAffectedVertices = currentJoint.skinCoordIndex.length;\n"+
"            var v;\n"+
"            for (v=0; v<iNumAffectedVertices; v++) {\n"+
"//             var vertex = currentJoint.affectedVertices[v];\n"+
"//             var weight = currentJoint.vertexWeights[v];\n"+
"               var vertex = currentJoint.skinCoordIndex[v];\n"+
"               var weight = currentJoint.skinCoordWeight[v];\n"+
"               var newVertex = currentMatrix.multVecMatrix(coordList[vertex]).multiply(weight);\n"+
"               humanoid.skinCoord.point[vertex] = humanoid.skinCoord.point[vertex].add(newVertex);\n"+
"            }\n"+
"            // Transform all children\n"+
"            var children = currentJoint.children;\n"+
"            var iNumChildren = children.length;\n"+
"            var c;\n"+
"            for (c=0; c<iNumChildren; c++) {\n"+
"               joint = children[c];\n"+
"               currentMatrix.getTransform(translation,rotation,scale);\n"+
"               Transform();\n"+
"            }\n"+
"         }\n"+
"      }\n"+
"      // Update event handler\n"+
"      function update(value,time) {\n"+
"         // Zero output data.\n"+
"         var iNumVertices = humanoid.skinCoord.point.length;\n"+
"         var v;\n"+
"         for (v=0; v<iNumVertices; v++) {\n"+
"            humanoid.skinCoord.point[v].x = 0;\n"+
"            humanoid.skinCoord.point[v].y = 0;\n"+
"            humanoid.skinCoord.point[v].z = 0;\n"+
"         }\n"+
"         // Initialise transform data\n"+
"         translation = new SFVec3f(0,0,0);\n"+
"         scale       = new SFVec3f(1,1,1);\n"+
"         rotation    = new SFRotation(0,0,1,0);\n"+
"         // First (and only) item in humanoidBody should be the humanoid_root.\n"+
"         // This is stored as the joint we want to do next\n"+
"         // This could do with being more robust, rather than a'should be ok'.\n"+
"//       joint = humanoid.humanoidBody[0];\n"+
"         joint = humanoid.skeleton[0];\n"+
"         // Call transform function\n"+
"         Transform();\n"+
"      }'''

Switch291.children.append(Script930)

Scene24.children.append(Switch291)
#**********Behavior Proto Instances***********
ProtoInstance939 = x3d.ProtoInstance()
ProtoInstance939.name = "LOA1_WalkAnimation"
ProtoInstance939.DEF = "WALK"

Scene24.children.append(ProtoInstance939)
ProtoInstance940 = x3d.ProtoInstance()
ProtoInstance940.name = "LOA1_RunAnimation"
ProtoInstance940.DEF = "RUN"

Scene24.children.append(ProtoInstance940)
ProtoInstance941 = x3d.ProtoInstance()
ProtoInstance941.name = "LOA1_JumpAnimation"
ProtoInstance941.DEF = "JUMP"

Scene24.children.append(ProtoInstance941)
ProtoInstance942 = x3d.ProtoInstance()
ProtoInstance942.name = "LOA1_StandAnimation"
ProtoInstance942.DEF = "STAND"

Scene24.children.append(ProtoInstance942)
ProtoInstance943 = x3d.ProtoInstance()
ProtoInstance943.name = "LOA1_KneelAnimation"
ProtoInstance943.DEF = "KNEEL"

Scene24.children.append(ProtoInstance943)
Group944 = x3d.Group()
Group944.DEF = "Interface"
Transform945 = x3d.Transform()
ProximitySensor946 = x3d.ProximitySensor()
ProximitySensor946.DEF = "HudProx"
ProximitySensor946.center = [0,20,0]
ProximitySensor946.size = [500,100,500]

Transform945.children.append(ProximitySensor946)

Group944.children.append(Transform945)
Collision947 = x3d.Collision()
Collision947.DEF = "HUD"
Collision947.enabled = False
Transform948 = x3d.Transform()
Transform948.DEF = "HudXform"
Transform949 = x3d.Transform()
Transform949.scale = [0.012,0.012,0.012]
Transform949.translation = [-0.005,-0.025,-0.08]
Transform950 = x3d.Transform()
Transform950.DEF = "Stand_Text"
TouchSensor951 = x3d.TouchSensor()
TouchSensor951.DEF = "Stand_Touch"
TouchSensor951.description = "click for behavior"

Transform950.children.append(TouchSensor951)
Shape952 = x3d.Shape()
Shape952.DEF = "Stand"
IndexedFaceSet953 = x3d.IndexedFaceSet()
IndexedFaceSet953.coordIndex = [1,30,29,-1,1,29,2,-1,31,47,46,-1,31,46,32,-1,78,77,80,-1,78,80,79,-1,96,113,112,-1,96,112,95,-1,95,112,111,-1,95,111,94,-1,94,111,110,-1,94,110,93,-1,93,110,109,-1,93,109,108,-1,93,108,100,-1,107,99,100,-1,107,100,108,-1,107,106,99,-1,106,105,98,-1,106,98,99,-1,104,97,98,-1,104,98,105,-1,103,102,104,-1,104,102,101,-1,104,101,97,-1,101,96,97,-1,101,97,101,-1,101,101,96,-1,96,101,113,-1,113,101,114,-1,115,86,85,-1,115,85,116,-1,117,87,84,-1,117,84,118,-1,119,83,120,-1,121,88,82,-1,121,82,122,-1,123,89,81,-1,123,81,124,-1,125,90,126,-1,127,92,128,-1,129,91,130,-1,54,49,50,-1,54,50,55,-1,76,75,74,-1,76,74,54,-1,54,74,73,-1,54,73,49,-1,49,73,48,-1,48,73,62,-1,48,62,61,-1,48,61,60,-1,48,60,53,-1,53,60,59,-1,53,59,53,-1,53,59,58,-1,53,58,52,-1,52,58,57,-1,52,57,51,-1,56,51,57,-1,56,55,50,-1,56,50,51,-1,62,73,72,-1,62,72,63,-1,63,72,71,-1,63,71,64,-1,64,71,70,-1,64,70,69,-1,64,69,65,-1,65,69,68,-1,65,68,67,-1,65,67,66,-1,131,40,39,-1,131,39,132,-1,133,43,42,-1,133,42,134,-1,135,37,36,-1,135,36,136,-1,137,41,38,-1,137,38,138,-1,139,44,35,-1,139,35,140,-1,141,34,142,-1,143,45,33,-1,143,33,144,-1,145,16,15,-1,145,15,146,-1,147,14,148,-1,149,17,13,-1,149,13,150,-1,151,18,12,-1,151,12,152,-1,153,19,11,-1,153,11,154,-1,155,20,10,-1,155,10,156,-1,157,9,158,-1,159,21,8,-1,159,8,160,-1,161,22,7,-1,161,7,162,-1,163,23,164,-1,165,24,6,-1,165,6,166,-1,167,25,5,-1,167,5,168,-1,169,26,170,-1,171,27,4,-1,171,4,172,-1,173,28,3,-1,173,3,174,-1,175,0,176,-1]
Coordinate954 = x3d.Coordinate()

IndexedFaceSet953.coord = Coordinate954

Shape952.geometry = IndexedFaceSet953
Appearance955 = x3d.Appearance()
Material956 = x3d.Material()
Material956.DEF = "text_color"
Material956.ambientIntensity = 0
Material956.diffuseColor = [0,0,0]
Material956.emissiveColor = [0.819,0.521,0.169]

Appearance955.material = Material956

Shape952.appearance = Appearance955

Transform950.children.append(Shape952)
Transform957 = x3d.Transform()
Transform957.scale = [84.89,77.52,77.52]
Transform957.translation = [0.04092,1.843,3.826]
Shape958 = x3d.Shape()
Shape958.DEF = "Stand_Back"
IndexedFaceSet959 = x3d.IndexedFaceSet()
IndexedFaceSet959.coordIndex = [0,2,3,-1,2,0,1,-1]
Coordinate960 = x3d.Coordinate()

IndexedFaceSet959.coord = Coordinate960

Shape958.geometry = IndexedFaceSet959
Appearance961 = x3d.Appearance()
Material962 = x3d.Material()
Material962.DEF = "Clear"
Material962.ambientIntensity = 0
Material962.diffuseColor = [0,0,0]
Material962.transparency = 1

Appearance961.material = Material962

Shape958.appearance = Appearance961

Transform957.children.append(Shape958)

Transform950.children.append(Transform957)

Transform949.children.append(Transform950)
Transform963 = x3d.Transform()
Transform963.DEF = "Walk_Text"
TouchSensor964 = x3d.TouchSensor()
TouchSensor964.DEF = "Walk_Touch"
TouchSensor964.description = "click for behavior"

Transform963.children.append(TouchSensor964)
Shape965 = x3d.Shape()
Shape965.DEF = "WALK_Shape"
IndexedFaceSet966 = x3d.IndexedFaceSet()
IndexedFaceSet966.coordIndex = [0,2,1,-1,3,2,0,-1,12,3,0,-1,4,3,12,-1,11,4,12,-1,5,4,11,-1,10,5,11,-1,6,5,10,-1,9,6,10,-1,7,6,9,-1,8,7,9,-1,15,14,13,-1,16,15,13,-1,19,18,17,-1,20,19,17,-1,27,20,17,-1,28,27,17,-1,26,20,27,-1,23,20,26,-1,21,20,23,-1,25,23,26,-1,22,21,23,-1,24,23,25,-1,29,30,31,-1,29,31,32,-1,33,34,35,-1,33,35,29,-1,29,35,36,-1,29,36,30,-1,30,36,37,-1,37,36,38,-1,37,38,39,-1,37,39,40,-1,37,40,41,-1,41,40,42,-1,41,42,41,-1,41,42,43,-1,41,43,44,-1,44,43,45,-1,44,45,46,-1,47,46,45,-1,47,32,31,-1,47,31,46,-1,38,36,48,-1,38,48,49,-1,49,48,50,-1,49,50,51,-1,51,50,52,-1,51,52,53,-1,51,53,54,-1,54,53,55,-1,54,55,56,-1,54,56,57,-1]
Coordinate967 = x3d.Coordinate()

IndexedFaceSet966.coord = Coordinate967

Shape965.geometry = IndexedFaceSet966
Appearance968 = x3d.Appearance()
Material969 = x3d.Material()
Material969.USE = "text_color"

Appearance968.material = Material969

Shape965.appearance = Appearance968

Transform963.children.append(Shape965)
Transform970 = x3d.Transform()
Transform970.scale = [81.3,81.3,81.31]
Transform970.translation = [-0.0414,1.941,4.015]
Shape971 = x3d.Shape()
Shape971.DEF = "Walk_Back"
IndexedFaceSet972 = x3d.IndexedFaceSet()
IndexedFaceSet972.coordIndex = [1,3,0,-1,3,1,2,-1]
Coordinate973 = x3d.Coordinate()

IndexedFaceSet972.coord = Coordinate973

Shape971.geometry = IndexedFaceSet972
Appearance974 = x3d.Appearance()
Material975 = x3d.Material()
Material975.USE = "Clear"

Appearance974.material = Material975

Shape971.appearance = Appearance974

Transform970.children.append(Shape971)

Transform963.children.append(Transform970)

Transform949.children.append(Transform963)
Transform976 = x3d.Transform()
Transform976.DEF = "Run_Text"
TouchSensor977 = x3d.TouchSensor()
TouchSensor977.DEF = "Run_Touch"
TouchSensor977.description = "click for behavior"

Transform976.children.append(TouchSensor977)
Shape978 = x3d.Shape()
Shape978.DEF = "Run"
IndexedFaceSet979 = x3d.IndexedFaceSet()
IndexedFaceSet979.coordIndex = [24,26,25,-1,53,39,54,-1,17,1,0,-1,17,0,16,-1,0,14,16,-1,0,15,14,-1,14,13,22,-1,14,22,16,-1,13,12,21,-1,13,21,22,-1,12,6,21,-1,12,11,7,-1,12,7,6,-1,11,8,7,-1,10,8,11,-1,10,9,8,-1,6,5,21,-1,5,4,20,-1,5,20,21,-1,4,3,19,-1,4,19,20,-1,3,2,18,-1,3,18,19,-1,18,2,1,-1,18,1,17,-1,55,32,31,-1,55,31,56,-1,57,33,30,-1,57,30,58,-1,59,29,60,-1,61,34,28,-1,61,28,62,-1,63,35,27,-1,63,27,64,-1,65,36,66,-1,67,38,68,-1,69,37,70,-1,71,23,72,-1,73,48,47,-1,73,47,74,-1,75,49,46,-1,75,46,76,-1,77,45,78,-1,79,50,44,-1,79,44,80,-1,81,51,43,-1,81,43,82,-1,83,41,84,-1,85,40,86,-1,87,52,88,-1,89,42,90,-1]
Coordinate980 = x3d.Coordinate()

IndexedFaceSet979.coord = Coordinate980

Shape978.geometry = IndexedFaceSet979
Appearance981 = x3d.Appearance()
Material982 = x3d.Material()
Material982.USE = "text_color"

Appearance981.material = Material982

Shape978.appearance = Appearance981

Transform976.children.append(Shape978)
Transform983 = x3d.Transform()
Transform983.scale = [82.47,82.47,82.48]
Transform983.translation = [-0.01579,1.968,4.074]
Shape984 = x3d.Shape()
Shape984.DEF = "Run_Back"
IndexedFaceSet985 = x3d.IndexedFaceSet()
IndexedFaceSet985.coordIndex = [0,2,3,-1,2,0,1,-1]
Coordinate986 = x3d.Coordinate()

IndexedFaceSet985.coord = Coordinate986

Shape984.geometry = IndexedFaceSet985
Appearance987 = x3d.Appearance()
Material988 = x3d.Material()
Material988.USE = "Clear"

Appearance987.material = Material988

Shape984.appearance = Appearance987

Transform983.children.append(Shape984)

Transform976.children.append(Transform983)

Transform949.children.append(Transform976)
Transform989 = x3d.Transform()
Transform989.DEF = "Jump_Text"
TouchSensor990 = x3d.TouchSensor()
TouchSensor990.DEF = "Jump_Touch"
TouchSensor990.description = "click for behavior"

Transform989.children.append(TouchSensor990)
Shape991 = x3d.Shape()
Shape991.DEF = "Jump"
IndexedFaceSet992 = x3d.IndexedFaceSet()
IndexedFaceSet992.coordIndex = [1,0,14,-1,1,14,2,-1,16,15,18,-1,16,18,17,-1,64,65,66,-1,67,68,69,-1,67,69,70,-1,71,72,73,-1,71,73,74,-1,75,76,77,-1,78,79,80,-1,78,80,81,-1,82,83,84,-1,82,84,85,-1,86,87,88,-1,89,90,91,-1,92,93,94,-1,95,96,97,-1,98,7,6,-1,98,6,99,-1,100,8,5,-1,100,5,101,-1,102,9,4,-1,102,4,103,-1,104,10,105,-1,106,11,3,-1,106,3,107,-1,108,12,109,-1,110,13,111,-1,112,27,26,-1,112,26,113,-1,114,28,25,-1,114,25,115,-1,116,24,117,-1,118,29,23,-1,118,23,119,-1,120,30,22,-1,120,22,121,-1,122,31,123,-1,124,34,33,-1,124,33,125,-1,126,35,32,-1,126,32,127,-1,128,21,129,-1,130,36,20,-1,130,20,131,-1,132,37,19,-1,132,19,133,-1,134,38,135,-1,136,40,137,-1,138,39,139,-1,53,58,59,-1,53,59,54,-1,53,52,58,-1,52,51,57,-1,52,57,58,-1,51,50,56,-1,51,56,57,-1,50,49,56,-1,49,48,63,-1,49,63,56,-1,48,47,63,-1,63,47,46,-1,63,46,62,-1,62,46,45,-1,62,45,44,-1,62,44,61,-1,61,44,60,-1,54,59,60,-1,44,43,42,-1,60,44,42,-1,41,55,54,-1,41,54,60,-1,41,60,42,-1]
Coordinate993 = x3d.Coordinate()

IndexedFaceSet992.coord = Coordinate993

Shape991.geometry = IndexedFaceSet992
Appearance994 = x3d.Appearance()
Material995 = x3d.Material()
Material995.USE = "text_color"

Appearance994.material = Material995

Shape991.appearance = Appearance994

Transform989.children.append(Shape991)
Transform996 = x3d.Transform()
Transform996.scale = [83.79,83.79,83.79]
Transform996.translation = [-0.008979,1.99,4.14]
Shape997 = x3d.Shape()
Shape997.DEF = "Jump_Back"
IndexedFaceSet998 = x3d.IndexedFaceSet()
IndexedFaceSet998.coordIndex = [0,2,3,-1,2,0,1,-1]
Coordinate999 = x3d.Coordinate()

IndexedFaceSet998.coord = Coordinate999

Shape997.geometry = IndexedFaceSet998
Appearance1000 = x3d.Appearance()
Material1001 = x3d.Material()
Material1001.USE = "Clear"

Appearance1000.material = Material1001

Shape997.appearance = Appearance1000

Transform996.children.append(Shape997)

Transform989.children.append(Transform996)

Transform949.children.append(Transform989)
Transform1002 = x3d.Transform()
Transform1002.DEF = "Kneel_Text"
Transform1002.translation = [1.3,-0.12,0]
TouchSensor1003 = x3d.TouchSensor()
TouchSensor1003.DEF = "Kneel_Touch"
TouchSensor1003.description = "click for behavior"

Transform1002.children.append(TouchSensor1003)
Shape1004 = x3d.Shape()
Shape1004.DEF = "Kneel"
Text1005 = x3d.Text()
Text1005.string = ["Kneel"]
FontStyle1006 = x3d.FontStyle()
FontStyle1006.family = ["SANS"]
FontStyle1006.size = 0.45
FontStyle1006.style = "BOLD"

Text1005.fontStyle = FontStyle1006

Shape1004.geometry = Text1005
Appearance1007 = x3d.Appearance()
Material1008 = x3d.Material()
Material1008.USE = "text_color"

Appearance1007.material = Material1008

Shape1004.appearance = Appearance1007

Transform1002.children.append(Shape1004)
Transform1009 = x3d.Transform()
Transform1009.translation = [0.5,0.15,-0.001]
Shape1010 = x3d.Shape()
Shape1010.DEF = "Kneel_Back"
Appearance1011 = x3d.Appearance()
Material1012 = x3d.Material()
Material1012.diffuseColor = [0,1,0]
Material1012.transparency = 1

Appearance1011.material = Material1012

Shape1010.appearance = Appearance1011
Box1013 = x3d.Box()
Box1013.size = [1,0.36,0.001]

Shape1010.geometry = Box1013

Transform1009.children.append(Shape1010)

Transform1002.children.append(Transform1009)

Transform949.children.append(Transform1002)
Group1014 = x3d.Group()
Transform1015 = x3d.Transform()
Transform1015.DEF = "Allen_Text"
Transform1015.translation = [2,4,0]
TouchSensor1016 = x3d.TouchSensor()
TouchSensor1016.DEF = "Allen_Touch"
TouchSensor1016.description = "click for Allen body"

Transform1015.children.append(TouchSensor1016)
Shape1017 = x3d.Shape()
Text1018 = x3d.Text()
Text1018.string = ["ALLEN"]
FontStyle1019 = x3d.FontStyle()
FontStyle1019.size = 0.25
FontStyle1019.spacing = 0.1
FontStyle1019.style = "BOLD"

Text1018.fontStyle = FontStyle1019

Shape1017.geometry = Text1018
Appearance1020 = x3d.Appearance()
Material1021 = x3d.Material()
Material1021.diffuseColor = [0.6,0.6,0.6]

Appearance1020.material = Material1021

Shape1017.appearance = Appearance1020

Transform1015.children.append(Shape1017)
Transform1022 = x3d.Transform()
Transform1022.translation = [0.38,0.075,-0.001]
Shape1023 = x3d.Shape()
Shape1023.DEF = "MenuB"
Appearance1024 = x3d.Appearance()
Material1025 = x3d.Material()
Material1025.diffuseColor = [0,1,0]
Material1025.transparency = 1

Appearance1024.material = Material1025

Shape1023.appearance = Appearance1024
Box1026 = x3d.Box()
Box1026.size = [0.78,0.18,0.001]

Shape1023.geometry = Box1026

Transform1022.children.append(Shape1023)

Transform1015.children.append(Transform1022)

Group1014.children.append(Transform1015)
Transform1027 = x3d.Transform()
Transform1027.DEF = "Nancy_Text"
Transform1027.translation = [2,3.5,0]
TouchSensor1028 = x3d.TouchSensor()
TouchSensor1028.DEF = "Nancy_Touch"
TouchSensor1028.description = "click for Nancy body"

Transform1027.children.append(TouchSensor1028)
Shape1029 = x3d.Shape()
Text1030 = x3d.Text()
Text1030.string = ["NANCY"]
FontStyle1031 = x3d.FontStyle()
FontStyle1031.size = 0.25
FontStyle1031.spacing = 0.1
FontStyle1031.style = "BOLD"

Text1030.fontStyle = FontStyle1031

Shape1029.geometry = Text1030
Appearance1032 = x3d.Appearance()
Material1033 = x3d.Material()
Material1033.diffuseColor = [0.6,0.6,0.6]

Appearance1032.material = Material1033

Shape1029.appearance = Appearance1032

Transform1027.children.append(Shape1029)
Transform1034 = x3d.Transform()
Transform1034.translation = [0.38,0.075,-0.001]
Shape1035 = x3d.Shape()
Shape1035.USE = "MenuB"

Transform1034.children.append(Shape1035)

Transform1027.children.append(Transform1034)

Group1014.children.append(Transform1027)
Transform1036 = x3d.Transform()
Transform1036.DEF = "Boxman_Text"
Transform1036.translation = [2,3,0]
TouchSensor1037 = x3d.TouchSensor()
TouchSensor1037.DEF = "Boxman_Touch"
TouchSensor1037.description = "click for BoxMan body"

Transform1036.children.append(TouchSensor1037)
Shape1038 = x3d.Shape()
Text1039 = x3d.Text()
Text1039.string = ["BOXMAN"]
FontStyle1040 = x3d.FontStyle()
FontStyle1040.size = 0.25
FontStyle1040.spacing = 0.1
FontStyle1040.style = "BOLD"

Text1039.fontStyle = FontStyle1040

Shape1038.geometry = Text1039
Appearance1041 = x3d.Appearance()
Material1042 = x3d.Material()
Material1042.diffuseColor = [0.6,0.6,0.6]

Appearance1041.material = Material1042

Shape1038.appearance = Appearance1041

Transform1036.children.append(Shape1038)
Transform1043 = x3d.Transform()
Transform1043.translation = [0.5,0.075,-0.001]
Shape1044 = x3d.Shape()
Appearance1045 = x3d.Appearance()
Material1046 = x3d.Material()
Material1046.diffuseColor = [0,1,0]
Material1046.transparency = 1

Appearance1045.material = Material1046

Shape1044.appearance = Appearance1045
Box1047 = x3d.Box()
Box1047.size = [1,0.18,0.001]

Shape1044.geometry = Box1047

Transform1043.children.append(Shape1044)

Transform1036.children.append(Transform1043)

Group1014.children.append(Transform1036)

Transform949.children.append(Group1014)

Transform948.children.append(Transform949)

Collision947.proxy = Transform948

Group944.children.append(Collision947)
Transform1048 = x3d.Transform()
Transform1048.DEF = "Floor"
Transform1048.scale = [1,0.0125,1]
Transform1048.translation = [0,-0.0125,0]
Shape1049 = x3d.Shape()
Box1050 = x3d.Box()

Shape1049.geometry = Box1050
Appearance1051 = x3d.Appearance()
Material1052 = x3d.Material()

Appearance1051.material = Material1052

Shape1049.appearance = Appearance1051

Transform1048.children.append(Shape1049)

Group944.children.append(Transform1048)

Scene24.children.append(Group944)
ROUTE1053 = x3d.ROUTE()
ROUTE1053.fromField = "position_changed"
ROUTE1053.fromNode = "HudProx"
ROUTE1053.toField = "set_translation"
ROUTE1053.toNode = "HudXform"

Scene24.children.append(ROUTE1053)
ROUTE1054 = x3d.ROUTE()
ROUTE1054.fromField = "orientation_changed"
ROUTE1054.fromNode = "HudProx"
ROUTE1054.toField = "set_rotation"
ROUTE1054.toNode = "HudXform"

Scene24.children.append(ROUTE1054)
Script1055 = x3d.Script()
Script1055.DEF = "ActorAnimator"
Script1055.directOutput = True
#***********Interfaces*****************
#Joint Nodes
#**************Avatar choice***************
#*************Behavior fields************
field1056 = x3d.field()
field1056.name = "changeBehaviorToWalk"
field1056.accessType = "inputOnly"
field1056.type = "SFBool"

Script1055.field.append(field1056)
field1057 = x3d.field()
field1057.name = "changeBehaviorToRun"
field1057.accessType = "inputOnly"
field1057.type = "SFBool"

Script1055.field.append(field1057)
field1058 = x3d.field()
field1058.name = "changeBehaviorToJump"
field1058.accessType = "inputOnly"
field1058.type = "SFBool"

Script1055.field.append(field1058)
field1059 = x3d.field()
field1059.name = "changeBehaviorToStand"
field1059.accessType = "inputOnly"
field1059.type = "SFBool"

Script1055.field.append(field1059)
field1060 = x3d.field()
field1060.name = "changeBehaviorToKneel"
field1060.accessType = "inputOnly"
field1060.type = "SFBool"

Script1055.field.append(field1060)
field1061 = x3d.field()
field1061.name = "switchAvatarToAllen"
field1061.accessType = "inputOnly"
field1061.type = "SFBool"

Script1055.field.append(field1061)
field1062 = x3d.field()
field1062.name = "switchAvatarToNancy"
field1062.accessType = "inputOnly"
field1062.type = "SFBool"

Script1055.field.append(field1062)
field1063 = x3d.field()
field1063.name = "switchAvatarToBoxman"
field1063.accessType = "inputOnly"
field1063.type = "SFBool"

Script1055.field.append(field1063)
field1064 = x3d.field()
field1064.name = "NancyJointNodes"
field1064.accessType = "initializeOnly"
field1064.type = "MFNode"
#TODO ensure name attribute not needed as part of USE node
ProtoInstance1065 = x3d.ProtoInstance()
ProtoInstance1065.USE = "Nancy_hanim_humanoid_root"

field1064.children.append(ProtoInstance1065)
ProtoInstance1066 = x3d.ProtoInstance()
ProtoInstance1066.USE = "Nancy_hanim_sacroiliac"

field1064.children.append(ProtoInstance1066)
ProtoInstance1067 = x3d.ProtoInstance()
ProtoInstance1067.USE = "Nancy_hanim_l_hip"

field1064.children.append(ProtoInstance1067)
ProtoInstance1068 = x3d.ProtoInstance()
ProtoInstance1068.USE = "Nancy_hanim_l_knee"

field1064.children.append(ProtoInstance1068)
ProtoInstance1069 = x3d.ProtoInstance()
ProtoInstance1069.USE = "Nancy_hanim_l_ankle"

field1064.children.append(ProtoInstance1069)
ProtoInstance1070 = x3d.ProtoInstance()
ProtoInstance1070.USE = "Nancy_hanim_r_hip"

field1064.children.append(ProtoInstance1070)
ProtoInstance1071 = x3d.ProtoInstance()
ProtoInstance1071.USE = "Nancy_hanim_r_knee"

field1064.children.append(ProtoInstance1071)
ProtoInstance1072 = x3d.ProtoInstance()
ProtoInstance1072.USE = "Nancy_hanim_r_ankle"

field1064.children.append(ProtoInstance1072)
ProtoInstance1073 = x3d.ProtoInstance()
ProtoInstance1073.USE = "Nancy_hanim_skullbase"

field1064.children.append(ProtoInstance1073)
ProtoInstance1074 = x3d.ProtoInstance()
ProtoInstance1074.USE = "Nancy_hanim_l_shoulder"

field1064.children.append(ProtoInstance1074)
ProtoInstance1075 = x3d.ProtoInstance()
ProtoInstance1075.USE = "Nancy_hanim_l_elbow"

field1064.children.append(ProtoInstance1075)
ProtoInstance1076 = x3d.ProtoInstance()
ProtoInstance1076.USE = "Nancy_hanim_l_wrist"

field1064.children.append(ProtoInstance1076)
ProtoInstance1077 = x3d.ProtoInstance()
ProtoInstance1077.USE = "Nancy_hanim_r_shoulder"

field1064.children.append(ProtoInstance1077)
ProtoInstance1078 = x3d.ProtoInstance()
ProtoInstance1078.USE = "Nancy_hanim_r_elbow"

field1064.children.append(ProtoInstance1078)
ProtoInstance1079 = x3d.ProtoInstance()
ProtoInstance1079.USE = "Nancy_hanim_r_wrist"

field1064.children.append(ProtoInstance1079)

Script1055.field.append(field1064)
field1080 = x3d.field()
field1080.name = "AllenJointNodes"
field1080.accessType = "initializeOnly"
field1080.type = "MFNode"
ProtoInstance1081 = x3d.ProtoInstance()
ProtoInstance1081.USE = "Allen_hanim_humanoid_root"

field1080.children.append(ProtoInstance1081)
ProtoInstance1082 = x3d.ProtoInstance()
ProtoInstance1082.USE = "Allen_hanim_sacroiliac"

field1080.children.append(ProtoInstance1082)
ProtoInstance1083 = x3d.ProtoInstance()
ProtoInstance1083.USE = "Allen_hanim_skullbase"

field1080.children.append(ProtoInstance1083)
ProtoInstance1084 = x3d.ProtoInstance()
ProtoInstance1084.USE = "Allen_hanim_l_hip"

field1080.children.append(ProtoInstance1084)
ProtoInstance1085 = x3d.ProtoInstance()
ProtoInstance1085.USE = "Allen_hanim_r_hip"

field1080.children.append(ProtoInstance1085)
ProtoInstance1086 = x3d.ProtoInstance()
ProtoInstance1086.USE = "Allen_hanim_l_knee"

field1080.children.append(ProtoInstance1086)
ProtoInstance1087 = x3d.ProtoInstance()
ProtoInstance1087.USE = "Allen_hanim_r_knee"

field1080.children.append(ProtoInstance1087)
ProtoInstance1088 = x3d.ProtoInstance()
ProtoInstance1088.USE = "Allen_hanim_l_ankle"

field1080.children.append(ProtoInstance1088)
ProtoInstance1089 = x3d.ProtoInstance()
ProtoInstance1089.USE = "Allen_hanim_r_ankle"

field1080.children.append(ProtoInstance1089)
ProtoInstance1090 = x3d.ProtoInstance()
ProtoInstance1090.USE = "Allen_hanim_l_shoulder"

field1080.children.append(ProtoInstance1090)
ProtoInstance1091 = x3d.ProtoInstance()
ProtoInstance1091.USE = "Allen_hanim_r_shoulder"

field1080.children.append(ProtoInstance1091)
ProtoInstance1092 = x3d.ProtoInstance()
ProtoInstance1092.USE = "Allen_hanim_l_elbow"

field1080.children.append(ProtoInstance1092)
ProtoInstance1093 = x3d.ProtoInstance()
ProtoInstance1093.USE = "Allen_hanim_r_elbow"

field1080.children.append(ProtoInstance1093)
ProtoInstance1094 = x3d.ProtoInstance()
ProtoInstance1094.USE = "Allen_hanim_l_wrist"

field1080.children.append(ProtoInstance1094)
ProtoInstance1095 = x3d.ProtoInstance()
ProtoInstance1095.USE = "Allen_hanim_r_wrist"

field1080.children.append(ProtoInstance1095)

Script1055.field.append(field1080)
field1096 = x3d.field()
field1096.name = "BoxmanJointNodes"
field1096.accessType = "initializeOnly"
field1096.type = "MFNode"
HAnimJoint1097 = x3d.HAnimJoint()
HAnimJoint1097.USE = "Boxman_humanoid_root"

field1096.joints.append(HAnimJoint1097)
HAnimJoint1098 = x3d.HAnimJoint()
HAnimJoint1098.USE = "Boxman_skullbase"

field1096.joints.append(HAnimJoint1098)
HAnimJoint1099 = x3d.HAnimJoint()
HAnimJoint1099.USE = "Boxman_vl5"

field1096.joints.append(HAnimJoint1099)
HAnimJoint1100 = x3d.HAnimJoint()
HAnimJoint1100.USE = "Boxman_l_hip"

field1096.joints.append(HAnimJoint1100)
HAnimJoint1101 = x3d.HAnimJoint()
HAnimJoint1101.USE = "Boxman_r_hip"

field1096.joints.append(HAnimJoint1101)
HAnimJoint1102 = x3d.HAnimJoint()
HAnimJoint1102.USE = "Boxman_l_knee"

field1096.joints.append(HAnimJoint1102)
HAnimJoint1103 = x3d.HAnimJoint()
HAnimJoint1103.USE = "Boxman_r_knee"

field1096.joints.append(HAnimJoint1103)
HAnimJoint1104 = x3d.HAnimJoint()
HAnimJoint1104.USE = "Boxman_l_ankle"

field1096.joints.append(HAnimJoint1104)
HAnimJoint1105 = x3d.HAnimJoint()
HAnimJoint1105.USE = "Boxman_r_ankle"

field1096.joints.append(HAnimJoint1105)
HAnimJoint1106 = x3d.HAnimJoint()
HAnimJoint1106.USE = "Boxman_l_shoulder"

field1096.joints.append(HAnimJoint1106)
HAnimJoint1107 = x3d.HAnimJoint()
HAnimJoint1107.USE = "Boxman_r_shoulder"

field1096.joints.append(HAnimJoint1107)
HAnimJoint1108 = x3d.HAnimJoint()
HAnimJoint1108.USE = "Boxman_l_elbow"

field1096.joints.append(HAnimJoint1108)
HAnimJoint1109 = x3d.HAnimJoint()
HAnimJoint1109.USE = "Boxman_r_elbow"

field1096.joints.append(HAnimJoint1109)
HAnimJoint1110 = x3d.HAnimJoint()
HAnimJoint1110.USE = "Boxman_l_wrist"

field1096.joints.append(HAnimJoint1110)
HAnimJoint1111 = x3d.HAnimJoint()
HAnimJoint1111.USE = "Boxman_r_wrist"

field1096.joints.append(HAnimJoint1111)
HAnimJoint1112 = x3d.HAnimJoint()
HAnimJoint1112.USE = "Boxman_l_midtarsal"

field1096.joints.append(HAnimJoint1112)
HAnimJoint1113 = x3d.HAnimJoint()
HAnimJoint1113.USE = "Boxman_r_midtarsal"

field1096.joints.append(HAnimJoint1113)

Script1055.field.append(field1096)
field1114 = x3d.field()
field1114.name = "AvatarChoice"
field1114.accessType = "outputOnly"
field1114.type = "SFInt32"

Script1055.field.append(field1114)
field1115 = x3d.field()
field1115.name = "Behaviors"
field1115.accessType = "initializeOnly"
field1115.type = "MFNode"
ProtoInstance1116 = x3d.ProtoInstance()
ProtoInstance1116.USE = "WALK"

field1115.children.append(ProtoInstance1116)
ProtoInstance1117 = x3d.ProtoInstance()
ProtoInstance1117.USE = "RUN"

field1115.children.append(ProtoInstance1117)
ProtoInstance1118 = x3d.ProtoInstance()
ProtoInstance1118.USE = "JUMP"

field1115.children.append(ProtoInstance1118)
ProtoInstance1119 = x3d.ProtoInstance()
ProtoInstance1119.USE = "STAND"

field1115.children.append(ProtoInstance1119)
ProtoInstance1120 = x3d.ProtoInstance()
ProtoInstance1120.USE = "KNEEL"

field1115.children.append(ProtoInstance1120)

Script1055.field.append(field1115)

Script1055.sourceCode = '''ecmascript:\n"+
"\n"+
"//Global Variables\n"+
"var currentAnimatorIndex;\n"+
"var avatarJoints;\n"+
"var animatorFields;\n"+
"\n"+
"function initialize() {\n"+
"\n"+
"   //Avatar Joint Names\n"+
"   avatarJoints = new Array();\n"+
"   avatarJoints[0] ='humanoid_root';\n"+
"   avatarJoints[1] ='sacroiliac';\n"+
"   avatarJoints[2] ='l_hip';\n"+
"   avatarJoints[3] ='l_knee';\n"+
"   avatarJoints[4] ='l_ankle';\n"+
"   avatarJoints[5] ='r_hip';\n"+
"   avatarJoints[6] ='r_knee';\n"+
"   avatarJoints[7] ='r_ankle';\n"+
"   avatarJoints[8] ='skullbase';\n"+
"   avatarJoints[9] ='l_shoulder';\n"+
"   avatarJoints[10] ='l_elbow';\n"+
"   avatarJoints[11] ='l_wrist';\n"+
"   avatarJoints[12] ='r_shoulder';\n"+
"   avatarJoints[13] ='r_elbow';\n"+
"   avatarJoints[14] ='r_wrist';\n"+
"   avatarJoints[15] ='l_midtarsal';\n"+
"   avatarJoints[16] ='r_midtarsal';\n"+
"   avatarJoints[17] ='vl_5';\n"+
"\n"+
"\n"+
"   //ANIMATOR field names will be used\n"+
"   //as fromField value of created ROUTES\n"+
"   animatorFields = new Array();\n"+
"   for(i = 0; i <= 17; i++) {\n"+
"\n"+
"      if(avatarJoints[i] =='sacroiliac') {\n"+
"         animatorFields[i] ='lower_body_rotation_changed';\n"+
"      }\n"+
"\n"+
"      else {\n"+
"	 animatorFields[i] = avatarJoints[i] + '_rotation_changed';\n"+
"      }\n"+
"   } //end for loop\n"+
"\n"+
"\n"+
"   // Current Avatar Choice\n"+
"   // 0 : Allen\n"+
"   // 1 : Nancy\n"+
"   // 2 : Boxman\n"+
"   AvatarChoice = 0;\n"+
"\n"+
"\n"+
"   // Current Animator Behavior Index\n"+
"   // 0 : WALK\n"+
"   // 1 : RUN\n"+
"   // 2 : JUMP\n"+
"   // 3 : STAND\n"+
"   // 4 : KNEEL\n"+
"   currentAnimatorIndex = 3; //Initial behavior: KNEEL\n"+
"\n"+
"   createRoutes();\n"+
"\n"+
"}\n"+
"\n"+
"\n"+
"function createRoutes() {\n"+
"   //Add Routes for Allen which is current avatar\n"+
"   if(AvatarChoice == 0) {\n"+
"\n"+
"      //Exception routing for humanoid_Root translation\n"+
"      Browser.addRoute(Behaviors[currentAnimatorIndex], avatarJoints[0] + '_translation_changed', AllenJointNodes[0],'set_translation');\n"+
"\n"+
"      for(i = 0; i < 15; i++) {\n"+
"\n"+
"         Browser.addRoute(Behaviors[currentAnimatorIndex], animatorFields[i],AllenJointNodes[i],'set_rotation');\n"+
"      }\n"+
"\n"+
"   }\n"+
"\n"+
"   //Add Routes for Nancy which is current avatar\n"+
"   if(AvatarChoice == 1) {\n"+
"\n"+
"      //Exception routing for humanoid_Root translation\n"+
"      Browser.addRoute(Behaviors[currentAnimatorIndex], avatarJoints[0] + '_translation_changed', NancyJointNodes[0],'set_translation');\n"+
"\n"+
"      for(i = 0; i < 15; i++) {\n"+
"\n"+
"         Browser.addRoute(Behaviors[currentAnimatorIndex], animatorFields[i],NancyJointNodes[i],'set_rotation');\n"+
"      }\n"+
"\n"+
"   }\n"+
"\n"+
"   //Add Routes for Boxman which is current avatar\n"+
"   if(AvatarChoice == 2) {\n"+
"\n"+
"      //Exception routing for humanoid_Root translation\n"+
"      Browser.addRoute(Behaviors[currentAnimatorIndex], avatarJoints[0] + '_translation_changed', BoxmanJointNodes[0],'set_translation');\n"+
"       for(i = 0; i <= 16; i++) {\n"+
"         if(i != 1) { //no sacroiliac in Boxman\n"+
"            Browser.addRoute(Behaviors[currentAnimatorIndex], animatorFields[i], BoxmanJointNodes[i],'set_rotation');\n"+
"         }\n"+
"      }\n"+
"    }\n"+
"}\n"+
"\n"+
"\n"+
"function removeRoutes() {\n"+
"   //Remove Routes for Allen which is current avatar\n"+
"   if(AvatarChoice == 0) {\n"+
"\n"+
"      //Exception routing for humanoid_Root translation\n"+
"      Browser.deleteRoute(Behaviors[currentAnimatorIndex], avatarJoints[0] + '_translation_changed', AllenJointNodes[0],'set_translation');\n"+
"\n"+
"      for(i = 0; i < 15; i++) {\n"+
"         Browser.deleteRoute(Behaviors[currentAnimatorIndex], animatorFields[i],AllenJointNodes[i],'set_rotation');\n"+
"      }\n"+
"\n"+
"   }\n"+
"\n"+
"   //Remove Routes for Nancy which is current avatar\n"+
"   if(AvatarChoice == 1) {\n"+
"\n"+
"      //Exception routing for humanoid_Root translation               \n"+
"      Browser.deleteRoute(Behaviors[currentAnimatorIndex], avatarJoints[0] + '_translation_changed', NancyJointNodes[0],'set_translation'); 	               \n"+
"\n"+
"      //Exception routing for humanoid_Root translation\n"+
"      Browser.deleteRoute(Behaviors[currentAnimatorIndex], avatarJoints[0] + '_translation_changed', NancyJointNodes[0],'set_translation');\n"+
"\n"+
"      for(i = 0; i < 15; i++) {\n"+
"\n"+
"         Browser.deleteRoute(Behaviors[currentAnimatorIndex], animatorFields[i],NancyJointNodes[i],'set_rotation');\n"+
"      }\n"+
"\n"+
"\n"+
"   }\n"+
"\n"+
"   //Remove Routes for Boxman which is current avatar\n"+
"   if(AvatarChoice == 2) {\n"+
"\n"+
"      //Exception routing for humanoid_Root translation\n"+
"      Browser.deleteRoute(Behaviors[currentAnimatorIndex], avatarJoints[0] + '_translation_changed', BoxmanJointNodes[0],'set_translation');\n"+
"\n"+
"      for(i = 0; i < 17; i++) {\n"+
"         if(i != 1) {\n"+
"            Browser.deleteRoute(Behaviors[currentAnimatorIndex], animatorFields[i],BoxmanJointNodes[i],'set_rotation');\n"+
"         }\n"+
"      }\n"+
"\n"+
"   }\n"+
"}\n"+
"\n"+
"\n"+
"\n"+
"function switchAvatarToAllen (bool, timeStamp) {//Invoked when Allen text is clicked.\n"+
"   //A control structure to avoid excessive work. If current avatar is Allen, don't do anything.\n"+
"   if(AvatarChoice != 0) {\n"+
"      removeRoutes();\n"+
"      AvatarChoice = 0;\n"+
"      createRoutes();\n"+
"\n"+
"   }\n"+
"}\n"+
"\n"+
"\n"+
"function switchAvatarToNancy (bool, timeStamp) {//Invoked when Nancy text is clicked.\n"+
"\n"+
"   //A control structure to avoid excessive work. If current avatar is Nancy, don't do anything.\n"+
"   if(AvatarChoice != 1) {\n"+
"      removeRoutes();\n"+
"      AvatarChoice = 1;\n"+
"      createRoutes();\n"+
"\n"+
"   }\n"+
"}\n"+
"\n"+
"\n"+
"function switchAvatarToBoxman (bool, timeStamp) {//Invoked when Boxman text is clicked.\n"+
"\n"+
"   //A control structure to avoid excessive work. If current avatar is Boxman, don't do anything.\n"+
"   if(AvatarChoice != 2) {\n"+
"      removeRoutes();\n"+
"      AvatarChoice = 2;\n"+
"      createRoutes();\n"+
"\n"+
"   }\n"+
"}\n"+
"\n"+
"\n"+
"function changeBehaviorToWalk(bool, timeStamp) {\n"+
"\n"+
"   if(currentAnimatorIndex != 0) {\n"+
"     removeRoutes();\n"+
"     currentAnimatorIndex = 0;\n"+
"     createRoutes();\n"+
"   }\n"+
"}\n"+
"\n"+
"function changeBehaviorToRun(bool, timeStamp) {\n"+
"\n"+
"   if(currentAnimatorIndex != 1) {\n"+
"      removeRoutes();\n"+
"      currentAnimatorIndex = 1;\n"+
"      createRoutes();\n"+
"   }\n"+
"}\n"+
"\n"+
"\n"+
"\n"+
"function changeBehaviorToJump(bool, timeStamp) {\n"+
"\n"+
"   if(currentAnimatorIndex != 2) {\n"+
"      removeRoutes();\n"+
"      currentAnimatorIndex = 2;\n"+
"      createRoutes();\n"+
"   }\n"+
"\n"+
"}\n"+
"\n"+
"\n"+
"function changeBehaviorToStand(bool, timeStamp) {\n"+
"\n"+
"   if(currentAnimatorIndex != 3) {\n"+
"      removeRoutes();\n"+
"      currentAnimatorIndex = 3;\n"+
"      createRoutes();\n"+
"   }\n"+
"\n"+
"}\n"+
"\n"+
"function changeBehaviorToKneel(bool, timeStamp) {\n"+
"\n"+
"   if(currentAnimatorIndex != 4) {\n"+
"      removeRoutes();\n"+
"      currentAnimatorIndex = 4;\n"+
"      createRoutes();\n"+
"   }\n"+
"\n"+
"}'''

Scene24.children.append(Script1055)
#***********Script routes*************
ROUTE1121 = x3d.ROUTE()
ROUTE1121.fromField = "AvatarChoice"
ROUTE1121.fromNode = "ActorAnimator"
ROUTE1121.toField = "whichChoice"
ROUTE1121.toNode = "AvatarSwitch"

Scene24.children.append(ROUTE1121)
#*************Behavior Touch Sensor Routes**************
ROUTE1122 = x3d.ROUTE()
ROUTE1122.fromField = "isActive"
ROUTE1122.fromNode = "Walk_Touch"
ROUTE1122.toField = "changeBehaviorToWalk"
ROUTE1122.toNode = "ActorAnimator"

Scene24.children.append(ROUTE1122)
ROUTE1123 = x3d.ROUTE()
ROUTE1123.fromField = "isActive"
ROUTE1123.fromNode = "Run_Touch"
ROUTE1123.toField = "changeBehaviorToRun"
ROUTE1123.toNode = "ActorAnimator"

Scene24.children.append(ROUTE1123)
ROUTE1124 = x3d.ROUTE()
ROUTE1124.fromField = "isActive"
ROUTE1124.fromNode = "Jump_Touch"
ROUTE1124.toField = "changeBehaviorToJump"
ROUTE1124.toNode = "ActorAnimator"

Scene24.children.append(ROUTE1124)
ROUTE1125 = x3d.ROUTE()
ROUTE1125.fromField = "isActive"
ROUTE1125.fromNode = "Stand_Touch"
ROUTE1125.toField = "changeBehaviorToStand"
ROUTE1125.toNode = "ActorAnimator"

Scene24.children.append(ROUTE1125)
ROUTE1126 = x3d.ROUTE()
ROUTE1126.fromField = "isActive"
ROUTE1126.fromNode = "Kneel_Touch"
ROUTE1126.toField = "changeBehaviorToKneel"
ROUTE1126.toNode = "ActorAnimator"

Scene24.children.append(ROUTE1126)
ROUTE1127 = x3d.ROUTE()
ROUTE1127.fromField = "touchTime"
ROUTE1127.fromNode = "Kneel_Touch"
ROUTE1127.toField = "set_startTime"
ROUTE1127.toNode = "KNEEL"

Scene24.children.append(ROUTE1127)
#*************Avatar Name Touch Sensor Routes**************
ROUTE1128 = x3d.ROUTE()
ROUTE1128.fromField = "isActive"
ROUTE1128.fromNode = "Allen_Touch"
ROUTE1128.toField = "switchAvatarToAllen"
ROUTE1128.toNode = "ActorAnimator"

Scene24.children.append(ROUTE1128)
ROUTE1129 = x3d.ROUTE()
ROUTE1129.fromField = "isActive"
ROUTE1129.fromNode = "Nancy_Touch"
ROUTE1129.toField = "switchAvatarToNancy"
ROUTE1129.toNode = "ActorAnimator"

Scene24.children.append(ROUTE1129)
ROUTE1130 = x3d.ROUTE()
ROUTE1130.fromField = "isActive"
ROUTE1130.fromNode = "Boxman_Touch"
ROUTE1130.toField = "switchAvatarToBoxman"
ROUTE1130.toNode = "ActorAnimator"

Scene24.children.append(ROUTE1130)
ROUTE1131 = x3d.ROUTE()
ROUTE1131.fromField = "rotation_changed"
ROUTE1131.fromNode = "Boxman_r_elbow"
ROUTE1131.toField = "update"
ROUTE1131.toNode = "ENGINE"

Scene24.children.append(ROUTE1131)

X3D0.Scene = Scene24
f = open("././InterchangableActorsViaDynamicRoutingPrototypes_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
