print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Interchange"
X3D0.version = "3.0"
head1 = x3d.head()
meta2 = x3d.meta()
meta2.name = "generator"
meta2.content = "tovrmlx3d, http://castle-engine.sourceforge.net/view3dscene.php#section_converting"

head1.children.append(meta2)
meta3 = x3d.meta()
meta3.name = "source"
meta3.content = "LOA0ExampleSourceInVRML.wrl"

head1.children.append(meta3)

X3D0.head = head1
Scene4 = x3d.Scene()
ProtoDeclare5 = x3d.ProtoDeclare()
ProtoDeclare5.name = "Humanoid"
ProtoInterface6 = x3d.ProtoInterface()
field7 = x3d.field()
field7.name = "center"
field7.accessType = "inputOutput"
field7.type = "SFVec3f"
field7.value = [0,0,0]

ProtoInterface6.field.append(field7)
field8 = x3d.field()
field8.name = "humanoidBody"
field8.accessType = "inputOutput"
field8.type = "MFNode"

ProtoInterface6.field.append(field8)
field9 = x3d.field()
field9.name = "info"
field9.accessType = "inputOutput"
field9.type = "MFString"

ProtoInterface6.field.append(field9)
field10 = x3d.field()
field10.name = "joints"
field10.accessType = "inputOutput"
field10.type = "MFNode"

ProtoInterface6.field.append(field10)
field11 = x3d.field()
field11.name = "name"
field11.accessType = "inputOutput"
field11.type = "SFString"

ProtoInterface6.field.append(field11)
field12 = x3d.field()
field12.name = "rotation"
field12.accessType = "inputOutput"
field12.type = "SFRotation"
field12.value = [0,0,1,0]

ProtoInterface6.field.append(field12)
field13 = x3d.field()
field13.name = "scale"
field13.accessType = "inputOutput"
field13.type = "SFVec3f"
field13.value = [1,1,1]

ProtoInterface6.field.append(field13)
field14 = x3d.field()
field14.name = "scaleOrientation"
field14.accessType = "inputOutput"
field14.type = "SFRotation"
field14.value = [0,0,1,0]

ProtoInterface6.field.append(field14)
field15 = x3d.field()
field15.name = "segments"
field15.accessType = "inputOutput"
field15.type = "MFNode"

ProtoInterface6.field.append(field15)
field16 = x3d.field()
field16.name = "sites"
field16.accessType = "inputOutput"
field16.type = "MFNode"

ProtoInterface6.field.append(field16)
field17 = x3d.field()
field17.name = "translation"
field17.accessType = "inputOutput"
field17.type = "SFVec3f"
field17.value = [0,0,0]

ProtoInterface6.field.append(field17)
field18 = x3d.field()
field18.name = "version"
field18.accessType = "inputOutput"
field18.type = "SFString"
field18.value = "200x"

ProtoInterface6.field.append(field18)
field19 = x3d.field()
field19.name = "viewpoints"
field19.accessType = "inputOutput"
field19.type = "MFNode"

ProtoInterface6.field.append(field19)
field20 = x3d.field()
field20.name = "bboxCenter"
field20.accessType = "initializeOnly"
field20.type = "SFVec3f"
field20.value = [0,0,0]

ProtoInterface6.field.append(field20)
field21 = x3d.field()
field21.name = "bboxSize"
field21.accessType = "initializeOnly"
field21.type = "SFVec3f"
field21.value = [-1,-1,-1]

ProtoInterface6.field.append(field21)

ProtoDeclare5.ProtoInterface = ProtoInterface6
ProtoBody22 = x3d.ProtoBody()
Transform23 = x3d.Transform()
Group24 = x3d.Group()
IS25 = x3d.IS()
connect26 = x3d.connect()
connect26.nodeField = "children"
connect26.protoField = "humanoidBody"

IS25.connect.append(connect26)

Group24.IS = IS25

Transform23.children.append(Group24)
Group27 = x3d.Group()
IS28 = x3d.IS()
connect29 = x3d.connect()
connect29.nodeField = "children"
connect29.protoField = "viewpoints"

IS28.connect.append(connect29)

Group27.IS = IS28

Transform23.children.append(Group27)
IS30 = x3d.IS()
connect31 = x3d.connect()
connect31.nodeField = "center"
connect31.protoField = "center"

IS30.connect.append(connect31)
connect32 = x3d.connect()
connect32.nodeField = "rotation"
connect32.protoField = "rotation"

IS30.connect.append(connect32)
connect33 = x3d.connect()
connect33.nodeField = "scale"
connect33.protoField = "scale"

IS30.connect.append(connect33)
connect34 = x3d.connect()
connect34.nodeField = "scaleOrientation"
connect34.protoField = "scaleOrientation"

IS30.connect.append(connect34)
connect35 = x3d.connect()
connect35.nodeField = "translation"
connect35.protoField = "translation"

IS30.connect.append(connect35)

Transform23.IS = IS30

ProtoBody22.children.append(Transform23)

ProtoDeclare5.ProtoBody = ProtoBody22

Scene4.children.append(ProtoDeclare5)
ProtoDeclare36 = x3d.ProtoDeclare()
ProtoDeclare36.name = "Joint"
ProtoInterface37 = x3d.ProtoInterface()
field38 = x3d.field()
field38.name = "center"
field38.accessType = "inputOutput"
field38.type = "SFVec3f"
field38.value = [0,0,0]

ProtoInterface37.field.append(field38)
field39 = x3d.field()
field39.name = "children"
field39.accessType = "inputOutput"
field39.type = "MFNode"

ProtoInterface37.field.append(field39)
field40 = x3d.field()
field40.name = "limitOrientation"
field40.accessType = "inputOutput"
field40.type = "SFRotation"
field40.value = [0,0,1,0]

ProtoInterface37.field.append(field40)
field41 = x3d.field()
field41.name = "llimit"
field41.accessType = "inputOutput"
field41.type = "MFFloat"

ProtoInterface37.field.append(field41)
field42 = x3d.field()
field42.name = "name"
field42.accessType = "inputOutput"
field42.type = "SFString"

ProtoInterface37.field.append(field42)
field43 = x3d.field()
field43.name = "rotation"
field43.accessType = "inputOutput"
field43.type = "SFRotation"
field43.value = [0,0,1,0]

ProtoInterface37.field.append(field43)
field44 = x3d.field()
field44.name = "scale"
field44.accessType = "inputOutput"
field44.type = "SFVec3f"
field44.value = [1,1,1]

ProtoInterface37.field.append(field44)
field45 = x3d.field()
field45.name = "scaleOrientation"
field45.accessType = "inputOutput"
field45.type = "SFRotation"
field45.value = [0,0,1,0]

ProtoInterface37.field.append(field45)
field46 = x3d.field()
field46.name = "stiffness"
field46.accessType = "inputOutput"
field46.type = "MFFloat"
field46.value = [1,1,1]

ProtoInterface37.field.append(field46)
field47 = x3d.field()
field47.name = "translation"
field47.accessType = "inputOutput"
field47.type = "SFVec3f"
field47.value = [0,0,0]

ProtoInterface37.field.append(field47)
field48 = x3d.field()
field48.name = "ulimit"
field48.accessType = "inputOutput"
field48.type = "MFFloat"

ProtoInterface37.field.append(field48)

ProtoDeclare36.ProtoInterface = ProtoInterface37
ProtoBody49 = x3d.ProtoBody()
Transform50 = x3d.Transform()
IS51 = x3d.IS()
connect52 = x3d.connect()
connect52.nodeField = "children"
connect52.protoField = "children"

IS51.connect.append(connect52)
connect53 = x3d.connect()
connect53.nodeField = "center"
connect53.protoField = "center"

IS51.connect.append(connect53)
connect54 = x3d.connect()
connect54.nodeField = "rotation"
connect54.protoField = "rotation"

IS51.connect.append(connect54)
connect55 = x3d.connect()
connect55.nodeField = "scale"
connect55.protoField = "scale"

IS51.connect.append(connect55)
connect56 = x3d.connect()
connect56.nodeField = "scaleOrientation"
connect56.protoField = "scaleOrientation"

IS51.connect.append(connect56)
connect57 = x3d.connect()
connect57.nodeField = "translation"
connect57.protoField = "translation"

IS51.connect.append(connect57)

Transform50.IS = IS51

ProtoBody49.children.append(Transform50)

ProtoDeclare36.ProtoBody = ProtoBody49

Scene4.children.append(ProtoDeclare36)
ProtoDeclare58 = x3d.ProtoDeclare()
ProtoDeclare58.name = "Segment"
ProtoInterface59 = x3d.ProtoInterface()
field60 = x3d.field()
field60.name = "addChildren"
field60.accessType = "inputOnly"
field60.type = "MFNode"

ProtoInterface59.field.append(field60)
field61 = x3d.field()
field61.name = "removeChildren"
field61.accessType = "inputOnly"
field61.type = "MFNode"

ProtoInterface59.field.append(field61)
field62 = x3d.field()
field62.name = "centerOfMass"
field62.accessType = "inputOutput"
field62.type = "SFVec3f"
field62.value = [0,0,0]

ProtoInterface59.field.append(field62)
field63 = x3d.field()
field63.name = "children"
field63.accessType = "inputOutput"
field63.type = "MFNode"

ProtoInterface59.field.append(field63)
field64 = x3d.field()
field64.name = "coord"
field64.accessType = "inputOutput"
field64.type = "SFNode"
field64.value = 

ProtoInterface59.field.append(field64)
field65 = x3d.field()
field65.name = "displacers"
field65.accessType = "inputOutput"
field65.type = "MFNode"

ProtoInterface59.field.append(field65)
field66 = x3d.field()
field66.name = "name"
field66.accessType = "inputOutput"
field66.type = "SFString"

ProtoInterface59.field.append(field66)
field67 = x3d.field()
field67.name = "mass"
field67.accessType = "inputOutput"
field67.type = "SFFloat"
field67.value = 0

ProtoInterface59.field.append(field67)
field68 = x3d.field()
field68.name = "momentsOfInertia"
field68.accessType = "inputOutput"
field68.type = "SFVec3f"
field68.value = [1,1,1]

ProtoInterface59.field.append(field68)
field69 = x3d.field()
field69.name = "bboxCenter"
field69.accessType = "initializeOnly"
field69.type = "SFVec3f"
field69.value = [0,0,0]

ProtoInterface59.field.append(field69)
field70 = x3d.field()
field70.name = "bboxSize"
field70.accessType = "initializeOnly"
field70.type = "SFVec3f"
field70.value = [-1,-1,-1]

ProtoInterface59.field.append(field70)

ProtoDeclare58.ProtoInterface = ProtoInterface59
ProtoBody71 = x3d.ProtoBody()
Group72 = x3d.Group()
IS73 = x3d.IS()
connect74 = x3d.connect()
connect74.nodeField = "children"
connect74.protoField = "children"

IS73.connect.append(connect74)
connect75 = x3d.connect()
connect75.nodeField = "bboxCenter"
connect75.protoField = "bboxCenter"

IS73.connect.append(connect75)
connect76 = x3d.connect()
connect76.nodeField = "bboxSize"
connect76.protoField = "bboxSize"

IS73.connect.append(connect76)
connect77 = x3d.connect()
connect77.nodeField = "addChildren"
connect77.protoField = "addChildren"

IS73.connect.append(connect77)
connect78 = x3d.connect()
connect78.nodeField = "removeChildren"
connect78.protoField = "removeChildren"

IS73.connect.append(connect78)

Group72.IS = IS73

ProtoBody71.children.append(Group72)

ProtoDeclare58.ProtoBody = ProtoBody71

Scene4.children.append(ProtoDeclare58)
ProtoDeclare79 = x3d.ProtoDeclare()
ProtoDeclare79.name = "Site"
ProtoInterface80 = x3d.ProtoInterface()
field81 = x3d.field()
field81.name = "addChildren"
field81.accessType = "inputOnly"
field81.type = "MFNode"

ProtoInterface80.field.append(field81)
field82 = x3d.field()
field82.name = "removeChildren"
field82.accessType = "inputOnly"
field82.type = "MFNode"

ProtoInterface80.field.append(field82)
field83 = x3d.field()
field83.name = "center"
field83.accessType = "inputOutput"
field83.type = "SFVec3f"
field83.value = [0,0,0]

ProtoInterface80.field.append(field83)
field84 = x3d.field()
field84.name = "children"
field84.accessType = "inputOutput"
field84.type = "MFNode"

ProtoInterface80.field.append(field84)
field85 = x3d.field()
field85.name = "name"
field85.accessType = "inputOutput"
field85.type = "SFString"

ProtoInterface80.field.append(field85)
field86 = x3d.field()
field86.name = "rotation"
field86.accessType = "inputOutput"
field86.type = "SFRotation"
field86.value = [0,0,1,0]

ProtoInterface80.field.append(field86)
field87 = x3d.field()
field87.name = "scale"
field87.accessType = "inputOutput"
field87.type = "SFVec3f"
field87.value = [1,1,1]

ProtoInterface80.field.append(field87)
field88 = x3d.field()
field88.name = "scaleOrientation"
field88.accessType = "inputOutput"
field88.type = "SFRotation"
field88.value = [0,0,1,0]

ProtoInterface80.field.append(field88)
field89 = x3d.field()
field89.name = "translation"
field89.accessType = "inputOutput"
field89.type = "SFVec3f"
field89.value = [0,0,0]

ProtoInterface80.field.append(field89)

ProtoDeclare79.ProtoInterface = ProtoInterface80
ProtoBody90 = x3d.ProtoBody()
Transform91 = x3d.Transform()
IS92 = x3d.IS()
connect93 = x3d.connect()
connect93.nodeField = "children"
connect93.protoField = "children"

IS92.connect.append(connect93)
connect94 = x3d.connect()
connect94.nodeField = "center"
connect94.protoField = "center"

IS92.connect.append(connect94)
connect95 = x3d.connect()
connect95.nodeField = "rotation"
connect95.protoField = "rotation"

IS92.connect.append(connect95)
connect96 = x3d.connect()
connect96.nodeField = "scale"
connect96.protoField = "scale"

IS92.connect.append(connect96)
connect97 = x3d.connect()
connect97.nodeField = "scaleOrientation"
connect97.protoField = "scaleOrientation"

IS92.connect.append(connect97)
connect98 = x3d.connect()
connect98.nodeField = "translation"
connect98.protoField = "translation"

IS92.connect.append(connect98)
connect99 = x3d.connect()
connect99.nodeField = "addChildren"
connect99.protoField = "addChildren"

IS92.connect.append(connect99)
connect100 = x3d.connect()
connect100.nodeField = "removeChildren"
connect100.protoField = "removeChildren"

IS92.connect.append(connect100)

Transform91.IS = IS92

ProtoBody90.children.append(Transform91)

ProtoDeclare79.ProtoBody = ProtoBody90

Scene4.children.append(ProtoDeclare79)
ProtoInstance101 = x3d.ProtoInstance()
ProtoInstance101.name = "Humanoid"
ProtoInstance101.DEF = "humanoid"
fieldValue102 = x3d.fieldValue()
fieldValue102.name = "humanoidBody"
ProtoInstance103 = x3d.ProtoInstance()
ProtoInstance103.name = "Joint"
ProtoInstance103.DEF = "hanim_humanoid_root"
fieldValue104 = x3d.fieldValue()
fieldValue104.name = "stiffness"
fieldValue104.value = "1 1 1"

ProtoInstance103.fieldValue.append(fieldValue104)
fieldValue105 = x3d.fieldValue()
fieldValue105.name = "name"
fieldValue105.value = "humanoid_root"

ProtoInstance103.fieldValue.append(fieldValue105)
fieldValue106 = x3d.fieldValue()
fieldValue106.name = "center"
fieldValue106.value = "0 0.8240000009536743 0.027699999511241913"

ProtoInstance103.fieldValue.append(fieldValue106)
fieldValue107 = x3d.fieldValue()
fieldValue107.name = "children"
ProtoInstance108 = x3d.ProtoInstance()
ProtoInstance108.name = "Segment"
ProtoInstance108.DEF = "hanim_sacrum"
fieldValue109 = x3d.fieldValue()
fieldValue109.name = "name"
fieldValue109.value = "sacrum"

ProtoInstance108.fieldValue.append(fieldValue109)
fieldValue110 = x3d.fieldValue()
fieldValue110.name = "children"
ProtoInstance111 = x3d.ProtoInstance()
ProtoInstance111.name = "Site"
ProtoInstance111.DEF = "hanim_skull_tip"
fieldValue112 = x3d.fieldValue()
fieldValue112.name = "name"
fieldValue112.value = "skull_tip"

ProtoInstance111.fieldValue.append(fieldValue112)
fieldValue113 = x3d.fieldValue()
fieldValue113.name = "translation"
fieldValue113.value = "0.004999999888241291 1.7503999471664429 0.005499999970197678"

ProtoInstance111.fieldValue.append(fieldValue113)

fieldValue110.children.append(ProtoInstance111)
ProtoInstance114 = x3d.ProtoInstance()
ProtoInstance114.name = "Site"
ProtoInstance114.DEF = "hanim_sellion"
fieldValue115 = x3d.fieldValue()
fieldValue115.name = "name"
fieldValue115.value = "sellion"

ProtoInstance114.fieldValue.append(fieldValue115)
fieldValue116 = x3d.fieldValue()
fieldValue116.name = "translation"
fieldValue116.value = "0.005799999926239252 1.631600022315979 0.0851999968290329"

ProtoInstance114.fieldValue.append(fieldValue116)

fieldValue110.children.append(ProtoInstance114)
ProtoInstance117 = x3d.ProtoInstance()
ProtoInstance117.name = "Site"
ProtoInstance117.DEF = "hanim_r_infraorbitale"
fieldValue118 = x3d.fieldValue()
fieldValue118.name = "name"
fieldValue118.value = "r_infraorbitale"

ProtoInstance117.fieldValue.append(fieldValue118)
fieldValue119 = x3d.fieldValue()
fieldValue119.name = "translation"
fieldValue119.value = "-0.02370000071823597 1.6171000003814697 0.07519999891519547"

ProtoInstance117.fieldValue.append(fieldValue119)

fieldValue110.children.append(ProtoInstance117)
ProtoInstance120 = x3d.ProtoInstance()
ProtoInstance120.name = "Site"
ProtoInstance120.DEF = "hanim_l_infraorbitale"
fieldValue121 = x3d.fieldValue()
fieldValue121.name = "name"
fieldValue121.value = "l_infraorbitale"

ProtoInstance120.fieldValue.append(fieldValue121)
fieldValue122 = x3d.fieldValue()
fieldValue122.name = "translation"
fieldValue122.value = "0.0340999998152256 1.6171000003814697 0.07519999891519547"

ProtoInstance120.fieldValue.append(fieldValue122)

fieldValue110.children.append(ProtoInstance120)
ProtoInstance123 = x3d.ProtoInstance()
ProtoInstance123.name = "Site"
ProtoInstance123.DEF = "hanim_supramenton"
fieldValue124 = x3d.fieldValue()
fieldValue124.name = "name"
fieldValue124.value = "supramenton"

ProtoInstance123.fieldValue.append(fieldValue124)
fieldValue125 = x3d.fieldValue()
fieldValue125.name = "translation"
fieldValue125.value = "0.006099999882280827 1.5410000085830688 0.08049999922513962"

ProtoInstance123.fieldValue.append(fieldValue125)

fieldValue110.children.append(ProtoInstance123)
ProtoInstance126 = x3d.ProtoInstance()
ProtoInstance126.name = "Site"
ProtoInstance126.DEF = "hanim_r_tragion"
fieldValue127 = x3d.fieldValue()
fieldValue127.name = "name"
fieldValue127.value = "r_tragion"

ProtoInstance126.fieldValue.append(fieldValue127)
fieldValue128 = x3d.fieldValue()
fieldValue128.name = "translation"
fieldValue128.value = "-0.06459999829530716 1.6346999406814575 0.03020000085234642"

ProtoInstance126.fieldValue.append(fieldValue128)

fieldValue110.children.append(ProtoInstance126)
ProtoInstance129 = x3d.ProtoInstance()
ProtoInstance129.name = "Site"
ProtoInstance129.DEF = "hanim_r_gonion"
fieldValue130 = x3d.fieldValue()
fieldValue130.name = "name"
fieldValue130.value = "r_gonion"

ProtoInstance129.fieldValue.append(fieldValue130)
fieldValue131 = x3d.fieldValue()
fieldValue131.name = "translation"
fieldValue131.value = "-0.052000001072883606 1.552899956703186 0.034699998795986176"

ProtoInstance129.fieldValue.append(fieldValue131)

fieldValue110.children.append(ProtoInstance129)
ProtoInstance132 = x3d.ProtoInstance()
ProtoInstance132.name = "Site"
ProtoInstance132.DEF = "hanim_l_tragion"
fieldValue133 = x3d.fieldValue()
fieldValue133.name = "name"
fieldValue133.value = "l_tragion"

ProtoInstance132.fieldValue.append(fieldValue133)
fieldValue134 = x3d.fieldValue()
fieldValue134.name = "translation"
fieldValue134.value = "0.0738999992609024 1.6347999572753906 0.028200000524520874"

ProtoInstance132.fieldValue.append(fieldValue134)

fieldValue110.children.append(ProtoInstance132)
ProtoInstance135 = x3d.ProtoInstance()
ProtoInstance135.name = "Site"
ProtoInstance135.DEF = "hanim_l_gonion"
fieldValue136 = x3d.fieldValue()
fieldValue136.name = "name"
fieldValue136.value = "l_gonion"

ProtoInstance135.fieldValue.append(fieldValue136)
fieldValue137 = x3d.fieldValue()
fieldValue137.name = "translation"
fieldValue137.value = "0.06310000270605087 1.5529999732971191 0.032999999821186066"

ProtoInstance135.fieldValue.append(fieldValue137)

fieldValue110.children.append(ProtoInstance135)
ProtoInstance138 = x3d.ProtoInstance()
ProtoInstance138.name = "Site"
ProtoInstance138.DEF = "hanim_nuchale"
fieldValue139 = x3d.fieldValue()
fieldValue139.name = "name"
fieldValue139.value = "nuchale"

ProtoInstance138.fieldValue.append(fieldValue139)
fieldValue140 = x3d.fieldValue()
fieldValue140.name = "translation"
fieldValue140.value = "0.0038999998942017555 1.5972000360488892 -0.07959999889135361"

ProtoInstance138.fieldValue.append(fieldValue140)

fieldValue110.children.append(ProtoInstance138)
ProtoInstance141 = x3d.ProtoInstance()
ProtoInstance141.name = "Site"
ProtoInstance141.DEF = "hanim_r_clavicale"
fieldValue142 = x3d.fieldValue()
fieldValue142.name = "name"
fieldValue142.value = "r_clavicale"

ProtoInstance141.fieldValue.append(fieldValue142)
fieldValue143 = x3d.fieldValue()
fieldValue143.name = "translation"
fieldValue143.value = "-0.011500000022351742 1.4943000078201294 0.03999999910593033"

ProtoInstance141.fieldValue.append(fieldValue143)

fieldValue110.children.append(ProtoInstance141)
ProtoInstance144 = x3d.ProtoInstance()
ProtoInstance144.name = "Site"
ProtoInstance144.DEF = "hanim_suprasternale"
fieldValue145 = x3d.fieldValue()
fieldValue145.name = "name"
fieldValue145.value = "suprasternale"

ProtoInstance144.fieldValue.append(fieldValue145)
fieldValue146 = x3d.fieldValue()
fieldValue146.name = "translation"
fieldValue146.value = "0.00839999970048666 1.4714000225067139 0.05510000139474869"

ProtoInstance144.fieldValue.append(fieldValue146)

fieldValue110.children.append(ProtoInstance144)
ProtoInstance147 = x3d.ProtoInstance()
ProtoInstance147.name = "Site"
ProtoInstance147.DEF = "hanim_l_clavicale"
fieldValue148 = x3d.fieldValue()
fieldValue148.name = "name"
fieldValue148.value = "l_clavicale"

ProtoInstance147.fieldValue.append(fieldValue148)
fieldValue149 = x3d.fieldValue()
fieldValue149.name = "translation"
fieldValue149.value = "0.02710000053048134 1.4943000078201294 0.039400000125169754"

ProtoInstance147.fieldValue.append(fieldValue149)

fieldValue110.children.append(ProtoInstance147)
ProtoInstance150 = x3d.ProtoInstance()
ProtoInstance150.name = "Site"
ProtoInstance150.DEF = "hanim_r_thelion"
fieldValue151 = x3d.fieldValue()
fieldValue151.name = "name"
fieldValue151.value = "r_thelion"

ProtoInstance150.fieldValue.append(fieldValue151)
fieldValue152 = x3d.fieldValue()
fieldValue152.name = "translation"
fieldValue152.value = "-0.07360000163316727 1.3385000228881836 0.1216999962925911"

ProtoInstance150.fieldValue.append(fieldValue152)

fieldValue110.children.append(ProtoInstance150)
ProtoInstance153 = x3d.ProtoInstance()
ProtoInstance153.name = "Site"
ProtoInstance153.DEF = "hanim_l_thelion"
fieldValue154 = x3d.fieldValue()
fieldValue154.name = "name"
fieldValue154.value = "l_thelion"

ProtoInstance153.fieldValue.append(fieldValue154)
fieldValue155 = x3d.fieldValue()
fieldValue155.name = "translation"
fieldValue155.value = "0.09179999679327011 1.3381999731063843 0.11919999867677689"

ProtoInstance153.fieldValue.append(fieldValue155)

fieldValue110.children.append(ProtoInstance153)
ProtoInstance156 = x3d.ProtoInstance()
ProtoInstance156.name = "Site"
ProtoInstance156.DEF = "hanim_substernale"
fieldValue157 = x3d.fieldValue()
fieldValue157.name = "name"
fieldValue157.value = "substernale"

ProtoInstance156.fieldValue.append(fieldValue157)
fieldValue158 = x3d.fieldValue()
fieldValue158.name = "translation"
fieldValue158.value = "0.008500000461935997 1.2994999885559082 0.11469999700784683"

ProtoInstance156.fieldValue.append(fieldValue158)

fieldValue110.children.append(ProtoInstance156)
ProtoInstance159 = x3d.ProtoInstance()
ProtoInstance159.name = "Site"
ProtoInstance159.DEF = "hanim_r_rib10"
fieldValue160 = x3d.fieldValue()
fieldValue160.name = "name"
fieldValue160.value = "r_rib10"

ProtoInstance159.fieldValue.append(fieldValue160)
fieldValue161 = x3d.fieldValue()
fieldValue161.name = "translation"
fieldValue161.value = "-0.07109999656677246 1.194100022315979 0.10159999877214432"

ProtoInstance159.fieldValue.append(fieldValue161)

fieldValue110.children.append(ProtoInstance159)
ProtoInstance162 = x3d.ProtoInstance()
ProtoInstance162.name = "Site"
ProtoInstance162.DEF = "hanim_r_asis"
fieldValue163 = x3d.fieldValue()
fieldValue163.name = "name"
fieldValue163.value = "r_asis"

ProtoInstance162.fieldValue.append(fieldValue163)
fieldValue164 = x3d.fieldValue()
fieldValue164.name = "translation"
fieldValue164.value = "-0.08869999647140503 1.0020999908447266 0.1111999973654747"

ProtoInstance162.fieldValue.append(fieldValue164)

