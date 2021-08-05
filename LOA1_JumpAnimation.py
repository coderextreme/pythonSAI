from x3dpsail import *
X3D0 = X3D()
X3D0.setProfile("Immersive")
X3D0.setVersion("3.3")
head1 = head()
meta2 = meta()
meta2.setName("title")
meta2.setContent("LOA1_JumpAnimation.x3d")

head1.addMeta(meta2)
meta3 = meta()
meta3.setName("description")
meta3.setContent("Humanoid animation prototype reusable by any Humanoid.")

head1.addMeta(meta3)
meta4 = meta()
meta4.setName("creator")
meta4.setContent("Cindy Ballreich cindy@ballreich.net 3Name3D")

head1.addMeta(meta4)
meta5 = meta()
meta5.setName("rights")
meta5.setContent("1997 3Name3D / Yglesias, Wallock, Divekar, Inc., all rights reserved.")

head1.addMeta(meta5)
meta6 = meta()
meta6.setName("translator")
meta6.setContent("Scott Tufts")

head1.addMeta(meta6)
meta7 = meta()
meta7.setName("translated")
meta7.setContent("1 December 2001")

head1.addMeta(meta7)
meta8 = meta()
meta8.setName("modified")
meta8.setContent("23 May 2020")

head1.addMeta(meta8)
meta9 = meta()
meta9.setName("reference")
meta9.setContent("http://www.ballreich.net/vrml/HAnim/nancy_HAnim.wrl")

head1.addMeta(meta9)
meta10 = meta()
meta10.setName("reference")
meta10.setContent("http://www.HAnim.org")

head1.addMeta(meta10)
meta11 = meta()
meta11.setName("reference")
meta11.setContent("http://HAnim.org/Models")

head1.addMeta(meta11)
meta12 = meta()
meta12.setName("reference")
meta12.setContent("http://HAnim.org/Nodes")

head1.addMeta(meta12)
meta13 = meta()
meta13.setName("subject")
meta13.setContent("InterchangableActorsViaDynamicRouting Nancy jump Animation HAnim 2001")

head1.addMeta(meta13)
meta14 = meta()
meta14.setName("identifier")
meta14.setContent("https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Prototypes/LOA1_JumpAnimation.x3d")

head1.addMeta(meta14)
meta15 = meta()
meta15.setName("generator")
meta15.setContent("X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit")

head1.addMeta(meta15)
meta16 = meta()
meta16.setName("license")
meta16.setContent("../license.html")

head1.addMeta(meta16)

X3D0.setHead(head1)
Scene17 = Scene()
WorldInfo18 = WorldInfo()
WorldInfo18.setTitle("LOA1_JumpAnimation.x3d")

Scene17.addChildren(WorldInfo18)
ProtoDeclare19 = ProtoDeclare()
ProtoDeclare19.setName("LOA1_JumpAnimation")
ProtoInterface20 = ProtoInterface()
field21 = field()
field21.setName("cycleInterval")
field21.setAccessType("inputOutput")
field21.setType("SFTime")
field21.setValue("2")

ProtoInterface20.addField(field21)
field22 = field()
field22.setName("enabled")
field22.setAccessType("inputOutput")
field22.setType("SFBool")
field22.setValue("true")

ProtoInterface20.addField(field22)
field23 = field()
field23.setName("loop")
field23.setAccessType("inputOutput")
field23.setType("SFBool")
field23.setValue("true")

ProtoInterface20.addField(field23)
field24 = field()
field24.setName("startTime")
field24.setAccessType("inputOutput")
field24.setType("SFTime")
field24.setValue("0")

ProtoInterface20.addField(field24)
field25 = field()
field25.setName("stopTime")
field25.setAccessType("inputOutput")
field25.setType("SFTime")
field25.setValue("-1")

ProtoInterface20.addField(field25)
field26 = field()
field26.setName("fraction_changed")
field26.setAccessType("outputOnly")
field26.setType("SFFloat")

ProtoInterface20.addField(field26)
field27 = field()
field27.setName("isActive")
field27.setAccessType("outputOnly")
field27.setType("SFBool")

