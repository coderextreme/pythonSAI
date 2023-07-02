print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"
head1 = x3d.head()
meta2 = x3d.meta()
meta2.name = "title"
meta2.content = "NancyPrototypes.x3d"

head1.children.append(meta2)
meta3 = x3d.meta()
meta3.name = "creator"
meta3.content = "Cindy Ballreich"

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.name = "translators"
meta4.content = "Tom Miller and Don Brutzman, NPS"

head1.children.append(meta4)
meta5 = x3d.meta()
meta5.name = "created"
meta5.content = "9 July 2000"

head1.children.append(meta5)
meta6 = x3d.meta()
meta6.name = "modified"
meta6.content = "22 February 2022"

head1.children.append(meta6)
meta7 = x3d.meta()
meta7.name = "description"
meta7.content = "Canonical HAnim 1.1 specification example, using ProtoDeclaration and ProtoInstance instead of native X3D tags. Prototype definitions are a compatible combination of version 1.0 and 2.0 prototype interfaces."

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.name = "warning"
meta8.content = "using ProtoDeclare is only for developmental experimentation, use X3D native tags for Humanoids instead"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "reference"
meta9.content = "NancyNativeTags.x3d"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "TODO"
meta10.content = "Material color of neck and arms is ignored/incorrect in Xj3D, possily DEF/USE problem."

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.name = "identifier"
meta11.content = "https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Prototypes/NancyPrototypes.x3d"

head1.children.append(meta11)
meta12 = x3d.meta()
meta12.name = "generator"
meta12.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"

head1.children.append(meta12)
meta13 = x3d.meta()
meta13.name = "license"
meta13.content = "../license.html"

head1.children.append(meta13)

X3D0.head = head1
Scene14 = x3d.Scene()
ProtoDeclare15 = x3d.ProtoDeclare()
ProtoDeclare15.name = "Displacer"
ProtoDeclare15.appinfo = "A Displacer can be used in three different ways: (a) identify the vertices corresponding to a particular feature on a Segment (b) represent a particular muscular action which displaces the vertices in various directions (linearly or radially) and (c) represent a complete configuration of the vertices in a Segment."
ProtoDeclare15.documentation = "http://HAnim.org/Specifications/HAnim2001/part1/Displacer.html"
ProtoInterface16 = x3d.ProtoInterface()
field17 = x3d.field()
field17.name = "name"
field17.accessType = "inputOutput"
field17.type = "SFString"

ProtoInterface16.field.append(field17)
field18 = x3d.field()
field18.name = "coordIndex"
field18.accessType = "inputOutput"
field18.type = "MFInt32"

ProtoInterface16.field.append(field18)
field19 = x3d.field()
field19.name = "displacements"
field19.accessType = "inputOutput"
field19.type = "MFVec3f"

ProtoInterface16.field.append(field19)

ProtoDeclare15.ProtoInterface = ProtoInterface16
ProtoBody20 = x3d.ProtoBody()
WorldInfo21 = x3d.WorldInfo()
WorldInfo21.info = ["null body node"]

ProtoBody20.children.append(WorldInfo21)

ProtoDeclare15.ProtoBody = ProtoBody20

Scene14.children.append(ProtoDeclare15)
ProtoDeclare22 = x3d.ProtoDeclare()
ProtoDeclare22.name = "Humanoid"
ProtoDeclare22.appinfo = "The Humanoid node serves as overall container for the Joint Segment Site and Viewpoint nodes which define the skeleton geometry and landmarks of the humanoid figure. Additionally the node provides a means for defining information about the author copyright and usage restrictions of the model."
ProtoDeclare22.documentation = "http://HAnim.org/Specifications/HAnim2001/part1/Humanoid.html"
ProtoInterface23 = x3d.ProtoInterface()
#HAnim v1.1 field definitions
field24 = x3d.field()
field24.name = "name"
field24.accessType = "inputOutput"
field24.type = "SFString"

ProtoInterface23.field.append(field24)
field25 = x3d.field()
field25.name = "version"
field25.accessType = "inputOutput"
field25.appinfo = "legal values: 1.1 or 2.0"
field25.type = "SFString"
field25.value = "1.1"

ProtoInterface23.field.append(field25)
field26 = x3d.field()
field26.name = "humanoidVersion"
field26.accessType = "inputOutput"
field26.appinfo = "Version of the humanoid being modeled. Hint: HAnim version 2.0"
field26.type = "SFString"

ProtoInterface23.field.append(field26)
field27 = x3d.field()
field27.name = "info"
field27.accessType = "inputOutput"
field27.type = "MFString"

ProtoInterface23.field.append(field27)
field28 = x3d.field()
field28.name = "translation"
field28.accessType = "inputOutput"
field28.type = "SFVec3f"
field28.value = [0,0,0]

ProtoInterface23.field.append(field28)
field29 = x3d.field()
field29.name = "rotation"
field29.accessType = "inputOutput"
field29.type = "SFRotation"
field29.value = [0,0,1,0]

ProtoInterface23.field.append(field29)
field30 = x3d.field()
field30.name = "center"
field30.accessType = "inputOutput"
field30.type = "SFVec3f"
field30.value = [0,0,0]

ProtoInterface23.field.append(field30)
field31 = x3d.field()
field31.name = "scale"
field31.accessType = "inputOutput"
field31.type = "SFVec3f"
field31.value = [1,1,1]

ProtoInterface23.field.append(field31)
field32 = x3d.field()
field32.name = "scaleOrientation"
field32.accessType = "inputOutput"
field32.type = "SFRotation"
field32.value = [0,0,1,0]

ProtoInterface23.field.append(field32)
field33 = x3d.field()
field33.name = "bboxCenter"
field33.accessType = "initializeOnly"
field33.type = "SFVec3f"
field33.value = [0,0,0]

ProtoInterface23.field.append(field33)
field34 = x3d.field()
field34.name = "bboxSize"
field34.accessType = "initializeOnly"
field34.type = "SFVec3f"
field34.value = [-1,-1,-1]

ProtoInterface23.field.append(field34)
field35 = x3d.field()
field35.name = "humanoidBody"
field35.accessType = "inputOutput"
field35.appinfo = "HAnim 1.1 field container for body geometry Hint: replaced by 2.0 skeleton"
field35.documentation = "http://HAnim.org/Specifications/HAnim1.1/#humanoid"
field35.type = "MFNode"

ProtoInterface23.field.append(field35)
field36 = x3d.field()
field36.name = "skeleton"
field36.accessType = "inputOutput"
field36.appinfo = "HAnim 2.0 field container for body geometry Hint: replaces 1.1 humanoidBody"
field36.documentation = "http://HAnim.org/Specifications/HAnim2001/part1/Humanoid.html"
field36.type = "MFNode"

ProtoInterface23.field.append(field36)
field37 = x3d.field()
field37.name = "joints"
field37.accessType = "inputOutput"
field37.appinfo = "Container field for Joint nodes"
field37.type = "MFNode"

ProtoInterface23.field.append(field37)
field38 = x3d.field()
field38.name = "segments"
field38.accessType = "inputOutput"
field38.appinfo = "Container field for Segment nodes"
field38.type = "MFNode"

ProtoInterface23.field.append(field38)
field39 = x3d.field()
field39.name = "sites"
field39.accessType = "inputOutput"
field39.appinfo = "Container field for Site nodes"
field39.type = "MFNode"

ProtoInterface23.field.append(field39)
field40 = x3d.field()
field40.name = "viewpoints"
field40.accessType = "inputOutput"
field40.appinfo = "Container field for Viewpoint nodes"
field40.type = "MFNode"

ProtoInterface23.field.append(field40)
field41 = x3d.field()
field41.name = "skinCoord"
field41.accessType = "inputOutput"
field41.appinfo = "Hint: HAnim version 2.0"
field41.type = "SFNode"
#NULL node

ProtoInterface23.field.append(field41)
field42 = x3d.field()
field42.name = "skinNormal"
field42.accessType = "inputOutput"
field42.appinfo = "Hint: HAnim version 2.0"
field42.type = "SFNode"
#NULL node

ProtoInterface23.field.append(field42)

ProtoDeclare22.ProtoInterface = ProtoInterface23
ProtoBody43 = x3d.ProtoBody()
Transform44 = x3d.Transform()
Transform44.DEF = "HumanoidTransform"
IS45 = x3d.IS()
connect46 = x3d.connect()
connect46.nodeField = "translation"
connect46.protoField = "translation"

IS45.connect.append(connect46)
connect47 = x3d.connect()
connect47.nodeField = "rotation"
connect47.protoField = "rotation"

IS45.connect.append(connect47)
connect48 = x3d.connect()
connect48.nodeField = "scale"
connect48.protoField = "scale"

IS45.connect.append(connect48)
connect49 = x3d.connect()
connect49.nodeField = "scaleOrientation"
connect49.protoField = "scaleOrientation"

IS45.connect.append(connect49)
connect50 = x3d.connect()
connect50.nodeField = "center"
connect50.protoField = "center"

IS45.connect.append(connect50)
connect51 = x3d.connect()
connect51.nodeField = "bboxCenter"
connect51.protoField = "bboxCenter"

IS45.connect.append(connect51)
connect52 = x3d.connect()
connect52.nodeField = "bboxSize"
connect52.protoField = "bboxSize"

IS45.connect.append(connect52)

Transform44.IS = IS45
Group53 = x3d.Group()
Group53.DEF = "HumanoidGroup1"
IS54 = x3d.IS()
connect55 = x3d.connect()
connect55.nodeField = "children"
connect55.protoField = "humanoidBody"

IS54.connect.append(connect55)

Group53.IS = IS54

Transform44.children.append(Group53)
Group56 = x3d.Group()
Group56.DEF = "HumanoidGroup2"
IS57 = x3d.IS()
connect58 = x3d.connect()
connect58.nodeField = "children"
connect58.protoField = "skeleton"

IS57.connect.append(connect58)

Group56.IS = IS57

Transform44.children.append(Group56)
Group59 = x3d.Group()
Group59.DEF = "HumanoidGroup3"
IS60 = x3d.IS()
connect61 = x3d.connect()
connect61.nodeField = "children"
connect61.protoField = "viewpoints"

IS60.connect.append(connect61)

Group59.IS = IS60

Transform44.children.append(Group59)

ProtoBody43.children.append(Transform44)

ProtoDeclare22.ProtoBody = ProtoBody43

Scene14.children.append(ProtoDeclare22)
ProtoDeclare62 = x3d.ProtoDeclare()
ProtoDeclare62.name = "Joint"
ProtoDeclare62.appinfo = "The Joint node is used as a building block to describe the articulations of the humanoid figure. Each articulation of the humanoid figure is represented by a Joint node each of which is organized into a hierarchy that describes the overall skeleton of the humanoid."
ProtoDeclare62.documentation = "http://HAnim.org/Specifications/HAnim2001/part1/Joint.html"
ProtoInterface63 = x3d.ProtoInterface()
field64 = x3d.field()
field64.name = "name"
field64.accessType = "inputOutput"
field64.type = "SFString"

ProtoInterface63.field.append(field64)
field65 = x3d.field()
field65.name = "ulimit"
field65.accessType = "inputOutput"
field65.type = "MFFloat"

ProtoInterface63.field.append(field65)
field66 = x3d.field()
field66.name = "llimit"
field66.accessType = "inputOutput"
field66.type = "MFFloat"

ProtoInterface63.field.append(field66)
field67 = x3d.field()
field67.name = "limitOrientation"
field67.accessType = "inputOutput"
field67.type = "SFRotation"
field67.value = [0,0,1,0]

ProtoInterface63.field.append(field67)
field68 = x3d.field()
field68.name = "skinCoordIndex"
field68.accessType = "inputOutput"
field68.type = "MFInt32"

ProtoInterface63.field.append(field68)
field69 = x3d.field()
field69.name = "skinCoordWeight"
field69.accessType = "inputOutput"
field69.type = "MFFloat"

ProtoInterface63.field.append(field69)
field70 = x3d.field()
field70.name = "stiffness"
field70.accessType = "inputOutput"
field70.type = "MFFloat"
field70.value = [0,0,0]

ProtoInterface63.field.append(field70)
field71 = x3d.field()
field71.name = "translation"
field71.accessType = "inputOutput"
field71.type = "SFVec3f"
field71.value = [0,0,0]

ProtoInterface63.field.append(field71)
field72 = x3d.field()
field72.name = "rotation"
field72.accessType = "inputOutput"
field72.type = "SFRotation"
field72.value = [0,0,1,0]

ProtoInterface63.field.append(field72)
field73 = x3d.field()
field73.name = "scale"
field73.accessType = "inputOutput"
field73.type = "SFVec3f"
field73.value = [1,1,1]

ProtoInterface63.field.append(field73)
field74 = x3d.field()
field74.name = "scaleOrientation"
field74.accessType = "inputOutput"
field74.type = "SFRotation"
field74.value = [0,0,1,0]

ProtoInterface63.field.append(field74)
field75 = x3d.field()
field75.name = "center"
field75.accessType = "inputOutput"
field75.type = "SFVec3f"
field75.value = [0,0,0]

ProtoInterface63.field.append(field75)
field76 = x3d.field()
field76.name = "bboxCenter"
field76.accessType = "initializeOnly"
field76.type = "SFVec3f"
field76.value = [0,0,0]

ProtoInterface63.field.append(field76)
field77 = x3d.field()
field77.name = "bboxSize"
field77.accessType = "initializeOnly"
field77.type = "SFVec3f"
field77.value = [-1,-1,-1]

ProtoInterface63.field.append(field77)
field78 = x3d.field()
field78.name = "children"
field78.accessType = "inputOutput"
field78.type = "MFNode"

ProtoInterface63.field.append(field78)
field79 = x3d.field()
field79.name = "addChildren"
field79.accessType = "inputOnly"
field79.type = "MFNode"

ProtoInterface63.field.append(field79)
field80 = x3d.field()
field80.name = "removeChildren"
field80.accessType = "inputOnly"
field80.type = "MFNode"

ProtoInterface63.field.append(field80)

ProtoDeclare62.ProtoInterface = ProtoInterface63
ProtoBody81 = x3d.ProtoBody()
Transform82 = x3d.Transform()
Transform82.DEF = "JointTransform"
IS83 = x3d.IS()
connect84 = x3d.connect()
connect84.nodeField = "translation"
connect84.protoField = "translation"

IS83.connect.append(connect84)
connect85 = x3d.connect()
connect85.nodeField = "rotation"
connect85.protoField = "rotation"

IS83.connect.append(connect85)
connect86 = x3d.connect()
connect86.nodeField = "scale"
connect86.protoField = "scale"

IS83.connect.append(connect86)
connect87 = x3d.connect()
connect87.nodeField = "scaleOrientation"
connect87.protoField = "scaleOrientation"

IS83.connect.append(connect87)
connect88 = x3d.connect()
connect88.nodeField = "center"
connect88.protoField = "center"

IS83.connect.append(connect88)
connect89 = x3d.connect()
connect89.nodeField = "bboxCenter"
connect89.protoField = "bboxCenter"

IS83.connect.append(connect89)
connect90 = x3d.connect()
connect90.nodeField = "bboxSize"
connect90.protoField = "bboxSize"

IS83.connect.append(connect90)
connect91 = x3d.connect()
connect91.nodeField = "children"
connect91.protoField = "children"

IS83.connect.append(connect91)
connect92 = x3d.connect()
connect92.nodeField = "addChildren"
connect92.protoField = "addChildren"

IS83.connect.append(connect92)
connect93 = x3d.connect()
connect93.nodeField = "removeChildren"
connect93.protoField = "removeChildren"

IS83.connect.append(connect93)

Transform82.IS = IS83

ProtoBody81.children.append(Transform82)

ProtoDeclare62.ProtoBody = ProtoBody81

Scene14.children.append(ProtoDeclare62)
ProtoDeclare94 = x3d.ProtoDeclare()
ProtoDeclare94.name = "Segment"
ProtoDeclare94.appinfo = "The Segment node is used describe the attributes of the physical links between the joints of the humanoid figure. Each body part (pelvis thigh calf etc) of the humanoid figure is represented by a Segment node."
ProtoDeclare94.documentation = "http://HAnim.org/Specifications/HAnim2001/part1/Segment.html"
ProtoInterface95 = x3d.ProtoInterface()
field96 = x3d.field()
field96.name = "name"
field96.accessType = "inputOutput"
field96.type = "SFString"

ProtoInterface95.field.append(field96)
field97 = x3d.field()
field97.name = "mass"
field97.accessType = "inputOutput"
field97.type = "SFFloat"
field97.value = 0

ProtoInterface95.field.append(field97)
field98 = x3d.field()
field98.name = "centerOfMass"
field98.accessType = "inputOutput"
field98.type = "SFVec3f"
field98.value = [0,0,0]

ProtoInterface95.field.append(field98)
field99 = x3d.field()
field99.name = "momentsOfInertia"
field99.accessType = "inputOutput"
field99.type = "MFFloat"
field99.value = [0,0,0,0,0,0,0,0,0]

ProtoInterface95.field.append(field99)
field100 = x3d.field()
field100.name = "bboxCenter"
field100.accessType = "initializeOnly"
field100.type = "SFVec3f"
field100.value = [0,0,0]

ProtoInterface95.field.append(field100)
field101 = x3d.field()
field101.name = "bboxSize"
field101.accessType = "initializeOnly"
field101.type = "SFVec3f"
field101.value = [-1,-1,-1]

ProtoInterface95.field.append(field101)
field102 = x3d.field()
field102.name = "children"
field102.accessType = "inputOutput"
field102.type = "MFNode"

ProtoInterface95.field.append(field102)
field103 = x3d.field()
field103.name = "addChildren"
field103.accessType = "inputOnly"
field103.type = "MFNode"

ProtoInterface95.field.append(field103)
field104 = x3d.field()
field104.name = "removeChildren"
field104.accessType = "inputOnly"
field104.type = "MFNode"

ProtoInterface95.field.append(field104)
field105 = x3d.field()
field105.name = "coord"
field105.accessType = "inputOutput"
field105.appinfo = "contains Coordinate nodes"
field105.type = "SFNode"
#NULL node

ProtoInterface95.field.append(field105)
field106 = x3d.field()
field106.name = "displacers"
field106.accessType = "inputOutput"
field106.appinfo = "contains Displacer nodes"
field106.type = "MFNode"

ProtoInterface95.field.append(field106)

ProtoDeclare94.ProtoInterface = ProtoInterface95
ProtoBody107 = x3d.ProtoBody()
Group108 = x3d.Group()
Group108.DEF = "SegmentGroup"
IS109 = x3d.IS()
connect110 = x3d.connect()
connect110.nodeField = "bboxCenter"
connect110.protoField = "bboxCenter"

IS109.connect.append(connect110)
connect111 = x3d.connect()
connect111.nodeField = "bboxSize"
connect111.protoField = "bboxSize"

IS109.connect.append(connect111)
connect112 = x3d.connect()
connect112.nodeField = "children"
connect112.protoField = "children"

IS109.connect.append(connect112)
connect113 = x3d.connect()
connect113.nodeField = "addChildren"
connect113.protoField = "addChildren"

IS109.connect.append(connect113)
connect114 = x3d.connect()
connect114.nodeField = "removeChildren"
connect114.protoField = "removeChildren"

IS109.connect.append(connect114)

Group108.IS = IS109

ProtoBody107.children.append(Group108)

ProtoDeclare94.ProtoBody = ProtoBody107

Scene14.children.append(ProtoDeclare94)
ProtoDeclare115 = x3d.ProtoDeclare()
ProtoDeclare115.name = "Site"
ProtoDeclare115.appinfo = "The Site node can be used for three purposes: (a) to define an \"end effector\" location which can be used by an inverse kinematics system (b) to define an attachment point for accessories such as jewelry and clothing and (c) to define a location for a virtual camera in the reference frame of a Segment node (such as a view \"through the eyes\" of the humanoid for use in multi-user worlds)."
ProtoDeclare115.documentation = "http://HAnim.org/Specifications/HAnim2001/part1/Site.html"
ProtoInterface116 = x3d.ProtoInterface()
field117 = x3d.field()
field117.name = "name"
field117.accessType = "inputOutput"
field117.type = "SFString"

ProtoInterface116.field.append(field117)
field118 = x3d.field()
field118.name = "translation"
field118.accessType = "inputOutput"
field118.type = "SFVec3f"
field118.value = [0,0,0]

ProtoInterface116.field.append(field118)
field119 = x3d.field()
field119.name = "rotation"
field119.accessType = "inputOutput"
field119.type = "SFRotation"
field119.value = [0,0,1,0]

ProtoInterface116.field.append(field119)
field120 = x3d.field()
field120.name = "scale"
field120.accessType = "inputOutput"
field120.type = "SFVec3f"
field120.value = [1,1,1]

ProtoInterface116.field.append(field120)
field121 = x3d.field()
field121.name = "scaleOrientation"
field121.accessType = "inputOutput"
field121.type = "SFRotation"
field121.value = [0,0,1,0]

ProtoInterface116.field.append(field121)
field122 = x3d.field()
field122.name = "center"
field122.accessType = "inputOutput"
field122.type = "SFVec3f"
field122.value = [0,0,0]

ProtoInterface116.field.append(field122)
field123 = x3d.field()
field123.name = "bboxCenter"
field123.accessType = "initializeOnly"
field123.type = "SFVec3f"
field123.value = [0,0,0]

ProtoInterface116.field.append(field123)
field124 = x3d.field()
field124.name = "bboxSize"
field124.accessType = "initializeOnly"
field124.type = "SFVec3f"
field124.value = [-1,-1,-1]

ProtoInterface116.field.append(field124)
field125 = x3d.field()
field125.name = "children"
field125.accessType = "inputOutput"
field125.type = "MFNode"

ProtoInterface116.field.append(field125)
field126 = x3d.field()
field126.name = "addChildren"
field126.accessType = "inputOnly"
field126.type = "MFNode"

ProtoInterface116.field.append(field126)
field127 = x3d.field()
field127.name = "removeChildren"
field127.accessType = "inputOnly"
field127.type = "MFNode"

ProtoInterface116.field.append(field127)

ProtoDeclare115.ProtoInterface = ProtoInterface116
ProtoBody128 = x3d.ProtoBody()
Transform129 = x3d.Transform()
Transform129.DEF = "SiteTransform"
IS130 = x3d.IS()
connect131 = x3d.connect()
connect131.nodeField = "translation"
connect131.protoField = "translation"

IS130.connect.append(connect131)
connect132 = x3d.connect()
connect132.nodeField = "rotation"
connect132.protoField = "rotation"

IS130.connect.append(connect132)
connect133 = x3d.connect()
connect133.nodeField = "scale"
connect133.protoField = "scale"

IS130.connect.append(connect133)
connect134 = x3d.connect()
connect134.nodeField = "scaleOrientation"
connect134.protoField = "scaleOrientation"

IS130.connect.append(connect134)
connect135 = x3d.connect()
connect135.nodeField = "center"
connect135.protoField = "center"

IS130.connect.append(connect135)
connect136 = x3d.connect()
connect136.nodeField = "bboxCenter"
connect136.protoField = "bboxCenter"

IS130.connect.append(connect136)
connect137 = x3d.connect()
connect137.nodeField = "bboxSize"
connect137.protoField = "bboxSize"

IS130.connect.append(connect137)
connect138 = x3d.connect()
connect138.nodeField = "children"
connect138.protoField = "children"

IS130.connect.append(connect138)
connect139 = x3d.connect()
connect139.nodeField = "addChildren"
connect139.protoField = "addChildren"

IS130.connect.append(connect139)
connect140 = x3d.connect()
connect140.nodeField = "removeChildren"
connect140.protoField = "removeChildren"

IS130.connect.append(connect140)

Transform129.IS = IS130

ProtoBody128.children.append(Transform129)

ProtoDeclare115.ProtoBody = ProtoBody128