fieldValue110.children.append(ProtoInstance162)
ProtoInstance165 = x3d.ProtoInstance()
ProtoInstance165.name = "Site"
ProtoInstance165.DEF = "hanim_l_rib10"
fieldValue166 = x3d.fieldValue()
fieldValue166.name = "name"
fieldValue166.value = "l_rib10"

ProtoInstance165.fieldValue.append(fieldValue166)
fieldValue167 = x3d.fieldValue()
fieldValue167.name = "translation"
fieldValue167.value = "0.08709999918937683 1.1924999952316284 0.09920000284910202"

ProtoInstance165.fieldValue.append(fieldValue167)

fieldValue110.children.append(ProtoInstance165)
ProtoInstance168 = x3d.ProtoInstance()
ProtoInstance168.name = "Site"
ProtoInstance168.DEF = "hanim_l_asis"
fieldValue169 = x3d.fieldValue()
fieldValue169.name = "name"
fieldValue169.value = "l_asis"

ProtoInstance168.fieldValue.append(fieldValue169)
fieldValue170 = x3d.fieldValue()
fieldValue170.name = "translation"
fieldValue170.value = "0.0925000011920929 0.9983000159263611 0.10520000010728836"

ProtoInstance168.fieldValue.append(fieldValue170)

fieldValue110.children.append(ProtoInstance168)
ProtoInstance171 = x3d.ProtoInstance()
ProtoInstance171.name = "Site"
ProtoInstance171.DEF = "hanim_r_iliocristale"
fieldValue172 = x3d.fieldValue()
fieldValue172.name = "name"
fieldValue172.value = "r_iliocristale"

ProtoInstance171.fieldValue.append(fieldValue172)
fieldValue173 = x3d.fieldValue()
fieldValue173.name = "translation"
fieldValue173.value = "-0.1525000035762787 1.0628000497817993 0.0035000001080334187"

ProtoInstance171.fieldValue.append(fieldValue173)

fieldValue110.children.append(ProtoInstance171)
ProtoInstance174 = x3d.ProtoInstance()
ProtoInstance174.name = "Site"
ProtoInstance174.DEF = "hanim_r_trochanterion"
fieldValue175 = x3d.fieldValue()
fieldValue175.name = "name"
fieldValue175.value = "r_trochanterion"

ProtoInstance174.fieldValue.append(fieldValue175)
fieldValue176 = x3d.fieldValue()
fieldValue176.name = "translation"
fieldValue176.value = "-0.1688999980688095 0.8418999910354614 0.03519999980926514"

ProtoInstance174.fieldValue.append(fieldValue176)

fieldValue110.children.append(ProtoInstance174)
ProtoInstance177 = x3d.ProtoInstance()
ProtoInstance177.name = "Site"
ProtoInstance177.DEF = "hanim_l_iliocristale"
fieldValue178 = x3d.fieldValue()
fieldValue178.name = "name"
fieldValue178.value = "l_iliocristale"

ProtoInstance177.fieldValue.append(fieldValue178)
fieldValue179 = x3d.fieldValue()
fieldValue179.name = "translation"
fieldValue179.value = "0.16120000183582306 1.0536999702453613 0.0007999999797903001"

ProtoInstance177.fieldValue.append(fieldValue179)

fieldValue110.children.append(ProtoInstance177)
ProtoInstance180 = x3d.ProtoInstance()
ProtoInstance180.name = "Site"
ProtoInstance180.DEF = "hanim_l_trochanterion"
fieldValue181 = x3d.fieldValue()
fieldValue181.name = "name"
fieldValue181.value = "l_trochanterion"

ProtoInstance180.fieldValue.append(fieldValue181)
fieldValue182 = x3d.fieldValue()
fieldValue182.name = "translation"
fieldValue182.value = "0.16769999265670776 0.8335999846458435 0.030300000682473183"

ProtoInstance180.fieldValue.append(fieldValue182)

fieldValue110.children.append(ProtoInstance180)
ProtoInstance183 = x3d.ProtoInstance()
ProtoInstance183.name = "Site"
ProtoInstance183.DEF = "hanim_cervicale"
fieldValue184 = x3d.fieldValue()
fieldValue184.name = "name"
fieldValue184.value = "cervicale"

ProtoInstance183.fieldValue.append(fieldValue184)
fieldValue185 = x3d.fieldValue()
fieldValue185.name = "translation"
fieldValue185.value = "0.006399999838322401 1.5199999809265137 -0.08150000125169754"

ProtoInstance183.fieldValue.append(fieldValue185)

fieldValue110.children.append(ProtoInstance183)
ProtoInstance186 = x3d.ProtoInstance()
ProtoInstance186.name = "Site"
ProtoInstance186.DEF = "hanim_spine_2_lower_back"
fieldValue187 = x3d.fieldValue()
fieldValue187.name = "name"
fieldValue187.value = "spine_2_lower_back"

ProtoInstance186.fieldValue.append(fieldValue187)
fieldValue188 = x3d.fieldValue()
fieldValue188.name = "translation"
fieldValue188.value = "0.004900000058114529 1.1907999515533447 -0.11129999905824661"

ProtoInstance186.fieldValue.append(fieldValue188)

fieldValue110.children.append(ProtoInstance186)
ProtoInstance189 = x3d.ProtoInstance()
ProtoInstance189.name = "Site"
ProtoInstance189.DEF = "hanim_r_psis"
fieldValue190 = x3d.fieldValue()
fieldValue190.name = "name"
fieldValue190.value = "r_psis"

ProtoInstance189.fieldValue.append(fieldValue190)
fieldValue191 = x3d.fieldValue()
fieldValue191.name = "translation"
fieldValue191.value = "-0.07159999758005142 1.0190000534057617 -0.11379999667406082"

ProtoInstance189.fieldValue.append(fieldValue191)

fieldValue110.children.append(ProtoInstance189)
ProtoInstance192 = x3d.ProtoInstance()
ProtoInstance192.name = "Site"
ProtoInstance192.DEF = "hanim_l_psis"
fieldValue193 = x3d.fieldValue()
fieldValue193.name = "name"
fieldValue193.value = "l_psis"

ProtoInstance192.fieldValue.append(fieldValue193)
fieldValue194 = x3d.fieldValue()
fieldValue194.name = "translation"
fieldValue194.value = "0.07739999890327454 1.0190000534057617 -0.11509999632835388"

ProtoInstance192.fieldValue.append(fieldValue194)

fieldValue110.children.append(ProtoInstance192)
ProtoInstance195 = x3d.ProtoInstance()
ProtoInstance195.name = "Site"
ProtoInstance195.DEF = "hanim_waist_preferred_posterior"
fieldValue196 = x3d.fieldValue()
fieldValue196.name = "name"
fieldValue196.value = "waist_preferred_posterior"

ProtoInstance195.fieldValue.append(fieldValue196)
fieldValue197 = x3d.fieldValue()
fieldValue197.name = "translation"
fieldValue197.value = "0.28999999165534973 1.0915000438690186 -0.10909999907016754"

ProtoInstance195.fieldValue.append(fieldValue197)

fieldValue110.children.append(ProtoInstance195)
ProtoInstance198 = x3d.ProtoInstance()
ProtoInstance198.name = "Site"
ProtoInstance198.DEF = "hanim_r_acromion"
fieldValue199 = x3d.fieldValue()
fieldValue199.name = "name"
fieldValue199.value = "r_acromion"

ProtoInstance198.fieldValue.append(fieldValue199)
fieldValue200 = x3d.fieldValue()
fieldValue200.name = "translation"
fieldValue200.value = "-0.19050000607967377 1.479099988937378 -0.04309999942779541"

ProtoInstance198.fieldValue.append(fieldValue200)

fieldValue110.children.append(ProtoInstance198)
ProtoInstance201 = x3d.ProtoInstance()
ProtoInstance201.name = "Site"
ProtoInstance201.DEF = "hanim_r_axilla_proximal"
fieldValue202 = x3d.fieldValue()
fieldValue202.name = "name"
fieldValue202.value = "r_axilla_proximal"

ProtoInstance201.fieldValue.append(fieldValue202)
fieldValue203 = x3d.fieldValue()
fieldValue203.name = "translation"
fieldValue203.value = "-0.16259999573230743 1.4071999788284302 -0.003100000089034438"

ProtoInstance201.fieldValue.append(fieldValue203)

fieldValue110.children.append(ProtoInstance201)
ProtoInstance204 = x3d.ProtoInstance()
ProtoInstance204.name = "Site"
ProtoInstance204.DEF = "hanim_r_radial_styloid"
fieldValue205 = x3d.fieldValue()
fieldValue205.name = "name"
fieldValue205.value = "r_radial_styloid"

ProtoInstance204.fieldValue.append(fieldValue205)
fieldValue206 = x3d.fieldValue()
fieldValue206.name = "translation"
fieldValue206.value = "-0.188400000333786 0.8676000237464905 -0.035999998450279236"

ProtoInstance204.fieldValue.append(fieldValue206)

fieldValue110.children.append(ProtoInstance204)
ProtoInstance207 = x3d.ProtoInstance()
ProtoInstance207.name = "Site"
ProtoInstance207.DEF = "hanim_r_axilla_distal"
fieldValue208 = x3d.fieldValue()
fieldValue208.name = "name"
fieldValue208.value = "r_axilla_distal"

ProtoInstance207.fieldValue.append(fieldValue208)
fieldValue209 = x3d.fieldValue()
fieldValue209.name = "translation"
fieldValue209.value = "-0.16030000150203705 1.4098000526428223 -0.08259999752044678"

ProtoInstance207.fieldValue.append(fieldValue209)

fieldValue110.children.append(ProtoInstance207)
ProtoInstance210 = x3d.ProtoInstance()
ProtoInstance210.name = "Site"
ProtoInstance210.DEF = "hanim_r_olecranon"
fieldValue211 = x3d.fieldValue()
fieldValue211.name = "name"
fieldValue211.value = "r_olecranon"

ProtoInstance210.fieldValue.append(fieldValue211)
fieldValue212 = x3d.fieldValue()
fieldValue212.name = "translation"
fieldValue212.value = "-0.1906999945640564 1.1404999494552612 -0.10649999976158142"

ProtoInstance210.fieldValue.append(fieldValue212)

fieldValue110.children.append(ProtoInstance210)
ProtoInstance213 = x3d.ProtoInstance()
ProtoInstance213.name = "Site"
ProtoInstance213.DEF = "hanim_r_humeral_lateral_epicondyles"
fieldValue214 = x3d.fieldValue()
fieldValue214.name = "name"
fieldValue214.value = "r_humeral_lateral_epicondyles"

ProtoInstance213.fieldValue.append(fieldValue214)
fieldValue215 = x3d.fieldValue()
fieldValue215.name = "translation"
fieldValue215.value = "-0.2223999947309494 1.1517000198364258 -0.10329999774694443"

ProtoInstance213.fieldValue.append(fieldValue215)

fieldValue110.children.append(ProtoInstance213)
ProtoInstance216 = x3d.ProtoInstance()
ProtoInstance216.name = "Site"
ProtoInstance216.DEF = "hanim_r_humeral_medial_epicondyles"
fieldValue217 = x3d.fieldValue()
fieldValue217.name = "name"
fieldValue217.value = "r_humeral_medial_epicondyles"

ProtoInstance216.fieldValue.append(fieldValue217)
fieldValue218 = x3d.fieldValue()
fieldValue218.name = "translation"
fieldValue218.value = "-0.1679999977350235 1.1297999620437622 -0.10620000213384628"

ProtoInstance216.fieldValue.append(fieldValue218)

fieldValue110.children.append(ProtoInstance216)
ProtoInstance219 = x3d.ProtoInstance()
ProtoInstance219.name = "Site"
ProtoInstance219.DEF = "hanim_r_radiale"
fieldValue220 = x3d.fieldValue()
fieldValue220.name = "name"
fieldValue220.value = "r_radiale"

ProtoInstance219.fieldValue.append(fieldValue220)
fieldValue221 = x3d.fieldValue()
fieldValue221.name = "translation"
fieldValue221.value = "-0.21299999952316284 1.1304999589920044 -0.10909999907016754"

ProtoInstance219.fieldValue.append(fieldValue221)

fieldValue110.children.append(ProtoInstance219)
ProtoInstance222 = x3d.ProtoInstance()
ProtoInstance222.name = "Site"
ProtoInstance222.DEF = "hanim_r_metacarpal_phalanx_2"
fieldValue223 = x3d.fieldValue()
fieldValue223.name = "name"
fieldValue223.value = "r_metacarpal_phalanx_2"

ProtoInstance222.fieldValue.append(fieldValue223)
fieldValue224 = x3d.fieldValue()
fieldValue224.name = "translation"
fieldValue224.value = "-0.19769999384880066 0.8169000148773193 -0.01769999973475933"

ProtoInstance222.fieldValue.append(fieldValue224)

fieldValue110.children.append(ProtoInstance222)
ProtoInstance225 = x3d.ProtoInstance()
ProtoInstance225.name = "Site"
ProtoInstance225.DEF = "hanim_r_dactylion"
fieldValue226 = x3d.fieldValue()
fieldValue226.name = "name"
fieldValue226.value = "r_dactylion"

ProtoInstance225.fieldValue.append(fieldValue226)
fieldValue227 = x3d.fieldValue()
fieldValue227.name = "translation"
fieldValue227.value = "-0.1941000074148178 0.6772000193595886 -0.04230000078678131"

ProtoInstance225.fieldValue.append(fieldValue227)

fieldValue110.children.append(ProtoInstance225)
ProtoInstance228 = x3d.ProtoInstance()
ProtoInstance228.name = "Site"
ProtoInstance228.DEF = "hanim_r_ulnar_styloid"
fieldValue229 = x3d.fieldValue()
fieldValue229.name = "name"
fieldValue229.value = "r_ulnar_styloid"

ProtoInstance228.fieldValue.append(fieldValue229)
fieldValue230 = x3d.fieldValue()
fieldValue230.name = "translation"
fieldValue230.value = "-0.21170000731945038 0.8561999797821045 -0.058400001376867294"

ProtoInstance228.fieldValue.append(fieldValue230)

fieldValue110.children.append(ProtoInstance228)
ProtoInstance231 = x3d.ProtoInstance()
ProtoInstance231.name = "Site"
ProtoInstance231.DEF = "hanim_r_metacarpal_phalanx_5"
fieldValue232 = x3d.fieldValue()
fieldValue232.name = "name"
fieldValue232.value = "r_metacarpal_phalanx_5"

ProtoInstance231.fieldValue.append(fieldValue232)
fieldValue233 = x3d.fieldValue()
fieldValue233.name = "translation"
fieldValue233.value = "-0.19290000200271606 0.7889999747276306 -0.10639999806880951"

ProtoInstance231.fieldValue.append(fieldValue233)

fieldValue110.children.append(ProtoInstance231)
ProtoInstance234 = x3d.ProtoInstance()
ProtoInstance234.name = "Site"
ProtoInstance234.DEF = "hanim_l_acromion"
fieldValue235 = x3d.fieldValue()
fieldValue235.name = "name"
fieldValue235.value = "l_acromion"

ProtoInstance234.fieldValue.append(fieldValue235)
fieldValue236 = x3d.fieldValue()
fieldValue236.name = "translation"
fieldValue236.value = "0.20319999754428864 1.4759999513626099 -0.04899999871850014"

ProtoInstance234.fieldValue.append(fieldValue236)

fieldValue110.children.append(ProtoInstance234)
ProtoInstance237 = x3d.ProtoInstance()
ProtoInstance237.name = "Site"
ProtoInstance237.DEF = "hanim_l_axilla_proximal"
fieldValue238 = x3d.fieldValue()
fieldValue238.name = "name"
fieldValue238.value = "l_axilla_proximal"

ProtoInstance237.fieldValue.append(fieldValue238)
fieldValue239 = x3d.fieldValue()
fieldValue239.name = "translation"
fieldValue239.value = "0.1776999980211258 1.406499981880188 -0.007499999832361937"

ProtoInstance237.fieldValue.append(fieldValue239)

fieldValue110.children.append(ProtoInstance237)
ProtoInstance240 = x3d.ProtoInstance()
ProtoInstance240.name = "Site"
ProtoInstance240.DEF = "hanim_l_radial_styloid"
fieldValue241 = x3d.fieldValue()
fieldValue241.name = "name"
fieldValue241.value = "l_radial_styloid"

ProtoInstance240.fieldValue.append(fieldValue241)
fieldValue242 = x3d.fieldValue()
fieldValue242.name = "translation"
fieldValue242.value = "0.19009999930858612 0.8644999861717224 -0.04149999842047691"

ProtoInstance240.fieldValue.append(fieldValue242)

fieldValue110.children.append(ProtoInstance240)
ProtoInstance243 = x3d.ProtoInstance()
ProtoInstance243.name = "Site"
ProtoInstance243.DEF = "hanim_l_axilla_distal"
fieldValue244 = x3d.fieldValue()
fieldValue244.name = "name"
fieldValue244.value = "l_axilla_distal"

ProtoInstance243.fieldValue.append(fieldValue244)
fieldValue245 = x3d.fieldValue()
fieldValue245.name = "translation"
fieldValue245.value = "0.17059999704360962 1.4071999788284302 -0.08749999850988388"

ProtoInstance243.fieldValue.append(fieldValue245)

fieldValue110.children.append(ProtoInstance243)
ProtoInstance246 = x3d.ProtoInstance()
ProtoInstance246.name = "Site"
ProtoInstance246.DEF = "hanim_l_olecranon"
fieldValue247 = x3d.fieldValue()
fieldValue247.name = "name"
fieldValue247.value = "l_olecranon"

ProtoInstance246.fieldValue.append(fieldValue247)
fieldValue248 = x3d.fieldValue()
fieldValue248.name = "translation"
fieldValue248.value = "-0.19619999825954437 1.1375000476837158 -0.11230000108480453"

ProtoInstance246.fieldValue.append(fieldValue248)

fieldValue110.children.append(ProtoInstance246)
ProtoInstance249 = x3d.ProtoInstance()
ProtoInstance249.name = "Site"
ProtoInstance249.DEF = "hanim_l_humeral_lateral_epicondyles"
fieldValue250 = x3d.fieldValue()
fieldValue250.name = "name"
fieldValue250.value = "l_humeral_lateral_epicondyles"

ProtoInstance249.fieldValue.append(fieldValue250)
fieldValue251 = x3d.fieldValue()
fieldValue251.name = "translation"
fieldValue251.value = "0.2280000001192093 1.1482000350952148 -0.10999999940395355"

ProtoInstance249.fieldValue.append(fieldValue251)

fieldValue110.children.append(ProtoInstance249)
ProtoInstance252 = x3d.ProtoInstance()
ProtoInstance252.name = "Site"
ProtoInstance252.DEF = "hanim_l_humeral_medial_epicondyles"
fieldValue253 = x3d.fieldValue()
fieldValue253.name = "name"
fieldValue253.value = "l_humeral_medial_epicondyles"

ProtoInstance252.fieldValue.append(fieldValue253)
fieldValue254 = x3d.fieldValue()
fieldValue254.name = "translation"
fieldValue254.value = "0.17350000143051147 1.1272000074386597 -0.11129999905824661"

ProtoInstance252.fieldValue.append(fieldValue254)

fieldValue110.children.append(ProtoInstance252)
ProtoInstance255 = x3d.ProtoInstance()
ProtoInstance255.name = "Site"
ProtoInstance255.DEF = "hanim_l_radiale"
fieldValue256 = x3d.fieldValue()
fieldValue256.name = "name"
fieldValue256.value = "l_radiale"

ProtoInstance255.fieldValue.append(fieldValue256)
fieldValue257 = x3d.fieldValue()
fieldValue257.name = "translation"
fieldValue257.value = "0.21819999814033508 1.1211999654769897 -0.11670000106096268"

ProtoInstance255.fieldValue.append(fieldValue257)

fieldValue110.children.append(ProtoInstance255)
ProtoInstance258 = x3d.ProtoInstance()
ProtoInstance258.name = "Site"
ProtoInstance258.DEF = "hanim_l_metacarpal_phalanx_2"
fieldValue259 = x3d.fieldValue()
fieldValue259.name = "name"
fieldValue259.value = "l_metacarpal_phalanx_2"

ProtoInstance258.fieldValue.append(fieldValue259)
fieldValue260 = x3d.fieldValue()
fieldValue260.name = "translation"
fieldValue260.value = "0.20090000331401825 0.8138999938964844 -0.02370000071823597"

ProtoInstance258.fieldValue.append(fieldValue260)

fieldValue110.children.append(ProtoInstance258)
ProtoInstance261 = x3d.ProtoInstance()
ProtoInstance261.name = "Site"
ProtoInstance261.DEF = "hanim_l_dactylion"
fieldValue262 = x3d.fieldValue()
fieldValue262.name = "name"
fieldValue262.value = "l_dactylion"

ProtoInstance261.fieldValue.append(fieldValue262)
fieldValue263 = x3d.fieldValue()
fieldValue263.name = "translation"
fieldValue263.value = "0.20559999346733093 0.6743000149726868 -0.04820000007748604"

ProtoInstance261.fieldValue.append(fieldValue263)

fieldValue110.children.append(ProtoInstance261)
ProtoInstance264 = x3d.ProtoInstance()
ProtoInstance264.name = "Site"
ProtoInstance264.DEF = "hanim_l_ulnar_styloid"
fieldValue265 = x3d.fieldValue()
fieldValue265.name = "name"
fieldValue265.value = "l_ulnar_styloid"

ProtoInstance264.fieldValue.append(fieldValue265)
fieldValue266 = x3d.fieldValue()
fieldValue266.name = "translation"
fieldValue266.value = "-0.2142000049352646 0.8529000282287598 -0.06480000168085098"

ProtoInstance264.fieldValue.append(fieldValue266)

fieldValue110.children.append(ProtoInstance264)
ProtoInstance267 = x3d.ProtoInstance()
ProtoInstance267.name = "Site"
ProtoInstance267.DEF = "hanim_l_metacarpal_phalanx_5"
fieldValue268 = x3d.fieldValue()
fieldValue268.name = "name"
fieldValue268.value = "l_metacarpal_phalanx_5"

ProtoInstance267.fieldValue.append(fieldValue268)
fieldValue269 = x3d.fieldValue()
fieldValue269.name = "translation"
fieldValue269.value = "0.19290000200271606 0.7860000133514404 -0.11219999939203262"

ProtoInstance267.fieldValue.append(fieldValue269)

fieldValue110.children.append(ProtoInstance267)
ProtoInstance270 = x3d.ProtoInstance()
ProtoInstance270.name = "Site"
ProtoInstance270.DEF = "hanim_r_knee_crease"
fieldValue271 = x3d.fieldValue()
fieldValue271.name = "name"
fieldValue271.value = "r_knee_crease"

ProtoInstance270.fieldValue.append(fieldValue271)
fieldValue272 = x3d.fieldValue()
fieldValue272.name = "translation"
fieldValue272.value = "-0.08250000327825546 0.49320000410079956 -0.032600000500679016"

ProtoInstance270.fieldValue.append(fieldValue272)

fieldValue110.children.append(ProtoInstance270)
ProtoInstance273 = x3d.ProtoInstance()
ProtoInstance273.name = "Site"
ProtoInstance273.DEF = "hanim_r_femoral_lateral_epicondyles"
fieldValue274 = x3d.fieldValue()
fieldValue274.name = "name"
fieldValue274.value = "r_femoral_lateral_epicondyles"

ProtoInstance273.fieldValue.append(fieldValue274)
fieldValue275 = x3d.fieldValue()
fieldValue275.name = "translation"
fieldValue275.value = "-0.1421000063419342 0.4991999864578247 0.03099999949336052"

ProtoInstance273.fieldValue.append(fieldValue275)

fieldValue110.children.append(ProtoInstance273)
ProtoInstance276 = x3d.ProtoInstance()
ProtoInstance276.name = "Site"
ProtoInstance276.DEF = "hanim_r_femoral_medial_epicondyles"
fieldValue277 = x3d.fieldValue()
fieldValue277.name = "name"
fieldValue277.value = "r_femoral_lateral_epicondyles"

ProtoInstance276.fieldValue.append(fieldValue277)
fieldValue278 = x3d.fieldValue()
fieldValue278.name = "translation"
fieldValue278.value = "-0.022099999710917473 0.5013999938964844 0.02889999933540821"

ProtoInstance276.fieldValue.append(fieldValue278)

fieldValue110.children.append(ProtoInstance276)
ProtoInstance279 = x3d.ProtoInstance()
ProtoInstance279.name = "Site"
ProtoInstance279.DEF = "hanim_r_tarsal_interphalangeal_phalanx_5"
fieldValue280 = x3d.fieldValue()
fieldValue280.name = "name"
fieldValue280.value = "r_tarsal_interphalangeal_phalanx_5"

ProtoInstance279.fieldValue.append(fieldValue280)
fieldValue281 = x3d.fieldValue()
fieldValue281.name = "translation"
fieldValue281.value = "-0.15230000019073486 0.016599999740719795 0.08950000256299973"

ProtoInstance279.fieldValue.append(fieldValue281)

fieldValue110.children.append(ProtoInstance279)
ProtoInstance282 = x3d.ProtoInstance()
ProtoInstance282.name = "Site"
ProtoInstance282.DEF = "hanim_r_lateral_malleolus"
fieldValue283 = x3d.fieldValue()
fieldValue283.name = "name"
fieldValue283.value = "r_lateral_malleolus"

ProtoInstance282.fieldValue.append(fieldValue283)
fieldValue284 = x3d.fieldValue()
fieldValue284.name = "translation"
fieldValue284.value = "-0.1005999967455864 0.0658000037074089 -0.10750000178813934"

ProtoInstance282.fieldValue.append(fieldValue284)

fieldValue110.children.append(ProtoInstance282)
ProtoInstance285 = x3d.ProtoInstance()
ProtoInstance285.name = "Site"
ProtoInstance285.DEF = "hanim_r_medial_malleolus"
fieldValue286 = x3d.fieldValue()
fieldValue286.name = "name"
fieldValue286.value = "r_medial_malleolus"

ProtoInstance285.fieldValue.append(fieldValue286)
fieldValue287 = x3d.fieldValue()
fieldValue287.name = "translation"
fieldValue287.value = "-0.05909999832510948 0.07599999755620956 -0.09279999881982803"

ProtoInstance285.fieldValue.append(fieldValue287)

fieldValue110.children.append(ProtoInstance285)
ProtoInstance288 = x3d.ProtoInstance()
ProtoInstance288.name = "Site"
ProtoInstance288.DEF = "hanim_r_sphyrion"
fieldValue289 = x3d.fieldValue()
fieldValue289.name = "name"
fieldValue289.value = "r_sphyrion"

ProtoInstance288.fieldValue.append(fieldValue289)
fieldValue290 = x3d.fieldValue()
fieldValue290.name = "translation"
fieldValue290.value = "-0.06030000001192093 0.061000000685453415 -0.10019999742507935"

ProtoInstance288.fieldValue.append(fieldValue290)

fieldValue110.children.append(ProtoInstance288)
ProtoInstance291 = x3d.ProtoInstance()
ProtoInstance291.name = "Site"
ProtoInstance291.DEF = "hanim_r_tarsal_interphalangeal_phalanx_1"
fieldValue292 = x3d.fieldValue()
fieldValue292.name = "name"
fieldValue292.value = "r_tarsal_interphalangeal_phalanx_1"