ProtoInterface20.addField(field27)
field28 = field()
field28.setName("HumanoidRoot_translation_changed")
field28.setAccessType("outputOnly")
field28.setType("SFVec3f")

ProtoInterface20.addField(field28)
field29 = field()
field29.setName("HumanoidRoot_rotation_changed")
field29.setAccessType("outputOnly")
field29.setType("SFRotation")

ProtoInterface20.addField(field29)
field30 = field()
field30.setName("lower_body_rotation_changed")
field30.setAccessType("outputOnly")
field30.setType("SFRotation")

ProtoInterface20.addField(field30)
field31 = field()
field31.setName("l_hip_rotation_changed")
field31.setAccessType("outputOnly")
field31.setType("SFRotation")

ProtoInterface20.addField(field31)
field32 = field()
field32.setName("l_knee_rotation_changed")
field32.setAccessType("outputOnly")
field32.setType("SFRotation")

ProtoInterface20.addField(field32)
field33 = field()
field33.setName("l_ankle_rotation_changed")
field33.setAccessType("outputOnly")
field33.setType("SFRotation")

ProtoInterface20.addField(field33)
field34 = field()
field34.setName("l_midtarsal_rotation_changed")
field34.setAccessType("outputOnly")
field34.setType("SFRotation")

ProtoInterface20.addField(field34)
field35 = field()
field35.setName("r_hip_rotation_changed")
field35.setAccessType("outputOnly")
field35.setType("SFRotation")

ProtoInterface20.addField(field35)
field36 = field()
field36.setName("r_knee_rotation_changed")
field36.setAccessType("outputOnly")
field36.setType("SFRotation")

ProtoInterface20.addField(field36)
field37 = field()
field37.setName("r_ankle_rotation_changed")
field37.setAccessType("outputOnly")
field37.setType("SFRotation")

ProtoInterface20.addField(field37)
field38 = field()
field38.setName("r_midtarsal_rotation_changed")
field38.setAccessType("outputOnly")
field38.setType("SFRotation")

ProtoInterface20.addField(field38)
field39 = field()
field39.setName("vl5_rotation_changed")
field39.setAccessType("outputOnly")
field39.setType("SFRotation")

ProtoInterface20.addField(field39)
field40 = field()
field40.setName("skullbase_rotation_changed")
field40.setAccessType("outputOnly")
field40.setType("SFRotation")

ProtoInterface20.addField(field40)
field41 = field()
field41.setName("l_shoulder_rotation_changed")
field41.setAccessType("outputOnly")
field41.setType("SFRotation")

ProtoInterface20.addField(field41)
field42 = field()
field42.setName("l_elbow_rotation_changed")
field42.setAccessType("outputOnly")
field42.setType("SFRotation")

ProtoInterface20.addField(field42)
field43 = field()
field43.setName("l_wrist_rotation_changed")
field43.setAccessType("outputOnly")
field43.setType("SFRotation")

ProtoInterface20.addField(field43)
field44 = field()
field44.setName("r_shoulder_rotation_changed")
field44.setAccessType("outputOnly")
field44.setType("SFRotation")

ProtoInterface20.addField(field44)
field45 = field()
field45.setName("r_elbow_rotation_changed")
field45.setAccessType("outputOnly")
field45.setType("SFRotation")

ProtoInterface20.addField(field45)
field46 = field()
field46.setName("r_wrist_rotation_changed")
field46.setAccessType("outputOnly")
field46.setType("SFRotation")

ProtoInterface20.addField(field46)

ProtoDeclare19.setProtoInterface(ProtoInterface20)
ProtoBody47 = ProtoBody()
Group48 = Group()
TimeSensor49 = TimeSensor()
TimeSensor49.setDEF("TIMER")
TimeSensor49.setLoop(True)
IS50 = IS()
connect51 = connect()
connect51.setNodeField("cycleInterval")
connect51.setProtoField("cycleInterval")

IS50.addConnect(connect51)
connect52 = connect()
connect52.setNodeField("enabled")
connect52.setProtoField("enabled")

