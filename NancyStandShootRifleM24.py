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
meta3.content = "NancyStandShootRifleM24.x3d"

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.name = "description"
meta4.content = "Canonical HAnim 1.1 specification example, using native X3D tags instead of ProtoDeclaration/ExternProtoDeclaration and ProtoInstance."

head1.children.append(meta4)
meta5 = x3d.meta()
meta5.name = "creator"
meta5.content = "Etsuko Lippi"

head1.children.append(meta5)
meta6 = x3d.meta()
meta6.name = "created"
meta6.content = "4 January 2002"

head1.children.append(meta6)
meta7 = x3d.meta()
meta7.name = "modified"
meta7.content = "23 May 2020"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.name = "warning"
meta8.content = "ProtoBody missing content"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "warning"
meta9.content = "Numerous QA warnings need to be corrected"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "warning"
meta10.content = "LOA1_ShootAnimation ought to be moved out as a separate prototype."

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.name = "identifier"
meta11.content = "https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Legacy/NancyStandShootRifleM24.x3d"

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
ExternProtoDeclare15 = x3d.ExternProtoDeclare()
ExternProtoDeclare15.name = "RifleM24"
ExternProtoDeclare15.appinfo = "Rifle M24"
ExternProtoDeclare15.url = ["../../Savage/Weapons/SmallArms/RifleM24Prototype.x3d#RifleM24","https://savage.nps.edu/Savage/Weapons/SmallArms/RifleM24Prototype.x3d#RifleM24","../../Savage/Weapons/SmallArms/RifleM24Prototype.wrl#RifleM24","https://savage.nps.edu/Savage/Weapons/SmallArms/RifleM24Prototype.wrl#RifleM24"]
field16 = x3d.field()
field16.name = "trigger"
field16.accessType = "inputOnly"
field16.appinfo = "input true to fire"
field16.type = "SFBool"

ExternProtoDeclare15.field.append(field16)
field17 = x3d.field()
field17.name = "fire"
field17.accessType = "outputOnly"
field17.appinfo = "output true when fired"
field17.type = "SFBool"

ExternProtoDeclare15.field.append(field17)
field18 = x3d.field()
field18.name = "animationStartTime"
field18.accessType = "inputOnly"
field18.appinfo = "trigger animation"
field18.type = "SFTime"

ExternProtoDeclare15.field.append(field18)

Scene14.children.append(ExternProtoDeclare15)
ProtoDeclare19 = x3d.ProtoDeclare()
ProtoDeclare19.name = "LOA1_ShootAnimation"
ProtoInterface20 = x3d.ProtoInterface()
field21 = x3d.field()
field21.name = "cycleInterval"
field21.accessType = "inputOutput"
field21.type = "SFTime"
field21.value = 0.009999999776482582

ProtoInterface20.field.append(field21)
field22 = x3d.field()
field22.name = "enabled"
field22.accessType = "inputOutput"
field22.type = "SFBool"
field22.value = True

ProtoInterface20.field.append(field22)
field23 = x3d.field()
field23.name = "loop"
field23.accessType = "inputOutput"
field23.type = "SFBool"
field23.value = True

ProtoInterface20.field.append(field23)
field24 = x3d.field()
field24.name = "startTime"
field24.accessType = "inputOutput"
field24.type = "SFTime"
field24.value = 0

ProtoInterface20.field.append(field24)
field25 = x3d.field()
field25.name = "stopTime"
field25.accessType = "inputOutput"
field25.type = "SFTime"
field25.value = -1

ProtoInterface20.field.append(field25)
field26 = x3d.field()
field26.name = "fraction_changed"
field26.accessType = "outputOnly"
field26.type = "SFFloat"

ProtoInterface20.field.append(field26)
field27 = x3d.field()
field27.name = "isActive"
field27.accessType = "outputOnly"
field27.type = "SFBool"

ProtoInterface20.field.append(field27)
field28 = x3d.field()
field28.name = "HumanoidRoot_translation_changed"
field28.accessType = "outputOnly"
field28.type = "SFVec3f"

ProtoInterface20.field.append(field28)
field29 = x3d.field()
field29.name = "HumanoidRoot_rotation_changed"
field29.accessType = "outputOnly"
field29.type = "SFRotation"

ProtoInterface20.field.append(field29)
field30 = x3d.field()
field30.name = "lower_body_rotation_changed"
field30.accessType = "outputOnly"
field30.type = "SFRotation"

ProtoInterface20.field.append(field30)
field31 = x3d.field()
field31.name = "l_hip_rotation_changed"
field31.accessType = "outputOnly"
field31.type = "SFRotation"

ProtoInterface20.field.append(field31)
field32 = x3d.field()
field32.name = "l_knee_rotation_changed"
field32.accessType = "outputOnly"
field32.type = "SFRotation"

ProtoInterface20.field.append(field32)
field33 = x3d.field()
field33.name = "l_ankle_rotation_changed"
field33.accessType = "outputOnly"
field33.type = "SFRotation"

ProtoInterface20.field.append(field33)
field34 = x3d.field()
field34.name = "l_midtarsal_rotation_changed"
field34.accessType = "outputOnly"
field34.type = "SFRotation"

ProtoInterface20.field.append(field34)
field35 = x3d.field()
field35.name = "r_hip_rotation_changed"
field35.accessType = "outputOnly"
field35.type = "SFRotation"

ProtoInterface20.field.append(field35)
field36 = x3d.field()
field36.name = "r_knee_rotation_changed"
field36.accessType = "outputOnly"
field36.type = "SFRotation"

ProtoInterface20.field.append(field36)
field37 = x3d.field()
field37.name = "r_ankle_rotation_changed"
field37.accessType = "outputOnly"
field37.type = "SFRotation"

ProtoInterface20.field.append(field37)
field38 = x3d.field()
field38.name = "r_midtarsal_rotation_changed"
field38.accessType = "outputOnly"
field38.type = "SFRotation"

ProtoInterface20.field.append(field38)
field39 = x3d.field()
field39.name = "vl5_rotation_changed"
field39.accessType = "outputOnly"
field39.type = "SFRotation"

ProtoInterface20.field.append(field39)
field40 = x3d.field()
field40.name = "skullbase_rotation_changed"
field40.accessType = "outputOnly"
field40.type = "SFRotation"

ProtoInterface20.field.append(field40)
field41 = x3d.field()
field41.name = "l_shoulder_rotation_changed"
field41.accessType = "outputOnly"
field41.type = "SFRotation"

ProtoInterface20.field.append(field41)
field42 = x3d.field()
field42.name = "l_elbow_rotation_changed"
field42.accessType = "outputOnly"
field42.type = "SFRotation"

ProtoInterface20.field.append(field42)
field43 = x3d.field()
field43.name = "l_wrist_rotation_changed"
field43.accessType = "outputOnly"
field43.type = "SFRotation"

ProtoInterface20.field.append(field43)
field44 = x3d.field()
field44.name = "r_shoulder_rotation_changed"
field44.accessType = "outputOnly"
field44.type = "SFRotation"

ProtoInterface20.field.append(field44)
field45 = x3d.field()
field45.name = "r_elbow_rotation_changed"
field45.accessType = "outputOnly"
field45.type = "SFRotation"

ProtoInterface20.field.append(field45)
field46 = x3d.field()
field46.name = "r_wrist_rotation_changed"
field46.accessType = "outputOnly"
field46.type = "SFRotation"

ProtoInterface20.field.append(field46)

ProtoDeclare19.ProtoInterface = ProtoInterface20
ProtoBody47 = x3d.ProtoBody()
Group48 = x3d.Group()
Group48.DEF = "ErrorLostContentCheckVersionControl"

ProtoBody47.children.append(Group48)

ProtoDeclare19.ProtoBody = ProtoBody47

Scene14.children.append(ProtoDeclare19)
#Start scene graph.
Background49 = x3d.Background()

Scene14.children.append(Background49)
Viewpoint50 = x3d.Viewpoint()
Viewpoint50.description = "Nancy Rifle Shooting Position"
Viewpoint50.position = [0,0.9,2.7]

Scene14.children.append(Viewpoint50)
Viewpoint51 = x3d.Viewpoint()
Viewpoint51.description = "Nancy Side Viewpoint"
Viewpoint51.orientation = [0,-1,0,1.4925]
Viewpoint51.position = [-2.7,0.9,0.4]

Scene14.children.append(Viewpoint51)
Viewpoint52 = x3d.Viewpoint()
Viewpoint52.description = "Nancy Above Viewpoint"
Viewpoint52.orientation = [0.954,0.244,0.172,4.6369]
Viewpoint52.position = [0.1,4.1,-0.2]

Scene14.children.append(Viewpoint52)
LOD53 = x3d.LOD()
LOD53.range = [50,100]
Group54 = x3d.Group()
Group54.DEF = "Viewpoint"
#High Resolution
Group55 = x3d.Group()
Group55.DEF = "HighResolution"
Transform56 = x3d.Transform()
HAnimHumanoid57 = x3d.HAnimHumanoid()
HAnimHumanoid57.name = "Nancy"
HAnimHumanoid57.DEF = "hanim_Nancy"
HAnimHumanoid57.version = "2.0"
HAnimJoint58 = x3d.HAnimJoint()
HAnimJoint58.name = "humanoid_root"
HAnimJoint58.DEF = "hanim_humanoid_root"
HAnimJoint58.center = [-0.00405,0.855,-0.000113]
HAnimJoint58.ulimit = [0,0,0]
HAnimJoint58.llimit = [0,0,0]
HAnimJoint59 = x3d.HAnimJoint()
HAnimJoint59.name = "sacroiliac"
HAnimJoint59.DEF = "hanim_sacroiliac"
HAnimJoint59.center = [0,1.01,-0.0204]
HAnimJoint59.ulimit = [0,0,0]
HAnimJoint59.llimit = [0,0,0]
HAnimSegment60 = x3d.HAnimSegment()
HAnimSegment60.name = "pelvis"
HAnimSegment60.DEF = "hanim_pelvis"
Shape61 = x3d.Shape()
Appearance62 = x3d.Appearance()
Material63 = x3d.Material()
Material63.DEF = "Pants_Color"
Material63.ambientIntensity = 0.25
Material63.diffuseColor = [0.054,0.233,0.39]

Appearance62.material = Material63
ImageTexture64 = x3d.ImageTexture()
ImageTexture64.DEF = "camo"
ImageTexture64.repeatS = False
ImageTexture64.repeatT = False
ImageTexture64.url = ["greenCamo.jpg","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Legacy/greenCamo.jpg"]

Appearance62.texture = ImageTexture64

Shape61.appearance = Appearance62
IndexedFaceSet65 = x3d.IndexedFaceSet()
IndexedFaceSet65.coordIndex = [0,1,40,-1,1,2,40,-1,2,3,40,-1,3,4,40,-1,4,5,40,-1,5,4,9,-1,4,3,8,-1,3,2,8,-1,2,1,6,-1,0,7,1,-1,7,6,1,-1,6,8,2,-1,9,4,10,-1,4,8,10,-1,8,6,12,-1,7,0,47,-1,50,5,9,-1,7,47,55,-1,55,13,7,-1,50,9,56,-1,9,10,14,-1,10,11,15,-1,11,12,16,-1,12,13,19,-1,13,55,17,-1,60,17,55,-1,17,19,13,-1,19,16,12,-1,16,15,11,-1,15,18,10,-1,14,56,9,-1,56,14,64,-1,17,60,20,-1,20,19,17,-1,21,64,14,-1,14,22,21,-1,15,16,24,-1,16,19,24,-1,19,20,26,-1,24,23,15,-1,64,21,69,-1,21,22,29,-1,19,26,25,-1,20,63,27,-1,27,26,20,-1,25,24,19,-1,30,29,22,-1,29,28,21,-1,28,69,21,-1,27,34,26,-1,69,28,79,-1,29,30,32,-1,30,23,33,-1,23,24,37,-1,25,26,34,-1,83,27,77,-1,37,33,23,-1,33,32,30,-1,31,79,28,-1,79,31,84,-1,32,33,36,-1,24,25,37,-1,34,27,83,-1,83,38,34,-1,34,37,25,-1,37,36,33,-1,36,35,32,-1,84,31,89,-1,31,35,89,-1,35,36,39,-1,36,37,39,-1,38,83,89,-1,89,39,38,-1,39,89,35,-1,40,41,0,-1,40,42,41,-1,40,43,42,-1,40,44,43,-1,40,45,44,-1,49,44,45,-1,48,43,44,-1,48,42,43,-1,46,41,42,-1,41,47,0,-1,41,46,47,-1,42,48,46,-1,51,44,49,-1,51,48,44,-1,48,52,53,-1,49,45,50,-1,56,49,50,-1,57,51,49,-1,58,53,52,-1,59,54,53,-1,62,55,54,-1,55,62,60,-1,54,59,62,-1,53,58,59,-1,51,61,58,-1,49,56,57,-1,64,57,56,-1,67,59,58,-1,68,62,59,-1,60,63,20,-1,60,62,63,-1,59,67,68,-1,58,61,67,-1,57,64,65,-1,65,66,57,-1,71,63,62,-1,69,65,64,-1,74,66,65,-1,78,68,67,-1,70,71,62,-1,63,72,27,-1,63,71,72,-1,68,78,76,-1,67,75,78,-1,66,74,75,-1,65,73,74,-1,65,69,73,-1,77,27,72,-1,71,82,72,-1,79,73,69,-1,81,75,74,-1,82,71,70,-1,77,72,83,-1,73,79,80,-1,84,80,79,-1,86,75,81,-1,83,72,82,-1,82,88,83,-1,70,87,82,-1,81,85,86,-1,89,80,84,-1,89,85,80,-1,90,86,85,-1,90,87,86,-1,89,83,88,-1,88,90,89,-1,85,89,90,-1,50,45,5,-1,45,40,5,-1,10,8,11,-1,8,12,11,-1,18,22,10,-1,22,14,10,-1,57,66,51,-1,66,61,51,-1,51,58,48,-1,58,52,48,-1,48,53,46,-1,53,54,46,-1,76,70,68,-1,70,62,68,-1,29,32,28,-1,28,32,31,-1,32,35,31,-1,85,81,80,-1,81,73,80,-1,81,74,73,-1,39,37,38,-1,37,34,38,-1,82,87,88,-1,87,90,88,-1,87,78,86,-1,78,75,86,-1,61,66,67,-1,66,75,67,-1,22,18,15,-1,23,30,15,-1,30,22,15,-1,13,12,7,-1,12,6,7,-1,46,54,47,-1,54,55,47,-1,87,76,78,-1,87,70,76,-1]
IndexedFaceSet65.creaseAngle = 1.14
Coordinate66 = x3d.Coordinate()