ProtoInstance291.fieldValue.append(fieldValue292)
fieldValue293 = x3d.fieldValue()
fieldValue293.name = "translation"
fieldValue293.value = "-0.05209999904036522 0.026000000536441803 0.01269999984651804"

ProtoInstance291.fieldValue.append(fieldValue293)

fieldValue110.children.append(ProtoInstance291)
ProtoInstance294 = x3d.ProtoInstance()
ProtoInstance294.name = "Site"
ProtoInstance294.DEF = "hanim_r_calcaneus_posterior"
fieldValue295 = x3d.fieldValue()
fieldValue295.name = "name"
fieldValue295.value = "r_calcaneus_posterior"

ProtoInstance294.fieldValue.append(fieldValue295)
fieldValue296 = x3d.fieldValue()
fieldValue296.name = "translation"
fieldValue296.value = "-0.06920000165700912 0.02969999983906746 -0.12210000306367874"

ProtoInstance294.fieldValue.append(fieldValue296)

fieldValue110.children.append(ProtoInstance294)
ProtoInstance297 = x3d.ProtoInstance()
ProtoInstance297.name = "Site"
ProtoInstance297.DEF = "hanim_r_tarsal_distal_phalanx_2"
fieldValue298 = x3d.fieldValue()
fieldValue298.name = "name"
fieldValue298.value = "r_tarsal_distal_phalanx_2"

ProtoInstance297.fieldValue.append(fieldValue298)
fieldValue299 = x3d.fieldValue()
fieldValue299.name = "translation"
fieldValue299.value = "-0.08829999715089798 0.013399999588727951 0.13830000162124634"

ProtoInstance297.fieldValue.append(fieldValue299)

fieldValue110.children.append(ProtoInstance297)
ProtoInstance300 = x3d.ProtoInstance()
ProtoInstance300.name = "Site"
ProtoInstance300.DEF = "hanim_l_knee_crease"
fieldValue301 = x3d.fieldValue()
fieldValue301.name = "name"
fieldValue301.value = "l_knee_crease"

ProtoInstance300.fieldValue.append(fieldValue301)
fieldValue302 = x3d.fieldValue()
fieldValue302.name = "translation"
fieldValue302.value = "0.09929999709129333 0.48809999227523804 -0.030899999663233757"

ProtoInstance300.fieldValue.append(fieldValue302)

fieldValue110.children.append(ProtoInstance300)
ProtoInstance303 = x3d.ProtoInstance()
ProtoInstance303.name = "Site"
ProtoInstance303.DEF = "hanim_l_femoral_lateral_epicondyles"
fieldValue304 = x3d.fieldValue()
fieldValue304.name = "name"
fieldValue304.value = "l_femoral_lateral_epicondyles"

ProtoInstance303.fieldValue.append(fieldValue304)
fieldValue305 = x3d.fieldValue()
fieldValue305.name = "translation"
fieldValue305.value = "0.1597999930381775 0.4966999888420105 0.02969999983906746"

ProtoInstance303.fieldValue.append(fieldValue305)

fieldValue110.children.append(ProtoInstance303)
ProtoInstance306 = x3d.ProtoInstance()
ProtoInstance306.name = "Site"
ProtoInstance306.DEF = "hanim_l_femoral_medial_epicondyles"
fieldValue307 = x3d.fieldValue()
fieldValue307.name = "name"
fieldValue307.value = "l_femoral_lateral_epicondyles"

ProtoInstance306.fieldValue.append(fieldValue307)
fieldValue308 = x3d.fieldValue()
fieldValue308.name = "translation"
fieldValue308.value = "0.039799999445676804 0.49459999799728394 0.030300000682473183"

ProtoInstance306.fieldValue.append(fieldValue308)

fieldValue110.children.append(ProtoInstance306)
ProtoInstance309 = x3d.ProtoInstance()
ProtoInstance309.name = "Site"
ProtoInstance309.DEF = "hanim_l_tarsal_interphalangeal_phalanx_5"
fieldValue310 = x3d.fieldValue()
fieldValue310.name = "name"
fieldValue310.value = "l_tarsal_interphalangeal_phalanx_5"

ProtoInstance309.fieldValue.append(fieldValue310)
fieldValue311 = x3d.fieldValue()
fieldValue311.name = "translation"
fieldValue311.value = "0.18250000476837158 0.007000000216066837 0.09279999881982803"

ProtoInstance309.fieldValue.append(fieldValue311)

fieldValue110.children.append(ProtoInstance309)
ProtoInstance312 = x3d.ProtoInstance()
ProtoInstance312.name = "Site"
ProtoInstance312.DEF = "hanim_l_lateral_malleolus"
fieldValue313 = x3d.fieldValue()
fieldValue313.name = "name"
fieldValue313.value = "l_lateral_malleolus"

ProtoInstance312.fieldValue.append(fieldValue313)
fieldValue314 = x3d.fieldValue()
fieldValue314.name = "translation"
fieldValue314.value = "0.13079999387264252 0.059700001031160355 -0.10320000350475311"

ProtoInstance312.fieldValue.append(fieldValue314)

fieldValue110.children.append(ProtoInstance312)
ProtoInstance315 = x3d.ProtoInstance()
ProtoInstance315.name = "Site"
ProtoInstance315.DEF = "hanim_l_medial_malleolus"
fieldValue316 = x3d.fieldValue()
fieldValue316.name = "name"
fieldValue316.value = "l_medial_malleolus"

ProtoInstance315.fieldValue.append(fieldValue316)
fieldValue317 = x3d.fieldValue()
fieldValue317.name = "translation"
fieldValue317.value = "0.08900000154972076 0.07159999758005142 -0.08810000121593475"

ProtoInstance315.fieldValue.append(fieldValue317)

fieldValue110.children.append(ProtoInstance315)
ProtoInstance318 = x3d.ProtoInstance()
ProtoInstance318.name = "Site"
ProtoInstance318.DEF = "hanim_l_sphyrion"
fieldValue319 = x3d.fieldValue()
fieldValue319.name = "name"
fieldValue319.value = "l_sphyrion"

ProtoInstance318.fieldValue.append(fieldValue319)
fieldValue320 = x3d.fieldValue()
fieldValue320.name = "translation"
fieldValue320.value = "0.08900000154972076 0.057500001043081284 -0.09430000185966492"

ProtoInstance318.fieldValue.append(fieldValue320)

fieldValue110.children.append(ProtoInstance318)
ProtoInstance321 = x3d.ProtoInstance()
ProtoInstance321.name = "Site"
ProtoInstance321.DEF = "hanim_l_tarsal_interphalangeal_phalanx_1"
fieldValue322 = x3d.fieldValue()
fieldValue322.name = "name"
fieldValue322.value = "l_tarsal_interphalangeal_phalanx_1"

ProtoInstance321.fieldValue.append(fieldValue322)
fieldValue323 = x3d.fieldValue()
fieldValue323.name = "translation"
fieldValue323.value = "0.08160000294446945 0.02319999970495701 0.010599999688565731"

ProtoInstance321.fieldValue.append(fieldValue323)

fieldValue110.children.append(ProtoInstance321)
ProtoInstance324 = x3d.ProtoInstance()
ProtoInstance324.name = "Site"
ProtoInstance324.DEF = "hanim_l_calcaneus_posterior"
fieldValue325 = x3d.fieldValue()
fieldValue325.name = "name"
fieldValue325.value = "l_calcaneus_posterior"

ProtoInstance324.fieldValue.append(fieldValue325)
fieldValue326 = x3d.fieldValue()
fieldValue326.name = "translation"
fieldValue326.value = "0.09740000218153 0.02590000070631504 -0.11710000038146973"

ProtoInstance324.fieldValue.append(fieldValue326)

fieldValue110.children.append(ProtoInstance324)
ProtoInstance327 = x3d.ProtoInstance()
ProtoInstance327.name = "Site"
ProtoInstance327.DEF = "hanim_l_tarsal_distal_phalanx_2"
fieldValue328 = x3d.fieldValue()
fieldValue328.name = "name"
fieldValue328.value = "l_tarsal_distal_phalanx_2"

ProtoInstance327.fieldValue.append(fieldValue328)
fieldValue329 = x3d.fieldValue()
fieldValue329.name = "translation"
fieldValue329.value = "0.11949999630451202 0.007899999618530273 0.14329999685287476"

ProtoInstance327.fieldValue.append(fieldValue329)

fieldValue110.children.append(ProtoInstance327)
ProtoInstance330 = x3d.ProtoInstance()
ProtoInstance330.name = "Site"
ProtoInstance330.DEF = "hanim_crotch"
fieldValue331 = x3d.fieldValue()
fieldValue331.name = "name"
fieldValue331.value = "crotch"

ProtoInstance330.fieldValue.append(fieldValue331)
fieldValue332 = x3d.fieldValue()
fieldValue332.name = "translation"
fieldValue332.value = "0.0034000000450760126 0.8266000151634216 0.025699999183416367"

ProtoInstance330.fieldValue.append(fieldValue332)

fieldValue110.children.append(ProtoInstance330)
ProtoInstance333 = x3d.ProtoInstance()
ProtoInstance333.name = "Site"
ProtoInstance333.DEF = "hanim_r_neck_base"
fieldValue334 = x3d.fieldValue()
fieldValue334.name = "name"
fieldValue334.value = "r_neck_base"

ProtoInstance333.fieldValue.append(fieldValue334)
fieldValue335 = x3d.fieldValue()
fieldValue335.name = "translation"
fieldValue335.value = "-0.04190000146627426 1.5148999691009521 -0.02199999988079071"

ProtoInstance333.fieldValue.append(fieldValue335)

fieldValue110.children.append(ProtoInstance333)
ProtoInstance336 = x3d.ProtoInstance()
ProtoInstance336.name = "Site"
ProtoInstance336.DEF = "hanim_l_neck_base"
fieldValue337 = x3d.fieldValue()
fieldValue337.name = "name"
fieldValue337.value = "l_neck_base"

ProtoInstance336.fieldValue.append(fieldValue337)
fieldValue338 = x3d.fieldValue()
fieldValue338.name = "translation"
fieldValue338.value = "0.06459999829530716 1.5140999555587769 -0.03799999877810478"

ProtoInstance336.fieldValue.append(fieldValue338)

fieldValue110.children.append(ProtoInstance336)
ProtoInstance339 = x3d.ProtoInstance()
ProtoInstance339.name = "Site"
ProtoInstance339.DEF = "hanim_navel"
fieldValue340 = x3d.fieldValue()
fieldValue340.name = "name"
fieldValue340.value = "navel"

ProtoInstance339.fieldValue.append(fieldValue340)
fieldValue341 = x3d.fieldValue()
fieldValue341.name = "translation"
fieldValue341.value = "0.006899999920278788 1.09660005569458 0.10170000046491623"

ProtoInstance339.fieldValue.append(fieldValue341)

fieldValue110.children.append(ProtoInstance339)

ProtoInstance108.fieldValue.append(fieldValue110)

fieldValue107.children.append(ProtoInstance108)

ProtoInstance103.fieldValue.append(fieldValue107)

fieldValue102.children.append(ProtoInstance103)

ProtoInstance101.fieldValue.append(fieldValue102)
fieldValue342 = x3d.fieldValue()
fieldValue342.name = "joints"
ProtoInstance343 = x3d.ProtoInstance()
ProtoInstance343.name = "Joint"
ProtoInstance343.DEF = "hanim_humanoid_root"
fieldValue344 = x3d.fieldValue()
fieldValue344.name = "stiffness"
fieldValue344.value = "1 1 1"

ProtoInstance343.fieldValue.append(fieldValue344)
fieldValue345 = x3d.fieldValue()
fieldValue345.name = "name"
fieldValue345.value = "humanoid_root"

ProtoInstance343.fieldValue.append(fieldValue345)
fieldValue346 = x3d.fieldValue()
fieldValue346.name = "center"
fieldValue346.value = "0 0.8240000009536743 0.027699999511241913"

ProtoInstance343.fieldValue.append(fieldValue346)
fieldValue347 = x3d.fieldValue()
fieldValue347.name = "children"
ProtoInstance348 = x3d.ProtoInstance()
ProtoInstance348.name = "Segment"
ProtoInstance348.DEF = "hanim_sacrum"
fieldValue349 = x3d.fieldValue()
fieldValue349.name = "name"
fieldValue349.value = "sacrum"

ProtoInstance348.fieldValue.append(fieldValue349)
fieldValue350 = x3d.fieldValue()
fieldValue350.name = "children"
ProtoInstance351 = x3d.ProtoInstance()
ProtoInstance351.name = "Site"
ProtoInstance351.DEF = "hanim_skull_tip"
fieldValue352 = x3d.fieldValue()
fieldValue352.name = "name"
fieldValue352.value = "skull_tip"

ProtoInstance351.fieldValue.append(fieldValue352)
fieldValue353 = x3d.fieldValue()
fieldValue353.name = "translation"
fieldValue353.value = "0.004999999888241291 1.7503999471664429 0.005499999970197678"

ProtoInstance351.fieldValue.append(fieldValue353)

fieldValue350.children.append(ProtoInstance351)
ProtoInstance354 = x3d.ProtoInstance()
ProtoInstance354.name = "Site"
ProtoInstance354.DEF = "hanim_sellion"
fieldValue355 = x3d.fieldValue()
fieldValue355.name = "name"
fieldValue355.value = "sellion"

ProtoInstance354.fieldValue.append(fieldValue355)
fieldValue356 = x3d.fieldValue()
fieldValue356.name = "translation"
fieldValue356.value = "0.005799999926239252 1.631600022315979 0.0851999968290329"

ProtoInstance354.fieldValue.append(fieldValue356)

fieldValue350.children.append(ProtoInstance354)
ProtoInstance357 = x3d.ProtoInstance()
ProtoInstance357.name = "Site"
ProtoInstance357.DEF = "hanim_r_infraorbitale"
fieldValue358 = x3d.fieldValue()
fieldValue358.name = "name"
fieldValue358.value = "r_infraorbitale"

ProtoInstance357.fieldValue.append(fieldValue358)
fieldValue359 = x3d.fieldValue()
fieldValue359.name = "translation"
fieldValue359.value = "-0.02370000071823597 1.6171000003814697 0.07519999891519547"

ProtoInstance357.fieldValue.append(fieldValue359)

fieldValue350.children.append(ProtoInstance357)
ProtoInstance360 = x3d.ProtoInstance()
ProtoInstance360.name = "Site"
ProtoInstance360.DEF = "hanim_l_infraorbitale"
fieldValue361 = x3d.fieldValue()
fieldValue361.name = "name"
fieldValue361.value = "l_infraorbitale"

ProtoInstance360.fieldValue.append(fieldValue361)
fieldValue362 = x3d.fieldValue()
fieldValue362.name = "translation"
fieldValue362.value = "0.0340999998152256 1.6171000003814697 0.07519999891519547"

ProtoInstance360.fieldValue.append(fieldValue362)

fieldValue350.children.append(ProtoInstance360)
ProtoInstance363 = x3d.ProtoInstance()
ProtoInstance363.name = "Site"
ProtoInstance363.DEF = "hanim_supramenton"
fieldValue364 = x3d.fieldValue()
fieldValue364.name = "name"
fieldValue364.value = "supramenton"

ProtoInstance363.fieldValue.append(fieldValue364)
fieldValue365 = x3d.fieldValue()
fieldValue365.name = "translation"
fieldValue365.value = "0.006099999882280827 1.5410000085830688 0.08049999922513962"

ProtoInstance363.fieldValue.append(fieldValue365)

fieldValue350.children.append(ProtoInstance363)
ProtoInstance366 = x3d.ProtoInstance()
ProtoInstance366.name = "Site"
ProtoInstance366.DEF = "hanim_r_tragion"
fieldValue367 = x3d.fieldValue()
fieldValue367.name = "name"
fieldValue367.value = "r_tragion"

ProtoInstance366.fieldValue.append(fieldValue367)
fieldValue368 = x3d.fieldValue()
fieldValue368.name = "translation"
fieldValue368.value = "-0.06459999829530716 1.6346999406814575 0.03020000085234642"

ProtoInstance366.fieldValue.append(fieldValue368)

fieldValue350.children.append(ProtoInstance366)
ProtoInstance369 = x3d.ProtoInstance()
ProtoInstance369.name = "Site"
ProtoInstance369.DEF = "hanim_r_gonion"
fieldValue370 = x3d.fieldValue()
fieldValue370.name = "name"
fieldValue370.value = "r_gonion"

ProtoInstance369.fieldValue.append(fieldValue370)
fieldValue371 = x3d.fieldValue()
fieldValue371.name = "translation"
fieldValue371.value = "-0.052000001072883606 1.552899956703186 0.034699998795986176"

ProtoInstance369.fieldValue.append(fieldValue371)

fieldValue350.children.append(ProtoInstance369)
ProtoInstance372 = x3d.ProtoInstance()
ProtoInstance372.name = "Site"
ProtoInstance372.DEF = "hanim_l_tragion"
fieldValue373 = x3d.fieldValue()
fieldValue373.name = "name"
fieldValue373.value = "l_tragion"

ProtoInstance372.fieldValue.append(fieldValue373)
fieldValue374 = x3d.fieldValue()
fieldValue374.name = "translation"
fieldValue374.value = "0.0738999992609024 1.6347999572753906 0.028200000524520874"

ProtoInstance372.fieldValue.append(fieldValue374)

fieldValue350.children.append(ProtoInstance372)
ProtoInstance375 = x3d.ProtoInstance()
ProtoInstance375.name = "Site"
ProtoInstance375.DEF = "hanim_l_gonion"
fieldValue376 = x3d.fieldValue()
fieldValue376.name = "name"
fieldValue376.value = "l_gonion"

ProtoInstance375.fieldValue.append(fieldValue376)
fieldValue377 = x3d.fieldValue()
fieldValue377.name = "translation"
fieldValue377.value = "0.06310000270605087 1.5529999732971191 0.032999999821186066"

ProtoInstance375.fieldValue.append(fieldValue377)

fieldValue350.children.append(ProtoInstance375)
ProtoInstance378 = x3d.ProtoInstance()
ProtoInstance378.name = "Site"
ProtoInstance378.DEF = "hanim_nuchale"
fieldValue379 = x3d.fieldValue()
fieldValue379.name = "name"
fieldValue379.value = "nuchale"

ProtoInstance378.fieldValue.append(fieldValue379)
fieldValue380 = x3d.fieldValue()
fieldValue380.name = "translation"
fieldValue380.value = "0.0038999998942017555 1.5972000360488892 -0.07959999889135361"

ProtoInstance378.fieldValue.append(fieldValue380)

fieldValue350.children.append(ProtoInstance378)
ProtoInstance381 = x3d.ProtoInstance()
ProtoInstance381.name = "Site"
ProtoInstance381.DEF = "hanim_r_clavicale"
fieldValue382 = x3d.fieldValue()
fieldValue382.name = "name"
fieldValue382.value = "r_clavicale"

ProtoInstance381.fieldValue.append(fieldValue382)
fieldValue383 = x3d.fieldValue()
fieldValue383.name = "translation"
fieldValue383.value = "-0.011500000022351742 1.4943000078201294 0.03999999910593033"

ProtoInstance381.fieldValue.append(fieldValue383)

fieldValue350.children.append(ProtoInstance381)
ProtoInstance384 = x3d.ProtoInstance()
ProtoInstance384.name = "Site"
ProtoInstance384.DEF = "hanim_suprasternale"
fieldValue385 = x3d.fieldValue()
fieldValue385.name = "name"
fieldValue385.value = "suprasternale"

ProtoInstance384.fieldValue.append(fieldValue385)
fieldValue386 = x3d.fieldValue()
fieldValue386.name = "translation"
fieldValue386.value = "0.00839999970048666 1.4714000225067139 0.05510000139474869"

ProtoInstance384.fieldValue.append(fieldValue386)

fieldValue350.children.append(ProtoInstance384)
ProtoInstance387 = x3d.ProtoInstance()
ProtoInstance387.name = "Site"
ProtoInstance387.DEF = "hanim_l_clavicale"
fieldValue388 = x3d.fieldValue()
fieldValue388.name = "name"
fieldValue388.value = "l_clavicale"

ProtoInstance387.fieldValue.append(fieldValue388)
fieldValue389 = x3d.fieldValue()
fieldValue389.name = "translation"
fieldValue389.value = "0.02710000053048134 1.4943000078201294 0.039400000125169754"

ProtoInstance387.fieldValue.append(fieldValue389)

fieldValue350.children.append(ProtoInstance387)
ProtoInstance390 = x3d.ProtoInstance()
ProtoInstance390.name = "Site"
ProtoInstance390.DEF = "hanim_r_thelion"
fieldValue391 = x3d.fieldValue()
fieldValue391.name = "name"
fieldValue391.value = "r_thelion"

ProtoInstance390.fieldValue.append(fieldValue391)
fieldValue392 = x3d.fieldValue()
fieldValue392.name = "translation"
fieldValue392.value = "-0.07360000163316727 1.3385000228881836 0.1216999962925911"

ProtoInstance390.fieldValue.append(fieldValue392)

fieldValue350.children.append(ProtoInstance390)
ProtoInstance393 = x3d.ProtoInstance()
ProtoInstance393.name = "Site"
ProtoInstance393.DEF = "hanim_l_thelion"
fieldValue394 = x3d.fieldValue()
fieldValue394.name = "name"
fieldValue394.value = "l_thelion"

ProtoInstance393.fieldValue.append(fieldValue394)
fieldValue395 = x3d.fieldValue()
fieldValue395.name = "translation"
fieldValue395.value = "0.09179999679327011 1.3381999731063843 0.11919999867677689"

ProtoInstance393.fieldValue.append(fieldValue395)

fieldValue350.children.append(ProtoInstance393)
ProtoInstance396 = x3d.ProtoInstance()
ProtoInstance396.name = "Site"
ProtoInstance396.DEF = "hanim_substernale"
fieldValue397 = x3d.fieldValue()
fieldValue397.name = "name"
fieldValue397.value = "substernale"

ProtoInstance396.fieldValue.append(fieldValue397)
fieldValue398 = x3d.fieldValue()
fieldValue398.name = "translation"
fieldValue398.value = "0.008500000461935997 1.2994999885559082 0.11469999700784683"

ProtoInstance396.fieldValue.append(fieldValue398)

fieldValue350.children.append(ProtoInstance396)
ProtoInstance399 = x3d.ProtoInstance()
ProtoInstance399.name = "Site"
ProtoInstance399.DEF = "hanim_r_rib10"
fieldValue400 = x3d.fieldValue()
fieldValue400.name = "name"
fieldValue400.value = "r_rib10"

ProtoInstance399.fieldValue.append(fieldValue400)
fieldValue401 = x3d.fieldValue()
fieldValue401.name = "translation"
fieldValue401.value = "-0.07109999656677246 1.194100022315979 0.10159999877214432"

ProtoInstance399.fieldValue.append(fieldValue401)

fieldValue350.children.append(ProtoInstance399)
ProtoInstance402 = x3d.ProtoInstance()
ProtoInstance402.name = "Site"
ProtoInstance402.DEF = "hanim_r_asis"
fieldValue403 = x3d.fieldValue()
fieldValue403.name = "name"
fieldValue403.value = "r_asis"

ProtoInstance402.fieldValue.append(fieldValue403)
fieldValue404 = x3d.fieldValue()
fieldValue404.name = "translation"
fieldValue404.value = "-0.08869999647140503 1.0020999908447266 0.1111999973654747"

ProtoInstance402.fieldValue.append(fieldValue404)

fieldValue350.children.append(ProtoInstance402)
ProtoInstance405 = x3d.ProtoInstance()
ProtoInstance405.name = "Site"
ProtoInstance405.DEF = "hanim_l_rib10"
fieldValue406 = x3d.fieldValue()
fieldValue406.name = "name"
fieldValue406.value = "l_rib10"

ProtoInstance405.fieldValue.append(fieldValue406)
fieldValue407 = x3d.fieldValue()
fieldValue407.name = "translation"
fieldValue407.value = "0.08709999918937683 1.1924999952316284 0.09920000284910202"

ProtoInstance405.fieldValue.append(fieldValue407)

fieldValue350.children.append(ProtoInstance405)
ProtoInstance408 = x3d.ProtoInstance()
ProtoInstance408.name = "Site"
ProtoInstance408.DEF = "hanim_l_asis"
fieldValue409 = x3d.fieldValue()
fieldValue409.name = "name"
fieldValue409.value = "l_asis"

ProtoInstance408.fieldValue.append(fieldValue409)
fieldValue410 = x3d.fieldValue()
fieldValue410.name = "translation"
fieldValue410.value = "0.0925000011920929 0.9983000159263611 0.10520000010728836"

ProtoInstance408.fieldValue.append(fieldValue410)

fieldValue350.children.append(ProtoInstance408)
ProtoInstance411 = x3d.ProtoInstance()
ProtoInstance411.name = "Site"
ProtoInstance411.DEF = "hanim_r_iliocristale"
fieldValue412 = x3d.fieldValue()
fieldValue412.name = "name"
fieldValue412.value = "r_iliocristale"

ProtoInstance411.fieldValue.append(fieldValue412)
fieldValue413 = x3d.fieldValue()
fieldValue413.name = "translation"
fieldValue413.value = "-0.1525000035762787 1.0628000497817993 0.0035000001080334187"

ProtoInstance411.fieldValue.append(fieldValue413)

fieldValue350.children.append(ProtoInstance411)
ProtoInstance414 = x3d.ProtoInstance()
ProtoInstance414.name = "Site"
ProtoInstance414.DEF = "hanim_r_trochanterion"
fieldValue415 = x3d.fieldValue()
fieldValue415.name = "name"
fieldValue415.value = "r_trochanterion"

ProtoInstance414.fieldValue.append(fieldValue415)
fieldValue416 = x3d.fieldValue()
fieldValue416.name = "translation"
fieldValue416.value = "-0.1688999980688095 0.8418999910354614 0.03519999980926514"

ProtoInstance414.fieldValue.append(fieldValue416)

fieldValue350.children.append(ProtoInstance414)
ProtoInstance417 = x3d.ProtoInstance()
ProtoInstance417.name = "Site"
ProtoInstance417.DEF = "hanim_l_iliocristale"
fieldValue418 = x3d.fieldValue()
fieldValue418.name = "name"
fieldValue418.value = "l_iliocristale"

ProtoInstance417.fieldValue.append(fieldValue418)
fieldValue419 = x3d.fieldValue()
fieldValue419.name = "translation"
fieldValue419.value = "0.16120000183582306 1.0536999702453613 0.0007999999797903001"

ProtoInstance417.fieldValue.append(fieldValue419)

fieldValue350.children.append(ProtoInstance417)
ProtoInstance420 = x3d.ProtoInstance()
ProtoInstance420.name = "Site"
ProtoInstance420.DEF = "hanim_l_trochanterion"
fieldValue421 = x3d.fieldValue()
fieldValue421.name = "name"
fieldValue421.value = "l_trochanterion"

ProtoInstance420.fieldValue.append(fieldValue421)
fieldValue422 = x3d.fieldValue()
fieldValue422.name = "translation"
fieldValue422.value = "0.16769999265670776 0.8335999846458435 0.030300000682473183"

ProtoInstance420.fieldValue.append(fieldValue422)

fieldValue350.children.append(ProtoInstance420)
ProtoInstance423 = x3d.ProtoInstance()
ProtoInstance423.name = "Site"
ProtoInstance423.DEF = "hanim_cervicale"
fieldValue424 = x3d.fieldValue()
fieldValue424.name = "name"
fieldValue424.value = "cervicale"

