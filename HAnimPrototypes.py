print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"
head1 = x3d.head()
#Originally these fundamental prototypes were defined in InterchangableActorsViaDynamicRoutingPrototypes.x3d
meta2 = x3d.meta()
meta2.name = "title"
meta2.content = "HAnimPrototypes.x3d"

head1.children.append(meta2)
meta3 = x3d.meta()
meta3.name = "description"
meta3.content = "Example implementation of X3D Humanoid Animation (HAnim) nodes using X3D prototypes."

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.name = "warning"
meta4.content = "These are developmental examples that can assist X3D player implementations and support interoperability. They are not intended for author use in regular X3D scenes."

head1.children.append(meta4)
meta5 = x3d.meta()
meta5.name = "warning"
meta5.content = "Developer note: names for these HAnim Prototypes need to be corrected if used internally in an X3D player implementation (e.g. Joint to HAnimJoint)."

head1.children.append(meta5)
meta6 = x3d.meta()
meta6.name = "warning"
meta6.content = "Need support for skin"

head1.children.append(meta6)
meta7 = x3d.meta()
meta7.name = "creator"
meta7.content = "Ozan APAYDIN, Don Brutzman"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.name = "translator"
meta8.content = "Ozan APAYDIN, Don Brutzman"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "created"
meta9.content = "15 November 2001"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "modified"
meta10.content = "23 May 2020"

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.name = "TODO"
meta11.content = "upgrade to match support requirements for HAnim 2.2"

head1.children.append(meta11)
meta12 = x3d.meta()
meta12.name = "reference"
meta12.content = "https://www.web3d.org/files/specifications/19774/V1.0/HAnim/HAnim.html"

head1.children.append(meta12)
meta13 = x3d.meta()
meta13.name = "reference"
meta13.content = "https://www.web3d.org/files/specifications/19775-1/V3.3/Part01/components/hanim.html"

head1.children.append(meta13)
meta14 = x3d.meta()
meta14.name = "reference"
meta14.content = "http://HAnim.org/Models/HAnim2001/boxman/boxman.wrl"

head1.children.append(meta14)
meta15 = x3d.meta()
meta15.name = "reference"
meta15.content = "http://HAnim.org/Specifications/HAnim2001"

head1.children.append(meta15)
meta16 = x3d.meta()
meta16.name = "reference"
meta16.content = "http://www.HAnim.org"

head1.children.append(meta16)
meta17 = x3d.meta()
meta17.name = "reference"
meta17.content = "http://HAnim.org/Models"

head1.children.append(meta17)
meta18 = x3d.meta()
meta18.name = "reference"
meta18.content = "http://HAnim.org/Specifications"

head1.children.append(meta18)
meta19 = x3d.meta()
meta19.name = "reference"
meta19.content = "InterchangableActorsViaDynamicRoutingPrototypes.x3d"

head1.children.append(meta19)
meta20 = x3d.meta()
meta20.name = "identifier"
meta20.content = "https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Prototypes/HAnimPrototypes.x3d"

head1.children.append(meta20)
meta21 = x3d.meta()
meta21.name = "generator"
meta21.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"

head1.children.append(meta21)
meta22 = x3d.meta()
meta22.name = "license"
meta22.content = "../license.html"

head1.children.append(meta22)

X3D0.head = head1
Scene23 = x3d.Scene()
#**********Human Model Protypes*********
ProtoDeclare24 = x3d.ProtoDeclare()
ProtoDeclare24.name = "Humanoid1_1"
ProtoDeclare24.appinfo = "The Humanoid node serves as overall container for the Joint Segment Site and Viewpoint nodes which define the skeleton geometry and landmarks of the humanoid figure. Additionally the node provides a means for defining information about the author copyright and usage restrictions of the model."
ProtoDeclare24.documentation = "http://HAnim.org/Specifications/HAnim2001/part1/Humanoid.html"
ProtoInterface25 = x3d.ProtoInterface()
#HAnim v1.1 field definitions
field26 = x3d.field()
field26.name = "name"
field26.accessType = "inputOutput"
field26.type = "SFString"