IS50.addConnect(connect52)
connect53 = connect()
connect53.setNodeField("loop")
connect53.setProtoField("loop")

IS50.addConnect(connect53)
connect54 = connect()
connect54.setNodeField("startTime")
connect54.setProtoField("startTime")

IS50.addConnect(connect54)
connect55 = connect()
connect55.setNodeField("stopTime")
connect55.setProtoField("stopTime")

IS50.addConnect(connect55)
connect56 = connect()
connect56.setNodeField("fraction_changed")
connect56.setProtoField("fraction_changed")

IS50.addConnect(connect56)
connect57 = connect()
connect57.setNodeField("isActive")
connect57.setProtoField("isActive")

IS50.addConnect(connect57)

TimeSensor49.setIS(IS50)

Group48.addChildren(TimeSensor49)
PositionInterpolator58 = PositionInterpolator()
PositionInterpolator58.setDEF("HUMANOIDROOT_POSITION_ANIMATOR")
PositionInterpolator58.setKey([0,0.04,0.08,0.12,0.16,0.2,0.24,0.28,0.32,0.36,0.4,0.44,0.48,0.64,0.76,0.8,0.84,0.88,0.92,0.96,1])
PositionInterpolator58.setKeyValue([0,0,0,0,-0.01264,-0.01289,0,-0.04712,-0.03738,-0.0003345,-0.1049,-0.05353,-0.0005712,-0.1892,-0.06561,-0.0008233,-0.286,-0.06276,-0.0009591,-0.3795,-0.05148,-0.00106,-0.4484,-0.03656,-0.00106,-0.4484,-0.03656,-0.001122,-0.3269,-0.1499,-0.0008616,-0.13,-0.06358,-0.0005128,-0.03123,-0.05488,0.0004779,0.053,0.02732,0.0001728,0.4148,0.006873,0,0.03045,0.02148,0,-0.01299,-0.01057,0,-0.06932,-0.01064,0.0001365,-0.1037,-0.005059,0.0001279,-0.07198,-0.007596,0.000141,-0.01626,-0.004935,0,0,0])
IS59 = IS()
connect60 = connect()
connect60.setNodeField("value_changed")
connect60.setProtoField("HumanoidRoot_translation_changed")

IS59.addConnect(connect60)

PositionInterpolator58.setIS(IS59)

Group48.addChildren(PositionInterpolator58)
OrientationInterpolator61 = OrientationInterpolator()
OrientationInterpolator61.setDEF("HUMANOIDROOT_ANIMATOR")
OrientationInterpolator61.setKey([0,0.28,0.32,0.48,0.64,0.76,1])
OrientationInterpolator61.setKeyValue([0,0,1,0,1,0,0,0.3273,1,0,0,0.3273,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0])
IS62 = IS()
connect63 = connect()
connect63.setNodeField("value_changed")
connect63.setProtoField("HumanoidRoot_rotation_changed")

IS62.addConnect(connect63)

OrientationInterpolator61.setIS(IS62)

Group48.addChildren(OrientationInterpolator61)
OrientationInterpolator64 = OrientationInterpolator()
OrientationInterpolator64.setDEF("SACROILIAC_ANIMATOR")
OrientationInterpolator64.setKey([0,0.28,0.32,0.48,0.76,1])
OrientationInterpolator64.setKeyValue([0,0,1,0,1,0,0,0.1892,1,0,0,0.1892,0,0,1,0,0,0,1,0,0,0,1,0])
IS65 = IS()
connect66 = connect()
connect66.setNodeField("value_changed")
connect66.setProtoField("lower_body_rotation_changed")

IS65.addConnect(connect66)

OrientationInterpolator64.setIS(IS65)