ProtoInstance423.fieldValue.append(fieldValue424)
fieldValue425 = x3d.fieldValue()
fieldValue425.name = "translation"
fieldValue425.value = "0.006399999838322401 1.5199999809265137 -0.08150000125169754"

ProtoInstance423.fieldValue.append(fieldValue425)

fieldValue350.children.append(ProtoInstance423)
ProtoInstance426 = x3d.ProtoInstance()
ProtoInstance426.name = "Site"
ProtoInstance426.DEF = "hanim_spine_2_lower_back"
fieldValue427 = x3d.fieldValue()
fieldValue427.name = "name"
fieldValue427.value = "spine_2_lower_back"

ProtoInstance426.fieldValue.append(fieldValue427)
fieldValue428 = x3d.fieldValue()
fieldValue428.name = "translation"
fieldValue428.value = "0.004900000058114529 1.1907999515533447 -0.11129999905824661"

ProtoInstance426.fieldValue.append(fieldValue428)

fieldValue350.children.append(ProtoInstance426)
ProtoInstance429 = x3d.ProtoInstance()
ProtoInstance429.name = "Site"
ProtoInstance429.DEF = "hanim_r_psis"
fieldValue430 = x3d.fieldValue()
fieldValue430.name = "name"
fieldValue430.value = "r_psis"

ProtoInstance429.fieldValue.append(fieldValue430)
fieldValue431 = x3d.fieldValue()
fieldValue431.name = "translation"
fieldValue431.value = "-0.07159999758005142 1.0190000534057617 -0.11379999667406082"

ProtoInstance429.fieldValue.append(fieldValue431)

fieldValue350.children.append(ProtoInstance429)
ProtoInstance432 = x3d.ProtoInstance()
ProtoInstance432.name = "Site"
ProtoInstance432.DEF = "hanim_l_psis"
fieldValue433 = x3d.fieldValue()
fieldValue433.name = "name"
fieldValue433.value = "l_psis"

ProtoInstance432.fieldValue.append(fieldValue433)
fieldValue434 = x3d.fieldValue()
fieldValue434.name = "translation"
fieldValue434.value = "0.07739999890327454 1.0190000534057617 -0.11509999632835388"

ProtoInstance432.fieldValue.append(fieldValue434)

fieldValue350.children.append(ProtoInstance432)
ProtoInstance435 = x3d.ProtoInstance()
ProtoInstance435.name = "Site"
ProtoInstance435.DEF = "hanim_waist_preferred_posterior"
fieldValue436 = x3d.fieldValue()
fieldValue436.name = "name"
fieldValue436.value = "waist_preferred_posterior"

ProtoInstance435.fieldValue.append(fieldValue436)
fieldValue437 = x3d.fieldValue()
fieldValue437.name = "translation"
fieldValue437.value = "0.28999999165534973 1.0915000438690186 -0.10909999907016754"

ProtoInstance435.fieldValue.append(fieldValue437)

fieldValue350.children.append(ProtoInstance435)
ProtoInstance438 = x3d.ProtoInstance()
ProtoInstance438.name = "Site"
ProtoInstance438.DEF = "hanim_r_acromion"
fieldValue439 = x3d.fieldValue()
fieldValue439.name = "name"
fieldValue439.value = "r_acromion"

ProtoInstance438.fieldValue.append(fieldValue439)
fieldValue440 = x3d.fieldValue()
fieldValue440.name = "translation"
fieldValue440.value = "-0.19050000607967377 1.479099988937378 -0.04309999942779541"

ProtoInstance438.fieldValue.append(fieldValue440)

fieldValue350.children.append(ProtoInstance438)
ProtoInstance441 = x3d.ProtoInstance()
ProtoInstance441.name = "Site"
ProtoInstance441.DEF = "hanim_r_axilla_proximal"
fieldValue442 = x3d.fieldValue()
fieldValue442.name = "name"
fieldValue442.value = "r_axilla_proximal"

ProtoInstance441.fieldValue.append(fieldValue442)
fieldValue443 = x3d.fieldValue()
fieldValue443.name = "translation"
fieldValue443.value = "-0.16259999573230743 1.4071999788284302 -0.003100000089034438"

ProtoInstance441.fieldValue.append(fieldValue443)

fieldValue350.children.append(ProtoInstance441)
ProtoInstance444 = x3d.ProtoInstance()
ProtoInstance444.name = "Site"
ProtoInstance444.DEF = "hanim_r_radial_styloid"
fieldValue445 = x3d.fieldValue()
fieldValue445.name = "name"
fieldValue445.value = "r_radial_styloid"

ProtoInstance444.fieldValue.append(fieldValue445)
fieldValue446 = x3d.fieldValue()
fieldValue446.name = "translation"
fieldValue446.value = "-0.188400000333786 0.8676000237464905 -0.035999998450279236"

ProtoInstance444.fieldValue.append(fieldValue446)

fieldValue350.children.append(ProtoInstance444)
ProtoInstance447 = x3d.ProtoInstance()
ProtoInstance447.name = "Site"
ProtoInstance447.DEF = "hanim_r_axilla_distal"
fieldValue448 = x3d.fieldValue()
fieldValue448.name = "name"
fieldValue448.value = "r_axilla_distal"

ProtoInstance447.fieldValue.append(fieldValue448)
fieldValue449 = x3d.fieldValue()
fieldValue449.name = "translation"
fieldValue449.value = "-0.16030000150203705 1.4098000526428223 -0.08259999752044678"

ProtoInstance447.fieldValue.append(fieldValue449)

fieldValue350.children.append(ProtoInstance447)
ProtoInstance450 = x3d.ProtoInstance()
ProtoInstance450.name = "Site"
ProtoInstance450.DEF = "hanim_r_olecranon"
fieldValue451 = x3d.fieldValue()
fieldValue451.name = "name"
fieldValue451.value = "r_olecranon"

ProtoInstance450.fieldValue.append(fieldValue451)
fieldValue452 = x3d.fieldValue()
fieldValue452.name = "translation"
fieldValue452.value = "-0.1906999945640564 1.1404999494552612 -0.10649999976158142"

ProtoInstance450.fieldValue.append(fieldValue452)

fieldValue350.children.append(ProtoInstance450)
ProtoInstance453 = x3d.ProtoInstance()
ProtoInstance453.name = "Site"
ProtoInstance453.DEF = "hanim_r_humeral_lateral_epicondyles"
fieldValue454 = x3d.fieldValue()
fieldValue454.name = "name"
fieldValue454.value = "r_humeral_lateral_epicondyles"

ProtoInstance453.fieldValue.append(fieldValue454)
fieldValue455 = x3d.fieldValue()
fieldValue455.name = "translation"
fieldValue455.value = "-0.2223999947309494 1.1517000198364258 -0.10329999774694443"

ProtoInstance453.fieldValue.append(fieldValue455)

fieldValue350.children.append(ProtoInstance453)
ProtoInstance456 = x3d.ProtoInstance()
ProtoInstance456.name = "Site"
ProtoInstance456.DEF = "hanim_r_humeral_medial_epicondyles"
fieldValue457 = x3d.fieldValue()
fieldValue457.name = "name"
fieldValue457.value = "r_humeral_medial_epicondyles"

ProtoInstance456.fieldValue.append(fieldValue457)
fieldValue458 = x3d.fieldValue()
fieldValue458.name = "translation"
fieldValue458.value = "-0.1679999977350235 1.1297999620437622 -0.10620000213384628"

ProtoInstance456.fieldValue.append(fieldValue458)

fieldValue350.children.append(ProtoInstance456)
ProtoInstance459 = x3d.ProtoInstance()
ProtoInstance459.name = "Site"
ProtoInstance459.DEF = "hanim_r_radiale"
fieldValue460 = x3d.fieldValue()
fieldValue460.name = "name"
fieldValue460.value = "r_radiale"

ProtoInstance459.fieldValue.append(fieldValue460)
fieldValue461 = x3d.fieldValue()
fieldValue461.name = "translation"
fieldValue461.value = "-0.21299999952316284 1.1304999589920044 -0.10909999907016754"

ProtoInstance459.fieldValue.append(fieldValue461)

fieldValue350.children.append(ProtoInstance459)
ProtoInstance462 = x3d.ProtoInstance()
ProtoInstance462.name = "Site"
ProtoInstance462.DEF = "hanim_r_metacarpal_phalanx_2"
fieldValue463 = x3d.fieldValue()
fieldValue463.name = "name"
fieldValue463.value = "r_metacarpal_phalanx_2"

ProtoInstance462.fieldValue.append(fieldValue463)
fieldValue464 = x3d.fieldValue()
fieldValue464.name = "translation"
fieldValue464.value = "-0.19769999384880066 0.8169000148773193 -0.01769999973475933"

ProtoInstance462.fieldValue.append(fieldValue464)

fieldValue350.children.append(ProtoInstance462)
ProtoInstance465 = x3d.ProtoInstance()
ProtoInstance465.name = "Site"
ProtoInstance465.DEF = "hanim_r_dactylion"
fieldValue466 = x3d.fieldValue()
fieldValue466.name = "name"
fieldValue466.value = "r_dactylion"

ProtoInstance465.fieldValue.append(fieldValue466)
fieldValue467 = x3d.fieldValue()
fieldValue467.name = "translation"
fieldValue467.value = "-0.1941000074148178 0.6772000193595886 -0.04230000078678131"

ProtoInstance465.fieldValue.append(fieldValue467)

fieldValue350.children.append(ProtoInstance465)
ProtoInstance468 = x3d.ProtoInstance()
ProtoInstance468.name = "Site"
ProtoInstance468.DEF = "hanim_r_ulnar_styloid"
fieldValue469 = x3d.fieldValue()
fieldValue469.name = "name"
fieldValue469.value = "r_ulnar_styloid"

ProtoInstance468.fieldValue.append(fieldValue469)
fieldValue470 = x3d.fieldValue()
fieldValue470.name = "translation"
fieldValue470.value = "-0.21170000731945038 0.8561999797821045 -0.058400001376867294"

ProtoInstance468.fieldValue.append(fieldValue470)

fieldValue350.children.append(ProtoInstance468)
ProtoInstance471 = x3d.ProtoInstance()
ProtoInstance471.name = "Site"
ProtoInstance471.DEF = "hanim_r_metacarpal_phalanx_5"
fieldValue472 = x3d.fieldValue()
fieldValue472.name = "name"
fieldValue472.value = "r_metacarpal_phalanx_5"

ProtoInstance471.fieldValue.append(fieldValue472)
fieldValue473 = x3d.fieldValue()
fieldValue473.name = "translation"
fieldValue473.value = "-0.19290000200271606 0.7889999747276306 -0.10639999806880951"

ProtoInstance471.fieldValue.append(fieldValue473)

fieldValue350.children.append(ProtoInstance471)
ProtoInstance474 = x3d.ProtoInstance()
ProtoInstance474.name = "Site"
ProtoInstance474.DEF = "hanim_l_acromion"
fieldValue475 = x3d.fieldValue()
fieldValue475.name = "name"
fieldValue475.value = "l_acromion"

ProtoInstance474.fieldValue.append(fieldValue475)
fieldValue476 = x3d.fieldValue()
fieldValue476.name = "translation"
fieldValue476.value = "0.20319999754428864 1.4759999513626099 -0.04899999871850014"

ProtoInstance474.fieldValue.append(fieldValue476)

fieldValue350.children.append(ProtoInstance474)
ProtoInstance477 = x3d.ProtoInstance()
ProtoInstance477.name = "Site"
ProtoInstance477.DEF = "hanim_l_axilla_proximal"
fieldValue478 = x3d.fieldValue()
fieldValue478.name = "name"
fieldValue478.value = "l_axilla_proximal"

ProtoInstance477.fieldValue.append(fieldValue478)
fieldValue479 = x3d.fieldValue()
fieldValue479.name = "translation"
fieldValue479.value = "0.1776999980211258 1.406499981880188 -0.007499999832361937"

ProtoInstance477.fieldValue.append(fieldValue479)

fieldValue350.children.append(ProtoInstance477)
ProtoInstance480 = x3d.ProtoInstance()
ProtoInstance480.name = "Site"
ProtoInstance480.DEF = "hanim_l_radial_styloid"
fieldValue481 = x3d.fieldValue()
fieldValue481.name = "name"
fieldValue481.value = "l_radial_styloid"

ProtoInstance480.fieldValue.append(fieldValue481)
fieldValue482 = x3d.fieldValue()
fieldValue482.name = "translation"
fieldValue482.value = "0.19009999930858612 0.8644999861717224 -0.04149999842047691"

ProtoInstance480.fieldValue.append(fieldValue482)

fieldValue350.children.append(ProtoInstance480)
ProtoInstance483 = x3d.ProtoInstance()
ProtoInstance483.name = "Site"
ProtoInstance483.DEF = "hanim_l_axilla_distal"
fieldValue484 = x3d.fieldValue()
fieldValue484.name = "name"
fieldValue484.value = "l_axilla_distal"

ProtoInstance483.fieldValue.append(fieldValue484)
fieldValue485 = x3d.fieldValue()
fieldValue485.name = "translation"
fieldValue485.value = "0.17059999704360962 1.4071999788284302 -0.08749999850988388"

ProtoInstance483.fieldValue.append(fieldValue485)

fieldValue350.children.append(ProtoInstance483)
ProtoInstance486 = x3d.ProtoInstance()
ProtoInstance486.name = "Site"
ProtoInstance486.DEF = "hanim_l_olecranon"
fieldValue487 = x3d.fieldValue()
fieldValue487.name = "name"
fieldValue487.value = "l_olecranon"

ProtoInstance486.fieldValue.append(fieldValue487)
fieldValue488 = x3d.fieldValue()
fieldValue488.name = "translation"
fieldValue488.value = "-0.19619999825954437 1.1375000476837158 -0.11230000108480453"

ProtoInstance486.fieldValue.append(fieldValue488)

fieldValue350.children.append(ProtoInstance486)
ProtoInstance489 = x3d.ProtoInstance()
ProtoInstance489.name = "Site"
ProtoInstance489.DEF = "hanim_l_humeral_lateral_epicondyles"
fieldValue490 = x3d.fieldValue()
fieldValue490.name = "name"
fieldValue490.value = "l_humeral_lateral_epicondyles"

ProtoInstance489.fieldValue.append(fieldValue490)
fieldValue491 = x3d.fieldValue()
fieldValue491.name = "translation"
fieldValue491.value = "0.2280000001192093 1.1482000350952148 -0.10999999940395355"

ProtoInstance489.fieldValue.append(fieldValue491)

fieldValue350.children.append(ProtoInstance489)
ProtoInstance492 = x3d.ProtoInstance()
ProtoInstance492.name = "Site"
ProtoInstance492.DEF = "hanim_l_humeral_medial_epicondyles"
fieldValue493 = x3d.fieldValue()
fieldValue493.name = "name"
fieldValue493.value = "l_humeral_medial_epicondyles"

ProtoInstance492.fieldValue.append(fieldValue493)
fieldValue494 = x3d.fieldValue()
fieldValue494.name = "translation"
fieldValue494.value = "0.17350000143051147 1.1272000074386597 -0.11129999905824661"

ProtoInstance492.fieldValue.append(fieldValue494)

fieldValue350.children.append(ProtoInstance492)
ProtoInstance495 = x3d.ProtoInstance()
ProtoInstance495.name = "Site"
ProtoInstance495.DEF = "hanim_l_radiale"
fieldValue496 = x3d.fieldValue()
fieldValue496.name = "name"
fieldValue496.value = "l_radiale"

ProtoInstance495.fieldValue.append(fieldValue496)
fieldValue497 = x3d.fieldValue()
fieldValue497.name = "translation"
fieldValue497.value = "0.21819999814033508 1.1211999654769897 -0.11670000106096268"

ProtoInstance495.fieldValue.append(fieldValue497)

fieldValue350.children.append(ProtoInstance495)
ProtoInstance498 = x3d.ProtoInstance()
ProtoInstance498.name = "Site"
ProtoInstance498.DEF = "hanim_l_metacarpal_phalanx_2"
fieldValue499 = x3d.fieldValue()
fieldValue499.name = "name"
fieldValue499.value = "l_metacarpal_phalanx_2"

ProtoInstance498.fieldValue.append(fieldValue499)
fieldValue500 = x3d.fieldValue()
fieldValue500.name = "translation"
fieldValue500.value = "0.20090000331401825 0.8138999938964844 -0.02370000071823597"

ProtoInstance498.fieldValue.append(fieldValue500)

fieldValue350.children.append(ProtoInstance498)
ProtoInstance501 = x3d.ProtoInstance()
ProtoInstance501.name = "Site"
ProtoInstance501.DEF = "hanim_l_dactylion"
fieldValue502 = x3d.fieldValue()
fieldValue502.name = "name"
fieldValue502.value = "l_dactylion"

ProtoInstance501.fieldValue.append(fieldValue502)
fieldValue503 = x3d.fieldValue()
fieldValue503.name = "translation"
fieldValue503.value = "0.20559999346733093 0.6743000149726868 -0.04820000007748604"

ProtoInstance501.fieldValue.append(fieldValue503)

fieldValue350.children.append(ProtoInstance501)
ProtoInstance504 = x3d.ProtoInstance()
ProtoInstance504.name = "Site"
ProtoInstance504.DEF = "hanim_l_ulnar_styloid"
fieldValue505 = x3d.fieldValue()
fieldValue505.name = "name"
fieldValue505.value = "l_ulnar_styloid"

ProtoInstance504.fieldValue.append(fieldValue505)
fieldValue506 = x3d.fieldValue()
fieldValue506.name = "translation"
fieldValue506.value = "-0.2142000049352646 0.8529000282287598 -0.06480000168085098"

ProtoInstance504.fieldValue.append(fieldValue506)

fieldValue350.children.append(ProtoInstance504)
ProtoInstance507 = x3d.ProtoInstance()
ProtoInstance507.name = "Site"
ProtoInstance507.DEF = "hanim_l_metacarpal_phalanx_5"
fieldValue508 = x3d.fieldValue()
fieldValue508.name = "name"
fieldValue508.value = "l_metacarpal_phalanx_5"

ProtoInstance507.fieldValue.append(fieldValue508)
fieldValue509 = x3d.fieldValue()
fieldValue509.name = "translation"
fieldValue509.value = "0.19290000200271606 0.7860000133514404 -0.11219999939203262"

ProtoInstance507.fieldValue.append(fieldValue509)

fieldValue350.children.append(ProtoInstance507)
ProtoInstance510 = x3d.ProtoInstance()
ProtoInstance510.name = "Site"
ProtoInstance510.DEF = "hanim_r_knee_crease"
fieldValue511 = x3d.fieldValue()
fieldValue511.name = "name"
fieldValue511.value = "r_knee_crease"

ProtoInstance510.fieldValue.append(fieldValue511)
fieldValue512 = x3d.fieldValue()
fieldValue512.name = "translation"
fieldValue512.value = "-0.08250000327825546 0.49320000410079956 -0.032600000500679016"

ProtoInstance510.fieldValue.append(fieldValue512)

fieldValue350.children.append(ProtoInstance510)
ProtoInstance513 = x3d.ProtoInstance()
ProtoInstance513.name = "Site"
ProtoInstance513.DEF = "hanim_r_femoral_lateral_epicondyles"
fieldValue514 = x3d.fieldValue()
fieldValue514.name = "name"
fieldValue514.value = "r_femoral_lateral_epicondyles"

ProtoInstance513.fieldValue.append(fieldValue514)
fieldValue515 = x3d.fieldValue()
fieldValue515.name = "translation"
fieldValue515.value = "-0.1421000063419342 0.4991999864578247 0.03099999949336052"

ProtoInstance513.fieldValue.append(fieldValue515)

fieldValue350.children.append(ProtoInstance513)
ProtoInstance516 = x3d.ProtoInstance()
ProtoInstance516.name = "Site"
ProtoInstance516.DEF = "hanim_r_femoral_medial_epicondyles"
fieldValue517 = x3d.fieldValue()
fieldValue517.name = "name"
fieldValue517.value = "r_femoral_lateral_epicondyles"

ProtoInstance516.fieldValue.append(fieldValue517)
fieldValue518 = x3d.fieldValue()
fieldValue518.name = "translation"
fieldValue518.value = "-0.022099999710917473 0.5013999938964844 0.02889999933540821"

ProtoInstance516.fieldValue.append(fieldValue518)

fieldValue350.children.append(ProtoInstance516)
ProtoInstance519 = x3d.ProtoInstance()
ProtoInstance519.name = "Site"
ProtoInstance519.DEF = "hanim_r_tarsal_interphalangeal_phalanx_5"
fieldValue520 = x3d.fieldValue()
fieldValue520.name = "name"
fieldValue520.value = "r_tarsal_interphalangeal_phalanx_5"

ProtoInstance519.fieldValue.append(fieldValue520)
fieldValue521 = x3d.fieldValue()
fieldValue521.name = "translation"
fieldValue521.value = "-0.15230000019073486 0.016599999740719795 0.08950000256299973"

ProtoInstance519.fieldValue.append(fieldValue521)

fieldValue350.children.append(ProtoInstance519)
ProtoInstance522 = x3d.ProtoInstance()
ProtoInstance522.name = "Site"
ProtoInstance522.DEF = "hanim_r_lateral_malleolus"
fieldValue523 = x3d.fieldValue()
fieldValue523.name = "name"
fieldValue523.value = "r_lateral_malleolus"

ProtoInstance522.fieldValue.append(fieldValue523)
fieldValue524 = x3d.fieldValue()
fieldValue524.name = "translation"
fieldValue524.value = "-0.1005999967455864 0.0658000037074089 -0.10750000178813934"

ProtoInstance522.fieldValue.append(fieldValue524)

fieldValue350.children.append(ProtoInstance522)
ProtoInstance525 = x3d.ProtoInstance()
ProtoInstance525.name = "Site"
ProtoInstance525.DEF = "hanim_r_medial_malleolus"
fieldValue526 = x3d.fieldValue()
fieldValue526.name = "name"
fieldValue526.value = "r_medial_malleolus"

ProtoInstance525.fieldValue.append(fieldValue526)
fieldValue527 = x3d.fieldValue()
fieldValue527.name = "translation"
fieldValue527.value = "-0.05909999832510948 0.07599999755620956 -0.09279999881982803"

ProtoInstance525.fieldValue.append(fieldValue527)

fieldValue350.children.append(ProtoInstance525)
ProtoInstance528 = x3d.ProtoInstance()
ProtoInstance528.name = "Site"
ProtoInstance528.DEF = "hanim_r_sphyrion"
fieldValue529 = x3d.fieldValue()
fieldValue529.name = "name"
fieldValue529.value = "r_sphyrion"

ProtoInstance528.fieldValue.append(fieldValue529)
fieldValue530 = x3d.fieldValue()
fieldValue530.name = "translation"
fieldValue530.value = "-0.06030000001192093 0.061000000685453415 -0.10019999742507935"

ProtoInstance528.fieldValue.append(fieldValue530)

fieldValue350.children.append(ProtoInstance528)
ProtoInstance531 = x3d.ProtoInstance()
ProtoInstance531.name = "Site"
ProtoInstance531.DEF = "hanim_r_tarsal_interphalangeal_phalanx_1"
fieldValue532 = x3d.fieldValue()
fieldValue532.name = "name"
fieldValue532.value = "r_tarsal_interphalangeal_phalanx_1"

ProtoInstance531.fieldValue.append(fieldValue532)
fieldValue533 = x3d.fieldValue()
fieldValue533.name = "translation"
fieldValue533.value = "-0.05209999904036522 0.026000000536441803 0.01269999984651804"

ProtoInstance531.fieldValue.append(fieldValue533)

fieldValue350.children.append(ProtoInstance531)
ProtoInstance534 = x3d.ProtoInstance()
ProtoInstance534.name = "Site"
ProtoInstance534.DEF = "hanim_r_calcaneus_posterior"
fieldValue535 = x3d.fieldValue()
fieldValue535.name = "name"
fieldValue535.value = "r_calcaneus_posterior"

ProtoInstance534.fieldValue.append(fieldValue535)
fieldValue536 = x3d.fieldValue()
fieldValue536.name = "translation"
fieldValue536.value = "-0.06920000165700912 0.02969999983906746 -0.12210000306367874"

ProtoInstance534.fieldValue.append(fieldValue536)

fieldValue350.children.append(ProtoInstance534)
ProtoInstance537 = x3d.ProtoInstance()
ProtoInstance537.name = "Site"
ProtoInstance537.DEF = "hanim_r_tarsal_distal_phalanx_2"
fieldValue538 = x3d.fieldValue()
fieldValue538.name = "name"
fieldValue538.value = "r_tarsal_distal_phalanx_2"

ProtoInstance537.fieldValue.append(fieldValue538)
fieldValue539 = x3d.fieldValue()
fieldValue539.name = "translation"
fieldValue539.value = "-0.08829999715089798 0.013399999588727951 0.13830000162124634"

ProtoInstance537.fieldValue.append(fieldValue539)

fieldValue350.children.append(ProtoInstance537)
ProtoInstance540 = x3d.ProtoInstance()
ProtoInstance540.name = "Site"
ProtoInstance540.DEF = "hanim_l_knee_crease"
fieldValue541 = x3d.fieldValue()
fieldValue541.name = "name"
fieldValue541.value = "l_knee_crease"

ProtoInstance540.fieldValue.append(fieldValue541)
fieldValue542 = x3d.fieldValue()
fieldValue542.name = "translation"
fieldValue542.value = "0.09929999709129333 0.48809999227523804 -0.030899999663233757"

ProtoInstance540.fieldValue.append(fieldValue542)

fieldValue350.children.append(ProtoInstance540)
ProtoInstance543 = x3d.ProtoInstance()
ProtoInstance543.name = "Site"
ProtoInstance543.DEF = "hanim_l_femoral_lateral_epicondyles"
fieldValue544 = x3d.fieldValue()
fieldValue544.name = "name"
fieldValue544.value = "l_femoral_lateral_epicondyles"

ProtoInstance543.fieldValue.append(fieldValue544)
fieldValue545 = x3d.fieldValue()
fieldValue545.name = "translation"
fieldValue545.value = "0.1597999930381775 0.4966999888420105 0.02969999983906746"

ProtoInstance543.fieldValue.append(fieldValue545)

fieldValue350.children.append(ProtoInstance543)
ProtoInstance546 = x3d.ProtoInstance()
ProtoInstance546.name = "Site"
ProtoInstance546.DEF = "hanim_l_femoral_medial_epicondyles"
fieldValue547 = x3d.fieldValue()
fieldValue547.name = "name"
fieldValue547.value = "l_femoral_lateral_epicondyles"

ProtoInstance546.fieldValue.append(fieldValue547)
fieldValue548 = x3d.fieldValue()
fieldValue548.name = "translation"
fieldValue548.value = "0.039799999445676804 0.49459999799728394 0.030300000682473183"

ProtoInstance546.fieldValue.append(fieldValue548)

fieldValue350.children.append(ProtoInstance546)
ProtoInstance549 = x3d.ProtoInstance()
ProtoInstance549.name = "Site"
ProtoInstance549.DEF = "hanim_l_tarsal_interphalangeal_phalanx_5"
fieldValue550 = x3d.fieldValue()
fieldValue550.name = "name"
fieldValue550.value = "l_tarsal_interphalangeal_phalanx_5"

