print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"
head1 = x3d.head()
meta2 = x3d.meta()
meta2.name = "title"
meta2.content = "AllenDuttonProtoInstances.x3d"

head1.children.append(meta2)
meta3 = x3d.meta()
meta3.name = "description"
meta3.content = "Articulated human model developed from laser-scan data."

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.name = "creator"
meta4.content = "Allen Dutton"

head1.children.append(meta4)
meta5 = x3d.meta()
meta5.name = "translator"
meta5.content = "Ozan APAYDIN"

head1.children.append(meta5)
meta6 = x3d.meta()
meta6.name = "created"
meta6.content = "8 June 2001"

head1.children.append(meta6)
meta7 = x3d.meta()
meta7.name = "translated"
meta7.content = "20 November 2001"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.name = "modified"
meta8.content = "4 July 2020"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "warning"
meta9.content = "using ProtoDeclare is only for developmental experimentation, use X3D native tags for Humanoids instead"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "reference"
meta10.content = "AllenDutton.x3d"

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.name = "reference"
meta11.content = "http://theses.nps.navy.mil/Thesis_01sep_Dutton.pdf"

head1.children.append(meta11)
meta12 = x3d.meta()
meta12.name = "reference"
meta12.content = "http://www.MovesInstitute.org/Theses/AllenDutton.pdf"

head1.children.append(meta12)
meta13 = x3d.meta()
meta13.name = "reference"
meta13.content = "http://www.HAnim.org"

head1.children.append(meta13)
meta14 = x3d.meta()
meta14.name = "identifier"
meta14.content = "https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Prototypes/AllenDuttonProtoInstances.x3d"

head1.children.append(meta14)
meta15 = x3d.meta()
meta15.name = "generator"
meta15.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"

head1.children.append(meta15)
meta16 = x3d.meta()
meta16.name = "license"
meta16.content = "../license.html"

head1.children.append(meta16)

X3D0.head = head1
Scene17 = x3d.Scene()
WorldInfo18 = x3d.WorldInfo()
WorldInfo18.title = "AllenDuttonProtoInstances.x3d"

Scene17.children.append(WorldInfo18)
ProtoDeclare19 = x3d.ProtoDeclare()
ProtoDeclare19.name = "Joint"
ProtoDeclare19.appinfo = "The Joint node is used as a building block to describe the articulations of the humanoid figure. Each articulation of the humanoid figure is represented by a Joint node each of which is organized into a hierarchy that describes the overall skeleton of the humanoid."
ProtoDeclare19.documentation = "http://HAnim.org/Specifications/HAnim2001/part1/Joint.html"
ProtoInterface20 = x3d.ProtoInterface()
field21 = x3d.field()
field21.name = "center"
field21.accessType = "inputOutput"
field21.type = "SFVec3f"
field21.value = [0,0,0]

ProtoInterface20.field.append(field21)
field22 = x3d.field()
field22.name = "children"
field22.accessType = "inputOutput"
field22.type = "MFNode"

ProtoInterface20.field.append(field22)
field23 = x3d.field()
field23.name = "llimit"
field23.accessType = "inputOutput"
field23.type = "MFFloat"

ProtoInterface20.field.append(field23)
field24 = x3d.field()
field24.name = "limitOrientation"
field24.accessType = "inputOutput"
field24.type = "SFRotation"
field24.value = [0,0,1,0]

ProtoInterface20.field.append(field24)
field25 = x3d.field()
field25.name = "name"
field25.accessType = "inputOutput"
field25.type = "SFString"

ProtoInterface20.field.append(field25)
field26 = x3d.field()
field26.name = "rotation"
field26.accessType = "inputOutput"
field26.type = "SFRotation"
field26.value = [0,0,1,0]

ProtoInterface20.field.append(field26)
field27 = x3d.field()
field27.name = "scale"
field27.accessType = "inputOutput"
field27.type = "SFVec3f"
field27.value = [1,1,1]

ProtoInterface20.field.append(field27)
field28 = x3d.field()
field28.name = "scaleOrientation"
field28.accessType = "inputOutput"
field28.type = "SFRotation"
field28.value = [0,0,1,0]

ProtoInterface20.field.append(field28)
field29 = x3d.field()
field29.name = "stiffness"
field29.accessType = "inputOutput"
field29.type = "MFFloat"
field29.value = [0,0,0]

ProtoInterface20.field.append(field29)
field30 = x3d.field()
field30.name = "translation"
field30.accessType = "inputOutput"
field30.type = "SFVec3f"
field30.value = [0,0,0]

ProtoInterface20.field.append(field30)
field31 = x3d.field()
field31.name = "ulimit"
field31.accessType = "inputOutput"
field31.type = "MFFloat"

ProtoInterface20.field.append(field31)

ProtoDeclare19.ProtoInterface = ProtoInterface20
ProtoBody32 = x3d.ProtoBody()
Transform33 = x3d.Transform()
Transform33.DEF = "JointTransform"
IS34 = x3d.IS()
connect35 = x3d.connect()
connect35.nodeField = "center"
connect35.protoField = "center"

IS34.connect.append(connect35)
connect36 = x3d.connect()
connect36.nodeField = "children"
connect36.protoField = "children"

IS34.connect.append(connect36)
connect37 = x3d.connect()
connect37.nodeField = "rotation"
connect37.protoField = "rotation"

IS34.connect.append(connect37)
connect38 = x3d.connect()
connect38.nodeField = "scale"
connect38.protoField = "scale"

IS34.connect.append(connect38)
connect39 = x3d.connect()
connect39.nodeField = "scaleOrientation"
connect39.protoField = "scaleOrientation"

IS34.connect.append(connect39)
connect40 = x3d.connect()
connect40.nodeField = "translation"
connect40.protoField = "translation"

IS34.connect.append(connect40)

Transform33.IS = IS34

ProtoBody32.children.append(Transform33)

ProtoDeclare19.ProtoBody = ProtoBody32

Scene17.children.append(ProtoDeclare19)
ProtoDeclare41 = x3d.ProtoDeclare()
ProtoDeclare41.name = "Segment"
ProtoDeclare41.appinfo = "The Segment node is used describe the attributes of the physical links between the joints of the humanoid figure. Each body part (pelvis thigh calf etc) of the humanoid figure is represented by a Segment node."
ProtoDeclare41.documentation = "http://HAnim.org/Specifications/HAnim2001/part1/Segment.html"
ProtoInterface42 = x3d.ProtoInterface()
field43 = x3d.field()
field43.name = "bboxCenter"
field43.accessType = "initializeOnly"
field43.type = "SFVec3f"
field43.value = [0,0,0]

ProtoInterface42.field.append(field43)
field44 = x3d.field()
field44.name = "bboxSize"
field44.accessType = "initializeOnly"
field44.type = "SFVec3f"
field44.value = [-1,-1,-1]

ProtoInterface42.field.append(field44)
field45 = x3d.field()
field45.name = "centerOfMass"
field45.accessType = "inputOutput"
field45.type = "SFVec3f"
field45.value = [0,0,0]

ProtoInterface42.field.append(field45)
field46 = x3d.field()
field46.name = "children"
field46.accessType = "inputOutput"
field46.type = "MFNode"

ProtoInterface42.field.append(field46)
field47 = x3d.field()
field47.name = "coord"
field47.accessType = "inputOutput"
field47.appinfo = "contains Coordinate nodes"
field47.type = "SFNode"
#NULL node

ProtoInterface42.field.append(field47)
field48 = x3d.field()
field48.name = "displacers"
field48.accessType = "inputOutput"
field48.appinfo = "contains Displacer nodes"
field48.type = "MFNode"

ProtoInterface42.field.append(field48)
field49 = x3d.field()
field49.name = "mass"
field49.accessType = "inputOutput"
field49.type = "SFFloat"
field49.value = 0

ProtoInterface42.field.append(field49)
field50 = x3d.field()
field50.name = "momentsOfInertia"
field50.accessType = "inputOutput"
field50.type = "MFFloat"
field50.value = [0,0,0,0,0,0,0,0,0]

ProtoInterface42.field.append(field50)
field51 = x3d.field()
field51.name = "name"
field51.accessType = "inputOutput"
field51.type = "SFString"

ProtoInterface42.field.append(field51)
field52 = x3d.field()
field52.name = "addChildren"
field52.accessType = "inputOnly"
field52.type = "MFNode"

ProtoInterface42.field.append(field52)
field53 = x3d.field()
field53.name = "removeChildren"
field53.accessType = "inputOnly"
field53.type = "MFNode"

ProtoInterface42.field.append(field53)

ProtoDeclare41.ProtoInterface = ProtoInterface42
ProtoBody54 = x3d.ProtoBody()
Group55 = x3d.Group()
Group55.DEF = "SegmentGroup"
IS56 = x3d.IS()
connect57 = x3d.connect()
connect57.nodeField = "bboxCenter"
connect57.protoField = "bboxCenter"

IS56.connect.append(connect57)
connect58 = x3d.connect()
connect58.nodeField = "bboxSize"
connect58.protoField = "bboxSize"

IS56.connect.append(connect58)
connect59 = x3d.connect()
connect59.nodeField = "children"
connect59.protoField = "children"

IS56.connect.append(connect59)
connect60 = x3d.connect()
connect60.nodeField = "addChildren"
connect60.protoField = "addChildren"

IS56.connect.append(connect60)
connect61 = x3d.connect()
connect61.nodeField = "removeChildren"
connect61.protoField = "removeChildren"

IS56.connect.append(connect61)

Group55.IS = IS56

ProtoBody54.children.append(Group55)

ProtoDeclare41.ProtoBody = ProtoBody54

Scene17.children.append(ProtoDeclare41)
ProtoDeclare62 = x3d.ProtoDeclare()
ProtoDeclare62.name = "Humanoid"
ProtoDeclare62.appinfo = "The Humanoid node serves as overall container for the Joint Segment Site and Viewpoint nodes which define the skeleton geometry and landmarks of the humanoid figure. Additionally the node provides a means for defining information about the author copyright and usage restrictions of the model."
ProtoDeclare62.documentation = "http://HAnim.org/Specifications/HAnim2001/part1/Humanoid.html"
ProtoInterface63 = x3d.ProtoInterface()
#HAnim v1.1 field definitions
field64 = x3d.field()
field64.name = "bboxCenter"
field64.accessType = "initializeOnly"
field64.type = "SFVec3f"
field64.value = [0,0,0]

ProtoInterface63.field.append(field64)
field65 = x3d.field()
field65.name = "bboxSize"
field65.accessType = "initializeOnly"
field65.type = "SFVec3f"
field65.value = [-1,-1,-1]

ProtoInterface63.field.append(field65)
field66 = x3d.field()
field66.name = "center"
field66.accessType = "inputOutput"
field66.type = "SFVec3f"
field66.value = [0,0,0]

ProtoInterface63.field.append(field66)
field67 = x3d.field()
field67.name = "humanoidBody"
field67.accessType = "inputOutput"
field67.appinfo = "HAnim 1.1 field container for body head. Hint: replaced by 2.0 skeleton."
field67.documentation = "http://HAnim.org/Specifications/HAnim1.1/#humanoid"
field67.type = "MFNode"

ProtoInterface63.field.append(field67)
field68 = x3d.field()
field68.name = "info"
field68.accessType = "inputOutput"
field68.type = "MFString"

ProtoInterface63.field.append(field68)
field69 = x3d.field()
field69.name = "joints"
field69.accessType = "inputOutput"
field69.appinfo = "Container field for Joint nodes"
field69.type = "MFNode"

ProtoInterface63.field.append(field69)
field70 = x3d.field()
field70.name = "name"
field70.accessType = "inputOutput"
field70.type = "SFString"

ProtoInterface63.field.append(field70)
field71 = x3d.field()
field71.name = "rotation"
field71.accessType = "inputOutput"
field71.type = "SFRotation"
field71.value = [0,0,1,0]

ProtoInterface63.field.append(field71)
field72 = x3d.field()
field72.name = "scale"
field72.accessType = "inputOutput"
field72.type = "SFVec3f"
field72.value = [1,1,1]

ProtoInterface63.field.append(field72)
field73 = x3d.field()
field73.name = "scaleOrientation"
field73.accessType = "inputOutput"
field73.type = "SFRotation"
field73.value = [0,0,1,0]

ProtoInterface63.field.append(field73)
field74 = x3d.field()
field74.name = "segments"
field74.accessType = "inputOutput"
field74.appinfo = "Container field for Segment nodes"
field74.type = "MFNode"

ProtoInterface63.field.append(field74)
field75 = x3d.field()
field75.name = "sites"
field75.accessType = "inputOutput"
field75.appinfo = "Container field for Site nodes"
field75.type = "MFNode"

ProtoInterface63.field.append(field75)
field76 = x3d.field()
field76.name = "translation"
field76.accessType = "inputOutput"
field76.type = "SFVec3f"
field76.value = [0,0,0]

ProtoInterface63.field.append(field76)
field77 = x3d.field()
field77.name = "version"
field77.accessType = "inputOutput"
field77.appinfo = "legal values: 1.1 or 2.0"
field77.type = "SFString"
field77.value = "1.1"

ProtoInterface63.field.append(field77)
field78 = x3d.field()
field78.name = "viewpoints"
field78.accessType = "inputOutput"
field78.appinfo = "Container field for Viewpoint nodes"
field78.type = "MFNode"

ProtoInterface63.field.append(field78)

ProtoDeclare62.ProtoInterface = ProtoInterface63
ProtoBody79 = x3d.ProtoBody()
Transform80 = x3d.Transform()
Transform80.DEF = "HumanoidTransform"
IS81 = x3d.IS()
connect82 = x3d.connect()
connect82.nodeField = "bboxCenter"
connect82.protoField = "bboxCenter"

IS81.connect.append(connect82)
connect83 = x3d.connect()
connect83.nodeField = "bboxSize"
connect83.protoField = "bboxSize"

IS81.connect.append(connect83)
connect84 = x3d.connect()
connect84.nodeField = "center"
connect84.protoField = "center"

IS81.connect.append(connect84)
connect85 = x3d.connect()
connect85.nodeField = "rotation"
connect85.protoField = "rotation"

IS81.connect.append(connect85)
connect86 = x3d.connect()
connect86.nodeField = "scale"
connect86.protoField = "scale"

IS81.connect.append(connect86)
connect87 = x3d.connect()
connect87.nodeField = "scaleOrientation"
connect87.protoField = "scaleOrientation"

IS81.connect.append(connect87)
connect88 = x3d.connect()
connect88.nodeField = "translation"
connect88.protoField = "translation"

IS81.connect.append(connect88)

Transform80.IS = IS81
Group89 = x3d.Group()
Group89.DEF = "HumanoidGroup1"
IS90 = x3d.IS()
connect91 = x3d.connect()
connect91.nodeField = "children"
connect91.protoField = "humanoidBody"

IS90.connect.append(connect91)

Group89.IS = IS90

Transform80.children.append(Group89)
#<Group DEF=\"HumanoidGroup2\"> <IS> <connect nodeField=\"children\" protoField=\"segments\"/> </IS> </Group> <Group DEF=\"HumanoidGroup3\"> <IS> <connect nodeField=\"children\" protoField=\"sites\"/> </IS> </Group>
Group92 = x3d.Group()
Group92.DEF = "HumanoidGroup4"
IS93 = x3d.IS()
connect94 = x3d.connect()
connect94.nodeField = "children"
connect94.protoField = "viewpoints"

IS93.connect.append(connect94)

Group92.IS = IS93

Transform80.children.append(Group92)

ProtoBody79.children.append(Transform80)

ProtoDeclare62.ProtoBody = ProtoBody79

Scene17.children.append(ProtoDeclare62)
#Start scene graph.
ProtoInstance95 = x3d.ProtoInstance()
ProtoInstance95.name = "Humanoid"
ProtoInstance95.DEF = "Humanoid"
fieldValue96 = x3d.fieldValue()
fieldValue96.name = "humanoidBody"
ProtoInstance97 = x3d.ProtoInstance()
ProtoInstance97.name = "Joint"
ProtoInstance97.DEF = "hanim_humanoid_root"
fieldValue98 = x3d.fieldValue()
fieldValue98.name = "name"
fieldValue98.value = "humanoid_root"

ProtoInstance97.fieldValue.append(fieldValue98)
fieldValue99 = x3d.fieldValue()
fieldValue99.name = "center"
fieldValue99.value = "-0.00405 0.855 -0.000113"

ProtoInstance97.fieldValue.append(fieldValue99)
fieldValue100 = x3d.fieldValue()
fieldValue100.name = "children"
ProtoInstance101 = x3d.ProtoInstance()
ProtoInstance101.name = "Joint"
ProtoInstance101.DEF = "hanim_sacroiliac"
fieldValue102 = x3d.fieldValue()
fieldValue102.name = "name"
fieldValue102.value = "sacroiliac"

ProtoInstance101.fieldValue.append(fieldValue102)
fieldValue103 = x3d.fieldValue()
fieldValue103.name = "center"
fieldValue103.value = "0 1.01 -0.0204"

ProtoInstance101.fieldValue.append(fieldValue103)
fieldValue104 = x3d.fieldValue()
fieldValue104.name = "children"
ProtoInstance105 = x3d.ProtoInstance()
ProtoInstance105.name = "Segment"
ProtoInstance105.DEF = "hanim_pelvis"
fieldValue106 = x3d.fieldValue()
fieldValue106.name = "name"
fieldValue106.value = "pelvis"

ProtoInstance105.fieldValue.append(fieldValue106)
fieldValue107 = x3d.fieldValue()
fieldValue107.name = "children"
Transform108 = x3d.Transform()
Transform108.center = [-0.7455,1,0.058]
Transform108.rotation = [0,1,0,1.570796]
Transform108.scale = [0.1,0.1,0.1]
Shape109 = x3d.Shape()
Appearance110 = x3d.Appearance()
Material111 = x3d.Material()
Material111.DEF = "Pants_Color"
Material111.ambientIntensity = 0.25
Material111.diffuseColor = [0.054,0.233,0.39]

Appearance110.material = Material111
ImageTexture112 = x3d.ImageTexture()
ImageTexture112.DEF = "camo"
ImageTexture112.repeatS = False
ImageTexture112.repeatT = False
ImageTexture112.url = ["greenCamo.gif","greenCamo.jpg","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Prototypes/greenCamo.gif","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Prototypes/greenCamo.jpg"]

Appearance110.texture = ImageTexture112

Shape109.appearance = Appearance110
IndexedFaceSet113 = x3d.IndexedFaceSet()
IndexedFaceSet113.coordIndex = [0,1,2,-1,3,4,5,-1,6,7,8,-1,9,10,11,-1,12,13,14,-1,15,16,17,-1,18,19,20,-1,21,22,23,-1,24,25,26,-1,27,28,29,-1,30,31,32,-1,33,34,35,-1,36,37,38,-1,39,40,41,-1,42,43,44,-1,45,46,47,-1,48,49,50,-1,51,52,53,-1,54,55,56,-1,57,58,59,-1,60,61,62,-1,63,64,65,-1,66,67,68,-1,69,70,71,-1,72,73,74,-1,75,76,77,-1,78,79,80,-1,81,82,83,-1,84,85,86,-1,87,88,89,-1,90,91,92,-1,93,94,95,-1,96,97,98,-1,99,100,101,-1,102,103,104,-1,105,106,107,-1,108,109,110,-1,111,112,113,-1,114,115,116,-1,117,118,119,-1,120,121,122,-1,123,124,125,-1,126,127,128,-1,129,130,131,-1,132,133,134,-1,135,136,137,-1,138,139,140,-1,141,142,143,-1,144,145,146,-1,147,148,149,-1,150,151,152,-1,153,154,155,-1,156,157,158,-1,159,160,161,-1,162,163,164,-1,165,166,167,-1,168,169,170,-1,171,172,173,-1,174,175,176,-1,177,178,179,-1,180,181,182,-1,183,184,185,-1,186,187,188,-1,189,190,191,-1,192,193,194,-1,195,196,197,-1,198,199,200,-1,201,202,203,-1,204,205,206,-1,207,208,209,-1,210,211,212,-1,213,214,215,-1,216,217,218,-1,219,220,221,-1,222,223,224,-1,225,226,227,-1,228,229,230,-1,231,232,233,-1,234,235,236,-1,237,238,239,-1,240,241,242,-1,243,244,245,-1,246,247,248,-1,249,250,251,-1,252,253,254,-1,255,256,257,-1,258,259,260,-1,261,262,263,-1,264,265,266,-1,267,268,269,-1,270,271,272,-1,273,274,275,-1,276,277,278,-1,279,280,281,-1,282,283,284,-1,285,286,287,-1,288,289,290,-1,291,292,293,-1,294,295,296,-1,297,298,299,-1,300,301,302,-1,303,304,305,-1,306,307,308,-1,309,310,311,-1,312,313,314,-1,315,316,317,-1,318,319,320,-1,321,322,323,-1,324,325,326,-1,327,328,329,-1,330,331,332,-1,333,334,335,-1,336,337,338,-1,339,340,341,-1,342,343,344,-1,345,346,347,-1,348,349,350,-1,351,352,353,-1,354,355,356,-1,357,358,359,-1,360,361,362,-1,363,364,365,-1,366,367,368,-1,369,370,371,-1,372,373,374,-1,375,376,377,-1,378,379,380,-1,381,382,383,-1,384,385,386,-1,387,388,389,-1,390,391,392,-1,393,394,395,-1,396,397,398,-1,399,400,401,-1,402,403,404,-1,405,406,407,-1,408,409,410,-1,411,412,413,-1,414,415,416,-1,417,418,419,-1,420,421,422,-1,423,424,425,-1,426,427,428,-1,429,430,431,-1,432,433,434,-1,435,436,437,-1,438,439,440,-1,441,442,443,-1,444,445,446,-1,447,448,449,-1,450,451,452,-1,453,454,455,-1,456,457,458,-1,459,460,461,-1,462,463,464,-1,465,466,467,-1,468,469,470,-1,471,472,473,-1,474,475,476,-1,477,478,479,-1,480,481,482,-1,483,484,485,-1,486,487,488,-1,489,490,491,-1,492,493,494,-1,495,496,497,-1,498,499,500,-1,501,502,503,-1,504,505,506,-1,507,508,509,-1,510,511,512,-1,513,514,515,-1,516,517,518,-1,519,520,521,-1,522,523,524,-1,525,526,527,-1,528,529,530,-1,531,532,533,-1,534,535,536,-1,537,538,539,-1,540,541,542,-1,543,544,545,-1,546,547,548,-1,549,550,551,-1,552,553,554,-1,555,556,557,-1,558,559,560,-1,561,562,563,-1,564,565,566,-1,567,568,569,-1,570,571,572,-1,573,574,575,-1,576,577,578,-1,579,580,581,-1,582,583,584,-1,585,586,587,-1,588,589,590,-1,591,592,593,-1,594,595,596,-1,597,598,599,-1,600,601,602,-1,603,604,605,-1,606,607,608,-1,609,610,611,-1,612,613,614,-1,615,616,617,-1,618,619,620,-1,621,622,623,-1,624,625,626,-1,627,628,629,-1,630,631,632,-1,633,634,635,-1,636,637,638,-1,639,640,641,-1,642,643,644,-1,645,646,647,-1,648,649,650,-1,651,652,653,-1,654,655,656,-1,657,658,659,-1,660,661,662,-1,663,664,665,-1,666,667,668,-1,669,670,671,-1,672,673,674,-1,675,676,677,-1,678,679,680,-1,681,682,683,-1,684,685,686,-1,687,688,689,-1,690,691,692,-1,693,694,695,-1,696,697,698,-1,699,700,701,-1,702,703,704,-1,705,706,707,-1,708,709,710,-1,711,712,713,-1,714,715,716,-1,717,718,719,-1,720,721,722,-1,723,724,725,-1,726,727,728,-1,729,730,731,-1,732,733,734,-1,735,736,737,-1,738,739,740,-1,741,742,743,-1,744,745,746,-1,747,748,749,-1,750,751,752,-1,753,754,755,-1,756,757,758,-1,759,760,761,-1,762,763,764,-1,765,766,767,-1,768,769,770,-1,771,772,773,-1,774,775,776,-1,777,778,779,-1,780,781,782,-1,783,784,785,-1,786,787,788,-1,789,790,791,-1,792,793,794,-1,795,796,797,-1,798,799,800,-1,801,802,803,-1,804,805,806,-1,807,808,809,-1,810,811,812,-1,813,814,815,-1,816,817,818,-1,819,820,821,-1,822,823,824,-1,825,826,827,-1,828,829,830,-1,831,832,833,-1,834,835,836,-1,837,838,839,-1,840,841,842,-1,843,844,845,-1,846,847,848,-1,849,850,851,-1,852,853,854,-1,855,856,857,-1,858,859,860,-1,861,862,863,-1,864,865,866,-1,867,868,869,-1,870,871,872,-1,873,874,875,-1,876,877,878,-1,879,880,881,-1,882,883,884,-1,885,886,887,-1,888,889,890,-1,891,892,893,-1,894,895,896,-1,897,898,899,-1,900,901,902,-1,903,904,905,-1,906,907,908,-1,909,910,911,-1,912,913,914,-1,915,916,917,-1,918,919,920,-1,921,922,923,-1,924,925,926,-1,927,928,929,-1,930,931,932,-1,933,934,935,-1,936,937,938,-1,939,940,941,-1,942,943,944,-1,945,946,947,-1,948,949,950,-1,951,952,953,-1,954,955,956,-1,957,958,959,-1,960,961,962,-1,963,964,965,-1,966,967,968,-1,969,970,971,-1,972,973,974,-1,975,976,977,-1,978,979,980,-1,981,982,983,-1,984,985,986,-1,987,988,989,-1,990,991,992,-1,993,994,995,-1,996,997,998,-1,999,1000,1001,-1,1002,1003,1004,-1,1005,1006,1007,-1,1008,1009,1010,-1,1011,1012,1013,-1,1014,1015,1016,-1,1017,1018,1019,-1,1020,1021,1022,-1,1023,1024,1025,-1,1026,1027,1028,-1,1029,1030,1031,-1,1032,1033,1034,-1,1035,1036,1037,-1,1038,1039,1040,-1,1041,1042,1043,-1,1044,1045,1046,-1,1047,1048,1049,-1,1050,1051,1052,-1,1053,1054,1055,-1,1056,1057,1058,-1,1059,1060,1061,-1,1062,1063,1064,-1,1065,1066,1067,-1,1068,1069,1070,-1,1071,1072,1073,-1,1074,1075,1076,-1,1077,1078,1079,-1,1080,1081,1082,-1,1083,1084,1085,-1,1086,1087,1088,-1,1089,1090,1091,-1,1092,1093,1094,-1,1095,1096,1097,-1,1098,1099,1100,-1,1101,1102,1103,-1,1104,1105,1106,-1,1107,1108,1109,-1,1110,1111,1112,-1,1113,1114,1115,-1,1116,1117,1118,-1,1119,1120,1121,-1,1122,1123,1124,-1,1125,1126,1127,-1,1128,1129,1130,-1,1131,1132,1133,-1,1134,1135,1136,-1,1137,1138,1139,-1,1140,1141,1142,-1,1143,1144,1145,-1,1146,1147,1148,-1,1149,1150,1151,-1,1152,1153,1154,-1,1155,1156,1157,-1,1158,1159,1160,-1,1161,1162,1163,-1,1164,1165,1166,-1,1167,1168,1169,-1,1170,1171,1172,-1,1173,1174,1175,-1,1176,1177,1178,-1,1179,1180,1181,-1,1182,1183,1184,-1,1185,1186,1187,-1,1188,1189,1190,-1,1191,1192,1193,-1,1194,1195,1196,-1,1197,1198,1199,-1,1200,1201,1202,-1,1203,1204,1205,-1,1206,1207,1208,-1,1209,1210,1211,-1,1212,1213,1214,-1,1215,1216,1217,-1,1218,1219,1220,-1,1221,1222,1223,-1,1224,1225,1226,-1,1227,1228,1229,-1,1230,1231,1232,-1,1233,1234,1235,-1,1236,1237,1238,-1,1239,1240,1241,-1,1242,1243,1244,-1,1245,1246,1247,-1,1248,1249,1250,-1,1251,1252,1253,-1,1254,1255,1256,-1,1257,1258,1259,-1,1260,1261,1262,-1,1263,1264,1265,-1,1266,1267,1268,-1,1269,1270,1271,-1,1272,1273,1274,-1,1275,1276,1277,-1,1278,1279,1280,-1,1281,1282,1283,-1,1284,1285,1286,-1,1287,1288,1289,-1,1290,1291,1292,-1,1293,1294,1295,-1,1296,1297,1298,-1,1299,1300,1301,-1,1302,1303,1304,-1,1305,1306,1307,-1,1308,1309,1310,-1,1311,1312,1313,-1,1314,1315,1316,-1,1317,1318,1319,-1,1320,1321,1322,-1,1323,1324,1325,-1,1326,1327,1328,-1,1329,1330,1331,-1,1332,1333,1334,-1,1335,1336,1337,-1,1338,1339,1340,-1,1341,1342,1343,-1,1344,1345,1346,-1,1347,1348,1349,-1,1350,1351,1352,-1,1353,1354,1355,-1,1356,1357,1358,-1,1359,1360,1361,-1,1362,1363,1364,-1,1365,1366,1367,-1,1368,1369,1370,-1,1371,1372,1373,-1,1374,1375,1376,-1,1377,1378,1379,-1,1380,1381,1382,-1,1383,1384,1385,-1,1386,1387,1388,-1,1389,1390,1391,-1,1392,1393,1394,-1,1395,1396,1397,-1,1398,1399,1400,-1,1401,1402,1403,-1,1404,1405,1406,-1,1407,1408,1409,-1,1410,1411,1412,-1,1413,1414,1415,-1,1416,1417,1418,-1,1419,1420,1421,-1,1422,1423,1424,-1,1425,1426,1427,-1,1428,1429,1430,-1,1431,1432,1433,-1,1434,1435,1436,-1,1437,1438,1439,-1,1440,1441,1442,-1,1443,1444,1445,-1,1446,1447,1448,-1,1449,1450,1451,-1,1452,1453,1454,-1,1455,1456,1457,-1,1458,1459,1460,-1,1461,1462,1463,-1,1464,1465,1466,-1,1467,1468,1469,-1,1470,1471,1472,-1,1473,1474,1475,-1,1476,1477,1478,-1,1479,1480,1481,-1,1482,1483,1484,-1,1485,1486,1487,-1,1488,1489,1490,-1,1491,1492,1493,-1,1494,1495,1496,-1,1497,1498,1499,-1,1500,1501,1502,-1,1503,1504,1505,-1,1506,1507,1508,-1,1509,1510,1511,-1,1512,1513,1514,-1,1515,1516,1517,-1,1518,1519,1520,-1,1521,1522,1523,-1,1524,1525,1526,-1,1527,1528,1529,-1,1530,1531,1532,-1,1533,1534,1535,-1,1536,1537,1538,-1,1539,1540,1541,-1,1542,1543,1544,-1,1545,1546,1547,-1,1548,1549,1550,-1,1551,1552,1553,-1,1554,1555,1556,-1,1557,1558,1559,-1,1560,1561,1562,-1,1563,1564,1565,-1,1566,1567,1568,-1,1569,1570,1571,-1,1572,1573,1574,-1,1575,1576,1577,-1,1578,1579,1580,-1,1581,1582,1583,-1,1584,1585,1586,-1,1587,1588,1589,-1,1590,1591,1592,-1,1593,1594,1595,-1,1596,1597,1598,-1,1599,1600,1601,-1,1602,1603,1604,-1,1605,1606,1607,-1,1608,1609,1610,-1,1611,1612,1613,-1,1614,1615,1616,-1,1617,1618,1619,-1,1620,1621,1622,-1,1623,1624,1625,-1,1626,1627,1628,-1,1629,1630,1631,-1,1632,1633,1634,-1,1635,1636,1637,-1,1638,1639,1640,-1,1641,1642,1643,-1,1644,1645,1646,-1,1647,1648,1649,-1,1650,1651,1652,-1,1653,1654,1655,-1,1656,1657,1658,-1,1659,1660,1661,-1,1662,1663,1664,-1,1665,1666,1667,-1,1668,1669,1670,-1,1671,1672,1673,-1,1674,1675,1676,-1,1677,1678,1679,-1,1680,1681,1682,-1,1683,1684,1685,-1,1686,1687,1688,-1,1689,1690,1691,-1,1692,1693,1694,-1,1695,1696,1697,-1,1698,1699,1700,-1,1701,1702,1703,-1,1704,1705,1706,-1,1707,1708,1709,-1,1710,1711,1712,-1,1713,1714,1715,-1,1716,1717,1718,-1,1719,1720,1721,-1,1722,1723,1724,-1,1725,1726,1727,-1,1728,1729,1730,-1,1731,1732,1733,-1,1734,1735,1736,-1,1737,1738,1739,-1,1740,1741,1742,-1,1743,1744,1745,-1,1746,1747,1748,-1,1749,1750,1751,-1,1752,1753,1754,-1,1755,1756,1757,-1,1758,1759,1760,-1,1761,1762,1763,-1,1764,1765,1766,-1,1767,1768,1769,-1,1770,1771,1772,-1,1773,1774,1775,-1,1776,1777,1778,-1,1779,1780,1781,-1,1782,1783,1784,-1,1785,1786,1787,-1,1788,1789,1790,-1,1791,1792,1793,-1,1794,1795,1796,-1,1797,1798,1799,-1,1800,1801,1802,-1,1803,1804,1805,-1,1806,1807,1808,-1,1809,1810,1811,-1,1812,1813,1814,-1,1815,1816,1817,-1,1818,1819,1820,-1,1821,1822,1823,-1,1824,1825,1826,-1,1827,1828,1829,-1,1830,1831,1832,-1,1833,1834,1835,-1,1836,1837,1838,-1,1839,1840,1841,-1,1842,1843,1844,-1,1845,1846,1847,-1,1848,1849,1850,-1,1851,1852,1853,-1,1854,1855,1856,-1,1857,1858,1859,-1,1860,1861,1862,-1,1863,1864,1865,-1,1866,1867,1868,-1,1869,1870,1871,-1,1872,1873,1874,-1,1875,1876,1877,-1,1878,1879,1880,-1,1881,1882,1883,-1,1884,1885,1886,-1,1887,1888,1889,-1,1890,1891,1892,-1,1893,1894,1895,-1,1896,1897,1898,-1,1899,1900,1901,-1,1902,1903,1904,-1,1905,1906,1907,-1,1908,1909,1910,-1,1911,1912,1913,-1,1914,1915,1916,-1,1917,1918,1919,-1,1920,1921,1922,-1,1923,1924,1925,-1,1926,1927,1928,-1,1929,1930,1931,-1,1932,1933,1934,-1,1935,1936,1937,-1,1938,1939,1940,-1,1941,1942,1943,-1,1944,1945,1946,-1,1947,1948,1949,-1,1950,1951,1952,-1,1953,1954,1955,-1,1956,1957,1958,-1,1959,1960,1961,-1,1962,1963,1964,-1,1965,1966,1967,-1,1968,1969,1970,-1,1971,1972,1973,-1,1974,1975,1976,-1,1977,1978,1979,-1,1980,1981,1982,-1,1983,1984,1985,-1,1986,1987,1988,-1,1989,1990,1991,-1,1992,1993,1994,-1,1995,1996,1997,-1,1998,1999,2000,-1,2001,2002,2003,-1,2004,2005,2006,-1,2007,2008,2009,-1,2010,2011,2012,-1,2013,2014,2015,-1,2016,2017,2018,-1,2019,2020,2021,-1,2022,2023,2024,-1,2025,2026,2027,-1,2028,2029,2030,-1,2031,2032,2033,-1,2034,2035,2036,-1,2037,2038,2039,-1,2040,2041,2042,-1,2043,2044,2045,-1,2046,2047,2048,-1,2049,2050,2051,-1,2052,2053,2054,-1,2055,2056,2057,-1,2058,2059,2060,-1,2061,2062,2063,-1,2064,2065,2066,-1,2067,2068,2069,-1,2070,2071,2072,-1,2073,2074,2075,-1,2076,2077,2078,-1,2079,2080,2081,-1,2082,2083,2084,-1,2085,2086,2087,-1,2088,2089,2090,-1,2091,2092,2093,-1,2094,2095,2096,-1,2097,2098,2099,-1,2100,2101,2102,-1,2103,2104,2105,-1,2106,2107,2108,-1,2109,2110,2111,-1,2112,2113,2114,-1,2115,2116,2117,-1,2118,2119,2120,-1,2121,2122,2123,-1,2124,2125,2126,-1,2127,2128,2129,-1,2130,2131,2132,-1,2133,2134,2135,-1,2136,2137,2138,-1,2139,2140,2141,-1,2142,2143,2144,-1,2145,2146,2147,-1,2148,2149,2150,-1,2151,2152,2153,-1,2154,2155,2156,-1,2157,2158,2159,-1,2160,2161,2162,-1,2163,2164,2165,-1,2166,2167,2168,-1,2169,2170,2171,-1,2172,2173,2174,-1,2175,2176,2177,-1,2178,2179,2180,-1,2181,2182,2183,-1,2184,2185,2186,-1,2187,2188,2189,-1,2190,2191,2192,-1,2193,2194,2195,-1,2196,2197,2198,-1,2199,2200,2201,-1,2202,2203,2204,-1,2205,2206,2207,-1,2208,2209,2210,-1,2211,2212,2213,-1,2214,2215,2216,-1,2217,2218,2219,-1,2220,2221,2222,-1,2223,2224,2225,-1,2226,2227,2228,-1,2229,2230,2231,-1,2232,2233,2234,-1,2235,2236,2237,-1,2238,2239,2240,-1,2241,2242,2243,-1,2244,2245,2246,-1,2247,2248,2249,-1,2250,2251,2252,-1,2253,2254,2255,-1,2256,2257,2258,-1,2259,2260,2261,-1,2262,2263,2264,-1,2265,2266,2267,-1,2268,2269,2270,-1,2271,2272,2273,-1,2274,2275,2276,-1,2277,2278,2279,-1,2280,2281,2282,-1,2283,2284,2285,-1,2286,2287,2288,-1,2289,2290,2291,-1,2292,2293,2294,-1,2295,2296,2297,-1,2298,2299,2300,-1,2301,2302,2303,-1,2304,2305,2306,-1,2307,2308,2309,-1,2310,2311,2312,-1,2313,2314,2315,-1,2316,2317,2318,-1,2319,2320,2321,-1,2322,2323,2324,-1,2325,2326,2327,-1,2328,2329,2330,-1,2331,2332,2333,-1,2334,2335,2336,-1,2337,2338,2339,-1,2340,2341,2342,-1,2343,2344,2345,-1,2346,2347,2348,-1,2349,2350,2351,-1,2352,2353,2354,-1,2355,2356,2357,-1,2358,2359,2360,-1,2361,2362,2363,-1,2364,2365,2366,-1,2367,2368,2369,-1,2370,2371,2372,-1,2373,2374,2375,-1,2376,2377,2378,-1,2379,2380,2381,-1,2382,2383,2384,-1,2385,2386,2387,-1,2388,2389,2390,-1,2391,2392,2393,-1,2394,2395,2396,-1,2397,2398,2399,-1,2400,2401,2402,-1,2403,2404,2405,-1,2406,2407,2408,-1,2409,2410,2411,-1,2412,2413,2414,-1,2415,2416,2417,-1,2418,2419,2420,-1,2421,2422,2423,-1,2424,2425,2426,-1,2427,2428,2429,-1,2430,2431,2432,-1,2433,2434,2435,-1,2436,2437,2438,-1,2439,2440,2441,-1,2442,2443,2444,-1,2445,2446,2447,-1,2448,2449,2450,-1,2451,2452,2453,-1,2454,2455,2456,-1,2457,2458,2459,-1,2460,2461,2462,-1,2463,2464,2465,-1,2466,2467,2468,-1,2469,2470,2471,-1,2472,2473,2474,-1,2475,2476,2477,-1,2478,2479,2480,-1,2481,2482,2483,-1,2484,2485,2486,-1,2487,2488,2489,-1,2490,2491,2492,-1,2493,2494,2495,-1,2496,2497,2498,-1,2499,2500,2501,-1,2502,2503,2504,-1,2505,2506,2507,-1,2508,2509,2510,-1,2511,2512,2513,-1,2514,2515,2516,-1,2517,2518,2519,-1,2520,2521,2522,-1,2523,2524,2525,-1,2526,2527,2528,-1,2529,2530,2531,-1,2532,2533,2534,-1,2535,2536,2537,-1,2538,2539,2540,-1,2541,2542,2543,-1,2544,2545,2546,-1,2547,2548,2549,-1,2550,2551,2552,-1,2553,2554,2555,-1,2556,2557,2558,-1,2559,2560,2561,-1,2562,2563,2564,-1,2565,2566,2567,-1,2568,2569,2570,-1,2571,2572,2573,-1,2574,2575,2576,-1,2577,2578,2579,-1,2580,2581,2582,-1,2583,2584,2585,-1,2586,2587,2588,-1,2589,2590,2591,-1,2592,2593,2594,-1,2595,2596,2597,-1,2598,2599,2600,-1,2601,2602,2603,-1,2604,2605,2606,-1,2607,2608,2609,-1,2610,2611,2612,-1,2613,2614,2615,-1,2616,2617,2618,-1,2619,2620,2621,-1,2622,2623,2624,-1,2625,2626,2627,-1,2628,2629,2630,-1,2631,2632,2633,-1,2634,2635,2636,-1,2637,2638,2639,-1,2640,2641,2642,-1,2643,2644,2645,-1,2646,2647,2648,-1,2649,2650,2651,-1,2652,2653,2654,-1,2655,2656,2657,-1,2658,2659,2660,-1,2661,2662,2663,-1,2664,2665,2666,-1,2667,2668,2669,-1,2670,2671,2672,-1,2673,2674,2675,-1,2676,2677,2678,-1,2679,2680,2681,-1,2682,2683,2684,-1,2685,2686,2687,-1,2688,2689,2690,-1,2691,2692,2693,-1,2694,2695,2696,-1,2697,2698,2699,-1,2700,2701,2702,-1,2703,2704,2705,-1,2706,2707,2708,-1,2709,2710,2711,-1,2712,2713,2714,-1,2715,2716,2717,-1,2718,2719,2720,-1,2721,2722,2723,-1,2724,2725,2726,-1,2727,2728,2729,-1,2730,2731,2732,-1,2733,2734,2735,-1,2736,2737,2738,-1,2739,2740,2741,-1,2742,2743,2744,-1,2745,2746,2747,-1,2748,2749,2750,-1,2751,2752,2753,-1,2754,2755,2756,-1,2757,2758,2759,-1,2760,2761,2762,-1,2763,2764,2765,-1,2766,2767,2768,-1,2769,2770,2771,-1,2772,2773,2774,-1,2775,2776,2777,-1,2778,2779,2780,-1,2781,2782,2783,-1,2784,2785,2786,-1,2787,2788,2789,-1,2790,2791,2792,-1,2793,2794,2795,-1,2796,2797,2798,-1,2799,2800,2801,-1,2802,2803,2804,-1,2805,2806,2807,-1,2808,2809,2810,-1,2811,2812,2813,-1,2814,2815,2816,-1,2817,2818,2819,-1,2820,2821,2822,-1,2823,2824,2825,-1,2826,2827,2828,-1,2829,2830,2831,-1,2832,2833,2834,-1,2835,2836,2837,-1,2838,2839,2840,-1,2841,2842,2843,-1,2844,2845,2846,-1,2847,2848,2849,-1,2850,2851,2852,-1,2853,2854,2855,-1,2856,2857,2858,-1,2859,2860,2861,-1,2862,2863,2864,-1,2865,2866,2867,-1,2868,2869,2870,-1,2871,2872,2873,-1,2874,2875,2876,-1,2877,2878,2879,-1,2880,2881,2882,-1,2883,2884,2885,-1,2886,2887,2888,-1,2889,2890,2891,-1,2892,2893,2894,-1,2895,2896,2897,-1,2898,2899,2900,-1,2901,2902,2903,-1,2904,2905,2906,-1,2907,2908,2909,-1,2910,2911,2912,-1,2913,2914,2915,-1,2916,2917,2918,-1,2919,2920,2921,-1,2922,2923,2924,-1,2925,2926,2927,-1,2928,2929,2930,-1,2931,2932,2933,-1,2934,2935,2936,-1,2937,2938,2939,-1,2940,2941,2942,-1,2943,2944,2945,-1,2946,2947,2948,-1,2949,2950,2951,-1,2952,2953,2954,-1,2955,2956,2957,-1,2958,2959,2960,-1,2961,2962,2963,-1,2964,2965,2966,-1,2967,2968,2969,-1,2970,2971,2972,-1,2973,2974,2975,-1,2976,2977,2978,-1,2979,2980,2981,-1,2982,2983,2984,-1,2985,2986,2987,-1,2988,2989,2990,-1,2991,2992,2993,-1,2994,2995,2996,-1,2997,2998,2999,-1]
IndexedFaceSet113.creaseAngle = 1.14
Coordinate114 = x3d.Coordinate()

IndexedFaceSet113.coord = Coordinate114

Shape109.geometry = IndexedFaceSet113

Transform108.children.append(Shape109)

fieldValue107.children.append(Transform108)

ProtoInstance105.fieldValue.append(fieldValue107)

fieldValue104.children.append(ProtoInstance105)
ProtoInstance115 = x3d.ProtoInstance()
ProtoInstance115.name = "Joint"
ProtoInstance115.DEF = "hanim_l_hip"
fieldValue116 = x3d.fieldValue()
fieldValue116.name = "name"
fieldValue116.value = "l_hip"

ProtoInstance115.fieldValue.append(fieldValue116)
fieldValue117 = x3d.fieldValue()
fieldValue117.name = "center"
fieldValue117.value = "0.122 0.888271 -0.0693267"

ProtoInstance115.fieldValue.append(fieldValue117)
fieldValue118 = x3d.fieldValue()
fieldValue118.name = "children"
ProtoInstance119 = x3d.ProtoInstance()
ProtoInstance119.name = "Segment"
ProtoInstance119.DEF = "hanim_l_thigh"
fieldValue120 = x3d.fieldValue()
fieldValue120.name = "name"
fieldValue120.value = "l_thigh"

ProtoInstance119.fieldValue.append(fieldValue120)
fieldValue121 = x3d.fieldValue()
fieldValue121.name = "children"
Transform122 = x3d.Transform()
Transform122.DEF = "l_thigh_adjust"
Transform122.center = [-0.7,1.1,0.04]
Transform122.rotation = [0,1,0,1.570796]
Transform122.scale = [0.1,0.1,0.1]
Shape123 = x3d.Shape()
Appearance124 = x3d.Appearance()
Material125 = x3d.Material()
Material125.USE = "Pants_Color"

Appearance124.material = Material125
ImageTexture126 = x3d.ImageTexture()
ImageTexture126.USE = "camo"

Appearance124.texture = ImageTexture126

Shape123.appearance = Appearance124
IndexedFaceSet127 = x3d.IndexedFaceSet()
IndexedFaceSet127.coordIndex = [0,1,2,-1,3,4,5,-1,6,7,8,-1,9,10,11,-1,12,13,14,-1,15,16,17,-1,18,19,20,-1,21,22,23,-1,24,25,26,-1,27,28,29,-1,30,31,32,-1,33,34,35,-1,36,37,38,-1,39,40,41,-1,42,43,44,-1,45,46,47,-1,48,49,50,-1,51,52,53,-1,54,55,56,-1,57,58,59,-1,60,61,62,-1,63,64,65,-1,66,67,68,-1,69,70,71,-1,72,73,74,-1,75,76,77,-1,78,79,80,-1,81,82,83,-1,84,85,86,-1,87,88,89,-1,90,91,92,-1,93,94,95,-1,96,97,98,-1,99,100,101,-1,102,103,104,-1,105,106,107,-1,108,109,110,-1,111,112,113,-1,114,115,116,-1,117,118,119,-1,120,121,122,-1,123,124,125,-1,126,127,128,-1,129,130,131,-1,132,133,134,-1,135,136,137,-1,138,139,140,-1,141,142,143,-1,144,145,146,-1,147,148,149,-1,150,151,152,-1,153,154,155,-1,156,157,158,-1,159,160,161,-1,162,163,164,-1,165,166,167,-1,168,169,170,-1,171,172,173,-1,174,175,176,-1,177,178,179,-1,180,181,182,-1,183,184,185,-1,181,183,182,-1,183,185,182,-1,183,158,184,-1,157,159,158,-1,164,165,162,-1,167,168,165,-1,165,168,162,-1,172,174,173,-1,176,179,174,-1,174,179,173,-1,179,178,173,-1,182,185,178,-1,178,185,173,-1,185,184,173,-1,184,158,173,-1,158,159,173,-1,170,173,168,-1,159,161,173,-1,173,161,168,-1,162,168,161,-1,186,187,188,-1,189,190,191,-1,192,193,194,-1,195,196,197,-1,198,199,200,-1,201,202,203,-1,204,205,206,-1,207,208,209,-1,210,211,212,-1,213,214,215,-1,216,217,218,-1,219,220,221,-1,222,223,224,-1,225,226,227,-1,228,229,230,-1,231,232,233,-1,234,235,236,-1,237,238,239,-1,240,241,242,-1,243,244,245,-1,246,247,248,-1,249,250,251,-1,252,253,254,-1,255,256,257,-1,258,259,260,-1,261,262,263,-1,264,265,266,-1,267,268,269,-1,270,271,272,-1,273,274,275,-1,276,277,278,-1,279,280,281,-1,282,283,284,-1,285,286,287,-1,288,289,290,-1,291,292,293,-1,294,295,296,-1,297,298,299,-1,300,301,302,-1,303,304,305,-1,306,307,308,-1,309,310,311,-1,312,313,314,-1,315,316,317,-1,318,319,320,-1,321,322,323,-1,324,325,326,-1,327,328,329,-1,330,331,332,-1,333,334,335,-1,336,337,338,-1,339,340,341,-1,342,343,344,-1,345,346,347,-1,348,349,350,-1,351,352,353,-1,354,355,356,-1,357,358,359,-1,360,361,362,-1,363,364,365,-1,366,367,368,-1,369,370,371,-1,372,373,374,-1,375,376,377,-1,378,379,380,-1,381,382,383,-1,384,385,386,-1,387,388,389,-1,390,391,392,-1,393,394,395,-1,396,397,398,-1,399,400,401,-1,402,403,404,-1,405,406,407,-1,408,409,410,-1,411,412,413,-1,414,415,416,-1,417,418,419,-1,420,421,422,-1,423,424,425,-1,426,427,428,-1,429,430,431,-1,432,433,434,-1,435,436,437,-1,438,439,440,-1,441,442,443,-1,444,445,446,-1,447,448,449,-1,450,451,452,-1,453,454,455,-1,456,457,458,-1,459,460,461,-1,462,463,464,-1,465,466,467,-1,468,469,470,-1,471,472,473,-1,474,475,476,-1,477,478,479,-1,480,481,482,-1,483,484,485,-1,486,487,488,-1,489,490,491,-1,492,493,494,-1,495,496,497,-1,498,499,500,-1,501,502,503,-1,504,505,506,-1,507,508,509,-1,510,511,512,-1,513,514,515,-1,516,517,518,-1,519,520,521,-1,522,523,524,-1,525,526,527,-1,528,529,530,-1,531,532,533,-1,534,535,536,-1,537,538,539,-1,540,541,542,-1,543,544,545,-1,546,547,548,-1,549,550,551,-1,552,553,554,-1,555,556,557,-1,558,559,560,-1,561,562,563,-1,564,565,566,-1,567,568,569,-1,570,571,572,-1,573,574,575,-1,576,577,578,-1,579,580,581,-1,582,583,584,-1,585,586,587,-1,588,589,590,-1,591,592,593,-1,594,595,596,-1,597,598,599,-1,600,601,602,-1,603,604,605,-1,606,607,608,-1,609,610,611,-1,612,613,614,-1,615,616,617,-1,618,619,620,-1,621,622,623,-1,624,625,626,-1,627,628,629,-1,630,631,632,-1,633,634,635,-1,636,637,638,-1,639,640,641,-1,642,643,644,-1,645,646,647,-1,648,649,650,-1,651,652,653,-1,654,655,656,-1,657,658,659,-1,660,661,662,-1,663,664,665,-1,666,667,668,-1,669,670,671,-1,672,673,674,-1,675,676,677,-1,678,679,680,-1,681,682,683,-1,684,685,686,-1,687,688,689,-1,690,691,692,-1,693,694,695,-1,696,697,698,-1,699,700,701,-1,702,703,704,-1,705,706,707,-1,708,709,710,-1,711,712,713,-1,714,715,716,-1,717,718,719,-1,720,721,722,-1,723,724,725,-1,726,727,728,-1,729,730,731,-1,732,733,734,-1,735,736,737,-1,738,739,740,-1,741,742,743,-1,744,745,746,-1,747,748,749,-1,750,751,752,-1,753,754,755,-1,756,757,758,-1,759,760,761,-1,762,763,764,-1,765,766,767,-1,768,769,770,-1,771,772,773,-1,774,775,776,-1,777,778,779,-1,780,781,782,-1,783,784,785,-1,786,787,788,-1,789,790,791,-1,792,793,794,-1,795,796,797,-1,798,799,800,-1,801,802,803,-1,804,805,806,-1,807,808,809,-1,810,811,812,-1,813,814,815,-1,816,817,818,-1,819,820,821,-1,822,823,824,-1,825,826,827,-1,828,829,830,-1,831,832,833,-1,834,835,836,-1,837,838,839,-1,840,841,842,-1,843,844,845,-1,846,847,848,-1,849,850,851,-1,852,853,854,-1,855,856,857,-1,858,859,860,-1,861,862,863,-1,864,865,866,-1,867,868,869,-1,870,871,872,-1,873,874,875,-1,876,877,878,-1,879,880,881,-1,882,883,884,-1,885,886,887,-1,888,889,890,-1,891,892,893,-1,894,895,896,-1,897,898,899,-1,900,901,902,-1,903,904,905,-1,906,907,908,-1,909,910,911,-1,912,913,914,-1,915,916,917,-1,918,919,920,-1,921,922,923,-1,924,925,926,-1,927,928,929,-1,930,931,932,-1,933,934,935,-1,936,937,938,-1,939,940,941,-1,942,943,944,-1,945,946,947,-1,948,949,950,-1,951,952,953,-1,954,955,956,-1,957,958,959,-1,960,961,962,-1,963,964,965,-1,966,967,968,-1,969,970,971,-1,972,973,974,-1,975,976,977,-1,978,979,980,-1,981,982,983,-1,984,985,986,-1,987,988,989,-1,990,991,992,-1,993,994,995,-1,996,997,998,-1,999,1000,1001,-1,1002,1003,1004,-1,1005,1006,1007,-1,1008,1009,1010,-1,1011,1012,1013,-1,1014,1015,1016,-1,1017,1018,1019,-1,1020,1021,1022,-1,1023,1024,1025,-1,1026,1027,1028,-1,1029,1030,1031,-1,1032,1033,1034,-1,1035,1036,1037,-1,1038,1039,1040,-1,1041,1042,1043,-1,1044,1045,1046,-1,1047,1048,1049,-1,1050,1051,1052,-1,1053,1054,1055,-1,1056,1057,1058,-1,1059,1060,1061,-1,1062,1063,1064,-1,1065,1066,1067,-1,1068,1069,1070,-1,1071,1072,1073,-1,1074,1075,1076,-1,1077,1078,1079,-1,1080,1081,1082,-1,1083,1084,1085,-1,1086,1087,1088,-1,1089,1090,1091,-1,1092,1093,1094,-1,1095,1096,1097,-1,1098,1099,1100,-1,1101,1102,1103,-1,1104,1105,1106,-1,1107,1108,1109,-1,1110,1111,1112,-1,1113,1114,1115,-1,1116,1117,1118,-1,1119,1120,1121,-1,1122,1123,1124,-1,1125,1126,1127,-1,1128,1129,1130,-1,1131,1132,1133,-1,1134,1135,1136,-1,1137,1138,1139,-1,1140,1141,1142,-1,1143,1144,1145,-1,1146,1147,1148,-1,1149,1150,1151,-1,1152,1153,1154,-1,1155,1156,1157,-1,1158,1159,1160,-1,1161,1162,1163,-1,1164,1165,1166,-1,1167,1168,1169,-1,1170,1171,1172,-1,1173,1174,1175,-1,1176,1177,1178,-1,1179,1180,1181,-1,1182,1183,1184,-1,1185,1186,1187,-1,1188,1189,1190,-1,1191,1192,1193,-1,1194,1195,1196,-1,1197,1198,1199,-1,1200,1201,1202,-1,1203,1204,1205,-1,1206,1207,1208,-1,1209,1210,1211,-1,1212,1213,1214,-1,1215,1216,1217,-1,1218,1219,1220,-1,1221,1222,1223,-1,1224,1225,1226,-1,1227,1228,1229,-1,1230,1231,1232,-1,1233,1234,1235,-1,1236,1237,1238,-1,1239,1240,1241,-1,1242,1243,1244,-1,1245,1246,1247,-1,1248,1249,1250,-1,1251,1252,1253,-1,1254,1255,1256,-1,1257,1258,1259,-1,1260,1261,1262,-1,1263,1264,1265,-1,1266,1267,1268,-1,1269,1270,1271,-1,1272,1273,1274,-1,1275,1276,1277,-1,1278,1279,1280,-1,1281,1282,1283,-1,1284,1285,1286,-1,1287,1288,1289,-1,1290,1291,1292,-1,1293,1294,1295,-1,1296,1297,1298,-1,1299,1300,1301,-1,1302,1303,1304,-1,1305,1306,1307,-1,1308,1309,1310,-1,1311,1312,1313,-1,1314,1315,1316,-1,1317,1318,1319,-1,1320,1321,1322,-1,1323,1324,1325,-1,1326,1327,1328,-1,1329,1330,1331,-1,1332,1333,1334,-1,1335,1336,1337,-1,1338,1339,1340,-1,1341,1342,1343,-1,1344,1345,1346,-1,1347,1348,1349,-1,1350,1351,1352,-1,1353,1354,1355,-1,1356,1357,1358,-1,1359,1360,1361,-1,1362,1363,1364,-1,1365,1366,1367,-1,1368,1369,1370,-1,1371,1372,1373,-1,1374,1375,1376,-1,1377,1378,1379,-1,1380,1381,1382,-1,1383,1384,1385,-1,1386,1387,1388,-1,1389,1390,1391,-1,1392,1393,1394,-1,1395,1396,1397,-1,1398,1399,1400,-1,1401,1402,1403,-1,1404,1405,1406,-1,1407,1408,1409,-1,1410,1411,1412,-1,1413,1414,1415,-1,1416,1417,1418,-1,1419,1420,1421,-1,1422,1423,1424,-1,1425,1426,1427,-1,1428,1429,1430,-1,1431,1432,1433,-1,1434,1435,1436,-1,1437,1438,1439,-1,1440,1441,1442,-1,1443,1444,1445,-1,1446,1447,1448,-1,1449,1450,1451,-1,1452,1453,1454,-1,1455,1456,1457,-1,1458,1459,1460,-1,1461,1462,1463,-1,1464,1465,1466,-1,1467,1468,1469,-1,1470,1471,1472,-1,1473,1474,1475,-1,1476,1477,1478,-1,1479,1480,1481,-1,1482,1483,1484,-1,1485,1486,1487,-1,1488,1489,1490,-1,1491,1492,1493,-1,1494,1495,1496,-1,1497,1498,1499,-1,1500,1501,1502,-1,1503,1504,1505,-1,1506,1507,1508,-1,1509,1510,1511,-1,1512,1513,1514,-1,1515,1516,1517,-1,1518,1519,1520,-1,1521,1522,1523,-1,1524,1525,1526,-1,1527,1528,1529,-1,1530,1531,1532,-1,1533,1534,1535,-1,1536,1537,1538,-1,1539,1540,1541,-1,1542,1543,1544,-1,1545,1546,1547,-1,1548,1549,1550,-1]
IndexedFaceSet127.creaseAngle = 1.32
Coordinate128 = x3d.Coordinate()

IndexedFaceSet127.coord = Coordinate128

Shape123.geometry = IndexedFaceSet127

Transform122.children.append(Shape123)

fieldValue121.children.append(Transform122)

ProtoInstance119.fieldValue.append(fieldValue121)

fieldValue118.children.append(ProtoInstance119)
ProtoInstance129 = x3d.ProtoInstance()
ProtoInstance129.name = "Joint"
ProtoInstance129.DEF = "hanim_l_knee"
fieldValue130 = x3d.fieldValue()
fieldValue130.name = "name"
fieldValue130.value = "l_knee"

ProtoInstance129.fieldValue.append(fieldValue130)
fieldValue131 = x3d.fieldValue()
fieldValue131.name = "center"
fieldValue131.value = "0.0738 0.517 -0.0284"

ProtoInstance129.fieldValue.append(fieldValue131)
fieldValue132 = x3d.fieldValue()
fieldValue132.name = "children"
ProtoInstance133 = x3d.ProtoInstance()
ProtoInstance133.name = "Segment"
ProtoInstance133.DEF = "hanim_l_calf"
fieldValue134 = x3d.fieldValue()
fieldValue134.name = "name"
fieldValue134.value = "l_calf"

ProtoInstance133.fieldValue.append(fieldValue134)
fieldValue135 = x3d.fieldValue()
fieldValue135.name = "children"
Transform136 = x3d.Transform()
Transform136.DEF = "l_calf_adjust"
Transform136.center = [-0.012,1.1,-0.01]
Transform136.rotation = [0,1,0,1.570796]
Transform136.scale = [0.1,0.1,0.1]
Shape137 = x3d.Shape()
Appearance138 = x3d.Appearance()
Material139 = x3d.Material()
Material139.USE = "Pants_Color"

Appearance138.material = Material139
ImageTexture140 = x3d.ImageTexture()
ImageTexture140.USE = "camo"

Appearance138.texture = ImageTexture140

Shape137.appearance = Appearance138
IndexedFaceSet141 = x3d.IndexedFaceSet()
IndexedFaceSet141.coordIndex = [4,5,2,-1,19,13,20,-1,20,13,12,-1,14,21,9,-1,22,23,24,-1,4,0,28,-1,29,15,6,-1,30,6,16,-1,30,29,6,-1,18,17,31,-1,11,27,26,-1,27,10,3,-1,33,34,23,-1,22,33,23,-1,35,36,37,-1,38,39,40,-1,38,18,39,-1,18,31,41,-1,42,13,19,-1,43,44,19,-1,9,45,46,-1,23,47,24,-1,29,30,48,-1,16,49,30,-1,50,51,52,-1,51,50,53,-1,35,37,54,-1,36,55,56,-1,36,35,55,-1,57,55,35,-1,39,57,40,-1,39,58,55,-1,59,41,60,-1,3,2,5,-1,61,22,24,-1,34,62,23,-1,48,63,62,-1,16,8,49,-1,7,25,52,-1,7,52,64,-1,65,64,51,-1,53,37,36,-1,50,37,53,-1,56,55,58,-1,66,56,58,-1,41,27,60,-1,39,18,41,-1,31,26,27,-1,59,60,67,-1,4,68,5,-1,69,68,4,-1,32,44,28,-1,43,19,20,-1,61,21,14,-1,47,70,21,-1,47,23,70,-1,62,63,23,-1,8,71,49,-1,57,39,55,-1,72,43,20,-1,22,61,14,-1,61,24,47,-1,63,73,23,-1,29,48,62,-1,52,51,64,-1,74,66,58,-1,58,59,67,-1,1,46,20,-1,75,70,76,-1,61,47,21,-1,70,73,77,-1,8,7,71,-1,71,7,64,-1,65,51,78,-1,51,79,78,-1,49,71,80,-1,81,51,53,-1,74,82,66,-1,66,83,56,-1,59,58,39,-1,9,21,45,-1,49,80,84,-1,85,86,74,-1,60,27,3,-1,69,4,28,-1,43,72,87,-1,88,89,75,-1,90,63,91,-1,78,84,80,-1,65,78,80,-1,51,81,79,-1,92,79,81,-1,93,92,81,-1,94,84,78,-1,94,78,79,-1,94,95,96,-1,94,92,95,-1,94,79,92,-1,92,93,95,-1,93,74,86,-1,97,60,3,-1,98,99,100,-1,45,21,70,-1,101,77,90,-1,23,73,70,-1,84,102,49,-1,95,93,86,-1,97,68,103,-1,68,3,5,-1,1,9,46,-1,104,98,89,-1,75,89,100,-1,75,45,70,-1,84,105,102,-1,106,323,107,-1,39,41,59,-1,58,67,108,-1,68,97,3,-1,100,99,46,-1,76,77,101,-1,63,48,91,-1,49,102,109,-1,110,98,104,-1,87,111,112,-1,104,89,112,-1,77,73,90,-1,113,102,105,-1,113,105,106,-1,106,107,113,-1,68,69,103,-1,46,99,20,-1,114,86,115,-1,115,85,116,-1,69,28,43,-1,99,72,20,-1,72,111,87,-1,117,112,89,-1,88,118,119,-1,45,100,46,-1,120,101,90,-1,109,48,30,-1,113,107,121,-1,113,121,122,-1,115,121,107,-1,122,121,123,-1,121,115,123,-1,123,115,116,-1,115,86,85,-1,28,44,43,-1,98,100,89,-1,117,89,88,-1,118,124,125,-1,88,75,76,-1,45,75,100,-1,73,63,90,-1,126,90,91,-1,91,127,128,-1,127,129,128,-1,49,109,30,-1,127,122,130,-1,130,122,123,-1,131,108,132,-1,133,131,134,-1,85,74,58,-1,131,133,108,-1,133,135,116,-1,111,104,112,-1,76,101,124,-1,136,126,91,-1,137,116,135,-1,133,116,85,-1,138,139,140,-1,141,87,112,-1,142,69,87,-1,70,77,76,-1,120,90,126,-1,101,120,124,-1,48,109,91,-1,102,143,109,-1,109,143,127,-1,144,135,145,-1,134,145,133,-1,108,85,58,-1,133,85,108,-1,41,31,27,-1,67,60,97,-1,143,122,127,-1,146,130,324,-1,146,127,130,-1,145,135,133,-1,67,140,147,-1,141,112,117,-1,120,148,125,-1,149,150,128,-1,151,134,152,-1,152,131,153,-1,103,67,97,-1,87,69,43,-1,126,148,120,-1,91,109,127,-1,154,129,146,-1,154,146,153,-1,129,149,128,-1,129,127,146,-1,147,155,132,-1,156,157,103,-1,156,103,69,-1,119,158,141,-1,120,125,124,-1,126,136,148,-1,136,150,159,-1,146,152,153,-1,142,156,69,-1,125,160,161,-1,160,136,159,-1,131,152,134,-1,147,132,108,-1,132,162,163,-1,138,140,67,-1,156,164,157,-1,165,118,125,-1,125,148,160,-1,160,166,161,-1,136,128,150,-1,162,167,163,-1,139,168,169,-1,142,170,156,-1,141,142,87,-1,88,119,117,-1,91,128,136,-1,159,150,171,-1,163,172,153,-1,163,153,131,-1,131,132,163,-1,140,155,147,-1,117,119,141,-1,148,136,160,-1,154,171,149,-1,172,173,154,-1,167,172,163,-1,174,175,162,-1,138,67,157,-1,170,164,156,-1,118,76,124,-1,160,159,176,-1,171,177,178,-1,154,173,171,-1,172,154,153,-1,179,162,180,-1,67,147,108,-1,138,157,164,-1,119,118,158,-1,165,161,181,-1,165,125,161,-1,165,181,182,-1,171,150,149,-1,183,167,184,-1,162,184,167,-1,159,185,176,-1,171,173,186,-1,187,184,188,-1,188,162,179,-1,188,179,189,-1,162,175,180,-1,139,138,168,-1,190,170,142,-1,171,186,189,-1,186,188,189,-1,178,159,171,-1,191,189,179,-1,191,177,189,-1,171,189,177,-1,132,174,162,-1,175,174,192,-1,139,169,193,-1,178,185,159,-1,160,176,166,-1,191,194,177,-1,191,179,195,-1,188,184,162,-1,140,139,155,-1,103,157,67,-1,164,170,168,-1,190,141,158,-1,196,158,118,-1,194,191,195,-1,180,197,198,-1,174,193,192,-1,170,199,200,-1,190,158,201,-1,202,176,185,-1,203,185,178,-1,203,204,202,-1,205,204,195,-1,204,203,195,-1,175,192,206,-1,174,155,193,-1,161,207,181,-1,208,195,198,-1,195,179,198,-1,169,200,209,-1,202,185,203,-1,208,205,195,-1,205,208,210,-1,198,179,180,-1,211,212,197,-1,166,207,161,-1,213,176,202,-1,202,204,213,-1,210,214,205,-1,210,208,212,-1,207,215,181,-1,176,216,166,-1,212,217,197,-1,211,197,180,-1,174,132,155,-1,139,193,155,-1,138,164,168,-1,182,218,165,-1,219,214,210,-1,219,212,211,-1,141,190,142,-1,170,200,168,-1,190,199,170,-1,216,220,166,-1,213,214,216,-1,221,222,223,-1,222,219,211,-1,219,210,212,-1,180,175,211,-1,201,224,225,-1,226,227,228,-1,196,201,158,-1,201,196,226,-1,220,215,207,-1,176,213,216,-1,220,216,219,-1,175,206,211,-1,193,229,192,-1,169,168,200,-1,196,118,165,-1,230,231,232,-1,118,88,76,-1,231,220,221,-1,166,220,207,-1,220,219,221,-1,225,233,234,-1,235,224,236,-1,231,215,220,-1,199,234,200,-1,201,226,224,-1,237,192,229,-1,218,196,165,-1,222,211,238,-1,190,201,225,-1,239,240,206,-1,229,193,169,-1,199,225,234,-1,224,241,225,-1,226,218,227,-1,226,196,218,-1,218,182,227,-1,230,242,243,-1,230,181,215,-1,221,219,222,-1,231,221,244,-1,182,243,227,-1,216,214,219,-1,192,237,206,-1,182,181,230,-1,245,223,246,-1,232,231,244,-1,209,229,169,-1,209,247,229,-1,200,234,209,-1,233,225,241,-1,230,232,242,-1,230,215,231,-1,232,244,248,-1,223,222,246,-1,249,239,229,-1,234,247,209,-1,235,250,251,-1,235,236,250,-1,243,182,230,-1,206,238,211,-1,226,228,252,-1,228,253,254,-1,190,225,199,-1,255,256,242,-1,244,255,248,-1,223,245,257,-1,234,233,247,-1,224,226,252,-1,232,248,242,-1,258,229,247,-1,223,244,221,-1,222,238,246,-1,259,260,240,-1,238,240,246,-1,240,239,261,-1,256,255,257,-1,260,246,240,-1,238,206,240,-1,239,237,229,-1,235,233,241,-1,239,206,237,-1,243,262,263,-1,249,229,264,-1,258,264,229,-1,258,251,264,-1,235,258,247,-1,242,262,243,-1,265,266,267,-1,268,245,267,-1,249,269,261,-1,268,256,257,-1,260,270,245,-1,243,263,227,-1,228,263,253,-1,255,242,248,-1,251,271,264,-1,233,235,247,-1,228,254,272,-1,268,267,262,-1,223,257,255,-1,273,274,271,-1,275,276,252,-1,256,268,262,-1,223,255,244,-1,259,240,261,-1,261,269,277,-1,278,249,264,-1,279,280,236,-1,280,250,236,-1,236,224,252,-1,261,277,259,-1,264,271,278,-1,274,278,271,-1,235,251,258,-1,273,271,281,-1,276,236,252,-1,262,282,283,-1,260,245,246,-1,274,284,278,-1,235,241,224,-1,228,227,263,-1,284,274,285,-1,273,285,274,-1,279,236,276,-1,286,287,276,-1,272,252,228,-1,268,257,245,-1,288,266,265,-1,284,249,278,-1,285,273,289,-1,250,280,251,-1,290,281,291,-1,292,253,262,-1,242,256,262,-1,293,294,270,-1,260,293,270,-1,269,284,285,-1,269,285,289,-1,269,289,290,-1,291,280,279,-1,271,251,281,-1,292,262,283,-1,265,267,270,-1,265,294,295,-1,281,280,291,-1,294,265,270,-1,296,259,297,-1,273,281,289,-1,282,267,266,-1,293,298,294,-1,249,284,269,-1,299,254,253,-1,253,263,262,-1,239,249,261,-1,290,289,281,-1,262,267,282,-1,302,288,295,-1,260,259,293,-1,296,298,293,-1,280,281,251,-1,275,252,303,-1,298,304,295,-1,296,297,301,-1,305,272,254,-1,299,306,254,-1,307,253,292,-1,288,265,295,-1,288,308,266,-1,277,269,290,-1,300,310,311,-1,277,297,259,-1,286,276,275,-1,299,309,312,-1,307,299,253,-1,313,314,302,-1,304,302,295,-1,311,304,300,-1,311,302,304,-1,302,311,313,-1,311,315,313,-1,302,308,288,-1,296,293,259,-1,308,316,266,-1,316,317,318,-1,302,314,308,-1,298,295,294,-1,317,319,315,-1,316,319,317,-1,314,313,308,-1,313,319,308,-1,287,279,276,-1,267,245,270,-1,316,308,319,-1,317,315,318,-1,313,315,319,-1,305,303,252,-1,299,312,306,-1,320,316,318,-1,282,321,283,-1,322,282,316,-1,287,291,279,-1,305,252,272,-1,316,282,266,-1,306,305,254,-1]
IndexedFaceSet141.creaseAngle = 1.57
Coordinate142 = x3d.Coordinate()

IndexedFaceSet141.coord = Coordinate142

Shape137.geometry = IndexedFaceSet141

Transform136.children.append(Shape137)

fieldValue135.children.append(Transform136)

ProtoInstance133.fieldValue.append(fieldValue135)

fieldValue132.children.append(ProtoInstance133)
ProtoInstance143 = x3d.ProtoInstance()
ProtoInstance143.name = "Joint"
ProtoInstance143.DEF = "hanim_l_ankle"
fieldValue144 = x3d.fieldValue()
fieldValue144.name = "name"
fieldValue144.value = "l_ankle"

ProtoInstance143.fieldValue.append(fieldValue144)
fieldValue145 = x3d.fieldValue()
fieldValue145.name = "center"
fieldValue145.value = "0.0645 0.0719 -0.048"

ProtoInstance143.fieldValue.append(fieldValue145)
fieldValue146 = x3d.fieldValue()
fieldValue146.name = "children"
ProtoInstance147 = x3d.ProtoInstance()
ProtoInstance147.name = "Segment"
ProtoInstance147.DEF = "hanim_l_hindfoot"
fieldValue148 = x3d.fieldValue()
fieldValue148.name = "name"
fieldValue148.value = "l_hindfoot"

ProtoInstance147.fieldValue.append(fieldValue148)
fieldValue149 = x3d.fieldValue()
fieldValue149.name = "children"
Transform150 = x3d.Transform()
Transform150.DEF = "l_foot_adjust"
Transform150.center = [-0.32,1.1,0.021]
Transform150.rotation = [0,1,0,1.570796]
Transform150.scale = [0.1,0.1,0.1]
Shape151 = x3d.Shape()
Appearance152 = x3d.Appearance()
Material153 = x3d.Material()
Material153.DEF = "Shoe_Color"
Material153.ambientIntensity = 0.25

Appearance152.material = Material153

Shape151.appearance = Appearance152
IndexedFaceSet154 = x3d.IndexedFaceSet()
IndexedFaceSet154.coordIndex = [0,1,2,-1,3,4,5,-1,6,7,8,-1,9,10,11,-1,12,13,14,-1,15,16,17,-1,18,19,20,-1,21,22,23,-1,24,25,26,-1,27,28,29,-1,30,31,32,-1,33,34,35,-1,36,37,38,-1,39,40,41,-1,42,43,44,-1,45,46,47,-1,48,49,50,-1,51,52,53,-1,54,55,56,-1,57,58,59,-1,60,61,62,-1,63,64,65,-1,66,67,68,-1,69,70,71,-1,72,73,74,-1,75,76,77,-1,78,79,80,-1,81,82,83,-1,84,85,86,-1,87,88,89,-1,90,91,92,-1,93,94,95,-1,96,97,98,-1,99,100,101,-1,102,103,104,-1,105,106,107,-1,108,109,110,-1,111,112,113,-1,114,115,116,-1,117,118,119,-1,120,121,122,-1,123,124,125,-1,126,127,128,-1,129,130,131,-1,132,133,134,-1,135,136,137,-1,138,139,140,-1,141,142,143,-1,144,145,146,-1,147,148,149,-1,150,151,152,-1,153,154,155,-1,156,157,158,-1,159,160,161,-1,162,163,164,-1,165,166,167,-1,168,169,170,-1,171,172,173,-1,174,175,176,-1,177,178,179,-1,180,181,182,-1,183,184,185,-1,186,187,188,-1,189,190,191,-1,192,193,194,-1,195,196,197,-1,198,199,200,-1,201,202,203,-1,204,205,206,-1,207,208,209,-1,210,211,212,-1,213,214,215,-1,216,217,218,-1,219,220,221,-1,222,223,224,-1,225,226,227,-1,228,229,230,-1,231,232,233,-1,234,235,236,-1,237,238,239,-1,240,241,242,-1,243,244,245,-1,246,247,248,-1,249,250,251,-1,252,253,254,-1,255,256,257,-1,258,259,260,-1,261,262,263,-1,264,265,266,-1,267,268,269,-1,270,271,272,-1,273,274,275,-1,276,277,278,-1,279,280,281,-1,282,283,284,-1,285,286,287,-1,288,289,290,-1,291,292,293,-1,294,295,296,-1,297,298,299,-1,300,301,302,-1,303,304,305,-1,306,307,308,-1,309,310,311,-1,312,313,314,-1,315,316,317,-1,318,319,320,-1,321,322,323,-1,324,325,326,-1,327,328,329,-1,330,331,332,-1,333,334,335,-1,336,337,338,-1,339,340,341,-1,342,343,344,-1,345,346,347,-1,348,349,350,-1,351,352,353,-1,354,355,356,-1,357,358,359,-1,360,361,362,-1,363,364,365,-1,366,367,368,-1,369,370,371,-1,372,373,374,-1,375,376,377,-1,378,379,380,-1,381,382,383,-1,384,385,386,-1,387,388,389,-1,390,391,392,-1,393,394,395,-1,396,397,398,-1,399,400,401,-1,402,403,404,-1,405,406,407,-1,408,409,410,-1,411,412,413,-1,414,415,416,-1,417,418,419,-1,420,421,422,-1,423,424,425,-1,426,427,428,-1,429,430,431,-1,432,433,434,-1,435,436,437,-1,438,439,440,-1,441,442,443,-1,444,445,446,-1,447,448,449,-1,450,451,452,-1,453,454,455,-1,456,457,458,-1,459,460,461,-1,462,463,464,-1,465,466,467,-1,468,469,470,-1,471,472,473,-1,474,475,476,-1,477,478,479,-1,480,481,482,-1,483,484,485,-1,486,487,488,-1,489,490,491,-1,492,493,494,-1,495,496,497,-1,498,499,500,-1,501,502,503,-1,504,505,506,-1,507,508,509,-1,510,511,512,-1,513,514,515,-1,516,517,518,-1,519,520,521,-1,522,523,524,-1,525,526,527,-1,528,529,530,-1,531,532,533,-1,534,535,536,-1,537,538,539,-1,540,541,542,-1,543,544,545,-1,546,547,548,-1,549,550,551,-1,552,553,554,-1,555,556,557,-1,558,559,560,-1,561,562,563,-1,564,565,566,-1,567,568,569,-1,570,571,572,-1,573,574,575,-1,576,577,578,-1,579,580,581,-1,582,583,584,-1,585,586,587,-1,588,589,590,-1,591,592,593,-1,594,595,596,-1,597,598,599,-1,600,601,602,-1,603,604,605,-1,606,607,608,-1,609,610,611,-1,612,613,614,-1,615,616,617,-1,618,619,620,-1,621,622,623,-1,624,625,626,-1,627,628,629,-1,630,631,632,-1,633,634,635,-1,636,637,638,-1,639,640,641,-1,642,643,644,-1,645,646,647,-1,648,649,650,-1,651,652,653,-1,654,655,656,-1,657,658,659,-1,660,661,662,-1,663,664,665,-1,666,667,668,-1,669,670,671,-1,672,673,674,-1,675,676,677,-1,678,679,680,-1,681,682,683,-1,684,685,686,-1,687,688,689,-1,690,691,692,-1,693,694,695,-1,696,697,698,-1,699,700,701,-1,702,703,704,-1,705,706,707,-1,708,709,710,-1,711,712,713,-1,714,715,716,-1,717,718,719,-1,720,721,722,-1,723,724,725,-1,726,727,728,-1,729,730,731,-1,732,733,734,-1,735,736,737,-1,738,739,740,-1,741,742,743,-1,744,745,746,-1,747,748,749,-1,750,751,752,-1,753,754,755,-1,756,757,758,-1,759,760,761,-1,762,763,764,-1,765,766,767,-1,768,769,770,-1,771,772,773,-1,774,775,776,-1,777,778,779,-1,780,781,782,-1,783,784,785,-1,786,787,788,-1,789,790,791,-1,792,793,794,-1,795,796,797,-1,798,799,800,-1,801,802,803,-1,804,805,806,-1,807,808,809,-1,810,811,812,-1,813,814,815,-1,816,817,818,-1,819,820,821,-1,822,823,824,-1,825,826,827,-1,828,829,830,-1,831,832,833,-1,834,835,836,-1,837,838,839,-1,840,841,842,-1,843,844,845,-1,846,847,848,-1,849,850,851,-1,852,853,854,-1,855,856,857,-1,858,859,860,-1,861,862,863,-1,864,865,866,-1,867,868,869,-1,870,871,872,-1,873,874,875,-1,876,877,878,-1,879,880,881,-1,882,883,884,-1,885,886,887,-1,888,889,890,-1,891,892,893,-1,894,895,896,-1,897,898,899,-1,900,901,902,-1,903,904,905,-1,906,907,908,-1,909,910,911,-1,912,913,914,-1,915,916,917,-1,918,919,920,-1,921,922,923,-1,924,925,926,-1,927,928,929,-1,930,931,932,-1,933,934,935,-1,936,937,938,-1,939,940,941,-1,942,943,944,-1,945,946,947,-1,948,949,950,-1,951,952,953,-1,954,955,956,-1,957,958,959,-1,960,961,962,-1,963,964,965,-1,966,967,968,-1,969,970,971,-1,972,973,974,-1,975,976,977,-1,978,979,980,-1,981,982,983,-1,984,985,986,-1,987,988,989,-1,990,991,992,-1,993,994,995,-1,996,997,998,-1,999,1000,1001,-1,1002,1003,1004,-1,1005,1006,1007,-1,1008,1009,1010,-1,1011,1012,1013,-1,1014,1015,1016,-1,1017,1018,1019,-1,1020,1021,1022,-1,1023,1024,1025,-1,1026,1027,1028,-1,1029,1030,1031,-1,1032,1033,1034,-1,1035,1036,1037,-1,1038,1039,1040,-1,1041,1042,1043,-1,1044,1045,1046,-1,1047,1048,1049,-1,1050,1051,1052,-1,1053,1054,1055,-1,1056,1057,1058,-1,1059,1060,1061,-1,1062,1063,1064,-1,1065,1066,1067,-1,1068,1069,1070,-1,1071,1072,1073,-1,1074,1075,1076,-1,1077,1078,1079,-1,1080,1081,1082,-1,1083,1084,1085,-1,1086,1087,1088,-1,1089,1090,1091,-1,1092,1093,1094,-1,1095,1096,1097,-1,1098,1099,1100,-1,1101,1102,1103,-1,1104,1105,1106,-1,1107,1108,1109,-1,1110,1111,1112,-1,1113,1114,1115,-1,1116,1117,1118,-1,1119,1120,1121,-1,1122,1123,1124,-1,1125,1126,1127,-1,1128,1129,1130,-1,1131,1132,1133,-1,1134,1135,1136,-1,1137,1138,1139,-1,1140,1141,1142,-1,1143,1144,1145,-1,1146,1147,1148,-1,1149,1150,1151,-1,1152,1153,1154,-1,1155,1156,1157,-1,1158,1159,1160,-1,1161,1162,1163,-1,1164,1165,1166,-1,1167,1168,1169,-1,1170,1171,1172,-1,1173,1174,1175,-1,1176,1177,1178,-1,1179,1180,1181,-1,1182,1183,1184,-1,1185,1186,1187,-1,1188,1189,1190,-1,1191,1192,1193,-1,1194,1195,1196,-1,1197,1198,1199,-1,1200,1201,1202,-1,1203,1204,1205,-1,1206,1207,1208,-1,1209,1210,1211,-1,1212,1213,1214,-1,1215,1216,1217,-1,1218,1219,1220,-1,1221,1222,1223,-1,1224,1225,1226,-1,1227,1228,1229,-1,1230,1231,1232,-1,1233,1234,1235,-1,1236,1237,1238,-1,1239,1240,1241,-1,1242,1243,1244,-1,1245,1246,1247,-1,1248,1249,1250,-1,1251,1252,1253,-1,1254,1255,1256,-1,1257,1258,1259,-1,1260,1261,1262,-1,1263,1264,1265,-1,1266,1267,1268,-1,1269,1270,1271,-1,1272,1273,1274,-1,1275,1276,1277,-1,1278,1279,1280,-1,1281,1282,1283,-1,1284,1285,1286,-1,1287,1288,1289,-1,1290,1291,1292,-1,1293,1294,1295,-1,1296,1297,1298,-1,1299,1300,1301,-1,1302,1303,1304,-1,1305,1306,1307,-1,1308,1309,1310,-1,1311,1312,1313,-1,1314,1315,1316,-1,1317,1318,1319,-1,1320,1321,1322,-1,1323,1324,1325,-1,1326,1327,1328,-1,1329,1330,1331,-1,1332,1333,1334,-1,1335,1336,1337,-1,1338,1339,1340,-1,1341,1342,1343,-1,1344,1345,1346,-1,1347,1348,1349,-1,1350,1351,1352,-1,1353,1354,1355,-1,1356,1357,1358,-1,1359,1360,1361,-1,1362,1363,1364,-1,1365,1366,1367,-1,1368,1369,1370,-1,1371,1372,1373,-1,1374,1375,1376,-1,1377,1378,1379,-1,1380,1381,1382,-1,1383,1384,1385,-1,1386,1387,1388,-1,1389,1390,1391,-1,1392,1393,1394,-1,1395,1396,1397,-1,1398,1399,1400,-1,1401,1402,1403,-1,1404,1405,1406,-1,1407,1408,1409,-1,1410,1411,1412,-1,1413,1414,1415,-1,1416,1417,1418,-1,1419,1420,1421,-1,1422,1423,1424,-1,1425,1426,1427,-1,1428,1429,1430,-1,1431,1432,1433,-1,1434,1435,1436,-1,1437,1438,1439,-1,1440,1441,1442,-1,1443,1444,1445,-1,1446,1447,1448,-1,1449,1450,1451,-1,1452,1453,1454,-1,1455,1456,1457,-1,1458,1459,1460,-1,1461,1462,1463,-1,1464,1465,1466,-1,1467,1468,1469,-1,1470,1471,1472,-1,1473,1474,1475,-1,1476,1477,1478,-1,1479,1480,1481,-1,1482,1483,1484,-1,1485,1486,1487,-1,1488,1489,1490,-1,1491,1492,1493,-1,1494,1495,1496,-1,1497,1498,1499,-1,1500,1501,1502,-1,1503,1504,1505,-1,1506,1507,1508,-1,1509,1510,1511,-1,1512,1513,1514,-1,1515,1516,1517,-1,1518,1519,1520,-1,1521,1522,1523,-1,1524,1525,1526,-1,1527,1528,1529,-1,1530,1531,1532,-1,1533,1534,1535,-1,1536,1537,1538,-1,1539,1540,1541,-1,1542,1543,1544,-1,1545,1546,1547,-1,1548,1549,1550,-1,1551,1552,1553,-1,1554,1555,1556,-1,1557,1558,1559,-1,1560,1561,1562,-1,1563,1564,1565,-1,1566,1567,1568,-1,1569,1570,1571,-1,1572,1573,1574,-1,1575,1576,1577,-1,1578,1579,1580,-1,1581,1582,1583,-1,1584,1585,1586,-1,1587,1588,1589,-1,1590,1591,1592,-1,1593,1594,1595,-1,1596,1597,1598,-1,1599,1600,1601,-1,1602,1603,1604,-1,1605,1606,1607,-1,1608,1609,1610,-1,1611,1612,1613,-1,1614,1615,1616,-1,1617,1618,1619,-1,1620,1621,1622,-1,1623,1624,1625,-1,1626,1627,1628,-1,1629,1630,1631,-1,1632,1633,1634,-1,1635,1636,1637,-1,1638,1639,1640,-1,1641,1642,1643,-1,1644,1645,1646,-1,1647,1648,1649,-1,1650,1651,1652,-1,1653,1654,1655,-1,1656,1657,1658,-1,1659,1660,1661,-1,1662,1663,1664,-1,1665,1666,1667,-1,1668,1669,1670,-1,1671,1672,1673,-1,1674,1675,1676,-1,1677,1678,1679,-1,1680,1681,1682,-1,1683,1684,1685,-1,1686,1687,1688,-1,1689,1690,1691,-1,1692,1693,1694,-1,1695,1696,1697,-1,1698,1699,1700,-1,1701,1702,1703,-1,1704,1705,1706,-1,1707,1708,1709,-1,1710,1711,1712,-1,1713,1714,1715,-1,1716,1717,1718,-1,1719,1720,1721,-1,1722,1723,1724,-1,1725,1726,1727,-1,1728,1729,1730,-1,1731,1732,1733,-1,1734,1735,1736,-1,1737,1738,1739,-1,1740,1741,1742,-1,1743,1744,1745,-1,1746,1747,1748,-1,1749,1750,1751,-1,1752,1753,1754,-1,1755,1756,1757,-1,1758,1759,1760,-1,1761,1762,1763,-1,1764,1765,1766,-1,1767,1768,1769,-1,1770,1771,1772,-1,1773,1774,1775,-1,1776,1777,1778,-1,1779,1780,1781,-1,1782,1783,1784,-1,1785,1786,1787,-1,1788,1789,1790,-1,1791,1792,1793,-1,1794,1795,1796,-1,1797,1798,1799,-1,1800,1801,1802,-1,1803,1804,1805,-1,1806,1807,1808,-1,1809,1810,1811,-1,1812,1813,1814,-1,1815,1816,1817,-1,1818,1819,1820,-1,1821,1822,1823,-1,1824,1825,1826,-1,1827,1828,1829,-1,1830,1831,1832,-1,1833,1834,1835,-1,1836,1837,1838,-1,1839,1840,1841,-1,1842,1843,1844,-1,1845,1846,1847,-1,1848,1849,1850,-1,1851,1852,1853,-1,1854,1855,1856,-1,1857,1858,1859,-1,1860,1861,1862,-1,1863,1864,1865,-1,1866,1867,1868,-1,1869,1870,1871,-1,1872,1873,1874,-1,1875,1876,1877,-1,1878,1879,1880,-1,1881,1882,1883,-1,1884,1885,1886,-1,1887,1888,1889,-1,1890,1891,1892,-1,1893,1894,1895,-1,1896,1897,1898,-1,1899,1900,1901,-1,1902,1903,1904,-1,1905,1906,1907,-1,1908,1909,1910,-1,1911,1912,1913,-1,1914,1915,1916,-1,1917,1918,1919,-1,1920,1921,1922,-1,1923,1924,1925,-1,1926,1927,1928,-1,1929,1930,1931,-1,1932,1933,1934,-1,1935,1936,1937,-1,1938,1939,1940,-1,1941,1942,1943,-1,1944,1945,1946,-1,1947,1948,1949,-1]
IndexedFaceSet154.creaseAngle = 1.57
Coordinate155 = x3d.Coordinate()

IndexedFaceSet154.coord = Coordinate155

Shape151.geometry = IndexedFaceSet154

Transform150.children.append(Shape151)

fieldValue149.children.append(Transform150)

ProtoInstance147.fieldValue.append(fieldValue149)

fieldValue146.children.append(ProtoInstance147)

ProtoInstance143.fieldValue.append(fieldValue146)

fieldValue132.children.append(ProtoInstance143)

ProtoInstance129.fieldValue.append(fieldValue132)

fieldValue118.children.append(ProtoInstance129)

ProtoInstance115.fieldValue.append(fieldValue118)

fieldValue104.children.append(ProtoInstance115)
ProtoInstance156 = x3d.ProtoInstance()
ProtoInstance156.name = "Joint"
ProtoInstance156.DEF = "hanim_r_hip"
fieldValue157 = x3d.fieldValue()
fieldValue157.name = "name"
fieldValue157.value = "r_hip"

ProtoInstance156.fieldValue.append(fieldValue157)
fieldValue158 = x3d.fieldValue()
fieldValue158.name = "center"
fieldValue158.value = "-0.11 0.892362 -0.0732533"

ProtoInstance156.fieldValue.append(fieldValue158)
fieldValue159 = x3d.fieldValue()
fieldValue159.name = "children"
ProtoInstance160 = x3d.ProtoInstance()
ProtoInstance160.name = "Segment"
ProtoInstance160.DEF = "hanim_r_thigh"
fieldValue161 = x3d.fieldValue()
fieldValue161.name = "name"
fieldValue161.value = "r_thigh"

ProtoInstance160.fieldValue.append(fieldValue161)
fieldValue162 = x3d.fieldValue()
fieldValue162.name = "children"
Transform163 = x3d.Transform()
Transform163.DEF = "r_thigh_adjust"
Transform163.center = [0.43,1.1,-0.05]
Transform163.rotation = [0,1,0,1.570796]
Transform163.scale = [0.1,0.1,0.1]
Shape164 = x3d.Shape()
Appearance165 = x3d.Appearance()
Material166 = x3d.Material()
Material166.USE = "Pants_Color"

Appearance165.material = Material166
ImageTexture167 = x3d.ImageTexture()
ImageTexture167.USE = "camo"

Appearance165.texture = ImageTexture167

Shape164.appearance = Appearance165
IndexedFaceSet168 = x3d.IndexedFaceSet()
IndexedFaceSet168.coordIndex = [0,1,2,-1,3,4,5,-1,6,7,8,-1,9,10,11,-1,12,13,14,-1,15,16,17,-1,18,19,20,-1,21,22,23,-1,24,25,26,-1,27,28,29,-1,30,31,32,-1,33,34,35,-1,36,37,38,-1,39,40,41,-1,42,43,44,-1,45,46,47,-1,48,49,50,-1,51,52,53,-1,54,55,56,-1,57,58,59,-1,60,61,62,-1,63,64,65,-1,66,67,68,-1,69,70,71,-1,72,73,74,-1,75,76,77,-1,78,79,80,-1,81,82,83,-1,84,85,86,-1,87,88,89,-1,90,91,92,-1,93,94,95,-1,96,97,98,-1,99,100,101,-1,102,103,104,-1,105,106,107,-1,108,109,110,-1,111,112,113,-1,114,115,116,-1,117,118,119,-1,120,121,122,-1,123,124,125,-1,126,127,128,-1,129,130,131,-1,132,133,134,-1,135,136,137,-1,138,139,140,-1,141,142,143,-1,144,145,146,-1,147,148,149,-1,150,151,152,-1,153,154,155,-1,156,157,158,-1,159,160,161,-1,162,163,164,-1,165,166,167,-1,168,169,170,-1,171,172,173,-1,174,175,176,-1,177,178,179,-1,180,181,182,-1,183,184,185,-1,186,187,188,-1,189,190,191,-1,192,193,194,-1,195,196,197,-1,198,199,200,-1,201,202,203,-1,204,205,206,-1,207,208,209,-1,210,211,212,-1,213,214,215,-1,216,217,218,-1,219,220,221,-1,222,223,224,-1,225,226,227,-1,228,229,230,-1,231,232,233,-1,234,235,236,-1,237,238,239,-1,240,241,242,-1,243,244,245,-1,246,247,248,-1,217,220,218,-1,222,226,223,-1,195,198,196,-1,198,200,196,-1,249,202,200,-1,200,202,196,-1,201,205,202,-1,218,220,214,-1,219,223,220,-1,202,205,196,-1,220,223,214,-1,215,214,212,-1,212,214,210,-1,214,223,210,-1,223,226,210,-1,204,208,205,-1,207,210,208,-1,210,226,208,-1,205,208,196,-1,208,226,196,-1,250,251,252,-1,253,254,255,-1,256,257,258,-1,259,260,261,-1,262,263,264,-1,265,266,267,-1,268,269,270,-1,271,272,273,-1,274,275,276,-1,277,278,279,-1,280,281,282,-1,283,284,285,-1,286,287,288,-1,289,290,291,-1,292,293,294,-1,295,296,297,-1,298,299,300,-1,301,302,303,-1,304,305,306,-1,307,308,309,-1,310,311,312,-1,313,314,315,-1,316,317,318,-1,319,320,321,-1,322,323,324,-1,325,326,327,-1,328,329,330,-1,331,332,333,-1,334,335,336,-1,337,338,339,-1,340,341,342,-1,343,344,345,-1,346,347,348,-1,349,350,351,-1,352,353,354,-1,355,356,357,-1,358,359,360,-1,361,362,363,-1,364,365,366,-1,367,368,369,-1,370,371,372,-1,373,374,375,-1,376,377,378,-1,379,380,381,-1,382,383,384,-1,383,382,384,-1,385,386,387,-1,388,389,390,-1,391,392,393,-1,394,395,396,-1,397,398,399,-1,400,401,402,-1,403,404,405,-1,406,407,408,-1,407,406,408,-1,409,410,411,-1,409,411,410,-1,412,413,414,-1,415,416,417,-1,418,419,420,-1,421,422,423,-1,424,425,426,-1,427,428,429,-1,428,427,429,-1,430,431,432,-1,433,434,435,-1,436,437,438,-1,439,440,441,-1,442,443,444,-1,445,446,447,-1,448,449,450,-1,451,452,453,-1,454,455,456,-1,455,454,456,-1,457,458,459,-1,460,461,462,-1,463,464,465,-1,466,467,468,-1,469,470,471,-1,472,473,474,-1,475,476,477,-1,478,479,480,-1,481,482,483,-1,484,485,486,-1,487,488,489,-1,490,491,492,-1,493,494,495,-1,496,497,498,-1,498,497,496,-1,499,500,501,-1,502,503,504,-1,505,506,507,-1,508,509,510,-1,511,512,513,-1,514,515,516,-1,517,518,519,-1,520,521,522,-1,523,524,525,-1,526,527,528,-1,529,530,531,-1,532,533,534,-1,533,532,534,-1,535,536,537,-1,538,539,540,-1,538,540,539,-1,541,542,543,-1,544,545,546,-1,547,548,549,-1,550,551,552,-1,553,554,555,-1,556,557,558,-1,559,560,561,-1,562,563,564,-1,565,566,567,-1,566,565,567,-1,568,569,570,-1,571,572,573,-1,574,575,576,-1,577,578,579,-1,580,581,582,-1,583,584,585,-1,586,587,588,-1,589,590,591,-1,590,589,591,-1,592,593,594,-1,595,596,597,-1,598,599,600,-1,601,602,603,-1,604,605,606,-1,607,608,609,-1,607,609,608,-1,610,611,612,-1,613,614,615,-1,613,615,614,-1,616,617,618,-1,619,620,621,-1,622,623,624,-1,625,626,627,-1,628,629,630,-1,631,632,633,-1,632,631,633,-1,634,635,636,-1,634,636,635,-1,637,638,639,-1,639,638,637,-1,640,641,642,-1,643,644,645,-1,646,647,648,-1,649,650,651,-1,652,653,654,-1,655,656,657,-1,656,655,657,-1,658,659,660,-1,660,659,658,-1,661,662,663,-1,664,665,666,-1,666,665,664,-1,667,668,669,-1,670,671,672,-1,673,674,675,-1,676,677,678,-1,679,680,681,-1,680,679,681,-1,682,683,684,-1,685,686,687,-1,688,689,690,-1,691,692,693,-1,694,695,696,-1,697,698,699,-1,700,701,702,-1,703,704,705,-1,706,707,708,-1,707,706,708,-1,709,710,711,-1,710,709,711,-1,712,713,714,-1,715,716,717,-1,718,719,720,-1,721,722,723,-1,724,725,726,-1,727,728,729,-1,728,727,729,-1,730,731,732,-1,733,734,735,-1,736,737,738,-1,739,740,741,-1,742,743,744,-1,745,746,747,-1,748,749,750,-1,751,752,753,-1,754,755,756,-1,757,758,759,-1,760,761,762,-1,763,764,765,-1,766,767,768,-1,769,770,771,-1,772,773,774,-1,775,776,777,-1,778,779,780,-1,781,782,783,-1,784,785,786,-1,787,788,789,-1,790,791,792,-1,793,794,795,-1,796,797,798,-1,799,800,801,-1,800,799,801,-1,802,803,804,-1,803,802,804,-1,805,806,807,-1,808,809,810,-1,811,812,813,-1,814,815,816,-1,817,818,819,-1,820,821,822,-1,823,824,825,-1,826,827,828,-1,829,830,831,-1,832,833,834,-1,835,836,837,-1,838,839,840,-1,841,842,843,-1,844,845,846,-1,847,848,849,-1,850,851,852,-1,853,854,855,-1,853,855,854,-1,856,857,858,-1,859,860,861,-1,862,863,864,-1,865,866,867,-1,868,869,870,-1,871,872,873,-1,874,875,876,-1,877,878,879,-1,880,881,882,-1,880,882,881,-1,883,884,885,-1,886,887,888,-1,889,890,891,-1,892,893,894,-1,895,896,897,-1,898,899,900,-1,901,902,903,-1,904,905,906,-1,907,908,909,-1,910,911,912,-1,913,914,915,-1,916,917,918,-1,919,920,921,-1,922,923,924,-1,925,926,927,-1,925,927,926,-1,928,929,930,-1,931,932,933,-1,934,935,936,-1,937,938,939,-1,940,941,942,-1,943,944,945,-1,946,947,948,-1,949,950,951,-1,952,953,954,-1,955,956,957,-1,958,959,960,-1,961,962,963,-1,964,965,966,-1,967,968,969,-1,970,971,972,-1,973,974,975,-1,976,977,978,-1,979,980,981,-1,982,983,984,-1,985,986,987,-1,988,989,990,-1,991,992,993,-1,994,995,996,-1,997,998,999,-1,1000,1001,1002,-1,1003,1004,1005,-1,1006,1007,1008,-1,1009,1010,1011,-1,1012,1013,1014,-1,1015,1016,1017,-1,1018,1019,1020,-1,1021,1022,1023,-1,1024,1025,1026,-1,1027,1028,1029,-1,1030,1031,1032,-1,1033,1034,1035,-1,1036,1037,1038,-1,1039,1040,1041,-1,1042,1043,1044,-1,1045,1046,1047,-1,1048,1049,1050,-1,1051,1052,1053,-1,1054,1055,1056,-1,1057,1058,1059,-1,1060,1061,1062,-1,1063,1064,1065,-1,1066,1067,1068,-1,1069,1070,1071,-1,1072,1073,1074,-1,1075,1076,1077,-1,1078,1079,1080,-1,1081,1082,1083,-1,1084,1085,1086,-1,1087,1088,1089,-1,1090,1091,1092,-1,1093,1094,1095,-1,1096,1097,1098,-1,1099,1100,1101,-1,1102,1103,1104,-1,1105,1106,1107,-1,1108,1109,1110,-1,1111,1112,1113,-1,1114,1115,1116,-1,1117,1118,1119,-1,1120,1121,1122,-1,1123,1124,1125,-1,1126,1127,1128,-1,1129,1130,1131,-1,1132,1133,1134,-1,1135,1136,1137,-1,1138,1139,1140,-1,1141,1142,1143,-1,1144,1145,1146,-1,1147,1148,1149,-1,1150,1151,1152,-1,1153,1154,1155,-1,1156,1157,1158,-1,1159,1160,1161,-1,1162,1163,1164,-1,1165,1166,1167,-1,1168,1169,1170,-1,1171,1172,1173,-1,1174,1175,1176,-1,1177,1178,1179,-1,1180,1181,1182,-1,1183,1184,1185,-1,1186,1187,1188,-1,1189,1190,1191,-1,1192,1193,1194,-1,1195,1196,1197,-1,1198,1199,1200,-1,1201,1202,1203,-1,1204,1205,1206,-1,1207,1208,1209,-1,1210,1211,1212,-1,1213,1214,1215,-1,1216,1217,1218,-1,1219,1220,1221,-1,1222,1223,1224,-1,1225,1226,1227,-1,1228,1229,1230,-1,1231,1232,1233,-1,1234,1235,1236,-1,1237,1238,1239,-1,1240,1241,1242,-1,1243,1244,1245,-1,1246,1247,1248,-1,1249,1250,1251,-1,1252,1253,1254,-1,1255,1256,1257,-1,1258,1259,1260,-1,1261,1262,1263,-1,1264,1265,1266,-1,1267,1268,1269,-1,1270,1271,1272,-1,1273,1274,1275,-1,1276,1277,1278,-1,1279,1280,1281,-1,1282,1283,1284,-1,1285,1286,1287,-1,1288,1289,1290,-1,1291,1292,1293,-1,1294,1295,1296,-1,1297,1298,1299,-1,1300,1301,1302,-1,1303,1304,1305,-1,1306,1307,1308,-1,1309,1310,1311,-1,1312,1313,1314,-1,1315,1316,1317,-1,1318,1319,1320,-1,1321,1322,1323,-1,1324,1325,1326,-1,1327,1328,1329,-1,1330,1331,1332,-1,1333,1334,1335,-1,1336,1337,1338,-1,1339,1340,1341,-1,1342,1343,1344,-1,1345,1346,1347,-1,1348,1349,1350,-1,1351,1352,1353,-1,1354,1355,1356,-1,1357,1358,1359,-1,1360,1361,1362,-1,1363,1364,1365,-1,1366,1367,1368,-1,1369,1370,1371,-1,1372,1373,1374,-1,1375,1376,1377,-1,1378,1379,1380,-1,1381,1382,1383,-1,1384,1385,1386,-1,1387,1388,1389,-1,1390,1391,1392,-1,1393,1394,1395,-1,1396,1397,1398,-1,1399,1400,1401,-1,1402,1403,1404,-1,1405,1406,1407,-1,1408,1409,1410,-1,1411,1412,1413,-1,1414,1415,1416,-1,1417,1418,1419,-1,1420,1421,1422,-1,1423,1424,1425,-1,1426,1427,1428,-1,1429,1430,1431,-1,1432,1433,1434,-1,1435,1436,1437,-1,1438,1439,1440,-1,1441,1442,1443,-1,1444,1445,1446,-1,1447,1448,1449,-1,1450,1451,1452,-1,1453,1454,1455,-1,1456,1457,1458,-1,1459,1460,1461,-1,1462,1463,1464,-1,1465,1466,1467,-1,1468,1469,1470,-1,1471,1472,1473,-1,1474,1475,1476,-1,1477,1478,1479,-1,1480,1481,1482,-1,1483,1484,1485,-1,1486,1487,1488,-1,1489,1490,1491,-1,1492,1493,1494,-1,1495,1496,1497,-1,1498,1499,1500,-1,1501,1502,1503,-1,1504,1505,1506,-1,1507,1508,1509,-1,1510,1511,1512,-1,1513,1514,1515,-1,1516,1517,1518,-1,1519,1520,1521,-1,1522,1523,1524,-1,1525,1526,1527,-1,1528,1529,1530,-1,1531,1532,1533,-1,1534,1535,1536,-1,1537,1538,1539,-1,1540,1541,1542,-1,1543,1544,1545,-1,1546,1547,1548,-1,1549,1550,1551,-1,1552,1553,1554,-1,1555,1556,1557,-1,1558,1559,1560,-1,1561,1562,1563,-1,1564,1565,1566,-1,1567,1568,1569,-1,1570,1571,1572,-1,1573,1574,1575,-1,1576,1577,1578,-1,1579,1580,1581,-1,1582,1583,1584,-1,1585,1586,1587,-1,1588,1589,1590,-1,1591,1592,1593,-1,1594,1595,1596,-1,1597,1598,1599,-1,1600,1601,1602,-1,1603,1604,1605,-1,1606,1607,1608,-1,1609,1610,1611,-1,1612,1613,1614,-1,1615,1616,1617,-1,1618,1619,1620,-1,1621,1622,1623,-1,1624,1625,1626,-1,1627,1628,1629,-1,1630,1631,1632,-1,1633,1634,1635,-1,1636,1637,1638,-1,1639,1640,1641,-1,1642,1643,1644,-1,1645,1646,1647,-1,1648,1649,1650,-1,1651,1652,1653,-1,1654,1655,1656,-1,1657,1658,1659,-1,1660,1661,1662,-1,1663,1664,1665,-1,1666,1667,1668,-1,1669,1670,1671,-1,1672,1673,1674,-1,1675,1676,1677,-1,1678,1679,1680,-1,1681,1682,1683,-1,1684,1685,1686,-1,1687,1688,1689,-1,1690,1691,1692,-1,1693,1694,1695,-1,1696,1697,1698,-1,1699,1700,1701,-1,1702,1703,1704,-1,1705,1706,1707,-1,1708,1709,1710,-1,1711,1712,1713,-1,1714,1715,1716,-1,1717,1718,1719,-1,1720,1721,1722,-1,1723,1724,1725,-1,1726,1727,1728,-1,1729,1730,1731,-1,1732,1733,1734,-1,1735,1736,1737,-1,1738,1739,1740,-1,1741,1742,1743,-1,1744,1745,1746,-1,1747,1748,1749,-1,1750,1751,1752,-1,1753,1754,1755,-1,1756,1757,1758,-1,1759,1760,1761,-1,1762,1763,1764,-1,1765,1766,1767,-1,1768,1769,1770,-1,1771,1772,1773,-1,1774,1775,1776,-1,1777,1778,1779,-1,1780,1781,1782,-1,1783,1784,1785,-1,1786,1787,1788,-1,1789,1790,1791,-1,1792,1793,1794,-1,1795,1796,1797,-1,1798,1799,1800,-1,1801,1802,1803,-1,1804,1805,1806,-1,1807,1808,1809,-1,1810,1811,1812,-1,1813,1814,1815,-1,1816,1817,1818,-1,1819,1820,1821,-1,1822,1823,1824,-1,1825,1826,1827,-1,1828,1829,1830,-1,1831,1832,1833,-1,1834,1835,1836,-1,1837,1838,1839,-1,1840,1841,1842,-1,1843,1844,1845,-1,1846,1847,1848,-1,1849,1850,1851,-1,1852,1853,1854,-1,1855,1856,1857,-1,1858,1859,1860,-1,1861,1862,1863,-1,1864,1865,1866,-1,1867,1868,1869,-1,1870,1871,1872,-1,1873,1874,1875,-1,1876,1877,1878,-1,1879,1880,1881,-1,1882,1883,1884,-1,1885,1886,1887,-1,1888,1889,1890,-1,1891,1892,1893,-1,1894,1895,1896,-1,1897,1898,1899,-1,1900,1901,1902,-1,1903,1904,1905,-1,1906,1907,1908,-1,1909,1910,1911,-1,1912,1913,1914,-1,1915,1916,1917,-1,1918,1919,1920,-1,1921,1922,1923,-1,1924,1925,1926,-1,1927,1928,1929,-1,1930,1931,1932,-1,1933,1934,1935,-1,1936,1937,1938,-1,1939,1940,1941,-1,1942,1943,1944,-1,1945,1946,1947,-1,1948,1949,1950,-1,1951,1952,1953,-1,1954,1955,1956,-1,1957,1958,1959,-1,1960,1961,1962,-1,1963,1964,1965,-1,1966,1967,1968,-1,1969,1970,1971,-1,1972,1973,1974,-1,1975,1976,1977,-1,1978,1979,1980,-1,1981,1982,1983,-1,1984,1985,1986,-1,1987,1988,1989,-1,1990,1991,1992,-1,1993,1994,1995,-1,1996,1997,1998,-1,1999,2000,2001,-1,2002,2003,2004,-1,2005,2006,2007,-1,2008,2009,2010,-1,2011,2012,2013,-1,2014,2015,2016,-1,2017,2018,2019,-1,2020,2021,2022,-1,2023,2024,2025,-1,2026,2027,2028,-1,2029,2030,2031,-1,2032,2033,2034,-1,2035,2036,2037,-1,2038,2039,2040,-1,2041,2042,2043,-1,2044,2045,2046,-1,2047,2048,2049,-1,2050,2051,2052,-1,2053,2054,2055,-1,2056,2057,2058,-1,2059,2060,2061,-1,2062,2063,2064,-1,2065,2066,2067,-1,2068,2069,2070,-1,2071,2072,2073,-1,2074,2075,2076,-1,2077,2078,2079,-1,2080,2081,2082,-1,2083,2084,2085,-1,2086,2087,2088,-1,2089,2090,2091,-1,2092,2093,2094,-1,2095,2096,2097,-1,2098,2099,2100,-1,2101,2102,2103,-1,2104,2105,2106,-1,2107,2108,2109,-1,2110,2111,2112,-1,2113,2114,2115,-1,2116,2117,2118,-1,2119,2120,2121,-1,2122,2123,2124,-1,2125,2126,2127,-1,2128,2129,2130,-1,2131,2132,2133,-1,2134,2135,2136,-1,2137,2138,2139,-1,2140,2141,2142,-1,2143,2144,2145,-1,2146,2147,2148,-1,2149,2150,2151,-1,2152,2153,2154,-1,2155,2156,2157,-1,2158,2159,2160,-1,2161,2162,2163,-1,2164,2165,2166,-1,2167,2168,2169,-1,2170,2171,2172,-1,2173,2174,2175,-1,2176,2177,2178,-1,2179,2180,2181,-1,2182,2183,2184,-1,2185,2186,2187,-1,2188,2189,2190,-1,2191,2192,2193,-1,2194,2195,2196,-1,2197,2198,2199,-1,2200,2201,2202,-1,2203,2204,2205,-1,2206,2207,2208,-1,2209,2210,2211,-1,2212,2213,2214,-1,2215,2216,2217,-1,2218,2219,2220,-1,2221,2222,2223,-1,2224,2225,2226,-1,2227,2228,2229,-1,2230,2231,2232,-1,2233,2234,2235,-1,2236,2237,2238,-1,2239,2240,2241,-1,2242,2243,2244,-1,2245,2246,2247,-1,2248,2249,2250,-1,2251,2252,2253,-1,2254,2255,2256,-1,2257,2258,2259,-1,2260,2261,2262,-1,2263,2264,2265,-1,2266,2267,2268,-1,2269,2270,2271,-1,2272,2273,2274,-1,2275,2276,2277,-1,2278,2279,2280,-1,2281,2282,2283,-1,2284,2285,2286,-1,2287,2288,2289,-1,2290,2291,2292,-1,2293,2294,2295,-1,2296,2297,2298,-1,2299,2300,2301,-1,2302,2303,2304,-1,2305,2306,2307,-1,2308,2309,2310,-1,2311,2312,2313,-1,2314,2315,2316,-1,2317,2318,2319,-1,2320,2321,2322,-1,2323,2324,2325,-1,2326,2327,2328,-1,2329,2330,2331,-1,2332,2333,2334,-1,2335,2336,2337,-1,2338,2339,2340,-1,2341,2342,2343,-1,2344,2345,2346,-1,2347,2348,2349,-1,2350,2351,2352,-1,2353,2354,2355,-1,2356,2357,2358,-1,2359,2360,2361,-1,2362,2363,2364,-1,2365,2366,2367,-1,2368,2369,2370,-1,2371,2372,2373,-1,2374,2375,2376,-1,2377,2378,2379,-1,2380,2381,2382,-1,2383,2384,2385,-1,2386,2387,2388,-1,2389,2390,2391,-1,2392,2393,2394,-1,2395,2396,2397,-1,2398,2399,2400,-1,2401,2402,2403,-1,2404,2405,2406,-1,2407,2408,2409,-1,2410,2411,2412,-1,2413,2414,2415,-1,2416,2417,2418,-1,2419,2420,2421,-1,2422,2423,2424,-1,2425,2426,2427,-1,2428,2429,2430,-1,2431,2432,2433,-1,2434,2435,2436,-1,2434,2436,2437,-1]
IndexedFaceSet168.creaseAngle = 1.61
Coordinate169 = x3d.Coordinate()

IndexedFaceSet168.coord = Coordinate169

Shape164.geometry = IndexedFaceSet168

Transform163.children.append(Shape164)

fieldValue162.children.append(Transform163)

ProtoInstance160.fieldValue.append(fieldValue162)

fieldValue159.children.append(ProtoInstance160)
ProtoInstance170 = x3d.ProtoInstance()
ProtoInstance170.name = "Joint"
ProtoInstance170.DEF = "hanim_r_knee"
fieldValue171 = x3d.fieldValue()
fieldValue171.name = "name"
fieldValue171.value = "r_knee"

ProtoInstance170.fieldValue.append(fieldValue171)
fieldValue172 = x3d.fieldValue()
fieldValue172.name = "center"
fieldValue172.value = "-0.0699 0.51 -0.0166"

ProtoInstance170.fieldValue.append(fieldValue172)
fieldValue173 = x3d.fieldValue()
fieldValue173.name = "children"
ProtoInstance174 = x3d.ProtoInstance()
ProtoInstance174.name = "Segment"
ProtoInstance174.DEF = "hanim_r_calf"
fieldValue175 = x3d.fieldValue()
fieldValue175.name = "name"
fieldValue175.value = "r_calf"

ProtoInstance174.fieldValue.append(fieldValue175)
fieldValue176 = x3d.fieldValue()
fieldValue176.name = "children"
Transform177 = x3d.Transform()
Transform177.DEF = "r_calf_adjust"
Transform177.center = [0.43,1.1,-0.05]
Transform177.rotation = [0,1,0,1.570796]
Transform177.scale = [0.1,0.1,0.1]
Shape178 = x3d.Shape()
Appearance179 = x3d.Appearance()
Material180 = x3d.Material()
Material180.USE = "Pants_Color"

Appearance179.material = Material180
ImageTexture181 = x3d.ImageTexture()
ImageTexture181.USE = "camo"

Appearance179.texture = ImageTexture181

Shape178.appearance = Appearance179
IndexedFaceSet182 = x3d.IndexedFaceSet()
IndexedFaceSet182.coordIndex = [0,1,2,-1,3,4,5,-1,6,7,8,-1,9,10,11,-1,12,13,14,-1,15,16,17,-1,18,19,20,-1,21,22,23,-1,24,25,26,-1,27,28,29,-1,30,31,32,-1,33,34,35,-1,36,37,38,-1,39,40,41,-1,42,43,44,-1,45,46,47,-1,48,49,50,-1,51,52,53,-1,54,55,56,-1,57,58,59,-1,60,61,62,-1,63,64,65,-1,66,67,68,-1,69,70,71,-1,72,73,74,-1,75,76,77,-1,78,79,80,-1,81,82,83,-1,84,85,86,-1,87,88,89,-1,90,91,92,-1,93,94,95,-1,96,97,98,-1,99,100,101,-1,102,103,104,-1,105,106,107,-1,108,109,110,-1,111,112,113,-1,114,115,116,-1,117,118,119,-1,120,121,122,-1,123,124,125,-1,126,127,128,-1,129,130,131,-1,132,133,134,-1,135,136,137,-1,138,139,140,-1,141,142,143,-1,144,145,146,-1,147,148,149,-1,150,151,152,-1,153,154,155,-1,156,157,158,-1,159,160,161,-1,162,163,164,-1,165,166,167,-1,168,169,170,-1,171,172,173,-1,174,175,176,-1,177,178,179,-1,180,181,182,-1,183,184,185,-1,186,187,188,-1,189,190,191,-1,192,193,194,-1,195,196,197,-1,198,199,200,-1,201,202,203,-1,204,205,206,-1,207,208,209,-1,210,211,212,-1,213,214,215,-1,216,217,218,-1,219,220,221,-1,222,223,224,-1,225,226,227,-1,228,229,230,-1,231,232,233,-1,234,235,236,-1,237,238,239,-1,240,241,242,-1,243,244,245,-1,246,247,248,-1,249,250,251,-1,252,253,254,-1,255,256,257,-1,258,259,260,-1,261,262,263,-1,264,265,266,-1,267,268,269,-1,270,271,272,-1,273,274,275,-1,276,277,278,-1,279,280,281,-1,282,283,284,-1,285,286,287,-1,288,289,290,-1,291,292,293,-1,294,295,296,-1,297,298,299,-1,300,301,302,-1,303,304,305,-1,306,307,308,-1,309,310,311,-1,312,313,314,-1,315,316,317,-1,318,319,320,-1,321,322,323,-1,324,325,326,-1,327,328,329,-1,330,331,332,-1,333,334,335,-1,336,337,338,-1,339,340,341,-1,342,343,344,-1,345,346,347,-1,348,349,350,-1,351,352,353,-1,354,355,356,-1,357,358,359,-1,360,361,362,-1,363,364,365,-1,366,367,368,-1,369,370,371,-1,372,373,374,-1,375,376,377,-1,378,379,380,-1,381,382,383,-1,384,385,386,-1,387,388,389,-1,390,391,392,-1,393,394,395,-1,396,397,398,-1,399,400,401,-1,402,403,404,-1,405,406,407,-1,408,409,410,-1,411,412,413,-1,414,415,416,-1,417,418,419,-1,420,421,422,-1,423,424,425,-1,426,427,428,-1,429,430,431,-1,432,433,434,-1,435,436,437,-1,438,439,440,-1,441,442,443,-1,444,445,446,-1,447,448,449,-1,450,451,452,-1,453,454,455,-1,456,457,458,-1,459,460,461,-1,462,463,464,-1,465,466,467,-1,468,469,470,-1,471,472,473,-1,474,475,476,-1,477,478,479,-1,480,481,482,-1,483,484,485,-1,486,487,488,-1,489,490,491,-1,492,493,494,-1,495,496,497,-1,498,499,500,-1,501,502,503,-1,504,505,506,-1,507,508,509,-1,510,511,512,-1,513,514,515,-1,516,517,518,-1,519,520,521,-1,522,523,524,-1,525,526,527,-1,528,529,530,-1,531,532,533,-1,534,535,536,-1,537,538,539,-1,540,541,542,-1,543,544,545,-1,546,547,548,-1,549,550,551,-1,552,553,554,-1,555,556,557,-1,558,559,560,-1,561,562,563,-1,564,565,566,-1,567,568,569,-1,570,571,572,-1,573,574,575,-1,576,577,578,-1,579,580,581,-1,582,583,584,-1,585,586,587,-1,588,589,590,-1,591,592,593,-1,594,595,596,-1,597,598,599,-1,600,601,602,-1,603,604,605,-1,606,607,608,-1,609,610,611,-1,612,613,614,-1,615,616,617,-1,618,619,620,-1,621,622,623,-1,624,625,626,-1,627,628,629,-1,630,631,632,-1,633,634,635,-1,636,637,638,-1,639,640,641,-1,642,643,644,-1,645,646,647,-1,648,649,650,-1,651,652,653,-1,654,655,656,-1,657,658,659,-1,660,661,662,-1,663,664,665,-1,666,667,668,-1,669,670,671,-1,672,673,674,-1,675,676,677,-1,678,679,680,-1,681,682,683,-1,684,685,686,-1,687,688,689,-1,690,691,692,-1,693,694,695,-1,696,697,698,-1,699,700,701,-1,702,703,704,-1,705,706,707,-1,708,709,710,-1,711,712,713,-1,714,715,716,-1,717,718,719,-1,720,721,722,-1,723,724,725,-1,726,727,728,-1,729,730,731,-1,732,733,734,-1,735,736,737,-1,738,739,740,-1,741,742,743,-1,744,745,746,-1,747,748,749,-1,750,751,752,-1,753,754,755,-1,756,757,758,-1,759,760,761,-1,762,763,764,-1,765,766,767,-1,768,769,770,-1,771,772,773,-1,774,775,776,-1,777,778,779,-1,780,781,782,-1,783,784,785,-1,786,787,788,-1,789,790,791,-1,792,793,794,-1,795,796,797,-1,798,799,800,-1,801,802,803,-1,804,805,806,-1,807,808,809,-1,810,811,812,-1,813,814,815,-1,816,817,818,-1,819,820,821,-1,822,823,824,-1,825,826,827,-1,828,829,830,-1,831,832,833,-1,834,835,836,-1,837,838,839,-1,840,841,842,-1,843,844,845,-1,846,847,848,-1,849,850,851,-1,852,853,854,-1,855,856,857,-1,858,859,860,-1,861,862,863,-1,864,865,866,-1,867,868,869,-1,870,871,872,-1,873,874,875,-1,876,877,878,-1,879,880,881,-1,882,883,884,-1,885,886,887,-1,888,889,890,-1,891,892,893,-1,894,895,896,-1,897,898,899,-1,900,901,902,-1,903,904,905,-1,906,907,908,-1,909,910,911,-1,912,913,914,-1,915,916,917,-1,918,919,920,-1,921,922,923,-1,924,925,926,-1,927,928,929,-1,930,931,932,-1,933,934,935,-1,936,937,938,-1,939,940,941,-1,942,943,944,-1,945,946,947,-1,948,949,950,-1,951,952,953,-1,954,955,956,-1,957,958,959,-1,960,961,962,-1,963,964,965,-1,966,967,968,-1,969,970,971,-1,972,973,974,-1,975,976,977,-1,978,979,980,-1,981,982,983,-1,984,985,986,-1,987,988,989,-1,990,991,992,-1,993,994,995,-1,996,997,998,-1,999,1000,1001,-1,1002,1003,1004,-1,1005,1006,1007,-1,1008,1009,1010,-1,1011,1012,1013,-1,1014,1015,1016,-1,1017,1018,1019,-1,1020,1021,1022,-1,1023,1024,1025,-1,1026,1027,1028,-1,1029,1030,1031,-1,1032,1033,1034,-1,1035,1036,1037,-1,1038,1039,1040,-1,1041,1042,1043,-1,1044,1045,1046,-1,1047,1048,1049,-1,1050,1051,1052,-1,1053,1054,1055,-1,1056,1057,1058,-1,1059,1060,1061,-1,1062,1063,1064,-1,1065,1066,1067,-1,1068,1069,1070,-1,1071,1072,1073,-1,1074,1075,1076,-1,1077,1078,1079,-1,1080,1081,1082,-1,1083,1084,1085,-1,1086,1087,1088,-1,1089,1090,1091,-1,1092,1093,1094,-1,1095,1096,1097,-1,1098,1099,1100,-1,1101,1102,1103,-1,1104,1105,1106,-1,1107,1108,1109,-1,1110,1111,1112,-1,1113,1114,1115,-1,1116,1117,1118,-1,1119,1120,1121,-1,1122,1123,1124,-1,1125,1126,1127,-1,1128,1129,1130,-1,1131,1132,1133,-1,1134,1135,1136,-1,1137,1138,1139,-1,1140,1141,1142,-1,1143,1144,1145,-1,1146,1147,1148,-1,1149,1150,1151,-1,1152,1153,1154,-1,1155,1156,1157,-1,1158,1159,1160,-1,1161,1162,1163,-1,1164,1165,1166,-1,1167,1168,1169,-1,1170,1171,1172,-1,1173,1174,1175,-1,1176,1177,1178,-1,1179,1180,1181,-1,1182,1183,1184,-1,1185,1186,1187,-1,1188,1189,1190,-1,1191,1192,1193,-1,1194,1195,1196,-1,1197,1198,1199,-1,1200,1201,1202,-1,1203,1204,1205,-1,1206,1207,1208,-1,1209,1210,1211,-1,1212,1213,1214,-1,1215,1216,1217,-1,1218,1219,1220,-1,1221,1222,1223,-1,1224,1225,1226,-1,1227,1228,1229,-1,1230,1231,1232,-1,1233,1234,1235,-1,1236,1237,1238,-1,1239,1240,1241,-1,1242,1243,1244,-1,1245,1246,1247,-1,1248,1249,1250,-1,1251,1252,1253,-1,1254,1255,1256,-1,1257,1258,1259,-1,1260,1261,1262,-1,1263,1264,1265,-1,1266,1267,1268,-1,1269,1270,1271,-1,1272,1273,1274,-1,1275,1276,1277,-1,1278,1279,1280,-1,1281,1282,1283,-1,1284,1285,1286,-1,1287,1288,1289,-1,1290,1291,1292,-1,1293,1294,1295,-1,1296,1297,1298,-1,1299,1300,1301,-1,1302,1303,1304,-1,1305,1306,1307,-1,1308,1309,1310,-1,1311,1312,1313,-1,1314,1315,1316,-1,1317,1318,1319,-1,1320,1321,1322,-1,1323,1324,1325,-1,1326,1327,1328,-1,1329,1330,1331,-1,1332,1333,1334,-1,1335,1336,1337,-1,1338,1339,1340,-1,1341,1342,1343,-1,1344,1345,1346,-1,1347,1348,1349,-1,1350,1351,1352,-1,1353,1354,1355,-1,1356,1357,1358,-1,1359,1360,1361,-1,1362,1363,1364,-1,1365,1366,1367,-1,1368,1369,1370,-1,1371,1372,1373,-1,1374,1375,1376,-1,1377,1378,1379,-1,1380,1381,1382,-1,1383,1384,1385,-1,1386,1387,1388,-1,1389,1390,1391,-1,1392,1393,1394,-1,1395,1396,1397,-1,1398,1399,1400,-1,1401,1402,1403,-1,1404,1405,1406,-1,1407,1408,1409,-1,1410,1411,1412,-1,1413,1414,1415,-1,1416,1417,1418,-1,1419,1420,1421,-1,1422,1423,1424,-1,1425,1426,1427,-1,1428,1429,1430,-1,1431,1432,1433,-1,1434,1435,1436,-1,1437,1438,1439,-1,1440,1441,1442,-1,1443,1444,1445,-1,1446,1447,1448,-1,1449,1450,1451,-1,1452,1453,1454,-1,1455,1456,1457,-1,1458,1459,1460,-1,1461,1462,1463,-1,1464,1465,1466,-1,1467,1468,1469,-1,1470,1471,1472,-1,1473,1474,1475,-1,1476,1477,1478,-1,1479,1480,1481,-1,1482,1483,1484,-1,1485,1486,1487,-1,1488,1489,1490,-1,1491,1492,1493,-1,1494,1495,1496,-1,1497,1498,1499,-1,1500,1501,1502,-1,1503,1504,1505,-1,1506,1507,1508,-1,1509,1510,1511,-1,1512,1513,1514,-1,1515,1516,1517,-1,1518,1519,1520,-1,1521,1522,1523,-1,1524,1525,1526,-1,1527,1528,1529,-1,1530,1531,1532,-1,1533,1534,1535,-1,1536,1537,1538,-1,1539,1540,1541,-1,1542,1543,1544,-1,1545,1546,1547,-1,1548,1549,1550,-1,1551,1552,1553,-1,1554,1555,1556,-1,1557,1558,1559,-1,1560,1561,1562,-1,1563,1564,1565,-1,1566,1567,1568,-1,1569,1570,1571,-1,1572,1573,1574,-1,1575,1576,1577,-1,1578,1579,1580,-1,1581,1582,1583,-1,1584,1585,1586,-1,1587,1588,1589,-1,1590,1591,1592,-1,1593,1594,1595,-1,1596,1597,1598,-1,1599,1600,1601,-1,1602,1603,1604,-1,1605,1606,1607,-1,1608,1609,1610,-1,1611,1612,1613,-1,1614,1615,1616,-1,1617,1618,1619,-1,1620,1621,1622,-1,1623,1624,1625,-1,1626,1627,1628,-1,1629,1630,1631,-1,1632,1633,1634,-1,1635,1636,1637,-1,1638,1639,1640,-1,1641,1642,1643,-1,1644,1645,1646,-1,1647,1648,1649,-1,1650,1651,1652,-1,1653,1654,1655,-1,1656,1657,1658,-1,1659,1660,1661,-1,1662,1663,1664,-1,1665,1666,1667,-1,1668,1669,1670,-1,1671,1672,1673,-1,1674,1675,1676,-1,1677,1678,1679,-1,1680,1681,1682,-1,1683,1684,1685,-1,1686,1687,1688,-1,1689,1690,1691,-1,1692,1693,1694,-1,1695,1696,1697,-1,1698,1699,1700,-1,1701,1702,1703,-1,1704,1705,1706,-1,1707,1708,1709,-1,1710,1711,1712,-1,1713,1714,1715,-1,1716,1717,1718,-1,1719,1720,1721,-1,1722,1723,1724,-1,1725,1726,1727,-1,1728,1729,1730,-1,1731,1732,1733,-1,1734,1735,1736,-1,1737,1738,1739,-1,1740,1741,1742,-1,1743,1744,1745,-1,1746,1747,1748,-1,1749,1750,1751,-1,1752,1753,1754,-1,1755,1756,1757,-1,1758,1759,1760,-1,1761,1762,1763,-1,1764,1765,1766,-1,1767,1768,1769,-1,1770,1771,1772,-1,1773,1774,1775,-1,1776,1777,1778,-1,1779,1780,1781,-1,1782,1783,1784,-1,1785,1786,1787,-1,1788,1789,1790,-1,1791,1792,1793,-1,1794,1795,1796,-1,1797,1798,1799,-1,1800,1801,1802,-1,1803,1804,1805,-1,1806,1807,1808,-1,1809,1810,1811,-1,1812,1813,1814,-1,1815,1816,1817,-1,1818,1819,1820,-1,1821,1822,1823,-1,1824,1825,1826,-1,1827,1828,1829,-1,1830,1831,1832,-1,1830,1832,1833,-1]
IndexedFaceSet182.creaseAngle = 1.57
Coordinate183 = x3d.Coordinate()

IndexedFaceSet182.coord = Coordinate183

Shape178.geometry = IndexedFaceSet182

Transform177.children.append(Shape178)

fieldValue176.children.append(Transform177)

ProtoInstance174.fieldValue.append(fieldValue176)

fieldValue173.children.append(ProtoInstance174)
ProtoInstance184 = x3d.ProtoInstance()
ProtoInstance184.name = "Joint"
ProtoInstance184.DEF = "hanim_r_ankle"
fieldValue185 = x3d.fieldValue()
fieldValue185.name = "name"
fieldValue185.value = "r_ankle"

ProtoInstance184.fieldValue.append(fieldValue185)
fieldValue186 = x3d.fieldValue()
fieldValue186.name = "center"
fieldValue186.value = "-0.064 0.0753 -0.0412"

ProtoInstance184.fieldValue.append(fieldValue186)
fieldValue187 = x3d.fieldValue()
fieldValue187.name = "children"
ProtoInstance188 = x3d.ProtoInstance()
ProtoInstance188.name = "Segment"
ProtoInstance188.DEF = "hanim_r_hindfoot"
fieldValue189 = x3d.fieldValue()
fieldValue189.name = "name"
fieldValue189.value = "r_hindfoot"

ProtoInstance188.fieldValue.append(fieldValue189)
fieldValue190 = x3d.fieldValue()
fieldValue190.name = "children"
Transform191 = x3d.Transform()
Transform191.DEF = "r_foot_adjust"
Transform191.center = [0.3319,1.1,-0.04]
Transform191.rotation = [0,1,0,1.570796]
Transform191.scale = [0.1,0.1,0.1]
Shape192 = x3d.Shape()
Appearance193 = x3d.Appearance()
Material194 = x3d.Material()
Material194.USE = "Shoe_Color"

Appearance193.material = Material194

Shape192.appearance = Appearance193
IndexedFaceSet195 = x3d.IndexedFaceSet()
IndexedFaceSet195.coordIndex = [0,1,2,-1,3,4,5,-1,6,7,8,-1,9,10,11,-1,12,13,14,-1,15,16,17,-1,18,19,20,-1,21,22,23,-1,24,25,26,-1,27,28,29,-1,30,31,32,-1,33,34,35,-1,36,37,38,-1,39,40,41,-1,42,43,44,-1,45,46,47,-1,48,49,50,-1,51,52,53,-1,54,55,56,-1,57,58,59,-1,60,61,62,-1,63,64,65,-1,66,67,68,-1,69,70,71,-1,72,73,74,-1,75,76,77,-1,78,79,80,-1,81,82,83,-1,84,85,86,-1,87,88,89,-1,90,91,92,-1,93,94,95,-1,96,97,98,-1,99,100,101,-1,102,103,104,-1,105,106,107,-1,108,109,110,-1,111,112,113,-1,114,115,116,-1,117,118,119,-1,120,121,122,-1,123,124,125,-1,126,127,128,-1,129,130,131,-1,132,133,134,-1,135,136,137,-1,138,139,140,-1,141,142,143,-1,144,145,146,-1,147,148,149,-1,150,151,152,-1,153,154,155,-1,156,157,158,-1,159,160,161,-1,162,163,164,-1,165,166,167,-1,168,169,170,-1,171,172,173,-1,174,175,176,-1,177,178,179,-1,180,181,182,-1,183,184,185,-1,186,187,188,-1,189,190,191,-1,192,193,194,-1,195,196,197,-1,198,199,200,-1,201,202,203,-1,204,205,206,-1,207,208,209,-1,210,211,212,-1,213,214,215,-1,216,217,218,-1,219,220,221,-1,222,223,224,-1,225,226,227,-1,228,229,230,-1,231,232,233,-1,234,235,236,-1,237,238,239,-1,240,241,242,-1,243,244,245,-1,246,247,248,-1,249,250,251,-1,252,253,254,-1,255,256,257,-1,258,259,260,-1,261,262,263,-1,264,265,266,-1,267,268,269,-1,270,271,272,-1,273,274,275,-1,276,277,278,-1,279,280,281,-1,282,283,284,-1,285,286,287,-1,288,289,290,-1,291,292,293,-1,294,295,296,-1,297,298,299,-1,300,301,302,-1,303,304,305,-1,306,307,308,-1,309,310,311,-1,312,313,314,-1,315,316,317,-1,318,319,320,-1,321,322,323,-1,324,325,326,-1,327,328,329,-1,330,331,332,-1,333,334,335,-1,336,337,338,-1,339,340,341,-1,342,343,344,-1,345,346,347,-1,348,349,350,-1,351,352,353,-1,354,355,356,-1,357,358,359,-1,360,361,362,-1,363,364,365,-1,366,367,368,-1,369,370,371,-1,372,373,374,-1,375,376,377,-1,378,379,380,-1,381,382,383,-1,384,385,386,-1,387,388,389,-1,390,391,392,-1,393,394,395,-1,396,397,398,-1,399,400,401,-1,402,403,404,-1,405,406,407,-1,408,409,410,-1,411,412,413,-1,414,415,416,-1,417,418,419,-1,420,421,422,-1,423,424,425,-1,426,427,428,-1,429,430,431,-1,432,433,434,-1,435,436,437,-1,438,439,440,-1,441,442,443,-1,444,445,446,-1,447,448,449,-1,450,451,452,-1,453,454,455,-1,456,457,458,-1,459,460,461,-1,462,463,464,-1,465,466,467,-1,468,469,470,-1,471,472,473,-1,474,475,476,-1,477,478,479,-1,480,481,482,-1,483,484,485,-1,486,487,488,-1,489,490,491,-1,492,493,494,-1,495,496,497,-1,498,499,500,-1,501,502,503,-1,504,505,506,-1,507,508,509,-1,510,511,512,-1,513,514,515,-1,516,517,518,-1,519,520,521,-1,522,523,524,-1,525,526,527,-1,528,529,530,-1,531,532,533,-1,534,535,536,-1,537,538,539,-1,540,541,542,-1,543,544,545,-1,546,547,548,-1,549,550,551,-1,552,553,554,-1,555,556,557,-1,558,559,560,-1,561,562,563,-1,564,565,566,-1,567,568,569,-1,570,571,572,-1,573,574,575,-1,576,577,578,-1,579,580,581,-1,582,583,584,-1,585,586,587,-1,588,589,590,-1,591,592,593,-1,594,595,596,-1,597,598,599,-1,600,601,602,-1,603,604,605,-1,606,607,608,-1,609,610,611,-1,612,613,614,-1,615,616,617,-1,618,619,620,-1,621,622,623,-1,624,625,626,-1,627,628,629,-1,630,631,632,-1,633,634,635,-1,636,637,638,-1,639,640,641,-1,642,643,644,-1,645,646,647,-1,648,649,650,-1,651,652,653,-1,654,655,656,-1,657,658,659,-1,660,661,662,-1,663,664,665,-1,666,667,668,-1,669,670,671,-1,672,673,674,-1,675,676,677,-1,678,679,680,-1,681,682,683,-1,684,685,686,-1,687,688,689,-1,690,691,692,-1,693,694,695,-1,696,697,698,-1,699,700,701,-1,702,703,704,-1,705,706,707,-1,708,709,710,-1,711,712,713,-1,714,715,716,-1,717,718,719,-1,720,721,722,-1,723,724,725,-1,726,727,728,-1,729,730,731,-1,732,733,734,-1,735,736,737,-1,738,739,740,-1,741,742,743,-1,744,745,746,-1,747,748,749,-1,750,751,752,-1,753,754,755,-1,756,757,758,-1,759,760,761,-1,762,763,764,-1,765,766,767,-1,768,769,770,-1,771,772,773,-1,774,775,776,-1,777,778,779,-1,780,781,782,-1,783,784,785,-1,786,787,788,-1,789,790,791,-1,792,793,794,-1,795,796,797,-1,798,799,800,-1,801,802,803,-1,804,805,806,-1,807,808,809,-1,810,811,812,-1,813,814,815,-1,816,817,818,-1,819,820,821,-1,822,823,824,-1,825,826,827,-1,828,829,830,-1,831,832,833,-1,834,835,836,-1,837,838,839,-1,840,841,842,-1,843,844,845,-1,846,847,848,-1,849,850,851,-1,852,853,854,-1,855,856,857,-1,858,859,860,-1,861,862,863,-1,864,865,866,-1,867,868,869,-1,870,871,872,-1,873,874,875,-1,876,877,878,-1,879,880,881,-1,882,883,884,-1,885,886,887,-1,888,889,890,-1,891,892,893,-1,894,895,896,-1,897,898,899,-1,900,901,902,-1,903,904,905,-1,906,907,908,-1,909,910,911,-1,912,913,914,-1,915,916,917,-1,918,919,920,-1,921,922,923,-1,924,925,926,-1,927,928,929,-1,930,931,932,-1,933,934,935,-1,936,937,938,-1,939,940,941,-1,942,943,944,-1,945,946,947,-1,948,949,950,-1,951,952,953,-1,954,955,956,-1,957,958,959,-1,960,961,962,-1,963,964,965,-1,966,967,968,-1,969,970,971,-1,972,973,974,-1,975,976,977,-1,978,979,980,-1,981,982,983,-1,984,985,986,-1,987,988,989,-1,990,991,992,-1,993,994,995,-1,996,997,998,-1,999,1000,1001,-1,1002,1003,1004,-1,1005,1006,1007,-1,1008,1009,1010,-1,1011,1012,1013,-1,1014,1015,1016,-1,1017,1018,1019,-1,1020,1021,1022,-1,1023,1024,1025,-1,1026,1027,1028,-1,1029,1030,1031,-1,1032,1033,1034,-1,1035,1036,1037,-1,1038,1039,1040,-1,1041,1042,1043,-1,1044,1045,1046,-1,1047,1048,1049,-1,1050,1051,1052,-1,1053,1054,1055,-1,1056,1057,1058,-1,1059,1060,1061,-1,1062,1063,1064,-1,1065,1066,1067,-1,1068,1069,1070,-1,1071,1072,1073,-1,1074,1075,1076,-1,1077,1078,1079,-1,1080,1081,1082,-1,1083,1084,1085,-1,1086,1087,1088,-1,1089,1090,1091,-1,1092,1093,1094,-1,1095,1096,1097,-1,1098,1099,1100,-1,1101,1102,1103,-1,1104,1105,1106,-1,1107,1108,1109,-1,1110,1111,1112,-1,1113,1114,1115,-1,1116,1117,1118,-1,1119,1120,1121,-1,1122,1123,1124,-1,1125,1126,1127,-1,1128,1129,1130,-1,1131,1132,1133,-1,1134,1135,1136,-1,1137,1138,1139,-1,1140,1141,1142,-1,1143,1144,1145,-1,1146,1147,1148,-1,1149,1150,1151,-1,1152,1153,1154,-1,1155,1156,1157,-1,1158,1159,1160,-1,1161,1162,1163,-1,1164,1165,1166,-1,1167,1168,1169,-1,1170,1171,1172,-1,1173,1174,1175,-1,1176,1177,1178,-1,1179,1180,1181,-1,1182,1183,1184,-1,1185,1186,1187,-1,1188,1189,1190,-1,1191,1192,1193,-1,1194,1195,1196,-1,1197,1198,1199,-1,1200,1201,1202,-1,1203,1204,1205,-1,1206,1207,1208,-1,1209,1210,1211,-1,1212,1213,1214,-1,1215,1216,1217,-1,1218,1219,1220,-1,1221,1222,1223,-1,1224,1225,1226,-1,1227,1228,1229,-1,1230,1231,1232,-1,1233,1234,1235,-1,1236,1237,1238,-1,1239,1240,1241,-1,1242,1243,1244,-1,1245,1246,1247,-1,1248,1249,1250,-1,1251,1252,1253,-1,1254,1255,1256,-1,1257,1258,1259,-1,1260,1261,1262,-1,1263,1264,1265,-1,1266,1267,1268,-1,1269,1270,1271,-1,1272,1273,1274,-1,1275,1276,1277,-1,1278,1279,1280,-1,1281,1282,1283,-1,1284,1285,1286,-1,1287,1288,1289,-1,1290,1291,1292,-1,1293,1294,1295,-1,1296,1297,1298,-1,1299,1300,1301,-1,1302,1303,1304,-1,1305,1306,1307,-1,1308,1309,1310,-1,1311,1312,1313,-1,1314,1315,1316,-1,1317,1318,1319,-1,1320,1321,1322,-1,1323,1324,1325,-1,1326,1327,1328,-1,1329,1330,1331,-1,1332,1333,1334,-1,1335,1336,1337,-1,1338,1339,1340,-1,1341,1342,1343,-1,1344,1345,1346,-1,1347,1348,1349,-1,1350,1351,1352,-1,1353,1354,1355,-1,1356,1357,1358,-1,1359,1360,1361,-1,1362,1363,1364,-1,1365,1366,1367,-1,1368,1369,1370,-1,1371,1372,1373,-1,1374,1375,1376,-1,1377,1378,1379,-1,1380,1381,1382,-1,1383,1384,1385,-1,1386,1387,1388,-1,1389,1390,1391,-1,1392,1393,1394,-1,1395,1396,1397,-1,1398,1399,1400,-1,1401,1402,1403,-1,1404,1405,1406,-1,1407,1408,1409,-1,1410,1411,1412,-1,1413,1414,1415,-1,1416,1417,1418,-1,1419,1420,1421,-1,1422,1423,1424,-1,1425,1426,1427,-1,1428,1429,1430,-1,1431,1432,1433,-1,1434,1435,1436,-1,1437,1438,1439,-1,1440,1441,1442,-1,1443,1444,1445,-1,1446,1447,1448,-1,1449,1450,1451,-1,1452,1453,1454,-1,1455,1456,1457,-1,1458,1459,1460,-1,1461,1462,1463,-1,1464,1465,1466,-1,1467,1468,1469,-1,1470,1471,1472,-1,1473,1474,1475,-1,1476,1477,1478,-1,1479,1480,1481,-1,1482,1483,1484,-1,1485,1486,1487,-1,1488,1489,1490,-1,1491,1492,1493,-1,1494,1495,1496,-1,1497,1498,1499,-1,1500,1501,1502,-1,1503,1504,1505,-1,1506,1507,1508,-1,1509,1510,1511,-1,1512,1513,1514,-1,1515,1516,1517,-1,1518,1519,1520,-1,1521,1522,1523,-1,1524,1525,1526,-1,1527,1528,1529,-1,1530,1531,1532,-1,1533,1534,1535,-1,1536,1537,1538,-1,1539,1540,1541,-1,1542,1543,1544,-1,1545,1546,1547,-1,1548,1549,1550,-1,1551,1552,1553,-1,1554,1555,1556,-1,1557,1558,1559,-1,1560,1561,1562,-1,1563,1564,1565,-1,1566,1567,1568,-1,1569,1570,1571,-1,1572,1573,1574,-1,1575,1576,1577,-1,1578,1579,1580,-1,1581,1582,1583,-1,1584,1585,1586,-1,1587,1588,1589,-1,1590,1591,1592,-1,1593,1594,1595,-1,1596,1597,1598,-1,1599,1600,1601,-1,1602,1603,1604,-1,1605,1606,1607,-1,1608,1609,1610,-1,1611,1612,1613,-1,1614,1615,1616,-1,1617,1618,1619,-1,1620,1621,1622,-1,1623,1624,1625,-1,1626,1627,1628,-1,1629,1630,1631,-1,1632,1633,1634,-1,1635,1636,1637,-1,1638,1639,1640,-1,1641,1642,1643,-1,1644,1645,1646,-1,1647,1648,1649,-1,1650,1651,1652,-1,1653,1654,1655,-1,1656,1657,1658,-1,1659,1660,1661,-1,1662,1663,1664,-1,1665,1666,1667,-1,1668,1669,1670,-1,1671,1672,1673,-1,1674,1675,1676,-1,1677,1678,1679,-1,1680,1681,1682,-1,1683,1684,1685,-1,1686,1687,1688,-1,1689,1690,1691,-1,1692,1693,1694,-1,1695,1696,1697,-1,1698,1699,1700,-1,1701,1702,1703,-1,1704,1705,1706,-1,1707,1708,1709,-1,1710,1711,1712,-1]
IndexedFaceSet195.creaseAngle = 1.57
Coordinate196 = x3d.Coordinate()

IndexedFaceSet195.coord = Coordinate196

Shape192.geometry = IndexedFaceSet195

Transform191.children.append(Shape192)

fieldValue190.children.append(Transform191)

ProtoInstance188.fieldValue.append(fieldValue190)

fieldValue187.children.append(ProtoInstance188)

ProtoInstance184.fieldValue.append(fieldValue187)

fieldValue173.children.append(ProtoInstance184)

ProtoInstance170.fieldValue.append(fieldValue173)

fieldValue159.children.append(ProtoInstance170)

ProtoInstance156.fieldValue.append(fieldValue159)

fieldValue104.children.append(ProtoInstance156)

ProtoInstance101.fieldValue.append(fieldValue104)

fieldValue100.children.append(ProtoInstance101)
ProtoInstance197 = x3d.ProtoInstance()
ProtoInstance197.name = "Joint"
ProtoInstance197.DEF = "hanim_vl1"
fieldValue198 = x3d.fieldValue()
fieldValue198.name = "name"
fieldValue198.value = "vl1"

ProtoInstance197.fieldValue.append(fieldValue198)
fieldValue199 = x3d.fieldValue()
fieldValue199.name = "center"
fieldValue199.value = "-0.00405 1.07 -0.0275"

ProtoInstance197.fieldValue.append(fieldValue199)
fieldValue200 = x3d.fieldValue()
fieldValue200.name = "children"
ProtoInstance201 = x3d.ProtoInstance()
ProtoInstance201.name = "Segment"
ProtoInstance201.DEF = "hanim_c7"
fieldValue202 = x3d.fieldValue()
fieldValue202.name = "name"
fieldValue202.value = "l1"

ProtoInstance201.fieldValue.append(fieldValue202)
fieldValue203 = x3d.fieldValue()
fieldValue203.name = "children"
Transform204 = x3d.Transform()
Transform204.DEF = "torso_adjust"
Transform204.center = [0,1,0]
Transform204.rotation = [0,1,0,1.570796]
Transform204.scale = [0.1,0.1,0.1]
Shape205 = x3d.Shape()
Appearance206 = x3d.Appearance()
Material207 = x3d.Material()
Material207.DEF = "Shirt_Color"
Material207.ambientIntensity = 0.25
Material207.diffuseColor = [0.6,0.0745,0.1137]

Appearance206.material = Material207
ImageTexture208 = x3d.ImageTexture()
ImageTexture208.USE = "camo"

Appearance206.texture = ImageTexture208

Shape205.appearance = Appearance206
IndexedFaceSet209 = x3d.IndexedFaceSet()
IndexedFaceSet209.coordIndex = [0,1,2,-1,3,4,5,-1,6,7,8,-1,9,10,11,-1,12,13,14,-1,15,16,17,-1,18,19,20,-1,21,22,23,-1,24,25,26,-1,27,28,29,-1,30,31,32,-1,33,34,35,-1,36,37,38,-1,39,40,41,-1,42,43,44,-1,45,46,47,-1,48,49,50,-1,53,57,58,-1,62,59,60,-1,67,68,69,-1,70,65,71,-1,76,77,78,-1,77,73,54,-1,79,55,80,-1,55,56,80,-1,59,62,52,-1,78,77,75,-1,64,79,80,-1,51,52,82,-1,83,84,82,-1,62,60,85,-1,86,87,88,-1,88,69,68,-1,89,76,78,-1,77,54,75,-1,78,75,66,-1,89,58,57,-1,53,90,57,-1,90,64,91,-1,63,79,64,-1,80,92,93,-1,92,80,56,-1,94,95,62,-1,85,69,88,-1,71,96,67,-1,97,71,65,-1,54,73,72,-1,58,89,78,-1,83,82,52,-1,98,62,87,-1,99,68,67,-1,70,67,69,-1,100,71,97,-1,438,101,74,-1,102,103,435,-1,53,64,90,-1,91,64,93,-1,81,104,56,-1,84,105,82,-1,106,83,107,-1,106,84,83,-1,95,107,52,-1,98,94,62,-1,86,88,108,-1,85,88,87,-1,68,108,88,-1,68,99,108,-1,99,67,96,-1,71,67,70,-1,100,96,71,-1,100,97,109,-1,110,109,111,-1,438,112,101,-1,103,112,435,-1,101,103,113,-1,102,114,115,-1,116,113,115,-1,117,90,91,-1,64,80,93,-1,92,56,104,-1,61,118,81,-1,105,119,51,-1,120,119,121,-1,107,83,52,-1,62,95,52,-1,95,94,122,-1,62,85,87,-1,123,98,87,-1,123,87,86,-1,86,108,124,-1,108,99,124,-1,110,100,109,-1,103,115,113,-1,103,102,115,-1,125,91,93,-1,104,81,126,-1,118,127,126,-1,120,121,128,-1,121,84,106,-1,121,105,84,-1,95,129,107,-1,129,95,122,-1,130,122,94,-1,130,94,131,-1,94,98,131,-1,132,110,133,-1,110,111,133,-1,134,135,136,-1,101,112,103,-1,135,101,113,-1,116,115,114,-1,137,138,116,-1,104,126,139,-1,139,126,127,-1,127,118,140,-1,118,126,81,-1,140,61,51,-1,140,118,61,-1,119,140,51,-1,119,120,140,-1,105,121,119,-1,82,105,51,-1,128,121,106,-1,141,142,133,-1,143,133,111,-1,101,135,74,-1,144,145,146,-1,144,146,147,-1,148,149,150,-1,151,150,149,-1,152,151,149,-1,153,154,155,-1,156,157,158,-1,159,160,154,-1,137,161,138,-1,162,163,145,-1,164,165,163,-1,166,167,168,-1,168,169,162,-1,168,164,169,-1,170,160,157,-1,156,170,157,-1,159,143,160,-1,143,141,133,-1,143,157,160,-1,136,138,161,-1,171,136,163,-1,164,167,158,-1,170,155,154,-1,156,151,155,-1,157,143,111,-1,146,163,136,-1,167,166,158,-1,168,167,164,-1,164,158,173,-1,156,155,170,-1,160,170,154,-1,159,141,143,-1,156,150,151,-1,136,161,147,-1,163,162,169,-1,166,150,156,-1,165,164,173,-1,138,113,116,-1,113,138,136,-1,163,146,145,-1,166,156,158,-1,175,176,157,-1,178,173,179,-1,135,113,136,-1,146,136,147,-1,157,111,172,-1,180,135,181,-1,164,163,169,-1,165,182,163,-1,183,175,157,-1,135,134,181,-1,157,176,158,-1,178,182,165,-1,180,184,185,-1,184,186,187,-1,134,188,186,-1,171,188,136,-1,182,171,163,-1,184,180,181,-1,134,186,181,-1,182,190,171,-1,187,191,192,-1,188,134,136,-1,193,194,183,-1,181,186,184,-1,195,190,182,-1,195,182,178,-1,196,197,198,-1,199,200,179,-1,199,158,176,-1,174,183,157,-1,183,177,193,-1,188,187,186,-1,190,201,171,-1,195,178,197,-1,178,165,173,-1,171,201,188,-1,203,190,195,-1,204,205,206,-1,206,175,194,-1,175,183,194,-1,189,193,177,-1,203,195,207,-1,203,201,190,-1,203,207,196,-1,197,207,195,-1,185,184,187,-1,207,197,196,-1,196,198,208,-1,192,185,187,-1,208,209,210,-1,201,211,188,-1,197,178,198,-1,175,206,176,-1,205,176,206,-1,201,203,196,-1,187,188,211,-1,172,174,157,-1,198,178,179,-1,187,211,191,-1,201,196,211,-1,173,158,199,-1,213,214,215,-1,196,208,211,-1,204,206,194,-1,216,205,204,-1,217,194,212,-1,193,212,194,-1,205,218,199,-1,205,216,218,-1,217,219,214,-1,204,217,214,-1,220,215,219,-1,198,179,222,-1,205,199,176,-1,193,202,212,-1,191,221,192,-1,179,173,199,-1,217,204,194,-1,213,216,214,-1,217,212,219,-1,219,215,214,-1,213,215,223,-1,218,213,225,-1,215,226,223,-1,223,225,213,-1,227,221,191,-1,179,200,222,-1,210,228,229,-1,218,216,213,-1,227,191,210,-1,227,210,229,-1,209,230,231,-1,230,208,198,-1,232,230,198,-1,200,218,225,-1,199,218,200,-1,226,233,234,-1,210,235,228,-1,230,209,208,-1,236,237,225,-1,235,238,239,-1,240,200,225,-1,241,228,242,-1,211,210,191,-1,211,208,210,-1,243,240,237,-1,238,235,210,-1,209,238,210,-1,209,231,238,-1,238,231,239,-1,232,245,246,-1,198,222,232,-1,222,240,245,-1,226,215,220,-1,247,248,232,-1,248,239,231,-1,226,220,233,-1,248,231,230,-1,216,204,214,-1,242,228,235,-1,247,235,239,-1,236,225,223,-1,223,234,236,-1,223,226,234,-1,234,233,251,-1,236,252,237,-1,253,252,236,-1,224,249,251,-1,254,241,242,-1,247,239,248,-1,255,256,257,-1,243,258,245,-1,240,222,200,-1,237,240,225,-1,234,259,236,-1,254,260,250,-1,246,245,261,-1,240,243,245,-1,247,242,235,-1,255,247,256,-1,234,251,259,-1,262,251,249,-1,248,230,232,-1,233,224,251,-1,255,257,264,-1,252,243,237,-1,242,255,254,-1,265,253,236,-1,224,244,249,-1,255,260,254,-1,232,222,245,-1,252,266,267,-1,265,268,253,-1,259,269,265,-1,255,264,260,-1,243,267,258,-1,259,265,236,-1,270,253,268,-1,251,262,259,-1,262,269,259,-1,243,252,267,-1,252,253,266,-1,267,272,258,-1,261,258,272,-1,269,268,265,-1,269,273,268,-1,273,269,262,-1,264,257,274,-1,246,247,232,-1,275,267,266,-1,273,262,271,-1,246,261,276,-1,255,242,247,-1,253,270,266,-1,275,266,273,-1,273,270,268,-1,262,249,263,-1,256,246,277,-1,245,258,261,-1,261,272,278,-1,273,266,270,-1,279,280,281,-1,256,282,257,-1,246,256,247,-1,267,283,272,-1,267,275,283,-1,261,278,284,-1,272,285,278,-1,286,277,287,-1,288,282,256,-1,279,289,275,-1,274,290,291,-1,288,256,277,-1,286,288,277,-1,292,279,281,-1,274,257,290,-1,288,293,282,-1,286,293,288,-1,294,286,287,-1,272,283,285,-1,282,293,290,-1,294,290,293,-1,293,286,294,-1,294,287,295,-1,246,287,277,-1,246,276,287,-1,279,275,273,-1,261,297,276,-1,279,273,280,-1,289,283,275,-1,273,271,280,-1,290,294,295,-1,289,285,283,-1,298,299,300,-1,297,261,284,-1,301,292,281,-1,291,300,302,-1,257,282,290,-1,295,291,290,-1,303,276,297,-1,279,304,289,-1,305,302,300,-1,285,289,304,-1,306,304,307,-1,276,298,287,-1,278,285,306,-1,299,309,300,-1,279,292,304,-1,305,300,309,-1,295,300,291,-1,285,304,306,-1,310,304,292,-1,309,308,305,-1,307,311,306,-1,278,306,284,-1,295,298,300,-1,310,292,301,-1,307,304,310,-1,312,309,313,-1,299,313,309,-1,311,314,306,-1,315,316,313,-1,306,314,284,-1,301,317,310,-1,314,311,318,-1,319,307,310,-1,314,321,284,-1,314,318,321,-1,307,318,311,-1,298,295,287,-1,321,318,319,-1,318,307,319,-1,322,297,284,-1,323,324,319,-1,320,312,313,-1,316,325,313,-1,301,296,317,-1,303,297,322,-1,326,303,322,-1,321,322,284,-1,327,325,316,-1,325,328,329,-1,316,315,330,-1,322,319,324,-1,331,326,332,-1,313,299,298,-1,303,315,313,-1,333,317,334,-1,335,336,337,-1,326,315,303,-1,317,333,310,-1,325,320,313,-1,338,323,319,-1,303,298,276,-1,326,331,315,-1,323,339,340,-1,326,322,324,-1,303,313,298,-1,322,321,319,-1,342,339,343,-1,344,328,345,-1,346,327,316,-1,347,348,330,-1,315,331,349,-1,324,323,350,-1,328,327,351,-1,315,349,330,-1,352,331,332,-1,350,323,340,-1,353,337,354,-1,330,349,347,-1,349,355,347,-1,355,349,352,-1,349,331,352,-1,352,332,356,-1,357,324,350,-1,358,357,350,-1,353,335,337,-1,335,316,336,-1,336,359,360,-1,359,330,348,-1,436,356,361,-1,332,326,324,-1,357,332,324,-1,357,362,363,-1,364,350,365,-1,366,365,340,-1,333,319,310,-1,336,360,337,-1,348,361,360,-1,356,369,361,-1,332,369,356,-1,363,332,357,-1,357,358,362,-1,358,350,364,-1,358,364,370,-1,365,350,340,-1,333,338,319,-1,329,328,344,-1,371,372,351,-1,335,346,316,-1,330,359,336,-1,359,348,360,-1,369,373,360,-1,369,360,361,-1,374,369,332,-1,370,375,376,-1,376,375,374,-1,376,358,370,-1,376,362,358,-1,376,363,362,-1,325,327,328,-1,351,377,378,-1,353,379,335,-1,316,330,336,-1,360,373,380,-1,374,373,369,-1,363,376,374,-1,363,374,332,-1,343,381,382,-1,383,384,385,-1,329,344,386,-1,387,371,346,-1,374,437,373,-1,390,370,365,-1,370,364,365,-1,366,340,391,-1,392,340,339,-1,340,392,391,-1,323,338,339,-1,328,393,345,-1,346,351,327,-1,351,372,377,-1,346,371,351,-1,387,394,395,-1,395,372,371,-1,387,395,371,-1,396,394,387,-1,337,380,354,-1,370,397,389,-1,390,397,370,-1,365,366,390,-1,398,391,342,-1,391,392,342,-1,338,343,339,-1,338,383,381,-1,386,368,329,-1,386,400,401,-1,386,344,400,-1,402,344,403,-1,402,400,344,-1,378,393,328,-1,378,328,351,-1,404,378,405,-1,377,405,378,-1,395,377,372,-1,439,395,394,-1,335,387,346,-1,380,337,360,-1,366,407,390,-1,407,366,391,-1,342,392,339,-1,402,408,400,-1,387,335,379,-1,353,409,379,-1,354,409,353,-1,410,391,398,-1,384,411,385,-1,412,413,384,-1,399,333,341,-1,402,403,414,-1,344,345,403,-1,393,404,415,-1,378,404,393,-1,406,416,415,-1,417,396,379,-1,417,409,418,-1,396,419,394,-1,417,379,409,-1,409,354,418,-1,407,391,410,-1,398,342,420,-1,421,342,343,-1,421,343,382,-1,399,383,338,-1,399,367,422,-1,343,338,381,-1,412,399,422,-1,399,338,333,-1,423,413,412,-1,415,416,393,-1,416,345,393,-1,396,387,379,-1,354,380,388,-1,385,411,426,-1,411,427,426,-1,383,385,428,-1,411,384,413,-1,412,384,399,-1,424,423,425,-1,414,429,431,-1,430,414,403,-1,429,414,430,-1,439,394,419,-1,426,428,385,-1,399,384,383,-1,432,433,424,-1,433,423,424,-1,433,413,423,-1,396,417,419,-1,354,388,418,-1,434,403,345,-1,70,440,65,-1,440,441,65,-1,441,442,65,-1,442,443,65,-1,443,444,65,-1,444,445,65,-1,445,446,65,-1,446,447,65,-1,447,448,65,-1,448,449,65,-1,449,450,65,-1,450,451,65,-1,451,452,65,-1,452,453,65,-1,453,454,65,-1,454,455,65,-1,455,456,65,-1,456,457,65,-1,457,458,65,-1,458,459,65,-1,462,463,461,-1,461,463,460,-1,460,463,459,-1,459,463,65,-1,329,368,325,-1,368,254,325,-1,325,254,320,-1,260,264,250,-1,274,291,264,-1,264,291,250,-1,291,302,250,-1,302,305,250,-1,305,312,250,-1,320,254,312,-1,250,312,254,-1,479,480,481,-1,482,483,484,-1,485,486,487,-1,483,480,484,-1,488,483,485,-1,488,485,487,-1,480,489,481,-1,490,480,491,-1,492,493,494,-1,486,485,482,-1,495,496,497,-1,495,497,498,-1,490,499,484,-1,483,489,480,-1,481,489,500,-1,479,491,480,-1,501,493,502,-1,494,493,501,-1,503,498,497,-1,504,497,505,-1,504,505,506,-1,485,483,482,-1,495,486,496,-1,492,494,507,-1,492,508,493,-1,509,510,507,-1,511,509,507,-1,504,506,512,-1,484,513,514,-1,507,510,515,-1,516,517,509,-1,509,511,516,-1,518,506,505,-1,506,518,519,-1,496,505,497,-1,492,507,515,-1,521,522,520,-1,522,517,520,-1,520,516,523,-1,520,517,516,-1,524,525,526,-1,525,527,528,-1,518,524,519,-1,514,529,482,-1,483,488,489,-1,502,491,501,-1,515,530,531,-1,533,534,535,-1,534,533,536,-1,486,482,496,-1,495,537,486,-1,484,499,513,-1,515,510,530,-1,533,539,536,-1,493,490,502,-1,492,540,508,-1,534,536,538,-1,542,527,543,-1,543,525,524,-1,544,536,545,-1,546,545,547,-1,542,543,505,-1,518,543,524,-1,490,484,480,-1,540,548,490,-1,493,508,490,-1,549,499,548,-1,550,540,541,-1,545,536,539,-1,542,539,527,-1,499,490,548,-1,502,490,491,-1,541,492,531,-1,527,539,533,-1,505,552,553,-1,549,548,554,-1,492,515,531,-1,544,538,536,-1,496,529,505,-1,496,482,529,-1,541,540,492,-1,551,544,545,-1,508,540,490,-1,545,539,542,-1,543,527,525,-1,514,482,484,-1,555,551,546,-1,514,556,529,-1,557,556,514,-1,513,557,514,-1,558,559,499,-1,549,554,560,-1,559,557,513,-1,559,513,499,-1,499,549,558,-1,542,505,553,-1,529,552,505,-1,557,559,563,-1,558,563,559,-1,560,554,564,-1,557,563,556,-1,554,550,565,-1,563,558,566,-1,541,532,562,-1,567,564,554,-1,568,550,541,-1,563,566,556,-1,569,570,561,-1,571,570,569,-1,556,573,529,-1,566,574,573,-1,548,540,554,-1,568,541,562,-1,850,561,570,-1,545,542,553,-1,549,560,558,-1,554,565,567,-1,568,565,550,-1,547,545,553,-1,569,575,576,-1,545,546,551,-1,543,518,505,-1,568,571,565,-1,556,566,573,-1,573,577,578,-1,560,566,558,-1,579,572,546,-1,579,547,580,-1,553,552,578,-1,574,581,573,-1,567,574,564,-1,573,581,577,-1,582,583,553,-1,529,573,552,-1,554,540,550,-1,569,565,571,-1,564,574,560,-1,576,567,565,-1,547,579,546,-1,584,585,586,-1,567,587,574,-1,572,579,591,-1,553,583,547,-1,592,553,578,-1,552,573,578,-1,592,582,553,-1,582,593,594,-1,566,560,574,-1,595,596,587,-1,569,576,565,-1,577,597,578,-1,584,581,574,-1,547,583,580,-1,577,581,599,-1,598,591,600,-1,580,600,591,-1,602,603,604,-1,577,599,597,-1,587,605,585,-1,597,606,592,-1,603,602,583,-1,583,582,603,-1,588,590,607,-1,604,594,608,-1,582,594,603,-1,593,609,610,-1,611,606,599,-1,579,580,591,-1,580,602,612,-1,610,613,593,-1,582,592,593,-1,578,597,592,-1,606,597,599,-1,601,595,587,-1,604,603,594,-1,596,605,587,-1,851,601,589,-1,593,611,609,-1,593,606,611,-1,574,587,585,-1,583,602,580,-1,593,608,594,-1,599,581,584,-1,584,611,599,-1,601,587,567,-1,600,580,612,-1,604,608,613,-1,584,574,585,-1,614,590,615,-1,586,617,618,-1,614,619,607,-1,614,607,590,-1,620,621,584,-1,586,605,617,-1,601,851,595,-1,576,601,567,-1,622,596,595,-1,623,614,615,-1,624,615,590,-1,625,616,612,-1,626,596,622,-1,627,623,628,-1,614,623,629,-1,628,623,615,-1,630,631,632,-1,633,628,630,-1,630,615,634,-1,625,612,602,-1,604,625,602,-1,586,620,584,-1,596,626,617,-1,632,635,626,-1,630,632,636,-1,630,628,615,-1,596,617,605,-1,638,639,631,-1,637,624,590,-1,625,641,616,-1,593,613,608,-1,634,615,624,-1,631,634,642,-1,631,630,634,-1,643,642,644,-1,646,625,604,-1,609,647,610,-1,626,648,617,-1,635,631,639,-1,632,631,635,-1,641,625,646,-1,646,649,650,-1,626,635,648,-1,651,638,652,-1,638,651,639,-1,653,643,644,-1,634,645,644,-1,644,642,634,-1,638,631,642,-1,652,654,655,-1,634,624,645,-1,641,656,657,-1,656,658,657,-1,648,659,618,-1,660,648,635,-1,660,659,648,-1,659,660,661,-1,643,662,663,-1,643,653,662,-1,849,655,665,-1,666,655,654,-1,651,652,655,-1,638,662,652,-1,655,667,665,-1,666,667,655,-1,662,668,652,-1,641,657,640,-1,669,670,649,-1,671,659,667,-1,659,671,672,-1,648,618,617,-1,672,673,620,-1,656,641,650,-1,674,656,650,-1,610,646,613,-1,586,618,620,-1,675,654,676,-1,849,651,655,-1,652,668,654,-1,668,664,677,-1,662,653,668,-1,641,640,616,-1,650,641,646,-1,669,678,670,-1,610,647,669,-1,646,669,649,-1,618,672,620,-1,671,667,666,-1,679,671,666,-1,675,666,654,-1,668,653,664,-1,610,669,646,-1,646,604,613,-1,679,666,675,-1,680,677,681,-1,675,676,682,-1,649,684,650,-1,685,686,647,-1,584,621,611,-1,585,605,586,-1,659,672,618,-1,676,687,680,-1,676,654,687,-1,688,683,656,-1,688,656,689,-1,656,674,689,-1,684,674,650,-1,678,686,685,-1,671,673,672,-1,690,691,692,-1,693,677,664,-1,692,682,676,-1,695,680,687,-1,674,696,689,-1,669,647,686,-1,621,697,609,-1,621,609,611,-1,621,620,697,-1,698,620,673,-1,699,700,670,-1,697,685,609,-1,682,692,679,-1,692,676,680,-1,680,695,677,-1,690,692,680,-1,693,681,677,-1,593,592,606,-1,671,702,673,-1,703,690,680,-1,674,684,696,-1,649,705,684,-1,702,671,679,-1,706,707,703,-1,703,707,708,-1,709,710,711,-1,670,712,649,-1,713,678,685,-1,714,715,716,-1,703,680,704,-1,694,696,701,-1,694,689,696,-1,685,647,609,-1,691,717,702,-1,706,703,704,-1,696,710,701,-1,700,699,718,-1,649,712,705,-1,670,713,719,-1,698,673,702,-1,698,702,717,-1,707,720,708,-1,710,696,711,-1,705,712,700,-1,669,686,678,-1,692,702,679,-1,680,681,704,-1,721,722,711,-1,709,711,722,-1,700,718,705,-1,711,696,684,-1,700,712,670,-1,692,691,702,-1,691,690,723,-1,724,708,725,-1,726,727,711,-1,713,728,719,-1,620,729,697,-1,690,703,708,-1,730,727,719,-1,718,726,711,-1,718,684,705,-1,721,711,727,-1,699,726,718,-1,719,699,670,-1,678,713,670,-1,729,685,697,-1,725,708,720,-1,718,711,684,-1,731,717,723,-1,690,732,723,-1,733,713,685,-1,734,698,717,-1,731,735,736,-1,691,723,717,-1,690,708,724,-1,728,739,719,-1,733,741,728,-1,733,742,741,-1,698,714,743,-1,744,715,745,-1,714,698,715,-1,734,736,745,-1,731,736,734,-1,731,723,735,-1,726,699,719,-1,717,731,734,-1,724,738,732,-1,740,746,747,-1,722,721,740,-1,726,719,727,-1,729,733,685,-1,742,743,714,-1,620,698,729,-1,715,734,745,-1,748,744,745,-1,749,750,732,-1,740,721,746,-1,751,746,721,-1,735,748,736,-1,751,721,727,-1,752,730,753,-1,730,754,753,-1,748,745,736,-1,749,732,738,-1,727,730,752,-1,739,730,719,-1,713,733,728,-1,756,716,744,-1,723,750,735,-1,690,724,732,-1,746,757,758,-1,759,751,752,-1,751,727,752,-1,739,728,741,-1,714,716,756,-1,715,698,734,-1,723,732,750,-1,738,737,755,-1,733,743,742,-1,760,742,714,-1,759,752,763,-1,735,750,749,-1,759,762,757,-1,746,751,757,-1,751,759,757,-1,754,764,753,-1,733,729,743,-1,744,748,765,-1,749,738,755,-1,730,739,754,-1,698,743,729,-1,766,735,749,-1,763,752,753,-1,739,767,754,-1,765,768,756,-1,759,769,762,-1,770,771,754,-1,742,760,741,-1,756,744,765,-1,766,768,765,-1,765,748,735,-1,766,755,761,-1,772,770,760,-1,744,716,715,-1,755,766,749,-1,766,765,735,-1,760,770,741,-1,764,754,773,-1,774,773,775,-1,773,754,775,-1,739,741,767,-1,770,767,741,-1,767,770,754,-1,769,776,777,-1,761,778,779,-1,766,779,768,-1,774,780,776,-1,753,764,763,-1,775,771,781,-1,756,760,714,-1,759,763,769,-1,771,775,754,-1,774,776,769,-1,780,774,775,-1,772,771,770,-1,768,782,756,-1,779,782,768,-1,761,783,778,-1,764,773,774,-1,763,774,769,-1,778,783,785,-1,763,764,774,-1,756,786,760,-1,761,779,766,-1,784,776,787,-1,786,771,772,-1,788,789,790,-1,791,779,792,-1,793,792,778,-1,792,779,778,-1,776,780,787,-1,780,775,794,-1,795,786,782,-1,778,785,796,-1,796,797,793,-1,796,793,778,-1,799,787,780,-1,782,786,756,-1,791,800,782,-1,801,787,802,-1,791,803,800,-1,793,803,792,-1,779,791,782,-1,791,792,803,-1,803,793,797,-1,796,785,798,-1,806,807,808,-1,787,799,802,-1,788,810,811,-1,788,811,812,-1,812,807,806,-1,794,799,780,-1,802,806,809,-1,794,806,799,-1,812,794,789,-1,786,813,781,-1,814,795,800,-1,800,803,797,-1,794,775,815,-1,786,772,760,-1,795,813,786,-1,816,817,818,-1,806,802,799,-1,794,812,806,-1,794,815,789,-1,775,781,815,-1,813,819,781,-1,813,820,819,-1,800,795,782,-1,798,821,816,-1,812,811,822,-1,812,822,804,-1,786,781,771,-1,821,823,816,-1,824,825,805,-1,796,798,816,-1,812,804,807,-1,816,814,800,-1,800,797,816,-1,788,812,789,-1,826,827,828,-1,824,805,822,-1,829,810,788,-1,795,814,813,-1,811,831,822,-1,788,790,832,-1,789,781,819,-1,835,825,824,-1,824,831,829,-1,811,810,831,-1,789,819,830,-1,831,824,822,-1,831,810,829,-1,827,826,817,-1,817,816,823,-1,836,834,825,-1,824,837,838,-1,816,818,814,-1,826,839,840,-1,797,796,816,-1,835,836,825,-1,835,824,838,-1,837,824,829,-1,837,829,788,-1,833,841,842,-1,835,843,836,-1,844,845,838,-1,789,815,781,-1,814,818,813,-1,842,827,817,-1,842,817,823,-1,817,826,840,-1,837,844,838,-1,789,830,790,-1,842,823,833,-1,846,844,837,-1,832,846,837,-1,832,837,788,-1,839,826,828,-1,847,820,818,-1,817,840,818,-1,818,820,813,-1,840,848,818,-1,848,847,818,-1,854,852,853,-1,855,856,857,-1,858,859,860,-1,861,862,863,-1,866,867,865,-1,865,867,864,-1,867,868,864,-1,874,875,873,-1,869,870,877,-1,870,871,877,-1,876,877,875,-1,875,877,873,-1,871,872,877,-1,873,877,872,-1,879,880,878,-1,878,880,882,-1,881,882,880,-1,883,884,885,-1,886,887,888,-1,889,890,891,-1,892,893,894,-1,895,896,897,-1,898,899,900,-1,901,902,903,-1,904,905,906,-1,907,908,909,-1,910,911,912,-1,913,914,915,-1,916,917,918,-1,919,920,921,-1,922,923,924,-1,925,926,927,-1,928,929,930,-1,931,932,933,-1,934,935,936,-1,937,938,939,-1,940,941,942,-1,943,944,945,-1,946,947,948,-1,949,950,951,-1,952,953,954,-1,955,956,957,-1,958,959,960,-1,961,962,963,-1,964,965,966,-1,967,968,969,-1,970,971,972,-1,973,974,975,-1,976,977,978,-1,979,980,981,-1,982,983,984,-1,985,986,987,-1,988,989,990,-1,991,992,993,-1,994,995,996,-1,997,998,999,-1,1000,1001,1002,-1,1003,1004,1005,-1,1006,1007,1008,-1,1009,1010,1011,-1,1012,1013,1014,-1,1015,1016,1017,-1,1018,1019,1020,-1,1021,1022,1023,-1,1024,1025,1026,-1,1027,1028,1029,-1,1030,1031,1032,-1,1033,1034,1035,-1,1036,1037,1038,-1,1039,1040,1041,-1,1042,1043,1044,-1,1045,1046,1047,-1,1048,1049,1050,-1,1051,1052,1053,-1,1054,1055,1056,-1,1057,1058,1059,-1,1060,1061,1062,-1,1063,1064,1065,-1,1066,1067,1068,-1,1069,1070,1071,-1,1072,1073,1074,-1,1075,1076,1077,-1,1078,1079,1080,-1,1081,1082,1083,-1,1084,1085,1086,-1,1087,1088,1089,-1,1090,1091,1092,-1,1093,1094,1095,-1,1096,1097,1098,-1,1099,1100,1101,-1,1102,1103,1104,-1,1105,1106,1107,-1,1108,1109,1110,-1,1111,1112,1113,-1,1114,1115,1116,-1,1117,1118,1119,-1,1120,1121,1122,-1,1123,1124,1125,-1,1126,1127,1128,-1,1129,1130,1131,-1,1132,1133,1134,-1,1135,1136,1137,-1,1138,1139,1140,-1,1141,1142,1143,-1,1144,1145,1146,-1,1147,1148,1149,-1,1150,1151,1152,-1,1153,1154,1155,-1,1156,1157,1158,-1,1159,1160,1161,-1,1162,1163,1164,-1,1165,1166,1167,-1,1168,1169,1170,-1,1171,1172,1173,-1,1174,1175,1176,-1,1177,1178,1179,-1,1180,1181,1182,-1,1183,1184,1185,-1,1186,1187,1188,-1,1189,1190,1191,-1,1192,1193,1194,-1,1195,1196,1197,-1,1198,1199,1200,-1,1201,1202,1203,-1,1204,1205,1206,-1,1207,1208,1209,-1,1210,1211,1212,-1,1213,1214,1215,-1,1216,1217,1218,-1,1219,1220,1221,-1,1222,1223,1224,-1,1225,1226,1227,-1,1228,1229,1230,-1,1231,1232,1233,-1,1234,1235,1236,-1,1237,1238,1239,-1,1240,1241,1242,-1,1243,1244,1245,-1,1246,1247,1248,-1,1249,1250,1251,-1,1252,1253,1254,-1,1255,1256,1257,-1,1258,1259,1260,-1,1261,1262,1263,-1,1264,1265,1266,-1,1267,1268,1269,-1,1270,1271,1272,-1,1273,1274,1275,-1,1276,1277,1278,-1,1279,1280,1281,-1,1282,1283,1284,-1,1285,1286,1287,-1,1288,1289,1290,-1,1291,1292,1293,-1,1294,1295,1296,-1,1297,1298,1299,-1,1300,1301,1302,-1,1303,1304,1305,-1,1306,1307,1308,-1,1309,1310,1311,-1,1312,1313,1314,-1,1315,1316,1317,-1,1318,1319,1320,-1,1321,1322,1323,-1,1324,1325,1326,-1,1327,1328,1329,-1,1330,1331,1332,-1,1333,1334,1335,-1,1336,1337,1338,-1,1339,1340,1341,-1,1342,1343,1344,-1,1345,1346,1347,-1,1348,1349,1350,-1,1351,1352,1353,-1,1354,1355,1356,-1,1357,1358,1359,-1,1360,1361,1362,-1,1363,1364,1365,-1,1366,1367,1368,-1,1369,1370,1371,-1,1372,1373,1374,-1,1375,1376,1377,-1,1378,1379,1380,-1,1381,1382,1383,-1,1384,1385,1386,-1,1387,1388,1389,-1,1390,1391,1392,-1,1393,1394,1395,-1,1396,1397,1398,-1,1399,1400,1401,-1,1402,1403,1404,-1,1405,1406,1407,-1,1408,1409,1410,-1,1411,1412,1413,-1,1414,1415,1416,-1,1417,1418,1419,-1,1420,1421,1422,-1,1423,1424,1425,-1,1426,1427,1428,-1,1429,1430,1431,-1,1432,1433,1434,-1,1435,1436,1437,-1,1438,1439,1440,-1,1441,1442,1443,-1,1444,1445,1446,-1,1447,1448,1449,-1,1450,1451,1452,-1,1453,1454,1455,-1,1456,1457,1458,-1,1459,1460,1461,-1,1462,1463,1464,-1,1465,1466,1467,-1,1468,1469,1470,-1,1471,1472,1473,-1,1474,1475,1476,-1,1477,1478,1479,-1,1480,1481,1482,-1,1483,1484,1485,-1,1486,1487,1488,-1,1489,1490,1491,-1,1492,1493,1494,-1,1495,1496,1497,-1,1498,1499,1500,-1,1501,1502,1503,-1,1504,1505,1506,-1,1507,1508,1509,-1,1510,1511,1512,-1,1513,1514,1515,-1,1516,1517,1518,-1,1519,1520,1521,-1,1522,1523,1524,-1,1525,1526,1527,-1,1528,1529,1530,-1,1531,1532,1533,-1,1534,1535,1536,-1,1537,1538,1539,-1,1540,1541,1542,-1,1543,1544,1545,-1,1546,1547,1548,-1,1549,1550,1551,-1,1552,1553,1554,-1,1555,1556,1557,-1,1558,1559,1560,-1,1561,1562,1563,-1,1564,1565,1566,-1,1567,1568,1569,-1,1570,1571,1572,-1,1573,1574,1575,-1,1576,1577,1578,-1,1579,1580,1581,-1,1582,1583,1584,-1,1585,1586,1587,-1,1588,1589,1590,-1,1591,1592,1593,-1,1594,1595,1596,-1,1597,1598,1599,-1,1600,1601,1602,-1,1603,1604,1605,-1,1606,1607,1608,-1,1609,1610,1611,-1,1612,1613,1614,-1,1615,1616,1617,-1,1618,1619,1620,-1,1621,1622,1623,-1,1624,1625,1626,-1,1627,1628,1629,-1,1630,1631,1632,-1,1633,1634,1635,-1,1636,1637,1638,-1,1639,1640,1641,-1,1642,1643,1644,-1,1645,1646,1647,-1,1648,1649,1650,-1,1651,1652,1653,-1,1654,1655,1656,-1,1657,1658,1659,-1,1660,1661,1662,-1,1663,1664,1665,-1,1666,1667,1668,-1,1669,1670,1671,-1,1672,1673,1674,-1,1675,1676,1677,-1,1678,1679,1680,-1,1681,1682,1683,-1,1684,1685,1686,-1,1687,1688,1689,-1,1690,1691,1692,-1,1693,1694,1695,-1,1696,1697,1698,-1,1699,1700,1701,-1,1702,1703,1704,-1,1705,1706,1707,-1,1708,1709,1710,-1,1711,1712,1713,-1,1714,1715,1716,-1,1717,1718,1719,-1,1720,1721,1722,-1,1723,1724,1725,-1,1726,1727,1728,-1,1729,1730,1731,-1,1732,1733,1734,-1,1735,1736,1737,-1,1738,1739,1740,-1,1741,1742,1743,-1,1744,1745,1746,-1,1747,1748,1749,-1,1750,1751,1752,-1,1753,1754,1755,-1,1756,1757,1758,-1,1759,1760,1761,-1,1762,1763,1764,-1,1765,1766,1767,-1,1768,1769,1770,-1,1771,1772,1773,-1,1774,1775,1776,-1,1777,1778,1779,-1,1780,1781,1782,-1,1783,1784,1785,-1,1786,1787,1788,-1,1789,1790,1791,-1,1792,1793,1794,-1,1795,1796,1797,-1,1798,1799,1800,-1,1801,1802,1803,-1,1804,1805,1806,-1,1807,1808,1809,-1,1810,1811,1812,-1,1813,1814,1815,-1,1816,1817,1818,-1,1819,1820,1821,-1,1822,1823,1824,-1,1825,1826,1827,-1,1828,1829,1830,-1,1831,1832,1833,-1,1834,1835,1836,-1,1837,1838,1839,-1,1840,1841,1842,-1,1843,1844,1845,-1,1846,1847,1848,-1,1849,1850,1851,-1,1852,1853,1854,-1,1855,1856,1857,-1,1858,1859,1860,-1,1861,1862,1863,-1,1864,1865,1866,-1,1867,1868,1869,-1,1870,1871,1872,-1,1873,1874,1875,-1,1876,1877,1878,-1,1879,1880,1881,-1,1882,1883,1884,-1,1885,1886,1887,-1,1888,1889,1890,-1,1891,1892,1893,-1,1894,1895,1896,-1,1897,1898,1899,-1,1900,1901,1902,-1,1903,1904,1905,-1,1906,1907,1908,-1,1909,1910,1911,-1,1912,1913,1914,-1,1915,1916,1917,-1,1918,1919,1920,-1,1921,1922,1923,-1,1924,1925,1926,-1,1927,1928,1929,-1,1930,1931,1932,-1,1933,1934,1935,-1,1936,1937,1938,-1,1939,1940,1941,-1,1942,1943,1944,-1,1945,1946,1947,-1,1948,1949,1950,-1,1951,1952,1953,-1,1954,1955,1956,-1,1957,1958,1959,-1,1960,1961,1962,-1,1963,1964,1965,-1,1966,1967,1968,-1,1969,1970,1971,-1,1972,1973,1974,-1,1975,1976,1977,-1,1978,1979,1980,-1,1981,1982,1983,-1,1984,1985,1986,-1,1987,1988,1989,-1,1990,1991,1992,-1,1993,1994,1995,-1,1996,1997,1998,-1,1999,2000,2001,-1,2002,2003,2004,-1,2005,2006,2007,-1,2008,2009,2010,-1,2011,2012,2013,-1,2014,2015,2016,-1,2017,2018,2019,-1,2020,2021,2022,-1,2023,2024,2025,-1,2026,2027,2028,-1,2029,2030,2031,-1,2032,2033,2034,-1,2035,2036,2037,-1,2038,2039,2040,-1,2041,2042,2043,-1,2044,2045,2046,-1,2047,2048,2049,-1,2050,2051,2052,-1,2053,2054,2055,-1,2056,2057,2058,-1,2059,2060,2061,-1,2062,2063,2064,-1,2065,2066,2067,-1,2068,2069,2070,-1,2071,2072,2073,-1,2074,2075,2076,-1,2077,2078,2079,-1,2080,2081,2082,-1,2083,2084,2085,-1,2086,2087,2088,-1,2089,2090,2091,-1,2092,2093,2094,-1,2095,2096,2097,-1,2098,2099,2100,-1,2101,2102,2103,-1,2104,2105,2106,-1,2107,2108,2109,-1,2110,2111,2112,-1,2113,2114,2115,-1,2116,2117,2118,-1,2119,2120,2121,-1,2122,2123,2124,-1,2125,2126,2127,-1,2128,2129,2130,-1,2131,2132,2133,-1,2134,2135,2136,-1,2137,2138,2139,-1,2140,2141,2142,-1,2143,2144,2145,-1,2146,2147,2148,-1,2149,2150,2151,-1,2152,2153,2154,-1,2155,2156,2157,-1,2158,2159,2160,-1,2161,2162,2163,-1,2164,2165,2166,-1,2167,2168,2169,-1,2170,2171,2172,-1,2173,2174,2175,-1,2176,2177,2178,-1,2179,2180,2181,-1,2182,2183,2184,-1,2185,2186,2187,-1,2188,2189,2190,-1,2191,2192,2193,-1,2194,2195,2196,-1,2197,2198,2199,-1,2200,2201,2202,-1,2203,2204,2205,-1,2206,2207,2208,-1,2209,2210,2211,-1,2212,2213,2214,-1,2215,2216,2217,-1,2218,2219,2220,-1,2221,2222,2223,-1,2224,2225,2226,-1,2227,2228,2229,-1,2230,2231,2232,-1,2233,2234,2235,-1,2236,2237,2238,-1,2239,2240,2241,-1,2242,2243,2244,-1,2245,2246,2247,-1,2248,2249,2250,-1,2251,2252,2253,-1,2254,2255,2256,-1,2257,2258,2259,-1,2260,2261,2262,-1,2263,2264,2265,-1,2266,2267,2268,-1,2269,2270,2271,-1,2272,2273,2274,-1,2275,2276,2277,-1,2278,2279,2280,-1,2281,2282,2283,-1,2284,2285,2286,-1,2287,2288,2289,-1,2290,2291,2292,-1,2293,2294,2295,-1,2296,2297,2298,-1,2299,2300,2301,-1,2302,2303,2304,-1,2305,2306,2307,-1,2308,2309,2310,-1,2311,2312,2313,-1,2314,2315,2316,-1,2317,2318,2319,-1,2320,2321,2322,-1,2323,2324,2325,-1,2326,2327,2328,-1,2329,2330,2331,-1,2332,2333,2334,-1,2335,2336,2337,-1,2338,2339,2340,-1,2341,2342,2343,-1,2344,2345,2346,-1,2347,2348,2349,-1,2350,2351,2352,-1,2353,2354,2355,-1,2356,2357,2358,-1,2359,2360,2361,-1,2362,2363,2364,-1,2365,2366,2367,-1,2368,2369,2370,-1,2371,2372,2373,-1,2374,2375,2376,-1,2377,2378,2379,-1,2380,2381,2382,-1,2383,2384,2385,-1,2386,2387,2388,-1,2389,2390,2391,-1,2392,2393,2394,-1,2395,2396,2397,-1,2398,2399,2400,-1,2401,2402,2403,-1,2404,2405,2406,-1,2407,2408,2409,-1,2410,2411,2412,-1,2413,2414,2415,-1,2416,2417,2418,-1,2419,2420,2421,-1,2422,2423,2424,-1,2425,2426,2427,-1,2428,2429,2430,-1,2431,2432,2433,-1,2434,2435,2436,-1,2437,2438,2439,-1,2440,2441,2442,-1,2443,2444,2445,-1,2446,2447,2448,-1,2449,2450,2451,-1,2452,2453,2454,-1,2455,2456,2457,-1,2458,2459,2460,-1,2461,2462,2463,-1,2464,2465,2466,-1,2467,2468,2469,-1,2470,2471,2472,-1,2473,2474,2475,-1,2476,2477,2478,-1,2479,2480,2481,-1,2482,2483,2484,-1,2485,2486,2487,-1,2488,2489,2490,-1,2491,2492,2493,-1,2494,2495,2496,-1,2497,2498,2499,-1,2500,2501,2502,-1,2503,2504,2505,-1,2506,2507,2508,-1,2509,2510,2511,-1,2512,2513,2514,-1,2515,2516,2517,-1,2518,2519,2520,-1,2521,2522,2523,-1,2524,2525,2526,-1,2527,2528,2529,-1,2530,2531,2532,-1,2533,2534,2535,-1,2536,2537,2538,-1,2539,2540,2541,-1,2542,2543,2544,-1,2545,2546,2551,-1,2550,2551,2549,-1,2551,2546,2549,-1,2549,2546,2548,-1,2547,2548,2546,-1,2555,2552,2554,-1,2553,2554,2552,-1,2567,2568,2566,-1,2568,2556,2566,-1,2566,2556,2565,-1,2558,2559,2557,-1,2560,2561,2559,-1,2559,2561,2557,-1,2561,2562,2557,-1,2562,2563,2557,-1,2563,2564,2557,-1,2565,2556,2564,-1,2557,2564,2556,-1,2570,2571,2569,-1,2571,2572,2569,-1,2572,2573,2569,-1,2573,2574,2569,-1,2574,2575,2569,-1,2575,2576,2569,-1,2576,2577,2569,-1,2577,2578,2569,-1,2578,2579,2569,-1,2579,2580,2569,-1,2580,2581,2569,-1,2581,2582,2569,-1,2582,2583,2569,-1,2583,2584,2569,-1,2584,2585,2569,-1,2585,2586,2569,-1,2586,2587,2569,-1,2587,2588,2569,-1,2612,2613,2614,-1,2615,2616,2617,-1,2618,2619,2620,-1,2633,2634,2632,-1,2634,2635,2632,-1,2636,2637,2635,-1,2638,2639,2637,-1,2639,2640,2637,-1,2642,2643,2641,-1,2623,2624,2622,-1,2628,2629,2627,-1,2630,2631,2629,-1,2631,2632,2629,-1,2629,2632,2627,-1,2632,2635,2627,-1,2627,2635,2626,-1,2635,2637,2626,-1,2637,2640,2626,-1,2643,2621,2641,-1,2626,2640,2625,-1,2640,2641,2625,-1,2641,2621,2625,-1,2624,2625,2622,-1,2622,2625,2621,-1,2656,2657,2658,-1,2659,2660,2661,-1,2662,2663,2664,-1,2665,2666,2667,-1,2668,2669,2670,-1,2671,2672,2673,-1,2674,2675,2676,-1,2677,2678,2679,-1,2682,2683,2681,-1,2685,2686,2684,-1,2686,2687,2684,-1,2687,2688,2684,-1,2689,2690,2688,-1,2694,2695,2693,-1,2695,2696,2693,-1,2696,2697,2693,-1,2701,2702,2700,-1,2680,2681,2702,-1,2684,2688,2683,-1,2688,2690,2683,-1,2683,2690,2681,-1,2690,2691,2681,-1,2691,2692,2681,-1,2692,2693,2681,-1,2697,2698,2693,-1,2681,2693,2702,-1,2698,2699,2693,-1,2702,2693,2700,-1,2699,2700,2693,-1,2860,2861,2862,-1,2872,2873,2871,-1,2871,2873,2870,-1,2870,2873,2869,-1,2875,2876,2874,-1,2878,2879,2877,-1,2880,2881,2879,-1,2882,2883,2881,-1,2885,2863,2884,-1,2864,2865,2863,-1,2866,2867,2865,-1,2868,2869,2867,-1,2869,2873,2867,-1,2876,2877,2874,-1,2879,2881,2877,-1,2881,2883,2877,-1,2883,2884,2877,-1,2865,2867,2863,-1,2867,2873,2863,-1,2873,2874,2863,-1,2863,2874,2884,-1,2877,2884,2874,-1,2926,2677,2927,-1,2679,2858,2677,-1,2858,2857,2677,-1,2677,2857,2927,-1,2857,2852,2927,-1,2852,2851,2927,-1,2851,2850,2927,-1,2848,2861,2849,-1,2848,2847,2860,-1,2846,2789,2847,-1,2789,2788,2847,-1,2849,2861,2850,-1,2860,2847,2861,-1,2788,2927,2847,-1,2850,2861,2927,-1,2847,2927,2861,-1,3021,3022,3023,-1,3024,3025,3026,-1,3027,3028,3029,-1,3030,3031,3032,-1,3033,3034,3035,-1,3036,3037,3038,-1,3039,3040,3041,-1,3042,3043,3044,-1,3045,3046,3047,-1,3048,3049,3050,-1,3051,3052,3053,-1,3054,3055,3056,-1,3057,3058,3059,-1,3060,3061,3062,-1,3063,3064,3065,-1,3066,3067,3068,-1,3069,3070,3071,-1,3072,3073,3074,-1,3025,3024,3023,-1,2,2859,3040,-1,2858,2679,2859,-1,3023,3024,3021,-1,3021,3024,3022,-1,3022,3024,3023,-1,3023,3024,2679,-1,2679,3024,2859,-1,3040,2859,3037,-1,3037,2859,3038,-1,3035,3038,3033,-1,3038,2859,3033,-1,3033,2859,3031,-1,3031,2859,3032,-1,2859,3024,3032,-1,3024,3028,3032,-1,3027,3032,3028,-1,3075,3076,3077,-1,3078,3079,3080,-1,3081,3082,3083,-1,3084,3085,3086,-1,3087,3088,3089,-1,3090,3091,3092,-1,2614,2616,2612,-1,2618,2654,2619,-1,2657,2656,2653,-1,2653,2652,2656,-1,2651,2650,2652,-1,2649,2661,2650,-1,2612,2616,2569,-1,2619,2654,2615,-1,2653,2656,2654,-1,2652,2650,2656,-1,2661,1,2650,-1,1,2570,2650,-1,2569,2616,2570,-1,2654,2656,2615,-1,2656,2650,2615,-1,2570,2616,2650,-1,2615,2650,2616,-1,2675,2671,2611,-1,2672,2670,2671,-1,2611,2671,2569,-1,2671,2670,2569,-1,2569,2670,2614,-1,2670,3091,2614,-1,2614,3091,2616,-1,3091,3087,2616,-1,3093,3094,3095,-1,3096,3097,3098,-1,3099,3100,3101,-1,3102,3103,3104,-1,3105,3106,3107,-1,3108,3109,3110,-1,3111,3112,3113,-1,3114,3115,3116,-1,3117,3118,3119,-1,3120,3121,3122,-1,3123,3124,3125,-1,3126,3127,3128,-1,3129,3130,3131,-1,3132,3133,3134,-1,3135,3136,3137,-1,3138,3139,3140,-1,3141,3142,3143,-1,3144,3145,3146,-1,3147,3148,3149,-1,3150,3151,3152,-1,3153,3154,3155,-1,3156,3157,3158,-1,3159,3160,3161,-1,3162,3163,3164,-1,3165,3166,3167,-1,3168,3169,3170,-1,3171,3172,3173,-1,3174,3175,3176,-1,3177,3178,3179,-1,3180,3181,3182,-1,3183,3184,3185,-1,3186,3187,3188,-1,3189,3190,3191,-1,3192,3193,3194,-1,3195,3196,3197,-1,3198,3199,3200,-1,3201,3202,3203,-1,3204,3205,3206,-1,3207,3208,3209,-1,3210,3211,3212,-1,3213,3214,3215,-1,3216,3217,3218,-1,3219,3220,3221,-1,3222,3223,3224,-1,3225,3226,3227,-1,3228,3229,3230,-1,3231,3232,3233,-1,3234,3235,3236,-1,3237,3238,3239,-1,3240,3241,3242,-1,3243,3244,3245,-1,3246,3247,3248,-1,3249,3250,3251,-1,3252,3253,3254,-1,3255,3256,3257,-1,3258,3259,3260,-1,3261,3262,3263,-1,3264,3265,3266,-1,3267,3268,3269,-1,3270,3271,3272,-1,3273,3274,3275,-1,3276,3277,3278,-1,3279,3280,3281,-1,3282,3283,3284,-1,3285,3286,3287,-1,3288,3289,3290,-1,3291,3292,3293,-1,3294,3295,3296,-1,3297,3298,3299,-1,3300,3301,3302,-1,3303,3304,3305,-1,3306,3307,3308,-1,3309,3310,3311,-1,3312,3313,3314,-1,3315,3316,3317,-1,3318,3319,3320,-1,3321,3322,3323,-1,3324,3325,3326,-1,3327,3328,3329,-1,3330,3331,3332,-1,3333,3334,3335,-1,3336,3337,3338,-1,3339,3340,3341,-1,3342,3343,3344,-1,3345,3346,3347,-1,3348,3349,3350,-1,3351,3352,3353,-1,3354,3355,3356,-1,3357,3358,3359,-1,3360,3361,3362,-1,3363,3364,3365,-1,3366,3367,3368,-1,3369,3370,3371,-1,3372,3373,3374,-1,3375,3376,3377,-1,3378,3379,3380,-1,3381,3382,3383,-1,3384,3385,3386,-1,3387,3388,3389,-1,3390,3391,3392,-1,3393,3394,3395,-1,3396,3397,3398,-1,3399,3400,3401,-1,3402,3403,3404,-1,3405,3406,3407,-1,3408,3409,3410,-1,3411,3412,3413,-1,3414,3415,3416,-1,3417,3418,3419,-1,3420,3421,3422,-1,3423,3424,3425,-1,3426,3427,3428,-1,3429,3430,3431,-1,3432,3433,3434,-1,3435,3436,3437,-1,3438,3439,3440,-1,3441,3442,3443,-1,3444,3445,3446,-1,3447,3448,3449,-1,3450,3451,3452,-1,3453,3454,3455,-1,3456,3457,3458,-1,3459,3460,3461,-1,3462,3463,3464,-1,3465,3466,3467,-1,3468,3469,3470,-1,3471,3472,3473,-1,3474,3475,3476,-1,3477,3478,3479,-1,3480,3481,3482,-1,3483,3484,3485,-1,3486,3487,3488,-1,3489,3490,3491,-1,3492,3493,3494,-1,3495,3496,3497,-1,3498,3499,3500,-1,3501,3502,3503,-1,3504,3505,3506,-1,3507,3508,3509,-1,3510,3511,3512,-1,3513,3514,3515,-1,3516,3517,3518,-1,3519,3520,3521,-1,3522,3523,3524,-1,3525,3526,3527,-1,3528,3529,3530,-1,3531,3532,3533,-1,3534,3535,3536,-1,3537,3538,3539,-1,3540,3541,3542,-1,3543,3544,3545,-1,3546,3547,3548,-1,3549,3550,3551,-1,3552,3553,3554,-1,3555,3556,3557,-1,3558,3559,3560,-1,3561,3562,3563,-1,3564,3565,3566,-1,3567,3568,3569,-1,3570,3571,3572,-1,3573,3574,3575,-1,3576,3577,3578,-1,3579,3580,3581,-1,3582,3583,3584,-1,3585,3586,3587,-1,3588,3589,3590,-1,3591,3592,3593,-1,3594,3595,3596,-1,3597,3598,3599,-1,3600,3601,3602,-1,3603,3604,3605,-1,3606,3607,3608,-1,3609,3610,3611,-1,3612,3613,3614,-1,3615,3616,3617,-1,3618,3619,3620,-1,3621,3622,3623,-1,3624,3625,3626,-1,3627,3628,3629,-1,3630,3631,3632,-1,3633,3634,3635,-1,3636,3637,3638,-1,3639,3640,3641,-1,3642,3643,3644,-1,3645,3646,3647,-1,3648,3649,3650,-1,3651,3652,3653,-1,3654,3655,3656,-1,3657,3658,3659,-1,3660,3661,3662,-1,3663,3664,3665,-1,3666,3667,3668,-1,3669,3670,3671,-1,3672,3673,3674,-1,3675,3676,3677,-1,3678,3679,3680,-1,3681,3682,3683,-1,3684,3685,3686,-1,3687,3688,3689,-1,3690,3691,3692,-1,3693,3694,3695,-1,3696,3697,3698,-1,3699,3700,3701,-1,3702,3703,3704,-1,3705,3706,3707,-1,3708,3709,3710,-1,3711,3712,3713,-1,3714,3715,3716,-1,3717,3718,3719,-1,3720,3721,3722,-1,3723,3724,3725,-1,3726,3727,3728,-1,3729,3730,3731,-1,3732,3733,3734,-1,3735,3736,3737,-1,3738,3739,3740,-1,3741,3742,3743,-1,3744,3745,3746,-1,3747,3748,3749,-1,3750,3751,3752,-1,3753,3754,3755,-1,3756,3757,3758,-1,3759,3760,3761,-1,3762,3763,3764,-1,3765,3766,3767,-1,3768,3769,3770,-1,3771,3772,3773,-1,3774,3775,3776,-1,3777,3778,3779,-1,3780,3781,3782,-1,3783,3784,3785,-1,3786,3787,3788,-1,3789,3790,3791,-1,3792,3793,3794,-1,3795,3796,3797,-1,3798,3799,3800,-1,3801,3802,3803,-1,3804,3805,3806,-1,3807,3808,3809,-1,3810,3811,3812,-1,3813,3814,3815,-1,3816,3817,3818,-1,3819,3820,3821,-1,3822,3823,3824,-1,3825,3826,3827,-1,3828,3829,3830,-1,3831,3832,3833,-1,3834,3835,3836,-1,3837,3838,3839,-1,3840,3841,3842,-1,3843,3844,3845,-1,3846,3847,3848,-1,3849,3850,3851,-1,3852,3853,3854,-1,3855,3856,3857,-1,3858,3859,3860,-1,3861,3862,3863,-1,3864,3865,3866,-1,3867,3868,3869,-1,3870,3871,3872,-1,3873,3874,3875,-1,3876,3877,3878,-1,3879,3880,3881,-1,3882,3883,3884,-1,3885,3886,3887,-1,3888,3889,3890,-1,3891,3892,3893,-1,3894,3895,3896,-1,3897,3898,3899,-1,3900,3901,3902,-1,3903,3904,3905,-1,3906,3907,3908,-1,3909,3910,3911,-1,3912,3913,3914,-1,3915,3916,3917,-1,3918,3919,3920,-1,3921,3922,3923,-1,3924,3925,3926,-1,3927,3928,3929,-1,3930,3931,3932,-1,3933,3934,3935,-1,3936,3937,3938,-1,3939,3940,3941,-1,3942,3943,3944,-1,3945,3946,3947,-1,3948,3949,3950,-1,3951,3952,3953,-1,3954,3955,3956,-1,3957,3958,3959,-1,3960,3961,3962,-1,3963,3964,3965,-1,3966,3967,3968,-1,3969,3970,3971,-1,3972,3973,3974,-1,3975,3976,3977,-1,3978,3979,3980,-1,3981,3982,3983,-1,3984,3985,3986,-1,3987,3988,3989,-1,3990,3991,3992,-1,3993,3994,3995,-1,3996,3997,3998,-1,3999,4000,4001,-1,4002,4003,4004,-1,4005,4006,4007,-1,4008,4009,4010,-1,4011,4012,4013,-1,4014,4015,4016,-1,4017,4018,4019,-1,4020,4021,4022,-1,4023,4024,4025,-1,4026,4027,4028,-1,4029,4030,4031,-1,4032,4033,4034,-1,4035,4036,4037,-1,4038,4039,4040,-1,4041,4042,4043,-1,4044,4045,4046,-1,4047,4048,4049,-1,4050,4051,4052,-1,4053,4054,4055,-1,4056,4057,4058,-1,4059,4060,4061,-1,4062,4063,4064,-1,4065,4066,4067,-1,4068,4069,4070,-1,4071,4072,4073,-1,4074,4075,4076,-1,4077,4078,4079,-1,4080,4081,4082,-1,4083,4084,4085,-1,4086,4087,4088,-1,4089,4090,4091,-1,4092,4093,4094,-1,4095,4096,4097,-1,4098,4099,4100,-1,4101,4102,4103,-1,4104,4105,4106,-1,4107,4108,4109,-1,4110,4111,4112,-1,4113,4114,4115,-1,4116,4117,4118,-1,4119,4120,4121,-1,4122,4123,4124,-1,4125,4126,4127,-1,4128,4129,4130,-1,4131,4132,4133,-1,4134,4135,4136,-1,4137,4138,4139,-1,4140,4141,4142,-1,4143,4144,4145,-1,4146,4147,4148,-1,4149,4150,4151,-1,4152,4153,4154,-1,4155,4156,4157,-1,4158,4159,4160,-1,4161,4162,4163,-1,4164,4165,4166,-1,4167,4168,4169,-1,4170,4171,4172,-1,4173,4174,4175,-1,4176,4177,4178,-1,4179,4180,4181,-1,4182,4183,4184,-1,4185,4186,4187,-1,4188,4189,4190,-1,4191,4192,4193,-1,4194,4195,4196,-1,4197,4198,4199,-1,4200,4201,4202,-1,4203,4204,4205,-1,4206,4207,4208,-1,4209,4210,4211,-1,4212,4213,4214,-1,4215,4216,4217,-1,4218,4219,4220,-1,4221,4222,4223,-1,4224,4225,4226,-1,4227,4228,4229,-1,4230,4231,4232,-1,4233,4234,4235,-1,4236,4237,4238,-1,4239,4240,4241,-1,4242,4243,4244,-1,4245,4246,4247,-1,4248,4249,4250,-1,4251,4252,4253,-1,4254,4255,4256,-1,4257,4258,4259,-1,4260,4261,4262,-1,4263,4264,4265,-1,4266,4267,4268,-1,4269,4270,4271,-1,4272,4273,4274,-1,4275,4276,4277,-1,4278,4279,4280,-1,4281,4282,4283,-1,4284,4285,4286,-1,4287,4288,4289,-1,4290,4291,4292,-1,4293,4294,4295,-1,4296,4297,4298,-1,4299,4300,4301,-1,4302,4303,4304,-1,4305,4306,4307,-1,4308,4309,4310,-1,4311,4312,4313,-1,4314,4315,4316,-1,4317,4318,4319,-1,4320,4321,4322,-1,4323,4324,4325,-1,4326,4327,4328,-1,4329,4330,4331,-1,4332,4333,4334,-1,4335,4336,4337,-1,4338,4339,4340,-1,4341,4342,4343,-1,4344,4345,4346,-1,4347,4348,4349,-1,4350,4351,4352,-1,4353,4354,4355,-1,4356,4357,4358,-1,4359,4360,4361,-1,4362,4363,4364,-1,4365,4366,4367,-1,4368,4369,4370,-1,4371,4372,4373,-1,4374,4375,4376,-1,4377,4378,4379,-1,4380,4381,4382,-1,4383,4384,4385,-1,4386,4387,4388,-1,4389,4390,4391,-1,4392,4393,4394,-1,4395,4396,4397,-1,4398,4399,4400,-1,4401,4402,4403,-1,4404,4405,4406,-1,4407,4408,4409,-1,4410,4411,4412,-1,4413,4414,4415,-1,4416,4417,4418,-1,4419,4420,4421,-1,4422,4423,4424,-1,4425,4426,4427,-1,4428,4429,4430,-1,4431,4432,4433,-1,4434,4435,4436,-1,4437,4438,4439,-1,4440,4441,4442,-1,4443,4444,4445,-1,4446,4447,4448,-1,4449,4450,4451,-1,4452,4453,4454,-1,4455,4456,4457,-1,4458,4459,4460,-1,4461,4462,4463,-1,4464,4465,4466,-1,4467,4468,4469,-1,4470,4471,4472,-1,4473,4474,4475,-1,4476,4477,4478,-1,4479,4480,4481,-1,4482,4483,4484,-1,4485,4486,4487,-1,4488,4489,4490,-1,4491,4492,4493,-1,4494,4495,4496,-1,4497,4498,4499,-1,4500,4501,4502,-1,4503,4504,4505,-1,4506,4507,4508,-1,4509,4510,4511,-1,4512,4513,4514,-1,4515,4516,4517,-1,4518,4519,4520,-1,4521,4522,4523,-1,4524,4525,4526,-1,4527,4528,4529,-1,4530,4531,4532,-1,4533,4534,4535,-1,4536,4537,4538,-1,4539,4540,4541,-1,4542,4543,4544,-1,4545,4546,4547,-1,4548,4549,4550,-1,4551,4552,4553,-1,4554,4555,4556,-1,4557,4558,4559,-1,4560,4561,4562,-1,4563,4564,4565,-1,4566,4567,4568,-1,4569,4570,4571,-1,4572,4573,4574,-1,4575,4576,4577,-1,4578,4579,4580,-1,4581,4582,4583,-1,4584,4585,4586,-1,4587,4588,4589,-1,4590,4591,4592,-1,4593,4594,4595,-1,4596,4597,4598,-1,4599,4600,4601,-1,4602,4603,4604,-1,4605,4606,4607,-1,4608,4609,4610,-1,4611,4612,4613,-1,4614,4615,4616,-1,4617,4618,4619,-1,4620,4621,4622,-1,4623,4624,4625,-1,4626,4627,4628,-1,4629,4630,4631,-1,4632,4633,4634,-1,4635,4636,4637,-1,4638,4639,4640,-1,4641,4642,4643,-1,4644,4645,4646,-1,4647,4648,4649,-1,4650,4651,4652,-1,4653,4654,4655,-1,4656,4657,4658,-1,4659,4660,4661,-1,4662,4663,4664,-1,4665,4666,4667,-1,4668,4669,4670,-1,4671,4672,4673,-1,4674,4675,4676,-1,4677,4678,4679,-1,4680,4681,4682,-1,4683,4684,4685,-1,4686,4687,4688,-1,4689,4690,4691,-1,4692,4693,4694,-1,4695,4696,4697,-1,4698,4699,4700,-1,4701,4702,4703,-1,4704,4705,4706,-1,4707,4708,4709,-1,4710,4711,4712,-1,4713,4714,4715,-1,4716,4717,4718,-1,4719,4720,4721,-1,4722,4723,4724,-1,4725,4726,4727,-1,4728,4729,4730,-1,4731,4732,4733,-1,4734,4735,4736,-1,4737,4738,4739,-1,4740,4741,4742,-1,4743,4744,4745,-1,4746,4747,4748,-1,4749,4750,4751,-1,4752,4753,4754,-1,4755,4756,4757,-1,4758,4759,4760,-1,4761,4762,4763,-1,4764,4765,4766,-1,4767,4768,4769,-1,4770,4771,4772,-1,4773,4774,4775,-1,4776,4777,4778,-1,4779,4780,4781,-1,4782,4783,4784,-1,4785,4786,4787,-1,4788,4789,4790,-1,4791,4792,4793,-1,4794,4795,4796,-1,4797,4798,4799,-1,4800,4801,4802,-1,4803,4804,4805,-1,4806,4807,4808,-1,4809,4810,4811,-1,4812,4813,4814,-1,4815,4816,4817,-1,4818,4819,4820,-1,4821,4822,4823,-1,4824,4825,4826,-1,4827,4828,4829,-1,4830,4831,4832,-1,4833,4834,4835,-1,4836,4837,4838,-1,4839,4840,4841,-1,4842,4843,4844,-1,4845,4846,4847,-1,4848,4849,4850,-1,4851,4852,4853,-1,4854,4855,4856,-1,4857,4858,4859,-1,4860,4861,4862,-1,4863,4864,4865,-1,4866,4867,4868,-1,4869,4870,4871,-1,4872,4873,4874,-1,4875,4876,4877,-1,4878,4879,4880,-1,4881,4882,4883,-1,4884,4885,4886,-1]
IndexedFaceSet209.creaseAngle = 1.59
Coordinate210 = x3d.Coordinate()

IndexedFaceSet209.coord = Coordinate210

Shape205.geometry = IndexedFaceSet209

Transform204.children.append(Shape205)

fieldValue203.children.append(Transform204)

ProtoInstance201.fieldValue.append(fieldValue203)

fieldValue200.children.append(ProtoInstance201)
ProtoInstance211 = x3d.ProtoInstance()
ProtoInstance211.name = "Joint"
ProtoInstance211.DEF = "hanim_l_shoulder"
fieldValue212 = x3d.fieldValue()
fieldValue212.name = "name"
fieldValue212.value = "l_shoulder"

ProtoInstance211.fieldValue.append(fieldValue212)
fieldValue213 = x3d.fieldValue()
fieldValue213.name = "center"
fieldValue213.value = "0.167 1.36 -0.0518"

ProtoInstance211.fieldValue.append(fieldValue213)
fieldValue214 = x3d.fieldValue()
fieldValue214.name = "children"
ProtoInstance215 = x3d.ProtoInstance()
ProtoInstance215.name = "Segment"
ProtoInstance215.DEF = "hanim_l_upperarm"
fieldValue216 = x3d.fieldValue()
fieldValue216.name = "name"
fieldValue216.value = "l_upperarm"

ProtoInstance215.fieldValue.append(fieldValue216)
fieldValue217 = x3d.fieldValue()
fieldValue217.name = "children"
Transform218 = x3d.Transform()
Transform218.DEF = "l_upperarm_adjust"
Transform218.center = [-0.435,1,0.06]
Transform218.rotation = [0,1,0,1.570796]
Transform218.scale = [0.1,0.1,0.1]
Shape219 = x3d.Shape()
Appearance220 = x3d.Appearance()
Material221 = x3d.Material()
Material221.DEF = "Skin_Color"
Material221.ambientIntensity = 0.25
Material221.diffuseColor = [0.749,0.601,0.462]

Appearance220.material = Material221
ImageTexture222 = x3d.ImageTexture()
ImageTexture222.USE = "camo"

Appearance220.texture = ImageTexture222

Shape219.appearance = Appearance220
IndexedFaceSet223 = x3d.IndexedFaceSet()
IndexedFaceSet223.coordIndex = [0,1,2,-1,3,4,5,-1,6,7,8,-1,9,10,11,-1,12,13,14,-1,15,16,17,-1,18,19,20,-1,21,22,23,-1,24,25,26,-1,27,28,29,-1,30,31,32,-1,33,34,35,-1,36,37,38,-1,39,40,41,-1,42,43,44,-1,45,46,47,-1,48,49,50,-1,51,52,53,-1,54,55,56,-1,57,58,59,-1,60,61,62,-1,63,64,65,-1,66,67,68,-1,69,70,71,-1,72,73,74,-1,75,76,77,-1,78,79,80,-1,81,82,83,-1,84,85,86,-1,87,88,89,-1,90,91,92,-1,93,94,95,-1,96,97,98,-1,99,100,101,-1,102,103,104,-1,105,106,107,-1,108,109,110,-1,111,112,113,-1,114,115,116,-1,117,118,119,-1,120,121,122,-1,123,124,125,-1,126,127,128,-1,129,130,131,-1,132,133,134,-1,135,136,137,-1,138,139,140,-1,141,142,143,-1,144,145,146,-1,147,148,149,-1,150,151,152,-1,153,154,155,-1,156,157,158,-1,159,160,161,-1,162,163,164,-1,165,166,167,-1,168,169,170,-1,171,172,173,-1,174,175,176,-1,177,178,179,-1,180,181,182,-1,183,184,185,-1,186,187,188,-1,189,190,191,-1,192,193,194,-1,195,196,197,-1,198,199,200,-1,201,202,203,-1,204,205,206,-1,207,208,209,-1,210,211,212,-1,213,214,215,-1,216,217,218,-1,219,220,221,-1,222,223,224,-1,225,226,227,-1,228,229,230,-1,231,232,233,-1,234,235,236,-1,237,238,239,-1,240,241,242,-1,243,244,245,-1,246,247,248,-1,249,250,251,-1,252,253,254,-1,255,256,257,-1,258,259,260,-1,261,262,263,-1,264,265,266,-1,267,268,269,-1,270,271,272,-1,273,274,275,-1,276,277,278,-1,279,280,281,-1,282,283,284,-1,285,286,287,-1,288,289,290,-1,291,292,293,-1,294,295,296,-1,297,298,299,-1,300,301,302,-1,303,304,305,-1,306,307,308,-1,309,310,311,-1,312,313,314,-1,315,316,317,-1,318,319,320,-1,321,322,323,-1,324,325,326,-1,327,328,329,-1,330,331,332,-1,333,334,335,-1,336,337,338,-1,339,340,341,-1,342,343,344,-1,345,346,347,-1,348,349,350,-1,351,352,353,-1,354,355,356,-1,357,358,359,-1,360,361,362,-1,363,364,365,-1,366,367,368,-1,369,370,371,-1,372,373,374,-1,375,376,377,-1,378,379,380,-1,381,382,383,-1,384,385,386,-1,387,388,389,-1,390,391,392,-1,393,394,395,-1,396,397,398,-1,399,400,401,-1,402,403,404,-1,405,406,407,-1,408,409,410,-1,411,412,413,-1,414,415,416,-1,417,418,419,-1,420,421,422,-1,423,424,425,-1,426,427,428,-1,429,430,431,-1,432,433,434,-1,435,436,437,-1,438,439,440,-1,441,442,443,-1,444,445,446,-1,447,448,449,-1,450,451,452,-1,453,454,455,-1,456,457,458,-1,459,460,461,-1,462,463,464,-1,465,466,467,-1,468,469,470,-1,471,472,473,-1,474,475,476,-1,477,478,479,-1,480,481,482,-1,483,484,485,-1,486,487,488,-1,489,490,491,-1,492,493,494,-1,495,496,497,-1,498,499,500,-1,501,502,503,-1,504,505,506,-1,507,508,509,-1,510,511,512,-1,513,514,515,-1,516,517,518,-1,519,520,521,-1,522,523,524,-1,525,526,527,-1,528,529,530,-1,531,532,533,-1,534,535,536,-1,537,538,539,-1,540,541,542,-1,543,544,545,-1,546,547,548,-1,549,550,551,-1,552,553,554,-1,555,556,557,-1,558,559,560,-1,561,562,563,-1,564,565,566,-1,567,568,569,-1,570,571,572,-1,573,574,575,-1,576,577,578,-1,579,580,581,-1,582,583,584,-1,585,586,587,-1,588,589,590,-1,591,592,593,-1,594,595,596,-1,597,598,599,-1,600,601,602,-1,603,604,605,-1,606,607,608,-1,609,610,611,-1,612,613,614,-1,615,616,617,-1,618,619,620,-1,621,622,623,-1,624,625,626,-1,627,628,629,-1,630,631,632,-1,633,634,635,-1,636,637,638,-1,639,640,641,-1,642,643,644,-1,645,646,647,-1,648,649,650,-1,651,652,653,-1,654,655,656,-1,657,658,659,-1,660,661,662,-1,663,664,665,-1,666,667,668,-1,669,670,671,-1,672,673,674,-1,675,676,677,-1,678,679,680,-1,681,682,683,-1,684,685,686,-1,687,688,689,-1,690,691,692,-1,693,694,695,-1,696,697,698,-1,699,700,701,-1,702,703,704,-1,705,706,707,-1,708,709,710,-1,711,712,713,-1,714,715,716,-1,717,718,719,-1,720,721,722,-1,723,724,725,-1,726,727,728,-1,729,730,731,-1,732,733,734,-1,735,736,737,-1,738,739,740,-1,741,742,743,-1,744,745,746,-1,747,748,749,-1,750,751,752,-1,753,754,755,-1,756,757,758,-1,759,760,761,-1,762,763,764,-1,765,766,767,-1,768,769,770,-1,771,772,773,-1,774,775,776,-1,777,778,779,-1,780,781,782,-1,783,784,785,-1,786,787,788,-1,789,790,791,-1,792,793,794,-1,795,796,797,-1,798,799,800,-1,801,802,803,-1,804,805,806,-1,807,808,809,-1,810,811,812,-1,813,814,815,-1,816,817,818,-1,819,820,821,-1,822,823,824,-1,825,826,827,-1,828,829,830,-1,831,832,833,-1,834,835,836,-1,837,838,839,-1,840,841,842,-1,843,844,845,-1,846,847,848,-1,849,850,851,-1,852,853,854,-1,855,856,857,-1,858,859,860,-1,861,862,863,-1,864,865,866,-1,867,868,869,-1,870,871,872,-1,873,874,875,-1,876,877,878,-1,879,880,881,-1,882,883,884,-1,885,886,887,-1,888,889,890,-1,891,892,893,-1,894,895,896,-1,897,898,899,-1,900,901,902,-1,903,904,905,-1,906,907,908,-1,909,910,911,-1,912,913,914,-1,915,916,917,-1,918,919,920,-1,921,922,923,-1,924,925,926,-1,927,928,929,-1,930,931,932,-1,933,934,935,-1,936,937,938,-1,939,940,941,-1,942,943,944,-1,945,946,947,-1,948,949,950,-1,951,952,953,-1,954,955,956,-1,957,958,959,-1,960,961,962,-1,963,964,965,-1,966,967,968,-1,969,970,971,-1,972,973,974,-1,975,976,977,-1,978,979,980,-1,981,982,983,-1,984,985,986,-1,987,988,989,-1,990,991,992,-1,993,994,995,-1,996,997,998,-1,999,1000,1001,-1,1002,1003,1004,-1,1005,1006,1007,-1,1008,1009,1010,-1,1011,1012,1013,-1,1014,1015,1016,-1,1017,1018,1019,-1,1020,1021,1022,-1,1023,1024,1025,-1,1026,1027,1028,-1,1029,1030,1031,-1,1032,1033,1034,-1,1035,1036,1037,-1,1038,1039,1040,-1,1041,1042,1043,-1,1044,1045,1046,-1,1047,1048,1049,-1,1050,1051,1052,-1,1053,1054,1055,-1,1056,1057,1058,-1,1059,1060,1061,-1,1062,1063,1064,-1,1065,1066,1067,-1,1068,1069,1070,-1,1071,1072,1073,-1,1074,1075,1076,-1,1077,1078,1079,-1,1080,1081,1082,-1,1083,1084,1085,-1,1086,1087,1088,-1,1089,1090,1091,-1,1092,1093,1094,-1,1095,1096,1097,-1,1098,1099,1100,-1,1101,1102,1103,-1,1104,1105,1106,-1,1107,1108,1109,-1,1110,1111,1112,-1,1113,1114,1115,-1,1116,1117,1118,-1,1119,1120,1121,-1,1122,1123,1124,-1,1125,1126,1127,-1,1128,1129,1130,-1,1131,1132,1133,-1,1134,1135,1136,-1,1137,1138,1139,-1,1140,1141,1142,-1,1143,1144,1145,-1,1146,1147,1148,-1,1149,1150,1151,-1,1152,1153,1154,-1,1155,1156,1157,-1,1158,1159,1160,-1,1161,1162,1163,-1,1164,1165,1166,-1,1167,1168,1169,-1,1170,1171,1172,-1,1173,1174,1175,-1,1176,1177,1178,-1,1179,1180,1181,-1,1182,1183,1184,-1,1185,1186,1187,-1,1188,1189,1190,-1,1191,1192,1193,-1,1194,1195,1196,-1,1197,1198,1199,-1,1200,1201,1202,-1,1203,1204,1205,-1,1206,1207,1208,-1,1209,1210,1211,-1,1212,1213,1214,-1,1215,1216,1217,-1,1218,1219,1220,-1,1221,1222,1223,-1,1224,1225,1226,-1,1227,1228,1229,-1,1230,1231,1232,-1,1233,1234,1235,-1,1236,1237,1238,-1,1239,1240,1241,-1,1242,1243,1244,-1,1245,1246,1247,-1,1248,1249,1250,-1,1251,1252,1253,-1,1254,1255,1256,-1,1257,1258,1259,-1,1260,1261,1262,-1,1263,1264,1265,-1,1266,1267,1268,-1,1269,1270,1271,-1,1272,1273,1274,-1,1275,1276,1277,-1,1278,1279,1280,-1,1281,1282,1283,-1,1284,1285,1286,-1,1287,1288,1289,-1,1290,1291,1292,-1,1293,1294,1295,-1,1296,1297,1298,-1,1299,1300,1301,-1,1302,1303,1304,-1,1305,1306,1307,-1,1308,1309,1310,-1,1311,1312,1313,-1,1314,1315,1316,-1,1317,1318,1319,-1,1320,1321,1322,-1,1323,1324,1325,-1,1326,1327,1328,-1,1329,1330,1331,-1,1332,1333,1334,-1,1335,1336,1337,-1,1338,1339,1340,-1,1341,1342,1343,-1,1344,1345,1346,-1,1347,1348,1349,-1,1350,1351,1352,-1,1353,1354,1355,-1,1356,1357,1358,-1,1359,1360,1361,-1,1362,1363,1364,-1,1365,1366,1367,-1,1368,1369,1370,-1,1371,1372,1373,-1,1374,1375,1376,-1,1377,1378,1379,-1,1380,1381,1382,-1,1383,1384,1385,-1,1386,1387,1388,-1,1389,1390,1391,-1,1392,1393,1394,-1,1395,1396,1397,-1,1398,1399,1400,-1,1401,1402,1403,-1,1404,1405,1406,-1,1407,1408,1409,-1,1410,1411,1412,-1,1413,1414,1415,-1,1416,1417,1418,-1,1419,1420,1421,-1,1422,1423,1424,-1,1425,1426,1427,-1,1428,1429,1430,-1,1431,1432,1433,-1,1434,1435,1436,-1,1437,1438,1439,-1,1440,1441,1442,-1,1443,1444,1445,-1,1446,1447,1448,-1,1449,1450,1451,-1,1452,1453,1454,-1,1455,1456,1457,-1,1458,1459,1460,-1,1461,1462,1463,-1,1464,1465,1466,-1,1467,1468,1469,-1,1470,1471,1472,-1,1473,1474,1475,-1,1476,1477,1478,-1,1479,1480,1481,-1,1482,1483,1484,-1,1485,1486,1487,-1,1488,1489,1490,-1,1491,1492,1493,-1,1494,1495,1496,-1,1497,1498,1499,-1,1500,1501,1502,-1,1503,1504,1505,-1,1506,1507,1508,-1,1509,1510,1511,-1,1512,1513,1514,-1,1515,1516,1517,-1,1518,1519,1520,-1,1521,1522,1523,-1,1524,1525,1526,-1,1527,1528,1529,-1,1530,1529,1528,-1,1528,1531,1530,-1,1532,1530,1531,-1,1535,1533,1534,-1]
IndexedFaceSet223.creaseAngle = 1.65
Coordinate224 = x3d.Coordinate()

IndexedFaceSet223.coord = Coordinate224

Shape219.geometry = IndexedFaceSet223

Transform218.children.append(Shape219)

fieldValue217.children.append(Transform218)

ProtoInstance215.fieldValue.append(fieldValue217)

fieldValue214.children.append(ProtoInstance215)
ProtoInstance225 = x3d.ProtoInstance()
ProtoInstance225.name = "Joint"
ProtoInstance225.DEF = "hanim_l_elbow"
fieldValue226 = x3d.fieldValue()
fieldValue226.name = "name"
fieldValue226.value = "l_elbow"

ProtoInstance225.fieldValue.append(fieldValue226)
fieldValue227 = x3d.fieldValue()
fieldValue227.name = "center"
fieldValue227.value = "0.196 1.07 -0.0518"

ProtoInstance225.fieldValue.append(fieldValue227)
fieldValue228 = x3d.fieldValue()
fieldValue228.name = "children"
ProtoInstance229 = x3d.ProtoInstance()
ProtoInstance229.name = "Segment"
ProtoInstance229.DEF = "hanim_l_forearm"
fieldValue230 = x3d.fieldValue()
fieldValue230.name = "name"
fieldValue230.value = "l_forearm"

ProtoInstance229.fieldValue.append(fieldValue230)
fieldValue231 = x3d.fieldValue()
fieldValue231.name = "children"
Transform232 = x3d.Transform()
Transform232.DEF = "l_forearm_adjust"
Transform232.center = [-0.634,1.01,0.0799]
Transform232.rotation = [0,1,0,1.570796]
Transform232.scale = [0.1,0.1,0.1]
Shape233 = x3d.Shape()
Appearance234 = x3d.Appearance()
Material235 = x3d.Material()
Material235.USE = "Skin_Color"

Appearance234.material = Material235
ImageTexture236 = x3d.ImageTexture()
ImageTexture236.USE = "camo"

Appearance234.texture = ImageTexture236

Shape233.appearance = Appearance234
IndexedFaceSet237 = x3d.IndexedFaceSet()
IndexedFaceSet237.coordIndex = [0,1,2,-1,3,4,5,-1,6,7,8,-1,9,10,11,-1,12,13,14,-1,15,16,17,-1,18,19,20,-1,21,22,23,-1,24,25,26,-1,27,28,29,-1,30,31,32,-1,33,34,35,-1,36,37,38,-1,39,40,41,-1,42,43,44,-1,45,46,47,-1,48,49,50,-1,51,52,53,-1,54,55,56,-1,57,58,59,-1,60,61,62,-1,63,64,65,-1,66,67,68,-1,69,70,71,-1,72,73,74,-1,75,76,77,-1,78,79,80,-1,81,82,83,-1,84,85,86,-1,87,88,89,-1,90,91,92,-1,93,94,95,-1,96,97,98,-1,99,100,101,-1,102,103,104,-1,105,106,107,-1,108,109,110,-1,111,112,113,-1,114,115,116,-1,117,118,119,-1,120,121,122,-1,123,124,125,-1,126,127,128,-1,129,130,131,-1,132,133,134,-1,135,136,137,-1,138,139,140,-1,141,142,143,-1,144,145,146,-1,147,148,149,-1,150,151,152,-1,153,154,155,-1,156,157,158,-1,159,160,161,-1,162,163,164,-1,165,166,167,-1,168,169,170,-1,171,172,173,-1,174,175,176,-1,177,178,179,-1,180,181,182,-1,183,184,185,-1,186,187,188,-1,189,190,191,-1,192,193,194,-1,195,196,197,-1,198,199,200,-1,201,202,203,-1,204,205,206,-1,207,208,209,-1,210,211,212,-1,213,214,215,-1,216,217,218,-1,219,220,221,-1,222,223,224,-1,225,226,227,-1,228,229,230,-1,231,232,233,-1,234,235,236,-1,237,238,239,-1,240,241,242,-1,243,244,245,-1,246,247,248,-1,249,250,251,-1,252,253,254,-1,255,256,257,-1,258,259,260,-1,261,262,263,-1,264,265,266,-1,267,268,269,-1,270,271,272,-1,273,274,275,-1,276,277,278,-1,279,280,281,-1,282,283,284,-1,285,286,287,-1,288,289,290,-1,291,292,293,-1,294,295,296,-1,297,298,299,-1,300,301,302,-1,303,304,305,-1,306,307,308,-1,309,310,311,-1,312,313,314,-1,315,316,317,-1,318,319,320,-1,321,322,323,-1,324,325,326,-1,327,328,329,-1,330,331,332,-1,333,334,335,-1,336,337,338,-1,339,340,341,-1,342,343,344,-1,345,346,347,-1,348,349,350,-1,351,352,353,-1,354,355,356,-1,357,358,359,-1,360,361,362,-1,363,364,365,-1,366,367,368,-1,369,370,371,-1,372,373,374,-1,375,376,377,-1,378,379,380,-1,381,382,383,-1,384,385,386,-1,387,388,389,-1,390,391,392,-1,393,394,395,-1,396,397,398,-1,399,400,401,-1,402,403,404,-1,405,406,407,-1,408,409,410,-1,411,412,413,-1,414,415,416,-1,417,418,419,-1,420,421,422,-1,423,424,425,-1,426,427,428,-1,429,430,431,-1,432,433,434,-1,435,436,437,-1,438,439,440,-1,441,442,443,-1,444,445,446,-1,447,448,449,-1,450,451,452,-1,453,454,455,-1,456,457,458,-1,459,460,461,-1,462,463,464,-1,465,466,467,-1,468,469,470,-1,471,472,473,-1,474,475,476,-1,477,478,479,-1,480,481,482,-1,483,484,485,-1,486,487,488,-1,489,490,491,-1,492,493,494,-1,495,496,497,-1,498,499,500,-1,501,502,503,-1,504,505,506,-1,507,508,509,-1,510,511,512,-1,513,514,515,-1,516,517,518,-1,519,520,521,-1,522,523,524,-1,525,526,527,-1,528,529,530,-1,531,532,533,-1,534,535,536,-1,537,538,539,-1,540,541,542,-1,543,544,545,-1,546,547,548,-1,549,550,551,-1,552,553,554,-1,555,556,557,-1,558,559,560,-1,561,562,563,-1,564,565,566,-1,567,568,569,-1,570,571,572,-1,573,574,575,-1,576,577,578,-1,579,580,581,-1,582,583,584,-1,585,586,587,-1,588,589,590,-1,591,592,593,-1,594,595,596,-1,597,598,599,-1,600,601,602,-1,603,604,605,-1,606,607,608,-1,609,610,611,-1,612,613,614,-1,615,616,617,-1,618,619,620,-1,621,622,623,-1,624,625,626,-1,627,628,629,-1,630,631,632,-1,633,634,635,-1,636,637,638,-1,639,640,641,-1,642,643,644,-1,645,646,647,-1,648,649,650,-1,651,652,653,-1,654,655,656,-1,657,658,659,-1,660,661,662,-1,663,664,665,-1,666,667,668,-1,669,670,671,-1,672,673,674,-1,675,676,677,-1,678,679,680,-1,681,682,683,-1,684,685,686,-1,687,688,689,-1,690,691,692,-1,693,694,695,-1,696,697,698,-1,699,700,701,-1,702,703,704,-1,705,706,707,-1,708,709,710,-1,711,712,713,-1,714,715,716,-1,717,718,719,-1,720,721,722,-1,723,724,725,-1,726,727,728,-1,729,730,731,-1,732,733,734,-1,735,736,737,-1,738,739,740,-1,741,742,743,-1,744,745,746,-1,747,748,749,-1,750,751,752,-1,753,754,755,-1,756,757,758,-1,759,760,761,-1,762,763,764,-1,765,766,767,-1,768,769,770,-1,771,772,773,-1,774,775,776,-1,777,778,779,-1,780,781,782,-1,783,784,785,-1,786,787,788,-1,789,790,791,-1,792,793,794,-1,795,796,797,-1,798,799,800,-1,801,802,803,-1,804,805,806,-1,807,808,809,-1,810,811,812,-1,813,814,815,-1,816,817,818,-1,819,820,821,-1,822,823,824,-1,825,826,827,-1,828,829,830,-1,831,832,833,-1,834,835,836,-1,837,838,839,-1,840,841,842,-1,843,844,845,-1,846,847,848,-1,849,850,851,-1,852,853,854,-1,855,856,857,-1,858,859,860,-1,861,862,863,-1,864,865,866,-1,867,868,869,-1,870,871,872,-1,873,874,875,-1,876,877,878,-1,879,880,881,-1,882,883,884,-1,885,886,887,-1,888,889,890,-1,891,892,893,-1,894,895,896,-1,897,898,899,-1,900,901,902,-1,903,904,905,-1,906,907,908,-1,909,910,911,-1,912,913,914,-1,915,916,917,-1,918,919,920,-1,921,922,923,-1,924,925,926,-1,927,928,929,-1,930,931,932,-1,933,934,935,-1,936,937,938,-1,939,940,941,-1,942,943,944,-1,945,946,947,-1,948,949,950,-1,951,952,953,-1,954,955,956,-1,957,958,959,-1,960,961,962,-1,963,964,965,-1,966,967,968,-1,969,970,971,-1,972,973,974,-1,975,976,977,-1,978,979,980,-1,981,982,983,-1,984,985,986,-1,987,988,989,-1,990,991,992,-1,993,994,995,-1,996,997,998,-1,999,1000,1001,-1,1002,1003,1004,-1,1005,1006,1007,-1,1008,1009,1010,-1,1011,1012,1013,-1,1014,1015,1016,-1,1017,1018,1019,-1,1020,1021,1022,-1,1023,1024,1025,-1,1026,1027,1028,-1,1029,1030,1031,-1,1032,1033,1034,-1,1035,1036,1037,-1,1038,1039,1040,-1,1041,1042,1043,-1,1044,1045,1046,-1,1047,1048,1049,-1,1050,1051,1052,-1,1053,1054,1055,-1,1056,1057,1058,-1,1059,1060,1061,-1,1062,1063,1064,-1,1065,1066,1067,-1,1068,1069,1070,-1,1071,1072,1073,-1,1074,1075,1076,-1,1077,1078,1079,-1,1080,1081,1082,-1,1083,1084,1085,-1,1086,1087,1088,-1,1089,1090,1091,-1,1092,1093,1094,-1,1095,1096,1097,-1,1098,1099,1100,-1,1101,1102,1103,-1,1104,1105,1106,-1,1107,1108,1109,-1,1110,1111,1112,-1,1113,1114,1115,-1,1116,1117,1118,-1,1119,1120,1121,-1,1122,1123,1124,-1,1125,1126,1127,-1,1128,1129,1130,-1,1131,1132,1133,-1,1134,1135,1136,-1,1137,1138,1139,-1,1140,1141,1142,-1,1143,1144,1145,-1,1146,1147,1148,-1,1149,1150,1151,-1,1152,1153,1154,-1,1155,1156,1157,-1,1158,1159,1160,-1,1161,1162,1163,-1,1164,1165,1166,-1,1167,1168,1169,-1,1170,1171,1172,-1,1173,1174,1175,-1,1176,1177,1178,-1,1179,1180,1181,-1,1182,1183,1184,-1,1185,1186,1187,-1,1188,1189,1190,-1,1191,1192,1193,-1,1194,1195,1196,-1,1197,1198,1199,-1,1200,1201,1202,-1,1203,1204,1205,-1,1206,1207,1208,-1,1209,1210,1211,-1,1212,1213,1214,-1,1215,1216,1217,-1,1218,1219,1220,-1,1221,1222,1223,-1,1224,1225,1226,-1,1227,1228,1229,-1,1230,1231,1232,-1,1233,1234,1235,-1,1236,1237,1238,-1,1239,1240,1241,-1,1242,1243,1244,-1,1245,1246,1247,-1,1248,1249,1250,-1,1251,1252,1253,-1,1254,1255,1256,-1,1257,1258,1259,-1,1260,1261,1262,-1,1263,1264,1265,-1,1266,1267,1268,-1,1269,1270,1271,-1,1272,1273,1274,-1,1275,1276,1277,-1,1278,1279,1280,-1,1281,1282,1283,-1,1284,1285,1286,-1,1287,1288,1289,-1,1290,1291,1292,-1,1293,1294,1295,-1,1296,1297,1298,-1,1299,1300,1301,-1,1302,1303,1304,-1,1305,1306,1307,-1,1308,1309,1310,-1,1311,1312,1313,-1,1314,1315,1316,-1,1317,1318,1319,-1,1320,1321,1322,-1,1323,1324,1325,-1,1326,1327,1328,-1,1329,1330,1331,-1,1332,1333,1334,-1,1335,1336,1337,-1,1338,1339,1340,-1,1341,1342,1343,-1,1344,1345,1346,-1,1347,1348,1349,-1,1350,1351,1352,-1,1353,1354,1355,-1,1356,1357,1358,-1,1359,1360,1361,-1,1362,1363,1364,-1,1365,1366,1367,-1,1368,1369,1370,-1,1371,1372,1373,-1,1374,1375,1376,-1,1377,1378,1379,-1,1380,1381,1382,-1,1383,1384,1385,-1,1386,1387,1388,-1,1389,1390,1391,-1,1392,1393,1394,-1,1395,1396,1397,-1,1398,1399,1400,-1,1401,1402,1403,-1,1404,1405,1406,-1,1407,1408,1409,-1,1410,1411,1412,-1,1413,1414,1415,-1,1416,1417,1418,-1,1419,1420,1421,-1,1422,1423,1424,-1,1425,1426,1427,-1,1428,1429,1430,-1,1431,1432,1433,-1,1434,1435,1436,-1,1437,1438,1439,-1,1440,1441,1442,-1,1443,1444,1445,-1,1446,1447,1448,-1,1449,1450,1451,-1,1452,1453,1454,-1,1455,1456,1457,-1,1458,1459,1460,-1,1461,1462,1463,-1,1464,1465,1466,-1,1467,1468,1469,-1,1470,1471,1472,-1,1473,1474,1475,-1,1476,1477,1478,-1,1479,1480,1481,-1,1482,1483,1484,-1,1485,1486,1487,-1]
IndexedFaceSet237.creaseAngle = 1.75
Coordinate238 = x3d.Coordinate()

IndexedFaceSet237.coord = Coordinate238

Shape233.geometry = IndexedFaceSet237

Transform232.children.append(Shape233)

fieldValue231.children.append(Transform232)

ProtoInstance229.fieldValue.append(fieldValue231)

fieldValue228.children.append(ProtoInstance229)
ProtoInstance239 = x3d.ProtoInstance()
ProtoInstance239.name = "Joint"
ProtoInstance239.DEF = "hanim_l_wrist"
fieldValue240 = x3d.fieldValue()
fieldValue240.name = "name"
fieldValue240.value = "l_wrist"

ProtoInstance239.fieldValue.append(fieldValue240)
fieldValue241 = x3d.fieldValue()
fieldValue241.name = "center"
fieldValue241.value = "0.213 0.811 -0.0338"

ProtoInstance239.fieldValue.append(fieldValue241)
fieldValue242 = x3d.fieldValue()
fieldValue242.name = "children"
ProtoInstance243 = x3d.ProtoInstance()
ProtoInstance243.name = "Segment"
ProtoInstance243.DEF = "hanim_l_hand"
fieldValue244 = x3d.fieldValue()
fieldValue244.name = "name"
fieldValue244.value = "l_hand"

ProtoInstance243.fieldValue.append(fieldValue244)
fieldValue245 = x3d.fieldValue()
fieldValue245.name = "children"
Transform246 = x3d.Transform()
Transform246.DEF = "l_hand_adjust"
Transform246.center = [-0.8355,1.015,0.1]
Transform246.rotation = [0,1,0,1.570796]
Transform246.scale = [0.1,0.1,0.1]
Shape247 = x3d.Shape()
Appearance248 = x3d.Appearance()
Material249 = x3d.Material()
Material249.USE = "Skin_Color"

Appearance248.material = Material249

Shape247.appearance = Appearance248
IndexedFaceSet250 = x3d.IndexedFaceSet()
IndexedFaceSet250.coordIndex = [0,1,2,-1,3,4,5,-1,6,7,8,-1,9,10,11,-1,12,13,14,-1,15,16,17,-1,18,19,20,-1,21,22,23,-1,24,25,26,-1,27,28,29,-1,30,31,32,-1,33,34,35,-1,36,37,38,-1,39,40,41,-1,42,43,44,-1,45,46,47,-1,48,49,50,-1,51,52,53,-1,54,55,56,-1,57,58,59,-1,60,61,62,-1,63,64,65,-1,66,67,68,-1,69,70,71,-1,72,73,74,-1,75,76,77,-1,78,79,80,-1,81,82,83,-1,84,85,86,-1,87,88,89,-1,90,91,92,-1,93,94,95,-1,96,97,98,-1,99,100,101,-1,102,103,104,-1,105,106,107,-1,108,109,110,-1,111,112,113,-1,114,115,116,-1,117,118,119,-1,120,121,122,-1,123,124,125,-1,126,127,128,-1,129,130,131,-1,132,133,134,-1,135,136,137,-1,138,139,140,-1,141,142,143,-1,144,145,146,-1,147,148,149,-1,150,151,152,-1,153,154,155,-1,156,157,158,-1,159,160,161,-1,162,163,164,-1,165,166,167,-1,168,169,170,-1,171,172,173,-1,174,175,176,-1,177,178,179,-1,180,181,182,-1,183,184,185,-1,186,187,188,-1,189,190,191,-1,192,193,194,-1,195,196,197,-1,198,199,200,-1,201,202,203,-1,204,205,206,-1,207,208,209,-1,210,211,212,-1,213,214,215,-1,216,217,218,-1,219,220,221,-1,222,223,224,-1,225,226,227,-1,228,229,230,-1,231,232,233,-1,234,235,236,-1,237,238,239,-1,240,241,242,-1,243,244,245,-1,246,247,248,-1,249,250,251,-1,252,253,254,-1,255,256,257,-1,258,259,260,-1,261,262,263,-1,264,265,266,-1,267,268,269,-1,270,271,272,-1,273,274,275,-1,276,277,278,-1,279,280,281,-1,282,283,284,-1,285,286,287,-1,288,289,290,-1,291,292,293,-1,294,295,296,-1,297,298,299,-1,300,301,302,-1,303,304,305,-1,306,307,308,-1,309,310,311,-1,312,313,314,-1,315,316,317,-1,318,319,320,-1,321,322,323,-1,324,325,326,-1,327,328,329,-1,330,331,332,-1,333,334,335,-1,336,337,338,-1,339,340,341,-1,342,343,344,-1,345,346,347,-1,348,349,350,-1,351,352,353,-1,354,355,356,-1,357,358,359,-1,360,361,362,-1,363,364,365,-1,366,367,368,-1,369,370,371,-1,372,373,374,-1,375,376,377,-1,378,379,380,-1,381,382,383,-1,384,385,386,-1,387,388,389,-1,390,391,392,-1,393,394,395,-1,396,397,398,-1,399,400,401,-1,402,403,404,-1,405,406,407,-1,408,409,410,-1,411,412,413,-1,414,415,416,-1,417,418,419,-1,420,421,422,-1,423,424,425,-1,426,427,428,-1,429,430,431,-1,432,433,434,-1,435,436,437,-1,438,439,440,-1,441,442,443,-1,444,445,446,-1,447,448,449,-1,450,451,452,-1,453,454,455,-1,456,457,458,-1,459,460,461,-1,462,463,464,-1,465,466,467,-1,468,469,470,-1,471,472,473,-1,474,475,476,-1,477,478,479,-1,480,481,482,-1,483,484,485,-1,486,487,488,-1,489,490,491,-1,492,493,494,-1,495,496,497,-1,498,499,500,-1,501,502,503,-1,504,505,506,-1,507,508,509,-1,510,511,512,-1,513,514,515,-1,516,517,518,-1,519,520,521,-1,522,523,524,-1,525,526,527,-1,528,529,530,-1,531,532,533,-1,534,535,536,-1,537,538,539,-1,540,541,542,-1,543,544,545,-1,546,547,548,-1,549,550,551,-1,552,553,554,-1,555,556,557,-1,558,559,560,-1,561,562,563,-1,564,565,566,-1,567,568,569,-1,570,571,572,-1,573,574,575,-1,576,577,578,-1,579,580,581,-1,582,583,584,-1,585,586,587,-1,588,589,590,-1,591,592,593,-1,594,595,596,-1,597,598,599,-1,600,601,602,-1,603,604,605,-1,606,607,608,-1,609,610,611,-1,612,613,614,-1,615,616,617,-1,618,619,620,-1,621,622,623,-1,624,625,626,-1,627,628,629,-1,630,631,632,-1,633,634,635,-1,636,637,638,-1,639,640,641,-1,642,643,644,-1,645,646,647,-1,648,649,650,-1,651,652,653,-1,654,655,656,-1,657,658,659,-1,660,661,662,-1,663,664,665,-1,666,667,668,-1,669,670,671,-1]
IndexedFaceSet250.creaseAngle = 1.48
Coordinate251 = x3d.Coordinate()

IndexedFaceSet250.coord = Coordinate251

Shape247.geometry = IndexedFaceSet250

Transform246.children.append(Shape247)

fieldValue245.children.append(Transform246)

ProtoInstance243.fieldValue.append(fieldValue245)

fieldValue242.children.append(ProtoInstance243)

ProtoInstance239.fieldValue.append(fieldValue242)

fieldValue228.children.append(ProtoInstance239)

ProtoInstance225.fieldValue.append(fieldValue228)

fieldValue214.children.append(ProtoInstance225)

ProtoInstance211.fieldValue.append(fieldValue214)

fieldValue200.children.append(ProtoInstance211)
ProtoInstance252 = x3d.ProtoInstance()
ProtoInstance252.name = "Joint"
ProtoInstance252.DEF = "hanim_r_shoulder"
fieldValue253 = x3d.fieldValue()
fieldValue253.name = "name"
fieldValue253.value = "r_shoulder"

ProtoInstance252.fieldValue.append(fieldValue253)
fieldValue254 = x3d.fieldValue()
fieldValue254.name = "center"
fieldValue254.value = "-0.167 1.36 -0.0458"

ProtoInstance252.fieldValue.append(fieldValue254)
fieldValue255 = x3d.fieldValue()
fieldValue255.name = "children"
ProtoInstance256 = x3d.ProtoInstance()
ProtoInstance256.name = "Segment"
ProtoInstance256.DEF = "hanim_r_upperarm"
fieldValue257 = x3d.fieldValue()
fieldValue257.name = "name"
fieldValue257.value = "r_upperarm"

ProtoInstance256.fieldValue.append(fieldValue257)
fieldValue258 = x3d.fieldValue()
fieldValue258.name = "children"
Transform259 = x3d.Transform()
Transform259.DEF = "r_upperarm_adjust"
Transform259.center = [0.27,1,-0.025]
Transform259.rotation = [0,1,0,1.570796]
Transform259.scale = [0.1,0.1,0.1]
Shape260 = x3d.Shape()
Appearance261 = x3d.Appearance()
Material262 = x3d.Material()
Material262.USE = "Skin_Color"

Appearance261.material = Material262
ImageTexture263 = x3d.ImageTexture()
ImageTexture263.USE = "camo"

Appearance261.texture = ImageTexture263

Shape260.appearance = Appearance261
IndexedFaceSet264 = x3d.IndexedFaceSet()
IndexedFaceSet264.coordIndex = [0,1,2,-1,3,4,5,-1,6,7,8,-1,9,10,11,-1,12,13,14,-1,15,16,17,-1,18,19,20,-1,21,22,23,-1,24,25,26,-1,27,28,29,-1,30,31,32,-1,33,34,35,-1,36,37,38,-1,39,40,41,-1,42,43,44,-1,45,46,47,-1,48,49,50,-1,51,52,53,-1,54,55,56,-1,57,58,59,-1,60,61,62,-1,63,64,65,-1,66,67,68,-1,69,70,71,-1,72,73,74,-1,75,76,77,-1,78,79,80,-1,81,82,83,-1,84,85,86,-1,87,88,89,-1,90,91,92,-1,93,94,95,-1,96,97,98,-1,99,100,101,-1,102,103,104,-1,105,106,107,-1,108,109,110,-1,111,112,113,-1,114,115,116,-1,117,118,119,-1,120,121,122,-1,123,124,125,-1,126,127,128,-1,129,130,131,-1,132,133,134,-1,135,136,137,-1,138,139,140,-1,141,142,143,-1,144,145,146,-1,147,148,149,-1,150,151,152,-1,153,154,155,-1,156,157,158,-1,159,160,161,-1,162,163,164,-1,165,166,167,-1,168,169,170,-1,171,172,173,-1,174,175,176,-1,177,178,179,-1,180,181,182,-1,183,184,185,-1,186,187,188,-1,189,190,191,-1,192,193,194,-1,195,196,197,-1,198,199,200,-1,201,202,203,-1,204,205,206,-1,207,208,209,-1,210,211,212,-1,213,214,215,-1,216,217,218,-1,219,220,221,-1,222,223,224,-1,225,226,227,-1,228,229,230,-1,231,232,233,-1,234,235,236,-1,237,238,239,-1,240,241,242,-1,243,244,245,-1,246,247,248,-1,249,250,251,-1,252,253,254,-1,255,256,257,-1,258,259,260,-1,261,262,263,-1,264,265,266,-1,267,268,269,-1,270,271,272,-1,273,274,275,-1,276,277,278,-1,279,280,281,-1,282,283,284,-1,285,286,287,-1,288,289,290,-1,291,292,293,-1,294,295,296,-1,297,298,299,-1,300,301,302,-1,303,304,305,-1,306,307,308,-1,309,310,311,-1,312,313,314,-1,315,316,317,-1,318,319,320,-1,321,322,323,-1,324,325,326,-1,327,328,329,-1,330,331,332,-1,333,334,335,-1,336,337,338,-1,339,340,341,-1,342,343,344,-1,345,346,347,-1,348,349,350,-1,351,352,353,-1,354,355,356,-1,357,358,359,-1,360,361,362,-1,363,364,365,-1,366,367,368,-1,369,370,371,-1,372,373,374,-1,375,376,377,-1,378,379,380,-1,381,382,383,-1,384,385,386,-1,387,388,389,-1,390,391,392,-1,393,394,395,-1,396,397,398,-1,399,400,401,-1,402,403,404,-1,405,406,407,-1,408,409,410,-1,411,412,413,-1,414,415,416,-1,417,418,419,-1,420,421,422,-1,423,424,425,-1,426,427,428,-1,429,430,431,-1,432,433,434,-1,435,436,437,-1,438,439,440,-1,441,442,443,-1,444,445,446,-1,447,448,449,-1,450,451,452,-1,453,454,455,-1,456,457,458,-1,459,460,461,-1,462,463,464,-1,465,466,467,-1,468,469,470,-1,471,472,473,-1,474,475,476,-1,477,478,479,-1,480,481,482,-1,483,484,485,-1,486,487,488,-1,489,490,491,-1,492,493,494,-1,495,496,497,-1,498,499,500,-1,501,502,503,-1,504,505,506,-1,507,508,509,-1,510,511,512,-1,513,514,515,-1,516,517,518,-1,519,520,521,-1,522,523,524,-1,525,526,527,-1,528,529,530,-1,531,532,533,-1,534,535,536,-1,537,538,539,-1,540,541,542,-1,543,544,545,-1,546,547,548,-1,549,550,551,-1,552,553,554,-1,555,556,557,-1,558,559,560,-1,561,562,563,-1,564,565,566,-1,567,568,569,-1,570,571,572,-1,573,574,575,-1,576,577,578,-1,579,580,581,-1,582,583,584,-1,585,586,587,-1,588,589,590,-1,591,592,593,-1,594,595,596,-1,597,598,599,-1,600,601,602,-1,603,604,605,-1,606,607,608,-1,609,610,611,-1,612,613,614,-1,615,616,617,-1,618,619,620,-1,621,622,623,-1,624,625,626,-1,627,628,629,-1,630,631,632,-1,633,634,635,-1,636,637,638,-1,639,640,641,-1,642,643,644,-1,645,646,647,-1,648,649,650,-1,651,652,653,-1,654,655,656,-1,657,658,659,-1,660,661,662,-1,663,664,665,-1,666,667,668,-1,669,670,671,-1,672,673,674,-1,675,676,677,-1,678,679,680,-1,681,682,683,-1,684,685,686,-1,687,688,689,-1,690,691,692,-1,693,694,695,-1,696,697,698,-1,699,700,701,-1,702,703,704,-1,705,706,707,-1,708,709,710,-1,711,712,713,-1,714,715,716,-1,717,718,719,-1,720,721,722,-1,723,724,725,-1,726,727,728,-1,729,730,731,-1,732,733,734,-1,735,736,737,-1,738,739,740,-1,741,742,743,-1,744,745,746,-1,747,748,749,-1,750,751,752,-1,753,754,755,-1,756,757,758,-1,759,760,761,-1,762,763,764,-1,765,766,767,-1,768,769,770,-1,771,772,773,-1,774,775,776,-1,777,778,779,-1,780,781,782,-1,783,784,785,-1,786,787,788,-1,789,790,791,-1,792,793,794,-1,795,796,797,-1,798,799,800,-1,801,802,803,-1,804,805,806,-1,807,808,809,-1,810,811,812,-1,813,814,815,-1,816,817,818,-1,819,820,821,-1,822,823,824,-1,825,826,827,-1,828,829,830,-1,831,832,833,-1,834,835,836,-1,837,838,839,-1,840,841,842,-1,843,844,845,-1,846,847,848,-1,849,850,851,-1,852,853,854,-1,855,856,857,-1,858,859,860,-1,861,862,863,-1,864,865,866,-1,867,868,869,-1,870,871,872,-1,873,874,875,-1,876,877,878,-1,879,880,881,-1,882,883,884,-1,885,886,887,-1,888,889,890,-1,891,892,893,-1,894,895,896,-1,897,898,899,-1,900,901,902,-1,903,904,905,-1,906,907,908,-1,909,910,911,-1,912,913,914,-1,915,916,917,-1,918,919,920,-1,921,922,923,-1,924,925,926,-1,927,928,929,-1,930,931,932,-1,933,934,935,-1,936,937,938,-1,939,940,941,-1,942,943,944,-1,945,946,947,-1,948,949,950,-1,951,952,953,-1,954,955,956,-1,957,958,959,-1,960,961,962,-1,963,964,965,-1,966,967,968,-1,969,970,971,-1,972,973,974,-1,975,976,977,-1,978,979,980,-1,981,982,983,-1,984,985,986,-1,987,988,989,-1,990,991,992,-1,993,994,995,-1,996,997,998,-1,999,1000,1001,-1,1002,1003,1004,-1,1005,1006,1007,-1,1008,1009,1010,-1,1011,1012,1013,-1,1014,1015,1016,-1,1017,1018,1019,-1,1020,1021,1022,-1,1023,1024,1025,-1,1026,1027,1028,-1,1029,1030,1031,-1,1032,1033,1034,-1,1035,1036,1037,-1,1038,1039,1040,-1,1041,1042,1043,-1,1044,1045,1046,-1,1047,1048,1049,-1,1050,1051,1052,-1,1053,1054,1055,-1,1056,1057,1058,-1,1059,1060,1061,-1,1062,1063,1064,-1,1065,1066,1067,-1,1068,1069,1070,-1,1071,1072,1073,-1,1074,1075,1076,-1,1077,1078,1079,-1,1080,1081,1082,-1,1083,1084,1085,-1,1086,1087,1088,-1,1089,1090,1091,-1,1092,1093,1094,-1,1095,1096,1097,-1,1098,1099,1100,-1,1101,1102,1103,-1,1104,1105,1106,-1,1107,1108,1109,-1,1110,1111,1112,-1,1113,1114,1115,-1,1116,1117,1118,-1,1119,1120,1121,-1,1122,1123,1124,-1,1125,1126,1127,-1,1128,1129,1130,-1,1131,1132,1133,-1,1134,1135,1136,-1,1137,1138,1139,-1,1140,1141,1142,-1,1143,1144,1145,-1,1146,1147,1148,-1,1149,1150,1151,-1,1152,1153,1154,-1,1155,1156,1157,-1,1158,1159,1160,-1,1161,1162,1163,-1,1164,1165,1166,-1,1167,1168,1169,-1,1170,1171,1172,-1,1173,1174,1175,-1,1176,1177,1178,-1,1179,1180,1181,-1,1182,1183,1184,-1,1185,1186,1187,-1,1188,1189,1190,-1,1191,1192,1193,-1,1194,1195,1196,-1,1197,1198,1199,-1,1200,1201,1202,-1,1203,1204,1205,-1,1206,1207,1208,-1,1209,1210,1211,-1,1212,1213,1214,-1,1215,1216,1217,-1,1218,1219,1220,-1,1221,1222,1223,-1,1224,1225,1226,-1,1227,1228,1229,-1,1230,1231,1232,-1,1233,1234,1235,-1,1236,1237,1238,-1,1239,1240,1241,-1,1242,1243,1244,-1,1245,1246,1247,-1,1248,1249,1250,-1,1251,1252,1253,-1,1254,1255,1256,-1,1257,1258,1259,-1,1260,1261,1262,-1,1263,1264,1265,-1,1266,1267,1268,-1,1269,1270,1271,-1,1272,1273,1274,-1,1275,1276,1277,-1,1278,1279,1280,-1,1281,1282,1283,-1,1284,1285,1286,-1,1287,1288,1289,-1,1290,1291,1292,-1,1293,1294,1295,-1,1296,1297,1298,-1,1299,1300,1301,-1,1302,1303,1304,-1,1305,1306,1307,-1,1308,1309,1310,-1,1311,1312,1313,-1,1314,1315,1316,-1,1317,1318,1319,-1,1320,1321,1322,-1,1323,1324,1325,-1,1326,1327,1328,-1,1329,1330,1331,-1,1332,1333,1334,-1,1335,1336,1337,-1,1338,1339,1340,-1,1341,1342,1343,-1,1344,1345,1346,-1,1347,1348,1349,-1,1350,1351,1352,-1,1353,1354,1355,-1,1356,1357,1358,-1,1359,1360,1361,-1,1362,1363,1364,-1,1365,1366,1367,-1,1368,1369,1370,-1,1371,1372,1373,-1,1374,1375,1376,-1,1377,1378,1379,-1,1380,1381,1382,-1,1383,1384,1385,-1,1386,1387,1388,-1,1389,1390,1391,-1,1392,1393,1394,-1,1395,1396,1397,-1,1398,1399,1400,-1,1401,1402,1403,-1,1404,1405,1406,-1,1407,1408,1409,-1,1410,1411,1412,-1,1413,1414,1415,-1,1416,1417,1418,-1,1419,1420,1421,-1,1422,1423,1424,-1,1425,1426,1427,-1,1428,1429,1430,-1,1431,1432,1433,-1,1434,1435,1436,-1,1437,1438,1439,-1,1440,1441,1442,-1,1443,1444,1445,-1,1446,1447,1448,-1,1449,1450,1451,-1,1452,1453,1454,-1,1455,1456,1457,-1,1458,1459,1460,-1,1461,1462,1463,-1,1464,1465,1466,-1,1467,1468,1469,-1,1470,1471,1472,-1,1473,1474,1475,-1,1476,1477,1478,-1,1479,1480,1481,-1,1482,1483,1484,-1,1485,1486,1487,-1,1488,1489,1490,-1,1491,1492,1493,-1,1494,1495,1496,-1,1497,1498,1499,-1,1500,1501,1502,-1,1503,1504,1505,-1,1506,1507,1508,-1,1509,1510,1511,-1,1512,1513,1514,-1,1515,1516,1517,-1,1518,1519,1520,-1,1521,1522,1523,-1,1524,1525,1526,-1,1527,1528,1529,-1,1530,1531,1532,-1,1533,1534,1535,-1,1536,1537,1538,-1,1539,1540,1541,-1,1542,1543,1544,-1,1545,1546,1547,-1,1548,1549,1550,-1,1551,1552,1553,-1,1554,1555,1556,-1,1557,1558,1559,-1,1560,1561,1562,-1,1563,1564,1565,-1,1566,1567,1568,-1,1569,1570,1571,-1,1572,1573,1574,-1,1575,1576,1577,-1,1578,1579,1580,-1,1581,1582,1583,-1,1584,1585,1586,-1,1587,1588,1589,-1,1590,1591,1592,-1,1593,1594,1595,-1,1596,1597,1598,-1,1599,1600,1601,-1,1602,1603,1604,-1,1605,1606,1607,-1,1608,1609,1610,-1,1611,1612,1613,-1,1614,1615,1616,-1,1617,1618,1619,-1,1620,1621,1622,-1,1623,1624,1625,-1,1626,1627,1628,-1,1629,1630,1631,-1,1632,1633,1634,-1,1635,1636,1637,-1,1638,1639,1640,-1,1641,1642,1643,-1,1644,1645,1646,-1,1647,1648,1649,-1,1650,1651,1652,-1,1653,1654,1655,-1,1656,1657,1658,-1,1659,1660,1661,-1,1662,1663,1664,-1,1665,1666,1667,-1,1668,1669,1670,-1,1671,1672,1673,-1,1674,1675,1676,-1,1677,1678,1679,-1,1680,1681,1682,-1,1683,1684,1685,-1,1686,1687,1688,-1,1689,1690,1691,-1,1692,1693,1694,-1,1695,1696,1697,-1,1698,1699,1700,-1,1701,1702,1703,-1,1704,1705,1706,-1,1707,1708,1709,-1,1710,1711,1712,-1,1713,1714,1715,-1,1716,1717,1718,-1,1719,1720,1721,-1,1722,1723,1724,-1,1725,1726,1727,-1,1728,1729,1730,-1,1731,1732,1733,-1,1734,1735,1736,-1,1737,1738,1739,-1,1740,1741,1742,-1,1743,1744,1745,-1,1746,1747,1748,-1,1749,1750,1751,-1,1752,1753,1754,-1,1755,1756,1757,-1,1758,1759,1760,-1,1761,1762,1763,-1,1764,1765,1766,-1,1767,1768,1769,-1,1770,1771,1772,-1,1773,1774,1775,-1,1776,1777,1778,-1,1779,1780,1781,-1,1782,1783,1784,-1,1785,1786,1787,-1,1788,1789,1790,-1,1791,1792,1793,-1,1794,1795,1796,-1,1797,1798,1799,-1,1800,1801,1802,-1,1803,1804,1805,-1,1806,1807,1808,-1,1809,1810,1811,-1,1812,1813,1814,-1]
IndexedFaceSet264.creaseAngle = 1.53
Coordinate265 = x3d.Coordinate()

IndexedFaceSet264.coord = Coordinate265

Shape260.geometry = IndexedFaceSet264

Transform259.children.append(Shape260)

fieldValue258.children.append(Transform259)

ProtoInstance256.fieldValue.append(fieldValue258)

fieldValue255.children.append(ProtoInstance256)
ProtoInstance266 = x3d.ProtoInstance()
ProtoInstance266.name = "Joint"
ProtoInstance266.DEF = "hanim_r_elbow"
fieldValue267 = x3d.fieldValue()
fieldValue267.name = "name"
fieldValue267.value = "r_elbow"

ProtoInstance266.fieldValue.append(fieldValue267)
fieldValue268 = x3d.fieldValue()
fieldValue268.name = "center"
fieldValue268.value = "-0.192 1.07 -0.0498"

ProtoInstance266.fieldValue.append(fieldValue268)
fieldValue269 = x3d.fieldValue()
fieldValue269.name = "children"
ProtoInstance270 = x3d.ProtoInstance()
ProtoInstance270.name = "Segment"
ProtoInstance270.DEF = "hanim_r_forearm"
fieldValue271 = x3d.fieldValue()
fieldValue271.name = "name"
fieldValue271.value = "r_forearm"

ProtoInstance270.fieldValue.append(fieldValue271)
fieldValue272 = x3d.fieldValue()
fieldValue272.name = "children"
Transform273 = x3d.Transform()
Transform273.DEF = "r_forearm_adjust"
Transform273.center = [0.7641,1.01,-0.07438]
Transform273.rotation = [0,1,0,1.570796]
Transform273.scale = [0.1,0.1,0.1]
Shape274 = x3d.Shape()
Appearance275 = x3d.Appearance()
Material276 = x3d.Material()
Material276.USE = "Skin_Color"

Appearance275.material = Material276
ImageTexture277 = x3d.ImageTexture()
ImageTexture277.USE = "camo"

Appearance275.texture = ImageTexture277

Shape274.appearance = Appearance275
IndexedFaceSet278 = x3d.IndexedFaceSet()
IndexedFaceSet278.coordIndex = [0,1,2,-1,3,4,5,-1,6,7,8,-1,9,10,11,-1,12,13,14,-1,15,16,17,-1,18,19,20,-1,21,22,23,-1,24,25,26,-1,27,28,29,-1,30,31,32,-1,33,34,35,-1,36,37,38,-1,39,40,41,-1,42,43,44,-1,45,46,47,-1,48,49,50,-1,51,52,53,-1,54,55,56,-1,57,58,59,-1,60,61,62,-1,63,64,65,-1,66,67,68,-1,69,70,71,-1,72,73,74,-1,75,76,77,-1,78,79,80,-1,81,82,83,-1,84,85,86,-1,87,88,89,-1,90,91,92,-1,93,94,95,-1,96,97,98,-1,99,100,101,-1,102,103,104,-1,105,106,107,-1,108,109,110,-1,111,112,113,-1,114,115,116,-1,117,118,119,-1,120,121,122,-1,123,124,125,-1,126,127,128,-1,129,130,131,-1,132,133,134,-1,135,136,137,-1,138,139,140,-1,141,142,143,-1,144,145,146,-1,147,148,149,-1,150,151,152,-1,153,154,155,-1,156,157,158,-1,159,160,161,-1,162,163,164,-1,165,166,167,-1,168,169,170,-1,171,172,173,-1,174,175,176,-1,177,178,179,-1,180,181,182,-1,183,184,185,-1,186,187,188,-1,189,190,191,-1,192,193,194,-1,195,196,197,-1,198,199,200,-1,201,202,203,-1,204,205,206,-1,207,208,209,-1,210,211,212,-1,213,214,215,-1,216,217,218,-1,219,220,221,-1,222,223,224,-1,225,226,227,-1,228,229,230,-1,231,232,233,-1,234,235,236,-1,237,238,239,-1,240,241,242,-1,243,244,245,-1,246,247,248,-1,249,250,251,-1,252,253,254,-1,255,256,257,-1,258,259,260,-1,261,262,263,-1,264,265,266,-1,267,268,269,-1,270,271,272,-1,273,274,275,-1,276,277,278,-1,279,280,281,-1,282,283,284,-1,285,286,287,-1,288,289,290,-1,291,292,293,-1,294,295,296,-1,297,298,299,-1,300,301,302,-1,63,65,60,-1,36,40,37,-1,40,39,37,-1,39,43,37,-1,43,42,37,-1,48,51,49,-1,60,65,61,-1,49,51,50,-1,51,53,50,-1,50,53,48,-1,48,53,47,-1,47,53,45,-1,45,53,42,-1,42,53,37,-1,53,54,37,-1,54,56,37,-1,65,37,61,-1,37,56,61,-1,62,61,60,-1,59,58,56,-1,56,58,61,-1,60,61,58,-1,303,304,305,-1,306,307,308,-1,309,310,311,-1,312,313,314,-1,315,316,317,-1,318,319,320,-1,321,322,323,-1,324,325,326,-1,327,328,329,-1,330,331,332,-1,333,334,335,-1,336,337,338,-1,339,340,341,-1,342,343,344,-1,345,346,347,-1,348,349,350,-1,351,352,353,-1,354,355,356,-1,357,358,359,-1,360,361,362,-1,363,364,365,-1,366,367,368,-1,369,370,371,-1,372,373,374,-1,375,376,377,-1,378,379,380,-1,381,382,383,-1,384,385,386,-1,387,388,389,-1,390,391,392,-1,393,394,395,-1,396,397,398,-1,399,400,401,-1,402,403,404,-1,405,406,407,-1,408,409,410,-1,411,412,413,-1,414,415,416,-1,417,418,419,-1,420,421,422,-1,423,424,425,-1,426,427,428,-1,429,430,431,-1,432,433,434,-1,435,436,437,-1,438,439,440,-1,441,442,443,-1,444,445,446,-1,447,448,449,-1,450,451,452,-1,453,454,455,-1,456,457,458,-1,459,460,461,-1,462,463,464,-1,465,466,467,-1,468,469,470,-1,471,472,473,-1,474,475,476,-1,477,478,479,-1,480,481,482,-1,483,484,485,-1,486,487,488,-1,489,490,491,-1,492,493,494,-1,495,496,497,-1,498,499,500,-1,501,502,503,-1,504,505,506,-1,507,508,509,-1,510,511,512,-1,513,514,515,-1,516,517,518,-1,519,520,521,-1,522,523,524,-1,525,526,527,-1,528,529,530,-1,531,532,533,-1,534,535,536,-1,537,538,539,-1,540,541,542,-1,543,544,545,-1,546,547,548,-1,549,550,551,-1,552,553,554,-1,555,556,557,-1,558,559,560,-1,561,562,563,-1,564,565,566,-1,567,568,569,-1,570,571,572,-1,573,574,575,-1,576,577,578,-1,579,580,581,-1,582,583,584,-1,585,586,587,-1,588,589,590,-1,591,592,593,-1,594,595,596,-1,597,598,599,-1,600,601,602,-1,603,604,605,-1,606,607,608,-1,609,610,611,-1,612,613,614,-1,615,616,617,-1,618,619,620,-1,621,622,623,-1,624,625,626,-1,627,628,629,-1,630,631,632,-1,633,634,635,-1,636,637,638,-1,639,640,641,-1,642,643,644,-1,645,646,647,-1,648,649,650,-1,651,652,653,-1,654,655,656,-1,657,658,659,-1,660,661,662,-1,663,664,665,-1,666,667,668,-1,669,670,671,-1,672,673,674,-1,675,676,677,-1,678,679,680,-1,681,682,683,-1,684,685,686,-1,687,688,689,-1,690,691,692,-1,693,694,695,-1,696,697,698,-1,699,700,701,-1,702,703,704,-1,705,706,707,-1,708,709,710,-1,711,712,713,-1,714,715,716,-1,717,718,719,-1,720,721,722,-1,723,724,725,-1,726,727,728,-1,729,730,731,-1,732,733,734,-1,735,736,737,-1,738,739,740,-1,741,742,743,-1,744,745,746,-1,747,748,749,-1,750,751,752,-1,753,754,755,-1,756,757,758,-1,759,760,761,-1,762,763,764,-1,765,766,767,-1,768,769,770,-1,771,772,773,-1,774,775,776,-1,777,778,779,-1,780,781,782,-1,783,784,785,-1,786,787,788,-1,789,790,791,-1,792,793,794,-1,795,796,797,-1,798,799,800,-1,801,802,803,-1,804,805,806,-1,807,808,809,-1,810,811,812,-1,813,814,815,-1,816,817,818,-1,819,820,821,-1,822,823,824,-1,825,826,827,-1,828,829,830,-1,831,832,833,-1,834,835,836,-1,837,838,839,-1,840,841,842,-1,843,844,845,-1,846,847,848,-1,849,850,851,-1,852,853,854,-1,855,856,857,-1,858,859,860,-1,861,862,863,-1,864,865,866,-1,867,868,869,-1,870,871,872,-1,873,874,875,-1,876,877,878,-1,879,880,881,-1,882,883,884,-1,885,886,887,-1,888,889,890,-1,891,892,893,-1,894,895,896,-1,897,898,899,-1,900,901,902,-1,903,904,905,-1,906,907,908,-1,909,910,911,-1,912,913,914,-1,915,916,917,-1,918,919,920,-1,921,922,923,-1,924,925,926,-1,927,928,929,-1,930,931,932,-1,933,934,935,-1,936,937,938,-1,939,940,941,-1,942,943,944,-1,945,946,947,-1,948,949,950,-1,951,952,953,-1,954,955,956,-1,957,958,959,-1,960,961,962,-1,963,964,965,-1,966,967,968,-1,969,970,971,-1,972,973,974,-1,975,976,977,-1,978,979,980,-1,981,982,983,-1,984,985,986,-1,987,988,989,-1,990,991,992,-1,993,994,995,-1,996,997,998,-1,999,1000,1001,-1,1002,1003,1004,-1,1005,1006,1007,-1,1008,1009,1010,-1,1011,1012,1013,-1,1014,1015,1016,-1,1017,1018,1019,-1,1020,1021,1022,-1,1023,1024,1025,-1,1026,1027,1028,-1,1029,1030,1031,-1,1032,1033,1034,-1,1035,1036,1037,-1,1038,1039,1040,-1,1041,1042,1043,-1,1044,1045,1046,-1,1047,1048,1049,-1,1050,1051,1052,-1,1053,1054,1055,-1,1056,1057,1058,-1,1059,1060,1061,-1,1062,1063,1064,-1,1065,1066,1067,-1,1068,1069,1070,-1,1071,1072,1073,-1,1074,1075,1076,-1,1077,1078,1079,-1,1080,1081,1082,-1,1083,1084,1085,-1,1086,1087,1088,-1,1089,1090,1091,-1,1092,1093,1094,-1,1095,1096,1097,-1,1098,1099,1100,-1,1101,1102,1103,-1,1104,1105,1106,-1,1107,1108,1109,-1,1110,1111,1112,-1,1113,1114,1115,-1,1116,1117,1118,-1,1119,1120,1121,-1,1122,1123,1124,-1,1125,1126,1127,-1,1128,1129,1130,-1,1131,1132,1133,-1,1134,1135,1136,-1,1137,1138,1139,-1,1140,1141,1142,-1,1143,1144,1145,-1,1146,1147,1148,-1,1149,1150,1151,-1,1152,1153,1154,-1,1155,1156,1157,-1,1158,1159,1160,-1,1161,1162,1163,-1,1164,1165,1166,-1,1167,1168,1169,-1,1170,1171,1172,-1,1173,1174,1175,-1,1176,1177,1178,-1,1179,1180,1181,-1,1182,1183,1184,-1,1185,1186,1187,-1,1188,1189,1190,-1,1191,1192,1193,-1,1194,1195,1196,-1,1197,1198,1199,-1,1200,1201,1202,-1,1203,1204,1205,-1,1206,1207,1208,-1,1209,1210,1211,-1,1212,1213,1214,-1,1215,1216,1217,-1,1218,1219,1220,-1,1221,1222,1223,-1,1224,1225,1226,-1,1227,1228,1229,-1,1230,1231,1232,-1,1233,1234,1235,-1,1236,1237,1238,-1,1239,1240,1241,-1,1242,1243,1244,-1,1245,1246,1247,-1,1248,1249,1250,-1,1251,1252,1253,-1,1254,1255,1256,-1,1257,1258,1259,-1,1260,1261,1262,-1,1263,1264,1265,-1,1266,1267,1268,-1,1269,1270,1271,-1,1272,1273,1274,-1,1275,1276,1277,-1,1278,1279,1280,-1,1281,1282,1283,-1,1284,1285,1286,-1,1287,1288,1289,-1,1290,1291,1292,-1,1293,1294,1295,-1,1296,1297,1298,-1,1299,1300,1301,-1,1302,1303,1304,-1,1305,1306,1307,-1,1308,1309,1310,-1,1311,1312,1313,-1,1314,1315,1316,-1,1317,1318,1319,-1,1320,1321,1322,-1,1323,1324,1325,-1,1326,1327,1328,-1,1329,1330,1331,-1,1332,1333,1334,-1,1335,1336,1337,-1,1338,1339,1340,-1,1341,1342,1343,-1,1344,1345,1346,-1,1347,1348,1349,-1,1350,1351,1352,-1,1353,1354,1355,-1,1356,1357,1358,-1,1359,1360,1361,-1,1362,1363,1364,-1,1365,1366,1367,-1,1368,1369,1370,-1,1371,1372,1373,-1,1374,1375,1376,-1,1377,1378,1379,-1,1380,1381,1382,-1,1383,1384,1385,-1,1386,1387,1388,-1,1389,1390,1391,-1,1392,1393,1394,-1,1395,1396,1397,-1,1398,1399,1400,-1,1401,1402,1403,-1,1404,1405,1406,-1,1407,1408,1409,-1,1410,1411,1412,-1,1413,1414,1415,-1,1416,1417,1418,-1,1419,1420,1421,-1,1422,1423,1424,-1,1425,1426,1427,-1,1428,1429,1430,-1,1431,1432,1433,-1,1434,1435,1436,-1,1437,1438,1439,-1,1440,1441,1442,-1,1443,1444,1445,-1,1446,1447,1448,-1,1449,1450,1451,-1,1452,1453,1454,-1,1455,1456,1457,-1,1458,1459,1460,-1,1461,1462,1463,-1,1464,1465,1466,-1,1467,1468,1469,-1,1470,1471,1472,-1,1473,1474,1475,-1,1476,1477,1478,-1,1479,1480,1481,-1,1482,1483,1484,-1,1485,1486,1487,-1,1488,1489,1490,-1,1491,1492,1493,-1,1494,1495,1496,-1,1497,1498,1499,-1,1500,1501,1502,-1,1503,1504,1505,-1,1506,1507,1508,-1,1509,1510,1511,-1,1512,1513,1514,-1,1515,1516,1517,-1,1518,1519,1520,-1,1521,1522,1523,-1,1524,1525,1526,-1,1527,1528,1529,-1,1530,1531,1532,-1,1533,1534,1535,-1,1536,1537,1538,-1,1539,1540,1541,-1,1542,1543,1544,-1,1545,1546,1547,-1,1548,1549,1550,-1,1551,1552,1553,-1,1554,1555,1556,-1,1557,1558,1559,-1,1560,1561,1562,-1,1563,1564,1565,-1,1566,1567,1568,-1,1569,1570,1571,-1,1572,1573,1574,-1,1575,1576,1577,-1,1578,1579,1580,-1,1581,1582,1583,-1,1584,1585,1586,-1,1587,1588,1589,-1,1590,1591,1592,-1,1593,1594,1595,-1,1596,1597,1598,-1,1599,1600,1601,-1,1602,1603,1604,-1,1605,1606,1607,-1,1608,1609,1610,-1,1611,1612,1613,-1,1614,1615,1616,-1,1617,1618,1619,-1,1620,1621,1622,-1,1623,1624,1625,-1,1626,1627,1628,-1,1629,1630,1631,-1,1632,1633,1634,-1,1635,1636,1637,-1,1638,1639,1640,-1,1641,1642,1643,-1,1644,1645,1646,-1,1647,1648,1649,-1,1650,1651,1652,-1,1653,1654,1655,-1,1656,1657,1658,-1,1659,1660,1661,-1,1662,1663,1664,-1,1665,1666,1667,-1,1668,1669,1670,-1,1671,1672,1673,-1,1674,1675,1676,-1,1677,1678,1679,-1,1680,1681,1682,-1,1683,1684,1685,-1,1686,1687,1688,-1,1689,1690,1691,-1,1692,1693,1694,-1,1695,1696,1697,-1,1698,1699,1700,-1,1701,1702,1703,-1,1704,1705,1706,-1,1707,1708,1709,-1,1710,1711,1712,-1,1713,1714,1715,-1,1716,1717,1718,-1,1719,1720,1721,-1]
IndexedFaceSet278.creaseAngle = 1.73
Coordinate279 = x3d.Coordinate()

IndexedFaceSet278.coord = Coordinate279

Shape274.geometry = IndexedFaceSet278

Transform273.children.append(Shape274)

fieldValue272.children.append(Transform273)

ProtoInstance270.fieldValue.append(fieldValue272)

fieldValue269.children.append(ProtoInstance270)
ProtoInstance280 = x3d.ProtoInstance()
ProtoInstance280.name = "Joint"
ProtoInstance280.DEF = "hanim_r_wrist"
fieldValue281 = x3d.fieldValue()
fieldValue281.name = "name"
fieldValue281.value = "r_wrist"

ProtoInstance280.fieldValue.append(fieldValue281)
fieldValue282 = x3d.fieldValue()
fieldValue282.name = "center"
fieldValue282.value = "-0.217 0.811 -0.0338"

ProtoInstance280.fieldValue.append(fieldValue282)
fieldValue283 = x3d.fieldValue()
fieldValue283.name = "children"
ProtoInstance284 = x3d.ProtoInstance()
ProtoInstance284.name = "Segment"
ProtoInstance284.DEF = "hanim_r_hand"
fieldValue285 = x3d.fieldValue()
fieldValue285.name = "name"
fieldValue285.value = "r_hand"

ProtoInstance284.fieldValue.append(fieldValue285)
fieldValue286 = x3d.fieldValue()
fieldValue286.name = "children"
Transform287 = x3d.Transform()
Transform287.DEF = "r_hand_adjust"
Transform287.center = [0.2693,1.011,-0.0248]
Transform287.rotation = [0,1,0,1.570796]
Transform287.scale = [0.1,0.1,0.1]
Shape288 = x3d.Shape()
Appearance289 = x3d.Appearance()
Material290 = x3d.Material()
Material290.USE = "Skin_Color"

Appearance289.material = Material290

Shape288.appearance = Appearance289
IndexedFaceSet291 = x3d.IndexedFaceSet()
IndexedFaceSet291.coordIndex = [0,1,2,-1,3,4,5,-1,6,7,8,-1,9,10,11,-1,12,13,14,-1,15,16,17,-1,18,19,20,-1,21,22,23,-1,24,25,26,-1,27,28,29,-1,30,31,32,-1,33,34,35,-1,36,37,38,-1,39,40,41,-1,42,43,44,-1,45,46,47,-1,48,49,50,-1,51,52,53,-1,54,55,56,-1,57,58,59,-1,60,61,62,-1,63,64,65,-1,66,67,68,-1,69,70,71,-1,72,73,74,-1,75,76,77,-1,78,79,80,-1,81,82,83,-1,84,85,86,-1,87,88,89,-1,90,91,92,-1,93,94,95,-1,96,97,98,-1,99,100,101,-1,102,103,104,-1,105,106,107,-1,108,109,110,-1,111,112,113,-1,114,115,116,-1,117,118,119,-1,120,121,122,-1,123,124,125,-1,126,127,128,-1,129,130,131,-1,132,133,134,-1,135,136,137,-1,138,139,140,-1,141,142,143,-1,144,145,146,-1,147,148,149,-1,150,151,152,-1,153,154,155,-1,156,157,158,-1,159,160,161,-1,162,163,164,-1,165,166,167,-1,168,169,170,-1,171,172,173,-1,174,175,176,-1,177,178,179,-1,180,181,182,-1,183,184,185,-1,186,187,188,-1,189,190,191,-1,192,193,194,-1,195,196,197,-1,198,199,200,-1,201,202,203,-1,204,205,206,-1,207,208,209,-1,210,211,212,-1,213,214,215,-1,216,217,218,-1,219,220,221,-1,222,223,224,-1,225,226,227,-1,228,229,230,-1,231,232,233,-1,234,235,236,-1,237,238,239,-1,240,241,242,-1,243,244,245,-1,246,247,248,-1,249,250,251,-1,252,253,254,-1,255,256,257,-1,258,259,260,-1,261,262,263,-1,264,265,266,-1,267,268,269,-1,270,271,272,-1,273,274,275,-1,276,277,278,-1,279,280,281,-1,282,283,284,-1,285,286,287,-1,288,289,290,-1,291,292,293,-1,294,295,296,-1,297,298,299,-1,300,301,302,-1,303,304,305,-1,306,307,308,-1,309,310,311,-1,312,313,314,-1,315,316,317,-1,318,319,320,-1,321,322,323,-1,324,325,326,-1,327,328,329,-1,330,331,332,-1,333,334,335,-1,336,337,338,-1,339,340,341,-1,342,343,344,-1,345,346,347,-1,348,349,350,-1,351,352,353,-1,354,355,356,-1,357,358,359,-1,360,361,362,-1,363,364,365,-1,366,367,368,-1,369,370,371,-1,372,373,374,-1,375,376,377,-1,378,379,380,-1,381,382,383,-1,384,385,386,-1,387,388,389,-1,390,391,392,-1,393,394,395,-1,396,397,398,-1,399,400,401,-1,402,403,404,-1,405,406,407,-1,408,409,410,-1,411,412,413,-1,414,415,416,-1,417,418,419,-1,420,421,422,-1,423,424,425,-1,426,427,428,-1,429,430,431,-1,432,433,434,-1,435,436,437,-1,438,439,440,-1,441,442,443,-1,444,445,446,-1,447,448,449,-1,450,451,452,-1,453,454,455,-1,456,457,458,-1,459,460,461,-1,462,463,464,-1,465,466,467,-1,468,469,470,-1,471,472,473,-1,474,475,476,-1,477,478,479,-1,480,481,482,-1,483,484,485,-1,486,487,488,-1,489,490,491,-1,492,493,494,-1,495,496,497,-1,498,499,500,-1,501,502,503,-1,504,505,506,-1,507,508,509,-1,510,511,512,-1,513,514,515,-1,516,517,518,-1,519,520,521,-1,522,523,524,-1,525,526,527,-1,528,529,530,-1,531,532,533,-1,534,535,536,-1,537,538,539,-1,540,541,542,-1,543,544,545,-1,546,547,548,-1,549,550,551,-1,552,553,554,-1,555,556,557,-1,558,559,560,-1,561,562,563,-1,564,565,566,-1,567,568,569,-1,570,571,572,-1,573,574,575,-1,576,577,578,-1,579,580,581,-1,582,583,584,-1,585,586,587,-1,588,589,590,-1,591,592,593,-1,594,595,596,-1,597,598,599,-1,600,601,602,-1,603,604,605,-1,606,607,608,-1,609,610,611,-1,612,613,614,-1,615,616,617,-1,618,619,620,-1,621,622,623,-1,624,625,626,-1,627,628,629,-1,630,631,632,-1,633,634,635,-1,636,637,638,-1,639,640,641,-1,642,643,644,-1,645,646,647,-1,648,649,650,-1,651,652,653,-1,654,655,656,-1,657,658,659,-1,660,661,662,-1,663,664,665,-1,666,667,668,-1,669,670,671,-1,672,673,674,-1,675,676,677,-1,678,679,680,-1,681,682,683,-1,684,685,686,-1,687,688,689,-1,690,691,692,-1,694,695,693,-1]
IndexedFaceSet291.creaseAngle = 1.57
Coordinate292 = x3d.Coordinate()

IndexedFaceSet291.coord = Coordinate292

Shape288.geometry = IndexedFaceSet291

Transform287.children.append(Shape288)

fieldValue286.children.append(Transform287)

ProtoInstance284.fieldValue.append(fieldValue286)

fieldValue283.children.append(ProtoInstance284)

ProtoInstance280.fieldValue.append(fieldValue283)

fieldValue269.children.append(ProtoInstance280)

ProtoInstance266.fieldValue.append(fieldValue269)

fieldValue255.children.append(ProtoInstance266)

ProtoInstance252.fieldValue.append(fieldValue255)

fieldValue200.children.append(ProtoInstance252)
ProtoInstance293 = x3d.ProtoInstance()
ProtoInstance293.name = "Joint"
ProtoInstance293.DEF = "hanim_vc4"
fieldValue294 = x3d.fieldValue()
fieldValue294.name = "name"
fieldValue294.value = "vc4"

ProtoInstance293.fieldValue.append(fieldValue294)
fieldValue295 = x3d.fieldValue()
fieldValue295.name = "center"
fieldValue295.value = "0 1.43 -0.0458"

ProtoInstance293.fieldValue.append(fieldValue295)
fieldValue296 = x3d.fieldValue()
fieldValue296.name = "children"
ProtoInstance297 = x3d.ProtoInstance()
ProtoInstance297.name = "Segment"
ProtoInstance297.DEF = "hanim_c4"
fieldValue298 = x3d.fieldValue()
fieldValue298.name = "name"
fieldValue298.value = "c4"

ProtoInstance297.fieldValue.append(fieldValue298)
fieldValue299 = x3d.fieldValue()
fieldValue299.name = "children"
Transform300 = x3d.Transform()
Transform300.DEF = "neck_adjust"
Transform300.center = [-0.36,1.03,0.04]
Transform300.rotation = [0,1,0,1.570796]
Transform300.scale = [0.1,0.1,0.1]
Shape301 = x3d.Shape()
Appearance302 = x3d.Appearance()
Material303 = x3d.Material()
Material303.USE = "Skin_Color"

Appearance302.material = Material303
ImageTexture304 = x3d.ImageTexture()
ImageTexture304.USE = "camo"

Appearance302.texture = ImageTexture304

Shape301.appearance = Appearance302
IndexedFaceSet305 = x3d.IndexedFaceSet()
IndexedFaceSet305.DEF = "neck"
IndexedFaceSet305.coordIndex = [0,1,2,-1,3,4,5,-1,6,7,8,-1,9,10,11,-1,12,13,14,-1,15,16,17,-1,18,19,20,-1,21,22,23,-1,24,25,26,-1,27,28,29,-1,30,31,32,-1,33,34,35,-1,36,37,38,-1,39,40,41,-1,42,43,44,-1,45,46,47,-1,48,49,50,-1,51,52,53,-1,54,55,56,-1,57,58,59,-1,60,61,62,-1,63,64,65,-1,66,67,68,-1,69,70,71,-1,72,73,74,-1,75,76,77,-1,78,79,80,-1,81,82,83,-1,84,85,86,-1,87,88,89,-1,90,91,92,-1,93,94,95,-1,96,97,98,-1,99,100,101,-1,102,103,104,-1,105,106,107,-1,108,109,110,-1,111,112,113,-1,114,115,116,-1,117,118,119,-1,120,121,122,-1,123,124,125,-1,126,127,128,-1,129,130,131,-1,132,133,134,-1,135,136,137,-1,138,139,140,-1,141,142,143,-1,144,145,146,-1,147,148,149,-1,150,151,152,-1,153,154,155,-1,156,157,158,-1,159,160,161,-1,162,163,164,-1,165,166,167,-1,168,169,170,-1,171,172,173,-1,174,175,176,-1,177,178,179,-1,180,181,182,-1,183,184,185,-1,186,187,188,-1,189,190,191,-1,192,193,194,-1,195,196,197,-1,198,199,200,-1,201,202,203,-1,204,205,206,-1,207,208,209,-1,210,211,212,-1,213,214,215,-1,216,217,218,-1,219,220,221,-1,222,223,224,-1,225,226,227,-1,228,229,230,-1,231,232,233,-1,234,235,236,-1,237,238,239,-1,240,241,242,-1,243,244,245,-1,246,247,248,-1,249,250,251,-1,252,253,254,-1,255,256,257,-1,258,259,260,-1,261,262,263,-1,264,265,266,-1,267,268,269,-1,270,271,272,-1,273,274,275,-1,276,277,278,-1,279,280,281,-1,282,283,284,-1,285,286,287,-1,288,289,290,-1,291,292,293,-1,294,295,296,-1,297,298,299,-1,300,301,302,-1,303,304,305,-1,306,307,308,-1,309,310,311,-1,312,313,314,-1,315,316,317,-1,318,319,320,-1,321,322,323,-1,324,325,326,-1,327,328,329,-1,330,331,332,-1,333,334,335,-1,336,337,338,-1,339,340,341,-1,342,343,344,-1,345,346,347,-1,348,349,350,-1,351,352,353,-1,354,355,356,-1,357,358,359,-1,360,361,362,-1,363,364,365,-1,366,367,368,-1,369,370,371,-1,372,373,374,-1,375,376,377,-1,378,379,380,-1,381,382,383,-1,384,385,386,-1,387,388,389,-1,390,391,392,-1,393,394,395,-1,396,397,398,-1,399,400,401,-1,402,403,404,-1,405,406,407,-1,408,409,410,-1,411,412,413,-1,414,415,416,-1,417,418,419,-1,420,421,422,-1,423,424,425,-1,426,427,428,-1,429,430,431,-1,432,433,434,-1,435,436,437,-1,438,439,440,-1,441,442,443,-1,444,445,446,-1,447,448,449,-1,450,451,452,-1,453,454,455,-1,456,457,458,-1,459,460,461,-1,462,463,464,-1,465,466,467,-1,468,469,470,-1,471,472,473,-1,474,475,476,-1,477,478,479,-1,480,481,482,-1,483,484,485,-1,486,487,488,-1,489,490,491,-1,492,493,494,-1,495,496,497,-1,498,499,500,-1,501,502,503,-1,504,505,506,-1,507,508,509,-1,510,511,512,-1,513,514,515,-1,516,517,518,-1,519,520,521,-1,522,523,524,-1,525,526,527,-1,528,529,530,-1,531,532,533,-1,534,535,536,-1,537,538,539,-1,540,541,542,-1,543,544,545,-1,546,547,548,-1,549,550,551,-1,552,553,554,-1,555,556,557,-1,558,559,560,-1,561,562,563,-1,564,565,566,-1,567,568,569,-1,570,571,572,-1,573,574,575,-1,576,577,578,-1,579,580,581,-1,582,583,584,-1]
IndexedFaceSet305.creaseAngle = 1.91
Coordinate306 = x3d.Coordinate()

IndexedFaceSet305.coord = Coordinate306

Shape301.geometry = IndexedFaceSet305

Transform300.children.append(Shape301)

fieldValue299.children.append(Transform300)

ProtoInstance297.fieldValue.append(fieldValue299)

fieldValue296.children.append(ProtoInstance297)
ProtoInstance307 = x3d.ProtoInstance()
ProtoInstance307.name = "Joint"
ProtoInstance307.DEF = "hanim_skullbase"
fieldValue308 = x3d.fieldValue()
fieldValue308.name = "name"
fieldValue308.value = "skullbase"

ProtoInstance307.fieldValue.append(fieldValue308)
fieldValue309 = x3d.fieldValue()
fieldValue309.name = "rotation"
fieldValue309.value = "0 1 0 0"

ProtoInstance307.fieldValue.append(fieldValue309)
fieldValue310 = x3d.fieldValue()
fieldValue310.name = "center"
fieldValue310.value = "0 1.4 0"

ProtoInstance307.fieldValue.append(fieldValue310)
fieldValue311 = x3d.fieldValue()
fieldValue311.name = "children"
ProtoInstance312 = x3d.ProtoInstance()
ProtoInstance312.name = "Segment"
ProtoInstance312.DEF = "hanim_skull"
fieldValue313 = x3d.fieldValue()
fieldValue313.name = "name"
fieldValue313.value = "skull"

ProtoInstance312.fieldValue.append(fieldValue313)
fieldValue314 = x3d.fieldValue()
fieldValue314.name = "children"
Transform315 = x3d.Transform()
Transform315.DEF = "skull_adjust"
Transform315.center = [-0.07,1.33,-0.035]
Transform315.scale = [0.001,0.001,0.001]
Shape316 = x3d.Shape()
Appearance317 = x3d.Appearance()
Material318 = x3d.Material()
Material318.USE = "Skin_Color"

Appearance317.material = Material318
ImageTexture319 = x3d.ImageTexture()
ImageTexture319.url = ["clone.gif","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Prototypes/clone.gif"]

Appearance317.texture = ImageTexture319

Shape316.appearance = Appearance317
IndexedFaceSet320 = x3d.IndexedFaceSet()
IndexedFaceSet320.coordIndex = [0,1,2,-1,2,3,0,-1,4,0,3,-1,3,5,4,-1,6,4,5,-1,5,7,6,-1,8,6,7,-1,9,10,11,-1,11,12,9,-1,13,9,12,-1,12,14,13,-1,15,13,14,-1,14,16,15,-1,17,15,16,-1,16,18,17,-1,19,17,18,-1,20,21,1,-1,1,0,20,-1,22,20,0,-1,0,4,22,-1,23,22,4,-1,4,6,23,-1,24,23,6,-1,6,8,24,-1,25,24,8,-1,26,27,28,-1,28,29,26,-1,30,26,29,-1,29,31,30,-1,32,30,31,-1,31,33,32,-1,34,32,33,-1,33,35,34,-1,36,34,35,-1,35,37,36,-1,38,36,37,-1,37,10,38,-1,39,38,10,-1,10,9,39,-1,40,39,9,-1,9,13,40,-1,41,40,13,-1,13,15,41,-1,42,41,15,-1,15,17,42,-1,43,42,17,-1,17,19,43,-1,44,43,19,-1,19,45,44,-1,46,44,45,-1,45,47,46,-1,48,46,47,-1,47,49,48,-1,50,48,49,-1,49,51,50,-1,52,50,51,-1,51,53,52,-1,54,52,53,-1,55,56,21,-1,21,20,55,-1,57,55,20,-1,20,22,57,-1,58,57,22,-1,22,23,58,-1,59,58,23,-1,23,24,59,-1,60,59,24,-1,24,25,60,-1,61,60,25,-1,62,63,64,-1,64,65,62,-1,66,62,65,-1,67,68,69,-1,69,27,67,-1,70,67,27,-1,27,26,70,-1,71,70,26,-1,26,30,71,-1,72,71,30,-1,30,32,72,-1,73,72,32,-1,32,34,73,-1,74,73,34,-1,34,36,74,-1,75,74,36,-1,36,38,75,-1,76,75,38,-1,38,39,76,-1,77,76,39,-1,39,40,77,-1,78,77,40,-1,40,41,78,-1,79,78,41,-1,41,42,79,-1,80,79,42,-1,42,43,80,-1,81,80,43,-1,43,44,81,-1,82,81,44,-1,44,46,82,-1,83,82,46,-1,46,48,83,-1,84,83,48,-1,48,50,84,-1,85,84,50,-1,50,52,85,-1,86,85,52,-1,52,54,86,-1,87,86,54,-1,54,88,87,-1,89,87,88,-1,88,56,89,-1,90,89,56,-1,56,55,90,-1,91,90,55,-1,55,57,91,-1,92,91,57,-1,57,58,92,-1,93,92,58,-1,58,59,93,-1,94,93,59,-1,59,60,94,-1,95,94,60,-1,60,61,95,-1,96,95,61,-1,61,97,96,-1,98,96,97,-1,97,63,98,-1,99,98,63,-1,63,62,99,-1,100,99,62,-1,62,66,100,-1,101,102,68,-1,68,67,101,-1,103,101,67,-1,67,70,103,-1,104,103,70,-1,70,71,104,-1,105,104,71,-1,71,72,105,-1,106,105,72,-1,72,73,106,-1,107,106,73,-1,73,74,107,-1,108,107,74,-1,74,75,108,-1,109,108,75,-1,75,76,109,-1,110,109,76,-1,76,77,110,-1,111,110,77,-1,77,78,111,-1,112,111,78,-1,78,79,112,-1,113,112,79,-1,79,80,113,-1,114,113,80,-1,80,81,114,-1,115,114,81,-1,81,82,115,-1,116,115,82,-1,82,83,116,-1,117,116,83,-1,83,84,117,-1,118,117,84,-1,84,85,118,-1,119,118,85,-1,85,86,119,-1,120,119,86,-1,86,87,120,-1,121,120,87,-1,87,89,121,-1,122,121,89,-1,89,90,122,-1,123,122,90,-1,90,91,123,-1,124,123,91,-1,91,92,124,-1,125,124,92,-1,92,93,125,-1,126,125,93,-1,93,94,126,-1,127,126,94,-1,94,95,127,-1,128,127,95,-1,95,96,128,-1,129,128,96,-1,96,98,129,-1,130,129,98,-1,98,99,130,-1,131,130,99,-1,99,100,131,-1,132,133,102,-1,102,101,132,-1,134,132,101,-1,101,103,134,-1,135,134,103,-1,103,104,135,-1,136,135,104,-1,104,105,136,-1,137,136,105,-1,105,106,137,-1,138,137,106,-1,106,107,138,-1,139,138,107,-1,107,108,139,-1,140,139,108,-1,108,109,140,-1,141,140,109,-1,109,110,141,-1,142,141,110,-1,110,111,142,-1,143,142,111,-1,111,112,143,-1,144,143,112,-1,112,113,144,-1,145,144,113,-1,113,114,145,-1,146,145,114,-1,114,115,146,-1,147,146,115,-1,115,116,147,-1,148,147,116,-1,116,117,148,-1,149,148,117,-1,117,118,149,-1,150,149,118,-1,118,119,150,-1,151,150,119,-1,119,120,151,-1,152,151,120,-1,120,121,152,-1,153,152,121,-1,121,122,153,-1,154,153,122,-1,122,123,154,-1,155,154,123,-1,123,124,155,-1,156,155,124,-1,124,125,156,-1,157,156,125,-1,125,126,157,-1,158,157,126,-1,126,127,158,-1,159,158,127,-1,127,128,159,-1,160,159,128,-1,128,129,160,-1,161,160,129,-1,129,130,161,-1,162,161,130,-1,130,131,162,-1,163,164,165,-1,165,166,163,-1,167,163,166,-1,166,168,167,-1,169,167,168,-1,168,133,169,-1,170,169,133,-1,133,132,170,-1,171,170,132,-1,132,134,171,-1,172,171,134,-1,134,135,172,-1,173,172,135,-1,135,136,173,-1,174,173,136,-1,136,137,174,-1,175,174,137,-1,137,138,175,-1,176,175,138,-1,138,139,176,-1,177,176,139,-1,139,140,177,-1,178,177,140,-1,140,141,178,-1,179,178,141,-1,141,142,179,-1,180,179,142,-1,142,143,180,-1,181,180,143,-1,143,144,181,-1,182,181,144,-1,144,145,182,-1,183,182,145,-1,145,146,183,-1,184,183,146,-1,146,147,184,-1,185,184,147,-1,147,148,185,-1,186,185,148,-1,148,149,186,-1,187,186,149,-1,149,150,187,-1,188,187,150,-1,150,151,188,-1,189,188,151,-1,151,152,189,-1,190,189,152,-1,152,153,190,-1,191,190,153,-1,153,154,191,-1,192,191,154,-1,154,155,192,-1,193,192,155,-1,155,156,193,-1,194,193,156,-1,156,157,194,-1,195,194,157,-1,157,158,195,-1,196,195,158,-1,158,159,196,-1,197,196,159,-1,159,160,197,-1,198,197,160,-1,160,161,198,-1,199,198,161,-1,161,162,199,-1,200,199,162,-1,164,163,201,-1,202,201,163,-1,163,167,202,-1,203,202,167,-1,167,169,203,-1,204,203,169,-1,169,170,204,-1,205,204,170,-1,170,171,205,-1,206,205,171,-1,171,172,206,-1,207,206,172,-1,172,173,207,-1,208,207,173,-1,173,174,208,-1,209,208,174,-1,174,175,209,-1,210,209,175,-1,175,176,210,-1,211,210,176,-1,176,177,211,-1,212,211,177,-1,177,178,212,-1,213,212,178,-1,178,179,213,-1,214,213,179,-1,179,180,214,-1,215,214,180,-1,180,181,215,-1,216,215,181,-1,181,182,216,-1,217,216,182,-1,182,183,217,-1,218,217,183,-1,183,184,218,-1,219,218,184,-1,184,185,219,-1,220,219,185,-1,185,186,220,-1,221,220,186,-1,186,187,221,-1,222,221,187,-1,187,188,222,-1,223,222,188,-1,188,189,223,-1,224,223,189,-1,189,190,224,-1,225,224,190,-1,190,191,225,-1,226,225,191,-1,191,192,226,-1,227,226,192,-1,192,193,227,-1,228,227,193,-1,193,194,228,-1,229,228,194,-1,194,195,229,-1,230,229,195,-1,195,196,230,-1,231,230,196,-1,196,197,231,-1,232,231,197,-1,197,198,232,-1,233,232,198,-1,198,199,233,-1,234,233,199,-1,199,200,234,-1,202,203,235,-1,236,235,203,-1,203,204,236,-1,237,236,204,-1,204,205,237,-1,238,237,205,-1,205,206,238,-1,239,238,206,-1,206,207,239,-1,240,239,207,-1,207,208,240,-1,241,240,208,-1,208,209,241,-1,242,241,209,-1,209,210,242,-1,243,242,210,-1,210,211,243,-1,244,243,211,-1,211,212,244,-1,245,244,212,-1,212,213,245,-1,246,245,213,-1,213,214,246,-1,247,246,214,-1,214,215,247,-1,248,247,215,-1,215,216,248,-1,249,248,216,-1,216,217,249,-1,250,249,217,-1,217,218,250,-1,251,250,218,-1,218,219,251,-1,252,251,219,-1,219,220,252,-1,253,252,220,-1,220,221,253,-1,254,253,221,-1,221,222,254,-1,255,254,222,-1,222,223,255,-1,256,255,223,-1,223,224,256,-1,257,256,224,-1,224,225,257,-1,258,257,225,-1,225,226,258,-1,259,258,226,-1,226,227,259,-1,260,259,227,-1,227,228,260,-1,261,260,228,-1,228,229,261,-1,262,261,229,-1,229,230,262,-1,263,262,230,-1,230,231,263,-1,264,263,231,-1,231,232,264,-1,265,264,232,-1,232,233,265,-1,266,265,233,-1,233,234,266,-1,267,266,234,-1,235,236,268,-1,269,268,236,-1,236,237,269,-1,270,269,237,-1,237,238,270,-1,271,270,238,-1,238,239,271,-1,272,271,239,-1,239,240,272,-1,273,272,240,-1,240,241,273,-1,274,273,241,-1,241,242,274,-1,275,274,242,-1,242,243,275,-1,276,275,243,-1,243,244,276,-1,277,276,244,-1,244,245,277,-1,278,277,245,-1,245,246,278,-1,279,278,246,-1,246,247,279,-1,280,279,247,-1,247,248,280,-1,281,280,248,-1,248,249,281,-1,282,281,249,-1,249,250,282,-1,283,282,250,-1,250,251,283,-1,284,283,251,-1,251,252,284,-1,285,284,252,-1,252,253,285,-1,286,285,253,-1,253,254,286,-1,287,286,254,-1,254,255,287,-1,288,287,255,-1,255,256,288,-1,289,288,256,-1,256,257,289,-1,290,289,257,-1,257,258,290,-1,291,290,258,-1,258,259,291,-1,292,291,259,-1,259,260,292,-1,293,292,260,-1,260,261,293,-1,294,293,261,-1,261,262,294,-1,295,294,262,-1,262,263,295,-1,296,295,263,-1,263,264,296,-1,297,296,264,-1,264,265,297,-1,298,297,265,-1,265,266,298,-1,299,298,266,-1,266,267,299,-1,300,301,268,-1,268,269,300,-1,302,300,269,-1,269,270,302,-1,303,302,270,-1,270,271,303,-1,304,303,271,-1,271,272,304,-1,305,304,272,-1,272,273,305,-1,306,305,273,-1,273,274,306,-1,307,306,274,-1,274,275,307,-1,308,307,275,-1,275,276,308,-1,309,308,276,-1,276,277,309,-1,310,309,277,-1,277,278,310,-1,311,310,278,-1,278,279,311,-1,312,311,279,-1,279,280,312,-1,313,312,280,-1,280,281,313,-1,314,313,281,-1,281,282,314,-1,315,314,282,-1,282,283,315,-1,316,315,283,-1,283,284,316,-1,317,316,284,-1,284,285,317,-1,318,317,285,-1,285,286,318,-1,319,318,286,-1,286,287,319,-1,320,319,287,-1,287,288,320,-1,321,320,288,-1,288,289,321,-1,322,321,289,-1,289,290,322,-1,323,322,290,-1,290,291,323,-1,324,323,291,-1,291,292,324,-1,325,324,292,-1,292,293,325,-1,326,325,293,-1,293,294,326,-1,327,326,294,-1,294,295,327,-1,328,327,295,-1,295,296,328,-1,329,328,296,-1,296,297,329,-1,330,329,297,-1,297,298,330,-1,331,330,298,-1,298,299,331,-1,332,333,301,-1,301,300,332,-1,334,332,300,-1,300,302,334,-1,335,334,302,-1,302,303,335,-1,336,335,303,-1,303,304,336,-1,337,336,304,-1,304,305,337,-1,338,337,305,-1,305,306,338,-1,339,338,306,-1,306,307,339,-1,340,339,307,-1,307,308,340,-1,341,340,308,-1,308,309,341,-1,342,341,309,-1,309,310,342,-1,343,342,310,-1,310,311,343,-1,344,343,311,-1,311,312,344,-1,345,344,312,-1,312,313,345,-1,346,345,313,-1,313,314,346,-1,347,346,314,-1,314,315,347,-1,348,347,315,-1,315,316,348,-1,349,348,316,-1,316,317,349,-1,350,349,317,-1,317,318,350,-1,351,350,318,-1,318,319,351,-1,352,351,319,-1,319,320,352,-1,353,352,320,-1,320,321,353,-1,354,353,321,-1,321,322,354,-1,355,354,322,-1,322,323,355,-1,356,355,323,-1,323,324,356,-1,357,356,324,-1,324,325,357,-1,358,357,325,-1,325,326,358,-1,359,358,326,-1,326,327,359,-1,360,359,327,-1,327,328,360,-1,361,360,328,-1,328,329,361,-1,362,361,329,-1,329,330,362,-1,363,362,330,-1,330,331,363,-1,364,363,331,-1,333,332,365,-1,366,365,332,-1,332,334,366,-1,367,366,334,-1,334,335,367,-1,368,367,335,-1,335,336,368,-1,369,368,336,-1,336,337,369,-1,370,369,337,-1,337,338,370,-1,371,370,338,-1,338,339,371,-1,372,371,339,-1,339,340,372,-1,373,372,340,-1,340,341,373,-1,374,373,341,-1,341,342,374,-1,375,374,342,-1,342,343,375,-1,376,375,343,-1,343,344,376,-1,377,376,344,-1,344,345,377,-1,378,377,345,-1,345,346,378,-1,379,378,346,-1,346,347,379,-1,380,379,347,-1,347,348,380,-1,381,380,348,-1,348,349,381,-1,382,381,349,-1,349,350,382,-1,383,382,350,-1,350,351,383,-1,384,383,351,-1,351,352,384,-1,385,384,352,-1,352,353,385,-1,386,385,353,-1,353,354,386,-1,387,386,354,-1,354,355,387,-1,388,387,355,-1,355,356,388,-1,389,388,356,-1,356,357,389,-1,390,389,357,-1,357,358,390,-1,391,390,358,-1,358,359,391,-1,392,391,359,-1,359,360,392,-1,393,392,360,-1,360,361,393,-1,394,393,361,-1,361,362,394,-1,395,394,362,-1,362,363,395,-1,396,395,363,-1,363,364,396,-1,397,398,365,-1,365,366,397,-1,399,397,366,-1,366,367,399,-1,400,399,367,-1,367,368,400,-1,401,400,368,-1,368,369,401,-1,402,401,369,-1,369,370,402,-1,403,402,370,-1,370,371,403,-1,404,403,371,-1,371,372,404,-1,405,404,372,-1,372,373,405,-1,406,405,373,-1,373,374,406,-1,407,406,374,-1,374,375,407,-1,408,407,375,-1,375,376,408,-1,409,408,376,-1,376,377,409,-1,410,409,377,-1,377,378,410,-1,411,410,378,-1,378,379,411,-1,412,411,379,-1,379,380,412,-1,413,412,380,-1,380,381,413,-1,414,413,381,-1,381,382,414,-1,415,414,382,-1,382,383,415,-1,416,415,383,-1,383,384,416,-1,417,416,384,-1,384,385,417,-1,418,417,385,-1,385,386,418,-1,419,418,386,-1,386,387,419,-1,420,419,387,-1,387,388,420,-1,421,420,388,-1,388,389,421,-1,422,421,389,-1,389,390,422,-1,423,422,390,-1,390,391,423,-1,424,423,391,-1,391,392,424,-1,425,424,392,-1,392,393,425,-1,426,425,393,-1,393,394,426,-1,427,426,394,-1,394,395,427,-1,428,427,395,-1,395,396,428,-1,429,430,398,-1,398,397,429,-1,431,429,397,-1,397,399,431,-1,432,431,399,-1,399,400,432,-1,433,432,400,-1,400,401,433,-1,434,433,401,-1,401,402,434,-1,435,434,402,-1,402,403,435,-1,436,435,403,-1,403,404,436,-1,437,436,404,-1,404,405,437,-1,438,437,405,-1,405,406,438,-1,439,438,406,-1,406,407,439,-1,440,439,407,-1,407,408,440,-1,441,440,408,-1,408,409,441,-1,442,441,409,-1,409,410,442,-1,443,442,410,-1,410,411,443,-1,444,443,411,-1,411,412,444,-1,445,444,412,-1,412,413,445,-1,446,445,413,-1,413,414,446,-1,447,446,414,-1,414,415,447,-1,448,447,415,-1,415,416,448,-1,449,448,416,-1,416,417,449,-1,450,449,417,-1,417,418,450,-1,451,450,418,-1,418,419,451,-1,452,451,419,-1,419,420,452,-1,453,452,420,-1,420,421,453,-1,454,453,421,-1,421,422,454,-1,455,454,422,-1,422,423,455,-1,456,455,423,-1,423,424,456,-1,457,456,424,-1,424,425,457,-1,458,457,425,-1,425,426,458,-1,459,458,426,-1,426,427,459,-1,460,459,427,-1,427,428,460,-1,430,429,461,-1,462,461,429,-1,429,431,462,-1,463,462,431,-1,431,432,463,-1,464,463,432,-1,432,433,464,-1,465,464,433,-1,433,434,465,-1,466,465,434,-1,434,435,466,-1,467,466,435,-1,435,436,467,-1,468,467,436,-1,436,437,468,-1,469,468,437,-1,437,438,469,-1,470,469,438,-1,438,439,470,-1,471,470,439,-1,439,440,471,-1,472,471,440,-1,440,441,472,-1,473,472,441,-1,441,442,473,-1,474,473,442,-1,442,443,474,-1,475,474,443,-1,443,444,475,-1,476,475,444,-1,444,445,476,-1,477,476,445,-1,445,446,477,-1,478,477,446,-1,446,447,478,-1,479,478,447,-1,447,448,479,-1,480,479,448,-1,448,449,480,-1,481,480,449,-1,449,450,481,-1,482,481,450,-1,450,451,482,-1,483,482,451,-1,451,452,483,-1,484,483,452,-1,452,453,484,-1,485,484,453,-1,453,454,485,-1,486,485,454,-1,454,455,486,-1,487,486,455,-1,455,456,487,-1,488,487,456,-1,456,457,488,-1,489,488,457,-1,457,458,489,-1,490,489,458,-1,458,459,490,-1,491,490,459,-1,459,460,491,-1,492,493,461,-1,461,462,492,-1,494,492,462,-1,462,463,494,-1,495,494,463,-1,463,464,495,-1,496,495,464,-1,464,465,496,-1,497,496,465,-1,465,466,497,-1,498,497,466,-1,466,467,498,-1,499,498,467,-1,467,468,499,-1,500,499,468,-1,468,469,500,-1,501,500,469,-1,469,470,501,-1,502,501,470,-1,470,471,502,-1,503,502,471,-1,471,472,503,-1,504,503,472,-1,472,473,504,-1,505,504,473,-1,473,474,505,-1,506,505,474,-1,474,475,506,-1,507,506,475,-1,475,476,507,-1,508,507,476,-1,476,477,508,-1,509,508,477,-1,477,478,509,-1,510,509,478,-1,478,479,510,-1,511,510,479,-1,479,480,511,-1,512,511,480,-1,480,481,512,-1,513,512,481,-1,481,482,513,-1,514,513,482,-1,482,483,514,-1,515,514,483,-1,483,484,515,-1,516,515,484,-1,484,485,516,-1,517,516,485,-1,485,486,517,-1,518,517,486,-1,486,487,518,-1,519,518,487,-1,487,488,519,-1,520,519,488,-1,488,489,520,-1,521,520,489,-1,489,490,521,-1,493,492,522,-1,523,522,492,-1,492,494,523,-1,524,523,494,-1,494,495,524,-1,525,524,495,-1,495,496,525,-1,526,525,496,-1,496,497,526,-1,527,526,497,-1,497,498,527,-1,528,527,498,-1,498,499,528,-1,529,528,499,-1,499,500,529,-1,530,529,500,-1,500,501,530,-1,531,530,501,-1,501,502,531,-1,532,531,502,-1,502,503,532,-1,533,532,503,-1,503,504,533,-1,534,533,504,-1,504,505,534,-1,535,534,505,-1,505,506,535,-1,536,535,506,-1,506,507,536,-1,537,536,507,-1,507,508,537,-1,538,537,508,-1,508,509,538,-1,539,538,509,-1,509,510,539,-1,540,539,510,-1,510,511,540,-1,541,540,511,-1,511,512,541,-1,542,541,512,-1,512,513,542,-1,543,542,513,-1,513,514,543,-1,544,543,514,-1,514,515,544,-1,545,544,515,-1,515,516,545,-1,546,545,516,-1,516,517,546,-1,547,546,517,-1,517,518,547,-1,548,547,518,-1,518,519,548,-1,549,548,519,-1,519,520,549,-1,550,549,520,-1,520,521,550,-1,551,550,521,-1,523,524,552,-1,553,552,524,-1,524,525,553,-1,554,553,525,-1,525,526,554,-1,555,554,526,-1,526,527,555,-1,556,555,527,-1,527,528,556,-1,557,556,528,-1,528,529,557,-1,558,557,529,-1,529,530,558,-1,559,558,530,-1,530,531,559,-1,560,559,531,-1,531,532,560,-1,561,560,532,-1,532,533,561,-1,562,561,533,-1,533,534,562,-1,563,562,534,-1,534,535,563,-1,564,563,535,-1,535,536,564,-1,565,564,536,-1,536,537,565,-1,566,565,537,-1,537,538,566,-1,567,566,538,-1,538,539,567,-1,568,567,539,-1,539,540,568,-1,569,568,540,-1,540,541,569,-1,570,569,541,-1,541,542,570,-1,571,570,542,-1,542,543,571,-1,572,571,543,-1,543,544,572,-1,573,572,544,-1,544,545,573,-1,574,573,545,-1,545,546,574,-1,575,574,546,-1,546,547,575,-1,576,575,547,-1,547,548,576,-1,577,576,548,-1,548,549,577,-1,578,577,549,-1,549,550,578,-1,579,578,550,-1,550,551,579,-1,580,581,552,-1,552,553,580,-1,582,580,553,-1,553,554,582,-1,583,582,554,-1,554,555,583,-1,584,583,555,-1,555,556,584,-1,585,584,556,-1,556,557,585,-1,586,585,557,-1,557,558,586,-1,587,586,558,-1,558,559,587,-1,588,587,559,-1,559,560,588,-1,589,588,560,-1,560,561,589,-1,590,589,561,-1,561,562,590,-1,591,590,562,-1,562,563,591,-1,592,591,563,-1,563,564,592,-1,593,592,564,-1,564,565,593,-1,594,593,565,-1,565,566,594,-1,595,594,566,-1,566,567,595,-1,596,595,567,-1,567,568,596,-1,597,596,568,-1,568,569,597,-1,598,597,569,-1,569,570,598,-1,599,598,570,-1,570,571,599,-1,600,599,571,-1,571,572,600,-1,601,600,572,-1,572,573,601,-1,602,601,573,-1,573,574,602,-1,603,602,574,-1,574,575,603,-1,604,603,575,-1,575,576,604,-1,605,604,576,-1,576,577,605,-1,606,605,577,-1,577,578,606,-1,607,608,581,-1,581,580,607,-1,609,607,580,-1,580,582,609,-1,610,609,582,-1,582,583,610,-1,611,610,583,-1,583,584,611,-1,612,611,584,-1,584,585,612,-1,613,612,585,-1,585,586,613,-1,614,613,586,-1,586,587,614,-1,615,614,587,-1,587,588,615,-1,616,615,588,-1,588,589,616,-1,617,616,589,-1,589,590,617,-1,618,617,590,-1,590,591,618,-1,619,618,591,-1,591,592,619,-1,620,619,592,-1,592,593,620,-1,621,620,593,-1,593,594,621,-1,622,621,594,-1,594,595,622,-1,623,622,595,-1,595,596,623,-1,624,623,596,-1,596,597,624,-1,625,624,597,-1,597,598,625,-1,626,625,598,-1,598,599,626,-1,627,626,599,-1,599,600,627,-1,628,627,600,-1,600,601,628,-1,629,628,601,-1,601,602,629,-1,630,629,602,-1,602,603,630,-1,631,630,603,-1,603,604,631,-1,632,631,604,-1,604,605,632,-1,633,632,605,-1,605,606,633,-1,634,635,608,-1,608,607,634,-1,636,634,607,-1,607,609,636,-1,637,636,609,-1,609,610,637,-1,638,637,610,-1,610,611,638,-1,639,638,611,-1,611,612,639,-1,640,639,612,-1,612,613,640,-1,641,640,613,-1,613,614,641,-1,642,641,614,-1,614,615,642,-1,643,642,615,-1,615,616,643,-1,644,643,616,-1,616,617,644,-1,645,644,617,-1,617,618,645,-1,646,645,618,-1,618,619,646,-1,647,646,619,-1,619,620,647,-1,648,647,620,-1,620,621,648,-1,649,648,621,-1,621,622,649,-1,650,649,622,-1,622,623,650,-1,651,650,623,-1,623,624,651,-1,652,651,624,-1,624,625,652,-1,653,652,625,-1,625,626,653,-1,654,653,626,-1,626,627,654,-1,655,654,627,-1,627,628,655,-1,656,655,628,-1,628,629,656,-1,657,656,629,-1,629,630,657,-1,658,657,630,-1,630,631,658,-1,659,658,631,-1,631,632,659,-1,660,659,632,-1,632,633,660,-1,661,660,633,-1,662,663,664,-1,664,665,662,-1,666,662,665,-1,665,635,666,-1,667,666,635,-1,635,634,667,-1,668,667,634,-1,634,636,668,-1,669,668,636,-1,636,637,669,-1,670,669,637,-1,637,638,670,-1,671,670,638,-1,638,639,671,-1,672,671,639,-1,639,640,672,-1,673,672,640,-1,640,641,673,-1,674,673,641,-1,641,642,674,-1,675,674,642,-1,642,643,675,-1,676,675,643,-1,643,644,676,-1,677,676,644,-1,644,645,677,-1,678,677,645,-1,645,646,678,-1,679,678,646,-1,646,647,679,-1,680,679,647,-1,647,648,680,-1,681,680,648,-1,648,649,681,-1,682,681,649,-1,649,650,682,-1,683,682,650,-1,650,651,683,-1,684,683,651,-1,651,652,684,-1,685,684,652,-1,652,653,685,-1,686,685,653,-1,653,654,686,-1,687,686,654,-1,654,655,687,-1,688,687,655,-1,655,656,688,-1,689,688,656,-1,656,657,689,-1,690,689,657,-1,657,658,690,-1,691,690,658,-1,658,659,691,-1,692,691,659,-1,659,660,692,-1,693,692,660,-1,660,661,693,-1,694,693,661,-1,695,696,663,-1,663,662,695,-1,697,695,662,-1,662,666,697,-1,698,697,666,-1,666,667,698,-1,699,698,667,-1,667,668,699,-1,700,699,668,-1,668,669,700,-1,701,700,669,-1,669,670,701,-1,702,701,670,-1,670,671,702,-1,703,702,671,-1,671,672,703,-1,704,703,672,-1,672,673,704,-1,705,704,673,-1,673,674,705,-1,706,705,674,-1,674,675,706,-1,707,706,675,-1,675,676,707,-1,708,707,676,-1,676,677,708,-1,709,708,677,-1,677,678,709,-1,710,709,678,-1,678,679,710,-1,711,710,679,-1,679,680,711,-1,712,711,680,-1,680,681,712,-1,713,712,681,-1,681,682,713,-1,714,713,682,-1,682,683,714,-1,715,714,683,-1,683,684,715,-1,716,715,684,-1,684,685,716,-1,717,716,685,-1,685,686,717,-1,718,717,686,-1,686,687,718,-1,719,718,687,-1,687,688,719,-1,720,719,688,-1,688,689,720,-1,721,720,689,-1,689,690,721,-1,722,721,690,-1,690,691,722,-1,723,722,691,-1,691,692,723,-1,724,723,692,-1,692,693,724,-1,725,724,693,-1,693,694,725,-1,726,725,694,-1,727,728,696,-1,696,695,727,-1,729,727,695,-1,695,697,729,-1,730,729,697,-1,697,698,730,-1,731,730,698,-1,698,699,731,-1,732,731,699,-1,699,700,732,-1,733,732,700,-1,700,701,733,-1,734,733,701,-1,701,702,734,-1,735,734,702,-1,702,703,735,-1,736,735,703,-1,703,704,736,-1,737,736,704,-1,704,705,737,-1,738,737,705,-1,705,706,738,-1,739,738,706,-1,706,707,739,-1,740,739,707,-1,707,708,740,-1,741,740,708,-1,708,709,741,-1,742,741,709,-1,709,710,742,-1,743,742,710,-1,710,711,743,-1,744,743,711,-1,711,712,744,-1,745,744,712,-1,712,713,745,-1,746,745,713,-1,713,714,746,-1,747,746,714,-1,714,715,747,-1,748,747,715,-1,715,716,748,-1,749,748,716,-1,716,717,749,-1,750,749,717,-1,717,718,750,-1,751,750,718,-1,718,719,751,-1,752,751,719,-1,719,720,752,-1,753,752,720,-1,720,721,753,-1,754,753,721,-1,721,722,754,-1,755,754,722,-1,722,723,755,-1,756,755,723,-1,723,724,756,-1,757,756,724,-1,724,725,757,-1,758,757,725,-1,725,726,758,-1,759,758,726,-1,728,727,760,-1,761,760,727,-1,727,729,761,-1,762,761,729,-1,729,730,762,-1,763,762,730,-1,730,731,763,-1,764,763,731,-1,731,732,764,-1,765,764,732,-1,732,733,765,-1,766,765,733,-1,733,734,766,-1,767,766,734,-1,734,735,767,-1,768,767,735,-1,735,736,768,-1,769,768,736,-1,736,737,769,-1,770,769,737,-1,737,738,770,-1,771,770,738,-1,738,739,771,-1,772,771,739,-1,739,740,772,-1,773,772,740,-1,740,741,773,-1,774,773,741,-1,741,742,774,-1,775,774,742,-1,742,743,775,-1,776,775,743,-1,743,744,776,-1,777,776,744,-1,744,745,777,-1,778,777,745,-1,745,746,778,-1,779,778,746,-1,746,747,779,-1,780,779,747,-1,747,748,780,-1,781,780,748,-1,748,749,781,-1,782,781,749,-1,749,750,782,-1,783,782,750,-1,750,751,783,-1,784,783,751,-1,751,752,784,-1,785,784,752,-1,752,753,785,-1,786,785,753,-1,753,754,786,-1,787,786,754,-1,754,755,787,-1,788,787,755,-1,755,756,788,-1,789,788,756,-1,756,757,789,-1,790,789,757,-1,757,758,790,-1,791,790,758,-1,758,759,791,-1,792,791,759,-1,793,794,760,-1,760,761,793,-1,795,793,761,-1,761,762,795,-1,796,795,762,-1,762,763,796,-1,797,796,763,-1,763,764,797,-1,798,797,764,-1,764,765,798,-1,799,798,765,-1,765,766,799,-1,800,799,766,-1,766,767,800,-1,801,800,767,-1,767,768,801,-1,802,801,768,-1,768,769,802,-1,803,802,769,-1,769,770,803,-1,804,803,770,-1,770,771,804,-1,805,804,771,-1,771,772,805,-1,806,805,772,-1,772,773,806,-1,807,806,773,-1,773,774,807,-1,808,807,774,-1,774,775,808,-1,809,808,775,-1,775,776,809,-1,810,809,776,-1,776,777,810,-1,811,810,777,-1,777,778,811,-1,812,811,778,-1,778,779,812,-1,813,812,779,-1,779,780,813,-1,814,813,780,-1,780,781,814,-1,815,814,781,-1,781,782,815,-1,816,815,782,-1,782,783,816,-1,817,816,783,-1,783,784,817,-1,818,817,784,-1,784,785,818,-1,819,818,785,-1,785,786,819,-1,820,819,786,-1,786,787,820,-1,821,820,787,-1,787,788,821,-1,822,821,788,-1,788,789,822,-1,823,822,789,-1,789,790,823,-1,824,823,790,-1,790,791,824,-1,825,824,791,-1,791,792,825,-1,826,825,792,-1,827,828,829,-1,829,794,827,-1,830,827,794,-1,794,793,830,-1,831,830,793,-1,793,795,831,-1,832,831,795,-1,795,796,832,-1,833,832,796,-1,796,797,833,-1,834,833,797,-1,797,798,834,-1,835,834,798,-1,798,799,835,-1,836,835,799,-1,799,800,836,-1,837,836,800,-1,800,801,837,-1,838,837,801,-1,801,802,838,-1,839,838,802,-1,802,803,839,-1,840,839,803,-1,803,804,840,-1,841,840,804,-1,804,805,841,-1,842,841,805,-1,805,806,842,-1,843,842,806,-1,806,807,843,-1,844,843,807,-1,807,808,844,-1,845,844,808,-1,808,809,845,-1,846,845,809,-1,809,810,846,-1,847,846,810,-1,810,811,847,-1,848,847,811,-1,811,812,848,-1,849,848,812,-1,812,813,849,-1,850,849,813,-1,813,814,850,-1,851,850,814,-1,814,815,851,-1,852,851,815,-1,815,816,852,-1,853,852,816,-1,816,817,853,-1,854,853,817,-1,817,818,854,-1,855,854,818,-1,818,819,855,-1,856,855,819,-1,819,820,856,-1,857,856,820,-1,820,821,857,-1,858,857,821,-1,821,822,858,-1,859,858,822,-1,822,823,859,-1,860,859,823,-1,823,824,860,-1,861,860,824,-1,824,825,861,-1,862,861,825,-1,825,826,862,-1,863,862,826,-1,864,865,828,-1,828,827,864,-1,866,864,827,-1,827,830,866,-1,867,866,830,-1,830,831,867,-1,868,867,831,-1,831,832,868,-1,869,868,832,-1,832,833,869,-1,870,869,833,-1,833,834,870,-1,871,870,834,-1,834,835,871,-1,872,871,835,-1,835,836,872,-1,873,872,836,-1,836,837,873,-1,874,873,837,-1,837,838,874,-1,875,874,838,-1,838,839,875,-1,876,875,839,-1,839,840,876,-1,877,876,840,-1,840,841,877,-1,878,877,841,-1,841,842,878,-1,879,878,842,-1,842,843,879,-1,880,879,843,-1,843,844,880,-1,881,880,844,-1,844,845,881,-1,882,881,845,-1,845,846,882,-1,883,882,846,-1,846,847,883,-1,884,883,847,-1,847,848,884,-1,885,884,848,-1,848,849,885,-1,886,885,849,-1,849,850,886,-1,887,886,850,-1,850,851,887,-1,888,887,851,-1,851,852,888,-1,889,888,852,-1,852,853,889,-1,890,889,853,-1,853,854,890,-1,891,890,854,-1,854,855,891,-1,892,891,855,-1,855,856,892,-1,893,892,856,-1,856,857,893,-1,894,893,857,-1,857,858,894,-1,895,894,858,-1,858,859,895,-1,896,895,859,-1,859,860,896,-1,897,896,860,-1,860,861,897,-1,898,897,861,-1,861,862,898,-1,899,898,862,-1,862,863,899,-1,900,899,863,-1,901,902,865,-1,865,864,901,-1,903,901,864,-1,864,866,903,-1,904,903,866,-1,866,867,904,-1,905,904,867,-1,867,868,905,-1,906,905,868,-1,868,869,906,-1,907,906,869,-1,869,870,907,-1,908,907,870,-1,870,871,908,-1,909,908,871,-1,871,872,909,-1,910,909,872,-1,872,873,910,-1,911,910,873,-1,873,874,911,-1,912,911,874,-1,874,875,912,-1,913,912,875,-1,875,876,913,-1,914,913,876,-1,876,877,914,-1,915,914,877,-1,877,878,915,-1,916,915,878,-1,878,879,916,-1,917,916,879,-1,879,880,917,-1,918,917,880,-1,880,881,918,-1,919,918,881,-1,881,882,919,-1,920,919,882,-1,882,883,920,-1,921,920,883,-1,883,884,921,-1,922,921,884,-1,884,885,922,-1,923,922,885,-1,885,886,923,-1,924,923,886,-1,886,887,924,-1,925,924,887,-1,887,888,925,-1,926,925,888,-1,888,889,926,-1,927,926,889,-1,889,890,927,-1,928,927,890,-1,890,891,928,-1,929,928,891,-1,891,892,929,-1,930,929,892,-1,892,893,930,-1,931,930,893,-1,893,894,931,-1,932,931,894,-1,894,895,932,-1,933,932,895,-1,895,896,933,-1,934,933,896,-1,896,897,934,-1,935,934,897,-1,897,898,935,-1,936,935,898,-1,898,899,936,-1,937,936,899,-1,899,900,937,-1,938,937,900,-1,939,940,941,-1,941,902,939,-1,942,939,902,-1,902,901,942,-1,943,942,901,-1,901,903,943,-1,944,943,903,-1,903,904,944,-1,945,944,904,-1,904,905,945,-1,946,945,905,-1,905,906,946,-1,947,946,906,-1,906,907,947,-1,948,947,907,-1,907,908,948,-1,949,948,908,-1,908,909,949,-1,950,949,909,-1,909,910,950,-1,951,950,910,-1,910,911,951,-1,952,951,911,-1,911,912,952,-1,953,952,912,-1,912,913,953,-1,954,953,913,-1,913,914,954,-1,955,954,914,-1,914,915,955,-1,956,955,915,-1,915,916,956,-1,957,956,916,-1,916,917,957,-1,958,957,917,-1,917,918,958,-1,959,958,918,-1,918,919,959,-1,960,959,919,-1,919,920,960,-1,961,960,920,-1,920,921,961,-1,962,961,921,-1,921,922,962,-1,963,962,922,-1,922,923,963,-1,964,963,923,-1,923,924,964,-1,965,964,924,-1,924,925,965,-1,966,965,925,-1,925,926,966,-1,967,966,926,-1,926,927,967,-1,968,967,927,-1,927,928,968,-1,969,968,928,-1,928,929,969,-1,970,969,929,-1,929,930,970,-1,971,970,930,-1,930,931,971,-1,972,971,931,-1,931,932,972,-1,973,972,932,-1,932,933,973,-1,974,973,933,-1,933,934,974,-1,975,974,934,-1,934,935,975,-1,976,975,935,-1,935,936,976,-1,977,976,936,-1,936,937,977,-1,978,977,937,-1,937,938,978,-1,940,939,979,-1,980,979,939,-1,939,942,980,-1,981,980,942,-1,942,943,981,-1,982,981,943,-1,943,944,982,-1,983,982,944,-1,944,945,983,-1,984,983,945,-1,945,946,984,-1,985,984,946,-1,946,947,985,-1,986,985,947,-1,947,948,986,-1,987,986,948,-1,948,949,987,-1,988,987,949,-1,949,950,988,-1,989,988,950,-1,950,951,989,-1,990,989,951,-1,951,952,990,-1,991,990,952,-1,952,953,991,-1,992,991,953,-1,953,954,992,-1,993,992,954,-1,954,955,993,-1,994,993,955,-1,955,956,994,-1,995,994,956,-1,956,957,995,-1,996,995,957,-1,957,958,996,-1,997,996,958,-1,958,959,997,-1,998,997,959,-1,959,960,998,-1,999,998,960,-1,960,961,999,-1,1000,999,961,-1,961,962,1000,-1,1001,1000,962,-1,962,963,1001,-1,1002,1001,963,-1,963,964,1002,-1,1003,1002,964,-1,964,965,1003,-1,1004,1003,965,-1,965,966,1004,-1,1005,1004,966,-1,966,967,1005,-1,1006,1005,967,-1,967,968,1006,-1,1007,1006,968,-1,968,969,1007,-1,1008,1007,969,-1,969,970,1008,-1,1009,1008,970,-1,970,971,1009,-1,1010,1009,971,-1,971,972,1010,-1,1011,1010,972,-1,972,973,1011,-1,1012,1011,973,-1,973,974,1012,-1,1013,1012,974,-1,974,975,1013,-1,1014,1013,975,-1,975,976,1014,-1,1015,1014,976,-1,976,977,1015,-1,1016,1015,977,-1,977,978,1016,-1,1017,1016,978,-1,1018,1019,979,-1,979,980,1018,-1,1020,1018,980,-1,980,981,1020,-1,1021,1020,981,-1,981,982,1021,-1,1022,1021,982,-1,982,983,1022,-1,1023,1022,983,-1,983,984,1023,-1,1024,1023,984,-1,984,985,1024,-1,1025,1024,985,-1,985,986,1025,-1,1026,1025,986,-1,986,987,1026,-1,1027,1026,987,-1,987,988,1027,-1,1028,1027,988,-1,988,989,1028,-1,1029,1028,989,-1,989,990,1029,-1,1030,1029,990,-1,990,991,1030,-1,1031,1030,991,-1,991,992,1031,-1,1032,1031,992,-1,992,993,1032,-1,1033,1032,993,-1,993,994,1033,-1,1034,1033,994,-1,994,995,1034,-1,1035,1034,995,-1,995,996,1035,-1,1036,1035,996,-1,996,997,1036,-1,1037,1036,997,-1,997,998,1037,-1,1038,1037,998,-1,998,999,1038,-1,1039,1038,999,-1,999,1000,1039,-1,1040,1039,1000,-1,1000,1001,1040,-1,1041,1040,1001,-1,1001,1002,1041,-1,1042,1041,1002,-1,1002,1003,1042,-1,1043,1042,1003,-1,1003,1004,1043,-1,1044,1043,1004,-1,1004,1005,1044,-1,1045,1044,1005,-1,1005,1006,1045,-1,1046,1045,1006,-1,1006,1007,1046,-1,1047,1046,1007,-1,1007,1008,1047,-1,1048,1047,1008,-1,1008,1009,1048,-1,1049,1048,1009,-1,1009,1010,1049,-1,1050,1049,1010,-1,1010,1011,1050,-1,1051,1050,1011,-1,1011,1012,1051,-1,1052,1051,1012,-1,1012,1013,1052,-1,1053,1052,1013,-1,1013,1014,1053,-1,1054,1053,1014,-1,1014,1015,1054,-1,1055,1054,1015,-1,1015,1016,1055,-1,1056,1055,1016,-1,1016,1017,1056,-1,1057,1056,1017,-1,1058,1059,1019,-1,1019,1018,1058,-1,1060,1058,1018,-1,1018,1020,1060,-1,1061,1060,1020,-1,1020,1021,1061,-1,1062,1061,1021,-1,1021,1022,1062,-1,1063,1062,1022,-1,1022,1023,1063,-1,1064,1063,1023,-1,1023,1024,1064,-1,1065,1064,1024,-1,1024,1025,1065,-1,1066,1065,1025,-1,1025,1026,1066,-1,1067,1066,1026,-1,1026,1027,1067,-1,1068,1067,1027,-1,1027,1028,1068,-1,1069,1068,1028,-1,1028,1029,1069,-1,1070,1069,1029,-1,1029,1030,1070,-1,1071,1070,1030,-1,1030,1031,1071,-1,1072,1071,1031,-1,1031,1032,1072,-1,1073,1072,1032,-1,1032,1033,1073,-1,1074,1073,1033,-1,1033,1034,1074,-1,1075,1074,1034,-1,1034,1035,1075,-1,1076,1075,1035,-1,1035,1036,1076,-1,1077,1076,1036,-1,1036,1037,1077,-1,1078,1077,1037,-1,1037,1038,1078,-1,1079,1078,1038,-1,1038,1039,1079,-1,1080,1079,1039,-1,1039,1040,1080,-1,1081,1080,1040,-1,1040,1041,1081,-1,1082,1081,1041,-1,1041,1042,1082,-1,1083,1082,1042,-1,1042,1043,1083,-1,1084,1083,1043,-1,1043,1044,1084,-1,1085,1084,1044,-1,1044,1045,1085,-1,1086,1085,1045,-1,1045,1046,1086,-1,1087,1086,1046,-1,1046,1047,1087,-1,1088,1087,1047,-1,1047,1048,1088,-1,1089,1088,1048,-1,1048,1049,1089,-1,1090,1089,1049,-1,1049,1050,1090,-1,1091,1090,1050,-1,1050,1051,1091,-1,1092,1091,1051,-1,1051,1052,1092,-1,1093,1092,1052,-1,1052,1053,1093,-1,1094,1093,1053,-1,1053,1054,1094,-1,1095,1094,1054,-1,1054,1055,1095,-1,1096,1095,1055,-1,1055,1056,1096,-1,1097,1096,1056,-1,1056,1057,1097,-1,1098,1097,1057,-1,1059,1058,1099,-1,1100,1099,1058,-1,1058,1060,1100,-1,1101,1100,1060,-1,1060,1061,1101,-1,1102,1101,1061,-1,1061,1062,1102,-1,1103,1102,1062,-1,1062,1063,1103,-1,1104,1103,1063,-1,1063,1064,1104,-1,1105,1104,1064,-1,1064,1065,1105,-1,1106,1105,1065,-1,1065,1066,1106,-1,1107,1106,1066,-1,1066,1067,1107,-1,1108,1107,1067,-1,1067,1068,1108,-1,1109,1108,1068,-1,1068,1069,1109,-1,1110,1109,1069,-1,1069,1070,1110,-1,1111,1110,1070,-1,1070,1071,1111,-1,1112,1111,1071,-1,1071,1072,1112,-1,1113,1112,1072,-1,1072,1073,1113,-1,1114,1113,1073,-1,1073,1074,1114,-1,1115,1114,1074,-1,1074,1075,1115,-1,1116,1115,1075,-1,1075,1076,1116,-1,1117,1116,1076,-1,1076,1077,1117,-1,1118,1117,1077,-1,1077,1078,1118,-1,1119,1118,1078,-1,1078,1079,1119,-1,1120,1119,1079,-1,1079,1080,1120,-1,1121,1120,1080,-1,1080,1081,1121,-1,1122,1121,1081,-1,1081,1082,1122,-1,1123,1122,1082,-1,1082,1083,1123,-1,1124,1123,1083,-1,1083,1084,1124,-1,1125,1124,1084,-1,1084,1085,1125,-1,1126,1125,1085,-1,1085,1086,1126,-1,1127,1126,1086,-1,1086,1087,1127,-1,1128,1127,1087,-1,1087,1088,1128,-1,1129,1128,1088,-1,1088,1089,1129,-1,1130,1129,1089,-1,1089,1090,1130,-1,1131,1130,1090,-1,1090,1091,1131,-1,1132,1131,1091,-1,1091,1092,1132,-1,1133,1132,1092,-1,1092,1093,1133,-1,1134,1133,1093,-1,1093,1094,1134,-1,1135,1134,1094,-1,1094,1095,1135,-1,1136,1135,1095,-1,1095,1096,1136,-1,1137,1136,1096,-1,1096,1097,1137,-1,1138,1137,1097,-1,1097,1098,1138,-1,1139,1138,1098,-1,1140,1141,1099,-1,1099,1100,1140,-1,1142,1140,1100,-1,1100,1101,1142,-1,1143,1142,1101,-1,1101,1102,1143,-1,1144,1143,1102,-1,1102,1103,1144,-1,1145,1144,1103,-1,1103,1104,1145,-1,1146,1145,1104,-1,1104,1105,1146,-1,1147,1146,1105,-1,1105,1106,1147,-1,1148,1147,1106,-1,1106,1107,1148,-1,1149,1148,1107,-1,1107,1108,1149,-1,1150,1149,1108,-1,1108,1109,1150,-1,1151,1150,1109,-1,1109,1110,1151,-1,1152,1151,1110,-1,1110,1111,1152,-1,1153,1152,1111,-1,1111,1112,1153,-1,1154,1153,1112,-1,1112,1113,1154,-1,1155,1154,1113,-1,1113,1114,1155,-1,1156,1155,1114,-1,1114,1115,1156,-1,1157,1156,1115,-1,1115,1116,1157,-1,1158,1157,1116,-1,1116,1117,1158,-1,1159,1158,1117,-1,1117,1118,1159,-1,1160,1159,1118,-1,1118,1119,1160,-1,1161,1160,1119,-1,1119,1120,1161,-1,1162,1161,1120,-1,1120,1121,1162,-1,1163,1162,1121,-1,1121,1122,1163,-1,1164,1163,1122,-1,1122,1123,1164,-1,1165,1164,1123,-1,1123,1124,1165,-1,1166,1165,1124,-1,1124,1125,1166,-1,1167,1166,1125,-1,1125,1126,1167,-1,1168,1167,1126,-1,1126,1127,1168,-1,1169,1168,1127,-1,1127,1128,1169,-1,1170,1169,1128,-1,1128,1129,1170,-1,1171,1170,1129,-1,1129,1130,1171,-1,1172,1171,1130,-1,1130,1131,1172,-1,1173,1172,1131,-1,1131,1132,1173,-1,1174,1173,1132,-1,1132,1133,1174,-1,1175,1174,1133,-1,1133,1134,1175,-1,1176,1175,1134,-1,1134,1135,1176,-1,1177,1176,1135,-1,1135,1136,1177,-1,1178,1177,1136,-1,1136,1137,1178,-1,1179,1178,1137,-1,1137,1138,1179,-1,1180,1179,1138,-1,1138,1139,1180,-1,1141,1140,1181,-1,1182,1181,1140,-1,1140,1142,1182,-1,1183,1182,1142,-1,1142,1143,1183,-1,1184,1183,1143,-1,1143,1144,1184,-1,1185,1184,1144,-1,1144,1145,1185,-1,1186,1185,1145,-1,1145,1146,1186,-1,1187,1186,1146,-1,1146,1147,1187,-1,1188,1187,1147,-1,1147,1148,1188,-1,1189,1188,1148,-1,1148,1149,1189,-1,1190,1189,1149,-1,1149,1150,1190,-1,1191,1190,1150,-1,1150,1151,1191,-1,1192,1191,1151,-1,1151,1152,1192,-1,1193,1192,1152,-1,1152,1153,1193,-1,1194,1193,1153,-1,1153,1154,1194,-1,1195,1194,1154,-1,1154,1155,1195,-1,1196,1195,1155,-1,1155,1156,1196,-1,1197,1196,1156,-1,1156,1157,1197,-1,1198,1197,1157,-1,1157,1158,1198,-1,1199,1198,1158,-1,1158,1159,1199,-1,1200,1199,1159,-1,1159,1160,1200,-1,1201,1200,1160,-1,1160,1161,1201,-1,1202,1201,1161,-1,1161,1162,1202,-1,1203,1202,1162,-1,1162,1163,1203,-1,1204,1203,1163,-1,1163,1164,1204,-1,1205,1204,1164,-1,1164,1165,1205,-1,1206,1205,1165,-1,1165,1166,1206,-1,1207,1206,1166,-1,1166,1167,1207,-1,1208,1207,1167,-1,1167,1168,1208,-1,1209,1208,1168,-1,1168,1169,1209,-1,1210,1209,1169,-1,1169,1170,1210,-1,1211,1210,1170,-1,1170,1171,1211,-1,1212,1211,1171,-1,1171,1172,1212,-1,1213,1212,1172,-1,1172,1173,1213,-1,1214,1213,1173,-1,1173,1174,1214,-1,1215,1214,1174,-1,1174,1175,1215,-1,1216,1215,1175,-1,1175,1176,1216,-1,1217,1216,1176,-1,1176,1177,1217,-1,1218,1217,1177,-1,1177,1178,1218,-1,1219,1218,1178,-1,1178,1179,1219,-1,1220,1221,1181,-1,1181,1182,1220,-1,1222,1220,1182,-1,1182,1183,1222,-1,1223,1222,1183,-1,1183,1184,1223,-1,1224,1223,1184,-1,1184,1185,1224,-1,1225,1224,1185,-1,1185,1186,1225,-1,1226,1225,1186,-1,1186,1187,1226,-1,1227,1226,1187,-1,1187,1188,1227,-1,1228,1227,1188,-1,1188,1189,1228,-1,1229,1228,1189,-1,1189,1190,1229,-1,1230,1229,1190,-1,1190,1191,1230,-1,1231,1230,1191,-1,1191,1192,1231,-1,1232,1231,1192,-1,1192,1193,1232,-1,1233,1232,1193,-1,1193,1194,1233,-1,1234,1233,1194,-1,1194,1195,1234,-1,1235,1234,1195,-1,1195,1196,1235,-1,1236,1235,1196,-1,1196,1197,1236,-1,1237,1236,1197,-1,1197,1198,1237,-1,1238,1237,1198,-1,1198,1199,1238,-1,1239,1238,1199,-1,1199,1200,1239,-1,1240,1239,1200,-1,1200,1201,1240,-1,1241,1240,1201,-1,1201,1202,1241,-1,1242,1241,1202,-1,1202,1203,1242,-1,1243,1242,1203,-1,1203,1204,1243,-1,1244,1243,1204,-1,1204,1205,1244,-1,1245,1244,1205,-1,1205,1206,1245,-1,1246,1245,1206,-1,1206,1207,1246,-1,1247,1246,1207,-1,1207,1208,1247,-1,1248,1247,1208,-1,1208,1209,1248,-1,1249,1248,1209,-1,1209,1210,1249,-1,1250,1249,1210,-1,1210,1211,1250,-1,1251,1250,1211,-1,1211,1212,1251,-1,1252,1251,1212,-1,1212,1213,1252,-1,1253,1252,1213,-1,1213,1214,1253,-1,1254,1253,1214,-1,1214,1215,1254,-1,1255,1254,1215,-1,1215,1216,1255,-1,1256,1255,1216,-1,1216,1217,1256,-1,1257,1256,1217,-1,1217,1218,1257,-1,1221,1220,1258,-1,1259,1258,1220,-1,1220,1222,1259,-1,1260,1259,1222,-1,1222,1223,1260,-1,1261,1260,1223,-1,1223,1224,1261,-1,1262,1261,1224,-1,1224,1225,1262,-1,1263,1262,1225,-1,1225,1226,1263,-1,1264,1263,1226,-1,1226,1227,1264,-1,1265,1264,1227,-1,1227,1228,1265,-1,1266,1265,1228,-1,1228,1229,1266,-1,1267,1266,1229,-1,1229,1230,1267,-1,1268,1267,1230,-1,1230,1231,1268,-1,1269,1268,1231,-1,1231,1232,1269,-1,1270,1269,1232,-1,1232,1233,1270,-1,1271,1270,1233,-1,1233,1234,1271,-1,1272,1271,1234,-1,1234,1235,1272,-1,1273,1272,1235,-1,1235,1236,1273,-1,1274,1273,1236,-1,1236,1237,1274,-1,1275,1274,1237,-1,1237,1238,1275,-1,1276,1275,1238,-1,1238,1239,1276,-1,1277,1276,1239,-1,1239,1240,1277,-1,1278,1277,1240,-1,1240,1241,1278,-1,1279,1278,1241,-1,1241,1242,1279,-1,1280,1279,1242,-1,1242,1243,1280,-1,1281,1280,1243,-1,1243,1244,1281,-1,1282,1281,1244,-1,1244,1245,1282,-1,1283,1282,1245,-1,1245,1246,1283,-1,1284,1283,1246,-1,1246,1247,1284,-1,1285,1284,1247,-1,1247,1248,1285,-1,1286,1285,1248,-1,1248,1249,1286,-1,1287,1286,1249,-1,1249,1250,1287,-1,1288,1287,1250,-1,1250,1251,1288,-1,1289,1288,1251,-1,1251,1252,1289,-1,1290,1289,1252,-1,1252,1253,1290,-1,1291,1290,1253,-1,1253,1254,1291,-1,1292,1291,1254,-1,1254,1255,1292,-1,1293,1292,1255,-1,1255,1256,1293,-1,1294,1293,1256,-1,1256,1257,1294,-1,1295,1294,1257,-1,1296,1297,1258,-1,1258,1259,1296,-1,1298,1296,1259,-1,1259,1260,1298,-1,1299,1298,1260,-1,1260,1261,1299,-1,1300,1299,1261,-1,1261,1262,1300,-1,1301,1300,1262,-1,1262,1263,1301,-1,1302,1301,1263,-1,1263,1264,1302,-1,1303,1302,1264,-1,1264,1265,1303,-1,1304,1303,1265,-1,1265,1266,1304,-1,1305,1304,1266,-1,1266,1267,1305,-1,1306,1305,1267,-1,1267,1268,1306,-1,1307,1306,1268,-1,1268,1269,1307,-1,1308,1307,1269,-1,1269,1270,1308,-1,1309,1308,1270,-1,1270,1271,1309,-1,1310,1309,1271,-1,1271,1272,1310,-1,1311,1310,1272,-1,1272,1273,1311,-1,1312,1311,1273,-1,1273,1274,1312,-1,1313,1312,1274,-1,1274,1275,1313,-1,1314,1313,1275,-1,1275,1276,1314,-1,1315,1314,1276,-1,1276,1277,1315,-1,1316,1315,1277,-1,1277,1278,1316,-1,1317,1316,1278,-1,1278,1279,1317,-1,1318,1317,1279,-1,1279,1280,1318,-1,1319,1318,1280,-1,1280,1281,1319,-1,1320,1319,1281,-1,1281,1282,1320,-1,1321,1320,1282,-1,1282,1283,1321,-1,1322,1321,1283,-1,1283,1284,1322,-1,1323,1322,1284,-1,1284,1285,1323,-1,1324,1323,1285,-1,1285,1286,1324,-1,1325,1324,1286,-1,1286,1287,1325,-1,1326,1325,1287,-1,1287,1288,1326,-1,1327,1326,1288,-1,1288,1289,1327,-1,1328,1327,1289,-1,1289,1290,1328,-1,1329,1328,1290,-1,1290,1291,1329,-1,1330,1329,1291,-1,1291,1292,1330,-1,1331,1330,1292,-1,1292,1293,1331,-1,1332,1331,1293,-1,1293,1294,1332,-1,1333,1332,1294,-1,1294,1295,1333,-1,1334,1333,1295,-1,1297,1296,1335,-1,1336,1335,1296,-1,1296,1298,1336,-1,1337,1336,1298,-1,1298,1299,1337,-1,1338,1337,1299,-1,1299,1300,1338,-1,1339,1338,1300,-1,1300,1301,1339,-1,1340,1339,1301,-1,1301,1302,1340,-1,1341,1340,1302,-1,1302,1303,1341,-1,1342,1341,1303,-1,1303,1304,1342,-1,1343,1342,1304,-1,1304,1305,1343,-1,1344,1343,1305,-1,1305,1306,1344,-1,1345,1344,1306,-1,1306,1307,1345,-1,1346,1345,1307,-1,1307,1308,1346,-1,1347,1346,1308,-1,1308,1309,1347,-1,1348,1347,1309,-1,1309,1310,1348,-1,1349,1348,1310,-1,1310,1311,1349,-1,1350,1349,1311,-1,1311,1312,1350,-1,1351,1350,1312,-1,1312,1313,1351,-1,1352,1351,1313,-1,1313,1314,1352,-1,1353,1352,1314,-1,1314,1315,1353,-1,1354,1353,1315,-1,1315,1316,1354,-1,1355,1354,1316,-1,1316,1317,1355,-1,1356,1355,1317,-1,1317,1318,1356,-1,1357,1356,1318,-1,1318,1319,1357,-1,1358,1357,1319,-1,1319,1320,1358,-1,1359,1358,1320,-1,1320,1321,1359,-1,1360,1359,1321,-1,1321,1322,1360,-1,1361,1360,1322,-1,1322,1323,1361,-1,1362,1361,1323,-1,1323,1324,1362,-1,1363,1362,1324,-1,1324,1325,1363,-1,1364,1363,1325,-1,1325,1326,1364,-1,1365,1364,1326,-1,1326,1327,1365,-1,1366,1365,1327,-1,1327,1328,1366,-1,1367,1366,1328,-1,1328,1329,1367,-1,1368,1367,1329,-1,1329,1330,1368,-1,1369,1368,1330,-1,1330,1331,1369,-1,1370,1369,1331,-1,1331,1332,1370,-1,1371,1370,1332,-1,1332,1333,1371,-1,1372,1371,1333,-1,1333,1334,1372,-1,1373,1374,1335,-1,1335,1336,1373,-1,1375,1373,1336,-1,1336,1337,1375,-1,1376,1375,1337,-1,1337,1338,1376,-1,1377,1376,1338,-1,1338,1339,1377,-1,1378,1377,1339,-1,1339,1340,1378,-1,1379,1378,1340,-1,1340,1341,1379,-1,1380,1379,1341,-1,1341,1342,1380,-1,1381,1380,1342,-1,1342,1343,1381,-1,1382,1381,1343,-1,1343,1344,1382,-1,1383,1382,1344,-1,1344,1345,1383,-1,1384,1383,1345,-1,1345,1346,1384,-1,1385,1384,1346,-1,1346,1347,1385,-1,1386,1385,1347,-1,1347,1348,1386,-1,1387,1386,1348,-1,1348,1349,1387,-1,1388,1387,1349,-1,1349,1350,1388,-1,1389,1388,1350,-1,1350,1351,1389,-1,1390,1389,1351,-1,1351,1352,1390,-1,1391,1390,1352,-1,1352,1353,1391,-1,1392,1391,1353,-1,1353,1354,1392,-1,1393,1392,1354,-1,1354,1355,1393,-1,1394,1393,1355,-1,1355,1356,1394,-1,1395,1394,1356,-1,1356,1357,1395,-1,1396,1395,1357,-1,1357,1358,1396,-1,1397,1396,1358,-1,1358,1359,1397,-1,1398,1397,1359,-1,1359,1360,1398,-1,1399,1398,1360,-1,1360,1361,1399,-1,1400,1399,1361,-1,1361,1362,1400,-1,1401,1400,1362,-1,1362,1363,1401,-1,1402,1401,1363,-1,1363,1364,1402,-1,1403,1402,1364,-1,1364,1365,1403,-1,1404,1403,1365,-1,1365,1366,1404,-1,1405,1404,1366,-1,1366,1367,1405,-1,1406,1405,1367,-1,1367,1368,1406,-1,1407,1406,1368,-1,1368,1369,1407,-1,1408,1407,1369,-1,1369,1370,1408,-1,1409,1408,1370,-1,1370,1371,1409,-1,1410,1409,1371,-1,1371,1372,1410,-1,1411,1410,1372,-1,1374,1373,1412,-1,1413,1412,1373,-1,1373,1375,1413,-1,1414,1413,1375,-1,1375,1376,1414,-1,1415,1414,1376,-1,1376,1377,1415,-1,1416,1415,1377,-1,1377,1378,1416,-1,1417,1416,1378,-1,1378,1379,1417,-1,1418,1417,1379,-1,1379,1380,1418,-1,1419,1418,1380,-1,1380,1381,1419,-1,1420,1419,1381,-1,1381,1382,1420,-1,1421,1420,1382,-1,1382,1383,1421,-1,1422,1421,1383,-1,1383,1384,1422,-1,1423,1422,1384,-1,1384,1385,1423,-1,1424,1423,1385,-1,1385,1386,1424,-1,1425,1424,1386,-1,1386,1387,1425,-1,1426,1425,1387,-1,1387,1388,1426,-1,1427,1426,1388,-1,1388,1389,1427,-1,1428,1427,1389,-1,1389,1390,1428,-1,1429,1428,1390,-1,1390,1391,1429,-1,1430,1429,1391,-1,1391,1392,1430,-1,1431,1430,1392,-1,1392,1393,1431,-1,1432,1431,1393,-1,1393,1394,1432,-1,1433,1432,1394,-1,1394,1395,1433,-1,1434,1433,1395,-1,1395,1396,1434,-1,1435,1434,1396,-1,1396,1397,1435,-1,1436,1435,1397,-1,1397,1398,1436,-1,1437,1436,1398,-1,1398,1399,1437,-1,1438,1437,1399,-1,1399,1400,1438,-1,1439,1438,1400,-1,1400,1401,1439,-1,1440,1439,1401,-1,1401,1402,1440,-1,1441,1440,1402,-1,1402,1403,1441,-1,1442,1441,1403,-1,1403,1404,1442,-1,1443,1442,1404,-1,1404,1405,1443,-1,1444,1443,1405,-1,1405,1406,1444,-1,1445,1444,1406,-1,1406,1407,1445,-1,1446,1445,1407,-1,1407,1408,1446,-1,1447,1446,1408,-1,1408,1409,1447,-1,1448,1447,1409,-1,1409,1410,1448,-1,1449,1448,1410,-1,1410,1411,1449,-1,1450,1451,1412,-1,1412,1413,1450,-1,1452,1450,1413,-1,1413,1414,1452,-1,1453,1452,1414,-1,1414,1415,1453,-1,1454,1453,1415,-1,1415,1416,1454,-1,1455,1454,1416,-1,1416,1417,1455,-1,1456,1455,1417,-1,1417,1418,1456,-1,1457,1456,1418,-1,1418,1419,1457,-1,1458,1457,1419,-1,1419,1420,1458,-1,1459,1458,1420,-1,1420,1421,1459,-1,1460,1459,1421,-1,1421,1422,1460,-1,1461,1460,1422,-1,1422,1423,1461,-1,1462,1461,1423,-1,1423,1424,1462,-1,1463,1462,1424,-1,1424,1425,1463,-1,1464,1463,1425,-1,1425,1426,1464,-1,1465,1464,1426,-1,1426,1427,1465,-1,1466,1465,1427,-1,1427,1428,1466,-1,1467,1466,1428,-1,1428,1429,1467,-1,1468,1467,1429,-1,1429,1430,1468,-1,1469,1468,1430,-1,1430,1431,1469,-1,1470,1469,1431,-1,1431,1432,1470,-1,1471,1470,1432,-1,1432,1433,1471,-1,1472,1471,1433,-1,1433,1434,1472,-1,1473,1472,1434,-1,1434,1435,1473,-1,1474,1473,1435,-1,1435,1436,1474,-1,1475,1474,1436,-1,1436,1437,1475,-1,1476,1475,1437,-1,1437,1438,1476,-1,1477,1476,1438,-1,1438,1439,1477,-1,1478,1477,1439,-1,1439,1440,1478,-1,1479,1478,1440,-1,1440,1441,1479,-1,1480,1479,1441,-1,1441,1442,1480,-1,1481,1480,1442,-1,1442,1443,1481,-1,1482,1481,1443,-1,1443,1444,1482,-1,1483,1482,1444,-1,1444,1445,1483,-1,1484,1483,1445,-1,1445,1446,1484,-1,1485,1484,1446,-1,1446,1447,1485,-1,1486,1485,1447,-1,1447,1448,1486,-1,1487,1486,1448,-1,1448,1449,1487,-1,1488,1487,1449,-1,1451,1450,1489,-1,1490,1489,1450,-1,1450,1452,1490,-1,1491,1490,1452,-1,1452,1453,1491,-1,1492,1491,1453,-1,1453,1454,1492,-1,1493,1492,1454,-1,1454,1455,1493,-1,1494,1493,1455,-1,1455,1456,1494,-1,1495,1494,1456,-1,1456,1457,1495,-1,1496,1495,1457,-1,1457,1458,1496,-1,1497,1496,1458,-1,1458,1459,1497,-1,1498,1497,1459,-1,1459,1460,1498,-1,1499,1498,1460,-1,1460,1461,1499,-1,1500,1499,1461,-1,1461,1462,1500,-1,1501,1500,1462,-1,1462,1463,1501,-1,1502,1501,1463,-1,1463,1464,1502,-1,1503,1502,1464,-1,1464,1465,1503,-1,1504,1503,1465,-1,1465,1466,1504,-1,1505,1504,1466,-1,1466,1467,1505,-1,1506,1505,1467,-1,1467,1468,1506,-1,1507,1506,1468,-1,1468,1469,1507,-1,1508,1507,1469,-1,1469,1470,1508,-1,1509,1508,1470,-1,1470,1471,1509,-1,1510,1509,1471,-1,1471,1472,1510,-1,1511,1510,1472,-1,1472,1473,1511,-1,1512,1511,1473,-1,1473,1474,1512,-1,1513,1512,1474,-1,1474,1475,1513,-1,1514,1513,1475,-1,1475,1476,1514,-1,1515,1514,1476,-1,1476,1477,1515,-1,1516,1515,1477,-1,1477,1478,1516,-1,1517,1516,1478,-1,1478,1479,1517,-1,1518,1517,1479,-1,1479,1480,1518,-1,1519,1518,1480,-1,1480,1481,1519,-1,1520,1519,1481,-1,1481,1482,1520,-1,1521,1520,1482,-1,1482,1483,1521,-1,1522,1521,1483,-1,1483,1484,1522,-1,1523,1522,1484,-1,1484,1485,1523,-1,1524,1523,1485,-1,1485,1486,1524,-1,1525,1524,1486,-1,1486,1487,1525,-1,1526,1525,1487,-1,1487,1488,1526,-1,1489,1490,1527,-1,1528,1527,1490,-1,1490,1491,1528,-1,1529,1528,1491,-1,1491,1492,1529,-1,1530,1529,1492,-1,1492,1493,1530,-1,1531,1530,1493,-1,1493,1494,1531,-1,1532,1531,1494,-1,1494,1495,1532,-1,1533,1532,1495,-1,1495,1496,1533,-1,1534,1533,1496,-1,1496,1497,1534,-1,1535,1534,1497,-1,1497,1498,1535,-1,1536,1535,1498,-1,1498,1499,1536,-1,1537,1536,1499,-1,1499,1500,1537,-1,1538,1537,1500,-1,1500,1501,1538,-1,1539,1538,1501,-1,1501,1502,1539,-1,1540,1539,1502,-1,1502,1503,1540,-1,1541,1540,1503,-1,1503,1504,1541,-1,1542,1541,1504,-1,1504,1505,1542,-1,1543,1542,1505,-1,1505,1506,1543,-1,1544,1543,1506,-1,1506,1507,1544,-1,1545,1544,1507,-1,1507,1508,1545,-1,1546,1545,1508,-1,1508,1509,1546,-1,1547,1546,1509,-1,1509,1510,1547,-1,1548,1547,1510,-1,1510,1511,1548,-1,1549,1548,1511,-1,1511,1512,1549,-1,1550,1549,1512,-1,1512,1513,1550,-1,1551,1550,1513,-1,1513,1514,1551,-1,1552,1551,1514,-1,1514,1515,1552,-1,1553,1552,1515,-1,1515,1516,1553,-1,1554,1553,1516,-1,1516,1517,1554,-1,1555,1554,1517,-1,1517,1518,1555,-1,1556,1555,1518,-1,1518,1519,1556,-1,1557,1556,1519,-1,1519,1520,1557,-1,1558,1557,1520,-1,1520,1521,1558,-1,1559,1558,1521,-1,1521,1522,1559,-1,1560,1559,1522,-1,1522,1523,1560,-1,1561,1560,1523,-1,1523,1524,1561,-1,1562,1561,1524,-1,1524,1525,1562,-1,1563,1562,1525,-1,1525,1526,1563,-1,1564,1563,1526,-1,1528,1529,1565,-1,1566,1565,1529,-1,1529,1530,1566,-1,1567,1566,1530,-1,1530,1531,1567,-1,1568,1567,1531,-1,1531,1532,1568,-1,1569,1568,1532,-1,1532,1533,1569,-1,1570,1569,1533,-1,1533,1534,1570,-1,1571,1570,1534,-1,1534,1535,1571,-1,1572,1571,1535,-1,1535,1536,1572,-1,1573,1572,1536,-1,1536,1537,1573,-1,1574,1573,1537,-1,1537,1538,1574,-1,1575,1574,1538,-1,1538,1539,1575,-1,1576,1575,1539,-1,1539,1540,1576,-1,1577,1576,1540,-1,1540,1541,1577,-1,1578,1577,1541,-1,1541,1542,1578,-1,1579,1578,1542,-1,1542,1543,1579,-1,1580,1579,1543,-1,1543,1544,1580,-1,1581,1580,1544,-1,1544,1545,1581,-1,1582,1581,1545,-1,1545,1546,1582,-1,1583,1582,1546,-1,1546,1547,1583,-1,1584,1583,1547,-1,1547,1548,1584,-1,1585,1584,1548,-1,1548,1549,1585,-1,1586,1585,1549,-1,1549,1550,1586,-1,1587,1586,1550,-1,1550,1551,1587,-1,1588,1587,1551,-1,1551,1552,1588,-1,1589,1588,1552,-1,1552,1553,1589,-1,1590,1589,1553,-1,1553,1554,1590,-1,1591,1590,1554,-1,1554,1555,1591,-1,1592,1591,1555,-1,1555,1556,1592,-1,1593,1592,1556,-1,1556,1557,1593,-1,1594,1593,1557,-1,1557,1558,1594,-1,1595,1594,1558,-1,1558,1559,1595,-1,1596,1595,1559,-1,1559,1560,1596,-1,1597,1596,1560,-1,1560,1561,1597,-1,1598,1597,1561,-1,1561,1562,1598,-1,1599,1598,1562,-1,1562,1563,1599,-1,1600,1599,1563,-1,1563,1564,1600,-1,1601,1600,1564,-1,1564,1602,1601,-1,1603,1601,1602,-1,1602,1604,1603,-1,1605,1603,1604,-1,1606,1607,1565,-1,1565,1566,1606,-1,1608,1606,1566,-1,1566,1567,1608,-1,1609,1608,1567,-1,1567,1568,1609,-1,1610,1609,1568,-1,1568,1569,1610,-1,1611,1610,1569,-1,1569,1570,1611,-1,1612,1611,1570,-1,1570,1571,1612,-1,1613,1612,1571,-1,1571,1572,1613,-1,1614,1613,1572,-1,1572,1573,1614,-1,1615,1614,1573,-1,1573,1574,1615,-1,1616,1615,1574,-1,1574,1575,1616,-1,1617,1616,1575,-1,1575,1576,1617,-1,1618,1617,1576,-1,1576,1577,1618,-1,1619,1618,1577,-1,1577,1578,1619,-1,1620,1619,1578,-1,1578,1579,1620,-1,1621,1620,1579,-1,1579,1580,1621,-1,1622,1621,1580,-1,1580,1581,1622,-1,1623,1622,1581,-1,1581,1582,1623,-1,1624,1623,1582,-1,1582,1583,1624,-1,1625,1624,1583,-1,1583,1584,1625,-1,1626,1625,1584,-1,1584,1585,1626,-1,1627,1626,1585,-1,1585,1586,1627,-1,1628,1627,1586,-1,1586,1587,1628,-1,1629,1628,1587,-1,1587,1588,1629,-1,1630,1629,1588,-1,1588,1589,1630,-1,1631,1630,1589,-1,1589,1590,1631,-1,1632,1631,1590,-1,1590,1591,1632,-1,1633,1632,1591,-1,1591,1592,1633,-1,1634,1633,1592,-1,1592,1593,1634,-1,1635,1634,1593,-1,1593,1594,1635,-1,1636,1635,1594,-1,1594,1595,1636,-1,1637,1636,1595,-1,1595,1596,1637,-1,1638,1637,1596,-1,1596,1597,1638,-1,1639,1638,1597,-1,1597,1598,1639,-1,1640,1639,1598,-1,1598,1599,1640,-1,1641,1640,1599,-1,1599,1600,1641,-1,1642,1641,1600,-1,1600,1601,1642,-1,1643,1642,1601,-1,1601,1603,1643,-1,1644,1643,1603,-1,1603,1605,1644,-1,1645,1644,1605,-1,1646,1647,1607,-1,1607,1606,1646,-1,1648,1646,1606,-1,1606,1608,1648,-1,1649,1648,1608,-1,1608,1609,1649,-1,1650,1649,1609,-1,1609,1610,1650,-1,1651,1650,1610,-1,1610,1611,1651,-1,1652,1651,1611,-1,1611,1612,1652,-1,1653,1652,1612,-1,1612,1613,1653,-1,1654,1653,1613,-1,1613,1614,1654,-1,1655,1654,1614,-1,1614,1615,1655,-1,1656,1655,1615,-1,1615,1616,1656,-1,1657,1656,1616,-1,1616,1617,1657,-1,1658,1657,1617,-1,1617,1618,1658,-1,1659,1658,1618,-1,1618,1619,1659,-1,1660,1659,1619,-1,1619,1620,1660,-1,1661,1660,1620,-1,1620,1621,1661,-1,1662,1661,1621,-1,1621,1622,1662,-1,1663,1662,1622,-1,1622,1623,1663,-1,1664,1663,1623,-1,1623,1624,1664,-1,1665,1664,1624,-1,1624,1625,1665,-1,1666,1665,1625,-1,1625,1626,1666,-1,1667,1666,1626,-1,1626,1627,1667,-1,1668,1667,1627,-1,1627,1628,1668,-1,1669,1668,1628,-1,1628,1629,1669,-1,1670,1669,1629,-1,1629,1630,1670,-1,1671,1670,1630,-1,1630,1631,1671,-1,1672,1671,1631,-1,1631,1632,1672,-1,1673,1672,1632,-1,1632,1633,1673,-1,1674,1673,1633,-1,1633,1634,1674,-1,1675,1674,1634,-1,1634,1635,1675,-1,1676,1675,1635,-1,1635,1636,1676,-1,1677,1676,1636,-1,1636,1637,1677,-1,1678,1677,1637,-1,1637,1638,1678,-1,1679,1678,1638,-1,1638,1639,1679,-1,1680,1679,1639,-1,1639,1640,1680,-1,1681,1680,1640,-1,1640,1641,1681,-1,1682,1681,1641,-1,1641,1642,1682,-1,1683,1682,1642,-1,1642,1643,1683,-1,1684,1683,1643,-1,1643,1644,1684,-1,1685,1684,1644,-1,1644,1645,1685,-1,1686,1687,1647,-1,1647,1646,1686,-1,1688,1686,1646,-1,1646,1648,1688,-1,1689,1688,1648,-1,1648,1649,1689,-1,1690,1689,1649,-1,1649,1650,1690,-1,1691,1690,1650,-1,1650,1651,1691,-1,1692,1691,1651,-1,1651,1652,1692,-1,1693,1692,1652,-1,1652,1653,1693,-1,1694,1693,1653,-1,1653,1654,1694,-1,1695,1694,1654,-1,1654,1655,1695,-1,1696,1695,1655,-1,1655,1656,1696,-1,1697,1696,1656,-1,1656,1657,1697,-1,1698,1697,1657,-1,1657,1658,1698,-1,1699,1698,1658,-1,1658,1659,1699,-1,1700,1699,1659,-1,1659,1660,1700,-1,1701,1700,1660,-1,1660,1661,1701,-1,1702,1701,1661,-1,1661,1662,1702,-1,1703,1702,1662,-1,1662,1663,1703,-1,1704,1703,1663,-1,1663,1664,1704,-1,1705,1704,1664,-1,1664,1665,1705,-1,1706,1705,1665,-1,1665,1666,1706,-1,1707,1706,1666,-1,1666,1667,1707,-1,1708,1707,1667,-1,1667,1668,1708,-1,1709,1708,1668,-1,1668,1669,1709,-1,1710,1709,1669,-1,1669,1670,1710,-1,1711,1710,1670,-1,1670,1671,1711,-1,1712,1711,1671,-1,1671,1672,1712,-1,1713,1712,1672,-1,1672,1673,1713,-1,1714,1713,1673,-1,1673,1674,1714,-1,1715,1714,1674,-1,1674,1675,1715,-1,1716,1715,1675,-1,1675,1676,1716,-1,1717,1716,1676,-1,1676,1677,1717,-1,1718,1717,1677,-1,1677,1678,1718,-1,1719,1718,1678,-1,1678,1679,1719,-1,1720,1719,1679,-1,1679,1680,1720,-1,1721,1720,1680,-1,1680,1681,1721,-1,1722,1721,1681,-1,1681,1682,1722,-1,1723,1722,1682,-1,1682,1683,1723,-1,1724,1723,1683,-1,1683,1684,1724,-1,1687,1686,1725,-1,1726,1725,1686,-1,1686,1688,1726,-1,1727,1726,1688,-1,1688,1689,1727,-1,1728,1727,1689,-1,1689,1690,1728,-1,1729,1728,1690,-1,1690,1691,1729,-1,1730,1729,1691,-1,1691,1692,1730,-1,1731,1730,1692,-1,1692,1693,1731,-1,1732,1731,1693,-1,1693,1694,1732,-1,1733,1732,1694,-1,1694,1695,1733,-1,1734,1733,1695,-1,1695,1696,1734,-1,1735,1734,1696,-1,1696,1697,1735,-1,1736,1735,1697,-1,1697,1698,1736,-1,1737,1736,1698,-1,1698,1699,1737,-1,1738,1737,1699,-1,1699,1700,1738,-1,1739,1738,1700,-1,1700,1701,1739,-1,1740,1739,1701,-1,1701,1702,1740,-1,1741,1740,1702,-1,1702,1703,1741,-1,1742,1741,1703,-1,1703,1704,1742,-1,1743,1742,1704,-1,1704,1705,1743,-1,1744,1743,1705,-1,1705,1706,1744,-1,1745,1744,1706,-1,1706,1707,1745,-1,1746,1745,1707,-1,1707,1708,1746,-1,1747,1746,1708,-1,1708,1709,1747,-1,1748,1747,1709,-1,1709,1710,1748,-1,1749,1748,1710,-1,1710,1711,1749,-1,1750,1749,1711,-1,1711,1712,1750,-1,1751,1750,1712,-1,1712,1713,1751,-1,1752,1751,1713,-1,1713,1714,1752,-1,1753,1752,1714,-1,1714,1715,1753,-1,1754,1753,1715,-1,1715,1716,1754,-1,1755,1754,1716,-1,1716,1717,1755,-1,1756,1755,1717,-1,1717,1718,1756,-1,1757,1756,1718,-1,1718,1719,1757,-1,1758,1757,1719,-1,1719,1720,1758,-1,1759,1758,1720,-1,1720,1721,1759,-1,1760,1759,1721,-1,1721,1722,1760,-1,1761,1760,1722,-1,1722,1723,1761,-1,1762,1761,1723,-1,1723,1724,1762,-1,1763,1762,1724,-1,1725,1726,1764,-1,1765,1764,1726,-1,1726,1727,1765,-1,1766,1765,1727,-1,1727,1728,1766,-1,1767,1766,1728,-1,1728,1729,1767,-1,1768,1767,1729,-1,1729,1730,1768,-1,1769,1768,1730,-1,1730,1731,1769,-1,1770,1769,1731,-1,1731,1732,1770,-1,1771,1770,1732,-1,1732,1733,1771,-1,1772,1771,1733,-1,1733,1734,1772,-1,1773,1772,1734,-1,1734,1735,1773,-1,1774,1773,1735,-1,1735,1736,1774,-1,1775,1774,1736,-1,1736,1737,1775,-1,1776,1775,1737,-1,1737,1738,1776,-1,1777,1776,1738,-1,1738,1739,1777,-1,1778,1777,1739,-1,1739,1740,1778,-1,1779,1778,1740,-1,1740,1741,1779,-1,1780,1779,1741,-1,1741,1742,1780,-1,1781,1780,1742,-1,1742,1743,1781,-1,1782,1781,1743,-1,1743,1744,1782,-1,1783,1782,1744,-1,1744,1745,1783,-1,1784,1783,1745,-1,1745,1746,1784,-1,1785,1784,1746,-1,1746,1747,1785,-1,1786,1785,1747,-1,1747,1748,1786,-1,1787,1786,1748,-1,1748,1749,1787,-1,1788,1787,1749,-1,1749,1750,1788,-1,1789,1788,1750,-1,1750,1751,1789,-1,1790,1789,1751,-1,1751,1752,1790,-1,1791,1790,1752,-1,1752,1753,1791,-1,1792,1791,1753,-1,1753,1754,1792,-1,1793,1792,1754,-1,1754,1755,1793,-1,1794,1793,1755,-1,1755,1756,1794,-1,1795,1794,1756,-1,1756,1757,1795,-1,1796,1795,1757,-1,1757,1758,1796,-1,1797,1796,1758,-1,1758,1759,1797,-1,1798,1797,1759,-1,1759,1760,1798,-1,1799,1798,1760,-1,1760,1761,1799,-1,1800,1799,1761,-1,1761,1762,1800,-1,1801,1800,1762,-1,1762,1763,1801,-1,1802,1801,1763,-1,1803,1804,1764,-1,1764,1765,1803,-1,1805,1803,1765,-1,1765,1766,1805,-1,1806,1805,1766,-1,1766,1767,1806,-1,1807,1806,1767,-1,1767,1768,1807,-1,1808,1807,1768,-1,1768,1769,1808,-1,1809,1808,1769,-1,1769,1770,1809,-1,1810,1809,1770,-1,1770,1771,1810,-1,1811,1810,1771,-1,1771,1772,1811,-1,1812,1811,1772,-1,1772,1773,1812,-1,1813,1812,1773,-1,1773,1774,1813,-1,1814,1813,1774,-1,1774,1775,1814,-1,1815,1814,1775,-1,1775,1776,1815,-1,1816,1815,1776,-1,1776,1777,1816,-1,1817,1816,1777,-1,1777,1778,1817,-1,1818,1817,1778,-1,1778,1779,1818,-1,1819,1818,1779,-1,1779,1780,1819,-1,1820,1819,1780,-1,1780,1781,1820,-1,1821,1820,1781,-1,1781,1782,1821,-1,1822,1821,1782,-1,1782,1783,1822,-1,1823,1822,1783,-1,1783,1784,1823,-1,1824,1823,1784,-1,1784,1785,1824,-1,1825,1824,1785,-1,1785,1786,1825,-1,1826,1825,1786,-1,1786,1787,1826,-1,1827,1826,1787,-1,1787,1788,1827,-1,1828,1827,1788,-1,1788,1789,1828,-1,1829,1828,1789,-1,1789,1790,1829,-1,1830,1829,1790,-1,1790,1791,1830,-1,1831,1830,1791,-1,1791,1792,1831,-1,1832,1831,1792,-1,1792,1793,1832,-1,1833,1832,1793,-1,1793,1794,1833,-1,1834,1833,1794,-1,1794,1795,1834,-1,1835,1834,1795,-1,1795,1796,1835,-1,1836,1835,1796,-1,1796,1797,1836,-1,1837,1836,1797,-1,1797,1798,1837,-1,1838,1837,1798,-1,1798,1799,1838,-1,1839,1838,1799,-1,1799,1800,1839,-1,1840,1839,1800,-1,1800,1801,1840,-1,1841,1840,1801,-1,1801,1802,1841,-1,1842,1843,1804,-1,1804,1803,1842,-1,1844,1842,1803,-1,1803,1805,1844,-1,1845,1844,1805,-1,1805,1806,1845,-1,1846,1845,1806,-1,1806,1807,1846,-1,1847,1846,1807,-1,1807,1808,1847,-1,1848,1847,1808,-1,1808,1809,1848,-1,1849,1848,1809,-1,1809,1810,1849,-1,1850,1849,1810,-1,1810,1811,1850,-1,1851,1850,1811,-1,1811,1812,1851,-1,1852,1851,1812,-1,1812,1813,1852,-1,1853,1852,1813,-1,1813,1814,1853,-1,1854,1853,1814,-1,1814,1815,1854,-1,1855,1854,1815,-1,1815,1816,1855,-1,1856,1855,1816,-1,1816,1817,1856,-1,1857,1856,1817,-1,1817,1818,1857,-1,1858,1857,1818,-1,1818,1819,1858,-1,1859,1858,1819,-1,1819,1820,1859,-1,1860,1859,1820,-1,1820,1821,1860,-1,1861,1860,1821,-1,1821,1822,1861,-1,1862,1861,1822,-1,1822,1823,1862,-1,1863,1862,1823,-1,1823,1824,1863,-1,1864,1863,1824,-1,1824,1825,1864,-1,1865,1864,1825,-1,1825,1826,1865,-1,1866,1865,1826,-1,1826,1827,1866,-1,1867,1866,1827,-1,1827,1828,1867,-1,1868,1867,1828,-1,1828,1829,1868,-1,1869,1868,1829,-1,1829,1830,1869,-1,1870,1869,1830,-1,1830,1831,1870,-1,1871,1870,1831,-1,1831,1832,1871,-1,1872,1871,1832,-1,1832,1833,1872,-1,1873,1872,1833,-1,1833,1834,1873,-1,1874,1873,1834,-1,1834,1835,1874,-1,1875,1874,1835,-1,1835,1836,1875,-1,1876,1875,1836,-1,1836,1837,1876,-1,1877,1876,1837,-1,1837,1838,1877,-1,1878,1877,1838,-1,1838,1839,1878,-1,1879,1878,1839,-1,1839,1840,1879,-1,1880,1879,1840,-1,1840,1841,1880,-1,1881,1880,1841,-1,1843,1842,1882,-1,1883,1882,1842,-1,1842,1844,1883,-1,1884,1883,1844,-1,1844,1845,1884,-1,1885,1884,1845,-1,1845,1846,1885,-1,1886,1885,1846,-1,1846,1847,1886,-1,1887,1886,1847,-1,1847,1848,1887,-1,1888,1887,1848,-1,1848,1849,1888,-1,1889,1888,1849,-1,1849,1850,1889,-1,1890,1889,1850,-1,1850,1851,1890,-1,1891,1890,1851,-1,1851,1852,1891,-1,1892,1891,1852,-1,1852,1853,1892,-1,1893,1892,1853,-1,1853,1854,1893,-1,1894,1893,1854,-1,1854,1855,1894,-1,1895,1894,1855,-1,1855,1856,1895,-1,1896,1895,1856,-1,1856,1857,1896,-1,1897,1896,1857,-1,1857,1858,1897,-1,1898,1897,1858,-1,1858,1859,1898,-1,1899,1898,1859,-1,1859,1860,1899,-1,1900,1899,1860,-1,1860,1861,1900,-1,1901,1900,1861,-1,1861,1862,1901,-1,1902,1901,1862,-1,1862,1863,1902,-1,1903,1902,1863,-1,1863,1864,1903,-1,1904,1903,1864,-1,1864,1865,1904,-1,1905,1904,1865,-1,1865,1866,1905,-1,1906,1905,1866,-1,1866,1867,1906,-1,1907,1906,1867,-1,1867,1868,1907,-1,1908,1907,1868,-1,1868,1869,1908,-1,1909,1908,1869,-1,1869,1870,1909,-1,1910,1909,1870,-1,1870,1871,1910,-1,1911,1910,1871,-1,1871,1872,1911,-1,1912,1911,1872,-1,1872,1873,1912,-1,1913,1912,1873,-1,1873,1874,1913,-1,1914,1913,1874,-1,1874,1875,1914,-1,1915,1914,1875,-1,1875,1876,1915,-1,1916,1915,1876,-1,1876,1877,1916,-1,1917,1916,1877,-1,1877,1878,1917,-1,1918,1917,1878,-1,1878,1879,1918,-1,1919,1918,1879,-1,1879,1880,1919,-1,1920,1919,1880,-1,1880,1881,1920,-1,1921,1920,1881,-1,1922,1923,1882,-1,1882,1883,1922,-1,1924,1922,1883,-1,1883,1884,1924,-1,1925,1924,1884,-1,1884,1885,1925,-1,1926,1925,1885,-1,1885,1886,1926,-1,1927,1926,1886,-1,1886,1887,1927,-1,1928,1927,1887,-1,1887,1888,1928,-1,1929,1928,1888,-1,1888,1889,1929,-1,1930,1929,1889,-1,1889,1890,1930,-1,1931,1930,1890,-1,1890,1891,1931,-1,1932,1931,1891,-1,1891,1892,1932,-1,1933,1932,1892,-1,1892,1893,1933,-1,1934,1933,1893,-1,1893,1894,1934,-1,1935,1934,1894,-1,1894,1895,1935,-1,1936,1935,1895,-1,1895,1896,1936,-1,1937,1936,1896,-1,1896,1897,1937,-1,1938,1937,1897,-1,1897,1898,1938,-1,1939,1938,1898,-1,1898,1899,1939,-1,1940,1939,1899,-1,1899,1900,1940,-1,1941,1940,1900,-1,1900,1901,1941,-1,1942,1941,1901,-1,1901,1902,1942,-1,1943,1942,1902,-1,1902,1903,1943,-1,1944,1943,1903,-1,1903,1904,1944,-1,1945,1944,1904,-1,1904,1905,1945,-1,1946,1945,1905,-1,1905,1906,1946,-1,1947,1946,1906,-1,1906,1907,1947,-1,1948,1947,1907,-1,1907,1908,1948,-1,1949,1948,1908,-1,1908,1909,1949,-1,1950,1949,1909,-1,1909,1910,1950,-1,1951,1950,1910,-1,1910,1911,1951,-1,1952,1951,1911,-1,1911,1912,1952,-1,1953,1952,1912,-1,1912,1913,1953,-1,1954,1953,1913,-1,1913,1914,1954,-1,1955,1954,1914,-1,1914,1915,1955,-1,1956,1955,1915,-1,1915,1916,1956,-1,1957,1956,1916,-1,1916,1917,1957,-1,1958,1957,1917,-1,1917,1918,1958,-1,1959,1958,1918,-1,1918,1919,1959,-1,1960,1959,1919,-1,1919,1920,1960,-1,1961,1960,1920,-1,1920,1921,1961,-1,1923,1922,1962,-1,1963,1962,1922,-1,1922,1924,1963,-1,1964,1963,1924,-1,1924,1925,1964,-1,1965,1964,1925,-1,1925,1926,1965,-1,1966,1965,1926,-1,1926,1927,1966,-1,1967,1966,1927,-1,1927,1928,1967,-1,1968,1967,1928,-1,1928,1929,1968,-1,1969,1968,1929,-1,1929,1930,1969,-1,1970,1969,1930,-1,1930,1931,1970,-1,1971,1970,1931,-1,1931,1932,1971,-1,1972,1971,1932,-1,1932,1933,1972,-1,1973,1972,1933,-1,1933,1934,1973,-1,1974,1973,1934,-1,1934,1935,1974,-1,1975,1974,1935,-1,1935,1936,1975,-1,1976,1975,1936,-1,1936,1937,1976,-1,1977,1976,1937,-1,1937,1938,1977,-1,1978,1977,1938,-1,1938,1939,1978,-1,1979,1978,1939,-1,1939,1940,1979,-1,1980,1979,1940,-1,1940,1941,1980,-1,1981,1980,1941,-1,1941,1942,1981,-1,1982,1981,1942,-1,1942,1943,1982,-1,1983,1982,1943,-1,1943,1944,1983,-1,1984,1983,1944,-1,1944,1945,1984,-1,1985,1984,1945,-1,1945,1946,1985,-1,1986,1985,1946,-1,1946,1947,1986,-1,1987,1986,1947,-1,1947,1948,1987,-1,1988,1987,1948,-1,1948,1949,1988,-1,1989,1988,1949,-1,1949,1950,1989,-1,1990,1989,1950,-1,1950,1951,1990,-1,1991,1990,1951,-1,1951,1952,1991,-1,1992,1991,1952,-1,1952,1953,1992,-1,1993,1992,1953,-1,1953,1954,1993,-1,1994,1993,1954,-1,1954,1955,1994,-1,1995,1994,1955,-1,1955,1956,1995,-1,1996,1995,1956,-1,1956,1957,1996,-1,1997,1996,1957,-1,1957,1958,1997,-1,1998,1997,1958,-1,1958,1959,1998,-1,1962,1963,1999,-1,2000,1999,1963,-1,1963,1964,2000,-1,2001,2000,1964,-1,1964,1965,2001,-1,2002,2001,1965,-1,1965,1966,2002,-1,2003,2002,1966,-1,1966,1967,2003,-1,2004,2003,1967,-1,1967,1968,2004,-1,2005,2004,1968,-1,1968,1969,2005,-1,2006,2005,1969,-1,1969,1970,2006,-1,2007,2006,1970,-1,1970,1971,2007,-1,2008,2007,1971,-1,1971,1972,2008,-1,2009,2008,1972,-1,1972,1973,2009,-1,2010,2009,1973,-1,1973,1974,2010,-1,2011,2010,1974,-1,1974,1975,2011,-1,2012,2011,1975,-1,1975,1976,2012,-1,2013,2012,1976,-1,1976,1977,2013,-1,2014,2013,1977,-1,1977,1978,2014,-1,2015,2014,1978,-1,1978,1979,2015,-1,2016,2015,1979,-1,1979,1980,2016,-1,2017,2016,1980,-1,1980,1981,2017,-1,2018,2017,1981,-1,1981,1982,2018,-1,2019,2018,1982,-1,1982,1983,2019,-1,2020,2019,1983,-1,1983,1984,2020,-1,2021,2020,1984,-1,1984,1985,2021,-1,2022,2021,1985,-1,1985,1986,2022,-1,2023,2022,1986,-1,1986,1987,2023,-1,2024,2023,1987,-1,1987,1988,2024,-1,2025,2024,1988,-1,1988,1989,2025,-1,2026,2025,1989,-1,1989,1990,2026,-1,2027,2026,1990,-1,1990,1991,2027,-1,2028,2027,1991,-1,1991,1992,2028,-1,2029,2028,1992,-1,1992,1993,2029,-1,2030,2029,1993,-1,1993,1994,2030,-1,2031,2030,1994,-1,1994,1995,2031,-1,2032,2031,1995,-1,1995,1996,2032,-1,2033,2032,1996,-1,1996,1997,2033,-1,2034,2033,1997,-1,1997,1998,2034,-1,2035,2036,1999,-1,1999,2000,2035,-1,2037,2035,2000,-1,2000,2001,2037,-1,2038,2037,2001,-1,2001,2002,2038,-1,2039,2038,2002,-1,2002,2003,2039,-1,2040,2039,2003,-1,2003,2004,2040,-1,2041,2040,2004,-1,2004,2005,2041,-1,2042,2041,2005,-1,2005,2006,2042,-1,2043,2042,2006,-1,2006,2007,2043,-1,2044,2043,2007,-1,2007,2008,2044,-1,2045,2044,2008,-1,2008,2009,2045,-1,2046,2045,2009,-1,2009,2010,2046,-1,2047,2046,2010,-1,2010,2011,2047,-1,2048,2047,2011,-1,2011,2012,2048,-1,2049,2048,2012,-1,2012,2013,2049,-1,2050,2049,2013,-1,2013,2014,2050,-1,2051,2050,2014,-1,2014,2015,2051,-1,2052,2051,2015,-1,2015,2016,2052,-1,2053,2052,2016,-1,2016,2017,2053,-1,2054,2053,2017,-1,2017,2018,2054,-1,2055,2054,2018,-1,2018,2019,2055,-1,2056,2055,2019,-1,2019,2020,2056,-1,2057,2056,2020,-1,2020,2021,2057,-1,2058,2057,2021,-1,2021,2022,2058,-1,2059,2058,2022,-1,2022,2023,2059,-1,2060,2059,2023,-1,2023,2024,2060,-1,2061,2060,2024,-1,2024,2025,2061,-1,2062,2061,2025,-1,2025,2026,2062,-1,2063,2062,2026,-1,2026,2027,2063,-1,2064,2063,2027,-1,2027,2028,2064,-1,2065,2064,2028,-1,2028,2029,2065,-1,2066,2065,2029,-1,2029,2030,2066,-1,2067,2066,2030,-1,2030,2031,2067,-1,2068,2067,2031,-1,2031,2032,2068,-1,2069,2068,2032,-1,2032,2033,2069,-1,2070,2069,2033,-1,2033,2034,2070,-1,2036,2035,2071,-1,2072,2071,2035,-1,2035,2037,2072,-1,2073,2072,2037,-1,2037,2038,2073,-1,2074,2073,2038,-1,2038,2039,2074,-1,2075,2074,2039,-1,2039,2040,2075,-1,2076,2075,2040,-1,2040,2041,2076,-1,2077,2076,2041,-1,2041,2042,2077,-1,2078,2077,2042,-1,2042,2043,2078,-1,2079,2078,2043,-1,2043,2044,2079,-1,2080,2079,2044,-1,2044,2045,2080,-1,2081,2080,2045,-1,2045,2046,2081,-1,2082,2081,2046,-1,2046,2047,2082,-1,2083,2082,2047,-1,2047,2048,2083,-1,2084,2083,2048,-1,2048,2049,2084,-1,2085,2084,2049,-1,2049,2050,2085,-1,2086,2085,2050,-1,2050,2051,2086,-1,2087,2086,2051,-1,2051,2052,2087,-1,2088,2087,2052,-1,2052,2053,2088,-1,2089,2088,2053,-1,2053,2054,2089,-1,2090,2089,2054,-1,2054,2055,2090,-1,2091,2090,2055,-1,2055,2056,2091,-1,2092,2091,2056,-1,2056,2057,2092,-1,2093,2092,2057,-1,2057,2058,2093,-1,2094,2093,2058,-1,2058,2059,2094,-1,2095,2094,2059,-1,2059,2060,2095,-1,2096,2095,2060,-1,2060,2061,2096,-1,2097,2096,2061,-1,2061,2062,2097,-1,2098,2097,2062,-1,2062,2063,2098,-1,2099,2098,2063,-1,2063,2064,2099,-1,2100,2099,2064,-1,2064,2065,2100,-1,2101,2100,2065,-1,2065,2066,2101,-1,2102,2101,2066,-1,2066,2067,2102,-1,2103,2102,2067,-1,2067,2068,2103,-1,2104,2103,2068,-1,2068,2069,2104,-1,2071,2072,2105,-1,2106,2105,2072,-1,2072,2073,2106,-1,2107,2106,2073,-1,2073,2074,2107,-1,2108,2107,2074,-1,2074,2075,2108,-1,2109,2108,2075,-1,2075,2076,2109,-1,2110,2109,2076,-1,2076,2077,2110,-1,2111,2110,2077,-1,2077,2078,2111,-1,2112,2111,2078,-1,2078,2079,2112,-1,2113,2112,2079,-1,2079,2080,2113,-1,2114,2113,2080,-1,2080,2081,2114,-1,2115,2114,2081,-1,2081,2082,2115,-1,2116,2115,2082,-1,2082,2083,2116,-1,2117,2116,2083,-1,2083,2084,2117,-1,2118,2117,2084,-1,2084,2085,2118,-1,2119,2118,2085,-1,2085,2086,2119,-1,2120,2119,2086,-1,2086,2087,2120,-1,2121,2120,2087,-1,2087,2088,2121,-1,2122,2121,2088,-1,2088,2089,2122,-1,2123,2122,2089,-1,2089,2090,2123,-1,2124,2123,2090,-1,2090,2091,2124,-1,2125,2124,2091,-1,2091,2092,2125,-1,2126,2125,2092,-1,2092,2093,2126,-1,2127,2126,2093,-1,2093,2094,2127,-1,2128,2127,2094,-1,2094,2095,2128,-1,2129,2128,2095,-1,2095,2096,2129,-1,2130,2129,2096,-1,2096,2097,2130,-1,2131,2130,2097,-1,2097,2098,2131,-1,2132,2131,2098,-1,2098,2099,2132,-1,2133,2132,2099,-1,2099,2100,2133,-1,2134,2133,2100,-1,2100,2101,2134,-1,2135,2134,2101,-1,2101,2102,2135,-1,2136,2135,2102,-1,2102,2103,2136,-1,2137,2136,2103,-1,2103,2104,2137,-1,2138,2139,2105,-1,2105,2106,2138,-1,2140,2138,2106,-1,2106,2107,2140,-1,2141,2140,2107,-1,2107,2108,2141,-1,2142,2141,2108,-1,2108,2109,2142,-1,2143,2142,2109,-1,2109,2110,2143,-1,2144,2143,2110,-1,2110,2111,2144,-1,2145,2144,2111,-1,2111,2112,2145,-1,2146,2145,2112,-1,2112,2113,2146,-1,2147,2146,2113,-1,2113,2114,2147,-1,2148,2147,2114,-1,2114,2115,2148,-1,2149,2148,2115,-1,2115,2116,2149,-1,2150,2149,2116,-1,2116,2117,2150,-1,2151,2150,2117,-1,2117,2118,2151,-1,2152,2151,2118,-1,2118,2119,2152,-1,2153,2152,2119,-1,2119,2120,2153,-1,2154,2153,2120,-1,2120,2121,2154,-1,2155,2154,2121,-1,2121,2122,2155,-1,2156,2155,2122,-1,2122,2123,2156,-1,2157,2156,2123,-1,2123,2124,2157,-1,2158,2157,2124,-1,2124,2125,2158,-1,2159,2158,2125,-1,2125,2126,2159,-1,2160,2159,2126,-1,2126,2127,2160,-1,2161,2160,2127,-1,2127,2128,2161,-1,2162,2161,2128,-1,2128,2129,2162,-1,2163,2162,2129,-1,2129,2130,2163,-1,2164,2163,2130,-1,2130,2131,2164,-1,2165,2164,2131,-1,2131,2132,2165,-1,2166,2165,2132,-1,2132,2133,2166,-1,2167,2166,2133,-1,2133,2134,2167,-1,2168,2167,2134,-1,2134,2135,2168,-1,2169,2168,2135,-1,2135,2136,2169,-1,2170,2169,2136,-1,2136,2137,2170,-1,2139,2138,2171,-1,2172,2171,2138,-1,2138,2140,2172,-1,2173,2172,2140,-1,2140,2141,2173,-1,2174,2173,2141,-1,2141,2142,2174,-1,2175,2174,2142,-1,2142,2143,2175,-1,2176,2175,2143,-1,2143,2144,2176,-1,2177,2176,2144,-1,2144,2145,2177,-1,2178,2177,2145,-1,2145,2146,2178,-1,2179,2178,2146,-1,2146,2147,2179,-1,2180,2179,2147,-1,2147,2148,2180,-1,2181,2180,2148,-1,2148,2149,2181,-1,2182,2181,2149,-1,2149,2150,2182,-1,2183,2182,2150,-1,2150,2151,2183,-1,2184,2183,2151,-1,2151,2152,2184,-1,2185,2184,2152,-1,2152,2153,2185,-1,2186,2185,2153,-1,2153,2154,2186,-1,2187,2186,2154,-1,2154,2155,2187,-1,2188,2187,2155,-1,2155,2156,2188,-1,2189,2188,2156,-1,2156,2157,2189,-1,2190,2189,2157,-1,2157,2158,2190,-1,2191,2190,2158,-1,2158,2159,2191,-1,2192,2191,2159,-1,2159,2160,2192,-1,2193,2192,2160,-1,2160,2161,2193,-1,2194,2193,2161,-1,2161,2162,2194,-1,2195,2194,2162,-1,2162,2163,2195,-1,2196,2195,2163,-1,2163,2164,2196,-1,2197,2196,2164,-1,2164,2165,2197,-1,2198,2197,2165,-1,2165,2166,2198,-1,2199,2198,2166,-1,2166,2167,2199,-1,2200,2199,2167,-1,2167,2168,2200,-1,2201,2200,2168,-1,2168,2169,2201,-1,2202,2201,2169,-1,2169,2170,2202,-1,2203,2202,2170,-1,2204,2205,2171,-1,2171,2172,2204,-1,2206,2204,2172,-1,2172,2173,2206,-1,2207,2206,2173,-1,2173,2174,2207,-1,2208,2207,2174,-1,2174,2175,2208,-1,2176,2177,2209,-1,2210,2209,2177,-1,2177,2178,2210,-1,2211,2210,2178,-1,2178,2179,2211,-1,2212,2211,2179,-1,2179,2180,2212,-1,2213,2212,2180,-1,2180,2181,2213,-1,2214,2213,2181,-1,2181,2182,2214,-1,2215,2214,2182,-1,2182,2183,2215,-1,2216,2215,2183,-1,2183,2184,2216,-1,2217,2216,2184,-1,2184,2185,2217,-1,2218,2217,2185,-1,2185,2186,2218,-1,2219,2218,2186,-1,2186,2187,2219,-1,2220,2219,2187,-1,2187,2188,2220,-1,2221,2220,2188,-1,2188,2189,2221,-1,2222,2221,2189,-1,2189,2190,2222,-1,2223,2222,2190,-1,2190,2191,2223,-1,2224,2223,2191,-1,2191,2192,2224,-1,2225,2224,2192,-1,2192,2193,2225,-1,2226,2225,2193,-1,2193,2194,2226,-1,2227,2226,2194,-1,2194,2195,2227,-1,2228,2227,2195,-1,2195,2196,2228,-1,2229,2228,2196,-1,2196,2197,2229,-1,2230,2229,2197,-1,2197,2198,2230,-1,2231,2230,2198,-1,2198,2199,2231,-1,2232,2231,2199,-1,2199,2200,2232,-1,2233,2232,2200,-1,2200,2201,2233,-1,2234,2233,2201,-1,2201,2202,2234,-1,2235,2234,2202,-1,2202,2203,2235,-1,2205,2204,2236,-1,2237,2236,2204,-1,2204,2206,2237,-1,2238,2237,2206,-1,2206,2207,2238,-1,2239,2238,2207,-1,2207,2208,2239,-1,2210,2211,2240,-1,2241,2240,2211,-1,2211,2212,2241,-1,2242,2241,2212,-1,2212,2213,2242,-1,2243,2242,2213,-1,2213,2214,2243,-1,2244,2243,2214,-1,2214,2215,2244,-1,2245,2244,2215,-1,2215,2216,2245,-1,2246,2245,2216,-1,2216,2217,2246,-1,2247,2246,2217,-1,2217,2218,2247,-1,2248,2247,2218,-1,2218,2219,2248,-1,2249,2248,2219,-1,2219,2220,2249,-1,2250,2249,2220,-1,2220,2221,2250,-1,2251,2250,2221,-1,2221,2222,2251,-1,2252,2251,2222,-1,2222,2223,2252,-1,2253,2252,2223,-1,2223,2224,2253,-1,2254,2253,2224,-1,2224,2225,2254,-1,2255,2254,2225,-1,2225,2226,2255,-1,2256,2255,2226,-1,2226,2227,2256,-1,2257,2256,2227,-1,2227,2228,2257,-1,2258,2257,2228,-1,2228,2229,2258,-1,2259,2258,2229,-1,2229,2230,2259,-1,2260,2259,2230,-1,2230,2231,2260,-1,2261,2260,2231,-1,2231,2232,2261,-1,2262,2261,2232,-1,2232,2233,2262,-1,2263,2262,2233,-1,2233,2234,2263,-1,2264,2263,2234,-1,2234,2235,2264,-1]
IndexedFaceSet320.creaseAngle = 1.57
IndexedFaceSet320.solid = False
Coordinate321 = x3d.Coordinate()

IndexedFaceSet320.coord = Coordinate321
TextureCoordinate322 = x3d.TextureCoordinate()

IndexedFaceSet320.texCoord = TextureCoordinate322

Shape316.geometry = IndexedFaceSet320

Transform315.children.append(Shape316)

fieldValue314.children.append(Transform315)

ProtoInstance312.fieldValue.append(fieldValue314)

fieldValue311.children.append(ProtoInstance312)

ProtoInstance307.fieldValue.append(fieldValue311)

fieldValue296.children.append(ProtoInstance307)

ProtoInstance293.fieldValue.append(fieldValue296)

fieldValue200.children.append(ProtoInstance293)

ProtoInstance197.fieldValue.append(fieldValue200)

fieldValue100.children.append(ProtoInstance197)

ProtoInstance97.fieldValue.append(fieldValue100)

fieldValue96.children.append(ProtoInstance97)
Group323 = x3d.Group()

fieldValue96.children.append(Group323)

ProtoInstance95.fieldValue.append(fieldValue96)
fieldValue324 = x3d.fieldValue()
fieldValue324.name = "joints"
ProtoInstance325 = x3d.ProtoInstance()
ProtoInstance325.USE = "hanim_humanoid_root"

fieldValue324.children.append(ProtoInstance325)
ProtoInstance326 = x3d.ProtoInstance()
ProtoInstance326.USE = "hanim_sacroiliac"

fieldValue324.children.append(ProtoInstance326)
ProtoInstance327 = x3d.ProtoInstance()
ProtoInstance327.USE = "hanim_l_hip"

fieldValue324.children.append(ProtoInstance327)
ProtoInstance328 = x3d.ProtoInstance()
ProtoInstance328.USE = "hanim_l_knee"

fieldValue324.children.append(ProtoInstance328)
ProtoInstance329 = x3d.ProtoInstance()
ProtoInstance329.USE = "hanim_l_ankle"

fieldValue324.children.append(ProtoInstance329)
ProtoInstance330 = x3d.ProtoInstance()
ProtoInstance330.USE = "hanim_r_hip"

fieldValue324.children.append(ProtoInstance330)
ProtoInstance331 = x3d.ProtoInstance()
ProtoInstance331.USE = "hanim_r_knee"

fieldValue324.children.append(ProtoInstance331)
ProtoInstance332 = x3d.ProtoInstance()
ProtoInstance332.USE = "hanim_r_ankle"

fieldValue324.children.append(ProtoInstance332)
ProtoInstance333 = x3d.ProtoInstance()
ProtoInstance333.USE = "hanim_vl1"

fieldValue324.children.append(ProtoInstance333)
ProtoInstance334 = x3d.ProtoInstance()
ProtoInstance334.USE = "hanim_l_shoulder"

fieldValue324.children.append(ProtoInstance334)
ProtoInstance335 = x3d.ProtoInstance()
ProtoInstance335.USE = "hanim_l_elbow"

fieldValue324.children.append(ProtoInstance335)
ProtoInstance336 = x3d.ProtoInstance()
ProtoInstance336.USE = "hanim_l_wrist"

fieldValue324.children.append(ProtoInstance336)
ProtoInstance337 = x3d.ProtoInstance()
ProtoInstance337.USE = "hanim_r_shoulder"

fieldValue324.children.append(ProtoInstance337)
ProtoInstance338 = x3d.ProtoInstance()
ProtoInstance338.USE = "hanim_r_elbow"

fieldValue324.children.append(ProtoInstance338)
ProtoInstance339 = x3d.ProtoInstance()
ProtoInstance339.USE = "hanim_r_wrist"

fieldValue324.children.append(ProtoInstance339)
ProtoInstance340 = x3d.ProtoInstance()
ProtoInstance340.USE = "hanim_vc4"

fieldValue324.children.append(ProtoInstance340)
ProtoInstance341 = x3d.ProtoInstance()
ProtoInstance341.USE = "hanim_skullbase"

fieldValue324.children.append(ProtoInstance341)

ProtoInstance95.fieldValue.append(fieldValue324)
fieldValue342 = x3d.fieldValue()
fieldValue342.name = "segments"
ProtoInstance343 = x3d.ProtoInstance()
ProtoInstance343.USE = "hanim_pelvis"

fieldValue342.children.append(ProtoInstance343)
ProtoInstance344 = x3d.ProtoInstance()
ProtoInstance344.USE = "hanim_l_thigh"

fieldValue342.children.append(ProtoInstance344)
ProtoInstance345 = x3d.ProtoInstance()
ProtoInstance345.USE = "hanim_l_calf"

fieldValue342.children.append(ProtoInstance345)
ProtoInstance346 = x3d.ProtoInstance()
ProtoInstance346.USE = "hanim_l_hindfoot"

fieldValue342.children.append(ProtoInstance346)
ProtoInstance347 = x3d.ProtoInstance()
ProtoInstance347.USE = "hanim_r_thigh"

fieldValue342.children.append(ProtoInstance347)
ProtoInstance348 = x3d.ProtoInstance()
ProtoInstance348.USE = "hanim_r_calf"

fieldValue342.children.append(ProtoInstance348)
ProtoInstance349 = x3d.ProtoInstance()
ProtoInstance349.USE = "hanim_r_hindfoot"

fieldValue342.children.append(ProtoInstance349)
ProtoInstance350 = x3d.ProtoInstance()
ProtoInstance350.USE = "hanim_c7"

fieldValue342.children.append(ProtoInstance350)
ProtoInstance351 = x3d.ProtoInstance()
ProtoInstance351.USE = "hanim_l_upperarm"

fieldValue342.children.append(ProtoInstance351)
ProtoInstance352 = x3d.ProtoInstance()
ProtoInstance352.USE = "hanim_l_forearm"

fieldValue342.children.append(ProtoInstance352)
ProtoInstance353 = x3d.ProtoInstance()
ProtoInstance353.USE = "hanim_l_hand"

fieldValue342.children.append(ProtoInstance353)
ProtoInstance354 = x3d.ProtoInstance()
ProtoInstance354.USE = "hanim_r_upperarm"

fieldValue342.children.append(ProtoInstance354)
ProtoInstance355 = x3d.ProtoInstance()
ProtoInstance355.USE = "hanim_r_forearm"

fieldValue342.children.append(ProtoInstance355)
ProtoInstance356 = x3d.ProtoInstance()
ProtoInstance356.USE = "hanim_r_hand"

fieldValue342.children.append(ProtoInstance356)
ProtoInstance357 = x3d.ProtoInstance()
ProtoInstance357.USE = "hanim_c4"

fieldValue342.children.append(ProtoInstance357)
ProtoInstance358 = x3d.ProtoInstance()
ProtoInstance358.USE = "hanim_skull"

fieldValue342.children.append(ProtoInstance358)

ProtoInstance95.fieldValue.append(fieldValue342)
fieldValue359 = x3d.fieldValue()
fieldValue359.name = "viewpoints"
Viewpoint360 = x3d.Viewpoint()
Viewpoint360.DEF = "InclinedView"
Viewpoint360.description = "Inclined View"
Viewpoint360.orientation = [-0.113,0.993,0.0347,0.671]
Viewpoint360.position = [1.62,1.05,2.06]

fieldValue359.children.append(Viewpoint360)
Viewpoint361 = x3d.Viewpoint()
Viewpoint361.DEF = "FrontView"
Viewpoint361.description = "Front View"
Viewpoint361.position = [0,0.854,2.57665]

fieldValue359.children.append(Viewpoint361)
Viewpoint362 = x3d.Viewpoint()
Viewpoint362.DEF = "SideView"
Viewpoint362.description = "Side View"
Viewpoint362.orientation = [0,1,0,1.57079]
Viewpoint362.position = [2.5929,0.854,0]

fieldValue359.children.append(Viewpoint362)
Viewpoint363 = x3d.Viewpoint()
Viewpoint363.DEF = "TopView"
Viewpoint363.description = "Top View"
Viewpoint363.orientation = [1,0,0,-1.57079]
Viewpoint363.position = [0,3.4495,0]

fieldValue359.children.append(Viewpoint363)

ProtoInstance95.fieldValue.append(fieldValue359)

Scene17.children.append(ProtoInstance95)
NavigationInfo364 = x3d.NavigationInfo()
NavigationInfo364.avatarSize = [0.15,1.53,0.75]
NavigationInfo364.speed = 0.5
NavigationInfo364.type = ["EXAMINE"]

Scene17.children.append(NavigationInfo364)
Group365 = x3d.Group()
Group365.DEF = "Interface"
Transform366 = x3d.Transform()
ProximitySensor367 = x3d.ProximitySensor()
ProximitySensor367.DEF = "HudProx"
ProximitySensor367.center = [0,20,0]
ProximitySensor367.size = [500,100,500]

Transform366.children.append(ProximitySensor367)

Group365.children.append(Transform366)
Collision368 = x3d.Collision()
Collision368.DEF = "HUD"
Collision368.enabled = False
Transform369 = x3d.Transform()
Transform369.DEF = "HudXform"
Transform370 = x3d.Transform()
Transform370.scale = [0.012,0.012,0.012]
Transform370.translation = [0.01107,-0.025,-0.08]
Transform371 = x3d.Transform()
Transform371.DEF = "Stand_Text"
TouchSensor372 = x3d.TouchSensor()
TouchSensor372.DEF = "Stand_Touch"
TouchSensor372.description = "click for behavior"

Transform371.children.append(TouchSensor372)
Shape373 = x3d.Shape()
Shape373.DEF = "Stand"
IndexedFaceSet374 = x3d.IndexedFaceSet()
IndexedFaceSet374.coordIndex = [1,30,29,-1,1,29,2,-1,31,47,46,-1,31,46,32,-1,78,77,80,-1,78,80,79,-1,96,113,112,-1,96,112,95,-1,95,112,111,-1,95,111,94,-1,94,111,110,-1,94,110,93,-1,93,110,109,-1,93,109,108,-1,93,108,100,-1,107,99,100,-1,107,100,108,-1,107,106,99,-1,106,105,98,-1,106,98,99,-1,104,97,98,-1,104,98,105,-1,103,102,104,-1,104,102,101,-1,104,101,97,-1,101,96,97,-1,101,97,101,-1,101,101,96,-1,96,101,113,-1,113,101,114,-1,115,86,85,-1,115,85,116,-1,117,87,84,-1,117,84,118,-1,119,83,120,-1,121,88,82,-1,121,82,122,-1,123,89,81,-1,123,81,124,-1,125,90,126,-1,127,92,128,-1,129,91,130,-1,54,49,50,-1,54,50,55,-1,76,75,74,-1,76,74,54,-1,54,74,73,-1,54,73,49,-1,49,73,48,-1,48,73,62,-1,48,62,61,-1,48,61,60,-1,48,60,53,-1,53,60,59,-1,53,59,53,-1,53,59,58,-1,53,58,52,-1,52,58,57,-1,52,57,51,-1,56,51,57,-1,56,55,50,-1,56,50,51,-1,62,73,72,-1,62,72,63,-1,63,72,71,-1,63,71,64,-1,64,71,70,-1,64,70,69,-1,64,69,65,-1,65,69,68,-1,65,68,67,-1,65,67,66,-1,131,40,39,-1,131,39,132,-1,133,43,42,-1,133,42,134,-1,135,37,36,-1,135,36,136,-1,137,41,38,-1,137,38,138,-1,139,44,35,-1,139,35,140,-1,141,34,142,-1,143,45,33,-1,143,33,144,-1,145,16,15,-1,145,15,146,-1,147,14,148,-1,149,17,13,-1,149,13,150,-1,151,18,12,-1,151,12,152,-1,153,19,11,-1,153,11,154,-1,155,20,10,-1,155,10,156,-1,157,9,158,-1,159,21,8,-1,159,8,160,-1,161,22,7,-1,161,7,162,-1,163,23,164,-1,165,24,6,-1,165,6,166,-1,167,25,5,-1,167,5,168,-1,169,26,170,-1,171,27,4,-1,171,4,172,-1,173,28,3,-1,173,3,174,-1,175,0,176,-1]
Coordinate375 = x3d.Coordinate()

IndexedFaceSet374.coord = Coordinate375

Shape373.geometry = IndexedFaceSet374
Appearance376 = x3d.Appearance()
Material377 = x3d.Material()
Material377.DEF = "text_color"
Material377.ambientIntensity = 0
Material377.diffuseColor = [0,0,0]
Material377.emissiveColor = [0.819,0.521,0.169]

Appearance376.material = Material377

Shape373.appearance = Appearance376

Transform371.children.append(Shape373)
Transform378 = x3d.Transform()
Transform378.scale = [84.89,77.52,77.52]
Transform378.translation = [0.04092,1.843,3.826]
Shape379 = x3d.Shape()
Shape379.DEF = "Stand_Back"
IndexedFaceSet380 = x3d.IndexedFaceSet()
IndexedFaceSet380.coordIndex = [0,2,3,-1,2,0,1,-1]
Coordinate381 = x3d.Coordinate()

IndexedFaceSet380.coord = Coordinate381

Shape379.geometry = IndexedFaceSet380
Appearance382 = x3d.Appearance()
Material383 = x3d.Material()
Material383.DEF = "Clear"
Material383.ambientIntensity = 0
Material383.diffuseColor = [0,0,0]
Material383.transparency = 1

Appearance382.material = Material383

Shape379.appearance = Appearance382

Transform378.children.append(Shape379)

Transform371.children.append(Transform378)

Transform370.children.append(Transform371)
Transform384 = x3d.Transform()
Transform384.DEF = "Walk_Text"
TouchSensor385 = x3d.TouchSensor()
TouchSensor385.DEF = "Walk_Touch"
TouchSensor385.description = "click for behavior"

Transform384.children.append(TouchSensor385)
Shape386 = x3d.Shape()
Shape386.DEF = "WALK"
IndexedFaceSet387 = x3d.IndexedFaceSet()
IndexedFaceSet387.coordIndex = [0,2,1,-1,3,2,0,-1,12,3,0,-1,4,3,12,-1,11,4,12,-1,5,4,11,-1,10,5,11,-1,6,5,10,-1,9,6,10,-1,7,6,9,-1,8,7,9,-1,15,14,13,-1,16,15,13,-1,19,18,17,-1,20,19,17,-1,27,20,17,-1,28,27,17,-1,26,20,27,-1,23,20,26,-1,21,20,23,-1,25,23,26,-1,22,21,23,-1,24,23,25,-1,29,30,31,-1,29,31,32,-1,33,34,35,-1,33,35,29,-1,29,35,36,-1,29,36,30,-1,30,36,37,-1,37,36,38,-1,37,38,39,-1,37,39,40,-1,37,40,41,-1,41,40,42,-1,41,42,41,-1,41,42,43,-1,41,43,44,-1,44,43,45,-1,44,45,46,-1,47,46,45,-1,47,32,31,-1,47,31,46,-1,38,36,48,-1,38,48,49,-1,49,48,50,-1,49,50,51,-1,51,50,52,-1,51,52,53,-1,51,53,54,-1,54,53,55,-1,54,55,56,-1,54,56,57,-1]
Coordinate388 = x3d.Coordinate()

IndexedFaceSet387.coord = Coordinate388

Shape386.geometry = IndexedFaceSet387
Appearance389 = x3d.Appearance()
Material390 = x3d.Material()
Material390.USE = "text_color"

Appearance389.material = Material390

Shape386.appearance = Appearance389

Transform384.children.append(Shape386)
Transform391 = x3d.Transform()
Transform391.scale = [81.3,81.3,81.31]
Transform391.translation = [-0.0414,1.941,4.015]
Shape392 = x3d.Shape()
Shape392.DEF = "Walk_Back"
IndexedFaceSet393 = x3d.IndexedFaceSet()
IndexedFaceSet393.coordIndex = [1,3,0,-1,3,1,2,-1]
Coordinate394 = x3d.Coordinate()

IndexedFaceSet393.coord = Coordinate394

Shape392.geometry = IndexedFaceSet393
Appearance395 = x3d.Appearance()
Material396 = x3d.Material()
Material396.USE = "Clear"

Appearance395.material = Material396

Shape392.appearance = Appearance395

Transform391.children.append(Shape392)

Transform384.children.append(Transform391)

Transform370.children.append(Transform384)
Transform397 = x3d.Transform()
Transform397.DEF = "Run_Text"
TouchSensor398 = x3d.TouchSensor()
TouchSensor398.DEF = "Run_Touch"
TouchSensor398.description = "click for behavior"

Transform397.children.append(TouchSensor398)
Shape399 = x3d.Shape()
Shape399.DEF = "Run"
IndexedFaceSet400 = x3d.IndexedFaceSet()
IndexedFaceSet400.coordIndex = [24,26,25,-1,53,39,54,-1,17,1,0,-1,17,0,16,-1,0,14,16,-1,0,15,14,-1,14,13,22,-1,14,22,16,-1,13,12,21,-1,13,21,22,-1,12,6,21,-1,12,11,7,-1,12,7,6,-1,11,8,7,-1,10,8,11,-1,10,9,8,-1,6,5,21,-1,5,4,20,-1,5,20,21,-1,4,3,19,-1,4,19,20,-1,3,2,18,-1,3,18,19,-1,18,2,1,-1,18,1,17,-1,55,32,31,-1,55,31,56,-1,57,33,30,-1,57,30,58,-1,59,29,60,-1,61,34,28,-1,61,28,62,-1,63,35,27,-1,63,27,64,-1,65,36,66,-1,67,38,68,-1,69,37,70,-1,71,23,72,-1,73,48,47,-1,73,47,74,-1,75,49,46,-1,75,46,76,-1,77,45,78,-1,79,50,44,-1,79,44,80,-1,81,51,43,-1,81,43,82,-1,83,41,84,-1,85,40,86,-1,87,52,88,-1,89,42,90,-1]
Coordinate401 = x3d.Coordinate()

IndexedFaceSet400.coord = Coordinate401

Shape399.geometry = IndexedFaceSet400
Appearance402 = x3d.Appearance()
Material403 = x3d.Material()
Material403.USE = "text_color"

Appearance402.material = Material403

Shape399.appearance = Appearance402

Transform397.children.append(Shape399)
Transform404 = x3d.Transform()
Transform404.scale = [82.47,82.47,82.48]
Transform404.translation = [-0.01579,1.968,4.074]
Shape405 = x3d.Shape()
Shape405.DEF = "Run_Back"
IndexedFaceSet406 = x3d.IndexedFaceSet()
IndexedFaceSet406.coordIndex = [0,2,3,-1,2,0,1,-1]
Coordinate407 = x3d.Coordinate()

IndexedFaceSet406.coord = Coordinate407

Shape405.geometry = IndexedFaceSet406
Appearance408 = x3d.Appearance()
Material409 = x3d.Material()
Material409.USE = "Clear"

Appearance408.material = Material409

Shape405.appearance = Appearance408

Transform404.children.append(Shape405)

Transform397.children.append(Transform404)

Transform370.children.append(Transform397)
Transform410 = x3d.Transform()
Transform410.DEF = "Jump_Text"
TouchSensor411 = x3d.TouchSensor()
TouchSensor411.DEF = "Jump_Touch"
TouchSensor411.description = "click for behavior"

Transform410.children.append(TouchSensor411)
Shape412 = x3d.Shape()
Shape412.DEF = "Jump"
IndexedFaceSet413 = x3d.IndexedFaceSet()
IndexedFaceSet413.coordIndex = [1,0,14,-1,1,14,2,-1,16,15,18,-1,16,18,17,-1,64,65,66,-1,67,68,69,-1,67,69,70,-1,71,72,73,-1,71,73,74,-1,75,76,77,-1,78,79,80,-1,78,80,81,-1,82,83,84,-1,82,84,85,-1,86,87,88,-1,89,90,91,-1,92,93,94,-1,95,96,97,-1,98,7,6,-1,98,6,99,-1,100,8,5,-1,100,5,101,-1,102,9,4,-1,102,4,103,-1,104,10,105,-1,106,11,3,-1,106,3,107,-1,108,12,109,-1,110,13,111,-1,112,27,26,-1,112,26,113,-1,114,28,25,-1,114,25,115,-1,116,24,117,-1,118,29,23,-1,118,23,119,-1,120,30,22,-1,120,22,121,-1,122,31,123,-1,124,34,33,-1,124,33,125,-1,126,35,32,-1,126,32,127,-1,128,21,129,-1,130,36,20,-1,130,20,131,-1,132,37,19,-1,132,19,133,-1,134,38,135,-1,136,40,137,-1,138,39,139,-1,53,58,59,-1,53,59,54,-1,53,52,58,-1,52,51,57,-1,52,57,58,-1,51,50,56,-1,51,56,57,-1,50,49,56,-1,49,48,63,-1,49,63,56,-1,48,47,63,-1,63,47,46,-1,63,46,62,-1,62,46,45,-1,62,45,44,-1,62,44,61,-1,61,44,60,-1,54,59,60,-1,44,43,42,-1,60,44,42,-1,41,55,54,-1,41,54,60,-1,41,60,42,-1]
Coordinate414 = x3d.Coordinate()

IndexedFaceSet413.coord = Coordinate414

Shape412.geometry = IndexedFaceSet413
Appearance415 = x3d.Appearance()
Material416 = x3d.Material()
Material416.USE = "text_color"

Appearance415.material = Material416

Shape412.appearance = Appearance415

Transform410.children.append(Shape412)
Transform417 = x3d.Transform()
Transform417.scale = [83.79,83.79,83.79]
Transform417.translation = [-0.008979,1.99,4.14]
Shape418 = x3d.Shape()
Shape418.DEF = "Jump_Back"
IndexedFaceSet419 = x3d.IndexedFaceSet()
IndexedFaceSet419.coordIndex = [0,2,3,-1,2,0,1,-1]
Coordinate420 = x3d.Coordinate()

IndexedFaceSet419.coord = Coordinate420

Shape418.geometry = IndexedFaceSet419
Appearance421 = x3d.Appearance()
Material422 = x3d.Material()
Material422.USE = "Clear"

Appearance421.material = Material422

Shape418.appearance = Appearance421

Transform417.children.append(Shape418)

Transform410.children.append(Transform417)

Transform370.children.append(Transform410)

Transform369.children.append(Transform370)

Collision368.proxy = Transform369

Group365.children.append(Collision368)
Transform423 = x3d.Transform()
Transform423.DEF = "Floor"
Transform423.scale = [1,0.0125,1]
Transform423.translation = [0,-0.0125,0]
Shape424 = x3d.Shape()
Box425 = x3d.Box()

Shape424.geometry = Box425
Appearance426 = x3d.Appearance()
Material427 = x3d.Material()

Appearance426.material = Material427

Shape424.appearance = Appearance426

Transform423.children.append(Shape424)

Group365.children.append(Transform423)

Scene17.children.append(Group365)
Group428 = x3d.Group()
Group428.DEF = "Animations"
Group429 = x3d.Group()
Group429.DEF = "Stand_Animation"
OrientationInterpolator430 = x3d.OrientationInterpolator()
OrientationInterpolator430.DEF = "r_ankle_RotationInterpolator_Stand"
OrientationInterpolator430.key = [0,1]

Group429.children.append(OrientationInterpolator430)
OrientationInterpolator431 = x3d.OrientationInterpolator()
OrientationInterpolator431.DEF = "r_knee_RotationInterpolator_Stand"
OrientationInterpolator431.key = [0,1]

Group429.children.append(OrientationInterpolator431)
OrientationInterpolator432 = x3d.OrientationInterpolator()
OrientationInterpolator432.DEF = "r_hip_RotationInterpolator_Stand"
OrientationInterpolator432.key = [0,1]

Group429.children.append(OrientationInterpolator432)
OrientationInterpolator433 = x3d.OrientationInterpolator()
OrientationInterpolator433.DEF = "l_ankle_RotationInterpolator_Stand"
OrientationInterpolator433.key = [0,1]

Group429.children.append(OrientationInterpolator433)
OrientationInterpolator434 = x3d.OrientationInterpolator()
OrientationInterpolator434.DEF = "l_knee_RotationInterpolator_Stand"
OrientationInterpolator434.key = [0,1]

Group429.children.append(OrientationInterpolator434)
OrientationInterpolator435 = x3d.OrientationInterpolator()
OrientationInterpolator435.DEF = "l_hip_RotationInterpolator_Stand"
OrientationInterpolator435.key = [0,1]

Group429.children.append(OrientationInterpolator435)
OrientationInterpolator436 = x3d.OrientationInterpolator()
OrientationInterpolator436.DEF = "lower_body_RotationInterpolator_Stand"
OrientationInterpolator436.key = [0,1]

Group429.children.append(OrientationInterpolator436)
OrientationInterpolator437 = x3d.OrientationInterpolator()
OrientationInterpolator437.DEF = "r_wrist_RotationInterpolator_Stand"
OrientationInterpolator437.key = [0,1]

Group429.children.append(OrientationInterpolator437)
OrientationInterpolator438 = x3d.OrientationInterpolator()
OrientationInterpolator438.DEF = "r_elbow_RotationInterpolator_Stand"
OrientationInterpolator438.key = [0,1]

Group429.children.append(OrientationInterpolator438)
OrientationInterpolator439 = x3d.OrientationInterpolator()
OrientationInterpolator439.DEF = "r_shoulder_RotationInterpolator_Stand"
OrientationInterpolator439.key = [0,1]

Group429.children.append(OrientationInterpolator439)
OrientationInterpolator440 = x3d.OrientationInterpolator()
OrientationInterpolator440.DEF = "l_wrist_RotationInterpolator_Stand"
OrientationInterpolator440.key = [0,1]

Group429.children.append(OrientationInterpolator440)
OrientationInterpolator441 = x3d.OrientationInterpolator()
OrientationInterpolator441.DEF = "l_elbow_RotationInterpolator_Stand"
OrientationInterpolator441.key = [0,1]

Group429.children.append(OrientationInterpolator441)
OrientationInterpolator442 = x3d.OrientationInterpolator()
OrientationInterpolator442.DEF = "l_shoulder_RotationInterpolator_Stand"
OrientationInterpolator442.key = [0,1]

Group429.children.append(OrientationInterpolator442)
OrientationInterpolator443 = x3d.OrientationInterpolator()
OrientationInterpolator443.DEF = "head_RotationInterpolator_Stand"
OrientationInterpolator443.key = [0,1]

Group429.children.append(OrientationInterpolator443)
OrientationInterpolator444 = x3d.OrientationInterpolator()
OrientationInterpolator444.DEF = "neck_RotationInterpolator_Stand"
OrientationInterpolator444.key = [0,1]

Group429.children.append(OrientationInterpolator444)
OrientationInterpolator445 = x3d.OrientationInterpolator()
OrientationInterpolator445.DEF = "upper_body_RotationInterpolator_Stand"
OrientationInterpolator445.key = [0,1]

Group429.children.append(OrientationInterpolator445)
OrientationInterpolator446 = x3d.OrientationInterpolator()
OrientationInterpolator446.DEF = "whole_body_RotationInterpolator_Stand"
OrientationInterpolator446.key = [0,1]

Group429.children.append(OrientationInterpolator446)
PositionInterpolator447 = x3d.PositionInterpolator()
PositionInterpolator447.DEF = "whole_body_TranslationInterpolator_Stand"
PositionInterpolator447.key = [0,1]

Group429.children.append(PositionInterpolator447)
TimeSensor448 = x3d.TimeSensor()
TimeSensor448.DEF = "Stand_Time"
TimeSensor448.cycleInterval = 0.009999999776482582

Group429.children.append(TimeSensor448)

Group428.children.append(Group429)
Group449 = x3d.Group()
Group449.DEF = "Walk_Animation"
OrientationInterpolator450 = x3d.OrientationInterpolator()
OrientationInterpolator450.DEF = "r_ankle_RotationInterpolator_BasicWalk"
OrientationInterpolator450.key = [0,0.125,0.2083,0.375,0.4583,0.5,0.6667,0.75,0.7917,0.9167,1]

Group449.children.append(OrientationInterpolator450)
OrientationInterpolator451 = x3d.OrientationInterpolator()
OrientationInterpolator451.DEF = "r_knee_RotationInterpolator_BasicWalk"
OrientationInterpolator451.key = [0,0.125,0.2083,0.2917,0.375,0.5,0.6667,0.7917,0.9167,1]

Group449.children.append(OrientationInterpolator451)
OrientationInterpolator452 = x3d.OrientationInterpolator()
OrientationInterpolator452.DEF = "r_hip_RotationInterpolator_BasicWalk"
OrientationInterpolator452.key = [0,0.125,0.2083,0.2917,0.375,0.5,0.6667,0.7917,0.9167,1]

Group449.children.append(OrientationInterpolator452)
OrientationInterpolator453 = x3d.OrientationInterpolator()
OrientationInterpolator453.DEF = "l_ankle_RotationInterpolator_BasicWalk"
OrientationInterpolator453.key = [0,0.125,0.2083,0.375,0.6667,0.9167,1]

Group449.children.append(OrientationInterpolator453)
OrientationInterpolator454 = x3d.OrientationInterpolator()
OrientationInterpolator454.DEF = "l_knee_RotationInterpolator_BasicWalk"
OrientationInterpolator454.key = [0,0.2083,0.375,0.5,0.6667,0.7917,0.9167,1]

Group449.children.append(OrientationInterpolator454)
OrientationInterpolator455 = x3d.OrientationInterpolator()
OrientationInterpolator455.DEF = "l_hip_RotationInterpolator_BasicWalk"
OrientationInterpolator455.key = [0,0.25,0.375,0.5,0.6667,0.7917,0.9167,1]

Group449.children.append(OrientationInterpolator455)
OrientationInterpolator456 = x3d.OrientationInterpolator()
OrientationInterpolator456.DEF = "lower_body_RotationInterpolator_BasicWalk"
OrientationInterpolator456.key = [0,0.5,1]

Group449.children.append(OrientationInterpolator456)
OrientationInterpolator457 = x3d.OrientationInterpolator()
OrientationInterpolator457.DEF = "r_wrist_RotationInterpolator_BasicWalk"
OrientationInterpolator457.key = [0,0.375,0.9167,1]

Group449.children.append(OrientationInterpolator457)
OrientationInterpolator458 = x3d.OrientationInterpolator()
OrientationInterpolator458.DEF = "r_elbow_RotationInterpolator_BasicWalk"
OrientationInterpolator458.key = [0,0.375,0.9167,1]

Group449.children.append(OrientationInterpolator458)
OrientationInterpolator459 = x3d.OrientationInterpolator()
OrientationInterpolator459.DEF = "r_shoulder_RotationInterpolator_BasicWalk"
OrientationInterpolator459.key = [0,0.375,0.9167,1]

Group449.children.append(OrientationInterpolator459)
OrientationInterpolator460 = x3d.OrientationInterpolator()
OrientationInterpolator460.DEF = "l_wrist_RotationInterpolator_BasicWalk"
OrientationInterpolator460.key = [0,0.375,0.9167,1]

Group449.children.append(OrientationInterpolator460)
OrientationInterpolator461 = x3d.OrientationInterpolator()
OrientationInterpolator461.DEF = "l_elbow_RotationInterpolator_BasicWalk"
OrientationInterpolator461.key = [0,0.375,0.9167,1]

Group449.children.append(OrientationInterpolator461)
OrientationInterpolator462 = x3d.OrientationInterpolator()
OrientationInterpolator462.DEF = "l_shoulder_RotationInterpolator_BasicWalk"
OrientationInterpolator462.key = [0,0.375,0.9167,1]

Group449.children.append(OrientationInterpolator462)
OrientationInterpolator463 = x3d.OrientationInterpolator()
OrientationInterpolator463.DEF = "head_RotationInterpolator_BasicWalk"
OrientationInterpolator463.key = [0,0.375,0.4167,0.5,0.5833,0.6667,0.75,0.8333,0.9167,1]

Group449.children.append(OrientationInterpolator463)
OrientationInterpolator464 = x3d.OrientationInterpolator()
OrientationInterpolator464.DEF = "neck_RotationInterpolator_BasicWalk"
OrientationInterpolator464.key = [0,1]

Group449.children.append(OrientationInterpolator464)
OrientationInterpolator465 = x3d.OrientationInterpolator()
OrientationInterpolator465.DEF = "upper_body_RotationInterpolator_BasicWalk"
OrientationInterpolator465.key = [0,0.2083,0.375,0.75,0.8333,1]

Group449.children.append(OrientationInterpolator465)
OrientationInterpolator466 = x3d.OrientationInterpolator()
OrientationInterpolator466.DEF = "whole_body_RotationInterpolator_BasicWalk"
OrientationInterpolator466.key = [0,1]

Group449.children.append(OrientationInterpolator466)
PositionInterpolator467 = x3d.PositionInterpolator()
PositionInterpolator467.DEF = "whole_body_TranslationInterpolator_BasicWalk"
PositionInterpolator467.key = [0,0.04167,0.125,0.1667,0.2083,0.25,0.2917,0.375,0.4583,0.5,0.5417,0.5833,0.625,0.7083,0.75,0.7917,0.875,0.9167,1]

Group449.children.append(PositionInterpolator467)
TimeSensor468 = x3d.TimeSensor()
TimeSensor468.DEF = "Walk_Time"
TimeSensor468.cycleInterval = 2
TimeSensor468.loop = True
TimeSensor468.startTime = -1

Group449.children.append(TimeSensor468)

Group428.children.append(Group449)
Group469 = x3d.Group()
Group469.DEF = "Run_Animation"
OrientationInterpolator470 = x3d.OrientationInterpolator()
OrientationInterpolator470.DEF = "r_ankle_RotationInterpolator_Run"
OrientationInterpolator470.key = [0,0.4909,0.7091,0.8,0.8182,1]

Group469.children.append(OrientationInterpolator470)
OrientationInterpolator471 = x3d.OrientationInterpolator()
OrientationInterpolator471.DEF = "r_knee_RotationInterpolator_Run"
OrientationInterpolator471.key = [0,0.03636,0.2182,0.4909,0.7455,1]

Group469.children.append(OrientationInterpolator471)
OrientationInterpolator472 = x3d.OrientationInterpolator()
OrientationInterpolator472.DEF = "r_hip_RotationInterpolator_Run"
OrientationInterpolator472.key = [0,0.2182,0.4909,0.7455,1]

Group469.children.append(OrientationInterpolator472)
OrientationInterpolator473 = x3d.OrientationInterpolator()
OrientationInterpolator473.DEF = "l_ankle_RotationInterpolator_Run"
OrientationInterpolator473.key = [0,0.2182,0.3091,0.4909,1]

Group469.children.append(OrientationInterpolator473)
OrientationInterpolator474 = x3d.OrientationInterpolator()
OrientationInterpolator474.DEF = "l_knee_RotationInterpolator_Run"
OrientationInterpolator474.key = [0,0.2182,0.4909,0.7455,1]

Group469.children.append(OrientationInterpolator474)
OrientationInterpolator475 = x3d.OrientationInterpolator()
OrientationInterpolator475.DEF = "l_hip_RotationInterpolator_Run"
OrientationInterpolator475.key = [0,0.2182,0.4909,0.7455,1]

Group469.children.append(OrientationInterpolator475)
OrientationInterpolator476 = x3d.OrientationInterpolator()
OrientationInterpolator476.DEF = "lower_body_RotationInterpolator_Run"
OrientationInterpolator476.key = [0,1]

Group469.children.append(OrientationInterpolator476)
OrientationInterpolator477 = x3d.OrientationInterpolator()
OrientationInterpolator477.DEF = "r_wrist_RotationInterpolator_Run"
OrientationInterpolator477.key = [0,1]

Group469.children.append(OrientationInterpolator477)
OrientationInterpolator478 = x3d.OrientationInterpolator()
OrientationInterpolator478.DEF = "r_elbow_RotationInterpolator_Run"
OrientationInterpolator478.key = [0,0.2182,0.4909,0.7455,1]

Group469.children.append(OrientationInterpolator478)
OrientationInterpolator479 = x3d.OrientationInterpolator()
OrientationInterpolator479.DEF = "r_shoulder_RotationInterpolator_Run"
OrientationInterpolator479.key = [0,0.2182,0.4909,0.7455,1]

Group469.children.append(OrientationInterpolator479)
OrientationInterpolator480 = x3d.OrientationInterpolator()
OrientationInterpolator480.DEF = "l_wrist_RotationInterpolator_Run"
OrientationInterpolator480.key = [0,1]

Group469.children.append(OrientationInterpolator480)
OrientationInterpolator481 = x3d.OrientationInterpolator()
OrientationInterpolator481.DEF = "l_elbow_RotationInterpolator_Run"
OrientationInterpolator481.key = [0,0.2182,0.4909,0.7455,1]

Group469.children.append(OrientationInterpolator481)
OrientationInterpolator482 = x3d.OrientationInterpolator()
OrientationInterpolator482.DEF = "l_shoulder_RotationInterpolator_Run"
OrientationInterpolator482.key = [0,0.2182,0.4909,0.7455,1]

Group469.children.append(OrientationInterpolator482)
OrientationInterpolator483 = x3d.OrientationInterpolator()
OrientationInterpolator483.DEF = "head_RotationInterpolator_Run"
OrientationInterpolator483.key = [0,0.4909,1]

Group469.children.append(OrientationInterpolator483)
OrientationInterpolator484 = x3d.OrientationInterpolator()
OrientationInterpolator484.DEF = "neck_RotationInterpolator_Run"
OrientationInterpolator484.key = [0,1]

Group469.children.append(OrientationInterpolator484)
OrientationInterpolator485 = x3d.OrientationInterpolator()
OrientationInterpolator485.DEF = "upper_body_RotationInterpolator_Run"
OrientationInterpolator485.key = [0,0.2545,0.4909,0.7636,1]

Group469.children.append(OrientationInterpolator485)
OrientationInterpolator486 = x3d.OrientationInterpolator()
OrientationInterpolator486.DEF = "whole_body_RotationInterpolator_Run"
OrientationInterpolator486.key = [0,1]

Group469.children.append(OrientationInterpolator486)
PositionInterpolator487 = x3d.PositionInterpolator()
PositionInterpolator487.DEF = "whole_body_TranslationInterpolator_Run"
PositionInterpolator487.key = [0,0.2182,0.2909,0.3091,0.7091,0.8,0.8182,1]

Group469.children.append(PositionInterpolator487)
TimeSensor488 = x3d.TimeSensor()
TimeSensor488.DEF = "Run_Time"
TimeSensor488.loop = True
TimeSensor488.startTime = -1

Group469.children.append(TimeSensor488)

Group428.children.append(Group469)
Group489 = x3d.Group()
Group489.DEF = "Jump_Animation"
OrientationInterpolator490 = x3d.OrientationInterpolator()
OrientationInterpolator490.DEF = "r_ankle_RotationInterpolator_Jump"
OrientationInterpolator490.key = [0,0.28,0.32,0.36,0.4,0.44,0.48,0.64,0.76,0.84,0.88,0.92,0.96,1]

Group489.children.append(OrientationInterpolator490)
OrientationInterpolator491 = x3d.OrientationInterpolator()
OrientationInterpolator491.DEF = "r_knee_RotationInterpolator_Jump"
OrientationInterpolator491.key = [0,0.28,0.32,0.48,0.64,0.76,0.88,1]

Group489.children.append(OrientationInterpolator491)
OrientationInterpolator492 = x3d.OrientationInterpolator()
OrientationInterpolator492.DEF = "r_hip_RotationInterpolator_Jump"
OrientationInterpolator492.key = [0,0.28,0.32,0.36,0.4,0.44,0.48,0.64,0.76,0.88,1]

Group489.children.append(OrientationInterpolator492)
OrientationInterpolator493 = x3d.OrientationInterpolator()
OrientationInterpolator493.DEF = "l_ankle_RotationInterpolator_Jump"
OrientationInterpolator493.key = [0,0.28,0.32,0.36,0.4,0.44,0.48,0.64,0.76,0.84,0.88,0.92,0.96,1]

Group489.children.append(OrientationInterpolator493)
OrientationInterpolator494 = x3d.OrientationInterpolator()
OrientationInterpolator494.DEF = "l_knee_RotationInterpolator_Jump"
OrientationInterpolator494.key = [0,0.28,0.32,0.48,0.64,0.76,0.88,1]

Group489.children.append(OrientationInterpolator494)
OrientationInterpolator495 = x3d.OrientationInterpolator()
OrientationInterpolator495.DEF = "l_hip_RotationInterpolator_Jump"
OrientationInterpolator495.key = [0,0.28,0.32,0.36,0.4,0.44,0.48,0.64,0.76,0.88,1]

Group489.children.append(OrientationInterpolator495)
OrientationInterpolator496 = x3d.OrientationInterpolator()
OrientationInterpolator496.DEF = "lower_body_RotationInterpolator_Jump"
OrientationInterpolator496.key = [0,0.28,0.32,0.48,0.76,1]

Group489.children.append(OrientationInterpolator496)
OrientationInterpolator497 = x3d.OrientationInterpolator()
OrientationInterpolator497.DEF = "r_wrist_RotationInterpolator_Jump"
OrientationInterpolator497.key = [0,0.28,0.32,0.64,0.76,1]

Group489.children.append(OrientationInterpolator497)
OrientationInterpolator498 = x3d.OrientationInterpolator()
OrientationInterpolator498.DEF = "r_elbow_RotationInterpolator_Jump"
OrientationInterpolator498.key = [0,0.28,0.32,0.64,0.76,1]

Group489.children.append(OrientationInterpolator498)
OrientationInterpolator499 = x3d.OrientationInterpolator()
OrientationInterpolator499.DEF = "r_shoulder_RotationInterpolator_Jump"
OrientationInterpolator499.key = [0,0.28,0.32,0.64,0.76,0.88,1]

Group489.children.append(OrientationInterpolator499)
OrientationInterpolator500 = x3d.OrientationInterpolator()
OrientationInterpolator500.DEF = "l_wrist_RotationInterpolator_Jump"
OrientationInterpolator500.key = [0,0.28,0.32,0.64,0.76,0.88,1]

Group489.children.append(OrientationInterpolator500)
OrientationInterpolator501 = x3d.OrientationInterpolator()
OrientationInterpolator501.DEF = "l_elbow_RotationInterpolator_Jump"
OrientationInterpolator501.key = [0,0.28,0.32,0.64,0.76,1]

Group489.children.append(OrientationInterpolator501)
OrientationInterpolator502 = x3d.OrientationInterpolator()
OrientationInterpolator502.DEF = "l_shoulder_RotationInterpolator_Jump"
OrientationInterpolator502.key = [0,0.28,0.32,0.64,0.76,0.88,1]

Group489.children.append(OrientationInterpolator502)
OrientationInterpolator503 = x3d.OrientationInterpolator()
OrientationInterpolator503.DEF = "head_RotationInterpolator_Jump"
OrientationInterpolator503.key = [0,0.28,0.32,0.48,0.76,1]

Group489.children.append(OrientationInterpolator503)
OrientationInterpolator504 = x3d.OrientationInterpolator()
OrientationInterpolator504.DEF = "neck_RotationInterpolator_Jump"
OrientationInterpolator504.key = [0,0.28,0.32,0.48,0.76,1]

Group489.children.append(OrientationInterpolator504)
OrientationInterpolator505 = x3d.OrientationInterpolator()
OrientationInterpolator505.DEF = "upper_body_RotationInterpolator_Jump"
OrientationInterpolator505.key = [0,0.28,0.32,0.48,0.76,0.88,1]

Group489.children.append(OrientationInterpolator505)
OrientationInterpolator506 = x3d.OrientationInterpolator()
OrientationInterpolator506.DEF = "whole_body_RotationInterpolator_Jump"
OrientationInterpolator506.key = [0,0.28,0.32,0.48,0.64,0.76,1]

Group489.children.append(OrientationInterpolator506)
PositionInterpolator507 = x3d.PositionInterpolator()
PositionInterpolator507.DEF = "whole_body_TranslationInterpolator_Jump"
PositionInterpolator507.key = [0,0.04,0.08,0.12,0.16,0.2,0.24,0.28,0.32,0.36,0.4,0.44,0.48,0.64,0.76,0.8,0.84,0.88,0.92,0.96,1]

Group489.children.append(PositionInterpolator507)
TimeSensor508 = x3d.TimeSensor()
TimeSensor508.DEF = "Jump_Time"
TimeSensor508.cycleInterval = 2
TimeSensor508.startTime = -1

Group489.children.append(TimeSensor508)

Group428.children.append(Group489)

Scene17.children.append(Group428)
ROUTE509 = x3d.ROUTE()
ROUTE509.fromField = "position_changed"
ROUTE509.fromNode = "HudProx"
ROUTE509.toField = "set_translation"
ROUTE509.toNode = "HudXform"

Scene17.children.append(ROUTE509)
ROUTE510 = x3d.ROUTE()
ROUTE510.fromField = "orientation_changed"
ROUTE510.fromNode = "HudProx"
ROUTE510.toField = "set_rotation"
ROUTE510.toNode = "HudXform"

Scene17.children.append(ROUTE510)
ROUTE511 = x3d.ROUTE()
ROUTE511.fromField = "touchTime"
ROUTE511.fromNode = "Stand_Touch"
ROUTE511.toField = "stopTime"
ROUTE511.toNode = "Walk_Time"

Scene17.children.append(ROUTE511)
ROUTE512 = x3d.ROUTE()
ROUTE512.fromField = "touchTime"
ROUTE512.fromNode = "Stand_Touch"
ROUTE512.toField = "stopTime"
ROUTE512.toNode = "Run_Time"

Scene17.children.append(ROUTE512)
ROUTE513 = x3d.ROUTE()
ROUTE513.fromField = "touchTime"
ROUTE513.fromNode = "Stand_Touch"
ROUTE513.toField = "stopTime"
ROUTE513.toNode = "Jump_Time"

Scene17.children.append(ROUTE513)
ROUTE514 = x3d.ROUTE()
ROUTE514.fromField = "touchTime"
ROUTE514.fromNode = "Stand_Touch"
ROUTE514.toField = "startTime"
ROUTE514.toNode = "Stand_Time"

Scene17.children.append(ROUTE514)
ROUTE515 = x3d.ROUTE()
ROUTE515.fromField = "touchTime"
ROUTE515.fromNode = "Walk_Touch"
ROUTE515.toField = "stopTime"
ROUTE515.toNode = "Stand_Time"

Scene17.children.append(ROUTE515)
ROUTE516 = x3d.ROUTE()
ROUTE516.fromField = "touchTime"
ROUTE516.fromNode = "Walk_Touch"
ROUTE516.toField = "stopTime"
ROUTE516.toNode = "Run_Time"

Scene17.children.append(ROUTE516)
ROUTE517 = x3d.ROUTE()
ROUTE517.fromField = "touchTime"
ROUTE517.fromNode = "Walk_Touch"
ROUTE517.toField = "stopTime"
ROUTE517.toNode = "Jump_Time"

Scene17.children.append(ROUTE517)
ROUTE518 = x3d.ROUTE()
ROUTE518.fromField = "touchTime"
ROUTE518.fromNode = "Walk_Touch"
ROUTE518.toField = "startTime"
ROUTE518.toNode = "Walk_Time"

Scene17.children.append(ROUTE518)
ROUTE519 = x3d.ROUTE()
ROUTE519.fromField = "touchTime"
ROUTE519.fromNode = "Run_Touch"
ROUTE519.toField = "stopTime"
ROUTE519.toNode = "Stand_Time"

Scene17.children.append(ROUTE519)
ROUTE520 = x3d.ROUTE()
ROUTE520.fromField = "touchTime"
ROUTE520.fromNode = "Run_Touch"
ROUTE520.toField = "stopTime"
ROUTE520.toNode = "Walk_Time"

Scene17.children.append(ROUTE520)
ROUTE521 = x3d.ROUTE()
ROUTE521.fromField = "touchTime"
ROUTE521.fromNode = "Run_Touch"
ROUTE521.toField = "stopTime"
ROUTE521.toNode = "Jump_Time"

Scene17.children.append(ROUTE521)
ROUTE522 = x3d.ROUTE()
ROUTE522.fromField = "touchTime"
ROUTE522.fromNode = "Run_Touch"
ROUTE522.toField = "startTime"
ROUTE522.toNode = "Run_Time"

Scene17.children.append(ROUTE522)
ROUTE523 = x3d.ROUTE()
ROUTE523.fromField = "touchTime"
ROUTE523.fromNode = "Jump_Touch"
ROUTE523.toField = "stopTime"
ROUTE523.toNode = "Stand_Time"

Scene17.children.append(ROUTE523)
ROUTE524 = x3d.ROUTE()
ROUTE524.fromField = "touchTime"
ROUTE524.fromNode = "Jump_Touch"
ROUTE524.toField = "stopTime"
ROUTE524.toNode = "Walk_Time"

Scene17.children.append(ROUTE524)
ROUTE525 = x3d.ROUTE()
ROUTE525.fromField = "touchTime"
ROUTE525.fromNode = "Jump_Touch"
ROUTE525.toField = "stopTime"
ROUTE525.toNode = "Run_Time"

Scene17.children.append(ROUTE525)
ROUTE526 = x3d.ROUTE()
ROUTE526.fromField = "touchTime"
ROUTE526.fromNode = "Jump_Touch"
ROUTE526.toField = "startTime"
ROUTE526.toNode = "Jump_Time"

Scene17.children.append(ROUTE526)
ROUTE527 = x3d.ROUTE()
ROUTE527.fromField = "fraction_changed"
ROUTE527.fromNode = "Stand_Time"
ROUTE527.toField = "set_fraction"
ROUTE527.toNode = "r_ankle_RotationInterpolator_Stand"

Scene17.children.append(ROUTE527)
ROUTE528 = x3d.ROUTE()
ROUTE528.fromField = "fraction_changed"
ROUTE528.fromNode = "Stand_Time"
ROUTE528.toField = "set_fraction"
ROUTE528.toNode = "r_knee_RotationInterpolator_Stand"

Scene17.children.append(ROUTE528)
ROUTE529 = x3d.ROUTE()
ROUTE529.fromField = "fraction_changed"
ROUTE529.fromNode = "Stand_Time"
ROUTE529.toField = "set_fraction"
ROUTE529.toNode = "r_hip_RotationInterpolator_Stand"

Scene17.children.append(ROUTE529)
ROUTE530 = x3d.ROUTE()
ROUTE530.fromField = "fraction_changed"
ROUTE530.fromNode = "Stand_Time"
ROUTE530.toField = "set_fraction"
ROUTE530.toNode = "l_ankle_RotationInterpolator_Stand"

Scene17.children.append(ROUTE530)
ROUTE531 = x3d.ROUTE()
ROUTE531.fromField = "fraction_changed"
ROUTE531.fromNode = "Stand_Time"
ROUTE531.toField = "set_fraction"
ROUTE531.toNode = "l_knee_RotationInterpolator_Stand"

Scene17.children.append(ROUTE531)
ROUTE532 = x3d.ROUTE()
ROUTE532.fromField = "fraction_changed"
ROUTE532.fromNode = "Stand_Time"
ROUTE532.toField = "set_fraction"
ROUTE532.toNode = "l_hip_RotationInterpolator_Stand"

Scene17.children.append(ROUTE532)
ROUTE533 = x3d.ROUTE()
ROUTE533.fromField = "fraction_changed"
ROUTE533.fromNode = "Stand_Time"
ROUTE533.toField = "set_fraction"
ROUTE533.toNode = "lower_body_RotationInterpolator_Stand"

Scene17.children.append(ROUTE533)
ROUTE534 = x3d.ROUTE()
ROUTE534.fromField = "fraction_changed"
ROUTE534.fromNode = "Stand_Time"
ROUTE534.toField = "set_fraction"
ROUTE534.toNode = "r_wrist_RotationInterpolator_Stand"

Scene17.children.append(ROUTE534)
ROUTE535 = x3d.ROUTE()
ROUTE535.fromField = "fraction_changed"
ROUTE535.fromNode = "Stand_Time"
ROUTE535.toField = "set_fraction"
ROUTE535.toNode = "r_elbow_RotationInterpolator_Stand"

Scene17.children.append(ROUTE535)
ROUTE536 = x3d.ROUTE()
ROUTE536.fromField = "fraction_changed"
ROUTE536.fromNode = "Stand_Time"
ROUTE536.toField = "set_fraction"
ROUTE536.toNode = "r_shoulder_RotationInterpolator_Stand"

Scene17.children.append(ROUTE536)
ROUTE537 = x3d.ROUTE()
ROUTE537.fromField = "fraction_changed"
ROUTE537.fromNode = "Stand_Time"
ROUTE537.toField = "set_fraction"
ROUTE537.toNode = "l_wrist_RotationInterpolator_Stand"

Scene17.children.append(ROUTE537)
ROUTE538 = x3d.ROUTE()
ROUTE538.fromField = "fraction_changed"
ROUTE538.fromNode = "Stand_Time"
ROUTE538.toField = "set_fraction"
ROUTE538.toNode = "l_elbow_RotationInterpolator_Stand"

Scene17.children.append(ROUTE538)
ROUTE539 = x3d.ROUTE()
ROUTE539.fromField = "fraction_changed"
ROUTE539.fromNode = "Stand_Time"
ROUTE539.toField = "set_fraction"
ROUTE539.toNode = "l_shoulder_RotationInterpolator_Stand"

Scene17.children.append(ROUTE539)
ROUTE540 = x3d.ROUTE()
ROUTE540.fromField = "fraction_changed"
ROUTE540.fromNode = "Stand_Time"
ROUTE540.toField = "set_fraction"
ROUTE540.toNode = "head_RotationInterpolator_Stand"

Scene17.children.append(ROUTE540)
ROUTE541 = x3d.ROUTE()
ROUTE541.fromField = "fraction_changed"
ROUTE541.fromNode = "Stand_Time"
ROUTE541.toField = "set_fraction"
ROUTE541.toNode = "neck_RotationInterpolator_Stand"

Scene17.children.append(ROUTE541)
ROUTE542 = x3d.ROUTE()
ROUTE542.fromField = "fraction_changed"
ROUTE542.fromNode = "Stand_Time"
ROUTE542.toField = "set_fraction"
ROUTE542.toNode = "upper_body_RotationInterpolator_Stand"

Scene17.children.append(ROUTE542)
ROUTE543 = x3d.ROUTE()
ROUTE543.fromField = "fraction_changed"
ROUTE543.fromNode = "Stand_Time"
ROUTE543.toField = "set_fraction"
ROUTE543.toNode = "whole_body_RotationInterpolator_Stand"

Scene17.children.append(ROUTE543)
ROUTE544 = x3d.ROUTE()
ROUTE544.fromField = "fraction_changed"
ROUTE544.fromNode = "Stand_Time"
ROUTE544.toField = "set_fraction"
ROUTE544.toNode = "whole_body_TranslationInterpolator_Stand"

Scene17.children.append(ROUTE544)
ROUTE545 = x3d.ROUTE()
ROUTE545.fromField = "value_changed"
ROUTE545.fromNode = "r_ankle_RotationInterpolator_Stand"
ROUTE545.toField = "set_rotation"
ROUTE545.toNode = "hanim_r_ankle"

Scene17.children.append(ROUTE545)
ROUTE546 = x3d.ROUTE()
ROUTE546.fromField = "value_changed"
ROUTE546.fromNode = "r_knee_RotationInterpolator_Stand"
ROUTE546.toField = "set_rotation"
ROUTE546.toNode = "hanim_r_knee"

Scene17.children.append(ROUTE546)
ROUTE547 = x3d.ROUTE()
ROUTE547.fromField = "value_changed"
ROUTE547.fromNode = "r_hip_RotationInterpolator_Stand"
ROUTE547.toField = "set_rotation"
ROUTE547.toNode = "hanim_r_hip"

Scene17.children.append(ROUTE547)
ROUTE548 = x3d.ROUTE()
ROUTE548.fromField = "value_changed"
ROUTE548.fromNode = "l_ankle_RotationInterpolator_Stand"
ROUTE548.toField = "set_rotation"
ROUTE548.toNode = "hanim_l_ankle"

Scene17.children.append(ROUTE548)
ROUTE549 = x3d.ROUTE()
ROUTE549.fromField = "value_changed"
ROUTE549.fromNode = "l_knee_RotationInterpolator_Stand"
ROUTE549.toField = "set_rotation"
ROUTE549.toNode = "hanim_l_knee"

Scene17.children.append(ROUTE549)
ROUTE550 = x3d.ROUTE()
ROUTE550.fromField = "value_changed"
ROUTE550.fromNode = "l_hip_RotationInterpolator_Stand"
ROUTE550.toField = "set_rotation"
ROUTE550.toNode = "hanim_l_hip"

Scene17.children.append(ROUTE550)
ROUTE551 = x3d.ROUTE()
ROUTE551.fromField = "value_changed"
ROUTE551.fromNode = "lower_body_RotationInterpolator_Stand"
ROUTE551.toField = "set_rotation"
ROUTE551.toNode = "hanim_sacroiliac"

Scene17.children.append(ROUTE551)
ROUTE552 = x3d.ROUTE()
ROUTE552.fromField = "value_changed"
ROUTE552.fromNode = "r_wrist_RotationInterpolator_Stand"
ROUTE552.toField = "set_rotation"
ROUTE552.toNode = "hanim_r_wrist"

Scene17.children.append(ROUTE552)
ROUTE553 = x3d.ROUTE()
ROUTE553.fromField = "value_changed"
ROUTE553.fromNode = "r_elbow_RotationInterpolator_Stand"
ROUTE553.toField = "set_rotation"
ROUTE553.toNode = "hanim_r_elbow"

Scene17.children.append(ROUTE553)
ROUTE554 = x3d.ROUTE()
ROUTE554.fromField = "value_changed"
ROUTE554.fromNode = "r_shoulder_RotationInterpolator_Stand"
ROUTE554.toField = "set_rotation"
ROUTE554.toNode = "hanim_r_shoulder"

Scene17.children.append(ROUTE554)
ROUTE555 = x3d.ROUTE()
ROUTE555.fromField = "value_changed"
ROUTE555.fromNode = "l_wrist_RotationInterpolator_Stand"
ROUTE555.toField = "set_rotation"
ROUTE555.toNode = "hanim_l_wrist"

Scene17.children.append(ROUTE555)
ROUTE556 = x3d.ROUTE()
ROUTE556.fromField = "value_changed"
ROUTE556.fromNode = "l_elbow_RotationInterpolator_Stand"
ROUTE556.toField = "set_rotation"
ROUTE556.toNode = "hanim_l_elbow"

Scene17.children.append(ROUTE556)
ROUTE557 = x3d.ROUTE()
ROUTE557.fromField = "value_changed"
ROUTE557.fromNode = "l_shoulder_RotationInterpolator_Stand"
ROUTE557.toField = "set_rotation"
ROUTE557.toNode = "hanim_l_shoulder"

Scene17.children.append(ROUTE557)
ROUTE558 = x3d.ROUTE()
ROUTE558.fromField = "value_changed"
ROUTE558.fromNode = "head_RotationInterpolator_Stand"
ROUTE558.toField = "set_rotation"
ROUTE558.toNode = "hanim_skullbase"

Scene17.children.append(ROUTE558)
ROUTE559 = x3d.ROUTE()
ROUTE559.fromField = "value_changed"
ROUTE559.fromNode = "neck_RotationInterpolator_Stand"
ROUTE559.toField = "set_rotation"
ROUTE559.toNode = "hanim_vc4"

Scene17.children.append(ROUTE559)
ROUTE560 = x3d.ROUTE()
ROUTE560.fromField = "value_changed"
ROUTE560.fromNode = "upper_body_RotationInterpolator_Stand"
ROUTE560.toField = "set_rotation"
ROUTE560.toNode = "hanim_vl1"

Scene17.children.append(ROUTE560)
ROUTE561 = x3d.ROUTE()
ROUTE561.fromField = "value_changed"
ROUTE561.fromNode = "whole_body_RotationInterpolator_Stand"
ROUTE561.toField = "set_rotation"
ROUTE561.toNode = "hanim_humanoid_root"

Scene17.children.append(ROUTE561)
ROUTE562 = x3d.ROUTE()
ROUTE562.fromField = "value_changed"
ROUTE562.fromNode = "whole_body_TranslationInterpolator_Stand"
ROUTE562.toField = "set_translation"
ROUTE562.toNode = "hanim_humanoid_root"

Scene17.children.append(ROUTE562)
ROUTE563 = x3d.ROUTE()
ROUTE563.fromField = "fraction_changed"
ROUTE563.fromNode = "Walk_Time"
ROUTE563.toField = "set_fraction"
ROUTE563.toNode = "r_ankle_RotationInterpolator_BasicWalk"

Scene17.children.append(ROUTE563)
ROUTE564 = x3d.ROUTE()
ROUTE564.fromField = "fraction_changed"
ROUTE564.fromNode = "Walk_Time"
ROUTE564.toField = "set_fraction"
ROUTE564.toNode = "r_knee_RotationInterpolator_BasicWalk"

Scene17.children.append(ROUTE564)
ROUTE565 = x3d.ROUTE()
ROUTE565.fromField = "fraction_changed"
ROUTE565.fromNode = "Walk_Time"
ROUTE565.toField = "set_fraction"
ROUTE565.toNode = "r_hip_RotationInterpolator_BasicWalk"

Scene17.children.append(ROUTE565)
ROUTE566 = x3d.ROUTE()
ROUTE566.fromField = "fraction_changed"
ROUTE566.fromNode = "Walk_Time"
ROUTE566.toField = "set_fraction"
ROUTE566.toNode = "l_ankle_RotationInterpolator_BasicWalk"

Scene17.children.append(ROUTE566)
ROUTE567 = x3d.ROUTE()
ROUTE567.fromField = "fraction_changed"
ROUTE567.fromNode = "Walk_Time"
ROUTE567.toField = "set_fraction"
ROUTE567.toNode = "l_knee_RotationInterpolator_BasicWalk"

Scene17.children.append(ROUTE567)
ROUTE568 = x3d.ROUTE()
ROUTE568.fromField = "fraction_changed"
ROUTE568.fromNode = "Walk_Time"
ROUTE568.toField = "set_fraction"
ROUTE568.toNode = "l_hip_RotationInterpolator_BasicWalk"

Scene17.children.append(ROUTE568)
ROUTE569 = x3d.ROUTE()
ROUTE569.fromField = "fraction_changed"
ROUTE569.fromNode = "Walk_Time"
ROUTE569.toField = "set_fraction"
ROUTE569.toNode = "lower_body_RotationInterpolator_BasicWalk"

Scene17.children.append(ROUTE569)
ROUTE570 = x3d.ROUTE()
ROUTE570.fromField = "fraction_changed"
ROUTE570.fromNode = "Walk_Time"
ROUTE570.toField = "set_fraction"
ROUTE570.toNode = "r_wrist_RotationInterpolator_BasicWalk"

Scene17.children.append(ROUTE570)
ROUTE571 = x3d.ROUTE()
ROUTE571.fromField = "fraction_changed"
ROUTE571.fromNode = "Walk_Time"
ROUTE571.toField = "set_fraction"
ROUTE571.toNode = "r_elbow_RotationInterpolator_BasicWalk"

Scene17.children.append(ROUTE571)
ROUTE572 = x3d.ROUTE()
ROUTE572.fromField = "fraction_changed"
ROUTE572.fromNode = "Walk_Time"
ROUTE572.toField = "set_fraction"
ROUTE572.toNode = "r_shoulder_RotationInterpolator_BasicWalk"

Scene17.children.append(ROUTE572)
ROUTE573 = x3d.ROUTE()
ROUTE573.fromField = "fraction_changed"
ROUTE573.fromNode = "Walk_Time"
ROUTE573.toField = "set_fraction"
ROUTE573.toNode = "l_wrist_RotationInterpolator_BasicWalk"

Scene17.children.append(ROUTE573)
ROUTE574 = x3d.ROUTE()
ROUTE574.fromField = "fraction_changed"
ROUTE574.fromNode = "Walk_Time"
ROUTE574.toField = "set_fraction"
ROUTE574.toNode = "l_elbow_RotationInterpolator_BasicWalk"

Scene17.children.append(ROUTE574)
ROUTE575 = x3d.ROUTE()
ROUTE575.fromField = "fraction_changed"
ROUTE575.fromNode = "Walk_Time"
ROUTE575.toField = "set_fraction"
ROUTE575.toNode = "l_shoulder_RotationInterpolator_BasicWalk"

Scene17.children.append(ROUTE575)
ROUTE576 = x3d.ROUTE()
ROUTE576.fromField = "fraction_changed"
ROUTE576.fromNode = "Walk_Time"
ROUTE576.toField = "set_fraction"
ROUTE576.toNode = "head_RotationInterpolator_BasicWalk"

Scene17.children.append(ROUTE576)
ROUTE577 = x3d.ROUTE()
ROUTE577.fromField = "fraction_changed"
ROUTE577.fromNode = "Walk_Time"
ROUTE577.toField = "set_fraction"
ROUTE577.toNode = "neck_RotationInterpolator_BasicWalk"

Scene17.children.append(ROUTE577)
ROUTE578 = x3d.ROUTE()
ROUTE578.fromField = "fraction_changed"
ROUTE578.fromNode = "Walk_Time"
ROUTE578.toField = "set_fraction"
ROUTE578.toNode = "upper_body_RotationInterpolator_BasicWalk"

Scene17.children.append(ROUTE578)
ROUTE579 = x3d.ROUTE()
ROUTE579.fromField = "fraction_changed"
ROUTE579.fromNode = "Walk_Time"
ROUTE579.toField = "set_fraction"
ROUTE579.toNode = "whole_body_RotationInterpolator_BasicWalk"

Scene17.children.append(ROUTE579)
ROUTE580 = x3d.ROUTE()
ROUTE580.fromField = "fraction_changed"
ROUTE580.fromNode = "Walk_Time"
ROUTE580.toField = "set_fraction"
ROUTE580.toNode = "whole_body_TranslationInterpolator_BasicWalk"

Scene17.children.append(ROUTE580)
ROUTE581 = x3d.ROUTE()
ROUTE581.fromField = "value_changed"
ROUTE581.fromNode = "r_ankle_RotationInterpolator_BasicWalk"
ROUTE581.toField = "set_rotation"
ROUTE581.toNode = "hanim_r_ankle"

Scene17.children.append(ROUTE581)
ROUTE582 = x3d.ROUTE()
ROUTE582.fromField = "value_changed"
ROUTE582.fromNode = "r_knee_RotationInterpolator_BasicWalk"
ROUTE582.toField = "set_rotation"
ROUTE582.toNode = "hanim_r_knee"

Scene17.children.append(ROUTE582)
ROUTE583 = x3d.ROUTE()
ROUTE583.fromField = "value_changed"
ROUTE583.fromNode = "r_hip_RotationInterpolator_BasicWalk"
ROUTE583.toField = "set_rotation"
ROUTE583.toNode = "hanim_r_hip"

Scene17.children.append(ROUTE583)
ROUTE584 = x3d.ROUTE()
ROUTE584.fromField = "value_changed"
ROUTE584.fromNode = "l_ankle_RotationInterpolator_BasicWalk"
ROUTE584.toField = "set_rotation"
ROUTE584.toNode = "hanim_l_ankle"

Scene17.children.append(ROUTE584)
ROUTE585 = x3d.ROUTE()
ROUTE585.fromField = "value_changed"
ROUTE585.fromNode = "l_knee_RotationInterpolator_BasicWalk"
ROUTE585.toField = "set_rotation"
ROUTE585.toNode = "hanim_l_knee"

Scene17.children.append(ROUTE585)
ROUTE586 = x3d.ROUTE()
ROUTE586.fromField = "value_changed"
ROUTE586.fromNode = "l_hip_RotationInterpolator_BasicWalk"
ROUTE586.toField = "set_rotation"
ROUTE586.toNode = "hanim_l_hip"

Scene17.children.append(ROUTE586)
ROUTE587 = x3d.ROUTE()
ROUTE587.fromField = "value_changed"
ROUTE587.fromNode = "lower_body_RotationInterpolator_BasicWalk"
ROUTE587.toField = "set_rotation"
ROUTE587.toNode = "hanim_sacroiliac"

Scene17.children.append(ROUTE587)
ROUTE588 = x3d.ROUTE()
ROUTE588.fromField = "value_changed"
ROUTE588.fromNode = "r_wrist_RotationInterpolator_BasicWalk"
ROUTE588.toField = "set_rotation"
ROUTE588.toNode = "hanim_r_wrist"

Scene17.children.append(ROUTE588)
ROUTE589 = x3d.ROUTE()
ROUTE589.fromField = "value_changed"
ROUTE589.fromNode = "r_elbow_RotationInterpolator_BasicWalk"
ROUTE589.toField = "set_rotation"
ROUTE589.toNode = "hanim_r_elbow"

Scene17.children.append(ROUTE589)
ROUTE590 = x3d.ROUTE()
ROUTE590.fromField = "value_changed"
ROUTE590.fromNode = "r_shoulder_RotationInterpolator_BasicWalk"
ROUTE590.toField = "set_rotation"
ROUTE590.toNode = "hanim_r_shoulder"

Scene17.children.append(ROUTE590)
ROUTE591 = x3d.ROUTE()
ROUTE591.fromField = "value_changed"
ROUTE591.fromNode = "l_wrist_RotationInterpolator_BasicWalk"
ROUTE591.toField = "set_rotation"
ROUTE591.toNode = "hanim_l_wrist"

Scene17.children.append(ROUTE591)
ROUTE592 = x3d.ROUTE()
ROUTE592.fromField = "value_changed"
ROUTE592.fromNode = "l_elbow_RotationInterpolator_BasicWalk"
ROUTE592.toField = "set_rotation"
ROUTE592.toNode = "hanim_l_elbow"

Scene17.children.append(ROUTE592)
ROUTE593 = x3d.ROUTE()
ROUTE593.fromField = "value_changed"
ROUTE593.fromNode = "l_shoulder_RotationInterpolator_BasicWalk"
ROUTE593.toField = "set_rotation"
ROUTE593.toNode = "hanim_l_shoulder"

Scene17.children.append(ROUTE593)
ROUTE594 = x3d.ROUTE()
ROUTE594.fromField = "value_changed"
ROUTE594.fromNode = "head_RotationInterpolator_BasicWalk"
ROUTE594.toField = "set_rotation"
ROUTE594.toNode = "hanim_skullbase"

Scene17.children.append(ROUTE594)
ROUTE595 = x3d.ROUTE()
ROUTE595.fromField = "value_changed"
ROUTE595.fromNode = "neck_RotationInterpolator_BasicWalk"
ROUTE595.toField = "set_rotation"
ROUTE595.toNode = "hanim_vc4"

Scene17.children.append(ROUTE595)
ROUTE596 = x3d.ROUTE()
ROUTE596.fromField = "value_changed"
ROUTE596.fromNode = "upper_body_RotationInterpolator_BasicWalk"
ROUTE596.toField = "set_rotation"
ROUTE596.toNode = "hanim_vl1"

Scene17.children.append(ROUTE596)
ROUTE597 = x3d.ROUTE()
ROUTE597.fromField = "value_changed"
ROUTE597.fromNode = "whole_body_RotationInterpolator_BasicWalk"
ROUTE597.toField = "set_rotation"
ROUTE597.toNode = "hanim_humanoid_root"

Scene17.children.append(ROUTE597)
ROUTE598 = x3d.ROUTE()
ROUTE598.fromField = "value_changed"
ROUTE598.fromNode = "whole_body_TranslationInterpolator_BasicWalk"
ROUTE598.toField = "set_translation"
ROUTE598.toNode = "hanim_humanoid_root"

Scene17.children.append(ROUTE598)
ROUTE599 = x3d.ROUTE()
ROUTE599.fromField = "fraction_changed"
ROUTE599.fromNode = "Run_Time"
ROUTE599.toField = "set_fraction"
ROUTE599.toNode = "r_ankle_RotationInterpolator_Run"

Scene17.children.append(ROUTE599)
ROUTE600 = x3d.ROUTE()
ROUTE600.fromField = "fraction_changed"
ROUTE600.fromNode = "Run_Time"
ROUTE600.toField = "set_fraction"
ROUTE600.toNode = "r_knee_RotationInterpolator_Run"

Scene17.children.append(ROUTE600)
ROUTE601 = x3d.ROUTE()
ROUTE601.fromField = "fraction_changed"
ROUTE601.fromNode = "Run_Time"
ROUTE601.toField = "set_fraction"
ROUTE601.toNode = "r_hip_RotationInterpolator_Run"

Scene17.children.append(ROUTE601)
ROUTE602 = x3d.ROUTE()
ROUTE602.fromField = "fraction_changed"
ROUTE602.fromNode = "Run_Time"
ROUTE602.toField = "set_fraction"
ROUTE602.toNode = "l_ankle_RotationInterpolator_Run"

Scene17.children.append(ROUTE602)
ROUTE603 = x3d.ROUTE()
ROUTE603.fromField = "fraction_changed"
ROUTE603.fromNode = "Run_Time"
ROUTE603.toField = "set_fraction"
ROUTE603.toNode = "l_knee_RotationInterpolator_Run"

Scene17.children.append(ROUTE603)
ROUTE604 = x3d.ROUTE()
ROUTE604.fromField = "fraction_changed"
ROUTE604.fromNode = "Run_Time"
ROUTE604.toField = "set_fraction"
ROUTE604.toNode = "l_hip_RotationInterpolator_Run"

Scene17.children.append(ROUTE604)
ROUTE605 = x3d.ROUTE()
ROUTE605.fromField = "fraction_changed"
ROUTE605.fromNode = "Run_Time"
ROUTE605.toField = "set_fraction"
ROUTE605.toNode = "lower_body_RotationInterpolator_Run"

Scene17.children.append(ROUTE605)
ROUTE606 = x3d.ROUTE()
ROUTE606.fromField = "fraction_changed"
ROUTE606.fromNode = "Run_Time"
ROUTE606.toField = "set_fraction"
ROUTE606.toNode = "r_wrist_RotationInterpolator_Run"

Scene17.children.append(ROUTE606)
ROUTE607 = x3d.ROUTE()
ROUTE607.fromField = "fraction_changed"
ROUTE607.fromNode = "Run_Time"
ROUTE607.toField = "set_fraction"
ROUTE607.toNode = "r_elbow_RotationInterpolator_Run"

Scene17.children.append(ROUTE607)
ROUTE608 = x3d.ROUTE()
ROUTE608.fromField = "fraction_changed"
ROUTE608.fromNode = "Run_Time"
ROUTE608.toField = "set_fraction"
ROUTE608.toNode = "r_shoulder_RotationInterpolator_Run"

Scene17.children.append(ROUTE608)
ROUTE609 = x3d.ROUTE()
ROUTE609.fromField = "fraction_changed"
ROUTE609.fromNode = "Run_Time"
ROUTE609.toField = "set_fraction"
ROUTE609.toNode = "l_wrist_RotationInterpolator_Run"

Scene17.children.append(ROUTE609)
ROUTE610 = x3d.ROUTE()
ROUTE610.fromField = "fraction_changed"
ROUTE610.fromNode = "Run_Time"
ROUTE610.toField = "set_fraction"
ROUTE610.toNode = "l_elbow_RotationInterpolator_Run"

Scene17.children.append(ROUTE610)
ROUTE611 = x3d.ROUTE()
ROUTE611.fromField = "fraction_changed"
ROUTE611.fromNode = "Run_Time"
ROUTE611.toField = "set_fraction"
ROUTE611.toNode = "l_shoulder_RotationInterpolator_Run"

Scene17.children.append(ROUTE611)
ROUTE612 = x3d.ROUTE()
ROUTE612.fromField = "fraction_changed"
ROUTE612.fromNode = "Run_Time"
ROUTE612.toField = "set_fraction"
ROUTE612.toNode = "head_RotationInterpolator_Run"

Scene17.children.append(ROUTE612)
ROUTE613 = x3d.ROUTE()
ROUTE613.fromField = "fraction_changed"
ROUTE613.fromNode = "Run_Time"
ROUTE613.toField = "set_fraction"
ROUTE613.toNode = "neck_RotationInterpolator_Run"

Scene17.children.append(ROUTE613)
ROUTE614 = x3d.ROUTE()
ROUTE614.fromField = "fraction_changed"
ROUTE614.fromNode = "Run_Time"
ROUTE614.toField = "set_fraction"
ROUTE614.toNode = "upper_body_RotationInterpolator_Run"

Scene17.children.append(ROUTE614)
ROUTE615 = x3d.ROUTE()
ROUTE615.fromField = "fraction_changed"
ROUTE615.fromNode = "Run_Time"
ROUTE615.toField = "set_fraction"
ROUTE615.toNode = "whole_body_RotationInterpolator_Run"

Scene17.children.append(ROUTE615)
ROUTE616 = x3d.ROUTE()
ROUTE616.fromField = "fraction_changed"
ROUTE616.fromNode = "Run_Time"
ROUTE616.toField = "set_fraction"
ROUTE616.toNode = "whole_body_TranslationInterpolator_Run"

Scene17.children.append(ROUTE616)
ROUTE617 = x3d.ROUTE()
ROUTE617.fromField = "value_changed"
ROUTE617.fromNode = "r_ankle_RotationInterpolator_Run"
ROUTE617.toField = "set_rotation"
ROUTE617.toNode = "hanim_r_ankle"

Scene17.children.append(ROUTE617)
ROUTE618 = x3d.ROUTE()
ROUTE618.fromField = "value_changed"
ROUTE618.fromNode = "r_knee_RotationInterpolator_Run"
ROUTE618.toField = "set_rotation"
ROUTE618.toNode = "hanim_r_knee"

Scene17.children.append(ROUTE618)
ROUTE619 = x3d.ROUTE()
ROUTE619.fromField = "value_changed"
ROUTE619.fromNode = "r_hip_RotationInterpolator_Run"
ROUTE619.toField = "set_rotation"
ROUTE619.toNode = "hanim_r_hip"

Scene17.children.append(ROUTE619)
ROUTE620 = x3d.ROUTE()
ROUTE620.fromField = "value_changed"
ROUTE620.fromNode = "l_ankle_RotationInterpolator_Run"
ROUTE620.toField = "set_rotation"
ROUTE620.toNode = "hanim_l_ankle"

Scene17.children.append(ROUTE620)
ROUTE621 = x3d.ROUTE()
ROUTE621.fromField = "value_changed"
ROUTE621.fromNode = "l_knee_RotationInterpolator_Run"
ROUTE621.toField = "set_rotation"
ROUTE621.toNode = "hanim_l_knee"

Scene17.children.append(ROUTE621)
ROUTE622 = x3d.ROUTE()
ROUTE622.fromField = "value_changed"
ROUTE622.fromNode = "l_hip_RotationInterpolator_Run"
ROUTE622.toField = "set_rotation"
ROUTE622.toNode = "hanim_l_hip"

Scene17.children.append(ROUTE622)
ROUTE623 = x3d.ROUTE()
ROUTE623.fromField = "value_changed"
ROUTE623.fromNode = "lower_body_RotationInterpolator_Run"
ROUTE623.toField = "set_rotation"
ROUTE623.toNode = "hanim_sacroiliac"

Scene17.children.append(ROUTE623)
ROUTE624 = x3d.ROUTE()
ROUTE624.fromField = "value_changed"
ROUTE624.fromNode = "r_wrist_RotationInterpolator_Run"
ROUTE624.toField = "set_rotation"
ROUTE624.toNode = "hanim_r_wrist"

Scene17.children.append(ROUTE624)
ROUTE625 = x3d.ROUTE()
ROUTE625.fromField = "value_changed"
ROUTE625.fromNode = "r_elbow_RotationInterpolator_Run"
ROUTE625.toField = "set_rotation"
ROUTE625.toNode = "hanim_r_elbow"

Scene17.children.append(ROUTE625)
ROUTE626 = x3d.ROUTE()
ROUTE626.fromField = "value_changed"
ROUTE626.fromNode = "r_shoulder_RotationInterpolator_Run"
ROUTE626.toField = "set_rotation"
ROUTE626.toNode = "hanim_r_shoulder"

Scene17.children.append(ROUTE626)
ROUTE627 = x3d.ROUTE()
ROUTE627.fromField = "value_changed"
ROUTE627.fromNode = "l_wrist_RotationInterpolator_Run"
ROUTE627.toField = "set_rotation"
ROUTE627.toNode = "hanim_l_wrist"

Scene17.children.append(ROUTE627)
ROUTE628 = x3d.ROUTE()
ROUTE628.fromField = "value_changed"
ROUTE628.fromNode = "l_elbow_RotationInterpolator_Run"
ROUTE628.toField = "set_rotation"
ROUTE628.toNode = "hanim_l_elbow"

Scene17.children.append(ROUTE628)
ROUTE629 = x3d.ROUTE()
ROUTE629.fromField = "value_changed"
ROUTE629.fromNode = "l_shoulder_RotationInterpolator_Run"
ROUTE629.toField = "set_rotation"
ROUTE629.toNode = "hanim_l_shoulder"

Scene17.children.append(ROUTE629)
ROUTE630 = x3d.ROUTE()
ROUTE630.fromField = "value_changed"
ROUTE630.fromNode = "head_RotationInterpolator_Run"
ROUTE630.toField = "set_rotation"
ROUTE630.toNode = "hanim_skullbase"

Scene17.children.append(ROUTE630)
ROUTE631 = x3d.ROUTE()
ROUTE631.fromField = "value_changed"
ROUTE631.fromNode = "neck_RotationInterpolator_Run"
ROUTE631.toField = "set_rotation"
ROUTE631.toNode = "hanim_vc4"

Scene17.children.append(ROUTE631)
ROUTE632 = x3d.ROUTE()
ROUTE632.fromField = "value_changed"
ROUTE632.fromNode = "upper_body_RotationInterpolator_Run"
ROUTE632.toField = "set_rotation"
ROUTE632.toNode = "hanim_vl1"

Scene17.children.append(ROUTE632)
ROUTE633 = x3d.ROUTE()
ROUTE633.fromField = "value_changed"
ROUTE633.fromNode = "whole_body_RotationInterpolator_Run"
ROUTE633.toField = "set_rotation"
ROUTE633.toNode = "hanim_humanoid_root"

Scene17.children.append(ROUTE633)
ROUTE634 = x3d.ROUTE()
ROUTE634.fromField = "value_changed"
ROUTE634.fromNode = "whole_body_TranslationInterpolator_Run"
ROUTE634.toField = "set_translation"
ROUTE634.toNode = "hanim_humanoid_root"

Scene17.children.append(ROUTE634)
ROUTE635 = x3d.ROUTE()
ROUTE635.fromField = "fraction_changed"
ROUTE635.fromNode = "Jump_Time"
ROUTE635.toField = "set_fraction"
ROUTE635.toNode = "r_ankle_RotationInterpolator_Jump"

Scene17.children.append(ROUTE635)
ROUTE636 = x3d.ROUTE()
ROUTE636.fromField = "fraction_changed"
ROUTE636.fromNode = "Jump_Time"
ROUTE636.toField = "set_fraction"
ROUTE636.toNode = "r_knee_RotationInterpolator_Jump"

Scene17.children.append(ROUTE636)
ROUTE637 = x3d.ROUTE()
ROUTE637.fromField = "fraction_changed"
ROUTE637.fromNode = "Jump_Time"
ROUTE637.toField = "set_fraction"
ROUTE637.toNode = "r_hip_RotationInterpolator_Jump"

Scene17.children.append(ROUTE637)
ROUTE638 = x3d.ROUTE()
ROUTE638.fromField = "fraction_changed"
ROUTE638.fromNode = "Jump_Time"
ROUTE638.toField = "set_fraction"
ROUTE638.toNode = "l_ankle_RotationInterpolator_Jump"

Scene17.children.append(ROUTE638)
ROUTE639 = x3d.ROUTE()
ROUTE639.fromField = "fraction_changed"
ROUTE639.fromNode = "Jump_Time"
ROUTE639.toField = "set_fraction"
ROUTE639.toNode = "l_knee_RotationInterpolator_Jump"

Scene17.children.append(ROUTE639)
ROUTE640 = x3d.ROUTE()
ROUTE640.fromField = "fraction_changed"
ROUTE640.fromNode = "Jump_Time"
ROUTE640.toField = "set_fraction"
ROUTE640.toNode = "l_hip_RotationInterpolator_Jump"

Scene17.children.append(ROUTE640)
ROUTE641 = x3d.ROUTE()
ROUTE641.fromField = "fraction_changed"
ROUTE641.fromNode = "Jump_Time"
ROUTE641.toField = "set_fraction"
ROUTE641.toNode = "lower_body_RotationInterpolator_Jump"

Scene17.children.append(ROUTE641)
ROUTE642 = x3d.ROUTE()
ROUTE642.fromField = "fraction_changed"
ROUTE642.fromNode = "Jump_Time"
ROUTE642.toField = "set_fraction"
ROUTE642.toNode = "r_wrist_RotationInterpolator_Jump"

Scene17.children.append(ROUTE642)
ROUTE643 = x3d.ROUTE()
ROUTE643.fromField = "fraction_changed"
ROUTE643.fromNode = "Jump_Time"
ROUTE643.toField = "set_fraction"
ROUTE643.toNode = "r_elbow_RotationInterpolator_Jump"

Scene17.children.append(ROUTE643)
ROUTE644 = x3d.ROUTE()
ROUTE644.fromField = "fraction_changed"
ROUTE644.fromNode = "Jump_Time"
ROUTE644.toField = "set_fraction"
ROUTE644.toNode = "r_shoulder_RotationInterpolator_Jump"

Scene17.children.append(ROUTE644)
ROUTE645 = x3d.ROUTE()
ROUTE645.fromField = "fraction_changed"
ROUTE645.fromNode = "Jump_Time"
ROUTE645.toField = "set_fraction"
ROUTE645.toNode = "l_wrist_RotationInterpolator_Jump"

Scene17.children.append(ROUTE645)
ROUTE646 = x3d.ROUTE()
ROUTE646.fromField = "fraction_changed"
ROUTE646.fromNode = "Jump_Time"
ROUTE646.toField = "set_fraction"
ROUTE646.toNode = "l_elbow_RotationInterpolator_Jump"

Scene17.children.append(ROUTE646)
ROUTE647 = x3d.ROUTE()
ROUTE647.fromField = "fraction_changed"
ROUTE647.fromNode = "Jump_Time"
ROUTE647.toField = "set_fraction"
ROUTE647.toNode = "l_shoulder_RotationInterpolator_Jump"

Scene17.children.append(ROUTE647)
ROUTE648 = x3d.ROUTE()
ROUTE648.fromField = "fraction_changed"
ROUTE648.fromNode = "Jump_Time"
ROUTE648.toField = "set_fraction"
ROUTE648.toNode = "head_RotationInterpolator_Jump"

Scene17.children.append(ROUTE648)
ROUTE649 = x3d.ROUTE()
ROUTE649.fromField = "fraction_changed"
ROUTE649.fromNode = "Jump_Time"
ROUTE649.toField = "set_fraction"
ROUTE649.toNode = "neck_RotationInterpolator_Jump"

Scene17.children.append(ROUTE649)
ROUTE650 = x3d.ROUTE()
ROUTE650.fromField = "fraction_changed"
ROUTE650.fromNode = "Jump_Time"
ROUTE650.toField = "set_fraction"
ROUTE650.toNode = "upper_body_RotationInterpolator_Jump"

Scene17.children.append(ROUTE650)
ROUTE651 = x3d.ROUTE()
ROUTE651.fromField = "fraction_changed"
ROUTE651.fromNode = "Jump_Time"
ROUTE651.toField = "set_fraction"
ROUTE651.toNode = "whole_body_RotationInterpolator_Jump"

Scene17.children.append(ROUTE651)
ROUTE652 = x3d.ROUTE()
ROUTE652.fromField = "fraction_changed"
ROUTE652.fromNode = "Jump_Time"
ROUTE652.toField = "set_fraction"
ROUTE652.toNode = "whole_body_TranslationInterpolator_Jump"

Scene17.children.append(ROUTE652)
ROUTE653 = x3d.ROUTE()
ROUTE653.fromField = "value_changed"
ROUTE653.fromNode = "r_ankle_RotationInterpolator_Jump"
ROUTE653.toField = "set_rotation"
ROUTE653.toNode = "hanim_r_ankle"

Scene17.children.append(ROUTE653)
ROUTE654 = x3d.ROUTE()
ROUTE654.fromField = "value_changed"
ROUTE654.fromNode = "r_knee_RotationInterpolator_Jump"
ROUTE654.toField = "set_rotation"
ROUTE654.toNode = "hanim_r_knee"

Scene17.children.append(ROUTE654)
ROUTE655 = x3d.ROUTE()
ROUTE655.fromField = "value_changed"
ROUTE655.fromNode = "r_hip_RotationInterpolator_Jump"
ROUTE655.toField = "set_rotation"
ROUTE655.toNode = "hanim_r_hip"

Scene17.children.append(ROUTE655)
ROUTE656 = x3d.ROUTE()
ROUTE656.fromField = "value_changed"
ROUTE656.fromNode = "l_ankle_RotationInterpolator_Jump"
ROUTE656.toField = "set_rotation"
ROUTE656.toNode = "hanim_l_ankle"

Scene17.children.append(ROUTE656)
ROUTE657 = x3d.ROUTE()
ROUTE657.fromField = "value_changed"
ROUTE657.fromNode = "l_knee_RotationInterpolator_Jump"
ROUTE657.toField = "set_rotation"
ROUTE657.toNode = "hanim_l_knee"

Scene17.children.append(ROUTE657)
ROUTE658 = x3d.ROUTE()
ROUTE658.fromField = "value_changed"
ROUTE658.fromNode = "l_hip_RotationInterpolator_Jump"
ROUTE658.toField = "set_rotation"
ROUTE658.toNode = "hanim_l_hip"

Scene17.children.append(ROUTE658)
ROUTE659 = x3d.ROUTE()
ROUTE659.fromField = "value_changed"
ROUTE659.fromNode = "lower_body_RotationInterpolator_Jump"
ROUTE659.toField = "set_rotation"
ROUTE659.toNode = "hanim_sacroiliac"

Scene17.children.append(ROUTE659)
ROUTE660 = x3d.ROUTE()
ROUTE660.fromField = "value_changed"
ROUTE660.fromNode = "r_wrist_RotationInterpolator_Jump"
ROUTE660.toField = "set_rotation"
ROUTE660.toNode = "hanim_r_wrist"

Scene17.children.append(ROUTE660)
ROUTE661 = x3d.ROUTE()
ROUTE661.fromField = "value_changed"
ROUTE661.fromNode = "r_elbow_RotationInterpolator_Jump"
ROUTE661.toField = "set_rotation"
ROUTE661.toNode = "hanim_r_elbow"

Scene17.children.append(ROUTE661)
ROUTE662 = x3d.ROUTE()
ROUTE662.fromField = "value_changed"
ROUTE662.fromNode = "r_shoulder_RotationInterpolator_Jump"
ROUTE662.toField = "set_rotation"
ROUTE662.toNode = "hanim_r_shoulder"

Scene17.children.append(ROUTE662)
ROUTE663 = x3d.ROUTE()
ROUTE663.fromField = "value_changed"
ROUTE663.fromNode = "l_wrist_RotationInterpolator_Jump"
ROUTE663.toField = "set_rotation"
ROUTE663.toNode = "hanim_l_wrist"

Scene17.children.append(ROUTE663)
ROUTE664 = x3d.ROUTE()
ROUTE664.fromField = "value_changed"
ROUTE664.fromNode = "l_elbow_RotationInterpolator_Jump"
ROUTE664.toField = "set_rotation"
ROUTE664.toNode = "hanim_l_elbow"

Scene17.children.append(ROUTE664)
ROUTE665 = x3d.ROUTE()
ROUTE665.fromField = "value_changed"
ROUTE665.fromNode = "l_shoulder_RotationInterpolator_Jump"
ROUTE665.toField = "set_rotation"
ROUTE665.toNode = "hanim_l_shoulder"

Scene17.children.append(ROUTE665)
ROUTE666 = x3d.ROUTE()
ROUTE666.fromField = "value_changed"
ROUTE666.fromNode = "head_RotationInterpolator_Jump"
ROUTE666.toField = "set_rotation"
ROUTE666.toNode = "hanim_skullbase"

Scene17.children.append(ROUTE666)
ROUTE667 = x3d.ROUTE()
ROUTE667.fromField = "value_changed"
ROUTE667.fromNode = "neck_RotationInterpolator_Jump"
ROUTE667.toField = "set_rotation"
ROUTE667.toNode = "hanim_vc4"

Scene17.children.append(ROUTE667)
ROUTE668 = x3d.ROUTE()
ROUTE668.fromField = "value_changed"
ROUTE668.fromNode = "upper_body_RotationInterpolator_Jump"
ROUTE668.toField = "set_rotation"
ROUTE668.toNode = "hanim_vl1"

Scene17.children.append(ROUTE668)
ROUTE669 = x3d.ROUTE()
ROUTE669.fromField = "value_changed"
ROUTE669.fromNode = "whole_body_RotationInterpolator_Jump"
ROUTE669.toField = "set_rotation"
ROUTE669.toNode = "hanim_humanoid_root"

Scene17.children.append(ROUTE669)
ROUTE670 = x3d.ROUTE()
ROUTE670.fromField = "value_changed"
ROUTE670.fromNode = "whole_body_TranslationInterpolator_Jump"
ROUTE670.toField = "set_translation"
ROUTE670.toNode = "hanim_humanoid_root"

Scene17.children.append(ROUTE670)

X3D0.Scene = Scene17
f = open("././AllenDuttonProtoInstances_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