IndexedFaceSet65.coord = Coordinate66

Shape61.geometry = IndexedFaceSet65

HAnimSegment60.children.append(Shape61)

HAnimJoint59.children.append(HAnimSegment60)
HAnimJoint67 = x3d.HAnimJoint()
HAnimJoint67.name = "l_hip"
HAnimJoint67.DEF = "hanim_l_hip"
HAnimJoint67.center = [0.122,0.888271,-0.0693267]
HAnimJoint67.ulimit = [0,0,0]
HAnimJoint67.llimit = [0,0,0]
HAnimSegment68 = x3d.HAnimSegment()
HAnimSegment68.name = "l_thigh"
HAnimSegment68.DEF = "hanim_l_thigh"
Shape69 = x3d.Shape()
Appearance70 = x3d.Appearance()
Material71 = x3d.Material()
Material71.USE = "Pants_Color"

Appearance70.material = Material71
ImageTexture72 = x3d.ImageTexture()
ImageTexture72.USE = "camo"

Appearance70.texture = ImageTexture72

Shape69.appearance = Appearance70
IndexedFaceSet73 = x3d.IndexedFaceSet()
IndexedFaceSet73.coordIndex = [0,4,5,-1,3,4,0,-1,0,7,1,-1,0,8,7,-1,0,6,8,-1,0,5,6,-1,0,2,3,-1,0,1,2,-1,9,2,1,-1,10,3,2,-1,11,4,3,-1,12,5,4,-1,13,6,5,-1,15,7,8,-1,9,1,7,-1,7,15,9,-1,8,14,15,-1,5,16,13,-1,5,12,16,-1,4,11,12,-1,3,10,11,-1,2,9,10,-1,20,13,16,-1,18,11,10,-1,19,12,11,-1,20,16,12,-1,23,15,14,-1,15,23,24,-1,12,19,20,-1,11,18,19,-1,10,17,18,-1,26,18,17,-1,27,19,18,-1,27,20,19,-1,28,21,20,-1,29,23,22,-1,23,29,30,-1,20,32,28,-1,20,27,32,-1,18,26,27,-1,17,25,26,-1,25,31,30,-1,30,29,26,-1,30,26,25,-1,29,28,27,-1,29,27,26,-1,28,32,27,-1,22,23,14,-1,20,21,13,-1,21,22,13,-1,22,14,13,-1,9,15,24,-1,10,9,17,-1,9,24,17,-1,6,13,8,-1,13,14,8,-1,28,29,21,-1,29,22,21,-1,24,31,17,-1,31,25,17,-1,30,31,23,-1,31,24,23,-1]
IndexedFaceSet73.creaseAngle = 1.32
Coordinate74 = x3d.Coordinate()

IndexedFaceSet73.coord = Coordinate74

Shape69.geometry = IndexedFaceSet73

HAnimSegment68.children.append(Shape69)

HAnimJoint67.children.append(HAnimSegment68)
HAnimJoint75 = x3d.HAnimJoint()
HAnimJoint75.name = "l_knee"
HAnimJoint75.DEF = "hanim_l_knee"
HAnimJoint75.center = [0.0738,0.517,-0.0284]
HAnimJoint75.ulimit = [0,0,0]
HAnimJoint75.llimit = [0,0,0]
HAnimSegment76 = x3d.HAnimSegment()
HAnimSegment76.name = "l_calf"
HAnimSegment76.DEF = "hanim_l_calf"
Shape77 = x3d.Shape()
Appearance78 = x3d.Appearance()
Material79 = x3d.Material()
Material79.USE = "Pants_Color"

Appearance78.material = Material79
ImageTexture80 = x3d.ImageTexture()
ImageTexture80.USE = "camo"

Appearance78.texture = ImageTexture80

Shape77.appearance = Appearance78
IndexedFaceSet81 = x3d.IndexedFaceSet()
IndexedFaceSet81.coordIndex = [2,1,0,-1,2,3,1,-1,2,4,3,-1,2,5,4,-1,2,6,5,-1,2,7,6,-1,2,8,7,-1,2,0,8,-1,9,8,0,-1,10,6,7,-1,11,5,6,-1,12,4,5,-1,12,3,4,-1,13,1,3,-1,1,13,14,-1,3,12,13,-1,5,11,12,-1,6,10,11,-1,8,9,15,-1,22,13,12,-1,13,22,14,-1,17,15,9,-1,20,12,11,-1,21,22,12,-1,23,9,14,-1,9,23,16,-1,14,22,23,-1,12,20,21,-1,15,17,18,-1,9,16,17,-1,24,17,16,-1,25,18,17,-1,26,19,18,-1,27,20,19,-1,28,21,20,-1,29,22,21,-1,30,23,22,-1,31,16,23,-1,23,30,31,-1,22,29,30,-1,21,28,29,-1,20,27,28,-1,19,26,27,-1,18,25,26,-1,17,24,25,-1,16,31,24,-1,33,26,25,-1,36,29,28,-1,37,31,30,-1,29,36,30,-1,25,24,33,-1,31,37,24,-1,32,33,24,-1,24,37,32,-1,38,37,30,-1,30,36,38,-1,41,33,32,-1,42,39,34,-1,44,36,35,-1,45,38,36,-1,46,37,38,-1,38,45,46,-1,36,44,45,-1,35,43,44,-1,39,42,47,-1,32,40,41,-1,40,46,45,-1,41,40,45,-1,41,45,44,-1,44,43,42,-1,44,42,41,-1,43,47,42,-1,39,35,28,-1,35,36,28,-1,34,39,27,-1,39,28,27,-1,33,34,26,-1,34,27,26,-1,33,41,34,-1,41,42,34,-1,40,32,46,-1,32,37,46,-1,10,19,11,-1,19,20,11,-1,14,9,1,-1,9,0,1,-1,8,15,7,-1,7,15,10,-1,15,19,10,-1,15,18,19,-1,43,35,47,-1,35,39,47,-1]
IndexedFaceSet81.creaseAngle = 1.57
Coordinate82 = x3d.Coordinate()

IndexedFaceSet81.coord = Coordinate82

Shape77.geometry = IndexedFaceSet81

HAnimSegment76.children.append(Shape77)

HAnimJoint75.children.append(HAnimSegment76)
HAnimJoint83 = x3d.HAnimJoint()
HAnimJoint83.name = "l_ankle"
HAnimJoint83.DEF = "hanim_l_ankle"
HAnimJoint83.center = [0.0645,0.0719,-0.048]
HAnimJoint83.ulimit = [0,0,0]
HAnimJoint83.llimit = [0,0,0]
HAnimSegment84 = x3d.HAnimSegment()
HAnimSegment84.name = "l_hindfoot"
HAnimSegment84.DEF = "hanim_l_hindfoot"
Shape85 = x3d.Shape()
Appearance86 = x3d.Appearance()
Material87 = x3d.Material()
Material87.DEF = "Shoe_Color"
Material87.ambientIntensity = 0.25
Material87.diffuseColor = [0,0,0]

Appearance86.material = Material87

Shape85.appearance = Appearance86
IndexedFaceSet88 = x3d.IndexedFaceSet()
IndexedFaceSet88.coordIndex = [2,1,0,-1,4,3,1,-1,2,4,1,-1,3,6,5,-1,1,3,5,-1,6,8,7,-1,5,6,7,-1,8,10,9,-1,7,8,9,-1,10,12,11,-1,9,10,11,-1,12,14,13,-1,11,12,13,-1,14,16,15,-1,13,14,15,-1,16,18,17,-1,15,16,17,-1,18,20,19,-1,17,18,19,-1,20,22,21,-1,19,20,21,-1,22,24,23,-1,21,22,23,-1,24,25,0,-1,23,24,0,-1,25,4,2,-1,0,25,2,-1,18,26,20,-1,16,26,18,-1,27,26,16,-1,14,27,16,-1,12,27,14,-1,28,27,12,-1,29,28,12,-1,10,29,12,-1,8,29,10,-1,6,37,8,-1,24,30,25,-1,31,30,24,-1,22,31,24,-1,32,31,22,-1,20,32,22,-1,33,32,20,-1,26,33,20,-1,34,33,26,-1,27,34,26,-1,35,34,27,-1,28,35,27,-1,29,35,28,-1,36,35,29,-1,8,36,29,-1,37,36,8,-1,6,38,37,-1,3,38,6,-1,39,38,3,-1,30,39,25,-1,41,40,30,-1,31,41,30,-1,42,41,31,-1,32,42,31,-1,43,42,32,-1,33,43,32,-1,44,43,33,-1,34,44,33,-1,45,44,34,-1,35,45,34,-1,46,45,35,-1,36,46,35,-1,47,46,36,-1,37,47,36,-1,38,47,37,-1,48,47,38,-1,49,48,38,-1,39,49,38,-1,40,49,39,-1,30,40,39,-1,48,49,50,-1,47,48,50,-1,46,47,50,-1,45,46,50,-1,44,45,50,-1,43,44,50,-1,42,43,50,-1,41,42,50,-1,40,41,50,-1,49,40,50,-1,11,13,15,-1,11,15,17,-1,9,11,17,-1,9,17,19,-1,7,9,19,-1,7,19,21,-1,5,7,21,-1,5,21,23,-1,5,23,0,-1,1,5,0,-1,3,4,39,-1,4,25,39,-1]
IndexedFaceSet88.creaseAngle = 1.57
Coordinate89 = x3d.Coordinate()

IndexedFaceSet88.coord = Coordinate89

Shape85.geometry = IndexedFaceSet88

HAnimSegment84.children.append(Shape85)

HAnimJoint83.children.append(HAnimSegment84)

HAnimJoint75.children.append(HAnimJoint83)

HAnimJoint67.children.append(HAnimJoint75)

HAnimJoint59.children.append(HAnimJoint67)
HAnimJoint90 = x3d.HAnimJoint()
HAnimJoint90.name = "r_hip"
HAnimJoint90.DEF = "hanim_r_hip"
HAnimJoint90.center = [-0.11,0.892362,-0.0732533]
HAnimJoint90.ulimit = [0,0,0]
HAnimJoint90.llimit = [0,0,0]
HAnimSegment91 = x3d.HAnimSegment()
HAnimSegment91.name = "r_thigh"
HAnimSegment91.DEF = "hanim_r_thigh"
Shape92 = x3d.Shape()
Appearance93 = x3d.Appearance()
Material94 = x3d.Material()
Material94.USE = "Pants_Color"

Appearance93.material = Material94
ImageTexture95 = x3d.ImageTexture()
ImageTexture95.USE = "camo"

Appearance93.texture = ImageTexture95

Shape92.appearance = Appearance93
IndexedFaceSet96 = x3d.IndexedFaceSet()
IndexedFaceSet96.coordIndex = [5,4,0,-1,0,4,3,-1,1,7,0,-1,7,8,0,-1,8,6,0,-1,6,5,0,-1,3,2,0,-1,2,1,0,-1,1,2,9,-1,2,3,10,-1,3,4,11,-1,4,5,12,-1,5,6,13,-1,8,7,15,-1,7,1,9,-1,9,15,7,-1,15,14,8,-1,13,16,5,-1,16,12,5,-1,12,11,4,-1,11,10,3,-1,10,9,2,-1,12,16,20,-1,13,14,22,-1,14,15,23,-1,24,23,15,-1,23,22,14,-1,20,19,12,-1,17,18,26,-1,18,19,27,-1,19,20,27,-1,20,21,28,-1,22,23,29,-1,30,29,23,-1,27,26,18,-1,26,25,17,-1,30,31,25,-1,25,26,29,-1,25,29,30,-1,26,27,28,-1,26,28,29,-1,27,20,28,-1,24,15,9,-1,22,21,13,-1,29,28,22,-1,28,21,22,-1,24,31,23,-1,31,30,23,-1,25,31,17,-1,31,24,17,-1,17,24,10,-1,24,9,10,-1,18,10,11,-1,18,17,10,-1,18,12,19,-1,18,11,12,-1,21,20,13,-1,20,16,13,-1,14,13,8,-1,13,6,8,-1]
IndexedFaceSet96.creaseAngle = 1.61
Coordinate97 = x3d.Coordinate()

IndexedFaceSet96.coord = Coordinate97

Shape92.geometry = IndexedFaceSet96

HAnimSegment91.children.append(Shape92)

HAnimJoint90.children.append(HAnimSegment91)
HAnimJoint98 = x3d.HAnimJoint()
HAnimJoint98.name = "r_knee"
HAnimJoint98.DEF = "hanim_r_knee"
HAnimJoint98.center = [-0.0699,0.51,-0.0166]
HAnimJoint98.ulimit = [0,0,0]
HAnimJoint98.llimit = [0,0,0]
HAnimSegment99 = x3d.HAnimSegment()
HAnimSegment99.name = "r_calf"
HAnimSegment99.DEF = "hanim_r_calf"
Shape100 = x3d.Shape()
Appearance101 = x3d.Appearance()
Material102 = x3d.Material()
Material102.USE = "Pants_Color"