ProtoInstance549.fieldValue.append(fieldValue550)
fieldValue551 = x3d.fieldValue()
fieldValue551.name = "translation"
fieldValue551.value = "0.18250000476837158 0.007000000216066837 0.09279999881982803"

ProtoInstance549.fieldValue.append(fieldValue551)

fieldValue350.children.append(ProtoInstance549)
ProtoInstance552 = x3d.ProtoInstance()
ProtoInstance552.name = "Site"
ProtoInstance552.DEF = "hanim_l_lateral_malleolus"
fieldValue553 = x3d.fieldValue()
fieldValue553.name = "name"
fieldValue553.value = "l_lateral_malleolus"

ProtoInstance552.fieldValue.append(fieldValue553)
fieldValue554 = x3d.fieldValue()
fieldValue554.name = "translation"
fieldValue554.value = "0.13079999387264252 0.059700001031160355 -0.10320000350475311"

ProtoInstance552.fieldValue.append(fieldValue554)

fieldValue350.children.append(ProtoInstance552)
ProtoInstance555 = x3d.ProtoInstance()
ProtoInstance555.name = "Site"
ProtoInstance555.DEF = "hanim_l_medial_malleolus"
fieldValue556 = x3d.fieldValue()
fieldValue556.name = "name"
fieldValue556.value = "l_medial_malleolus"

ProtoInstance555.fieldValue.append(fieldValue556)
fieldValue557 = x3d.fieldValue()
fieldValue557.name = "translation"
fieldValue557.value = "0.08900000154972076 0.07159999758005142 -0.08810000121593475"

ProtoInstance555.fieldValue.append(fieldValue557)

fieldValue350.children.append(ProtoInstance555)
ProtoInstance558 = x3d.ProtoInstance()
ProtoInstance558.name = "Site"
ProtoInstance558.DEF = "hanim_l_sphyrion"
fieldValue559 = x3d.fieldValue()
fieldValue559.name = "name"
fieldValue559.value = "l_sphyrion"

ProtoInstance558.fieldValue.append(fieldValue559)
fieldValue560 = x3d.fieldValue()
fieldValue560.name = "translation"
fieldValue560.value = "0.08900000154972076 0.057500001043081284 -0.09430000185966492"

ProtoInstance558.fieldValue.append(fieldValue560)

fieldValue350.children.append(ProtoInstance558)
ProtoInstance561 = x3d.ProtoInstance()
ProtoInstance561.name = "Site"
ProtoInstance561.DEF = "hanim_l_tarsal_interphalangeal_phalanx_1"
fieldValue562 = x3d.fieldValue()
fieldValue562.name = "name"
fieldValue562.value = "l_tarsal_interphalangeal_phalanx_1"

ProtoInstance561.fieldValue.append(fieldValue562)
fieldValue563 = x3d.fieldValue()
fieldValue563.name = "translation"
fieldValue563.value = "0.08160000294446945 0.02319999970495701 0.010599999688565731"

ProtoInstance561.fieldValue.append(fieldValue563)

fieldValue350.children.append(ProtoInstance561)
ProtoInstance564 = x3d.ProtoInstance()
ProtoInstance564.name = "Site"
ProtoInstance564.DEF = "hanim_l_calcaneus_posterior"
fieldValue565 = x3d.fieldValue()
fieldValue565.name = "name"
fieldValue565.value = "l_calcaneus_posterior"

ProtoInstance564.fieldValue.append(fieldValue565)
fieldValue566 = x3d.fieldValue()
fieldValue566.name = "translation"
fieldValue566.value = "0.09740000218153 0.02590000070631504 -0.11710000038146973"

ProtoInstance564.fieldValue.append(fieldValue566)

fieldValue350.children.append(ProtoInstance564)
ProtoInstance567 = x3d.ProtoInstance()
ProtoInstance567.name = "Site"
ProtoInstance567.DEF = "hanim_l_tarsal_distal_phalanx_2"
fieldValue568 = x3d.fieldValue()
fieldValue568.name = "name"
fieldValue568.value = "l_tarsal_distal_phalanx_2"

ProtoInstance567.fieldValue.append(fieldValue568)
fieldValue569 = x3d.fieldValue()
fieldValue569.name = "translation"
fieldValue569.value = "0.11949999630451202 0.007899999618530273 0.14329999685287476"

ProtoInstance567.fieldValue.append(fieldValue569)

fieldValue350.children.append(ProtoInstance567)
ProtoInstance570 = x3d.ProtoInstance()
ProtoInstance570.name = "Site"
ProtoInstance570.DEF = "hanim_crotch"
fieldValue571 = x3d.fieldValue()
fieldValue571.name = "name"
fieldValue571.value = "crotch"

ProtoInstance570.fieldValue.append(fieldValue571)
fieldValue572 = x3d.fieldValue()
fieldValue572.name = "translation"
fieldValue572.value = "0.0034000000450760126 0.8266000151634216 0.025699999183416367"

ProtoInstance570.fieldValue.append(fieldValue572)

fieldValue350.children.append(ProtoInstance570)
ProtoInstance573 = x3d.ProtoInstance()
ProtoInstance573.name = "Site"
ProtoInstance573.DEF = "hanim_r_neck_base"
fieldValue574 = x3d.fieldValue()
fieldValue574.name = "name"
fieldValue574.value = "r_neck_base"

ProtoInstance573.fieldValue.append(fieldValue574)
fieldValue575 = x3d.fieldValue()
fieldValue575.name = "translation"
fieldValue575.value = "-0.04190000146627426 1.5148999691009521 -0.02199999988079071"

ProtoInstance573.fieldValue.append(fieldValue575)

fieldValue350.children.append(ProtoInstance573)
ProtoInstance576 = x3d.ProtoInstance()
ProtoInstance576.name = "Site"
ProtoInstance576.DEF = "hanim_l_neck_base"
fieldValue577 = x3d.fieldValue()
fieldValue577.name = "name"
fieldValue577.value = "l_neck_base"

ProtoInstance576.fieldValue.append(fieldValue577)
fieldValue578 = x3d.fieldValue()
fieldValue578.name = "translation"
fieldValue578.value = "0.06459999829530716 1.5140999555587769 -0.03799999877810478"

ProtoInstance576.fieldValue.append(fieldValue578)

fieldValue350.children.append(ProtoInstance576)
ProtoInstance579 = x3d.ProtoInstance()
ProtoInstance579.name = "Site"
ProtoInstance579.DEF = "hanim_navel"
fieldValue580 = x3d.fieldValue()
fieldValue580.name = "name"
fieldValue580.value = "navel"

ProtoInstance579.fieldValue.append(fieldValue580)
fieldValue581 = x3d.fieldValue()
fieldValue581.name = "translation"
fieldValue581.value = "0.006899999920278788 1.09660005569458 0.10170000046491623"

ProtoInstance579.fieldValue.append(fieldValue581)

fieldValue350.children.append(ProtoInstance579)

ProtoInstance348.fieldValue.append(fieldValue350)

fieldValue347.children.append(ProtoInstance348)

ProtoInstance343.fieldValue.append(fieldValue347)

fieldValue342.children.append(ProtoInstance343)

ProtoInstance101.fieldValue.append(fieldValue342)
fieldValue582 = x3d.fieldValue()
fieldValue582.name = "segments"
ProtoInstance583 = x3d.ProtoInstance()
ProtoInstance583.name = "Segment"
ProtoInstance583.DEF = "hanim_sacrum"
fieldValue584 = x3d.fieldValue()
fieldValue584.name = "name"
fieldValue584.value = "sacrum"

ProtoInstance583.fieldValue.append(fieldValue584)
fieldValue585 = x3d.fieldValue()
fieldValue585.name = "children"
ProtoInstance586 = x3d.ProtoInstance()
ProtoInstance586.name = "Site"
ProtoInstance586.DEF = "hanim_skull_tip"
fieldValue587 = x3d.fieldValue()
fieldValue587.name = "name"
fieldValue587.value = "skull_tip"

ProtoInstance586.fieldValue.append(fieldValue587)
fieldValue588 = x3d.fieldValue()
fieldValue588.name = "translation"
fieldValue588.value = "0.004999999888241291 1.7503999471664429 0.005499999970197678"

ProtoInstance586.fieldValue.append(fieldValue588)

fieldValue585.children.append(ProtoInstance586)
ProtoInstance589 = x3d.ProtoInstance()
ProtoInstance589.name = "Site"
ProtoInstance589.DEF = "hanim_sellion"
fieldValue590 = x3d.fieldValue()
fieldValue590.name = "name"
fieldValue590.value = "sellion"

ProtoInstance589.fieldValue.append(fieldValue590)
fieldValue591 = x3d.fieldValue()
fieldValue591.name = "translation"
fieldValue591.value = "0.005799999926239252 1.631600022315979 0.0851999968290329"

ProtoInstance589.fieldValue.append(fieldValue591)

fieldValue585.children.append(ProtoInstance589)
ProtoInstance592 = x3d.ProtoInstance()
ProtoInstance592.name = "Site"
ProtoInstance592.DEF = "hanim_r_infraorbitale"
fieldValue593 = x3d.fieldValue()
fieldValue593.name = "name"
fieldValue593.value = "r_infraorbitale"

ProtoInstance592.fieldValue.append(fieldValue593)
fieldValue594 = x3d.fieldValue()
fieldValue594.name = "translation"
fieldValue594.value = "-0.02370000071823597 1.6171000003814697 0.07519999891519547"

ProtoInstance592.fieldValue.append(fieldValue594)

fieldValue585.children.append(ProtoInstance592)
ProtoInstance595 = x3d.ProtoInstance()
ProtoInstance595.name = "Site"
ProtoInstance595.DEF = "hanim_l_infraorbitale"
fieldValue596 = x3d.fieldValue()
fieldValue596.name = "name"
fieldValue596.value = "l_infraorbitale"

ProtoInstance595.fieldValue.append(fieldValue596)
fieldValue597 = x3d.fieldValue()
fieldValue597.name = "translation"
fieldValue597.value = "0.0340999998152256 1.6171000003814697 0.07519999891519547"

ProtoInstance595.fieldValue.append(fieldValue597)

fieldValue585.children.append(ProtoInstance595)
ProtoInstance598 = x3d.ProtoInstance()
ProtoInstance598.name = "Site"
ProtoInstance598.DEF = "hanim_supramenton"
fieldValue599 = x3d.fieldValue()
fieldValue599.name = "name"
fieldValue599.value = "supramenton"

ProtoInstance598.fieldValue.append(fieldValue599)
fieldValue600 = x3d.fieldValue()
fieldValue600.name = "translation"
fieldValue600.value = "0.006099999882280827 1.5410000085830688 0.08049999922513962"

ProtoInstance598.fieldValue.append(fieldValue600)

fieldValue585.children.append(ProtoInstance598)
ProtoInstance601 = x3d.ProtoInstance()
ProtoInstance601.name = "Site"
ProtoInstance601.DEF = "hanim_r_tragion"
fieldValue602 = x3d.fieldValue()
fieldValue602.name = "name"
fieldValue602.value = "r_tragion"

ProtoInstance601.fieldValue.append(fieldValue602)
fieldValue603 = x3d.fieldValue()
fieldValue603.name = "translation"
fieldValue603.value = "-0.06459999829530716 1.6346999406814575 0.03020000085234642"

ProtoInstance601.fieldValue.append(fieldValue603)

fieldValue585.children.append(ProtoInstance601)
ProtoInstance604 = x3d.ProtoInstance()
ProtoInstance604.name = "Site"
ProtoInstance604.DEF = "hanim_r_gonion"
fieldValue605 = x3d.fieldValue()
fieldValue605.name = "name"
fieldValue605.value = "r_gonion"

ProtoInstance604.fieldValue.append(fieldValue605)
fieldValue606 = x3d.fieldValue()
fieldValue606.name = "translation"
fieldValue606.value = "-0.052000001072883606 1.552899956703186 0.034699998795986176"

ProtoInstance604.fieldValue.append(fieldValue606)

fieldValue585.children.append(ProtoInstance604)
ProtoInstance607 = x3d.ProtoInstance()
ProtoInstance607.name = "Site"
ProtoInstance607.DEF = "hanim_l_tragion"
fieldValue608 = x3d.fieldValue()
fieldValue608.name = "name"
fieldValue608.value = "l_tragion"

ProtoInstance607.fieldValue.append(fieldValue608)
fieldValue609 = x3d.fieldValue()
fieldValue609.name = "translation"
fieldValue609.value = "0.0738999992609024 1.6347999572753906 0.028200000524520874"

ProtoInstance607.fieldValue.append(fieldValue609)

fieldValue585.children.append(ProtoInstance607)
ProtoInstance610 = x3d.ProtoInstance()
ProtoInstance610.name = "Site"
ProtoInstance610.DEF = "hanim_l_gonion"
fieldValue611 = x3d.fieldValue()
fieldValue611.name = "name"
fieldValue611.value = "l_gonion"

ProtoInstance610.fieldValue.append(fieldValue611)
fieldValue612 = x3d.fieldValue()
fieldValue612.name = "translation"
fieldValue612.value = "0.06310000270605087 1.5529999732971191 0.032999999821186066"

ProtoInstance610.fieldValue.append(fieldValue612)

fieldValue585.children.append(ProtoInstance610)
ProtoInstance613 = x3d.ProtoInstance()
ProtoInstance613.name = "Site"
ProtoInstance613.DEF = "hanim_nuchale"
fieldValue614 = x3d.fieldValue()
fieldValue614.name = "name"
fieldValue614.value = "nuchale"

ProtoInstance613.fieldValue.append(fieldValue614)
fieldValue615 = x3d.fieldValue()
fieldValue615.name = "translation"
fieldValue615.value = "0.0038999998942017555 1.5972000360488892 -0.07959999889135361"

ProtoInstance613.fieldValue.append(fieldValue615)

fieldValue585.children.append(ProtoInstance613)
ProtoInstance616 = x3d.ProtoInstance()
ProtoInstance616.name = "Site"
ProtoInstance616.DEF = "hanim_r_clavicale"
fieldValue617 = x3d.fieldValue()
fieldValue617.name = "name"
fieldValue617.value = "r_clavicale"

ProtoInstance616.fieldValue.append(fieldValue617)
fieldValue618 = x3d.fieldValue()
fieldValue618.name = "translation"
fieldValue618.value = "-0.011500000022351742 1.4943000078201294 0.03999999910593033"

ProtoInstance616.fieldValue.append(fieldValue618)

fieldValue585.children.append(ProtoInstance616)
ProtoInstance619 = x3d.ProtoInstance()
ProtoInstance619.name = "Site"
ProtoInstance619.DEF = "hanim_suprasternale"
fieldValue620 = x3d.fieldValue()
fieldValue620.name = "name"
fieldValue620.value = "suprasternale"

ProtoInstance619.fieldValue.append(fieldValue620)
fieldValue621 = x3d.fieldValue()
fieldValue621.name = "translation"
fieldValue621.value = "0.00839999970048666 1.4714000225067139 0.05510000139474869"

ProtoInstance619.fieldValue.append(fieldValue621)

fieldValue585.children.append(ProtoInstance619)
ProtoInstance622 = x3d.ProtoInstance()
ProtoInstance622.name = "Site"
ProtoInstance622.DEF = "hanim_l_clavicale"
fieldValue623 = x3d.fieldValue()
fieldValue623.name = "name"
fieldValue623.value = "l_clavicale"

ProtoInstance622.fieldValue.append(fieldValue623)
fieldValue624 = x3d.fieldValue()
fieldValue624.name = "translation"
fieldValue624.value = "0.02710000053048134 1.4943000078201294 0.039400000125169754"

ProtoInstance622.fieldValue.append(fieldValue624)

fieldValue585.children.append(ProtoInstance622)
ProtoInstance625 = x3d.ProtoInstance()
ProtoInstance625.name = "Site"
ProtoInstance625.DEF = "hanim_r_thelion"
fieldValue626 = x3d.fieldValue()
fieldValue626.name = "name"
fieldValue626.value = "r_thelion"

ProtoInstance625.fieldValue.append(fieldValue626)
fieldValue627 = x3d.fieldValue()
fieldValue627.name = "translation"
fieldValue627.value = "-0.07360000163316727 1.3385000228881836 0.1216999962925911"

ProtoInstance625.fieldValue.append(fieldValue627)

fieldValue585.children.append(ProtoInstance625)
ProtoInstance628 = x3d.ProtoInstance()
ProtoInstance628.name = "Site"
ProtoInstance628.DEF = "hanim_l_thelion"
fieldValue629 = x3d.fieldValue()
fieldValue629.name = "name"
fieldValue629.value = "l_thelion"

ProtoInstance628.fieldValue.append(fieldValue629)
fieldValue630 = x3d.fieldValue()
fieldValue630.name = "translation"
fieldValue630.value = "0.09179999679327011 1.3381999731063843 0.11919999867677689"

ProtoInstance628.fieldValue.append(fieldValue630)

fieldValue585.children.append(ProtoInstance628)
ProtoInstance631 = x3d.ProtoInstance()
ProtoInstance631.name = "Site"
ProtoInstance631.DEF = "hanim_substernale"
fieldValue632 = x3d.fieldValue()
fieldValue632.name = "name"
fieldValue632.value = "substernale"

ProtoInstance631.fieldValue.append(fieldValue632)
fieldValue633 = x3d.fieldValue()
fieldValue633.name = "translation"
fieldValue633.value = "0.008500000461935997 1.2994999885559082 0.11469999700784683"

ProtoInstance631.fieldValue.append(fieldValue633)

fieldValue585.children.append(ProtoInstance631)
ProtoInstance634 = x3d.ProtoInstance()
ProtoInstance634.name = "Site"
ProtoInstance634.DEF = "hanim_r_rib10"
fieldValue635 = x3d.fieldValue()
fieldValue635.name = "name"
fieldValue635.value = "r_rib10"

ProtoInstance634.fieldValue.append(fieldValue635)
fieldValue636 = x3d.fieldValue()
fieldValue636.name = "translation"
fieldValue636.value = "-0.07109999656677246 1.194100022315979 0.10159999877214432"

ProtoInstance634.fieldValue.append(fieldValue636)

fieldValue585.children.append(ProtoInstance634)
ProtoInstance637 = x3d.ProtoInstance()
ProtoInstance637.name = "Site"
ProtoInstance637.DEF = "hanim_r_asis"
fieldValue638 = x3d.fieldValue()
fieldValue638.name = "name"
fieldValue638.value = "r_asis"

ProtoInstance637.fieldValue.append(fieldValue638)
fieldValue639 = x3d.fieldValue()
fieldValue639.name = "translation"
fieldValue639.value = "-0.08869999647140503 1.0020999908447266 0.1111999973654747"

ProtoInstance637.fieldValue.append(fieldValue639)

fieldValue585.children.append(ProtoInstance637)
ProtoInstance640 = x3d.ProtoInstance()
ProtoInstance640.name = "Site"
ProtoInstance640.DEF = "hanim_l_rib10"
fieldValue641 = x3d.fieldValue()
fieldValue641.name = "name"
fieldValue641.value = "l_rib10"

ProtoInstance640.fieldValue.append(fieldValue641)
fieldValue642 = x3d.fieldValue()
fieldValue642.name = "translation"
fieldValue642.value = "0.08709999918937683 1.1924999952316284 0.09920000284910202"

ProtoInstance640.fieldValue.append(fieldValue642)

fieldValue585.children.append(ProtoInstance640)
ProtoInstance643 = x3d.ProtoInstance()
ProtoInstance643.name = "Site"
ProtoInstance643.DEF = "hanim_l_asis"
fieldValue644 = x3d.fieldValue()
fieldValue644.name = "name"
fieldValue644.value = "l_asis"

ProtoInstance643.fieldValue.append(fieldValue644)
fieldValue645 = x3d.fieldValue()
fieldValue645.name = "translation"
fieldValue645.value = "0.0925000011920929 0.9983000159263611 0.10520000010728836"

ProtoInstance643.fieldValue.append(fieldValue645)

fieldValue585.children.append(ProtoInstance643)
ProtoInstance646 = x3d.ProtoInstance()
ProtoInstance646.name = "Site"
ProtoInstance646.DEF = "hanim_r_iliocristale"
fieldValue647 = x3d.fieldValue()
fieldValue647.name = "name"
fieldValue647.value = "r_iliocristale"

ProtoInstance646.fieldValue.append(fieldValue647)
fieldValue648 = x3d.fieldValue()
fieldValue648.name = "translation"
fieldValue648.value = "-0.1525000035762787 1.0628000497817993 0.0035000001080334187"

ProtoInstance646.fieldValue.append(fieldValue648)

fieldValue585.children.append(ProtoInstance646)
ProtoInstance649 = x3d.ProtoInstance()
ProtoInstance649.name = "Site"
ProtoInstance649.DEF = "hanim_r_trochanterion"
fieldValue650 = x3d.fieldValue()
fieldValue650.name = "name"
fieldValue650.value = "r_trochanterion"

ProtoInstance649.fieldValue.append(fieldValue650)
fieldValue651 = x3d.fieldValue()
fieldValue651.name = "translation"
fieldValue651.value = "-0.1688999980688095 0.8418999910354614 0.03519999980926514"

ProtoInstance649.fieldValue.append(fieldValue651)

fieldValue585.children.append(ProtoInstance649)
ProtoInstance652 = x3d.ProtoInstance()
ProtoInstance652.name = "Site"
ProtoInstance652.DEF = "hanim_l_iliocristale"
fieldValue653 = x3d.fieldValue()
fieldValue653.name = "name"
fieldValue653.value = "l_iliocristale"

ProtoInstance652.fieldValue.append(fieldValue653)
fieldValue654 = x3d.fieldValue()
fieldValue654.name = "translation"
fieldValue654.value = "0.16120000183582306 1.0536999702453613 0.0007999999797903001"

ProtoInstance652.fieldValue.append(fieldValue654)

fieldValue585.children.append(ProtoInstance652)
ProtoInstance655 = x3d.ProtoInstance()
ProtoInstance655.name = "Site"
ProtoInstance655.DEF = "hanim_l_trochanterion"
fieldValue656 = x3d.fieldValue()
fieldValue656.name = "name"
fieldValue656.value = "l_trochanterion"

ProtoInstance655.fieldValue.append(fieldValue656)
fieldValue657 = x3d.fieldValue()
fieldValue657.name = "translation"
fieldValue657.value = "0.16769999265670776 0.8335999846458435 0.030300000682473183"

ProtoInstance655.fieldValue.append(fieldValue657)

fieldValue585.children.append(ProtoInstance655)
ProtoInstance658 = x3d.ProtoInstance()
ProtoInstance658.name = "Site"
ProtoInstance658.DEF = "hanim_cervicale"
fieldValue659 = x3d.fieldValue()
fieldValue659.name = "name"
fieldValue659.value = "cervicale"

ProtoInstance658.fieldValue.append(fieldValue659)
fieldValue660 = x3d.fieldValue()
fieldValue660.name = "translation"
fieldValue660.value = "0.006399999838322401 1.5199999809265137 -0.08150000125169754"

ProtoInstance658.fieldValue.append(fieldValue660)

fieldValue585.children.append(ProtoInstance658)
ProtoInstance661 = x3d.ProtoInstance()
ProtoInstance661.name = "Site"
ProtoInstance661.DEF = "hanim_spine_2_lower_back"
fieldValue662 = x3d.fieldValue()
fieldValue662.name = "name"
fieldValue662.value = "spine_2_lower_back"

ProtoInstance661.fieldValue.append(fieldValue662)
fieldValue663 = x3d.fieldValue()
fieldValue663.name = "translation"
fieldValue663.value = "0.004900000058114529 1.1907999515533447 -0.11129999905824661"

ProtoInstance661.fieldValue.append(fieldValue663)

fieldValue585.children.append(ProtoInstance661)
ProtoInstance664 = x3d.ProtoInstance()
ProtoInstance664.name = "Site"
ProtoInstance664.DEF = "hanim_r_psis"
fieldValue665 = x3d.fieldValue()
fieldValue665.name = "name"
fieldValue665.value = "r_psis"

ProtoInstance664.fieldValue.append(fieldValue665)
fieldValue666 = x3d.fieldValue()
fieldValue666.name = "translation"
fieldValue666.value = "-0.07159999758005142 1.0190000534057617 -0.11379999667406082"

ProtoInstance664.fieldValue.append(fieldValue666)

fieldValue585.children.append(ProtoInstance664)
ProtoInstance667 = x3d.ProtoInstance()
ProtoInstance667.name = "Site"
ProtoInstance667.DEF = "hanim_l_psis"
fieldValue668 = x3d.fieldValue()
fieldValue668.name = "name"
fieldValue668.value = "l_psis"

ProtoInstance667.fieldValue.append(fieldValue668)
fieldValue669 = x3d.fieldValue()
fieldValue669.name = "translation"
fieldValue669.value = "0.07739999890327454 1.0190000534057617 -0.11509999632835388"

ProtoInstance667.fieldValue.append(fieldValue669)

fieldValue585.children.append(ProtoInstance667)
ProtoInstance670 = x3d.ProtoInstance()
ProtoInstance670.name = "Site"
ProtoInstance670.DEF = "hanim_waist_preferred_posterior"
fieldValue671 = x3d.fieldValue()
fieldValue671.name = "name"
fieldValue671.value = "waist_preferred_posterior"

ProtoInstance670.fieldValue.append(fieldValue671)
fieldValue672 = x3d.fieldValue()
fieldValue672.name = "translation"
fieldValue672.value = "0.28999999165534973 1.0915000438690186 -0.10909999907016754"

ProtoInstance670.fieldValue.append(fieldValue672)

fieldValue585.children.append(ProtoInstance670)
ProtoInstance673 = x3d.ProtoInstance()
ProtoInstance673.name = "Site"
ProtoInstance673.DEF = "hanim_r_acromion"
fieldValue674 = x3d.fieldValue()
fieldValue674.name = "name"
fieldValue674.value = "r_acromion"

ProtoInstance673.fieldValue.append(fieldValue674)
fieldValue675 = x3d.fieldValue()
fieldValue675.name = "translation"
fieldValue675.value = "-0.19050000607967377 1.479099988937378 -0.04309999942779541"

ProtoInstance673.fieldValue.append(fieldValue675)

fieldValue585.children.append(ProtoInstance673)
ProtoInstance676 = x3d.ProtoInstance()
ProtoInstance676.name = "Site"
ProtoInstance676.DEF = "hanim_r_axilla_proximal"
fieldValue677 = x3d.fieldValue()
fieldValue677.name = "name"
fieldValue677.value = "r_axilla_proximal"

ProtoInstance676.fieldValue.append(fieldValue677)
fieldValue678 = x3d.fieldValue()
fieldValue678.name = "translation"
fieldValue678.value = "-0.16259999573230743 1.4071999788284302 -0.003100000089034438"

ProtoInstance676.fieldValue.append(fieldValue678)

fieldValue585.children.append(ProtoInstance676)
ProtoInstance679 = x3d.ProtoInstance()
ProtoInstance679.name = "Site"
ProtoInstance679.DEF = "hanim_r_radial_styloid"
fieldValue680 = x3d.fieldValue()
fieldValue680.name = "name"
fieldValue680.value = "r_radial_styloid"

ProtoInstance679.fieldValue.append(fieldValue680)
fieldValue681 = x3d.fieldValue()
fieldValue681.name = "translation"
fieldValue681.value = "-0.188400000333786 0.8676000237464905 -0.035999998450279236"