Group48.addChildren(OrientationInterpolator64)
OrientationInterpolator67 = OrientationInterpolator()
OrientationInterpolator67.setDEF("L_HIP_ANIMATOR")
OrientationInterpolator67.setKey([0,0.28,0.32,0.36,0.4,0.44,0.48,0.64,0.76,0.88,1])
OrientationInterpolator67.setKeyValue([0,0,1,0,1,0,0,4.349,1,0,0,4.349,1,0,0,4.615,-1,0,0,0.9136,-1,0,0,0.3614,0,0,1,0,-1,0,0,0.7869,-1,0,0,0.3918,-1,0,0,0.5433,0,0,1,0])
IS68 = IS()
connect69 = connect()
connect69.setNodeField("value_changed")
connect69.setProtoField("l_hip_rotation_changed")

IS68.addConnect(connect69)

OrientationInterpolator67.setIS(IS68)

Group48.addChildren(OrientationInterpolator67)
OrientationInterpolator70 = OrientationInterpolator()
OrientationInterpolator70.setDEF("L_KNEE_ANIMATOR")
OrientationInterpolator70.setKey([0,0.28,0.32,0.48,0.64,0.76,0.88,1])
OrientationInterpolator70.setKeyValue([0,0,1,0,1,0,0,2.047,1,0,0,2.047,0,0,1,0,1,0,0,1.566,1,0,0,0.5913,1,0,0,0.9235,0,0,1,0])
IS71 = IS()
connect72 = connect()
connect72.setNodeField("value_changed")
connect72.setProtoField("l_knee_rotation_changed")

IS71.addConnect(connect72)

OrientationInterpolator70.setIS(IS71)

Group48.addChildren(OrientationInterpolator70)
OrientationInterpolator73 = OrientationInterpolator()
OrientationInterpolator73.setDEF("L_ANKLE_ANIMATOR")
OrientationInterpolator73.setKey([0,0.28,0.32,0.36,0.4,0.44,0.48,0.64,0.76,0.84,0.88,0.92,0.96,1])
OrientationInterpolator73.setKeyValue([0,0,1,0,-1,0,0,0.625,-1,0,0,0.625,-1,0,0,0.3364,-1,0,0,0.2742,-1,0,0,0.05078,1,0,0,0.2833,1,0,0,0.6667,1,0,0,0.2833,-1,0,0,0.2108,-1,0,0,0.375,-1,0,0,0.3146,-1,0,0,0.1174,0,0,1,0])
IS74 = IS()
connect75 = connect()
connect75.setNodeField("value_changed")
connect75.setProtoField("l_ankle_rotation_changed")

IS74.addConnect(connect75)

OrientationInterpolator73.setIS(IS74)

Group48.addChildren(OrientationInterpolator73)
OrientationInterpolator76 = OrientationInterpolator()
OrientationInterpolator76.setDEF("L_MIDTARSAL_ANIMATOR")
OrientationInterpolator76.setKey([0,0.5,1])
OrientationInterpolator76.setKeyValue([1,0,0,0,1,0,0,-0.2,1,0,0,0])
IS77 = IS()
connect78 = connect()
connect78.setNodeField("value_changed")
connect78.setProtoField("l_midtarsal_rotation_changed")

IS77.addConnect(connect78)

OrientationInterpolator76.setIS(IS77)

Group48.addChildren(OrientationInterpolator76)
OrientationInterpolator79 = OrientationInterpolator()
OrientationInterpolator79.setDEF("R_HIP_ANIMATOR")
OrientationInterpolator79.setKey([0,0.28,0.32,0.36,0.4,0.44,0.48,0.64,0.76,0.88,1])
OrientationInterpolator79.setKeyValue([0,0,1,0,1,0,0,4.433,1,0,0,4.433,1,0,0,4.647,-1,0,0,0.8943,-1,0,0,0.3698,0,0,1,0,-1,0,0,0.4963,-1,0,0,0.3829,-1,0,0,0.5169,0,0,1,0])
IS80 = IS()
connect81 = connect()
connect81.setNodeField("value_changed")
connect81.setProtoField("r_hip_rotation_changed")

IS80.addConnect(connect81)

OrientationInterpolator79.setIS(IS80)

