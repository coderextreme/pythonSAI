from x3dpsail import *
X3D0 = X3D()
X3D0.setProfile("Immersive")
X3D0.setVersion("3.3")
head1 = head()
component2 = component()
component2.setName("H-Anim")
component2.setLevel(1)

head1.addComponent(component2)
meta3 = meta()
meta3.setName("title")
meta3.setContent("InterchangableActorsViaDynamicRoutingPrototypes.x3d")

head1.addMeta(meta3)
meta4 = meta()
meta4.setName("description")
meta4.setContent("This example demonstrates interchangeability of avatars (Nancy, Allen, Boxman) and animation behaviors (Stand, Run, Jump, Walk) via dynamic routing.")

head1.addMeta(meta4)
meta5 = meta()
meta5.setName("warning")
meta5.setContent("this example needs to be converted from HAnim Prototypes to HAnim native tags.")

head1.addMeta(meta5)
meta6 = meta()
meta6.setName("creator")
meta6.setContent("Ozan APAYDIN")

head1.addMeta(meta6)
meta7 = meta()
meta7.setName("translator")
meta7.setContent("Ozan APAYDIN")

head1.addMeta(meta7)
meta8 = meta()
meta8.setName("created")
meta8.setContent("15 November 2001")

head1.addMeta(meta8)
meta9 = meta()
meta9.setName("modified")
meta9.setContent("9 July 2020")

head1.addMeta(meta9)
meta10 = meta()
meta10.setName("TODO")
meta10.setContent("replace usages of original Boxman .wrl fragments, fix numerous warnings")

head1.addMeta(meta10)
meta11 = meta()
meta11.setName("TODO")
meta11.setContent("Inconsistent validation problem with HAnimJoint, ProtoInstance USE nodes: required @name attribute must also be present")

head1.addMeta(meta11)
meta12 = meta()
meta12.setName("reference")
meta12.setContent("http://www.movesinstitute.org/Theses/ApaydinThesis.pdf")

head1.addMeta(meta12)
meta13 = meta()
meta13.setName("MovingImage")
meta13.setContent("VoiceActivated/ApaydinOzanThesisPresentation.ppt")

head1.addMeta(meta13)
meta14 = meta()
meta14.setName("MovingImage")
meta14.setContent("https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/VoiceActivated/ApaydinOzanThesisFinalVideo.mpg")

head1.addMeta(meta14)
meta15 = meta()
meta15.setName("MovingImage")
meta15.setContent("https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/VoiceActivated/NancyVUI.wmv")

head1.addMeta(meta15)
meta16 = meta()
meta16.setName("reference")
meta16.setContent("http://HAnim.org/Models/HAnim2001/boxman/boxman.wrl")

head1.addMeta(meta16)
meta17 = meta()
meta17.setName("reference")
meta17.setContent("http://HAnim.org/Specifications/HAnim2001")

head1.addMeta(meta17)
meta18 = meta()
meta18.setName("reference")
meta18.setContent("http://www.HAnim.org")

head1.addMeta(meta18)
meta19 = meta()
meta19.setName("reference")
meta19.setContent("http://HAnim.org/Models")

head1.addMeta(meta19)
meta20 = meta()
meta20.setName("reference")
meta20.setContent("http://HAnim.org/Specifications")

head1.addMeta(meta20)
meta21 = meta()
meta21.setName("identifier")
meta21.setContent("https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Prototypes/InterchangableActorsViaDynamicRoutingPrototypes.x3d")

head1.addMeta(meta21)
meta22 = meta()
meta22.setName("generator")
meta22.setContent("X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit")

head1.addMeta(meta22)
meta23 = meta()
meta23.setName("license")
meta23.setContent("../license.html")

head1.addMeta(meta23)

X3D0.setHead(head1)
Scene24 = Scene()
#************Behavior Prototypes***************
ExternProtoDeclare25 = ExternProtoDeclare()
ExternProtoDeclare25.setName("LOA1_StandAnimation")
ExternProtoDeclare25.setUrl(["LOA1_StandAnimation.x3d#LOA1_StandAnimation","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/LOA1_StandAnimation.x3d#LOA1_StandAnimation","LOA1_StandAnimation.wrl#LOA1_StandAnimation","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/LOA1_StandAnimation.wrl#LOA1_StandAnimation"])
field26 = field()
field26.setName("cycleInterval")
field26.setAccessType("inputOutput")
field26.setType("SFTime")

ExternProtoDeclare25.addField(field26)
field27 = field()
field27.setName("enabled")
field27.setAccessType("inputOutput")
field27.setType("SFBool")

ExternProtoDeclare25.addField(field27)
field28 = field()
field28.setName("loop")
field28.setAccessType("inputOutput")
field28.setType("SFBool")

ExternProtoDeclare25.addField(field28)
field29 = field()
field29.setName("startTime")
field29.setAccessType("inputOutput")
field29.setType("SFTime")

ExternProtoDeclare25.addField(field29)
field30 = field()
field30.setName("stopTime")
field30.setAccessType("inputOutput")
field30.setType("SFTime")

ExternProtoDeclare25.addField(field30)
field31 = field()
field31.setName("fraction_changed")
field31.setAccessType("outputOnly")
field31.setType("SFFloat")

ExternProtoDeclare25.addField(field31)
field32 = field()
field32.setName("humanoid_root_translation_changed")
field32.setAccessType("outputOnly")
field32.setType("SFVec3f")

ExternProtoDeclare25.addField(field32)
field33 = field()
field33.setName("humanoid_root_rotation_changed")
field33.setAccessType("outputOnly")
field33.setType("SFRotation")

ExternProtoDeclare25.addField(field33)
field34 = field()
field34.setName("lower_body_rotation_changed")
field34.setAccessType("outputOnly")
field34.setType("SFRotation")

ExternProtoDeclare25.addField(field34)
field35 = field()
field35.setName("l_hip_rotation_changed")
field35.setAccessType("outputOnly")
field35.setType("SFRotation")

ExternProtoDeclare25.addField(field35)
field36 = field()
field36.setName("l_knee_rotation_changed")
field36.setAccessType("outputOnly")
field36.setType("SFRotation")

ExternProtoDeclare25.addField(field36)
field37 = field()
field37.setName("l_ankle_rotation_changed")
field37.setAccessType("outputOnly")
field37.setType("SFRotation")

ExternProtoDeclare25.addField(field37)
field38 = field()
field38.setName("l_midtarsal_rotation_changed")
field38.setAccessType("outputOnly")
field38.setType("SFRotation")

ExternProtoDeclare25.addField(field38)
field39 = field()
field39.setName("r_hip_rotation_changed")
field39.setAccessType("outputOnly")
field39.setType("SFRotation")

ExternProtoDeclare25.addField(field39)
field40 = field()
field40.setName("r_knee_rotation_changed")
field40.setAccessType("outputOnly")
field40.setType("SFRotation")

ExternProtoDeclare25.addField(field40)
field41 = field()
field41.setName("r_ankle_rotation_changed")
field41.setAccessType("outputOnly")
field41.setType("SFRotation")

ExternProtoDeclare25.addField(field41)
field42 = field()
field42.setName("r_midtarsal_rotation_changed")
field42.setAccessType("outputOnly")
field42.setType("SFRotation")

ExternProtoDeclare25.addField(field42)
field43 = field()
field43.setName("vl5_rotation_changed")
field43.setAccessType("outputOnly")
field43.setType("SFRotation")

ExternProtoDeclare25.addField(field43)
field44 = field()
field44.setName("skullbase_rotation_changed")
field44.setAccessType("outputOnly")
field44.setType("SFRotation")

ExternProtoDeclare25.addField(field44)
field45 = field()
field45.setName("l_shoulder_rotation_changed")
field45.setAccessType("outputOnly")
field45.setType("SFRotation")

ExternProtoDeclare25.addField(field45)
field46 = field()
field46.setName("l_elbow_rotation_changed")
field46.setAccessType("outputOnly")
field46.setType("SFRotation")

ExternProtoDeclare25.addField(field46)
field47 = field()
field47.setName("l_wrist_rotation_changed")
field47.setAccessType("outputOnly")
field47.setType("SFRotation")

ExternProtoDeclare25.addField(field47)
field48 = field()
field48.setName("r_shoulder_rotation_changed")
field48.setAccessType("outputOnly")
field48.setType("SFRotation")

ExternProtoDeclare25.addField(field48)
field49 = field()
field49.setName("r_elbow_rotation_changed")
field49.setAccessType("outputOnly")
field49.setType("SFRotation")

ExternProtoDeclare25.addField(field49)
field50 = field()
field50.setName("r_wrist_rotation_changed")
field50.setAccessType("outputOnly")
field50.setType("SFRotation")

ExternProtoDeclare25.addField(field50)
field51 = field()
field51.setName("isActive")
field51.setAccessType("outputOnly")
field51.setType("SFBool")

ExternProtoDeclare25.addField(field51)

Scene24.addChildren(ExternProtoDeclare25)
ExternProtoDeclare52 = ExternProtoDeclare()
ExternProtoDeclare52.setName("LOA1_WalkAnimation")
ExternProtoDeclare52.setUrl(["LOA1_WalkAnimation.x3d#LOA1_WalkAnimation","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/LOA1_WalkAnimation.x3d#LOA1_WalkAnimation","LOA1_WalkAnimation.wrl#LOA1_WalkAnimation","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/LOA1_WalkAnimation.wrl#LOA1_WalkAnimation"])
field53 = field()
field53.setName("cycleInterval")
field53.setAccessType("inputOutput")
field53.setType("SFTime")

ExternProtoDeclare52.addField(field53)
field54 = field()
field54.setName("enabled")
field54.setAccessType("inputOutput")
field54.setType("SFBool")

ExternProtoDeclare52.addField(field54)
field55 = field()
field55.setName("loop")
field55.setAccessType("inputOutput")
field55.setType("SFBool")

ExternProtoDeclare52.addField(field55)
field56 = field()
field56.setName("startTime")
field56.setAccessType("inputOutput")
field56.setType("SFTime")

ExternProtoDeclare52.addField(field56)
field57 = field()
field57.setName("stopTime")
field57.setAccessType("inputOutput")
field57.setType("SFTime")

ExternProtoDeclare52.addField(field57)
field58 = field()
field58.setName("fraction_changed")
field58.setAccessType("outputOnly")
field58.setType("SFFloat")

ExternProtoDeclare52.addField(field58)
field59 = field()
field59.setName("humanoid_root_translation_changed")
field59.setAccessType("outputOnly")
field59.setType("SFVec3f")

ExternProtoDeclare52.addField(field59)
field60 = field()
field60.setName("humanoid_root_rotation_changed")
field60.setAccessType("outputOnly")
field60.setType("SFRotation")

ExternProtoDeclare52.addField(field60)
field61 = field()
field61.setName("lower_body_rotation_changed")
field61.setAccessType("outputOnly")
field61.setType("SFRotation")

ExternProtoDeclare52.addField(field61)
field62 = field()
field62.setName("l_hip_rotation_changed")
field62.setAccessType("outputOnly")
field62.setType("SFRotation")

ExternProtoDeclare52.addField(field62)
field63 = field()
field63.setName("l_knee_rotation_changed")
field63.setAccessType("outputOnly")
field63.setType("SFRotation")

ExternProtoDeclare52.addField(field63)
field64 = field()
field64.setName("l_ankle_rotation_changed")
field64.setAccessType("outputOnly")
field64.setType("SFRotation")

ExternProtoDeclare52.addField(field64)
field65 = field()
field65.setName("l_midtarsal_rotation_changed")
field65.setAccessType("outputOnly")
field65.setType("SFRotation")

ExternProtoDeclare52.addField(field65)
field66 = field()
field66.setName("r_hip_rotation_changed")
field66.setAccessType("outputOnly")
field66.setType("SFRotation")

ExternProtoDeclare52.addField(field66)
field67 = field()
field67.setName("r_knee_rotation_changed")
field67.setAccessType("outputOnly")
field67.setType("SFRotation")

ExternProtoDeclare52.addField(field67)
field68 = field()
field68.setName("r_ankle_rotation_changed")
field68.setAccessType("outputOnly")
field68.setType("SFRotation")

ExternProtoDeclare52.addField(field68)
field69 = field()
field69.setName("r_midtarsal_rotation_changed")
field69.setAccessType("outputOnly")
field69.setType("SFRotation")

ExternProtoDeclare52.addField(field69)
field70 = field()
field70.setName("vl5_rotation_changed")
field70.setAccessType("outputOnly")
field70.setType("SFRotation")

ExternProtoDeclare52.addField(field70)
field71 = field()
field71.setName("skullbase_rotation_changed")
field71.setAccessType("outputOnly")
field71.setType("SFRotation")

ExternProtoDeclare52.addField(field71)
field72 = field()
field72.setName("l_shoulder_rotation_changed")
field72.setAccessType("outputOnly")
field72.setType("SFRotation")

ExternProtoDeclare52.addField(field72)
field73 = field()
field73.setName("l_elbow_rotation_changed")
field73.setAccessType("outputOnly")
field73.setType("SFRotation")

ExternProtoDeclare52.addField(field73)
field74 = field()
field74.setName("l_wrist_rotation_changed")
field74.setAccessType("outputOnly")
field74.setType("SFRotation")

ExternProtoDeclare52.addField(field74)
field75 = field()
field75.setName("r_shoulder_rotation_changed")
field75.setAccessType("outputOnly")
field75.setType("SFRotation")

ExternProtoDeclare52.addField(field75)
field76 = field()
field76.setName("r_elbow_rotation_changed")
field76.setAccessType("outputOnly")
field76.setType("SFRotation")

ExternProtoDeclare52.addField(field76)
field77 = field()
field77.setName("r_wrist_rotation_changed")
field77.setAccessType("outputOnly")
field77.setType("SFRotation")

ExternProtoDeclare52.addField(field77)
field78 = field()
field78.setName("isActive")
field78.setAccessType("outputOnly")
field78.setType("SFBool")

ExternProtoDeclare52.addField(field78)

Scene24.addChildren(ExternProtoDeclare52)
ExternProtoDeclare79 = ExternProtoDeclare()
ExternProtoDeclare79.setName("LOA1_RunAnimation")
ExternProtoDeclare79.setUrl(["LOA1_RunAnimation.x3d#LOA1_RunAnimation","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/LOA1_RunAnimation.x3d#LOA1_RunAnimation","LOA1_RunAnimation.wrl#LOA1_RunAnimation","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/LOA1_RunAnimation.wrl#LOA1_RunAnimation"])
field80 = field()
field80.setName("cycleInterval")
field80.setAccessType("inputOutput")
field80.setType("SFTime")

ExternProtoDeclare79.addField(field80)
field81 = field()
field81.setName("enabled")
field81.setAccessType("inputOutput")
field81.setType("SFBool")

ExternProtoDeclare79.addField(field81)
field82 = field()
field82.setName("loop")
field82.setAccessType("inputOutput")
field82.setType("SFBool")

ExternProtoDeclare79.addField(field82)
field83 = field()
field83.setName("startTime")
field83.setAccessType("inputOutput")
field83.setType("SFTime")

ExternProtoDeclare79.addField(field83)
field84 = field()
field84.setName("stopTime")
field84.setAccessType("inputOutput")
field84.setType("SFTime")

ExternProtoDeclare79.addField(field84)
field85 = field()
field85.setName("fraction_changed")
field85.setAccessType("outputOnly")
field85.setType("SFFloat")

ExternProtoDeclare79.addField(field85)
field86 = field()
field86.setName("humanoid_root_translation_changed")
field86.setAccessType("outputOnly")
field86.setType("SFVec3f")

ExternProtoDeclare79.addField(field86)
field87 = field()
field87.setName("humanoid_root_rotation_changed")
field87.setAccessType("outputOnly")
field87.setType("SFRotation")

ExternProtoDeclare79.addField(field87)
field88 = field()
field88.setName("lower_body_rotation_changed")
field88.setAccessType("outputOnly")
field88.setType("SFRotation")

ExternProtoDeclare79.addField(field88)
field89 = field()
field89.setName("l_hip_rotation_changed")
field89.setAccessType("outputOnly")
field89.setType("SFRotation")

ExternProtoDeclare79.addField(field89)
field90 = field()
field90.setName("l_knee_rotation_changed")
field90.setAccessType("outputOnly")
field90.setType("SFRotation")

ExternProtoDeclare79.addField(field90)
field91 = field()
field91.setName("l_ankle_rotation_changed")
field91.setAccessType("outputOnly")
field91.setType("SFRotation")

ExternProtoDeclare79.addField(field91)
field92 = field()
field92.setName("l_midtarsal_rotation_changed")
field92.setAccessType("outputOnly")
field92.setType("SFRotation")

ExternProtoDeclare79.addField(field92)
field93 = field()
field93.setName("r_hip_rotation_changed")
field93.setAccessType("outputOnly")
field93.setType("SFRotation")

ExternProtoDeclare79.addField(field93)
field94 = field()
field94.setName("r_knee_rotation_changed")
field94.setAccessType("outputOnly")
field94.setType("SFRotation")

ExternProtoDeclare79.addField(field94)
field95 = field()
field95.setName("r_ankle_rotation_changed")
field95.setAccessType("outputOnly")
field95.setType("SFRotation")

ExternProtoDeclare79.addField(field95)
field96 = field()
field96.setName("r_midtarsal_rotation_changed")
field96.setAccessType("outputOnly")
field96.setType("SFRotation")

ExternProtoDeclare79.addField(field96)
field97 = field()
field97.setName("vl5_rotation_changed")
field97.setAccessType("outputOnly")
field97.setType("SFRotation")

ExternProtoDeclare79.addField(field97)
field98 = field()
field98.setName("skullbase_rotation_changed")
field98.setAccessType("outputOnly")
field98.setType("SFRotation")

ExternProtoDeclare79.addField(field98)
field99 = field()
field99.setName("l_shoulder_rotation_changed")
field99.setAccessType("outputOnly")
field99.setType("SFRotation")

ExternProtoDeclare79.addField(field99)
field100 = field()
field100.setName("l_elbow_rotation_changed")
field100.setAccessType("outputOnly")
field100.setType("SFRotation")

ExternProtoDeclare79.addField(field100)
field101 = field()
field101.setName("l_wrist_rotation_changed")
field101.setAccessType("outputOnly")
field101.setType("SFRotation")

ExternProtoDeclare79.addField(field101)
field102 = field()
field102.setName("r_shoulder_rotation_changed")
field102.setAccessType("outputOnly")
field102.setType("SFRotation")

ExternProtoDeclare79.addField(field102)
field103 = field()
field103.setName("r_elbow_rotation_changed")
field103.setAccessType("outputOnly")
field103.setType("SFRotation")

ExternProtoDeclare79.addField(field103)
field104 = field()
field104.setName("r_wrist_rotation_changed")
field104.setAccessType("outputOnly")
field104.setType("SFRotation")

ExternProtoDeclare79.addField(field104)
field105 = field()
field105.setName("isActive")
field105.setAccessType("outputOnly")
field105.setType("SFBool")

ExternProtoDeclare79.addField(field105)

Scene24.addChildren(ExternProtoDeclare79)
ExternProtoDeclare106 = ExternProtoDeclare()
ExternProtoDeclare106.setName("LOA1_JumpAnimation")
ExternProtoDeclare106.setUrl(["LOA1_JumpAnimation.x3d#LOA1_JumpAnimation","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/LOA1_JumpAnimation.x3d#LOA1_JumpAnimation","LOA1_JumpAnimation.wrl#LOA1_JumpAnimation","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/LOA1_JumpAnimation.wrl#LOA1_JumpAnimation"])
field107 = field()
field107.setName("cycleInterval")
field107.setAccessType("inputOutput")
field107.setType("SFTime")

ExternProtoDeclare106.addField(field107)
field108 = field()
field108.setName("enabled")
field108.setAccessType("inputOutput")
field108.setType("SFBool")

ExternProtoDeclare106.addField(field108)
field109 = field()
field109.setName("loop")
field109.setAccessType("inputOutput")
field109.setType("SFBool")

ExternProtoDeclare106.addField(field109)
field110 = field()
field110.setName("startTime")
field110.setAccessType("inputOutput")
field110.setType("SFTime")

ExternProtoDeclare106.addField(field110)
field111 = field()
field111.setName("stopTime")
field111.setAccessType("inputOutput")
field111.setType("SFTime")

ExternProtoDeclare106.addField(field111)
field112 = field()
field112.setName("fraction_changed")
field112.setAccessType("outputOnly")
field112.setType("SFFloat")

ExternProtoDeclare106.addField(field112)
field113 = field()
field113.setName("humanoid_root_translation_changed")
field113.setAccessType("outputOnly")
field113.setType("SFVec3f")

ExternProtoDeclare106.addField(field113)
field114 = field()
field114.setName("humanoid_root_rotation_changed")
field114.setAccessType("outputOnly")
field114.setType("SFRotation")

ExternProtoDeclare106.addField(field114)
field115 = field()
field115.setName("lower_body_rotation_changed")
field115.setAccessType("outputOnly")
field115.setType("SFRotation")

ExternProtoDeclare106.addField(field115)
field116 = field()
field116.setName("l_hip_rotation_changed")
field116.setAccessType("outputOnly")
field116.setType("SFRotation")

ExternProtoDeclare106.addField(field116)
field117 = field()
field117.setName("l_knee_rotation_changed")
field117.setAccessType("outputOnly")
field117.setType("SFRotation")

ExternProtoDeclare106.addField(field117)
field118 = field()
field118.setName("l_ankle_rotation_changed")
field118.setAccessType("outputOnly")
field118.setType("SFRotation")

ExternProtoDeclare106.addField(field118)
field119 = field()
field119.setName("l_midtarsal_rotation_changed")
field119.setAccessType("outputOnly")
field119.setType("SFRotation")

ExternProtoDeclare106.addField(field119)
field120 = field()
field120.setName("r_hip_rotation_changed")
field120.setAccessType("outputOnly")
field120.setType("SFRotation")

ExternProtoDeclare106.addField(field120)
field121 = field()
field121.setName("r_knee_rotation_changed")
field121.setAccessType("outputOnly")
field121.setType("SFRotation")

ExternProtoDeclare106.addField(field121)
field122 = field()
field122.setName("r_ankle_rotation_changed")
field122.setAccessType("outputOnly")
field122.setType("SFRotation")

ExternProtoDeclare106.addField(field122)
field123 = field()
field123.setName("r_midtarsal_rotation_changed")
field123.setAccessType("outputOnly")
field123.setType("SFRotation")

ExternProtoDeclare106.addField(field123)
field124 = field()
field124.setName("vl5_rotation_changed")
field124.setAccessType("outputOnly")
field124.setType("SFRotation")

ExternProtoDeclare106.addField(field124)
field125 = field()
field125.setName("skullbase_rotation_changed")
field125.setAccessType("outputOnly")
field125.setType("SFRotation")

ExternProtoDeclare106.addField(field125)
field126 = field()
field126.setName("l_shoulder_rotation_changed")
field126.setAccessType("outputOnly")
field126.setType("SFRotation")

ExternProtoDeclare106.addField(field126)
field127 = field()
field127.setName("l_elbow_rotation_changed")
field127.setAccessType("outputOnly")
field127.setType("SFRotation")

ExternProtoDeclare106.addField(field127)
field128 = field()
field128.setName("l_wrist_rotation_changed")
field128.setAccessType("outputOnly")
field128.setType("SFRotation")

ExternProtoDeclare106.addField(field128)
field129 = field()
field129.setName("r_shoulder_rotation_changed")
field129.setAccessType("outputOnly")
field129.setType("SFRotation")

ExternProtoDeclare106.addField(field129)
field130 = field()
field130.setName("r_elbow_rotation_changed")
field130.setAccessType("outputOnly")
field130.setType("SFRotation")

ExternProtoDeclare106.addField(field130)
field131 = field()
field131.setName("r_wrist_rotation_changed")
field131.setAccessType("outputOnly")
field131.setType("SFRotation")

ExternProtoDeclare106.addField(field131)
field132 = field()
field132.setName("isActive")
field132.setAccessType("outputOnly")
field132.setType("SFBool")

ExternProtoDeclare106.addField(field132)

Scene24.addChildren(ExternProtoDeclare106)
ExternProtoDeclare133 = ExternProtoDeclare()
ExternProtoDeclare133.setName("LOA1_KneelAnimation")
ExternProtoDeclare133.setUrl(["LOA1_KneelAnimation.x3d#LOA1_KneelAnimation","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/LOA1_KneelAnimation.x3d#LOA1_KneelAnimation","LOA1_KneelAnimation.wrl#LOA1_KneelAnimation","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/LOA1_KneelAnimation.wrl#LOA1_KneelAnimation"])
field134 = field()
field134.setName("cycleInterval")
field134.setAccessType("inputOutput")
field134.setType("SFTime")

ExternProtoDeclare133.addField(field134)
field135 = field()
field135.setName("enabled")
field135.setAccessType("inputOutput")
field135.setType("SFBool")

ExternProtoDeclare133.addField(field135)
field136 = field()
field136.setName("loop")
field136.setAccessType("inputOutput")
field136.setType("SFBool")

ExternProtoDeclare133.addField(field136)
field137 = field()
field137.setName("startTime")
field137.setAccessType("inputOutput")
field137.setType("SFTime")

ExternProtoDeclare133.addField(field137)
field138 = field()
field138.setName("stopTime")
field138.setAccessType("inputOutput")
field138.setType("SFTime")

ExternProtoDeclare133.addField(field138)
field139 = field()
field139.setName("fraction_changed")
field139.setAccessType("outputOnly")
field139.setType("SFFloat")

ExternProtoDeclare133.addField(field139)
field140 = field()
field140.setName("isActive")
field140.setAccessType("outputOnly")
field140.setType("SFBool")

ExternProtoDeclare133.addField(field140)
field141 = field()
field141.setName("humanoid_root_translation_changed")
field141.setAccessType("outputOnly")
field141.setType("SFVec3f")

ExternProtoDeclare133.addField(field141)
field142 = field()
field142.setName("humanoid_root_rotation_changed")
field142.setAccessType("outputOnly")
field142.setType("SFRotation")

ExternProtoDeclare133.addField(field142)
field143 = field()
field143.setName("lower_body_rotation_changed")
field143.setAccessType("outputOnly")
field143.setType("SFRotation")

ExternProtoDeclare133.addField(field143)
field144 = field()
field144.setName("l_hip_rotation_changed")
field144.setAccessType("outputOnly")
field144.setType("SFRotation")

ExternProtoDeclare133.addField(field144)
field145 = field()
field145.setName("l_knee_rotation_changed")
field145.setAccessType("outputOnly")
field145.setType("SFRotation")

ExternProtoDeclare133.addField(field145)
field146 = field()
field146.setName("l_ankle_rotation_changed")
field146.setAccessType("outputOnly")
field146.setType("SFRotation")

ExternProtoDeclare133.addField(field146)
field147 = field()
field147.setName("l_midtarsal_rotation_changed")
field147.setAccessType("outputOnly")
field147.setType("SFRotation")

ExternProtoDeclare133.addField(field147)
field148 = field()
field148.setName("r_hip_rotation_changed")
field148.setAccessType("outputOnly")
field148.setType("SFRotation")

ExternProtoDeclare133.addField(field148)
field149 = field()
field149.setName("r_knee_rotation_changed")
field149.setAccessType("outputOnly")
field149.setType("SFRotation")

ExternProtoDeclare133.addField(field149)
field150 = field()
field150.setName("r_ankle_rotation_changed")
field150.setAccessType("outputOnly")
field150.setType("SFRotation")

ExternProtoDeclare133.addField(field150)
field151 = field()
field151.setName("r_midtarsal_rotation_changed")
field151.setAccessType("outputOnly")
field151.setType("SFRotation")

ExternProtoDeclare133.addField(field151)
field152 = field()
field152.setName("vl5_rotation_changed")
field152.setAccessType("outputOnly")
field152.setType("SFRotation")

ExternProtoDeclare133.addField(field152)
field153 = field()
field153.setName("skullbase_rotation_changed")
field153.setAccessType("outputOnly")
field153.setType("SFRotation")

ExternProtoDeclare133.addField(field153)
field154 = field()
field154.setName("l_shoulder_rotation_changed")
field154.setAccessType("outputOnly")
field154.setType("SFRotation")

ExternProtoDeclare133.addField(field154)
field155 = field()
field155.setName("l_elbow_rotation_changed")
field155.setAccessType("outputOnly")
field155.setType("SFRotation")

ExternProtoDeclare133.addField(field155)
field156 = field()
field156.setName("l_wrist_rotation_changed")
field156.setAccessType("outputOnly")
field156.setType("SFRotation")

ExternProtoDeclare133.addField(field156)
field157 = field()
field157.setName("r_shoulder_rotation_changed")
field157.setAccessType("outputOnly")
field157.setType("SFRotation")

ExternProtoDeclare133.addField(field157)
field158 = field()
field158.setName("r_elbow_rotation_changed")
field158.setAccessType("outputOnly")
field158.setType("SFRotation")

ExternProtoDeclare133.addField(field158)
field159 = field()
field159.setName("r_wrist_rotation_changed")
field159.setAccessType("outputOnly")
field159.setType("SFRotation")

ExternProtoDeclare133.addField(field159)

Scene24.addChildren(ExternProtoDeclare133)
#**********Human Model Protypes*********
ProtoDeclare160 = ProtoDeclare()
ProtoDeclare160.setName("Humanoid1_1")
ProtoDeclare160.setAppinfo("The Humanoid node serves as overall container for the Joint Segment Site and Viewpoint nodes which define the skeleton geometry and landmarks of the humanoid figure. Additionally the node provides a means for defining information about the author copyright and usage restrictions of the model.")
ProtoDeclare160.setDocumentation("http://HAnim.org/Specifications/HAnim2001/part1/Humanoid.html")
ProtoInterface161 = ProtoInterface()
#HAnim v1.1 field definitions
field162 = field()
field162.setName("name")
field162.setAccessType("inputOutput")
field162.setType("SFString")

ProtoInterface161.addField(field162)
field163 = field()
field163.setName("version")
field163.setAccessType("inputOutput")
field163.setAppinfo("legal values: 1.1 or 2.0")
field163.setType("SFString")
field163.setValue("1.1")

ProtoInterface161.addField(field163)
field164 = field()
field164.setName("humanoidVersion")
field164.setAccessType("inputOutput")
field164.setAppinfo("Version of the humanoid being modeled. Hint: HAnim version 2.0")
field164.setType("SFString")

ProtoInterface161.addField(field164)
field165 = field()
field165.setName("info")
field165.setAccessType("inputOutput")
field165.setType("MFString")

ProtoInterface161.addField(field165)
field166 = field()
field166.setName("translation")
field166.setAccessType("inputOutput")
field166.setType("SFVec3f")
field166.setValue("0 0 0")

ProtoInterface161.addField(field166)
field167 = field()
field167.setName("rotation")
field167.setAccessType("inputOutput")
field167.setType("SFRotation")
field167.setValue("0 0 1 0")

ProtoInterface161.addField(field167)
field168 = field()
field168.setName("center")
field168.setAccessType("inputOutput")
field168.setType("SFVec3f")
field168.setValue("0 0 0")

ProtoInterface161.addField(field168)
field169 = field()
field169.setName("scale")
field169.setAccessType("inputOutput")
field169.setType("SFVec3f")
field169.setValue("1 1 1")

ProtoInterface161.addField(field169)
field170 = field()
field170.setName("scaleOrientation")
field170.setAccessType("inputOutput")
field170.setType("SFRotation")
field170.setValue("0 0 1 0")

ProtoInterface161.addField(field170)
field171 = field()
field171.setName("bboxCenter")
field171.setAccessType("initializeOnly")
field171.setType("SFVec3f")
field171.setValue("0 0 0")

ProtoInterface161.addField(field171)
field172 = field()
field172.setName("bboxSize")
field172.setAccessType("initializeOnly")
field172.setType("SFVec3f")
field172.setValue("-1 -1 -1")

ProtoInterface161.addField(field172)
field173 = field()
field173.setName("humanoidBody")
field173.setAccessType("inputOutput")
field173.setAppinfo("HAnim 1.1 field container for body head. Hint: replaced by 2.0 skeleton.")
field173.setDocumentation("http://HAnim.org/Specifications/HAnim1.1/#humanoid")
field173.setType("MFNode")

ProtoInterface161.addField(field173)
field174 = field()
field174.setName("skeleton")
field174.setAccessType("inputOutput")
field174.setAppinfo("HAnim 2.0 field container for body geometry Hint: replaces 1.1 humanoidBody")
field174.setDocumentation("http://HAnim.org/Specifications/HAnim2001/part1/Humanoid.html")
field174.setType("MFNode")

ProtoInterface161.addField(field174)
field175 = field()
field175.setName("joints")
field175.setAccessType("inputOutput")
field175.setAppinfo("Container field for Joint nodes")
field175.setType("MFNode")

ProtoInterface161.addField(field175)
field176 = field()
field176.setName("segments")
field176.setAccessType("inputOutput")
field176.setAppinfo("Container field for Segment nodes")
field176.setType("MFNode")

ProtoInterface161.addField(field176)
field177 = field()
field177.setName("sites")
field177.setAccessType("inputOutput")
field177.setAppinfo("Container field for Site nodes")
field177.setType("MFNode")

ProtoInterface161.addField(field177)
field178 = field()
field178.setName("viewpoints")
field178.setAccessType("inputOutput")
field178.setAppinfo("Container field for Viewpoint nodes")
field178.setType("MFNode")

ProtoInterface161.addField(field178)
field179 = field()
field179.setName("skinCoord")
field179.setAccessType("inputOutput")
field179.setAppinfo("Hint: HAnim version 2.0")
field179.setType("SFNode")
#NULL node

ProtoInterface161.addField(field179)
field180 = field()
field180.setName("skinNormal")
field180.setAccessType("inputOutput")
field180.setAppinfo("Hint: HAnim version 2.0")
field180.setType("SFNode")
#NULL node

ProtoInterface161.addField(field180)

ProtoDeclare160.setProtoInterface(ProtoInterface161)
ProtoBody181 = ProtoBody()
Transform182 = Transform()
Transform182.setDEF("HumanoidTransform")
IS183 = IS()
connect184 = connect()
connect184.setNodeField("translation")
connect184.setProtoField("translation")

IS183.addConnect(connect184)
connect185 = connect()
connect185.setNodeField("rotation")
connect185.setProtoField("rotation")

IS183.addConnect(connect185)
connect186 = connect()
connect186.setNodeField("center")
connect186.setProtoField("center")

IS183.addConnect(connect186)
connect187 = connect()
connect187.setNodeField("scale")
connect187.setProtoField("scale")

IS183.addConnect(connect187)
connect188 = connect()
connect188.setNodeField("scaleOrientation")
connect188.setProtoField("scaleOrientation")

IS183.addConnect(connect188)
connect189 = connect()
connect189.setNodeField("bboxCenter")
connect189.setProtoField("bboxCenter")

IS183.addConnect(connect189)
connect190 = connect()
connect190.setNodeField("bboxSize")
connect190.setProtoField("bboxSize")

IS183.addConnect(connect190)

Transform182.setIS(IS183)
Group191 = Group()
Group191.setDEF("HumanoidGroup1")
IS192 = IS()
connect193 = connect()
connect193.setNodeField("children")
connect193.setProtoField("humanoidBody")

IS192.addConnect(connect193)

Group191.setIS(IS192)

Transform182.addChildren(Group191)
Group194 = Group()
Group194.setDEF("HumanoidGroup2")
IS195 = IS()
connect196 = connect()
connect196.setNodeField("children")
connect196.setProtoField("skeleton")

IS195.addConnect(connect196)

Group194.setIS(IS195)

Transform182.addChildren(Group194)
Group197 = Group()
Group197.setDEF("HumanoidGroup3")
IS198 = IS()
connect199 = connect()
connect199.setNodeField("children")
connect199.setProtoField("viewpoints")

IS198.addConnect(connect199)

Group197.setIS(IS198)

Transform182.addChildren(Group197)

ProtoBody181.addChildren(Transform182)

ProtoDeclare160.setProtoBody(ProtoBody181)

Scene24.addChildren(ProtoDeclare160)
ProtoDeclare200 = ProtoDeclare()
ProtoDeclare200.setName("Joint")
ProtoDeclare200.setAppinfo("The Joint node is used as a building block to describe the articulations of the humanoid figure. Each articulation of the humanoid figure is represented by a Joint node each of which is organized into a hierarchy that describes the overall skeleton of the humanoid.")
ProtoDeclare200.setDocumentation("http://HAnim.org/Specifications/HAnim2001/part1/Joint.html")
ProtoInterface201 = ProtoInterface()
field202 = field()
field202.setName("name")
field202.setAccessType("inputOutput")
field202.setType("SFString")

ProtoInterface201.addField(field202)
field203 = field()
field203.setName("ulimit")
field203.setAccessType("inputOutput")
field203.setType("MFFloat")

ProtoInterface201.addField(field203)
field204 = field()
field204.setName("llimit")
field204.setAccessType("inputOutput")
field204.setType("MFFloat")

ProtoInterface201.addField(field204)
field205 = field()
field205.setName("limitOrientation")
field205.setAccessType("inputOutput")
field205.setType("SFRotation")
field205.setValue("0 0 1 0")

ProtoInterface201.addField(field205)
field206 = field()
field206.setName("skinCoordIndex")
field206.setAccessType("inputOutput")
field206.setType("MFInt32")

ProtoInterface201.addField(field206)
field207 = field()
field207.setName("skinCoordWeight")
field207.setAccessType("inputOutput")
field207.setType("MFFloat")

ProtoInterface201.addField(field207)
field208 = field()
field208.setName("stiffness")
field208.setAccessType("inputOutput")
field208.setType("MFFloat")
field208.setValue("0 0 0")

ProtoInterface201.addField(field208)
field209 = field()
field209.setName("translation")
field209.setAccessType("inputOutput")
field209.setType("SFVec3f")
field209.setValue("0 0 0")

ProtoInterface201.addField(field209)
field210 = field()
field210.setName("rotation")
field210.setAccessType("inputOutput")
field210.setType("SFRotation")
field210.setValue("0 0 1 0")

ProtoInterface201.addField(field210)
field211 = field()
field211.setName("scale")
field211.setAccessType("inputOutput")
field211.setType("SFVec3f")
field211.setValue("1 1 1")

ProtoInterface201.addField(field211)
field212 = field()
field212.setName("scaleOrientation")
field212.setAccessType("inputOutput")
field212.setType("SFRotation")
field212.setValue("0 0 1 0")

ProtoInterface201.addField(field212)
field213 = field()
field213.setName("center")
field213.setAccessType("inputOutput")
field213.setType("SFVec3f")
field213.setValue("0 0 0")

ProtoInterface201.addField(field213)
field214 = field()
field214.setName("bboxCenter")
field214.setAccessType("initializeOnly")
field214.setType("SFVec3f")
field214.setValue("0 0 0")

ProtoInterface201.addField(field214)
field215 = field()
field215.setName("bboxSize")
field215.setAccessType("initializeOnly")
field215.setType("SFVec3f")
field215.setValue("-1 -1 -1")

ProtoInterface201.addField(field215)
field216 = field()
field216.setName("children")
field216.setAccessType("inputOutput")
field216.setType("MFNode")

ProtoInterface201.addField(field216)
field217 = field()
field217.setName("addChildren")
field217.setAccessType("inputOnly")
field217.setType("MFNode")

ProtoInterface201.addField(field217)
field218 = field()
field218.setName("removeChildren")
field218.setAccessType("inputOnly")
field218.setType("MFNode")

ProtoInterface201.addField(field218)

ProtoDeclare200.setProtoInterface(ProtoInterface201)
ProtoBody219 = ProtoBody()
Transform220 = Transform()
Transform220.setDEF("JointTransform")
IS221 = IS()
connect222 = connect()
connect222.setNodeField("translation")
connect222.setProtoField("translation")

IS221.addConnect(connect222)
connect223 = connect()
connect223.setNodeField("rotation")
connect223.setProtoField("rotation")

IS221.addConnect(connect223)
connect224 = connect()
connect224.setNodeField("center")
connect224.setProtoField("center")

IS221.addConnect(connect224)
connect225 = connect()
connect225.setNodeField("scale")
connect225.setProtoField("scale")

IS221.addConnect(connect225)
connect226 = connect()
connect226.setNodeField("scaleOrientation")
connect226.setProtoField("scaleOrientation")

IS221.addConnect(connect226)
connect227 = connect()
connect227.setNodeField("bboxCenter")
connect227.setProtoField("bboxCenter")

IS221.addConnect(connect227)
connect228 = connect()
connect228.setNodeField("bboxSize")
connect228.setProtoField("bboxSize")

IS221.addConnect(connect228)
connect229 = connect()
connect229.setNodeField("children")
connect229.setProtoField("children")

IS221.addConnect(connect229)
connect230 = connect()
connect230.setNodeField("addChildren")
connect230.setProtoField("addChildren")

IS221.addConnect(connect230)
connect231 = connect()
connect231.setNodeField("removeChildren")
connect231.setProtoField("removeChildren")

IS221.addConnect(connect231)

Transform220.setIS(IS221)

ProtoBody219.addChildren(Transform220)

ProtoDeclare200.setProtoBody(ProtoBody219)

Scene24.addChildren(ProtoDeclare200)
ProtoDeclare232 = ProtoDeclare()
ProtoDeclare232.setName("Segment")
ProtoDeclare232.setAppinfo("The Segment node is used describe the attributes of the physical links between the joints of the humanoid figure. Each body part (pelvis thigh calf etc.) of the humanoid figure is represented by a Segment node.")
ProtoDeclare232.setDocumentation("http://HAnim.org/Specifications/HAnim2001/part1/Segment.html")
ProtoInterface233 = ProtoInterface()
field234 = field()
field234.setName("name")
field234.setAccessType("inputOutput")
field234.setType("SFString")

ProtoInterface233.addField(field234)
field235 = field()
field235.setName("mass")
field235.setAccessType("inputOutput")
field235.setType("SFFloat")
field235.setValue("0")

ProtoInterface233.addField(field235)
field236 = field()
field236.setName("centerOfMass")
field236.setAccessType("inputOutput")
field236.setType("SFVec3f")
field236.setValue("0 0 0")

ProtoInterface233.addField(field236)
field237 = field()
field237.setName("momentsOfInertia")
field237.setAccessType("inputOutput")
field237.setType("MFFloat")
field237.setValue("0 0 0 0 0 0 0 0 0")

ProtoInterface233.addField(field237)
field238 = field()
field238.setName("bboxCenter")
field238.setAccessType("initializeOnly")
field238.setType("SFVec3f")
field238.setValue("0 0 0")

ProtoInterface233.addField(field238)
field239 = field()
field239.setName("bboxSize")
field239.setAccessType("initializeOnly")
field239.setType("SFVec3f")
field239.setValue("-1 -1 -1")

ProtoInterface233.addField(field239)
field240 = field()
field240.setName("children")
field240.setAccessType("inputOutput")
field240.setType("MFNode")

ProtoInterface233.addField(field240)
field241 = field()
field241.setName("addChildren")
field241.setAccessType("inputOnly")
field241.setType("MFNode")

ProtoInterface233.addField(field241)
field242 = field()
field242.setName("removeChildren")
field242.setAccessType("inputOnly")
field242.setType("MFNode")

ProtoInterface233.addField(field242)
field243 = field()
field243.setName("coord")
field243.setAccessType("inputOutput")
field243.setAppinfo("contains Coordinate nodes")
field243.setType("SFNode")
#NULL node

ProtoInterface233.addField(field243)
field244 = field()
field244.setName("displacers")
field244.setAccessType("inputOutput")
field244.setAppinfo("contains Displacer nodes")
field244.setType("MFNode")

ProtoInterface233.addField(field244)

ProtoDeclare232.setProtoInterface(ProtoInterface233)
ProtoBody245 = ProtoBody()
Group246 = Group()
Group246.setDEF("SegmentGroup")
IS247 = IS()
connect248 = connect()
connect248.setNodeField("bboxCenter")
connect248.setProtoField("bboxCenter")

IS247.addConnect(connect248)
connect249 = connect()
connect249.setNodeField("bboxSize")
connect249.setProtoField("bboxSize")

IS247.addConnect(connect249)
connect250 = connect()
connect250.setNodeField("children")
connect250.setProtoField("children")

IS247.addConnect(connect250)
connect251 = connect()
connect251.setNodeField("addChildren")
connect251.setProtoField("addChildren")

IS247.addConnect(connect251)
connect252 = connect()
connect252.setNodeField("removeChildren")
connect252.setProtoField("removeChildren")

IS247.addConnect(connect252)

Group246.setIS(IS247)

ProtoBody245.addChildren(Group246)

ProtoDeclare232.setProtoBody(ProtoBody245)

Scene24.addChildren(ProtoDeclare232)
ProtoDeclare253 = ProtoDeclare()
ProtoDeclare253.setName("Site")
ProtoDeclare253.setAppinfo("The Site node can be used for three purposes: (a) to define an \"end effector\" location which can be used by an inverse kinematics system (b) to define an attachment point for accessories such as jewelry and clothing and (c) to define a location for a virtual camera in the reference frame of a Segment node (such as a view \"through the eyes\" of the humanoid for use in multi-user worlds).")
ProtoDeclare253.setDocumentation("http://HAnim.org/Specifications/HAnim2001/part1/Site.html")
ProtoInterface254 = ProtoInterface()
field255 = field()
field255.setName("name")
field255.setAccessType("inputOutput")
field255.setType("SFString")

ProtoInterface254.addField(field255)
field256 = field()
field256.setName("translation")
field256.setAccessType("inputOutput")
field256.setType("SFVec3f")
field256.setValue("0 0 0")

ProtoInterface254.addField(field256)
field257 = field()
field257.setName("rotation")
field257.setAccessType("inputOutput")
field257.setType("SFRotation")
field257.setValue("0 0 1 0")

ProtoInterface254.addField(field257)
field258 = field()
field258.setName("scale")
field258.setAccessType("inputOutput")
field258.setType("SFVec3f")
field258.setValue("1 1 1")

ProtoInterface254.addField(field258)
field259 = field()
field259.setName("scaleOrientation")
field259.setAccessType("inputOutput")
field259.setType("SFRotation")
field259.setValue("0 0 1 0")

ProtoInterface254.addField(field259)
field260 = field()
field260.setName("center")
field260.setAccessType("inputOutput")
field260.setType("SFVec3f")
field260.setValue("0 0 0")

ProtoInterface254.addField(field260)
field261 = field()
field261.setName("bboxCenter")
field261.setAccessType("initializeOnly")
field261.setType("SFVec3f")
field261.setValue("0 0 0")

ProtoInterface254.addField(field261)
field262 = field()
field262.setName("bboxSize")
field262.setAccessType("initializeOnly")
field262.setType("SFVec3f")
field262.setValue("-1 -1 -1")

ProtoInterface254.addField(field262)
field263 = field()
field263.setName("children")
field263.setAccessType("inputOutput")
field263.setType("MFNode")

ProtoInterface254.addField(field263)
field264 = field()
field264.setName("addChildren")
field264.setAccessType("inputOnly")
field264.setType("MFNode")

ProtoInterface254.addField(field264)
field265 = field()
field265.setName("removeChildren")
field265.setAccessType("inputOnly")
field265.setType("MFNode")

ProtoInterface254.addField(field265)

ProtoDeclare253.setProtoInterface(ProtoInterface254)
ProtoBody266 = ProtoBody()
Transform267 = Transform()
Transform267.setDEF("SiteTransform")
IS268 = IS()
connect269 = connect()
connect269.setNodeField("translation")
connect269.setProtoField("translation")

IS268.addConnect(connect269)
connect270 = connect()
connect270.setNodeField("rotation")
connect270.setProtoField("rotation")

IS268.addConnect(connect270)
connect271 = connect()
connect271.setNodeField("center")
connect271.setProtoField("center")

IS268.addConnect(connect271)
connect272 = connect()
connect272.setNodeField("scale")
connect272.setProtoField("scale")

IS268.addConnect(connect272)
connect273 = connect()
connect273.setNodeField("scaleOrientation")
connect273.setProtoField("scaleOrientation")

IS268.addConnect(connect273)
connect274 = connect()
connect274.setNodeField("bboxCenter")
connect274.setProtoField("bboxCenter")

IS268.addConnect(connect274)
connect275 = connect()
connect275.setNodeField("bboxSize")
connect275.setProtoField("bboxSize")

IS268.addConnect(connect275)
connect276 = connect()
connect276.setNodeField("children")
connect276.setProtoField("children")

IS268.addConnect(connect276)
connect277 = connect()
connect277.setNodeField("addChildren")
connect277.setProtoField("addChildren")

IS268.addConnect(connect277)
connect278 = connect()
connect278.setNodeField("removeChildren")
connect278.setProtoField("removeChildren")

IS268.addConnect(connect278)

Transform267.setIS(IS268)

ProtoBody266.addChildren(Transform267)

ProtoDeclare253.setProtoBody(ProtoBody266)

Scene24.addChildren(ProtoDeclare253)
ProtoDeclare279 = ProtoDeclare()
ProtoDeclare279.setName("Displacer")
ProtoDeclare279.setAppinfo("A Displacer can be used in three different ways: (a) identify the vertices corresponding to a particular feature on a Segment (b) represent a particular muscular action which displaces the vertices in various directions (linearly or radially) and (c) represent a complete configuration of the vertices in a Segment.")
ProtoDeclare279.setDocumentation("http://HAnim.org/Specifications/HAnim2001/part1/Displacer.html")
ProtoInterface280 = ProtoInterface()
field281 = field()
field281.setName("name")
field281.setAccessType("inputOutput")
field281.setType("SFString")

ProtoInterface280.addField(field281)
field282 = field()
field282.setName("coordIndex")
field282.setAccessType("inputOutput")
field282.setType("MFInt32")

ProtoInterface280.addField(field282)
field283 = field()
field283.setName("displacements")
field283.setAccessType("inputOutput")
field283.setType("MFVec3f")

ProtoInterface280.addField(field283)

ProtoDeclare279.setProtoInterface(ProtoInterface280)
ProtoBody284 = ProtoBody()
WorldInfo285 = WorldInfo()
WorldInfo285.setInfo(["null body node"])

ProtoBody284.addChildren(WorldInfo285)

ProtoDeclare279.setProtoBody(ProtoBody284)

Scene24.addChildren(ProtoDeclare279)
#***********ViewPoints*************
Viewpoint286 = Viewpoint()
Viewpoint286.setDEF("InclinedView")
Viewpoint286.setDescription("Inclined View")
Viewpoint286.setOrientation([-0.113,0.993,0.0347,0.671])
Viewpoint286.setPosition([1.62,1.05,2.06])

Scene24.addChildren(Viewpoint286)
Viewpoint287 = Viewpoint()
Viewpoint287.setDEF("FrontView")
Viewpoint287.setDescription("Front View")
Viewpoint287.setPosition([0,0.854,2.57665])

Scene24.addChildren(Viewpoint287)
Viewpoint288 = Viewpoint()
Viewpoint288.setDEF("SideView")
Viewpoint288.setDescription("Side View")
Viewpoint288.setOrientation([0,1,0,1.57079])
Viewpoint288.setPosition([2.5929,0.854,0])

Scene24.addChildren(Viewpoint288)
Viewpoint289 = Viewpoint()
Viewpoint289.setDEF("TopView")
Viewpoint289.setDescription("Top View")
Viewpoint289.setOrientation([1,0,0,-1.57079])
Viewpoint289.setPosition([0,3.4495,0])

Scene24.addChildren(Viewpoint289)
NavigationInfo290 = NavigationInfo()
NavigationInfo290.setAvatarSize([0.15,1.53,0.75])
NavigationInfo290.setSpeed(0.5)
NavigationInfo290.setType(["EXAMINE"])

Scene24.addChildren(NavigationInfo290)
#**********Avatar Proto Instances***********
Switch291 = Switch()
Switch291.setDEF("AvatarSwitch")
Switch291.setWhichChoice(0)
#Humanoid1 used for v1.1 humanoid, which is what Allen and Nancy are. Boxman is HAnim 2001. Can't have identically named prototypes for Humanoid in each version since prototype signatures are different.
ProtoInstance292 = ProtoInstance()
ProtoInstance292.setName("Humanoid1_1")
ProtoInstance292.setDEF("Allen")
fieldValue293 = fieldValue()
fieldValue293.setName("humanoidBody")
ProtoInstance294 = ProtoInstance()
ProtoInstance294.setName("Joint")
ProtoInstance294.setDEF("Allen_hanim_humanoid_root")
fieldValue295 = fieldValue()
fieldValue295.setName("name")
fieldValue295.setValue("humanoid_root")

ProtoInstance294.addFieldValue(fieldValue295)
fieldValue296 = fieldValue()
fieldValue296.setName("center")
fieldValue296.setValue("-0.00405 0.855 -0.000113")

ProtoInstance294.addFieldValue(fieldValue296)
fieldValue297 = fieldValue()
fieldValue297.setName("children")
ProtoInstance298 = ProtoInstance()
ProtoInstance298.setName("Joint")
ProtoInstance298.setDEF("Allen_hanim_sacroiliac")
fieldValue299 = fieldValue()
fieldValue299.setName("name")
fieldValue299.setValue("sacroiliac")

ProtoInstance298.addFieldValue(fieldValue299)
fieldValue300 = fieldValue()
fieldValue300.setName("center")
fieldValue300.setValue("0 1.01 -0.0204")

ProtoInstance298.addFieldValue(fieldValue300)
fieldValue301 = fieldValue()
fieldValue301.setName("children")
ProtoInstance302 = ProtoInstance()
ProtoInstance302.setName("Segment")
ProtoInstance302.setDEF("Allen_hanim_pelvis")
fieldValue303 = fieldValue()
fieldValue303.setName("name")
fieldValue303.setValue("pelvis")

ProtoInstance302.addFieldValue(fieldValue303)
fieldValue304 = fieldValue()
fieldValue304.setName("children")
Transform305 = Transform()
Transform305.setCenter([-0.7455,1,0.058])
Transform305.setRotation([0,1,0,1.570796])
Transform305.setScale([0.1,0.1,0.1])
Shape306 = Shape()
Appearance307 = Appearance()
Material308 = Material()
Material308.setDEF("Pants_Color")
Material308.setAmbientIntensity(0.25)
Material308.setDiffuseColor([0.054,0.233,0.39])

Appearance307.setMaterial(Material308)
ImageTexture309 = ImageTexture()
ImageTexture309.setDEF("camo")
ImageTexture309.setRepeatS(False)
ImageTexture309.setRepeatT(False)
ImageTexture309.setUrl(["greenCamo.gif","greenCamo.jpg","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/greenCamo.gif","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/greenCamo.jpg"])

Appearance307.setTexture(ImageTexture309)

Shape306.setAppearance(Appearance307)
IndexedFaceSet310 = IndexedFaceSet()
IndexedFaceSet310.setCoordIndex([0,1,2,-1,3,4,5,-1,6,7,8,-1,9,10,11,-1,12,13,14,-1,15,16,17,-1,18,19,20,-1,21,22,23,-1,24,25,26,-1,27,28,29,-1,30,31,32,-1,33,34,35,-1,36,37,38,-1,39,40,41,-1,42,43,44,-1,45,46,47,-1,48,49,50,-1,51,52,53,-1,54,55,56,-1,57,58,59,-1,60,61,62,-1,63,64,65,-1,66,67,68,-1,69,70,71,-1,72,73,74,-1,75,76,77,-1,78,79,80,-1,81,82,83,-1,84,85,86,-1,87,88,89,-1,90,91,92,-1,93,94,95,-1,96,97,98,-1,99,100,101,-1,102,103,104,-1,105,106,107,-1,108,109,110,-1,111,112,113,-1,114,115,116,-1,117,118,119,-1,120,121,122,-1,123,124,125,-1,126,127,128,-1,129,130,131,-1,132,133,134,-1,135,136,137,-1,138,139,140,-1,141,142,143,-1,144,145,146,-1,147,148,149,-1,150,151,152,-1,153,154,155,-1,156,157,158,-1,159,160,161,-1,162,163,164,-1,165,166,167,-1,168,169,170,-1,171,172,173,-1,174,175,176,-1,177,178,179,-1,180,181,182,-1,183,184,185,-1,186,187,188,-1,189,190,191,-1,192,193,194,-1,195,196,197,-1,198,199,200,-1,201,202,203,-1,204,205,206,-1,207,208,209,-1,210,211,212,-1,213,214,215,-1,216,217,218,-1,219,220,221,-1,222,223,224,-1,225,226,227,-1,228,229,230,-1,231,232,233,-1,234,235,236,-1,237,238,239,-1,240,241,242,-1,243,244,245,-1,246,247,248,-1,249,250,251,-1,252,253,254,-1,255,256,257,-1,258,259,260,-1,261,262,263,-1,264,265,266,-1,267,268,269,-1,270,271,272,-1,273,274,275,-1,276,277,278,-1,279,280,281,-1,282,283,284,-1,285,286,287,-1,288,289,290,-1,291,292,293,-1,294,295,296,-1,297,298,299,-1,300,301,302,-1,303,304,305,-1,306,307,308,-1,309,310,311,-1,312,313,314,-1,315,316,317,-1,318,319,320,-1,321,322,323,-1,324,325,326,-1,327,328,329,-1,330,331,332,-1,333,334,335,-1,336,337,338,-1,339,340,341,-1,342,343,344,-1,345,346,347,-1,348,349,350,-1,351,352,353,-1,354,355,356,-1,357,358,359,-1,360,361,362,-1,363,364,365,-1,366,367,368,-1,369,370,371,-1,372,373,374,-1,375,376,377,-1,378,379,380,-1,381,382,383,-1,384,385,386,-1,387,388,389,-1,390,391,392,-1,393,394,395,-1,396,397,398,-1,399,400,401,-1,402,403,404,-1,405,406,407,-1,408,409,410,-1,411,412,413,-1,414,415,416,-1,417,418,419,-1,420,421,422,-1,423,424,425,-1,426,427,428,-1,429,430,431,-1,432,433,434,-1,435,436,437,-1,438,439,440,-1,441,442,443,-1,444,445,446,-1,447,448,449,-1,450,451,452,-1,453,454,455,-1,456,457,458,-1,459,460,461,-1,462,463,464,-1,465,466,467,-1,468,469,470,-1,471,472,473,-1,474,475,476,-1,477,478,479,-1,480,481,482,-1,483,484,485,-1,486,487,488,-1,489,490,491,-1,492,493,494,-1,495,496,497,-1,498,499,500,-1,501,502,503,-1,504,505,506,-1,507,508,509,-1,510,511,512,-1,513,514,515,-1,516,517,518,-1,519,520,521,-1,522,523,524,-1,525,526,527,-1,528,529,530,-1,531,532,533,-1,534,535,536,-1,537,538,539,-1,540,541,542,-1,543,544,545,-1,546,547,548,-1,549,550,551,-1,552,553,554,-1,555,556,557,-1,558,559,560,-1,561,562,563,-1,564,565,566,-1,567,568,569,-1,570,571,572,-1,573,574,575,-1,576,577,578,-1,579,580,581,-1,582,583,584,-1,585,586,587,-1,588,589,590,-1,591,592,593,-1,594,595,596,-1,597,598,599,-1,600,601,602,-1,603,604,605,-1,606,607,608,-1,609,610,611,-1,612,613,614,-1,615,616,617,-1,618,619,620,-1,621,622,623,-1,624,625,626,-1,627,628,629,-1,630,631,632,-1,633,634,635,-1,636,637,638,-1,639,640,641,-1,642,643,644,-1,645,646,647,-1,648,649,650,-1,651,652,653,-1,654,655,656,-1,657,658,659,-1,660,661,662,-1,663,664,665,-1,666,667,668,-1,669,670,671,-1,672,673,674,-1,675,676,677,-1,678,679,680,-1,681,682,683,-1,684,685,686,-1,687,688,689,-1,690,691,692,-1,693,694,695,-1,696,697,698,-1,699,700,701,-1,702,703,704,-1,705,706,707,-1,708,709,710,-1,711,712,713,-1,714,715,716,-1,717,718,719,-1,720,721,722,-1,723,724,725,-1,726,727,728,-1,729,730,731,-1,732,733,734,-1,735,736,737,-1,738,739,740,-1,741,742,743,-1,744,745,746,-1,747,748,749,-1,750,751,752,-1,753,754,755,-1,756,757,758,-1,759,760,761,-1,762,763,764,-1,765,766,767,-1,768,769,770,-1,771,772,773,-1,774,775,776,-1,777,778,779,-1,780,781,782,-1,783,784,785,-1,786,787,788,-1,789,790,791,-1,792,793,794,-1,795,796,797,-1,798,799,800,-1,801,802,803,-1,804,805,806,-1,807,808,809,-1,810,811,812,-1,813,814,815,-1,816,817,818,-1,819,820,821,-1,822,823,824,-1,825,826,827,-1,828,829,830,-1,831,832,833,-1,834,835,836,-1,837,838,839,-1,840,841,842,-1,843,844,845,-1,846,847,848,-1,849,850,851,-1,852,853,854,-1,855,856,857,-1,858,859,860,-1,861,862,863,-1,864,865,866,-1,867,868,869,-1,870,871,872,-1,873,874,875,-1,876,877,878,-1,879,880,881,-1,882,883,884,-1,885,886,887,-1,888,889,890,-1,891,892,893,-1,894,895,896,-1,897,898,899,-1,900,901,902,-1,903,904,905,-1,906,907,908,-1,909,910,911,-1,912,913,914,-1,915,916,917,-1,918,919,920,-1,921,922,923,-1,924,925,926,-1,927,928,929,-1,930,931,932,-1,933,934,935,-1,936,937,938,-1,939,940,941,-1,942,943,944,-1,945,946,947,-1,948,949,950,-1,951,952,953,-1,954,955,956,-1,957,958,959,-1,960,961,962,-1,963,964,965,-1,966,967,968,-1,969,970,971,-1,972,973,974,-1,975,976,977,-1,978,979,980,-1,981,982,983,-1,984,985,986,-1,987,988,989,-1,990,991,992,-1,993,994,995,-1,996,997,998,-1,999,1000,1001,-1,1002,1003,1004,-1,1005,1006,1007,-1,1008,1009,1010,-1,1011,1012,1013,-1,1014,1015,1016,-1,1017,1018,1019,-1,1020,1021,1022,-1,1023,1024,1025,-1,1026,1027,1028,-1,1029,1030,1031,-1,1032,1033,1034,-1,1035,1036,1037,-1,1038,1039,1040,-1,1041,1042,1043,-1,1044,1045,1046,-1,1047,1048,1049,-1,1050,1051,1052,-1,1053,1054,1055,-1,1056,1057,1058,-1,1059,1060,1061,-1,1062,1063,1064,-1,1065,1066,1067,-1,1068,1069,1070,-1,1071,1072,1073,-1,1074,1075,1076,-1,1077,1078,1079,-1,1080,1081,1082,-1,1083,1084,1085,-1,1086,1087,1088,-1,1089,1090,1091,-1,1092,1093,1094,-1,1095,1096,1097,-1,1098,1099,1100,-1,1101,1102,1103,-1,1104,1105,1106,-1,1107,1108,1109,-1,1110,1111,1112,-1,1113,1114,1115,-1,1116,1117,1118,-1,1119,1120,1121,-1,1122,1123,1124,-1,1125,1126,1127,-1,1128,1129,1130,-1,1131,1132,1133,-1,1134,1135,1136,-1,1137,1138,1139,-1,1140,1141,1142,-1,1143,1144,1145,-1,1146,1147,1148,-1,1149,1150,1151,-1,1152,1153,1154,-1,1155,1156,1157,-1,1158,1159,1160,-1,1161,1162,1163,-1,1164,1165,1166,-1,1167,1168,1169,-1,1170,1171,1172,-1,1173,1174,1175,-1,1176,1177,1178,-1,1179,1180,1181,-1,1182,1183,1184,-1,1185,1186,1187,-1,1188,1189,1190,-1,1191,1192,1193,-1,1194,1195,1196,-1,1197,1198,1199,-1,1200,1201,1202,-1,1203,1204,1205,-1,1206,1207,1208,-1,1209,1210,1211,-1,1212,1213,1214,-1,1215,1216,1217,-1,1218,1219,1220,-1,1221,1222,1223,-1,1224,1225,1226,-1,1227,1228,1229,-1,1230,1231,1232,-1,1233,1234,1235,-1,1236,1237,1238,-1,1239,1240,1241,-1,1242,1243,1244,-1,1245,1246,1247,-1,1248,1249,1250,-1,1251,1252,1253,-1,1254,1255,1256,-1,1257,1258,1259,-1,1260,1261,1262,-1,1263,1264,1265,-1,1266,1267,1268,-1,1269,1270,1271,-1,1272,1273,1274,-1,1275,1276,1277,-1,1278,1279,1280,-1,1281,1282,1283,-1,1284,1285,1286,-1,1287,1288,1289,-1,1290,1291,1292,-1,1293,1294,1295,-1,1296,1297,1298,-1,1299,1300,1301,-1,1302,1303,1304,-1,1305,1306,1307,-1,1308,1309,1310,-1,1311,1312,1313,-1,1314,1315,1316,-1,1317,1318,1319,-1,1320,1321,1322,-1,1323,1324,1325,-1,1326,1327,1328,-1,1329,1330,1331,-1,1332,1333,1334,-1,1335,1336,1337,-1,1338,1339,1340,-1,1341,1342,1343,-1,1344,1345,1346,-1,1347,1348,1349,-1,1350,1351,1352,-1,1353,1354,1355,-1,1356,1357,1358,-1,1359,1360,1361,-1,1362,1363,1364,-1,1365,1366,1367,-1,1368,1369,1370,-1,1371,1372,1373,-1,1374,1375,1376,-1,1377,1378,1379,-1,1380,1381,1382,-1,1383,1384,1385,-1,1386,1387,1388,-1,1389,1390,1391,-1,1392,1393,1394,-1,1395,1396,1397,-1,1398,1399,1400,-1,1401,1402,1403,-1,1404,1405,1406,-1,1407,1408,1409,-1,1410,1411,1412,-1,1413,1414,1415,-1,1416,1417,1418,-1,1419,1420,1421,-1,1422,1423,1424,-1,1425,1426,1427,-1,1428,1429,1430,-1,1431,1432,1433,-1,1434,1435,1436,-1,1437,1438,1439,-1,1440,1441,1442,-1,1443,1444,1445,-1,1446,1447,1448,-1,1449,1450,1451,-1,1452,1453,1454,-1,1455,1456,1457,-1,1458,1459,1460,-1,1461,1462,1463,-1,1464,1465,1466,-1,1467,1468,1469,-1,1470,1471,1472,-1,1473,1474,1475,-1,1476,1477,1478,-1,1479,1480,1481,-1,1482,1483,1484,-1,1485,1486,1487,-1,1488,1489,1490,-1,1491,1492,1493,-1,1494,1495,1496,-1,1497,1498,1499,-1,1500,1501,1502,-1,1503,1504,1505,-1,1506,1507,1508,-1,1509,1510,1511,-1,1512,1513,1514,-1,1515,1516,1517,-1,1518,1519,1520,-1,1521,1522,1523,-1,1524,1525,1526,-1,1527,1528,1529,-1,1530,1531,1532,-1,1533,1534,1535,-1,1536,1537,1538,-1,1539,1540,1541,-1,1542,1543,1544,-1,1545,1546,1547,-1,1548,1549,1550,-1,1551,1552,1553,-1,1554,1555,1556,-1,1557,1558,1559,-1,1560,1561,1562,-1,1563,1564,1565,-1,1566,1567,1568,-1,1569,1570,1571,-1,1572,1573,1574,-1,1575,1576,1577,-1,1578,1579,1580,-1,1581,1582,1583,-1,1584,1585,1586,-1,1587,1588,1589,-1,1590,1591,1592,-1,1593,1594,1595,-1,1596,1597,1598,-1,1599,1600,1601,-1,1602,1603,1604,-1,1605,1606,1607,-1,1608,1609,1610,-1,1611,1612,1613,-1,1614,1615,1616,-1,1617,1618,1619,-1,1620,1621,1622,-1,1623,1624,1625,-1,1626,1627,1628,-1,1629,1630,1631,-1,1632,1633,1634,-1,1635,1636,1637,-1,1638,1639,1640,-1,1641,1642,1643,-1,1644,1645,1646,-1,1647,1648,1649,-1,1650,1651,1652,-1,1653,1654,1655,-1,1656,1657,1658,-1,1659,1660,1661,-1,1662,1663,1664,-1,1665,1666,1667,-1,1668,1669,1670,-1,1671,1672,1673,-1,1674,1675,1676,-1,1677,1678,1679,-1,1680,1681,1682,-1,1683,1684,1685,-1,1686,1687,1688,-1,1689,1690,1691,-1,1692,1693,1694,-1,1695,1696,1697,-1,1698,1699,1700,-1,1701,1702,1703,-1,1704,1705,1706,-1,1707,1708,1709,-1,1710,1711,1712,-1,1713,1714,1715,-1,1716,1717,1718,-1,1719,1720,1721,-1,1722,1723,1724,-1,1725,1726,1727,-1,1728,1729,1730,-1,1731,1732,1733,-1,1734,1735,1736,-1,1737,1738,1739,-1,1740,1741,1742,-1,1743,1744,1745,-1,1746,1747,1748,-1,1749,1750,1751,-1,1752,1753,1754,-1,1755,1756,1757,-1,1758,1759,1760,-1,1761,1762,1763,-1,1764,1765,1766,-1,1767,1768,1769,-1,1770,1771,1772,-1,1773,1774,1775,-1,1776,1777,1778,-1,1779,1780,1781,-1,1782,1783,1784,-1,1785,1786,1787,-1,1788,1789,1790,-1,1791,1792,1793,-1,1794,1795,1796,-1,1797,1798,1799,-1,1800,1801,1802,-1,1803,1804,1805,-1,1806,1807,1808,-1,1809,1810,1811,-1,1812,1813,1814,-1,1815,1816,1817,-1,1818,1819,1820,-1,1821,1822,1823,-1,1824,1825,1826,-1,1827,1828,1829,-1,1830,1831,1832,-1,1833,1834,1835,-1,1836,1837,1838,-1,1839,1840,1841,-1,1842,1843,1844,-1,1845,1846,1847,-1,1848,1849,1850,-1,1851,1852,1853,-1,1854,1855,1856,-1,1857,1858,1859,-1,1860,1861,1862,-1,1863,1864,1865,-1,1866,1867,1868,-1,1869,1870,1871,-1,1872,1873,1874,-1,1875,1876,1877,-1,1878,1879,1880,-1,1881,1882,1883,-1,1884,1885,1886,-1,1887,1888,1889,-1,1890,1891,1892,-1,1893,1894,1895,-1,1896,1897,1898,-1,1899,1900,1901,-1,1902,1903,1904,-1,1905,1906,1907,-1,1908,1909,1910,-1,1911,1912,1913,-1,1914,1915,1916,-1,1917,1918,1919,-1,1920,1921,1922,-1,1923,1924,1925,-1,1926,1927,1928,-1,1929,1930,1931,-1,1932,1933,1934,-1,1935,1936,1937,-1,1938,1939,1940,-1,1941,1942,1943,-1,1944,1945,1946,-1,1947,1948,1949,-1,1950,1951,1952,-1,1953,1954,1955,-1,1956,1957,1958,-1,1959,1960,1961,-1,1962,1963,1964,-1,1965,1966,1967,-1,1968,1969,1970,-1,1971,1972,1973,-1,1974,1975,1976,-1,1977,1978,1979,-1,1980,1981,1982,-1,1983,1984,1985,-1,1986,1987,1988,-1,1989,1990,1991,-1,1992,1993,1994,-1,1995,1996,1997,-1,1998,1999,2000,-1,2001,2002,2003,-1,2004,2005,2006,-1,2007,2008,2009,-1,2010,2011,2012,-1,2013,2014,2015,-1,2016,2017,2018,-1,2019,2020,2021,-1,2022,2023,2024,-1,2025,2026,2027,-1,2028,2029,2030,-1,2031,2032,2033,-1,2034,2035,2036,-1,2037,2038,2039,-1,2040,2041,2042,-1,2043,2044,2045,-1,2046,2047,2048,-1,2049,2050,2051,-1,2052,2053,2054,-1,2055,2056,2057,-1,2058,2059,2060,-1,2061,2062,2063,-1,2064,2065,2066,-1,2067,2068,2069,-1,2070,2071,2072,-1,2073,2074,2075,-1,2076,2077,2078,-1,2079,2080,2081,-1,2082,2083,2084,-1,2085,2086,2087,-1,2088,2089,2090,-1,2091,2092,2093,-1,2094,2095,2096,-1,2097,2098,2099,-1,2100,2101,2102,-1,2103,2104,2105,-1,2106,2107,2108,-1,2109,2110,2111,-1,2112,2113,2114,-1,2115,2116,2117,-1,2118,2119,2120,-1,2121,2122,2123,-1,2124,2125,2126,-1,2127,2128,2129,-1,2130,2131,2132,-1,2133,2134,2135,-1,2136,2137,2138,-1,2139,2140,2141,-1,2142,2143,2144,-1,2145,2146,2147,-1,2148,2149,2150,-1,2151,2152,2153,-1,2154,2155,2156,-1,2157,2158,2159,-1,2160,2161,2162,-1,2163,2164,2165,-1,2166,2167,2168,-1,2169,2170,2171,-1,2172,2173,2174,-1,2175,2176,2177,-1,2178,2179,2180,-1,2181,2182,2183,-1,2184,2185,2186,-1,2187,2188,2189,-1,2190,2191,2192,-1,2193,2194,2195,-1,2196,2197,2198,-1,2199,2200,2201,-1,2202,2203,2204,-1,2205,2206,2207,-1,2208,2209,2210,-1,2211,2212,2213,-1,2214,2215,2216,-1,2217,2218,2219,-1,2220,2221,2222,-1,2223,2224,2225,-1,2226,2227,2228,-1,2229,2230,2231,-1,2232,2233,2234,-1,2235,2236,2237,-1,2238,2239,2240,-1,2241,2242,2243,-1,2244,2245,2246,-1,2247,2248,2249,-1,2250,2251,2252,-1,2253,2254,2255,-1,2256,2257,2258,-1,2259,2260,2261,-1,2262,2263,2264,-1,2265,2266,2267,-1,2268,2269,2270,-1,2271,2272,2273,-1,2274,2275,2276,-1,2277,2278,2279,-1,2280,2281,2282,-1,2283,2284,2285,-1,2286,2287,2288,-1,2289,2290,2291,-1,2292,2293,2294,-1,2295,2296,2297,-1,2298,2299,2300,-1,2301,2302,2303,-1,2304,2305,2306,-1,2307,2308,2309,-1,2310,2311,2312,-1,2313,2314,2315,-1,2316,2317,2318,-1,2319,2320,2321,-1,2322,2323,2324,-1,2325,2326,2327,-1,2328,2329,2330,-1,2331,2332,2333,-1,2334,2335,2336,-1,2337,2338,2339,-1,2340,2341,2342,-1,2343,2344,2345,-1,2346,2347,2348,-1,2349,2350,2351,-1,2352,2353,2354,-1,2355,2356,2357,-1,2358,2359,2360,-1,2361,2362,2363,-1,2364,2365,2366,-1,2367,2368,2369,-1,2370,2371,2372,-1,2373,2374,2375,-1,2376,2377,2378,-1,2379,2380,2381,-1,2382,2383,2384,-1,2385,2386,2387,-1,2388,2389,2390,-1,2391,2392,2393,-1,2394,2395,2396,-1,2397,2398,2399,-1,2400,2401,2402,-1,2403,2404,2405,-1,2406,2407,2408,-1,2409,2410,2411,-1,2412,2413,2414,-1,2415,2416,2417,-1,2418,2419,2420,-1,2421,2422,2423,-1,2424,2425,2426,-1,2427,2428,2429,-1,2430,2431,2432,-1,2433,2434,2435,-1,2436,2437,2438,-1,2439,2440,2441,-1,2442,2443,2444,-1,2445,2446,2447,-1,2448,2449,2450,-1,2451,2452,2453,-1,2454,2455,2456,-1,2457,2458,2459,-1,2460,2461,2462,-1,2463,2464,2465,-1,2466,2467,2468,-1,2469,2470,2471,-1,2472,2473,2474,-1,2475,2476,2477,-1,2478,2479,2480,-1,2481,2482,2483,-1,2484,2485,2486,-1,2487,2488,2489,-1,2490,2491,2492,-1,2493,2494,2495,-1,2496,2497,2498,-1,2499,2500,2501,-1,2502,2503,2504,-1,2505,2506,2507,-1,2508,2509,2510,-1,2511,2512,2513,-1,2514,2515,2516,-1,2517,2518,2519,-1,2520,2521,2522,-1,2523,2524,2525,-1,2526,2527,2528,-1,2529,2530,2531,-1,2532,2533,2534,-1,2535,2536,2537,-1,2538,2539,2540,-1,2541,2542,2543,-1,2544,2545,2546,-1,2547,2548,2549,-1,2550,2551,2552,-1,2553,2554,2555,-1,2556,2557,2558,-1,2559,2560,2561,-1,2562,2563,2564,-1,2565,2566,2567,-1,2568,2569,2570,-1,2571,2572,2573,-1,2574,2575,2576,-1,2577,2578,2579,-1,2580,2581,2582,-1,2583,2584,2585,-1,2586,2587,2588,-1,2589,2590,2591,-1,2592,2593,2594,-1,2595,2596,2597,-1,2598,2599,2600,-1,2601,2602,2603,-1,2604,2605,2606,-1,2607,2608,2609,-1,2610,2611,2612,-1,2613,2614,2615,-1,2616,2617,2618,-1,2619,2620,2621,-1,2622,2623,2624,-1,2625,2626,2627,-1,2628,2629,2630,-1,2631,2632,2633,-1,2634,2635,2636,-1,2637,2638,2639,-1,2640,2641,2642,-1,2643,2644,2645,-1,2646,2647,2648,-1,2649,2650,2651,-1,2652,2653,2654,-1,2655,2656,2657,-1,2658,2659,2660,-1,2661,2662,2663,-1,2664,2665,2666,-1,2667,2668,2669,-1,2670,2671,2672,-1,2673,2674,2675,-1,2676,2677,2678,-1,2679,2680,2681,-1,2682,2683,2684,-1,2685,2686,2687,-1,2688,2689,2690,-1,2691,2692,2693,-1,2694,2695,2696,-1,2697,2698,2699,-1,2700,2701,2702,-1,2703,2704,2705,-1,2706,2707,2708,-1,2709,2710,2711,-1,2712,2713,2714,-1,2715,2716,2717,-1,2718,2719,2720,-1,2721,2722,2723,-1,2724,2725,2726,-1,2727,2728,2729,-1,2730,2731,2732,-1,2733,2734,2735,-1,2736,2737,2738,-1,2739,2740,2741,-1,2742,2743,2744,-1,2745,2746,2747,-1,2748,2749,2750,-1,2751,2752,2753,-1,2754,2755,2756,-1,2757,2758,2759,-1,2760,2761,2762,-1,2763,2764,2765,-1,2766,2767,2768,-1,2769,2770,2771,-1,2772,2773,2774,-1,2775,2776,2777,-1,2778,2779,2780,-1,2781,2782,2783,-1,2784,2785,2786,-1,2787,2788,2789,-1,2790,2791,2792,-1,2793,2794,2795,-1,2796,2797,2798,-1,2799,2800,2801,-1,2802,2803,2804,-1,2805,2806,2807,-1,2808,2809,2810,-1,2811,2812,2813,-1,2814,2815,2816,-1,2817,2818,2819,-1,2820,2821,2822,-1,2823,2824,2825,-1,2826,2827,2828,-1,2829,2830,2831,-1,2832,2833,2834,-1,2835,2836,2837,-1,2838,2839,2840,-1,2841,2842,2843,-1,2844,2845,2846,-1,2847,2848,2849,-1,2850,2851,2852,-1,2853,2854,2855,-1,2856,2857,2858,-1,2859,2860,2861,-1,2862,2863,2864,-1,2865,2866,2867,-1,2868,2869,2870,-1,2871,2872,2873,-1,2874,2875,2876,-1,2877,2878,2879,-1,2880,2881,2882,-1,2883,2884,2885,-1,2886,2887,2888,-1,2889,2890,2891,-1,2892,2893,2894,-1,2895,2896,2897,-1,2898,2899,2900,-1,2901,2902,2903,-1,2904,2905,2906,-1,2907,2908,2909,-1,2910,2911,2912,-1,2913,2914,2915,-1,2916,2917,2918,-1,2919,2920,2921,-1,2922,2923,2924,-1,2925,2926,2927,-1,2928,2929,2930,-1,2931,2932,2933,-1,2934,2935,2936,-1,2937,2938,2939,-1,2940,2941,2942,-1,2943,2944,2945,-1,2946,2947,2948,-1,2949,2950,2951,-1,2952,2953,2954,-1,2955,2956,2957,-1,2958,2959,2960,-1,2961,2962,2963,-1,2964,2965,2966,-1,2967,2968,2969,-1,2970,2971,2972,-1,2973,2974,2975,-1,2976,2977,2978,-1,2979,2980,2981,-1,2982,2983,2984,-1,2985,2986,2987,-1,2988,2989,2990,-1,2991,2992,2993,-1,2994,2995,2996,-1,2997,2998,2999,-1])
IndexedFaceSet310.setCreaseAngle(1.14)
Coordinate311 = Coordinate()
Coordinate311.setPoint([-0.9,-0.99,8.13,-0.89,-0.79,8.34,-0.82,-0.51,8.11,-0.91,-0.43,7.52,-0.93,-0.39,7.31,-0.98,-0.87,7.35,-0.71,-0.51,8.52,-0.78,-0.63,8.53,-0.68,-0.55,8.64,-0.62,-0.67,6.28,-0.72,-0.63,6.28,-0.61,-0.59,6.29,-0.71,-0.51,6.33,-0.73,-0.59,6.3,-0.72,-0.63,6.4,-0.71,-0.51,6.33,-0.72,-0.63,6.4,-0.68,-0.59,6.46,0.12,-0.71,9.4,0.27,-0.71,9.37,0.17,-0.51,9.33,-0.28,-0.59,9.24,-0.27,-0.63,9.19,-0.18,-0.67,9.25,-0.18,-0.67,9.25,-0.08,-0.63,9.32,-0.23,-0.51,9.42,-0.82,-0.55,6.9,-0.83,-0.67,6.89,-0.87,-0.75,7.08,-0.8,-0.59,6.83,-0.81,-0.59,6.86,-0.81,-0.55,6.87,-0.69,-0.79,6.54,-0.68,-0.59,6.46,-0.72,-0.63,6.4,-0.72,-0.63,6.28,-0.73,-0.59,6.3,-0.61,-0.59,6.29,1.75,-0.75,8.42,1.72,-0.55,8.51,1.47,-0.87,8.85,-0.38,-0.55,9.16,-0.35,-0.67,9.14,-0.29,-0.59,9.18,-0.63,-0.79,8.86,-0.61,-0.55,8.85,-0.67,-0.67,8.67,-0.67,-0.67,8.67,-0.61,-0.55,8.85,-0.68,-0.55,8.64,-0.93,-0.39,7.31,-0.83,-0.47,7.12,-0.98,-0.87,7.35,-0.87,-0.75,7.08,-0.83,-0.67,6.89,-0.83,-0.75,6.89,-0.81,-0.55,6.87,-0.81,-0.59,6.86,-0.82,-0.55,6.9,-0.7,-0.67,6.65,-0.82,-0.67,6.86,-0.8,-0.59,6.83,-0.72,-0.63,6.28,-0.62,-0.67,6.28,-0.74,-0.71,6.26,-0.01,-0.63,5.62,0.03,-0.59,5.61,0.1,-0.63,5.56,-0.14,-0.83,9.33,-0.18,-0.67,9.25,-0.29,-0.75,9.18,-0.27,-0.63,9.19,-0.35,-0.67,9.14,-0.29,-0.75,9.18,-0.29,-0.59,9.18,-0.27,-0.63,9.19,-0.28,-0.59,9.24,-0.47,-0.63,9.12,-0.35,-0.67,9.14,-0.38,-0.55,9.16,-0.44,-0.55,9.1,-0.47,-0.63,9.12,-0.38,-0.55,9.16,-0.67,-0.67,8.67,-0.78,-0.63,8.53,-0.83,-0.79,8.63,-0.67,-0.67,8.67,-0.68,-0.55,8.64,-0.78,-0.63,8.53,-0.9,-0.59,8.5,-0.91,-0.67,8.54,-0.78,-0.63,8.53,-0.92,-0.75,8.55,-0.91,-0.67,8.54,-0.89,-0.79,8.34,-0.56,-0.55,6.14,-0.62,-0.67,6.28,-0.61,-0.59,6.29,-0.51,-0.59,5.95,-0.42,-0.63,5.94,-0.54,-0.63,6.07,-0.47,-0.59,5.78,-0.45,-0.59,5.76,-0.37,-0.63,5.82,-0.17,-0.63,5.68,-0.23,-0.59,5.59,-0.15,-0.59,5.58,-0.01,-0.63,5.62,-0.06,-0.63,5.62,-0.03,-0.59,5.6,0.42,-0.63,5.47,0.38,-0.75,5.48,0.31,-0.63,5.5,1.1,-0.63,5.73,1,-0.99,5.59,0.82,-0.71,5.55,1.79,-0.75,7.92,1.79,-0.75,7.77,1.82,-0.63,7.83,1.26,-0.71,9.02,1.22,-0.67,9.03,1.12,-0.79,9.1,1.05,-1.07,9.16,1.15,-0.95,9.09,0.91,-0.83,9.2,0.46,-0.63,9.34,0.54,-0.71,9.36,0.58,-0.67,9.35,0.46,-0.75,9.38,0.54,-0.71,9.36,0.46,-0.63,9.34,-0.18,-0.67,9.25,-0.27,-0.63,9.19,-0.29,-0.75,9.18,-0.35,-0.67,9.14,-0.27,-0.63,9.19,-0.29,-0.59,9.18,-0.35,-0.67,9.14,-0.46,-0.75,9.18,-0.29,-0.75,9.18,-0.55,-0.51,8.95,-0.61,-0.55,8.85,-0.63,-0.79,8.86,-0.92,-0.79,8.59,-0.92,-0.75,8.55,-0.89,-0.91,8.46,-0.83,-0.47,7.12,-0.87,-0.75,7.08,-0.98,-0.87,7.35,-0.82,-0.67,6.86,-0.83,-0.67,6.89,-0.81,-0.59,6.86,-0.74,-0.71,6.26,-0.73,-0.75,6.38,-0.72,-0.63,6.4,-0.73,-0.59,6.3,-0.72,-0.63,6.28,-0.72,-0.63,6.4,-0.72,-0.63,6.28,-0.74,-0.71,6.26,-0.72,-0.63,6.4,-0.42,-0.63,5.94,-0.34,-0.91,5.86,-0.54,-0.63,6.07,-0.42,-0.63,5.94,-0.37,-0.63,5.82,-0.34,-0.91,5.86,-0.22,-0.63,5.71,-0.21,-0.67,5.77,-0.21,-0.63,5.8,-0.22,-0.63,5.71,-0.17,-0.63,5.68,-0.21,-0.67,5.77,-0.15,-0.59,5.58,-0.06,-0.63,5.62,-0.17,-0.63,5.68,-0.18,-0.87,5.68,-0.21,-0.67,5.77,-0.17,-0.63,5.68,-0.01,-0.63,5.62,0.1,-0.63,5.56,-0.03,-0.75,5.56,0.42,-0.63,5.47,0.53,-0.63,5.53,0.46,-0.67,5.46,0.58,-0.67,5.53,0.46,-0.67,5.46,0.53,-0.63,5.53,0.53,-0.63,5.53,0.64,-0.63,5.58,0.58,-0.67,5.53,0.67,-0.67,5.57,0.58,-0.67,5.53,0.64,-0.63,5.58,0.12,-0.71,9.4,0.17,-0.75,9.4,0.27,-0.71,9.37,-0.18,-0.67,9.25,-0.23,-0.51,9.42,-0.28,-0.59,9.24,-0.46,-0.75,9.18,-0.47,-0.63,9.12,-0.63,-0.79,8.86,-0.47,-0.63,9.12,-0.55,-0.51,8.95,-0.63,-0.79,8.86,-0.82,-0.67,6.86,-0.81,-0.59,6.86,-0.8,-0.59,6.83,-0.7,-0.67,6.65,-0.8,-0.59,6.83,-0.77,-0.43,6.78,-0.69,-0.79,6.54,-0.7,-0.67,6.65,-0.68,-0.59,6.46,-0.73,-0.79,6.23,-0.74,-0.71,6.26,-0.62,-0.67,6.28,-0.46,-0.99,6.02,-0.76,-0.99,6.17,-0.64,-0.83,6.23,-0.06,-0.63,5.62,-0.01,-0.63,5.62,-0.03,-0.75,5.56,0.62,-0.75,5.52,0.67,-0.67,5.57,0.82,-0.71,5.55,0.62,-0.75,5.52,0.58,-0.71,5.52,0.67,-0.67,5.57,1.55,-0.63,6.11,1.56,-1.11,6,1.38,-0.75,5.9,1.73,-0.63,6.36,1.75,-0.87,6.34,1.55,-0.63,6.11,1.73,-0.63,6.36,1.78,-0.67,6.43,1.75,-0.87,6.34,1.75,-0.87,6.34,1.78,-0.67,6.43,1.85,-0.67,6.69,1.76,-0.87,7.4,1.86,-0.67,7.33,1.81,-0.67,7.54,1.22,-0.67,9.03,1.26,-0.71,9.02,1.28,-0.67,9,0.91,-0.83,9.2,0.8,-0.47,9.23,0.66,-0.67,9.3,0.46,-0.75,9.38,0.27,-0.71,9.37,0.35,-0.83,9.35,0.46,-0.63,9.34,0.35,-0.59,9.35,0.27,-0.71,9.37,0,-0.51,9.38,-0.08,-0.63,9.32,0.12,-0.71,9.4,-0.08,-0.63,9.32,-0.18,-0.67,9.25,-0.14,-0.83,9.33,-0.89,-0.79,8.34,-0.9,-0.59,8.5,-0.82,-0.51,8.11,-0.91,-0.43,7.52,-1,-0.79,7.55,-0.91,-0.51,7.85,-0.83,-0.67,6.89,-0.82,-0.67,6.86,-0.83,-0.75,6.89,-0.29,-0.63,5.77,-0.21,-0.63,5.8,-0.21,-0.67,5.77,-0.37,-0.63,5.82,-0.29,-0.63,5.77,-0.34,-0.91,5.86,0.31,-0.63,5.5,0.14,-0.79,5.51,0.1,-0.63,5.56,0.42,-0.63,5.47,0.46,-0.67,5.46,0.38,-0.75,5.48,0.58,-0.71,5.52,0.51,-0.75,5.47,0.46,-0.67,5.46,0.62,-0.75,5.52,0.51,-0.75,5.47,0.58,-0.71,5.52,0.52,-0.83,5.47,0.61,-0.83,5.51,0.55,-1.19,5.5,0.61,-0.83,5.51,0.72,-1.19,5.49,0.55,-1.19,5.5,0.58,-0.71,5.52,0.58,-0.67,5.53,0.67,-0.67,5.57,0.61,-0.83,5.51,0.62,-0.75,5.52,0.82,-0.71,5.55,1.86,-1.07,7.02,1.76,-1.35,6.7,1.76,-1.07,6.37,1.85,-0.67,6.69,1.9,-0.79,6.78,1.76,-1.07,6.37,1.76,-0.87,7.4,1.92,-0.71,7.28,1.86,-0.67,7.33,1.82,-0.67,8.08,1.75,-0.75,8.42,1.73,-1.11,7.96,1.34,-0.75,8.97,1.47,-0.87,8.85,1.51,-0.47,8.8,0.66,-0.67,9.3,0.58,-0.75,9.35,0.64,-0.83,9.29,0.66,-0.67,9.3,0.58,-0.67,9.35,0.58,-0.75,9.35,0.54,-0.71,9.36,0.58,-0.75,9.35,0.58,-0.67,9.35,0.46,-0.75,9.38,0.46,-0.63,9.34,0.27,-0.71,9.37,0.27,-0.95,9.41,0.23,-0.91,9.38,0.1,-0.95,9.42,-0.74,-1.39,9.02,-0.79,-1.55,8.98,-0.46,-1.55,9.29,-0.46,-0.75,9.18,-0.42,-0.91,9.27,-0.29,-0.75,9.18,-0.92,-0.75,8.55,-0.92,-0.79,8.59,-0.83,-0.79,8.63,-0.67,-0.67,8.67,-0.83,-0.79,8.63,-0.68,-0.95,8.75,-0.92,-0.79,8.59,-0.86,-0.91,8.7,-0.83,-0.79,8.63,-0.85,-1.23,8.84,-0.9,-1.03,8.68,-0.87,-1.15,8.41,-1,-0.79,7.55,-0.91,-0.43,7.52,-0.98,-0.87,7.35,-0.82,-0.55,6.9,-0.81,-0.59,6.86,-0.83,-0.67,6.89,-0.7,-0.67,6.65,-0.76,-0.87,6.75,-0.82,-0.67,6.86,-0.74,-0.71,6.26,-0.73,-0.79,6.23,-0.73,-0.75,6.38,-0.18,-0.87,5.68,-0.34,-0.91,5.86,-0.21,-0.67,5.77,0.31,-0.63,5.5,0.38,-0.75,5.48,0.14,-0.79,5.51,0.04,-0.95,5.62,0.14,-0.79,5.51,0.39,-0.87,5.49,0.67,-0.67,5.57,0.73,-0.59,5.58,0.82,-0.71,5.55,1.75,-0.87,6.34,1.85,-0.67,6.69,1.76,-1.07,6.37,1.86,-0.71,6.78,1.9,-0.79,6.78,1.85,-0.67,6.69,1.92,-0.79,6.91,1.9,-0.79,6.78,1.86,-0.71,6.78,1.91,-0.71,7.18,1.86,-1.07,7.02,1.9,-0.71,7,1.28,-0.67,9,1.26,-0.71,9.02,1.34,-0.75,8.97,0.51,-0.83,9.38,0.54,-0.83,9.36,0.54,-0.79,9.36,0.44,-0.83,9.39,0.46,-0.75,9.38,0.35,-0.83,9.35,0.11,-0.79,9.4,0.17,-0.75,9.4,0.12,-0.71,9.4,0.24,-0.83,9.39,0.17,-0.75,9.4,0.11,-0.79,9.4,-0.78,-0.63,8.53,-0.91,-0.67,8.54,-0.83,-0.79,8.63,-0.91,-0.67,8.54,-0.9,-0.59,8.5,-0.89,-0.79,8.34,-0.92,-0.75,8.55,-0.89,-0.79,8.34,-0.89,-0.91,8.46,-0.76,-0.87,6.75,-0.83,-0.75,6.89,-0.82,-0.67,6.86,-0.69,-0.79,6.54,-0.72,-0.63,6.4,-0.73,-0.75,6.38,-0.69,-0.79,6.54,-0.78,-0.95,6.27,-0.72,-1.19,6.51,-0.73,-0.79,6.23,-0.77,-0.83,6.24,-0.73,-0.75,6.38,-0.64,-0.83,6.23,-0.73,-0.79,6.23,-0.62,-0.67,6.28,-0.46,-0.99,6.02,-0.64,-0.83,6.23,-0.54,-0.63,6.07,-0.18,-0.87,5.68,-0.03,-0.75,5.56,0.04,-0.95,5.62,0.03,-1.11,5.57,0.04,-0.95,5.62,0.39,-0.87,5.49,1.9,-0.71,7,1.92,-0.79,6.91,1.86,-0.71,6.78,1.75,-0.75,8.42,1.72,-0.91,8.46,1.73,-1.11,7.96,1.26,-0.71,9.02,1.12,-0.79,9.1,1.15,-0.95,9.09,0.91,-0.83,9.2,1.12,-0.79,9.1,0.8,-0.47,9.23,0.64,-0.95,9.29,0.64,-0.83,9.29,0.52,-0.95,9.34,0.54,-0.71,9.36,0.55,-0.75,9.36,0.58,-0.75,9.35,0.51,-0.83,9.38,0.54,-0.79,9.36,0.46,-0.75,9.38,0.51,-0.83,9.38,0.46,-0.75,9.38,0.44,-0.83,9.39,0.41,-0.87,9.38,0.44,-0.83,9.39,0.35,-0.83,9.35,0.26,-0.79,9.38,0.35,-0.83,9.35,0.27,-0.71,9.37,0.24,-0.83,9.39,0.35,-0.83,9.35,0.26,-0.79,9.38,0.24,-0.83,9.39,0.26,-0.79,9.38,0.17,-0.75,9.4,0.1,-0.95,9.42,0.23,-0.91,9.38,0.11,-0.79,9.4,0.23,-0.91,9.38,0.24,-0.83,9.39,0.11,-0.79,9.4,0.41,-0.87,9.38,0.35,-0.83,9.35,0.35,-0.87,9.35,-0.89,-0.91,8.46,-0.89,-0.79,8.34,-0.9,-0.99,8.13,-0.76,-0.99,6.17,-0.78,-0.95,6.27,-0.64,-0.83,6.23,-0.77,-1.23,6.2,-0.76,-0.99,6.17,-0.46,-0.99,6.02,0.03,-1.11,5.57,-0.19,-1.15,5.7,-0.14,-1.03,5.66,0.51,-0.75,5.47,0.38,-0.75,5.48,0.46,-0.67,5.46,0.51,-0.75,5.47,0.39,-0.87,5.49,0.38,-0.75,5.48,0.52,-0.83,5.47,0.39,-0.87,5.49,0.51,-0.75,5.47,1.75,-0.87,6.34,1.56,-1.11,6,1.55,-0.63,6.11,1.7,-1.23,8.17,1.69,-1.27,8.1,1.73,-1.11,7.96,0.54,-0.79,9.36,0.64,-0.83,9.29,0.58,-0.75,9.35,0.48,-0.87,9.39,0.51,-0.87,9.37,0.51,-0.83,9.38,-0.08,-0.63,9.32,0.11,-0.79,9.4,0.12,-0.71,9.4,-0.35,-0.67,9.14,-0.47,-0.63,9.12,-0.46,-0.75,9.18,-0.42,-0.91,9.27,-0.46,-0.75,9.18,-0.63,-0.79,8.86,-0.63,-0.79,8.86,-0.67,-0.67,8.67,-0.68,-0.95,8.75,-0.9,-0.99,8.13,-1.03,-1.07,7.74,-1.02,-1.31,8.02,-0.82,-0.55,6.9,-0.87,-0.75,7.08,-0.83,-0.47,7.12,-0.76,-0.87,6.75,-0.9,-1.19,7.18,-0.83,-0.75,6.89,-0.74,-1.11,6.69,-0.76,-0.87,6.75,-0.69,-0.79,6.54,-0.69,-0.79,6.54,-0.73,-0.75,6.38,-0.78,-0.95,6.27,-0.77,-0.83,6.24,-0.73,-0.79,6.23,-0.64,-0.83,6.23,-0.64,-0.83,6.23,-0.62,-0.67,6.28,-0.54,-0.63,6.07,-0.56,-0.55,6.14,-0.54,-0.63,6.07,-0.62,-0.67,6.28,-0.31,-1.11,5.8,-0.23,-1.27,5.75,-0.52,-1.55,5.94,0.14,-0.79,5.51,-0.03,-0.75,5.56,0.1,-0.63,5.56,0.14,-0.79,5.51,0.38,-0.75,5.48,0.39,-0.87,5.49,1.83,-0.99,7.3,1.86,-1.07,7.02,1.91,-0.71,7.18,1.78,-0.99,7.36,1.83,-0.99,7.3,1.76,-0.87,7.4,1.71,-0.95,7.51,1.81,-0.67,7.54,1.79,-0.75,7.77,1.71,-0.95,7.51,1.76,-0.87,7.4,1.81,-0.67,7.54,1.79,-0.75,7.77,1.79,-0.75,7.92,1.69,-0.99,7.7,1.75,-0.75,8.42,1.47,-0.87,8.85,1.72,-0.91,8.46,1.15,-0.95,9.09,1.12,-0.79,9.1,0.91,-0.83,9.2,0.64,-0.83,9.29,0.54,-0.83,9.36,0.52,-0.95,9.34,0.51,-0.87,9.37,0.54,-0.83,9.36,0.51,-0.83,9.38,0.44,-0.95,9.44,0.39,-0.91,9.47,0.41,-0.87,9.38,0.44,-0.83,9.39,0.41,-0.87,9.38,0.39,-0.91,9.47,0.44,-0.95,9.44,0.41,-0.87,9.38,0.35,-0.95,9.39,0.35,-0.95,9.39,0.31,-1.03,9.41,0.42,-1.03,9.45,0.1,-0.95,9.42,0.11,-0.79,9.4,-0.14,-0.83,9.33,-0.08,-0.63,9.32,-0.14,-0.83,9.33,0.11,-0.79,9.4,-0.91,-0.67,8.54,-0.92,-0.75,8.55,-0.83,-0.79,8.63,-0.91,-0.51,7.85,-1,-0.79,7.55,-1.03,-1.07,7.74,-0.91,-0.51,7.85,-1.03,-1.07,7.74,-0.9,-0.99,8.13,-0.74,-1.11,6.69,-0.69,-0.79,6.54,-0.72,-1.19,6.51,-0.76,-0.87,6.75,-0.7,-0.67,6.65,-0.69,-0.79,6.54,-0.18,-1.23,5.71,-0.19,-1.15,5.7,0.03,-1.11,5.57,-0.29,-0.63,5.77,-0.21,-0.67,5.77,-0.34,-0.91,5.86,0.03,-1.11,5.57,-0.14,-1.03,5.66,0.04,-0.95,5.62,0.52,-0.83,5.47,0.55,-1.19,5.5,0.39,-0.87,5.49,1.1,-0.63,5.73,1.38,-0.75,5.9,1,-0.99,5.59,1.36,-1.27,5.77,1.38,-0.75,5.9,1.56,-1.11,6,1,-0.99,5.59,1.06,-1.23,5.58,0.83,-1.15,5.55,1.83,-0.99,7.3,1.91,-0.71,7.18,1.92,-0.71,7.28,1.72,-0.91,8.46,1.7,-1.23,8.17,1.73,-1.11,7.96,1.19,-1.27,9.12,1.29,-1.43,9.01,1.44,-1.27,8.86,1.34,-0.75,8.97,1.26,-0.71,9.02,1.15,-0.95,9.09,0.64,-0.83,9.29,0.64,-0.95,9.29,0.91,-0.83,9.2,0.54,-0.83,9.36,0.51,-0.87,9.37,0.52,-0.95,9.34,0.54,-0.79,9.36,0.54,-0.83,9.36,0.64,-0.83,9.29,-0.83,-0.79,8.63,-0.86,-0.91,8.7,-0.68,-0.95,8.75,-0.91,-0.51,7.85,-0.9,-0.99,8.13,-0.82,-0.51,8.11,-0.9,-1.19,7.18,-0.78,-1.39,7.4,-0.97,-1.11,7.43,-0.78,-0.95,6.27,-0.77,-0.83,6.24,-0.64,-0.83,6.23,-0.31,-1.11,5.8,-0.46,-0.99,6.02,-0.34,-0.91,5.86,-0.22,-1.11,5.72,-0.34,-0.91,5.86,-0.14,-1.03,5.66,0.61,-0.83,5.51,0.83,-1.15,5.55,0.72,-1.19,5.49,1.86,-1.07,7.02,1.71,-1.47,6.87,1.76,-1.35,6.7,1.68,-0.99,7.46,1.78,-0.99,7.36,1.76,-0.87,7.4,1.71,-0.95,7.51,1.68,-0.99,7.46,1.76,-0.87,7.4,1.69,-0.99,7.7,1.71,-0.95,7.51,1.79,-0.75,7.77,0.92,-1.15,9.2,0.91,-0.83,9.2,0.64,-0.95,9.29,0.64,-0.83,9.29,0.91,-0.83,9.2,0.66,-0.67,9.3,0.51,-0.87,9.37,0.5,-0.95,9.36,0.52,-0.95,9.34,0.52,-0.95,9.34,0.52,-0.99,9.34,0.64,-0.95,9.29,0.52,-0.99,9.34,0.44,-0.95,9.44,0.42,-1.03,9.45,0.35,-0.95,9.39,0.27,-0.95,9.41,0.31,-1.03,9.41,0.24,-1.23,9.43,0.31,-1.03,9.41,0.1,-0.95,9.42,0.44,-0.95,9.44,0.35,-0.95,9.39,0.42,-1.03,9.45,-0.89,-0.91,8.46,-0.9,-1.03,8.68,-0.86,-0.91,8.7,-1,-0.79,7.55,-0.98,-0.87,7.35,-0.97,-1.11,7.43,-0.9,-1.19,7.18,-0.97,-1.11,7.43,-0.98,-0.87,7.35,-0.31,-1.11,5.8,-0.52,-1.55,5.94,-0.62,-1.47,6.01,0.14,-0.79,5.51,0.04,-0.95,5.62,-0.03,-0.75,5.56,0.61,-0.83,5.51,1,-0.99,5.59,0.83,-1.15,5.55,0.61,-0.83,5.51,0.82,-0.71,5.55,1,-0.99,5.59,1.66,-1.03,7.5,1.68,-0.99,7.46,1.71,-0.95,7.51,1.66,-1.03,7.5,1.71,-0.95,7.51,1.69,-0.99,7.7,1.47,-0.87,8.85,1.47,-1.07,8.84,1.72,-0.91,8.46,0.92,-1.15,9.2,1.05,-1.07,9.16,0.91,-0.83,9.2,0.92,-1.15,9.2,1.02,-1.19,9.18,1.05,-1.07,9.16,0.59,-1.15,9.32,0.64,-0.95,9.29,0.52,-0.99,9.34,0.52,-0.99,9.34,0.42,-1.03,9.45,0.42,-1.07,9.4,-0.14,-0.83,9.33,-0.29,-0.75,9.18,-0.42,-0.91,9.27,-0.01,-1.03,9.38,-0.14,-0.83,9.33,-0.12,-1.07,9.38,-0.87,-0.75,7.08,-0.9,-1.19,7.18,-0.98,-0.87,7.35,-0.72,-1.19,6.51,-0.75,-1.43,6.64,-0.74,-1.11,6.69,-0.78,-0.95,6.27,-0.73,-0.75,6.38,-0.77,-0.83,6.24,-0.18,-0.87,5.68,-0.06,-0.63,5.62,-0.03,-0.75,5.56,1.9,-0.79,6.78,1.86,-1.07,7.02,1.76,-1.07,6.37,1.76,-0.87,7.4,1.83,-0.99,7.3,1.92,-0.71,7.28,1.78,-0.99,7.36,1.76,-1.03,7.38,1.83,-0.99,7.3,1.86,-1.07,7.02,1.92,-0.79,6.91,1.9,-0.71,7,1.52,-1.35,7.64,1.49,-1.27,7.5,1.69,-0.99,7.7,0.42,-1.07,9.4,0.42,-1.03,9.45,0.31,-1.03,9.41,0.4,-1.11,9.43,0.46,-1.23,9.37,0.49,-1.15,9.35,0.31,-1.03,9.41,0.27,-0.95,9.41,0.1,-0.95,9.42,0.4,-1.11,9.43,0.42,-1.07,9.4,0.31,-1.03,9.41,-0.01,-1.03,9.38,0.1,-0.95,9.42,-0.14,-0.83,9.33,0,-1.11,9.38,0.07,-1.39,9.47,0.15,-1.35,9.43,-0.9,-1.03,8.68,-0.85,-1.23,8.84,-0.68,-0.95,8.75,-0.89,-0.91,8.46,-0.87,-1.15,8.41,-0.9,-1.03,8.68,-0.78,-0.95,6.27,-0.77,-1.23,6.2,-0.72,-1.19,6.51,-0.46,-0.99,6.02,-0.54,-0.63,6.07,-0.34,-0.91,5.86,1.36,-1.27,5.77,1.56,-1.11,6,1.53,-1.47,5.95,1.83,-0.99,7.3,1.72,-1.23,7.29,1.86,-1.07,7.02,1.49,-1.27,7.5,1.66,-1.03,7.5,1.69,-0.99,7.7,1.49,-1.27,7.5,1.72,-1.23,7.29,1.66,-1.03,7.5,1.79,-0.75,7.92,1.82,-0.67,8.08,1.73,-1.11,7.96,1.47,-1.07,8.84,1.55,-1.19,8.72,1.72,-0.91,8.46,1.06,-1.19,9.16,1.09,-1.23,9.16,1.18,-1.15,9.11,0.48,-1.11,9.35,0.59,-1.15,9.32,0.52,-0.99,9.34,0.42,-1.07,9.4,0.42,-1.11,9.38,0.48,-1.11,9.35,0,-1.11,9.38,0.24,-1.23,9.43,0.1,-0.95,9.42,-0.01,-1.03,9.38,0,-1.11,9.38,0.1,-0.95,9.42,-0.42,-1.35,9.3,-0.2,-1.63,9.4,-0.08,-1.55,9.51,-0.46,-1.11,9.26,-0.42,-0.91,9.27,-0.63,-0.79,8.86,-0.86,-0.91,8.7,-0.9,-1.03,8.68,-0.68,-0.95,8.75,-0.92,-0.79,8.59,-0.89,-0.91,8.46,-0.86,-0.91,8.7,-0.86,-1.59,8.69,-0.85,-1.47,8.83,-0.87,-1.15,8.41,-0.89,-0.91,8.46,-0.9,-0.99,8.13,-0.87,-1.15,8.41,-0.87,-1.15,8.41,-0.9,-0.99,8.13,-1.02,-1.31,8.02,-1.01,-1.55,7.99,-1.02,-1.31,8.02,-0.93,-1.39,7.62,-0.97,-1.11,7.43,-0.78,-1.39,7.4,-0.93,-1.39,7.62,-0.18,-0.87,5.68,-0.17,-0.63,5.68,-0.06,-0.63,5.62,-0.34,-0.91,5.86,-0.18,-0.87,5.68,-0.14,-1.03,5.66,-0.19,-1.15,5.7,-0.22,-1.15,5.72,-0.22,-1.11,5.72,-0.18,-1.23,5.71,0.03,-1.11,5.57,-0.12,-1.47,5.64,1.72,-1.23,7.29,1.76,-1.03,7.38,1.66,-1.03,7.5,1.18,-1.15,9.11,1.09,-1.23,9.16,1.19,-1.27,9.12,1.02,-1.19,9.18,1.06,-1.19,9.16,1.05,-1.07,9.16,1.05,-1.07,9.16,1.06,-1.19,9.16,1.18,-1.15,9.11,1.02,-1.31,9.21,0.92,-1.15,9.2,0.73,-1.47,9.36,0.48,-1.11,9.35,0.52,-0.99,9.34,0.42,-1.07,9.4,0.4,-1.11,9.43,0.34,-1.19,9.39,0.46,-1.23,9.37,0.34,-1.19,9.39,0.4,-1.11,9.43,0.31,-1.03,9.41,1.83,-0.99,7.3,1.76,-1.03,7.38,1.72,-1.23,7.29,1.79,-0.75,7.92,1.73,-1.11,7.96,1.69,-0.99,7.7,1.7,-1.23,8.17,1.67,-1.31,8.19,1.69,-1.27,8.1,1.44,-1.71,8.24,1.58,-1.47,8.1,1.51,-1.63,8.52,1.67,-1.31,8.19,1.7,-1.23,8.17,1.65,-1.19,8.48,1.18,-1.15,9.11,1.19,-1.27,9.12,1.44,-1.27,8.86,1.44,-1.27,8.86,1.29,-1.43,9.01,1.47,-1.39,8.8,1.06,-1.19,9.16,1.06,-1.23,9.17,1.09,-1.23,9.16,1.05,-1.07,9.16,1.18,-1.15,9.11,1.15,-0.95,9.09,0.92,-1.15,9.2,1.02,-1.31,9.21,1.02,-1.19,9.18,0.36,-1.35,9.41,0.32,-1.47,9.45,0.64,-1.55,9.36,0.34,-1.19,9.39,0.31,-1.03,9.41,0.24,-1.23,9.43,0,-1.11,9.38,-0.12,-1.07,9.38,-0.02,-1.43,9.46,-0.74,-1.11,6.69,-0.77,-1.43,6.74,-0.86,-1.35,7.13,-0.74,-1.11,6.69,-0.86,-1.35,7.13,-0.9,-1.19,7.18,-0.9,-1.19,7.18,-0.87,-0.75,7.08,-0.83,-0.75,6.89,-0.77,-1.31,6.24,-0.77,-1.23,6.2,-0.68,-1.35,6.08,-0.18,-1.23,5.71,-0.22,-1.15,5.72,-0.19,-1.15,5.7,-0.14,-1.03,5.66,-0.19,-1.15,5.7,-0.22,-1.11,5.72,0.72,-1.19,5.49,0.83,-1.15,5.55,0.83,-1.19,5.54,-0.42,-0.91,9.27,-0.12,-1.07,9.38,-0.14,-0.83,9.33,-0.42,-0.91,9.27,-0.46,-1.11,9.26,-0.12,-1.07,9.38,-1.03,-1.07,7.74,-0.93,-1.39,7.62,-1.02,-1.31,8.02,-1.03,-1.07,7.74,-0.97,-1.11,7.43,-0.93,-1.39,7.62,-0.77,-1.23,6.2,-0.78,-0.95,6.27,-0.76,-0.99,6.17,-0.68,-1.35,6.08,-0.31,-1.11,5.8,-0.62,-1.47,6.01,0.46,-1.43,5.47,-0.12,-1.47,5.64,0.03,-1.11,5.57,0.55,-1.19,5.5,0.03,-1.11,5.57,0.39,-0.87,5.49,1.2,-1.19,5.66,1.06,-1.23,5.58,1,-0.99,5.59,1.56,-1.11,6,1.58,-1.35,6.17,1.53,-1.47,5.95,1.69,-1.27,8.1,1.58,-1.47,8.1,1.52,-1.35,7.64,1.51,-1.63,8.52,1.67,-1.31,8.19,1.58,-1.35,8.58,1.67,-1.31,8.19,1.65,-1.19,8.48,1.58,-1.35,8.58,1.55,-1.19,8.72,1.65,-1.19,8.48,1.72,-0.91,8.46,1.55,-1.19,8.72,1.58,-1.35,8.58,1.65,-1.19,8.48,1.55,-1.19,8.72,1.48,-1.27,8.81,1.49,-1.31,8.78,1.47,-1.07,8.84,1.44,-1.27,8.86,1.48,-1.27,8.81,1.15,-0.95,9.09,1.47,-0.87,8.85,1.34,-0.75,8.97,1.02,-1.19,9.18,1.06,-1.23,9.17,1.06,-1.19,9.16,0.59,-1.15,9.32,0.48,-1.11,9.35,0.49,-1.15,9.35,0.59,-1.15,9.32,0.46,-1.23,9.37,0.73,-1.47,9.36,1.38,-0.75,5.9,1.2,-1.19,5.66,1,-0.99,5.59,1.36,-1.27,5.77,1.2,-1.19,5.66,1.38,-0.75,5.9,1.55,-1.19,8.72,1.49,-1.31,8.78,1.58,-1.35,8.58,1.47,-1.07,8.84,1.48,-1.27,8.81,1.55,-1.19,8.72,1.15,-0.95,9.09,1.18,-1.15,9.11,1.44,-1.27,8.86,1.09,-1.23,9.16,1.06,-1.23,9.17,1.1,-1.27,9.16,0.24,-1.31,9.43,0.29,-1.27,9.43,0.24,-1.23,9.43,0,-1.11,9.38,-0.02,-1.43,9.46,0.07,-1.39,9.47,-0.85,-1.47,8.83,-0.85,-1.23,8.84,-0.87,-1.15,8.41,-0.9,-1.95,8,-0.93,-1.99,8.13,-0.96,-1.87,8.22,-0.68,-1.35,6.08,-0.77,-1.23,6.2,-0.46,-0.99,6.02,-0.77,-1.31,6.24,-0.68,-1.35,6.08,-0.75,-1.43,6.17,-0.18,-1.23,5.71,-0.23,-1.27,5.75,-0.22,-1.15,5.72,0.24,-1.23,9.43,0.15,-1.35,9.43,0.24,-1.31,9.43,0,-1.11,9.38,0.15,-1.35,9.43,0.24,-1.23,9.43,-0.46,-1.11,9.26,-0.63,-0.79,8.86,-0.68,-0.95,8.75,-0.77,-1.23,6.2,-0.77,-1.31,6.24,-0.72,-1.19,6.51,-0.22,-1.11,5.72,-0.31,-1.11,5.8,-0.34,-0.91,5.86,-0.22,-1.11,5.72,-0.22,-1.15,5.72,-0.31,-1.11,5.8,0.58,-1.35,5.49,0.72,-1.19,5.49,0.7,-1.39,5.48,1.07,-1.35,5.61,1.18,-1.23,5.72,1.19,-1.55,5.71,1.52,-1.35,7.64,1.45,-1.35,7.54,1.49,-1.27,7.5,1.69,-1.27,8.1,1.67,-1.31,8.19,1.58,-1.47,8.1,1.48,-1.27,8.81,1.48,-1.31,8.81,1.49,-1.31,8.78,0.59,-1.15,9.32,0.92,-1.15,9.2,0.64,-0.95,9.29,0.36,-1.35,9.41,0.46,-1.23,9.37,0.34,-1.19,9.39,1.75,-0.87,6.34,1.76,-1.07,6.37,1.56,-1.11,6,1.58,-1.47,8.1,1.47,-1.59,7.93,1.52,-1.35,7.64,1.52,-1.35,7.64,1.69,-0.99,7.7,1.73,-1.11,7.96,1.48,-1.31,8.81,1.48,-1.27,8.81,1.44,-1.27,8.86,1.15,-0.95,9.09,1.47,-1.07,8.84,1.47,-0.87,8.85,1.09,-1.23,9.16,1.1,-1.27,9.16,1.19,-1.27,9.12,1.11,-1.43,9.17,1.17,-1.47,9.11,1.19,-1.27,9.12,1.06,-1.23,9.17,1.02,-1.31,9.21,1.1,-1.27,9.16,1.02,-1.31,9.21,1.06,-1.23,9.17,1.02,-1.19,9.18,1.02,-1.31,9.21,0.73,-1.47,9.36,0.94,-1.47,9.22,0.59,-1.15,9.32,0.49,-1.15,9.35,0.46,-1.23,9.37,0.46,-1.23,9.37,0.36,-1.35,9.41,0.64,-1.55,9.36,0.15,-1.35,9.43,0.16,-1.39,9.43,0.2,-1.39,9.42,-0.46,-1.11,9.26,-0.68,-0.95,8.75,-0.85,-1.23,8.84,-0.85,-1.47,8.83,-0.74,-1.39,9.02,-0.85,-1.23,8.84,-0.93,-1.39,7.62,-0.78,-1.39,7.4,-0.71,-1.51,7.42,-0.49,-1.99,7.52,-0.55,-2.07,7.55,-0.73,-1.95,7.68,-0.75,-1.47,6.56,-0.72,-1.19,6.51,-0.77,-1.31,6.24,-0.23,-1.27,5.75,-0.31,-1.11,5.8,-0.22,-1.15,5.72,-0.14,-1.03,5.66,-0.18,-0.87,5.68,0.04,-0.95,5.62,0.55,-1.19,5.5,0.58,-1.35,5.49,0.46,-1.43,5.47,1.2,-1.19,5.66,1.18,-1.23,5.72,1.06,-1.23,5.58,-0.02,-1.43,9.46,-0.42,-1.35,9.3,-0.08,-1.55,9.51,-0.75,-1.75,9.06,-0.56,-1.87,9.26,-0.46,-1.55,9.29,-1.02,-1.31,8.02,-0.99,-1.67,8.34,-0.87,-1.15,8.41,-1,-0.79,7.55,-0.97,-1.11,7.43,-1.03,-1.07,7.74,-0.77,-1.43,6.74,-0.74,-1.11,6.69,-0.75,-1.43,6.64,-0.68,-1.35,6.08,-0.46,-0.99,6.02,-0.31,-1.11,5.8,0.58,-1.35,5.49,0.55,-1.19,5.5,0.72,-1.19,5.49,0.9,-1.67,5.54,0.64,-1.63,5.47,0.7,-1.39,5.48,1.54,-1.71,6.13,1.59,-1.63,6.09,1.57,-1.55,6.31,1.72,-1.23,7.29,1.52,-1.59,7.2,1.86,-1.07,7.02,1.42,-1.47,7.63,1.32,-1.47,7.56,1.33,-1.43,7.55,1.42,-1.39,7.56,1.45,-1.35,7.54,1.52,-1.35,7.64,1.47,-1.39,8.8,1.49,-1.31,8.78,1.48,-1.31,8.81,1.15,-0.95,9.09,1.44,-1.27,8.86,1.47,-1.07,8.84,0.46,-1.23,9.37,0.64,-1.55,9.36,0.73,-1.47,9.36,0.36,-1.35,9.41,0.32,-1.35,9.41,0.32,-1.47,9.45,0.32,-1.35,9.41,0.24,-1.31,9.43,0.2,-1.39,9.42,0.24,-1.31,9.43,0.15,-1.35,9.43,0.2,-1.39,9.42,1.42,-1.39,7.56,1.42,-1.47,7.63,1.33,-1.43,7.55,1.42,-1.39,7.56,1.52,-1.35,7.64,1.42,-1.47,7.63,1.48,-1.31,8.81,1.44,-1.27,8.86,1.47,-1.39,8.8,1.17,-1.47,9.11,1.21,-1.51,9.06,1.29,-1.43,9.01,1.02,-1.43,9.22,1.11,-1.43,9.17,1.02,-1.31,9.21,0.13,-1.43,9.44,0.17,-1.43,9.44,0.07,-1.39,9.47,0.06,-1.43,9.48,0.13,-1.43,9.44,0.07,-1.39,9.47,0.06,-1.43,9.48,0.07,-1.39,9.47,-0.02,-1.43,9.46,-0.12,-1.07,9.38,-0.42,-1.35,9.3,-0.02,-1.43,9.46,-0.79,-1.55,8.98,-0.75,-1.75,9.06,-0.46,-1.55,9.29,-0.78,-1.39,7.4,-0.9,-1.19,7.18,-0.86,-1.35,7.13,-0.86,-1.35,7.13,-0.79,-1.63,6.96,-0.72,-1.83,7.2,-0.75,-1.47,6.56,-0.75,-1.43,6.64,-0.72,-1.19,6.51,-0.76,-0.87,6.75,-0.74,-1.11,6.69,-0.9,-1.19,7.18,-0.77,-1.43,6.74,-0.79,-1.63,6.96,-0.86,-1.35,7.13,-0.75,-1.43,6.17,-0.68,-1.35,6.08,-0.62,-1.47,6.01,-0.76,-1.55,6.21,-0.75,-1.43,6.17,-0.62,-1.47,6.01,0.34,-1.67,5.44,0.11,-1.75,5.49,-0.12,-1.47,5.64,1.76,-1.07,6.37,1.58,-1.35,6.17,1.56,-1.11,6,1.49,-1.27,7.5,1.43,-1.39,7.48,1.72,-1.23,7.29,1.45,-1.35,7.54,1.43,-1.39,7.48,1.49,-1.27,7.5,-0.02,-1.43,9.46,0.01,-1.47,9.48,0.06,-1.43,9.48,-0.08,-1.55,9.51,-0.05,-1.47,9.56,0.01,-1.47,9.48,-0.85,-1.47,8.83,-0.81,-1.75,8.88,-0.79,-1.55,8.98,-1.01,-1.55,7.99,-0.93,-1.39,7.62,-0.9,-1.71,7.81,-0.77,-1.43,6.74,-0.75,-1.43,6.64,-0.75,-1.47,6.64,-0.75,-1.47,6.64,-0.75,-1.43,6.64,-0.75,-1.47,6.56,0.64,-1.63,5.47,0.46,-1.63,5.4,0.53,-1.51,5.44,0.7,-1.39,5.48,0.83,-1.19,5.54,0.95,-1.39,5.62,0.7,-1.39,5.48,0.72,-1.19,5.49,0.83,-1.19,5.54,1.76,-1.35,6.7,1.57,-1.55,6.31,1.58,-1.35,6.17,1.58,-1.59,6.49,1.76,-1.35,6.7,1.56,-1.71,6.75,1.48,-1.51,7.37,1.52,-1.59,7.2,1.72,-1.23,7.29,1.9,-0.79,6.78,1.92,-0.79,6.91,1.86,-1.07,7.02,1.43,-1.39,7.48,1.48,-1.51,7.37,1.72,-1.23,7.29,1.37,-1.47,7.47,1.4,-1.47,7.46,1.43,-1.39,7.48,1.32,-1.47,7.56,1.22,-1.59,7.59,1.3,-1.51,7.5,1.58,-1.47,8.1,1.37,-1.75,8.13,1.47,-1.59,7.93,1.51,-1.63,8.52,1.58,-1.35,8.58,1.47,-1.39,8.8,1.49,-1.31,8.78,1.47,-1.39,8.8,1.58,-1.35,8.58,1.21,-1.51,9.06,1.17,-1.47,9.11,1.15,-1.51,9.09,1.17,-1.47,9.11,1.11,-1.43,9.17,1.09,-1.47,9.15,1.02,-1.43,9.22,1.02,-1.31,9.21,0.94,-1.47,9.22,0.8,-1.63,9.3,0.88,-1.55,9.21,0.73,-1.47,9.36,0.21,-1.43,9.44,0.32,-1.47,9.45,0.32,-1.35,9.41,0.56,-1.71,9.34,0.22,-1.63,9.48,0.25,-1.91,9.47,0.21,-1.43,9.44,0.17,-1.43,9.44,0.18,-1.47,9.44,-0.08,-1.55,9.51,0.01,-1.47,9.48,-0.02,-1.43,9.46,-0.86,-1.59,8.69,-0.87,-1.15,8.41,-0.99,-1.67,8.34,-0.96,-1.87,8.22,-0.99,-1.67,8.34,-1.01,-1.55,7.99,-0.67,-1.67,7.39,-0.86,-1.35,7.13,-0.72,-1.83,7.2,-0.76,-1.55,6.21,-0.78,-1.63,6.42,-0.75,-1.47,6.56,-0.12,-1.47,5.64,0.11,-1.75,5.49,-0.01,-1.91,5.54,0.55,-1.47,5.46,0.46,-1.43,5.47,0.58,-1.35,5.49,0.53,-1.51,5.44,0.55,-1.47,5.46,0.57,-1.47,5.45,0.64,-1.63,5.47,0.57,-1.47,5.45,0.7,-1.39,5.48,1.19,-1.55,5.71,0.9,-1.67,5.54,0.95,-1.39,5.62,1.07,-1.35,5.61,1.06,-1.23,5.58,1.18,-1.23,5.72,1.19,-1.55,5.71,1.33,-1.75,6.05,1.17,-1.75,5.69,1.59,-1.63,6.09,1.53,-1.55,5.98,1.58,-1.35,6.17,1.76,-1.07,6.37,1.76,-1.35,6.7,1.58,-1.35,6.17,1.52,-1.59,7.2,1.71,-1.47,6.87,1.86,-1.07,7.02,1.32,-1.47,7.56,1.3,-1.51,7.5,1.39,-1.51,7.45,1.04,-1.79,7.68,1.1,-1.91,7.78,1.06,-1.95,7.74,1.47,-1.59,7.93,1.42,-1.47,7.63,1.52,-1.35,7.64,1.72,-0.91,8.46,1.65,-1.19,8.48,1.7,-1.23,8.17,1.29,-1.43,9.01,1.35,-1.55,8.91,1.47,-1.39,8.8,1.32,-1.63,8.91,1.35,-1.55,8.91,1.28,-1.59,8.96,1.11,-1.43,9.17,1.19,-1.27,9.12,1.1,-1.27,9.16,1.11,-1.43,9.17,1.1,-1.27,9.16,1.02,-1.31,9.21,0.73,-1.47,9.36,0.88,-1.55,9.21,0.94,-1.47,9.22,0.8,-1.63,9.3,0.73,-1.47,9.36,0.72,-1.63,9.32,0.92,-1.15,9.2,0.59,-1.15,9.32,0.73,-1.47,9.36,0.2,-1.39,9.42,0.21,-1.43,9.44,0.32,-1.35,9.41,0.18,-1.47,9.44,0.17,-1.43,9.44,0.13,-1.43,9.44,-0.2,-1.63,9.4,-0.09,-1.63,9.47,-0.08,-1.55,9.51,-0.42,-1.35,9.3,-0.74,-1.39,9.02,-0.46,-1.55,9.29,-0.56,-1.87,9.26,-0.75,-1.75,9.06,-0.77,-1.83,9,-0.67,-1.67,7.39,-0.71,-1.51,7.42,-0.86,-1.35,7.13,-0.71,-1.51,7.42,-0.78,-1.39,7.4,-0.86,-1.35,7.13,-0.77,-1.43,6.74,-0.75,-1.47,6.64,-0.79,-1.59,6.74,-0.79,-1.63,6.7,-0.79,-1.59,6.74,-0.75,-1.47,6.64,-0.75,-1.43,6.17,-0.75,-1.47,6.56,-0.77,-1.31,6.24,-0.52,-1.55,5.94,-0.23,-1.27,5.75,-0.12,-1.47,5.64,0.46,-1.43,5.47,0.34,-1.67,5.44,-0.12,-1.47,5.64,0.64,-1.63,5.47,0.53,-1.51,5.44,0.57,-1.47,5.45,1.17,-1.75,5.69,0.97,-1.83,5.57,0.9,-1.67,5.54,1.57,-1.55,6.31,1.65,-1.75,6.27,1.6,-1.75,6.17,1.71,-1.47,6.87,1.52,-1.59,7.2,1.56,-1.71,6.75,1.48,-1.51,7.37,1.39,-1.51,7.45,1.36,-1.67,7.3,1.43,-1.39,7.48,1.4,-1.47,7.46,1.48,-1.51,7.37,1.42,-1.47,7.63,1.25,-1.63,7.64,1.22,-1.59,7.59,1.47,-1.39,8.8,1.35,-1.55,8.91,1.38,-1.63,8.85,1.35,-1.55,8.91,1.27,-1.55,8.99,1.28,-1.59,8.96,1.29,-1.43,9.01,1.27,-1.55,8.99,1.35,-1.55,8.91,1.27,-1.55,8.99,1.29,-1.43,9.01,1.21,-1.51,9.06,1.17,-1.47,9.11,1.29,-1.43,9.01,1.19,-1.27,9.12,0.96,-1.51,9.13,1.05,-1.75,8.96,1.12,-1.67,8.87,0.96,-1.51,9.13,0.89,-1.75,9.22,1.05,-1.75,8.96,0.18,-1.47,9.44,0.05,-1.51,9.46,0.12,-1.59,9.47,-0.08,-1.55,9.51,-0.09,-1.63,9.47,-0.1,-1.63,9.51,-0.77,-1.43,6.74,-0.79,-1.59,6.74,-0.79,-1.63,6.96,-0.62,-1.47,6.01,-0.52,-1.55,5.94,-0.62,-1.67,6,-0.12,-1.47,5.64,-0.23,-1.27,5.75,-0.18,-1.23,5.71,1.03,-1.95,5.6,0.97,-1.83,5.57,1.17,-1.75,5.69,1.59,-1.63,6.09,1.58,-1.35,6.17,1.57,-1.55,6.31,1.53,-1.55,5.98,1.53,-1.47,5.95,1.58,-1.35,6.17,1.57,-1.79,6.54,1.58,-1.79,6.47,1.58,-1.59,6.49,1.76,-1.35,6.7,1.58,-1.59,6.49,1.57,-1.55,6.31,1.39,-1.51,7.45,1.48,-1.51,7.37,1.4,-1.47,7.46,1.39,-1.51,7.45,1.3,-1.67,7.37,1.36,-1.67,7.3,1.39,-1.51,7.45,1.3,-1.51,7.5,1.3,-1.67,7.37,1.58,-1.47,8.1,1.44,-1.71,8.24,1.37,-1.75,8.13,1.46,-1.71,8.71,1.51,-1.63,8.52,1.47,-1.39,8.8,1.27,-1.55,8.99,1.21,-1.51,9.06,1.19,-1.55,9.04,1.26,-1.59,8.98,1.28,-1.59,8.96,1.27,-1.55,8.99,0.95,-1.87,9.15,1.03,-1.91,9.02,1.05,-1.75,8.96,0.12,-1.59,9.47,0.22,-1.63,9.48,0.32,-1.47,9.45,0.18,-1.47,9.44,0.13,-1.43,9.44,0.05,-1.51,9.46,0.05,-1.59,9.46,0.12,-1.59,9.47,0.05,-1.51,9.46,-0.42,-1.35,9.3,-0.46,-1.55,9.29,-0.2,-1.63,9.4,-1.01,-1.55,7.99,-0.9,-1.71,7.81,-0.91,-1.87,7.96,-0.75,-1.43,6.17,-0.76,-1.55,6.21,-0.75,-1.47,6.56,-0.68,-1.67,6.07,-0.62,-1.47,6.01,-0.62,-1.67,6,-0.59,-1.71,5.99,-0.61,-1.71,6.01,-0.62,-1.67,6,0.3,-1.75,5.45,0.34,-1.67,5.44,0.44,-1.75,5.47,0.46,-1.43,5.47,0.55,-1.47,5.46,0.53,-1.51,5.44,0.64,-1.63,5.47,0.9,-1.67,5.54,0.82,-1.79,5.56,1.34,-1.87,5.97,1.27,-1.95,5.8,1.17,-1.75,5.69,1.55,-1.83,6.78,1.56,-1.71,6.75,1.42,-1.83,7.04,1.76,-1.35,6.7,1.71,-1.47,6.87,1.56,-1.71,6.75,1.14,-1.63,7.58,1.04,-1.79,7.68,0.99,-1.75,7.61,1.73,-1.11,7.96,1.69,-1.27,8.1,1.52,-1.35,7.64,1.27,-1.63,8.95,1.32,-1.63,8.91,1.28,-1.59,8.96,0.96,-1.51,9.13,0.88,-1.55,9.21,0.89,-1.75,9.22,0.88,-1.55,9.21,0.8,-1.63,9.3,0.82,-1.67,9.28,0.88,-1.55,9.21,0.96,-1.51,9.13,0.94,-1.47,9.22,0.8,-1.63,9.3,0.72,-1.63,9.32,0.69,-1.67,9.29,0.73,-1.47,9.36,0.64,-1.55,9.36,0.72,-1.63,9.32,0.72,-1.63,9.32,0.64,-1.55,9.36,0.67,-1.67,9.31,0.67,-1.71,9.31,0.67,-1.67,9.31,0.56,-1.71,9.34,-0.2,-1.79,9.48,-0.2,-1.63,9.4,-0.46,-1.55,9.29,-0.71,-1.51,7.42,-0.9,-1.71,7.81,-0.93,-1.39,7.62,-0.75,-1.79,6.93,-0.78,-1.67,6.73,-0.77,-1.75,6.69,-0.79,-1.63,6.7,-0.78,-1.67,6.73,-0.79,-1.59,6.74,-0.78,-1.63,6.42,-0.79,-1.63,6.7,-0.75,-1.47,6.56,-0.52,-1.55,5.94,-0.48,-1.75,5.89,-0.59,-1.71,5.99,-0.52,-1.55,5.94,-0.59,-1.71,5.99,-0.62,-1.67,6,-0.28,-1.99,5.75,-0.48,-1.75,5.89,-0.12,-1.47,5.64,0.46,-1.63,5.4,0.46,-1.43,5.47,0.53,-1.51,5.44,0.34,-1.67,5.44,0.46,-1.63,5.4,0.45,-1.71,5.46,1.54,-1.71,6.13,1.57,-1.55,6.31,1.6,-1.75,6.17,1.2,-1.67,7.45,1.2,-1.71,7.41,1.3,-1.67,7.37,1.2,-1.67,7.45,1.3,-1.67,7.37,1.3,-1.51,7.5,1.51,-1.63,8.52,1.35,-1.79,8.53,1.29,-1.79,8.39,1.33,-1.75,8.32,1.44,-1.71,8.24,1.51,-1.63,8.52,1.46,-1.71,8.71,1.41,-1.75,8.63,1.51,-1.63,8.52,1.32,-1.63,8.91,1.38,-1.63,8.85,1.35,-1.55,8.91,1.3,-1.67,8.9,1.32,-1.67,8.88,1.32,-1.63,8.91,0.81,-1.71,9.27,0.89,-1.75,9.22,0.82,-1.67,9.28,0.8,-1.67,9.3,0.82,-1.67,9.28,0.8,-1.63,9.3,0.67,-1.67,9.31,0.69,-1.67,9.29,0.72,-1.63,9.32,0.67,-1.67,9.31,0.64,-1.55,9.36,0.56,-1.71,9.34,0.81,-1.71,9.27,0.67,-1.71,9.31,0.57,-2.03,9.3,0.32,-1.47,9.45,0.56,-1.71,9.34,0.64,-1.55,9.36,0.12,-1.59,9.47,0.32,-1.47,9.45,0.18,-1.47,9.44,0.07,-1.75,9.47,0.22,-1.63,9.48,0.12,-1.59,9.47,-0.1,-1.63,9.51,-0.09,-1.63,9.47,0,-1.67,9.49,-0.46,-1.11,9.26,-0.42,-1.35,9.3,-0.12,-1.07,9.38,-0.56,-1.87,9.26,-0.77,-1.83,9,-0.73,-2.07,9.11,-0.81,-1.75,8.88,-0.77,-1.83,9,-0.75,-1.75,9.06,-0.84,-2.03,7.9,-0.89,-1.99,7.97,-0.91,-1.87,7.96,-0.78,-1.67,6.73,-0.79,-1.63,6.7,-0.77,-1.75,6.69,-0.68,-1.67,6.07,-0.62,-1.67,6,-0.61,-1.71,6.01,-0.6,-1.75,5.99,-0.59,-1.71,5.99,-0.48,-1.75,5.89,0.55,-1.19,5.5,0.46,-1.43,5.47,0.03,-1.11,5.57,0.1,-1.87,5.48,0.11,-1.75,5.49,0.31,-1.83,5.46,0.31,-1.83,5.46,0.29,-1.95,5.45,0.1,-1.87,5.48,0.45,-1.71,5.46,0.64,-1.63,5.47,0.65,-1.79,5.46,0.45,-1.71,5.46,0.46,-1.63,5.4,0.64,-1.63,5.47,1.19,-1.55,5.71,0.95,-1.39,5.62,1.07,-1.35,5.61,0.82,-1.79,5.56,0.9,-1.67,5.54,0.97,-1.83,5.57,1.29,-1.39,5.9,1.33,-1.75,6.05,1.19,-1.55,5.71,1.54,-1.71,6.13,1.56,-1.67,6.07,1.59,-1.63,6.09,1.36,-1.67,7.3,1.52,-1.59,7.2,1.48,-1.51,7.37,1.2,-1.71,7.41,1.2,-1.67,7.45,1.16,-1.71,7.45,1.32,-1.47,7.56,1.42,-1.47,7.63,1.22,-1.59,7.59,1.47,-1.59,7.93,1.25,-1.63,7.64,1.42,-1.47,7.63,1.37,-1.75,8.13,1.35,-1.79,8.05,1.47,-1.59,7.93,1.37,-1.75,8.13,1.44,-1.71,8.24,1.39,-1.75,8.24,1.33,-1.75,8.32,1.51,-1.63,8.52,1.29,-1.79,8.39,1.36,-1.71,8.83,1.36,-1.75,8.79,1.46,-1.71,8.71,1.38,-1.63,8.85,1.36,-1.71,8.83,1.46,-1.71,8.71,1.36,-1.71,8.83,1.38,-1.63,8.85,1.32,-1.67,8.88,1.32,-1.63,8.91,1.32,-1.67,8.88,1.38,-1.63,8.85,1.12,-1.71,8.83,1.14,-1.71,8.8,1.12,-1.67,8.87,1.12,-1.71,8.83,1.12,-1.67,8.87,1.05,-1.75,8.96,0.69,-1.67,9.29,0.67,-1.67,9.31,0.67,-1.71,9.31,-0.07,-1.83,9.47,0.06,-1.79,9.46,-0.04,-1.71,9.5,-0.09,-1.63,9.47,-0.2,-1.63,9.4,-0.2,-1.79,9.48,-0.81,-1.75,8.88,-0.75,-1.75,9.06,-0.79,-1.55,8.98,-0.83,-1.87,8.86,-0.93,-1.83,8.63,-0.82,-1.95,8.85,-0.78,-1.63,6.42,-0.77,-1.75,6.69,-0.79,-1.63,6.7,-0.61,-1.71,6.01,-0.6,-1.75,5.99,-0.66,-1.79,6.05,-0.61,-1.71,6.01,-0.59,-1.71,5.99,-0.6,-1.75,5.99,-0.48,-1.75,5.89,-0.52,-1.55,5.94,-0.12,-1.47,5.64,-0.28,-1.99,5.75,-0.12,-1.47,5.64,-0.01,-1.91,5.54,0.1,-1.87,5.48,-0.01,-1.91,5.54,0.11,-1.75,5.49,0.46,-1.63,5.4,0.34,-1.67,5.44,0.46,-1.43,5.47,0.34,-1.67,5.44,0.45,-1.71,5.46,0.44,-1.75,5.47,0.9,-1.67,5.54,0.7,-1.39,5.48,0.95,-1.39,5.62,0.65,-1.79,5.46,0.64,-1.63,5.47,0.82,-1.79,5.56,1.29,-1.39,5.9,1.19,-1.55,5.71,1.18,-1.23,5.72,1.41,-1.71,6.18,1.33,-1.75,6.05,1.29,-1.39,5.9,1.42,-1.83,7.04,1.33,-1.71,7.24,1.29,-1.87,7.17,1.56,-1.71,6.75,1.52,-1.59,7.2,1.42,-1.83,7.04,1.19,-1.75,7.32,1.22,-1.75,7.3,1.2,-1.71,7.41,1.14,-1.63,7.58,1.22,-1.59,7.59,1.25,-1.63,7.64,1.47,-1.59,7.93,1.32,-1.71,7.89,1.25,-1.63,7.64,1.33,-1.75,8.32,1.39,-1.75,8.24,1.44,-1.71,8.24,1.58,-1.47,8.1,1.67,-1.31,8.19,1.51,-1.63,8.52,1.45,-1.75,8.71,1.46,-1.71,8.71,1.36,-1.75,8.79,1.44,-1.79,8.72,1.45,-1.75,8.71,1.36,-1.75,8.79,1.36,-1.71,8.83,1.32,-1.67,8.88,1.31,-1.71,8.87,1.34,-1.75,8.81,1.36,-1.75,8.79,1.36,-1.71,8.83,1.14,-1.71,8.8,1.12,-1.71,8.83,1.14,-1.75,8.8,1.12,-1.71,8.83,1.05,-1.75,8.96,1.08,-1.87,8.91,0.89,-1.75,9.22,0.81,-1.71,9.27,0.85,-1.91,9.23,0.57,-2.03,9.3,0.25,-1.91,9.47,0.18,-2.07,9.48,0.06,-1.79,9.46,0.07,-1.75,9.47,-0.04,-1.71,9.5,0,-1.67,9.49,0.07,-1.75,9.47,0.12,-1.59,9.47,0.07,-1.75,9.47,0,-1.67,9.49,-0.04,-1.71,9.5,-0.96,-1.83,8.54,-0.93,-1.83,8.63,-0.86,-1.59,8.69,-0.96,-1.83,8.54,-0.96,-1.87,8.22,-0.95,-2.11,8.35,-1.02,-1.31,8.02,-1.01,-1.55,7.99,-0.99,-1.67,8.34,-0.67,-1.67,7.39,-0.58,-1.91,7.37,-0.57,-1.79,7.5,-0.72,-1.83,7.2,-0.79,-1.63,6.96,-0.75,-1.79,6.93,-0.75,-1.79,6.93,-0.79,-1.63,6.96,-0.78,-1.67,6.73,-0.68,-1.67,6.07,-0.66,-1.79,6.05,-0.77,-1.91,6.32,-0.68,-1.67,6.07,-0.77,-1.91,6.32,-0.76,-1.55,6.21,-0.61,-1.71,6.01,-0.66,-1.79,6.05,-0.68,-1.67,6.07,1.1,-1.91,7.78,1.04,-1.79,7.68,1.2,-1.87,7.86,1.27,-1.83,7.92,1.2,-1.87,7.86,1.32,-1.71,7.89,1.04,-1.79,7.68,1.25,-1.63,7.64,1.32,-1.71,7.89,1.35,-1.79,8.05,1.3,-1.83,8.01,1.32,-1.71,7.89,1.6,-1.75,6.17,1.65,-1.75,6.27,1.57,-1.91,6.25,1.58,-1.79,6.47,1.56,-1.83,6.38,1.65,-1.75,6.27,1.58,-1.79,6.47,1.65,-1.75,6.27,1.58,-1.59,6.49,1.57,-1.79,6.54,1.58,-1.59,6.49,1.56,-1.71,6.75,1.56,-1.71,6.75,1.53,-1.83,6.61,1.57,-1.79,6.54,1.36,-1.67,7.3,1.33,-1.71,7.24,1.52,-1.59,7.2,1.22,-1.75,7.3,1.29,-1.87,7.17,1.33,-1.71,7.24,1.32,-1.83,8.44,1.29,-1.79,8.39,1.35,-1.79,8.53,1.41,-1.75,8.63,1.35,-1.79,8.53,1.51,-1.63,8.52,1.46,-1.71,8.71,1.47,-1.39,8.8,1.38,-1.63,8.85,1.45,-1.75,8.71,1.41,-1.75,8.63,1.46,-1.71,8.71,1.44,-1.79,8.72,1.42,-1.79,8.7,1.45,-1.75,8.71,1.44,-1.79,8.72,1.36,-1.75,8.79,1.34,-1.79,8.78,1.14,-1.75,8.8,1.12,-1.71,8.83,1.08,-1.87,8.91,0.95,-1.87,9.15,0.89,-1.75,9.22,0.85,-1.91,9.23,0.88,-1.55,9.21,0.82,-1.67,9.28,0.89,-1.75,9.22,0.81,-1.71,9.27,0.57,-2.03,9.3,0.85,-1.91,9.23,0.32,-1.47,9.45,0.21,-1.43,9.44,0.18,-1.47,9.44,-0.25,-1.79,9.55,-0.21,-1.91,9.48,-0.25,-1.91,9.55,-0.25,-1.79,9.55,-0.2,-1.79,9.48,-0.21,-1.91,9.48,-0.42,-1.35,9.3,-0.46,-1.11,9.26,-0.74,-1.39,9.02,-0.96,-1.83,8.54,-0.86,-1.59,8.69,-0.99,-1.67,8.34,-0.93,-1.83,8.63,-0.96,-1.83,8.54,-0.92,-2.15,8.51,-0.96,-1.87,8.22,-1.01,-1.55,7.99,-0.91,-1.87,7.96,-0.58,-1.91,7.37,-0.51,-1.91,7.47,-0.57,-1.79,7.5,-0.72,-1.83,7.2,-0.58,-1.91,7.37,-0.67,-1.67,7.39,-0.79,-1.63,6.96,-0.79,-1.59,6.74,-0.78,-1.67,6.73,-0.04,-2.03,5.55,-0.09,-2.15,5.59,-0.28,-1.99,5.75,0.65,-1.79,5.46,0.57,-1.95,5.45,0.44,-1.91,5.45,1.17,-1.75,5.69,0.9,-1.67,5.54,1.19,-1.55,5.71,1.37,-1.87,6.24,1.33,-1.75,6.05,1.41,-1.71,6.18,1.33,-1.75,6.05,1.37,-1.87,6.24,1.34,-1.87,5.97,1.57,-1.91,6.25,1.65,-1.75,6.27,1.56,-1.83,6.38,1.65,-1.75,6.27,1.57,-1.55,6.31,1.58,-1.59,6.49,1.53,-1.83,6.61,1.56,-1.71,6.75,1.55,-1.83,6.78,1.08,-1.79,7.38,1.06,-1.83,7.37,1.19,-1.83,7.28,1.22,-1.75,7.3,1.19,-1.75,7.32,1.19,-1.83,7.28,1.08,-1.79,7.38,1.19,-1.83,7.28,1.19,-1.75,7.32,0.93,-1.87,7.69,0.95,-1.83,7.71,1.06,-1.95,7.74,1.04,-1.79,7.68,1.32,-1.71,7.89,1.2,-1.87,7.86,1.1,-1.91,7.78,1.2,-1.87,7.86,1.16,-1.91,7.89,1.14,-1.63,7.58,1.25,-1.63,7.64,1.04,-1.79,7.68,1.35,-1.79,8.05,1.32,-1.71,7.89,1.47,-1.59,7.93,1.3,-1.83,8.01,1.27,-1.83,7.92,1.32,-1.71,7.89,1.37,-1.75,8.13,1.35,-1.79,8.13,1.35,-1.79,8.05,1.27,-1.83,8.07,1.3,-1.83,8.01,1.35,-1.79,8.05,1.25,-1.79,8.31,1.33,-1.75,8.32,1.29,-1.79,8.39,1.25,-1.79,8.31,1.34,-1.99,8.28,1.21,-1.91,8.22,1.42,-1.79,8.7,1.43,-1.83,8.68,1.4,-1.83,8.63,1.41,-1.75,8.63,1.42,-1.79,8.7,1.4,-1.83,8.63,1.42,-1.79,8.7,1.41,-1.75,8.63,1.45,-1.75,8.71,1.4,-1.83,8.71,1.43,-1.83,8.68,1.42,-1.79,8.7,1.08,-1.87,8.91,1.06,-1.95,8.93,1.07,-1.99,8.79,0.56,-1.71,9.34,0.25,-1.91,9.47,0.57,-2.03,9.3,-0.07,-1.83,9.47,-0.04,-1.71,9.5,-0.1,-1.79,9.49,-0.21,-1.91,9.48,-0.17,-2.07,9.49,-0.12,-1.99,9.5,-0.85,-1.47,8.83,-0.86,-1.59,8.69,-0.81,-1.75,8.88,-0.83,-1.87,8.86,-0.81,-1.75,8.88,-0.93,-1.83,8.63,-0.96,-1.83,8.54,-0.99,-1.67,8.34,-0.96,-1.87,8.22,-0.91,-1.87,7.96,-0.89,-1.99,7.97,-0.9,-1.95,8,-0.71,-1.51,7.42,-0.67,-1.67,7.39,-0.9,-1.71,7.81,-0.77,-1.75,6.69,-0.68,-2.35,6.85,-0.75,-1.79,6.93,-0.79,-1.63,6.7,-0.75,-1.47,6.64,-0.75,-1.47,6.56,-0.68,-1.67,6.07,-0.76,-1.55,6.21,-0.62,-1.47,6.01,0.34,-1.67,5.44,0.3,-1.75,5.45,0.11,-1.75,5.49,0.29,-1.95,5.45,0.25,-1.99,5.45,0.1,-1.87,5.48,0.34,-1.87,5.36,0.4,-1.87,5.46,0.31,-1.83,5.46,1.03,-1.95,5.6,0.95,-1.91,5.58,0.97,-1.83,5.57,1.62,-1.95,6.32,1.57,-1.91,6.25,1.56,-1.83,6.38,1.52,-1.87,6.46,1.56,-1.83,6.38,1.58,-1.79,6.47,1.48,-1.83,6.46,1.52,-1.87,6.46,1.58,-1.79,6.47,1.4,-1.83,6.56,1.48,-1.87,6.51,1.48,-1.83,6.46,1.52,-1.59,7.2,1.33,-1.71,7.24,1.42,-1.83,7.04,1.22,-1.75,7.3,1.19,-1.83,7.28,1.29,-1.87,7.17,1.29,-1.87,7.17,1.19,-1.83,7.28,1.15,-1.91,7.25,0.85,-1.83,7.67,0.93,-1.87,7.69,0.83,-1.91,7.61,0.95,-1.83,7.71,0.93,-1.87,7.69,0.85,-1.83,7.67,0.97,-1.95,7.66,0.93,-1.87,7.69,1.06,-1.95,7.74,1.2,-1.87,7.86,1.27,-1.83,7.92,1.25,-1.87,7.94,1.19,-1.83,8.23,1.21,-1.91,8.22,1.2,-1.83,8.16,1.19,-1.83,8.23,1.25,-1.79,8.31,1.21,-1.91,8.22,1.4,-1.91,8.49,1.32,-1.83,8.44,1.35,-1.79,8.53,1.42,-1.87,8.59,1.4,-1.83,8.63,1.4,-1.87,8.65,1.4,-1.83,8.63,1.35,-1.79,8.53,1.41,-1.75,8.63,1.03,-1.91,9.02,1.08,-1.87,8.91,1.05,-1.75,8.96,1.03,-1.91,9.02,1.06,-1.95,8.93,1.08,-1.87,8.91,0.67,-1.71,9.31,0.56,-1.71,9.34,0.57,-2.03,9.3,0.22,-1.63,9.48,0.07,-1.75,9.47,0.09,-1.83,9.45,0.09,-1.83,9.45,0.07,-1.75,9.47,0.06,-1.79,9.46,-0.09,-1.91,9.46,-0.08,-1.95,9.46,-0.03,-1.95,9.47,-0.09,-1.91,9.46,-0.07,-1.83,9.47,-0.12,-1.83,9.47,-0.31,-1.91,9.44,-0.2,-1.79,9.48,-0.46,-1.55,9.29,-0.21,-1.91,9.48,-0.12,-1.99,9.5,-0.08,-1.95,9.46,-0.56,-1.87,9.26,-0.31,-1.91,9.44,-0.46,-1.55,9.29,-0.74,-1.39,9.02,-0.46,-1.11,9.26,-0.85,-1.23,8.84,-0.83,-1.87,8.86,-0.81,-1.95,8.88,-0.77,-1.83,9,-0.81,-1.95,8.88,-0.82,-1.99,8.88,-0.81,-1.99,8.91,-0.81,-1.75,8.88,-0.86,-1.59,8.69,-0.93,-1.83,8.63,-0.88,-2.07,8.78,-0.82,-1.95,8.85,-0.93,-1.83,8.63,-0.9,-1.95,8,-0.96,-1.87,8.22,-0.91,-1.87,7.96,-0.77,-1.91,6.32,-0.78,-1.63,6.42,-0.76,-1.55,6.21,-0.6,-1.95,5.99,-0.6,-1.75,5.99,-0.48,-1.75,5.89,-0.01,-2.03,5.54,-0.01,-1.91,5.54,0.1,-1.87,5.48,0.4,-1.87,5.46,0.39,-1.91,5.45,0.35,-1.91,5.45,1.03,-1.95,5.6,1.17,-1.75,5.69,1.27,-1.95,5.8,1.48,-1.87,6.51,1.52,-1.87,6.46,1.48,-1.83,6.46,1.48,-1.87,6.51,1.4,-1.83,6.56,1.4,-1.87,6.61,1.54,-2.19,6.6,1.4,-1.87,6.61,1.23,-1.87,6.92,1.12,-1.91,7.26,1.15,-1.91,7.25,1.19,-1.83,7.28,0.83,-1.91,7.61,0.93,-1.87,7.69,0.94,-1.95,7.64,0.95,-1.83,7.71,1.04,-1.79,7.68,1.06,-1.95,7.74,1.32,-1.83,8.44,1.4,-1.91,8.49,1.4,-1.95,8.46,1.25,-1.79,8.31,1.36,-1.95,8.37,1.34,-1.99,8.28,1.4,-1.91,8.49,1.35,-1.79,8.53,1.42,-1.87,8.59,1.38,-1.95,8.57,1.4,-1.91,8.49,1.42,-1.87,8.59,1.4,-1.83,8.63,1.42,-1.87,8.59,1.35,-1.79,8.53,1.01,-1.95,9.05,0.95,-1.87,9.15,0.94,-1.99,9.14,0.95,-1.87,9.15,0.85,-1.91,9.23,0.94,-1.99,9.14,0.56,-1.71,9.34,0.32,-1.47,9.45,0.22,-1.63,9.48,-0.16,-1.87,9.47,-0.12,-1.83,9.47,-0.2,-1.79,9.48,-0.13,-1.91,9.46,-0.09,-1.91,9.46,-0.12,-1.83,9.47,-0.13,-1.91,9.46,-0.12,-1.83,9.47,-0.16,-1.87,9.47,1.01,-1.95,9.05,1.03,-1.95,9.02,1.03,-1.91,9.02,0.08,-1.95,9.48,0.18,-2.07,9.48,0.25,-1.91,9.47,0.09,-1.83,9.45,0.25,-1.91,9.47,0.22,-1.63,9.48,-0.03,-1.95,9.47,0.06,-1.79,9.46,-0.07,-1.83,9.47,-0.03,-1.95,9.47,-0.07,-1.83,9.47,-0.09,-1.91,9.46,0.09,-1.83,9.45,0.06,-1.79,9.46,-0.03,-1.95,9.47,0.08,-1.95,9.48,0.09,-1.83,9.45,-0.03,-1.95,9.47,-0.21,-1.91,9.48,-0.31,-1.91,9.44,-0.17,-2.07,9.49,-0.85,-1.47,8.83,-0.79,-1.55,8.98,-0.74,-1.39,9.02,-0.81,-1.99,8.91,-0.77,-1.83,9,-0.81,-1.95,8.88,-0.58,-1.91,7.37,-0.63,-1.99,7.29,-0.55,-2.03,7.38,-0.6,-1.95,5.99,-0.66,-1.79,6.05,-0.6,-1.75,5.99,0.3,-1.75,5.45,0.31,-1.83,5.46,0.11,-1.75,5.49,0.35,-1.91,5.45,0.34,-1.95,5.45,0.29,-1.95,5.45,0.35,-1.91,5.45,0.31,-1.83,5.46,0.4,-1.87,5.46,0.35,-1.91,5.45,0.39,-1.91,5.45,0.44,-1.95,5.42,0.39,-1.91,5.45,0.44,-1.91,5.45,0.44,-1.95,5.42,0.44,-1.95,5.42,0.44,-1.91,5.45,0.57,-1.95,5.45,0.57,-1.95,5.45,0.64,-2.11,5.47,0.53,-2.03,5.44,0.68,-2.27,5.48,0.64,-2.11,5.47,0.89,-2.15,5.66,0.86,-1.95,5.61,0.71,-1.95,5.49,0.82,-1.79,5.56,1.03,-1.95,5.6,1.16,-2.11,5.69,1.02,-2.11,5.65,1.03,-1.95,5.6,1.27,-1.95,5.8,1.16,-2.11,5.69,1.27,-1.95,5.8,1.34,-1.87,5.97,1.32,-2.11,5.91,1.54,-2.03,6.35,1.62,-1.95,6.32,1.52,-1.87,6.46,1.52,-1.87,6.46,1.56,-2.03,6.5,1.59,-2.03,6.45,1.52,-1.87,6.46,1.48,-1.87,6.51,1.56,-2.03,6.5,1.15,-1.91,7.25,1.12,-1.91,7.26,1.05,-1.95,7.28,1.05,-1.95,7.28,1.12,-1.91,7.26,1,-1.87,7.27,1.05,-1.95,7.28,1,-1.87,7.27,0.92,-1.95,7.37,0.84,-1.87,7.34,0.92,-1.95,7.37,1,-1.87,7.27,0.82,-2.07,7.58,0.83,-1.91,7.61,0.94,-1.95,7.64,0.82,-2.07,7.58,0.78,-1.99,7.53,0.83,-1.91,7.61,0.93,-1.87,7.69,0.97,-1.95,7.66,0.94,-1.95,7.64,1.1,-1.91,7.78,1.03,-1.95,7.83,1.06,-1.95,7.74,1.03,-1.95,7.91,1.08,-1.99,7.98,1.06,-2.03,7.89,1.1,-1.91,7.97,1.08,-1.91,8.02,1.08,-1.99,7.98,1.08,-1.99,7.98,1.08,-1.91,8.02,1.33,-2.07,8.17,1.08,-1.91,8.02,1.21,-1.91,8.22,1.33,-2.07,8.17,1.36,-1.95,8.37,1.4,-1.95,8.46,1.38,-1.99,8.45,1.29,-1.79,8.39,1.32,-1.83,8.44,1.36,-1.95,8.37,1.38,-1.95,8.5,1.4,-1.95,8.46,1.4,-1.91,8.49,1.38,-1.95,8.5,1.4,-1.91,8.49,1.38,-1.95,8.57,-0.03,-1.95,9.47,-0.08,-1.95,9.46,-0.12,-1.99,9.5,-0.2,-1.79,9.48,-0.31,-1.91,9.44,-0.21,-1.91,9.48,-0.81,-1.99,8.91,-0.73,-2.07,9.11,-0.77,-1.83,9,-0.83,-1.87,8.86,-0.82,-1.95,8.85,-0.81,-1.95,8.88,-0.89,-1.99,7.97,-0.9,-1.99,8,-0.9,-1.95,8,-0.72,-1.83,7.2,-0.63,-1.99,7.29,-0.58,-1.91,7.37,0.05,-2.07,5.51,-0.01,-2.03,5.54,0.1,-1.87,5.48,0.29,-1.95,5.45,0.31,-1.83,5.46,0.35,-1.91,5.45,0.71,-1.95,5.49,0.65,-1.79,5.46,0.82,-1.79,5.56,0.71,-1.95,5.49,0.57,-1.95,5.45,0.65,-1.79,5.46,1.37,-2.15,6.46,1.3,-2.23,6.4,1.37,-1.87,6.24,1.54,-2.03,6.35,1.52,-1.87,6.46,1.59,-2.03,6.45,1.48,-1.87,6.51,1.4,-1.87,6.61,1.56,-2.03,6.5,1.23,-1.87,6.92,1.12,-1.91,7.06,1.14,-2.07,7.12,1.05,-1.95,7.28,1.05,-2.11,7.24,1.05,-1.99,7.2,1.05,-1.95,7.28,0.92,-1.95,7.37,1.05,-2.11,7.24,0.84,-1.91,7.42,0.92,-1.95,7.37,0.84,-1.87,7.34,0.92,-1.95,7.37,0.81,-2.07,7.43,0.88,-2.15,7.37,0.78,-1.99,7.53,0.76,-1.95,7.54,0.83,-1.91,7.61,0.95,-1.99,7.82,1.06,-2.03,7.89,0.98,-2.07,7.76,0.95,-1.99,7.82,1.03,-1.95,7.83,1.06,-2.03,7.89,1.03,-1.95,7.91,1.03,-1.95,7.83,1.1,-1.91,7.78,1.03,-1.95,7.83,1.03,-1.95,7.91,1.06,-2.03,7.89,1.13,-2.07,7.91,1.32,-2.19,8.2,1.33,-2.31,8.07,1.03,-1.95,7.91,1.1,-1.91,7.97,1.08,-1.99,7.98,1.13,-2.07,7.91,1.06,-2.03,7.89,1.08,-1.99,7.98,1.25,-1.79,8.31,1.29,-1.79,8.39,1.36,-1.95,8.37,1.36,-1.95,8.37,1.32,-1.83,8.44,1.4,-1.95,8.46,1.36,-1.95,8.37,1.38,-1.99,8.45,1.36,-2.03,8.4,1.36,-1.95,8.37,1.36,-2.03,8.4,1.36,-2.07,8.32,1.36,-2.03,8.4,1.38,-1.99,8.45,1.37,-2.03,8.46,1.38,-1.99,8.45,1.38,-1.95,8.5,1.38,-1.99,8.5,1.38,-1.99,8.45,1.4,-1.95,8.46,1.38,-1.95,8.5,1.14,-1.75,8.8,1.07,-1.99,8.79,1.17,-1.99,8.52,0.89,-1.75,9.22,0.95,-1.87,9.15,1.05,-1.75,8.96,1.03,-1.95,9.02,1.03,-2.03,8.95,1.06,-1.95,8.93,1.03,-1.95,9.02,1.01,-1.95,9.05,1.01,-1.99,9.05,0.95,-1.87,9.15,1.01,-1.95,9.05,1.03,-1.91,9.02,0,-2.03,9.49,0.18,-2.07,9.48,0.08,-1.95,9.48,1.07,-1.99,8.79,1.11,-2.15,8.54,1.17,-1.99,8.52,1.03,-1.91,9.02,1.03,-1.95,9.02,1.06,-1.95,8.93,0.98,-2.35,8.99,1.03,-2.03,8.95,0.88,-2.31,9.13,0.94,-1.99,9.14,1.01,-1.99,9.05,1.01,-1.95,9.05,0.54,-2.35,9.35,0.57,-2.03,9.3,0.18,-2.07,9.48,0.18,-2.07,9.48,0,-2.03,9.49,-0.1,-2.23,9.52,-0.83,-1.87,8.86,-0.77,-1.83,9,-0.81,-1.75,8.88,-0.82,-1.99,8.88,-0.81,-1.95,8.88,-0.82,-1.95,8.85,-0.91,-1.87,7.96,-0.9,-1.71,7.81,-0.73,-1.95,7.68,-0.67,-1.67,7.39,-0.57,-1.79,7.5,-0.9,-1.71,7.81,-0.48,-2.03,7.47,-0.49,-1.99,7.52,-0.51,-1.91,7.47,0.34,-1.99,5.44,0.25,-1.99,5.45,0.29,-1.95,5.45,0.57,-1.95,5.45,0.71,-1.95,5.49,0.64,-2.11,5.47,1.33,-1.75,6.05,1.34,-1.87,5.97,1.17,-1.75,5.69,1.32,-2.11,5.91,1.34,-1.87,5.97,1.37,-1.87,6.24,1.48,-2.31,6.77,1.23,-1.87,6.92,1.14,-2.07,7.12,1.12,-1.91,7.06,1.07,-1.99,7.18,1.14,-2.07,7.12,1.14,-2.07,7.12,1.07,-1.99,7.18,1.08,-2.03,7.18,0.75,-2.03,7.52,0.78,-1.99,7.53,0.82,-2.07,7.58,0.89,-2.15,7.6,0.82,-2.07,7.58,0.89,-2.03,7.71,0.82,-2.07,7.58,0.94,-1.95,7.64,0.89,-2.03,7.71,0.92,-1.99,7.73,0.94,-1.95,7.64,0.97,-1.95,7.66,0.89,-2.03,7.71,0.98,-2.07,7.76,0.89,-2.15,7.6,1.06,-2.03,7.89,1.1,-2.15,7.82,0.98,-2.07,7.76,1.13,-2.07,7.91,1.33,-2.07,8.17,1.32,-2.19,8.2,1.34,-1.99,8.28,1.36,-1.95,8.37,1.36,-2.07,8.32,1.14,-1.75,8.8,1.08,-1.87,8.91,1.07,-1.99,8.79,1.01,-1.99,9.05,1.03,-2.03,8.95,1.03,-1.95,9.02,0.81,-1.71,9.27,0.69,-1.67,9.29,0.67,-1.71,9.31,0.09,-1.83,9.45,0.08,-1.95,9.48,0.25,-1.91,9.47,-0.31,-1.91,9.44,-0.35,-2.07,9.44,-0.17,-2.07,9.49,-0.56,-1.87,9.26,-0.35,-2.07,9.44,-0.31,-1.91,9.44,-0.84,-2.03,7.9,-0.91,-1.87,7.96,-0.73,-1.95,7.68,-0.57,-1.79,7.5,-0.73,-1.95,7.68,-0.9,-1.71,7.81,-0.49,-1.99,7.52,-0.73,-1.95,7.68,-0.51,-1.91,7.47,-0.66,-1.79,6.05,-0.6,-1.95,5.99,-0.77,-1.91,6.32,-0.01,-2.03,5.54,-0.04,-2.03,5.55,-0.01,-1.91,5.54,-0.01,-2.07,5.54,-0.01,-2.03,5.54,0.05,-2.07,5.51,0.34,-1.99,5.44,0.29,-2.07,5.44,0.25,-1.99,5.45,0.48,-2.03,5.4,0.34,-1.99,5.44,0.44,-1.95,5.42,0.46,-2.07,5.42,0.48,-2.03,5.4,0.53,-2.03,5.44,1.27,-1.95,5.8,1.32,-2.11,5.91,1.16,-2.11,5.69,1.54,-2.03,6.35,1.59,-2.03,6.45,1.54,-2.15,6.45,1.62,-1.95,6.32,1.56,-1.83,6.38,1.52,-1.87,6.46,1.14,-2.07,7.12,1.08,-2.03,7.18,1.05,-2.11,7.24,1.08,-2.03,7.18,1.07,-1.99,7.18,1.05,-1.99,7.2,1.08,-2.03,7.18,1.05,-1.99,7.2,1.05,-2.11,7.24,0.92,-1.95,7.37,0.88,-2.15,7.37,1.05,-2.11,7.24,0.81,-2.07,7.43,0.92,-1.95,7.37,0.84,-1.91,7.42,0.94,-1.95,7.64,0.92,-1.99,7.73,0.89,-2.03,7.71,0.89,-2.03,7.71,0.92,-1.99,7.73,0.98,-2.07,7.76,0.95,-1.99,7.82,0.98,-2.07,7.76,0.92,-1.99,7.73,1.13,-2.07,7.91,1.08,-1.99,7.98,1.33,-2.07,8.17,1.35,-2.15,8.22,1.34,-1.99,8.28,1.36,-2.07,8.32,1.03,-2.03,8.95,1.01,-1.99,9.05,0.88,-2.31,9.13,0.7,-2.19,9.22,0.94,-1.99,9.14,0.85,-1.91,9.23,0,-2.03,9.49,-0.08,-2.03,9.5,-0.1,-2.23,9.52,-0.08,-2.03,9.5,-0.12,-1.99,9.5,-0.17,-2.07,9.49,-0.73,-1.95,7.68,-0.57,-1.79,7.5,-0.51,-1.91,7.47,-0.49,-1.99,7.52,-0.48,-2.03,7.47,-0.55,-2.07,7.55,-0.28,-1.99,5.75,-0.6,-1.95,5.99,-0.48,-1.75,5.89,-0.01,-2.07,5.54,-0.04,-2.03,5.55,-0.01,-2.03,5.54,0.48,-2.03,5.4,0.46,-2.07,5.42,0.34,-1.99,5.44,0.64,-2.11,5.47,0.68,-2.27,5.48,0.42,-2.27,5.43,0.96,-2.19,5.69,1.02,-2.11,5.65,1.09,-2.27,5.72,1.59,-2.03,6.45,1.56,-2.03,6.5,1.54,-2.15,6.45,1.12,-1.91,7.06,1.04,-1.95,7.16,1.07,-1.99,7.18,0.75,-2.03,7.52,0.82,-2.07,7.58,0.73,-2.19,7.53,0.77,-2.23,7.54,0.73,-2.19,7.53,0.89,-2.15,7.6,1.33,-2.07,8.17,1.21,-1.91,8.22,1.34,-1.99,8.28,1.36,-2.07,8.32,1.36,-2.03,8.4,1.34,-2.07,8.42,1.35,-2.15,8.22,1.33,-2.07,8.17,1.34,-1.99,8.28,1.16,-2.39,8.31,1.24,-2.19,8.31,1.11,-2.15,8.54,1.01,-1.99,9.05,0.94,-1.99,9.14,0.88,-2.31,9.13,-0.04,-2.03,5.55,-0.01,-2.07,5.54,-0.09,-2.15,5.59,0.46,-2.07,5.42,0.53,-2.03,5.44,0.64,-2.11,5.47,1.02,-2.11,5.65,0.96,-2.19,5.69,0.89,-2.15,5.66,1.33,-2.31,8.07,1.1,-2.15,7.82,1.13,-2.07,7.91,1.35,-2.15,8.22,1.36,-2.07,8.32,1.34,-2.11,8.33,1.3,-2.15,8.31,1.35,-2.15,8.22,1.34,-2.11,8.33,0.82,-2.07,7.58,0.89,-2.15,7.6,0.73,-2.19,7.53,0.87,-2.31,7.62,0.98,-2.07,7.76,1.1,-2.15,7.82,1.1,-2.15,7.82,1.06,-2.03,7.89,1.13,-2.07,7.91,1.35,-2.15,8.22,1.32,-2.19,8.2,1.33,-2.07,8.17,1.17,-1.99,8.52,1.11,-2.15,8.54,1.2,-2.07,8.42,1.06,-1.95,8.93,1.03,-2.03,8.95,1.07,-1.99,8.79,0.29,-2.07,5.44,0.05,-2.07,5.51,0.25,-1.99,5.45,0.46,-2.07,5.42,0.29,-2.07,5.44,0.34,-1.99,5.44,0.46,-2.07,5.42,0.64,-2.11,5.47,0.42,-2.27,5.43,1.48,-2.31,6.77,1.54,-2.19,6.6,1.23,-1.87,6.92,1.54,-2.19,6.6,1.56,-2.03,6.5,1.4,-1.87,6.61,1,-2.31,7.24,1.05,-2.11,7.24,0.88,-2.15,7.37,0.77,-2.23,7.54,0.89,-2.15,7.6,0.87,-2.31,7.62,0.87,-2.31,7.62,0.89,-2.15,7.6,0.98,-2.07,7.76,1.33,-2.31,8.07,1.29,-2.39,8.02,1.1,-2.15,7.82,-0.04,-2.03,5.55,-0.28,-1.99,5.75,-0.01,-1.91,5.54,1.02,-2.11,5.65,1.16,-2.11,5.69,1.09,-2.27,5.72,1.3,-2.23,6.4,1.35,-2.51,5.96,1.32,-2.11,5.91,1.35,-2.51,5.96,1.29,-2.31,5.82,1.32,-2.11,5.91,1.48,-2.35,6.6,1.49,-2.27,6.53,1.54,-2.19,6.6,1.54,-2.19,6.6,1.54,-2.15,6.45,1.56,-2.03,6.5,1.48,-2.35,6.6,1.44,-2.31,6.56,1.49,-2.27,6.53,1.08,-1.91,8.02,1.2,-1.83,8.16,1.21,-1.91,8.22,1.24,-2.19,8.31,1.2,-2.07,8.42,1.11,-2.15,8.54,0.94,-1.99,9.14,0.7,-2.19,9.22,0.88,-2.31,9.13,0.64,-2.11,5.47,0.71,-1.95,5.49,0.89,-2.15,5.66,0.71,-1.95,5.49,0.86,-1.95,5.61,0.89,-2.15,5.66,1.09,-2.27,5.72,1.16,-2.11,5.69,1.29,-2.31,5.82,1.54,-2.19,6.6,1.49,-2.27,6.53,1.54,-2.15,6.45,0.81,-2.07,7.43,0.74,-2.11,7.41,0.88,-2.15,7.37,0.57,-2.03,9.3,0.7,-2.19,9.22,0.85,-1.91,9.23,-0.77,-1.75,6.69,-0.78,-1.63,6.42,-0.77,-1.91,6.32,0.46,-2.07,5.42,0.42,-2.27,5.43,0.29,-2.07,5.44,1.09,-2.27,5.72,0.99,-2.35,5.74,0.97,-2.31,5.71,1.09,-2.27,5.72,1.29,-2.31,5.82,1.11,-2.39,5.76,1.32,-2.27,6.5,1.3,-2.23,6.4,1.37,-2.15,6.46,0.54,-2.35,9.35,0.7,-2.19,9.22,0.57,-2.03,9.3,0.25,-1.99,5.45,0.05,-2.07,5.51,0.1,-1.87,5.48,0.96,-2.19,5.69,0.94,-2.27,5.7,0.89,-2.15,5.66,1.32,-2.11,5.91,1.29,-2.31,5.82,1.16,-2.11,5.69,1.3,-2.23,6.4,1.32,-2.11,5.91,1.37,-1.87,6.24,0.77,-2.35,7.36,0.88,-2.15,7.37,0.74,-2.11,7.41,0.94,-2.27,5.7,0.68,-2.27,5.48,0.89,-2.15,5.66,0.77,-2.35,7.36,1,-2.31,7.24,0.88,-2.15,7.37,0.05,-2.07,5.51,0.29,-2.07,5.44,0.06,-2.31,5.52,1.35,-2.39,6.63,1.29,-2.31,6.48,1.32,-2.27,6.5,1.05,-2.11,7.24,1,-2.31,7.24,1.14,-2.07,7.12,0.71,-2.35,7.39,0.77,-2.35,7.36,0.74,-2.11,7.41,1.32,-2.27,6.5,1.29,-2.31,6.48,1.3,-2.23,6.4,1.48,-2.35,6.6,1.48,-2.31,6.77,1.49,-2.43,6.74,1.48,-2.35,6.6,1.54,-2.19,6.6,1.48,-2.31,6.77,0.98,-2.35,8.99,1.07,-1.99,8.79,1.03,-2.03,8.95,1.16,-2.39,8.31,1.32,-2.19,8.2,1.24,-2.19,8.31,1.16,-2.39,8.31,1.33,-2.31,8.07,1.32,-2.19,8.2,0.98,-2.35,8.99,1.11,-2.15,8.54,1.07,-1.99,8.79,1.16,-2.51,6.98,1.48,-2.31,6.77,1.14,-2.07,7.12,1.16,-2.51,6.98,1.14,-2.07,7.12,1,-2.31,7.24,1.59,-1.03,6.05,1.55,-0.99,6.02,1.52,-0.99,6.07])

IndexedFaceSet310.setCoord(Coordinate311)

Shape306.setGeometry(IndexedFaceSet310)

Transform305.addChildren(Shape306)

fieldValue304.addChildren(Transform305)

ProtoInstance302.addFieldValue(fieldValue304)

fieldValue301.addChildren(ProtoInstance302)
ProtoInstance312 = ProtoInstance()
ProtoInstance312.setName("Joint")
ProtoInstance312.setDEF("Allen_hanim_l_hip")
fieldValue313 = fieldValue()
fieldValue313.setName("name")
fieldValue313.setValue("l_hip")

ProtoInstance312.addFieldValue(fieldValue313)
fieldValue314 = fieldValue()
fieldValue314.setName("center")
fieldValue314.setValue("0.122 0.888271 -0.0693267")

ProtoInstance312.addFieldValue(fieldValue314)
fieldValue315 = fieldValue()
fieldValue315.setName("children")
ProtoInstance316 = ProtoInstance()
ProtoInstance316.setName("Segment")
ProtoInstance316.setDEF("Allen_hanim_l_thigh")
fieldValue317 = fieldValue()
fieldValue317.setName("name")
fieldValue317.setValue("l_thigh")

ProtoInstance316.addFieldValue(fieldValue317)
fieldValue318 = fieldValue()
fieldValue318.setName("children")
Transform319 = Transform()
Transform319.setDEF("l_thigh_adjust")
Transform319.setCenter([-0.7,1.1,0.04])
Transform319.setRotation([0,1,0,1.570796])
Transform319.setScale([0.1,0.1,0.1])
Shape320 = Shape()
Appearance321 = Appearance()
Material322 = Material()
Material322.setUSE("Pants_Color")

Appearance321.setMaterial(Material322)
ImageTexture323 = ImageTexture()
ImageTexture323.setUSE("camo")

Appearance321.setTexture(ImageTexture323)

Shape320.setAppearance(Appearance321)
IndexedFaceSet324 = IndexedFaceSet()
IndexedFaceSet324.setCoordIndex([0,1,2,-1,3,4,5,-1,6,7,8,-1,9,10,11,-1,12,13,14,-1,15,16,17,-1,18,19,20,-1,21,22,23,-1,24,25,26,-1,27,28,29,-1,30,31,32,-1,33,34,35,-1,36,37,38,-1,39,40,41,-1,42,43,44,-1,45,46,47,-1,48,49,50,-1,51,52,53,-1,54,55,56,-1,57,58,59,-1,60,61,62,-1,63,64,65,-1,66,67,68,-1,69,70,71,-1,72,73,74,-1,75,76,77,-1,78,79,80,-1,81,82,83,-1,84,85,86,-1,87,88,89,-1,90,91,92,-1,93,94,95,-1,96,97,98,-1,99,100,101,-1,102,103,104,-1,105,106,107,-1,108,109,110,-1,111,112,113,-1,114,115,116,-1,117,118,119,-1,120,121,122,-1,123,124,125,-1,126,127,128,-1,129,130,131,-1,132,133,134,-1,135,136,137,-1,138,139,140,-1,141,142,143,-1,144,145,146,-1,147,148,149,-1,150,151,152,-1,153,154,155,-1,156,157,158,-1,159,160,161,-1,162,163,164,-1,165,166,167,-1,168,169,170,-1,171,172,173,-1,174,175,176,-1,177,178,179,-1,180,181,182,-1,183,184,185,-1,181,183,182,-1,183,185,182,-1,183,158,184,-1,157,159,158,-1,164,165,162,-1,167,168,165,-1,165,168,162,-1,172,174,173,-1,176,179,174,-1,174,179,173,-1,179,178,173,-1,182,185,178,-1,178,185,173,-1,185,184,173,-1,184,158,173,-1,158,159,173,-1,170,173,168,-1,159,161,173,-1,173,161,168,-1,162,168,161,-1,186,187,188,-1,189,190,191,-1,192,193,194,-1,195,196,197,-1,198,199,200,-1,201,202,203,-1,204,205,206,-1,207,208,209,-1,210,211,212,-1,213,214,215,-1,216,217,218,-1,219,220,221,-1,222,223,224,-1,225,226,227,-1,228,229,230,-1,231,232,233,-1,234,235,236,-1,237,238,239,-1,240,241,242,-1,243,244,245,-1,246,247,248,-1,249,250,251,-1,252,253,254,-1,255,256,257,-1,258,259,260,-1,261,262,263,-1,264,265,266,-1,267,268,269,-1,270,271,272,-1,273,274,275,-1,276,277,278,-1,279,280,281,-1,282,283,284,-1,285,286,287,-1,288,289,290,-1,291,292,293,-1,294,295,296,-1,297,298,299,-1,300,301,302,-1,303,304,305,-1,306,307,308,-1,309,310,311,-1,312,313,314,-1,315,316,317,-1,318,319,320,-1,321,322,323,-1,324,325,326,-1,327,328,329,-1,330,331,332,-1,333,334,335,-1,336,337,338,-1,339,340,341,-1,342,343,344,-1,345,346,347,-1,348,349,350,-1,351,352,353,-1,354,355,356,-1,357,358,359,-1,360,361,362,-1,363,364,365,-1,366,367,368,-1,369,370,371,-1,372,373,374,-1,375,376,377,-1,378,379,380,-1,381,382,383,-1,384,385,386,-1,387,388,389,-1,390,391,392,-1,393,394,395,-1,396,397,398,-1,399,400,401,-1,402,403,404,-1,405,406,407,-1,408,409,410,-1,411,412,413,-1,414,415,416,-1,417,418,419,-1,420,421,422,-1,423,424,425,-1,426,427,428,-1,429,430,431,-1,432,433,434,-1,435,436,437,-1,438,439,440,-1,441,442,443,-1,444,445,446,-1,447,448,449,-1,450,451,452,-1,453,454,455,-1,456,457,458,-1,459,460,461,-1,462,463,464,-1,465,466,467,-1,468,469,470,-1,471,472,473,-1,474,475,476,-1,477,478,479,-1,480,481,482,-1,483,484,485,-1,486,487,488,-1,489,490,491,-1,492,493,494,-1,495,496,497,-1,498,499,500,-1,501,502,503,-1,504,505,506,-1,507,508,509,-1,510,511,512,-1,513,514,515,-1,516,517,518,-1,519,520,521,-1,522,523,524,-1,525,526,527,-1,528,529,530,-1,531,532,533,-1,534,535,536,-1,537,538,539,-1,540,541,542,-1,543,544,545,-1,546,547,548,-1,549,550,551,-1,552,553,554,-1,555,556,557,-1,558,559,560,-1,561,562,563,-1,564,565,566,-1,567,568,569,-1,570,571,572,-1,573,574,575,-1,576,577,578,-1,579,580,581,-1,582,583,584,-1,585,586,587,-1,588,589,590,-1,591,592,593,-1,594,595,596,-1,597,598,599,-1,600,601,602,-1,603,604,605,-1,606,607,608,-1,609,610,611,-1,612,613,614,-1,615,616,617,-1,618,619,620,-1,621,622,623,-1,624,625,626,-1,627,628,629,-1,630,631,632,-1,633,634,635,-1,636,637,638,-1,639,640,641,-1,642,643,644,-1,645,646,647,-1,648,649,650,-1,651,652,653,-1,654,655,656,-1,657,658,659,-1,660,661,662,-1,663,664,665,-1,666,667,668,-1,669,670,671,-1,672,673,674,-1,675,676,677,-1,678,679,680,-1,681,682,683,-1,684,685,686,-1,687,688,689,-1,690,691,692,-1,693,694,695,-1,696,697,698,-1,699,700,701,-1,702,703,704,-1,705,706,707,-1,708,709,710,-1,711,712,713,-1,714,715,716,-1,717,718,719,-1,720,721,722,-1,723,724,725,-1,726,727,728,-1,729,730,731,-1,732,733,734,-1,735,736,737,-1,738,739,740,-1,741,742,743,-1,744,745,746,-1,747,748,749,-1,750,751,752,-1,753,754,755,-1,756,757,758,-1,759,760,761,-1,762,763,764,-1,765,766,767,-1,768,769,770,-1,771,772,773,-1,774,775,776,-1,777,778,779,-1,780,781,782,-1,783,784,785,-1,786,787,788,-1,789,790,791,-1,792,793,794,-1,795,796,797,-1,798,799,800,-1,801,802,803,-1,804,805,806,-1,807,808,809,-1,810,811,812,-1,813,814,815,-1,816,817,818,-1,819,820,821,-1,822,823,824,-1,825,826,827,-1,828,829,830,-1,831,832,833,-1,834,835,836,-1,837,838,839,-1,840,841,842,-1,843,844,845,-1,846,847,848,-1,849,850,851,-1,852,853,854,-1,855,856,857,-1,858,859,860,-1,861,862,863,-1,864,865,866,-1,867,868,869,-1,870,871,872,-1,873,874,875,-1,876,877,878,-1,879,880,881,-1,882,883,884,-1,885,886,887,-1,888,889,890,-1,891,892,893,-1,894,895,896,-1,897,898,899,-1,900,901,902,-1,903,904,905,-1,906,907,908,-1,909,910,911,-1,912,913,914,-1,915,916,917,-1,918,919,920,-1,921,922,923,-1,924,925,926,-1,927,928,929,-1,930,931,932,-1,933,934,935,-1,936,937,938,-1,939,940,941,-1,942,943,944,-1,945,946,947,-1,948,949,950,-1,951,952,953,-1,954,955,956,-1,957,958,959,-1,960,961,962,-1,963,964,965,-1,966,967,968,-1,969,970,971,-1,972,973,974,-1,975,976,977,-1,978,979,980,-1,981,982,983,-1,984,985,986,-1,987,988,989,-1,990,991,992,-1,993,994,995,-1,996,997,998,-1,999,1000,1001,-1,1002,1003,1004,-1,1005,1006,1007,-1,1008,1009,1010,-1,1011,1012,1013,-1,1014,1015,1016,-1,1017,1018,1019,-1,1020,1021,1022,-1,1023,1024,1025,-1,1026,1027,1028,-1,1029,1030,1031,-1,1032,1033,1034,-1,1035,1036,1037,-1,1038,1039,1040,-1,1041,1042,1043,-1,1044,1045,1046,-1,1047,1048,1049,-1,1050,1051,1052,-1,1053,1054,1055,-1,1056,1057,1058,-1,1059,1060,1061,-1,1062,1063,1064,-1,1065,1066,1067,-1,1068,1069,1070,-1,1071,1072,1073,-1,1074,1075,1076,-1,1077,1078,1079,-1,1080,1081,1082,-1,1083,1084,1085,-1,1086,1087,1088,-1,1089,1090,1091,-1,1092,1093,1094,-1,1095,1096,1097,-1,1098,1099,1100,-1,1101,1102,1103,-1,1104,1105,1106,-1,1107,1108,1109,-1,1110,1111,1112,-1,1113,1114,1115,-1,1116,1117,1118,-1,1119,1120,1121,-1,1122,1123,1124,-1,1125,1126,1127,-1,1128,1129,1130,-1,1131,1132,1133,-1,1134,1135,1136,-1,1137,1138,1139,-1,1140,1141,1142,-1,1143,1144,1145,-1,1146,1147,1148,-1,1149,1150,1151,-1,1152,1153,1154,-1,1155,1156,1157,-1,1158,1159,1160,-1,1161,1162,1163,-1,1164,1165,1166,-1,1167,1168,1169,-1,1170,1171,1172,-1,1173,1174,1175,-1,1176,1177,1178,-1,1179,1180,1181,-1,1182,1183,1184,-1,1185,1186,1187,-1,1188,1189,1190,-1,1191,1192,1193,-1,1194,1195,1196,-1,1197,1198,1199,-1,1200,1201,1202,-1,1203,1204,1205,-1,1206,1207,1208,-1,1209,1210,1211,-1,1212,1213,1214,-1,1215,1216,1217,-1,1218,1219,1220,-1,1221,1222,1223,-1,1224,1225,1226,-1,1227,1228,1229,-1,1230,1231,1232,-1,1233,1234,1235,-1,1236,1237,1238,-1,1239,1240,1241,-1,1242,1243,1244,-1,1245,1246,1247,-1,1248,1249,1250,-1,1251,1252,1253,-1,1254,1255,1256,-1,1257,1258,1259,-1,1260,1261,1262,-1,1263,1264,1265,-1,1266,1267,1268,-1,1269,1270,1271,-1,1272,1273,1274,-1,1275,1276,1277,-1,1278,1279,1280,-1,1281,1282,1283,-1,1284,1285,1286,-1,1287,1288,1289,-1,1290,1291,1292,-1,1293,1294,1295,-1,1296,1297,1298,-1,1299,1300,1301,-1,1302,1303,1304,-1,1305,1306,1307,-1,1308,1309,1310,-1,1311,1312,1313,-1,1314,1315,1316,-1,1317,1318,1319,-1,1320,1321,1322,-1,1323,1324,1325,-1,1326,1327,1328,-1,1329,1330,1331,-1,1332,1333,1334,-1,1335,1336,1337,-1,1338,1339,1340,-1,1341,1342,1343,-1,1344,1345,1346,-1,1347,1348,1349,-1,1350,1351,1352,-1,1353,1354,1355,-1,1356,1357,1358,-1,1359,1360,1361,-1,1362,1363,1364,-1,1365,1366,1367,-1,1368,1369,1370,-1,1371,1372,1373,-1,1374,1375,1376,-1,1377,1378,1379,-1,1380,1381,1382,-1,1383,1384,1385,-1,1386,1387,1388,-1,1389,1390,1391,-1,1392,1393,1394,-1,1395,1396,1397,-1,1398,1399,1400,-1,1401,1402,1403,-1,1404,1405,1406,-1,1407,1408,1409,-1,1410,1411,1412,-1,1413,1414,1415,-1,1416,1417,1418,-1,1419,1420,1421,-1,1422,1423,1424,-1,1425,1426,1427,-1,1428,1429,1430,-1,1431,1432,1433,-1,1434,1435,1436,-1,1437,1438,1439,-1,1440,1441,1442,-1,1443,1444,1445,-1,1446,1447,1448,-1,1449,1450,1451,-1,1452,1453,1454,-1,1455,1456,1457,-1,1458,1459,1460,-1,1461,1462,1463,-1,1464,1465,1466,-1,1467,1468,1469,-1,1470,1471,1472,-1,1473,1474,1475,-1,1476,1477,1478,-1,1479,1480,1481,-1,1482,1483,1484,-1,1485,1486,1487,-1,1488,1489,1490,-1,1491,1492,1493,-1,1494,1495,1496,-1,1497,1498,1499,-1,1500,1501,1502,-1,1503,1504,1505,-1,1506,1507,1508,-1,1509,1510,1511,-1,1512,1513,1514,-1,1515,1516,1517,-1,1518,1519,1520,-1,1521,1522,1523,-1,1524,1525,1526,-1,1527,1528,1529,-1,1530,1531,1532,-1,1533,1534,1535,-1,1536,1537,1538,-1,1539,1540,1541,-1,1542,1543,1544,-1,1545,1546,1547,-1,1548,1549,1550,-1])
IndexedFaceSet324.setCreaseAngle(1.32)
Coordinate325 = Coordinate()
Coordinate325.setPoint([-1.07,-2.63,8.17,-1.06,-2.95,8.05,-1.04,-2.99,8.19,-1.06,-2.95,8.05,-1.1,-2.63,8.08,-1.09,-2.91,7.89,-0.69,-2.87,7.09,-0.88,-3.03,7.36,-0.87,-2.75,7.21,-0.96,-2.79,8.42,-0.96,-2.75,8.39,-1.02,-2.87,8.31,-1.07,-2.79,7.67,-1.04,-2.75,7.54,-1.04,-2.79,7.54,-1.04,-2.79,7.54,-1.03,-2.79,7.51,-1.03,-2.83,7.52,-1.03,-2.83,7.52,-0.98,-2.83,7.43,-0.99,-2.99,7.51,-0.95,-2.79,8.45,-0.97,-2.87,8.43,-0.87,-2.87,8.65,-0.95,-2.79,8.45,-0.96,-2.79,8.42,-0.97,-2.87,8.43,-1.02,-2.87,8.31,-1.07,-2.63,8.17,-1.04,-2.99,8.19,-0.97,-2.87,8.43,-0.96,-2.79,8.42,-1.02,-2.87,8.31,-1.04,-2.79,7.54,-1.03,-2.83,7.52,-1.03,-2.91,7.63,-0.31,-2.87,9.03,-0.49,-2.87,8.97,-0.24,-3.03,9.06,-1.07,-2.99,7.98,-1.06,-2.95,8.05,-1.09,-2.91,7.89,-1.07,-2.99,7.98,-1.09,-2.91,7.89,-1.02,-3.19,7.67,-1.04,-2.79,7.54,-1.03,-2.91,7.63,-1.07,-2.79,7.67,-1.03,-2.83,7.52,-1.03,-2.79,7.51,-0.98,-2.83,7.43,-0.69,-2.87,7.09,-0.55,-2.95,7.06,-0.61,-2.99,7.08,0.53,-3.31,8.84,0.39,-3.15,8.89,0.06,-3.71,9.03,-1.03,-2.91,7.63,-1.03,-2.83,7.52,-0.99,-2.99,7.51,-0.88,-3.03,7.36,-0.98,-2.83,7.43,-0.87,-2.75,7.21,0.63,-3.03,7.07,0.72,-3.11,7.16,0.55,-3.15,7.1,-0.23,-2.83,9.04,-0.31,-2.87,9.03,-0.24,-3.03,9.06,-1.09,-2.91,7.89,-1.1,-2.67,7.76,-1.07,-2.79,7.67,-1.09,-2.91,7.89,-1.03,-2.91,7.63,-1.02,-3.19,7.67,-1.07,-2.99,8.05,-1.07,-2.99,7.98,-1.05,-3.23,8.01,-0.99,-2.99,7.51,-0.98,-2.83,7.43,-0.88,-3.03,7.36,-1.07,-2.99,8.05,-1.04,-2.99,8.19,-1.06,-2.95,8.05,-1.04,-2.99,8.19,-1.05,-3.23,8.01,-1.02,-3.19,8.35,-1.07,-2.99,7.98,-1.07,-2.99,8.05,-1.06,-2.95,8.05,-0.99,-2.99,7.51,-1.02,-3.19,7.67,-1.03,-2.91,7.63,-0.58,-2.99,6.95,-0.53,-3.07,7.07,-0.55,-2.99,7.06,0.74,-3.11,8.67,0.56,-2.99,8.76,0.53,-3.31,8.84,-0.7,-2.67,8.79,-0.87,-2.87,8.65,-0.78,-3.07,8.8,-0.7,-2.67,8.79,-0.78,-3.07,8.8,-0.62,-3.07,8.92,-0.73,-3.35,8.81,-0.78,-3.07,8.8,-1.02,-3.19,8.35,-1.04,-2.99,8.19,-1.02,-3.19,8.35,-1.02,-2.87,8.31,-1.07,-2.99,7.98,-1.02,-3.19,7.67,-1.05,-3.23,8.01,-1.04,-2.99,8.19,-1.07,-2.99,8.05,-1.05,-3.23,8.01,-0.88,-3.55,7.44,-1.02,-3.19,7.67,-0.88,-3.03,7.36,-0.55,-2.95,7.06,-0.55,-2.99,7.06,-0.61,-2.99,7.08,1.02,-3.19,7.84,0.97,-2.95,8.08,0.97,-3.43,8.12,0.04,-2.87,9.02,-0.24,-3.03,9.06,-0.07,-3.39,9.04,-0.7,-2.67,8.79,-0.62,-3.07,8.92,-0.49,-2.87,8.97,-0.48,-3.15,7.07,-0.58,-3.19,7.1,-0.53,-3.07,7.07,-0.61,-2.99,7.08,-0.55,-2.99,7.06,-0.53,-3.07,7.07,0.96,-2.95,7.36,1.15,-3.19,7.55,0.85,-3.39,7.29,-0.97,-2.87,8.43,-1.02,-3.19,8.35,-0.87,-2.87,8.65,-1.09,-2.91,7.89,-1.07,-2.79,7.67,-1.03,-2.91,7.63,-0.53,-3.07,7.07,-0.58,-3.19,7.1,-0.61,-2.99,7.08,-0.53,-3.15,6.99,-0.48,-3.15,7.07,-0.53,-3.07,7.07,-0.58,-2.99,6.95,-0.53,-3.15,6.99,-0.53,-3.07,7.07,0.53,-3.23,7.11,0.49,-3.19,7.1,0.55,-3.15,7.1,0.55,-3.43,7.17,0.58,-3.51,7.22,0.49,-3.55,7.21,0.49,-3.67,7.25,0.53,-3.79,7.33,0.38,-3.75,7.29,0.38,-3.75,7.29,0.32,-3.83,7.29,0.23,-3.79,7.28,0.58,-3.51,7.22,0.52,-3.59,7.22,0.49,-3.55,7.21,0.27,-3.99,7.29,0.18,-3.95,7.28,0.26,-3.91,7.3,0.25,-4.07,7.27,0.19,-4.19,7.28,0.14,-4.15,7.27,-0.09,-4.19,7.21,-0.08,-3.99,7.17,0.06,-4.03,7.18,-0.69,-2.87,7.09,-0.63,-2.83,7.01,-0.55,-2.95,7.06,-0.63,-2.83,7.01,-0.59,-2.95,6.96,-0.55,-2.95,7.06,0.61,-3.51,8.76,0.84,-3.15,8.52,0.74,-3.11,8.67,0.61,-3.51,8.76,0.34,-4.31,8.97,0.86,-3.63,8.54,-0.62,-3.07,8.92,-0.24,-3.03,9.06,-0.49,-2.87,8.97,-0.88,-3.03,7.36,-0.58,-3.19,7.1,-0.67,-3.39,7.19,0.85,-3.39,7.29,0.72,-3.11,7.16,0.96,-2.95,7.36,0.97,-3.43,8.12,1.1,-3.55,7.66,1.02,-3.19,7.84,0.86,-3.63,8.54,0.98,-3.71,8.36,0.97,-3.43,8.12,-0.07,-3.39,9.04,0.39,-3.15,8.89,0.04,-2.87,9.02,-1.02,-3.19,8.35,-0.97,-2.87,8.43,-1.02,-2.87,8.31,1.02,-3.19,7.84,1.15,-3.19,7.55,1.19,-3.11,7.61,0.34,-4.31,8.97,0.87,-4.27,8.46,0.86,-3.63,8.54,-0.24,-3.03,9.06,-0.62,-3.07,8.92,-0.07,-3.39,9.04,-0.73,-3.35,8.81,-0.62,-3.07,8.92,-0.78,-3.07,8.8,-1.02,-3.19,8.35,-0.78,-3.07,8.8,-0.87,-2.87,8.65,-0.48,-3.39,7.11,-0.67,-3.39,7.19,-0.58,-3.19,7.1,-0.69,-2.87,7.09,-0.61,-2.99,7.08,-0.88,-3.03,7.36,0.55,-3.43,7.17,0.46,-3.35,7.12,0.53,-3.23,7.11,0.53,-3.23,7.11,0.55,-3.15,7.1,0.72,-3.11,7.16,-0.37,-3.71,8.96,-0.62,-3.07,8.92,-0.73,-3.35,8.81,0.34,-4.31,8.97,0.73,-4.47,8.63,0.87,-4.27,8.46,0.85,-3.39,7.29,0.55,-3.43,7.17,0.53,-3.23,7.11,1.15,-3.19,7.55,1.12,-3.39,7.5,0.85,-3.39,7.29,0.97,-2.95,8.08,0.84,-3.15,8.52,0.97,-3.43,8.12,0.84,-3.15,8.52,0.86,-3.63,8.54,0.97,-3.43,8.12,-0.62,-3.07,8.92,-0.37,-3.71,8.96,-0.07,-3.39,9.04,-0.88,-3.55,7.44,-0.99,-3.55,7.7,-1.02,-3.19,7.67,0.58,-3.51,7.22,0.55,-3.43,7.17,0.85,-3.39,7.29,1.12,-3.39,7.5,0.82,-3.55,7.31,0.85,-3.39,7.29,1.1,-3.55,7.66,1.12,-3.39,7.5,1.02,-3.19,7.84,0.53,-3.31,8.84,0.61,-3.51,8.76,0.74,-3.11,8.67,-1.02,-3.19,7.67,-0.99,-2.99,7.51,-0.88,-3.03,7.36,1.12,-3.39,7.5,1.1,-3.55,7.66,0.98,-3.75,7.45,-1.05,-3.23,8.01,-1.03,-3.51,8.21,-1.02,-3.19,8.35,-0.48,-3.39,7.11,-0.58,-3.19,7.1,-0.48,-3.15,7.07,-0.34,-3.43,7.07,-0.34,-3.43,7.11,-0.35,-3.39,7.1,-0.34,-3.43,7.07,-0.35,-3.39,7.1,-0.39,-3.35,7.07,0.58,-3.51,7.22,0.85,-3.39,7.29,0.82,-3.55,7.31,0.82,-3.55,7.31,1.12,-3.39,7.5,0.98,-3.75,7.45,0.56,-2.99,8.76,0.39,-3.15,8.89,0.53,-3.31,8.84,-0.55,-3.79,7.21,-0.67,-3.39,7.19,-0.48,-3.39,7.11,-0.39,-3.35,7.07,-0.35,-3.39,7.1,-0.48,-3.39,7.11,-0.31,-3.47,7.06,-0.29,-3.47,7.12,-0.34,-3.43,7.11,-0.34,-3.43,7.11,-0.34,-3.43,7.07,-0.31,-3.47,7.06,0.43,-4.11,7.36,0.39,-3.83,7.32,0.53,-3.79,7.33,0.39,-3.15,8.89,-0.07,-3.39,9.04,0.06,-3.71,9.03,-0.99,-3.55,7.7,-1.05,-3.23,8.01,-1.02,-3.19,7.67,-1,-3.87,7.92,-0.78,-4.07,7.45,-0.94,-4.35,7.78,-0.34,-3.43,7.11,-0.38,-3.51,7.12,-0.48,-3.39,7.11,-0.38,-3.51,7.12,-0.29,-3.47,7.12,-0.28,-3.51,7.12,-0.34,-3.43,7.11,-0.29,-3.47,7.12,-0.38,-3.51,7.12,-0.25,-3.51,7.11,-0.28,-3.51,7.12,-0.29,-3.47,7.12,0.85,-3.39,7.29,0.53,-3.23,7.11,0.72,-3.11,7.16,1.12,-3.39,7.5,1.15,-3.19,7.55,1.02,-3.19,7.84,0.84,-3.15,8.52,0.61,-3.51,8.76,0.86,-3.63,8.54,-1.02,-3.71,8.14,-0.93,-3.95,8.44,-0.85,-3.75,8.64,-1,-3.87,7.92,-0.99,-3.55,7.7,-0.78,-4.07,7.45,-0.67,-3.39,7.19,-0.88,-3.55,7.44,-0.88,-3.03,7.36,-0.35,-3.39,7.1,-0.34,-3.43,7.11,-0.48,-3.39,7.11,-0.28,-3.51,7.12,-0.31,-3.59,7.13,-0.38,-3.51,7.12,-0.39,-3.35,7.07,-0.48,-3.39,7.11,-0.48,-3.15,7.07,-0.3,-3.55,7.03,-0.29,-3.59,7.04,-0.31,-3.59,7.13,-0.3,-3.55,7.03,-0.31,-3.59,7.13,-0.28,-3.51,7.12,0.49,-3.67,7.25,0.47,-3.63,7.23,0.52,-3.59,7.22,0.58,-3.51,7.22,0.58,-3.63,7.26,0.52,-3.59,7.22,0.53,-3.79,7.33,0.98,-3.75,7.45,0.97,-3.91,7.5,-0.29,-3.59,7.04,-0.23,-3.59,7.13,-0.31,-3.59,7.13,-0.23,-3.59,7.13,-0.24,-3.75,7.16,-0.31,-3.59,7.13,0.49,-3.67,7.25,0.52,-3.59,7.22,0.58,-3.63,7.26,0.82,-3.55,7.31,0.58,-3.63,7.26,0.58,-3.51,7.22,-0.07,-3.39,9.04,-0.37,-3.71,8.96,0.06,-3.71,9.03,-0.31,-3.59,7.13,-0.24,-3.75,7.16,-0.55,-3.79,7.21,0.53,-3.79,7.33,0.39,-3.83,7.32,0.38,-3.75,7.29,-1.02,-3.71,8.14,-1.03,-3.51,8.21,-0.99,-3.55,7.7,-0.88,-3.03,7.36,-0.61,-2.99,7.08,-0.58,-3.19,7.1,-1,-3.87,7.92,-0.94,-4.35,7.78,-0.99,-4.47,8.14,-0.16,-3.67,7.11,-0.24,-3.75,7.16,-0.23,-3.59,7.13,0.49,-3.67,7.25,0.58,-3.63,7.26,0.53,-3.79,7.33,-0.85,-3.75,8.64,-0.37,-3.71,8.96,-0.73,-3.35,8.81,-1.03,-3.51,8.21,-1.05,-3.23,8.01,-0.99,-3.55,7.7,-0.31,-3.59,7.13,-0.55,-3.79,7.21,-0.38,-3.51,7.12,1,-4.47,8.34,1.07,-4.55,8.04,1.06,-4.35,7.87,0.97,-3.43,8.12,1.08,-3.71,7.97,1.1,-3.55,7.66,0.98,-3.71,8.36,1.08,-3.71,7.97,0.97,-3.43,8.12,-0.08,-4.07,9.02,-0.75,-4.07,8.71,-0.73,-4.39,8.7,-0.15,-3.83,7.16,-0.24,-3.75,7.16,-0.16,-3.67,7.11,0.32,-3.83,7.29,0.38,-3.75,7.29,0.39,-3.83,7.32,0.53,-3.79,7.33,0.58,-3.63,7.26,0.98,-3.75,7.45,1.08,-3.71,7.97,0.98,-3.75,7.45,1.1,-3.55,7.66,-1.03,-3.51,8.21,-0.85,-3.75,8.64,-0.73,-3.35,8.81,-0.09,-3.83,7.13,-0.15,-3.83,7.16,-0.16,-3.67,7.11,0.32,-3.83,7.29,0.26,-3.91,7.3,0.22,-3.87,7.29,0.43,-4.11,7.36,0.3,-4.19,7.31,0.25,-4.07,7.27,0.43,-4.11,7.36,0.86,-4.19,7.5,0.46,-4.51,7.42,1.03,-4.27,7.71,0.97,-3.91,7.5,1.08,-3.71,7.97,-0.55,-3.79,7.21,-0.48,-3.39,7.11,-0.38,-3.51,7.12,-0.21,-3.95,7.18,-0.34,-4.31,7.27,-0.52,-4.15,7.28,1.08,-3.71,7.97,0.97,-3.91,7.5,0.98,-3.75,7.45,-1.03,-3.51,8.21,-1.02,-3.71,8.14,-0.85,-3.75,8.64,-1.03,-3.51,8.21,-0.73,-3.35,8.81,-1.02,-3.19,8.35,-0.55,-3.79,7.21,-0.78,-4.07,7.45,-0.88,-3.55,7.44,-0.13,-3.91,7.17,-0.21,-3.95,7.18,-0.15,-3.83,7.16,-0.04,-3.95,7.17,-0.09,-3.95,7.17,-0.13,-3.91,7.17,0.43,-4.11,7.36,0.25,-4.07,7.27,0.27,-3.99,7.29,0.86,-4.19,7.5,0.43,-4.11,7.36,0.53,-3.79,7.33,-0.85,-3.75,8.64,-0.93,-3.95,8.44,-0.75,-4.07,8.71,-0.52,-4.15,7.28,-0.78,-4.07,7.45,-0.55,-3.79,7.21,-0.21,-3.95,7.18,-0.09,-4.19,7.21,-0.34,-4.31,7.27,-0.21,-3.95,7.18,-0.55,-3.79,7.21,-0.24,-3.75,7.16,-0.09,-3.95,7.17,-0.21,-3.95,7.18,-0.13,-3.91,7.17,0.26,-3.91,7.3,0.32,-3.83,7.29,0.39,-3.83,7.32,0.97,-3.91,7.5,0.86,-4.19,7.5,0.53,-3.79,7.33,-0.08,-4.07,9.02,0.03,-4.31,9.01,0.34,-4.31,8.97,0.06,-3.71,9.03,-0.08,-4.07,9.02,0.34,-4.31,8.97,-0.08,-4.07,9.02,-0.37,-3.71,8.96,-0.75,-4.07,8.71,-0.99,-3.55,7.7,-0.88,-3.55,7.44,-0.78,-4.07,7.45,-0.67,-3.39,7.19,-0.55,-3.79,7.21,-0.88,-3.55,7.44,-0.21,-3.95,7.18,-0.24,-3.75,7.16,-0.15,-3.83,7.16,-0.09,-3.95,7.17,-0.08,-3.99,7.17,-0.21,-3.95,7.18,0.25,-4.07,7.27,0.2,-4.03,7.27,0.27,-3.99,7.29,1.06,-4.35,7.87,1.08,-3.71,7.97,1.05,-3.95,8.26,-0.08,-4.07,9.02,-0.73,-4.39,8.7,-0.57,-4.55,8.81,-0.75,-4.07,8.71,-0.94,-4.15,8.37,-0.73,-4.39,8.7,-0.08,-3.99,7.17,-0.09,-4.19,7.21,-0.21,-3.95,7.18,0.25,-4.07,7.27,0.3,-4.19,7.31,0.19,-4.19,7.28,0.43,-4.11,7.36,0.27,-3.99,7.29,0.39,-3.83,7.32,0.27,-3.99,7.29,0.26,-3.91,7.3,0.39,-3.83,7.32,1.03,-4.27,7.71,0.86,-4.19,7.5,0.97,-3.91,7.5,-1.02,-3.71,8.14,-0.99,-3.55,7.7,-1,-3.87,7.92,-0.94,-4.15,8.37,-1,-3.87,7.92,-0.99,-4.47,8.14,-0.78,-4.07,7.45,-0.52,-4.15,7.28,-0.79,-4.43,7.56,-0.52,-4.15,7.28,-0.34,-4.31,7.27,-0.79,-4.43,7.56,1.04,-4.15,8.3,1.02,-4.27,8.36,1.06,-4.35,7.87,0.34,-4.31,8.97,0.43,-4.51,8.96,0.73,-4.47,8.63,0.14,-4.15,7.27,0.19,-4.19,7.28,0.16,-4.27,7.26,0.58,-3.63,7.26,0.82,-3.55,7.31,0.98,-3.75,7.45,0.87,-4.27,8.46,1.04,-4.15,8.3,1.05,-3.95,8.26,0.87,-4.27,8.46,1.02,-4.27,8.36,1.04,-4.15,8.3,0.61,-3.51,8.76,0.06,-3.71,9.03,0.34,-4.31,8.97,0.87,-4.27,8.46,1.05,-3.95,8.26,0.98,-3.71,8.36,0.01,-4.27,7.21,-0.09,-4.19,7.21,0.06,-4.03,7.18,-0.08,-4.07,9.02,0.06,-3.71,9.03,-0.37,-3.71,8.96,-0.15,-4.55,8.88,0.03,-4.31,9.01,-0.08,-4.07,9.02,-0.92,-4.87,8.32,-0.77,-4.91,8.51,-0.73,-4.39,8.7,-1,-3.87,7.92,-0.94,-4.15,8.37,-0.93,-3.95,8.44,-0.73,-4.39,8.7,-0.94,-4.15,8.37,-0.99,-4.47,8.14,0.01,-4.27,7.21,0.02,-4.31,7.22,-0.06,-4.31,7.23,0.19,-4.19,7.28,0.3,-4.19,7.31,0.16,-4.27,7.26,0.3,-4.19,7.31,0.43,-4.11,7.36,0.46,-4.51,7.42,0.98,-3.71,8.36,1.05,-3.95,8.26,1.08,-3.71,7.97,-1.02,-3.71,8.14,-1,-3.87,7.92,-0.93,-3.95,8.44,-0.09,-4.19,7.21,0.01,-4.27,7.21,-0.06,-4.31,7.23,1.06,-4.35,7.87,1.03,-4.27,7.71,1.08,-3.71,7.97,0.43,-4.51,8.96,0.03,-4.31,9.01,-0.15,-4.55,8.88,-0.77,-4.91,8.51,-0.61,-4.91,8.76,-0.57,-4.55,8.81,-0.79,-4.43,7.56,-0.94,-4.35,7.78,-0.78,-4.07,7.45,0.1,-4.27,7.21,0.01,-4.27,7.21,0.06,-4.03,7.18,-0.75,-4.07,8.71,-0.93,-3.95,8.44,-0.94,-4.15,8.37,-0.06,-4.31,7.23,0.02,-4.31,7.22,-0.01,-4.59,7.31,-0.01,-4.59,7.31,0.48,-4.83,7.4,-0.22,-5.03,7.37,1.02,-4.27,8.36,1,-4.47,8.34,1.06,-4.35,7.87,1.07,-4.75,8.12,1,-4.47,8.34,0.85,-4.79,8.65,0.45,-4.71,8.98,0.43,-4.51,8.96,-0.15,-4.55,8.88,-0.15,-4.55,8.88,-0.08,-4.07,9.02,-0.57,-4.55,8.81,0.16,-4.27,7.26,-0.01,-4.59,7.31,0.02,-4.31,7.22,0.87,-4.27,8.46,1,-4.47,8.34,1.02,-4.27,8.36,0.73,-4.47,8.63,0.43,-4.51,8.96,0.73,-4.83,8.82,-0.73,-4.39,8.7,-0.77,-4.91,8.51,-0.57,-4.55,8.81,-0.28,-4.71,7.32,-0.5,-4.99,7.49,-0.77,-4.79,7.66,-0.21,-3.95,7.18,-0.52,-4.15,7.28,-0.55,-3.79,7.21,-0.27,-4.51,7.29,-0.06,-4.31,7.23,-0.01,-4.59,7.31,-0.06,-4.31,7.23,-0.27,-4.51,7.29,-0.34,-4.31,7.27,0.73,-4.55,7.59,0.97,-4.67,7.75,0.83,-5.19,7.74,1.07,-4.91,8.12,0.85,-4.79,8.65,1.05,-5.19,8.27,-0.61,-4.91,8.76,-0.41,-4.91,8.88,-0.57,-4.55,8.81,-0.85,-3.75,8.64,-0.75,-4.07,8.71,-0.37,-3.71,8.96,-0.92,-4.87,8.32,-0.73,-4.39,8.7,-0.99,-4.47,8.14,-0.94,-4.35,7.78,-0.98,-4.71,8.02,-0.99,-4.47,8.14,-0.01,-4.59,7.31,-0.22,-5.03,7.37,-0.28,-4.71,7.32,1.03,-4.27,7.71,0.73,-4.55,7.59,0.86,-4.19,7.5,1.07,-4.75,8.12,0.85,-4.79,8.65,1.07,-4.91,8.12,-0.28,-4.71,7.32,-0.77,-4.79,7.66,-0.79,-4.43,7.56,-0.09,-4.19,7.21,-0.06,-4.31,7.23,-0.34,-4.31,7.27,1.03,-4.27,7.71,0.97,-4.67,7.75,0.73,-4.55,7.59,1.07,-4.75,8.12,1.07,-4.55,8.04,1,-4.47,8.34,0.61,-3.51,8.76,0.53,-3.31,8.84,0.06,-3.71,9.03,0.87,-4.27,8.46,0.98,-3.71,8.36,0.86,-3.63,8.54,-0.15,-4.55,8.88,-0.41,-4.91,8.88,0.09,-5.03,9,0.16,-4.27,7.26,0.46,-4.51,7.42,-0.01,-4.59,7.31,1.06,-4.35,7.87,1.07,-4.55,8.04,0.97,-4.67,7.75,0.45,-4.71,8.98,-0.15,-4.55,8.88,0.09,-5.03,9,0.86,-4.19,7.5,0.73,-4.55,7.59,0.46,-4.51,7.42,0.46,-4.51,7.42,0.48,-4.83,7.4,-0.01,-4.59,7.31,1.03,-4.27,7.71,1.06,-4.35,7.87,0.97,-4.67,7.75,1.05,-3.95,8.26,1.04,-4.15,8.3,1.06,-4.35,7.87,0.87,-4.27,8.46,0.73,-4.47,8.63,1,-4.47,8.34,-0.98,-4.99,8.1,-0.92,-4.87,8.32,-0.98,-4.71,8.02,-0.34,-4.31,7.27,-0.27,-4.51,7.29,-0.79,-4.43,7.56,0.73,-4.47,8.63,0.85,-4.79,8.65,1,-4.47,8.34,-0.92,-4.87,8.32,-0.86,-4.99,8.39,-0.77,-4.91,8.51,-0.5,-4.99,7.49,-0.8,-5.43,7.9,-0.85,-5.11,7.86,0.46,-4.51,7.42,0.73,-4.55,7.59,0.48,-4.83,7.4,-0.27,-4.51,7.29,-0.01,-4.59,7.31,-0.28,-4.71,7.32,0.43,-4.51,8.96,0.45,-4.71,8.98,0.73,-4.83,8.82,-0.98,-4.99,8.1,-0.96,-5.15,8.2,-0.93,-4.99,8.29,0.43,-4.51,8.96,0.34,-4.31,8.97,0.03,-4.31,9.01,-0.77,-4.91,8.51,-0.71,-5.07,8.61,-0.61,-4.91,8.76,-0.57,-4.55,8.81,-0.41,-4.91,8.88,-0.15,-4.55,8.88,-0.92,-4.87,8.32,-0.99,-4.47,8.14,-0.98,-4.71,8.02,0.73,-4.47,8.63,0.73,-4.83,8.82,0.85,-4.79,8.65,-0.92,-4.87,8.32,-0.93,-4.99,8.29,-0.86,-4.99,8.39,-0.77,-4.79,7.66,-0.98,-4.71,8.02,-0.94,-4.35,7.78,-0.88,-4.95,7.83,-0.5,-4.99,7.49,-0.85,-5.11,7.86,-0.28,-4.71,7.32,-0.22,-5.03,7.37,-0.5,-4.99,7.49,0.16,-4.27,7.26,0.3,-4.19,7.31,0.46,-4.51,7.42,0.85,-4.79,8.65,0.96,-5.19,8.55,1.05,-5.19,8.27,-0.86,-5.03,8.39,-0.86,-4.99,8.39,-0.93,-4.99,8.29,-0.92,-4.87,8.32,-0.98,-4.99,8.1,-0.93,-4.99,8.29,-0.77,-4.79,7.66,-0.88,-4.95,7.83,-0.98,-4.71,8.02,0.64,-5.43,7.58,0.29,-5.43,7.53,0.48,-4.83,7.4,1.07,-4.55,8.04,1.07,-4.75,8.12,0.97,-4.67,7.75,0.74,-5.39,8.89,0.96,-5.19,8.55,0.63,-5.03,8.94,0.45,-4.71,8.98,0.09,-5.03,9,0.54,-5.15,8.97,0.63,-5.03,8.94,0.73,-4.83,8.82,0.45,-4.71,8.98,-0.27,-4.51,7.29,-0.28,-4.71,7.32,-0.79,-4.43,7.56,0.09,-5.03,9,0.42,-5.51,8.91,0.54,-5.15,8.97,-0.86,-5.03,8.39,-0.84,-5.03,8.42,-0.86,-4.99,8.39,-0.87,-5.11,8.39,-0.93,-4.99,8.29,-0.96,-5.15,8.2,-0.88,-4.95,7.83,-0.98,-4.99,8.1,-0.98,-4.71,8.02,1.06,-5.11,8.02,0.83,-5.19,7.74,0.97,-4.67,7.75,0.63,-5.03,8.94,0.45,-4.71,8.98,0.54,-5.15,8.97,0.09,-5.03,9,-0.18,-5.39,8.98,0.42,-5.51,8.91,-0.84,-5.03,8.42,-0.86,-5.03,8.39,-0.87,-5.11,8.39,-0.94,-4.35,7.78,-0.79,-4.43,7.56,-0.77,-4.79,7.66,0.96,-5.19,8.55,0.85,-4.79,8.65,0.73,-4.83,8.82,-0.61,-4.91,8.76,-0.32,-5.27,8.92,-0.41,-4.91,8.88,-0.86,-4.99,8.39,-0.84,-5.03,8.42,-0.77,-4.91,8.51,1.06,-5.11,8.02,1.07,-4.91,8.12,1.05,-5.19,8.27,1.05,-5.71,8.49,1.06,-5.59,8.43,0.91,-5.47,8.77,-0.97,-5.31,8.14,-0.85,-5.11,7.86,-0.8,-5.43,7.9,-0.41,-4.91,8.88,-0.32,-5.27,8.92,0.09,-5.03,9,-0.87,-5.11,8.39,-0.86,-5.03,8.39,-0.93,-4.99,8.29,-0.97,-5.31,8.14,-0.96,-5.15,8.2,-0.85,-5.11,7.86,-0.96,-5.15,8.2,-0.98,-4.99,8.1,-0.85,-5.11,7.86,0.29,-5.43,7.53,-0.08,-5.43,7.41,0.48,-4.83,7.4,0.97,-4.67,7.75,1.07,-4.75,8.12,1.07,-4.91,8.12,0.74,-5.39,8.89,0.91,-5.47,8.77,0.96,-5.19,8.55,-0.71,-5.07,8.61,-0.84,-5.03,8.42,-0.87,-5.11,8.39,-0.96,-5.15,8.2,-0.97,-5.31,8.14,-0.9,-5.27,8.35,1.05,-5.19,8.27,1.06,-5.59,8.43,1,-5.43,7.99,0.63,-5.51,8.87,0.74,-5.39,8.89,0.54,-5.15,8.97,-0.93,-5.47,8.28,-0.97,-5.31,8.14,-0.89,-5.59,8.06,-0.08,-5.43,7.41,-0.5,-4.99,7.49,-0.22,-5.03,7.37,0.81,-5.55,7.69,1,-5.43,7.99,0.97,-5.63,7.9,0.91,-5.47,8.77,0.76,-5.47,8.9,0.74,-5.55,8.88,0.42,-5.51,8.91,0.63,-5.51,8.87,0.54,-5.15,8.97,0.96,-5.19,8.55,0.73,-4.83,8.82,0.63,-5.03,8.94,0.54,-5.15,8.97,0.74,-5.39,8.89,0.63,-5.03,8.94,-0.71,-5.07,8.61,-0.77,-4.91,8.51,-0.84,-5.03,8.42,-0.9,-5.27,8.35,-0.87,-5.11,8.39,-0.96,-5.15,8.2,-0.51,-5.59,8.62,-0.9,-5.27,8.35,-0.93,-5.47,8.28,0.09,-5.03,9,-0.32,-5.27,8.92,-0.18,-5.39,8.98,-0.97,-5.31,8.14,-0.93,-5.47,8.28,-0.9,-5.27,8.35,0.81,-5.55,7.69,0.64,-5.43,7.58,0.83,-5.19,7.74,1.06,-5.11,8.02,0.97,-4.67,7.75,1.07,-4.91,8.12,1.06,-5.11,8.02,1.05,-5.19,8.27,1,-5.43,7.99,1.06,-5.59,8.43,1.05,-5.71,8.49,1.03,-5.91,8.11,1.06,-5.11,8.02,1,-5.43,7.99,0.83,-5.19,7.74,-0.25,-5.55,8.88,-0.18,-5.39,8.98,-0.32,-5.27,8.92,-0.85,-5.11,7.86,-0.98,-4.99,8.1,-0.88,-4.95,7.83,0.83,-5.19,7.74,1,-5.43,7.99,0.81,-5.55,7.69,1.06,-5.59,8.43,1.03,-5.91,8.11,0.97,-5.63,7.9,-0.93,-5.47,8.28,-0.86,-5.67,8.31,-0.72,-5.71,8.44,-0.61,-4.91,8.76,-0.71,-5.07,8.61,-0.32,-5.27,8.92,-0.8,-5.43,7.9,-0.89,-5.59,8.06,-0.97,-5.31,8.14,-0.01,-5.59,7.43,-0.08,-5.43,7.41,0.29,-5.43,7.53,0.64,-5.43,7.58,0.43,-5.91,7.66,0.29,-5.43,7.53,1,-5.43,7.99,1.06,-5.59,8.43,0.97,-5.63,7.9,-0.41,-5.67,8.73,-0.25,-5.55,8.88,-0.32,-5.27,8.92,-0.51,-5.59,8.62,-0.93,-5.47,8.28,-0.72,-5.71,8.44,-0.51,-5.59,8.62,-0.71,-5.07,8.61,-0.9,-5.27,8.35,0.76,-5.47,8.9,0.74,-5.39,8.89,0.63,-5.51,8.87,0.48,-4.83,7.4,0.73,-4.55,7.59,0.83,-5.19,7.74,0.63,-5.51,8.87,0.36,-5.91,9,0.74,-5.71,8.83,-0.88,-4.95,7.83,-0.77,-4.79,7.66,-0.5,-4.99,7.49,-0.08,-5.43,7.41,-0.22,-5.03,7.37,0.48,-4.83,7.4,-0.1,-5.59,9,-0.2,-5.75,8.95,0.1,-5.83,8.92,-0.94,-5.63,8.14,-0.67,-5.87,8.09,-0.89,-5.79,8.22,-0.67,-5.87,8.09,-0.89,-5.59,8.06,-0.8,-5.43,7.9,-0.21,-5.67,7.5,-0.08,-5.43,7.41,-0.01,-5.59,7.43,0.91,-5.47,8.77,0.93,-5.71,8.79,1.05,-5.71,8.49,0.91,-5.47,8.77,0.74,-5.55,8.88,0.93,-5.71,8.79,0.63,-5.51,8.87,0.74,-5.71,8.83,0.74,-5.55,8.88,-0.1,-5.59,9,-0.25,-5.55,8.88,-0.2,-5.75,8.95,-0.51,-5.59,8.62,-0.62,-5.87,8.7,-0.41,-5.67,8.73,-0.94,-5.63,8.14,-0.97,-5.75,8.27,-0.86,-5.67,8.31,-0.93,-5.47,8.28,-0.89,-5.59,8.06,-0.94,-5.63,8.14,-0.21,-5.67,7.5,-0.8,-5.43,7.9,-0.5,-4.99,7.49,-0.67,-5.87,8.09,-0.76,-6.07,8.45,-0.84,-5.91,8.3,-0.21,-5.67,7.5,-0.01,-5.59,7.43,-0.07,-5.99,7.5,1.05,-5.71,8.49,0.93,-5.71,8.79,0.99,-5.79,8.76,1.06,-5.59,8.43,0.96,-5.19,8.55,0.91,-5.47,8.77,1.05,-5.19,8.27,0.96,-5.19,8.55,1.06,-5.59,8.43,0.91,-5.47,8.77,0.74,-5.39,8.89,0.76,-5.47,8.9,0.36,-5.91,9,0.42,-5.51,8.91,0.1,-5.83,8.92,0.42,-5.51,8.91,-0.1,-5.59,9,0.1,-5.83,8.92,-0.51,-5.59,8.62,-0.41,-5.67,8.73,-0.32,-5.27,8.92,-0.41,-5.67,8.73,-0.48,-5.91,8.78,-0.34,-5.87,8.87,-0.71,-5.07,8.61,-0.87,-5.11,8.39,-0.9,-5.27,8.35,0.81,-6.19,7.79,0.43,-6.23,7.7,0.79,-5.91,7.74,-0.18,-5.39,8.98,-0.1,-5.59,9,0.42,-5.51,8.91,-0.18,-5.39,8.98,-0.25,-5.55,8.88,-0.1,-5.59,9,-0.72,-5.71,8.44,-0.89,-5.83,8.41,-0.8,-5.83,8.49,-0.94,-5.63,8.14,-0.86,-5.67,8.31,-0.93,-5.47,8.28,-0.01,-5.59,7.43,0.07,-5.99,7.46,-0.07,-5.99,7.5,0.63,-5.51,8.87,0.42,-5.51,8.91,0.36,-5.91,9,-0.71,-5.07,8.61,-0.51,-5.59,8.62,-0.32,-5.27,8.92,-0.62,-5.87,8.7,-0.72,-5.71,8.44,-0.8,-5.83,8.49,-0.97,-5.75,8.27,-0.89,-5.79,8.22,-0.93,-5.83,8.3,-0.89,-5.79,8.22,-0.97,-5.75,8.27,-0.94,-5.63,8.14,1.05,-5.71,8.49,0.99,-5.79,8.76,1.07,-5.83,8.55,0.86,-5.99,8.81,1,-5.91,8.77,0.99,-5.79,8.76,0.74,-5.71,8.83,0.93,-5.71,8.79,0.74,-5.55,8.88,0.1,-5.83,8.92,-0.2,-5.75,8.95,-0.07,-5.99,8.93,-0.62,-5.87,8.7,-0.51,-5.59,8.62,-0.72,-5.71,8.44,-0.72,-5.71,8.44,-0.86,-5.67,8.31,-0.89,-5.83,8.41,-0.8,-5.83,8.49,-0.89,-5.83,8.41,-0.89,-5.87,8.45,-0.89,-5.79,8.22,-0.67,-5.87,8.09,-0.84,-5.91,8.3,-0.94,-5.63,8.14,-0.89,-5.59,8.06,-0.67,-5.87,8.09,-0.86,-5.67,8.31,-0.93,-5.83,8.3,-0.89,-5.83,8.41,-0.97,-5.75,8.27,-0.93,-5.83,8.3,-0.86,-5.67,8.31,-0.37,-5.95,7.91,-0.21,-5.67,7.5,-0.07,-5.99,7.5,1.03,-5.91,8.11,0.97,-5.91,7.9,0.96,-5.83,7.87,0.97,-5.91,7.9,1.03,-5.91,8.11,1.05,-6.11,8.1,1.11,-6.07,8.35,1.07,-5.83,8.55,1.04,-5.95,8.72,0.99,-5.79,8.76,1,-5.91,8.77,1.07,-5.83,8.55,1,-5.91,8.77,1.04,-5.95,8.72,1.07,-5.83,8.55,-0.62,-5.87,8.7,-0.48,-5.91,8.78,-0.41,-5.67,8.73,-0.34,-5.87,8.87,-0.48,-5.91,8.78,-0.42,-6.19,8.7,-0.89,-5.79,8.22,-0.84,-5.91,8.3,-0.93,-5.83,8.3,-0.67,-5.87,8.09,-0.46,-6.23,8.38,-0.76,-6.07,8.45,-0.37,-6.03,8.03,-0.67,-5.87,8.09,-0.37,-5.95,7.91,0.64,-5.43,7.58,0.48,-4.83,7.4,0.83,-5.19,7.74,1.11,-6.07,8.35,1.08,-6.23,8.19,1.05,-6.11,8.1,1.11,-6.07,8.35,1.04,-5.95,8.72,1.05,-6.11,8.73,0.14,-6.03,8.97,0.1,-5.83,8.92,-0.02,-6.03,8.93,-0.34,-5.87,8.87,-0.2,-5.75,8.95,-0.41,-5.67,8.73,-0.34,-5.87,8.87,-0.22,-5.95,8.89,-0.2,-5.75,8.95,-0.62,-5.87,8.7,-0.74,-6.03,8.6,-0.66,-6.07,8.62,-0.89,-5.99,8.49,-0.88,-5.95,8.54,-0.89,-5.87,8.45,-0.84,-5.91,8.3,-0.89,-5.87,8.45,-0.89,-5.83,8.41,-0.37,-6.03,8.03,-0.37,-5.95,7.91,-0.21,-6.31,7.93,0.97,-5.63,7.9,0.96,-5.83,7.87,0.81,-5.55,7.69,0.86,-5.99,8.81,0.93,-5.71,8.79,0.74,-5.71,8.83,-0.2,-5.75,8.95,-0.22,-5.95,8.89,-0.07,-5.99,8.93,-0.09,-6.03,8.91,-0.07,-5.99,8.93,-0.22,-5.95,8.89,-0.8,-5.83,8.49,-0.89,-5.87,8.45,-0.88,-5.95,8.54,-0.84,-5.91,8.3,-0.76,-6.07,8.45,-0.89,-5.99,8.49,-0.84,-5.91,8.3,-0.89,-5.99,8.49,-0.89,-5.87,8.45,-0.08,-5.43,7.41,-0.21,-5.67,7.5,-0.5,-4.99,7.49,0.64,-5.43,7.58,0.81,-5.55,7.69,0.43,-5.91,7.66,0.79,-5.91,7.74,0.96,-5.83,7.87,0.97,-5.91,7.9,0.86,-5.99,8.81,0.99,-5.79,8.76,0.93,-5.71,8.79,0.74,-5.71,8.83,0.36,-5.91,9,0.46,-6.07,9,0.86,-5.99,8.81,0.97,-5.99,8.78,1,-5.91,8.77,-0.2,-5.75,8.95,-0.25,-5.55,8.88,-0.41,-5.67,8.73,-0.66,-6.07,8.62,-0.75,-6.15,8.75,-0.52,-6.11,8.66,-0.67,-5.87,8.09,-0.8,-5.43,7.9,-0.37,-5.95,7.91,-0.8,-5.43,7.9,-0.21,-5.67,7.5,-0.37,-5.95,7.91,-0.07,-5.99,7.5,0.07,-5.99,7.46,0.1,-6.23,7.49,0.96,-5.83,7.87,0.79,-5.91,7.74,0.81,-5.55,7.69,1.03,-5.91,8.11,0.96,-5.83,7.87,0.97,-5.63,7.9,0.36,-5.91,9,0.1,-5.83,8.92,0.14,-6.03,8.97,-0.89,-5.99,8.49,-0.88,-6.03,8.53,-0.88,-5.95,8.54,-0.93,-5.83,8.3,-0.84,-5.91,8.3,-0.89,-5.83,8.41,-0.01,-5.59,7.43,0.43,-5.91,7.66,0.07,-5.99,7.46,0.43,-6.23,7.7,0.43,-5.91,7.66,0.79,-5.91,7.74,1.03,-5.91,8.11,1.11,-6.07,8.35,1.05,-6.11,8.1,1.05,-6.11,8.73,1.04,-5.95,8.72,0.97,-5.99,8.78,1.04,-5.95,8.72,1,-5.91,8.77,0.97,-5.99,8.78,0.56,-6.39,8.99,0,-6.19,8.85,0,-6.39,8.88,0.46,-6.07,9,0.36,-5.91,9,0.14,-6.03,8.97,0.1,-5.83,8.92,-0.07,-5.99,8.93,-0.02,-6.03,8.93,-0.51,-6.27,8.8,-0.42,-6.19,8.7,-0.52,-6.11,8.66,-0.48,-5.91,8.78,-0.52,-6.11,8.66,-0.42,-6.19,8.7,-0.83,-6.11,8.58,-0.74,-6.03,8.6,-0.88,-6.03,8.53,-0.88,-6.03,8.53,-0.74,-6.03,8.6,-0.88,-5.95,8.54,-0.89,-5.99,8.49,-0.76,-6.07,8.45,-0.88,-6.03,8.53,-0.76,-6.07,8.45,-0.46,-6.23,8.38,-0.47,-6.31,8.49,-0.01,-5.59,7.43,0.29,-5.43,7.53,0.43,-5.91,7.66,0.81,-5.55,7.69,0.79,-5.91,7.74,0.43,-5.91,7.66,1.05,-6.11,8.73,0.97,-5.99,8.78,0.91,-6.19,8.85,-0.09,-6.03,8.91,-0.02,-6.03,8.93,-0.07,-5.99,8.93,-0.15,-6.15,8.8,-0.09,-6.03,8.91,-0.22,-5.95,8.89,-0.22,-5.95,8.89,-0.34,-5.87,8.87,-0.42,-6.19,8.7,-0.62,-5.87,8.7,-0.8,-5.83,8.49,-0.74,-6.03,8.6,-0.84,-6.11,8.64,-0.74,-6.03,8.6,-0.83,-6.11,8.58,-0.76,-6.19,8.64,-0.83,-6.11,8.58,-0.76,-6.07,8.45,-0.76,-6.07,8.45,-0.83,-6.11,8.58,-0.88,-6.03,8.53,0.1,-6.23,7.49,0.43,-6.23,7.7,0.11,-6.39,7.5,-0.07,-5.99,7.5,0.1,-6.23,7.49,-0.02,-6.27,7.54,0.97,-5.91,7.9,0.95,-6.03,7.88,0.79,-5.91,7.74,1.05,-6.19,8.1,1.04,-6.19,8.07,1.05,-6.11,8.1,1.08,-6.23,8.19,1.05,-6.19,8.1,1.05,-6.11,8.1,-0.09,-6.03,8.91,-0.15,-6.15,8.8,0,-6.19,8.85,-0.28,-6.35,8.83,-0.15,-6.15,8.8,-0.42,-6.19,8.7,-0.52,-6.11,8.66,-0.75,-6.15,8.75,-0.65,-6.23,8.84,-0.52,-6.11,8.66,-0.62,-5.87,8.7,-0.66,-6.07,8.62,-0.52,-6.11,8.66,-0.48,-5.91,8.78,-0.62,-5.87,8.7,-0.74,-6.03,8.6,-0.8,-5.83,8.49,-0.88,-5.95,8.54,-0.74,-6.03,8.6,-0.84,-6.11,8.64,-0.76,-6.19,8.64,-0.76,-6.19,8.64,-0.76,-6.07,8.45,-0.62,-6.27,8.68,-0.84,-6.11,8.64,-0.83,-6.11,8.58,-0.76,-6.19,8.64,-0.67,-5.87,8.09,-0.37,-6.03,8.03,-0.46,-6.23,8.38,-0.02,-6.27,7.54,-0.07,-6.27,7.65,-0.07,-5.99,7.5,0.1,-6.23,7.49,0.43,-5.91,7.66,0.43,-6.23,7.7,0.95,-6.03,7.88,0.81,-6.19,7.79,0.79,-5.91,7.74,1.08,-6.23,8.19,1.05,-6.23,8.1,1.05,-6.19,8.1,-0.02,-6.03,8.93,0,-6.19,8.85,0.14,-6.03,8.97,-0.02,-6.03,8.93,-0.09,-6.03,8.91,0,-6.19,8.85,-0.22,-5.95,8.89,-0.42,-6.19,8.7,-0.15,-6.15,8.8,-0.37,-6.03,8.03,-0.21,-6.31,7.93,-0.37,-6.39,8.26,1.05,-5.71,8.49,1.07,-5.83,8.55,1.03,-5.91,8.11,1.11,-6.07,8.35,1.05,-6.11,8.73,1.12,-6.31,8.63,0.97,-5.99,8.78,0.86,-5.99,8.81,0.91,-6.19,8.85,-0.66,-6.07,8.62,-0.74,-6.03,8.6,-0.76,-6.19,8.64,0,-6.31,7.52,0.1,-6.23,7.49,0.11,-6.39,7.5,0.95,-6.03,7.88,0.97,-5.91,7.9,1.05,-6.11,8.1,1.04,-6.19,8.07,1.05,-6.19,8.1,1.05,-6.23,8.1,1.07,-5.83,8.55,1.11,-6.07,8.35,1.03,-5.91,8.11,0.56,-6.39,8.99,0.14,-6.03,8.97,0,-6.19,8.85,-0.15,-6.15,8.8,-0.22,-6.35,8.85,0,-6.19,8.85,-0.46,-6.23,8.38,-0.37,-6.03,8.03,-0.37,-6.39,8.26,0,-6.31,7.52,-0.02,-6.31,7.54,-0.02,-6.27,7.54,0.1,-6.23,7.49,0,-6.31,7.52,-0.02,-6.27,7.54,1.04,-6.19,8.07,1.05,-6.23,8.1,1.01,-6.27,8.02,1.05,-6.11,8.1,1.04,-6.19,8.07,0.95,-6.03,7.88,0.81,-6.19,7.79,0.95,-6.03,7.88,1.01,-6.27,8.02,0.46,-6.07,9,0.87,-6.35,8.9,0.91,-6.19,8.85,-0.75,-6.15,8.75,-0.66,-6.07,8.62,-0.76,-6.19,8.64,-0.07,-6.27,7.65,-0.21,-6.31,7.93,-0.37,-5.95,7.91,-0.07,-6.27,7.65,-0.37,-5.95,7.91,-0.07,-5.99,7.5,-0.07,-6.27,7.65,-0.02,-6.27,7.54,-0.02,-6.31,7.54,1.04,-6.19,8.07,1.01,-6.27,8.02,0.95,-6.03,7.88,0.91,-6.19,8.85,1.12,-6.31,8.63,1.05,-6.11,8.73,1.08,-6.23,8.19,1.11,-6.07,8.35,1.12,-6.31,8.63,0.56,-6.39,8.99,0.46,-6.07,9,0.14,-6.03,8.97,-0.51,-6.27,8.8,-0.52,-6.11,8.66,-0.65,-6.23,8.84,0.46,-6.07,9,0.91,-6.19,8.85,0.86,-5.99,8.81,0.86,-5.99,8.81,0.74,-5.71,8.83,0.46,-6.07,9,-0.07,-6.27,7.65,-0.02,-6.31,7.54,-0.01,-6.39,7.54,-0.22,-6.35,8.85,0,-6.39,8.88,0,-6.19,8.85,0.1,-6.23,7.49,0.07,-5.99,7.46,0.43,-5.91,7.66,-0.28,-6.35,8.83,-0.22,-6.35,8.85,-0.15,-6.15,8.8,0.91,-6.19,8.85,0.87,-6.35,8.9,1.12,-6.31,8.63,0.46,-6.07,9,0.56,-6.39,8.99,0.87,-6.35,8.9])

IndexedFaceSet324.setCoord(Coordinate325)

Shape320.setGeometry(IndexedFaceSet324)

Transform319.addChildren(Shape320)

fieldValue318.addChildren(Transform319)

ProtoInstance316.addFieldValue(fieldValue318)

fieldValue315.addChildren(ProtoInstance316)
ProtoInstance326 = ProtoInstance()
ProtoInstance326.setName("Joint")
ProtoInstance326.setDEF("Allen_hanim_l_knee")
fieldValue327 = fieldValue()
fieldValue327.setName("name")
fieldValue327.setValue("l_knee")

ProtoInstance326.addFieldValue(fieldValue327)
fieldValue328 = fieldValue()
fieldValue328.setName("center")
fieldValue328.setValue("0.0738 0.517 -0.0284")

ProtoInstance326.addFieldValue(fieldValue328)
fieldValue329 = fieldValue()
fieldValue329.setName("children")
ProtoInstance330 = ProtoInstance()
ProtoInstance330.setName("Segment")
ProtoInstance330.setDEF("Allen_hanim_l_calf")
fieldValue331 = fieldValue()
fieldValue331.setName("name")
fieldValue331.setValue("l_calf")

ProtoInstance330.addFieldValue(fieldValue331)
fieldValue332 = fieldValue()
fieldValue332.setName("children")
Transform333 = Transform()
Transform333.setDEF("l_calf_adjust")
Transform333.setCenter([-0.012,1.1,-0.01])
Transform333.setRotation([0,1,0,1.570796])
Transform333.setScale([0.1,0.1,0.1])
Shape334 = Shape()
Appearance335 = Appearance()
Material336 = Material()
Material336.setUSE("Pants_Color")

Appearance335.setMaterial(Material336)
ImageTexture337 = ImageTexture()
ImageTexture337.setUSE("camo")

Appearance335.setTexture(ImageTexture337)

Shape334.setAppearance(Appearance335)
IndexedFaceSet338 = IndexedFaceSet()
IndexedFaceSet338.setCoordIndex([4,5,2,-1,19,13,20,-1,20,13,12,-1,14,21,9,-1,22,23,24,-1,4,0,28,-1,29,15,6,-1,30,6,16,-1,30,29,6,-1,18,17,31,-1,11,27,26,-1,27,10,3,-1,33,34,23,-1,22,33,23,-1,35,36,37,-1,38,39,40,-1,38,18,39,-1,18,31,41,-1,42,13,19,-1,43,44,19,-1,9,45,46,-1,23,47,24,-1,29,30,48,-1,16,49,30,-1,50,51,52,-1,51,50,53,-1,35,37,54,-1,36,55,56,-1,36,35,55,-1,57,55,35,-1,39,57,40,-1,39,58,55,-1,59,41,60,-1,3,2,5,-1,61,22,24,-1,34,62,23,-1,48,63,62,-1,16,8,49,-1,7,25,52,-1,7,52,64,-1,65,64,51,-1,53,37,36,-1,50,37,53,-1,56,55,58,-1,66,56,58,-1,41,27,60,-1,39,18,41,-1,31,26,27,-1,59,60,67,-1,4,68,5,-1,69,68,4,-1,32,44,28,-1,43,19,20,-1,61,21,14,-1,47,70,21,-1,47,23,70,-1,62,63,23,-1,8,71,49,-1,57,39,55,-1,72,43,20,-1,22,61,14,-1,61,24,47,-1,63,73,23,-1,29,48,62,-1,52,51,64,-1,74,66,58,-1,58,59,67,-1,1,46,20,-1,75,70,76,-1,61,47,21,-1,70,73,77,-1,8,7,71,-1,71,7,64,-1,65,51,78,-1,51,79,78,-1,49,71,80,-1,81,51,53,-1,74,82,66,-1,66,83,56,-1,59,58,39,-1,9,21,45,-1,49,80,84,-1,85,86,74,-1,60,27,3,-1,69,4,28,-1,43,72,87,-1,88,89,75,-1,90,63,91,-1,78,84,80,-1,65,78,80,-1,51,81,79,-1,92,79,81,-1,93,92,81,-1,94,84,78,-1,94,78,79,-1,94,95,96,-1,94,92,95,-1,94,79,92,-1,92,93,95,-1,93,74,86,-1,97,60,3,-1,98,99,100,-1,45,21,70,-1,101,77,90,-1,23,73,70,-1,84,102,49,-1,95,93,86,-1,97,68,103,-1,68,3,5,-1,1,9,46,-1,104,98,89,-1,75,89,100,-1,75,45,70,-1,84,105,102,-1,106,323,107,-1,39,41,59,-1,58,67,108,-1,68,97,3,-1,100,99,46,-1,76,77,101,-1,63,48,91,-1,49,102,109,-1,110,98,104,-1,87,111,112,-1,104,89,112,-1,77,73,90,-1,113,102,105,-1,113,105,106,-1,106,107,113,-1,68,69,103,-1,46,99,20,-1,114,86,115,-1,115,85,116,-1,69,28,43,-1,99,72,20,-1,72,111,87,-1,117,112,89,-1,88,118,119,-1,45,100,46,-1,120,101,90,-1,109,48,30,-1,113,107,121,-1,113,121,122,-1,115,121,107,-1,122,121,123,-1,121,115,123,-1,123,115,116,-1,115,86,85,-1,28,44,43,-1,98,100,89,-1,117,89,88,-1,118,124,125,-1,88,75,76,-1,45,75,100,-1,73,63,90,-1,126,90,91,-1,91,127,128,-1,127,129,128,-1,49,109,30,-1,127,122,130,-1,130,122,123,-1,131,108,132,-1,133,131,134,-1,85,74,58,-1,131,133,108,-1,133,135,116,-1,111,104,112,-1,76,101,124,-1,136,126,91,-1,137,116,135,-1,133,116,85,-1,138,139,140,-1,141,87,112,-1,142,69,87,-1,70,77,76,-1,120,90,126,-1,101,120,124,-1,48,109,91,-1,102,143,109,-1,109,143,127,-1,144,135,145,-1,134,145,133,-1,108,85,58,-1,133,85,108,-1,41,31,27,-1,67,60,97,-1,143,122,127,-1,146,130,324,-1,146,127,130,-1,145,135,133,-1,67,140,147,-1,141,112,117,-1,120,148,125,-1,149,150,128,-1,151,134,152,-1,152,131,153,-1,103,67,97,-1,87,69,43,-1,126,148,120,-1,91,109,127,-1,154,129,146,-1,154,146,153,-1,129,149,128,-1,129,127,146,-1,147,155,132,-1,156,157,103,-1,156,103,69,-1,119,158,141,-1,120,125,124,-1,126,136,148,-1,136,150,159,-1,146,152,153,-1,142,156,69,-1,125,160,161,-1,160,136,159,-1,131,152,134,-1,147,132,108,-1,132,162,163,-1,138,140,67,-1,156,164,157,-1,165,118,125,-1,125,148,160,-1,160,166,161,-1,136,128,150,-1,162,167,163,-1,139,168,169,-1,142,170,156,-1,141,142,87,-1,88,119,117,-1,91,128,136,-1,159,150,171,-1,163,172,153,-1,163,153,131,-1,131,132,163,-1,140,155,147,-1,117,119,141,-1,148,136,160,-1,154,171,149,-1,172,173,154,-1,167,172,163,-1,174,175,162,-1,138,67,157,-1,170,164,156,-1,118,76,124,-1,160,159,176,-1,171,177,178,-1,154,173,171,-1,172,154,153,-1,179,162,180,-1,67,147,108,-1,138,157,164,-1,119,118,158,-1,165,161,181,-1,165,125,161,-1,165,181,182,-1,171,150,149,-1,183,167,184,-1,162,184,167,-1,159,185,176,-1,171,173,186,-1,187,184,188,-1,188,162,179,-1,188,179,189,-1,162,175,180,-1,139,138,168,-1,190,170,142,-1,171,186,189,-1,186,188,189,-1,178,159,171,-1,191,189,179,-1,191,177,189,-1,171,189,177,-1,132,174,162,-1,175,174,192,-1,139,169,193,-1,178,185,159,-1,160,176,166,-1,191,194,177,-1,191,179,195,-1,188,184,162,-1,140,139,155,-1,103,157,67,-1,164,170,168,-1,190,141,158,-1,196,158,118,-1,194,191,195,-1,180,197,198,-1,174,193,192,-1,170,199,200,-1,190,158,201,-1,202,176,185,-1,203,185,178,-1,203,204,202,-1,205,204,195,-1,204,203,195,-1,175,192,206,-1,174,155,193,-1,161,207,181,-1,208,195,198,-1,195,179,198,-1,169,200,209,-1,202,185,203,-1,208,205,195,-1,205,208,210,-1,198,179,180,-1,211,212,197,-1,166,207,161,-1,213,176,202,-1,202,204,213,-1,210,214,205,-1,210,208,212,-1,207,215,181,-1,176,216,166,-1,212,217,197,-1,211,197,180,-1,174,132,155,-1,139,193,155,-1,138,164,168,-1,182,218,165,-1,219,214,210,-1,219,212,211,-1,141,190,142,-1,170,200,168,-1,190,199,170,-1,216,220,166,-1,213,214,216,-1,221,222,223,-1,222,219,211,-1,219,210,212,-1,180,175,211,-1,201,224,225,-1,226,227,228,-1,196,201,158,-1,201,196,226,-1,220,215,207,-1,176,213,216,-1,220,216,219,-1,175,206,211,-1,193,229,192,-1,169,168,200,-1,196,118,165,-1,230,231,232,-1,118,88,76,-1,231,220,221,-1,166,220,207,-1,220,219,221,-1,225,233,234,-1,235,224,236,-1,231,215,220,-1,199,234,200,-1,201,226,224,-1,237,192,229,-1,218,196,165,-1,222,211,238,-1,190,201,225,-1,239,240,206,-1,229,193,169,-1,199,225,234,-1,224,241,225,-1,226,218,227,-1,226,196,218,-1,218,182,227,-1,230,242,243,-1,230,181,215,-1,221,219,222,-1,231,221,244,-1,182,243,227,-1,216,214,219,-1,192,237,206,-1,182,181,230,-1,245,223,246,-1,232,231,244,-1,209,229,169,-1,209,247,229,-1,200,234,209,-1,233,225,241,-1,230,232,242,-1,230,215,231,-1,232,244,248,-1,223,222,246,-1,249,239,229,-1,234,247,209,-1,235,250,251,-1,235,236,250,-1,243,182,230,-1,206,238,211,-1,226,228,252,-1,228,253,254,-1,190,225,199,-1,255,256,242,-1,244,255,248,-1,223,245,257,-1,234,233,247,-1,224,226,252,-1,232,248,242,-1,258,229,247,-1,223,244,221,-1,222,238,246,-1,259,260,240,-1,238,240,246,-1,240,239,261,-1,256,255,257,-1,260,246,240,-1,238,206,240,-1,239,237,229,-1,235,233,241,-1,239,206,237,-1,243,262,263,-1,249,229,264,-1,258,264,229,-1,258,251,264,-1,235,258,247,-1,242,262,243,-1,265,266,267,-1,268,245,267,-1,249,269,261,-1,268,256,257,-1,260,270,245,-1,243,263,227,-1,228,263,253,-1,255,242,248,-1,251,271,264,-1,233,235,247,-1,228,254,272,-1,268,267,262,-1,223,257,255,-1,273,274,271,-1,275,276,252,-1,256,268,262,-1,223,255,244,-1,259,240,261,-1,261,269,277,-1,278,249,264,-1,279,280,236,-1,280,250,236,-1,236,224,252,-1,261,277,259,-1,264,271,278,-1,274,278,271,-1,235,251,258,-1,273,271,281,-1,276,236,252,-1,262,282,283,-1,260,245,246,-1,274,284,278,-1,235,241,224,-1,228,227,263,-1,284,274,285,-1,273,285,274,-1,279,236,276,-1,286,287,276,-1,272,252,228,-1,268,257,245,-1,288,266,265,-1,284,249,278,-1,285,273,289,-1,250,280,251,-1,290,281,291,-1,292,253,262,-1,242,256,262,-1,293,294,270,-1,260,293,270,-1,269,284,285,-1,269,285,289,-1,269,289,290,-1,291,280,279,-1,271,251,281,-1,292,262,283,-1,265,267,270,-1,265,294,295,-1,281,280,291,-1,294,265,270,-1,296,259,297,-1,273,281,289,-1,282,267,266,-1,293,298,294,-1,249,284,269,-1,299,254,253,-1,253,263,262,-1,239,249,261,-1,290,289,281,-1,262,267,282,-1,302,288,295,-1,260,259,293,-1,296,298,293,-1,280,281,251,-1,275,252,303,-1,298,304,295,-1,296,297,301,-1,305,272,254,-1,299,306,254,-1,307,253,292,-1,288,265,295,-1,288,308,266,-1,277,269,290,-1,300,310,311,-1,277,297,259,-1,286,276,275,-1,299,309,312,-1,307,299,253,-1,313,314,302,-1,304,302,295,-1,311,304,300,-1,311,302,304,-1,302,311,313,-1,311,315,313,-1,302,308,288,-1,296,293,259,-1,308,316,266,-1,316,317,318,-1,302,314,308,-1,298,295,294,-1,317,319,315,-1,316,319,317,-1,314,313,308,-1,313,319,308,-1,287,279,276,-1,267,245,270,-1,316,308,319,-1,317,315,318,-1,313,315,319,-1,305,303,252,-1,299,312,306,-1,320,316,318,-1,282,321,283,-1,322,282,316,-1,287,291,279,-1,305,252,272,-1,316,282,266,-1,306,305,254,-1])
IndexedFaceSet338.setCreaseAngle(1.57)
Coordinate339 = Coordinate()
Coordinate339.setPoint([1.16,-9.12,1.14,0.45,-9.08,1.07,1.41,-9,1.55,1.38,-8.92,1.6,1.28,-8.84,1.24,1.4,-8.8,1.41,-0.22,-9,1.92,0.18,-8.88,2.17,0.04,-8.96,2.09,0.25,-8.96,1.1,1.19,-9.04,1.88,1.16,-9.04,1.95,0.7,-9.04,1.04,0.77,-8.96,0.98,0.04,-9.04,1.12,-0.14,-9,1.82,-0.11,-8.96,2,0.93,-9,1.94,0.89,-8.96,1.95,0.79,-8.92,0.96,0.67,-8.88,0.98,0.05,-8.8,1.17,-0.08,-8.96,1.21,-0.16,-8.84,1.26,-0.1,-8.88,1.19,0.29,-8.96,2.2,1.04,-9,1.99,1.14,-8.88,1.87,0.97,-8.92,1.05,-0.23,-8.96,1.86,-0.17,-8.8,1.94,1,-8.96,2.01,0.89,-8.96,1,-0.09,-9,1.32,-0.14,-9,1.43,0.6,-8.92,1.98,0.54,-8.88,1.97,0.46,-8.92,1.97,0.8,-8.96,1.94,0.8,-8.88,1.95,0.75,-8.96,1.97,0.92,-8.84,2.06,0.8,-8.96,0.97,0.73,-8.72,0.96,0.85,-8.92,0.99,0.22,-8.68,1.15,0.39,-8.68,1.02,-0.11,-8.84,1.19,-0.28,-8.72,1.76,-0.01,-8.68,2.08,0.39,-8.92,1.99,0.26,-8.8,2.03,0.32,-8.92,2.08,0.44,-8.84,1.95,0.46,-8.96,2,0.62,-8.84,1.97,0.56,-8.8,1.97,0.73,-8.92,1.97,0.69,-8.64,2.07,0.88,-8.72,2.06,1.21,-8.64,1.85,-0.08,-8.88,1.17,-0.22,-8.96,1.52,-0.31,-8.68,1.59,0.22,-8.8,2.12,0.21,-8.76,2.08,0.51,-8.76,1.97,1.1,-8.28,1.87,1.41,-8.64,1.44,1.28,-8.44,1.28,-0.1,-8.68,1.19,0.11,-8.76,2.15,0.56,-8.56,0.94,-0.26,-8.64,1.3,0.41,-8.68,2.01,0.24,-8.48,1.08,-0.06,-8.32,1.23,-0.25,-8.48,1.26,0.19,-8.68,2.02,0.23,-8.68,1.97,0.14,-8.72,2.13,0.27,-8.72,1.96,0.4,-8.76,2.02,0.51,-8.8,1.98,0.12,-8.64,2.09,0.48,-8.44,1.99,0.38,-8.52,1.96,0.67,-8.48,1.01,0.29,-8.16,0.9,0.32,-8.44,0.96,-0.35,-8.52,1.45,-0.23,-8.36,1.87,0.29,-8.68,2.04,0.35,-8.68,2.01,0.25,-8.64,1.97,0.3,-8.6,2.01,0.25,-8.6,1.98,1.37,-8.48,1.67,0.43,-8.56,0.94,0.44,-8.6,0.94,0.39,-8.6,0.98,-0.28,-8.36,1.28,0.06,-8.52,2.06,1.39,-8.32,1.56,0.45,-8.52,0.92,0.15,-8.6,2.02,0.21,-8.6,1.95,0.23,-8.56,1.93,0.67,-8.36,2.07,-0.04,-8.44,2.03,0.46,-8.56,0.92,0.52,-8.52,0.93,0.44,-8.4,0.91,0.19,-8.52,1.94,0.35,-8.52,1.94,0.36,-8.48,1.93,0.37,-8.4,1.92,0.41,-8.16,0.88,0.04,-7.88,0.96,0.35,-8.04,0.87,-0.33,-8.32,1.31,0.27,-8.48,1.97,0.21,-8.44,1.92,0.32,-8.44,1.93,-0.18,-8.24,1.25,-0.4,-8.12,1.33,-0.38,-8.32,1.54,0.08,-8.32,1.96,-0.21,-8.2,1.89,-0.04,-8.16,1.94,0.24,-8.36,1.86,0.38,-8.16,1.92,0.59,-8,2.06,0.38,-8.32,1.92,0.33,-8.28,1.88,0.35,-8.36,1.9,-0.37,-8.16,1.67,0.34,-8.4,1.91,1.28,-8,1.76,1.19,-7.88,1.83,1.05,-8.08,1.91,0.72,-8.04,0.94,1.2,-8.2,1.18,0.04,-8.44,2.04,0.32,-8.36,1.89,0.32,-8.32,1.89,0.21,-8.28,1.86,0.88,-8.08,1.93,-0.41,-8.24,1.4,-0.11,-8.12,1.93,-0.17,-8.08,1.9,0.29,-8.28,1.87,0.3,-8.24,1.87,0.22,-8.12,1.81,0.01,-8.08,1.87,0.82,-7.88,2,1.39,-8.16,1.49,1.34,-8.08,1.69,0.54,-7.68,0.84,-0.24,-8,1.84,-0.38,-8,1.68,-0.5,-7.76,1.4,0.24,-7.84,1.83,0.24,-8.04,1.83,1.38,-7.92,1.53,-0.06,-7.72,0.99,-0.48,-7.64,1.57,0.18,-7.96,1.8,1.36,-7.64,1.62,1.31,-7.56,1.7,1.28,-7.92,1.24,-0.02,-7.96,1.84,0.18,-8,1.8,0.06,-7.96,1.8,0.45,-7.68,2.01,0.24,-7.6,1.87,-0.33,-7.76,1.75,-0.02,-7.84,1.78,-0.12,-7.84,1.83,0.07,-7.76,1.73,0.16,-7.64,1.78,-0.36,-7.4,1.13,-0.1,-7.32,0.96,0.15,-7.96,1.79,0.15,-7.92,1.79,-0.17,-7.8,1.83,0.05,-7.92,1.78,0.12,-7.92,1.77,0.12,-7.88,1.77,0.01,-7.88,1.78,0.89,-7.8,0.96,-0.01,-7.8,1.79,0.56,-7.36,2.05,1.08,-7.56,1.9,-0.02,-7.8,1.78,-0.01,-7.76,1.75,0.35,-7.44,0.79,0.07,-7.64,1.73,0.07,-7.68,1.73,1.33,-7.44,1.28,1.37,-7.48,1.46,0.69,-7.56,0.85,-0.18,-7.72,1.8,-0.15,-7.76,1.82,-0.14,-7.68,1.78,-0.12,-7.64,1.75,0.36,-7.16,1.9,-0.53,-7.6,1.42,-0.06,-7.64,1.72,1.29,-7.24,1.72,-0.09,-7.6,1.72,0.11,-7.52,1.74,0.04,-7.6,1.72,-0.21,-7.64,1.78,-0.17,-7.6,1.75,-0.53,-7.44,1.38,-0.28,-7.52,1.72,0.04,-7.64,1.72,0.1,-7.28,0.81,-0.13,-7.44,1.69,-0.42,-7.44,1.64,-0.43,-7.2,1.57,-0.08,-7.16,1.65,-0.28,-7,1.61,1.03,-6.88,0.94,1.21,-7.28,1.14,0.6,-7.12,0.8,0,-6.96,0.77,0.2,-6.68,0.67,0.97,-7.2,1.96,-0.38,-7.28,1.12,-0.58,-7.28,1.45,-0.56,-7.16,1.36,1.35,-7.12,1.34,1.36,-7.24,1.4,1.35,-6.84,1.41,1.24,-6.6,1.12,0.65,-7.2,2.06,0.19,-7.12,1.8,0.58,-7,2.07,0.33,-6.88,2.02,1.3,-7.08,1.22,-0.55,-6.88,1.37,-0.3,-6.92,0.98,-0.52,-7.08,1.49,-0.46,-6.72,1.74,0.06,-6.84,1.96,1.3,-7.12,1.69,-0.6,-7.08,1.43,0.89,-6.68,1.98,1.33,-6.64,1.35,1.26,-6.64,1.7,0.66,-6.64,0.72,0.01,-6.24,0.66,0.23,-6.28,0.53,-0.56,-6.92,1.55,-0.57,-6.8,1.49,-0.54,-6.76,1.65,1.25,-6.76,1.73,0.22,-6.32,2.03,-0.03,-6.6,1.99,0.57,-6.52,2.04,-0.33,-6.56,1.12,-0.27,-6.68,0.94,1.1,-6.68,1.87,-0.5,-6.32,1.87,-0.51,-6.16,1.75,-0.53,-6.44,1.64,-0.55,-6.68,1.62,0.97,-6.36,1.93,-0.37,-6.48,1.89,1.12,-6.56,1.85,0.37,-6.44,0.59,1.09,-6.44,1.87,1.07,-6.48,1.89,1.16,-5.96,1,1.25,-6.28,1.12,0.7,-6.08,1.97,1.07,-6.56,1.89,1.31,-6.28,1.33,1.32,-6.4,1.47,1.2,-6.36,1.76,-0.33,-6,1.47,-0.23,-6.08,1.24,1.04,-6.48,1.9,1.06,-6.44,1.89,1.2,-5.92,1.08,1.22,-5.92,1.17,-0.53,-6.12,1.88,1.08,-6.36,1.86,1.01,-6.04,1.88,1.26,-6,1.62,-0.06,-6,0.91,-0.11,-6.28,2,-0.29,-6.24,1.99,-0.33,-6.16,1.98,-0.08,-6.12,1.95,0.14,-6.08,1.87,-0.14,-6.12,1.95,0.13,-6.08,0.53,-0.14,-6.04,1.81,-0.07,-6.04,1.83,-0.45,-6.04,1.92,0.95,-5.88,0.77,-0.21,-6.08,1.87,0.57,-5.92,0.68,0.25,-6.08,0.49,0.07,-5.96,0.63,-0.48,-6.04,1.81,0.12,-6,0.52,-0.28,-5.88,1.68,-0.37,-5.96,1.78,0.14,-6,0.5,-0.51,-5.96,1.86,-0.52,-6,1.92,-0.51,-5.92,1.82,-0.48,-5.96,1.66,-0.62,-5.92,1.77,-0.6,-5.84,1.73,-0.59,-5.96,1.8,-0.62,-5.88,1.62,-0.32,-5.92,1.36,-0.62,-5.76,1.43,0.25,-8.6,1.98,0.32,-8.32,1.89])

IndexedFaceSet338.setCoord(Coordinate339)

Shape334.setGeometry(IndexedFaceSet338)

Transform333.addChildren(Shape334)

fieldValue332.addChildren(Transform333)

ProtoInstance330.addFieldValue(fieldValue332)

fieldValue329.addChildren(ProtoInstance330)
ProtoInstance340 = ProtoInstance()
ProtoInstance340.setName("Joint")
ProtoInstance340.setDEF("Allen_hanim_l_ankle")
fieldValue341 = fieldValue()
fieldValue341.setName("name")
fieldValue341.setValue("l_ankle")

ProtoInstance340.addFieldValue(fieldValue341)
fieldValue342 = fieldValue()
fieldValue342.setName("center")
fieldValue342.setValue("0.0645 0.0719 -0.048")

ProtoInstance340.addFieldValue(fieldValue342)
fieldValue343 = fieldValue()
fieldValue343.setName("children")
ProtoInstance344 = ProtoInstance()
ProtoInstance344.setName("Segment")
ProtoInstance344.setDEF("Allen_hanim_l_hindfoot")
fieldValue345 = fieldValue()
fieldValue345.setName("name")
fieldValue345.setValue("l_hindfoot")

ProtoInstance344.addFieldValue(fieldValue345)
fieldValue346 = fieldValue()
fieldValue346.setName("children")
Transform347 = Transform()
Transform347.setDEF("l_foot_adjust")
Transform347.setCenter([-0.32,1.1,0.021])
Transform347.setRotation([0,1,0,1.570796])
Transform347.setScale([0.1,0.1,0.1])
Shape348 = Shape()
Appearance349 = Appearance()
Material350 = Material()
Material350.setDEF("Shoe_Color")
Material350.setAmbientIntensity(0.25)

Appearance349.setMaterial(Material350)

Shape348.setAppearance(Appearance349)
IndexedFaceSet351 = IndexedFaceSet()
IndexedFaceSet351.setCoordIndex([0,1,2,-1,3,4,5,-1,6,7,8,-1,9,10,11,-1,12,13,14,-1,15,16,17,-1,18,19,20,-1,21,22,23,-1,24,25,26,-1,27,28,29,-1,30,31,32,-1,33,34,35,-1,36,37,38,-1,39,40,41,-1,42,43,44,-1,45,46,47,-1,48,49,50,-1,51,52,53,-1,54,55,56,-1,57,58,59,-1,60,61,62,-1,63,64,65,-1,66,67,68,-1,69,70,71,-1,72,73,74,-1,75,76,77,-1,78,79,80,-1,81,82,83,-1,84,85,86,-1,87,88,89,-1,90,91,92,-1,93,94,95,-1,96,97,98,-1,99,100,101,-1,102,103,104,-1,105,106,107,-1,108,109,110,-1,111,112,113,-1,114,115,116,-1,117,118,119,-1,120,121,122,-1,123,124,125,-1,126,127,128,-1,129,130,131,-1,132,133,134,-1,135,136,137,-1,138,139,140,-1,141,142,143,-1,144,145,146,-1,147,148,149,-1,150,151,152,-1,153,154,155,-1,156,157,158,-1,159,160,161,-1,162,163,164,-1,165,166,167,-1,168,169,170,-1,171,172,173,-1,174,175,176,-1,177,178,179,-1,180,181,182,-1,183,184,185,-1,186,187,188,-1,189,190,191,-1,192,193,194,-1,195,196,197,-1,198,199,200,-1,201,202,203,-1,204,205,206,-1,207,208,209,-1,210,211,212,-1,213,214,215,-1,216,217,218,-1,219,220,221,-1,222,223,224,-1,225,226,227,-1,228,229,230,-1,231,232,233,-1,234,235,236,-1,237,238,239,-1,240,241,242,-1,243,244,245,-1,246,247,248,-1,249,250,251,-1,252,253,254,-1,255,256,257,-1,258,259,260,-1,261,262,263,-1,264,265,266,-1,267,268,269,-1,270,271,272,-1,273,274,275,-1,276,277,278,-1,279,280,281,-1,282,283,284,-1,285,286,287,-1,288,289,290,-1,291,292,293,-1,294,295,296,-1,297,298,299,-1,300,301,302,-1,303,304,305,-1,306,307,308,-1,309,310,311,-1,312,313,314,-1,315,316,317,-1,318,319,320,-1,321,322,323,-1,324,325,326,-1,327,328,329,-1,330,331,332,-1,333,334,335,-1,336,337,338,-1,339,340,341,-1,342,343,344,-1,345,346,347,-1,348,349,350,-1,351,352,353,-1,354,355,356,-1,357,358,359,-1,360,361,362,-1,363,364,365,-1,366,367,368,-1,369,370,371,-1,372,373,374,-1,375,376,377,-1,378,379,380,-1,381,382,383,-1,384,385,386,-1,387,388,389,-1,390,391,392,-1,393,394,395,-1,396,397,398,-1,399,400,401,-1,402,403,404,-1,405,406,407,-1,408,409,410,-1,411,412,413,-1,414,415,416,-1,417,418,419,-1,420,421,422,-1,423,424,425,-1,426,427,428,-1,429,430,431,-1,432,433,434,-1,435,436,437,-1,438,439,440,-1,441,442,443,-1,444,445,446,-1,447,448,449,-1,450,451,452,-1,453,454,455,-1,456,457,458,-1,459,460,461,-1,462,463,464,-1,465,466,467,-1,468,469,470,-1,471,472,473,-1,474,475,476,-1,477,478,479,-1,480,481,482,-1,483,484,485,-1,486,487,488,-1,489,490,491,-1,492,493,494,-1,495,496,497,-1,498,499,500,-1,501,502,503,-1,504,505,506,-1,507,508,509,-1,510,511,512,-1,513,514,515,-1,516,517,518,-1,519,520,521,-1,522,523,524,-1,525,526,527,-1,528,529,530,-1,531,532,533,-1,534,535,536,-1,537,538,539,-1,540,541,542,-1,543,544,545,-1,546,547,548,-1,549,550,551,-1,552,553,554,-1,555,556,557,-1,558,559,560,-1,561,562,563,-1,564,565,566,-1,567,568,569,-1,570,571,572,-1,573,574,575,-1,576,577,578,-1,579,580,581,-1,582,583,584,-1,585,586,587,-1,588,589,590,-1,591,592,593,-1,594,595,596,-1,597,598,599,-1,600,601,602,-1,603,604,605,-1,606,607,608,-1,609,610,611,-1,612,613,614,-1,615,616,617,-1,618,619,620,-1,621,622,623,-1,624,625,626,-1,627,628,629,-1,630,631,632,-1,633,634,635,-1,636,637,638,-1,639,640,641,-1,642,643,644,-1,645,646,647,-1,648,649,650,-1,651,652,653,-1,654,655,656,-1,657,658,659,-1,660,661,662,-1,663,664,665,-1,666,667,668,-1,669,670,671,-1,672,673,674,-1,675,676,677,-1,678,679,680,-1,681,682,683,-1,684,685,686,-1,687,688,689,-1,690,691,692,-1,693,694,695,-1,696,697,698,-1,699,700,701,-1,702,703,704,-1,705,706,707,-1,708,709,710,-1,711,712,713,-1,714,715,716,-1,717,718,719,-1,720,721,722,-1,723,724,725,-1,726,727,728,-1,729,730,731,-1,732,733,734,-1,735,736,737,-1,738,739,740,-1,741,742,743,-1,744,745,746,-1,747,748,749,-1,750,751,752,-1,753,754,755,-1,756,757,758,-1,759,760,761,-1,762,763,764,-1,765,766,767,-1,768,769,770,-1,771,772,773,-1,774,775,776,-1,777,778,779,-1,780,781,782,-1,783,784,785,-1,786,787,788,-1,789,790,791,-1,792,793,794,-1,795,796,797,-1,798,799,800,-1,801,802,803,-1,804,805,806,-1,807,808,809,-1,810,811,812,-1,813,814,815,-1,816,817,818,-1,819,820,821,-1,822,823,824,-1,825,826,827,-1,828,829,830,-1,831,832,833,-1,834,835,836,-1,837,838,839,-1,840,841,842,-1,843,844,845,-1,846,847,848,-1,849,850,851,-1,852,853,854,-1,855,856,857,-1,858,859,860,-1,861,862,863,-1,864,865,866,-1,867,868,869,-1,870,871,872,-1,873,874,875,-1,876,877,878,-1,879,880,881,-1,882,883,884,-1,885,886,887,-1,888,889,890,-1,891,892,893,-1,894,895,896,-1,897,898,899,-1,900,901,902,-1,903,904,905,-1,906,907,908,-1,909,910,911,-1,912,913,914,-1,915,916,917,-1,918,919,920,-1,921,922,923,-1,924,925,926,-1,927,928,929,-1,930,931,932,-1,933,934,935,-1,936,937,938,-1,939,940,941,-1,942,943,944,-1,945,946,947,-1,948,949,950,-1,951,952,953,-1,954,955,956,-1,957,958,959,-1,960,961,962,-1,963,964,965,-1,966,967,968,-1,969,970,971,-1,972,973,974,-1,975,976,977,-1,978,979,980,-1,981,982,983,-1,984,985,986,-1,987,988,989,-1,990,991,992,-1,993,994,995,-1,996,997,998,-1,999,1000,1001,-1,1002,1003,1004,-1,1005,1006,1007,-1,1008,1009,1010,-1,1011,1012,1013,-1,1014,1015,1016,-1,1017,1018,1019,-1,1020,1021,1022,-1,1023,1024,1025,-1,1026,1027,1028,-1,1029,1030,1031,-1,1032,1033,1034,-1,1035,1036,1037,-1,1038,1039,1040,-1,1041,1042,1043,-1,1044,1045,1046,-1,1047,1048,1049,-1,1050,1051,1052,-1,1053,1054,1055,-1,1056,1057,1058,-1,1059,1060,1061,-1,1062,1063,1064,-1,1065,1066,1067,-1,1068,1069,1070,-1,1071,1072,1073,-1,1074,1075,1076,-1,1077,1078,1079,-1,1080,1081,1082,-1,1083,1084,1085,-1,1086,1087,1088,-1,1089,1090,1091,-1,1092,1093,1094,-1,1095,1096,1097,-1,1098,1099,1100,-1,1101,1102,1103,-1,1104,1105,1106,-1,1107,1108,1109,-1,1110,1111,1112,-1,1113,1114,1115,-1,1116,1117,1118,-1,1119,1120,1121,-1,1122,1123,1124,-1,1125,1126,1127,-1,1128,1129,1130,-1,1131,1132,1133,-1,1134,1135,1136,-1,1137,1138,1139,-1,1140,1141,1142,-1,1143,1144,1145,-1,1146,1147,1148,-1,1149,1150,1151,-1,1152,1153,1154,-1,1155,1156,1157,-1,1158,1159,1160,-1,1161,1162,1163,-1,1164,1165,1166,-1,1167,1168,1169,-1,1170,1171,1172,-1,1173,1174,1175,-1,1176,1177,1178,-1,1179,1180,1181,-1,1182,1183,1184,-1,1185,1186,1187,-1,1188,1189,1190,-1,1191,1192,1193,-1,1194,1195,1196,-1,1197,1198,1199,-1,1200,1201,1202,-1,1203,1204,1205,-1,1206,1207,1208,-1,1209,1210,1211,-1,1212,1213,1214,-1,1215,1216,1217,-1,1218,1219,1220,-1,1221,1222,1223,-1,1224,1225,1226,-1,1227,1228,1229,-1,1230,1231,1232,-1,1233,1234,1235,-1,1236,1237,1238,-1,1239,1240,1241,-1,1242,1243,1244,-1,1245,1246,1247,-1,1248,1249,1250,-1,1251,1252,1253,-1,1254,1255,1256,-1,1257,1258,1259,-1,1260,1261,1262,-1,1263,1264,1265,-1,1266,1267,1268,-1,1269,1270,1271,-1,1272,1273,1274,-1,1275,1276,1277,-1,1278,1279,1280,-1,1281,1282,1283,-1,1284,1285,1286,-1,1287,1288,1289,-1,1290,1291,1292,-1,1293,1294,1295,-1,1296,1297,1298,-1,1299,1300,1301,-1,1302,1303,1304,-1,1305,1306,1307,-1,1308,1309,1310,-1,1311,1312,1313,-1,1314,1315,1316,-1,1317,1318,1319,-1,1320,1321,1322,-1,1323,1324,1325,-1,1326,1327,1328,-1,1329,1330,1331,-1,1332,1333,1334,-1,1335,1336,1337,-1,1338,1339,1340,-1,1341,1342,1343,-1,1344,1345,1346,-1,1347,1348,1349,-1,1350,1351,1352,-1,1353,1354,1355,-1,1356,1357,1358,-1,1359,1360,1361,-1,1362,1363,1364,-1,1365,1366,1367,-1,1368,1369,1370,-1,1371,1372,1373,-1,1374,1375,1376,-1,1377,1378,1379,-1,1380,1381,1382,-1,1383,1384,1385,-1,1386,1387,1388,-1,1389,1390,1391,-1,1392,1393,1394,-1,1395,1396,1397,-1,1398,1399,1400,-1,1401,1402,1403,-1,1404,1405,1406,-1,1407,1408,1409,-1,1410,1411,1412,-1,1413,1414,1415,-1,1416,1417,1418,-1,1419,1420,1421,-1,1422,1423,1424,-1,1425,1426,1427,-1,1428,1429,1430,-1,1431,1432,1433,-1,1434,1435,1436,-1,1437,1438,1439,-1,1440,1441,1442,-1,1443,1444,1445,-1,1446,1447,1448,-1,1449,1450,1451,-1,1452,1453,1454,-1,1455,1456,1457,-1,1458,1459,1460,-1,1461,1462,1463,-1,1464,1465,1466,-1,1467,1468,1469,-1,1470,1471,1472,-1,1473,1474,1475,-1,1476,1477,1478,-1,1479,1480,1481,-1,1482,1483,1484,-1,1485,1486,1487,-1,1488,1489,1490,-1,1491,1492,1493,-1,1494,1495,1496,-1,1497,1498,1499,-1,1500,1501,1502,-1,1503,1504,1505,-1,1506,1507,1508,-1,1509,1510,1511,-1,1512,1513,1514,-1,1515,1516,1517,-1,1518,1519,1520,-1,1521,1522,1523,-1,1524,1525,1526,-1,1527,1528,1529,-1,1530,1531,1532,-1,1533,1534,1535,-1,1536,1537,1538,-1,1539,1540,1541,-1,1542,1543,1544,-1,1545,1546,1547,-1,1548,1549,1550,-1,1551,1552,1553,-1,1554,1555,1556,-1,1557,1558,1559,-1,1560,1561,1562,-1,1563,1564,1565,-1,1566,1567,1568,-1,1569,1570,1571,-1,1572,1573,1574,-1,1575,1576,1577,-1,1578,1579,1580,-1,1581,1582,1583,-1,1584,1585,1586,-1,1587,1588,1589,-1,1590,1591,1592,-1,1593,1594,1595,-1,1596,1597,1598,-1,1599,1600,1601,-1,1602,1603,1604,-1,1605,1606,1607,-1,1608,1609,1610,-1,1611,1612,1613,-1,1614,1615,1616,-1,1617,1618,1619,-1,1620,1621,1622,-1,1623,1624,1625,-1,1626,1627,1628,-1,1629,1630,1631,-1,1632,1633,1634,-1,1635,1636,1637,-1,1638,1639,1640,-1,1641,1642,1643,-1,1644,1645,1646,-1,1647,1648,1649,-1,1650,1651,1652,-1,1653,1654,1655,-1,1656,1657,1658,-1,1659,1660,1661,-1,1662,1663,1664,-1,1665,1666,1667,-1,1668,1669,1670,-1,1671,1672,1673,-1,1674,1675,1676,-1,1677,1678,1679,-1,1680,1681,1682,-1,1683,1684,1685,-1,1686,1687,1688,-1,1689,1690,1691,-1,1692,1693,1694,-1,1695,1696,1697,-1,1698,1699,1700,-1,1701,1702,1703,-1,1704,1705,1706,-1,1707,1708,1709,-1,1710,1711,1712,-1,1713,1714,1715,-1,1716,1717,1718,-1,1719,1720,1721,-1,1722,1723,1724,-1,1725,1726,1727,-1,1728,1729,1730,-1,1731,1732,1733,-1,1734,1735,1736,-1,1737,1738,1739,-1,1740,1741,1742,-1,1743,1744,1745,-1,1746,1747,1748,-1,1749,1750,1751,-1,1752,1753,1754,-1,1755,1756,1757,-1,1758,1759,1760,-1,1761,1762,1763,-1,1764,1765,1766,-1,1767,1768,1769,-1,1770,1771,1772,-1,1773,1774,1775,-1,1776,1777,1778,-1,1779,1780,1781,-1,1782,1783,1784,-1,1785,1786,1787,-1,1788,1789,1790,-1,1791,1792,1793,-1,1794,1795,1796,-1,1797,1798,1799,-1,1800,1801,1802,-1,1803,1804,1805,-1,1806,1807,1808,-1,1809,1810,1811,-1,1812,1813,1814,-1,1815,1816,1817,-1,1818,1819,1820,-1,1821,1822,1823,-1,1824,1825,1826,-1,1827,1828,1829,-1,1830,1831,1832,-1,1833,1834,1835,-1,1836,1837,1838,-1,1839,1840,1841,-1,1842,1843,1844,-1,1845,1846,1847,-1,1848,1849,1850,-1,1851,1852,1853,-1,1854,1855,1856,-1,1857,1858,1859,-1,1860,1861,1862,-1,1863,1864,1865,-1,1866,1867,1868,-1,1869,1870,1871,-1,1872,1873,1874,-1,1875,1876,1877,-1,1878,1879,1880,-1,1881,1882,1883,-1,1884,1885,1886,-1,1887,1888,1889,-1,1890,1891,1892,-1,1893,1894,1895,-1,1896,1897,1898,-1,1899,1900,1901,-1,1902,1903,1904,-1,1905,1906,1907,-1,1908,1909,1910,-1,1911,1912,1913,-1,1914,1915,1916,-1,1917,1918,1919,-1,1920,1921,1922,-1,1923,1924,1925,-1,1926,1927,1928,-1,1929,1930,1931,-1,1932,1933,1934,-1,1935,1936,1937,-1,1938,1939,1940,-1,1941,1942,1943,-1,1944,1945,1946,-1,1947,1948,1949,-1])
IndexedFaceSet351.setCreaseAngle(1.57)
Coordinate352 = Coordinate()
Coordinate352.setPoint([0.25,-8.96,4.21,0.1,-9.08,4.2,0.04,-9.04,4.23,1.16,-9.12,4.25,1.28,-8.84,4.35,1.41,-9,4.66,0.25,-8.96,4.21,0.17,-9.08,4.14,0.1,-9.08,4.2,0.89,-8.96,4.11,0.97,-8.92,4.16,0.97,-9.04,4.13,0.29,-8.96,5.31,0.13,-9.16,5.21,0.28,-9.16,5.28,-0.08,-9.12,5.06,-0.04,-9.12,5.14,-0.13,-9.04,5.09,0.25,-8.96,4.21,0.45,-9.08,4.18,0.31,-9.08,4.14,0.97,-9.04,4.13,0.97,-8.92,4.16,1.16,-9.12,4.25,0.29,-8.96,5.31,0.35,-9.04,5.34,0.37,-9,5.27,-0.08,-8.96,4.32,0.04,-9.04,4.23,0.06,-9.08,4.28,-0.09,-9,4.43,-0.08,-8.96,4.32,0.06,-9.08,4.28,0.45,-9.08,4.18,0.67,-8.88,4.09,0.7,-9.04,4.15,1.19,-9.04,4.99,1.26,-9.12,4.93,1.38,-8.92,4.71,1.06,-9.08,5.1,1.16,-9.04,5.06,1.04,-9,5.1,0.57,-9.2,4.16,0.45,-9.08,4.18,0.7,-9.04,4.15,0.85,-9,4.08,0.82,-9,4.1,0.89,-8.96,4.11,0.85,-9,4.08,0.89,-8.96,4.11,0.97,-9.04,4.13,1.16,-9.12,4.25,1.41,-9,4.66,1.41,-9.16,4.66,1.26,-9.48,4.41,1.16,-9.12,4.25,1.41,-9.16,4.66,1.04,-9,5.1,1,-8.96,5.12,0.93,-9,5.05,0.29,-8.96,5.31,0.18,-8.88,5.28,0.13,-9.16,5.21,0.04,-8.96,5.2,-0.11,-8.96,5.11,-0.04,-9.12,5.14,1.41,-9.16,4.66,1.41,-9,4.66,1.26,-9.12,4.93,1.16,-9.04,5.06,1.19,-9.04,4.99,1.14,-8.88,4.98,1.16,-9.04,5.06,1.16,-9.08,5.03,1.19,-9.04,4.99,1.04,-9,5.1,1.02,-9.08,5.06,1.06,-9.08,5.1,1.02,-9.08,5.06,1.04,-9,5.1,0.93,-9,5.05,0.35,-9.04,5.34,0.28,-9.16,5.28,0.4,-9.12,5.34,0.35,-9.04,5.34,0.29,-8.96,5.31,0.28,-9.16,5.28,-0.11,-8.96,5.11,-0.13,-9.04,5.09,-0.04,-9.12,5.14,0.04,-8.96,5.2,-0.04,-9.12,5.14,0.02,-9.12,5.17,-0.07,-9.12,5.03,-0.11,-9.08,5.04,-0.08,-9.04,4.91,-0.11,-9.08,5.04,-0.14,-9,4.93,-0.08,-9.04,4.91,-0.14,-9,4.93,-0.09,-9,4.91,-0.08,-9.04,4.91,-0.09,-9,4.91,-0.11,-9,4.85,-0.08,-9.04,4.91,0,-9.04,4.66,-0.06,-9.04,4.65,-0.09,-9,4.71,0.25,-9.08,4.13,0.17,-9.08,4.14,0.25,-8.96,4.21,0.77,-9.08,4.14,0.7,-9.04,4.15,0.78,-9,4.11,0.82,-9,4.1,0.85,-9,4.08,0.83,-9.04,4.11,0.86,-9.04,4.09,0.83,-9.04,4.11,0.85,-9,4.08,0.87,-9,5.01,0.83,-9.04,5.03,0.93,-9,5.05,0.87,-9,5.01,0.93,-9,5.05,0.89,-8.96,5.06,0.8,-9.04,5.05,0.83,-9.04,5.03,0.87,-9,5.01,1.04,-9.12,5.04,1.09,-9.12,5.09,1.06,-9.08,5.1,0.97,-9.08,5.02,1.02,-9.08,5.06,0.93,-9,5.05,0.13,-9.16,5.21,0.04,-8.96,5.2,0.02,-9.12,5.17,-0.13,-9.04,5.09,-0.11,-8.96,5.11,-0.22,-9,5.03,-0.14,-9,4.93,-0.11,-9.08,5.04,-0.22,-9,5.03,-0.08,-9.04,4.91,-0.11,-9,4.85,-0.13,-9.12,4.9,-0.11,-9,4.85,-0.19,-9.16,4.77,-0.13,-9.12,4.9,-0.06,-9.04,4.65,0,-9.04,4.66,0.05,-9.12,4.59,0.06,-9.08,4.28,0.04,-9.04,4.23,0.1,-9.08,4.2,0.77,-8.96,4.09,0.78,-9,4.11,0.7,-9.04,4.15,0.57,-9.2,4.16,0.7,-9.04,4.15,0.77,-9.08,4.14,0.83,-9.04,4.11,0.78,-9,4.11,0.82,-9,4.1,0.97,-9.04,4.13,0.93,-9.12,4.11,0.84,-9.08,4.12,1.26,-9.48,4.41,1.4,-9.32,4.77,1.4,-9.52,4.71,1.13,-9.08,5.05,1.16,-9.08,5.03,1.16,-9.04,5.06,0.83,-9.04,5.03,0.8,-9.04,5.05,0.84,-9.12,5.05,0.8,-9.04,5.05,0.78,-9.04,5.07,0.78,-9.08,5.07,0.76,-9.08,5.09,0.78,-9.08,5.07,0.78,-9.04,5.07,0.13,-9.12,4.22,0.06,-9.08,4.28,0.1,-9.08,4.2,0.45,-9.08,4.18,0.34,-9.16,4.09,0.31,-9.08,4.14,0.77,-9.08,4.14,0.78,-9,4.11,0.83,-9.04,4.11,0.84,-9.08,4.12,0.77,-9.08,4.14,0.83,-9.04,4.11,0.86,-9.16,4.13,0.93,-9.12,4.11,0.93,-9.16,4.12,0.93,-9.12,4.11,0.97,-9.04,4.13,1.01,-9.16,4.14,1.19,-9.04,4.99,1.2,-9.08,5,1.26,-9.12,4.93,1.16,-9.08,5.03,1.2,-9.08,5,1.19,-9.04,4.99,1.02,-9.08,5.06,1.04,-9.12,5.04,1.06,-9.08,5.1,0.25,-9.08,4.13,0.31,-9.08,4.14,0.28,-9.12,4.22,0.25,-9.08,4.13,0.24,-9.12,4.21,0.17,-9.08,4.14,0.25,-9.08,4.13,0.25,-8.96,4.21,0.31,-9.08,4.14,0.2,-9.12,4.2,0.1,-9.08,4.2,0.17,-9.08,4.14,0.46,-9.2,5.34,0.4,-9.12,5.34,0.28,-9.16,5.28,0.18,-8.88,5.28,0.04,-8.96,5.2,0.13,-9.16,5.21,-0.11,-9.08,5.04,-0.13,-9.04,5.09,-0.22,-9,5.03,-0.07,-9.12,5.03,-0.08,-9.12,5.06,-0.11,-9.08,5.04,-0.07,-9.12,5.03,-0.08,-9.04,4.91,-0.13,-9.12,4.9,-0.09,-9,4.71,-0.19,-9.16,4.77,-0.11,-9,4.85,0.09,-9.04,4.62,0.05,-9.12,4.59,0,-9.04,4.66,-0.01,-9.28,4.42,-0.13,-9.2,4.55,0.05,-9.12,4.59,0.78,-9.16,5.11,0.81,-9.16,5.09,0.78,-9.08,5.07,0.46,-9.2,5.34,0.5,-9.16,5.35,0.4,-9.12,5.34,0.5,-9.16,5.35,0.52,-9.12,5.3,0.4,-9.12,5.34,0.13,-9.16,5.21,0.02,-9.12,5.17,-0.01,-9.16,5.12,0.02,-9.12,5.17,-0.04,-9.12,5.14,-0.01,-9.16,5.12,-0.08,-9.12,5.06,-0.13,-9.04,5.09,-0.11,-9.08,5.04,-0.08,-9.12,5.06,-0.09,-9.16,5.08,-0.04,-9.12,5.14,-0.09,-9.16,5.08,-0.07,-9.12,5.03,-0.09,-9.16,5.01,-0.09,-9.16,5.08,-0.08,-9.12,5.06,-0.07,-9.12,5.03,-0.17,-9.16,4.91,-0.13,-9.12,4.9,-0.19,-9.16,4.77,-0.28,-9.2,4.79,-0.19,-9.16,4.77,-0.24,-9.24,4.7,-0.09,-9.36,4.51,-0.13,-9.2,4.55,-0.01,-9.28,4.42,0.09,-9.08,4.43,-0.01,-9.28,4.42,0.05,-9.12,4.59,0.29,-9.2,4.25,0.26,-9.16,4.17,0.35,-9.32,4.14,0.27,-9.16,4.11,0.24,-9.12,4.12,0.31,-9.08,4.14,0.27,-9.16,4.11,0.31,-9.08,4.14,0.34,-9.16,4.09,0.27,-9.16,4.11,0.34,-9.16,4.09,0.35,-9.32,4.14,0.48,-9.28,4.09,0.35,-9.32,4.14,0.34,-9.16,4.09,0.93,-9.12,4.11,0.86,-9.16,4.13,0.84,-9.08,4.12,0.87,-9.2,4.14,0.89,-9.32,4.16,0.8,-9.24,4.16,1.41,-9.16,4.66,1.26,-9.12,4.93,1.28,-9.2,4.94,1.41,-9,4.66,1.38,-8.92,4.71,1.26,-9.12,4.93,1.2,-9.08,5,1.21,-9.2,5,1.26,-9.12,4.93,1.16,-9.12,5.04,1.2,-9.08,5,1.16,-9.08,5.03,1.2,-9.08,5,1.16,-9.12,5.04,1.21,-9.2,5,0.78,-9.08,5.07,0.81,-9.16,5.09,0.84,-9.12,5.05,0.78,-9.16,5.11,0.78,-9.08,5.07,0.76,-9.08,5.09,0.8,-9.04,5.05,0.78,-9.08,5.07,0.84,-9.12,5.05,0.46,-9.2,5.34,0.28,-9.16,5.28,0.29,-9.2,5.24,-0.44,-9.24,5.09,-0.52,-9.24,5.18,-0.44,-9.2,5.17,-0.17,-9.24,4.6,-0.24,-9.24,4.7,-0.19,-9.16,4.77,-0.17,-9.24,4.6,-0.19,-9.16,4.77,-0.06,-9.04,4.65,-0.13,-9.2,4.55,-0.17,-9.24,4.6,-0.06,-9.04,4.65,0.26,-9.16,4.17,0.29,-9.2,4.25,0.28,-9.12,4.22,0.24,-9.12,4.12,0.26,-9.16,4.17,0.17,-9.12,4.18,0.27,-9.16,4.11,0.26,-9.16,4.17,0.24,-9.12,4.12,0.26,-9.16,4.17,0.27,-9.16,4.11,0.35,-9.32,4.14,0.48,-9.28,4.09,0.61,-9.56,4.19,0.39,-9.48,4.21,0.57,-9.2,4.16,0.48,-9.28,4.09,0.45,-9.08,4.18,0.8,-9.24,4.16,0.82,-9.44,4.13,0.72,-9.48,4.13,0.86,-9.16,4.13,0.87,-9.2,4.14,0.8,-9.24,4.16,1.21,-9.2,5,1.28,-9.2,4.94,1.26,-9.12,4.93,1.14,-9.2,5.05,1.16,-9.12,5.04,1.09,-9.12,5.09,1.14,-9.2,5.05,1.21,-9.2,5,1.16,-9.12,5.04,0.91,-9.16,5.03,0.84,-9.12,5.05,0.9,-9.2,5.05,0.81,-9.16,5.09,0.9,-9.2,5.05,0.84,-9.12,5.05,0.46,-9.2,5.34,0.46,-9.24,5.3,0.58,-9.24,5.36,0.5,-9.16,5.35,0.46,-9.2,5.34,0.58,-9.24,5.36,-0.11,-9.24,5.17,-0.16,-9.32,5.23,-0.08,-9.28,5.25,-0.11,-9.24,5.17,-0.15,-9.2,5.18,-0.16,-9.32,5.23,-0.25,-9.2,5.1,-0.25,-9.24,5.14,-0.15,-9.2,5.18,-0.31,-9.24,5.15,-0.25,-9.24,5.14,-0.25,-9.2,5.1,-0.25,-9.2,5.1,-0.36,-9.2,5.14,-0.31,-9.24,5.15,-0.43,-9.24,5.2,-0.31,-9.24,5.15,-0.36,-9.2,5.14,-0.36,-9.2,5.14,-0.44,-9.2,5.17,-0.43,-9.24,5.2,-0.38,-9.16,5.01,-0.44,-9.24,5.09,-0.44,-9.2,5.17,-0.38,-9.16,5.01,-0.44,-9.2,5.17,-0.48,-9.16,5.16,-0.42,-9.24,4.99,-0.44,-9.24,5.09,-0.38,-9.16,5.01,-0.43,-9.24,4.92,-0.42,-9.24,4.99,-0.38,-9.16,5.01,-0.35,-9.24,4.76,-0.24,-9.24,4.7,-0.27,-9.36,4.59,-0.35,-9.24,4.76,-0.28,-9.2,4.79,-0.24,-9.24,4.7,0.12,-9.28,4.33,-0.01,-9.28,4.42,0.14,-9.12,4.39,-0.09,-9,4.71,-0.06,-9.04,4.65,-0.19,-9.16,4.77,0.05,-9.12,4.59,-0.13,-9.2,4.55,-0.06,-9.04,4.65,-0.01,-9.28,4.42,0.09,-9.08,4.43,0.14,-9.12,4.39,0.29,-9.2,4.25,0.28,-9.16,4.35,0.28,-9.12,4.22,0.86,-9.16,4.13,0.77,-9.08,4.14,0.84,-9.08,4.12,1.01,-9.16,4.14,0.97,-9.04,4.13,1.16,-9.12,4.25,1.09,-9.32,4.19,1.26,-9.48,4.41,1.17,-9.52,4.28,1.28,-9.2,4.94,1.21,-9.2,5,1.21,-9.24,5,1.18,-9.24,5.02,1.21,-9.24,5,1.21,-9.2,5,0.97,-9.32,5.03,0.99,-9.28,5.01,0.9,-9.2,5.05,0.9,-9.2,5.05,0.81,-9.16,5.09,0.8,-9.24,5.2,0.67,-9.28,5.33,0.58,-9.24,5.36,0.63,-9.28,5.29,-0.28,-9.44,5.31,-0.12,-9.4,5.27,-0.16,-9.32,5.23,-0.25,-9.24,5.14,-0.31,-9.24,5.15,-0.3,-9.28,5.18,-0.25,-9.24,5.14,-0.16,-9.32,5.23,-0.15,-9.2,5.18,-0.35,-9.28,5.17,-0.3,-9.28,5.18,-0.31,-9.24,5.15,-0.52,-9.24,5.18,-0.58,-9.28,5.22,-0.54,-9.28,5.26,-0.52,-9.24,5.18,-0.43,-9.24,5.2,-0.44,-9.2,5.17,-0.48,-9.28,5.12,-0.58,-9.28,5.22,-0.52,-9.24,5.18,-0.52,-9.24,5.18,-0.44,-9.24,5.09,-0.48,-9.28,5.12,-0.46,-9.32,4.97,-0.43,-9.24,4.92,-0.57,-9.36,4.8,-0.47,-9.24,4.78,-0.54,-9.28,4.76,-0.43,-9.24,4.92,-0.44,-9.36,4.68,-0.48,-9.28,4.7,-0.35,-9.24,4.76,-0.28,-9.2,4.79,-0.35,-9.24,4.76,-0.31,-9.2,4.84,-0.35,-9.24,4.76,-0.48,-9.28,4.7,-0.47,-9.24,4.78,-0.15,-9.28,4.58,-0.17,-9.28,4.6,-0.17,-9.24,4.6,-0.16,-9.32,4.57,-0.15,-9.28,4.58,-0.09,-9.36,4.51,-0.13,-9.2,4.55,-0.15,-9.28,4.58,-0.17,-9.24,4.6,0.09,-9.08,4.43,0.05,-9.12,4.59,0.09,-9.04,4.62,0.12,-9.28,4.33,0.14,-9.12,4.39,0.28,-9.16,4.35,0.89,-9.32,4.16,0.87,-9.2,4.14,1.01,-9.16,4.14,1.21,-9.24,5,1.21,-9.32,5,1.23,-9.32,4.98,0.88,-9.48,5.16,0.97,-9.32,5.03,0.8,-9.24,5.2,0.79,-9.4,5.28,0.69,-9.28,5.31,0.67,-9.32,5.34,0.69,-9.28,5.31,0.67,-9.28,5.33,0.67,-9.32,5.34,0.67,-9.32,5.34,0.67,-9.28,5.33,0.63,-9.28,5.29,0.64,-9.32,5.25,0.64,-9.28,5.25,0.56,-9.28,5.19,0.35,-9.32,5.12,0.35,-9.36,5.19,0.46,-9.28,5.12,0.34,-9.32,5.09,0.35,-9.32,5.12,0.32,-9.28,5.15,0.28,-9.32,5.1,0.34,-9.32,5.09,0.32,-9.28,5.15,-0.25,-9.24,5.14,-0.3,-9.28,5.18,-0.16,-9.32,5.23,-0.61,-9.32,5.25,-0.64,-9.32,5.26,-0.54,-9.28,5.26,-0.58,-9.28,5.22,-0.61,-9.32,5.25,-0.54,-9.28,5.26,-0.43,-9.24,5.2,-0.52,-9.24,5.18,-0.54,-9.28,5.26,-0.59,-9.32,5.22,-0.61,-9.32,5.25,-0.58,-9.28,5.22,-0.46,-9.32,4.97,-0.37,-9.28,5.01,-0.42,-9.24,4.99,-0.46,-9.32,4.97,-0.42,-9.24,4.99,-0.43,-9.24,4.92,-0.54,-9.28,4.76,-0.57,-9.28,4.7,-0.57,-9.36,4.8,-0.6,-9.32,4.63,-0.57,-9.28,4.7,-0.48,-9.4,4.61,-0.57,-9.28,4.7,-0.48,-9.28,4.7,-0.48,-9.4,4.61,-0.48,-9.28,4.7,-0.44,-9.36,4.68,-0.48,-9.4,4.61,-0.17,-9.28,4.6,-0.15,-9.28,4.58,-0.16,-9.32,4.57,-0.15,-9.28,4.58,-0.13,-9.2,4.55,-0.09,-9.36,4.51,-0.01,-9.28,4.42,0.12,-9.52,4.41,-0.09,-9.36,4.51,0.24,-9.32,4.36,0.28,-9.16,4.35,0.29,-9.2,4.25,0.48,-9.28,4.09,0.34,-9.16,4.09,0.45,-9.08,4.18,0.77,-9.08,4.14,0.8,-9.24,4.16,0.57,-9.2,4.16,0.89,-9.32,4.16,1.01,-9.16,4.14,1.02,-9.36,4.16,0.86,-9.16,4.13,0.8,-9.24,4.16,0.77,-9.08,4.14,1.01,-9.16,4.14,1.16,-9.12,4.25,1.09,-9.32,4.19,1.02,-9.36,4.16,1.01,-9.16,4.14,1.09,-9.32,4.19,1.09,-9.32,4.19,1.08,-9.52,4.24,1.04,-9.48,4.19,1.37,-9.36,4.86,1.4,-9.32,4.77,1.28,-9.2,4.94,1.4,-9.32,4.77,1.37,-9.36,4.86,1.4,-9.52,4.71,0.84,-9.44,5.24,0.79,-9.4,5.28,0.79,-9.44,5.28,0.67,-9.32,5.34,0.64,-9.32,5.25,0.7,-9.44,5.32,0.63,-9.28,5.29,0.64,-9.32,5.25,0.67,-9.32,5.34,0.64,-9.32,5.25,0.63,-9.28,5.29,0.64,-9.28,5.25,0.64,-9.32,5.25,0.56,-9.28,5.19,0.59,-9.48,5.25,0.64,-9.32,5.25,0.59,-9.48,5.25,0.7,-9.44,5.32,0.56,-9.28,5.19,0.43,-9.44,5.22,0.49,-9.48,5.21,0.56,-9.28,5.19,0.49,-9.48,5.21,0.59,-9.48,5.25,0.35,-9.32,5.12,0.46,-9.28,5.12,0.32,-9.28,5.15,0.35,-9.36,5.19,0.35,-9.32,5.12,0.39,-9.36,5.1,-0.12,-9.4,5.27,-0.06,-9.36,5.31,-0.08,-9.28,5.25,-0.28,-9.44,5.31,-0.17,-9.48,5.3,-0.12,-9.4,5.27,-0.28,-9.44,5.31,-0.26,-9.48,5.33,-0.17,-9.48,5.3,-0.3,-9.28,5.18,-0.35,-9.36,5.14,-0.32,-9.36,5.26,-0.3,-9.28,5.18,-0.32,-9.36,5.26,-0.16,-9.32,5.23,-0.53,-9.32,4.96,-0.46,-9.32,4.97,-0.49,-9.36,5.02,-0.46,-9.32,4.97,-0.57,-9.36,4.8,-0.62,-9.4,4.92,-0.49,-9.36,5.02,-0.46,-9.32,4.97,-0.62,-9.4,4.92,-0.54,-9.28,4.76,-0.57,-9.36,4.8,-0.43,-9.24,4.92,-0.57,-9.28,4.7,-0.64,-9.36,4.68,-0.57,-9.36,4.8,-0.6,-9.32,4.63,-0.64,-9.36,4.68,-0.57,-9.28,4.7,-0.6,-9.32,4.63,-0.56,-9.44,4.59,-0.64,-9.36,4.68,-0.44,-9.36,4.68,-0.35,-9.24,4.76,-0.27,-9.36,4.59,-0.17,-9.28,4.6,-0.24,-9.24,4.7,-0.17,-9.24,4.6,-0.27,-9.36,4.59,-0.17,-9.28,4.6,-0.16,-9.32,4.57,0.24,-9.32,4.36,0.12,-9.28,4.33,0.28,-9.16,4.35,0.12,-9.52,4.41,0.24,-9.32,4.36,0.29,-9.6,4.32,0.35,-9.32,4.14,0.24,-9.32,4.36,0.29,-9.2,4.25,0.98,-9.44,4.16,1.02,-9.36,4.16,1.04,-9.48,4.19,1.26,-9.48,4.41,1.09,-9.32,4.19,1.16,-9.12,4.25,1.23,-9.32,4.98,1.24,-9.4,4.98,1.26,-9.4,4.96,1.23,-9.32,4.98,1.28,-9.2,4.94,1.21,-9.24,5,-0.07,-9.4,5.39,-0.11,-9.44,5.34,-0.13,-9.44,5.39,-0.67,-9.4,4.68,-0.64,-9.36,4.68,-0.56,-9.44,4.59,-0.74,-9.4,4.63,-0.67,-9.4,4.68,-0.56,-9.44,4.59,-0.56,-9.48,4.55,-0.65,-9.6,4.59,-0.74,-9.48,4.59,-0.48,-9.4,4.61,-0.56,-9.44,4.59,-0.6,-9.32,4.63,-0.45,-9.44,4.6,-0.48,-9.4,4.61,-0.44,-9.36,4.68,-0.17,-9.28,4.6,-0.27,-9.36,4.59,-0.24,-9.24,4.7,-0.35,-9.64,4.49,-0.38,-9.44,4.58,-0.27,-9.36,4.59,0.12,-9.52,4.41,-0.16,-9.52,4.46,-0.09,-9.36,4.51,0.39,-9.48,4.21,0.29,-9.6,4.32,0.24,-9.32,4.36,0.48,-9.28,4.09,0.57,-9.2,4.16,0.72,-9.48,4.13,0.89,-9.32,4.16,0.88,-9.44,4.15,0.82,-9.44,4.13,1.27,-9.76,4.43,1.22,-9.56,4.32,1.26,-9.48,4.41,1.26,-9.48,4.41,1.41,-9.16,4.66,1.4,-9.32,4.77,1.4,-9.32,4.77,1.41,-9.16,4.66,1.28,-9.2,4.94,1.37,-9.36,4.86,1.26,-9.4,4.96,1.29,-9.44,4.95,1.26,-9.4,4.96,1.27,-9.44,4.97,1.29,-9.44,4.95,0.97,-9.32,5.03,0.9,-9.2,5.05,0.8,-9.24,5.2,1.05,-9.36,4.99,1.08,-9.48,5.01,1.18,-9.52,4.97,0.84,-9.44,5.24,0.88,-9.48,5.16,0.8,-9.24,5.2,0.79,-9.4,5.28,0.67,-9.32,5.34,0.7,-9.44,5.32,0.56,-9.28,5.19,0.46,-9.28,5.12,0.43,-9.44,5.22,-0.1,-9.44,5.44,-0.07,-9.44,5.44,-0.07,-9.4,5.39,-0.1,-9.44,5.44,-0.07,-9.4,5.39,-0.13,-9.44,5.39,-0.12,-9.4,5.27,-0.11,-9.44,5.34,-0.06,-9.36,5.31,-0.11,-9.44,5.34,-0.07,-9.4,5.39,-0.06,-9.36,5.31,-0.37,-9.4,5.3,-0.37,-9.44,5.33,-0.28,-9.44,5.31,-0.37,-9.4,5.3,-0.28,-9.44,5.31,-0.32,-9.36,5.26,-0.37,-9.44,5.33,-0.37,-9.4,5.3,-0.41,-9.44,5.22,-0.37,-9.4,5.3,-0.49,-9.4,5.27,-0.41,-9.44,5.22,-0.49,-9.4,5.27,-0.57,-9.4,5.19,-0.47,-9.44,5.19,-0.68,-9.52,5.01,-0.59,-9.44,5.11,-0.49,-9.36,5.02,-0.46,-9.56,5.36,-0.41,-9.44,5.22,-0.47,-9.44,5.19,-0.68,-9.52,5.01,-0.49,-9.36,5.02,-0.62,-9.4,4.92,-0.63,-9.4,4.8,-0.62,-9.4,4.92,-0.57,-9.36,4.8,-0.68,-9.44,4.8,-0.67,-9.4,4.68,-0.7,-9.44,4.67,-0.68,-9.44,4.8,-0.63,-9.4,4.8,-0.67,-9.4,4.68,-0.67,-9.4,4.68,-0.74,-9.4,4.63,-0.7,-9.44,4.67,-0.74,-9.48,4.59,-0.7,-9.44,4.67,-0.74,-9.4,4.63,-0.48,-9.4,4.61,-0.45,-9.44,4.6,-0.56,-9.44,4.59,-0.45,-9.44,4.65,-0.45,-9.44,4.6,-0.48,-9.4,4.61,-0.45,-9.44,4.6,-0.45,-9.44,4.65,-0.48,-9.4,4.61,-0.45,-9.44,4.6,-0.44,-9.36,4.68,-0.38,-9.44,4.58,0.12,-9.52,4.41,0.29,-9.6,4.32,0.24,-9.76,4.43,0.57,-9.2,4.16,0.8,-9.24,4.16,0.72,-9.48,4.13,0.92,-9.4,4.15,0.88,-9.44,4.15,0.89,-9.32,4.16,0.88,-9.44,4.15,0.92,-9.4,4.15,0.98,-9.44,4.16,0.8,-9.24,4.16,0.89,-9.32,4.16,0.82,-9.44,4.13,1.02,-9.36,4.16,1.09,-9.32,4.19,1.04,-9.48,4.19,1.02,-9.36,4.16,0.98,-9.44,4.16,0.92,-9.4,4.15,1.23,-9.32,4.98,1.26,-9.4,4.96,1.37,-9.36,4.86,1.23,-9.32,4.98,1.37,-9.36,4.86,1.28,-9.2,4.94,1.08,-9.48,5.01,1.16,-9.56,5,1.18,-9.52,4.97,0.84,-9.44,5.24,0.8,-9.24,5.2,0.79,-9.4,5.28,0.84,-9.44,5.24,0.83,-9.48,5.24,0.88,-9.48,5.16,1.05,-9.36,4.99,0.97,-9.32,5.03,0.88,-9.48,5.16,-0.13,-9.48,5.46,-0.12,-9.52,5.53,-0.09,-9.52,5.48,-0.11,-9.44,5.34,-0.1,-9.52,5.44,-0.13,-9.48,5.46,-0.11,-9.52,5.34,-0.06,-9.48,5.34,-0.11,-9.44,5.34,-0.32,-9.36,5.26,-0.28,-9.44,5.31,-0.16,-9.32,5.23,-0.57,-9.4,5.19,-0.59,-9.44,5.11,-0.65,-9.56,5.17,-0.47,-9.44,5.19,-0.41,-9.44,5.22,-0.49,-9.4,5.27,-0.59,-9.56,5.27,-0.46,-9.56,5.36,-0.47,-9.44,5.19,-0.59,-9.44,5.11,-0.68,-9.52,5.01,-0.65,-9.56,5.17,-0.49,-9.36,5.02,-0.59,-9.44,5.11,-0.57,-9.4,5.19,-0.62,-9.4,4.92,-0.73,-9.48,4.86,-0.72,-9.52,4.89,-0.62,-9.4,4.92,-0.68,-9.44,4.8,-0.73,-9.48,4.86,-0.68,-9.44,4.8,-0.75,-9.48,4.78,-0.73,-9.48,4.86,-0.62,-9.4,4.92,-0.72,-9.52,4.89,-0.68,-9.52,5.01,-0.74,-9.48,4.59,-0.77,-9.48,4.63,-0.7,-9.44,4.67,-0.5,-9.48,4.55,-0.45,-9.44,4.6,-0.46,-9.52,4.58,-0.45,-9.44,4.6,-0.38,-9.44,4.58,-0.46,-9.52,4.58,0.12,-9.28,4.33,0.24,-9.32,4.36,0.12,-9.52,4.41,0.35,-9.32,4.14,0.48,-9.28,4.09,0.39,-9.48,4.21,0.35,-9.32,4.14,0.39,-9.48,4.21,0.24,-9.32,4.36,0.82,-9.44,4.13,0.82,-9.48,4.14,0.72,-9.48,4.13,0.95,-9.56,5.13,1.08,-9.48,5.01,0.88,-9.48,5.16,0.69,-9.28,5.31,0.79,-9.4,5.28,0.8,-9.24,5.2,0.7,-9.44,5.32,0.59,-9.48,5.25,0.69,-9.56,5.25,0.59,-9.48,5.25,0.49,-9.48,5.21,0.49,-9.52,5.18,0.49,-9.48,5.21,0.43,-9.44,5.22,0.47,-9.52,5.2,0.43,-9.44,5.22,0.39,-9.56,5.25,0.47,-9.52,5.2,0.35,-9.36,5.19,0.24,-9.44,5.29,0.43,-9.44,5.22,-0.13,-9.44,5.39,-0.11,-9.44,5.34,-0.03,-9.48,5.36,0.7,-9.44,5.32,0.69,-9.56,5.25,0.74,-9.6,5.25,-0.14,-9.52,5.53,-0.13,-9.48,5.46,-0.1,-9.52,5.44,-0.04,-9.56,5.36,-0.1,-9.52,5.44,-0.11,-9.52,5.34,-0.11,-9.52,5.34,-0.11,-9.44,5.34,-0.17,-9.48,5.3,-0.12,-9.4,5.27,-0.08,-9.28,5.25,-0.16,-9.32,5.23,-0.17,-9.48,5.3,-0.11,-9.44,5.34,-0.12,-9.4,5.27,-0.18,-9.52,5.35,-0.11,-9.52,5.34,-0.17,-9.48,5.3,-0.39,-9.52,5.44,-0.33,-9.52,5.42,-0.38,-9.48,5.38,-0.46,-9.56,5.36,-0.37,-9.44,5.33,-0.41,-9.44,5.22,-0.46,-9.56,5.36,-0.38,-9.48,5.38,-0.37,-9.44,5.33,-0.59,-9.56,5.27,-0.47,-9.44,5.19,-0.57,-9.4,5.19,-0.62,-9.4,4.92,-0.63,-9.4,4.8,-0.68,-9.44,4.8,-0.74,-9.52,4.86,-0.72,-9.52,4.89,-0.73,-9.48,4.86,-0.75,-9.48,4.78,-0.72,-9.52,4.76,-0.73,-9.48,4.86,-0.73,-9.52,4.71,-0.72,-9.52,4.76,-0.75,-9.48,4.78,-0.75,-9.48,4.78,-0.77,-9.48,4.63,-0.73,-9.52,4.71,-0.81,-9.52,4.61,-0.73,-9.52,4.71,-0.77,-9.48,4.63,-0.77,-9.48,4.63,-0.74,-9.48,4.59,-0.81,-9.52,4.61,-0.74,-9.48,4.59,-0.71,-9.6,4.57,-0.81,-9.52,4.61,-0.56,-9.44,4.59,-0.74,-9.48,4.59,-0.74,-9.4,4.63,-0.52,-9.56,4.5,-0.5,-9.48,4.55,-0.46,-9.52,4.58,-0.09,-9.36,4.51,-0.16,-9.52,4.46,-0.16,-9.32,4.57,-0.28,-9.84,4.51,-0.35,-9.64,4.49,-0.16,-9.52,4.46,0.61,-9.56,4.19,0.41,-9.64,4.27,0.39,-9.48,4.21,1.08,-9.52,4.24,1,-9.52,4.21,1.04,-9.48,4.19,1.09,-9.32,4.19,1.17,-9.52,4.28,1.08,-9.52,4.24,1.26,-9.48,4.41,1.22,-9.56,4.32,1.17,-9.52,4.28,0.46,-9.28,5.12,0.35,-9.36,5.19,0.43,-9.44,5.22,0.47,-9.52,5.2,0.49,-9.52,5.18,0.49,-9.48,5.21,0.39,-9.56,5.25,0.22,-9.64,5.31,0.33,-9.68,5.28,0.05,-9.4,5.24,0.08,-9.48,5.31,0.24,-9.44,5.29,-0.09,-9.52,5.48,0,-9.48,5.45,-0.07,-9.44,5.44,-0.09,-9.52,5.48,-0.07,-9.44,5.44,-0.1,-9.44,5.44,-0.13,-9.48,5.46,-0.09,-9.52,5.48,-0.1,-9.44,5.44,0.59,-9.56,5.21,0.69,-9.56,5.25,0.59,-9.48,5.25,-0.09,-9.52,5.48,-0.12,-9.52,5.53,-0.16,-9.6,5.54,-0.27,-9.56,5.56,-0.16,-9.6,5.54,-0.12,-9.52,5.53,-0.27,-9.56,5.56,-0.12,-9.52,5.53,-0.13,-9.48,5.46,-0.39,-9.56,5.53,-0.37,-9.64,5.45,-0.4,-9.6,5.54,-0.39,-9.56,5.53,-0.39,-9.52,5.44,-0.37,-9.64,5.45,-0.46,-9.56,5.36,-0.39,-9.52,5.44,-0.38,-9.48,5.38,-0.39,-9.52,5.44,-0.44,-9.64,5.42,-0.37,-9.64,5.45,-0.59,-9.56,5.27,-0.65,-9.56,5.17,-0.72,-9.6,5.22,-0.65,-9.56,5.17,-0.68,-9.52,5.01,-0.73,-9.56,5.04,-0.77,-9.56,5.03,-0.73,-9.56,5.04,-0.68,-9.52,5.01,-0.92,-9.52,4.74,-0.88,-9.56,4.83,-0.79,-9.52,4.82,-0.99,-9.56,4.7,-0.88,-9.56,4.83,-0.92,-9.52,4.74,-0.92,-9.56,4.6,-0.97,-9.56,4.59,-0.96,-9.52,4.61,-0.83,-9.56,4.64,-0.81,-9.52,4.61,-0.71,-9.6,4.57,-0.63,-9.6,4.53,-0.52,-9.56,4.5,-0.52,-9.68,4.5,-0.56,-9.44,4.59,-0.56,-9.48,4.55,-0.74,-9.48,4.59,-0.52,-9.56,4.5,-0.56,-9.48,4.55,-0.5,-9.48,4.55,-0.48,-9.6,4.56,-0.52,-9.56,4.5,-0.46,-9.52,4.58,-0.16,-9.52,4.46,0.12,-9.52,4.41,0.04,-9.72,4.46,1.16,-9.56,4.29,1.08,-9.52,4.24,1.17,-9.52,4.28,1.08,-9.48,5.01,1.05,-9.36,4.99,0.88,-9.48,5.16,0.49,-9.52,5.18,0.47,-9.52,5.2,0.51,-9.6,5.19,0.39,-9.56,5.25,0.43,-9.44,5.22,0.24,-9.44,5.29,0.08,-9.48,5.31,0.22,-9.64,5.31,0.24,-9.44,5.29,-0.16,-9.6,5.38,-0.04,-9.56,5.36,-0.11,-9.52,5.34,-0.1,-9.52,5.44,-0.06,-9.48,5.34,-0.11,-9.52,5.34,-0.11,-9.44,5.34,-0.06,-9.48,5.34,-0.1,-9.52,5.44,0.74,-9.6,5.25,0.69,-9.56,5.25,0.69,-9.6,5.22,-0.4,-9.6,5.54,-0.27,-9.6,5.6,-0.27,-9.56,5.56,-0.27,-9.56,5.56,-0.27,-9.6,5.6,-0.16,-9.6,5.54,-0.39,-9.56,5.53,-0.4,-9.6,5.54,-0.27,-9.56,5.56,-0.39,-9.52,5.44,-0.46,-9.56,5.36,-0.44,-9.64,5.42,-0.59,-9.56,5.27,-0.57,-9.4,5.19,-0.65,-9.56,5.17,-1.41,-9.88,5.22,-1.29,-9.6,5.21,-1.34,-9.56,5.13,-1.41,-9.88,5.22,-1.29,-9.84,5.28,-1.29,-9.6,5.21,-0.99,-9.56,4.7,-1.34,-9.72,4.71,-1.32,-9.64,4.81,-0.96,-9.52,4.61,-0.99,-9.56,4.7,-0.92,-9.52,4.74,-0.99,-9.56,4.7,-0.96,-9.52,4.61,-0.97,-9.56,4.59,-0.99,-9.56,4.7,-0.97,-9.56,4.59,-0.93,-9.68,4.63,-0.56,-9.48,4.55,-0.52,-9.56,4.5,-0.63,-9.6,4.53,-0.56,-9.48,4.55,-0.63,-9.6,4.53,-0.65,-9.6,4.59,-0.65,-9.6,4.59,-0.71,-9.6,4.57,-0.74,-9.48,4.59,-0.48,-9.6,4.56,-0.46,-9.52,4.58,-0.35,-9.64,4.49,-0.38,-9.44,4.58,-0.44,-9.36,4.68,-0.27,-9.36,4.59,-0.38,-9.44,4.58,-0.35,-9.64,4.49,-0.46,-9.52,4.58,0.04,-9.72,4.46,0.24,-9.76,4.43,0.06,-9.84,4.52,0.36,-9.64,4.38,0.37,-9.72,4.39,0.24,-9.76,4.43,0.39,-9.48,4.21,0.41,-9.64,4.27,0.36,-9.64,4.3,0.63,-9.68,4.25,0.49,-9.68,4.29,0.61,-9.56,4.19,0.72,-9.56,4.17,0.61,-9.56,4.19,0.72,-9.48,4.13,1.22,-9.56,4.32,1.16,-9.56,4.29,1.17,-9.52,4.28,0.95,-9.76,4.28,1.2,-9.76,4.37,1.12,-9.84,4.42,1.34,-9.56,4.91,1.4,-9.52,4.71,1.37,-9.36,4.86,1.19,-9.6,5.02,1.16,-9.56,5,1.06,-9.64,5.07,0.47,-9.52,5.2,0.39,-9.56,5.25,0.51,-9.6,5.19,0,-9.56,5.36,0.22,-9.64,5.31,0.08,-9.48,5.31,-0.57,-9.68,5.44,-0.44,-9.64,5.42,-0.46,-9.56,5.36,-0.57,-9.68,5.44,-0.46,-9.56,5.36,-0.59,-9.56,5.27,-0.44,-9.64,5.42,-0.57,-9.68,5.44,-0.52,-9.72,5.48,-0.82,-9.64,5.36,-1.01,-9.6,5.31,-0.96,-9.8,5.45,-1.29,-9.84,5.28,-1.16,-9.88,5.34,-1.12,-9.76,5.38,-1.26,-9.56,5.12,-1.34,-9.56,5.13,-1.29,-9.6,5.21,-1.49,-9.92,5.13,-1.41,-9.88,5.22,-1.39,-9.56,4.98,-1.34,-9.72,4.71,-1.44,-9.92,4.71,-1.47,-9.72,4.8,-1.34,-9.72,4.71,-0.99,-9.56,4.7,-0.93,-9.68,4.63,-0.84,-9.72,4.55,-0.91,-9.84,4.53,-0.93,-9.68,4.63,-0.97,-9.56,4.59,-0.98,-9.6,4.51,-0.93,-9.68,4.63,-0.98,-9.6,4.51,-0.96,-9.6,4.49,-0.97,-9.64,4.47,-0.97,-9.64,4.47,-0.96,-9.6,4.49,-0.88,-9.64,4.43,-0.83,-9.6,4.52,-0.88,-9.64,4.43,-0.96,-9.6,4.49,-0.78,-9.64,4.48,-0.88,-9.64,4.43,-0.83,-9.6,4.52,-0.63,-9.6,4.53,-0.69,-9.64,4.44,-0.78,-9.64,4.48,-0.65,-9.64,4.43,-0.63,-9.6,4.53,-0.52,-9.68,4.5,-0.52,-9.68,4.5,-0.52,-9.56,4.5,-0.48,-9.6,4.56,-0.16,-9.52,4.46,-0.27,-9.36,4.59,-0.16,-9.32,4.57,0.04,-9.72,4.46,0.12,-9.52,4.41,0.24,-9.76,4.43,0.36,-9.64,4.3,0.36,-9.64,4.38,0.29,-9.6,4.32,0.39,-9.48,4.21,0.36,-9.64,4.3,0.29,-9.6,4.32,1.34,-9.56,4.91,1.37,-9.36,4.86,1.29,-9.44,4.95,1.34,-9.56,4.91,1.36,-9.76,4.8,1.4,-9.52,4.71,1.16,-9.56,5,1.19,-9.6,5.02,1.26,-9.6,4.97,1.16,-9.56,5,1.08,-9.48,5.01,1.06,-9.64,5.07,1.06,-9.64,5.07,0.96,-9.64,5.14,0.96,-9.68,5.14,0.39,-9.56,5.25,0.39,-9.64,5.25,0.51,-9.6,5.19,0.22,-9.64,5.31,0.39,-9.56,5.25,0.24,-9.44,5.29,0.2,-9.84,5.33,0.3,-9.76,5.33,0.22,-9.64,5.31,-0.01,-9.64,5.38,0.02,-9.88,5.37,0.22,-9.64,5.31,0,-9.56,5.36,-0.04,-9.56,5.36,-0.01,-9.64,5.38,-0.47,-9.68,4.51,-0.52,-9.68,4.5,-0.48,-9.6,4.56,-0.47,-9.68,4.51,-0.48,-9.6,4.56,-0.35,-9.64,4.49,-0.28,-9.84,4.51,-0.33,-9.88,4.54,-0.47,-9.68,4.51,0.29,-9.6,4.32,0.36,-9.64,4.38,0.24,-9.76,4.43,0.45,-9.68,4.38,0.42,-9.68,4.39,0.36,-9.64,4.38,-0.71,-9.6,5.28,-0.77,-9.64,5.36,-0.57,-9.68,5.44,-0.71,-9.6,5.28,-0.57,-9.68,5.44,-0.59,-9.56,5.27,-1.49,-9.92,5.13,-1.39,-9.56,4.98,-1.5,-9.72,4.89,-1.33,-10,4.65,-1.34,-9.72,4.71,-1.05,-9.92,4.57,-0.87,-9.72,4.44,-0.84,-9.72,4.55,-0.97,-9.64,4.47,-0.88,-9.64,4.43,-0.87,-9.72,4.44,-0.97,-9.64,4.47,-0.69,-9.64,4.44,-0.73,-9.68,4.4,-0.78,-9.64,4.48,-0.65,-9.64,4.43,-0.69,-9.64,4.44,-0.63,-9.6,4.53,-0.63,-9.68,4.45,-0.73,-9.68,4.4,-0.69,-9.64,4.44,-0.69,-9.64,4.44,-0.65,-9.64,4.43,-0.63,-9.68,4.45,0.49,-9.68,4.29,0.41,-9.64,4.27,0.61,-9.56,4.19,0.48,-9.28,4.09,0.72,-9.48,4.13,0.61,-9.56,4.19,0.95,-9.56,5.13,1.06,-9.64,5.07,1.08,-9.48,5.01,1.08,-9.68,5.09,1.06,-9.64,5.07,0.96,-9.68,5.14,0.95,-9.56,5.13,0.88,-9.48,5.16,0.89,-9.56,5.16,0.93,-9.68,5.16,0.96,-9.68,5.14,0.96,-9.64,5.14,0.39,-9.64,5.25,0.39,-9.56,5.25,0.33,-9.68,5.28,-0.16,-9.6,5.38,-0.11,-9.52,5.34,-0.18,-9.52,5.35,-0.39,-9.72,5.46,-0.31,-9.76,5.45,-0.16,-9.6,5.38,-0.77,-9.64,5.36,-0.82,-9.64,5.36,-0.75,-9.68,5.42,-0.77,-9.64,5.36,-0.75,-9.68,5.42,-0.57,-9.68,5.44,-1.12,-9.76,5.38,-1.01,-9.6,5.31,-1.29,-9.6,5.21,-1.5,-9.72,4.89,-1.39,-9.56,4.98,-1.32,-9.64,4.81,-0.93,-9.68,4.63,-0.98,-9.6,4.51,-0.97,-9.64,4.47,-0.88,-9.64,4.43,-0.82,-9.72,4.41,-0.87,-9.72,4.44,-0.82,-9.72,4.41,-0.88,-9.64,4.43,-0.78,-9.64,4.48,-0.73,-9.68,4.4,-0.82,-9.72,4.41,-0.78,-9.64,4.48,-0.71,-9.72,4.46,-0.82,-9.72,4.41,-0.73,-9.68,4.4,-0.62,-9.72,4.5,-0.5,-9.88,4.52,-0.79,-9.88,4.51,0.14,-9.88,4.58,0.06,-9.84,4.52,0.24,-9.76,4.43,0.12,-9.28,4.33,0.12,-9.52,4.41,-0.01,-9.28,4.42,0.42,-9.68,4.39,0.41,-9.72,4.39,0.37,-9.72,4.39,0.42,-9.68,4.39,0.37,-9.72,4.39,0.36,-9.64,4.38,0.87,-9.84,4.38,0.82,-9.88,4.41,0.65,-9.72,4.35,0.63,-9.68,4.25,0.72,-9.56,4.17,0.8,-9.6,4.24,0.63,-9.68,4.25,0.61,-9.56,4.19,0.72,-9.56,4.17,0.63,-9.68,4.25,0.65,-9.72,4.35,0.49,-9.68,4.29,0.63,-9.68,4.25,0.8,-9.6,4.24,0.65,-9.72,4.35,1.2,-9.76,4.37,1.08,-9.6,4.31,1.16,-9.56,4.29,1.2,-9.76,4.37,1.16,-9.56,4.29,1.22,-9.56,4.32,1.34,-9.56,4.91,1.26,-9.6,4.97,1.27,-9.68,4.97,1.19,-9.6,5.02,1.27,-9.68,4.97,1.26,-9.6,4.97,1.08,-9.68,5.09,1.09,-9.72,5.09,1.11,-9.72,5.07,1.08,-9.68,5.09,1.11,-9.72,5.07,1.19,-9.6,5.02,1.08,-9.68,5.09,1.19,-9.6,5.02,1.06,-9.64,5.07,0.98,-9.72,5.08,1.08,-9.68,5.09,0.96,-9.68,5.14,0.96,-9.68,5.14,0.95,-9.72,5.1,0.98,-9.72,5.08,0.95,-9.56,5.13,0.96,-9.64,5.14,1.06,-9.64,5.07,0.02,-9.88,5.37,0.2,-9.84,5.33,0.22,-9.64,5.31,-0.01,-9.64,5.38,-0.04,-9.56,5.36,-0.16,-9.6,5.38,-0.31,-9.76,5.45,-0.15,-9.72,5.43,-0.16,-9.6,5.38,-0.39,-9.72,5.46,-0.37,-9.76,5.48,-0.31,-9.76,5.45,-0.24,-9.8,5.47,-0.31,-9.76,5.45,-0.31,-9.84,5.49,-0.52,-9.72,5.48,-0.56,-9.8,5.51,-0.43,-9.84,5.5,-0.64,-9.76,5.49,-0.52,-9.72,5.48,-0.57,-9.68,5.44,-0.75,-9.68,5.42,-0.64,-9.76,5.49,-0.57,-9.68,5.44,-0.82,-9.64,5.36,-0.84,-9.6,5.26,-1.01,-9.6,5.31,-0.75,-9.68,5.42,-0.82,-9.64,5.36,-0.96,-9.8,5.45,-1.01,-9.6,5.31,-1.12,-9.76,5.38,-0.96,-9.8,5.45,-1.29,-9.84,5.28,-1.41,-9.88,5.22,-1.39,-9.92,5.24,-1.32,-9.64,4.81,-1.34,-9.72,4.71,-1.47,-9.72,4.8,-1.33,-10,4.65,-1.05,-9.92,4.57,-1.07,-10,4.55,-1.34,-9.72,4.71,-0.93,-9.68,4.63,-1.05,-9.92,4.57,-0.81,-9.76,4.53,-0.79,-9.88,4.51,-0.91,-9.84,4.53,-0.71,-9.72,4.46,-0.79,-9.88,4.51,-0.81,-9.76,4.53,-0.52,-9.68,4.5,-0.47,-9.68,4.51,-0.5,-9.88,4.52,-0.16,-9.52,4.46,-0.35,-9.64,4.49,-0.27,-9.36,4.59,0.04,-9.72,4.46,0.06,-9.84,4.52,0.01,-9.84,4.52,0.42,-9.8,4.43,0.37,-9.72,4.39,0.41,-9.72,4.39,0.57,-9.88,4.48,0.46,-9.72,4.38,0.65,-9.72,4.35,1.27,-9.76,4.43,1.26,-9.48,4.41,1.4,-9.52,4.71,1.29,-9.8,4.57,1.27,-9.76,4.43,1.4,-9.52,4.71,1.36,-9.76,4.8,1.34,-9.56,4.91,1.27,-9.68,4.97,1.27,-9.8,4.83,1.36,-9.76,4.8,1.27,-9.68,4.97,1.26,-9.6,4.97,1.34,-9.56,4.91,1.29,-9.44,4.95,1.11,-9.72,5.07,1.11,-9.8,5.04,1.27,-9.68,4.97,1.05,-9.76,5.07,0.98,-9.72,5.08,0.98,-9.76,5.08,0.98,-9.72,5.08,0.95,-9.72,5.1,0.98,-9.76,5.08,0.95,-9.72,5.1,0.9,-9.8,5.09,0.98,-9.76,5.08,0.63,-9.76,5.22,0.56,-9.72,5.24,0.51,-9.8,5.24,0.56,-9.72,5.24,0.63,-9.76,5.22,0.7,-9.72,5.2,0.41,-9.72,5.27,0.47,-9.76,5.28,0.56,-9.72,5.24,0.33,-9.68,5.28,0.3,-9.76,5.33,0.38,-9.8,5.28,0.22,-9.64,5.31,0.3,-9.76,5.33,0.33,-9.68,5.28,0.02,-9.88,5.37,-0.01,-9.64,5.38,-0.15,-9.72,5.43,0.38,-9.8,5.28,0.47,-9.76,5.28,0.41,-9.72,5.27,0.38,-9.8,5.28,0.3,-9.76,5.33,0.29,-9.88,5.29,0.02,-9.88,5.37,-0.15,-9.72,5.43,-0.24,-9.8,5.47,-0.15,-9.72,5.43,-0.01,-9.64,5.38,-0.16,-9.6,5.38,-0.24,-9.8,5.47,-0.31,-9.84,5.49,-0.25,-9.88,5.46,-0.31,-9.84,5.49,-0.31,-9.76,5.45,-0.37,-9.76,5.48,-0.56,-9.8,5.51,-0.52,-9.72,5.48,-0.64,-9.76,5.49,-0.56,-9.8,5.51,-0.64,-9.76,5.49,-0.73,-9.88,5.48,-0.75,-9.68,5.42,-0.96,-9.8,5.45,-0.73,-9.88,5.48,-0.73,-9.88,5.48,-0.96,-9.8,5.45,-0.87,-9.92,5.43,-0.97,-9.88,5.42,-1.12,-9.76,5.38,-1.16,-9.88,5.34,-1.47,-9.72,4.8,-1.5,-9.72,4.89,-1.32,-9.64,4.81,-0.33,-9.88,4.54,-0.5,-9.88,4.52,-0.47,-9.68,4.51,-0.62,-9.72,4.5,-0.52,-9.68,4.5,-0.5,-9.88,4.52,-0.28,-9.84,4.51,-0.47,-9.68,4.51,-0.35,-9.64,4.49,0.22,-9.92,4.57,0.24,-9.76,4.43,0.28,-9.88,4.55,0.24,-9.76,4.43,0.37,-9.72,4.39,0.42,-9.8,4.43,0.42,-9.8,4.43,0.41,-9.72,4.39,0.46,-9.72,4.38,0.57,-9.88,4.48,0.65,-9.72,4.35,0.82,-9.88,4.41,0.87,-9.84,4.38,0.87,-9.88,4.41,0.82,-9.88,4.41,0.95,-9.76,4.28,0.65,-9.72,4.35,0.8,-9.6,4.24,1.21,-9.88,4.47,1.2,-9.76,4.37,1.27,-9.76,4.43,1.21,-9.88,4.47,1.12,-9.84,4.42,1.2,-9.76,4.37,1.27,-9.8,4.83,1.27,-9.68,4.97,1.18,-9.84,4.98,1.4,-9.52,4.71,1.31,-9.84,4.66,1.29,-9.8,4.57,1.19,-9.6,5.02,1.11,-9.72,5.07,1.27,-9.68,4.97,1.08,-9.8,5.05,1.11,-9.8,5.04,1.11,-9.72,5.07,0.9,-9.8,5.09,0.7,-9.72,5.2,0.68,-9.8,5.18,0.9,-9.8,5.09,0.77,-9.68,5.18,0.7,-9.72,5.2,0.77,-9.68,5.18,0.9,-9.8,5.09,0.95,-9.72,5.1,0.68,-9.8,5.18,0.63,-9.76,5.22,0.63,-9.8,5.22,0.63,-9.76,5.22,0.68,-9.8,5.18,0.7,-9.72,5.2,0.51,-9.8,5.24,0.56,-9.72,5.24,0.47,-9.76,5.28,0.47,-9.76,5.28,0.46,-9.8,5.27,0.51,-9.8,5.24,-0.75,-9.68,5.42,-0.73,-9.88,5.48,-0.64,-9.76,5.49,-0.97,-9.88,5.42,-0.97,-9.92,5.39,-0.87,-9.92,5.43,-0.97,-9.88,5.42,-0.96,-9.8,5.45,-1.12,-9.76,5.38,-1.29,-9.84,5.28,-1.12,-9.76,5.38,-1.29,-9.6,5.21,-1.41,-9.88,5.22,-1.34,-9.56,5.13,-1.39,-9.56,4.98,-1.5,-9.72,4.89,-1.47,-9.72,4.8,-1.55,-9.96,4.85,-0.84,-9.72,4.55,-0.81,-9.76,4.53,-0.91,-9.84,4.53,-0.28,-9.84,4.51,-0.29,-9.88,4.54,-0.33,-9.88,4.54,0.01,-9.84,4.52,-0.28,-9.84,4.51,0.04,-9.72,4.46,0.95,-9.76,4.28,0.87,-9.84,4.38,0.65,-9.72,4.35,0.94,-9.84,4.36,0.87,-9.84,4.38,0.95,-9.76,4.28,0.95,-9.76,4.28,0.8,-9.6,4.24,1.08,-9.6,4.31,0.95,-9.76,4.28,1.12,-9.84,4.42,0.94,-9.84,4.36,0.95,-9.76,4.28,1.08,-9.6,4.31,1.2,-9.76,4.37,1.27,-9.76,4.43,1.2,-9.76,4.37,1.22,-9.56,4.32,1.29,-9.8,4.57,1.25,-9.84,4.55,1.27,-9.76,4.43,1.26,-9.84,4.58,1.25,-9.84,4.55,1.29,-9.8,4.57,1.4,-9.52,4.71,1.36,-9.76,4.8,1.31,-9.84,4.66,1.27,-9.8,4.83,1.31,-9.84,4.84,1.33,-9.84,4.79,1.11,-9.8,5.04,1.18,-9.84,4.98,1.27,-9.68,4.97,1.18,-9.84,4.98,1.11,-9.8,5.04,1.1,-9.84,5.03,0.43,-9.84,5.25,0.38,-9.8,5.28,0.29,-9.88,5.29,0,-9.56,5.36,-0.01,-9.64,5.38,0.22,-9.64,5.31,-0.31,-9.84,5.49,-0.37,-9.76,5.48,-0.43,-9.84,5.5,-0.52,-9.72,5.48,-0.43,-9.84,5.5,-0.37,-9.76,5.48,-0.56,-9.8,5.51,-0.57,-9.84,5.5,-0.43,-9.84,5.5,-0.97,-9.88,5.42,-0.87,-9.92,5.43,-0.96,-9.8,5.45,-1.29,-9.84,5.28,-1.28,-9.88,5.28,-1.16,-9.88,5.34,-1.49,-9.92,5.13,-1.5,-9.72,4.89,-1.55,-9.92,5.02,-0.89,-9.92,4.54,-0.79,-9.88,4.51,-0.78,-9.92,4.52,-0.71,-9.72,4.46,-0.62,-9.72,4.5,-0.79,-9.88,4.51,-0.28,-9.84,4.51,-0.16,-9.52,4.46,0.04,-9.72,4.46,0.01,-9.84,4.52,0.06,-9.84,4.52,0.09,-9.88,4.59,0.14,-9.88,4.58,0.09,-9.88,4.59,0.06,-9.84,4.52,0.28,-9.88,4.55,0.24,-9.76,4.43,0.42,-9.8,4.43,0.28,-9.88,4.55,0.42,-9.8,4.43,0.57,-9.88,4.48,0.57,-9.88,4.48,0.42,-9.8,4.43,0.46,-9.72,4.38,0.46,-9.72,4.38,0.49,-9.68,4.29,0.65,-9.72,4.35,1.21,-9.88,4.47,1.27,-9.76,4.43,1.25,-9.84,4.55,1.29,-9.88,4.56,1.31,-9.84,4.66,1.33,-9.96,4.72,1.33,-9.96,4.72,1.33,-9.84,4.79,1.34,-9.88,4.82,1.33,-9.84,4.79,1.36,-9.76,4.8,1.27,-9.8,4.83,0.33,-9.68,5.28,0.38,-9.8,5.28,0.41,-9.72,5.27,0.3,-9.76,5.33,0.2,-9.84,5.33,0.29,-9.88,5.29,0.29,-9.88,5.29,0.2,-9.84,5.33,0.19,-9.88,5.32,-0.25,-9.88,5.46,0.02,-9.88,5.37,-0.24,-9.8,5.47,-0.25,-9.88,5.46,-0.31,-9.84,5.49,-0.32,-9.88,5.48,-1.39,-9.92,5.24,-1.41,-9.88,5.22,-1.49,-9.92,5.13,-1.5,-9.72,4.89,-1.55,-9.96,4.85,-1.55,-9.92,5.02,-1.44,-9.92,4.71,-1.34,-9.72,4.71,-1.33,-10,4.65,-0.91,-9.84,4.53,-0.89,-9.92,4.54,-0.96,-9.96,4.52,-0.96,-9.96,4.52,-0.89,-9.92,4.54,-0.89,-9.96,4.5,-0.89,-9.92,4.54,-0.91,-9.84,4.53,-0.79,-9.88,4.51,0.02,-9.92,4.6,0.09,-9.88,4.59,0.1,-9.92,4.59,0.09,-9.88,4.59,0.14,-9.88,4.58,0.1,-9.92,4.59,0.1,-9.92,4.59,0.14,-9.88,4.58,0.22,-9.92,4.57,0.22,-9.92,4.57,0.28,-9.88,4.55,0.29,-9.92,4.55,0.22,-9.92,4.57,0.14,-9.88,4.58,0.24,-9.76,4.43,1.25,-9.92,4.51,1.21,-9.88,4.47,1.25,-9.84,4.55,1.29,-9.88,4.56,1.29,-9.92,4.56,1.25,-9.92,4.51,1.29,-9.88,4.56,1.25,-9.92,4.51,1.25,-9.84,4.55,1.33,-9.96,4.72,1.31,-9.84,4.66,1.33,-9.84,4.79,1.33,-9.84,4.79,1.31,-9.84,4.66,1.36,-9.76,4.8,-1.45,-10,4.78,-1.55,-9.96,4.85,-1.44,-9.92,4.71,-1.55,-9.96,4.85,-1.47,-9.72,4.8,-1.44,-9.92,4.71,-1.44,-9.92,4.71,-1.33,-10,4.65,-1.45,-10,4.78,-0.93,-9.68,4.63,-0.91,-9.84,4.53,-1.05,-9.92,4.57,-0.91,-9.84,4.53,-0.96,-9.96,4.52,-1.05,-9.92,4.57,-0.84,-9.72,4.55,-0.93,-9.68,4.63,-0.97,-9.64,4.47,1.24,-9.96,4.49,1.25,-9.92,4.51,1.28,-9.96,4.54,1.28,-9.96,4.54,1.25,-9.92,4.51,1.29,-9.92,4.56,1.28,-9.96,4.54,1.29,-9.92,4.56,1.31,-9.96,4.62,1.34,-9.96,4.82,1.33,-9.96,4.72,1.34,-9.88,4.82,-0.72,-9.36,5.31,-0.75,-9.36,5.32,-0.67,-9.32,5.3,-0.72,-9.36,5.31,-0.67,-9.32,5.3,-0.64,-9.36,5.29,-0.64,-9.36,5.29,-0.67,-9.32,5.3,-0.68,-9.36,5.34,-0.76,-9.4,5.36,-0.75,-9.36,5.32,-0.73,-9.4,5.31,-0.75,-9.36,5.32,-0.72,-9.36,5.31,-0.73,-9.4,5.31,-0.3,-9.16,5.04,-0.26,-9.16,5.04,-0.25,-9.2,5.1])

IndexedFaceSet351.setCoord(Coordinate352)

Shape348.setGeometry(IndexedFaceSet351)

Transform347.addChildren(Shape348)

fieldValue346.addChildren(Transform347)

ProtoInstance344.addFieldValue(fieldValue346)

fieldValue343.addChildren(ProtoInstance344)

ProtoInstance340.addFieldValue(fieldValue343)

fieldValue329.addChildren(ProtoInstance340)

ProtoInstance326.addFieldValue(fieldValue329)

fieldValue315.addChildren(ProtoInstance326)

ProtoInstance312.addFieldValue(fieldValue315)

fieldValue301.addChildren(ProtoInstance312)
ProtoInstance353 = ProtoInstance()
ProtoInstance353.setName("Joint")
ProtoInstance353.setDEF("Allen_hanim_r_hip")
fieldValue354 = fieldValue()
fieldValue354.setName("name")
fieldValue354.setValue("r_hip")

ProtoInstance353.addFieldValue(fieldValue354)
fieldValue355 = fieldValue()
fieldValue355.setName("center")
fieldValue355.setValue("-0.11 0.892362 -0.0732533")

ProtoInstance353.addFieldValue(fieldValue355)
fieldValue356 = fieldValue()
fieldValue356.setName("children")
ProtoInstance357 = ProtoInstance()
ProtoInstance357.setName("Segment")
ProtoInstance357.setDEF("Allen_hanim_r_thigh")
fieldValue358 = fieldValue()
fieldValue358.setName("name")
fieldValue358.setValue("r_thigh")

ProtoInstance357.addFieldValue(fieldValue358)
fieldValue359 = fieldValue()
fieldValue359.setName("children")
Transform360 = Transform()
Transform360.setDEF("r_thigh_adjust")
Transform360.setCenter([0.43,1.1,-0.05])
Transform360.setRotation([0,1,0,1.570796])
Transform360.setScale([0.1,0.1,0.1])
Shape361 = Shape()
Appearance362 = Appearance()
Material363 = Material()
Material363.setUSE("Pants_Color")

Appearance362.setMaterial(Material363)
ImageTexture364 = ImageTexture()
ImageTexture364.setUSE("camo")

Appearance362.setTexture(ImageTexture364)

Shape361.setAppearance(Appearance362)
IndexedFaceSet365 = IndexedFaceSet()
IndexedFaceSet365.setCoordIndex([0,1,2,-1,3,4,5,-1,6,7,8,-1,9,10,11,-1,12,13,14,-1,15,16,17,-1,18,19,20,-1,21,22,23,-1,24,25,26,-1,27,28,29,-1,30,31,32,-1,33,34,35,-1,36,37,38,-1,39,40,41,-1,42,43,44,-1,45,46,47,-1,48,49,50,-1,51,52,53,-1,54,55,56,-1,57,58,59,-1,60,61,62,-1,63,64,65,-1,66,67,68,-1,69,70,71,-1,72,73,74,-1,75,76,77,-1,78,79,80,-1,81,82,83,-1,84,85,86,-1,87,88,89,-1,90,91,92,-1,93,94,95,-1,96,97,98,-1,99,100,101,-1,102,103,104,-1,105,106,107,-1,108,109,110,-1,111,112,113,-1,114,115,116,-1,117,118,119,-1,120,121,122,-1,123,124,125,-1,126,127,128,-1,129,130,131,-1,132,133,134,-1,135,136,137,-1,138,139,140,-1,141,142,143,-1,144,145,146,-1,147,148,149,-1,150,151,152,-1,153,154,155,-1,156,157,158,-1,159,160,161,-1,162,163,164,-1,165,166,167,-1,168,169,170,-1,171,172,173,-1,174,175,176,-1,177,178,179,-1,180,181,182,-1,183,184,185,-1,186,187,188,-1,189,190,191,-1,192,193,194,-1,195,196,197,-1,198,199,200,-1,201,202,203,-1,204,205,206,-1,207,208,209,-1,210,211,212,-1,213,214,215,-1,216,217,218,-1,219,220,221,-1,222,223,224,-1,225,226,227,-1,228,229,230,-1,231,232,233,-1,234,235,236,-1,237,238,239,-1,240,241,242,-1,243,244,245,-1,246,247,248,-1,217,220,218,-1,222,226,223,-1,195,198,196,-1,198,200,196,-1,249,202,200,-1,200,202,196,-1,201,205,202,-1,218,220,214,-1,219,223,220,-1,202,205,196,-1,220,223,214,-1,215,214,212,-1,212,214,210,-1,214,223,210,-1,223,226,210,-1,204,208,205,-1,207,210,208,-1,210,226,208,-1,205,208,196,-1,208,226,196,-1,250,251,252,-1,253,254,255,-1,256,257,258,-1,259,260,261,-1,262,263,264,-1,265,266,267,-1,268,269,270,-1,271,272,273,-1,274,275,276,-1,277,278,279,-1,280,281,282,-1,283,284,285,-1,286,287,288,-1,289,290,291,-1,292,293,294,-1,295,296,297,-1,298,299,300,-1,301,302,303,-1,304,305,306,-1,307,308,309,-1,310,311,312,-1,313,314,315,-1,316,317,318,-1,319,320,321,-1,322,323,324,-1,325,326,327,-1,328,329,330,-1,331,332,333,-1,334,335,336,-1,337,338,339,-1,340,341,342,-1,343,344,345,-1,346,347,348,-1,349,350,351,-1,352,353,354,-1,355,356,357,-1,358,359,360,-1,361,362,363,-1,364,365,366,-1,367,368,369,-1,370,371,372,-1,373,374,375,-1,376,377,378,-1,379,380,381,-1,382,383,384,-1,383,382,384,-1,385,386,387,-1,388,389,390,-1,391,392,393,-1,394,395,396,-1,397,398,399,-1,400,401,402,-1,403,404,405,-1,406,407,408,-1,407,406,408,-1,409,410,411,-1,409,411,410,-1,412,413,414,-1,415,416,417,-1,418,419,420,-1,421,422,423,-1,424,425,426,-1,427,428,429,-1,428,427,429,-1,430,431,432,-1,433,434,435,-1,436,437,438,-1,439,440,441,-1,442,443,444,-1,445,446,447,-1,448,449,450,-1,451,452,453,-1,454,455,456,-1,455,454,456,-1,457,458,459,-1,460,461,462,-1,463,464,465,-1,466,467,468,-1,469,470,471,-1,472,473,474,-1,475,476,477,-1,478,479,480,-1,481,482,483,-1,484,485,486,-1,487,488,489,-1,490,491,492,-1,493,494,495,-1,496,497,498,-1,498,497,496,-1,499,500,501,-1,502,503,504,-1,505,506,507,-1,508,509,510,-1,511,512,513,-1,514,515,516,-1,517,518,519,-1,520,521,522,-1,523,524,525,-1,526,527,528,-1,529,530,531,-1,532,533,534,-1,533,532,534,-1,535,536,537,-1,538,539,540,-1,538,540,539,-1,541,542,543,-1,544,545,546,-1,547,548,549,-1,550,551,552,-1,553,554,555,-1,556,557,558,-1,559,560,561,-1,562,563,564,-1,565,566,567,-1,566,565,567,-1,568,569,570,-1,571,572,573,-1,574,575,576,-1,577,578,579,-1,580,581,582,-1,583,584,585,-1,586,587,588,-1,589,590,591,-1,590,589,591,-1,592,593,594,-1,595,596,597,-1,598,599,600,-1,601,602,603,-1,604,605,606,-1,607,608,609,-1,607,609,608,-1,610,611,612,-1,613,614,615,-1,613,615,614,-1,616,617,618,-1,619,620,621,-1,622,623,624,-1,625,626,627,-1,628,629,630,-1,631,632,633,-1,632,631,633,-1,634,635,636,-1,634,636,635,-1,637,638,639,-1,639,638,637,-1,640,641,642,-1,643,644,645,-1,646,647,648,-1,649,650,651,-1,652,653,654,-1,655,656,657,-1,656,655,657,-1,658,659,660,-1,660,659,658,-1,661,662,663,-1,664,665,666,-1,666,665,664,-1,667,668,669,-1,670,671,672,-1,673,674,675,-1,676,677,678,-1,679,680,681,-1,680,679,681,-1,682,683,684,-1,685,686,687,-1,688,689,690,-1,691,692,693,-1,694,695,696,-1,697,698,699,-1,700,701,702,-1,703,704,705,-1,706,707,708,-1,707,706,708,-1,709,710,711,-1,710,709,711,-1,712,713,714,-1,715,716,717,-1,718,719,720,-1,721,722,723,-1,724,725,726,-1,727,728,729,-1,728,727,729,-1,730,731,732,-1,733,734,735,-1,736,737,738,-1,739,740,741,-1,742,743,744,-1,745,746,747,-1,748,749,750,-1,751,752,753,-1,754,755,756,-1,757,758,759,-1,760,761,762,-1,763,764,765,-1,766,767,768,-1,769,770,771,-1,772,773,774,-1,775,776,777,-1,778,779,780,-1,781,782,783,-1,784,785,786,-1,787,788,789,-1,790,791,792,-1,793,794,795,-1,796,797,798,-1,799,800,801,-1,800,799,801,-1,802,803,804,-1,803,802,804,-1,805,806,807,-1,808,809,810,-1,811,812,813,-1,814,815,816,-1,817,818,819,-1,820,821,822,-1,823,824,825,-1,826,827,828,-1,829,830,831,-1,832,833,834,-1,835,836,837,-1,838,839,840,-1,841,842,843,-1,844,845,846,-1,847,848,849,-1,850,851,852,-1,853,854,855,-1,853,855,854,-1,856,857,858,-1,859,860,861,-1,862,863,864,-1,865,866,867,-1,868,869,870,-1,871,872,873,-1,874,875,876,-1,877,878,879,-1,880,881,882,-1,880,882,881,-1,883,884,885,-1,886,887,888,-1,889,890,891,-1,892,893,894,-1,895,896,897,-1,898,899,900,-1,901,902,903,-1,904,905,906,-1,907,908,909,-1,910,911,912,-1,913,914,915,-1,916,917,918,-1,919,920,921,-1,922,923,924,-1,925,926,927,-1,925,927,926,-1,928,929,930,-1,931,932,933,-1,934,935,936,-1,937,938,939,-1,940,941,942,-1,943,944,945,-1,946,947,948,-1,949,950,951,-1,952,953,954,-1,955,956,957,-1,958,959,960,-1,961,962,963,-1,964,965,966,-1,967,968,969,-1,970,971,972,-1,973,974,975,-1,976,977,978,-1,979,980,981,-1,982,983,984,-1,985,986,987,-1,988,989,990,-1,991,992,993,-1,994,995,996,-1,997,998,999,-1,1000,1001,1002,-1,1003,1004,1005,-1,1006,1007,1008,-1,1009,1010,1011,-1,1012,1013,1014,-1,1015,1016,1017,-1,1018,1019,1020,-1,1021,1022,1023,-1,1024,1025,1026,-1,1027,1028,1029,-1,1030,1031,1032,-1,1033,1034,1035,-1,1036,1037,1038,-1,1039,1040,1041,-1,1042,1043,1044,-1,1045,1046,1047,-1,1048,1049,1050,-1,1051,1052,1053,-1,1054,1055,1056,-1,1057,1058,1059,-1,1060,1061,1062,-1,1063,1064,1065,-1,1066,1067,1068,-1,1069,1070,1071,-1,1072,1073,1074,-1,1075,1076,1077,-1,1078,1079,1080,-1,1081,1082,1083,-1,1084,1085,1086,-1,1087,1088,1089,-1,1090,1091,1092,-1,1093,1094,1095,-1,1096,1097,1098,-1,1099,1100,1101,-1,1102,1103,1104,-1,1105,1106,1107,-1,1108,1109,1110,-1,1111,1112,1113,-1,1114,1115,1116,-1,1117,1118,1119,-1,1120,1121,1122,-1,1123,1124,1125,-1,1126,1127,1128,-1,1129,1130,1131,-1,1132,1133,1134,-1,1135,1136,1137,-1,1138,1139,1140,-1,1141,1142,1143,-1,1144,1145,1146,-1,1147,1148,1149,-1,1150,1151,1152,-1,1153,1154,1155,-1,1156,1157,1158,-1,1159,1160,1161,-1,1162,1163,1164,-1,1165,1166,1167,-1,1168,1169,1170,-1,1171,1172,1173,-1,1174,1175,1176,-1,1177,1178,1179,-1,1180,1181,1182,-1,1183,1184,1185,-1,1186,1187,1188,-1,1189,1190,1191,-1,1192,1193,1194,-1,1195,1196,1197,-1,1198,1199,1200,-1,1201,1202,1203,-1,1204,1205,1206,-1,1207,1208,1209,-1,1210,1211,1212,-1,1213,1214,1215,-1,1216,1217,1218,-1,1219,1220,1221,-1,1222,1223,1224,-1,1225,1226,1227,-1,1228,1229,1230,-1,1231,1232,1233,-1,1234,1235,1236,-1,1237,1238,1239,-1,1240,1241,1242,-1,1243,1244,1245,-1,1246,1247,1248,-1,1249,1250,1251,-1,1252,1253,1254,-1,1255,1256,1257,-1,1258,1259,1260,-1,1261,1262,1263,-1,1264,1265,1266,-1,1267,1268,1269,-1,1270,1271,1272,-1,1273,1274,1275,-1,1276,1277,1278,-1,1279,1280,1281,-1,1282,1283,1284,-1,1285,1286,1287,-1,1288,1289,1290,-1,1291,1292,1293,-1,1294,1295,1296,-1,1297,1298,1299,-1,1300,1301,1302,-1,1303,1304,1305,-1,1306,1307,1308,-1,1309,1310,1311,-1,1312,1313,1314,-1,1315,1316,1317,-1,1318,1319,1320,-1,1321,1322,1323,-1,1324,1325,1326,-1,1327,1328,1329,-1,1330,1331,1332,-1,1333,1334,1335,-1,1336,1337,1338,-1,1339,1340,1341,-1,1342,1343,1344,-1,1345,1346,1347,-1,1348,1349,1350,-1,1351,1352,1353,-1,1354,1355,1356,-1,1357,1358,1359,-1,1360,1361,1362,-1,1363,1364,1365,-1,1366,1367,1368,-1,1369,1370,1371,-1,1372,1373,1374,-1,1375,1376,1377,-1,1378,1379,1380,-1,1381,1382,1383,-1,1384,1385,1386,-1,1387,1388,1389,-1,1390,1391,1392,-1,1393,1394,1395,-1,1396,1397,1398,-1,1399,1400,1401,-1,1402,1403,1404,-1,1405,1406,1407,-1,1408,1409,1410,-1,1411,1412,1413,-1,1414,1415,1416,-1,1417,1418,1419,-1,1420,1421,1422,-1,1423,1424,1425,-1,1426,1427,1428,-1,1429,1430,1431,-1,1432,1433,1434,-1,1435,1436,1437,-1,1438,1439,1440,-1,1441,1442,1443,-1,1444,1445,1446,-1,1447,1448,1449,-1,1450,1451,1452,-1,1453,1454,1455,-1,1456,1457,1458,-1,1459,1460,1461,-1,1462,1463,1464,-1,1465,1466,1467,-1,1468,1469,1470,-1,1471,1472,1473,-1,1474,1475,1476,-1,1477,1478,1479,-1,1480,1481,1482,-1,1483,1484,1485,-1,1486,1487,1488,-1,1489,1490,1491,-1,1492,1493,1494,-1,1495,1496,1497,-1,1498,1499,1500,-1,1501,1502,1503,-1,1504,1505,1506,-1,1507,1508,1509,-1,1510,1511,1512,-1,1513,1514,1515,-1,1516,1517,1518,-1,1519,1520,1521,-1,1522,1523,1524,-1,1525,1526,1527,-1,1528,1529,1530,-1,1531,1532,1533,-1,1534,1535,1536,-1,1537,1538,1539,-1,1540,1541,1542,-1,1543,1544,1545,-1,1546,1547,1548,-1,1549,1550,1551,-1,1552,1553,1554,-1,1555,1556,1557,-1,1558,1559,1560,-1,1561,1562,1563,-1,1564,1565,1566,-1,1567,1568,1569,-1,1570,1571,1572,-1,1573,1574,1575,-1,1576,1577,1578,-1,1579,1580,1581,-1,1582,1583,1584,-1,1585,1586,1587,-1,1588,1589,1590,-1,1591,1592,1593,-1,1594,1595,1596,-1,1597,1598,1599,-1,1600,1601,1602,-1,1603,1604,1605,-1,1606,1607,1608,-1,1609,1610,1611,-1,1612,1613,1614,-1,1615,1616,1617,-1,1618,1619,1620,-1,1621,1622,1623,-1,1624,1625,1626,-1,1627,1628,1629,-1,1630,1631,1632,-1,1633,1634,1635,-1,1636,1637,1638,-1,1639,1640,1641,-1,1642,1643,1644,-1,1645,1646,1647,-1,1648,1649,1650,-1,1651,1652,1653,-1,1654,1655,1656,-1,1657,1658,1659,-1,1660,1661,1662,-1,1663,1664,1665,-1,1666,1667,1668,-1,1669,1670,1671,-1,1672,1673,1674,-1,1675,1676,1677,-1,1678,1679,1680,-1,1681,1682,1683,-1,1684,1685,1686,-1,1687,1688,1689,-1,1690,1691,1692,-1,1693,1694,1695,-1,1696,1697,1698,-1,1699,1700,1701,-1,1702,1703,1704,-1,1705,1706,1707,-1,1708,1709,1710,-1,1711,1712,1713,-1,1714,1715,1716,-1,1717,1718,1719,-1,1720,1721,1722,-1,1723,1724,1725,-1,1726,1727,1728,-1,1729,1730,1731,-1,1732,1733,1734,-1,1735,1736,1737,-1,1738,1739,1740,-1,1741,1742,1743,-1,1744,1745,1746,-1,1747,1748,1749,-1,1750,1751,1752,-1,1753,1754,1755,-1,1756,1757,1758,-1,1759,1760,1761,-1,1762,1763,1764,-1,1765,1766,1767,-1,1768,1769,1770,-1,1771,1772,1773,-1,1774,1775,1776,-1,1777,1778,1779,-1,1780,1781,1782,-1,1783,1784,1785,-1,1786,1787,1788,-1,1789,1790,1791,-1,1792,1793,1794,-1,1795,1796,1797,-1,1798,1799,1800,-1,1801,1802,1803,-1,1804,1805,1806,-1,1807,1808,1809,-1,1810,1811,1812,-1,1813,1814,1815,-1,1816,1817,1818,-1,1819,1820,1821,-1,1822,1823,1824,-1,1825,1826,1827,-1,1828,1829,1830,-1,1831,1832,1833,-1,1834,1835,1836,-1,1837,1838,1839,-1,1840,1841,1842,-1,1843,1844,1845,-1,1846,1847,1848,-1,1849,1850,1851,-1,1852,1853,1854,-1,1855,1856,1857,-1,1858,1859,1860,-1,1861,1862,1863,-1,1864,1865,1866,-1,1867,1868,1869,-1,1870,1871,1872,-1,1873,1874,1875,-1,1876,1877,1878,-1,1879,1880,1881,-1,1882,1883,1884,-1,1885,1886,1887,-1,1888,1889,1890,-1,1891,1892,1893,-1,1894,1895,1896,-1,1897,1898,1899,-1,1900,1901,1902,-1,1903,1904,1905,-1,1906,1907,1908,-1,1909,1910,1911,-1,1912,1913,1914,-1,1915,1916,1917,-1,1918,1919,1920,-1,1921,1922,1923,-1,1924,1925,1926,-1,1927,1928,1929,-1,1930,1931,1932,-1,1933,1934,1935,-1,1936,1937,1938,-1,1939,1940,1941,-1,1942,1943,1944,-1,1945,1946,1947,-1,1948,1949,1950,-1,1951,1952,1953,-1,1954,1955,1956,-1,1957,1958,1959,-1,1960,1961,1962,-1,1963,1964,1965,-1,1966,1967,1968,-1,1969,1970,1971,-1,1972,1973,1974,-1,1975,1976,1977,-1,1978,1979,1980,-1,1981,1982,1983,-1,1984,1985,1986,-1,1987,1988,1989,-1,1990,1991,1992,-1,1993,1994,1995,-1,1996,1997,1998,-1,1999,2000,2001,-1,2002,2003,2004,-1,2005,2006,2007,-1,2008,2009,2010,-1,2011,2012,2013,-1,2014,2015,2016,-1,2017,2018,2019,-1,2020,2021,2022,-1,2023,2024,2025,-1,2026,2027,2028,-1,2029,2030,2031,-1,2032,2033,2034,-1,2035,2036,2037,-1,2038,2039,2040,-1,2041,2042,2043,-1,2044,2045,2046,-1,2047,2048,2049,-1,2050,2051,2052,-1,2053,2054,2055,-1,2056,2057,2058,-1,2059,2060,2061,-1,2062,2063,2064,-1,2065,2066,2067,-1,2068,2069,2070,-1,2071,2072,2073,-1,2074,2075,2076,-1,2077,2078,2079,-1,2080,2081,2082,-1,2083,2084,2085,-1,2086,2087,2088,-1,2089,2090,2091,-1,2092,2093,2094,-1,2095,2096,2097,-1,2098,2099,2100,-1,2101,2102,2103,-1,2104,2105,2106,-1,2107,2108,2109,-1,2110,2111,2112,-1,2113,2114,2115,-1,2116,2117,2118,-1,2119,2120,2121,-1,2122,2123,2124,-1,2125,2126,2127,-1,2128,2129,2130,-1,2131,2132,2133,-1,2134,2135,2136,-1,2137,2138,2139,-1,2140,2141,2142,-1,2143,2144,2145,-1,2146,2147,2148,-1,2149,2150,2151,-1,2152,2153,2154,-1,2155,2156,2157,-1,2158,2159,2160,-1,2161,2162,2163,-1,2164,2165,2166,-1,2167,2168,2169,-1,2170,2171,2172,-1,2173,2174,2175,-1,2176,2177,2178,-1,2179,2180,2181,-1,2182,2183,2184,-1,2185,2186,2187,-1,2188,2189,2190,-1,2191,2192,2193,-1,2194,2195,2196,-1,2197,2198,2199,-1,2200,2201,2202,-1,2203,2204,2205,-1,2206,2207,2208,-1,2209,2210,2211,-1,2212,2213,2214,-1,2215,2216,2217,-1,2218,2219,2220,-1,2221,2222,2223,-1,2224,2225,2226,-1,2227,2228,2229,-1,2230,2231,2232,-1,2233,2234,2235,-1,2236,2237,2238,-1,2239,2240,2241,-1,2242,2243,2244,-1,2245,2246,2247,-1,2248,2249,2250,-1,2251,2252,2253,-1,2254,2255,2256,-1,2257,2258,2259,-1,2260,2261,2262,-1,2263,2264,2265,-1,2266,2267,2268,-1,2269,2270,2271,-1,2272,2273,2274,-1,2275,2276,2277,-1,2278,2279,2280,-1,2281,2282,2283,-1,2284,2285,2286,-1,2287,2288,2289,-1,2290,2291,2292,-1,2293,2294,2295,-1,2296,2297,2298,-1,2299,2300,2301,-1,2302,2303,2304,-1,2305,2306,2307,-1,2308,2309,2310,-1,2311,2312,2313,-1,2314,2315,2316,-1,2317,2318,2319,-1,2320,2321,2322,-1,2323,2324,2325,-1,2326,2327,2328,-1,2329,2330,2331,-1,2332,2333,2334,-1,2335,2336,2337,-1,2338,2339,2340,-1,2341,2342,2343,-1,2344,2345,2346,-1,2347,2348,2349,-1,2350,2351,2352,-1,2353,2354,2355,-1,2356,2357,2358,-1,2359,2360,2361,-1,2362,2363,2364,-1,2365,2366,2367,-1,2368,2369,2370,-1,2371,2372,2373,-1,2374,2375,2376,-1,2377,2378,2379,-1,2380,2381,2382,-1,2383,2384,2385,-1,2386,2387,2388,-1,2389,2390,2391,-1,2392,2393,2394,-1,2395,2396,2397,-1,2398,2399,2400,-1,2401,2402,2403,-1,2404,2405,2406,-1,2407,2408,2409,-1,2410,2411,2412,-1,2413,2414,2415,-1,2416,2417,2418,-1,2419,2420,2421,-1,2422,2423,2424,-1,2425,2426,2427,-1,2428,2429,2430,-1,2431,2432,2433,-1,2434,2435,2436,-1,2434,2436,2437,-1])
IndexedFaceSet365.setCreaseAngle(1.61)
Coordinate366 = Coordinate()
Coordinate366.setPoint([-0.77,-2.4,-5.57,-0.74,-2.76,-5.63,-0.68,-2.84,-5.04,-0.68,-2.84,-5.04,-0.53,-2.68,-4.56,-0.63,-2.48,-4.6,-0.77,-2.24,-5.2,-0.77,-2.4,-5.57,-0.68,-2.84,-5.04,-0.68,-2.84,-5.04,-0.72,-2.32,-4.69,-0.75,-2.28,-4.95,-0.74,-2.96,-5.47,-0.69,-3.4,-5.63,-0.68,-3.6,-5.34,-0.09,-2.64,-6.3,-0.45,-2.76,-6.05,-0.28,-2.48,-6.14,-0.53,-2.68,-4.56,-0.55,-2.52,-4.51,-0.63,-2.48,-4.6,-0.68,-2.84,-5.04,-0.63,-2.48,-4.6,-0.72,-2.32,-4.69,-0.74,-2.76,-5.63,-0.74,-2.96,-5.47,-0.68,-2.84,-5.04,-0.09,-2.64,-6.3,0.06,-2.8,-6.36,-0.28,-3.08,-6.18,-0.01,-2.56,-6.34,0.05,-2.56,-6.37,0.06,-2.8,-6.36,-0.45,-2.64,-4.47,-0.53,-2.68,-4.56,-0.44,-2.68,-4.47,-0.74,-2.76,-5.63,-0.77,-2.4,-5.57,-0.6,-2.44,-5.9,-0.6,-2.44,-5.9,-0.28,-2.48,-6.14,-0.45,-2.76,-6.05,-0.28,-3.08,-6.18,-0.4,-3.08,-6.09,-0.45,-2.76,-6.05,-0.09,-2.64,-6.3,-0.01,-2.56,-6.34,0.06,-2.8,-6.36,-0.44,-2.68,-4.47,-0.53,-2.68,-4.56,-0.43,-2.92,-4.55,-0.66,-2.96,-5.79,-0.6,-2.44,-5.9,-0.45,-2.76,-6.05,0.77,-2.84,-4.53,0.83,-2.96,-4.59,1,-2.8,-4.65,-0.55,-3.16,-4.84,-0.53,-3.24,-4.85,-0.45,-3.28,-4.73,0.22,-3.52,-6.39,0.8,-3.16,-6.34,0.75,-3.56,-6.4,1.48,-2.84,-5.28,1.49,-2.92,-5.14,1.33,-2.92,-5.25,1.16,-3,-4.91,1.41,-3,-5.04,1.48,-2.8,-5.11,-0.35,-2.88,-4.46,-0.39,-2.84,-4.44,-0.43,-2.92,-4.55,-0.66,-2.96,-5.79,-0.74,-2.76,-5.63,-0.6,-2.44,-5.9,0.06,-2.8,-6.36,-0.15,-3.16,-6.23,-0.28,-3.08,-6.18,0.99,-2.84,-6.15,1.09,-2.76,-6.17,1.11,-2.88,-6.12,0.9,-3.16,-4.74,1.04,-3.44,-4.7,1.16,-3.4,-4.75,-0.35,-2.88,-4.46,-0.43,-2.92,-4.55,-0.33,-2.92,-4.51,-0.68,-2.84,-5.04,-0.43,-2.92,-4.55,-0.53,-2.68,-4.56,-0.69,-3.4,-5.63,-0.74,-2.96,-5.47,-0.66,-2.96,-5.79,1.04,-2.92,-6.11,0.99,-2.84,-6.15,1.11,-2.88,-6.12,0.97,-2.8,-6.17,0.86,-2.88,-6.24,0.94,-2.76,-6.19,1.35,-2.88,-5.26,1.33,-2.92,-5.25,1.29,-2.92,-5.33,1.29,-2.8,-5.41,1.28,-3.04,-5.4,1.34,-3.04,-5.66,1.49,-2.92,-5.14,1.41,-3,-5.04,1.34,-3,-5.19,1.16,-3,-4.91,1.31,-3.08,-4.94,1.41,-3,-5.04,0.71,-2.84,-4.5,0.7,-2.88,-4.51,0.77,-2.84,-4.53,-0.35,-2.88,-4.46,-0.33,-2.92,-4.51,-0.32,-2.96,-4.48,-0.66,-2.96,-5.79,-0.45,-2.76,-6.05,-0.4,-3.08,-6.09,0.71,-2.96,-6.4,0.68,-2.76,-6.41,0.86,-2.88,-6.24,0.97,-2.8,-6.17,0.99,-2.84,-6.15,0.86,-2.88,-6.24,1.22,-2.96,-6.09,1.11,-2.88,-6.12,1.29,-2.8,-6.06,1.35,-3,-5.92,1.3,-2.72,-5.49,1.34,-3.04,-5.66,1.49,-2.92,-5.14,1.34,-3,-5.19,1.33,-2.92,-5.25,0.77,-2.84,-4.53,0.71,-2.96,-4.54,0.83,-2.96,-4.59,-0.32,-2.96,-4.52,-0.32,-2.96,-4.48,-0.33,-2.92,-4.51,-0.64,-3.16,-5.03,-0.55,-3.16,-4.84,-0.68,-2.84,-5.04,0.22,-3.52,-6.39,0.42,-2.76,-6.45,0.71,-2.96,-6.4,0.22,-3.52,-6.39,0.06,-2.8,-6.36,0.42,-2.76,-6.45,1.28,-3.04,-5.4,1.33,-2.92,-5.25,1.34,-3,-5.19,0.77,-2.84,-4.53,0.7,-2.88,-4.51,0.71,-2.96,-4.54,-0.3,-3,-4.5,-0.23,-3,-4.51,-0.32,-2.96,-4.48,-0.32,-2.96,-4.48,-0.32,-2.96,-4.52,-0.3,-3,-4.5,-0.22,-3.08,-4.52,-0.2,-3.04,-4.53,-0.23,-3,-4.51,-0.32,-2.96,-4.52,-0.33,-2.92,-4.51,-0.43,-2.92,-4.55,-0.43,-2.92,-4.55,-0.68,-2.84,-5.04,-0.55,-3.16,-4.84,-0.09,-2.64,-6.3,-0.28,-3.08,-6.18,-0.45,-2.76,-6.05,0.86,-2.88,-6.24,0.8,-3.16,-6.34,0.71,-2.96,-6.4,0.42,-2.76,-6.45,0.06,-2.8,-6.36,0.29,-2.56,-6.45,0.99,-2.84,-6.15,0.94,-3.08,-6.15,0.86,-2.88,-6.24,1.29,-2.8,-5.41,1.34,-3.04,-5.66,1.3,-2.72,-5.49,1.28,-3.04,-5.4,1.29,-2.92,-5.33,1.33,-2.92,-5.25,1.26,-3.4,-5.17,1.27,-3.32,-5.28,1.34,-3,-5.19,0.71,-2.96,-4.54,0.71,-3.04,-4.58,0.83,-2.96,-4.59,-0.22,-3.08,-4.52,-0.3,-3,-4.5,-0.33,-3.08,-4.55,-0.22,-3.08,-4.52,-0.33,-3.08,-4.55,-0.15,-3.28,-4.57,0.03,-3.72,-4.62,0.01,-3.68,-4.61,-0.06,-3.68,-4.63,0.07,-3.8,-4.61,0.03,-3.72,-4.62,-0.02,-3.88,-4.66,0.42,-2.76,-6.45,0.68,-2.76,-6.41,0.71,-2.96,-6.4,0.94,-2.76,-6.19,0.86,-2.88,-6.24,0.68,-2.76,-6.41,0.44,-3.64,-4.69,0.48,-3.8,-4.74,0.6,-3.76,-4.71,0.6,-3.76,-4.71,0.61,-3.8,-4.7,0.69,-3.8,-4.71,0.79,-3.76,-4.7,0.69,-3.8,-4.71,0.81,-3.88,-4.73,0.85,-3.72,-4.69,0.95,-3.8,-4.73,1.11,-3.6,-4.79,0.84,-3.56,-4.63,1.11,-3.6,-4.79,1.04,-3.44,-4.7,0.89,-3.36,-4.63,0.84,-3.48,-4.62,1.04,-3.44,-4.7,0.81,-3.44,-4.61,0.89,-3.36,-4.63,0.75,-3.4,-4.59,0.65,-3.32,-4.55,0.68,-3.36,-4.56,0.67,-3.28,-4.57,0.67,-3.12,-4.61,0.58,-3.16,-4.57,0.65,-3.24,-4.59,0.71,-3.04,-4.58,0.67,-3.12,-4.61,0.78,-3.2,-4.68,0.7,-2.88,-4.51,0.68,-2.96,-4.52,0.71,-2.96,-4.54,0.67,-2.88,-4.5,0.7,-2.88,-4.51,0.71,-2.84,-4.5,0,-3.52,-4.64,-0.22,-3.08,-4.52,-0.23,-3,-4.51,-0.3,-3,-4.5,0.22,-3.52,-6.39,0.71,-2.96,-6.4,0.8,-3.16,-6.34,1.22,-2.96,-6.09,1.35,-3,-5.92,1.19,-3.36,-5.92,1.41,-3,-5.04,1.49,-2.92,-5.14,1.48,-2.8,-5.11,0.9,-3.16,-4.74,0.78,-3.2,-4.68,0.89,-3.36,-4.63,0.83,-2.96,-4.59,0.71,-3.04,-4.58,0.9,-3.16,-4.74,0.69,-3.04,-4.55,0.71,-3.04,-4.58,0.71,-2.96,-4.54,-0.33,-3.08,-4.55,-0.3,-3,-4.5,-0.32,-2.96,-4.52,0.99,-2.84,-6.15,1.04,-2.92,-6.11,0.94,-3.08,-6.15,1.38,-3.4,-5.83,1.19,-3.36,-5.92,1.35,-3,-5.92,1.35,-3,-5.92,1.22,-2.96,-6.09,1.29,-2.8,-6.06,1.29,-2.8,-5.41,1.29,-2.92,-5.33,1.28,-3.04,-5.4,1.35,-2.88,-5.26,1.29,-2.92,-5.33,1.29,-2.8,-5.41,1.41,-3,-5.04,1.26,-3.4,-5.17,1.34,-3,-5.19,0.83,-2.96,-4.59,0.9,-3.16,-4.74,1.16,-3,-4.91,-0.33,-3.08,-4.55,-0.32,-2.96,-4.52,-0.43,-2.92,-4.55,0.94,-3.08,-6.15,1.09,-3,-6.07,1.19,-3.36,-5.92,1.35,-3,-5.92,1.34,-3.04,-5.66,1.41,-3.24,-5.71,1.09,-3,-6.07,1.22,-2.96,-6.09,1.19,-3.36,-5.92,1,-2.8,-4.65,0.83,-2.96,-4.59,1.16,-3,-4.91,-0.33,-3.08,-4.55,-0.55,-3.16,-4.84,-0.45,-3.28,-4.73,-0.33,-3.08,-4.55,-0.43,-2.92,-4.55,-0.55,-3.16,-4.84,-0.74,-2.96,-5.47,-0.74,-2.76,-5.63,-0.66,-2.96,-5.79,-0.54,-3.36,-5.92,-0.4,-3.08,-6.09,-0.23,-3.16,-6.18,-0.14,-3.4,-6.25,-0.41,-4,-6.05,-0.51,-3.68,-5.95,1.09,-3,-6.07,1.04,-2.92,-6.11,1.1,-2.96,-6.08,1.09,-3,-6.07,0.94,-3.08,-6.15,1.04,-2.92,-6.11,1.41,-3,-5.04,1.31,-3.08,-4.94,1.26,-3.4,-5.17,0.9,-3.16,-4.74,1.26,-3.28,-4.86,1.16,-3,-4.91,0.71,-3.04,-4.58,0.78,-3.2,-4.68,0.9,-3.16,-4.74,-0.15,-3.28,-4.57,-0.45,-3.28,-4.73,-0.4,-3.48,-4.76,-0.33,-3.08,-4.55,-0.45,-3.28,-4.73,-0.15,-3.28,-4.57,-0.15,-3.16,-6.23,-0.23,-3.16,-6.18,-0.28,-3.08,-6.18,0.77,-3.76,-6.4,1.16,-4.12,-5.87,1.03,-4.2,-6.29,0.94,-3.08,-6.15,0.8,-3.16,-6.34,0.86,-2.88,-6.24,0.9,-3.16,-4.74,0.89,-3.36,-4.63,1.04,-3.44,-4.7,0.67,-3.12,-4.61,0.65,-3.24,-4.59,0.78,-3.2,-4.68,-0.45,-3.28,-4.73,-0.53,-3.24,-4.85,-0.53,-3.28,-4.85,-0.64,-3.16,-5.03,-0.55,-3.24,-4.88,-0.55,-3.16,-4.84,-0.68,-3.6,-5.34,-0.55,-3.32,-4.91,-0.64,-3.16,-5.03,-0.54,-3.36,-5.92,-0.69,-3.4,-5.63,-0.66,-2.96,-5.79,1.16,-4.12,-5.87,1.1,-4.28,-6.12,1.03,-4.2,-6.29,1.27,-3.32,-5.28,1.39,-3.56,-5.3,1.43,-3.36,-5.69,1.31,-3.08,-4.94,1.22,-3.36,-5,1.26,-3.4,-5.17,0.58,-3.16,-4.57,0.59,-3.24,-4.56,0.65,-3.24,-4.59,-0.55,-3.24,-4.88,-0.53,-3.24,-4.85,-0.55,-3.16,-4.84,-0.53,-3.24,-4.85,-0.55,-3.24,-4.88,-0.53,-3.28,-4.85,-0.64,-3.16,-5.03,-0.74,-2.96,-5.47,-0.68,-3.6,-5.34,-0.4,-3.08,-6.09,-0.28,-3.08,-6.18,-0.23,-3.16,-6.18,-0.23,-3.16,-6.18,-0.15,-3.16,-6.23,-0.14,-3.4,-6.25,0.22,-3.52,-6.39,-0.15,-3.16,-6.23,0.06,-2.8,-6.36,1.26,-3.28,-4.86,1.31,-3.08,-4.94,1.16,-3,-4.91,0.68,-3.36,-4.56,0.68,-3.4,-4.57,0.75,-3.4,-4.59,-0.15,-3.28,-4.57,-0.2,-3.56,-4.64,-0.03,-3.44,-4.58,-0.53,-3.28,-4.85,-0.55,-3.24,-4.88,-0.55,-3.32,-4.91,-0.55,-3.32,-4.91,-0.55,-3.24,-4.88,-0.64,-3.16,-5.03,-0.14,-3.4,-6.25,-0.15,-3.16,-6.23,0.22,-3.52,-6.39,0.89,-3.36,-4.63,0.78,-3.2,-4.68,0.75,-3.4,-4.59,0.65,-3.32,-4.55,0.67,-3.28,-4.57,0.65,-3.24,-4.59,0.61,-3.32,-4.54,0.65,-3.32,-4.55,0.65,-3.24,-4.59,-0.4,-3.48,-4.76,-0.53,-3.28,-4.85,-0.55,-3.32,-4.91,1.38,-3.4,-5.83,1.35,-3,-5.92,1.41,-3.24,-5.71,1.31,-3.08,-4.94,1.26,-3.28,-4.86,1.22,-3.36,-5,1.27,-3.32,-5.28,1.28,-3.04,-5.4,1.34,-3,-5.19,1.24,-3.44,-4.84,1.18,-3.44,-4.77,1.11,-3.6,-4.79,0.89,-3.36,-4.63,0.81,-3.44,-4.61,0.84,-3.48,-4.62,0.65,-3.24,-4.59,0.67,-3.28,-4.57,0.78,-3.2,-4.68,0.78,-3.2,-4.68,0.67,-3.28,-4.57,0.75,-3.4,-4.59,0.64,-3.36,-4.55,0.68,-3.36,-4.56,0.65,-3.32,-4.55,-0.54,-3.36,-5.92,-0.66,-2.96,-5.79,-0.4,-3.08,-6.09,-0.14,-3.4,-6.25,-0.54,-3.36,-5.92,-0.23,-3.16,-6.18,1.27,-3.32,-5.28,1.43,-3.36,-5.69,1.41,-3.24,-5.71,1.21,-3.4,-4.86,1.22,-3.4,-4.9,1.26,-3.28,-4.86,1.16,-3.4,-4.75,1.18,-3.44,-4.77,1.21,-3.4,-4.86,1.22,-3.4,-4.9,1.22,-3.36,-5,1.26,-3.28,-4.86,1.16,-3.4,-4.75,1.04,-3.44,-4.7,1.18,-3.44,-4.77,0.67,-3.28,-4.57,0.68,-3.36,-4.56,0.75,-3.4,-4.59,-0.06,-3.68,-4.63,-0.2,-3.56,-4.64,-0.17,-4.04,-4.77,-0.4,-3.48,-4.76,-0.45,-3.28,-4.73,-0.53,-3.28,-4.85,1.19,-3.36,-5.92,1.38,-3.4,-5.83,1.13,-3.64,-5.92,1.18,-3.44,-4.77,1.24,-3.44,-4.84,1.21,-3.4,-4.86,1.16,-3.4,-4.75,1.26,-3.28,-4.86,0.9,-3.16,-4.74,0.81,-3.44,-4.61,0.75,-3.4,-4.59,0.74,-3.44,-4.59,-0.03,-3.44,-4.58,-0.2,-3.56,-4.64,-0.06,-3.68,-4.63,-0.15,-3.28,-4.57,-0.4,-3.48,-4.76,-0.2,-3.56,-4.64,-0.4,-3.48,-4.76,-0.47,-4,-5.04,-0.17,-4.04,-4.77,-0.64,-3.16,-5.03,-0.68,-2.84,-5.04,-0.74,-2.96,-5.47,-0.69,-3.4,-5.63,-0.54,-3.36,-5.92,-0.66,-3.68,-5.64,-0.41,-4,-6.05,0.44,-3.76,-6.4,0.43,-4.08,-6.37,1.42,-3.56,-5.75,1.38,-3.4,-5.83,1.43,-3.36,-5.69,1.41,-3.24,-5.71,1.43,-3.36,-5.69,1.38,-3.4,-5.83,1.39,-3.56,-5.3,1.47,-3.72,-5.57,1.43,-3.36,-5.69,1.27,-3.32,-5.28,1.34,-3.04,-5.66,1.28,-3.04,-5.4,1.24,-3.44,-4.84,1.22,-3.4,-4.9,1.21,-3.4,-4.86,0.8,-3.48,-4.62,0.84,-3.48,-4.62,0.81,-3.44,-4.61,1.22,-3.36,-5,1.31,-3.56,-4.98,1.26,-3.4,-5.17,-0.03,-3.44,-4.58,-0.06,-3.68,-4.63,0.01,-3.68,-4.61,-0.68,-3.6,-5.34,-0.66,-4,-5.56,-0.56,-3.8,-5.12,0.75,-3.56,-6.4,0.94,-3.08,-6.15,1.19,-3.36,-5.92,1.26,-3.4,-5.17,1.39,-3.56,-5.3,1.27,-3.32,-5.28,1.28,-3.56,-4.92,1.24,-3.44,-4.84,1.11,-3.6,-4.79,1.22,-3.4,-4.9,1.24,-3.44,-4.84,1.28,-3.56,-4.92,1.22,-3.36,-5,1.28,-3.56,-4.92,1.31,-3.56,-4.98,1.31,-3.56,-4.98,1.39,-3.56,-5.3,1.26,-3.4,-5.17,1.16,-3.4,-4.75,1.21,-3.4,-4.86,1.26,-3.28,-4.86,0.84,-3.48,-4.62,0.84,-3.56,-4.63,1.04,-3.44,-4.7,-0.02,-3.88,-4.66,-0.06,-3.68,-4.63,-0.17,-4.04,-4.77,-0.54,-3.36,-5.92,-0.51,-3.68,-5.95,-0.66,-3.68,-5.64,-0.65,-4.16,-5.58,-0.61,-4.6,-5.71,-0.55,-4.72,-5.42,0.44,-3.76,-6.4,0.22,-3.52,-6.39,0.75,-3.56,-6.4,0.75,-3.56,-6.4,0.8,-3.16,-6.34,0.94,-3.08,-6.15,1.19,-3.84,-5.85,1.47,-4,-5.46,1.16,-4.12,-5.87,1.18,-3.44,-4.77,1.04,-3.44,-4.7,1.11,-3.6,-4.79,0.52,-3.56,-4.7,0.44,-3.56,-4.69,0.44,-3.64,-4.69,-0.42,-4.4,-5.11,-0.65,-4.16,-5.58,-0.55,-4.72,-5.42,-0.65,-4.16,-5.58,-0.41,-4,-6.05,-0.34,-4.32,-6.11,0.77,-3.76,-6.4,1.03,-4.2,-6.29,0.78,-4.12,-6.38,0.77,-3.76,-6.4,1.13,-3.64,-5.92,1.19,-3.84,-5.85,1.25,-3.64,-4.91,1.28,-3.56,-4.92,1.11,-3.6,-4.79,0.81,-3.6,-4.65,0.84,-3.64,-4.67,0.84,-3.56,-4.63,0.44,-3.64,-4.69,0.6,-3.76,-4.71,0.64,-3.64,-4.68,0.52,-3.56,-4.7,0.44,-3.64,-4.69,0.64,-3.64,-4.68,-0.68,-3.6,-5.34,-0.56,-3.8,-5.12,-0.55,-3.32,-4.91,1.47,-3.72,-5.57,1.42,-3.56,-5.75,1.43,-3.36,-5.69,1.31,-3.56,-4.98,1.25,-3.64,-4.91,1.29,-3.84,-5.11,1.22,-3.36,-5,1.22,-3.4,-4.9,1.28,-3.56,-4.92,0.95,-3.8,-4.73,0.95,-3.96,-4.77,1.09,-4,-4.81,0.81,-3.6,-4.65,0.82,-3.64,-4.65,0.84,-3.64,-4.67,0.64,-3.64,-4.68,0.69,-3.8,-4.71,0.79,-3.76,-4.7,0.03,-3.72,-4.62,0.06,-3.72,-4.61,0.01,-3.68,-4.61,0.03,-3.72,-4.62,-0.06,-3.68,-4.63,-0.02,-3.88,-4.66,-0.68,-3.6,-5.34,-0.66,-3.68,-5.64,-0.66,-4,-5.56,-0.41,-4,-6.05,-0.14,-3.4,-6.25,0.22,-3.52,-6.39,1.27,-3.32,-5.28,1.41,-3.24,-5.71,1.34,-3.04,-5.66,1.31,-3.56,-4.98,1.28,-3.56,-4.92,1.25,-3.64,-4.91,0.83,-3.72,-4.68,0.85,-3.72,-4.69,0.84,-3.64,-4.67,0.03,-3.72,-4.62,0.07,-3.8,-4.61,0.06,-3.72,-4.61,0.84,-3.56,-4.63,0.84,-3.64,-4.67,1.11,-3.6,-4.79,0.48,-3.8,-4.74,0.44,-3.64,-4.69,0.35,-3.72,-4.69,0.45,-3.88,-4.72,0.48,-3.8,-4.74,0.35,-3.72,-4.69,1.25,-3.64,-4.91,1.2,-3.76,-4.87,1.29,-3.84,-5.11,1.2,-3.76,-4.87,0.95,-3.8,-4.73,1.09,-4,-4.81,0.64,-3.64,-4.68,0.6,-3.76,-4.71,0.69,-3.8,-4.71,0.12,-3.84,-4.61,0.07,-3.8,-4.61,-0.02,-3.88,-4.66,-0.56,-3.8,-5.12,-0.4,-3.48,-4.76,-0.55,-3.32,-4.91,1.38,-3.4,-5.83,1.42,-3.56,-5.75,1.13,-3.64,-5.92,1.19,-3.84,-5.85,1.42,-3.56,-5.75,1.47,-3.72,-5.57,1.29,-3.84,-5.11,1.26,-4.08,-5.02,1.36,-4.12,-5.21,1.2,-3.76,-4.87,1.22,-3.88,-4.98,1.29,-3.84,-5.11,1.22,-3.88,-4.98,1.2,-3.76,-4.87,1.09,-4,-4.81,0.84,-3.64,-4.67,0.85,-3.72,-4.69,1.11,-3.6,-4.79,0.84,-3.76,-4.7,0.81,-3.88,-4.73,0.95,-3.8,-4.73,0.85,-3.72,-4.69,0.84,-3.76,-4.7,0.95,-3.8,-4.73,0.16,-4.08,-4.64,0.12,-3.84,-4.61,-0.02,-3.88,-4.66,-0.51,-3.68,-5.95,-0.66,-4,-5.56,-0.66,-3.68,-5.64,1.47,-3.72,-5.57,1.29,-3.84,-5.11,1.47,-4,-5.46,1.2,-3.76,-4.87,1.25,-3.64,-4.91,1.11,-3.6,-4.79,0.88,-3.92,-4.75,0.81,-3.88,-4.73,0.81,-3.92,-4.73,0.68,-3.88,-4.72,0.81,-3.88,-4.73,0.69,-3.8,-4.71,0.84,-3.76,-4.7,0.79,-3.76,-4.7,0.81,-3.88,-4.73,0.55,-3.88,-4.75,0.45,-3.88,-4.72,0.56,-3.96,-4.74,0.54,-3.84,-4.76,0.48,-3.8,-4.74,0.45,-3.88,-4.72,0.55,-3.88,-4.75,0.54,-3.84,-4.76,0.45,-3.88,-4.72,1.19,-3.84,-5.85,1.47,-3.72,-5.57,1.47,-4,-5.46,1.26,-4.2,-5.02,1.43,-4.36,-5.3,1.36,-4.12,-5.21,0.81,-3.88,-4.73,0.88,-3.92,-4.75,0.95,-3.8,-4.73,0.55,-3.88,-4.75,0.56,-3.96,-4.74,0.67,-3.96,-4.77,0.32,-3.92,-4.67,0.39,-4,-4.69,0.45,-3.88,-4.72,-0.2,-3.56,-4.64,-0.4,-3.48,-4.76,-0.17,-4.04,-4.77,-0.14,-3.4,-6.25,-0.51,-3.68,-5.95,-0.54,-3.36,-5.92,0.77,-3.76,-6.4,0.44,-3.76,-6.4,0.75,-3.56,-6.4,0.75,-3.56,-6.4,1.19,-3.36,-5.92,1.13,-3.64,-5.92,1.19,-3.84,-5.85,1.13,-3.64,-5.92,1.42,-3.56,-5.75,1.29,-3.84,-5.11,1.36,-4.12,-5.21,1.47,-4,-5.46,0.95,-3.96,-4.77,0.88,-3.92,-4.75,0.88,-3.96,-4.75,0.56,-3.96,-4.74,0.39,-4.2,-4.69,0.51,-4.28,-4.71,0.32,-3.92,-4.67,0.32,-4,-4.67,0.39,-4,-4.69,-0.41,-4,-6.05,0.43,-4.08,-6.37,-0.09,-4.4,-6.22,0.77,-3.76,-6.4,0.78,-4.12,-6.38,0.44,-3.76,-6.4,1.29,-3.84,-5.11,1.39,-3.56,-5.3,1.31,-3.56,-4.98,1.15,-4.08,-4.87,1.21,-4.08,-4.94,1.22,-3.88,-4.98,1.29,-3.84,-5.11,1.22,-3.88,-4.98,1.26,-4.08,-5.02,0.56,-3.96,-4.74,0.51,-4.28,-4.71,0.67,-3.96,-4.77,0.32,-4,-4.67,0.32,-4.04,-4.67,0.39,-4,-4.69,0.28,-4,-4.67,0.32,-4,-4.67,0.32,-3.92,-4.67,-0.17,-4.04,-4.77,0.16,-4.08,-4.64,-0.02,-3.88,-4.66,-0.17,-4.04,-4.77,-0.42,-4.4,-5.11,-0.13,-4.6,-4.91,-0.61,-4.6,-5.71,-0.65,-4.16,-5.58,-0.34,-4.32,-6.11,-0.47,-4,-5.04,-0.66,-4,-5.56,-0.65,-4.16,-5.58,0.78,-4.12,-6.38,0.43,-4.08,-6.37,0.44,-3.76,-6.4,0.77,-3.76,-6.4,0.75,-3.56,-6.4,1.13,-3.64,-5.92,1.2,-3.76,-4.87,1.11,-3.6,-4.79,0.95,-3.8,-4.73,0.95,-3.96,-4.77,0.95,-3.8,-4.73,0.88,-3.92,-4.75,0.51,-4.28,-4.71,1.01,-4.28,-4.83,0.9,-4.04,-4.81,0.56,-3.96,-4.74,0.35,-4.12,-4.68,0.39,-4.2,-4.69,0.78,-4.12,-6.38,1.03,-4.2,-6.29,1.02,-4.28,-6.32,1.47,-4,-5.46,1.45,-4.32,-5.45,1.16,-4.12,-5.87,1.47,-3.72,-5.57,1.39,-3.56,-5.3,1.29,-3.84,-5.11,1.15,-4.08,-4.87,1.16,-4.16,-4.9,1.19,-4.12,-4.92,0.39,-4,-4.69,0.56,-3.96,-4.74,0.45,-3.88,-4.72,0.16,-4.08,-4.64,0.11,-4.24,-4.72,0.23,-4.2,-4.65,0.16,-4.08,-4.64,0.23,-4.2,-4.65,0.28,-4.16,-4.67,0.77,-3.76,-6.4,1.19,-3.84,-5.85,1.16,-4.12,-5.87,1.43,-4.36,-5.3,1.45,-4.32,-5.45,1.36,-4.12,-5.21,1.21,-4.12,-4.94,1.26,-4.2,-5.02,1.26,-4.08,-5.02,1.22,-3.88,-4.98,1.21,-4.08,-4.94,1.26,-4.08,-5.02,1.16,-4.16,-4.9,1.19,-4.16,-4.92,1.19,-4.12,-4.92,1.19,-4.12,-4.92,1.21,-4.12,-4.94,1.21,-4.08,-4.94,0.39,-4.2,-4.69,0.35,-4.12,-4.68,0.32,-4.16,-4.67,0.32,-4.16,-4.67,0.35,-4.12,-4.68,0.32,-4.04,-4.67,0.32,-3.92,-4.67,0.45,-3.88,-4.72,0.35,-3.72,-4.69,0.32,-4.04,-4.67,0.35,-4.12,-4.68,0.39,-4,-4.69,-0.17,-4.04,-4.77,0.11,-4.24,-4.72,0.16,-4.08,-4.64,-0.69,-3.4,-5.63,-0.66,-3.68,-5.64,-0.68,-3.6,-5.34,-0.41,-4,-6.05,0.22,-3.52,-6.39,0.44,-3.76,-6.4,1.16,-4.28,-5.9,1.16,-4.12,-5.87,1.45,-4.32,-5.45,1.26,-4.08,-5.02,1.26,-4.2,-5.02,1.36,-4.12,-5.21,1.21,-4.08,-4.94,1.21,-4.12,-4.94,1.26,-4.08,-5.02,1.21,-4.12,-4.94,1.19,-4.12,-4.92,1.19,-4.16,-4.92,1.15,-4.08,-4.87,1.19,-4.12,-4.92,1.21,-4.08,-4.94,1.09,-4,-4.81,1.15,-4.08,-4.87,1.22,-3.88,-4.98,1.19,-4.16,-4.92,1.16,-4.16,-4.9,1.18,-4.24,-4.93,1.01,-4.28,-4.83,1.18,-4.24,-4.93,1.16,-4.16,-4.9,1.01,-4.28,-4.83,1.16,-4.16,-4.9,1.15,-4.08,-4.87,1.01,-4.28,-4.83,1.09,-4,-4.81,0.9,-4.04,-4.81,0.28,-4.16,-4.67,0.32,-4.16,-4.67,0.32,-4.04,-4.67,0.32,-4.16,-4.67,0.28,-4.16,-4.67,0.23,-4.2,-4.65,0.11,-4.24,-4.72,-0.17,-4.04,-4.77,-0.13,-4.6,-4.91,1.01,-4.28,-4.83,0.73,-4.6,-4.8,0.87,-4.72,-4.84,0.39,-4.2,-4.69,0.32,-4.16,-4.67,0.31,-4.2,-4.68,-0.34,-4.32,-6.11,-0.41,-4,-6.05,-0.09,-4.4,-6.22,1.26,-4.2,-5.02,1.21,-4.12,-4.94,1.19,-4.16,-4.92,1.18,-4.24,-4.93,1.26,-4.2,-5.02,1.19,-4.16,-4.92,0.56,-3.96,-4.74,0.39,-4,-4.69,0.35,-4.12,-4.68,0.3,-4.32,-4.66,0.23,-4.2,-4.65,0.11,-4.24,-4.72,-0.42,-4.4,-5.11,-0.47,-4,-5.04,-0.65,-4.16,-5.58,1.1,-4.28,-6.12,1.12,-4.6,-6.28,1.07,-4.48,-6.31,1.41,-4.52,-5.53,1.45,-4.32,-5.45,1.43,-4.36,-5.3,1.01,-4.28,-4.83,1.15,-4.08,-4.87,1.09,-4,-4.81,1.16,-4.48,-4.98,1.18,-4.24,-4.93,1.01,-4.28,-4.83,0.57,-4.48,-4.73,0.73,-4.6,-4.8,1.01,-4.28,-4.83,0.39,-4.28,-4.69,0.39,-4.2,-4.69,0.35,-4.24,-4.69,0.35,-4.24,-4.69,0.39,-4.2,-4.69,0.31,-4.2,-4.68,0.3,-4.32,-4.66,0.39,-4.28,-4.69,0.35,-4.24,-4.69,0.3,-4.32,-4.66,0.35,-4.24,-4.69,0.23,-4.2,-4.65,-0.4,-3.48,-4.76,-0.56,-3.8,-5.12,-0.47,-4,-5.04,-0.09,-4.4,-6.22,0.4,-4.84,-6.27,0.25,-4.96,-6.24,1.26,-4.2,-5.02,1.18,-4.24,-4.93,1.16,-4.48,-4.98,0.38,-4.4,-4.7,0.22,-4.48,-4.76,0.44,-4.52,-4.69,-0.47,-4,-5.04,-0.56,-3.8,-5.12,-0.66,-4,-5.56,-0.41,-4,-6.05,-0.66,-4,-5.56,-0.51,-3.68,-5.95,1.02,-4.28,-6.32,1.03,-4.2,-6.29,1.1,-4.28,-6.12,1.16,-4.12,-5.87,1.16,-4.28,-5.9,1.1,-4.28,-6.12,0.9,-4.04,-4.81,1.09,-4,-4.81,0.95,-3.96,-4.77,0.51,-4.28,-4.71,0.9,-4.04,-4.81,0.67,-3.96,-4.77,0.57,-4.48,-4.73,0.51,-4.28,-4.71,0.38,-4.4,-4.7,1.02,-4.28,-6.32,1.1,-4.28,-6.12,1.07,-4.48,-6.31,1.26,-4.2,-5.02,1.38,-4.6,-5.19,1.43,-4.36,-5.3,0.39,-4.2,-4.69,0.39,-4.28,-4.69,0.51,-4.28,-4.71,0.22,-4.48,-4.76,0.38,-4.64,-4.75,0.44,-4.52,-4.69,0.22,-4.48,-4.76,0.3,-4.32,-4.66,0.11,-4.24,-4.72,-0.52,-4.72,-5.92,-0.61,-4.6,-5.71,-0.34,-4.32,-6.11,0.44,-4.52,-4.69,0.57,-4.48,-4.73,0.38,-4.4,-4.7,0.38,-4.4,-4.7,0.51,-4.28,-4.71,0.39,-4.28,-4.69,-0.42,-4.4,-5.11,-0.24,-4.8,-5.05,-0.13,-4.6,-4.91,0.38,-4.64,-4.75,0.48,-4.64,-4.72,0.44,-4.52,-4.69,0.1,-5.2,-4.96,-0.13,-4.6,-4.91,-0.24,-4.8,-5.05,0.38,-4.4,-4.7,0.3,-4.32,-4.66,0.22,-4.48,-4.76,1.45,-4.32,-5.45,1.47,-4,-5.46,1.36,-4.12,-5.21,0.22,-4.48,-4.76,0.11,-4.24,-4.72,-0.13,-4.6,-4.91,0.4,-4.84,-6.27,-0.09,-4.4,-6.22,0.43,-4.08,-6.37,1.07,-4.48,-6.31,0.85,-4.56,-6.37,1.02,-4.28,-6.32,1.07,-4.48,-6.31,1.12,-4.6,-6.28,0.85,-4.56,-6.37,1.28,-4.8,-5.73,1.29,-4.96,-6.03,1.24,-4.72,-6.1,1.38,-4.6,-5.19,1.26,-4.2,-5.02,1.16,-4.48,-4.98,1.21,-4.76,-5.02,1.38,-4.6,-5.19,1.16,-4.48,-4.98,0.48,-4.64,-4.72,0.57,-4.6,-4.74,0.44,-4.52,-4.69,-0.42,-4.4,-5.11,-0.17,-4.04,-4.77,-0.47,-4,-5.04,-0.41,-4,-6.05,-0.65,-4.16,-5.58,-0.66,-4,-5.56,0.73,-4.6,-4.8,0.6,-4.6,-4.75,0.6,-4.64,-4.75,0.57,-4.6,-4.74,0.6,-4.6,-4.75,0.57,-4.48,-4.73,0.57,-4.48,-4.73,0.6,-4.6,-4.75,0.73,-4.6,-4.8,0.38,-4.64,-4.75,0.22,-4.48,-4.76,-0.13,-4.6,-4.91,0.57,-4.6,-4.74,0.57,-4.48,-4.73,0.44,-4.52,-4.69,-0.42,-4.4,-5.11,-0.55,-4.72,-5.42,-0.24,-4.8,-5.05,-0.61,-4.6,-5.71,-0.61,-4.76,-5.64,-0.55,-4.72,-5.42,-0.59,-4.96,-5.62,-0.52,-4.72,-5.92,-0.43,-5.08,-6.03,0.85,-4.56,-6.37,0.78,-4.12,-6.38,1.02,-4.28,-6.32,1.38,-4.6,-5.19,1.21,-4.76,-5.02,1.42,-4.8,-5.28,0.51,-4.28,-4.71,0.57,-4.48,-4.73,1.01,-4.28,-4.83,0.6,-4.6,-4.75,0.57,-4.6,-4.74,0.6,-4.64,-4.75,0.56,-4.64,-4.74,0.6,-4.64,-4.75,0.57,-4.6,-4.74,-0.2,-4.96,-6.15,-0.09,-4.4,-6.22,0.25,-4.96,-6.24,0.59,-5.2,-6.23,0.67,-4.96,-6.32,0.94,-5.2,-6.33,0.85,-4.56,-6.37,1.12,-4.6,-6.28,1.17,-4.96,-6.27,1.24,-4.72,-6.1,1.29,-4.96,-6.03,1.17,-4.96,-6.27,0.71,-4.68,-4.78,0.73,-4.6,-4.8,0.6,-4.64,-4.75,0.48,-4.64,-4.72,0.53,-4.76,-4.75,0.6,-4.68,-4.75,-0.2,-4.96,-6.15,-0.43,-5.08,-6.03,-0.52,-4.72,-5.92,0.43,-4.08,-6.37,0.78,-4.12,-6.38,0.85,-4.56,-6.37,0.67,-4.96,-6.32,0.63,-4.76,-6.36,1.17,-4.96,-6.27,1.1,-4.28,-6.12,1.24,-4.72,-6.1,1.12,-4.6,-6.28,1.41,-4.52,-5.53,1.16,-4.28,-5.9,1.45,-4.32,-5.45,0.83,-4.92,-4.83,0.98,-5.16,-4.9,1.21,-4.76,-5.02,0.73,-4.6,-4.8,0.71,-4.68,-4.78,0.87,-4.72,-4.84,0.6,-4.64,-4.75,0.6,-4.68,-4.75,0.71,-4.68,-4.78,0.48,-4.64,-4.72,0.38,-4.64,-4.75,0.53,-4.76,-4.75,0.43,-4.08,-6.37,0.85,-4.56,-6.37,0.63,-4.76,-6.36,0.4,-4.84,-6.27,0.63,-4.76,-6.36,0.59,-4.88,-6.31,1.43,-4.36,-5.3,1.38,-4.6,-5.19,1.41,-4.52,-5.53,1.38,-4.6,-5.19,1.42,-4.68,-5.46,1.41,-4.52,-5.53,0.71,-4.68,-4.78,0.71,-4.96,-4.77,0.83,-4.92,-4.83,-0.55,-4.72,-5.42,-0.61,-4.76,-5.64,-0.59,-4.96,-5.62,0.4,-4.84,-6.27,0.43,-4.08,-6.37,0.63,-4.76,-6.36,1.12,-4.6,-6.28,1.24,-4.72,-6.1,1.17,-4.96,-6.27,1.38,-4.6,-5.19,1.42,-4.8,-5.28,1.42,-4.68,-5.46,0.87,-4.72,-4.84,1.21,-4.76,-5.02,1.16,-4.48,-4.98,-0.2,-4.96,-6.15,-0.52,-4.72,-5.92,-0.34,-4.32,-6.11,1.41,-4.52,-5.53,1.42,-4.68,-5.46,1.28,-4.8,-5.73,1.42,-4.8,-5.28,1.32,-4.88,-5.62,1.42,-4.68,-5.46,1.42,-5.24,-5.39,1.34,-5.12,-5.19,1.24,-5.56,-5.12,0.53,-4.76,-4.75,0.71,-4.96,-4.77,0.6,-4.68,-4.75,0.53,-4.76,-4.75,0.42,-5.08,-4.93,0.71,-4.96,-4.77,0.41,-5.2,-4.96,0.42,-5.08,-4.93,0.1,-5.2,-4.96,-0.59,-4.96,-5.62,-0.61,-4.76,-5.64,-0.52,-4.72,-5.92,-0.52,-4.72,-5.92,-0.61,-4.76,-5.64,-0.61,-4.6,-5.71,0.43,-4.92,-6.33,0.4,-4.92,-6.32,0.4,-4.84,-6.27,0.43,-4.92,-6.33,0.4,-4.84,-6.27,0.59,-4.88,-6.31,0.63,-4.76,-6.36,0.85,-4.56,-6.37,1.17,-4.96,-6.27,1.29,-4.96,-6.03,1.28,-4.8,-5.73,1.43,-5.16,-5.73,1.42,-4.8,-5.28,1.42,-5,-5.31,1.32,-4.88,-5.62,-0.09,-4.4,-6.22,-0.2,-4.96,-6.15,-0.34,-4.32,-6.11,0.25,-4.96,-6.24,0.4,-4.84,-6.27,0.4,-4.92,-6.32,1.28,-4.8,-5.73,1.32,-4.88,-5.62,1.43,-5.16,-5.73,0.87,-4.72,-4.84,1.16,-4.48,-4.98,1.01,-4.28,-4.83,0.87,-4.72,-4.84,0.71,-4.68,-4.78,0.83,-4.92,-4.83,0.81,-5.16,-4.84,0.75,-5.12,-4.83,0.61,-5.32,-4.96,0.42,-5.08,-4.93,0.38,-4.64,-4.75,-0.13,-4.6,-4.91,0.1,-5.2,-4.96,0.42,-5.08,-4.93,-0.13,-4.6,-4.91,0.43,-4.92,-6.33,0.45,-4.96,-6.32,0.4,-4.92,-6.32,0.59,-4.88,-6.31,0.45,-4.96,-6.32,0.43,-4.92,-6.33,1.17,-4.96,-6.27,1.29,-4.96,-6.03,1.29,-5.16,-6.18,0.83,-4.92,-4.83,0.71,-4.96,-4.77,0.75,-5.12,-4.83,0.42,-5.08,-4.93,0.53,-4.76,-4.75,0.38,-4.64,-4.75,-0.4,-5.4,-6.04,-0.06,-5.32,-6.19,-0.03,-5.48,-6.16,0.29,-5.04,-6.29,0.25,-4.96,-6.24,0.4,-4.92,-6.32,0.29,-5.04,-6.29,0.45,-4.96,-6.32,0.59,-5.2,-6.23,0.29,-5.04,-6.29,0.4,-4.92,-6.32,0.45,-4.96,-6.32,0.94,-5.2,-6.33,1.17,-4.96,-6.27,1.29,-5.16,-6.18,1.42,-4.68,-5.46,1.32,-4.88,-5.62,1.28,-4.8,-5.73,1.42,-5.08,-5.39,1.43,-5.16,-5.73,1.32,-4.88,-5.62,1.34,-5.12,-5.19,1.42,-5,-5.31,1.21,-4.76,-5.02,-0.57,-5.2,-5.66,-0.59,-4.96,-5.62,-0.43,-5.08,-6.03,0.07,-5.12,-6.2,0.25,-4.96,-6.24,0.29,-5.04,-6.29,0.67,-4.96,-6.32,1.17,-4.96,-6.27,0.94,-5.2,-6.33,1.28,-4.8,-5.73,1.24,-4.72,-6.1,1.16,-4.28,-5.9,1.1,-4.28,-6.12,1.16,-4.28,-5.9,1.24,-4.72,-6.1,1.29,-4.96,-6.03,1.44,-5.24,-5.88,1.29,-5.16,-6.18,0.83,-4.92,-4.83,0.75,-5.12,-4.83,0.81,-5.16,-4.84,0.41,-5.2,-4.96,0.1,-5.2,-4.96,0.3,-5.44,-4.96,0.1,-5.2,-4.96,-0.24,-4.8,-5.05,-0.2,-5.32,-5.19,-0.57,-5.2,-5.66,-0.51,-5.4,-5.91,-0.51,-5.32,-5.53,0.07,-5.12,-6.2,-0.2,-4.96,-6.15,0.25,-4.96,-6.24,0.45,-4.96,-6.32,0.59,-4.88,-6.31,0.67,-4.96,-6.32,0.67,-4.96,-6.32,0.59,-4.88,-6.31,0.63,-4.76,-6.36,1.17,-5.68,-6.27,1.29,-5.16,-6.18,1.48,-5.44,-5.94,1.41,-4.52,-5.53,1.28,-4.8,-5.73,1.16,-4.28,-5.9,1.34,-5.12,-5.19,1.42,-5.08,-5.39,1.42,-5,-5.31,0.42,-5.08,-4.93,0.75,-5.12,-4.83,0.71,-4.96,-4.77,0.71,-4.96,-4.77,0.71,-4.68,-4.78,0.6,-4.68,-4.75,0.3,-5.44,-4.96,0.1,-5.2,-4.96,-0.2,-5.32,-5.19,0.07,-5.12,-6.2,0.29,-5.04,-6.29,0.36,-5.36,-6.15,1.45,-5.56,-5.69,1.48,-5.44,-5.94,1.44,-5.24,-5.88,0.98,-5.16,-4.9,1.34,-5.12,-5.19,1.21,-4.76,-5.02,0.3,-5.44,-4.96,-0.2,-5.32,-5.19,-0.09,-5.88,-5.3,-0.57,-5.2,-5.66,-0.43,-5.08,-6.03,-0.51,-5.4,-5.91,-0.43,-5.08,-6.03,-0.2,-4.96,-6.15,-0.06,-5.32,-6.19,-0.06,-5.32,-6.19,0.36,-5.36,-6.15,-0.03,-5.48,-6.16,1.42,-5,-5.31,1.42,-4.8,-5.28,1.21,-4.76,-5.02,1.42,-5,-5.31,1.42,-5.08,-5.39,1.32,-4.88,-5.62,0.86,-5.28,-4.88,1.04,-5.56,-4.96,1.12,-5.48,-4.98,-0.59,-4.96,-5.62,-0.51,-5.32,-5.53,-0.2,-5.32,-5.19,-0.22,-5.64,-6.09,-0.03,-5.48,-6.16,0.05,-5.64,-6.06,0.5,-5.52,-6.23,0.94,-5.32,-6.33,0.82,-5.72,-6.39,0.83,-4.92,-4.83,1.21,-4.76,-5.02,0.87,-4.72,-4.84,0.98,-5.16,-4.9,0.83,-4.92,-4.83,0.81,-5.16,-4.84,0.86,-5.28,-4.88,0.98,-5.16,-4.9,0.81,-5.16,-4.84,1.43,-5.16,-5.73,1.42,-5.08,-5.39,1.42,-5.24,-5.39,1.42,-5.08,-5.39,1.34,-5.12,-5.19,1.42,-5.24,-5.39,1.42,-5.24,-5.39,1.45,-5.56,-5.69,1.43,-5.16,-5.73,0.86,-5.28,-4.88,0.81,-5.16,-4.84,0.61,-5.32,-4.96,0.42,-5.08,-4.93,0.41,-5.2,-4.96,0.75,-5.12,-4.83,0.07,-5.12,-6.2,-0.06,-5.32,-6.19,-0.2,-4.96,-6.15,-0.43,-5.08,-6.03,-0.06,-5.32,-6.19,-0.4,-5.4,-6.04,0.59,-5.2,-6.23,0.5,-5.52,-6.23,0.36,-5.36,-6.15,0.94,-5.32,-6.33,0.94,-5.2,-6.33,1.29,-5.16,-6.18,1.45,-5.56,-5.69,1.44,-5.24,-5.88,1.43,-5.16,-5.73,0.98,-5.16,-4.9,1.12,-5.48,-4.98,1.34,-5.12,-5.19,0.75,-5.12,-4.83,0.41,-5.2,-4.96,0.61,-5.32,-4.96,0.45,-4.96,-6.32,0.67,-4.96,-6.32,0.59,-5.2,-6.23,0.59,-5.2,-6.23,0.94,-5.2,-6.33,0.94,-5.32,-6.33,1.17,-5.68,-6.27,0.94,-5.32,-6.33,1.29,-5.16,-6.18,1.44,-5.24,-5.88,1.29,-4.96,-6.03,1.43,-5.16,-5.73,1.42,-5.24,-5.39,1.3,-5.68,-5.22,1.45,-5.56,-5.69,-0.51,-5.32,-5.53,-0.51,-5.6,-5.63,-0.2,-5.32,-5.19,0.36,-5.36,-6.15,0.29,-5.04,-6.29,0.59,-5.2,-6.23,0.59,-5.2,-6.23,0.94,-5.32,-6.33,0.5,-5.52,-6.23,0.86,-5.28,-4.88,0.62,-5.6,-5.04,1.04,-5.56,-4.96,0.86,-5.28,-4.88,1.12,-5.48,-4.98,0.98,-5.16,-4.9,0.41,-5.2,-4.96,0.3,-5.44,-4.96,0.61,-5.32,-4.96,-0.43,-5.08,-6.03,-0.4,-5.4,-6.04,-0.51,-5.4,-5.91,0.36,-5.36,-6.15,0.32,-5.6,-6.11,-0.03,-5.48,-6.16,-0.06,-5.32,-6.19,0.07,-5.12,-6.2,0.36,-5.36,-6.15,1.44,-5.24,-5.88,1.48,-5.44,-5.94,1.29,-5.16,-6.18,-0.55,-4.72,-5.42,-0.2,-5.32,-5.19,-0.24,-4.8,-5.05,-0.55,-4.72,-5.42,-0.59,-4.96,-5.62,-0.2,-5.32,-5.19,-0.51,-5.4,-5.91,-0.51,-5.6,-5.63,-0.51,-5.32,-5.53,1.52,-5.64,-5.89,1.17,-5.68,-6.27,1.48,-5.44,-5.94,1.17,-5.8,-5.09,1.07,-5.72,-5.05,0.89,-6.08,-5.1,0.34,-5.72,-4.98,0.62,-5.6,-5.04,0.3,-5.44,-4.96,0.05,-5.64,-6.06,-0.03,-5.48,-6.16,0.32,-5.6,-6.11,1.34,-5.12,-5.19,1.12,-5.48,-4.98,1.24,-5.56,-5.12,1.24,-5.56,-5.12,1.04,-5.56,-4.96,1.07,-5.72,-5.05,-0.59,-4.96,-5.62,-0.57,-5.2,-5.66,-0.51,-5.32,-5.53,-0.46,-5.6,-5.98,-0.4,-5.4,-6.04,-0.22,-5.64,-6.09,0.82,-5.72,-6.39,0.94,-5.32,-6.33,1.17,-5.68,-6.27,1.48,-5.44,-5.94,1.45,-5.56,-5.69,1.52,-5.64,-5.89,1.07,-5.72,-5.05,1.04,-5.56,-4.96,0.62,-5.6,-5.04,0.34,-5.72,-4.98,0.3,-5.44,-4.96,-0.09,-5.88,-5.3,-0.51,-5.4,-5.91,-0.46,-5.6,-5.98,-0.51,-5.6,-5.63,-0.4,-5.4,-6.04,-0.03,-5.48,-6.16,-0.22,-5.64,-6.09,-0.51,-5.4,-5.91,-0.4,-5.4,-6.04,-0.46,-5.6,-5.98,1.3,-5.68,-5.22,1.26,-5.64,-5.1,1.17,-5.8,-5.09,1.26,-5.64,-5.1,1.07,-5.72,-5.05,1.17,-5.8,-5.09,0.3,-5.44,-4.96,0.62,-5.6,-5.04,0.61,-5.32,-4.96,0.31,-5.76,-6.11,0.32,-5.6,-6.11,0.46,-5.72,-6.19,0.5,-5.52,-6.23,0.32,-5.6,-6.11,0.36,-5.36,-6.15,0.62,-5.6,-5.04,0.34,-5.72,-4.98,0.43,-5.84,-4.98,0.26,-6.04,-5.07,0.34,-5.72,-4.98,-0.09,-5.88,-5.3,-0.51,-5.6,-5.63,-0.33,-5.84,-5.47,-0.2,-5.32,-5.19,1.58,-6.36,-5.9,1.55,-5.92,-5.88,1.54,-6.04,-5.53,1.33,-5.8,-5.16,1.17,-5.8,-5.09,1.22,-5.92,-5.17,1.42,-5.24,-5.39,1.24,-5.56,-5.12,1.3,-5.68,-5.22,0.89,-6.08,-5.1,1.07,-5.72,-5.05,0.43,-5.84,-4.98,0.43,-5.84,-4.98,0.34,-5.72,-4.98,0.26,-6.04,-5.07,-0.42,-5.92,-5.94,-0.42,-5.92,-5.59,-0.51,-5.6,-5.63,0.2,-5.84,-6.09,0.13,-5.84,-6.04,0.05,-5.64,-6.06,0.52,-5.76,-6.25,0.5,-5.52,-6.23,0.82,-5.72,-6.39,1.17,-6.04,-6.27,1.17,-5.68,-6.27,1.55,-5.92,-5.88,1.24,-5.56,-5.12,1.12,-5.48,-4.98,1.04,-5.56,-4.96,-0.42,-5.92,-5.94,-0.52,-6.08,-5.84,-0.49,-6.04,-5.76,0.5,-5.52,-6.23,0.46,-5.72,-6.19,0.32,-5.6,-6.11,1.33,-5.8,-5.16,1.3,-5.68,-5.22,1.17,-5.8,-5.09,-0.42,-5.92,-5.59,-0.2,-6.16,-5.71,-0.06,-6.04,-5.47,-0.22,-5.64,-6.09,-0.42,-5.92,-5.94,-0.46,-5.6,-5.98,0.32,-5.6,-6.11,0.31,-5.76,-6.11,0.05,-5.64,-6.06,0.52,-5.76,-6.25,0.41,-5.84,-6.31,0.46,-5.72,-6.19,0.52,-5.76,-6.25,0.46,-5.72,-6.19,0.5,-5.52,-6.23,1.52,-5.64,-5.89,1.45,-5.56,-5.69,1.55,-5.92,-5.88,0.89,-6.08,-5.1,0.43,-5.84,-4.98,0.81,-6.2,-5.04,0.41,-5.84,-6.31,0.34,-6.12,-6.41,0.21,-5.96,-6.32,0.64,-5.84,-6.38,0.52,-5.76,-6.25,0.82,-5.72,-6.39,0.64,-5.84,-6.38,0.53,-5.84,-6.36,0.52,-5.76,-6.25,1.3,-5.68,-5.22,1.33,-5.8,-5.16,1.4,-5.88,-5.25,0.86,-5.28,-4.88,0.61,-5.32,-4.96,0.62,-5.6,-5.04,-0.33,-5.84,-5.47,-0.09,-5.88,-5.3,-0.2,-5.32,-5.19,-0.33,-5.84,-5.47,-0.42,-5.92,-5.59,-0.06,-6.04,-5.47,-0.51,-5.6,-5.63,-0.42,-5.92,-5.59,-0.33,-5.84,-5.47,-0.22,-5.64,-6.09,-0.05,-5.96,-5.99,-0.17,-5.96,-5.93,0.2,-5.84,-6.09,0.31,-5.76,-6.11,0.21,-5.96,-6.32,0.31,-5.76,-6.11,0.41,-5.84,-6.31,0.21,-5.96,-6.32,0.31,-5.76,-6.11,0.2,-5.84,-6.09,0.05,-5.64,-6.06,0.51,-6.12,-6.41,0.61,-5.96,-6.33,0.71,-6.28,-6.4,0.53,-5.84,-6.36,0.41,-5.84,-6.31,0.52,-5.76,-6.25,0.61,-5.96,-6.33,0.53,-5.84,-6.36,0.64,-5.84,-6.38,0.61,-5.96,-6.33,0.64,-5.84,-6.38,0.92,-6.08,-6.36,1.24,-5.56,-5.12,1.26,-5.64,-5.1,1.3,-5.68,-5.22,1.17,-5.8,-5.09,0.89,-6.08,-5.1,1.22,-5.92,-5.17,-0.46,-5.6,-5.98,-0.42,-5.92,-5.94,-0.51,-5.6,-5.63,0.05,-5.64,-6.06,0.13,-5.84,-6.04,-0.05,-5.96,-5.99,0,-6,-6.14,0.13,-5.84,-6.04,0.2,-5.84,-6.09,0.41,-5.84,-6.31,0.31,-5.76,-6.11,0.46,-5.72,-6.19,0.43,-5.84,-4.98,0.36,-6.12,-5.03,0.81,-6.2,-5.04,-0.09,-5.88,-5.3,-0.33,-5.84,-5.47,-0.06,-6.04,-5.47,-0.37,-6.28,-5.95,-0.46,-6.2,-5.91,-0.42,-6.12,-5.87,-0.42,-6.12,-5.87,-0.42,-5.92,-5.94,-0.17,-5.96,-5.93,-0.22,-5.64,-6.09,0.05,-5.64,-6.06,-0.05,-5.96,-5.99,-0.22,-5.64,-6.09,-0.17,-5.96,-5.93,-0.42,-5.92,-5.94,-0.17,-5.96,-5.93,-0.34,-6.2,-6.11,-0.37,-6.28,-5.95,1.3,-5.68,-5.22,1.4,-5.88,-5.25,1.45,-5.56,-5.69,1.45,-5.56,-5.69,1.54,-6.04,-5.53,1.55,-5.92,-5.88,1.33,-5.8,-5.16,1.22,-5.92,-5.17,1.4,-5.88,-5.25,-0.42,-5.92,-5.59,-0.49,-6.04,-5.76,-0.2,-6.16,-5.71,-0.42,-5.92,-5.94,-0.49,-6.04,-5.76,-0.42,-5.92,-5.59,0.21,-5.96,-6.32,0,-6,-6.14,0.2,-5.84,-6.09,0,-6,-6.14,0.21,-5.96,-6.32,-0.04,-6.2,-6.37,0.21,-5.96,-6.32,0.34,-6.12,-6.41,-0.04,-6.2,-6.37,0.53,-5.84,-6.36,0.51,-6.12,-6.41,0.41,-5.84,-6.31,1.26,-5.64,-5.1,1.24,-5.56,-5.12,1.07,-5.72,-5.05,0.43,-5.84,-4.98,0.26,-6.04,-5.07,0.36,-6.12,-5.03,0.06,-6.12,-5.38,0.12,-6.24,-5.31,0.26,-6.04,-5.07,-0.06,-6.04,-5.47,0.06,-6.12,-5.38,-0.09,-5.88,-5.3,-0.17,-5.96,-5.93,-0.37,-6.28,-5.95,-0.42,-6.12,-5.87,0.64,-5.84,-6.38,0.82,-5.72,-6.39,0.92,-6.08,-6.36,0.97,-6.2,-6.3,1.27,-6.56,-6.24,0.92,-6.44,-6.39,-0.48,-6.12,-5.8,-0.45,-6.2,-5.86,-0.2,-6.16,-5.71,0.13,-5.84,-6.04,0,-6,-6.14,-0.05,-5.96,-5.99,-0.34,-6.2,-6.11,-0.05,-5.96,-5.99,0,-6,-6.14,-0.34,-6.2,-6.11,0,-6,-6.14,-0.13,-6.2,-6.33,0.61,-5.96,-6.33,0.81,-6.2,-6.32,0.71,-6.28,-6.4,1.17,-6.04,-6.27,0.92,-6.08,-6.36,0.82,-5.72,-6.39,1.22,-5.92,-5.17,0.89,-6.08,-5.1,1.32,-6.2,-5.2,0.36,-6.12,-5.03,0.42,-6.32,-5.04,0.81,-6.2,-5.04,-0.49,-6.04,-5.76,-0.48,-6.12,-5.8,-0.2,-6.16,-5.71,-0.52,-6.08,-5.84,-0.42,-5.92,-5.94,-0.42,-6.12,-5.87,-0.04,-6.2,-6.37,-0.13,-6.2,-6.33,0,-6,-6.14,0.53,-5.84,-6.36,0.61,-5.96,-6.33,0.51,-6.12,-6.41,0.81,-6.2,-6.32,0.92,-6.08,-6.36,0.97,-6.2,-6.3,0.89,-6.08,-5.1,0.81,-6.2,-5.04,0.89,-6.24,-5.06,-0.48,-6.12,-5.8,-0.49,-6.04,-5.76,-0.52,-6.08,-5.84,-0.42,-6.12,-5.87,-0.48,-6.12,-5.8,-0.52,-6.08,-5.84,-0.32,-6.36,-6.13,-0.34,-6.2,-6.11,-0.13,-6.2,-6.33,0.61,-5.96,-6.33,0.92,-6.08,-6.36,0.81,-6.2,-6.32,1.4,-5.88,-5.25,1.54,-6.04,-5.53,1.45,-5.56,-5.69,1.07,-5.72,-5.05,0.62,-5.6,-5.04,0.43,-5.84,-4.98,0.84,-6.32,-5.05,0.81,-6.2,-5.04,0.42,-6.32,-5.04,0.12,-6.24,-5.31,0,-6.48,-5.41,0.09,-6.56,-5.32,-0.06,-6.04,-5.47,-0.2,-6.16,-5.71,0,-6.48,-5.41,0.51,-6.12,-6.41,0.34,-6.12,-6.41,0.41,-5.84,-6.31,1.58,-6.36,-5.9,1.54,-6.04,-5.53,1.58,-6.4,-5.53,0.92,-6.4,-5.07,1.34,-6.48,-5.22,1.32,-6.2,-5.2,1.54,-6.04,-5.53,1.4,-5.88,-5.25,1.32,-6.2,-5.2,-0.2,-6.16,-5.71,-0.45,-6.2,-5.86,-0.28,-6.28,-5.9,-0.37,-6.28,-5.95,-0.28,-6.28,-5.9,-0.45,-6.2,-5.86,-0.45,-6.2,-5.86,-0.48,-6.12,-5.8,-0.42,-6.12,-5.87,-0.46,-6.2,-5.91,-0.45,-6.2,-5.86,-0.42,-6.12,-5.87,-0.32,-6.36,-6.13,-0.13,-6.2,-6.33,-0.09,-6.36,-6.29,-0.04,-6.28,-6.41,-0.08,-6.28,-6.4,-0.04,-6.2,-6.37,1.17,-6.04,-6.27,0.82,-5.72,-6.39,1.17,-5.68,-6.27,0.97,-6.2,-6.3,0.92,-6.08,-6.36,1.17,-6.04,-6.27,1.17,-5.68,-6.27,1.52,-5.64,-5.89,1.55,-5.92,-5.88,1.58,-6.4,-5.53,1.54,-6.04,-5.53,1.32,-6.2,-5.2,0.89,-6.24,-5.06,0.84,-6.32,-5.05,0.92,-6.4,-5.07,0.89,-6.24,-5.06,0.81,-6.2,-5.04,0.84,-6.32,-5.05,-0.28,-6.28,-5.9,-0.24,-6.36,-5.86,-0.2,-6.16,-5.71,-0.34,-6.2,-6.11,-0.17,-5.96,-5.93,-0.05,-5.96,-5.99,-0.37,-6.28,-5.95,-0.45,-6.2,-5.86,-0.46,-6.2,-5.91,-0.42,-6.28,-6.02,-0.37,-6.28,-5.95,-0.34,-6.2,-6.11,-0.42,-6.28,-6.02,-0.32,-6.36,-6.13,-0.35,-6.4,-6.04,-0.42,-6.28,-6.02,-0.34,-6.2,-6.11,-0.32,-6.36,-6.13,-0.13,-6.2,-6.33,-0.04,-6.2,-6.37,-0.08,-6.28,-6.4,0.03,-6.32,-6.43,-0.04,-6.28,-6.41,-0.04,-6.2,-6.37,0.97,-6.2,-6.3,0.81,-6.36,-6.39,0.81,-6.2,-6.32,1.26,-6.68,-5.17,1.34,-6.48,-5.22,0.92,-6.4,-5.07,0.65,-6.52,-5.06,0.42,-6.32,-5.04,0.36,-6.6,-5.11,-0.09,-5.88,-5.3,0.06,-6.12,-5.38,0.26,-6.04,-5.07,0.12,-6.24,-5.31,0.36,-6.12,-5.03,0.26,-6.04,-5.07,0.42,-6.32,-5.04,0.12,-6.24,-5.31,0.09,-6.56,-5.32,-0.37,-6.28,-5.95,-0.27,-6.36,-5.91,-0.28,-6.28,-5.9,-0.37,-6.28,-5.95,-0.35,-6.4,-6.04,-0.27,-6.36,-5.91,-0.09,-6.36,-6.29,-0.12,-6.44,-6.12,-0.32,-6.36,-6.13,-0.08,-6.28,-6.4,-0.04,-6.28,-6.41,-0.05,-6.32,-6.42,-0.06,-6.44,-6.39,0.1,-6.56,-6.37,-0.11,-6.56,-6.31,0.03,-6.32,-6.43,-0.05,-6.32,-6.42,-0.04,-6.28,-6.41,0.1,-6.56,-6.37,0.03,-6.32,-6.43,0.34,-6.12,-6.41,0.34,-6.12,-6.41,0.51,-6.12,-6.41,0.53,-6.68,-6.32,0.81,-6.36,-6.39,0.71,-6.28,-6.4,0.81,-6.2,-6.32,1.48,-6.24,-6.05,1.17,-6.04,-6.27,1.55,-5.92,-5.88,1.58,-6.36,-5.9,1.48,-6.24,-6.05,1.55,-5.92,-5.88,0.89,-6.08,-5.1,0.89,-6.24,-5.06,1.32,-6.2,-5.2,1.22,-5.92,-5.17,1.32,-6.2,-5.2,1.4,-5.88,-5.25,0.12,-6.24,-5.31,0.42,-6.32,-5.04,0.36,-6.12,-5.03,-0.27,-6.36,-5.91,-0.24,-6.36,-5.86,-0.28,-6.28,-5.9,1.61,-6.88,-5.78,1.58,-6.4,-5.53,1.56,-6.64,-5.44,-0.13,-6.2,-6.33,-0.08,-6.28,-6.4,-0.09,-6.36,-6.29,-0.06,-6.44,-6.39,-0.09,-6.36,-6.29,-0.05,-6.32,-6.42,-0.08,-6.28,-6.4,-0.05,-6.32,-6.42,-0.09,-6.36,-6.29,0.03,-6.32,-6.43,-0.04,-6.2,-6.37,0.34,-6.12,-6.41,0.71,-6.28,-6.4,0.81,-6.36,-6.39,0.53,-6.68,-6.32,1.27,-6.56,-6.24,1.55,-6.8,-5.99,1.32,-6.92,-6.2,1.27,-6.56,-6.24,1.48,-6.24,-6.05,1.58,-6.36,-5.9,1.32,-6.2,-5.2,0.89,-6.24,-5.06,0.92,-6.4,-5.07,-0.16,-6.56,-5.63,-0.2,-6.72,-5.8,-0.19,-6.76,-5.71,-0.16,-6.56,-5.63,-0.25,-6.64,-5.84,-0.2,-6.72,-5.8,-0.37,-6.28,-5.95,-0.42,-6.28,-6.02,-0.35,-6.4,-6.04,0.1,-6.56,-6.37,0.34,-6.12,-6.41,0.53,-6.68,-6.32,0.51,-6.12,-6.41,0.71,-6.28,-6.4,0.53,-6.68,-6.32,0.97,-6.2,-6.3,0.92,-6.44,-6.39,0.81,-6.36,-6.39,1.55,-6.8,-5.99,1.27,-6.56,-6.24,1.58,-6.36,-5.9,-0.2,-6.16,-5.71,-0.16,-6.56,-5.63,0,-6.48,-5.41,-0.31,-6.48,-5.93,-0.27,-6.36,-5.91,-0.35,-6.4,-6.04,-0.12,-6.44,-6.12,-0.08,-6.52,-6.05,-0.24,-6.52,-5.99,-0.09,-6.36,-6.29,-0.06,-6.44,-6.39,-0.11,-6.56,-6.31,-0.06,-6.44,-6.39,-0.05,-6.32,-6.42,0.03,-6.32,-6.43,0.65,-6.52,-5.06,0.92,-6.4,-5.07,0.84,-6.32,-5.05,0.12,-6.24,-5.31,0.06,-6.12,-5.38,0,-6.48,-5.41,-0.24,-6.36,-5.86,-0.3,-6.48,-5.88,-0.16,-6.56,-5.63,-0.31,-6.48,-5.93,-0.3,-6.48,-5.88,-0.27,-6.36,-5.91,-0.2,-6.16,-5.71,-0.24,-6.36,-5.86,-0.16,-6.56,-5.63,-0.3,-6.48,-5.88,-0.31,-6.48,-5.93,-0.3,-6.52,-5.92,-0.3,-6.52,-5.92,-0.31,-6.48,-5.93,-0.24,-6.52,-5.99,-0.24,-6.52,-5.99,-0.31,-6.48,-5.93,-0.35,-6.4,-6.04,-0.24,-6.52,-5.99,-0.08,-6.52,-6.05,-0.13,-6.64,-5.9,-0.12,-6.44,-6.12,-0.24,-6.52,-5.99,-0.35,-6.4,-6.04,-0.12,-6.44,-6.12,-0.35,-6.4,-6.04,-0.32,-6.36,-6.13,1.48,-6.24,-6.05,1.27,-6.56,-6.24,1.17,-6.04,-6.27,1.05,-6.68,-6.34,1.27,-6.56,-6.24,1.32,-6.92,-6.2,1.55,-6.8,-5.99,1.46,-6.96,-6.11,1.32,-6.92,-6.2,1.56,-6.64,-5.44,1.34,-6.48,-5.22,1.26,-6.68,-5.17,0.42,-6.32,-5.04,0.09,-6.56,-5.32,0.36,-6.6,-5.11,-0.3,-6.48,-5.88,-0.24,-6.36,-5.86,-0.27,-6.36,-5.91,-0.3,-6.48,-5.88,-0.3,-6.52,-5.92,-0.25,-6.64,-5.84,-0.3,-6.52,-5.92,-0.13,-6.64,-5.9,-0.25,-6.64,-5.84,-0.08,-6.52,-6.05,-0.12,-6.44,-6.12,-0.11,-6.56,-6.31,-0.12,-6.44,-6.12,-0.09,-6.36,-6.29,-0.11,-6.56,-6.31,1.56,-6.64,-5.44,1.26,-6.68,-5.17,1.54,-6.8,-5.41,0.38,-6.76,-5.12,0.09,-6.56,-5.32,0.13,-6.92,-5.42,0.09,-6.56,-5.32,0,-6.48,-5.41,-0.09,-6.84,-5.56,0.09,-6.56,-5.32,-0.09,-6.84,-5.56,0.13,-6.92,-5.42,0.06,-6.12,-5.38,-0.06,-6.04,-5.47,0,-6.48,-5.41,-0.3,-6.52,-5.92,-0.24,-6.52,-5.99,-0.13,-6.64,-5.9,-0.01,-6.64,-6.04,-0.13,-6.64,-5.9,-0.08,-6.52,-6.05,0.1,-6.56,-6.37,-0.06,-6.44,-6.39,0.03,-6.32,-6.43,0.81,-6.36,-6.39,0.92,-6.44,-6.39,0.53,-6.68,-6.32,0.92,-6.44,-6.39,1.27,-6.56,-6.24,1.05,-6.68,-6.34,0.92,-6.4,-5.07,0.87,-7.04,-5.07,1.26,-6.68,-5.17,-0.16,-6.56,-5.63,-0.19,-6.76,-5.71,-0.09,-6.84,-5.56,-0.3,-6.48,-5.88,-0.25,-6.64,-5.84,-0.16,-6.56,-5.63,-0.11,-6.8,-6.15,-0.01,-6.64,-6.04,-0.11,-6.56,-6.31,0.53,-6.68,-6.32,0.41,-7.04,-6.39,0.24,-6.8,-6.29,0.92,-6.44,-6.39,1.05,-6.68,-6.34,0.53,-6.68,-6.32,0.09,-6.56,-5.32,0.38,-6.76,-5.12,0.36,-6.6,-5.11,-0.01,-6.64,-6.04,-0.08,-6.52,-6.05,-0.11,-6.56,-6.31,1.34,-6.48,-5.22,1.58,-6.4,-5.53,1.32,-6.2,-5.2,0.92,-6.4,-5.07,0.68,-6.96,-5.08,0.87,-7.04,-5.07,-0.01,-6.64,-6.04,-0.01,-6.68,-5.99,-0.13,-6.64,-5.9,-0.01,-6.68,-5.99,-0.01,-6.64,-6.04,-0.11,-6.8,-6.15,0.65,-6.52,-5.06,0.84,-6.32,-5.05,0.42,-6.32,-5.04,-0.25,-6.64,-5.84,-0.13,-6.64,-5.9,-0.2,-6.72,-5.8,-0.13,-6.88,-5.7,0.07,-7,-5.84,-0.04,-7.04,-5.53,-0.01,-6.68,-5.99,0,-6.76,-5.99,-0.13,-6.64,-5.9,-0.11,-6.8,-6.27,-0.11,-6.8,-6.15,-0.11,-6.56,-6.31,0.24,-6.8,-6.29,0.04,-6.96,-6.26,-0.04,-6.76,-6.33,0.1,-6.56,-6.37,-0.04,-6.76,-6.33,-0.11,-6.56,-6.31,1.27,-6.56,-6.24,0.97,-6.2,-6.3,1.17,-6.04,-6.27,1.2,-7.04,-6.26,1.17,-7,-6.27,1.32,-6.92,-6.2,1.34,-6.48,-5.22,1.56,-6.64,-5.44,1.58,-6.4,-5.53,0.62,-7.2,-5.18,0.68,-6.96,-5.08,0.38,-6.76,-5.12,0,-6.76,-5.99,-0.01,-6.68,-5.99,-0.11,-6.8,-6.15,-0.04,-6.76,-6.33,-0.11,-6.8,-6.27,-0.11,-6.56,-6.31,0.24,-6.8,-6.29,0.41,-7.04,-6.39,0.04,-6.96,-6.26,1.55,-6.8,-5.99,1.58,-7.12,-5.97,1.46,-6.96,-6.11,1.61,-6.88,-5.78,1.58,-6.36,-5.9,1.58,-6.4,-5.53,1.61,-6.88,-5.78,1.56,-6.64,-5.44,1.54,-6.8,-5.41,1.26,-6.68,-5.17,0.87,-7.04,-5.07,1.23,-7.04,-5.16,0.65,-6.52,-5.06,0.36,-6.6,-5.11,0.38,-6.76,-5.12,-0.09,-6.84,-5.56,-0.19,-6.76,-5.71,-0.13,-6.88,-5.7,-0.13,-6.88,-5.7,-0.19,-6.76,-5.71,0.03,-6.84,-5.92,-0.13,-6.88,-5.7,0.03,-6.84,-5.92,0.07,-7,-5.84,-0.2,-6.72,-5.8,-0.13,-6.64,-5.9,0.03,-6.84,-5.92,0.03,-6.84,-5.92,0,-6.76,-5.99,-0.03,-6.84,-6.07,-0.03,-6.84,-6.07,0,-6.76,-5.99,-0.11,-6.8,-6.15,0.04,-6.96,-6.26,-0.08,-6.88,-6.29,-0.04,-6.76,-6.33,0.53,-6.68,-6.32,0.66,-6.92,-6.41,0.41,-7.04,-6.39,1.61,-6.88,-5.78,1.55,-6.8,-5.99,1.58,-6.36,-5.9,1.61,-6.88,-5.78,1.54,-6.8,-5.41,1.61,-7.08,-5.59,0,-6.48,-5.41,-0.16,-6.56,-5.63,-0.09,-6.84,-5.56,0.03,-6.84,-5.92,-0.13,-6.64,-5.9,0,-6.76,-5.99,-0.11,-6.84,-6.15,-0.08,-6.88,-6.29,-0.1,-6.92,-6.27,0.53,-6.68,-6.32,0.24,-6.8,-6.29,0.1,-6.56,-6.37,-0.04,-6.76,-6.33,-0.08,-6.88,-6.29,-0.11,-6.8,-6.27,0.1,-6.56,-6.37,0.24,-6.8,-6.29,-0.04,-6.76,-6.33,-0.09,-6.84,-5.56,-0.13,-6.88,-5.7,-0.04,-7.04,-5.53,-0.11,-6.84,-6.15,-0.11,-6.8,-6.15,-0.11,-6.8,-6.27,-0.11,-6.84,-6.15,-0.11,-6.8,-6.27,-0.08,-6.88,-6.29,0.04,-6.96,-6.26,-0.1,-6.92,-6.27,-0.08,-6.88,-6.29,0.85,-6.92,-6.33,0.66,-6.92,-6.41,0.53,-6.68,-6.32,1.17,-7,-6.27,1.05,-7,-6.3,1.05,-6.68,-6.34,1.26,-6.68,-5.17,1.44,-6.96,-5.3,1.54,-6.8,-5.41,0.92,-6.4,-5.07,0.65,-6.52,-5.06,0.68,-6.96,-5.08,0.69,-7.24,-6.43,0.59,-7.2,-6.43,0.66,-6.92,-6.41,1.33,-7,-6.17,1.32,-6.92,-6.2,1.46,-6.96,-6.11,1.61,-6.88,-5.78,1.61,-7.08,-5.59,1.58,-7.12,-5.97,1.61,-7.08,-5.59,1.4,-7.28,-5.29,1.62,-7.4,-5.65,1.54,-6.8,-5.41,1.44,-6.96,-5.3,1.61,-7.08,-5.59,1.23,-7.04,-5.16,0.87,-7.04,-5.07,0.86,-7.16,-5.06,-0.04,-7.04,-5.53,0.13,-6.92,-5.42,-0.09,-6.84,-5.56,-0.19,-6.76,-5.71,-0.2,-6.72,-5.8,0.03,-6.84,-5.92,0.03,-6.84,-5.92,-0.03,-6.84,-6.07,0.07,-7,-5.84,-0.12,-7.08,-6.17,-0.03,-6.84,-6.07,-0.11,-6.84,-6.15,1.17,-7,-6.27,1.05,-6.68,-6.34,1.32,-6.92,-6.2,1.2,-7.04,-6.26,1.17,-7.04,-6.27,1.17,-7,-6.27,1.21,-7.12,-6.26,1.2,-7.04,-6.26,1.33,-7,-6.17,1.55,-6.8,-5.99,1.61,-6.88,-5.78,1.58,-7.12,-5.97,1.4,-7.28,-5.29,1.23,-7.04,-5.16,0.93,-7.28,-5.07,-0.12,-7.08,-6.17,-0.11,-6.84,-6.15,-0.1,-6.92,-6.27,0.8,-7.24,-6.37,0.66,-6.92,-6.41,0.85,-6.92,-6.33,1.2,-7.04,-6.26,1.32,-6.92,-6.2,1.33,-7,-6.17,1.33,-7,-6.17,1.46,-6.96,-6.11,1.52,-7.32,-6.04,1.24,-7.28,-6.25,1.21,-7.12,-6.26,1.33,-7,-6.17,1.61,-7.08,-5.59,1.62,-7.4,-5.65,1.58,-7.12,-5.97,0.65,-6.52,-5.06,0.38,-6.76,-5.12,0.68,-6.96,-5.08,0.62,-7.2,-5.18,0.86,-7.16,-5.06,0.87,-7.04,-5.07,0.04,-6.96,-6.26,-0.12,-7.08,-6.24,-0.1,-6.92,-6.27,1.05,-6.68,-6.34,0.85,-6.92,-6.33,0.53,-6.68,-6.32,1.06,-7.16,-6.31,1.05,-7,-6.3,1.17,-7.04,-6.27,1.21,-7.12,-6.26,1.17,-7.04,-6.27,1.2,-7.04,-6.26,1.23,-7.04,-5.16,1.44,-6.96,-5.3,1.26,-6.68,-5.17,0.25,-7.32,-5.32,0.38,-6.76,-5.12,0.13,-6.92,-5.42,0.85,-6.92,-6.33,1.06,-7.16,-6.31,0.9,-7.28,-6.36,1.23,-7.04,-5.16,1.4,-7.28,-5.29,1.44,-6.96,-5.3,1.05,-7,-6.3,1.17,-7,-6.27,1.17,-7.04,-6.27,0.62,-7.2,-5.18,0.87,-7.04,-5.07,0.68,-6.96,-5.08,0.25,-7.32,-5.32,0.62,-7.2,-5.18,0.38,-6.76,-5.12,0.59,-7.2,-6.43,0.41,-7.04,-6.39,0.66,-6.92,-6.41,0.8,-7.24,-6.37,0.69,-7.24,-6.43,0.66,-6.92,-6.41,1.05,-7,-6.3,0.85,-6.92,-6.33,1.05,-6.68,-6.34,1.21,-7.12,-6.26,1.06,-7.16,-6.31,1.17,-7.04,-6.27,0.8,-7.24,-6.37,0.85,-6.92,-6.33,0.9,-7.28,-6.36,1.17,-7.28,-6.27,1.21,-7.12,-6.26,1.24,-7.28,-6.25,1.24,-7.28,-6.25,1.33,-7,-6.17,1.52,-7.32,-6.04,0.85,-6.92,-6.33,1.05,-7,-6.3,1.06,-7.16,-6.31,1.06,-7.16,-6.31,1.17,-7.28,-6.27,1.12,-7.32,-6.29,1.17,-7.28,-6.27,1.06,-7.16,-6.31,1.21,-7.12,-6.26,1.61,-7.08,-5.59,1.44,-6.96,-5.3,1.4,-7.28,-5.29,1.23,-7.04,-5.16,0.86,-7.16,-5.06,0.93,-7.28,-5.07,1.46,-6.96,-6.11,1.58,-7.12,-5.97,1.52,-7.32,-6.04,1.52,-7.32,-6.04,1.58,-7.12,-5.97,1.62,-7.4,-5.65,-0.5,-6.12,-5.82,-0.51,-6.08,-5.82,-0.51,-6.08,-5.86,-0.49,-6.12,-5.86])

IndexedFaceSet365.setCoord(Coordinate366)

Shape361.setGeometry(IndexedFaceSet365)

Transform360.addChildren(Shape361)

fieldValue359.addChildren(Transform360)

ProtoInstance357.addFieldValue(fieldValue359)

fieldValue356.addChildren(ProtoInstance357)
ProtoInstance367 = ProtoInstance()
ProtoInstance367.setName("Joint")
ProtoInstance367.setDEF("Allen_hanim_r_knee")
fieldValue368 = fieldValue()
fieldValue368.setName("name")
fieldValue368.setValue("r_knee")

ProtoInstance367.addFieldValue(fieldValue368)
fieldValue369 = fieldValue()
fieldValue369.setName("center")
fieldValue369.setValue("-0.0699 0.51 -0.0166")

ProtoInstance367.addFieldValue(fieldValue369)
fieldValue370 = fieldValue()
fieldValue370.setName("children")
ProtoInstance371 = ProtoInstance()
ProtoInstance371.setName("Segment")
ProtoInstance371.setDEF("Allen_hanim_r_calf")
fieldValue372 = fieldValue()
fieldValue372.setName("name")
fieldValue372.setValue("r_calf")

ProtoInstance371.addFieldValue(fieldValue372)
fieldValue373 = fieldValue()
fieldValue373.setName("children")
Transform374 = Transform()
Transform374.setDEF("r_calf_adjust")
Transform374.setCenter([0.43,1.1,-0.05])
Transform374.setRotation([0,1,0,1.570796])
Transform374.setScale([0.1,0.1,0.1])
Shape375 = Shape()
Appearance376 = Appearance()
Material377 = Material()
Material377.setUSE("Pants_Color")

Appearance376.setMaterial(Material377)
ImageTexture378 = ImageTexture()
ImageTexture378.setUSE("camo")

Appearance376.setTexture(ImageTexture378)

Shape375.setAppearance(Appearance376)
IndexedFaceSet379 = IndexedFaceSet()
IndexedFaceSet379.setCoordIndex([0,1,2,-1,3,4,5,-1,6,7,8,-1,9,10,11,-1,12,13,14,-1,15,16,17,-1,18,19,20,-1,21,22,23,-1,24,25,26,-1,27,28,29,-1,30,31,32,-1,33,34,35,-1,36,37,38,-1,39,40,41,-1,42,43,44,-1,45,46,47,-1,48,49,50,-1,51,52,53,-1,54,55,56,-1,57,58,59,-1,60,61,62,-1,63,64,65,-1,66,67,68,-1,69,70,71,-1,72,73,74,-1,75,76,77,-1,78,79,80,-1,81,82,83,-1,84,85,86,-1,87,88,89,-1,90,91,92,-1,93,94,95,-1,96,97,98,-1,99,100,101,-1,102,103,104,-1,105,106,107,-1,108,109,110,-1,111,112,113,-1,114,115,116,-1,117,118,119,-1,120,121,122,-1,123,124,125,-1,126,127,128,-1,129,130,131,-1,132,133,134,-1,135,136,137,-1,138,139,140,-1,141,142,143,-1,144,145,146,-1,147,148,149,-1,150,151,152,-1,153,154,155,-1,156,157,158,-1,159,160,161,-1,162,163,164,-1,165,166,167,-1,168,169,170,-1,171,172,173,-1,174,175,176,-1,177,178,179,-1,180,181,182,-1,183,184,185,-1,186,187,188,-1,189,190,191,-1,192,193,194,-1,195,196,197,-1,198,199,200,-1,201,202,203,-1,204,205,206,-1,207,208,209,-1,210,211,212,-1,213,214,215,-1,216,217,218,-1,219,220,221,-1,222,223,224,-1,225,226,227,-1,228,229,230,-1,231,232,233,-1,234,235,236,-1,237,238,239,-1,240,241,242,-1,243,244,245,-1,246,247,248,-1,249,250,251,-1,252,253,254,-1,255,256,257,-1,258,259,260,-1,261,262,263,-1,264,265,266,-1,267,268,269,-1,270,271,272,-1,273,274,275,-1,276,277,278,-1,279,280,281,-1,282,283,284,-1,285,286,287,-1,288,289,290,-1,291,292,293,-1,294,295,296,-1,297,298,299,-1,300,301,302,-1,303,304,305,-1,306,307,308,-1,309,310,311,-1,312,313,314,-1,315,316,317,-1,318,319,320,-1,321,322,323,-1,324,325,326,-1,327,328,329,-1,330,331,332,-1,333,334,335,-1,336,337,338,-1,339,340,341,-1,342,343,344,-1,345,346,347,-1,348,349,350,-1,351,352,353,-1,354,355,356,-1,357,358,359,-1,360,361,362,-1,363,364,365,-1,366,367,368,-1,369,370,371,-1,372,373,374,-1,375,376,377,-1,378,379,380,-1,381,382,383,-1,384,385,386,-1,387,388,389,-1,390,391,392,-1,393,394,395,-1,396,397,398,-1,399,400,401,-1,402,403,404,-1,405,406,407,-1,408,409,410,-1,411,412,413,-1,414,415,416,-1,417,418,419,-1,420,421,422,-1,423,424,425,-1,426,427,428,-1,429,430,431,-1,432,433,434,-1,435,436,437,-1,438,439,440,-1,441,442,443,-1,444,445,446,-1,447,448,449,-1,450,451,452,-1,453,454,455,-1,456,457,458,-1,459,460,461,-1,462,463,464,-1,465,466,467,-1,468,469,470,-1,471,472,473,-1,474,475,476,-1,477,478,479,-1,480,481,482,-1,483,484,485,-1,486,487,488,-1,489,490,491,-1,492,493,494,-1,495,496,497,-1,498,499,500,-1,501,502,503,-1,504,505,506,-1,507,508,509,-1,510,511,512,-1,513,514,515,-1,516,517,518,-1,519,520,521,-1,522,523,524,-1,525,526,527,-1,528,529,530,-1,531,532,533,-1,534,535,536,-1,537,538,539,-1,540,541,542,-1,543,544,545,-1,546,547,548,-1,549,550,551,-1,552,553,554,-1,555,556,557,-1,558,559,560,-1,561,562,563,-1,564,565,566,-1,567,568,569,-1,570,571,572,-1,573,574,575,-1,576,577,578,-1,579,580,581,-1,582,583,584,-1,585,586,587,-1,588,589,590,-1,591,592,593,-1,594,595,596,-1,597,598,599,-1,600,601,602,-1,603,604,605,-1,606,607,608,-1,609,610,611,-1,612,613,614,-1,615,616,617,-1,618,619,620,-1,621,622,623,-1,624,625,626,-1,627,628,629,-1,630,631,632,-1,633,634,635,-1,636,637,638,-1,639,640,641,-1,642,643,644,-1,645,646,647,-1,648,649,650,-1,651,652,653,-1,654,655,656,-1,657,658,659,-1,660,661,662,-1,663,664,665,-1,666,667,668,-1,669,670,671,-1,672,673,674,-1,675,676,677,-1,678,679,680,-1,681,682,683,-1,684,685,686,-1,687,688,689,-1,690,691,692,-1,693,694,695,-1,696,697,698,-1,699,700,701,-1,702,703,704,-1,705,706,707,-1,708,709,710,-1,711,712,713,-1,714,715,716,-1,717,718,719,-1,720,721,722,-1,723,724,725,-1,726,727,728,-1,729,730,731,-1,732,733,734,-1,735,736,737,-1,738,739,740,-1,741,742,743,-1,744,745,746,-1,747,748,749,-1,750,751,752,-1,753,754,755,-1,756,757,758,-1,759,760,761,-1,762,763,764,-1,765,766,767,-1,768,769,770,-1,771,772,773,-1,774,775,776,-1,777,778,779,-1,780,781,782,-1,783,784,785,-1,786,787,788,-1,789,790,791,-1,792,793,794,-1,795,796,797,-1,798,799,800,-1,801,802,803,-1,804,805,806,-1,807,808,809,-1,810,811,812,-1,813,814,815,-1,816,817,818,-1,819,820,821,-1,822,823,824,-1,825,826,827,-1,828,829,830,-1,831,832,833,-1,834,835,836,-1,837,838,839,-1,840,841,842,-1,843,844,845,-1,846,847,848,-1,849,850,851,-1,852,853,854,-1,855,856,857,-1,858,859,860,-1,861,862,863,-1,864,865,866,-1,867,868,869,-1,870,871,872,-1,873,874,875,-1,876,877,878,-1,879,880,881,-1,882,883,884,-1,885,886,887,-1,888,889,890,-1,891,892,893,-1,894,895,896,-1,897,898,899,-1,900,901,902,-1,903,904,905,-1,906,907,908,-1,909,910,911,-1,912,913,914,-1,915,916,917,-1,918,919,920,-1,921,922,923,-1,924,925,926,-1,927,928,929,-1,930,931,932,-1,933,934,935,-1,936,937,938,-1,939,940,941,-1,942,943,944,-1,945,946,947,-1,948,949,950,-1,951,952,953,-1,954,955,956,-1,957,958,959,-1,960,961,962,-1,963,964,965,-1,966,967,968,-1,969,970,971,-1,972,973,974,-1,975,976,977,-1,978,979,980,-1,981,982,983,-1,984,985,986,-1,987,988,989,-1,990,991,992,-1,993,994,995,-1,996,997,998,-1,999,1000,1001,-1,1002,1003,1004,-1,1005,1006,1007,-1,1008,1009,1010,-1,1011,1012,1013,-1,1014,1015,1016,-1,1017,1018,1019,-1,1020,1021,1022,-1,1023,1024,1025,-1,1026,1027,1028,-1,1029,1030,1031,-1,1032,1033,1034,-1,1035,1036,1037,-1,1038,1039,1040,-1,1041,1042,1043,-1,1044,1045,1046,-1,1047,1048,1049,-1,1050,1051,1052,-1,1053,1054,1055,-1,1056,1057,1058,-1,1059,1060,1061,-1,1062,1063,1064,-1,1065,1066,1067,-1,1068,1069,1070,-1,1071,1072,1073,-1,1074,1075,1076,-1,1077,1078,1079,-1,1080,1081,1082,-1,1083,1084,1085,-1,1086,1087,1088,-1,1089,1090,1091,-1,1092,1093,1094,-1,1095,1096,1097,-1,1098,1099,1100,-1,1101,1102,1103,-1,1104,1105,1106,-1,1107,1108,1109,-1,1110,1111,1112,-1,1113,1114,1115,-1,1116,1117,1118,-1,1119,1120,1121,-1,1122,1123,1124,-1,1125,1126,1127,-1,1128,1129,1130,-1,1131,1132,1133,-1,1134,1135,1136,-1,1137,1138,1139,-1,1140,1141,1142,-1,1143,1144,1145,-1,1146,1147,1148,-1,1149,1150,1151,-1,1152,1153,1154,-1,1155,1156,1157,-1,1158,1159,1160,-1,1161,1162,1163,-1,1164,1165,1166,-1,1167,1168,1169,-1,1170,1171,1172,-1,1173,1174,1175,-1,1176,1177,1178,-1,1179,1180,1181,-1,1182,1183,1184,-1,1185,1186,1187,-1,1188,1189,1190,-1,1191,1192,1193,-1,1194,1195,1196,-1,1197,1198,1199,-1,1200,1201,1202,-1,1203,1204,1205,-1,1206,1207,1208,-1,1209,1210,1211,-1,1212,1213,1214,-1,1215,1216,1217,-1,1218,1219,1220,-1,1221,1222,1223,-1,1224,1225,1226,-1,1227,1228,1229,-1,1230,1231,1232,-1,1233,1234,1235,-1,1236,1237,1238,-1,1239,1240,1241,-1,1242,1243,1244,-1,1245,1246,1247,-1,1248,1249,1250,-1,1251,1252,1253,-1,1254,1255,1256,-1,1257,1258,1259,-1,1260,1261,1262,-1,1263,1264,1265,-1,1266,1267,1268,-1,1269,1270,1271,-1,1272,1273,1274,-1,1275,1276,1277,-1,1278,1279,1280,-1,1281,1282,1283,-1,1284,1285,1286,-1,1287,1288,1289,-1,1290,1291,1292,-1,1293,1294,1295,-1,1296,1297,1298,-1,1299,1300,1301,-1,1302,1303,1304,-1,1305,1306,1307,-1,1308,1309,1310,-1,1311,1312,1313,-1,1314,1315,1316,-1,1317,1318,1319,-1,1320,1321,1322,-1,1323,1324,1325,-1,1326,1327,1328,-1,1329,1330,1331,-1,1332,1333,1334,-1,1335,1336,1337,-1,1338,1339,1340,-1,1341,1342,1343,-1,1344,1345,1346,-1,1347,1348,1349,-1,1350,1351,1352,-1,1353,1354,1355,-1,1356,1357,1358,-1,1359,1360,1361,-1,1362,1363,1364,-1,1365,1366,1367,-1,1368,1369,1370,-1,1371,1372,1373,-1,1374,1375,1376,-1,1377,1378,1379,-1,1380,1381,1382,-1,1383,1384,1385,-1,1386,1387,1388,-1,1389,1390,1391,-1,1392,1393,1394,-1,1395,1396,1397,-1,1398,1399,1400,-1,1401,1402,1403,-1,1404,1405,1406,-1,1407,1408,1409,-1,1410,1411,1412,-1,1413,1414,1415,-1,1416,1417,1418,-1,1419,1420,1421,-1,1422,1423,1424,-1,1425,1426,1427,-1,1428,1429,1430,-1,1431,1432,1433,-1,1434,1435,1436,-1,1437,1438,1439,-1,1440,1441,1442,-1,1443,1444,1445,-1,1446,1447,1448,-1,1449,1450,1451,-1,1452,1453,1454,-1,1455,1456,1457,-1,1458,1459,1460,-1,1461,1462,1463,-1,1464,1465,1466,-1,1467,1468,1469,-1,1470,1471,1472,-1,1473,1474,1475,-1,1476,1477,1478,-1,1479,1480,1481,-1,1482,1483,1484,-1,1485,1486,1487,-1,1488,1489,1490,-1,1491,1492,1493,-1,1494,1495,1496,-1,1497,1498,1499,-1,1500,1501,1502,-1,1503,1504,1505,-1,1506,1507,1508,-1,1509,1510,1511,-1,1512,1513,1514,-1,1515,1516,1517,-1,1518,1519,1520,-1,1521,1522,1523,-1,1524,1525,1526,-1,1527,1528,1529,-1,1530,1531,1532,-1,1533,1534,1535,-1,1536,1537,1538,-1,1539,1540,1541,-1,1542,1543,1544,-1,1545,1546,1547,-1,1548,1549,1550,-1,1551,1552,1553,-1,1554,1555,1556,-1,1557,1558,1559,-1,1560,1561,1562,-1,1563,1564,1565,-1,1566,1567,1568,-1,1569,1570,1571,-1,1572,1573,1574,-1,1575,1576,1577,-1,1578,1579,1580,-1,1581,1582,1583,-1,1584,1585,1586,-1,1587,1588,1589,-1,1590,1591,1592,-1,1593,1594,1595,-1,1596,1597,1598,-1,1599,1600,1601,-1,1602,1603,1604,-1,1605,1606,1607,-1,1608,1609,1610,-1,1611,1612,1613,-1,1614,1615,1616,-1,1617,1618,1619,-1,1620,1621,1622,-1,1623,1624,1625,-1,1626,1627,1628,-1,1629,1630,1631,-1,1632,1633,1634,-1,1635,1636,1637,-1,1638,1639,1640,-1,1641,1642,1643,-1,1644,1645,1646,-1,1647,1648,1649,-1,1650,1651,1652,-1,1653,1654,1655,-1,1656,1657,1658,-1,1659,1660,1661,-1,1662,1663,1664,-1,1665,1666,1667,-1,1668,1669,1670,-1,1671,1672,1673,-1,1674,1675,1676,-1,1677,1678,1679,-1,1680,1681,1682,-1,1683,1684,1685,-1,1686,1687,1688,-1,1689,1690,1691,-1,1692,1693,1694,-1,1695,1696,1697,-1,1698,1699,1700,-1,1701,1702,1703,-1,1704,1705,1706,-1,1707,1708,1709,-1,1710,1711,1712,-1,1713,1714,1715,-1,1716,1717,1718,-1,1719,1720,1721,-1,1722,1723,1724,-1,1725,1726,1727,-1,1728,1729,1730,-1,1731,1732,1733,-1,1734,1735,1736,-1,1737,1738,1739,-1,1740,1741,1742,-1,1743,1744,1745,-1,1746,1747,1748,-1,1749,1750,1751,-1,1752,1753,1754,-1,1755,1756,1757,-1,1758,1759,1760,-1,1761,1762,1763,-1,1764,1765,1766,-1,1767,1768,1769,-1,1770,1771,1772,-1,1773,1774,1775,-1,1776,1777,1778,-1,1779,1780,1781,-1,1782,1783,1784,-1,1785,1786,1787,-1,1788,1789,1790,-1,1791,1792,1793,-1,1794,1795,1796,-1,1797,1798,1799,-1,1800,1801,1802,-1,1803,1804,1805,-1,1806,1807,1808,-1,1809,1810,1811,-1,1812,1813,1814,-1,1815,1816,1817,-1,1818,1819,1820,-1,1821,1822,1823,-1,1824,1825,1826,-1,1827,1828,1829,-1,1830,1831,1832,-1,1830,1832,1833,-1])
IndexedFaceSet379.setCreaseAngle(1.57)
Coordinate380 = Coordinate()
Coordinate380.setPoint([-0.42,-5.92,-5.94,-0.52,-6.08,-5.84,-0.49,-6.04,-5.76,-0.42,-5.92,-5.59,-0.2,-6.16,-5.71,-0.06,-6.04,-5.47,0.51,-6.12,-6.41,0.61,-5.96,-6.33,0.71,-6.28,-6.4,0.43,-5.84,-4.98,0.36,-6.12,-5.03,0.81,-6.2,-5.04,-0.37,-6.28,-5.95,-0.46,-6.2,-5.91,-0.42,-6.12,-5.87,-0.42,-6.12,-5.87,-0.42,-5.92,-5.94,-0.17,-5.96,-5.93,-0.17,-5.96,-5.93,-0.34,-6.2,-6.11,-0.37,-6.28,-5.95,-0.42,-5.92,-5.59,-0.49,-6.04,-5.76,-0.2,-6.16,-5.71,-0.42,-5.92,-5.94,-0.49,-6.04,-5.76,-0.42,-5.92,-5.59,0,-6,-6.14,0.21,-5.96,-6.32,-0.04,-6.2,-6.37,0.21,-5.96,-6.32,0.34,-6.12,-6.41,-0.04,-6.2,-6.37,0.06,-6.12,-5.38,0.12,-6.24,-5.31,0.26,-6.04,-5.07,-0.06,-6.04,-5.47,0.06,-6.12,-5.38,-0.09,-5.88,-5.3,-0.17,-5.96,-5.93,-0.37,-6.28,-5.95,-0.42,-6.12,-5.87,0.97,-6.2,-6.3,1.27,-6.56,-6.24,0.92,-6.44,-6.39,-0.48,-6.12,-5.8,-0.45,-6.2,-5.86,-0.2,-6.16,-5.71,-0.34,-6.2,-6.11,-0.05,-5.96,-5.99,0,-6,-6.14,-0.34,-6.2,-6.11,0,-6,-6.14,-0.13,-6.2,-6.33,0.61,-5.96,-6.33,0.81,-6.2,-6.32,0.71,-6.28,-6.4,0.36,-6.12,-5.03,0.42,-6.32,-5.04,0.81,-6.2,-5.04,-0.49,-6.04,-5.76,-0.48,-6.12,-5.8,-0.2,-6.16,-5.71,-0.52,-6.08,-5.84,-0.42,-5.92,-5.94,-0.42,-6.12,-5.87,-0.04,-6.2,-6.37,-0.13,-6.2,-6.33,0,-6,-6.14,0.81,-6.2,-6.32,0.92,-6.08,-6.36,0.97,-6.2,-6.3,0.89,-6.08,-5.09,0.81,-6.2,-5.04,0.89,-6.24,-5.05,-0.48,-6.12,-5.8,-0.49,-6.04,-5.76,-0.52,-6.08,-5.84,-0.42,-6.12,-5.87,-0.48,-6.12,-5.8,-0.52,-6.08,-5.84,-0.32,-6.36,-6.13,-0.34,-6.2,-6.11,-0.13,-6.2,-6.33,0.61,-5.96,-6.33,0.92,-6.08,-6.36,0.81,-6.2,-6.32,0.84,-6.32,-5.05,0.81,-6.2,-5.04,0.42,-6.32,-5.04,0.12,-6.24,-5.31,0,-6.48,-5.41,0.09,-6.56,-5.32,-0.06,-6.04,-5.47,-0.2,-6.16,-5.71,0,-6.48,-5.41,1.58,-6.36,-5.9,1.54,-6.04,-5.53,1.58,-6.4,-5.53,0.92,-6.4,-5.07,1.34,-6.48,-5.22,1.32,-6.2,-5.2,-0.2,-6.16,-5.71,-0.45,-6.2,-5.86,-0.28,-6.28,-5.9,-0.37,-6.28,-5.95,-0.28,-6.28,-5.9,-0.45,-6.2,-5.86,-0.45,-6.2,-5.86,-0.48,-6.12,-5.8,-0.42,-6.12,-5.87,-0.46,-6.2,-5.91,-0.45,-6.2,-5.86,-0.42,-6.12,-5.87,-0.32,-6.36,-6.13,-0.13,-6.2,-6.33,-0.09,-6.36,-6.29,-0.04,-6.28,-6.41,-0.08,-6.28,-6.4,-0.04,-6.2,-6.37,0.97,-6.2,-6.3,0.92,-6.08,-6.36,1.17,-6.04,-6.27,1.58,-6.4,-5.53,1.54,-6.04,-5.53,1.32,-6.2,-5.2,0.89,-6.24,-5.05,0.84,-6.32,-5.05,0.92,-6.4,-5.07,0.89,-6.24,-5.05,0.81,-6.2,-5.04,0.84,-6.32,-5.05,-0.28,-6.28,-5.9,-0.24,-6.36,-5.86,-0.2,-6.16,-5.71,-0.34,-6.2,-6.11,-0.17,-5.96,-5.93,-0.05,-5.96,-5.99,-0.37,-6.28,-5.95,-0.45,-6.2,-5.86,-0.46,-6.2,-5.91,-0.42,-6.28,-6.02,-0.37,-6.28,-5.95,-0.34,-6.2,-6.11,-0.42,-6.28,-6.02,-0.32,-6.36,-6.13,-0.35,-6.4,-6.04,-0.42,-6.28,-6.02,-0.34,-6.2,-6.11,-0.32,-6.36,-6.13,-0.13,-6.2,-6.33,-0.04,-6.2,-6.37,-0.08,-6.28,-6.4,0.03,-6.32,-6.43,-0.04,-6.28,-6.41,-0.04,-6.2,-6.37,0.97,-6.2,-6.3,0.81,-6.36,-6.38,0.81,-6.2,-6.32,1.26,-6.68,-5.17,1.34,-6.48,-5.22,0.92,-6.4,-5.07,0.65,-6.52,-5.06,0.42,-6.32,-5.04,0.36,-6.6,-5.11,-0.09,-5.88,-5.3,0.06,-6.12,-5.38,0.26,-6.04,-5.07,0.12,-6.24,-5.31,0.36,-6.12,-5.03,0.26,-6.04,-5.07,0.42,-6.32,-5.04,0.12,-6.24,-5.31,0.09,-6.56,-5.32,-0.37,-6.28,-5.95,-0.27,-6.36,-5.91,-0.28,-6.28,-5.9,-0.37,-6.28,-5.95,-0.35,-6.4,-6.04,-0.27,-6.36,-5.91,-0.09,-6.36,-6.29,-0.12,-6.44,-6.12,-0.32,-6.36,-6.13,-0.08,-6.28,-6.4,-0.04,-6.28,-6.41,-0.05,-6.32,-6.42,-0.06,-6.44,-6.39,0.1,-6.56,-6.37,-0.11,-6.56,-6.31,0.03,-6.32,-6.43,-0.05,-6.32,-6.42,-0.04,-6.28,-6.41,0.1,-6.56,-6.37,0.03,-6.32,-6.43,0.34,-6.12,-6.41,0.34,-6.12,-6.41,0.51,-6.12,-6.41,0.53,-6.68,-6.32,0.81,-6.36,-6.38,0.71,-6.28,-6.4,0.81,-6.2,-6.32,1.58,-6.36,-5.9,1.48,-6.24,-6.05,1.55,-5.92,-5.88,0.89,-6.08,-5.09,0.89,-6.24,-5.05,1.32,-6.2,-5.2,0.12,-6.24,-5.31,0.42,-6.32,-5.04,0.36,-6.12,-5.03,-0.27,-6.36,-5.91,-0.24,-6.36,-5.86,-0.28,-6.28,-5.9,1.61,-6.88,-5.78,1.58,-6.4,-5.53,1.56,-6.64,-5.43,-0.13,-6.2,-6.33,-0.08,-6.28,-6.4,-0.09,-6.36,-6.29,-0.06,-6.44,-6.39,-0.09,-6.36,-6.29,-0.05,-6.32,-6.42,-0.08,-6.28,-6.4,-0.05,-6.32,-6.42,-0.09,-6.36,-6.29,0.03,-6.32,-6.43,-0.04,-6.2,-6.37,0.34,-6.12,-6.41,0.71,-6.28,-6.4,0.81,-6.36,-6.38,0.53,-6.68,-6.32,1.27,-6.56,-6.24,1.55,-6.8,-5.99,1.32,-6.92,-6.2,1.27,-6.56,-6.24,1.48,-6.24,-6.05,1.58,-6.36,-5.9,1.32,-6.2,-5.2,0.89,-6.24,-5.05,0.92,-6.4,-5.07,-0.16,-6.56,-5.62,-0.2,-6.72,-5.8,-0.19,-6.76,-5.71,-0.16,-6.56,-5.62,-0.25,-6.64,-5.83,-0.2,-6.72,-5.8,-0.37,-6.28,-5.95,-0.42,-6.28,-6.02,-0.35,-6.4,-6.04,0.1,-6.56,-6.37,0.34,-6.12,-6.41,0.53,-6.68,-6.32,0.51,-6.12,-6.41,0.71,-6.28,-6.4,0.53,-6.68,-6.32,0.97,-6.2,-6.3,0.92,-6.44,-6.39,0.81,-6.36,-6.38,1.55,-6.8,-5.99,1.27,-6.56,-6.24,1.58,-6.36,-5.9,-0.2,-6.16,-5.71,-0.16,-6.56,-5.62,0,-6.48,-5.41,-0.31,-6.48,-5.93,-0.27,-6.36,-5.91,-0.35,-6.4,-6.04,-0.12,-6.44,-6.12,-0.08,-6.52,-6.05,-0.24,-6.52,-5.99,-0.09,-6.36,-6.29,-0.06,-6.44,-6.39,-0.11,-6.56,-6.31,-0.06,-6.44,-6.39,-0.05,-6.32,-6.42,0.03,-6.32,-6.43,0.65,-6.52,-5.06,0.92,-6.4,-5.07,0.84,-6.32,-5.05,0.12,-6.24,-5.31,0.06,-6.12,-5.38,0,-6.48,-5.41,-0.24,-6.36,-5.86,-0.3,-6.48,-5.88,-0.16,-6.56,-5.62,-0.31,-6.48,-5.93,-0.3,-6.48,-5.88,-0.27,-6.36,-5.91,-0.2,-6.16,-5.71,-0.24,-6.36,-5.86,-0.16,-6.56,-5.62,-0.3,-6.48,-5.88,-0.31,-6.48,-5.93,-0.3,-6.52,-5.92,-0.3,-6.52,-5.92,-0.31,-6.48,-5.93,-0.24,-6.52,-5.99,-0.24,-6.52,-5.99,-0.31,-6.48,-5.93,-0.35,-6.4,-6.04,-0.24,-6.52,-5.99,-0.08,-6.52,-6.05,-0.13,-6.64,-5.9,-0.12,-6.44,-6.12,-0.24,-6.52,-5.99,-0.35,-6.4,-6.04,-0.12,-6.44,-6.12,-0.35,-6.4,-6.04,-0.32,-6.36,-6.13,1.48,-6.24,-6.05,1.27,-6.56,-6.24,1.17,-6.04,-6.27,1.05,-6.68,-6.34,1.27,-6.56,-6.24,1.32,-6.92,-6.2,1.55,-6.8,-5.99,1.46,-6.96,-6.11,1.32,-6.92,-6.2,1.56,-6.64,-5.43,1.34,-6.48,-5.22,1.26,-6.68,-5.17,0.42,-6.32,-5.04,0.09,-6.56,-5.32,0.36,-6.6,-5.11,-0.3,-6.48,-5.88,-0.24,-6.36,-5.86,-0.27,-6.36,-5.91,-0.3,-6.48,-5.88,-0.3,-6.52,-5.92,-0.25,-6.64,-5.83,-0.3,-6.52,-5.92,-0.13,-6.64,-5.9,-0.25,-6.64,-5.83,-0.08,-6.52,-6.05,-0.12,-6.44,-6.12,-0.11,-6.56,-6.31,-0.12,-6.44,-6.12,-0.09,-6.36,-6.29,-0.11,-6.56,-6.31,1.56,-6.64,-5.43,1.26,-6.68,-5.17,1.54,-6.8,-5.41,0.38,-6.76,-5.12,0.09,-6.56,-5.32,0.13,-6.92,-5.42,0.09,-6.56,-5.32,0,-6.48,-5.41,-0.09,-6.84,-5.56,0.09,-6.56,-5.32,-0.09,-6.84,-5.56,0.13,-6.92,-5.42,0.06,-6.12,-5.38,-0.06,-6.04,-5.47,0,-6.48,-5.41,-0.3,-6.52,-5.92,-0.24,-6.52,-5.99,-0.13,-6.64,-5.9,-0.01,-6.64,-6.04,-0.13,-6.64,-5.9,-0.08,-6.52,-6.05,0.1,-6.56,-6.37,-0.06,-6.44,-6.39,0.03,-6.32,-6.43,0.81,-6.36,-6.38,0.92,-6.44,-6.39,0.53,-6.68,-6.32,0.92,-6.44,-6.39,1.27,-6.56,-6.24,1.05,-6.68,-6.34,0.92,-6.4,-5.07,0.87,-7.04,-5.07,1.26,-6.68,-5.17,-0.16,-6.56,-5.62,-0.19,-6.76,-5.71,-0.09,-6.84,-5.56,-0.3,-6.48,-5.88,-0.25,-6.64,-5.83,-0.16,-6.56,-5.62,-0.11,-6.8,-6.15,-0.01,-6.64,-6.04,-0.11,-6.56,-6.31,0.53,-6.68,-6.32,0.41,-7.04,-6.39,0.24,-6.8,-6.29,0.92,-6.44,-6.39,1.05,-6.68,-6.34,0.53,-6.68,-6.32,0.09,-6.56,-5.32,0.38,-6.76,-5.12,0.36,-6.6,-5.11,-0.01,-6.64,-6.04,-0.08,-6.52,-6.05,-0.11,-6.56,-6.31,1.34,-6.48,-5.22,1.58,-6.4,-5.53,1.32,-6.2,-5.2,0.92,-6.4,-5.07,0.68,-6.96,-5.08,0.87,-7.04,-5.07,-0.01,-6.64,-6.04,-0.01,-6.68,-5.99,-0.13,-6.64,-5.9,-0.01,-6.68,-5.99,-0.01,-6.64,-6.04,-0.11,-6.8,-6.15,0.65,-6.52,-5.06,0.84,-6.32,-5.05,0.42,-6.32,-5.04,-0.25,-6.64,-5.83,-0.13,-6.64,-5.9,-0.2,-6.72,-5.8,-0.13,-6.88,-5.7,0.07,-7,-5.84,-0.04,-7.04,-5.52,-0.01,-6.68,-5.99,0,-6.76,-5.98,-0.13,-6.64,-5.9,-0.11,-6.8,-6.27,-0.11,-6.8,-6.15,-0.11,-6.56,-6.31,0.24,-6.8,-6.29,0.04,-6.96,-6.26,-0.04,-6.76,-6.33,0.1,-6.56,-6.37,-0.04,-6.76,-6.33,-0.11,-6.56,-6.31,1.27,-6.56,-6.24,0.97,-6.2,-6.3,1.17,-6.04,-6.27,1.2,-7.04,-6.26,1.17,-7,-6.27,1.32,-6.92,-6.2,1.34,-6.48,-5.22,1.56,-6.64,-5.43,1.58,-6.4,-5.53,0.62,-7.2,-5.18,0.68,-6.96,-5.08,0.38,-6.76,-5.12,0,-6.76,-5.98,-0.01,-6.68,-5.99,-0.11,-6.8,-6.15,-0.04,-6.76,-6.33,-0.11,-6.8,-6.27,-0.11,-6.56,-6.31,0.24,-6.8,-6.29,0.41,-7.04,-6.39,0.04,-6.96,-6.26,1.55,-6.8,-5.99,1.58,-7.12,-5.97,1.46,-6.96,-6.11,1.61,-6.88,-5.78,1.58,-6.36,-5.9,1.58,-6.4,-5.53,1.61,-6.88,-5.78,1.56,-6.64,-5.43,1.54,-6.8,-5.41,1.26,-6.68,-5.17,0.87,-7.04,-5.07,1.23,-7.04,-5.16,0.65,-6.52,-5.06,0.36,-6.6,-5.11,0.38,-6.76,-5.12,-0.09,-6.84,-5.56,-0.19,-6.76,-5.71,-0.13,-6.88,-5.7,-0.13,-6.88,-5.7,-0.19,-6.76,-5.71,0.03,-6.84,-5.92,-0.13,-6.88,-5.7,0.03,-6.84,-5.92,0.07,-7,-5.84,-0.2,-6.72,-5.8,-0.13,-6.64,-5.9,0.03,-6.84,-5.92,0.03,-6.84,-5.92,0,-6.76,-5.98,-0.03,-6.84,-6.07,-0.03,-6.84,-6.07,0,-6.76,-5.98,-0.11,-6.8,-6.15,0.04,-6.96,-6.26,-0.08,-6.88,-6.28,-0.04,-6.76,-6.33,0.53,-6.68,-6.32,0.66,-6.92,-6.41,0.41,-7.04,-6.39,1.61,-6.88,-5.78,1.55,-6.8,-5.99,1.58,-6.36,-5.9,1.61,-6.88,-5.78,1.54,-6.8,-5.41,1.61,-7.08,-5.59,0,-6.48,-5.41,-0.16,-6.56,-5.62,-0.09,-6.84,-5.56,0.03,-6.84,-5.92,-0.13,-6.64,-5.9,0,-6.76,-5.98,-0.03,-6.84,-6.07,-0.12,-7.08,-6.17,-0.06,-7.2,-6.04,-0.11,-6.84,-6.15,-0.08,-6.88,-6.28,-0.1,-6.92,-6.26,0.53,-6.68,-6.32,0.24,-6.8,-6.29,0.1,-6.56,-6.37,-0.04,-6.76,-6.33,-0.08,-6.88,-6.28,-0.11,-6.8,-6.27,0.1,-6.56,-6.37,0.24,-6.8,-6.29,-0.04,-6.76,-6.33,-0.09,-6.84,-5.56,-0.13,-6.88,-5.7,-0.04,-7.04,-5.52,-0.11,-6.84,-6.15,-0.11,-6.8,-6.15,-0.11,-6.8,-6.27,-0.11,-6.84,-6.15,-0.11,-6.8,-6.27,-0.08,-6.88,-6.28,0.04,-6.96,-6.26,-0.1,-6.92,-6.26,-0.08,-6.88,-6.28,0.85,-6.92,-6.33,0.66,-6.92,-6.41,0.53,-6.68,-6.32,1.17,-7,-6.27,1.05,-7,-6.3,1.05,-6.68,-6.34,1.26,-6.68,-5.17,1.44,-6.96,-5.3,1.54,-6.8,-5.41,0.92,-6.4,-5.07,0.65,-6.52,-5.06,0.68,-6.96,-5.08,0.69,-7.24,-6.42,0.59,-7.2,-6.43,0.66,-6.92,-6.41,1.33,-7,-6.17,1.32,-6.92,-6.2,1.46,-6.96,-6.11,1.61,-6.88,-5.78,1.61,-7.08,-5.59,1.58,-7.12,-5.97,1.61,-7.08,-5.59,1.4,-7.28,-5.29,1.62,-7.4,-5.65,1.54,-6.8,-5.41,1.44,-6.96,-5.3,1.61,-7.08,-5.59,1.23,-7.04,-5.16,0.87,-7.04,-5.07,0.86,-7.16,-5.06,-0.04,-7.04,-5.52,0.13,-6.92,-5.42,-0.09,-6.84,-5.56,-0.19,-6.76,-5.71,-0.2,-6.72,-5.8,0.03,-6.84,-5.92,0.03,-6.84,-5.92,-0.03,-6.84,-6.07,0.07,-7,-5.84,-0.12,-7.08,-6.17,-0.03,-6.84,-6.07,-0.11,-6.84,-6.15,1.17,-7,-6.27,1.05,-6.68,-6.34,1.32,-6.92,-6.2,1.2,-7.04,-6.26,1.17,-7.04,-6.27,1.17,-7,-6.27,1.21,-7.12,-6.26,1.2,-7.04,-6.26,1.33,-7,-6.17,1.55,-6.8,-5.99,1.61,-6.88,-5.78,1.58,-7.12,-5.97,1.4,-7.28,-5.29,1.23,-7.04,-5.16,0.93,-7.28,-5.07,-0.12,-7.08,-6.17,-0.11,-6.84,-6.15,-0.1,-6.92,-6.26,0.8,-7.24,-6.37,0.66,-6.92,-6.41,0.85,-6.92,-6.33,1.2,-7.04,-6.26,1.32,-6.92,-6.2,1.33,-7,-6.17,1.33,-7,-6.17,1.46,-6.96,-6.11,1.52,-7.32,-6.04,1.24,-7.28,-6.25,1.21,-7.12,-6.26,1.33,-7,-6.17,1.61,-7.08,-5.59,1.62,-7.4,-5.65,1.58,-7.12,-5.97,0.65,-6.52,-5.06,0.38,-6.76,-5.12,0.68,-6.96,-5.08,0.62,-7.2,-5.18,0.86,-7.16,-5.06,0.87,-7.04,-5.07,0.06,-7.16,-5.45,0.08,-7.32,-5.5,0.25,-7.32,-5.32,-0.04,-7.04,-5.52,0.06,-7.16,-5.45,0.13,-6.92,-5.42,-0.04,-7.04,-5.52,0.07,-7,-5.84,-0.01,-7.16,-5.6,0.04,-6.96,-6.26,-0.07,-7.12,-6.28,-0.12,-7.08,-6.24,0.04,-6.96,-6.26,-0.12,-7.08,-6.24,-0.1,-6.92,-6.26,1.05,-6.68,-6.34,0.85,-6.92,-6.33,0.53,-6.68,-6.32,1.06,-7.16,-6.31,1.05,-7,-6.3,1.17,-7.04,-6.27,1.21,-7.12,-6.26,1.17,-7.04,-6.27,1.2,-7.04,-6.26,1.23,-7.04,-5.16,1.44,-6.96,-5.3,1.26,-6.68,-5.17,0.25,-7.32,-5.32,0.38,-6.76,-5.12,0.13,-6.92,-5.42,0.07,-7,-5.84,0.12,-7.2,-5.76,-0.01,-7.16,-5.6,-0.12,-7.08,-6.24,-0.12,-7.12,-6.21,-0.12,-7.08,-6.17,0.85,-6.92,-6.33,1.06,-7.16,-6.31,0.9,-7.28,-6.36,1.4,-7.28,-5.29,1.53,-7.6,-5.46,1.62,-7.4,-5.65,1.23,-7.04,-5.16,1.4,-7.28,-5.29,1.44,-6.96,-5.3,-0.01,-7.16,-5.6,0.06,-7.16,-5.45,-0.04,-7.04,-5.52,-0.01,-7.16,-5.6,0.12,-7.2,-5.76,0.02,-7.24,-5.57,-0.12,-7.08,-6.17,-0.12,-7.12,-6.21,-0.06,-7.2,-6.04,-0.07,-7.12,-6.28,-0.05,-7.24,-6.3,-0.12,-7.12,-6.21,-0.12,-7.08,-6.24,-0.12,-7.08,-6.17,-0.1,-6.92,-6.26,1.05,-7,-6.3,1.17,-7,-6.27,1.17,-7.04,-6.27,0.62,-7.2,-5.18,0.87,-7.04,-5.07,0.68,-6.96,-5.08,0.25,-7.32,-5.32,0.62,-7.2,-5.18,0.38,-6.76,-5.12,0.12,-7.2,-5.76,0.06,-7.32,-5.62,0.02,-7.24,-5.57,0.1,-7.24,-5.91,0.12,-7.2,-5.76,0.07,-7,-5.84,0.1,-7.24,-5.91,-0.06,-7.2,-6.04,-0.09,-7.36,-6.06,-0.12,-7.12,-6.21,-0.12,-7.08,-6.24,-0.07,-7.12,-6.28,0.59,-7.2,-6.43,0.41,-7.04,-6.39,0.66,-6.92,-6.41,0.59,-7.2,-6.43,0.54,-7.28,-6.43,0.41,-7.04,-6.39,0.8,-7.24,-6.37,0.69,-7.24,-6.42,0.66,-6.92,-6.41,1.05,-7,-6.3,0.85,-6.92,-6.33,1.05,-6.68,-6.34,1.21,-7.12,-6.26,1.06,-7.16,-6.31,1.17,-7.04,-6.27,0.93,-7.28,-5.07,0.91,-7.56,-5.09,1.32,-7.48,-5.24,0.62,-7.2,-5.18,0.91,-7.56,-5.09,0.93,-7.28,-5.07,0.27,-7.24,-6.38,0.05,-7.68,-6.37,-0.06,-7.48,-6.27,0.54,-7.28,-6.43,0.27,-7.24,-6.38,0.41,-7.04,-6.39,0.69,-7.24,-6.42,0.69,-7.28,-6.42,0.64,-7.28,-6.43,0.8,-7.24,-6.37,0.85,-6.92,-6.33,0.9,-7.28,-6.36,0.85,-7.36,-6.33,0.9,-7.28,-6.36,1,-7.44,-6.28,0.9,-7.28,-6.36,0.8,-7.28,-6.37,0.8,-7.24,-6.37,0.9,-7.28,-6.36,1.12,-7.32,-6.29,1,-7.44,-6.28,1.17,-7.28,-6.27,1.21,-7.12,-6.26,1.24,-7.28,-6.25,1.24,-7.28,-6.25,1.33,-7,-6.17,1.52,-7.32,-6.04,-0.01,-7.16,-5.6,0.02,-7.24,-5.57,0.06,-7.16,-5.45,-0.06,-7.2,-6.04,0.1,-7.24,-5.91,0.07,-7,-5.84,-0.06,-7.2,-6.04,-0.12,-7.12,-6.21,-0.05,-7.24,-6.3,0.27,-7.24,-6.38,-0.05,-7.24,-6.3,-0.07,-7.12,-6.28,0.85,-6.92,-6.33,1.05,-7,-6.3,1.06,-7.16,-6.31,0.64,-7.28,-6.43,0.59,-7.2,-6.43,0.69,-7.24,-6.42,1.06,-7.16,-6.31,1.17,-7.28,-6.27,1.12,-7.32,-6.29,1.53,-7.44,-6.05,1.52,-7.32,-6.04,1.62,-7.4,-5.65,1.4,-7.28,-5.29,0.93,-7.28,-5.07,1.32,-7.48,-5.24,0.02,-7.24,-5.57,0.08,-7.32,-5.5,0.06,-7.16,-5.45,-0.09,-7.36,-6.06,-0.06,-7.2,-6.04,-0.05,-7.24,-6.3,-0.05,-7.24,-6.3,0.27,-7.24,-6.38,-0.06,-7.48,-6.27,0.64,-7.28,-6.43,0.54,-7.28,-6.43,0.59,-7.2,-6.43,0.64,-7.28,-6.43,0.69,-7.28,-6.42,0.64,-7.32,-6.42,0.77,-7.32,-6.36,0.64,-7.32,-6.42,0.69,-7.28,-6.42,0.69,-7.28,-6.42,0.8,-7.28,-6.37,0.77,-7.32,-6.36,0.85,-7.36,-6.33,0.77,-7.36,-6.36,0.77,-7.32,-6.36,0.9,-7.28,-6.36,1.06,-7.16,-6.31,1.12,-7.32,-6.29,1.17,-7.28,-6.27,1.06,-7.16,-6.31,1.21,-7.12,-6.26,1.16,-7.56,-6.27,1.21,-7.32,-6.27,1.31,-7.4,-6.23,1.12,-7.32,-6.29,1.17,-7.28,-6.27,1.21,-7.32,-6.27,1.24,-7.28,-6.25,1.21,-7.32,-6.27,1.17,-7.28,-6.27,1.53,-7.44,-6.05,1.52,-7.56,-6.08,1.31,-7.4,-6.23,1.61,-7.08,-5.59,1.44,-6.96,-5.3,1.4,-7.28,-5.29,0.62,-7.2,-5.18,0.25,-7.32,-5.32,0.44,-7.68,-5.24,0.62,-7.2,-5.18,0.93,-7.28,-5.07,0.86,-7.16,-5.06,0.25,-7.32,-5.32,0.13,-6.92,-5.42,0.06,-7.16,-5.45,0.08,-7.32,-5.5,0.06,-7.32,-5.62,0.14,-7.52,-5.54,-0.06,-7.2,-6.04,0.07,-7,-5.84,-0.03,-6.84,-6.07,0.41,-7.04,-6.39,0.27,-7.24,-6.38,0.04,-6.96,-6.26,0.64,-7.32,-6.42,0.54,-7.28,-6.43,0.64,-7.28,-6.43,0.85,-7.36,-6.33,0.77,-7.32,-6.36,0.8,-7.28,-6.37,0.85,-7.36,-6.33,0.8,-7.28,-6.37,0.9,-7.28,-6.36,1.31,-7.4,-6.23,1.24,-7.28,-6.25,1.52,-7.32,-6.04,1.53,-7.44,-6.05,1.62,-7.4,-5.65,1.63,-7.72,-5.89,1.23,-7.04,-5.16,0.86,-7.16,-5.06,0.93,-7.28,-5.07,0.91,-7.56,-5.09,0.62,-7.2,-5.18,0.44,-7.68,-5.24,0.22,-7.52,-5.74,0.06,-7.32,-5.62,0.12,-7.2,-5.76,0.59,-7.4,-6.42,0.54,-7.28,-6.43,0.64,-7.32,-6.42,0.69,-7.48,-6.38,0.59,-7.4,-6.42,0.64,-7.32,-6.42,0.77,-7.36,-6.36,0.79,-7.44,-6.35,0.69,-7.48,-6.38,0.85,-7.36,-6.33,1,-7.44,-6.28,0.9,-7.44,-6.29,1.31,-7.4,-6.23,1.21,-7.32,-6.27,1.24,-7.28,-6.25,0.22,-7.52,-5.74,-0.09,-7.36,-6.06,-0.06,-7.76,-6.02,0.08,-7.32,-5.5,0.02,-7.24,-5.57,0.06,-7.32,-5.62,0.54,-7.28,-6.43,0.39,-7.56,-6.44,0.27,-7.24,-6.38,0.77,-7.36,-6.36,0.69,-7.48,-6.38,0.64,-7.32,-6.42,0.77,-7.36,-6.36,0.85,-7.36,-6.33,0.79,-7.44,-6.35,0.9,-7.44,-6.29,0.79,-7.44,-6.35,0.85,-7.36,-6.33,0.9,-7.48,-6.29,0.9,-7.44,-6.29,1,-7.44,-6.28,1.53,-7.6,-5.46,1.32,-7.48,-5.24,1.16,-7.76,-5.18,0.69,-7.48,-6.38,0.79,-7.44,-6.35,0.79,-7.48,-6.35,1.16,-7.56,-6.27,1.12,-7.32,-6.29,1.21,-7.32,-6.27,1.16,-7.56,-6.27,1,-7.44,-6.28,1.12,-7.32,-6.29,0.21,-7.64,-5.45,0.44,-7.68,-5.24,0.25,-7.32,-5.32,0.22,-7.52,-5.74,0.14,-7.52,-5.54,0.06,-7.32,-5.62,1.16,-7.68,-6.26,1.07,-7.68,-6.26,1.16,-7.56,-6.27,0.91,-7.56,-5.09,0.84,-7.72,-5.12,1.16,-7.76,-5.18,0.24,-7.68,-5.79,0.14,-7.52,-5.54,0.22,-7.52,-5.74,0.22,-7.52,-5.74,0.12,-7.2,-5.76,0.1,-7.24,-5.91,-0.06,-7.48,-6.27,-0.09,-7.36,-6.06,-0.05,-7.24,-6.3,0.96,-7.68,-6.31,0.88,-7.68,-6.31,0.92,-7.6,-6.31,0.91,-7.56,-6.31,1,-7.44,-6.28,1.02,-7.6,-6.26,0.91,-7.56,-6.31,0.9,-7.48,-6.29,1,-7.44,-6.28,1.46,-6.96,-6.11,1.58,-7.12,-5.97,1.52,-7.32,-6.04,1.52,-7.56,-6.08,1.33,-7.56,-6.2,1.31,-7.4,-6.23,1.53,-7.44,-6.05,1.31,-7.4,-6.23,1.52,-7.32,-6.04,1.53,-7.44,-6.05,1.63,-7.72,-5.89,1.52,-7.56,-6.08,1.52,-7.32,-6.04,1.58,-7.12,-5.97,1.62,-7.4,-5.65,0.22,-7.52,-5.74,0.1,-7.24,-5.91,-0.09,-7.36,-6.06,0.21,-7.64,-5.45,0.33,-7.88,-5.42,0.44,-7.68,-5.24,-0.06,-7.76,-6.02,0.04,-7.88,-5.84,0.24,-7.68,-5.79,0.54,-7.28,-6.43,0.59,-7.4,-6.42,0.39,-7.56,-6.44,0.79,-7.48,-6.35,0.9,-7.48,-6.29,0.91,-7.56,-6.31,1.16,-7.56,-6.27,1.31,-7.4,-6.23,1.33,-7.56,-6.2,1.33,-7.56,-6.2,1.52,-7.56,-6.08,1.31,-7.84,-6.24,1.35,-7.96,-5.29,1.43,-8.08,-5.38,1.58,-7.88,-5.57,1.4,-7.28,-5.29,1.32,-7.48,-5.24,1.53,-7.6,-5.46,0.33,-7.88,-5.42,0.21,-7.64,-5.45,0.24,-7.68,-5.79,-0.06,-7.48,-6.27,-0.06,-7.76,-6.02,-0.09,-7.36,-6.06,0.27,-7.24,-6.38,0.39,-7.56,-6.44,0.05,-7.68,-6.37,0.92,-7.6,-6.31,0.81,-7.64,-6.32,0.91,-7.56,-6.31,1.07,-7.68,-6.26,0.96,-7.68,-6.31,1.02,-7.6,-6.26,1.16,-7.68,-6.26,1.33,-7.56,-6.2,1.31,-7.84,-6.24,1.16,-7.68,-6.26,1.16,-7.56,-6.27,1.33,-7.56,-6.2,1.62,-7.4,-5.65,1.53,-7.6,-5.46,1.63,-7.72,-5.89,0.84,-7.72,-5.12,0.91,-7.56,-5.09,0.44,-7.68,-5.24,0.33,-7.88,-5.42,0.41,-7.88,-5.25,0.44,-7.68,-5.24,0.14,-7.52,-5.54,0.25,-7.32,-5.32,0.08,-7.32,-5.5,0.14,-7.52,-5.54,0.21,-7.64,-5.45,0.25,-7.32,-5.32,0.25,-7.84,-6.44,0.39,-7.56,-6.44,0.37,-7.88,-6.38,0.88,-7.68,-6.31,0.81,-7.64,-6.32,0.92,-7.6,-6.31,1.07,-7.68,-6.26,1.02,-7.6,-6.26,1.16,-7.56,-6.27,1,-7.44,-6.28,1.16,-7.56,-6.27,1.02,-7.6,-6.26,1.18,-7.8,-6.25,1.16,-7.68,-6.26,1.31,-7.84,-6.24,1.07,-7.72,-6.25,1.07,-7.68,-6.26,1.16,-7.68,-6.26,1.61,-7.96,-5.62,1.58,-7.88,-5.57,1.43,-8.08,-5.38,0.25,-7.84,-6.44,0.14,-7.84,-6.41,0.05,-7.68,-6.37,0.81,-7.64,-6.32,0.69,-7.48,-6.38,0.79,-7.48,-6.35,0.81,-7.64,-6.32,0.79,-7.48,-6.35,0.91,-7.56,-6.31,0.92,-7.76,-6.31,0.92,-7.8,-6.3,0.87,-7.8,-6.31,0.92,-7.76,-6.31,0.88,-7.68,-6.31,0.96,-7.68,-6.31,0.96,-7.68,-6.31,0.92,-7.6,-6.31,1.02,-7.6,-6.26,0.91,-7.56,-5.09,1.16,-7.76,-5.18,1.32,-7.48,-5.24,1.16,-7.76,-5.18,0.84,-7.72,-5.12,0.82,-8.04,-5.14,0.04,-7.88,-5.84,0.12,-8.04,-5.75,0.24,-7.68,-5.79,0.25,-7.84,-6.44,0.05,-7.68,-6.37,0.39,-7.56,-6.44,0.27,-7.24,-6.38,-0.07,-7.12,-6.28,0.04,-6.96,-6.26,0.87,-7.8,-6.31,0.79,-7.88,-6.3,0.81,-7.64,-6.32,1.03,-7.76,-6.25,0.92,-7.76,-6.31,0.96,-7.68,-6.31,1.07,-7.72,-6.25,1.03,-7.76,-6.25,0.96,-7.68,-6.31,1.53,-7.6,-5.46,1.58,-7.88,-5.57,1.63,-7.72,-5.89,0.24,-7.68,-5.79,0.22,-7.52,-5.74,-0.06,-7.76,-6.02,0.39,-7.56,-6.44,0.45,-7.84,-6.35,0.37,-7.88,-6.38,0.87,-7.8,-6.31,0.81,-7.64,-6.32,0.88,-7.68,-6.31,0.92,-7.76,-6.31,0.87,-7.8,-6.31,0.88,-7.68,-6.31,1.6,-7.8,-5.95,1.52,-7.56,-6.08,1.63,-7.72,-5.89,0.44,-7.68,-5.24,0.41,-7.88,-5.25,0.84,-7.72,-5.12,0.12,-8.04,-5.75,0.42,-8.04,-5.55,0.24,-7.68,-5.79,0.45,-7.84,-6.35,0.55,-7.96,-6.31,0.43,-7.96,-6.36,0.69,-7.48,-6.38,0.45,-7.84,-6.35,0.39,-7.56,-6.44,0.87,-7.8,-6.31,0.92,-7.8,-6.3,0.88,-7.84,-6.3,1,-7.84,-6.24,0.88,-7.84,-6.3,0.92,-7.8,-6.3,0.92,-7.8,-6.3,1.03,-7.8,-6.24,1,-7.84,-6.24,1,-7.84,-6.24,1.03,-7.8,-6.24,1.09,-7.92,-6.24,0.89,-8.04,-6.22,1,-7.88,-6.24,1.09,-7.92,-6.24,1.18,-7.8,-6.25,1.07,-7.72,-6.25,1.16,-7.68,-6.26,1.35,-7.96,-5.29,1.53,-7.6,-5.46,1.16,-7.76,-5.18,0.81,-7.64,-6.32,0.79,-7.88,-6.3,0.55,-7.96,-6.31,0.69,-7.48,-6.38,0.39,-7.56,-6.44,0.59,-7.4,-6.42,0.79,-7.88,-6.3,0.87,-7.8,-6.31,0.88,-7.84,-6.3,1,-7.88,-6.24,1,-7.84,-6.24,1.09,-7.92,-6.24,1.18,-7.8,-6.25,1.09,-7.92,-6.24,1.03,-7.8,-6.24,1.18,-7.8,-6.25,1.03,-7.76,-6.25,1.07,-7.72,-6.25,0.41,-7.88,-5.25,0.42,-8.04,-5.55,0.55,-8.08,-5.17,-0.06,-7.76,-6.02,-0.05,-7.92,-6.03,0.04,-7.88,-5.84,0.12,-8.04,-5.75,0.04,-7.88,-5.84,-0.05,-7.92,-6.03,0.15,-7.96,-6.4,0.25,-7.88,-6.44,0.3,-7.96,-6.44,0.25,-7.88,-6.44,0.37,-7.88,-6.38,0.3,-7.96,-6.44,0.81,-7.64,-6.32,0.55,-7.96,-6.31,0.45,-7.84,-6.35,0.89,-7.88,-6.28,0.79,-7.88,-6.3,0.88,-7.84,-6.3,0.89,-7.88,-6.28,1,-7.88,-6.24,0.89,-8.04,-6.22,0.89,-8.04,-6.22,1.09,-7.92,-6.24,1.12,-8.32,-6.25,1.18,-7.8,-6.25,1.03,-7.8,-6.24,1.03,-7.76,-6.25,1.09,-7.92,-6.24,1.18,-7.8,-6.25,1.31,-7.84,-6.24,1.6,-8.12,-5.99,1.37,-8.2,-6.22,1.31,-7.84,-6.24,1.61,-7.96,-5.62,1.6,-7.8,-5.95,1.63,-7.72,-5.89,1.61,-7.96,-5.62,1.43,-8.08,-5.38,1.51,-8.16,-5.47,0.41,-7.88,-5.25,0.55,-8.08,-5.17,0.84,-7.72,-5.12,0.12,-8.04,-5.75,0.19,-8.36,-5.65,0.38,-8.2,-5.6,-0.02,-7.92,-6.27,-0.04,-8.08,-6.14,-0.05,-7.92,-6.03,-0.06,-7.48,-6.27,0.05,-7.68,-6.37,-0.06,-7.76,-6.02,0.05,-7.68,-6.37,0.14,-7.84,-6.41,-0.02,-7.92,-6.27,0.14,-7.84,-6.41,0.25,-7.88,-6.44,0.15,-7.96,-6.4,0.25,-7.84,-6.44,0.25,-7.88,-6.44,0.14,-7.84,-6.41,0.37,-7.88,-6.38,0.43,-7.96,-6.36,0.3,-7.96,-6.44,0.43,-7.96,-6.36,0.37,-7.88,-6.38,0.45,-7.84,-6.35,0.69,-7.48,-6.38,0.81,-7.64,-6.32,0.45,-7.84,-6.35,0.89,-8.04,-6.22,0.79,-7.88,-6.3,0.89,-7.88,-6.28,1.6,-7.8,-5.95,1.31,-7.84,-6.24,1.52,-7.56,-6.08,0.24,-7.68,-5.79,0.21,-7.64,-5.45,0.14,-7.52,-5.54,0.77,-8.32,-6.24,0.47,-8.28,-6.37,0.58,-8.04,-6.28,1.58,-7.88,-5.57,1.61,-7.96,-5.62,1.63,-7.72,-5.89,1.13,-8.24,-5.21,1.35,-7.96,-5.29,1.16,-7.76,-5.18,1.26,-8.48,-5.29,1.13,-8.24,-5.21,0.76,-8.44,-5.13,0.42,-8.04,-5.55,0.55,-8.24,-5.21,0.55,-8.08,-5.17,-0.02,-8.36,-6.01,0.19,-8.36,-5.65,0.12,-8.04,-5.75,0.43,-7.96,-6.36,0.43,-8.04,-6.37,0.3,-7.96,-6.44,0.58,-8.04,-6.28,0.79,-7.88,-6.3,0.89,-8.04,-6.22,1.12,-8.32,-6.25,0.77,-8.32,-6.24,0.89,-8.04,-6.22,1.37,-8.2,-6.22,1.47,-8.36,-6.16,1.32,-8.32,-6.16,1.09,-7.92,-6.24,1.31,-7.84,-6.24,1.37,-8.2,-6.22,1.49,-8.2,-5.45,1.43,-8.08,-5.38,1.4,-8.24,-5.37,1.35,-7.96,-5.29,1.58,-7.88,-5.57,1.53,-7.6,-5.46,1.43,-8.08,-5.38,1.13,-8.24,-5.21,1.4,-8.24,-5.37,1.13,-8.24,-5.21,1.26,-8.48,-5.29,1.4,-8.24,-5.37,0.4,-8.4,-5.54,0.56,-8.44,-5.39,0.55,-8.24,-5.21,0.41,-7.88,-5.25,0.33,-7.88,-5.42,0.42,-8.04,-5.55,-0.02,-8.36,-6.01,0.12,-8.04,-5.75,-0.04,-8.08,-6.14,-0.02,-8.36,-6.01,-0.04,-8.08,-6.14,0.1,-8.2,-6.37,-0.02,-7.92,-6.27,-0.05,-7.92,-6.03,-0.06,-7.76,-6.02,0.47,-8.28,-6.37,0.77,-8.32,-6.24,0.69,-8.4,-6.23,1.09,-7.92,-6.24,1.37,-8.2,-6.22,1.12,-8.32,-6.25,1.6,-7.8,-5.95,1.61,-7.96,-5.62,1.6,-8.12,-5.99,1.51,-8.16,-5.47,1.58,-8.2,-5.57,1.61,-7.96,-5.62,0.4,-8.4,-5.54,0.38,-8.2,-5.6,0.19,-8.36,-5.65,-0.02,-7.92,-6.27,0.15,-7.96,-6.4,0.1,-8.2,-6.37,-0.04,-8.08,-6.14,-0.02,-7.92,-6.27,0.1,-8.2,-6.37,1.61,-7.96,-5.62,1.65,-8.24,-5.75,1.6,-8.12,-5.99,1.43,-8.08,-5.38,1.35,-7.96,-5.29,1.13,-8.24,-5.21,0.38,-8.2,-5.6,0.4,-8.4,-5.54,0.55,-8.24,-5.21,0.12,-8.04,-5.75,0.38,-8.2,-5.6,0.42,-8.04,-5.55,0.77,-8.32,-6.24,0.58,-8.04,-6.28,0.89,-8.04,-6.22,0.58,-8.04,-6.28,0.55,-7.96,-6.31,0.79,-7.88,-6.3,1.49,-8.2,-5.45,1.51,-8.16,-5.47,1.43,-8.08,-5.38,0.42,-8.04,-5.55,0.38,-8.2,-5.6,0.55,-8.24,-5.21,0.05,-7.68,-6.37,-0.02,-7.92,-6.27,-0.06,-7.76,-6.02,1.51,-8.16,-5.47,1.51,-8.2,-5.47,1.58,-8.2,-5.57,1.49,-8.2,-5.45,1.51,-8.2,-5.47,1.51,-8.16,-5.47,1.4,-8.24,-5.37,1.49,-8.24,-5.45,1.49,-8.2,-5.45,1.55,-8.4,-5.52,1.49,-8.24,-5.45,1.4,-8.24,-5.37,0.82,-8.04,-5.14,0.55,-8.08,-5.17,0.55,-8.24,-5.21,1.58,-8.2,-5.57,1.65,-8.24,-5.75,1.61,-7.96,-5.62,1.57,-8.28,-5.54,1.49,-8.24,-5.45,1.55,-8.4,-5.52,1.51,-8.2,-5.47,1.49,-8.2,-5.45,1.49,-8.24,-5.45,1.26,-8.48,-5.29,1.15,-8.64,-5.27,1.22,-8.68,-5.32,0.55,-8.08,-5.17,0.82,-8.04,-5.14,0.84,-7.72,-5.12,0.4,-8.4,-5.54,0.19,-8.36,-5.65,0.32,-8.56,-5.52,0.14,-7.84,-6.41,0.15,-7.96,-6.4,-0.02,-7.92,-6.27,1.51,-8.2,-5.47,1.49,-8.24,-5.45,1.57,-8.28,-5.54,0.61,-8.32,-5.17,0.76,-8.44,-5.13,0.82,-8.04,-5.14,0.47,-8.28,-6.37,0.43,-8.04,-6.37,0.58,-8.04,-6.28,0.88,-8.6,-6.26,0.69,-8.4,-6.23,0.77,-8.32,-6.24,1.24,-8.52,-6.26,1.61,-8.68,-6.03,1.57,-8.8,-6.11,1.51,-8.2,-5.47,1.57,-8.28,-5.54,1.58,-8.2,-5.57,1.55,-8.4,-5.52,1.63,-8.8,-5.61,1.64,-8.72,-5.78,1.55,-8.4,-5.52,1.4,-8.24,-5.37,1.26,-8.48,-5.29,1.13,-8.24,-5.21,1.16,-7.76,-5.18,0.82,-8.04,-5.14,1.15,-8.64,-5.27,1.26,-8.48,-5.29,0.76,-8.44,-5.13,0.61,-8.32,-5.17,0.82,-8.04,-5.14,0.55,-8.24,-5.21,0.19,-8.36,-5.65,0.05,-8.76,-5.88,0.26,-8.76,-5.62,-0.01,-8.6,-6.02,0.05,-8.76,-5.88,0.19,-8.36,-5.65,-0.02,-8.36,-6.01,-0.01,-8.6,-6.02,0.19,-8.36,-5.65,1.23,-8.68,-6.29,1.24,-8.52,-6.26,1.57,-8.8,-6.11,1.57,-8.28,-5.54,1.65,-8.24,-5.75,1.58,-8.2,-5.57,0.98,-8.68,-5.14,0.76,-8.44,-5.13,0.76,-8.68,-5.2,0.04,-8.68,-6.26,0.4,-8.56,-6.43,0.44,-8.68,-6.43,0.47,-8.28,-6.37,0.4,-8.56,-6.43,0.1,-8.2,-6.37,1.6,-8.12,-5.99,1.47,-8.36,-6.16,1.37,-8.2,-6.22,1.6,-7.8,-5.95,1.6,-8.12,-5.99,1.31,-7.84,-6.24,0.56,-8.44,-5.39,0.69,-8.64,-5.23,0.61,-8.32,-5.17,0.56,-8.44,-5.39,0.61,-8.32,-5.17,0.55,-8.24,-5.21,0.1,-8.2,-6.37,0.15,-7.96,-6.4,0.3,-7.96,-6.44,1.24,-8.52,-6.26,1.47,-8.36,-6.16,1.61,-8.68,-6.03,1.32,-8.32,-6.16,1.12,-8.32,-6.25,1.37,-8.2,-6.22,1.47,-8.36,-6.16,1.65,-8.24,-5.75,1.65,-8.6,-5.95,1.47,-8.36,-6.16,1.65,-8.6,-5.95,1.61,-8.68,-6.03,0.04,-8.68,-6.26,0.44,-8.68,-6.43,0.24,-8.92,-6.37,0.47,-8.28,-6.37,0.1,-8.2,-6.37,0.43,-8.04,-6.37,1.57,-8.28,-5.54,1.55,-8.4,-5.52,1.65,-8.24,-5.75,0.69,-8.64,-5.23,0.76,-8.44,-5.13,0.61,-8.32,-5.17,0.42,-8.04,-5.55,0.33,-7.88,-5.42,0.24,-7.68,-5.79,0.12,-8.04,-5.75,-0.05,-7.92,-6.03,-0.04,-8.08,-6.14,0.09,-8.52,-6.34,-0.02,-8.36,-6.01,0.1,-8.2,-6.37,0.4,-8.56,-6.43,0.09,-8.52,-6.34,0.1,-8.2,-6.37,0.4,-8.56,-6.43,0.53,-8.56,-6.36,0.53,-8.64,-6.36,1.23,-8.68,-6.29,1.57,-8.8,-6.11,1.44,-8.92,-6.21,0.32,-8.56,-5.52,0.19,-8.36,-5.65,0.26,-8.76,-5.62,0.77,-8.6,-6.32,0.66,-8.56,-6.29,0.69,-8.4,-6.23,1.15,-8.64,-5.27,0.98,-8.68,-5.14,1.07,-8.72,-5.17,1.55,-8.4,-5.52,1.55,-8.88,-5.48,1.63,-8.8,-5.61,0.76,-8.44,-5.13,0.69,-8.64,-5.23,0.76,-8.68,-5.2,0.66,-8.56,-6.29,0.53,-8.56,-6.36,0.47,-8.28,-6.37,0.56,-8.68,-6.36,0.6,-8.84,-6.38,0.54,-8.84,-6.39,0.88,-8.6,-6.26,0.77,-8.32,-6.24,1.12,-8.32,-6.25,0.88,-8.6,-6.26,0.77,-8.6,-6.32,0.69,-8.4,-6.23,1.23,-8.68,-6.29,1.2,-8.8,-6.35,1,-8.76,-6.34,1.24,-8.52,-6.26,1.12,-8.32,-6.25,1.32,-8.32,-6.16,1.24,-8.52,-6.26,1.32,-8.32,-6.16,1.47,-8.36,-6.16,0.4,-8.4,-5.54,0.32,-8.56,-5.52,0.56,-8.44,-5.39,0.09,-8.52,-6.34,0.04,-8.68,-6.26,-0.01,-8.6,-6.02,0.04,-8.68,-6.26,0.09,-8.52,-6.34,0.4,-8.56,-6.43,0.4,-8.56,-6.43,0.53,-8.64,-6.36,0.44,-8.68,-6.43,0.66,-8.56,-6.29,0.77,-8.6,-6.32,0.76,-8.64,-6.32,1.23,-8.68,-6.29,1.44,-8.92,-6.21,1.39,-8.96,-6.28,1.64,-8.72,-5.78,1.63,-8.8,-5.61,1.57,-8.92,-5.66,0.98,-8.68,-5.14,0.76,-8.68,-5.2,0.8,-8.76,-5.19,0.72,-8.8,-5.29,0.78,-8.76,-5.22,0.76,-8.68,-5.2,0.72,-8.8,-5.29,0.69,-8.64,-5.23,0.66,-8.84,-5.36,0.1,-8.2,-6.37,0.3,-7.96,-6.44,0.43,-8.04,-6.37,0.66,-8.56,-6.29,0.47,-8.28,-6.37,0.69,-8.4,-6.23,0.56,-8.68,-6.36,0.44,-8.68,-6.43,0.53,-8.64,-6.36,0.47,-8.28,-6.37,0.53,-8.56,-6.36,0.4,-8.56,-6.43,0.53,-8.64,-6.36,0.63,-8.64,-6.32,0.56,-8.68,-6.36,0.87,-8.64,-6.27,0.88,-8.6,-6.26,0.97,-8.68,-6.27,1.61,-8.68,-6.03,1.65,-8.6,-5.95,1.64,-8.72,-5.78,1.22,-8.68,-5.32,1.15,-8.64,-5.27,1.19,-8.72,-5.27,1.55,-8.4,-5.52,1.34,-8.84,-5.3,1.55,-8.88,-5.48,0.98,-8.68,-5.14,0.99,-8.76,-5.15,1.07,-8.72,-5.17,0.8,-8.76,-5.19,0.99,-8.76,-5.15,0.98,-8.68,-5.14,0.72,-8.8,-5.29,0.76,-8.68,-5.2,0.69,-8.64,-5.23,0.63,-8.64,-6.32,0.76,-8.64,-6.32,0.6,-8.84,-6.38,0.66,-8.56,-6.29,0.76,-8.64,-6.32,0.63,-8.64,-6.32,1.24,-8.52,-6.26,0.97,-8.68,-6.27,1.12,-8.32,-6.25,1.47,-8.36,-6.16,1.6,-8.12,-5.99,1.65,-8.24,-5.75,1.55,-8.4,-5.52,1.65,-8.6,-5.95,1.65,-8.24,-5.75,1.1,-8.8,-5.19,1.2,-8.8,-5.22,1.19,-8.72,-5.27,0.99,-8.76,-5.15,0.8,-8.76,-5.19,0.84,-8.84,-5.19,1.13,-8.24,-5.21,0.82,-8.04,-5.14,0.76,-8.44,-5.13,0.78,-8.76,-5.22,0.8,-8.76,-5.19,0.76,-8.68,-5.2,0.32,-8.56,-5.52,0.66,-8.84,-5.36,0.56,-8.44,-5.39,0.09,-8.52,-6.34,-0.01,-8.6,-6.02,-0.02,-8.36,-6.01,0.56,-8.68,-6.36,0.63,-8.64,-6.32,0.6,-8.84,-6.38,0.87,-8.64,-6.27,0.88,-8.8,-6.42,0.76,-8.64,-6.32,0.87,-8.64,-6.27,0.97,-8.68,-6.27,0.88,-8.8,-6.42,1.2,-8.8,-6.35,1.07,-8.84,-6.37,1,-8.76,-6.34,1.23,-8.68,-6.29,1,-8.76,-6.34,0.97,-8.68,-6.27,1.2,-8.8,-6.35,1.23,-8.68,-6.29,1.39,-8.96,-6.28,1.57,-8.8,-6.11,1.64,-8.72,-5.78,1.56,-9,-6.12,1.57,-8.8,-6.11,1.61,-8.68,-6.03,1.64,-8.72,-5.78,1.15,-8.64,-5.27,0.76,-8.44,-5.13,0.98,-8.68,-5.14,0.8,-8.76,-5.19,0.78,-8.76,-5.22,0.78,-8.8,-5.22,0.78,-8.8,-5.22,0.78,-8.76,-5.22,0.72,-8.8,-5.29,0.83,-8.92,-5.22,0.78,-8.8,-5.22,0.72,-8.8,-5.29,0,-8.96,-6.11,0.03,-8.96,-5.96,0.05,-8.76,-5.88,0.88,-8.8,-6.42,0.69,-9,-6.46,0.6,-8.84,-6.38,0.97,-8.68,-6.27,1,-8.76,-6.34,0.88,-8.8,-6.42,1.22,-8.68,-5.32,1.19,-8.72,-5.27,1.23,-8.8,-5.24,1.2,-8.8,-5.22,1.23,-8.8,-5.24,1.19,-8.72,-5.27,1.1,-8.8,-5.19,1.19,-8.72,-5.27,1.07,-8.72,-5.17,1.19,-8.72,-5.27,1.15,-8.64,-5.27,1.07,-8.72,-5.17,1.08,-8.8,-5.17,1.1,-8.8,-5.19,1.07,-8.72,-5.17,1.1,-8.8,-5.19,1.08,-8.8,-5.17,1.02,-8.84,-5.17,1.02,-8.84,-5.17,1.08,-8.8,-5.17,0.99,-8.76,-5.15,0.8,-8.76,-5.19,0.78,-8.8,-5.22,0.84,-8.84,-5.19,0.24,-8.92,-6.37,0.05,-8.88,-6.26,0.04,-8.68,-6.26,1.24,-8.52,-6.26,1.23,-8.68,-6.29,0.97,-8.68,-6.27,1.21,-8.88,-6.38,1.2,-8.8,-6.35,1.39,-8.96,-6.28,1.55,-8.4,-5.52,1.64,-8.72,-5.78,1.65,-8.6,-5.95,1.22,-8.68,-5.32,1.23,-8.8,-5.24,1.34,-8.84,-5.3,1.55,-8.4,-5.52,1.22,-8.68,-5.32,1.34,-8.84,-5.3,1.23,-8.8,-5.24,1.2,-8.8,-5.22,1.2,-8.84,-5.22,1.02,-8.84,-5.17,1.08,-8.96,-5.21,1.13,-8.88,-5.21,0.05,-8.88,-6.26,0,-8.96,-6.11,-0.01,-8.6,-6.02,0.05,-8.88,-6.26,-0.01,-8.6,-6.02,0.04,-8.68,-6.26,0.45,-8.84,-6.43,0.54,-8.84,-6.39,0.53,-8.88,-6.4,0.54,-8.84,-6.39,0.6,-8.84,-6.38,0.53,-8.88,-6.4,0.6,-8.84,-6.38,0.69,-9,-6.46,0.53,-8.88,-6.4,0.88,-8.8,-6.42,0.81,-9,-6.48,0.69,-9,-6.46,0.81,-9,-6.48,0.88,-8.8,-6.42,0.94,-8.84,-6.45,0.88,-8.8,-6.42,0.6,-8.84,-6.38,0.76,-8.64,-6.32,0.94,-8.84,-6.45,1.07,-8.84,-6.37,0.99,-8.88,-6.43,1.1,-8.88,-6.39,0.99,-8.88,-6.43,1.07,-8.84,-6.37,1.21,-8.88,-6.38,1.21,-8.96,-6.41,1.15,-8.92,-6.39,0.97,-8.68,-6.27,0.88,-8.6,-6.26,1.12,-8.32,-6.25,0.84,-8.84,-5.19,1.02,-8.84,-5.17,0.99,-8.76,-5.15,0.53,-8.88,-6.4,0.48,-9,-6.44,0.45,-8.84,-6.43,0.94,-8.84,-6.45,0.99,-8.88,-6.43,0.93,-9,-6.5,1.21,-8.88,-6.38,1.15,-8.92,-6.39,1.1,-8.88,-6.39,1.2,-8.8,-6.35,1.1,-8.88,-6.39,1.07,-8.84,-6.37,1.2,-8.8,-6.35,1.21,-8.88,-6.38,1.1,-8.88,-6.39,1.57,-8.92,-5.66,1.63,-8.8,-5.61,1.55,-8.88,-5.48,1.23,-8.8,-5.24,1.2,-8.84,-5.22,1.34,-8.84,-5.3,1.34,-8.84,-5.3,1.51,-9,-5.4,1.55,-8.88,-5.48,1.55,-8.4,-5.52,1.26,-8.48,-5.29,1.22,-8.68,-5.32,1.08,-8.96,-5.21,1.02,-8.84,-5.17,0.83,-8.92,-5.22,0.72,-8.8,-5.29,0.66,-8.84,-5.36,0.83,-8.92,-5.22,0,-8.96,-6.11,0.05,-8.76,-5.88,-0.01,-8.6,-6.02,0.05,-8.76,-5.88,0.08,-9.08,-5.8,0.16,-9.04,-5.74,0.01,-9,-6.14,0,-8.96,-6.11,0.05,-8.88,-6.26,1.2,-8.84,-5.22,1.24,-9.04,-5.26,1.34,-8.84,-5.3,0.66,-8.84,-5.36,0.69,-8.64,-5.23,0.56,-8.44,-5.39,0.05,-8.76,-5.88,0.03,-8.96,-5.96,0.08,-9.08,-5.8,0.05,-8.76,-5.88,0.16,-9.04,-5.74,0.26,-8.76,-5.62,0.44,-8.68,-6.43,0.45,-8.84,-6.43,0.24,-8.92,-6.37,0.83,-8.92,-5.22,0.84,-8.84,-5.19,0.78,-8.8,-5.22,0.32,-9.08,-5.59,0.5,-9.08,-5.42,0.26,-8.76,-5.62,0.16,-9.04,-5.74,0.22,-9.08,-5.67,0.26,-8.76,-5.62,0.15,-9.08,-6.28,0.05,-8.88,-6.26,0.24,-8.92,-6.37,0.48,-9,-6.44,0.24,-8.92,-6.37,0.45,-8.84,-6.43,1.56,-9,-6.12,1.44,-8.92,-6.21,1.57,-8.8,-6.11,0.66,-8.84,-5.36,0.32,-8.56,-5.52,0.26,-8.76,-5.62,0.84,-8.84,-5.19,0.83,-8.92,-5.22,1.02,-8.84,-5.17,0.22,-9.08,-5.67,0.32,-9.08,-5.59,0.26,-8.76,-5.62,0.5,-9.08,-5.42,0.66,-8.84,-5.36,0.26,-8.76,-5.62,-0.5,-6.12,-5.82,-0.51,-6.08,-5.82,-0.51,-6.08,-5.86,-0.49,-6.12,-5.86])

IndexedFaceSet379.setCoord(Coordinate380)

Shape375.setGeometry(IndexedFaceSet379)

Transform374.addChildren(Shape375)

fieldValue373.addChildren(Transform374)

ProtoInstance371.addFieldValue(fieldValue373)

fieldValue370.addChildren(ProtoInstance371)
ProtoInstance381 = ProtoInstance()
ProtoInstance381.setName("Joint")
ProtoInstance381.setDEF("Allen_hanim_r_ankle")
fieldValue382 = fieldValue()
fieldValue382.setName("name")
fieldValue382.setValue("r_ankle")

ProtoInstance381.addFieldValue(fieldValue382)
fieldValue383 = fieldValue()
fieldValue383.setName("center")
fieldValue383.setValue("-0.064 0.0753 -0.0412")

ProtoInstance381.addFieldValue(fieldValue383)
fieldValue384 = fieldValue()
fieldValue384.setName("children")
ProtoInstance385 = ProtoInstance()
ProtoInstance385.setName("Segment")
ProtoInstance385.setDEF("Allen_hanim_r_hindfoot")
fieldValue386 = fieldValue()
fieldValue386.setName("name")
fieldValue386.setValue("r_hindfoot")

ProtoInstance385.addFieldValue(fieldValue386)
fieldValue387 = fieldValue()
fieldValue387.setName("children")
Transform388 = Transform()
Transform388.setDEF("r_foot_adjust")
Transform388.setCenter([0.3319,1.1,-0.04])
Transform388.setRotation([0,1,0,1.570796])
Transform388.setScale([0.1,0.1,0.1])
Shape389 = Shape()
Appearance390 = Appearance()
Material391 = Material()
Material391.setUSE("Shoe_Color")

Appearance390.setMaterial(Material391)

Shape389.setAppearance(Appearance390)
IndexedFaceSet392 = IndexedFaceSet()
IndexedFaceSet392.setCoordIndex([0,1,2,-1,3,4,5,-1,6,7,8,-1,9,10,11,-1,12,13,14,-1,15,16,17,-1,18,19,20,-1,21,22,23,-1,24,25,26,-1,27,28,29,-1,30,31,32,-1,33,34,35,-1,36,37,38,-1,39,40,41,-1,42,43,44,-1,45,46,47,-1,48,49,50,-1,51,52,53,-1,54,55,56,-1,57,58,59,-1,60,61,62,-1,63,64,65,-1,66,67,68,-1,69,70,71,-1,72,73,74,-1,75,76,77,-1,78,79,80,-1,81,82,83,-1,84,85,86,-1,87,88,89,-1,90,91,92,-1,93,94,95,-1,96,97,98,-1,99,100,101,-1,102,103,104,-1,105,106,107,-1,108,109,110,-1,111,112,113,-1,114,115,116,-1,117,118,119,-1,120,121,122,-1,123,124,125,-1,126,127,128,-1,129,130,131,-1,132,133,134,-1,135,136,137,-1,138,139,140,-1,141,142,143,-1,144,145,146,-1,147,148,149,-1,150,151,152,-1,153,154,155,-1,156,157,158,-1,159,160,161,-1,162,163,164,-1,165,166,167,-1,168,169,170,-1,171,172,173,-1,174,175,176,-1,177,178,179,-1,180,181,182,-1,183,184,185,-1,186,187,188,-1,189,190,191,-1,192,193,194,-1,195,196,197,-1,198,199,200,-1,201,202,203,-1,204,205,206,-1,207,208,209,-1,210,211,212,-1,213,214,215,-1,216,217,218,-1,219,220,221,-1,222,223,224,-1,225,226,227,-1,228,229,230,-1,231,232,233,-1,234,235,236,-1,237,238,239,-1,240,241,242,-1,243,244,245,-1,246,247,248,-1,249,250,251,-1,252,253,254,-1,255,256,257,-1,258,259,260,-1,261,262,263,-1,264,265,266,-1,267,268,269,-1,270,271,272,-1,273,274,275,-1,276,277,278,-1,279,280,281,-1,282,283,284,-1,285,286,287,-1,288,289,290,-1,291,292,293,-1,294,295,296,-1,297,298,299,-1,300,301,302,-1,303,304,305,-1,306,307,308,-1,309,310,311,-1,312,313,314,-1,315,316,317,-1,318,319,320,-1,321,322,323,-1,324,325,326,-1,327,328,329,-1,330,331,332,-1,333,334,335,-1,336,337,338,-1,339,340,341,-1,342,343,344,-1,345,346,347,-1,348,349,350,-1,351,352,353,-1,354,355,356,-1,357,358,359,-1,360,361,362,-1,363,364,365,-1,366,367,368,-1,369,370,371,-1,372,373,374,-1,375,376,377,-1,378,379,380,-1,381,382,383,-1,384,385,386,-1,387,388,389,-1,390,391,392,-1,393,394,395,-1,396,397,398,-1,399,400,401,-1,402,403,404,-1,405,406,407,-1,408,409,410,-1,411,412,413,-1,414,415,416,-1,417,418,419,-1,420,421,422,-1,423,424,425,-1,426,427,428,-1,429,430,431,-1,432,433,434,-1,435,436,437,-1,438,439,440,-1,441,442,443,-1,444,445,446,-1,447,448,449,-1,450,451,452,-1,453,454,455,-1,456,457,458,-1,459,460,461,-1,462,463,464,-1,465,466,467,-1,468,469,470,-1,471,472,473,-1,474,475,476,-1,477,478,479,-1,480,481,482,-1,483,484,485,-1,486,487,488,-1,489,490,491,-1,492,493,494,-1,495,496,497,-1,498,499,500,-1,501,502,503,-1,504,505,506,-1,507,508,509,-1,510,511,512,-1,513,514,515,-1,516,517,518,-1,519,520,521,-1,522,523,524,-1,525,526,527,-1,528,529,530,-1,531,532,533,-1,534,535,536,-1,537,538,539,-1,540,541,542,-1,543,544,545,-1,546,547,548,-1,549,550,551,-1,552,553,554,-1,555,556,557,-1,558,559,560,-1,561,562,563,-1,564,565,566,-1,567,568,569,-1,570,571,572,-1,573,574,575,-1,576,577,578,-1,579,580,581,-1,582,583,584,-1,585,586,587,-1,588,589,590,-1,591,592,593,-1,594,595,596,-1,597,598,599,-1,600,601,602,-1,603,604,605,-1,606,607,608,-1,609,610,611,-1,612,613,614,-1,615,616,617,-1,618,619,620,-1,621,622,623,-1,624,625,626,-1,627,628,629,-1,630,631,632,-1,633,634,635,-1,636,637,638,-1,639,640,641,-1,642,643,644,-1,645,646,647,-1,648,649,650,-1,651,652,653,-1,654,655,656,-1,657,658,659,-1,660,661,662,-1,663,664,665,-1,666,667,668,-1,669,670,671,-1,672,673,674,-1,675,676,677,-1,678,679,680,-1,681,682,683,-1,684,685,686,-1,687,688,689,-1,690,691,692,-1,693,694,695,-1,696,697,698,-1,699,700,701,-1,702,703,704,-1,705,706,707,-1,708,709,710,-1,711,712,713,-1,714,715,716,-1,717,718,719,-1,720,721,722,-1,723,724,725,-1,726,727,728,-1,729,730,731,-1,732,733,734,-1,735,736,737,-1,738,739,740,-1,741,742,743,-1,744,745,746,-1,747,748,749,-1,750,751,752,-1,753,754,755,-1,756,757,758,-1,759,760,761,-1,762,763,764,-1,765,766,767,-1,768,769,770,-1,771,772,773,-1,774,775,776,-1,777,778,779,-1,780,781,782,-1,783,784,785,-1,786,787,788,-1,789,790,791,-1,792,793,794,-1,795,796,797,-1,798,799,800,-1,801,802,803,-1,804,805,806,-1,807,808,809,-1,810,811,812,-1,813,814,815,-1,816,817,818,-1,819,820,821,-1,822,823,824,-1,825,826,827,-1,828,829,830,-1,831,832,833,-1,834,835,836,-1,837,838,839,-1,840,841,842,-1,843,844,845,-1,846,847,848,-1,849,850,851,-1,852,853,854,-1,855,856,857,-1,858,859,860,-1,861,862,863,-1,864,865,866,-1,867,868,869,-1,870,871,872,-1,873,874,875,-1,876,877,878,-1,879,880,881,-1,882,883,884,-1,885,886,887,-1,888,889,890,-1,891,892,893,-1,894,895,896,-1,897,898,899,-1,900,901,902,-1,903,904,905,-1,906,907,908,-1,909,910,911,-1,912,913,914,-1,915,916,917,-1,918,919,920,-1,921,922,923,-1,924,925,926,-1,927,928,929,-1,930,931,932,-1,933,934,935,-1,936,937,938,-1,939,940,941,-1,942,943,944,-1,945,946,947,-1,948,949,950,-1,951,952,953,-1,954,955,956,-1,957,958,959,-1,960,961,962,-1,963,964,965,-1,966,967,968,-1,969,970,971,-1,972,973,974,-1,975,976,977,-1,978,979,980,-1,981,982,983,-1,984,985,986,-1,987,988,989,-1,990,991,992,-1,993,994,995,-1,996,997,998,-1,999,1000,1001,-1,1002,1003,1004,-1,1005,1006,1007,-1,1008,1009,1010,-1,1011,1012,1013,-1,1014,1015,1016,-1,1017,1018,1019,-1,1020,1021,1022,-1,1023,1024,1025,-1,1026,1027,1028,-1,1029,1030,1031,-1,1032,1033,1034,-1,1035,1036,1037,-1,1038,1039,1040,-1,1041,1042,1043,-1,1044,1045,1046,-1,1047,1048,1049,-1,1050,1051,1052,-1,1053,1054,1055,-1,1056,1057,1058,-1,1059,1060,1061,-1,1062,1063,1064,-1,1065,1066,1067,-1,1068,1069,1070,-1,1071,1072,1073,-1,1074,1075,1076,-1,1077,1078,1079,-1,1080,1081,1082,-1,1083,1084,1085,-1,1086,1087,1088,-1,1089,1090,1091,-1,1092,1093,1094,-1,1095,1096,1097,-1,1098,1099,1100,-1,1101,1102,1103,-1,1104,1105,1106,-1,1107,1108,1109,-1,1110,1111,1112,-1,1113,1114,1115,-1,1116,1117,1118,-1,1119,1120,1121,-1,1122,1123,1124,-1,1125,1126,1127,-1,1128,1129,1130,-1,1131,1132,1133,-1,1134,1135,1136,-1,1137,1138,1139,-1,1140,1141,1142,-1,1143,1144,1145,-1,1146,1147,1148,-1,1149,1150,1151,-1,1152,1153,1154,-1,1155,1156,1157,-1,1158,1159,1160,-1,1161,1162,1163,-1,1164,1165,1166,-1,1167,1168,1169,-1,1170,1171,1172,-1,1173,1174,1175,-1,1176,1177,1178,-1,1179,1180,1181,-1,1182,1183,1184,-1,1185,1186,1187,-1,1188,1189,1190,-1,1191,1192,1193,-1,1194,1195,1196,-1,1197,1198,1199,-1,1200,1201,1202,-1,1203,1204,1205,-1,1206,1207,1208,-1,1209,1210,1211,-1,1212,1213,1214,-1,1215,1216,1217,-1,1218,1219,1220,-1,1221,1222,1223,-1,1224,1225,1226,-1,1227,1228,1229,-1,1230,1231,1232,-1,1233,1234,1235,-1,1236,1237,1238,-1,1239,1240,1241,-1,1242,1243,1244,-1,1245,1246,1247,-1,1248,1249,1250,-1,1251,1252,1253,-1,1254,1255,1256,-1,1257,1258,1259,-1,1260,1261,1262,-1,1263,1264,1265,-1,1266,1267,1268,-1,1269,1270,1271,-1,1272,1273,1274,-1,1275,1276,1277,-1,1278,1279,1280,-1,1281,1282,1283,-1,1284,1285,1286,-1,1287,1288,1289,-1,1290,1291,1292,-1,1293,1294,1295,-1,1296,1297,1298,-1,1299,1300,1301,-1,1302,1303,1304,-1,1305,1306,1307,-1,1308,1309,1310,-1,1311,1312,1313,-1,1314,1315,1316,-1,1317,1318,1319,-1,1320,1321,1322,-1,1323,1324,1325,-1,1326,1327,1328,-1,1329,1330,1331,-1,1332,1333,1334,-1,1335,1336,1337,-1,1338,1339,1340,-1,1341,1342,1343,-1,1344,1345,1346,-1,1347,1348,1349,-1,1350,1351,1352,-1,1353,1354,1355,-1,1356,1357,1358,-1,1359,1360,1361,-1,1362,1363,1364,-1,1365,1366,1367,-1,1368,1369,1370,-1,1371,1372,1373,-1,1374,1375,1376,-1,1377,1378,1379,-1,1380,1381,1382,-1,1383,1384,1385,-1,1386,1387,1388,-1,1389,1390,1391,-1,1392,1393,1394,-1,1395,1396,1397,-1,1398,1399,1400,-1,1401,1402,1403,-1,1404,1405,1406,-1,1407,1408,1409,-1,1410,1411,1412,-1,1413,1414,1415,-1,1416,1417,1418,-1,1419,1420,1421,-1,1422,1423,1424,-1,1425,1426,1427,-1,1428,1429,1430,-1,1431,1432,1433,-1,1434,1435,1436,-1,1437,1438,1439,-1,1440,1441,1442,-1,1443,1444,1445,-1,1446,1447,1448,-1,1449,1450,1451,-1,1452,1453,1454,-1,1455,1456,1457,-1,1458,1459,1460,-1,1461,1462,1463,-1,1464,1465,1466,-1,1467,1468,1469,-1,1470,1471,1472,-1,1473,1474,1475,-1,1476,1477,1478,-1,1479,1480,1481,-1,1482,1483,1484,-1,1485,1486,1487,-1,1488,1489,1490,-1,1491,1492,1493,-1,1494,1495,1496,-1,1497,1498,1499,-1,1500,1501,1502,-1,1503,1504,1505,-1,1506,1507,1508,-1,1509,1510,1511,-1,1512,1513,1514,-1,1515,1516,1517,-1,1518,1519,1520,-1,1521,1522,1523,-1,1524,1525,1526,-1,1527,1528,1529,-1,1530,1531,1532,-1,1533,1534,1535,-1,1536,1537,1538,-1,1539,1540,1541,-1,1542,1543,1544,-1,1545,1546,1547,-1,1548,1549,1550,-1,1551,1552,1553,-1,1554,1555,1556,-1,1557,1558,1559,-1,1560,1561,1562,-1,1563,1564,1565,-1,1566,1567,1568,-1,1569,1570,1571,-1,1572,1573,1574,-1,1575,1576,1577,-1,1578,1579,1580,-1,1581,1582,1583,-1,1584,1585,1586,-1,1587,1588,1589,-1,1590,1591,1592,-1,1593,1594,1595,-1,1596,1597,1598,-1,1599,1600,1601,-1,1602,1603,1604,-1,1605,1606,1607,-1,1608,1609,1610,-1,1611,1612,1613,-1,1614,1615,1616,-1,1617,1618,1619,-1,1620,1621,1622,-1,1623,1624,1625,-1,1626,1627,1628,-1,1629,1630,1631,-1,1632,1633,1634,-1,1635,1636,1637,-1,1638,1639,1640,-1,1641,1642,1643,-1,1644,1645,1646,-1,1647,1648,1649,-1,1650,1651,1652,-1,1653,1654,1655,-1,1656,1657,1658,-1,1659,1660,1661,-1,1662,1663,1664,-1,1665,1666,1667,-1,1668,1669,1670,-1,1671,1672,1673,-1,1674,1675,1676,-1,1677,1678,1679,-1,1680,1681,1682,-1,1683,1684,1685,-1,1686,1687,1688,-1,1689,1690,1691,-1,1692,1693,1694,-1,1695,1696,1697,-1,1698,1699,1700,-1,1701,1702,1703,-1,1704,1705,1706,-1,1707,1708,1709,-1,1710,1711,1712,-1])
IndexedFaceSet392.setCreaseAngle(1.57)
Coordinate393 = Coordinate()
Coordinate393.setPoint([0.5,-9.08,-4.43,0.8,-9.12,-4.28,0.66,-8.84,-4.37,0.8,-9.12,-4.28,1.01,-9.24,-4.28,1.05,-9.08,-4.24,1.57,-8.92,-4.67,1.55,-8.88,-4.49,1.56,-8.96,-4.52,0.52,-9.08,-5.42,0.69,-9,-5.47,0.76,-9.08,-5.45,1.39,-8.96,-5.29,1.25,-8.96,-5.41,1.21,-8.88,-5.38,1.34,-8.84,-4.31,1.48,-9.04,-4.35,1.51,-9,-4.41,0.81,-9,-5.49,0.94,-8.84,-5.46,0.93,-9,-5.5,1.25,-8.96,-5.41,1.24,-8.96,-5.44,1.21,-8.96,-5.42,1.57,-8.92,-4.67,1.54,-9.2,-4.73,1.48,-9.08,-4.97,1.54,-8.96,-4.5,1.56,-8.96,-4.52,1.55,-8.88,-4.49,1.51,-9,-4.41,1.54,-8.96,-4.5,1.55,-8.88,-4.49,1.24,-9.04,-4.27,1.2,-8.84,-4.23,1.13,-8.88,-4.22,1.01,-9,-5.51,0.93,-9,-5.5,1.02,-8.92,-5.47,1.21,-8.88,-5.38,1.25,-8.96,-5.41,1.21,-8.96,-5.42,1.44,-8.92,-5.21,1.47,-9,-5.27,1.39,-8.96,-5.29,1.34,-8.84,-4.31,1.24,-9.04,-4.27,1.35,-9.08,-4.3,0.03,-8.96,-4.97,0.02,-9.08,-4.9,0.08,-9.08,-4.81,0.1,-9.04,-5.08,0.1,-9.04,-4.98,0.03,-8.96,-4.97,0.01,-9,-5.15,0.12,-9.12,-5.24,0.08,-9.16,-5.16,0.48,-9,-5.45,0.29,-9.08,-5.33,0.24,-8.92,-5.38,0.48,-9,-5.45,0.53,-8.88,-5.41,0.69,-9,-5.47,0.99,-8.88,-5.44,1.02,-8.92,-5.47,0.93,-9,-5.5,1.09,-9,-5.49,1.02,-8.92,-5.47,1.15,-8.92,-5.4,1.09,-9,-5.49,1.01,-9,-5.51,1.02,-8.92,-5.47,1.09,-9,-5.49,1.15,-8.92,-5.4,1.18,-9,-5.49,1.15,-8.92,-5.4,1.21,-8.96,-5.42,1.18,-9,-5.49,1.64,-8.72,-4.79,1.48,-9.08,-4.97,1.56,-9,-5.13,1.49,-9,-4.54,1.49,-9,-4.58,1.56,-8.96,-4.52,1.56,-8.96,-4.52,1.54,-8.96,-4.5,1.49,-9,-4.54,1.5,-9,-5.22,1.47,-9,-5.27,1.44,-8.92,-5.21,1.52,-9.08,-5.14,1.5,-9,-5.22,1.56,-9,-5.13,1.56,-9,-5.13,1.5,-9,-5.22,1.44,-8.92,-5.21,1.48,-9.2,-5.01,1.52,-9.08,-5.14,1.48,-9.08,-4.97,1.46,-9.04,-4.46,1.48,-9.04,-4.35,1.49,-9.12,-4.46,1.46,-9.04,-4.46,1.51,-9,-4.41,1.48,-9.04,-4.35,1.24,-9.04,-4.27,1.25,-9.08,-4.28,1.35,-9.08,-4.3,1.08,-8.96,-4.22,1.24,-9.04,-4.27,1.13,-8.88,-4.22,0,-8.96,-5.11,0.1,-9.04,-5.08,0.03,-8.96,-4.97,0.29,-9.08,-5.33,0.22,-9.08,-5.31,0.24,-8.92,-5.38,0.22,-9.08,-5.31,0.15,-9.08,-5.29,0.24,-8.92,-5.38,0.89,-9.08,-5.46,1.01,-9,-5.51,1.08,-9.08,-5.5,0.8,-9.12,-4.28,1.05,-9.08,-4.24,0.83,-8.92,-4.23,0.5,-9.08,-4.43,0.51,-9.4,-4.48,0.8,-9.12,-4.28,0.22,-9.08,-4.67,0.22,-9.12,-4.68,0.32,-9.08,-4.6,0.03,-8.96,-4.97,0.1,-9.04,-4.98,0.02,-9.08,-4.9,0.1,-9.04,-4.98,0.1,-9.04,-5.08,0.03,-9.08,-5,0.03,-9.08,-5,0.04,-9.28,-5,0.01,-9.12,-4.91,0,-8.96,-5.11,0.01,-9,-5.15,0.1,-9.04,-5.08,0.52,-9.08,-5.42,0.48,-9,-5.45,0.69,-9,-5.47,0.76,-9.08,-5.45,0.69,-9,-5.47,0.81,-9,-5.49,0.89,-9.08,-5.46,0.81,-9,-5.49,0.93,-9,-5.5,0.89,-9.08,-5.46,0.76,-9.08,-5.45,0.81,-9,-5.49,1.01,-9,-5.51,1.09,-9,-5.49,1.1,-9.04,-5.52,1.08,-9.08,-5.5,1.01,-9,-5.51,1.1,-9.04,-5.52,0.89,-9.08,-5.46,0.93,-9,-5.5,1.01,-9,-5.51,1.4,-9.12,-5.41,1.38,-9.08,-5.4,1.43,-9.08,-5.35,1.38,-9.08,-5.4,1.43,-9.04,-5.35,1.43,-9.08,-5.35,1.44,-9.12,-5.24,1.46,-9.2,-5.35,1.43,-9.08,-5.35,1.43,-9.08,-5.35,1.43,-9.04,-5.35,1.48,-9.04,-5.24,1.43,-9.04,-5.35,1.47,-9,-5.27,1.48,-9.04,-5.24,1.5,-9,-5.22,1.48,-9.04,-5.24,1.47,-9,-5.27,1.52,-9.08,-5.14,1.48,-9.04,-5.24,1.5,-9,-5.22,1.52,-9.08,-5.14,1.56,-9,-5.13,1.48,-9.08,-4.97,1.49,-9,-4.61,1.54,-9.2,-4.73,1.57,-8.92,-4.67,1.46,-9.08,-4.6,1.49,-9,-4.58,1.49,-9,-4.54,1.46,-9.04,-4.51,1.46,-9.08,-4.6,1.49,-9,-4.54,1.25,-9.08,-4.28,1.26,-9.12,-4.3,1.35,-9.08,-4.3,1.24,-9.04,-4.27,1.08,-8.96,-4.22,1.05,-9.08,-4.24,1.13,-9.08,-4.25,1.17,-9.12,-4.25,1.25,-9.08,-4.28,1.05,-9.08,-4.24,1.08,-8.96,-4.22,0.83,-8.92,-4.23,0.8,-9.12,-4.28,0.83,-8.92,-4.23,0.66,-8.84,-4.37,0.19,-9.12,-4.69,0.22,-9.12,-4.68,0.22,-9.08,-4.67,0.19,-9.12,-4.69,0.22,-9.08,-4.67,0.16,-9.04,-4.74,0.11,-9.12,-4.74,0.19,-9.12,-4.69,0.16,-9.04,-4.74,0.08,-9.08,-4.81,0.02,-9.08,-4.9,0.08,-9.12,-4.88,0.02,-9.08,-4.9,0.01,-9.12,-4.91,0.08,-9.12,-4.88,0.03,-9.08,-5,0.01,-9.12,-4.91,0.02,-9.08,-4.9,0.1,-9.04,-4.98,0.03,-9.08,-5,0.02,-9.08,-4.9,0.1,-9.04,-5.08,0.01,-9.2,-5.1,0.03,-9.08,-5,0.1,-9.04,-5.08,0.01,-9,-5.15,0.08,-9.16,-5.16,0.01,-9,-5.15,0.05,-8.88,-5.27,0.15,-9.08,-5.29,0.01,-9,-5.15,0.15,-9.08,-5.29,0.12,-9.12,-5.24,0.48,-9,-5.45,0.52,-9.08,-5.42,0.29,-9.08,-5.33,1.4,-9.12,-5.41,1.43,-9.08,-5.35,1.46,-9.2,-5.35,1.44,-9.12,-5.24,1.43,-9.08,-5.35,1.48,-9.04,-5.24,1.46,-9.2,-5.18,1.44,-9.12,-5.2,1.52,-9.08,-5.14,1.46,-9.2,-5.18,1.52,-9.08,-5.14,1.48,-9.2,-5.01,1.54,-9.2,-4.73,1.5,-9.2,-4.92,1.48,-9.08,-4.97,1.64,-8.72,-4.79,1.57,-8.92,-4.67,1.48,-9.08,-4.97,1.49,-9,-4.61,1.46,-9.08,-4.6,1.54,-9.2,-4.73,1.38,-9.12,-4.32,1.44,-9.2,-4.35,1.48,-9.04,-4.35,1.52,-9.2,-4.43,1.49,-9.12,-4.46,1.48,-9.04,-4.35,1.35,-9.08,-4.3,1.38,-9.12,-4.32,1.48,-9.04,-4.35,1.44,-9.2,-4.35,1.52,-9.2,-4.43,1.48,-9.04,-4.35,1.34,-8.84,-4.31,1.35,-9.08,-4.3,1.48,-9.04,-4.35,1.35,-9.12,-4.3,1.38,-9.12,-4.32,1.35,-9.08,-4.3,1.44,-9.12,-5.24,1.44,-9.12,-5.2,1.46,-9.2,-5.18,1.46,-9.08,-4.6,1.49,-9,-4.61,1.49,-9,-4.58,1.49,-9.12,-4.46,1.46,-9.08,-4.6,1.46,-9.04,-4.51,1.52,-9.2,-4.43,1.44,-9.2,-4.35,1.38,-9.36,-4.36,1.38,-9.12,-4.32,1.38,-9.16,-4.32,1.44,-9.2,-4.35,1.26,-9.12,-4.3,1.17,-9.12,-4.25,1.19,-9.2,-4.29,1.01,-9.24,-4.28,0.99,-9.68,-4.45,1.12,-9.68,-4.43,0.5,-9.08,-4.43,0.32,-9.08,-4.6,0.34,-9.24,-4.58,1.01,-9.24,-4.28,0.81,-9.6,-4.47,0.99,-9.68,-4.45,0.08,-9.12,-4.88,0.12,-9.2,-4.79,0.29,-9.12,-4.91,0.1,-9.04,-5.08,0.08,-9.16,-5.16,0.01,-9.2,-5.1,0.12,-9.12,-5.24,0.07,-9.16,-5.31,0.08,-9.16,-5.16,0.12,-9.12,-5.24,0.15,-9.12,-5.26,0.14,-9.16,-5.33,0.28,-9.12,-5.23,0.22,-9.08,-5.31,0.29,-9.08,-5.33,0.33,-9.12,-5.3,0.31,-9.16,-5.32,0.28,-9.12,-5.23,0.31,-9.16,-5.32,0.21,-9.16,-5.27,0.28,-9.12,-5.23,0.33,-9.12,-5.3,0.28,-9.12,-5.23,0.29,-9.08,-5.33,1.11,-9.28,-5.36,1.13,-9.12,-5.41,1.22,-9.24,-5.45,1.2,-9.12,-5.51,1.13,-9.12,-5.41,1.08,-9.08,-5.5,0.38,-9.16,-5.38,0.35,-9.2,-5.4,0.3,-9.2,-5.37,0.38,-9.16,-5.38,0.3,-9.2,-5.37,0.31,-9.16,-5.32,0.38,-9.16,-5.38,0.31,-9.16,-5.32,0.33,-9.12,-5.3,0.35,-9.2,-5.4,0.38,-9.16,-5.38,0.4,-9.2,-5.44,0.68,-9.2,-5.29,0.82,-9.28,-5.37,0.68,-9.28,-5.44,0.79,-9.16,-5.27,0.68,-9.2,-5.29,0.61,-9.16,-5.26,0.68,-9.2,-5.29,0.79,-9.16,-5.27,0.82,-9.28,-5.37,1.06,-9.44,-5.35,1.22,-9.36,-5.38,1.31,-9.44,-5.38,1.11,-9.28,-5.36,1.02,-9.16,-5.35,1.13,-9.12,-5.41,1.2,-9.12,-5.51,1.08,-9.08,-5.5,1.1,-9.04,-5.52,1.59,-9.2,-4.61,1.46,-9.08,-4.6,1.49,-9.12,-4.46,1.49,-9.12,-4.46,1.46,-9.04,-4.51,1.46,-9.04,-4.46,1.46,-9.08,-4.6,1.59,-9.2,-4.61,1.54,-9.2,-4.73,1.52,-9.2,-4.43,1.62,-9.44,-4.63,1.59,-9.2,-4.61,1.32,-9.48,-4.37,1.38,-9.36,-4.36,1.19,-9.2,-4.29,1.17,-9.12,-4.25,1.26,-9.12,-4.3,1.25,-9.08,-4.28,0.22,-9.12,-4.68,0.28,-9.2,-4.68,0.32,-9.08,-4.6,0.34,-9.24,-4.58,0.32,-9.08,-4.6,0.28,-9.2,-4.68,0.28,-9.2,-4.68,0.35,-9.28,-4.77,0.38,-9.32,-4.72,0.31,-9.16,-4.82,0.3,-9.24,-4.81,0.28,-9.2,-4.68,-0.01,-9.28,-5.18,-0.14,-9.44,-5.38,-0.19,-9.4,-5.22,0.08,-9.16,-5.4,0.04,-9.2,-5.36,0.07,-9.16,-5.31,0.08,-9.2,-5.47,0.07,-9.2,-5.5,0.08,-9.16,-5.4,0.08,-9.2,-5.47,0.12,-9.16,-5.39,0.16,-9.2,-5.34,0.08,-9.2,-5.47,0.08,-9.16,-5.4,0.12,-9.16,-5.39,0.14,-9.16,-5.33,0.16,-9.2,-5.34,0.12,-9.16,-5.39,0.16,-9.2,-5.34,0.14,-9.16,-5.33,0.19,-9.16,-5.29,0.14,-9.16,-5.33,0.15,-9.12,-5.26,0.19,-9.16,-5.29,0.34,-9.24,-5.49,0.35,-9.2,-5.4,0.4,-9.2,-5.44,0.98,-9.36,-5.42,0.95,-9.32,-5.41,1.11,-9.28,-5.36,1.22,-9.24,-5.45,1.13,-9.12,-5.41,1.2,-9.12,-5.51,1.25,-9.24,-5.47,1.22,-9.24,-5.45,1.25,-9.16,-5.51,1.46,-9.2,-5.18,1.48,-9.2,-5.01,1.61,-9.28,-5.03,1.47,-9.28,-5.31,1.44,-9.24,-5.36,1.46,-9.2,-5.35,1.5,-9.44,-5.18,1.46,-9.4,-5.26,1.46,-9.2,-5.18,1.5,-9.2,-4.92,1.48,-9.2,-5.01,1.48,-9.08,-4.97,1.54,-9.2,-4.73,1.62,-9.44,-4.63,1.64,-9.24,-4.76,1.54,-9.2,-4.73,1.59,-9.2,-4.61,1.62,-9.44,-4.63,1.44,-9.2,-4.35,1.38,-9.16,-4.32,1.38,-9.36,-4.36,1.38,-9.16,-4.32,1.26,-9.12,-4.3,1.19,-9.2,-4.29,1.01,-9.24,-4.28,0.8,-9.12,-4.28,0.81,-9.6,-4.47,0.28,-9.2,-4.68,0.3,-9.24,-4.81,0.35,-9.28,-4.77,0.31,-9.16,-4.82,0.28,-9.2,-4.68,0.22,-9.12,-4.68,0.12,-9.2,-4.79,0.3,-9.24,-4.81,0.31,-9.16,-4.82,0.08,-9.12,-4.88,0.04,-9.28,-5,0.12,-9.2,-4.79,0.03,-9.08,-5,0.01,-9.2,-5.1,0.04,-9.28,-5,0.07,-9.16,-5.31,0.04,-9.2,-5.36,-0.01,-9.28,-5.18,0.08,-9.16,-5.4,0.02,-9.2,-5.49,0.04,-9.2,-5.36,0.05,-9.24,-5.54,-0.01,-9.24,-5.5,0.02,-9.2,-5.49,0.02,-9.2,-5.49,0.05,-9.2,-5.52,0.05,-9.24,-5.54,0.08,-9.24,-5.51,0.05,-9.24,-5.54,0.05,-9.2,-5.52,0.05,-9.2,-5.52,0.07,-9.2,-5.5,0.08,-9.24,-5.51,0.07,-9.2,-5.5,0.08,-9.2,-5.47,0.08,-9.24,-5.51,0.15,-9.24,-5.5,0.08,-9.24,-5.51,0.08,-9.2,-5.47,1.47,-9.28,-5.31,1.46,-9.4,-5.26,1.43,-9.36,-5.31,1.46,-9.2,-5.18,1.46,-9.4,-5.26,1.47,-9.28,-5.31,1.59,-9.24,-4.92,1.61,-9.28,-5.03,1.48,-9.2,-5.01,1.5,-9.2,-4.92,1.59,-9.24,-4.92,1.48,-9.2,-5.01,1.59,-9.24,-4.92,1.66,-9.56,-4.92,1.61,-9.28,-5.03,1.52,-9.2,-4.43,1.38,-9.36,-4.36,1.44,-9.52,-4.46,1.52,-9.2,-4.43,1.59,-9.2,-4.61,1.49,-9.12,-4.46,0.34,-9.24,-4.58,0.28,-9.2,-4.68,0.38,-9.32,-4.72,0.3,-9.24,-4.81,0.19,-9.32,-4.73,0.35,-9.28,-4.77,0.12,-9.2,-4.79,0.31,-9.16,-4.82,0.29,-9.12,-4.91,0.08,-9.12,-4.88,0.01,-9.12,-4.91,0.04,-9.28,-5,0.15,-9.08,-5.29,0.15,-9.12,-5.26,0.12,-9.12,-5.24,-0.05,-9.28,-5.02,-0.06,-9.32,-4.99,0.02,-9.36,-4.99,0.01,-9.2,-5.1,-0.01,-9.28,-5.18,-0.05,-9.28,-5.02,0.01,-9.2,-5.1,0.08,-9.16,-5.16,-0.01,-9.28,-5.18,0.04,-9.2,-5.36,-0.12,-9.44,-5.49,-0.14,-9.44,-5.38,-0.01,-9.24,-5.5,0.05,-9.24,-5.54,0,-9.28,-5.58,0.05,-9.24,-5.54,0,-9.28,-5.49,0,-9.28,-5.58,0.1,-9.28,-5.5,0,-9.28,-5.49,0.05,-9.24,-5.54,0.05,-9.24,-5.54,0.08,-9.24,-5.51,0.1,-9.28,-5.5,0.39,-9.24,-5.53,0.34,-9.24,-5.49,0.4,-9.2,-5.44,0.48,-9.28,-5.53,0.39,-9.28,-5.57,0.39,-9.24,-5.53,0.8,-9.32,-5.38,0.82,-9.28,-5.37,0.95,-9.32,-5.41,0.8,-9.32,-5.38,0.95,-9.32,-5.41,0.94,-9.36,-5.41,0.82,-9.28,-5.37,1.02,-9.16,-5.35,0.95,-9.32,-5.41,0.24,-9.24,-5.46,0.34,-9.24,-5.49,0.19,-9.32,-5.54,0.39,-9.28,-5.57,0.36,-9.52,-5.71,0.26,-9.52,-5.71,0.39,-9.24,-5.53,0.39,-9.28,-5.57,0.34,-9.24,-5.49,0.98,-9.36,-5.42,1.06,-9.44,-5.35,0.96,-9.4,-5.39,0.98,-9.36,-5.42,1.11,-9.28,-5.36,1.06,-9.44,-5.35,0.82,-9.28,-5.37,0.79,-9.16,-5.27,1.02,-9.16,-5.35,1.22,-9.36,-5.38,1.11,-9.28,-5.36,1.22,-9.24,-5.45,1.47,-9.28,-5.31,1.43,-9.36,-5.31,1.39,-9.32,-5.39,1.5,-9.44,-5.18,1.46,-9.2,-5.18,1.61,-9.28,-5.03,1.5,-9.44,-5.18,1.61,-9.28,-5.03,1.53,-9.56,-5.13,1.61,-9.28,-5.03,1.66,-9.56,-4.92,1.53,-9.56,-5.13,1.01,-9.24,-4.28,1.19,-9.2,-4.29,1.17,-9.12,-4.25,0.51,-9.4,-4.48,0.5,-9.08,-4.43,0.34,-9.24,-4.58,0.19,-9.32,-4.73,0.3,-9.24,-4.81,0.12,-9.2,-4.79,-0.12,-9.36,-4.99,-0.05,-9.36,-5.11,-0.14,-9.48,-5.05,-0.05,-9.36,-5.11,-0.19,-9.4,-5.22,-0.14,-9.48,-5.05,-0.01,-9.28,-5.18,0.04,-9.2,-5.36,-0.14,-9.44,-5.38,0.05,-9.32,-5.45,0.04,-9.32,-5.48,0,-9.28,-5.49,1.37,-9.32,-5.37,1.39,-9.32,-5.39,1.43,-9.36,-5.31,1.46,-9.2,-5.18,1.47,-9.28,-5.31,1.46,-9.2,-5.35,1.46,-9.2,-5.18,1.46,-9.2,-5.35,1.44,-9.12,-5.24,1.69,-9.56,-4.69,1.66,-9.8,-4.89,1.66,-9.56,-4.92,0.38,-9.32,-4.72,0.39,-9.52,-4.61,0.51,-9.4,-4.48,0.19,-9.32,-4.73,0.38,-9.32,-4.72,0.35,-9.28,-4.77,0.08,-9.36,-4.98,0.04,-9.28,-5,0.02,-9.36,-4.99,0.02,-9.36,-4.99,0.04,-9.28,-5,-0.05,-9.28,-5.02,-0.05,-9.28,-5.02,-0.01,-9.28,-5.18,-0.05,-9.36,-5.11,-0.05,-9.28,-5.02,0.04,-9.28,-5,0.01,-9.2,-5.1,0.24,-9.24,-5.46,0.19,-9.32,-5.54,0.1,-9.28,-5.5,0.95,-9.32,-5.41,1.02,-9.16,-5.35,1.11,-9.28,-5.36,0.98,-9.36,-5.42,0.94,-9.36,-5.41,0.95,-9.32,-5.41,1.22,-9.24,-5.45,1.2,-9.12,-5.51,1.25,-9.16,-5.51,1.22,-9.36,-5.38,1.3,-9.36,-5.39,1.31,-9.44,-5.38,-0.12,-9.36,-4.99,-0.06,-9.32,-4.99,-0.05,-9.36,-5.11,0.04,-9.2,-5.36,-0.01,-9.24,-5.5,-0.12,-9.44,-5.49,0.02,-9.36,-5.65,0.02,-9.4,-5.65,-0.02,-9.36,-5.67,0.06,-9.36,-5.49,0.02,-9.36,-5.65,0,-9.28,-5.58,0.04,-9.32,-5.48,0.06,-9.36,-5.49,0,-9.28,-5.58,0,-9.28,-5.49,0.04,-9.32,-5.48,0,-9.28,-5.58,0.6,-9.4,-5.62,0.36,-9.52,-5.71,0.39,-9.28,-5.57,0.87,-9.4,-5.47,0.92,-9.52,-5.47,0.83,-9.44,-5.52,0.94,-9.36,-5.41,0.98,-9.36,-5.42,0.96,-9.4,-5.39,0.92,-9.52,-5.47,0.87,-9.4,-5.47,0.96,-9.4,-5.39,1.3,-9.36,-5.39,1.22,-9.36,-5.38,1.22,-9.24,-5.45,1.36,-9.4,-5.37,1.33,-9.4,-5.36,1.3,-9.36,-5.39,1.46,-9.4,-5.26,1.44,-9.44,-5.25,1.42,-9.4,-5.31,1.53,-9.56,-5.13,1.59,-9.8,-5.1,1.5,-9.6,-5.18,1.62,-9.44,-4.63,1.66,-9.56,-4.92,1.64,-9.24,-4.76,1.05,-9.08,-4.24,1.01,-9.24,-4.28,1.17,-9.12,-4.25,0.51,-9.4,-4.48,0.54,-9.6,-4.57,0.66,-9.64,-4.55,0.19,-9.32,-4.73,0.22,-9.52,-4.75,0.38,-9.32,-4.72,0.19,-9.32,-4.73,0.17,-9.48,-4.83,0.22,-9.52,-4.75,0.04,-9.28,-5,0.05,-9.36,-4.92,0.12,-9.2,-4.79,0.08,-9.36,-4.98,0.05,-9.36,-4.92,0.04,-9.28,-5,0.02,-9.36,-4.99,0.05,-9.36,-4.92,0.08,-9.36,-4.98,0,-9.4,-4.96,0.02,-9.36,-4.99,-0.06,-9.32,-4.99,-0.07,-9.4,-4.95,-0.18,-9.44,-4.94,-0.15,-9.52,-4.89,-0.12,-9.36,-4.99,-0.14,-9.48,-5.05,-0.18,-9.44,-4.94,-0.05,-9.36,-5.11,-0.06,-9.32,-4.99,-0.05,-9.28,-5.02,-0.19,-9.4,-5.22,-0.05,-9.36,-5.11,-0.01,-9.28,-5.18,0.08,-9.16,-5.16,0.07,-9.16,-5.31,-0.01,-9.28,-5.18,-0.3,-9.52,-5.33,-0.28,-9.52,-5.21,-0.19,-9.4,-5.22,-0.18,-9.4,-5.58,-0.12,-9.32,-5.57,-0.02,-9.36,-5.67,-0.18,-9.4,-5.58,-0.08,-9.44,-5.73,-0.2,-9.44,-5.71,0,-9.28,-5.58,-0.02,-9.36,-5.67,-0.12,-9.32,-5.57,0.02,-9.36,-5.65,-0.02,-9.36,-5.67,0,-9.28,-5.58,0.08,-9.4,-5.63,0.02,-9.4,-5.65,0.02,-9.36,-5.65,1.01,-9.52,-5.39,1.06,-9.44,-5.35,1.09,-9.48,-5.33,1.06,-9.44,-5.35,1.11,-9.28,-5.36,1.22,-9.36,-5.38,1.33,-9.4,-5.36,1.31,-9.44,-5.38,1.3,-9.36,-5.39,1.46,-9.4,-5.26,1.42,-9.4,-5.31,1.43,-9.36,-5.31,1.44,-9.44,-5.25,1.46,-9.4,-5.26,1.5,-9.44,-5.18,1.38,-9.16,-4.32,1.19,-9.2,-4.29,1.38,-9.36,-4.36,0.05,-9.36,-4.92,0.19,-9.32,-4.73,0.12,-9.2,-4.79,0,-9.4,-4.96,0.06,-9.48,-4.86,0.05,-9.36,-4.92,-0.07,-9.4,-4.95,-0.12,-9.36,-4.99,-0.18,-9.44,-4.94,-0.26,-9.52,-5.41,-0.3,-9.52,-5.33,-0.14,-9.44,-5.38,0.04,-9.2,-5.36,0.02,-9.2,-5.49,-0.01,-9.24,-5.5,-0.18,-9.4,-5.58,-0.18,-9.44,-5.58,-0.12,-9.44,-5.49,-0.18,-9.4,-5.58,-0.02,-9.36,-5.67,-0.08,-9.44,-5.73,-0.32,-9.4,-5.77,-0.36,-9.44,-5.77,-0.27,-9.44,-5.67,-0.17,-9.56,-5.76,-0.08,-9.44,-5.73,-0.05,-9.52,-5.7,0.02,-9.4,-5.65,0.03,-9.44,-5.67,-0.08,-9.44,-5.73,-0.02,-9.36,-5.67,0.02,-9.4,-5.65,-0.08,-9.44,-5.73,0.19,-9.32,-5.54,0.26,-9.52,-5.71,0.12,-9.44,-5.63,0.39,-9.28,-5.57,0.26,-9.52,-5.71,0.19,-9.32,-5.54,0.39,-9.28,-5.57,0.19,-9.32,-5.54,0.34,-9.24,-5.49,-0.12,-9.44,-5.49,-0.21,-9.48,-5.44,-0.14,-9.44,-5.38,-0.12,-9.44,-5.49,-0.01,-9.24,-5.5,-0.12,-9.32,-5.57,-0.13,-9.48,-5.53,-0.21,-9.48,-5.44,-0.12,-9.44,-5.49,-0.12,-9.44,-5.49,-0.18,-9.44,-5.58,-0.13,-9.48,-5.53,-0.1,-9.48,-5.59,-0.13,-9.48,-5.53,-0.18,-9.44,-5.58,-0.12,-9.48,-5.61,-0.1,-9.48,-5.59,-0.18,-9.44,-5.58,1.48,-9.52,-5.2,1.43,-9.48,-5.28,1.44,-9.44,-5.25,1.44,-9.52,-4.46,1.32,-9.48,-4.37,1.31,-9.52,-4.38,0.06,-9.48,-4.86,0.09,-9.52,-4.85,0.17,-9.48,-4.83,0,-9.4,-4.96,-0.01,-9.56,-4.92,0.06,-9.48,-4.86,0.02,-9.36,-4.99,0,-9.4,-4.96,0.05,-9.36,-4.92,-0.07,-9.4,-4.95,-0.15,-9.52,-4.89,-0.01,-9.56,-4.92,-0.14,-9.48,-5.05,-0.14,-9.52,-4.97,-0.18,-9.44,-4.94,-0.22,-9.8,-4.92,-0.17,-9.6,-4.96,-0.39,-9.6,-5.09,-0.22,-9.8,-4.92,-0.39,-9.6,-5.09,-0.46,-9.68,-5.08,-0.3,-9.52,-5.33,-0.19,-9.4,-5.22,-0.14,-9.44,-5.38,-0.35,-9.48,-5.8,-0.4,-9.48,-5.8,-0.36,-9.44,-5.77,-0.35,-9.48,-5.8,-0.36,-9.44,-5.77,-0.32,-9.4,-5.77,-0.17,-9.56,-5.76,-0.05,-9.52,-5.7,0.01,-9.6,-5.81,0.03,-9.44,-5.67,0.01,-9.6,-5.81,-0.05,-9.52,-5.7,0.6,-9.4,-5.62,0.54,-9.56,-5.68,0.36,-9.52,-5.71,0.73,-9.48,-5.59,0.71,-9.52,-5.58,0.65,-9.48,-5.63,0.81,-9.56,-5.54,0.78,-9.56,-5.56,0.75,-9.48,-5.58,1.01,-9.52,-5.39,0.96,-9.4,-5.39,1.06,-9.44,-5.35,0.83,-9.44,-5.52,0.82,-9.4,-5.51,0.87,-9.4,-5.47,1.01,-9.52,-5.39,0.92,-9.52,-5.47,0.96,-9.4,-5.39,0.92,-9.52,-5.47,0.81,-9.56,-5.54,0.83,-9.44,-5.52,1.23,-9.52,-4.36,1.19,-9.2,-4.29,1.01,-9.24,-4.28,1.01,-9.24,-4.28,1.12,-9.68,-4.43,1.23,-9.52,-4.36,0.51,-9.4,-4.48,0.66,-9.64,-4.55,0.81,-9.6,-4.47,0.39,-9.52,-4.61,0.38,-9.32,-4.72,0.22,-9.52,-4.75,0.38,-9.32,-4.72,0.51,-9.4,-4.48,0.34,-9.24,-4.58,-0.11,-9.64,-4.92,-0.15,-9.52,-4.89,-0.19,-9.56,-4.91,-0.19,-9.4,-5.22,-0.28,-9.52,-5.21,-0.14,-9.48,-5.05,-0.26,-9.52,-5.41,-0.32,-9.48,-5.61,-0.41,-9.52,-5.65,-0.32,-9.48,-5.61,-0.26,-9.52,-5.41,-0.14,-9.44,-5.38,-0.32,-9.48,-5.61,-0.38,-9.48,-5.7,-0.41,-9.52,-5.65,-0.47,-9.52,-5.74,-0.41,-9.52,-5.65,-0.38,-9.48,-5.7,-0.44,-9.52,-5.79,-0.47,-9.52,-5.74,-0.38,-9.48,-5.7,-0.4,-9.48,-5.8,-0.38,-9.48,-5.7,-0.36,-9.44,-5.77,-0.41,-9.56,-5.73,-0.44,-9.52,-5.79,-0.4,-9.48,-5.8,-0.1,-9.48,-5.59,-0.12,-9.48,-5.61,-0.11,-9.52,-5.66,-0.2,-9.44,-5.71,-0.23,-9.52,-5.68,-0.11,-9.52,-5.66,-0.2,-9.44,-5.71,-0.11,-9.52,-5.66,-0.12,-9.48,-5.61,-0.32,-9.52,-5.73,-0.3,-9.52,-5.74,-0.38,-9.48,-5.7,-0.2,-9.44,-5.71,-0.08,-9.44,-5.73,-0.17,-9.56,-5.76,-0.18,-9.4,-5.58,-0.12,-9.44,-5.49,-0.12,-9.32,-5.57,0.54,-9.56,-5.68,0.6,-9.4,-5.62,0.65,-9.48,-5.63,0.7,-9.44,-5.57,0.73,-9.48,-5.59,0.65,-9.48,-5.63,0.7,-9.44,-5.57,0.65,-9.48,-5.63,0.6,-9.4,-5.62,1.48,-9.52,-5.2,1.44,-9.44,-5.25,1.5,-9.44,-5.18,1.5,-9.44,-5.18,1.53,-9.56,-5.13,1.48,-9.52,-5.2,1.44,-9.52,-4.46,1.34,-9.56,-4.43,1.4,-9.64,-4.46,1.23,-9.52,-4.36,1.32,-9.48,-4.37,1.19,-9.2,-4.29,1.52,-9.2,-4.43,1.44,-9.52,-4.46,1.62,-9.44,-4.63,0.06,-9.48,-4.86,0.17,-9.48,-4.83,0.19,-9.32,-4.73,0.05,-9.36,-4.92,0.06,-9.48,-4.86,0.19,-9.32,-4.73,0.09,-9.52,-4.85,0.06,-9.48,-4.86,0.06,-9.52,-4.8,1.32,-9.68,-4.45,1.23,-9.52,-4.36,1.12,-9.68,-4.43,0.99,-9.68,-4.45,0.81,-9.68,-4.5,0.84,-9.72,-4.6,0.29,-9.64,-4.77,0.41,-9.64,-4.74,0.39,-9.52,-4.61,0.18,-9.52,-4.83,0.22,-9.52,-4.75,0.17,-9.48,-4.83,0.15,-9.64,-4.73,0.18,-9.52,-4.83,0.04,-9.56,-4.8,-0.01,-9.56,-4.92,0.04,-9.56,-4.8,0.06,-9.48,-4.86,-0.11,-9.64,-4.92,-0.01,-9.56,-4.92,-0.15,-9.52,-4.89,-0.17,-9.6,-4.96,-0.19,-9.56,-4.91,-0.14,-9.52,-4.97,-0.38,-9.56,-5.21,-0.3,-9.52,-5.33,-0.38,-9.56,-5.35,-0.38,-9.56,-5.21,-0.28,-9.52,-5.21,-0.3,-9.52,-5.33,-0.32,-9.56,-5.69,-0.41,-9.52,-5.65,-0.42,-9.56,-5.69,-0.41,-9.52,-5.65,-0.47,-9.52,-5.74,-0.42,-9.56,-5.69,-0.42,-9.56,-5.69,-0.47,-9.52,-5.74,-0.51,-9.56,-5.71,-0.68,-9.72,-5.87,-0.37,-9.6,-5.81,-0.35,-9.68,-5.87,-0.65,-9.88,-5.89,-0.68,-9.72,-5.87,-0.35,-9.68,-5.87,-0.44,-9.52,-5.79,-0.41,-9.56,-5.73,-0.47,-9.52,-5.74,-0.4,-9.48,-5.8,-0.44,-9.52,-5.79,-0.38,-9.48,-5.7,-0.41,-9.56,-5.73,-0.4,-9.48,-5.8,-0.35,-9.48,-5.8,-0.3,-9.52,-5.74,-0.3,-9.56,-5.71,-0.23,-9.52,-5.68,-0.3,-9.52,-5.74,-0.23,-9.52,-5.68,-0.2,-9.44,-5.71,-0.3,-9.52,-5.74,-0.32,-9.52,-5.73,-0.3,-9.56,-5.71,-0.32,-9.52,-5.73,-0.25,-9.52,-5.71,-0.3,-9.56,-5.71,-0.3,-9.56,-5.71,-0.25,-9.52,-5.71,-0.17,-9.56,-5.76,0.03,-9.44,-5.67,0.12,-9.44,-5.63,0.01,-9.6,-5.81,0.26,-9.52,-5.71,0.32,-9.6,-5.75,0.19,-9.64,-5.84,0.6,-9.6,-5.66,0.54,-9.56,-5.68,0.65,-9.48,-5.63,0.69,-9.64,-5.61,0.6,-9.6,-5.66,0.71,-9.52,-5.58,0.71,-9.52,-5.58,0.73,-9.48,-5.59,0.75,-9.48,-5.58,0.81,-9.56,-5.54,0.75,-9.48,-5.58,0.83,-9.44,-5.52,0.92,-9.52,-5.47,0.91,-9.56,-5.46,0.81,-9.56,-5.54,0.87,-9.4,-5.47,0.94,-9.36,-5.41,0.96,-9.4,-5.39,1.59,-9.8,-5.1,1.48,-9.8,-5.21,1.5,-9.6,-5.18,1.55,-9.6,-4.53,1.69,-9.56,-4.69,1.62,-9.44,-4.63,1.43,-9.68,-4.51,1.49,-9.72,-4.54,1.55,-9.6,-4.53,1.44,-9.52,-4.46,1.38,-9.36,-4.36,1.32,-9.48,-4.37,1.32,-9.68,-4.45,1.34,-9.56,-4.43,1.23,-9.52,-4.36,0.8,-9.12,-4.28,0.51,-9.4,-4.48,0.81,-9.6,-4.47,0.39,-9.52,-4.61,0.47,-9.6,-4.6,0.51,-9.4,-4.48,0.47,-9.6,-4.6,0.41,-9.64,-4.74,0.54,-9.64,-4.68,0.15,-9.64,-4.73,0.29,-9.64,-4.77,0.22,-9.52,-4.75,-0.01,-9.56,-4.92,-0.11,-9.64,-4.92,0.03,-9.64,-4.87,0,-9.4,-4.96,-0.07,-9.4,-4.95,-0.01,-9.56,-4.92,-0.14,-9.52,-4.97,-0.19,-9.56,-4.91,-0.15,-9.52,-4.89,-0.18,-9.44,-4.94,-0.14,-9.52,-4.97,-0.15,-9.52,-4.89,-0.51,-9.56,-5.07,-0.46,-9.68,-5.08,-0.39,-9.6,-5.09,-0.95,-9.6,-5.47,-0.85,-9.6,-5.5,-0.93,-9.56,-5.56,-0.67,-9.56,-5.79,-0.54,-9.56,-5.75,-0.68,-9.72,-5.87,-0.68,-9.72,-5.87,-0.54,-9.56,-5.75,-0.37,-9.6,-5.81,-0.33,-9.56,-5.7,-0.3,-9.56,-5.71,-0.31,-9.6,-5.8,-0.3,-9.56,-5.71,-0.17,-9.56,-5.76,-0.31,-9.6,-5.8,-0.31,-9.6,-5.8,-0.17,-9.56,-5.76,-0.09,-9.76,-5.93,-0.17,-9.56,-5.76,0.01,-9.6,-5.81,-0.09,-9.76,-5.93,-0.05,-9.52,-5.7,-0.08,-9.44,-5.73,0.03,-9.44,-5.67,-0.2,-9.44,-5.71,-0.17,-9.56,-5.76,-0.25,-9.52,-5.71,0.12,-9.44,-5.63,0.26,-9.52,-5.71,0.01,-9.6,-5.81,0.26,-9.52,-5.71,0.19,-9.64,-5.84,0.12,-9.64,-5.83,0.26,-9.52,-5.71,0.36,-9.52,-5.71,0.35,-9.56,-5.75,0.26,-9.52,-5.71,0.35,-9.56,-5.75,0.32,-9.6,-5.75,0.4,-9.6,-5.71,0.32,-9.6,-5.75,0.35,-9.56,-5.75,0.49,-9.6,-5.69,0.54,-9.56,-5.68,0.6,-9.6,-5.66,0.69,-9.64,-5.61,0.71,-9.52,-5.58,0.78,-9.56,-5.56,0.6,-9.6,-5.66,0.65,-9.48,-5.63,0.71,-9.52,-5.58,0.78,-9.56,-5.56,0.71,-9.52,-5.58,0.75,-9.48,-5.58,1.55,-9.6,-4.53,1.44,-9.52,-4.46,1.4,-9.64,-4.46,1.34,-9.56,-4.43,1.44,-9.52,-4.46,1.31,-9.52,-4.38,1.4,-9.64,-4.46,1.34,-9.56,-4.43,1.32,-9.68,-4.45,0.47,-9.6,-4.6,0.54,-9.6,-4.57,0.51,-9.4,-4.48,0.41,-9.64,-4.74,0.47,-9.6,-4.6,0.39,-9.52,-4.61,0.41,-9.64,-4.74,0.53,-9.76,-4.71,0.54,-9.64,-4.68,0.29,-9.64,-4.77,0.39,-9.52,-4.61,0.22,-9.52,-4.75,0.15,-9.64,-4.73,0.04,-9.56,-4.8,0.04,-9.64,-4.77,0.15,-9.64,-4.73,0.22,-9.52,-4.75,0.18,-9.52,-4.83,0.04,-9.56,-4.8,0.18,-9.52,-4.83,0.06,-9.48,-4.86,0.04,-9.64,-4.77,0.04,-9.56,-4.8,0.03,-9.64,-4.87,0.03,-9.64,-4.87,0.1,-9.68,-4.85,0.04,-9.64,-4.77,-0.01,-9.56,-4.92,0.03,-9.64,-4.87,0.04,-9.56,-4.8,-0.17,-9.6,-4.96,-0.11,-9.64,-4.92,-0.19,-9.56,-4.91,-0.11,-9.64,-4.92,-0.17,-9.6,-4.96,-0.22,-9.8,-4.92,-0.17,-9.6,-4.96,-0.14,-9.52,-4.97,-0.39,-9.6,-5.09,-0.63,-9.76,-5.11,-0.46,-9.68,-5.08,-0.53,-9.6,-5.18,-0.72,-9.68,-5.23,-0.63,-9.76,-5.11,-0.53,-9.6,-5.18,-0.88,-9.64,-5.38,-0.84,-9.64,-5.36,-0.95,-9.6,-5.36,-0.72,-9.68,-5.23,-0.85,-9.68,-5.32,-0.88,-9.88,-5.26,-0.93,-9.56,-5.56,-0.92,-9.56,-5.65,-1.02,-9.68,-5.54,0.01,-9.6,-5.81,-0.02,-9.76,-5.91,-0.09,-9.76,-5.93,0.19,-9.64,-5.84,0.32,-9.6,-5.75,0.34,-9.64,-5.76,0.26,-9.52,-5.71,0.12,-9.64,-5.83,0.01,-9.6,-5.81,0.4,-9.6,-5.71,0.45,-9.6,-5.71,0.42,-9.68,-5.75,0.49,-9.6,-5.69,0.5,-9.64,-5.71,0.45,-9.6,-5.71,0.49,-9.6,-5.69,0.45,-9.6,-5.71,0.54,-9.56,-5.68,0.51,-9.64,-5.7,0.5,-9.64,-5.71,0.49,-9.6,-5.69,0.8,-9.64,-5.54,0.69,-9.64,-5.61,0.78,-9.56,-5.56,0.71,-9.68,-4.55,0.81,-9.68,-4.5,0.81,-9.6,-4.47,0.71,-9.68,-4.55,0.81,-9.6,-4.47,0.66,-9.64,-4.55,0.72,-9.68,-4.59,0.71,-9.68,-4.55,0.66,-9.64,-4.55,0.72,-9.68,-4.59,0.53,-9.76,-4.71,0.84,-9.84,-4.67,-0.14,-9.52,-4.97,-0.14,-9.48,-5.05,-0.39,-9.6,-5.09,-0.14,-9.48,-5.05,-0.28,-9.52,-5.21,-0.39,-9.6,-5.09,-0.51,-9.56,-5.07,-0.53,-9.6,-5.18,-0.46,-9.68,-5.08,-0.72,-9.64,-5.26,-0.72,-9.68,-5.23,-0.53,-9.6,-5.18,-0.84,-9.64,-5.36,-0.85,-9.68,-5.32,-0.8,-9.6,-5.27,-0.95,-9.6,-5.47,-0.94,-9.72,-5.33,-0.88,-9.64,-5.38,-1.02,-9.68,-5.54,-0.95,-9.6,-5.47,-0.93,-9.56,-5.56,-0.92,-9.56,-5.65,-0.84,-9.84,-5.81,-1.02,-9.68,-5.54,-0.8,-9.56,-5.74,-0.67,-9.56,-5.79,-0.68,-9.72,-5.87,-0.37,-9.6,-5.81,-0.31,-9.6,-5.8,-0.35,-9.68,-5.87,0.45,-9.6,-5.71,0.5,-9.64,-5.71,0.48,-9.68,-5.71,0.45,-9.6,-5.71,0.48,-9.68,-5.71,0.42,-9.68,-5.75,0.5,-9.64,-5.71,0.51,-9.64,-5.7,0.58,-9.68,-5.67,1.66,-9.56,-4.92,1.66,-9.8,-4.89,1.59,-9.8,-5.1,1.62,-9.44,-4.63,1.69,-9.56,-4.69,1.66,-9.56,-4.92,1.55,-9.6,-4.53,1.62,-9.44,-4.63,1.44,-9.52,-4.46,1.43,-9.68,-4.51,1.55,-9.6,-4.53,1.4,-9.64,-4.46,1.4,-9.64,-4.46,1.4,-9.68,-4.49,1.43,-9.68,-4.51,1.59,-9.84,-4.65,1.62,-9.84,-4.74,1.69,-9.56,-4.69,1.49,-9.72,-4.54,1.69,-9.56,-4.69,1.55,-9.6,-4.53,1.49,-9.72,-4.54,1.43,-9.68,-4.51,1.43,-9.72,-4.51,1.32,-9.68,-4.45,1.3,-9.72,-4.52,1.43,-9.72,-4.51,1.12,-9.68,-4.43,1.16,-9.8,-4.53,1.3,-9.72,-4.52,1.28,-9.88,-4.54,1.37,-9.84,-4.51,1.3,-9.72,-4.52,0.95,-9.88,-4.68,0.84,-9.72,-4.6,0.84,-9.84,-4.67,0.95,-9.88,-4.68,0.99,-9.68,-4.45,0.84,-9.72,-4.6,0.81,-9.6,-4.47,0.81,-9.68,-4.5,0.99,-9.68,-4.45,0.29,-9.64,-4.77,0.29,-9.68,-4.8,0.41,-9.64,-4.74,0.1,-9.68,-4.85,0.07,-9.84,-4.9,0.21,-9.72,-4.82,-0.85,-9.68,-5.32,-0.72,-9.64,-5.26,-0.8,-9.6,-5.27,-0.72,-9.68,-5.23,-0.72,-9.64,-5.26,-0.85,-9.68,-5.32,-0.85,-9.68,-5.32,-0.84,-9.64,-5.36,-0.88,-9.64,-5.38,-1.04,-9.96,-5.37,-0.88,-9.88,-5.26,-0.94,-9.72,-5.33,-0.84,-9.84,-5.81,-0.92,-9.56,-5.65,-0.8,-9.56,-5.74,-0.35,-9.68,-5.87,-0.31,-9.6,-5.8,-0.09,-9.76,-5.93,1.62,-9.84,-4.74,1.66,-9.8,-4.89,1.69,-9.56,-4.69,1.43,-9.72,-4.51,1.37,-9.84,-4.51,1.49,-9.72,-4.54,1.12,-9.68,-4.43,1.3,-9.72,-4.52,1.32,-9.68,-4.45,0.84,-9.72,-4.6,0.72,-9.68,-4.59,0.84,-9.84,-4.67,0.72,-9.68,-4.59,0.54,-9.64,-4.68,0.53,-9.76,-4.71,0.38,-9.84,-4.83,0.48,-9.88,-4.86,0.53,-9.84,-4.79,-0.72,-9.68,-5.23,-0.88,-9.88,-5.26,-0.75,-9.88,-5.17,-0.94,-9.72,-5.33,-0.85,-9.68,-5.32,-0.88,-9.64,-5.38,-0.95,-9.6,-5.47,-1.02,-9.68,-5.54,-0.94,-9.72,-5.33,-1.07,-9.88,-5.66,-1.02,-9.68,-5.54,-0.99,-9.88,-5.78,-0.02,-9.76,-5.91,0.01,-9.6,-5.81,0.12,-9.64,-5.83,0.15,-9.76,-5.88,-0.02,-9.76,-5.91,0.12,-9.64,-5.83,1.66,-9.56,-4.92,1.59,-9.24,-4.92,1.64,-9.24,-4.76,1.53,-9.56,-5.13,1.66,-9.56,-4.92,1.59,-9.8,-5.1,1.59,-9.84,-4.65,1.49,-9.72,-4.54,1.37,-9.84,-4.51,1.3,-9.72,-4.52,1.37,-9.84,-4.51,1.43,-9.72,-4.51,1.12,-9.68,-4.43,0.99,-9.68,-4.45,1.16,-9.8,-4.53,0.54,-9.64,-4.68,0.66,-9.64,-4.55,0.54,-9.6,-4.57,-0.06,-9.84,-4.92,0.07,-9.84,-4.9,0.1,-9.68,-4.85,-0.22,-9.8,-4.92,-0.06,-9.84,-4.92,-0.11,-9.64,-4.92,-0.46,-9.68,-5.08,-0.63,-9.76,-5.11,-0.53,-9.92,-5.07,-0.84,-9.96,-5.21,-0.88,-9.88,-5.26,-1.04,-9.96,-5.37,-0.88,-9.88,-5.26,-0.82,-9.92,-5.19,-0.75,-9.88,-5.17,-0.84,-9.84,-5.81,-0.8,-9.56,-5.74,-0.68,-9.72,-5.87,-0.84,-9.84,-5.81,-0.68,-9.72,-5.87,-0.75,-9.92,-5.89,-0.19,-9.88,-5.94,-0.35,-9.68,-5.87,-0.09,-9.76,-5.93,-0.1,-9.88,-5.9,-0.19,-9.88,-5.94,-0.09,-9.76,-5.93,-0.09,-9.76,-5.93,-0.02,-9.76,-5.91,-0.04,-9.8,-5.93,1.49,-9.72,-4.54,1.59,-9.84,-4.65,1.69,-9.56,-4.69,1.28,-9.88,-4.54,1.3,-9.72,-4.52,1.16,-9.8,-4.53,0.95,-9.88,-4.68,1.08,-9.88,-4.62,0.99,-9.68,-4.45,0.84,-9.84,-4.67,0.53,-9.76,-4.71,0.53,-9.84,-4.79,0.54,-9.64,-4.68,0.72,-9.68,-4.59,0.66,-9.64,-4.55,0.38,-9.84,-4.83,0.41,-9.64,-4.74,0.29,-9.68,-4.8,0.38,-9.84,-4.83,0.29,-9.68,-4.8,0.21,-9.72,-4.82,0.03,-9.64,-4.87,-0.11,-9.64,-4.92,-0.06,-9.84,-4.92,0.03,-9.64,-4.87,-0.06,-9.84,-4.92,0.1,-9.68,-4.85,-0.13,-9.88,-4.95,-0.06,-9.84,-4.92,-0.22,-9.8,-4.92,-0.68,-9.72,-5.87,-0.65,-9.88,-5.89,-0.75,-9.92,-5.89,-0.54,-9.56,-5.75,-0.41,-9.56,-5.73,-0.37,-9.6,-5.81,-0.1,-9.88,-5.9,-0.03,-9.84,-5.92,0,-9.88,-5.89,0.05,-9.84,-5.89,-0.03,-9.84,-5.92,-0.04,-9.8,-5.93,1.28,-9.88,-4.54,1.16,-9.8,-4.53,1.23,-9.88,-4.58,1.23,-9.88,-4.58,1.16,-9.8,-4.53,1.08,-9.88,-4.62,1.16,-9.8,-4.53,0.99,-9.68,-4.45,1.08,-9.88,-4.62,0.95,-9.88,-4.68,0.84,-9.84,-4.67,0.88,-9.88,-4.74,0.38,-9.84,-4.83,0.53,-9.84,-4.79,0.53,-9.76,-4.71,0.38,-9.84,-4.83,0.41,-9.88,-4.89,0.48,-9.88,-4.86,0.38,-9.84,-4.83,0.53,-9.76,-4.71,0.41,-9.64,-4.74,0.38,-9.84,-4.83,0.21,-9.72,-4.82,0.07,-9.84,-4.9,-0.22,-9.8,-4.92,-0.46,-9.68,-5.08,-0.38,-9.92,-5.03,-0.13,-9.88,-4.95,-0.22,-9.8,-4.92,-0.38,-9.92,-5.03,-0.38,-9.92,-5.03,-0.46,-9.68,-5.08,-0.53,-9.92,-5.07,-0.75,-9.88,-5.17,-0.67,-9.88,-5.12,-0.72,-9.68,-5.23,-0.94,-9.72,-5.33,-1.02,-9.68,-5.54,-1.1,-9.88,-5.49,-0.19,-9.88,-5.94,-0.65,-9.88,-5.89,-0.35,-9.68,-5.87,-0.54,-9.56,-5.75,-0.47,-9.52,-5.74,-0.41,-9.56,-5.73,-0.1,-9.88,-5.9,-0.09,-9.76,-5.93,-0.04,-9.8,-5.93,-0.1,-9.88,-5.9,-0.04,-9.8,-5.93,-0.03,-9.84,-5.92,1.63,-9.88,-4.69,1.62,-9.84,-4.74,1.59,-9.84,-4.65,1.63,-9.88,-4.69,1.59,-9.84,-4.65,1.58,-9.88,-4.66,0.89,-9.92,-4.74,0.95,-9.88,-4.68,0.88,-9.88,-4.74,0.89,-9.92,-4.74,0.88,-9.88,-4.74,0.8,-9.92,-4.79,0.52,-9.92,-4.93,0.41,-9.88,-4.89,0.41,-9.92,-4.99,0.41,-9.88,-4.89,0.52,-9.92,-4.93,0.48,-9.88,-4.86,-0.53,-9.92,-5.07,-0.67,-9.88,-5.12,-0.63,-9.92,-5.14,-0.53,-9.92,-5.07,-0.63,-9.76,-5.11,-0.67,-9.88,-5.12,-0.67,-9.88,-5.12,-0.63,-9.76,-5.11,-0.72,-9.68,-5.23,-0.85,-9.68,-5.32,-0.94,-9.72,-5.33,-0.88,-9.88,-5.26,-1.04,-9.96,-5.37,-1.1,-9.88,-5.49,-1.07,-9.96,-5.46,-1.07,-9.96,-5.46,-1.07,-9.88,-5.66,-1.01,-9.96,-5.72,-0.99,-9.88,-5.78,-0.85,-9.88,-5.86,-0.85,-9.96,-5.86,-0.84,-9.84,-5.81,-0.99,-9.88,-5.78,-1.02,-9.68,-5.54,-0.75,-9.92,-5.89,-0.65,-9.88,-5.89,-0.63,-9.92,-5.92,-0.79,-10,-5.18,-0.76,-9.96,-5.16,-0.82,-9.92,-5.19,-0.88,-9.88,-5.26,-0.84,-9.96,-5.21,-0.82,-9.92,-5.19,-1.04,-9.96,-5.37,-0.94,-9.72,-5.33,-1.1,-9.88,-5.49,-1.07,-9.96,-5.46,-1.1,-9.88,-5.49,-1.07,-9.88,-5.66,-1.07,-9.88,-5.66,-1.1,-9.88,-5.49,-1.02,-9.68,-5.54,-1.01,-9.96,-5.72,-1.07,-9.88,-5.66,-0.99,-9.88,-5.78,-1.01,-9.96,-5.72,-0.99,-9.88,-5.78,-0.85,-9.96,-5.86,-0.84,-9.84,-5.81,-0.85,-9.88,-5.86,-0.99,-9.88,-5.78,-0.79,-10,-5.18,-0.82,-9.92,-5.19,-0.84,-9.96,-5.21,-0.79,-10,-5.18,-0.84,-9.96,-5.21,-0.84,-10,-5.21,-0.78,-9.96,-5.88,-0.81,-9.96,-5.87,-0.75,-9.92,-5.89,0.75,-9.76,-5.61,0.66,-9.76,-5.66,0.7,-9.68,-5.61,0.66,-9.76,-5.66,0.64,-9.72,-5.68,0.7,-9.68,-5.61,0.7,-9.68,-5.61,0.64,-9.72,-5.68,0.58,-9.68,-5.67,0.69,-9.64,-5.61,0.7,-9.68,-5.61,0.58,-9.68,-5.67,0.6,-9.76,-5.69,0.64,-9.72,-5.68,0.66,-9.76,-5.66,0.75,-9.76,-5.61,0.7,-9.68,-5.61,0.78,-9.72,-5.59,0.42,-9.68,-5.75,0.42,-9.72,-5.75,0.36,-9.72,-5.78,0.3,-9.76,-5.84,0.36,-9.72,-5.78,0.38,-9.76,-5.82,0.38,-9.76,-5.82,0.42,-9.72,-5.75,0.52,-9.76,-5.74,0.42,-9.72,-5.75,0.38,-9.76,-5.82,0.36,-9.72,-5.78,0.91,-9.68,-5.5,0.9,-9.68,-5.53,0.96,-9.64,-5.47,0.91,-9.68,-5.5,0.96,-9.64,-5.47,1,-9.68,-5.46,0.96,-9.64,-5.47,0.98,-9.64,-5.44,1,-9.68,-5.46,0.81,-9.72,-5.58,0.9,-9.68,-5.53,0.93,-9.72,-5.52,0.9,-9.68,-5.53,0.91,-9.68,-5.5,0.93,-9.72,-5.52,1,-9.64,-5.42,0.98,-9.64,-5.44,1.06,-9.6,-5.39])

IndexedFaceSet392.setCoord(Coordinate393)

Shape389.setGeometry(IndexedFaceSet392)

Transform388.addChildren(Shape389)

fieldValue387.addChildren(Transform388)

ProtoInstance385.addFieldValue(fieldValue387)

fieldValue384.addChildren(ProtoInstance385)

ProtoInstance381.addFieldValue(fieldValue384)

fieldValue370.addChildren(ProtoInstance381)

ProtoInstance367.addFieldValue(fieldValue370)

fieldValue356.addChildren(ProtoInstance367)

ProtoInstance353.addFieldValue(fieldValue356)

fieldValue301.addChildren(ProtoInstance353)

ProtoInstance298.addFieldValue(fieldValue301)

fieldValue297.addChildren(ProtoInstance298)
ProtoInstance394 = ProtoInstance()
ProtoInstance394.setName("Joint")
ProtoInstance394.setDEF("Allen_hanim_vl1")
fieldValue395 = fieldValue()
fieldValue395.setName("name")
fieldValue395.setValue("vl1")

ProtoInstance394.addFieldValue(fieldValue395)
fieldValue396 = fieldValue()
fieldValue396.setName("center")
fieldValue396.setValue("-0.00405 1.07 -0.0275")

ProtoInstance394.addFieldValue(fieldValue396)
fieldValue397 = fieldValue()
fieldValue397.setName("children")
ProtoInstance398 = ProtoInstance()
ProtoInstance398.setName("Segment")
ProtoInstance398.setDEF("Allen_hanim_c7")
fieldValue399 = fieldValue()
fieldValue399.setName("name")
fieldValue399.setValue("l1")

ProtoInstance398.addFieldValue(fieldValue399)
fieldValue400 = fieldValue()
fieldValue400.setName("children")
Transform401 = Transform()
Transform401.setDEF("torso_adjust")
Transform401.setCenter([0,1,0])
Transform401.setRotation([0,1,0,1.570796])
Transform401.setScale([0.1,0.1,0.1])
Shape402 = Shape()
Appearance403 = Appearance()
Material404 = Material()
Material404.setDEF("Shirt_Color")
Material404.setAmbientIntensity(0.25)
Material404.setDiffuseColor([0.6,0.0745,0.1137])

Appearance403.setMaterial(Material404)
ImageTexture405 = ImageTexture()
ImageTexture405.setUSE("camo")

Appearance403.setTexture(ImageTexture405)

Shape402.setAppearance(Appearance403)
IndexedFaceSet406 = IndexedFaceSet()
IndexedFaceSet406.setCoordIndex([0,1,2,-1,3,4,5,-1,6,7,8,-1,9,10,11,-1,12,13,14,-1,15,16,17,-1,18,19,20,-1,21,22,23,-1,24,25,26,-1,27,28,29,-1,30,31,32,-1,33,34,35,-1,36,37,38,-1,39,40,41,-1,42,43,44,-1,45,46,47,-1,48,49,50,-1,53,57,58,-1,62,59,60,-1,67,68,69,-1,70,65,71,-1,76,77,78,-1,77,73,54,-1,79,55,80,-1,55,56,80,-1,59,62,52,-1,78,77,75,-1,64,79,80,-1,51,52,82,-1,83,84,82,-1,62,60,85,-1,86,87,88,-1,88,69,68,-1,89,76,78,-1,77,54,75,-1,78,75,66,-1,89,58,57,-1,53,90,57,-1,90,64,91,-1,63,79,64,-1,80,92,93,-1,92,80,56,-1,94,95,62,-1,85,69,88,-1,71,96,67,-1,97,71,65,-1,54,73,72,-1,58,89,78,-1,83,82,52,-1,98,62,87,-1,99,68,67,-1,70,67,69,-1,100,71,97,-1,438,101,74,-1,102,103,435,-1,53,64,90,-1,91,64,93,-1,81,104,56,-1,84,105,82,-1,106,83,107,-1,106,84,83,-1,95,107,52,-1,98,94,62,-1,86,88,108,-1,85,88,87,-1,68,108,88,-1,68,99,108,-1,99,67,96,-1,71,67,70,-1,100,96,71,-1,100,97,109,-1,110,109,111,-1,438,112,101,-1,103,112,435,-1,101,103,113,-1,102,114,115,-1,116,113,115,-1,117,90,91,-1,64,80,93,-1,92,56,104,-1,61,118,81,-1,105,119,51,-1,120,119,121,-1,107,83,52,-1,62,95,52,-1,95,94,122,-1,62,85,87,-1,123,98,87,-1,123,87,86,-1,86,108,124,-1,108,99,124,-1,110,100,109,-1,103,115,113,-1,103,102,115,-1,125,91,93,-1,104,81,126,-1,118,127,126,-1,120,121,128,-1,121,84,106,-1,121,105,84,-1,95,129,107,-1,129,95,122,-1,130,122,94,-1,130,94,131,-1,94,98,131,-1,132,110,133,-1,110,111,133,-1,134,135,136,-1,101,112,103,-1,135,101,113,-1,116,115,114,-1,137,138,116,-1,104,126,139,-1,139,126,127,-1,127,118,140,-1,118,126,81,-1,140,61,51,-1,140,118,61,-1,119,140,51,-1,119,120,140,-1,105,121,119,-1,82,105,51,-1,128,121,106,-1,141,142,133,-1,143,133,111,-1,101,135,74,-1,144,145,146,-1,144,146,147,-1,148,149,150,-1,151,150,149,-1,152,151,149,-1,153,154,155,-1,156,157,158,-1,159,160,154,-1,137,161,138,-1,162,163,145,-1,164,165,163,-1,166,167,168,-1,168,169,162,-1,168,164,169,-1,170,160,157,-1,156,170,157,-1,159,143,160,-1,143,141,133,-1,143,157,160,-1,136,138,161,-1,171,136,163,-1,164,167,158,-1,170,155,154,-1,156,151,155,-1,157,143,111,-1,146,163,136,-1,167,166,158,-1,168,167,164,-1,164,158,173,-1,156,155,170,-1,160,170,154,-1,159,141,143,-1,156,150,151,-1,136,161,147,-1,163,162,169,-1,166,150,156,-1,165,164,173,-1,138,113,116,-1,113,138,136,-1,163,146,145,-1,166,156,158,-1,175,176,157,-1,178,173,179,-1,135,113,136,-1,146,136,147,-1,157,111,172,-1,180,135,181,-1,164,163,169,-1,165,182,163,-1,183,175,157,-1,135,134,181,-1,157,176,158,-1,178,182,165,-1,180,184,185,-1,184,186,187,-1,134,188,186,-1,171,188,136,-1,182,171,163,-1,184,180,181,-1,134,186,181,-1,182,190,171,-1,187,191,192,-1,188,134,136,-1,193,194,183,-1,181,186,184,-1,195,190,182,-1,195,182,178,-1,196,197,198,-1,199,200,179,-1,199,158,176,-1,174,183,157,-1,183,177,193,-1,188,187,186,-1,190,201,171,-1,195,178,197,-1,178,165,173,-1,171,201,188,-1,203,190,195,-1,204,205,206,-1,206,175,194,-1,175,183,194,-1,189,193,177,-1,203,195,207,-1,203,201,190,-1,203,207,196,-1,197,207,195,-1,185,184,187,-1,207,197,196,-1,196,198,208,-1,192,185,187,-1,208,209,210,-1,201,211,188,-1,197,178,198,-1,175,206,176,-1,205,176,206,-1,201,203,196,-1,187,188,211,-1,172,174,157,-1,198,178,179,-1,187,211,191,-1,201,196,211,-1,173,158,199,-1,213,214,215,-1,196,208,211,-1,204,206,194,-1,216,205,204,-1,217,194,212,-1,193,212,194,-1,205,218,199,-1,205,216,218,-1,217,219,214,-1,204,217,214,-1,220,215,219,-1,198,179,222,-1,205,199,176,-1,193,202,212,-1,191,221,192,-1,179,173,199,-1,217,204,194,-1,213,216,214,-1,217,212,219,-1,219,215,214,-1,213,215,223,-1,218,213,225,-1,215,226,223,-1,223,225,213,-1,227,221,191,-1,179,200,222,-1,210,228,229,-1,218,216,213,-1,227,191,210,-1,227,210,229,-1,209,230,231,-1,230,208,198,-1,232,230,198,-1,200,218,225,-1,199,218,200,-1,226,233,234,-1,210,235,228,-1,230,209,208,-1,236,237,225,-1,235,238,239,-1,240,200,225,-1,241,228,242,-1,211,210,191,-1,211,208,210,-1,243,240,237,-1,238,235,210,-1,209,238,210,-1,209,231,238,-1,238,231,239,-1,232,245,246,-1,198,222,232,-1,222,240,245,-1,226,215,220,-1,247,248,232,-1,248,239,231,-1,226,220,233,-1,248,231,230,-1,216,204,214,-1,242,228,235,-1,247,235,239,-1,236,225,223,-1,223,234,236,-1,223,226,234,-1,234,233,251,-1,236,252,237,-1,253,252,236,-1,224,249,251,-1,254,241,242,-1,247,239,248,-1,255,256,257,-1,243,258,245,-1,240,222,200,-1,237,240,225,-1,234,259,236,-1,254,260,250,-1,246,245,261,-1,240,243,245,-1,247,242,235,-1,255,247,256,-1,234,251,259,-1,262,251,249,-1,248,230,232,-1,233,224,251,-1,255,257,264,-1,252,243,237,-1,242,255,254,-1,265,253,236,-1,224,244,249,-1,255,260,254,-1,232,222,245,-1,252,266,267,-1,265,268,253,-1,259,269,265,-1,255,264,260,-1,243,267,258,-1,259,265,236,-1,270,253,268,-1,251,262,259,-1,262,269,259,-1,243,252,267,-1,252,253,266,-1,267,272,258,-1,261,258,272,-1,269,268,265,-1,269,273,268,-1,273,269,262,-1,264,257,274,-1,246,247,232,-1,275,267,266,-1,273,262,271,-1,246,261,276,-1,255,242,247,-1,253,270,266,-1,275,266,273,-1,273,270,268,-1,262,249,263,-1,256,246,277,-1,245,258,261,-1,261,272,278,-1,273,266,270,-1,279,280,281,-1,256,282,257,-1,246,256,247,-1,267,283,272,-1,267,275,283,-1,261,278,284,-1,272,285,278,-1,286,277,287,-1,288,282,256,-1,279,289,275,-1,274,290,291,-1,288,256,277,-1,286,288,277,-1,292,279,281,-1,274,257,290,-1,288,293,282,-1,286,293,288,-1,294,286,287,-1,272,283,285,-1,282,293,290,-1,294,290,293,-1,293,286,294,-1,294,287,295,-1,246,287,277,-1,246,276,287,-1,279,275,273,-1,261,297,276,-1,279,273,280,-1,289,283,275,-1,273,271,280,-1,290,294,295,-1,289,285,283,-1,298,299,300,-1,297,261,284,-1,301,292,281,-1,291,300,302,-1,257,282,290,-1,295,291,290,-1,303,276,297,-1,279,304,289,-1,305,302,300,-1,285,289,304,-1,306,304,307,-1,276,298,287,-1,278,285,306,-1,299,309,300,-1,279,292,304,-1,305,300,309,-1,295,300,291,-1,285,304,306,-1,310,304,292,-1,309,308,305,-1,307,311,306,-1,278,306,284,-1,295,298,300,-1,310,292,301,-1,307,304,310,-1,312,309,313,-1,299,313,309,-1,311,314,306,-1,315,316,313,-1,306,314,284,-1,301,317,310,-1,314,311,318,-1,319,307,310,-1,314,321,284,-1,314,318,321,-1,307,318,311,-1,298,295,287,-1,321,318,319,-1,318,307,319,-1,322,297,284,-1,323,324,319,-1,320,312,313,-1,316,325,313,-1,301,296,317,-1,303,297,322,-1,326,303,322,-1,321,322,284,-1,327,325,316,-1,325,328,329,-1,316,315,330,-1,322,319,324,-1,331,326,332,-1,313,299,298,-1,303,315,313,-1,333,317,334,-1,335,336,337,-1,326,315,303,-1,317,333,310,-1,325,320,313,-1,338,323,319,-1,303,298,276,-1,326,331,315,-1,323,339,340,-1,326,322,324,-1,303,313,298,-1,322,321,319,-1,342,339,343,-1,344,328,345,-1,346,327,316,-1,347,348,330,-1,315,331,349,-1,324,323,350,-1,328,327,351,-1,315,349,330,-1,352,331,332,-1,350,323,340,-1,353,337,354,-1,330,349,347,-1,349,355,347,-1,355,349,352,-1,349,331,352,-1,352,332,356,-1,357,324,350,-1,358,357,350,-1,353,335,337,-1,335,316,336,-1,336,359,360,-1,359,330,348,-1,436,356,361,-1,332,326,324,-1,357,332,324,-1,357,362,363,-1,364,350,365,-1,366,365,340,-1,333,319,310,-1,336,360,337,-1,348,361,360,-1,356,369,361,-1,332,369,356,-1,363,332,357,-1,357,358,362,-1,358,350,364,-1,358,364,370,-1,365,350,340,-1,333,338,319,-1,329,328,344,-1,371,372,351,-1,335,346,316,-1,330,359,336,-1,359,348,360,-1,369,373,360,-1,369,360,361,-1,374,369,332,-1,370,375,376,-1,376,375,374,-1,376,358,370,-1,376,362,358,-1,376,363,362,-1,325,327,328,-1,351,377,378,-1,353,379,335,-1,316,330,336,-1,360,373,380,-1,374,373,369,-1,363,376,374,-1,363,374,332,-1,343,381,382,-1,383,384,385,-1,329,344,386,-1,387,371,346,-1,374,437,373,-1,390,370,365,-1,370,364,365,-1,366,340,391,-1,392,340,339,-1,340,392,391,-1,323,338,339,-1,328,393,345,-1,346,351,327,-1,351,372,377,-1,346,371,351,-1,387,394,395,-1,395,372,371,-1,387,395,371,-1,396,394,387,-1,337,380,354,-1,370,397,389,-1,390,397,370,-1,365,366,390,-1,398,391,342,-1,391,392,342,-1,338,343,339,-1,338,383,381,-1,386,368,329,-1,386,400,401,-1,386,344,400,-1,402,344,403,-1,402,400,344,-1,378,393,328,-1,378,328,351,-1,404,378,405,-1,377,405,378,-1,395,377,372,-1,439,395,394,-1,335,387,346,-1,380,337,360,-1,366,407,390,-1,407,366,391,-1,342,392,339,-1,402,408,400,-1,387,335,379,-1,353,409,379,-1,354,409,353,-1,410,391,398,-1,384,411,385,-1,412,413,384,-1,399,333,341,-1,402,403,414,-1,344,345,403,-1,393,404,415,-1,378,404,393,-1,406,416,415,-1,417,396,379,-1,417,409,418,-1,396,419,394,-1,417,379,409,-1,409,354,418,-1,407,391,410,-1,398,342,420,-1,421,342,343,-1,421,343,382,-1,399,383,338,-1,399,367,422,-1,343,338,381,-1,412,399,422,-1,399,338,333,-1,423,413,412,-1,415,416,393,-1,416,345,393,-1,396,387,379,-1,354,380,388,-1,385,411,426,-1,411,427,426,-1,383,385,428,-1,411,384,413,-1,412,384,399,-1,424,423,425,-1,414,429,431,-1,430,414,403,-1,429,414,430,-1,439,394,419,-1,426,428,385,-1,399,384,383,-1,432,433,424,-1,433,423,424,-1,433,413,423,-1,396,417,419,-1,354,388,418,-1,434,403,345,-1,70,440,65,-1,440,441,65,-1,441,442,65,-1,442,443,65,-1,443,444,65,-1,444,445,65,-1,445,446,65,-1,446,447,65,-1,447,448,65,-1,448,449,65,-1,449,450,65,-1,450,451,65,-1,451,452,65,-1,452,453,65,-1,453,454,65,-1,454,455,65,-1,455,456,65,-1,456,457,65,-1,457,458,65,-1,458,459,65,-1,462,463,461,-1,461,463,460,-1,460,463,459,-1,459,463,65,-1,329,368,325,-1,368,254,325,-1,325,254,320,-1,260,264,250,-1,274,291,264,-1,264,291,250,-1,291,302,250,-1,302,305,250,-1,305,312,250,-1,320,254,312,-1,250,312,254,-1,479,480,481,-1,482,483,484,-1,485,486,487,-1,483,480,484,-1,488,483,485,-1,488,485,487,-1,480,489,481,-1,490,480,491,-1,492,493,494,-1,486,485,482,-1,495,496,497,-1,495,497,498,-1,490,499,484,-1,483,489,480,-1,481,489,500,-1,479,491,480,-1,501,493,502,-1,494,493,501,-1,503,498,497,-1,504,497,505,-1,504,505,506,-1,485,483,482,-1,495,486,496,-1,492,494,507,-1,492,508,493,-1,509,510,507,-1,511,509,507,-1,504,506,512,-1,484,513,514,-1,507,510,515,-1,516,517,509,-1,509,511,516,-1,518,506,505,-1,506,518,519,-1,496,505,497,-1,492,507,515,-1,521,522,520,-1,522,517,520,-1,520,516,523,-1,520,517,516,-1,524,525,526,-1,525,527,528,-1,518,524,519,-1,514,529,482,-1,483,488,489,-1,502,491,501,-1,515,530,531,-1,533,534,535,-1,534,533,536,-1,486,482,496,-1,495,537,486,-1,484,499,513,-1,515,510,530,-1,533,539,536,-1,493,490,502,-1,492,540,508,-1,534,536,538,-1,542,527,543,-1,543,525,524,-1,544,536,545,-1,546,545,547,-1,542,543,505,-1,518,543,524,-1,490,484,480,-1,540,548,490,-1,493,508,490,-1,549,499,548,-1,550,540,541,-1,545,536,539,-1,542,539,527,-1,499,490,548,-1,502,490,491,-1,541,492,531,-1,527,539,533,-1,505,552,553,-1,549,548,554,-1,492,515,531,-1,544,538,536,-1,496,529,505,-1,496,482,529,-1,541,540,492,-1,551,544,545,-1,508,540,490,-1,545,539,542,-1,543,527,525,-1,514,482,484,-1,555,551,546,-1,514,556,529,-1,557,556,514,-1,513,557,514,-1,558,559,499,-1,549,554,560,-1,559,557,513,-1,559,513,499,-1,499,549,558,-1,542,505,553,-1,529,552,505,-1,557,559,563,-1,558,563,559,-1,560,554,564,-1,557,563,556,-1,554,550,565,-1,563,558,566,-1,541,532,562,-1,567,564,554,-1,568,550,541,-1,563,566,556,-1,569,570,561,-1,571,570,569,-1,556,573,529,-1,566,574,573,-1,548,540,554,-1,568,541,562,-1,850,561,570,-1,545,542,553,-1,549,560,558,-1,554,565,567,-1,568,565,550,-1,547,545,553,-1,569,575,576,-1,545,546,551,-1,543,518,505,-1,568,571,565,-1,556,566,573,-1,573,577,578,-1,560,566,558,-1,579,572,546,-1,579,547,580,-1,553,552,578,-1,574,581,573,-1,567,574,564,-1,573,581,577,-1,582,583,553,-1,529,573,552,-1,554,540,550,-1,569,565,571,-1,564,574,560,-1,576,567,565,-1,547,579,546,-1,584,585,586,-1,567,587,574,-1,572,579,591,-1,553,583,547,-1,592,553,578,-1,552,573,578,-1,592,582,553,-1,582,593,594,-1,566,560,574,-1,595,596,587,-1,569,576,565,-1,577,597,578,-1,584,581,574,-1,547,583,580,-1,577,581,599,-1,598,591,600,-1,580,600,591,-1,602,603,604,-1,577,599,597,-1,587,605,585,-1,597,606,592,-1,603,602,583,-1,583,582,603,-1,588,590,607,-1,604,594,608,-1,582,594,603,-1,593,609,610,-1,611,606,599,-1,579,580,591,-1,580,602,612,-1,610,613,593,-1,582,592,593,-1,578,597,592,-1,606,597,599,-1,601,595,587,-1,604,603,594,-1,596,605,587,-1,851,601,589,-1,593,611,609,-1,593,606,611,-1,574,587,585,-1,583,602,580,-1,593,608,594,-1,599,581,584,-1,584,611,599,-1,601,587,567,-1,600,580,612,-1,604,608,613,-1,584,574,585,-1,614,590,615,-1,586,617,618,-1,614,619,607,-1,614,607,590,-1,620,621,584,-1,586,605,617,-1,601,851,595,-1,576,601,567,-1,622,596,595,-1,623,614,615,-1,624,615,590,-1,625,616,612,-1,626,596,622,-1,627,623,628,-1,614,623,629,-1,628,623,615,-1,630,631,632,-1,633,628,630,-1,630,615,634,-1,625,612,602,-1,604,625,602,-1,586,620,584,-1,596,626,617,-1,632,635,626,-1,630,632,636,-1,630,628,615,-1,596,617,605,-1,638,639,631,-1,637,624,590,-1,625,641,616,-1,593,613,608,-1,634,615,624,-1,631,634,642,-1,631,630,634,-1,643,642,644,-1,646,625,604,-1,609,647,610,-1,626,648,617,-1,635,631,639,-1,632,631,635,-1,641,625,646,-1,646,649,650,-1,626,635,648,-1,651,638,652,-1,638,651,639,-1,653,643,644,-1,634,645,644,-1,644,642,634,-1,638,631,642,-1,652,654,655,-1,634,624,645,-1,641,656,657,-1,656,658,657,-1,648,659,618,-1,660,648,635,-1,660,659,648,-1,659,660,661,-1,643,662,663,-1,643,653,662,-1,849,655,665,-1,666,655,654,-1,651,652,655,-1,638,662,652,-1,655,667,665,-1,666,667,655,-1,662,668,652,-1,641,657,640,-1,669,670,649,-1,671,659,667,-1,659,671,672,-1,648,618,617,-1,672,673,620,-1,656,641,650,-1,674,656,650,-1,610,646,613,-1,586,618,620,-1,675,654,676,-1,849,651,655,-1,652,668,654,-1,668,664,677,-1,662,653,668,-1,641,640,616,-1,650,641,646,-1,669,678,670,-1,610,647,669,-1,646,669,649,-1,618,672,620,-1,671,667,666,-1,679,671,666,-1,675,666,654,-1,668,653,664,-1,610,669,646,-1,646,604,613,-1,679,666,675,-1,680,677,681,-1,675,676,682,-1,649,684,650,-1,685,686,647,-1,584,621,611,-1,585,605,586,-1,659,672,618,-1,676,687,680,-1,676,654,687,-1,688,683,656,-1,688,656,689,-1,656,674,689,-1,684,674,650,-1,678,686,685,-1,671,673,672,-1,690,691,692,-1,693,677,664,-1,692,682,676,-1,695,680,687,-1,674,696,689,-1,669,647,686,-1,621,697,609,-1,621,609,611,-1,621,620,697,-1,698,620,673,-1,699,700,670,-1,697,685,609,-1,682,692,679,-1,692,676,680,-1,680,695,677,-1,690,692,680,-1,693,681,677,-1,593,592,606,-1,671,702,673,-1,703,690,680,-1,674,684,696,-1,649,705,684,-1,702,671,679,-1,706,707,703,-1,703,707,708,-1,709,710,711,-1,670,712,649,-1,713,678,685,-1,714,715,716,-1,703,680,704,-1,694,696,701,-1,694,689,696,-1,685,647,609,-1,691,717,702,-1,706,703,704,-1,696,710,701,-1,700,699,718,-1,649,712,705,-1,670,713,719,-1,698,673,702,-1,698,702,717,-1,707,720,708,-1,710,696,711,-1,705,712,700,-1,669,686,678,-1,692,702,679,-1,680,681,704,-1,721,722,711,-1,709,711,722,-1,700,718,705,-1,711,696,684,-1,700,712,670,-1,692,691,702,-1,691,690,723,-1,724,708,725,-1,726,727,711,-1,713,728,719,-1,620,729,697,-1,690,703,708,-1,730,727,719,-1,718,726,711,-1,718,684,705,-1,721,711,727,-1,699,726,718,-1,719,699,670,-1,678,713,670,-1,729,685,697,-1,725,708,720,-1,718,711,684,-1,731,717,723,-1,690,732,723,-1,733,713,685,-1,734,698,717,-1,731,735,736,-1,691,723,717,-1,690,708,724,-1,728,739,719,-1,733,741,728,-1,733,742,741,-1,698,714,743,-1,744,715,745,-1,714,698,715,-1,734,736,745,-1,731,736,734,-1,731,723,735,-1,726,699,719,-1,717,731,734,-1,724,738,732,-1,740,746,747,-1,722,721,740,-1,726,719,727,-1,729,733,685,-1,742,743,714,-1,620,698,729,-1,715,734,745,-1,748,744,745,-1,749,750,732,-1,740,721,746,-1,751,746,721,-1,735,748,736,-1,751,721,727,-1,752,730,753,-1,730,754,753,-1,748,745,736,-1,749,732,738,-1,727,730,752,-1,739,730,719,-1,713,733,728,-1,756,716,744,-1,723,750,735,-1,690,724,732,-1,746,757,758,-1,759,751,752,-1,751,727,752,-1,739,728,741,-1,714,716,756,-1,715,698,734,-1,723,732,750,-1,738,737,755,-1,733,743,742,-1,760,742,714,-1,759,752,763,-1,735,750,749,-1,759,762,757,-1,746,751,757,-1,751,759,757,-1,754,764,753,-1,733,729,743,-1,744,748,765,-1,749,738,755,-1,730,739,754,-1,698,743,729,-1,766,735,749,-1,763,752,753,-1,739,767,754,-1,765,768,756,-1,759,769,762,-1,770,771,754,-1,742,760,741,-1,756,744,765,-1,766,768,765,-1,765,748,735,-1,766,755,761,-1,772,770,760,-1,744,716,715,-1,755,766,749,-1,766,765,735,-1,760,770,741,-1,764,754,773,-1,774,773,775,-1,773,754,775,-1,739,741,767,-1,770,767,741,-1,767,770,754,-1,769,776,777,-1,761,778,779,-1,766,779,768,-1,774,780,776,-1,753,764,763,-1,775,771,781,-1,756,760,714,-1,759,763,769,-1,771,775,754,-1,774,776,769,-1,780,774,775,-1,772,771,770,-1,768,782,756,-1,779,782,768,-1,761,783,778,-1,764,773,774,-1,763,774,769,-1,778,783,785,-1,763,764,774,-1,756,786,760,-1,761,779,766,-1,784,776,787,-1,786,771,772,-1,788,789,790,-1,791,779,792,-1,793,792,778,-1,792,779,778,-1,776,780,787,-1,780,775,794,-1,795,786,782,-1,778,785,796,-1,796,797,793,-1,796,793,778,-1,799,787,780,-1,782,786,756,-1,791,800,782,-1,801,787,802,-1,791,803,800,-1,793,803,792,-1,779,791,782,-1,791,792,803,-1,803,793,797,-1,796,785,798,-1,806,807,808,-1,787,799,802,-1,788,810,811,-1,788,811,812,-1,812,807,806,-1,794,799,780,-1,802,806,809,-1,794,806,799,-1,812,794,789,-1,786,813,781,-1,814,795,800,-1,800,803,797,-1,794,775,815,-1,786,772,760,-1,795,813,786,-1,816,817,818,-1,806,802,799,-1,794,812,806,-1,794,815,789,-1,775,781,815,-1,813,819,781,-1,813,820,819,-1,800,795,782,-1,798,821,816,-1,812,811,822,-1,812,822,804,-1,786,781,771,-1,821,823,816,-1,824,825,805,-1,796,798,816,-1,812,804,807,-1,816,814,800,-1,800,797,816,-1,788,812,789,-1,826,827,828,-1,824,805,822,-1,829,810,788,-1,795,814,813,-1,811,831,822,-1,788,790,832,-1,789,781,819,-1,835,825,824,-1,824,831,829,-1,811,810,831,-1,789,819,830,-1,831,824,822,-1,831,810,829,-1,827,826,817,-1,817,816,823,-1,836,834,825,-1,824,837,838,-1,816,818,814,-1,826,839,840,-1,797,796,816,-1,835,836,825,-1,835,824,838,-1,837,824,829,-1,837,829,788,-1,833,841,842,-1,835,843,836,-1,844,845,838,-1,789,815,781,-1,814,818,813,-1,842,827,817,-1,842,817,823,-1,817,826,840,-1,837,844,838,-1,789,830,790,-1,842,823,833,-1,846,844,837,-1,832,846,837,-1,832,837,788,-1,839,826,828,-1,847,820,818,-1,817,840,818,-1,818,820,813,-1,840,848,818,-1,848,847,818,-1,854,852,853,-1,855,856,857,-1,858,859,860,-1,861,862,863,-1,866,867,865,-1,865,867,864,-1,867,868,864,-1,874,875,873,-1,869,870,877,-1,870,871,877,-1,876,877,875,-1,875,877,873,-1,871,872,877,-1,873,877,872,-1,879,880,878,-1,878,880,882,-1,881,882,880,-1,883,884,885,-1,886,887,888,-1,889,890,891,-1,892,893,894,-1,895,896,897,-1,898,899,900,-1,901,902,903,-1,904,905,906,-1,907,908,909,-1,910,911,912,-1,913,914,915,-1,916,917,918,-1,919,920,921,-1,922,923,924,-1,925,926,927,-1,928,929,930,-1,931,932,933,-1,934,935,936,-1,937,938,939,-1,940,941,942,-1,943,944,945,-1,946,947,948,-1,949,950,951,-1,952,953,954,-1,955,956,957,-1,958,959,960,-1,961,962,963,-1,964,965,966,-1,967,968,969,-1,970,971,972,-1,973,974,975,-1,976,977,978,-1,979,980,981,-1,982,983,984,-1,985,986,987,-1,988,989,990,-1,991,992,993,-1,994,995,996,-1,997,998,999,-1,1000,1001,1002,-1,1003,1004,1005,-1,1006,1007,1008,-1,1009,1010,1011,-1,1012,1013,1014,-1,1015,1016,1017,-1,1018,1019,1020,-1,1021,1022,1023,-1,1024,1025,1026,-1,1027,1028,1029,-1,1030,1031,1032,-1,1033,1034,1035,-1,1036,1037,1038,-1,1039,1040,1041,-1,1042,1043,1044,-1,1045,1046,1047,-1,1048,1049,1050,-1,1051,1052,1053,-1,1054,1055,1056,-1,1057,1058,1059,-1,1060,1061,1062,-1,1063,1064,1065,-1,1066,1067,1068,-1,1069,1070,1071,-1,1072,1073,1074,-1,1075,1076,1077,-1,1078,1079,1080,-1,1081,1082,1083,-1,1084,1085,1086,-1,1087,1088,1089,-1,1090,1091,1092,-1,1093,1094,1095,-1,1096,1097,1098,-1,1099,1100,1101,-1,1102,1103,1104,-1,1105,1106,1107,-1,1108,1109,1110,-1,1111,1112,1113,-1,1114,1115,1116,-1,1117,1118,1119,-1,1120,1121,1122,-1,1123,1124,1125,-1,1126,1127,1128,-1,1129,1130,1131,-1,1132,1133,1134,-1,1135,1136,1137,-1,1138,1139,1140,-1,1141,1142,1143,-1,1144,1145,1146,-1,1147,1148,1149,-1,1150,1151,1152,-1,1153,1154,1155,-1,1156,1157,1158,-1,1159,1160,1161,-1,1162,1163,1164,-1,1165,1166,1167,-1,1168,1169,1170,-1,1171,1172,1173,-1,1174,1175,1176,-1,1177,1178,1179,-1,1180,1181,1182,-1,1183,1184,1185,-1,1186,1187,1188,-1,1189,1190,1191,-1,1192,1193,1194,-1,1195,1196,1197,-1,1198,1199,1200,-1,1201,1202,1203,-1,1204,1205,1206,-1,1207,1208,1209,-1,1210,1211,1212,-1,1213,1214,1215,-1,1216,1217,1218,-1,1219,1220,1221,-1,1222,1223,1224,-1,1225,1226,1227,-1,1228,1229,1230,-1,1231,1232,1233,-1,1234,1235,1236,-1,1237,1238,1239,-1,1240,1241,1242,-1,1243,1244,1245,-1,1246,1247,1248,-1,1249,1250,1251,-1,1252,1253,1254,-1,1255,1256,1257,-1,1258,1259,1260,-1,1261,1262,1263,-1,1264,1265,1266,-1,1267,1268,1269,-1,1270,1271,1272,-1,1273,1274,1275,-1,1276,1277,1278,-1,1279,1280,1281,-1,1282,1283,1284,-1,1285,1286,1287,-1,1288,1289,1290,-1,1291,1292,1293,-1,1294,1295,1296,-1,1297,1298,1299,-1,1300,1301,1302,-1,1303,1304,1305,-1,1306,1307,1308,-1,1309,1310,1311,-1,1312,1313,1314,-1,1315,1316,1317,-1,1318,1319,1320,-1,1321,1322,1323,-1,1324,1325,1326,-1,1327,1328,1329,-1,1330,1331,1332,-1,1333,1334,1335,-1,1336,1337,1338,-1,1339,1340,1341,-1,1342,1343,1344,-1,1345,1346,1347,-1,1348,1349,1350,-1,1351,1352,1353,-1,1354,1355,1356,-1,1357,1358,1359,-1,1360,1361,1362,-1,1363,1364,1365,-1,1366,1367,1368,-1,1369,1370,1371,-1,1372,1373,1374,-1,1375,1376,1377,-1,1378,1379,1380,-1,1381,1382,1383,-1,1384,1385,1386,-1,1387,1388,1389,-1,1390,1391,1392,-1,1393,1394,1395,-1,1396,1397,1398,-1,1399,1400,1401,-1,1402,1403,1404,-1,1405,1406,1407,-1,1408,1409,1410,-1,1411,1412,1413,-1,1414,1415,1416,-1,1417,1418,1419,-1,1420,1421,1422,-1,1423,1424,1425,-1,1426,1427,1428,-1,1429,1430,1431,-1,1432,1433,1434,-1,1435,1436,1437,-1,1438,1439,1440,-1,1441,1442,1443,-1,1444,1445,1446,-1,1447,1448,1449,-1,1450,1451,1452,-1,1453,1454,1455,-1,1456,1457,1458,-1,1459,1460,1461,-1,1462,1463,1464,-1,1465,1466,1467,-1,1468,1469,1470,-1,1471,1472,1473,-1,1474,1475,1476,-1,1477,1478,1479,-1,1480,1481,1482,-1,1483,1484,1485,-1,1486,1487,1488,-1,1489,1490,1491,-1,1492,1493,1494,-1,1495,1496,1497,-1,1498,1499,1500,-1,1501,1502,1503,-1,1504,1505,1506,-1,1507,1508,1509,-1,1510,1511,1512,-1,1513,1514,1515,-1,1516,1517,1518,-1,1519,1520,1521,-1,1522,1523,1524,-1,1525,1526,1527,-1,1528,1529,1530,-1,1531,1532,1533,-1,1534,1535,1536,-1,1537,1538,1539,-1,1540,1541,1542,-1,1543,1544,1545,-1,1546,1547,1548,-1,1549,1550,1551,-1,1552,1553,1554,-1,1555,1556,1557,-1,1558,1559,1560,-1,1561,1562,1563,-1,1564,1565,1566,-1,1567,1568,1569,-1,1570,1571,1572,-1,1573,1574,1575,-1,1576,1577,1578,-1,1579,1580,1581,-1,1582,1583,1584,-1,1585,1586,1587,-1,1588,1589,1590,-1,1591,1592,1593,-1,1594,1595,1596,-1,1597,1598,1599,-1,1600,1601,1602,-1,1603,1604,1605,-1,1606,1607,1608,-1,1609,1610,1611,-1,1612,1613,1614,-1,1615,1616,1617,-1,1618,1619,1620,-1,1621,1622,1623,-1,1624,1625,1626,-1,1627,1628,1629,-1,1630,1631,1632,-1,1633,1634,1635,-1,1636,1637,1638,-1,1639,1640,1641,-1,1642,1643,1644,-1,1645,1646,1647,-1,1648,1649,1650,-1,1651,1652,1653,-1,1654,1655,1656,-1,1657,1658,1659,-1,1660,1661,1662,-1,1663,1664,1665,-1,1666,1667,1668,-1,1669,1670,1671,-1,1672,1673,1674,-1,1675,1676,1677,-1,1678,1679,1680,-1,1681,1682,1683,-1,1684,1685,1686,-1,1687,1688,1689,-1,1690,1691,1692,-1,1693,1694,1695,-1,1696,1697,1698,-1,1699,1700,1701,-1,1702,1703,1704,-1,1705,1706,1707,-1,1708,1709,1710,-1,1711,1712,1713,-1,1714,1715,1716,-1,1717,1718,1719,-1,1720,1721,1722,-1,1723,1724,1725,-1,1726,1727,1728,-1,1729,1730,1731,-1,1732,1733,1734,-1,1735,1736,1737,-1,1738,1739,1740,-1,1741,1742,1743,-1,1744,1745,1746,-1,1747,1748,1749,-1,1750,1751,1752,-1,1753,1754,1755,-1,1756,1757,1758,-1,1759,1760,1761,-1,1762,1763,1764,-1,1765,1766,1767,-1,1768,1769,1770,-1,1771,1772,1773,-1,1774,1775,1776,-1,1777,1778,1779,-1,1780,1781,1782,-1,1783,1784,1785,-1,1786,1787,1788,-1,1789,1790,1791,-1,1792,1793,1794,-1,1795,1796,1797,-1,1798,1799,1800,-1,1801,1802,1803,-1,1804,1805,1806,-1,1807,1808,1809,-1,1810,1811,1812,-1,1813,1814,1815,-1,1816,1817,1818,-1,1819,1820,1821,-1,1822,1823,1824,-1,1825,1826,1827,-1,1828,1829,1830,-1,1831,1832,1833,-1,1834,1835,1836,-1,1837,1838,1839,-1,1840,1841,1842,-1,1843,1844,1845,-1,1846,1847,1848,-1,1849,1850,1851,-1,1852,1853,1854,-1,1855,1856,1857,-1,1858,1859,1860,-1,1861,1862,1863,-1,1864,1865,1866,-1,1867,1868,1869,-1,1870,1871,1872,-1,1873,1874,1875,-1,1876,1877,1878,-1,1879,1880,1881,-1,1882,1883,1884,-1,1885,1886,1887,-1,1888,1889,1890,-1,1891,1892,1893,-1,1894,1895,1896,-1,1897,1898,1899,-1,1900,1901,1902,-1,1903,1904,1905,-1,1906,1907,1908,-1,1909,1910,1911,-1,1912,1913,1914,-1,1915,1916,1917,-1,1918,1919,1920,-1,1921,1922,1923,-1,1924,1925,1926,-1,1927,1928,1929,-1,1930,1931,1932,-1,1933,1934,1935,-1,1936,1937,1938,-1,1939,1940,1941,-1,1942,1943,1944,-1,1945,1946,1947,-1,1948,1949,1950,-1,1951,1952,1953,-1,1954,1955,1956,-1,1957,1958,1959,-1,1960,1961,1962,-1,1963,1964,1965,-1,1966,1967,1968,-1,1969,1970,1971,-1,1972,1973,1974,-1,1975,1976,1977,-1,1978,1979,1980,-1,1981,1982,1983,-1,1984,1985,1986,-1,1987,1988,1989,-1,1990,1991,1992,-1,1993,1994,1995,-1,1996,1997,1998,-1,1999,2000,2001,-1,2002,2003,2004,-1,2005,2006,2007,-1,2008,2009,2010,-1,2011,2012,2013,-1,2014,2015,2016,-1,2017,2018,2019,-1,2020,2021,2022,-1,2023,2024,2025,-1,2026,2027,2028,-1,2029,2030,2031,-1,2032,2033,2034,-1,2035,2036,2037,-1,2038,2039,2040,-1,2041,2042,2043,-1,2044,2045,2046,-1,2047,2048,2049,-1,2050,2051,2052,-1,2053,2054,2055,-1,2056,2057,2058,-1,2059,2060,2061,-1,2062,2063,2064,-1,2065,2066,2067,-1,2068,2069,2070,-1,2071,2072,2073,-1,2074,2075,2076,-1,2077,2078,2079,-1,2080,2081,2082,-1,2083,2084,2085,-1,2086,2087,2088,-1,2089,2090,2091,-1,2092,2093,2094,-1,2095,2096,2097,-1,2098,2099,2100,-1,2101,2102,2103,-1,2104,2105,2106,-1,2107,2108,2109,-1,2110,2111,2112,-1,2113,2114,2115,-1,2116,2117,2118,-1,2119,2120,2121,-1,2122,2123,2124,-1,2125,2126,2127,-1,2128,2129,2130,-1,2131,2132,2133,-1,2134,2135,2136,-1,2137,2138,2139,-1,2140,2141,2142,-1,2143,2144,2145,-1,2146,2147,2148,-1,2149,2150,2151,-1,2152,2153,2154,-1,2155,2156,2157,-1,2158,2159,2160,-1,2161,2162,2163,-1,2164,2165,2166,-1,2167,2168,2169,-1,2170,2171,2172,-1,2173,2174,2175,-1,2176,2177,2178,-1,2179,2180,2181,-1,2182,2183,2184,-1,2185,2186,2187,-1,2188,2189,2190,-1,2191,2192,2193,-1,2194,2195,2196,-1,2197,2198,2199,-1,2200,2201,2202,-1,2203,2204,2205,-1,2206,2207,2208,-1,2209,2210,2211,-1,2212,2213,2214,-1,2215,2216,2217,-1,2218,2219,2220,-1,2221,2222,2223,-1,2224,2225,2226,-1,2227,2228,2229,-1,2230,2231,2232,-1,2233,2234,2235,-1,2236,2237,2238,-1,2239,2240,2241,-1,2242,2243,2244,-1,2245,2246,2247,-1,2248,2249,2250,-1,2251,2252,2253,-1,2254,2255,2256,-1,2257,2258,2259,-1,2260,2261,2262,-1,2263,2264,2265,-1,2266,2267,2268,-1,2269,2270,2271,-1,2272,2273,2274,-1,2275,2276,2277,-1,2278,2279,2280,-1,2281,2282,2283,-1,2284,2285,2286,-1,2287,2288,2289,-1,2290,2291,2292,-1,2293,2294,2295,-1,2296,2297,2298,-1,2299,2300,2301,-1,2302,2303,2304,-1,2305,2306,2307,-1,2308,2309,2310,-1,2311,2312,2313,-1,2314,2315,2316,-1,2317,2318,2319,-1,2320,2321,2322,-1,2323,2324,2325,-1,2326,2327,2328,-1,2329,2330,2331,-1,2332,2333,2334,-1,2335,2336,2337,-1,2338,2339,2340,-1,2341,2342,2343,-1,2344,2345,2346,-1,2347,2348,2349,-1,2350,2351,2352,-1,2353,2354,2355,-1,2356,2357,2358,-1,2359,2360,2361,-1,2362,2363,2364,-1,2365,2366,2367,-1,2368,2369,2370,-1,2371,2372,2373,-1,2374,2375,2376,-1,2377,2378,2379,-1,2380,2381,2382,-1,2383,2384,2385,-1,2386,2387,2388,-1,2389,2390,2391,-1,2392,2393,2394,-1,2395,2396,2397,-1,2398,2399,2400,-1,2401,2402,2403,-1,2404,2405,2406,-1,2407,2408,2409,-1,2410,2411,2412,-1,2413,2414,2415,-1,2416,2417,2418,-1,2419,2420,2421,-1,2422,2423,2424,-1,2425,2426,2427,-1,2428,2429,2430,-1,2431,2432,2433,-1,2434,2435,2436,-1,2437,2438,2439,-1,2440,2441,2442,-1,2443,2444,2445,-1,2446,2447,2448,-1,2449,2450,2451,-1,2452,2453,2454,-1,2455,2456,2457,-1,2458,2459,2460,-1,2461,2462,2463,-1,2464,2465,2466,-1,2467,2468,2469,-1,2470,2471,2472,-1,2473,2474,2475,-1,2476,2477,2478,-1,2479,2480,2481,-1,2482,2483,2484,-1,2485,2486,2487,-1,2488,2489,2490,-1,2491,2492,2493,-1,2494,2495,2496,-1,2497,2498,2499,-1,2500,2501,2502,-1,2503,2504,2505,-1,2506,2507,2508,-1,2509,2510,2511,-1,2512,2513,2514,-1,2515,2516,2517,-1,2518,2519,2520,-1,2521,2522,2523,-1,2524,2525,2526,-1,2527,2528,2529,-1,2530,2531,2532,-1,2533,2534,2535,-1,2536,2537,2538,-1,2539,2540,2541,-1,2542,2543,2544,-1,2545,2546,2551,-1,2550,2551,2549,-1,2551,2546,2549,-1,2549,2546,2548,-1,2547,2548,2546,-1,2555,2552,2554,-1,2553,2554,2552,-1,2567,2568,2566,-1,2568,2556,2566,-1,2566,2556,2565,-1,2558,2559,2557,-1,2560,2561,2559,-1,2559,2561,2557,-1,2561,2562,2557,-1,2562,2563,2557,-1,2563,2564,2557,-1,2565,2556,2564,-1,2557,2564,2556,-1,2570,2571,2569,-1,2571,2572,2569,-1,2572,2573,2569,-1,2573,2574,2569,-1,2574,2575,2569,-1,2575,2576,2569,-1,2576,2577,2569,-1,2577,2578,2569,-1,2578,2579,2569,-1,2579,2580,2569,-1,2580,2581,2569,-1,2581,2582,2569,-1,2582,2583,2569,-1,2583,2584,2569,-1,2584,2585,2569,-1,2585,2586,2569,-1,2586,2587,2569,-1,2587,2588,2569,-1,2612,2613,2614,-1,2615,2616,2617,-1,2618,2619,2620,-1,2633,2634,2632,-1,2634,2635,2632,-1,2636,2637,2635,-1,2638,2639,2637,-1,2639,2640,2637,-1,2642,2643,2641,-1,2623,2624,2622,-1,2628,2629,2627,-1,2630,2631,2629,-1,2631,2632,2629,-1,2629,2632,2627,-1,2632,2635,2627,-1,2627,2635,2626,-1,2635,2637,2626,-1,2637,2640,2626,-1,2643,2621,2641,-1,2626,2640,2625,-1,2640,2641,2625,-1,2641,2621,2625,-1,2624,2625,2622,-1,2622,2625,2621,-1,2656,2657,2658,-1,2659,2660,2661,-1,2662,2663,2664,-1,2665,2666,2667,-1,2668,2669,2670,-1,2671,2672,2673,-1,2674,2675,2676,-1,2677,2678,2679,-1,2682,2683,2681,-1,2685,2686,2684,-1,2686,2687,2684,-1,2687,2688,2684,-1,2689,2690,2688,-1,2694,2695,2693,-1,2695,2696,2693,-1,2696,2697,2693,-1,2701,2702,2700,-1,2680,2681,2702,-1,2684,2688,2683,-1,2688,2690,2683,-1,2683,2690,2681,-1,2690,2691,2681,-1,2691,2692,2681,-1,2692,2693,2681,-1,2697,2698,2693,-1,2681,2693,2702,-1,2698,2699,2693,-1,2702,2693,2700,-1,2699,2700,2693,-1,2860,2861,2862,-1,2872,2873,2871,-1,2871,2873,2870,-1,2870,2873,2869,-1,2875,2876,2874,-1,2878,2879,2877,-1,2880,2881,2879,-1,2882,2883,2881,-1,2885,2863,2884,-1,2864,2865,2863,-1,2866,2867,2865,-1,2868,2869,2867,-1,2869,2873,2867,-1,2876,2877,2874,-1,2879,2881,2877,-1,2881,2883,2877,-1,2883,2884,2877,-1,2865,2867,2863,-1,2867,2873,2863,-1,2873,2874,2863,-1,2863,2874,2884,-1,2877,2884,2874,-1,2926,2677,2927,-1,2679,2858,2677,-1,2858,2857,2677,-1,2677,2857,2927,-1,2857,2852,2927,-1,2852,2851,2927,-1,2851,2850,2927,-1,2848,2861,2849,-1,2848,2847,2860,-1,2846,2789,2847,-1,2789,2788,2847,-1,2849,2861,2850,-1,2860,2847,2861,-1,2788,2927,2847,-1,2850,2861,2927,-1,2847,2927,2861,-1,3021,3022,3023,-1,3024,3025,3026,-1,3027,3028,3029,-1,3030,3031,3032,-1,3033,3034,3035,-1,3036,3037,3038,-1,3039,3040,3041,-1,3042,3043,3044,-1,3045,3046,3047,-1,3048,3049,3050,-1,3051,3052,3053,-1,3054,3055,3056,-1,3057,3058,3059,-1,3060,3061,3062,-1,3063,3064,3065,-1,3066,3067,3068,-1,3069,3070,3071,-1,3072,3073,3074,-1,3025,3024,3023,-1,2,2859,3040,-1,2858,2679,2859,-1,3023,3024,3021,-1,3021,3024,3022,-1,3022,3024,3023,-1,3023,3024,2679,-1,2679,3024,2859,-1,3040,2859,3037,-1,3037,2859,3038,-1,3035,3038,3033,-1,3038,2859,3033,-1,3033,2859,3031,-1,3031,2859,3032,-1,2859,3024,3032,-1,3024,3028,3032,-1,3027,3032,3028,-1,3075,3076,3077,-1,3078,3079,3080,-1,3081,3082,3083,-1,3084,3085,3086,-1,3087,3088,3089,-1,3090,3091,3092,-1,2614,2616,2612,-1,2618,2654,2619,-1,2657,2656,2653,-1,2653,2652,2656,-1,2651,2650,2652,-1,2649,2661,2650,-1,2612,2616,2569,-1,2619,2654,2615,-1,2653,2656,2654,-1,2652,2650,2656,-1,2661,1,2650,-1,1,2570,2650,-1,2569,2616,2570,-1,2654,2656,2615,-1,2656,2650,2615,-1,2570,2616,2650,-1,2615,2650,2616,-1,2675,2671,2611,-1,2672,2670,2671,-1,2611,2671,2569,-1,2671,2670,2569,-1,2569,2670,2614,-1,2670,3091,2614,-1,2614,3091,2616,-1,3091,3087,2616,-1,3093,3094,3095,-1,3096,3097,3098,-1,3099,3100,3101,-1,3102,3103,3104,-1,3105,3106,3107,-1,3108,3109,3110,-1,3111,3112,3113,-1,3114,3115,3116,-1,3117,3118,3119,-1,3120,3121,3122,-1,3123,3124,3125,-1,3126,3127,3128,-1,3129,3130,3131,-1,3132,3133,3134,-1,3135,3136,3137,-1,3138,3139,3140,-1,3141,3142,3143,-1,3144,3145,3146,-1,3147,3148,3149,-1,3150,3151,3152,-1,3153,3154,3155,-1,3156,3157,3158,-1,3159,3160,3161,-1,3162,3163,3164,-1,3165,3166,3167,-1,3168,3169,3170,-1,3171,3172,3173,-1,3174,3175,3176,-1,3177,3178,3179,-1,3180,3181,3182,-1,3183,3184,3185,-1,3186,3187,3188,-1,3189,3190,3191,-1,3192,3193,3194,-1,3195,3196,3197,-1,3198,3199,3200,-1,3201,3202,3203,-1,3204,3205,3206,-1,3207,3208,3209,-1,3210,3211,3212,-1,3213,3214,3215,-1,3216,3217,3218,-1,3219,3220,3221,-1,3222,3223,3224,-1,3225,3226,3227,-1,3228,3229,3230,-1,3231,3232,3233,-1,3234,3235,3236,-1,3237,3238,3239,-1,3240,3241,3242,-1,3243,3244,3245,-1,3246,3247,3248,-1,3249,3250,3251,-1,3252,3253,3254,-1,3255,3256,3257,-1,3258,3259,3260,-1,3261,3262,3263,-1,3264,3265,3266,-1,3267,3268,3269,-1,3270,3271,3272,-1,3273,3274,3275,-1,3276,3277,3278,-1,3279,3280,3281,-1,3282,3283,3284,-1,3285,3286,3287,-1,3288,3289,3290,-1,3291,3292,3293,-1,3294,3295,3296,-1,3297,3298,3299,-1,3300,3301,3302,-1,3303,3304,3305,-1,3306,3307,3308,-1,3309,3310,3311,-1,3312,3313,3314,-1,3315,3316,3317,-1,3318,3319,3320,-1,3321,3322,3323,-1,3324,3325,3326,-1,3327,3328,3329,-1,3330,3331,3332,-1,3333,3334,3335,-1,3336,3337,3338,-1,3339,3340,3341,-1,3342,3343,3344,-1,3345,3346,3347,-1,3348,3349,3350,-1,3351,3352,3353,-1,3354,3355,3356,-1,3357,3358,3359,-1,3360,3361,3362,-1,3363,3364,3365,-1,3366,3367,3368,-1,3369,3370,3371,-1,3372,3373,3374,-1,3375,3376,3377,-1,3378,3379,3380,-1,3381,3382,3383,-1,3384,3385,3386,-1,3387,3388,3389,-1,3390,3391,3392,-1,3393,3394,3395,-1,3396,3397,3398,-1,3399,3400,3401,-1,3402,3403,3404,-1,3405,3406,3407,-1,3408,3409,3410,-1,3411,3412,3413,-1,3414,3415,3416,-1,3417,3418,3419,-1,3420,3421,3422,-1,3423,3424,3425,-1,3426,3427,3428,-1,3429,3430,3431,-1,3432,3433,3434,-1,3435,3436,3437,-1,3438,3439,3440,-1,3441,3442,3443,-1,3444,3445,3446,-1,3447,3448,3449,-1,3450,3451,3452,-1,3453,3454,3455,-1,3456,3457,3458,-1,3459,3460,3461,-1,3462,3463,3464,-1,3465,3466,3467,-1,3468,3469,3470,-1,3471,3472,3473,-1,3474,3475,3476,-1,3477,3478,3479,-1,3480,3481,3482,-1,3483,3484,3485,-1,3486,3487,3488,-1,3489,3490,3491,-1,3492,3493,3494,-1,3495,3496,3497,-1,3498,3499,3500,-1,3501,3502,3503,-1,3504,3505,3506,-1,3507,3508,3509,-1,3510,3511,3512,-1,3513,3514,3515,-1,3516,3517,3518,-1,3519,3520,3521,-1,3522,3523,3524,-1,3525,3526,3527,-1,3528,3529,3530,-1,3531,3532,3533,-1,3534,3535,3536,-1,3537,3538,3539,-1,3540,3541,3542,-1,3543,3544,3545,-1,3546,3547,3548,-1,3549,3550,3551,-1,3552,3553,3554,-1,3555,3556,3557,-1,3558,3559,3560,-1,3561,3562,3563,-1,3564,3565,3566,-1,3567,3568,3569,-1,3570,3571,3572,-1,3573,3574,3575,-1,3576,3577,3578,-1,3579,3580,3581,-1,3582,3583,3584,-1,3585,3586,3587,-1,3588,3589,3590,-1,3591,3592,3593,-1,3594,3595,3596,-1,3597,3598,3599,-1,3600,3601,3602,-1,3603,3604,3605,-1,3606,3607,3608,-1,3609,3610,3611,-1,3612,3613,3614,-1,3615,3616,3617,-1,3618,3619,3620,-1,3621,3622,3623,-1,3624,3625,3626,-1,3627,3628,3629,-1,3630,3631,3632,-1,3633,3634,3635,-1,3636,3637,3638,-1,3639,3640,3641,-1,3642,3643,3644,-1,3645,3646,3647,-1,3648,3649,3650,-1,3651,3652,3653,-1,3654,3655,3656,-1,3657,3658,3659,-1,3660,3661,3662,-1,3663,3664,3665,-1,3666,3667,3668,-1,3669,3670,3671,-1,3672,3673,3674,-1,3675,3676,3677,-1,3678,3679,3680,-1,3681,3682,3683,-1,3684,3685,3686,-1,3687,3688,3689,-1,3690,3691,3692,-1,3693,3694,3695,-1,3696,3697,3698,-1,3699,3700,3701,-1,3702,3703,3704,-1,3705,3706,3707,-1,3708,3709,3710,-1,3711,3712,3713,-1,3714,3715,3716,-1,3717,3718,3719,-1,3720,3721,3722,-1,3723,3724,3725,-1,3726,3727,3728,-1,3729,3730,3731,-1,3732,3733,3734,-1,3735,3736,3737,-1,3738,3739,3740,-1,3741,3742,3743,-1,3744,3745,3746,-1,3747,3748,3749,-1,3750,3751,3752,-1,3753,3754,3755,-1,3756,3757,3758,-1,3759,3760,3761,-1,3762,3763,3764,-1,3765,3766,3767,-1,3768,3769,3770,-1,3771,3772,3773,-1,3774,3775,3776,-1,3777,3778,3779,-1,3780,3781,3782,-1,3783,3784,3785,-1,3786,3787,3788,-1,3789,3790,3791,-1,3792,3793,3794,-1,3795,3796,3797,-1,3798,3799,3800,-1,3801,3802,3803,-1,3804,3805,3806,-1,3807,3808,3809,-1,3810,3811,3812,-1,3813,3814,3815,-1,3816,3817,3818,-1,3819,3820,3821,-1,3822,3823,3824,-1,3825,3826,3827,-1,3828,3829,3830,-1,3831,3832,3833,-1,3834,3835,3836,-1,3837,3838,3839,-1,3840,3841,3842,-1,3843,3844,3845,-1,3846,3847,3848,-1,3849,3850,3851,-1,3852,3853,3854,-1,3855,3856,3857,-1,3858,3859,3860,-1,3861,3862,3863,-1,3864,3865,3866,-1,3867,3868,3869,-1,3870,3871,3872,-1,3873,3874,3875,-1,3876,3877,3878,-1,3879,3880,3881,-1,3882,3883,3884,-1,3885,3886,3887,-1,3888,3889,3890,-1,3891,3892,3893,-1,3894,3895,3896,-1,3897,3898,3899,-1,3900,3901,3902,-1,3903,3904,3905,-1,3906,3907,3908,-1,3909,3910,3911,-1,3912,3913,3914,-1,3915,3916,3917,-1,3918,3919,3920,-1,3921,3922,3923,-1,3924,3925,3926,-1,3927,3928,3929,-1,3930,3931,3932,-1,3933,3934,3935,-1,3936,3937,3938,-1,3939,3940,3941,-1,3942,3943,3944,-1,3945,3946,3947,-1,3948,3949,3950,-1,3951,3952,3953,-1,3954,3955,3956,-1,3957,3958,3959,-1,3960,3961,3962,-1,3963,3964,3965,-1,3966,3967,3968,-1,3969,3970,3971,-1,3972,3973,3974,-1,3975,3976,3977,-1,3978,3979,3980,-1,3981,3982,3983,-1,3984,3985,3986,-1,3987,3988,3989,-1,3990,3991,3992,-1,3993,3994,3995,-1,3996,3997,3998,-1,3999,4000,4001,-1,4002,4003,4004,-1,4005,4006,4007,-1,4008,4009,4010,-1,4011,4012,4013,-1,4014,4015,4016,-1,4017,4018,4019,-1,4020,4021,4022,-1,4023,4024,4025,-1,4026,4027,4028,-1,4029,4030,4031,-1,4032,4033,4034,-1,4035,4036,4037,-1,4038,4039,4040,-1,4041,4042,4043,-1,4044,4045,4046,-1,4047,4048,4049,-1,4050,4051,4052,-1,4053,4054,4055,-1,4056,4057,4058,-1,4059,4060,4061,-1,4062,4063,4064,-1,4065,4066,4067,-1,4068,4069,4070,-1,4071,4072,4073,-1,4074,4075,4076,-1,4077,4078,4079,-1,4080,4081,4082,-1,4083,4084,4085,-1,4086,4087,4088,-1,4089,4090,4091,-1,4092,4093,4094,-1,4095,4096,4097,-1,4098,4099,4100,-1,4101,4102,4103,-1,4104,4105,4106,-1,4107,4108,4109,-1,4110,4111,4112,-1,4113,4114,4115,-1,4116,4117,4118,-1,4119,4120,4121,-1,4122,4123,4124,-1,4125,4126,4127,-1,4128,4129,4130,-1,4131,4132,4133,-1,4134,4135,4136,-1,4137,4138,4139,-1,4140,4141,4142,-1,4143,4144,4145,-1,4146,4147,4148,-1,4149,4150,4151,-1,4152,4153,4154,-1,4155,4156,4157,-1,4158,4159,4160,-1,4161,4162,4163,-1,4164,4165,4166,-1,4167,4168,4169,-1,4170,4171,4172,-1,4173,4174,4175,-1,4176,4177,4178,-1,4179,4180,4181,-1,4182,4183,4184,-1,4185,4186,4187,-1,4188,4189,4190,-1,4191,4192,4193,-1,4194,4195,4196,-1,4197,4198,4199,-1,4200,4201,4202,-1,4203,4204,4205,-1,4206,4207,4208,-1,4209,4210,4211,-1,4212,4213,4214,-1,4215,4216,4217,-1,4218,4219,4220,-1,4221,4222,4223,-1,4224,4225,4226,-1,4227,4228,4229,-1,4230,4231,4232,-1,4233,4234,4235,-1,4236,4237,4238,-1,4239,4240,4241,-1,4242,4243,4244,-1,4245,4246,4247,-1,4248,4249,4250,-1,4251,4252,4253,-1,4254,4255,4256,-1,4257,4258,4259,-1,4260,4261,4262,-1,4263,4264,4265,-1,4266,4267,4268,-1,4269,4270,4271,-1,4272,4273,4274,-1,4275,4276,4277,-1,4278,4279,4280,-1,4281,4282,4283,-1,4284,4285,4286,-1,4287,4288,4289,-1,4290,4291,4292,-1,4293,4294,4295,-1,4296,4297,4298,-1,4299,4300,4301,-1,4302,4303,4304,-1,4305,4306,4307,-1,4308,4309,4310,-1,4311,4312,4313,-1,4314,4315,4316,-1,4317,4318,4319,-1,4320,4321,4322,-1,4323,4324,4325,-1,4326,4327,4328,-1,4329,4330,4331,-1,4332,4333,4334,-1,4335,4336,4337,-1,4338,4339,4340,-1,4341,4342,4343,-1,4344,4345,4346,-1,4347,4348,4349,-1,4350,4351,4352,-1,4353,4354,4355,-1,4356,4357,4358,-1,4359,4360,4361,-1,4362,4363,4364,-1,4365,4366,4367,-1,4368,4369,4370,-1,4371,4372,4373,-1,4374,4375,4376,-1,4377,4378,4379,-1,4380,4381,4382,-1,4383,4384,4385,-1,4386,4387,4388,-1,4389,4390,4391,-1,4392,4393,4394,-1,4395,4396,4397,-1,4398,4399,4400,-1,4401,4402,4403,-1,4404,4405,4406,-1,4407,4408,4409,-1,4410,4411,4412,-1,4413,4414,4415,-1,4416,4417,4418,-1,4419,4420,4421,-1,4422,4423,4424,-1,4425,4426,4427,-1,4428,4429,4430,-1,4431,4432,4433,-1,4434,4435,4436,-1,4437,4438,4439,-1,4440,4441,4442,-1,4443,4444,4445,-1,4446,4447,4448,-1,4449,4450,4451,-1,4452,4453,4454,-1,4455,4456,4457,-1,4458,4459,4460,-1,4461,4462,4463,-1,4464,4465,4466,-1,4467,4468,4469,-1,4470,4471,4472,-1,4473,4474,4475,-1,4476,4477,4478,-1,4479,4480,4481,-1,4482,4483,4484,-1,4485,4486,4487,-1,4488,4489,4490,-1,4491,4492,4493,-1,4494,4495,4496,-1,4497,4498,4499,-1,4500,4501,4502,-1,4503,4504,4505,-1,4506,4507,4508,-1,4509,4510,4511,-1,4512,4513,4514,-1,4515,4516,4517,-1,4518,4519,4520,-1,4521,4522,4523,-1,4524,4525,4526,-1,4527,4528,4529,-1,4530,4531,4532,-1,4533,4534,4535,-1,4536,4537,4538,-1,4539,4540,4541,-1,4542,4543,4544,-1,4545,4546,4547,-1,4548,4549,4550,-1,4551,4552,4553,-1,4554,4555,4556,-1,4557,4558,4559,-1,4560,4561,4562,-1,4563,4564,4565,-1,4566,4567,4568,-1,4569,4570,4571,-1,4572,4573,4574,-1,4575,4576,4577,-1,4578,4579,4580,-1,4581,4582,4583,-1,4584,4585,4586,-1,4587,4588,4589,-1,4590,4591,4592,-1,4593,4594,4595,-1,4596,4597,4598,-1,4599,4600,4601,-1,4602,4603,4604,-1,4605,4606,4607,-1,4608,4609,4610,-1,4611,4612,4613,-1,4614,4615,4616,-1,4617,4618,4619,-1,4620,4621,4622,-1,4623,4624,4625,-1,4626,4627,4628,-1,4629,4630,4631,-1,4632,4633,4634,-1,4635,4636,4637,-1,4638,4639,4640,-1,4641,4642,4643,-1,4644,4645,4646,-1,4647,4648,4649,-1,4650,4651,4652,-1,4653,4654,4655,-1,4656,4657,4658,-1,4659,4660,4661,-1,4662,4663,4664,-1,4665,4666,4667,-1,4668,4669,4670,-1,4671,4672,4673,-1,4674,4675,4676,-1,4677,4678,4679,-1,4680,4681,4682,-1,4683,4684,4685,-1,4686,4687,4688,-1,4689,4690,4691,-1,4692,4693,4694,-1,4695,4696,4697,-1,4698,4699,4700,-1,4701,4702,4703,-1,4704,4705,4706,-1,4707,4708,4709,-1,4710,4711,4712,-1,4713,4714,4715,-1,4716,4717,4718,-1,4719,4720,4721,-1,4722,4723,4724,-1,4725,4726,4727,-1,4728,4729,4730,-1,4731,4732,4733,-1,4734,4735,4736,-1,4737,4738,4739,-1,4740,4741,4742,-1,4743,4744,4745,-1,4746,4747,4748,-1,4749,4750,4751,-1,4752,4753,4754,-1,4755,4756,4757,-1,4758,4759,4760,-1,4761,4762,4763,-1,4764,4765,4766,-1,4767,4768,4769,-1,4770,4771,4772,-1,4773,4774,4775,-1,4776,4777,4778,-1,4779,4780,4781,-1,4782,4783,4784,-1,4785,4786,4787,-1,4788,4789,4790,-1,4791,4792,4793,-1,4794,4795,4796,-1,4797,4798,4799,-1,4800,4801,4802,-1,4803,4804,4805,-1,4806,4807,4808,-1,4809,4810,4811,-1,4812,4813,4814,-1,4815,4816,4817,-1,4818,4819,4820,-1,4821,4822,4823,-1,4824,4825,4826,-1,4827,4828,4829,-1,4830,4831,4832,-1,4833,4834,4835,-1,4836,4837,4838,-1,4839,4840,4841,-1,4842,4843,4844,-1,4845,4846,4847,-1,4848,4849,4850,-1,4851,4852,4853,-1,4854,4855,4856,-1,4857,4858,4859,-1,4860,4861,4862,-1,4863,4864,4865,-1,4866,4867,4868,-1,4869,4870,4871,-1,4872,4873,4874,-1,4875,4876,4877,-1,4878,4879,4880,-1,4881,4882,4883,-1,4884,4885,4886,-1])
IndexedFaceSet406.setCreaseAngle(1.59)
Coordinate407 = Coordinate()
Coordinate407.setPoint([0.89,4.4,0.99,0.77,4.4,1.1,0.83,4.36,1.14,0.68,4.36,1.12,0.7,4.36,1.15,0.77,4.4,1.1,0.7,4.36,1.15,0.71,4.36,1.17,0.77,4.4,1.1,0.6,4.32,1.18,0.68,4.36,1.12,0.67,4.4,1.06,0.67,4.4,1.06,0.68,4.36,1.12,0.77,4.4,1.1,0.67,4.4,1.06,0.77,4.4,1.1,0.78,4.44,1.05,0.59,4.4,1,0.4,4.24,1.06,0.6,4.32,1.18,1,4.32,1.01,0.89,4.4,0.99,0.83,4.36,1.14,0.83,4.36,1.14,0.77,4.4,1.1,0.78,4.36,1.18,0.71,4.36,1.17,0.64,4.32,1.23,0.7,4.32,1.29,0.71,4.36,1.17,0.7,4.32,1.29,0.78,4.36,1.27,0.71,4.36,1.17,0.7,4.36,1.15,0.64,4.32,1.23,0.62,4.32,1.2,0.64,4.32,1.23,0.7,4.36,1.15,0.6,4.32,1.18,0.67,4.4,1.06,0.59,4.4,1,0.89,4.4,0.99,0.78,4.44,1.05,0.77,4.4,1.1,0.87,4.32,1.17,1,4.32,1.01,0.83,4.36,1.14,0.81,4.32,1.24,0.85,4.32,1.2,0.78,4.36,1.27,-0.91,-1,0.37,-0.82,-1,0.63,-0.7,-1.16,-0.84,0.41,-1.04,-1.34,-0.82,-1.04,-0.58,-0.83,-0.96,-0.36,-0.66,-0.88,-0.94,-0.68,-1.08,-1.02,-0.9,-1.08,1.01,-0.78,-1.12,1.04,-0.91,-0.92,0.04,-0.84,-0.92,0.97,-0.8,-1.08,-0.65,-0.77,-0.92,-0.7,0.3,-1,1.47,-0.73,-1.08,-1.18,-0.65,-0.92,1.25,-0.66,-0.92,1.19,-0.68,-1.04,1.16,-0.61,-1.04,1.37,-0.61,-0.92,1.37,0.35,-1,-1.59,0.23,-0.96,-1.33,0.26,-0.72,-1.5,-0.61,-1.08,-1.19,-0.78,-0.92,-1.22,-0.69,-0.96,-1.26,-0.71,-1,-1.16,-0.81,-1.04,-0.62,-0.81,-0.96,-0.58,-0.93,-0.88,-0.17,-0.86,-0.92,0.48,-0.81,-0.88,0.59,-0.85,-0.84,0.47,-0.71,-1,1.03,-0.68,-0.84,1.09,-0.7,-0.88,1.03,-0.68,-0.92,1.12,-0.71,-0.92,-1.1,-0.73,-0.88,-0.79,-0.76,-0.84,-0.72,-0.78,-0.8,-0.53,-0.78,-0.8,-0.64,-0.8,-0.84,0.98,-0.8,-0.84,0.91,-0.66,-0.88,1.29,0.28,-0.84,1.56,-0.76,-0.84,1,-0.65,-0.88,1.21,-0.71,-0.88,1.37,0.18,-0.72,-1.41,-0.85,-0.88,-1.17,-0.88,-0.84,-1.26,-0.9,-0.8,-0.18,-0.86,-0.84,0.45,-0.83,-0.8,0.5,-0.8,-0.8,0.77,-0.67,-0.88,1.15,0.31,-0.8,1.5,-0.79,-0.84,1.38,0.32,-0.64,1.49,-0.81,-0.92,-1.28,-0.95,-0.72,-1.16,-0.84,-0.88,-1.13,-0.91,-0.84,-1.13,-0.97,-0.8,-0.99,-0.76,-0.84,-0.81,-0.92,-0.8,0.01,-0.88,-0.8,0.38,-0.96,-0.76,0.41,-0.86,-0.8,0.44,-0.78,-0.8,0.94,-0.71,-0.84,1,-0.75,-0.84,1.26,-0.81,-0.8,-0.7,-0.93,-0.8,-0.16,-1.02,-0.76,-0.08,-0.94,-0.76,0.5,-0.86,-0.8,0.92,-0.84,-0.8,1.01,-0.8,-0.8,1.06,-0.8,-0.84,1.33,-0.86,-0.8,1.32,-0.77,-0.16,-1.2,0.26,-0.52,-1.37,-1.02,-0.44,-0.87,-0.96,-0.8,-0.91,-1.04,-0.68,-0.97,-0.98,-0.76,-0.22,-1,-0.76,0.13,-0.93,-0.76,1.23,-0.88,-0.8,1.2,-0.95,-0.68,1.24,-1.05,-0.76,-0.55,-1.11,-0.72,-0.48,-1.1,-0.72,-0.63,-1.04,-0.76,-0.73,-1,-0.76,0.59,-1.01,-0.76,0.63,-1.08,-0.72,0.63,-1.07,-0.72,0.7,-0.98,-0.76,0.67,-0.98,-0.76,0.76,-1,-0.76,0.8,-1.06,-0.72,0.76,-1.11,-0.6,0.65,-0.98,-0.36,1,-1.11,0,0.54,-0.96,-0.76,1.1,-1.05,-0.64,0.97,-1.03,-0.76,-0.84,-1.14,-0.72,-0.23,-1.15,-0.56,-0.43,-1.18,-0.4,0.04,-1.16,-0.2,-0.13,-1.11,-0.72,0.43,-1.18,-0.64,0.22,-1.14,-0.72,0.13,-1.19,-0.64,-0.12,-1.07,-0.68,0.85,-1.05,-0.04,-0.7,0.29,-0.48,1.49,-1.14,0.12,0.38,0.27,-0.32,1.52,-0.79,0.2,1.34,-0.86,0.16,1.06,-0.19,0,1.51,-1.11,0.16,-0.4,-1.13,0.6,0.34,0.46,-0.12,-1.66,0.22,-0.04,-1.51,-1.1,0.04,-0.5,0.29,0,1.49,0.26,0.04,-1.51,0.37,0.28,-1.54,0.17,0,-1.47,0.21,0.28,-1.44,-0.94,0,-0.96,0.29,0.12,1.62,-1.06,0.16,-0.59,0.28,0.68,-1.27,0.35,0.44,-1.52,0.27,0.24,1.63,-0.67,0.44,1.34,-1.07,0.2,-0.56,-1.05,0.32,-0.58,-1.07,0.24,-0.52,-1.09,0.52,-0.42,-0.95,0.52,0.83,-1.07,0.76,0.44,-1.04,0.16,-0.69,0.23,0.36,1.66,-1.06,0.2,-0.59,-0.79,0.56,1.27,-0.92,0.56,1.07,-0.84,0.28,1.27,-1.06,0.24,-0.56,-1,0.64,-0.73,-0.87,1.08,-0.94,-0.69,0.96,-1.14,-0.94,0.48,-0.88,0.36,0.56,1.34,-0.92,0.92,1.07,-0.61,0.84,1.22,-0.53,1.04,1.31,-0.92,0.72,1.11,-0.51,0.64,1.29,-0.95,0.68,0.94,0.29,0.92,1.59,-0.48,1.2,1.53,0.42,0.76,-1.58,-1.11,1.12,0.14,-0.62,1.24,1.23,0.26,1.08,1.57,-0.96,1.04,0.99,-0.58,1.24,1.35,0.33,0.84,-1.5,0.42,1.24,-1.41,0.36,1.04,-1.51,-0.95,1.2,-0.81,-0.87,1.16,-0.94,-1.03,1.4,-0.56,0.27,0.91,1.51,-0.58,1.4,1.46,-0.8,1.2,-1.03,-0.79,1.44,1.05,-0.94,1.4,0.94,-0.85,1.16,-0.96,-0.85,1.2,-0.96,-1.01,1.2,0.65,0.4,1.44,-1.49,-0.69,1.36,-1.29,-1,1.56,0.76,0.29,1.52,1.49,-1.07,1.72,0.06,-0.96,2.12,-0.75,-0.87,1.48,-0.98,-0.9,1.28,-0.89,0.29,1.74,1.45,0.5,1.6,-1.46,-0.36,1.52,1.41,-0.81,1.6,1.03,-0.79,1.68,1.2,0.45,1.52,-1.46,-0.66,1.72,-1.35,-0.89,2.16,-1.03,-0.79,2.2,-1.26,-1.03,1.84,0.59,-0.58,1.56,1.42,-0.28,1.72,-1.42,-0.99,2.32,0.21,0.22,2.16,1.39,0.22,2.06,1.67,-0.51,2,-1.38,-0.7,1.64,1.36,-0.85,1.96,1.2,-0.91,2.04,1.06,-0.71,1.72,1.33,-0.51,1.8,1.33,-0.79,1.8,1.27,0.23,2.31,1.61,-1.01,2.04,0.69,-0.5,2,1.33,-0.66,2.24,-1.39,-0.91,2.28,1.1,-0.88,2.52,-0.68,-0.89,2.32,-1.03,-0.99,2.44,0.56,-0.7,2.64,1.21,0.19,2.43,1.63,0.23,2.56,1.51,-0.83,2.28,-1.18,-0.96,2.28,0.99,-0.78,2.88,0.31,-0.97,2.48,0.74,-0.85,2.36,-1.12,-0.86,2.48,-0.97,-0.85,2.32,-1.12,-0.85,2.6,0.98,-0.8,2.4,-1.19,-0.52,2.6,-1.39,-0.59,2.84,1.24,-0.83,2.36,-1.14,-0.82,2.4,-1.13,-0.77,2.56,-1.09,-0.3,3.04,1.55,-0.8,2.84,0.06,-0.67,2.8,-1,-0.52,2.92,-1.23,-0.49,2.76,-1.37,0.21,2.96,1.52,-0.38,2.76,-1.47,-0.54,3.36,-0.19,-0.78,2.8,0.86,-0.37,2.8,-1.46,-0.74,2.92,0.57,-0.64,3.04,0.69,-0.35,2.84,-1.48,-0.39,2.92,-1.39,-0.6,3.04,0.92,-0.69,3,0.58,-0.25,3.08,-1.48,-0.32,3.28,-1.18,-0.69,3,0.54,-0.29,3.68,-0.3,-0.09,3.84,-0.59,0.21,3.44,1.5,-0.66,3.04,0.56,-0.54,3.2,0.62,-0.14,3.24,-1.58,-0.64,3.08,0.51,-0.65,3.16,0.15,-0.11,3.92,0.5,-0.23,3.8,0.26,-0.01,3.64,-1.35,-0.34,3.72,-0.03,0.1,3.92,-0.87,0.27,4.04,-1,0.39,4.08,-1.45,-0.2,3.88,-0.3,-0.34,3.8,-0.15,-0.26,3.88,0.03,0.05,3.88,1.34,-0.01,3.76,1.52,0.01,4.04,-0.56,-0.1,3.96,-0.34,-0.17,4.08,-0.32,0.09,4.04,0.81,0.01,4.12,0.57,-0.08,4.04,0.43,0.19,3.88,1.52,-0.07,4.28,0.52,0.11,4.2,0.68,0.48,4.16,-1.22,0.37,4.24,-1,0.09,4.04,-0.72,-0.22,3.88,-0.24,-0.12,3.92,-0.23,-0.27,3.84,-0.24,-0.19,3.92,0.3,0.18,4.08,-0.84,-0.29,3.88,-0.14,-0.13,4.16,-0.51,-0.07,4.2,-0.39,-0.25,3.88,-0.22,-0.19,3.92,-0.14,-0.21,3.92,0.17,-0.12,3.96,0.18,-0.1,3.92,-0.29,-0.12,4,-0.19,-0.14,3.92,-0.17,-0.12,3.96,0.14,-0.13,3.96,0.12,-0.08,4,0.27,-0.2,4.08,0.32,-0.21,4.12,0.35,0.42,4.16,1.6,0.54,4.16,-1.55,-0.14,3.96,-0.1,-0.17,4.08,0.21,0.14,4.08,-0.68,0.17,4.12,-0.69,-0.14,4.04,-0.09,-0.2,4.04,0.06,-0.24,4.04,0.12,-0.16,4,0.14,0.19,4.16,-0.71,0.24,4.12,-0.83,-0.11,4.16,-0.57,-0.04,4.2,-0.28,0.31,4.32,0.83,0.06,4.36,0.68,0.4,4.24,1.06,0.46,4.24,1.31,0.54,4.17,1.2,0.52,4.16,-1.45,0.06,4.12,-0.63,0,4.4,-0.4,-0.11,4.08,0.09,-0.2,4.12,0.27,-0.15,4.2,0.39,-0.13,4.16,0.48,0.3,4.16,-0.9,0.02,4.2,-0.74,0.13,4.16,-0.72,-0.02,4.24,-0.7,-0.12,4.12,0.2,0.01,4.28,0.38,0.25,4.08,1.43,0.6,4.2,-1.35,0.61,4.2,-1.42,0.63,4.24,-1.21,0.53,4.28,-1.02,0.3,4.16,-0.85,0.29,4.16,-0.79,0.07,4.2,-0.77,-0.17,4.16,0.32,0.67,4.24,-1.29,-0.11,4.2,-0.54,-0.07,4.16,0.32,0.55,4.28,1.28,0.54,4.24,1.44,0.57,4.28,1.34,0.67,4.28,-1.13,0.22,4.2,-0.89,0.21,4.28,-0.9,-0.04,4.28,-0.6,0.07,4.32,-0.46,0.03,4.32,-0.69,0.04,4.32,0.47,0.02,4.36,0.6,0.5,4.2,1.54,0.04,4.14,1.44,0.79,4.24,1.49,0.02,4.1,1.53,0.62,4.32,1.2,0.64,4.32,1.23,0.6,4.32,1.18,0.74,4.32,-1.08,0.65,4.32,-1,0.72,4.28,-1.17,0.75,4.32,1.37,0.67,4.32,1.31,0.54,4.32,-0.97,-0.78,-0.92,-1.22,-0.25,3.88,-0.22,-0.11,4.08,0.09,0.23,-0.96,-1.33,0.07,4.2,-0.77,-0.54,-1.02,1.38,-0.47,-1.01,1.4,-0.4,-1,1.41,-0.33,-0.98,1.43,-0.26,-0.97,1.44,-0.19,-0.95,1.45,-0.12,-0.94,1.47,-0.05,-0.92,1.48,0.02,-0.91,1.5,0.09,-0.89,1.51,0.16,-0.88,1.53,0.23,-0.86,1.54,0.3,-0.85,1.55,0.37,-0.84,1.57,0.44,-0.82,1.58,0.51,-0.81,1.6,0.58,-0.79,1.61,0.65,-0.78,1.63,0.71,-0.76,1.64,0.79,-0.75,1.66,0.78,-0.5,1.65,0.77,-0.25,1.64,0.77,0,1.63,0.76,0.25,1.62,0.76,0.5,1.62,0.75,0.75,1.61,0.86,1,1.6,0.86,1.25,1.59,0.85,1.5,1.58,0.85,1.75,1.58,0.84,2,1.57,0.84,2.24,1.56,0.83,2.49,1.55,0.83,2.74,1.54,0.82,2.99,1.54,0.81,3.24,1.53,0.81,3.49,1.52,0.8,3.74,1.51,0.8,3.99,1.5,2.04,-1.16,-0.61,2.17,-1,-0.45,2.09,-1.16,-0.4,2.19,-0.8,-0.09,2.17,-1.04,-0.19,2.14,-0.72,-0.31,2.14,-1.08,-0.11,2.12,-1.08,-0.01,2.03,-1.12,-0.03,2.12,-1.12,-0.24,2.13,-1.12,-0.35,2,-0.64,-0.88,2.09,-1.12,-0.68,1.91,-0.8,-1.32,2.01,-0.92,-1.1,1.79,-1.08,-1.27,2.1,-1.04,0.15,2.19,-0.88,0.13,2.11,-0.96,0.37,2.05,-1.04,0.3,1.98,-0.4,-0.5,2.07,-1.16,-0.33,2.01,-1.12,-0.95,2.09,-1,-0.91,1.96,-1.04,0.4,2.08,-0.96,0.49,2.15,-0.64,0.45,2.08,-0.92,0.62,1.73,-1,-1.38,1.97,-0.76,-1.15,1.65,-0.96,-1.41,1.68,-0.96,-1.42,1.64,-0.96,-1.38,2,-0.96,0.6,1.99,-0.36,-0.4,2.01,-0.36,-0.27,1.79,-0.88,-1.46,1.59,-0.92,-1.46,1.62,-0.92,-1.48,2.09,-0.84,0.71,1.97,-0.92,0.77,1.55,-0.88,-1.53,1.55,-0.92,-1.61,1.64,-0.92,-1.5,1.54,-0.88,-1.46,2,-0.88,0.79,1.98,-0.84,0.89,1.93,-0.88,0.85,1.92,-0.8,1.07,1.88,-0.84,1.04,2,-0.32,-0.07,1.67,-0.92,-1.53,1.76,-0.76,-1.55,1.32,-0.32,-1.68,1.72,-0.8,1.34,1.66,-0.76,1.49,1.62,-0.8,1.45,1.73,-0.56,1.47,2.05,-1.08,0.11,1.54,-0.76,1.58,1.88,-0.68,1.28,1.76,-0.4,-1.15,1.66,-0.56,-1.48,1.99,-0.48,0.98,2.08,-0.68,0.86,0.78,-0.76,1.68,1.77,-0.2,1.34,0.71,-0.08,1.48,1.71,0.16,1.33,1.88,-0.44,-0.86,1.9,-0.32,-0.77,1.66,-0.24,-1.37,0.77,-0.58,1.64,1.89,-0.04,0.37,1.92,0.08,1,1.88,-0.12,-1.08,1.31,-0.28,1.56,1.99,-0.28,-0.27,1.99,-0.32,-0.4,1.97,-0.28,-0.46,1.99,-0.32,-0.43,1.98,-0.08,-0.72,1.2,-0.2,-1.6,1.38,-0.2,-1.54,1.98,-0.28,-0.42,1.94,0.04,-0.98,1.48,0.04,-1.31,1.97,-0.16,-0.41,1.64,0.2,-1.21,1.48,-0.16,-1.46,1.25,0,-1.45,1.33,-0.12,-1.47,1.39,-0.12,-1.43,0.76,0.21,1.65,1.91,0,-0.07,1.98,0.32,-0.86,1.17,0.28,-1.65,1.42,0.44,-1.53,1.8,0.52,0.22,1.79,0.44,0.37,1.38,0.2,1.41,1.31,0.56,1.39,1.8,0.52,0.03,1.91,0.6,0.95,1.8,0.4,1.21,1.8,0.88,-0.24,1.95,0.72,-0.88,1.92,1.16,-0.85,1.85,0.48,-1.13,1.42,0.8,-1.46,1.18,0.64,-1.66,1.3,0.92,-1.52,0.71,0.52,1.51,1.8,0.68,0.61,1.87,0.92,0.75,1.89,0.76,1.05,1.59,0.88,-1.39,1.75,0.92,-1.25,1.78,0.52,0.32,0.71,0.6,1.62,1.77,0.6,0.2,0.7,0.6,1.54,1.5,0.6,-1.48,1.45,0.76,1.27,1.79,0.72,1.16,1.78,0.92,1.12,1.89,0.92,-1.09,1.76,0.8,0.46,1.38,0.88,-1.43,1.9,0.92,0.98,1.73,1.28,0.45,1.91,1.2,0.91,1.72,1.04,0.34,0.71,0.92,1.6,1.9,1.04,0.97,1.4,0.92,-1.41,1.41,1.04,-1.41,0.72,1.12,1.61,1.9,1.12,-1.1,1.92,1.28,-1,1.4,0.88,-1.41,1.79,1.6,-0.55,1.74,1.36,-0.01,1.6,0.96,-1.32,1.45,0.96,-1.37,1.41,1.12,-1.49,1.48,1.04,1.22,1.68,1.04,-1.28,1.47,0.96,-1.35,1.47,1,-1.35,1.45,0.92,-1.37,1.49,1.04,-1.33,1.56,1.16,-1.26,1.58,1.08,-1.28,1.49,1,-1.32,1.44,1.2,-1.47,1.67,1.24,-1.23,1.57,1.04,-1.27,1.32,1.08,-1.61,1.49,1.32,-1.33,1.57,1.28,-1.23,0.71,1.28,1.6,1.43,1.32,1.29,1.46,1.28,-1.45,1.49,1.32,-1.47,1.41,1.24,-1.6,1.4,1.2,-1.59,1.59,1.36,1.11,1.87,1.48,0.75,1.8,1.24,-1.17,1.55,1.8,1.12,1.45,1.48,1.27,1.57,1.32,-1.24,1.51,1.4,-1.34,1.51,1.36,-1.52,1.53,1.52,-1.28,1.63,1.4,-1.2,0.71,1.52,1.53,0.71,1.36,1.59,0.72,1.48,1.64,1.75,1.36,-1.18,1.74,1.28,-1.2,1.64,1.32,-1.21,1.51,1.36,-1.41,1.5,1.32,-1.4,1.54,1.52,-1.58,1.66,1.36,-1.18,1.64,1.48,-1.17,1.66,1.4,-1.19,1.56,1.48,-1.41,1.79,1.48,1.01,1.63,1.92,1.03,1.83,1.56,-1.12,1.91,1.52,-0.99,1.91,1.68,-0.89,1.49,1.6,1.45,1.64,1.56,-1.17,1.55,1.6,-1.26,1.58,1.56,-1.47,1.84,1.88,0.89,1.74,1.6,-1.14,1.6,1.64,-1.36,1.57,1.64,-1.56,1.64,1.64,-1.17,0.72,1.56,1.65,1.48,1.8,1.29,1.69,1.84,0.48,1.87,1.72,0.79,1.53,1.56,-1.32,0.72,1.6,1.59,0.71,1.64,1.55,1.6,1.92,-1.29,1.62,1.84,-1.16,1.64,1.72,-1.17,1.53,1.6,-1.6,0.73,1.74,1.63,1.58,1.56,-1.39,1.57,1.88,1.48,1.65,1.72,0.21,1.75,1.96,-0.52,1.55,2.04,1.12,1.54,1.92,1.11,0.72,1.88,1.6,1.9,1.8,-1.02,1.65,1.8,-1.47,1.59,1.72,-1.58,1.53,1.88,1.14,1.58,1.8,-1.6,1.6,1.84,-1.58,1.68,1.92,-1.53,0.74,2,1.62,0.74,1.92,1.59,1.54,2.04,1.31,1.54,1.88,1.11,1.84,2.04,0.77,1.72,2.44,-0.3,1.79,2.36,-0.68,1.73,2.52,-0.61,1.91,2.04,-0.96,1.5,2,1.19,1.56,2.12,1.09,1.6,1.92,-1.58,1.64,2.28,1.5,0.76,2.16,1.61,1.72,2.12,-1.08,1.72,2.08,-1.48,1.64,2,-1.58,1.51,2.04,1.2,1.55,2.4,1.15,1.82,2.32,0.79,1.64,1.96,0.07,1.63,2.52,0.99,1.88,2.16,-1.01,1.64,2.32,-1.32,1.68,2.04,0.48,1.89,2.24,-0.83,1.71,2.52,-1.11,1.9,2.28,-0.92,1.69,2.32,-1.67,1.76,2.24,-1.51,1.78,2.4,0.88,0.77,2.28,1.64,1.77,2.48,0.68,1.6,2.4,0.04,1.62,2.2,-0.04,1.89,2.56,-0.83,1.9,2.32,-0.84,1.65,2.4,1.49,0.75,2.44,1.6,1.84,2.52,-0.98,1.66,2.52,-1.32,1.66,2.44,-1.26,1.63,2.44,1.43,1.56,2.48,1.17,1.6,2.76,1.05,1.75,2.88,0.88,1.8,2.72,-1.49,1.73,2.76,-0.61,0.79,2.48,1.58,0.77,2.44,1.58,1.65,2.6,1.45,1.6,2.64,0.05,1.82,3.04,-1.55,0.79,2.6,1.59,1.59,2.68,1.31,1.6,2.84,1.08,1.87,2.76,-0.85,1.69,2.8,-1.32,1.79,2.64,0.74,1.84,2.92,-0.91,0.77,2.71,1.55,1.63,2.76,0.44,1.62,3.08,0.45,1.66,2.92,0.24,1.61,2.96,1.05,1.58,3.08,1.24,1.69,3.32,0.91,0.77,2.91,1.51,0.8,2.86,1.6,1.64,3.32,-1.36,1.69,3.24,-1.23,1.57,3.24,1.36,1.56,3.64,0.38,1.78,3.24,-0.91,1.8,3.2,-1.57,0.79,3.02,1.64,1.73,3.4,-1.54,1.6,3.48,-0.37,0.76,3.1,1.57,1.28,4.04,1.16,1.46,3.92,0.82,1.12,4.32,0.8,1.66,3.36,-1.16,1.66,3.4,-1.22,1.65,3.44,-1.25,1.52,3.56,1.24,1.65,3.68,-0.81,1.6,3.48,-1.36,1.63,3.48,-1.24,1.57,3.68,-1.56,1.59,3.44,1.5,1.65,3.48,-1.07,0.75,3.1,1.6,0.75,3.23,1.56,1.65,3.44,-1.22,0.78,3.68,1.6,0.75,3.88,1.65,0.76,3.5,1.52,0.75,3.6,1.52,0.8,3.6,1.62,0.77,3.34,1.59,1.26,4,1.3,1.3,3.92,1.34,1.08,3.68,1.34,1.49,3.96,-0.23,1.57,3.84,-0.9,1.6,3.64,0.86,1.42,3.88,-1.31,1.22,4.12,-1.14,1.4,4.08,-0.89,1.4,4.16,0.16,1.22,4.4,-0.51,1.4,3.8,-1.74,0.7,3.76,1.48,1.28,3.96,-1.51,1.09,4.12,1.39,0.74,4.12,1.5,1.01,4.28,-1.1,0.98,4.24,-1.26,0.94,4.28,-1.19,1.24,4.04,1.28,1.18,4.44,0.45,1.24,4,1.33,1,4.32,1.01,1,4.16,-1.49,0.82,4.16,1.6,0.68,4.24,1.44,0.67,4.2,1.5,0.75,4.28,1.22,0.68,4.28,1.31,1,4.32,-1.05,1.04,4.32,-1.01,0.94,4.2,-1.42,0.97,4.2,-1.36,0.65,4.24,1.45,0.68,4.32,1.2,0.64,4.32,1.24,0.69,4.32,1.17,1.12,4.4,-0.74,1.04,4.4,-0.86,1.64,1.32,-1.21,1.38,-0.2,-1.54,1.42,0.8,-1.46,1.92,-1.2,-0.2,1.91,-1.2,-0.3,1.86,-1.16,-0.15,1.86,-1.2,-0.3,1.87,-1.2,-0.2,1.81,-1.16,-0.15,1.81,-1.16,-0.15,1.87,-1.2,-0.2,1.86,-1.2,-0.3,1.7,1.6,-1.14,1.59,1.56,-1.17,1.59,1.64,-1.17,1.49,1.52,-1.28,1.51,1.48,-1.41,1.53,1.56,-1.47,1.53,1.56,-1.39,1.49,1.56,-1.32,1.63,1.24,-1.23,1.52,1.28,-1.23,1.53,1.32,-1.24,1.59,1.32,-1.21,1.61,1.36,-1.18,1.61,1.4,-1.19,1.71,1.36,-1.18,1.59,1.32,-1.21,1.69,1.28,-1.2,1.42,1.28,-1.45,1.44,1.32,-1.47,1.45,1.32,-1.4,1.46,1.36,-1.41,1.45,1.32,-1.33,1.35,4.08,-0.89,1.17,4.4,-0.51,1.44,3.96,-0.23,1.18,4.12,-1.14,0.99,4.32,-1.01,1.35,4.08,-0.89,0.95,4.32,1.01,0.7,4.28,1.22,1.23,4.04,1.16,0.95,4.32,1.01,0.65,4.32,1.17,0.7,4.28,1.22,0.65,4.32,1.17,0.63,4.32,1.2,0.7,4.28,1.22,0.7,4.28,1.22,0.63,4.32,1.2,0.63,4.28,1.31,1.18,4.12,-1.14,0.96,4.28,-1.1,0.99,4.32,-1.01,0.92,4.2,-1.36,1.18,4.12,-1.14,1.23,3.96,-1.51,1.52,3.84,-0.9,1.35,4.08,-0.89,1.44,3.96,-0.23,1.41,3.92,0.82,1.56,3.64,0.86,1.52,3.64,0.38,0.63,4.32,1.2,0.59,4.32,1.24,0.63,4.28,1.31,0.63,4.24,1.44,0.6,4.24,1.45,0.62,4.2,1.5,0.7,4.28,1.22,1.19,4.04,1.28,1.23,4.04,1.16,0.7,4.28,1.22,1.04,4.12,1.39,1.19,4.04,1.28,0.63,4.24,1.44,1.04,4.12,1.39,0.63,4.28,1.31,0.63,4.24,1.44,0.62,4.2,1.5,0.7,4.12,1.5,1.58,3.48,-1.24,0.81,3.48,-1.36,0.82,4.05,-1.6,0.82,4.05,-1.6,1.35,4.08,-0.89,1.52,3.84,-0.9,1.04,4.12,1.39,0.7,4.28,1.22,0.63,4.28,1.31,1.18,4.12,-1.14,0.82,4.05,-1.6,1.23,3.96,-1.51,0.93,4.24,-1.26,0.96,4.28,-1.1,1.18,4.12,-1.14,1.2,4,1.33,1.21,4,1.3,1.19,4.04,1.28,1.2,4,1.33,1.04,4.12,1.39,0.66,3.76,1.48,1.26,3.92,1.34,1.21,4,1.3,1.2,4,1.33,1.04,4.12,1.39,1.2,4,1.33,1.19,4.04,1.28,0.63,4.24,1.44,0.7,4.12,1.5,1.04,4.12,1.39,1.41,3.92,0.82,1.52,3.64,0.38,1.36,4.16,0.16,1.23,4.04,1.16,1.07,4.32,0.8,0.95,4.32,1.01,1.26,3.92,1.34,1.2,4,1.33,0.66,3.76,1.48,1.6,3.68,-0.81,1.52,3.84,-0.9,1.44,3.96,-0.23,1.19,4.04,1.28,1.21,4,1.3,1.23,4.04,1.16,1.23,4.04,1.16,1.03,3.68,1.34,1.41,3.92,0.82,1.6,3.48,-1.07,1.58,3.48,-1.24,0.82,4.05,-1.6,0.82,4.05,-1.6,1.52,3.84,-0.9,1.6,3.48,-1.07,1.03,3.68,1.34,0.73,3.68,1.6,0.7,3.6,1.52,0.81,3.48,-1.36,1.52,3.68,-1.56,0.82,4.05,-1.6,1.04,4.12,1.39,0.7,4.12,1.5,0.7,3.88,1.65,1.55,3.48,-0.37,1.52,3.64,0.38,1.58,3.08,0.45,1.03,3.68,1.34,0.66,3.76,1.48,0.73,3.68,1.6,1.03,3.68,1.34,1.26,3.92,1.34,0.66,3.76,1.48,1.52,3.68,-1.56,0.87,3.8,-1.74,0.82,4.05,-1.6,1.6,3.48,-1.07,1.6,3.68,-0.81,1.73,3.24,-0.91,1.44,3.96,-0.23,1.17,4.4,-0.51,1.36,4.16,0.16,1.44,3.96,-0.23,1.36,4.16,0.16,1.52,3.64,0.38,1.64,3.32,0.91,1.52,3.64,0.38,1.56,3.64,0.86,1.47,3.56,1.24,1.56,3.64,0.86,1.41,3.92,0.82,1.47,3.56,1.24,1.03,3.68,1.34,0.71,3.5,1.52,0.71,3.5,1.52,0.7,3.23,1.56,1.55,3.44,1.5,0.82,4.05,-1.6,1.18,4.12,-1.14,1.35,4.08,-0.89,1.6,3.68,-0.81,1.44,3.96,-0.23,1.55,3.48,-0.37,1.55,3.48,-0.37,1.61,2.92,0.24,1.55,2.64,0.05,1.47,3.56,1.24,1.64,3.32,0.91,1.56,3.64,0.86,1.6,3.48,-1.07,1.61,3.44,-1.22,1.58,3.48,-1.24,1.52,3.84,-0.9,1.6,3.68,-0.81,1.6,3.48,-1.07,1.55,3.48,-0.37,1.44,3.96,-0.23,1.52,3.64,0.38,1.03,3.68,1.34,1.47,3.56,1.24,1.41,3.92,0.82,1.47,3.56,1.24,0.71,3.5,1.52,1.55,3.44,1.5,0.7,3.23,1.56,0.71,3.5,1.52,0.72,3.34,1.59,1.47,3.56,1.24,1.55,3.44,1.5,1.53,3.24,1.36,1.03,3.68,1.34,0.7,3.6,1.52,0.71,3.5,1.52,1.23,4.04,1.16,1.26,3.92,1.34,1.03,3.68,1.34,1.23,4.04,1.16,1.21,4,1.3,1.26,3.92,1.34,0.71,3.1,1.57,1.55,3.44,1.5,0.7,3.23,1.56,0.71,3.5,1.52,0.7,3.6,1.52,0.76,3.6,1.62,0.81,3.48,-1.36,1.68,3.4,-1.54,1.52,3.68,-1.56,1.61,3.44,-1.22,1.6,3.44,-1.25,1.58,3.48,-1.24,1.62,3.36,-1.16,1.61,3.4,-1.22,1.61,3.44,-1.22,1.64,3.24,-1.23,1.62,3.36,-1.16,1.73,3.24,-0.91,1.6,3.44,-1.25,1.61,3.44,-1.22,1.61,3.4,-1.22,1.62,3.36,-1.16,1.61,3.44,-1.22,1.6,3.48,-1.07,0.7,3.1,1.6,0.71,3.1,1.57,0.7,3.23,1.56,1.62,3.36,-1.16,1.6,3.48,-1.07,1.73,3.24,-0.91,1.73,3.24,-0.91,1.55,3.48,-0.37,1.68,2.76,-0.61,1.55,3.44,1.5,0.71,3.1,1.57,1.53,3.24,1.36,0.81,3.48,-1.36,1.6,3.44,-1.25,0.84,3.32,-1.36,0.81,3.48,-1.36,1.58,3.48,-1.24,1.6,3.44,-1.25,0.84,3.32,-1.36,1.68,3.4,-1.54,0.81,3.48,-1.36,1.6,3.68,-0.81,1.55,3.48,-0.37,1.73,3.24,-0.91,1.53,3.24,1.36,1.64,3.32,0.91,1.47,3.56,1.24,0.72,2.91,1.51,1.53,3.24,1.36,0.71,3.1,1.57,1.61,3.4,-1.22,1.64,3.24,-1.23,0.84,3.32,-1.36,1.6,3.44,-1.25,1.61,3.4,-1.22,0.84,3.32,-1.36,1.62,3.36,-1.16,1.64,3.24,-1.23,1.61,3.4,-1.22,1.23,4.04,1.16,1.41,3.92,0.82,1.07,4.32,0.8,1.55,3.48,-0.37,1.58,3.08,0.45,1.61,2.92,0.24,0.74,3.02,1.64,0.72,2.91,1.51,0.71,3.1,1.57,0.87,3.04,-1.55,1.64,3.24,-1.23,1.64,2.8,-1.32,1.68,2.76,-0.61,1.55,3.48,-0.37,1.55,2.64,0.05,1.55,2.68,1.31,1.55,2.84,1.08,1.54,3.08,1.24,0.84,3.32,-1.36,1.75,3.2,-1.57,1.68,3.4,-1.54,1.55,2.68,1.31,1.54,3.08,1.24,0.72,2.71,1.55,1.55,2.84,1.08,1.56,2.96,1.05,1.54,3.08,1.24,0.87,3.04,-1.55,1.75,3.2,-1.57,0.84,3.32,-1.36,1.64,3.24,-1.23,1.73,3.24,-0.91,1.79,2.92,-0.91,1.79,2.92,-0.91,1.73,3.24,-0.91,1.68,2.76,-0.61,1.61,2.92,0.24,1.58,3.08,0.45,1.58,2.76,0.44,1.53,3.24,1.36,1.54,3.08,1.24,1.64,3.32,0.91,1.54,3.08,1.24,0.72,2.91,1.51,0.72,2.71,1.55,1.58,3.08,0.45,1.64,3.32,0.91,1.7,2.88,0.88,1.61,2.6,1.45,1.55,2.68,1.31,0.72,2.71,1.55,1.68,2.76,-0.61,1.55,2.64,0.05,1.67,2.44,-0.3,1.64,3.32,0.91,1.58,3.08,0.45,1.52,3.64,0.38,1.56,2.76,1.05,1.55,2.84,1.08,1.55,2.68,1.31,1.54,3.08,1.24,1.53,3.24,1.36,0.72,2.91,1.51,1.64,2.8,-1.32,1.64,3.24,-1.23,1.79,2.92,-0.91,0.87,3.04,-1.55,0.84,3.32,-1.36,1.64,3.24,-1.23,1.74,2.64,0.74,1.58,2.76,0.44,1.7,2.88,0.88,1.58,2.76,0.44,1.74,2.64,0.74,1.72,2.48,0.68,1.73,2.4,0.88,1.72,2.48,0.68,1.74,2.64,0.74,1.56,2.96,1.05,1.7,2.88,0.88,1.64,3.32,0.91,1.54,3.08,1.24,1.56,2.96,1.05,1.64,3.32,0.91,1.55,2.84,1.08,1.7,2.88,0.88,1.56,2.96,1.05,1.55,2.64,0.05,1.58,2.76,0.44,1.72,2.48,0.68,1.64,2.8,-1.32,1.82,2.76,-0.85,1.66,2.52,-1.11,0.86,2.72,-1.49,1.64,2.8,-1.32,1.61,2.52,-1.32,1.84,2.56,-0.83,1.69,2.52,-0.61,1.74,2.36,-0.68,1.61,2.92,0.24,1.58,2.76,0.44,1.55,2.64,0.05,1.64,2.8,-1.32,0.86,2.72,-1.49,0.87,3.04,-1.55,1.82,2.76,-0.85,1.79,2.52,-0.98,1.66,2.52,-1.11,1.64,2.8,-1.32,1.79,2.92,-0.91,1.82,2.76,-0.85,1.68,2.76,-0.61,1.84,2.56,-0.83,1.82,2.76,-0.85,1.55,2.4,0.04,1.55,2.64,0.05,1.72,2.48,0.68,1.58,2.76,0.44,1.58,3.08,0.45,1.7,2.88,0.88,1.61,2.6,1.45,0.72,2.71,1.55,0.75,2.6,1.59,1.82,2.76,-0.85,1.79,2.92,-0.91,1.68,2.76,-0.61,1.73,2.4,0.88,1.74,2.64,0.74,1.7,2.88,0.88,1.55,2.68,1.31,1.52,2.48,1.17,1.56,2.76,1.05,1.64,2.8,-1.32,1.66,2.52,-1.11,1.61,2.52,-1.32,1.7,1.96,-0.52,1.58,2.2,-0.04,1.59,1.96,0.07,1.59,2.52,0.99,1.73,2.4,0.88,1.7,2.88,0.88,1.61,2.52,-1.32,0.94,2.24,-1.51,0.86,2.72,-1.49,1.84,2.56,-0.83,1.79,2.52,-0.98,1.82,2.76,-0.85,1.63,2.04,0.48,1.59,1.96,0.07,1.58,2.2,-0.04,1.7,2.88,0.88,1.55,2.84,1.08,1.56,2.76,1.05,1.59,2.44,1.43,1.61,2.6,1.45,0.74,2.48,1.58,1.61,2.4,1.49,1.59,2.44,1.43,0.74,2.48,1.58,1.61,2.6,1.45,0.75,2.6,1.59,0.74,2.48,1.58,1.66,2.52,-1.11,1.62,2.44,-1.26,1.61,2.52,-1.32,1.61,2.6,1.45,1.52,2.48,1.17,1.55,2.68,1.31,1.55,2.64,0.05,1.55,2.4,0.04,1.67,2.44,-0.3,1.63,2.04,0.48,1.58,2.2,-0.04,1.55,2.4,0.04,0.94,2.24,-1.51,0.87,2.32,-1.67,0.86,2.72,-1.49,1.67,2.12,-1.08,0.83,2.32,-1.32,1.62,2.44,-1.26,1.74,2.36,-0.68,1.7,1.96,-0.52,1.84,2.24,-0.83,1.67,2.44,-0.3,1.69,2.52,-0.61,1.68,2.76,-0.61,1.73,2.4,0.88,1.77,2.32,0.79,1.72,2.48,0.68,1.59,2.44,1.43,1.5,2.4,1.15,1.52,2.48,1.17,1.61,2.6,1.45,1.59,2.44,1.43,1.52,2.48,1.17,1.61,2.4,1.49,0.74,2.48,1.58,0.73,2.44,1.58,1.55,1.92,-1.29,0.9,2.08,-1.48,0.83,2.32,-1.32,1.67,2.12,-1.08,1.62,2.44,-1.26,1.66,2.52,-1.11,1.68,2.76,-0.61,1.69,2.52,-0.61,1.84,2.56,-0.83,1.79,2.04,0.77,1.63,2.04,0.48,1.77,2.32,0.79,1.73,2.4,0.88,1.59,2.52,0.99,1.51,2.12,1.09,1.5,2.4,1.15,1.59,2.52,0.99,1.52,2.48,1.17,1.61,2.52,-1.32,0.83,2.32,-1.32,0.94,2.24,-1.51,1.79,2.52,-0.98,1.85,2.32,-0.84,1.86,2.28,-0.92,1.59,2.52,0.99,1.7,2.88,0.88,1.56,2.76,1.05,1.52,2.48,1.17,1.59,2.52,0.99,1.56,2.76,1.05,1.59,2.44,1.43,1.59,2.28,1.5,1.5,2.4,1.15,1.66,2.52,-1.11,1.79,2.52,-0.98,1.86,2.28,-0.92,1.59,2.44,1.43,1.61,2.4,1.49,1.59,2.28,1.5,0.72,2.28,1.64,1.59,2.28,1.5,1.61,2.4,1.49,1.61,2.52,-1.32,1.62,2.44,-1.26,0.83,2.32,-1.32,1.79,2.52,-0.98,1.84,2.56,-0.83,1.85,2.32,-0.84,1.74,2.36,-0.68,1.84,2.24,-0.83,1.85,2.32,-0.84,1.75,1.6,-0.55,1.7,1.96,-0.52,1.59,1.96,0.07,1.55,2.4,0.04,1.58,2.2,-0.04,1.67,2.44,-0.3,1.59,1.96,0.07,1.63,2.04,0.48,1.64,1.84,0.48,1.46,2.04,1.2,1.51,2.12,1.09,1.5,2.4,1.15,0.71,2.16,1.61,1.59,2.28,1.5,0.72,2.28,1.64,0.72,2.28,1.64,1.61,2.4,1.49,0.71,2.44,1.6,0.9,2.08,-1.48,0.94,2.24,-1.51,0.83,2.32,-1.32,1.86,2.04,-0.96,1.83,2.16,-1.01,1.84,2.24,-0.83,1.46,2.04,1.2,1.5,2.04,1.12,1.51,2.12,1.09,1.83,2.16,-1.01,1.67,2.12,-1.08,1.66,2.52,-1.11,1.83,2.16,-1.01,1.86,2.28,-0.92,1.84,2.24,-0.83,1.84,2.24,-0.83,1.86,2.28,-0.92,1.85,2.32,-0.84,1.67,2.44,-0.3,1.7,1.96,-0.52,1.74,2.36,-0.68,1.84,2.56,-0.83,1.74,2.36,-0.68,1.85,2.32,-0.84,1.7,1.96,-0.52,1.67,2.44,-0.3,1.58,2.2,-0.04,1.63,2.04,0.48,1.55,2.4,0.04,1.72,2.48,0.68,1.63,2.04,0.48,1.72,2.48,0.68,1.77,2.32,0.79,1.77,2.32,0.79,1.73,2.4,0.88,1.51,2.12,1.09,1.55,1.92,-1.29,1.63,1.92,-1.53,0.9,2.08,-1.48,1.58,1.84,-1.16,1.67,2.12,-1.08,1.86,2.04,-0.96,1.83,2.16,-1.01,1.66,2.52,-1.11,1.86,2.28,-0.92,1.84,2.24,-0.83,1.7,1.96,-0.52,1.86,2.04,-0.96,1.63,2.04,0.48,1.79,2.04,0.77,1.64,1.84,0.48,1.55,1.92,-1.29,0.83,2.32,-1.32,1.67,2.12,-1.08,1.83,2.16,-1.01,1.86,2.04,-0.96,1.67,2.12,-1.08,1.45,2,1.19,1.5,2.04,1.31,1.43,1.8,1.29,0.89,2,-1.58,1.63,1.92,-1.53,0.87,1.92,-1.58,1.59,1.96,0.07,1.64,1.84,0.48,1.61,1.72,0.21,1.79,1.88,0.89,1.79,2.04,0.77,1.58,1.92,1.03,1.51,2.12,1.09,1.5,2.04,1.12,1.58,1.92,1.03,1.5,2.04,1.12,1.46,2.04,1.2,1.45,2,1.19,1.59,2.28,1.5,1.5,2.04,1.31,1.5,2.4,1.15,1.45,2,1.19,1.43,1.8,1.29,1.48,1.88,1.14,1.45,2,1.19,1.46,2.04,1.2,1.5,2.04,1.31,1.59,2.52,0.99,1.5,2.4,1.15,1.51,2.12,1.09,1.55,1.92,-1.29,0.87,1.86,-1.47,1.63,1.92,-1.53,1.75,1.6,-0.55,1.59,1.96,0.07,1.61,1.72,0.21,1.79,2.04,0.77,1.77,2.32,0.79,1.51,2.12,1.09,1.46,2.04,1.2,1.5,2.4,1.15,1.5,2.04,1.31,0.9,2.08,-1.48,1.63,1.92,-1.53,0.89,2,-1.58,1.58,1.84,-1.16,1.55,1.92,-1.29,1.67,2.12,-1.08,1.59,1.72,-1.17,1.58,1.84,-1.16,1.85,1.8,-1.02,1.5,1.92,1.11,1.49,1.88,1.11,1.58,1.92,1.03,1.5,2.04,1.31,1.52,1.88,1.48,1.43,1.8,1.29,1.5,1.92,1.11,1.45,2,1.19,1.48,1.88,1.14,0.7,2,1.62,1.5,2.04,1.31,0.71,2.16,1.61,1.59,2.28,1.5,0.71,2.16,1.61,1.5,2.04,1.31,1.55,1.64,-1.36,0.86,1.7,-1.56,0.88,1.78,-1.58,1.59,1.72,-1.17,1.85,1.8,-1.02,1.7,1.6,-1.14,1.75,1.48,1.01,1.82,1.72,0.79,1.79,1.88,0.89,1.48,1.88,1.14,1.49,1.88,1.11,1.5,1.92,1.11,0.69,1.92,1.59,1.52,1.88,1.48,1.5,2.04,1.31,1.55,1.84,-1.58,0.87,1.92,-1.58,1.63,1.92,-1.53,1.7,1.96,-0.52,1.85,1.8,-1.02,1.86,2.04,-0.96,1.7,1.96,-0.52,1.86,1.68,-0.89,1.85,1.8,-1.02,1.58,1.92,1.03,1.79,2.04,0.77,1.51,2.12,1.09,1.5,1.8,1.12,1.49,1.88,1.11,1.48,1.88,1.14,1.5,1.92,1.11,1.5,2.04,1.12,1.45,2,1.19,1.52,1.88,1.48,0.69,1.92,1.59,0.68,1.88,1.6,0.86,1.86,-1.6,0.87,1.86,-1.47,0.88,1.78,-1.58,1.58,1.84,-1.16,1.86,2.04,-0.96,1.85,1.8,-1.02,1.64,1.84,0.48,1.83,1.48,0.75,1.68,1.28,0.45,0.68,1.74,1.63,0.67,1.64,1.55,1.52,1.88,1.48,0.68,1.74,1.63,1.52,1.88,1.48,0.68,1.88,1.6,0.87,1.86,-1.47,1.55,1.64,-1.36,0.88,1.78,-1.58,1.67,2.44,-0.3,1.74,2.36,-0.68,1.69,2.52,-0.61,1.79,2.04,0.77,1.79,1.88,0.89,1.64,1.84,0.48,1.58,1.92,1.03,1.49,1.88,1.11,1.5,1.8,1.12,0.7,2,1.62,0.69,1.92,1.59,1.5,2.04,1.31,0.87,1.86,-1.47,1.55,1.84,-1.58,1.63,1.92,-1.53,0.86,1.86,-1.6,1.55,1.84,-1.58,0.87,1.86,-1.47,1.85,1.8,-1.02,1.78,1.56,-1.12,1.7,1.6,-1.14,1.5,1.8,1.12,1.48,1.88,1.14,1.43,1.8,1.29,1.45,1.6,1.45,1.43,1.8,1.29,1.52,1.88,1.48,0.87,1.86,-1.47,1.55,1.92,-1.29,1.55,1.64,-1.36,1.78,1.56,-1.12,1.85,1.8,-1.02,1.86,1.68,-0.89,1.83,0.92,0.75,1.76,0.68,0.61,1.71,0.8,0.46,0.82,1.66,-1.6,0.86,1.7,-1.56,1.53,1.56,-1.47,1.55,1.92,-1.29,1.59,1.72,-1.17,1.55,1.64,-1.36,1.55,1.64,-1.36,1.53,1.56,-1.39,1.53,1.56,-1.47,1.59,1.72,-1.17,1.51,1.6,-1.26,1.55,1.64,-1.36,1.59,1.64,-1.17,1.59,1.72,-1.17,1.7,1.6,-1.14,1.61,1.72,0.21,1.64,1.84,0.48,1.68,1.28,0.45,1.5,2.04,1.12,1.5,1.92,1.11,1.58,1.92,1.03,1.7,1.96,-0.52,1.75,1.6,-0.55,1.86,1.68,-0.89,1.69,1.36,-0.01,1.75,1.6,-0.55,1.61,1.72,0.21,1.69,1.36,-0.01,1.68,1.28,0.45,1.68,1.04,0.34,1.69,1.36,-0.01,1.61,1.72,0.21,1.68,1.28,0.45,1.75,1.48,1.01,1.83,1.48,0.75,1.82,1.72,0.79,1.45,1.6,1.45,1.52,1.88,1.48,0.67,1.64,1.55,1.53,1.56,-1.39,1.55,1.64,-1.36,1.49,1.56,-1.32,1.59,1.72,-1.17,1.59,1.64,-1.17,1.51,1.6,-1.26,0.82,1.66,-1.6,1.53,1.56,-1.47,0.82,1.58,-1.58,1.55,1.92,-1.29,1.58,1.84,-1.16,1.59,1.72,-1.17,1.78,1.56,-1.12,1.86,1.68,-0.89,1.87,1.52,-0.99,1.79,1.88,0.89,1.82,1.72,0.79,1.64,1.84,0.48,1.43,1.8,1.29,1.45,1.6,1.45,1.41,1.48,1.27,0.67,1.52,1.53,1.45,1.6,1.45,0.67,1.64,1.55,0.67,1.6,1.59,0.67,1.52,1.53,0.67,1.64,1.55,0.67,1.6,1.59,0.68,1.56,1.65,0.67,1.52,1.53,1.51,1.6,-1.26,1.49,1.52,-1.28,1.49,1.56,-1.32,1.51,1.6,-1.26,1.49,1.56,-1.32,1.55,1.64,-1.36,1.71,1.36,-1.18,1.87,1.52,-0.99,1.88,1.28,-1,1.9,0.72,-0.88,1.85,0.92,-1.09,1.87,1.16,-0.85,1.76,0.88,-0.24,1.69,1.36,-0.01,1.68,1.04,0.34,1.64,1.84,0.48,1.82,1.72,0.79,1.83,1.48,0.75,1.5,1.8,1.12,1.43,1.8,1.29,1.41,1.48,1.27,1.59,1.56,-1.17,1.51,1.6,-1.26,1.59,1.64,-1.17,1.55,1.64,-1.36,1.53,1.56,-1.47,0.86,1.7,-1.56,1.7,1.6,-1.14,1.6,1.48,-1.17,1.59,1.56,-1.17,1.54,1.36,1.11,1.74,0.92,1.12,1.85,1.04,0.97,1.86,1.2,0.91,1.75,1.48,1.01,1.54,1.36,1.11,1.51,1.48,-1.41,0.78,1.63,-1.53,0.82,1.58,-1.58,1.59,1.56,-1.17,1.6,1.48,-1.17,1.49,1.52,-1.28,1.7,1.6,-1.14,1.78,1.56,-1.12,1.6,1.48,-1.17,1.78,1.56,-1.12,1.61,1.4,-1.19,1.6,1.48,-1.17,1.88,1.28,-1,1.87,1.52,-0.99,1.75,1.6,-0.55,1.54,1.36,1.11,1.75,1.48,1.01,1.5,1.8,1.12,1.86,1.2,0.91,1.83,1.48,0.75,1.75,1.48,1.01,1.75,1.48,1.01,1.79,1.88,0.89,1.58,1.92,1.03,1.41,1.48,1.27,1.39,1.32,1.29,1.54,1.36,1.11,1.39,1.32,1.29,0.66,1.28,1.6,0.68,1.12,1.61,1.46,1.36,-1.41,0.78,1.63,-1.53,1.51,1.48,-1.41,1.51,1.48,-1.41,0.82,1.58,-1.58,1.53,1.56,-1.47,1.46,1.4,-1.34,1.51,1.48,-1.41,1.49,1.52,-1.28,1.59,1.32,-1.21,1.53,1.32,-1.24,1.58,1.4,-1.2,1.59,1.56,-1.17,1.49,1.52,-1.28,1.51,1.6,-1.26,1.87,1.16,-0.85,1.88,1.28,-1,1.75,1.6,-0.55,1.86,1.2,0.91,1.54,1.36,1.11,1.85,1.04,0.97,1.45,1.6,1.45,0.67,1.52,1.53,1.41,1.48,1.27,0.67,1.52,1.53,1.39,1.32,1.29,1.41,1.48,1.27,1.87,1.52,-0.99,1.86,1.68,-0.89,1.75,1.6,-0.55,1.75,1.24,-1.17,1.88,1.28,-1,1.85,1.12,-1.1,1.71,1.36,-1.18,1.78,1.56,-1.12,1.87,1.52,-0.99,1.78,1.56,-1.12,1.71,1.36,-1.18,1.61,1.4,-1.19,1.75,1.48,1.01,1.58,1.92,1.03,1.5,1.8,1.12,1.39,1.32,1.29,0.67,1.36,1.59,0.66,1.28,1.6,1.46,1.36,-1.41,1.51,1.48,-1.41,1.46,1.4,-1.34,1.6,1.48,-1.17,1.61,1.4,-1.19,1.58,1.4,-1.2,1.58,1.4,-1.2,1.61,1.4,-1.19,1.61,1.36,-1.18,1.45,1.32,-1.33,1.46,1.36,-1.41,1.46,1.4,-1.34,1.53,1.32,-1.24,1.46,1.4,-1.34,1.58,1.4,-1.2,1.6,1.48,-1.17,1.58,1.4,-1.2,1.49,1.52,-1.28,1.59,1.32,-1.21,1.58,1.4,-1.2,1.61,1.36,-1.18,1.44,1.32,-1.47,0.78,1.63,-1.53,1.46,1.36,-1.41,1.44,1.32,-1.47,1.46,1.36,-1.41,1.45,1.32,-1.4,1.71,1.36,-1.18,1.69,1.28,-1.2,1.59,1.32,-1.21,1.69,1.28,-1.2,1.71,1.36,-1.18,1.75,1.24,-1.17,1.69,1.28,-1.2,1.75,1.24,-1.17,1.63,1.24,-1.23,1.75,1.24,-1.17,1.71,1.36,-1.18,1.88,1.28,-1,0.67,1.52,1.53,0.68,1.48,1.64,0.67,1.36,1.59,1.39,1.32,1.29,0.67,1.52,1.53,0.67,1.36,1.59,0.82,1.41,-1.67,0.81,1.3,-1.49,1.35,1.2,-1.59,1.46,1.4,-1.34,1.49,1.52,-1.28,1.58,1.4,-1.2,1.45,1.32,-1.33,1.51,1.16,-1.26,1.42,1.28,-1.45,0.82,1.5,-1.6,1.42,1.28,-1.45,0.82,1.41,-1.67,0.82,1.41,-1.67,1.35,1.2,-1.59,0.82,1.5,-1.6,0.78,1.63,-1.53,1.44,1.32,-1.47,0.82,1.5,-1.6,1.45,1.32,-1.33,1.53,1.32,-1.24,1.52,1.28,-1.23,1.53,1.32,-1.24,1.45,1.32,-1.33,1.46,1.4,-1.34,1.64,1.04,-1.28,1.63,1.24,-1.23,1.75,1.24,-1.17,1.54,1.36,1.11,1.5,1.8,1.12,1.41,1.48,1.27,1.39,1.32,1.29,1.44,1.04,1.22,1.54,1.36,1.11,1.53,1.08,-1.28,1.51,1.16,-1.26,1.63,1.24,-1.23,1.63,1.24,-1.23,1.51,1.16,-1.26,1.52,1.28,-1.23,1.64,1.04,-1.28,1.75,1.24,-1.17,1.85,1.12,-1.1,1.68,1.28,0.45,1.83,1.48,0.75,1.86,1.2,0.91,1.54,1.36,1.11,1.44,1.04,1.22,1.74,0.92,1.12,1.44,1.32,-1.47,1.42,1.28,-1.45,0.82,1.5,-1.6,1.51,1.16,-1.26,1.45,1.04,-1.33,0.82,1.41,-1.67,1.51,1.16,-1.26,0.82,1.41,-1.67,1.42,1.28,-1.45,0.82,1.41,-1.67,1.36,1.04,-1.41,0.81,1.3,-1.49,1.83,0.92,0.75,1.85,1.04,0.97,1.85,0.92,0.98,1.44,1.04,1.22,1.39,1.32,1.29,0.68,1.12,1.61,1.1,1.08,-1.61,0.81,1.3,-1.49,0.85,0.92,-1.52,1.45,1.32,-1.33,1.52,1.28,-1.23,1.51,1.16,-1.26,1.7,0.92,-1.25,1.85,1.12,-1.1,1.85,0.92,-1.09,1.45,1.04,-1.33,1.43,1,-1.35,1.36,1.04,-1.41,1.45,1.04,-1.33,1.53,1.08,-1.28,1.52,1.04,-1.27,1.53,1.08,-1.28,1.63,1.24,-1.23,1.64,1.04,-1.28,1.7,0.92,-1.25,1.64,1.04,-1.28,1.85,1.12,-1.1,1.87,1.16,-0.85,1.75,1.6,-0.55,1.76,0.88,-0.24,1.74,0.92,1.12,1.44,1.04,1.22,1.4,0.76,1.27,1.44,1.04,1.22,0.67,0.92,1.6,1.4,0.76,1.27,1.45,1.04,-1.33,1.36,1.04,-1.41,0.82,1.41,-1.67,1.44,1,-1.32,1.43,1,-1.35,1.45,1.04,-1.33,1.45,1.04,-1.33,1.51,1.16,-1.26,1.53,1.08,-1.28,1.43,1,-1.35,1.41,0.96,-1.37,1.36,1.04,-1.41,0.95,0.92,-1.41,1.41,0.96,-1.37,1.4,0.92,-1.37,1.43,0.96,-1.35,1.41,0.96,-1.37,1.43,1,-1.35,1.64,1.04,-1.28,1.7,0.92,-1.25,1.55,0.96,-1.32,1.44,1.04,1.22,0.68,1.12,1.61,0.67,0.92,1.6,0.81,1.3,-1.49,1.36,1.04,-1.41,0.85,0.92,-1.52,1.41,0.96,-1.37,0.95,0.92,-1.41,1.36,1.04,-1.41,1.55,0.96,-1.32,1.7,0.92,-1.25,1.54,0.88,-1.39,0.93,0.57,-1.53,0.93,0.7,-1.48,1.6,0.2,-1.21,0.93,0.7,-1.48,0.97,0.8,-1.46,1.54,0.88,-1.39,1.87,1.16,-0.85,1.85,0.92,-1.09,1.85,1.12,-1.1,1.75,1.6,-0.55,1.69,1.36,-0.01,1.76,0.88,-0.24,0.95,0.92,-1.41,0.93,0.88,-1.43,0.85,0.92,-1.52,0.95,0.92,-1.41,0.95,0.88,-1.41,0.93,0.88,-1.43,1.87,1.16,-0.85,1.85,1.12,-1.1,1.88,1.28,-1,0.95,0.92,-1.41,0.85,0.92,-1.52,1.36,1.04,-1.41,1.76,0.88,-0.24,1.93,0.32,-0.86,1.9,0.72,-0.88,1.74,0.92,1.12,1.85,0.92,0.98,1.85,1.04,0.97,0.65,0.6,1.54,1.27,0.56,1.39,0.67,0.92,1.6,0.93,0.7,-1.48,1.8,0.48,-1.13,1.6,0.2,-1.21,1.76,0.88,-0.24,1.68,1.04,0.34,1.72,0.6,0.2,1.72,0.6,0.2,1.75,0.52,0.03,1.76,0.88,-0.24,1.83,0.92,0.75,1.85,0.92,0.98,1.85,0.76,1.05,1.75,0.4,1.21,1.4,0.76,1.27,1.27,0.56,1.39,1.93,0.32,-0.86,1.8,0.48,-1.13,1.9,0.72,-0.88,1.83,0.92,0.75,1.71,0.8,0.46,1.68,1.04,0.34,1.83,0.92,0.75,1.68,1.04,0.34,1.68,1.28,0.45,0.97,0.8,-1.46,0.93,0.7,-1.48,0.95,0.75,-1.66,1.7,0.92,-1.25,1.85,0.92,-1.09,1.8,0.48,-1.13,1.74,0.92,1.12,1.74,0.72,1.16,1.85,0.76,1.05,0.93,0.7,-1.48,1.54,0.88,-1.39,1.8,0.48,-1.13,1.71,0.8,0.46,1.73,0.52,0.32,1.72,0.6,0.2,1.74,0.44,0.37,1.73,0.52,0.32,1.76,0.68,0.61,1.87,0.6,0.95,1.76,0.68,0.61,1.83,0.92,0.75,1.86,1.2,0.91,1.85,1.04,0.97,1.83,0.92,0.75,1.27,0.56,1.39,1.4,0.76,1.27,0.67,0.92,1.6,1.33,0.2,1.41,1.27,0.56,1.39,0.67,0.52,1.51,1.68,1.04,0.34,1.71,0.8,0.46,1.72,0.6,0.2,1.83,0.92,0.75,1.68,1.28,0.45,1.86,1.2,0.91,1.87,0.6,0.95,1.85,0.76,1.05,1.74,0.72,1.16,1.74,0.92,1.12,1.85,0.76,1.05,1.85,0.92,0.98,0.97,0.8,-1.46,0.85,0.92,-1.52,0.93,0.88,-1.43,1.75,0.4,1.21,1.87,0.6,0.95,1.74,0.72,1.16,1.74,0.72,1.16,1.4,0.76,1.27,1.75,0.4,1.21,1.73,0.52,0.32,1.71,0.8,0.46,1.76,0.68,0.61,1.8,0.48,-1.13,1.85,0.92,-1.09,1.9,0.72,-0.88,1.75,0.52,0.22,1.72,0.6,0.2,1.73,0.52,0.32,1.4,0.76,1.27,1.74,0.72,1.16,1.74,0.92,1.12,1.27,0.56,1.39,0.65,0.6,1.54,0.67,0.52,1.51,0.66,0.6,1.62,0.67,0.52,1.51,0.65,0.6,1.54,1.75,0.52,0.22,1.75,0.52,0.03,1.72,0.6,0.2,1.66,0.16,1.33,1.75,0.4,1.21,1.27,0.56,1.39,1.76,0.88,-0.24,1.75,0.52,0.03,1.93,0.32,-0.86,1.75,0.52,0.22,1.73,0.52,0.32,1.74,0.44,0.37,0.96,0.2,-1.45,0.93,0.57,-1.53,1.43,0.04,-1.31,1.54,0.88,-1.39,1.7,0.92,-1.25,1.8,0.48,-1.13,1.93,-0.16,-0.41,1.93,-0.08,-0.72,1.93,0.32,-0.86,1.87,0.6,0.95,1.83,0.92,0.75,1.85,0.76,1.05,1.76,0.68,0.61,1.87,0.6,0.95,1.88,0.08,1,1.84,-0.04,0.37,1.86,0,-0.07,1.74,0.44,0.37,1.76,0.68,0.61,1.88,0.08,1,1.74,0.44,0.37,1.88,0.08,1,1.75,0.4,1.21,1.66,0.16,1.33,1.6,0.2,-1.21,1.8,0.48,-1.13,1.93,0.32,-0.86,1.76,0.88,-0.24,1.9,0.72,-0.88,1.87,1.16,-0.85,1.66,0.16,1.33,1.33,0.2,1.41,0.66,-0.08,1.48,0.93,0.57,-1.53,1.6,0.2,-1.21,1.43,0.04,-1.31,1.89,0.04,-0.98,1.93,0.32,-0.86,1.93,-0.08,-0.72,0.96,0.2,-1.45,1.43,0.04,-1.31,0.95,-0.1,-1.43,1.83,-0.12,-1.08,1.71,-0.4,-1.15,1.61,-0.24,-1.37,1.95,-0.32,-0.07,1.86,0,-0.07,1.84,-0.04,0.37,1.87,0.6,0.95,1.75,0.4,1.21,1.88,0.08,1,1.86,0,-0.07,1.75,0.52,0.03,1.75,0.52,0.22,1.6,0.2,-1.21,1.93,0.32,-0.86,1.89,0.04,-0.98,1.93,0.32,-0.86,1.75,0.52,0.03,1.86,0,-0.07,1.88,0.08,1,1.84,-0.04,0.37,1.74,0.44,0.37,1.33,0.2,1.41,1.66,0.16,1.33,1.27,0.56,1.39,1.93,-0.08,-0.72,1.93,-0.16,-0.41,1.92,-0.28,-0.46,1.86,0,-0.07,1.75,0.52,0.22,1.74,0.44,0.37,1.94,-0.28,-0.27,1.93,-0.16,-0.41,1.86,0,-0.07,0.94,-0.12,-1.46,0.95,-0.1,-1.43,1.43,0.04,-1.31,2.03,-0.68,0.86,2.04,-0.84,0.71,2.11,-0.64,0.45,1.72,-0.2,1.34,0.66,-0.08,1.48,0.72,-0.58,1.64,0.96,0.2,-1.45,0.99,0.36,-1.65,0.93,0.57,-1.53,1.66,0.16,1.33,1.72,-0.2,1.34,1.88,0.08,1,0.94,-0.12,-1.46,1.43,0.04,-1.31,1.61,-0.24,-1.37,1.83,-0.12,-1.08,1.43,0.04,-1.31,1.6,0.2,-1.21,1.86,-0.32,-0.77,1.93,-0.08,-0.72,1.92,-0.28,-0.46,1.72,-0.2,1.34,1.95,-0.48,0.98,1.88,0.08,1,0.94,-0.03,-1.54,0.96,0.05,-1.6,0.94,-0.07,-1.47,0.94,-0.12,-1.46,0.96,-0.56,-1.48,0.97,-0.2,-1.54,1.83,-0.44,-0.86,1.71,-0.4,-1.15,1.83,-0.12,-1.08,1.93,-0.16,-0.41,1.93,0.32,-0.86,1.86,0,-0.07,1.94,-0.28,-0.27,1.86,0,-0.07,1.95,-0.32,-0.07,0.95,-0.1,-1.43,0.94,-0.07,-1.47,0.96,0.2,-1.45,0.96,0.2,-1.45,0.94,-0.07,-1.47,0.96,0.05,-1.6,1.93,-0.28,-0.42,1.93,-0.16,-0.41,1.94,-0.28,-0.27,0.94,-0.12,-1.46,1.61,-0.24,-1.37,0.96,-0.56,-1.48,1.6,0.2,-1.21,1.89,0.04,-0.98,1.83,-0.12,-1.08,0.96,-0.56,-1.48,0.99,-0.32,-1.68,0.97,-0.2,-1.54,1.93,-0.28,-0.42,1.92,-0.28,-0.46,1.93,-0.16,-0.41,1.83,-0.12,-1.08,1.61,-0.24,-1.37,1.43,0.04,-1.31,1.95,-0.32,-0.4,1.93,-0.28,-0.42,1.94,-0.28,-0.27,1.93,-0.08,-0.72,1.83,-0.12,-1.08,1.89,0.04,-0.98,1.92,-0.28,-0.46,1.93,-0.28,-0.42,1.95,-0.32,-0.43,1.95,-0.32,-0.4,1.95,-0.32,-0.43,1.93,-0.28,-0.42,1.95,-0.32,-0.07,1.84,-0.04,0.37,2.11,-0.64,0.45,1.95,-0.48,0.98,2.11,-0.64,0.45,1.88,0.08,1,1.93,-0.4,-0.5,1.86,-0.32,-0.77,1.92,-0.28,-0.46,1.95,-0.32,-0.43,1.94,-0.36,-0.4,1.93,-0.4,-0.5,1.95,-0.32,-0.43,1.95,-0.32,-0.4,1.94,-0.36,-0.4,1.86,-0.32,-0.77,1.83,-0.12,-1.08,1.93,-0.08,-0.72,1.92,-0.28,-0.46,1.95,-0.32,-0.43,1.93,-0.4,-0.5,1.94,-0.36,-0.4,1.95,-0.32,-0.4,1.96,-0.36,-0.27,1.95,-0.32,-0.4,1.94,-0.28,-0.27,1.96,-0.36,-0.27,1.96,-0.36,-0.27,1.94,-0.28,-0.27,1.95,-0.32,-0.07,1.27,-0.28,1.56,0.72,-0.58,1.64,0.66,-0.08,1.48,1.96,-0.36,-0.27,2.14,-0.8,-0.09,2.09,-0.72,-0.31,2.03,-0.68,0.86,1.87,-0.8,1.07,1.93,-0.84,0.89,1.72,-0.2,1.34,1.83,-0.68,1.28,1.95,-0.48,0.98,1.92,-0.76,-1.15,1.71,-0.4,-1.15,1.95,-0.64,-0.88,0.72,-0.58,1.64,0.74,-0.76,1.68,1.72,-0.2,1.34,0.96,-0.56,-1.48,1.71,-0.4,-1.15,1.86,-0.8,-1.32,2.14,-0.88,0.13,2.14,-0.8,-0.09,1.95,-0.32,-0.07,2.14,-0.88,0.13,1.95,-0.32,-0.07,2.11,-0.64,0.45,1.86,-0.8,-1.32,1.75,-0.88,-1.46,0.98,-0.76,-1.55,1.86,-0.32,-0.77,1.83,-0.44,-0.86,1.83,-0.12,-1.08,2.11,-0.64,0.45,1.84,-0.04,0.37,1.88,0.08,1,1.87,-0.8,1.07,1.83,-0.68,1.28,1.68,-0.8,1.34,0.96,-0.56,-1.48,1.86,-0.8,-1.32,0.98,-0.76,-1.55,2.05,-1,-0.91,1.95,-0.64,-0.88,2.04,-1.12,-0.68,1.93,-0.4,-0.5,1.95,-0.64,-0.88,1.83,-0.44,-0.86,1.95,-0.48,0.98,1.83,-0.68,1.28,1.87,-0.8,1.07,1.72,-0.2,1.34,1.68,-0.56,1.47,1.83,-0.68,1.28,1.61,-0.24,-1.37,1.71,-0.4,-1.15,0.96,-0.56,-1.48,1.86,-0.32,-0.77,1.93,-0.4,-0.5,1.83,-0.44,-0.86,1.96,-0.92,-1.1,1.92,-0.76,-1.15,1.95,-0.64,-0.88,1.71,-0.4,-1.15,1.83,-0.44,-0.86,1.95,-0.64,-0.88,1.95,-0.64,-0.88,2.09,-0.72,-0.31,2.13,-1,-0.45,2.04,-0.84,0.71,2.03,-0.68,0.86,1.95,-0.88,0.79,1.95,-0.48,0.98,2.03,-0.68,0.86,2.11,-0.64,0.45,0.66,-0.08,1.48,1.72,-0.2,1.34,1.66,0.16,1.33,0.74,-0.76,1.68,1.68,-0.56,1.47,1.72,-0.2,1.34,2.03,-0.68,0.86,1.93,-0.84,0.89,1.95,-0.88,0.79,1.95,-0.48,0.98,1.87,-0.8,1.07,2.03,-0.68,0.86,1.62,-0.76,1.49,1.68,-0.56,1.47,1.49,-0.76,1.58,1.86,-0.8,-1.32,1.71,-0.4,-1.15,1.92,-0.76,-1.15,1.96,-0.92,-1.1,1.95,-0.64,-0.88,2.05,-1,-0.91,1.68,-0.8,1.34,1.83,-0.68,1.28,1.68,-0.56,1.47,1.75,-0.88,-1.46,1.16,-0.96,-1.42,1,-0.81,-1.53,2.09,-0.72,-0.31,1.93,-0.4,-0.5,1.94,-0.36,-0.4,2.06,-1.04,0.15,2,-1.08,0.11,2.07,-1.08,-0.01,2.07,-1.08,-0.01,2.14,-0.8,-0.09,2.14,-0.88,0.13,1.62,-0.76,1.49,1.68,-0.8,1.34,1.68,-0.56,1.47,1.68,-0.8,1.34,1.62,-0.76,1.49,1.57,-0.8,1.45,1.75,-0.88,-1.46,1,-0.81,-1.53,0.98,-0.76,-1.55,2.05,-1,-0.91,2.04,-1.12,-0.68,1.96,-1.12,-0.95,2.12,-1.04,-0.19,2.08,-1.12,-0.24,2.08,-1.12,-0.35,1.96,-0.36,-0.27,1.95,-0.32,-0.07,2.14,-0.8,-0.09,2.04,-0.84,0.71,1.95,-0.88,0.79,1.92,-0.92,0.77,1.93,-0.84,0.89,1.87,-0.8,1.07,1.83,-0.84,1.04,1.95,-0.88,0.79,1.93,-0.84,0.89,1.89,-0.88,0.85,1.03,-0.88,-1.53,1.09,-0.92,-1.48,1.07,-0.92,-1.46,1.03,-0.88,-1.53,1.07,-0.92,-1.46,1.02,-0.88,-1.46,1.12,-0.92,-1.5,1.09,-0.92,-1.48,1.03,-0.88,-1.53,1.02,-0.92,-1.61,1.12,-0.92,-1.5,1.03,-0.88,-1.53,1.86,-0.8,-1.32,1.68,-1,-1.38,1.75,-0.88,-1.46,2.14,-0.88,0.13,2.11,-0.64,0.45,2.06,-0.96,0.37,2.03,-0.92,0.62,2.04,-0.84,0.71,1.92,-0.92,0.77,2.04,-0.84,0.71,2.03,-0.92,0.62,2.11,-0.64,0.45,1.13,-0.96,-1.41,1.12,-0.96,-1.38,1.07,-0.92,-1.46,1.07,-0.92,-1.46,1.09,-0.92,-1.48,1.13,-0.96,-1.41,1.68,-1,-1.38,1.16,-0.96,-1.42,1.75,-0.88,-1.46,2.09,-0.72,-0.31,1.94,-0.36,-0.4,1.96,-0.36,-0.27,2.04,-0.96,0.49,2.03,-0.92,0.62,1.96,-0.96,0.6,1.12,-0.96,-1.38,1.13,-0.96,-1.41,1.68,-1,-1.38,1.13,-0.96,-1.41,1.16,-0.96,-1.42,1.68,-1,-1.38,1.86,-0.8,-1.32,1.92,-0.76,-1.15,1.96,-0.92,-1.1,1.86,-0.8,-1.32,1.74,-1.08,-1.27,1.68,-1,-1.38,2.06,-1.04,0.15,2.07,-1.08,-0.01,2.14,-0.88,0.13,2.09,-1.08,-0.11,2.12,-1.04,-0.19,2.14,-0.8,-0.09,2.04,-0.96,0.49,2.11,-0.64,0.45,2.03,-0.92,0.62,2.04,-0.96,0.49,2.06,-0.96,0.37,2.11,-0.64,0.45,1.91,-1.04,0.4,2,-1.04,0.3,2.06,-0.96,0.37,1.74,-1.08,-1.27,1.96,-0.92,-1.1,1.96,-1.12,-0.95,1.96,-1.12,-0.95,1.96,-0.92,-1.1,2.05,-1,-0.91,1.99,-1.16,-0.61,2.04,-1.12,-0.68,2.13,-1,-0.45,2.04,-1.16,-0.4,2.08,-1.12,-0.35,2.03,-1.16,-0.33,2.12,-1.04,-0.19,2.08,-1.12,-0.35,2.13,-1,-0.45,1.95,-0.64,-0.88,1.93,-0.4,-0.5,2.09,-0.72,-0.31,2.06,-1.04,0.15,2.06,-0.96,0.37,2,-1.04,0.3,2.06,-1.04,0.15,2.14,-0.88,0.13,2.06,-0.96,0.37,2.07,-1.08,-0.01,2.09,-1.08,-0.11,2.14,-0.8,-0.09,1.86,-0.8,-1.32,1.96,-0.92,-1.1,1.74,-1.08,-1.27,1.95,-0.64,-0.88,2.13,-1,-0.45,2.04,-1.12,-0.68,2.13,-1,-0.45,2.08,-1.12,-0.35,2.04,-1.16,-0.4,2.08,-1.12,-0.24,2.09,-1.08,-0.11,1.99,-1.12,-0.03,2.08,-1.12,-0.24,2.12,-1.04,-0.19,2.09,-1.08,-0.11,2.12,-1.04,-0.19,2.13,-1,-0.45,2.09,-0.72,-0.31,2.09,-1.08,-0.11,2.07,-1.08,-0.01,1.99,-1.12,-0.03,2.14,-0.8,-0.09,2.12,-1.04,-0.19,2.09,-0.72,-0.31,1.99,-1.16,-0.61,2.13,-1,-0.45,2.04,-1.16,-0.4,-0.17,3.92,-0.23,-0.27,3.88,-0.24,-0.3,3.88,-0.22,-0.34,3.88,-0.14,-0.24,3.92,-0.14,-0.3,3.88,-0.22,-0.19,3.92,-0.17,-0.39,2.84,-1.48,-0.43,2.92,-1.39,-0.3,3.08,-1.48,-0.42,2.8,-1.46,0.4,1.52,-1.46,0.45,1.6,-1.46,-0.33,1.72,-1.42,-0.56,2,-1.38,-0.7,2.24,-1.39,-0.56,2.6,-1.39,-0.43,2.76,-1.47,-0.42,2.8,-1.46,-0.3,3.08,-1.48,-0.18,3.24,-1.58,-0.06,3.64,-1.35,0.34,4.08,-1.45,0.49,4.16,-1.55,0.8,-0.89,1.63,-0.66,-1.04,1.37,-0.59,-1.02,1.38,-0.52,-1.01,1.4,-0.45,-1,1.41,-0.38,-0.98,1.43,-0.31,-0.97,1.44,-0.24,-0.95,1.45,-0.17,-0.94,1.47,-0.1,-0.92,1.48,-0.03,-0.91,1.5,0.04,-0.89,1.51,0.11,-0.88,1.53,0.18,-0.86,1.54,0.25,-0.85,1.55,0.32,-0.84,1.57,0.39,-0.82,1.58,0.46,-0.81,1.6,0.53,-0.79,1.61,0.6,-0.78,1.63,0.67,-0.76,1.64,0.74,-0.75,1.66,0.73,-0.5,1.65,0.73,-0.25,1.64,0.72,0,1.63,0.72,0.25,1.62,0.71,0.5,1.62,0.7,0.75,1.61,0.82,1,1.6,0.81,1.25,1.59,0.81,1.5,1.58,0.8,1.75,1.58,0.8,2,1.57,0.79,2.24,1.56,0.78,2.49,1.55,0.78,2.74,1.54,0.77,2.99,1.54,0.77,3.24,1.53,0.76,3.49,1.52,0.76,3.74,1.51,0.75,3.99,1.5,0.75,4.24,1.49,0.67,4.1,1.53,0.23,-0.84,1.56,-0.66,-0.92,1.37,0.26,-1,1.47,-0.76,-0.88,1.37,0.23,-0.84,1.56,0.26,-0.8,1.5,-0.84,-0.84,1.38,0.27,-0.64,1.49,-0.9,-0.8,1.32,0.23,-0.84,1.56,-0.19,-1,1.47,0.06,4.1,1.53,0,4.14,1.44,0.49,4.24,1.44,0.45,4.2,1.54,0.37,4.16,1.6,0.2,4.08,1.43,0.15,3.88,1.52,0,3.88,1.34,-0.06,3.76,1.52,0.16,3.44,1.5,-0.35,3.04,1.55,0.16,2.96,1.52,0.19,2.56,1.51,0.14,2.43,1.63,0.18,2.31,1.61,0.18,2.16,1.39,0.17,2.06,1.67,0.24,1.74,1.45,0.24,1.52,1.49,0.21,1.08,1.57,0.22,0.91,1.51,-0.53,1.2,1.53,0.24,0.92,1.59,0.31,0.56,1.34,0.18,0.36,1.66,0.22,0.24,1.63,0.24,0.12,1.62,-0.24,0,1.51,0.24,0,1.49,0.22,-0.32,1.52,0.24,-0.48,1.49,0.27,-0.64,1.49,0.26,-0.8,1.5,0.24,-0.48,1.49,0.22,-0.32,1.52,-1.02,-0.36,1,0.22,0.24,1.63,0.18,0.36,1.66,0.31,0.56,1.34,0.16,2.96,1.52,-0.64,2.84,1.24,0.19,2.56,1.51,0.2,4.08,1.43,0,3.88,1.34,0.15,3.88,1.52,0.75,4.24,1.49,0,4.14,1.44,-0.03,4.1,1.53,0.2,4.08,1.43,0.37,4.16,1.6,0.45,4.2,1.54,0.62,4.2,1.5,0.77,4.16,1.6,0.7,4.12,1.5,0.87,3.8,-1.74,1.23,3.96,-1.51,0.82,4.05,-1.6,0.57,4.2,-1.42,0.55,4.2,-1.35,0.62,4.24,-1.29,0.58,4.24,-1.21,0.63,4.28,-1.13,0.68,4.28,-1.17,0.69,4.32,-1.08,0.6,4.32,-1,0.48,4.28,-1.02,0.49,4.32,-0.97,0.32,4.24,-1,0.16,4.28,-0.9,0.03,4.2,-0.77,0.17,4.2,-0.89,0.26,4.16,-0.85,0.25,4.16,-0.79,0.14,4.16,-0.71,0.09,4.16,-0.72,0.03,4.2,-0.77,-0.01,4.32,-0.69,-0.08,4.28,-0.6,0.02,4.32,-0.46,-0.04,4.4,-0.4,-0.09,4.2,-0.28,-0.19,4.04,-0.09,-0.16,4.08,0.09,-0.24,4.04,0.06,-0.29,4.04,0.12,-0.22,4.08,0.21,-0.16,4.08,0.09,-0.17,4.12,0.2,-0.24,4.12,0.27,-0.21,4.16,0.32,-0.12,4.16,0.32,-0.04,4.28,0.38,-0.01,4.32,0.47,-0.12,4.28,0.52,-0.03,4.36,0.6,0.01,4.36,0.68,0.27,4.32,0.83,0.36,4.24,1.06,0.55,4.32,1.18,0.57,4.32,1.2,0.59,4.32,1.23,0.51,4.28,1.28,0.53,4.28,1.34,0.62,4.32,1.31,0.7,4.32,1.37,0.75,4.24,1.49,0.75,3.99,1.5,0.76,3.74,1.51,0.76,3.49,1.52,0.77,3.24,1.53,0.77,2.99,1.54,0.78,2.74,1.54,0.78,2.49,1.55,0.79,2.24,1.56,0.8,2,1.57,0.8,1.75,1.58,0.81,1.5,1.58,0.81,1.25,1.59,0.82,1,1.6,0.7,0.75,1.61,0.71,0.5,1.62,0.72,0.25,1.62,0.72,0,1.63,0.73,-0.25,1.64,0.73,-0.5,1.65,0.74,-0.75,1.66,0.67,-0.76,1.64,0.6,-0.78,1.63,0.53,-0.79,1.61,0.46,-0.81,1.6,0.39,-0.82,1.58,0.32,-0.84,1.57,0.25,-0.86,1.55,0.18,-0.86,1.54,0.11,-0.88,1.53,0.04,-0.89,1.51,-0.03,-0.91,1.5,-0.1,-0.92,1.48,-0.17,-0.94,1.47,-0.24,-0.95,1.45,-0.31,-0.97,1.44,-0.38,-0.98,1.43,-0.45,-1,1.41,-0.52,-1.01,1.4,-0.59,-1.02,1.38,-0.66,-1.04,1.37,-0.73,-1.04,1.16,-0.76,-1,1.03,-0.82,-1.12,1.04,-0.94,-1.08,1.01,-0.86,-1,0.63,-0.96,-1,0.37,-0.96,-0.92,0.04,-0.98,-0.88,-0.17,-0.88,-0.96,-0.36,-0.86,-1.04,-0.58,-0.86,-1.04,-0.62,-0.85,-1.08,-0.65,-0.82,-0.92,-0.7,-0.75,-1.16,-0.84,-0.73,-1.08,-1.02,-0.76,-1,-1.16,-0.78,-1.08,-1.18,-0.66,-1.08,-1.19,0.36,-1.04,-1.34,0.3,-1,-1.59,0.19,-0.96,-1.33,-0.74,-0.96,-1.26,-0.83,-0.92,-1.22,-0.76,-0.92,-1.1,-0.71,-0.88,-0.94,-0.77,-0.88,-0.79,-0.81,-0.84,-0.81,-0.81,-0.84,-0.72,-0.86,-0.8,-0.7,-0.83,-0.8,-0.64,-0.83,-0.8,-0.53,-0.95,-0.8,-0.18,-1.03,-0.76,-0.22,-1.07,-0.76,-0.08,-1.04,-0.76,0.13,-1,-0.76,0.41,-0.99,-0.76,0.5,-0.88,-0.8,0.5,-0.85,-0.8,0.77,-0.91,-0.8,0.92,-0.83,-0.8,0.94,-0.88,-0.8,1.01,-0.85,-0.8,1.06,-0.8,-0.84,1,-0.76,-0.84,1,-0.73,-0.84,1.09,-0.79,-0.84,1.26,-0.7,-0.88,1.21,-0.71,-0.88,1.29,-0.76,-0.88,1.37,-0.84,-0.84,1.38,-0.85,-0.84,1.33,-0.9,-0.8,1.32,-0.93,-0.8,1.2,-0.98,-0.76,1.23,-1.01,-0.76,1.1,-1.04,-0.76,0.8,-1.03,-0.76,0.76,-1.11,-0.72,0.76,-1.12,-0.72,0.7,-1.02,-0.76,0.67,-1.06,-0.76,0.63,-1.04,-0.76,0.59,-1.12,-0.72,0.63,-1.15,-0.72,0.43,-1.19,-0.72,0.13,-1.19,-0.72,-0.23,-1.16,-0.72,-0.48,-1.1,-0.76,-0.55,-1.09,-0.76,-0.73,-1.08,-0.76,-0.84,-1.01,-0.8,-0.91,-1.02,-0.8,-0.99,-0.89,-0.88,-1.13,-0.9,-0.88,-1.17,-0.83,-0.92,-1.22,-0.85,-0.92,-1.28,0.19,-0.96,-1.33,0.22,-0.72,-1.5,0.22,-0.52,-1.37,0.41,-0.12,-1.66,0.33,0.28,-1.54,0.3,0.44,-1.52,0.38,0.76,-1.58,0.29,0.84,-1.5,0.32,1.04,-1.51,0.37,1.24,-1.41,0.35,1.44,-1.49,0.4,1.52,-1.46,0.49,4.16,-1.55,0.48,4.16,-1.45,0.22,0.04,-1.51,0.41,-0.12,-1.66,0.17,-0.04,-1.51,0.89,4.28,-1.19,0.93,4.24,-1.26,0.92,4.2,-1.36,0.89,4.2,-1.42,0.82,4.16,-1.49,1.23,3.96,-1.51,0.87,3.8,-1.74,1.52,3.68,-1.56,1.68,3.4,-1.54,1.75,3.2,-1.57,0.87,3.04,-1.55,0.86,2.72,-1.49,0.87,2.32,-1.67,0.94,2.24,-1.51,0.9,2.08,-1.48,0.89,2,-1.58,0.87,1.92,-1.58,1.55,1.84,-1.58,0.86,1.86,-1.6,0.88,1.78,-1.58,0.86,1.7,-1.56,0.82,1.66,-1.6,0.82,1.58,-1.58,0.78,1.63,-1.53,0.82,1.5,-1.6,1.35,1.2,-1.59,0.81,1.3,-1.49,1.1,1.08,-1.61,0.85,0.92,-1.52,0.97,0.8,-1.46,0.93,0.88,-1.43,0.95,0.88,-1.41,0.95,0.92,-1.41,1.4,0.92,-1.37,1.41,0.96,-1.37,1.43,0.96,-1.35,1.43,1,-1.35,1.44,1,-1.32,1.45,1.04,-1.33,1.52,1.04,-1.27,1.53,1.08,-1.28,1.64,1.04,-1.28,1.55,0.96,-1.32,1.54,0.88,-1.39,0.97,0.8,-1.46,0.95,0.75,-1.66,0.93,0.7,-1.48,0.93,0.57,-1.53,0.99,0.36,-1.65,0.96,0.2,-1.45,0.96,0.05,-1.6,0.94,-0.03,-1.54,0.94,-0.07,-1.47,0.95,-0.1,-1.43,0.94,-0.12,-1.46,0.97,-0.2,-1.54,0.99,-0.32,-1.68,0.96,-0.56,-1.48,0.98,-0.76,-1.55,1,-0.81,-1.53,1.16,-0.96,-1.42,1.13,-0.96,-1.41,1.09,-0.92,-1.48,1.12,-0.92,-1.5,1.02,-0.92,-1.61,1.03,-0.88,-1.53,1.02,-0.88,-1.46,1.07,-0.92,-1.46,1.12,-0.96,-1.38,1.68,-1,-1.38,1.74,-1.08,-1.27,1.96,-1.12,-0.95,2.04,-1.12,-0.68,1.99,-1.16,-0.61,2.04,-1.16,-0.4,2.03,-1.16,-0.33,2.08,-1.12,-0.35,2.08,-1.12,-0.24,1.99,-1.12,-0.03,2.07,-1.08,-0.01,2,-1.08,0.11,2.06,-1.04,0.15,2,-1.04,0.3,1.91,-1.04,0.4,2.06,-0.96,0.37,2.04,-0.96,0.49,1.96,-0.96,0.6,2.03,-0.92,0.62,1.92,-0.92,0.77,1.95,-0.88,0.79,1.89,-0.88,0.85,1.93,-0.84,0.89,1.83,-0.84,1.04,1.87,-0.8,1.07,1.68,-0.8,1.34,1.57,-0.8,1.45,1.62,-0.76,1.49,1.49,-0.76,1.58,0.74,-0.76,1.68,0.72,-0.58,1.64,1.27,-0.28,1.56,0.66,-0.08,1.48,0.71,0.21,1.65,0.67,0.52,1.51,0.66,0.6,1.62,0.65,0.6,1.54,0.67,0.92,1.6,0.68,1.12,1.61,0.66,1.28,1.6,0.67,1.36,1.59,0.68,1.48,1.64,0.67,1.52,1.53,0.68,1.56,1.65,0.67,1.6,1.59,0.67,1.64,1.55,0.68,1.74,1.63,0.68,1.88,1.6,0.69,1.92,1.59,0.7,2,1.62,0.71,2.16,1.61,0.72,2.28,1.64,0.71,2.44,1.6,1.61,2.4,1.49,0.73,2.44,1.58,0.74,2.48,1.58,0.75,2.6,1.59,0.72,2.71,1.55,0.75,2.86,1.6,0.72,2.91,1.51,0.74,3.02,1.64,0.71,3.1,1.57,0.7,3.1,1.6,0.7,3.23,1.56,0.72,3.34,1.59,0.71,3.5,1.52,0.76,3.6,1.62,0.7,3.6,1.52,0.73,3.68,1.6,0.66,3.76,1.48,0.7,3.88,1.65,0.7,4.12,1.5,0.77,4.16,1.6,0.62,4.2,1.5,0.6,4.24,1.45,0.63,4.24,1.44,0.63,4.28,1.31,0.59,4.32,1.24,0.63,4.32,1.2,0.65,4.32,1.17,0.95,4.32,1.01,1.07,4.32,0.8,1.13,4.44,0.45,1.36,4.16,0.16,1.17,4.4,-0.51,1.08,4.4,-0.74,1,4.4,-0.86,0.99,4.32,-1.01,0.95,4.32,-1.05,0.92,4.2,-1.36,1.23,3.96,-1.51,0.82,4.16,-1.49,0.82,4.16,-1.49,0.89,4.2,-1.42,0.92,4.2,-1.36,0.92,4.2,-1.36,0.93,4.24,-1.26,1.18,4.12,-1.14,0.96,4.28,-1.1,0.93,4.24,-1.26,0.89,4.28,-1.19,0.95,4.32,-1.05,0.96,4.28,-1.1,0.89,4.28,-1.19,0.96,4.28,-1.1,0.95,4.32,-1.05,0.99,4.32,-1.01,0.99,4.32,-1.01,1,4.4,-0.86,1.35,4.08,-0.89,1,4.4,-0.86,1.08,4.4,-0.74,1.35,4.08,-0.89,1.08,4.4,-0.74,1.17,4.4,-0.51,1.35,4.08,-0.89,1.41,3.92,0.82,1.36,4.16,0.16,1.13,4.44,0.45,1.41,3.92,0.82,1.13,4.44,0.45,1.07,4.32,0.8,0.84,4.4,0.99,0.95,4.32,1.01,0.78,4.36,1.14,0.74,4.44,1.05,0.84,4.4,0.99,0.72,4.4,1.1,0.72,4.4,1.1,0.62,4.4,1.06,0.74,4.44,1.05,0.55,4.32,1.18,0.62,4.4,1.06,0.54,4.4,1,0.36,4.24,1.06,0.54,4.4,1,0.55,4.32,1.18,-0.24,4.12,0.27,-0.17,4.12,0.2,-0.22,4.08,0.21,0.49,4.32,-0.97,0.48,4.28,-1.02,0.32,4.24,-1,1.04,4.12,1.39,0.7,3.88,1.65,0.66,3.76,1.48,0.72,2.71,1.55,0.72,2.91,1.51,0.75,2.86,1.6,0.71,0.21,1.65,1.33,0.2,1.41,0.67,0.52,1.51,1.33,0.2,1.41,0.71,0.21,1.65,0.66,-0.08,1.48,0.74,-0.76,1.68,1.49,-0.76,1.58,1.68,-0.56,1.47,-0.66,-1.04,1.37,0.26,-1,1.47,-0.66,-0.92,1.37,-0.12,4.2,-0.39,-0.04,4.4,-0.4,0.02,4.32,-0.46,-0.07,4.24,-0.7,-0.08,4.28,-0.6,-0.01,4.32,-0.69,0.62,4.32,1.31,0.53,4.28,1.34,0,4.14,1.44,0.62,4.32,1.31,0,4.14,1.44,0.75,4.24,1.49,0.7,4.32,1.37,0.62,4.32,1.31,0.75,4.24,1.49,0.2,4.08,1.43,0.41,4.24,1.31,0.36,4.24,1.06,0.57,4.32,1.2,0.55,4.32,1.18,0.49,4.17,1.2,0.03,4.2,-0.77,-0.02,4.2,-0.74,-0.01,4.32,-0.69,0.69,4.32,-1.08,0.63,4.28,-1.13,0.6,4.32,-1,0.6,4.32,-1,0.63,4.28,-1.13,0.48,4.28,-1.02,0.63,4.28,-1.13,0.69,4.32,-1.08,0.68,4.28,-1.17,0.49,4.24,1.44,0.41,4.24,1.31,0.2,4.08,1.43,0.51,4.28,1.28,0.41,4.24,1.31,0.53,4.28,1.34,0.36,4.24,1.06,0.49,4.17,1.2,0.55,4.32,1.18,0.51,4.28,1.28,0.59,4.32,1.23,0.57,4.32,1.2,0.49,4.17,1.2,0.51,4.28,1.28,0.57,4.32,1.2,-0.12,4.2,-0.39,-0.09,4.2,-0.28,-0.04,4.4,-0.4,-0.07,4.24,-0.7,0.01,4.12,-0.63,-0.16,4.16,-0.57,0.16,4.28,-0.9,0.32,4.24,-1,0.25,4.16,-0.9,0.17,4.2,-0.89,0.16,4.28,-0.9,0.25,4.16,-0.9,0,4.14,1.44,0.53,4.28,1.34,0.49,4.24,1.44,0.2,4.08,1.43,0.04,4.04,0.81,0,3.88,1.34,0.49,4.24,1.44,0.2,4.08,1.43,0.45,4.2,1.54,0.06,4.2,0.68,0.04,4.04,0.81,0.27,4.32,0.83,0.2,4.08,1.43,0.36,4.24,1.06,0.04,4.04,0.81,-0.03,4.36,0.6,0.06,4.2,0.68,0.01,4.36,0.68,-0.03,4.36,0.6,-0.12,4.28,0.52,0.06,4.2,0.68,-0.04,4.28,0.38,-0.12,4.28,0.52,-0.01,4.32,0.47,-0.21,4.16,0.32,-0.2,4.2,0.39,-0.12,4.16,0.32,-0.16,4.2,-0.54,-0.12,4.2,-0.39,0.02,4.32,-0.46,-0.08,4.28,-0.6,-0.16,4.16,-0.57,-0.16,4.2,-0.54,-0.07,4.24,-0.7,-0.01,4.32,-0.69,-0.02,4.2,-0.74,-0.08,4.28,-0.6,-0.16,4.2,-0.54,0.02,4.32,-0.46,-0.08,4.28,-0.6,-0.07,4.24,-0.7,-0.16,4.16,-0.57,0.03,4.2,-0.77,0.16,4.28,-0.9,0.17,4.2,-0.89,0.19,4.12,-0.83,0.26,4.16,-0.85,0.25,4.16,-0.9,0.25,4.16,-0.9,0.26,4.16,-0.85,0.17,4.2,-0.89,0.43,4.16,-1.22,0.32,4.24,-1,0.48,4.28,-1.02,0.58,4.24,-1.21,0.48,4.28,-1.02,0.63,4.28,-1.13,0.49,4.24,1.44,0.53,4.28,1.34,0.41,4.24,1.31,0.41,4.24,1.31,0.51,4.28,1.28,0.49,4.17,1.2,-0.12,4.16,0.32,-0.2,4.2,0.39,-0.04,4.28,0.38,-0.12,4.2,-0.39,-0.16,4.2,-0.54,-0.18,4.16,-0.51,-0.18,4.16,-0.51,-0.16,4.2,-0.54,-0.16,4.16,-0.57,0.01,4.12,-0.63,-0.04,4.04,-0.56,-0.16,4.16,-0.57,0.58,4.24,-1.21,0.62,4.24,-1.29,0.55,4.2,-1.35,-0.12,4.28,0.52,-0.18,4.16,0.48,-0.04,4.12,0.57,-0.21,4.16,0.32,-0.26,4.12,0.35,-0.2,4.2,0.39,-0.26,4.12,0.35,-0.21,4.16,0.32,-0.24,4.12,0.27,-0.09,4.2,-0.28,-0.22,4.08,-0.32,-0.17,4,-0.19,-0.04,4.04,-0.56,0.01,4.12,-0.63,0.04,4.04,-0.72,0.03,4.2,-0.77,0.09,4.16,-0.72,-0.02,4.2,-0.74,0.09,4.16,-0.72,0.14,4.16,-0.71,0.12,4.12,-0.69,0.14,4.16,-0.71,0.25,4.16,-0.79,0.19,4.12,-0.83,0.26,4.16,-0.85,0.19,4.12,-0.83,0.25,4.16,-0.79,0.19,4.12,-0.83,0.22,4.04,-1,0.13,4.08,-0.84,0.19,4.12,-0.83,0.25,4.16,-0.9,0.22,4.04,-1,0.58,4.24,-1.21,0.55,4.2,-1.35,0.43,4.16,-1.22,0.58,4.24,-1.21,0.43,4.16,-1.22,0.48,4.28,-1.02,0.48,4.16,-1.45,0.43,4.16,-1.22,0.55,4.2,-1.35,0.48,4.16,-1.45,0.55,4.2,-1.35,0.57,4.2,-1.42,0.48,4.16,-1.45,0.49,4.16,-1.55,0.34,4.08,-1.45,0.04,4.04,0.81,0.36,4.24,1.06,0.27,4.32,0.83,0.04,4.04,0.81,0.06,4.2,0.68,-0.04,4.12,0.57,-0.2,4.2,0.39,-0.18,4.16,0.48,-0.12,4.28,0.52,-0.04,4.28,0.38,-0.2,4.2,0.39,-0.12,4.28,0.52,-0.25,4.08,0.32,-0.26,4.12,0.35,-0.24,4.12,0.27,-0.22,4.08,0.21,-0.17,4.12,0.2,-0.16,4.08,0.09,-0.22,4.08,-0.32,-0.09,4.2,-0.28,-0.12,4.2,-0.39,-0.07,4.24,-0.7,-0.02,4.2,-0.74,0.01,4.12,-0.63,0.01,4.12,-0.63,0.09,4.16,-0.72,0.1,4.08,-0.68,0.09,4.16,-0.72,0.12,4.12,-0.69,0.1,4.08,-0.68,0.01,4.12,-0.63,-0.02,4.2,-0.74,0.09,4.16,-0.72,0.04,4.04,-0.72,0.1,4.08,-0.68,0.13,4.08,-0.84,0.13,4.08,-0.84,0.12,4.12,-0.69,0.14,4.16,-0.71,0.04,4.04,-0.72,0.13,4.08,-0.84,0.05,3.92,-0.87,0.22,4.04,-1,0.25,4.16,-0.9,0.32,4.24,-1,-0.16,3.92,0.5,0.04,4.04,0.81,-0.04,4.12,0.57,-0.13,4.04,0.43,-0.18,4.16,0.48,-0.2,4.2,0.39,-0.18,4.16,0.48,-0.13,4.04,0.43,-0.04,4.12,0.57,-0.26,4.12,0.35,-0.13,4.04,0.43,-0.2,4.2,0.39,-0.22,4.08,0.21,-0.13,4,0.27,-0.25,4.08,0.32,-0.24,4.12,0.27,-0.22,4.08,0.21,-0.25,4.08,0.32,-0.24,4.04,0.06,-0.16,4.08,0.09,-0.19,4.04,-0.09,0.01,4.12,-0.63,0.1,4.08,-0.68,0.04,4.04,-0.72,0.34,4.08,-1.45,0.43,4.16,-1.22,0.48,4.16,-1.45,0.36,4.24,1.06,0.41,4.24,1.31,0.49,4.17,1.2,0.06,4.2,0.68,0.27,4.32,0.83,0.01,4.36,0.68,-0.18,3.96,0.12,-0.24,4.04,0.06,-0.31,3.88,0.03,-0.18,3.96,0.12,-0.2,4,0.14,-0.24,4.04,0.06,-0.24,4.04,0.06,-0.19,4.04,-0.09,-0.19,3.96,-0.1,-0.17,4,-0.19,-0.19,4.04,-0.09,-0.09,4.2,-0.28,-0.13,3.84,-0.59,-0.25,3.88,-0.3,-0.15,3.96,-0.34,-0.18,4.16,-0.51,-0.16,4.16,-0.57,-0.04,4.04,-0.56,0.13,4.08,-0.84,0.14,4.16,-0.71,0.19,4.12,-0.83,-0.06,3.64,-1.35,0.05,3.92,-0.87,0.22,4.04,-1,-0.2,4,0.14,-0.18,3.96,0.12,-0.17,3.96,0.14,-0.2,4,0.14,-0.17,3.96,0.14,-0.17,3.96,0.18,-0.2,4,0.14,-0.17,3.96,0.18,-0.22,4.08,0.21,-0.2,4,0.14,-0.29,4.04,0.12,-0.24,4.04,0.06,-0.22,4.08,0.21,-0.29,4.04,0.12,-0.2,4,0.14,-0.24,4.04,0.06,-0.19,3.96,-0.1,-0.31,3.88,0.03,-0.19,3.96,-0.1,-0.17,4,-0.19,-0.19,3.92,-0.17,-0.19,3.96,-0.1,-0.19,4.04,-0.09,-0.17,4,-0.19,-0.15,3.92,-0.29,-0.17,3.92,-0.23,-0.17,4,-0.19,-0.25,3.88,-0.3,-0.15,3.92,-0.29,-0.15,3.96,-0.34,-0.04,4.04,-0.56,0.04,4.04,-0.72,-0.13,3.84,-0.59,0.1,4.08,-0.68,0.12,4.12,-0.69,0.13,4.08,-0.84,0.34,4.08,-1.45,0.22,4.04,-1,0.43,4.16,-1.22,0,3.88,1.34,0.04,4.04,0.81,-0.59,3.2,0.62,-0.25,4.08,0.32,-0.24,3.92,0.3,-0.13,4.04,0.43,-0.17,3.96,0.18,-0.13,4,0.27,-0.22,4.08,0.21,-0.17,3.96,0.18,-0.24,3.92,0.3,-0.13,4,0.27,-0.26,3.92,0.17,-0.17,3.96,0.18,-0.17,3.96,0.14,-0.18,3.96,0.12,-0.31,3.88,0.03,-0.26,3.92,0.17,-0.31,3.88,0.03,-0.19,3.96,-0.1,-0.24,3.92,-0.14,-0.24,3.92,-0.14,-0.19,3.96,-0.1,-0.19,3.92,-0.17,-0.17,3.92,-0.23,-0.19,3.92,-0.17,-0.17,4,-0.19,-0.15,3.96,-0.34,-0.17,4,-0.19,-0.22,4.08,-0.32,0,3.88,1.34,-0.59,3.2,0.62,-0.65,3.04,0.92,-0.26,4.12,0.35,-0.25,4.08,0.32,-0.13,4.04,0.43,-0.13,4,0.27,-0.24,3.92,0.3,-0.25,4.08,0.32,-0.26,3.92,0.17,-0.17,3.96,0.14,-0.18,3.96,0.12,-0.26,3.92,0.17,-0.31,3.88,0.03,-0.28,3.8,0.26,-0.31,3.88,0.03,-0.39,3.72,-0.03,-0.28,3.8,0.26,-0.3,3.88,-0.22,-0.24,3.92,-0.14,-0.19,3.92,-0.17,-0.15,3.92,-0.29,-0.25,3.88,-0.3,-0.17,3.92,-0.23,-0.15,3.96,-0.34,-0.15,3.92,-0.29,-0.17,4,-0.19,-0.04,4.04,-0.56,-0.13,3.84,-0.59,-0.15,3.96,-0.34,-0.18,4.16,-0.51,-0.04,4.04,-0.56,-0.22,4.08,-0.32,-0.17,3.96,0.18,-0.26,3.92,0.17,-0.24,3.92,0.3,-0.26,3.92,0.17,-0.28,3.8,0.26,-0.24,3.92,0.3,-0.34,3.88,-0.14,-0.31,3.88,0.03,-0.24,3.92,-0.14,-0.31,3.84,-0.24,-0.39,3.8,-0.15,-0.34,3.88,-0.14,-0.3,3.88,-0.22,-0.31,3.84,-0.24,-0.34,3.88,-0.14,-0.31,3.84,-0.24,-0.3,3.88,-0.22,-0.27,3.88,-0.24,-0.25,3.88,-0.3,-0.31,3.84,-0.24,-0.27,3.88,-0.24,-0.18,4.16,-0.51,-0.22,4.08,-0.32,-0.12,4.2,-0.39,-0.24,3.92,0.3,-0.16,3.92,0.5,-0.13,4.04,0.43,-0.34,3.88,-0.14,-0.39,3.8,-0.15,-0.31,3.88,0.03,-0.34,3.68,-0.3,-0.31,3.84,-0.24,-0.25,3.88,-0.3,0.22,4.04,-1,0.05,3.92,-0.87,0.13,4.08,-0.84,-0.28,3.8,0.26,-0.16,3.92,0.5,-0.24,3.92,0.3,-0.34,3.68,-0.3,-0.39,3.8,-0.15,-0.31,3.84,-0.24,-0.27,3.88,-0.24,-0.17,3.92,-0.23,-0.25,3.88,-0.3,0.04,4.04,-0.72,0.05,3.92,-0.87,-0.13,3.84,-0.59,0.43,4.16,-1.22,0.22,4.04,-1,0.32,4.24,-1,-0.12,4.28,0.52,-0.04,4.12,0.57,0.06,4.2,0.68,-0.7,3.16,0.15,-0.69,3.08,0.51,-0.59,3.2,0.62,-0.59,3.36,-0.19,-0.36,3.28,-1.18,-0.71,2.8,-1,-0.39,3.72,-0.03,-0.7,3.16,0.15,-0.28,3.8,0.26,-0.16,3.92,0.5,-0.04,4.12,0.57,-0.13,4.04,0.43,-0.39,3.72,-0.03,-0.39,3.8,-0.15,-0.34,3.68,-0.3,-0.59,3.36,-0.19,-0.71,2.8,-1,-0.93,2.52,-0.68,0.04,4.04,0.81,-0.16,3.92,0.5,-0.59,3.2,0.62,-0.06,3.64,-1.35,-0.18,3.24,-1.58,-0.36,3.28,-1.18,0.16,3.44,1.5,0,3.88,1.34,-0.65,3.04,0.92,-0.39,3.72,-0.03,-0.34,3.68,-0.3,-0.59,3.36,-0.19,-0.04,4.04,-0.56,-0.15,3.96,-0.34,-0.22,4.08,-0.32,0,3.88,1.34,0.16,3.44,1.5,-0.06,3.76,1.52,-0.59,3.36,-0.19,-0.34,3.68,-0.3,-0.36,3.28,-1.18,-0.36,3.28,-1.18,-0.57,2.92,-1.23,-0.71,2.8,-1,-0.39,3.8,-0.15,-0.39,3.72,-0.03,-0.31,3.88,0.03,-0.7,3.16,0.15,-0.59,3.2,0.62,-0.28,3.8,0.26,-0.13,3.84,-0.59,-0.34,3.68,-0.3,-0.25,3.88,-0.3,-0.06,3.64,-1.35,0.22,4.04,-1,0.34,4.08,-1.45,0.05,3.92,-0.87,-0.06,3.64,-1.35,-0.13,3.84,-0.59,-0.69,3.08,0.51,-0.7,3.16,0.15,-0.83,2.88,0.31,-0.39,3.72,-0.03,-0.59,3.36,-0.19,-0.7,3.16,0.15,-0.59,3.36,-0.19,-0.84,2.84,0.06,-0.7,3.16,0.15,0.16,2.96,1.52,-0.35,3.04,1.55,0.16,3.44,1.5,-0.13,3.84,-0.59,-0.06,3.64,-1.35,-0.36,3.28,-1.18,-0.18,3.24,-1.58,-0.3,3.08,-1.48,-0.36,3.28,-1.18,-0.16,3.92,0.5,-0.28,3.8,0.26,-0.59,3.2,0.62,-0.7,3.16,0.15,-0.84,2.84,0.06,-0.83,2.88,0.31,-0.71,3.04,0.56,-0.69,3.04,0.69,-0.59,3.2,0.62,-0.69,3.08,0.51,-0.71,3.04,0.56,-0.59,3.2,0.62,-0.71,2.8,-1,-0.82,2.56,-1.09,-0.9,2.48,-0.97,-0.69,3.04,0.69,-0.71,3.04,0.56,-0.73,3,0.58,-0.73,3,0.54,-0.71,3.04,0.56,-0.69,3.08,0.51,-0.73,3,0.54,-0.69,3.08,0.51,-0.83,2.88,0.31,-0.59,3.2,0.62,-0.69,3.04,0.69,-0.65,3.04,0.92,-0.73,3,0.54,-0.73,3,0.58,-0.71,3.04,0.56,0.16,2.96,1.52,0.16,3.44,1.5,-0.65,3.04,0.92,-0.79,2.92,0.57,-0.73,3,0.54,-0.83,2.88,0.31,-0.34,3.68,-0.3,-0.13,3.84,-0.59,-0.36,3.28,-1.18,-0.73,3,0.58,-0.73,3,0.54,-0.79,2.92,0.57,-0.57,2.92,-1.23,-0.36,3.28,-1.18,-0.43,2.92,-1.39,-0.3,3.08,-1.48,-0.43,2.92,-1.39,-0.36,3.28,-1.18,-0.69,3.04,0.69,-0.83,2.8,0.86,-0.65,3.04,0.92,-0.65,3.04,0.92,-0.64,2.84,1.24,0.16,2.96,1.52,-0.82,2.56,-1.09,-0.71,2.8,-1,-0.54,2.76,-1.37,-1.03,2.44,0.56,-0.79,2.92,0.57,-0.83,2.88,0.31,-0.69,3.04,0.69,-0.73,3,0.58,-0.79,2.92,0.57,-0.43,2.92,-1.39,-0.39,2.84,-1.48,-0.42,2.8,-1.46,-0.65,3.04,0.92,-0.83,2.8,0.86,-0.64,2.84,1.24,-1.01,2.48,0.74,-0.83,2.8,0.86,-0.79,2.92,0.57,-0.82,2.56,-1.09,-0.54,2.76,-1.37,-0.56,2.6,-1.39,-0.42,2.8,-1.46,-0.54,2.76,-1.37,-0.43,2.92,-1.39,-0.75,2.64,1.21,-0.64,2.84,1.24,-0.83,2.8,0.86,-0.57,2.92,-1.23,-0.43,2.92,-1.39,-0.54,2.76,-1.37,-1.03,2.44,0.56,-1.01,2.48,0.74,-0.79,2.92,0.57,-0.93,2.52,-0.68,-0.71,2.8,-1,-0.9,2.48,-0.97,-0.79,2.92,0.57,-0.83,2.8,0.86,-0.69,3.04,0.69,-1.01,2.48,0.74,-0.9,2.6,0.98,-0.83,2.8,0.86,-0.42,2.8,-1.46,-0.43,2.76,-1.47,-0.54,2.76,-1.37,-0.75,2.64,1.21,-0.83,2.8,0.86,-0.9,2.6,0.98,-0.59,3.36,-0.19,-0.93,2.52,-0.68,-0.84,2.84,0.06,-0.82,2.56,-1.09,-0.56,2.6,-1.39,-0.84,2.4,-1.19,-0.83,2.2,-1.26,-0.88,2.28,-1.18,-0.84,2.4,-1.19,-0.56,2.6,-1.39,-0.54,2.76,-1.37,-0.43,2.76,-1.47,-0.84,2.84,0.06,-1.04,2.32,0.21,-0.83,2.88,0.31,-0.71,2.8,-1,-0.57,2.92,-1.23,-0.54,2.76,-1.37,-0.9,2.6,0.98,-1.01,2.48,0.74,-1,2.28,0.99,-0.84,2.4,-1.19,-0.87,2.4,-1.13,-0.82,2.56,-1.09,-0.55,2,1.33,0.18,2.31,1.61,0.14,2.43,1.63,-0.9,2.6,0.98,-1,2.28,0.99,-0.96,2.28,1.1,-0.75,2.64,1.21,-0.55,2,1.33,0.14,2.43,1.63,-1.04,2.32,0.21,-0.84,2.84,0.06,-0.93,2.52,-0.68,-0.75,2.64,1.21,-0.96,2.28,1.1,-0.55,2,1.33,-1.01,2.12,-0.75,-0.93,2.52,-0.68,-0.9,2.48,-0.97,-1.01,2.12,-0.75,-0.9,2.48,-0.97,-0.93,2.32,-1.03,-0.87,2.4,-1.13,-0.9,2.48,-0.97,-0.82,2.56,-1.09,-0.88,2.36,-1.14,-0.89,2.36,-1.12,-0.87,2.4,-1.13,-0.87,2.4,-1.13,-0.84,2.4,-1.19,-0.88,2.36,-1.14,-0.88,2.28,-1.18,-0.88,2.36,-1.14,-0.84,2.4,-1.19,-1.06,2.04,0.69,-1,2.28,0.99,-1.01,2.48,0.74,-0.87,2.4,-1.13,-0.89,2.36,-1.12,-0.9,2.48,-0.97,-0.89,2.36,-1.12,-0.88,2.36,-1.14,-0.9,2.32,-1.12,-0.9,2.32,-1.12,-0.88,2.36,-1.14,-0.88,2.28,-1.18,-0.7,2.24,-1.39,-0.83,2.2,-1.26,-0.84,2.4,-1.19,-0.64,2.84,1.24,-0.75,2.64,1.21,0.19,2.56,1.51,-0.89,2.36,-1.12,-0.9,2.32,-1.12,-0.93,2.32,-1.03,-0.9,2.32,-1.12,-0.94,2.16,-1.03,-0.93,2.32,-1.03,-0.7,2.24,-1.39,-0.84,2.4,-1.19,-0.56,2.6,-1.39,-0.75,2.64,1.21,-0.9,2.6,0.98,-0.96,2.28,1.1,-0.9,2.32,-1.12,-0.88,2.28,-1.18,-0.94,2.16,-1.03,-0.89,2.36,-1.12,-0.93,2.32,-1.03,-0.9,2.48,-0.97,-1.06,2.04,0.69,-1.01,2.48,0.74,-1.03,2.44,0.56,-1.04,2.32,0.21,-1.03,2.44,0.56,-0.83,2.88,0.31,-0.96,2.04,1.06,-0.96,2.28,1.1,-1,2.28,0.99,-0.96,2.04,1.06,-1,2.28,0.99,-1.06,2.04,0.69,-1.01,2.12,-0.75,-0.94,2.16,-1.03,-0.92,1.48,-0.98,-0.94,2.16,-1.03,-0.88,2.28,-1.18,-0.83,2.2,-1.26,-0.75,2.64,1.21,0.14,2.43,1.63,0.19,2.56,1.51,-0.55,2,1.33,-0.9,1.96,1.2,-0.84,1.8,1.27,-1.04,2.32,0.21,-1.06,2.04,0.69,-1.03,2.44,0.56,-1.12,1.72,0.06,-1.08,1.84,0.59,-1.04,2.32,0.21,-0.94,2.16,-1.03,-1.01,2.12,-0.75,-0.93,2.32,-1.03,0.18,2.16,1.39,0.24,1.74,1.45,0.17,2.06,1.67,-0.55,2,1.33,-0.84,1.8,1.27,-0.76,1.72,1.33,-0.96,2.28,1.1,-0.9,1.96,1.2,-0.55,2,1.33,-0.83,1.68,1.2,-0.84,1.8,1.27,-0.9,1.96,1.2,-0.7,1.72,-1.35,-0.73,1.36,-1.29,-0.92,1.48,-0.98,-1.01,2.12,-0.75,-1.04,2.32,0.21,-0.93,2.52,-0.68,-0.55,2,1.33,0.18,2.16,1.39,0.18,2.31,1.61,-0.96,2.28,1.1,-0.96,2.04,1.06,-0.9,1.96,1.2,-1.01,2.12,-0.75,-0.92,1.48,-0.98,-1.08,1.4,-0.56,-0.56,2,-1.38,-0.83,2.2,-1.26,-0.7,2.24,-1.39,-0.55,2,1.33,-0.56,1.8,1.33,0.18,2.16,1.39,-0.56,1.8,1.33,-0.55,2,1.33,-0.76,1.72,1.33,-0.56,1.8,1.33,-0.76,1.72,1.33,-0.75,1.64,1.36,-1.04,2.32,0.21,-1.08,1.84,0.59,-1.06,2.04,0.69,-0.96,2.04,1.06,-1.06,2.04,0.69,-1.08,1.84,0.59,-0.86,1.6,1.03,-0.83,1.68,1.2,-0.9,1.96,1.2,-1.05,1.56,0.76,-0.86,1.6,1.03,-0.96,2.04,1.06,0.18,2.16,1.39,-0.56,1.8,1.33,-0.63,1.56,1.42,-0.4,1.52,1.41,0.18,2.16,1.39,-0.63,1.56,1.42,-0.84,1.8,1.27,-0.83,1.68,1.2,-0.76,1.72,1.33,-0.63,1.56,1.42,-0.75,1.64,1.36,-0.84,1.44,1.05,-1.05,1.56,0.76,-0.96,2.04,1.06,-1.08,1.84,0.59,-0.7,1.72,-1.35,-0.56,2,-1.38,-0.33,1.72,-1.42,-0.63,1.56,1.42,-0.56,1.8,1.33,-0.75,1.64,1.36,-0.75,1.64,1.36,-0.76,1.72,1.33,-0.83,1.68,1.2,-0.86,1.6,1.03,-0.9,1.96,1.2,-0.96,2.04,1.06,-1.08,1.4,-0.56,-1.16,1.12,0.14,-1.12,1.72,0.06,-0.7,1.72,-1.35,-0.33,1.72,-1.42,0.4,1.52,-1.46,0.21,1.08,1.57,0.24,1.52,1.49,0.24,1.74,1.45,-0.75,1.64,1.36,-0.83,1.68,1.2,-0.84,1.44,1.05,-0.73,1.36,-1.29,-0.7,1.72,-1.35,0.4,1.52,-1.46,-0.86,1.6,1.03,-1.05,1.56,0.76,-0.98,1.4,0.94,-0.7,1.72,-1.35,-0.83,2.2,-1.26,-0.56,2,-1.38,0.22,0.91,1.51,0.21,1.08,1.57,-0.4,1.52,1.41,-0.95,1.28,-0.89,-0.99,1.2,-0.81,-1.08,1.4,-0.56,0.18,2.16,1.39,-0.4,1.52,1.41,0.24,1.74,1.45,-0.63,1.4,1.46,-0.4,1.52,1.41,-0.63,1.56,1.42,-0.7,1.72,-1.35,-0.92,1.48,-0.98,-0.94,2.16,-1.03,-0.92,1.48,-0.98,-0.73,1.36,-1.29,-0.84,1.2,-1.03,-1.06,1.2,0.65,-1.05,1.56,0.76,-1.12,1.72,0.06,-1.01,2.12,-0.75,-1.12,1.72,0.06,-1.04,2.32,0.21,0.4,1.52,-1.46,-0.33,1.72,-1.42,0.45,1.6,-1.46,-0.63,1.4,1.46,-0.63,1.56,1.42,-0.84,1.44,1.05,-0.98,1.4,0.94,-1.06,1.2,0.65,-1,1.04,0.99,-1.06,1.2,0.65,-1.16,1.12,0.14,-1.12,0.76,0.44,-1.05,1.56,0.76,-1.08,1.84,0.59,-1.12,1.72,0.06,-0.7,1.72,-1.35,-0.94,2.16,-1.03,-0.83,2.2,-1.26,-0.92,1.48,-0.98,-0.9,1.2,-0.96,-0.95,1.28,-0.89,0.4,1.52,-1.46,0.35,1.44,-1.49,-0.73,1.36,-1.29,0.21,1.08,1.57,0.24,1.74,1.45,-0.4,1.52,1.41,-0.83,1.68,1.2,-0.86,1.6,1.03,-0.84,1.44,1.05,-0.84,1.44,1.05,-0.86,1.6,1.03,-0.98,1.4,0.94,-0.63,1.4,1.46,0.22,0.91,1.51,-0.4,1.52,1.41,-0.66,1.24,1.23,-0.63,1.24,1.35,-0.63,1.4,1.46,-0.66,1.24,1.23,-0.63,1.4,1.46,-0.84,1.44,1.05,-0.84,1.44,1.05,-1,1.04,0.99,-0.66,1.24,1.23,-0.92,1.48,-0.98,-0.84,1.2,-1.03,-0.9,1.2,-0.96,-0.73,1.36,-1.29,0.37,1.24,-1.41,-0.84,1.2,-1.03,-0.97,0.72,1.11,-0.84,0.56,1.27,-0.66,0.84,1.22,-0.95,1.28,-0.89,-0.92,1.16,-0.94,-0.99,1.2,-0.81,-0.63,1.24,1.35,-0.53,1.2,1.53,0.22,0.91,1.51,-0.95,1.28,-0.89,-0.9,1.2,-0.96,-0.92,1.16,-0.94,-0.92,1.48,-0.98,-0.95,1.28,-0.89,-1.08,1.4,-0.56,-0.63,1.24,1.35,-0.58,1.04,1.31,-0.53,1.2,1.53,-1.16,1.12,0.14,-1.06,1.2,0.65,-1.12,1.72,0.06,-1.14,0.52,-0.42,-1.16,1.12,0.14,-1.08,1.4,-0.56,-1.08,1.4,-0.56,-1.12,1.72,0.06,-1.01,2.12,-0.75,-0.9,1.16,-0.96,-0.92,1.16,-0.94,-0.9,1.2,-0.96,-0.92,1.08,-0.94,-0.92,1.16,-0.94,-0.9,1.16,-0.96,-0.92,1.08,-0.94,-0.9,1.16,-0.96,-0.74,0.96,-1.14,-0.9,1.16,-0.96,-0.84,1.2,-1.03,-0.74,0.96,-1.14,-1.05,1.56,0.76,-1.06,1.2,0.65,-0.98,1.4,0.94,-0.98,0.48,-0.88,-1.04,0.64,-0.73,-0.74,0.96,-1.14,-0.98,0.48,-0.88,-0.74,0.96,-1.14,0.24,0.68,-1.27,0.35,1.44,-1.49,0.37,1.24,-1.41,-0.73,1.36,-1.29,-1.06,1.2,0.65,-1.12,0.76,0.44,-1,1.04,0.99,-0.84,1.2,-1.03,-0.9,1.16,-0.96,-0.9,1.2,-0.96,-0.84,1.44,1.05,-0.98,1.4,0.94,-1,1.04,0.99,-0.99,1.2,-0.81,-0.92,1.08,-0.94,-1.04,0.64,-0.73,-0.74,0.96,-1.14,-0.84,1.2,-1.03,0.37,1.24,-1.41,-0.63,1.24,1.35,0.22,0.91,1.51,-0.63,1.4,1.46,-0.99,0.52,0.83,-1,0.68,0.94,-1.12,0.76,0.44,-1.12,0.76,0.44,-1,0.68,0.94,-1,1.04,0.99,-1.08,1.4,-0.56,-0.99,1.2,-0.81,-1.14,0.52,-0.42,-0.99,1.2,-0.81,-1.04,0.64,-0.73,-1.14,0.52,-0.42,-0.92,1.08,-0.94,-0.99,1.2,-0.81,-0.92,1.16,-0.94,0.29,0.84,-1.5,-0.74,0.96,-1.14,0.32,1.04,-1.51,0.29,0.84,-1.5,0.24,0.68,-1.27,-0.74,0.96,-1.14,-1,0.68,0.94,-0.97,0.72,1.11,-0.97,0.92,1.07,-0.74,0.96,-1.14,0.37,1.24,-1.41,0.32,1.04,-1.51,-1.18,0.6,0.34,-1.12,0.76,0.44,-1.16,1.12,0.14,0.29,0.84,-1.5,0.38,0.76,-1.58,0.24,0.68,-1.27,-0.66,1.24,1.23,-1,1.04,0.99,-0.97,0.92,1.07,-0.58,1.04,1.31,-0.63,1.24,1.35,-0.66,1.24,1.23,-1,0.68,0.94,-0.97,0.92,1.07,-1,1.04,0.99,-0.97,0.92,1.07,-0.58,1.04,1.31,-0.66,1.24,1.23,0.24,0.92,1.59,-0.58,1.04,1.31,-0.66,0.84,1.22,-0.55,0.64,1.29,0.31,0.56,1.34,0.24,0.92,1.59,-0.97,0.92,1.07,-0.97,0.72,1.11,-0.66,0.84,1.22,-0.55,0.64,1.29,-0.84,0.56,1.27,-0.72,0.44,1.34,-1.18,0.6,0.34,-1.19,0.12,0.38,-0.99,0.52,0.83,0.24,0.68,-1.27,0.38,0.76,-1.58,0.3,0.44,-1.52,-0.97,0.56,1.07,-0.99,0.52,0.83,-0.91,0.16,1.06,-1.14,0.52,-0.42,-1.18,0.6,0.34,-1.16,1.12,0.14,-0.53,1.2,1.53,-0.58,1.04,1.31,0.24,0.92,1.59,-0.84,0.56,1.27,-0.55,0.64,1.29,-0.66,0.84,1.22,-0.55,0.64,1.29,0.24,0.92,1.59,-0.66,0.84,1.22,-0.97,0.56,1.07,-0.97,0.72,1.11,-1,0.68,0.94,-0.97,0.56,1.07,-1,0.68,0.94,-0.99,0.52,0.83,0.22,0.24,1.63,0.31,0.56,1.34,-0.72,0.44,1.34,-0.55,0.64,1.29,-0.72,0.44,1.34,0.31,0.56,1.34,-0.97,0.72,1.11,-0.97,0.56,1.07,-0.84,0.56,1.27,-0.84,0.56,1.27,-0.89,0.28,1.27,-0.72,0.44,1.34,-1.1,0.32,-0.58,-1.04,0.64,-0.73,-0.98,0.48,-0.88,-0.97,0.92,1.07,-0.66,0.84,1.22,-0.58,1.04,1.31,-1.19,0.12,0.38,-1.15,0,0.54,-0.99,0.52,0.83,-1.08,0.16,-0.69,-1.1,0.32,-0.58,-0.98,0.48,-0.88,0.16,0.28,-1.44,-0.98,0.48,-0.88,0.24,0.68,-1.27,-1.14,0.52,-0.42,-1.15,0.16,-0.4,-1.18,0.6,0.34,0.16,0.28,-1.44,-0.98,0,-0.96,-0.98,0.48,-0.88,-1.08,0.16,-0.69,-1.11,0.2,-0.59,-1.1,0.32,-0.58,-0.97,0.56,1.07,-0.91,0.16,1.06,-0.89,0.28,1.27,-0.83,0.2,1.34,-0.89,0.28,1.27,-0.91,0.16,1.06,-1.12,0.24,-0.52,-1.15,0.16,-0.4,-1.14,0.52,-0.42,-1.08,0.16,-0.69,-0.98,0.48,-0.88,-0.98,0,-0.96,-1.04,0.64,-0.73,-0.92,1.08,-0.94,-0.74,0.96,-1.14,0.3,0.44,-1.52,0.33,0.28,-1.54,0.16,0.28,-1.44,-1.1,0.32,-0.58,-1.14,0.52,-0.42,-1.04,0.64,-0.73,-1.11,0.24,-0.56,-1.12,0.24,-0.52,-1.1,0.32,-0.58,0.33,0.28,-1.54,0.22,0.04,-1.51,0.16,0.28,-1.44,-1.12,0.24,-0.52,-1.11,0.24,-0.56,-1.12,0.2,-0.56,-1.11,0.2,-0.59,-1.11,0.24,-0.56,-1.1,0.32,-0.58,-1.11,0.2,-0.59,-1.08,0.16,-0.69,-1.11,0.16,-0.59,-1.11,0.2,-0.59,-1.12,0.2,-0.56,-1.11,0.24,-0.56,0.24,0.12,1.62,0.22,0.24,1.63,-0.24,0,1.51,-0.83,0.2,1.34,0.24,0,1.49,-0.72,0.44,1.34,-0.89,0.28,1.27,-0.83,0.2,1.34,-0.72,0.44,1.34,-0.84,0.56,1.27,-0.97,0.56,1.07,-0.89,0.28,1.27,-1.11,0.2,-0.59,-1.11,0.16,-0.59,-1.12,0.2,-0.56,-1.1,-0.04,-0.7,-1.08,0.16,-0.69,-0.98,0,-0.96,-1.15,0.16,-0.4,-1.21,-0.2,-0.13,-1.19,0.12,0.38,-1.12,0.2,-0.56,-1.15,0.16,-0.4,-1.12,0.24,-0.52,-1.11,0.16,-0.59,-1.08,0.16,-0.69,-1.1,-0.04,-0.7,-0.98,0,-0.96,0.16,0.28,-1.44,0.13,0,-1.47,0.24,0,1.49,-0.24,0,1.51,0.22,0.24,1.63,0.22,-0.32,1.52,0.24,0,1.49,-1.02,-0.36,1,-0.99,0.52,0.83,-1.15,0,0.54,-0.91,0.16,1.06,-0.99,0.52,0.83,-1.12,0.76,0.44,-1.18,0.6,0.34,-1.1,0.32,-0.58,-1.12,0.24,-0.52,-1.14,0.52,-0.42,-1.12,0.2,-0.56,-1.14,0.04,-0.5,-1.15,0.16,-0.4,-1.12,0.2,-0.56,-1.11,0.16,-0.59,-1.14,0.04,-0.5,0.17,-0.04,-1.51,0.13,0,-1.47,0.22,0.04,-1.51,0.22,0.24,1.63,-0.72,0.44,1.34,0.24,0,1.49,-0.98,0,-0.96,-0.81,-0.16,-1.2,-1.07,-0.44,-0.87,0.16,0.28,-1.44,0.24,0.68,-1.27,0.3,0.44,-1.52,-1.14,0.04,-0.5,-1.11,0.16,-0.59,-1.1,-0.04,-0.7,-0.81,-0.16,-1.2,0.13,0,-1.47,0.17,-0.04,-1.51,-1.14,0.04,-0.5,-1.1,-0.04,-0.7,-1.2,-0.56,-0.43,-1.1,-0.04,-0.7,-0.98,0,-0.96,-1.07,-0.44,-0.87,-0.81,-0.16,-1.2,-0.98,0,-0.96,0.13,0,-1.47,0.22,0.04,-1.51,0.13,0,-1.47,0.16,0.28,-1.44,0.41,-0.12,-1.66,0.22,0.04,-1.51,0.33,0.28,-1.54,-1.15,0.16,-0.4,-1.14,0.04,-0.5,-1.21,-0.2,-0.13,-1.02,-0.36,1,-0.91,0.16,1.06,-1.15,0,0.54,0.22,-0.52,-1.37,-0.81,-0.16,-1.2,0.17,-0.04,-1.51,0.24,0,1.49,-0.83,0.2,1.34,-1.02,-0.36,1,-1.21,-0.2,-0.13,-1.14,0.04,-0.5,-1.2,-0.56,-0.43,-1.22,-0.4,0.04,-1.2,-0.56,-0.43,-1.24,-0.64,-0.12,0.41,-0.12,-1.66,0.22,-0.52,-1.37,0.17,-0.04,-1.51,-1.02,-0.36,1,0.27,-0.64,1.49,0.24,-0.48,1.49,-1.15,-0.72,-0.63,-1.07,-0.44,-0.87,-1.09,-0.76,-0.73,0.22,-0.52,-1.37,-1,-0.72,-1.16,-1.07,-0.44,-0.87,-1.15,0.16,-0.4,-1.19,0.12,0.38,-1.18,0.6,0.34,-0.83,0.2,1.34,-0.91,0.16,1.06,-1.02,-0.36,1,-1.15,-0.72,0.43,-1.16,-0.6,0.65,-1.15,0,0.54,-1.2,-0.56,-0.43,-1.15,-0.72,-0.63,-1.16,-0.72,-0.48,-1,-0.72,-1.16,-1.09,-0.68,-0.97,-1.07,-0.44,-0.87,-1.09,-0.68,-0.97,-1,-0.72,-1.16,-1.02,-0.8,-0.99,-1.21,-0.2,-0.13,-1.22,-0.4,0.04,-1.19,0.12,0.38,-1.15,-0.72,0.43,-1.12,-0.72,0.63,-1.16,-0.6,0.65,-1.2,-0.56,-0.43,-1.19,-0.72,-0.23,-1.24,-0.64,-0.12,-1.07,-0.44,-0.87,-1.08,-0.76,-0.84,-1.09,-0.76,-0.73,-1.16,-0.6,0.65,-1.12,-0.72,0.63,-1.12,-0.72,0.7,-1.01,-0.76,1.1,-0.98,-0.76,1.23,-1,-0.68,1.24,-1.09,-0.64,0.97,-1.12,-0.68,0.85,-1.04,-0.76,0.8,-1.16,-0.6,0.65,-1.11,-0.72,0.76,-1.12,-0.68,0.85,-1.22,-0.4,0.04,-1.15,0,0.54,-1.19,0.12,0.38,-1.19,-0.72,0.13,-1.22,-0.64,0.22,-1.22,-0.4,0.04,-1.22,-0.64,0.22,-1.15,-0.72,0.43,-1.15,0,0.54,-1.15,-0.72,-0.63,-1.2,-0.56,-0.43,-1.07,-0.44,-0.87,-1.02,-0.36,1,-1,-0.68,1.24,0.27,-0.64,1.49,-1.16,-0.6,0.65,-1.12,-0.72,0.7,-1.11,-0.72,0.76,-1.12,-0.68,0.85,-1.11,-0.72,0.76,-1.04,-0.76,0.8,-1.22,-0.4,0.04,-1.22,-0.64,0.22,-1.15,0,0.54,-1.1,-0.04,-0.7,-1.07,-0.44,-0.87,-1.2,-0.56,-0.43,-1.07,-0.44,-0.87,-1.09,-0.68,-0.97,-1.08,-0.76,-0.84,-1,-0.68,1.24,-1.02,-0.36,1,-1.09,-0.64,0.97,-1,-0.68,1.24,-0.98,-0.76,1.23,-0.9,-0.8,1.32,-1.01,-0.76,1.1,-1,-0.68,1.24,-1.09,-0.64,0.97,-1.16,-0.6,0.65,-1.12,-0.68,0.85,-1.02,-0.36,1,-1.12,-0.68,0.85,-1.09,-0.64,0.97,-1.02,-0.36,1,-1.19,-0.72,0.13,-1.22,-0.4,0.04,-1.24,-0.64,-0.12,-1.19,-0.72,0.13,-1.24,-0.64,-0.12,-1.19,-0.72,-0.23,-1.15,-0.72,0.43,-1.22,-0.64,0.22,-1.19,-0.72,0.13,-1.22,-0.4,0.04,-1.21,-0.2,-0.13,-1.2,-0.56,-0.43,-1.19,-0.72,-0.23,-1.2,-0.56,-0.43,-1.16,-0.72,-0.48,-1.01,-0.8,-0.91,-1.08,-0.76,-0.84,-1.09,-0.68,-0.97,-1.01,-0.76,1.1,-1.09,-0.64,0.97,-1.04,-0.76,0.8,-1.16,-0.6,0.65,-1.02,-0.36,1,-1.15,0,0.54,-1.03,-0.76,0.76,-1.04,-0.76,0.8,-1.11,-0.72,0.76,-1.02,-0.76,0.67,-1.12,-0.72,0.7,-1.06,-0.76,0.63,-1.12,-0.72,0.7,-1.12,-0.72,0.63,-1.06,-0.76,0.63,-1.04,-0.76,0.59,-1.06,-0.76,0.63,-1.12,-0.72,0.63,-1.1,-0.76,-0.55,-1.15,-0.72,-0.63,-1.09,-0.76,-0.73,-1.1,-0.76,-0.55,-1.16,-0.72,-0.48,-1.15,-0.72,-0.63,0.14,-0.72,-1.41,0.22,-0.52,-1.37,0.22,-0.72,-1.5,-1,-0.68,1.24,-0.9,-0.8,1.32,0.27,-0.64,1.49,-0.98,-0.76,1.23,-0.93,-0.8,1.2,-0.9,-0.8,1.32,-0.99,-0.76,0.5,-0.9,-0.8,0.44,-0.88,-0.8,0.5,-0.91,-0.92,0.48,-0.91,-0.84,0.45,-0.96,-1,0.37,-0.91,-0.84,0.45,-0.9,-0.8,0.44,-0.93,-0.8,0.38,-0.93,-0.8,0.38,-1,-0.76,0.41,-1.04,-0.76,0.13,-0.93,-0.8,0.38,-1.04,-0.76,0.13,-0.96,-1,0.37,-1.04,-0.76,0.13,-0.97,-0.8,0.01,-0.96,-0.92,0.04,-1.04,-0.76,0.13,-0.96,-0.92,0.04,-0.96,-1,0.37,-0.97,-0.8,0.01,-0.97,-0.8,-0.16,-0.98,-0.88,-0.17,-1.07,-0.76,-0.08,-0.97,-0.8,0.01,-1.04,-0.76,0.13,-1.03,-0.76,-0.22,-0.97,-0.8,-0.16,-1.07,-0.76,-0.08,-0.95,-0.8,-0.18,-0.97,-0.8,-0.16,-1.03,-0.76,-0.22,-1.01,-0.8,-0.91,-1.09,-0.68,-0.97,-1.02,-0.8,-0.99,-1.02,-0.8,-0.99,-0.96,-0.84,-1.13,-0.89,-0.88,-1.13,0.22,-0.52,-1.37,0.14,-0.72,-1.41,-1,-0.72,-1.16,0.14,-0.72,-1.41,-0.85,-0.92,-1.28,-0.92,-0.84,-1.26,-0.81,-0.16,-1.2,0.22,-0.52,-1.37,-1.07,-0.44,-0.87,-0.85,-0.84,1.33,-0.84,-0.84,1.38,-0.9,-0.8,1.32,-0.85,-0.84,0.98,-0.8,-0.84,1,-0.85,-0.8,1.06,-0.88,-0.8,1.01,-0.85,-0.84,0.98,-0.85,-0.8,1.06,-0.88,-0.8,1.01,-0.83,-0.8,0.94,-0.85,-0.84,0.98,-0.91,-0.8,0.92,-0.85,-0.84,0.91,-0.83,-0.8,0.94,-0.85,-0.84,0.91,-0.91,-0.8,0.92,-0.85,-0.8,0.77,-0.9,-0.8,0.44,-0.91,-0.84,0.45,-0.9,-0.84,0.47,-0.9,-0.8,0.44,-0.9,-0.84,0.47,-0.88,-0.8,0.5,-1,-0.76,0.41,-0.9,-0.8,0.44,-0.99,-0.76,0.5,-0.97,-0.8,0.01,-1.07,-0.76,-0.08,-0.97,-0.8,-0.16,-0.95,-0.8,-0.18,-0.98,-0.88,-0.17,-0.97,-0.8,-0.16,-0.86,-0.8,-0.7,-0.81,-0.84,-0.72,-0.83,-0.8,-0.64,-0.92,-0.84,-1.26,-0.9,-0.88,-1.17,-0.96,-0.84,-1.13,-0.92,-0.84,-1.26,-0.96,-0.84,-1.13,-1,-0.72,-1.16,-0.84,-0.84,1.38,-0.76,-0.88,1.37,0.26,-0.8,1.5,-0.72,-0.88,1.15,-0.7,-0.88,1.21,-0.79,-0.84,1.26,-0.73,-0.84,1.09,-0.72,-0.88,1.15,-0.79,-0.84,1.26,-0.76,-0.84,1,-0.75,-0.88,1.03,-0.73,-0.84,1.09,-0.76,-0.84,1,-0.8,-0.84,1,-0.75,-0.88,1.03,-0.88,-0.92,0.97,-0.76,-1,1.03,-0.75,-0.88,1.03,-0.85,-0.84,0.91,-0.85,-0.84,0.98,-0.83,-0.8,0.94,-0.88,-0.92,0.97,-0.85,-0.84,0.91,-0.86,-1,0.63,-0.85,-0.8,0.77,-0.86,-0.88,0.59,-0.86,-1,0.63,-1,-0.76,0.41,-0.93,-0.8,0.38,-0.9,-0.8,0.44,-0.91,-0.84,0.45,-0.93,-0.8,0.38,-0.96,-1,0.37,-0.96,-0.92,0.04,-0.97,-0.8,0.01,-0.98,-0.88,-0.17,-0.83,-0.8,-0.53,-0.88,-0.96,-0.36,-0.95,-0.8,-0.18,-0.82,-0.92,-0.7,-0.85,-0.96,-0.58,-0.83,-0.8,-0.64,-0.81,-0.84,-0.81,-0.77,-0.88,-0.79,-0.81,-0.84,-0.72,-1.02,-0.8,-0.99,-1,-0.72,-1.16,-0.96,-0.84,-1.13,-0.9,-0.88,-1.17,-0.89,-0.88,-1.13,-0.96,-0.84,-1.13,0.14,-0.72,-1.41,-0.92,-0.84,-1.26,-1,-0.72,-1.16,-0.92,-0.84,-1.26,-0.85,-0.92,-1.28,-0.83,-0.92,-1.22,0.19,-0.96,-1.33,-0.85,-0.92,-1.28,0.14,-0.72,-1.41,-0.84,-0.84,1.38,0.26,-0.8,1.5,0.27,-0.64,1.49,-0.76,-0.88,1.37,-0.71,-0.88,1.29,-0.66,-0.92,1.37,-0.66,-0.92,1.37,-0.69,-0.92,1.25,-0.66,-1.04,1.37,-0.7,-0.88,1.21,-0.69,-0.92,1.25,-0.71,-0.88,1.29,-0.71,-0.92,1.19,-0.7,-0.88,1.21,-0.72,-0.88,1.15,-0.71,-0.92,1.19,-0.72,-0.88,1.15,-0.73,-0.92,1.12,-0.76,-1,1.03,-0.73,-0.92,1.12,-0.75,-0.88,1.03,-0.73,-0.84,1.09,-0.73,-0.92,1.12,-0.72,-0.88,1.15,-0.8,-0.84,1,-0.85,-0.84,0.98,-0.88,-0.92,0.97,-0.85,-0.84,0.91,-0.85,-0.8,0.77,-0.86,-1,0.63,-0.88,-0.8,0.5,-0.9,-0.84,0.47,-0.86,-0.88,0.59,-0.88,-0.8,0.5,-0.86,-0.88,0.59,-0.85,-0.8,0.77,-0.9,-0.84,0.47,-0.91,-0.84,0.45,-0.91,-0.92,0.48,-0.98,-0.88,-0.17,-0.95,-0.8,-0.18,-0.88,-0.96,-0.36,-0.81,-0.84,-0.72,-0.82,-0.92,-0.7,-0.83,-0.8,-0.64,-0.75,-1.16,-0.84,-0.82,-0.92,-0.7,-0.77,-0.88,-0.79,-0.9,-0.88,-1.17,-0.92,-0.84,-1.26,-0.83,-0.92,-1.22,0.19,-0.96,-1.33,0.14,-0.72,-1.41,0.22,-0.72,-1.5,-0.76,-0.88,1.37,-0.66,-0.92,1.37,0.23,-0.84,1.56,-0.66,-1.04,1.37,-0.69,-0.92,1.25,-0.73,-1.04,1.16,-0.7,-0.88,1.21,-0.71,-0.92,1.19,-0.69,-0.92,1.25,-0.8,-0.84,1,-0.88,-0.92,0.97,-0.75,-0.88,1.03,-0.86,-0.88,0.59,-0.91,-0.92,0.48,-0.86,-1,0.63,-0.73,-1.08,-1.02,-0.76,-0.92,-1.1,-0.76,-1,-1.16,0.36,-1.04,-1.34,0.19,-0.96,-1.33,0.3,-1,-1.59,-0.66,-0.92,1.37,-0.71,-0.88,1.29,-0.69,-0.92,1.25,-0.76,-1,1.03,-0.73,-1.04,1.16,-0.73,-0.92,1.12,-0.85,-0.84,0.98,-0.85,-0.84,0.91,-0.88,-0.92,0.97,-0.83,-0.8,-0.53,-0.85,-0.96,-0.58,-0.88,-0.96,-0.36,-0.85,-0.96,-0.58,-0.83,-0.8,-0.53,-0.83,-0.8,-0.64,-0.85,-1.08,-0.65,-0.86,-1.04,-0.62,-0.82,-0.92,-0.7,-0.77,-0.88,-0.79,-0.82,-0.92,-0.7,-0.81,-0.84,-0.72,-0.75,-1.16,-0.84,-0.77,-0.88,-0.79,-0.71,-0.88,-0.94,-0.76,-0.92,-1.1,-0.73,-1.08,-1.02,-0.71,-0.88,-0.94,-0.76,-1,-1.16,-0.66,-1.08,-1.19,-0.78,-1.08,-1.18,-0.74,-0.96,-1.26,0.36,-1.04,-1.34,-0.66,-1.08,-1.19,-0.76,-0.92,-1.1,-0.83,-0.92,-1.22,-0.76,-1,-1.16,-0.73,-0.92,1.12,-0.73,-1.04,1.16,-0.71,-0.92,1.19,-0.73,-0.84,1.09,-0.75,-0.88,1.03,-0.73,-0.92,1.12,-0.88,-0.92,0.97,-0.82,-1.12,1.04,-0.76,-1,1.03,-0.86,-0.88,0.59,-0.9,-0.84,0.47,-0.91,-0.92,0.48,-0.96,-1,0.37,-0.86,-1,0.63,-0.91,-0.92,0.48,-0.82,-0.92,-0.7,-0.86,-1.04,-0.62,-0.85,-0.96,-0.58,-0.76,-1,-1.16,-0.74,-0.96,-1.26,-0.66,-1.08,-1.19,-0.94,-1.08,1.01,-0.88,-0.92,0.97,-0.86,-1,0.63,-0.86,-1.04,-0.58,-0.88,-0.96,-0.36,-0.85,-0.96,-0.58,-0.86,-1.04,-0.62,-0.86,-1.04,-0.58,-0.85,-0.96,-0.58,-0.74,-0.96,-1.26,0.19,-0.96,-1.33,0.36,-1.04,-1.34,-0.83,-0.92,-1.22,-0.74,-0.96,-1.26,-0.76,-1,-1.16,-0.69,-0.92,1.25,-0.71,-0.92,1.19,-0.73,-1.04,1.16,-0.88,-0.92,0.97,-0.94,-1.08,1.01,-0.82,-1.12,1.04,-0.75,-1.16,-0.84,-0.71,-0.88,-0.94,-0.73,-1.08,-1.02,0.81,4.32,1.2,0.76,4.32,1.24,0.73,4.36,1.27,0.76,4.32,1.24,0.81,4.32,1.2,0.73,4.36,1.27,0.95,4.32,1.01,0.82,4.32,1.17,0.78,4.36,1.14,0.82,4.32,1.17,0.95,4.32,1.01,0.78,4.36,1.14,0.84,4.4,0.99,0.74,4.44,1.05,0.72,4.4,1.1,0.62,4.4,1.06,0.55,4.32,1.18,0.54,4.4,1,0.59,4.32,1.23,0.57,4.32,1.2,0.65,4.36,1.15,0.57,4.32,1.2,0.59,4.32,1.23,0.65,4.36,1.15,0.65,4.36,1.15,0.67,4.36,1.17,0.59,4.32,1.23,0.67,4.36,1.17,0.65,4.36,1.15,0.59,4.32,1.23,0.65,4.32,1.29,0.67,4.36,1.17,0.73,4.36,1.27,0.67,4.36,1.17,0.65,4.32,1.29,0.73,4.36,1.27,0.59,4.32,1.23,0.67,4.36,1.17,0.65,4.32,1.29,0.67,4.36,1.17,0.59,4.32,1.23,0.65,4.32,1.29,0.72,4.4,1.1,0.78,4.36,1.14,0.74,4.36,1.18,0.78,4.36,1.14,0.72,4.4,1.1,0.74,4.36,1.18,0.95,4.32,1.01,0.84,4.4,0.99,0.78,4.36,1.14,0.54,4.4,1,0.36,4.24,1.06,0.55,4.32,1.18,0.62,4.4,1.06,0.72,4.4,1.1,0.74,4.44,1.05,0.64,4.36,1.12,0.62,4.4,1.06,0.72,4.4,1.1,0.62,4.4,1.06,0.64,4.36,1.12,0.72,4.4,1.1,0.64,4.36,1.12,0.55,4.32,1.18,0.62,4.4,1.06,0.55,4.32,1.18,0.64,4.36,1.12,0.62,4.4,1.06,0.67,4.36,1.17,0.65,4.36,1.15,0.72,4.4,1.1,0.65,4.36,1.15,0.67,4.36,1.17,0.72,4.4,1.1,0.65,4.36,1.15,0.64,4.36,1.12,0.72,4.4,1.1,0.64,4.36,1.12,0.65,4.36,1.15,0.72,4.4,1.1,0.72,4.4,1.1,0.84,4.4,0.99,0.78,4.36,1.14,0.84,4.4,0.99,0.72,4.4,1.1,0.78,4.36,1.14])

IndexedFaceSet406.setCoord(Coordinate407)

Shape402.setGeometry(IndexedFaceSet406)

Transform401.addChildren(Shape402)

fieldValue400.addChildren(Transform401)

ProtoInstance398.addFieldValue(fieldValue400)

fieldValue397.addChildren(ProtoInstance398)
ProtoInstance408 = ProtoInstance()
ProtoInstance408.setName("Joint")
ProtoInstance408.setDEF("Allen_hanim_l_shoulder")
fieldValue409 = fieldValue()
fieldValue409.setName("name")
fieldValue409.setValue("l_shoulder")

ProtoInstance408.addFieldValue(fieldValue409)
fieldValue410 = fieldValue()
fieldValue410.setName("center")
fieldValue410.setValue("0.167 1.36 -0.0518")

ProtoInstance408.addFieldValue(fieldValue410)
fieldValue411 = fieldValue()
fieldValue411.setName("children")
ProtoInstance412 = ProtoInstance()
ProtoInstance412.setName("Segment")
ProtoInstance412.setDEF("Allen_hanim_l_upperarm")
fieldValue413 = fieldValue()
fieldValue413.setName("name")
fieldValue413.setValue("l_upperarm")

ProtoInstance412.addFieldValue(fieldValue413)
fieldValue414 = fieldValue()
fieldValue414.setName("children")
Transform415 = Transform()
Transform415.setDEF("Allen_l_upperarm_adjust")
Transform415.setCenter([-0.435,1,0.06])
Transform415.setRotation([0,1,0,1.570796])
Transform415.setScale([0.1,0.1,0.1])
Shape416 = Shape()
Appearance417 = Appearance()
Material418 = Material()
Material418.setDEF("Skin_Color")
Material418.setAmbientIntensity(0.25)
Material418.setDiffuseColor([0.749,0.601,0.462])

Appearance417.setMaterial(Material418)
ImageTexture419 = ImageTexture()
ImageTexture419.setUSE("camo")

Appearance417.setTexture(ImageTexture419)

Shape416.setAppearance(Appearance417)
IndexedFaceSet420 = IndexedFaceSet()
IndexedFaceSet420.setCoordIndex([0,1,2,-1,3,4,5,-1,6,7,8,-1,9,10,11,-1,12,13,14,-1,15,16,17,-1,18,19,20,-1,21,22,23,-1,24,25,26,-1,27,28,29,-1,30,31,32,-1,33,34,35,-1,36,37,38,-1,39,40,41,-1,42,43,44,-1,45,46,47,-1,48,49,50,-1,51,52,53,-1,54,55,56,-1,57,58,59,-1,60,61,62,-1,63,64,65,-1,66,67,68,-1,69,70,71,-1,72,73,74,-1,75,76,77,-1,78,79,80,-1,81,82,83,-1,84,85,86,-1,87,88,89,-1,90,91,92,-1,93,94,95,-1,96,97,98,-1,99,100,101,-1,102,103,104,-1,105,106,107,-1,108,109,110,-1,111,112,113,-1,114,115,116,-1,117,118,119,-1,120,121,122,-1,123,124,125,-1,126,127,128,-1,129,130,131,-1,132,133,134,-1,135,136,137,-1,138,139,140,-1,141,142,143,-1,144,145,146,-1,147,148,149,-1,150,151,152,-1,153,154,155,-1,156,157,158,-1,159,160,161,-1,162,163,164,-1,165,166,167,-1,168,169,170,-1,171,172,173,-1,174,175,176,-1,177,178,179,-1,180,181,182,-1,183,184,185,-1,186,187,188,-1,189,190,191,-1,192,193,194,-1,195,196,197,-1,198,199,200,-1,201,202,203,-1,204,205,206,-1,207,208,209,-1,210,211,212,-1,213,214,215,-1,216,217,218,-1,219,220,221,-1,222,223,224,-1,225,226,227,-1,228,229,230,-1,231,232,233,-1,234,235,236,-1,237,238,239,-1,240,241,242,-1,243,244,245,-1,246,247,248,-1,249,250,251,-1,252,253,254,-1,255,256,257,-1,258,259,260,-1,261,262,263,-1,264,265,266,-1,267,268,269,-1,270,271,272,-1,273,274,275,-1,276,277,278,-1,279,280,281,-1,282,283,284,-1,285,286,287,-1,288,289,290,-1,291,292,293,-1,294,295,296,-1,297,298,299,-1,300,301,302,-1,303,304,305,-1,306,307,308,-1,309,310,311,-1,312,313,314,-1,315,316,317,-1,318,319,320,-1,321,322,323,-1,324,325,326,-1,327,328,329,-1,330,331,332,-1,333,334,335,-1,336,337,338,-1,339,340,341,-1,342,343,344,-1,345,346,347,-1,348,349,350,-1,351,352,353,-1,354,355,356,-1,357,358,359,-1,360,361,362,-1,363,364,365,-1,366,367,368,-1,369,370,371,-1,372,373,374,-1,375,376,377,-1,378,379,380,-1,381,382,383,-1,384,385,386,-1,387,388,389,-1,390,391,392,-1,393,394,395,-1,396,397,398,-1,399,400,401,-1,402,403,404,-1,405,406,407,-1,408,409,410,-1,411,412,413,-1,414,415,416,-1,417,418,419,-1,420,421,422,-1,423,424,425,-1,426,427,428,-1,429,430,431,-1,432,433,434,-1,435,436,437,-1,438,439,440,-1,441,442,443,-1,444,445,446,-1,447,448,449,-1,450,451,452,-1,453,454,455,-1,456,457,458,-1,459,460,461,-1,462,463,464,-1,465,466,467,-1,468,469,470,-1,471,472,473,-1,474,475,476,-1,477,478,479,-1,480,481,482,-1,483,484,485,-1,486,487,488,-1,489,490,491,-1,492,493,494,-1,495,496,497,-1,498,499,500,-1,501,502,503,-1,504,505,506,-1,507,508,509,-1,510,511,512,-1,513,514,515,-1,516,517,518,-1,519,520,521,-1,522,523,524,-1,525,526,527,-1,528,529,530,-1,531,532,533,-1,534,535,536,-1,537,538,539,-1,540,541,542,-1,543,544,545,-1,546,547,548,-1,549,550,551,-1,552,553,554,-1,555,556,557,-1,558,559,560,-1,561,562,563,-1,564,565,566,-1,567,568,569,-1,570,571,572,-1,573,574,575,-1,576,577,578,-1,579,580,581,-1,582,583,584,-1,585,586,587,-1,588,589,590,-1,591,592,593,-1,594,595,596,-1,597,598,599,-1,600,601,602,-1,603,604,605,-1,606,607,608,-1,609,610,611,-1,612,613,614,-1,615,616,617,-1,618,619,620,-1,621,622,623,-1,624,625,626,-1,627,628,629,-1,630,631,632,-1,633,634,635,-1,636,637,638,-1,639,640,641,-1,642,643,644,-1,645,646,647,-1,648,649,650,-1,651,652,653,-1,654,655,656,-1,657,658,659,-1,660,661,662,-1,663,664,665,-1,666,667,668,-1,669,670,671,-1,672,673,674,-1,675,676,677,-1,678,679,680,-1,681,682,683,-1,684,685,686,-1,687,688,689,-1,690,691,692,-1,693,694,695,-1,696,697,698,-1,699,700,701,-1,702,703,704,-1,705,706,707,-1,708,709,710,-1,711,712,713,-1,714,715,716,-1,717,718,719,-1,720,721,722,-1,723,724,725,-1,726,727,728,-1,729,730,731,-1,732,733,734,-1,735,736,737,-1,738,739,740,-1,741,742,743,-1,744,745,746,-1,747,748,749,-1,750,751,752,-1,753,754,755,-1,756,757,758,-1,759,760,761,-1,762,763,764,-1,765,766,767,-1,768,769,770,-1,771,772,773,-1,774,775,776,-1,777,778,779,-1,780,781,782,-1,783,784,785,-1,786,787,788,-1,789,790,791,-1,792,793,794,-1,795,796,797,-1,798,799,800,-1,801,802,803,-1,804,805,806,-1,807,808,809,-1,810,811,812,-1,813,814,815,-1,816,817,818,-1,819,820,821,-1,822,823,824,-1,825,826,827,-1,828,829,830,-1,831,832,833,-1,834,835,836,-1,837,838,839,-1,840,841,842,-1,843,844,845,-1,846,847,848,-1,849,850,851,-1,852,853,854,-1,855,856,857,-1,858,859,860,-1,861,862,863,-1,864,865,866,-1,867,868,869,-1,870,871,872,-1,873,874,875,-1,876,877,878,-1,879,880,881,-1,882,883,884,-1,885,886,887,-1,888,889,890,-1,891,892,893,-1,894,895,896,-1,897,898,899,-1,900,901,902,-1,903,904,905,-1,906,907,908,-1,909,910,911,-1,912,913,914,-1,915,916,917,-1,918,919,920,-1,921,922,923,-1,924,925,926,-1,927,928,929,-1,930,931,932,-1,933,934,935,-1,936,937,938,-1,939,940,941,-1,942,943,944,-1,945,946,947,-1,948,949,950,-1,951,952,953,-1,954,955,956,-1,957,958,959,-1,960,961,962,-1,963,964,965,-1,966,967,968,-1,969,970,971,-1,972,973,974,-1,975,976,977,-1,978,979,980,-1,981,982,983,-1,984,985,986,-1,987,988,989,-1,990,991,992,-1,993,994,995,-1,996,997,998,-1,999,1000,1001,-1,1002,1003,1004,-1,1005,1006,1007,-1,1008,1009,1010,-1,1011,1012,1013,-1,1014,1015,1016,-1,1017,1018,1019,-1,1020,1021,1022,-1,1023,1024,1025,-1,1026,1027,1028,-1,1029,1030,1031,-1,1032,1033,1034,-1,1035,1036,1037,-1,1038,1039,1040,-1,1041,1042,1043,-1,1044,1045,1046,-1,1047,1048,1049,-1,1050,1051,1052,-1,1053,1054,1055,-1,1056,1057,1058,-1,1059,1060,1061,-1,1062,1063,1064,-1,1065,1066,1067,-1,1068,1069,1070,-1,1071,1072,1073,-1,1074,1075,1076,-1,1077,1078,1079,-1,1080,1081,1082,-1,1083,1084,1085,-1,1086,1087,1088,-1,1089,1090,1091,-1,1092,1093,1094,-1,1095,1096,1097,-1,1098,1099,1100,-1,1101,1102,1103,-1,1104,1105,1106,-1,1107,1108,1109,-1,1110,1111,1112,-1,1113,1114,1115,-1,1116,1117,1118,-1,1119,1120,1121,-1,1122,1123,1124,-1,1125,1126,1127,-1,1128,1129,1130,-1,1131,1132,1133,-1,1134,1135,1136,-1,1137,1138,1139,-1,1140,1141,1142,-1,1143,1144,1145,-1,1146,1147,1148,-1,1149,1150,1151,-1,1152,1153,1154,-1,1155,1156,1157,-1,1158,1159,1160,-1,1161,1162,1163,-1,1164,1165,1166,-1,1167,1168,1169,-1,1170,1171,1172,-1,1173,1174,1175,-1,1176,1177,1178,-1,1179,1180,1181,-1,1182,1183,1184,-1,1185,1186,1187,-1,1188,1189,1190,-1,1191,1192,1193,-1,1194,1195,1196,-1,1197,1198,1199,-1,1200,1201,1202,-1,1203,1204,1205,-1,1206,1207,1208,-1,1209,1210,1211,-1,1212,1213,1214,-1,1215,1216,1217,-1,1218,1219,1220,-1,1221,1222,1223,-1,1224,1225,1226,-1,1227,1228,1229,-1,1230,1231,1232,-1,1233,1234,1235,-1,1236,1237,1238,-1,1239,1240,1241,-1,1242,1243,1244,-1,1245,1246,1247,-1,1248,1249,1250,-1,1251,1252,1253,-1,1254,1255,1256,-1,1257,1258,1259,-1,1260,1261,1262,-1,1263,1264,1265,-1,1266,1267,1268,-1,1269,1270,1271,-1,1272,1273,1274,-1,1275,1276,1277,-1,1278,1279,1280,-1,1281,1282,1283,-1,1284,1285,1286,-1,1287,1288,1289,-1,1290,1291,1292,-1,1293,1294,1295,-1,1296,1297,1298,-1,1299,1300,1301,-1,1302,1303,1304,-1,1305,1306,1307,-1,1308,1309,1310,-1,1311,1312,1313,-1,1314,1315,1316,-1,1317,1318,1319,-1,1320,1321,1322,-1,1323,1324,1325,-1,1326,1327,1328,-1,1329,1330,1331,-1,1332,1333,1334,-1,1335,1336,1337,-1,1338,1339,1340,-1,1341,1342,1343,-1,1344,1345,1346,-1,1347,1348,1349,-1,1350,1351,1352,-1,1353,1354,1355,-1,1356,1357,1358,-1,1359,1360,1361,-1,1362,1363,1364,-1,1365,1366,1367,-1,1368,1369,1370,-1,1371,1372,1373,-1,1374,1375,1376,-1,1377,1378,1379,-1,1380,1381,1382,-1,1383,1384,1385,-1,1386,1387,1388,-1,1389,1390,1391,-1,1392,1393,1394,-1,1395,1396,1397,-1,1398,1399,1400,-1,1401,1402,1403,-1,1404,1405,1406,-1,1407,1408,1409,-1,1410,1411,1412,-1,1413,1414,1415,-1,1416,1417,1418,-1,1419,1420,1421,-1,1422,1423,1424,-1,1425,1426,1427,-1,1428,1429,1430,-1,1431,1432,1433,-1,1434,1435,1436,-1,1437,1438,1439,-1,1440,1441,1442,-1,1443,1444,1445,-1,1446,1447,1448,-1,1449,1450,1451,-1,1452,1453,1454,-1,1455,1456,1457,-1,1458,1459,1460,-1,1461,1462,1463,-1,1464,1465,1466,-1,1467,1468,1469,-1,1470,1471,1472,-1,1473,1474,1475,-1,1476,1477,1478,-1,1479,1480,1481,-1,1482,1483,1484,-1,1485,1486,1487,-1,1488,1489,1490,-1,1491,1492,1493,-1,1494,1495,1496,-1,1497,1498,1499,-1,1500,1501,1502,-1,1503,1504,1505,-1,1506,1507,1508,-1,1509,1510,1511,-1,1512,1513,1514,-1,1515,1516,1517,-1,1518,1519,1520,-1,1521,1522,1523,-1,1524,1525,1526,-1,1527,1528,1529,-1,1530,1529,1528,-1,1528,1531,1530,-1,1532,1530,1531,-1,1535,1533,1534,-1])
IndexedFaceSet420.setCreaseAngle(1.65)
Coordinate421 = Coordinate()
Coordinate421.setPoint([0.69,4.24,5.73,0.67,4.24,5.71,0.66,4.2,5.79,0.66,4.2,5.79,0.67,4.24,5.71,0.57,4.2,5.78,0.25,4.08,5.64,0.09,3.88,5.93,0.17,3.96,5.98,0.76,4.12,5.92,0.79,4.12,5.91,0.78,4.16,5.89,0.78,4.16,5.89,0.71,4.16,5.9,0.76,4.12,5.92,0.72,4.12,5.93,0.76,4.12,5.92,0.71,4.16,5.9,0.78,4.16,5.89,0.79,4.12,5.91,0.82,4.16,5.81,0.79,4.12,5.91,0.76,4.12,5.92,0.8,4.08,5.99,1.03,3.84,6.14,0.66,4.04,6.15,0.67,3.88,6.33,0.45,4.12,5.97,0.66,4.04,6.15,0.67,4.12,6.04,0.25,4.08,5.64,0.17,3.96,5.98,0.42,4.16,5.81,0.8,4.08,5.99,0.98,4,5.95,0.79,4.12,5.91,1.03,3.84,6.14,0.8,4.08,5.99,0.66,4.04,6.15,0.45,4.12,5.97,0.48,4.16,5.88,0.42,4.16,5.81,1.21,3.88,5.87,1.03,3.84,6.14,1.24,3.68,6.12,0.98,4,5.95,0.8,4.08,5.99,1.03,3.84,6.14,0.36,4,6.15,0.67,3.88,6.33,0.66,4.04,6.15,0.53,3.72,6.43,0.22,3.8,6.24,0.38,3.48,6.5,0.17,3.96,5.98,0.45,4.12,5.97,0.42,4.16,5.81,0.8,4.08,5.99,0.67,4.12,6.04,0.66,4.04,6.15,0.82,3.68,6.37,1.03,3.84,6.14,0.67,3.88,6.33,0.36,4,6.15,0.53,3.72,6.43,0.67,3.88,6.33,1.42,3.48,6.07,1.46,3.48,5.99,1.33,3.56,5.88,0.45,4.12,5.97,0.36,4,6.15,0.66,4.04,6.15,0.17,3.96,5.98,0.36,4,6.15,0.45,4.12,5.97,0.36,4,6.15,0.22,3.8,6.24,0.53,3.72,6.43,0.17,3.96,5.98,0.22,3.8,6.24,0.36,4,6.15,0.17,3.96,5.98,0.09,3.88,5.93,0.22,3.8,6.24,1.03,3.84,6.14,0.82,3.68,6.37,1.04,3.44,6.39,1.43,3.68,5.82,1.33,3.56,5.88,1.45,3.6,5.83,1.21,3.88,5.87,0.98,4,5.95,1.03,3.84,6.14,1.24,3.68,6.12,1.03,3.84,6.14,1.04,3.44,6.39,0.53,3.72,6.43,0.6,3.64,6.49,0.69,3.68,6.42,0.67,3.88,6.33,0.53,3.72,6.43,0.69,3.68,6.42,0.09,3.88,5.93,0.06,3.56,6.21,0.22,3.8,6.24,0.09,3.88,5.93,-0.01,3.76,5.89,0.06,3.56,6.21,1.24,3.68,6.12,1.33,3.56,5.88,1.21,3.88,5.87,0.67,3.88,6.33,0.69,3.68,6.42,0.82,3.68,6.37,0.82,3.68,6.37,0.69,3.68,6.42,0.7,3.6,6.46,1.24,3.68,6.12,1.04,3.44,6.39,1.36,3.52,6.11,1.33,3.56,5.88,1.38,3.48,5.86,1.45,3.6,5.83,1.24,3.68,6.12,1.36,3.52,6.11,1.33,3.56,5.88,0.83,3.52,6.45,0.82,3.68,6.37,0.7,3.6,6.46,0.7,3.6,6.46,0.68,3.52,6.51,0.75,3.48,6.5,0.49,3.52,6.53,0.6,3.64,6.49,0.53,3.72,6.43,0.22,3.8,6.24,0.22,3.4,6.39,0.38,3.48,6.5,0.22,3.4,6.39,0.22,3.8,6.24,0.06,3.56,6.21,0.06,3.56,6.21,0,3.44,6.03,0.06,3.4,6.32,0.68,3.52,6.51,0.7,3.6,6.46,0.6,3.64,6.49,0.49,3.52,6.53,0.64,3.52,6.57,0.6,3.64,6.49,0.06,3.56,6.21,-0.01,3.76,5.89,0,3.44,6.03,0.66,3.48,6.57,0.69,3.48,6.61,0.64,3.52,6.57,0.6,3.44,6.6,0.66,3.48,6.57,0.64,3.52,6.57,0.54,3.4,6.61,0.49,3.52,6.53,0.38,3.48,6.5,0.38,3.48,6.5,0.49,3.52,6.53,0.53,3.72,6.43,0.21,3.32,6.4,0.22,3.4,6.39,0.06,3.4,6.32,1.38,3.48,5.86,1.33,3.56,5.88,1.46,3.48,5.99,1.36,3.52,6.11,1.42,3.48,6.07,1.33,3.56,5.88,0.82,3.68,6.37,0.83,3.52,6.45,1.04,3.44,6.39,0.83,3.52,6.45,0.75,3.48,6.5,0.77,3.44,6.51,0.75,3.48,6.5,0.83,3.52,6.45,0.7,3.6,6.46,0.64,3.52,6.57,0.68,3.52,6.51,0.6,3.64,6.49,0.6,3.44,6.6,0.64,3.52,6.57,0.49,3.52,6.53,0.49,3.52,6.53,0.54,3.4,6.61,0.6,3.44,6.6,0,3.44,6.03,-0.05,3.28,6.21,-0.01,3.32,6.29,1.46,3.48,5.99,1.51,3.36,6.03,1.53,3.36,5.94,1.33,3.56,5.88,1.43,3.68,5.82,1.21,3.88,5.87,1.42,3.48,6.07,1.36,3.52,6.11,1.34,3.28,6.29,1.34,3.28,6.29,1.04,3.44,6.39,0.97,3.24,6.53,0.83,3.52,6.45,0.77,3.44,6.51,0.85,3.36,6.5,0.68,3.52,6.51,0.69,3.48,6.53,0.75,3.48,6.5,0.71,3.44,6.54,0.74,3.44,6.53,0.69,3.48,6.61,0.69,3.48,6.61,0.66,3.48,6.57,0.71,3.44,6.54,0.68,3.44,6.56,0.71,3.44,6.54,0.66,3.48,6.57,0.74,3.44,6.53,0.71,3.44,6.54,0.72,3.4,6.55,0.66,3.4,6.58,0.69,3.4,6.57,0.6,3.44,6.6,0.6,3.44,6.6,0.54,3.4,6.61,0.59,3.36,6.65,0.6,3.44,6.6,0.59,3.36,6.65,0.66,3.4,6.58,0.13,3.16,6.38,-0.01,3.32,6.29,-0.05,3.24,6.25,1.46,3.48,5.99,1.42,3.48,6.07,1.51,3.36,6.03,0.74,3.44,6.53,0.72,3.4,6.55,0.77,3.44,6.51,0.72,3.32,6.59,0.85,3.36,6.5,0.72,3.4,6.55,0.55,3.28,6.67,0.59,3.36,6.65,0.54,3.4,6.61,0.22,3.4,6.39,0.21,3.32,6.4,0.23,3.32,6.42,0.38,3.48,6.5,0.22,3.4,6.39,0.23,3.32,6.42,-0.03,3.16,6.13,-0.05,3.28,6.21,-0.04,3.24,5.99,-0.05,3.28,6.21,-0.03,3.32,5.98,-0.04,3.24,5.99,1.53,3.36,5.94,1.51,3.36,6.03,1.61,3.16,5.92,1.51,3.36,6.03,1.42,3.48,6.07,1.34,3.28,6.29,0.83,3.52,6.45,0.85,3.36,6.5,1.04,3.44,6.39,0.72,3.4,6.55,0.85,3.36,6.5,0.77,3.44,6.51,0.68,3.32,6.61,0.59,3.36,6.65,0.55,3.28,6.67,0.3,3.24,6.52,0.54,3.4,6.61,0.38,3.48,6.5,0.06,3.4,6.32,0.22,3.4,6.39,0.06,3.56,6.21,0.21,3.32,6.4,0.06,3.4,6.32,0.15,3.28,6.37,-0.05,3.28,6.21,0,3.44,6.03,-0.03,3.32,5.98,1.45,3.2,6.22,1.34,3.28,6.29,1.38,3.08,6.33,0.85,3.36,6.5,0.97,3.24,6.53,1.04,3.44,6.39,0.72,3.32,6.59,0.69,3.4,6.57,0.66,3.4,6.58,0.72,3.32,6.59,0.72,3.4,6.55,0.69,3.4,6.57,1.38,3.08,6.33,1.34,3.28,6.29,0.97,3.24,6.53,1.04,3.44,6.39,1.34,3.28,6.29,1.36,3.52,6.11,0.85,3.36,6.5,0.72,3.32,6.59,0.97,3.24,6.53,0.55,3.28,6.67,0.6,3.2,6.71,0.68,3.24,6.63,0.45,3.16,6.67,0.58,3.16,6.73,0.6,3.2,6.71,0.21,3.28,6.4,0.23,3.32,6.42,0.21,3.32,6.4,-0.05,3.24,6.25,-0.05,3.28,6.21,-0.03,3.16,6.13,0,3.44,6.03,-0.01,3.32,6.29,0.06,3.4,6.32,-0.05,3.28,6.21,-0.05,3.24,6.25,-0.01,3.32,6.29,0.54,3.08,6.75,0.45,3.16,6.67,0.35,2.96,6.63,0.09,2.76,6.44,0.13,3.16,6.38,-0.06,3.12,6.29,0.15,3.28,6.37,0.21,3.28,6.4,0.21,3.32,6.4,-0.06,3.12,6.29,0.13,3.16,6.38,-0.05,3.24,6.25,1.66,3.16,5.82,1.61,3.16,5.92,1.62,3.04,5.91,1.45,3.2,6.22,1.51,3.36,6.03,1.34,3.28,6.29,0.68,3.24,6.63,0.72,3.32,6.59,0.68,3.32,6.61,0.3,3.24,6.52,0.55,3.28,6.67,0.54,3.4,6.61,1.48,3.08,6.13,1.45,3.2,6.22,1.5,3.04,6.22,1.45,3.2,6.22,1.38,3.08,6.33,1.5,3.04,6.22,0.72,3.32,6.59,0.68,3.24,6.63,0.97,3.24,6.53,0.6,3.2,6.71,0.61,3.16,6.68,0.68,3.24,6.63,0.58,3.16,6.73,0.61,3.16,6.68,0.6,3.2,6.71,0.55,3.28,6.67,0.45,3.16,6.67,0.6,3.2,6.71,0.3,3.24,6.52,0.45,3.16,6.67,0.55,3.28,6.67,0.35,2.96,6.63,0.45,3.16,6.67,0.3,3.24,6.52,0.13,3.16,6.38,0.21,3.28,6.4,0.15,3.28,6.37,0.15,3.28,6.37,0.06,3.4,6.32,-0.01,3.32,6.29,-0.03,3.12,6.05,-0.03,3.16,6.13,-0.04,3.24,5.99,0.23,3.32,6.42,0.21,3.28,6.4,0.3,3.24,6.52,0.13,3.16,6.38,0.15,3.28,6.37,-0.01,3.32,6.29,-0.05,3.24,6.25,-0.03,3.16,6.13,-0.06,3.12,6.29,1.38,3.08,6.33,0.97,3.24,6.53,1.06,2.96,6.6,0.69,3.08,6.67,0.7,3.04,6.67,0.8,3.04,6.62,0.61,3.16,6.68,0.69,3.08,6.67,0.68,3.24,6.63,0.61,3.12,6.78,0.62,3.08,6.76,0.61,3.16,6.68,1.65,3.32,5.85,1.66,3.16,5.82,1.68,3.16,5.72,1.48,3.08,6.13,1.54,3.08,6.07,1.51,3.36,6.03,1.51,3.36,6.03,1.54,3.08,6.07,1.61,3.16,5.92,1.45,3.2,6.22,1.48,3.08,6.13,1.51,3.36,6.03,1.06,2.96,6.6,0.97,3.24,6.53,0.8,3.04,6.62,0.69,3.08,6.67,0.8,3.04,6.62,0.68,3.24,6.63,0.62,3.08,6.76,0.69,3.08,6.67,0.61,3.16,6.68,0.61,3.12,6.78,0.61,3.16,6.68,0.58,3.16,6.73,0.61,3.12,6.78,0.54,3.08,6.75,0.62,3.08,6.76,0.61,3.12,6.78,0.58,3.16,6.73,0.54,3.08,6.75,0.54,3,6.79,0.54,3.08,6.75,0.35,2.96,6.63,0.49,2.92,6.79,0.54,3,6.79,0.35,2.96,6.63,0.35,2.96,6.63,0.13,3.16,6.38,0.09,2.76,6.44,0.23,3.32,6.42,0.3,3.24,6.52,0.38,3.48,6.5,-0.03,3.12,6.05,-0.09,2.88,6.09,-0.12,2.96,6.22,0.54,3,6.79,0.63,3.04,6.77,0.62,3.08,6.76,-0.03,3.16,6.13,-0.12,2.96,6.22,-0.06,3.12,6.29,-0.03,3.16,6.13,-0.03,3.12,6.05,-0.12,2.96,6.22,1.32,2.84,6.47,1.41,2.56,6.39,1.55,2.72,6.23,0.73,2.88,6.68,0.8,3.04,6.62,0.7,3.04,6.67,0.54,3,6.79,0.62,3.08,6.76,0.54,3.08,6.75,0.49,2.92,6.79,0.35,2.96,6.63,0.37,2.84,6.72,0.35,2.96,6.63,0.09,2.76,6.44,0.28,2.68,6.57,1.59,2.8,6.12,1.57,2.92,6.06,1.53,2.92,6.2,0.8,3.04,6.62,0.97,3.24,6.53,0.68,3.24,6.63,0.54,3.08,6.75,0.58,3.16,6.73,0.45,3.16,6.67,0.09,2.76,6.44,-0.06,3.12,6.29,-0.12,2.96,6.22,-0.09,2.88,6.09,-0.14,2.88,6.17,-0.12,2.96,6.22,1.53,2.92,6.2,1.5,3.04,6.22,1.32,2.84,6.47,1.5,3.04,6.22,1.38,3.08,6.33,1.32,2.84,6.47,0.65,2.96,6.73,0.7,3.04,6.67,0.63,3.04,6.77,0.54,3,6.79,0.49,2.92,6.79,0.65,2.96,6.73,1.71,2.84,5.76,1.66,3.16,5.82,1.62,3.04,5.91,1.71,2.84,5.76,1.65,2.92,5.98,1.66,2.8,5.95,1.06,2.96,6.6,1.32,2.84,6.47,1.38,3.08,6.33,0.37,2.84,6.72,0.35,2.96,6.63,0.28,2.68,6.57,0.3,3.24,6.52,0.21,3.28,6.4,0.13,3.16,6.38,0.09,2.76,6.44,-0.08,2.8,6.27,-0.06,2.64,6.33,1.54,3.08,6.07,1.62,3.04,5.91,1.61,3.16,5.92,1.54,3.08,6.07,1.57,2.92,6.06,1.65,2.92,5.98,1.54,3.08,6.07,1.65,2.92,5.98,1.62,3.04,5.91,1.53,2.92,6.2,1.55,2.72,6.23,1.59,2.8,6.12,0.73,2.88,6.68,0.7,3.04,6.67,0.65,2.96,6.73,0.65,2.96,6.73,0.51,2.84,6.8,0.73,2.88,6.68,-0.07,2.96,5.97,-0.03,2.88,6.02,-0.09,2.88,6.09,-0.03,3.12,6.05,-0.07,2.96,5.97,-0.09,2.88,6.09,-0.09,2.88,6.09,-0.03,2.88,6.02,-0.07,2.84,6,1.32,2.84,6.47,1.06,2.96,6.6,1.28,2.52,6.59,0.35,2.96,6.63,0.3,3.24,6.52,0.13,3.16,6.38,0.51,2.84,6.8,0.38,2.6,6.83,0.58,2.64,6.87,-0.08,2.8,6.27,-0.14,2.88,6.17,-0.13,2.84,6.12,-0.17,2.8,6.04,-0.24,2.68,6.05,-0.16,2.72,6.03,1.71,2.84,5.76,1.62,3.04,5.91,1.65,2.92,5.98,1.59,2.8,6.12,1.63,2.8,6.02,1.57,2.92,6.06,1.28,2.52,6.59,1.06,2.96,6.6,0.73,2.88,6.68,1.63,2.8,6.02,1.66,2.8,5.95,1.65,2.92,5.98,1.53,2.92,6.2,1.32,2.84,6.47,1.55,2.72,6.23,1.06,2.96,6.6,0.8,3.04,6.62,0.73,2.88,6.68,0.51,2.84,6.8,0.37,2.84,6.72,0.38,2.6,6.83,-0.12,2.96,6.22,-0.14,2.88,6.17,-0.08,2.8,6.27,1.63,2.8,6.02,1.63,2.76,6.02,1.66,2.8,5.95,1.63,2.8,6.02,1.65,2.92,5.98,1.57,2.92,6.06,1.59,2.8,6.12,1.53,2.68,6.12,1.63,2.76,6.02,1.28,2.52,6.59,1.41,2.56,6.39,1.32,2.84,6.47,0.49,2.92,6.79,0.51,2.84,6.8,0.65,2.96,6.73,0.27,2.4,6.79,0.38,2.6,6.83,0.24,2.48,6.53,1.63,2.76,6.02,1.53,2.68,6.12,1.56,2.6,5.95,1.59,2.8,6.12,1.55,2.72,6.23,1.53,2.68,6.12,1.55,2.72,6.23,1.41,2.56,6.39,1.59,2.64,6.21,0.51,2.84,6.8,0.58,2.64,6.87,0.73,2.88,6.68,0.09,2.76,6.44,-0.12,2.96,6.22,-0.08,2.8,6.27,-0.11,2.68,6.11,-0.08,2.8,6.27,-0.13,2.84,6.12,-0.03,2.72,5.98,-0.16,2.72,6.03,-0.11,2.68,6.11,-0.24,2.68,6.05,-0.11,2.6,6.11,-0.11,2.68,6.11,1.71,2.84,5.76,1.66,2.8,5.95,1.64,2.6,5.8,1.52,2.52,5.98,1.59,2.52,6.08,1.56,2.32,5.95,1.59,2.64,6.21,1.41,2.56,6.39,1.59,2.52,6.08,0.37,2.84,6.72,0.51,2.84,6.8,0.49,2.92,6.79,0.38,2.6,6.83,0.37,2.84,6.72,0.28,2.68,6.57,0.38,2.6,6.83,0.27,2.4,6.79,0.57,2.52,6.91,0.24,2.48,6.53,0.28,2.68,6.57,0.09,2.76,6.44,-0.06,2.64,6.33,-0.11,2.68,6.11,-0.11,2.6,6.11,-0.16,2.72,6.03,-0.24,2.68,6.05,-0.11,2.68,6.11,-0.06,2.64,6.33,-0.08,2.8,6.27,-0.11,2.68,6.11,1.56,2.6,5.95,1.66,2.8,5.95,1.63,2.76,6.02,1.53,2.68,6.12,1.59,2.52,6.08,1.56,2.6,5.95,1.56,2.6,5.95,1.59,2.52,6.08,1.52,2.52,5.98,-0.06,2.64,6.33,-0.11,2.6,6.11,-0.08,2.32,6.23,0.76,2.4,6.82,1.28,2.52,6.59,0.73,2.88,6.68,1.55,2.72,6.23,1.59,2.64,6.21,1.53,2.68,6.12,1.59,2.64,6.21,1.59,2.52,6.08,1.53,2.68,6.12,-0.08,2.32,6.23,-0.04,2.12,6.13,0.1,2,6.22,1.66,2.8,5.95,1.56,2.6,5.95,1.64,2.6,5.8,1.61,2.24,6.06,1.56,2.32,5.95,1.59,2.52,6.08,1.29,2.24,6.67,0.9,2.28,6.82,1.15,2.08,6.83,0.62,2.4,6.9,0.66,2.36,6.9,0.76,2.4,6.82,0.25,2.28,6.59,-0.08,2.32,6.23,0.1,2,6.22,0.24,2.48,6.53,0.09,2.76,6.44,-0.06,2.64,6.33,-0.11,2.6,6.11,-0.07,2.28,6.11,-0.08,2.32,6.23,1.64,2.48,5.82,1.64,2.48,5.79,1.64,2.6,5.8,1.41,2.44,5.84,1.49,2.44,5.79,1.47,2.52,5.85,1.64,2.48,5.79,1.64,2.48,5.82,1.61,2.44,5.81,1.51,2.52,5.81,1.49,2.44,5.79,1.61,2.44,5.81,1.49,2.44,5.79,1.51,2.52,5.81,1.47,2.52,5.85,1.51,2.52,5.81,1.61,2.44,5.81,1.64,2.48,5.82,-0.06,2.64,6.33,-0.08,2.32,6.23,0.24,2.48,6.53,-0.11,2.6,6.11,-0.23,2.4,5.9,-0.07,2.28,6.11,1.59,2.52,6.08,1.41,2.56,6.39,1.48,2.28,6.29,0.58,2.64,6.87,0.76,2.4,6.82,0.73,2.88,6.68,0.56,2.36,6.96,0.62,2.4,6.9,0.57,2.52,6.91,0.58,2.64,6.87,0.38,2.6,6.83,0.57,2.52,6.91,0.76,2.4,6.82,0.58,2.64,6.87,0.57,2.52,6.91,0.62,2.4,6.9,0.76,2.4,6.82,0.57,2.52,6.91,0.62,2.4,6.9,0.63,2.36,6.91,0.66,2.36,6.9,0.27,2.4,6.79,0.56,2.36,6.96,0.57,2.52,6.91,0.27,2.4,6.79,0.24,2.48,6.53,0.25,2.28,6.59,0.38,2.6,6.83,0.28,2.68,6.57,0.24,2.48,6.53,0.56,2.36,6.96,0.27,2.4,6.79,0.26,2.2,6.87,1.61,2.24,6.06,1.59,2.52,6.08,1.48,2.28,6.29,0.76,2.4,6.82,0.66,2.36,6.9,0.68,2.32,6.91,1.61,2.24,6.06,1.59,2.12,6.1,1.53,2.16,5.97,0.76,2.4,6.82,0.9,2.28,6.82,1.28,2.52,6.59,0.9,2.28,6.82,1.29,2.24,6.67,1.28,2.52,6.59,0.9,2.28,6.82,0.76,2.4,6.82,0.68,2.32,6.91,0.53,2.04,7.05,0.64,2.04,7,0.56,2.36,6.96,-0.08,2.32,6.23,-0.07,2.28,6.11,-0.04,2.12,6.13,0.07,1.84,6.31,0.25,2.28,6.59,0.1,2,6.22,1.28,2.52,6.59,1.48,2.28,6.29,1.41,2.56,6.39,1.15,2.08,6.83,0.9,2.28,6.82,1.03,1.96,6.9,0.68,2.32,6.91,0.64,2.04,7,0.81,2,6.94,0.53,2.04,7.05,0.56,2.36,6.96,0.26,2.2,6.87,1.56,2.32,5.95,1.61,2.24,6.06,1.53,2.16,5.97,1.5,2.12,6,1.53,1.92,6.01,1.53,2,5.94,0.64,2.04,7,0.68,2.32,6.91,0.56,2.36,6.96,0.9,2.28,6.82,0.68,2.32,6.91,0.81,2,6.94,0.19,1.8,6.56,0.18,2.08,6.78,0.25,2.28,6.59,0.27,2.4,6.79,0.25,2.28,6.59,0.26,2.2,6.87,0.25,2.28,6.59,0.24,2.48,6.53,-0.08,2.32,6.23,1.59,2.16,5.85,1.61,2.16,5.82,1.62,2.28,5.86,1.59,2.12,6.1,1.61,2.24,6.06,1.48,2.28,6.29,1.35,2,6.69,1.29,2.24,6.67,1.15,2.08,6.83,1.5,2.12,6,1.5,2.12,5.96,1.53,2.16,5.97,1.29,2.24,6.67,1.35,2,6.69,1.48,2.28,6.29,0.07,1.84,6.31,0.19,1.8,6.56,0.25,2.28,6.59,0.17,1.72,6.5,0.19,1.8,6.56,0.07,1.84,6.31,1.5,2.12,5.96,1.5,2.12,6,1.53,2,5.94,1.5,2.12,6,1.59,2.12,6.1,1.53,1.92,6.01,0.9,2.28,6.82,0.81,2,6.94,1.03,1.96,6.9,0.81,2,6.94,0.64,2.04,7,0.66,1.96,7.01,0.22,2.04,6.9,0.34,1.72,7.04,0.46,1.92,7.07,0.22,2.04,6.9,0.26,2.2,6.87,0.18,2.08,6.78,0.18,2.08,6.78,0.26,2.2,6.87,0.25,2.28,6.59,0.81,2,6.94,0.66,1.96,7.01,0.78,1.88,6.99,0.64,2.04,7,0.53,2.04,7.05,0.57,2,7.1,0.26,2.2,6.87,0.22,2.04,6.9,0.53,2.04,7.05,0.09,1.72,6.8,0.22,2.04,6.9,0.18,2.08,6.78,0.57,2,7.1,0.53,2.04,7.05,0.56,2,7.04,1.59,2.12,6.1,1.52,1.96,6.13,1.53,1.92,6.01,1.52,1.96,6.13,1.59,2.12,6.1,1.48,2.28,6.29,1.28,2.52,6.59,1.29,2.24,6.67,1.48,2.28,6.29,1.25,1.56,6.88,1.44,1.6,6.6,1.35,2,6.69,0.59,1.96,7.05,0.63,1.96,7.02,0.55,2,7.08,0.59,1.96,7.05,0.55,2,7.08,0.46,1.92,7.07,0.58,1.92,7.13,0.59,1.96,7.05,0.46,1.92,7.07,0.48,1.4,7.16,0.56,1.64,7.13,0.34,1.72,7.04,0.58,1.92,7.13,0.46,1.92,7.07,0.57,1.88,7.06,0.09,1.72,6.8,0.34,1.72,7.04,0.22,2.04,6.9,0.1,2,6.22,-0.04,2.12,6.13,0.05,2,5.92,1.51,1.92,5.91,1.58,1.92,5.8,1.58,2,5.84,1.51,1.92,5.91,1.58,2,5.84,1.53,2,5.94,1.53,1.92,6.01,1.51,1.92,5.91,1.53,2,5.94,1.51,1.88,5.91,1.51,1.92,5.91,1.53,1.92,6.01,1.5,2.12,6,1.53,2.16,5.97,1.59,2.12,6.1,1.39,1.88,6.44,1.42,1.68,6.48,1.38,1.64,6.3,1.39,1.88,6.44,1.52,1.96,6.13,1.48,2.28,6.29,0.22,2.04,6.9,0.46,1.92,7.07,0.53,2.04,7.05,0.09,1.72,6.8,0.18,2.08,6.78,0.19,1.8,6.56,1.51,1.88,5.91,1.53,1.92,6.01,1.49,1.84,6.1,1.39,1.88,6.44,1.49,1.84,6.1,1.52,1.96,6.13,0.64,1.88,7.04,0.66,1.96,7.01,0.63,1.96,7.02,0.57,1.88,7.06,0.58,1.88,7.08,0.58,1.92,7.13,0.55,1.84,7.11,0.57,1.88,7.06,0.46,1.92,7.07,0.55,2,7.08,0.53,2.04,7.05,0.46,1.92,7.07,1.35,2,6.69,1.42,1.68,6.48,1.39,1.88,6.44,0.81,2,6.94,0.78,1.88,6.99,1.03,1.96,6.9,0.64,1.88,7.04,0.78,1.88,6.99,0.66,1.96,7.01,0.64,1.88,7.04,0.63,1.96,7.02,0.59,1.96,7.05,0.58,1.88,7.08,0.7,1.76,7.05,0.64,1.88,7.04,0.58,1.88,7.08,0.57,1.88,7.06,0.55,1.84,7.11,0.55,1.84,7.11,0.46,1.92,7.07,0.34,1.72,7.04,0.12,1.84,6.06,0.21,1.8,6.1,0.1,2,6.22,0.21,1.8,6.1,0.13,1.76,6.19,0.1,2,6.22,0.22,1.76,6.06,0.2,1.76,6.11,0.21,1.8,6.1,1.49,1.84,6.1,1.53,1.92,6.01,1.52,1.96,6.13,1.35,2,6.69,1.39,1.88,6.44,1.48,2.28,6.29,1.15,2.08,6.83,1.03,1.96,6.9,1.35,2,6.69,0.21,1.8,6.1,0.2,1.76,6.11,0.13,1.76,6.19,0.12,1.84,6.06,0.1,2,6.22,0.05,2,5.92,0.22,1.76,6.06,0.21,1.8,6.1,0.12,1.84,6.06,0.64,1.44,7.11,0.7,1.76,7.05,0.56,1.64,7.13,0.64,1.88,7.04,0.7,1.76,7.05,0.78,1.88,6.99,0.58,1.88,7.08,0.55,1.84,7.11,0.7,1.76,7.05,0.17,1.72,6.5,0.04,1.56,6.69,0.06,1.68,6.72,0.17,1.72,6.5,0.07,1.84,6.31,0.13,1.56,6.38,0.17,1.72,6.5,0.13,1.56,6.38,0.17,1.6,6.5,0.07,1.84,6.31,0.13,1.76,6.19,0.13,1.72,6.23,0.2,1.76,6.11,0.22,1.76,6.06,0.22,1.72,6.13,1.49,1.68,5.84,1.43,1.72,5.97,1.38,1.64,5.97,1.43,1.68,6.01,1.43,1.72,5.97,1.49,1.84,6.1,1.38,1.64,6.3,1.4,1.6,6.03,1.43,1.68,6.01,1.42,1.68,6.48,1.44,1.6,6.6,1.43,1.6,6.48,1.14,1.64,6.95,0.78,1.88,6.99,0.7,1.76,7.05,0.64,1.44,7.11,0.82,1.44,7.03,0.7,1.76,7.05,1.49,1.68,5.84,1.56,1.88,5.81,1.51,1.88,5.91,1.43,1.72,5.97,1.51,1.88,5.91,1.49,1.84,6.1,1.4,1.6,6.03,1.36,1.56,5.95,1.38,1.64,5.97,1.35,2,6.69,1.44,1.6,6.6,1.42,1.68,6.48,0.34,1.72,7.04,0.56,1.64,7.13,0.55,1.84,7.11,0.09,1.72,6.8,0.19,1.8,6.56,0.06,1.68,6.72,0.09,1.72,6.8,0.06,1.68,6.72,0.1,1.44,6.87,0.13,1.76,6.19,0.07,1.84,6.31,0.1,2,6.22,1.43,1.72,5.97,1.43,1.68,6.01,1.38,1.64,5.97,1.45,1.48,6.57,1.42,1.48,6.45,1.43,1.52,6.45,1.14,1.64,6.95,1.25,1.56,6.88,1.35,2,6.69,1.25,1.56,6.88,1.45,1.48,6.57,1.44,1.6,6.6,1.36,1.56,5.95,1.44,1.6,5.91,1.38,1.64,5.97,1.43,1.68,6.01,1.4,1.6,6.03,1.38,1.64,5.97,1.38,1.64,6.3,1.43,1.68,6.01,1.49,1.84,6.1,0.56,1.64,7.13,0.7,1.76,7.05,0.55,1.84,7.11,1.03,1.96,6.9,1.14,1.64,6.95,1.35,2,6.69,0.19,1.8,6.56,0.17,1.72,6.5,0.06,1.68,6.72,0.13,1.56,6.38,0.15,1.52,6.49,0.17,1.6,6.5,1.43,1.72,5.97,1.49,1.68,5.84,1.51,1.88,5.91,1.48,1.64,5.84,1.51,1.64,5.76,1.49,1.68,5.84,1.45,1.6,5.92,1.47,1.6,5.86,1.48,1.64,5.84,1.48,1.64,5.84,1.38,1.64,5.97,1.45,1.6,5.92,1.33,1.6,5.89,1.45,1.6,5.92,1.38,1.64,5.97,1.44,1.6,5.91,1.45,1.56,5.86,1.49,1.6,5.8,1.36,1.56,5.95,1.45,1.56,5.86,1.44,1.6,5.91,1.36,1.52,5.98,1.36,1.56,5.95,1.4,1.6,6.03,1.41,1.56,6.42,1.42,1.52,6.42,1.37,1.56,6.3,1.41,1.56,6.42,1.37,1.56,6.3,1.38,1.64,6.3,1.39,1.88,6.44,1.38,1.64,6.3,1.49,1.84,6.1,1.43,1.52,6.45,1.41,1.56,6.42,1.43,1.6,6.48,1.25,1.56,6.88,1.19,1.24,6.99,1.45,1.32,6.61,0.06,1.68,6.72,0.04,1.56,6.69,0.1,1.44,6.87,0.04,1.56,6.69,0.03,1.36,6.57,0.1,1.44,6.87,0.17,1.72,6.5,0.17,1.6,6.5,0.04,1.56,6.69,0.21,1.36,6.32,0.16,1.4,6.41,0.13,1.56,6.38,0.07,1.84,6.31,0.13,1.72,6.23,0.13,1.56,6.38,1.36,1.52,5.98,1.36,1.4,6.12,1.27,1.32,6.01,1.37,1.56,6.3,1.4,1.6,6.03,1.38,1.64,6.3,1.42,1.52,6.42,1.39,1.44,6.33,1.37,1.56,6.3,1.42,1.68,6.48,1.43,1.6,6.48,1.41,1.56,6.42,1.43,1.52,6.45,1.42,1.52,6.42,1.41,1.56,6.42,1.42,1.68,6.48,1.41,1.56,6.42,1.38,1.64,6.3,1.19,1.24,6.99,1.27,1.08,6.78,1.45,1.32,6.61,0.64,1.44,7.11,0.56,1.64,7.13,0.48,1.4,7.16,0.17,1.6,6.5,0.06,1.52,6.59,0.04,1.56,6.69,0.15,1.52,6.49,0.06,1.52,6.59,0.17,1.6,6.5,1.36,1.52,5.98,1.27,1.32,6.01,1.3,1.32,5.92,1.39,1.44,6.33,1.32,1.16,6.41,1.33,1.28,6.12,1.25,1.56,6.88,1.14,1.64,6.95,1.19,1.24,6.99,1.14,1.64,6.95,1.03,1.96,6.9,0.78,1.88,6.99,0.67,1.32,7.14,0.64,1.44,7.11,0.48,1.4,7.16,0.13,1.56,6.38,0.15,1.48,6.44,0.15,1.52,6.49,0.16,1.4,6.41,0.15,1.48,6.44,0.13,1.56,6.38,1.37,1.56,6.3,1.39,1.44,6.33,1.36,1.4,6.12,1.37,1.56,6.3,1.36,1.4,6.12,1.4,1.6,6.03,1.42,1.48,6.45,1.42,1.52,6.42,1.43,1.52,6.45,1.39,1.44,6.33,1.42,1.52,6.42,1.42,1.48,6.45,1.45,1.48,6.57,1.43,1.52,6.45,1.43,1.6,6.48,1.45,1.48,6.57,1.45,1.32,6.61,1.42,1.48,6.45,0.04,1.56,6.69,0.06,1.52,6.59,0.03,1.36,6.57,0.15,1.48,6.44,0.03,1.36,6.57,0.06,1.52,6.59,0.27,1.44,6.14,0.22,1.44,6.2,0.18,1.56,6.2,1.36,1.4,6.12,1.33,1.28,6.12,1.27,1.32,6.01,0.82,1.44,7.03,1.14,1.64,6.95,0.7,1.76,7.05,0.67,1.32,7.14,0.48,1.4,7.16,0.61,1.24,7.21,0.34,1.72,7.04,0.09,1.72,6.8,0.1,1.44,6.87,0.25,1.4,7.07,0.34,1.72,7.04,0.1,1.44,6.87,0.27,1.32,6.24,0.18,1.32,6.34,0.21,1.36,6.32,0.21,1.36,6.32,0.13,1.36,6.47,0.16,1.4,6.41,0.22,1.44,6.2,0.21,1.36,6.32,0.13,1.56,6.38,0.13,1.72,6.23,0.18,1.56,6.2,0.13,1.56,6.38,1.36,1.4,6.12,1.36,1.52,5.98,1.4,1.6,6.03,1.14,1.64,6.95,0.92,1.32,7,1.19,1.24,6.99,0.81,1.36,7.02,0.82,1.44,7.03,0.78,1.36,7.04,0.82,1.44,7.03,0.81,1.36,7.02,0.92,1.32,7,0.25,1.4,7.07,0.48,1.4,7.16,0.34,1.72,7.04,0.1,1.44,6.87,0.07,1.24,6.75,0.17,1.16,6.98,0.22,1.44,6.2,0.13,1.56,6.38,0.18,1.56,6.2,0.21,1.36,6.32,0.22,1.44,6.2,0.27,1.32,6.24,1.32,1.16,6.41,1.42,1.48,6.45,1.45,1.32,6.61,1.45,1.48,6.57,1.43,1.6,6.48,1.44,1.6,6.6,0.81,1.36,7.02,0.78,1.36,7.04,0.79,1.32,7.04,0.79,1.32,7.04,0.78,1.36,7.04,0.67,1.32,7.14,0.29,1.32,7.11,0.25,1.4,7.07,0.17,1.16,6.98,0.16,1.4,6.41,0.18,1.32,6.46,0.09,1.32,6.46,0.24,1.36,6.47,0.23,1.32,6.47,0.18,1.32,6.46,0.15,1.48,6.44,0.16,1.4,6.41,0.09,1.32,6.46,0.15,1.48,6.44,0.09,1.32,6.46,0.03,1.36,6.57,0.29,1.28,6.23,0.27,1.32,6.24,0.32,1.32,6.14,0.32,1.32,6.14,0.27,1.32,6.24,0.22,1.44,6.2,1.27,1.32,6.01,1.33,1.28,6.12,1.2,1.24,6.02,1.32,1.16,6.41,1.39,1.44,6.33,1.42,1.48,6.45,0.78,1.36,7.04,0.64,1.44,7.11,0.67,1.32,7.14,0.17,1.16,6.98,0.07,1.24,6.75,0.12,0.8,6.86,0.1,1.44,6.87,0.17,1.16,6.98,0.25,1.4,7.07,0.07,1.24,6.75,0.18,1.04,6.53,0.16,0.96,6.61,0.03,1.36,6.57,0.07,1.24,6.75,0.1,1.44,6.87,0.16,1.4,6.41,0.24,1.36,6.47,0.18,1.32,6.46,0.13,1.16,6.38,0.07,1.2,6.49,0.09,1.32,6.46,1.33,1.28,6.12,1.21,1.2,6.05,1.2,1.24,6.02,0.64,1.44,7.11,0.78,1.36,7.04,0.82,1.44,7.03,0.25,1.4,7.07,0.29,1.32,7.11,0.48,1.4,7.16,0.07,1.2,6.49,0.07,1.24,6.75,0.03,1.36,6.57,0.09,1.32,6.46,0.07,1.2,6.49,0.03,1.36,6.57,1.16,1.12,6.09,1.21,1.2,6.05,1.23,1.08,6.25,1.36,1.4,6.12,1.39,1.44,6.33,1.33,1.28,6.12,1.32,1.16,6.41,1.42,0.96,6.52,1.23,1.08,6.25,1.42,0.96,6.52,1.38,0.76,6.41,1.23,1.08,6.25,0.62,1.08,7.19,0.83,0.76,7.07,1.02,1.04,7,0.67,1.32,7.14,0.62,1.08,7.19,0.79,1.32,7.04,0.29,1.32,7.11,0.62,1.08,7.19,0.61,1.24,7.21,1.21,1.2,6.05,1.33,1.28,6.12,1.23,1.08,6.25,1.44,1.16,6.55,1.45,1.32,6.61,1.27,1.08,6.78,1.25,1.56,6.88,1.45,1.32,6.61,1.45,1.48,6.57,0.82,1.44,7.03,0.92,1.32,7,1.14,1.64,6.95,0.92,1.32,7,0.81,1.36,7.02,0.79,1.32,7.04,0.07,1.24,6.75,0.16,0.96,6.61,0.12,0.8,6.86,1.16,1.16,6.05,1.21,1.2,6.05,1.16,1.12,6.09,0.83,0.76,7.07,0.96,0.76,7.03,1.02,1.04,7,0.67,1.32,7.14,0.61,1.24,7.21,0.62,1.08,7.19,0.61,1.24,7.21,0.48,1.4,7.16,0.29,1.32,7.11,0.13,1.16,6.38,0.09,1.32,6.46,0.18,1.32,6.46,1.11,1.08,6.05,1.15,0.96,6.17,1.1,1,6.05,1.26,1,7,1.31,0.92,6.92,1.27,1.08,6.78,1.02,1.04,7,0.96,0.76,7.03,1.06,0.72,6.99,1.22,0.92,7.01,1.26,1,7,1.02,1.04,7,1.19,1.24,6.99,1.26,1,7,1.27,1.08,6.78,0.62,1.08,7.19,1.02,1.04,7,0.79,1.32,7.04,0.17,1.08,6.37,0.16,1.08,6.41,0.13,1.16,6.38,1.15,0.96,6.17,1.16,1.12,6.09,1.23,1.08,6.25,0.29,1.32,7.11,0.33,0.96,7.16,0.62,1.08,7.19,0.16,1.08,6.41,0.18,1.04,6.53,0.07,1.2,6.49,1.02,1.04,7,1.19,1.24,6.99,0.92,1.32,7,1.22,0.92,7.01,1.02,1.04,7,1.06,0.72,6.99,0.29,1.32,7.11,0.17,1.16,6.98,0.33,0.96,7.16,0.16,1.08,6.41,0.07,1.2,6.49,0.13,1.16,6.38,0.2,1.04,6.41,0.18,1.04,6.53,0.16,1.08,6.41,0.2,1.04,6.41,0.24,0.92,6.48,0.18,1.04,6.53,1.1,1,6.05,1.15,0.96,6.17,0.96,0.88,6.15,1.11,1.08,6.05,1.16,1.12,6.09,1.15,0.96,6.17,1.32,1.16,6.41,1.45,1.32,6.61,1.44,1.16,6.55,1.27,1.08,6.78,1.42,0.96,6.52,1.44,1.16,6.55,1.32,1.16,6.41,1.23,1.08,6.25,1.33,1.28,6.12,0.33,0.96,7.16,0.56,0.96,7.25,0.62,1.08,7.19,0.07,1.2,6.49,0.18,1.04,6.53,0.07,1.24,6.75,1.32,1.16,6.41,1.44,1.16,6.55,1.42,0.96,6.52,1.3,0.8,6.96,1.31,0.92,6.92,1.22,0.92,7.01,1.15,0.96,6.17,1.12,0.88,6.26,0.96,0.88,6.15,1.27,1.08,6.78,1.31,0.92,6.92,1.42,0.96,6.52,1.02,1.04,7,0.92,1.32,7,0.79,1.32,7.04,1.22,0.92,7.01,1.17,0.68,6.93,1.3,0.8,6.96,0.83,0.76,7.07,0.62,1.08,7.19,0.56,0.96,7.25,1.31,0.92,6.92,1.3,0.8,6.96,1.4,0.68,6.88,1.12,0.88,6.26,1.01,0.76,6.15,0.96,0.88,6.15,1.31,0.64,6.49,1.38,0.76,6.41,1.42,0.96,6.52,1.12,0.88,6.26,1.15,0.96,6.17,1.23,1.08,6.25,1.31,0.92,6.92,1.4,0.68,6.88,1.42,0.96,6.52,1.38,0.76,6.41,1.12,0.88,6.26,1.23,1.08,6.25,1.26,1,7,1.22,0.92,7.01,1.31,0.92,6.92,1.26,1,7,1.19,1.24,6.99,1.02,1.04,7,1.51,2.2,5.84,1.58,2.2,5.87,1.49,2.24,5.83,1.63,2.24,5.86,1.63,2.2,5.82,1.63,2.24,5.81,0.65,4.2,5.83,0.58,4.16,5.88,0.71,4.16,5.9])

IndexedFaceSet420.setCoord(Coordinate421)

Shape416.setGeometry(IndexedFaceSet420)

Transform415.addChildren(Shape416)

fieldValue414.addChildren(Transform415)

ProtoInstance412.addFieldValue(fieldValue414)

fieldValue411.addChildren(ProtoInstance412)
ProtoInstance422 = ProtoInstance()
ProtoInstance422.setName("Joint")
ProtoInstance422.setDEF("Allen_hanim_l_elbow")
fieldValue423 = fieldValue()
fieldValue423.setName("name")
fieldValue423.setValue("l_elbow")

ProtoInstance422.addFieldValue(fieldValue423)
fieldValue424 = fieldValue()
fieldValue424.setName("center")
fieldValue424.setValue("0.196 1.07 -0.0518")

ProtoInstance422.addFieldValue(fieldValue424)
fieldValue425 = fieldValue()
fieldValue425.setName("children")
ProtoInstance426 = ProtoInstance()
ProtoInstance426.setName("Segment")
ProtoInstance426.setDEF("Allen_hanim_l_forearm")
fieldValue427 = fieldValue()
fieldValue427.setName("name")
fieldValue427.setValue("l_forearm")

ProtoInstance426.addFieldValue(fieldValue427)
fieldValue428 = fieldValue()
fieldValue428.setName("children")
Transform429 = Transform()
Transform429.setDEF("Allen_l_forearm_adjust")
Transform429.setCenter([-0.634,1.01,0.0799])
Transform429.setRotation([0,1,0,1.570796])
Transform429.setScale([0.1,0.1,0.1])
Shape430 = Shape()
Appearance431 = Appearance()
Material432 = Material()
Material432.setUSE("Skin_Color")

Appearance431.setMaterial(Material432)
ImageTexture433 = ImageTexture()
ImageTexture433.setUSE("camo")

Appearance431.setTexture(ImageTexture433)

Shape430.setAppearance(Appearance431)
IndexedFaceSet434 = IndexedFaceSet()
IndexedFaceSet434.setCoordIndex([0,1,2,-1,3,4,5,-1,6,7,8,-1,9,10,11,-1,12,13,14,-1,15,16,17,-1,18,19,20,-1,21,22,23,-1,24,25,26,-1,27,28,29,-1,30,31,32,-1,33,34,35,-1,36,37,38,-1,39,40,41,-1,42,43,44,-1,45,46,47,-1,48,49,50,-1,51,52,53,-1,54,55,56,-1,57,58,59,-1,60,61,62,-1,63,64,65,-1,66,67,68,-1,69,70,71,-1,72,73,74,-1,75,76,77,-1,78,79,80,-1,81,82,83,-1,84,85,86,-1,87,88,89,-1,90,91,92,-1,93,94,95,-1,96,97,98,-1,99,100,101,-1,102,103,104,-1,105,106,107,-1,108,109,110,-1,111,112,113,-1,114,115,116,-1,117,118,119,-1,120,121,122,-1,123,124,125,-1,126,127,128,-1,129,130,131,-1,132,133,134,-1,135,136,137,-1,138,139,140,-1,141,142,143,-1,144,145,146,-1,147,148,149,-1,150,151,152,-1,153,154,155,-1,156,157,158,-1,159,160,161,-1,162,163,164,-1,165,166,167,-1,168,169,170,-1,171,172,173,-1,174,175,176,-1,177,178,179,-1,180,181,182,-1,183,184,185,-1,186,187,188,-1,189,190,191,-1,192,193,194,-1,195,196,197,-1,198,199,200,-1,201,202,203,-1,204,205,206,-1,207,208,209,-1,210,211,212,-1,213,214,215,-1,216,217,218,-1,219,220,221,-1,222,223,224,-1,225,226,227,-1,228,229,230,-1,231,232,233,-1,234,235,236,-1,237,238,239,-1,240,241,242,-1,243,244,245,-1,246,247,248,-1,249,250,251,-1,252,253,254,-1,255,256,257,-1,258,259,260,-1,261,262,263,-1,264,265,266,-1,267,268,269,-1,270,271,272,-1,273,274,275,-1,276,277,278,-1,279,280,281,-1,282,283,284,-1,285,286,287,-1,288,289,290,-1,291,292,293,-1,294,295,296,-1,297,298,299,-1,300,301,302,-1,303,304,305,-1,306,307,308,-1,309,310,311,-1,312,313,314,-1,315,316,317,-1,318,319,320,-1,321,322,323,-1,324,325,326,-1,327,328,329,-1,330,331,332,-1,333,334,335,-1,336,337,338,-1,339,340,341,-1,342,343,344,-1,345,346,347,-1,348,349,350,-1,351,352,353,-1,354,355,356,-1,357,358,359,-1,360,361,362,-1,363,364,365,-1,366,367,368,-1,369,370,371,-1,372,373,374,-1,375,376,377,-1,378,379,380,-1,381,382,383,-1,384,385,386,-1,387,388,389,-1,390,391,392,-1,393,394,395,-1,396,397,398,-1,399,400,401,-1,402,403,404,-1,405,406,407,-1,408,409,410,-1,411,412,413,-1,414,415,416,-1,417,418,419,-1,420,421,422,-1,423,424,425,-1,426,427,428,-1,429,430,431,-1,432,433,434,-1,435,436,437,-1,438,439,440,-1,441,442,443,-1,444,445,446,-1,447,448,449,-1,450,451,452,-1,453,454,455,-1,456,457,458,-1,459,460,461,-1,462,463,464,-1,465,466,467,-1,468,469,470,-1,471,472,473,-1,474,475,476,-1,477,478,479,-1,480,481,482,-1,483,484,485,-1,486,487,488,-1,489,490,491,-1,492,493,494,-1,495,496,497,-1,498,499,500,-1,501,502,503,-1,504,505,506,-1,507,508,509,-1,510,511,512,-1,513,514,515,-1,516,517,518,-1,519,520,521,-1,522,523,524,-1,525,526,527,-1,528,529,530,-1,531,532,533,-1,534,535,536,-1,537,538,539,-1,540,541,542,-1,543,544,545,-1,546,547,548,-1,549,550,551,-1,552,553,554,-1,555,556,557,-1,558,559,560,-1,561,562,563,-1,564,565,566,-1,567,568,569,-1,570,571,572,-1,573,574,575,-1,576,577,578,-1,579,580,581,-1,582,583,584,-1,585,586,587,-1,588,589,590,-1,591,592,593,-1,594,595,596,-1,597,598,599,-1,600,601,602,-1,603,604,605,-1,606,607,608,-1,609,610,611,-1,612,613,614,-1,615,616,617,-1,618,619,620,-1,621,622,623,-1,624,625,626,-1,627,628,629,-1,630,631,632,-1,633,634,635,-1,636,637,638,-1,639,640,641,-1,642,643,644,-1,645,646,647,-1,648,649,650,-1,651,652,653,-1,654,655,656,-1,657,658,659,-1,660,661,662,-1,663,664,665,-1,666,667,668,-1,669,670,671,-1,672,673,674,-1,675,676,677,-1,678,679,680,-1,681,682,683,-1,684,685,686,-1,687,688,689,-1,690,691,692,-1,693,694,695,-1,696,697,698,-1,699,700,701,-1,702,703,704,-1,705,706,707,-1,708,709,710,-1,711,712,713,-1,714,715,716,-1,717,718,719,-1,720,721,722,-1,723,724,725,-1,726,727,728,-1,729,730,731,-1,732,733,734,-1,735,736,737,-1,738,739,740,-1,741,742,743,-1,744,745,746,-1,747,748,749,-1,750,751,752,-1,753,754,755,-1,756,757,758,-1,759,760,761,-1,762,763,764,-1,765,766,767,-1,768,769,770,-1,771,772,773,-1,774,775,776,-1,777,778,779,-1,780,781,782,-1,783,784,785,-1,786,787,788,-1,789,790,791,-1,792,793,794,-1,795,796,797,-1,798,799,800,-1,801,802,803,-1,804,805,806,-1,807,808,809,-1,810,811,812,-1,813,814,815,-1,816,817,818,-1,819,820,821,-1,822,823,824,-1,825,826,827,-1,828,829,830,-1,831,832,833,-1,834,835,836,-1,837,838,839,-1,840,841,842,-1,843,844,845,-1,846,847,848,-1,849,850,851,-1,852,853,854,-1,855,856,857,-1,858,859,860,-1,861,862,863,-1,864,865,866,-1,867,868,869,-1,870,871,872,-1,873,874,875,-1,876,877,878,-1,879,880,881,-1,882,883,884,-1,885,886,887,-1,888,889,890,-1,891,892,893,-1,894,895,896,-1,897,898,899,-1,900,901,902,-1,903,904,905,-1,906,907,908,-1,909,910,911,-1,912,913,914,-1,915,916,917,-1,918,919,920,-1,921,922,923,-1,924,925,926,-1,927,928,929,-1,930,931,932,-1,933,934,935,-1,936,937,938,-1,939,940,941,-1,942,943,944,-1,945,946,947,-1,948,949,950,-1,951,952,953,-1,954,955,956,-1,957,958,959,-1,960,961,962,-1,963,964,965,-1,966,967,968,-1,969,970,971,-1,972,973,974,-1,975,976,977,-1,978,979,980,-1,981,982,983,-1,984,985,986,-1,987,988,989,-1,990,991,992,-1,993,994,995,-1,996,997,998,-1,999,1000,1001,-1,1002,1003,1004,-1,1005,1006,1007,-1,1008,1009,1010,-1,1011,1012,1013,-1,1014,1015,1016,-1,1017,1018,1019,-1,1020,1021,1022,-1,1023,1024,1025,-1,1026,1027,1028,-1,1029,1030,1031,-1,1032,1033,1034,-1,1035,1036,1037,-1,1038,1039,1040,-1,1041,1042,1043,-1,1044,1045,1046,-1,1047,1048,1049,-1,1050,1051,1052,-1,1053,1054,1055,-1,1056,1057,1058,-1,1059,1060,1061,-1,1062,1063,1064,-1,1065,1066,1067,-1,1068,1069,1070,-1,1071,1072,1073,-1,1074,1075,1076,-1,1077,1078,1079,-1,1080,1081,1082,-1,1083,1084,1085,-1,1086,1087,1088,-1,1089,1090,1091,-1,1092,1093,1094,-1,1095,1096,1097,-1,1098,1099,1100,-1,1101,1102,1103,-1,1104,1105,1106,-1,1107,1108,1109,-1,1110,1111,1112,-1,1113,1114,1115,-1,1116,1117,1118,-1,1119,1120,1121,-1,1122,1123,1124,-1,1125,1126,1127,-1,1128,1129,1130,-1,1131,1132,1133,-1,1134,1135,1136,-1,1137,1138,1139,-1,1140,1141,1142,-1,1143,1144,1145,-1,1146,1147,1148,-1,1149,1150,1151,-1,1152,1153,1154,-1,1155,1156,1157,-1,1158,1159,1160,-1,1161,1162,1163,-1,1164,1165,1166,-1,1167,1168,1169,-1,1170,1171,1172,-1,1173,1174,1175,-1,1176,1177,1178,-1,1179,1180,1181,-1,1182,1183,1184,-1,1185,1186,1187,-1,1188,1189,1190,-1,1191,1192,1193,-1,1194,1195,1196,-1,1197,1198,1199,-1,1200,1201,1202,-1,1203,1204,1205,-1,1206,1207,1208,-1,1209,1210,1211,-1,1212,1213,1214,-1,1215,1216,1217,-1,1218,1219,1220,-1,1221,1222,1223,-1,1224,1225,1226,-1,1227,1228,1229,-1,1230,1231,1232,-1,1233,1234,1235,-1,1236,1237,1238,-1,1239,1240,1241,-1,1242,1243,1244,-1,1245,1246,1247,-1,1248,1249,1250,-1,1251,1252,1253,-1,1254,1255,1256,-1,1257,1258,1259,-1,1260,1261,1262,-1,1263,1264,1265,-1,1266,1267,1268,-1,1269,1270,1271,-1,1272,1273,1274,-1,1275,1276,1277,-1,1278,1279,1280,-1,1281,1282,1283,-1,1284,1285,1286,-1,1287,1288,1289,-1,1290,1291,1292,-1,1293,1294,1295,-1,1296,1297,1298,-1,1299,1300,1301,-1,1302,1303,1304,-1,1305,1306,1307,-1,1308,1309,1310,-1,1311,1312,1313,-1,1314,1315,1316,-1,1317,1318,1319,-1,1320,1321,1322,-1,1323,1324,1325,-1,1326,1327,1328,-1,1329,1330,1331,-1,1332,1333,1334,-1,1335,1336,1337,-1,1338,1339,1340,-1,1341,1342,1343,-1,1344,1345,1346,-1,1347,1348,1349,-1,1350,1351,1352,-1,1353,1354,1355,-1,1356,1357,1358,-1,1359,1360,1361,-1,1362,1363,1364,-1,1365,1366,1367,-1,1368,1369,1370,-1,1371,1372,1373,-1,1374,1375,1376,-1,1377,1378,1379,-1,1380,1381,1382,-1,1383,1384,1385,-1,1386,1387,1388,-1,1389,1390,1391,-1,1392,1393,1394,-1,1395,1396,1397,-1,1398,1399,1400,-1,1401,1402,1403,-1,1404,1405,1406,-1,1407,1408,1409,-1,1410,1411,1412,-1,1413,1414,1415,-1,1416,1417,1418,-1,1419,1420,1421,-1,1422,1423,1424,-1,1425,1426,1427,-1,1428,1429,1430,-1,1431,1432,1433,-1,1434,1435,1436,-1,1437,1438,1439,-1,1440,1441,1442,-1,1443,1444,1445,-1,1446,1447,1448,-1,1449,1450,1451,-1,1452,1453,1454,-1,1455,1456,1457,-1,1458,1459,1460,-1,1461,1462,1463,-1,1464,1465,1466,-1,1467,1468,1469,-1,1470,1471,1472,-1,1473,1474,1475,-1,1476,1477,1478,-1,1479,1480,1481,-1,1482,1483,1484,-1,1485,1486,1487,-1])
IndexedFaceSet434.setCreaseAngle(1.75)
Coordinate435 = Coordinate()
Coordinate435.setPoint([0.33,0.96,9.16,0.17,1.16,8.98,0.12,0.8,8.87,1.22,0.92,9.02,1.06,0.72,9,1.17,0.68,8.93,0.22,0.96,8.32,0.24,0.92,8.49,0.2,1.04,8.41,0.24,0.92,8.49,0.16,0.96,8.61,0.18,1.04,8.53,1.3,0.6,8.32,1.16,0.64,8.16,1.12,0.88,8.26,0.22,0.96,8.32,0.33,0.8,8.43,0.24,0.92,8.49,0.12,0.8,8.87,0.16,0.96,8.61,0.1,0.72,8.64,1.04,0.68,8.1,1.01,0.76,8.16,1.16,0.64,8.16,1.01,0.76,8.16,1.12,0.88,8.26,1.16,0.64,8.16,0.28,0.72,9.23,0.33,0.96,9.16,0.12,0.8,8.87,0.32,0.64,9.28,0.28,0.72,9.23,0.17,0.64,9.16,0.3,0.96,8.23,0.43,0.8,8.18,0.44,0.76,8.24,0.56,0.96,9.26,0.44,0.64,9.33,0.72,0.56,9.22,0.25,0.8,8.52,0.1,0.72,8.64,0.16,0.96,8.61,0.33,0.8,8.43,0.25,0.8,8.52,0.24,0.92,8.49,0.37,0.72,8.36,0.33,0.8,8.43,0.3,0.96,8.23,0.33,0.8,8.43,0.22,0.96,8.32,0.3,0.96,8.23,1.4,0.68,8.88,1.31,0.64,8.5,1.42,0.96,8.53,1.3,0.8,8.97,1.26,0.6,8.94,1.35,0.6,8.93,0.83,0.76,9.08,0.56,0.96,9.26,0.72,0.56,9.22,0.56,0.96,9.26,0.33,0.96,9.16,0.44,0.64,9.33,0.25,0.8,8.52,0.16,0.96,8.61,0.24,0.92,8.49,0.21,0.64,8.46,0.19,0.64,8.48,0.25,0.72,8.49,0.44,0.76,8.24,0.48,0.72,8.25,0.37,0.72,8.36,0.44,0.76,8.24,0.37,0.72,8.36,0.3,0.96,8.23,1.04,0.68,8.1,0.98,0.72,8.11,1.01,0.76,8.16,1.16,0.64,8.16,1.3,0.6,8.32,1.28,0.52,8.33,1.38,0.76,8.41,1.3,0.6,8.32,1.12,0.88,8.26,1.28,0.52,8.33,1.31,0.64,8.5,1.37,0.48,8.56,1.17,0.68,8.93,1.06,0.72,9,1.06,0.68,9,1.03,0.68,9.02,1.06,0.68,9,1.06,0.72,9,0.96,0.76,9.03,0.94,0.68,9.05,1.03,0.68,9.02,1.04,0.64,9.02,0.98,0.4,9.05,1.09,0.6,8.98,0.94,0.68,9.05,0.83,0.76,9.08,0.72,0.56,9.22,1.09,0.2,8.87,1.13,0.36,8.87,0.98,0.4,9.05,0.94,0.68,9.05,0.96,0.76,9.03,0.83,0.76,9.08,0.33,0.96,9.16,0.28,0.72,9.23,0.44,0.64,9.33,0.17,0.64,9.16,0.28,0.72,9.23,0.12,0.8,8.87,0.25,0.8,8.52,0.25,0.72,8.49,0.1,0.72,8.64,1.02,0.64,8.08,1.08,0.6,8.11,1,0.44,8.13,1.08,0.6,8.11,1.04,0.68,8.1,1.16,0.64,8.16,1.31,0.64,8.5,1.3,0.6,8.32,1.38,0.76,8.41,1.31,0.64,8.5,1.4,0.68,8.88,1.43,0.56,8.79,1.17,0.56,8.9,1.26,0.6,8.94,1.17,0.68,8.93,1.06,0.68,9,1.03,0.68,9.02,1.04,0.64,9.02,0.96,0.76,9.03,1.03,0.68,9.02,1.06,0.72,9,0.28,0.72,9.23,0.32,0.64,9.28,0.44,0.64,9.33,0.32,0.64,9.28,0.46,0.36,9.32,0.44,0.64,9.33,0.09,0.6,9.03,0.17,0.64,9.16,0.12,0.8,8.87,0.25,0.72,8.49,0.19,0.64,8.48,0.1,0.72,8.64,1.02,0.64,8.08,1.04,0.68,8.1,1.08,0.6,8.11,1,0.44,8.13,1.09,0.48,8.17,1.01,0.36,8.19,1.08,0.6,8.11,1.09,0.48,8.17,1,0.44,8.13,1.09,0.48,8.17,1.08,0.6,8.11,1.16,0.64,8.16,1.3,0.6,8.32,1.31,0.64,8.5,1.28,0.52,8.33,1.3,0.8,8.97,1.17,0.68,8.93,1.26,0.6,8.94,1.4,0.68,8.88,1.3,0.8,8.97,1.35,0.6,8.93,1.17,0.68,8.93,1.06,0.68,9,1.09,0.6,8.98,1.04,0.64,9.02,1.03,0.68,9.02,0.94,0.68,9.05,0.32,0.64,9.28,0.17,0.64,9.16,0.17,0.32,9.16,0.12,0.8,8.87,0.07,0.56,8.9,0.09,0.6,9.03,0.19,0.64,8.48,0.11,0.6,8.57,0.1,0.72,8.64,1.17,0.56,8.9,1.17,0.68,8.93,1.09,0.6,8.98,1.17,0.56,8.9,1.09,0.6,8.98,1.12,0.48,8.93,1.04,0.64,9.02,1.09,0.6,8.98,1.06,0.68,9,0.1,0.72,8.64,0.11,0.6,8.57,0.06,0.52,8.68,0.17,0.32,9.16,0.07,0.08,9.13,0.19,0.12,9.26,0.07,0.56,8.9,0.12,0.8,8.87,0.1,0.72,8.64,1.37,0.48,8.56,1.31,0.64,8.5,1.43,0.56,8.79,1.43,0.56,8.79,1.4,0.68,8.88,1.35,0.6,8.93,1,0.44,8.13,1.01,0.36,8.19,0.98,0.36,8.18,1.09,0.48,8.17,1.28,0.52,8.33,1.26,0.32,8.46,1.28,0.52,8.33,1.37,0.48,8.56,1.26,0.32,8.46,1.43,0.56,8.79,1.35,0.6,8.93,1.44,0.52,8.91,1.36,0.48,8.9,1.43,0.56,8.79,1.44,0.52,8.91,1.19,0.48,8.87,1.26,0.52,8.89,1.17,0.56,8.9,0.98,0.4,9.05,0.94,0.68,9.05,0.72,0.56,9.22,0.17,0.4,8.5,0.16,0.32,8.65,0.06,0.52,8.68,0.16,0.52,8.45,0.15,0.48,8.48,0.11,0.6,8.57,1.19,0.48,8.87,1.17,0.56,8.9,1.12,0.48,8.93,1.04,0.64,9.02,0.94,0.68,9.05,0.98,0.4,9.05,0.06,0.52,8.68,0.07,0.56,8.9,0.1,0.72,8.64,0.15,0.48,8.48,0.06,0.52,8.68,0.11,0.6,8.57,0.16,0.52,8.45,0.11,0.6,8.57,0.19,0.64,8.48,0.16,0.48,8.46,0.15,0.48,8.48,0.16,0.52,8.45,1.09,0.48,8.17,1.16,0.64,8.16,1.28,0.52,8.33,1.36,0.48,8.9,1.44,0.52,8.91,1.35,0.6,8.93,0.98,0.24,8.22,1.01,0.36,8.19,1.12,0.2,8.45,1.36,0.48,8.9,1.43,0.44,8.82,1.43,0.56,8.79,1.41,0.4,8.79,1.43,0.44,8.82,1.47,0.4,8.9,1.21,0.44,8.85,1.19,0.48,8.87,1.13,0.36,8.87,1.19,0.48,8.87,1.12,0.48,8.93,1.13,0.36,8.87,1.12,0.48,8.93,1.09,0.6,8.98,0.98,0.4,9.05,1.01,0.36,8.19,1.09,0.48,8.17,1.26,0.32,8.46,1.25,0.32,8.62,1.37,0.48,8.56,1.32,0.4,8.71,1.34,0.4,8.73,1.32,0.4,8.71,1.36,0.44,8.72,1.21,0.44,8.85,1.13,0.36,8.87,1.21,0.36,8.81,1.13,0.36,8.87,1.12,0.48,8.93,0.98,0.4,9.05,1.43,0.44,8.82,1.36,0.44,8.72,1.43,0.56,8.79,0.98,0.24,8.22,1,0.08,8.35,0.95,0.08,8.27,1.36,0.44,8.72,1.37,0.48,8.56,1.43,0.56,8.79,1.43,0.44,8.82,1.41,0.4,8.79,1.36,0.44,8.72,1.32,0.4,8.71,1.34,0.4,8.73,1.34,0.36,8.73,1.4,0.36,8.78,1.34,0.36,8.73,1.34,0.4,8.73,1.43,0.44,8.82,1.4,0.36,8.78,1.34,0.4,8.73,1.4,0.36,8.78,1.43,0.44,8.82,1.35,0.36,8.85,1.3,0.44,8.89,1.21,0.44,8.85,1.21,0.36,8.81,1.3,0.44,8.89,1.21,0.36,8.81,1.35,0.36,8.85,1.3,0.44,8.89,1.35,0.36,8.85,1.36,0.48,8.9,1.35,0.36,8.85,1.43,0.44,8.82,1.36,0.48,8.9,0.17,0.32,9.16,0.17,0.64,9.16,0.09,0.6,9.03,0.17,0.32,9.16,0.07,0.56,8.9,0.01,0.12,8.87,0.07,0.56,8.9,0.17,0.32,9.16,0.09,0.6,9.03,0.23,0.28,8.55,0.17,0.4,8.5,0.24,0.36,8.46,0.15,0.48,8.48,0.17,0.4,8.5,0.06,0.52,8.68,0.98,0.36,8.18,1.01,0.36,8.19,0.98,0.24,8.22,1.25,0.32,8.62,1.26,0.32,8.46,1.37,0.48,8.56,1.36,0.16,8.61,1.29,0.12,8.51,1.18,0.24,8.59,1.34,0.36,8.73,1.25,0.32,8.62,1.32,0.4,8.71,1.37,0.48,8.56,1.36,0.44,8.72,1.32,0.4,8.71,1.18,0.28,8.79,1.13,0.36,8.87,1.09,0.2,8.87,1.21,0.36,8.81,1.13,0.36,8.87,1.18,0.28,8.79,0.72,0.56,9.22,0.46,0.36,9.32,0.66,0.12,9.33,0.98,0.4,9.05,0.72,0.56,9.22,0.66,0.12,9.33,0.44,0.04,9.38,0.61,-0.44,9.33,0.66,0.12,9.33,0.19,0.12,9.26,0.44,0.04,9.38,0.46,0.36,9.32,0.27,0.28,8.47,0.24,0.36,8.46,0.27,0.36,8.4,0.38,0.28,8.36,0.27,0.28,8.47,0.27,0.36,8.4,1.16,0.24,8.53,1.12,0.2,8.45,1.26,0.32,8.46,1.35,0.28,8.81,1.4,0.36,8.78,1.35,0.36,8.85,1.31,0.28,8.82,1.35,0.28,8.81,1.35,0.36,8.85,1.13,0.16,8.52,1.16,0.24,8.53,1.29,0.12,8.51,1.36,0.16,8.61,1.18,0.24,8.59,1.25,0.32,8.62,1.39,0.24,8.76,1.39,0.24,8.7,1.34,0.36,8.73,1.39,0.24,8.76,1.35,0.28,8.81,1.32,0.24,8.79,1.35,0.28,8.81,1.34,0.36,8.73,1.4,0.36,8.78,0.09,0.08,8.55,0.03,0.08,8.7,0.19,0.24,8.55,0.23,0.28,8.55,0.16,0.32,8.65,0.17,0.4,8.5,0.21,0.24,8.53,0.19,0.24,8.55,0.23,0.28,8.55,1.26,0.32,8.46,1.25,0.32,8.62,1.18,0.24,8.59,1.13,0.16,8.52,1.12,0.2,8.45,1.16,0.24,8.53,1.35,0.28,8.81,1.39,0.24,8.76,1.34,0.36,8.73,1.09,0.2,8.87,1.14,0.16,8.76,1.18,0.28,8.79,0.23,0.28,8.55,0.24,0.36,8.46,0.27,0.28,8.47,0.23,0.28,8.55,0.19,0.24,8.55,0.16,0.32,8.65,1.16,0.24,8.53,1.18,0.24,8.59,1.29,0.12,8.51,1.16,0.24,8.53,1.26,0.32,8.46,1.18,0.24,8.59,1.14,0.16,8.76,1.12,0,8.73,1.19,0.08,8.68,0.44,0.64,9.33,0.46,0.36,9.32,0.72,0.56,9.22,0.07,0.56,8.9,0.06,0.52,8.68,0.16,0.32,8.65,0.01,0.12,8.87,0.03,0.08,8.7,0.09,-0.12,8.71,0.07,0.08,9.13,0.17,0.32,9.16,0.01,0.12,8.87,1.06,0.12,8.46,1.12,0.2,8.45,1.13,0.16,8.52,1.12,0.2,8.45,1.06,0.12,8.46,0.98,0.24,8.22,1.06,0.12,8.46,1.13,0,8.33,1,0.08,8.35,1.39,0.24,8.7,1.36,0.16,8.61,1.25,0.32,8.62,1.34,0.36,8.73,1.39,0.24,8.7,1.25,0.32,8.62,1.36,0.16,8.61,1.39,0.24,8.7,1.33,0.12,8.72,1.36,0.08,8.68,1.36,0.16,8.61,1.33,0.12,8.72,1.32,0.16,8.75,1.33,0.12,8.72,1.39,0.24,8.7,1.39,0.24,8.76,1.32,0.16,8.75,1.39,0.24,8.7,1.32,0.16,8.75,1.39,0.24,8.76,1.32,0.24,8.79,1.33,0.12,8.72,1.32,0.16,8.75,1.25,0.12,8.73,1.18,0.28,8.79,1.14,0.16,8.76,1.25,0.12,8.73,1.18,0.28,8.79,1.32,0.16,8.75,1.32,0.24,8.79,1.18,0.28,8.79,1.25,0.12,8.73,1.32,0.16,8.75,1.16,-0.08,8.65,1.14,-0.28,8.79,1.21,-0.32,8.57,1.14,0.16,8.76,1.19,0.08,8.68,1.25,0.12,8.73,0.01,0.12,8.87,0.07,0.56,8.9,0.16,0.32,8.65,1.09,0.2,8.87,0.98,0.4,9.05,0.66,0.12,9.33,0.66,0.12,9.33,0.46,0.36,9.32,0.44,0.04,9.38,0.19,0.12,9.26,0.46,0.36,9.32,0.17,0.32,9.16,0.01,0.12,8.87,0.16,0.32,8.65,0.03,0.08,8.7,0.03,0.08,8.7,0.16,0.32,8.65,0.19,0.24,8.55,0.01,0.12,8.87,0.06,-0.08,9.09,0.07,0.08,9.13,1.3,0.04,8.47,1.13,0,8.33,1.06,0.12,8.46,1.13,0,8.33,1.3,0.04,8.47,1.14,-0.16,8.4,1.06,0.12,8.46,1,0.08,8.35,0.98,0.24,8.22,1.3,0.04,8.47,1.29,0.12,8.51,1.33,0,8.58,0.95,0.08,8.27,0.97,0.04,8.37,0.87,0,8.33,1,0.08,8.35,1.13,0,8.33,1.02,0,8.33,1.01,0.36,8.19,1.26,0.32,8.46,1.12,0.2,8.45,1.3,0.04,8.47,1.33,0,8.58,1.26,-0.16,8.5,0.46,0.36,9.32,0.32,0.64,9.28,0.17,0.32,9.16,0.03,0.08,8.7,0.19,-0.08,8.6,0.09,-0.12,8.71,0.12,0.04,8.5,0.09,0.08,8.55,0.19,0.24,8.55,0.87,0,8.33,0.97,0.04,8.37,1.02,0,8.33,0.97,0.04,8.37,0.95,0.08,8.27,1,0.08,8.35,0.97,0.04,8.37,1,0.08,8.35,1.02,0,8.33,1.3,0.04,8.47,1.26,-0.16,8.5,1.14,-0.16,8.4,1.3,0.04,8.47,1.06,0.12,8.46,1.13,0.16,8.52,1.29,0.12,8.51,1.3,0.04,8.47,1.13,0.16,8.52,1.36,0.16,8.61,1.3,0.04,8.65,1.33,0,8.58,1.36,0.16,8.61,1.36,0.08,8.68,1.3,0.04,8.65,1.29,0.12,8.51,1.36,0.16,8.61,1.33,0,8.58,1.16,-0.08,8.65,1.21,-0.32,8.57,1.26,-0.16,8.5,1.09,0.2,8.87,0.66,0.12,9.33,0.93,-0.32,9.09,0.26,-0.16,9.32,0.07,0.08,9.13,0.06,-0.08,9.09,0.26,-0.16,9.32,0.19,0.12,9.26,0.07,0.08,9.13,0.03,0.08,8.7,0.09,0.08,8.55,0.19,-0.08,8.6,1.3,0.04,8.65,1.19,0.08,8.68,1.16,-0.08,8.65,1.33,0,8.58,1.3,0.04,8.65,1.16,-0.08,8.65,0,-0.36,9.14,0.06,-0.32,8.69,-0.08,-0.56,8.84,0.09,0.08,8.55,0.12,0.04,8.5,0.19,-0.08,8.6,0.12,0.04,8.5,0.16,0,8.47,0.19,-0.08,8.6,1.13,0,8.33,1.09,-0.08,8.28,1.02,0,8.33,0.99,-0.04,8.24,1.02,0,8.33,1.09,-0.08,8.28,0.99,-0.04,8.24,1.09,-0.08,8.28,1,-0.16,8.24,0.98,-0.2,8.29,1,-0.16,8.24,1.09,-0.08,8.28,0.16,0,8.47,0.2,0,8.41,0.3,-0.08,8.45,0.19,-0.08,8.6,0.16,0,8.47,0.3,-0.08,8.45,0.36,-0.08,8.37,0.3,-0.08,8.45,0.2,0,8.41,1.09,-0.08,8.28,1.13,0,8.33,1.14,-0.16,8.4,1.19,0.08,8.68,1.12,0,8.73,1.16,-0.08,8.65,1.14,-0.28,8.79,1.16,-0.08,8.65,1.12,0,8.73,1.14,0.16,8.76,1.09,0.2,8.87,1.12,0,8.73,1.09,0.2,8.87,0.93,-0.32,9.09,1.12,0,8.73,0.19,0.12,9.26,0.26,-0.16,9.32,0.44,0.04,9.38,0.01,0.12,8.87,0.09,-0.12,8.71,0.06,-0.08,9.09,0.98,-0.2,8.29,1.09,-0.08,8.28,1.14,-0.16,8.4,0.18,-0.16,8.59,0.15,-0.24,8.6,0.09,-0.12,8.71,0.98,-0.2,8.29,1.14,-0.16,8.4,0.99,-0.28,8.32,1.26,-0.16,8.5,1.21,-0.32,8.57,1.14,-0.16,8.4,0.61,-0.44,9.33,0.93,-0.32,9.09,0.66,0.12,9.33,0.19,-0.08,8.6,0.18,-0.16,8.59,0.09,-0.12,8.71,0.15,-0.24,8.6,0.06,-0.32,8.69,0.09,-0.12,8.71,0.17,-0.24,8.58,0.15,-0.24,8.6,0.18,-0.16,8.59,1.33,0,8.58,1.16,-0.08,8.65,1.26,-0.16,8.5,0.44,0.04,9.38,0.39,-0.32,9.41,0.61,-0.44,9.33,0,-0.36,9.14,-0.08,-0.56,8.84,-0.11,-0.64,9.03,1.12,-0.36,8.45,0.99,-0.28,8.32,1.14,-0.16,8.4,1.21,-0.32,8.57,1.12,-0.36,8.45,1.14,-0.16,8.4,0.13,-0.36,9.3,0.26,-0.16,9.32,0.06,-0.08,9.09,0,-0.36,9.14,0.09,-0.12,8.71,0.06,-0.32,8.69,0.99,-0.28,8.32,1.12,-0.36,8.45,0.93,-0.32,8.33,1,-0.6,8.53,1.12,-0.48,8.56,1.04,-0.52,8.86,1.12,-0.48,8.56,1.14,-0.28,8.79,1.04,-0.52,8.86,1.12,-0.48,8.56,1.12,-0.36,8.45,1.21,-0.32,8.57,0.61,-0.44,9.33,0.39,-0.64,9.4,0.85,-0.84,9.14,0.13,-0.36,9.3,0.06,-0.08,9.09,0,-0.36,9.14,0.93,-0.32,9.09,1.04,-0.52,8.86,1.14,-0.28,8.79,0.93,-0.32,9.09,1.14,-0.28,8.79,1.12,0,8.73,0.18,-0.6,9.37,0.39,-0.64,9.4,0.39,-0.32,9.41,0.26,-0.16,9.32,0.13,-0.36,9.3,0.39,-0.32,9.41,0.18,-0.6,9.37,0.39,-0.32,9.41,0.13,-0.36,9.3,-0.11,-0.64,9.03,-0.03,-0.88,9.26,0.18,-0.6,9.37,0.16,-0.4,8.61,0.06,-0.32,8.69,0.15,-0.24,8.6,0.61,-0.44,9.33,0.91,-0.44,9.11,0.93,-0.32,9.09,0.21,-0.44,8.55,0.12,-0.44,8.64,0.16,-0.4,8.61,0.93,-0.32,8.33,1,-0.6,8.53,0.86,-0.64,8.48,1.12,-0.48,8.56,1.21,-0.32,8.57,1.14,-0.28,8.79,0.86,-0.64,8.48,1,-0.6,8.53,0.9,-0.96,8.82,-0.02,-0.84,8.73,-0.08,-0.56,8.84,0.04,-0.6,8.63,0.06,-0.32,8.69,0.12,-0.44,8.64,0.02,-0.52,8.65,0.08,-0.52,8.58,0.02,-0.52,8.65,0.12,-0.44,8.64,0.12,-0.44,8.64,0.06,-0.32,8.69,0.16,-0.4,8.61,0.91,-0.44,9.11,0.85,-0.84,9.14,0.95,-0.84,9.02,1.04,-0.52,8.86,0.93,-0.32,9.09,0.91,-0.44,9.11,0.02,-0.52,8.65,-0.08,-0.56,8.84,0.06,-0.32,8.69,0.02,-0.52,8.65,0.08,-0.52,8.58,0.06,-0.56,8.61,0.08,-0.52,8.58,0.08,-0.56,8.58,0.06,-0.56,8.61,0.9,-0.96,8.82,0.61,-0.92,8.55,0.75,-0.72,8.49,1,-0.76,8.9,0.91,-0.44,9.11,0.95,-0.84,9.02,0.44,0.04,9.38,0.26,-0.16,9.32,0.39,-0.32,9.41,0,-0.36,9.14,0.18,-0.6,9.37,0.13,-0.36,9.3,0.07,-0.6,8.61,0.04,-0.6,8.63,0.06,-0.56,8.61,1.12,-0.36,8.45,1.12,-0.48,8.56,1,-0.6,8.53,0.93,-0.32,8.33,1.12,-0.36,8.45,1,-0.6,8.53,1,-0.76,8.9,1.04,-0.52,8.86,0.91,-0.44,9.11,0.39,-0.64,9.4,0.51,-1.04,9.28,0.85,-0.84,9.14,0.22,-0.92,9.38,0.18,-0.6,9.37,-0.03,-0.88,9.26,-0.11,-0.64,9.03,-0.02,-0.84,8.73,-0.14,-1,9.01,0.86,-0.64,8.48,0.9,-0.96,8.82,0.75,-0.72,8.49,0.75,-0.72,8.49,0.8,-0.68,8.44,0.86,-0.64,8.48,0.39,-0.64,9.4,0.18,-0.6,9.37,0.22,-0.92,9.38,0.39,-0.64,9.4,0.22,-0.92,9.38,0.51,-1.04,9.28,-0.11,-0.64,9.03,-0.14,-1,9.01,-0.03,-0.88,9.26,0.04,-0.6,8.63,0.02,-0.52,8.65,0.06,-0.56,8.61,1,-0.6,8.53,1.04,-0.52,8.86,1,-0.76,8.9,0.91,-0.44,9.11,0.61,-0.44,9.33,0.85,-0.84,9.14,0.75,-0.72,8.49,0.61,-0.92,8.55,0.59,-0.8,8.49,0.61,-0.44,9.33,0.39,-0.32,9.41,0.39,-0.64,9.4,0,-0.36,9.14,0.06,-0.08,9.09,0.09,-0.12,8.71,-0.08,-0.56,8.84,0.02,-0.52,8.65,0.04,-0.6,8.63,-0.11,-0.64,9.03,-0.08,-0.56,8.84,-0.02,-0.84,8.73,0.59,-0.8,8.49,0.61,-0.92,8.55,0.46,-0.84,8.51,0.61,-0.92,8.55,0.44,-0.96,8.52,0.46,-0.84,8.51,0.9,-0.96,8.82,1,-0.76,8.9,0.95,-0.84,9.02,1,-0.6,8.53,1,-0.76,8.9,0.9,-0.96,8.82,-0.14,-1,9.01,-0.16,-1.04,9.1,-0.03,-0.88,9.26,0.46,-0.84,8.51,0.44,-0.96,8.52,0.4,-0.92,8.51,0.59,-0.8,8.49,0.46,-0.84,8.51,0.45,-0.8,8.52,0.08,-0.88,8.66,-0.02,-0.84,8.73,0.04,-0.6,8.63,0.85,-0.84,9.14,0.9,-1.04,9.1,0.94,-0.96,9.01,0.17,-1.08,9.34,0.22,-0.92,9.38,-0.03,-0.88,9.26,0,-0.36,9.14,-0.11,-0.64,9.03,0.18,-0.6,9.37,-0.02,-0.84,8.73,-0.15,-1,8.78,-0.14,-1,9.01,-0.13,-1.04,8.64,-0.15,-1,8.78,-0.02,-0.84,8.73,0.9,-0.96,8.82,0.95,-0.84,9.02,0.94,-0.96,9.01,-0.01,-1.04,8.59,-0.13,-1.04,8.64,-0.02,-0.84,8.73,0.7,-1.12,8.89,0.6,-1.24,8.89,0.51,-1.24,8.8,-0.03,-0.88,9.26,-0.1,-1.04,9.24,-0.08,-1.08,9.3,-0.21,-1.04,8.69,-0.11,-1.2,8.58,-0.26,-1.16,8.8,0.08,-0.88,8.66,0.15,-1,8.64,0.11,-1,8.64,0.08,-0.88,8.66,0.11,-1,8.64,-0.01,-1.04,8.59,0.44,-0.96,8.52,0.47,-1.16,8.72,0.36,-1.12,8.58,0.95,-0.84,9.02,0.85,-0.84,9.14,0.94,-0.96,9.01,0.17,-1.08,9.34,-0.03,-0.88,9.26,-0.08,-1.08,9.3,-0.1,-1.04,9.24,-0.13,-1.08,9.3,-0.08,-1.08,9.3,-0.18,-1.04,9,-0.16,-1.04,9.1,-0.14,-1,9.01,-0.15,-1,8.78,-0.21,-1.04,8.69,-0.25,-1.04,8.77,-0.21,-1.04,8.69,-0.15,-1,8.78,-0.13,-1.04,8.64,-0.25,-1.04,8.77,-0.21,-1.04,8.69,-0.26,-1.16,8.8,0.7,-1.12,8.89,0.83,-1.2,9.09,0.75,-1.32,9,0.51,-1.04,9.28,0.22,-0.92,9.38,0.26,-1.12,9.34,-0.16,-1.04,9.1,-0.26,-1.08,9.13,-0.1,-1.04,9.24,-0.16,-1.04,9.1,-0.1,-1.04,9.24,-0.03,-0.88,9.26,-0.25,-1.04,8.77,-0.26,-1.16,8.8,-0.31,-1.08,8.91,-0.02,-0.84,8.73,0.08,-0.88,8.66,-0.01,-1.04,8.59,-0.01,-1.04,8.59,0.11,-1,8.64,0.11,-1.04,8.57,0.11,-1.04,8.57,0.08,-1.16,8.59,0.04,-1.12,8.63,0.36,-1.12,8.58,0.47,-1.16,8.72,0.39,-1.2,8.71,0.61,-0.92,8.55,0.47,-1.16,8.72,0.44,-0.96,8.52,0.26,-1.12,9.34,0.17,-1.08,9.34,0.17,-1.12,9.39,0.22,-0.92,9.38,0.17,-1.08,9.34,0.26,-1.12,9.34,0.15,-1.12,9.42,0.17,-1.12,9.39,0.17,-1.08,9.34,-0.1,-1.56,9.35,-0.02,-1.28,9.4,-0.14,-1.36,9.2,-0.13,-1.08,9.3,-0.23,-1.16,9.3,-0.14,-1.2,9.38,-0.13,-1.08,9.3,-0.1,-1.04,9.24,-0.26,-1.08,9.13,-0.23,-1.16,9.3,-0.13,-1.08,9.3,-0.26,-1.08,9.13,-0.29,-1.16,8.97,-0.3,-1.08,9.01,-0.31,-1.08,8.91,-0.3,-1.08,9.01,-0.27,-1.04,8.92,-0.31,-1.08,8.91,-0.29,-1.16,8.97,-0.31,-1.08,8.91,-0.26,-1.16,8.8,-0.25,-1.04,8.77,-0.31,-1.08,8.91,-0.27,-1.04,8.92,0,-1.12,8.63,-0.01,-1.04,8.59,0.04,-1.12,8.63,0.08,-1.16,8.59,0.11,-1.04,8.57,0.18,-1.08,8.54,0.2,-1.16,8.6,0.08,-1.16,8.59,0.2,-1.12,8.57,0.7,-1.12,8.89,0.51,-1.24,8.8,0.47,-1.16,8.72,0.9,-1.04,9.1,0.85,-0.84,9.14,0.51,-1.04,9.28,0.14,-1.2,9.55,0.25,-1.16,9.46,0.15,-1.12,9.42,0.06,-1.12,9.5,0.14,-1.2,9.55,0.15,-1.12,9.42,-0.12,-1.12,9.4,-0.13,-1.08,9.3,-0.14,-1.2,9.38,-0.11,-1.2,8.58,-0.13,-1.04,8.64,0,-1.12,8.63,-0.21,-1.04,8.69,-0.13,-1.04,8.64,-0.11,-1.2,8.58,0,-1.12,8.63,-0.13,-1.04,8.64,-0.01,-1.04,8.59,0,-1.12,8.63,0.04,-1.12,8.63,0.01,-1.16,8.56,0.08,-1.16,8.59,0.01,-1.16,8.56,0.04,-1.12,8.63,0.08,-1.16,8.59,0.18,-1.08,8.54,0.2,-1.12,8.57,-0.01,-1.04,8.59,0.11,-1.04,8.57,0.04,-1.12,8.63,0.28,-1.2,8.63,0.29,-1.16,8.59,0.36,-1.12,8.58,0.47,-1.16,8.72,0.51,-1.24,8.8,0.44,-1.24,8.74,0.7,-1.12,8.89,0.47,-1.16,8.72,0.61,-0.92,8.55,0.79,-1.2,9.2,0.83,-1.2,9.09,0.9,-1.04,9.1,0.44,-1.2,9.46,0.54,-1.24,9.43,0.51,-1.04,9.28,0.51,-1.04,9.28,0.26,-1.12,9.34,0.44,-1.2,9.46,0.25,-1.16,9.46,0.44,-1.2,9.46,0.26,-1.12,9.34,0.25,-1.16,9.46,0.17,-1.12,9.39,0.15,-1.12,9.42,-0.12,-1.12,9.4,-0.14,-1.2,9.38,-0.02,-1.28,9.4,-0.23,-1.16,9.3,-0.26,-1.08,9.13,-0.17,-1.28,9.11,-0.26,-1.08,9.13,-0.3,-1.08,9.01,-0.29,-1.16,8.97,-0.17,-1.24,8.84,-0.26,-1.16,8.8,-0.11,-1.2,8.58,0.01,-1.16,8.56,-0.11,-1.2,8.58,0,-1.12,8.63,0.01,-1.16,8.56,0.03,-1.28,8.5,-0.11,-1.2,8.58,0.37,-1.24,8.61,0.28,-1.2,8.63,0.36,-1.12,8.58,0.44,-1.24,8.67,0.39,-1.2,8.71,0.44,-1.24,8.74,0.39,-1.2,8.71,0.47,-1.16,8.72,0.44,-1.24,8.74,0.57,-1.28,8.72,0.51,-1.24,8.8,0.6,-1.24,8.89,0.7,-1.12,8.89,0.9,-0.96,8.82,0.94,-0.96,9.01,0.75,-1.32,9,0.83,-1.2,9.09,0.79,-1.2,9.2,0.54,-1.24,9.43,0.65,-1.28,9.33,0.51,-1.04,9.28,0.65,-1.28,9.33,0.79,-1.2,9.2,0.51,-1.04,9.28,-0.29,-1.16,8.97,-0.26,-1.16,8.8,-0.17,-1.24,8.84,-0.05,-1.32,8.63,-0.14,-1.4,8.63,-0.23,-1.36,8.75,-0.17,-1.24,8.84,-0.11,-1.2,8.58,-0.23,-1.36,8.75,-0.11,-1.2,8.58,-0.05,-1.32,8.63,-0.23,-1.36,8.75,0.39,-1.2,8.71,0.37,-1.24,8.61,0.36,-1.12,8.58,0.44,-1.24,8.67,0.37,-1.24,8.61,0.39,-1.2,8.71,0.6,-1.24,8.89,0.7,-1.12,8.89,0.75,-1.32,9,0.9,-0.96,8.82,0.7,-1.12,8.89,0.61,-0.92,8.55,0.67,-1.32,8.84,0.6,-1.24,8.89,0.75,-1.32,9,0.79,-1.2,9.2,0.65,-1.28,9.33,0.6,-1.4,9.24,0.79,-1.2,9.2,0.9,-1.04,9.1,0.51,-1.04,9.28,0.44,-1.2,9.46,0.4,-1.36,9.42,0.54,-1.24,9.43,-0.29,-1.16,8.97,-0.17,-1.28,9.11,-0.26,-1.08,9.13,0.06,-1.28,8.48,0.03,-1.28,8.5,0.03,-1.2,8.5,0.03,-1.28,8.5,-0.05,-1.32,8.63,-0.11,-1.2,8.58,0.36,-1.36,8.57,0.4,-1.44,8.59,0.33,-1.44,8.56,0.37,-1.24,8.61,0.44,-1.24,8.67,0.36,-1.36,8.57,0.44,-1.24,8.67,0.49,-1.36,8.67,0.36,-1.36,8.57,0.57,-1.28,8.72,0.6,-1.24,8.89,0.67,-1.32,8.84,0.83,-1.2,9.09,0.7,-1.12,8.89,0.9,-1.04,9.1,0.7,-1.12,8.89,0.94,-0.96,9.01,0.9,-1.04,9.1,0.28,-1.28,9.54,0.4,-1.36,9.42,0.44,-1.2,9.46,0.28,-1.28,9.54,0.25,-1.16,9.46,0.14,-1.2,9.55,0.12,-1.56,9.49,0.14,-1.2,9.55,-0.02,-1.28,9.4,-0.29,-1.52,8.98,-0.25,-1.56,9.09,-0.24,-1.44,9.16,0.01,-1.16,8.56,0.03,-1.2,8.5,0.03,-1.28,8.5,0.57,-1.28,8.72,0.49,-1.36,8.67,0.44,-1.24,8.67,0.57,-1.28,8.72,0.54,-1.36,8.71,0.49,-1.36,8.67,0.56,-1.4,8.8,0.54,-1.36,8.71,0.57,-1.28,8.72,0.75,-1.32,9,0.68,-1.4,9.01,0.66,-1.4,8.88,0.75,-1.32,9,0.79,-1.2,9.2,0.6,-1.4,9.24,0.56,-1.4,9.28,0.6,-1.4,9.24,0.65,-1.28,9.33,0.4,-1.36,9.42,0.55,-1.36,9.35,0.54,-1.24,9.43,0.28,-1.28,9.54,0.44,-1.2,9.46,0.25,-1.16,9.46,-0.02,-1.28,9.4,0.14,-1.2,9.55,0.06,-1.12,9.5,0.06,-1.12,9.5,-0.12,-1.12,9.4,-0.02,-1.28,9.4,-0.23,-1.16,9.3,-0.14,-1.36,9.2,-0.14,-1.2,9.38,-0.17,-1.28,9.11,-0.24,-1.44,9.16,-0.14,-1.36,9.2,0.37,-1.24,8.61,0.36,-1.36,8.57,0.33,-1.32,8.56,0.56,-1.4,8.8,0.51,-1.4,8.8,0.54,-1.36,8.71,0.56,-1.4,8.8,0.57,-1.28,8.72,0.67,-1.32,8.84,0.66,-1.4,8.88,0.56,-1.4,8.8,0.67,-1.32,8.84,0.75,-1.32,9,0.66,-1.4,8.88,0.67,-1.32,8.84,0.68,-1.4,9.01,0.75,-1.32,9,0.6,-1.4,9.24,0.55,-1.36,9.35,0.56,-1.4,9.28,0.65,-1.28,9.33,0.55,-1.36,9.35,0.65,-1.28,9.33,0.54,-1.24,9.43,0.49,-1.4,9.27,0.56,-1.4,9.28,0.55,-1.36,9.35,0.35,-1.4,9.34,0.48,-1.6,9.26,0.45,-1.44,9.04,0.12,-1.56,9.49,-0.02,-1.28,9.4,-0.1,-1.56,9.35,0.12,-1.56,9.49,0.28,-1.28,9.54,0.14,-1.2,9.55,-0.23,-1.16,9.3,-0.17,-1.28,9.11,-0.14,-1.36,9.2,-0.29,-1.16,8.97,-0.17,-1.24,8.84,-0.17,-1.28,9.11,-0.25,-1.4,8.74,-0.27,-1.4,8.76,-0.23,-1.36,8.75,-0.25,-1.4,8.74,-0.23,-1.36,8.75,-0.14,-1.4,8.63,-0.25,-1.4,8.74,-0.14,-1.4,8.63,-0.2,-1.52,8.74,0.05,-1.36,8.52,0.03,-1.4,8.54,-0.05,-1.32,8.63,0.03,-1.28,8.5,0.05,-1.36,8.52,-0.05,-1.32,8.63,0.06,-1.4,8.53,0.03,-1.4,8.54,0.05,-1.36,8.52,0.37,-1.48,8.57,0.4,-1.44,8.59,0.43,-1.52,8.64,0.49,-1.36,8.67,0.4,-1.44,8.59,0.36,-1.36,8.57,0.42,-1.4,8.75,0.41,-1.4,8.8,0.42,-1.44,8.79,0.42,-1.44,8.79,0.45,-1.44,8.88,0.52,-1.56,8.9,0.4,-1.36,9.42,0.28,-1.28,9.54,0.27,-1.52,9.47,-0.24,-1.44,9.16,-0.2,-1.56,9.21,-0.14,-1.36,9.2,-0.24,-1.44,9.16,-0.25,-1.56,9.09,-0.2,-1.56,9.21,-0.17,-1.24,8.84,-0.31,-1.4,8.88,-0.17,-1.28,9.11,-0.23,-1.36,8.75,-0.27,-1.4,8.76,-0.31,-1.4,8.88,-0.27,-1.4,8.76,-0.25,-1.4,8.74,-0.26,-1.44,8.77,-0.14,-1.4,8.63,-0.05,-1.32,8.63,0.03,-1.4,8.54,-0.23,-1.36,8.75,-0.31,-1.4,8.88,-0.17,-1.24,8.84,-0.14,-1.4,8.63,0.03,-1.4,8.54,-0.03,-1.64,8.61,0.37,-1.48,8.57,0.33,-1.44,8.56,0.4,-1.44,8.59,0.37,-1.48,8.57,0.43,-1.52,8.64,0.24,-1.64,8.7,0.49,-1.36,8.67,0.42,-1.4,8.75,0.4,-1.44,8.59,0.42,-1.4,8.75,0.43,-1.52,8.64,0.4,-1.44,8.59,0.45,-1.44,8.88,0.42,-1.44,8.79,0.41,-1.4,8.8,0.35,-1.4,9.34,0.4,-1.36,9.42,0.27,-1.52,9.47,0.25,-1.64,9.47,0.32,-1.6,9.43,0.27,-1.52,9.47,-0.25,-1.4,8.74,-0.2,-1.52,8.74,-0.26,-1.44,8.77,-0.2,-1.52,8.74,-0.14,-1.4,8.63,-0.03,-1.64,8.61,0.43,-1.52,8.64,0.42,-1.44,8.79,0.47,-1.56,8.72,0.43,-1.52,8.64,0.42,-1.4,8.75,0.42,-1.44,8.79,0.42,-1.44,8.79,0.52,-1.56,8.9,0.47,-1.56,8.72,0.52,-1.56,8.9,0.45,-1.44,9.04,0.48,-1.6,9.26,0.52,-1.56,8.9,0.45,-1.44,8.88,0.45,-1.44,9.04,-0.26,-1.44,8.77,-0.29,-1.52,8.98,-0.31,-1.4,8.88,-0.2,-1.52,8.74,-0.03,-1.64,8.61,-0.18,-1.68,8.6,0.47,-1.56,8.72,0.52,-1.56,8.9,0.46,-1.68,8.84,0.35,-1.4,9.34,0.32,-1.6,9.43,0.41,-1.6,9.36,0.33,-1.76,9.25,0.48,-1.6,9.26,0.41,-1.6,9.36,0.35,-1.4,9.34,0.41,-1.6,9.36,0.48,-1.6,9.26,0.12,-1.56,9.49,0.27,-1.52,9.47,0.28,-1.28,9.54,-0.2,-1.56,9.21,-0.15,-1.64,9.21,-0.1,-1.56,9.35,-0.31,-1.4,8.88,-0.29,-1.52,8.98,-0.17,-1.28,9.11,-0.31,-1.4,8.88,-0.27,-1.4,8.76,-0.26,-1.44,8.77,0.03,-1.4,8.54,0.17,-1.64,8.66,-0.03,-1.64,8.61,0.24,-1.64,8.7,0.47,-1.56,8.72,0.46,-1.68,8.84,0.24,-1.64,8.7,0.43,-1.52,8.64,0.47,-1.56,8.72,0.49,-1.72,9.14,0.43,-1.88,9.08,0.46,-1.68,8.84,0.41,-1.6,9.36,0.32,-1.6,9.43,0.33,-1.68,9.4,0.12,-1.56,9.49,-0.1,-1.56,9.35,0.05,-1.68,9.32,-0.2,-1.56,9.21,-0.17,-1.64,9.18,-0.15,-1.64,9.21,0.25,-1.64,9.47,0.27,-1.52,9.47,0.12,-1.56,9.49,0.25,-1.64,9.47,0.12,-1.56,9.49,0.05,-1.68,9.32,-0.14,-1.36,9.2,-0.02,-1.28,9.4,-0.14,-1.2,9.38,-0.2,-1.56,9.21,-0.1,-1.56,9.35,-0.14,-1.36,9.2,0.23,-1.76,9.28,0.33,-1.76,9.25,0.33,-1.68,9.4,0.16,-1.72,8.68,0.15,-1.68,8.69,0.24,-1.64,8.7,0.49,-1.72,9.14,0.52,-1.56,8.9,0.48,-1.6,9.26,0.35,-1.4,9.34,0.27,-1.52,9.47,0.32,-1.6,9.43,-0.25,-1.56,9.09,-0.17,-1.64,9.18,-0.2,-1.56,9.21,-0.29,-1.52,8.98,-0.24,-1.44,9.16,-0.17,-1.28,9.11,0.16,-1.72,8.68,0.24,-1.64,8.7,0.24,-1.76,8.74,0.33,-1.76,9.25,0.49,-1.72,9.14,0.48,-1.6,9.26,0.33,-1.76,9.25,0.41,-1.6,9.36,0.33,-1.68,9.4,-0.15,-1.64,9.21,-0.08,-1.76,9.26,-0.1,-1.56,9.35,-0.26,-1.44,8.77,-0.2,-1.52,8.74,-0.29,-1.52,8.98,0.46,-1.68,8.84,0.24,-1.76,8.74,0.24,-1.64,8.7,0.23,-1.76,9.28,0.25,-1.64,9.47,0.05,-1.68,9.32,0.23,-1.76,9.28,0.33,-1.68,9.4,0.25,-1.64,9.47,-0.08,-1.76,9.26,0.05,-1.68,9.32,-0.1,-1.56,9.35,-0.25,-1.56,9.09,-0.2,-1.68,9.16,-0.17,-1.64,9.18,0.49,-1.72,9.14,0.46,-1.68,8.84,0.52,-1.56,8.9,0.24,-1.76,8.74,0.46,-1.68,8.84,0.43,-1.88,9.08,0.43,-1.88,9.08,0.49,-1.72,9.14,0.33,-1.76,9.25])

IndexedFaceSet434.setCoord(Coordinate435)

Shape430.setGeometry(IndexedFaceSet434)

Transform429.addChildren(Shape430)

fieldValue428.addChildren(Transform429)

ProtoInstance426.addFieldValue(fieldValue428)

fieldValue425.addChildren(ProtoInstance426)
ProtoInstance436 = ProtoInstance()
ProtoInstance436.setName("Joint")
ProtoInstance436.setDEF("Allen_hanim_l_wrist")
fieldValue437 = fieldValue()
fieldValue437.setName("name")
fieldValue437.setValue("l_wrist")

ProtoInstance436.addFieldValue(fieldValue437)
fieldValue438 = fieldValue()
fieldValue438.setName("center")
fieldValue438.setValue("0.213 0.811 -0.0338")

ProtoInstance436.addFieldValue(fieldValue438)
fieldValue439 = fieldValue()
fieldValue439.setName("children")
ProtoInstance440 = ProtoInstance()
ProtoInstance440.setName("Segment")
ProtoInstance440.setDEF("Allen_hanim_l_hand")
fieldValue441 = fieldValue()
fieldValue441.setName("name")
fieldValue441.setValue("l_hand")

ProtoInstance440.addFieldValue(fieldValue441)
fieldValue442 = fieldValue()
fieldValue442.setName("children")
Transform443 = Transform()
Transform443.setDEF("Allen_l_hand_adjust")
Transform443.setCenter([-0.8355,1.015,0.1])
Transform443.setRotation([0,1,0,1.570796])
Transform443.setScale([0.1,0.1,0.1])
Shape444 = Shape()
Appearance445 = Appearance()
Material446 = Material()
Material446.setUSE("Skin_Color")

Appearance445.setMaterial(Material446)

Shape444.setAppearance(Appearance445)
IndexedFaceSet447 = IndexedFaceSet()
IndexedFaceSet447.setCoordIndex([0,1,2,-1,3,4,5,-1,6,7,8,-1,9,10,11,-1,12,13,14,-1,15,16,17,-1,18,19,20,-1,21,22,23,-1,24,25,26,-1,27,28,29,-1,30,31,32,-1,33,34,35,-1,36,37,38,-1,39,40,41,-1,42,43,44,-1,45,46,47,-1,48,49,50,-1,51,52,53,-1,54,55,56,-1,57,58,59,-1,60,61,62,-1,63,64,65,-1,66,67,68,-1,69,70,71,-1,72,73,74,-1,75,76,77,-1,78,79,80,-1,81,82,83,-1,84,85,86,-1,87,88,89,-1,90,91,92,-1,93,94,95,-1,96,97,98,-1,99,100,101,-1,102,103,104,-1,105,106,107,-1,108,109,110,-1,111,112,113,-1,114,115,116,-1,117,118,119,-1,120,121,122,-1,123,124,125,-1,126,127,128,-1,129,130,131,-1,132,133,134,-1,135,136,137,-1,138,139,140,-1,141,142,143,-1,144,145,146,-1,147,148,149,-1,150,151,152,-1,153,154,155,-1,156,157,158,-1,159,160,161,-1,162,163,164,-1,165,166,167,-1,168,169,170,-1,171,172,173,-1,174,175,176,-1,177,178,179,-1,180,181,182,-1,183,184,185,-1,186,187,188,-1,189,190,191,-1,192,193,194,-1,195,196,197,-1,198,199,200,-1,201,202,203,-1,204,205,206,-1,207,208,209,-1,210,211,212,-1,213,214,215,-1,216,217,218,-1,219,220,221,-1,222,223,224,-1,225,226,227,-1,228,229,230,-1,231,232,233,-1,234,235,236,-1,237,238,239,-1,240,241,242,-1,243,244,245,-1,246,247,248,-1,249,250,251,-1,252,253,254,-1,255,256,257,-1,258,259,260,-1,261,262,263,-1,264,265,266,-1,267,268,269,-1,270,271,272,-1,273,274,275,-1,276,277,278,-1,279,280,281,-1,282,283,284,-1,285,286,287,-1,288,289,290,-1,291,292,293,-1,294,295,296,-1,297,298,299,-1,300,301,302,-1,303,304,305,-1,306,307,308,-1,309,310,311,-1,312,313,314,-1,315,316,317,-1,318,319,320,-1,321,322,323,-1,324,325,326,-1,327,328,329,-1,330,331,332,-1,333,334,335,-1,336,337,338,-1,339,340,341,-1,342,343,344,-1,345,346,347,-1,348,349,350,-1,351,352,353,-1,354,355,356,-1,357,358,359,-1,360,361,362,-1,363,364,365,-1,366,367,368,-1,369,370,371,-1,372,373,374,-1,375,376,377,-1,378,379,380,-1,381,382,383,-1,384,385,386,-1,387,388,389,-1,390,391,392,-1,393,394,395,-1,396,397,398,-1,399,400,401,-1,402,403,404,-1,405,406,407,-1,408,409,410,-1,411,412,413,-1,414,415,416,-1,417,418,419,-1,420,421,422,-1,423,424,425,-1,426,427,428,-1,429,430,431,-1,432,433,434,-1,435,436,437,-1,438,439,440,-1,441,442,443,-1,444,445,446,-1,447,448,449,-1,450,451,452,-1,453,454,455,-1,456,457,458,-1,459,460,461,-1,462,463,464,-1,465,466,467,-1,468,469,470,-1,471,472,473,-1,474,475,476,-1,477,478,479,-1,480,481,482,-1,483,484,485,-1,486,487,488,-1,489,490,491,-1,492,493,494,-1,495,496,497,-1,498,499,500,-1,501,502,503,-1,504,505,506,-1,507,508,509,-1,510,511,512,-1,513,514,515,-1,516,517,518,-1,519,520,521,-1,522,523,524,-1,525,526,527,-1,528,529,530,-1,531,532,533,-1,534,535,536,-1,537,538,539,-1,540,541,542,-1,543,544,545,-1,546,547,548,-1,549,550,551,-1,552,553,554,-1,555,556,557,-1,558,559,560,-1,561,562,563,-1,564,565,566,-1,567,568,569,-1,570,571,572,-1,573,574,575,-1,576,577,578,-1,579,580,581,-1,582,583,584,-1,585,586,587,-1,588,589,590,-1,591,592,593,-1,594,595,596,-1,597,598,599,-1,600,601,602,-1,603,604,605,-1,606,607,608,-1,609,610,611,-1,612,613,614,-1,615,616,617,-1,618,619,620,-1,621,622,623,-1,624,625,626,-1,627,628,629,-1,630,631,632,-1,633,634,635,-1,636,637,638,-1,639,640,641,-1,642,643,644,-1,645,646,647,-1,648,649,650,-1,651,652,653,-1,654,655,656,-1,657,658,659,-1,660,661,662,-1,663,664,665,-1,666,667,668,-1,669,670,671,-1])
IndexedFaceSet447.setCreaseAngle(1.48)
Coordinate448 = Coordinate()
Coordinate448.setPoint([-0.18,-1.68,10.63,-0.3,-1.68,10.77,-0.2,-1.52,10.78,-0.25,-1.56,11.13,-0.29,-1.52,11.02,-0.3,-1.72,11.09,-0.3,-1.68,10.77,-0.18,-1.68,10.63,-0.26,-1.84,10.61,-0.29,-1.52,11.02,-0.3,-1.68,10.77,-0.3,-1.72,11.09,-0.03,-1.72,10.57,-0.1,-1.84,10.59,-0.18,-1.68,10.63,0.24,-1.76,10.78,0.23,-1.92,10.85,0.15,-1.8,10.73,0.23,-1.76,11.32,0.05,-1.68,11.36,0.12,-1.84,11.38,-0.2,-1.68,11.2,-0.18,-1.68,11.22,-0.17,-1.64,11.22,-0.2,-1.68,11.2,-0.25,-1.56,11.13,-0.3,-1.72,11.09,-0.18,-1.68,11.22,-0.15,-1.64,11.24,-0.17,-1.64,11.22,-0.2,-1.72,11.21,-0.2,-1.68,11.2,-0.3,-1.72,11.09,-0.45,-1.96,10.81,-0.3,-1.68,10.77,-0.26,-1.84,10.61,0.15,-1.8,10.73,0.12,-1.76,10.71,0.16,-1.72,10.72,-0.15,-1.64,11.24,-0.18,-1.68,11.22,-0.08,-1.76,11.3,-0.2,-1.72,11.21,-0.18,-1.68,11.22,-0.2,-1.68,11.2,-0.18,-1.68,10.63,-0.1,-1.84,10.59,-0.26,-1.84,10.61,-0.13,-1.88,10.56,-0.22,-1.92,10.56,-0.26,-1.84,10.61,0.15,-1.8,10.73,0.16,-1.72,10.72,0.24,-1.76,10.78,0.23,-1.76,11.32,0.29,-1.88,11.33,0.33,-1.76,11.29,-0.08,-1.76,11.3,-0.18,-1.68,11.22,-0.2,-1.72,11.21,-0.08,-1.76,11.3,-0.35,-1.96,11.12,-0.04,-1.92,11.31,-0.2,-1.72,11.21,-0.3,-1.72,11.09,-0.35,-1.96,11.12,0.07,-1.8,10.61,-0.02,-1.8,10.62,-0.03,-1.72,10.57,-0.35,-2.08,11.2,-0.09,-2.2,11.35,-0.04,-1.92,11.31,-0.08,-1.76,11.3,-0.2,-1.72,11.21,-0.35,-1.96,11.12,-0.26,-1.84,10.61,-0.1,-1.84,10.59,-0.13,-1.88,10.56,-0.02,-1.8,10.62,-0.1,-1.84,10.59,-0.03,-1.72,10.57,0,-1.84,10.64,-0.1,-1.84,10.59,-0.02,-1.8,10.62,0.13,-1.88,11.39,0.12,-1.84,11.38,0,-1.88,11.36,0.13,-1.88,11.39,0,-1.88,11.36,0.06,-1.96,11.35,0.13,-1.88,10.74,0.1,-1.84,10.67,0.15,-1.8,10.73,0.23,-1.92,10.85,0.1,-1.92,10.83,0.13,-1.88,10.74,0.29,-1.96,11.33,0.32,-2.12,11.27,0.39,-2,11.21,0.13,-1.88,11.39,0.15,-1.88,11.39,0.12,-1.84,11.38,0.12,-1.84,11.38,0.05,-1.68,11.36,0,-1.88,11.36,-0.08,-1.76,11.3,-0.04,-1.92,11.31,0,-1.88,11.36,-0.45,-1.96,10.81,-0.26,-1.84,10.61,-0.41,-2,10.64,-0.2,-1.52,10.78,-0.3,-1.68,10.77,-0.29,-1.52,11.02,-0.03,-1.72,10.57,-0.18,-1.68,10.63,-0.03,-1.64,10.65,-0.07,-1.88,10.57,-0.13,-1.88,10.56,-0.1,-1.84,10.59,0.13,-1.88,10.74,0.1,-1.92,10.83,0.04,-1.96,10.77,0.23,-1.92,10.85,0.24,-1.76,10.78,0.43,-1.88,11.12,0.23,-1.92,10.85,0.13,-1.88,10.74,0.15,-1.8,10.73,0.2,-1.96,10.95,0.23,-1.92,10.85,0.43,-1.88,11.12,0.29,-1.88,11.33,0.39,-2,11.21,0.33,-1.76,11.29,0.15,-1.88,11.39,0.13,-1.88,11.39,0.14,-1.92,11.4,0.14,-1.92,11.4,0.17,-2.04,11.36,0.24,-2,11.33,0.14,-1.92,11.4,0.13,-1.88,11.39,0.06,-1.96,11.35,-0.08,-1.76,11.3,0,-1.88,11.36,0.05,-1.68,11.36,-0.35,-2.08,11.2,-0.26,-2.28,11.28,-0.09,-2.2,11.35,-0.35,-2.08,11.2,-0.49,-2.08,10.96,-0.45,-2.2,11.16,0.23,-2.12,10.96,0.17,-2.28,10.86,0.02,-2.2,10.86,0.26,-1.96,11.35,0.29,-1.96,11.33,0.29,-1.88,11.33,0.12,-1.84,11.38,0.15,-1.88,11.39,0.23,-1.76,11.32,0.17,-2.04,11.36,0.21,-2.08,11.35,0.24,-2,11.33,0.15,-1.88,11.39,0.26,-1.96,11.35,0.29,-1.88,11.33,-0.04,-1.92,11.31,0.06,-1.96,11.35,0,-1.88,11.36,0.06,-1.96,11.35,-0.04,-1.92,11.31,-0.09,-2.2,11.35,-0.3,-1.68,10.77,-0.45,-1.96,10.81,-0.3,-1.72,11.09,-0.49,-2.08,10.96,-0.45,-1.96,10.81,-0.44,-2.32,10.79,-0.22,-1.92,10.56,-0.28,-2.12,10.56,-0.41,-2,10.64,0.07,-2,10.75,0.02,-2,10.68,0.04,-1.96,10.77,0.05,-2,10.8,0.07,-2,10.75,0.04,-1.96,10.77,0.1,-1.92,10.83,0.05,-2,10.8,0.04,-1.96,10.77,0.39,-2,11.21,0.43,-1.88,11.12,0.33,-1.76,11.29,0.15,-1.88,11.39,0.14,-1.92,11.4,0.26,-1.96,11.35,-0.1,-2,10.55,-0.13,-2,10.56,-0.13,-1.88,10.56,0.07,-2,10.75,0.05,-2,10.8,0.01,-2.04,10.78,0.01,-2.04,10.78,-0.05,-2.08,10.9,-0.12,-2.12,10.88,-0.12,-2.12,10.88,-0.05,-2.08,10.9,0.02,-2.2,10.86,0.08,-1.96,10.96,0.05,-2.04,10.98,0,-2.04,10.94,0.23,-2.12,10.96,0.2,-1.96,10.95,0.39,-2,11.21,0.24,-2,11.33,0.29,-1.96,11.33,0.26,-1.96,11.35,0.15,-1.88,11.39,0.29,-1.88,11.33,0.23,-1.76,11.32,-0.35,-2.08,11.2,-0.35,-1.96,11.12,-0.49,-2.08,10.96,-0.22,-1.92,10.56,-0.16,-2.08,10.58,-0.28,-2.12,10.56,-0.13,-2,10.56,-0.22,-1.92,10.56,-0.13,-1.88,10.56,0.06,-1.96,11.35,0.11,-2.08,11.39,0.17,-2.04,11.36,0.11,-2.08,11.39,0.06,-1.96,11.35,-0.09,-2.2,11.35,-0.45,-2.2,11.16,-0.49,-2.08,10.96,-0.54,-2.24,10.97,-0.41,-2,10.64,-0.38,-2.16,10.55,-0.49,-2.2,10.62,-0.45,-1.96,10.81,-0.49,-2.2,10.62,-0.44,-2.32,10.79,-0.13,-2.08,10.56,-0.16,-2.08,10.58,-0.13,-2,10.56,0.01,-2.04,10.78,0.05,-2,10.8,0,-2.04,10.94,0.08,-1.96,10.96,0.05,-2,10.8,0.1,-1.92,10.83,0.08,-1.96,10.96,0,-2.04,10.94,0.05,-2,10.8,0.29,-1.88,11.33,0.29,-1.96,11.33,0.39,-2,11.21,0.29,-1.96,11.33,0.24,-2,11.33,0.32,-2.12,11.27,0.17,-2.04,11.36,0.18,-2.08,11.36,0.21,-2.08,11.35,0.24,-2,11.33,0.26,-1.96,11.35,0.14,-1.92,11.4,-0.05,-2.08,10.9,0.01,-2.04,10.78,0,-2.04,10.94,0.24,-2.16,11.07,0.23,-2.12,10.96,0.39,-2,11.21,-0.35,-1.96,11.12,-0.35,-2.08,11.2,-0.04,-1.92,11.31,-0.35,-2.08,11.2,-0.45,-2.2,11.16,-0.26,-2.28,11.28,-0.45,-1.96,10.81,-0.41,-2,10.64,-0.49,-2.2,10.62,-0.28,-2.12,10.56,-0.3,-2.16,10.54,-0.38,-2.16,10.55,-0.28,-2.12,10.56,-0.16,-2.08,10.58,-0.15,-2.12,10.58,-0.22,-1.92,10.56,-0.13,-2,10.56,-0.16,-2.08,10.58,-0.15,-2.16,10.87,0.02,-2.2,10.86,-0.04,-2.32,10.75,-0.12,-2.12,10.88,0.02,-2.2,10.86,-0.15,-2.16,10.87,0.05,-2.04,10.98,0.08,-1.96,10.96,0.2,-1.96,10.95,0.05,-2.04,10.98,0.02,-2.2,10.86,0,-2.04,10.94,0.24,-2.16,11.07,0.39,-2,11.21,0.32,-2.12,11.27,0.24,-2,11.33,0.21,-2.08,11.35,0.32,-2.12,11.27,0.21,-2.08,11.35,0.22,-2.12,11.35,0.32,-2.12,11.27,0.11,-2.08,11.39,-0.09,-2.2,11.35,0.02,-2.24,11.38,0.13,-2.2,11.41,0.02,-2.24,11.38,0.13,-2.4,11.21,-0.26,-1.84,10.61,-0.22,-1.92,10.56,-0.41,-2,10.64,-0.28,-2.12,10.56,-0.38,-2.16,10.55,-0.41,-2,10.64,0.02,-2.2,10.86,-0.05,-2.08,10.9,0,-2.04,10.94,0.3,-2.2,10.98,0.31,-2.28,10.95,0.17,-2.28,10.86,0.23,-2.12,10.96,0.02,-2.2,10.86,0.05,-2.04,10.98,0.27,-2.44,10.98,0.31,-2.28,10.95,0.36,-2.36,11.07,0.2,-1.96,10.95,0.43,-1.88,11.12,0.39,-2,11.21,0.32,-2.12,11.27,0.3,-2.2,11.29,0.24,-2.16,11.07,0.32,-2.12,11.27,0.22,-2.12,11.35,0.3,-2.2,11.29,0.13,-2.2,11.41,0.11,-2.08,11.39,0.02,-2.24,11.38,0.14,-1.92,11.4,0.06,-1.96,11.35,0.17,-2.04,11.36,0.02,-2.24,11.38,-0.09,-2.2,11.35,-0.06,-2.4,11.26,-0.35,-1.96,11.12,-0.3,-1.72,11.09,-0.45,-1.96,10.81,-0.49,-2.08,10.96,-0.35,-1.96,11.12,-0.45,-1.96,10.81,0.02,-2.2,10.86,0.17,-2.28,10.86,-0.04,-2.32,10.75,0.24,-2.16,11.07,0.3,-2.2,10.98,0.23,-2.12,10.96,0.13,-2.2,11.41,0.22,-2.12,11.35,0.11,-2.08,11.39,-0.45,-2.2,11.16,-0.54,-2.24,10.97,-0.53,-2.32,11.03,-0.45,-2.28,10.53,-0.53,-2.36,10.65,-0.49,-2.2,10.62,0.27,-2.44,10.98,0.18,-2.44,10.89,0.31,-2.28,10.95,0.23,-2.12,10.96,0.05,-2.04,10.98,0.2,-1.96,10.95,0.3,-2.2,11.29,0.29,-2.28,11.26,0.24,-2.16,11.07,0.3,-2.2,11.29,0.22,-2.12,11.35,0.13,-2.2,11.41,-0.46,-2.32,11.17,-0.45,-2.2,11.16,-0.53,-2.32,11.03,-0.34,-2.52,10.58,-0.37,-2.6,10.59,-0.41,-2.6,10.68,-0.37,-2.28,10.55,-0.45,-2.28,10.53,-0.38,-2.16,10.55,-0.45,-2.28,10.53,-0.49,-2.2,10.62,-0.38,-2.16,10.55,-0.06,-2.4,10.7,-0.06,-2.36,10.7,-0.04,-2.32,10.75,0.23,-2.12,10.96,0.3,-2.2,10.98,0.17,-2.28,10.86,0.35,-2.32,11.11,0.3,-2.2,10.98,0.24,-2.16,11.07,0.02,-2.24,11.38,-0.06,-2.4,11.26,0.13,-2.4,11.21,-0.54,-2.24,10.97,-0.49,-2.08,10.96,-0.44,-2.32,10.79,-0.46,-2.32,11.17,-0.28,-2.36,11.26,-0.45,-2.2,11.16,-0.48,-2.52,10.95,-0.44,-2.32,10.79,-0.41,-2.6,10.68,-0.48,-2.52,10.95,-0.53,-2.32,11.03,-0.44,-2.32,10.79,-0.45,-2.44,10.57,-0.53,-2.36,10.65,-0.45,-2.28,10.53,0.35,-2.32,11.11,0.31,-2.28,10.95,0.3,-2.2,10.98,0.13,-2.4,11.21,-0.06,-2.4,11.26,0.06,-2.52,11.21,0.29,-2.28,11.26,0.3,-2.2,11.29,0.13,-2.2,11.41,-0.26,-2.28,11.28,-0.28,-2.36,11.26,-0.06,-2.4,11.26,-0.53,-2.32,11.03,-0.48,-2.52,10.95,-0.46,-2.32,11.17,-0.45,-2.44,10.57,-0.45,-2.28,10.53,-0.41,-2.4,10.53,-0.15,-2.36,10.66,-0.06,-2.36,10.7,-0.15,-2.4,10.66,-0.06,-2.4,10.7,-0.15,-2.4,10.66,-0.06,-2.36,10.7,0.01,-2.44,10.76,-0.06,-2.4,10.7,-0.04,-2.32,10.75,0.35,-2.32,11.11,0.24,-2.16,11.07,0.29,-2.28,11.26,0.27,-2.4,11.2,0.29,-2.28,11.26,0.13,-2.2,11.41,0.15,-2.4,10.84,0.01,-2.44,10.76,-0.04,-2.32,10.75,0.18,-2.44,10.89,0.15,-2.4,10.84,0.17,-2.28,10.86,0.27,-2.44,10.98,0.36,-2.36,11.07,0.27,-2.4,11.2,0.35,-2.32,11.11,0.36,-2.36,11.07,0.31,-2.28,10.95,0.18,-2.44,10.89,0.27,-2.44,10.98,0.21,-2.48,11.03,0.27,-2.44,10.98,0.27,-2.4,11.2,0.17,-2.56,11.03,0.27,-2.4,11.2,0.35,-2.32,11.11,0.29,-2.28,11.26,0.27,-2.4,11.2,0.36,-2.36,11.07,0.35,-2.32,11.11,-0.09,-2.2,11.35,-0.26,-2.28,11.28,-0.06,-2.4,11.26,-0.49,-2.2,10.62,-0.53,-2.36,10.65,-0.44,-2.32,10.79,-0.28,-2.4,10.59,-0.15,-2.4,10.66,-0.22,-2.44,10.6,-0.1,-2.44,10.66,-0.22,-2.44,10.6,-0.15,-2.4,10.66,0.05,-2.6,10.91,-0.04,-2.52,10.76,0.01,-2.44,10.76,-0.04,-2.6,10.83,-0.04,-2.52,10.76,0.05,-2.6,10.91,0.13,-2.4,11.21,0.27,-2.4,11.2,0.13,-2.2,11.41,0.06,-2.52,11.21,-0.06,-2.4,11.26,0,-2.56,11.1,-0.48,-2.52,10.95,-0.28,-2.36,11.26,-0.46,-2.32,11.17,-0.43,-2.6,10.93,-0.48,-2.52,10.95,-0.41,-2.6,10.68,-0.32,-2.48,10.56,-0.34,-2.52,10.58,-0.45,-2.44,10.57,-0.22,-2.44,10.6,-0.32,-2.48,10.56,-0.28,-2.4,10.59,-0.2,-2.48,10.62,-0.32,-2.48,10.56,-0.22,-2.44,10.6,-0.04,-2.52,10.76,-0.04,-2.6,10.83,-0.19,-2.68,10.86,0.17,-2.28,10.86,0.15,-2.4,10.84,-0.04,-2.32,10.75,0.18,-2.44,10.89,0.17,-2.28,10.86,0.31,-2.28,10.95,0.17,-2.48,10.9,0.05,-2.6,10.91,0.01,-2.44,10.76,0.27,-2.44,10.98,0.2,-2.52,10.95,0.17,-2.48,10.9,0.27,-2.4,11.2,0.13,-2.4,11.21,0.17,-2.56,11.03,-0.06,-2.4,11.26,-0.15,-2.6,11.06,0,-2.56,11.1,-0.28,-2.36,11.26,-0.26,-2.28,11.28,-0.45,-2.2,11.16,-0.48,-2.52,10.95,-0.31,-2.6,10.99,-0.28,-2.36,11.26,-0.43,-2.6,10.93,-0.34,-2.64,10.97,-0.31,-2.6,10.99,-0.53,-2.32,11.03,-0.54,-2.24,10.97,-0.44,-2.32,10.79,-0.32,-2.48,10.56,-0.45,-2.44,10.57,-0.41,-2.4,10.53,-0.32,-2.48,10.56,-0.41,-2.4,10.53,-0.28,-2.4,10.59,0.15,-2.4,10.84,0.18,-2.44,10.89,0.17,-2.48,10.9,0.17,-2.56,11.03,0.2,-2.52,10.95,0.27,-2.44,10.98,0.17,-2.56,11.03,0.06,-2.52,11.21,0,-2.56,11.1,0.13,-2.4,11.21,0.06,-2.52,11.21,0.17,-2.56,11.03,-0.28,-2.36,11.26,-0.31,-2.6,10.99,-0.15,-2.6,11.06,0,-2.56,11.1,-0.05,-2.64,10.97,0.01,-2.6,10.98,0,-2.56,11.1,-0.15,-2.6,11.06,-0.05,-2.64,10.97,-0.06,-2.4,11.26,-0.28,-2.36,11.26,-0.15,-2.6,11.06,-0.32,-2.6,10.56,-0.37,-2.6,10.59,-0.34,-2.52,10.58,-0.34,-2.52,10.58,-0.41,-2.6,10.68,-0.45,-2.44,10.57,-0.43,-2.6,10.93,-0.41,-2.6,10.68,-0.33,-2.64,10.75,-0.39,-2.68,10.89,-0.43,-2.6,10.93,-0.33,-2.64,10.75,0.2,-2.52,10.95,0.17,-2.6,11.01,0.05,-2.6,10.91,0.15,-2.4,10.84,0.17,-2.48,10.9,0.01,-2.44,10.76,0.17,-2.48,10.9,0.2,-2.52,10.95,0.05,-2.6,10.91,0.17,-2.56,11.03,0.17,-2.6,11.01,0.2,-2.52,10.95,0.17,-2.6,11.05,0.17,-2.6,11.01,0.17,-2.56,11.03,-0.04,-2.6,10.83,-0.05,-2.68,10.88,-0.19,-2.68,10.86,-0.01,-2.64,10.91,0.01,-2.6,10.98,-0.05,-2.64,10.97,-0.01,-2.64,10.91,0.04,-2.6,10.94,0.01,-2.6,10.98,-0.28,-2.64,10.96,-0.29,-2.68,10.94,-0.13,-2.68,10.93,-0.48,-2.52,10.95,-0.43,-2.6,10.93,-0.31,-2.6,10.99,-0.3,-2.64,10.97,-0.28,-2.64,10.96,-0.31,-2.6,10.99,-0.34,-2.64,10.97,-0.3,-2.64,10.97,-0.31,-2.6,10.99,-0.34,-2.64,10.97,-0.43,-2.6,10.93,-0.39,-2.68,10.89,-0.33,-2.64,10.75,-0.41,-2.6,10.68,-0.34,-2.64,10.62,-0.41,-2.6,10.68,-0.37,-2.6,10.59,-0.34,-2.64,10.62,-0.41,-2.6,10.68,-0.53,-2.36,10.65,-0.45,-2.44,10.57,-0.13,-2.68,10.93,-0.05,-2.64,10.97,-0.15,-2.6,11.06,-0.31,-2.6,10.99,-0.28,-2.64,10.96,-0.15,-2.6,11.06,-0.28,-2.64,10.96,-0.13,-2.68,10.93,-0.15,-2.6,11.06,-0.3,-2.68,10.88,-0.28,-2.64,10.96,-0.29,-2.68,10.94,-0.28,-2.64,10.96,-0.3,-2.64,10.97,-0.29,-2.68,10.94,-0.39,-2.68,10.89,-0.33,-2.64,10.75,-0.28,-2.68,10.83,-0.41,-2.6,10.68,-0.44,-2.32,10.79,-0.53,-2.36,10.65,0,-2.04,10.66,0.02,-2,10.68,-0.02,-2.04,10.72])

IndexedFaceSet447.setCoord(Coordinate448)

Shape444.setGeometry(IndexedFaceSet447)

Transform443.addChildren(Shape444)

fieldValue442.addChildren(Transform443)

ProtoInstance440.addFieldValue(fieldValue442)

fieldValue439.addChildren(ProtoInstance440)

ProtoInstance436.addFieldValue(fieldValue439)

fieldValue425.addChildren(ProtoInstance436)

ProtoInstance422.addFieldValue(fieldValue425)

fieldValue411.addChildren(ProtoInstance422)

ProtoInstance408.addFieldValue(fieldValue411)

fieldValue397.addChildren(ProtoInstance408)
ProtoInstance449 = ProtoInstance()
ProtoInstance449.setName("Joint")
ProtoInstance449.setDEF("Allen_hanim_r_shoulder")
fieldValue450 = fieldValue()
fieldValue450.setName("name")
fieldValue450.setValue("r_shoulder")

ProtoInstance449.addFieldValue(fieldValue450)
fieldValue451 = fieldValue()
fieldValue451.setName("center")
fieldValue451.setValue("-0.167 1.36 -0.0458")

ProtoInstance449.addFieldValue(fieldValue451)
fieldValue452 = fieldValue()
fieldValue452.setName("children")
ProtoInstance453 = ProtoInstance()
ProtoInstance453.setName("Segment")
ProtoInstance453.setDEF("Allen_hanim_r_upperarm")
fieldValue454 = fieldValue()
fieldValue454.setName("name")
fieldValue454.setValue("r_upperarm")

ProtoInstance453.addFieldValue(fieldValue454)
fieldValue455 = fieldValue()
fieldValue455.setName("children")
Transform456 = Transform()
Transform456.setDEF("Allen_r_upperarm_adjust")
Transform456.setCenter([0.27,1,-0.025])
Transform456.setRotation([0,1,0,1.570796])
Transform456.setScale([0.1,0.1,0.1])
Shape457 = Shape()
Appearance458 = Appearance()
Material459 = Material()
Material459.setUSE("Skin_Color")

Appearance458.setMaterial(Material459)
ImageTexture460 = ImageTexture()
ImageTexture460.setUSE("camo")

Appearance458.setTexture(ImageTexture460)

Shape457.setAppearance(Appearance458)
IndexedFaceSet461 = IndexedFaceSet()
IndexedFaceSet461.setCoordIndex([0,1,2,-1,3,4,5,-1,6,7,8,-1,9,10,11,-1,12,13,14,-1,15,16,17,-1,18,19,20,-1,21,22,23,-1,24,25,26,-1,27,28,29,-1,30,31,32,-1,33,34,35,-1,36,37,38,-1,39,40,41,-1,42,43,44,-1,45,46,47,-1,48,49,50,-1,51,52,53,-1,54,55,56,-1,57,58,59,-1,60,61,62,-1,63,64,65,-1,66,67,68,-1,69,70,71,-1,72,73,74,-1,75,76,77,-1,78,79,80,-1,81,82,83,-1,84,85,86,-1,87,88,89,-1,90,91,92,-1,93,94,95,-1,96,97,98,-1,99,100,101,-1,102,103,104,-1,105,106,107,-1,108,109,110,-1,111,112,113,-1,114,115,116,-1,117,118,119,-1,120,121,122,-1,123,124,125,-1,126,127,128,-1,129,130,131,-1,132,133,134,-1,135,136,137,-1,138,139,140,-1,141,142,143,-1,144,145,146,-1,147,148,149,-1,150,151,152,-1,153,154,155,-1,156,157,158,-1,159,160,161,-1,162,163,164,-1,165,166,167,-1,168,169,170,-1,171,172,173,-1,174,175,176,-1,177,178,179,-1,180,181,182,-1,183,184,185,-1,186,187,188,-1,189,190,191,-1,192,193,194,-1,195,196,197,-1,198,199,200,-1,201,202,203,-1,204,205,206,-1,207,208,209,-1,210,211,212,-1,213,214,215,-1,216,217,218,-1,219,220,221,-1,222,223,224,-1,225,226,227,-1,228,229,230,-1,231,232,233,-1,234,235,236,-1,237,238,239,-1,240,241,242,-1,243,244,245,-1,246,247,248,-1,249,250,251,-1,252,253,254,-1,255,256,257,-1,258,259,260,-1,261,262,263,-1,264,265,266,-1,267,268,269,-1,270,271,272,-1,273,274,275,-1,276,277,278,-1,279,280,281,-1,282,283,284,-1,285,286,287,-1,288,289,290,-1,291,292,293,-1,294,295,296,-1,297,298,299,-1,300,301,302,-1,303,304,305,-1,306,307,308,-1,309,310,311,-1,312,313,314,-1,315,316,317,-1,318,319,320,-1,321,322,323,-1,324,325,326,-1,327,328,329,-1,330,331,332,-1,333,334,335,-1,336,337,338,-1,339,340,341,-1,342,343,344,-1,345,346,347,-1,348,349,350,-1,351,352,353,-1,354,355,356,-1,357,358,359,-1,360,361,362,-1,363,364,365,-1,366,367,368,-1,369,370,371,-1,372,373,374,-1,375,376,377,-1,378,379,380,-1,381,382,383,-1,384,385,386,-1,387,388,389,-1,390,391,392,-1,393,394,395,-1,396,397,398,-1,399,400,401,-1,402,403,404,-1,405,406,407,-1,408,409,410,-1,411,412,413,-1,414,415,416,-1,417,418,419,-1,420,421,422,-1,423,424,425,-1,426,427,428,-1,429,430,431,-1,432,433,434,-1,435,436,437,-1,438,439,440,-1,441,442,443,-1,444,445,446,-1,447,448,449,-1,450,451,452,-1,453,454,455,-1,456,457,458,-1,459,460,461,-1,462,463,464,-1,465,466,467,-1,468,469,470,-1,471,472,473,-1,474,475,476,-1,477,478,479,-1,480,481,482,-1,483,484,485,-1,486,487,488,-1,489,490,491,-1,492,493,494,-1,495,496,497,-1,498,499,500,-1,501,502,503,-1,504,505,506,-1,507,508,509,-1,510,511,512,-1,513,514,515,-1,516,517,518,-1,519,520,521,-1,522,523,524,-1,525,526,527,-1,528,529,530,-1,531,532,533,-1,534,535,536,-1,537,538,539,-1,540,541,542,-1,543,544,545,-1,546,547,548,-1,549,550,551,-1,552,553,554,-1,555,556,557,-1,558,559,560,-1,561,562,563,-1,564,565,566,-1,567,568,569,-1,570,571,572,-1,573,574,575,-1,576,577,578,-1,579,580,581,-1,582,583,584,-1,585,586,587,-1,588,589,590,-1,591,592,593,-1,594,595,596,-1,597,598,599,-1,600,601,602,-1,603,604,605,-1,606,607,608,-1,609,610,611,-1,612,613,614,-1,615,616,617,-1,618,619,620,-1,621,622,623,-1,624,625,626,-1,627,628,629,-1,630,631,632,-1,633,634,635,-1,636,637,638,-1,639,640,641,-1,642,643,644,-1,645,646,647,-1,648,649,650,-1,651,652,653,-1,654,655,656,-1,657,658,659,-1,660,661,662,-1,663,664,665,-1,666,667,668,-1,669,670,671,-1,672,673,674,-1,675,676,677,-1,678,679,680,-1,681,682,683,-1,684,685,686,-1,687,688,689,-1,690,691,692,-1,693,694,695,-1,696,697,698,-1,699,700,701,-1,702,703,704,-1,705,706,707,-1,708,709,710,-1,711,712,713,-1,714,715,716,-1,717,718,719,-1,720,721,722,-1,723,724,725,-1,726,727,728,-1,729,730,731,-1,732,733,734,-1,735,736,737,-1,738,739,740,-1,741,742,743,-1,744,745,746,-1,747,748,749,-1,750,751,752,-1,753,754,755,-1,756,757,758,-1,759,760,761,-1,762,763,764,-1,765,766,767,-1,768,769,770,-1,771,772,773,-1,774,775,776,-1,777,778,779,-1,780,781,782,-1,783,784,785,-1,786,787,788,-1,789,790,791,-1,792,793,794,-1,795,796,797,-1,798,799,800,-1,801,802,803,-1,804,805,806,-1,807,808,809,-1,810,811,812,-1,813,814,815,-1,816,817,818,-1,819,820,821,-1,822,823,824,-1,825,826,827,-1,828,829,830,-1,831,832,833,-1,834,835,836,-1,837,838,839,-1,840,841,842,-1,843,844,845,-1,846,847,848,-1,849,850,851,-1,852,853,854,-1,855,856,857,-1,858,859,860,-1,861,862,863,-1,864,865,866,-1,867,868,869,-1,870,871,872,-1,873,874,875,-1,876,877,878,-1,879,880,881,-1,882,883,884,-1,885,886,887,-1,888,889,890,-1,891,892,893,-1,894,895,896,-1,897,898,899,-1,900,901,902,-1,903,904,905,-1,906,907,908,-1,909,910,911,-1,912,913,914,-1,915,916,917,-1,918,919,920,-1,921,922,923,-1,924,925,926,-1,927,928,929,-1,930,931,932,-1,933,934,935,-1,936,937,938,-1,939,940,941,-1,942,943,944,-1,945,946,947,-1,948,949,950,-1,951,952,953,-1,954,955,956,-1,957,958,959,-1,960,961,962,-1,963,964,965,-1,966,967,968,-1,969,970,971,-1,972,973,974,-1,975,976,977,-1,978,979,980,-1,981,982,983,-1,984,985,986,-1,987,988,989,-1,990,991,992,-1,993,994,995,-1,996,997,998,-1,999,1000,1001,-1,1002,1003,1004,-1,1005,1006,1007,-1,1008,1009,1010,-1,1011,1012,1013,-1,1014,1015,1016,-1,1017,1018,1019,-1,1020,1021,1022,-1,1023,1024,1025,-1,1026,1027,1028,-1,1029,1030,1031,-1,1032,1033,1034,-1,1035,1036,1037,-1,1038,1039,1040,-1,1041,1042,1043,-1,1044,1045,1046,-1,1047,1048,1049,-1,1050,1051,1052,-1,1053,1054,1055,-1,1056,1057,1058,-1,1059,1060,1061,-1,1062,1063,1064,-1,1065,1066,1067,-1,1068,1069,1070,-1,1071,1072,1073,-1,1074,1075,1076,-1,1077,1078,1079,-1,1080,1081,1082,-1,1083,1084,1085,-1,1086,1087,1088,-1,1089,1090,1091,-1,1092,1093,1094,-1,1095,1096,1097,-1,1098,1099,1100,-1,1101,1102,1103,-1,1104,1105,1106,-1,1107,1108,1109,-1,1110,1111,1112,-1,1113,1114,1115,-1,1116,1117,1118,-1,1119,1120,1121,-1,1122,1123,1124,-1,1125,1126,1127,-1,1128,1129,1130,-1,1131,1132,1133,-1,1134,1135,1136,-1,1137,1138,1139,-1,1140,1141,1142,-1,1143,1144,1145,-1,1146,1147,1148,-1,1149,1150,1151,-1,1152,1153,1154,-1,1155,1156,1157,-1,1158,1159,1160,-1,1161,1162,1163,-1,1164,1165,1166,-1,1167,1168,1169,-1,1170,1171,1172,-1,1173,1174,1175,-1,1176,1177,1178,-1,1179,1180,1181,-1,1182,1183,1184,-1,1185,1186,1187,-1,1188,1189,1190,-1,1191,1192,1193,-1,1194,1195,1196,-1,1197,1198,1199,-1,1200,1201,1202,-1,1203,1204,1205,-1,1206,1207,1208,-1,1209,1210,1211,-1,1212,1213,1214,-1,1215,1216,1217,-1,1218,1219,1220,-1,1221,1222,1223,-1,1224,1225,1226,-1,1227,1228,1229,-1,1230,1231,1232,-1,1233,1234,1235,-1,1236,1237,1238,-1,1239,1240,1241,-1,1242,1243,1244,-1,1245,1246,1247,-1,1248,1249,1250,-1,1251,1252,1253,-1,1254,1255,1256,-1,1257,1258,1259,-1,1260,1261,1262,-1,1263,1264,1265,-1,1266,1267,1268,-1,1269,1270,1271,-1,1272,1273,1274,-1,1275,1276,1277,-1,1278,1279,1280,-1,1281,1282,1283,-1,1284,1285,1286,-1,1287,1288,1289,-1,1290,1291,1292,-1,1293,1294,1295,-1,1296,1297,1298,-1,1299,1300,1301,-1,1302,1303,1304,-1,1305,1306,1307,-1,1308,1309,1310,-1,1311,1312,1313,-1,1314,1315,1316,-1,1317,1318,1319,-1,1320,1321,1322,-1,1323,1324,1325,-1,1326,1327,1328,-1,1329,1330,1331,-1,1332,1333,1334,-1,1335,1336,1337,-1,1338,1339,1340,-1,1341,1342,1343,-1,1344,1345,1346,-1,1347,1348,1349,-1,1350,1351,1352,-1,1353,1354,1355,-1,1356,1357,1358,-1,1359,1360,1361,-1,1362,1363,1364,-1,1365,1366,1367,-1,1368,1369,1370,-1,1371,1372,1373,-1,1374,1375,1376,-1,1377,1378,1379,-1,1380,1381,1382,-1,1383,1384,1385,-1,1386,1387,1388,-1,1389,1390,1391,-1,1392,1393,1394,-1,1395,1396,1397,-1,1398,1399,1400,-1,1401,1402,1403,-1,1404,1405,1406,-1,1407,1408,1409,-1,1410,1411,1412,-1,1413,1414,1415,-1,1416,1417,1418,-1,1419,1420,1421,-1,1422,1423,1424,-1,1425,1426,1427,-1,1428,1429,1430,-1,1431,1432,1433,-1,1434,1435,1436,-1,1437,1438,1439,-1,1440,1441,1442,-1,1443,1444,1445,-1,1446,1447,1448,-1,1449,1450,1451,-1,1452,1453,1454,-1,1455,1456,1457,-1,1458,1459,1460,-1,1461,1462,1463,-1,1464,1465,1466,-1,1467,1468,1469,-1,1470,1471,1472,-1,1473,1474,1475,-1,1476,1477,1478,-1,1479,1480,1481,-1,1482,1483,1484,-1,1485,1486,1487,-1,1488,1489,1490,-1,1491,1492,1493,-1,1494,1495,1496,-1,1497,1498,1499,-1,1500,1501,1502,-1,1503,1504,1505,-1,1506,1507,1508,-1,1509,1510,1511,-1,1512,1513,1514,-1,1515,1516,1517,-1,1518,1519,1520,-1,1521,1522,1523,-1,1524,1525,1526,-1,1527,1528,1529,-1,1530,1531,1532,-1,1533,1534,1535,-1,1536,1537,1538,-1,1539,1540,1541,-1,1542,1543,1544,-1,1545,1546,1547,-1,1548,1549,1550,-1,1551,1552,1553,-1,1554,1555,1556,-1,1557,1558,1559,-1,1560,1561,1562,-1,1563,1564,1565,-1,1566,1567,1568,-1,1569,1570,1571,-1,1572,1573,1574,-1,1575,1576,1577,-1,1578,1579,1580,-1,1581,1582,1583,-1,1584,1585,1586,-1,1587,1588,1589,-1,1590,1591,1592,-1,1593,1594,1595,-1,1596,1597,1598,-1,1599,1600,1601,-1,1602,1603,1604,-1,1605,1606,1607,-1,1608,1609,1610,-1,1611,1612,1613,-1,1614,1615,1616,-1,1617,1618,1619,-1,1620,1621,1622,-1,1623,1624,1625,-1,1626,1627,1628,-1,1629,1630,1631,-1,1632,1633,1634,-1,1635,1636,1637,-1,1638,1639,1640,-1,1641,1642,1643,-1,1644,1645,1646,-1,1647,1648,1649,-1,1650,1651,1652,-1,1653,1654,1655,-1,1656,1657,1658,-1,1659,1660,1661,-1,1662,1663,1664,-1,1665,1666,1667,-1,1668,1669,1670,-1,1671,1672,1673,-1,1674,1675,1676,-1,1677,1678,1679,-1,1680,1681,1682,-1,1683,1684,1685,-1,1686,1687,1688,-1,1689,1690,1691,-1,1692,1693,1694,-1,1695,1696,1697,-1,1698,1699,1700,-1,1701,1702,1703,-1,1704,1705,1706,-1,1707,1708,1709,-1,1710,1711,1712,-1,1713,1714,1715,-1,1716,1717,1718,-1,1719,1720,1721,-1,1722,1723,1724,-1,1725,1726,1727,-1,1728,1729,1730,-1,1731,1732,1733,-1,1734,1735,1736,-1,1737,1738,1739,-1,1740,1741,1742,-1,1743,1744,1745,-1,1746,1747,1748,-1,1749,1750,1751,-1,1752,1753,1754,-1,1755,1756,1757,-1,1758,1759,1760,-1,1761,1762,1763,-1,1764,1765,1766,-1,1767,1768,1769,-1,1770,1771,1772,-1,1773,1774,1775,-1,1776,1777,1778,-1,1779,1780,1781,-1,1782,1783,1784,-1,1785,1786,1787,-1,1788,1789,1790,-1,1791,1792,1793,-1,1794,1795,1796,-1,1797,1798,1799,-1,1800,1801,1802,-1,1803,1804,1805,-1,1806,1807,1808,-1,1809,1810,1811,-1,1812,1813,1814,-1])
IndexedFaceSet461.setCreaseAngle(1.53)
Coordinate462 = Coordinate()
Coordinate462.setPoint([0.29,3.96,-4.4,0.54,4.16,-4.27,0.69,4.16,-4.42,0.84,4.12,-4.47,0.82,4.12,-4.49,0.76,4.16,-4.44,1.06,4.08,-4.4,1.13,3.96,-4.52,0.93,4.04,-4.56,1,4.16,-4.21,1.06,4.08,-4.4,0.91,4.16,-4.29,0.82,4.12,-4.49,0.84,4.12,-4.47,0.91,4.08,-4.51,0.91,4.08,-4.51,1.06,4.08,-4.4,0.93,4.04,-4.56,0.89,4.12,-4.43,0.91,4.08,-4.51,0.84,4.12,-4.47,0.91,4.08,-4.51,0.89,4.12,-4.43,1.06,4.08,-4.4,0.69,4.04,-4.62,0.69,4.16,-4.42,0.76,4.16,-4.44,0.93,4,-4.64,0.93,4.04,-4.56,1.13,3.96,-4.52,0.37,3.88,-4.69,0.27,3.8,-4.66,0.29,3.96,-4.4,0.69,4.04,-4.62,0.76,4.16,-4.44,0.82,4.12,-4.49,0.68,3.96,-4.74,0.84,4,-4.68,0.89,3.92,-4.75,0.93,4,-4.64,0.9,4,-4.66,0.93,4.04,-4.56,0.89,4.12,-4.43,0.91,4.16,-4.29,1.06,4.08,-4.4,1.02,3.92,-4.67,0.93,3.96,-4.67,0.93,4,-4.64,1.13,3.96,-4.52,1.27,3.84,-4.55,1.21,3.84,-4.57,1.28,3.96,-4.22,1.4,3.8,-4.45,1.27,3.84,-4.55,0.69,4.04,-4.62,0.76,4.04,-4.63,0.68,3.96,-4.74,0.68,3.96,-4.74,0.76,4.04,-4.63,0.84,4,-4.68,0.84,4,-4.68,0.93,3.96,-4.67,0.89,3.92,-4.75,0.9,4,-4.66,0.93,4,-4.64,0.93,3.96,-4.67,1.4,3.8,-4.45,1.35,3.8,-4.56,1.27,3.84,-4.55,1.13,3.96,-4.52,1.28,3.96,-4.22,1.27,3.84,-4.55,1.28,3.96,-4.22,1.06,4.08,-4.4,1,4.16,-4.21,1.02,3.92,-4.67,0.93,4,-4.64,1.13,3.96,-4.52,0.29,3.96,-4.4,0.39,4.08,-4.17,0.54,4.16,-4.27,0.76,4.04,-4.63,0.69,4.04,-4.62,0.82,4.12,-4.49,0.29,3.96,-4.4,0.69,4.16,-4.42,0.69,4.04,-4.62,0.29,3.96,-4.4,0.14,3.72,-4.53,-0.01,3.64,-4.07,0.89,3.92,-4.75,0.86,3.72,-4.91,0.78,3.88,-4.82,0.84,4,-4.68,0.9,4,-4.66,0.93,3.96,-4.67,1.13,3.76,-4.71,1.21,3.84,-4.57,1.24,3.76,-4.6,1.21,3.84,-4.57,1.13,3.76,-4.71,1.02,3.92,-4.67,0.89,3.92,-4.75,0.93,3.96,-4.67,1.02,3.92,-4.67,1.13,3.96,-4.52,1.06,4.08,-4.4,1.28,3.96,-4.22,0.39,4.08,-4.17,0.29,3.96,-4.4,-0.01,3.64,-4.07,0.78,3.88,-4.82,0.79,3.68,-4.96,0.5,3.68,-4.89,1.21,3.84,-4.57,1.02,3.92,-4.67,1.13,3.96,-4.52,0.68,3.96,-4.74,0.37,3.88,-4.69,0.69,4.04,-4.62,0.89,3.92,-4.75,0.98,3.68,-4.93,0.86,3.72,-4.91,1.24,3.64,-4.67,1.3,3.52,-4.71,1.05,3.6,-4.94,1.43,3.68,-4.59,1.4,3.8,-4.45,1.52,3.64,-4.52,1.38,3.72,-4.58,1.35,3.8,-4.56,1.4,3.8,-4.45,0.89,3.92,-4.75,1.02,3.92,-4.67,1.13,3.76,-4.71,0.89,3.92,-4.75,1.13,3.76,-4.71,0.98,3.68,-4.93,1.05,3.6,-4.94,0.98,3.68,-4.93,1.13,3.76,-4.71,1.35,3.8,-4.56,1.28,3.72,-4.59,1.24,3.76,-4.6,1.57,3.68,-4.28,1.52,3.64,-4.52,1.4,3.8,-4.45,1.35,3.8,-4.56,1.38,3.72,-4.58,1.28,3.72,-4.59,1.43,3.68,-4.59,1.38,3.72,-4.58,1.4,3.8,-4.45,0.29,3.96,-4.4,0.27,3.8,-4.66,0.14,3.72,-4.53,0.23,3.44,-4.8,0.22,3.24,-4.86,0.06,3.16,-4.52,0.86,3.72,-4.91,0.87,3.68,-4.93,0.79,3.68,-4.96,1.05,3.4,-5.05,0.84,3.4,-5.08,0.83,3.64,-4.96,1.13,3.76,-4.71,1.24,3.64,-4.67,1.05,3.6,-4.94,0.51,3.32,-5.04,0.22,3.24,-4.86,0.23,3.44,-4.8,0.14,3.72,-4.53,0.27,3.8,-4.66,0.23,3.44,-4.8,0.37,3.88,-4.69,0.29,3.96,-4.4,0.69,4.04,-4.62,0.5,3.68,-4.89,0.37,3.88,-4.69,0.68,3.96,-4.74,1.29,3.64,-4.63,1.24,3.64,-4.67,1.28,3.72,-4.59,1.35,3.64,-4.6,1.29,3.64,-4.63,1.28,3.72,-4.59,-0.03,3.4,-4.51,-0.14,3.24,-4.29,-0.01,3.64,-4.07,1.24,3.64,-4.67,1.13,3.76,-4.71,1.24,3.76,-4.6,0.5,3.68,-4.89,0.27,3.8,-4.66,0.37,3.88,-4.69,0.76,3.56,-5.03,0.79,3.68,-4.96,0.83,3.64,-4.96,0.78,3.88,-4.82,0.5,3.68,-4.89,0.68,3.96,-4.74,1.47,3.56,-4.61,1.54,3.6,-4.55,1.63,3.44,-4.58,1.68,3.36,-4.51,1.58,3.52,-4.4,1.73,3.4,-4.26,1.68,3.36,-4.51,1.63,3.44,-4.58,1.58,3.52,-4.4,1.73,3.4,-4.26,1.58,3.52,-4.4,1.57,3.68,-4.28,0.65,3.28,-5.12,0.51,3.32,-5.04,0.76,3.56,-5.03,1.3,3.52,-4.71,1.24,3.64,-4.67,1.29,3.64,-4.63,-0.03,3.4,-4.51,-0.01,3.64,-4.07,0.14,3.72,-4.53,0.78,3.88,-4.82,0.86,3.72,-4.91,0.79,3.68,-4.96,0.76,3.56,-5.03,0.83,3.64,-4.96,0.84,3.4,-5.08,0.98,3.68,-4.93,1.05,3.6,-4.94,0.83,3.64,-4.96,1.24,3.64,-4.67,1.24,3.76,-4.6,1.28,3.72,-4.59,0.76,3.56,-5.03,0.5,3.68,-4.89,0.79,3.68,-4.96,0.51,3.32,-5.04,0.5,3.68,-4.89,0.76,3.56,-5.03,1.05,3.6,-4.94,1.05,3.4,-5.05,0.83,3.64,-4.96,1.05,3.4,-5.05,0.99,3.36,-5.12,0.84,3.4,-5.08,1.02,3.32,-5.1,1.05,3.4,-5.05,1.22,3.36,-4.99,1.37,3.48,-4.65,1.3,3.52,-4.71,1.29,3.64,-4.63,1.41,3.48,-4.61,1.37,3.48,-4.65,1.29,3.64,-4.63,1.68,3.36,-4.51,1.64,3.36,-4.58,1.63,3.44,-4.58,1.63,3.44,-4.58,1.54,3.6,-4.55,1.58,3.52,-4.4,0.23,3.44,-4.8,-0.03,3.4,-4.51,0.14,3.72,-4.53,0.65,3.28,-5.12,0.76,3.56,-5.03,0.84,3.4,-5.08,1.05,3.4,-5.05,1.02,3.32,-5.1,0.99,3.36,-5.12,1.4,3.36,-4.71,1.3,3.52,-4.71,1.37,3.48,-4.65,1.46,3.36,-4.64,1.41,3.48,-4.61,1.5,3.4,-4.6,1.46,3.36,-4.64,1.37,3.48,-4.65,1.41,3.48,-4.61,1.64,3.36,-4.58,1.59,3.4,-4.59,1.63,3.44,-4.58,1.58,3.52,-4.4,1.54,3.6,-4.55,1.52,3.64,-4.52,1.8,3.2,-4.28,1.71,3.28,-4.44,1.73,3.4,-4.26,0.97,3.32,-5.14,0.99,3.36,-5.12,1.02,3.32,-5.1,1.05,3.4,-5.05,1.05,3.6,-4.94,1.22,3.36,-4.99,0.51,3.32,-5.04,0.65,3.28,-5.12,0.6,2.88,-5.24,0.84,3.4,-5.08,0.97,3.32,-5.14,0.83,3.28,-5.17,0.83,3.2,-5.2,0.97,3.32,-5.14,0.96,3.16,-5.2,1.22,3.36,-4.99,1.17,3.08,-5.14,1.08,3.12,-5.14,1.02,3.32,-5.1,1.22,3.36,-4.99,1.08,3.12,-5.14,1.4,3.36,-4.71,1.48,3.24,-4.73,1.38,3.28,-4.92,1.38,3.28,-4.92,1.22,3.36,-4.99,1.3,3.52,-4.71,1.4,3.36,-4.71,1.46,3.36,-4.64,1.48,3.24,-4.73,1.46,3.36,-4.64,1.4,3.36,-4.71,1.37,3.48,-4.65,1.46,3.36,-4.64,1.52,3.32,-4.61,1.48,3.24,-4.73,1.68,3.28,-4.58,1.71,3.28,-4.44,1.76,3.24,-4.5,1.68,3.36,-4.51,1.73,3.4,-4.26,1.71,3.28,-4.44,1.68,3.28,-4.58,1.68,3.36,-4.51,1.71,3.28,-4.44,1.57,3.68,-4.28,1.58,3.52,-4.4,1.52,3.64,-4.52,-0.08,3.28,-4.51,-0.03,3.4,-4.51,0.06,3.16,-4.52,0.51,3.32,-5.04,0.23,3.44,-4.8,0.5,3.68,-4.89,0.84,3.4,-5.08,0.99,3.36,-5.12,0.97,3.32,-5.14,0.83,3.2,-5.2,0.83,3.28,-5.17,0.97,3.32,-5.14,1.3,3.52,-4.71,1.22,3.36,-4.99,1.05,3.6,-4.94,1.38,3.28,-4.92,1.48,3.24,-4.73,1.58,3.12,-4.72,1.64,3.36,-4.58,1.54,3.28,-4.59,1.52,3.32,-4.61,1.68,3.28,-4.58,1.54,3.28,-4.59,1.64,3.36,-4.58,1.68,3.36,-4.51,1.68,3.28,-4.58,1.64,3.36,-4.58,1.72,3.16,-4.43,1.76,3.24,-4.5,1.71,3.28,-4.44,0.65,3.28,-5.12,0.84,3.4,-5.08,0.83,3.28,-5.17,0.83,3.2,-5.2,0.79,3.2,-5.2,0.83,3.28,-5.17,0.96,3.16,-5.2,1.02,3.32,-5.1,1.08,3.12,-5.14,1.38,3.28,-4.92,1.58,3.12,-4.72,1.63,2.96,-4.83,-0.13,3.2,-4.48,-0.08,3.28,-4.51,0.06,3.16,-4.52,0.96,3.16,-5.2,0.97,3.32,-5.14,1.02,3.32,-5.1,0.96,3.16,-5.2,1.08,3.12,-5.14,1.04,3.08,-5.19,1.31,3.04,-5.08,1.22,3.36,-4.99,1.38,3.28,-4.92,1.4,3.36,-4.71,1.38,3.28,-4.92,1.3,3.52,-4.71,1.52,3.32,-4.61,1.54,3.28,-4.59,1.48,3.24,-4.73,1.62,3.08,-4.64,1.71,3.08,-4.56,1.72,3.04,-4.57,1.73,3.2,-4.54,1.7,3.2,-4.55,1.76,3.24,-4.5,1.76,3.12,-4.49,1.82,3.16,-4.5,1.73,3.2,-4.54,1.73,3.2,-4.54,1.76,3.24,-4.5,1.72,3.16,-4.43,-0.13,3.2,-4.48,0.01,3.04,-4.53,-0.15,2.84,-4.5,0.06,3.16,-4.52,0.22,3.24,-4.86,0.17,3.08,-4.85,0.27,3.8,-4.66,0.5,3.68,-4.89,0.23,3.44,-4.8,0.65,3.28,-5.12,0.83,3.28,-5.17,0.79,3.2,-5.2,0.79,3.2,-5.2,0.83,3.16,-5.23,0.78,3.08,-5.25,0.79,3.2,-5.2,0.83,3.2,-5.2,0.83,3.16,-5.23,0.86,3.16,-5.21,0.83,3.16,-5.23,0.83,3.2,-5.2,1.31,3.04,-5.08,1.17,3.08,-5.14,1.22,3.36,-4.99,1.7,3.2,-4.55,1.7,3.16,-4.55,1.63,3.2,-4.57,1.73,3.16,-4.54,1.7,3.16,-4.55,1.7,3.2,-4.55,1.7,3.2,-4.55,1.73,3.2,-4.54,1.73,3.16,-4.54,-0.13,3.2,-4.48,0.06,3.16,-4.52,0.01,3.04,-4.53,0.96,3.16,-5.2,1.04,3.08,-5.19,0.93,3.08,-5.25,1.48,3.24,-4.73,1.61,3.12,-4.63,1.58,3.12,-4.72,1.63,3.2,-4.57,1.48,3.24,-4.73,1.54,3.28,-4.59,1.7,3.16,-4.55,1.61,3.12,-4.63,1.63,3.2,-4.57,1.76,3.12,-4.49,1.73,3.12,-4.54,1.82,3.16,-4.5,1.76,3.12,-4.49,1.73,3.2,-4.54,1.72,3.16,-4.43,1.72,3.16,-4.43,1.71,3.28,-4.44,1.8,3.2,-4.28,1.8,2.72,-4.21,1.8,2.64,-4.44,1.78,2.88,-4.54,1.73,3.12,-4.54,1.76,3.12,-4.49,1.77,3.08,-4.46,0.23,3.44,-4.8,0.06,3.16,-4.52,-0.03,3.4,-4.51,0.29,2.8,-4.99,0.51,3.32,-5.04,0.6,2.88,-5.24,0.79,3.2,-5.2,0.78,3.08,-5.25,0.65,3.28,-5.12,0.83,3.16,-5.23,0.84,3.12,-5.24,0.78,3.08,-5.25,0.78,3.08,-5.25,0.84,3.12,-5.24,0.93,3.08,-5.25,1.04,3.08,-5.19,1.08,3.12,-5.14,1.09,3.08,-5.15,1.63,3.2,-4.57,1.61,3.12,-4.63,1.48,3.24,-4.73,1.7,3.12,-4.55,1.73,3.12,-4.54,1.71,3.08,-4.56,1.74,3.08,-4.54,1.71,3.08,-4.56,1.73,3.12,-4.54,0.06,3.16,-4.52,0.17,3.08,-4.85,0.11,3,-4.79,0.09,2.96,-4.65,0.01,3.04,-4.53,0.06,3.16,-4.52,1.18,2.96,-5.14,1.31,3.04,-5.08,1.3,2.88,-5.15,1.42,2.84,-5.09,1.31,3.04,-5.08,1.63,2.96,-4.83,1.58,3.12,-4.72,1.61,3.12,-4.63,1.62,3.08,-4.64,1.63,2.96,-4.83,1.58,3.12,-4.72,1.62,3.08,-4.64,1.77,3.04,-4.53,1.75,3.04,-4.55,1.77,3.08,-4.46,1.8,3.2,-4.28,1.82,3.04,-4.26,1.72,3.16,-4.43,0.09,2.96,-4.65,0.06,3.16,-4.52,0.11,3,-4.79,0.93,3.08,-5.25,1.05,3.04,-5.2,0.87,2.88,-5.34,0.84,3.12,-5.24,0.96,3.16,-5.2,0.93,3.08,-5.25,1.62,3.08,-4.64,1.68,2.96,-4.61,1.63,2.96,-4.83,1.7,3.16,-4.55,1.7,3.12,-4.55,1.61,3.12,-4.63,1.62,3.08,-4.64,1.61,3.12,-4.63,1.7,3.12,-4.55,1.62,3.08,-4.64,1.7,3.12,-4.55,1.71,3.08,-4.56,1.75,3.04,-4.55,1.77,3.04,-4.53,1.75,3,-4.55,1.77,3,-4.53,1.75,3,-4.55,1.77,3.04,-4.53,1.8,3,-4.44,1.77,3.04,-4.53,1.77,3.08,-4.46,1.82,3.04,-4.26,1.8,3,-4.44,1.77,3.08,-4.46,1.82,3.04,-4.26,1.77,3.08,-4.46,1.72,3.16,-4.43,0.22,2.84,-4.86,0.1,2.84,-4.8,0.11,3,-4.79,0.17,3.08,-4.85,0.22,3.24,-4.86,0.51,3.32,-5.04,0.93,3.08,-5.25,0.87,2.88,-5.34,0.78,3.08,-5.25,1.17,3.08,-5.14,1.18,2.96,-5.14,1.12,2.96,-5.17,1.63,2.68,-4.94,1.5,2.4,-5.15,1.43,2.48,-5.17,1.75,3,-4.55,1.72,3.04,-4.57,1.75,3.04,-4.55,1.75,3,-4.55,1.68,2.96,-4.61,1.72,3.04,-4.57,1.75,2.96,-4.55,1.8,3,-4.44,1.78,2.88,-4.54,1.31,3.04,-5.08,1.18,2.96,-5.14,1.17,3.08,-5.14,1.3,2.88,-5.15,1.31,3.04,-5.08,1.42,2.84,-5.09,1.31,3.04,-5.08,1.38,3.28,-4.92,1.63,2.96,-4.83,1.68,2.84,-4.87,1.63,2.96,-4.83,1.66,2.84,-4.67,1.68,2.96,-4.61,1.66,2.84,-4.67,1.63,2.96,-4.83,1.75,3,-4.55,1.75,2.96,-4.55,1.68,2.96,-4.61,1.75,2.96,-4.55,1.78,2.88,-4.54,1.68,2.96,-4.61,1.04,3.08,-5.19,1.05,3.04,-5.2,0.93,3.08,-5.25,1.05,3.04,-5.2,1.12,2.96,-5.17,0.87,2.88,-5.34,1.12,2.96,-5.17,1.05,3.04,-5.2,1.17,3.08,-5.14,1.28,2.56,-5.21,1.13,2.72,-5.25,1.18,2.84,-5.18,1.41,2.6,-5.16,1.63,2.68,-4.94,1.43,2.48,-5.17,1.63,2.96,-4.83,1.68,2.84,-4.87,1.42,2.84,-5.09,1.68,2.96,-4.61,1.62,3.08,-4.64,1.72,3.04,-4.57,1.68,2.96,-4.61,1.78,2.88,-4.54,1.66,2.84,-4.67,0.09,2.96,-4.65,0.03,2.84,-4.55,0.01,3.04,-4.53,0.13,2.68,-4.57,0.11,2.72,-4.56,0.1,2.76,-4.64,0.22,2.84,-4.86,0.29,2.8,-4.99,0.25,2.76,-4.95,0.87,2.88,-5.34,0.6,2.88,-5.24,0.78,3.08,-5.25,0.03,2.84,-4.55,-0.15,2.84,-4.5,0.01,3.04,-4.53,0.25,2.76,-4.95,0.24,2.68,-4.95,0.21,2.64,-4.91,0.22,2.84,-4.86,0.25,2.76,-4.95,0.21,2.64,-4.91,0.17,3.08,-4.85,0.29,2.8,-4.99,0.22,2.84,-4.86,0.29,2.8,-4.99,0.17,3.08,-4.85,0.51,3.32,-5.04,1.68,2.84,-4.87,1.66,2.84,-4.67,1.72,2.8,-4.82,1.8,2.64,-4.44,1.73,2.64,-4.61,1.78,2.88,-4.54,0.22,2.84,-4.86,0.11,3,-4.79,0.17,3.08,-4.85,0.07,2.8,-4.75,0.21,2.64,-4.91,0.08,2.6,-4.66,0.5,2.52,-5.21,0.41,2.6,-5.09,0.6,2.88,-5.24,1.13,2.72,-5.25,0.88,2.68,-5.37,0.87,2.88,-5.34,1.41,2.6,-5.16,1.43,2.48,-5.17,1.38,2.48,-5.21,1.63,2.68,-4.94,1.68,2.84,-4.87,1.72,2.8,-4.82,1.8,2.72,-4.21,1.78,2.88,-4.54,1.8,3,-4.44,0.09,2.96,-4.65,0.09,2.8,-4.61,0.03,2.84,-4.55,0.1,2.84,-4.8,0.07,2.8,-4.75,0.09,2.96,-4.65,0.1,2.84,-4.8,0.09,2.96,-4.65,0.11,3,-4.79,0.41,2.6,-5.09,0.29,2.8,-4.99,0.6,2.88,-5.24,1.18,2.84,-5.18,0.87,2.88,-5.34,1.12,2.96,-5.17,1.41,2.6,-5.16,1.28,2.56,-5.21,1.3,2.88,-5.15,1.28,2.56,-5.21,1.18,2.84,-5.18,1.3,2.88,-5.15,1.63,2.68,-4.94,1.8,2.6,-4.73,1.6,2.4,-4.96,0.02,2.72,-4.59,0.09,2.8,-4.61,0.1,2.76,-4.64,0.02,2.72,-4.59,0.03,2.84,-4.55,0.09,2.8,-4.61,0.11,2.72,-4.56,0.02,2.72,-4.59,0.1,2.76,-4.64,0.1,2.64,-4.6,0.13,2.68,-4.57,0.1,2.76,-4.64,0.07,2.8,-4.75,0.1,2.76,-4.64,0.09,2.8,-4.61,0.07,2.8,-4.75,0.09,2.8,-4.61,0.09,2.96,-4.65,0.26,2.68,-4.98,0.25,2.76,-4.95,0.29,2.8,-4.99,0.33,2.6,-5,0.26,2.68,-4.98,0.29,2.8,-4.99,0.78,3.08,-5.25,0.6,2.88,-5.24,0.65,3.28,-5.12,1.72,2.8,-4.82,1.66,2.84,-4.67,1.73,2.64,-4.61,0.08,2.6,-4.66,0.1,2.64,-4.6,0.1,2.76,-4.64,0.07,2.8,-4.75,0.1,2.84,-4.8,0.21,2.64,-4.91,0.33,2.6,-5,0.29,2.8,-4.99,0.41,2.6,-5.09,0.1,2.84,-4.8,0.22,2.84,-4.86,0.21,2.64,-4.91,0.26,2.68,-4.98,0.24,2.68,-4.95,0.25,2.76,-4.95,0.33,2.6,-5,0.41,2.6,-5.09,0.38,2.52,-5.07,0.62,2.4,-5.34,0.5,2.52,-5.21,0.88,2.68,-5.37,0.87,2.88,-5.34,0.88,2.68,-5.37,0.6,2.88,-5.24,1.18,2.84,-5.18,1.13,2.72,-5.25,0.87,2.88,-5.34,1.41,2.6,-5.16,1.3,2.88,-5.15,1.42,2.84,-5.09,1.72,2.8,-4.82,1.73,2.64,-4.61,1.8,2.6,-4.73,1.66,2.84,-4.67,1.78,2.88,-4.54,1.73,2.64,-4.61,0.03,2.84,-4.55,-0.07,2.8,-4.59,-0.15,2.84,-4.5,0.02,2.72,-4.59,-0.07,2.8,-4.59,0.03,2.84,-4.55,0.02,2.72,-4.59,0,2.68,-4.61,-0.07,2.8,-4.59,0.08,2.6,-4.66,0.1,2.76,-4.64,0.07,2.8,-4.75,0.24,2.68,-4.95,0.24,2.64,-4.95,0.21,2.64,-4.91,0.24,2.68,-4.95,0.26,2.68,-4.98,0.24,2.64,-4.95,0.5,2.52,-5.21,0.47,2.44,-5.19,0.4,2.48,-5.1,1.68,2.84,-4.87,1.63,2.68,-4.94,1.42,2.84,-5.09,-0.07,2.8,-4.59,-0.18,2.48,-4.4,-0.15,2.84,-4.5,-0.07,2.8,-4.59,0,2.68,-4.61,-0.18,2.48,-4.4,0.21,2.64,-4.91,0.24,2.64,-4.95,0.29,2.48,-4.96,0.33,2.6,-5,0.38,2.52,-5.07,0.29,2.48,-4.96,0.4,2.52,-5.09,0.5,2.52,-5.21,0.4,2.48,-5.1,0.88,2.68,-5.37,0.5,2.52,-5.21,0.6,2.88,-5.24,1.41,2.6,-5.16,1.38,2.48,-5.21,1.28,2.56,-5.21,-0.11,2.36,-4.47,0.14,2.48,-4.65,0.12,2.32,-4.62,0.1,2.64,-4.6,0.08,2.6,-4.66,0,2.68,-4.61,1.86,2.28,-4.55,1.83,2.4,-4.79,1.8,2.6,-4.73,1.73,2.64,-4.61,1.86,2.28,-4.55,1.8,2.6,-4.73,0.12,2.32,-4.62,0.13,2.16,-4.62,-0.01,2.16,-4.58,0.4,2.52,-5.09,0.38,2.52,-5.07,0.41,2.6,-5.09,1.11,2.4,-5.38,1.01,2.44,-5.39,1.13,2.72,-5.25,1.11,2.4,-5.38,1.28,2.56,-5.21,1.34,2.44,-5.22,1.8,2.6,-4.73,1.72,2.36,-4.82,1.6,2.4,-4.96,-0.11,2.36,-4.47,0.12,2.32,-4.62,-0.01,2.16,-4.58,0.14,2.48,-4.65,-0.06,2.52,-4.58,0.08,2.6,-4.66,0.29,2.48,-4.96,0.17,2.32,-4.78,0.14,2.48,-4.65,0.38,2.52,-5.07,0.4,2.48,-5.1,0.36,2.4,-5.05,0.38,2.52,-5.07,0.36,2.4,-5.05,0.29,2.48,-4.96,0.38,2.52,-5.07,0.4,2.52,-5.09,0.4,2.48,-5.1,0.4,2.48,-5.1,0.47,2.44,-5.19,0.37,2.4,-5.08,0.5,2.28,-5.25,0.62,2.4,-5.34,0.64,2.28,-5.4,0.93,2.4,-5.43,0.64,2.28,-5.4,0.62,2.4,-5.34,1.41,2.6,-5.16,1.42,2.84,-5.09,1.63,2.68,-4.94,1.73,2.64,-4.61,1.8,2.64,-4.44,1.86,2.28,-4.55,0,2.68,-4.61,-0.06,2.52,-4.58,-0.18,2.48,-4.4,0.08,2.6,-4.66,-0.06,2.52,-4.58,0,2.68,-4.61,0.37,2.4,-5.08,0.36,2.4,-5.05,0.4,2.48,-5.1,0.47,2.44,-5.19,0.38,2.36,-5.11,0.37,2.4,-5.08,0.4,2.52,-5.09,0.41,2.6,-5.09,0.5,2.52,-5.21,0.47,2.44,-5.19,0.5,2.28,-5.25,0.38,2.36,-5.11,0.88,2.68,-5.37,1.01,2.44,-5.39,0.93,2.4,-5.43,0.93,2.4,-5.43,0.99,2.4,-5.41,1,2.36,-5.41,1,2.36,-5.41,1.11,2.4,-5.38,1.09,2.2,-5.44,1.28,2.56,-5.21,1.38,2.48,-5.21,1.34,2.44,-5.22,1.38,2.48,-5.21,1.38,2.44,-5.21,1.34,2.44,-5.22,1.38,2.48,-5.21,1.43,2.48,-5.17,1.38,2.44,-5.21,1.8,2.72,-4.21,1.8,3,-4.44,1.82,3.04,-4.26,1.11,2.4,-5.38,1.13,2.72,-5.25,1.28,2.56,-5.21,1.63,2.68,-4.94,1.72,2.8,-4.82,1.8,2.6,-4.73,0.21,2.64,-4.91,0.29,2.48,-4.96,0.14,2.48,-4.65,0.62,2.4,-5.34,0.47,2.44,-5.19,0.5,2.52,-5.21,1.01,2.44,-5.39,0.99,2.4,-5.41,0.93,2.4,-5.43,1.01,2.4,-5.39,0.99,2.4,-5.41,1.01,2.44,-5.39,-0.11,2.36,-4.47,-0.18,2.48,-4.4,-0.06,2.52,-4.58,-0.18,2.16,-4.49,-0.11,2.36,-4.47,-0.01,2.16,-4.58,-0.11,2.36,-4.47,-0.06,2.52,-4.58,0.14,2.48,-4.65,0.17,2.32,-4.78,0.29,2.48,-4.96,0.33,2.28,-4.92,0.24,2.64,-4.95,0.26,2.68,-4.98,0.33,2.6,-5,0.38,2.36,-5.11,0.37,2.36,-5.08,0.37,2.4,-5.08,0.36,2.28,-5.09,0.38,2.36,-5.11,0.5,2.28,-5.25,1.38,2.44,-5.21,1.5,2.4,-5.15,1.38,2.32,-5.25,1.8,2.6,-4.73,1.83,2.4,-4.79,1.72,2.36,-4.82,1.8,2.32,-4.8,1.72,2.36,-4.82,1.83,2.4,-4.79,1.79,2.28,-4.8,1.8,2.32,-4.8,1.87,2.28,-4.7,1.8,2.32,-4.8,1.83,2.4,-4.79,1.87,2.28,-4.7,1.9,2.08,-4.65,1.89,2.16,-4.6,1.77,1.96,-4.55,1.69,2.32,-4.39,1.8,2.64,-4.44,1.8,2.72,-4.21,0.17,2.28,-4.62,0.12,2.32,-4.62,0.17,2.32,-4.78,0.17,2.32,-4.78,0.12,2.32,-4.62,0.14,2.48,-4.65,0.2,2.2,-4.75,0.17,2.32,-4.78,0.33,2.28,-4.92,0.24,2.64,-4.95,0.33,2.6,-5,0.29,2.48,-4.96,0.37,2.36,-5.08,0.36,2.4,-5.05,0.37,2.4,-5.08,0.36,2.4,-5.05,0.37,2.36,-5.08,0.33,2.28,-4.92,0.38,2.36,-5.11,0.36,2.28,-5.09,0.37,2.36,-5.08,0.62,2.4,-5.34,0.88,2.68,-5.37,0.93,2.4,-5.43,0.34,2.2,-5.07,0.5,2.28,-5.25,0.36,1.84,-5.05,1.34,2.44,-5.22,1.38,2.32,-5.25,1.11,2.4,-5.38,1.63,2.68,-4.94,1.6,2.4,-4.96,1.5,2.4,-5.15,1.87,2.28,-4.7,1.89,2.16,-4.6,1.81,2.2,-4.78,0.19,2.24,-4.64,0.17,2.28,-4.62,0.17,2.32,-4.78,0.21,2.64,-4.91,0.14,2.48,-4.65,0.08,2.6,-4.66,0.36,2.4,-5.05,0.33,2.28,-4.92,0.29,2.48,-4.96,0.93,2.4,-5.43,0.92,2.16,-5.49,0.64,2.28,-5.4,1.38,2.32,-5.25,1.34,2.44,-5.22,1.38,2.44,-5.21,1.5,2.4,-5.15,1.38,2.44,-5.21,1.43,2.48,-5.17,1.5,2.4,-5.15,1.63,2.24,-4.91,1.62,2.04,-5.08,1.69,2.28,-4.8,1.67,2.28,-4.83,1.72,2.36,-4.82,0.19,2.24,-4.64,0.17,2.32,-4.78,0.2,2.2,-4.75,0.19,2.24,-4.64,0.2,2.2,-4.75,0.24,2.12,-4.64,0.2,2.2,-4.75,0.33,2.28,-4.92,0.33,2.08,-4.8,0.88,2.68,-5.37,1.13,2.72,-5.25,1.01,2.44,-5.39,0.93,2.4,-5.43,1,2.36,-5.41,0.92,2.16,-5.49,1.33,1.96,-5.4,1.38,2.32,-5.25,1.62,2.04,-5.08,1.67,2.28,-4.83,1.63,2.24,-4.91,1.6,2.4,-4.96,1.67,2.28,-4.83,1.6,2.4,-4.96,1.72,2.36,-4.82,1.69,2.24,-4.8,1.79,2.28,-4.8,1.81,2.2,-4.78,1.89,2.16,-4.6,1.9,2.08,-4.65,1.81,2.2,-4.78,1.81,2.2,-4.78,1.79,2.28,-4.8,1.87,2.28,-4.7,-0.18,2.16,-4.49,-0.23,2.2,-4.45,-0.11,2.36,-4.47,0.12,2.32,-4.62,0.17,2.28,-4.62,0.13,2.16,-4.62,0.19,2.24,-4.64,0.13,2.16,-4.62,0.17,2.28,-4.62,0.37,2.36,-5.08,0.36,2.28,-5.09,0.33,2.28,-4.92,0.62,2.4,-5.34,0.5,2.28,-5.25,0.47,2.44,-5.19,1,2.36,-5.41,1.09,2.2,-5.44,0.92,2.16,-5.49,1.62,2.04,-5.08,1.63,2.24,-4.91,1.64,2.16,-4.88,1.67,2.28,-4.83,1.67,2.24,-4.83,1.63,2.24,-4.91,1.67,2.24,-4.83,1.69,2.24,-4.8,1.66,2.16,-4.82,1.83,2.04,-4.71,1.78,2.08,-4.75,1.81,2.2,-4.78,1.9,2.08,-4.65,1.83,2.04,-4.71,1.81,2.2,-4.78,1.89,2.16,-4.6,1.66,2.04,-4.48,1.77,1.96,-4.55,1.86,2.28,-4.55,1.87,2.28,-4.7,1.83,2.4,-4.79,0.64,2.28,-5.4,0.5,1.52,-5.44,0.5,2.28,-5.25,1.62,2.04,-5.08,1.64,2.16,-4.88,1.68,1.92,-4.9,1.5,2.4,-5.15,1.6,2.4,-4.96,1.63,2.24,-4.91,0.13,2.16,-4.62,0.19,2.24,-4.64,0.24,2.12,-4.64,0.13,2.16,-4.62,0.07,2,-4.55,0.02,2.04,-4.55,0.13,2.16,-4.62,0.24,2.12,-4.64,0.17,1.96,-4.54,0.36,2.28,-5.09,0.34,2.2,-5.07,0.33,2.28,-4.92,0.34,2.2,-5.07,0.36,2.28,-5.09,0.5,2.28,-5.25,1.64,2.16,-4.88,1.63,2.24,-4.91,1.67,2.24,-4.83,1.66,2.16,-4.82,1.64,2.16,-4.88,1.67,2.24,-4.83,1.7,2.16,-4.77,1.66,2.16,-4.82,1.69,2.24,-4.8,1.66,2.04,-4.48,1.89,2.16,-4.6,1.86,2.28,-4.55,1.66,2.04,-4.48,1.86,2.28,-4.55,1.69,2.32,-4.39,0.02,2.04,-4.55,-0.03,2.04,-4.52,-0.01,2.16,-4.58,1.09,2.2,-5.44,1.38,2.32,-5.25,1.33,1.96,-5.4,1.66,2.12,-4.81,1.64,2.16,-4.88,1.66,2.16,-4.82,1.87,2.28,-4.7,1.86,2.28,-4.55,1.89,2.16,-4.6,1.9,2.08,-4.65,1.77,1.96,-4.55,1.87,1.96,-4.61,-0.18,2.16,-4.49,-0.01,2.16,-4.58,-0.03,2.04,-4.52,0.02,2.04,-4.55,0.06,2,-4.52,-0.03,2.04,-4.52,0.33,1.92,-4.57,0.33,2.08,-4.8,0.36,1.84,-5.05,-0.01,2.16,-4.58,0.13,2.16,-4.62,0.02,2.04,-4.55,0.34,2.2,-5.07,0.36,1.84,-5.05,0.33,2.08,-4.8,1.38,2.32,-5.25,1.09,2.2,-5.44,1.11,2.4,-5.38,-0.08,2.04,-4.44,-0.18,2.16,-4.49,-0.03,2.04,-4.52,0.07,2,-4.55,0.06,2,-4.52,0.02,2.04,-4.55,1.87,1.96,-4.61,1.82,1.92,-4.67,1.8,1.96,-4.7,0.33,1.92,-4.57,0.42,1.72,-4.65,0.45,1.84,-4.5,0.33,2.08,-4.8,0.24,2.12,-4.64,0.2,2.2,-4.75,0.5,1.52,-5.44,0.36,1.84,-5.05,0.5,2.28,-5.25,0.96,1.84,-5.61,1.33,1.96,-5.4,1.41,1.6,-5.49,1.41,1.6,-5.49,1.07,1.4,-5.69,0.96,1.84,-5.61,0.96,1.84,-5.61,1.09,2.2,-5.44,1.33,1.96,-5.4,1.38,2.32,-5.25,1.5,2.4,-5.15,1.62,2.04,-5.08,1.71,2,-4.71,1.68,1.92,-4.9,1.66,2.08,-4.75,1.71,2,-4.71,1.7,1.92,-4.7,1.64,1.88,-4.77,1.64,2.16,-4.88,1.66,2.12,-4.81,1.68,1.92,-4.9,1.87,1.96,-4.61,1.83,2.04,-4.71,1.9,2.08,-4.65,1.87,1.96,-4.61,1.8,1.96,-4.7,1.83,2.04,-4.71,1.82,1.92,-4.67,1.77,1.96,-4.55,1.81,1.8,-4.63,1.61,1.92,-4.52,1.57,2,-4.51,1.52,1.96,-4.48,1.57,2,-4.51,1.5,2,-4.5,1.52,1.96,-4.48,0.23,1.96,-4.41,0.32,1.92,-4.42,0.31,1.88,-4.39,0.26,1.92,-4.54,0.32,1.92,-4.42,0.23,1.96,-4.41,0.17,1.96,-4.54,0.26,1.92,-4.54,0.23,1.96,-4.41,0.26,1.92,-4.54,0.24,2.12,-4.64,0.33,1.92,-4.57,0.33,1.92,-4.57,0.24,2.12,-4.64,0.33,2.08,-4.8,0.33,2.28,-4.92,0.34,2.2,-5.07,0.33,2.08,-4.8,1.71,2,-4.71,1.64,1.88,-4.77,1.68,1.92,-4.9,1.68,1.92,-4.9,1.66,2.12,-4.81,1.66,2.08,-4.75,1.61,1.8,-4.49,1.77,1.96,-4.55,1.61,1.92,-4.52,1.61,1.92,-4.52,1.52,1.96,-4.48,1.51,1.92,-4.49,1.66,2.04,-4.48,1.61,1.92,-4.52,1.77,1.96,-4.55,1.51,1.92,-4.49,1.52,1.96,-4.48,1.58,1.96,-4.4,0.33,1.92,-4.57,0.45,1.84,-4.5,0.4,1.88,-4.47,0.13,2.16,-4.62,0.17,1.96,-4.54,0.07,2,-4.55,1.33,1.96,-5.4,1.62,2.04,-5.08,1.65,1.76,-5.14,1.7,1.92,-4.7,1.81,1.8,-4.63,1.66,1.72,-4.67,1.8,1.96,-4.7,1.82,1.92,-4.67,1.7,1.92,-4.7,1.66,2.04,-4.48,1.57,2,-4.51,1.61,1.92,-4.52,0.31,1.88,-4.39,0.32,1.92,-4.42,0.4,1.88,-4.47,0.4,1.72,-4.39,0.31,1.88,-4.39,0.4,1.88,-4.47,0.52,1.76,-4.48,0.45,1.84,-4.5,0.42,1.72,-4.65,0.26,1.92,-4.54,0.17,1.96,-4.54,0.24,2.12,-4.64,0.36,1.84,-5.05,0.37,1.6,-4.92,0.42,1.6,-4.76,1.7,1.68,-4.89,1.64,1.88,-4.77,1.66,1.72,-4.67,1.82,1.92,-4.67,1.87,1.96,-4.61,1.77,1.96,-4.55,1.74,1.76,-4.49,1.75,1.72,-4.48,1.79,1.72,-4.59,1.61,1.8,-4.49,1.61,1.92,-4.52,1.51,1.92,-4.49,0.45,1.84,-4.5,0.52,1.76,-4.48,0.51,1.8,-4.42,0.51,1.8,-4.42,0.52,1.76,-4.48,0.4,1.72,-4.39,0.92,2.16,-5.49,0.96,1.84,-5.61,0.5,1.52,-5.44,1.65,1.76,-5.14,1.68,1.92,-4.9,1.7,1.68,-4.89,1.68,1.92,-4.9,1.65,1.76,-5.14,1.62,2.04,-5.08,1.7,1.68,-4.89,1.68,1.92,-4.9,1.64,1.88,-4.77,1.51,1.76,-4.45,1.61,1.8,-4.49,1.51,1.92,-4.49,1.61,1.8,-4.49,1.51,1.76,-4.45,1.6,1.72,-4.45,1.44,1.84,-4.47,1.51,1.76,-4.45,1.51,1.92,-4.49,0.57,1.64,-4.53,0.52,1.76,-4.48,0.42,1.72,-4.65,0.42,1.72,-4.65,0.33,1.92,-4.57,0.36,1.84,-5.05,0.36,1.84,-5.05,0.38,1.56,-5.19,0.37,1.6,-4.92,0.44,1.32,-5.37,0.38,1.56,-5.19,0.5,1.52,-5.44,0.5,1.52,-5.44,0.74,1.28,-5.63,0.44,1.32,-5.37,1.67,1.48,-4.83,1.7,1.68,-4.89,1.66,1.72,-4.67,1.81,1.8,-4.63,1.79,1.72,-4.59,1.66,1.72,-4.67,1.61,1.8,-4.49,1.74,1.76,-4.49,1.77,1.96,-4.55,1.58,1.68,-4.43,1.6,1.72,-4.45,1.51,1.76,-4.45,0.4,1.72,-4.39,0.4,1.88,-4.47,0.45,1.84,-4.5,0.31,1.88,-4.39,0.15,1.96,-4.37,0.23,1.96,-4.41,0.51,1.8,-4.42,0.4,1.72,-4.39,0.45,1.84,-4.5,0.42,1.72,-4.65,0.42,1.6,-4.76,0.48,1.56,-4.67,1.7,1.92,-4.7,1.82,1.92,-4.67,1.81,1.8,-4.63,1.64,1.88,-4.77,1.7,1.92,-4.7,1.66,1.72,-4.67,1.76,1.64,-4.51,1.79,1.72,-4.59,1.75,1.72,-4.48,1.72,1.72,-4.47,1.75,1.72,-4.48,1.74,1.76,-4.49,1.72,1.72,-4.47,1.74,1.76,-4.49,1.61,1.8,-4.49,1.63,1.72,-4.45,1.72,1.72,-4.47,1.61,1.8,-4.49,0.52,1.76,-4.48,0.58,1.68,-4.44,0.4,1.72,-4.39,0.58,1.68,-4.44,0.52,1.76,-4.48,0.57,1.64,-4.53,0.74,1.28,-5.63,0.5,1.52,-5.44,0.96,1.84,-5.61,1.58,1.68,-4.43,1.6,1.56,-4.42,1.7,1.6,-4.45,1.52,1.64,-4.4,1.58,1.68,-4.43,1.51,1.76,-4.45,0.58,1.68,-4.44,0.59,1.64,-4.43,0.51,1.6,-4.42,0.59,1.64,-4.43,0.58,1.68,-4.44,0.57,1.64,-4.53,1.64,1.64,-5.21,1.41,1.6,-5.49,1.33,1.96,-5.4,1.74,1.76,-4.49,1.79,1.72,-4.59,1.81,1.8,-4.63,1.74,1.76,-4.49,1.81,1.8,-4.63,1.77,1.96,-4.55,1.72,1.68,-4.47,1.75,1.72,-4.48,1.72,1.72,-4.47,1.72,1.68,-4.47,1.58,1.68,-4.43,1.59,1.64,-4.42,1.72,1.68,-4.47,1.6,1.72,-4.45,1.58,1.68,-4.43,1.7,1.6,-4.45,1.76,1.64,-4.51,1.72,1.68,-4.47,0.51,1.6,-4.42,0.4,1.72,-4.39,0.58,1.68,-4.44,0.61,1.6,-4.45,0.59,1.64,-4.43,0.57,1.64,-4.53,0.42,1.6,-4.76,0.37,1.6,-4.92,0.41,1.52,-4.81,1.65,1.76,-5.14,1.64,1.64,-5.21,1.33,1.96,-5.4,1.74,1.56,-4.53,1.61,1.52,-4.67,1.66,1.72,-4.67,1.72,1.68,-4.47,1.76,1.64,-4.51,1.75,1.72,-4.48,1.7,1.6,-4.45,1.72,1.68,-4.47,1.59,1.64,-4.42,0.61,1.6,-4.45,0.58,1.56,-4.43,0.51,1.6,-4.42,0.61,1.6,-4.45,0.51,1.6,-4.42,0.59,1.64,-4.43,0.59,1.56,-4.5,0.61,1.6,-4.45,0.57,1.64,-4.53,0.55,1.56,-4.58,0.59,1.56,-4.5,0.57,1.64,-4.53,0.55,1.56,-4.58,0.57,1.64,-4.53,0.42,1.72,-4.65,0.48,1.56,-4.67,0.55,1.56,-4.58,0.42,1.72,-4.65,0.44,1.36,-4.95,0.43,1.44,-4.79,0.41,1.52,-4.81,0.64,2.28,-5.4,0.92,2.16,-5.49,0.5,1.52,-5.44,1.7,1.6,-4.45,1.71,1.52,-4.48,1.74,1.56,-4.53,1.6,1.56,-4.42,1.52,1.64,-4.4,1.49,1.6,-4.39,1.58,1.68,-4.43,1.52,1.64,-4.4,1.6,1.56,-4.42,1.59,1.52,-4.42,1.6,1.56,-4.42,1.49,1.6,-4.39,1.59,1.52,-4.42,1.49,1.6,-4.39,1.43,1.52,-4.44,0.54,1.48,-4.43,0.67,1.48,-4.48,0.66,1.44,-4.48,0.59,1.56,-4.5,0.58,1.56,-4.43,0.61,1.6,-4.45,0.64,1.44,-4.54,0.59,1.56,-4.5,0.55,1.56,-4.58,0.49,1.52,-4.7,0.48,1.56,-4.67,0.42,1.6,-4.76,0.41,1.52,-4.81,0.49,1.52,-4.7,0.42,1.6,-4.76,0.5,1.52,-5.44,0.38,1.56,-5.19,0.36,1.84,-5.05,1.64,1.64,-5.21,1.68,1.48,-5.23,1.41,1.6,-5.49,1.67,1.48,-4.83,1.66,1.72,-4.67,1.61,1.52,-4.67,1.76,1.64,-4.51,1.74,1.56,-4.53,1.66,1.72,-4.67,1.7,1.6,-4.45,1.74,1.56,-4.53,1.76,1.64,-4.51,1.6,1.56,-4.42,1.71,1.52,-4.48,1.7,1.6,-4.45,0.52,1.28,-4.45,0.54,1.48,-4.43,0.61,1.4,-4.45,0.54,1.48,-4.43,0.51,1.6,-4.42,0.58,1.56,-4.43,0.54,1.48,-4.43,0.66,1.44,-4.48,0.61,1.4,-4.45,0.67,1.48,-4.48,0.59,1.56,-4.5,0.64,1.44,-4.54,0.44,1.36,-4.95,0.41,1.52,-4.81,0.37,1.6,-4.92,0.82,0.92,-5.76,0.74,1.28,-5.63,1.03,1.28,-5.72,1.7,1.68,-4.89,1.64,1.64,-5.21,1.65,1.76,-5.14,1.56,1.48,-4.71,1.67,1.48,-4.83,1.61,1.52,-4.67,1.56,1.48,-4.71,1.61,1.52,-4.67,1.58,1.48,-4.69,1.58,1.44,-4.72,1.58,1.48,-4.69,1.61,1.36,-4.57,0.51,1.32,-4.76,0.5,1.36,-4.74,0.43,1.44,-4.79,1.7,1.68,-4.89,1.67,1.48,-4.83,1.73,1.44,-4.93,1.73,1.44,-4.93,1.73,1.16,-5.01,1.68,1.48,-5.23,1.58,1.44,-4.72,1.56,1.48,-4.71,1.58,1.48,-4.69,1.66,1.44,-4.56,1.58,1.48,-4.69,1.61,1.52,-4.67,1.58,1.48,-4.69,1.66,1.44,-4.56,1.61,1.36,-4.57,1.76,1.64,-4.51,1.66,1.72,-4.67,1.79,1.72,-4.59,1.74,1.56,-4.53,1.66,1.44,-4.56,1.61,1.52,-4.67,1.61,1.36,-4.57,1.6,1.52,-4.42,1.59,1.36,-4.42,1.6,1.56,-4.42,1.6,1.52,-4.42,1.71,1.52,-4.48,0.52,1.28,-4.45,0.61,1.4,-4.45,0.61,1.32,-4.45,0.54,1.48,-4.43,0.58,1.56,-4.43,0.67,1.48,-4.48,0.64,1.44,-4.54,0.66,1.44,-4.48,0.67,1.48,-4.48,0.51,1.44,-4.69,0.5,1.36,-4.74,0.57,1.36,-4.64,0.51,1.44,-4.69,0.43,1.44,-4.79,0.5,1.36,-4.74,0.36,1.84,-5.05,0.42,1.6,-4.76,0.42,1.72,-4.65,1.41,1.6,-5.49,1.39,1.28,-5.51,1.07,1.4,-5.69,0.96,1.84,-5.61,0.92,2.16,-5.49,1.09,2.2,-5.44,1.67,1.48,-4.83,1.67,1.44,-4.82,1.73,1.44,-4.93,1.62,1.36,-4.75,1.67,1.44,-4.82,1.58,1.44,-4.72,1.66,1.44,-4.56,1.71,1.52,-4.48,1.6,1.52,-4.42,0.58,1.56,-4.43,0.59,1.56,-4.5,0.67,1.48,-4.48,0.66,1.44,-4.48,0.69,1.4,-4.5,0.61,1.4,-4.45,0.69,1.4,-4.5,0.72,1.36,-4.44,0.61,1.4,-4.45,0.38,1.56,-5.19,0.44,1.32,-5.37,0.44,1.36,-4.95,0.49,1.08,-4.94,0.45,1.2,-4.9,0.44,1.32,-5.37,0.45,1.2,-4.9,0.44,1.36,-4.95,0.44,1.32,-5.37,1.07,1.4,-5.69,1.03,1.28,-5.72,0.74,1.28,-5.63,1.7,1.68,-4.89,1.73,1.44,-4.93,1.64,1.64,-5.21,1.58,1.44,-4.72,1.61,1.36,-4.57,1.62,1.36,-4.75,1.61,1.36,-4.57,1.51,1.32,-4.64,1.62,1.36,-4.75,1.61,1.36,-4.57,1.59,1.36,-4.42,1.59,1.32,-4.46,1.74,1.56,-4.53,1.71,1.52,-4.48,1.66,1.44,-4.56,0.72,1.32,-4.44,0.66,1.32,-4.44,0.72,1.36,-4.44,0.67,1.32,-4.55,0.72,1.36,-4.44,0.69,1.4,-4.5,0.67,1.32,-4.55,0.72,1.32,-4.44,0.72,1.36,-4.44,0.5,1.2,-4.81,0.55,1.28,-4.73,0.51,1.32,-4.76,0.5,1.2,-4.81,0.58,1.24,-4.75,0.55,1.28,-4.73,0.38,1.56,-5.19,0.44,1.36,-4.95,0.37,1.6,-4.92,1.73,1.44,-4.93,1.67,1.44,-4.82,1.7,1.24,-4.84,1.7,1.24,-4.84,1.62,1.36,-4.75,1.52,1.28,-4.66,1.61,1.36,-4.57,1.66,1.44,-4.56,1.6,1.52,-4.42,1.59,1.32,-4.46,1.59,1.36,-4.42,1.55,1.32,-4.42,1.49,1.32,-4.42,1.55,1.32,-4.42,1.59,1.36,-4.42,0.67,1.32,-4.55,0.59,1.32,-4.66,0.62,1.28,-4.63,0.55,1.28,-4.73,0.62,1.28,-4.63,0.59,1.32,-4.66,0.59,1.32,-4.66,0.51,1.32,-4.76,0.55,1.28,-4.73,0.45,1.2,-4.9,0.5,1.2,-4.81,0.51,1.32,-4.76,1.68,1.48,-5.23,1.39,1.28,-5.51,1.41,1.6,-5.49,1.73,1.44,-4.93,1.7,1.24,-4.84,1.73,1.16,-5.01,1.51,1.32,-4.64,1.52,1.28,-4.66,1.62,1.36,-4.75,1.53,1.28,-4.61,1.52,1.28,-4.66,1.51,1.32,-4.64,1.52,1.2,-4.57,1.57,1.28,-4.47,1.52,1.24,-4.44,1.61,1.36,-4.57,1.53,1.28,-4.61,1.51,1.32,-4.64,0.51,1.32,-4.76,0.43,1.44,-4.79,0.44,1.36,-4.95,0.74,1.28,-5.63,0.51,1.04,-5.47,0.44,1.32,-5.37,1.68,1.48,-5.23,1.66,1.16,-5.4,1.39,1.28,-5.51,1.73,1.44,-4.93,1.68,1.48,-5.23,1.64,1.64,-5.21,1.67,1.44,-4.82,1.62,1.36,-4.75,1.7,1.24,-4.84,1.57,1.28,-4.47,1.61,1.36,-4.57,1.59,1.32,-4.46,1.53,1.28,-4.61,1.61,1.36,-4.57,1.57,1.28,-4.47,1.51,1.32,-4.38,1.5,1.28,-4.42,1.57,1.28,-4.47,1.52,1.24,-4.44,1.5,1.28,-4.42,1.42,1.24,-4.41,0.45,1.2,-4.9,0.51,1.32,-4.76,0.44,1.36,-4.95,1.52,1.2,-4.64,1.7,1.24,-4.84,1.52,1.28,-4.66,1.52,1.2,-4.64,1.52,1.2,-4.57,1.47,1.12,-4.57,1.52,1.2,-4.57,1.52,1.2,-4.64,1.53,1.28,-4.61,1.52,1.2,-4.57,1.52,1.24,-4.44,1.51,1.2,-4.45,1.5,1.28,-4.42,1.52,1.24,-4.44,1.57,1.28,-4.47,1.46,1.16,-4.45,1.43,1.12,-4.48,1.47,1.12,-4.57,1.52,1.2,-4.57,1.53,1.28,-4.61,1.57,1.28,-4.47,1.46,1.16,-4.45,1.51,1.2,-4.45,1.41,1.2,-4.35,1.07,1.4,-5.69,0.74,1.28,-5.63,0.96,1.84,-5.61,1.73,1.16,-5.01,1.7,1.24,-4.84,1.62,1,-4.75,1.52,1.2,-4.64,1.52,1.28,-4.66,1.53,1.28,-4.61,1.47,1.12,-4.57,1.52,1.2,-4.57,1.46,1.16,-4.45,1.51,1.2,-4.45,1.46,1.16,-4.45,1.52,1.2,-4.57,1.7,1.24,-4.84,1.52,1.2,-4.64,1.62,1,-4.75,1.43,1.12,-4.48,1.34,1.12,-4.34,1.34,1.08,-4.44,0.49,1.08,-4.94,0.44,1.32,-5.37,0.55,0.88,-5.05,1.25,0.96,-5.67,1.03,1.28,-5.72,1.39,1.28,-5.51,1.73,1.16,-5.01,1.66,1.16,-5.4,1.68,1.48,-5.23,1.47,1.12,-4.57,1.62,1,-4.75,1.52,1.2,-4.64,1.03,1.28,-5.72,1.07,1.4,-5.69,1.39,1.28,-5.51])

IndexedFaceSet461.setCoord(Coordinate462)

Shape457.setGeometry(IndexedFaceSet461)

Transform456.addChildren(Shape457)

fieldValue455.addChildren(Transform456)

ProtoInstance453.addFieldValue(fieldValue455)

fieldValue452.addChildren(ProtoInstance453)
ProtoInstance463 = ProtoInstance()
ProtoInstance463.setName("Joint")
ProtoInstance463.setDEF("Allen_hanim_r_elbow")
fieldValue464 = fieldValue()
fieldValue464.setName("name")
fieldValue464.setValue("r_elbow")

ProtoInstance463.addFieldValue(fieldValue464)
fieldValue465 = fieldValue()
fieldValue465.setName("center")
fieldValue465.setValue("-0.192 1.07 -0.0498")

ProtoInstance463.addFieldValue(fieldValue465)
fieldValue466 = fieldValue()
fieldValue466.setName("children")
ProtoInstance467 = ProtoInstance()
ProtoInstance467.setName("Segment")
ProtoInstance467.setDEF("Allen_hanim_r_forearm")
fieldValue468 = fieldValue()
fieldValue468.setName("name")
fieldValue468.setValue("r_forearm")

ProtoInstance467.addFieldValue(fieldValue468)
fieldValue469 = fieldValue()
fieldValue469.setName("children")
Transform470 = Transform()
Transform470.setDEF("Allen_r_forearm_adjust")
Transform470.setCenter([0.7641,1.01,-0.07438])
Transform470.setRotation([0,1,0,1.570796])
Transform470.setScale([0.1,0.1,0.1])
Shape471 = Shape()
Appearance472 = Appearance()
Material473 = Material()
Material473.setUSE("Skin_Color")

Appearance472.setMaterial(Material473)
ImageTexture474 = ImageTexture()
ImageTexture474.setUSE("camo")

Appearance472.setTexture(ImageTexture474)

Shape471.setAppearance(Appearance472)
IndexedFaceSet475 = IndexedFaceSet()
IndexedFaceSet475.setCoordIndex([0,1,2,-1,3,4,5,-1,6,7,8,-1,9,10,11,-1,12,13,14,-1,15,16,17,-1,18,19,20,-1,21,22,23,-1,24,25,26,-1,27,28,29,-1,30,31,32,-1,33,34,35,-1,36,37,38,-1,39,40,41,-1,42,43,44,-1,45,46,47,-1,48,49,50,-1,51,52,53,-1,54,55,56,-1,57,58,59,-1,60,61,62,-1,63,64,65,-1,66,67,68,-1,69,70,71,-1,72,73,74,-1,75,76,77,-1,78,79,80,-1,81,82,83,-1,84,85,86,-1,87,88,89,-1,90,91,92,-1,93,94,95,-1,96,97,98,-1,99,100,101,-1,102,103,104,-1,105,106,107,-1,108,109,110,-1,111,112,113,-1,114,115,116,-1,117,118,119,-1,120,121,122,-1,123,124,125,-1,126,127,128,-1,129,130,131,-1,132,133,134,-1,135,136,137,-1,138,139,140,-1,141,142,143,-1,144,145,146,-1,147,148,149,-1,150,151,152,-1,153,154,155,-1,156,157,158,-1,159,160,161,-1,162,163,164,-1,165,166,167,-1,168,169,170,-1,171,172,173,-1,174,175,176,-1,177,178,179,-1,180,181,182,-1,183,184,185,-1,186,187,188,-1,189,190,191,-1,192,193,194,-1,195,196,197,-1,198,199,200,-1,201,202,203,-1,204,205,206,-1,207,208,209,-1,210,211,212,-1,213,214,215,-1,216,217,218,-1,219,220,221,-1,222,223,224,-1,225,226,227,-1,228,229,230,-1,231,232,233,-1,234,235,236,-1,237,238,239,-1,240,241,242,-1,243,244,245,-1,246,247,248,-1,249,250,251,-1,252,253,254,-1,255,256,257,-1,258,259,260,-1,261,262,263,-1,264,265,266,-1,267,268,269,-1,270,271,272,-1,273,274,275,-1,276,277,278,-1,279,280,281,-1,282,283,284,-1,285,286,287,-1,288,289,290,-1,291,292,293,-1,294,295,296,-1,297,298,299,-1,300,301,302,-1,63,65,60,-1,36,40,37,-1,40,39,37,-1,39,43,37,-1,43,42,37,-1,48,51,49,-1,60,65,61,-1,49,51,50,-1,51,53,50,-1,50,53,48,-1,48,53,47,-1,47,53,45,-1,45,53,42,-1,42,53,37,-1,53,54,37,-1,54,56,37,-1,65,37,61,-1,37,56,61,-1,62,61,60,-1,59,58,56,-1,56,58,61,-1,60,61,58,-1,303,304,305,-1,306,307,308,-1,309,310,311,-1,312,313,314,-1,315,316,317,-1,318,319,320,-1,321,322,323,-1,324,325,326,-1,327,328,329,-1,330,331,332,-1,333,334,335,-1,336,337,338,-1,339,340,341,-1,342,343,344,-1,345,346,347,-1,348,349,350,-1,351,352,353,-1,354,355,356,-1,357,358,359,-1,360,361,362,-1,363,364,365,-1,366,367,368,-1,369,370,371,-1,372,373,374,-1,375,376,377,-1,378,379,380,-1,381,382,383,-1,384,385,386,-1,387,388,389,-1,390,391,392,-1,393,394,395,-1,396,397,398,-1,399,400,401,-1,402,403,404,-1,405,406,407,-1,408,409,410,-1,411,412,413,-1,414,415,416,-1,417,418,419,-1,420,421,422,-1,423,424,425,-1,426,427,428,-1,429,430,431,-1,432,433,434,-1,435,436,437,-1,438,439,440,-1,441,442,443,-1,444,445,446,-1,447,448,449,-1,450,451,452,-1,453,454,455,-1,456,457,458,-1,459,460,461,-1,462,463,464,-1,465,466,467,-1,468,469,470,-1,471,472,473,-1,474,475,476,-1,477,478,479,-1,480,481,482,-1,483,484,485,-1,486,487,488,-1,489,490,491,-1,492,493,494,-1,495,496,497,-1,498,499,500,-1,501,502,503,-1,504,505,506,-1,507,508,509,-1,510,511,512,-1,513,514,515,-1,516,517,518,-1,519,520,521,-1,522,523,524,-1,525,526,527,-1,528,529,530,-1,531,532,533,-1,534,535,536,-1,537,538,539,-1,540,541,542,-1,543,544,545,-1,546,547,548,-1,549,550,551,-1,552,553,554,-1,555,556,557,-1,558,559,560,-1,561,562,563,-1,564,565,566,-1,567,568,569,-1,570,571,572,-1,573,574,575,-1,576,577,578,-1,579,580,581,-1,582,583,584,-1,585,586,587,-1,588,589,590,-1,591,592,593,-1,594,595,596,-1,597,598,599,-1,600,601,602,-1,603,604,605,-1,606,607,608,-1,609,610,611,-1,612,613,614,-1,615,616,617,-1,618,619,620,-1,621,622,623,-1,624,625,626,-1,627,628,629,-1,630,631,632,-1,633,634,635,-1,636,637,638,-1,639,640,641,-1,642,643,644,-1,645,646,647,-1,648,649,650,-1,651,652,653,-1,654,655,656,-1,657,658,659,-1,660,661,662,-1,663,664,665,-1,666,667,668,-1,669,670,671,-1,672,673,674,-1,675,676,677,-1,678,679,680,-1,681,682,683,-1,684,685,686,-1,687,688,689,-1,690,691,692,-1,693,694,695,-1,696,697,698,-1,699,700,701,-1,702,703,704,-1,705,706,707,-1,708,709,710,-1,711,712,713,-1,714,715,716,-1,717,718,719,-1,720,721,722,-1,723,724,725,-1,726,727,728,-1,729,730,731,-1,732,733,734,-1,735,736,737,-1,738,739,740,-1,741,742,743,-1,744,745,746,-1,747,748,749,-1,750,751,752,-1,753,754,755,-1,756,757,758,-1,759,760,761,-1,762,763,764,-1,765,766,767,-1,768,769,770,-1,771,772,773,-1,774,775,776,-1,777,778,779,-1,780,781,782,-1,783,784,785,-1,786,787,788,-1,789,790,791,-1,792,793,794,-1,795,796,797,-1,798,799,800,-1,801,802,803,-1,804,805,806,-1,807,808,809,-1,810,811,812,-1,813,814,815,-1,816,817,818,-1,819,820,821,-1,822,823,824,-1,825,826,827,-1,828,829,830,-1,831,832,833,-1,834,835,836,-1,837,838,839,-1,840,841,842,-1,843,844,845,-1,846,847,848,-1,849,850,851,-1,852,853,854,-1,855,856,857,-1,858,859,860,-1,861,862,863,-1,864,865,866,-1,867,868,869,-1,870,871,872,-1,873,874,875,-1,876,877,878,-1,879,880,881,-1,882,883,884,-1,885,886,887,-1,888,889,890,-1,891,892,893,-1,894,895,896,-1,897,898,899,-1,900,901,902,-1,903,904,905,-1,906,907,908,-1,909,910,911,-1,912,913,914,-1,915,916,917,-1,918,919,920,-1,921,922,923,-1,924,925,926,-1,927,928,929,-1,930,931,932,-1,933,934,935,-1,936,937,938,-1,939,940,941,-1,942,943,944,-1,945,946,947,-1,948,949,950,-1,951,952,953,-1,954,955,956,-1,957,958,959,-1,960,961,962,-1,963,964,965,-1,966,967,968,-1,969,970,971,-1,972,973,974,-1,975,976,977,-1,978,979,980,-1,981,982,983,-1,984,985,986,-1,987,988,989,-1,990,991,992,-1,993,994,995,-1,996,997,998,-1,999,1000,1001,-1,1002,1003,1004,-1,1005,1006,1007,-1,1008,1009,1010,-1,1011,1012,1013,-1,1014,1015,1016,-1,1017,1018,1019,-1,1020,1021,1022,-1,1023,1024,1025,-1,1026,1027,1028,-1,1029,1030,1031,-1,1032,1033,1034,-1,1035,1036,1037,-1,1038,1039,1040,-1,1041,1042,1043,-1,1044,1045,1046,-1,1047,1048,1049,-1,1050,1051,1052,-1,1053,1054,1055,-1,1056,1057,1058,-1,1059,1060,1061,-1,1062,1063,1064,-1,1065,1066,1067,-1,1068,1069,1070,-1,1071,1072,1073,-1,1074,1075,1076,-1,1077,1078,1079,-1,1080,1081,1082,-1,1083,1084,1085,-1,1086,1087,1088,-1,1089,1090,1091,-1,1092,1093,1094,-1,1095,1096,1097,-1,1098,1099,1100,-1,1101,1102,1103,-1,1104,1105,1106,-1,1107,1108,1109,-1,1110,1111,1112,-1,1113,1114,1115,-1,1116,1117,1118,-1,1119,1120,1121,-1,1122,1123,1124,-1,1125,1126,1127,-1,1128,1129,1130,-1,1131,1132,1133,-1,1134,1135,1136,-1,1137,1138,1139,-1,1140,1141,1142,-1,1143,1144,1145,-1,1146,1147,1148,-1,1149,1150,1151,-1,1152,1153,1154,-1,1155,1156,1157,-1,1158,1159,1160,-1,1161,1162,1163,-1,1164,1165,1166,-1,1167,1168,1169,-1,1170,1171,1172,-1,1173,1174,1175,-1,1176,1177,1178,-1,1179,1180,1181,-1,1182,1183,1184,-1,1185,1186,1187,-1,1188,1189,1190,-1,1191,1192,1193,-1,1194,1195,1196,-1,1197,1198,1199,-1,1200,1201,1202,-1,1203,1204,1205,-1,1206,1207,1208,-1,1209,1210,1211,-1,1212,1213,1214,-1,1215,1216,1217,-1,1218,1219,1220,-1,1221,1222,1223,-1,1224,1225,1226,-1,1227,1228,1229,-1,1230,1231,1232,-1,1233,1234,1235,-1,1236,1237,1238,-1,1239,1240,1241,-1,1242,1243,1244,-1,1245,1246,1247,-1,1248,1249,1250,-1,1251,1252,1253,-1,1254,1255,1256,-1,1257,1258,1259,-1,1260,1261,1262,-1,1263,1264,1265,-1,1266,1267,1268,-1,1269,1270,1271,-1,1272,1273,1274,-1,1275,1276,1277,-1,1278,1279,1280,-1,1281,1282,1283,-1,1284,1285,1286,-1,1287,1288,1289,-1,1290,1291,1292,-1,1293,1294,1295,-1,1296,1297,1298,-1,1299,1300,1301,-1,1302,1303,1304,-1,1305,1306,1307,-1,1308,1309,1310,-1,1311,1312,1313,-1,1314,1315,1316,-1,1317,1318,1319,-1,1320,1321,1322,-1,1323,1324,1325,-1,1326,1327,1328,-1,1329,1330,1331,-1,1332,1333,1334,-1,1335,1336,1337,-1,1338,1339,1340,-1,1341,1342,1343,-1,1344,1345,1346,-1,1347,1348,1349,-1,1350,1351,1352,-1,1353,1354,1355,-1,1356,1357,1358,-1,1359,1360,1361,-1,1362,1363,1364,-1,1365,1366,1367,-1,1368,1369,1370,-1,1371,1372,1373,-1,1374,1375,1376,-1,1377,1378,1379,-1,1380,1381,1382,-1,1383,1384,1385,-1,1386,1387,1388,-1,1389,1390,1391,-1,1392,1393,1394,-1,1395,1396,1397,-1,1398,1399,1400,-1,1401,1402,1403,-1,1404,1405,1406,-1,1407,1408,1409,-1,1410,1411,1412,-1,1413,1414,1415,-1,1416,1417,1418,-1,1419,1420,1421,-1,1422,1423,1424,-1,1425,1426,1427,-1,1428,1429,1430,-1,1431,1432,1433,-1,1434,1435,1436,-1,1437,1438,1439,-1,1440,1441,1442,-1,1443,1444,1445,-1,1446,1447,1448,-1,1449,1450,1451,-1,1452,1453,1454,-1,1455,1456,1457,-1,1458,1459,1460,-1,1461,1462,1463,-1,1464,1465,1466,-1,1467,1468,1469,-1,1470,1471,1472,-1,1473,1474,1475,-1,1476,1477,1478,-1,1479,1480,1481,-1,1482,1483,1484,-1,1485,1486,1487,-1,1488,1489,1490,-1,1491,1492,1493,-1,1494,1495,1496,-1,1497,1498,1499,-1,1500,1501,1502,-1,1503,1504,1505,-1,1506,1507,1508,-1,1509,1510,1511,-1,1512,1513,1514,-1,1515,1516,1517,-1,1518,1519,1520,-1,1521,1522,1523,-1,1524,1525,1526,-1,1527,1528,1529,-1,1530,1531,1532,-1,1533,1534,1535,-1,1536,1537,1538,-1,1539,1540,1541,-1,1542,1543,1544,-1,1545,1546,1547,-1,1548,1549,1550,-1,1551,1552,1553,-1,1554,1555,1556,-1,1557,1558,1559,-1,1560,1561,1562,-1,1563,1564,1565,-1,1566,1567,1568,-1,1569,1570,1571,-1,1572,1573,1574,-1,1575,1576,1577,-1,1578,1579,1580,-1,1581,1582,1583,-1,1584,1585,1586,-1,1587,1588,1589,-1,1590,1591,1592,-1,1593,1594,1595,-1,1596,1597,1598,-1,1599,1600,1601,-1,1602,1603,1604,-1,1605,1606,1607,-1,1608,1609,1610,-1,1611,1612,1613,-1,1614,1615,1616,-1,1617,1618,1619,-1,1620,1621,1622,-1,1623,1624,1625,-1,1626,1627,1628,-1,1629,1630,1631,-1,1632,1633,1634,-1,1635,1636,1637,-1,1638,1639,1640,-1,1641,1642,1643,-1,1644,1645,1646,-1,1647,1648,1649,-1,1650,1651,1652,-1,1653,1654,1655,-1,1656,1657,1658,-1,1659,1660,1661,-1,1662,1663,1664,-1,1665,1666,1667,-1,1668,1669,1670,-1,1671,1672,1673,-1,1674,1675,1676,-1,1677,1678,1679,-1,1680,1681,1682,-1,1683,1684,1685,-1,1686,1687,1688,-1,1689,1690,1691,-1,1692,1693,1694,-1,1695,1696,1697,-1,1698,1699,1700,-1,1701,1702,1703,-1,1704,1705,1706,-1,1707,1708,1709,-1,1710,1711,1712,-1,1713,1714,1715,-1,1716,1717,1718,-1,1719,1720,1721,-1])
IndexedFaceSet475.setCreaseAngle(1.73)
Coordinate476 = Coordinate()
Coordinate476.setPoint([0.51,1.04,-10.46,0.45,0.72,-10.27,0.55,0.88,-10.04,1.1,0.96,-10.77,0.82,0.92,-10.75,1.03,1.28,-10.71,1.39,1.28,-10.5,1.4,0.8,-10.53,1.25,0.96,-10.65,1.66,0.88,-10.09,1.73,1.16,-10,1.62,1,-9.74,1.26,0.68,-9.65,1.54,0.72,-9.88,1.4,0.96,-9.53,1.39,1.28,-10.5,1.66,1.16,-10.39,1.4,0.8,-10.53,1.66,0.88,-10.09,1.62,1,-9.74,1.54,0.72,-9.88,0.56,1.08,-9.83,0.59,0.92,-9.84,0.6,0.96,-9.79,0.56,1.08,-9.83,0.55,0.88,-10.04,0.59,0.92,-9.84,0.51,1.04,-10.46,0.74,1.28,-10.62,0.82,0.92,-10.75,0.44,1.32,-10.36,0.51,1.04,-10.46,0.55,0.88,-10.04,1.43,1.12,-9.47,1.34,1.08,-9.42,1.4,0.96,-9.53,0.7,0.96,-9.67,0.72,1.04,-9.62,0.68,1.08,-9.69,1.34,1.08,-9.42,1.3,1,-9.46,1.4,0.96,-9.53,1.29,0.96,-9.47,1.19,0.76,-9.59,1.4,0.96,-9.53,1.19,0.6,-9.59,1.26,0.68,-9.65,1.15,0.72,-9.66,1.17,0.56,-9.57,1.2,0.56,-9.58,1.19,0.6,-9.59,1.2,0.56,-9.58,1.27,0.56,-9.6,1.19,0.6,-9.59,1.21,0.48,-9.57,1.24,0.48,-9.59,1.2,0.56,-9.58,1.39,0.48,-9.62,1.24,0.48,-9.59,1.25,0.44,-9.58,1.29,0.4,-9.59,1.39,0.48,-9.62,1.25,0.44,-9.58,1.1,0.32,-9.66,1.15,0.28,-9.66,1.29,0.4,-9.59,1.1,0.28,-9.67,1.15,0.28,-9.66,1.1,0.32,-9.66,1.15,0.28,-9.66,1.32,0.32,-9.64,1.29,0.4,-9.59,1.14,0.24,-9.67,1.18,0.24,-9.67,1.15,0.28,-9.66,1.15,0.28,-9.66,1.18,0.24,-9.67,1.32,0.32,-9.64,1.27,0.2,-9.68,1.18,0.24,-9.67,1.19,0.2,-9.67,1.27,0.2,-9.68,1.4,0.2,-9.72,1.32,0.32,-9.64,1.24,0.16,-9.7,1.28,0.16,-9.71,1.27,0.2,-9.68,1.4,0.2,-9.72,1.28,0.16,-9.71,1.29,0.08,-9.78,1.29,0.08,-9.78,1.16,0.08,-9.81,1.13,-0.04,-9.83,1.12,0.08,-9.81,1.16,0.08,-9.81,1.09,0.12,-9.83,1.09,0.12,-9.83,0.96,0.12,-9.81,0.98,0.04,-9.8,1.12,0.08,-9.81,1.09,0.12,-9.83,0.98,0.04,-9.8,1.02,0,-9.81,1.12,0.08,-9.81,0.98,0.04,-9.8,0.93,-0.04,-9.84,0.96,-0.08,-9.86,1.02,0,-9.81,0.93,-0.08,-9.84,0.96,-0.08,-9.86,0.93,-0.04,-9.84,1,-0.16,-9.86,1.01,-0.08,-9.86,0.96,-0.08,-9.86,1,-0.16,-9.86,0.96,-0.08,-9.86,0.94,-0.12,-9.88,1,-0.16,-9.86,1.07,-0.28,-9.85,1.13,-0.04,-9.83,0.94,-0.2,-9.87,0.96,-0.28,-9.86,1,-0.28,-9.86,1.02,-0.36,-9.85,1.07,-0.28,-9.85,1,-0.28,-9.86,1.02,-0.36,-9.85,1.11,-0.36,-9.85,1.07,-0.28,-9.85,1.11,-0.36,-9.85,1.13,-0.44,-9.87,1.25,-0.32,-9.81,1.08,-0.44,-9.88,1.13,-0.44,-9.87,1.11,-0.36,-9.85,1.22,-0.48,-9.87,1.13,-0.44,-9.87,1.13,-0.48,-9.87,1.38,-0.6,-9.94,1.37,-0.4,-9.83,1.22,-0.48,-9.87,1.18,-0.56,-9.91,1.22,-0.56,-9.92,1.22,-0.48,-9.87,1.22,-0.56,-9.92,1.38,-0.6,-9.94,1.22,-0.48,-9.87,1.1,-0.72,-10.1,1.34,-0.72,-10.05,1.22,-0.56,-9.92,1.02,-0.72,-10.13,1,-0.96,-10.22,1.1,-0.72,-10.1,0.91,-0.68,-10.14,0.91,-0.72,-10.14,1.02,-0.72,-10.13,0.76,-0.8,-10.15,0.79,-0.8,-10.16,0.84,-0.76,-10.15,0.71,-0.92,-10.19,0.78,-0.92,-10.2,0.79,-0.8,-10.16,0.74,-1.08,-10.2,0.79,-1.08,-10.24,0.78,-0.92,-10.2,0.86,-1.12,-10.25,0.79,-1.08,-10.24,0.78,-1.12,-10.24,1,-0.96,-10.22,0.86,-1.12,-10.25,1.11,-1.12,-10.28,0.86,-1.12,-10.25,0.89,-1.2,-10.35,1.1,-1.16,-10.33,0.68,-1.2,-10.37,0.81,-1.28,-10.42,0.89,-1.2,-10.35,0.68,-1.2,-10.37,0.68,-1.28,-10.37,0.81,-1.28,-10.42,0.84,-1.32,-10.32,0.74,-1.32,-10.24,0.63,-1.44,-10.25,0.59,-1.52,-10.29,0.63,-1.52,-10.3,0.63,-1.44,-10.25,0.48,-1.52,-10.29,0.46,-1.36,-10.27,0.23,-1.64,-10.37,0.46,-1.36,-10.27,0.49,-1.28,-10.25,0.35,-1.24,-10.34,0.6,-1.24,-10.34,0.51,-1.2,-10.34,0.49,-1.28,-10.25,0.58,-1.16,-10.28,0.56,-1.16,-10.31,0.62,-1.2,-10.38,0.56,-1.16,-10.31,0.58,-1.16,-10.28,0.54,-1.12,-10.25,0.56,-1.16,-10.31,0.54,-1.12,-10.25,0.48,-1.12,-10.29,0.36,-1.04,-10.31,0.38,-0.96,-10.36,0.35,-1.16,-10.42,0.36,-1.04,-10.31,0.39,-1,-10.29,0.38,-0.96,-10.36,0.29,-1,-10.52,0.38,-0.96,-10.36,0.41,-0.88,-10.38,0.39,-0.8,-10.33,0.33,-0.68,-10.44,0.41,-0.88,-10.38,0.33,-0.68,-10.44,0.44,-0.72,-10.32,0.41,-0.68,-10.31,0.41,-0.68,-10.31,0.48,-0.6,-10.29,0.38,-0.44,-10.4,0.48,-0.6,-10.29,0.51,-0.56,-10.19,0.47,-0.52,-10.25,0.42,-0.36,-10.31,0.47,-0.52,-10.25,0.47,-0.48,-10.18,0.54,-0.32,-10.08,0.5,-0.24,-10.15,0.47,-0.48,-10.18,0.54,-0.32,-10.08,0.62,-0.32,-9.98,0.56,-0.28,-9.99,0.54,-0.32,-10.08,0.56,-0.28,-9.99,0.57,-0.2,-10.06,0.57,-0.2,-10.06,0.6,-0.16,-10.03,0.59,-0.08,-10.04,0.59,-0.08,-10.04,0.59,-0.04,-10,0.56,0,-10.02,0.56,0.12,-9.99,0.55,0.12,-10.04,0.56,0,-10.02,0.57,0.2,-10.02,0.55,0.2,-10.08,0.5,0.16,-10.08,0.55,0.2,-10.08,0.57,0.2,-10.02,0.59,0.24,-10,0.68,0.32,-9.92,0.71,0.32,-9.86,0.69,0.36,-9.88,0.69,0.36,-9.88,0.62,0.36,-9.97,0.68,0.32,-9.92,0.63,0.48,-9.89,0.59,0.4,-9.96,0.68,0.4,-9.85,0.59,0.4,-9.96,0.63,0.48,-9.89,0.56,0.48,-9.98,0.54,0.56,-10,0.47,0.56,-10.14,0.56,0.48,-9.98,0.47,0.56,-10.14,0.56,0.4,-10.02,0.56,0.48,-9.98,0.47,0.64,-10.18,0.45,0.72,-10.27,0.45,0.6,-10.2,0.45,0.72,-10.27,0.47,0.64,-10.18,0.53,0.68,-10.09,0.47,0.64,-10.18,0.53,0.64,-10.09,0.53,0.68,-10.09,0.45,0.72,-10.27,0.53,0.68,-10.09,0.55,0.88,-10.04,0.62,0.68,-9.97,0.66,0.72,-9.94,0.55,0.88,-10.04,0.66,0.72,-9.94,0.67,0.8,-9.85,0.55,0.88,-10.04,0.84,0.72,-9.63,0.82,0.8,-9.61,0.77,0.72,-9.77,0.82,0.8,-9.61,0.69,0.8,-9.79,0.77,0.72,-9.77,0.67,0.8,-9.85,0.69,0.8,-9.79,0.67,0.84,-9.78,0.69,0.92,-9.72,0.59,0.92,-9.84,0.67,0.84,-9.78,0.8,0.84,-9.59,0.7,0.96,-9.67,0.69,0.92,-9.72,1.25,0.96,-10.65,1.23,0.88,-10.71,1.1,0.96,-10.77,1.23,0.88,-10.71,1.15,0.88,-10.77,1.1,0.96,-10.77,1.47,1.12,-9.55,1.4,0.96,-9.53,1.62,1,-9.74,0.56,1.08,-9.83,0.49,1.08,-9.93,0.55,0.88,-10.04,0.59,0.92,-9.84,0.67,0.8,-9.85,0.67,0.84,-9.78,0.43,0.6,-10.4,0.51,1.04,-10.46,0.6,0.68,-10.66,1.15,0.88,-10.77,1.23,0.88,-10.71,1.24,0.84,-10.72,1.47,1.12,-9.55,1.43,1.12,-9.47,1.4,0.96,-9.53,1.29,0.96,-9.47,1.4,0.96,-9.53,1.3,1,-9.46,1.26,0.84,-10.69,1.24,0.84,-10.72,1.23,0.88,-10.71,1.26,0.84,-10.69,1.25,0.96,-10.65,1.4,0.8,-10.53,1.66,1.16,-10.39,1.62,0.84,-10.36,1.4,0.8,-10.53,1.76,0.88,-10.23,1.62,0.84,-10.36,1.66,1.16,-10.39,1.73,1.16,-10,1.76,0.88,-10.23,1.66,1.16,-10.39,1.66,0.88,-10.09,1.76,0.88,-10.23,1.73,1.16,-10,0.8,0.84,-9.59,0.69,0.92,-9.72,0.67,0.84,-9.78,1.25,0.96,-10.65,1.1,0.96,-10.77,1.03,1.28,-10.71,1.1,0.96,-10.77,1.15,0.88,-10.77,1.08,0.88,-10.83,1.23,0.64,-10.82,0.97,0.72,-10.82,1.08,0.88,-10.83,1.26,0.76,-10.73,1.24,0.84,-10.72,1.26,0.84,-10.69,1.26,0.76,-10.73,1.4,0.8,-10.53,1.41,0.72,-10.55,1.62,0.84,-10.36,1.53,0.72,-10.41,1.4,0.8,-10.53,1.73,0.72,-10.33,1.62,0.84,-10.36,1.76,0.88,-10.23,1.79,0.68,-10.2,1.76,0.88,-10.23,1.66,0.88,-10.09,0.43,0.6,-10.4,0.45,0.72,-10.27,0.51,1.04,-10.46,1.15,0.88,-10.77,1.23,0.64,-10.82,1.08,0.88,-10.83,1.26,0.84,-10.69,1.23,0.88,-10.71,1.25,0.96,-10.65,1.61,0.76,-10.36,1.62,0.84,-10.36,1.73,0.72,-10.33,1.54,0.72,-9.88,1.62,1,-9.74,1.4,0.96,-9.53,0.51,1.04,-10.46,0.82,0.92,-10.75,0.6,0.68,-10.66,1.1,0.96,-10.77,1.08,0.88,-10.83,0.82,0.92,-10.75,1.08,0.88,-10.83,0.81,0.8,-10.79,0.82,0.92,-10.75,1.43,0.72,-10.52,1.4,0.8,-10.53,1.53,0.72,-10.41,1.53,0.72,-10.41,1.62,0.84,-10.36,1.61,0.76,-10.36,1.79,0.68,-10.2,1.74,0.56,-9.99,1.8,0.44,-10.14,1.73,0.72,-10.33,1.79,0.68,-10.2,1.62,0.68,-10.33,0.77,0.72,-9.77,0.67,0.8,-9.85,0.66,0.72,-9.94,0.77,0.72,-9.77,0.69,0.8,-9.79,0.67,0.8,-9.85,0.67,0.8,-9.85,0.59,0.92,-9.84,0.55,0.88,-10.04,0.45,0.44,-10.27,0.47,0.56,-10.14,0.45,0.6,-10.2,0.82,0.92,-10.75,0.81,0.8,-10.79,0.6,0.68,-10.66,1.08,0.88,-10.83,0.97,0.72,-10.82,0.81,0.8,-10.79,1.45,0.68,-10.54,1.43,0.72,-10.52,1.53,0.72,-10.41,1.79,0.68,-10.2,1.66,0.88,-10.09,1.54,0.72,-9.88,1.79,0.68,-10.2,1.73,0.72,-10.33,1.76,0.88,-10.23,1.54,0.72,-9.88,1.26,0.68,-9.65,1.39,0.48,-9.62,0.53,0.68,-10.09,0.62,0.68,-9.97,0.55,0.88,-10.04,1.43,0.72,-10.52,1.41,0.72,-10.55,1.4,0.8,-10.53,1.41,0.72,-10.55,1.43,0.72,-10.52,1.45,0.68,-10.54,1.53,0.72,-10.41,1.62,0.68,-10.33,1.51,0.44,-10.58,1.26,0.68,-9.65,1.27,0.56,-9.6,1.39,0.48,-9.62,1.19,0.76,-9.59,1.26,0.68,-9.65,1.4,0.96,-9.53,0.96,0.6,-10.83,0.92,0.6,-10.82,0.97,0.72,-10.82,1.04,0.56,-10.84,0.96,0.6,-10.83,0.97,0.72,-10.82,1.23,0.64,-10.82,1.04,0.56,-10.84,0.97,0.72,-10.82,1.2,0.44,-10.87,1.37,0.6,-10.7,1.33,0.28,-10.71,1.62,0.68,-10.33,1.53,0.72,-10.41,1.61,0.76,-10.36,1.62,0.68,-10.33,1.8,0.44,-10.14,1.72,0.36,-10.21,1.39,0.48,-9.62,1.27,0.56,-9.6,1.24,0.48,-9.59,1.26,0.68,-9.65,1.19,0.76,-9.59,1.15,0.72,-9.66,0.47,0.44,-10.45,0.49,0.16,-10.67,0.44,0.2,-10.52,0.89,0.48,-10.81,0.49,0.16,-10.67,0.6,0.68,-10.66,0.49,0.16,-10.67,0.47,0.44,-10.45,0.6,0.68,-10.66,0.96,0.56,-10.83,1.1,0.36,-10.87,0.89,0.48,-10.81,0.96,0.56,-10.83,0.96,0.6,-10.83,1.04,0.56,-10.84,1.15,0.88,-10.77,1.26,0.76,-10.73,1.23,0.64,-10.82,1.26,0.76,-10.73,1.26,0.84,-10.69,1.4,0.8,-10.53,1.33,0.28,-10.71,1.38,0.12,-10.56,1.34,0.04,-10.86,1.41,0.72,-10.55,1.37,0.6,-10.7,1.26,0.76,-10.73,1.41,0.72,-10.55,1.45,0.68,-10.54,1.37,0.6,-10.7,1.24,0.48,-9.59,1.27,0.56,-9.6,1.2,0.56,-9.58,1.19,0.6,-9.59,1.27,0.56,-9.6,1.26,0.68,-9.65,0.45,0.44,-10.27,0.48,0.32,-10.25,0.56,0.4,-10.02,0.43,0.6,-10.4,0.6,0.68,-10.66,0.47,0.44,-10.45,0.47,0.44,-10.45,0.45,0.44,-10.27,0.43,0.6,-10.4,0.97,0.72,-10.82,0.92,0.6,-10.82,0.81,0.8,-10.79,1.04,0.56,-10.84,1.23,0.64,-10.82,1.2,0.44,-10.87,0.92,0.6,-10.82,0.96,0.6,-10.83,0.96,0.56,-10.83,1.62,0.4,-10.29,1.62,0.68,-10.33,1.72,0.36,-10.21,1.37,0.6,-10.7,1.45,0.68,-10.54,1.51,0.44,-10.58,0.45,0.6,-10.2,0.45,0.72,-10.27,0.43,0.6,-10.4,1.62,0.68,-10.33,1.79,0.68,-10.2,1.8,0.44,-10.14,1.63,0.44,-9.84,1.54,0.72,-9.88,1.39,0.48,-9.62,0.92,0.6,-10.82,0.96,0.56,-10.83,0.89,0.48,-10.81,0.96,0.56,-10.83,1.04,0.56,-10.84,1.1,0.36,-10.87,1.15,0.88,-10.77,1.24,0.84,-10.72,1.26,0.76,-10.73,1.37,0.6,-10.7,1.23,0.64,-10.82,1.26,0.76,-10.73,1.51,0.44,-10.58,1.45,0.68,-10.54,1.53,0.72,-10.41,1.63,0.44,-9.84,1.74,0.56,-9.99,1.54,0.72,-9.88,1.04,0.56,-10.84,1.2,0.44,-10.87,1.1,0.36,-10.87,1.2,0.44,-10.87,1.23,0.64,-10.82,1.37,0.6,-10.7,1.1,0.36,-10.87,1.2,0.44,-10.87,1.33,0.28,-10.71,1.33,0.28,-10.71,1.37,0.6,-10.7,1.51,0.44,-10.58,1.58,0.2,-10.48,1.51,0.44,-10.58,1.62,0.4,-10.29,1.74,0.56,-9.99,1.79,0.68,-10.2,1.54,0.72,-9.88,1.79,0.4,-10.1,1.78,0.2,-10.06,1.72,0.36,-10.21,1.8,0.44,-10.14,1.74,0.56,-9.99,1.79,0.4,-10.1,1.63,0.44,-9.84,1.32,0.32,-9.64,1.4,0.2,-9.72,0.56,0.4,-10.02,0.59,0.4,-9.96,0.56,0.48,-9.98,0.92,0.6,-10.82,0.6,0.68,-10.66,0.81,0.8,-10.79,1.38,0.12,-10.56,1.58,0.2,-10.48,1.48,0.08,-10.45,0.59,0.4,-9.96,0.56,0.4,-10.02,0.62,0.36,-9.97,0.55,0.2,-10.08,0.59,0.24,-10,0.56,0.4,-10.02,0.42,0.2,-10.42,0.41,0.08,-10.38,0.43,0.04,-10.28,1.1,0.36,-10.87,1.33,0.28,-10.71,1.28,0.16,-10.9,0.59,0.24,-10,0.62,0.36,-9.97,0.56,0.4,-10.02,0.47,0.56,-10.14,0.45,0.44,-10.27,0.56,0.4,-10.02,0.45,0.44,-10.27,0.45,0.6,-10.2,0.43,0.6,-10.4,0.47,0.44,-10.45,0.44,0.2,-10.52,0.42,0.2,-10.42,0.92,0.6,-10.82,0.89,0.48,-10.81,0.6,0.68,-10.66,1.8,0.44,-10.14,1.79,0.4,-10.1,1.72,0.36,-10.21,1.62,0.4,-10.29,1.51,0.44,-10.58,1.62,0.68,-10.33,1.74,0.56,-9.99,1.63,0.44,-9.84,1.79,0.4,-10.1,1.32,0.32,-9.64,1.39,0.48,-9.62,1.29,0.4,-9.59,0.59,0.24,-10,0.68,0.32,-9.92,0.62,0.36,-9.97,0.55,0.2,-10.08,0.48,0.32,-10.25,0.49,0.16,-10.12,0.47,0.44,-10.45,0.42,0.2,-10.42,0.48,0.32,-10.25,0.89,0.48,-10.81,0.76,0.12,-10.88,0.49,0.16,-10.67,1.63,0.16,-10.4,1.58,0.2,-10.48,1.62,0.4,-10.29,0.55,0.2,-10.08,0.56,0.4,-10.02,0.48,0.32,-10.25,0.44,0.2,-10.52,0.41,0.08,-10.43,0.42,0.2,-10.42,1.48,0.08,-10.45,1.58,0.2,-10.48,1.63,0.16,-10.4,1.33,0.28,-10.71,1.51,0.44,-10.58,1.38,0.12,-10.56,1.78,0.2,-10.06,1.63,0.16,-10.4,1.72,0.36,-10.21,1.79,0.4,-10.1,1.63,0.44,-9.84,1.78,0.2,-10.06,1.78,0.2,-10.06,1.63,0.44,-9.84,1.61,0,-9.9,0.49,0.16,-10.12,0.5,0.16,-10.08,0.55,0.2,-10.08,0.51,0.04,-10.11,0.55,0.12,-10.04,0.5,0.16,-10.08,1.1,0.36,-10.87,1.22,0.12,-10.93,0.76,0.12,-10.88,1.63,0.16,-10.4,1.62,0.4,-10.29,1.72,0.36,-10.21,1.78,0.2,-10.06,1.61,0.04,-10.36,1.63,0.16,-10.4,1.68,-0.04,-10.15,1.61,0.04,-10.36,1.78,0.2,-10.06,1.63,0.44,-9.84,1.39,0.48,-9.62,1.32,0.32,-9.64,1.18,0.24,-9.67,1.27,0.2,-9.68,1.32,0.32,-9.64,0.51,0.04,-10.11,0.5,0.16,-10.08,0.49,0.16,-10.12,0.48,0.32,-10.25,0.45,0.44,-10.27,0.47,0.44,-10.45,0.49,0.16,-10.12,0.42,0.2,-10.42,0.43,0.04,-10.28,0.49,0.16,-10.67,0.52,-0.12,-10.68,0.44,0.04,-10.48,1.1,0.36,-10.87,0.76,0.12,-10.88,0.89,0.48,-10.81,1.22,0.12,-10.93,1.28,0.16,-10.9,1.34,0.04,-10.86,1.33,0.28,-10.71,1.34,0.04,-10.86,1.28,0.16,-10.9,1.51,0.44,-10.58,1.58,0.2,-10.48,1.38,0.12,-10.56,1.27,0.2,-9.68,1.28,0.16,-9.71,1.4,0.2,-9.72,0.44,0.04,-10.48,0.42,0.04,-10.41,0.41,0.08,-10.43,0.44,0.2,-10.52,0.44,0.04,-10.48,0.41,0.08,-10.43,0.44,0.2,-10.52,0.49,0.16,-10.67,0.44,0.04,-10.48,0.52,-0.12,-10.68,0.49,0.16,-10.67,0.76,0.12,-10.88,1.1,0.36,-10.87,1.28,0.16,-10.9,1.22,0.12,-10.93,1.73,0,-10.03,1.68,-0.08,-10.04,1.68,-0.04,-10.15,1.13,-0.04,-9.83,1.25,-0.32,-9.81,1.5,-0.2,-9.84,0.55,0.12,-10.04,0.51,0.04,-10.11,0.56,0,-10.02,0.51,0.04,-10.11,0.49,0.16,-10.12,0.43,0.04,-10.28,0.41,0.08,-10.38,0.42,0.04,-10.41,0.43,0.04,-10.28,0.41,0.08,-10.43,0.41,0.08,-10.38,0.42,0.2,-10.42,0.41,0.08,-10.38,0.41,0.08,-10.43,0.42,0.04,-10.41,1.31,-0.2,-10.88,1.34,0.04,-10.86,1.4,-0.2,-10.6,1.48,0.08,-10.45,1.63,0.16,-10.4,1.57,0.04,-10.4,1.61,0.04,-10.36,1.57,0.04,-10.4,1.63,0.16,-10.4,1.73,0,-10.03,1.78,0.2,-10.06,1.61,0,-9.9,0.59,-0.08,-10.04,0.56,0,-10.02,0.51,0.04,-10.11,0.49,0.16,-10.12,0.48,0.32,-10.25,0.42,0.2,-10.42,0.42,0.04,-10.41,0.44,0.04,-10.48,0.43,-0.16,-10.41,0.43,-0.16,-10.41,0.52,-0.12,-10.68,0.39,-0.36,-10.56,1.48,0.08,-10.45,1.45,0.04,-10.43,1.38,0.12,-10.56,1.49,0,-10.35,1.57,0.04,-10.4,1.61,0.04,-10.36,1.49,0,-10.35,1.61,0.04,-10.36,1.68,-0.04,-10.15,1.61,0,-9.9,1.68,-0.08,-10.04,1.73,0,-10.03,1.29,0.08,-9.78,1.13,-0.04,-9.83,1.5,-0.2,-9.84,1.12,0.08,-9.81,1.13,-0.04,-9.83,1.16,0.08,-9.81,0.5,-0.24,-10.15,0.43,-0.16,-10.41,0.42,-0.36,-10.31,0.74,-0.28,-10.9,1.22,0.12,-10.93,1.16,-0.36,-10.91,1.45,0.04,-10.43,1.49,0,-10.35,1.37,-0.16,-10.49,1.73,0,-10.03,1.68,-0.04,-10.15,1.78,0.2,-10.06,1.29,0.08,-9.78,1.5,-0.2,-9.84,1.61,0,-9.9,1.01,-0.08,-9.86,1,-0.16,-9.86,1.13,-0.04,-9.83,1.02,0,-9.81,1.13,-0.04,-9.83,1.12,0.08,-9.81,0.43,0.04,-10.28,0.5,-0.24,-10.15,0.51,0.04,-10.11,1.39,-0.28,-10.31,1.37,-0.16,-10.49,1.49,0,-10.35,1.68,-0.08,-10.04,1.61,0,-9.9,1.62,-0.2,-9.96,0.96,-0.08,-9.86,1.01,-0.08,-9.86,1.02,0,-9.81,0.43,-0.16,-10.41,0.44,0.04,-10.48,0.52,-0.12,-10.68,1.38,0.12,-10.56,1.4,-0.2,-10.6,1.34,0.04,-10.86,1.63,0.44,-9.84,1.4,0.2,-9.72,1.61,0,-9.9,0.59,-0.08,-10.04,0.51,0.04,-10.11,0.5,-0.24,-10.15,0.43,0.04,-10.28,0.43,-0.16,-10.41,0.5,-0.24,-10.15,0.76,0.12,-10.88,0.74,-0.28,-10.9,0.52,-0.12,-10.68,1.31,-0.2,-10.88,1.22,0.12,-10.93,1.34,0.04,-10.86,1.43,-0.32,-10.63,1.44,-0.4,-10.79,1.4,-0.36,-10.83,1.38,0.12,-10.56,1.45,0.04,-10.43,1.37,-0.16,-10.49,1.38,0.12,-10.56,1.37,-0.16,-10.49,1.4,-0.2,-10.6,1.07,-0.28,-9.85,1.25,-0.32,-9.81,1.13,-0.04,-9.83,0.57,-0.2,-10.06,0.59,-0.08,-10.04,0.5,-0.24,-10.15,0.57,-0.2,-10.06,0.5,-0.24,-10.15,0.54,-0.32,-10.08,1.68,-0.08,-10.04,1.62,-0.2,-9.96,1.44,-0.2,-10.16,1.29,0.08,-9.78,1.61,0,-9.9,1.4,0.2,-9.72,1.02,0,-9.81,1.01,-0.08,-9.86,1.13,-0.04,-9.83,1,-0.16,-9.86,1,-0.28,-9.86,1.07,-0.28,-9.85,0.43,0.04,-10.28,0.42,0.04,-10.41,0.43,-0.16,-10.41,1.22,0.12,-10.93,1.31,-0.2,-10.88,1.16,-0.36,-10.91,0.48,-0.4,-10.75,0.39,-0.36,-10.56,0.52,-0.12,-10.68,1.39,-0.28,-10.83,1.4,-0.36,-10.83,1.16,-0.36,-10.91,1.39,-0.28,-10.83,1.4,-0.2,-10.6,1.43,-0.32,-10.63,1.44,-0.2,-10.16,1.41,-0.28,-10.15,1.39,-0.28,-10.31,1.68,-0.04,-10.15,1.68,-0.08,-10.04,1.44,-0.2,-10.16,1.62,-0.2,-9.96,1.41,-0.28,-10.15,1.44,-0.2,-10.16,1.57,-0.24,-9.9,1.62,-0.2,-9.96,1.61,0,-9.9,1.5,-0.2,-9.84,1.25,-0.32,-9.81,1.37,-0.4,-9.83,1.5,-0.2,-9.84,1.57,-0.24,-9.9,1.61,0,-9.9,1.22,0.12,-10.93,0.74,-0.28,-10.9,0.76,0.12,-10.88,1.5,-0.2,-9.84,1.48,-0.36,-9.86,1.57,-0.24,-9.9,1.62,-0.2,-9.96,1.57,-0.24,-9.9,1.41,-0.28,-10.15,1,-0.16,-9.86,0.94,-0.2,-9.87,1,-0.28,-9.86,0.42,-0.36,-10.31,0.43,-0.16,-10.41,0.39,-0.36,-10.56,1.39,-0.28,-10.83,1.31,-0.2,-10.88,1.4,-0.2,-10.6,1.39,-0.28,-10.83,1.43,-0.32,-10.63,1.4,-0.36,-10.83,1.48,-0.36,-9.86,1.5,-0.2,-9.84,1.37,-0.4,-9.83,0.39,-0.36,-10.56,0.33,-0.68,-10.44,0.38,-0.44,-10.4,1.48,-0.56,-10.01,1.5,-0.52,-10.15,1.41,-0.28,-10.15,1.44,-0.2,-10.16,1.49,0,-10.35,1.68,-0.04,-10.15,1.22,-0.48,-9.87,1.37,-0.4,-9.83,1.25,-0.32,-9.81,0.74,-0.28,-10.9,0.48,-0.4,-10.75,0.52,-0.12,-10.68,1.44,-0.4,-10.79,1.48,-0.52,-10.74,1.35,-0.6,-10.87,1.44,-0.2,-10.16,1.39,-0.28,-10.31,1.49,0,-10.35,1.13,-0.44,-9.87,1.22,-0.48,-9.87,1.25,-0.32,-9.81,0.5,-0.24,-10.15,0.42,-0.36,-10.31,0.47,-0.48,-10.18,1.4,-0.36,-10.83,1.35,-0.6,-10.87,1.16,-0.36,-10.91,1.39,-0.28,-10.83,1.16,-0.36,-10.91,1.31,-0.2,-10.88,1.39,-0.28,-10.31,1.41,-0.28,-10.15,1.5,-0.52,-10.15,1.43,-0.32,-10.63,1.37,-0.16,-10.49,1.39,-0.28,-10.31,1.38,-0.6,-9.94,1.48,-0.56,-10.01,1.37,-0.4,-9.83,1.11,-0.36,-9.85,1.25,-0.32,-9.81,1.07,-0.28,-9.85,0.38,-0.44,-10.4,0.42,-0.36,-10.31,0.39,-0.36,-10.56,0.39,-0.36,-10.56,0.35,-0.76,-10.63,0.33,-0.68,-10.44,1.41,-0.28,-10.15,1.57,-0.24,-9.9,1.48,-0.36,-9.86,1.48,-0.56,-10.01,1.48,-0.36,-9.86,1.37,-0.4,-9.83,0.42,-0.36,-10.31,0.38,-0.44,-10.4,0.47,-0.52,-10.25,0.48,-0.6,-10.29,0.47,-0.52,-10.25,0.38,-0.44,-10.4,0.74,-0.28,-10.9,1.16,-0.36,-10.91,0.82,-0.68,-10.94,1.4,-0.36,-10.83,1.44,-0.4,-10.79,1.35,-0.6,-10.87,1.43,-0.32,-10.63,1.4,-0.2,-10.6,1.37,-0.16,-10.49,1.49,-0.92,-10.82,1.48,-0.52,-10.74,1.57,-0.88,-10.59,1.48,-0.52,-10.74,1.44,-0.4,-10.79,1.43,-0.32,-10.63,1.48,-0.56,-10.01,1.34,-0.72,-10.05,1.5,-0.52,-10.15,0.48,-0.4,-10.75,0.74,-0.28,-10.9,0.82,-0.68,-10.94,1.39,-0.28,-10.31,1.54,-0.76,-10.31,1.43,-0.32,-10.63,1.48,-0.56,-10.01,1.41,-0.28,-10.15,1.48,-0.36,-9.86,1.34,-0.72,-10.05,1.48,-0.56,-10.01,1.38,-0.6,-9.94,1.54,-0.76,-10.31,1.48,-0.52,-10.74,1.43,-0.32,-10.63,0.41,-1,-10.82,0.35,-0.76,-10.63,0.82,-0.68,-10.94,1.49,-0.92,-10.82,1.32,-1.16,-10.92,1.06,-1.08,-10.98,1.34,-0.72,-10.05,1.41,-0.88,-10.23,1.54,-0.76,-10.31,1.34,-0.72,-10.05,1.38,-0.6,-9.94,1.22,-0.56,-9.92,0.33,-0.68,-10.44,0.41,-0.68,-10.31,0.38,-0.44,-10.4,0.35,-0.76,-10.63,0.48,-0.4,-10.75,0.82,-0.68,-10.94,0.33,-0.68,-10.44,0.29,-1,-10.52,0.41,-0.88,-10.38,1.35,-0.6,-10.87,1.49,-0.92,-10.82,1.06,-1.08,-10.98,1.39,-0.28,-10.31,1.5,-0.52,-10.15,1.54,-0.76,-10.31,1.34,-0.72,-10.05,1.54,-0.76,-10.31,1.5,-0.52,-10.15,0.38,-0.96,-10.36,0.29,-1,-10.52,0.35,-1.16,-10.42,0.39,-0.36,-10.56,0.48,-0.4,-10.75,0.35,-0.76,-10.63,1,-0.96,-10.22,1.29,-1.04,-10.29,1.41,-0.88,-10.23,1.02,-0.72,-10.13,0.91,-0.72,-10.14,0.89,-0.84,-10.19,1,-0.96,-10.22,1.41,-0.88,-10.23,1.1,-0.72,-10.1,0.33,-0.68,-10.44,0.39,-0.8,-10.33,0.44,-0.72,-10.32,0.33,-0.68,-10.44,0.35,-0.76,-10.63,0.29,-1,-10.52,1.32,-1.16,-10.92,1.16,-1.2,-10.93,1.06,-1.08,-10.98,1.56,-1,-10.6,1.44,-1.12,-10.63,1.5,-1.16,-10.74,0.91,-0.72,-10.14,0.84,-0.76,-10.15,0.89,-0.84,-10.19,1.49,-0.92,-10.82,1.57,-0.88,-10.59,1.56,-1,-10.6,1.35,-0.6,-10.87,0.82,-0.68,-10.94,1.16,-0.36,-10.91,1.54,-0.76,-10.31,1.57,-0.88,-10.59,1.48,-0.52,-10.74,1,-0.96,-10.22,1.11,-1.12,-10.28,1.29,-1.04,-10.29,0.89,-0.84,-10.19,0.84,-0.76,-10.15,0.79,-0.8,-10.16,0.62,-1,-10.95,0.86,-0.92,-10.91,0.79,-1.04,-11.01,1.49,-0.92,-10.82,1.35,-0.6,-10.87,1.48,-0.52,-10.74,1.02,-0.72,-10.13,0.89,-0.84,-10.19,1,-0.96,-10.22,0.29,-1,-10.52,0.41,-1,-10.82,0.34,-1.2,-10.8,0.82,-0.68,-10.94,0.86,-0.92,-10.91,0.62,-1,-10.95,1.57,-1.16,-10.81,1.62,-1.12,-10.79,1.58,-1.08,-10.77,1.43,-1.08,-10.49,1.42,-1.12,-10.57,1.56,-1,-10.6,1.41,-0.88,-10.23,1.43,-1.08,-10.49,1.54,-0.76,-10.31,0.89,-0.84,-10.19,0.78,-0.92,-10.2,1,-0.96,-10.22,0.78,-0.92,-10.2,0.89,-0.84,-10.19,0.79,-0.8,-10.16,0.79,-1.08,-10.24,1,-0.96,-10.22,0.78,-0.92,-10.2,0.21,-1.2,-10.59,0.34,-1.2,-10.8,0.2,-1.28,-10.72,0.35,-1.16,-10.42,0.29,-1,-10.52,0.21,-1.2,-10.59,0.62,-1,-10.95,0.41,-1,-10.82,0.82,-0.68,-10.94,0.89,-1.08,-11.01,0.79,-1.04,-11.01,0.86,-0.92,-10.91,1.06,-1.08,-10.98,0.89,-1.08,-11.01,0.86,-0.92,-10.91,1.44,-1.12,-10.63,1.56,-1,-10.6,1.42,-1.12,-10.57,0.66,-1.24,-10.92,0.58,-1.24,-10.95,0.62,-1,-10.95,1.35,-0.6,-10.87,1.06,-1.08,-10.98,0.86,-0.92,-10.91,1.35,-0.6,-10.87,0.86,-0.92,-10.91,0.82,-0.68,-10.94,1.58,-1.08,-10.77,1.53,-1.08,-10.85,1.49,-0.92,-10.82,1.29,-1.04,-10.29,1.33,-1.12,-10.45,1.43,-1.08,-10.49,1.41,-0.88,-10.23,1.29,-1.04,-10.29,1.43,-1.08,-10.49,1.43,-1.08,-10.49,1.56,-1,-10.6,1.57,-0.88,-10.59,0.79,-1.08,-10.24,0.86,-1.12,-10.25,1,-0.96,-10.22,0.44,-1.2,-10.83,0.34,-1.2,-10.8,0.41,-1,-10.82,0.92,-1.24,-10.86,0.8,-1.28,-10.92,0.89,-1.08,-11.01,1.42,-1.12,-10.57,1.43,-1.08,-10.49,1.33,-1.12,-10.45,1.43,-1.08,-10.49,1.57,-0.88,-10.59,1.54,-0.76,-10.31,1.11,-1.12,-10.28,1.15,-1.16,-10.33,1.29,-1.04,-10.29,0.51,-1.2,-10.34,0.56,-1.16,-10.31,0.48,-1.12,-10.29,0.62,-1,-10.95,0.44,-1.2,-10.83,0.41,-1,-10.82,0.8,-1.28,-10.92,0.73,-1.16,-10.98,0.89,-1.08,-11.01,0.79,-1.04,-11.01,0.89,-1.08,-11.01,0.73,-1.16,-10.98,1.02,-1.2,-10.93,1.06,-1.08,-10.98,1.16,-1.2,-10.93,1.29,-1.2,-10.87,1.16,-1.2,-10.93,1.32,-1.16,-10.92,1.29,-1.2,-10.87,1.32,-1.16,-10.92,1.51,-1.24,-10.82,1.49,-0.92,-10.82,1.53,-1.08,-10.85,1.32,-1.16,-10.92,1.58,-1.08,-10.77,1.56,-1,-10.6,1.5,-1.16,-10.74,1.53,-1.08,-10.85,1.51,-1.24,-10.82,1.32,-1.16,-10.92,1.62,-1.12,-10.79,1.53,-1.08,-10.85,1.58,-1.08,-10.77,1.57,-1.16,-10.81,1.58,-1.08,-10.77,1.5,-1.16,-10.74,1.58,-1.08,-10.77,1.49,-0.92,-10.82,1.56,-1,-10.6,1.44,-1.12,-10.63,1.37,-1.16,-10.69,1.5,-1.16,-10.74,1.11,-1.2,-10.44,1.24,-1.16,-10.48,1.15,-1.16,-10.33,1.15,-1.16,-10.33,1.33,-1.12,-10.45,1.29,-1.04,-10.29,1.1,-1.16,-10.33,1.15,-1.16,-10.33,1.11,-1.12,-10.28,1.1,-0.72,-10.1,1.41,-0.88,-10.23,1.34,-0.72,-10.05,0.49,-1.28,-10.25,0.51,-1.2,-10.34,0.35,-1.24,-10.34,0.35,-1.16,-10.42,0.48,-1.12,-10.29,0.36,-1.04,-10.31,0.21,-1.2,-10.59,0.29,-1,-10.52,0.34,-1.2,-10.8,0.23,-1.4,-10.44,0.35,-1.24,-10.34,0.35,-1.16,-10.42,0.29,-1,-10.52,0.35,-0.76,-10.63,0.41,-1,-10.82,0.62,-1,-10.95,0.58,-1.24,-10.95,0.48,-1.24,-10.92,0.73,-1.16,-10.98,0.66,-1.24,-10.92,0.62,-1,-10.95,0.8,-1.28,-10.92,0.75,-1.28,-10.96,0.73,-1.16,-10.98,1.06,-1.08,-10.98,1.02,-1.2,-10.93,0.89,-1.08,-11.01,1.33,-1.28,-10.79,1.27,-1.24,-10.84,1.29,-1.2,-10.87,1.62,-1.12,-10.79,1.57,-1.16,-10.81,1.53,-1.08,-10.85,1.5,-1.16,-10.74,1.51,-1.24,-10.82,1.57,-1.16,-10.81,1.16,-1.24,-10.6,1.11,-1.2,-10.44,1.05,-1.28,-10.49,1.24,-1.16,-10.48,1.11,-1.2,-10.44,1.16,-1.24,-10.6,1.15,-1.16,-10.33,1.24,-1.16,-10.48,1.33,-1.12,-10.45,0.89,-1.2,-10.35,1.05,-1.28,-10.49,1.11,-1.2,-10.44,1.1,-1.16,-10.33,0.89,-1.2,-10.35,1.11,-1.2,-10.44,0.86,-1.12,-10.25,1.1,-1.16,-10.33,1.11,-1.12,-10.28,1.53,-1.08,-10.85,1.57,-1.16,-10.81,1.51,-1.24,-10.82,1.39,-1.4,-10.55,1.45,-1.4,-10.64,1.46,-1.32,-10.65,1.37,-1.16,-10.69,1.5,-1.28,-10.75,1.5,-1.16,-10.74,1.26,-1.16,-10.63,1.24,-1.16,-10.48,1.16,-1.24,-10.6,0.81,-1.28,-10.42,0.85,-1.32,-10.46,0.89,-1.2,-10.35,0.35,-1.16,-10.42,0.35,-1.24,-10.34,0.51,-1.2,-10.34,0.23,-1.4,-10.44,0.35,-1.16,-10.42,0.21,-1.2,-10.59,0.23,-1.4,-10.44,0.2,-1.28,-10.72,0.18,-1.44,-10.74,0.23,-1.4,-10.44,0.21,-1.2,-10.59,0.2,-1.28,-10.72,0.73,-1.16,-10.98,0.62,-1,-10.95,0.79,-1.04,-11.01,0.82,-1.32,-10.9,0.99,-1.28,-10.8,1.08,-1.4,-10.75,0.82,-1.32,-10.9,0.8,-1.28,-10.92,0.92,-1.24,-10.86,0.92,-1.24,-10.86,0.89,-1.08,-11.01,1.02,-1.2,-10.93,0.98,-1.24,-10.85,1.02,-1.2,-10.93,1.03,-1.24,-10.89,0.46,-1.36,-10.27,0.23,-1.4,-10.44,0.23,-1.64,-10.37,0.35,-1.16,-10.42,0.51,-1.2,-10.34,0.48,-1.12,-10.29,0.46,-1.36,-10.27,0.35,-1.24,-10.34,0.23,-1.4,-10.44,0.32,-1.24,-10.89,0.41,-1.24,-10.93,0.35,-1.4,-10.95,0.32,-1.24,-10.89,0.35,-1.4,-10.95,0.18,-1.44,-10.74,0.41,-1.24,-10.93,0.48,-1.24,-10.92,0.45,-1.28,-10.98,0.62,-1,-10.95,0.48,-1.24,-10.92,0.44,-1.2,-10.83,0.58,-1.24,-10.95,0.45,-1.28,-10.98,0.48,-1.24,-10.92,0.75,-1.28,-10.96,0.66,-1.24,-10.92,0.73,-1.16,-10.98,1.33,-1.28,-10.79,1.29,-1.2,-10.87,1.51,-1.24,-10.82,1.42,-1.32,-10.81,1.33,-1.28,-10.79,1.51,-1.24,-10.82,1.41,-1.4,-10.73,1.42,-1.32,-10.81,1.5,-1.28,-10.75,1.51,-1.24,-10.82,1.5,-1.28,-10.75,1.42,-1.32,-10.81,1.5,-1.28,-10.75,1.51,-1.24,-10.82,1.5,-1.16,-10.74,1.16,-1.24,-10.6,1.18,-1.36,-10.62,1.26,-1.16,-10.63,0.85,-1.32,-10.46,0.95,-1.32,-10.49,0.89,-1.2,-10.35,0.85,-1.32,-10.46,0.81,-1.28,-10.42,0.8,-1.32,-10.39,0.45,-1.28,-10.98,0.51,-1.52,-11.05,0.35,-1.4,-10.95,0.8,-1.28,-10.92,0.85,-1.32,-10.96,0.75,-1.28,-10.96,0.82,-1.32,-10.9,0.85,-1.32,-10.96,0.8,-1.28,-10.92,0.98,-1.24,-10.85,0.92,-1.24,-10.86,1.02,-1.2,-10.93,1.46,-1.32,-10.65,1.41,-1.4,-10.73,1.5,-1.28,-10.75,1.37,-1.16,-10.69,1.46,-1.32,-10.65,1.5,-1.28,-10.75,1.05,-1.28,-10.49,0.89,-1.2,-10.35,0.95,-1.32,-10.49,1.05,-1.28,-10.49,0.95,-1.32,-10.49,1.04,-1.36,-10.57,0.95,-1.32,-10.49,0.93,-1.36,-10.51,1.04,-1.36,-10.57,0.32,-1.24,-10.89,0.18,-1.44,-10.74,0.2,-1.28,-10.72,0.58,-1.24,-10.95,0.62,-1.28,-11.04,0.45,-1.28,-10.98,0.82,-1.32,-11.09,0.8,-1.48,-11.08,0.58,-1.44,-11.07,0.87,-1.32,-11.05,0.96,-1.36,-11.08,0.8,-1.48,-11.08,0.92,-1.24,-10.86,0.98,-1.24,-10.85,0.99,-1.28,-10.8,0.82,-1.32,-10.9,0.92,-1.24,-10.86,0.99,-1.28,-10.8,1.45,-1.4,-10.64,1.41,-1.4,-10.73,1.46,-1.32,-10.65,1.18,-1.36,-10.62,1.33,-1.36,-10.57,1.37,-1.16,-10.69,1.18,-1.36,-10.62,1.37,-1.16,-10.69,1.26,-1.16,-10.63,1.11,-1.36,-10.63,1.18,-1.36,-10.62,1.16,-1.24,-10.6,1.04,-1.36,-10.57,1.11,-1.36,-10.63,1.16,-1.24,-10.6,1.04,-1.36,-10.57,1.16,-1.24,-10.6,1.05,-1.28,-10.49,0.96,-1.36,-10.45,0.93,-1.36,-10.51,0.95,-1.32,-10.49,0.45,-1.28,-10.98,0.35,-1.4,-10.95,0.41,-1.24,-10.93,0.62,-1.28,-11.04,0.58,-1.44,-11.07,0.45,-1.28,-10.98,0.82,-1.32,-11.09,0.58,-1.44,-11.07,0.62,-1.28,-11.04,0.87,-1.32,-11.05,0.8,-1.48,-11.08,0.82,-1.32,-11.09,1.13,-1.4,-10.71,1.16,-1.44,-10.74,1.08,-1.4,-10.75,1.33,-1.36,-10.57,1.39,-1.4,-10.55,1.46,-1.32,-10.65,1.33,-1.36,-10.57,1.46,-1.32,-10.65,1.37,-1.16,-10.69,1.39,-1.4,-10.55,1.33,-1.36,-10.57,1.37,-1.48,-10.53,0.83,-1.52,-10.4,0.84,-1.32,-10.32,0.63,-1.44,-10.25,0.91,-1.36,-10.3,0.96,-1.44,-10.29,1.02,-1.36,-10.36,0.83,-1.52,-10.4,0.96,-1.44,-10.29,0.91,-1.36,-10.3,0.34,-1.2,-10.8,0.32,-1.24,-10.89,0.2,-1.28,-10.72,0.45,-1.28,-10.98,0.58,-1.44,-11.07,0.51,-1.52,-11.05,1.04,-1.48,-11.02,1.08,-1.36,-10.98,1.13,-1.44,-11.01,1.04,-1.48,-11.02,0.97,-1.48,-11.08,0.96,-1.36,-11.08,1.12,-1.36,-10.71,1.08,-1.4,-10.75,0.99,-1.28,-10.8,1.13,-1.4,-10.71,1.08,-1.4,-10.75,1.12,-1.36,-10.71,1.35,-1.44,-10.69,1.41,-1.4,-10.73,1.43,-1.44,-10.63,1.41,-1.4,-10.73,1.45,-1.4,-10.64,1.43,-1.44,-10.63,1.48,-1.44,-10.64,1.43,-1.44,-10.63,1.45,-1.4,-10.64,1.46,-1.44,-10.62,1.48,-1.44,-10.64,1.45,-1.4,-10.64,1.38,-1.48,-10.63,1.46,-1.44,-10.62,1.39,-1.4,-10.55,1.46,-1.44,-10.62,1.45,-1.4,-10.64,1.39,-1.4,-10.55,1.33,-1.36,-10.57,1.26,-1.4,-10.47,1.37,-1.48,-10.53,1.18,-1.4,-10.46,1.21,-1.56,-10.52,1.26,-1.4,-10.47,0.96,-1.44,-10.29,0.99,-1.52,-10.34,1.02,-1.36,-10.36,0.83,-1.52,-10.4,0.91,-1.36,-10.3,0.84,-1.32,-10.32,0.99,-1.52,-10.34,0.96,-1.44,-10.29,0.83,-1.52,-10.4,1.04,-1.48,-11.02,1.13,-1.44,-11.01,1.09,-1.52,-10.91,1.22,-1.44,-10.85,1.13,-1.44,-11.01,1.08,-1.36,-10.98,1.22,-1.44,-10.85,1.17,-1.52,-10.93,1.13,-1.44,-11.01,1.22,-1.44,-10.85,1.21,-1.56,-10.84,1.17,-1.52,-10.93,1.16,-1.44,-10.74,1.29,-1.44,-10.68,1.21,-1.56,-10.84,1.18,-1.36,-10.62,1.29,-1.44,-10.68,1.16,-1.44,-10.74,1.38,-1.48,-10.63,1.37,-1.48,-10.66,1.46,-1.44,-10.62,1.38,-1.48,-10.63,1.39,-1.4,-10.55,1.37,-1.48,-10.53,1.37,-1.52,-10.61,1.38,-1.48,-10.63,1.37,-1.48,-10.53,1.1,-1.4,-10.37,1.17,-1.48,-10.38,1.18,-1.4,-10.46,0.63,-1.52,-10.3,0.66,-1.6,-10.35,0.83,-1.52,-10.4,0.51,-1.52,-11.05,0.58,-1.44,-11.07,0.78,-1.56,-11.02,0.78,-1.56,-11.02,0.8,-1.48,-11.08,0.96,-1.56,-11,0.8,-1.48,-11.08,0.97,-1.48,-11.08,0.96,-1.56,-11,1.04,-1.48,-11.02,0.96,-1.36,-11.08,1.08,-1.36,-10.98,1.04,-1.48,-11.02,1.01,-1.52,-10.96,0.97,-1.48,-11.08,1.09,-1.52,-10.91,1.13,-1.44,-11.01,1.17,-1.52,-10.93,1.35,-1.48,-10.68,1.33,-1.56,-10.67,1.21,-1.56,-10.84,1.29,-1.44,-10.68,1.35,-1.48,-10.68,1.21,-1.56,-10.84,1.35,-1.48,-10.68,1.29,-1.44,-10.68,1.35,-1.44,-10.69,1.37,-1.48,-10.66,1.33,-1.56,-10.67,1.35,-1.48,-10.68,1.37,-1.52,-10.61,1.37,-1.48,-10.53,1.21,-1.56,-10.52,1.33,-1.56,-10.67,1.37,-1.52,-10.61,1.21,-1.56,-10.52,1.21,-1.56,-10.52,1.37,-1.48,-10.53,1.26,-1.4,-10.47,0.99,-1.52,-10.34,1.09,-1.52,-10.38,1.1,-1.4,-10.37,0.99,-1.52,-10.34,1.1,-1.4,-10.37,1.02,-1.36,-10.36,1.18,-1.36,-10.62,1.16,-1.44,-10.74,1.13,-1.4,-10.71,1.22,-1.44,-10.85,1.16,-1.44,-10.74,1.21,-1.56,-10.84,1.37,-1.48,-10.66,1.38,-1.48,-10.63,1.37,-1.52,-10.61,1.37,-1.48,-10.66,1.37,-1.52,-10.61,1.33,-1.56,-10.67,1.09,-1.52,-10.38,1.06,-1.56,-10.44,1.21,-1.56,-10.52,1.17,-1.48,-10.38,1.09,-1.52,-10.38,1.21,-1.56,-10.52,1.18,-1.4,-10.46,1.17,-1.48,-10.38,1.21,-1.56,-10.52,1.1,-1.4,-10.37,1.09,-1.52,-10.38,1.17,-1.48,-10.38,0.75,-1.56,-10.46,0.83,-1.52,-10.4,0.66,-1.6,-10.35,0.96,-1.56,-11,0.97,-1.48,-11.08,1.01,-1.52,-10.96,0.96,-1.36,-11.08,0.97,-1.48,-11.08,0.8,-1.48,-11.08,0.96,-1.56,-11,1.01,-1.52,-10.96,0.99,-1.56,-10.95,0.23,-1.64,-10.37,0.23,-1.4,-10.44,0.18,-1.44,-10.74,0.58,-1.44,-11.07,0.8,-1.48,-11.08,0.78,-1.56,-11.02,0.98,-1.6,-10.86,0.93,-1.6,-10.87,0.99,-1.56,-10.95,1.01,-1.56,-10.81,0.98,-1.6,-10.86,0.99,-1.56,-10.95,1.01,-1.56,-10.81,0.99,-1.56,-10.95,1.01,-1.52,-10.96,1.01,-1.56,-10.81,0.98,-1.6,-10.82,0.98,-1.6,-10.86,0.82,-1.56,-10.52,0.79,-1.6,-10.55,0.85,-1.6,-10.61,0.82,-1.56,-10.52,0.75,-1.56,-10.54,0.79,-1.6,-10.55,0.75,-1.56,-10.46,0.79,-1.6,-10.55,0.75,-1.56,-10.54,0.63,-1.44,-10.25,0.63,-1.52,-10.3,0.83,-1.52,-10.4,0.61,-1.56,-10.31,0.66,-1.6,-10.35,0.63,-1.52,-10.3,0.98,-1.6,-10.82,0.96,-1.6,-10.72,0.88,-1.64,-10.8,0.96,-1.6,-10.72,0.98,-1.6,-10.82,1.01,-1.56,-10.81,0.95,-1.56,-10.5,0.9,-1.56,-10.49,0.89,-1.6,-10.54,0.76,0.6,-9.82,0.79,0.6,-9.75,0.82,0.64,-9.77])

IndexedFaceSet475.setCoord(Coordinate476)

Shape471.setGeometry(IndexedFaceSet475)

Transform470.addChildren(Shape471)

fieldValue469.addChildren(Transform470)

ProtoInstance467.addFieldValue(fieldValue469)

fieldValue466.addChildren(ProtoInstance467)
ProtoInstance477 = ProtoInstance()
ProtoInstance477.setName("Joint")
ProtoInstance477.setDEF("Allen_hanim_r_wrist")
fieldValue478 = fieldValue()
fieldValue478.setName("name")
fieldValue478.setValue("r_wrist")

ProtoInstance477.addFieldValue(fieldValue478)
fieldValue479 = fieldValue()
fieldValue479.setName("center")
fieldValue479.setValue("-0.217 0.811 -0.0338")

ProtoInstance477.addFieldValue(fieldValue479)
fieldValue480 = fieldValue()
fieldValue480.setName("children")
ProtoInstance481 = ProtoInstance()
ProtoInstance481.setName("Segment")
ProtoInstance481.setDEF("Allen_hanim_r_hand")
fieldValue482 = fieldValue()
fieldValue482.setName("name")
fieldValue482.setValue("r_hand")

ProtoInstance481.addFieldValue(fieldValue482)
fieldValue483 = fieldValue()
fieldValue483.setName("children")
Transform484 = Transform()
Transform484.setDEF("Allen_r_hand_adjust")
Transform484.setCenter([0.2693,1.011,-0.0248])
Transform484.setRotation([0,1,0,1.570796])
Transform484.setScale([0.1,0.1,0.1])
Shape485 = Shape()
Appearance486 = Appearance()
Material487 = Material()
Material487.setUSE("Skin_Color")

Appearance486.setMaterial(Material487)

Shape485.setAppearance(Appearance486)
IndexedFaceSet488 = IndexedFaceSet()
IndexedFaceSet488.setCoordIndex([0,1,2,-1,3,4,5,-1,6,7,8,-1,9,10,11,-1,12,13,14,-1,15,16,17,-1,18,19,20,-1,21,22,23,-1,24,25,26,-1,27,28,29,-1,30,31,32,-1,33,34,35,-1,36,37,38,-1,39,40,41,-1,42,43,44,-1,45,46,47,-1,48,49,50,-1,51,52,53,-1,54,55,56,-1,57,58,59,-1,60,61,62,-1,63,64,65,-1,66,67,68,-1,69,70,71,-1,72,73,74,-1,75,76,77,-1,78,79,80,-1,81,82,83,-1,84,85,86,-1,87,88,89,-1,90,91,92,-1,93,94,95,-1,96,97,98,-1,99,100,101,-1,102,103,104,-1,105,106,107,-1,108,109,110,-1,111,112,113,-1,114,115,116,-1,117,118,119,-1,120,121,122,-1,123,124,125,-1,126,127,128,-1,129,130,131,-1,132,133,134,-1,135,136,137,-1,138,139,140,-1,141,142,143,-1,144,145,146,-1,147,148,149,-1,150,151,152,-1,153,154,155,-1,156,157,158,-1,159,160,161,-1,162,163,164,-1,165,166,167,-1,168,169,170,-1,171,172,173,-1,174,175,176,-1,177,178,179,-1,180,181,182,-1,183,184,185,-1,186,187,188,-1,189,190,191,-1,192,193,194,-1,195,196,197,-1,198,199,200,-1,201,202,203,-1,204,205,206,-1,207,208,209,-1,210,211,212,-1,213,214,215,-1,216,217,218,-1,219,220,221,-1,222,223,224,-1,225,226,227,-1,228,229,230,-1,231,232,233,-1,234,235,236,-1,237,238,239,-1,240,241,242,-1,243,244,245,-1,246,247,248,-1,249,250,251,-1,252,253,254,-1,255,256,257,-1,258,259,260,-1,261,262,263,-1,264,265,266,-1,267,268,269,-1,270,271,272,-1,273,274,275,-1,276,277,278,-1,279,280,281,-1,282,283,284,-1,285,286,287,-1,288,289,290,-1,291,292,293,-1,294,295,296,-1,297,298,299,-1,300,301,302,-1,303,304,305,-1,306,307,308,-1,309,310,311,-1,312,313,314,-1,315,316,317,-1,318,319,320,-1,321,322,323,-1,324,325,326,-1,327,328,329,-1,330,331,332,-1,333,334,335,-1,336,337,338,-1,339,340,341,-1,342,343,344,-1,345,346,347,-1,348,349,350,-1,351,352,353,-1,354,355,356,-1,357,358,359,-1,360,361,362,-1,363,364,365,-1,366,367,368,-1,369,370,371,-1,372,373,374,-1,375,376,377,-1,378,379,380,-1,381,382,383,-1,384,385,386,-1,387,388,389,-1,390,391,392,-1,393,394,395,-1,396,397,398,-1,399,400,401,-1,402,403,404,-1,405,406,407,-1,408,409,410,-1,411,412,413,-1,414,415,416,-1,417,418,419,-1,420,421,422,-1,423,424,425,-1,426,427,428,-1,429,430,431,-1,432,433,434,-1,435,436,437,-1,438,439,440,-1,441,442,443,-1,444,445,446,-1,447,448,449,-1,450,451,452,-1,453,454,455,-1,456,457,458,-1,459,460,461,-1,462,463,464,-1,465,466,467,-1,468,469,470,-1,471,472,473,-1,474,475,476,-1,477,478,479,-1,480,481,482,-1,483,484,485,-1,486,487,488,-1,489,490,491,-1,492,493,494,-1,495,496,497,-1,498,499,500,-1,501,502,503,-1,504,505,506,-1,507,508,509,-1,510,511,512,-1,513,514,515,-1,516,517,518,-1,519,520,521,-1,522,523,524,-1,525,526,527,-1,528,529,530,-1,531,532,533,-1,534,535,536,-1,537,538,539,-1,540,541,542,-1,543,544,545,-1,546,547,548,-1,549,550,551,-1,552,553,554,-1,555,556,557,-1,558,559,560,-1,561,562,563,-1,564,565,566,-1,567,568,569,-1,570,571,572,-1,573,574,575,-1,576,577,578,-1,579,580,581,-1,582,583,584,-1,585,586,587,-1,588,589,590,-1,591,592,593,-1,594,595,596,-1,597,598,599,-1,600,601,602,-1,603,604,605,-1,606,607,608,-1,609,610,611,-1,612,613,614,-1,615,616,617,-1,618,619,620,-1,621,622,623,-1,624,625,626,-1,627,628,629,-1,630,631,632,-1,633,634,635,-1,636,637,638,-1,639,640,641,-1,642,643,644,-1,645,646,647,-1,648,649,650,-1,651,652,653,-1,654,655,656,-1,657,658,659,-1,660,661,662,-1,663,664,665,-1,666,667,668,-1,669,670,671,-1,672,673,674,-1,675,676,677,-1,678,679,680,-1,681,682,683,-1,684,685,686,-1,687,688,689,-1,690,691,692,-1,694,695,693,-1])
IndexedFaceSet488.setCreaseAngle(1.57)
Coordinate489 = Coordinate()
Coordinate489.setPoint([0.18,-1.44,-5.74,0.25,-1.72,-5.87,0.16,-1.72,-5.43,0.66,-1.6,-5.35,0.61,-1.56,-5.31,0.48,-1.72,-5.34,0.61,-1.56,-5.31,0.48,-1.52,-5.29,0.48,-1.72,-5.34,0.35,-1.4,-5.95,0.25,-1.72,-5.87,0.18,-1.44,-5.74,0.81,-1.6,-5.9,0.8,-1.68,-5.93,0.78,-1.56,-6.02,0.96,-1.6,-5.72,0.93,-1.68,-5.63,0.89,-1.68,-5.77,0.96,-1.6,-5.72,1.01,-1.6,-5.64,0.93,-1.68,-5.63,0.66,-1.6,-5.35,0.48,-1.72,-5.34,0.7,-1.76,-5.43,0.16,-1.72,-5.43,0.23,-1.64,-5.37,0.18,-1.44,-5.74,0.81,-1.6,-5.9,0.87,-1.64,-5.83,0.8,-1.68,-5.93,0.87,-1.64,-5.83,0.88,-1.64,-5.8,0.88,-1.68,-5.8,0.89,-1.68,-5.77,0.88,-1.68,-5.8,0.88,-1.64,-5.8,0.89,-1.68,-5.77,0.93,-1.68,-5.63,0.9,-1.84,-5.65,0.96,-1.6,-5.72,0.89,-1.68,-5.77,0.88,-1.64,-5.8,0.85,-1.6,-5.62,0.84,-1.8,-5.55,0.93,-1.68,-5.63,0.97,-1.6,-5.59,0.85,-1.6,-5.62,0.93,-1.68,-5.63,1.01,-1.6,-5.64,0.97,-1.6,-5.59,0.93,-1.68,-5.63,0.25,-1.72,-5.87,0.15,-1.84,-5.8,0.16,-1.72,-5.43,0.21,-2.24,-5.95,0.13,-2.08,-5.9,0.56,-1.96,-5.96,0.36,-1.76,-5.31,0.48,-1.72,-5.34,0.48,-1.52,-5.29,0.16,-1.72,-5.43,0.08,-1.92,-5.3,0.24,-1.88,-5.27,0.23,-1.64,-5.37,0.31,-1.8,-5.31,0.36,-1.76,-5.31,0.88,-1.68,-5.8,0.9,-1.76,-5.8,0.8,-1.68,-5.93,0.87,-1.64,-5.83,0.88,-1.68,-5.8,0.8,-1.68,-5.93,0.85,-1.6,-5.62,0.79,-1.6,-5.55,0.84,-1.8,-5.55,0.45,-1.8,-5.36,0.36,-1.76,-5.31,0.31,-1.8,-5.31,0.23,-1.64,-5.37,0.36,-1.76,-5.31,0.48,-1.52,-5.29,0.24,-1.88,-5.27,0.32,-1.84,-5.28,0.31,-1.8,-5.31,0.15,-1.84,-5.8,-0.01,-1.92,-5.62,0.16,-1.72,-5.43,0.8,-1.84,-5.96,0.56,-1.96,-5.96,0.51,-1.52,-6.05,0.9,-1.76,-5.8,0.88,-1.68,-5.8,0.89,-1.68,-5.77,0.81,-1.6,-5.9,0.89,-1.6,-5.88,0.87,-1.64,-5.83,0.93,-1.68,-5.63,0.84,-1.8,-5.55,0.9,-1.84,-5.65,0.89,-1.68,-5.77,0.9,-1.84,-5.65,0.9,-1.76,-5.8,0.7,-1.76,-5.43,0.75,-1.56,-5.46,0.66,-1.6,-5.35,0.8,-2,-5.93,0.8,-1.84,-5.96,0.9,-1.76,-5.8,0.45,-1.8,-5.36,0.48,-1.8,-5.38,0.48,-1.72,-5.34,0.64,-2.28,-6.01,0.5,-2.52,-5.79,0.26,-2.48,-5.83,0.8,-1.68,-5.93,0.51,-1.52,-6.05,0.78,-1.56,-6.02,0.9,-1.76,-5.8,0.8,-1.84,-5.96,0.8,-1.68,-5.93,0.72,-2.04,-5.61,0.85,-2.12,-5.8,0.9,-1.84,-5.65,0.7,-1.76,-5.43,0.84,-1.8,-5.55,0.79,-1.6,-5.55,0.24,-1.88,-5.27,0.34,-1.88,-5.3,0.32,-1.84,-5.28,0.23,-1.64,-5.37,0.16,-1.72,-5.43,0.31,-1.8,-5.31,0.16,-1.72,-5.43,0.24,-1.88,-5.27,0.31,-1.8,-5.31,0.12,-2,-5.26,-0.05,-2.12,-5.32,0.05,-2.2,-5.28,-0.09,-2.24,-5.73,-0.01,-1.92,-5.62,-0.03,-2.24,-5.87,0.8,-1.84,-5.96,0.8,-2,-5.93,0.56,-1.96,-5.96,0.8,-1.68,-5.93,0.8,-1.84,-5.96,0.51,-1.52,-6.05,0.7,-1.76,-5.43,0.79,-1.6,-5.55,0.75,-1.56,-5.46,0.44,-2,-5.42,0.52,-1.96,-5.54,0.48,-1.8,-5.38,-0.03,-1.96,-5.52,-0.09,-2.24,-5.73,0,-2.2,-5.5,0.13,-2.08,-5.9,0.15,-1.84,-5.8,0.56,-1.96,-5.96,0.25,-1.72,-5.87,0.35,-1.4,-5.95,0.51,-1.52,-6.05,0.8,-2,-5.93,0.9,-1.76,-5.8,0.9,-1.84,-5.65,0.8,-2,-5.93,0.9,-1.84,-5.65,0.85,-2.12,-5.8,0.48,-1.72,-5.34,0.48,-1.8,-5.38,0.7,-1.76,-5.43,0.7,-1.76,-5.43,0.48,-1.8,-5.38,0.66,-1.88,-5.54,0.12,-2,-5.26,0.26,-1.92,-5.24,0.24,-1.88,-5.27,-0.07,-2.12,-5.41,-0.03,-1.96,-5.52,0,-2.2,-5.5,0.26,-2.04,-5.24,0.12,-2,-5.26,0.05,-2.2,-5.28,0.21,-2.24,-5.95,0.64,-2.28,-6.01,0.26,-2.48,-5.83,0.61,-2.04,-5.62,0.72,-2.04,-5.61,0.66,-1.88,-5.54,0.52,-1.96,-5.54,0.66,-1.88,-5.54,0.48,-1.8,-5.38,0.08,-1.92,-5.3,0.12,-2,-5.26,0.24,-1.88,-5.27,-0.06,-2.24,-5.27,0.05,-2.28,-5.32,0.05,-2.2,-5.28,-0.03,-1.96,-5.52,0.16,-1.72,-5.43,-0.01,-1.92,-5.62,0.61,-2.04,-5.62,0.52,-1.96,-5.54,0.52,-2.04,-5.63,-0.07,-2.12,-5.41,-0.05,-2.12,-5.32,0.08,-1.92,-5.3,-0.03,-1.96,-5.52,-0.07,-2.12,-5.41,0.08,-1.92,-5.3,0,-2.2,-5.5,-0.09,-2.24,-5.73,-0.07,-2.44,-5.48,0.52,-1.96,-5.54,0.61,-2.04,-5.62,0.66,-1.88,-5.54,0.84,-1.8,-5.55,0.7,-1.76,-5.43,0.66,-1.88,-5.54,0.61,-2.04,-5.62,0.54,-2.16,-5.53,0.73,-2.16,-5.61,0,-2.2,-5.5,-0.07,-2.44,-5.48,-0.15,-2.36,-5.41,0.73,-2.16,-5.61,0.72,-2.04,-5.61,0.61,-2.04,-5.62,0.47,-2.16,-5.55,0.33,-2.16,-5.54,0.32,-2.16,-5.59,0.47,-2.16,-5.55,0.52,-2.04,-5.63,0.52,-1.96,-5.54,0.44,-2,-5.42,0.47,-2.16,-5.55,0.52,-1.96,-5.54,0.33,-2.08,-5.43,0.33,-2.16,-5.54,0.47,-2.16,-5.55,-0.05,-2.12,-5.32,0.12,-2,-5.26,0.08,-1.92,-5.3,-0.01,-1.92,-5.62,0.13,-2.08,-5.9,-0.03,-2.24,-5.87,0.77,-2.24,-5.56,0.73,-2.16,-5.61,0.55,-2.28,-5.44,0.72,-2.04,-5.61,0.84,-1.8,-5.55,0.66,-1.88,-5.54,0.61,-2.04,-5.62,0.52,-2.04,-5.63,0.54,-2.16,-5.53,0.47,-2.16,-5.55,0.54,-2.16,-5.53,0.52,-2.04,-5.63,0.44,-2,-5.42,0.33,-2.08,-5.43,0.47,-2.16,-5.55,0.3,-2.16,-5.49,0.33,-2.16,-5.54,0.33,-2.08,-5.43,-0.1,-2.2,-5.41,-0.05,-2.12,-5.32,-0.07,-2.12,-5.41,-0.1,-2.2,-5.41,-0.07,-2.12,-5.41,0,-2.2,-5.5,-0.03,-1.96,-5.52,0.08,-1.92,-5.3,0.16,-1.72,-5.43,0.64,-2.28,-6.01,0.63,-2.48,-5.77,0.5,-2.52,-5.79,0.7,-2.16,-6,0.56,-1.96,-5.96,0.8,-2,-5.93,0.7,-2.16,-6,0.8,-2,-5.93,0.85,-2.12,-5.8,0.72,-2.04,-5.61,0.73,-2.16,-5.61,0.85,-2.12,-5.8,0.73,-2.16,-5.61,0.54,-2.16,-5.53,0.55,-2.28,-5.44,0.3,-2.16,-5.49,0.42,-2.2,-5.51,0.33,-2.16,-5.54,0.26,-2.2,-5.45,0.3,-2.16,-5.49,0.31,-2.12,-5.41,0.3,-2.16,-5.49,0.33,-2.08,-5.43,0.31,-2.12,-5.41,-0.06,-2.24,-5.27,-0.05,-2.12,-5.32,-0.1,-2.2,-5.41,-0.06,-2.24,-5.27,0.05,-2.2,-5.28,-0.05,-2.12,-5.32,0.13,-2.08,-5.9,-0.01,-1.92,-5.62,0.15,-1.84,-5.8,0.72,-2.04,-5.61,0.9,-1.84,-5.65,0.84,-1.8,-5.55,0.77,-2.24,-5.56,0.55,-2.28,-5.44,0.72,-2.36,-5.53,0.72,-2.36,-5.53,0.55,-2.28,-5.44,0.58,-2.36,-5.45,0.8,-2.4,-5.78,0.76,-2.4,-5.58,0.77,-2.48,-5.65,0.54,-2.16,-5.53,0.51,-2.2,-5.48,0.55,-2.28,-5.44,0.51,-2.2,-5.48,0.42,-2.2,-5.51,0.49,-2.24,-5.45,0.49,-2.24,-5.45,0.42,-2.2,-5.51,0.3,-2.28,-5.4,0.46,-2.4,-5.4,0.55,-2.28,-5.44,0.49,-2.24,-5.45,-0.1,-2.2,-5.41,0,-2.2,-5.5,-0.15,-2.36,-5.41,-0.03,-2.24,-5.87,-0.02,-2.32,-5.87,-0.09,-2.24,-5.73,-0.02,-2.32,-5.87,0.21,-2.24,-5.95,0.26,-2.48,-5.83,0.76,-2.4,-5.58,0.8,-2.4,-5.78,0.82,-2.24,-5.82,0.73,-2.16,-5.61,0.82,-2.24,-5.82,0.85,-2.12,-5.8,0.77,-2.24,-5.56,0.72,-2.36,-5.53,0.76,-2.4,-5.58,0.73,-2.16,-5.61,0.77,-2.24,-5.56,0.82,-2.24,-5.82,0.51,-2.2,-5.48,0.49,-2.24,-5.45,0.55,-2.28,-5.44,0.3,-2.28,-5.4,0.42,-2.2,-5.51,0.3,-2.16,-5.49,0.26,-2.2,-5.45,0.3,-2.28,-5.4,0.3,-2.16,-5.49,0.05,-2.2,-5.28,0.05,-2.28,-5.32,0.13,-2.28,-5.34,-0.06,-2.24,-5.27,-0.15,-2.36,-5.41,-0.11,-2.4,-5.31,-0.06,-2.24,-5.27,-0.1,-2.2,-5.41,-0.15,-2.36,-5.41,-0.03,-1.96,-5.52,-0.01,-1.92,-5.62,-0.09,-2.24,-5.73,-0.09,-2.24,-5.73,-0.02,-2.44,-5.79,-0.08,-2.48,-5.6,-0.06,-2.56,-5.62,-0.08,-2.48,-5.6,-0.02,-2.44,-5.79,-0.09,-2.24,-5.73,-0.08,-2.48,-5.6,-0.07,-2.44,-5.48,0.13,-2.08,-5.9,0.21,-2.24,-5.95,-0.03,-2.24,-5.87,0.21,-2.24,-5.95,-0.02,-2.32,-5.87,-0.03,-2.24,-5.87,0.15,-1.84,-5.8,0.25,-1.72,-5.87,0.56,-1.96,-5.96,0.25,-1.72,-5.87,0.51,-1.52,-6.05,0.56,-1.96,-5.96,0.64,-2.28,-6.01,0.7,-2.16,-6,0.74,-2.28,-5.96,0.82,-2.24,-5.82,0.74,-2.28,-5.96,0.7,-2.16,-6,0.82,-2.24,-5.82,0.7,-2.16,-6,0.85,-2.12,-5.8,0.72,-2.36,-5.53,0.6,-2.4,-5.47,0.61,-2.44,-5.5,0.46,-2.4,-5.4,0.49,-2.24,-5.45,0.3,-2.28,-5.4,0.26,-2.2,-5.45,0.26,-2.24,-5.39,0.3,-2.28,-5.4,0.3,-2.28,-5.4,0.31,-2.52,-5.39,0.4,-2.44,-5.37,0.01,-2.52,-5.32,0.03,-2.64,-5.37,0.2,-2.56,-5.38,-0.03,-2.36,-5.26,0.05,-2.28,-5.32,-0.06,-2.24,-5.27,-0.03,-2.36,-5.26,-0.06,-2.24,-5.27,-0.11,-2.4,-5.31,0.74,-2.28,-5.96,0.71,-2.44,-5.83,0.64,-2.28,-6.01,0.74,-2.28,-5.96,0.82,-2.24,-5.82,0.8,-2.4,-5.78,0.58,-2.36,-5.45,0.55,-2.28,-5.44,0.46,-2.4,-5.4,0.01,-2.52,-5.32,0.2,-2.56,-5.38,0.13,-2.28,-5.34,-0.02,-2.44,-5.79,-0.02,-2.32,-5.87,0.26,-2.48,-5.83,0.57,-2.56,-5.69,0.47,-2.56,-5.73,0.5,-2.52,-5.79,0.71,-2.44,-5.83,0.8,-2.4,-5.78,0.69,-2.48,-5.77,0.77,-2.24,-5.56,0.76,-2.4,-5.58,0.82,-2.24,-5.82,0.72,-2.48,-5.61,0.6,-2.56,-5.64,0.62,-2.52,-5.69,0.6,-2.4,-5.47,0.72,-2.36,-5.53,0.58,-2.36,-5.45,0.58,-2.4,-5.46,0.6,-2.4,-5.47,0.58,-2.36,-5.45,-0.03,-2.36,-5.26,-0.11,-2.4,-5.31,0.01,-2.52,-5.32,0.03,-2.68,-5.59,0.01,-2.64,-5.51,-0.06,-2.56,-5.62,0.71,-2.44,-5.83,0.69,-2.48,-5.77,0.63,-2.48,-5.77,0.71,-2.44,-5.83,0.74,-2.28,-5.96,0.8,-2.4,-5.78,0.8,-2.4,-5.78,0.77,-2.48,-5.65,0.69,-2.48,-5.77,0.77,-2.48,-5.65,0.76,-2.4,-5.58,0.72,-2.48,-5.61,0.76,-2.4,-5.58,0.72,-2.36,-5.53,0.61,-2.44,-5.5,0.6,-2.56,-5.64,0.72,-2.48,-5.61,0.61,-2.44,-5.5,0.6,-2.4,-5.47,0.58,-2.4,-5.46,0.61,-2.44,-5.5,0.51,-2.56,-5.51,0.4,-2.44,-5.37,0.31,-2.52,-5.39,0.58,-2.4,-5.46,0.58,-2.36,-5.45,0.46,-2.4,-5.4,0.51,-2.56,-5.51,0.46,-2.4,-5.4,0.4,-2.44,-5.37,0.3,-2.28,-5.4,0.13,-2.28,-5.34,0.31,-2.52,-5.39,-0.07,-2.44,-5.48,-0.09,-2.48,-5.44,-0.15,-2.36,-5.41,-0.06,-2.48,-5.47,-0.09,-2.48,-5.44,-0.07,-2.44,-5.48,-0.02,-2.64,-5.37,-0.04,-2.6,-5.36,-0.04,-2.56,-5.46,0.33,-2.6,-5.71,0.27,-2.64,-5.63,0.09,-2.64,-5.71,0.64,-2.28,-6.01,0.71,-2.44,-5.83,0.63,-2.48,-5.77,0.21,-2.24,-5.95,0.56,-1.96,-5.96,0.64,-2.28,-6.01,0.72,-2.48,-5.61,0.76,-2.4,-5.58,0.61,-2.44,-5.5,0.13,-2.28,-5.34,0.2,-2.56,-5.38,0.31,-2.52,-5.39,0.05,-2.28,-5.32,0.01,-2.52,-5.32,0.13,-2.28,-5.34,0.01,-2.52,-5.32,-0.11,-2.4,-5.31,-0.09,-2.48,-5.44,-0.09,-2.48,-5.44,-0.11,-2.4,-5.31,-0.15,-2.36,-5.41,0.05,-2.28,-5.32,-0.03,-2.36,-5.26,0.01,-2.52,-5.32,0.26,-2.48,-5.83,0.33,-2.6,-5.71,0.09,-2.64,-5.71,0.39,-2.56,-5.71,0.33,-2.6,-5.71,0.26,-2.48,-5.83,0.56,-1.96,-5.96,0.7,-2.16,-6,0.64,-2.28,-6.01,0.01,-2.52,-5.32,-0.04,-2.6,-5.36,0.03,-2.64,-5.37,0.01,-2.52,-5.32,-0.09,-2.48,-5.44,-0.04,-2.6,-5.36,-0.08,-2.48,-5.6,-0.06,-2.48,-5.47,-0.07,-2.44,-5.48,-0.04,-2.56,-5.46,-0.06,-2.56,-5.62,0.01,-2.64,-5.51,-0.08,-2.48,-5.6,-0.04,-2.56,-5.46,-0.06,-2.48,-5.47,-0.02,-2.32,-5.87,-0.02,-2.44,-5.79,-0.09,-2.24,-5.73,0.04,-2.56,-5.74,0.26,-2.48,-5.83,0.09,-2.64,-5.71,0.5,-2.52,-5.79,0.39,-2.56,-5.71,0.26,-2.48,-5.83,0.57,-2.56,-5.69,0.5,-2.52,-5.79,0.63,-2.48,-5.77,0.62,-2.52,-5.69,0.57,-2.56,-5.69,0.63,-2.48,-5.77,0.51,-2.56,-5.51,0.61,-2.44,-5.5,0.58,-2.4,-5.46,0.51,-2.56,-5.51,0.58,-2.4,-5.46,0.46,-2.4,-5.4,0.4,-2.44,-5.37,0.46,-2.4,-5.4,0.3,-2.28,-5.4,0.2,-2.56,-5.38,0.19,-2.64,-5.41,0.28,-2.6,-5.46,-0.02,-2.64,-5.37,-0.04,-2.56,-5.46,0.01,-2.64,-5.51,-0.09,-2.48,-5.44,-0.04,-2.56,-5.46,-0.04,-2.6,-5.36,-0.04,-2.56,-5.46,-0.09,-2.48,-5.44,-0.06,-2.48,-5.47,0.5,-2.52,-5.79,0.47,-2.56,-5.73,0.39,-2.56,-5.71,0.57,-2.56,-5.69,0.6,-2.56,-5.64,0.57,-2.6,-5.58,0.6,-2.56,-5.64,0.57,-2.56,-5.69,0.62,-2.52,-5.69,0.57,-2.6,-5.58,0.51,-2.56,-5.51,0.44,-2.64,-5.61,0.57,-2.6,-5.58,0.6,-2.56,-5.64,0.61,-2.44,-5.5,0.51,-2.56,-5.51,0.57,-2.6,-5.58,0.61,-2.44,-5.5,0.32,-2.6,-5.47,0.51,-2.56,-5.51,0.31,-2.52,-5.39,0.32,-2.6,-5.47,0.36,-2.64,-5.52,0.51,-2.56,-5.51,0.51,-2.56,-5.51,0.36,-2.64,-5.52,0.44,-2.64,-5.61,0.28,-2.6,-5.46,0.32,-2.6,-5.47,0.31,-2.52,-5.39,0.32,-2.6,-5.47,0.28,-2.6,-5.46,0.3,-2.64,-5.54,0.19,-2.64,-5.41,0.3,-2.64,-5.54,0.28,-2.6,-5.46,0.19,-2.64,-5.41,0.2,-2.56,-5.38,0.03,-2.64,-5.37,-0.04,-2.6,-5.36,-0.02,-2.64,-5.37,0.03,-2.64,-5.37,0.03,-2.68,-5.59,-0.06,-2.56,-5.62,0.06,-2.64,-5.68,-0.06,-2.56,-5.62,-0.02,-2.44,-5.79,0.04,-2.56,-5.74,-0.04,-2.56,-5.46,-0.08,-2.48,-5.6,-0.06,-2.56,-5.62,0.04,-2.56,-5.74,0.09,-2.64,-5.71,0.06,-2.64,-5.68,0.04,-2.56,-5.74,-0.02,-2.44,-5.79,0.26,-2.48,-5.83,0.28,-2.64,-5.55,0.36,-2.64,-5.52,0.32,-2.6,-5.47,0.26,-2.68,-5.54,0.29,-2.68,-5.53,0.27,-2.64,-5.63,0.26,-2.68,-5.54,0.27,-2.64,-5.63,0.34,-2.68,-5.6,0.34,-2.68,-5.6,0.27,-2.64,-5.63,0.33,-2.6,-5.71,0.4,-2.64,-5.61,0.34,-2.68,-5.6,0.33,-2.6,-5.71,0.4,-2.64,-5.61,0.33,-2.6,-5.71,0.39,-2.56,-5.71,0.4,-2.64,-5.61,0.44,-2.64,-5.61,0.34,-2.68,-5.6,0.34,-2.68,-5.6,0.36,-2.64,-5.52,0.29,-2.68,-5.53,0.34,-2.68,-5.6,0.44,-2.64,-5.61,0.36,-2.64,-5.52,0.36,-2.64,-5.52,0.28,-2.64,-5.55,0.29,-2.68,-5.53,0.19,-2.68,-5.58,0.29,-2.68,-5.53,0.28,-2.64,-5.55,0.14,-2.64,-5.59,0.19,-2.68,-5.58,0.28,-2.64,-5.55,0.14,-2.64,-5.59,0.1,-2.64,-5.58,0.06,-2.68,-5.61,-0.06,-2.56,-5.62,0.04,-2.56,-5.74,0.06,-2.64,-5.68,0.03,-2.68,-5.59,0.06,-2.64,-5.68,0.09,-2.68,-5.66,0.14,-2.64,-5.59,0.06,-2.68,-5.61,0.19,-2.68,-5.58])

IndexedFaceSet488.setCoord(Coordinate489)

Shape485.setGeometry(IndexedFaceSet488)

Transform484.addChildren(Shape485)

fieldValue483.addChildren(Transform484)

ProtoInstance481.addFieldValue(fieldValue483)

fieldValue480.addChildren(ProtoInstance481)

ProtoInstance477.addFieldValue(fieldValue480)

fieldValue466.addChildren(ProtoInstance477)

ProtoInstance463.addFieldValue(fieldValue466)

fieldValue452.addChildren(ProtoInstance463)

ProtoInstance449.addFieldValue(fieldValue452)

fieldValue397.addChildren(ProtoInstance449)
ProtoInstance490 = ProtoInstance()
ProtoInstance490.setName("Joint")
ProtoInstance490.setDEF("Allen_hanim_vc4")
fieldValue491 = fieldValue()
fieldValue491.setName("name")
fieldValue491.setValue("vc4")

ProtoInstance490.addFieldValue(fieldValue491)
fieldValue492 = fieldValue()
fieldValue492.setName("center")
fieldValue492.setValue("0 1.43 -0.0458")

ProtoInstance490.addFieldValue(fieldValue492)
fieldValue493 = fieldValue()
fieldValue493.setName("children")
ProtoInstance494 = ProtoInstance()
ProtoInstance494.setName("Segment")
ProtoInstance494.setDEF("Allen_hanim_c4")
fieldValue495 = fieldValue()
fieldValue495.setName("name")
fieldValue495.setValue("c4")

ProtoInstance494.addFieldValue(fieldValue495)
fieldValue496 = fieldValue()
fieldValue496.setName("children")
Transform497 = Transform()
Transform497.setDEF("neck_adjust")
Transform497.setCenter([-0.36,1.03,0.04])
Transform497.setRotation([0,1,0,1.570796])
Transform497.setScale([0.1,0.1,0.1])
Shape498 = Shape()
Appearance499 = Appearance()
Material500 = Material()
Material500.setUSE("Skin_Color")

Appearance499.setMaterial(Material500)
ImageTexture501 = ImageTexture()
ImageTexture501.setUSE("camo")

Appearance499.setTexture(ImageTexture501)

Shape498.setAppearance(Appearance499)
IndexedFaceSet502 = IndexedFaceSet()
IndexedFaceSet502.setCoordIndex([0,1,2,-1,3,4,5,-1,6,7,8,-1,9,10,11,-1,12,13,14,-1,15,16,17,-1,18,19,20,-1,21,22,23,-1,24,25,26,-1,27,28,29,-1,30,31,32,-1,33,34,35,-1,36,37,38,-1,39,40,41,-1,42,43,44,-1,45,46,47,-1,48,49,50,-1,51,52,53,-1,54,55,56,-1,57,58,59,-1,60,61,62,-1,63,64,65,-1,66,67,68,-1,69,70,71,-1,72,73,74,-1,75,76,77,-1,78,79,80,-1,81,82,83,-1,84,85,86,-1,87,88,89,-1,90,91,92,-1,93,94,95,-1,96,97,98,-1,99,100,101,-1,102,103,104,-1,105,106,107,-1,108,109,110,-1,111,112,113,-1,114,115,116,-1,117,118,119,-1,120,121,122,-1,123,124,125,-1,126,127,128,-1,129,130,131,-1,132,133,134,-1,135,136,137,-1,138,139,140,-1,141,142,143,-1,144,145,146,-1,147,148,149,-1,150,151,152,-1,153,154,155,-1,156,157,158,-1,159,160,161,-1,162,163,164,-1,165,166,167,-1,168,169,170,-1,171,172,173,-1,174,175,176,-1,177,178,179,-1,180,181,182,-1,183,184,185,-1,186,187,188,-1,189,190,191,-1,192,193,194,-1,195,196,197,-1,198,199,200,-1,201,202,203,-1,204,205,206,-1,207,208,209,-1,210,211,212,-1,213,214,215,-1,216,217,218,-1,219,220,221,-1,222,223,224,-1,225,226,227,-1,228,229,230,-1,231,232,233,-1,234,235,236,-1,237,238,239,-1,240,241,242,-1,243,244,245,-1,246,247,248,-1,249,250,251,-1,252,253,254,-1,255,256,257,-1,258,259,260,-1,261,262,263,-1,264,265,266,-1,267,268,269,-1,270,271,272,-1,273,274,275,-1,276,277,278,-1,279,280,281,-1,282,283,284,-1,285,286,287,-1,288,289,290,-1,291,292,293,-1,294,295,296,-1,297,298,299,-1,300,301,302,-1,303,304,305,-1,306,307,308,-1,309,310,311,-1,312,313,314,-1,315,316,317,-1,318,319,320,-1,321,322,323,-1,324,325,326,-1,327,328,329,-1,330,331,332,-1,333,334,335,-1,336,337,338,-1,339,340,341,-1,342,343,344,-1,345,346,347,-1,348,349,350,-1,351,352,353,-1,354,355,356,-1,357,358,359,-1,360,361,362,-1,363,364,365,-1,366,367,368,-1,369,370,371,-1,372,373,374,-1,375,376,377,-1,378,379,380,-1,381,382,383,-1,384,385,386,-1,387,388,389,-1,390,391,392,-1,393,394,395,-1,396,397,398,-1,399,400,401,-1,402,403,404,-1,405,406,407,-1,408,409,410,-1,411,412,413,-1,414,415,416,-1,417,418,419,-1,420,421,422,-1,423,424,425,-1,426,427,428,-1,429,430,431,-1,432,433,434,-1,435,436,437,-1,438,439,440,-1,441,442,443,-1,444,445,446,-1,447,448,449,-1,450,451,452,-1,453,454,455,-1,456,457,458,-1,459,460,461,-1,462,463,464,-1,465,466,467,-1,468,469,470,-1,471,472,473,-1,474,475,476,-1,477,478,479,-1,480,481,482,-1,483,484,485,-1,486,487,488,-1,489,490,491,-1,492,493,494,-1,495,496,497,-1,498,499,500,-1,501,502,503,-1,504,505,506,-1,507,508,509,-1,510,511,512,-1,513,514,515,-1,516,517,518,-1,519,520,521,-1,522,523,524,-1,525,526,527,-1,528,529,530,-1,531,532,533,-1,534,535,536,-1,537,538,539,-1,540,541,542,-1,543,544,545,-1,546,547,548,-1,549,550,551,-1,552,553,554,-1,555,556,557,-1,558,559,560,-1,561,562,563,-1,564,565,566,-1,567,568,569,-1,570,571,572,-1,573,574,575,-1,576,577,578,-1,579,580,581,-1,582,583,584,-1])
IndexedFaceSet502.setCreaseAngle(1.91)
Coordinate503 = Coordinate()
Coordinate503.setPoint([0.96,4.75,3.62,0.9,4.59,3.37,0.85,4.67,3.29,0.59,4.51,3.04,0.7,4.55,3.11,0.7,4.51,3.11,0.85,4.67,3.29,0.9,4.59,3.37,0.9,4.55,3.22,0.81,4.55,3.21,0.75,4.71,3.18,0.85,4.67,3.29,0.99,4.55,3.8,1.03,4.55,3.67,0.94,4.63,3.68,0.77,4.55,3.17,0.75,4.71,3.18,0.81,4.55,3.21,0.96,4.75,3.62,0.94,4.63,3.68,0.96,4.59,3.62,1.03,4.55,3.67,0.96,4.59,3.62,0.94,4.63,3.68,0.99,4.55,3.8,0.94,4.63,3.68,0.91,4.55,3.81,0.74,4.51,3.11,0.7,4.51,3.11,0.7,4.55,3.11,0.9,4.59,3.37,0.97,4.55,3.32,0.9,4.55,3.22,0.9,4.59,3.37,0.96,4.75,3.62,0.96,4.59,3.62,0.48,4.51,4.19,0.53,4.47,4.23,0.58,4.51,4.16,0.81,4.55,3.21,0.85,4.67,3.29,0.9,4.55,3.22,0.77,4.55,3.17,0.7,4.55,3.11,0.75,4.71,3.18,0.77,4.55,3.17,0.74,4.51,3.11,0.7,4.55,3.11,0.83,4.51,3.09,0.74,4.51,3.11,0.77,4.55,3.17,0.85,4.51,3.11,0.83,4.51,3.09,0.77,4.55,3.17,1.01,4.55,3.33,1.05,4.55,3.34,1.06,4.51,3.26,1.03,4.55,3.67,1.1,4.51,3.7,1.08,4.55,3.64,1.12,4.47,3.55,1.1,4.51,3.7,1.18,4.23,3.72,1.1,4.51,3.7,1.06,4.51,3.86,1.14,4.23,3.89,0.86,4.51,4.08,0.87,4.47,4.1,0.97,4.51,4.06,0.86,4.51,4.08,0.97,4.51,4.06,0.97,4.55,4.03,0.74,4.51,3.11,0.83,4.51,3.09,0.81,4.47,3.08,0.78,4.47,3.01,0.81,4.47,3.08,0.83,4.51,3.09,0.89,4.47,2.97,0.87,4.47,2.95,0.9,4.51,3.03,0.98,4.51,3.1,1.06,4.39,3.18,0.97,4.43,3.03,0.98,4.51,3.1,0.97,4.43,3.03,0.89,4.47,2.97,1.12,4.47,3.55,1.1,4.43,3.34,1.05,4.55,3.34,1.08,4.55,3.64,1.12,4.47,3.55,1.05,4.55,3.34,1.1,4.51,3.7,1.12,4.47,3.55,1.08,4.55,3.64,1.1,4.51,3.7,0.99,4.55,3.8,1.06,4.51,3.86,1.03,4.51,3.95,0.97,4.55,4.03,0.97,4.51,4.06,1.03,4.51,3.95,0.98,4.35,4.14,1.14,4.23,3.89,0.95,4.47,4.16,0.97,4.47,4.13,0.88,4.51,4.17,0.88,4.51,4.17,0.89,4.51,4.12,0.95,4.47,4.16,0.53,4.47,4.23,0.48,4.51,4.19,0.43,4.39,4.23,0.23,4.23,4.33,0.33,4.23,4.44,0.41,4.35,4.35,0.87,4.47,2.95,0.87,4.39,2.91,0.76,4.43,2.88,0.97,4.43,3.03,0.95,4.19,2.89,0.87,4.39,2.91,1.06,4.51,3.26,1.1,4.43,3.34,1.06,4.39,3.18,1.1,4.43,3.34,1.06,4.51,3.26,1.05,4.55,3.34,0.86,4.51,4.25,0.92,4.43,4.21,0.95,4.47,4.16,0.6,4.47,4.26,0.53,4.47,4.23,0.54,4.43,4.18,0.54,4.43,4.18,0.53,4.47,4.23,0.43,4.39,4.23,0.48,4.51,4.19,0.36,4.47,4.23,0.43,4.39,4.23,0.61,4.39,2.87,0.62,4.39,2.91,0.67,4.43,2.92,0.67,4.43,2.92,0.74,4.23,2.82,0.61,4.39,2.87,0.76,4.43,2.88,0.67,4.43,2.92,0.73,4.43,3.01,0.87,4.47,2.95,0.76,4.43,2.88,0.73,4.43,3.01,0.87,4.47,2.95,0.89,4.47,2.97,0.87,4.39,2.91,0.89,4.47,2.97,0.97,4.43,3.03,0.87,4.39,2.91,1.06,4.51,3.26,1.06,4.39,3.18,0.98,4.51,3.1,1.1,4.51,3.7,1.03,4.55,3.67,0.99,4.55,3.8,1.06,4.51,3.86,1.03,4.51,3.95,1.14,4.23,3.89,0.97,4.51,4.06,0.97,4.47,4.13,0.98,4.35,4.14,1.03,4.51,3.95,0.97,4.51,4.06,0.98,4.35,4.14,0.96,4.43,4.17,0.97,4.47,4.13,0.95,4.47,4.16,0.92,4.43,4.21,0.96,4.43,4.17,0.95,4.47,4.16,0.83,4.43,4.29,0.86,4.51,4.25,0.79,4.47,4.3,0.92,4.43,4.21,0.95,4.19,4.31,0.98,4.35,4.14,0.92,4.43,4.21,0.83,4.43,4.29,0.95,4.19,4.31,0.7,4.47,4.33,0.65,4.43,4.4,0.76,4.39,4.35,0.5,4.31,4.46,0.57,4.43,4.34,0.41,4.35,4.35,0.47,4.35,4.24,0.43,4.35,4.29,0.43,4.39,4.23,0.43,4.39,4.23,0.36,4.47,4.23,0.36,4.35,4.23,0.54,4.35,2.97,0.56,4.35,3.02,0.52,4.39,3.02,0.21,4.15,2.85,0.63,4.15,2.77,0.54,4.03,2.65,0.61,4.39,2.87,0.74,4.23,2.82,0.63,4.15,2.77,0.95,4.19,2.89,0.93,4.15,2.83,0.74,4.23,2.82,0.97,4.47,4.13,0.96,4.43,4.17,0.98,4.35,4.14,0.83,4.43,4.29,0.92,4.43,4.21,0.86,4.51,4.25,0.59,4.11,4.62,0.63,4.15,4.53,0.48,4.19,4.48,0.43,4.35,4.29,0.36,4.35,4.23,0.41,4.35,4.35,0.23,4.23,4.33,0.41,4.35,4.35,0.36,4.35,4.23,0.36,4.35,4.23,0.47,4.35,4.24,0.43,4.39,4.23,0.33,4.23,4.44,0.5,4.31,4.46,0.41,4.35,4.35,0.56,4.35,3.02,0.54,4.35,2.97,0.47,4.31,2.99,0.5,4.35,2.86,0.47,4.31,2.99,0.54,4.35,2.97,0.83,4.43,4.29,0.7,4.47,4.33,0.76,4.39,4.35,0.5,4.31,4.46,0.65,4.43,4.4,0.57,4.43,4.34,0.23,4.23,4.33,0.36,4.35,4.23,0.18,4.23,4.18,0.43,4.35,4.29,0.47,4.35,4.24,0.36,4.35,4.23,0.31,4.23,2.96,0.38,4.27,2.99,0.45,4.31,2.85,0.5,4.35,2.86,0.45,4.31,2.85,0.47,4.31,2.99,1.18,4.23,3.72,1.1,4.51,3.7,1.14,4.23,3.89,0.72,4.19,4.5,0.65,4.43,4.4,0.5,4.31,4.46,0.83,4.43,4.29,0.89,4.19,4.38,0.95,4.19,4.31,0.5,4.31,4.46,0.33,4.23,4.44,0.48,4.19,4.48,0,4.11,3.22,0.23,4.39,3.02,0.27,4.23,3.01,0.3,4.27,3,0.31,4.23,2.96,0.27,4.23,3.01,0.38,4.27,2.99,0.31,4.23,2.96,0.3,4.27,3,0.21,4.15,2.85,0.54,4.03,2.65,0.37,3.95,2.62,0.38,4.27,2.99,0.47,4.31,2.99,0.45,4.31,2.85,0.45,4.31,2.85,0.5,4.35,2.86,0.63,4.15,2.77,0.7,4.07,2.67,0.74,4.23,2.82,0.82,4.11,2.73,0.72,4.19,4.5,0.89,4.19,4.38,0.76,4.39,4.35,0.72,4.19,4.5,0.76,4.39,4.35,0.65,4.43,4.4,0.06,4.07,4.3,0.17,4.19,4.33,0.15,4.15,4.17,0.07,3.91,2.85,0.03,4.03,2.93,0.21,4.15,2.85,0.23,4.39,3.02,0.3,4.27,3,0.27,4.23,3.01,0.76,4.43,2.88,0.87,4.39,2.91,0.74,4.23,2.82,0.95,4.19,2.89,0.96,4.15,2.85,0.93,4.15,2.83,1.06,4.39,3.18,1.22,4.11,3.11,1.06,4.15,2.96,0.98,4.35,4.14,1.18,4.15,4.07,1.14,4.23,3.89,0.83,4.43,4.29,0.76,4.39,4.35,0.89,4.19,4.38,0.98,4.35,4.14,0.96,4.43,4.17,0.92,4.43,4.21,0.4,3.95,4.68,0.59,4.11,4.62,0.48,4.19,4.48,0.73,4.15,4.6,0.72,4.19,4.5,0.63,4.15,4.53,0.63,4.15,4.53,0.5,4.31,4.46,0.48,4.19,4.48,0.63,4.15,4.53,0.72,4.19,4.5,0.5,4.31,4.46,0.23,4.23,4.33,0.31,4.03,4.45,0.33,4.23,4.44,0.27,4.23,3.01,0.03,4.03,2.93,0.07,4.03,3.16,0.7,4.07,2.67,0.63,4.15,2.77,0.74,4.23,2.82,0.87,4.39,2.91,0.95,4.19,2.89,0.74,4.23,2.82,0.67,4.43,2.92,0.76,4.43,2.88,0.74,4.23,2.82,0.96,4.15,2.85,0.95,4.19,2.89,1.06,4.15,2.96,0.97,4.43,3.03,1.06,4.39,3.18,1.06,4.15,2.96,0.97,4.43,3.03,1.06,4.15,2.96,0.95,4.19,2.89,1.22,4.11,3.11,1.18,4.23,3.72,1.4,3.87,3.79,0.94,4.15,4.46,0.97,4.15,4.45,0.89,4.19,4.38,0.93,4.15,2.83,0.96,4.15,2.85,1,4.11,2.84,1.01,4.11,2.81,1,4.11,2.84,0.96,4.15,2.85,0.4,3.95,4.68,0.48,4.19,4.48,0.31,4.03,4.45,0.18,4.23,4.18,0.17,4.19,4.33,0.23,4.23,4.33,0.21,4.15,2.85,0.37,3.95,2.62,0.21,3.99,2.73,0.27,4.23,3.01,0.31,4.23,2.96,0.21,4.15,2.85,0.5,4.35,2.86,0.61,4.39,2.87,0.63,4.15,2.77,0.93,4.15,2.83,0.86,4.11,2.77,0.74,4.23,2.82,0.86,4.11,2.77,0.93,4.15,2.83,1,4.11,2.75,1.06,4.15,2.96,1.22,4.11,3.11,1.12,4.11,2.88,1.12,4.03,4.42,0.97,4.15,4.45,0.96,4.11,4.52,0.96,4.11,4.52,0.89,4.11,4.61,1,4.03,4.63,0.02,4.07,4.22,0.06,4.07,4.3,0.15,4.15,4.17,0.02,4.07,4.22,0.15,4.15,4.17,0.11,4.11,4.12,0.04,4.03,4.09,0.02,4.07,4.22,0.11,4.11,4.12,-0.09,4.23,3.93,0.01,3.99,4,0.04,4.03,4.09,0.07,4.03,3.16,0.03,4.03,2.93,-0.04,3.99,3.02,0.27,4.23,3.01,0.21,4.15,2.85,0.03,4.03,2.93,0.7,4.07,2.67,0.82,4.11,2.73,0.84,4.07,2.71,0.86,4.11,2.77,0.82,4.11,2.73,0.74,4.23,2.82,0.84,4.07,2.71,0.82,4.11,2.73,0.86,4.07,2.65,1,4.11,2.75,1.04,4.03,2.61,0.97,4.07,2.66,1,4.11,2.75,1.04,4.11,2.76,1.04,4.03,2.61,1.12,4.03,4.42,1.03,4.15,4.38,0.97,4.15,4.45,0.94,4.15,4.46,0.96,4.11,4.52,0.97,4.15,4.45,0.96,4.11,4.52,0.86,4.15,4.55,0.89,4.11,4.61,0.86,4.15,4.55,0.96,4.11,4.52,0.94,4.15,4.46,0.18,4.23,4.18,0.15,4.15,4.17,0.17,4.19,4.33,0.23,4.23,4.33,0.17,4.19,4.33,0.31,4.03,4.45,0.54,4.03,2.65,0.63,4.15,2.77,0.65,4.03,2.63,0.63,4.15,2.77,0.7,4.07,2.67,0.65,4.03,2.63,1,4.03,2.57,0.97,4.07,2.66,1.04,4.03,2.61,0.04,4.03,4.09,-0.07,3.99,4.14,0.02,4.07,4.22,0,4.11,3.22,0.27,4.23,3.01,0.07,4.03,3.16,0.21,4.15,2.85,0.31,4.23,2.96,0.45,4.31,2.85,0.21,4.15,2.85,0.45,4.31,2.85,0.63,4.15,2.77,0.74,4.03,2.54,0.65,4.03,2.63,0.7,4.07,2.67,0.31,4.03,4.45,0.48,4.19,4.48,0.33,4.23,4.44,0.17,4.19,4.33,0.06,4.07,4.3,0.31,4.03,4.45,-0.09,4.23,3.93,0.04,4.03,4.09,0.11,4.11,4.12,0.07,3.91,2.85,0.21,4.15,2.85,0.21,3.99,2.73,1.03,4.15,4.38,1.18,4.15,4.07,0.95,4.19,4.31,1.12,4.03,4.42,0.96,4.11,4.52,1,4.03,4.63,1.1,4.43,3.34,1.12,4.47,3.55,1.18,4.23,3.72,1.22,4.11,3.11,1.1,4.43,3.34,1.18,4.23,3.72,1.18,4.15,4.07,0.98,4.35,4.14,0.95,4.19,4.31,1.4,3.87,3.79,1.18,4.23,3.72,1.14,4.23,3.89,1.4,3.87,3.79,1.14,4.23,3.89,1.18,4.15,4.07,1.22,4.11,3.11,1.06,4.39,3.18,1.1,4.43,3.34,1.03,4.15,4.38,1.12,4.03,4.42,1.18,4.15,4.07,0.71,4.39,3.03,0.69,4.39,3.05,0.73,4.43,3.01,0.61,4.47,3.02,0.59,4.43,3.05,0.52,4.47,3.01,0.61,4.47,3.02,0.52,4.47,3.01,0.59,4.51,3.04,0.52,4.39,3.02,0.59,4.43,3.05,0.6,4.39,3.02,0.59,4.43,3.05,0.52,4.39,3.02,0.52,4.47,3.01,0.74,4.47,4.3,0.64,4.47,4.25,0.67,4.43,4.24,0.91,4.55,3.81,0.76,4.63,4,0.78,4.55,4.01,0.76,4.55,4.03,0.78,4.55,4.01,0.76,4.63,4,0.76,4.55,4.03,0.76,4.63,4,0.72,4.59,4.04,0.71,4.55,4.07,0.72,4.59,4.04,0.66,4.55,4.11,0.83,4.51,4.1,0.86,4.51,4.08,0.78,4.55,4.01,0.78,4.55,4.01,0.76,4.55,4.03,0.83,4.51,4.1,0.81,4.51,4.12,0.83,4.51,4.1,0.76,4.55,4.03,0.81,4.51,4.12,0.71,4.55,4.07,0.66,4.51,4.11,0.81,4.51,4.12,0.76,4.55,4.03,0.71,4.55,4.07,0.71,4.55,4.07,0.76,4.55,4.03,0.72,4.59,4.04,0.66,4.55,4.11,0.66,4.51,4.11,0.71,4.55,4.07,0.66,4.51,4.11,0.66,4.55,4.11,0.58,4.51,4.16,0.86,4.51,4.08,0.83,4.51,4.1,0.82,4.47,4.17,0.83,4.51,4.1,0.81,4.51,4.12,0.82,4.47,4.17,0.9,4.51,4.08,0.97,4.55,4.03,0.91,4.51,3.96,0.97,4.55,4.03,0.97,4.55,3.96,0.91,4.51,3.96,0.56,4.35,3.02,0.47,4.31,2.99,0.52,4.39,3.02])

IndexedFaceSet502.setCoord(Coordinate503)

Shape498.setGeometry(IndexedFaceSet502)

Transform497.addChildren(Shape498)

fieldValue496.addChildren(Transform497)

ProtoInstance494.addFieldValue(fieldValue496)

fieldValue493.addChildren(ProtoInstance494)
ProtoInstance504 = ProtoInstance()
ProtoInstance504.setName("Joint")
ProtoInstance504.setDEF("Allen_hanim_skullbase")
fieldValue505 = fieldValue()
fieldValue505.setName("name")
fieldValue505.setValue("skullbase")

ProtoInstance504.addFieldValue(fieldValue505)
fieldValue506 = fieldValue()
fieldValue506.setName("rotation")
fieldValue506.setValue("0 1 0 0")

ProtoInstance504.addFieldValue(fieldValue506)
fieldValue507 = fieldValue()
fieldValue507.setName("center")
fieldValue507.setValue("0 1.4 0")

ProtoInstance504.addFieldValue(fieldValue507)
fieldValue508 = fieldValue()
fieldValue508.setName("children")
ProtoInstance509 = ProtoInstance()
ProtoInstance509.setName("Segment")
ProtoInstance509.setDEF("Allen_hanim_skull")
fieldValue510 = fieldValue()
fieldValue510.setName("name")
fieldValue510.setValue("skull")

ProtoInstance509.addFieldValue(fieldValue510)
fieldValue511 = fieldValue()
fieldValue511.setName("children")
Transform512 = Transform()
Transform512.setDEF("skull_adjust")
Transform512.setCenter([-0.07,1.33,-0.035])
Transform512.setScale([0.001,0.001,0.001])
Shape513 = Shape()
Appearance514 = Appearance()
Material515 = Material()
Material515.setUSE("Skin_Color")

Appearance514.setMaterial(Material515)
ImageTexture516 = ImageTexture()
ImageTexture516.setDEF("CLONE")
ImageTexture516.setUrl(["clone.gif","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/clone.gif"])

Appearance514.setTexture(ImageTexture516)

Shape513.setAppearance(Appearance514)
IndexedFaceSet517 = IndexedFaceSet()
IndexedFaceSet517.setCoordIndex([0,1,2,-1,2,3,0,-1,4,0,3,-1,3,5,4,-1,6,4,5,-1,5,7,6,-1,8,6,7,-1,9,10,11,-1,11,12,9,-1,13,9,12,-1,12,14,13,-1,15,13,14,-1,14,16,15,-1,17,15,16,-1,16,18,17,-1,19,17,18,-1,20,21,1,-1,1,0,20,-1,22,20,0,-1,0,4,22,-1,23,22,4,-1,4,6,23,-1,24,23,6,-1,6,8,24,-1,25,24,8,-1,26,27,28,-1,28,29,26,-1,30,26,29,-1,29,31,30,-1,32,30,31,-1,31,33,32,-1,34,32,33,-1,33,35,34,-1,36,34,35,-1,35,37,36,-1,38,36,37,-1,37,10,38,-1,39,38,10,-1,10,9,39,-1,40,39,9,-1,9,13,40,-1,41,40,13,-1,13,15,41,-1,42,41,15,-1,15,17,42,-1,43,42,17,-1,17,19,43,-1,44,43,19,-1,19,45,44,-1,46,44,45,-1,45,47,46,-1,48,46,47,-1,47,49,48,-1,50,48,49,-1,49,51,50,-1,52,50,51,-1,51,53,52,-1,54,52,53,-1,55,56,21,-1,21,20,55,-1,57,55,20,-1,20,22,57,-1,58,57,22,-1,22,23,58,-1,59,58,23,-1,23,24,59,-1,60,59,24,-1,24,25,60,-1,61,60,25,-1,62,63,64,-1,64,65,62,-1,66,62,65,-1,67,68,69,-1,69,27,67,-1,70,67,27,-1,27,26,70,-1,71,70,26,-1,26,30,71,-1,72,71,30,-1,30,32,72,-1,73,72,32,-1,32,34,73,-1,74,73,34,-1,34,36,74,-1,75,74,36,-1,36,38,75,-1,76,75,38,-1,38,39,76,-1,77,76,39,-1,39,40,77,-1,78,77,40,-1,40,41,78,-1,79,78,41,-1,41,42,79,-1,80,79,42,-1,42,43,80,-1,81,80,43,-1,43,44,81,-1,82,81,44,-1,44,46,82,-1,83,82,46,-1,46,48,83,-1,84,83,48,-1,48,50,84,-1,85,84,50,-1,50,52,85,-1,86,85,52,-1,52,54,86,-1,87,86,54,-1,54,88,87,-1,89,87,88,-1,88,56,89,-1,90,89,56,-1,56,55,90,-1,91,90,55,-1,55,57,91,-1,92,91,57,-1,57,58,92,-1,93,92,58,-1,58,59,93,-1,94,93,59,-1,59,60,94,-1,95,94,60,-1,60,61,95,-1,96,95,61,-1,61,97,96,-1,98,96,97,-1,97,63,98,-1,99,98,63,-1,63,62,99,-1,100,99,62,-1,62,66,100,-1,101,102,68,-1,68,67,101,-1,103,101,67,-1,67,70,103,-1,104,103,70,-1,70,71,104,-1,105,104,71,-1,71,72,105,-1,106,105,72,-1,72,73,106,-1,107,106,73,-1,73,74,107,-1,108,107,74,-1,74,75,108,-1,109,108,75,-1,75,76,109,-1,110,109,76,-1,76,77,110,-1,111,110,77,-1,77,78,111,-1,112,111,78,-1,78,79,112,-1,113,112,79,-1,79,80,113,-1,114,113,80,-1,80,81,114,-1,115,114,81,-1,81,82,115,-1,116,115,82,-1,82,83,116,-1,117,116,83,-1,83,84,117,-1,118,117,84,-1,84,85,118,-1,119,118,85,-1,85,86,119,-1,120,119,86,-1,86,87,120,-1,121,120,87,-1,87,89,121,-1,122,121,89,-1,89,90,122,-1,123,122,90,-1,90,91,123,-1,124,123,91,-1,91,92,124,-1,125,124,92,-1,92,93,125,-1,126,125,93,-1,93,94,126,-1,127,126,94,-1,94,95,127,-1,128,127,95,-1,95,96,128,-1,129,128,96,-1,96,98,129,-1,130,129,98,-1,98,99,130,-1,131,130,99,-1,99,100,131,-1,132,133,102,-1,102,101,132,-1,134,132,101,-1,101,103,134,-1,135,134,103,-1,103,104,135,-1,136,135,104,-1,104,105,136,-1,137,136,105,-1,105,106,137,-1,138,137,106,-1,106,107,138,-1,139,138,107,-1,107,108,139,-1,140,139,108,-1,108,109,140,-1,141,140,109,-1,109,110,141,-1,142,141,110,-1,110,111,142,-1,143,142,111,-1,111,112,143,-1,144,143,112,-1,112,113,144,-1,145,144,113,-1,113,114,145,-1,146,145,114,-1,114,115,146,-1,147,146,115,-1,115,116,147,-1,148,147,116,-1,116,117,148,-1,149,148,117,-1,117,118,149,-1,150,149,118,-1,118,119,150,-1,151,150,119,-1,119,120,151,-1,152,151,120,-1,120,121,152,-1,153,152,121,-1,121,122,153,-1,154,153,122,-1,122,123,154,-1,155,154,123,-1,123,124,155,-1,156,155,124,-1,124,125,156,-1,157,156,125,-1,125,126,157,-1,158,157,126,-1,126,127,158,-1,159,158,127,-1,127,128,159,-1,160,159,128,-1,128,129,160,-1,161,160,129,-1,129,130,161,-1,162,161,130,-1,130,131,162,-1,163,164,165,-1,165,166,163,-1,167,163,166,-1,166,168,167,-1,169,167,168,-1,168,133,169,-1,170,169,133,-1,133,132,170,-1,171,170,132,-1,132,134,171,-1,172,171,134,-1,134,135,172,-1,173,172,135,-1,135,136,173,-1,174,173,136,-1,136,137,174,-1,175,174,137,-1,137,138,175,-1,176,175,138,-1,138,139,176,-1,177,176,139,-1,139,140,177,-1,178,177,140,-1,140,141,178,-1,179,178,141,-1,141,142,179,-1,180,179,142,-1,142,143,180,-1,181,180,143,-1,143,144,181,-1,182,181,144,-1,144,145,182,-1,183,182,145,-1,145,146,183,-1,184,183,146,-1,146,147,184,-1,185,184,147,-1,147,148,185,-1,186,185,148,-1,148,149,186,-1,187,186,149,-1,149,150,187,-1,188,187,150,-1,150,151,188,-1,189,188,151,-1,151,152,189,-1,190,189,152,-1,152,153,190,-1,191,190,153,-1,153,154,191,-1,192,191,154,-1,154,155,192,-1,193,192,155,-1,155,156,193,-1,194,193,156,-1,156,157,194,-1,195,194,157,-1,157,158,195,-1,196,195,158,-1,158,159,196,-1,197,196,159,-1,159,160,197,-1,198,197,160,-1,160,161,198,-1,199,198,161,-1,161,162,199,-1,200,199,162,-1,164,163,201,-1,202,201,163,-1,163,167,202,-1,203,202,167,-1,167,169,203,-1,204,203,169,-1,169,170,204,-1,205,204,170,-1,170,171,205,-1,206,205,171,-1,171,172,206,-1,207,206,172,-1,172,173,207,-1,208,207,173,-1,173,174,208,-1,209,208,174,-1,174,175,209,-1,210,209,175,-1,175,176,210,-1,211,210,176,-1,176,177,211,-1,212,211,177,-1,177,178,212,-1,213,212,178,-1,178,179,213,-1,214,213,179,-1,179,180,214,-1,215,214,180,-1,180,181,215,-1,216,215,181,-1,181,182,216,-1,217,216,182,-1,182,183,217,-1,218,217,183,-1,183,184,218,-1,219,218,184,-1,184,185,219,-1,220,219,185,-1,185,186,220,-1,221,220,186,-1,186,187,221,-1,222,221,187,-1,187,188,222,-1,223,222,188,-1,188,189,223,-1,224,223,189,-1,189,190,224,-1,225,224,190,-1,190,191,225,-1,226,225,191,-1,191,192,226,-1,227,226,192,-1,192,193,227,-1,228,227,193,-1,193,194,228,-1,229,228,194,-1,194,195,229,-1,230,229,195,-1,195,196,230,-1,231,230,196,-1,196,197,231,-1,232,231,197,-1,197,198,232,-1,233,232,198,-1,198,199,233,-1,234,233,199,-1,199,200,234,-1,202,203,235,-1,236,235,203,-1,203,204,236,-1,237,236,204,-1,204,205,237,-1,238,237,205,-1,205,206,238,-1,239,238,206,-1,206,207,239,-1,240,239,207,-1,207,208,240,-1,241,240,208,-1,208,209,241,-1,242,241,209,-1,209,210,242,-1,243,242,210,-1,210,211,243,-1,244,243,211,-1,211,212,244,-1,245,244,212,-1,212,213,245,-1,246,245,213,-1,213,214,246,-1,247,246,214,-1,214,215,247,-1,248,247,215,-1,215,216,248,-1,249,248,216,-1,216,217,249,-1,250,249,217,-1,217,218,250,-1,251,250,218,-1,218,219,251,-1,252,251,219,-1,219,220,252,-1,253,252,220,-1,220,221,253,-1,254,253,221,-1,221,222,254,-1,255,254,222,-1,222,223,255,-1,256,255,223,-1,223,224,256,-1,257,256,224,-1,224,225,257,-1,258,257,225,-1,225,226,258,-1,259,258,226,-1,226,227,259,-1,260,259,227,-1,227,228,260,-1,261,260,228,-1,228,229,261,-1,262,261,229,-1,229,230,262,-1,263,262,230,-1,230,231,263,-1,264,263,231,-1,231,232,264,-1,265,264,232,-1,232,233,265,-1,266,265,233,-1,233,234,266,-1,267,266,234,-1,235,236,268,-1,269,268,236,-1,236,237,269,-1,270,269,237,-1,237,238,270,-1,271,270,238,-1,238,239,271,-1,272,271,239,-1,239,240,272,-1,273,272,240,-1,240,241,273,-1,274,273,241,-1,241,242,274,-1,275,274,242,-1,242,243,275,-1,276,275,243,-1,243,244,276,-1,277,276,244,-1,244,245,277,-1,278,277,245,-1,245,246,278,-1,279,278,246,-1,246,247,279,-1,280,279,247,-1,247,248,280,-1,281,280,248,-1,248,249,281,-1,282,281,249,-1,249,250,282,-1,283,282,250,-1,250,251,283,-1,284,283,251,-1,251,252,284,-1,285,284,252,-1,252,253,285,-1,286,285,253,-1,253,254,286,-1,287,286,254,-1,254,255,287,-1,288,287,255,-1,255,256,288,-1,289,288,256,-1,256,257,289,-1,290,289,257,-1,257,258,290,-1,291,290,258,-1,258,259,291,-1,292,291,259,-1,259,260,292,-1,293,292,260,-1,260,261,293,-1,294,293,261,-1,261,262,294,-1,295,294,262,-1,262,263,295,-1,296,295,263,-1,263,264,296,-1,297,296,264,-1,264,265,297,-1,298,297,265,-1,265,266,298,-1,299,298,266,-1,266,267,299,-1,300,301,268,-1,268,269,300,-1,302,300,269,-1,269,270,302,-1,303,302,270,-1,270,271,303,-1,304,303,271,-1,271,272,304,-1,305,304,272,-1,272,273,305,-1,306,305,273,-1,273,274,306,-1,307,306,274,-1,274,275,307,-1,308,307,275,-1,275,276,308,-1,309,308,276,-1,276,277,309,-1,310,309,277,-1,277,278,310,-1,311,310,278,-1,278,279,311,-1,312,311,279,-1,279,280,312,-1,313,312,280,-1,280,281,313,-1,314,313,281,-1,281,282,314,-1,315,314,282,-1,282,283,315,-1,316,315,283,-1,283,284,316,-1,317,316,284,-1,284,285,317,-1,318,317,285,-1,285,286,318,-1,319,318,286,-1,286,287,319,-1,320,319,287,-1,287,288,320,-1,321,320,288,-1,288,289,321,-1,322,321,289,-1,289,290,322,-1,323,322,290,-1,290,291,323,-1,324,323,291,-1,291,292,324,-1,325,324,292,-1,292,293,325,-1,326,325,293,-1,293,294,326,-1,327,326,294,-1,294,295,327,-1,328,327,295,-1,295,296,328,-1,329,328,296,-1,296,297,329,-1,330,329,297,-1,297,298,330,-1,331,330,298,-1,298,299,331,-1,332,333,301,-1,301,300,332,-1,334,332,300,-1,300,302,334,-1,335,334,302,-1,302,303,335,-1,336,335,303,-1,303,304,336,-1,337,336,304,-1,304,305,337,-1,338,337,305,-1,305,306,338,-1,339,338,306,-1,306,307,339,-1,340,339,307,-1,307,308,340,-1,341,340,308,-1,308,309,341,-1,342,341,309,-1,309,310,342,-1,343,342,310,-1,310,311,343,-1,344,343,311,-1,311,312,344,-1,345,344,312,-1,312,313,345,-1,346,345,313,-1,313,314,346,-1,347,346,314,-1,314,315,347,-1,348,347,315,-1,315,316,348,-1,349,348,316,-1,316,317,349,-1,350,349,317,-1,317,318,350,-1,351,350,318,-1,318,319,351,-1,352,351,319,-1,319,320,352,-1,353,352,320,-1,320,321,353,-1,354,353,321,-1,321,322,354,-1,355,354,322,-1,322,323,355,-1,356,355,323,-1,323,324,356,-1,357,356,324,-1,324,325,357,-1,358,357,325,-1,325,326,358,-1,359,358,326,-1,326,327,359,-1,360,359,327,-1,327,328,360,-1,361,360,328,-1,328,329,361,-1,362,361,329,-1,329,330,362,-1,363,362,330,-1,330,331,363,-1,364,363,331,-1,333,332,365,-1,366,365,332,-1,332,334,366,-1,367,366,334,-1,334,335,367,-1,368,367,335,-1,335,336,368,-1,369,368,336,-1,336,337,369,-1,370,369,337,-1,337,338,370,-1,371,370,338,-1,338,339,371,-1,372,371,339,-1,339,340,372,-1,373,372,340,-1,340,341,373,-1,374,373,341,-1,341,342,374,-1,375,374,342,-1,342,343,375,-1,376,375,343,-1,343,344,376,-1,377,376,344,-1,344,345,377,-1,378,377,345,-1,345,346,378,-1,379,378,346,-1,346,347,379,-1,380,379,347,-1,347,348,380,-1,381,380,348,-1,348,349,381,-1,382,381,349,-1,349,350,382,-1,383,382,350,-1,350,351,383,-1,384,383,351,-1,351,352,384,-1,385,384,352,-1,352,353,385,-1,386,385,353,-1,353,354,386,-1,387,386,354,-1,354,355,387,-1,388,387,355,-1,355,356,388,-1,389,388,356,-1,356,357,389,-1,390,389,357,-1,357,358,390,-1,391,390,358,-1,358,359,391,-1,392,391,359,-1,359,360,392,-1,393,392,360,-1,360,361,393,-1,394,393,361,-1,361,362,394,-1,395,394,362,-1,362,363,395,-1,396,395,363,-1,363,364,396,-1,397,398,365,-1,365,366,397,-1,399,397,366,-1,366,367,399,-1,400,399,367,-1,367,368,400,-1,401,400,368,-1,368,369,401,-1,402,401,369,-1,369,370,402,-1,403,402,370,-1,370,371,403,-1,404,403,371,-1,371,372,404,-1,405,404,372,-1,372,373,405,-1,406,405,373,-1,373,374,406,-1,407,406,374,-1,374,375,407,-1,408,407,375,-1,375,376,408,-1,409,408,376,-1,376,377,409,-1,410,409,377,-1,377,378,410,-1,411,410,378,-1,378,379,411,-1,412,411,379,-1,379,380,412,-1,413,412,380,-1,380,381,413,-1,414,413,381,-1,381,382,414,-1,415,414,382,-1,382,383,415,-1,416,415,383,-1,383,384,416,-1,417,416,384,-1,384,385,417,-1,418,417,385,-1,385,386,418,-1,419,418,386,-1,386,387,419,-1,420,419,387,-1,387,388,420,-1,421,420,388,-1,388,389,421,-1,422,421,389,-1,389,390,422,-1,423,422,390,-1,390,391,423,-1,424,423,391,-1,391,392,424,-1,425,424,392,-1,392,393,425,-1,426,425,393,-1,393,394,426,-1,427,426,394,-1,394,395,427,-1,428,427,395,-1,395,396,428,-1,429,430,398,-1,398,397,429,-1,431,429,397,-1,397,399,431,-1,432,431,399,-1,399,400,432,-1,433,432,400,-1,400,401,433,-1,434,433,401,-1,401,402,434,-1,435,434,402,-1,402,403,435,-1,436,435,403,-1,403,404,436,-1,437,436,404,-1,404,405,437,-1,438,437,405,-1,405,406,438,-1,439,438,406,-1,406,407,439,-1,440,439,407,-1,407,408,440,-1,441,440,408,-1,408,409,441,-1,442,441,409,-1,409,410,442,-1,443,442,410,-1,410,411,443,-1,444,443,411,-1,411,412,444,-1,445,444,412,-1,412,413,445,-1,446,445,413,-1,413,414,446,-1,447,446,414,-1,414,415,447,-1,448,447,415,-1,415,416,448,-1,449,448,416,-1,416,417,449,-1,450,449,417,-1,417,418,450,-1,451,450,418,-1,418,419,451,-1,452,451,419,-1,419,420,452,-1,453,452,420,-1,420,421,453,-1,454,453,421,-1,421,422,454,-1,455,454,422,-1,422,423,455,-1,456,455,423,-1,423,424,456,-1,457,456,424,-1,424,425,457,-1,458,457,425,-1,425,426,458,-1,459,458,426,-1,426,427,459,-1,460,459,427,-1,427,428,460,-1,430,429,461,-1,462,461,429,-1,429,431,462,-1,463,462,431,-1,431,432,463,-1,464,463,432,-1,432,433,464,-1,465,464,433,-1,433,434,465,-1,466,465,434,-1,434,435,466,-1,467,466,435,-1,435,436,467,-1,468,467,436,-1,436,437,468,-1,469,468,437,-1,437,438,469,-1,470,469,438,-1,438,439,470,-1,471,470,439,-1,439,440,471,-1,472,471,440,-1,440,441,472,-1,473,472,441,-1,441,442,473,-1,474,473,442,-1,442,443,474,-1,475,474,443,-1,443,444,475,-1,476,475,444,-1,444,445,476,-1,477,476,445,-1,445,446,477,-1,478,477,446,-1,446,447,478,-1,479,478,447,-1,447,448,479,-1,480,479,448,-1,448,449,480,-1,481,480,449,-1,449,450,481,-1,482,481,450,-1,450,451,482,-1,483,482,451,-1,451,452,483,-1,484,483,452,-1,452,453,484,-1,485,484,453,-1,453,454,485,-1,486,485,454,-1,454,455,486,-1,487,486,455,-1,455,456,487,-1,488,487,456,-1,456,457,488,-1,489,488,457,-1,457,458,489,-1,490,489,458,-1,458,459,490,-1,491,490,459,-1,459,460,491,-1,492,493,461,-1,461,462,492,-1,494,492,462,-1,462,463,494,-1,495,494,463,-1,463,464,495,-1,496,495,464,-1,464,465,496,-1,497,496,465,-1,465,466,497,-1,498,497,466,-1,466,467,498,-1,499,498,467,-1,467,468,499,-1,500,499,468,-1,468,469,500,-1,501,500,469,-1,469,470,501,-1,502,501,470,-1,470,471,502,-1,503,502,471,-1,471,472,503,-1,504,503,472,-1,472,473,504,-1,505,504,473,-1,473,474,505,-1,506,505,474,-1,474,475,506,-1,507,506,475,-1,475,476,507,-1,508,507,476,-1,476,477,508,-1,509,508,477,-1,477,478,509,-1,510,509,478,-1,478,479,510,-1,511,510,479,-1,479,480,511,-1,512,511,480,-1,480,481,512,-1,513,512,481,-1,481,482,513,-1,514,513,482,-1,482,483,514,-1,515,514,483,-1,483,484,515,-1,516,515,484,-1,484,485,516,-1,517,516,485,-1,485,486,517,-1,518,517,486,-1,486,487,518,-1,519,518,487,-1,487,488,519,-1,520,519,488,-1,488,489,520,-1,521,520,489,-1,489,490,521,-1,493,492,522,-1,523,522,492,-1,492,494,523,-1,524,523,494,-1,494,495,524,-1,525,524,495,-1,495,496,525,-1,526,525,496,-1,496,497,526,-1,527,526,497,-1,497,498,527,-1,528,527,498,-1,498,499,528,-1,529,528,499,-1,499,500,529,-1,530,529,500,-1,500,501,530,-1,531,530,501,-1,501,502,531,-1,532,531,502,-1,502,503,532,-1,533,532,503,-1,503,504,533,-1,534,533,504,-1,504,505,534,-1,535,534,505,-1,505,506,535,-1,536,535,506,-1,506,507,536,-1,537,536,507,-1,507,508,537,-1,538,537,508,-1,508,509,538,-1,539,538,509,-1,509,510,539,-1,540,539,510,-1,510,511,540,-1,541,540,511,-1,511,512,541,-1,542,541,512,-1,512,513,542,-1,543,542,513,-1,513,514,543,-1,544,543,514,-1,514,515,544,-1,545,544,515,-1,515,516,545,-1,546,545,516,-1,516,517,546,-1,547,546,517,-1,517,518,547,-1,548,547,518,-1,518,519,548,-1,549,548,519,-1,519,520,549,-1,550,549,520,-1,520,521,550,-1,551,550,521,-1,523,524,552,-1,553,552,524,-1,524,525,553,-1,554,553,525,-1,525,526,554,-1,555,554,526,-1,526,527,555,-1,556,555,527,-1,527,528,556,-1,557,556,528,-1,528,529,557,-1,558,557,529,-1,529,530,558,-1,559,558,530,-1,530,531,559,-1,560,559,531,-1,531,532,560,-1,561,560,532,-1,532,533,561,-1,562,561,533,-1,533,534,562,-1,563,562,534,-1,534,535,563,-1,564,563,535,-1,535,536,564,-1,565,564,536,-1,536,537,565,-1,566,565,537,-1,537,538,566,-1,567,566,538,-1,538,539,567,-1,568,567,539,-1,539,540,568,-1,569,568,540,-1,540,541,569,-1,570,569,541,-1,541,542,570,-1,571,570,542,-1,542,543,571,-1,572,571,543,-1,543,544,572,-1,573,572,544,-1,544,545,573,-1,574,573,545,-1,545,546,574,-1,575,574,546,-1,546,547,575,-1,576,575,547,-1,547,548,576,-1,577,576,548,-1,548,549,577,-1,578,577,549,-1,549,550,578,-1,579,578,550,-1,550,551,579,-1,580,581,552,-1,552,553,580,-1,582,580,553,-1,553,554,582,-1,583,582,554,-1,554,555,583,-1,584,583,555,-1,555,556,584,-1,585,584,556,-1,556,557,585,-1,586,585,557,-1,557,558,586,-1,587,586,558,-1,558,559,587,-1,588,587,559,-1,559,560,588,-1,589,588,560,-1,560,561,589,-1,590,589,561,-1,561,562,590,-1,591,590,562,-1,562,563,591,-1,592,591,563,-1,563,564,592,-1,593,592,564,-1,564,565,593,-1,594,593,565,-1,565,566,594,-1,595,594,566,-1,566,567,595,-1,596,595,567,-1,567,568,596,-1,597,596,568,-1,568,569,597,-1,598,597,569,-1,569,570,598,-1,599,598,570,-1,570,571,599,-1,600,599,571,-1,571,572,600,-1,601,600,572,-1,572,573,601,-1,602,601,573,-1,573,574,602,-1,603,602,574,-1,574,575,603,-1,604,603,575,-1,575,576,604,-1,605,604,576,-1,576,577,605,-1,606,605,577,-1,577,578,606,-1,607,608,581,-1,581,580,607,-1,609,607,580,-1,580,582,609,-1,610,609,582,-1,582,583,610,-1,611,610,583,-1,583,584,611,-1,612,611,584,-1,584,585,612,-1,613,612,585,-1,585,586,613,-1,614,613,586,-1,586,587,614,-1,615,614,587,-1,587,588,615,-1,616,615,588,-1,588,589,616,-1,617,616,589,-1,589,590,617,-1,618,617,590,-1,590,591,618,-1,619,618,591,-1,591,592,619,-1,620,619,592,-1,592,593,620,-1,621,620,593,-1,593,594,621,-1,622,621,594,-1,594,595,622,-1,623,622,595,-1,595,596,623,-1,624,623,596,-1,596,597,624,-1,625,624,597,-1,597,598,625,-1,626,625,598,-1,598,599,626,-1,627,626,599,-1,599,600,627,-1,628,627,600,-1,600,601,628,-1,629,628,601,-1,601,602,629,-1,630,629,602,-1,602,603,630,-1,631,630,603,-1,603,604,631,-1,632,631,604,-1,604,605,632,-1,633,632,605,-1,605,606,633,-1,634,635,608,-1,608,607,634,-1,636,634,607,-1,607,609,636,-1,637,636,609,-1,609,610,637,-1,638,637,610,-1,610,611,638,-1,639,638,611,-1,611,612,639,-1,640,639,612,-1,612,613,640,-1,641,640,613,-1,613,614,641,-1,642,641,614,-1,614,615,642,-1,643,642,615,-1,615,616,643,-1,644,643,616,-1,616,617,644,-1,645,644,617,-1,617,618,645,-1,646,645,618,-1,618,619,646,-1,647,646,619,-1,619,620,647,-1,648,647,620,-1,620,621,648,-1,649,648,621,-1,621,622,649,-1,650,649,622,-1,622,623,650,-1,651,650,623,-1,623,624,651,-1,652,651,624,-1,624,625,652,-1,653,652,625,-1,625,626,653,-1,654,653,626,-1,626,627,654,-1,655,654,627,-1,627,628,655,-1,656,655,628,-1,628,629,656,-1,657,656,629,-1,629,630,657,-1,658,657,630,-1,630,631,658,-1,659,658,631,-1,631,632,659,-1,660,659,632,-1,632,633,660,-1,661,660,633,-1,662,663,664,-1,664,665,662,-1,666,662,665,-1,665,635,666,-1,667,666,635,-1,635,634,667,-1,668,667,634,-1,634,636,668,-1,669,668,636,-1,636,637,669,-1,670,669,637,-1,637,638,670,-1,671,670,638,-1,638,639,671,-1,672,671,639,-1,639,640,672,-1,673,672,640,-1,640,641,673,-1,674,673,641,-1,641,642,674,-1,675,674,642,-1,642,643,675,-1,676,675,643,-1,643,644,676,-1,677,676,644,-1,644,645,677,-1,678,677,645,-1,645,646,678,-1,679,678,646,-1,646,647,679,-1,680,679,647,-1,647,648,680,-1,681,680,648,-1,648,649,681,-1,682,681,649,-1,649,650,682,-1,683,682,650,-1,650,651,683,-1,684,683,651,-1,651,652,684,-1,685,684,652,-1,652,653,685,-1,686,685,653,-1,653,654,686,-1,687,686,654,-1,654,655,687,-1,688,687,655,-1,655,656,688,-1,689,688,656,-1,656,657,689,-1,690,689,657,-1,657,658,690,-1,691,690,658,-1,658,659,691,-1,692,691,659,-1,659,660,692,-1,693,692,660,-1,660,661,693,-1,694,693,661,-1,695,696,663,-1,663,662,695,-1,697,695,662,-1,662,666,697,-1,698,697,666,-1,666,667,698,-1,699,698,667,-1,667,668,699,-1,700,699,668,-1,668,669,700,-1,701,700,669,-1,669,670,701,-1,702,701,670,-1,670,671,702,-1,703,702,671,-1,671,672,703,-1,704,703,672,-1,672,673,704,-1,705,704,673,-1,673,674,705,-1,706,705,674,-1,674,675,706,-1,707,706,675,-1,675,676,707,-1,708,707,676,-1,676,677,708,-1,709,708,677,-1,677,678,709,-1,710,709,678,-1,678,679,710,-1,711,710,679,-1,679,680,711,-1,712,711,680,-1,680,681,712,-1,713,712,681,-1,681,682,713,-1,714,713,682,-1,682,683,714,-1,715,714,683,-1,683,684,715,-1,716,715,684,-1,684,685,716,-1,717,716,685,-1,685,686,717,-1,718,717,686,-1,686,687,718,-1,719,718,687,-1,687,688,719,-1,720,719,688,-1,688,689,720,-1,721,720,689,-1,689,690,721,-1,722,721,690,-1,690,691,722,-1,723,722,691,-1,691,692,723,-1,724,723,692,-1,692,693,724,-1,725,724,693,-1,693,694,725,-1,726,725,694,-1,727,728,696,-1,696,695,727,-1,729,727,695,-1,695,697,729,-1,730,729,697,-1,697,698,730,-1,731,730,698,-1,698,699,731,-1,732,731,699,-1,699,700,732,-1,733,732,700,-1,700,701,733,-1,734,733,701,-1,701,702,734,-1,735,734,702,-1,702,703,735,-1,736,735,703,-1,703,704,736,-1,737,736,704,-1,704,705,737,-1,738,737,705,-1,705,706,738,-1,739,738,706,-1,706,707,739,-1,740,739,707,-1,707,708,740,-1,741,740,708,-1,708,709,741,-1,742,741,709,-1,709,710,742,-1,743,742,710,-1,710,711,743,-1,744,743,711,-1,711,712,744,-1,745,744,712,-1,712,713,745,-1,746,745,713,-1,713,714,746,-1,747,746,714,-1,714,715,747,-1,748,747,715,-1,715,716,748,-1,749,748,716,-1,716,717,749,-1,750,749,717,-1,717,718,750,-1,751,750,718,-1,718,719,751,-1,752,751,719,-1,719,720,752,-1,753,752,720,-1,720,721,753,-1,754,753,721,-1,721,722,754,-1,755,754,722,-1,722,723,755,-1,756,755,723,-1,723,724,756,-1,757,756,724,-1,724,725,757,-1,758,757,725,-1,725,726,758,-1,759,758,726,-1,728,727,760,-1,761,760,727,-1,727,729,761,-1,762,761,729,-1,729,730,762,-1,763,762,730,-1,730,731,763,-1,764,763,731,-1,731,732,764,-1,765,764,732,-1,732,733,765,-1,766,765,733,-1,733,734,766,-1,767,766,734,-1,734,735,767,-1,768,767,735,-1,735,736,768,-1,769,768,736,-1,736,737,769,-1,770,769,737,-1,737,738,770,-1,771,770,738,-1,738,739,771,-1,772,771,739,-1,739,740,772,-1,773,772,740,-1,740,741,773,-1,774,773,741,-1,741,742,774,-1,775,774,742,-1,742,743,775,-1,776,775,743,-1,743,744,776,-1,777,776,744,-1,744,745,777,-1,778,777,745,-1,745,746,778,-1,779,778,746,-1,746,747,779,-1,780,779,747,-1,747,748,780,-1,781,780,748,-1,748,749,781,-1,782,781,749,-1,749,750,782,-1,783,782,750,-1,750,751,783,-1,784,783,751,-1,751,752,784,-1,785,784,752,-1,752,753,785,-1,786,785,753,-1,753,754,786,-1,787,786,754,-1,754,755,787,-1,788,787,755,-1,755,756,788,-1,789,788,756,-1,756,757,789,-1,790,789,757,-1,757,758,790,-1,791,790,758,-1,758,759,791,-1,792,791,759,-1,793,794,760,-1,760,761,793,-1,795,793,761,-1,761,762,795,-1,796,795,762,-1,762,763,796,-1,797,796,763,-1,763,764,797,-1,798,797,764,-1,764,765,798,-1,799,798,765,-1,765,766,799,-1,800,799,766,-1,766,767,800,-1,801,800,767,-1,767,768,801,-1,802,801,768,-1,768,769,802,-1,803,802,769,-1,769,770,803,-1,804,803,770,-1,770,771,804,-1,805,804,771,-1,771,772,805,-1,806,805,772,-1,772,773,806,-1,807,806,773,-1,773,774,807,-1,808,807,774,-1,774,775,808,-1,809,808,775,-1,775,776,809,-1,810,809,776,-1,776,777,810,-1,811,810,777,-1,777,778,811,-1,812,811,778,-1,778,779,812,-1,813,812,779,-1,779,780,813,-1,814,813,780,-1,780,781,814,-1,815,814,781,-1,781,782,815,-1,816,815,782,-1,782,783,816,-1,817,816,783,-1,783,784,817,-1,818,817,784,-1,784,785,818,-1,819,818,785,-1,785,786,819,-1,820,819,786,-1,786,787,820,-1,821,820,787,-1,787,788,821,-1,822,821,788,-1,788,789,822,-1,823,822,789,-1,789,790,823,-1,824,823,790,-1,790,791,824,-1,825,824,791,-1,791,792,825,-1,826,825,792,-1,827,828,829,-1,829,794,827,-1,830,827,794,-1,794,793,830,-1,831,830,793,-1,793,795,831,-1,832,831,795,-1,795,796,832,-1,833,832,796,-1,796,797,833,-1,834,833,797,-1,797,798,834,-1,835,834,798,-1,798,799,835,-1,836,835,799,-1,799,800,836,-1,837,836,800,-1,800,801,837,-1,838,837,801,-1,801,802,838,-1,839,838,802,-1,802,803,839,-1,840,839,803,-1,803,804,840,-1,841,840,804,-1,804,805,841,-1,842,841,805,-1,805,806,842,-1,843,842,806,-1,806,807,843,-1,844,843,807,-1,807,808,844,-1,845,844,808,-1,808,809,845,-1,846,845,809,-1,809,810,846,-1,847,846,810,-1,810,811,847,-1,848,847,811,-1,811,812,848,-1,849,848,812,-1,812,813,849,-1,850,849,813,-1,813,814,850,-1,851,850,814,-1,814,815,851,-1,852,851,815,-1,815,816,852,-1,853,852,816,-1,816,817,853,-1,854,853,817,-1,817,818,854,-1,855,854,818,-1,818,819,855,-1,856,855,819,-1,819,820,856,-1,857,856,820,-1,820,821,857,-1,858,857,821,-1,821,822,858,-1,859,858,822,-1,822,823,859,-1,860,859,823,-1,823,824,860,-1,861,860,824,-1,824,825,861,-1,862,861,825,-1,825,826,862,-1,863,862,826,-1,864,865,828,-1,828,827,864,-1,866,864,827,-1,827,830,866,-1,867,866,830,-1,830,831,867,-1,868,867,831,-1,831,832,868,-1,869,868,832,-1,832,833,869,-1,870,869,833,-1,833,834,870,-1,871,870,834,-1,834,835,871,-1,872,871,835,-1,835,836,872,-1,873,872,836,-1,836,837,873,-1,874,873,837,-1,837,838,874,-1,875,874,838,-1,838,839,875,-1,876,875,839,-1,839,840,876,-1,877,876,840,-1,840,841,877,-1,878,877,841,-1,841,842,878,-1,879,878,842,-1,842,843,879,-1,880,879,843,-1,843,844,880,-1,881,880,844,-1,844,845,881,-1,882,881,845,-1,845,846,882,-1,883,882,846,-1,846,847,883,-1,884,883,847,-1,847,848,884,-1,885,884,848,-1,848,849,885,-1,886,885,849,-1,849,850,886,-1,887,886,850,-1,850,851,887,-1,888,887,851,-1,851,852,888,-1,889,888,852,-1,852,853,889,-1,890,889,853,-1,853,854,890,-1,891,890,854,-1,854,855,891,-1,892,891,855,-1,855,856,892,-1,893,892,856,-1,856,857,893,-1,894,893,857,-1,857,858,894,-1,895,894,858,-1,858,859,895,-1,896,895,859,-1,859,860,896,-1,897,896,860,-1,860,861,897,-1,898,897,861,-1,861,862,898,-1,899,898,862,-1,862,863,899,-1,900,899,863,-1,901,902,865,-1,865,864,901,-1,903,901,864,-1,864,866,903,-1,904,903,866,-1,866,867,904,-1,905,904,867,-1,867,868,905,-1,906,905,868,-1,868,869,906,-1,907,906,869,-1,869,870,907,-1,908,907,870,-1,870,871,908,-1,909,908,871,-1,871,872,909,-1,910,909,872,-1,872,873,910,-1,911,910,873,-1,873,874,911,-1,912,911,874,-1,874,875,912,-1,913,912,875,-1,875,876,913,-1,914,913,876,-1,876,877,914,-1,915,914,877,-1,877,878,915,-1,916,915,878,-1,878,879,916,-1,917,916,879,-1,879,880,917,-1,918,917,880,-1,880,881,918,-1,919,918,881,-1,881,882,919,-1,920,919,882,-1,882,883,920,-1,921,920,883,-1,883,884,921,-1,922,921,884,-1,884,885,922,-1,923,922,885,-1,885,886,923,-1,924,923,886,-1,886,887,924,-1,925,924,887,-1,887,888,925,-1,926,925,888,-1,888,889,926,-1,927,926,889,-1,889,890,927,-1,928,927,890,-1,890,891,928,-1,929,928,891,-1,891,892,929,-1,930,929,892,-1,892,893,930,-1,931,930,893,-1,893,894,931,-1,932,931,894,-1,894,895,932,-1,933,932,895,-1,895,896,933,-1,934,933,896,-1,896,897,934,-1,935,934,897,-1,897,898,935,-1,936,935,898,-1,898,899,936,-1,937,936,899,-1,899,900,937,-1,938,937,900,-1,939,940,941,-1,941,902,939,-1,942,939,902,-1,902,901,942,-1,943,942,901,-1,901,903,943,-1,944,943,903,-1,903,904,944,-1,945,944,904,-1,904,905,945,-1,946,945,905,-1,905,906,946,-1,947,946,906,-1,906,907,947,-1,948,947,907,-1,907,908,948,-1,949,948,908,-1,908,909,949,-1,950,949,909,-1,909,910,950,-1,951,950,910,-1,910,911,951,-1,952,951,911,-1,911,912,952,-1,953,952,912,-1,912,913,953,-1,954,953,913,-1,913,914,954,-1,955,954,914,-1,914,915,955,-1,956,955,915,-1,915,916,956,-1,957,956,916,-1,916,917,957,-1,958,957,917,-1,917,918,958,-1,959,958,918,-1,918,919,959,-1,960,959,919,-1,919,920,960,-1,961,960,920,-1,920,921,961,-1,962,961,921,-1,921,922,962,-1,963,962,922,-1,922,923,963,-1,964,963,923,-1,923,924,964,-1,965,964,924,-1,924,925,965,-1,966,965,925,-1,925,926,966,-1,967,966,926,-1,926,927,967,-1,968,967,927,-1,927,928,968,-1,969,968,928,-1,928,929,969,-1,970,969,929,-1,929,930,970,-1,971,970,930,-1,930,931,971,-1,972,971,931,-1,931,932,972,-1,973,972,932,-1,932,933,973,-1,974,973,933,-1,933,934,974,-1,975,974,934,-1,934,935,975,-1,976,975,935,-1,935,936,976,-1,977,976,936,-1,936,937,977,-1,978,977,937,-1,937,938,978,-1,940,939,979,-1,980,979,939,-1,939,942,980,-1,981,980,942,-1,942,943,981,-1,982,981,943,-1,943,944,982,-1,983,982,944,-1,944,945,983,-1,984,983,945,-1,945,946,984,-1,985,984,946,-1,946,947,985,-1,986,985,947,-1,947,948,986,-1,987,986,948,-1,948,949,987,-1,988,987,949,-1,949,950,988,-1,989,988,950,-1,950,951,989,-1,990,989,951,-1,951,952,990,-1,991,990,952,-1,952,953,991,-1,992,991,953,-1,953,954,992,-1,993,992,954,-1,954,955,993,-1,994,993,955,-1,955,956,994,-1,995,994,956,-1,956,957,995,-1,996,995,957,-1,957,958,996,-1,997,996,958,-1,958,959,997,-1,998,997,959,-1,959,960,998,-1,999,998,960,-1,960,961,999,-1,1000,999,961,-1,961,962,1000,-1,1001,1000,962,-1,962,963,1001,-1,1002,1001,963,-1,963,964,1002,-1,1003,1002,964,-1,964,965,1003,-1,1004,1003,965,-1,965,966,1004,-1,1005,1004,966,-1,966,967,1005,-1,1006,1005,967,-1,967,968,1006,-1,1007,1006,968,-1,968,969,1007,-1,1008,1007,969,-1,969,970,1008,-1,1009,1008,970,-1,970,971,1009,-1,1010,1009,971,-1,971,972,1010,-1,1011,1010,972,-1,972,973,1011,-1,1012,1011,973,-1,973,974,1012,-1,1013,1012,974,-1,974,975,1013,-1,1014,1013,975,-1,975,976,1014,-1,1015,1014,976,-1,976,977,1015,-1,1016,1015,977,-1,977,978,1016,-1,1017,1016,978,-1,1018,1019,979,-1,979,980,1018,-1,1020,1018,980,-1,980,981,1020,-1,1021,1020,981,-1,981,982,1021,-1,1022,1021,982,-1,982,983,1022,-1,1023,1022,983,-1,983,984,1023,-1,1024,1023,984,-1,984,985,1024,-1,1025,1024,985,-1,985,986,1025,-1,1026,1025,986,-1,986,987,1026,-1,1027,1026,987,-1,987,988,1027,-1,1028,1027,988,-1,988,989,1028,-1,1029,1028,989,-1,989,990,1029,-1,1030,1029,990,-1,990,991,1030,-1,1031,1030,991,-1,991,992,1031,-1,1032,1031,992,-1,992,993,1032,-1,1033,1032,993,-1,993,994,1033,-1,1034,1033,994,-1,994,995,1034,-1,1035,1034,995,-1,995,996,1035,-1,1036,1035,996,-1,996,997,1036,-1,1037,1036,997,-1,997,998,1037,-1,1038,1037,998,-1,998,999,1038,-1,1039,1038,999,-1,999,1000,1039,-1,1040,1039,1000,-1,1000,1001,1040,-1,1041,1040,1001,-1,1001,1002,1041,-1,1042,1041,1002,-1,1002,1003,1042,-1,1043,1042,1003,-1,1003,1004,1043,-1,1044,1043,1004,-1,1004,1005,1044,-1,1045,1044,1005,-1,1005,1006,1045,-1,1046,1045,1006,-1,1006,1007,1046,-1,1047,1046,1007,-1,1007,1008,1047,-1,1048,1047,1008,-1,1008,1009,1048,-1,1049,1048,1009,-1,1009,1010,1049,-1,1050,1049,1010,-1,1010,1011,1050,-1,1051,1050,1011,-1,1011,1012,1051,-1,1052,1051,1012,-1,1012,1013,1052,-1,1053,1052,1013,-1,1013,1014,1053,-1,1054,1053,1014,-1,1014,1015,1054,-1,1055,1054,1015,-1,1015,1016,1055,-1,1056,1055,1016,-1,1016,1017,1056,-1,1057,1056,1017,-1,1058,1059,1019,-1,1019,1018,1058,-1,1060,1058,1018,-1,1018,1020,1060,-1,1061,1060,1020,-1,1020,1021,1061,-1,1062,1061,1021,-1,1021,1022,1062,-1,1063,1062,1022,-1,1022,1023,1063,-1,1064,1063,1023,-1,1023,1024,1064,-1,1065,1064,1024,-1,1024,1025,1065,-1,1066,1065,1025,-1,1025,1026,1066,-1,1067,1066,1026,-1,1026,1027,1067,-1,1068,1067,1027,-1,1027,1028,1068,-1,1069,1068,1028,-1,1028,1029,1069,-1,1070,1069,1029,-1,1029,1030,1070,-1,1071,1070,1030,-1,1030,1031,1071,-1,1072,1071,1031,-1,1031,1032,1072,-1,1073,1072,1032,-1,1032,1033,1073,-1,1074,1073,1033,-1,1033,1034,1074,-1,1075,1074,1034,-1,1034,1035,1075,-1,1076,1075,1035,-1,1035,1036,1076,-1,1077,1076,1036,-1,1036,1037,1077,-1,1078,1077,1037,-1,1037,1038,1078,-1,1079,1078,1038,-1,1038,1039,1079,-1,1080,1079,1039,-1,1039,1040,1080,-1,1081,1080,1040,-1,1040,1041,1081,-1,1082,1081,1041,-1,1041,1042,1082,-1,1083,1082,1042,-1,1042,1043,1083,-1,1084,1083,1043,-1,1043,1044,1084,-1,1085,1084,1044,-1,1044,1045,1085,-1,1086,1085,1045,-1,1045,1046,1086,-1,1087,1086,1046,-1,1046,1047,1087,-1,1088,1087,1047,-1,1047,1048,1088,-1,1089,1088,1048,-1,1048,1049,1089,-1,1090,1089,1049,-1,1049,1050,1090,-1,1091,1090,1050,-1,1050,1051,1091,-1,1092,1091,1051,-1,1051,1052,1092,-1,1093,1092,1052,-1,1052,1053,1093,-1,1094,1093,1053,-1,1053,1054,1094,-1,1095,1094,1054,-1,1054,1055,1095,-1,1096,1095,1055,-1,1055,1056,1096,-1,1097,1096,1056,-1,1056,1057,1097,-1,1098,1097,1057,-1,1059,1058,1099,-1,1100,1099,1058,-1,1058,1060,1100,-1,1101,1100,1060,-1,1060,1061,1101,-1,1102,1101,1061,-1,1061,1062,1102,-1,1103,1102,1062,-1,1062,1063,1103,-1,1104,1103,1063,-1,1063,1064,1104,-1,1105,1104,1064,-1,1064,1065,1105,-1,1106,1105,1065,-1,1065,1066,1106,-1,1107,1106,1066,-1,1066,1067,1107,-1,1108,1107,1067,-1,1067,1068,1108,-1,1109,1108,1068,-1,1068,1069,1109,-1,1110,1109,1069,-1,1069,1070,1110,-1,1111,1110,1070,-1,1070,1071,1111,-1,1112,1111,1071,-1,1071,1072,1112,-1,1113,1112,1072,-1,1072,1073,1113,-1,1114,1113,1073,-1,1073,1074,1114,-1,1115,1114,1074,-1,1074,1075,1115,-1,1116,1115,1075,-1,1075,1076,1116,-1,1117,1116,1076,-1,1076,1077,1117,-1,1118,1117,1077,-1,1077,1078,1118,-1,1119,1118,1078,-1,1078,1079,1119,-1,1120,1119,1079,-1,1079,1080,1120,-1,1121,1120,1080,-1,1080,1081,1121,-1,1122,1121,1081,-1,1081,1082,1122,-1,1123,1122,1082,-1,1082,1083,1123,-1,1124,1123,1083,-1,1083,1084,1124,-1,1125,1124,1084,-1,1084,1085,1125,-1,1126,1125,1085,-1,1085,1086,1126,-1,1127,1126,1086,-1,1086,1087,1127,-1,1128,1127,1087,-1,1087,1088,1128,-1,1129,1128,1088,-1,1088,1089,1129,-1,1130,1129,1089,-1,1089,1090,1130,-1,1131,1130,1090,-1,1090,1091,1131,-1,1132,1131,1091,-1,1091,1092,1132,-1,1133,1132,1092,-1,1092,1093,1133,-1,1134,1133,1093,-1,1093,1094,1134,-1,1135,1134,1094,-1,1094,1095,1135,-1,1136,1135,1095,-1,1095,1096,1136,-1,1137,1136,1096,-1,1096,1097,1137,-1,1138,1137,1097,-1,1097,1098,1138,-1,1139,1138,1098,-1,1140,1141,1099,-1,1099,1100,1140,-1,1142,1140,1100,-1,1100,1101,1142,-1,1143,1142,1101,-1,1101,1102,1143,-1,1144,1143,1102,-1,1102,1103,1144,-1,1145,1144,1103,-1,1103,1104,1145,-1,1146,1145,1104,-1,1104,1105,1146,-1,1147,1146,1105,-1,1105,1106,1147,-1,1148,1147,1106,-1,1106,1107,1148,-1,1149,1148,1107,-1,1107,1108,1149,-1,1150,1149,1108,-1,1108,1109,1150,-1,1151,1150,1109,-1,1109,1110,1151,-1,1152,1151,1110,-1,1110,1111,1152,-1,1153,1152,1111,-1,1111,1112,1153,-1,1154,1153,1112,-1,1112,1113,1154,-1,1155,1154,1113,-1,1113,1114,1155,-1,1156,1155,1114,-1,1114,1115,1156,-1,1157,1156,1115,-1,1115,1116,1157,-1,1158,1157,1116,-1,1116,1117,1158,-1,1159,1158,1117,-1,1117,1118,1159,-1,1160,1159,1118,-1,1118,1119,1160,-1,1161,1160,1119,-1,1119,1120,1161,-1,1162,1161,1120,-1,1120,1121,1162,-1,1163,1162,1121,-1,1121,1122,1163,-1,1164,1163,1122,-1,1122,1123,1164,-1,1165,1164,1123,-1,1123,1124,1165,-1,1166,1165,1124,-1,1124,1125,1166,-1,1167,1166,1125,-1,1125,1126,1167,-1,1168,1167,1126,-1,1126,1127,1168,-1,1169,1168,1127,-1,1127,1128,1169,-1,1170,1169,1128,-1,1128,1129,1170,-1,1171,1170,1129,-1,1129,1130,1171,-1,1172,1171,1130,-1,1130,1131,1172,-1,1173,1172,1131,-1,1131,1132,1173,-1,1174,1173,1132,-1,1132,1133,1174,-1,1175,1174,1133,-1,1133,1134,1175,-1,1176,1175,1134,-1,1134,1135,1176,-1,1177,1176,1135,-1,1135,1136,1177,-1,1178,1177,1136,-1,1136,1137,1178,-1,1179,1178,1137,-1,1137,1138,1179,-1,1180,1179,1138,-1,1138,1139,1180,-1,1141,1140,1181,-1,1182,1181,1140,-1,1140,1142,1182,-1,1183,1182,1142,-1,1142,1143,1183,-1,1184,1183,1143,-1,1143,1144,1184,-1,1185,1184,1144,-1,1144,1145,1185,-1,1186,1185,1145,-1,1145,1146,1186,-1,1187,1186,1146,-1,1146,1147,1187,-1,1188,1187,1147,-1,1147,1148,1188,-1,1189,1188,1148,-1,1148,1149,1189,-1,1190,1189,1149,-1,1149,1150,1190,-1,1191,1190,1150,-1,1150,1151,1191,-1,1192,1191,1151,-1,1151,1152,1192,-1,1193,1192,1152,-1,1152,1153,1193,-1,1194,1193,1153,-1,1153,1154,1194,-1,1195,1194,1154,-1,1154,1155,1195,-1,1196,1195,1155,-1,1155,1156,1196,-1,1197,1196,1156,-1,1156,1157,1197,-1,1198,1197,1157,-1,1157,1158,1198,-1,1199,1198,1158,-1,1158,1159,1199,-1,1200,1199,1159,-1,1159,1160,1200,-1,1201,1200,1160,-1,1160,1161,1201,-1,1202,1201,1161,-1,1161,1162,1202,-1,1203,1202,1162,-1,1162,1163,1203,-1,1204,1203,1163,-1,1163,1164,1204,-1,1205,1204,1164,-1,1164,1165,1205,-1,1206,1205,1165,-1,1165,1166,1206,-1,1207,1206,1166,-1,1166,1167,1207,-1,1208,1207,1167,-1,1167,1168,1208,-1,1209,1208,1168,-1,1168,1169,1209,-1,1210,1209,1169,-1,1169,1170,1210,-1,1211,1210,1170,-1,1170,1171,1211,-1,1212,1211,1171,-1,1171,1172,1212,-1,1213,1212,1172,-1,1172,1173,1213,-1,1214,1213,1173,-1,1173,1174,1214,-1,1215,1214,1174,-1,1174,1175,1215,-1,1216,1215,1175,-1,1175,1176,1216,-1,1217,1216,1176,-1,1176,1177,1217,-1,1218,1217,1177,-1,1177,1178,1218,-1,1219,1218,1178,-1,1178,1179,1219,-1,1220,1221,1181,-1,1181,1182,1220,-1,1222,1220,1182,-1,1182,1183,1222,-1,1223,1222,1183,-1,1183,1184,1223,-1,1224,1223,1184,-1,1184,1185,1224,-1,1225,1224,1185,-1,1185,1186,1225,-1,1226,1225,1186,-1,1186,1187,1226,-1,1227,1226,1187,-1,1187,1188,1227,-1,1228,1227,1188,-1,1188,1189,1228,-1,1229,1228,1189,-1,1189,1190,1229,-1,1230,1229,1190,-1,1190,1191,1230,-1,1231,1230,1191,-1,1191,1192,1231,-1,1232,1231,1192,-1,1192,1193,1232,-1,1233,1232,1193,-1,1193,1194,1233,-1,1234,1233,1194,-1,1194,1195,1234,-1,1235,1234,1195,-1,1195,1196,1235,-1,1236,1235,1196,-1,1196,1197,1236,-1,1237,1236,1197,-1,1197,1198,1237,-1,1238,1237,1198,-1,1198,1199,1238,-1,1239,1238,1199,-1,1199,1200,1239,-1,1240,1239,1200,-1,1200,1201,1240,-1,1241,1240,1201,-1,1201,1202,1241,-1,1242,1241,1202,-1,1202,1203,1242,-1,1243,1242,1203,-1,1203,1204,1243,-1,1244,1243,1204,-1,1204,1205,1244,-1,1245,1244,1205,-1,1205,1206,1245,-1,1246,1245,1206,-1,1206,1207,1246,-1,1247,1246,1207,-1,1207,1208,1247,-1,1248,1247,1208,-1,1208,1209,1248,-1,1249,1248,1209,-1,1209,1210,1249,-1,1250,1249,1210,-1,1210,1211,1250,-1,1251,1250,1211,-1,1211,1212,1251,-1,1252,1251,1212,-1,1212,1213,1252,-1,1253,1252,1213,-1,1213,1214,1253,-1,1254,1253,1214,-1,1214,1215,1254,-1,1255,1254,1215,-1,1215,1216,1255,-1,1256,1255,1216,-1,1216,1217,1256,-1,1257,1256,1217,-1,1217,1218,1257,-1,1221,1220,1258,-1,1259,1258,1220,-1,1220,1222,1259,-1,1260,1259,1222,-1,1222,1223,1260,-1,1261,1260,1223,-1,1223,1224,1261,-1,1262,1261,1224,-1,1224,1225,1262,-1,1263,1262,1225,-1,1225,1226,1263,-1,1264,1263,1226,-1,1226,1227,1264,-1,1265,1264,1227,-1,1227,1228,1265,-1,1266,1265,1228,-1,1228,1229,1266,-1,1267,1266,1229,-1,1229,1230,1267,-1,1268,1267,1230,-1,1230,1231,1268,-1,1269,1268,1231,-1,1231,1232,1269,-1,1270,1269,1232,-1,1232,1233,1270,-1,1271,1270,1233,-1,1233,1234,1271,-1,1272,1271,1234,-1,1234,1235,1272,-1,1273,1272,1235,-1,1235,1236,1273,-1,1274,1273,1236,-1,1236,1237,1274,-1,1275,1274,1237,-1,1237,1238,1275,-1,1276,1275,1238,-1,1238,1239,1276,-1,1277,1276,1239,-1,1239,1240,1277,-1,1278,1277,1240,-1,1240,1241,1278,-1,1279,1278,1241,-1,1241,1242,1279,-1,1280,1279,1242,-1,1242,1243,1280,-1,1281,1280,1243,-1,1243,1244,1281,-1,1282,1281,1244,-1,1244,1245,1282,-1,1283,1282,1245,-1,1245,1246,1283,-1,1284,1283,1246,-1,1246,1247,1284,-1,1285,1284,1247,-1,1247,1248,1285,-1,1286,1285,1248,-1,1248,1249,1286,-1,1287,1286,1249,-1,1249,1250,1287,-1,1288,1287,1250,-1,1250,1251,1288,-1,1289,1288,1251,-1,1251,1252,1289,-1,1290,1289,1252,-1,1252,1253,1290,-1,1291,1290,1253,-1,1253,1254,1291,-1,1292,1291,1254,-1,1254,1255,1292,-1,1293,1292,1255,-1,1255,1256,1293,-1,1294,1293,1256,-1,1256,1257,1294,-1,1295,1294,1257,-1,1296,1297,1258,-1,1258,1259,1296,-1,1298,1296,1259,-1,1259,1260,1298,-1,1299,1298,1260,-1,1260,1261,1299,-1,1300,1299,1261,-1,1261,1262,1300,-1,1301,1300,1262,-1,1262,1263,1301,-1,1302,1301,1263,-1,1263,1264,1302,-1,1303,1302,1264,-1,1264,1265,1303,-1,1304,1303,1265,-1,1265,1266,1304,-1,1305,1304,1266,-1,1266,1267,1305,-1,1306,1305,1267,-1,1267,1268,1306,-1,1307,1306,1268,-1,1268,1269,1307,-1,1308,1307,1269,-1,1269,1270,1308,-1,1309,1308,1270,-1,1270,1271,1309,-1,1310,1309,1271,-1,1271,1272,1310,-1,1311,1310,1272,-1,1272,1273,1311,-1,1312,1311,1273,-1,1273,1274,1312,-1,1313,1312,1274,-1,1274,1275,1313,-1,1314,1313,1275,-1,1275,1276,1314,-1,1315,1314,1276,-1,1276,1277,1315,-1,1316,1315,1277,-1,1277,1278,1316,-1,1317,1316,1278,-1,1278,1279,1317,-1,1318,1317,1279,-1,1279,1280,1318,-1,1319,1318,1280,-1,1280,1281,1319,-1,1320,1319,1281,-1,1281,1282,1320,-1,1321,1320,1282,-1,1282,1283,1321,-1,1322,1321,1283,-1,1283,1284,1322,-1,1323,1322,1284,-1,1284,1285,1323,-1,1324,1323,1285,-1,1285,1286,1324,-1,1325,1324,1286,-1,1286,1287,1325,-1,1326,1325,1287,-1,1287,1288,1326,-1,1327,1326,1288,-1,1288,1289,1327,-1,1328,1327,1289,-1,1289,1290,1328,-1,1329,1328,1290,-1,1290,1291,1329,-1,1330,1329,1291,-1,1291,1292,1330,-1,1331,1330,1292,-1,1292,1293,1331,-1,1332,1331,1293,-1,1293,1294,1332,-1,1333,1332,1294,-1,1294,1295,1333,-1,1334,1333,1295,-1,1297,1296,1335,-1,1336,1335,1296,-1,1296,1298,1336,-1,1337,1336,1298,-1,1298,1299,1337,-1,1338,1337,1299,-1,1299,1300,1338,-1,1339,1338,1300,-1,1300,1301,1339,-1,1340,1339,1301,-1,1301,1302,1340,-1,1341,1340,1302,-1,1302,1303,1341,-1,1342,1341,1303,-1,1303,1304,1342,-1,1343,1342,1304,-1,1304,1305,1343,-1,1344,1343,1305,-1,1305,1306,1344,-1,1345,1344,1306,-1,1306,1307,1345,-1,1346,1345,1307,-1,1307,1308,1346,-1,1347,1346,1308,-1,1308,1309,1347,-1,1348,1347,1309,-1,1309,1310,1348,-1,1349,1348,1310,-1,1310,1311,1349,-1,1350,1349,1311,-1,1311,1312,1350,-1,1351,1350,1312,-1,1312,1313,1351,-1,1352,1351,1313,-1,1313,1314,1352,-1,1353,1352,1314,-1,1314,1315,1353,-1,1354,1353,1315,-1,1315,1316,1354,-1,1355,1354,1316,-1,1316,1317,1355,-1,1356,1355,1317,-1,1317,1318,1356,-1,1357,1356,1318,-1,1318,1319,1357,-1,1358,1357,1319,-1,1319,1320,1358,-1,1359,1358,1320,-1,1320,1321,1359,-1,1360,1359,1321,-1,1321,1322,1360,-1,1361,1360,1322,-1,1322,1323,1361,-1,1362,1361,1323,-1,1323,1324,1362,-1,1363,1362,1324,-1,1324,1325,1363,-1,1364,1363,1325,-1,1325,1326,1364,-1,1365,1364,1326,-1,1326,1327,1365,-1,1366,1365,1327,-1,1327,1328,1366,-1,1367,1366,1328,-1,1328,1329,1367,-1,1368,1367,1329,-1,1329,1330,1368,-1,1369,1368,1330,-1,1330,1331,1369,-1,1370,1369,1331,-1,1331,1332,1370,-1,1371,1370,1332,-1,1332,1333,1371,-1,1372,1371,1333,-1,1333,1334,1372,-1,1373,1374,1335,-1,1335,1336,1373,-1,1375,1373,1336,-1,1336,1337,1375,-1,1376,1375,1337,-1,1337,1338,1376,-1,1377,1376,1338,-1,1338,1339,1377,-1,1378,1377,1339,-1,1339,1340,1378,-1,1379,1378,1340,-1,1340,1341,1379,-1,1380,1379,1341,-1,1341,1342,1380,-1,1381,1380,1342,-1,1342,1343,1381,-1,1382,1381,1343,-1,1343,1344,1382,-1,1383,1382,1344,-1,1344,1345,1383,-1,1384,1383,1345,-1,1345,1346,1384,-1,1385,1384,1346,-1,1346,1347,1385,-1,1386,1385,1347,-1,1347,1348,1386,-1,1387,1386,1348,-1,1348,1349,1387,-1,1388,1387,1349,-1,1349,1350,1388,-1,1389,1388,1350,-1,1350,1351,1389,-1,1390,1389,1351,-1,1351,1352,1390,-1,1391,1390,1352,-1,1352,1353,1391,-1,1392,1391,1353,-1,1353,1354,1392,-1,1393,1392,1354,-1,1354,1355,1393,-1,1394,1393,1355,-1,1355,1356,1394,-1,1395,1394,1356,-1,1356,1357,1395,-1,1396,1395,1357,-1,1357,1358,1396,-1,1397,1396,1358,-1,1358,1359,1397,-1,1398,1397,1359,-1,1359,1360,1398,-1,1399,1398,1360,-1,1360,1361,1399,-1,1400,1399,1361,-1,1361,1362,1400,-1,1401,1400,1362,-1,1362,1363,1401,-1,1402,1401,1363,-1,1363,1364,1402,-1,1403,1402,1364,-1,1364,1365,1403,-1,1404,1403,1365,-1,1365,1366,1404,-1,1405,1404,1366,-1,1366,1367,1405,-1,1406,1405,1367,-1,1367,1368,1406,-1,1407,1406,1368,-1,1368,1369,1407,-1,1408,1407,1369,-1,1369,1370,1408,-1,1409,1408,1370,-1,1370,1371,1409,-1,1410,1409,1371,-1,1371,1372,1410,-1,1411,1410,1372,-1,1374,1373,1412,-1,1413,1412,1373,-1,1373,1375,1413,-1,1414,1413,1375,-1,1375,1376,1414,-1,1415,1414,1376,-1,1376,1377,1415,-1,1416,1415,1377,-1,1377,1378,1416,-1,1417,1416,1378,-1,1378,1379,1417,-1,1418,1417,1379,-1,1379,1380,1418,-1,1419,1418,1380,-1,1380,1381,1419,-1,1420,1419,1381,-1,1381,1382,1420,-1,1421,1420,1382,-1,1382,1383,1421,-1,1422,1421,1383,-1,1383,1384,1422,-1,1423,1422,1384,-1,1384,1385,1423,-1,1424,1423,1385,-1,1385,1386,1424,-1,1425,1424,1386,-1,1386,1387,1425,-1,1426,1425,1387,-1,1387,1388,1426,-1,1427,1426,1388,-1,1388,1389,1427,-1,1428,1427,1389,-1,1389,1390,1428,-1,1429,1428,1390,-1,1390,1391,1429,-1,1430,1429,1391,-1,1391,1392,1430,-1,1431,1430,1392,-1,1392,1393,1431,-1,1432,1431,1393,-1,1393,1394,1432,-1,1433,1432,1394,-1,1394,1395,1433,-1,1434,1433,1395,-1,1395,1396,1434,-1,1435,1434,1396,-1,1396,1397,1435,-1,1436,1435,1397,-1,1397,1398,1436,-1,1437,1436,1398,-1,1398,1399,1437,-1,1438,1437,1399,-1,1399,1400,1438,-1,1439,1438,1400,-1,1400,1401,1439,-1,1440,1439,1401,-1,1401,1402,1440,-1,1441,1440,1402,-1,1402,1403,1441,-1,1442,1441,1403,-1,1403,1404,1442,-1,1443,1442,1404,-1,1404,1405,1443,-1,1444,1443,1405,-1,1405,1406,1444,-1,1445,1444,1406,-1,1406,1407,1445,-1,1446,1445,1407,-1,1407,1408,1446,-1,1447,1446,1408,-1,1408,1409,1447,-1,1448,1447,1409,-1,1409,1410,1448,-1,1449,1448,1410,-1,1410,1411,1449,-1,1450,1451,1412,-1,1412,1413,1450,-1,1452,1450,1413,-1,1413,1414,1452,-1,1453,1452,1414,-1,1414,1415,1453,-1,1454,1453,1415,-1,1415,1416,1454,-1,1455,1454,1416,-1,1416,1417,1455,-1,1456,1455,1417,-1,1417,1418,1456,-1,1457,1456,1418,-1,1418,1419,1457,-1,1458,1457,1419,-1,1419,1420,1458,-1,1459,1458,1420,-1,1420,1421,1459,-1,1460,1459,1421,-1,1421,1422,1460,-1,1461,1460,1422,-1,1422,1423,1461,-1,1462,1461,1423,-1,1423,1424,1462,-1,1463,1462,1424,-1,1424,1425,1463,-1,1464,1463,1425,-1,1425,1426,1464,-1,1465,1464,1426,-1,1426,1427,1465,-1,1466,1465,1427,-1,1427,1428,1466,-1,1467,1466,1428,-1,1428,1429,1467,-1,1468,1467,1429,-1,1429,1430,1468,-1,1469,1468,1430,-1,1430,1431,1469,-1,1470,1469,1431,-1,1431,1432,1470,-1,1471,1470,1432,-1,1432,1433,1471,-1,1472,1471,1433,-1,1433,1434,1472,-1,1473,1472,1434,-1,1434,1435,1473,-1,1474,1473,1435,-1,1435,1436,1474,-1,1475,1474,1436,-1,1436,1437,1475,-1,1476,1475,1437,-1,1437,1438,1476,-1,1477,1476,1438,-1,1438,1439,1477,-1,1478,1477,1439,-1,1439,1440,1478,-1,1479,1478,1440,-1,1440,1441,1479,-1,1480,1479,1441,-1,1441,1442,1480,-1,1481,1480,1442,-1,1442,1443,1481,-1,1482,1481,1443,-1,1443,1444,1482,-1,1483,1482,1444,-1,1444,1445,1483,-1,1484,1483,1445,-1,1445,1446,1484,-1,1485,1484,1446,-1,1446,1447,1485,-1,1486,1485,1447,-1,1447,1448,1486,-1,1487,1486,1448,-1,1448,1449,1487,-1,1488,1487,1449,-1,1451,1450,1489,-1,1490,1489,1450,-1,1450,1452,1490,-1,1491,1490,1452,-1,1452,1453,1491,-1,1492,1491,1453,-1,1453,1454,1492,-1,1493,1492,1454,-1,1454,1455,1493,-1,1494,1493,1455,-1,1455,1456,1494,-1,1495,1494,1456,-1,1456,1457,1495,-1,1496,1495,1457,-1,1457,1458,1496,-1,1497,1496,1458,-1,1458,1459,1497,-1,1498,1497,1459,-1,1459,1460,1498,-1,1499,1498,1460,-1,1460,1461,1499,-1,1500,1499,1461,-1,1461,1462,1500,-1,1501,1500,1462,-1,1462,1463,1501,-1,1502,1501,1463,-1,1463,1464,1502,-1,1503,1502,1464,-1,1464,1465,1503,-1,1504,1503,1465,-1,1465,1466,1504,-1,1505,1504,1466,-1,1466,1467,1505,-1,1506,1505,1467,-1,1467,1468,1506,-1,1507,1506,1468,-1,1468,1469,1507,-1,1508,1507,1469,-1,1469,1470,1508,-1,1509,1508,1470,-1,1470,1471,1509,-1,1510,1509,1471,-1,1471,1472,1510,-1,1511,1510,1472,-1,1472,1473,1511,-1,1512,1511,1473,-1,1473,1474,1512,-1,1513,1512,1474,-1,1474,1475,1513,-1,1514,1513,1475,-1,1475,1476,1514,-1,1515,1514,1476,-1,1476,1477,1515,-1,1516,1515,1477,-1,1477,1478,1516,-1,1517,1516,1478,-1,1478,1479,1517,-1,1518,1517,1479,-1,1479,1480,1518,-1,1519,1518,1480,-1,1480,1481,1519,-1,1520,1519,1481,-1,1481,1482,1520,-1,1521,1520,1482,-1,1482,1483,1521,-1,1522,1521,1483,-1,1483,1484,1522,-1,1523,1522,1484,-1,1484,1485,1523,-1,1524,1523,1485,-1,1485,1486,1524,-1,1525,1524,1486,-1,1486,1487,1525,-1,1526,1525,1487,-1,1487,1488,1526,-1,1489,1490,1527,-1,1528,1527,1490,-1,1490,1491,1528,-1,1529,1528,1491,-1,1491,1492,1529,-1,1530,1529,1492,-1,1492,1493,1530,-1,1531,1530,1493,-1,1493,1494,1531,-1,1532,1531,1494,-1,1494,1495,1532,-1,1533,1532,1495,-1,1495,1496,1533,-1,1534,1533,1496,-1,1496,1497,1534,-1,1535,1534,1497,-1,1497,1498,1535,-1,1536,1535,1498,-1,1498,1499,1536,-1,1537,1536,1499,-1,1499,1500,1537,-1,1538,1537,1500,-1,1500,1501,1538,-1,1539,1538,1501,-1,1501,1502,1539,-1,1540,1539,1502,-1,1502,1503,1540,-1,1541,1540,1503,-1,1503,1504,1541,-1,1542,1541,1504,-1,1504,1505,1542,-1,1543,1542,1505,-1,1505,1506,1543,-1,1544,1543,1506,-1,1506,1507,1544,-1,1545,1544,1507,-1,1507,1508,1545,-1,1546,1545,1508,-1,1508,1509,1546,-1,1547,1546,1509,-1,1509,1510,1547,-1,1548,1547,1510,-1,1510,1511,1548,-1,1549,1548,1511,-1,1511,1512,1549,-1,1550,1549,1512,-1,1512,1513,1550,-1,1551,1550,1513,-1,1513,1514,1551,-1,1552,1551,1514,-1,1514,1515,1552,-1,1553,1552,1515,-1,1515,1516,1553,-1,1554,1553,1516,-1,1516,1517,1554,-1,1555,1554,1517,-1,1517,1518,1555,-1,1556,1555,1518,-1,1518,1519,1556,-1,1557,1556,1519,-1,1519,1520,1557,-1,1558,1557,1520,-1,1520,1521,1558,-1,1559,1558,1521,-1,1521,1522,1559,-1,1560,1559,1522,-1,1522,1523,1560,-1,1561,1560,1523,-1,1523,1524,1561,-1,1562,1561,1524,-1,1524,1525,1562,-1,1563,1562,1525,-1,1525,1526,1563,-1,1564,1563,1526,-1,1528,1529,1565,-1,1566,1565,1529,-1,1529,1530,1566,-1,1567,1566,1530,-1,1530,1531,1567,-1,1568,1567,1531,-1,1531,1532,1568,-1,1569,1568,1532,-1,1532,1533,1569,-1,1570,1569,1533,-1,1533,1534,1570,-1,1571,1570,1534,-1,1534,1535,1571,-1,1572,1571,1535,-1,1535,1536,1572,-1,1573,1572,1536,-1,1536,1537,1573,-1,1574,1573,1537,-1,1537,1538,1574,-1,1575,1574,1538,-1,1538,1539,1575,-1,1576,1575,1539,-1,1539,1540,1576,-1,1577,1576,1540,-1,1540,1541,1577,-1,1578,1577,1541,-1,1541,1542,1578,-1,1579,1578,1542,-1,1542,1543,1579,-1,1580,1579,1543,-1,1543,1544,1580,-1,1581,1580,1544,-1,1544,1545,1581,-1,1582,1581,1545,-1,1545,1546,1582,-1,1583,1582,1546,-1,1546,1547,1583,-1,1584,1583,1547,-1,1547,1548,1584,-1,1585,1584,1548,-1,1548,1549,1585,-1,1586,1585,1549,-1,1549,1550,1586,-1,1587,1586,1550,-1,1550,1551,1587,-1,1588,1587,1551,-1,1551,1552,1588,-1,1589,1588,1552,-1,1552,1553,1589,-1,1590,1589,1553,-1,1553,1554,1590,-1,1591,1590,1554,-1,1554,1555,1591,-1,1592,1591,1555,-1,1555,1556,1592,-1,1593,1592,1556,-1,1556,1557,1593,-1,1594,1593,1557,-1,1557,1558,1594,-1,1595,1594,1558,-1,1558,1559,1595,-1,1596,1595,1559,-1,1559,1560,1596,-1,1597,1596,1560,-1,1560,1561,1597,-1,1598,1597,1561,-1,1561,1562,1598,-1,1599,1598,1562,-1,1562,1563,1599,-1,1600,1599,1563,-1,1563,1564,1600,-1,1601,1600,1564,-1,1564,1602,1601,-1,1603,1601,1602,-1,1602,1604,1603,-1,1605,1603,1604,-1,1606,1607,1565,-1,1565,1566,1606,-1,1608,1606,1566,-1,1566,1567,1608,-1,1609,1608,1567,-1,1567,1568,1609,-1,1610,1609,1568,-1,1568,1569,1610,-1,1611,1610,1569,-1,1569,1570,1611,-1,1612,1611,1570,-1,1570,1571,1612,-1,1613,1612,1571,-1,1571,1572,1613,-1,1614,1613,1572,-1,1572,1573,1614,-1,1615,1614,1573,-1,1573,1574,1615,-1,1616,1615,1574,-1,1574,1575,1616,-1,1617,1616,1575,-1,1575,1576,1617,-1,1618,1617,1576,-1,1576,1577,1618,-1,1619,1618,1577,-1,1577,1578,1619,-1,1620,1619,1578,-1,1578,1579,1620,-1,1621,1620,1579,-1,1579,1580,1621,-1,1622,1621,1580,-1,1580,1581,1622,-1,1623,1622,1581,-1,1581,1582,1623,-1,1624,1623,1582,-1,1582,1583,1624,-1,1625,1624,1583,-1,1583,1584,1625,-1,1626,1625,1584,-1,1584,1585,1626,-1,1627,1626,1585,-1,1585,1586,1627,-1,1628,1627,1586,-1,1586,1587,1628,-1,1629,1628,1587,-1,1587,1588,1629,-1,1630,1629,1588,-1,1588,1589,1630,-1,1631,1630,1589,-1,1589,1590,1631,-1,1632,1631,1590,-1,1590,1591,1632,-1,1633,1632,1591,-1,1591,1592,1633,-1,1634,1633,1592,-1,1592,1593,1634,-1,1635,1634,1593,-1,1593,1594,1635,-1,1636,1635,1594,-1,1594,1595,1636,-1,1637,1636,1595,-1,1595,1596,1637,-1,1638,1637,1596,-1,1596,1597,1638,-1,1639,1638,1597,-1,1597,1598,1639,-1,1640,1639,1598,-1,1598,1599,1640,-1,1641,1640,1599,-1,1599,1600,1641,-1,1642,1641,1600,-1,1600,1601,1642,-1,1643,1642,1601,-1,1601,1603,1643,-1,1644,1643,1603,-1,1603,1605,1644,-1,1645,1644,1605,-1,1646,1647,1607,-1,1607,1606,1646,-1,1648,1646,1606,-1,1606,1608,1648,-1,1649,1648,1608,-1,1608,1609,1649,-1,1650,1649,1609,-1,1609,1610,1650,-1,1651,1650,1610,-1,1610,1611,1651,-1,1652,1651,1611,-1,1611,1612,1652,-1,1653,1652,1612,-1,1612,1613,1653,-1,1654,1653,1613,-1,1613,1614,1654,-1,1655,1654,1614,-1,1614,1615,1655,-1,1656,1655,1615,-1,1615,1616,1656,-1,1657,1656,1616,-1,1616,1617,1657,-1,1658,1657,1617,-1,1617,1618,1658,-1,1659,1658,1618,-1,1618,1619,1659,-1,1660,1659,1619,-1,1619,1620,1660,-1,1661,1660,1620,-1,1620,1621,1661,-1,1662,1661,1621,-1,1621,1622,1662,-1,1663,1662,1622,-1,1622,1623,1663,-1,1664,1663,1623,-1,1623,1624,1664,-1,1665,1664,1624,-1,1624,1625,1665,-1,1666,1665,1625,-1,1625,1626,1666,-1,1667,1666,1626,-1,1626,1627,1667,-1,1668,1667,1627,-1,1627,1628,1668,-1,1669,1668,1628,-1,1628,1629,1669,-1,1670,1669,1629,-1,1629,1630,1670,-1,1671,1670,1630,-1,1630,1631,1671,-1,1672,1671,1631,-1,1631,1632,1672,-1,1673,1672,1632,-1,1632,1633,1673,-1,1674,1673,1633,-1,1633,1634,1674,-1,1675,1674,1634,-1,1634,1635,1675,-1,1676,1675,1635,-1,1635,1636,1676,-1,1677,1676,1636,-1,1636,1637,1677,-1,1678,1677,1637,-1,1637,1638,1678,-1,1679,1678,1638,-1,1638,1639,1679,-1,1680,1679,1639,-1,1639,1640,1680,-1,1681,1680,1640,-1,1640,1641,1681,-1,1682,1681,1641,-1,1641,1642,1682,-1,1683,1682,1642,-1,1642,1643,1683,-1,1684,1683,1643,-1,1643,1644,1684,-1,1685,1684,1644,-1,1644,1645,1685,-1,1686,1687,1647,-1,1647,1646,1686,-1,1688,1686,1646,-1,1646,1648,1688,-1,1689,1688,1648,-1,1648,1649,1689,-1,1690,1689,1649,-1,1649,1650,1690,-1,1691,1690,1650,-1,1650,1651,1691,-1,1692,1691,1651,-1,1651,1652,1692,-1,1693,1692,1652,-1,1652,1653,1693,-1,1694,1693,1653,-1,1653,1654,1694,-1,1695,1694,1654,-1,1654,1655,1695,-1,1696,1695,1655,-1,1655,1656,1696,-1,1697,1696,1656,-1,1656,1657,1697,-1,1698,1697,1657,-1,1657,1658,1698,-1,1699,1698,1658,-1,1658,1659,1699,-1,1700,1699,1659,-1,1659,1660,1700,-1,1701,1700,1660,-1,1660,1661,1701,-1,1702,1701,1661,-1,1661,1662,1702,-1,1703,1702,1662,-1,1662,1663,1703,-1,1704,1703,1663,-1,1663,1664,1704,-1,1705,1704,1664,-1,1664,1665,1705,-1,1706,1705,1665,-1,1665,1666,1706,-1,1707,1706,1666,-1,1666,1667,1707,-1,1708,1707,1667,-1,1667,1668,1708,-1,1709,1708,1668,-1,1668,1669,1709,-1,1710,1709,1669,-1,1669,1670,1710,-1,1711,1710,1670,-1,1670,1671,1711,-1,1712,1711,1671,-1,1671,1672,1712,-1,1713,1712,1672,-1,1672,1673,1713,-1,1714,1713,1673,-1,1673,1674,1714,-1,1715,1714,1674,-1,1674,1675,1715,-1,1716,1715,1675,-1,1675,1676,1716,-1,1717,1716,1676,-1,1676,1677,1717,-1,1718,1717,1677,-1,1677,1678,1718,-1,1719,1718,1678,-1,1678,1679,1719,-1,1720,1719,1679,-1,1679,1680,1720,-1,1721,1720,1680,-1,1680,1681,1721,-1,1722,1721,1681,-1,1681,1682,1722,-1,1723,1722,1682,-1,1682,1683,1723,-1,1724,1723,1683,-1,1683,1684,1724,-1,1687,1686,1725,-1,1726,1725,1686,-1,1686,1688,1726,-1,1727,1726,1688,-1,1688,1689,1727,-1,1728,1727,1689,-1,1689,1690,1728,-1,1729,1728,1690,-1,1690,1691,1729,-1,1730,1729,1691,-1,1691,1692,1730,-1,1731,1730,1692,-1,1692,1693,1731,-1,1732,1731,1693,-1,1693,1694,1732,-1,1733,1732,1694,-1,1694,1695,1733,-1,1734,1733,1695,-1,1695,1696,1734,-1,1735,1734,1696,-1,1696,1697,1735,-1,1736,1735,1697,-1,1697,1698,1736,-1,1737,1736,1698,-1,1698,1699,1737,-1,1738,1737,1699,-1,1699,1700,1738,-1,1739,1738,1700,-1,1700,1701,1739,-1,1740,1739,1701,-1,1701,1702,1740,-1,1741,1740,1702,-1,1702,1703,1741,-1,1742,1741,1703,-1,1703,1704,1742,-1,1743,1742,1704,-1,1704,1705,1743,-1,1744,1743,1705,-1,1705,1706,1744,-1,1745,1744,1706,-1,1706,1707,1745,-1,1746,1745,1707,-1,1707,1708,1746,-1,1747,1746,1708,-1,1708,1709,1747,-1,1748,1747,1709,-1,1709,1710,1748,-1,1749,1748,1710,-1,1710,1711,1749,-1,1750,1749,1711,-1,1711,1712,1750,-1,1751,1750,1712,-1,1712,1713,1751,-1,1752,1751,1713,-1,1713,1714,1752,-1,1753,1752,1714,-1,1714,1715,1753,-1,1754,1753,1715,-1,1715,1716,1754,-1,1755,1754,1716,-1,1716,1717,1755,-1,1756,1755,1717,-1,1717,1718,1756,-1,1757,1756,1718,-1,1718,1719,1757,-1,1758,1757,1719,-1,1719,1720,1758,-1,1759,1758,1720,-1,1720,1721,1759,-1,1760,1759,1721,-1,1721,1722,1760,-1,1761,1760,1722,-1,1722,1723,1761,-1,1762,1761,1723,-1,1723,1724,1762,-1,1763,1762,1724,-1,1725,1726,1764,-1,1765,1764,1726,-1,1726,1727,1765,-1,1766,1765,1727,-1,1727,1728,1766,-1,1767,1766,1728,-1,1728,1729,1767,-1,1768,1767,1729,-1,1729,1730,1768,-1,1769,1768,1730,-1,1730,1731,1769,-1,1770,1769,1731,-1,1731,1732,1770,-1,1771,1770,1732,-1,1732,1733,1771,-1,1772,1771,1733,-1,1733,1734,1772,-1,1773,1772,1734,-1,1734,1735,1773,-1,1774,1773,1735,-1,1735,1736,1774,-1,1775,1774,1736,-1,1736,1737,1775,-1,1776,1775,1737,-1,1737,1738,1776,-1,1777,1776,1738,-1,1738,1739,1777,-1,1778,1777,1739,-1,1739,1740,1778,-1,1779,1778,1740,-1,1740,1741,1779,-1,1780,1779,1741,-1,1741,1742,1780,-1,1781,1780,1742,-1,1742,1743,1781,-1,1782,1781,1743,-1,1743,1744,1782,-1,1783,1782,1744,-1,1744,1745,1783,-1,1784,1783,1745,-1,1745,1746,1784,-1,1785,1784,1746,-1,1746,1747,1785,-1,1786,1785,1747,-1,1747,1748,1786,-1,1787,1786,1748,-1,1748,1749,1787,-1,1788,1787,1749,-1,1749,1750,1788,-1,1789,1788,1750,-1,1750,1751,1789,-1,1790,1789,1751,-1,1751,1752,1790,-1,1791,1790,1752,-1,1752,1753,1791,-1,1792,1791,1753,-1,1753,1754,1792,-1,1793,1792,1754,-1,1754,1755,1793,-1,1794,1793,1755,-1,1755,1756,1794,-1,1795,1794,1756,-1,1756,1757,1795,-1,1796,1795,1757,-1,1757,1758,1796,-1,1797,1796,1758,-1,1758,1759,1797,-1,1798,1797,1759,-1,1759,1760,1798,-1,1799,1798,1760,-1,1760,1761,1799,-1,1800,1799,1761,-1,1761,1762,1800,-1,1801,1800,1762,-1,1762,1763,1801,-1,1802,1801,1763,-1,1803,1804,1764,-1,1764,1765,1803,-1,1805,1803,1765,-1,1765,1766,1805,-1,1806,1805,1766,-1,1766,1767,1806,-1,1807,1806,1767,-1,1767,1768,1807,-1,1808,1807,1768,-1,1768,1769,1808,-1,1809,1808,1769,-1,1769,1770,1809,-1,1810,1809,1770,-1,1770,1771,1810,-1,1811,1810,1771,-1,1771,1772,1811,-1,1812,1811,1772,-1,1772,1773,1812,-1,1813,1812,1773,-1,1773,1774,1813,-1,1814,1813,1774,-1,1774,1775,1814,-1,1815,1814,1775,-1,1775,1776,1815,-1,1816,1815,1776,-1,1776,1777,1816,-1,1817,1816,1777,-1,1777,1778,1817,-1,1818,1817,1778,-1,1778,1779,1818,-1,1819,1818,1779,-1,1779,1780,1819,-1,1820,1819,1780,-1,1780,1781,1820,-1,1821,1820,1781,-1,1781,1782,1821,-1,1822,1821,1782,-1,1782,1783,1822,-1,1823,1822,1783,-1,1783,1784,1823,-1,1824,1823,1784,-1,1784,1785,1824,-1,1825,1824,1785,-1,1785,1786,1825,-1,1826,1825,1786,-1,1786,1787,1826,-1,1827,1826,1787,-1,1787,1788,1827,-1,1828,1827,1788,-1,1788,1789,1828,-1,1829,1828,1789,-1,1789,1790,1829,-1,1830,1829,1790,-1,1790,1791,1830,-1,1831,1830,1791,-1,1791,1792,1831,-1,1832,1831,1792,-1,1792,1793,1832,-1,1833,1832,1793,-1,1793,1794,1833,-1,1834,1833,1794,-1,1794,1795,1834,-1,1835,1834,1795,-1,1795,1796,1835,-1,1836,1835,1796,-1,1796,1797,1836,-1,1837,1836,1797,-1,1797,1798,1837,-1,1838,1837,1798,-1,1798,1799,1838,-1,1839,1838,1799,-1,1799,1800,1839,-1,1840,1839,1800,-1,1800,1801,1840,-1,1841,1840,1801,-1,1801,1802,1841,-1,1842,1843,1804,-1,1804,1803,1842,-1,1844,1842,1803,-1,1803,1805,1844,-1,1845,1844,1805,-1,1805,1806,1845,-1,1846,1845,1806,-1,1806,1807,1846,-1,1847,1846,1807,-1,1807,1808,1847,-1,1848,1847,1808,-1,1808,1809,1848,-1,1849,1848,1809,-1,1809,1810,1849,-1,1850,1849,1810,-1,1810,1811,1850,-1,1851,1850,1811,-1,1811,1812,1851,-1,1852,1851,1812,-1,1812,1813,1852,-1,1853,1852,1813,-1,1813,1814,1853,-1,1854,1853,1814,-1,1814,1815,1854,-1,1855,1854,1815,-1,1815,1816,1855,-1,1856,1855,1816,-1,1816,1817,1856,-1,1857,1856,1817,-1,1817,1818,1857,-1,1858,1857,1818,-1,1818,1819,1858,-1,1859,1858,1819,-1,1819,1820,1859,-1,1860,1859,1820,-1,1820,1821,1860,-1,1861,1860,1821,-1,1821,1822,1861,-1,1862,1861,1822,-1,1822,1823,1862,-1,1863,1862,1823,-1,1823,1824,1863,-1,1864,1863,1824,-1,1824,1825,1864,-1,1865,1864,1825,-1,1825,1826,1865,-1,1866,1865,1826,-1,1826,1827,1866,-1,1867,1866,1827,-1,1827,1828,1867,-1,1868,1867,1828,-1,1828,1829,1868,-1,1869,1868,1829,-1,1829,1830,1869,-1,1870,1869,1830,-1,1830,1831,1870,-1,1871,1870,1831,-1,1831,1832,1871,-1,1872,1871,1832,-1,1832,1833,1872,-1,1873,1872,1833,-1,1833,1834,1873,-1,1874,1873,1834,-1,1834,1835,1874,-1,1875,1874,1835,-1,1835,1836,1875,-1,1876,1875,1836,-1,1836,1837,1876,-1,1877,1876,1837,-1,1837,1838,1877,-1,1878,1877,1838,-1,1838,1839,1878,-1,1879,1878,1839,-1,1839,1840,1879,-1,1880,1879,1840,-1,1840,1841,1880,-1,1881,1880,1841,-1,1843,1842,1882,-1,1883,1882,1842,-1,1842,1844,1883,-1,1884,1883,1844,-1,1844,1845,1884,-1,1885,1884,1845,-1,1845,1846,1885,-1,1886,1885,1846,-1,1846,1847,1886,-1,1887,1886,1847,-1,1847,1848,1887,-1,1888,1887,1848,-1,1848,1849,1888,-1,1889,1888,1849,-1,1849,1850,1889,-1,1890,1889,1850,-1,1850,1851,1890,-1,1891,1890,1851,-1,1851,1852,1891,-1,1892,1891,1852,-1,1852,1853,1892,-1,1893,1892,1853,-1,1853,1854,1893,-1,1894,1893,1854,-1,1854,1855,1894,-1,1895,1894,1855,-1,1855,1856,1895,-1,1896,1895,1856,-1,1856,1857,1896,-1,1897,1896,1857,-1,1857,1858,1897,-1,1898,1897,1858,-1,1858,1859,1898,-1,1899,1898,1859,-1,1859,1860,1899,-1,1900,1899,1860,-1,1860,1861,1900,-1,1901,1900,1861,-1,1861,1862,1901,-1,1902,1901,1862,-1,1862,1863,1902,-1,1903,1902,1863,-1,1863,1864,1903,-1,1904,1903,1864,-1,1864,1865,1904,-1,1905,1904,1865,-1,1865,1866,1905,-1,1906,1905,1866,-1,1866,1867,1906,-1,1907,1906,1867,-1,1867,1868,1907,-1,1908,1907,1868,-1,1868,1869,1908,-1,1909,1908,1869,-1,1869,1870,1909,-1,1910,1909,1870,-1,1870,1871,1910,-1,1911,1910,1871,-1,1871,1872,1911,-1,1912,1911,1872,-1,1872,1873,1912,-1,1913,1912,1873,-1,1873,1874,1913,-1,1914,1913,1874,-1,1874,1875,1914,-1,1915,1914,1875,-1,1875,1876,1915,-1,1916,1915,1876,-1,1876,1877,1916,-1,1917,1916,1877,-1,1877,1878,1917,-1,1918,1917,1878,-1,1878,1879,1918,-1,1919,1918,1879,-1,1879,1880,1919,-1,1920,1919,1880,-1,1880,1881,1920,-1,1921,1920,1881,-1,1922,1923,1882,-1,1882,1883,1922,-1,1924,1922,1883,-1,1883,1884,1924,-1,1925,1924,1884,-1,1884,1885,1925,-1,1926,1925,1885,-1,1885,1886,1926,-1,1927,1926,1886,-1,1886,1887,1927,-1,1928,1927,1887,-1,1887,1888,1928,-1,1929,1928,1888,-1,1888,1889,1929,-1,1930,1929,1889,-1,1889,1890,1930,-1,1931,1930,1890,-1,1890,1891,1931,-1,1932,1931,1891,-1,1891,1892,1932,-1,1933,1932,1892,-1,1892,1893,1933,-1,1934,1933,1893,-1,1893,1894,1934,-1,1935,1934,1894,-1,1894,1895,1935,-1,1936,1935,1895,-1,1895,1896,1936,-1,1937,1936,1896,-1,1896,1897,1937,-1,1938,1937,1897,-1,1897,1898,1938,-1,1939,1938,1898,-1,1898,1899,1939,-1,1940,1939,1899,-1,1899,1900,1940,-1,1941,1940,1900,-1,1900,1901,1941,-1,1942,1941,1901,-1,1901,1902,1942,-1,1943,1942,1902,-1,1902,1903,1943,-1,1944,1943,1903,-1,1903,1904,1944,-1,1945,1944,1904,-1,1904,1905,1945,-1,1946,1945,1905,-1,1905,1906,1946,-1,1947,1946,1906,-1,1906,1907,1947,-1,1948,1947,1907,-1,1907,1908,1948,-1,1949,1948,1908,-1,1908,1909,1949,-1,1950,1949,1909,-1,1909,1910,1950,-1,1951,1950,1910,-1,1910,1911,1951,-1,1952,1951,1911,-1,1911,1912,1952,-1,1953,1952,1912,-1,1912,1913,1953,-1,1954,1953,1913,-1,1913,1914,1954,-1,1955,1954,1914,-1,1914,1915,1955,-1,1956,1955,1915,-1,1915,1916,1956,-1,1957,1956,1916,-1,1916,1917,1957,-1,1958,1957,1917,-1,1917,1918,1958,-1,1959,1958,1918,-1,1918,1919,1959,-1,1960,1959,1919,-1,1919,1920,1960,-1,1961,1960,1920,-1,1920,1921,1961,-1,1923,1922,1962,-1,1963,1962,1922,-1,1922,1924,1963,-1,1964,1963,1924,-1,1924,1925,1964,-1,1965,1964,1925,-1,1925,1926,1965,-1,1966,1965,1926,-1,1926,1927,1966,-1,1967,1966,1927,-1,1927,1928,1967,-1,1968,1967,1928,-1,1928,1929,1968,-1,1969,1968,1929,-1,1929,1930,1969,-1,1970,1969,1930,-1,1930,1931,1970,-1,1971,1970,1931,-1,1931,1932,1971,-1,1972,1971,1932,-1,1932,1933,1972,-1,1973,1972,1933,-1,1933,1934,1973,-1,1974,1973,1934,-1,1934,1935,1974,-1,1975,1974,1935,-1,1935,1936,1975,-1,1976,1975,1936,-1,1936,1937,1976,-1,1977,1976,1937,-1,1937,1938,1977,-1,1978,1977,1938,-1,1938,1939,1978,-1,1979,1978,1939,-1,1939,1940,1979,-1,1980,1979,1940,-1,1940,1941,1980,-1,1981,1980,1941,-1,1941,1942,1981,-1,1982,1981,1942,-1,1942,1943,1982,-1,1983,1982,1943,-1,1943,1944,1983,-1,1984,1983,1944,-1,1944,1945,1984,-1,1985,1984,1945,-1,1945,1946,1985,-1,1986,1985,1946,-1,1946,1947,1986,-1,1987,1986,1947,-1,1947,1948,1987,-1,1988,1987,1948,-1,1948,1949,1988,-1,1989,1988,1949,-1,1949,1950,1989,-1,1990,1989,1950,-1,1950,1951,1990,-1,1991,1990,1951,-1,1951,1952,1991,-1,1992,1991,1952,-1,1952,1953,1992,-1,1993,1992,1953,-1,1953,1954,1993,-1,1994,1993,1954,-1,1954,1955,1994,-1,1995,1994,1955,-1,1955,1956,1995,-1,1996,1995,1956,-1,1956,1957,1996,-1,1997,1996,1957,-1,1957,1958,1997,-1,1998,1997,1958,-1,1958,1959,1998,-1,1962,1963,1999,-1,2000,1999,1963,-1,1963,1964,2000,-1,2001,2000,1964,-1,1964,1965,2001,-1,2002,2001,1965,-1,1965,1966,2002,-1,2003,2002,1966,-1,1966,1967,2003,-1,2004,2003,1967,-1,1967,1968,2004,-1,2005,2004,1968,-1,1968,1969,2005,-1,2006,2005,1969,-1,1969,1970,2006,-1,2007,2006,1970,-1,1970,1971,2007,-1,2008,2007,1971,-1,1971,1972,2008,-1,2009,2008,1972,-1,1972,1973,2009,-1,2010,2009,1973,-1,1973,1974,2010,-1,2011,2010,1974,-1,1974,1975,2011,-1,2012,2011,1975,-1,1975,1976,2012,-1,2013,2012,1976,-1,1976,1977,2013,-1,2014,2013,1977,-1,1977,1978,2014,-1,2015,2014,1978,-1,1978,1979,2015,-1,2016,2015,1979,-1,1979,1980,2016,-1,2017,2016,1980,-1,1980,1981,2017,-1,2018,2017,1981,-1,1981,1982,2018,-1,2019,2018,1982,-1,1982,1983,2019,-1,2020,2019,1983,-1,1983,1984,2020,-1,2021,2020,1984,-1,1984,1985,2021,-1,2022,2021,1985,-1,1985,1986,2022,-1,2023,2022,1986,-1,1986,1987,2023,-1,2024,2023,1987,-1,1987,1988,2024,-1,2025,2024,1988,-1,1988,1989,2025,-1,2026,2025,1989,-1,1989,1990,2026,-1,2027,2026,1990,-1,1990,1991,2027,-1,2028,2027,1991,-1,1991,1992,2028,-1,2029,2028,1992,-1,1992,1993,2029,-1,2030,2029,1993,-1,1993,1994,2030,-1,2031,2030,1994,-1,1994,1995,2031,-1,2032,2031,1995,-1,1995,1996,2032,-1,2033,2032,1996,-1,1996,1997,2033,-1,2034,2033,1997,-1,1997,1998,2034,-1,2035,2036,1999,-1,1999,2000,2035,-1,2037,2035,2000,-1,2000,2001,2037,-1,2038,2037,2001,-1,2001,2002,2038,-1,2039,2038,2002,-1,2002,2003,2039,-1,2040,2039,2003,-1,2003,2004,2040,-1,2041,2040,2004,-1,2004,2005,2041,-1,2042,2041,2005,-1,2005,2006,2042,-1,2043,2042,2006,-1,2006,2007,2043,-1,2044,2043,2007,-1,2007,2008,2044,-1,2045,2044,2008,-1,2008,2009,2045,-1,2046,2045,2009,-1,2009,2010,2046,-1,2047,2046,2010,-1,2010,2011,2047,-1,2048,2047,2011,-1,2011,2012,2048,-1,2049,2048,2012,-1,2012,2013,2049,-1,2050,2049,2013,-1,2013,2014,2050,-1,2051,2050,2014,-1,2014,2015,2051,-1,2052,2051,2015,-1,2015,2016,2052,-1,2053,2052,2016,-1,2016,2017,2053,-1,2054,2053,2017,-1,2017,2018,2054,-1,2055,2054,2018,-1,2018,2019,2055,-1,2056,2055,2019,-1,2019,2020,2056,-1,2057,2056,2020,-1,2020,2021,2057,-1,2058,2057,2021,-1,2021,2022,2058,-1,2059,2058,2022,-1,2022,2023,2059,-1,2060,2059,2023,-1,2023,2024,2060,-1,2061,2060,2024,-1,2024,2025,2061,-1,2062,2061,2025,-1,2025,2026,2062,-1,2063,2062,2026,-1,2026,2027,2063,-1,2064,2063,2027,-1,2027,2028,2064,-1,2065,2064,2028,-1,2028,2029,2065,-1,2066,2065,2029,-1,2029,2030,2066,-1,2067,2066,2030,-1,2030,2031,2067,-1,2068,2067,2031,-1,2031,2032,2068,-1,2069,2068,2032,-1,2032,2033,2069,-1,2070,2069,2033,-1,2033,2034,2070,-1,2036,2035,2071,-1,2072,2071,2035,-1,2035,2037,2072,-1,2073,2072,2037,-1,2037,2038,2073,-1,2074,2073,2038,-1,2038,2039,2074,-1,2075,2074,2039,-1,2039,2040,2075,-1,2076,2075,2040,-1,2040,2041,2076,-1,2077,2076,2041,-1,2041,2042,2077,-1,2078,2077,2042,-1,2042,2043,2078,-1,2079,2078,2043,-1,2043,2044,2079,-1,2080,2079,2044,-1,2044,2045,2080,-1,2081,2080,2045,-1,2045,2046,2081,-1,2082,2081,2046,-1,2046,2047,2082,-1,2083,2082,2047,-1,2047,2048,2083,-1,2084,2083,2048,-1,2048,2049,2084,-1,2085,2084,2049,-1,2049,2050,2085,-1,2086,2085,2050,-1,2050,2051,2086,-1,2087,2086,2051,-1,2051,2052,2087,-1,2088,2087,2052,-1,2052,2053,2088,-1,2089,2088,2053,-1,2053,2054,2089,-1,2090,2089,2054,-1,2054,2055,2090,-1,2091,2090,2055,-1,2055,2056,2091,-1,2092,2091,2056,-1,2056,2057,2092,-1,2093,2092,2057,-1,2057,2058,2093,-1,2094,2093,2058,-1,2058,2059,2094,-1,2095,2094,2059,-1,2059,2060,2095,-1,2096,2095,2060,-1,2060,2061,2096,-1,2097,2096,2061,-1,2061,2062,2097,-1,2098,2097,2062,-1,2062,2063,2098,-1,2099,2098,2063,-1,2063,2064,2099,-1,2100,2099,2064,-1,2064,2065,2100,-1,2101,2100,2065,-1,2065,2066,2101,-1,2102,2101,2066,-1,2066,2067,2102,-1,2103,2102,2067,-1,2067,2068,2103,-1,2104,2103,2068,-1,2068,2069,2104,-1,2071,2072,2105,-1,2106,2105,2072,-1,2072,2073,2106,-1,2107,2106,2073,-1,2073,2074,2107,-1,2108,2107,2074,-1,2074,2075,2108,-1,2109,2108,2075,-1,2075,2076,2109,-1,2110,2109,2076,-1,2076,2077,2110,-1,2111,2110,2077,-1,2077,2078,2111,-1,2112,2111,2078,-1,2078,2079,2112,-1,2113,2112,2079,-1,2079,2080,2113,-1,2114,2113,2080,-1,2080,2081,2114,-1,2115,2114,2081,-1,2081,2082,2115,-1,2116,2115,2082,-1,2082,2083,2116,-1,2117,2116,2083,-1,2083,2084,2117,-1,2118,2117,2084,-1,2084,2085,2118,-1,2119,2118,2085,-1,2085,2086,2119,-1,2120,2119,2086,-1,2086,2087,2120,-1,2121,2120,2087,-1,2087,2088,2121,-1,2122,2121,2088,-1,2088,2089,2122,-1,2123,2122,2089,-1,2089,2090,2123,-1,2124,2123,2090,-1,2090,2091,2124,-1,2125,2124,2091,-1,2091,2092,2125,-1,2126,2125,2092,-1,2092,2093,2126,-1,2127,2126,2093,-1,2093,2094,2127,-1,2128,2127,2094,-1,2094,2095,2128,-1,2129,2128,2095,-1,2095,2096,2129,-1,2130,2129,2096,-1,2096,2097,2130,-1,2131,2130,2097,-1,2097,2098,2131,-1,2132,2131,2098,-1,2098,2099,2132,-1,2133,2132,2099,-1,2099,2100,2133,-1,2134,2133,2100,-1,2100,2101,2134,-1,2135,2134,2101,-1,2101,2102,2135,-1,2136,2135,2102,-1,2102,2103,2136,-1,2137,2136,2103,-1,2103,2104,2137,-1,2138,2139,2105,-1,2105,2106,2138,-1,2140,2138,2106,-1,2106,2107,2140,-1,2141,2140,2107,-1,2107,2108,2141,-1,2142,2141,2108,-1,2108,2109,2142,-1,2143,2142,2109,-1,2109,2110,2143,-1,2144,2143,2110,-1,2110,2111,2144,-1,2145,2144,2111,-1,2111,2112,2145,-1,2146,2145,2112,-1,2112,2113,2146,-1,2147,2146,2113,-1,2113,2114,2147,-1,2148,2147,2114,-1,2114,2115,2148,-1,2149,2148,2115,-1,2115,2116,2149,-1,2150,2149,2116,-1,2116,2117,2150,-1,2151,2150,2117,-1,2117,2118,2151,-1,2152,2151,2118,-1,2118,2119,2152,-1,2153,2152,2119,-1,2119,2120,2153,-1,2154,2153,2120,-1,2120,2121,2154,-1,2155,2154,2121,-1,2121,2122,2155,-1,2156,2155,2122,-1,2122,2123,2156,-1,2157,2156,2123,-1,2123,2124,2157,-1,2158,2157,2124,-1,2124,2125,2158,-1,2159,2158,2125,-1,2125,2126,2159,-1,2160,2159,2126,-1,2126,2127,2160,-1,2161,2160,2127,-1,2127,2128,2161,-1,2162,2161,2128,-1,2128,2129,2162,-1,2163,2162,2129,-1,2129,2130,2163,-1,2164,2163,2130,-1,2130,2131,2164,-1,2165,2164,2131,-1,2131,2132,2165,-1,2166,2165,2132,-1,2132,2133,2166,-1,2167,2166,2133,-1,2133,2134,2167,-1,2168,2167,2134,-1,2134,2135,2168,-1,2169,2168,2135,-1,2135,2136,2169,-1,2170,2169,2136,-1,2136,2137,2170,-1,2139,2138,2171,-1,2172,2171,2138,-1,2138,2140,2172,-1,2173,2172,2140,-1,2140,2141,2173,-1,2174,2173,2141,-1,2141,2142,2174,-1,2175,2174,2142,-1,2142,2143,2175,-1,2176,2175,2143,-1,2143,2144,2176,-1,2177,2176,2144,-1,2144,2145,2177,-1,2178,2177,2145,-1,2145,2146,2178,-1,2179,2178,2146,-1,2146,2147,2179,-1,2180,2179,2147,-1,2147,2148,2180,-1,2181,2180,2148,-1,2148,2149,2181,-1,2182,2181,2149,-1,2149,2150,2182,-1,2183,2182,2150,-1,2150,2151,2183,-1,2184,2183,2151,-1,2151,2152,2184,-1,2185,2184,2152,-1,2152,2153,2185,-1,2186,2185,2153,-1,2153,2154,2186,-1,2187,2186,2154,-1,2154,2155,2187,-1,2188,2187,2155,-1,2155,2156,2188,-1,2189,2188,2156,-1,2156,2157,2189,-1,2190,2189,2157,-1,2157,2158,2190,-1,2191,2190,2158,-1,2158,2159,2191,-1,2192,2191,2159,-1,2159,2160,2192,-1,2193,2192,2160,-1,2160,2161,2193,-1,2194,2193,2161,-1,2161,2162,2194,-1,2195,2194,2162,-1,2162,2163,2195,-1,2196,2195,2163,-1,2163,2164,2196,-1,2197,2196,2164,-1,2164,2165,2197,-1,2198,2197,2165,-1,2165,2166,2198,-1,2199,2198,2166,-1,2166,2167,2199,-1,2200,2199,2167,-1,2167,2168,2200,-1,2201,2200,2168,-1,2168,2169,2201,-1,2202,2201,2169,-1,2169,2170,2202,-1,2203,2202,2170,-1,2204,2205,2171,-1,2171,2172,2204,-1,2206,2204,2172,-1,2172,2173,2206,-1,2207,2206,2173,-1,2173,2174,2207,-1,2208,2207,2174,-1,2174,2175,2208,-1,2176,2177,2209,-1,2210,2209,2177,-1,2177,2178,2210,-1,2211,2210,2178,-1,2178,2179,2211,-1,2212,2211,2179,-1,2179,2180,2212,-1,2213,2212,2180,-1,2180,2181,2213,-1,2214,2213,2181,-1,2181,2182,2214,-1,2215,2214,2182,-1,2182,2183,2215,-1,2216,2215,2183,-1,2183,2184,2216,-1,2217,2216,2184,-1,2184,2185,2217,-1,2218,2217,2185,-1,2185,2186,2218,-1,2219,2218,2186,-1,2186,2187,2219,-1,2220,2219,2187,-1,2187,2188,2220,-1,2221,2220,2188,-1,2188,2189,2221,-1,2222,2221,2189,-1,2189,2190,2222,-1,2223,2222,2190,-1,2190,2191,2223,-1,2224,2223,2191,-1,2191,2192,2224,-1,2225,2224,2192,-1,2192,2193,2225,-1,2226,2225,2193,-1,2193,2194,2226,-1,2227,2226,2194,-1,2194,2195,2227,-1,2228,2227,2195,-1,2195,2196,2228,-1,2229,2228,2196,-1,2196,2197,2229,-1,2230,2229,2197,-1,2197,2198,2230,-1,2231,2230,2198,-1,2198,2199,2231,-1,2232,2231,2199,-1,2199,2200,2232,-1,2233,2232,2200,-1,2200,2201,2233,-1,2234,2233,2201,-1,2201,2202,2234,-1,2235,2234,2202,-1,2202,2203,2235,-1,2205,2204,2236,-1,2237,2236,2204,-1,2204,2206,2237,-1,2238,2237,2206,-1,2206,2207,2238,-1,2239,2238,2207,-1,2207,2208,2239,-1,2210,2211,2240,-1,2241,2240,2211,-1,2211,2212,2241,-1,2242,2241,2212,-1,2212,2213,2242,-1,2243,2242,2213,-1,2213,2214,2243,-1,2244,2243,2214,-1,2214,2215,2244,-1,2245,2244,2215,-1,2215,2216,2245,-1,2246,2245,2216,-1,2216,2217,2246,-1,2247,2246,2217,-1,2217,2218,2247,-1,2248,2247,2218,-1,2218,2219,2248,-1,2249,2248,2219,-1,2219,2220,2249,-1,2250,2249,2220,-1,2220,2221,2250,-1,2251,2250,2221,-1,2221,2222,2251,-1,2252,2251,2222,-1,2222,2223,2252,-1,2253,2252,2223,-1,2223,2224,2253,-1,2254,2253,2224,-1,2224,2225,2254,-1,2255,2254,2225,-1,2225,2226,2255,-1,2256,2255,2226,-1,2226,2227,2256,-1,2257,2256,2227,-1,2227,2228,2257,-1,2258,2257,2228,-1,2228,2229,2258,-1,2259,2258,2229,-1,2229,2230,2259,-1,2260,2259,2230,-1,2230,2231,2260,-1,2261,2260,2231,-1,2231,2232,2261,-1,2262,2261,2232,-1,2232,2233,2262,-1,2263,2262,2233,-1,2233,2234,2263,-1,2264,2263,2234,-1,2234,2235,2264,-1])
IndexedFaceSet517.setCreaseAngle(1.57)
IndexedFaceSet517.setSolid(False)
Coordinate518 = Coordinate()
Coordinate518.setPoint([110.572,-39.5036,63.5633,106.325,-40.8309,58.5202,108.187,-42.0738,68.6372,112.39,-40.7534,73.5916,114.872,-38.2579,68.3271,116.727,-40.2621,75.6672,119.083,-37.5411,71.2134,120.79,-40.0419,76.7704,122.976,-36.3295,75.8227,49.4739,-36.7337,54.0405,44.9053,-36.9436,52.9487,47.0875,-41.2803,52.3002,51.6517,-41.0797,53.3464,54.0251,-36.6217,54.7837,56.1936,-41.1026,53.6043,58.5731,-36.742,54.6979,60.7671,-41.2593,53.3948,63.1262,-37.0551,53.9256,65.3114,-41.6834,52.241,67.6892,-37.5792,52.4017,108.812,-38.4447,52.6248,104.629,-39.9357,46.9408,113.009,-36.9744,58.2404,117.32,-35.4994,63.8891,121.751,-34.2563,68.7247,127.094,-34.7886,67.3228,19.4995,-35.4864,41.4987,14.7492,-36.2581,38.3624,16.9977,-40.123,39.5552,21.7292,-39.3508,42.6525,24.1908,-34.8339,44.2024,26.3976,-38.8179,44.8923,28.8532,-34.3126,46.4306,31.0404,-38.3215,47.0026,33.4872,-33.8162,48.5701,35.6692,-37.9,48.8467,38.1231,-33.3001,50.7836,40.2904,-37.4634,50.7476,42.7273,-32.7893,52.9791,47.3156,-32.3497,54.9181,51.8583,-32.0849,56.2233,56.3916,-32.0749,56.6063,60.929,-32.3333,56.0193,65.4804,-32.8035,54.668,70.0369,-33.4212,52.7852,72.2633,-38.2466,50.3689,74.6205,-34.1361,50.5553,76.8513,-38.9674,48.1491,79.2225,-34.9001,48.1518,81.4707,-39.5858,46.3013,83.8409,-35.7028,45.6125,86.1101,-40.4142,43.7068,88.4796,-36.5642,42.8648,90.7515,-41.3195,40.8399,93.1722,-37.5313,39.7413,106.879,-36.8596,43.3197,102.618,-40.0994,31.2086,111.257,-35.7307,47.7849,115.562,-34.0273,54.3321,119.862,-32.5291,60.1382,124.69,-32.1918,61.7961,129.225,-33.7012,56.7043,143.091,-34.5745,54.7703,139.368,-35.2517,52.0207,141.648,-38.2619,56.191,145.414,-38.0217,57.3333,146.822,-33.8088,57.8632,12.5127,-32.5919,36.4326,7.91179,-34.3528,29.6224,10.0386,-37.3138,34.1979,17.264,-31.6381,40.2802,21.9764,-30.9098,43.2987,26.647,-30.3075,45.8545,31.2992,-29.7495,48.2485,35.9351,-29.1496,50.7986,40.5593,-28.5351,53.4043,45.1506,-27.9584,55.8719,49.7091,-27.4956,57.9212,54.2406,-27.2847,59.0461,58.768,-27.4011,58.9708,63.2904,-27.8427,57.7025,67.8336,-28.4902,55.6822,72.3966,-29.2472,53.2643,76.9826,-30.0888,50.5405,81.587,-30.9629,47.7013,86.2081,-31.831,44.8889,90.8715,-32.7496,41.8972,95.564,-33.8211,38.3492,97.8755,-38.7426,35.7357,100.317,-35.121,33.9697,105.036,-36.8423,28.0399,109.382,-34.1455,38.3234,113.726,-32.291,45.5136,118.056,-30.7563,51.5299,122.358,-29.682,55.8526,126.976,-30.2155,54.2963,131.604,-30.0857,55.1871,133.601,-33.2101,58.8702,136.152,-30.4724,54.1684,140.886,-31.2531,51.7232,144.73,-30.6307,54.3436,10.255,-28.9613,34.3422,6.14426,-29.7916,30.9397,15.0172,-27.8403,38.8657,19.7619,-27.0076,42.3153,24.4438,-26.3259,45.2009,29.1325,-25.6186,48.1845,33.7715,-24.8951,51.2288,38.4034,-24.1405,54.3906,42.9998,-23.4101,57.4628,47.5628,-22.8029,60.0764,52.0951,-22.4175,61.8649,56.6082,-22.3594,62.4352,61.1168,-22.6729,61.6246,65.6185,-23.2687,59.7649,70.1692,-24.1128,56.9868,74.7265,-25.0562,53.8429,79.318,-26.0433,50.5418,83.9446,-27.0204,47.2837,88.5852,-27.962,44.162,93.2695,-28.9745,40.783,97.9823,-30.1411,36.835,102.763,-31.5582,31.963,107.402,-30.9512,34.6236,111.835,-29.7678,39.4148,116.13,-28.4446,44.7154,120.456,-27.2176,49.6645,124.866,-26.636,52.2196,129.402,-26.5722,52.8605,134.008,-26.929,51.9433,138.77,-27.7543,49.2987,143.674,-28.1464,48.2951,8.00089,-25.3607,32.1078,3.46991,-26.5874,27.1358,12.7614,-24.1255,37.1244,17.5394,-23.1498,41.1625,22.2482,-22.356,44.5119,26.9329,-21.551,47.9042,31.6017,-20.6906,51.5072,36.2541,-19.741,55.4486,40.8573,-18.8716,59.0866,45.4267,-18.1184,62.2862,49.9687,-17.5503,64.7873,54.4725,-17.3336,65.9623,58.9609,-17.4882,65.7371,63.4589,-17.9174,64.4791,67.9591,-18.6805,61.9633,72.5069,-19.6741,58.5843,77.0758,-20.8506,54.5195,81.6662,-22.03,50.4482,86.3083,-23.1182,46.7284,90.9586,-24.1397,43.2639,95.6665,-25.2496,39.474,100.411,-26.5564,34.9467,105.202,-28.106,29.5088,109.965,-27.4803,32.2901,114.263,-25.8881,38.6761,118.503,-24.669,43.6492,122.906,-23.9136,46.8911,127.413,-23.6492,48.2923,132.02,-23.8898,47.7983,136.673,-24.3378,46.5281,141.701,-25.3499,43.174,-7.71807,-24.4978,18.3579,-12.6519,-27.4342,6.77402,-9.73315,-29.7263,14.3553,-5.55076,-27.2476,23.9857,-2.94735,-21.4853,30.2354,-0.8385,-24.1124,36.1717,1.51927,-20.6188,33.887,5.87422,-21.4913,30.8729,10.4978,-20.4341,35.2709,15.2988,-19.3356,39.8353,20.0358,-18.4015,43.7691,24.7558,-17.4848,47.6374,29.4415,-16.4739,51.8664,34.1097,-15.4118,56.2929,38.7235,-14.4073,60.4976,43.3127,-13.493,64.3578,47.8592,-12.7875,67.418,52.3559,-12.3725,69.3659,56.8268,-12.3086,69.9708,61.2967,-12.5846,69.2776,65.7681,-13.2222,67.2037,70.2721,-14.1622,63.9781,74.8126,-15.3262,59.9005,79.4097,-16.6515,55.2136,84.0243,-17.9842,50.5029,88.6763,-19.2293,46.1329,93.3399,-20.3863,42.1043,98.0608,-21.6089,37.8318,102.85,-23.0421,32.7625,107.637,-24.7835,26.5149,112.455,-25.886,22.7194,116.65,-22.4024,36.4276,120.984,-21.4239,40.5572,125.427,-20.8502,43.1516,130.011,-20.8239,43.6675,134.645,-21.1103,42.9935,139.285,-21.5469,41.7459,145.264,-22.7844,37.6334,-8.54312,-23.863,15.3949,-5.25939,-19.6569,21.0526,-0.955781,-18.1007,27.399,3.42121,-17.9215,28.4506,8.20627,-16.7976,33.1762,13.0495,-15.5617,38.3404,17.8202,-14.51,42.787,22.5648,-13.4981,47.0796,27.2733,-12.3908,51.7425,31.959,-11.1952,56.749,36.61,-10.0236,61.6617,41.2115,-8.87724,66.4759,45.7519,-7.93084,70.5123,50.2592,-7.28793,73.3707,54.7029,-7.02206,74.7642,59.166,-7.12843,74.7174,63.6159,-7.5701,73.3713,68.0838,-8.41613,70.4604,72.5899,-9.62114,66.1628,77.1302,-11.0291,61.083,81.7304,-12.5533,55.5603,86.3527,-14.0113,50.2988,91.0317,-15.3709,45.4266,95.7286,-16.6331,40.937,100.476,-17.9809,36.1222,105.302,-19.6029,30.253,110.214,-21.3458,23.9259,114.672,-20.5219,27.5031,119.039,-18.9547,33.9939,123.476,-18.1565,37.4919,128.005,-17.7768,39.378,132.591,-17.8873,39.3686,137.168,-18.1195,38.887,142.003,-16.9638,43.8497,-3.68544,-14.5125,24.9983,1.21701,-14.4091,25.7699,5.89188,-13.2375,30.746,10.7922,-11.8514,36.5775,15.5965,-10.6651,41.6187,20.3609,-9.55212,46.3705,25.1104,-8.36804,51.4032,29.819,-7.0057,57.1374,34.4851,-5.59116,63.0761,39.1072,-4.25517,68.7046,43.6524,-3.05274,73.8043,48.1801,-2.12725,77.8151,52.6345,-1.63164,80.1313,57.054,-1.4721,81.1251,61.4642,-1.74431,80.4221,65.9121,-2.42227,78.128,70.3546,-3.53388,74.1301,74.8655,-5.11838,68.2801,79.4306,-6.75842,62.2185,84.0647,-8.46942,55.8868,88.7226,-10.1214,49.792,93.3963,-11.5747,44.482,98.1276,-12.9561,39.4634,102.913,-14.4538,33.9943,107.785,-16.2201,27.4792,112.686,-17.836,21.561,116.99,-16.7067,26.3908,121.532,-15.6004,31.1599,125.983,-14.8609,34.4773,130.538,-14.7702,35.2529,135.144,-15.004,34.7583,140.038,-15.2618,34.2096,144.792,-13.1872,42.8721,-1.12865,-9.93023,26.8972,3.57809,-9.65175,28.374,8.51495,-8.17098,34.6694,13.3669,-6.86141,40.2775,18.1628,-5.64567,45.5092,22.9266,-4.36254,51.0098,27.6637,-2.8617,57.38,32.368,-1.26919,64.1156,36.9968,0.348734,70.9496,41.5983,1.83436,77.255,46.1111,2.97753,82.1894,50.5972,3.79481,85.8233,54.9749,4.37362,88.5001,59.3688,4.33273,88.7069,63.7735,3.75282,86.7662,68.1626,2.82321,83.4315,72.6416,1.29156,77.7043,77.1219,-0.579337,70.6262,81.741,-2.57362,63.0701,86.3749,-4.42631,56.0828,91.0537,-6.21678,49.3501,95.7915,-7.82459,43.3547,100.543,-9.31855,37.8171,105.36,-10.964,31.6835,110.296,-12.9744,24.1067,115.235,-15.106,16.0475,120.099,-15.2101,16.0818,124.014,-12.1169,28.7849,128.571,-11.7881,30.5203,133.163,-11.9255,30.3981,137.758,-12.6024,28.1218,142.984,-12.7103,28.2085,1.30922,-6.16857,25.5445,-3.52062,-7.13678,21.2416,6.23329,-4.512,32.6444,11.1305,-3.07439,38.8552,15.9563,-1.74036,44.6435,20.7568,-0.325952,50.7576,25.5295,1.2712,57.6116,30.2661,3.10465,65.422,34.9481,4.93318,73.2103,39.6811,7.27051,83.0635,44.1316,8.64831,89.0139,48.5532,9.78417,93.9843,52.8186,11.4376,101.041,57.297,10.6062,98.054,61.6651,10.3708,97.4753,66.0486,9.78431,95.4791,70.3958,8.66184,91.3127,74.8588,6.92759,84.6822,79.4222,4.04632,73.4196,84.0249,1.71517,64.3898,88.7056,-0.374595,56.3467,93.3952,-2.3536,48.7547,98.1517,-4.03425,42.3795,102.956,-5.7235,35.9763,107.836,-7.5618,28.979,112.821,-9.89677,19.9824,117.805,-11.6408,13.3815,122.092,-9.62435,21.9434,126.555,-8.79964,25.6993,131.16,-8.88585,25.7809,135.882,-9.6956,22.9446,140.555,-12.4226,12.3371,-1.17733,-3.17319,20.64,-6.07234,-4.60055,14.3794,3.92279,-0.973791,30.087,8.88419,0.684313,37.2996,13.7416,2.09582,43.4934,18.5863,3.65421,50.2913,23.3804,5.43266,57.9921,28.1658,7.42853,66.5868,32.9639,9.82084,76.8125,37.6987,12.3483,87.5905,42.4245,14.2788,95.9178,46.7809,15.5266,101.415,50.9713,16.1115,104.178,55.2762,16.4978,106.136,59.6146,16.2878,105.649,63.9328,16.1016,105.261,68.3692,15.3205,102.441,72.7298,14.4497,99.2499,77.433,13.3918,95.3283,82.4495,11.7634,89.1137,86.2958,5.96914,65.629,91.0134,3.66028,56.5718,95.7466,1.5262,48.2361,100.542,-0.327142,41.0619,105.387,-2.169,33.9417,110.326,-4.33945,25.4825,115.386,-6.70251,16.2463,120.486,-8.3413,9.99475,124.568,-6.09111,19.6181,129.146,-5.83339,21.1092,133.815,-6.51707,18.74,138.339,-7.25077,16.151,142.587,-8.71192,10.562,-3.74977,0.342919,17.7892,1.54779,2.38251,26.7163,6.61734,4.39013,35.5014,11.5392,6.01489,42.6809,16.4144,7.66969,49.984,21.2643,9.63019,58.5618,26.0955,11.8571,68.2503,30.9003,14.5419,79.8479,35.6277,17.138,91.0706,40.1475,19.1054,99.6585,44.5293,19.9158,103.414,48.9027,20.4218,105.902,53.2229,20.6576,107.261,57.5373,20.6801,107.733,61.8361,20.5616,107.618,66.1407,20.2575,106.732,70.4736,19.7351,104.941,74.8595,18.7386,101.181,79.4655,17.3478,95.8009,84.4318,15.4761,88.4661,88.9646,12.4615,76.3112,93.3211,7.65791,56.6736,98.1051,5.35091,47.4983,102.951,3.31622,39.4667,107.85,1.24143,31.2746,112.886,-1.32317,21.0559,118.051,-3.72909,11.5149,122.65,-3.58626,12.5445,127.125,-2.89678,15.8436,131.845,-3.49884,13.7826,136.467,-4.46249,10.2033,141.155,-4.66377,9.81553,-1.0066,5.10696,20.5822,-4.16645,5.24656,16.4992,4.33545,8.0485,33.4726,9.33046,9.85031,41.5147,14.2382,11.7417,49.9323,19.1854,13.9722,59.7881,24.1282,16.7894,72.1287,28.9369,19.149,82.5233,33.5424,21.8203,94.2253,38.0773,23.0185,99.6862,42.461,23.742,103.13,46.8234,24.1992,105.447,51.1463,24.5236,107.2,55.4721,24.6766,108.231,59.7745,24.5771,108.194,64.075,24.3876,107.777,68.3874,24.0266,106.639,72.7109,23.3968,104.366,77.0604,22.5056,100.992,81.5589,21.0575,95.2782,86.2192,18.8921,86.5488,90.822,15.578,72.9521,95.6156,11.8937,57.8101,100.442,9.31299,47.3428,105.351,6.9477,37.7972,110.344,4.4845,27.8475,115.59,0.986057,13.5434,120.678,-0.989185,5.67189,125.157,-0.0983138,9.87051,129.794,-0.270512,9.58654,134.3,-0.407656,9.4442,138.822,-2.46312,1.17917,-3.29671,9.29064,20.5808,-8.61272,6.24572,7.04446,2.03456,11.5464,30.7154,7.08924,13.7408,40.5736,12.2331,16.2668,51.8621,17.3196,19.414,65.8187,22.2668,22.0545,77.5874,26.962,24.6277,89.0519,31.5219,25.7861,94.4252,35.9506,26.6979,98.7317,40.3623,27.3552,101.945,44.7273,27.7868,104.186,49.0666,28.1044,105.938,53.4119,28.3175,107.242,57.6953,28.3867,107.927,61.9974,28.254,107.747,66.3147,27.9629,106.89,70.637,27.4673,105.158,74.9671,26.7792,102.601,79.3404,25.9543,99.4633,83.7729,24.7136,94.5467,88.2306,22.7684,86.6085,92.9578,19.6858,73.8127,97.863,16.5462,60.7917,102.817,13.1964,46.8734,107.794,10.4791,35.6765,112.925,7.29628,22.4965,118.727,1.42522,-2.16316,123.201,2.63266,3.45628,127.752,2.93198,5.18205,132.318,3.34326,7.39344,135.64,0.833802,1.49006,-5.93276,12.0602,14.4069,-0.228117,15.6324,30.471,4.8658,17.4867,38.9979,10.2966,21.237,55.9311,15.2402,25.6763,75.639,20.2544,26.7954,80.9433,24.8828,28.4779,88.6918,29.3801,29.4644,93.3942,33.8424,30.2444,97.1936,38.2613,30.919,100.532,42.6228,31.3144,102.649,46.9754,31.566,104.14,51.3229,31.7732,105.439,55.6149,31.8694,106.251,59.931,31.813,106.401,64.2376,31.6138,105.93,68.5366,31.2473,104.73,72.8753,30.7389,102.917,77.2338,30.0669,100.394,81.6051,29.2729,97.3426,86.0493,28.1792,92.9928,90.5043,26.9662,88.1254,94.9714,25.6035,82.6072,99.9859,21.4209,64.8463,105.111,17.1341,46.6424,110.235,13.7801,32.5095,115.85,8.70823,10.9327,121.203,5.26776,-3.55015,125.692,6.01936,0.1663,129.966,6.13991,1.10591,135.657,5.76625,0.0664419,-2.69018,18.5371,24.9892,-4.64274,17.0454,18.2243,2.63538,21.2232,37.3559,8.96709,24.5196,52.5079,13.3842,29.7317,76.006,18.2061,31.3088,83.4187,22.7876,32.3857,88.5997,27.2939,33.2301,92.7465,31.7541,33.9132,96.1757,36.1733,34.5325,99.3206,40.5472,34.9752,101.681,44.9119,35.2692,103.384,49.2345,35.3808,104.277,53.5382,35.3675,104.616,57.8332,35.3806,105.074,62.1413,35.2727,104.998,66.4581,34.9906,104.154,70.7735,34.6283,102.956,75.1078,34.1549,101.269,79.4825,33.529,98.9135,83.8671,32.6969,95.6465,88.322,31.7024,91.6689,92.76,30.6053,87.2367,97.3106,29.2635,81.7334,100.942,25.4595,65.2655,107.216,20.8616,45.4776,113.173,13.8977,15.224,119.201,7.7228,-11.5448,123.626,8.94069,-5.71377,127.924,9.28241,-3.77861,-5.30528,20.5389,15.2767,0.320356,25.458,37.9315,6.08285,31.6876,66.4997,11.4384,34.1775,78.1677,16.169,35.4458,84.3023,20.717,36.3141,88.6241,25.2171,37.0493,92.3442,29.6724,37.6646,95.522,34.0879,38.2609,98.6132,38.4684,38.8027,101.458,42.8247,39.1699,103.515,47.179,39.3638,104.794,51.492,39.4795,105.72,55.7584,39.3815,105.682,60.0788,39.2819,105.642,64.3854,39.0751,105.121,68.6844,38.7873,104.236,73.0132,38.4117,102.961,77.3582,37.8839,101.004,81.7264,37.1381,98.0707,86.1282,36.2641,94.565,90.5688,35.3661,90.9573,95.0449,34.4283,87.1755,99.5526,33.3587,82.805,103.158,28.5181,61.4205,109.014,24.4604,43.7021,115.648,17.8617,14.74,121.734,11.4105,-13.763,125.749,12.6266,-7.89406,129.5,13.0356,-5.65537,3.99023,35.4678,65.5081,9.42282,38.3539,79.1862,14.0823,39.4115,84.4516,18.6532,40.3202,89.0302,23.1548,41.0016,92.5642,27.5841,41.4839,95.1833,31.9991,42.0303,98.0958,36.4042,42.6383,101.29,40.7686,43.1439,104.014,45.1088,43.5728,106.387,49.4703,43.8764,108.19,53.7435,43.9084,108.745,58.0113,43.8158,108.731,62.3057,43.5967,108.143,66.6094,43.3031,107.216,70.8888,42.9292,105.922,75.2384,42.3397,103.651,79.5772,41.631,100.835,83.9559,40.8053,97.4898,88.3724,39.9129,93.8451,92.784,39.1178,90.6457,97.2556,38.39,87.7622,101.782,37.4102,83.7338,106.512,35.5285,75.6039,112.421,26.9444,37.263,117.869,23.5085,22.1989,122.889,18.5282,3.60639,126.518,13.0914,-12.1242,7.37362,42.352,79.4316,2.19878,40.3187,69.5105,12.0018,43.3533,84.5195,16.5811,44.2673,89.1988,21.1048,44.9937,93.0018,25.5237,45.4256,95.4285,29.8966,45.762,97.4092,34.3127,46.262,100.154,38.7097,46.8777,103.437,43.0643,47.4799,106.655,47.404,48.008,109.528,51.7313,48.357,111.569,56.0518,48.3494,111.954,60.2627,48.1711,111.537,64.5106,47.8939,110.666,68.8026,47.5002,109.258,73.1029,46.9149,106.963,77.4485,46.1002,103.608,81.8189,45.2616,100.146,86.2087,44.3955,96.5587,90.6069,43.6421,93.4979,95.0142,43.0814,91.3349,99.4824,42.3759,88.5074,103.985,41.3438,84.1661,108.688,39.6671,76.852,114.348,34.2913,52.7381,118.443,26.4376,21.6952,5.28968,46.2583,79.2725,0.496454,44.422,70.1346,9.91772,47.2491,84.397,14.4888,48.1175,88.9384,19.0205,48.9332,93.2277,23.4771,49.4657,96.1733,27.8473,49.638,97.4109,32.2163,49.7985,98.5932,36.6016,50.3603,101.675,41.006,51.0742,105.478,45.3691,51.6292,108.527,49.7199,52.0077,110.743,53.9767,52.1449,111.812,58.2201,52.1072,112.055,62.4665,51.9185,111.586,66.7053,51.5894,110.454,71.0233,51.1109,108.626,75.3769,50.3568,105.5,79.718,49.5107,101.941,84.09,48.6339,98.2402,88.4609,47.9952,95.6659,92.8189,47.5832,94.1628,97.2187,47.0575,92.1279,101.685,46.2667,88.849,106.233,45.1093,83.8475,110.941,43.4967,76.7143,115.898,41.286,66.7846,3.18811,50.098,78.8114,-1.81801,47.4884,65.7817,7.8335,51.1109,84.1305,12.4083,51.9234,88.4805,16.9367,52.7001,92.6559,21.4229,53.3553,96.2437,25.8215,53.7506,98.5762,30.1926,53.8325,99.4008,34.6328,53.9813,100.553,39.052,54.6025,103.977,43.3555,55.2375,107.457,47.6394,55.5529,109.401,51.9626,55.7634,110.846,56.1704,55.7732,111.317,60.4134,56.0518,113.084,64.6478,55.7467,112.046,68.8832,55.1745,109.728,73.2429,54.6528,107.665,77.5831,54.0158,105.048,81.8917,53.017,100.692,86.2791,52.3246,97.816,90.6541,52.0855,97.1181,95.0167,51.5921,95.1978,99.4555,50.8199,91.9483,103.946,49.9741,88.3514,108.507,48.7918,83.1465,113.246,47.1915,75.9548,118.671,44.134,61.848,-10.3555,46.4108,40.4618,-14.2059,47.049,38.3833,-13.8611,41.97,38.2208,-7.61112,46.5998,51.4079,-4.40985,50.5301,61.1674,1.04725,53.7216,77.2978,5.74316,54.8991,83.5186,10.3237,55.712,87.9469,14.8386,56.4216,91.8657,19.3242,57.1211,95.7323,23.7671,57.6908,98.9614,28.1561,58.06,101.207,32.5726,58.2025,102.346,36.9159,58.6026,104.74,41.2912,59.2026,108.115,45.5375,59.6356,110.664,49.881,59.9184,112.487,54.1531,60.158,114.094,58.3906,60.288,115.164,62.6692,60.3005,115.664,66.8359,59.862,113.951,71.1322,59.3207,111.75,75.4563,58.7152,109.239,79.727,57.9678,106.031,84.1283,57.1066,102.281,88.4882,56.5227,99.8832,92.8511,56.0828,98.1898,97.2655,55.2999,94.8276,101.702,54.5287,91.5257,106.198,53.6306,87.6113,110.795,52.4051,82.1094,115.573,50.6833,74.2031,118.84,50.1673,67.2605,-12.8578,51.6142,46.164,-16.5772,50.9977,37.8302,-6.74855,54.0516,58.8222,-1.21828,57.0954,74.5035,3.61757,58.6269,82.6072,8.22219,59.491,87.3704,12.7505,60.1788,91.2503,17.2427,60.8306,94.9489,21.6931,61.4124,98.2958,26.1232,61.9224,101.284,30.5163,62.3294,103.757,34.8647,62.6373,105.735,39.2063,63.0431,108.2,43.5213,63.5003,110.919,47.8097,63.9488,113.593,52.0953,64.3229,115.897,56.3832,64.4747,117.097,60.6087,64.437,117.35,64.8397,64.247,116.849,69.0738,63.9409,115.771,73.346,63.3565,113.315,77.6292,62.5987,109.999,81.9862,61.798,106.478,86.3199,61.1188,103.56,90.662,60.5131,101.01,95.0809,59.7192,97.5333,99.5069,58.9557,94.2091,103.941,58.2293,91.0711,108.456,57.2498,86.6844,113.11,55.9443,80.6941,117.977,53.9941,71.5235,123.139,51.8577,61.4674,-15.2812,55.0829,43.2657,-22.0613,53.0231,32.413,-9.06552,57.4697,55.894,-3.52937,60.2776,70.6599,1.42037,62.1595,80.6935,6.10999,63.2185,86.536,10.6707,63.9785,90.8542,15.1732,64.6354,94.6454,19.6334,65.1795,97.8618,24.0338,65.6214,100.557,28.427,65.9807,102.833,32.7826,66.2581,104.692,37.1041,66.5438,106.592,41.434,66.9128,108.913,45.7501,67.3672,111.666,50.0445,67.8281,114.451,54.3032,68.1569,116.565,58.5701,68.1341,116.901,62.8054,68.0024,116.685,67.04,67.8197,116.212,71.2925,67.334,114.208,75.562,66.5788,110.844,79.8642,65.8463,107.6,84.2128,65.1903,104.748,88.5547,64.6113,102.285,92.9116,64.0485,99.9075,97.3195,63.3343,96.7701,101.723,62.7072,94.0739,106.177,61.9393,90.6716,110.756,60.8229,85.5208,115.446,59.3702,78.6823,120.357,56.9344,66.8924,123.919,55.9266,57.1185,-17.5056,58.7306,41.2116,-11.4615,60.6578,51.6913,-5.88804,63.5042,66.9283,-0.789315,65.622,78.3718,3.97128,66.8808,85.3577,8.59106,67.7532,90.3386,13.1114,68.4487,94.3999,17.5863,69.0316,97.8764,21.9947,69.4069,100.278,26.3614,69.6879,102.19,30.677,69.8657,103.567,35.0092,70.0325,104.888,39.3436,70.3039,106.75,43.6514,70.6355,108.919,47.9638,71.105,111.8,52.2541,71.5708,114.66,56.4973,71.8118,116.359,60.7285,71.7395,116.443,64.9736,71.5985,116.176,69.2194,71.2526,114.855,73.4961,70.5005,111.446,77.8032,69.7055,107.82,82.1413,69.0693,105.017,86.4565,68.5656,102.894,90.8036,68.0932,100.936,95.1531,67.6176,98.9625,99.5204,67.131,96.9351,103.942,66.4905,94.1217,108.45,65.5678,89.8658,113.063,64.3179,83.9375,117.808,62.6262,75.7485,123.129,59.4122,59.7884,129.049,55.5023,40.3258,-13.9529,63.3109,44.536,-19.8742,57.9236,15.6211,-8.22004,66.782,63.3539,-3.04938,68.9229,75.1365,1.78195,70.4152,83.4847,6.47509,71.4476,89.4048,11.0476,72.2423,94.0661,15.5297,72.8524,97.7512,19.9381,73.2567,100.35,24.3133,73.5111,102.158,28.6302,73.6239,103.22,32.9287,73.6687,103.923,37.2367,73.7748,104.949,41.5426,73.9484,106.33,45.8497,74.2509,108.387,50.157,74.7737,111.6,54.4588,75.2905,114.781,58.6964,75.5739,116.732,62.9215,75.5017,116.818,67.1462,75.2046,115.726,71.4372,74.4057,112.009,75.7409,73.5157,107.818,80.0673,72.8458,104.784,84.3767,72.3955,102.9,88.7104,72.0415,101.524,93.0313,71.7273,100.357,97.3488,71.3743,98.9847,101.729,70.894,96.9536,106.184,70.1722,93.6656,110.714,69.1114,88.6083,115.403,67.6757,81.6042,120.228,65.6977,71.7709,125.863,61.6369,51.1112,131.721,57.1283,28.1271,-21.5105,61.0591,10.3734,-26.7426,59.2666,0.23041,-22.7091,59.4164,8.74164,-16.4047,65.2846,33.5536,-10.5797,69.9983,59.3386,-5.3636,72.1671,71.4971,-0.394823,73.9253,81.4366,4.33238,75.0456,87.9418,8.9573,75.9528,93.2979,13.4628,76.6061,97.2855,17.8829,77.0718,100.263,22.2543,77.3659,102.319,26.5907,77.478,103.398,30.8968,77.4642,103.802,35.213,77.4254,104.074,39.4727,77.432,104.585,43.8724,77.5996,105.968,47.9884,78.1795,109.529,52.4899,78.7573,113.113,56.783,79.3638,116.832,60.7606,80.0322,120.85,64.8568,80.0484,121.397,69.2167,79.2781,117.769,73.7399,77.4346,108.43,78.6143,78.1441,112.788,82.2328,75.0613,96.7092,86.5917,75.9172,101.771,90.927,75.7373,101.299,95.2054,75.5239,100.641,99.5629,75.1257,99.0069,103.957,74.566,96.5138,108.424,73.7228,92.5157,113.032,72.5388,86.714,117.77,70.9443,78.7347,122.865,68.3623,65.5225,128.656,62.5178,34.9779,132.456,59.2068,12.1179,-23.9629,64.6773,7.47392,-30.9863,64.394,5.22013,-19.1738,67.1498,21.4611,-13.3369,72.2662,49.9913,-7.66601,75.4398,67.8993,-2.57297,77.4066,79.1773,2.20499,78.6439,86.4504,6.85655,79.6193,92.2841,11.3698,80.3336,96.6822,15.8312,80.8344,99.9117,20.1953,81.1507,102.128,24.5399,81.336,103.628,28.8513,81.3587,104.24,33.145,81.2841,104.32,37.3963,81.1678,104.171,41.8052,81.179,104.73,46.0394,82.3176,111.41,50.4835,83.1991,116.71,54.8333,83.6203,119.497,59.0221,84.8707,126.779,63.0552,85.3694,129.954,66.6294,85.0631,128.712,71.3825,83.6211,121.504,75.732,82.4448,115.485,80.2331,81.0073,108.178,84.3814,78.1831,93.2845,88.7935,79.6909,101.994,93.1005,79.5282,101.601,97.4126,79.2429,100.543,101.79,78.7802,98.5272,106.211,78.111,95.3929,110.724,77.2131,91.025,115.368,75.8888,84.3518,120.225,73.9756,74.4991,125.81,69.0103,48.2716,131.536,63.6509,19.6071,135.175,61.8104,4.52699,-27.4052,69.876,13.1739,-31.5893,70.0687,13.7322,-21.8733,71.1365,20.7816,-15.9042,74.6954,41.2141,-10.0197,78.7168,64.2067,-4.8397,80.7285,75.9619,0.0499632,82.2243,84.8235,4.73297,83.2272,90.9275,9.28623,83.9973,95.726,13.7603,84.5294,99.1941,18.1466,84.8653,101.565,22.503,85.095,103.343,26.7982,85.1888,104.361,31.0886,85.1566,104.679,35.3682,85.0278,104.46,39.6328,84.8997,104.243,44.1245,86.3776,112.959,48.5784,88.006,122.507,52.2692,89.2161,129.664,57.1201,88.6834,127.256,61.1276,89.5864,132.73,65.3181,89.5416,132.968,69.4355,89.2396,131.772,73.5413,88.2666,126.853,78.009,86.0426,115.037,82.4574,83.2399,100.009,86.7067,82.9642,98.986,90.9806,83.4748,102.303,95.3069,83.202,101.294,99.6415,82.8321,99.7472,104.048,82.3075,97.3517,108.488,81.6001,93.9453,113.032,80.5624,88.7191,117.724,79.1642,81.5109,122.723,76.8648,69.3401,128.236,73.4101,50.8229,134.115,68.5711,24.6629,135.99,68.0608,22.5145,-33.9092,72.5797,4.56904,-37.4103,72.5092,3.7968,-36.1617,69.59,10.5341,-29.6251,73.7137,11.5296,-24.2968,74.8758,18.7218,-18.9667,76.2001,26.8343,-12.4309,81.8972,59.8409,-7.14439,84.0455,72.6135,-2.12543,85.7777,83.0027,2.60928,86.8698,89.7387,7.19425,87.6162,94.5014,11.6644,88.1516,98.0585,16.0706,88.4979,100.538,20.4228,88.7314,102.373,24.77,88.8765,103.707,29.0667,88.9441,104.598,33.328,88.902,104.865,37.5983,88.773,104.64,41.9061,88.8359,105.504,46.3474,90.387,114.801,50.7585,92.274,125.993,54.8798,92.9153,130.109,59.1134,93.1288,131.817,63.2388,93.1986,132.7,67.3435,93.0382,132.279,71.5278,92.611,130.358,75.8077,90.9438,121.436,80.4602,87.5883,103.012,84.706,85.8803,93.8533,88.9214,87.3161,102.472,93.2188,87.0933,101.721,97.5533,86.7277,100.167,101.905,86.2939,98.2285,106.309,85.7527,95.6896,110.766,85.0259,92.1065,115.362,83.8996,86.2813,120.147,82.3373,78.0124,125.293,79.6673,63.5213,130.455,78.6852,58.6003,134.74,75.5987,42.1663,-36.364,75.1775,-4.4262,-32.0925,77.0409,6.87017,-26.9951,78.0174,13.1246,-21.6603,79.23,20.7567,-15.5558,83.0884,43.7622,-9.46434,87.3282,68.955,-4.36448,89.1835,80.2744,0.460563,90.4523,88.1768,5.07531,91.2564,93.3737,9.57887,91.7817,96.9479,13.9658,92.1244,99.4568,18.3287,92.3426,101.243,22.6943,92.5005,102.68,27.0007,92.5413,103.436,31.2896,92.5776,104.164,35.5744,92.5964,104.79,39.8518,92.5437,105.003,44.0938,92.7124,106.489,49.054,95.1731,121.279,53.0252,96.0427,126.774,57.0588,96.4714,129.735,61.215,96.6259,131.127,65.3988,96.5763,131.346,69.5804,96.2466,129.948,73.5481,95.726,127.426,78.0122,93.3454,114.261,82.5517,91.3411,103.216,86.8209,91.1609,102.69,91.1343,90.8951,101.677,95.4563,90.5576,100.25,99.8099,90.1648,98.5084,104.18,89.7189,96.4621,108.592,89.1604,93.7713,113.085,88.359,89.6884,117.716,87.2196,83.6733,122.58,85.4239,73.8992,127.454,84.18,67.3138,132.214,83.5108,64.0327,135.741,83.4443,58.5129,-34.5813,80.2221,1.17953,-40.1967,80.3361,1.24121,-29.5742,81.3565,8.49654,-24.3483,82.3718,15.1166,-18.3418,85.4948,34.314,-11.8682,90.4636,64.2944,-6.63739,92.4826,76.8253,-1.71732,93.9044,85.8032,2.94484,94.7917,91.6034,7.45816,95.3453,95.4208,11.8794,95.7141,98.1399,16.2445,95.9375,99.9955,20.5865,96.0513,101.202,24.8887,96.1264,102.176,29.2031,96.1761,103.001,33.5149,96.2055,103.706,37.8033,96.244,104.462,42.0862,96.295,105.29,46.3747,96.8321,108.981,50.9304,98.4397,119.001,55.0544,99.3899,125.103,59.1951,99.7879,127.955,63.3516,99.9268,129.284,67.5528,99.7394,128.697,71.5857,99.3496,126.9,75.2533,99.1839,126.391,80.4521,95.2889,104.088,84.7756,94.9101,102.388,89.0781,94.6175,101.193,93.399,94.2981,99.8428,97.728,93.9461,98.3011,102.092,93.5623,96.5763,106.461,93.1308,94.5711,110.888,92.5393,91.6305,115.43,91.6581,86.999,120.121,90.3971,80.1496,125.013,88.6797,70.6389,129.779,87.7161,65.551,134.722,86.5225,59.1339,139.465,86.3822,58.9041,-37.0402,84.4055,1.33271,-42.0112,83.9986,-1.74684,-32.105,84.8201,4.45391,-27.1101,85.27,7.78934,-21.9809,86.1577,13.7738,-15.5206,90.6068,41.2962,-9.00861,95.615,72.2442,-3.97583,97.2118,82.4765,0.75435,98.2281,89.1833,5.30943,98.8657,93.5929,9.76911,99.2686,96.5789,14.139,99.5005,98.5267,18.487,99.5977,99.6606,22.8108,99.6648,100.61,27.1059,99.7163,101.463,31.4083,99.7537,102.231,35.7254,99.8375,103.279,40.0033,99.8903,104.136,44.2795,100.023,105.47,48.5349,100.696,110.051,52.8728,101.69,116.571,57.1494,102.718,123.279,61.3594,103.121,126.232,65.506,103.15,126.927,69.6351,102.888,125.869,73.7396,102.101,121.656,76.4534,102.043,121.756,82.705,98.699,102.336,87.0226,98.3103,100.54,91.3399,97.9509,98.9198,95.6737,97.6311,97.5386,99.9962,97.336,96.3038,104.351,96.9679,94.6341,108.745,96.5279,92.5367,113.208,95.8791,89.1929,117.765,94.9912,84.4243,122.592,93.4694,75.8808,127.553,91.5008,64.6666,132.561,89.8028,55.0849,138.1,87.6048,42.4096,141.864,86.3253,28.9043,-39.4858,87.8493,-3.04845,-34.5362,88.4757,1.45322,-29.6952,88.7566,3.81379,-24.7599,89.0207,6.07294,-18.1439,93.617,35.1149,-11.4325,98.6906,67.138,-6.3112,100.448,78.591,-1.49117,101.559,86.0299,3.12953,102.312,91.2516,7.62738,102.785,94.7373,12.0168,103.042,96.8856,16.3673,103.167,98.2195,20.7058,103.233,99.1839,25.0191,103.275,99.9998,29.3161,103.308,100.76,33.6165,103.341,101.517,37.9302,103.424,102.579,42.2145,103.569,104.024,46.52,103.9,106.606,50.7904,104.493,110.791,55.1181,105.396,116.886,59.3336,106.127,121.913,63.5068,106.434,124.334,67.6994,106.259,123.795,71.6648,106.207,123.983,75.4641,104.392,113.353,80.1817,103.17,106.387,84.9493,101.998,99.8517,89.269,101.655,98.2998,93.6036,101.385,97.1913,97.9006,101.097,95.9705,102.27,100.744,94.3583,106.641,100.357,92.5351,111.041,99.8923,90.2415,115.547,99.1841,86.4654,120.182,98.1642,80.793,125.068,96.4613,70.9603,130.008,94.6067,60.2011,135.188,92.5041,47.9519,141.696,87.5988,18.678,144.208,85.889,8.36843,-36.9679,92.2048,-1.1899,-41.7602,92.0899,-2.55807,-32.0622,92.578,1.8123,-27.2334,92.6103,2.65824,-21.247,95.5345,21.9419,-15.0344,99.1976,45.7495,-8.68164,103.581,73.8993,-3.79895,104.783,82.0868,0.887404,105.592,87.7805,5.41664,106.149,91.8777,9.86509,106.465,94.4498,14.2415,106.639,96.1268,18.5763,106.782,97.5984,22.9259,106.919,99.0321,27.2368,106.974,99.9502,31.5364,106.986,100.59,35.8024,106.967,101.038,40.1087,107.033,102.016,44.4364,107.214,103.719,48.7004,107.675,107.168,53.0058,108.344,111.932,57.3307,109.062,116.994,61.5031,109.573,120.743,65.6749,109.645,121.74,69.777,109.508,121.418,74.2088,106.575,103.61,78.6134,106.183,101.727,82.9049,105.707,99.2993,87.2427,105.378,97.8008,91.5679,105.153,96.9501,95.8296,104.889,95.8442,100.177,104.551,94.2883,104.56,104.116,92.1281,108.947,103.698,90.0699,113.412,103.14,87.1469,117.941,102.376,82.9428,122.708,101.12,75.6816,127.784,98.9818,62.929,133.173,96.3077,46.8575,139.376,91.6352,18.3609,143.379,87.0612,7.33496,-39.3323,96.0508,-3.16808,-34.3966,96.4387,0.00274385,-29.5149,96.7212,2.48717,-24.1724,98.0578,11.7998,-18.0386,101.335,33.6364,-11.1072,106.582,68.1794,-6.13752,107.966,77.7279,-1.41882,108.79,83.6535,3.14548,109.359,87.9234,7.62898,109.756,91.0772,12.075,110.095,93.8595,16.497,110.363,96.1772,20.861,110.562,98.0465,25.2111,110.64,99.1319,29.5573,110.655,99.8161,33.8045,110.654,100.386,38.0011,110.545,100.259,42.3305,110.621,101.328,46.6331,110.89,103.624,50.9251,111.367,107.257,55.2269,112.052,112.223,59.461,112.677,116.793,63.6412,112.981,119.296,67.8915,112.733,118.28,71.81,112.377,116.523,76.5664,109.815,100.738,80.8573,109.409,98.7065,85.1625,109.172,97.7552,89.4325,108.928,96.7606,93.714,108.735,96.0862,98.0454,108.456,94.8711,102.446,107.995,92.4931,106.885,107.469,89.7085,111.3,106.956,87.0001,115.799,106.304,83.4073,120.384,105.441,78.4812,125.22,104.085,70.4212,130.792,101.024,51.5431,134.447,96.3222,38.9205,-36.8594,100.089,-3.25774,-41.7995,99.6838,-6.62343,-31.812,100.655,1.16269,-26.9827,100.864,3.22182,-21.0727,103.572,21.6378,-14.8652,107.097,45.5928,-8.49796,111.15,73.1979,-3.73921,111.974,79.2644,0.859097,112.545,83.6532,5.39141,113.007,87.3126,9.8998,113.524,91.336,14.3762,113.941,94.6923,18.7985,114.223,97.1535,23.0972,114.355,98.6184,27.4796,114.374,99.3475,31.7808,114.347,99.7671,36.0156,114.298,100.033,40.2126,114.178,99.8284,44.5264,114.195,100.536,48.8468,114.507,103.175,53.1602,115.096,107.62,57.4154,115.772,112.63,61.6539,116.222,116.158,65.8153,116.229,116.771,70.1311,115.143,110.248,74.0185,114.911,109.26,78.7188,113.072,97.8442,83.0327,112.888,97.2254,87.3708,112.716,96.6831,91.6746,112.602,96.5158,95.9335,112.45,96.0909,100.252,112.092,94.3236,104.696,111.521,91.1783,109.2,110.847,87.3625,113.698,110.132,83.281,118.246,109.397,79.0678,122.91,108.413,73.2429,128.081,107.029,64.8806,-39.3457,103.736,-6.67312,-34.2459,104.366,-1.70168,-29.1496,104.991,3.22396,-24.3899,105.144,4.95087,-17.7536,109.516,35.2307,-11.6653,112.847,58.4222,-6.04359,115.263,75.4103,-1.4204,115.837,79.9224,3.13824,116.279,83.5403,7.71228,116.859,88.0826,12.2743,117.438,92.6205,16.7245,117.883,96.237,21.1091,118.118,98.4392,25.4048,118.22,99.7398,29.7044,118.196,100.19,33.9602,118.059,99.8726,38.2291,117.812,98.8198,42.4442,117.723,98.8232,46.6905,117.717,99.3846,51.0965,118.122,102.713,55.3782,118.884,108.421,59.6487,119.471,112.952,63.775,119.67,114.858,68.0345,119.321,113.114,72.336,117.832,103.735,76.3531,117.276,100.567,80.9729,116.568,96.4576,85.2186,116.605,97.2945,89.5756,116.503,97.2078,93.8428,116.392,97.0482,98.1394,116.181,96.2216,102.502,115.732,93.8071,106.942,114.993,89.4599,111.532,114.132,84.3162,116.092,113.271,79.166,120.676,112.483,74.5052,125.476,111.374,67.723,130.404,110.555,62.9107,-36.7533,107.992,-5.28001,-41.5589,107.763,-7.58175,-31.6743,108.584,-0.452444,-26.6,109.148,4.1764,-20.7207,111.877,24.0046,-14.6717,114.86,45.3211,-8.36696,118.559,71.4383,-3.64683,119.281,77.091,0.929195,119.718,80.768,5.47102,120.153,84.4209,10.0728,120.774,89.3546,14.6705,121.575,95.5294,19.0676,121.99,99.0195,23.3455,121.942,99.3158,27.6367,121.924,99.8206,31.8809,121.836,99.8362,36.1595,121.6,98.843,40.4272,121.365,97.8474,44.6736,121.271,97.8125,48.9167,121.322,98.7802,53.3084,122.027,104.244,57.5478,122.797,110.13,61.778,123.058,112.527,66.0274,122.89,111.983,70.2747,121.747,104.747,74.6334,120.363,95.8711,78.8188,120.162,95.0843,83.0716,120.167,95.7157,87.4291,120.207,96.6059,91.7547,120.114,96.571,96.0404,120.041,96.6693,100.355,119.829,95.8162,104.7,119.471,93.9655,109.277,118.33,86.7743,113.9,117.302,80.3658,118.481,116.514,75.5929,123.137,115.648,70.2928,128.26,113.866,58.7766,130.079,113.669,57.6094,-39.1114,111.822,-7.54859,-34.1652,112.245,-3.80404,-28.9008,113.028,2.50461,-23.4094,114.56,14.1137,-17.1531,118.082,39.8904,-10.7679,121.765,66.6555,-5.88301,122.751,74.328,-1.21523,123.362,79.3284,3.37299,123.786,83.0041,7.91613,124.269,87.09,12.4498,124.833,91.7344,16.8908,125.272,95.491,21.3011,125.422,97.2051,25.5488,125.417,97.807,29.7541,125.353,97.9952,34.049,125.285,98.1558,38.3533,124.991,96.7311,42.5854,124.827,96.208,46.8802,124.881,97.2176,51.1705,125.395,101.466,55.5164,126.092,106.999,59.7628,126.499,110.478,63.9937,126.537,111.364,68.362,126.111,109.009,72.5447,124.81,100.473,76.8281,123.897,94.6861,80.906,123.7,93.894,85.2041,123.693,94.4584,89.8384,123.406,93.1088,94.0038,123.45,94.0081,98.34,123.435,94.5203,102.634,123.034,92.3174,107.049,122.514,89.2887,111.608,121.53,83.0187,116.249,120.717,77.9682,120.831,119.92,73.0062,125.642,118.767,65.5821,131.573,116.586,51.1411,-36.4247,116.383,-3.82058,-40.5371,116.475,-3.85906,-31.0992,117.472,4.87382,-25.6124,118.254,11.3436,-20.2115,120.232,26.4556,-14.0704,123.579,51.4218,-8.20888,126.064,70.3089,-3.41841,126.944,77.397,1.29595,127.661,83.2946,5.8338,128.118,87.2894,10.3215,128.502,90.7509,14.7512,128.863,94.0441,19.1871,129.132,96.6632,23.5322,129.299,98.5342,27.7644,128.835,95.847,31.9869,128.974,97.4979,36.257,128.74,96.4647,40.5012,128.617,96.2296,44.8155,128.638,97.0313,49.026,129.095,100.962,53.4275,129.617,105.38,57.7207,130.074,109.313,61.9544,130.129,110.343,66.1905,129.962,109.776,70.5227,129.391,106.309,74.8092,128.414,99.9192,79.1128,127.639,94.9737,83.2514,127.415,93.9721,87.6476,127.379,94.3557,91.9965,127.051,92.6329,96.2794,126.962,92.6163,100.539,126.931,93.0139,104.93,126.577,91.1038,109.361,125.929,87.0741,113.884,125.218,82.6074,118.48,124.398,77.3662,123.273,123.23,69.6474,129.11,120.457,50.5461,135.132,117.605,30.9071,-38.2715,120.697,-2.47292,-33.869,121.328,2.98541,-28.2074,122.147,9.90239,-23.2023,123.025,17.2153,-17.9964,124.438,28.5075,-10.6505,129.201,64.7947,-5.69345,130.341,74.0076,-0.870901,131.309,81.932,3.82751,132.114,88.6252,8.30025,132.517,92.3224,12.7719,132.814,95.2234,17.2262,133.077,97.8735,21.51,133.069,98.4931,26.599,133.073,99.3277,30.0616,132.794,97.8138,34.2224,132.679,97.6273,38.5208,132.579,97.5596,42.8575,132.938,100.886,47.0951,133.235,103.74,51.2927,133.451,105.984,55.6654,133.808,109.292,59.8836,133.832,110.116,64.1208,133.752,110.173,68.3931,133.587,109.611,72.6253,133.031,106.155,77.1444,132.301,101.458,81.2115,131.352,95.0628,85.5706,131.058,93.5475,90.0263,130.969,93.5615,94.1102,131.038,94.6802,98.2905,131.067,95.5158,102.648,130.854,94.5901,107.081,130.45,92.2663,111.564,129.811,88.2071,116.095,129.088,83.5379,120.819,127.838,74.9996,125.84,126.18,63.5013,132.789,121.579,30.6063,-35.5088,125.26,1.66625,-40.4361,124.996,-1.17505,-30.8874,125.515,4.4018,-25.9137,125.842,7.71098,-20.0491,128.234,26.8367,-13.2057,132.168,57.7162,-8.06945,133.5,68.654,-3.15679,134.614,77.9074,1.63806,135.671,86.7003,6.32399,136.418,93.1331,10.8475,136.84,97.0687,15.2551,137.109,99.8278,19.6407,137.256,101.656,24.2552,137.346,103.083,28.6279,137.549,105.335,32.2323,136.948,101.377,36.8228,137.131,103.493,41.1284,137.072,103.742,45.3421,137.656,108.841,49.4941,137.778,110.425,53.7306,137.704,110.539,57.8651,137.634,110.66,62.093,137.521,110.476,66.3559,137.416,110.346,70.5199,137.352,110.515,74.7075,137.247,110.37,78.9818,136.509,105.443,83.1549,135.894,101.436,87.5338,135.687,100.542,91.9528,135.585,100.445,96.1345,135.252,98.5626,100.337,135.144,98.3785,104.762,134.805,96.4826,109.231,134.224,92.7563,113.704,133.618,88.8449,118.454,132.412,80.4219,123.367,130.832,69.1926,128.657,128.761,54.3079,131.191,126.963,41.1714,-37.5843,129.29,1.05293,-33.9403,128.744,-2.47812,-28.3729,129.369,3.30383,-22.7191,131.206,18.6863,-16.0259,134.851,48.0345,-10.6127,136.53,62.0101,-5.55838,137.724,72.1531,-0.682641,138.814,81.458,4.04846,139.819,90.0775,8.7221,140.582,96.8032,13.2176,140.975,100.617,17.6857,141.205,103.152,22.0293,141.369,105.158,26.2704,141.519,107.032,30.5205,141.811,110.016,34.6994,141.812,110.717,39.0475,141.785,111.223,43.2748,141.763,111.753,47.5058,141.709,112.022,51.6991,141.623,112.038,55.8403,141.481,111.613,60.0511,141.34,111.195,64.288,141.21,110.869,68.5311,141.138,110.994,72.6719,141.139,111.662,76.8715,140.976,111.064,81.0993,140.724,109.772,85.2498,140.508,108.751,89.6191,140.227,107.255,94.0506,139.862,105.115,98.3099,139.513,103.064,102.578,139.085,100.394,107.02,138.538,96.8322,111.442,137.931,92.7967,116.121,136.885,85.3819,120.993,135.359,74.269,126.087,133.527,60.8097,132.125,130.549,38.6,-37.1097,131.919,-10.1436,-32.0255,132.624,-3.58087,-24.9533,135.166,18.1492,-18.3889,138.247,43.6155,-13.1555,139.591,55.2714,-8.05626,140.802,65.8488,-3.08125,141.882,75.3447,1.77705,142.891,84.257,6.49742,143.813,92.443,11.0896,144.488,98.6299,15.6499,144.935,102.987,19.9474,145.126,105.265,24.1839,145.258,107.052,28.4874,145.389,108.839,32.7032,145.449,110.043,36.9892,145.484,111.047,41.2243,145.465,111.617,45.4311,145.409,111.879,49.635,145.378,112.342,53.8348,145.283,112.281,58.0401,145.151,111.932,62.2483,145.028,111.645,66.4791,144.957,111.782,70.6744,144.858,111.681,74.8833,144.702,111.122,79.104,144.528,110.422,83.3209,144.284,109.159,87.5092,144.09,108.285,91.8066,143.831,106.908,96.1456,143.49,104.878,100.532,143.093,102.406,104.932,142.571,98.9402,109.367,141.989,94.9895,113.961,141.04,88.1385,118.712,139.7,78.1807,123.718,138.021,65.5595,128.939,136.061,50.7239,134.113,134.242,37.0007,-26.1463,140.225,26.3282,-20.8352,141.453,37.3925,-15.5244,142.973,50.8505,-10.4665,144.063,60.7193,-5.49384,145.056,69.7794,-0.614534,145.971,78.179,4.13955,146.81,85.9179,8.77219,147.542,92.7683,13.3058,148.092,98.0936,17.7463,148.499,102.23,22.0649,148.725,104.852,26.3691,148.836,106.527,30.6442,148.926,108.028,34.8735,149.013,109.481,39.1725,149.066,110.667,43.3976,149.064,111.386,47.6121,149.056,112.056,51.8252,148.988,112.226,56.0549,148.829,111.646,60.2207,148.702,111.319,64.4365,148.617,111.339,68.7067,148.568,111.653,72.8562,148.459,111.458,77.0973,148.228,110.277,81.2966,148.009,109.178,85.5001,147.783,108.017,89.8049,147.489,106.32,94.1137,147.159,104.317,98.4296,146.828,102.311,102.795,146.382,99.3596,107.196,145.791,95.2201,111.713,145.002,89.4693,116.423,143.875,80.9823,121.302,142.524,70.6763,126.365,140.833,57.6032,131.881,138.625,40.3584,137.269,136.743,25.7694,140.031,132.501,24.0455,143.341,134.182,5.72165,145.686,130.269,7.09483,149.608,131.774,-13.0368,-23.7682,144.467,29.1438,-26.7465,145.297,27.238,-18.0932,146.187,44.745,-12.84,147.433,56.2579,-7.87715,148.337,64.8301,-2.99206,149.196,72.9967,1.77919,149.982,80.5256,6.44679,150.661,87.1358,11.0348,151.219,92.6991,15.5274,151.668,97.3146,19.9129,152.05,101.354,24.2356,152.27,104.009,28.5924,152.406,105.943,32.8466,152.525,107.723,37.112,152.622,109.311,41.3682,152.649,110.31,45.5967,152.671,111.248,49.8033,152.634,111.688,53.998,152.511,111.396,58.2092,152.361,110.864,62.4148,152.276,110.889,66.6473,152.167,110.702,70.8377,152.015,110.148,75.0161,151.885,109.774,79.2766,151.68,108.778,83.5014,151.477,107.781,87.7747,151.221,106.346,92.0552,150.908,104.431,96.3442,150.553,102.153,100.69,150.112,99.152,105.129,149.518,94.881,109.649,148.751,89.1541,114.225,147.851,82.3057,118.963,146.796,74.1757,123.88,145.462,63.7135,129.131,143.681,49.5347,134.475,141.866,35.0832,140.484,139.08,12.5341,147.336,135.945,-12.7844,149.536,135.122,-19.5451,-25.4984,149.15,35.1632,-31.5731,147.347,18.3169,-19.8893,150.301,46.2484,-15.2256,150.882,52.2417,-10.2625,151.724,60.5297,-5.36189,152.488,68.1217,-0.557388,153.244,75.6319,4.14179,153.915,82.374,8.73929,154.458,87.9776,13.2814,154.948,93.1021,17.7395,155.323,97.2167,22.1292,155.612,100.555,26.4752,155.816,103.147,30.7743,155.972,105.312,35.0451,156.099,107.221,39.3064,156.19,108.802,43.5514,156.245,110.06,47.7805,156.206,110.506,51.9886,156.111,110.445,56.1831,155.991,110.171,60.3528,155.87,109.871,64.588,155.754,109.622,68.8098,155.676,109.698,72.9931,155.567,109.501,77.2172,155.407,108.858,81.4624,155.187,107.687,85.7103,154.932,106.215,89.9664,154.643,104.448,94.2778,154.295,102.164,98.6211,153.843,98.9858,103.015,153.285,94.8819,107.516,152.594,89.6418,112.068,151.811,83.6075,116.738,150.905,76.5254,121.509,149.836,68.0279,126.517,148.471,57.0054,131.735,146.782,43.1909,137.777,144.041,20.3747,143.55,142.402,7.09757,148.34,137.229,-13.1026,-28.142,152.335,27.9716,-33.3216,151.15,16.2629,-22.6102,153.535,39.8391,-17.7617,154.123,46.105,-12.6313,155.161,56.4435,-7.71853,155.88,63.8812,-2.91438,156.536,70.7243,1.82557,157.199,77.6094,6.48227,157.773,83.6768,11.0484,158.263,88.9695,15.5467,158.675,93.5503,19.9738,159.003,97.3628,24.3328,159.222,100.172,28.6704,159.408,102.681,32.9659,159.57,104.967,37.2292,159.665,106.631,41.4669,159.723,107.961,45.7261,159.733,108.863,49.9547,159.679,109.181,54.1761,159.581,109.095,58.3722,159.436,108.585,62.5605,159.325,108.363,66.7808,159.223,108.237,70.968,159.114,108.025,75.2023,158.96,107.416,79.4389,158.785,106.621,83.665,158.568,105.444,87.9109,158.292,103.734,92.185,157.985,101.738,96.544,157.548,98.6012,100.937,157.038,94.8036,105.381,156.432,90.1608,109.904,155.728,84.6434,114.531,154.902,78.0414,119.259,153.971,70.5178,124.081,152.952,62.2177,129.123,151.62,51.1516,134.507,149.746,35.2838,139.716,148.675,26.5722,-30.7369,155.594,21.0409,-25.2196,156.868,33.9846,-19.5193,158.134,46.8609,-15.1483,158.431,50.5608,-10.1122,159.305,59.6903,-5.2655,159.956,66.716,-0.50989,160.525,72.9609,4.20135,161.1,79.2399,8.81118,161.603,84.839,13.3381,162.029,89.7036,17.7879,162.366,93.7219,22.1922,162.608,96.8513,26.5326,162.802,99.5109,30.8538,162.975,101.976,35.1209,163.073,103.735,39.3973,163.157,105.357,43.6577,163.197,106.566,47.891,163.2,107.419,52.1073,163.114,107.451,56.2896,162.998,107.185,60.5132,162.876,106.867,64.7509,162.739,106.419,68.9395,162.621,106.121,73.1672,162.489,105.695,77.4193,162.317,104.906,81.6446,162.128,103.946,85.8839,161.878,102.427,90.1797,161.573,100.394,94.5245,161.19,97.6558,98.8841,160.732,94.211,103.301,160.194,90.0419,107.781,159.574,85.1161,112.379,158.831,79.0783,117.045,158.005,72.2754,121.79,157.119,64.923,126.721,156.04,55.8276,131.813,154.795,45.2097,137.303,152.835,28.0627,141.62,153.196,32.1281,-27.8854,159.981,25.6468,-22.6709,160.887,35.4413,-17.6661,161.745,44.7288,-12.5627,162.67,54.6696,-7.71943,163.361,62.3188,-2.9013,163.911,68.5967,1.87539,164.418,74.4542,6.56133,164.976,80.769,11.122,165.425,86.0211,15.6043,165.769,90.2513,20.0252,166.014,93.5212,24.3743,166.199,96.1925,28.7063,166.351,98.5413,33.0286,166.488,100.742,37.3174,166.58,102.5,41.5569,166.638,103.919,45.8233,166.642,104.828,50.0418,166.584,105.124,54.269,166.481,104.981,58.4659,166.382,104.877,62.7133,166.285,104.79,66.9379,166.164,104.469,71.138,166.019,103.906,75.3951,165.848,103.096,79.6369,165.657,102.091,83.876,165.432,100.757,88.1731,165.155,98.931,92.4972,164.799,96.3552,96.8542,164.386,93.2345,101.241,163.922,89.6234,105.693,163.38,85.2859,110.2,162.761,80.207,114.838,161.991,73.7174,119.561,161.14,66.4606,124.399,160.218,58.5385,129.309,159.267,50.3501,134.2,158.173,40.7811,139.329,157.069,31.1698,144.887,156.137,23.2903,-25.7511,163.752,24.3943,-32.4237,162.123,6.91588,-20.1534,164.982,37.7836,-15.0047,166.05,49.4825,-10.0984,166.757,57.5666,-5.27902,167.284,63.8387,-0.4697,167.779,69.7831,4.24464,168.318,76.1473,8.87431,168.832,82.2325,13.4103,169.192,86.7776,17.8597,169.443,90.2222,22.2231,169.627,92.989,26.5752,169.792,95.5536,30.9093,169.928,97.8203,35.2114,170.027,99.7172,39.4855,170.099,101.327,43.7554,170.129,102.521,48.0004,170.098,103.101,52.2272,170.025,103.266,56.4239,169.944,103.335,60.6419,169.864,103.406,64.8991,169.737,103.02,69.1257,169.593,102.455,73.3715,169.417,101.579,77.6199,169.238,100.66,81.855,169.015,99.3024,86.1374,168.754,97.5673,90.4757,168.418,95.1094,94.8013,168.045,92.2713,99.1657,167.631,89.0308,103.595,167.167,85.3052,108.085,166.616,80.7219,112.643,165.959,75.1057,117.343,165.114,67.6655,122.143,164.207,59.6204,126.843,163.499,53.5049,131.855,162.565,45.2245,136.893,161.492,35.5683,142.001,160.06,22.3803,-28.8105,166.578,12.2024,-31.2547,165.82,3.7743,-22.8542,168.184,29.9733,-17.3385,169.464,44.3261,-12.4535,170.175,52.7328,-7.66494,170.667,58.8722,-2.87194,171.118,64.5851,1.92432,171.657,71.1893,6.61103,172.192,77.719,11.175,172.61,83.0212,15.6484,172.888,86.8761,20.0608,173.097,90.0065,24.44,173.269,92.7404,28.784,173.403,95.0745,33.0931,173.514,97.1664,37.4003,173.606,99.0497,41.6843,173.655,100.484,45.9421,173.656,101.426,50.1847,173.597,101.735,54.4113,173.52,101.861,58.6153,173.444,101.973,62.8421,173.332,101.73,67.0816,173.196,101.232,71.3179,173.027,100.387,75.5737,172.853,99.4969,79.8378,172.643,98.2279,84.1254,172.387,96.4892,88.4038,172.095,94.3836,92.7221,171.746,91.6925,97.0968,171.351,88.5348,101.493,170.93,85.1059,105.963,170.431,80.9003,110.498,169.832,75.6775,115.214,169.023,68.3415,119.947,168.096,59.7992,124.693,167.282,52.4035,129.302,166.611,46.4329,134.622,165.686,38.0173,139.491,164.523,27.064,143.91,163.844,20.962,-32.5299,168.76,-7.79535,-26.2604,170.744,14.7085,-19.941,172.673,36.6086,-15.0119,173.418,45.698,-10.1874,173.998,53.0115,-5.33768,174.475,59.2198,-0.48213,174.973,65.6408,4.25881,175.514,72.4956,8.92672,175.999,78.7272,13.437,176.328,83.2622,17.8999,176.571,86.8852,22.2993,176.761,89.918,26.6645,176.913,92.5371,31.0044,177.037,94.8496,35.3071,177.131,96.8229,39.5997,177.201,98.544,43.8881,177.214,99.6505,48.1255,177.183,100.27,52.3652,177.125,100.609,56.5894,177.044,100.688,60.7984,176.943,100.54,65.0166,176.806,100.016,69.2652,176.655,99.3379,73.5475,176.479,98.3949,77.7896,176.289,97.2942,82.064,176.065,95.83,86.3645,175.782,93.7491,90.6728,175.475,91.4046,95.0269,175.112,88.47,99.4083,174.703,85.0506,103.851,174.232,80.9726,108.389,173.665,75.9069,112.998,172.993,69.7292,117.851,171.999,60.2015,122.65,171.053,51.1615,127.721,169.98,40.8348,132.077,169.975,41.6104,137.304,168.667,28.7347,142.525,167.352,15.926,147.147,166.483,7.64018,-29.5665,173.207,-2.73585,-31.3155,173.178,-3.39117,-23.1242,175.417,23.1182,-17.2891,176.864,40.4419,-12.504,177.404,47.5884,-7.73599,177.872,53.9322,-2.95127,178.304,59.8643,1.87921,178.831,66.8329,6.57162,179.344,73.6197,11.1602,179.732,79.0043,15.7125,180.032,83.4107,20.1494,180.255,86.9343,24.5317,180.441,90.034,28.9022,180.577,92.5755,33.2092,180.683,94.7604,37.5011,180.758,96.6039,41.7851,180.792,97.9763,46.045,180.797,99.0257,50.3007,180.742,99.4131,54.5499,180.673,99.6399,58.769,180.59,99.6892,63.01,180.447,99.093,67.2405,180.29,98.3202,71.4786,180.136,97.5839,75.7327,179.953,96.5191,80.0118,179.743,95.1524,84.3083,179.491,93.3366,88.6228,179.201,91.089,92.9505,178.876,88.4599,97.3222,178.488,85.1426,101.743,178.035,81.1174,106.256,177.509,76.2978,110.845,176.866,70.2137,115.663,175.935,61.0075,120.474,174.982,51.5616,125.285,174.047,42.2948,129.995,173.806,40.6025,134.476,173.352,36.5198,140.632,171.116,13.2709,145.016,170.437,6.69944,-31.8502,177.565,0.357677,-25.9106,178.697,14.7957,-20.3627,179.746,28.2057,-14.8941,180.826,41.9392,-9.95122,181.254,48.109,-5.34714,181.659,53.9533,-0.566478,182.138,60.6528,4.21679,182.673,67.9714,8.8584,183.111,74.1534,13.4463,183.445,79.1222,17.9536,183.72,83.4052,22.377,183.926,86.8611,26.7798,184.102,89.9671,31.132,184.228,92.4928,35.4259,184.309,94.4781,39.7072,184.356,96.0632,43.9774,184.363,97.1809,48.2467,184.334,97.8779,52.5024,184.278,98.2686,56.7523,184.2,98.3874,60.9816,184.087,98.108,65.21,183.942,97.4509,69.4263,183.801,96.8291,73.6817,183.622,95.7671,77.9544,183.41,94.3341,82.2338,183.189,92.7952,86.5602,182.92,90.708,90.8857,182.615,88.201,95.2361,182.275,85.2995,99.6491,181.844,81.3684,104.14,181.327,76.4579,108.725,180.694,70.2586,113.411,179.914,62.3867,118.318,178.924,52.1721,123.334,177.837,40.8759,127.988,177.606,39.2184,132.092,177.523,39.1117,-26.3807,183.324,22.3894,-22.6517,183.367,23.9625,-17.628,184.112,34.1918,-12.4949,184.754,43.1943,-7.59962,184.838,45.524,-2.88619,185.567,55.4591,1.80921,185.988,61.7195,6.53963,186.477,68.7785,11.1842,186.855,74.5002,15.7102,187.156,79.2585,20.1958,187.405,83.3923,24.6136,187.593,86.7788,28.9987,187.735,89.5971,33.3256,187.834,91.8935,37.6311,187.893,93.6964,41.8911,187.906,94.9389,46.1629,187.888,95.7999,50.4365,187.848,96.4025,54.6834,187.781,96.6606,58.9323,187.694,96.685,63.1802,187.572,96.2734,67.3926,187.446,95.8058,71.6293,187.281,94.8727,75.8901,187.09,93.6369,80.1903,186.867,92.0136,84.4995,186.616,90.0505,88.8137,186.331,87.6914,93.1783,186.001,84.7824,97.5714,185.61,81.1688,102.028,185.108,76.2412,106.589,184.503,70.1108,111.266,183.774,62.5255,116.136,182.878,53.0077,121.256,181.815,41.5689,126.993,180.475,27.0244,131.674,179.929,21.5474,-24.9203,186.877,18.0153,-27.619,187.32,22.7965,-20.1333,187.562,27.8861,-15.0567,188.233,37.6328,-10.2037,188.607,43.6482,-4.69799,189.096,51.2259,-0.681482,189.24,54.1683,4.16902,189.802,62.4641,8.84045,190.224,68.976,13.4465,190.564,74.4589,17.9523,190.831,78.9901,22.3942,191.053,82.9515,26.8121,191.232,86.3602,31.169,191.337,88.8358,35.5142,191.413,90.9408,39.8118,191.431,92.311,44.091,191.435,93.4893,48.3461,191.407,94.2587,52.5872,191.359,94.7725,56.8347,191.288,94.996,61.0964,191.192,94.901,65.3486,191.057,94.3131,69.5784,190.901,93.4584,73.8464,190.714,92.2134,78.1437,190.488,90.4998,82.4477,190.255,88.6792,86.7724,189.976,86.2947,91.1334,189.679,83.6789,95.507,189.324,80.3503,99.9484,188.869,75.7897,104.519,188.296,69.8005,109.152,187.616,62.5108,113.91,186.843,54.0763,119,185.828,42.7495,124.316,184.923,32.8314,130.484,183.618,18.2957,-26.5103,190.229,9.8904,-23.565,190.253,11.0422,-17.5832,191.655,30.8727,-12.6684,192.173,39.0346,-6.99077,192.75,48.137,-3.08856,192.529,46.4896,1.68041,193.069,54.8507,6.4643,193.54,62.3238,11.1373,193.964,69.145,15.6415,194.232,73.8988,20.1393,194.481,78.3973,24.6161,194.664,82.0326,28.9875,194.785,84.837,33.3469,194.867,87.1206,37.6819,194.914,88.9296,41.955,194.943,90.4978,46.272,194.968,92.0058,50.5251,194.938,92.7721,54.6654,194.946,93.9992,59.0388,194.746,92.6023,63.2943,194.623,92.1478,67.5283,194.497,91.641,71.7882,194.317,90.4466,76.0983,194.103,88.8055,80.4007,193.868,86.8912,84.7281,193.616,84.7449,89.0699,193.325,82.0988,93.4704,192.979,78.7511,97.8997,192.561,74.4621,102.406,192.052,69.0256,107.011,191.443,62.3162,111.741,190.741,54.4272,116.563,189.97,45.6717,121.536,189.073,35.3183,-25.5857,194.267,10.8881,-20.2471,195.045,23.0705,-15.3313,195.569,31.6983,-10.3618,196.032,39.5043,-4.26899,196.75,51.0295,-0.928242,196.314,46.2589,3.78823,196.733,53.3552,8.73886,197.509,65.3046,13.2995,197.581,67.662,17.8125,197.85,72.662,22.3525,198.09,77.2471,26.7982,198.24,80.5955,31.1925,198.344,83.2958,35.5094,198.398,85.2859,39.8163,198.418,86.8122,44.139,198.43,88.2154,48.4545,198.386,88.8648,52.4503,198.66,93.6993,57.3217,198.348,90.8597,61.4225,198.202,90.0323,65.5196,198.052,89.1543,69.7853,197.906,88.364,74.0524,197.707,86.8522,78.3576,197.457,84.6445,82.7097,197.211,82.4981,87.0539,196.926,79.8134,91.496,196.593,76.4944,95.8855,196.204,72.4071,100.286,195.751,67.4404,104.884,195.193,61.1094,109.528,194.573,53.9524,113.911,193.988,47.188,116.076,194.214,51.1961,-23.0012,198.522,15.7536,-28.2008,197.993,6.53053,-17.4544,199.375,29.6114,-12.4999,199.712,36.0107,-7.43704,200.1,43.1535,-1.91697,200.525,50.9566,3.39734,201.305,63.6883,6.30722,200.686,55.9333,10.4163,200.845,59.5572,15.4924,201.195,66.0548,20.0125,201.468,71.3331,24.5047,201.657,75.4161,28.9489,201.791,78.6848,33.2829,201.868,81.106,37.6156,201.898,82.8602,42.1077,201.947,84.91,46.3598,201.836,84.6387,50.5686,201.938,87.339,54.7271,201.928,88.4289,59.8137,201.793,88.0235,63.5725,201.706,87.8828,67.8052,201.505,86.2623,72.0238,201.301,84.5957,76.3284,201.075,82.6306,80.7238,200.788,79.8271,85.0795,200.475,76.6289,89.4646,200.191,73.8273,93.8109,199.866,70.4362,98.3409,199.352,64.4195,102.906,198.835,58.363,107.285,198.403,53.4308,111.474,197.986,48.6744,114.951,198.078,50.9928,-25.2855,202.266,11.8019,-19.6523,203.129,26.5577,-15.1402,203.358,31.5821,-10.3992,203.54,35.9405,-4.96099,203.945,43.7807,1.56348,204.461,53.832,5.30551,204.539,56.1286,8.8834,204.57,57.7956,12.993,204.561,59.0874,17.6145,204.816,64.3977,22.2115,204.998,68.6143,26.7132,205.168,72.6058,31.0812,205.27,75.5546,35.9366,205.414,79.2404,40.1402,205.49,81.7171,44.3674,205.601,84.6931,48.6514,205.745,88.1705,53.2784,205.766,89.9272,57.8586,205.321,84.8118,62.4449,205.288,85.7723,66.7452,204.798,79.8383,70.2306,204.921,82.6158,74.2807,204.712,80.7308,78.5995,204.403,77.4355,83.0487,204.119,74.5414,87.4561,203.786,70.8882,91.8526,203.4,66.4493,96.4675,202.965,61.33,101.005,202.468,55.2599,105.057,202.157,51.7817,109.569,201.593,44.6999,113.286,201.491,44.3003,117.254,201.547,46.27,-21.6542,206.957,24.4348,-24.1712,206.959,23.8677,-17.1267,207.313,31.6956,-12.8317,207.351,33.9496,-8.01103,207.455,37.3395,3.08494,207.706,45.36,6.41117,207.529,43.7179,10.4506,207.828,49.8671,15.1817,208.179,57,19.7916,208.324,60.8667,24.3696,208.504,65.2569,28.9277,208.651,69.1246,33.4427,208.805,73.0553,38.6581,208.982,77.6153,42.8009,209.009,79.4179,49.9504,208.341,72.5519,51.0226,209.589,91.1414,57.557,208.708,80.1321,60.8719,208.889,83.6554,64.6686,208.769,82.8995,68.3215,208.836,85.023,72.1759,208.548,81.7403,76.5535,208.207,77.8047,81.0278,207.908,74.5343,85.4149,207.542,70.1827,89.9028,207.298,67.7478,93.8272,206.701,59.6474,99.0598,206.051,51.0754,103.185,205.748,47.5672,107.253,205.364,42.8133,111.992,204.74,34.4783,114.737,204.753,35.9496,-23.1575,211.086,27.2572,-18.7808,211.403,34.2053,-16.5594,211.046,29.7547,-9.98428,211.513,39.5637,8.12495,210.824,35.2465,13.9366,211.643,50.8928,17.6191,211.741,53.8707,22.0153,211.871,57.6458,26.5681,212.06,62.4087,31.0724,212.19,66.1891,35.3492,212.362,70.5647,39.8705,212.442,73.4865,47.4177,211.85,67.3922,51.4921,212.203,74.4023,55.5127,212.308,77.3485,59.1157,212.52,81.7521,62.3767,212.58,83.5925,66.9218,212.261,79.9401,71.5828,211.717,72.648,74.3425,211.775,74.3358,78.832,211.213,66.5792,83.2807,210.963,63.9095,87.6425,210.776,62.2302,91.7628,210.387,57.1702,96.8718,209.57,45.3394,100.983,209.353,43.0597,105.207,208.987,38.3933,109.661,208.6,33.4265,114.834,208.451,32.4476])

IndexedFaceSet517.setCoord(Coordinate518)
TextureCoordinate519 = TextureCoordinate()
TextureCoordinate519.setPoint([0.747729,0.0118408,0.726727,0.00952291,0.737635,0.0000925064,0.758642,0.00240936,0.769102,0.0140387,0.779783,0.00330219,0.789771,0.0153309,0.799443,0.00372753,0.80948,0.017501,0.459233,0.0235079,0.437887,0.0231323,0.448389,0.00845623,0.469709,0.00880909,0.480551,0.0237164,0.490982,0.00878334,0.501893,0.0235253,0.512415,0.00853233,0.523251,0.0230034,0.533688,0.00782871,0.544606,0.0221203,0.737091,0.0208984,0.716515,0.0183155,0.75792,0.0234724,0.779501,0.0260815,0.801656,0.0283079,0.826591,0.0274036,0.320621,0.0327828,0.299202,0.0314602,0.309656,0.0176747,0.331041,0.0189812,0.341956,0.033909,0.352378,0.0198889,0.363325,0.0348154,0.3737,0.0207399,0.384659,0.0356842,0.395067,0.021468,0.406078,0.0365926,0.416465,0.0222261,0.427436,0.0374969,0.44882,0.0382819,0.470091,0.0387635,0.491387,0.0387996,0.512719,0.0383658,0.534083,0.0375631,0.5554,0.0365066,0.565932,0.0209963,0.576752,0.0352864,0.587233,0.0197868,0.598091,0.0339884,0.608624,0.0187584,0.619402,0.0326314,0.629962,0.0173798,0.640686,0.0311818,0.651177,0.0158802,0.662065,0.0295616,0.726147,0.0308119,0.704367,0.0252899,0.747373,0.0327898,0.76888,0.0357842,0.790434,0.0384531,0.81359,0.0390904,0.833509,0.0364895,0.89783,0.0351181,0.879534,0.0338779,0.891681,0.0214992,0.909701,0.0219833,0.91637,0.0365115,0.288967,0.044887,0.269205,0.0418708,0.278299,0.0296668,0.310204,0.0465405,0.331542,0.047814,0.352869,0.0488752,0.37423,0.049865,0.395592,0.0509353,0.416993,0.0520381,0.43835,0.0530804,0.459669,0.0539249,0.480968,0.0543228,0.502305,0.0541367,0.523607,0.0533707,0.544938,0.0522417,0.566267,0.0509251,0.587591,0.0494667,0.608886,0.0479606,0.630153,0.0464746,0.651486,0.0449105,0.672762,0.0430935,0.683244,0.0275393,0.694052,0.0408999,0.714751,0.0380123,0.736626,0.0426471,0.758225,0.0458963,0.779752,0.0486252,0.800942,0.0505674,0.822164,0.0496723,0.844083,0.049951,0.854678,0.0373991,0.86506,0.0493204,0.886394,0.0480003,0.905228,0.0491508,0.278699,0.0582273,0.26052,0.0567882,0.299789,0.0601929,0.321154,0.0616673,0.342446,0.0628841,0.363869,0.064155,0.385168,0.0654633,0.40654,0.0668368,0.427875,0.0681758,0.449198,0.0692993,0.47051,0.0700247,0.491825,0.070155,0.513145,0.0696089,0.534382,0.0685513,0.555746,0.0670497,0.577015,0.0653793,0.598311,0.0636421,0.619648,0.061935,0.64094,0.0603024,0.662282,0.0585566,0.683542,0.0565549,0.704812,0.054137,0.726626,0.0552258,0.748023,0.057326,0.769063,0.0596914,0.790359,0.0619092,0.811594,0.0629935,0.832975,0.0631578,0.85423,0.062574,0.875617,0.0611616,0.898113,0.0605206,0.268512,0.0714888,0.248832,0.069338,0.28942,0.0736788,0.310774,0.0754269,0.332072,0.0768621,0.353382,0.0783278,0.374723,0.0799049,0.39609,0.0816578,0.417403,0.0832766,0.438728,0.0846918,0.460081,0.0857722,0.48139,0.0862027,0.502688,0.0859426,0.524014,0.0851733,0.545267,0.0837889,0.566608,0.0819886,0.587875,0.0798672,0.609087,0.0777577,0.630421,0.0758297,0.65168,0.0740358,0.673029,0.0720983,0.694288,0.069829,0.715428,0.0671569,0.737816,0.0682907,0.758935,0.0711361,0.779685,0.0733482,0.800938,0.074748,0.822287,0.0752738,0.843601,0.0748947,0.864865,0.0741468,0.88713,0.0723964,0.19973,0.0798931,0.180658,0.0748129,0.191995,0.0639081,0.208385,0.0681904,0.218369,0.0852091,0.226851,0.0736927,0.237992,0.086759,0.258724,0.0852029,0.279066,0.0870998,0.30036,0.0890912,0.321639,0.0908009,0.343,0.0924928,0.364303,0.0943718,0.385663,0.0963624,0.40696,0.0982622,0.428329,0.100008,0.449693,0.10137,0.470982,0.102188,0.492251,0.10234,0.51354,0.101847,0.534785,0.10067,0.556062,0.0989286,0.57734,0.0967803,0.598683,0.0943512,0.619926,0.0919305,0.641202,0.0896917,0.662409,0.087632,0.683693,0.085471,0.704996,0.0829541,0.725881,0.0799196,0.747167,0.0780336,0.769309,0.0842306,0.790302,0.086034,0.811544,0.0871196,0.832948,0.0872206,0.854243,0.0867588,0.875352,0.0860291,0.901624,0.0838528,0.196695,0.0832767,0.209896,0.0952431,0.227926,0.0980375,0.247732,0.0983551,0.268665,0.100396,0.28996,0.102663,0.311244,0.104612,0.332602,0.106505,0.353905,0.108592,0.375237,0.110865,0.396609,0.113115,0.417945,0.115338,0.439231,0.117194,0.460572,0.118473,0.481764,0.119024,0.503117,0.118852,0.524394,0.118028,0.545662,0.116425,0.566933,0.114143,0.588151,0.111495,0.609418,0.108654,0.630605,0.105966,0.651904,0.103488,0.673154,0.101211,0.694413,0.0987995,0.715671,0.0959177,0.737009,0.0928534,0.758123,0.0943738,0.779615,0.0972288,0.800914,0.0987249,0.822333,0.0994688,0.843533,0.0993237,0.86454,0.0989593,0.88849,0.101122,0.215756,0.111176,0.237983,0.111377,0.258269,0.113526,0.279602,0.116097,0.300862,0.118322,0.322177,0.120431,0.343563,0.122694,0.364859,0.125322,0.386152,0.128079,0.407494,0.130714,0.42873,0.133113,0.450142,0.134983,0.471426,0.136008,0.492659,0.136365,0.513887,0.135859,0.535238,0.134548,0.556409,0.132386,0.577648,0.129317,0.598903,0.126175,0.620225,0.122933,0.641444,0.119842,0.662608,0.117157,0.683881,0.114633,0.705137,0.111921,0.726396,0.108749,0.747657,0.105886,0.768332,0.107968,0.790257,0.110027,0.811559,0.111432,0.832752,0.111654,0.853823,0.111285,0.876182,0.110872,0.900956,0.114742,0.226685,0.126143,0.247903,0.126672,0.269213,0.12945,0.290504,0.131936,0.311816,0.13427,0.333137,0.136757,0.35442,0.139694,0.375748,0.142847,0.396968,0.14609,0.418367,0.149109,0.43968,0.151464,0.461121,0.153174,0.482208,0.154404,0.503502,0.154362,0.524836,0.153215,0.545978,0.151358,0.567307,0.148299,0.588332,0.144596,0.609704,0.140702,0.630916,0.137137,0.652103,0.133737,0.673414,0.130725,0.69463,0.127961,0.715837,0.124946,0.737083,0.121297,0.757954,0.11748,0.78003,0.117345,0.800912,0.12303,0.822265,0.123693,0.843307,0.123498,0.863698,0.122313,0.887645,0.122175,0.237892,0.139597,0.216899,0.137775,0.258861,0.142737,0.280153,0.1455,0.30143,0.148094,0.322756,0.150873,0.344074,0.154046,0.36536,0.157734,0.386689,0.161466,0.408371,0.166305,0.429377,0.169214,0.45053,0.171645,0.471031,0.175203,0.493052,0.173479,0.514414,0.173027,0.5358,0.171832,0.556845,0.169517,0.578144,0.16595,0.59931,0.160091,0.620446,0.155449,0.641718,0.151359,0.662785,0.147544,0.684061,0.144354,0.705313,0.141187,0.72656,0.137778,0.747621,0.133497,0.768872,0.130358,0.790301,0.134109,0.811614,0.135694,0.832692,0.135593,0.853444,0.134155,0.871477,0.129223,0.227446,0.151563,0.206796,0.14887,0.248533,0.155766,0.269809,0.158988,0.291075,0.161768,0.312413,0.164873,0.333629,0.168458,0.354973,0.17254,0.37651,0.17751,0.398088,0.182861,0.420266,0.187033,0.441162,0.189778,0.461588,0.191099,0.482709,0.191994,0.504094,0.191586,0.525361,0.191232,0.54712,0.189583,0.568374,0.18775,0.591121,0.185529,0.615014,0.182111,0.631146,0.170145,0.652416,0.16555,0.673517,0.161374,0.69478,0.157807,0.716007,0.15431,0.73714,0.150237,0.758351,0.145869,0.780075,0.1429,0.800859,0.147122,0.822086,0.147664,0.842679,0.14645,0.862461,0.145149,0.87996,0.142507,0.21617,0.164464,0.238146,0.168408,0.259448,0.172349,0.280727,0.17559,0.302039,0.178935,0.323297,0.182949,0.344629,0.187581,0.365957,0.193266,0.387409,0.198882,0.408547,0.203227,0.429722,0.205066,0.451079,0.206242,0.472317,0.20682,0.493597,0.206925,0.514818,0.206716,0.536048,0.206095,0.557343,0.204992,0.578709,0.202849,0.60087,0.199863,0.624363,0.195873,0.644877,0.189526,0.663105,0.179667,0.684241,0.175086,0.705516,0.171116,0.726696,0.167127,0.747793,0.162264,0.769248,0.157787,0.790287,0.158113,0.811374,0.159468,0.832216,0.1584,0.852105,0.156662,0.873132,0.156352,0.227678,0.179776,0.214254,0.181549,0.249102,0.185591,0.270437,0.189231,0.291599,0.193107,0.313012,0.197748,0.334388,0.20372,0.35588,0.208833,0.376632,0.214732,0.39816,0.21745,0.41934,0.219124,0.440629,0.220209,0.461843,0.220998,0.483162,0.221402,0.504415,0.221235,0.525653,0.220865,0.546911,0.220109,0.568119,0.21875,0.589287,0.216813,0.610839,0.213658,0.632621,0.208975,0.653163,0.20192,0.673884,0.194276,0.694948,0.189063,0.716168,0.184379,0.737335,0.179583,0.758371,0.172893,0.779633,0.169216,0.800814,0.170957,0.821673,0.170695,0.841963,0.170497,0.859917,0.166702,0.216959,0.193952,0.196416,0.18798,0.238876,0.198482,0.259966,0.202965,0.281554,0.208222,0.302809,0.214909,0.324312,0.22066,0.345107,0.226383,0.366508,0.229029,0.387607,0.231141,0.408898,0.232691,0.430163,0.233733,0.45142,0.234519,0.472794,0.235069,0.493925,0.235289,0.515174,0.235045,0.536477,0.234439,0.557732,0.233367,0.578907,0.231861,0.600144,0.230054,0.621369,0.227325,0.642166,0.223063,0.663296,0.216402,0.684747,0.209777,0.705777,0.202876,0.726902,0.197416,0.747921,0.191149,0.768984,0.179914,0.790305,0.182261,0.81118,0.182894,0.832308,0.183745,0.845641,0.177481,0.206291,0.2053,0.228252,0.212533,0.249739,0.216386,0.27134,0.224283,0.290718,0.233998,0.31379,0.236542,0.334826,0.240374,0.355966,0.242669,0.377233,0.244511,0.398489,0.246123,0.419702,0.247097,0.440998,0.247742,0.462338,0.248287,0.48347,0.248574,0.504758,0.248507,0.525998,0.248108,0.547157,0.247321,0.568433,0.24621,0.589682,0.244726,0.610846,0.242972,0.632101,0.240548,0.653172,0.237876,0.674015,0.234897,0.695255,0.225809,0.716262,0.216793,0.737391,0.209956,0.758664,0.199907,0.77958,0.193321,0.800531,0.194825,0.819916,0.195119,0.845127,0.194474,0.218054,0.224141,0.210879,0.221075,0.239522,0.229763,0.265567,0.236835,0.281488,0.248345,0.303199,0.25197,0.324426,0.25449,0.345652,0.256495,0.366914,0.258141,0.388145,0.259649,0.409354,0.26075,0.430663,0.261506,0.45188,0.261834,0.47306,0.261868,0.494209,0.261966,0.515438,0.261779,0.536691,0.261182,0.557888,0.260398,0.579099,0.259357,0.600387,0.257965,0.621537,0.256102,0.642815,0.253878,0.663791,0.251438,0.68497,0.248466,0.699675,0.240051,0.725689,0.230257,0.747237,0.215995,0.768741,0.203973,0.789734,0.20638,0.809374,0.207106,0.208357,0.233827,0.228393,0.244174,0.248499,0.25787,0.27143,0.263588,0.292933,0.266572,0.314125,0.268652,0.335354,0.270436,0.356591,0.271949,0.377771,0.273427,0.398929,0.274784,0.420149,0.275729,0.441493,0.276263,0.462701,0.276611,0.483743,0.276444,0.50505,0.276276,0.52628,0.275851,0.547441,0.275233,0.568691,0.274408,0.589922,0.273224,0.611099,0.271528,0.63226,0.269542,0.653458,0.267515,0.674658,0.26541,0.695764,0.263019,0.709333,0.252148,0.733552,0.243419,0.758199,0.229713,0.779322,0.217001,0.798509,0.219432,0.815771,0.220284,0.238534,0.271509,0.261256,0.27824,0.282565,0.280783,0.303783,0.282997,0.325027,0.284687,0.346198,0.285908,0.367366,0.287291,0.38857,0.288833,0.409747,0.290134,0.430939,0.291254,0.452363,0.292073,0.473469,0.292225,0.49458,0.292072,0.51582,0.291609,0.537074,0.290965,0.558156,0.290127,0.579471,0.288768,0.600596,0.287128,0.621753,0.285216,0.642924,0.283158,0.663989,0.281346,0.685269,0.279706,0.706496,0.277487,0.727743,0.2732,0.74791,0.254084,0.769753,0.246847,0.788307,0.235609,0.800854,0.222292,0.251086,0.292484,0.22875,0.287623,0.27224,0.294939,0.29344,0.297206,0.314714,0.299037,0.335853,0.30016,0.356927,0.301053,0.378199,0.302355,0.399432,0.303951,0.420592,0.305522,0.44183,0.306919,0.46316,0.307874,0.48458,0.307934,0.505477,0.307564,0.526536,0.306948,0.54776,0.306043,0.568922,0.304665,0.590139,0.302726,0.611333,0.300742,0.632472,0.298705,0.653578,0.296956,0.67474,0.295683,0.695998,0.29407,0.717028,0.291689,0.738242,0.287811,0.76,0.275479,0.772136,0.257029,0.240843,0.306509,0.22021,0.302042,0.261939,0.308983,0.283084,0.311179,0.304266,0.313264,0.325482,0.314659,0.346655,0.315163,0.36788,0.315639,0.389019,0.317123,0.410307,0.319003,0.4316,0.320491,0.453,0.321538,0.474063,0.32197,0.495116,0.321956,0.51619,0.321557,0.537192,0.320801,0.558511,0.319669,0.57985,0.317846,0.600967,0.315804,0.62208,0.3137,0.643177,0.312201,0.664258,0.31127,0.685396,0.310062,0.706552,0.308214,0.727638,0.30549,0.748838,0.301706,0.770299,0.29657,0.230594,0.320366,0.21009,0.31396,0.251674,0.322938,0.272833,0.325035,0.293975,0.327059,0.315183,0.328791,0.336308,0.329873,0.357608,0.330161,0.379243,0.330622,0.40059,0.332295,0.421497,0.334012,0.442545,0.334912,0.463886,0.335544,0.484738,0.335655,0.505776,0.336467,0.5268,0.33576,0.547746,0.334363,0.569228,0.333105,0.59049,0.331557,0.611332,0.329095,0.632553,0.32743,0.653883,0.326917,0.674939,0.325764,0.696063,0.323921,0.717243,0.321907,0.738289,0.319081,0.759543,0.315271,0.782107,0.308055,0.176857,0.315869,0.159557,0.318431,0.161542,0.300849,0.186624,0.314046,0.198807,0.325749,0.220442,0.333675,0.241469,0.336703,0.262587,0.338838,0.283669,0.340727,0.304774,0.342603,0.325933,0.344158,0.347106,0.3452,0.368653,0.345657,0.389746,0.346787,0.411001,0.348449,0.431813,0.349678,0.453249,0.350518,0.474411,0.351245,0.495472,0.351682,0.516778,0.351808,0.537492,0.350733,0.558761,0.349392,0.58006,0.34789,0.600935,0.346024,0.622272,0.343876,0.64342,0.342459,0.664586,0.34142,0.685666,0.339508,0.706731,0.337639,0.727834,0.335463,0.748925,0.332487,0.770108,0.328323,0.783999,0.328222,0.16324,0.332631,0.148477,0.332181,0.188157,0.338656,0.210068,0.346323,0.231181,0.3503,0.25228,0.352605,0.273388,0.354472,0.294512,0.356258,0.315643,0.357873,0.336866,0.359308,0.358101,0.360478,0.379276,0.361388,0.400447,0.362564,0.421565,0.363885,0.442663,0.365189,0.463869,0.366298,0.485207,0.366807,0.506286,0.366801,0.527391,0.366381,0.548471,0.365648,0.569621,0.364166,0.590665,0.362226,0.611921,0.360187,0.632991,0.358482,0.654034,0.356982,0.67521,0.354999,0.696309,0.353109,0.717348,0.351327,0.738401,0.348909,0.759587,0.345687,0.780787,0.340895,0.8028,0.335732,0.152579,0.345283,0.124709,0.340165,0.177824,0.351268,0.199821,0.358436,0.220829,0.363371,0.241994,0.366225,0.26311,0.368318,0.284223,0.370152,0.305391,0.371697,0.326483,0.372976,0.347711,0.374039,0.368903,0.374884,0.389996,0.375755,0.411169,0.376857,0.432335,0.378199,0.453502,0.379566,0.474625,0.380574,0.495899,0.380612,0.517026,0.380348,0.538133,0.379945,0.559241,0.378708,0.580266,0.376739,0.60133,0.374845,0.622533,0.373172,0.643637,0.371715,0.664728,0.370309,0.68585,0.368508,0.706903,0.36695,0.727956,0.36503,0.749101,0.362218,0.770181,0.358571,0.790807,0.352491,0.805127,0.351101,0.142623,0.358338,0.16756,0.363254,0.189384,0.370604,0.210562,0.376223,0.231683,0.379655,0.252867,0.382088,0.273965,0.384062,0.295119,0.385744,0.316279,0.386867,0.33741,0.387736,0.358443,0.388324,0.379622,0.388883,0.40081,0.389735,0.421917,0.390756,0.443088,0.392167,0.464266,0.393576,0.48535,0.394358,0.506449,0.394259,0.527615,0.393968,0.548735,0.393103,0.569842,0.391106,0.590947,0.389005,0.612138,0.387357,0.633182,0.38608,0.654318,0.384895,0.675385,0.383706,0.696449,0.382493,0.717549,0.380872,0.73865,0.378508,0.759716,0.3753,0.780634,0.370978,0.801961,0.362859,0.824508,0.353276,0.157839,0.373822,0.139644,0.360449,0.179095,0.382848,0.200352,0.388602,0.221332,0.392714,0.242561,0.395626,0.263721,0.397912,0.28483,0.399703,0.305928,0.400931,0.327103,0.401746,0.348177,0.402165,0.369253,0.402394,0.390369,0.402796,0.411484,0.40339,0.432613,0.404351,0.453763,0.405941,0.475015,0.407525,0.496091,0.408446,0.51717,0.408348,0.538219,0.407607,0.559435,0.40544,0.580536,0.403031,0.60168,0.401259,0.622739,0.40011,0.643904,0.399234,0.664979,0.398471,0.685955,0.397603,0.707062,0.396388,0.728203,0.394517,0.749188,0.391739,0.770283,0.387986,0.791051,0.382854,0.812375,0.3725,0.833306,0.361434,0.133633,0.372032,0.113394,0.36763,0.128829,0.366716,0.149622,0.382576,0.168874,0.394872,0.190057,0.400774,0.211123,0.405672,0.232276,0.408877,0.253458,0.41152,0.274566,0.413469,0.295614,0.414897,0.316708,0.415843,0.33787,0.416272,0.359022,0.416341,0.380259,0.41634,0.401206,0.416468,0.422795,0.417061,0.442901,0.418836,0.465058,0.420628,0.486322,0.422511,0.506153,0.424581,0.526677,0.424741,0.548396,0.422598,0.57046,0.417372,0.59493,0.419549,0.6114,0.410846,0.633311,0.413379,0.654569,0.412984,0.675497,0.412494,0.696617,0.411485,0.717684,0.410027,0.738694,0.407787,0.759817,0.404628,0.780809,0.40039,0.801831,0.393592,0.820878,0.378654,0.832014,0.371577,0.12323,0.384717,0.0923491,0.383884,0.140456,0.390966,0.158512,0.4043,0.179873,0.412964,0.201005,0.418513,0.2221,0.422101,0.243218,0.424987,0.264215,0.427149,0.285374,0.428709,0.306376,0.42974,0.327494,0.430393,0.348642,0.430574,0.3698,0.430471,0.39078,0.430245,0.412469,0.430396,0.432881,0.433852,0.454671,0.436591,0.476286,0.437972,0.497152,0.441864,0.51749,0.4435,0.535518,0.442669,0.559171,0.438433,0.58057,0.43506,0.602371,0.430948,0.621364,0.422905,0.643963,0.427354,0.665093,0.427003,0.686122,0.426299,0.707255,0.425088,0.72829,0.423294,0.749379,0.420865,0.770385,0.417266,0.791354,0.412095,0.811009,0.398899,0.829747,0.385375,0.842016,0.381859,0.105483,0.401309,0.0863179,0.401721,0.128089,0.404637,0.149017,0.414061,0.16954,0.425105,0.190778,0.430859,0.211855,0.435244,0.232972,0.438262,0.254004,0.440629,0.275126,0.442313,0.296173,0.443424,0.317274,0.444225,0.338267,0.444623,0.359378,0.444647,0.380515,0.444384,0.401571,0.444123,0.423023,0.448677,0.444586,0.453767,0.462786,0.457619,0.487341,0.456114,0.507526,0.459048,0.528759,0.459038,0.549578,0.458221,0.570078,0.455323,0.591673,0.448655,0.612395,0.440427,0.63315,0.439737,0.65456,0.441363,0.675693,0.440683,0.696732,0.439721,0.717896,0.438311,0.738914,0.436378,0.759891,0.43351,0.780887,0.42965,0.801778,0.42334,0.822876,0.414065,0.842777,0.401531,0.850739,0.4002,0.0788985,0.411541,0.0634443,0.411286,0.0668005,0.400425,0.0957379,0.414528,0.117461,0.417655,0.139178,0.42125,0.15921,0.436911,0.180467,0.443133,0.201597,0.448276,0.222708,0.451612,0.243836,0.453955,0.264863,0.455682,0.285941,0.456849,0.306975,0.457679,0.328143,0.458244,0.349185,0.458574,0.37017,0.458572,0.391266,0.458306,0.412443,0.458624,0.43372,0.463507,0.455122,0.469532,0.475737,0.471692,0.497113,0.472507,0.518004,0.472862,0.538788,0.472483,0.559887,0.471258,0.58092,0.466145,0.602632,0.455991,0.622594,0.45101,0.644242,0.455424,0.665287,0.454882,0.686351,0.453914,0.707364,0.452746,0.728436,0.451265,0.749432,0.449246,0.770432,0.446077,0.791488,0.441691,0.81227,0.434266,0.83532,0.43167,0.850591,0.423284,0.0709267,0.421474,0.0859862,0.426377,0.106838,0.429049,0.128555,0.432388,0.149328,0.443043,0.170239,0.455247,0.191327,0.460831,0.212447,0.464756,0.233535,0.467319,0.254667,0.469052,0.275599,0.470232,0.296657,0.471034,0.317863,0.471653,0.338946,0.47191,0.359978,0.472153,0.381034,0.472343,0.402121,0.472312,0.422942,0.472965,0.446599,0.480863,0.46628,0.48378,0.486538,0.485297,0.507536,0.485937,0.528707,0.485915,0.549813,0.484986,0.569719,0.483436,0.591208,0.476005,0.612746,0.46992,0.63372,0.469498,0.654823,0.468816,0.675863,0.467916,0.696944,0.466851,0.717978,0.46563,0.738993,0.464075,0.759982,0.461801,0.780998,0.458547,0.80191,0.453421,0.823387,0.449966,0.845053,0.448186,0.860012,0.448774,0.0765914,0.437769,0.0513845,0.437933,0.0965137,0.440891,0.11792,0.44374,0.139155,0.45245,0.159991,0.466861,0.181158,0.473014,0.2023,0.477469,0.223368,0.480335,0.244421,0.48219,0.265422,0.483477,0.286433,0.484314,0.307529,0.484808,0.328518,0.485181,0.349631,0.485475,0.370781,0.485706,0.391842,0.485966,0.412899,0.486264,0.433819,0.488106,0.455896,0.493418,0.476336,0.496653,0.497135,0.498102,0.518113,0.498704,0.539316,0.498231,0.559588,0.497087,0.578036,0.496667,0.602264,0.48433,0.623408,0.48328,0.644442,0.482502,0.665495,0.481643,0.6865,0.480685,0.707578,0.479633,0.72856,0.478438,0.749533,0.476757,0.770542,0.474208,0.791524,0.470542,0.812482,0.46558,0.833755,0.462892,0.855255,0.45957,0.877574,0.459302,0.0652458,0.451761,0.0441572,0.450549,0.0862785,0.452999,0.107628,0.454343,0.128859,0.456899,0.149766,0.469599,0.170925,0.484621,0.19208,0.489682,0.213118,0.493002,0.234143,0.495158,0.255208,0.496582,0.276176,0.497464,0.297275,0.497919,0.318336,0.498277,0.339312,0.498585,0.360371,0.498849,0.381503,0.499263,0.402502,0.499576,0.423492,0.500146,0.444236,0.502471,0.465491,0.505876,0.486695,0.509429,0.507838,0.510928,0.528735,0.511173,0.549505,0.510442,0.569928,0.507964,0.583544,0.50786,0.612999,0.497182,0.634051,0.496084,0.655054,0.495083,0.676107,0.494211,0.697074,0.49342,0.718061,0.492401,0.739087,0.491161,0.760072,0.489277,0.781032,0.486668,0.802105,0.482156,0.822742,0.476384,0.843662,0.471521,0.86574,0.465337,0.878844,0.462479,0.0556903,0.463729,0.076181,0.46557,0.0970923,0.466469,0.118554,0.467328,0.139314,0.480572,0.160687,0.495971,0.181718,0.501607,0.20285,0.505281,0.223881,0.507848,0.244939,0.509527,0.265904,0.510512,0.286931,0.511071,0.308024,0.511435,0.329059,0.511723,0.350058,0.511981,0.371106,0.512239,0.392219,0.51266,0.413196,0.513288,0.434258,0.514528,0.455167,0.516644,0.476469,0.519821,0.497463,0.522446,0.51842,0.523646,0.539484,0.523204,0.55942,0.523171,0.577827,0.517189,0.600704,0.513311,0.623578,0.509635,0.644606,0.508671,0.665707,0.507944,0.68656,0.507161,0.707646,0.506172,0.728628,0.505076,0.749576,0.503739,0.770588,0.501638,0.791592,0.498578,0.812449,0.493447,0.832918,0.487951,0.853671,0.481835,0.874713,0.46791,0.882868,0.463241,0.0660004,0.478294,0.0450811,0.477845,0.0869055,0.479474,0.108308,0.479696,0.129055,0.488222,0.150147,0.499285,0.171504,0.513124,0.192566,0.51715,0.213665,0.519942,0.234623,0.52193,0.255702,0.523131,0.276723,0.523867,0.29765,0.524498,0.318717,0.525111,0.339733,0.525453,0.360771,0.525647,0.381693,0.525741,0.402781,0.526117,0.423958,0.526883,0.444785,0.52859,0.465901,0.531022,0.487296,0.533639,0.50813,0.53556,0.529056,0.535968,0.549619,0.53565,0.570805,0.525825,0.59238,0.524675,0.613271,0.523243,0.6344,0.522308,0.655493,0.521717,0.6762,0.520996,0.697204,0.520037,0.718201,0.518765,0.739149,0.517551,0.760199,0.515892,0.781123,0.513583,0.80222,0.509733,0.822967,0.503196,0.843732,0.495199,0.863856,0.481663,0.878738,0.467288,0.0559149,0.491304,0.0768311,0.492554,0.0978634,0.493506,0.118822,0.497539,0.139785,0.507488,0.161432,0.524132,0.18233,0.528807,0.203385,0.531696,0.22435,0.533757,0.24536,0.535252,0.266396,0.536563,0.28752,0.537636,0.308536,0.538477,0.329689,0.538906,0.350927,0.539123,0.371723,0.539282,0.392368,0.539071,0.413559,0.539495,0.434578,0.540576,0.45557,0.542383,0.476713,0.544925,0.497719,0.547276,0.518615,0.54851,0.539857,0.547807,0.559366,0.546708,0.582024,0.538037,0.602952,0.536817,0.623985,0.536172,0.6448,0.535508,0.665676,0.535013,0.686678,0.534233,0.707758,0.532845,0.728845,0.53125,0.74972,0.529705,0.770686,0.52771,0.791581,0.525048,0.812635,0.520826,0.833745,0.511349,0.84727,0.495929,0.0667526,0.504982,0.0459779,0.503654,0.0877625,0.506789,0.108752,0.507553,0.129461,0.515853,0.150501,0.527004,0.17212,0.540382,0.193187,0.543318,0.214162,0.545422,0.235171,0.547167,0.256127,0.549115,0.277226,0.550728,0.298367,0.55188,0.319174,0.552509,0.340566,0.55275,0.361632,0.552827,0.382409,0.552825,0.403059,0.552573,0.424206,0.552805,0.445302,0.554068,0.466398,0.556309,0.487369,0.558879,0.508452,0.560661,0.529231,0.560856,0.550524,0.557159,0.56976,0.556491,0.592176,0.550238,0.613278,0.54977,0.63448,0.549341,0.655541,0.549112,0.676333,0.54875,0.697166,0.547682,0.718273,0.545893,0.739406,0.543766,0.760301,0.541519,0.781244,0.539221,0.802149,0.536123,0.824534,0.531772,0.0566841,0.517336,0.0776302,0.519376,0.0987612,0.521415,0.119609,0.522034,0.140114,0.53582,0.161318,0.546867,0.182989,0.555216,0.203937,0.557367,0.224979,0.559078,0.246019,0.561281,0.267182,0.563502,0.288164,0.565257,0.309227,0.566275,0.330089,0.56682,0.351146,0.566914,0.372104,0.566601,0.393195,0.565898,0.413893,0.565756,0.434707,0.565911,0.456197,0.567538,0.477138,0.570459,0.498257,0.572772,0.518808,0.573671,0.539989,0.572577,0.560934,0.567374,0.580538,0.565551,0.602902,0.563225,0.62379,0.563528,0.645139,0.563339,0.666029,0.563116,0.686945,0.562541,0.707856,0.561132,0.728664,0.558721,0.74985,0.555914,0.770693,0.553133,0.791574,0.550624,0.812729,0.547069,0.834797,0.544521,0.0674833,0.531641,0.0469258,0.530786,0.0884641,0.533623,0.10967,0.535535,0.129829,0.544309,0.151019,0.554249,0.172808,0.567055,0.193782,0.56977,0.214804,0.571501,0.235812,0.573232,0.256965,0.575644,0.278033,0.578732,0.298875,0.580431,0.319822,0.580443,0.340816,0.580566,0.361668,0.580429,0.382809,0.579758,0.40386,0.579086,0.424698,0.578925,0.445461,0.579295,0.466823,0.582062,0.487639,0.58509,0.508636,0.586248,0.529761,0.58581,0.55059,0.581764,0.571592,0.576904,0.592029,0.576352,0.6129,0.576545,0.634337,0.576872,0.655523,0.576713,0.67653,0.576625,0.697514,0.576036,0.718414,0.574925,0.739248,0.571035,0.760206,0.567595,0.781114,0.565024,0.802061,0.562208,0.823275,0.556336,0.831535,0.555742,0.0575709,0.544479,0.0782655,0.545973,0.0996477,0.548623,0.120558,0.553709,0.140942,0.565539,0.162579,0.578489,0.183612,0.582201,0.204628,0.584598,0.225793,0.586336,0.246789,0.588301,0.267779,0.590574,0.288676,0.5924,0.309943,0.593158,0.330662,0.593332,0.35126,0.593288,0.37231,0.593229,0.393582,0.59233,0.41437,0.591911,0.435345,0.592301,0.456185,0.594414,0.477428,0.597233,0.498413,0.59897,0.519428,0.599308,0.541061,0.597887,0.561374,0.593175,0.582047,0.589974,0.601928,0.589424,0.622997,0.589581,0.645488,0.588722,0.665959,0.589059,0.687231,0.589187,0.707814,0.587896,0.728737,0.586177,0.749527,0.582794,0.77076,0.580066,0.791532,0.577412,0.812536,0.573547,0.83651,0.566258,0.0679343,0.559788,0.0495725,0.559928,0.0886934,0.563506,0.11125,0.566272,0.130899,0.573066,0.151462,0.584845,0.173441,0.593993,0.194336,0.597434,0.215452,0.600307,0.236411,0.602226,0.257406,0.603881,0.27829,0.60546,0.299464,0.606694,0.320426,0.607538,0.341604,0.605972,0.362059,0.606701,0.383117,0.606011,0.403937,0.605744,0.425015,0.606023,0.445437,0.607967,0.466934,0.610185,0.488078,0.61216,0.509078,0.612575,0.530096,0.612126,0.551449,0.610113,0.572265,0.606558,0.593033,0.603804,0.613188,0.603142,0.634722,0.603201,0.655752,0.602157,0.676654,0.60201,0.697509,0.602081,0.718574,0.600942,0.739305,0.598709,0.76023,0.596265,0.781135,0.593445,0.802133,0.589403,0.824582,0.579811,0.846978,0.570275,0.058939,0.574197,0.0766705,0.576461,0.0997583,0.579428,0.12001,0.582604,0.140192,0.587676,0.16325,0.605041,0.184159,0.60952,0.205125,0.613415,0.226111,0.616728,0.246969,0.618511,0.268142,0.619888,0.289397,0.62114,0.31029,0.621323,0.335131,0.621596,0.352353,0.620674,0.372786,0.620433,0.393877,0.620253,0.414869,0.621875,0.435533,0.623256,0.456139,0.624318,0.477669,0.625956,0.498583,0.62626,0.519615,0.62615,0.540804,0.625703,0.561625,0.6237,0.583639,0.621038,0.603098,0.617522,0.624268,0.616584,0.646041,0.616446,0.666155,0.616902,0.686732,0.617207,0.707882,0.61658,0.729077,0.615221,0.750039,0.612966,0.770925,0.610414,0.79157,0.605914,0.812507,0.600004,0.83589,0.583951,0.0695505,0.58968,0.0485241,0.588571,0.0893471,0.590747,0.110641,0.592082,0.131061,0.600686,0.153112,0.615333,0.174147,0.620617,0.195001,0.625149,0.215762,0.629523,0.236912,0.63273,0.258091,0.634655,0.279105,0.63597,0.300299,0.636797,0.322765,0.637407,0.343977,0.638466,0.362309,0.636218,0.384665,0.637198,0.405877,0.637186,0.426287,0.639787,0.446781,0.640503,0.467811,0.640423,0.488339,0.640348,0.509334,0.640107,0.530498,0.639895,0.551177,0.639847,0.571959,0.639629,0.592785,0.636834,0.613012,0.634555,0.634461,0.633938,0.656178,0.633742,0.676443,0.63261,0.69703,0.632377,0.71837,0.631235,0.739452,0.629136,0.760367,0.626958,0.78135,0.622472,0.802049,0.616642,0.823095,0.609131,0.831271,0.602684,0.0602305,0.603192,0.0778584,0.601459,0.100817,0.603887,0.121271,0.610655,0.142686,0.624394,0.163829,0.631087,0.184894,0.636011,0.205718,0.6406,0.226372,0.644913,0.247525,0.648296,0.268707,0.650171,0.290163,0.651376,0.311204,0.652304,0.331841,0.653168,0.35244,0.654635,0.373085,0.654872,0.394621,0.655001,0.415576,0.655146,0.436589,0.655149,0.457439,0.655017,0.478042,0.654646,0.498975,0.654277,0.520023,0.653959,0.541102,0.653885,0.561705,0.654109,0.582536,0.653646,0.603419,0.652807,0.623897,0.652118,0.645356,0.65117,0.666965,0.649876,0.687651,0.648642,0.708182,0.647085,0.729281,0.645059,0.750036,0.642802,0.771073,0.638804,0.791802,0.632982,0.812537,0.626111,0.834682,0.615188,0.0662719,0.611846,0.0865901,0.614574,0.11104,0.624115,0.132851,0.636036,0.153663,0.641536,0.174595,0.646617,0.195638,0.651248,0.216637,0.655662,0.237488,0.659771,0.258484,0.662884,0.27995,0.665055,0.300689,0.66613,0.321301,0.666946,0.342317,0.667765,0.363048,0.668273,0.384199,0.668673,0.405181,0.668839,0.426068,0.668839,0.446942,0.668949,0.467833,0.668775,0.488755,0.668444,0.509678,0.668147,0.530711,0.66808,0.551562,0.667886,0.572448,0.667442,0.593358,0.666923,0.614165,0.666102,0.634824,0.665493,0.655918,0.664612,0.677058,0.663382,0.698268,0.66192,0.719257,0.659939,0.740169,0.657716,0.761036,0.653997,0.78162,0.648737,0.802348,0.642236,0.82301,0.6348,0.843236,0.628086,0.102563,0.641776,0.123304,0.646825,0.143696,0.653137,0.164471,0.657825,0.185444,0.662193,0.206495,0.666299,0.227432,0.670129,0.248287,0.67355,0.269255,0.676209,0.29021,0.678261,0.311001,0.679519,0.331977,0.680274,0.352903,0.680938,0.373669,0.68158,0.394867,0.682078,0.415785,0.682325,0.436684,0.682547,0.457625,0.682498,0.478677,0.68204,0.499386,0.681723,0.520336,0.681593,0.541566,0.681621,0.562181,0.681378,0.583172,0.680597,0.603915,0.679865,0.624629,0.679101,0.645727,0.678048,0.666731,0.676835,0.687689,0.675625,0.708633,0.673918,0.729393,0.671595,0.750198,0.668448,0.771062,0.663926,0.791944,0.658555,0.812565,0.651918,0.833629,0.643429,0.854272,0.636427,0.866624,0.621848,0.875784,0.627122,0.887005,0.613976,0.897855,0.618676,0.112306,0.656684,0.0992155,0.659301,0.133422,0.663931,0.154405,0.669372,0.17531,0.67346,0.196282,0.67741,0.217187,0.681094,0.238104,0.684355,0.259125,0.687109,0.280094,0.689393,0.300827,0.691391,0.321644,0.692664,0.342843,0.693556,0.363635,0.69437,0.384574,0.695084,0.405587,0.695482,0.426508,0.695848,0.447385,0.695945,0.468245,0.695646,0.489182,0.695216,0.510073,0.695089,0.531092,0.694847,0.551879,0.694408,0.572596,0.694067,0.593653,0.693388,0.614492,0.692712,0.635478,0.691802,0.656375,0.690636,0.67718,0.689282,0.698048,0.68755,0.719005,0.685157,0.739876,0.682024,0.760546,0.678348,0.781415,0.674065,0.802212,0.668681,0.823157,0.661586,0.843936,0.654536,0.864747,0.643951,0.887645,0.632523,0.895228,0.62961,0.102037,0.673248,0.0801492,0.665551,0.124325,0.678386,0.144222,0.68114,0.16506,0.685057,0.186114,0.688687,0.207022,0.692327,0.227904,0.695625,0.248818,0.698375,0.269784,0.700903,0.290739,0.702924,0.311658,0.704549,0.332613,0.705786,0.353501,0.706801,0.374366,0.707684,0.395294,0.708393,0.41623,0.708931,0.437191,0.70903,0.458088,0.708856,0.478921,0.708567,0.499621,0.708265,0.520635,0.707989,0.541583,0.707891,0.562328,0.707646,0.583235,0.707159,0.604172,0.706389,0.625041,0.705459,0.645853,0.704374,0.666792,0.703015,0.687646,0.701189,0.708452,0.698887,0.72939,0.696007,0.750196,0.692746,0.771088,0.688985,0.791834,0.684563,0.812697,0.678961,0.833336,0.672127,0.854573,0.661267,0.876741,0.655071,0.891935,0.636828,0.092167,0.683591,0.0727239,0.678334,0.113595,0.689036,0.134097,0.691887,0.154902,0.696763,0.175912,0.700288,0.196853,0.703563,0.217739,0.706903,0.238685,0.709866,0.2596,0.71246,0.280537,0.714708,0.301448,0.716571,0.322343,0.717916,0.343291,0.719107,0.364158,0.720187,0.385027,0.720938,0.405866,0.721512,0.426896,0.721856,0.447843,0.721886,0.46878,0.721698,0.489597,0.721282,0.510356,0.721023,0.531267,0.720815,0.552005,0.720562,0.572942,0.720095,0.59385,0.719529,0.614636,0.718759,0.635408,0.717706,0.656211,0.716504,0.677173,0.714701,0.698063,0.71256,0.718887,0.709993,0.739729,0.706996,0.760614,0.703473,0.781501,0.699528,0.802345,0.695249,0.823143,0.689685,0.843716,0.681948,0.86512,0.677725,0.0825465,0.694085,0.103307,0.699968,0.125423,0.705956,0.14469,0.707598,0.165598,0.711917,0.186547,0.715257,0.207538,0.718248,0.228549,0.721292,0.249471,0.724022,0.270365,0.726399,0.291236,0.728356,0.3122,0.729858,0.333048,0.731122,0.353934,0.73229,0.374736,0.733086,0.395667,0.733812,0.416618,0.734319,0.437506,0.734636,0.458379,0.734513,0.479094,0.734229,0.500003,0.733918,0.520968,0.733537,0.541677,0.733238,0.562561,0.732871,0.583521,0.732309,0.604301,0.731657,0.62505,0.730709,0.64595,0.729489,0.666906,0.727901,0.687709,0.725949,0.708521,0.723632,0.729329,0.720942,0.750269,0.717704,0.771121,0.714116,0.791951,0.710296,0.812912,0.705668,0.833849,0.70038,0.85427,0.692128,0.875413,0.693902,0.0937417,0.70976,0.11438,0.714199,0.134565,0.718475,0.155349,0.723144,0.175942,0.726761,0.197079,0.729743,0.218369,0.732547,0.239344,0.735618,0.260191,0.738177,0.28107,0.740229,0.301992,0.741795,0.32279,0.743056,0.343659,0.744153,0.364591,0.745178,0.385495,0.745971,0.406256,0.746588,0.427243,0.746932,0.448062,0.74695,0.468952,0.746732,0.489686,0.746537,0.510666,0.74635,0.531524,0.746039,0.552238,0.745599,0.573194,0.745028,0.594027,0.744354,0.614773,0.743507,0.635692,0.7424,0.656568,0.740902,0.677417,0.739124,0.698201,0.737102,0.719027,0.734717,0.739788,0.731971,0.760665,0.728534,0.781513,0.724753,0.802454,0.720691,0.823361,0.716556,0.843471,0.711827,0.864329,0.707149,0.887356,0.703322,0.103751,0.72271,0.0795492,0.714865,0.12505,0.72884,0.145284,0.7343,0.16588,0.738095,0.186878,0.741047,0.208155,0.743869,0.229107,0.746938,0.249959,0.749901,0.270918,0.7521,0.291847,0.753745,0.31261,0.755048,0.333458,0.756251,0.35436,0.757304,0.375239,0.758166,0.396084,0.758879,0.417006,0.759373,0.43789,0.759541,0.458726,0.759489,0.479422,0.759386,0.500227,0.759285,0.521222,0.758939,0.542043,0.758498,0.56292,0.757893,0.583772,0.757266,0.604482,0.756409,0.625329,0.755353,0.646288,0.75392,0.667031,0.752295,0.687787,0.750469,0.708641,0.748403,0.729472,0.74591,0.75023,0.742914,0.771015,0.739033,0.791843,0.734903,0.812425,0.731773,0.833614,0.727628,0.8542,0.722896,0.87364,0.716614,0.0938141,0.730787,0.0857239,0.727086,0.114957,0.738828,0.135807,0.745482,0.156042,0.749398,0.176786,0.752256,0.1979,0.754937,0.219023,0.758095,0.239895,0.761256,0.260695,0.763825,0.281552,0.76567,0.302395,0.767152,0.323266,0.768436,0.34413,0.769518,0.364946,0.770478,0.385859,0.771332,0.406772,0.77195,0.427648,0.77231,0.448519,0.772334,0.469331,0.772261,0.490036,0.772181,0.510857,0.771912,0.531724,0.771508,0.55254,0.770921,0.573417,0.77031,0.594267,0.7695,0.615135,0.768445,0.635845,0.767201,0.656588,0.765655,0.677427,0.763874,0.698202,0.761963,0.71905,0.759665,0.739834,0.756868,0.760801,0.753034,0.781275,0.748657,0.801798,0.744903,0.821807,0.741886,0.844186,0.737718,0.863372,0.732452,0.881698,0.72951,0.0838698,0.735518,0.104321,0.745434,0.126008,0.755459,0.146027,0.759647,0.166406,0.76304,0.187486,0.765934,0.208776,0.768968,0.229662,0.77226,0.250601,0.775276,0.271376,0.777455,0.292271,0.779181,0.313101,0.780612,0.333948,0.781836,0.354815,0.782906,0.375631,0.783803,0.396501,0.784571,0.417467,0.785015,0.438256,0.785203,0.459093,0.785243,0.479872,0.785145,0.500582,0.784928,0.521325,0.784511,0.542192,0.784013,0.563184,0.783374,0.58393,0.782655,0.604756,0.781746,0.625586,0.780516,0.646337,0.779153,0.667133,0.777489,0.687868,0.775584,0.708648,0.773352,0.729525,0.770634,0.750312,0.767381,0.771228,0.762504,0.791663,0.757948,0.812688,0.752843,0.833178,0.753088,0.853602,0.746906,0.873569,0.74084,0.891872,0.736966,0.0951509,0.751243,0.0875507,0.750971,0.115597,0.762791,0.136873,0.770774,0.156965,0.774052,0.177466,0.776983,0.198394,0.779746,0.219506,0.783057,0.240267,0.786321,0.261093,0.788911,0.282148,0.791025,0.302975,0.7927,0.323744,0.794166,0.344656,0.79535,0.365404,0.796354,0.3862,0.797182,0.407071,0.797765,0.427901,0.798179,0.448785,0.798244,0.469659,0.798224,0.490396,0.798111,0.511239,0.797656,0.532003,0.797109,0.552775,0.796582,0.573577,0.795882,0.594434,0.795025,0.615277,0.793935,0.636084,0.792624,0.656816,0.79112,0.677552,0.789268,0.698273,0.787064,0.719134,0.78447,0.739907,0.781263,0.760829,0.776541,0.781315,0.771781,0.801511,0.767187,0.822985,0.766244,0.842624,0.764186,0.863922,0.753264,0.881723,0.750182,0.0836399,0.766254,0.105476,0.772603,0.126395,0.778636,0.147341,0.78497,0.168556,0.787784,0.188502,0.790474,0.209274,0.793616,0.23016,0.797107,0.250905,0.800072,0.271879,0.802452,0.292787,0.804503,0.313596,0.806143,0.334494,0.807612,0.355344,0.808788,0.376072,0.809686,0.396854,0.810379,0.417681,0.810827,0.438574,0.811054,0.45944,0.81112,0.480299,0.811043,0.501063,0.810757,0.521806,0.810271,0.542466,0.809806,0.563269,0.809109,0.584088,0.808218,0.604874,0.807275,0.625768,0.806048,0.646522,0.804609,0.667242,0.802972,0.687983,0.800816,0.708767,0.798176,0.729559,0.79491,0.75023,0.790851,0.771104,0.785703,0.79184,0.78013,0.813053,0.779208,0.832089,0.779044,0.100544,0.789678,0.11708,0.790284,0.136887,0.794914,0.157933,0.79904,0.180096,0.800004,0.199484,0.804679,0.220058,0.807612,0.240847,0.81098,0.261783,0.813716,0.282558,0.81599,0.303434,0.817965,0.324262,0.819569,0.345145,0.820888,0.36592,0.821943,0.386732,0.822745,0.407441,0.823256,0.428284,0.823568,0.449182,0.823745,0.469984,0.823742,0.490809,0.823615,0.511628,0.82326,0.532255,0.822876,0.552962,0.822249,0.573731,0.821463,0.594613,0.820476,0.61544,0.819316,0.636169,0.817955,0.656974,0.816316,0.677694,0.814324,0.698355,0.811678,0.719096,0.808449,0.739854,0.804533,0.76081,0.799723,0.782111,0.79407,0.805025,0.787054,0.82504,0.784398,0.108501,0.801147,0.0945434,0.803412,0.127157,0.805566,0.14752,0.809997,0.168283,0.812715,0.191905,0.816209,0.210011,0.817505,0.230867,0.821437,0.251583,0.824536,0.272445,0.827151,0.293213,0.82931,0.313943,0.831195,0.334795,0.832809,0.355606,0.833949,0.3765,0.834903,0.397316,0.835477,0.418109,0.835952,0.438856,0.836216,0.459576,0.836346,0.480352,0.836325,0.501208,0.836136,0.522005,0.835689,0.542661,0.835104,0.563449,0.834315,0.584298,0.833284,0.605103,0.832201,0.625875,0.83083,0.646701,0.829345,0.667382,0.827504,0.688059,0.825048,0.708923,0.821892,0.729595,0.818125,0.750341,0.813847,0.77165,0.808237,0.793934,0.803386,0.818497,0.796439,0.103822,0.810983,0.116774,0.811425,0.137748,0.820407,0.157981,0.824108,0.181813,0.828306,0.200522,0.827374,0.220766,0.831283,0.241593,0.834812,0.262312,0.838064,0.282887,0.840312,0.303656,0.842452,0.324636,0.844166,0.345365,0.845466,0.366208,0.846504,0.387072,0.8473,0.407726,0.847975,0.428659,0.848621,0.449375,0.848882,0.469556,0.849388,0.490954,0.848515,0.511729,0.848139,0.532381,0.847738,0.553108,0.846978,0.574005,0.845987,0.594779,0.844859,0.615577,0.843615,0.636301,0.842119,0.657111,0.840272,0.677785,0.837961,0.698468,0.835091,0.71917,0.831617,0.739968,0.827606,0.760713,0.823234,0.781455,0.818171,0.107479,0.824941,0.127796,0.830361,0.147682,0.834228,0.168361,0.837764,0.193581,0.843129,0.210488,0.840698,0.23086,0.843987,0.251523,0.849725,0.272741,0.850754,0.293331,0.85312,0.31431,0.855298,0.335197,0.856862,0.356051,0.858104,0.376716,0.858988,0.397454,0.859635,0.418337,0.860221,0.439283,0.860417,0.458529,0.862804,0.482391,0.861167,0.502382,0.860603,0.522324,0.860014,0.543058,0.859466,0.563727,0.858547,0.584473,0.857271,0.605368,0.856031,0.626082,0.854522,0.647083,0.852695,0.667592,0.850496,0.687858,0.847874,0.708628,0.844597,0.72922,0.840954,0.748411,0.837552,0.759446,0.839305,0.117408,0.840576,0.0969419,0.836553,0.138352,0.846822,0.159277,0.849678,0.180738,0.852922,0.204448,0.856511,0.226317,0.862596,0.241929,0.858666,0.260543,0.860299,0.283314,0.863373,0.303908,0.865871,0.324757,0.867789,0.345647,0.869307,0.366234,0.870402,0.386978,0.87116,0.408537,0.872071,0.429167,0.871791,0.449435,0.873048,0.469607,0.873477,0.49435,0.8731,0.512623,0.87291,0.533155,0.871936,0.553556,0.870941,0.574292,0.869795,0.595322,0.868222,0.616014,0.866459,0.636773,0.864906,0.657159,0.863067,0.677888,0.859929,0.698553,0.856804,0.718331,0.854266,0.737076,0.851836,0.753883,0.852821,0.108154,0.85234,0.129025,0.858957,0.148217,0.861154,0.168835,0.863055,0.191918,0.866628,0.219883,0.871245,0.236963,0.872278,0.253478,0.872984,0.272639,0.873477,0.29353,0.875957,0.314688,0.877915,0.335586,0.879776,0.356132,0.881124,0.379056,0.882845,0.399093,0.883975,0.4193,0.885366,0.439864,0.887024,0.462295,0.887785,0.484686,0.884981,0.506922,0.885317,0.527653,0.882132,0.544576,0.883462,0.564065,0.882369,0.584678,0.880554,0.605832,0.878949,0.62659,0.876973,0.647058,0.87462,0.668301,0.871943,0.688827,0.86883,0.707315,0.867018,0.727141,0.863473,0.744425,0.863149,0.763398,0.863956,0.120344,0.871515,0.109006,0.871256,0.138833,0.874753,0.157974,0.875662,0.179315,0.877113,0.228887,0.880572,0.244798,0.879694,0.262367,0.882521,0.283204,0.885849,0.304305,0.887605,0.325321,0.889636,0.346482,0.891422,0.367579,0.893254,0.392136,0.895388,0.411935,0.896176,0.446767,0.892198,0.451045,0.901959,0.483098,0.895938,0.499085,0.89772,0.517458,0.897235,0.535195,0.898227,0.553729,0.896422,0.574633,0.894276,0.595907,0.892479,0.616529,0.890154,0.637698,0.888798,0.655325,0.884666,0.678778,0.880329,0.697571,0.878515,0.715744,0.87611,0.73616,0.872026,0.749182,0.872529,0.112333,0.886344,0.130218,0.889462,0.141867,0.887183,0.169338,0.891701,0.254429,0.889061,0.278331,0.896368,0.295091,0.897701,0.315181,0.899405,0.336007,0.901608,0.356907,0.903341,0.376797,0.905389,0.398155,0.906717,0.43473,0.903205,0.453868,0.90664,0.473094,0.908038,0.490391,0.910235,0.506157,0.911129,0.528078,0.909104,0.550258,0.905242,0.563578,0.906046,0.584563,0.902017,0.605527,0.900554,0.626086,0.89959,0.645012,0.896975,0.667441,0.891097,0.686302,0.889882,0.705193,0.887533,0.724936,0.885057,0.748657,0.884468])

IndexedFaceSet517.setTexCoord(TextureCoordinate519)

Shape513.setGeometry(IndexedFaceSet517)

Transform512.addChildren(Shape513)

fieldValue511.addChildren(Transform512)

ProtoInstance509.addFieldValue(fieldValue511)

fieldValue508.addChildren(ProtoInstance509)

ProtoInstance504.addFieldValue(fieldValue508)

fieldValue493.addChildren(ProtoInstance504)

ProtoInstance490.addFieldValue(fieldValue493)

fieldValue397.addChildren(ProtoInstance490)

ProtoInstance394.addFieldValue(fieldValue397)

fieldValue297.addChildren(ProtoInstance394)

ProtoInstance294.addFieldValue(fieldValue297)

fieldValue293.addChildren(ProtoInstance294)
Group520 = Group()

fieldValue293.addChildren(Group520)

ProtoInstance292.addFieldValue(fieldValue293)
fieldValue521 = fieldValue()
fieldValue521.setName("joints")
ProtoInstance522 = ProtoInstance()
ProtoInstance522.setUSE("Allen_hanim_humanoid_root")

fieldValue521.addChildren(ProtoInstance522)
ProtoInstance523 = ProtoInstance()
ProtoInstance523.setUSE("Allen_hanim_sacroiliac")

fieldValue521.addChildren(ProtoInstance523)
ProtoInstance524 = ProtoInstance()
ProtoInstance524.setUSE("Allen_hanim_l_hip")

fieldValue521.addChildren(ProtoInstance524)
ProtoInstance525 = ProtoInstance()
ProtoInstance525.setUSE("Allen_hanim_l_knee")

fieldValue521.addChildren(ProtoInstance525)
ProtoInstance526 = ProtoInstance()
ProtoInstance526.setUSE("Allen_hanim_l_ankle")

fieldValue521.addChildren(ProtoInstance526)
ProtoInstance527 = ProtoInstance()
ProtoInstance527.setUSE("Allen_hanim_r_hip")

fieldValue521.addChildren(ProtoInstance527)
ProtoInstance528 = ProtoInstance()
ProtoInstance528.setUSE("Allen_hanim_r_knee")

fieldValue521.addChildren(ProtoInstance528)
ProtoInstance529 = ProtoInstance()
ProtoInstance529.setUSE("Allen_hanim_r_ankle")

fieldValue521.addChildren(ProtoInstance529)
ProtoInstance530 = ProtoInstance()
ProtoInstance530.setUSE("Allen_hanim_vl1")

fieldValue521.addChildren(ProtoInstance530)
ProtoInstance531 = ProtoInstance()
ProtoInstance531.setUSE("Allen_hanim_l_shoulder")

fieldValue521.addChildren(ProtoInstance531)
ProtoInstance532 = ProtoInstance()
ProtoInstance532.setUSE("Allen_hanim_l_elbow")

fieldValue521.addChildren(ProtoInstance532)
ProtoInstance533 = ProtoInstance()
ProtoInstance533.setUSE("Allen_hanim_l_wrist")

fieldValue521.addChildren(ProtoInstance533)
ProtoInstance534 = ProtoInstance()
ProtoInstance534.setUSE("Allen_hanim_r_shoulder")

fieldValue521.addChildren(ProtoInstance534)
ProtoInstance535 = ProtoInstance()
ProtoInstance535.setUSE("Allen_hanim_r_elbow")

fieldValue521.addChildren(ProtoInstance535)
ProtoInstance536 = ProtoInstance()
ProtoInstance536.setUSE("Allen_hanim_r_wrist")

fieldValue521.addChildren(ProtoInstance536)
ProtoInstance537 = ProtoInstance()
ProtoInstance537.setUSE("Allen_hanim_vc4")

fieldValue521.addChildren(ProtoInstance537)
ProtoInstance538 = ProtoInstance()
ProtoInstance538.setUSE("Allen_hanim_skullbase")

fieldValue521.addChildren(ProtoInstance538)

ProtoInstance292.addFieldValue(fieldValue521)
fieldValue539 = fieldValue()
fieldValue539.setName("segments")
ProtoInstance540 = ProtoInstance()
ProtoInstance540.setUSE("Allen_hanim_pelvis")

fieldValue539.addChildren(ProtoInstance540)
ProtoInstance541 = ProtoInstance()
ProtoInstance541.setUSE("Allen_hanim_l_thigh")

fieldValue539.addChildren(ProtoInstance541)
ProtoInstance542 = ProtoInstance()
ProtoInstance542.setUSE("Allen_hanim_l_calf")

fieldValue539.addChildren(ProtoInstance542)
ProtoInstance543 = ProtoInstance()
ProtoInstance543.setUSE("Allen_hanim_l_hindfoot")

fieldValue539.addChildren(ProtoInstance543)
ProtoInstance544 = ProtoInstance()
ProtoInstance544.setUSE("Allen_hanim_r_thigh")

fieldValue539.addChildren(ProtoInstance544)
ProtoInstance545 = ProtoInstance()
ProtoInstance545.setUSE("Allen_hanim_r_calf")

fieldValue539.addChildren(ProtoInstance545)
ProtoInstance546 = ProtoInstance()
ProtoInstance546.setUSE("Allen_hanim_r_hindfoot")

fieldValue539.addChildren(ProtoInstance546)
ProtoInstance547 = ProtoInstance()
ProtoInstance547.setUSE("Allen_hanim_c7")

fieldValue539.addChildren(ProtoInstance547)
ProtoInstance548 = ProtoInstance()
ProtoInstance548.setUSE("Allen_hanim_l_upperarm")

fieldValue539.addChildren(ProtoInstance548)
ProtoInstance549 = ProtoInstance()
ProtoInstance549.setUSE("Allen_hanim_l_forearm")

fieldValue539.addChildren(ProtoInstance549)
ProtoInstance550 = ProtoInstance()
ProtoInstance550.setUSE("Allen_hanim_l_hand")

fieldValue539.addChildren(ProtoInstance550)
ProtoInstance551 = ProtoInstance()
ProtoInstance551.setUSE("Allen_hanim_r_upperarm")

fieldValue539.addChildren(ProtoInstance551)
ProtoInstance552 = ProtoInstance()
ProtoInstance552.setUSE("Allen_hanim_r_forearm")

fieldValue539.addChildren(ProtoInstance552)
ProtoInstance553 = ProtoInstance()
ProtoInstance553.setUSE("Allen_hanim_r_hand")

fieldValue539.addChildren(ProtoInstance553)
ProtoInstance554 = ProtoInstance()
ProtoInstance554.setUSE("Allen_hanim_c4")

fieldValue539.addChildren(ProtoInstance554)
ProtoInstance555 = ProtoInstance()
ProtoInstance555.setUSE("Allen_hanim_skull")

fieldValue539.addChildren(ProtoInstance555)

ProtoInstance292.addFieldValue(fieldValue539)

Switch291.addChildren(ProtoInstance292)
ProtoInstance556 = ProtoInstance()
ProtoInstance556.setName("Humanoid1_1")
ProtoInstance556.setDEF("Nancy")
fieldValue557 = fieldValue()
fieldValue557.setName("name")
fieldValue557.setValue("nancy")

ProtoInstance556.addFieldValue(fieldValue557)
fieldValue558 = fieldValue()
fieldValue558.setName("version")
fieldValue558.setValue("1.1")

ProtoInstance556.addFieldValue(fieldValue558)
fieldValue559 = fieldValue()
fieldValue559.setName("info")
fieldValue559.setValue("\"humanoidVersion=Nancy V1.2b\" \"authorName=Cindy Ballreich\" \"authorEmail=cindy@ballreich.net\" \"copyright=1997 3Name3D / Yglesias Wallock Divekar Inc. all rights reserved.\" \"creationDate=Tue Dec 30 08:30:08 PST 1997\" \"usageRestrictions=Noncommercial usage is ok if 3Name3D name and logo <www.ballreich.net/vrml/HAnim/small_logo.gif> is present and proper credit is given.\"")

ProtoInstance556.addFieldValue(fieldValue559)
fieldValue560 = fieldValue()
fieldValue560.setName("humanoidBody")
ProtoInstance561 = ProtoInstance()
ProtoInstance561.setName("Joint")
ProtoInstance561.setDEF("Nancy_hanim_humanoid_root")
fieldValue562 = fieldValue()
fieldValue562.setName("name")
fieldValue562.setValue("humanoid_root")

ProtoInstance561.addFieldValue(fieldValue562)
fieldValue563 = fieldValue()
fieldValue563.setName("center")
fieldValue563.setValue("-0.00405 0.855 -0.000113")

ProtoInstance561.addFieldValue(fieldValue563)
fieldValue564 = fieldValue()
fieldValue564.setName("children")
ProtoInstance565 = ProtoInstance()
ProtoInstance565.setName("Joint")
ProtoInstance565.setDEF("Nancy_hanim_sacroiliac")
fieldValue566 = fieldValue()
fieldValue566.setName("name")
fieldValue566.setValue("sacroiliac")

ProtoInstance565.addFieldValue(fieldValue566)
fieldValue567 = fieldValue()
fieldValue567.setName("center")
fieldValue567.setValue("0 1.01 -0.0204")

ProtoInstance565.addFieldValue(fieldValue567)
fieldValue568 = fieldValue()
fieldValue568.setName("children")
ProtoInstance569 = ProtoInstance()
ProtoInstance569.setName("Segment")
ProtoInstance569.setDEF("Nancy_hanim_pelvis")
fieldValue570 = fieldValue()
fieldValue570.setName("name")
fieldValue570.setValue("pelvis")

ProtoInstance569.addFieldValue(fieldValue570)
fieldValue571 = fieldValue()
fieldValue571.setName("children")
Shape572 = Shape()
Appearance573 = Appearance()
Material574 = Material()
Material574.setUSE("Pants_Color")

Appearance573.setMaterial(Material574)

Shape572.setAppearance(Appearance573)
IndexedFaceSet575 = IndexedFaceSet()
IndexedFaceSet575.setCoordIndex([0,1,40,-1,1,2,40,-1,2,3,40,-1,3,4,40,-1,4,5,40,-1,5,4,9,-1,4,3,8,-1,3,2,8,-1,2,1,6,-1,0,7,1,-1,7,6,1,-1,6,8,2,-1,9,4,10,-1,4,8,10,-1,8,6,12,-1,7,0,47,-1,50,5,9,-1,7,47,55,-1,55,13,7,-1,50,9,56,-1,9,10,14,-1,10,11,15,-1,11,12,16,-1,12,13,19,-1,13,55,17,-1,60,17,55,-1,17,19,13,-1,19,16,12,-1,16,15,11,-1,15,18,10,-1,14,56,9,-1,56,14,64,-1,17,60,20,-1,20,19,17,-1,21,64,14,-1,14,22,21,-1,15,16,24,-1,16,19,24,-1,19,20,26,-1,24,23,15,-1,64,21,69,-1,21,22,29,-1,19,26,25,-1,20,63,27,-1,27,26,20,-1,25,24,19,-1,30,29,22,-1,29,28,21,-1,28,69,21,-1,27,34,26,-1,69,28,79,-1,29,30,32,-1,30,23,33,-1,23,24,37,-1,25,26,34,-1,83,27,77,-1,37,33,23,-1,33,32,30,-1,31,79,28,-1,79,31,84,-1,32,33,36,-1,24,25,37,-1,34,27,83,-1,83,38,34,-1,34,37,25,-1,37,36,33,-1,36,35,32,-1,84,31,89,-1,31,35,89,-1,35,36,39,-1,36,37,39,-1,38,83,89,-1,89,39,38,-1,39,89,35,-1,40,41,0,-1,40,42,41,-1,40,43,42,-1,40,44,43,-1,40,45,44,-1,49,44,45,-1,48,43,44,-1,48,42,43,-1,46,41,42,-1,41,47,0,-1,41,46,47,-1,42,48,46,-1,51,44,49,-1,51,48,44,-1,48,52,53,-1,49,45,50,-1,56,49,50,-1,57,51,49,-1,58,53,52,-1,59,54,53,-1,62,55,54,-1,55,62,60,-1,54,59,62,-1,53,58,59,-1,51,61,58,-1,49,56,57,-1,64,57,56,-1,67,59,58,-1,68,62,59,-1,60,63,20,-1,60,62,63,-1,59,67,68,-1,58,61,67,-1,57,64,65,-1,65,66,57,-1,71,63,62,-1,69,65,64,-1,74,66,65,-1,78,68,67,-1,70,71,62,-1,63,72,27,-1,63,71,72,-1,68,78,76,-1,67,75,78,-1,66,74,75,-1,65,73,74,-1,65,69,73,-1,77,27,72,-1,71,82,72,-1,79,73,69,-1,81,75,74,-1,82,71,70,-1,77,72,83,-1,73,79,80,-1,84,80,79,-1,86,75,81,-1,83,72,82,-1,82,88,83,-1,70,87,82,-1,81,85,86,-1,89,80,84,-1,89,85,80,-1,90,86,85,-1,90,87,86,-1,89,83,88,-1,88,90,89,-1,85,89,90,-1,50,45,5,-1,45,40,5,-1,10,8,11,-1,8,12,11,-1,18,22,10,-1,22,14,10,-1,57,66,51,-1,66,61,51,-1,51,58,48,-1,58,52,48,-1,48,53,46,-1,53,54,46,-1,76,70,68,-1,70,62,68,-1,29,32,28,-1,28,32,31,-1,32,35,31,-1,85,81,80,-1,81,73,80,-1,81,74,73,-1,39,37,38,-1,37,34,38,-1,82,87,88,-1,87,90,88,-1,87,78,86,-1,78,75,86,-1,61,66,67,-1,66,75,67,-1,22,18,15,-1,23,30,15,-1,30,22,15,-1,13,12,7,-1,12,6,7,-1,46,54,47,-1,54,55,47,-1,87,76,78,-1,87,70,76,-1])
IndexedFaceSet575.setCreaseAngle(1.14)
Coordinate576 = Coordinate()
Coordinate576.setPoint([0,1.06,0.0218,0.0561,1.07,0.00726,0.0851,1.07,-0.0115,0.104,1.07,-0.0497,0.0851,1.07,-0.0851,0.032,1.06,-0.0985,0.0873,1.04,0.0078,0.033,1.04,0.0395,0.123,1.05,-0.0405,0.0609,1.02,-0.106,0.0894,0.996,-0.106,0.143,1,-0.0309,0.117,1,0.0164,0.0314,0.999,0.0502,0.0314,0.96,-0.13,0.156,0.966,-0.0405,0.156,0.968,-0.00724,0.0341,0.954,0.0513,0.115,0.96,-0.0916,0.121,0.926,0.0352,0.0357,0.92,0.0497,0.0314,0.91,-0.146,0.0991,0.91,-0.131,0.169,0.883,-0.0448,0.169,0.885,-0.00939,0.123,0.873,0.0384,0.0926,0.872,0.047,0.0325,0.873,0.0287,0.0293,0.866,-0.142,0.102,0.869,-0.131,0.129,0.868,-0.103,0.0314,0.84,-0.125,0.101,0.844,-0.122,0.133,0.846,-0.0878,0.0653,0.835,0.0132,0.0615,0.824,-0.111,0.0985,0.823,-0.101,0.132,0.826,-0.0448,0.0609,0.821,-0.0158,0.0599,0.812,-0.0545,0,1.08,-0.0266,-0.0561,1.07,0.00726,-0.0851,1.07,-0.0115,-0.104,1.07,-0.0497,-0.0851,1.07,-0.0851,-0.032,1.06,-0.0985,-0.0873,1.04,0.0078,-0.033,1.04,0.0395,-0.123,1.05,-0.0405,-0.0609,1.02,-0.106,0,1.02,-0.108,-0.0894,0.996,-0.106,-0.143,1,-0.0309,-0.144,1,-0.011,-0.117,1,0.0164,-0.0314,0.999,0.0502,0,0.961,-0.123,-0.0314,0.96,-0.13,-0.156,0.966,-0.0405,-0.156,0.968,-0.00724,-0.0341,0.954,0.0513,-0.115,0.96,-0.0916,-0.121,0.926,0.0352,-0.0357,0.92,0.0497,0,0.91,-0.127,-0.0314,0.91,-0.146,-0.0991,0.91,-0.131,-0.167,0.911,-0.0448,-0.167,0.912,-0.00671,0,0.883,-0.129,-0.123,0.873,0.0384,-0.0926,0.872,0.047,-0.0325,0.873,0.0287,-0.0293,0.866,-0.142,-0.102,0.869,-0.131,-0.129,0.868,-0.103,-0.166,0.863,-0.0148,0,0.863,-0.00456,-0.166,0.862,-0.0459,0,0.858,-0.1,-0.0314,0.84,-0.125,-0.101,0.844,-0.122,-0.0653,0.835,0.0132,0,0.839,-0.0217,0,0.835,-0.0867,-0.0615,0.824,-0.111,-0.0985,0.823,-0.101,-0.132,0.826,-0.0448,-0.0609,0.821,-0.0158,0,0.831,-0.0626,-0.0599,0.812,-0.0545])

IndexedFaceSet575.setCoord(Coordinate576)

Shape572.setGeometry(IndexedFaceSet575)

fieldValue571.addChildren(Shape572)

ProtoInstance569.addFieldValue(fieldValue571)

fieldValue568.addChildren(ProtoInstance569)
ProtoInstance577 = ProtoInstance()
ProtoInstance577.setName("Joint")
ProtoInstance577.setDEF("Nancy_hanim_l_hip")
fieldValue578 = fieldValue()
fieldValue578.setName("name")
fieldValue578.setValue("l_hip")

ProtoInstance577.addFieldValue(fieldValue578)
fieldValue579 = fieldValue()
fieldValue579.setName("center")
fieldValue579.setValue("0.122 0.888271 -0.0693267")

ProtoInstance577.addFieldValue(fieldValue579)
fieldValue580 = fieldValue()
fieldValue580.setName("children")
ProtoInstance581 = ProtoInstance()
ProtoInstance581.setName("Segment")
ProtoInstance581.setDEF("Nancy_hanim_l_thigh")
fieldValue582 = fieldValue()
fieldValue582.setName("name")
fieldValue582.setValue("l_thigh")

ProtoInstance581.addFieldValue(fieldValue582)
fieldValue583 = fieldValue()
fieldValue583.setName("children")
Shape584 = Shape()
Appearance585 = Appearance()
Material586 = Material()
Material586.setUSE("Pants_Color")

Appearance585.setMaterial(Material586)

Shape584.setAppearance(Appearance585)
IndexedFaceSet587 = IndexedFaceSet()
IndexedFaceSet587.setCoordIndex([0,4,5,-1,3,4,0,-1,0,7,1,-1,0,8,7,-1,0,6,8,-1,0,5,6,-1,0,2,3,-1,0,1,2,-1,9,2,1,-1,10,3,2,-1,11,4,3,-1,12,5,4,-1,13,6,5,-1,15,7,8,-1,9,1,7,-1,7,15,9,-1,8,14,15,-1,5,16,13,-1,5,12,16,-1,4,11,12,-1,3,10,11,-1,2,9,10,-1,20,13,16,-1,18,11,10,-1,19,12,11,-1,20,16,12,-1,23,15,14,-1,15,23,24,-1,12,19,20,-1,11,18,19,-1,10,17,18,-1,26,18,17,-1,27,19,18,-1,27,20,19,-1,28,21,20,-1,29,23,22,-1,23,29,30,-1,20,32,28,-1,20,27,32,-1,18,26,27,-1,17,25,26,-1,25,31,30,-1,30,29,26,-1,30,26,25,-1,29,28,27,-1,29,27,26,-1,28,32,27,-1,22,23,14,-1,20,21,13,-1,21,22,13,-1,22,14,13,-1,9,15,24,-1,10,9,17,-1,9,24,17,-1,6,13,8,-1,13,14,8,-1,28,29,21,-1,29,22,21,-1,24,31,17,-1,31,25,17,-1,30,31,23,-1,31,24,23,-1])
IndexedFaceSet587.setCreaseAngle(1.32)
Coordinate588 = Coordinate()
Coordinate588.setPoint([0.0969,0.804,-0.0486,0.101,0.876,0.0336,0.17,0.894,-0.00778,0.17,0.891,-0.076,0.124,0.858,-0.129,0.076,0.843,-0.143,0.025,0.819,-0.0889,0.0507,0.847,0.0196,0.00349,0.826,-0.0287,0.0991,0.808,0.0406,0.161,0.814,-0.00187,0.165,0.808,-0.0755,0.122,0.788,-0.126,0.00993,0.762,-0.0937,0.00993,0.762,-0.0309,0.0491,0.777,0.0185,0.0755,0.766,-0.139,0.13,0.597,-0.00618,0.132,0.6,-0.0593,0.108,0.603,-0.105,0.0722,0.601,-0.118,0.0314,0.59,-0.0953,0.0239,0.566,-0.0427,0.047,0.566,0.0051,0.0878,0.581,0.0217,0.114,0.499,-0.0132,0.116,0.488,-0.061,0.103,0.567,-0.0991,0.0362,0.557,-0.0926,0.025,0.486,-0.047,0.0507,0.497,-0.00188,0.0862,0.513,0.018,0.0733,0.579,-0.108])

IndexedFaceSet587.setCoord(Coordinate588)

Shape584.setGeometry(IndexedFaceSet587)

fieldValue583.addChildren(Shape584)

ProtoInstance581.addFieldValue(fieldValue583)

fieldValue580.addChildren(ProtoInstance581)
ProtoInstance589 = ProtoInstance()
ProtoInstance589.setName("Joint")
ProtoInstance589.setDEF("Nancy_hanim_l_knee")
fieldValue590 = fieldValue()
fieldValue590.setName("name")
fieldValue590.setValue("l_knee")

ProtoInstance589.addFieldValue(fieldValue590)
fieldValue591 = fieldValue()
fieldValue591.setName("center")
fieldValue591.setValue("0.0738 0.517 -0.0284")

ProtoInstance589.addFieldValue(fieldValue591)
fieldValue592 = fieldValue()
fieldValue592.setName("children")
ProtoInstance593 = ProtoInstance()
ProtoInstance593.setName("Segment")
ProtoInstance593.setDEF("Nancy_hanim_l_calf")
fieldValue594 = fieldValue()
fieldValue594.setName("name")
fieldValue594.setValue("l_calf")

ProtoInstance593.addFieldValue(fieldValue594)
fieldValue595 = fieldValue()
fieldValue595.setName("children")
Shape596 = Shape()
Appearance597 = Appearance()
Material598 = Material()
Material598.setUSE("Pants_Color")

Appearance597.setMaterial(Material598)

Shape596.setAppearance(Appearance597)
IndexedFaceSet599 = IndexedFaceSet()
IndexedFaceSet599.setCoordIndex([2,1,0,-1,2,3,1,-1,2,4,3,-1,2,5,4,-1,2,6,5,-1,2,7,6,-1,2,8,7,-1,2,0,8,-1,9,8,0,-1,10,6,7,-1,11,5,6,-1,12,4,5,-1,12,3,4,-1,13,1,3,-1,1,13,14,-1,3,12,13,-1,5,11,12,-1,6,10,11,-1,8,9,15,-1,22,13,12,-1,13,22,14,-1,17,15,9,-1,20,12,11,-1,21,22,12,-1,23,9,14,-1,9,23,16,-1,14,22,23,-1,12,20,21,-1,15,17,18,-1,9,16,17,-1,24,17,16,-1,25,18,17,-1,26,19,18,-1,27,20,19,-1,28,21,20,-1,29,22,21,-1,30,23,22,-1,31,16,23,-1,23,30,31,-1,22,29,30,-1,21,28,29,-1,20,27,28,-1,19,26,27,-1,18,25,26,-1,17,24,25,-1,16,31,24,-1,33,26,25,-1,36,29,28,-1,37,31,30,-1,29,36,30,-1,25,24,33,-1,31,37,24,-1,32,33,24,-1,24,37,32,-1,38,37,30,-1,30,36,38,-1,41,33,32,-1,42,39,34,-1,44,36,35,-1,45,38,36,-1,46,37,38,-1,38,45,46,-1,36,44,45,-1,35,43,44,-1,39,42,47,-1,32,40,41,-1,40,46,45,-1,41,40,45,-1,41,45,44,-1,44,43,42,-1,44,42,41,-1,43,47,42,-1,39,35,28,-1,35,36,28,-1,34,39,27,-1,39,28,27,-1,33,34,26,-1,34,27,26,-1,33,41,34,-1,41,42,34,-1,40,32,46,-1,32,37,46,-1,10,19,11,-1,19,20,11,-1,14,9,1,-1,9,0,1,-1,8,15,7,-1,7,15,10,-1,15,19,10,-1,15,18,19,-1,43,35,47,-1,35,39,47,-1])
IndexedFaceSet599.setCreaseAngle(1.57)
Coordinate600 = Coordinate()
Coordinate600.setPoint([0.0883,0.532,-0.00349,0.0609,0.533,-0.00833,0.0814,0.55,-0.0395,0.0529,0.536,-0.0368,0.0577,0.544,-0.0577,0.0722,0.546,-0.0717,0.0975,0.54,-0.0647,0.105,0.539,-0.0438,0.104,0.539,-0.0223,0.0862,0.506,0.0158,0.101,0.51,-0.0798,0.0706,0.51,-0.101,0.0406,0.513,-0.0744,0.0368,0.51,-0.0357,0.0556,0.506,-0.000272,0.117,0.508,-0.0169,0.0878,0.361,-0.0126,0.123,0.363,-0.04,0.123,0.363,-0.0663,0.107,0.367,-0.107,0.0588,0.365,-0.122,0.0228,0.358,-0.0926,0.0239,0.358,-0.0475,0.0497,0.358,-0.0234,0.118,0.311,-0.0411,0.118,0.309,-0.0685,0.105,0.31,-0.108,0.0572,0.308,-0.123,0.0201,0.309,-0.0937,0.0191,0.311,-0.0508,0.0475,0.307,-0.0282,0.0883,0.309,-0.018,0.0959,0.124,-0.04,0.0905,0.12,-0.0647,0.0738,0.117,-0.0814,0.0373,0.121,-0.0636,0.0416,0.124,-0.0416,0.0744,0.13,-0.0212,0.0561,0.13,-0.0245,0.0529,0.121,-0.0873,0.0948,0.0897,-0.0368,0.0916,0.0779,-0.0604,0.0717,0.0854,-0.0765,0.0406,0.0918,-0.0626,0.0384,0.0881,-0.0363,0.054,0.0972,-0.0175,0.0765,0.11,-0.0169,0.0486,0.0999,-0.0835])

IndexedFaceSet599.setCoord(Coordinate600)

Shape596.setGeometry(IndexedFaceSet599)

fieldValue595.addChildren(Shape596)

ProtoInstance593.addFieldValue(fieldValue595)

fieldValue592.addChildren(ProtoInstance593)
ProtoInstance601 = ProtoInstance()
ProtoInstance601.setName("Joint")
ProtoInstance601.setDEF("Nancy_hanim_l_ankle")
fieldValue602 = fieldValue()
fieldValue602.setName("name")
fieldValue602.setValue("l_ankle")

ProtoInstance601.addFieldValue(fieldValue602)
fieldValue603 = fieldValue()
fieldValue603.setName("center")
fieldValue603.setValue("0.0645 0.0719 -0.048")

ProtoInstance601.addFieldValue(fieldValue603)
fieldValue604 = fieldValue()
fieldValue604.setName("children")
ProtoInstance605 = ProtoInstance()
ProtoInstance605.setName("Segment")
ProtoInstance605.setDEF("Nancy_hanim_l_hindfoot")
fieldValue606 = fieldValue()
fieldValue606.setName("name")
fieldValue606.setValue("l_hindfoot")

ProtoInstance605.addFieldValue(fieldValue606)
fieldValue607 = fieldValue()
fieldValue607.setName("children")
Shape608 = Shape()
Appearance609 = Appearance()
Material610 = Material()
Material610.setUSE("Shoe_Color")

Appearance609.setMaterial(Material610)

Shape608.setAppearance(Appearance609)
IndexedFaceSet611 = IndexedFaceSet()
IndexedFaceSet611.setCoordIndex([2,1,0,-1,4,3,1,-1,2,4,1,-1,3,6,5,-1,1,3,5,-1,6,8,7,-1,5,6,7,-1,8,10,9,-1,7,8,9,-1,10,12,11,-1,9,10,11,-1,12,14,13,-1,11,12,13,-1,14,16,15,-1,13,14,15,-1,16,18,17,-1,15,16,17,-1,18,20,19,-1,17,18,19,-1,20,22,21,-1,19,20,21,-1,22,24,23,-1,21,22,23,-1,24,25,0,-1,23,24,0,-1,25,4,2,-1,0,25,2,-1,18,26,20,-1,16,26,18,-1,27,26,16,-1,14,27,16,-1,12,27,14,-1,28,27,12,-1,29,28,12,-1,10,29,12,-1,8,29,10,-1,6,37,8,-1,24,30,25,-1,31,30,24,-1,22,31,24,-1,32,31,22,-1,20,32,22,-1,33,32,20,-1,26,33,20,-1,34,33,26,-1,27,34,26,-1,35,34,27,-1,28,35,27,-1,29,35,28,-1,36,35,29,-1,8,36,29,-1,37,36,8,-1,6,38,37,-1,3,38,6,-1,39,38,3,-1,30,39,25,-1,41,40,30,-1,31,41,30,-1,42,41,31,-1,32,42,31,-1,43,42,32,-1,33,43,32,-1,44,43,33,-1,34,44,33,-1,45,44,34,-1,35,45,34,-1,46,45,35,-1,36,46,35,-1,47,46,36,-1,37,47,36,-1,38,47,37,-1,48,47,38,-1,49,48,38,-1,39,49,38,-1,40,49,39,-1,30,40,39,-1,48,49,50,-1,47,48,50,-1,46,47,50,-1,45,46,50,-1,44,45,50,-1,43,44,50,-1,42,43,50,-1,41,42,50,-1,40,41,50,-1,49,40,50,-1,11,13,15,-1,11,15,17,-1,9,11,17,-1,9,17,19,-1,7,9,19,-1,7,19,21,-1,5,7,21,-1,5,21,23,-1,5,23,0,-1,1,5,0,-1,3,4,39,-1,4,25,39,-1])
IndexedFaceSet611.setCreaseAngle(1.57)
Coordinate612 = Coordinate()
Coordinate612.setPoint([0.0529,0,-0.0923,0.0863,0,-0.0862,0.0727,0,-0.0994,0.0863,0.0219,-0.0862,0.0727,0.0219,-0.0994,0.1,0,-0.0594,0.1,0.0219,-0.0594,0.113,0,0.0645,0.113,0.0219,0.0645,0.112,0,0.117,0.112,0.0156,0.117,0.0701,0,0.146,0.0701,0.0156,0.146,0.0468,0,0.153,0.0468,0.0156,0.153,0.0215,0,0.146,0.0215,0.0156,0.146,0.0165,0,0.125,0.0165,0.0156,0.125,0.0211,0,0.0377,0.0211,0.0219,0.0377,0.0393,0,-0.0129,0.0393,0.0219,-0.0129,0.0433,0,-0.0534,0.0433,0.0219,-0.0534,0.0529,0.0219,-0.0923,0.0305,0.0253,0.0938,0.0505,0.0253,0.099,0.0854,0.0253,0.0834,0.102,0.0253,0.0707,0.0568,0.0573,-0.0918,0.0492,0.0573,-0.0497,0.0435,0.0573,-0.0225,0.0442,0.0573,0.0235,0.0623,0.0573,0.0366,0.0911,0.0573,0.0159,0.0962,0.0573,-0.0121,0.0911,0.0573,-0.0482,0.0758,0.0573,-0.0899,0.0676,0.0573,-0.0962,0.0578,0.0953,-0.0896,0.0489,0.0953,-0.0757,0.0447,0.0953,-0.0432,0.0451,0.0953,-0.0128,0.0624,0.0953,-0.00466,0.0857,0.0953,-0.0134,0.0953,0.0953,-0.038,0.0843,0.0953,-0.0803,0.0761,0.0953,-0.0889,0.0682,0.0953,-0.0929,0.0675,0.13,-0.0608])

IndexedFaceSet611.setCoord(Coordinate612)

Shape608.setGeometry(IndexedFaceSet611)

fieldValue607.addChildren(Shape608)

ProtoInstance605.addFieldValue(fieldValue607)

fieldValue604.addChildren(ProtoInstance605)

ProtoInstance601.addFieldValue(fieldValue604)

fieldValue592.addChildren(ProtoInstance601)

ProtoInstance589.addFieldValue(fieldValue592)

fieldValue580.addChildren(ProtoInstance589)

ProtoInstance577.addFieldValue(fieldValue580)

fieldValue568.addChildren(ProtoInstance577)
ProtoInstance613 = ProtoInstance()
ProtoInstance613.setName("Joint")
ProtoInstance613.setDEF("Nancy_hanim_r_hip")
fieldValue614 = fieldValue()
fieldValue614.setName("name")
fieldValue614.setValue("r_hip")

ProtoInstance613.addFieldValue(fieldValue614)
fieldValue615 = fieldValue()
fieldValue615.setName("center")
fieldValue615.setValue("-0.11 0.892362 -0.0732533")

ProtoInstance613.addFieldValue(fieldValue615)
fieldValue616 = fieldValue()
fieldValue616.setName("children")
ProtoInstance617 = ProtoInstance()
ProtoInstance617.setName("Segment")
ProtoInstance617.setDEF("Nancy_hanim_r_thigh")
fieldValue618 = fieldValue()
fieldValue618.setName("name")
fieldValue618.setValue("r_thigh")

ProtoInstance617.addFieldValue(fieldValue618)
fieldValue619 = fieldValue()
fieldValue619.setName("children")
Shape620 = Shape()
Appearance621 = Appearance()
Material622 = Material()
Material622.setUSE("Pants_Color")

Appearance621.setMaterial(Material622)

Shape620.setAppearance(Appearance621)
IndexedFaceSet623 = IndexedFaceSet()
IndexedFaceSet623.setCoordIndex([5,4,0,-1,0,4,3,-1,1,7,0,-1,7,8,0,-1,8,6,0,-1,6,5,0,-1,3,2,0,-1,2,1,0,-1,1,2,9,-1,2,3,10,-1,3,4,11,-1,4,5,12,-1,5,6,13,-1,8,7,15,-1,7,1,9,-1,9,15,7,-1,15,14,8,-1,13,16,5,-1,16,12,5,-1,12,11,4,-1,11,10,3,-1,10,9,2,-1,12,16,20,-1,13,14,22,-1,14,15,23,-1,24,23,15,-1,23,22,14,-1,20,19,12,-1,17,18,26,-1,18,19,27,-1,19,20,27,-1,20,21,28,-1,22,23,29,-1,30,29,23,-1,27,26,18,-1,26,25,17,-1,30,31,25,-1,25,26,29,-1,25,29,30,-1,26,27,28,-1,26,28,29,-1,27,20,28,-1,24,15,9,-1,22,21,13,-1,29,28,22,-1,28,21,22,-1,24,31,23,-1,31,30,23,-1,25,31,17,-1,31,24,17,-1,17,24,10,-1,24,9,10,-1,18,10,11,-1,18,17,10,-1,18,12,19,-1,18,11,12,-1,21,20,13,-1,20,16,13,-1,14,13,8,-1,13,6,8,-1])
IndexedFaceSet623.setCreaseAngle(1.61)
Coordinate624 = Coordinate()
Coordinate624.setPoint([-0.0969,0.804,-0.0486,-0.101,0.876,0.0336,-0.17,0.894,-0.00778,-0.17,0.891,-0.076,-0.124,0.858,-0.129,-0.076,0.843,-0.143,-0.025,0.819,-0.0889,-0.0507,0.847,0.0196,-0.00349,0.826,-0.0287,-0.0991,0.808,0.0406,-0.161,0.814,-0.00187,-0.165,0.808,-0.0755,-0.122,0.788,-0.126,-0.00993,0.762,-0.0937,-0.00993,0.762,-0.0309,-0.0491,0.777,0.0185,-0.0755,0.766,-0.139,-0.13,0.597,-0.00618,-0.132,0.6,-0.0593,-0.108,0.603,-0.105,-0.0722,0.601,-0.118,-0.0314,0.59,-0.0953,-0.0239,0.566,-0.0427,-0.047,0.566,0.0051,-0.0878,0.581,0.0217,-0.114,0.499,-0.0132,-0.116,0.488,-0.061,-0.103,0.567,-0.0991,-0.0362,0.557,-0.0926,-0.025,0.486,-0.047,-0.0507,0.497,-0.00188,-0.0862,0.513,0.018])

IndexedFaceSet623.setCoord(Coordinate624)

Shape620.setGeometry(IndexedFaceSet623)

fieldValue619.addChildren(Shape620)

ProtoInstance617.addFieldValue(fieldValue619)

fieldValue616.addChildren(ProtoInstance617)
ProtoInstance625 = ProtoInstance()
ProtoInstance625.setName("Joint")
ProtoInstance625.setDEF("Nancy_hanim_r_knee")
fieldValue626 = fieldValue()
fieldValue626.setName("name")
fieldValue626.setValue("r_knee")

ProtoInstance625.addFieldValue(fieldValue626)
fieldValue627 = fieldValue()
fieldValue627.setName("center")
fieldValue627.setValue("-0.0699 0.51 -0.0166")

ProtoInstance625.addFieldValue(fieldValue627)
fieldValue628 = fieldValue()
fieldValue628.setName("children")
ProtoInstance629 = ProtoInstance()
ProtoInstance629.setName("Segment")
ProtoInstance629.setDEF("Nancy_hanim_r_calf")
fieldValue630 = fieldValue()
fieldValue630.setName("name")
fieldValue630.setValue("r_calf")

ProtoInstance629.addFieldValue(fieldValue630)
fieldValue631 = fieldValue()
fieldValue631.setName("children")
Shape632 = Shape()
Appearance633 = Appearance()
Material634 = Material()
Material634.setUSE("Pants_Color")

Appearance633.setMaterial(Material634)

Shape632.setAppearance(Appearance633)
IndexedFaceSet635 = IndexedFaceSet()
IndexedFaceSet635.setCoordIndex([14,25,18,-1,25,32,18,-1,32,27,18,-1,27,22,18,-1,22,10,18,-1,10,6,18,-1,6,8,18,-1,8,14,18,-1,14,8,17,-1,6,10,9,-1,10,22,24,-1,22,27,39,-1,27,32,39,-1,32,25,42,-1,25,14,30,-1,17,30,14,-1,30,42,25,-1,42,39,32,-1,39,24,22,-1,24,9,10,-1,4,17,8,-1,39,42,43,-1,30,43,42,-1,17,4,1,-1,24,39,26,-1,39,43,44,-1,30,17,34,-1,16,34,17,-1,34,43,30,-1,44,26,39,-1,0,1,4,-1,1,16,17,-1,16,1,3,-1,1,0,2,-1,0,5,7,-1,5,26,28,-1,26,44,45,-1,44,43,46,-1,43,34,36,-1,34,16,15,-1,15,36,34,-1,36,46,43,-1,46,45,44,-1,45,28,26,-1,28,7,5,-1,7,2,0,-1,2,3,1,-1,3,15,16,-1,45,46,37,-1,36,15,20,-1,36,37,46,-1,13,2,7,-1,3,20,15,-1,3,2,13,-1,36,20,29,-1,29,37,36,-1,13,21,23,-1,21,33,23,-1,41,37,40,-1,37,29,31,-1,29,20,19,-1,19,31,29,-1,31,40,37,-1,40,38,41,-1,35,23,33,-1,23,12,13,-1,12,11,13,-1,31,19,11,-1,40,31,11,-1,40,11,12,-1,12,23,38,-1,12,38,40,-1,23,35,38,-1,28,21,7,-1,21,13,7,-1,45,33,28,-1,33,21,28,-1,33,45,41,-1,45,37,41,-1,33,41,35,-1,41,38,35,-1,20,3,47,-1,11,19,47,-1,19,20,47,-1,13,47,3,-1,13,11,47,-1,4,8,6,-1,26,5,24,-1,5,9,24,-1,6,9,4,-1,9,0,4,-1,9,5,0,-1])
IndexedFaceSet635.setCreaseAngle(1.57)
Coordinate636 = Coordinate()
Coordinate636.setPoint([-0.123,0.363,-0.0663,-0.123,0.363,-0.04,-0.118,0.309,-0.0685,-0.118,0.311,-0.0411,-0.117,0.508,-0.0169,-0.107,0.367,-0.107,-0.105,0.539,-0.0438,-0.105,0.31,-0.108,-0.104,0.539,-0.0223,-0.101,0.51,-0.0798,-0.0975,0.54,-0.0647,-0.0948,0.0897,-0.0368,-0.0916,0.0779,-0.0604,-0.0905,0.12,-0.0647,-0.0883,0.532,-0.00349,-0.0883,0.309,-0.018,-0.0878,0.361,-0.0126,-0.0862,0.506,0.0158,-0.0814,0.55,-0.0395,-0.0765,0.11,-0.0169,-0.0744,0.13,-0.0212,-0.0738,0.117,-0.0814,-0.0722,0.546,-0.0717,-0.0717,0.0854,-0.0765,-0.0706,0.51,-0.101,-0.0609,0.533,-0.00833,-0.0588,0.365,-0.122,-0.0577,0.544,-0.0577,-0.0572,0.308,-0.123,-0.0561,0.13,-0.0245,-0.0556,0.506,-0.000272,-0.054,0.0972,-0.0175,-0.0529,0.536,-0.0368,-0.0529,0.121,-0.0873,-0.0497,0.358,-0.0234,-0.0486,0.0999,-0.0835,-0.0475,0.307,-0.0282,-0.0416,0.124,-0.0416,-0.0406,0.0918,-0.0626,-0.0406,0.513,-0.0744,-0.0384,0.0881,-0.0363,-0.0373,0.121,-0.0636,-0.0368,0.51,-0.0357,-0.0239,0.358,-0.0475,-0.0228,0.358,-0.0926,-0.0201,0.309,-0.0937,-0.0191,0.311,-0.0508,-0.0985,0.125,-0.0375])

IndexedFaceSet635.setCoord(Coordinate636)

Shape632.setGeometry(IndexedFaceSet635)

fieldValue631.addChildren(Shape632)

ProtoInstance629.addFieldValue(fieldValue631)

fieldValue628.addChildren(ProtoInstance629)
ProtoInstance637 = ProtoInstance()
ProtoInstance637.setName("Joint")
ProtoInstance637.setDEF("Nancy_hanim_r_ankle")
fieldValue638 = fieldValue()
fieldValue638.setName("name")
fieldValue638.setValue("r_ankle")

ProtoInstance637.addFieldValue(fieldValue638)
fieldValue639 = fieldValue()
fieldValue639.setName("center")
fieldValue639.setValue("-0.064 0.0753 -0.0412")

ProtoInstance637.addFieldValue(fieldValue639)
fieldValue640 = fieldValue()
fieldValue640.setName("children")
ProtoInstance641 = ProtoInstance()
ProtoInstance641.setName("Segment")
ProtoInstance641.setDEF("Nancy_hanim_r_hindfoot")
fieldValue642 = fieldValue()
fieldValue642.setName("name")
fieldValue642.setValue("r_hindfoot")

ProtoInstance641.addFieldValue(fieldValue642)
fieldValue643 = fieldValue()
fieldValue643.setName("children")
Shape644 = Shape()
Appearance645 = Appearance()
Material646 = Material()
Material646.setUSE("Shoe_Color")

Appearance645.setMaterial(Material646)

Shape644.setAppearance(Appearance645)
IndexedFaceSet647 = IndexedFaceSet()
IndexedFaceSet647.setCoordIndex([6,50,0,-1,50,8,7,-1,50,7,0,-1,1,9,8,-1,1,8,50,-1,49,10,9,-1,49,9,1,-1,46,11,10,-1,46,10,49,-1,2,12,11,-1,2,11,46,-1,3,13,12,-1,3,12,2,-1,4,14,13,-1,4,13,3,-1,45,14,4,-1,47,15,45,-1,19,15,47,-1,48,18,19,-1,5,16,18,-1,5,18,48,-1,6,17,16,-1,6,16,5,-1,0,7,17,-1,0,17,6,-1,14,20,21,-1,14,21,13,-1,13,21,12,-1,12,21,22,-1,12,22,11,-1,11,22,10,-1,17,23,16,-1,16,23,24,-1,16,24,18,-1,18,24,25,-1,18,25,19,-1,19,25,26,-1,19,26,15,-1,15,26,20,-1,20,26,27,-1,20,27,21,-1,21,27,28,-1,21,28,22,-1,22,28,29,-1,10,30,9,-1,9,30,31,-1,9,31,8,-1,8,31,32,-1,17,32,23,-1,23,33,34,-1,23,34,35,-1,23,35,24,-1,24,35,36,-1,24,36,25,-1,25,36,37,-1,25,37,26,-1,26,37,38,-1,26,38,27,-1,27,38,39,-1,27,39,28,-1,28,39,40,-1,28,40,29,-1,29,40,41,-1,29,41,30,-1,30,41,42,-1,30,42,31,-1,31,42,43,-1,31,43,32,-1,32,43,33,-1,32,33,23,-1,44,43,42,-1,44,42,41,-1,44,41,40,-1,44,40,39,-1,44,39,38,-1,44,38,37,-1,44,37,36,-1,44,36,35,-1,44,35,34,-1,44,34,33,-1,44,33,43,-1,4,3,2,-1,45,4,2,-1,45,2,46,-1,47,45,46,-1,48,46,49,-1,5,48,49,-1,5,49,1,-1,6,5,1,-1,6,1,50,-1,30,10,29,-1,10,22,29,-1,17,7,32,-1,7,8,32,-1,19,47,48,-1,47,46,48,-1,20,14,15,-1,14,45,15,-1])
IndexedFaceSet647.setCreaseAngle(1.57)
Coordinate648 = Coordinate()
Coordinate648.setPoint([-0.0727,0,-0.0994,-0.1,0,-0.0594,-0.0701,0,0.146,-0.0468,0,0.153,-0.0215,0,0.146,-0.0433,0,-0.0534,-0.0529,0,-0.0923,-0.0727,0.0219,-0.0994,-0.0863,0.0219,-0.0862,-0.1,0.0219,-0.0594,-0.108,0.0219,-0.00479,-0.112,0.0156,0.117,-0.0701,0.0156,0.146,-0.0468,0.0156,0.153,-0.0215,0.0156,0.146,-0.0165,0.017,0.0777,-0.0433,0.0219,-0.0534,-0.0529,0.0219,-0.0923,-0.0445,0.0273,-0.0189,-0.0265,0.0253,0.0549,-0.0305,0.0253,0.0938,-0.069,0.0253,0.0938,-0.102,0.0253,0.0707,-0.0568,0.0573,-0.0918,-0.0492,0.0573,-0.0497,-0.0424,0.0573,-0.00142,-0.0478,0.0573,0.0341,-0.0623,0.0573,0.0366,-0.0864,0.0573,0.0245,-0.0962,0.0573,-0.0121,-0.0845,0.0573,-0.0764,-0.0758,0.0573,-0.0899,-0.0676,0.0573,-0.0962,-0.0578,0.0953,-0.0896,-0.0489,0.0953,-0.0757,-0.0459,0.0953,-0.0615,-0.0435,0.0953,-0.0292,-0.0485,0.0953,-0.00582,-0.0624,0.0953,-0.00466,-0.0857,0.0953,-0.0134,-0.0953,0.0953,-0.038,-0.0843,0.0953,-0.0803,-0.0761,0.0953,-0.0889,-0.0682,0.0953,-0.0929,-0.0675,0.13,-0.0608,-0.0165,0,0.125,-0.112,0,0.117,-0.0165,0,0.0777,-0.0393,0,-0.0129,-0.108,0,-0.00479,-0.0863,0,-0.0862])

IndexedFaceSet647.setCoord(Coordinate648)

Shape644.setGeometry(IndexedFaceSet647)

fieldValue643.addChildren(Shape644)

ProtoInstance641.addFieldValue(fieldValue643)

fieldValue640.addChildren(ProtoInstance641)

ProtoInstance637.addFieldValue(fieldValue640)

fieldValue628.addChildren(ProtoInstance637)

ProtoInstance625.addFieldValue(fieldValue628)

fieldValue616.addChildren(ProtoInstance625)

ProtoInstance613.addFieldValue(fieldValue616)

fieldValue568.addChildren(ProtoInstance613)

ProtoInstance565.addFieldValue(fieldValue568)

fieldValue564.addChildren(ProtoInstance565)
ProtoInstance649 = ProtoInstance()
ProtoInstance649.setName("Joint")
ProtoInstance649.setDEF("Nancy_hanim_vl1")
fieldValue650 = fieldValue()
fieldValue650.setName("name")
fieldValue650.setValue("vl1")

ProtoInstance649.addFieldValue(fieldValue650)
fieldValue651 = fieldValue()
fieldValue651.setName("center")
fieldValue651.setValue("-0.00405 1.07 -0.0275")

ProtoInstance649.addFieldValue(fieldValue651)
fieldValue652 = fieldValue()
fieldValue652.setName("children")
ProtoInstance653 = ProtoInstance()
ProtoInstance653.setName("Segment")
ProtoInstance653.setDEF("Nancy_hanim_c7")
fieldValue654 = fieldValue()
fieldValue654.setName("name")
fieldValue654.setValue("l1")

ProtoInstance653.addFieldValue(fieldValue654)
fieldValue655 = fieldValue()
fieldValue655.setName("children")
Shape656 = Shape()
Appearance657 = Appearance()
Material658 = Material()
Material658.setUSE("Shirt_Color")

Appearance657.setMaterial(Material658)
ImageTexture659 = ImageTexture()
ImageTexture659.setDEF("small_logo_Tex")
ImageTexture659.setUrl(["small_logo.gif","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/small_logo.gif"])

Appearance657.setTexture(ImageTexture659)

Shape656.setAppearance(Appearance657)
IndexedFaceSet660 = IndexedFaceSet()
IndexedFaceSet660.setCoordIndex([0,1,2,-1,3,0,2,-1,4,5,6,-1,6,7,4,-1,8,7,6,-1,6,9,8,-1,9,10,8,-1,6,5,11,-1,9,6,12,-1,11,12,6,-1,12,10,9,-1,7,8,13,-1,13,4,7,-1,14,15,16,-1,15,17,13,-1,4,13,17,-1,17,15,18,-1,13,19,15,-1,19,13,8,-1,19,16,15,-1,16,19,8,-1,17,20,4,-1,5,4,20,-1,18,21,17,-1,20,17,21,-1,16,22,14,-1,22,16,23,-1,8,23,16,-1,23,8,10,-1,24,25,26,-1,26,27,24,-1,25,28,26,-1,28,29,30,-1,30,26,28,-1,31,32,33,-1,32,25,33,-1,25,24,34,-1,33,25,34,-1,24,35,34,-1,27,35,24,-1,33,36,31,-1,27,26,37,-1,37,26,30,-1,38,37,30,-1,33,34,39,-1,39,34,35,-1,39,35,40,-1,41,38,30,-1,35,27,42,-1,37,42,27,-1,40,35,42,-1,42,37,43,-1,37,38,44,-1,44,43,37,-1,36,45,46,-1,36,33,45,-1,40,42,47,-1,43,47,42,-1,47,48,40,-1,39,40,48,-1,47,43,49,-1,43,44,49,-1,50,49,44,-1,51,46,52,-1,46,45,52,-1,52,45,53,-1,33,53,45,-1,33,39,53,-1,49,54,47,-1,48,47,54,-1,55,56,52,-1,57,52,53,-1,57,55,52,-1,58,57,53,-1,59,58,53,-1,53,39,59,-1,39,48,59,-1,59,48,54,-1,58,59,60,-1,54,49,61,-1,59,54,61,-1,60,59,61,-1,49,50,62,-1,63,62,50,-1,62,61,49,-1,64,63,50,-1,63,64,65,-1,65,62,63,-1,66,60,61,-1,62,65,67,-1,68,67,65,-1,64,69,70,-1,64,70,65,-1,70,68,65,-1,69,71,72,-1,72,70,69,-1,73,74,75,-1,66,76,60,-1,67,77,62,-1,62,77,61,-1,77,66,61,-1,66,77,78,-1,77,67,79,-1,79,67,68,-1,79,78,77,-1,68,70,80,-1,70,72,80,-1,80,79,68,-1,74,73,81,-1,73,76,82,-1,82,81,73,-1,76,66,83,-1,78,83,66,-1,83,82,76,-1,78,79,84,-1,79,80,84,-1,84,85,78,-1,86,84,80,-1,81,82,87,-1,87,88,81,-1,82,83,89,-1,83,78,89,-1,89,87,82,-1,78,85,89,-1,90,91,92,-1,92,93,90,-1,90,94,91,-1,95,96,94,-1,94,90,95,-1,29,96,97,-1,96,95,97,-1,97,30,29,-1,30,97,41,-1,41,97,95,-1,98,99,100,-1,98,91,99,-1,101,92,91,-1,98,101,91,-1,101,102,92,-1,92,102,93,-1,36,103,31,-1,51,103,36,46,-1,103,100,31,-1,100,103,98,-1,104,90,93,-1,90,104,95,-1,95,105,41,-1,104,105,95,-1,106,101,98,-1,102,101,106,-1,107,93,102,-1,93,107,104,-1,108,104,107,-1,107,109,108,-1,110,105,104,-1,104,108,110,-1,109,107,111,-1,107,102,111,-1,111,102,106,-1,111,112,109,-1,106,112,111,-1,113,110,108,-1,110,113,114,-1,51,52,115,-1,116,115,117,-1,117,106,116,-1,118,109,112,-1,119,108,109,-1,108,119,113,-1,109,118,119,-1,120,113,119,-1,119,121,120,-1,52,56,122,-1,122,115,52,-1,115,122,123,-1,117,124,125,-1,106,117,125,-1,118,112,106,125,-1,119,118,125,-1,121,119,125,-1,126,124,123,-1,127,114,113,-1,114,127,128,-1,113,120,127,-1,114,128,129,-1,130,126,123,-1,122,130,123,-1,131,120,121,-1,131,127,120,-1,132,129,128,-1,128,127,132,-1,74,81,133,-1,81,134,133,-1,121,135,131,-1,136,132,127,-1,132,136,137,-1,138,71,129,-1,138,129,132,-1,137,138,132,-1,139,72,71,-1,72,139,80,-1,71,138,139,-1,140,135,121,-1,140,121,125,-1,141,127,131,-1,127,141,136,-1,131,135,141,-1,142,141,135,-1,143,136,141,-1,136,143,137,-1,141,142,143,-1,144,138,137,-1,144,139,138,-1,143,144,137,-1,145,146,134,-1,145,140,146,-1,134,81,145,-1,147,135,140,-1,135,147,142,-1,140,145,147,-1,148,80,139,-1,80,148,86,-1,139,144,148,-1,149,143,142,-1,149,144,143,-1,142,150,149,-1,151,148,144,-1,144,149,151,-1,152,145,81,-1,81,88,152,-1,153,147,145,-1,153,142,147,-1,145,152,153,-1,153,150,142,-1,154,86,148,-1,148,151,154,-1,155,28,25,-1,155,29,28,-1,155,25,32,-1,155,32,31,-1,155,31,100,-1,155,100,99,-1,155,99,91,-1,155,91,94,-1,155,94,96,-1,155,96,29,-1,156,151,149,-1,156,154,151,-1,156,149,150,-1,156,150,153,-1,156,153,152,-1,156,152,88,-1,156,88,87,-1,156,87,89,-1,156,89,85,-1,156,85,84,-1,156,84,86,-1,156,86,154,-1,76,157,60,-1,76,73,158,157,-1,159,158,73,75,160,-1,161,56,55,-1,60,162,58,-1,162,60,157,-1,161,55,163,-1,57,164,163,55,-1,160,163,164,-1,160,164,159,-1,164,57,165,-1,164,165,159,-1,57,58,166,165,-1,166,58,162,-1,165,166,159,-1,166,162,157,158,159,-1,140,125,167,-1,124,168,125,-1,168,167,125,-1,124,169,168,-1,146,140,167,170,-1,168,170,167,-1,168,169,170,-1,146,170,171,-1,169,171,170,-1,172,134,146,171,-1,134,172,130,-1,169,124,126,173,-1,173,126,130,-1,169,173,172,171,-1,173,130,172,-1,122,74,133,174,-1,133,134,174,-1,130,122,174,-1,134,130,174,-1,122,56,175,74,-1,74,175,176,-1,175,56,161,176,-1,74,176,75,-1,176,161,163,-1,176,160,75,-1,176,163,160,-1,115,116,177,51,-1,106,98,177,116,-1,51,177,103,-1,177,98,103,-1])
IndexedFaceSet660.setCreaseAngle(1.59)
Coordinate661 = Coordinate()
Coordinate661.setPoint([0.043,1.25,0.0614,0.101,1.25,0.0614,0.103,1.31,0.0195,0.021,1.32,0.0276,0.0572,1.27,-0.153,0.0524,1.15,-0.134,0,1.19,-0.14,0,1.26,-0.147,-0.0572,1.27,-0.153,-0.0228,1.18,-0.14,-0.0524,1.15,-0.134,0,1.13,-0.126,-0.0228,1.13,-0.124,0,1.31,-0.146,-0.0545,1.35,-0.138,0,1.35,-0.136,-0.0593,1.3,-0.151,0.0593,1.3,-0.151,0.0545,1.35,-0.138,-0.0255,1.3,-0.146,0.0975,1.26,-0.15,0.1,1.3,-0.148,-0.1,1.3,-0.148,-0.0975,1.26,-0.15,-0.117,1.41,-0.0395,-0.0674,1.45,-0.0314,-0.0926,1.41,-0.0937,-0.124,1.4,-0.0706,-0.0583,1.44,-0.0615,-0.0228,1.46,-0.0872,-0.0534,1.42,-0.112,-0.0228,1.42,0.00351,-0.0593,1.43,-0.0185,-0.0787,1.39,-0.00293,-0.112,1.4,-0.0131,-0.164,1.39,-0.0373,-0.0153,1.39,0.0159,-0.0953,1.35,-0.136,-0.0545,1.35,-0.138,-0.139,1.34,0.00297,-0.137,1.34,-0.0368,0,1.35,-0.136,-0.156,1.35,-0.0915,-0.132,1.29,-0.127,-0.1,1.3,-0.148,-0.0418,1.35,0.0168,-0.013,1.37,0.0167,-0.151,1.28,-0.0878,-0.136,1.32,-0.0406,-0.124,1.26,-0.125,-0.0975,1.26,-0.15,0.00228,1.37,0.0167,-0.00959,1.32,0.0276,-0.0918,1.31,0.0195,-0.141,1.25,-0.0744,-0.0316,1.25,0.0614,-0.00261,1.25,0.0458,-0.0611,1.25,0.0668,-0.0896,1.25,0.0614,-0.126,1.24,0.012,-0.126,1.22,0.0141,-0.129,1.17,-0.0523,-0.115,1.16,-0.105,-0.0851,1.18,-0.134,-0.0524,1.15,-0.134,-0.083,1.13,-0.122,-0.117,1.15,-0.018,-0.11,1.1,-0.0846,-0.0808,1.1,-0.111,-0.0228,1.13,-0.124,-0.0524,1.1,-0.119,0,1.13,-0.126,-0.0228,1.1,-0.116,-0.0563,1.15,0.0377,-0.00476,1.18,0.0458,-0.0343,1.18,0.0485,-0.0966,1.15,-0.00413,-0.12,1.1,-0.0373,-0.121,1.07,-0.0356,-0.106,1.07,-0.0711,-0.0475,1.06,-0.105,0,1.08,0.0556,-0.0787,1.08,0.0347,-0.103,1.08,0.00296,-0.0975,1.01,-0.0873,-0.134,0.998,-0.0314,-0.0475,1.02,-0.109,-0.0325,1.02,0.0529,0,1.02,0.0422,-0.0975,1.02,0.0132,0.0926,1.41,-0.0937,0.0674,1.45,-0.0314,0.117,1.41,-0.0395,0.124,1.4,-0.0706,0.0583,1.44,-0.0615,0.0534,1.42,-0.112,0.0228,1.46,-0.0872,0,1.4,-0.112,0.0787,1.39,-0.00293,0.0593,1.43,-0.0185,0.0228,1.42,0.00351,0.112,1.4,-0.0131,0.164,1.39,-0.0373,0.0153,1.39,0.0159,0.0953,1.35,-0.136,0.0545,1.35,-0.138,0.139,1.34,0.00297,0.156,1.35,-0.0915,0.132,1.29,-0.127,0.151,1.28,-0.0878,0.1,1.3,-0.148,0.137,1.34,-0.0368,0.147,1.32,-0.0406,0.124,1.26,-0.125,0.0975,1.26,-0.15,0.021,1.32,0.0276,0.0532,1.35,0.0168,0.103,1.31,0.0195,0.135,1.29,-0.0406,0.141,1.25,-0.0744,0.132,1.18,-0.083,0.134,1.19,-0.0572,0.014,1.25,0.0458,0.043,1.25,0.0614,0.101,1.25,0.0614,0.138,1.24,0.012,0.065,1.23,0.0743,0.115,1.16,-0.105,0.0851,1.18,-0.134,0.0524,1.15,-0.134,0.043,1.2,0.0641,0.127,1.14,-0.0427,0.083,1.13,-0.122,0.0162,1.18,0.0458,0.0457,1.18,0.0485,0.117,1.15,-0.018,0.11,1.1,-0.0846,0.0808,1.1,-0.111,0.0524,1.1,-0.119,0.0228,1.1,-0.116,0.108,1.15,-0.00413,0.12,1.1,-0.0373,0.121,1.07,-0.0356,0.106,1.07,-0.0711,0.0475,1.06,-0.105,0.0787,1.08,0.0347,0.0844,1.15,0.0297,0.103,1.08,0.00296,0,1.07,-0.11,0.0975,1.01,-0.0873,0.134,0.998,-0.0475,0.0475,1.02,-0.109,0.0325,1.02,0.0529,0.0975,1.02,0.0132,0,1.02,-0.117,0,1.44,-0.0389,0,1.01,-0.0259,-0.104,1.19,0.0423,-0.0778,1.19,0.0642,-0.078,1.19,0.0644,-0.0493,1.2,0.0664,-0.0281,1.22,0.0587,-0.104,1.2,0.0568,-0.0484,1.21,0.0692,-0.0549,1.21,0.0708,-0.0806,1.21,0.0713,-0.0852,1.21,0.0703,0.116,1.19,0.043,0.114,1.21,0.0572,0.0967,1.21,0.0701,0.11,1.19,0.0502,0.093,1.19,0.0622,0.0832,1.19,0.0662,0.0863,1.21,0.0728,0.0154,1.21,0.0458,-0.00393,1.21,0.0458,-0.0145,1.2,0.0512,0.0534,1.35,0.0168])

IndexedFaceSet660.setCoord(Coordinate661)
TextureCoordinate662 = TextureCoordinate()
TextureCoordinate662.setPoint([0.1611,-0.02056,0.9468,-0.02056,0.9739,0.9344,-0.137,1.094,0.1973,0.6424,0.2231,0.04876,0.5054,0.2466,0.5054,0.5929,0.8135,0.6424,0.6282,0.1972,0.7876,0.04876,0.5054,-0.05018,0.6282,-0.05018,0.5054,0.8403,0.7989,1.038,0.5054,1.038,0.8248,0.7908,0.186,0.7908,0.2118,1.038,0.6427,0.7908,-0.01977,0.5929,-0.03324,0.7908,1.044,0.7908,1.031,0.5929,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

IndexedFaceSet660.setTexCoord(TextureCoordinate662)

Shape656.setGeometry(IndexedFaceSet660)

fieldValue655.addChildren(Shape656)

ProtoInstance653.addFieldValue(fieldValue655)

fieldValue652.addChildren(ProtoInstance653)
ProtoInstance663 = ProtoInstance()
ProtoInstance663.setName("Joint")
ProtoInstance663.setDEF("Nancy_hanim_l_shoulder")
fieldValue664 = fieldValue()
fieldValue664.setName("name")
fieldValue664.setValue("l_shoulder")

ProtoInstance663.addFieldValue(fieldValue664)
fieldValue665 = fieldValue()
fieldValue665.setName("center")
fieldValue665.setValue("0.167 1.36 -0.0518")

ProtoInstance663.addFieldValue(fieldValue665)
fieldValue666 = fieldValue()
fieldValue666.setName("children")
ProtoInstance667 = ProtoInstance()
ProtoInstance667.setName("Segment")
ProtoInstance667.setDEF("Nancy_hanim_l_upperarm")
fieldValue668 = fieldValue()
fieldValue668.setName("name")
fieldValue668.setValue("l_upperarm")

ProtoInstance667.addFieldValue(fieldValue668)
fieldValue669 = fieldValue()
fieldValue669.setName("children")
Transform670 = Transform()
Transform670.setDEF("l_upperarm_adjust")
Transform670.setCenter([0.182,1.22,-0.047])
Transform670.setRotation([1,0,0,0.119])
Transform670.setTranslation([0,0.0004203,-0.01665])
Shape671 = Shape()
Appearance672 = Appearance()
Material673 = Material()
Material673.setUSE("Skin_Color")

Appearance672.setMaterial(Material673)

Shape671.setAppearance(Appearance672)
IndexedFaceSet674 = IndexedFaceSet()
IndexedFaceSet674.setCoordIndex([2,1,0,-1,2,3,1,-1,2,4,3,-1,2,0,5,-1,6,5,0,-1,7,2,5,-1,8,4,2,-1,8,3,4,-1,9,1,3,-1,10,0,1,-1,0,10,6,-1,1,9,10,-1,3,8,9,-1,2,7,8,-1,5,6,7,-1,11,7,6,-1,14,9,8,-1,15,10,9,-1,11,6,10,-1,10,15,11,-1,9,14,15,-1,8,13,14,-1,8,16,13,-1,7,11,12,-1,21,15,14,-1,15,17,11,-1,15,21,17,-1,16,19,13,-1,13,19,20,-1,21,14,20,-1,14,13,20,-1,12,17,18,-1,12,11,17,-1,12,18,16,-1,18,19,16,-1,12,16,7,-1,16,8,7,-1,19,18,17,-1,20,19,21,-1,19,17,21,-1])
IndexedFaceSet674.setCreaseAngle(1.65)
Coordinate675 = Coordinate()
Coordinate675.setPoint([0.174,1.37,-0.0625,0.185,1.38,-0.0395,0.156,1.39,-0.0464,0.174,1.37,-0.0158,0.154,1.37,-0.0185,0.157,1.38,-0.0733,0.182,1.33,-0.0728,0.151,1.33,-0.0937,0.15,1.34,-0.000787,0.185,1.33,-0.00025,0.201,1.33,-0.0411,0.189,1.26,-0.0808,0.155,1.26,-0.0867,0.151,1.26,-0.000789,0.19,1.26,-0.00401,0.209,1.26,-0.0427,0.141,1.26,-0.0421,0.203,1.08,-0.0744,0.162,1.05,-0.0561,0.169,1.08,-0.00885,0.208,1.07,-0.00133,0.221,1.08,-0.0352])

IndexedFaceSet674.setCoord(Coordinate675)

Shape671.setGeometry(IndexedFaceSet674)

Transform670.addChildren(Shape671)

fieldValue669.addChildren(Transform670)

ProtoInstance667.addFieldValue(fieldValue669)

fieldValue666.addChildren(ProtoInstance667)
ProtoInstance676 = ProtoInstance()
ProtoInstance676.setName("Joint")
ProtoInstance676.setDEF("Nancy_hanim_l_elbow")
fieldValue677 = fieldValue()
fieldValue677.setName("name")
fieldValue677.setValue("l_elbow")

ProtoInstance676.addFieldValue(fieldValue677)
fieldValue678 = fieldValue()
fieldValue678.setName("center")
fieldValue678.setValue("0.196 1.07 -0.0518")

ProtoInstance676.addFieldValue(fieldValue678)
fieldValue679 = fieldValue()
fieldValue679.setName("children")
ProtoInstance680 = ProtoInstance()
ProtoInstance680.setName("Segment")
ProtoInstance680.setDEF("Nancy_hanim_l_forearm")
fieldValue681 = fieldValue()
fieldValue681.setName("name")
fieldValue681.setValue("l_forearm")

ProtoInstance680.addFieldValue(fieldValue681)
fieldValue682 = fieldValue()
fieldValue682.setName("children")
Transform683 = Transform()
Transform683.setDEF("l_forearm_adjust")
Transform683.setCenter([0.198,0.961,-0.0405])
Transform683.setRotation([-1,0,0,0.1])
Transform683.setTranslation([0,0.003724,-0.0236])
Shape684 = Shape()
Appearance685 = Appearance()
Material686 = Material()
Material686.setUSE("Skin_Color")

Appearance685.setMaterial(Material686)

Shape684.setAppearance(Appearance685)
IndexedFaceSet687 = IndexedFaceSet()
IndexedFaceSet687.setCoordIndex([2,1,0,-1,2,3,1,-1,2,4,3,-1,2,5,4,-1,2,6,5,-1,2,0,6,-1,7,6,0,-1,8,5,6,-1,9,4,5,-1,9,3,4,-1,10,1,3,-1,11,0,1,-1,0,11,7,-1,1,10,11,-1,3,9,10,-1,5,12,9,-1,5,8,12,-1,6,7,8,-1,17,16,15,-1,14,17,15,-1,14,18,17,-1,13,18,14,-1,16,17,10,-1,16,10,9,-1,15,16,9,-1,15,9,12,-1,18,13,7,-1,18,7,11,-1,13,14,8,-1,13,8,7,-1,14,15,8,-1,15,12,8,-1,17,18,10,-1,18,11,10,-1])
IndexedFaceSet687.setCreaseAngle(1.75)
Coordinate688 = Coordinate()
Coordinate688.setPoint([0.177,1.09,-0.0609,0.202,1.1,-0.0566,0.189,1.1,-0.0395,0.213,1.1,-0.025,0.203,1.1,-0.0158,0.182,1.09,-0.00563,0.167,1.09,-0.0325,0.176,1.08,-0.0781,0.16,1.06,-0.0373,0.214,1.07,-0.00402,0.228,1.07,-0.0319,0.208,1.08,-0.0765,0.179,1.07,-0.00294,0.21,0.818,-0.0615,0.201,0.82,-0.0405,0.205,0.819,-0.00832,0.224,0.818,-0.00778,0.237,0.82,-0.0282,0.231,0.819,-0.0609])

IndexedFaceSet687.setCoord(Coordinate688)

Shape684.setGeometry(IndexedFaceSet687)

Transform683.addChildren(Shape684)

fieldValue682.addChildren(Transform683)

ProtoInstance680.addFieldValue(fieldValue682)

fieldValue679.addChildren(ProtoInstance680)
ProtoInstance689 = ProtoInstance()
ProtoInstance689.setName("Joint")
ProtoInstance689.setDEF("Nancy_hanim_l_wrist")
fieldValue690 = fieldValue()
fieldValue690.setName("name")
fieldValue690.setValue("l_wrist")

ProtoInstance689.addFieldValue(fieldValue690)
fieldValue691 = fieldValue()
fieldValue691.setName("center")
fieldValue691.setValue("0.213 0.811 -0.0338")

ProtoInstance689.addFieldValue(fieldValue691)
fieldValue692 = fieldValue()
fieldValue692.setName("children")
ProtoInstance693 = ProtoInstance()
ProtoInstance693.setName("Segment")
ProtoInstance693.setDEF("Nancy_hanim_l_hand")
fieldValue694 = fieldValue()
fieldValue694.setName("name")
fieldValue694.setValue("l_hand")

ProtoInstance693.addFieldValue(fieldValue694)
fieldValue695 = fieldValue()
fieldValue695.setName("children")
Transform696 = Transform()
Transform696.setDEF("l_hand_adjust")
Transform696.setCenter([0.213,0.811,-0.0338])
Transform696.setRotation([-0.06361,-0.9967,0.04988,1.333])
Transform696.setTranslation([0,0.005142,-0.008662])
Shape697 = Shape()
Appearance698 = Appearance()
Material699 = Material()
Material699.setUSE("Skin_Color")

Appearance698.setMaterial(Material699)

Shape697.setAppearance(Appearance698)
IndexedFaceSet700 = IndexedFaceSet()
IndexedFaceSet700.setCoordIndex([2,1,0,-1,5,4,3,-1,3,7,6,-1,2,3,6,-1,7,9,8,-1,6,7,8,-1,9,11,10,-1,8,9,10,-1,11,13,12,-1,10,11,12,-1,13,15,14,-1,12,13,14,-1,15,17,16,-1,14,15,16,-1,17,19,18,-1,16,17,18,-1,19,21,20,-1,18,19,20,-1,31,4,1,-1,4,5,0,-1,1,4,0,-1,5,3,2,-1,0,5,2,-1,26,25,24,-1,26,24,23,-1,27,26,23,-1,28,27,23,-1,28,23,22,-1,29,28,22,-1,29,22,21,-1,30,29,21,-1,15,13,11,-1,17,15,11,-1,19,17,11,-1,19,11,9,-1,31,19,9,-1,31,9,7,-1,4,31,7,-1,4,7,3,-1,30,21,19,-1,31,30,19,-1,12,14,16,-1,10,12,16,-1,10,16,18,-1,8,10,18,-1,6,8,1,-1,2,6,1,-1,39,38,37,-1,37,38,40,-1,37,40,36,-1,36,40,41,-1,36,41,35,-1,35,41,42,-1,35,42,34,-1,34,42,43,-1,34,43,33,-1,33,43,44,-1,33,44,32,-1,20,32,44,-1,20,44,45,-1,20,45,46,-1,47,8,18,-1,47,18,20,-1,47,20,46,-1,8,47,1,-1,22,33,32,-1,23,35,34,-1,23,36,35,-1,37,24,25,-1,40,38,27,-1,29,43,42,-1,45,44,30,-1,47,31,1,-1,47,46,31,-1,29,30,43,-1,30,44,43,-1,45,31,46,-1,45,30,31,-1,28,29,41,-1,29,42,41,-1,28,40,27,-1,28,41,40,-1,26,27,39,-1,27,38,39,-1,25,39,37,-1,25,26,39,-1,24,36,23,-1,24,37,36,-1,23,34,22,-1,34,33,22,-1,22,32,21,-1,32,20,21,-1])
IndexedFaceSet700.setCreaseAngle(1.48)
Coordinate701 = Coordinate()
Coordinate701.setPoint([0.211,0.828,-0.0434,0.194,0.81,-0.0445,0.237,0.82,-0.0425,0.236,0.82,-0.0237,0.194,0.81,-0.0254,0.21,0.828,-0.0247,0.252,0.801,-0.0424,0.252,0.801,-0.0231,0.269,0.765,-0.0426,0.268,0.765,-0.0225,0.273,0.732,-0.0395,0.272,0.732,-0.0223,0.27,0.704,-0.0342,0.27,0.704,-0.0224,0.262,0.703,-0.0345,0.261,0.703,-0.0227,0.256,0.717,-0.0389,0.256,0.717,-0.023,0.255,0.738,-0.0408,0.255,0.738,-0.023,0.251,0.734,-0.0406,0.251,0.734,-0.0232,0.251,0.692,-0.0232,0.248,0.657,-0.0233,0.24,0.645,-0.0236,0.226,0.637,-0.0241,0.213,0.639,-0.0246,0.197,0.652,-0.0253,0.188,0.669,-0.0256,0.184,0.697,-0.0258,0.183,0.73,-0.0258,0.187,0.77,-0.0257,0.244,0.696,-0.0375,0.244,0.692,-0.0372,0.242,0.661,-0.0345,0.241,0.658,-0.0343,0.241,0.656,-0.0341,0.231,0.646,-0.0336,0.206,0.65,-0.0349,0.218,0.644,-0.034,0.205,0.652,-0.0352,0.198,0.667,-0.0367,0.195,0.691,-0.039,0.194,0.696,-0.0395,0.193,0.725,-0.042,0.193,0.731,-0.0425,0.197,0.765,-0.0449,0.197,0.77,-0.0453])

IndexedFaceSet700.setCoord(Coordinate701)

Shape697.setGeometry(IndexedFaceSet700)

Transform696.addChildren(Shape697)

fieldValue695.addChildren(Transform696)

ProtoInstance693.addFieldValue(fieldValue695)

fieldValue692.addChildren(ProtoInstance693)

ProtoInstance689.addFieldValue(fieldValue692)

fieldValue679.addChildren(ProtoInstance689)

ProtoInstance676.addFieldValue(fieldValue679)

fieldValue666.addChildren(ProtoInstance676)

ProtoInstance663.addFieldValue(fieldValue666)

fieldValue652.addChildren(ProtoInstance663)
ProtoInstance702 = ProtoInstance()
ProtoInstance702.setName("Joint")
ProtoInstance702.setDEF("Nancy_hanim_r_shoulder")
fieldValue703 = fieldValue()
fieldValue703.setName("name")
fieldValue703.setValue("r_shoulder")

ProtoInstance702.addFieldValue(fieldValue703)
fieldValue704 = fieldValue()
fieldValue704.setName("center")
fieldValue704.setValue("-0.167 1.36 -0.0458")

ProtoInstance702.addFieldValue(fieldValue704)
fieldValue705 = fieldValue()
fieldValue705.setName("children")
ProtoInstance706 = ProtoInstance()
ProtoInstance706.setName("Segment")
ProtoInstance706.setDEF("Nancy_hanim_r_upperarm")
fieldValue707 = fieldValue()
fieldValue707.setName("name")
fieldValue707.setValue("r_upperarm")

ProtoInstance706.addFieldValue(fieldValue707)
fieldValue708 = fieldValue()
fieldValue708.setName("children")
Transform709 = Transform()
Transform709.setDEF("r_upperarm_adjust")
Transform709.setCenter([-0.182,1.22,-0.047])
Transform709.setRotation([1,0,0,0.0836])
Transform709.setTranslation([0,0.000589,-0.01169])
Shape710 = Shape()
Appearance711 = Appearance()
Material712 = Material()
Material712.setUSE("Skin_Color")

Appearance711.setMaterial(Material712)

Shape710.setAppearance(Appearance711)
IndexedFaceSet713 = IndexedFaceSet()
IndexedFaceSet713.setCoordIndex([14,10,20,-1,10,13,20,-1,13,22,20,-1,19,14,20,-1,14,19,12,-1,19,20,24,-1,20,22,25,-1,22,13,25,-1,13,10,11,-1,10,14,5,-1,12,5,14,-1,5,11,10,-1,11,25,13,-1,25,24,20,-1,24,12,19,-1,12,24,9,-1,25,11,8,-1,11,5,2,-1,5,12,9,-1,9,2,5,-1,2,8,11,-1,8,23,25,-1,23,27,25,-1,21,9,24,-1,9,21,7,-1,27,23,18,-1,23,8,18,-1,8,2,6,-1,2,9,7,-1,7,1,2,-1,1,6,2,-1,6,18,8,-1,18,26,27,-1,16,7,21,-1,7,16,4,-1,16,26,17,-1,26,18,15,-1,18,6,3,-1,6,1,0,-1,1,7,0,-1,4,0,7,-1,0,3,6,-1,3,15,18,-1,15,17,26,-1,17,4,16,-1,3,0,15,-1,15,0,4,-1,15,4,17,-1,25,27,24,-1,27,21,24,-1,27,26,21,-1,26,16,21,-1])
IndexedFaceSet713.setCreaseAngle(1.53)
Coordinate714 = Coordinate()
Coordinate714.setPoint([-0.221,1.08,-0.0352,-0.214,1.14,-0.0405,-0.209,1.26,-0.0427,-0.208,1.07,-0.00133,-0.203,1.08,-0.0744,-0.201,1.33,-0.0411,-0.198,1.14,-0.0024,-0.198,1.13,-0.076,-0.19,1.26,-0.00401,-0.189,1.26,-0.0808,-0.185,1.38,-0.0395,-0.185,1.33,-0.00025,-0.182,1.33,-0.0728,-0.174,1.37,-0.0158,-0.174,1.37,-0.0625,-0.169,1.08,-0.00885,-0.167,1.13,-0.0744,-0.162,1.05,-0.0561,-0.16,1.13,-0.000793,-0.157,1.38,-0.0733,-0.156,1.39,-0.0464,-0.155,1.26,-0.0867,-0.154,1.37,-0.0185,-0.151,1.26,-0.000789,-0.151,1.33,-0.0937,-0.15,1.34,-0.000787,-0.15,1.13,-0.0411,-0.141,1.26,-0.0421])

IndexedFaceSet713.setCoord(Coordinate714)

Shape710.setGeometry(IndexedFaceSet713)

Transform709.addChildren(Shape710)

fieldValue708.addChildren(Transform709)

ProtoInstance706.addFieldValue(fieldValue708)

fieldValue705.addChildren(ProtoInstance706)
ProtoInstance715 = ProtoInstance()
ProtoInstance715.setName("Joint")
ProtoInstance715.setDEF("Nancy_hanim_r_elbow")
fieldValue716 = fieldValue()
fieldValue716.setName("name")
fieldValue716.setValue("r_elbow")

ProtoInstance715.addFieldValue(fieldValue716)
fieldValue717 = fieldValue()
fieldValue717.setName("center")
fieldValue717.setValue("-0.192 1.07 -0.0498")

ProtoInstance715.addFieldValue(fieldValue717)
fieldValue718 = fieldValue()
fieldValue718.setName("children")
ProtoInstance719 = ProtoInstance()
ProtoInstance719.setName("Segment")
ProtoInstance719.setDEF("Nancy_hanim_r_forearm")
fieldValue720 = fieldValue()
fieldValue720.setName("name")
fieldValue720.setValue("r_forearm")

ProtoInstance719.addFieldValue(fieldValue720)
fieldValue721 = fieldValue()
fieldValue721.setName("children")
Transform722 = Transform()
Transform722.setDEF("r_forearm_adjust")
Transform722.setCenter([-0.198,0.961,-0.0397])
Transform722.setRotation([-1,0,0,0.1254])
Transform722.setTranslation([0,0.003466,-0.01065])
Shape723 = Shape()
Appearance724 = Appearance()
Material725 = Material()
Material725.setUSE("Skin_Color")

Appearance724.setMaterial(Material725)

Shape723.setAppearance(Appearance724)
IndexedFaceSet726 = IndexedFaceSet()
IndexedFaceSet726.setCoordIndex([20,13,15,-1,13,8,15,-1,8,12,15,-1,12,18,15,-1,18,22,15,-1,22,20,15,-1,20,22,21,-1,22,18,24,-1,18,12,7,-1,12,8,7,-1,8,13,3,-1,13,20,10,-1,21,10,20,-1,10,3,13,-1,3,7,8,-1,7,19,18,-1,19,24,18,-1,24,21,22,-1,21,24,23,-1,24,19,16,-1,19,7,6,-1,7,3,1,-1,3,10,5,-1,10,21,17,-1,17,5,10,-1,5,1,3,-1,1,6,7,-1,6,16,19,-1,16,23,24,-1,23,17,21,-1,1,5,2,-1,5,17,9,-1,9,2,5,-1,1,4,6,-1,4,16,6,-1,23,9,17,-1,9,23,14,-1,23,16,11,-1,4,11,16,-1,11,14,23,-1,11,4,0,-1,11,0,14,-1,0,2,14,-1,14,2,9,-1,2,0,1,-1,0,4,1,-1])
IndexedFaceSet726.setCreaseAngle(1.73)
Coordinate727 = Coordinate()
Coordinate727.setPoint([-0.237,0.82,-0.0282,-0.235,1.02,-0.033,-0.231,0.819,-0.0609,-0.228,1.07,-0.0319,-0.224,0.818,-0.00778,-0.221,1.01,-0.0744,-0.218,1.01,-0.00133,-0.214,1.07,-0.00402,-0.213,1.1,-0.025,-0.21,0.818,-0.0615,-0.208,1.08,-0.0765,-0.205,0.819,-0.00832,-0.203,1.1,-0.0158,-0.202,1.1,-0.0566,-0.201,0.82,-0.0405,-0.189,1.1,-0.0395,-0.183,1.01,-0.00831,-0.183,1.01,-0.0781,-0.182,1.09,-0.00563,-0.179,1.07,-0.00294,-0.177,1.09,-0.0609,-0.176,1.08,-0.0781,-0.167,1.09,-0.0325,-0.166,1,-0.0405,-0.16,1.06,-0.0373])

IndexedFaceSet726.setCoord(Coordinate727)

Shape723.setGeometry(IndexedFaceSet726)

Transform722.addChildren(Shape723)

fieldValue721.addChildren(Transform722)

ProtoInstance719.addFieldValue(fieldValue721)

fieldValue718.addChildren(ProtoInstance719)
ProtoInstance728 = ProtoInstance()
ProtoInstance728.setName("Joint")
ProtoInstance728.setDEF("Nancy_hanim_r_wrist")
fieldValue729 = fieldValue()
fieldValue729.setName("name")
fieldValue729.setValue("r_wrist")

ProtoInstance728.addFieldValue(fieldValue729)
fieldValue730 = fieldValue()
fieldValue730.setName("center")
fieldValue730.setValue("-0.217 0.811 -0.0338")

ProtoInstance728.addFieldValue(fieldValue730)
fieldValue731 = fieldValue()
fieldValue731.setName("children")
ProtoInstance732 = ProtoInstance()
ProtoInstance732.setName("Segment")
ProtoInstance732.setDEF("Nancy_hanim_r_hand")
fieldValue733 = fieldValue()
fieldValue733.setName("name")
fieldValue733.setValue("r_hand")

ProtoInstance732.addFieldValue(fieldValue733)
fieldValue734 = fieldValue()
fieldValue734.setName("children")
Transform735 = Transform()
Transform735.setDEF("r_hand_adjust")
Transform735.setCenter([-0.217,0.811,-0.0338])
Transform735.setRotation([-0.09024,0.994,-0.0624,1.216])
Shape736 = Shape()
Appearance737 = Appearance()
Material738 = Material()
Material738.setUSE("Skin_Color")

Appearance737.setMaterial(Material738)

Shape736.setAppearance(Appearance737)
IndexedFaceSet739 = IndexedFaceSet()
IndexedFaceSet739.setCoordIndex([10,9,0,-1,11,30,31,-1,1,12,11,-1,1,11,0,-1,2,13,12,-1,2,12,1,-1,3,14,13,-1,3,13,2,-1,4,15,14,-1,4,14,3,-1,5,16,15,-1,5,15,4,-1,6,17,16,-1,6,16,5,-1,7,18,17,-1,7,17,6,-1,8,19,18,-1,8,18,7,-1,10,31,30,-1,10,30,9,-1,0,11,31,-1,0,31,10,-1,22,23,24,-1,21,22,24,-1,21,24,25,-1,21,25,26,-1,20,21,26,-1,20,26,27,-1,19,20,27,-1,19,27,28,-1,14,15,16,-1,14,16,17,-1,14,17,18,-1,13,14,18,-1,13,18,29,-1,12,13,29,-1,12,29,30,-1,11,12,30,-1,18,19,28,-1,18,28,29,-1,6,5,4,-1,6,4,3,-1,7,6,3,-1,7,3,2,-1,9,2,1,-1,9,1,0,-1,32,38,33,-1,33,38,39,-1,33,39,34,-1,34,39,40,-1,34,40,35,-1,35,40,41,-1,35,41,36,-1,36,41,42,-1,36,42,37,-1,37,42,43,-1,37,43,44,-1,44,43,8,-1,44,8,45,-1,45,8,46,-1,46,8,7,-1,46,7,2,-1,46,2,47,-1,9,47,2,-1,25,34,35,-1,25,33,34,-1,25,24,33,-1,24,32,33,-1,32,24,23,-1,40,39,21,-1,41,40,21,-1,43,19,8,-1,43,20,19,-1,43,42,20,-1,21,20,41,-1,20,42,41,-1,38,22,39,-1,22,21,39,-1,32,23,38,-1,23,22,38,-1,26,25,35,-1,27,36,37,-1,27,37,28,-1,37,44,28,-1,26,35,27,-1,35,36,27,-1,28,44,45,-1,29,46,47,-1,29,9,30,-1,29,47,9,-1,28,45,29,-1,45,46,29,-1])
IndexedFaceSet739.setCreaseAngle(1.57)
Coordinate740 = Coordinate()
Coordinate740.setPoint([-0.237,0.82,-0.0425,-0.252,0.801,-0.0424,-0.269,0.765,-0.0426,-0.273,0.732,-0.0395,-0.27,0.704,-0.0342,-0.262,0.703,-0.0345,-0.256,0.717,-0.0389,-0.255,0.738,-0.0408,-0.251,0.734,-0.0406,-0.194,0.81,-0.0445,-0.211,0.828,-0.0434,-0.236,0.82,-0.0237,-0.252,0.801,-0.0231,-0.268,0.765,-0.0225,-0.272,0.732,-0.0223,-0.27,0.704,-0.0224,-0.261,0.703,-0.0227,-0.256,0.717,-0.023,-0.255,0.738,-0.023,-0.251,0.734,-0.0232,-0.251,0.692,-0.0232,-0.248,0.657,-0.0233,-0.24,0.645,-0.0236,-0.226,0.637,-0.0241,-0.213,0.639,-0.0246,-0.197,0.652,-0.0253,-0.188,0.669,-0.0256,-0.184,0.697,-0.0258,-0.183,0.73,-0.0258,-0.187,0.77,-0.0257,-0.194,0.81,-0.0254,-0.21,0.828,-0.0247,-0.221,0.641,-0.0336,-0.21,0.65,-0.0348,-0.206,0.652,-0.0352,-0.198,0.667,-0.0368,-0.193,0.692,-0.0392,-0.192,0.696,-0.0396,-0.231,0.646,-0.0336,-0.238,0.656,-0.0342,-0.24,0.658,-0.0344,-0.24,0.662,-0.0347,-0.243,0.692,-0.0372,-0.243,0.696,-0.0376,-0.192,0.725,-0.0421,-0.192,0.73,-0.0426,-0.195,0.766,-0.0451,-0.196,0.77,-0.0454])

IndexedFaceSet739.setCoord(Coordinate740)

Shape736.setGeometry(IndexedFaceSet739)

Transform735.addChildren(Shape736)

fieldValue734.addChildren(Transform735)

ProtoInstance732.addFieldValue(fieldValue734)

fieldValue731.addChildren(ProtoInstance732)

ProtoInstance728.addFieldValue(fieldValue731)

fieldValue718.addChildren(ProtoInstance728)

ProtoInstance715.addFieldValue(fieldValue718)

fieldValue705.addChildren(ProtoInstance715)

ProtoInstance702.addFieldValue(fieldValue705)

fieldValue652.addChildren(ProtoInstance702)
ProtoInstance741 = ProtoInstance()
ProtoInstance741.setName("Joint")
ProtoInstance741.setDEF("Nancy_hanim_vc4")
fieldValue742 = fieldValue()
fieldValue742.setName("name")
fieldValue742.setValue("vc4")

ProtoInstance741.addFieldValue(fieldValue742)
fieldValue743 = fieldValue()
fieldValue743.setName("center")
fieldValue743.setValue("0 1.43 -0.0458")

ProtoInstance741.addFieldValue(fieldValue743)
fieldValue744 = fieldValue()
fieldValue744.setName("children")
ProtoInstance745 = ProtoInstance()
ProtoInstance745.setName("Segment")
ProtoInstance745.setDEF("Nancy_hanim_c4")
fieldValue746 = fieldValue()
fieldValue746.setName("name")
fieldValue746.setValue("c4")

ProtoInstance745.addFieldValue(fieldValue746)
fieldValue747 = fieldValue()
fieldValue747.setName("children")
Shape748 = Shape()
Appearance749 = Appearance()
Material750 = Material()
Material750.setUSE("Skin_Color")

Appearance749.setMaterial(Material750)

Shape748.setAppearance(Appearance749)
IndexedFaceSet751 = IndexedFaceSet()
IndexedFaceSet751.setDEF("neck")
IndexedFaceSet751.setCoordIndex([6,5,2,-1,6,2,3,-1,5,4,1,-1,5,1,2,-1,4,7,0,-1,4,0,1,-1,11,10,9,-1,11,9,8,-1,10,13,12,-1,10,12,9,-1,13,15,14,-1,13,14,12,-1,6,3,11,-1,6,11,8,-1,7,14,15,-1,7,15,0,-1,2,10,11,-1,2,11,3,-1,2,1,13,-1,2,13,10,-1,1,0,15,-1,1,15,13,-1,9,5,6,-1,9,6,8,-1,9,12,4,-1,9,4,5,-1,12,14,7,-1,12,7,4,-1])
IndexedFaceSet751.setCreaseAngle(1.91)
Coordinate752 = Coordinate()
Coordinate752.setPoint([0.0105,1.54,-0.1,0.0357,1.54,-0.0685,0.0382,1.55,-0.0474,0.0105,1.55,-0.0204,0.0373,1.4,-0.0593,0.0577,1.4,-0.0266,0.0158,1.4,0.00512,0.0132,1.41,-0.0824,-0.0158,1.4,0.00512,-0.0577,1.4,-0.0266,-0.0382,1.55,-0.0474,-0.0105,1.55,-0.0204,-0.0373,1.4,-0.0593,-0.0357,1.54,-0.0685,-0.0132,1.41,-0.0824,-0.0105,1.54,-0.1])

IndexedFaceSet751.setCoord(Coordinate752)

Shape748.setGeometry(IndexedFaceSet751)

fieldValue747.addChildren(Shape748)

ProtoInstance745.addFieldValue(fieldValue747)

fieldValue744.addChildren(ProtoInstance745)
ProtoInstance753 = ProtoInstance()
ProtoInstance753.setName("Joint")
ProtoInstance753.setDEF("Nancy_hanim_skullbase")
fieldValue754 = fieldValue()
fieldValue754.setName("name")
fieldValue754.setValue("skullbase")

ProtoInstance753.addFieldValue(fieldValue754)
fieldValue755 = fieldValue()
fieldValue755.setName("center")
fieldValue755.setValue("0 1.54 -0.0409")

ProtoInstance753.addFieldValue(fieldValue755)
fieldValue756 = fieldValue()
fieldValue756.setName("children")
ProtoInstance757 = ProtoInstance()
ProtoInstance757.setName("Segment")
ProtoInstance757.setDEF("Nancy_hanim_skull")
fieldValue758 = fieldValue()
fieldValue758.setName("name")
fieldValue758.setValue("skull")

ProtoInstance757.addFieldValue(fieldValue758)
fieldValue759 = fieldValue()
fieldValue759.setName("children")
Shape760 = Shape()
Appearance761 = Appearance()
Material762 = Material()
Material762.setUSE("Skin_Color")

Appearance761.setMaterial(Material762)

Shape760.setAppearance(Appearance761)
IndexedFaceSet763 = IndexedFaceSet()
IndexedFaceSet763.setDEF("headIFS")
IndexedFaceSet763.setColorIndex([1,1,1,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,1,1,1,-1,1,1,1,-1,0,0,0,-1,1,1,1,-1,1,1,1,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,2,2,2,-1,2,2,2,-1,2,2,2,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,2,2,2,-1,2,2,2,-1,2,2,2,-1,0,0,0,-1,0,0,0,-1,2,2,2,-1,2,2,2,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,1,1,1,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,2,2,2,-1,2,2,2,-1,2,2,2,-1,2,2,2,-1,2,2,2,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,2,2,2,-1,2,2,2,-1,2,2,2,-1,0,0,0,-1,0,0,0,-1,2,2,2,-1,2,2,2,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,3,3,3,-1,3,3,3,-1,0,0,0,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,3,3,3,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,3,3,3,-1,3,3,3,-1,0,0,0,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,3,3,3,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1])
IndexedFaceSet763.setCoordIndex([48,87,58,-1,91,92,59,-1,59,92,88,-1,88,93,231,-1,232,86,233,-1,86,89,233,-1,89,57,56,-1,49,55,57,-1,102,86,96,-1,86,90,96,-1,97,95,96,-1,97,127,95,-1,41,96,154,-1,41,102,96,-1,99,102,41,-1,153,99,41,-1,102,40,86,-1,234,235,236,-1,87,237,58,-1,56,57,91,-1,87,234,237,-1,234,236,237,-1,89,49,57,-1,49,50,55,-1,40,89,86,-1,89,56,233,-1,232,90,86,-1,90,97,96,-1,92,93,88,-1,93,94,231,-1,232,231,94,-1,97,90,232,-1,96,42,154,-1,95,42,96,-1,53,46,45,-1,53,45,51,-1,53,51,92,-1,92,51,52,-1,92,52,93,-1,94,93,52,-1,94,52,4,-1,97,232,94,-1,54,47,46,-1,54,46,53,-1,55,47,54,-1,50,47,55,-1,34,33,50,-1,34,50,49,-1,35,34,49,-1,35,49,89,-1,35,89,40,-1,99,39,102,-1,39,35,40,-1,31,34,35,-1,31,35,32,-1,14,32,35,-1,14,35,39,-1,14,39,98,-1,137,38,153,-1,38,99,153,-1,38,98,99,-1,37,238,239,-1,11,238,37,-1,101,37,36,-1,241,141,242,-1,10,12,242,-1,12,13,14,-1,12,14,243,-1,13,15,32,-1,13,32,14,-1,15,16,31,-1,15,31,32,-1,2,70,10,-1,2,10,141,-1,70,69,12,-1,70,12,10,-1,69,68,13,-1,69,13,12,-1,68,67,15,-1,68,15,13,-1,67,66,16,-1,67,16,15,-1,98,39,99,-1,101,11,37,-1,100,101,36,-1,36,244,240,-1,141,10,242,-1,12,243,242,-1,36,37,239,-1,36,239,244,-1,57,55,91,-1,55,54,91,-1,39,40,102,-1,123,103,120,-1,114,122,104,-1,115,122,114,-1,208,105,115,-1,210,119,211,-1,210,106,119,-1,116,107,106,-1,107,108,117,-1,126,119,109,-1,126,110,119,-1,126,95,125,-1,95,127,125,-1,154,126,111,-1,126,109,111,-1,111,109,112,-1,111,112,153,-1,119,113,109,-1,207,213,214,-1,123,209,103,-1,213,212,214,-1,209,214,103,-1,209,207,214,-1,107,117,106,-1,108,118,117,-1,119,106,113,-1,210,116,106,-1,119,110,211,-1,126,125,110,-1,115,105,122,-1,208,124,105,-1,124,208,211,-1,211,110,125,-1,154,42,126,-1,126,42,95,-1,168,128,121,-1,170,168,121,-1,122,170,121,-1,172,170,122,-1,105,172,122,-1,172,105,124,-1,4,172,124,-1,124,211,125,-1,128,130,129,-1,121,128,129,-1,129,130,108,-1,108,130,118,-1,118,131,132,-1,117,118,132,-1,117,132,133,-1,106,117,133,-1,113,106,133,-1,109,152,112,-1,113,133,152,-1,133,132,134,-1,135,133,134,-1,133,135,136,-1,152,133,136,-1,148,152,136,-1,153,138,137,-1,153,112,138,-1,112,148,138,-1,219,217,139,-1,36,240,149,-1,139,217,140,-1,149,139,151,-1,36,149,100,-1,220,141,241,-1,220,150,142,-1,136,143,150,-1,221,136,150,-1,135,144,143,-1,136,135,143,-1,134,158,144,-1,135,134,144,-1,142,161,2,-1,141,142,2,-1,150,145,161,-1,142,150,161,-1,143,146,145,-1,150,143,145,-1,144,147,146,-1,143,144,146,-1,158,160,147,-1,144,158,147,-1,112,152,148,-1,139,140,151,-1,149,151,100,-1,240,218,149,-1,220,142,141,-1,220,221,150,-1,219,139,149,-1,218,219,149,-1,104,108,107,-1,104,129,108,-1,109,113,152,-1,153,41,111,-1,129,104,122,-1,129,122,121,-1,91,54,92,-1,54,53,92,-1,97,94,127,-1,127,94,4,-1,125,127,124,-1,127,4,124,-1,154,111,41,-1,31,30,33,-1,31,33,34,-1,16,17,30,-1,16,30,31,-1,66,65,17,-1,66,17,16,-1,2,73,156,-1,2,156,70,-1,156,72,66,-1,156,66,67,-1,156,67,68,-1,156,68,69,-1,156,69,70,-1,72,71,65,-1,72,65,66,-1,17,18,30,-1,45,44,51,-1,51,44,43,-1,51,43,52,-1,52,43,1,-1,52,1,4,-1,245,246,27,-1,245,27,3,-1,246,247,28,-1,246,28,27,-1,248,22,29,-1,248,29,28,-1,248,28,247,-1,27,26,0,-1,27,0,3,-1,27,28,25,-1,27,25,26,-1,29,24,25,-1,29,25,28,-1,22,23,24,-1,22,24,29,-1,249,250,22,-1,249,22,248,-1,250,60,23,-1,250,23,22,-1,17,254,18,-1,65,254,17,-1,71,64,65,-1,63,74,75,-1,63,75,61,-1,64,255,254,-1,75,62,61,-1,62,76,60,-1,76,77,23,-1,76,23,60,-1,77,24,23,-1,77,78,25,-1,77,25,24,-1,78,84,26,-1,78,26,25,-1,84,192,0,-1,84,0,26,-1,84,83,193,-1,84,193,192,-1,79,83,84,-1,79,84,78,-1,76,79,78,-1,76,78,77,-1,80,83,79,-1,80,204,83,-1,75,81,80,-1,81,85,204,-1,81,204,80,-1,74,81,75,-1,74,82,81,-1,82,5,85,-1,82,85,81,-1,155,8,71,-1,155,71,72,-1,8,6,64,-1,8,64,71,-1,6,7,255,-1,6,255,64,-1,7,9,256,-1,7,256,255,-1,9,257,256,-1,73,155,156,-1,155,72,156,-1,204,193,83,-1,64,254,65,-1,131,157,134,-1,132,131,134,-1,157,159,158,-1,134,157,158,-1,159,206,160,-1,158,159,160,-1,203,73,2,-1,161,203,2,-1,160,162,203,-1,147,160,203,-1,146,147,203,-1,145,146,203,-1,161,145,203,-1,206,163,162,-1,160,206,162,-1,157,164,159,-1,170,169,168,-1,171,169,170,-1,172,171,170,-1,1,171,172,-1,4,1,172,-1,173,227,245,-1,3,173,245,-1,174,226,227,-1,173,174,227,-1,176,175,215,-1,174,176,215,-1,226,174,215,-1,0,177,173,-1,3,0,173,-1,178,174,173,-1,177,178,173,-1,178,179,176,-1,174,178,176,-1,179,180,175,-1,176,179,175,-1,175,225,216,-1,215,175,216,-1,180,181,225,-1,175,180,225,-1,164,228,159,-1,159,228,206,-1,206,185,163,-1,187,186,184,-1,183,187,184,-1,228,229,185,-1,183,182,187,-1,181,188,182,-1,180,189,188,-1,181,180,188,-1,180,179,189,-1,178,190,189,-1,179,178,189,-1,177,191,190,-1,178,177,190,-1,0,192,191,-1,177,0,191,-1,193,205,191,-1,192,193,191,-1,191,205,194,-1,190,191,194,-1,190,194,188,-1,189,190,188,-1,194,205,195,-1,205,204,195,-1,195,196,187,-1,204,85,196,-1,195,204,196,-1,187,196,186,-1,196,197,186,-1,85,5,197,-1,196,85,197,-1,163,198,202,-1,162,163,202,-1,185,199,198,-1,163,185,198,-1,229,200,199,-1,185,229,199,-1,230,201,200,-1,229,230,200,-1,230,257,201,-1,203,202,73,-1,203,162,202,-1,205,193,204,-1,206,228,185,-1,198,8,155,-1,198,155,202,-1,155,73,202,-1,199,6,8,-1,199,8,198,-1,7,6,199,-1,7,199,200,-1,201,9,7,-1,201,7,200,-1,201,257,9,-1,188,194,195,-1,188,195,182,-1,195,187,182,-1,80,79,76,-1,80,62,75,-1,80,76,62,-1,47,50,33,-1,131,118,130,-1,20,21,47,-1,21,46,47,-1,20,33,19,-1,20,47,33,-1,33,30,19,-1,30,18,19,-1,62,60,251,-1,60,250,251,-1,252,61,251,-1,61,62,251,-1,252,63,61,-1,252,253,63,-1,166,130,167,-1,130,128,167,-1,166,131,130,-1,166,165,131,-1,165,157,131,-1,165,164,157,-1,224,181,182,-1,224,225,181,-1,224,183,223,-1,224,182,183,-1,183,184,223,-1,184,222,223,-1])
IndexedFaceSet763.setCreaseAngle(0.7854)
Coordinate764 = Coordinate()
Coordinate764.setDEF("Face")
Coordinate764.setPoint([0,1.708,-0.0435,0,1.655,0.04322,0,1.486,0.02335,0,1.694,0.007789,0,1.631,0.051,0,1.524,-0.102,0.04,1.51,-0.07278,0.04029,1.514,-0.08254,0.03528,1.502,-0.05013,0.03479,1.517,-0.09269,0.0116,1.494,0.03382,0.01946,1.52,0.03421,0.02204,1.494,0.0272,0.02734,1.498,0.02215,0.02788,1.528,0.03084,0.0338,1.503,0.0124,0.04008,1.509,0.002821,0.05122,1.518,-0.02784,0.05867,1.544,-0.03316,0.06433,1.563,-0.03678,0.06732,1.583,-0.03683,0.06769,1.617,-0.03436,0.06641,1.637,-0.03046,0.06818,1.637,-0.04285,0.06308,1.666,-0.04036,0.05305,1.685,-0.03987,0.03136,1.7,-0.0413,0.02919,1.688,0.0091,0.05272,1.674,-0.001657,0.06061,1.66,-0.0101,0.05254,1.541,-0.01363,0.04099,1.527,0.008832,0.03528,1.524,0.02097,0.05792,1.557,-0.004307,0.04413,1.539,0.0149,0.03746,1.539,0.02656,0.003407,1.524,0.04155,0.01481,1.526,0.03912,0.005112,1.532,0.04358,0.02438,1.542,0.03578,0.02636,1.55,0.03808,0.006135,1.55,0.0545,0,1.559,0.05502,0.02958,1.651,0.03965,0.04847,1.643,0.02895,0.05856,1.63,0.01803,0.06182,1.614,0.008199,0.06194,1.6,0.002668,0.01489,1.583,0.04109,0.05282,1.569,0.02821,0.05767,1.58,0.0184,0.04643,1.625,0.03705,0.0264,1.628,0.04807,0.0556,1.609,0.02579,0.05467,1.599,0.02153,0.05316,1.589,0.0207,0.03603,1.58,0.03536,0.04597,1.586,0.02904,0.02106,1.592,0.03748,0.03428,1.595,0.03294,0.06808,1.617,-0.06112,0.06714,1.564,-0.07003,0.06993,1.594,-0.08238,0.05324,1.536,-0.05922,0.04904,1.521,-0.05132,0.04758,1.514,-0.03107,0.03539,1.503,-0.00093,0.02999,1.498,0.006194,0.02308,1.492,0.01628,0.01772,1.488,0.02135,0.01378,1.488,0.02484,0.04349,1.512,-0.03987,0.02308,1.499,-0.02088,0,1.487,-0.018,0.04795,1.531,-0.08973,0.05739,1.555,-0.0982,0.06815,1.622,-0.107,0.06872,1.655,-0.08466,0.05233,1.678,-0.09642,0.05334,1.631,-0.1239,0.05011,1.581,-0.1193,0.04359,1.551,-0.1067,0.03839,1.528,-0.09652,0.03399,1.636,-0.1304,0.03224,1.685,-0.1024,0,1.557,-0.1126,0.01864,1.566,0.04105,0.0249,1.58,0.0387,0.02735,1.596,0.03552,0.04317,1.564,0.03643,0.01246,1.577,0.04276,0.04354,1.59,0.02822,0.04557,1.601,0.03652,0.0291,1.603,0.04274,0.01856,1.6,0.04349,0,1.579,0.04893,0.01064,1.558,0.04476,0.005501,1.578,0.04574,0.01405,1.531,0.04152,0.01037,1.544,0.04266,0,1.515,0.03836,0.00797,1.515,0.03774,0.01824,1.55,0.04063,-0.0249,1.58,0.0387,-0.04354,1.59,0.02822,-0.0291,1.603,0.04274,-0.04317,1.564,0.03643,-0.04597,1.586,0.02904,-0.05316,1.589,0.0207,-0.01824,1.55,0.04063,-0.01246,1.577,0.04276,-0.006135,1.55,0.0545,-0.01037,1.544,0.04266,-0.02636,1.55,0.03808,-0.03428,1.595,0.03294,-0.02735,1.596,0.03552,-0.03603,1.58,0.03536,-0.05282,1.569,0.02821,-0.05767,1.58,0.0184,-0.01864,1.566,0.04105,-0.01489,1.583,0.04109,-0.0556,1.609,0.02579,-0.04557,1.601,0.03652,-0.02106,1.592,0.03748,-0.01856,1.6,0.04349,-0.005501,1.578,0.04574,-0.01064,1.558,0.04476,0,1.592,0.04694,-0.06182,1.614,0.008199,-0.05467,1.599,0.02153,-0.06194,1.6,0.002668,-0.05792,1.557,-0.004307,-0.04413,1.539,0.0149,-0.03746,1.539,0.02656,-0.04099,1.527,0.008832,-0.03528,1.524,0.02097,-0.02788,1.528,0.03084,0,1.53,0.04236,-0.005112,1.532,0.04358,-0.01481,1.526,0.03912,-0.01946,1.52,0.03421,0,1.495,0.0348,-0.0116,1.494,0.03382,-0.02734,1.498,0.02215,-0.0338,1.503,0.0124,-0.01772,1.488,0.02135,-0.02308,1.492,0.01628,-0.02999,1.498,0.006194,-0.01405,1.531,0.04152,-0.003407,1.524,0.04155,-0.02204,1.494,0.0272,-0.00797,1.515,0.03774,-0.02438,1.542,0.03578,0,1.543,0.04432,0,1.555,0.05692,0.02295,1.492,-0.02694,0.007322,1.489,-0.01677,-0.05254,1.541,-0.01363,-0.04008,1.509,0.002821,-0.05122,1.518,-0.02784,-0.03539,1.503,-0.00093,-0.01378,1.488,0.02484,-0.02308,1.499,-0.02088,-0.04349,1.512,-0.03987,-0.05867,1.544,-0.03316,-0.06433,1.563,-0.03678,-0.06732,1.583,-0.03683,-0.06769,1.617,-0.03436,-0.05856,1.63,0.01803,-0.04847,1.643,0.02895,-0.04643,1.625,0.03705,-0.02958,1.651,0.03965,-0.0264,1.628,0.04807,-0.02919,1.688,0.0091,-0.05272,1.674,-0.001657,-0.06641,1.637,-0.03046,-0.06061,1.66,-0.0101,-0.03136,1.7,-0.0413,-0.05305,1.685,-0.03987,-0.06308,1.666,-0.04036,-0.06818,1.637,-0.04285,-0.06808,1.617,-0.06112,-0.06993,1.594,-0.08238,-0.06714,1.564,-0.07003,-0.05324,1.536,-0.05922,-0.04904,1.521,-0.05132,-0.04795,1.531,-0.08973,-0.05739,1.555,-0.0982,-0.06815,1.622,-0.107,-0.06872,1.655,-0.08466,-0.05233,1.678,-0.09642,-0.03224,1.685,-0.1024,0,1.69,-0.1047,0,1.64,-0.1342,-0.05334,1.631,-0.1239,-0.05011,1.581,-0.1193,-0.04359,1.551,-0.1067,-0.03839,1.528,-0.09652,-0.03528,1.502,-0.05013,-0.04,1.51,-0.07278,-0.04029,1.514,-0.08254,-0.03479,1.517,-0.09269,-0.02295,1.492,-0.02694,-0.007322,1.489,-0.01677,0,1.588,-0.1329,-0.03399,1.636,-0.1304,-0.04758,1.514,-0.03107,-0.03428,1.595,0.03294,-0.02106,1.592,0.03748,-0.02735,1.596,0.03552,-0.0249,1.58,0.0387,-0.01489,1.583,0.04109,-0.04597,1.586,0.02904,-0.04354,1.59,0.02822,-0.03603,1.58,0.03536,-0.05856,1.63,0.01803,-0.06182,1.614,0.008199,-0.02788,1.528,0.03084,-0.005112,1.532,0.04358,-0.01405,1.531,0.04152,-0.00797,1.515,0.03774,-0.01946,1.52,0.03421,-0.05867,1.544,-0.03316,-0.06433,1.563,-0.03678,-0.06732,1.583,-0.03683,-0.06769,1.617,-0.03436,-0.04847,1.643,0.02895,-0.02958,1.651,0.03965,-0.05324,1.536,-0.05922,-0.04795,1.531,-0.08973,-0.03839,1.528,-0.09652,0.02106,1.592,0.03748,0.01489,1.583,0.04109,0.0249,1.58,0.0387,0.03603,1.58,0.03536,0.04354,1.59,0.02822,0.03428,1.595,0.03294,0.02735,1.596,0.03552,0.02788,1.528,0.03084,0.01405,1.531,0.04152,0,1.53,0.04236,0,1.515,0.03836,0.00797,1.515,0.03774,0.01946,1.52,0.03421,0.005112,1.532,0.04358,0,1.655,0.04322,0.02958,1.651,0.03965,0.04847,1.643,0.02895,0.05856,1.63,0.01803,0.06182,1.614,0.008199,0.06769,1.617,-0.03436,0.06732,1.583,-0.03683,0.06433,1.563,-0.03678,0.05867,1.544,-0.03316,0.05324,1.536,-0.05922,0.04795,1.531,-0.08973,0.03839,1.528,-0.09652,0,1.524,-0.102])

IndexedFaceSet763.setCoord(Coordinate764)
Color765 = Color()
Color765.setColor([0.749,0.601,0.462,0.1735,0.2602,0.749,0.6364,0.133,0.1526,0.4545,0.2759,0.1902])

IndexedFaceSet763.setColor(Color765)

Shape760.setGeometry(IndexedFaceSet763)

fieldValue759.addChildren(Shape760)

ProtoInstance757.addFieldValue(fieldValue759)

fieldValue756.addChildren(ProtoInstance757)

ProtoInstance753.addFieldValue(fieldValue756)

fieldValue744.addChildren(ProtoInstance753)

ProtoInstance741.addFieldValue(fieldValue744)

fieldValue652.addChildren(ProtoInstance741)

ProtoInstance649.addFieldValue(fieldValue652)

fieldValue564.addChildren(ProtoInstance649)

ProtoInstance561.addFieldValue(fieldValue564)

fieldValue560.addChildren(ProtoInstance561)
Group766 = Group()

fieldValue560.addChildren(Group766)

ProtoInstance556.addFieldValue(fieldValue560)
fieldValue767 = fieldValue()
fieldValue767.setName("joints")
ProtoInstance768 = ProtoInstance()
ProtoInstance768.setUSE("Nancy_hanim_humanoid_root")

fieldValue767.addChildren(ProtoInstance768)
ProtoInstance769 = ProtoInstance()
ProtoInstance769.setUSE("Nancy_hanim_sacroiliac")

fieldValue767.addChildren(ProtoInstance769)
ProtoInstance770 = ProtoInstance()
ProtoInstance770.setUSE("Nancy_hanim_l_hip")

fieldValue767.addChildren(ProtoInstance770)
ProtoInstance771 = ProtoInstance()
ProtoInstance771.setUSE("Nancy_hanim_l_knee")

fieldValue767.addChildren(ProtoInstance771)
ProtoInstance772 = ProtoInstance()
ProtoInstance772.setUSE("Nancy_hanim_l_ankle")

fieldValue767.addChildren(ProtoInstance772)
ProtoInstance773 = ProtoInstance()
ProtoInstance773.setUSE("Nancy_hanim_r_hip")

fieldValue767.addChildren(ProtoInstance773)
ProtoInstance774 = ProtoInstance()
ProtoInstance774.setUSE("Nancy_hanim_r_knee")

fieldValue767.addChildren(ProtoInstance774)
ProtoInstance775 = ProtoInstance()
ProtoInstance775.setUSE("Nancy_hanim_r_ankle")

fieldValue767.addChildren(ProtoInstance775)
ProtoInstance776 = ProtoInstance()
ProtoInstance776.setUSE("Nancy_hanim_vl1")

fieldValue767.addChildren(ProtoInstance776)
ProtoInstance777 = ProtoInstance()
ProtoInstance777.setUSE("Nancy_hanim_l_shoulder")

fieldValue767.addChildren(ProtoInstance777)
ProtoInstance778 = ProtoInstance()
ProtoInstance778.setUSE("Nancy_hanim_l_elbow")

fieldValue767.addChildren(ProtoInstance778)
ProtoInstance779 = ProtoInstance()
ProtoInstance779.setUSE("Nancy_hanim_l_wrist")

fieldValue767.addChildren(ProtoInstance779)
ProtoInstance780 = ProtoInstance()
ProtoInstance780.setUSE("Nancy_hanim_r_shoulder")

fieldValue767.addChildren(ProtoInstance780)
ProtoInstance781 = ProtoInstance()
ProtoInstance781.setUSE("Nancy_hanim_r_elbow")

fieldValue767.addChildren(ProtoInstance781)
ProtoInstance782 = ProtoInstance()
ProtoInstance782.setUSE("Nancy_hanim_r_wrist")

fieldValue767.addChildren(ProtoInstance782)
ProtoInstance783 = ProtoInstance()
ProtoInstance783.setUSE("Nancy_hanim_vc4")

fieldValue767.addChildren(ProtoInstance783)
ProtoInstance784 = ProtoInstance()
ProtoInstance784.setUSE("Nancy_hanim_skullbase")

fieldValue767.addChildren(ProtoInstance784)

ProtoInstance556.addFieldValue(fieldValue767)
fieldValue785 = fieldValue()
fieldValue785.setName("segments")
ProtoInstance786 = ProtoInstance()
ProtoInstance786.setUSE("Nancy_hanim_pelvis")

fieldValue785.addChildren(ProtoInstance786)
ProtoInstance787 = ProtoInstance()
ProtoInstance787.setUSE("Nancy_hanim_l_thigh")

fieldValue785.addChildren(ProtoInstance787)
ProtoInstance788 = ProtoInstance()
ProtoInstance788.setUSE("Nancy_hanim_l_calf")

fieldValue785.addChildren(ProtoInstance788)
ProtoInstance789 = ProtoInstance()
ProtoInstance789.setUSE("Nancy_hanim_l_hindfoot")

fieldValue785.addChildren(ProtoInstance789)
ProtoInstance790 = ProtoInstance()
ProtoInstance790.setUSE("Nancy_hanim_r_thigh")

fieldValue785.addChildren(ProtoInstance790)
ProtoInstance791 = ProtoInstance()
ProtoInstance791.setUSE("Nancy_hanim_r_calf")

fieldValue785.addChildren(ProtoInstance791)
ProtoInstance792 = ProtoInstance()
ProtoInstance792.setUSE("Nancy_hanim_r_hindfoot")

fieldValue785.addChildren(ProtoInstance792)
ProtoInstance793 = ProtoInstance()
ProtoInstance793.setUSE("Nancy_hanim_c7")

fieldValue785.addChildren(ProtoInstance793)
ProtoInstance794 = ProtoInstance()
ProtoInstance794.setUSE("Nancy_hanim_l_upperarm")

fieldValue785.addChildren(ProtoInstance794)
ProtoInstance795 = ProtoInstance()
ProtoInstance795.setUSE("Nancy_hanim_l_forearm")

fieldValue785.addChildren(ProtoInstance795)
ProtoInstance796 = ProtoInstance()
ProtoInstance796.setUSE("Nancy_hanim_l_hand")

fieldValue785.addChildren(ProtoInstance796)
ProtoInstance797 = ProtoInstance()
ProtoInstance797.setUSE("Nancy_hanim_r_upperarm")

fieldValue785.addChildren(ProtoInstance797)
ProtoInstance798 = ProtoInstance()
ProtoInstance798.setUSE("Nancy_hanim_r_forearm")

fieldValue785.addChildren(ProtoInstance798)
ProtoInstance799 = ProtoInstance()
ProtoInstance799.setUSE("Nancy_hanim_r_hand")

fieldValue785.addChildren(ProtoInstance799)
ProtoInstance800 = ProtoInstance()
ProtoInstance800.setUSE("Nancy_hanim_c4")

fieldValue785.addChildren(ProtoInstance800)
ProtoInstance801 = ProtoInstance()
ProtoInstance801.setUSE("Nancy_hanim_skull")

fieldValue785.addChildren(ProtoInstance801)

ProtoInstance556.addFieldValue(fieldValue785)

Switch291.addChildren(ProtoInstance556)
HAnimHumanoid802 = HAnimHumanoid()
HAnimHumanoid802.setName("Humanoid")
HAnimHumanoid802.setDEF("Boxman_Humanoid")
HAnimHumanoid802.setVersion("1.0")
HAnimJoint803 = HAnimJoint()
HAnimJoint803.setName("humanoid_root")
HAnimJoint803.setDEF("Boxman_humanoid_root")
HAnimJoint803.setCenter([0,0.9723,-0.0728])
HAnimJoint803.setSkinCoordIndex([0,1,2,3,4,5,6,7,8,9,10,11])
HAnimJoint803.setSkinCoordWeight([1,1,1,1,1,1,1,1,1,1,1,1])
HAnimJoint803.setStiffness([0,0,0])
HAnimSegment804 = HAnimSegment()
HAnimSegment804.setName("sacrum")
HAnimSegment804.setDEF("Boxman_sacrum")
Inline805 = Inline()
Inline805.setUrl(["centres/sacrum.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/centres/sacrum.wrl"])

HAnimSegment804.addChildren(Inline805)

HAnimJoint803.addChildren(HAnimSegment804)
HAnimJoint806 = HAnimJoint()
HAnimJoint806.setName("l_hip")
HAnimJoint806.setDEF("Boxman_l_hip")
HAnimJoint806.setCenter([0.0956,0.9364,0])
HAnimJoint806.setSkinCoordIndex([12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43])
HAnimJoint806.setSkinCoordWeight([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5])
HAnimJoint806.setStiffness([0,0,0])
HAnimSegment807 = HAnimSegment()
HAnimSegment807.setName("l_thigh")
HAnimSegment807.setDEF("Boxman_l_thigh")
Inline808 = Inline()
Inline808.setUrl(["centres/l_thigh.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/centres/l_thigh.wrl"])

HAnimSegment807.addChildren(Inline808)

HAnimJoint806.addChildren(HAnimSegment807)
HAnimJoint809 = HAnimJoint()
HAnimJoint809.setName("l_knee")
HAnimJoint809.setDEF("Boxman_l_knee")
HAnimJoint809.setCenter([0.0956,0.5095,-0.0036])
HAnimJoint809.setSkinCoordIndex([36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63])
HAnimJoint809.setSkinCoordWeight([0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
HAnimJoint809.setStiffness([0,0,0])
HAnimSegment810 = HAnimSegment()
HAnimSegment810.setName("l_calf")
HAnimSegment810.setDEF("Boxman_l_calf")
Inline811 = Inline()
Inline811.setUrl(["centres/l_calf.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/centres/l_calf.wrl"])

HAnimSegment810.addChildren(Inline811)

HAnimJoint809.addChildren(HAnimSegment810)
HAnimJoint812 = HAnimJoint()
HAnimJoint812.setName("l_ankle")
HAnimJoint812.setDEF("Boxman_l_ankle")
HAnimJoint812.setCenter([0.0946,0.0762,-0.0261])
HAnimJoint812.setSkinCoordIndex([64,65,66,67,68,69,70,71])
HAnimJoint812.setSkinCoordWeight([1,1,1,1,1,1,1,1])
HAnimJoint812.setStiffness([0,0,0])
HAnimSegment813 = HAnimSegment()
HAnimSegment813.setName("l_hindfoot")
HAnimSegment813.setDEF("Boxman_l_hindfoot")
Inline814 = Inline()
Inline814.setUrl(["centres/l_hindfoot.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/centres/l_hindfoot.wrl"])

HAnimSegment813.addChildren(Inline814)

HAnimJoint812.addChildren(HAnimSegment813)
HAnimJoint815 = HAnimJoint()
HAnimJoint815.setName("l_midtarsal")
HAnimJoint815.setDEF("Boxman_l_midtarsal")
HAnimJoint815.setCenter([0.1079,0.0317,0.067])
HAnimJoint815.setSkinCoordIndex([72,73,74,75,76,77,78,79])
HAnimJoint815.setSkinCoordWeight([1,1,1,1,1,1,1,1])
HAnimJoint815.setStiffness([0,0,0])
HAnimSegment816 = HAnimSegment()
HAnimSegment816.setName("l_middistal")
HAnimSegment816.setDEF("Boxman_l_middistal")
Inline817 = Inline()
Inline817.setUrl(["centres/l_middistal.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/centres/l_middistal.wrl"])

HAnimSegment816.addChildren(Inline817)
HAnimSite818 = HAnimSite()
HAnimSite818.setName("l_middistal_tip")
HAnimSite818.setDEF("Boxman_l_middistal_tip")
HAnimSite818.setTranslation([0.095,0.0005,0.1924])

HAnimSegment816.addChildren(HAnimSite818)
Inline819 = Inline()
Inline819.setUrl(["centres/l_middistal_tip.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/centres/l_middistal_tip.wrl"])

HAnimSegment816.addChildren(Inline819)

HAnimJoint815.addChildren(HAnimSegment816)

HAnimJoint812.addChildren(HAnimJoint815)

HAnimJoint809.addChildren(HAnimJoint812)

HAnimJoint806.addChildren(HAnimJoint809)

HAnimJoint803.addChildren(HAnimJoint806)
HAnimJoint820 = HAnimJoint()
HAnimJoint820.setName("r_hip")
HAnimJoint820.setDEF("Boxman_r_hip")
HAnimJoint820.setCenter([-0.0956,0.9364,0])
HAnimJoint820.setSkinCoordIndex([80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111])
HAnimJoint820.setSkinCoordWeight([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5])
HAnimJoint820.setStiffness([0,0,0])
HAnimSegment821 = HAnimSegment()
HAnimSegment821.setName("r_thigh")
HAnimSegment821.setDEF("Boxman_r_thigh")
Inline822 = Inline()
Inline822.setUrl(["centres/r_thigh.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/centres/r_thigh.wrl"])

HAnimSegment821.addChildren(Inline822)

HAnimJoint820.addChildren(HAnimSegment821)
HAnimJoint823 = HAnimJoint()
HAnimJoint823.setName("r_knee")
HAnimJoint823.setDEF("Boxman_r_knee")
HAnimJoint823.setCenter([-0.0956,0.5095,-0.0036])
HAnimJoint823.setSkinCoordIndex([104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131])
HAnimJoint823.setSkinCoordWeight([0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
HAnimJoint823.setStiffness([0,0,0])
HAnimSegment824 = HAnimSegment()
HAnimSegment824.setName("r_calf")
HAnimSegment824.setDEF("Boxman_r_calf")
Inline825 = Inline()
Inline825.setUrl(["centres/r_calf.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/centres/r_calf.wrl"])

HAnimSegment824.addChildren(Inline825)

HAnimJoint823.addChildren(HAnimSegment824)
HAnimJoint826 = HAnimJoint()
HAnimJoint826.setName("r_ankle")
HAnimJoint826.setDEF("Boxman_r_ankle")
HAnimJoint826.setCenter([-0.0946,0.0762,-0.0261])
HAnimJoint826.setSkinCoordIndex([132,133,134,135,136,137,138,139])
HAnimJoint826.setSkinCoordWeight([1,1,1,1,1,1,1,1])
HAnimJoint826.setStiffness([0,0,0])
HAnimSegment827 = HAnimSegment()
HAnimSegment827.setName("r_hindfoot")
HAnimSegment827.setDEF("Boxman_r_hindfoot")
Inline828 = Inline()
Inline828.setUrl(["centres/r_hindfoot.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/centres/r_hindfoot.wrl"])

HAnimSegment827.addChildren(Inline828)

HAnimJoint826.addChildren(HAnimSegment827)
HAnimJoint829 = HAnimJoint()
HAnimJoint829.setName("r_midtarsal")
HAnimJoint829.setDEF("Boxman_r_midtarsal")
HAnimJoint829.setCenter([-0.1079,0.0317,0.067])
HAnimJoint829.setSkinCoordIndex([140,141,142,143,144,145,146,147])
HAnimJoint829.setSkinCoordWeight([1,1,1,1,1,1,1,1])
HAnimJoint829.setStiffness([0,0,0])
HAnimSegment830 = HAnimSegment()
HAnimSegment830.setName("r_middistal")
HAnimSegment830.setDEF("Boxman_r_middistal")
Inline831 = Inline()
Inline831.setUrl(["centres/r_middistal.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/centres/r_middistal.wrl"])

HAnimSegment830.addChildren(Inline831)
HAnimSite832 = HAnimSite()
HAnimSite832.setName("r_middistal_tip")
HAnimSite832.setDEF("Boxman_r_middistal_tip")
HAnimSite832.setTranslation([-0.095,0.0005,0.1924])

HAnimSegment830.addChildren(HAnimSite832)
Inline833 = Inline()
Inline833.setUrl(["centres/r_middistal_tip.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/centres/r_middistal_tip.wrl"])

HAnimSegment830.addChildren(Inline833)

HAnimJoint829.addChildren(HAnimSegment830)

HAnimJoint826.addChildren(HAnimJoint829)

HAnimJoint823.addChildren(HAnimJoint826)

HAnimJoint820.addChildren(HAnimJoint823)

HAnimJoint803.addChildren(HAnimJoint820)
HAnimJoint834 = HAnimJoint()
HAnimJoint834.setName("vl5")
HAnimJoint834.setDEF("Boxman_vl5")
HAnimJoint834.setCenter([0,1.0817,-0.0728])
HAnimJoint834.setSkinCoordIndex([148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167])
HAnimJoint834.setSkinCoordWeight([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
HAnimJoint834.setStiffness([0,0,0])
HAnimSegment835 = HAnimSegment()
HAnimSegment835.setName("l5")
HAnimSegment835.setDEF("Boxman_l5")
Inline836 = Inline()
Inline836.setUrl(["centres/l5.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/centres/l5.wrl"])

HAnimSegment835.addChildren(Inline836)

HAnimJoint834.addChildren(HAnimSegment835)
HAnimJoint837 = HAnimJoint()
HAnimJoint837.setName("skullbase")
HAnimJoint837.setDEF("Boxman_skullbase")
HAnimJoint837.setCenter([0,1.644,0.036])
HAnimJoint837.setSkinCoordIndex([168,169,170,171,172,173,174,175])
HAnimJoint837.setSkinCoordWeight([1,1,1,1,1,1,1,1])
HAnimJoint837.setStiffness([0,0,0])
HAnimSegment838 = HAnimSegment()
HAnimSegment838.setName("skull")
HAnimSegment838.setDEF("Boxman_skull")
Inline839 = Inline()
Inline839.setUrl(["centres/skull.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/centres/skull.wrl"])

HAnimSegment838.addChildren(Inline839)
HAnimSite840 = HAnimSite()
HAnimSite840.setName("skull_tip")
HAnimSite840.setDEF("Boxman_skull_tip")
HAnimSite840.setTranslation([-0.0029,1.7771,0.0274])

HAnimSegment838.addChildren(HAnimSite840)
Inline841 = Inline()
Inline841.setUrl(["centres/skull_tip.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/centres/skull_tip.wrl"])

HAnimSegment838.addChildren(Inline841)

HAnimJoint837.addChildren(HAnimSegment838)

HAnimJoint834.addChildren(HAnimJoint837)
HAnimJoint842 = HAnimJoint()
HAnimJoint842.setName("l_shoulder")
HAnimJoint842.setDEF("Boxman_l_shoulder")
HAnimJoint842.setCenter([0.1968,1.4642,-0.0265])
HAnimJoint842.setSkinCoordIndex([176,177,178,179,180,181,182,183])
HAnimJoint842.setSkinCoordWeight([1,1,1,1,1,1,1,1])
HAnimJoint842.setStiffness([0,0,0])
HAnimSegment843 = HAnimSegment()
HAnimSegment843.setName("l_upperarm")
HAnimSegment843.setDEF("Boxman_l_upperarm")
Inline844 = Inline()
Inline844.setUrl(["centres/l_upperarm.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/centres/l_upperarm.wrl"])

HAnimSegment843.addChildren(Inline844)

HAnimJoint842.addChildren(HAnimSegment843)
HAnimJoint845 = HAnimJoint()
HAnimJoint845.setName("l_elbow")
HAnimJoint845.setDEF("Boxman_l_elbow")
HAnimJoint845.setCenter([0.1982,1.1622,-0.0557])
HAnimJoint845.setSkinCoordIndex([184,185,186,187,188,189,190,191])
HAnimJoint845.setSkinCoordWeight([1,1,1,1,1,1,1,1])
HAnimJoint845.setStiffness([0,0,0])
HAnimSegment846 = HAnimSegment()
HAnimSegment846.setName("l_forearm")
HAnimSegment846.setDEF("Boxman_l_forearm")
Inline847 = Inline()
Inline847.setUrl(["centres/l_forearm.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/centres/l_forearm.wrl"])

HAnimSegment846.addChildren(Inline847)

HAnimJoint845.addChildren(HAnimSegment846)
HAnimJoint848 = HAnimJoint()
HAnimJoint848.setName("l_wrist")
HAnimJoint848.setDEF("Boxman_l_wrist")
HAnimJoint848.setCenter([0.1972,0.8929,-0.069])
HAnimJoint848.setSkinCoordIndex([192,193,194,195,196,197,198,199])
HAnimJoint848.setSkinCoordWeight([1,1,1,1,1,1,1,1])
HAnimJoint848.setStiffness([0,0,0])
HAnimSegment849 = HAnimSegment()
HAnimSegment849.setName("l_hand")
HAnimSegment849.setDEF("Boxman_l_hand")
Inline850 = Inline()
Inline850.setUrl(["centres/l_hand.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/centres/l_hand.wrl"])

HAnimSegment849.addChildren(Inline850)
HAnimSite851 = HAnimSite()
HAnimSite851.setName("l_hand_tip")
HAnimSite851.setDEF("Boxman_l_hand_tip")
HAnimSite851.setTranslation([0.1912,0.6976,-0.071])

HAnimSegment849.addChildren(HAnimSite851)
Inline852 = Inline()
Inline852.setUrl(["centres/l_hand_tip.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/centres/l_hand_tip.wrl"])

HAnimSegment849.addChildren(Inline852)

HAnimJoint848.addChildren(HAnimSegment849)

HAnimJoint845.addChildren(HAnimJoint848)

HAnimJoint842.addChildren(HAnimJoint845)

HAnimJoint834.addChildren(HAnimJoint842)
HAnimJoint853 = HAnimJoint()
HAnimJoint853.setName("r_shoulder")
HAnimJoint853.setDEF("Boxman_r_shoulder")
HAnimJoint853.setCenter([-0.1968,1.4642,-0.0265])
HAnimJoint853.setSkinCoordIndex([200,201,202,203,204,205,206,207])
HAnimJoint853.setSkinCoordWeight([1,1,1,1,1,1,1,1])
HAnimJoint853.setStiffness([0,0,0])
HAnimSegment854 = HAnimSegment()
HAnimSegment854.setName("r_upperarm")
HAnimSegment854.setDEF("Boxman_r_upperarm")
Inline855 = Inline()
Inline855.setUrl(["centres/r_upperarm.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/centres/r_upperarm.wrl"])

HAnimSegment854.addChildren(Inline855)

HAnimJoint853.addChildren(HAnimSegment854)
HAnimJoint856 = HAnimJoint()
HAnimJoint856.setName("r_elbow")
HAnimJoint856.setDEF("Boxman_r_elbow")
HAnimJoint856.setCenter([-0.1982,1.1622,-0.0557])
HAnimJoint856.setSkinCoordIndex([208,209,210,211,212,213,214,215])
HAnimJoint856.setSkinCoordWeight([1,1,1,1,1,1,1,1])
HAnimJoint856.setStiffness([0,0,0])
HAnimSegment857 = HAnimSegment()
HAnimSegment857.setName("r_forearm")
HAnimSegment857.setDEF("Boxman_r_forearm")
Inline858 = Inline()
Inline858.setUrl(["centres/r_forearm.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/centres/r_forearm.wrl"])

HAnimSegment857.addChildren(Inline858)

HAnimJoint856.addChildren(HAnimSegment857)
HAnimJoint859 = HAnimJoint()
HAnimJoint859.setName("r_wrist")
HAnimJoint859.setDEF("Boxman_r_wrist")
HAnimJoint859.setCenter([-0.1972,0.8929,-0.069])
HAnimJoint859.setSkinCoordIndex([216,217,218,219,220,221,222,223])
HAnimJoint859.setSkinCoordWeight([1,1,1,1,1,1,1,1])
HAnimJoint859.setStiffness([0,0,0])
HAnimSegment860 = HAnimSegment()
HAnimSegment860.setName("r_hand")
HAnimSegment860.setDEF("Boxman_r_hand")
Inline861 = Inline()
Inline861.setUrl(["centres/r_hand.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/centres/r_hand.wrl"])

HAnimSegment860.addChildren(Inline861)
HAnimSite862 = HAnimSite()
HAnimSite862.setName("r_hand_tip")
HAnimSite862.setDEF("Boxman_r_hand_tip")
HAnimSite862.setTranslation([-0.1912,0.6976,-0.071])

HAnimSegment860.addChildren(HAnimSite862)
Inline863 = Inline()
Inline863.setUrl(["centres/r_hand_tip.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/CharactersLegacy/centres/r_hand_tip.wrl"])

HAnimSegment860.addChildren(Inline863)

HAnimJoint859.addChildren(HAnimSegment860)

HAnimJoint856.addChildren(HAnimJoint859)

HAnimJoint853.addChildren(HAnimJoint856)

HAnimJoint834.addChildren(HAnimJoint853)

HAnimJoint803.addChildren(HAnimJoint834)

HAnimHumanoid802.setSkeleton(HAnimJoint803)
## sacrum (12) # l_thigh (28) # l_calf (24) # l_hindfoot (8) # l_middistal (8) # r_thigh (28) # r_calf (24) # r_hindfoot (8) # r_middistal (8) # l5 (20) # skull (8) # l_upperarm (8) # l_forearm (8) # l_hand (8) # r_upperarm (8) # r_forearm (8) # r_hand (8)
Coordinate864 = Coordinate()
Coordinate864.setDEF("SKINCOORD")
Coordinate864.setPoint([-0.05,1,0.05,0.05,1,0.05,0.03,0.97,-0.1,-0.03,0.97,-0.1,0.03,0.94,-0.075,-0.03,0.94,-0.075,0,0.92,0,0,0.94,0.03,-0.12,1.06,0.05,0.12,1.06,0.05,0.12,1.06,-0.1,-0.12,1.06,-0.1,0.0456,0.9364,0.05,0.1456,0.9364,0.05,0.1456,0.9364,-0.05,0.0456,0.9364,-0.05,0.0456,0.9,0.05,0.1456,0.9,0.05,0.1456,0.9,-0.05,0.0456,0.9,-0.05,0.0456,0.8,0.05,0.1456,0.8,0.05,0.1456,0.8,-0.05,0.0456,0.8,-0.05,0.0456,0.7,0.05,0.1456,0.7,0.05,0.1456,0.7,-0.05,0.0456,0.7,-0.05,0.0456,0.6,0.05,0.1456,0.6,0.05,0.1456,0.6,-0.05,0.0456,0.6,-0.05,0.0456,0.55,0.05,0.1456,0.55,0.05,0.1456,0.55,-0.05,0.0456,0.55,-0.05,0.0456,0.52,0.05,0.1456,0.52,0.05,0.1456,0.52,-0.05,0.0456,0.52,-0.05,0.0456,0.5,0.05,0.1456,0.5,0.05,0.1456,0.5,-0.05,0.0456,0.5,-0.05,0.0454,0.43,0.045,0.1454,0.43,0.045,0.1454,0.43,-0.055,0.0454,0.43,-0.055,0.0452,0.36,0.04,0.1452,0.36,0.04,0.1452,0.36,-0.06,0.0452,0.36,-0.06,0.045,0.29,0.035,0.145,0.29,0.035,0.145,0.29,-0.065,0.045,0.29,-0.065,0.0448,0.21,0.03,0.1448,0.21,0.03,0.1448,0.21,-0.07,0.0448,0.21,-0.07,0.0446,0.1262,0.025,0.1446,0.1262,0.025,0.1446,0.1262,-0.075,0.0446,0.1262,-0.075,0.0446,0.0762,0.025,0.1446,0.0762,0.025,0.1446,0,-0.075,0.0446,0,-0.075,0.0446,0.0562,0.057,0.1446,0.0562,0.057,0.1446,0,0.057,0.0446,0,0.057,0.0446,0.0562,0.087,0.1446,0.0562,0.087,0.1446,0,0.087,0.0446,0,0.087,0.0446,0.0562,0.1924,0.1446,0.0562,0.1924,0.1446,0,0.1924,0.0446,0,0.1924,-0.0456,0.9364,0.05,-0.1456,0.9364,0.05,-0.1456,0.9364,-0.05,-0.0456,0.9364,-0.05,-0.0456,0.9,0.05,-0.1456,0.9,0.05,-0.1456,0.9,-0.05,-0.0456,0.9,-0.05,-0.0456,0.8,0.05,-0.1456,0.8,0.05,-0.1456,0.8,-0.05,-0.0456,0.8,-0.05,-0.0456,0.7,0.05,-0.1456,0.7,0.05,-0.1456,0.7,-0.05,-0.0456,0.7,-0.05,-0.0456,0.6,0.05,-0.1456,0.6,0.05,-0.1456,0.6,-0.05,-0.0456,0.6,-0.05,-0.0456,0.55,0.05,-0.1456,0.55,0.05,-0.1456,0.55,-0.05,-0.0456,0.55,-0.05,-0.0456,0.52,0.05,-0.1456,0.52,0.05,-0.1456,0.52,-0.05,-0.0456,0.52,-0.05,-0.0456,0.5,0.05,-0.1456,0.5,0.05,-0.1456,0.5,-0.05,-0.0456,0.5,-0.05,-0.0454,0.43,0.045,-0.1454,0.43,0.045,-0.1454,0.43,-0.055,-0.0454,0.43,-0.055,-0.0452,0.36,0.04,-0.1452,0.36,0.04,-0.1452,0.36,-0.06,-0.0452,0.36,-0.06,-0.045,0.29,0.035,-0.145,0.29,0.035,-0.145,0.29,-0.065,-0.045,0.29,-0.065,-0.0448,0.21,0.03,-0.1448,0.21,0.03,-0.1448,0.21,-0.07,-0.0448,0.21,-0.07,-0.0446,0.1262,0.025,-0.1446,0.1262,0.025,-0.1446,0.1262,-0.075,-0.0446,0.1262,-0.075,-0.0446,0.0762,0.025,-0.1446,0.0762,0.025,-0.1446,0,-0.075,-0.0446,0,-0.075,-0.0446,0.0562,0.057,-0.1446,0.0562,0.057,-0.1446,0,0.057,-0.0446,0,0.057,-0.0446,0.0562,0.087,-0.1446,0.0562,0.087,-0.1446,0,0.087,-0.0446,0,0.087,-0.0446,0.0562,0.1924,-0.1446,0.0562,0.1924,-0.1446,0,0.1924,-0.0446,0,0.1924,-0.12,1.1,0.05,0.12,1.1,0.05,0.12,1.1,-0.1,-0.12,1.1,-0.1,-0.14,1.42,0.045,0.14,1.42,0.045,0.14,1.42,-0.09,-0.14,1.42,-0.09,-0.24,1.52,0.035,0.24,1.52,0.035,0.24,1.52,-0.09,-0.24,1.52,-0.09,-0.05,1.56,0.03,0.05,1.56,0.03,0.05,1.56,-0.06,-0.05,1.56,-0.06,-0.05,1.6,0.06,0.05,1.6,0.06,0.05,1.62,-0.03,-0.05,1.62,-0.03,-0.07,1.777,0.13,0.07,1.777,0.13,0.07,1.777,-0.03,-0.07,1.777,-0.03,-0.07,1.6,0.13,0.07,1.6,0.13,0.07,1.66,-0.03,-0.07,1.66,-0.03,0.16,1.42,0.015,0.24,1.5,0.015,0.24,1.5,-0.075,0.16,1.42,-0.075,0.17,1.18,-0.025,0.23,1.18,-0.025,0.23,1.18,-0.085,0.17,1.18,-0.085,0.17,1.14,-0.025,0.23,1.14,-0.025,0.23,1.14,-0.085,0.17,1.14,-0.085,0.18,0.91,-0.05,0.22,0.91,-0.05,0.22,0.91,-0.09,0.18,0.91,-0.09,0.18,0.87,-0.02,0.22,0.87,-0.02,0.22,0.87,-0.1,0.18,0.87,-0.1,0.18,0.6976,-0.02,0.22,0.6976,-0.02,0.22,0.6976,-0.1,0.18,0.6976,-0.1,-0.16,1.42,0.015,-0.24,1.5,0.015,-0.24,1.5,-0.075,-0.16,1.42,-0.075,-0.17,1.18,-0.025,-0.23,1.18,-0.025,-0.23,1.18,-0.085,-0.17,1.18,-0.085,-0.17,1.14,-0.025,-0.23,1.14,-0.025,-0.23,1.14,-0.085,-0.17,1.14,-0.085,-0.18,0.91,-0.05,-0.22,0.91,-0.05,-0.22,0.91,-0.09,-0.18,0.91,-0.09,-0.18,0.87,-0.02,-0.22,0.87,-0.02,-0.22,0.87,-0.1,-0.18,0.87,-0.1,-0.18,0.6976,-0.02,-0.22,0.6976,-0.02,-0.22,0.6976,-0.1,-0.18,0.6976,-0.1])

HAnimHumanoid802.setSkinCoord(Coordinate864)
Group865 = Group()
Shape866 = Shape()
Shape866.setDEF("TrouserSkin")
Appearance867 = Appearance()
Material868 = Material()
Material868.setDiffuseColor([0,0,1])
Material868.setTransparency(0.5)

Appearance867.setMaterial(Material868)

Shape866.setAppearance(Appearance867)
## 0: sacrum (8) # 1: l_hip joint (8) # 2: r_hip joint (8) # 3: l_thigh (48) # 4: l_knee joint (8) # 5: l_calf (40) # 10: r_thigh (48) # 11: r_knee joint (8) # 12: r_calf (40)
IndexedFaceSet869 = IndexedFaceSet()
IndexedFaceSet869.setCoordIndex([0,7,1,-1,8,0,1,-1,1,9,8,-1,10,2,3,-1,3,11,10,-1,2,4,5,-1,5,3,2,-1,4,6,5,-1,7,12,1,-1,1,12,13,-1,13,9,1,-1,9,13,14,-1,14,10,9,-1,10,14,15,-1,15,2,10,-1,12,7,6,-1,6,15,12,-1,15,6,4,-1,4,2,15,-1,0,80,7,-1,81,80,0,-1,0,8,81,-1,82,81,8,-1,8,11,82,-1,83,82,11,-1,11,3,83,-1,6,7,80,-1,80,83,6,-1,5,6,83,-1,83,3,5,-1,12,16,17,-1,17,13,12,-1,13,17,18,-1,18,14,13,-1,14,18,19,-1,19,15,14,-1,15,19,16,-1,16,12,15,-1,16,20,21,-1,21,17,16,-1,17,21,22,-1,22,18,17,-1,18,22,23,-1,23,19,18,-1,19,23,20,-1,20,16,19,-1,20,24,25,-1,25,21,20,-1,21,25,26,-1,26,22,21,-1,22,26,27,-1,27,23,22,-1,23,27,24,-1,24,20,23,-1,24,28,29,-1,29,25,24,-1,25,29,30,-1,30,26,25,-1,26,30,31,-1,31,27,26,-1,27,31,28,-1,28,24,27,-1,28,32,33,-1,33,29,28,-1,29,33,34,-1,34,30,29,-1,30,34,35,-1,35,31,30,-1,31,35,32,-1,32,28,31,-1,32,36,37,-1,37,33,32,-1,33,37,38,-1,38,34,33,-1,34,38,39,-1,39,35,34,-1,35,39,36,-1,36,32,35,-1,36,40,41,-1,41,37,36,-1,37,41,42,-1,42,38,37,-1,38,42,43,-1,43,39,38,-1,39,43,40,-1,40,36,39,-1,40,44,45,-1,45,41,40,-1,41,45,46,-1,46,42,41,-1,42,46,47,-1,47,43,42,-1,43,47,44,-1,44,40,43,-1,44,48,49,-1,49,45,44,-1,45,49,50,-1,50,46,45,-1,46,50,51,-1,51,47,46,-1,47,51,48,-1,48,44,47,-1,48,52,53,-1,53,49,48,-1,49,53,54,-1,54,50,49,-1,50,54,55,-1,55,51,50,-1,51,55,52,-1,52,48,51,-1,52,56,57,-1,57,53,52,-1,53,57,58,-1,58,54,53,-1,54,58,59,-1,59,55,54,-1,55,59,56,-1,56,52,55,-1,56,60,61,-1,61,57,56,-1,57,61,62,-1,62,58,57,-1,58,62,63,-1,63,59,58,-1,59,63,60,-1,60,56,59,-1,81,85,84,-1,84,80,81,-1,82,86,85,-1,85,81,82,-1,83,87,86,-1,86,82,83,-1,80,84,87,-1,87,83,80,-1,85,89,88,-1,88,84,85,-1,86,90,89,-1,89,85,86,-1,87,91,90,-1,90,86,87,-1,84,88,91,-1,91,87,84,-1,89,93,92,-1,92,88,89,-1,90,94,93,-1,93,89,90,-1,91,95,94,-1,94,90,91,-1,88,92,95,-1,95,91,88,-1,93,97,96,-1,96,92,93,-1,94,98,97,-1,97,93,94,-1,95,99,98,-1,98,94,95,-1,92,96,99,-1,99,95,92,-1,97,101,100,-1,100,96,97,-1,98,102,101,-1,101,97,98,-1,99,103,102,-1,102,98,99,-1,96,100,103,-1,103,99,96,-1,101,105,104,-1,104,100,101,-1,102,106,105,-1,105,101,102,-1,103,107,106,-1,106,102,103,-1,100,104,107,-1,107,103,100,-1,105,109,108,-1,108,104,105,-1,106,110,109,-1,109,105,106,-1,107,111,110,-1,110,106,107,-1,104,108,111,-1,111,107,104,-1,109,113,112,-1,112,108,109,-1,110,114,113,-1,113,109,110,-1,111,115,114,-1,114,110,111,-1,108,112,115,-1,115,111,108,-1,113,117,116,-1,116,112,113,-1,114,118,117,-1,117,113,114,-1,115,119,118,-1,118,114,115,-1,112,116,119,-1,119,115,112,-1,117,121,120,-1,120,116,117,-1,118,122,121,-1,121,117,118,-1,119,123,122,-1,122,118,119,-1,116,120,123,-1,123,119,116,-1,121,125,124,-1,124,120,121,-1,122,126,125,-1,125,121,122,-1,123,127,126,-1,126,122,123,-1,120,124,127,-1,127,123,120,-1,125,129,128,-1,128,124,125,-1,126,130,129,-1,129,125,126,-1,127,131,130,-1,130,126,127,-1,124,128,131,-1,131,127,124,-1])
Coordinate870 = Coordinate()
Coordinate870.setUSE("SKINCOORD")

IndexedFaceSet869.setCoord(Coordinate870)

Shape866.setGeometry(IndexedFaceSet869)

Group865.addChildren(Shape866)
Shape871 = Shape()
Shape871.setDEF("ShoeSkin")
Appearance872 = Appearance()
Material873 = Material()
Material873.setDiffuseColor([0,0,0])
Material873.setTransparency(0.5)

Appearance872.setMaterial(Material873)

Shape871.setAppearance(Appearance872)
## 6: l_ankle joint (8) # 7: l_hindfoot (8) # 8: l_midtarsal joint (8) # 9: l_middistal (10) # 13: r_ankle joint (8) # 14: r_hindfoot (8) # 15: r_midtarsal joint (8) # 16: r_middistal (10)
IndexedFaceSet874 = IndexedFaceSet()
IndexedFaceSet874.setCoordIndex([60,64,65,-1,65,61,60,-1,61,65,66,-1,66,62,61,-1,62,66,67,-1,67,63,62,-1,63,67,64,-1,64,60,63,-1,64,68,69,-1,69,65,64,-1,65,69,70,-1,70,66,65,-1,66,70,71,-1,71,67,66,-1,67,71,68,-1,68,64,67,-1,68,72,73,-1,73,69,68,-1,69,73,74,-1,74,70,69,-1,70,74,75,-1,75,71,70,-1,71,75,72,-1,72,68,71,-1,72,76,77,-1,77,73,72,-1,73,77,78,-1,78,74,73,-1,74,78,79,-1,79,75,74,-1,75,79,76,-1,76,72,75,-1,76,79,78,-1,78,77,76,-1,129,133,132,-1,132,128,129,-1,130,134,133,-1,133,129,130,-1,131,135,134,-1,134,130,131,-1,128,132,135,-1,135,131,128,-1,133,137,136,-1,136,132,133,-1,134,138,137,-1,137,133,134,-1,135,139,138,-1,138,134,135,-1,132,136,139,-1,139,135,132,-1,137,141,140,-1,140,136,137,-1,138,142,141,-1,141,137,138,-1,139,143,142,-1,142,138,139,-1,136,140,143,-1,143,139,136,-1,141,145,144,-1,144,140,141,-1,142,146,145,-1,145,141,142,-1,143,147,146,-1,146,142,143,-1,140,144,147,-1,147,143,140,-1,145,146,147,-1,147,144,145,-1])
Coordinate875 = Coordinate()
Coordinate875.setUSE("SKINCOORD")

IndexedFaceSet874.setCoord(Coordinate875)

Shape871.setGeometry(IndexedFaceSet874)

Group865.addChildren(Shape871)
Shape876 = Shape()
Shape876.setDEF("ShirtSkin")
Appearance877 = Appearance()
Material878 = Material()
Material878.setDiffuseColor([1,1,0])
Material878.setTransparency(0.5)

Appearance877.setMaterial(Material878)

Shape876.setAppearance(Appearance877)
## 17: vl5_joint (8) # 18: l5 (28) # 21: l_shoulder joint (8) # 22: l_upperarm (8) # 23: l_elbow joint (8) # 24: l_forearm (8) # 27: r_shoulder joint (8) # 28: r_upperarm (8) # 29: r_elbow joint (8) # 30: r_forearm (8)
IndexedFaceSet879 = IndexedFaceSet()
IndexedFaceSet879.setCoordIndex([148,8,9,-1,9,149,148,-1,149,9,10,-1,10,150,149,-1,150,10,11,-1,11,151,150,-1,151,11,8,-1,8,148,151,-1,152,148,149,-1,149,153,152,-1,153,149,150,-1,150,154,153,-1,154,150,151,-1,151,155,154,-1,155,151,148,-1,148,152,155,-1,156,152,153,-1,153,157,156,-1,158,154,155,-1,155,159,158,-1,160,156,157,-1,157,161,160,-1,161,157,158,-1,158,162,161,-1,162,158,159,-1,159,163,162,-1,163,159,156,-1,156,160,163,-1,164,160,161,-1,161,165,164,-1,165,161,162,-1,162,166,165,-1,166,162,163,-1,163,167,166,-1,167,163,160,-1,160,164,167,-1,153,176,177,-1,177,157,153,-1,157,177,178,-1,178,158,157,-1,158,178,179,-1,179,154,158,-1,154,179,176,-1,176,153,154,-1,176,180,181,-1,181,177,176,-1,177,181,182,-1,182,178,177,-1,178,182,183,-1,183,179,178,-1,179,183,180,-1,180,176,179,-1,180,184,185,-1,185,181,180,-1,181,185,186,-1,186,182,181,-1,182,186,187,-1,187,183,182,-1,183,187,184,-1,184,180,183,-1,184,188,189,-1,189,185,184,-1,185,189,190,-1,190,186,185,-1,186,190,191,-1,191,187,186,-1,187,191,188,-1,188,184,187,-1,152,156,201,-1,201,200,152,-1,156,159,202,-1,202,201,156,-1,159,155,203,-1,203,202,159,-1,155,152,200,-1,200,203,155,-1,201,205,204,-1,204,200,201,-1,202,206,205,-1,205,201,202,-1,203,207,206,-1,206,202,203,-1,200,204,207,-1,207,203,200,-1,205,209,208,-1,208,204,205,-1,206,210,209,-1,209,205,206,-1,207,211,210,-1,210,206,207,-1,204,208,211,-1,211,207,204,-1,209,213,212,-1,212,208,209,-1,210,214,213,-1,213,209,210,-1,211,215,214,-1,214,210,211,-1,208,212,215,-1,215,211,208,-1])
Coordinate880 = Coordinate()
Coordinate880.setUSE("SKINCOORD")

IndexedFaceSet879.setCoord(Coordinate880)

Shape876.setGeometry(IndexedFaceSet879)

Group865.addChildren(Shape876)
Shape881 = Shape()
Shape881.setDEF("HeadHandsFleshToneSkin")
Appearance882 = Appearance()
Material883 = Material()
Material883.setDiffuseColor([1,0.75,0.75])
Material883.setTransparency(0.5)

Appearance882.setMaterial(Material883)

Shape881.setAppearance(Appearance882)
## 19: skullbase joint (8) # 20: skull (10) # 25: l_wrist joint (8) # 26: l_hand (10) # 31: r_wrist joint (8) # 32: r_hand (10)
IndexedFaceSet884 = IndexedFaceSet()
IndexedFaceSet884.setCoordIndex([172,164,165,-1,165,173,172,-1,173,165,166,-1,166,174,173,-1,174,166,167,-1,167,175,174,-1,175,167,164,-1,164,172,175,-1,168,172,173,-1,173,169,168,-1,169,173,174,-1,174,170,169,-1,170,174,175,-1,175,171,170,-1,171,175,172,-1,172,168,171,-1,171,168,169,-1,169,170,171,-1,188,192,193,-1,193,189,188,-1,189,193,194,-1,194,190,189,-1,190,194,195,-1,195,191,190,-1,191,195,192,-1,192,188,191,-1,192,196,197,-1,197,193,192,-1,193,197,198,-1,198,194,193,-1,194,198,199,-1,199,195,194,-1,195,199,196,-1,196,192,195,-1,196,199,198,-1,198,197,196,-1,213,217,216,-1,216,212,213,-1,214,218,217,-1,217,213,214,-1,215,219,218,-1,218,214,215,-1,212,216,219,-1,219,215,212,-1,217,221,220,-1,220,216,217,-1,218,222,221,-1,221,217,218,-1,219,223,222,-1,222,218,219,-1,216,220,223,-1,223,219,216,-1,221,222,223,-1,223,220,221,-1])
Coordinate885 = Coordinate()
Coordinate885.setUSE("SKINCOORD")

IndexedFaceSet884.setCoord(Coordinate885)

Shape881.setGeometry(IndexedFaceSet884)

Group865.addChildren(Shape881)
Shape886 = Shape()
Shape886.setDEF("SkinLines")
Appearance887 = Appearance()
Material888 = Material()
Material888.setDiffuseColor([0,0,0])

Appearance887.setMaterial(Material888)

Shape886.setAppearance(Appearance887)
#Combined set of prior IFS coordIndex values
IndexedLineSet889 = IndexedLineSet()
IndexedLineSet889.setCoordIndex([0,7,1,-1,8,0,1,-1,1,9,8,-1,10,2,3,-1,3,11,10,-1,2,4,5,-1,5,3,2,-1,4,6,5,-1,7,12,1,-1,1,12,13,-1,13,9,1,-1,9,13,14,-1,14,10,9,-1,10,14,15,-1,15,2,10,-1,12,7,6,-1,6,15,12,-1,15,6,4,-1,4,2,15,-1,0,80,7,-1,81,80,0,-1,0,8,81,-1,82,81,8,-1,8,11,82,-1,83,82,11,-1,11,3,83,-1,6,7,80,-1,80,83,6,-1,5,6,83,-1,83,3,5,-1,12,16,17,-1,17,13,12,-1,13,17,18,-1,18,14,13,-1,14,18,19,-1,19,15,14,-1,15,19,16,-1,16,12,15,-1,16,20,21,-1,21,17,16,-1,17,21,22,-1,22,18,17,-1,18,22,23,-1,23,19,18,-1,19,23,20,-1,20,16,19,-1,20,24,25,-1,25,21,20,-1,21,25,26,-1,26,22,21,-1,22,26,27,-1,27,23,22,-1,23,27,24,-1,24,20,23,-1,24,28,29,-1,29,25,24,-1,25,29,30,-1,30,26,25,-1,26,30,31,-1,31,27,26,-1,27,31,28,-1,28,24,27,-1,28,32,33,-1,33,29,28,-1,29,33,34,-1,34,30,29,-1,30,34,35,-1,35,31,30,-1,31,35,32,-1,32,28,31,-1,32,36,37,-1,37,33,32,-1,33,37,38,-1,38,34,33,-1,34,38,39,-1,39,35,34,-1,35,39,36,-1,36,32,35,-1,36,40,41,-1,41,37,36,-1,37,41,42,-1,42,38,37,-1,38,42,43,-1,43,39,38,-1,39,43,40,-1,40,36,39,-1,40,44,45,-1,45,41,40,-1,41,45,46,-1,46,42,41,-1,42,46,47,-1,47,43,42,-1,43,47,44,-1,44,40,43,-1,44,48,49,-1,49,45,44,-1,45,49,50,-1,50,46,45,-1,46,50,51,-1,51,47,46,-1,47,51,48,-1,48,44,47,-1,48,52,53,-1,53,49,48,-1,49,53,54,-1,54,50,49,-1,50,54,55,-1,55,51,50,-1,51,55,52,-1,52,48,51,-1,52,56,57,-1,57,53,52,-1,53,57,58,-1,58,54,53,-1,54,58,59,-1,59,55,54,-1,55,59,56,-1,56,52,55,-1,56,60,61,-1,61,57,56,-1,57,61,62,-1,62,58,57,-1,58,62,63,-1,63,59,58,-1,59,63,60,-1,60,56,59,-1,81,85,84,-1,84,80,81,-1,82,86,85,-1,85,81,82,-1,83,87,86,-1,86,82,83,-1,80,84,87,-1,87,83,80,-1,85,89,88,-1,88,84,85,-1,86,90,89,-1,89,85,86,-1,87,91,90,-1,90,86,87,-1,84,88,91,-1,91,87,84,-1,89,93,92,-1,92,88,89,-1,90,94,93,-1,93,89,90,-1,91,95,94,-1,94,90,91,-1,88,92,95,-1,95,91,88,-1,93,97,96,-1,96,92,93,-1,94,98,97,-1,97,93,94,-1,95,99,98,-1,98,94,95,-1,92,96,99,-1,99,95,92,-1,97,101,100,-1,100,96,97,-1,98,102,101,-1,101,97,98,-1,99,103,102,-1,102,98,99,-1,96,100,103,-1,103,99,96,-1,101,105,104,-1,104,100,101,-1,102,106,105,-1,105,101,102,-1,103,107,106,-1,106,102,103,-1,100,104,107,-1,107,103,100,-1,105,109,108,-1,108,104,105,-1,106,110,109,-1,109,105,106,-1,107,111,110,-1,110,106,107,-1,104,108,111,-1,111,107,104,-1,109,113,112,-1,112,108,109,-1,110,114,113,-1,113,109,110,-1,111,115,114,-1,114,110,111,-1,108,112,115,-1,115,111,108,-1,113,117,116,-1,116,112,113,-1,114,118,117,-1,117,113,114,-1,115,119,118,-1,118,114,115,-1,112,116,119,-1,119,115,112,-1,117,121,120,-1,120,116,117,-1,118,122,121,-1,121,117,118,-1,119,123,122,-1,122,118,119,-1,116,120,123,-1,123,119,116,-1,121,125,124,-1,124,120,121,-1,122,126,125,-1,125,121,122,-1,123,127,126,-1,126,122,123,-1,120,124,127,-1,127,123,120,-1,125,129,128,-1,128,124,125,-1,126,130,129,-1,129,125,126,-1,127,131,130,-1,130,126,127,-1,124,128,131,-1,131,127,124,-1,60,64,65,-1,65,61,60,-1,61,65,66,-1,66,62,61,-1,62,66,67,-1,67,63,62,-1,63,67,64,-1,64,60,63,-1,64,68,69,-1,69,65,64,-1,65,69,70,-1,70,66,65,-1,66,70,71,-1,71,67,66,-1,67,71,68,-1,68,64,67,-1,68,72,73,-1,73,69,68,-1,69,73,74,-1,74,70,69,-1,70,74,75,-1,75,71,70,-1,71,75,72,-1,72,68,71,-1,72,76,77,-1,77,73,72,-1,73,77,78,-1,78,74,73,-1,74,78,79,-1,79,75,74,-1,75,79,76,-1,76,72,75,-1,76,79,78,-1,78,77,76,-1,129,133,132,-1,132,128,129,-1,130,134,133,-1,133,129,130,-1,131,135,134,-1,134,130,131,-1,128,132,135,-1,135,131,128,-1,133,137,136,-1,136,132,133,-1,134,138,137,-1,137,133,134,-1,135,139,138,-1,138,134,135,-1,132,136,139,-1,139,135,132,-1,137,141,140,-1,140,136,137,-1,138,142,141,-1,141,137,138,-1,139,143,142,-1,142,138,139,-1,136,140,143,-1,143,139,136,-1,141,145,144,-1,144,140,141,-1,142,146,145,-1,145,141,142,-1,143,147,146,-1,146,142,143,-1,140,144,147,-1,147,143,140,-1,145,146,147,-1,147,144,145,-1,148,8,9,-1,9,149,148,-1,149,9,10,-1,10,150,149,-1,150,10,11,-1,11,151,150,-1,151,11,8,-1,8,148,151,-1,152,148,149,-1,149,153,152,-1,153,149,150,-1,150,154,153,-1,154,150,151,-1,151,155,154,-1,155,151,148,-1,148,152,155,-1,156,152,153,-1,153,157,156,-1,158,154,155,-1,155,159,158,-1,160,156,157,-1,157,161,160,-1,161,157,158,-1,158,162,161,-1,162,158,159,-1,159,163,162,-1,163,159,156,-1,156,160,163,-1,164,160,161,-1,161,165,164,-1,165,161,162,-1,162,166,165,-1,166,162,163,-1,163,167,166,-1,167,163,160,-1,160,164,167,-1,153,176,177,-1,177,157,153,-1,157,177,178,-1,178,158,157,-1,158,178,179,-1,179,154,158,-1,154,179,176,-1,176,153,154,-1,176,180,181,-1,181,177,176,-1,177,181,182,-1,182,178,177,-1,178,182,183,-1,183,179,178,-1,179,183,180,-1,180,176,179,-1,180,184,185,-1,185,181,180,-1,181,185,186,-1,186,182,181,-1,182,186,187,-1,187,183,182,-1,183,187,184,-1,184,180,183,-1,184,188,189,-1,189,185,184,-1,185,189,190,-1,190,186,185,-1,186,190,191,-1,191,187,186,-1,187,191,188,-1,188,184,187,-1,152,156,201,-1,201,200,152,-1,156,159,202,-1,202,201,156,-1,159,155,203,-1,203,202,159,-1,155,152,200,-1,200,203,155,-1,201,205,204,-1,204,200,201,-1,202,206,205,-1,205,201,202,-1,203,207,206,-1,206,202,203,-1,200,204,207,-1,207,203,200,-1,205,209,208,-1,208,204,205,-1,206,210,209,-1,209,205,206,-1,207,211,210,-1,210,206,207,-1,204,208,211,-1,211,207,204,-1,209,213,212,-1,212,208,209,-1,210,214,213,-1,213,209,210,-1,211,215,214,-1,214,210,211,-1,208,212,215,-1,215,211,208,-1,172,164,165,-1,165,173,172,-1,173,165,166,-1,166,174,173,-1,174,166,167,-1,167,175,174,-1,175,167,164,-1,164,172,175,-1,168,172,173,-1,173,169,168,-1,169,173,174,-1,174,170,169,-1,170,174,175,-1,175,171,170,-1,171,175,172,-1,172,168,171,-1,171,168,169,-1,169,170,171,-1,188,192,193,-1,193,189,188,-1,189,193,194,-1,194,190,189,-1,190,194,195,-1,195,191,190,-1,191,195,192,-1,192,188,191,-1,192,196,197,-1,197,193,192,-1,193,197,198,-1,198,194,193,-1,194,198,199,-1,199,195,194,-1,195,199,196,-1,196,192,195,-1,196,199,198,-1,198,197,196,-1,213,217,216,-1,216,212,213,-1,214,218,217,-1,217,213,214,-1,215,219,218,-1,218,214,215,-1,212,216,219,-1,219,215,212,-1,217,221,220,-1,220,216,217,-1,218,222,221,-1,221,217,218,-1,219,223,222,-1,222,218,219,-1,216,220,223,-1,223,219,216,-1,221,222,223,-1,223,220,221,-1])
Coordinate890 = Coordinate()
Coordinate890.setUSE("SKINCOORD")

IndexedLineSet889.setCoord(Coordinate890)

Shape886.setGeometry(IndexedLineSet889)

Group865.addChildren(Shape886)

HAnimHumanoid802.setSkin(Group865)
HAnimJoint891 = HAnimJoint()
HAnimJoint891.setUSE("Boxman_humanoid_root")

HAnimHumanoid802.addJoints(HAnimJoint891)
HAnimJoint892 = HAnimJoint()
HAnimJoint892.setUSE("Boxman_skullbase")

HAnimHumanoid802.addJoints(HAnimJoint892)
HAnimJoint893 = HAnimJoint()
HAnimJoint893.setUSE("Boxman_vl5")

HAnimHumanoid802.addJoints(HAnimJoint893)
HAnimJoint894 = HAnimJoint()
HAnimJoint894.setUSE("Boxman_r_ankle")

HAnimHumanoid802.addJoints(HAnimJoint894)
HAnimJoint895 = HAnimJoint()
HAnimJoint895.setUSE("Boxman_l_ankle")

HAnimHumanoid802.addJoints(HAnimJoint895)
HAnimJoint896 = HAnimJoint()
HAnimJoint896.setUSE("Boxman_r_elbow")

HAnimHumanoid802.addJoints(HAnimJoint896)
HAnimJoint897 = HAnimJoint()
HAnimJoint897.setUSE("Boxman_l_elbow")

HAnimHumanoid802.addJoints(HAnimJoint897)
HAnimJoint898 = HAnimJoint()
HAnimJoint898.setUSE("Boxman_r_hip")

HAnimHumanoid802.addJoints(HAnimJoint898)
HAnimJoint899 = HAnimJoint()
HAnimJoint899.setUSE("Boxman_l_hip")

HAnimHumanoid802.addJoints(HAnimJoint899)
HAnimJoint900 = HAnimJoint()
HAnimJoint900.setUSE("Boxman_l_knee")

HAnimHumanoid802.addJoints(HAnimJoint900)
HAnimJoint901 = HAnimJoint()
HAnimJoint901.setUSE("Boxman_r_knee")

HAnimHumanoid802.addJoints(HAnimJoint901)
HAnimJoint902 = HAnimJoint()
HAnimJoint902.setUSE("Boxman_r_midtarsal")

HAnimHumanoid802.addJoints(HAnimJoint902)
HAnimJoint903 = HAnimJoint()
HAnimJoint903.setUSE("Boxman_l_midtarsal")

HAnimHumanoid802.addJoints(HAnimJoint903)
HAnimJoint904 = HAnimJoint()
HAnimJoint904.setUSE("Boxman_r_shoulder")

HAnimHumanoid802.addJoints(HAnimJoint904)
HAnimJoint905 = HAnimJoint()
HAnimJoint905.setUSE("Boxman_l_shoulder")

HAnimHumanoid802.addJoints(HAnimJoint905)
HAnimJoint906 = HAnimJoint()
HAnimJoint906.setUSE("Boxman_r_wrist")

HAnimHumanoid802.addJoints(HAnimJoint906)
HAnimJoint907 = HAnimJoint()
HAnimJoint907.setUSE("Boxman_l_wrist")

HAnimHumanoid802.addJoints(HAnimJoint907)
HAnimSegment908 = HAnimSegment()
HAnimSegment908.setUSE("Boxman_sacrum")

HAnimHumanoid802.addSegments(HAnimSegment908)
HAnimSegment909 = HAnimSegment()
HAnimSegment909.setUSE("Boxman_l5")

HAnimHumanoid802.addSegments(HAnimSegment909)
HAnimSegment910 = HAnimSegment()
HAnimSegment910.setUSE("Boxman_skull")

HAnimHumanoid802.addSegments(HAnimSegment910)
HAnimSegment911 = HAnimSegment()
HAnimSegment911.setUSE("Boxman_l_calf")

HAnimHumanoid802.addSegments(HAnimSegment911)
HAnimSegment912 = HAnimSegment()
HAnimSegment912.setUSE("Boxman_r_calf")

HAnimHumanoid802.addSegments(HAnimSegment912)
HAnimSegment913 = HAnimSegment()
HAnimSegment913.setUSE("Boxman_l_forearm")

HAnimHumanoid802.addSegments(HAnimSegment913)
HAnimSegment914 = HAnimSegment()
HAnimSegment914.setUSE("Boxman_r_forearm")

HAnimHumanoid802.addSegments(HAnimSegment914)
HAnimSegment915 = HAnimSegment()
HAnimSegment915.setUSE("Boxman_l_hand")

HAnimHumanoid802.addSegments(HAnimSegment915)
HAnimSegment916 = HAnimSegment()
HAnimSegment916.setUSE("Boxman_r_hand")

HAnimHumanoid802.addSegments(HAnimSegment916)
HAnimSegment917 = HAnimSegment()
HAnimSegment917.setUSE("Boxman_l_hindfoot")

HAnimHumanoid802.addSegments(HAnimSegment917)
HAnimSegment918 = HAnimSegment()
HAnimSegment918.setUSE("Boxman_r_hindfoot")

HAnimHumanoid802.addSegments(HAnimSegment918)
HAnimSegment919 = HAnimSegment()
HAnimSegment919.setUSE("Boxman_l_middistal")

HAnimHumanoid802.addSegments(HAnimSegment919)
HAnimSegment920 = HAnimSegment()
HAnimSegment920.setUSE("Boxman_r_middistal")

HAnimHumanoid802.addSegments(HAnimSegment920)
HAnimSegment921 = HAnimSegment()
HAnimSegment921.setUSE("Boxman_l_thigh")

HAnimHumanoid802.addSegments(HAnimSegment921)
HAnimSegment922 = HAnimSegment()
HAnimSegment922.setUSE("Boxman_r_thigh")

HAnimHumanoid802.addSegments(HAnimSegment922)
HAnimSegment923 = HAnimSegment()
HAnimSegment923.setUSE("Boxman_l_upperarm")

HAnimHumanoid802.addSegments(HAnimSegment923)
HAnimSegment924 = HAnimSegment()
HAnimSegment924.setUSE("Boxman_r_upperarm")

HAnimHumanoid802.addSegments(HAnimSegment924)
HAnimSite925 = HAnimSite()
HAnimSite925.setUSE("Boxman_skull_tip")

HAnimHumanoid802.addSites(HAnimSite925)
HAnimSite926 = HAnimSite()
HAnimSite926.setUSE("Boxman_l_hand_tip")

HAnimHumanoid802.addSites(HAnimSite926)
HAnimSite927 = HAnimSite()
HAnimSite927.setUSE("Boxman_r_hand_tip")

HAnimHumanoid802.addSites(HAnimSite927)
HAnimSite928 = HAnimSite()
HAnimSite928.setUSE("Boxman_l_middistal_tip")

HAnimHumanoid802.addSites(HAnimSite928)
HAnimSite929 = HAnimSite()
HAnimSite929.setUSE("Boxman_r_middistal_tip")

HAnimHumanoid802.addSites(HAnimSite929)

Switch291.addChildren(HAnimHumanoid802)
Script930 = Script()
Script930.setDEF("ENGINE")
Script930.setDirectOutput(True)
field931 = field()
field931.setName("update")
field931.setAccessType("inputOnly")
field931.setType("SFRotation")

Script930.addField(field931)
field932 = field()
field932.setName("humanoid")
field932.setAccessType("initializeOnly")
field932.setType("SFNode")
HAnimHumanoid933 = HAnimHumanoid()
HAnimHumanoid933.setUSE("Boxman_Humanoid")

field932.addChildren(HAnimHumanoid933)

Script930.addField(field932)
field934 = field()
field934.setName("coordList")
field934.setAccessType("initializeOnly")
field934.setType("MFVec3f")

Script930.addField(field934)
field935 = field()
field935.setName("joint")
field935.setAccessType("initializeOnly")
field935.setType("SFNode")
#NULL node

Script930.addField(field935)
field936 = field()
field936.setName("translation")
field936.setAccessType("initializeOnly")
field936.setType("SFVec3f")
field936.setValue("0 0 0")

Script930.addField(field936)
field937 = field()
field937.setName("rotation")
field937.setAccessType("initializeOnly")
field937.setType("SFRotation")
field937.setValue("1 0 0 0")

Script930.addField(field937)
field938 = field()
field938.setName("scale")
field938.setAccessType("initializeOnly")
field938.setType("SFVec3f")
field938.setValue("1 1 1")

Script930.addField(field938)

Script930.setSourceCode('''ecmascript:\n"+
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
"      }''')

Switch291.addChildren(Script930)

Scene24.addChildren(Switch291)
#**********Behavior Proto Instances***********
ProtoInstance939 = ProtoInstance()
ProtoInstance939.setName("LOA1_WalkAnimation")
ProtoInstance939.setDEF("WALK")

Scene24.addChildren(ProtoInstance939)
ProtoInstance940 = ProtoInstance()
ProtoInstance940.setName("LOA1_RunAnimation")
ProtoInstance940.setDEF("RUN")

Scene24.addChildren(ProtoInstance940)
ProtoInstance941 = ProtoInstance()
ProtoInstance941.setName("LOA1_JumpAnimation")
ProtoInstance941.setDEF("JUMP")

Scene24.addChildren(ProtoInstance941)
ProtoInstance942 = ProtoInstance()
ProtoInstance942.setName("LOA1_StandAnimation")
ProtoInstance942.setDEF("STAND")

Scene24.addChildren(ProtoInstance942)
ProtoInstance943 = ProtoInstance()
ProtoInstance943.setName("LOA1_KneelAnimation")
ProtoInstance943.setDEF("KNEEL")

Scene24.addChildren(ProtoInstance943)
Group944 = Group()
Group944.setDEF("Interface")
Transform945 = Transform()
ProximitySensor946 = ProximitySensor()
ProximitySensor946.setDEF("HudProx")
ProximitySensor946.setCenter([0,20,0])
ProximitySensor946.setSize([500,100,500])

Transform945.addChildren(ProximitySensor946)

Group944.addChildren(Transform945)
Collision947 = Collision()
Collision947.setDEF("HUD")
Collision947.setEnabled(False)
Transform948 = Transform()
Transform948.setDEF("HudXform")
Transform949 = Transform()
Transform949.setScale([0.012,0.012,0.012])
Transform949.setTranslation([-0.005,-0.025,-0.08])
Transform950 = Transform()
Transform950.setDEF("Stand_Text")
TouchSensor951 = TouchSensor()
TouchSensor951.setDEF("Stand_Touch")
TouchSensor951.setDescription("click for behavior")

Transform950.addChildren(TouchSensor951)
Shape952 = Shape()
Shape952.setDEF("Stand")
IndexedFaceSet953 = IndexedFaceSet()
IndexedFaceSet953.setCoordIndex([1,30,29,-1,1,29,2,-1,31,47,46,-1,31,46,32,-1,78,77,80,-1,78,80,79,-1,96,113,112,-1,96,112,95,-1,95,112,111,-1,95,111,94,-1,94,111,110,-1,94,110,93,-1,93,110,109,-1,93,109,108,-1,93,108,100,-1,107,99,100,-1,107,100,108,-1,107,106,99,-1,106,105,98,-1,106,98,99,-1,104,97,98,-1,104,98,105,-1,103,102,104,-1,104,102,101,-1,104,101,97,-1,101,96,97,-1,101,97,101,-1,101,101,96,-1,96,101,113,-1,113,101,114,-1,115,86,85,-1,115,85,116,-1,117,87,84,-1,117,84,118,-1,119,83,120,-1,121,88,82,-1,121,82,122,-1,123,89,81,-1,123,81,124,-1,125,90,126,-1,127,92,128,-1,129,91,130,-1,54,49,50,-1,54,50,55,-1,76,75,74,-1,76,74,54,-1,54,74,73,-1,54,73,49,-1,49,73,48,-1,48,73,62,-1,48,62,61,-1,48,61,60,-1,48,60,53,-1,53,60,59,-1,53,59,53,-1,53,59,58,-1,53,58,52,-1,52,58,57,-1,52,57,51,-1,56,51,57,-1,56,55,50,-1,56,50,51,-1,62,73,72,-1,62,72,63,-1,63,72,71,-1,63,71,64,-1,64,71,70,-1,64,70,69,-1,64,69,65,-1,65,69,68,-1,65,68,67,-1,65,67,66,-1,131,40,39,-1,131,39,132,-1,133,43,42,-1,133,42,134,-1,135,37,36,-1,135,36,136,-1,137,41,38,-1,137,38,138,-1,139,44,35,-1,139,35,140,-1,141,34,142,-1,143,45,33,-1,143,33,144,-1,145,16,15,-1,145,15,146,-1,147,14,148,-1,149,17,13,-1,149,13,150,-1,151,18,12,-1,151,12,152,-1,153,19,11,-1,153,11,154,-1,155,20,10,-1,155,10,156,-1,157,9,158,-1,159,21,8,-1,159,8,160,-1,161,22,7,-1,161,7,162,-1,163,23,164,-1,165,24,6,-1,165,6,166,-1,167,25,5,-1,167,5,168,-1,169,26,170,-1,171,27,4,-1,171,4,172,-1,173,28,3,-1,173,3,174,-1,175,0,176,-1])
Coordinate954 = Coordinate()
Coordinate954.setPoint([-3.21,-0.0154,0,-3.15,-0.0154,0,-3.14,-0.0467,0,-3.1,-0.0601,0,-3.05,-0.051,0,-3.04,-0.0254,0,-3.05,-0.00248,0,-3.1,0.0122,0,-3.16,0.03,0,-3.2,0.0684,0,-3.2,0.133,0,-3.16,0.17,0,-3.1,0.182,0,-3.04,0.171,0,-3.01,0.136,0,-3,0.095,0,-3.05,0.095,0,-3.06,0.125,0,-3.1,0.136,0,-3.14,0.126,0,-3.15,0.103,0,-3.14,0.0815,0,-3.1,0.0689,0,-3.04,0.0512,0,-3,0.0249,0,-2.99,-0.0195,0,-3,-0.0708,0,-3.05,-0.104,0,-3.1,-0.108,0,-3.16,-0.0947,0,-3.2,-0.0586,0,-2.86,-0.102,0,-2.9,-0.102,0,-2.94,-0.0832,0,-2.94,-0.0457,0,-2.94,0.0645,0,-2.97,0.0645,0,-2.97,0.103,0,-2.94,0.103,0,-2.94,0.158,0,-2.89,0.158,0,-2.89,0.103,0,-2.86,0.103,0,-2.86,0.0645,0,-2.89,0.0645,0,-2.89,-0.0483,0,-2.88,-0.0608,0,-2.86,-0.0612,0,-2.71,-0.000798,0,-2.71,-0.0373,0,-2.74,-0.0637,0,-2.77,-0.0624,0,-2.78,-0.0416,0,-2.77,-0.0195,0,-2.71,-0.0754,0,-2.74,-0.103,0,-2.79,-0.106,0,-2.82,-0.0865,0,-2.84,-0.0431,0,-2.82,0.000177,0,-2.78,0.0201,0,-2.73,0.0275,0,-2.71,0.0446,0,-2.72,0.0614,0,-2.74,0.0675,0,-2.77,0.0573,0,-2.78,0.039,0,-2.83,0.039,0,-2.82,0.0765,0,-2.78,0.105,0,-2.74,0.11,0,-2.71,0.107,0,-2.67,0.0849,0,-2.66,0.0526,0,-2.66,-0.0763,0,-2.65,-0.101,0,-2.7,-0.101,0,-2.61,-0.101,0,-2.61,0.103,0,-2.56,0.103,0,-2.56,0.0787,0,-2.52,0.104,0,-2.47,0.105,0,-2.43,0.0743,0,-2.43,0.038,0,-2.43,-0.101,0,-2.48,-0.101,0,-2.48,0.0224,0,-2.49,0.0514,0,-2.52,0.0627,0,-2.54,0.0505,0,-2.55,0.02,0,-2.55,-0.101,0,-2.33,0.0279,0,-2.31,0.0587,0,-2.27,0.0589,0,-2.25,0.0281,0,-2.25,-0.0232,0,-2.27,-0.0563,0,-2.31,-0.057,0,-2.33,-0.0245,0,-2.19,0.175,0,-2.19,-0.101,0,-2.25,-0.101,0,-2.25,-0.073,0,-2.26,-0.0913,0,-2.31,-0.108,0,-2.35,-0.0915,0,-2.38,-0.0424,0,-2.39,0.0243,0,-2.37,0.0809,0,-2.32,0.108,0,-2.28,0.106,0,-2.25,0.0776,0,-2.25,0.175,0,-2.48,0.0224,0,-2.43,0.038,0,-2.49,0.0514,0,-2.43,0.0743,0,-2.49,0.0514,0,-2.47,0.105,0,-2.52,0.0627,0,-2.52,0.104,0,-2.54,0.0505,0,-2.56,0.0787,0,-2.55,0.02,0,-2.56,0.0787,0,-2.61,-0.101,0,-2.55,0.02,0,-2.61,-0.101,0,-2.56,0.0787,0,-2.89,0.103,0,-2.94,0.103,0,-2.89,0.0645,0,-2.89,0.103,0,-2.94,0.103,0,-2.94,0.0645,0,-2.89,0.0645,0,-2.94,0.0645,0,-2.89,-0.0483,0,-2.94,-0.0457,0,-2.89,-0.0483,0,-2.94,-0.0832,0,-2.88,-0.0608,0,-2.9,-0.102,0,-3.06,0.125,0,-3.01,0.136,0,-3.06,0.125,0,-3.04,0.171,0,-3.1,0.136,0,-3.1,0.182,0,-3.14,0.126,0,-3.16,0.17,0,-3.15,0.103,0,-3.2,0.133,0,-3.14,0.0815,0,-3.2,0.0684,0,-3.14,0.0815,0,-3.16,0.03,0,-3.1,0.0689,0,-3.1,0.0122,0,-3.04,0.0512,0,-3.05,-0.00248,0,-3,0.0249,0,-3.05,-0.00248,0,-2.99,-0.0195,0,-3.04,-0.0254,0,-3,-0.0708,0,-3.05,-0.051,0,-3.05,-0.104,0,-3.05,-0.051,0,-3.1,-0.108,0,-3.1,-0.0601,0,-3.16,-0.0947,0,-3.14,-0.0467,0,-3.15,-0.0154,0,-3.2,-0.0586,0])

IndexedFaceSet953.setCoord(Coordinate954)

Shape952.setGeometry(IndexedFaceSet953)
Appearance955 = Appearance()
Material956 = Material()
Material956.setDEF("text_color")
Material956.setAmbientIntensity(0)
Material956.setDiffuseColor([0,0,0])
Material956.setEmissiveColor([0.819,0.521,0.169])

Appearance955.setMaterial(Material956)

Shape952.setAppearance(Appearance955)

Transform950.addChildren(Shape952)
Transform957 = Transform()
Transform957.setScale([84.89,77.52,77.52])
Transform957.setTranslation([0.04092,1.843,3.826])
Shape958 = Shape()
Shape958.setDEF("Stand_Back")
IndexedFaceSet959 = IndexedFaceSet()
IndexedFaceSet959.setCoordIndex([0,2,3,-1,2,0,1,-1])
Coordinate960 = Coordinate()
Coordinate960.setPoint([-0.02572,-0.02535,-0.05,-0.02578,-0.02131,-0.05,-0.03871,-0.02131,-0.05,-0.03877,-0.02541,-0.05])

IndexedFaceSet959.setCoord(Coordinate960)

Shape958.setGeometry(IndexedFaceSet959)
Appearance961 = Appearance()
Material962 = Material()
Material962.setDEF("Clear")
Material962.setAmbientIntensity(0)
Material962.setDiffuseColor([0,0,0])
Material962.setTransparency(1)

Appearance961.setMaterial(Material962)

Shape958.setAppearance(Appearance961)

Transform957.addChildren(Shape958)

Transform950.addChildren(Transform957)

Transform949.addChildren(Transform950)
Transform963 = Transform()
Transform963.setDEF("Walk_Text")
TouchSensor964 = TouchSensor()
TouchSensor964.setDEF("Walk_Touch")
TouchSensor964.setDescription("click for behavior")

Transform963.addChildren(TouchSensor964)
Shape965 = Shape()
Shape965.setDEF("WALK_Shape")
IndexedFaceSet966 = IndexedFaceSet()
IndexedFaceSet966.setCoordIndex([0,2,1,-1,3,2,0,-1,12,3,0,-1,4,3,12,-1,11,4,12,-1,5,4,11,-1,10,5,11,-1,6,5,10,-1,9,6,10,-1,7,6,9,-1,8,7,9,-1,15,14,13,-1,16,15,13,-1,19,18,17,-1,20,19,17,-1,27,20,17,-1,28,27,17,-1,26,20,27,-1,23,20,26,-1,21,20,23,-1,25,23,26,-1,22,21,23,-1,24,23,25,-1,29,30,31,-1,29,31,32,-1,33,34,35,-1,33,35,29,-1,29,35,36,-1,29,36,30,-1,30,36,37,-1,37,36,38,-1,37,38,39,-1,37,39,40,-1,37,40,41,-1,41,40,42,-1,41,42,41,-1,41,42,43,-1,41,43,44,-1,44,43,45,-1,44,45,46,-1,47,46,45,-1,47,32,31,-1,47,31,46,-1,38,36,48,-1,38,48,49,-1,49,48,50,-1,49,50,51,-1,51,50,52,-1,51,52,53,-1,51,53,54,-1,54,53,55,-1,54,55,56,-1,54,56,57,-1])
Coordinate967 = Coordinate()
Coordinate967.setPoint([-1.88,-0.101,0,-1.96,0.175,0,-1.91,0.175,0,-1.86,-0.0195,0,-1.82,0.175,0,-1.76,0.175,0,-1.72,-0.0195,0,-1.67,0.175,0,-1.61,0.175,0,-1.69,-0.101,0,-1.75,-0.101,0,-1.79,0.111,0,-1.83,-0.101,0,-1.38,-0.101,0,-1.38,0.175,0,-1.32,0.175,0,-1.32,-0.101,0,-1.27,-0.101,0,-1.27,0.175,0,-1.22,0.175,0,-1.22,0.0304,0,-1.16,0.103,0,-1.09,0.103,0,-1.16,0.0272,0,-1.09,-0.101,0,-1.15,-0.101,0,-1.2,-0.0141,0,-1.22,-0.0363,0,-1.22,-0.101,0,-1.48,-0.0754,0,-1.48,-0.0373,0,-1.51,-0.0637,0,-1.51,-0.103,0,-1.47,-0.101,0,-1.42,-0.101,0,-1.43,-0.0763,0,-1.43,0.0526,0,-1.48,-0.000798,0,-1.48,0.0446,0,-1.5,0.0275,0,-1.55,0.0201,0,-1.54,-0.0195,0,-1.59,0.000177,0,-1.61,-0.0431,0,-1.55,-0.0416,0,-1.59,-0.0865,0,-1.54,-0.0624,0,-1.56,-0.106,0,-1.44,0.0849,0,-1.49,0.0614,0,-1.48,0.107,0,-1.51,0.0675,0,-1.52,0.11,0,-1.55,0.105,0,-1.54,0.0573,0,-1.59,0.0765,0,-1.6,0.039,0,-1.55,0.039,0])

IndexedFaceSet966.setCoord(Coordinate967)

Shape965.setGeometry(IndexedFaceSet966)
Appearance968 = Appearance()
Material969 = Material()
Material969.setUSE("text_color")

Appearance968.setMaterial(Material969)

Shape965.setAppearance(Appearance968)

Transform963.addChildren(Shape965)
Transform970 = Transform()
Transform970.setScale([81.3,81.3,81.31])
Transform970.setTranslation([-0.0414,1.941,4.015])
Shape971 = Shape()
Shape971.setDEF("Walk_Back")
IndexedFaceSet972 = IndexedFaceSet()
IndexedFaceSet972.setCoordIndex([1,3,0,-1,3,1,2,-1])
Coordinate973 = Coordinate()
Coordinate973.setPoint([-0.02381,-0.02541,-0.05,-0.0127,-0.02541,-0.05,-0.01263,-0.02139,-0.05,-0.02381,-0.02146,-0.05])

IndexedFaceSet972.setCoord(Coordinate973)

Shape971.setGeometry(IndexedFaceSet972)
Appearance974 = Appearance()
Material975 = Material()
Material975.setUSE("Clear")

Appearance974.setMaterial(Material975)

Shape971.setAppearance(Appearance974)

Transform970.addChildren(Shape971)

Transform963.addChildren(Transform970)

Transform949.addChildren(Transform963)
Transform976 = Transform()
Transform976.setDEF("Run_Text")
TouchSensor977 = TouchSensor()
TouchSensor977.setDEF("Run_Touch")
TouchSensor977.setDescription("click for behavior")

Transform976.addChildren(TouchSensor977)
Shape978 = Shape()
Shape978.setDEF("Run")
IndexedFaceSet979 = IndexedFaceSet()
IndexedFaceSet979.setCoordIndex([24,26,25,-1,53,39,54,-1,17,1,0,-1,17,0,16,-1,0,14,16,-1,0,15,14,-1,14,13,22,-1,14,22,16,-1,13,12,21,-1,13,21,22,-1,12,6,21,-1,12,11,7,-1,12,7,6,-1,11,8,7,-1,10,8,11,-1,10,9,8,-1,6,5,21,-1,5,4,20,-1,5,20,21,-1,4,3,19,-1,4,19,20,-1,3,2,18,-1,3,18,19,-1,18,2,1,-1,18,1,17,-1,55,32,31,-1,55,31,56,-1,57,33,30,-1,57,30,58,-1,59,29,60,-1,61,34,28,-1,61,28,62,-1,63,35,27,-1,63,27,64,-1,65,36,66,-1,67,38,68,-1,69,37,70,-1,71,23,72,-1,73,48,47,-1,73,47,74,-1,75,49,46,-1,75,46,76,-1,77,45,78,-1,79,50,44,-1,79,44,80,-1,81,51,43,-1,81,43,82,-1,83,41,84,-1,85,40,86,-1,87,52,88,-1,89,42,90,-1])
Coordinate980 = Coordinate()
Coordinate980.setPoint([-0.829,-0.101,0,-0.829,0.175,0,-0.662,0.172,0,-0.622,0.148,0,-0.607,0.103,0,-0.62,0.0501,0,-0.648,0.0316,0,-0.615,-0.0063,0,-0.611,-0.0764,0,-0.601,-0.101,0,-0.664,-0.101,0,-0.671,-0.0373,0,-0.68,-0.00372,0,-0.712,0.00648,0,-0.772,0.00648,0,-0.772,-0.101,0,-0.772,0.0546,0,-0.772,0.127,0,-0.703,0.127,0,-0.673,0.118,0,-0.663,0.091,0,-0.674,0.063,0,-0.705,0.0546,0,-0.379,0.103,0,-0.379,-0.101,0,-0.432,-0.101,0,-0.432,-0.0764,0,-0.466,-0.101,0,-0.518,-0.102,0,-0.555,-0.072,0,-0.56,-0.0357,0,-0.56,0.103,0,-0.506,0.103,0,-0.506,-0.0201,0,-0.5,-0.0491,0,-0.472,-0.0604,0,-0.443,-0.0482,0,-0.433,-0.0177,0,-0.433,0.103,0,-0.331,-0.101,0,-0.331,0.103,0,-0.278,0.103,0,-0.278,0.0787,0,-0.244,0.104,0,-0.192,0.105,0,-0.154,0.0743,0,-0.149,0.038,0,-0.149,-0.101,0,-0.203,-0.101,0,-0.203,0.0224,0,-0.209,0.0514,0,-0.238,0.0627,0,-0.266,0.0505,0,-0.277,0.02,0,-0.277,-0.101,0,-0.506,-0.0201,0,-0.56,-0.0357,0,-0.5,-0.0491,0,-0.555,-0.072,0,-0.5,-0.0491,0,-0.518,-0.102,0,-0.472,-0.0604,0,-0.466,-0.101,0,-0.443,-0.0482,0,-0.432,-0.0764,0,-0.433,-0.0177,0,-0.432,-0.0764,0,-0.379,0.103,0,-0.433,-0.0177,0,-0.379,0.103,0,-0.432,-0.0764,0,-0.379,-0.101,0,-0.432,-0.0764,0,-0.203,0.0224,0,-0.149,0.038,0,-0.209,0.0514,0,-0.154,0.0743,0,-0.209,0.0514,0,-0.192,0.105,0,-0.238,0.0627,0,-0.244,0.104,0,-0.266,0.0505,0,-0.278,0.0787,0,-0.278,0.0787,0,-0.331,0.103,0,-0.277,0.02,0,-0.331,-0.101,0,-0.277,0.02,0,-0.278,0.0787,0,-0.277,0.02,0,-0.331,0.103,0])

IndexedFaceSet979.setCoord(Coordinate980)

Shape978.setGeometry(IndexedFaceSet979)
Appearance981 = Appearance()
Material982 = Material()
Material982.setUSE("text_color")

Appearance981.setMaterial(Material982)

Shape978.setAppearance(Appearance981)

Transform976.addChildren(Shape978)
Transform983 = Transform()
Transform983.setScale([82.47,82.47,82.48])
Transform983.setTranslation([-0.01579,1.968,4.074])
Shape984 = Shape()
Shape984.setDEF("Run_Back")
IndexedFaceSet985 = IndexedFaceSet()
IndexedFaceSet985.setCoordIndex([0,2,3,-1,2,0,1,-1])
Coordinate986 = Coordinate()
Coordinate986.setPoint([-0.01009,-0.02534,-0.05,-0.001382,-0.02541,-0.05,-0.001315,-0.02146,-0.05,-0.01022,-0.02146,-0.05])

IndexedFaceSet985.setCoord(Coordinate986)

Shape984.setGeometry(IndexedFaceSet985)
Appearance987 = Appearance()
Material988 = Material()
Material988.setUSE("Clear")

Appearance987.setMaterial(Material988)

Shape984.setAppearance(Appearance987)

Transform983.addChildren(Shape984)

Transform976.addChildren(Transform983)

Transform949.addChildren(Transform976)
Transform989 = Transform()
Transform989.setDEF("Jump_Text")
TouchSensor990 = TouchSensor()
TouchSensor990.setDEF("Jump_Touch")
TouchSensor990.setDescription("click for behavior")

Transform989.addChildren(TouchSensor990)
Shape991 = Shape()
Shape991.setDEF("Jump")
IndexedFaceSet992 = IndexedFaceSet()
IndexedFaceSet992.setCoordIndex([1,0,14,-1,1,14,2,-1,16,15,18,-1,16,18,17,-1,64,65,66,-1,67,68,69,-1,67,69,70,-1,71,72,73,-1,71,73,74,-1,75,76,77,-1,78,79,80,-1,78,80,81,-1,82,83,84,-1,82,84,85,-1,86,87,88,-1,89,90,91,-1,92,93,94,-1,95,96,97,-1,98,7,6,-1,98,6,99,-1,100,8,5,-1,100,5,101,-1,102,9,4,-1,102,4,103,-1,104,10,105,-1,106,11,3,-1,106,3,107,-1,108,12,109,-1,110,13,111,-1,112,27,26,-1,112,26,113,-1,114,28,25,-1,114,25,115,-1,116,24,117,-1,118,29,23,-1,118,23,119,-1,120,30,22,-1,120,22,121,-1,122,31,123,-1,124,34,33,-1,124,33,125,-1,126,35,32,-1,126,32,127,-1,128,21,129,-1,130,36,20,-1,130,20,131,-1,132,37,19,-1,132,19,133,-1,134,38,135,-1,136,40,137,-1,138,39,139,-1,53,58,59,-1,53,59,54,-1,53,52,58,-1,52,51,57,-1,52,57,58,-1,51,50,56,-1,51,56,57,-1,50,49,56,-1,49,48,63,-1,49,63,56,-1,48,47,63,-1,63,47,46,-1,63,46,62,-1,62,46,45,-1,62,45,44,-1,62,44,61,-1,61,44,60,-1,54,59,60,-1,44,43,42,-1,60,44,42,-1,41,55,54,-1,41,54,60,-1,41,60,42,-1])
Coordinate993 = Coordinate()
Coordinate993.setPoint([0.108,0.00195,0,0.163,0.00195,0,0.166,-0.0473,0,0.194,-0.0608,0,0.222,-0.0492,0,0.228,-0.017,0,0.228,0.175,0,0.284,0.175,0,0.284,-0.02,0,0.271,-0.0798,0,0.23,-0.104,0,0.193,-0.108,0,0.155,-0.102,0,0.117,-0.0714,0,0.108,-0.0357,0,0.563,-0.101,0,0.563,0.103,0,0.615,0.103,0,0.615,0.0803,0,0.649,0.105,0,0.696,0.105,0,0.728,0.0788,0,0.76,0.104,0,0.811,0.104,0,0.842,0.081,0,0.853,0.0416,0,0.853,-0.101,0,0.799,-0.101,0,0.799,0.0305,0,0.79,0.0544,0,0.767,0.0616,0,0.743,0.0507,0,0.734,0.0228,0,0.734,-0.101,0,0.681,-0.101,0,0.681,0.0301,0,0.673,0.0532,0,0.65,0.0611,0,0.626,0.0506,0,0.617,0.0224,0,0.617,-0.101,0,0.9,-0.182,0,0.9,0.103,0,0.952,0.103,0,0.952,0.0751,0,0.968,0.0934,0,1.01,0.11,0,1.05,0.103,0,1.07,0.0796,0,1.1,0.0251,0,1.1,-0.0222,0,1.07,-0.0788,0,1.03,-0.106,0,0.988,-0.103,0,0.953,-0.0755,0,0.953,-0.182,0,1.04,-0.000177,0,1.03,-0.0446,0,0.999,-0.0603,0,0.966,-0.0453,0,0.953,-0.000177,0,0.963,0.045,0,0.998,0.063,0,1.03,0.0462,0,0.515,-0.101,0,0.462,-0.0764,0,0.462,-0.101,0,0.388,-0.0201,0,0.388,0.103,0,0.334,0.103,0,0.334,-0.0357,0,0.394,-0.0491,0,0.388,-0.0201,0,0.334,-0.0357,0,0.339,-0.072,0,0.394,-0.0491,0,0.339,-0.072,0,0.376,-0.102,0,0.422,-0.0604,0,0.394,-0.0491,0,0.376,-0.102,0,0.428,-0.101,0,0.451,-0.0482,0,0.422,-0.0604,0,0.428,-0.101,0,0.462,-0.0764,0,0.461,-0.0177,0,0.451,-0.0482,0,0.462,-0.0764,0,0.515,0.103,0,0.461,0.103,0,0.461,-0.0177,0,0.515,0.103,0,0.461,-0.0177,0,0.462,-0.0764,0,0.515,-0.101,0,0.515,0.103,0,0.462,-0.0764,0,0.284,-0.02,0,0.228,-0.017,0,0.271,-0.0798,0,0.222,-0.0492,0,0.23,-0.104,0,0.194,-0.0608,0,0.193,-0.108,0,0.194,-0.0608,0,0.155,-0.102,0,0.166,-0.0473,0,0.117,-0.0714,0,0.166,-0.0473,0,0.108,-0.0357,0,0.166,-0.0473,0,0.799,0.0305,0,0.853,0.0416,0,0.79,0.0544,0,0.842,0.081,0,0.79,0.0544,0,0.811,0.104,0,0.767,0.0616,0,0.76,0.104,0,0.743,0.0507,0,0.728,0.0788,0,0.734,0.0228,0,0.728,0.0788,0,0.681,0.0301,0,0.734,0.0228,0,0.673,0.0532,0,0.728,0.0788,0,0.673,0.0532,0,0.696,0.105,0,0.65,0.0611,0,0.649,0.105,0,0.626,0.0506,0,0.615,0.0803,0,0.617,0.0224,0,0.615,0.0803,0,0.563,-0.101,0,0.617,0.0224,0,0.563,-0.101,0,0.615,0.0803,0])

IndexedFaceSet992.setCoord(Coordinate993)

Shape991.setGeometry(IndexedFaceSet992)
Appearance994 = Appearance()
Material995 = Material()
Material995.setUSE("text_color")

Appearance994.setMaterial(Material995)

Shape991.setAppearance(Appearance994)

Transform989.addChildren(Shape991)
Transform996 = Transform()
Transform996.setScale([83.79,83.79,83.79])
Transform996.setTranslation([-0.008979,1.99,4.14])
Shape997 = Shape()
Shape997.setDEF("Jump_Back")
IndexedFaceSet998 = IndexedFaceSet()
IndexedFaceSet998.setCoordIndex([0,2,3,-1,2,0,1,-1])
Coordinate999 = Coordinate()
Coordinate999.setPoint([0.001296,-0.02541,-0.05,0.01335,-0.02527,-0.05,0.01328,-0.02152,-0.05,0.001229,-0.02146,-0.05])

IndexedFaceSet998.setCoord(Coordinate999)

Shape997.setGeometry(IndexedFaceSet998)
Appearance1000 = Appearance()
Material1001 = Material()
Material1001.setUSE("Clear")

Appearance1000.setMaterial(Material1001)

Shape997.setAppearance(Appearance1000)

Transform996.addChildren(Shape997)

Transform989.addChildren(Transform996)

Transform949.addChildren(Transform989)
Transform1002 = Transform()
Transform1002.setDEF("Kneel_Text")
Transform1002.setTranslation([1.3,-0.12,0])
TouchSensor1003 = TouchSensor()
TouchSensor1003.setDEF("Kneel_Touch")
TouchSensor1003.setDescription("click for behavior")

Transform1002.addChildren(TouchSensor1003)
Shape1004 = Shape()
Shape1004.setDEF("Kneel")
Text1005 = Text()
Text1005.setString(["Kneel"])
FontStyle1006 = FontStyle()
FontStyle1006.setFamily(["SANS"])
FontStyle1006.setSize(0.45)
FontStyle1006.setStyle("BOLD")

Text1005.setFontStyle(FontStyle1006)

Shape1004.setGeometry(Text1005)
Appearance1007 = Appearance()
Material1008 = Material()
Material1008.setUSE("text_color")

Appearance1007.setMaterial(Material1008)

Shape1004.setAppearance(Appearance1007)

Transform1002.addChildren(Shape1004)
Transform1009 = Transform()
Transform1009.setTranslation([0.5,0.15,-0.001])
Shape1010 = Shape()
Shape1010.setDEF("Kneel_Back")
Appearance1011 = Appearance()
Material1012 = Material()
Material1012.setDiffuseColor([0,1,0])
Material1012.setTransparency(1)

Appearance1011.setMaterial(Material1012)

Shape1010.setAppearance(Appearance1011)
Box1013 = Box()
Box1013.setSize([1,0.36,0.001])

Shape1010.setGeometry(Box1013)

Transform1009.addChildren(Shape1010)

Transform1002.addChildren(Transform1009)

Transform949.addChildren(Transform1002)
Group1014 = Group()
Transform1015 = Transform()
Transform1015.setDEF("Allen_Text")
Transform1015.setTranslation([2,4,0])
TouchSensor1016 = TouchSensor()
TouchSensor1016.setDEF("Allen_Touch")
TouchSensor1016.setDescription("click for Allen body")

Transform1015.addChildren(TouchSensor1016)
Shape1017 = Shape()
Text1018 = Text()
Text1018.setString(["ALLEN"])
FontStyle1019 = FontStyle()
FontStyle1019.setSize(0.25)
FontStyle1019.setSpacing(0.1)
FontStyle1019.setStyle("BOLD")

Text1018.setFontStyle(FontStyle1019)

Shape1017.setGeometry(Text1018)
Appearance1020 = Appearance()
Material1021 = Material()
Material1021.setDiffuseColor([0.6,0.6,0.6])

Appearance1020.setMaterial(Material1021)

Shape1017.setAppearance(Appearance1020)

Transform1015.addChildren(Shape1017)
Transform1022 = Transform()
Transform1022.setTranslation([0.38,0.075,-0.001])
Shape1023 = Shape()
Shape1023.setDEF("MenuB")
Appearance1024 = Appearance()
Material1025 = Material()
Material1025.setDiffuseColor([0,1,0])
Material1025.setTransparency(1)

Appearance1024.setMaterial(Material1025)

Shape1023.setAppearance(Appearance1024)
Box1026 = Box()
Box1026.setSize([0.78,0.18,0.001])

Shape1023.setGeometry(Box1026)

Transform1022.addChildren(Shape1023)

Transform1015.addChildren(Transform1022)

Group1014.addChildren(Transform1015)
Transform1027 = Transform()
Transform1027.setDEF("Nancy_Text")
Transform1027.setTranslation([2,3.5,0])
TouchSensor1028 = TouchSensor()
TouchSensor1028.setDEF("Nancy_Touch")
TouchSensor1028.setDescription("click for Nancy body")

Transform1027.addChildren(TouchSensor1028)
Shape1029 = Shape()
Text1030 = Text()
Text1030.setString(["NANCY"])
FontStyle1031 = FontStyle()
FontStyle1031.setSize(0.25)
FontStyle1031.setSpacing(0.1)
FontStyle1031.setStyle("BOLD")

Text1030.setFontStyle(FontStyle1031)

Shape1029.setGeometry(Text1030)
Appearance1032 = Appearance()
Material1033 = Material()
Material1033.setDiffuseColor([0.6,0.6,0.6])

Appearance1032.setMaterial(Material1033)

Shape1029.setAppearance(Appearance1032)

Transform1027.addChildren(Shape1029)
Transform1034 = Transform()
Transform1034.setTranslation([0.38,0.075,-0.001])
Shape1035 = Shape()
Shape1035.setUSE("MenuB")

Transform1034.addChildren(Shape1035)

Transform1027.addChildren(Transform1034)

Group1014.addChildren(Transform1027)
Transform1036 = Transform()
Transform1036.setDEF("Boxman_Text")
Transform1036.setTranslation([2,3,0])
TouchSensor1037 = TouchSensor()
TouchSensor1037.setDEF("Boxman_Touch")
TouchSensor1037.setDescription("click for BoxMan body")

Transform1036.addChildren(TouchSensor1037)
Shape1038 = Shape()
Text1039 = Text()
Text1039.setString(["BOXMAN"])
FontStyle1040 = FontStyle()
FontStyle1040.setSize(0.25)
FontStyle1040.setSpacing(0.1)
FontStyle1040.setStyle("BOLD")

Text1039.setFontStyle(FontStyle1040)

Shape1038.setGeometry(Text1039)
Appearance1041 = Appearance()
Material1042 = Material()
Material1042.setDiffuseColor([0.6,0.6,0.6])

Appearance1041.setMaterial(Material1042)

Shape1038.setAppearance(Appearance1041)

Transform1036.addChildren(Shape1038)
Transform1043 = Transform()
Transform1043.setTranslation([0.5,0.075,-0.001])
Shape1044 = Shape()
Appearance1045 = Appearance()
Material1046 = Material()
Material1046.setDiffuseColor([0,1,0])
Material1046.setTransparency(1)

Appearance1045.setMaterial(Material1046)

Shape1044.setAppearance(Appearance1045)
Box1047 = Box()
Box1047.setSize([1,0.18,0.001])

Shape1044.setGeometry(Box1047)

Transform1043.addChildren(Shape1044)

Transform1036.addChildren(Transform1043)

Group1014.addChildren(Transform1036)

Transform949.addChildren(Group1014)

Transform948.addChildren(Transform949)

Collision947.setProxy(Transform948)

Group944.addChildren(Collision947)
Transform1048 = Transform()
Transform1048.setDEF("Floor")
Transform1048.setScale([1,0.0125,1])
Transform1048.setTranslation([0,-0.0125,0])
Shape1049 = Shape()
Box1050 = Box()

Shape1049.setGeometry(Box1050)
Appearance1051 = Appearance()
Material1052 = Material()

Appearance1051.setMaterial(Material1052)

Shape1049.setAppearance(Appearance1051)

Transform1048.addChildren(Shape1049)

Group944.addChildren(Transform1048)

Scene24.addChildren(Group944)
ROUTE1053 = ROUTE()
ROUTE1053.setFromField("position_changed")
ROUTE1053.setFromNode("HudProx")
ROUTE1053.setToField("set_translation")
ROUTE1053.setToNode("HudXform")

Scene24.addChildren(ROUTE1053)
ROUTE1054 = ROUTE()
ROUTE1054.setFromField("orientation_changed")
ROUTE1054.setFromNode("HudProx")
ROUTE1054.setToField("set_rotation")
ROUTE1054.setToNode("HudXform")

Scene24.addChildren(ROUTE1054)
Script1055 = Script()
Script1055.setDEF("ActorAnimator")
Script1055.setDirectOutput(True)
#***********Interfaces*****************
#Joint Nodes
#**************Avatar choice***************
#*************Behavior fields************
field1056 = field()
field1056.setName("changeBehaviorToWalk")
field1056.setAccessType("inputOnly")
field1056.setType("SFBool")

Script1055.addField(field1056)
field1057 = field()
field1057.setName("changeBehaviorToRun")
field1057.setAccessType("inputOnly")
field1057.setType("SFBool")

Script1055.addField(field1057)
field1058 = field()
field1058.setName("changeBehaviorToJump")
field1058.setAccessType("inputOnly")
field1058.setType("SFBool")

Script1055.addField(field1058)
field1059 = field()
field1059.setName("changeBehaviorToStand")
field1059.setAccessType("inputOnly")
field1059.setType("SFBool")

Script1055.addField(field1059)
field1060 = field()
field1060.setName("changeBehaviorToKneel")
field1060.setAccessType("inputOnly")
field1060.setType("SFBool")

Script1055.addField(field1060)
field1061 = field()
field1061.setName("switchAvatarToAllen")
field1061.setAccessType("inputOnly")
field1061.setType("SFBool")

Script1055.addField(field1061)
field1062 = field()
field1062.setName("switchAvatarToNancy")
field1062.setAccessType("inputOnly")
field1062.setType("SFBool")

Script1055.addField(field1062)
field1063 = field()
field1063.setName("switchAvatarToBoxman")
field1063.setAccessType("inputOnly")
field1063.setType("SFBool")

Script1055.addField(field1063)
field1064 = field()
field1064.setName("NancyJointNodes")
field1064.setAccessType("initializeOnly")
field1064.setType("MFNode")
#TODO ensure name attribute not needed as part of USE node
ProtoInstance1065 = ProtoInstance()
ProtoInstance1065.setUSE("Nancy_hanim_humanoid_root")

field1064.addChildren(ProtoInstance1065)
ProtoInstance1066 = ProtoInstance()
ProtoInstance1066.setUSE("Nancy_hanim_sacroiliac")

field1064.addChildren(ProtoInstance1066)
ProtoInstance1067 = ProtoInstance()
ProtoInstance1067.setUSE("Nancy_hanim_l_hip")

field1064.addChildren(ProtoInstance1067)
ProtoInstance1068 = ProtoInstance()
ProtoInstance1068.setUSE("Nancy_hanim_l_knee")

field1064.addChildren(ProtoInstance1068)
ProtoInstance1069 = ProtoInstance()
ProtoInstance1069.setUSE("Nancy_hanim_l_ankle")

field1064.addChildren(ProtoInstance1069)
ProtoInstance1070 = ProtoInstance()
ProtoInstance1070.setUSE("Nancy_hanim_r_hip")

field1064.addChildren(ProtoInstance1070)
ProtoInstance1071 = ProtoInstance()
ProtoInstance1071.setUSE("Nancy_hanim_r_knee")

field1064.addChildren(ProtoInstance1071)
ProtoInstance1072 = ProtoInstance()
ProtoInstance1072.setUSE("Nancy_hanim_r_ankle")

field1064.addChildren(ProtoInstance1072)
ProtoInstance1073 = ProtoInstance()
ProtoInstance1073.setUSE("Nancy_hanim_skullbase")

field1064.addChildren(ProtoInstance1073)
ProtoInstance1074 = ProtoInstance()
ProtoInstance1074.setUSE("Nancy_hanim_l_shoulder")

field1064.addChildren(ProtoInstance1074)
ProtoInstance1075 = ProtoInstance()
ProtoInstance1075.setUSE("Nancy_hanim_l_elbow")

field1064.addChildren(ProtoInstance1075)
ProtoInstance1076 = ProtoInstance()
ProtoInstance1076.setUSE("Nancy_hanim_l_wrist")

field1064.addChildren(ProtoInstance1076)
ProtoInstance1077 = ProtoInstance()
ProtoInstance1077.setUSE("Nancy_hanim_r_shoulder")

field1064.addChildren(ProtoInstance1077)
ProtoInstance1078 = ProtoInstance()
ProtoInstance1078.setUSE("Nancy_hanim_r_elbow")

field1064.addChildren(ProtoInstance1078)
ProtoInstance1079 = ProtoInstance()
ProtoInstance1079.setUSE("Nancy_hanim_r_wrist")

field1064.addChildren(ProtoInstance1079)

Script1055.addField(field1064)
field1080 = field()
field1080.setName("AllenJointNodes")
field1080.setAccessType("initializeOnly")
field1080.setType("MFNode")
ProtoInstance1081 = ProtoInstance()
ProtoInstance1081.setUSE("Allen_hanim_humanoid_root")

field1080.addChildren(ProtoInstance1081)
ProtoInstance1082 = ProtoInstance()
ProtoInstance1082.setUSE("Allen_hanim_sacroiliac")

field1080.addChildren(ProtoInstance1082)
ProtoInstance1083 = ProtoInstance()
ProtoInstance1083.setUSE("Allen_hanim_skullbase")

field1080.addChildren(ProtoInstance1083)
ProtoInstance1084 = ProtoInstance()
ProtoInstance1084.setUSE("Allen_hanim_l_hip")

field1080.addChildren(ProtoInstance1084)
ProtoInstance1085 = ProtoInstance()
ProtoInstance1085.setUSE("Allen_hanim_r_hip")

field1080.addChildren(ProtoInstance1085)
ProtoInstance1086 = ProtoInstance()
ProtoInstance1086.setUSE("Allen_hanim_l_knee")

field1080.addChildren(ProtoInstance1086)
ProtoInstance1087 = ProtoInstance()
ProtoInstance1087.setUSE("Allen_hanim_r_knee")

field1080.addChildren(ProtoInstance1087)
ProtoInstance1088 = ProtoInstance()
ProtoInstance1088.setUSE("Allen_hanim_l_ankle")

field1080.addChildren(ProtoInstance1088)
ProtoInstance1089 = ProtoInstance()
ProtoInstance1089.setUSE("Allen_hanim_r_ankle")

field1080.addChildren(ProtoInstance1089)
ProtoInstance1090 = ProtoInstance()
ProtoInstance1090.setUSE("Allen_hanim_l_shoulder")

field1080.addChildren(ProtoInstance1090)
ProtoInstance1091 = ProtoInstance()
ProtoInstance1091.setUSE("Allen_hanim_r_shoulder")

field1080.addChildren(ProtoInstance1091)
ProtoInstance1092 = ProtoInstance()
ProtoInstance1092.setUSE("Allen_hanim_l_elbow")

field1080.addChildren(ProtoInstance1092)
ProtoInstance1093 = ProtoInstance()
ProtoInstance1093.setUSE("Allen_hanim_r_elbow")

field1080.addChildren(ProtoInstance1093)
ProtoInstance1094 = ProtoInstance()
ProtoInstance1094.setUSE("Allen_hanim_l_wrist")

field1080.addChildren(ProtoInstance1094)
ProtoInstance1095 = ProtoInstance()
ProtoInstance1095.setUSE("Allen_hanim_r_wrist")

field1080.addChildren(ProtoInstance1095)

Script1055.addField(field1080)
field1096 = field()
field1096.setName("BoxmanJointNodes")
field1096.setAccessType("initializeOnly")
field1096.setType("MFNode")
HAnimJoint1097 = HAnimJoint()
HAnimJoint1097.setUSE("Boxman_humanoid_root")

field1096.addJoints(HAnimJoint1097)
HAnimJoint1098 = HAnimJoint()
HAnimJoint1098.setUSE("Boxman_skullbase")

field1096.addJoints(HAnimJoint1098)
HAnimJoint1099 = HAnimJoint()
HAnimJoint1099.setUSE("Boxman_vl5")

field1096.addJoints(HAnimJoint1099)
HAnimJoint1100 = HAnimJoint()
HAnimJoint1100.setUSE("Boxman_l_hip")

field1096.addJoints(HAnimJoint1100)
HAnimJoint1101 = HAnimJoint()
HAnimJoint1101.setUSE("Boxman_r_hip")

field1096.addJoints(HAnimJoint1101)
HAnimJoint1102 = HAnimJoint()
HAnimJoint1102.setUSE("Boxman_l_knee")

field1096.addJoints(HAnimJoint1102)
HAnimJoint1103 = HAnimJoint()
HAnimJoint1103.setUSE("Boxman_r_knee")

field1096.addJoints(HAnimJoint1103)
HAnimJoint1104 = HAnimJoint()
HAnimJoint1104.setUSE("Boxman_l_ankle")

field1096.addJoints(HAnimJoint1104)
HAnimJoint1105 = HAnimJoint()
HAnimJoint1105.setUSE("Boxman_r_ankle")

field1096.addJoints(HAnimJoint1105)
HAnimJoint1106 = HAnimJoint()
HAnimJoint1106.setUSE("Boxman_l_shoulder")

field1096.addJoints(HAnimJoint1106)
HAnimJoint1107 = HAnimJoint()
HAnimJoint1107.setUSE("Boxman_r_shoulder")

field1096.addJoints(HAnimJoint1107)
HAnimJoint1108 = HAnimJoint()
HAnimJoint1108.setUSE("Boxman_l_elbow")

field1096.addJoints(HAnimJoint1108)
HAnimJoint1109 = HAnimJoint()
HAnimJoint1109.setUSE("Boxman_r_elbow")

field1096.addJoints(HAnimJoint1109)
HAnimJoint1110 = HAnimJoint()
HAnimJoint1110.setUSE("Boxman_l_wrist")

field1096.addJoints(HAnimJoint1110)
HAnimJoint1111 = HAnimJoint()
HAnimJoint1111.setUSE("Boxman_r_wrist")

field1096.addJoints(HAnimJoint1111)
HAnimJoint1112 = HAnimJoint()
HAnimJoint1112.setUSE("Boxman_l_midtarsal")

field1096.addJoints(HAnimJoint1112)
HAnimJoint1113 = HAnimJoint()
HAnimJoint1113.setUSE("Boxman_r_midtarsal")

field1096.addJoints(HAnimJoint1113)

Script1055.addField(field1096)
field1114 = field()
field1114.setName("AvatarChoice")
field1114.setAccessType("outputOnly")
field1114.setType("SFInt32")

Script1055.addField(field1114)
field1115 = field()
field1115.setName("Behaviors")
field1115.setAccessType("initializeOnly")
field1115.setType("MFNode")
ProtoInstance1116 = ProtoInstance()
ProtoInstance1116.setUSE("WALK")

field1115.addChildren(ProtoInstance1116)
ProtoInstance1117 = ProtoInstance()
ProtoInstance1117.setUSE("RUN")

field1115.addChildren(ProtoInstance1117)
ProtoInstance1118 = ProtoInstance()
ProtoInstance1118.setUSE("JUMP")

field1115.addChildren(ProtoInstance1118)
ProtoInstance1119 = ProtoInstance()
ProtoInstance1119.setUSE("STAND")

field1115.addChildren(ProtoInstance1119)
ProtoInstance1120 = ProtoInstance()
ProtoInstance1120.setUSE("KNEEL")

field1115.addChildren(ProtoInstance1120)

Script1055.addField(field1115)

Script1055.setSourceCode('''ecmascript:\n"+
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
"}''')

Scene24.addChildren(Script1055)
#***********Script routes*************
ROUTE1121 = ROUTE()
ROUTE1121.setFromField("AvatarChoice")
ROUTE1121.setFromNode("ActorAnimator")
ROUTE1121.setToField("whichChoice")
ROUTE1121.setToNode("AvatarSwitch")

Scene24.addChildren(ROUTE1121)
#*************Behavior Touch Sensor Routes**************
ROUTE1122 = ROUTE()
ROUTE1122.setFromField("isActive")
ROUTE1122.setFromNode("Walk_Touch")
ROUTE1122.setToField("changeBehaviorToWalk")
ROUTE1122.setToNode("ActorAnimator")

Scene24.addChildren(ROUTE1122)
ROUTE1123 = ROUTE()
ROUTE1123.setFromField("isActive")
ROUTE1123.setFromNode("Run_Touch")
ROUTE1123.setToField("changeBehaviorToRun")
ROUTE1123.setToNode("ActorAnimator")

Scene24.addChildren(ROUTE1123)
ROUTE1124 = ROUTE()
ROUTE1124.setFromField("isActive")
ROUTE1124.setFromNode("Jump_Touch")
ROUTE1124.setToField("changeBehaviorToJump")
ROUTE1124.setToNode("ActorAnimator")

Scene24.addChildren(ROUTE1124)
ROUTE1125 = ROUTE()
ROUTE1125.setFromField("isActive")
ROUTE1125.setFromNode("Stand_Touch")
ROUTE1125.setToField("changeBehaviorToStand")
ROUTE1125.setToNode("ActorAnimator")

Scene24.addChildren(ROUTE1125)
ROUTE1126 = ROUTE()
ROUTE1126.setFromField("isActive")
ROUTE1126.setFromNode("Kneel_Touch")
ROUTE1126.setToField("changeBehaviorToKneel")
ROUTE1126.setToNode("ActorAnimator")

Scene24.addChildren(ROUTE1126)
ROUTE1127 = ROUTE()
ROUTE1127.setFromField("touchTime")
ROUTE1127.setFromNode("Kneel_Touch")
ROUTE1127.setToField("set_startTime")
ROUTE1127.setToNode("KNEEL")

Scene24.addChildren(ROUTE1127)
#*************Avatar Name Touch Sensor Routes**************
ROUTE1128 = ROUTE()
ROUTE1128.setFromField("isActive")
ROUTE1128.setFromNode("Allen_Touch")
ROUTE1128.setToField("switchAvatarToAllen")
ROUTE1128.setToNode("ActorAnimator")

Scene24.addChildren(ROUTE1128)
ROUTE1129 = ROUTE()
ROUTE1129.setFromField("isActive")
ROUTE1129.setFromNode("Nancy_Touch")
ROUTE1129.setToField("switchAvatarToNancy")
ROUTE1129.setToNode("ActorAnimator")

Scene24.addChildren(ROUTE1129)
ROUTE1130 = ROUTE()
ROUTE1130.setFromField("isActive")
ROUTE1130.setFromNode("Boxman_Touch")
ROUTE1130.setToField("switchAvatarToBoxman")
ROUTE1130.setToNode("ActorAnimator")

Scene24.addChildren(ROUTE1130)
ROUTE1131 = ROUTE()
ROUTE1131.setFromField("rotation_changed")
ROUTE1131.setFromNode("Boxman_r_elbow")
ROUTE1131.setToField("update")
ROUTE1131.setToNode("ENGINE")

Scene24.addChildren(ROUTE1131)

X3D0.setScene(Scene24)
X3D0.toFileX3D("././InterchangableActorsViaDynamicRoutingPrototypes_RoundTrip.x3d")