Appearance101.material = Material102
ImageTexture103 = x3d.ImageTexture()
ImageTexture103.USE = "camo"

Appearance101.texture = ImageTexture103

Shape100.appearance = Appearance101
IndexedFaceSet104 = x3d.IndexedFaceSet()
IndexedFaceSet104.coordIndex = [14,25,18,-1,25,32,18,-1,32,27,18,-1,27,22,18,-1,22,10,18,-1,10,6,18,-1,6,8,18,-1,8,14,18,-1,14,8,17,-1,6,10,9,-1,10,22,24,-1,22,27,39,-1,27,32,39,-1,32,25,42,-1,25,14,30,-1,17,30,14,-1,30,42,25,-1,42,39,32,-1,39,24,22,-1,24,9,10,-1,4,17,8,-1,39,42,43,-1,30,43,42,-1,17,4,1,-1,24,39,26,-1,39,43,44,-1,30,17,34,-1,16,34,17,-1,34,43,30,-1,44,26,39,-1,0,1,4,-1,1,16,17,-1,16,1,3,-1,1,0,2,-1,0,5,7,-1,5,26,28,-1,26,44,45,-1,44,43,46,-1,43,34,36,-1,34,16,15,-1,15,36,34,-1,36,46,43,-1,46,45,44,-1,45,28,26,-1,28,7,5,-1,7,2,0,-1,2,3,1,-1,3,15,16,-1,45,46,37,-1,36,15,20,-1,36,37,46,-1,13,2,7,-1,3,20,15,-1,3,2,13,-1,36,20,29,-1,29,37,36,-1,13,21,23,-1,21,33,23,-1,41,37,40,-1,37,29,31,-1,29,20,19,-1,19,31,29,-1,31,40,37,-1,40,38,41,-1,35,23,33,-1,23,12,13,-1,12,11,13,-1,31,19,11,-1,40,31,11,-1,40,11,12,-1,12,23,38,-1,12,38,40,-1,23,35,38,-1,28,21,7,-1,21,13,7,-1,45,33,28,-1,33,21,28,-1,33,45,41,-1,45,37,41,-1,33,41,35,-1,41,38,35,-1,20,3,47,-1,11,19,47,-1,19,20,47,-1,13,47,3,-1,13,11,47,-1,4,8,6,-1,26,5,24,-1,5,9,24,-1,6,9,4,-1,9,0,4,-1,9,5,0,-1]
IndexedFaceSet104.creaseAngle = 1.57
Coordinate105 = x3d.Coordinate()

IndexedFaceSet104.coord = Coordinate105

Shape100.geometry = IndexedFaceSet104

HAnimSegment99.children.append(Shape100)

HAnimJoint98.children.append(HAnimSegment99)
HAnimJoint106 = x3d.HAnimJoint()
HAnimJoint106.name = "r_ankle"
HAnimJoint106.DEF = "hanim_r_ankle"
HAnimJoint106.center = [-0.064,0.0753,-0.0412]
HAnimJoint106.ulimit = [0,0,0]
HAnimJoint106.llimit = [0,0,0]
HAnimSegment107 = x3d.HAnimSegment()
HAnimSegment107.name = "r_hindfoot"
HAnimSegment107.DEF = "hanim_r_hindfoot"
Shape108 = x3d.Shape()
Appearance109 = x3d.Appearance()
Material110 = x3d.Material()
Material110.USE = "Shoe_Color"

Appearance109.material = Material110

Shape108.appearance = Appearance109
IndexedFaceSet111 = x3d.IndexedFaceSet()
IndexedFaceSet111.coordIndex = [6,50,0,-1,50,8,7,-1,50,7,0,-1,1,9,8,-1,1,8,50,-1,49,10,9,-1,49,9,1,-1,46,11,10,-1,46,10,49,-1,2,12,11,-1,2,11,46,-1,3,13,12,-1,3,12,2,-1,4,14,13,-1,4,13,3,-1,45,14,4,-1,47,15,45,-1,19,15,47,-1,48,18,19,-1,5,16,18,-1,5,18,48,-1,6,17,16,-1,6,16,5,-1,0,7,17,-1,0,17,6,-1,14,20,21,-1,14,21,13,-1,13,21,12,-1,12,21,22,-1,12,22,11,-1,11,22,10,-1,17,23,16,-1,16,23,24,-1,16,24,18,-1,18,24,25,-1,18,25,19,-1,19,25,26,-1,19,26,15,-1,15,26,20,-1,20,26,27,-1,20,27,21,-1,21,27,28,-1,21,28,22,-1,22,28,29,-1,10,30,9,-1,9,30,31,-1,9,31,8,-1,8,31,32,-1,17,32,23,-1,23,33,34,-1,23,34,35,-1,23,35,24,-1,24,35,36,-1,24,36,25,-1,25,36,37,-1,25,37,26,-1,26,37,38,-1,26,38,27,-1,27,38,39,-1,27,39,28,-1,28,39,40,-1,28,40,29,-1,29,40,41,-1,29,41,30,-1,30,41,42,-1,30,42,31,-1,31,42,43,-1,31,43,32,-1,32,43,33,-1,32,33,23,-1,44,43,42,-1,44,42,41,-1,44,41,40,-1,44,40,39,-1,44,39,38,-1,44,38,37,-1,44,37,36,-1,44,36,35,-1,44,35,34,-1,44,34,33,-1,44,33,43,-1,4,3,2,-1,45,4,2,-1,45,2,46,-1,47,45,46,-1,48,46,49,-1,5,48,49,-1,5,49,1,-1,6,5,1,-1,6,1,50,-1,30,10,29,-1,10,22,29,-1,17,7,32,-1,7,8,32,-1,19,47,48,-1,47,46,48,-1,20,14,15,-1,14,45,15,-1]
IndexedFaceSet111.creaseAngle = 1.57
Coordinate112 = x3d.Coordinate()

IndexedFaceSet111.coord = Coordinate112

Shape108.geometry = IndexedFaceSet111

HAnimSegment107.children.append(Shape108)

HAnimJoint106.children.append(HAnimSegment107)

HAnimJoint98.children.append(HAnimJoint106)

HAnimJoint90.children.append(HAnimJoint98)

HAnimJoint59.children.append(HAnimJoint90)

HAnimJoint58.children.append(HAnimJoint59)
HAnimJoint113 = x3d.HAnimJoint()
HAnimJoint113.name = "vl1"
HAnimJoint113.DEF = "hanim_vl1"
HAnimJoint113.center = [-0.00405,1.07,-0.0275]
HAnimJoint113.ulimit = [0,0,0]
HAnimJoint113.llimit = [0,0,0]
HAnimSegment114 = x3d.HAnimSegment()
HAnimSegment114.name = "l1"
HAnimSegment114.DEF = "hanim_l1"
Transform115 = x3d.Transform()
Group116 = x3d.Group()
Transform117 = x3d.Transform()
Transform117.scale = [1.1,1.1,1.1]
Transform117.translation = [0,-0.12,0]
Shape118 = x3d.Shape()
Appearance119 = x3d.Appearance()
Material120 = x3d.Material()
Material120.DEF = "JacketColor"
Material120.diffuseColor = [0.01,0.28,0.01]

Appearance119.material = Material120

Shape118.appearance = Appearance119
IndexedFaceSet121 = x3d.IndexedFaceSet()
IndexedFaceSet121.coordIndex = [4,5,6,-1,6,7,4,-1,8,7,6,-1,6,9,8,-1,9,10,8,-1,6,5,11,-1,9,6,12,-1,11,12,6,-1,12,10,9,-1,7,8,13,-1,13,4,7,-1,14,15,16,-1,15,17,13,-1,4,13,17,-1,17,15,18,-1,13,19,15,-1,19,13,8,-1,19,16,15,-1,16,19,8,-1,17,20,4,-1,5,4,20,-1,18,21,17,-1,20,17,21,-1,16,22,14,-1,22,16,23,-1,8,23,16,-1,23,8,10,-1,24,25,26,-1,26,27,24,-1,25,28,26,-1,28,29,30,-1,30,26,28,-1,25,24,34,-1,33,25,34,-1,24,35,34,-1,27,35,24,-1,27,26,37,-1,37,26,30,-1,38,37,30,-1,33,34,39,-1,39,34,35,-1,41,38,30,-1,35,27,42,-1,37,42,27,-1,42,37,43,-1,37,38,44,-1,44,43,37,-1,43,47,42,-1,47,43,49,-1,43,44,49,-1,50,49,44,-1,33,39,53,-1,49,54,47,-1,59,58,53,-1,53,39,59,-1,58,59,60,-1,54,49,61,-1,49,50,62,-1,63,62,50,-1,62,61,49,-1,64,63,50,-1,63,64,65,-1,65,62,63,-1,66,60,61,-1,62,65,67,-1,68,67,65,-1,64,69,70,-1,64,70,65,-1,70,68,65,-1,69,71,72,-1,72,70,69,-1,66,76,60,-1,67,77,62,-1,62,77,61,-1,77,66,61,-1,66,77,78,-1,77,67,79,-1,79,67,68,-1,79,78,77,-1,68,70,80,-1,70,72,80,-1,80,79,68,-1,73,76,82,-1,76,66,83,-1,78,83,66,-1,83,82,76,-1,78,79,84,-1,79,80,84,-1,84,85,78,-1,86,84,80,-1,82,83,89,-1,83,78,89,-1,89,87,82,-1,78,85,89,-1,90,91,92,-1,92,93,90,-1,90,94,91,-1,95,96,94,-1,94,90,95,-1,29,96,97,-1,96,95,97,-1,97,30,29,-1,30,97,41,-1,41,97,95,-1,101,92,91,-1,98,101,91,-1,101,102,92,-1,92,102,93,-1,104,90,93,-1,90,104,95,-1,95,105,41,-1,104,105,95,-1,106,101,98,-1,102,101,106,-1,107,93,102,-1,93,107,104,-1,108,104,107,-1,107,109,108,-1,110,105,104,-1,104,108,110,-1,113,110,108,-1,110,113,114,-1,119,108,109,-1,108,119,113,-1,120,113,119,-1,119,121,120,-1,117,124,125,-1,106,117,125,-1,127,114,113,-1,114,127,128,-1,113,120,127,-1,114,128,129,-1,131,120,121,-1,131,127,120,-1,132,129,128,-1,128,127,132,-1,121,135,131,-1,136,132,127,-1,132,136,137,-1,138,71,129,-1,138,129,132,-1,137,138,132,-1,139,72,71,-1,72,139,80,-1,71,138,139,-1,140,135,121,-1,140,121,125,-1,141,127,131,-1,127,141,136,-1,131,135,141,-1,142,141,135,-1,143,136,141,-1,136,143,137,-1,141,142,143,-1,144,138,137,-1,144,139,138,-1,143,144,137,-1,145,140,146,-1,147,135,140,-1,135,147,142,-1,140,145,147,-1,148,80,139,-1,80,148,86,-1,139,144,148,-1,149,143,142,-1,149,144,143,-1,142,150,149,-1,151,148,144,-1,144,149,151,-1,153,147,145,-1,153,142,147,-1,145,152,153,-1,153,150,142,-1,154,86,148,-1,148,151,154,-1,76,157,60,-1,76,73,158,157,-1,60,162,58,-1,162,60,157,-1,166,58,162,-1,165,166,159,-1,166,162,157,158,159,-1,140,125,167,-1,124,168,125,-1,168,167,125,-1,124,169,168,-1,146,140,167,170,-1,168,170,167,-1,168,169,170,-1,146,170,171,-1,169,171,170,-1,98,117,106,-1]
IndexedFaceSet121.creaseAngle = 1.59
Coordinate122 = x3d.Coordinate()

IndexedFaceSet121.coord = Coordinate122
TextureCoordinate123 = x3d.TextureCoordinate()

IndexedFaceSet121.texCoord = TextureCoordinate123

Shape118.geometry = IndexedFaceSet121

Transform117.children.append(Shape118)

Group116.children.append(Transform117)

Transform115.children.append(Group116)

HAnimSegment114.children.append(Transform115)
Shape124 = x3d.Shape()
Appearance125 = x3d.Appearance()
Material126 = x3d.Material()
Material126.DEF = "Shirt_Color"
Material126.ambientIntensity = 0.25
Material126.diffuseColor = [0.6,0.0745,0.1137]

Appearance125.material = Material126
ImageTexture127 = x3d.ImageTexture()
ImageTexture127.DEF = "small_logo_Tex"
ImageTexture127.url = ["small_logo.gif","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Legacy/small_logo.gif"]

Appearance125.texture = ImageTexture127