Group48.addChildren(OrientationInterpolator79)
OrientationInterpolator82 = OrientationInterpolator()
OrientationInterpolator82.setDEF("R_KNEE_ANIMATOR")
OrientationInterpolator82.setKey([0,0.28,0.32,0.48,0.64,0.76,0.88,1])
OrientationInterpolator82.setKeyValue([0,0,1,0,1,0,0,2.005,1,0,0,2.005,0,0,1,0,1,0,0,0.9507,1,0,0,0.5845,1,0,0,0.9054,0,0,1,0])
IS83 = IS()
connect84 = connect()
connect84.setNodeField("value_changed")
connect84.setProtoField("r_knee_rotation_changed")

IS83.addConnect(connect84)

OrientationInterpolator82.setIS(IS83)

Group48.addChildren(OrientationInterpolator82)
OrientationInterpolator85 = OrientationInterpolator()
OrientationInterpolator85.setDEF("R_ANKLE_ANIMATOR")
OrientationInterpolator85.setKey([0,0.28,0.32,0.36,0.4,0.44,0.48,0.64,0.76,0.84,0.88,0.92,0.96,1])
OrientationInterpolator85.setKeyValue([0,0,1,0,-1,0,0,0.6735,-1,0,0,0.6735,-1,0,0,0.3527,-1,0,0,0.3038,-1,0,0,0.07964,1,0,0,0.3001,1,0,0,0.6509,1,0,0,0.3001,-1,0,0,0.2087,-1,0,0,0.3756,-1,0,0,0.3279,-1,0,0,0.1193,0,0,1,0])
IS86 = IS()
connect87 = connect()
connect87.setNodeField("value_changed")
connect87.setProtoField("r_ankle_rotation_changed")

IS86.addConnect(connect87)

OrientationInterpolator85.setIS(IS86)

Group48.addChildren(OrientationInterpolator85)
OrientationInterpolator88 = OrientationInterpolator()
OrientationInterpolator88.setDEF("R_MIDTARSAL_ANIMATOR")
OrientationInterpolator88.setKey([0,0.5,1])
OrientationInterpolator88.setKeyValue([1,0,0,-0.2,1,0,0,0,1,0,0,-0.2])
IS89 = IS()
connect90 = connect()
connect90.setNodeField("value_changed")
connect90.setProtoField("r_midtarsal_rotation_changed")

IS89.addConnect(connect90)

OrientationInterpolator88.setIS(IS89)

Group48.addChildren(OrientationInterpolator88)
OrientationInterpolator91 = OrientationInterpolator()
OrientationInterpolator91.setDEF("VL5_ANIMATOR")
OrientationInterpolator91.setKey([0,0.2083,0.375,0.75,0.8333,1])
OrientationInterpolator91.setKeyValue([0,1,0,0.0826,-0.01972,-0.5974,0.8017,0.08231,0.009296,-0.9648,0.2627,0.1734,-0.01238,0.9549,-0.2968,0.08732,-0.008125,0.9691,-0.2463,0.158,0,1,0,0.0826])
IS92 = IS()
connect93 = connect()
connect93.setNodeField("value_changed")
connect93.setProtoField("vl5_rotation_changed")

IS92.addConnect(connect93)

OrientationInterpolator91.setIS(IS92)

Group48.addChildren(OrientationInterpolator91)
OrientationInterpolator94 = OrientationInterpolator()
OrientationInterpolator94.setDEF("SKULLBASE_ANIMATOR")
OrientationInterpolator94.setKey([0,0.28,0.32,0.48,0.76,1])
OrientationInterpolator94.setKeyValue([0,0,1,0,-1,0,0,0.5989,-1,0,0,0.5989,-1,0,0,0.3216,1,0,0,0.06503,0,0,1,0])
IS95 = IS()
connect96 = connect()
connect96.setNodeField("value_changed")
connect96.setProtoField("skullbase_rotation_changed")

IS95.addConnect(connect96)

OrientationInterpolator94.setIS(IS95)