Scene14.children.append(ProtoDeclare115)
#Start scene graph.
ProtoInstance141 = x3d.ProtoInstance()
ProtoInstance141.name = "Humanoid"
ProtoInstance141.DEF = "Humanoid"
fieldValue142 = x3d.fieldValue()
fieldValue142.name = "name"
fieldValue142.value = "nancy"

ProtoInstance141.fieldValue.append(fieldValue142)
fieldValue143 = x3d.fieldValue()
fieldValue143.name = "version"
fieldValue143.value = "1.1"

ProtoInstance141.fieldValue.append(fieldValue143)
fieldValue144 = x3d.fieldValue()
fieldValue144.name = "info"
fieldValue144.value = "\"humanoidVersion=Nancy V1.2b\" \"authorName=Cindy Ballreich\" \"authorEmail=cindy@ballreich.net\" \"copyright=1997 3Name3D / Yglesias Wallock Divekar Inc. all rights reserved.\" \"creationDate=Tue Dec 30 08:30:08 PST 1997\" \"usageRestrictions=Noncommercial usage is ok if 3Name3D name and logo www.ballreich.net/vrml/HAnim/small_logo.gif is present and proper credit is given.\""

ProtoInstance141.fieldValue.append(fieldValue144)
fieldValue145 = x3d.fieldValue()
fieldValue145.name = "humanoidBody"
ProtoInstance146 = x3d.ProtoInstance()
ProtoInstance146.name = "Joint"
ProtoInstance146.DEF = "hanim_humanoid_root"
fieldValue147 = x3d.fieldValue()
fieldValue147.name = "name"
fieldValue147.value = "humanoid_root"

ProtoInstance146.fieldValue.append(fieldValue147)
fieldValue148 = x3d.fieldValue()
fieldValue148.name = "center"
fieldValue148.value = "-0.00405 0.855 -0.000113"

ProtoInstance146.fieldValue.append(fieldValue148)
fieldValue149 = x3d.fieldValue()
fieldValue149.name = "children"
ProtoInstance150 = x3d.ProtoInstance()
ProtoInstance150.name = "Joint"
ProtoInstance150.DEF = "hanim_sacroiliac"
fieldValue151 = x3d.fieldValue()
fieldValue151.name = "name"
fieldValue151.value = "sacroiliac"

ProtoInstance150.fieldValue.append(fieldValue151)
fieldValue152 = x3d.fieldValue()
fieldValue152.name = "center"
fieldValue152.value = "0 1.01 -0.0204"

ProtoInstance150.fieldValue.append(fieldValue152)
fieldValue153 = x3d.fieldValue()
fieldValue153.name = "children"
ProtoInstance154 = x3d.ProtoInstance()
ProtoInstance154.name = "Segment"
ProtoInstance154.DEF = "hanim_pelvis"
fieldValue155 = x3d.fieldValue()
fieldValue155.name = "name"
fieldValue155.value = "pelvis"

ProtoInstance154.fieldValue.append(fieldValue155)
fieldValue156 = x3d.fieldValue()
fieldValue156.name = "children"
Shape157 = x3d.Shape()
Appearance158 = x3d.Appearance()
Material159 = x3d.Material()
Material159.DEF = "Pants_Color"
Material159.ambientIntensity = 0.25
Material159.diffuseColor = [0.054,0.233,0.39]

Appearance158.material = Material159

Shape157.appearance = Appearance158
IndexedFaceSet160 = x3d.IndexedFaceSet()
IndexedFaceSet160.coordIndex = [0,1,40,-1,1,2,40,-1,2,3,40,-1,3,4,40,-1,4,5,40,-1,5,4,9,-1,4,3,8,-1,3,2,8,-1,2,1,6,-1,0,7,1,-1,7,6,1,-1,6,8,2,-1,9,4,10,-1,4,8,10,-1,8,6,12,-1,7,0,47,-1,50,5,9,-1,7,47,55,-1,55,13,7,-1,50,9,56,-1,9,10,14,-1,10,11,15,-1,11,12,16,-1,12,13,19,-1,13,55,17,-1,60,17,55,-1,17,19,13,-1,19,16,12,-1,16,15,11,-1,15,18,10,-1,14,56,9,-1,56,14,64,-1,17,60,20,-1,20,19,17,-1,21,64,14,-1,14,22,21,-1,15,16,24,-1,16,19,24,-1,19,20,26,-1,24,23,15,-1,64,21,69,-1,21,22,29,-1,19,26,25,-1,20,63,27,-1,27,26,20,-1,25,24,19,-1,30,29,22,-1,29,28,21,-1,28,69,21,-1,27,34,26,-1,69,28,79,-1,29,30,32,-1,30,23,33,-1,23,24,37,-1,25,26,34,-1,83,27,77,-1,37,33,23,-1,33,32,30,-1,31,79,28,-1,79,31,84,-1,32,33,36,-1,24,25,37,-1,34,27,83,-1,83,38,34,-1,34,37,25,-1,37,36,33,-1,36,35,32,-1,84,31,89,-1,31,35,89,-1,35,36,39,-1,36,37,39,-1,38,83,89,-1,89,39,38,-1,39,89,35,-1,40,41,0,-1,40,42,41,-1,40,43,42,-1,40,44,43,-1,40,45,44,-1,49,44,45,-1,48,43,44,-1,48,42,43,-1,46,41,42,-1,41,47,0,-1,41,46,47,-1,42,48,46,-1,51,44,49,-1,51,48,44,-1,48,52,53,-1,49,45,50,-1,56,49,50,-1,57,51,49,-1,58,53,52,-1,59,54,53,-1,62,55,54,-1,55,62,60,-1,54,59,62,-1,53,58,59,-1,51,61,58,-1,49,56,57,-1,64,57,56,-1,67,59,58,-1,68,62,59,-1,60,63,20,-1,60,62,63,-1,59,67,68,-1,58,61,67,-1,57,64,65,-1,65,66,57,-1,71,63,62,-1,69,65,64,-1,74,66,65,-1,78,68,67,-1,70,71,62,-1,63,72,27,-1,63,71,72,-1,68,78,76,-1,67,75,78,-1,66,74,75,-1,65,73,74,-1,65,69,73,-1,77,27,72,-1,71,82,72,-1,79,73,69,-1,81,75,74,-1,82,71,70,-1,77,72,83,-1,73,79,80,-1,84,80,79,-1,86,75,81,-1,83,72,82,-1,82,88,83,-1,70,87,82,-1,81,85,86,-1,89,80,84,-1,89,85,80,-1,90,86,85,-1,90,87,86,-1,89,83,88,-1,88,90,89,-1,85,89,90,-1,50,45,5,-1,45,40,5,-1,10,8,11,-1,8,12,11,-1,18,22,10,-1,22,14,10,-1,57,66,51,-1,66,61,51,-1,51,58,48,-1,58,52,48,-1,48,53,46,-1,53,54,46,-1,76,70,68,-1,70,62,68,-1,29,32,28,-1,28,32,31,-1,32,35,31,-1,85,81,80,-1,81,73,80,-1,81,74,73,-1,39,37,38,-1,37,34,38,-1,82,87,88,-1,87,90,88,-1,87,78,86,-1,78,75,86,-1,61,66,67,-1,66,75,67,-1,22,18,15,-1,23,30,15,-1,30,22,15,-1,13,12,7,-1,12,6,7,-1,46,54,47,-1,54,55,47,-1,87,76,78,-1,87,70,76,-1]
IndexedFaceSet160.creaseAngle = 1.14
Coordinate161 = x3d.Coordinate()

IndexedFaceSet160.coord = Coordinate161

Shape157.geometry = IndexedFaceSet160

fieldValue156.children.append(Shape157)

ProtoInstance154.fieldValue.append(fieldValue156)

fieldValue153.children.append(ProtoInstance154)
ProtoInstance162 = x3d.ProtoInstance()
ProtoInstance162.name = "Joint"
ProtoInstance162.DEF = "hanim_l_hip"
fieldValue163 = x3d.fieldValue()
fieldValue163.name = "name"
fieldValue163.value = "l_hip"

ProtoInstance162.fieldValue.append(fieldValue163)
fieldValue164 = x3d.fieldValue()
fieldValue164.name = "center"
fieldValue164.value = "0.122 0.888271 -0.0693267"

ProtoInstance162.fieldValue.append(fieldValue164)
fieldValue165 = x3d.fieldValue()
fieldValue165.name = "children"
ProtoInstance166 = x3d.ProtoInstance()
ProtoInstance166.name = "Segment"
ProtoInstance166.DEF = "hanim_l_thigh"
fieldValue167 = x3d.fieldValue()
fieldValue167.name = "name"
fieldValue167.value = "l_thigh"

ProtoInstance166.fieldValue.append(fieldValue167)
fieldValue168 = x3d.fieldValue()
fieldValue168.name = "children"
Shape169 = x3d.Shape()
Appearance170 = x3d.Appearance()
Material171 = x3d.Material()
Material171.USE = "Pants_Color"

Appearance170.material = Material171

Shape169.appearance = Appearance170
IndexedFaceSet172 = x3d.IndexedFaceSet()
IndexedFaceSet172.coordIndex = [0,4,5,-1,3,4,0,-1,0,7,1,-1,0,8,7,-1,0,6,8,-1,0,5,6,-1,0,2,3,-1,0,1,2,-1,9,2,1,-1,10,3,2,-1,11,4,3,-1,12,5,4,-1,13,6,5,-1,15,7,8,-1,9,1,7,-1,7,15,9,-1,8,14,15,-1,5,16,13,-1,5,12,16,-1,4,11,12,-1,3,10,11,-1,2,9,10,-1,20,13,16,-1,18,11,10,-1,19,12,11,-1,20,16,12,-1,23,15,14,-1,15,23,24,-1,12,19,20,-1,11,18,19,-1,10,17,18,-1,26,18,17,-1,27,19,18,-1,27,20,19,-1,28,21,20,-1,29,23,22,-1,23,29,30,-1,20,32,28,-1,20,27,32,-1,18,26,27,-1,17,25,26,-1,25,31,30,-1,30,29,26,-1,30,26,25,-1,29,28,27,-1,29,27,26,-1,28,32,27,-1,22,23,14,-1,20,21,13,-1,21,22,13,-1,22,14,13,-1,9,15,24,-1,10,9,17,-1,9,24,17,-1,6,13,8,-1,13,14,8,-1,28,29,21,-1,29,22,21,-1,24,31,17,-1,31,25,17,-1,30,31,23,-1,31,24,23,-1]
IndexedFaceSet172.creaseAngle = 1.32
Coordinate173 = x3d.Coordinate()

IndexedFaceSet172.coord = Coordinate173

Shape169.geometry = IndexedFaceSet172

fieldValue168.children.append(Shape169)

ProtoInstance166.fieldValue.append(fieldValue168)

fieldValue165.children.append(ProtoInstance166)
ProtoInstance174 = x3d.ProtoInstance()
ProtoInstance174.name = "Joint"
ProtoInstance174.DEF = "hanim_l_knee"
fieldValue175 = x3d.fieldValue()
fieldValue175.name = "name"
fieldValue175.value = "l_knee"

ProtoInstance174.fieldValue.append(fieldValue175)
fieldValue176 = x3d.fieldValue()
fieldValue176.name = "center"
fieldValue176.value = "0.0738 0.517 -0.0284"

ProtoInstance174.fieldValue.append(fieldValue176)
fieldValue177 = x3d.fieldValue()
fieldValue177.name = "children"
ProtoInstance178 = x3d.ProtoInstance()
ProtoInstance178.name = "Segment"
ProtoInstance178.DEF = "hanim_l_calf"
fieldValue179 = x3d.fieldValue()
fieldValue179.name = "name"
fieldValue179.value = "l_calf"

ProtoInstance178.fieldValue.append(fieldValue179)
fieldValue180 = x3d.fieldValue()
fieldValue180.name = "children"
Shape181 = x3d.Shape()
Appearance182 = x3d.Appearance()
Material183 = x3d.Material()
Material183.USE = "Pants_Color"

Appearance182.material = Material183

Shape181.appearance = Appearance182
IndexedFaceSet184 = x3d.IndexedFaceSet()
IndexedFaceSet184.coordIndex = [2,1,0,-1,2,3,1,-1,2,4,3,-1,2,5,4,-1,2,6,5,-1,2,7,6,-1,2,8,7,-1,2,0,8,-1,9,8,0,-1,10,6,7,-1,11,5,6,-1,12,4,5,-1,12,3,4,-1,13,1,3,-1,1,13,14,-1,3,12,13,-1,5,11,12,-1,6,10,11,-1,8,9,15,-1,22,13,12,-1,13,22,14,-1,17,15,9,-1,20,12,11,-1,21,22,12,-1,23,9,14,-1,9,23,16,-1,14,22,23,-1,12,20,21,-1,15,17,18,-1,9,16,17,-1,24,17,16,-1,25,18,17,-1,26,19,18,-1,27,20,19,-1,28,21,20,-1,29,22,21,-1,30,23,22,-1,31,16,23,-1,23,30,31,-1,22,29,30,-1,21,28,29,-1,20,27,28,-1,19,26,27,-1,18,25,26,-1,17,24,25,-1,16,31,24,-1,33,26,25,-1,36,29,28,-1,37,31,30,-1,29,36,30,-1,25,24,33,-1,31,37,24,-1,32,33,24,-1,24,37,32,-1,38,37,30,-1,30,36,38,-1,41,33,32,-1,42,39,34,-1,44,36,35,-1,45,38,36,-1,46,37,38,-1,38,45,46,-1,36,44,45,-1,35,43,44,-1,39,42,47,-1,32,40,41,-1,40,46,45,-1,41,40,45,-1,41,45,44,-1,44,43,42,-1,44,42,41,-1,43,47,42,-1,39,35,28,-1,35,36,28,-1,34,39,27,-1,39,28,27,-1,33,34,26,-1,34,27,26,-1,33,41,34,-1,41,42,34,-1,40,32,46,-1,32,37,46,-1,10,19,11,-1,19,20,11,-1,14,9,1,-1,9,0,1,-1,8,15,7,-1,7,15,10,-1,15,19,10,-1,15,18,19,-1,43,35,47,-1,35,39,47,-1]
IndexedFaceSet184.creaseAngle = 1.57
Coordinate185 = x3d.Coordinate()

IndexedFaceSet184.coord = Coordinate185

Shape181.geometry = IndexedFaceSet184

fieldValue180.children.append(Shape181)

ProtoInstance178.fieldValue.append(fieldValue180)

fieldValue177.children.append(ProtoInstance178)
ProtoInstance186 = x3d.ProtoInstance()
ProtoInstance186.name = "Joint"
ProtoInstance186.DEF = "hanim_l_ankle"
fieldValue187 = x3d.fieldValue()
fieldValue187.name = "name"
fieldValue187.value = "l_ankle"

ProtoInstance186.fieldValue.append(fieldValue187)
fieldValue188 = x3d.fieldValue()
fieldValue188.name = "center"
fieldValue188.value = "0.0645 0.0719 -0.048"

ProtoInstance186.fieldValue.append(fieldValue188)
fieldValue189 = x3d.fieldValue()
fieldValue189.name = "children"
ProtoInstance190 = x3d.ProtoInstance()
ProtoInstance190.name = "Segment"
ProtoInstance190.DEF = "hanim_l_hindfoot"
fieldValue191 = x3d.fieldValue()
fieldValue191.name = "name"
fieldValue191.value = "l_hindfoot"

ProtoInstance190.fieldValue.append(fieldValue191)
fieldValue192 = x3d.fieldValue()
fieldValue192.name = "children"
Shape193 = x3d.Shape()
Appearance194 = x3d.Appearance()
Material195 = x3d.Material()
Material195.DEF = "Shoe_Color"
Material195.ambientIntensity = 0.25

Appearance194.material = Material195

Shape193.appearance = Appearance194
IndexedFaceSet196 = x3d.IndexedFaceSet()
IndexedFaceSet196.coordIndex = [2,1,0,-1,4,3,1,-1,2,4,1,-1,3,6,5,-1,1,3,5,-1,6,8,7,-1,5,6,7,-1,8,10,9,-1,7,8,9,-1,10,12,11,-1,9,10,11,-1,12,14,13,-1,11,12,13,-1,14,16,15,-1,13,14,15,-1,16,18,17,-1,15,16,17,-1,18,20,19,-1,17,18,19,-1,20,22,21,-1,19,20,21,-1,22,24,23,-1,21,22,23,-1,24,25,0,-1,23,24,0,-1,25,4,2,-1,0,25,2,-1,18,26,20,-1,16,26,18,-1,27,26,16,-1,14,27,16,-1,12,27,14,-1,28,27,12,-1,29,28,12,-1,10,29,12,-1,8,29,10,-1,6,37,8,-1,24,30,25,-1,31,30,24,-1,22,31,24,-1,32,31,22,-1,20,32,22,-1,33,32,20,-1,26,33,20,-1,34,33,26,-1,27,34,26,-1,35,34,27,-1,28,35,27,-1,29,35,28,-1,36,35,29,-1,8,36,29,-1,37,36,8,-1,6,38,37,-1,3,38,6,-1,39,38,3,-1,30,39,25,-1,41,40,30,-1,31,41,30,-1,42,41,31,-1,32,42,31,-1,43,42,32,-1,33,43,32,-1,44,43,33,-1,34,44,33,-1,45,44,34,-1,35,45,34,-1,46,45,35,-1,36,46,35,-1,47,46,36,-1,37,47,36,-1,38,47,37,-1,48,47,38,-1,49,48,38,-1,39,49,38,-1,40,49,39,-1,30,40,39,-1,48,49,50,-1,47,48,50,-1,46,47,50,-1,45,46,50,-1,44,45,50,-1,43,44,50,-1,42,43,50,-1,41,42,50,-1,40,41,50,-1,49,40,50,-1,11,13,15,-1,11,15,17,-1,9,11,17,-1,9,17,19,-1,7,9,19,-1,7,19,21,-1,5,7,21,-1,5,21,23,-1,5,23,0,-1,1,5,0,-1,3,4,39,-1,4,25,39,-1]
IndexedFaceSet196.creaseAngle = 1.57
Coordinate197 = x3d.Coordinate()

IndexedFaceSet196.coord = Coordinate197

Shape193.geometry = IndexedFaceSet196

fieldValue192.children.append(Shape193)

ProtoInstance190.fieldValue.append(fieldValue192)

fieldValue189.children.append(ProtoInstance190)

ProtoInstance186.fieldValue.append(fieldValue189)

fieldValue177.children.append(ProtoInstance186)

ProtoInstance174.fieldValue.append(fieldValue177)

fieldValue165.children.append(ProtoInstance174)

ProtoInstance162.fieldValue.append(fieldValue165)

fieldValue153.children.append(ProtoInstance162)
ProtoInstance198 = x3d.ProtoInstance()
ProtoInstance198.name = "Joint"
ProtoInstance198.DEF = "hanim_r_hip"
fieldValue199 = x3d.fieldValue()
fieldValue199.name = "name"
fieldValue199.value = "r_hip"

ProtoInstance198.fieldValue.append(fieldValue199)
fieldValue200 = x3d.fieldValue()
fieldValue200.name = "center"
fieldValue200.value = "-0.11 0.892362 -0.0732533"

ProtoInstance198.fieldValue.append(fieldValue200)
fieldValue201 = x3d.fieldValue()
fieldValue201.name = "children"
ProtoInstance202 = x3d.ProtoInstance()
ProtoInstance202.name = "Segment"
ProtoInstance202.DEF = "hanim_r_thigh"
fieldValue203 = x3d.fieldValue()
fieldValue203.name = "name"
fieldValue203.value = "r_thigh"

ProtoInstance202.fieldValue.append(fieldValue203)
fieldValue204 = x3d.fieldValue()
fieldValue204.name = "children"
Shape205 = x3d.Shape()
Appearance206 = x3d.Appearance()
Material207 = x3d.Material()
Material207.USE = "Pants_Color"

Appearance206.material = Material207

Shape205.appearance = Appearance206
IndexedFaceSet208 = x3d.IndexedFaceSet()
IndexedFaceSet208.coordIndex = [5,4,0,-1,0,4,3,-1,1,7,0,-1,7,8,0,-1,8,6,0,-1,6,5,0,-1,3,2,0,-1,2,1,0,-1,1,2,9,-1,2,3,10,-1,3,4,11,-1,4,5,12,-1,5,6,13,-1,8,7,15,-1,7,1,9,-1,9,15,7,-1,15,14,8,-1,13,16,5,-1,16,12,5,-1,12,11,4,-1,11,10,3,-1,10,9,2,-1,12,16,20,-1,13,14,22,-1,14,15,23,-1,24,23,15,-1,23,22,14,-1,20,19,12,-1,17,18,26,-1,18,19,27,-1,19,20,27,-1,20,21,28,-1,22,23,29,-1,30,29,23,-1,27,26,18,-1,26,25,17,-1,30,31,25,-1,25,26,29,-1,25,29,30,-1,26,27,28,-1,26,28,29,-1,27,20,28,-1,24,15,9,-1,22,21,13,-1,29,28,22,-1,28,21,22,-1,24,31,23,-1,31,30,23,-1,25,31,17,-1,31,24,17,-1,17,24,10,-1,24,9,10,-1,18,10,11,-1,18,17,10,-1,18,12,19,-1,18,11,12,-1,21,20,13,-1,20,16,13,-1,14,13,8,-1,13,6,8,-1]
IndexedFaceSet208.creaseAngle = 1.61
Coordinate209 = x3d.Coordinate()

IndexedFaceSet208.coord = Coordinate209

Shape205.geometry = IndexedFaceSet208

fieldValue204.children.append(Shape205)

ProtoInstance202.fieldValue.append(fieldValue204)

fieldValue201.children.append(ProtoInstance202)
ProtoInstance210 = x3d.ProtoInstance()
ProtoInstance210.name = "Joint"
ProtoInstance210.DEF = "hanim_r_knee"
fieldValue211 = x3d.fieldValue()
fieldValue211.name = "name"
fieldValue211.value = "r_knee"

ProtoInstance210.fieldValue.append(fieldValue211)
fieldValue212 = x3d.fieldValue()
fieldValue212.name = "center"
fieldValue212.value = "-0.0699 0.51 -0.0166"

ProtoInstance210.fieldValue.append(fieldValue212)
fieldValue213 = x3d.fieldValue()
fieldValue213.name = "children"
ProtoInstance214 = x3d.ProtoInstance()
ProtoInstance214.name = "Segment"
ProtoInstance214.DEF = "hanim_r_calf"
fieldValue215 = x3d.fieldValue()
fieldValue215.name = "name"
fieldValue215.value = "r_calf"

ProtoInstance214.fieldValue.append(fieldValue215)
fieldValue216 = x3d.fieldValue()
fieldValue216.name = "children"
Shape217 = x3d.Shape()
Appearance218 = x3d.Appearance()
Material219 = x3d.Material()
Material219.USE = "Pants_Color"

Appearance218.material = Material219