Shape124.appearance = Appearance125
IndexedFaceSet128 = x3d.IndexedFaceSet()
IndexedFaceSet128.coordIndex = [0,1,2,-1,3,0,2,-1,4,5,6,-1,6,7,4,-1,8,7,6,-1,6,9,8,-1,9,10,8,-1,6,5,11,-1,9,6,12,-1,11,12,6,-1,12,10,9,-1,7,8,13,-1,13,4,7,-1,14,15,16,-1,15,17,13,-1,4,13,17,-1,17,15,18,-1,13,19,15,-1,19,13,8,-1,19,16,15,-1,16,19,8,-1,17,20,4,-1,5,4,20,-1,18,21,17,-1,20,17,21,-1,16,22,14,-1,22,16,23,-1,8,23,16,-1,23,8,10,-1,24,25,26,-1,26,27,24,-1,25,28,26,-1,28,29,30,-1,30,26,28,-1,31,32,33,-1,32,25,33,-1,25,24,34,-1,33,25,34,-1,24,35,34,-1,27,35,24,-1,33,36,31,-1,27,26,37,-1,37,26,30,-1,38,37,30,-1,33,34,39,-1,39,34,35,-1,39,35,40,-1,41,38,30,-1,35,27,42,-1,37,42,27,-1,40,35,42,-1,42,37,43,-1,37,38,44,-1,44,43,37,-1,36,45,46,-1,36,33,45,-1,40,42,47,-1,43,47,42,-1,47,48,40,-1,39,40,48,-1,47,43,49,-1,43,44,49,-1,50,49,44,-1,51,46,52,-1,46,45,52,-1,52,45,53,-1,33,53,45,-1,33,39,53,-1,49,54,47,-1,48,47,54,-1,55,56,52,-1,57,52,53,-1,57,55,52,-1,58,57,53,-1,59,58,53,-1,53,39,59,-1,39,48,59,-1,59,48,54,-1,58,59,60,-1,54,49,61,-1,59,54,61,-1,60,59,61,-1,49,50,62,-1,63,62,50,-1,62,61,49,-1,64,63,50,-1,63,64,65,-1,65,62,63,-1,66,60,61,-1,62,65,67,-1,68,67,65,-1,64,69,70,-1,64,70,65,-1,70,68,65,-1,69,71,72,-1,72,70,69,-1,73,74,75,-1,66,76,60,-1,67,77,62,-1,62,77,61,-1,77,66,61,-1,66,77,78,-1,77,67,79,-1,79,67,68,-1,79,78,77,-1,68,70,80,-1,70,72,80,-1,80,79,68,-1,74,73,81,-1,73,76,82,-1,82,81,73,-1,76,66,83,-1,78,83,66,-1,83,82,76,-1,78,79,84,-1,79,80,84,-1,84,85,78,-1,86,84,80,-1,81,82,87,-1,87,88,81,-1,82,83,89,-1,83,78,89,-1,89,87,82,-1,78,85,89,-1,90,91,92,-1,92,93,90,-1,90,94,91,-1,95,96,94,-1,94,90,95,-1,29,96,97,-1,96,95,97,-1,97,30,29,-1,30,97,41,-1,41,97,95,-1,98,99,100,-1,98,91,99,-1,101,92,91,-1,98,101,91,-1,101,102,92,-1,92,102,93,-1,36,103,31,-1,51,103,36,46,-1,103,100,31,-1,100,103,98,-1,104,90,93,-1,90,104,95,-1,95,105,41,-1,104,105,95,-1,106,101,98,-1,102,101,106,-1,107,93,102,-1,93,107,104,-1,108,104,107,-1,107,109,108,-1,110,105,104,-1,104,108,110,-1,109,107,111,-1,107,102,111,-1,111,102,106,-1,111,112,109,-1,106,112,111,-1,113,110,108,-1,110,113,114,-1,51,52,115,-1,116,115,117,-1,117,106,116,-1,118,109,112,-1,119,108,109,-1,108,119,113,-1,109,118,119,-1,120,113,119,-1,119,121,120,-1,52,56,122,-1,122,115,52,-1,115,122,123,-1,117,124,125,-1,106,117,125,-1,118,112,106,125,-1,119,118,125,-1,121,119,125,-1,126,124,123,-1,127,114,113,-1,114,127,128,-1,113,120,127,-1,114,128,129,-1,130,126,123,-1,122,130,123,-1,131,120,121,-1,131,127,120,-1,132,129,128,-1,128,127,132,-1,74,81,133,-1,81,134,133,-1,121,135,131,-1,136,132,127,-1,132,136,137,-1,138,71,129,-1,138,129,132,-1,137,138,132,-1,139,72,71,-1,72,139,80,-1,71,138,139,-1,140,135,121,-1,140,121,125,-1,141,127,131,-1,127,141,136,-1,131,135,141,-1,142,141,135,-1,143,136,141,-1,136,143,137,-1,141,142,143,-1,144,138,137,-1,144,139,138,-1,143,144,137,-1,145,146,134,-1,145,140,146,-1,134,81,145,-1,147,135,140,-1,135,147,142,-1,140,145,147,-1,148,80,139,-1,80,148,86,-1,139,144,148,-1,149,143,142,-1,149,144,143,-1,142,150,149,-1,151,148,144,-1,144,149,151,-1,152,145,81,-1,81,88,152,-1,153,147,145,-1,153,142,147,-1,145,152,153,-1,153,150,142,-1,154,86,148,-1,148,151,154,-1,155,28,25,-1,155,29,28,-1,155,25,32,-1,155,32,31,-1,155,31,100,-1,155,100,99,-1,155,99,91,-1,155,91,94,-1,155,94,96,-1,155,96,29,-1,156,151,149,-1,156,154,151,-1,156,149,150,-1,156,150,153,-1,156,153,152,-1,156,152,88,-1,156,88,87,-1,156,87,89,-1,156,89,85,-1,156,85,84,-1,156,84,86,-1,156,86,154,-1,76,157,60,-1,76,73,158,157,-1,159,158,73,75,160,-1,161,56,55,-1,60,162,58,-1,162,60,157,-1,161,55,163,-1,57,164,163,55,-1,160,163,164,-1,160,164,159,-1,164,57,165,-1,164,165,159,-1,57,58,166,165,-1,166,58,162,-1,165,166,159,-1,166,162,157,158,159,-1,140,125,167,-1,124,168,125,-1,168,167,125,-1,124,169,168,-1,146,140,167,170,-1,168,170,167,-1,168,169,170,-1,146,170,171,-1,169,171,170,-1,172,134,146,171,-1,134,172,130,-1,169,124,126,173,-1,173,126,130,-1,169,173,172,171,-1,173,130,172,-1,122,74,133,174,-1,133,134,174,-1,130,122,174,-1,134,130,174,-1,122,56,175,74,-1,74,175,176,-1,175,56,161,176,-1,74,176,75,-1,176,161,163,-1,176,160,75,-1,176,163,160,-1,115,116,177,51,-1,106,98,177,116,-1,51,177,103,-1,177,98,103,-1]
IndexedFaceSet128.creaseAngle = 1.59
Coordinate129 = x3d.Coordinate()

IndexedFaceSet128.coord = Coordinate129
TextureCoordinate130 = x3d.TextureCoordinate()

IndexedFaceSet128.texCoord = TextureCoordinate130

Shape124.geometry = IndexedFaceSet128

HAnimSegment114.children.append(Shape124)

HAnimJoint113.children.append(HAnimSegment114)
HAnimJoint131 = x3d.HAnimJoint()
HAnimJoint131.name = "l_shoulder"
HAnimJoint131.DEF = "hanim_l_shoulder"
HAnimJoint131.center = [0.167,1.36,-0.0518]
HAnimJoint131.ulimit = [0,0,0]
HAnimJoint131.llimit = [0,0,0]
HAnimSegment132 = x3d.HAnimSegment()
HAnimSegment132.name = "l_upperarm"
HAnimSegment132.DEF = "hanim_l_upperarm"
Transform133 = x3d.Transform()
Transform133.DEF = "l_upperarm_adjust"
Transform133.center = [0.182,1.22,-0.047]
Transform133.rotation = [1,0,0,0.119]
Transform133.translation = [0.167,1.36,-0.0518]
Shape134 = x3d.Shape()
Appearance135 = x3d.Appearance()
Material136 = x3d.Material()
Material136.DEF = "Skin_Color"
Material136.ambientIntensity = 0.25
Material136.diffuseColor = [0.749,0.601,0.462]

Appearance135.material = Material136

Shape134.appearance = Appearance135
IndexedFaceSet137 = x3d.IndexedFaceSet()
IndexedFaceSet137.coordIndex = [2,1,0,-1,2,3,1,-1,2,4,3,-1,2,0,5,-1,6,5,0,-1,7,2,5,-1,8,4,2,-1,8,3,4,-1,9,1,3,-1,10,0,1,-1,0,10,6,-1,1,9,10,-1,3,8,9,-1,2,7,8,-1,5,6,7,-1,11,7,6,-1,14,9,8,-1,15,10,9,-1,11,6,10,-1,10,15,11,-1,9,14,15,-1,8,13,14,-1,8,16,13,-1,7,11,12,-1,21,15,14,-1,15,17,11,-1,15,21,17,-1,16,19,13,-1,13,19,20,-1,21,14,20,-1,14,13,20,-1,12,17,18,-1,12,11,17,-1,12,18,16,-1,18,19,16,-1,12,16,7,-1,16,8,7,-1,19,18,17,-1,20,19,21,-1,19,17,21,-1]
IndexedFaceSet137.creaseAngle = 1.65
Coordinate138 = x3d.Coordinate()

IndexedFaceSet137.coord = Coordinate138

Shape134.geometry = IndexedFaceSet137

Transform133.children.append(Shape134)

HAnimSegment132.children.append(Transform133)

HAnimJoint131.children.append(HAnimSegment132)
HAnimJoint139 = x3d.HAnimJoint()
HAnimJoint139.name = "l_elbow"
HAnimJoint139.DEF = "hanim_l_elbow"
HAnimJoint139.center = [0.196,1.07,-0.0518]
HAnimJoint139.ulimit = [0,0,0]
HAnimJoint139.llimit = [0,0,0]
HAnimSegment140 = x3d.HAnimSegment()
HAnimSegment140.name = "l_forearm"
HAnimSegment140.DEF = "hanim_l_forearm"
Transform141 = x3d.Transform()
Transform141.DEF = "l_forearm_adjust"
Transform141.center = [0.198,0.961,-0.0405]
Transform141.rotation = [-1,0,0,0.1]
Transform141.translation = [0.196,1.07,-0.0518]
Shape142 = x3d.Shape()
Appearance143 = x3d.Appearance()
Material144 = x3d.Material()
Material144.USE = "Skin_Color"

Appearance143.material = Material144

Shape142.appearance = Appearance143
IndexedFaceSet145 = x3d.IndexedFaceSet()
IndexedFaceSet145.coordIndex = [2,1,0,-1,2,3,1,-1,2,4,3,-1,2,5,4,-1,2,6,5,-1,2,0,6,-1,7,6,0,-1,8,5,6,-1,9,4,5,-1,9,3,4,-1,10,1,3,-1,11,0,1,-1,0,11,7,-1,1,10,11,-1,3,9,10,-1,5,12,9,-1,5,8,12,-1,6,7,8,-1,17,16,15,-1,14,17,15,-1,14,18,17,-1,13,18,14,-1,16,17,10,-1,16,10,9,-1,15,16,9,-1,15,9,12,-1,18,13,7,-1,18,7,11,-1,13,14,8,-1,13,8,7,-1,14,15,8,-1,15,12,8,-1,17,18,10,-1,18,11,10,-1]
IndexedFaceSet145.creaseAngle = 1.75
Coordinate146 = x3d.Coordinate()

IndexedFaceSet145.coord = Coordinate146

Shape142.geometry = IndexedFaceSet145

Transform141.children.append(Shape142)

HAnimSegment140.children.append(Transform141)

HAnimJoint139.children.append(HAnimSegment140)
HAnimJoint147 = x3d.HAnimJoint()
HAnimJoint147.name = "l_wrist"
HAnimJoint147.DEF = "hanim_l_wrist"
HAnimJoint147.center = [0.213,0.811,-0.0338]
HAnimJoint147.ulimit = [0,0,0]
HAnimJoint147.llimit = [0,0,0]
HAnimSegment148 = x3d.HAnimSegment()
HAnimSegment148.name = "l_hand"
HAnimSegment148.DEF = "hanim_l_hand"
Transform149 = x3d.Transform()
Transform149.DEF = "l_hand_adjust"
Transform149.center = [0.213,0.811,-0.0338]
Transform149.rotation = [-0.06361,-0.9967,0.04988,1.333]
Transform149.translation = [0.213,0.811,-0.0338]
Shape150 = x3d.Shape()
Appearance151 = x3d.Appearance()
Material152 = x3d.Material()
Material152.USE = "Skin_Color"

Appearance151.material = Material152

Shape150.appearance = Appearance151
IndexedFaceSet153 = x3d.IndexedFaceSet()
IndexedFaceSet153.coordIndex = [2,1,0,-1,5,4,3,-1,3,7,6,-1,2,3,6,-1,7,9,8,-1,6,7,8,-1,9,11,10,-1,8,9,10,-1,11,13,12,-1,10,11,12,-1,13,15,14,-1,12,13,14,-1,15,17,16,-1,14,15,16,-1,17,19,18,-1,16,17,18,-1,19,21,20,-1,18,19,20,-1,31,4,1,-1,4,5,0,-1,1,4,0,-1,5,3,2,-1,0,5,2,-1,26,25,24,-1,26,24,23,-1,27,26,23,-1,28,27,23,-1,28,23,22,-1,29,28,22,-1,29,22,21,-1,30,29,21,-1,15,13,11,-1,17,15,11,-1,19,17,11,-1,19,11,9,-1,31,19,9,-1,31,9,7,-1,4,31,7,-1,4,7,3,-1,30,21,19,-1,31,30,19,-1,12,14,16,-1,10,12,16,-1,10,16,18,-1,8,10,18,-1,6,8,1,-1,2,6,1,-1,39,38,37,-1,37,38,40,-1,37,40,36,-1,36,40,41,-1,36,41,35,-1,35,41,42,-1,35,42,34,-1,34,42,43,-1,34,43,33,-1,33,43,44,-1,33,44,32,-1,20,32,44,-1,20,44,45,-1,20,45,46,-1,47,8,18,-1,47,18,20,-1,47,20,46,-1,8,47,1,-1,22,33,32,-1,23,35,34,-1,23,36,35,-1,37,24,25,-1,40,38,27,-1,29,43,42,-1,45,44,30,-1,47,31,1,-1,47,46,31,-1,29,30,43,-1,30,44,43,-1,45,31,46,-1,45,30,31,-1,28,29,41,-1,29,42,41,-1,28,40,27,-1,28,41,40,-1,26,27,39,-1,27,38,39,-1,25,39,37,-1,25,26,39,-1,24,36,23,-1,24,37,36,-1,23,34,22,-1,34,33,22,-1,22,32,21,-1,32,20,21,-1]
IndexedFaceSet153.creaseAngle = 1.48
Coordinate154 = x3d.Coordinate()