ProtoInstance679.fieldValue.append(fieldValue681)

fieldValue585.children.append(ProtoInstance679)
ProtoInstance682 = x3d.ProtoInstance()
ProtoInstance682.name = "Site"
ProtoInstance682.DEF = "hanim_r_axilla_distal"
fieldValue683 = x3d.fieldValue()
fieldValue683.name = "name"
fieldValue683.value = "r_axilla_distal"

ProtoInstance682.fieldValue.append(fieldValue683)
fieldValue684 = x3d.fieldValue()
fieldValue684.name = "translation"
fieldValue684.value = "-0.16030000150203705 1.4098000526428223 -0.08259999752044678"

ProtoInstance682.fieldValue.append(fieldValue684)

fieldValue585.children.append(ProtoInstance682)
ProtoInstance685 = x3d.ProtoInstance()
ProtoInstance685.name = "Site"
ProtoInstance685.DEF = "hanim_r_olecranon"
fieldValue686 = x3d.fieldValue()
fieldValue686.name = "name"
fieldValue686.value = "r_olecranon"

ProtoInstance685.fieldValue.append(fieldValue686)
fieldValue687 = x3d.fieldValue()
fieldValue687.name = "translation"
fieldValue687.value = "-0.1906999945640564 1.1404999494552612 -0.10649999976158142"

ProtoInstance685.fieldValue.append(fieldValue687)

fieldValue585.children.append(ProtoInstance685)
ProtoInstance688 = x3d.ProtoInstance()
ProtoInstance688.name = "Site"
ProtoInstance688.DEF = "hanim_r_humeral_lateral_epicondyles"
fieldValue689 = x3d.fieldValue()
fieldValue689.name = "name"
fieldValue689.value = "r_humeral_lateral_epicondyles"

ProtoInstance688.fieldValue.append(fieldValue689)
fieldValue690 = x3d.fieldValue()
fieldValue690.name = "translation"
fieldValue690.value = "-0.2223999947309494 1.1517000198364258 -0.10329999774694443"

ProtoInstance688.fieldValue.append(fieldValue690)

fieldValue585.children.append(ProtoInstance688)
ProtoInstance691 = x3d.ProtoInstance()
ProtoInstance691.name = "Site"
ProtoInstance691.DEF = "hanim_r_humeral_medial_epicondyles"
fieldValue692 = x3d.fieldValue()
fieldValue692.name = "name"
fieldValue692.value = "r_humeral_medial_epicondyles"

ProtoInstance691.fieldValue.append(fieldValue692)
fieldValue693 = x3d.fieldValue()
fieldValue693.name = "translation"
fieldValue693.value = "-0.1679999977350235 1.1297999620437622 -0.10620000213384628"

ProtoInstance691.fieldValue.append(fieldValue693)

fieldValue585.children.append(ProtoInstance691)
ProtoInstance694 = x3d.ProtoInstance()
ProtoInstance694.name = "Site"
ProtoInstance694.DEF = "hanim_r_radiale"
fieldValue695 = x3d.fieldValue()
fieldValue695.name = "name"
fieldValue695.value = "r_radiale"

ProtoInstance694.fieldValue.append(fieldValue695)
fieldValue696 = x3d.fieldValue()
fieldValue696.name = "translation"
fieldValue696.value = "-0.21299999952316284 1.1304999589920044 -0.10909999907016754"

ProtoInstance694.fieldValue.append(fieldValue696)

fieldValue585.children.append(ProtoInstance694)
ProtoInstance697 = x3d.ProtoInstance()
ProtoInstance697.name = "Site"
ProtoInstance697.DEF = "hanim_r_metacarpal_phalanx_2"
fieldValue698 = x3d.fieldValue()
fieldValue698.name = "name"
fieldValue698.value = "r_metacarpal_phalanx_2"

ProtoInstance697.fieldValue.append(fieldValue698)
fieldValue699 = x3d.fieldValue()
fieldValue699.name = "translation"
fieldValue699.value = "-0.19769999384880066 0.8169000148773193 -0.01769999973475933"

ProtoInstance697.fieldValue.append(fieldValue699)

fieldValue585.children.append(ProtoInstance697)
ProtoInstance700 = x3d.ProtoInstance()
ProtoInstance700.name = "Site"
ProtoInstance700.DEF = "hanim_r_dactylion"
fieldValue701 = x3d.fieldValue()
fieldValue701.name = "name"
fieldValue701.value = "r_dactylion"

ProtoInstance700.fieldValue.append(fieldValue701)
fieldValue702 = x3d.fieldValue()
fieldValue702.name = "translation"
fieldValue702.value = "-0.1941000074148178 0.6772000193595886 -0.04230000078678131"

ProtoInstance700.fieldValue.append(fieldValue702)

fieldValue585.children.append(ProtoInstance700)
ProtoInstance703 = x3d.ProtoInstance()
ProtoInstance703.name = "Site"
ProtoInstance703.DEF = "hanim_r_ulnar_styloid"
fieldValue704 = x3d.fieldValue()
fieldValue704.name = "name"
fieldValue704.value = "r_ulnar_styloid"

ProtoInstance703.fieldValue.append(fieldValue704)
fieldValue705 = x3d.fieldValue()
fieldValue705.name = "translation"
fieldValue705.value = "-0.21170000731945038 0.8561999797821045 -0.058400001376867294"

ProtoInstance703.fieldValue.append(fieldValue705)

fieldValue585.children.append(ProtoInstance703)
ProtoInstance706 = x3d.ProtoInstance()
ProtoInstance706.name = "Site"
ProtoInstance706.DEF = "hanim_r_metacarpal_phalanx_5"
fieldValue707 = x3d.fieldValue()
fieldValue707.name = "name"
fieldValue707.value = "r_metacarpal_phalanx_5"

ProtoInstance706.fieldValue.append(fieldValue707)
fieldValue708 = x3d.fieldValue()
fieldValue708.name = "translation"
fieldValue708.value = "-0.19290000200271606 0.7889999747276306 -0.10639999806880951"

ProtoInstance706.fieldValue.append(fieldValue708)

fieldValue585.children.append(ProtoInstance706)
ProtoInstance709 = x3d.ProtoInstance()
ProtoInstance709.name = "Site"
ProtoInstance709.DEF = "hanim_l_acromion"
fieldValue710 = x3d.fieldValue()
fieldValue710.name = "name"
fieldValue710.value = "l_acromion"

ProtoInstance709.fieldValue.append(fieldValue710)
fieldValue711 = x3d.fieldValue()
fieldValue711.name = "translation"
fieldValue711.value = "0.20319999754428864 1.4759999513626099 -0.04899999871850014"

ProtoInstance709.fieldValue.append(fieldValue711)

fieldValue585.children.append(ProtoInstance709)
ProtoInstance712 = x3d.ProtoInstance()
ProtoInstance712.name = "Site"
ProtoInstance712.DEF = "hanim_l_axilla_proximal"
fieldValue713 = x3d.fieldValue()
fieldValue713.name = "name"
fieldValue713.value = "l_axilla_proximal"

ProtoInstance712.fieldValue.append(fieldValue713)
fieldValue714 = x3d.fieldValue()
fieldValue714.name = "translation"
fieldValue714.value = "0.1776999980211258 1.406499981880188 -0.007499999832361937"

ProtoInstance712.fieldValue.append(fieldValue714)

fieldValue585.children.append(ProtoInstance712)
ProtoInstance715 = x3d.ProtoInstance()
ProtoInstance715.name = "Site"
ProtoInstance715.DEF = "hanim_l_radial_styloid"
fieldValue716 = x3d.fieldValue()
fieldValue716.name = "name"
fieldValue716.value = "l_radial_styloid"

ProtoInstance715.fieldValue.append(fieldValue716)
fieldValue717 = x3d.fieldValue()
fieldValue717.name = "translation"
fieldValue717.value = "0.19009999930858612 0.8644999861717224 -0.04149999842047691"

ProtoInstance715.fieldValue.append(fieldValue717)

fieldValue585.children.append(ProtoInstance715)
ProtoInstance718 = x3d.ProtoInstance()
ProtoInstance718.name = "Site"
ProtoInstance718.DEF = "hanim_l_axilla_distal"
fieldValue719 = x3d.fieldValue()
fieldValue719.name = "name"
fieldValue719.value = "l_axilla_distal"

ProtoInstance718.fieldValue.append(fieldValue719)
fieldValue720 = x3d.fieldValue()
fieldValue720.name = "translation"
fieldValue720.value = "0.17059999704360962 1.4071999788284302 -0.08749999850988388"

ProtoInstance718.fieldValue.append(fieldValue720)

fieldValue585.children.append(ProtoInstance718)
ProtoInstance721 = x3d.ProtoInstance()
ProtoInstance721.name = "Site"
ProtoInstance721.DEF = "hanim_l_olecranon"
fieldValue722 = x3d.fieldValue()
fieldValue722.name = "name"
fieldValue722.value = "l_olecranon"

ProtoInstance721.fieldValue.append(fieldValue722)
fieldValue723 = x3d.fieldValue()
fieldValue723.name = "translation"
fieldValue723.value = "-0.19619999825954437 1.1375000476837158 -0.11230000108480453"

ProtoInstance721.fieldValue.append(fieldValue723)

fieldValue585.children.append(ProtoInstance721)
ProtoInstance724 = x3d.ProtoInstance()
ProtoInstance724.name = "Site"
ProtoInstance724.DEF = "hanim_l_humeral_lateral_epicondyles"
fieldValue725 = x3d.fieldValue()
fieldValue725.name = "name"
fieldValue725.value = "l_humeral_lateral_epicondyles"

ProtoInstance724.fieldValue.append(fieldValue725)
fieldValue726 = x3d.fieldValue()
fieldValue726.name = "translation"
fieldValue726.value = "0.2280000001192093 1.1482000350952148 -0.10999999940395355"

ProtoInstance724.fieldValue.append(fieldValue726)

fieldValue585.children.append(ProtoInstance724)
ProtoInstance727 = x3d.ProtoInstance()
ProtoInstance727.name = "Site"
ProtoInstance727.DEF = "hanim_l_humeral_medial_epicondyles"
fieldValue728 = x3d.fieldValue()
fieldValue728.name = "name"
fieldValue728.value = "l_humeral_medial_epicondyles"

ProtoInstance727.fieldValue.append(fieldValue728)
fieldValue729 = x3d.fieldValue()
fieldValue729.name = "translation"
fieldValue729.value = "0.17350000143051147 1.1272000074386597 -0.11129999905824661"

ProtoInstance727.fieldValue.append(fieldValue729)

fieldValue585.children.append(ProtoInstance727)
ProtoInstance730 = x3d.ProtoInstance()
ProtoInstance730.name = "Site"
ProtoInstance730.DEF = "hanim_l_radiale"
fieldValue731 = x3d.fieldValue()
fieldValue731.name = "name"
fieldValue731.value = "l_radiale"

ProtoInstance730.fieldValue.append(fieldValue731)
fieldValue732 = x3d.fieldValue()
fieldValue732.name = "translation"
fieldValue732.value = "0.21819999814033508 1.1211999654769897 -0.11670000106096268"

ProtoInstance730.fieldValue.append(fieldValue732)

fieldValue585.children.append(ProtoInstance730)
ProtoInstance733 = x3d.ProtoInstance()
ProtoInstance733.name = "Site"
ProtoInstance733.DEF = "hanim_l_metacarpal_phalanx_2"
fieldValue734 = x3d.fieldValue()
fieldValue734.name = "name"
fieldValue734.value = "l_metacarpal_phalanx_2"

ProtoInstance733.fieldValue.append(fieldValue734)
fieldValue735 = x3d.fieldValue()
fieldValue735.name = "translation"
fieldValue735.value = "0.20090000331401825 0.8138999938964844 -0.02370000071823597"

ProtoInstance733.fieldValue.append(fieldValue735)

fieldValue585.children.append(ProtoInstance733)
ProtoInstance736 = x3d.ProtoInstance()
ProtoInstance736.name = "Site"
ProtoInstance736.DEF = "hanim_l_dactylion"
fieldValue737 = x3d.fieldValue()
fieldValue737.name = "name"
fieldValue737.value = "l_dactylion"

ProtoInstance736.fieldValue.append(fieldValue737)
fieldValue738 = x3d.fieldValue()
fieldValue738.name = "translation"
fieldValue738.value = "0.20559999346733093 0.6743000149726868 -0.04820000007748604"

ProtoInstance736.fieldValue.append(fieldValue738)

fieldValue585.children.append(ProtoInstance736)
ProtoInstance739 = x3d.ProtoInstance()
ProtoInstance739.name = "Site"
ProtoInstance739.DEF = "hanim_l_ulnar_styloid"
fieldValue740 = x3d.fieldValue()
fieldValue740.name = "name"
fieldValue740.value = "l_ulnar_styloid"

ProtoInstance739.fieldValue.append(fieldValue740)
fieldValue741 = x3d.fieldValue()
fieldValue741.name = "translation"
fieldValue741.value = "-0.2142000049352646 0.8529000282287598 -0.06480000168085098"

ProtoInstance739.fieldValue.append(fieldValue741)

fieldValue585.children.append(ProtoInstance739)
ProtoInstance742 = x3d.ProtoInstance()
ProtoInstance742.name = "Site"
ProtoInstance742.DEF = "hanim_l_metacarpal_phalanx_5"
fieldValue743 = x3d.fieldValue()
fieldValue743.name = "name"
fieldValue743.value = "l_metacarpal_phalanx_5"

ProtoInstance742.fieldValue.append(fieldValue743)
fieldValue744 = x3d.fieldValue()
fieldValue744.name = "translation"
fieldValue744.value = "0.19290000200271606 0.7860000133514404 -0.11219999939203262"

ProtoInstance742.fieldValue.append(fieldValue744)

fieldValue585.children.append(ProtoInstance742)
ProtoInstance745 = x3d.ProtoInstance()
ProtoInstance745.name = "Site"
ProtoInstance745.DEF = "hanim_r_knee_crease"
fieldValue746 = x3d.fieldValue()
fieldValue746.name = "name"
fieldValue746.value = "r_knee_crease"

ProtoInstance745.fieldValue.append(fieldValue746)
fieldValue747 = x3d.fieldValue()
fieldValue747.name = "translation"
fieldValue747.value = "-0.08250000327825546 0.49320000410079956 -0.032600000500679016"

ProtoInstance745.fieldValue.append(fieldValue747)

fieldValue585.children.append(ProtoInstance745)
ProtoInstance748 = x3d.ProtoInstance()
ProtoInstance748.name = "Site"
ProtoInstance748.DEF = "hanim_r_femoral_lateral_epicondyles"
fieldValue749 = x3d.fieldValue()
fieldValue749.name = "name"
fieldValue749.value = "r_femoral_lateral_epicondyles"

ProtoInstance748.fieldValue.append(fieldValue749)
fieldValue750 = x3d.fieldValue()
fieldValue750.name = "translation"
fieldValue750.value = "-0.1421000063419342 0.4991999864578247 0.03099999949336052"

ProtoInstance748.fieldValue.append(fieldValue750)

fieldValue585.children.append(ProtoInstance748)
ProtoInstance751 = x3d.ProtoInstance()
ProtoInstance751.name = "Site"
ProtoInstance751.DEF = "hanim_r_femoral_medial_epicondyles"
fieldValue752 = x3d.fieldValue()
fieldValue752.name = "name"
fieldValue752.value = "r_femoral_lateral_epicondyles"

ProtoInstance751.fieldValue.append(fieldValue752)
fieldValue753 = x3d.fieldValue()
fieldValue753.name = "translation"
fieldValue753.value = "-0.022099999710917473 0.5013999938964844 0.02889999933540821"

ProtoInstance751.fieldValue.append(fieldValue753)

fieldValue585.children.append(ProtoInstance751)
ProtoInstance754 = x3d.ProtoInstance()
ProtoInstance754.name = "Site"
ProtoInstance754.DEF = "hanim_r_tarsal_interphalangeal_phalanx_5"
fieldValue755 = x3d.fieldValue()
fieldValue755.name = "name"
fieldValue755.value = "r_tarsal_interphalangeal_phalanx_5"

ProtoInstance754.fieldValue.append(fieldValue755)
fieldValue756 = x3d.fieldValue()
fieldValue756.name = "translation"
fieldValue756.value = "-0.15230000019073486 0.016599999740719795 0.08950000256299973"

ProtoInstance754.fieldValue.append(fieldValue756)

fieldValue585.children.append(ProtoInstance754)
ProtoInstance757 = x3d.ProtoInstance()
ProtoInstance757.name = "Site"
ProtoInstance757.DEF = "hanim_r_lateral_malleolus"
fieldValue758 = x3d.fieldValue()
fieldValue758.name = "name"
fieldValue758.value = "r_lateral_malleolus"

ProtoInstance757.fieldValue.append(fieldValue758)
fieldValue759 = x3d.fieldValue()
fieldValue759.name = "translation"
fieldValue759.value = "-0.1005999967455864 0.0658000037074089 -0.10750000178813934"

ProtoInstance757.fieldValue.append(fieldValue759)

fieldValue585.children.append(ProtoInstance757)
ProtoInstance760 = x3d.ProtoInstance()
ProtoInstance760.name = "Site"
ProtoInstance760.DEF = "hanim_r_medial_malleolus"
fieldValue761 = x3d.fieldValue()
fieldValue761.name = "name"
fieldValue761.value = "r_medial_malleolus"

ProtoInstance760.fieldValue.append(fieldValue761)
fieldValue762 = x3d.fieldValue()
fieldValue762.name = "translation"
fieldValue762.value = "-0.05909999832510948 0.07599999755620956 -0.09279999881982803"

ProtoInstance760.fieldValue.append(fieldValue762)

fieldValue585.children.append(ProtoInstance760)
ProtoInstance763 = x3d.ProtoInstance()
ProtoInstance763.name = "Site"
ProtoInstance763.DEF = "hanim_r_sphyrion"
fieldValue764 = x3d.fieldValue()
fieldValue764.name = "name"
fieldValue764.value = "r_sphyrion"

ProtoInstance763.fieldValue.append(fieldValue764)
fieldValue765 = x3d.fieldValue()
fieldValue765.name = "translation"
fieldValue765.value = "-0.06030000001192093 0.061000000685453415 -0.10019999742507935"

ProtoInstance763.fieldValue.append(fieldValue765)

fieldValue585.children.append(ProtoInstance763)
ProtoInstance766 = x3d.ProtoInstance()
ProtoInstance766.name = "Site"
ProtoInstance766.DEF = "hanim_r_tarsal_interphalangeal_phalanx_1"
fieldValue767 = x3d.fieldValue()
fieldValue767.name = "name"
fieldValue767.value = "r_tarsal_interphalangeal_phalanx_1"

ProtoInstance766.fieldValue.append(fieldValue767)
fieldValue768 = x3d.fieldValue()
fieldValue768.name = "translation"
fieldValue768.value = "-0.05209999904036522 0.026000000536441803 0.01269999984651804"

ProtoInstance766.fieldValue.append(fieldValue768)

fieldValue585.children.append(ProtoInstance766)
ProtoInstance769 = x3d.ProtoInstance()
ProtoInstance769.name = "Site"
ProtoInstance769.DEF = "hanim_r_calcaneus_posterior"
fieldValue770 = x3d.fieldValue()
fieldValue770.name = "name"
fieldValue770.value = "r_calcaneus_posterior"

ProtoInstance769.fieldValue.append(fieldValue770)
fieldValue771 = x3d.fieldValue()
fieldValue771.name = "translation"
fieldValue771.value = "-0.06920000165700912 0.02969999983906746 -0.12210000306367874"

ProtoInstance769.fieldValue.append(fieldValue771)

fieldValue585.children.append(ProtoInstance769)
ProtoInstance772 = x3d.ProtoInstance()
ProtoInstance772.name = "Site"
ProtoInstance772.DEF = "hanim_r_tarsal_distal_phalanx_2"
fieldValue773 = x3d.fieldValue()
fieldValue773.name = "name"
fieldValue773.value = "r_tarsal_distal_phalanx_2"

ProtoInstance772.fieldValue.append(fieldValue773)
fieldValue774 = x3d.fieldValue()
fieldValue774.name = "translation"
fieldValue774.value = "-0.08829999715089798 0.013399999588727951 0.13830000162124634"

ProtoInstance772.fieldValue.append(fieldValue774)

fieldValue585.children.append(ProtoInstance772)
ProtoInstance775 = x3d.ProtoInstance()
ProtoInstance775.name = "Site"
ProtoInstance775.DEF = "hanim_l_knee_crease"
fieldValue776 = x3d.fieldValue()
fieldValue776.name = "name"
fieldValue776.value = "l_knee_crease"

ProtoInstance775.fieldValue.append(fieldValue776)
fieldValue777 = x3d.fieldValue()
fieldValue777.name = "translation"
fieldValue777.value = "0.09929999709129333 0.48809999227523804 -0.030899999663233757"

ProtoInstance775.fieldValue.append(fieldValue777)

fieldValue585.children.append(ProtoInstance775)
ProtoInstance778 = x3d.ProtoInstance()
ProtoInstance778.name = "Site"
ProtoInstance778.DEF = "hanim_l_femoral_lateral_epicondyles"
fieldValue779 = x3d.fieldValue()
fieldValue779.name = "name"
fieldValue779.value = "l_femoral_lateral_epicondyles"

ProtoInstance778.fieldValue.append(fieldValue779)
fieldValue780 = x3d.fieldValue()
fieldValue780.name = "translation"
fieldValue780.value = "0.1597999930381775 0.4966999888420105 0.02969999983906746"

ProtoInstance778.fieldValue.append(fieldValue780)

fieldValue585.children.append(ProtoInstance778)
ProtoInstance781 = x3d.ProtoInstance()
ProtoInstance781.name = "Site"
ProtoInstance781.DEF = "hanim_l_femoral_medial_epicondyles"
fieldValue782 = x3d.fieldValue()
fieldValue782.name = "name"
fieldValue782.value = "l_femoral_lateral_epicondyles"

ProtoInstance781.fieldValue.append(fieldValue782)
fieldValue783 = x3d.fieldValue()
fieldValue783.name = "translation"
fieldValue783.value = "0.039799999445676804 0.49459999799728394 0.030300000682473183"

ProtoInstance781.fieldValue.append(fieldValue783)

fieldValue585.children.append(ProtoInstance781)
ProtoInstance784 = x3d.ProtoInstance()
ProtoInstance784.name = "Site"
ProtoInstance784.DEF = "hanim_l_tarsal_interphalangeal_phalanx_5"
fieldValue785 = x3d.fieldValue()
fieldValue785.name = "name"
fieldValue785.value = "l_tarsal_interphalangeal_phalanx_5"

ProtoInstance784.fieldValue.append(fieldValue785)
fieldValue786 = x3d.fieldValue()
fieldValue786.name = "translation"
fieldValue786.value = "0.18250000476837158 0.007000000216066837 0.09279999881982803"

ProtoInstance784.fieldValue.append(fieldValue786)

fieldValue585.children.append(ProtoInstance784)
ProtoInstance787 = x3d.ProtoInstance()
ProtoInstance787.name = "Site"
ProtoInstance787.DEF = "hanim_l_lateral_malleolus"
fieldValue788 = x3d.fieldValue()
fieldValue788.name = "name"
fieldValue788.value = "l_lateral_malleolus"

ProtoInstance787.fieldValue.append(fieldValue788)
fieldValue789 = x3d.fieldValue()
fieldValue789.name = "translation"
fieldValue789.value = "0.13079999387264252 0.059700001031160355 -0.10320000350475311"

ProtoInstance787.fieldValue.append(fieldValue789)

fieldValue585.children.append(ProtoInstance787)
ProtoInstance790 = x3d.ProtoInstance()
ProtoInstance790.name = "Site"
ProtoInstance790.DEF = "hanim_l_medial_malleolus"
fieldValue791 = x3d.fieldValue()
fieldValue791.name = "name"
fieldValue791.value = "l_medial_malleolus"

ProtoInstance790.fieldValue.append(fieldValue791)
fieldValue792 = x3d.fieldValue()
fieldValue792.name = "translation"
fieldValue792.value = "0.08900000154972076 0.07159999758005142 -0.08810000121593475"

ProtoInstance790.fieldValue.append(fieldValue792)

fieldValue585.children.append(ProtoInstance790)
ProtoInstance793 = x3d.ProtoInstance()
ProtoInstance793.name = "Site"
ProtoInstance793.DEF = "hanim_l_sphyrion"
fieldValue794 = x3d.fieldValue()
fieldValue794.name = "name"
fieldValue794.value = "l_sphyrion"

ProtoInstance793.fieldValue.append(fieldValue794)
fieldValue795 = x3d.fieldValue()
fieldValue795.name = "translation"
fieldValue795.value = "0.08900000154972076 0.057500001043081284 -0.09430000185966492"

ProtoInstance793.fieldValue.append(fieldValue795)

fieldValue585.children.append(ProtoInstance793)
ProtoInstance796 = x3d.ProtoInstance()
ProtoInstance796.name = "Site"
ProtoInstance796.DEF = "hanim_l_tarsal_interphalangeal_phalanx_1"
fieldValue797 = x3d.fieldValue()
fieldValue797.name = "name"
fieldValue797.value = "l_tarsal_interphalangeal_phalanx_1"

ProtoInstance796.fieldValue.append(fieldValue797)
fieldValue798 = x3d.fieldValue()
fieldValue798.name = "translation"
fieldValue798.value = "0.08160000294446945 0.02319999970495701 0.010599999688565731"

ProtoInstance796.fieldValue.append(fieldValue798)

fieldValue585.children.append(ProtoInstance796)
ProtoInstance799 = x3d.ProtoInstance()
ProtoInstance799.name = "Site"
ProtoInstance799.DEF = "hanim_l_calcaneus_posterior"
fieldValue800 = x3d.fieldValue()
fieldValue800.name = "name"
fieldValue800.value = "l_calcaneus_posterior"

ProtoInstance799.fieldValue.append(fieldValue800)
fieldValue801 = x3d.fieldValue()
fieldValue801.name = "translation"
fieldValue801.value = "0.09740000218153 0.02590000070631504 -0.11710000038146973"

ProtoInstance799.fieldValue.append(fieldValue801)

fieldValue585.children.append(ProtoInstance799)
ProtoInstance802 = x3d.ProtoInstance()
ProtoInstance802.name = "Site"
ProtoInstance802.DEF = "hanim_l_tarsal_distal_phalanx_2"
fieldValue803 = x3d.fieldValue()
fieldValue803.name = "name"
fieldValue803.value = "l_tarsal_distal_phalanx_2"

ProtoInstance802.fieldValue.append(fieldValue803)
fieldValue804 = x3d.fieldValue()
fieldValue804.name = "translation"
fieldValue804.value = "0.11949999630451202 0.007899999618530273 0.14329999685287476"

ProtoInstance802.fieldValue.append(fieldValue804)

fieldValue585.children.append(ProtoInstance802)
ProtoInstance805 = x3d.ProtoInstance()
ProtoInstance805.name = "Site"
ProtoInstance805.DEF = "hanim_crotch"
fieldValue806 = x3d.fieldValue()
fieldValue806.name = "name"
fieldValue806.value = "crotch"

ProtoInstance805.fieldValue.append(fieldValue806)
fieldValue807 = x3d.fieldValue()
fieldValue807.name = "translation"
fieldValue807.value = "0.0034000000450760126 0.8266000151634216 0.025699999183416367"