Shape217.appearance = Appearance218
IndexedFaceSet220 = x3d.IndexedFaceSet()
IndexedFaceSet220.coordIndex = [14,25,18,-1,25,32,18,-1,32,27,18,-1,27,22,18,-1,22,10,18,-1,10,6,18,-1,6,8,18,-1,8,14,18,-1,14,8,17,-1,6,10,9,-1,10,22,24,-1,22,27,39,-1,27,32,39,-1,32,25,42,-1,25,14,30,-1,17,30,14,-1,30,42,25,-1,42,39,32,-1,39,24,22,-1,24,9,10,-1,4,17,8,-1,39,42,43,-1,30,43,42,-1,17,4,1,-1,24,39,26,-1,39,43,44,-1,30,17,34,-1,16,34,17,-1,34,43,30,-1,44,26,39,-1,0,1,4,-1,1,16,17,-1,16,1,3,-1,1,0,2,-1,0,5,7,-1,5,26,28,-1,26,44,45,-1,44,43,46,-1,43,34,36,-1,34,16,15,-1,15,36,34,-1,36,46,43,-1,46,45,44,-1,45,28,26,-1,28,7,5,-1,7,2,0,-1,2,3,1,-1,3,15,16,-1,45,46,37,-1,36,15,20,-1,36,37,46,-1,13,2,7,-1,3,20,15,-1,3,2,13,-1,36,20,29,-1,29,37,36,-1,13,21,23,-1,21,33,23,-1,41,37,40,-1,37,29,31,-1,29,20,19,-1,19,31,29,-1,31,40,37,-1,40,38,41,-1,35,23,33,-1,23,12,13,-1,12,11,13,-1,31,19,11,-1,40,31,11,-1,40,11,12,-1,12,23,38,-1,12,38,40,-1,23,35,38,-1,28,21,7,-1,21,13,7,-1,45,33,28,-1,33,21,28,-1,33,45,41,-1,45,37,41,-1,33,41,35,-1,41,38,35,-1,20,3,47,-1,11,19,47,-1,19,20,47,-1,13,47,3,-1,13,11,47,-1,4,8,6,-1,26,5,24,-1,5,9,24,-1,6,9,4,-1,9,0,4,-1,9,5,0,-1]
IndexedFaceSet220.creaseAngle = 1.57
Coordinate221 = x3d.Coordinate()

IndexedFaceSet220.coord = Coordinate221

Shape217.geometry = IndexedFaceSet220

fieldValue216.children.append(Shape217)

ProtoInstance214.fieldValue.append(fieldValue216)

fieldValue213.children.append(ProtoInstance214)
ProtoInstance222 = x3d.ProtoInstance()
ProtoInstance222.name = "Joint"
ProtoInstance222.DEF = "hanim_r_ankle"
fieldValue223 = x3d.fieldValue()
fieldValue223.name = "name"
fieldValue223.value = "r_ankle"

ProtoInstance222.fieldValue.append(fieldValue223)
fieldValue224 = x3d.fieldValue()
fieldValue224.name = "center"
fieldValue224.value = "-0.064 0.0753 -0.0412"

ProtoInstance222.fieldValue.append(fieldValue224)
fieldValue225 = x3d.fieldValue()
fieldValue225.name = "children"
ProtoInstance226 = x3d.ProtoInstance()
ProtoInstance226.name = "Segment"
ProtoInstance226.DEF = "hanim_r_hindfoot"
fieldValue227 = x3d.fieldValue()
fieldValue227.name = "name"
fieldValue227.value = "r_hindfoot"

ProtoInstance226.fieldValue.append(fieldValue227)
fieldValue228 = x3d.fieldValue()
fieldValue228.name = "children"
Shape229 = x3d.Shape()
Appearance230 = x3d.Appearance()
Material231 = x3d.Material()
Material231.USE = "Shoe_Color"

Appearance230.material = Material231

Shape229.appearance = Appearance230
IndexedFaceSet232 = x3d.IndexedFaceSet()
IndexedFaceSet232.coordIndex = [6,50,0,-1,50,8,7,-1,50,7,0,-1,1,9,8,-1,1,8,50,-1,49,10,9,-1,49,9,1,-1,46,11,10,-1,46,10,49,-1,2,12,11,-1,2,11,46,-1,3,13,12,-1,3,12,2,-1,4,14,13,-1,4,13,3,-1,45,14,4,-1,47,15,45,-1,19,15,47,-1,48,18,19,-1,5,16,18,-1,5,18,48,-1,6,17,16,-1,6,16,5,-1,0,7,17,-1,0,17,6,-1,14,20,21,-1,14,21,13,-1,13,21,12,-1,12,21,22,-1,12,22,11,-1,11,22,10,-1,17,23,16,-1,16,23,24,-1,16,24,18,-1,18,24,25,-1,18,25,19,-1,19,25,26,-1,19,26,15,-1,15,26,20,-1,20,26,27,-1,20,27,21,-1,21,27,28,-1,21,28,22,-1,22,28,29,-1,10,30,9,-1,9,30,31,-1,9,31,8,-1,8,31,32,-1,17,32,23,-1,23,33,34,-1,23,34,35,-1,23,35,24,-1,24,35,36,-1,24,36,25,-1,25,36,37,-1,25,37,26,-1,26,37,38,-1,26,38,27,-1,27,38,39,-1,27,39,28,-1,28,39,40,-1,28,40,29,-1,29,40,41,-1,29,41,30,-1,30,41,42,-1,30,42,31,-1,31,42,43,-1,31,43,32,-1,32,43,33,-1,32,33,23,-1,44,43,42,-1,44,42,41,-1,44,41,40,-1,44,40,39,-1,44,39,38,-1,44,38,37,-1,44,37,36,-1,44,36,35,-1,44,35,34,-1,44,34,33,-1,44,33,43,-1,4,3,2,-1,45,4,2,-1,45,2,46,-1,47,45,46,-1,48,46,49,-1,5,48,49,-1,5,49,1,-1,6,5,1,-1,6,1,50,-1,30,10,29,-1,10,22,29,-1,17,7,32,-1,7,8,32,-1,19,47,48,-1,47,46,48,-1,20,14,15,-1,14,45,15,-1]
IndexedFaceSet232.creaseAngle = 1.57
Coordinate233 = x3d.Coordinate()

IndexedFaceSet232.coord = Coordinate233

Shape229.geometry = IndexedFaceSet232

fieldValue228.children.append(Shape229)

ProtoInstance226.fieldValue.append(fieldValue228)

fieldValue225.children.append(ProtoInstance226)

ProtoInstance222.fieldValue.append(fieldValue225)

fieldValue213.children.append(ProtoInstance222)

ProtoInstance210.fieldValue.append(fieldValue213)

fieldValue201.children.append(ProtoInstance210)

ProtoInstance198.fieldValue.append(fieldValue201)

fieldValue153.children.append(ProtoInstance198)

ProtoInstance150.fieldValue.append(fieldValue153)

fieldValue149.children.append(ProtoInstance150)
ProtoInstance234 = x3d.ProtoInstance()
ProtoInstance234.name = "Joint"
ProtoInstance234.DEF = "hanim_vl1"
fieldValue235 = x3d.fieldValue()
fieldValue235.name = "name"
fieldValue235.value = "vl1"

ProtoInstance234.fieldValue.append(fieldValue235)
fieldValue236 = x3d.fieldValue()
fieldValue236.name = "center"
fieldValue236.value = "-0.00405 1.07 -0.0275"

ProtoInstance234.fieldValue.append(fieldValue236)
fieldValue237 = x3d.fieldValue()
fieldValue237.name = "children"
ProtoInstance238 = x3d.ProtoInstance()
ProtoInstance238.name = "Segment"
ProtoInstance238.DEF = "hanim_c7"
fieldValue239 = x3d.fieldValue()
fieldValue239.name = "name"
fieldValue239.value = "l1"

ProtoInstance238.fieldValue.append(fieldValue239)
fieldValue240 = x3d.fieldValue()
fieldValue240.name = "children"
Shape241 = x3d.Shape()
Appearance242 = x3d.Appearance()
Material243 = x3d.Material()
Material243.DEF = "Shirt_Color"
Material243.ambientIntensity = 0.25
Material243.diffuseColor = [0.6,0.0745,0.1137]

Appearance242.material = Material243
ImageTexture244 = x3d.ImageTexture()
ImageTexture244.DEF = "small_logo_Tex"
ImageTexture244.url = ["small_logo.gif","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Prototypes/small_logo.gif"]

Appearance242.texture = ImageTexture244

Shape241.appearance = Appearance242
IndexedFaceSet245 = x3d.IndexedFaceSet()
IndexedFaceSet245.coordIndex = [0,1,2,-1,3,0,2,-1,4,5,6,-1,6,7,4,-1,8,7,6,-1,6,9,8,-1,9,10,8,-1,6,5,11,-1,9,6,12,-1,11,12,6,-1,12,10,9,-1,7,8,13,-1,13,4,7,-1,14,15,16,-1,15,17,13,-1,4,13,17,-1,17,15,18,-1,13,19,15,-1,19,13,8,-1,19,16,15,-1,16,19,8,-1,17,20,4,-1,5,4,20,-1,18,21,17,-1,20,17,21,-1,16,22,14,-1,22,16,23,-1,8,23,16,-1,23,8,10,-1,24,25,26,-1,26,27,24,-1,25,28,26,-1,28,29,30,-1,30,26,28,-1,31,32,33,-1,32,25,33,-1,25,24,34,-1,33,25,34,-1,24,35,34,-1,27,35,24,-1,33,36,31,-1,27,26,37,-1,37,26,30,-1,38,37,30,-1,33,34,39,-1,39,34,35,-1,39,35,40,-1,41,38,30,-1,35,27,42,-1,37,42,27,-1,40,35,42,-1,42,37,43,-1,37,38,44,-1,44,43,37,-1,36,45,46,-1,36,33,45,-1,40,42,47,-1,43,47,42,-1,47,48,40,-1,39,40,48,-1,47,43,49,-1,43,44,49,-1,50,49,44,-1,51,46,52,-1,46,45,52,-1,52,45,53,-1,33,53,45,-1,33,39,53,-1,49,54,47,-1,48,47,54,-1,55,56,52,-1,57,52,53,-1,57,55,52,-1,58,57,53,-1,59,58,53,-1,53,39,59,-1,39,48,59,-1,59,48,54,-1,58,59,60,-1,54,49,61,-1,59,54,61,-1,60,59,61,-1,49,50,62,-1,63,62,50,-1,62,61,49,-1,64,63,50,-1,63,64,65,-1,65,62,63,-1,66,60,61,-1,62,65,67,-1,68,67,65,-1,64,69,70,-1,64,70,65,-1,70,68,65,-1,69,71,72,-1,72,70,69,-1,73,74,75,-1,66,76,60,-1,67,77,62,-1,62,77,61,-1,77,66,61,-1,66,77,78,-1,77,67,79,-1,79,67,68,-1,79,78,77,-1,68,70,80,-1,70,72,80,-1,80,79,68,-1,74,73,81,-1,73,76,82,-1,82,81,73,-1,76,66,83,-1,78,83,66,-1,83,82,76,-1,78,79,84,-1,79,80,84,-1,84,85,78,-1,86,84,80,-1,81,82,87,-1,87,88,81,-1,82,83,89,-1,83,78,89,-1,89,87,82,-1,78,85,89,-1,90,91,92,-1,92,93,90,-1,90,94,91,-1,95,96,94,-1,94,90,95,-1,29,96,97,-1,96,95,97,-1,97,30,29,-1,30,97,41,-1,41,97,95,-1,98,99,100,-1,98,91,99,-1,101,92,91,-1,98,101,91,-1,101,102,92,-1,92,102,93,-1,36,103,31,-1,51,103,36,46,-1,103,100,31,-1,100,103,98,-1,104,90,93,-1,90,104,95,-1,95,105,41,-1,104,105,95,-1,106,101,98,-1,102,101,106,-1,107,93,102,-1,93,107,104,-1,108,104,107,-1,107,109,108,-1,110,105,104,-1,104,108,110,-1,109,107,111,-1,107,102,111,-1,111,102,106,-1,111,112,109,-1,106,112,111,-1,113,110,108,-1,110,113,114,-1,51,52,115,-1,116,115,117,-1,117,106,116,-1,118,109,112,-1,119,108,109,-1,108,119,113,-1,109,118,119,-1,120,113,119,-1,119,121,120,-1,52,56,122,-1,122,115,52,-1,115,122,123,-1,117,124,125,-1,106,117,125,-1,118,112,106,125,-1,119,118,125,-1,121,119,125,-1,126,124,123,-1,127,114,113,-1,114,127,128,-1,113,120,127,-1,114,128,129,-1,130,126,123,-1,122,130,123,-1,131,120,121,-1,131,127,120,-1,132,129,128,-1,128,127,132,-1,74,81,133,-1,81,134,133,-1,121,135,131,-1,136,132,127,-1,132,136,137,-1,138,71,129,-1,138,129,132,-1,137,138,132,-1,139,72,71,-1,72,139,80,-1,71,138,139,-1,140,135,121,-1,140,121,125,-1,141,127,131,-1,127,141,136,-1,131,135,141,-1,142,141,135,-1,143,136,141,-1,136,143,137,-1,141,142,143,-1,144,138,137,-1,144,139,138,-1,143,144,137,-1,145,146,134,-1,145,140,146,-1,134,81,145,-1,147,135,140,-1,135,147,142,-1,140,145,147,-1,148,80,139,-1,80,148,86,-1,139,144,148,-1,149,143,142,-1,149,144,143,-1,142,150,149,-1,151,148,144,-1,144,149,151,-1,152,145,81,-1,81,88,152,-1,153,147,145,-1,153,142,147,-1,145,152,153,-1,153,150,142,-1,154,86,148,-1,148,151,154,-1,155,28,25,-1,155,29,28,-1,155,25,32,-1,155,32,31,-1,155,31,100,-1,155,100,99,-1,155,99,91,-1,155,91,94,-1,155,94,96,-1,155,96,29,-1,156,151,149,-1,156,154,151,-1,156,149,150,-1,156,150,153,-1,156,153,152,-1,156,152,88,-1,156,88,87,-1,156,87,89,-1,156,89,85,-1,156,85,84,-1,156,84,86,-1,156,86,154,-1,76,157,60,-1,76,73,158,157,-1,159,158,73,75,160,-1,161,56,55,-1,60,162,58,-1,162,60,157,-1,161,55,163,-1,57,164,163,55,-1,160,163,164,-1,160,164,159,-1,164,57,165,-1,164,165,159,-1,57,58,166,165,-1,166,58,162,-1,165,166,159,-1,166,162,157,158,159,-1,140,125,167,-1,124,168,125,-1,168,167,125,-1,124,169,168,-1,146,140,167,170,-1,168,170,167,-1,168,169,170,-1,146,170,171,-1,169,171,170,-1,172,134,146,171,-1,134,172,130,-1,169,124,126,173,-1,173,126,130,-1,169,173,172,171,-1,173,130,172,-1,122,74,133,174,-1,133,134,174,-1,130,122,174,-1,134,130,174,-1,122,56,175,74,-1,74,175,176,-1,175,56,161,176,-1,74,176,75,-1,176,161,163,-1,176,160,75,-1,176,163,160,-1,115,116,177,51,-1,106,98,177,116,-1,51,177,103,-1,177,98,103,-1]
IndexedFaceSet245.creaseAngle = 1.59
Coordinate246 = x3d.Coordinate()

IndexedFaceSet245.coord = Coordinate246
TextureCoordinate247 = x3d.TextureCoordinate()

IndexedFaceSet245.texCoord = TextureCoordinate247

Shape241.geometry = IndexedFaceSet245

fieldValue240.children.append(Shape241)

ProtoInstance238.fieldValue.append(fieldValue240)

fieldValue237.children.append(ProtoInstance238)
ProtoInstance248 = x3d.ProtoInstance()
ProtoInstance248.name = "Joint"
ProtoInstance248.DEF = "hanim_l_shoulder"
fieldValue249 = x3d.fieldValue()
fieldValue249.name = "name"
fieldValue249.value = "l_shoulder"

ProtoInstance248.fieldValue.append(fieldValue249)
fieldValue250 = x3d.fieldValue()
fieldValue250.name = "center"
fieldValue250.value = "0.167 1.36 -0.0518"

ProtoInstance248.fieldValue.append(fieldValue250)
fieldValue251 = x3d.fieldValue()
fieldValue251.name = "children"
ProtoInstance252 = x3d.ProtoInstance()
ProtoInstance252.name = "Segment"
ProtoInstance252.DEF = "hanim_l_upperarm"
fieldValue253 = x3d.fieldValue()
fieldValue253.name = "name"
fieldValue253.value = "l_upperarm"

ProtoInstance252.fieldValue.append(fieldValue253)
fieldValue254 = x3d.fieldValue()
fieldValue254.name = "children"
Transform255 = x3d.Transform()
Transform255.DEF = "l_upperarm_adjust"
Transform255.center = [0.182,1.22,-0.047]
Transform255.rotation = [1,0,0,0.119]
Transform255.translation = [0,0.0004203,-0.01665]
Shape256 = x3d.Shape()
Appearance257 = x3d.Appearance()
Material258 = x3d.Material()
Material258.DEF = "Skin_Color"
Material258.ambientIntensity = 0.25
Material258.diffuseColor = [0.749,0.601,0.462]

Appearance257.material = Material258

Shape256.appearance = Appearance257
IndexedFaceSet259 = x3d.IndexedFaceSet()
IndexedFaceSet259.coordIndex = [2,1,0,-1,2,3,1,-1,2,4,3,-1,2,0,5,-1,6,5,0,-1,7,2,5,-1,8,4,2,-1,8,3,4,-1,9,1,3,-1,10,0,1,-1,0,10,6,-1,1,9,10,-1,3,8,9,-1,2,7,8,-1,5,6,7,-1,11,7,6,-1,14,9,8,-1,15,10,9,-1,11,6,10,-1,10,15,11,-1,9,14,15,-1,8,13,14,-1,8,16,13,-1,7,11,12,-1,21,15,14,-1,15,17,11,-1,15,21,17,-1,16,19,13,-1,13,19,20,-1,21,14,20,-1,14,13,20,-1,12,17,18,-1,12,11,17,-1,12,18,16,-1,18,19,16,-1,12,16,7,-1,16,8,7,-1,19,18,17,-1,20,19,21,-1,19,17,21,-1]
IndexedFaceSet259.creaseAngle = 1.65
Coordinate260 = x3d.Coordinate()

IndexedFaceSet259.coord = Coordinate260

Shape256.geometry = IndexedFaceSet259

Transform255.children.append(Shape256)

fieldValue254.children.append(Transform255)

ProtoInstance252.fieldValue.append(fieldValue254)

fieldValue251.children.append(ProtoInstance252)
ProtoInstance261 = x3d.ProtoInstance()
ProtoInstance261.name = "Joint"
ProtoInstance261.DEF = "hanim_l_elbow"
fieldValue262 = x3d.fieldValue()
fieldValue262.name = "name"
fieldValue262.value = "l_elbow"

ProtoInstance261.fieldValue.append(fieldValue262)
fieldValue263 = x3d.fieldValue()
fieldValue263.name = "center"
fieldValue263.value = "0.196 1.07 -0.0518"

ProtoInstance261.fieldValue.append(fieldValue263)
fieldValue264 = x3d.fieldValue()
fieldValue264.name = "children"
ProtoInstance265 = x3d.ProtoInstance()
ProtoInstance265.name = "Segment"
ProtoInstance265.DEF = "hanim_l_forearm"
fieldValue266 = x3d.fieldValue()
fieldValue266.name = "name"
fieldValue266.value = "l_forearm"

ProtoInstance265.fieldValue.append(fieldValue266)
fieldValue267 = x3d.fieldValue()
fieldValue267.name = "children"
Transform268 = x3d.Transform()
Transform268.DEF = "l_forearm_adjust"
Transform268.center = [0.198,0.961,-0.0405]
Transform268.rotation = [-1,0,0,0.1]
Transform268.translation = [0,0.003724,-0.0236]
Shape269 = x3d.Shape()
Appearance270 = x3d.Appearance()
Material271 = x3d.Material()
Material271.USE = "Skin_Color"

Appearance270.material = Material271

Shape269.appearance = Appearance270
IndexedFaceSet272 = x3d.IndexedFaceSet()
IndexedFaceSet272.coordIndex = [2,1,0,-1,2,3,1,-1,2,4,3,-1,2,5,4,-1,2,6,5,-1,2,0,6,-1,7,6,0,-1,8,5,6,-1,9,4,5,-1,9,3,4,-1,10,1,3,-1,11,0,1,-1,0,11,7,-1,1,10,11,-1,3,9,10,-1,5,12,9,-1,5,8,12,-1,6,7,8,-1,17,16,15,-1,14,17,15,-1,14,18,17,-1,13,18,14,-1,16,17,10,-1,16,10,9,-1,15,16,9,-1,15,9,12,-1,18,13,7,-1,18,7,11,-1,13,14,8,-1,13,8,7,-1,14,15,8,-1,15,12,8,-1,17,18,10,-1,18,11,10,-1]
IndexedFaceSet272.creaseAngle = 1.75
Coordinate273 = x3d.Coordinate()

IndexedFaceSet272.coord = Coordinate273

Shape269.geometry = IndexedFaceSet272

Transform268.children.append(Shape269)

fieldValue267.children.append(Transform268)

ProtoInstance265.fieldValue.append(fieldValue267)

fieldValue264.children.append(ProtoInstance265)
ProtoInstance274 = x3d.ProtoInstance()
ProtoInstance274.name = "Joint"
ProtoInstance274.DEF = "hanim_l_wrist"
fieldValue275 = x3d.fieldValue()
fieldValue275.name = "name"
fieldValue275.value = "l_wrist"

ProtoInstance274.fieldValue.append(fieldValue275)
fieldValue276 = x3d.fieldValue()
fieldValue276.name = "center"
fieldValue276.value = "0.213 0.811 -0.0338"

ProtoInstance274.fieldValue.append(fieldValue276)
fieldValue277 = x3d.fieldValue()
fieldValue277.name = "children"
ProtoInstance278 = x3d.ProtoInstance()
ProtoInstance278.name = "Segment"
ProtoInstance278.DEF = "hanim_l_hand"
fieldValue279 = x3d.fieldValue()
fieldValue279.name = "name"
fieldValue279.value = "l_hand"

ProtoInstance278.fieldValue.append(fieldValue279)
fieldValue280 = x3d.fieldValue()
fieldValue280.name = "children"
Transform281 = x3d.Transform()
Transform281.DEF = "l_hand_adjust"
Transform281.center = [0.213,0.811,-0.0338]
Transform281.rotation = [-0.06361,-0.9967,0.04988,1.333]
Transform281.translation = [0,0.005142,-0.008662]
Shape282 = x3d.Shape()
Appearance283 = x3d.Appearance()
Material284 = x3d.Material()
Material284.USE = "Skin_Color"

Appearance283.material = Material284

Shape282.appearance = Appearance283
IndexedFaceSet285 = x3d.IndexedFaceSet()
IndexedFaceSet285.coordIndex = [2,1,0,-1,5,4,3,-1,3,7,6,-1,2,3,6,-1,7,9,8,-1,6,7,8,-1,9,11,10,-1,8,9,10,-1,11,13,12,-1,10,11,12,-1,13,15,14,-1,12,13,14,-1,15,17,16,-1,14,15,16,-1,17,19,18,-1,16,17,18,-1,19,21,20,-1,18,19,20,-1,31,4,1,-1,4,5,0,-1,1,4,0,-1,5,3,2,-1,0,5,2,-1,26,25,24,-1,26,24,23,-1,27,26,23,-1,28,27,23,-1,28,23,22,-1,29,28,22,-1,29,22,21,-1,30,29,21,-1,15,13,11,-1,17,15,11,-1,19,17,11,-1,19,11,9,-1,31,19,9,-1,31,9,7,-1,4,31,7,-1,4,7,3,-1,30,21,19,-1,31,30,19,-1,12,14,16,-1,10,12,16,-1,10,16,18,-1,8,10,18,-1,6,8,1,-1,2,6,1,-1,39,38,37,-1,37,38,40,-1,37,40,36,-1,36,40,41,-1,36,41,35,-1,35,41,42,-1,35,42,34,-1,34,42,43,-1,34,43,33,-1,33,43,44,-1,33,44,32,-1,20,32,44,-1,20,44,45,-1,20,45,46,-1,47,8,18,-1,47,18,20,-1,47,20,46,-1,8,47,1,-1,22,33,32,-1,23,35,34,-1,23,36,35,-1,37,24,25,-1,40,38,27,-1,29,43,42,-1,45,44,30,-1,47,31,1,-1,47,46,31,-1,29,30,43,-1,30,44,43,-1,45,31,46,-1,45,30,31,-1,28,29,41,-1,29,42,41,-1,28,40,27,-1,28,41,40,-1,26,27,39,-1,27,38,39,-1,25,39,37,-1,25,26,39,-1,24,36,23,-1,24,37,36,-1,23,34,22,-1,34,33,22,-1,22,32,21,-1,32,20,21,-1]
IndexedFaceSet285.creaseAngle = 1.48
Coordinate286 = x3d.Coordinate()