ProtoInterface25.field.append(field26)
field27 = x3d.field()
field27.name = "version"
field27.accessType = "inputOutput"
field27.appinfo = "legal values: 1.1 or 2.0"
field27.type = "SFString"
field27.value = "1.1"

ProtoInterface25.field.append(field27)
field28 = x3d.field()
field28.name = "humanoidVersion"
field28.accessType = "inputOutput"
field28.appinfo = "Version of the humanoid being modeled. Hint: HAnim version 2.0"
field28.type = "SFString"

ProtoInterface25.field.append(field28)
field29 = x3d.field()
field29.name = "info"
field29.accessType = "inputOutput"
field29.type = "MFString"

ProtoInterface25.field.append(field29)
field30 = x3d.field()
field30.name = "translation"
field30.accessType = "inputOutput"
field30.type = "SFVec3f"
field30.value = [0,0,0]

ProtoInterface25.field.append(field30)
field31 = x3d.field()
field31.name = "rotation"
field31.accessType = "inputOutput"
field31.type = "SFRotation"
field31.value = [0,0,1,0]

ProtoInterface25.field.append(field31)
field32 = x3d.field()
field32.name = "center"
field32.accessType = "inputOutput"
field32.type = "SFVec3f"
field32.value = [0,0,0]

ProtoInterface25.field.append(field32)
field33 = x3d.field()
field33.name = "scale"
field33.accessType = "inputOutput"
field33.type = "SFVec3f"
field33.value = [1,1,1]

ProtoInterface25.field.append(field33)
field34 = x3d.field()
field34.name = "scaleOrientation"
field34.accessType = "inputOutput"
field34.type = "SFRotation"
field34.value = [0,0,1,0]

ProtoInterface25.field.append(field34)
field35 = x3d.field()
field35.name = "bboxCenter"
field35.accessType = "initializeOnly"
field35.type = "SFVec3f"
field35.value = [0,0,0]

ProtoInterface25.field.append(field35)
field36 = x3d.field()
field36.name = "bboxSize"
field36.accessType = "initializeOnly"
field36.type = "SFVec3f"
field36.value = [-1,-1,-1]

ProtoInterface25.field.append(field36)
field37 = x3d.field()
field37.name = "humanoidBody"
field37.accessType = "inputOutput"
field37.appinfo = "HAnim 1.1 field container for body head. Hint: replaced by 2.0 skeleton."
field37.documentation = "http://HAnim.org/Specifications/HAnim1.1/#humanoid"
field37.type = "MFNode"

ProtoInterface25.field.append(field37)
field38 = x3d.field()
field38.name = "skeleton"
field38.accessType = "inputOutput"
field38.appinfo = "HAnim 2.0 field container for body geometry Hint: replaces 1.1 humanoidBody"
field38.documentation = "http://HAnim.org/Specifications/HAnim2001/part1/Humanoid.html"
field38.type = "MFNode"

ProtoInterface25.field.append(field38)
field39 = x3d.field()
field39.name = "joints"
field39.accessType = "inputOutput"
field39.appinfo = "Container field for Joint nodes"
field39.type = "MFNode"

ProtoInterface25.field.append(field39)
field40 = x3d.field()
field40.name = "segments"
field40.accessType = "inputOutput"
field40.appinfo = "Container field for Segment nodes"
field40.type = "MFNode"

ProtoInterface25.field.append(field40)
field41 = x3d.field()
field41.name = "sites"
field41.accessType = "inputOutput"
field41.appinfo = "Container field for Site nodes"
field41.type = "MFNode"

ProtoInterface25.field.append(field41)
field42 = x3d.field()
field42.name = "viewpoints"
field42.accessType = "inputOutput"
field42.appinfo = "Container field for Viewpoint nodes"
field42.type = "MFNode"