ProtoInstance805.fieldValue.append(fieldValue807)

fieldValue585.children.append(ProtoInstance805)
ProtoInstance808 = x3d.ProtoInstance()
ProtoInstance808.name = "Site"
ProtoInstance808.DEF = "hanim_r_neck_base"
fieldValue809 = x3d.fieldValue()
fieldValue809.name = "name"
fieldValue809.value = "r_neck_base"

ProtoInstance808.fieldValue.append(fieldValue809)
fieldValue810 = x3d.fieldValue()
fieldValue810.name = "translation"
fieldValue810.value = "-0.04190000146627426 1.5148999691009521 -0.02199999988079071"

ProtoInstance808.fieldValue.append(fieldValue810)

fieldValue585.children.append(ProtoInstance808)
ProtoInstance811 = x3d.ProtoInstance()
ProtoInstance811.name = "Site"
ProtoInstance811.DEF = "hanim_l_neck_base"
fieldValue812 = x3d.fieldValue()
fieldValue812.name = "name"
fieldValue812.value = "l_neck_base"

ProtoInstance811.fieldValue.append(fieldValue812)
fieldValue813 = x3d.fieldValue()
fieldValue813.name = "translation"
fieldValue813.value = "0.06459999829530716 1.5140999555587769 -0.03799999877810478"

ProtoInstance811.fieldValue.append(fieldValue813)

fieldValue585.children.append(ProtoInstance811)
ProtoInstance814 = x3d.ProtoInstance()
ProtoInstance814.name = "Site"
ProtoInstance814.DEF = "hanim_navel"
fieldValue815 = x3d.fieldValue()
fieldValue815.name = "name"
fieldValue815.value = "navel"

ProtoInstance814.fieldValue.append(fieldValue815)
fieldValue816 = x3d.fieldValue()
fieldValue816.name = "translation"
fieldValue816.value = "0.006899999920278788 1.09660005569458 0.10170000046491623"

ProtoInstance814.fieldValue.append(fieldValue816)

fieldValue585.children.append(ProtoInstance814)

ProtoInstance583.fieldValue.append(fieldValue585)

fieldValue582.children.append(ProtoInstance583)

ProtoInstance101.fieldValue.append(fieldValue582)
fieldValue817 = x3d.fieldValue()
fieldValue817.name = "sites"
ProtoInstance818 = x3d.ProtoInstance()
ProtoInstance818.name = "Site"
ProtoInstance818.DEF = "hanim_skull_tip"
fieldValue819 = x3d.fieldValue()
fieldValue819.name = "name"
fieldValue819.value = "skull_tip"

ProtoInstance818.fieldValue.append(fieldValue819)
fieldValue820 = x3d.fieldValue()
fieldValue820.name = "translation"
fieldValue820.value = "0.004999999888241291 1.7503999471664429 0.005499999970197678"

ProtoInstance818.fieldValue.append(fieldValue820)

fieldValue817.children.append(ProtoInstance818)
ProtoInstance821 = x3d.ProtoInstance()
ProtoInstance821.name = "Site"
ProtoInstance821.DEF = "hanim_sellion"
fieldValue822 = x3d.fieldValue()
fieldValue822.name = "name"
fieldValue822.value = "sellion"

ProtoInstance821.fieldValue.append(fieldValue822)
fieldValue823 = x3d.fieldValue()
fieldValue823.name = "translation"
fieldValue823.value = "0.005799999926239252 1.631600022315979 0.0851999968290329"

ProtoInstance821.fieldValue.append(fieldValue823)

fieldValue817.children.append(ProtoInstance821)
ProtoInstance824 = x3d.ProtoInstance()
ProtoInstance824.name = "Site"
ProtoInstance824.DEF = "hanim_r_infraorbitale"
fieldValue825 = x3d.fieldValue()
fieldValue825.name = "name"
fieldValue825.value = "r_infraorbitale"

ProtoInstance824.fieldValue.append(fieldValue825)
fieldValue826 = x3d.fieldValue()
fieldValue826.name = "translation"
fieldValue826.value = "-0.02370000071823597 1.6171000003814697 0.07519999891519547"

ProtoInstance824.fieldValue.append(fieldValue826)

fieldValue817.children.append(ProtoInstance824)
ProtoInstance827 = x3d.ProtoInstance()
ProtoInstance827.name = "Site"
ProtoInstance827.DEF = "hanim_l_infraorbitale"
fieldValue828 = x3d.fieldValue()
fieldValue828.name = "name"
fieldValue828.value = "l_infraorbitale"

ProtoInstance827.fieldValue.append(fieldValue828)
fieldValue829 = x3d.fieldValue()
fieldValue829.name = "translation"
fieldValue829.value = "0.0340999998152256 1.6171000003814697 0.07519999891519547"

ProtoInstance827.fieldValue.append(fieldValue829)

fieldValue817.children.append(ProtoInstance827)
ProtoInstance830 = x3d.ProtoInstance()
ProtoInstance830.name = "Site"
ProtoInstance830.DEF = "hanim_supramenton"
fieldValue831 = x3d.fieldValue()
fieldValue831.name = "name"
fieldValue831.value = "supramenton"

ProtoInstance830.fieldValue.append(fieldValue831)
fieldValue832 = x3d.fieldValue()
fieldValue832.name = "translation"
fieldValue832.value = "0.006099999882280827 1.5410000085830688 0.08049999922513962"

ProtoInstance830.fieldValue.append(fieldValue832)

fieldValue817.children.append(ProtoInstance830)
ProtoInstance833 = x3d.ProtoInstance()
ProtoInstance833.name = "Site"
ProtoInstance833.DEF = "hanim_r_tragion"
fieldValue834 = x3d.fieldValue()
fieldValue834.name = "name"
fieldValue834.value = "r_tragion"

ProtoInstance833.fieldValue.append(fieldValue834)
fieldValue835 = x3d.fieldValue()
fieldValue835.name = "translation"
fieldValue835.value = "-0.06459999829530716 1.6346999406814575 0.03020000085234642"

ProtoInstance833.fieldValue.append(fieldValue835)

fieldValue817.children.append(ProtoInstance833)
ProtoInstance836 = x3d.ProtoInstance()
ProtoInstance836.name = "Site"
ProtoInstance836.DEF = "hanim_r_gonion"
fieldValue837 = x3d.fieldValue()
fieldValue837.name = "name"
fieldValue837.value = "r_gonion"

ProtoInstance836.fieldValue.append(fieldValue837)
fieldValue838 = x3d.fieldValue()
fieldValue838.name = "translation"
fieldValue838.value = "-0.052000001072883606 1.552899956703186 0.034699998795986176"

ProtoInstance836.fieldValue.append(fieldValue838)

fieldValue817.children.append(ProtoInstance836)
ProtoInstance839 = x3d.ProtoInstance()
ProtoInstance839.name = "Site"
ProtoInstance839.DEF = "hanim_l_tragion"
fieldValue840 = x3d.fieldValue()
fieldValue840.name = "name"
fieldValue840.value = "l_tragion"

ProtoInstance839.fieldValue.append(fieldValue840)
fieldValue841 = x3d.fieldValue()
fieldValue841.name = "translation"
fieldValue841.value = "0.0738999992609024 1.6347999572753906 0.028200000524520874"

ProtoInstance839.fieldValue.append(fieldValue841)

fieldValue817.children.append(ProtoInstance839)
ProtoInstance842 = x3d.ProtoInstance()
ProtoInstance842.name = "Site"
ProtoInstance842.DEF = "hanim_l_gonion"
fieldValue843 = x3d.fieldValue()
fieldValue843.name = "name"
fieldValue843.value = "l_gonion"

ProtoInstance842.fieldValue.append(fieldValue843)
fieldValue844 = x3d.fieldValue()
fieldValue844.name = "translation"
fieldValue844.value = "0.06310000270605087 1.5529999732971191 0.032999999821186066"

ProtoInstance842.fieldValue.append(fieldValue844)

fieldValue817.children.append(ProtoInstance842)
ProtoInstance845 = x3d.ProtoInstance()
ProtoInstance845.name = "Site"
ProtoInstance845.DEF = "hanim_nuchale"
fieldValue846 = x3d.fieldValue()
fieldValue846.name = "name"
fieldValue846.value = "nuchale"

ProtoInstance845.fieldValue.append(fieldValue846)
fieldValue847 = x3d.fieldValue()
fieldValue847.name = "translation"
fieldValue847.value = "0.0038999998942017555 1.5972000360488892 -0.07959999889135361"

ProtoInstance845.fieldValue.append(fieldValue847)

fieldValue817.children.append(ProtoInstance845)
ProtoInstance848 = x3d.ProtoInstance()
ProtoInstance848.name = "Site"
ProtoInstance848.DEF = "hanim_r_clavicale"
fieldValue849 = x3d.fieldValue()
fieldValue849.name = "name"
fieldValue849.value = "r_clavicale"

ProtoInstance848.fieldValue.append(fieldValue849)
fieldValue850 = x3d.fieldValue()
fieldValue850.name = "translation"
fieldValue850.value = "-0.011500000022351742 1.4943000078201294 0.03999999910593033"

ProtoInstance848.fieldValue.append(fieldValue850)

fieldValue817.children.append(ProtoInstance848)
ProtoInstance851 = x3d.ProtoInstance()
ProtoInstance851.name = "Site"
ProtoInstance851.DEF = "hanim_suprasternale"
fieldValue852 = x3d.fieldValue()
fieldValue852.name = "name"
fieldValue852.value = "suprasternale"

ProtoInstance851.fieldValue.append(fieldValue852)
fieldValue853 = x3d.fieldValue()
fieldValue853.name = "translation"
fieldValue853.value = "0.00839999970048666 1.4714000225067139 0.05510000139474869"

ProtoInstance851.fieldValue.append(fieldValue853)

fieldValue817.children.append(ProtoInstance851)
ProtoInstance854 = x3d.ProtoInstance()
ProtoInstance854.name = "Site"
ProtoInstance854.DEF = "hanim_l_clavicale"
fieldValue855 = x3d.fieldValue()
fieldValue855.name = "name"
fieldValue855.value = "l_clavicale"

ProtoInstance854.fieldValue.append(fieldValue855)
fieldValue856 = x3d.fieldValue()
fieldValue856.name = "translation"
fieldValue856.value = "0.02710000053048134 1.4943000078201294 0.039400000125169754"

ProtoInstance854.fieldValue.append(fieldValue856)

fieldValue817.children.append(ProtoInstance854)
ProtoInstance857 = x3d.ProtoInstance()
ProtoInstance857.name = "Site"
ProtoInstance857.DEF = "hanim_r_thelion"
fieldValue858 = x3d.fieldValue()
fieldValue858.name = "name"
fieldValue858.value = "r_thelion"

ProtoInstance857.fieldValue.append(fieldValue858)
fieldValue859 = x3d.fieldValue()
fieldValue859.name = "translation"
fieldValue859.value = "-0.07360000163316727 1.3385000228881836 0.1216999962925911"

ProtoInstance857.fieldValue.append(fieldValue859)

fieldValue817.children.append(ProtoInstance857)
ProtoInstance860 = x3d.ProtoInstance()
ProtoInstance860.name = "Site"
ProtoInstance860.DEF = "hanim_l_thelion"
fieldValue861 = x3d.fieldValue()
fieldValue861.name = "name"
fieldValue861.value = "l_thelion"

ProtoInstance860.fieldValue.append(fieldValue861)
fieldValue862 = x3d.fieldValue()
fieldValue862.name = "translation"
fieldValue862.value = "0.09179999679327011 1.3381999731063843 0.11919999867677689"

ProtoInstance860.fieldValue.append(fieldValue862)

fieldValue817.children.append(ProtoInstance860)
ProtoInstance863 = x3d.ProtoInstance()
ProtoInstance863.name = "Site"
ProtoInstance863.DEF = "hanim_substernale"
fieldValue864 = x3d.fieldValue()
fieldValue864.name = "name"
fieldValue864.value = "substernale"

ProtoInstance863.fieldValue.append(fieldValue864)
fieldValue865 = x3d.fieldValue()
fieldValue865.name = "translation"
fieldValue865.value = "0.008500000461935997 1.2994999885559082 0.11469999700784683"

ProtoInstance863.fieldValue.append(fieldValue865)

fieldValue817.children.append(ProtoInstance863)
ProtoInstance866 = x3d.ProtoInstance()
ProtoInstance866.name = "Site"
ProtoInstance866.DEF = "hanim_r_rib10"
fieldValue867 = x3d.fieldValue()
fieldValue867.name = "name"
fieldValue867.value = "r_rib10"

ProtoInstance866.fieldValue.append(fieldValue867)
fieldValue868 = x3d.fieldValue()
fieldValue868.name = "translation"
fieldValue868.value = "-0.07109999656677246 1.194100022315979 0.10159999877214432"

ProtoInstance866.fieldValue.append(fieldValue868)

fieldValue817.children.append(ProtoInstance866)
ProtoInstance869 = x3d.ProtoInstance()
ProtoInstance869.name = "Site"
ProtoInstance869.DEF = "hanim_r_asis"
fieldValue870 = x3d.fieldValue()
fieldValue870.name = "name"
fieldValue870.value = "r_asis"

ProtoInstance869.fieldValue.append(fieldValue870)
fieldValue871 = x3d.fieldValue()
fieldValue871.name = "translation"
fieldValue871.value = "-0.08869999647140503 1.0020999908447266 0.1111999973654747"

ProtoInstance869.fieldValue.append(fieldValue871)

fieldValue817.children.append(ProtoInstance869)
ProtoInstance872 = x3d.ProtoInstance()
ProtoInstance872.name = "Site"
ProtoInstance872.DEF = "hanim_l_rib10"
fieldValue873 = x3d.fieldValue()
fieldValue873.name = "name"
fieldValue873.value = "l_rib10"

ProtoInstance872.fieldValue.append(fieldValue873)
fieldValue874 = x3d.fieldValue()
fieldValue874.name = "translation"
fieldValue874.value = "0.08709999918937683 1.1924999952316284 0.09920000284910202"

ProtoInstance872.fieldValue.append(fieldValue874)

fieldValue817.children.append(ProtoInstance872)
ProtoInstance875 = x3d.ProtoInstance()
ProtoInstance875.name = "Site"
ProtoInstance875.DEF = "hanim_l_asis"
fieldValue876 = x3d.fieldValue()
fieldValue876.name = "name"
fieldValue876.value = "l_asis"

ProtoInstance875.fieldValue.append(fieldValue876)
fieldValue877 = x3d.fieldValue()
fieldValue877.name = "translation"
fieldValue877.value = "0.0925000011920929 0.9983000159263611 0.10520000010728836"

ProtoInstance875.fieldValue.append(fieldValue877)

fieldValue817.children.append(ProtoInstance875)
ProtoInstance878 = x3d.ProtoInstance()
ProtoInstance878.name = "Site"
ProtoInstance878.DEF = "hanim_r_iliocristale"
fieldValue879 = x3d.fieldValue()
fieldValue879.name = "name"
fieldValue879.value = "r_iliocristale"

ProtoInstance878.fieldValue.append(fieldValue879)
fieldValue880 = x3d.fieldValue()
fieldValue880.name = "translation"
fieldValue880.value = "-0.1525000035762787 1.0628000497817993 0.0035000001080334187"

ProtoInstance878.fieldValue.append(fieldValue880)

fieldValue817.children.append(ProtoInstance878)
ProtoInstance881 = x3d.ProtoInstance()
ProtoInstance881.name = "Site"
ProtoInstance881.DEF = "hanim_r_trochanterion"
fieldValue882 = x3d.fieldValue()
fieldValue882.name = "name"
fieldValue882.value = "r_trochanterion"

ProtoInstance881.fieldValue.append(fieldValue882)
fieldValue883 = x3d.fieldValue()
fieldValue883.name = "translation"
fieldValue883.value = "-0.1688999980688095 0.8418999910354614 0.03519999980926514"

ProtoInstance881.fieldValue.append(fieldValue883)

fieldValue817.children.append(ProtoInstance881)
ProtoInstance884 = x3d.ProtoInstance()
ProtoInstance884.name = "Site"
ProtoInstance884.DEF = "hanim_l_iliocristale"
fieldValue885 = x3d.fieldValue()
fieldValue885.name = "name"
fieldValue885.value = "l_iliocristale"

ProtoInstance884.fieldValue.append(fieldValue885)
fieldValue886 = x3d.fieldValue()
fieldValue886.name = "translation"
fieldValue886.value = "0.16120000183582306 1.0536999702453613 0.0007999999797903001"

ProtoInstance884.fieldValue.append(fieldValue886)

fieldValue817.children.append(ProtoInstance884)
ProtoInstance887 = x3d.ProtoInstance()
ProtoInstance887.name = "Site"
ProtoInstance887.DEF = "hanim_l_trochanterion"
fieldValue888 = x3d.fieldValue()
fieldValue888.name = "name"
fieldValue888.value = "l_trochanterion"

ProtoInstance887.fieldValue.append(fieldValue888)
fieldValue889 = x3d.fieldValue()
fieldValue889.name = "translation"
fieldValue889.value = "0.16769999265670776 0.8335999846458435 0.030300000682473183"

ProtoInstance887.fieldValue.append(fieldValue889)

fieldValue817.children.append(ProtoInstance887)
ProtoInstance890 = x3d.ProtoInstance()
ProtoInstance890.name = "Site"
ProtoInstance890.DEF = "hanim_cervicale"
fieldValue891 = x3d.fieldValue()
fieldValue891.name = "name"
fieldValue891.value = "cervicale"

ProtoInstance890.fieldValue.append(fieldValue891)
fieldValue892 = x3d.fieldValue()
fieldValue892.name = "translation"
fieldValue892.value = "0.006399999838322401 1.5199999809265137 -0.08150000125169754"

ProtoInstance890.fieldValue.append(fieldValue892)

fieldValue817.children.append(ProtoInstance890)
ProtoInstance893 = x3d.ProtoInstance()
ProtoInstance893.name = "Site"
ProtoInstance893.DEF = "hanim_spine_2_lower_back"
fieldValue894 = x3d.fieldValue()
fieldValue894.name = "name"
fieldValue894.value = "spine_2_lower_back"

ProtoInstance893.fieldValue.append(fieldValue894)
fieldValue895 = x3d.fieldValue()
fieldValue895.name = "translation"
fieldValue895.value = "0.004900000058114529 1.1907999515533447 -0.11129999905824661"

ProtoInstance893.fieldValue.append(fieldValue895)

fieldValue817.children.append(ProtoInstance893)
ProtoInstance896 = x3d.ProtoInstance()
ProtoInstance896.name = "Site"
ProtoInstance896.DEF = "hanim_r_psis"
fieldValue897 = x3d.fieldValue()
fieldValue897.name = "name"
fieldValue897.value = "r_psis"

ProtoInstance896.fieldValue.append(fieldValue897)
fieldValue898 = x3d.fieldValue()
fieldValue898.name = "translation"
fieldValue898.value = "-0.07159999758005142 1.0190000534057617 -0.11379999667406082"

ProtoInstance896.fieldValue.append(fieldValue898)

fieldValue817.children.append(ProtoInstance896)
ProtoInstance899 = x3d.ProtoInstance()
ProtoInstance899.name = "Site"
ProtoInstance899.DEF = "hanim_l_psis"
fieldValue900 = x3d.fieldValue()
fieldValue900.name = "name"
fieldValue900.value = "l_psis"

ProtoInstance899.fieldValue.append(fieldValue900)
fieldValue901 = x3d.fieldValue()
fieldValue901.name = "translation"
fieldValue901.value = "0.07739999890327454 1.0190000534057617 -0.11509999632835388"

ProtoInstance899.fieldValue.append(fieldValue901)

fieldValue817.children.append(ProtoInstance899)
ProtoInstance902 = x3d.ProtoInstance()
ProtoInstance902.name = "Site"
ProtoInstance902.DEF = "hanim_waist_preferred_posterior"
fieldValue903 = x3d.fieldValue()
fieldValue903.name = "name"
fieldValue903.value = "waist_preferred_posterior"

ProtoInstance902.fieldValue.append(fieldValue903)
fieldValue904 = x3d.fieldValue()
fieldValue904.name = "translation"
fieldValue904.value = "0.28999999165534973 1.0915000438690186 -0.10909999907016754"

ProtoInstance902.fieldValue.append(fieldValue904)

fieldValue817.children.append(ProtoInstance902)
ProtoInstance905 = x3d.ProtoInstance()
ProtoInstance905.name = "Site"
ProtoInstance905.DEF = "hanim_r_acromion"
fieldValue906 = x3d.fieldValue()
fieldValue906.name = "name"
fieldValue906.value = "r_acromion"

ProtoInstance905.fieldValue.append(fieldValue906)
fieldValue907 = x3d.fieldValue()
fieldValue907.name = "translation"
fieldValue907.value = "-0.19050000607967377 1.479099988937378 -0.04309999942779541"

ProtoInstance905.fieldValue.append(fieldValue907)

fieldValue817.children.append(ProtoInstance905)
ProtoInstance908 = x3d.ProtoInstance()
ProtoInstance908.name = "Site"
ProtoInstance908.DEF = "hanim_r_axilla_proximal"
fieldValue909 = x3d.fieldValue()
fieldValue909.name = "name"
fieldValue909.value = "r_axilla_proximal"

ProtoInstance908.fieldValue.append(fieldValue909)
fieldValue910 = x3d.fieldValue()
fieldValue910.name = "translation"
fieldValue910.value = "-0.16259999573230743 1.4071999788284302 -0.003100000089034438"

ProtoInstance908.fieldValue.append(fieldValue910)

fieldValue817.children.append(ProtoInstance908)
ProtoInstance911 = x3d.ProtoInstance()
ProtoInstance911.name = "Site"
ProtoInstance911.DEF = "hanim_r_radial_styloid"
fieldValue912 = x3d.fieldValue()
fieldValue912.name = "name"
fieldValue912.value = "r_radial_styloid"

ProtoInstance911.fieldValue.append(fieldValue912)
fieldValue913 = x3d.fieldValue()
fieldValue913.name = "translation"
fieldValue913.value = "-0.188400000333786 0.8676000237464905 -0.035999998450279236"

ProtoInstance911.fieldValue.append(fieldValue913)

fieldValue817.children.append(ProtoInstance911)
ProtoInstance914 = x3d.ProtoInstance()
ProtoInstance914.name = "Site"
ProtoInstance914.DEF = "hanim_r_axilla_distal"
fieldValue915 = x3d.fieldValue()
fieldValue915.name = "name"
fieldValue915.value = "r_axilla_distal"

ProtoInstance914.fieldValue.append(fieldValue915)
fieldValue916 = x3d.fieldValue()
fieldValue916.name = "translation"
fieldValue916.value = "-0.16030000150203705 1.4098000526428223 -0.08259999752044678"

ProtoInstance914.fieldValue.append(fieldValue916)

fieldValue817.children.append(ProtoInstance914)
ProtoInstance917 = x3d.ProtoInstance()
ProtoInstance917.name = "Site"
ProtoInstance917.DEF = "hanim_r_olecranon"
fieldValue918 = x3d.fieldValue()
fieldValue918.name = "name"
fieldValue918.value = "r_olecranon"

ProtoInstance917.fieldValue.append(fieldValue918)
fieldValue919 = x3d.fieldValue()
fieldValue919.name = "translation"
fieldValue919.value = "-0.1906999945640564 1.1404999494552612 -0.10649999976158142"

ProtoInstance917.fieldValue.append(fieldValue919)

fieldValue817.children.append(ProtoInstance917)
ProtoInstance920 = x3d.ProtoInstance()
ProtoInstance920.name = "Site"
ProtoInstance920.DEF = "hanim_r_humeral_lateral_epicondyles"
fieldValue921 = x3d.fieldValue()
fieldValue921.name = "name"
fieldValue921.value = "r_humeral_lateral_epicondyles"

ProtoInstance920.fieldValue.append(fieldValue921)
fieldValue922 = x3d.fieldValue()
fieldValue922.name = "translation"
fieldValue922.value = "-0.2223999947309494 1.1517000198364258 -0.10329999774694443"

ProtoInstance920.fieldValue.append(fieldValue922)

fieldValue817.children.append(ProtoInstance920)
ProtoInstance923 = x3d.ProtoInstance()
ProtoInstance923.name = "Site"
ProtoInstance923.DEF = "hanim_r_humeral_medial_epicondyles"
fieldValue924 = x3d.fieldValue()
fieldValue924.name = "name"
fieldValue924.value = "r_humeral_medial_epicondyles"

ProtoInstance923.fieldValue.append(fieldValue924)
fieldValue925 = x3d.fieldValue()
fieldValue925.name = "translation"
fieldValue925.value = "-0.1679999977350235 1.1297999620437622 -0.10620000213384628"

ProtoInstance923.fieldValue.append(fieldValue925)

fieldValue817.children.append(ProtoInstance923)
ProtoInstance926 = x3d.ProtoInstance()
ProtoInstance926.name = "Site"
ProtoInstance926.DEF = "hanim_r_radiale"
fieldValue927 = x3d.fieldValue()
fieldValue927.name = "name"
fieldValue927.value = "r_radiale"

ProtoInstance926.fieldValue.append(fieldValue927)
fieldValue928 = x3d.fieldValue()
fieldValue928.name = "translation"
fieldValue928.value = "-0.21299999952316284 1.1304999589920044 -0.10909999907016754"

ProtoInstance926.fieldValue.append(fieldValue928)

fieldValue817.children.append(ProtoInstance926)
ProtoInstance929 = x3d.ProtoInstance()
ProtoInstance929.name = "Site"
ProtoInstance929.DEF = "hanim_r_metacarpal_phalanx_2"
fieldValue930 = x3d.fieldValue()
fieldValue930.name = "name"
fieldValue930.value = "r_metacarpal_phalanx_2"

ProtoInstance929.fieldValue.append(fieldValue930)
fieldValue931 = x3d.fieldValue()
fieldValue931.name = "translation"
fieldValue931.value = "-0.19769999384880066 0.8169000148773193 -0.01769999973475933"

ProtoInstance929.fieldValue.append(fieldValue931)

fieldValue817.children.append(ProtoInstance929)
ProtoInstance932 = x3d.ProtoInstance()
ProtoInstance932.name = "Site"
ProtoInstance932.DEF = "hanim_r_dactylion"
fieldValue933 = x3d.fieldValue()
fieldValue933.name = "name"
fieldValue933.value = "r_dactylion"

ProtoInstance932.fieldValue.append(fieldValue933)
fieldValue934 = x3d.fieldValue()
fieldValue934.name = "translation"
fieldValue934.value = "-0.1941000074148178 0.6772000193595886 -0.04230000078678131"

ProtoInstance932.fieldValue.append(fieldValue934)

fieldValue817.children.append(ProtoInstance932)
ProtoInstance935 = x3d.ProtoInstance()
ProtoInstance935.name = "Site"
ProtoInstance935.DEF = "hanim_r_ulnar_styloid"
fieldValue936 = x3d.fieldValue()
fieldValue936.name = "name"
fieldValue936.value = "r_ulnar_styloid"

ProtoInstance935.fieldValue.append(fieldValue936)
fieldValue937 = x3d.fieldValue()
fieldValue937.name = "translation"
fieldValue937.value = "-0.21170000731945038 0.8561999797821045 -0.058400001376867294"

ProtoInstance935.fieldValue.append(fieldValue937)