IndexedFaceSet285.coord = Coordinate286

Shape282.geometry = IndexedFaceSet285

Transform281.children.append(Shape282)

fieldValue280.children.append(Transform281)

ProtoInstance278.fieldValue.append(fieldValue280)

fieldValue277.children.append(ProtoInstance278)

ProtoInstance274.fieldValue.append(fieldValue277)

fieldValue264.children.append(ProtoInstance274)

ProtoInstance261.fieldValue.append(fieldValue264)

fieldValue251.children.append(ProtoInstance261)

ProtoInstance248.fieldValue.append(fieldValue251)

fieldValue237.children.append(ProtoInstance248)
ProtoInstance287 = x3d.ProtoInstance()
ProtoInstance287.name = "Joint"
ProtoInstance287.DEF = "hanim_r_shoulder"
fieldValue288 = x3d.fieldValue()
fieldValue288.name = "name"
fieldValue288.value = "r_shoulder"

ProtoInstance287.fieldValue.append(fieldValue288)
fieldValue289 = x3d.fieldValue()
fieldValue289.name = "center"
fieldValue289.value = "-0.167 1.36 -0.0458"

ProtoInstance287.fieldValue.append(fieldValue289)
fieldValue290 = x3d.fieldValue()
fieldValue290.name = "children"
ProtoInstance291 = x3d.ProtoInstance()
ProtoInstance291.name = "Segment"
ProtoInstance291.DEF = "hanim_r_upperarm"
fieldValue292 = x3d.fieldValue()
fieldValue292.name = "name"
fieldValue292.value = "r_upperarm"

ProtoInstance291.fieldValue.append(fieldValue292)
fieldValue293 = x3d.fieldValue()
fieldValue293.name = "children"
Transform294 = x3d.Transform()
Transform294.DEF = "r_upperarm_adjust"
Transform294.center = [-0.182,1.22,-0.047]
Transform294.rotation = [1,0,0,0.0836]
Transform294.translation = [0,0.000589,-0.01169]
Shape295 = x3d.Shape()
Appearance296 = x3d.Appearance()
Material297 = x3d.Material()
Material297.USE = "Skin_Color"

Appearance296.material = Material297

Shape295.appearance = Appearance296
IndexedFaceSet298 = x3d.IndexedFaceSet()
IndexedFaceSet298.coordIndex = [14,10,20,-1,10,13,20,-1,13,22,20,-1,19,14,20,-1,14,19,12,-1,19,20,24,-1,20,22,25,-1,22,13,25,-1,13,10,11,-1,10,14,5,-1,12,5,14,-1,5,11,10,-1,11,25,13,-1,25,24,20,-1,24,12,19,-1,12,24,9,-1,25,11,8,-1,11,5,2,-1,5,12,9,-1,9,2,5,-1,2,8,11,-1,8,23,25,-1,23,27,25,-1,21,9,24,-1,9,21,7,-1,27,23,18,-1,23,8,18,-1,8,2,6,-1,2,9,7,-1,7,1,2,-1,1,6,2,-1,6,18,8,-1,18,26,27,-1,16,7,21,-1,7,16,4,-1,16,26,17,-1,26,18,15,-1,18,6,3,-1,6,1,0,-1,1,7,0,-1,4,0,7,-1,0,3,6,-1,3,15,18,-1,15,17,26,-1,17,4,16,-1,3,0,15,-1,15,0,4,-1,15,4,17,-1,25,27,24,-1,27,21,24,-1,27,26,21,-1,26,16,21,-1]
IndexedFaceSet298.creaseAngle = 1.53
Coordinate299 = x3d.Coordinate()

IndexedFaceSet298.coord = Coordinate299

Shape295.geometry = IndexedFaceSet298

Transform294.children.append(Shape295)

fieldValue293.children.append(Transform294)

ProtoInstance291.fieldValue.append(fieldValue293)

fieldValue290.children.append(ProtoInstance291)
ProtoInstance300 = x3d.ProtoInstance()
ProtoInstance300.name = "Joint"
ProtoInstance300.DEF = "hanim_r_elbow"
fieldValue301 = x3d.fieldValue()
fieldValue301.name = "name"
fieldValue301.value = "r_elbow"

ProtoInstance300.fieldValue.append(fieldValue301)
fieldValue302 = x3d.fieldValue()
fieldValue302.name = "center"
fieldValue302.value = "-0.192 1.07 -0.0498"

ProtoInstance300.fieldValue.append(fieldValue302)
fieldValue303 = x3d.fieldValue()
fieldValue303.name = "children"
ProtoInstance304 = x3d.ProtoInstance()
ProtoInstance304.name = "Segment"
ProtoInstance304.DEF = "hanim_r_forearm"
fieldValue305 = x3d.fieldValue()
fieldValue305.name = "name"
fieldValue305.value = "r_forearm"

ProtoInstance304.fieldValue.append(fieldValue305)
fieldValue306 = x3d.fieldValue()
fieldValue306.name = "children"
Transform307 = x3d.Transform()
Transform307.DEF = "r_forearm_adjust"
Transform307.center = [-0.198,0.961,-0.0397]
Transform307.rotation = [-1,0,0,0.1254]
Transform307.translation = [0,0.003466,-0.01065]
Shape308 = x3d.Shape()
Appearance309 = x3d.Appearance()
Material310 = x3d.Material()
Material310.USE = "Skin_Color"

Appearance309.material = Material310

Shape308.appearance = Appearance309
IndexedFaceSet311 = x3d.IndexedFaceSet()
IndexedFaceSet311.coordIndex = [20,13,15,-1,13,8,15,-1,8,12,15,-1,12,18,15,-1,18,22,15,-1,22,20,15,-1,20,22,21,-1,22,18,24,-1,18,12,7,-1,12,8,7,-1,8,13,3,-1,13,20,10,-1,21,10,20,-1,10,3,13,-1,3,7,8,-1,7,19,18,-1,19,24,18,-1,24,21,22,-1,21,24,23,-1,24,19,16,-1,19,7,6,-1,7,3,1,-1,3,10,5,-1,10,21,17,-1,17,5,10,-1,5,1,3,-1,1,6,7,-1,6,16,19,-1,16,23,24,-1,23,17,21,-1,1,5,2,-1,5,17,9,-1,9,2,5,-1,1,4,6,-1,4,16,6,-1,23,9,17,-1,9,23,14,-1,23,16,11,-1,4,11,16,-1,11,14,23,-1,11,4,0,-1,11,0,14,-1,0,2,14,-1,14,2,9,-1,2,0,1,-1,0,4,1,-1]
IndexedFaceSet311.creaseAngle = 1.73
Coordinate312 = x3d.Coordinate()

IndexedFaceSet311.coord = Coordinate312

Shape308.geometry = IndexedFaceSet311

Transform307.children.append(Shape308)

fieldValue306.children.append(Transform307)

ProtoInstance304.fieldValue.append(fieldValue306)

fieldValue303.children.append(ProtoInstance304)
ProtoInstance313 = x3d.ProtoInstance()
ProtoInstance313.name = "Joint"
ProtoInstance313.DEF = "hanim_r_wrist"
fieldValue314 = x3d.fieldValue()
fieldValue314.name = "name"
fieldValue314.value = "r_wrist"

ProtoInstance313.fieldValue.append(fieldValue314)
fieldValue315 = x3d.fieldValue()
fieldValue315.name = "center"
fieldValue315.value = "-0.217 0.811 -0.0338"

ProtoInstance313.fieldValue.append(fieldValue315)
fieldValue316 = x3d.fieldValue()
fieldValue316.name = "children"
ProtoInstance317 = x3d.ProtoInstance()
ProtoInstance317.name = "Segment"
ProtoInstance317.DEF = "hanim_r_hand"
fieldValue318 = x3d.fieldValue()
fieldValue318.name = "name"
fieldValue318.value = "r_hand"

ProtoInstance317.fieldValue.append(fieldValue318)
fieldValue319 = x3d.fieldValue()
fieldValue319.name = "children"
Transform320 = x3d.Transform()
Transform320.DEF = "r_hand_adjust"
Transform320.center = [-0.217,0.811,-0.0338]
Transform320.rotation = [-0.09024,0.994,-0.0624,1.216]
Shape321 = x3d.Shape()
Appearance322 = x3d.Appearance()
Material323 = x3d.Material()
Material323.USE = "Skin_Color"

Appearance322.material = Material323

Shape321.appearance = Appearance322
IndexedFaceSet324 = x3d.IndexedFaceSet()
IndexedFaceSet324.coordIndex = [10,9,0,-1,11,30,31,-1,1,12,11,-1,1,11,0,-1,2,13,12,-1,2,12,1,-1,3,14,13,-1,3,13,2,-1,4,15,14,-1,4,14,3,-1,5,16,15,-1,5,15,4,-1,6,17,16,-1,6,16,5,-1,7,18,17,-1,7,17,6,-1,8,19,18,-1,8,18,7,-1,10,31,30,-1,10,30,9,-1,0,11,31,-1,0,31,10,-1,22,23,24,-1,21,22,24,-1,21,24,25,-1,21,25,26,-1,20,21,26,-1,20,26,27,-1,19,20,27,-1,19,27,28,-1,14,15,16,-1,14,16,17,-1,14,17,18,-1,13,14,18,-1,13,18,29,-1,12,13,29,-1,12,29,30,-1,11,12,30,-1,18,19,28,-1,18,28,29,-1,6,5,4,-1,6,4,3,-1,7,6,3,-1,7,3,2,-1,9,2,1,-1,9,1,0,-1,32,38,33,-1,33,38,39,-1,33,39,34,-1,34,39,40,-1,34,40,35,-1,35,40,41,-1,35,41,36,-1,36,41,42,-1,36,42,37,-1,37,42,43,-1,37,43,44,-1,44,43,8,-1,44,8,45,-1,45,8,46,-1,46,8,7,-1,46,7,2,-1,46,2,47,-1,9,47,2,-1,25,34,35,-1,25,33,34,-1,25,24,33,-1,24,32,33,-1,32,24,23,-1,40,39,21,-1,41,40,21,-1,43,19,8,-1,43,20,19,-1,43,42,20,-1,21,20,41,-1,20,42,41,-1,38,22,39,-1,22,21,39,-1,32,23,38,-1,23,22,38,-1,26,25,35,-1,27,36,37,-1,27,37,28,-1,37,44,28,-1,26,35,27,-1,35,36,27,-1,28,44,45,-1,29,46,47,-1,29,9,30,-1,29,47,9,-1,28,45,29,-1,45,46,29,-1]
IndexedFaceSet324.creaseAngle = 1.57
Coordinate325 = x3d.Coordinate()

IndexedFaceSet324.coord = Coordinate325

Shape321.geometry = IndexedFaceSet324

Transform320.children.append(Shape321)

fieldValue319.children.append(Transform320)

ProtoInstance317.fieldValue.append(fieldValue319)

fieldValue316.children.append(ProtoInstance317)

ProtoInstance313.fieldValue.append(fieldValue316)

fieldValue303.children.append(ProtoInstance313)

ProtoInstance300.fieldValue.append(fieldValue303)

fieldValue290.children.append(ProtoInstance300)

ProtoInstance287.fieldValue.append(fieldValue290)

fieldValue237.children.append(ProtoInstance287)
ProtoInstance326 = x3d.ProtoInstance()
ProtoInstance326.name = "Joint"
ProtoInstance326.DEF = "hanim_vc4"
fieldValue327 = x3d.fieldValue()
fieldValue327.name = "name"
fieldValue327.value = "vc4"

ProtoInstance326.fieldValue.append(fieldValue327)
fieldValue328 = x3d.fieldValue()
fieldValue328.name = "center"
fieldValue328.value = "0 1.43 -0.0458"

ProtoInstance326.fieldValue.append(fieldValue328)
fieldValue329 = x3d.fieldValue()
fieldValue329.name = "children"
ProtoInstance330 = x3d.ProtoInstance()
ProtoInstance330.name = "Segment"
ProtoInstance330.DEF = "hanim_c4"
fieldValue331 = x3d.fieldValue()
fieldValue331.name = "name"
fieldValue331.value = "c4"

ProtoInstance330.fieldValue.append(fieldValue331)
fieldValue332 = x3d.fieldValue()
fieldValue332.name = "children"
Shape333 = x3d.Shape()
Appearance334 = x3d.Appearance()
Material335 = x3d.Material()
Material335.USE = "Skin_Color"

Appearance334.material = Material335

Shape333.appearance = Appearance334
IndexedFaceSet336 = x3d.IndexedFaceSet()
IndexedFaceSet336.DEF = "neck"
IndexedFaceSet336.coordIndex = [6,5,2,-1,6,2,3,-1,5,4,1,-1,5,1,2,-1,4,7,0,-1,4,0,1,-1,11,10,9,-1,11,9,8,-1,10,13,12,-1,10,12,9,-1,13,15,14,-1,13,14,12,-1,6,3,11,-1,6,11,8,-1,7,14,15,-1,7,15,0,-1,2,10,11,-1,2,11,3,-1,2,1,13,-1,2,13,10,-1,1,0,15,-1,1,15,13,-1,9,5,6,-1,9,6,8,-1,9,12,4,-1,9,4,5,-1,12,14,7,-1,12,7,4,-1]
IndexedFaceSet336.creaseAngle = 1.91
Coordinate337 = x3d.Coordinate()

IndexedFaceSet336.coord = Coordinate337

Shape333.geometry = IndexedFaceSet336

fieldValue332.children.append(Shape333)

ProtoInstance330.fieldValue.append(fieldValue332)

fieldValue329.children.append(ProtoInstance330)
ProtoInstance338 = x3d.ProtoInstance()
ProtoInstance338.name = "Joint"
ProtoInstance338.DEF = "hanim_skullbase"
fieldValue339 = x3d.fieldValue()
fieldValue339.name = "name"
fieldValue339.value = "skullbase"

ProtoInstance338.fieldValue.append(fieldValue339)
fieldValue340 = x3d.fieldValue()
fieldValue340.name = "center"
fieldValue340.value = "0 1.54 -0.0409"

ProtoInstance338.fieldValue.append(fieldValue340)
fieldValue341 = x3d.fieldValue()
fieldValue341.name = "children"
ProtoInstance342 = x3d.ProtoInstance()
ProtoInstance342.name = "Segment"
ProtoInstance342.DEF = "hanim_skull"
fieldValue343 = x3d.fieldValue()
fieldValue343.name = "name"
fieldValue343.value = "skull"

ProtoInstance342.fieldValue.append(fieldValue343)
fieldValue344 = x3d.fieldValue()
fieldValue344.name = "children"
Shape345 = x3d.Shape()
Appearance346 = x3d.Appearance()
Material347 = x3d.Material()
Material347.USE = "Skin_Color"

Appearance346.material = Material347

Shape345.appearance = Appearance346
IndexedFaceSet348 = x3d.IndexedFaceSet()
IndexedFaceSet348.DEF = "headIFS"
IndexedFaceSet348.colorIndex = [1,1,1,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,1,1,1,-1,1,1,1,-1,0,0,0,-1,1,1,1,-1,1,1,1,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,2,2,2,-1,2,2,2,-1,2,2,2,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,2,2,2,-1,2,2,2,-1,2,2,2,-1,0,0,0,-1,0,0,0,-1,2,2,2,-1,2,2,2,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,1,1,1,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,2,2,2,-1,2,2,2,-1,2,2,2,-1,2,2,2,-1,2,2,2,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,2,2,2,-1,2,2,2,-1,2,2,2,-1,0,0,0,-1,0,0,0,-1,2,2,2,-1,2,2,2,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,3,3,3,-1,3,3,3,-1,0,0,0,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,3,3,3,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,3,3,3,-1,3,3,3,-1,0,0,0,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,3,3,3,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1]
IndexedFaceSet348.coordIndex = [48,87,58,-1,91,92,59,-1,59,92,88,-1,88,93,231,-1,232,86,233,-1,86,89,233,-1,89,57,56,-1,49,55,57,-1,102,86,96,-1,86,90,96,-1,97,95,96,-1,97,127,95,-1,41,96,154,-1,41,102,96,-1,99,102,41,-1,153,99,41,-1,102,40,86,-1,234,235,236,-1,87,237,58,-1,56,57,91,-1,87,234,237,-1,234,236,237,-1,89,49,57,-1,49,50,55,-1,40,89,86,-1,89,56,233,-1,232,90,86,-1,90,97,96,-1,92,93,88,-1,93,94,231,-1,232,231,94,-1,97,90,232,-1,96,42,154,-1,95,42,96,-1,53,46,45,-1,53,45,51,-1,53,51,92,-1,92,51,52,-1,92,52,93,-1,94,93,52,-1,94,52,4,-1,97,232,94,-1,54,47,46,-1,54,46,53,-1,55,47,54,-1,50,47,55,-1,34,33,50,-1,34,50,49,-1,35,34,49,-1,35,49,89,-1,35,89,40,-1,99,39,102,-1,39,35,40,-1,31,34,35,-1,31,35,32,-1,14,32,35,-1,14,35,39,-1,14,39,98,-1,137,38,153,-1,38,99,153,-1,38,98,99,-1,37,238,239,-1,11,238,37,-1,101,37,36,-1,241,141,242,-1,10,12,242,-1,12,13,14,-1,12,14,243,-1,13,15,32,-1,13,32,14,-1,15,16,31,-1,15,31,32,-1,2,70,10,-1,2,10,141,-1,70,69,12,-1,70,12,10,-1,69,68,13,-1,69,13,12,-1,68,67,15,-1,68,15,13,-1,67,66,16,-1,67,16,15,-1,98,39,99,-1,101,11,37,-1,100,101,36,-1,36,244,240,-1,141,10,242,-1,12,243,242,-1,36,37,239,-1,36,239,244,-1,57,55,91,-1,55,54,91,-1,39,40,102,-1,123,103,120,-1,114,122,104,-1,115,122,114,-1,208,105,115,-1,210,119,211,-1,210,106,119,-1,116,107,106,-1,107,108,117,-1,126,119,109,-1,126,110,119,-1,126,95,125,-1,95,127,125,-1,154,126,111,-1,126,109,111,-1,111,109,112,-1,111,112,153,-1,119,113,109,-1,207,213,214,-1,123,209,103,-1,213,212,214,-1,209,214,103,-1,209,207,214,-1,107,117,106,-1,108,118,117,-1,119,106,113,-1,210,116,106,-1,119,110,211,-1,126,125,110,-1,115,105,122,-1,208,124,105,-1,124,208,211,-1,211,110,125,-1,154,42,126,-1,126,42,95,-1,168,128,121,-1,170,168,121,-1,122,170,121,-1,172,170,122,-1,105,172,122,-1,172,105,124,-1,4,172,124,-1,124,211,125,-1,128,130,129,-1,121,128,129,-1,129,130,108,-1,108,130,118,-1,118,131,132,-1,117,118,132,-1,117,132,133,-1,106,117,133,-1,113,106,133,-1,109,152,112,-1,113,133,152,-1,133,132,134,-1,135,133,134,-1,133,135,136,-1,152,133,136,-1,148,152,136,-1,153,138,137,-1,153,112,138,-1,112,148,138,-1,219,217,139,-1,36,240,149,-1,139,217,140,-1,149,139,151,-1,36,149,100,-1,220,141,241,-1,220,150,142,-1,136,143,150,-1,221,136,150,-1,135,144,143,-1,136,135,143,-1,134,158,144,-1,135,134,144,-1,142,161,2,-1,141,142,2,-1,150,145,161,-1,142,150,161,-1,143,146,145,-1,150,143,145,-1,144,147,146,-1,143,144,146,-1,158,160,147,-1,144,158,147,-1,112,152,148,-1,139,140,151,-1,149,151,100,-1,240,218,149,-1,220,142,141,-1,220,221,150,-1,219,139,149,-1,218,219,149,-1,104,108,107,-1,104,129,108,-1,109,113,152,-1,153,41,111,-1,129,104,122,-1,129,122,121,-1,91,54,92,-1,54,53,92,-1,97,94,127,-1,127,94,4,-1,125,127,124,-1,127,4,124,-1,154,111,41,-1,31,30,33,-1,31,33,34,-1,16,17,30,-1,16,30,31,-1,66,65,17,-1,66,17,16,-1,2,73,156,-1,2,156,70,-1,156,72,66,-1,156,66,67,-1,156,67,68,-1,156,68,69,-1,156,69,70,-1,72,71,65,-1,72,65,66,-1,17,18,30,-1,45,44,51,-1,51,44,43,-1,51,43,52,-1,52,43,1,-1,52,1,4,-1,245,246,27,-1,245,27,3,-1,246,247,28,-1,246,28,27,-1,248,22,29,-1,248,29,28,-1,248,28,247,-1,27,26,0,-1,27,0,3,-1,27,28,25,-1,27,25,26,-1,29,24,25,-1,29,25,28,-1,22,23,24,-1,22,24,29,-1,249,250,22,-1,249,22,248,-1,250,60,23,-1,250,23,22,-1,17,254,18,-1,65,254,17,-1,71,64,65,-1,63,74,75,-1,63,75,61,-1,64,255,254,-1,75,62,61,-1,62,76,60,-1,76,77,23,-1,76,23,60,-1,77,24,23,-1,77,78,25,-1,77,25,24,-1,78,84,26,-1,78,26,25,-1,84,192,0,-1,84,0,26,-1,84,83,193,-1,84,193,192,-1,79,83,84,-1,79,84,78,-1,76,79,78,-1,76,78,77,-1,80,83,79,-1,80,204,83,-1,75,81,80,-1,81,85,204,-1,81,204,80,-1,74,81,75,-1,74,82,81,-1,82,5,85,-1,82,85,81,-1,155,8,71,-1,155,71,72,-1,8,6,64,-1,8,64,71,-1,6,7,255,-1,6,255,64,-1,7,9,256,-1,7,256,255,-1,9,257,256,-1,73,155,156,-1,155,72,156,-1,204,193,83,-1,64,254,65,-1,131,157,134,-1,132,131,134,-1,157,159,158,-1,134,157,158,-1,159,206,160,-1,158,159,160,-1,203,73,2,-1,161,203,2,-1,160,162,203,-1,147,160,203,-1,146,147,203,-1,145,146,203,-1,161,145,203,-1,206,163,162,-1,160,206,162,-1,157,164,159,-1,170,169,168,-1,171,169,170,-1,172,171,170,-1,1,171,172,-1,4,1,172,-1,173,227,245,-1,3,173,245,-1,174,226,227,-1,173,174,227,-1,176,175,215,-1,174,176,215,-1,226,174,215,-1,0,177,173,-1,3,0,173,-1,178,174,173,-1,177,178,173,-1,178,179,176,-1,174,178,176,-1,179,180,175,-1,176,179,175,-1,175,225,216,-1,215,175,216,-1,180,181,225,-1,175,180,225,-1,164,228,159,-1,159,228,206,-1,206,185,163,-1,187,186,184,-1,183,187,184,-1,228,229,185,-1,183,182,187,-1,181,188,182,-1,180,189,188,-1,181,180,188,-1,180,179,189,-1,178,190,189,-1,179,178,189,-1,177,191,190,-1,178,177,190,-1,0,192,191,-1,177,0,191,-1,193,205,191,-1,192,193,191,-1,191,205,194,-1,190,191,194,-1,190,194,188,-1,189,190,188,-1,194,205,195,-1,205,204,195,-1,195,196,187,-1,204,85,196,-1,195,204,196,-1,187,196,186,-1,196,197,186,-1,85,5,197,-1,196,85,197,-1,163,198,202,-1,162,163,202,-1,185,199,198,-1,163,185,198,-1,229,200,199,-1,185,229,199,-1,230,201,200,-1,229,230,200,-1,230,257,201,-1,203,202,73,-1,203,162,202,-1,205,193,204,-1,206,228,185,-1,198,8,155,-1,198,155,202,-1,155,73,202,-1,199,6,8,-1,199,8,198,-1,7,6,199,-1,7,199,200,-1,201,9,7,-1,201,7,200,-1,201,257,9,-1,188,194,195,-1,188,195,182,-1,195,187,182,-1,80,79,76,-1,80,62,75,-1,80,76,62,-1,47,50,33,-1,131,118,130,-1,20,21,47,-1,21,46,47,-1,20,33,19,-1,20,47,33,-1,33,30,19,-1,30,18,19,-1,62,60,251,-1,60,250,251,-1,252,61,251,-1,61,62,251,-1,252,63,61,-1,252,253,63,-1,166,130,167,-1,130,128,167,-1,166,131,130,-1,166,165,131,-1,165,157,131,-1,165,164,157,-1,224,181,182,-1,224,225,181,-1,224,183,223,-1,224,182,183,-1,183,184,223,-1,184,222,223,-1]
IndexedFaceSet348.creaseAngle = 0.7854
Coordinate349 = x3d.Coordinate()
Coordinate349.DEF = "Face"