ProtoInterface25.field.append(field42)
field43 = x3d.field()
field43.name = "skinCoord"
field43.accessType = "inputOutput"
field43.appinfo = "Hint: HAnim version 2.0"
field43.type = "SFNode"
#NULL

ProtoInterface25.field.append(field43)
field44 = x3d.field()
field44.name = "skinNormal"
field44.accessType = "inputOutput"
field44.appinfo = "Hint: HAnim version 2.0"
field44.type = "SFNode"
#NULL

ProtoInterface25.field.append(field44)

ProtoDeclare24.ProtoInterface = ProtoInterface25
ProtoBody45 = x3d.ProtoBody()
Transform46 = x3d.Transform()
Transform46.DEF = "HumanoidTransform"
IS47 = x3d.IS()
connect48 = x3d.connect()
connect48.nodeField = "translation"
connect48.protoField = "translation"

IS47.connect.append(connect48)
connect49 = x3d.connect()
connect49.nodeField = "rotation"
connect49.protoField = "rotation"

IS47.connect.append(connect49)
connect50 = x3d.connect()
connect50.nodeField = "center"
connect50.protoField = "center"

IS47.connect.append(connect50)
connect51 = x3d.connect()
connect51.nodeField = "scale"
connect51.protoField = "scale"

IS47.connect.append(connect51)
connect52 = x3d.connect()
connect52.nodeField = "scaleOrientation"
connect52.protoField = "scaleOrientation"

IS47.connect.append(connect52)
connect53 = x3d.connect()
connect53.nodeField = "bboxCenter"
connect53.protoField = "bboxCenter"

IS47.connect.append(connect53)
connect54 = x3d.connect()
connect54.nodeField = "bboxSize"
connect54.protoField = "bboxSize"

IS47.connect.append(connect54)

Transform46.IS = IS47
Group55 = x3d.Group()
Group55.DEF = "HumanoidGroup1"
IS56 = x3d.IS()
connect57 = x3d.connect()
connect57.nodeField = "children"
connect57.protoField = "humanoidBody"

IS56.connect.append(connect57)

Group55.IS = IS56

Transform46.children.append(Group55)
Group58 = x3d.Group()
Group58.DEF = "HumanoidGroup2"
IS59 = x3d.IS()
connect60 = x3d.connect()
connect60.nodeField = "children"
connect60.protoField = "skeleton"

IS59.connect.append(connect60)

Group58.IS = IS59

Transform46.children.append(Group58)
Group61 = x3d.Group()
Group61.DEF = "HumanoidGroup3"
IS62 = x3d.IS()
connect63 = x3d.connect()
connect63.nodeField = "children"
connect63.protoField = "viewpoints"

IS62.connect.append(connect63)

Group61.IS = IS62

Transform46.children.append(Group61)

ProtoBody45.children.append(Transform46)

ProtoDeclare24.ProtoBody = ProtoBody45

Scene23.children.append(ProtoDeclare24)
ProtoDeclare64 = x3d.ProtoDeclare()
ProtoDeclare64.name = "Joint"
ProtoDeclare64.appinfo = "The Joint node is used as a building block to describe the articulations of the humanoid figure. Each articulation of the humanoid figure is represented by a Joint node each of which is organized into a hierarchy that describes the overall skeleton of the humanoid."
ProtoDeclare64.documentation = "http://HAnim.org/Specifications/HAnim2001/part1/Joint.html"
ProtoInterface65 = x3d.ProtoInterface()
field66 = x3d.field()
field66.name = "name"
field66.accessType = "inputOutput"
field66.type = "SFString"

ProtoInterface65.field.append(field66)
field67 = x3d.field()
field67.name = "ulimit"
field67.accessType = "inputOutput"
field67.type = "MFFloat"