IndexedFaceSet153.coord = Coordinate154

Shape150.geometry = IndexedFaceSet153

Transform149.children.append(Shape150)

HAnimSegment148.children.append(Transform149)

HAnimJoint147.children.append(HAnimSegment148)

HAnimJoint139.children.append(HAnimJoint147)

HAnimJoint131.children.append(HAnimJoint139)

HAnimJoint113.children.append(HAnimJoint131)
HAnimJoint155 = x3d.HAnimJoint()
HAnimJoint155.name = "r_shoulder"
HAnimJoint155.DEF = "hanim_r_shoulder"
HAnimJoint155.center = [-0.167,1.36,-0.0458]
HAnimJoint155.ulimit = [0,0,0]
HAnimJoint155.llimit = [0,0,0]
HAnimSegment156 = x3d.HAnimSegment()
HAnimSegment156.name = "r_upperarm"
HAnimSegment156.DEF = "hanim_r_upperarm"
Transform157 = x3d.Transform()
Transform157.DEF = "r_upperarm_adjust"
Transform157.center = [-0.182,1.22,-0.047]
Transform157.rotation = [1,0,0,0.0836]
Transform157.translation = [-0.167,1.36,-0.0458]
Shape158 = x3d.Shape()
Appearance159 = x3d.Appearance()
Material160 = x3d.Material()
Material160.USE = "Skin_Color"

Appearance159.material = Material160

Shape158.appearance = Appearance159
IndexedFaceSet161 = x3d.IndexedFaceSet()
IndexedFaceSet161.coordIndex = [14,10,20,-1,10,13,20,-1,13,22,20,-1,19,14,20,-1,14,19,12,-1,19,20,24,-1,20,22,25,-1,22,13,25,-1,13,10,11,-1,10,14,5,-1,12,5,14,-1,5,11,10,-1,11,25,13,-1,25,24,20,-1,24,12,19,-1,12,24,9,-1,25,11,8,-1,11,5,2,-1,5,12,9,-1,9,2,5,-1,2,8,11,-1,8,23,25,-1,23,27,25,-1,21,9,24,-1,9,21,7,-1,27,23,18,-1,23,8,18,-1,8,2,6,-1,2,9,7,-1,7,1,2,-1,1,6,2,-1,6,18,8,-1,18,26,27,-1,16,7,21,-1,7,16,4,-1,16,26,17,-1,26,18,15,-1,18,6,3,-1,6,1,0,-1,1,7,0,-1,4,0,7,-1,0,3,6,-1,3,15,18,-1,15,17,26,-1,17,4,16,-1,3,0,15,-1,15,0,4,-1,15,4,17,-1,25,27,24,-1,27,21,24,-1,27,26,21,-1,26,16,21,-1]
IndexedFaceSet161.creaseAngle = 1.53
Coordinate162 = x3d.Coordinate()

IndexedFaceSet161.coord = Coordinate162

Shape158.geometry = IndexedFaceSet161

Transform157.children.append(Shape158)

HAnimSegment156.children.append(Transform157)

HAnimJoint155.children.append(HAnimSegment156)
HAnimJoint163 = x3d.HAnimJoint()
HAnimJoint163.name = "r_elbow"
HAnimJoint163.DEF = "hanim_r_elbow"
HAnimJoint163.center = [-0.192,1.07,-0.0498]
HAnimJoint163.ulimit = [0,0,0]
HAnimJoint163.llimit = [0,0,0]
HAnimSegment164 = x3d.HAnimSegment()
HAnimSegment164.name = "r_forearm"
HAnimSegment164.DEF = "hanim_r_forearm"
Transform165 = x3d.Transform()
Transform165.DEF = "r_forearm_adjust"
Transform165.center = [-0.198,0.961,-0.0397]
Transform165.rotation = [-1,0,0,0.1254]
Transform165.translation = [-0.192,1.07,-0.0498]
Shape166 = x3d.Shape()
Appearance167 = x3d.Appearance()
Material168 = x3d.Material()
Material168.USE = "Skin_Color"

Appearance167.material = Material168

Shape166.appearance = Appearance167
IndexedFaceSet169 = x3d.IndexedFaceSet()
IndexedFaceSet169.coordIndex = [20,13,15,-1,13,8,15,-1,8,12,15,-1,12,18,15,-1,18,22,15,-1,22,20,15,-1,20,22,21,-1,22,18,24,-1,18,12,7,-1,12,8,7,-1,8,13,3,-1,13,20,10,-1,21,10,20,-1,10,3,13,-1,3,7,8,-1,7,19,18,-1,19,24,18,-1,24,21,22,-1,21,24,23,-1,24,19,16,-1,19,7,6,-1,7,3,1,-1,3,10,5,-1,10,21,17,-1,17,5,10,-1,5,1,3,-1,1,6,7,-1,6,16,19,-1,16,23,24,-1,23,17,21,-1,1,5,2,-1,5,17,9,-1,9,2,5,-1,1,4,6,-1,4,16,6,-1,23,9,17,-1,9,23,14,-1,23,16,11,-1,4,11,16,-1,11,14,23,-1,11,4,0,-1,11,0,14,-1,0,2,14,-1,14,2,9,-1,2,0,1,-1,0,4,1,-1]
IndexedFaceSet169.creaseAngle = 1.73
Coordinate170 = x3d.Coordinate()

IndexedFaceSet169.coord = Coordinate170

Shape166.geometry = IndexedFaceSet169

Transform165.children.append(Shape166)

HAnimSegment164.children.append(Transform165)

HAnimJoint163.children.append(HAnimSegment164)
HAnimJoint171 = x3d.HAnimJoint()
HAnimJoint171.name = "r_wrist"
HAnimJoint171.DEF = "hanim_r_wrist"
HAnimJoint171.center = [-0.217,0.811,-0.0338]
HAnimJoint171.ulimit = [0,0,0]
HAnimJoint171.llimit = [0,0,0]
HAnimSegment172 = x3d.HAnimSegment()
HAnimSegment172.name = "r_hand"
HAnimSegment172.DEF = "hanim_r_hand"
Group173 = x3d.Group()
Transform174 = x3d.Transform()
Transform174.DEF = "r_hand_adjust"
Transform174.center = [-0.217,0.811,-0.0338]
Transform174.rotation = [-0.09024,0.994,-0.0624,1.216]
Shape175 = x3d.Shape()
Appearance176 = x3d.Appearance()
Material177 = x3d.Material()
Material177.USE = "Skin_Color"

Appearance176.material = Material177

Shape175.appearance = Appearance176
IndexedFaceSet178 = x3d.IndexedFaceSet()
IndexedFaceSet178.coordIndex = [10,9,0,-1,11,30,31,-1,1,12,11,-1,1,11,0,-1,2,13,12,-1,2,12,1,-1,3,14,13,-1,3,13,2,-1,4,15,14,-1,4,14,3,-1,5,16,15,-1,5,15,4,-1,6,17,16,-1,6,16,5,-1,7,18,17,-1,7,17,6,-1,8,19,18,-1,8,18,7,-1,10,31,30,-1,10,30,9,-1,0,11,31,-1,0,31,10,-1,22,23,24,-1,21,22,24,-1,21,24,25,-1,21,25,26,-1,20,21,26,-1,20,26,27,-1,19,20,27,-1,19,27,28,-1,14,15,16,-1,14,16,17,-1,14,17,18,-1,13,14,18,-1,13,18,29,-1,12,13,29,-1,12,29,30,-1,11,12,30,-1,18,19,28,-1,18,28,29,-1,6,5,4,-1,6,4,3,-1,7,6,3,-1,7,3,2,-1,9,2,1,-1,9,1,0,-1,32,38,33,-1,33,38,39,-1,33,39,34,-1,34,39,40,-1,34,40,35,-1,35,40,41,-1,35,41,36,-1,36,41,42,-1,36,42,37,-1,37,42,43,-1,37,43,44,-1,44,43,8,-1,44,8,45,-1,45,8,46,-1,46,8,7,-1,46,7,2,-1,46,2,47,-1,9,47,2,-1,25,34,35,-1,25,33,34,-1,25,24,33,-1,24,32,33,-1,32,24,23,-1,40,39,21,-1,41,40,21,-1,43,19,8,-1,43,20,19,-1,43,42,20,-1,21,20,41,-1,20,42,41,-1,38,22,39,-1,22,21,39,-1,32,23,38,-1,23,22,38,-1,26,25,35,-1,27,36,37,-1,27,37,28,-1,37,44,28,-1,26,35,27,-1,35,36,27,-1,28,44,45,-1,29,46,47,-1,29,9,30,-1,29,47,9,-1,28,45,29,-1,45,46,29,-1]
IndexedFaceSet178.creaseAngle = 1.57
Coordinate179 = x3d.Coordinate()

IndexedFaceSet178.coord = Coordinate179

Shape175.geometry = IndexedFaceSet178

Transform174.children.append(Shape175)

Group173.children.append(Transform174)
Transform180 = x3d.Transform()
Transform180.center = [-0.8,0.45,0.1]
Transform180.rotation = [0,0,1,-2.7]
Transform180.scale = [0.1,0.1,0.1]
Transform181 = x3d.Transform()
Transform181.rotation = [1,0,0,1.57]
Transform181.translation = [-0.7,0,0]
ProtoInstance182 = x3d.ProtoInstance()
ProtoInstance182.name = "RifleM24"
ProtoInstance182.DEF = "rifleM24"

Transform181.children.append(ProtoInstance182)
Script183 = x3d.Script()
Script183.DEF = "FireScript"
field184 = x3d.field()
field184.name = "fire"
field184.accessType = "outputOnly"
field184.type = "SFBool"

Script183.field.append(field184)
field185 = x3d.field()
field185.name = "enabled"
field185.accessType = "inputOnly"
field185.type = "SFBool"

Script183.field.append(field185)

Script183.sourceCode = '''ecmascript:\n"+
"\n"+
"function enabled (value, timeStamp)\n"+
"{\n"+
"        //print ('enabled value =' + value);\n"+
"        if (value == true)\n"+
"           fire = value;\n"+
"}'''

Transform181.children.append(Script183)
TouchSensor186 = x3d.TouchSensor()
TouchSensor186.DEF = "FireTouchSensor"
TouchSensor186.description = "click for shoot rifle"

Transform181.children.append(TouchSensor186)
ROUTE187 = x3d.ROUTE()
ROUTE187.fromField = "isOver"
ROUTE187.fromNode = "FireTouchSensor"
ROUTE187.toField = "enabled"
ROUTE187.toNode = "FireScript"

Transform181.children.append(ROUTE187)
ROUTE188 = x3d.ROUTE()
ROUTE188.fromField = "touchTime"
ROUTE188.fromNode = "FireTouchSensor"
ROUTE188.toField = "animationStartTime"
ROUTE188.toNode = "rifleM24"

Transform181.children.append(ROUTE188)
ROUTE189 = x3d.ROUTE()
ROUTE189.fromField = "fire"
ROUTE189.fromNode = "FireScript"
ROUTE189.toField = "trigger"
ROUTE189.toNode = "rifleM24"

Transform181.children.append(ROUTE189)

Transform180.children.append(Transform181)

Group173.children.append(Transform180)

HAnimSegment172.children.append(Group173)

HAnimJoint171.children.append(HAnimSegment172)

HAnimJoint163.children.append(HAnimJoint171)

HAnimJoint155.children.append(HAnimJoint163)

HAnimJoint113.children.append(HAnimJoint155)
HAnimJoint190 = x3d.HAnimJoint()
HAnimJoint190.name = "vc4"
HAnimJoint190.DEF = "hanim_vc4"
HAnimJoint190.center = [0,1.43,-0.0458]
HAnimJoint190.ulimit = [0,0,0]
HAnimJoint190.llimit = [0,0,0]
HAnimSegment191 = x3d.HAnimSegment()
HAnimSegment191.name = "c4"
HAnimSegment191.DEF = "hanim_c4"
Shape192 = x3d.Shape()
Appearance193 = x3d.Appearance()
Material194 = x3d.Material()
Material194.USE = "Skin_Color"

Appearance193.material = Material194

Shape192.appearance = Appearance193
IndexedFaceSet195 = x3d.IndexedFaceSet()
IndexedFaceSet195.DEF = "neck"
IndexedFaceSet195.coordIndex = [6,5,2,-1,6,2,3,-1,5,4,1,-1,5,1,2,-1,4,7,0,-1,4,0,1,-1,11,10,9,-1,11,9,8,-1,10,13,12,-1,10,12,9,-1,13,15,14,-1,13,14,12,-1,6,3,11,-1,6,11,8,-1,7,14,15,-1,7,15,0,-1,2,10,11,-1,2,11,3,-1,2,1,13,-1,2,13,10,-1,1,0,15,-1,1,15,13,-1,9,5,6,-1,9,6,8,-1,9,12,4,-1,9,4,5,-1,12,14,7,-1,12,7,4,-1]
IndexedFaceSet195.creaseAngle = 1.91
Coordinate196 = x3d.Coordinate()

IndexedFaceSet195.coord = Coordinate196

Shape192.geometry = IndexedFaceSet195

HAnimSegment191.children.append(Shape192)

HAnimJoint190.children.append(HAnimSegment191)
HAnimJoint197 = x3d.HAnimJoint()
HAnimJoint197.name = "skullbase"
HAnimJoint197.DEF = "hanim_skullbase"
HAnimJoint197.center = [0,1.54,-0.0409]
HAnimJoint197.ulimit = [0,0,0]
HAnimJoint197.llimit = [0,0,0]
HAnimSegment198 = x3d.HAnimSegment()
HAnimSegment198.name = "skull"
HAnimSegment198.DEF = "hanim_skull"
Group199 = x3d.Group()
Transform200 = x3d.Transform()
Transform200.DEF = "helmet"
Transform200.scale = [0.105,0.135,0.125]
Transform200.translation = [0,1.6,-0.05]
Shape201 = x3d.Shape()
Appearance202 = x3d.Appearance()
Material203 = x3d.Material()