IndexedFaceSet348.coord = Coordinate349
Color350 = x3d.Color()

IndexedFaceSet348.color = Color350

Shape345.geometry = IndexedFaceSet348

fieldValue344.children.append(Shape345)

ProtoInstance342.fieldValue.append(fieldValue344)

fieldValue341.children.append(ProtoInstance342)

ProtoInstance338.fieldValue.append(fieldValue341)

fieldValue329.children.append(ProtoInstance338)

ProtoInstance326.fieldValue.append(fieldValue329)

fieldValue237.children.append(ProtoInstance326)

ProtoInstance234.fieldValue.append(fieldValue237)

fieldValue149.children.append(ProtoInstance234)

ProtoInstance146.fieldValue.append(fieldValue149)

fieldValue145.children.append(ProtoInstance146)
Group351 = x3d.Group()

fieldValue145.children.append(Group351)

ProtoInstance141.fieldValue.append(fieldValue145)
fieldValue352 = x3d.fieldValue()
fieldValue352.name = "joints"
ProtoInstance353 = x3d.ProtoInstance()
ProtoInstance353.USE = "hanim_humanoid_root"

fieldValue352.children.append(ProtoInstance353)
ProtoInstance354 = x3d.ProtoInstance()
ProtoInstance354.USE = "hanim_sacroiliac"

fieldValue352.children.append(ProtoInstance354)
ProtoInstance355 = x3d.ProtoInstance()
ProtoInstance355.USE = "hanim_l_hip"

fieldValue352.children.append(ProtoInstance355)
ProtoInstance356 = x3d.ProtoInstance()
ProtoInstance356.USE = "hanim_l_knee"

fieldValue352.children.append(ProtoInstance356)
ProtoInstance357 = x3d.ProtoInstance()
ProtoInstance357.USE = "hanim_l_ankle"

fieldValue352.children.append(ProtoInstance357)
ProtoInstance358 = x3d.ProtoInstance()
ProtoInstance358.USE = "hanim_r_hip"

fieldValue352.children.append(ProtoInstance358)
ProtoInstance359 = x3d.ProtoInstance()
ProtoInstance359.USE = "hanim_r_knee"

fieldValue352.children.append(ProtoInstance359)
ProtoInstance360 = x3d.ProtoInstance()
ProtoInstance360.USE = "hanim_r_ankle"

fieldValue352.children.append(ProtoInstance360)
ProtoInstance361 = x3d.ProtoInstance()
ProtoInstance361.USE = "hanim_vl1"

fieldValue352.children.append(ProtoInstance361)
ProtoInstance362 = x3d.ProtoInstance()
ProtoInstance362.USE = "hanim_l_shoulder"

fieldValue352.children.append(ProtoInstance362)
ProtoInstance363 = x3d.ProtoInstance()
ProtoInstance363.USE = "hanim_l_elbow"

fieldValue352.children.append(ProtoInstance363)
ProtoInstance364 = x3d.ProtoInstance()
ProtoInstance364.USE = "hanim_l_wrist"

fieldValue352.children.append(ProtoInstance364)
ProtoInstance365 = x3d.ProtoInstance()
ProtoInstance365.USE = "hanim_r_shoulder"

fieldValue352.children.append(ProtoInstance365)
ProtoInstance366 = x3d.ProtoInstance()
ProtoInstance366.USE = "hanim_r_elbow"

fieldValue352.children.append(ProtoInstance366)
ProtoInstance367 = x3d.ProtoInstance()
ProtoInstance367.USE = "hanim_r_wrist"

fieldValue352.children.append(ProtoInstance367)
ProtoInstance368 = x3d.ProtoInstance()
ProtoInstance368.USE = "hanim_vc4"

fieldValue352.children.append(ProtoInstance368)
ProtoInstance369 = x3d.ProtoInstance()
ProtoInstance369.USE = "hanim_skullbase"

fieldValue352.children.append(ProtoInstance369)

ProtoInstance141.fieldValue.append(fieldValue352)
fieldValue370 = x3d.fieldValue()
fieldValue370.name = "segments"
ProtoInstance371 = x3d.ProtoInstance()
ProtoInstance371.USE = "hanim_pelvis"

fieldValue370.children.append(ProtoInstance371)
ProtoInstance372 = x3d.ProtoInstance()
ProtoInstance372.USE = "hanim_l_thigh"

fieldValue370.children.append(ProtoInstance372)
ProtoInstance373 = x3d.ProtoInstance()
ProtoInstance373.USE = "hanim_l_calf"

fieldValue370.children.append(ProtoInstance373)
ProtoInstance374 = x3d.ProtoInstance()
ProtoInstance374.USE = "hanim_l_hindfoot"

fieldValue370.children.append(ProtoInstance374)
ProtoInstance375 = x3d.ProtoInstance()
ProtoInstance375.USE = "hanim_r_thigh"

fieldValue370.children.append(ProtoInstance375)
ProtoInstance376 = x3d.ProtoInstance()
ProtoInstance376.USE = "hanim_r_calf"

fieldValue370.children.append(ProtoInstance376)
ProtoInstance377 = x3d.ProtoInstance()
ProtoInstance377.USE = "hanim_r_hindfoot"

fieldValue370.children.append(ProtoInstance377)
ProtoInstance378 = x3d.ProtoInstance()
ProtoInstance378.USE = "hanim_c7"

fieldValue370.children.append(ProtoInstance378)
ProtoInstance379 = x3d.ProtoInstance()
ProtoInstance379.USE = "hanim_l_upperarm"

fieldValue370.children.append(ProtoInstance379)
ProtoInstance380 = x3d.ProtoInstance()
ProtoInstance380.USE = "hanim_l_forearm"

fieldValue370.children.append(ProtoInstance380)
ProtoInstance381 = x3d.ProtoInstance()
ProtoInstance381.USE = "hanim_l_hand"

fieldValue370.children.append(ProtoInstance381)
ProtoInstance382 = x3d.ProtoInstance()
ProtoInstance382.USE = "hanim_r_upperarm"

fieldValue370.children.append(ProtoInstance382)
ProtoInstance383 = x3d.ProtoInstance()
ProtoInstance383.USE = "hanim_r_forearm"

fieldValue370.children.append(ProtoInstance383)
ProtoInstance384 = x3d.ProtoInstance()
ProtoInstance384.USE = "hanim_r_hand"

fieldValue370.children.append(ProtoInstance384)
ProtoInstance385 = x3d.ProtoInstance()
ProtoInstance385.USE = "hanim_c4"

fieldValue370.children.append(ProtoInstance385)
ProtoInstance386 = x3d.ProtoInstance()
ProtoInstance386.USE = "hanim_skull"

fieldValue370.children.append(ProtoInstance386)

ProtoInstance141.fieldValue.append(fieldValue370)
fieldValue387 = x3d.fieldValue()
fieldValue387.name = "viewpoints"
Viewpoint388 = x3d.Viewpoint()
Viewpoint388.DEF = "InclinedView"
Viewpoint388.description = "Inclined View"
Viewpoint388.orientation = [-0.113,0.993,0.0347,0.671]
Viewpoint388.position = [1.62,1.05,2.06]

fieldValue387.children.append(Viewpoint388)
Viewpoint389 = x3d.Viewpoint()
Viewpoint389.DEF = "FrontView"
Viewpoint389.description = "Front View"
Viewpoint389.position = [0,0.854,2.57665]

fieldValue387.children.append(Viewpoint389)
Viewpoint390 = x3d.Viewpoint()
Viewpoint390.DEF = "SideView"
Viewpoint390.description = "Side View"
Viewpoint390.orientation = [0,1,0,1.57079]
Viewpoint390.position = [2.5929,0.854,0]

fieldValue387.children.append(Viewpoint390)
Viewpoint391 = x3d.Viewpoint()
Viewpoint391.DEF = "TopView"
Viewpoint391.description = "Top View"
Viewpoint391.orientation = [1,0,0,-1.57079]
Viewpoint391.position = [0,3.4495,0]

fieldValue387.children.append(Viewpoint391)

ProtoInstance141.fieldValue.append(fieldValue387)

Scene14.children.append(ProtoInstance141)
WorldInfo392 = x3d.WorldInfo()
WorldInfo392.info = ["Copyright (c) 1997. 3Name3D / Yglesias Wallock Divekar, Inc."]
WorldInfo392.title = "Nancy - an HAnim compliant avatar by 3Name3D"

Scene14.children.append(WorldInfo392)
NavigationInfo393 = x3d.NavigationInfo()
NavigationInfo393.avatarSize = [0.15,1.53,0.75]
NavigationInfo393.speed = 0.5
NavigationInfo393.type = ["EXAMINE"]

Scene14.children.append(NavigationInfo393)
Group394 = x3d.Group()
Group394.DEF = "Interface"
Transform395 = x3d.Transform()
ProximitySensor396 = x3d.ProximitySensor()
ProximitySensor396.DEF = "HudProx"
ProximitySensor396.center = [0,20,0]
ProximitySensor396.size = [500,100,500]

Transform395.children.append(ProximitySensor396)

Group394.children.append(Transform395)
Collision397 = x3d.Collision()
Collision397.DEF = "HUD"
Collision397.enabled = False
Transform398 = x3d.Transform()
Transform398.DEF = "HudXform"
Transform399 = x3d.Transform()
Transform399.scale = [0.012,0.012,0.012]
Transform399.translation = [0.01107,-0.025,-0.08]
Transform400 = x3d.Transform()
Transform400.DEF = "Stand_Text"
TouchSensor401 = x3d.TouchSensor()
TouchSensor401.DEF = "Stand_Touch"
TouchSensor401.description = "click for behavior"

Transform400.children.append(TouchSensor401)
Shape402 = x3d.Shape()
Shape402.DEF = "Stand"
IndexedFaceSet403 = x3d.IndexedFaceSet()
IndexedFaceSet403.coordIndex = [1,30,29,-1,1,29,2,-1,31,47,46,-1,31,46,32,-1,78,77,80,-1,78,80,79,-1,96,113,112,-1,96,112,95,-1,95,112,111,-1,95,111,94,-1,94,111,110,-1,94,110,93,-1,93,110,109,-1,93,109,108,-1,93,108,100,-1,107,99,100,-1,107,100,108,-1,107,106,99,-1,106,105,98,-1,106,98,99,-1,104,97,98,-1,104,98,105,-1,103,102,104,-1,104,102,101,-1,104,101,97,-1,101,96,97,-1,101,97,101,-1,101,101,96,-1,96,101,113,-1,113,101,114,-1,115,86,85,-1,115,85,116,-1,117,87,84,-1,117,84,118,-1,119,83,120,-1,121,88,82,-1,121,82,122,-1,123,89,81,-1,123,81,124,-1,125,90,126,-1,127,92,128,-1,129,91,130,-1,54,49,50,-1,54,50,55,-1,76,75,74,-1,76,74,54,-1,54,74,73,-1,54,73,49,-1,49,73,48,-1,48,73,62,-1,48,62,61,-1,48,61,60,-1,48,60,53,-1,53,60,59,-1,53,59,53,-1,53,59,58,-1,53,58,52,-1,52,58,57,-1,52,57,51,-1,56,51,57,-1,56,55,50,-1,56,50,51,-1,62,73,72,-1,62,72,63,-1,63,72,71,-1,63,71,64,-1,64,71,70,-1,64,70,69,-1,64,69,65,-1,65,69,68,-1,65,68,67,-1,65,67,66,-1,131,40,39,-1,131,39,132,-1,133,43,42,-1,133,42,134,-1,135,37,36,-1,135,36,136,-1,137,41,38,-1,137,38,138,-1,139,44,35,-1,139,35,140,-1,141,34,142,-1,143,45,33,-1,143,33,144,-1,145,16,15,-1,145,15,146,-1,147,14,148,-1,149,17,13,-1,149,13,150,-1,151,18,12,-1,151,12,152,-1,153,19,11,-1,153,11,154,-1,155,20,10,-1,155,10,156,-1,157,9,158,-1,159,21,8,-1,159,8,160,-1,161,22,7,-1,161,7,162,-1,163,23,164,-1,165,24,6,-1,165,6,166,-1,167,25,5,-1,167,5,168,-1,169,26,170,-1,171,27,4,-1,171,4,172,-1,173,28,3,-1,173,3,174,-1,175,0,176,-1]
Coordinate404 = x3d.Coordinate()

IndexedFaceSet403.coord = Coordinate404

Shape402.geometry = IndexedFaceSet403
Appearance405 = x3d.Appearance()
Material406 = x3d.Material()
Material406.DEF = "text_color"
Material406.ambientIntensity = 0
Material406.diffuseColor = [0,0,0]
Material406.emissiveColor = [0.819,0.521,0.169]

Appearance405.material = Material406

Shape402.appearance = Appearance405

Transform400.children.append(Shape402)
Transform407 = x3d.Transform()
Transform407.scale = [84.89,77.52,77.52]
Transform407.translation = [0.04092,1.843,3.826]
Shape408 = x3d.Shape()
Shape408.DEF = "Stand_Back"
IndexedFaceSet409 = x3d.IndexedFaceSet()
IndexedFaceSet409.coordIndex = [0,2,3,-1,2,0,1,-1]
Coordinate410 = x3d.Coordinate()

IndexedFaceSet409.coord = Coordinate410

Shape408.geometry = IndexedFaceSet409
Appearance411 = x3d.Appearance()
Material412 = x3d.Material()
Material412.DEF = "Clear"
Material412.ambientIntensity = 0
Material412.diffuseColor = [0,0,0]
Material412.transparency = 1

Appearance411.material = Material412

Shape408.appearance = Appearance411

Transform407.children.append(Shape408)

Transform400.children.append(Transform407)

Transform399.children.append(Transform400)
Transform413 = x3d.Transform()
Transform413.DEF = "Walk_Text"
TouchSensor414 = x3d.TouchSensor()
TouchSensor414.DEF = "Walk_Touch"
TouchSensor414.description = "click for behavior"

Transform413.children.append(TouchSensor414)
Shape415 = x3d.Shape()
Shape415.DEF = "WALK"
IndexedFaceSet416 = x3d.IndexedFaceSet()
IndexedFaceSet416.coordIndex = [0,2,1,-1,3,2,0,-1,12,3,0,-1,4,3,12,-1,11,4,12,-1,5,4,11,-1,10,5,11,-1,6,5,10,-1,9,6,10,-1,7,6,9,-1,8,7,9,-1,15,14,13,-1,16,15,13,-1,19,18,17,-1,20,19,17,-1,27,20,17,-1,28,27,17,-1,26,20,27,-1,23,20,26,-1,21,20,23,-1,25,23,26,-1,22,21,23,-1,24,23,25,-1,29,30,31,-1,29,31,32,-1,33,34,35,-1,33,35,29,-1,29,35,36,-1,29,36,30,-1,30,36,37,-1,37,36,38,-1,37,38,39,-1,37,39,40,-1,37,40,41,-1,41,40,42,-1,41,42,41,-1,41,42,43,-1,41,43,44,-1,44,43,45,-1,44,45,46,-1,47,46,45,-1,47,32,31,-1,47,31,46,-1,38,36,48,-1,38,48,49,-1,49,48,50,-1,49,50,51,-1,51,50,52,-1,51,52,53,-1,51,53,54,-1,54,53,55,-1,54,55,56,-1,54,56,57,-1]
Coordinate417 = x3d.Coordinate()

IndexedFaceSet416.coord = Coordinate417

Shape415.geometry = IndexedFaceSet416
Appearance418 = x3d.Appearance()
Material419 = x3d.Material()
Material419.USE = "text_color"

Appearance418.material = Material419

Shape415.appearance = Appearance418

Transform413.children.append(Shape415)
Transform420 = x3d.Transform()
Transform420.scale = [81.3,81.3,81.31]
Transform420.translation = [-0.0414,1.941,4.015]
Shape421 = x3d.Shape()
Shape421.DEF = "Walk_Back"
IndexedFaceSet422 = x3d.IndexedFaceSet()
IndexedFaceSet422.coordIndex = [1,3,0,-1,3,1,2,-1]
Coordinate423 = x3d.Coordinate()

IndexedFaceSet422.coord = Coordinate423

Shape421.geometry = IndexedFaceSet422
Appearance424 = x3d.Appearance()
Material425 = x3d.Material()
Material425.USE = "Clear"

Appearance424.material = Material425

Shape421.appearance = Appearance424

Transform420.children.append(Shape421)

Transform413.children.append(Transform420)

Transform399.children.append(Transform413)
Transform426 = x3d.Transform()
Transform426.DEF = "Run_Text"
TouchSensor427 = x3d.TouchSensor()
TouchSensor427.DEF = "Run_Touch"
TouchSensor427.description = "click for behavior"

Transform426.children.append(TouchSensor427)
Shape428 = x3d.Shape()
Shape428.DEF = "Run"
IndexedFaceSet429 = x3d.IndexedFaceSet()
IndexedFaceSet429.coordIndex = [24,26,25,-1,53,39,54,-1,17,1,0,-1,17,0,16,-1,0,14,16,-1,0,15,14,-1,14,13,22,-1,14,22,16,-1,13,12,21,-1,13,21,22,-1,12,6,21,-1,12,11,7,-1,12,7,6,-1,11,8,7,-1,10,8,11,-1,10,9,8,-1,6,5,21,-1,5,4,20,-1,5,20,21,-1,4,3,19,-1,4,19,20,-1,3,2,18,-1,3,18,19,-1,18,2,1,-1,18,1,17,-1,55,32,31,-1,55,31,56,-1,57,33,30,-1,57,30,58,-1,59,29,60,-1,61,34,28,-1,61,28,62,-1,63,35,27,-1,63,27,64,-1,65,36,66,-1,67,38,68,-1,69,37,70,-1,71,23,72,-1,73,48,47,-1,73,47,74,-1,75,49,46,-1,75,46,76,-1,77,45,78,-1,79,50,44,-1,79,44,80,-1,81,51,43,-1,81,43,82,-1,83,41,84,-1,85,40,86,-1,87,52,88,-1,89,42,90,-1]
Coordinate430 = x3d.Coordinate()

IndexedFaceSet429.coord = Coordinate430

Shape428.geometry = IndexedFaceSet429
Appearance431 = x3d.Appearance()
Material432 = x3d.Material()
Material432.USE = "text_color"

Appearance431.material = Material432

Shape428.appearance = Appearance431

Transform426.children.append(Shape428)
Transform433 = x3d.Transform()
Transform433.scale = [82.47,82.47,82.48]
Transform433.translation = [-0.01579,1.968,4.074]
Shape434 = x3d.Shape()
Shape434.DEF = "Run_Back"
IndexedFaceSet435 = x3d.IndexedFaceSet()
IndexedFaceSet435.coordIndex = [0,2,3,-1,2,0,1,-1]
Coordinate436 = x3d.Coordinate()

IndexedFaceSet435.coord = Coordinate436

Shape434.geometry = IndexedFaceSet435
Appearance437 = x3d.Appearance()
Material438 = x3d.Material()
Material438.USE = "Clear"

Appearance437.material = Material438

Shape434.appearance = Appearance437

Transform433.children.append(Shape434)

Transform426.children.append(Transform433)

Transform399.children.append(Transform426)
Transform439 = x3d.Transform()
Transform439.DEF = "Jump_Text"
TouchSensor440 = x3d.TouchSensor()
TouchSensor440.DEF = "Jump_Touch"
TouchSensor440.description = "click for behavior"

Transform439.children.append(TouchSensor440)
Shape441 = x3d.Shape()
Shape441.DEF = "Jump"
IndexedFaceSet442 = x3d.IndexedFaceSet()
IndexedFaceSet442.coordIndex = [1,0,14,-1,1,14,2,-1,16,15,18,-1,16,18,17,-1,64,65,66,-1,67,68,69,-1,67,69,70,-1,71,72,73,-1,71,73,74,-1,75,76,77,-1,78,79,80,-1,78,80,81,-1,82,83,84,-1,82,84,85,-1,86,87,88,-1,89,90,91,-1,92,93,94,-1,95,96,97,-1,98,7,6,-1,98,6,99,-1,100,8,5,-1,100,5,101,-1,102,9,4,-1,102,4,103,-1,104,10,105,-1,106,11,3,-1,106,3,107,-1,108,12,109,-1,110,13,111,-1,112,27,26,-1,112,26,113,-1,114,28,25,-1,114,25,115,-1,116,24,117,-1,118,29,23,-1,118,23,119,-1,120,30,22,-1,120,22,121,-1,122,31,123,-1,124,34,33,-1,124,33,125,-1,126,35,32,-1,126,32,127,-1,128,21,129,-1,130,36,20,-1,130,20,131,-1,132,37,19,-1,132,19,133,-1,134,38,135,-1,136,40,137,-1,138,39,139,-1,53,58,59,-1,53,59,54,-1,53,52,58,-1,52,51,57,-1,52,57,58,-1,51,50,56,-1,51,56,57,-1,50,49,56,-1,49,48,63,-1,49,63,56,-1,48,47,63,-1,63,47,46,-1,63,46,62,-1,62,46,45,-1,62,45,44,-1,62,44,61,-1,61,44,60,-1,54,59,60,-1,44,43,42,-1,60,44,42,-1,41,55,54,-1,41,54,60,-1,41,60,42,-1]
Coordinate443 = x3d.Coordinate()

IndexedFaceSet442.coord = Coordinate443

Shape441.geometry = IndexedFaceSet442
Appearance444 = x3d.Appearance()
Material445 = x3d.Material()
Material445.USE = "text_color"

Appearance444.material = Material445

Shape441.appearance = Appearance444

Transform439.children.append(Shape441)
Transform446 = x3d.Transform()
Transform446.scale = [83.79,83.79,83.79]
Transform446.translation = [-0.008979,1.99,4.14]
Shape447 = x3d.Shape()
Shape447.DEF = "Jump_Back"
IndexedFaceSet448 = x3d.IndexedFaceSet()
IndexedFaceSet448.coordIndex = [0,2,3,-1,2,0,1,-1]
Coordinate449 = x3d.Coordinate()

IndexedFaceSet448.coord = Coordinate449

Shape447.geometry = IndexedFaceSet448
Appearance450 = x3d.Appearance()
Material451 = x3d.Material()
Material451.USE = "Clear"

Appearance450.material = Material451

Shape447.appearance = Appearance450

Transform446.children.append(Shape447)

Transform439.children.append(Transform446)

Transform399.children.append(Transform439)

Transform398.children.append(Transform399)

Collision397.proxy = Transform398

Group394.children.append(Collision397)
Transform452 = x3d.Transform()
Transform452.DEF = "Floor"
Transform452.scale = [1,0.0125,1]
Transform452.translation = [0,-0.0125,0]
Shape453 = x3d.Shape()
Box454 = x3d.Box()