ProtoInterface65.field.append(field67)
field68 = x3d.field()
field68.name = "llimit"
field68.accessType = "inputOutput"
field68.type = "MFFloat"

ProtoInterface65.field.append(field68)
field69 = x3d.field()
field69.name = "limitOrientation"
field69.accessType = "inputOutput"
field69.type = "SFRotation"
field69.value = [0,0,1,0]

ProtoInterface65.field.append(field69)
field70 = x3d.field()
field70.name = "skinCoordIndex"
field70.accessType = "inputOutput"
field70.type = "MFInt32"

ProtoInterface65.field.append(field70)
field71 = x3d.field()
field71.name = "skinCoordWeight"
field71.accessType = "inputOutput"
field71.type = "MFFloat"

ProtoInterface65.field.append(field71)
field72 = x3d.field()
field72.name = "stiffness"
field72.accessType = "inputOutput"
field72.type = "MFFloat"
field72.value = [0,0,0]

ProtoInterface65.field.append(field72)
field73 = x3d.field()
field73.name = "translation"
field73.accessType = "inputOutput"
field73.type = "SFVec3f"
field73.value = [0,0,0]

ProtoInterface65.field.append(field73)
field74 = x3d.field()
field74.name = "rotation"
field74.accessType = "inputOutput"
field74.type = "SFRotation"
field74.value = [0,0,1,0]

ProtoInterface65.field.append(field74)
field75 = x3d.field()
field75.name = "scale"
field75.accessType = "inputOutput"
field75.type = "SFVec3f"
field75.value = [1,1,1]

ProtoInterface65.field.append(field75)
field76 = x3d.field()
field76.name = "scaleOrientation"
field76.accessType = "inputOutput"
field76.type = "SFRotation"
field76.value = [0,0,1,0]

ProtoInterface65.field.append(field76)
field77 = x3d.field()
field77.name = "center"
field77.accessType = "inputOutput"
field77.type = "SFVec3f"
field77.value = [0,0,0]

ProtoInterface65.field.append(field77)
field78 = x3d.field()
field78.name = "bboxCenter"
field78.accessType = "initializeOnly"
field78.type = "SFVec3f"
field78.value = [0,0,0]

ProtoInterface65.field.append(field78)
field79 = x3d.field()
field79.name = "bboxSize"
field79.accessType = "initializeOnly"
field79.type = "SFVec3f"
field79.value = [-1,-1,-1]

ProtoInterface65.field.append(field79)
field80 = x3d.field()
field80.name = "children"
field80.accessType = "inputOutput"
field80.type = "MFNode"

ProtoInterface65.field.append(field80)
field81 = x3d.field()
field81.name = "addChildren"
field81.accessType = "inputOnly"
field81.type = "MFNode"

ProtoInterface65.field.append(field81)
field82 = x3d.field()
field82.name = "removeChildren"
field82.accessType = "inputOnly"
field82.type = "MFNode"

ProtoInterface65.field.append(field82)

ProtoDeclare64.ProtoInterface = ProtoInterface65
ProtoBody83 = x3d.ProtoBody()
Transform84 = x3d.Transform()
Transform84.DEF = "JointTransform"
IS85 = x3d.IS()
connect86 = x3d.connect()
connect86.nodeField = "translation"
connect86.protoField = "translation"

IS85.connect.append(connect86)
connect87 = x3d.connect()
connect87.nodeField = "rotation"
connect87.protoField = "rotation"

IS85.connect.append(connect87)
connect88 = x3d.connect()
connect88.nodeField = "center"
connect88.protoField = "center"

IS85.connect.append(connect88)
connect89 = x3d.connect()
connect89.nodeField = "scale"
connect89.protoField = "scale"

IS85.connect.append(connect89)
connect90 = x3d.connect()
connect90.nodeField = "scaleOrientation"
connect90.protoField = "scaleOrientation"