Appearance202.material = Material203
ImageTexture204 = x3d.ImageTexture()
ImageTexture204.USE = "camo"

Appearance202.texture = ImageTexture204

Shape201.appearance = Appearance202
IndexedFaceSet205 = x3d.IndexedFaceSet()
IndexedFaceSet205.coordIndex = [0,1,2,-1,1,3,4,-1,2,4,5,-1,3,6,7,-1,4,7,8,-1,5,8,9,-1,6,10,11,-1,7,11,12,-1,8,12,13,-1,9,13,14,-1,10,15,16,-1,11,16,17,-1,12,17,18,-1,13,18,19,-1,14,19,20,-1,1,4,2,-1,3,7,4,-1,4,8,5,-1,6,11,7,-1,7,12,8,-1,8,13,9,-1,10,16,11,-1,11,17,12,-1,12,18,13,-1,13,19,14,-1,21,22,23,-1,22,24,25,-1,23,25,26,-1,24,27,28,-1,25,28,29,-1,26,29,30,-1,27,31,32,-1,28,32,33,-1,29,33,34,-1,30,34,35,-1,31,0,2,-1,32,2,5,-1,33,5,9,-1,34,9,14,-1,35,14,20,-1,22,25,23,-1,24,28,25,-1,25,29,26,-1,27,32,28,-1,28,33,29,-1,29,34,30,-1,31,2,32,-1,32,5,33,-1,33,9,34,-1,34,14,35,-1,21,36,22,-1,36,37,38,-1,22,38,24,-1,37,39,40,-1,38,40,41,-1,24,41,27,-1,41,42,43,-1,27,43,31,-1,31,44,0,-1,36,38,22,-1,37,40,38,-1,38,41,24,-1,40,42,41,-1,41,43,27,-1,43,44,31,-1,15,45,16,-1,45,46,47,-1,16,47,17,-1,46,48,49,-1,47,49,50,-1,17,50,18,-1,48,51,52,-1,49,52,53,-1,50,53,54,-1,18,54,19,-1,51,55,56,-1,52,56,57,-1,53,57,58,-1,54,58,59,-1,19,59,20,-1,45,47,16,-1,46,49,47,-1,47,50,17,-1,48,52,49,-1,49,53,50,-1,50,54,18,-1,51,56,52,-1,52,57,53,-1,53,58,54,-1,54,59,19,-1,15,60,45,-1,45,61,46,-1,61,62,63,-1,46,63,48,-1,63,64,65,-1,48,65,51,-1,64,66,67,-1,65,67,68,-1,51,68,55,-1,60,61,45,-1,61,63,46,-1,62,64,63,-1,63,65,48,-1,64,67,65,-1,65,68,51,-1,55,69,56,-1,69,70,71,-1,56,71,57,-1,70,72,73,-1,71,73,74,-1,57,74,58,-1,72,75,76,-1,73,76,77,-1,74,77,78,-1,58,78,59,-1,75,79,80,-1,76,80,81,-1,77,81,82,-1,78,82,83,-1,59,83,20,-1,69,71,56,-1,70,73,71,-1,71,74,57,-1,72,76,73,-1,73,77,74,-1,74,78,58,-1,75,80,76,-1,76,81,77,-1,77,82,78,-1,78,83,59,-1,55,84,69,-1,84,85,86,-1,69,86,70,-1,85,87,88,-1,86,88,89,-1,70,89,72,-1,87,90,91,-1,88,91,92,-1,89,92,93,-1,72,93,75,-1,90,94,95,-1,91,95,96,-1,92,96,97,-1,93,97,98,-1,75,98,79,-1,84,86,69,-1,85,88,86,-1,86,89,70,-1,87,91,88,-1,88,92,89,-1,89,93,72,-1,90,95,91,-1,91,96,92,-1,92,97,93,-1,93,98,75,-1,79,99,80,-1,99,100,101,-1,80,101,81,-1,100,102,103,-1,101,103,104,-1,81,104,82,-1,102,105,106,-1,103,106,107,-1,104,107,108,-1,82,108,83,-1,105,21,23,-1,106,23,26,-1,107,26,30,-1,108,30,35,-1,83,35,20,-1,99,101,80,-1,100,103,101,-1,101,104,81,-1,102,106,103,-1,103,107,104,-1,104,108,82,-1,105,23,106,-1,106,26,107,-1,107,30,108,-1,108,35,83,-1,79,109,99,-1,109,110,111,-1,99,111,100,-1,110,112,113,-1,111,113,114,-1,100,114,102,-1,112,115,116,-1,113,116,117,-1,114,117,118,-1,102,118,105,-1,115,119,120,-1,116,120,121,-1,117,121,122,-1,118,122,123,-1,105,123,21,-1,109,111,99,-1,110,113,111,-1,111,114,100,-1,112,116,113,-1,113,117,114,-1,114,118,102,-1,115,120,116,-1,116,121,117,-1,117,122,118,-1,118,123,105,-1,119,115,124,-1,115,112,128,-1,124,128,125,-1,112,110,129,-1,128,129,130,-1,125,130,126,-1,110,109,131,-1,129,131,132,-1,130,132,133,-1,126,133,127,-1,109,79,98,-1,131,98,97,-1,132,97,96,-1,133,96,95,-1,127,95,94,-1,115,128,124,-1,112,129,128,-1,128,130,125,-1,110,131,129,-1,129,132,130,-1,130,133,126,-1,109,98,131,-1,131,97,132,-1,132,96,133,-1,133,95,127,-1,39,37,135,-1,37,36,137,-1,135,137,138,-1,136,138,139,-1,36,21,123,-1,137,123,122,-1,138,122,121,-1,139,121,120,-1,134,120,119,-1,37,137,135,-1,135,138,136,-1,36,123,137,-1,137,122,138,-1,138,121,139,-1,139,120,134,-1,94,90,140,-1,90,87,141,-1,87,85,142,-1,141,142,143,-1,85,84,144,-1,142,144,145,-1,84,55,68,-1,144,68,67,-1,145,67,66,-1,90,141,140,-1,87,142,141,-1,85,144,142,-1,142,145,143,-1,84,68,144,-1,144,67,145,-1]
IndexedFaceSet205.creaseAngle = 0.1
IndexedFaceSet205.solid = False
Coordinate206 = x3d.Coordinate()

IndexedFaceSet205.coord = Coordinate206

Shape201.geometry = IndexedFaceSet205

Transform200.children.append(Shape201)

Group199.children.append(Transform200)
Transform207 = x3d.Transform()
Transform207.DEF = "helmetBelt"
Transform207.scale = [3,3.5,3]
Transform207.translation = [0,1.61,0]
Shape208 = x3d.Shape()
Appearance209 = x3d.Appearance()
Appearance209.DEF = "BeltColor"
Material210 = x3d.Material()
Material210.USE = "JacketColor"

Appearance209.material = Material210

Shape208.appearance = Appearance209
Extrusion211 = x3d.Extrusion()
Extrusion211.creaseAngle = 1.57

Shape208.geometry = Extrusion211

Transform207.children.append(Shape208)

Group199.children.append(Transform207)
Shape212 = x3d.Shape()
Appearance213 = x3d.Appearance()
Material214 = x3d.Material()
Material214.USE = "Skin_Color"

Appearance213.material = Material214

Shape212.appearance = Appearance213
IndexedFaceSet215 = x3d.IndexedFaceSet()
IndexedFaceSet215.DEF = "headIFS"
IndexedFaceSet215.colorIndex = [1,1,1,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,1,1,1,-1,1,1,1,-1,0,0,0,-1,1,1,1,-1,1,1,1,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,2,2,2,-1,2,2,2,-1,2,2,2,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,2,2,2,-1,2,2,2,-1,2,2,2,-1,0,0,0,-1,0,0,0,-1,2,2,2,-1,2,2,2,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,1,1,1,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,2,2,2,-1,2,2,2,-1,2,2,2,-1,2,2,2,-1,2,2,2,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,2,2,2,-1,2,2,2,-1,2,2,2,-1,0,0,0,-1,0,0,0,-1,2,2,2,-1,2,2,2,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,3,3,3,-1,3,3,3,-1,0,0,0,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,3,3,3,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,3,3,3,-1,3,3,3,-1,0,0,0,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,3,3,3,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1]
IndexedFaceSet215.coordIndex = [48,87,58,-1,91,92,59,-1,59,92,88,-1,88,93,231,-1,232,86,233,-1,86,89,233,-1,89,57,56,-1,49,55,57,-1,102,86,96,-1,86,90,96,-1,97,95,96,-1,97,127,95,-1,41,96,154,-1,41,102,96,-1,99,102,41,-1,153,99,41,-1,102,40,86,-1,234,235,236,-1,87,237,58,-1,56,57,91,-1,87,234,237,-1,234,236,237,-1,89,49,57,-1,49,50,55,-1,40,89,86,-1,89,56,233,-1,232,90,86,-1,90,97,96,-1,92,93,88,-1,93,94,231,-1,232,231,94,-1,97,90,232,-1,96,42,154,-1,95,42,96,-1,53,46,45,-1,53,45,51,-1,53,51,92,-1,92,51,52,-1,92,52,93,-1,94,93,52,-1,94,52,4,-1,97,232,94,-1,54,47,46,-1,54,46,53,-1,55,47,54,-1,50,47,55,-1,34,33,50,-1,34,50,49,-1,35,34,49,-1,35,49,89,-1,35,89,40,-1,99,39,102,-1,39,35,40,-1,31,34,35,-1,31,35,32,-1,14,32,35,-1,14,35,39,-1,14,39,98,-1,137,38,153,-1,38,99,153,-1,38,98,99,-1,37,238,239,-1,11,238,37,-1,101,37,36,-1,241,141,242,-1,10,12,242,-1,12,13,14,-1,12,14,243,-1,13,15,32,-1,13,32,14,-1,15,16,31,-1,15,31,32,-1,2,70,10,-1,2,10,141,-1,70,69,12,-1,70,12,10,-1,69,68,13,-1,69,13,12,-1,68,67,15,-1,68,15,13,-1,67,66,16,-1,67,16,15,-1,98,39,99,-1,101,11,37,-1,100,101,36,-1,36,244,240,-1,141,10,242,-1,12,243,242,-1,36,37,239,-1,36,239,244,-1,57,55,91,-1,55,54,91,-1,39,40,102,-1,123,103,120,-1,114,122,104,-1,115,122,114,-1,208,105,115,-1,210,119,211,-1,210,106,119,-1,116,107,106,-1,107,108,117,-1,126,119,109,-1,126,110,119,-1,126,95,125,-1,95,127,125,-1,154,126,111,-1,126,109,111,-1,111,109,112,-1,111,112,153,-1,119,113,109,-1,207,213,214,-1,123,209,103,-1,213,212,214,-1,209,214,103,-1,209,207,214,-1,107,117,106,-1,108,118,117,-1,119,106,113,-1,210,116,106,-1,119,110,211,-1,126,125,110,-1,115,105,122,-1,208,124,105,-1,124,208,211,-1,211,110,125,-1,154,42,126,-1,126,42,95,-1,168,128,121,-1,170,168,121,-1,122,170,121,-1,172,170,122,-1,105,172,122,-1,172,105,124,-1,4,172,124,-1,124,211,125,-1,128,130,129,-1,121,128,129,-1,129,130,108,-1,108,130,118,-1,118,131,132,-1,117,118,132,-1,117,132,133,-1,106,117,133,-1,113,106,133,-1,109,152,112,-1,113,133,152,-1,133,132,134,-1,135,133,134,-1,133,135,136,-1,152,133,136,-1,148,152,136,-1,153,138,137,-1,153,112,138,-1,112,148,138,-1,219,217,139,-1,36,240,149,-1,139,217,140,-1,149,139,151,-1,36,149,100,-1,220,141,241,-1,220,150,142,-1,136,143,150,-1,221,136,150,-1,135,144,143,-1,136,135,143,-1,134,158,144,-1,135,134,144,-1,142,161,2,-1,141,142,2,-1,150,145,161,-1,142,150,161,-1,143,146,145,-1,150,143,145,-1,144,147,146,-1,143,144,146,-1,158,160,147,-1,144,158,147,-1,112,152,148,-1,139,140,151,-1,149,151,100,-1,240,218,149,-1,220,142,141,-1,220,221,150,-1,219,139,149,-1,218,219,149,-1,104,108,107,-1,104,129,108,-1,109,113,152,-1,153,41,111,-1,129,104,122,-1,129,122,121,-1,91,54,92,-1,54,53,92,-1,97,94,127,-1,127,94,4,-1,125,127,124,-1,127,4,124,-1,154,111,41,-1,31,30,33,-1,31,33,34,-1,16,17,30,-1,16,30,31,-1,66,65,17,-1,66,17,16,-1,2,73,156,-1,2,156,70,-1,156,72,66,-1,156,66,67,-1,156,67,68,-1,156,68,69,-1,156,69,70,-1,72,71,65,-1,72,65,66,-1,17,18,30,-1,45,44,51,-1,51,44,43,-1,51,43,52,-1,52,43,1,-1,52,1,4,-1,245,246,27,-1,245,27,3,-1,246,247,28,-1,246,28,27,-1,248,22,29,-1,248,29,28,-1,248,28,247,-1,27,26,0,-1,27,0,3,-1,27,28,25,-1,27,25,26,-1,29,24,25,-1,29,25,28,-1,22,23,24,-1,22,24,29,-1,249,250,22,-1,249,22,248,-1,250,60,23,-1,250,23,22,-1,17,254,18,-1,65,254,17,-1,71,64,65,-1,63,74,75,-1,63,75,61,-1,64,255,254,-1,75,62,61,-1,62,76,60,-1,76,77,23,-1,76,23,60,-1,77,24,23,-1,77,78,25,-1,77,25,24,-1,78,84,26,-1,78,26,25,-1,84,192,0,-1,84,0,26,-1,84,83,193,-1,84,193,192,-1,79,83,84,-1,79,84,78,-1,76,79,78,-1,76,78,77,-1,80,83,79,-1,80,204,83,-1,75,81,80,-1,81,85,204,-1,81,204,80,-1,74,81,75,-1,74,82,81,-1,82,5,85,-1,82,85,81,-1,155,8,71,-1,155,71,72,-1,8,6,64,-1,8,64,71,-1,6,7,255,-1,6,255,64,-1,7,9,256,-1,7,256,255,-1,9,257,256,-1,73,155,156,-1,155,72,156,-1,204,193,83,-1,64,254,65,-1,131,157,134,-1,132,131,134,-1,157,159,158,-1,134,157,158,-1,159,206,160,-1,158,159,160,-1,203,73,2,-1,161,203,2,-1,160,162,203,-1,147,160,203,-1,146,147,203,-1,145,146,203,-1,161,145,203,-1,206,163,162,-1,160,206,162,-1,157,164,159,-1,170,169,168,-1,171,169,170,-1,172,171,170,-1,1,171,172,-1,4,1,172,-1,173,227,245,-1,3,173,245,-1,174,226,227,-1,173,174,227,-1,176,175,215,-1,174,176,215,-1,226,174,215,-1,0,177,173,-1,3,0,173,-1,178,174,173,-1,177,178,173,-1,178,179,176,-1,174,178,176,-1,179,180,175,-1,176,179,175,-1,175,225,216,-1,215,175,216,-1,180,181,225,-1,175,180,225,-1,164,228,159,-1,159,228,206,-1,206,185,163,-1,187,186,184,-1,183,187,184,-1,228,229,185,-1,183,182,187,-1,181,188,182,-1,180,189,188,-1,181,180,188,-1,180,179,189,-1,178,190,189,-1,179,178,189,-1,177,191,190,-1,178,177,190,-1,0,192,191,-1,177,0,191,-1,193,205,191,-1,192,193,191,-1,191,205,194,-1,190,191,194,-1,190,194,188,-1,189,190,188,-1,194,205,195,-1,205,204,195,-1,195,196,187,-1,204,85,196,-1,195,204,196,-1,187,196,186,-1,196,197,186,-1,85,5,197,-1,196,85,197,-1,163,198,202,-1,162,163,202,-1,185,199,198,-1,163,185,198,-1,229,200,199,-1,185,229,199,-1,230,201,200,-1,229,230,200,-1,230,257,201,-1,203,202,73,-1,203,162,202,-1,205,193,204,-1,206,228,185,-1,198,8,155,-1,198,155,202,-1,155,73,202,-1,199,6,8,-1,199,8,198,-1,7,6,199,-1,7,199,200,-1,201,9,7,-1,201,7,200,-1,201,257,9,-1,188,194,195,-1,188,195,182,-1,195,187,182,-1,80,79,76,-1,80,62,75,-1,80,76,62,-1,47,50,33,-1,131,118,130,-1,20,21,47,-1,21,46,47,-1,20,33,19,-1,20,47,33,-1,33,30,19,-1,30,18,19,-1,62,60,251,-1,60,250,251,-1,252,61,251,-1,61,62,251,-1,252,63,61,-1,252,253,63,-1,166,130,167,-1,130,128,167,-1,166,131,130,-1,166,165,131,-1,165,157,131,-1,165,164,157,-1,224,181,182,-1,224,225,181,-1,224,183,223,-1,224,182,183,-1,183,184,223,-1,184,222,223,-1]
IndexedFaceSet215.creaseAngle = 0.7854
Coordinate216 = x3d.Coordinate()
Coordinate216.DEF = "Face"