Shape453.geometry = Box454
Appearance455 = x3d.Appearance()
Material456 = x3d.Material()

Appearance455.material = Material456

Shape453.appearance = Appearance455

Transform452.children.append(Shape453)

Group394.children.append(Transform452)

Scene14.children.append(Group394)
Group457 = x3d.Group()
Group457.DEF = "Animations"
Group458 = x3d.Group()
Group458.DEF = "Stand_Animation"
OrientationInterpolator459 = x3d.OrientationInterpolator()
OrientationInterpolator459.DEF = "r_ankle_RotationInterpolator_Stand"
OrientationInterpolator459.key = [0,1]

Group458.children.append(OrientationInterpolator459)
OrientationInterpolator460 = x3d.OrientationInterpolator()
OrientationInterpolator460.DEF = "r_knee_RotationInterpolator_Stand"
OrientationInterpolator460.key = [0,1]

Group458.children.append(OrientationInterpolator460)
OrientationInterpolator461 = x3d.OrientationInterpolator()
OrientationInterpolator461.DEF = "r_hip_RotationInterpolator_Stand"
OrientationInterpolator461.key = [0,1]

Group458.children.append(OrientationInterpolator461)
OrientationInterpolator462 = x3d.OrientationInterpolator()
OrientationInterpolator462.DEF = "l_ankle_RotationInterpolator_Stand"
OrientationInterpolator462.key = [0,1]

Group458.children.append(OrientationInterpolator462)
OrientationInterpolator463 = x3d.OrientationInterpolator()
OrientationInterpolator463.DEF = "l_knee_RotationInterpolator_Stand"
OrientationInterpolator463.key = [0,1]

Group458.children.append(OrientationInterpolator463)
OrientationInterpolator464 = x3d.OrientationInterpolator()
OrientationInterpolator464.DEF = "l_hip_RotationInterpolator_Stand"
OrientationInterpolator464.key = [0,1]

Group458.children.append(OrientationInterpolator464)
OrientationInterpolator465 = x3d.OrientationInterpolator()
OrientationInterpolator465.DEF = "lower_body_RotationInterpolator_Stand"
OrientationInterpolator465.key = [0,1]

Group458.children.append(OrientationInterpolator465)
OrientationInterpolator466 = x3d.OrientationInterpolator()
OrientationInterpolator466.DEF = "r_wrist_RotationInterpolator_Stand"
OrientationInterpolator466.key = [0,1]

Group458.children.append(OrientationInterpolator466)
OrientationInterpolator467 = x3d.OrientationInterpolator()
OrientationInterpolator467.DEF = "r_elbow_RotationInterpolator_Stand"
OrientationInterpolator467.key = [0,1]

Group458.children.append(OrientationInterpolator467)
OrientationInterpolator468 = x3d.OrientationInterpolator()
OrientationInterpolator468.DEF = "r_shoulder_RotationInterpolator_Stand"
OrientationInterpolator468.key = [0,1]

Group458.children.append(OrientationInterpolator468)
OrientationInterpolator469 = x3d.OrientationInterpolator()
OrientationInterpolator469.DEF = "l_wrist_RotationInterpolator_Stand"
OrientationInterpolator469.key = [0,1]

Group458.children.append(OrientationInterpolator469)
OrientationInterpolator470 = x3d.OrientationInterpolator()
OrientationInterpolator470.DEF = "l_elbow_RotationInterpolator_Stand"
OrientationInterpolator470.key = [0,1]

Group458.children.append(OrientationInterpolator470)
OrientationInterpolator471 = x3d.OrientationInterpolator()
OrientationInterpolator471.DEF = "l_shoulder_RotationInterpolator_Stand"
OrientationInterpolator471.key = [0,1]

Group458.children.append(OrientationInterpolator471)
OrientationInterpolator472 = x3d.OrientationInterpolator()
OrientationInterpolator472.DEF = "head_RotationInterpolator_Stand"
OrientationInterpolator472.key = [0,1]

Group458.children.append(OrientationInterpolator472)
OrientationInterpolator473 = x3d.OrientationInterpolator()
OrientationInterpolator473.DEF = "neck_RotationInterpolator_Stand"
OrientationInterpolator473.key = [0,1]

Group458.children.append(OrientationInterpolator473)
OrientationInterpolator474 = x3d.OrientationInterpolator()
OrientationInterpolator474.DEF = "upper_body_RotationInterpolator_Stand"
OrientationInterpolator474.key = [0,1]

Group458.children.append(OrientationInterpolator474)
OrientationInterpolator475 = x3d.OrientationInterpolator()
OrientationInterpolator475.DEF = "whole_body_RotationInterpolator_Stand"
OrientationInterpolator475.key = [0,1]

Group458.children.append(OrientationInterpolator475)
PositionInterpolator476 = x3d.PositionInterpolator()
PositionInterpolator476.DEF = "whole_body_TranslationInterpolator_Stand"
PositionInterpolator476.key = [0,1]

Group458.children.append(PositionInterpolator476)
TimeSensor477 = x3d.TimeSensor()
TimeSensor477.DEF = "Stand_Time"
TimeSensor477.cycleInterval = 0.009999999776482582

Group458.children.append(TimeSensor477)

Group457.children.append(Group458)
Group478 = x3d.Group()
Group478.DEF = "Walk_Animation"
OrientationInterpolator479 = x3d.OrientationInterpolator()
OrientationInterpolator479.DEF = "r_ankle_RotationInterpolator_BasicWalk"
OrientationInterpolator479.key = [0,0.125,0.2083,0.375,0.4583,0.5,0.6667,0.75,0.7917,0.9167,1]

Group478.children.append(OrientationInterpolator479)
OrientationInterpolator480 = x3d.OrientationInterpolator()
OrientationInterpolator480.DEF = "r_knee_RotationInterpolator_BasicWalk"
OrientationInterpolator480.key = [0,0.125,0.2083,0.2917,0.375,0.5,0.6667,0.7917,0.9167,1]

Group478.children.append(OrientationInterpolator480)
OrientationInterpolator481 = x3d.OrientationInterpolator()
OrientationInterpolator481.DEF = "r_hip_RotationInterpolator_BasicWalk"
OrientationInterpolator481.key = [0,0.125,0.2083,0.2917,0.375,0.5,0.6667,0.7917,0.9167,1]

Group478.children.append(OrientationInterpolator481)
OrientationInterpolator482 = x3d.OrientationInterpolator()
OrientationInterpolator482.DEF = "l_ankle_RotationInterpolator_BasicWalk"
OrientationInterpolator482.key = [0,0.125,0.2083,0.375,0.6667,0.9167,1]

Group478.children.append(OrientationInterpolator482)
OrientationInterpolator483 = x3d.OrientationInterpolator()
OrientationInterpolator483.DEF = "l_knee_RotationInterpolator_BasicWalk"
OrientationInterpolator483.key = [0,0.2083,0.375,0.5,0.6667,0.7917,0.9167,1]

Group478.children.append(OrientationInterpolator483)
OrientationInterpolator484 = x3d.OrientationInterpolator()
OrientationInterpolator484.DEF = "l_hip_RotationInterpolator_BasicWalk"
OrientationInterpolator484.key = [0,0.25,0.375,0.5,0.6667,0.7917,0.9167,1]

Group478.children.append(OrientationInterpolator484)
OrientationInterpolator485 = x3d.OrientationInterpolator()
OrientationInterpolator485.DEF = "lower_body_RotationInterpolator_BasicWalk"
OrientationInterpolator485.key = [0,0.5,1]

Group478.children.append(OrientationInterpolator485)
OrientationInterpolator486 = x3d.OrientationInterpolator()
OrientationInterpolator486.DEF = "r_wrist_RotationInterpolator_BasicWalk"
OrientationInterpolator486.key = [0,0.375,0.9167,1]

Group478.children.append(OrientationInterpolator486)
OrientationInterpolator487 = x3d.OrientationInterpolator()
OrientationInterpolator487.DEF = "r_elbow_RotationInterpolator_BasicWalk"
OrientationInterpolator487.key = [0,0.375,0.9167,1]

Group478.children.append(OrientationInterpolator487)
OrientationInterpolator488 = x3d.OrientationInterpolator()
OrientationInterpolator488.DEF = "r_shoulder_RotationInterpolator_BasicWalk"
OrientationInterpolator488.key = [0,0.375,0.9167,1]

Group478.children.append(OrientationInterpolator488)
OrientationInterpolator489 = x3d.OrientationInterpolator()
OrientationInterpolator489.DEF = "l_wrist_RotationInterpolator_BasicWalk"
OrientationInterpolator489.key = [0,0.375,0.9167,1]

Group478.children.append(OrientationInterpolator489)
OrientationInterpolator490 = x3d.OrientationInterpolator()
OrientationInterpolator490.DEF = "l_elbow_RotationInterpolator_BasicWalk"
OrientationInterpolator490.key = [0,0.375,0.9167,1]

Group478.children.append(OrientationInterpolator490)
OrientationInterpolator491 = x3d.OrientationInterpolator()
OrientationInterpolator491.DEF = "l_shoulder_RotationInterpolator_BasicWalk"
OrientationInterpolator491.key = [0,0.375,0.9167,1]

Group478.children.append(OrientationInterpolator491)
OrientationInterpolator492 = x3d.OrientationInterpolator()
OrientationInterpolator492.DEF = "head_RotationInterpolator_BasicWalk"
OrientationInterpolator492.key = [0,0.375,0.4167,0.5,0.5833,0.6667,0.75,0.8333,0.9167,1]

Group478.children.append(OrientationInterpolator492)
OrientationInterpolator493 = x3d.OrientationInterpolator()
OrientationInterpolator493.DEF = "neck_RotationInterpolator_BasicWalk"
OrientationInterpolator493.key = [0,1]

Group478.children.append(OrientationInterpolator493)
OrientationInterpolator494 = x3d.OrientationInterpolator()
OrientationInterpolator494.DEF = "upper_body_RotationInterpolator_BasicWalk"
OrientationInterpolator494.key = [0,0.2083,0.375,0.75,0.8333,1]

Group478.children.append(OrientationInterpolator494)
OrientationInterpolator495 = x3d.OrientationInterpolator()
OrientationInterpolator495.DEF = "whole_body_RotationInterpolator_BasicWalk"
OrientationInterpolator495.key = [0,1]

Group478.children.append(OrientationInterpolator495)
PositionInterpolator496 = x3d.PositionInterpolator()
PositionInterpolator496.DEF = "whole_body_TranslationInterpolator_BasicWalk"
PositionInterpolator496.key = [0,0.04167,0.125,0.1667,0.2083,0.25,0.2917,0.375,0.4583,0.5,0.5417,0.5833,0.625,0.7083,0.75,0.7917,0.875,0.9167,1]

Group478.children.append(PositionInterpolator496)
TimeSensor497 = x3d.TimeSensor()
TimeSensor497.DEF = "Walk_Time"
TimeSensor497.cycleInterval = 2
TimeSensor497.loop = True
TimeSensor497.startTime = -1

Group478.children.append(TimeSensor497)

Group457.children.append(Group478)
Group498 = x3d.Group()
Group498.DEF = "Run_Animation"
OrientationInterpolator499 = x3d.OrientationInterpolator()
OrientationInterpolator499.DEF = "r_ankle_RotationInterpolator_Run"
OrientationInterpolator499.key = [0,0.4909,0.7091,0.8,0.8182,1]

Group498.children.append(OrientationInterpolator499)
OrientationInterpolator500 = x3d.OrientationInterpolator()
OrientationInterpolator500.DEF = "r_knee_RotationInterpolator_Run"
OrientationInterpolator500.key = [0,0.03636,0.2182,0.4909,0.7455,1]

Group498.children.append(OrientationInterpolator500)
OrientationInterpolator501 = x3d.OrientationInterpolator()
OrientationInterpolator501.DEF = "r_hip_RotationInterpolator_Run"
OrientationInterpolator501.key = [0,0.2182,0.4909,0.7455,1]

Group498.children.append(OrientationInterpolator501)
OrientationInterpolator502 = x3d.OrientationInterpolator()
OrientationInterpolator502.DEF = "l_ankle_RotationInterpolator_Run"
OrientationInterpolator502.key = [0,0.2182,0.3091,0.4909,1]

Group498.children.append(OrientationInterpolator502)
OrientationInterpolator503 = x3d.OrientationInterpolator()
OrientationInterpolator503.DEF = "l_knee_RotationInterpolator_Run"
OrientationInterpolator503.key = [0,0.2182,0.4909,0.7455,1]

Group498.children.append(OrientationInterpolator503)
OrientationInterpolator504 = x3d.OrientationInterpolator()
OrientationInterpolator504.DEF = "l_hip_RotationInterpolator_Run"
OrientationInterpolator504.key = [0,0.2182,0.4909,0.7455,1]

Group498.children.append(OrientationInterpolator504)
OrientationInterpolator505 = x3d.OrientationInterpolator()
OrientationInterpolator505.DEF = "lower_body_RotationInterpolator_Run"
OrientationInterpolator505.key = [0,1]

Group498.children.append(OrientationInterpolator505)
OrientationInterpolator506 = x3d.OrientationInterpolator()
OrientationInterpolator506.DEF = "r_wrist_RotationInterpolator_Run"
OrientationInterpolator506.key = [0,1]

Group498.children.append(OrientationInterpolator506)
OrientationInterpolator507 = x3d.OrientationInterpolator()
OrientationInterpolator507.DEF = "r_elbow_RotationInterpolator_Run"
OrientationInterpolator507.key = [0,0.2182,0.4909,0.7455,1]

Group498.children.append(OrientationInterpolator507)
OrientationInterpolator508 = x3d.OrientationInterpolator()
OrientationInterpolator508.DEF = "r_shoulder_RotationInterpolator_Run"
OrientationInterpolator508.key = [0,0.2182,0.4909,0.7455,1]

Group498.children.append(OrientationInterpolator508)
OrientationInterpolator509 = x3d.OrientationInterpolator()
OrientationInterpolator509.DEF = "l_wrist_RotationInterpolator_Run"
OrientationInterpolator509.key = [0,1]

Group498.children.append(OrientationInterpolator509)
OrientationInterpolator510 = x3d.OrientationInterpolator()
OrientationInterpolator510.DEF = "l_elbow_RotationInterpolator_Run"
OrientationInterpolator510.key = [0,0.2182,0.4909,0.7455,1]

Group498.children.append(OrientationInterpolator510)
OrientationInterpolator511 = x3d.OrientationInterpolator()
OrientationInterpolator511.DEF = "l_shoulder_RotationInterpolator_Run"
OrientationInterpolator511.key = [0,0.2182,0.4909,0.7455,1]

Group498.children.append(OrientationInterpolator511)
OrientationInterpolator512 = x3d.OrientationInterpolator()
OrientationInterpolator512.DEF = "head_RotationInterpolator_Run"
OrientationInterpolator512.key = [0,0.4909,1]

Group498.children.append(OrientationInterpolator512)
OrientationInterpolator513 = x3d.OrientationInterpolator()
OrientationInterpolator513.DEF = "neck_RotationInterpolator_Run"
OrientationInterpolator513.key = [0,1]

Group498.children.append(OrientationInterpolator513)
OrientationInterpolator514 = x3d.OrientationInterpolator()
OrientationInterpolator514.DEF = "upper_body_RotationInterpolator_Run"
OrientationInterpolator514.key = [0,0.2545,0.4909,0.7636,1]

Group498.children.append(OrientationInterpolator514)
OrientationInterpolator515 = x3d.OrientationInterpolator()
OrientationInterpolator515.DEF = "whole_body_RotationInterpolator_Run"
OrientationInterpolator515.key = [0,1]

Group498.children.append(OrientationInterpolator515)
PositionInterpolator516 = x3d.PositionInterpolator()
PositionInterpolator516.DEF = "whole_body_TranslationInterpolator_Run"
PositionInterpolator516.key = [0,0.2182,0.2909,0.3091,0.7091,0.8,0.8182,1]

Group498.children.append(PositionInterpolator516)
TimeSensor517 = x3d.TimeSensor()
TimeSensor517.DEF = "Run_Time"
TimeSensor517.loop = True
TimeSensor517.startTime = -1

Group498.children.append(TimeSensor517)

Group457.children.append(Group498)
Group518 = x3d.Group()
Group518.DEF = "Jump_Animation"
OrientationInterpolator519 = x3d.OrientationInterpolator()
OrientationInterpolator519.DEF = "r_ankle_RotationInterpolator_Jump"
OrientationInterpolator519.key = [0,0.28,0.32,0.36,0.4,0.44,0.48,0.64,0.76,0.84,0.88,0.92,0.96,1]

Group518.children.append(OrientationInterpolator519)
OrientationInterpolator520 = x3d.OrientationInterpolator()
OrientationInterpolator520.DEF = "r_knee_RotationInterpolator_Jump"
OrientationInterpolator520.key = [0,0.28,0.32,0.48,0.64,0.76,0.88,1]

Group518.children.append(OrientationInterpolator520)
OrientationInterpolator521 = x3d.OrientationInterpolator()
OrientationInterpolator521.DEF = "r_hip_RotationInterpolator_Jump"
OrientationInterpolator521.key = [0,0.28,0.32,0.36,0.4,0.44,0.48,0.64,0.76,0.88,1]

Group518.children.append(OrientationInterpolator521)
OrientationInterpolator522 = x3d.OrientationInterpolator()
OrientationInterpolator522.DEF = "l_ankle_RotationInterpolator_Jump"
OrientationInterpolator522.key = [0,0.28,0.32,0.36,0.4,0.44,0.48,0.64,0.76,0.84,0.88,0.92,0.96,1]

Group518.children.append(OrientationInterpolator522)
OrientationInterpolator523 = x3d.OrientationInterpolator()
OrientationInterpolator523.DEF = "l_knee_RotationInterpolator_Jump"
OrientationInterpolator523.key = [0,0.28,0.32,0.48,0.64,0.76,0.88,1]

Group518.children.append(OrientationInterpolator523)
OrientationInterpolator524 = x3d.OrientationInterpolator()
OrientationInterpolator524.DEF = "l_hip_RotationInterpolator_Jump"
OrientationInterpolator524.key = [0,0.28,0.32,0.36,0.4,0.44,0.48,0.64,0.76,0.88,1]

Group518.children.append(OrientationInterpolator524)
OrientationInterpolator525 = x3d.OrientationInterpolator()
OrientationInterpolator525.DEF = "lower_body_RotationInterpolator_Jump"
OrientationInterpolator525.key = [0,0.28,0.32,0.48,0.76,1]

Group518.children.append(OrientationInterpolator525)
OrientationInterpolator526 = x3d.OrientationInterpolator()
OrientationInterpolator526.DEF = "r_wrist_RotationInterpolator_Jump"
OrientationInterpolator526.key = [0,0.28,0.32,0.64,0.76,1]

Group518.children.append(OrientationInterpolator526)
OrientationInterpolator527 = x3d.OrientationInterpolator()
OrientationInterpolator527.DEF = "r_elbow_RotationInterpolator_Jump"
OrientationInterpolator527.key = [0,0.28,0.32,0.64,0.76,1]

Group518.children.append(OrientationInterpolator527)
OrientationInterpolator528 = x3d.OrientationInterpolator()
OrientationInterpolator528.DEF = "r_shoulder_RotationInterpolator_Jump"
OrientationInterpolator528.key = [0,0.28,0.32,0.64,0.76,0.88,1]

Group518.children.append(OrientationInterpolator528)
OrientationInterpolator529 = x3d.OrientationInterpolator()
OrientationInterpolator529.DEF = "l_wrist_RotationInterpolator_Jump"
OrientationInterpolator529.key = [0,0.28,0.32,0.64,0.76,0.88,1]

Group518.children.append(OrientationInterpolator529)
OrientationInterpolator530 = x3d.OrientationInterpolator()
OrientationInterpolator530.DEF = "l_elbow_RotationInterpolator_Jump"
OrientationInterpolator530.key = [0,0.28,0.32,0.64,0.76,1]

Group518.children.append(OrientationInterpolator530)
OrientationInterpolator531 = x3d.OrientationInterpolator()
OrientationInterpolator531.DEF = "l_shoulder_RotationInterpolator_Jump"
OrientationInterpolator531.key = [0,0.28,0.32,0.64,0.76,0.88,1]

Group518.children.append(OrientationInterpolator531)
OrientationInterpolator532 = x3d.OrientationInterpolator()
OrientationInterpolator532.DEF = "head_RotationInterpolator_Jump"
OrientationInterpolator532.key = [0,0.28,0.32,0.48,0.76,1]

Group518.children.append(OrientationInterpolator532)
OrientationInterpolator533 = x3d.OrientationInterpolator()
OrientationInterpolator533.DEF = "neck_RotationInterpolator_Jump"
OrientationInterpolator533.key = [0,0.28,0.32,0.48,0.76,1]

Group518.children.append(OrientationInterpolator533)
OrientationInterpolator534 = x3d.OrientationInterpolator()
OrientationInterpolator534.DEF = "upper_body_RotationInterpolator_Jump"
OrientationInterpolator534.key = [0,0.28,0.32,0.48,0.76,0.88,1]

Group518.children.append(OrientationInterpolator534)
OrientationInterpolator535 = x3d.OrientationInterpolator()
OrientationInterpolator535.DEF = "whole_body_RotationInterpolator_Jump"
OrientationInterpolator535.key = [0,0.28,0.32,0.48,0.64,0.76,1]

Group518.children.append(OrientationInterpolator535)
PositionInterpolator536 = x3d.PositionInterpolator()
PositionInterpolator536.DEF = "whole_body_TranslationInterpolator_Jump"
PositionInterpolator536.key = [0,0.04,0.08,0.12,0.16,0.2,0.24,0.28,0.32,0.36,0.4,0.44,0.48,0.64,0.76,0.8,0.84,0.88,0.92,0.96,1]

Group518.children.append(PositionInterpolator536)
TimeSensor537 = x3d.TimeSensor()
TimeSensor537.DEF = "Jump_Time"
TimeSensor537.cycleInterval = 2
TimeSensor537.startTime = -1

Group518.children.append(TimeSensor537)

Group457.children.append(Group518)

Scene14.children.append(Group457)
ROUTE538 = x3d.ROUTE()
ROUTE538.fromField = "position_changed"
ROUTE538.fromNode = "HudProx"
ROUTE538.toField = "set_translation"
ROUTE538.toNode = "HudXform"

Scene14.children.append(ROUTE538)
ROUTE539 = x3d.ROUTE()
ROUTE539.fromField = "orientation_changed"
ROUTE539.fromNode = "HudProx"
ROUTE539.toField = "set_rotation"
ROUTE539.toNode = "HudXform"

Scene14.children.append(ROUTE539)
ROUTE540 = x3d.ROUTE()
ROUTE540.fromField = "touchTime"
ROUTE540.fromNode = "Stand_Touch"
ROUTE540.toField = "stopTime"
ROUTE540.toNode = "Walk_Time"

Scene14.children.append(ROUTE540)
ROUTE541 = x3d.ROUTE()
ROUTE541.fromField = "touchTime"
ROUTE541.fromNode = "Stand_Touch"
ROUTE541.toField = "stopTime"
ROUTE541.toNode = "Run_Time"

Scene14.children.append(ROUTE541)
ROUTE542 = x3d.ROUTE()
ROUTE542.fromField = "touchTime"
ROUTE542.fromNode = "Stand_Touch"
ROUTE542.toField = "stopTime"
ROUTE542.toNode = "Jump_Time"

Scene14.children.append(ROUTE542)
ROUTE543 = x3d.ROUTE()
ROUTE543.fromField = "touchTime"
ROUTE543.fromNode = "Stand_Touch"
ROUTE543.toField = "startTime"
ROUTE543.toNode = "Stand_Time"

Scene14.children.append(ROUTE543)
ROUTE544 = x3d.ROUTE()
ROUTE544.fromField = "touchTime"
ROUTE544.fromNode = "Walk_Touch"
ROUTE544.toField = "stopTime"
ROUTE544.toNode = "Stand_Time"