fieldValue817.children.append(ProtoInstance935)
ProtoInstance938 = x3d.ProtoInstance()
ProtoInstance938.name = "Site"
ProtoInstance938.DEF = "hanim_r_metacarpal_phalanx_5"
fieldValue939 = x3d.fieldValue()
fieldValue939.name = "name"
fieldValue939.value = "r_metacarpal_phalanx_5"

ProtoInstance938.fieldValue.append(fieldValue939)
fieldValue940 = x3d.fieldValue()
fieldValue940.name = "translation"
fieldValue940.value = "-0.19290000200271606 0.7889999747276306 -0.10639999806880951"

ProtoInstance938.fieldValue.append(fieldValue940)

fieldValue817.children.append(ProtoInstance938)
ProtoInstance941 = x3d.ProtoInstance()
ProtoInstance941.name = "Site"
ProtoInstance941.DEF = "hanim_l_acromion"
fieldValue942 = x3d.fieldValue()
fieldValue942.name = "name"
fieldValue942.value = "l_acromion"

ProtoInstance941.fieldValue.append(fieldValue942)
fieldValue943 = x3d.fieldValue()
fieldValue943.name = "translation"
fieldValue943.value = "0.20319999754428864 1.4759999513626099 -0.04899999871850014"

ProtoInstance941.fieldValue.append(fieldValue943)

fieldValue817.children.append(ProtoInstance941)
ProtoInstance944 = x3d.ProtoInstance()
ProtoInstance944.name = "Site"
ProtoInstance944.DEF = "hanim_l_axilla_proximal"
fieldValue945 = x3d.fieldValue()
fieldValue945.name = "name"
fieldValue945.value = "l_axilla_proximal"

ProtoInstance944.fieldValue.append(fieldValue945)
fieldValue946 = x3d.fieldValue()
fieldValue946.name = "translation"
fieldValue946.value = "0.1776999980211258 1.406499981880188 -0.007499999832361937"

ProtoInstance944.fieldValue.append(fieldValue946)

fieldValue817.children.append(ProtoInstance944)
ProtoInstance947 = x3d.ProtoInstance()
ProtoInstance947.name = "Site"
ProtoInstance947.DEF = "hanim_l_radial_styloid"
fieldValue948 = x3d.fieldValue()
fieldValue948.name = "name"
fieldValue948.value = "l_radial_styloid"

ProtoInstance947.fieldValue.append(fieldValue948)
fieldValue949 = x3d.fieldValue()
fieldValue949.name = "translation"
fieldValue949.value = "0.19009999930858612 0.8644999861717224 -0.04149999842047691"

ProtoInstance947.fieldValue.append(fieldValue949)

fieldValue817.children.append(ProtoInstance947)
ProtoInstance950 = x3d.ProtoInstance()
ProtoInstance950.name = "Site"
ProtoInstance950.DEF = "hanim_l_axilla_distal"
fieldValue951 = x3d.fieldValue()
fieldValue951.name = "name"
fieldValue951.value = "l_axilla_distal"

ProtoInstance950.fieldValue.append(fieldValue951)
fieldValue952 = x3d.fieldValue()
fieldValue952.name = "translation"
fieldValue952.value = "0.17059999704360962 1.4071999788284302 -0.08749999850988388"

ProtoInstance950.fieldValue.append(fieldValue952)

fieldValue817.children.append(ProtoInstance950)
ProtoInstance953 = x3d.ProtoInstance()
ProtoInstance953.name = "Site"
ProtoInstance953.DEF = "hanim_l_olecranon"
fieldValue954 = x3d.fieldValue()
fieldValue954.name = "name"
fieldValue954.value = "l_olecranon"

ProtoInstance953.fieldValue.append(fieldValue954)
fieldValue955 = x3d.fieldValue()
fieldValue955.name = "translation"
fieldValue955.value = "-0.19619999825954437 1.1375000476837158 -0.11230000108480453"

ProtoInstance953.fieldValue.append(fieldValue955)

fieldValue817.children.append(ProtoInstance953)
ProtoInstance956 = x3d.ProtoInstance()
ProtoInstance956.name = "Site"
ProtoInstance956.DEF = "hanim_l_humeral_lateral_epicondyles"
fieldValue957 = x3d.fieldValue()
fieldValue957.name = "name"
fieldValue957.value = "l_humeral_lateral_epicondyles"

ProtoInstance956.fieldValue.append(fieldValue957)
fieldValue958 = x3d.fieldValue()
fieldValue958.name = "translation"
fieldValue958.value = "0.2280000001192093 1.1482000350952148 -0.10999999940395355"

ProtoInstance956.fieldValue.append(fieldValue958)

fieldValue817.children.append(ProtoInstance956)
ProtoInstance959 = x3d.ProtoInstance()
ProtoInstance959.name = "Site"
ProtoInstance959.DEF = "hanim_l_humeral_medial_epicondyles"
fieldValue960 = x3d.fieldValue()
fieldValue960.name = "name"
fieldValue960.value = "l_humeral_medial_epicondyles"

ProtoInstance959.fieldValue.append(fieldValue960)
fieldValue961 = x3d.fieldValue()
fieldValue961.name = "translation"
fieldValue961.value = "0.17350000143051147 1.1272000074386597 -0.11129999905824661"

ProtoInstance959.fieldValue.append(fieldValue961)

fieldValue817.children.append(ProtoInstance959)
ProtoInstance962 = x3d.ProtoInstance()
ProtoInstance962.name = "Site"
ProtoInstance962.DEF = "hanim_l_radiale"
fieldValue963 = x3d.fieldValue()
fieldValue963.name = "name"
fieldValue963.value = "l_radiale"

ProtoInstance962.fieldValue.append(fieldValue963)
fieldValue964 = x3d.fieldValue()
fieldValue964.name = "translation"
fieldValue964.value = "0.21819999814033508 1.1211999654769897 -0.11670000106096268"

ProtoInstance962.fieldValue.append(fieldValue964)

fieldValue817.children.append(ProtoInstance962)
ProtoInstance965 = x3d.ProtoInstance()
ProtoInstance965.name = "Site"
ProtoInstance965.DEF = "hanim_l_metacarpal_phalanx_2"
fieldValue966 = x3d.fieldValue()
fieldValue966.name = "name"
fieldValue966.value = "l_metacarpal_phalanx_2"

ProtoInstance965.fieldValue.append(fieldValue966)
fieldValue967 = x3d.fieldValue()
fieldValue967.name = "translation"
fieldValue967.value = "0.20090000331401825 0.8138999938964844 -0.02370000071823597"

ProtoInstance965.fieldValue.append(fieldValue967)

fieldValue817.children.append(ProtoInstance965)
ProtoInstance968 = x3d.ProtoInstance()
ProtoInstance968.name = "Site"
ProtoInstance968.DEF = "hanim_l_dactylion"
fieldValue969 = x3d.fieldValue()
fieldValue969.name = "name"
fieldValue969.value = "l_dactylion"

ProtoInstance968.fieldValue.append(fieldValue969)
fieldValue970 = x3d.fieldValue()
fieldValue970.name = "translation"
fieldValue970.value = "0.20559999346733093 0.6743000149726868 -0.04820000007748604"

ProtoInstance968.fieldValue.append(fieldValue970)

fieldValue817.children.append(ProtoInstance968)
ProtoInstance971 = x3d.ProtoInstance()
ProtoInstance971.name = "Site"
ProtoInstance971.DEF = "hanim_l_ulnar_styloid"
fieldValue972 = x3d.fieldValue()
fieldValue972.name = "name"
fieldValue972.value = "l_ulnar_styloid"

ProtoInstance971.fieldValue.append(fieldValue972)
fieldValue973 = x3d.fieldValue()
fieldValue973.name = "translation"
fieldValue973.value = "-0.2142000049352646 0.8529000282287598 -0.06480000168085098"

ProtoInstance971.fieldValue.append(fieldValue973)

fieldValue817.children.append(ProtoInstance971)
ProtoInstance974 = x3d.ProtoInstance()
ProtoInstance974.name = "Site"
ProtoInstance974.DEF = "hanim_l_metacarpal_phalanx_5"
fieldValue975 = x3d.fieldValue()
fieldValue975.name = "name"
fieldValue975.value = "l_metacarpal_phalanx_5"

ProtoInstance974.fieldValue.append(fieldValue975)
fieldValue976 = x3d.fieldValue()
fieldValue976.name = "translation"
fieldValue976.value = "0.19290000200271606 0.7860000133514404 -0.11219999939203262"

ProtoInstance974.fieldValue.append(fieldValue976)

fieldValue817.children.append(ProtoInstance974)
ProtoInstance977 = x3d.ProtoInstance()
ProtoInstance977.name = "Site"
ProtoInstance977.DEF = "hanim_r_knee_crease"
fieldValue978 = x3d.fieldValue()
fieldValue978.name = "name"
fieldValue978.value = "r_knee_crease"

ProtoInstance977.fieldValue.append(fieldValue978)
fieldValue979 = x3d.fieldValue()
fieldValue979.name = "translation"
fieldValue979.value = "-0.08250000327825546 0.49320000410079956 -0.032600000500679016"

ProtoInstance977.fieldValue.append(fieldValue979)

fieldValue817.children.append(ProtoInstance977)
ProtoInstance980 = x3d.ProtoInstance()
ProtoInstance980.name = "Site"
ProtoInstance980.DEF = "hanim_r_femoral_lateral_epicondyles"
fieldValue981 = x3d.fieldValue()
fieldValue981.name = "name"
fieldValue981.value = "r_femoral_lateral_epicondyles"

ProtoInstance980.fieldValue.append(fieldValue981)
fieldValue982 = x3d.fieldValue()
fieldValue982.name = "translation"
fieldValue982.value = "-0.1421000063419342 0.4991999864578247 0.03099999949336052"

ProtoInstance980.fieldValue.append(fieldValue982)

fieldValue817.children.append(ProtoInstance980)
ProtoInstance983 = x3d.ProtoInstance()
ProtoInstance983.name = "Site"
ProtoInstance983.DEF = "hanim_r_femoral_medial_epicondyles"
fieldValue984 = x3d.fieldValue()
fieldValue984.name = "name"
fieldValue984.value = "r_femoral_lateral_epicondyles"

ProtoInstance983.fieldValue.append(fieldValue984)
fieldValue985 = x3d.fieldValue()
fieldValue985.name = "translation"
fieldValue985.value = "-0.022099999710917473 0.5013999938964844 0.02889999933540821"

ProtoInstance983.fieldValue.append(fieldValue985)

fieldValue817.children.append(ProtoInstance983)
ProtoInstance986 = x3d.ProtoInstance()
ProtoInstance986.name = "Site"
ProtoInstance986.DEF = "hanim_r_tarsal_interphalangeal_phalanx_5"
fieldValue987 = x3d.fieldValue()
fieldValue987.name = "name"
fieldValue987.value = "r_tarsal_interphalangeal_phalanx_5"

ProtoInstance986.fieldValue.append(fieldValue987)
fieldValue988 = x3d.fieldValue()
fieldValue988.name = "translation"
fieldValue988.value = "-0.15230000019073486 0.016599999740719795 0.08950000256299973"

ProtoInstance986.fieldValue.append(fieldValue988)

fieldValue817.children.append(ProtoInstance986)
ProtoInstance989 = x3d.ProtoInstance()
ProtoInstance989.name = "Site"
ProtoInstance989.DEF = "hanim_r_lateral_malleolus"
fieldValue990 = x3d.fieldValue()
fieldValue990.name = "name"
fieldValue990.value = "r_lateral_malleolus"

ProtoInstance989.fieldValue.append(fieldValue990)
fieldValue991 = x3d.fieldValue()
fieldValue991.name = "translation"
fieldValue991.value = "-0.1005999967455864 0.0658000037074089 -0.10750000178813934"

ProtoInstance989.fieldValue.append(fieldValue991)

fieldValue817.children.append(ProtoInstance989)
ProtoInstance992 = x3d.ProtoInstance()
ProtoInstance992.name = "Site"
ProtoInstance992.DEF = "hanim_r_medial_malleolus"
fieldValue993 = x3d.fieldValue()
fieldValue993.name = "name"
fieldValue993.value = "r_medial_malleolus"

ProtoInstance992.fieldValue.append(fieldValue993)
fieldValue994 = x3d.fieldValue()
fieldValue994.name = "translation"
fieldValue994.value = "-0.05909999832510948 0.07599999755620956 -0.09279999881982803"

ProtoInstance992.fieldValue.append(fieldValue994)

fieldValue817.children.append(ProtoInstance992)
ProtoInstance995 = x3d.ProtoInstance()
ProtoInstance995.name = "Site"
ProtoInstance995.DEF = "hanim_r_sphyrion"
fieldValue996 = x3d.fieldValue()
fieldValue996.name = "name"
fieldValue996.value = "r_sphyrion"

ProtoInstance995.fieldValue.append(fieldValue996)
fieldValue997 = x3d.fieldValue()
fieldValue997.name = "translation"
fieldValue997.value = "-0.06030000001192093 0.061000000685453415 -0.10019999742507935"

ProtoInstance995.fieldValue.append(fieldValue997)

fieldValue817.children.append(ProtoInstance995)
ProtoInstance998 = x3d.ProtoInstance()
ProtoInstance998.name = "Site"
ProtoInstance998.DEF = "hanim_r_tarsal_interphalangeal_phalanx_1"
fieldValue999 = x3d.fieldValue()
fieldValue999.name = "name"
fieldValue999.value = "r_tarsal_interphalangeal_phalanx_1"

ProtoInstance998.fieldValue.append(fieldValue999)
fieldValue1000 = x3d.fieldValue()
fieldValue1000.name = "translation"
fieldValue1000.value = "-0.05209999904036522 0.026000000536441803 0.01269999984651804"

ProtoInstance998.fieldValue.append(fieldValue1000)

fieldValue817.children.append(ProtoInstance998)
ProtoInstance1001 = x3d.ProtoInstance()
ProtoInstance1001.name = "Site"
ProtoInstance1001.DEF = "hanim_r_calcaneus_posterior"
fieldValue1002 = x3d.fieldValue()
fieldValue1002.name = "name"
fieldValue1002.value = "r_calcaneus_posterior"

ProtoInstance1001.fieldValue.append(fieldValue1002)
fieldValue1003 = x3d.fieldValue()
fieldValue1003.name = "translation"
fieldValue1003.value = "-0.06920000165700912 0.02969999983906746 -0.12210000306367874"

ProtoInstance1001.fieldValue.append(fieldValue1003)

fieldValue817.children.append(ProtoInstance1001)
ProtoInstance1004 = x3d.ProtoInstance()
ProtoInstance1004.name = "Site"
ProtoInstance1004.DEF = "hanim_r_tarsal_distal_phalanx_2"
fieldValue1005 = x3d.fieldValue()
fieldValue1005.name = "name"
fieldValue1005.value = "r_tarsal_distal_phalanx_2"

ProtoInstance1004.fieldValue.append(fieldValue1005)
fieldValue1006 = x3d.fieldValue()
fieldValue1006.name = "translation"
fieldValue1006.value = "-0.08829999715089798 0.013399999588727951 0.13830000162124634"

ProtoInstance1004.fieldValue.append(fieldValue1006)

fieldValue817.children.append(ProtoInstance1004)
ProtoInstance1007 = x3d.ProtoInstance()
ProtoInstance1007.name = "Site"
ProtoInstance1007.DEF = "hanim_l_knee_crease"
fieldValue1008 = x3d.fieldValue()
fieldValue1008.name = "name"
fieldValue1008.value = "l_knee_crease"

ProtoInstance1007.fieldValue.append(fieldValue1008)
fieldValue1009 = x3d.fieldValue()
fieldValue1009.name = "translation"
fieldValue1009.value = "0.09929999709129333 0.48809999227523804 -0.030899999663233757"

ProtoInstance1007.fieldValue.append(fieldValue1009)

fieldValue817.children.append(ProtoInstance1007)
ProtoInstance1010 = x3d.ProtoInstance()
ProtoInstance1010.name = "Site"
ProtoInstance1010.DEF = "hanim_l_femoral_lateral_epicondyles"
fieldValue1011 = x3d.fieldValue()
fieldValue1011.name = "name"
fieldValue1011.value = "l_femoral_lateral_epicondyles"

ProtoInstance1010.fieldValue.append(fieldValue1011)
fieldValue1012 = x3d.fieldValue()
fieldValue1012.name = "translation"
fieldValue1012.value = "0.1597999930381775 0.4966999888420105 0.02969999983906746"

ProtoInstance1010.fieldValue.append(fieldValue1012)

fieldValue817.children.append(ProtoInstance1010)
ProtoInstance1013 = x3d.ProtoInstance()
ProtoInstance1013.name = "Site"
ProtoInstance1013.DEF = "hanim_l_femoral_medial_epicondyles"
fieldValue1014 = x3d.fieldValue()
fieldValue1014.name = "name"
fieldValue1014.value = "l_femoral_lateral_epicondyles"

ProtoInstance1013.fieldValue.append(fieldValue1014)
fieldValue1015 = x3d.fieldValue()
fieldValue1015.name = "translation"
fieldValue1015.value = "0.039799999445676804 0.49459999799728394 0.030300000682473183"

ProtoInstance1013.fieldValue.append(fieldValue1015)

fieldValue817.children.append(ProtoInstance1013)
ProtoInstance1016 = x3d.ProtoInstance()
ProtoInstance1016.name = "Site"
ProtoInstance1016.DEF = "hanim_l_tarsal_interphalangeal_phalanx_5"
fieldValue1017 = x3d.fieldValue()
fieldValue1017.name = "name"
fieldValue1017.value = "l_tarsal_interphalangeal_phalanx_5"

ProtoInstance1016.fieldValue.append(fieldValue1017)
fieldValue1018 = x3d.fieldValue()
fieldValue1018.name = "translation"
fieldValue1018.value = "0.18250000476837158 0.007000000216066837 0.09279999881982803"

ProtoInstance1016.fieldValue.append(fieldValue1018)

fieldValue817.children.append(ProtoInstance1016)
ProtoInstance1019 = x3d.ProtoInstance()
ProtoInstance1019.name = "Site"
ProtoInstance1019.DEF = "hanim_l_lateral_malleolus"
fieldValue1020 = x3d.fieldValue()
fieldValue1020.name = "name"
fieldValue1020.value = "l_lateral_malleolus"

ProtoInstance1019.fieldValue.append(fieldValue1020)
fieldValue1021 = x3d.fieldValue()
fieldValue1021.name = "translation"
fieldValue1021.value = "0.13079999387264252 0.059700001031160355 -0.10320000350475311"

ProtoInstance1019.fieldValue.append(fieldValue1021)

fieldValue817.children.append(ProtoInstance1019)
ProtoInstance1022 = x3d.ProtoInstance()
ProtoInstance1022.name = "Site"
ProtoInstance1022.DEF = "hanim_l_medial_malleolus"
fieldValue1023 = x3d.fieldValue()
fieldValue1023.name = "name"
fieldValue1023.value = "l_medial_malleolus"

ProtoInstance1022.fieldValue.append(fieldValue1023)
fieldValue1024 = x3d.fieldValue()
fieldValue1024.name = "translation"
fieldValue1024.value = "0.08900000154972076 0.07159999758005142 -0.08810000121593475"

ProtoInstance1022.fieldValue.append(fieldValue1024)

fieldValue817.children.append(ProtoInstance1022)
ProtoInstance1025 = x3d.ProtoInstance()
ProtoInstance1025.name = "Site"
ProtoInstance1025.DEF = "hanim_l_sphyrion"
fieldValue1026 = x3d.fieldValue()
fieldValue1026.name = "name"
fieldValue1026.value = "l_sphyrion"

ProtoInstance1025.fieldValue.append(fieldValue1026)
fieldValue1027 = x3d.fieldValue()
fieldValue1027.name = "translation"
fieldValue1027.value = "0.08900000154972076 0.057500001043081284 -0.09430000185966492"

ProtoInstance1025.fieldValue.append(fieldValue1027)

fieldValue817.children.append(ProtoInstance1025)
ProtoInstance1028 = x3d.ProtoInstance()
ProtoInstance1028.name = "Site"
ProtoInstance1028.DEF = "hanim_l_tarsal_interphalangeal_phalanx_1"
fieldValue1029 = x3d.fieldValue()
fieldValue1029.name = "name"
fieldValue1029.value = "l_tarsal_interphalangeal_phalanx_1"

ProtoInstance1028.fieldValue.append(fieldValue1029)
fieldValue1030 = x3d.fieldValue()
fieldValue1030.name = "translation"
fieldValue1030.value = "0.08160000294446945 0.02319999970495701 0.010599999688565731"

ProtoInstance1028.fieldValue.append(fieldValue1030)

fieldValue817.children.append(ProtoInstance1028)
ProtoInstance1031 = x3d.ProtoInstance()
ProtoInstance1031.name = "Site"
ProtoInstance1031.DEF = "hanim_l_calcaneus_posterior"
fieldValue1032 = x3d.fieldValue()
fieldValue1032.name = "name"
fieldValue1032.value = "l_calcaneus_posterior"

ProtoInstance1031.fieldValue.append(fieldValue1032)
fieldValue1033 = x3d.fieldValue()
fieldValue1033.name = "translation"
fieldValue1033.value = "0.09740000218153 0.02590000070631504 -0.11710000038146973"

ProtoInstance1031.fieldValue.append(fieldValue1033)

fieldValue817.children.append(ProtoInstance1031)
ProtoInstance1034 = x3d.ProtoInstance()
ProtoInstance1034.name = "Site"
ProtoInstance1034.DEF = "hanim_l_tarsal_distal_phalanx_2"
fieldValue1035 = x3d.fieldValue()
fieldValue1035.name = "name"
fieldValue1035.value = "l_tarsal_distal_phalanx_2"

ProtoInstance1034.fieldValue.append(fieldValue1035)
fieldValue1036 = x3d.fieldValue()
fieldValue1036.name = "translation"
fieldValue1036.value = "0.11949999630451202 0.007899999618530273 0.14329999685287476"

ProtoInstance1034.fieldValue.append(fieldValue1036)

fieldValue817.children.append(ProtoInstance1034)
ProtoInstance1037 = x3d.ProtoInstance()
ProtoInstance1037.name = "Site"
ProtoInstance1037.DEF = "hanim_crotch"
fieldValue1038 = x3d.fieldValue()
fieldValue1038.name = "name"
fieldValue1038.value = "crotch"

ProtoInstance1037.fieldValue.append(fieldValue1038)
fieldValue1039 = x3d.fieldValue()
fieldValue1039.name = "translation"
fieldValue1039.value = "0.0034000000450760126 0.8266000151634216 0.025699999183416367"

ProtoInstance1037.fieldValue.append(fieldValue1039)

fieldValue817.children.append(ProtoInstance1037)
ProtoInstance1040 = x3d.ProtoInstance()
ProtoInstance1040.name = "Site"
ProtoInstance1040.DEF = "hanim_r_neck_base"
fieldValue1041 = x3d.fieldValue()
fieldValue1041.name = "name"
fieldValue1041.value = "r_neck_base"

ProtoInstance1040.fieldValue.append(fieldValue1041)
fieldValue1042 = x3d.fieldValue()
fieldValue1042.name = "translation"
fieldValue1042.value = "-0.04190000146627426 1.5148999691009521 -0.02199999988079071"

ProtoInstance1040.fieldValue.append(fieldValue1042)

fieldValue817.children.append(ProtoInstance1040)
ProtoInstance1043 = x3d.ProtoInstance()
ProtoInstance1043.name = "Site"
ProtoInstance1043.DEF = "hanim_l_neck_base"
fieldValue1044 = x3d.fieldValue()
fieldValue1044.name = "name"
fieldValue1044.value = "l_neck_base"

ProtoInstance1043.fieldValue.append(fieldValue1044)
fieldValue1045 = x3d.fieldValue()
fieldValue1045.name = "translation"
fieldValue1045.value = "0.06459999829530716 1.5140999555587769 -0.03799999877810478"

ProtoInstance1043.fieldValue.append(fieldValue1045)

fieldValue817.children.append(ProtoInstance1043)
ProtoInstance1046 = x3d.ProtoInstance()
ProtoInstance1046.name = "Site"
ProtoInstance1046.DEF = "hanim_navel"
fieldValue1047 = x3d.fieldValue()
fieldValue1047.name = "name"
fieldValue1047.value = "navel"

ProtoInstance1046.fieldValue.append(fieldValue1047)
fieldValue1048 = x3d.fieldValue()
fieldValue1048.name = "translation"
fieldValue1048.value = "0.006899999920278788 1.09660005569458 0.10170000046491623"

ProtoInstance1046.fieldValue.append(fieldValue1048)

fieldValue817.children.append(ProtoInstance1046)

ProtoInstance101.fieldValue.append(fieldValue817)
fieldValue1049 = x3d.fieldValue()
fieldValue1049.name = "name"
fieldValue1049.value = "humanoid"

ProtoInstance101.fieldValue.append(fieldValue1049)
fieldValue1050 = x3d.fieldValue()
fieldValue1050.name = "info"
fieldValue1050.value = "\"authorName=Matthew T. Beitler\" \"authorEmail=beitler@graphics.cis.upenn.edu or beitler@acm.org\" \"creationDate=05/12/99\" \"copyright=Copyright 1999-2003, Matthew T. Beitler\" \"humanoidVersion=JointCenters 200x, LOA0\" \"usageRestrictions= PERMISSION TO FULLY USE THIS SCENE GRAPH IS GRANTED, PROVIDED THIS COPYRIGHT INFORMATION AND DOCUMENTATION OF THE ORIGINAL AUTHOR IS INCLUDED. This humanoid scene graph is provided 'as-is' and without warranty of any kind, express, implied or otherwise, including without limitation, any warranty of merchantability or fitness for a particular purpose.\" \"modificationDate=08/12/03\""

ProtoInstance101.fieldValue.append(fieldValue1050)

Scene4.children.append(ProtoInstance101)
Group1051 = x3d.Group()
Group1051.DEF = "JointCenters_WorldInfo"
WorldInfo1052 = x3d.WorldInfo()
WorldInfo1052.title = "HANIM 200x Default Joint Centers, LOA&#8209;0"
WorldInfo1052.info = [" HANIM 200x Default Joint Centers, Level-Of-Articulation 0 --------------------------------------------------------- HANIM 200x (VRML97) Author name: eMpTy (a.k.a. Matthew T. Beitler) HANIM 200x (VRML97) Author email: beitler@cis.upenn.edu or beitler@acm.org HANIM 200x (VRML97) Author homepage: http://www.cis.upenn.edu/~beitler HANIM 200x (VRML97) Compliance Date: August 12, 2003 HANIM 200x Compliance Information: http://H-Anim.org/Specifications/H-Anim200x Construction Info (joint centers): The joint centers of this figure are based on the work of Norman Badler, director of the Center for Human modelling and Simulation at the University of Pennsylvania. The original document which these joint centers are based on can be found at: http://www.cis.upenn.edu/~badler/anthro/89-71.ps "]

Group1051.children.append(WorldInfo1052)

Scene4.children.append(Group1051)
NavigationInfo1053 = x3d.NavigationInfo()
NavigationInfo1053.avatarSize = [0.25,1.600000023841858,0.75]
NavigationInfo1053.speed = 1.5

Scene4.children.append(NavigationInfo1053)

X3D0.Scene = Scene4
f = open("././foo_RoundTrip.x3d", "w")
f.write(X3D0.XML())
f.close()