Group48.addChildren(OrientationInterpolator94)
OrientationInterpolator97 = OrientationInterpolator()
OrientationInterpolator97.setDEF("L_SHOULDER_ANIMATOR")
OrientationInterpolator97.setKey([0,0.28,0.32,0.64,0.76,0.88,1])
OrientationInterpolator97.setKeyValue([0,0,1,0,-0.9987,0.02554,0.04498,1.57,-0.9987,0.02554,0.04498,1.57,1,0.0004113,0.003055,4.114,-0.8413,0.3238,0.4329,1.453,-0.877,0.4198,0.2337,0.6009,0,0,1,0])
IS98 = IS()
connect99 = connect()
connect99.setNodeField("value_changed")
connect99.setProtoField("l_shoulder_rotation_changed")

IS98.addConnect(connect99)

OrientationInterpolator97.setIS(IS98)

Group48.addChildren(OrientationInterpolator97)
OrientationInterpolator100 = OrientationInterpolator()
OrientationInterpolator100.setDEF("L_ELBOW_ANIMATOR")
OrientationInterpolator100.setKey([0,0.28,0.32,0.64,0.76,1])
OrientationInterpolator100.setKeyValue([0,0,1,0,-1,0,0,0.1229,-1,0,0,0.1229,-1,0,0,0.5976,-1,0,0,0.3917,0,0,1,0])
IS101 = IS()
connect102 = connect()
connect102.setNodeField("value_changed")
connect102.setProtoField("l_elbow_rotation_changed")

IS101.addConnect(connect102)

OrientationInterpolator100.setIS(IS101)

Group48.addChildren(OrientationInterpolator100)
OrientationInterpolator103 = OrientationInterpolator()
OrientationInterpolator103.setDEF("L_WRIST_ANIMATOR")
OrientationInterpolator103.setKey([0,0.28,0.32,0.64,0.76,0.88,1])
OrientationInterpolator103.setKeyValue([0,0,1,0,0.0672928,0.989475,-0.128107,4.15574,0.0672928,0.989475,-0.128107,4.15574,0.00364942,0.999901,0.0135896,4.5822,0,-1,0,0.655922,-0.00050618,-0.999999,0.0012782,1.28397,0,0,1,0])
IS104 = IS()
connect105 = connect()
connect105.setNodeField("value_changed")
connect105.setProtoField("l_wrist_rotation_changed")

IS104.addConnect(connect105)

OrientationInterpolator103.setIS(IS104)

Group48.addChildren(OrientationInterpolator103)
OrientationInterpolator106 = OrientationInterpolator()
OrientationInterpolator106.setDEF("R_SHOULDER_ANIMATOR")
OrientationInterpolator106.setKey([0,0.28,0.32,0.64,0.76,0.88,1])
OrientationInterpolator106.setKeyValue([0,0,1,0,0.9992,0.02042,0.03558,4.688,0.9992,0.02042,0.03558,4.688,0.9989,-0.04623,0.005159,4.079,-0.8687,-0.2525,-0.4261,1.501,-0.941,-0.2893,-0.1754,0.4788,0,0,1,0])
IS107 = IS()
connect108 = connect()
connect108.setNodeField("value_changed")
connect108.setProtoField("r_shoulder_rotation_changed")

IS107.addConnect(connect108)

OrientationInterpolator106.setIS(IS107)

Group48.addChildren(OrientationInterpolator106)
OrientationInterpolator109 = OrientationInterpolator()
OrientationInterpolator109.setDEF("R_ELBOW_ANIMATOR")
OrientationInterpolator109.setKey([0,0.28,0.32,0.64,0.76,1])
OrientationInterpolator109.setKeyValue([0,0,1,0,-1,0,0,0.04151,-1,0,0,0.04151,-1,0,0,0.5855,-1,0,0,0.5852,0,0,1,0])
IS110 = IS()
connect111 = connect()
connect111.setNodeField("value_changed")
connect111.setProtoField("r_elbow_rotation_changed")

IS110.addConnect(connect111)

OrientationInterpolator109.setIS(IS110)