Scene14.children.append(ROUTE544)
ROUTE545 = x3d.ROUTE()
ROUTE545.fromField = "touchTime"
ROUTE545.fromNode = "Walk_Touch"
ROUTE545.toField = "stopTime"
ROUTE545.toNode = "Run_Time"

Scene14.children.append(ROUTE545)
ROUTE546 = x3d.ROUTE()
ROUTE546.fromField = "touchTime"
ROUTE546.fromNode = "Walk_Touch"
ROUTE546.toField = "stopTime"
ROUTE546.toNode = "Jump_Time"

Scene14.children.append(ROUTE546)
ROUTE547 = x3d.ROUTE()
ROUTE547.fromField = "touchTime"
ROUTE547.fromNode = "Walk_Touch"
ROUTE547.toField = "startTime"
ROUTE547.toNode = "Walk_Time"

Scene14.children.append(ROUTE547)
ROUTE548 = x3d.ROUTE()
ROUTE548.fromField = "touchTime"
ROUTE548.fromNode = "Run_Touch"
ROUTE548.toField = "stopTime"
ROUTE548.toNode = "Stand_Time"

Scene14.children.append(ROUTE548)
ROUTE549 = x3d.ROUTE()
ROUTE549.fromField = "touchTime"
ROUTE549.fromNode = "Run_Touch"
ROUTE549.toField = "stopTime"
ROUTE549.toNode = "Walk_Time"

Scene14.children.append(ROUTE549)
ROUTE550 = x3d.ROUTE()
ROUTE550.fromField = "touchTime"
ROUTE550.fromNode = "Run_Touch"
ROUTE550.toField = "stopTime"
ROUTE550.toNode = "Jump_Time"

Scene14.children.append(ROUTE550)
ROUTE551 = x3d.ROUTE()
ROUTE551.fromField = "touchTime"
ROUTE551.fromNode = "Run_Touch"
ROUTE551.toField = "startTime"
ROUTE551.toNode = "Run_Time"

Scene14.children.append(ROUTE551)
ROUTE552 = x3d.ROUTE()
ROUTE552.fromField = "touchTime"
ROUTE552.fromNode = "Jump_Touch"
ROUTE552.toField = "stopTime"
ROUTE552.toNode = "Stand_Time"

Scene14.children.append(ROUTE552)
ROUTE553 = x3d.ROUTE()
ROUTE553.fromField = "touchTime"
ROUTE553.fromNode = "Jump_Touch"
ROUTE553.toField = "stopTime"
ROUTE553.toNode = "Walk_Time"

Scene14.children.append(ROUTE553)
ROUTE554 = x3d.ROUTE()
ROUTE554.fromField = "touchTime"
ROUTE554.fromNode = "Jump_Touch"
ROUTE554.toField = "stopTime"
ROUTE554.toNode = "Run_Time"

Scene14.children.append(ROUTE554)
ROUTE555 = x3d.ROUTE()
ROUTE555.fromField = "touchTime"
ROUTE555.fromNode = "Jump_Touch"
ROUTE555.toField = "startTime"
ROUTE555.toNode = "Jump_Time"

Scene14.children.append(ROUTE555)
ROUTE556 = x3d.ROUTE()
ROUTE556.fromField = "fraction_changed"
ROUTE556.fromNode = "Stand_Time"
ROUTE556.toField = "set_fraction"
ROUTE556.toNode = "r_ankle_RotationInterpolator_Stand"

Scene14.children.append(ROUTE556)
ROUTE557 = x3d.ROUTE()
ROUTE557.fromField = "fraction_changed"
ROUTE557.fromNode = "Stand_Time"
ROUTE557.toField = "set_fraction"
ROUTE557.toNode = "r_knee_RotationInterpolator_Stand"

Scene14.children.append(ROUTE557)
ROUTE558 = x3d.ROUTE()
ROUTE558.fromField = "fraction_changed"
ROUTE558.fromNode = "Stand_Time"
ROUTE558.toField = "set_fraction"
ROUTE558.toNode = "r_hip_RotationInterpolator_Stand"

Scene14.children.append(ROUTE558)
ROUTE559 = x3d.ROUTE()
ROUTE559.fromField = "fraction_changed"
ROUTE559.fromNode = "Stand_Time"
ROUTE559.toField = "set_fraction"
ROUTE559.toNode = "l_ankle_RotationInterpolator_Stand"

Scene14.children.append(ROUTE559)
ROUTE560 = x3d.ROUTE()
ROUTE560.fromField = "fraction_changed"
ROUTE560.fromNode = "Stand_Time"
ROUTE560.toField = "set_fraction"
ROUTE560.toNode = "l_knee_RotationInterpolator_Stand"

Scene14.children.append(ROUTE560)
ROUTE561 = x3d.ROUTE()
ROUTE561.fromField = "fraction_changed"
ROUTE561.fromNode = "Stand_Time"
ROUTE561.toField = "set_fraction"
ROUTE561.toNode = "l_hip_RotationInterpolator_Stand"

Scene14.children.append(ROUTE561)
ROUTE562 = x3d.ROUTE()
ROUTE562.fromField = "fraction_changed"
ROUTE562.fromNode = "Stand_Time"
ROUTE562.toField = "set_fraction"
ROUTE562.toNode = "lower_body_RotationInterpolator_Stand"

Scene14.children.append(ROUTE562)
ROUTE563 = x3d.ROUTE()
ROUTE563.fromField = "fraction_changed"
ROUTE563.fromNode = "Stand_Time"
ROUTE563.toField = "set_fraction"
ROUTE563.toNode = "r_wrist_RotationInterpolator_Stand"

Scene14.children.append(ROUTE563)
ROUTE564 = x3d.ROUTE()
ROUTE564.fromField = "fraction_changed"
ROUTE564.fromNode = "Stand_Time"
ROUTE564.toField = "set_fraction"
ROUTE564.toNode = "r_elbow_RotationInterpolator_Stand"

Scene14.children.append(ROUTE564)
ROUTE565 = x3d.ROUTE()
ROUTE565.fromField = "fraction_changed"
ROUTE565.fromNode = "Stand_Time"
ROUTE565.toField = "set_fraction"
ROUTE565.toNode = "r_shoulder_RotationInterpolator_Stand"

Scene14.children.append(ROUTE565)
ROUTE566 = x3d.ROUTE()
ROUTE566.fromField = "fraction_changed"
ROUTE566.fromNode = "Stand_Time"
ROUTE566.toField = "set_fraction"
ROUTE566.toNode = "l_wrist_RotationInterpolator_Stand"

Scene14.children.append(ROUTE566)
ROUTE567 = x3d.ROUTE()
ROUTE567.fromField = "fraction_changed"
ROUTE567.fromNode = "Stand_Time"
ROUTE567.toField = "set_fraction"
ROUTE567.toNode = "l_elbow_RotationInterpolator_Stand"

Scene14.children.append(ROUTE567)
ROUTE568 = x3d.ROUTE()
ROUTE568.fromField = "fraction_changed"
ROUTE568.fromNode = "Stand_Time"
ROUTE568.toField = "set_fraction"
ROUTE568.toNode = "l_shoulder_RotationInterpolator_Stand"

Scene14.children.append(ROUTE568)
ROUTE569 = x3d.ROUTE()
ROUTE569.fromField = "fraction_changed"
ROUTE569.fromNode = "Stand_Time"
ROUTE569.toField = "set_fraction"
ROUTE569.toNode = "head_RotationInterpolator_Stand"

Scene14.children.append(ROUTE569)
ROUTE570 = x3d.ROUTE()
ROUTE570.fromField = "fraction_changed"
ROUTE570.fromNode = "Stand_Time"
ROUTE570.toField = "set_fraction"
ROUTE570.toNode = "neck_RotationInterpolator_Stand"

Scene14.children.append(ROUTE570)
ROUTE571 = x3d.ROUTE()
ROUTE571.fromField = "fraction_changed"
ROUTE571.fromNode = "Stand_Time"
ROUTE571.toField = "set_fraction"
ROUTE571.toNode = "upper_body_RotationInterpolator_Stand"

Scene14.children.append(ROUTE571)
ROUTE572 = x3d.ROUTE()
ROUTE572.fromField = "fraction_changed"
ROUTE572.fromNode = "Stand_Time"
ROUTE572.toField = "set_fraction"
ROUTE572.toNode = "whole_body_RotationInterpolator_Stand"

Scene14.children.append(ROUTE572)
ROUTE573 = x3d.ROUTE()
ROUTE573.fromField = "fraction_changed"
ROUTE573.fromNode = "Stand_Time"
ROUTE573.toField = "set_fraction"
ROUTE573.toNode = "whole_body_TranslationInterpolator_Stand"

Scene14.children.append(ROUTE573)
ROUTE574 = x3d.ROUTE()
ROUTE574.fromField = "value_changed"
ROUTE574.fromNode = "r_ankle_RotationInterpolator_Stand"
ROUTE574.toField = "set_rotation"
ROUTE574.toNode = "hanim_r_ankle"

Scene14.children.append(ROUTE574)
ROUTE575 = x3d.ROUTE()
ROUTE575.fromField = "value_changed"
ROUTE575.fromNode = "r_knee_RotationInterpolator_Stand"
ROUTE575.toField = "set_rotation"
ROUTE575.toNode = "hanim_r_knee"

Scene14.children.append(ROUTE575)
ROUTE576 = x3d.ROUTE()
ROUTE576.fromField = "value_changed"
ROUTE576.fromNode = "r_hip_RotationInterpolator_Stand"
ROUTE576.toField = "set_rotation"
ROUTE576.toNode = "hanim_r_hip"

Scene14.children.append(ROUTE576)
ROUTE577 = x3d.ROUTE()
ROUTE577.fromField = "value_changed"
ROUTE577.fromNode = "l_ankle_RotationInterpolator_Stand"
ROUTE577.toField = "set_rotation"
ROUTE577.toNode = "hanim_l_ankle"

Scene14.children.append(ROUTE577)
ROUTE578 = x3d.ROUTE()
ROUTE578.fromField = "value_changed"
ROUTE578.fromNode = "l_knee_RotationInterpolator_Stand"
ROUTE578.toField = "set_rotation"
ROUTE578.toNode = "hanim_l_knee"

Scene14.children.append(ROUTE578)
ROUTE579 = x3d.ROUTE()
ROUTE579.fromField = "value_changed"
ROUTE579.fromNode = "l_hip_RotationInterpolator_Stand"
ROUTE579.toField = "set_rotation"
ROUTE579.toNode = "hanim_l_hip"

Scene14.children.append(ROUTE579)
ROUTE580 = x3d.ROUTE()
ROUTE580.fromField = "value_changed"
ROUTE580.fromNode = "lower_body_RotationInterpolator_Stand"
ROUTE580.toField = "set_rotation"
ROUTE580.toNode = "hanim_sacroiliac"

Scene14.children.append(ROUTE580)
ROUTE581 = x3d.ROUTE()
ROUTE581.fromField = "value_changed"
ROUTE581.fromNode = "r_wrist_RotationInterpolator_Stand"
ROUTE581.toField = "set_rotation"
ROUTE581.toNode = "hanim_r_wrist"

Scene14.children.append(ROUTE581)
ROUTE582 = x3d.ROUTE()
ROUTE582.fromField = "value_changed"
ROUTE582.fromNode = "r_elbow_RotationInterpolator_Stand"
ROUTE582.toField = "set_rotation"
ROUTE582.toNode = "hanim_r_elbow"

Scene14.children.append(ROUTE582)
ROUTE583 = x3d.ROUTE()
ROUTE583.fromField = "value_changed"
ROUTE583.fromNode = "r_shoulder_RotationInterpolator_Stand"
ROUTE583.toField = "set_rotation"
ROUTE583.toNode = "hanim_r_shoulder"

Scene14.children.append(ROUTE583)
ROUTE584 = x3d.ROUTE()
ROUTE584.fromField = "value_changed"
ROUTE584.fromNode = "l_wrist_RotationInterpolator_Stand"
ROUTE584.toField = "set_rotation"
ROUTE584.toNode = "hanim_l_wrist"

Scene14.children.append(ROUTE584)
ROUTE585 = x3d.ROUTE()
ROUTE585.fromField = "value_changed"
ROUTE585.fromNode = "l_elbow_RotationInterpolator_Stand"
ROUTE585.toField = "set_rotation"
ROUTE585.toNode = "hanim_l_elbow"

Scene14.children.append(ROUTE585)
ROUTE586 = x3d.ROUTE()
ROUTE586.fromField = "value_changed"
ROUTE586.fromNode = "l_shoulder_RotationInterpolator_Stand"
ROUTE586.toField = "set_rotation"
ROUTE586.toNode = "hanim_l_shoulder"

Scene14.children.append(ROUTE586)
ROUTE587 = x3d.ROUTE()
ROUTE587.fromField = "value_changed"
ROUTE587.fromNode = "head_RotationInterpolator_Stand"
ROUTE587.toField = "set_rotation"
ROUTE587.toNode = "hanim_skullbase"

Scene14.children.append(ROUTE587)
ROUTE588 = x3d.ROUTE()
ROUTE588.fromField = "value_changed"
ROUTE588.fromNode = "neck_RotationInterpolator_Stand"
ROUTE588.toField = "set_rotation"
ROUTE588.toNode = "hanim_vc4"

Scene14.children.append(ROUTE588)
ROUTE589 = x3d.ROUTE()
ROUTE589.fromField = "value_changed"
ROUTE589.fromNode = "upper_body_RotationInterpolator_Stand"
ROUTE589.toField = "set_rotation"
ROUTE589.toNode = "hanim_vl1"

Scene14.children.append(ROUTE589)
ROUTE590 = x3d.ROUTE()
ROUTE590.fromField = "value_changed"
ROUTE590.fromNode = "whole_body_RotationInterpolator_Stand"
ROUTE590.toField = "set_rotation"
ROUTE590.toNode = "hanim_humanoid_root"

Scene14.children.append(ROUTE590)
ROUTE591 = x3d.ROUTE()
ROUTE591.fromField = "value_changed"
ROUTE591.fromNode = "whole_body_TranslationInterpolator_Stand"
ROUTE591.toField = "set_translation"
ROUTE591.toNode = "hanim_humanoid_root"

Scene14.children.append(ROUTE591)
ROUTE592 = x3d.ROUTE()
ROUTE592.fromField = "fraction_changed"
ROUTE592.fromNode = "Walk_Time"
ROUTE592.toField = "set_fraction"
ROUTE592.toNode = "r_ankle_RotationInterpolator_BasicWalk"

Scene14.children.append(ROUTE592)
ROUTE593 = x3d.ROUTE()
ROUTE593.fromField = "fraction_changed"
ROUTE593.fromNode = "Walk_Time"
ROUTE593.toField = "set_fraction"
ROUTE593.toNode = "r_knee_RotationInterpolator_BasicWalk"

Scene14.children.append(ROUTE593)
ROUTE594 = x3d.ROUTE()
ROUTE594.fromField = "fraction_changed"
ROUTE594.fromNode = "Walk_Time"
ROUTE594.toField = "set_fraction"
ROUTE594.toNode = "r_hip_RotationInterpolator_BasicWalk"

Scene14.children.append(ROUTE594)
ROUTE595 = x3d.ROUTE()
ROUTE595.fromField = "fraction_changed"
ROUTE595.fromNode = "Walk_Time"
ROUTE595.toField = "set_fraction"
ROUTE595.toNode = "l_ankle_RotationInterpolator_BasicWalk"

Scene14.children.append(ROUTE595)
ROUTE596 = x3d.ROUTE()
ROUTE596.fromField = "fraction_changed"
ROUTE596.fromNode = "Walk_Time"
ROUTE596.toField = "set_fraction"
ROUTE596.toNode = "l_knee_RotationInterpolator_BasicWalk"

Scene14.children.append(ROUTE596)
ROUTE597 = x3d.ROUTE()
ROUTE597.fromField = "fraction_changed"
ROUTE597.fromNode = "Walk_Time"
ROUTE597.toField = "set_fraction"
ROUTE597.toNode = "l_hip_RotationInterpolator_BasicWalk"

Scene14.children.append(ROUTE597)
ROUTE598 = x3d.ROUTE()
ROUTE598.fromField = "fraction_changed"
ROUTE598.fromNode = "Walk_Time"
ROUTE598.toField = "set_fraction"
ROUTE598.toNode = "lower_body_RotationInterpolator_BasicWalk"

Scene14.children.append(ROUTE598)
ROUTE599 = x3d.ROUTE()
ROUTE599.fromField = "fraction_changed"
ROUTE599.fromNode = "Walk_Time"
ROUTE599.toField = "set_fraction"
ROUTE599.toNode = "r_wrist_RotationInterpolator_BasicWalk"

Scene14.children.append(ROUTE599)
ROUTE600 = x3d.ROUTE()
ROUTE600.fromField = "fraction_changed"
ROUTE600.fromNode = "Walk_Time"
ROUTE600.toField = "set_fraction"
ROUTE600.toNode = "r_elbow_RotationInterpolator_BasicWalk"

Scene14.children.append(ROUTE600)
ROUTE601 = x3d.ROUTE()
ROUTE601.fromField = "fraction_changed"
ROUTE601.fromNode = "Walk_Time"
ROUTE601.toField = "set_fraction"
ROUTE601.toNode = "r_shoulder_RotationInterpolator_BasicWalk"

Scene14.children.append(ROUTE601)
ROUTE602 = x3d.ROUTE()
ROUTE602.fromField = "fraction_changed"
ROUTE602.fromNode = "Walk_Time"
ROUTE602.toField = "set_fraction"
ROUTE602.toNode = "l_wrist_RotationInterpolator_BasicWalk"

Scene14.children.append(ROUTE602)
ROUTE603 = x3d.ROUTE()
ROUTE603.fromField = "fraction_changed"
ROUTE603.fromNode = "Walk_Time"
ROUTE603.toField = "set_fraction"
ROUTE603.toNode = "l_elbow_RotationInterpolator_BasicWalk"

Scene14.children.append(ROUTE603)
ROUTE604 = x3d.ROUTE()
ROUTE604.fromField = "fraction_changed"
ROUTE604.fromNode = "Walk_Time"
ROUTE604.toField = "set_fraction"
ROUTE604.toNode = "l_shoulder_RotationInterpolator_BasicWalk"

Scene14.children.append(ROUTE604)
ROUTE605 = x3d.ROUTE()
ROUTE605.fromField = "fraction_changed"
ROUTE605.fromNode = "Walk_Time"
ROUTE605.toField = "set_fraction"
ROUTE605.toNode = "head_RotationInterpolator_BasicWalk"

Scene14.children.append(ROUTE605)
ROUTE606 = x3d.ROUTE()
ROUTE606.fromField = "fraction_changed"
ROUTE606.fromNode = "Walk_Time"
ROUTE606.toField = "set_fraction"
ROUTE606.toNode = "neck_RotationInterpolator_BasicWalk"

Scene14.children.append(ROUTE606)
ROUTE607 = x3d.ROUTE()
ROUTE607.fromField = "fraction_changed"
ROUTE607.fromNode = "Walk_Time"
ROUTE607.toField = "set_fraction"
ROUTE607.toNode = "upper_body_RotationInterpolator_BasicWalk"

Scene14.children.append(ROUTE607)
ROUTE608 = x3d.ROUTE()
ROUTE608.fromField = "fraction_changed"
ROUTE608.fromNode = "Walk_Time"
ROUTE608.toField = "set_fraction"
ROUTE608.toNode = "whole_body_RotationInterpolator_BasicWalk"

Scene14.children.append(ROUTE608)
ROUTE609 = x3d.ROUTE()
ROUTE609.fromField = "fraction_changed"
ROUTE609.fromNode = "Walk_Time"
ROUTE609.toField = "set_fraction"
ROUTE609.toNode = "whole_body_TranslationInterpolator_BasicWalk"

Scene14.children.append(ROUTE609)
ROUTE610 = x3d.ROUTE()
ROUTE610.fromField = "value_changed"
ROUTE610.fromNode = "r_ankle_RotationInterpolator_BasicWalk"
ROUTE610.toField = "set_rotation"
ROUTE610.toNode = "hanim_r_ankle"

Scene14.children.append(ROUTE610)
ROUTE611 = x3d.ROUTE()
ROUTE611.fromField = "value_changed"
ROUTE611.fromNode = "r_knee_RotationInterpolator_BasicWalk"
ROUTE611.toField = "set_rotation"
ROUTE611.toNode = "hanim_r_knee"

Scene14.children.append(ROUTE611)
ROUTE612 = x3d.ROUTE()
ROUTE612.fromField = "value_changed"
ROUTE612.fromNode = "r_hip_RotationInterpolator_BasicWalk"
ROUTE612.toField = "set_rotation"
ROUTE612.toNode = "hanim_r_hip"

Scene14.children.append(ROUTE612)
ROUTE613 = x3d.ROUTE()
ROUTE613.fromField = "value_changed"
ROUTE613.fromNode = "l_ankle_RotationInterpolator_BasicWalk"
ROUTE613.toField = "set_rotation"
ROUTE613.toNode = "hanim_l_ankle"

Scene14.children.append(ROUTE613)
ROUTE614 = x3d.ROUTE()
ROUTE614.fromField = "value_changed"
ROUTE614.fromNode = "l_knee_RotationInterpolator_BasicWalk"
ROUTE614.toField = "set_rotation"
ROUTE614.toNode = "hanim_l_knee"

Scene14.children.append(ROUTE614)
ROUTE615 = x3d.ROUTE()
ROUTE615.fromField = "value_changed"
ROUTE615.fromNode = "l_hip_RotationInterpolator_BasicWalk"
ROUTE615.toField = "set_rotation"
ROUTE615.toNode = "hanim_l_hip"

Scene14.children.append(ROUTE615)
ROUTE616 = x3d.ROUTE()
ROUTE616.fromField = "value_changed"
ROUTE616.fromNode = "lower_body_RotationInterpolator_BasicWalk"
ROUTE616.toField = "set_rotation"
ROUTE616.toNode = "hanim_sacroiliac"

Scene14.children.append(ROUTE616)
ROUTE617 = x3d.ROUTE()
ROUTE617.fromField = "value_changed"
ROUTE617.fromNode = "r_wrist_RotationInterpolator_BasicWalk"
ROUTE617.toField = "set_rotation"
ROUTE617.toNode = "hanim_r_wrist"

Scene14.children.append(ROUTE617)
ROUTE618 = x3d.ROUTE()
ROUTE618.fromField = "value_changed"
ROUTE618.fromNode = "r_elbow_RotationInterpolator_BasicWalk"
ROUTE618.toField = "set_rotation"
ROUTE618.toNode = "hanim_r_elbow"

Scene14.children.append(ROUTE618)
ROUTE619 = x3d.ROUTE()
ROUTE619.fromField = "value_changed"
ROUTE619.fromNode = "r_shoulder_RotationInterpolator_BasicWalk"
ROUTE619.toField = "set_rotation"
ROUTE619.toNode = "hanim_r_shoulder"

Scene14.children.append(ROUTE619)
ROUTE620 = x3d.ROUTE()
ROUTE620.fromField = "value_changed"
ROUTE620.fromNode = "l_wrist_RotationInterpolator_BasicWalk"
ROUTE620.toField = "set_rotation"
ROUTE620.toNode = "hanim_l_wrist"

Scene14.children.append(ROUTE620)
ROUTE621 = x3d.ROUTE()
ROUTE621.fromField = "value_changed"
ROUTE621.fromNode = "l_elbow_RotationInterpolator_BasicWalk"
ROUTE621.toField = "set_rotation"
ROUTE621.toNode = "hanim_l_elbow"

Scene14.children.append(ROUTE621)
ROUTE622 = x3d.ROUTE()
ROUTE622.fromField = "value_changed"
ROUTE622.fromNode = "l_shoulder_RotationInterpolator_BasicWalk"
ROUTE622.toField = "set_rotation"
ROUTE622.toNode = "hanim_l_shoulder"