IndexedFaceSet215.coord = Coordinate216
Color217 = x3d.Color()

IndexedFaceSet215.color = Color217

Shape212.geometry = IndexedFaceSet215

Group199.children.append(Shape212)

HAnimSegment198.children.append(Group199)

HAnimJoint197.children.append(HAnimSegment198)

HAnimJoint190.children.append(HAnimJoint197)

HAnimJoint113.children.append(HAnimJoint190)

HAnimJoint58.children.append(HAnimJoint113)

HAnimHumanoid57.skeleton.append(HAnimJoint58)
HAnimJoint218 = x3d.HAnimJoint()
HAnimJoint218.USE = "hanim_humanoid_root"

HAnimHumanoid57.joints.append(HAnimJoint218)
HAnimJoint219 = x3d.HAnimJoint()
HAnimJoint219.USE = "hanim_sacroiliac"

HAnimHumanoid57.joints.append(HAnimJoint219)
HAnimJoint220 = x3d.HAnimJoint()
HAnimJoint220.USE = "hanim_vl1"

HAnimHumanoid57.joints.append(HAnimJoint220)
HAnimJoint221 = x3d.HAnimJoint()
HAnimJoint221.USE = "hanim_vc4"

HAnimHumanoid57.joints.append(HAnimJoint221)
HAnimJoint222 = x3d.HAnimJoint()
HAnimJoint222.USE = "hanim_skullbase"

HAnimHumanoid57.joints.append(HAnimJoint222)
HAnimJoint223 = x3d.HAnimJoint()
HAnimJoint223.USE = "hanim_l_ankle"

HAnimHumanoid57.joints.append(HAnimJoint223)
HAnimJoint224 = x3d.HAnimJoint()
HAnimJoint224.USE = "hanim_r_ankle"

HAnimHumanoid57.joints.append(HAnimJoint224)
HAnimJoint225 = x3d.HAnimJoint()
HAnimJoint225.USE = "hanim_l_elbow"

HAnimHumanoid57.joints.append(HAnimJoint225)
HAnimJoint226 = x3d.HAnimJoint()
HAnimJoint226.USE = "hanim_r_elbow"

HAnimHumanoid57.joints.append(HAnimJoint226)
HAnimJoint227 = x3d.HAnimJoint()
HAnimJoint227.USE = "hanim_l_hip"

HAnimHumanoid57.joints.append(HAnimJoint227)
HAnimJoint228 = x3d.HAnimJoint()
HAnimJoint228.USE = "hanim_r_hip"

HAnimHumanoid57.joints.append(HAnimJoint228)
HAnimJoint229 = x3d.HAnimJoint()
HAnimJoint229.USE = "hanim_l_knee"

HAnimHumanoid57.joints.append(HAnimJoint229)
HAnimJoint230 = x3d.HAnimJoint()
HAnimJoint230.USE = "hanim_r_knee"

HAnimHumanoid57.joints.append(HAnimJoint230)
HAnimJoint231 = x3d.HAnimJoint()
HAnimJoint231.USE = "hanim_l_shoulder"

HAnimHumanoid57.joints.append(HAnimJoint231)
HAnimJoint232 = x3d.HAnimJoint()
HAnimJoint232.USE = "hanim_r_shoulder"

HAnimHumanoid57.joints.append(HAnimJoint232)
HAnimJoint233 = x3d.HAnimJoint()
HAnimJoint233.USE = "hanim_l_wrist"

HAnimHumanoid57.joints.append(HAnimJoint233)
HAnimJoint234 = x3d.HAnimJoint()
HAnimJoint234.USE = "hanim_r_wrist"

HAnimHumanoid57.joints.append(HAnimJoint234)
HAnimSegment235 = x3d.HAnimSegment()
HAnimSegment235.USE = "hanim_pelvis"

HAnimHumanoid57.segments.append(HAnimSegment235)
HAnimSegment236 = x3d.HAnimSegment()
HAnimSegment236.USE = "hanim_l1"

HAnimHumanoid57.segments.append(HAnimSegment236)
HAnimSegment237 = x3d.HAnimSegment()
HAnimSegment237.USE = "hanim_c4"

HAnimHumanoid57.segments.append(HAnimSegment237)
HAnimSegment238 = x3d.HAnimSegment()
HAnimSegment238.USE = "hanim_skull"

HAnimHumanoid57.segments.append(HAnimSegment238)
HAnimSegment239 = x3d.HAnimSegment()
HAnimSegment239.USE = "hanim_l_calf"

HAnimHumanoid57.segments.append(HAnimSegment239)
HAnimSegment240 = x3d.HAnimSegment()
HAnimSegment240.USE = "hanim_r_calf"

HAnimHumanoid57.segments.append(HAnimSegment240)
HAnimSegment241 = x3d.HAnimSegment()
HAnimSegment241.USE = "hanim_l_forearm"

HAnimHumanoid57.segments.append(HAnimSegment241)
HAnimSegment242 = x3d.HAnimSegment()
HAnimSegment242.USE = "hanim_r_forearm"

HAnimHumanoid57.segments.append(HAnimSegment242)
HAnimSegment243 = x3d.HAnimSegment()
HAnimSegment243.USE = "hanim_l_hand"

HAnimHumanoid57.segments.append(HAnimSegment243)
HAnimSegment244 = x3d.HAnimSegment()
HAnimSegment244.USE = "hanim_r_hand"

HAnimHumanoid57.segments.append(HAnimSegment244)
HAnimSegment245 = x3d.HAnimSegment()
HAnimSegment245.USE = "hanim_l_hindfoot"

HAnimHumanoid57.segments.append(HAnimSegment245)
HAnimSegment246 = x3d.HAnimSegment()
HAnimSegment246.USE = "hanim_r_hindfoot"

HAnimHumanoid57.segments.append(HAnimSegment246)
HAnimSegment247 = x3d.HAnimSegment()
HAnimSegment247.USE = "hanim_l_thigh"

HAnimHumanoid57.segments.append(HAnimSegment247)
HAnimSegment248 = x3d.HAnimSegment()
HAnimSegment248.USE = "hanim_r_thigh"

HAnimHumanoid57.segments.append(HAnimSegment248)
HAnimSegment249 = x3d.HAnimSegment()
HAnimSegment249.USE = "hanim_l_upperarm"

HAnimHumanoid57.segments.append(HAnimSegment249)
HAnimSegment250 = x3d.HAnimSegment()
HAnimSegment250.USE = "hanim_r_upperarm"

HAnimHumanoid57.segments.append(HAnimSegment250)

Transform56.children.append(HAnimHumanoid57)

Group55.children.append(Transform56)
ProtoInstance251 = x3d.ProtoInstance()
ProtoInstance251.name = "LOA1_ShootAnimation"
fieldValue252 = x3d.fieldValue()
fieldValue252.name = "cycleInterval"
fieldValue252.value = "0.009999999776482582"

ProtoInstance251.fieldValue.append(fieldValue252)

Group55.children.append(ProtoInstance251)
TimeSensor253 = x3d.TimeSensor()
TimeSensor253.DEF = "TIMER"
TimeSensor253.cycleInterval = 4

Group55.children.append(TimeSensor253)

Group54.children.append(Group55)

LOD53.children.append(Group54)
Transform254 = x3d.Transform()

LOD53.children.append(Transform254)
Transform255 = x3d.Transform()
Transform255.translation = [0,1,0]
Shape256 = x3d.Shape()
Box257 = x3d.Box()
Box257.size = [0.5,2,0.3]

Shape256.geometry = Box257
Appearance258 = x3d.Appearance()
Material259 = x3d.Material()
Material259.diffuseColor = [0.1,0.4,0.1]

Appearance258.material = Material259

Shape256.appearance = Appearance258

Transform255.children.append(Shape256)

LOD53.children.append(Transform255)

Scene14.children.append(LOD53)
NavigationInfo260 = x3d.NavigationInfo()
NavigationInfo260.avatarSize = [0.15,1.53,0.75]
NavigationInfo260.speed = 0.5
NavigationInfo260.type = ["EXAMINE"]

Scene14.children.append(NavigationInfo260)
WorldInfo261 = x3d.WorldInfo()
WorldInfo261.info = ["Copyright (c) 1997. 3Name3D / Yglesias Wallock Divekar, Inc."]
WorldInfo261.title = "Nancy - an HAnim compliant avatar by 3Name3D"

Scene14.children.append(WorldInfo261)
Group262 = x3d.Group()
ProximitySensor263 = x3d.ProximitySensor()
ProximitySensor263.DEF = "TriggerProximitySensor"
ProximitySensor263.size = [50,50,50]

Group262.children.append(ProximitySensor263)
PositionInterpolator264 = x3d.PositionInterpolator()
PositionInterpolator264.DEF = "HUMANOIDROOT_POSITION_ANIMATOR"
PositionInterpolator264.key = [0,1]

Group262.children.append(PositionInterpolator264)
OrientationInterpolator265 = x3d.OrientationInterpolator()
OrientationInterpolator265.DEF = "HUMANOIDROOT_ANIMATOR"
OrientationInterpolator265.key = [0,1]

Group262.children.append(OrientationInterpolator265)
OrientationInterpolator266 = x3d.OrientationInterpolator()
OrientationInterpolator266.DEF = "SACROILIAC_ANIMATOR"
OrientationInterpolator266.key = [0,1]

Group262.children.append(OrientationInterpolator266)
OrientationInterpolator267 = x3d.OrientationInterpolator()
OrientationInterpolator267.DEF = "L_HIP_ANIMATOR"
OrientationInterpolator267.key = [0,1]

Group262.children.append(OrientationInterpolator267)
OrientationInterpolator268 = x3d.OrientationInterpolator()
OrientationInterpolator268.DEF = "L_KNEE_ANIMATOR"
OrientationInterpolator268.key = [0,1]

Group262.children.append(OrientationInterpolator268)
OrientationInterpolator269 = x3d.OrientationInterpolator()
OrientationInterpolator269.DEF = "L_ANKLE_ANIMATOR"
OrientationInterpolator269.key = [0,1]