Group48.addChildren(OrientationInterpolator109)
OrientationInterpolator112 = OrientationInterpolator()
OrientationInterpolator112.setDEF("R_WRIST_ANIMATOR")
OrientationInterpolator112.setKey([0,0.28,0.32,0.64,0.76,1])
OrientationInterpolator112.setKeyValue([0,0,1,0,-0.0585279,0.983903,-0.168849,1.85956,-0.0585279,0.983903,-0.168849,1.85956,-0.00222418,0.99801,-0.0630095,1.46072,0,1,0,0.497349,0,0,1,0])
IS113 = IS()
connect114 = connect()
connect114.setNodeField("value_changed")
connect114.setProtoField("r_wrist_rotation_changed")

IS113.addConnect(connect114)

OrientationInterpolator112.setIS(IS113)

Group48.addChildren(OrientationInterpolator112)

ProtoBody47.addChildren(Group48)
ROUTE115 = ROUTE()
ROUTE115.setFromField("fraction_changed")
ROUTE115.setFromNode("TIMER")
ROUTE115.setToField("set_fraction")
ROUTE115.setToNode("HUMANOIDROOT_POSITION_ANIMATOR")

ProtoBody47.addChildren(ROUTE115)
ROUTE116 = ROUTE()
ROUTE116.setFromField("fraction_changed")
ROUTE116.setFromNode("TIMER")
ROUTE116.setToField("set_fraction")
ROUTE116.setToNode("HUMANOIDROOT_ANIMATOR")

ProtoBody47.addChildren(ROUTE116)
ROUTE117 = ROUTE()
ROUTE117.setFromField("fraction_changed")
ROUTE117.setFromNode("TIMER")
ROUTE117.setToField("set_fraction")
ROUTE117.setToNode("SACROILIAC_ANIMATOR")

ProtoBody47.addChildren(ROUTE117)
ROUTE118 = ROUTE()
ROUTE118.setFromField("fraction_changed")
ROUTE118.setFromNode("TIMER")
ROUTE118.setToField("set_fraction")
ROUTE118.setToNode("L_HIP_ANIMATOR")

ProtoBody47.addChildren(ROUTE118)
ROUTE119 = ROUTE()
ROUTE119.setFromField("fraction_changed")
ROUTE119.setFromNode("TIMER")
ROUTE119.setToField("set_fraction")
ROUTE119.setToNode("L_KNEE_ANIMATOR")

ProtoBody47.addChildren(ROUTE119)
ROUTE120 = ROUTE()
ROUTE120.setFromField("fraction_changed")
ROUTE120.setFromNode("TIMER")
ROUTE120.setToField("set_fraction")
ROUTE120.setToNode("L_ANKLE_ANIMATOR")

ProtoBody47.addChildren(ROUTE120)
ROUTE121 = ROUTE()
ROUTE121.setFromField("fraction_changed")
ROUTE121.setFromNode("TIMER")
ROUTE121.setToField("set_fraction")
ROUTE121.setToNode("L_MIDTARSAL_ANIMATOR")

ProtoBody47.addChildren(ROUTE121)
ROUTE122 = ROUTE()
ROUTE122.setFromField("fraction_changed")
ROUTE122.setFromNode("TIMER")
ROUTE122.setToField("set_fraction")
ROUTE122.setToNode("R_HIP_ANIMATOR")

ProtoBody47.addChildren(ROUTE122)
ROUTE123 = ROUTE()
ROUTE123.setFromField("fraction_changed")
ROUTE123.setFromNode("TIMER")
ROUTE123.setToField("set_fraction")
ROUTE123.setToNode("R_KNEE_ANIMATOR")

ProtoBody47.addChildren(ROUTE123)
ROUTE124 = ROUTE()
ROUTE124.setFromField("fraction_changed")
ROUTE124.setFromNode("TIMER")
ROUTE124.setToField("set_fraction")
ROUTE124.setToNode("R_ANKLE_ANIMATOR")

ProtoBody47.addChildren(ROUTE124)
ROUTE125 = ROUTE()
ROUTE125.setFromField("fraction_changed")
ROUTE125.setFromNode("TIMER")
ROUTE125.setToField("set_fraction")
ROUTE125.setToNode("R_MIDTARSAL_ANIMATOR")