IS85.connect.append(connect90)
connect91 = x3d.connect()
connect91.nodeField = "bboxCenter"
connect91.protoField = "bboxCenter"

IS85.connect.append(connect91)
connect92 = x3d.connect()
connect92.nodeField = "bboxSize"
connect92.protoField = "bboxSize"

IS85.connect.append(connect92)
connect93 = x3d.connect()
connect93.nodeField = "children"
connect93.protoField = "children"

IS85.connect.append(connect93)
connect94 = x3d.connect()
connect94.nodeField = "addChildren"
connect94.protoField = "addChildren"

IS85.connect.append(connect94)
connect95 = x3d.connect()
connect95.nodeField = "removeChildren"
connect95.protoField = "removeChildren"

IS85.connect.append(connect95)

Transform84.IS = IS85

ProtoBody83.children.append(Transform84)

ProtoDeclare64.ProtoBody = ProtoBody83

Scene23.children.append(ProtoDeclare64)
ProtoDeclare96 = x3d.ProtoDeclare()
ProtoDeclare96.name = "Segment"
ProtoDeclare96.appinfo = "The Segment node is used describe the attributes of the physical links between the joints of the humanoid figure. Each body part (pelvis thigh calf etc.) of the humanoid figure is represented by a Segment node."
ProtoDeclare96.documentation = "http://HAnim.org/Specifications/HAnim2001/part1/Segment.html"
ProtoInterface97 = x3d.ProtoInterface()
field98 = x3d.field()
field98.name = "name"
field98.accessType = "inputOutput"
field98.type = "SFString"

ProtoInterface97.field.append(field98)
field99 = x3d.field()
field99.name = "mass"
field99.accessType = "inputOutput"
field99.type = "SFFloat"
field99.value = 0

ProtoInterface97.field.append(field99)
field100 = x3d.field()
field100.name = "centerOfMass"
field100.accessType = "inputOutput"
field100.type = "SFVec3f"
field100.value = [0,0,0]

ProtoInterface97.field.append(field100)
field101 = x3d.field()
field101.name = "momentsOfInertia"
field101.accessType = "inputOutput"
field101.type = "MFFloat"
field101.value = [0,0,0,0,0,0,0,0,0]

ProtoInterface97.field.append(field101)
field102 = x3d.field()
field102.name = "bboxCenter"
field102.accessType = "initializeOnly"
field102.type = "SFVec3f"
field102.value = [0,0,0]

ProtoInterface97.field.append(field102)
field103 = x3d.field()
field103.name = "bboxSize"
field103.accessType = "initializeOnly"
field103.type = "SFVec3f"
field103.value = [-1,-1,-1]

ProtoInterface97.field.append(field103)
field104 = x3d.field()
field104.name = "children"
field104.accessType = "inputOutput"
field104.type = "MFNode"

ProtoInterface97.field.append(field104)
field105 = x3d.field()
field105.name = "addChildren"
field105.accessType = "inputOnly"
field105.type = "MFNode"

ProtoInterface97.field.append(field105)
field106 = x3d.field()
field106.name = "removeChildren"
field106.accessType = "inputOnly"
field106.type = "MFNode"

ProtoInterface97.field.append(field106)
field107 = x3d.field()
field107.name = "coord"
field107.accessType = "inputOutput"
field107.appinfo = "contains Coordinate nodes"
field107.type = "SFNode"
#NULL

ProtoInterface97.field.append(field107)
field108 = x3d.field()
field108.name = "displacers"
field108.accessType = "inputOutput"
field108.appinfo = "contains Displacer nodes"
field108.type = "MFNode"

ProtoInterface97.field.append(field108)

ProtoDeclare96.ProtoInterface = ProtoInterface97
ProtoBody109 = x3d.ProtoBody()
Group110 = x3d.Group()
Group110.DEF = "SegmentGroup"
IS111 = x3d.IS()
connect112 = x3d.connect()
connect112.nodeField = "bboxCenter"
connect112.protoField = "bboxCenter"