Group262.children.append(OrientationInterpolator269)
OrientationInterpolator270 = x3d.OrientationInterpolator()
OrientationInterpolator270.DEF = "L_MIDTARSAL_ANIMATOR"
OrientationInterpolator270.key = [0,1]

Group262.children.append(OrientationInterpolator270)
OrientationInterpolator271 = x3d.OrientationInterpolator()
OrientationInterpolator271.DEF = "R_HIP_ANIMATOR"
OrientationInterpolator271.key = [0,1]

Group262.children.append(OrientationInterpolator271)
OrientationInterpolator272 = x3d.OrientationInterpolator()
OrientationInterpolator272.DEF = "R_KNEE_ANIMATOR"
OrientationInterpolator272.key = [0,1]

Group262.children.append(OrientationInterpolator272)
OrientationInterpolator273 = x3d.OrientationInterpolator()
OrientationInterpolator273.DEF = "R_ANKLE_ANIMATOR"
OrientationInterpolator273.key = [0,1]

Group262.children.append(OrientationInterpolator273)
OrientationInterpolator274 = x3d.OrientationInterpolator()
OrientationInterpolator274.DEF = "R_MIDTARSAL_ANIMATOR"
OrientationInterpolator274.key = [0,1]

Group262.children.append(OrientationInterpolator274)
OrientationInterpolator275 = x3d.OrientationInterpolator()
OrientationInterpolator275.DEF = "VL5_ANIMATOR"
OrientationInterpolator275.key = [0,1]

Group262.children.append(OrientationInterpolator275)
OrientationInterpolator276 = x3d.OrientationInterpolator()
OrientationInterpolator276.DEF = "SKULLBASE_ANIMATOR"
OrientationInterpolator276.key = [0,0.1,0.5,0.7,1]

Group262.children.append(OrientationInterpolator276)
OrientationInterpolator277 = x3d.OrientationInterpolator()
OrientationInterpolator277.DEF = "L_SHOULDER_ANIMATOR"
OrientationInterpolator277.key = [0,0.08,0.8,1]

Group262.children.append(OrientationInterpolator277)
OrientationInterpolator278 = x3d.OrientationInterpolator()
OrientationInterpolator278.DEF = "L_ELBOW_ANIMATOR"
OrientationInterpolator278.key = [0,0.3,0.4,0.45,1]

Group262.children.append(OrientationInterpolator278)
OrientationInterpolator279 = x3d.OrientationInterpolator()
OrientationInterpolator279.DEF = "L_WRIST_ANIMATOR"
OrientationInterpolator279.key = [0,0.3,1]

Group262.children.append(OrientationInterpolator279)
OrientationInterpolator280 = x3d.OrientationInterpolator()
OrientationInterpolator280.DEF = "R_SHOULDER_ANIMATOR"
OrientationInterpolator280.key = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]

Group262.children.append(OrientationInterpolator280)
OrientationInterpolator281 = x3d.OrientationInterpolator()
OrientationInterpolator281.DEF = "R_ELBOW_ANIMATOR"
OrientationInterpolator281.key = [0,0.1,0.2,0.5,0.6,0.7,0.8,1]

Group262.children.append(OrientationInterpolator281)
OrientationInterpolator282 = x3d.OrientationInterpolator()
OrientationInterpolator282.DEF = "R_WRIST_ANIMATOR"
OrientationInterpolator282.key = [0,1]

Group262.children.append(OrientationInterpolator282)

Scene14.children.append(Group262)
ROUTE283 = x3d.ROUTE()
ROUTE283.fromField = "enterTime"
ROUTE283.fromNode = "TriggerProximitySensor"
ROUTE283.toField = "startTime"
ROUTE283.toNode = "TIMER"

Scene14.children.append(ROUTE283)
ROUTE284 = x3d.ROUTE()
ROUTE284.fromField = "fraction_changed"
ROUTE284.fromNode = "TIMER"
ROUTE284.toField = "set_fraction"
ROUTE284.toNode = "HUMANOIDROOT_POSITION_ANIMATOR"

Scene14.children.append(ROUTE284)
ROUTE285 = x3d.ROUTE()
ROUTE285.fromField = "fraction_changed"
ROUTE285.fromNode = "TIMER"
ROUTE285.toField = "set_fraction"
ROUTE285.toNode = "HUMANOIDROOT_ANIMATOR"

Scene14.children.append(ROUTE285)
ROUTE286 = x3d.ROUTE()
ROUTE286.fromField = "fraction_changed"
ROUTE286.fromNode = "TIMER"
ROUTE286.toField = "set_fraction"
ROUTE286.toNode = "SACROILIAC_ANIMATOR"

Scene14.children.append(ROUTE286)
ROUTE287 = x3d.ROUTE()
ROUTE287.fromField = "fraction_changed"
ROUTE287.fromNode = "TIMER"
ROUTE287.toField = "set_fraction"
ROUTE287.toNode = "L_HIP_ANIMATOR"

Scene14.children.append(ROUTE287)
ROUTE288 = x3d.ROUTE()
ROUTE288.fromField = "fraction_changed"
ROUTE288.fromNode = "TIMER"
ROUTE288.toField = "set_fraction"
ROUTE288.toNode = "L_KNEE_ANIMATOR"

Scene14.children.append(ROUTE288)
ROUTE289 = x3d.ROUTE()
ROUTE289.fromField = "fraction_changed"
ROUTE289.fromNode = "TIMER"
ROUTE289.toField = "set_fraction"
ROUTE289.toNode = "L_ANKLE_ANIMATOR"

Scene14.children.append(ROUTE289)
ROUTE290 = x3d.ROUTE()
ROUTE290.fromField = "fraction_changed"
ROUTE290.fromNode = "TIMER"
ROUTE290.toField = "set_fraction"
ROUTE290.toNode = "L_MIDTARSAL_ANIMATOR"

Scene14.children.append(ROUTE290)
ROUTE291 = x3d.ROUTE()
ROUTE291.fromField = "fraction_changed"
ROUTE291.fromNode = "TIMER"
ROUTE291.toField = "set_fraction"
ROUTE291.toNode = "R_HIP_ANIMATOR"

Scene14.children.append(ROUTE291)
ROUTE292 = x3d.ROUTE()
ROUTE292.fromField = "fraction_changed"
ROUTE292.fromNode = "TIMER"
ROUTE292.toField = "set_fraction"
ROUTE292.toNode = "R_KNEE_ANIMATOR"

Scene14.children.append(ROUTE292)
ROUTE293 = x3d.ROUTE()
ROUTE293.fromField = "fraction_changed"
ROUTE293.fromNode = "TIMER"
ROUTE293.toField = "set_fraction"
ROUTE293.toNode = "R_ANKLE_ANIMATOR"

Scene14.children.append(ROUTE293)
ROUTE294 = x3d.ROUTE()
ROUTE294.fromField = "fraction_changed"
ROUTE294.fromNode = "TIMER"
ROUTE294.toField = "set_fraction"
ROUTE294.toNode = "R_MIDTARSAL_ANIMATOR"

Scene14.children.append(ROUTE294)
ROUTE295 = x3d.ROUTE()
ROUTE295.fromField = "fraction_changed"
ROUTE295.fromNode = "TIMER"
ROUTE295.toField = "set_fraction"
ROUTE295.toNode = "VL5_ANIMATOR"

Scene14.children.append(ROUTE295)
ROUTE296 = x3d.ROUTE()
ROUTE296.fromField = "fraction_changed"
ROUTE296.fromNode = "TIMER"
ROUTE296.toField = "set_fraction"
ROUTE296.toNode = "SKULLBASE_ANIMATOR"

Scene14.children.append(ROUTE296)
ROUTE297 = x3d.ROUTE()
ROUTE297.fromField = "fraction_changed"
ROUTE297.fromNode = "TIMER"
ROUTE297.toField = "set_fraction"
ROUTE297.toNode = "L_SHOULDER_ANIMATOR"

Scene14.children.append(ROUTE297)
ROUTE298 = x3d.ROUTE()
ROUTE298.fromField = "fraction_changed"
ROUTE298.fromNode = "TIMER"
ROUTE298.toField = "set_fraction"
ROUTE298.toNode = "L_ELBOW_ANIMATOR"

Scene14.children.append(ROUTE298)
ROUTE299 = x3d.ROUTE()
ROUTE299.fromField = "fraction_changed"
ROUTE299.fromNode = "TIMER"
ROUTE299.toField = "set_fraction"
ROUTE299.toNode = "L_WRIST_ANIMATOR"

Scene14.children.append(ROUTE299)
ROUTE300 = x3d.ROUTE()
ROUTE300.fromField = "fraction_changed"
ROUTE300.fromNode = "TIMER"
ROUTE300.toField = "set_fraction"
ROUTE300.toNode = "R_SHOULDER_ANIMATOR"

Scene14.children.append(ROUTE300)
ROUTE301 = x3d.ROUTE()
ROUTE301.fromField = "fraction_changed"
ROUTE301.fromNode = "TIMER"
ROUTE301.toField = "set_fraction"
ROUTE301.toNode = "R_ELBOW_ANIMATOR"

Scene14.children.append(ROUTE301)
ROUTE302 = x3d.ROUTE()
ROUTE302.fromField = "fraction_changed"
ROUTE302.fromNode = "TIMER"
ROUTE302.toField = "set_fraction"
ROUTE302.toNode = "R_WRIST_ANIMATOR"

Scene14.children.append(ROUTE302)
#Animation
ROUTE303 = x3d.ROUTE()
ROUTE303.fromField = "value_changed"
ROUTE303.fromNode = "R_ANKLE_ANIMATOR"
ROUTE303.toField = "set_rotation"
ROUTE303.toNode = "hanim_r_ankle"

Scene14.children.append(ROUTE303)
ROUTE304 = x3d.ROUTE()
ROUTE304.fromField = "value_changed"
ROUTE304.fromNode = "R_KNEE_ANIMATOR"
ROUTE304.toField = "set_rotation"
ROUTE304.toNode = "hanim_r_knee"

Scene14.children.append(ROUTE304)
ROUTE305 = x3d.ROUTE()
ROUTE305.fromField = "value_changed"
ROUTE305.fromNode = "R_HIP_ANIMATOR"
ROUTE305.toField = "set_rotation"
ROUTE305.toNode = "hanim_r_hip"

Scene14.children.append(ROUTE305)
ROUTE306 = x3d.ROUTE()
ROUTE306.fromField = "value_changed"
ROUTE306.fromNode = "L_ANKLE_ANIMATOR"
ROUTE306.toField = "set_rotation"
ROUTE306.toNode = "hanim_l_ankle"

Scene14.children.append(ROUTE306)
ROUTE307 = x3d.ROUTE()
ROUTE307.fromField = "value_changed"
ROUTE307.fromNode = "L_KNEE_ANIMATOR"
ROUTE307.toField = "set_rotation"
ROUTE307.toNode = "hanim_l_knee"

Scene14.children.append(ROUTE307)
ROUTE308 = x3d.ROUTE()
ROUTE308.fromField = "value_changed"
ROUTE308.fromNode = "L_HIP_ANIMATOR"
ROUTE308.toField = "set_rotation"
ROUTE308.toNode = "hanim_l_hip"

Scene14.children.append(ROUTE308)
ROUTE309 = x3d.ROUTE()
ROUTE309.fromField = "value_changed"
ROUTE309.fromNode = "VL5_ANIMATOR"
ROUTE309.toField = "set_rotation"
ROUTE309.toNode = "hanim_sacroiliac"

Scene14.children.append(ROUTE309)
ROUTE310 = x3d.ROUTE()
ROUTE310.fromField = "value_changed"
ROUTE310.fromNode = "R_WRIST_ANIMATOR"
ROUTE310.toField = "set_rotation"
ROUTE310.toNode = "r_hand_adjust"

Scene14.children.append(ROUTE310)
ROUTE311 = x3d.ROUTE()
ROUTE311.fromField = "value_changed"
ROUTE311.fromNode = "R_ELBOW_ANIMATOR"
ROUTE311.toField = "set_rotation"
ROUTE311.toNode = "hanim_r_elbow"

Scene14.children.append(ROUTE311)
ROUTE312 = x3d.ROUTE()
ROUTE312.fromField = "value_changed"
ROUTE312.fromNode = "R_SHOULDER_ANIMATOR"
ROUTE312.toField = "set_rotation"
ROUTE312.toNode = "hanim_r_shoulder"

Scene14.children.append(ROUTE312)
ROUTE313 = x3d.ROUTE()
ROUTE313.fromField = "value_changed"
ROUTE313.fromNode = "L_WRIST_ANIMATOR"
ROUTE313.toField = "set_rotation"
ROUTE313.toNode = "hanim_l_wrist"

Scene14.children.append(ROUTE313)
ROUTE314 = x3d.ROUTE()
ROUTE314.fromField = "value_changed"
ROUTE314.fromNode = "L_ELBOW_ANIMATOR"
ROUTE314.toField = "set_rotation"
ROUTE314.toNode = "hanim_l_elbow"

Scene14.children.append(ROUTE314)
ROUTE315 = x3d.ROUTE()
ROUTE315.fromField = "value_changed"
ROUTE315.fromNode = "L_SHOULDER_ANIMATOR"
ROUTE315.toField = "set_rotation"
ROUTE315.toNode = "hanim_l_shoulder"

Scene14.children.append(ROUTE315)
ROUTE316 = x3d.ROUTE()
ROUTE316.fromField = "value_changed"
ROUTE316.fromNode = "SKULLBASE_ANIMATOR"
ROUTE316.toField = "set_rotation"
ROUTE316.toNode = "hanim_skullbase"

Scene14.children.append(ROUTE316)

X3D0.Scene = Scene14
f = open("././NancyStandShootRifleM24_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