ProtoBody47.addChildren(ROUTE125)
ROUTE126 = ROUTE()
ROUTE126.setFromField("fraction_changed")
ROUTE126.setFromNode("TIMER")
ROUTE126.setToField("set_fraction")
ROUTE126.setToNode("VL5_ANIMATOR")

ProtoBody47.addChildren(ROUTE126)
ROUTE127 = ROUTE()
ROUTE127.setFromField("fraction_changed")
ROUTE127.setFromNode("TIMER")
ROUTE127.setToField("set_fraction")
ROUTE127.setToNode("SKULLBASE_ANIMATOR")

ProtoBody47.addChildren(ROUTE127)
ROUTE128 = ROUTE()
ROUTE128.setFromField("fraction_changed")
ROUTE128.setFromNode("TIMER")
ROUTE128.setToField("set_fraction")
ROUTE128.setToNode("L_SHOULDER_ANIMATOR")

ProtoBody47.addChildren(ROUTE128)
ROUTE129 = ROUTE()
ROUTE129.setFromField("fraction_changed")
ROUTE129.setFromNode("TIMER")
ROUTE129.setToField("set_fraction")
ROUTE129.setToNode("L_ELBOW_ANIMATOR")

ProtoBody47.addChildren(ROUTE129)
ROUTE130 = ROUTE()
ROUTE130.setFromField("fraction_changed")
ROUTE130.setFromNode("TIMER")
ROUTE130.setToField("set_fraction")
ROUTE130.setToNode("L_WRIST_ANIMATOR")

ProtoBody47.addChildren(ROUTE130)
ROUTE131 = ROUTE()
ROUTE131.setFromField("fraction_changed")
ROUTE131.setFromNode("TIMER")
ROUTE131.setToField("set_fraction")
ROUTE131.setToNode("R_SHOULDER_ANIMATOR")

ProtoBody47.addChildren(ROUTE131)
ROUTE132 = ROUTE()
ROUTE132.setFromField("fraction_changed")
ROUTE132.setFromNode("TIMER")
ROUTE132.setToField("set_fraction")
ROUTE132.setToNode("R_ELBOW_ANIMATOR")

ProtoBody47.addChildren(ROUTE132)
ROUTE133 = ROUTE()
ROUTE133.setFromField("fraction_changed")
ROUTE133.setFromNode("TIMER")
ROUTE133.setToField("set_fraction")
ROUTE133.setToNode("R_WRIST_ANIMATOR")

ProtoBody47.addChildren(ROUTE133)

ProtoDeclare19.setProtoBody(ProtoBody47)

Scene17.addChildren(ProtoDeclare19)
Anchor134 = Anchor()
Anchor134.setDescription("see InterchangableActorsViaDynamicRouting scene")
Anchor134.setParameter(["target=_blank"])
Anchor134.setUrl(["InterchangableActorsViaDynamicRouting.x3d","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Prototypes/InterchangableActorsViaDynamicRouting.x3d","InterchangableActorsViaDynamicRouting.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Prototypes/InterchangableActorsViaDynamicRouting.wrl"])
Shape135 = Shape()
Text136 = Text()
Text136.setString(["LOA1_JumpAnimation.x3d","defines a prototype","for animating a humanoid.","","Click this text to see","InterchangableActorsViaDynamicRouting example."])
FontStyle137 = FontStyle()
FontStyle137.setJustify(["MIDDLE","MIDDLE"])
FontStyle137.setSize(0.8)

Text136.setFontStyle(FontStyle137)

Shape135.setGeometry(Text136)
Appearance138 = Appearance()
Material139 = Material()
Material139.setDiffuseColor([1,1,0.2])

Appearance138.setMaterial(Material139)

Shape135.setAppearance(Appearance138)

Anchor134.addChildren(Shape135)

Scene17.addChildren(Anchor134)

X3D0.setScene(Scene17)
X3D0.toFileX3D("././LOA1_JumpAnimation_RoundTrip.x3d")