IS111.connect.append(connect112)
connect113 = x3d.connect()
connect113.nodeField = "bboxSize"
connect113.protoField = "bboxSize"

IS111.connect.append(connect113)
connect114 = x3d.connect()
connect114.nodeField = "children"
connect114.protoField = "children"

IS111.connect.append(connect114)
connect115 = x3d.connect()
connect115.nodeField = "addChildren"
connect115.protoField = "addChildren"

IS111.connect.append(connect115)
connect116 = x3d.connect()
connect116.nodeField = "removeChildren"
connect116.protoField = "removeChildren"

IS111.connect.append(connect116)

Group110.IS = IS111

ProtoBody109.children.append(Group110)

ProtoDeclare96.ProtoBody = ProtoBody109

Scene23.children.append(ProtoDeclare96)
ProtoDeclare117 = x3d.ProtoDeclare()
ProtoDeclare117.name = "Site"
ProtoDeclare117.appinfo = "The Site node can be used for three purposes: (a) to define an \"end effector\" location which can be used by an inverse kinematics system (b) to define an attachment point for accessories such as jewelry and clothing and (c) to define a location for a virtual camera in the reference frame of a Segment node (such as a view \"through the eyes\" of the humanoid for use in multi-user worlds)."
ProtoDeclare117.documentation = "http://HAnim.org/Specifications/HAnim2001/part1/Site.html"
ProtoInterface118 = x3d.ProtoInterface()
field119 = x3d.field()
field119.name = "name"
field119.accessType = "inputOutput"
field119.type = "SFString"

ProtoInterface118.field.append(field119)
field120 = x3d.field()
field120.name = "translation"
field120.accessType = "inputOutput"
field120.type = "SFVec3f"
field120.value = [0,0,0]

ProtoInterface118.field.append(field120)
field121 = x3d.field()
field121.name = "rotation"
field121.accessType = "inputOutput"
field121.type = "SFRotation"
field121.value = [0,0,1,0]

ProtoInterface118.field.append(field121)
field122 = x3d.field()
field122.name = "scale"
field122.accessType = "inputOutput"
field122.type = "SFVec3f"
field122.value = [1,1,1]

ProtoInterface118.field.append(field122)
field123 = x3d.field()
field123.name = "scaleOrientation"
field123.accessType = "inputOutput"
field123.type = "SFRotation"
field123.value = [0,0,1,0]

ProtoInterface118.field.append(field123)
field124 = x3d.field()
field124.name = "center"
field124.accessType = "inputOutput"
field124.type = "SFVec3f"
field124.value = [0,0,0]

ProtoInterface118.field.append(field124)
field125 = x3d.field()
field125.name = "bboxCenter"
field125.accessType = "initializeOnly"
field125.type = "SFVec3f"
field125.value = [0,0,0]

ProtoInterface118.field.append(field125)
field126 = x3d.field()
field126.name = "bboxSize"
field126.accessType = "initializeOnly"
field126.type = "SFVec3f"
field126.value = [-1,-1,-1]

ProtoInterface118.field.append(field126)
field127 = x3d.field()
field127.name = "children"
field127.accessType = "inputOutput"
field127.type = "MFNode"

ProtoInterface118.field.append(field127)
field128 = x3d.field()
field128.name = "addChildren"
field128.accessType = "inputOnly"
field128.type = "MFNode"

ProtoInterface118.field.append(field128)
field129 = x3d.field()
field129.name = "removeChildren"
field129.accessType = "inputOnly"
field129.type = "MFNode"

ProtoInterface118.field.append(field129)

ProtoDeclare117.ProtoInterface = ProtoInterface118
ProtoBody130 = x3d.ProtoBody()
Transform131 = x3d.Transform()
Transform131.DEF = "SiteTransform"
IS132 = x3d.IS()
connect133 = x3d.connect()
connect133.nodeField = "translation"
connect133.protoField = "translation"