Scene14.children.append(ROUTE622)
ROUTE623 = x3d.ROUTE()
ROUTE623.fromField = "value_changed"
ROUTE623.fromNode = "head_RotationInterpolator_BasicWalk"
ROUTE623.toField = "set_rotation"
ROUTE623.toNode = "hanim_skullbase"

Scene14.children.append(ROUTE623)
ROUTE624 = x3d.ROUTE()
ROUTE624.fromField = "value_changed"
ROUTE624.fromNode = "neck_RotationInterpolator_BasicWalk"
ROUTE624.toField = "set_rotation"
ROUTE624.toNode = "hanim_vc4"

Scene14.children.append(ROUTE624)
ROUTE625 = x3d.ROUTE()
ROUTE625.fromField = "value_changed"
ROUTE625.fromNode = "upper_body_RotationInterpolator_BasicWalk"
ROUTE625.toField = "set_rotation"
ROUTE625.toNode = "hanim_vl1"

Scene14.children.append(ROUTE625)
ROUTE626 = x3d.ROUTE()
ROUTE626.fromField = "value_changed"
ROUTE626.fromNode = "whole_body_RotationInterpolator_BasicWalk"
ROUTE626.toField = "set_rotation"
ROUTE626.toNode = "hanim_humanoid_root"

Scene14.children.append(ROUTE626)
ROUTE627 = x3d.ROUTE()
ROUTE627.fromField = "value_changed"
ROUTE627.fromNode = "whole_body_TranslationInterpolator_BasicWalk"
ROUTE627.toField = "set_translation"
ROUTE627.toNode = "hanim_humanoid_root"

Scene14.children.append(ROUTE627)
ROUTE628 = x3d.ROUTE()
ROUTE628.fromField = "fraction_changed"
ROUTE628.fromNode = "Run_Time"
ROUTE628.toField = "set_fraction"
ROUTE628.toNode = "r_ankle_RotationInterpolator_Run"

Scene14.children.append(ROUTE628)
ROUTE629 = x3d.ROUTE()
ROUTE629.fromField = "fraction_changed"
ROUTE629.fromNode = "Run_Time"
ROUTE629.toField = "set_fraction"
ROUTE629.toNode = "r_knee_RotationInterpolator_Run"

Scene14.children.append(ROUTE629)
ROUTE630 = x3d.ROUTE()
ROUTE630.fromField = "fraction_changed"
ROUTE630.fromNode = "Run_Time"
ROUTE630.toField = "set_fraction"
ROUTE630.toNode = "r_hip_RotationInterpolator_Run"

Scene14.children.append(ROUTE630)
ROUTE631 = x3d.ROUTE()
ROUTE631.fromField = "fraction_changed"
ROUTE631.fromNode = "Run_Time"
ROUTE631.toField = "set_fraction"
ROUTE631.toNode = "l_ankle_RotationInterpolator_Run"

Scene14.children.append(ROUTE631)
ROUTE632 = x3d.ROUTE()
ROUTE632.fromField = "fraction_changed"
ROUTE632.fromNode = "Run_Time"
ROUTE632.toField = "set_fraction"
ROUTE632.toNode = "l_knee_RotationInterpolator_Run"

Scene14.children.append(ROUTE632)
ROUTE633 = x3d.ROUTE()
ROUTE633.fromField = "fraction_changed"
ROUTE633.fromNode = "Run_Time"
ROUTE633.toField = "set_fraction"
ROUTE633.toNode = "l_hip_RotationInterpolator_Run"

Scene14.children.append(ROUTE633)
ROUTE634 = x3d.ROUTE()
ROUTE634.fromField = "fraction_changed"
ROUTE634.fromNode = "Run_Time"
ROUTE634.toField = "set_fraction"
ROUTE634.toNode = "lower_body_RotationInterpolator_Run"

Scene14.children.append(ROUTE634)
ROUTE635 = x3d.ROUTE()
ROUTE635.fromField = "fraction_changed"
ROUTE635.fromNode = "Run_Time"
ROUTE635.toField = "set_fraction"
ROUTE635.toNode = "r_wrist_RotationInterpolator_Run"

Scene14.children.append(ROUTE635)
ROUTE636 = x3d.ROUTE()
ROUTE636.fromField = "fraction_changed"
ROUTE636.fromNode = "Run_Time"
ROUTE636.toField = "set_fraction"
ROUTE636.toNode = "r_elbow_RotationInterpolator_Run"

Scene14.children.append(ROUTE636)
ROUTE637 = x3d.ROUTE()
ROUTE637.fromField = "fraction_changed"
ROUTE637.fromNode = "Run_Time"
ROUTE637.toField = "set_fraction"
ROUTE637.toNode = "r_shoulder_RotationInterpolator_Run"

Scene14.children.append(ROUTE637)
ROUTE638 = x3d.ROUTE()
ROUTE638.fromField = "fraction_changed"
ROUTE638.fromNode = "Run_Time"
ROUTE638.toField = "set_fraction"
ROUTE638.toNode = "l_wrist_RotationInterpolator_Run"

Scene14.children.append(ROUTE638)
ROUTE639 = x3d.ROUTE()
ROUTE639.fromField = "fraction_changed"
ROUTE639.fromNode = "Run_Time"
ROUTE639.toField = "set_fraction"
ROUTE639.toNode = "l_elbow_RotationInterpolator_Run"

Scene14.children.append(ROUTE639)
ROUTE640 = x3d.ROUTE()
ROUTE640.fromField = "fraction_changed"
ROUTE640.fromNode = "Run_Time"
ROUTE640.toField = "set_fraction"
ROUTE640.toNode = "l_shoulder_RotationInterpolator_Run"

Scene14.children.append(ROUTE640)
ROUTE641 = x3d.ROUTE()
ROUTE641.fromField = "fraction_changed"
ROUTE641.fromNode = "Run_Time"
ROUTE641.toField = "set_fraction"
ROUTE641.toNode = "head_RotationInterpolator_Run"

Scene14.children.append(ROUTE641)
ROUTE642 = x3d.ROUTE()
ROUTE642.fromField = "fraction_changed"
ROUTE642.fromNode = "Run_Time"
ROUTE642.toField = "set_fraction"
ROUTE642.toNode = "neck_RotationInterpolator_Run"

Scene14.children.append(ROUTE642)
ROUTE643 = x3d.ROUTE()
ROUTE643.fromField = "fraction_changed"
ROUTE643.fromNode = "Run_Time"
ROUTE643.toField = "set_fraction"
ROUTE643.toNode = "upper_body_RotationInterpolator_Run"

Scene14.children.append(ROUTE643)
ROUTE644 = x3d.ROUTE()
ROUTE644.fromField = "fraction_changed"
ROUTE644.fromNode = "Run_Time"
ROUTE644.toField = "set_fraction"
ROUTE644.toNode = "whole_body_RotationInterpolator_Run"

Scene14.children.append(ROUTE644)
ROUTE645 = x3d.ROUTE()
ROUTE645.fromField = "fraction_changed"
ROUTE645.fromNode = "Run_Time"
ROUTE645.toField = "set_fraction"
ROUTE645.toNode = "whole_body_TranslationInterpolator_Run"

Scene14.children.append(ROUTE645)
ROUTE646 = x3d.ROUTE()
ROUTE646.fromField = "value_changed"
ROUTE646.fromNode = "r_ankle_RotationInterpolator_Run"
ROUTE646.toField = "set_rotation"
ROUTE646.toNode = "hanim_r_ankle"

Scene14.children.append(ROUTE646)
ROUTE647 = x3d.ROUTE()
ROUTE647.fromField = "value_changed"
ROUTE647.fromNode = "r_knee_RotationInterpolator_Run"
ROUTE647.toField = "set_rotation"
ROUTE647.toNode = "hanim_r_knee"

Scene14.children.append(ROUTE647)
ROUTE648 = x3d.ROUTE()
ROUTE648.fromField = "value_changed"
ROUTE648.fromNode = "r_hip_RotationInterpolator_Run"
ROUTE648.toField = "set_rotation"
ROUTE648.toNode = "hanim_r_hip"

Scene14.children.append(ROUTE648)
ROUTE649 = x3d.ROUTE()
ROUTE649.fromField = "value_changed"
ROUTE649.fromNode = "l_ankle_RotationInterpolator_Run"
ROUTE649.toField = "set_rotation"
ROUTE649.toNode = "hanim_l_ankle"

Scene14.children.append(ROUTE649)
ROUTE650 = x3d.ROUTE()
ROUTE650.fromField = "value_changed"
ROUTE650.fromNode = "l_knee_RotationInterpolator_Run"
ROUTE650.toField = "set_rotation"
ROUTE650.toNode = "hanim_l_knee"

Scene14.children.append(ROUTE650)
ROUTE651 = x3d.ROUTE()
ROUTE651.fromField = "value_changed"
ROUTE651.fromNode = "l_hip_RotationInterpolator_Run"
ROUTE651.toField = "set_rotation"
ROUTE651.toNode = "hanim_l_hip"

Scene14.children.append(ROUTE651)
ROUTE652 = x3d.ROUTE()
ROUTE652.fromField = "value_changed"
ROUTE652.fromNode = "lower_body_RotationInterpolator_Run"
ROUTE652.toField = "set_rotation"
ROUTE652.toNode = "hanim_sacroiliac"

Scene14.children.append(ROUTE652)
ROUTE653 = x3d.ROUTE()
ROUTE653.fromField = "value_changed"
ROUTE653.fromNode = "r_wrist_RotationInterpolator_Run"
ROUTE653.toField = "set_rotation"
ROUTE653.toNode = "hanim_r_wrist"

Scene14.children.append(ROUTE653)
ROUTE654 = x3d.ROUTE()
ROUTE654.fromField = "value_changed"
ROUTE654.fromNode = "r_elbow_RotationInterpolator_Run"
ROUTE654.toField = "set_rotation"
ROUTE654.toNode = "hanim_r_elbow"

Scene14.children.append(ROUTE654)
ROUTE655 = x3d.ROUTE()
ROUTE655.fromField = "value_changed"
ROUTE655.fromNode = "r_shoulder_RotationInterpolator_Run"
ROUTE655.toField = "set_rotation"
ROUTE655.toNode = "hanim_r_shoulder"

Scene14.children.append(ROUTE655)
ROUTE656 = x3d.ROUTE()
ROUTE656.fromField = "value_changed"
ROUTE656.fromNode = "l_wrist_RotationInterpolator_Run"
ROUTE656.toField = "set_rotation"
ROUTE656.toNode = "hanim_l_wrist"

Scene14.children.append(ROUTE656)
ROUTE657 = x3d.ROUTE()
ROUTE657.fromField = "value_changed"
ROUTE657.fromNode = "l_elbow_RotationInterpolator_Run"
ROUTE657.toField = "set_rotation"
ROUTE657.toNode = "hanim_l_elbow"

Scene14.children.append(ROUTE657)
ROUTE658 = x3d.ROUTE()
ROUTE658.fromField = "value_changed"
ROUTE658.fromNode = "l_shoulder_RotationInterpolator_Run"
ROUTE658.toField = "set_rotation"
ROUTE658.toNode = "hanim_l_shoulder"

Scene14.children.append(ROUTE658)
ROUTE659 = x3d.ROUTE()
ROUTE659.fromField = "value_changed"
ROUTE659.fromNode = "head_RotationInterpolator_Run"
ROUTE659.toField = "set_rotation"
ROUTE659.toNode = "hanim_skullbase"

Scene14.children.append(ROUTE659)
ROUTE660 = x3d.ROUTE()
ROUTE660.fromField = "value_changed"
ROUTE660.fromNode = "neck_RotationInterpolator_Run"
ROUTE660.toField = "set_rotation"
ROUTE660.toNode = "hanim_vc4"

Scene14.children.append(ROUTE660)
ROUTE661 = x3d.ROUTE()
ROUTE661.fromField = "value_changed"
ROUTE661.fromNode = "upper_body_RotationInterpolator_Run"
ROUTE661.toField = "set_rotation"
ROUTE661.toNode = "hanim_vl1"

Scene14.children.append(ROUTE661)
ROUTE662 = x3d.ROUTE()
ROUTE662.fromField = "value_changed"
ROUTE662.fromNode = "whole_body_RotationInterpolator_Run"
ROUTE662.toField = "set_rotation"
ROUTE662.toNode = "hanim_humanoid_root"

Scene14.children.append(ROUTE662)
ROUTE663 = x3d.ROUTE()
ROUTE663.fromField = "value_changed"
ROUTE663.fromNode = "whole_body_TranslationInterpolator_Run"
ROUTE663.toField = "set_translation"
ROUTE663.toNode = "hanim_humanoid_root"

Scene14.children.append(ROUTE663)
ROUTE664 = x3d.ROUTE()
ROUTE664.fromField = "fraction_changed"
ROUTE664.fromNode = "Jump_Time"
ROUTE664.toField = "set_fraction"
ROUTE664.toNode = "r_ankle_RotationInterpolator_Jump"

Scene14.children.append(ROUTE664)
ROUTE665 = x3d.ROUTE()
ROUTE665.fromField = "fraction_changed"
ROUTE665.fromNode = "Jump_Time"
ROUTE665.toField = "set_fraction"
ROUTE665.toNode = "r_knee_RotationInterpolator_Jump"

Scene14.children.append(ROUTE665)
ROUTE666 = x3d.ROUTE()
ROUTE666.fromField = "fraction_changed"
ROUTE666.fromNode = "Jump_Time"
ROUTE666.toField = "set_fraction"
ROUTE666.toNode = "r_hip_RotationInterpolator_Jump"

Scene14.children.append(ROUTE666)
ROUTE667 = x3d.ROUTE()
ROUTE667.fromField = "fraction_changed"
ROUTE667.fromNode = "Jump_Time"
ROUTE667.toField = "set_fraction"
ROUTE667.toNode = "l_ankle_RotationInterpolator_Jump"

Scene14.children.append(ROUTE667)
ROUTE668 = x3d.ROUTE()
ROUTE668.fromField = "fraction_changed"
ROUTE668.fromNode = "Jump_Time"
ROUTE668.toField = "set_fraction"
ROUTE668.toNode = "l_knee_RotationInterpolator_Jump"

Scene14.children.append(ROUTE668)
ROUTE669 = x3d.ROUTE()
ROUTE669.fromField = "fraction_changed"
ROUTE669.fromNode = "Jump_Time"
ROUTE669.toField = "set_fraction"
ROUTE669.toNode = "l_hip_RotationInterpolator_Jump"

Scene14.children.append(ROUTE669)
ROUTE670 = x3d.ROUTE()
ROUTE670.fromField = "fraction_changed"
ROUTE670.fromNode = "Jump_Time"
ROUTE670.toField = "set_fraction"
ROUTE670.toNode = "lower_body_RotationInterpolator_Jump"

Scene14.children.append(ROUTE670)
ROUTE671 = x3d.ROUTE()
ROUTE671.fromField = "fraction_changed"
ROUTE671.fromNode = "Jump_Time"
ROUTE671.toField = "set_fraction"
ROUTE671.toNode = "r_wrist_RotationInterpolator_Jump"

Scene14.children.append(ROUTE671)
ROUTE672 = x3d.ROUTE()
ROUTE672.fromField = "fraction_changed"
ROUTE672.fromNode = "Jump_Time"
ROUTE672.toField = "set_fraction"
ROUTE672.toNode = "r_elbow_RotationInterpolator_Jump"

Scene14.children.append(ROUTE672)
ROUTE673 = x3d.ROUTE()
ROUTE673.fromField = "fraction_changed"
ROUTE673.fromNode = "Jump_Time"
ROUTE673.toField = "set_fraction"
ROUTE673.toNode = "r_shoulder_RotationInterpolator_Jump"

Scene14.children.append(ROUTE673)
ROUTE674 = x3d.ROUTE()
ROUTE674.fromField = "fraction_changed"
ROUTE674.fromNode = "Jump_Time"
ROUTE674.toField = "set_fraction"
ROUTE674.toNode = "l_wrist_RotationInterpolator_Jump"

Scene14.children.append(ROUTE674)
ROUTE675 = x3d.ROUTE()
ROUTE675.fromField = "fraction_changed"
ROUTE675.fromNode = "Jump_Time"
ROUTE675.toField = "set_fraction"
ROUTE675.toNode = "l_elbow_RotationInterpolator_Jump"

Scene14.children.append(ROUTE675)
ROUTE676 = x3d.ROUTE()
ROUTE676.fromField = "fraction_changed"
ROUTE676.fromNode = "Jump_Time"
ROUTE676.toField = "set_fraction"
ROUTE676.toNode = "l_shoulder_RotationInterpolator_Jump"

Scene14.children.append(ROUTE676)
ROUTE677 = x3d.ROUTE()
ROUTE677.fromField = "fraction_changed"
ROUTE677.fromNode = "Jump_Time"
ROUTE677.toField = "set_fraction"
ROUTE677.toNode = "head_RotationInterpolator_Jump"

Scene14.children.append(ROUTE677)
ROUTE678 = x3d.ROUTE()
ROUTE678.fromField = "fraction_changed"
ROUTE678.fromNode = "Jump_Time"
ROUTE678.toField = "set_fraction"
ROUTE678.toNode = "neck_RotationInterpolator_Jump"

Scene14.children.append(ROUTE678)
ROUTE679 = x3d.ROUTE()
ROUTE679.fromField = "fraction_changed"
ROUTE679.fromNode = "Jump_Time"
ROUTE679.toField = "set_fraction"
ROUTE679.toNode = "upper_body_RotationInterpolator_Jump"

Scene14.children.append(ROUTE679)
ROUTE680 = x3d.ROUTE()
ROUTE680.fromField = "fraction_changed"
ROUTE680.fromNode = "Jump_Time"
ROUTE680.toField = "set_fraction"
ROUTE680.toNode = "whole_body_RotationInterpolator_Jump"

Scene14.children.append(ROUTE680)
ROUTE681 = x3d.ROUTE()
ROUTE681.fromField = "fraction_changed"
ROUTE681.fromNode = "Jump_Time"
ROUTE681.toField = "set_fraction"
ROUTE681.toNode = "whole_body_TranslationInterpolator_Jump"

Scene14.children.append(ROUTE681)
ROUTE682 = x3d.ROUTE()
ROUTE682.fromField = "value_changed"
ROUTE682.fromNode = "r_ankle_RotationInterpolator_Jump"
ROUTE682.toField = "set_rotation"
ROUTE682.toNode = "hanim_r_ankle"

Scene14.children.append(ROUTE682)
ROUTE683 = x3d.ROUTE()
ROUTE683.fromField = "value_changed"
ROUTE683.fromNode = "r_knee_RotationInterpolator_Jump"
ROUTE683.toField = "set_rotation"
ROUTE683.toNode = "hanim_r_knee"

Scene14.children.append(ROUTE683)
ROUTE684 = x3d.ROUTE()
ROUTE684.fromField = "value_changed"
ROUTE684.fromNode = "r_hip_RotationInterpolator_Jump"
ROUTE684.toField = "set_rotation"
ROUTE684.toNode = "hanim_r_hip"

Scene14.children.append(ROUTE684)
ROUTE685 = x3d.ROUTE()
ROUTE685.fromField = "value_changed"
ROUTE685.fromNode = "l_ankle_RotationInterpolator_Jump"
ROUTE685.toField = "set_rotation"
ROUTE685.toNode = "hanim_l_ankle"

Scene14.children.append(ROUTE685)
ROUTE686 = x3d.ROUTE()
ROUTE686.fromField = "value_changed"
ROUTE686.fromNode = "l_knee_RotationInterpolator_Jump"
ROUTE686.toField = "set_rotation"
ROUTE686.toNode = "hanim_l_knee"

Scene14.children.append(ROUTE686)
ROUTE687 = x3d.ROUTE()
ROUTE687.fromField = "value_changed"
ROUTE687.fromNode = "l_hip_RotationInterpolator_Jump"
ROUTE687.toField = "set_rotation"
ROUTE687.toNode = "hanim_l_hip"

Scene14.children.append(ROUTE687)
ROUTE688 = x3d.ROUTE()
ROUTE688.fromField = "value_changed"
ROUTE688.fromNode = "lower_body_RotationInterpolator_Jump"
ROUTE688.toField = "set_rotation"
ROUTE688.toNode = "hanim_sacroiliac"

Scene14.children.append(ROUTE688)
ROUTE689 = x3d.ROUTE()
ROUTE689.fromField = "value_changed"
ROUTE689.fromNode = "r_wrist_RotationInterpolator_Jump"
ROUTE689.toField = "set_rotation"
ROUTE689.toNode = "hanim_r_wrist"

Scene14.children.append(ROUTE689)
ROUTE690 = x3d.ROUTE()
ROUTE690.fromField = "value_changed"
ROUTE690.fromNode = "r_elbow_RotationInterpolator_Jump"
ROUTE690.toField = "set_rotation"
ROUTE690.toNode = "hanim_r_elbow"

Scene14.children.append(ROUTE690)
ROUTE691 = x3d.ROUTE()
ROUTE691.fromField = "value_changed"
ROUTE691.fromNode = "r_shoulder_RotationInterpolator_Jump"
ROUTE691.toField = "set_rotation"
ROUTE691.toNode = "hanim_r_shoulder"

Scene14.children.append(ROUTE691)
ROUTE692 = x3d.ROUTE()
ROUTE692.fromField = "value_changed"
ROUTE692.fromNode = "l_wrist_RotationInterpolator_Jump"
ROUTE692.toField = "set_rotation"
ROUTE692.toNode = "hanim_l_wrist"

Scene14.children.append(ROUTE692)
ROUTE693 = x3d.ROUTE()
ROUTE693.fromField = "value_changed"
ROUTE693.fromNode = "l_elbow_RotationInterpolator_Jump"
ROUTE693.toField = "set_rotation"
ROUTE693.toNode = "hanim_l_elbow"

Scene14.children.append(ROUTE693)
ROUTE694 = x3d.ROUTE()
ROUTE694.fromField = "value_changed"
ROUTE694.fromNode = "l_shoulder_RotationInterpolator_Jump"
ROUTE694.toField = "set_rotation"
ROUTE694.toNode = "hanim_l_shoulder"

Scene14.children.append(ROUTE694)
ROUTE695 = x3d.ROUTE()
ROUTE695.fromField = "value_changed"
ROUTE695.fromNode = "head_RotationInterpolator_Jump"
ROUTE695.toField = "set_rotation"
ROUTE695.toNode = "hanim_skullbase"

Scene14.children.append(ROUTE695)
ROUTE696 = x3d.ROUTE()
ROUTE696.fromField = "value_changed"
ROUTE696.fromNode = "neck_RotationInterpolator_Jump"
ROUTE696.toField = "set_rotation"
ROUTE696.toNode = "hanim_vc4"

Scene14.children.append(ROUTE696)
ROUTE697 = x3d.ROUTE()
ROUTE697.fromField = "value_changed"
ROUTE697.fromNode = "upper_body_RotationInterpolator_Jump"
ROUTE697.toField = "set_rotation"
ROUTE697.toNode = "hanim_vl1"

Scene14.children.append(ROUTE697)
ROUTE698 = x3d.ROUTE()
ROUTE698.fromField = "value_changed"
ROUTE698.fromNode = "whole_body_RotationInterpolator_Jump"
ROUTE698.toField = "set_rotation"
ROUTE698.toNode = "hanim_humanoid_root"

Scene14.children.append(ROUTE698)
ROUTE699 = x3d.ROUTE()
ROUTE699.fromField = "value_changed"
ROUTE699.fromNode = "whole_body_TranslationInterpolator_Jump"
ROUTE699.toField = "set_translation"
ROUTE699.toNode = "hanim_humanoid_root"

Scene14.children.append(ROUTE699)

X3D0.Scene = Scene14
f = open("././NancyPrototypes_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