IS132.connect.append(connect133)
connect134 = x3d.connect()
connect134.nodeField = "rotation"
connect134.protoField = "rotation"

IS132.connect.append(connect134)
connect135 = x3d.connect()
connect135.nodeField = "center"
connect135.protoField = "center"

IS132.connect.append(connect135)
connect136 = x3d.connect()
connect136.nodeField = "scale"
connect136.protoField = "scale"

IS132.connect.append(connect136)
connect137 = x3d.connect()
connect137.nodeField = "scaleOrientation"
connect137.protoField = "scaleOrientation"

IS132.connect.append(connect137)
connect138 = x3d.connect()
connect138.nodeField = "bboxCenter"
connect138.protoField = "bboxCenter"

IS132.connect.append(connect138)
connect139 = x3d.connect()
connect139.nodeField = "bboxSize"
connect139.protoField = "bboxSize"

IS132.connect.append(connect139)
connect140 = x3d.connect()
connect140.nodeField = "children"
connect140.protoField = "children"

IS132.connect.append(connect140)
connect141 = x3d.connect()
connect141.nodeField = "addChildren"
connect141.protoField = "addChildren"

IS132.connect.append(connect141)
connect142 = x3d.connect()
connect142.nodeField = "removeChildren"
connect142.protoField = "removeChildren"

IS132.connect.append(connect142)

Transform131.IS = IS132

ProtoBody130.children.append(Transform131)

ProtoDeclare117.ProtoBody = ProtoBody130

Scene23.children.append(ProtoDeclare117)
ProtoDeclare143 = x3d.ProtoDeclare()
ProtoDeclare143.name = "Displacer"
ProtoDeclare143.appinfo = "A Displacer can be used in three different ways: (a) identify the vertices corresponding to a particular feature on a Segment (b) represent a particular muscular action which displaces the vertices in various directions (linearly or radially) and (c) represent a complete configuration of the vertices in a Segment."
ProtoDeclare143.documentation = "http://HAnim.org/Specifications/HAnim2001/part1/Displacer.html"
ProtoInterface144 = x3d.ProtoInterface()
field145 = x3d.field()
field145.name = "name"
field145.accessType = "inputOutput"
field145.type = "SFString"

ProtoInterface144.field.append(field145)
field146 = x3d.field()
field146.name = "coordIndex"
field146.accessType = "inputOutput"
field146.type = "MFInt32"

ProtoInterface144.field.append(field146)
field147 = x3d.field()
field147.name = "displacements"
field147.accessType = "inputOutput"
field147.type = "MFVec3f"

ProtoInterface144.field.append(field147)

ProtoDeclare143.ProtoInterface = ProtoInterface144
ProtoBody148 = x3d.ProtoBody()
WorldInfo149 = x3d.WorldInfo()
WorldInfo149.info = ["null body node"]

ProtoBody148.children.append(WorldInfo149)

ProtoDeclare143.ProtoBody = ProtoBody148

Scene23.children.append(ProtoDeclare143)
Shape150 = x3d.Shape()
Text151 = x3d.Text()
Text151.string = ["Humanoid Animation","(HAnim) prototype","implementations"]
FontStyle152 = x3d.FontStyle()
FontStyle152.justify = ["MIDDLE","MIDDLE"]

Text151.fontStyle = FontStyle152

Shape150.geometry = Text151
Appearance153 = x3d.Appearance()
Material154 = x3d.Material()
Material154.ambientIntensity = 0.25
Material154.diffuseColor = [0.795918,0.505869,0.093315]
Material154.shininess = 0.39
Material154.specularColor = [0.923469,0.428866,0.006369]
#Universal Media Library: Autumn 9

Appearance153.material = Material154

Shape150.appearance = Appearance153

Scene23.children.append(Shape150)

X3D0.Scene = Scene23
f = open("././HAnimPrototypes_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
