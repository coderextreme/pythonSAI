print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Immersive"
X3D0.version = "3.3"
head1 = x3d.head()
meta2 = x3d.meta()
meta2.name = "title"
meta2.content = "NancyDivingProtoInstances.x3d"

head1.children.append(meta2)
meta3 = x3d.meta()
meta3.name = "description"
meta3.content = "Nancy having fun scuba diving - developmental model using ProtoInstance instead of HAnim native tags, do not use this pattern."

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.name = "warning"
meta4.content = "This is a developmental example, use HAnim native tags as shown in other examples instead of the prototypes and ProtoInstances shown here."

head1.children.append(meta4)
meta5 = x3d.meta()
meta5.name = "creator"
meta5.content = "Etsuko Lippi"

head1.children.append(meta5)
meta6 = x3d.meta()
meta6.name = "translators"
meta6.content = "Tom Miller and Don Brutzman, NPS"

head1.children.append(meta6)
meta7 = x3d.meta()
meta7.name = "created"
meta7.content = "19 November 2001"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.name = "modified"
meta8.content = "4 July 2020"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "TODO"
meta9.content = "left arm motion still has a problem"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "creator"
meta10.content = "Cindy Ballreich cindy@ballreich.net 3Name3D"

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.name = "rights"
meta11.content = "1997 3Name3D / Yglesias, Wallock, Divekar, Inc., all rights reserved."

head1.children.append(meta11)
meta12 = x3d.meta()
meta12.name = "identifier"
meta12.content = "https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Prototypes/NancyDivingProtoInstances.x3d"

head1.children.append(meta12)
meta13 = x3d.meta()
meta13.name = "generator"
meta13.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"

head1.children.append(meta13)
meta14 = x3d.meta()
meta14.name = "license"
meta14.content = "../license.html"

head1.children.append(meta14)

X3D0.head = head1
Scene15 = x3d.Scene()
ExternProtoDeclare16 = x3d.ExternProtoDeclare()
ExternProtoDeclare16.name = "Joint"
ExternProtoDeclare16.appinfo = "The Joint node is used as a building block to describe the articulations of the humanoid figure. Each articulation of the humanoid figure is represented by a Joint node each of which is organized into a hierarchy that describes the overall skeleton of the humanoid."
ExternProtoDeclare16.documentation = "http://HAnim.org/Specifications/HAnim2001/part1/Joint.html"
ExternProtoDeclare16.url = ["NancyPrototypes.x3d#Joint","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Prototypes/NancyPrototypes.x3d#Joint","NancyPrototypes.wrl#Joint","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Prototypes/NancyPrototypes.wrl#Joint"]
field17 = x3d.field()
field17.name = "center"
field17.accessType = "inputOutput"
field17.type = "SFVec3f"

ExternProtoDeclare16.field.append(field17)
field18 = x3d.field()
field18.name = "children"
field18.accessType = "inputOutput"
field18.type = "MFNode"

ExternProtoDeclare16.field.append(field18)
field19 = x3d.field()
field19.name = "llimit"
field19.accessType = "inputOutput"
field19.type = "MFFloat"

ExternProtoDeclare16.field.append(field19)
field20 = x3d.field()
field20.name = "limitOrientation"
field20.accessType = "inputOutput"
field20.type = "SFRotation"

ExternProtoDeclare16.field.append(field20)
field21 = x3d.field()
field21.name = "name"
field21.accessType = "inputOutput"
field21.type = "SFString"

ExternProtoDeclare16.field.append(field21)
field22 = x3d.field()
field22.name = "rotation"
field22.accessType = "inputOutput"
field22.type = "SFRotation"

ExternProtoDeclare16.field.append(field22)
field23 = x3d.field()
field23.name = "scale"
field23.accessType = "inputOutput"
field23.type = "SFVec3f"

ExternProtoDeclare16.field.append(field23)
field24 = x3d.field()
field24.name = "scaleOrientation"
field24.accessType = "inputOutput"
field24.type = "SFRotation"

ExternProtoDeclare16.field.append(field24)
field25 = x3d.field()
field25.name = "stiffness"
field25.accessType = "inputOutput"
field25.type = "MFFloat"

ExternProtoDeclare16.field.append(field25)
field26 = x3d.field()
field26.name = "translation"
field26.accessType = "inputOutput"
field26.type = "SFVec3f"

ExternProtoDeclare16.field.append(field26)
field27 = x3d.field()
field27.name = "ulimit"
field27.accessType = "inputOutput"
field27.type = "MFFloat"

ExternProtoDeclare16.field.append(field27)
field28 = x3d.field()
field28.name = "removeChildren"
field28.accessType = "inputOnly"
field28.type = "MFNode"

ExternProtoDeclare16.field.append(field28)
field29 = x3d.field()
field29.name = "bboxSize"
field29.accessType = "initializeOnly"
field29.type = "SFVec3f"

ExternProtoDeclare16.field.append(field29)
field30 = x3d.field()
field30.name = "skinCoordIndex"
field30.accessType = "inputOutput"
field30.type = "MFInt32"

ExternProtoDeclare16.field.append(field30)
field31 = x3d.field()
field31.name = "bboxCenter"
field31.accessType = "initializeOnly"
field31.type = "SFVec3f"

ExternProtoDeclare16.field.append(field31)
field32 = x3d.field()
field32.name = "skinCoordWeight"
field32.accessType = "inputOutput"
field32.type = "MFFloat"

ExternProtoDeclare16.field.append(field32)
field33 = x3d.field()
field33.name = "addChildren"
field33.accessType = "inputOnly"
field33.type = "MFNode"

ExternProtoDeclare16.field.append(field33)

Scene15.children.append(ExternProtoDeclare16)
ExternProtoDeclare34 = x3d.ExternProtoDeclare()
ExternProtoDeclare34.name = "Segment"
ExternProtoDeclare34.appinfo = "The Segment node is used describe the attributes of the physical links between the joints of the humanoid figure. Each body part (pelvis thigh calf etc) of the humanoid figure is represented by a Segment node."
ExternProtoDeclare34.documentation = "http://HAnim.org/Specifications/HAnim2001/part1/Segment.html"
ExternProtoDeclare34.url = ["NancyPrototypes.x3d#Segment","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Prototypes/NancyPrototypes.x3d#Segment","NancyPrototypes.wrl#Segment","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Prototypes/NancyPrototypes.wrl#Segment"]
field35 = x3d.field()
field35.name = "bboxCenter"
field35.accessType = "initializeOnly"
field35.type = "SFVec3f"

ExternProtoDeclare34.field.append(field35)
field36 = x3d.field()
field36.name = "bboxSize"
field36.accessType = "initializeOnly"
field36.type = "SFVec3f"

ExternProtoDeclare34.field.append(field36)
field37 = x3d.field()
field37.name = "centerOfMass"
field37.accessType = "inputOutput"
field37.type = "SFVec3f"

ExternProtoDeclare34.field.append(field37)
field38 = x3d.field()
field38.name = "children"
field38.accessType = "inputOutput"
field38.type = "MFNode"

ExternProtoDeclare34.field.append(field38)
field39 = x3d.field()
field39.name = "coord"
field39.accessType = "inputOutput"
field39.appinfo = "contains Coordinate nodes"
field39.type = "SFNode"

ExternProtoDeclare34.field.append(field39)
field40 = x3d.field()
field40.name = "displacers"
field40.accessType = "inputOutput"
field40.appinfo = "contains Displacer nodes"
field40.type = "MFNode"

ExternProtoDeclare34.field.append(field40)
field41 = x3d.field()
field41.name = "mass"
field41.accessType = "inputOutput"
field41.type = "SFFloat"

ExternProtoDeclare34.field.append(field41)
field42 = x3d.field()
field42.name = "momentsOfInertia"
field42.accessType = "inputOutput"
field42.type = "MFFloat"

ExternProtoDeclare34.field.append(field42)
field43 = x3d.field()
field43.name = "name"
field43.accessType = "inputOutput"
field43.type = "SFString"

ExternProtoDeclare34.field.append(field43)
field44 = x3d.field()
field44.name = "addChildren"
field44.accessType = "inputOnly"
field44.type = "MFNode"

ExternProtoDeclare34.field.append(field44)
field45 = x3d.field()
field45.name = "removeChildren"
field45.accessType = "inputOnly"
field45.type = "MFNode"

ExternProtoDeclare34.field.append(field45)

Scene15.children.append(ExternProtoDeclare34)
ExternProtoDeclare46 = x3d.ExternProtoDeclare()
ExternProtoDeclare46.name = "Humanoid"
ExternProtoDeclare46.appinfo = "The Humanoid node serves as overall container for the Joint Segment Site and Viewpoint nodes which define the skeleton geometry and landmarks of the humanoid figure. Additionally the node provides a means for defining information about the author copyright and usage restrictions of the model."
ExternProtoDeclare46.documentation = "http://HAnim.org/Specifications/HAnim2001/part1/Humanoid.html"
ExternProtoDeclare46.url = ["NancyPrototypes.x3d#Humanoid","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Prototypes/NancyPrototypes.x3d#Humanoid","NancyPrototypes.wrl#Humanoid","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Prototypes/NancyPrototypes.wrl#Humanoid"]
field47 = x3d.field()
field47.name = "bboxCenter"
field47.accessType = "initializeOnly"
field47.type = "SFVec3f"

ExternProtoDeclare46.field.append(field47)
field48 = x3d.field()
field48.name = "bboxSize"
field48.accessType = "initializeOnly"
field48.type = "SFVec3f"

ExternProtoDeclare46.field.append(field48)
field49 = x3d.field()
field49.name = "center"
field49.accessType = "inputOutput"
field49.type = "SFVec3f"

ExternProtoDeclare46.field.append(field49)
field50 = x3d.field()
field50.name = "humanoidBody"
field50.accessType = "inputOutput"
field50.appinfo = "HAnim 1.1 field container for body geometry Hint: replaced by 2.0 skeleton"
field50.documentation = "http://HAnim.org/Specifications/HAnim1.1/#humanoid"
field50.type = "MFNode"

ExternProtoDeclare46.field.append(field50)
field51 = x3d.field()
field51.name = "info"
field51.accessType = "inputOutput"
field51.type = "MFString"

ExternProtoDeclare46.field.append(field51)
field52 = x3d.field()
field52.name = "joints"
field52.accessType = "inputOutput"
field52.appinfo = "Container field for Joint nodes"
field52.type = "MFNode"

ExternProtoDeclare46.field.append(field52)
field53 = x3d.field()
field53.name = "name"
field53.accessType = "inputOutput"
field53.type = "SFString"

ExternProtoDeclare46.field.append(field53)
field54 = x3d.field()
field54.name = "rotation"
field54.accessType = "inputOutput"
field54.type = "SFRotation"

ExternProtoDeclare46.field.append(field54)
field55 = x3d.field()
field55.name = "scale"
field55.accessType = "inputOutput"
field55.type = "SFVec3f"

ExternProtoDeclare46.field.append(field55)
field56 = x3d.field()
field56.name = "scaleOrientation"
field56.accessType = "inputOutput"
field56.type = "SFRotation"

ExternProtoDeclare46.field.append(field56)
field57 = x3d.field()
field57.name = "segments"
field57.accessType = "inputOutput"
field57.appinfo = "Container field for Segment nodes"
field57.type = "MFNode"

ExternProtoDeclare46.field.append(field57)
field58 = x3d.field()
field58.name = "sites"
field58.accessType = "inputOutput"
field58.appinfo = "Container field for Site nodes"
field58.type = "MFNode"

ExternProtoDeclare46.field.append(field58)
field59 = x3d.field()
field59.name = "translation"
field59.accessType = "inputOutput"
field59.type = "SFVec3f"

ExternProtoDeclare46.field.append(field59)
field60 = x3d.field()
field60.name = "version"
field60.accessType = "inputOutput"
field60.appinfo = "legal values: 1.1 or 2.0"
field60.type = "SFString"

ExternProtoDeclare46.field.append(field60)
field61 = x3d.field()
field61.name = "viewpoints"
field61.accessType = "inputOutput"
field61.appinfo = "Container field for Viewpoint nodes"
field61.type = "MFNode"

ExternProtoDeclare46.field.append(field61)
field62 = x3d.field()
field62.name = "skinNormal"
field62.accessType = "inputOutput"
field62.appinfo = "Hint: HAnim version 2.0"
field62.type = "SFNode"

ExternProtoDeclare46.field.append(field62)
field63 = x3d.field()
field63.name = "humanoidVersion"
field63.accessType = "inputOutput"
field63.appinfo = "Version of the humanoid being modeled. Hint: HAnim version 2.0"
field63.type = "SFString"

ExternProtoDeclare46.field.append(field63)
field64 = x3d.field()
field64.name = "skeleton"
field64.accessType = "inputOutput"
field64.appinfo = "HAnim 2.0 field container for body geometry Hint: replaces 1.1 humanoidBody"
field64.documentation = "http://HAnim.org/Specifications/HAnim2001/part1/Humanoid.html"
field64.type = "MFNode"

ExternProtoDeclare46.field.append(field64)
field65 = x3d.field()
field65.name = "skinCoord"
field65.accessType = "inputOutput"
field65.appinfo = "Hint: HAnim version 2.0"
field65.type = "SFNode"

ExternProtoDeclare46.field.append(field65)

Scene15.children.append(ExternProtoDeclare46)
#====================
ExternProtoDeclare66 = x3d.ExternProtoDeclare()
ExternProtoDeclare66.name = "ViewPositionOrientation"
ExternProtoDeclare66.appinfo = "ViewPositionOrientation provides provides console output of local position and orientation as user navigates"
ExternProtoDeclare66.url = ["../../Savage/Tools/Authoring/ViewPositionOrientationPrototype.x3d#ViewPositionOrientation","../../Savage/Tools/Authoring/ViewPositionOrientationPrototype.x3d#ViewPositionOrientation","https://savage.nps.edu/Savage/Tools/Authoring/ViewPositionOrientationPrototype.x3d#ViewPositionOrientation","../../Savage/Tools/Authoring/ViewPositionOrientationPrototype.wrl#ViewPositionOrientation","../../Savage/Tools/Authoring/ViewPositionOrientationPrototype.wrl#ViewPositionOrientation","https://savage.nps.edu/Savage/Tools/Authoring/ViewPositionOrientationPrototype.wrl#ViewPositionOrientation"]
field67 = x3d.field()
field67.name = "enabled"
field67.accessType = "inputOutput"
field67.appinfo = "Whether or not ViewPositionOrientation sends output to console"
field67.type = "SFBool"

ExternProtoDeclare66.field.append(field67)
field68 = x3d.field()
field68.name = "traceEnabled"
field68.accessType = "initializeOnly"
field68.appinfo = "Output internal trace messages for debugging this node, intended for developer use only"
field68.type = "SFBool"

ExternProtoDeclare66.field.append(field68)
field69 = x3d.field()
field69.name = "set_traceEnabled"
field69.accessType = "inputOnly"
field69.appinfo = "Ability to turn output tracing on/off at runtime"
field69.type = "SFBool"

ExternProtoDeclare66.field.append(field69)
field70 = x3d.field()
field70.name = "position_changed"
field70.accessType = "outputOnly"
field70.appinfo = "Output local position"
field70.type = "SFVec3f"

ExternProtoDeclare66.field.append(field70)
field71 = x3d.field()
field71.name = "orientation_changed"
field71.accessType = "outputOnly"
field71.appinfo = "Output local orientation"
field71.type = "SFRotation"

ExternProtoDeclare66.field.append(field71)
field72 = x3d.field()
field72.name = "outputViewpointString"
field72.accessType = "outputOnly"
field72.appinfo = "MFString value of new Viewpoint, suitable for use in string field of a Text node"
field72.type = "MFString"

ExternProtoDeclare66.field.append(field72)

Scene15.children.append(ExternProtoDeclare66)
ProtoInstance73 = x3d.ProtoInstance()
ProtoInstance73.name = "ViewPositionOrientation"
ProtoInstance73.DEF = "ExampleViewPositionOrientation"
fieldValue74 = x3d.fieldValue()
fieldValue74.name = "enabled"
fieldValue74.value = "true"

ProtoInstance73.fieldValue.append(fieldValue74)

Scene15.children.append(ProtoInstance73)
#Example use: https://savage.nps.edu/Savage/Tools/Animation/ViewPositionOrientationExample.x3d
#====================
#Start scene graph.
ProtoInstance75 = x3d.ProtoInstance()
ProtoInstance75.name = "ViewPositionOrientation"
fieldValue76 = x3d.fieldValue()
fieldValue76.name = "enabled"
fieldValue76.value = "true"

ProtoInstance75.fieldValue.append(fieldValue76)

Scene15.children.append(ProtoInstance75)
Background77 = x3d.Background()
Background77.skyColor = [0,0.4,1]

Scene15.children.append(Background77)
NavigationInfo78 = x3d.NavigationInfo()
NavigationInfo78.avatarSize = [0.15,1.53,0.75]
NavigationInfo78.speed = 0.5
NavigationInfo78.type = ["EXAMINE"]

Scene15.children.append(NavigationInfo78)
Viewpoint79 = x3d.Viewpoint()
Viewpoint79.description = "Nancy diving default viewpoint"
Viewpoint79.position = [-0.8,0,3.1]

Scene15.children.append(Viewpoint79)
LOD80 = x3d.LOD()
Group81 = x3d.Group()
Group81.DEF = "Viewpoint"
#High Resolution
Viewpoint82 = x3d.Viewpoint()
Viewpoint82.description = "Nancy front viewpoint"
Viewpoint82.orientation = [-0.354,0.878,-0.321,4.5485]
Viewpoint82.position = [-2.2,-0.7,0]

Group81.children.append(Viewpoint82)
Viewpoint83 = x3d.Viewpoint()
Viewpoint83.description = "Nancy above viewpoint"
Viewpoint83.orientation = [-0.126,-0.978,-0.168,1.5385]
Viewpoint83.position = [-3,0.5,0]

Group81.children.append(Viewpoint83)
Viewpoint84 = x3d.Viewpoint()
Viewpoint84.description = "Nancy back viewpoint"
Viewpoint84.orientation = [0.037,0.999,-0.011,1.572]
Viewpoint84.position = [0.7,0.1,0]

Group81.children.append(Viewpoint84)
Viewpoint85 = x3d.Viewpoint()
Viewpoint85.description = "Nancy side viewpoint"
Viewpoint85.orientation = [0.121,0.987,-0.105,3.2682]
Viewpoint85.position = [-1.2,-0.2,-1.5]

Group81.children.append(Viewpoint85)
Viewpoint86 = x3d.Viewpoint()
Viewpoint86.description = "Nancy viewpoint through her goggles"
Viewpoint86.orientation = [-0.357,0.872,0.335,1.5225]
Viewpoint86.position = [-1.5,0.1,0]

Group81.children.append(Viewpoint86)
Group87 = x3d.Group()
Group87.DEF = "HighResolution"
Transform88 = x3d.Transform()
Transform88.rotation = [1,0,0,1.57]
Transform89 = x3d.Transform()
Transform89.rotation = [0,0,1,1.57]
WorldInfo90 = x3d.WorldInfo()
WorldInfo90.info = ["Copyright (c) 1997. 3Name3D / Yglesias Wallock Divekar, Inc."]
WorldInfo90.title = "Nancy - an HAnim compliant avatar by 3Name3D"

Transform89.children.append(WorldInfo90)
ProtoInstance91 = x3d.ProtoInstance()
ProtoInstance91.name = "Humanoid"
ProtoInstance91.DEF = "Humanoid"
fieldValue92 = x3d.fieldValue()
fieldValue92.name = "humanoidBody"
ProtoInstance93 = x3d.ProtoInstance()
ProtoInstance93.name = "Joint"
ProtoInstance93.DEF = "hanim_humanoid_root"
fieldValue94 = x3d.fieldValue()
fieldValue94.name = "name"
fieldValue94.value = "humanoid_root"

ProtoInstance93.fieldValue.append(fieldValue94)
fieldValue95 = x3d.fieldValue()
fieldValue95.name = "center"
fieldValue95.value = "-0.00405 0.855 -0.000113"

ProtoInstance93.fieldValue.append(fieldValue95)
fieldValue96 = x3d.fieldValue()
fieldValue96.name = "children"
ProtoInstance97 = x3d.ProtoInstance()
ProtoInstance97.name = "Joint"
ProtoInstance97.DEF = "hanim_sacroiliac"
fieldValue98 = x3d.fieldValue()
fieldValue98.name = "name"
fieldValue98.value = "sacroiliac"

ProtoInstance97.fieldValue.append(fieldValue98)
fieldValue99 = x3d.fieldValue()
fieldValue99.name = "center"
fieldValue99.value = "0 1.01 -0.0204"

ProtoInstance97.fieldValue.append(fieldValue99)
fieldValue100 = x3d.fieldValue()
fieldValue100.name = "children"
ProtoInstance101 = x3d.ProtoInstance()
ProtoInstance101.name = "Segment"
ProtoInstance101.DEF = "hanim_pelvis"
fieldValue102 = x3d.fieldValue()
fieldValue102.name = "name"
fieldValue102.value = "pelvis"

ProtoInstance101.fieldValue.append(fieldValue102)
fieldValue103 = x3d.fieldValue()
fieldValue103.name = "children"
Shape104 = x3d.Shape()
Appearance105 = x3d.Appearance()
Material106 = x3d.Material()
Material106.DEF = "Pants_Color"
Material106.diffuseColor = [0,0,0.502]

Appearance105.material = Material106

Shape104.appearance = Appearance105
IndexedFaceSet107 = x3d.IndexedFaceSet()
IndexedFaceSet107.coordIndex = [0,1,40,-1,1,2,40,-1,2,3,40,-1,3,4,40,-1,4,5,40,-1,5,4,9,-1,4,3,8,-1,3,2,8,-1,2,1,6,-1,0,7,1,-1,7,6,1,-1,6,8,2,-1,9,4,10,-1,4,8,10,-1,8,6,12,-1,7,0,47,-1,50,5,9,-1,7,47,55,-1,55,13,7,-1,50,9,56,-1,9,10,14,-1,10,11,15,-1,11,12,16,-1,12,13,19,-1,13,55,17,-1,60,17,55,-1,17,19,13,-1,19,16,12,-1,16,15,11,-1,15,18,10,-1,14,56,9,-1,56,14,64,-1,17,60,20,-1,20,19,17,-1,21,64,14,-1,14,22,21,-1,15,16,24,-1,16,19,24,-1,19,20,26,-1,24,23,15,-1,64,21,69,-1,21,22,29,-1,19,26,25,-1,20,63,27,-1,27,26,20,-1,25,24,19,-1,30,29,22,-1,29,28,21,-1,28,69,21,-1,27,34,26,-1,69,28,79,-1,29,30,32,-1,30,23,33,-1,23,24,37,-1,25,26,34,-1,83,27,77,-1,37,33,23,-1,33,32,30,-1,31,79,28,-1,79,31,84,-1,32,33,36,-1,24,25,37,-1,34,27,83,-1,83,38,34,-1,34,37,25,-1,37,36,33,-1,36,35,32,-1,84,31,89,-1,31,35,89,-1,35,36,39,-1,36,37,39,-1,38,83,89,-1,89,39,38,-1,39,89,35,-1,40,41,0,-1,40,42,41,-1,40,43,42,-1,40,44,43,-1,40,45,44,-1,49,44,45,-1,48,43,44,-1,48,42,43,-1,46,41,42,-1,41,47,0,-1,41,46,47,-1,42,48,46,-1,51,44,49,-1,51,48,44,-1,48,52,53,-1,49,45,50,-1,56,49,50,-1,57,51,49,-1,58,53,52,-1,59,54,53,-1,62,55,54,-1,55,62,60,-1,54,59,62,-1,53,58,59,-1,51,61,58,-1,49,56,57,-1,64,57,56,-1,67,59,58,-1,68,62,59,-1,60,63,20,-1,60,62,63,-1,59,67,68,-1,58,61,67,-1,57,64,65,-1,65,66,57,-1,71,63,62,-1,69,65,64,-1,74,66,65,-1,78,68,67,-1,70,71,62,-1,63,72,27,-1,63,71,72,-1,68,78,76,-1,67,75,78,-1,66,74,75,-1,65,73,74,-1,65,69,73,-1,77,27,72,-1,71,82,72,-1,79,73,69,-1,81,75,74,-1,82,71,70,-1,77,72,83,-1,73,79,80,-1,84,80,79,-1,86,75,81,-1,83,72,82,-1,82,88,83,-1,70,87,82,-1,81,85,86,-1,89,80,84,-1,89,85,80,-1,90,86,85,-1,90,87,86,-1,89,83,88,-1,88,90,89,-1,85,89,90,-1,50,45,5,-1,45,40,5,-1,10,8,11,-1,8,12,11,-1,18,22,10,-1,22,14,10,-1,57,66,51,-1,66,61,51,-1,51,58,48,-1,58,52,48,-1,48,53,46,-1,53,54,46,-1,76,70,68,-1,70,62,68,-1,29,32,28,-1,28,32,31,-1,32,35,31,-1,85,81,80,-1,81,73,80,-1,81,74,73,-1,39,37,38,-1,37,34,38,-1,82,87,88,-1,87,90,88,-1,87,78,86,-1,78,75,86,-1,61,66,67,-1,66,75,67,-1,22,18,15,-1,23,30,15,-1,30,22,15,-1,13,12,7,-1,12,6,7,-1,46,54,47,-1,54,55,47,-1,87,76,78,-1,87,70,76,-1]
IndexedFaceSet107.creaseAngle = 1.14
Coordinate108 = x3d.Coordinate()
Coordinate108.point = (0.0000,1.0600,0.0218,0.0561,1.0700,0.0073,0.0851,1.0700,-0.0115,0.1040,1.0700,-0.0497,0.0851,1.0700,-0.0851,0.0320,1.0600,-0.0985,0.0873,1.0400,0.0078,0.0330,1.0400,0.0395,0.1230,1.0500,-0.0405,0.0609,1.0200,-0.1060,0.0894,0.9960,-0.1060,0.1430,1.0000,-0.0309,0.1170,1.0000,0.0164,0.0314,0.9990,0.0502,0.0314,0.9600,-0.1300,0.1560,0.9660,-0.0405,0.1560,0.9680,-0.0072,0.0341,0.9540,0.0513,0.1150,0.9600,-0.0916,0.1210,0.9260,0.0352,0.0357,0.9200,0.0497,0.0314,0.9100,-0.1460,0.0991,0.9100,-0.1310,0.1690,0.8830,-0.0448,0.1690,0.8850,-0.0094,0.1230,0.8730,0.0384,0.0926,0.8720,0.0470,0.0325,0.8730,0.0287,0.0293,0.8660,-0.1420,0.1020,0.8690,-0.1310,0.1290,0.8680,-0.1030,0.0314,0.8400,-0.1250,0.1010,0.8440,-0.1220,0.1330,0.8460,-0.0878,0.0653,0.8350,0.0132,0.0615,0.8240,-0.1110,0.0985,0.8230,-0.1010,0.1320,0.8260,-0.0448,0.0609,0.8210,-0.0158,0.0599,0.8120,-0.0545,0.0000,1.0800,-0.0266,-0.0561,1.0700,0.0073,-0.0851,1.0700,-0.0115,-0.1040,1.0700,-0.0497,-0.0851,1.0700,-0.0851,-0.0320,1.0600,-0.0985,-0.0873,1.0400,0.0078,-0.0330,1.0400,0.0395,-0.1230,1.0500,-0.0405,-0.0609,1.0200,-0.1060,0.0000,1.0200,-0.1080,-0.0894,0.9960,-0.1060,-0.1430,1.0000,-0.0309,-0.1440,1.0000,-0.0110,-0.1170,1.0000,0.0164,-0.0314,0.9990,0.0502,0.0000,0.9610,-0.1230,-0.0314,0.9600,-0.1300,-0.1560,0.9660,-0.0405,-0.1560,0.9680,-0.0072,-0.0341,0.9540,0.0513,-0.1150,0.9600,-0.0916,-0.1210,0.9260,0.0352,-0.0357,0.9200,0.0497,0.0000,0.9100,-0.1270,-0.0314,0.9100,-0.1460,-0.0991,0.9100,-0.1310,-0.1670,0.9110,-0.0448,-0.1670,0.9120,-0.0067,0.0000,0.8830,-0.1290,-0.1230,0.8730,0.0384,-0.0926,0.8720,0.0470,-0.0325,0.8730,0.0287,-0.0293,0.8660,-0.1420,-0.1020,0.8690,-0.1310,-0.1290,0.8680,-0.1030,-0.1660,0.8630,-0.0148,0.0000,0.8630,-0.0046,-0.1660,0.8620,-0.0459,0.0000,0.8580,-0.1000,-0.0314,0.8400,-0.1250,-0.1010,0.8440,-0.1220,-0.0653,0.8350,0.0132,0.0000,0.8390,-0.0217,0.0000,0.8350,-0.0867,-0.0615,0.8240,-0.1110,-0.0985,0.8230,-0.1010,-0.1320,0.8260,-0.0448,-0.0609,0.8210,-0.0158,0.0000,0.8310,-0.0626,-0.0599,0.8120,-0.0545)

IndexedFaceSet107.coord = Coordinate108

Shape104.geometry = IndexedFaceSet107

fieldValue103.children.append(Shape104)

ProtoInstance101.fieldValue.append(fieldValue103)

fieldValue100.children.append(ProtoInstance101)
ProtoInstance109 = x3d.ProtoInstance()
ProtoInstance109.name = "Joint"
ProtoInstance109.DEF = "hanim_l_hip"
fieldValue110 = x3d.fieldValue()
fieldValue110.name = "name"
fieldValue110.value = "l_hip"

ProtoInstance109.fieldValue.append(fieldValue110)
fieldValue111 = x3d.fieldValue()
fieldValue111.name = "center"
fieldValue111.value = "0.122 0.888271 -0.0693267"

ProtoInstance109.fieldValue.append(fieldValue111)
fieldValue112 = x3d.fieldValue()
fieldValue112.name = "children"
ProtoInstance113 = x3d.ProtoInstance()
ProtoInstance113.name = "Segment"
ProtoInstance113.DEF = "hanim_l_thigh"
fieldValue114 = x3d.fieldValue()
fieldValue114.name = "name"
fieldValue114.value = "l_thigh"

ProtoInstance113.fieldValue.append(fieldValue114)
fieldValue115 = x3d.fieldValue()
fieldValue115.name = "children"
Shape116 = x3d.Shape()
Appearance117 = x3d.Appearance()
Material118 = x3d.Material()
Material118.USE = "Pants_Color"

Appearance117.material = Material118

Shape116.appearance = Appearance117
IndexedFaceSet119 = x3d.IndexedFaceSet()
IndexedFaceSet119.coordIndex = [0,4,5,-1,3,4,0,-1,0,7,1,-1,0,8,7,-1,0,6,8,-1,0,5,6,-1,0,2,3,-1,0,1,2,-1,9,2,1,-1,10,3,2,-1,11,4,3,-1,12,5,4,-1,13,6,5,-1,15,7,8,-1,9,1,7,-1,7,15,9,-1,8,14,15,-1,5,16,13,-1,5,12,16,-1,4,11,12,-1,3,10,11,-1,2,9,10,-1,20,13,16,-1,18,11,10,-1,19,12,11,-1,20,16,12,-1,23,15,14,-1,15,23,24,-1,12,19,20,-1,11,18,19,-1,10,17,18,-1,26,18,17,-1,27,19,18,-1,27,20,19,-1,28,21,20,-1,29,23,22,-1,23,29,30,-1,20,32,28,-1,20,27,32,-1,18,26,27,-1,17,25,26,-1,25,31,30,-1,30,29,26,-1,30,26,25,-1,29,28,27,-1,29,27,26,-1,28,32,27,-1,22,23,14,-1,20,21,13,-1,21,22,13,-1,22,14,13,-1,9,15,24,-1,10,9,17,-1,9,24,17,-1,6,13,8,-1,13,14,8,-1,28,29,21,-1,29,22,21,-1,24,31,17,-1,31,25,17,-1,30,31,23,-1,31,24,23,-1]
IndexedFaceSet119.creaseAngle = 1.32
Coordinate120 = x3d.Coordinate()
Coordinate120.point = (0.0969,0.8040,-0.0486,0.1010,0.8760,0.0336,0.1700,0.8940,-0.0078,0.1700,0.8910,-0.0760,0.1240,0.8580,-0.1290,0.0760,0.8430,-0.1430,0.0250,0.8190,-0.0889,0.0507,0.8470,0.0196,0.0035,0.8260,-0.0287,0.0991,0.8080,0.0406,0.1610,0.8140,-0.0019,0.1650,0.8080,-0.0755,0.1220,0.7880,-0.1260,0.0099,0.7620,-0.0937,0.0099,0.7620,-0.0309,0.0491,0.7770,0.0185,0.0755,0.7660,-0.1390,0.1300,0.5970,-0.0062,0.1320,0.6000,-0.0593,0.1080,0.6030,-0.1050,0.0722,0.6010,-0.1180,0.0314,0.5900,-0.0953,0.0239,0.5660,-0.0427,0.0470,0.5660,0.0051,0.0878,0.5810,0.0217,0.1140,0.4990,-0.0132,0.1160,0.4880,-0.0610,0.1030,0.5670,-0.0991,0.0362,0.5570,-0.0926,0.0250,0.4860,-0.0470,0.0507,0.4970,-0.0019,0.0862,0.5130,0.0180,0.0733,0.5790,-0.1080)

IndexedFaceSet119.coord = Coordinate120

Shape116.geometry = IndexedFaceSet119

fieldValue115.children.append(Shape116)

ProtoInstance113.fieldValue.append(fieldValue115)

fieldValue112.children.append(ProtoInstance113)
ProtoInstance121 = x3d.ProtoInstance()
ProtoInstance121.name = "Joint"
ProtoInstance121.DEF = "hanim_l_knee"
fieldValue122 = x3d.fieldValue()
fieldValue122.name = "name"
fieldValue122.value = "l_knee"

ProtoInstance121.fieldValue.append(fieldValue122)
fieldValue123 = x3d.fieldValue()
fieldValue123.name = "center"
fieldValue123.value = "0.0738 0.517 -0.0284"

ProtoInstance121.fieldValue.append(fieldValue123)
fieldValue124 = x3d.fieldValue()
fieldValue124.name = "children"
ProtoInstance125 = x3d.ProtoInstance()
ProtoInstance125.name = "Segment"
ProtoInstance125.DEF = "hanim_l_calf"
fieldValue126 = x3d.fieldValue()
fieldValue126.name = "name"
fieldValue126.value = "l_calf"

ProtoInstance125.fieldValue.append(fieldValue126)
fieldValue127 = x3d.fieldValue()
fieldValue127.name = "children"
Shape128 = x3d.Shape()
Appearance129 = x3d.Appearance()
Material130 = x3d.Material()
Material130.USE = "Pants_Color"

Appearance129.material = Material130

Shape128.appearance = Appearance129
IndexedFaceSet131 = x3d.IndexedFaceSet()
IndexedFaceSet131.coordIndex = [2,1,0,-1,2,3,1,-1,2,4,3,-1,2,5,4,-1,2,6,5,-1,2,7,6,-1,2,8,7,-1,2,0,8,-1,9,8,0,-1,10,6,7,-1,11,5,6,-1,12,4,5,-1,12,3,4,-1,13,1,3,-1,1,13,14,-1,3,12,13,-1,5,11,12,-1,6,10,11,-1,8,9,15,-1,22,13,12,-1,13,22,14,-1,17,15,9,-1,20,12,11,-1,21,22,12,-1,23,9,14,-1,9,23,16,-1,14,22,23,-1,12,20,21,-1,15,17,18,-1,9,16,17,-1,24,17,16,-1,25,18,17,-1,26,19,18,-1,27,20,19,-1,28,21,20,-1,29,22,21,-1,30,23,22,-1,31,16,23,-1,23,30,31,-1,22,29,30,-1,21,28,29,-1,20,27,28,-1,19,26,27,-1,18,25,26,-1,17,24,25,-1,16,31,24,-1,33,26,25,-1,36,29,28,-1,37,31,30,-1,29,36,30,-1,25,24,33,-1,31,37,24,-1,32,33,24,-1,24,37,32,-1,38,37,30,-1,30,36,38,-1,41,33,32,-1,42,39,34,-1,44,36,35,-1,45,38,36,-1,46,37,38,-1,38,45,46,-1,36,44,45,-1,35,43,44,-1,39,42,47,-1,32,40,41,-1,40,46,45,-1,41,40,45,-1,41,45,44,-1,44,43,42,-1,44,42,41,-1,43,47,42,-1,39,35,28,-1,35,36,28,-1,34,39,27,-1,39,28,27,-1,33,34,26,-1,34,27,26,-1,33,41,34,-1,41,42,34,-1,40,32,46,-1,32,37,46,-1,10,19,11,-1,19,20,11,-1,14,9,1,-1,9,0,1,-1,8,15,7,-1,7,15,10,-1,15,19,10,-1,15,18,19,-1,43,35,47,-1,35,39,47,-1]
IndexedFaceSet131.creaseAngle = 1.57
Coordinate132 = x3d.Coordinate()
Coordinate132.point = (0.0883,0.5320,-0.0035,0.0609,0.5330,-0.0083,0.0814,0.5500,-0.0395,0.0529,0.5360,-0.0368,0.0577,0.5440,-0.0577,0.0722,0.5460,-0.0717,0.0975,0.5400,-0.0647,0.1050,0.5390,-0.0438,0.1040,0.5390,-0.0223,0.0862,0.5060,0.0158,0.1010,0.5100,-0.0798,0.0706,0.5100,-0.1010,0.0406,0.5130,-0.0744,0.0368,0.5100,-0.0357,0.0556,0.5060,-0.0003,0.1170,0.5080,-0.0169,0.0878,0.3610,-0.0126,0.1230,0.3630,-0.0400,0.1230,0.3630,-0.0663,0.1070,0.3670,-0.1070,0.0588,0.3650,-0.1220,0.0228,0.3580,-0.0926,0.0239,0.3580,-0.0475,0.0497,0.3580,-0.0234,0.1180,0.3110,-0.0411,0.1180,0.3090,-0.0685,0.1050,0.3100,-0.1080,0.0572,0.3080,-0.1230,0.0201,0.3090,-0.0937,0.0191,0.3110,-0.0508,0.0475,0.3070,-0.0282,0.0883,0.3090,-0.0180,0.0959,0.1240,-0.0400,0.0905,0.1200,-0.0647,0.0738,0.1170,-0.0814,0.0373,0.1210,-0.0636,0.0416,0.1240,-0.0416,0.0744,0.1300,-0.0212,0.0561,0.1300,-0.0245,0.0529,0.1210,-0.0873,0.0948,0.0897,-0.0368,0.0916,0.0779,-0.0604,0.0717,0.0854,-0.0765,0.0406,0.0918,-0.0626,0.0384,0.0881,-0.0363,0.0540,0.0972,-0.0175,0.0765,0.1100,-0.0169,0.0486,0.0999,-0.0835)

IndexedFaceSet131.coord = Coordinate132

Shape128.geometry = IndexedFaceSet131

fieldValue127.children.append(Shape128)

ProtoInstance125.fieldValue.append(fieldValue127)

fieldValue124.children.append(ProtoInstance125)
ProtoInstance133 = x3d.ProtoInstance()
ProtoInstance133.name = "Joint"
ProtoInstance133.DEF = "hanim_l_ankle"
fieldValue134 = x3d.fieldValue()
fieldValue134.name = "name"
fieldValue134.value = "l_ankle"

ProtoInstance133.fieldValue.append(fieldValue134)
fieldValue135 = x3d.fieldValue()
fieldValue135.name = "center"
fieldValue135.value = "0.0645 0.0719 -0.048"

ProtoInstance133.fieldValue.append(fieldValue135)
fieldValue136 = x3d.fieldValue()
fieldValue136.name = "children"
ProtoInstance137 = x3d.ProtoInstance()
ProtoInstance137.name = "Segment"
ProtoInstance137.DEF = "hanim_l_hindfoot"
fieldValue138 = x3d.fieldValue()
fieldValue138.name = "name"
fieldValue138.value = "l_hindfoot"

ProtoInstance137.fieldValue.append(fieldValue138)
fieldValue139 = x3d.fieldValue()
fieldValue139.name = "children"
Shape140 = x3d.Shape()
Appearance141 = x3d.Appearance()
Material142 = x3d.Material()
Material142.DEF = "Shoe_Color"
Material142.ambientIntensity = 0.25
Material142.diffuseColor = [0.753,1,0.243]

Appearance141.material = Material142

Shape140.appearance = Appearance141
IndexedFaceSet143 = x3d.IndexedFaceSet()
IndexedFaceSet143.coordIndex = [2,1,0,-1,4,3,1,-1,2,4,1,-1,3,6,5,-1,1,3,5,-1,6,8,7,-1,5,6,7,-1,8,10,9,-1,7,8,9,-1,10,12,11,-1,9,10,11,-1,12,14,13,-1,11,12,13,-1,14,16,15,-1,13,14,15,-1,16,18,17,-1,15,16,17,-1,18,20,19,-1,17,18,19,-1,20,22,21,-1,19,20,21,-1,22,24,23,-1,21,22,23,-1,24,25,0,-1,23,24,0,-1,25,4,2,-1,0,25,2,-1,18,26,20,-1,16,26,18,-1,27,26,16,-1,14,27,16,-1,12,27,14,-1,28,27,12,-1,29,28,12,-1,10,29,12,-1,8,29,10,-1,6,37,8,-1,24,30,25,-1,31,30,24,-1,22,31,24,-1,32,31,22,-1,20,32,22,-1,33,32,20,-1,26,33,20,-1,34,33,26,-1,27,34,26,-1,35,34,27,-1,28,35,27,-1,29,35,28,-1,36,35,29,-1,8,36,29,-1,37,36,8,-1,6,38,37,-1,3,38,6,-1,39,38,3,-1,30,39,25,-1,41,40,30,-1,31,41,30,-1,42,41,31,-1,32,42,31,-1,43,42,32,-1,33,43,32,-1,44,43,33,-1,34,44,33,-1,45,44,34,-1,35,45,34,-1,46,45,35,-1,36,46,35,-1,47,46,36,-1,37,47,36,-1,38,47,37,-1,48,47,38,-1,49,48,38,-1,39,49,38,-1,40,49,39,-1,30,40,39,-1,48,49,50,-1,47,48,50,-1,46,47,50,-1,45,46,50,-1,44,45,50,-1,43,44,50,-1,42,43,50,-1,41,42,50,-1,40,41,50,-1,49,40,50,-1,11,13,15,-1,11,15,17,-1,9,11,17,-1,9,17,19,-1,7,9,19,-1,7,19,21,-1,5,7,21,-1,5,21,23,-1,5,23,0,-1,1,5,0,-1,3,4,39,-1,4,25,39,-1]
IndexedFaceSet143.creaseAngle = 1.57
Coordinate144 = x3d.Coordinate()
Coordinate144.point = (0.0529,0.0000,-0.0923,0.0863,0.0000,-0.0862,0.0727,0.0000,-0.0994,0.0863,0.0219,-0.0862,0.0727,0.0219,-0.0994,0.1000,0.0000,-0.0594,0.1000,0.0219,-0.0594,0.1130,0.0000,0.0645,0.1130,0.0219,0.0645,0.1120,0.0000,0.1170,0.1120,0.0156,0.1170,0.0701,0.0000,0.1460,0.0701,0.0156,0.1460,0.0468,0.0000,0.1530,0.0468,0.0156,0.1530,0.0215,0.0000,0.1460,0.0215,0.0156,0.1460,0.0165,0.0000,0.1250,0.0165,0.0156,0.1250,0.0211,0.0000,0.0377,0.0211,0.0219,0.0377,0.0393,0.0000,-0.0129,0.0393,0.0219,-0.0129,0.0433,0.0000,-0.0534,0.0433,0.0219,-0.0534,0.0529,0.0219,-0.0923,0.0305,0.0253,0.0938,0.0505,0.0253,0.0990,0.0854,0.0253,0.0834,0.1020,0.0253,0.0707,0.0568,0.0573,-0.0918,0.0492,0.0573,-0.0497,0.0435,0.0573,-0.0225,0.0442,0.0573,0.0235,0.0623,0.0573,0.0366,0.0911,0.0573,0.0159,0.0962,0.0573,-0.0121,0.0911,0.0573,-0.0482,0.0758,0.0573,-0.0899,0.0676,0.0573,-0.0962,0.0578,0.0953,-0.0896,0.0489,0.0953,-0.0757,0.0447,0.0953,-0.0432,0.0451,0.0953,-0.0128,0.0624,0.0953,-0.0047,0.0857,0.0953,-0.0134,0.0953,0.0953,-0.0380,0.0843,0.0953,-0.0803,0.0761,0.0953,-0.0889,0.0682,0.0953,-0.0929,0.0675,0.1300,-0.0608)

IndexedFaceSet143.coord = Coordinate144

Shape140.geometry = IndexedFaceSet143

fieldValue139.children.append(Shape140)
Transform145 = x3d.Transform()
Transform145.scale = [0.015,0.015,0.015]
Transform146 = x3d.Transform()
Transform146.rotation = [0,0,1,1.57]
Transform146.translation = [6,-0.5,-7.5]
Shape147 = x3d.Shape()
Appearance148 = x3d.Appearance()
Material149 = x3d.Material()
Material149.diffuseColor = [0.753,1,0.243]

Appearance148.material = Material149

Shape147.appearance = Appearance148
Extrusion150 = x3d.Extrusion()
Extrusion150.DEF = "Finl"
Extrusion150.ccw = False
Extrusion150.creaseAngle = 3.14
Extrusion150.crossSection = [-1,0,-0.8,2,-0.7,3,0,5.2,0.7,3,0.8,2,1,0,0.8,-2,0.7,-3,0,-5.2,-0.7,-3,-0.8,-2,-1,0]
Extrusion150.scale = [0.25,0.25,0.5,0.75,0.5,1.2,0.5,1.35,0.5,1.35,0.5,1.35,0.5,1.35,0.5,1.35,0.5,1.35]
Extrusion150.spine = (0.0000,0.0000,1.0000,0.0000,0.0000,5.0000,0.0000,0.0000,8.0000,0.0000,0.0000,12.0000,0.0000,0.0000,15.0000,0.5000,0.0000,18.0000,1.5000,0.0000,25.0000,2.5000,0.0000,30.0000,4.0000,0.0000,34.0000)

Shape147.geometry = Extrusion150

Transform146.children.append(Shape147)

Transform145.children.append(Transform146)

fieldValue139.children.append(Transform145)

ProtoInstance137.fieldValue.append(fieldValue139)

fieldValue136.children.append(ProtoInstance137)

ProtoInstance133.fieldValue.append(fieldValue136)

fieldValue124.children.append(ProtoInstance133)

ProtoInstance121.fieldValue.append(fieldValue124)

fieldValue112.children.append(ProtoInstance121)

ProtoInstance109.fieldValue.append(fieldValue112)

fieldValue100.children.append(ProtoInstance109)
ProtoInstance151 = x3d.ProtoInstance()
ProtoInstance151.name = "Joint"
ProtoInstance151.DEF = "hanim_r_hip"
fieldValue152 = x3d.fieldValue()
fieldValue152.name = "name"
fieldValue152.value = "r_hip"

ProtoInstance151.fieldValue.append(fieldValue152)
fieldValue153 = x3d.fieldValue()
fieldValue153.name = "center"
fieldValue153.value = "-0.11 0.892362 -0.0732533"

ProtoInstance151.fieldValue.append(fieldValue153)
fieldValue154 = x3d.fieldValue()
fieldValue154.name = "children"
ProtoInstance155 = x3d.ProtoInstance()
ProtoInstance155.name = "Segment"
ProtoInstance155.DEF = "hanim_r_thigh"
fieldValue156 = x3d.fieldValue()
fieldValue156.name = "name"
fieldValue156.value = "r_thigh"

ProtoInstance155.fieldValue.append(fieldValue156)
fieldValue157 = x3d.fieldValue()
fieldValue157.name = "children"
Shape158 = x3d.Shape()
Appearance159 = x3d.Appearance()
Material160 = x3d.Material()
Material160.USE = "Pants_Color"

Appearance159.material = Material160

Shape158.appearance = Appearance159
IndexedFaceSet161 = x3d.IndexedFaceSet()
IndexedFaceSet161.coordIndex = [5,4,0,-1,0,4,3,-1,1,7,0,-1,7,8,0,-1,8,6,0,-1,6,5,0,-1,3,2,0,-1,2,1,0,-1,1,2,9,-1,2,3,10,-1,3,4,11,-1,4,5,12,-1,5,6,13,-1,8,7,15,-1,7,1,9,-1,9,15,7,-1,15,14,8,-1,13,16,5,-1,16,12,5,-1,12,11,4,-1,11,10,3,-1,10,9,2,-1,12,16,20,-1,13,14,22,-1,14,15,23,-1,24,23,15,-1,23,22,14,-1,20,19,12,-1,17,18,26,-1,18,19,27,-1,19,20,27,-1,20,21,28,-1,22,23,29,-1,30,29,23,-1,27,26,18,-1,26,25,17,-1,30,31,25,-1,25,26,29,-1,25,29,30,-1,26,27,28,-1,26,28,29,-1,27,20,28,-1,24,15,9,-1,22,21,13,-1,29,28,22,-1,28,21,22,-1,24,31,23,-1,31,30,23,-1,25,31,17,-1,31,24,17,-1,17,24,10,-1,24,9,10,-1,18,10,11,-1,18,17,10,-1,18,12,19,-1,18,11,12,-1,21,20,13,-1,20,16,13,-1,14,13,8,-1,13,6,8,-1]
IndexedFaceSet161.creaseAngle = 1.61
Coordinate162 = x3d.Coordinate()
Coordinate162.point = (-0.0969,0.8040,-0.0486,-0.1010,0.8760,0.0336,-0.1700,0.8940,-0.0078,-0.1700,0.8910,-0.0760,-0.1240,0.8580,-0.1290,-0.0760,0.8430,-0.1430,-0.0250,0.8190,-0.0889,-0.0507,0.8470,0.0196,-0.0035,0.8260,-0.0287,-0.0991,0.8080,0.0406,-0.1610,0.8140,-0.0019,-0.1650,0.8080,-0.0755,-0.1220,0.7880,-0.1260,-0.0099,0.7620,-0.0937,-0.0099,0.7620,-0.0309,-0.0491,0.7770,0.0185,-0.0755,0.7660,-0.1390,-0.1300,0.5970,-0.0062,-0.1320,0.6000,-0.0593,-0.1080,0.6030,-0.1050,-0.0722,0.6010,-0.1180,-0.0314,0.5900,-0.0953,-0.0239,0.5660,-0.0427,-0.0470,0.5660,0.0051,-0.0878,0.5810,0.0217,-0.1140,0.4990,-0.0132,-0.1160,0.4880,-0.0610,-0.1030,0.5670,-0.0991,-0.0362,0.5570,-0.0926,-0.0250,0.4860,-0.0470,-0.0507,0.4970,-0.0019,-0.0862,0.5130,0.0180)

IndexedFaceSet161.coord = Coordinate162

Shape158.geometry = IndexedFaceSet161

fieldValue157.children.append(Shape158)

ProtoInstance155.fieldValue.append(fieldValue157)

fieldValue154.children.append(ProtoInstance155)
ProtoInstance163 = x3d.ProtoInstance()
ProtoInstance163.name = "Joint"
ProtoInstance163.DEF = "hanim_r_knee"
fieldValue164 = x3d.fieldValue()
fieldValue164.name = "name"
fieldValue164.value = "r_knee"

ProtoInstance163.fieldValue.append(fieldValue164)
fieldValue165 = x3d.fieldValue()
fieldValue165.name = "center"
fieldValue165.value = "-0.0699 0.51 -0.0166"

ProtoInstance163.fieldValue.append(fieldValue165)
fieldValue166 = x3d.fieldValue()
fieldValue166.name = "children"
ProtoInstance167 = x3d.ProtoInstance()
ProtoInstance167.name = "Segment"
ProtoInstance167.DEF = "hanim_r_calf"
fieldValue168 = x3d.fieldValue()
fieldValue168.name = "name"
fieldValue168.value = "r_calf"

ProtoInstance167.fieldValue.append(fieldValue168)
fieldValue169 = x3d.fieldValue()
fieldValue169.name = "children"
Shape170 = x3d.Shape()
Appearance171 = x3d.Appearance()
Material172 = x3d.Material()
Material172.USE = "Pants_Color"

Appearance171.material = Material172

Shape170.appearance = Appearance171
IndexedFaceSet173 = x3d.IndexedFaceSet()
IndexedFaceSet173.coordIndex = [14,25,18,-1,25,32,18,-1,32,27,18,-1,27,22,18,-1,22,10,18,-1,10,6,18,-1,6,8,18,-1,8,14,18,-1,14,8,17,-1,6,10,9,-1,10,22,24,-1,22,27,39,-1,27,32,39,-1,32,25,42,-1,25,14,30,-1,17,30,14,-1,30,42,25,-1,42,39,32,-1,39,24,22,-1,24,9,10,-1,4,17,8,-1,39,42,43,-1,30,43,42,-1,17,4,1,-1,24,39,26,-1,39,43,44,-1,30,17,34,-1,16,34,17,-1,34,43,30,-1,44,26,39,-1,0,1,4,-1,1,16,17,-1,16,1,3,-1,1,0,2,-1,0,5,7,-1,5,26,28,-1,26,44,45,-1,44,43,46,-1,43,34,36,-1,34,16,15,-1,15,36,34,-1,36,46,43,-1,46,45,44,-1,45,28,26,-1,28,7,5,-1,7,2,0,-1,2,3,1,-1,3,15,16,-1,45,46,37,-1,36,15,20,-1,36,37,46,-1,13,2,7,-1,3,20,15,-1,3,2,13,-1,36,20,29,-1,29,37,36,-1,13,21,23,-1,21,33,23,-1,41,37,40,-1,37,29,31,-1,29,20,19,-1,19,31,29,-1,31,40,37,-1,40,38,41,-1,35,23,33,-1,23,12,13,-1,12,11,13,-1,31,19,11,-1,40,31,11,-1,40,11,12,-1,12,23,38,-1,12,38,40,-1,23,35,38,-1,28,21,7,-1,21,13,7,-1,45,33,28,-1,33,21,28,-1,33,45,41,-1,45,37,41,-1,33,41,35,-1,41,38,35,-1,20,3,47,-1,11,19,47,-1,19,20,47,-1,13,47,3,-1,13,11,47,-1,4,8,6,-1,26,5,24,-1,5,9,24,-1,6,9,4,-1,9,0,4,-1,9,5,0,-1]
IndexedFaceSet173.creaseAngle = 1.57
Coordinate174 = x3d.Coordinate()
Coordinate174.point = (-0.1230,0.3630,-0.0663,-0.1230,0.3630,-0.0400,-0.1180,0.3090,-0.0685,-0.1180,0.3110,-0.0411,-0.1170,0.5080,-0.0169,-0.1070,0.3670,-0.1070,-0.1050,0.5390,-0.0438,-0.1050,0.3100,-0.1080,-0.1040,0.5390,-0.0223,-0.1010,0.5100,-0.0798,-0.0975,0.5400,-0.0647,-0.0948,0.0897,-0.0368,-0.0916,0.0779,-0.0604,-0.0905,0.1200,-0.0647,-0.0883,0.5320,-0.0035,-0.0883,0.3090,-0.0180,-0.0878,0.3610,-0.0126,-0.0862,0.5060,0.0158,-0.0814,0.5500,-0.0395,-0.0765,0.1100,-0.0169,-0.0744,0.1300,-0.0212,-0.0738,0.1170,-0.0814,-0.0722,0.5460,-0.0717,-0.0717,0.0854,-0.0765,-0.0706,0.5100,-0.1010,-0.0609,0.5330,-0.0083,-0.0588,0.3650,-0.1220,-0.0577,0.5440,-0.0577,-0.0572,0.3080,-0.1230,-0.0561,0.1300,-0.0245,-0.0556,0.5060,-0.0003,-0.0540,0.0972,-0.0175,-0.0529,0.5360,-0.0368,-0.0529,0.1210,-0.0873,-0.0497,0.3580,-0.0234,-0.0486,0.0999,-0.0835,-0.0475,0.3070,-0.0282,-0.0416,0.1240,-0.0416,-0.0406,0.0918,-0.0626,-0.0406,0.5130,-0.0744,-0.0384,0.0881,-0.0363,-0.0373,0.1210,-0.0636,-0.0368,0.5100,-0.0357,-0.0239,0.3580,-0.0475,-0.0228,0.3580,-0.0926,-0.0201,0.3090,-0.0937,-0.0191,0.3110,-0.0508,-0.0985,0.1250,-0.0375)

IndexedFaceSet173.coord = Coordinate174

Shape170.geometry = IndexedFaceSet173

fieldValue169.children.append(Shape170)

ProtoInstance167.fieldValue.append(fieldValue169)

fieldValue166.children.append(ProtoInstance167)
ProtoInstance175 = x3d.ProtoInstance()
ProtoInstance175.name = "Joint"
ProtoInstance175.DEF = "hanim_r_ankle"
fieldValue176 = x3d.fieldValue()
fieldValue176.name = "name"
fieldValue176.value = "r_ankle"

ProtoInstance175.fieldValue.append(fieldValue176)
fieldValue177 = x3d.fieldValue()
fieldValue177.name = "center"
fieldValue177.value = "-0.064 0.0753 -0.0412"

ProtoInstance175.fieldValue.append(fieldValue177)
fieldValue178 = x3d.fieldValue()
fieldValue178.name = "children"
ProtoInstance179 = x3d.ProtoInstance()
ProtoInstance179.name = "Segment"
ProtoInstance179.DEF = "hanim_r_hindfoot"
fieldValue180 = x3d.fieldValue()
fieldValue180.name = "name"
fieldValue180.value = "r_hindfoot"

ProtoInstance179.fieldValue.append(fieldValue180)
fieldValue181 = x3d.fieldValue()
fieldValue181.name = "children"
Shape182 = x3d.Shape()
Appearance183 = x3d.Appearance()
Material184 = x3d.Material()
Material184.USE = "Shoe_Color"

Appearance183.material = Material184

Shape182.appearance = Appearance183
IndexedFaceSet185 = x3d.IndexedFaceSet()
IndexedFaceSet185.coordIndex = [6,50,0,-1,50,8,7,-1,50,7,0,-1,1,9,8,-1,1,8,50,-1,49,10,9,-1,49,9,1,-1,46,11,10,-1,46,10,49,-1,2,12,11,-1,2,11,46,-1,3,13,12,-1,3,12,2,-1,4,14,13,-1,4,13,3,-1,45,14,4,-1,47,15,45,-1,19,15,47,-1,48,18,19,-1,5,16,18,-1,5,18,48,-1,6,17,16,-1,6,16,5,-1,0,7,17,-1,0,17,6,-1,14,20,21,-1,14,21,13,-1,13,21,12,-1,12,21,22,-1,12,22,11,-1,11,22,10,-1,17,23,16,-1,16,23,24,-1,16,24,18,-1,18,24,25,-1,18,25,19,-1,19,25,26,-1,19,26,15,-1,15,26,20,-1,20,26,27,-1,20,27,21,-1,21,27,28,-1,21,28,22,-1,22,28,29,-1,10,30,9,-1,9,30,31,-1,9,31,8,-1,8,31,32,-1,17,32,23,-1,23,33,34,-1,23,34,35,-1,23,35,24,-1,24,35,36,-1,24,36,25,-1,25,36,37,-1,25,37,26,-1,26,37,38,-1,26,38,27,-1,27,38,39,-1,27,39,28,-1,28,39,40,-1,28,40,29,-1,29,40,41,-1,29,41,30,-1,30,41,42,-1,30,42,31,-1,31,42,43,-1,31,43,32,-1,32,43,33,-1,32,33,23,-1,44,43,42,-1,44,42,41,-1,44,41,40,-1,44,40,39,-1,44,39,38,-1,44,38,37,-1,44,37,36,-1,44,36,35,-1,44,35,34,-1,44,34,33,-1,44,33,43,-1,4,3,2,-1,45,4,2,-1,45,2,46,-1,47,45,46,-1,48,46,49,-1,5,48,49,-1,5,49,1,-1,6,5,1,-1,6,1,50,-1,30,10,29,-1,10,22,29,-1,17,7,32,-1,7,8,32,-1,19,47,48,-1,47,46,48,-1,20,14,15,-1,14,45,15,-1]
IndexedFaceSet185.creaseAngle = 1.57
Coordinate186 = x3d.Coordinate()
Coordinate186.point = (-0.0727,0.0000,-0.0994,-0.1000,0.0000,-0.0594,-0.0701,0.0000,0.1460,-0.0468,0.0000,0.1530,-0.0215,0.0000,0.1460,-0.0433,0.0000,-0.0534,-0.0529,0.0000,-0.0923,-0.0727,0.0219,-0.0994,-0.0863,0.0219,-0.0862,-0.1000,0.0219,-0.0594,-0.1080,0.0219,-0.0048,-0.1120,0.0156,0.1170,-0.0701,0.0156,0.1460,-0.0468,0.0156,0.1530,-0.0215,0.0156,0.1460,-0.0165,0.0170,0.0777,-0.0433,0.0219,-0.0534,-0.0529,0.0219,-0.0923,-0.0445,0.0273,-0.0189,-0.0265,0.0253,0.0549,-0.0305,0.0253,0.0938,-0.0690,0.0253,0.0938,-0.1020,0.0253,0.0707,-0.0568,0.0573,-0.0918,-0.0492,0.0573,-0.0497,-0.0424,0.0573,-0.0014,-0.0478,0.0573,0.0341,-0.0623,0.0573,0.0366,-0.0864,0.0573,0.0245,-0.0962,0.0573,-0.0121,-0.0845,0.0573,-0.0764,-0.0758,0.0573,-0.0899,-0.0676,0.0573,-0.0962,-0.0578,0.0953,-0.0896,-0.0489,0.0953,-0.0757,-0.0459,0.0953,-0.0615,-0.0435,0.0953,-0.0292,-0.0485,0.0953,-0.0058,-0.0624,0.0953,-0.0047,-0.0857,0.0953,-0.0134,-0.0953,0.0953,-0.0380,-0.0843,0.0953,-0.0803,-0.0761,0.0953,-0.0889,-0.0682,0.0953,-0.0929,-0.0675,0.1300,-0.0608,-0.0165,0.0000,0.1250,-0.1120,0.0000,0.1170,-0.0165,0.0000,0.0777,-0.0393,0.0000,-0.0129,-0.1080,0.0000,-0.0048,-0.0863,0.0000,-0.0862)

IndexedFaceSet185.coord = Coordinate186

Shape182.geometry = IndexedFaceSet185

fieldValue181.children.append(Shape182)
Transform187 = x3d.Transform()
Transform187.scale = [0.015,0.015,0.015]
Transform188 = x3d.Transform()
Transform188.rotation = [0,0,1,1.57]
Transform188.translation = [-5,-0.5,-7.5]
Shape189 = x3d.Shape()
Appearance190 = x3d.Appearance()
Material191 = x3d.Material()
Material191.diffuseColor = [0.753,1,0.243]

Appearance190.material = Material191

Shape189.appearance = Appearance190
Extrusion192 = x3d.Extrusion()
Extrusion192.DEF = "Finr"
Extrusion192.ccw = False
Extrusion192.creaseAngle = 3.14
Extrusion192.crossSection = [-1,0,-0.8,2,-0.7,3,0,5.2,0.7,3,0.8,2,1,0,0.8,-2,0.7,-3,0,-5.2,-0.7,-3,-0.8,-2,-1,0]
Extrusion192.scale = [0.25,0.25,0.5,0.75,0.5,1.2,0.5,1.35,0.5,1.35,0.5,1.35,0.5,1.35,0.5,1.35,0.5,1.35]
Extrusion192.spine = (0.0000,0.0000,1.0000,0.0000,0.0000,5.0000,0.0000,0.0000,8.0000,0.0000,0.0000,12.0000,0.0000,0.0000,15.0000,0.5000,0.0000,18.0000,1.5000,0.0000,25.0000,2.5000,0.0000,30.0000,4.0000,0.0000,34.0000)

Shape189.geometry = Extrusion192

Transform188.children.append(Shape189)

Transform187.children.append(Transform188)

fieldValue181.children.append(Transform187)

ProtoInstance179.fieldValue.append(fieldValue181)

fieldValue178.children.append(ProtoInstance179)

ProtoInstance175.fieldValue.append(fieldValue178)

fieldValue166.children.append(ProtoInstance175)

ProtoInstance163.fieldValue.append(fieldValue166)

fieldValue154.children.append(ProtoInstance163)

ProtoInstance151.fieldValue.append(fieldValue154)

fieldValue100.children.append(ProtoInstance151)

ProtoInstance97.fieldValue.append(fieldValue100)

fieldValue96.children.append(ProtoInstance97)
#Fins animation
ProximitySensor193 = x3d.ProximitySensor()
ProximitySensor193.DEF = "FinTriggerProximitySensor"
ProximitySensor193.size = [5,5,5]

fieldValue96.children.append(ProximitySensor193)
TimeSensor194 = x3d.TimeSensor()
TimeSensor194.DEF = "FinClock"
TimeSensor194.cycleInterval = 7
TimeSensor194.loop = True

fieldValue96.children.append(TimeSensor194)
Group195 = x3d.Group()
Script196 = x3d.Script()
Script196.DEF = "FinScript"
field197 = x3d.field()
field197.name = "keyValueR"
field197.accessType = "outputOnly"
field197.type = "MFVec3f"

Script196.field.append(field197)
field198 = x3d.field()
field198.name = "keyValueL"
field198.accessType = "outputOnly"
field198.type = "MFVec3f"

Script196.field.append(field198)
field199 = x3d.field()
field199.name = "set_fraction"
field199.accessType = "inputOnly"
field199.type = "SFFloat"

Script196.field.append(field199)
field200 = x3d.field()
field200.name = "finL"
field200.accessType = "inputOnly"
field200.type = "SFBool"

Script196.field.append(field200)
field201 = x3d.field()
field201.name = "finR"
field201.accessType = "inputOnly"
field201.type = "SFBool"

Script196.field.append(field201)
field202 = x3d.field()
field202.name = "traceEnabled"
field202.accessType = "initializeOnly"
field202.type = "SFBool"
field202.value = True

Script196.field.append(field202)

Script196.sourceCode = '''ecmascript:\n"+
"\n"+
"var finWarpL;\n"+
"var finWarpR;\n"+
"\n"+
"function initialize ()\n"+
"{\n"+
"	finWarpL = 0;\n"+
"	finWarpR = 0;\n"+
"}\n"+
"\n"+
"function finL(value, timeStamp)\n"+
"{\n"+
"	if (value == 0)\n"+
"	{\n"+
"		finWarpL = 0;\n"+
"	}\n"+
"	else\n"+
"	{\n"+
"		finWarpL = 1;\n"+
"	}\n"+
"	//print ('finWarpL' + finWarpL);\n"+
"}			 \n"+
"\n"+
"function finR(value, timeStamp)\n"+
"{\n"+
"	if (value == 0)\n"+
"	{\n"+
"		finWarpR = 0;\n"+
"	}\n"+
"	else\n"+
"	{\n"+
"		finWarpR = 1;\n"+
"	}\n"+
"	//print ('finWarpR' + finWarpR);\n"+
"}\n"+
"function finMove(fraction, timeStamp)\n"+
" {  	\n"+
"	if (finWarpL == 1)\n"+
"	{\n"+
"		// level 3 (warp outside) Left					\n"+
"		kVL7 = new SFVec3f(1.25, 0, 25);  \n"+
"     		kVL8 = new SFVec3f(2.5, 0, 30);\n"+
"      		kVL9 = new SFVec3f(3.25, 0, 34);			\n"+
"	}	\n"+
"	else \n"+
"	{		\n"+
"		// level -2 (warp inside) Left					\n"+
"		kVL7 = new SFVec3f(-1.25, 0, 25);  \n"+
"     		kVL8 = new SFVec3f(-2.5, 0, 30);\n"+
"      		kVL9 = new SFVec3f(-3.25, 0, 34);	\n"+
"	}\n"+
"\n"+
"	if (finWarpR == 0)\n"+
"	{		\n"+
"		// level  1 (warp outside ) Right    			\n"+
"		kVR7 = new SFVec3f(1.25, 0, 25);  \n"+
"     		kVR8 = new SFVec3f(2.5, 0, 30);\n"+
"      		kVR9 = new SFVec3f(3.25, 0, 34);	  	\n"+
"	\n"+
"	}	\n"+
"	else \n"+
"	{		\n"+
"		// level  -2 ( warp inside) Right      				\n"+
"		kVR7 = new SFVec3f(-1.25, 0, 25);  \n"+
"     		kVR8 = new SFVec3f(-2.5, 0, 30);\n"+
"      		kVR9 = new SFVec3f(-3.25, 0, 34);\n"+
"	}\n"+
"\n"+
"	// Left Fin (fixed spine)\n"+
"	kVL1 = new SFVec3f(0, 0, 1);  \n"+
"     	kVL2 = new SFVec3f(0, 0, 5);\n"+
"      	kVL3 = new SFVec3f(0, 0, 8);\n"+
"	kVL4 = new SFVec3f(0, 0, 12); \n"+
"	kVL5 = new SFVec3f(0, 0, 15); 	\n"+
"	kVL6 = new SFVec3f(0, 0, 18);			\n"+
"      	keyValueL = new MFVec3f(kVL1, kVL2, kVL3, kVL4, kVL5, kVL6, kVL7, kVL8, kVL9);  \n"+
"	\n"+
"	// Right Fin (fixed spine)\n"+
"	kVR1 = new SFVec3f(0, 0, 1);  \n"+
"     	kVR2 = new SFVec3f(0, 0, 5);\n"+
"      	kVR3 = new SFVec3f(0, 0, 8);\n"+
"	kVR4 = new SFVec3f(0, 0, 12);  	\n"+
"	kVR5 = new SFVec3f(0, 0, 15);\n"+
"	kVR6 = new SFVec3f(0, 0, 18);			\n"+
"      	keyValueR = new MFVec3f(kVR1, kVR2, kVR3, kVR4, kVR5, kVR6, kVR7, kVR8, kVR9);  \n"+
"      	\n"+
"	//tracePrint ('[keyValueL = ]' + keyValueL);     \n"+
"	//tracePrint ('[keyValueR = ]' + keyValueR);     \n"+
"			\n"+
"}\n"+
"\n"+
"function set_fraction (value, timeStamp)\n"+
"{\n"+
"	finMove(value);\n"+
"	//tracePrint('time fraction =' + value);\n"+
"	\n"+
"}\n"+
"\n"+
"function tracePrint (outputString)\n"+
"{\n"+
"	if (traceEnabled) Browser.print ('[Fin Move]' + outputString);\n"+
"}'''

Group195.children.append(Script196)
ROUTE203 = x3d.ROUTE()
ROUTE203.fromField = "isActive"
ROUTE203.fromNode = "FinTriggerProximitySensor"
ROUTE203.toField = "enabled"
ROUTE203.toNode = "FinClock"

Group195.children.append(ROUTE203)
ROUTE204 = x3d.ROUTE()
ROUTE204.fromField = "fraction_changed"
ROUTE204.fromNode = "FinClock"
ROUTE204.toField = "set_fraction"
ROUTE204.toNode = "FinScript"

Group195.children.append(ROUTE204)
ROUTE205 = x3d.ROUTE()
ROUTE205.fromField = "keyValueR"
ROUTE205.fromNode = "FinScript"
ROUTE205.toField = "set_spine"
ROUTE205.toNode = "Finr"

Group195.children.append(ROUTE205)
ROUTE206 = x3d.ROUTE()
ROUTE206.fromField = "keyValueL"
ROUTE206.fromNode = "FinScript"
ROUTE206.toField = "set_spine"
ROUTE206.toNode = "Finl"

Group195.children.append(ROUTE206)

fieldValue96.children.append(Group195)
ProtoInstance207 = x3d.ProtoInstance()
ProtoInstance207.name = "Joint"
ProtoInstance207.DEF = "hanim_vl1"
fieldValue208 = x3d.fieldValue()
fieldValue208.name = "name"
fieldValue208.value = "vl1"

ProtoInstance207.fieldValue.append(fieldValue208)
fieldValue209 = x3d.fieldValue()
fieldValue209.name = "center"
fieldValue209.value = "-0.00405 1.07 -0.0275"

ProtoInstance207.fieldValue.append(fieldValue209)
fieldValue210 = x3d.fieldValue()
fieldValue210.name = "children"
ProtoInstance211 = x3d.ProtoInstance()
ProtoInstance211.name = "Segment"
ProtoInstance211.DEF = "hanim_c7"
fieldValue212 = x3d.fieldValue()
fieldValue212.name = "name"
fieldValue212.value = "l1"

ProtoInstance211.fieldValue.append(fieldValue212)
fieldValue213 = x3d.fieldValue()
fieldValue213.name = "children"
Transform214 = x3d.Transform()
Transform214.scale = [1.05,1.05,1.05]
Transform214.translation = [0,-0.09,0]
Shape215 = x3d.Shape()
Appearance216 = x3d.Appearance()
Material217 = x3d.Material()
Material217.DEF = "WetShirtColor"
Material217.ambientIntensity = 0.25
Material217.diffuseColor = [0,0,0.502]

Appearance216.material = Material217
ImageTexture218 = x3d.ImageTexture()
ImageTexture218.DEF = "small_logo_Tex"
ImageTexture218.url = ["small_logo.gif","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Prototypes/small_logo.gif"]

Appearance216.texture = ImageTexture218

Shape215.appearance = Appearance216
IndexedFaceSet219 = x3d.IndexedFaceSet()
IndexedFaceSet219.coordIndex = [0,1,2,-1,3,0,2,-1,4,5,6,-1,6,7,4,-1,8,7,6,-1,6,9,8,-1,9,10,8,-1,6,5,11,-1,9,6,12,-1,11,12,6,-1,12,10,9,-1,7,8,13,-1,13,4,7,-1,14,15,16,-1,15,17,13,-1,4,13,17,-1,17,15,18,-1,13,19,15,-1,19,13,8,-1,19,16,15,-1,16,19,8,-1,17,20,4,-1,5,4,20,-1,18,21,17,-1,20,17,21,-1,16,22,14,-1,22,16,23,-1,8,23,16,-1,23,8,10,-1,24,25,26,-1,26,27,24,-1,25,28,26,-1,28,29,30,-1,30,26,28,-1,31,32,33,-1,32,25,33,-1,25,24,34,-1,33,25,34,-1,24,35,34,-1,27,35,24,-1,33,36,31,-1,27,26,37,-1,37,26,30,-1,38,37,30,-1,33,34,39,-1,39,34,35,-1,39,35,40,-1,41,38,30,-1,35,27,42,-1,37,42,27,-1,40,35,42,-1,42,37,43,-1,37,38,44,-1,44,43,37,-1,36,45,46,-1,36,33,45,-1,40,42,47,-1,43,47,42,-1,47,48,40,-1,39,40,48,-1,47,43,49,-1,43,44,49,-1,50,49,44,-1,51,46,52,-1,46,45,52,-1,52,45,53,-1,33,53,45,-1,33,39,53,-1,49,54,47,-1,48,47,54,-1,55,56,52,-1,57,52,53,-1,57,55,52,-1,58,57,53,-1,59,58,53,-1,53,39,59,-1,39,48,59,-1,59,48,54,-1,58,59,60,-1,54,49,61,-1,59,54,61,-1,60,59,61,-1,49,50,62,-1,63,62,50,-1,62,61,49,-1,64,63,50,-1,63,64,65,-1,65,62,63,-1,66,60,61,-1,62,65,67,-1,68,67,65,-1,64,69,70,-1,64,70,65,-1,70,68,65,-1,69,71,72,-1,72,70,69,-1,73,74,75,-1,66,76,60,-1,67,77,62,-1,62,77,61,-1,77,66,61,-1,66,77,78,-1,77,67,79,-1,79,67,68,-1,79,78,77,-1,68,70,80,-1,70,72,80,-1,80,79,68,-1,74,73,81,-1,73,76,82,-1,82,81,73,-1,76,66,83,-1,78,83,66,-1,83,82,76,-1,78,79,84,-1,79,80,84,-1,84,85,78,-1,86,84,80,-1,81,82,87,-1,87,88,81,-1,82,83,89,-1,83,78,89,-1,89,87,82,-1,78,85,89,-1,90,91,92,-1,92,93,90,-1,90,94,91,-1,95,96,94,-1,94,90,95,-1,29,96,97,-1,96,95,97,-1,97,30,29,-1,30,97,41,-1,41,97,95,-1,98,99,100,-1,98,91,99,-1,101,92,91,-1,98,101,91,-1,101,102,92,-1,92,102,93,-1,36,103,31,-1,51,103,36,46,-1,103,100,31,-1,100,103,98,-1,104,90,93,-1,90,104,95,-1,95,105,41,-1,104,105,95,-1,106,101,98,-1,102,101,106,-1,107,93,102,-1,93,107,104,-1,108,104,107,-1,107,109,108,-1,110,105,104,-1,104,108,110,-1,109,107,111,-1,107,102,111,-1,111,102,106,-1,111,112,109,-1,106,112,111,-1,113,110,108,-1,110,113,114,-1,51,52,115,-1,116,115,117,-1,117,106,116,-1,118,109,112,-1,119,108,109,-1,108,119,113,-1,109,118,119,-1,120,113,119,-1,119,121,120,-1,52,56,122,-1,122,115,52,-1,115,122,123,-1,117,124,125,-1,106,117,125,-1,118,112,106,125,-1,119,118,125,-1,121,119,125,-1,126,124,123,-1,127,114,113,-1,114,127,128,-1,113,120,127,-1,114,128,129,-1,130,126,123,-1,122,130,123,-1,131,120,121,-1,131,127,120,-1,132,129,128,-1,128,127,132,-1,74,81,133,-1,81,134,133,-1,121,135,131,-1,136,132,127,-1,132,136,137,-1,138,71,129,-1,138,129,132,-1,137,138,132,-1,139,72,71,-1,72,139,80,-1,71,138,139,-1,140,135,121,-1,140,121,125,-1,141,127,131,-1,127,141,136,-1,131,135,141,-1,142,141,135,-1,143,136,141,-1,136,143,137,-1,141,142,143,-1,144,138,137,-1,144,139,138,-1,143,144,137,-1,145,146,134,-1,145,140,146,-1,134,81,145,-1,147,135,140,-1,135,147,142,-1,140,145,147,-1,148,80,139,-1,80,148,86,-1,139,144,148,-1,149,143,142,-1,149,144,143,-1,142,150,149,-1,151,148,144,-1,144,149,151,-1,152,145,81,-1,81,88,152,-1,153,147,145,-1,153,142,147,-1,145,152,153,-1,153,150,142,-1,154,86,148,-1,148,151,154,-1,155,28,25,-1,155,29,28,-1,155,25,32,-1,155,32,31,-1,155,31,100,-1,155,100,99,-1,155,99,91,-1,155,91,94,-1,155,94,96,-1,155,96,29,-1,156,151,149,-1,156,154,151,-1,156,149,150,-1,156,150,153,-1,156,153,152,-1,156,152,88,-1,156,88,87,-1,156,87,89,-1,156,89,85,-1,156,85,84,-1,156,84,86,-1,156,86,154,-1,76,157,60,-1,76,73,158,157,-1,159,158,73,75,160,-1,161,56,55,-1,60,162,58,-1,162,60,157,-1,161,55,163,-1,57,164,163,55,-1,160,163,164,-1,160,164,159,-1,164,57,165,-1,164,165,159,-1,57,58,166,165,-1,166,58,162,-1,165,166,159,-1,166,162,157,158,159,-1,140,125,167,-1,124,168,125,-1,168,167,125,-1,124,169,168,-1,146,140,167,170,-1,168,170,167,-1,168,169,170,-1,146,170,171,-1,169,171,170,-1,172,134,146,171,-1,134,172,130,-1,169,124,126,173,-1,173,126,130,-1,169,173,172,171,-1,173,130,172,-1,122,74,133,174,-1,133,134,174,-1,130,122,174,-1,134,130,174,-1,122,56,175,74,-1,74,175,176,-1,175,56,161,176,-1,74,176,75,-1,176,161,163,-1,176,160,75,-1,176,163,160,-1,115,116,177,51,-1,106,98,177,116,-1,51,177,103,-1,177,98,103,-1]
IndexedFaceSet219.creaseAngle = 1.59
Coordinate220 = x3d.Coordinate()
Coordinate220.point = (0.0430,1.2500,0.0614,0.1010,1.2500,0.0614,0.1030,1.3100,0.0195,0.0210,1.3200,0.0276,0.0572,1.2700,-0.1530,0.0524,1.1500,-0.1340,0.0000,1.1900,-0.1400,0.0000,1.2600,-0.1470,-0.0572,1.2700,-0.1530,-0.0228,1.1800,-0.1400,-0.0524,1.1500,-0.1340,0.0000,1.1300,-0.1260,-0.0228,1.1300,-0.1240,0.0000,1.3100,-0.1460,-0.0545,1.3500,-0.1380,0.0000,1.3500,-0.1360,-0.0593,1.3000,-0.1510,0.0593,1.3000,-0.1510,0.0545,1.3500,-0.1380,-0.0255,1.3000,-0.1460,0.0975,1.2600,-0.1500,0.1000,1.3000,-0.1480,-0.1000,1.3000,-0.1480,-0.0975,1.2600,-0.1500,-0.1170,1.4100,-0.0395,-0.0674,1.4500,-0.0314,-0.0926,1.4100,-0.0937,-0.1240,1.4000,-0.0706,-0.0583,1.4400,-0.0615,-0.0228,1.4600,-0.0872,-0.0534,1.4200,-0.1120,-0.0228,1.4200,0.0035,-0.0593,1.4300,-0.0185,-0.0787,1.3900,-0.0029,-0.1120,1.4000,-0.0131,-0.1640,1.3900,-0.0373,-0.0153,1.3900,0.0159,-0.0953,1.3500,-0.1360,-0.0545,1.3500,-0.1380,-0.1390,1.3400,0.0030,-0.1370,1.3400,-0.0368,0.0000,1.3500,-0.1360,-0.1560,1.3500,-0.0915,-0.1320,1.2900,-0.1270,-0.1000,1.3000,-0.1480,-0.0418,1.3500,0.0168,-0.0130,1.3700,0.0167,-0.1510,1.2800,-0.0878,-0.1360,1.3200,-0.0406,-0.1240,1.2600,-0.1250,-0.0975,1.2600,-0.1500,0.0023,1.3700,0.0167,-0.0096,1.3200,0.0276,-0.0918,1.3100,0.0195,-0.1410,1.2500,-0.0744,-0.0316,1.2500,0.0614,-0.0026,1.2500,0.0458,-0.0611,1.2500,0.0668,-0.0896,1.2500,0.0614,-0.1260,1.2400,0.0120,-0.1260,1.2200,0.0141,-0.1290,1.1700,-0.0523,-0.1150,1.1600,-0.1050,-0.0851,1.1800,-0.1340,-0.0524,1.1500,-0.1340,-0.0830,1.1300,-0.1220,-0.1170,1.1500,-0.0180,-0.1100,1.1000,-0.0846,-0.0808,1.1000,-0.1110,-0.0228,1.1300,-0.1240,-0.0524,1.1000,-0.1190,0.0000,1.1300,-0.1260,-0.0228,1.1000,-0.1160,-0.0563,1.1500,0.0377,-0.0048,1.1800,0.0458,-0.0343,1.1800,0.0485,-0.0966,1.1500,-0.0041,-0.1200,1.1000,-0.0373,-0.1210,1.0700,-0.0356,-0.1060,1.0700,-0.0711,-0.0475,1.0600,-0.1050,0.0000,1.0800,0.0556,-0.0787,1.0800,0.0347,-0.1030,1.0800,0.0030,-0.0975,1.0100,-0.0873,-0.1340,0.9980,-0.0314,-0.0475,1.0200,-0.1090,-0.0325,1.0200,0.0529,0.0000,1.0200,0.0422,-0.0975,1.0200,0.0132,0.0926,1.4100,-0.0937,0.0674,1.4500,-0.0314,0.1170,1.4100,-0.0395,0.1240,1.4000,-0.0706,0.0583,1.4400,-0.0615,0.0534,1.4200,-0.1120,0.0228,1.4600,-0.0872,0.0000,1.4000,-0.1120,0.0787,1.3900,-0.0029,0.0593,1.4300,-0.0185,0.0228,1.4200,0.0035,0.1120,1.4000,-0.0131,0.1640,1.3900,-0.0373,0.0153,1.3900,0.0159,0.0953,1.3500,-0.1360,0.0545,1.3500,-0.1380,0.1390,1.3400,0.0030,0.1560,1.3500,-0.0915,0.1320,1.2900,-0.1270,0.1510,1.2800,-0.0878,0.1000,1.3000,-0.1480,0.1370,1.3400,-0.0368,0.1470,1.3200,-0.0406,0.1240,1.2600,-0.1250,0.0975,1.2600,-0.1500,0.0210,1.3200,0.0276,0.0532,1.3500,0.0168,0.1030,1.3100,0.0195,0.1350,1.2900,-0.0406,0.1410,1.2500,-0.0744,0.1320,1.1800,-0.0830,0.1340,1.1900,-0.0572,0.0140,1.2500,0.0458,0.0430,1.2500,0.0614,0.1010,1.2500,0.0614,0.1380,1.2400,0.0120,0.0650,1.2300,0.0743,0.1150,1.1600,-0.1050,0.0851,1.1800,-0.1340,0.0524,1.1500,-0.1340,0.0430,1.2000,0.0641,0.1270,1.1400,-0.0427,0.0830,1.1300,-0.1220,0.0162,1.1800,0.0458,0.0457,1.1800,0.0485,0.1170,1.1500,-0.0180,0.1100,1.1000,-0.0846,0.0808,1.1000,-0.1110,0.0524,1.1000,-0.1190,0.0228,1.1000,-0.1160,0.1080,1.1500,-0.0041,0.1200,1.1000,-0.0373,0.1210,1.0700,-0.0356,0.1060,1.0700,-0.0711,0.0475,1.0600,-0.1050,0.0787,1.0800,0.0347,0.0844,1.1500,0.0297,0.1030,1.0800,0.0030,0.0000,1.0700,-0.1100,0.0975,1.0100,-0.0873,0.1340,0.9980,-0.0475,0.0475,1.0200,-0.1090,0.0325,1.0200,0.0529,0.0975,1.0200,0.0132,0.0000,1.0200,-0.1170,0.0000,1.4400,-0.0389,0.0000,1.0100,-0.0259,-0.1040,1.1900,0.0423,-0.0778,1.1900,0.0642,-0.0780,1.1900,0.0644,-0.0493,1.2000,0.0664,-0.0281,1.2200,0.0587,-0.1040,1.2000,0.0568,-0.0484,1.2100,0.0692,-0.0549,1.2100,0.0708,-0.0806,1.2100,0.0713,-0.0852,1.2100,0.0703,0.1160,1.1900,0.0430,0.1140,1.2100,0.0572,0.0967,1.2100,0.0701,0.1100,1.1900,0.0502,0.0930,1.1900,0.0622,0.0832,1.1900,0.0662,0.0863,1.2100,0.0728,0.0154,1.2100,0.0458,-0.0039,1.2100,0.0458,-0.0145,1.2000,0.0512,0.0534,1.3500,0.0168)

IndexedFaceSet219.coord = Coordinate220
TextureCoordinate221 = x3d.TextureCoordinate()
TextureCoordinate221.point = [0.1611,-0.02056,0.9468,-0.02056,0.9739,0.9344,-0.137,1.094,0.1973,0.6424,0.2231,0.04876,0.5054,0.2466,0.5054,0.5929,0.8135,0.6424,0.6282,0.1972,0.7876,0.04876,0.5054,-0.05018,0.6282,-0.05018,0.5054,0.8403,0.7989,1.038,0.5054,1.038,0.8248,0.7908,0.186,0.7908,0.2118,1.038,0.6427,0.7908,-0.01977,0.5929,-0.03324,0.7908,1.044,0.7908,1.031,0.5929,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

IndexedFaceSet219.texCoord.append(TextureCoordinate221)

Shape215.geometry = IndexedFaceSet219

Transform214.children.append(Shape215)

fieldValue213.children.append(Transform214)
#<Transform DEF='Imaf3D'> <Shape> <Appearance> <Material/> <ImageTexture/> </Appearance> <IndexedFaceSet> <Coordinate/> <TextureCoordinate/> </IndexedFaceSet> </Shape> </Transform>
Transform222 = x3d.Transform()
Transform222.scale = [1.25,1.1,1.3]
Transform222.translation = [0,1.18,0.015]
Group223 = x3d.Group()
Transform224 = x3d.Transform()
Transform224.translation = [0,-1.2,0]
Shape225 = x3d.Shape()
Appearance226 = x3d.Appearance()
Material227 = x3d.Material()
Material227.DEF = "BCLColor"
Material227.ambientIntensity = 0.25
Material227.diffuseColor = [0.0588,0.0588,0.0588]
Material227.shininess = 0.5

Appearance226.material = Material227

Shape225.appearance = Appearance226
IndexedFaceSet228 = x3d.IndexedFaceSet()
IndexedFaceSet228.coordIndex = [4,5,6,-1,6,7,4,-1,8,7,6,-1,6,9,8,-1,9,10,8,-1,6,5,11,-1,9,6,12,-1,11,12,6,-1,12,10,9,-1,7,8,13,-1,13,4,7,-1,14,15,16,-1,15,17,13,-1,4,13,17,-1,17,15,18,-1,13,19,15,-1,19,13,8,-1,19,16,15,-1,16,19,8,-1,17,20,4,-1,5,4,20,-1,18,21,17,-1,20,17,21,-1,16,22,14,-1,22,16,23,-1,8,23,16,-1,23,8,10,-1,24,25,26,-1,26,27,24,-1,25,28,26,-1,28,29,30,-1,30,26,28,-1,25,24,34,-1,33,25,34,-1,24,35,34,-1,27,35,24,-1,27,26,37,-1,37,26,30,-1,38,37,30,-1,33,34,39,-1,39,34,35,-1,41,38,30,-1,35,27,42,-1,37,42,27,-1,42,37,43,-1,37,38,44,-1,44,43,37,-1,43,47,42,-1,47,43,49,-1,43,44,49,-1,50,49,44,-1,33,39,53,-1,49,54,47,-1,59,58,53,-1,53,39,59,-1,58,59,60,-1,54,49,61,-1,49,50,62,-1,63,62,50,-1,62,61,49,-1,64,63,50,-1,63,64,65,-1,65,62,63,-1,66,60,61,-1,62,65,67,-1,68,67,65,-1,64,69,70,-1,64,70,65,-1,70,68,65,-1,69,71,72,-1,72,70,69,-1,66,76,60,-1,67,77,62,-1,62,77,61,-1,77,66,61,-1,66,77,78,-1,77,67,79,-1,79,67,68,-1,79,78,77,-1,68,70,80,-1,70,72,80,-1,80,79,68,-1,73,76,82,-1,76,66,83,-1,78,83,66,-1,83,82,76,-1,78,79,84,-1,79,80,84,-1,84,85,78,-1,86,84,80,-1,82,83,89,-1,83,78,89,-1,89,87,82,-1,78,85,89,-1,90,91,92,-1,92,93,90,-1,90,94,91,-1,95,96,94,-1,94,90,95,-1,29,96,97,-1,96,95,97,-1,97,30,29,-1,30,97,41,-1,41,97,95,-1,101,92,91,-1,98,101,91,-1,101,102,92,-1,92,102,93,-1,104,90,93,-1,90,104,95,-1,95,105,41,-1,104,105,95,-1,106,101,98,-1,102,101,106,-1,107,93,102,-1,93,107,104,-1,108,104,107,-1,107,109,108,-1,110,105,104,-1,104,108,110,-1,113,110,108,-1,110,113,114,-1,119,108,109,-1,108,119,113,-1,120,113,119,-1,119,121,120,-1,117,124,125,-1,106,117,125,-1,127,114,113,-1,114,127,128,-1,113,120,127,-1,114,128,129,-1,131,120,121,-1,131,127,120,-1,132,129,128,-1,128,127,132,-1,121,135,131,-1,136,132,127,-1,132,136,137,-1,138,71,129,-1,138,129,132,-1,137,138,132,-1,139,72,71,-1,72,139,80,-1,71,138,139,-1,140,135,121,-1,140,121,125,-1,141,127,131,-1,127,141,136,-1,131,135,141,-1,142,141,135,-1,143,136,141,-1,136,143,137,-1,141,142,143,-1,144,138,137,-1,144,139,138,-1,143,144,137,-1,145,140,146,-1,147,135,140,-1,135,147,142,-1,140,145,147,-1,148,80,139,-1,80,148,86,-1,139,144,148,-1,149,143,142,-1,149,144,143,-1,142,150,149,-1,151,148,144,-1,144,149,151,-1,153,147,145,-1,153,142,147,-1,145,152,153,-1,153,150,142,-1,154,86,148,-1,148,151,154,-1,76,157,60,-1,76,73,158,157,-1,60,162,58,-1,162,60,157,-1,166,58,162,-1,165,166,159,-1,166,162,157,158,159,-1,140,125,167,-1,124,168,125,-1,168,167,125,-1,124,169,168,-1,146,140,167,170,-1,168,170,167,-1,168,169,170,-1,146,170,171,-1,169,171,170,-1,98,117,106,-1]
IndexedFaceSet228.creaseAngle = 1.59
IndexedFaceSet228.solid = False
Coordinate229 = x3d.Coordinate()
Coordinate229.point = (0.0430,1.2500,0.0614,0.1010,1.2500,0.0614,0.1030,1.3100,0.0195,0.0210,1.3200,0.0276,0.0572,1.2700,-0.1530,0.0524,1.1500,-0.1340,0.0000,1.1900,-0.1400,0.0000,1.2600,-0.1470,-0.0572,1.2700,-0.1530,-0.0228,1.1800,-0.1400,-0.0524,1.1500,-0.1340,0.0000,1.1300,-0.1260,-0.0228,1.1300,-0.1240,0.0000,1.3100,-0.1460,-0.0545,1.3500,-0.1380,0.0000,1.3500,-0.1360,-0.0593,1.3000,-0.1510,0.0593,1.3000,-0.1510,0.0545,1.3500,-0.1380,-0.0255,1.3000,-0.1460,0.0975,1.2600,-0.1500,0.1000,1.3000,-0.1480,-0.1000,1.3000,-0.1480,-0.0975,1.2600,-0.1500,-0.1170,1.4100,-0.0395,-0.0674,1.4500,-0.0314,-0.0926,1.4100,-0.0937,-0.1240,1.4000,-0.0706,-0.0583,1.4400,-0.0615,-0.0228,1.4600,-0.0872,-0.0534,1.4200,-0.1120,-0.0228,1.4200,0.0035,-0.0593,1.4300,-0.0185,-0.0787,1.3900,-0.0029,-0.1120,1.4000,-0.0131,-0.1640,1.3900,-0.0373,-0.0153,1.3900,0.0159,-0.0953,1.3500,-0.1360,-0.0545,1.3500,-0.1380,-0.1390,1.3400,0.0030,-0.1370,1.3400,-0.0368,0.0000,1.3500,-0.1360,-0.1560,1.3500,-0.0915,-0.1320,1.2900,-0.1270,-0.1000,1.3000,-0.1480,-0.0418,1.3500,0.0168,-0.0130,1.3700,0.0167,-0.1510,1.2800,-0.0878,-0.1360,1.3200,-0.0406,-0.1240,1.2600,-0.1250,-0.0975,1.2600,-0.1500,0.0023,1.3700,0.0167,-0.0096,1.3200,0.0276,-0.0918,1.3100,0.0195,-0.1410,1.2500,-0.0744,-0.0316,1.2500,0.0614,-0.0026,1.2500,0.0458,-0.0611,1.2500,0.0668,-0.0896,1.2500,0.0614,-0.1260,1.2400,0.0120,-0.1260,1.2200,0.0141,-0.1290,1.1700,-0.0523,-0.1150,1.1600,-0.1050,-0.0851,1.1800,-0.1340,-0.0524,1.1500,-0.1340,-0.0830,1.1300,-0.1220,-0.1170,1.1500,-0.0180,-0.1100,1.1000,-0.0846,-0.0808,1.1000,-0.1110,-0.0228,1.1300,-0.1240,-0.0524,1.1000,-0.1190,0.0000,1.1300,-0.1260,-0.0228,1.1000,-0.1160,-0.0563,1.1500,0.0377,-0.0048,1.1800,0.0458,-0.0343,1.1800,0.0485,-0.0966,1.1500,-0.0041,-0.1200,1.1000,-0.0373,-0.1210,1.0700,-0.0356,-0.1060,1.0700,-0.0711,-0.0475,1.0600,-0.1050,0.0000,1.0800,0.0556,-0.0787,1.0800,0.0347,-0.1030,1.0800,0.0030,-0.0975,1.0100,-0.0873,-0.1340,0.9980,-0.0314,-0.0475,1.0200,-0.1090,-0.0325,1.0200,0.0529,0.0000,1.0200,0.0422,-0.0975,1.0200,0.0132,0.0926,1.4100,-0.0937,0.0674,1.4500,-0.0314,0.1170,1.4100,-0.0395,0.1240,1.4000,-0.0706,0.0583,1.4400,-0.0615,0.0534,1.4200,-0.1120,0.0228,1.4600,-0.0872,0.0000,1.4000,-0.1120,0.0787,1.3900,-0.0029,0.0593,1.4300,-0.0185,0.0228,1.4200,0.0035,0.1120,1.4000,-0.0131,0.1640,1.3900,-0.0373,0.0153,1.3900,0.0159,0.0953,1.3500,-0.1360,0.0545,1.3500,-0.1380,0.1390,1.3400,0.0030,0.1560,1.3500,-0.0915,0.1320,1.2900,-0.1270,0.1510,1.2800,-0.0878,0.1000,1.3000,-0.1480,0.1370,1.3400,-0.0368,0.1470,1.3200,-0.0406,0.1240,1.2600,-0.1250,0.0975,1.2600,-0.1500,0.0210,1.3200,0.0276,0.0532,1.3500,0.0168,0.1030,1.3100,0.0195,0.1350,1.2900,-0.0406,0.1410,1.2500,-0.0744,0.1320,1.1800,-0.0830,0.1340,1.1900,-0.0572,0.0140,1.2500,0.0458,0.0430,1.2500,0.0614,0.1010,1.2500,0.0614,0.1380,1.2400,0.0120,0.0650,1.2300,0.0743,0.1150,1.1600,-0.1050,0.0851,1.1800,-0.1340,0.0524,1.1500,-0.1340,0.0430,1.2000,0.0641,0.1270,1.1400,-0.0427,0.0830,1.1300,-0.1220,0.0162,1.1800,0.0458,0.0457,1.1800,0.0485,0.1170,1.1500,-0.0180,0.1100,1.1000,-0.0846,0.0808,1.1000,-0.1110,0.0524,1.1000,-0.1190,0.0228,1.1000,-0.1160,0.1080,1.1500,-0.0041,0.1200,1.1000,-0.0373,0.1210,1.0700,-0.0356,0.1060,1.0700,-0.0711,0.0475,1.0600,-0.1050,0.0787,1.0800,0.0347,0.0844,1.1500,0.0297,0.1030,1.0800,0.0030,0.0000,1.0700,-0.1100,0.0975,1.0100,-0.0873,0.1340,0.9980,-0.0475,0.0475,1.0200,-0.1090,0.0325,1.0200,0.0529,0.0975,1.0200,0.0132,0.0000,1.0200,-0.1170,0.0000,1.4400,-0.0389,0.0000,1.0100,-0.0259,-0.1040,1.1900,0.0423,-0.0778,1.1900,0.0642,-0.0780,1.1900,0.0644,-0.0493,1.2000,0.0664,-0.0281,1.2200,0.0587,-0.1040,1.2000,0.0568,-0.0484,1.2100,0.0692,-0.0549,1.2100,0.0708,-0.0806,1.2100,0.0713,-0.0852,1.2100,0.0703,0.1160,1.1900,0.0430,0.1140,1.2100,0.0572,0.0967,1.2100,0.0701,0.1100,1.1900,0.0502,0.0930,1.1900,0.0622,0.0832,1.1900,0.0662,0.0863,1.2100,0.0728,0.0154,1.2100,0.0458,-0.0039,1.2100,0.0458,-0.0145,1.2000,0.0512,0.0534,1.3500,0.0168)

IndexedFaceSet228.coord = Coordinate229
TextureCoordinate230 = x3d.TextureCoordinate()
TextureCoordinate230.point = [0.1611,-0.02056,0.9468,-0.02056,0.9739,0.9344,-0.137,1.094,0.1973,0.6424,0.2231,0.04876,0.5054,0.2466,0.5054,0.5929,0.8135,0.6424,0.6282,0.1972,0.7876,0.04876,0.5054,-0.05018,0.6282,-0.05018,0.5054,0.8403,0.7989,1.038,0.5054,1.038,0.8248,0.7908,0.186,0.7908,0.2118,1.038,0.6427,0.7908,-0.01977,0.5929,-0.03324,0.7908,1.044,0.7908,1.031,0.5929,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

IndexedFaceSet228.texCoord.append(TextureCoordinate230)

Shape225.geometry = IndexedFaceSet228

Transform224.children.append(Shape225)

Group223.children.append(Transform224)
Transform231 = x3d.Transform()
Transform231.rotation = [0,0,1,1.57]
Transform231.scale = [2,1.5,1.5]
Transform231.translation = [0.13,0.22,-0.1]
Transform232 = x3d.Transform()
Transform232.rotation = [1,0,0,1.4]
Shape233 = x3d.Shape()
Shape233.DEF = "BCLSnorkelPad"
Appearance234 = x3d.Appearance()
Material235 = x3d.Material()
Material235.USE = "BCLColor"

Appearance234.material = Material235

Shape233.appearance = Appearance234
Extrusion236 = x3d.Extrusion()
Extrusion236.crossSection = [0,0.013,0.00494,0.01196,0.00923,0.00923,0.01196,0.00494,0.013,0,0.01196,-0.00494,0.00923,-0.00923,0.00494,-0.01196,0,0.013]
Extrusion236.spine = (-0.0300,0.0100,0.0000,-0.0050,0.0400,0.0000,0.0000,0.0600,0.0000,-0.0100,0.0750,0.0000)

Shape233.geometry = Extrusion236

Transform232.children.append(Shape233)

Transform231.children.append(Transform232)

Group223.children.append(Transform231)
Transform237 = x3d.Transform()
Transform237.rotation = [-1,0,0,0.8]
Transform237.translation = [0.07,0.08,0.125]
Shape238 = x3d.Shape()
Appearance239 = x3d.Appearance()
Material240 = x3d.Material()
Material240.DEF = "BCLSnorkel"
Material240.diffuseColor = [0.25,0.25,0.25]
Material240.shininess = 0.5
Material240.transparency = 0.1

Appearance239.material = Material240

Shape238.appearance = Appearance239
Extrusion241 = x3d.Extrusion()
Extrusion241.crossSection = [0,0.013,0.00494,0.01196,0.00923,0.00923,0.01196,0.00494,0.013,0,0.01196,-0.00494,0.00923,-0.00923,0.00494,-0.01196,0,0.013,-0.00494,-0.01196,-0.00923,-0.00923,-0.01196,-0.00494,-0.013,0,-0.01196,0.00494,-0.00923,0.00923,-0.00494,0.01196,0,0.013]
Extrusion241.scale = [0.8,0.8,1,1]
Extrusion241.spine = (0.0300,0.0300,-0.0500,0.0500,0.2000,0.0000)

Shape238.geometry = Extrusion241

Transform237.children.append(Shape238)

Group223.children.append(Transform237)
Group242 = x3d.Group()
Group242.DEF = "buckle"
Transform243 = x3d.Transform()
Transform243.rotation = [-1,0,0,0.68]
Transform243.translation = [-0.08,0.1,0.029]
Shape244 = x3d.Shape()
Appearance245 = x3d.Appearance()
Appearance245.DEF = "buckleHolder"
Material246 = x3d.Material()
Material246.diffuseColor = [0.25,0.25,0.25]

Appearance245.material = Material246

Shape244.appearance = Appearance245
Box247 = x3d.Box()
Box247.size = [0.03,0.03,0.005]

Shape244.geometry = Box247

Transform243.children.append(Shape244)

Group242.children.append(Transform243)
Transform248 = x3d.Transform()
Transform248.rotation = [-1,0,0,0.68]
Transform248.translation = [0.03,0.1,0.027]
Shape249 = x3d.Shape()
Appearance250 = x3d.Appearance()
Appearance250.USE = "buckleHolder"

Shape249.appearance = Appearance250
Box251 = x3d.Box()
Box251.size = [0.15,0.03,0.001]

Shape249.geometry = Box251

Transform248.children.append(Shape249)

Group242.children.append(Transform248)
Transform252 = x3d.Transform()
Transform252.rotation = [-1,0,0,0.68]
Transform252.translation = [-0.045,0.1,0.028]
Shape253 = x3d.Shape()
Appearance254 = x3d.Appearance()
Appearance254.DEF = "pin"
Material255 = x3d.Material()

Appearance254.material = Material255

Shape253.appearance = Appearance254
Box256 = x3d.Box()
Box256.size = [0.02,0.028,0.005]

Shape253.geometry = Box256

Transform252.children.append(Shape253)

Group242.children.append(Transform252)
Transform257 = x3d.Transform()
Transform257.rotation = [0,0,1,1.57]
Transform257.translation = [-0.06,0.1,0.029]
Shape258 = x3d.Shape()
Appearance259 = x3d.Appearance()
Appearance259.USE = "pin"

Shape258.appearance = Appearance259
Cylinder260 = x3d.Cylinder()
Cylinder260.height = 0.02
Cylinder260.radius = 0.0024

Shape258.geometry = Cylinder260

Transform257.children.append(Shape258)

Group242.children.append(Transform257)
Transform261 = x3d.Transform()
Transform261.rotation = [0,0,1,1.57]
Transform261.translation = [-0.06,0.109,0.0217]
Shape262 = x3d.Shape()
Appearance263 = x3d.Appearance()
Appearance263.USE = "pin"

Shape262.appearance = Appearance263
Cylinder264 = x3d.Cylinder()
Cylinder264.height = 0.02
Cylinder264.radius = 0.0024

Shape262.geometry = Cylinder264

Transform261.children.append(Shape262)

Group242.children.append(Transform261)
Transform265 = x3d.Transform()
Transform265.rotation = [0,0,1,1.57]
Transform265.translation = [-0.06,0.091,0.036]
Shape266 = x3d.Shape()
Appearance267 = x3d.Appearance()
Appearance267.USE = "pin"

Shape266.appearance = Appearance267
Cylinder268 = x3d.Cylinder()
Cylinder268.height = 0.02
Cylinder268.radius = 0.0024

Shape266.geometry = Cylinder268

Transform265.children.append(Shape266)

Group242.children.append(Transform265)

Group223.children.append(Group242)
Group269 = x3d.Group()
Group269.DEF = "buckleBelt"
Transform270 = x3d.Transform()
Transform270.rotation = [0,1,0,-0.68]
Transform270.translation = [-0.07,-0.12,0.038]
Shape271 = x3d.Shape()
Appearance272 = x3d.Appearance()
Appearance272.USE = "buckleHolder"

Shape271.appearance = Appearance272
Box273 = x3d.Box()
Box273.size = [0.04,0.1,0.005]

Shape271.geometry = Box273

Transform270.children.append(Shape271)

Group269.children.append(Transform270)
Transform274 = x3d.Transform()
Transform274.translation = [0.005,-0.12,0.053]
Shape275 = x3d.Shape()
Appearance276 = x3d.Appearance()
Appearance276.USE = "buckleHolder"

Shape275.appearance = Appearance276
Box277 = x3d.Box()
Box277.size = [0.12,0.11,0.001]

Shape275.geometry = Box277

Transform274.children.append(Shape275)

Group269.children.append(Transform274)
Transform278 = x3d.Transform()
Transform278.rotation = [0,1,0,0.68]
Transform278.translation = [0.075,-0.12,0.038]
Shape279 = x3d.Shape()
Appearance280 = x3d.Appearance()
Appearance280.USE = "buckleHolder"

Shape279.appearance = Appearance280
Box281 = x3d.Box()
Box281.size = [0.04,0.1,0.005]

Shape279.geometry = Box281

Transform278.children.append(Shape279)

Group269.children.append(Transform278)

Group223.children.append(Group269)

Transform222.children.append(Group223)

fieldValue213.children.append(Transform222)
Transform282 = x3d.Transform()
Transform282.DEF = "ScubaTank"
Transform282.rotation = [0,1,0,3.14]
Transform282.scale = [0.8,0.8,0.8]
Transform282.translation = [0,1.1,-0.23]
Transform283 = x3d.Transform()
Shape284 = x3d.Shape()
Appearance285 = x3d.Appearance()
Material286 = x3d.Material()
Material286.DEF = "tank"
Material286.ambientIntensity = 0.3
Material286.diffuseColor = [0.3,0.3,0.5]
Material286.shininess = 0.1
Material286.specularColor = [0.7,0.7,0.8]

Appearance285.material = Material286

Shape284.appearance = Appearance285
Cylinder287 = x3d.Cylinder()
Cylinder287.height = 0.7
Cylinder287.radius = 0.1

Shape284.geometry = Cylinder287

Transform283.children.append(Shape284)

Transform282.children.append(Transform283)
Transform288 = x3d.Transform()
Transform288.translation = [0,0.35,0]
Shape289 = x3d.Shape()
Appearance290 = x3d.Appearance()
Material291 = x3d.Material()
Material291.USE = "tank"

Appearance290.material = Material291

Shape289.appearance = Appearance290
Sphere292 = x3d.Sphere()
Sphere292.radius = 0.098

Shape289.geometry = Sphere292

Transform288.children.append(Shape289)

Transform282.children.append(Transform288)
Transform293 = x3d.Transform()
Transform293.translation = [0,-0.35,0]
Shape294 = x3d.Shape()
Shape294.DEF = "tankBottom"
Appearance295 = x3d.Appearance()
Material296 = x3d.Material()
Material296.ambientIntensity = 0.3
Material296.diffuseColor = [0,0,0]

Appearance295.material = Material296

Shape294.appearance = Appearance295
Cylinder297 = x3d.Cylinder()
Cylinder297.height = 0.06
Cylinder297.radius = 0.101

Shape294.geometry = Cylinder297

Transform293.children.append(Shape294)

Transform282.children.append(Transform293)
Group298 = x3d.Group()
Group298.DEF = "tankNozzle"
Transform299 = x3d.Transform()
Transform300 = x3d.Transform()
Transform300.translation = [0,0.45,0]
Shape301 = x3d.Shape()
Shape301.DEF = "pressure"
Appearance302 = x3d.Appearance()
Material303 = x3d.Material()
Material303.DEF = "pressureColor"
Material303.ambientIntensity = 0.4
Material303.diffuseColor = [0.91,0.91,0.91]
Material303.shininess = 0.16
Material303.specularColor = [0.91,0.9,0.91]

Appearance302.material = Material303

Shape301.appearance = Appearance302
Cylinder304 = x3d.Cylinder()
Cylinder304.height = 0.1
Cylinder304.radius = 0.015

Shape301.geometry = Cylinder304

Transform300.children.append(Shape301)

Transform299.children.append(Transform300)
Transform305 = x3d.Transform()
Transform305.translation = [0,0.5,0]
Shape306 = x3d.Shape()
Shape306.DEF = "pressureTop"
Appearance307 = x3d.Appearance()
Material308 = x3d.Material()
Material308.DEF = "top"
Material308.diffuseColor = [0,0,0]

Appearance307.material = Material308

Shape306.appearance = Appearance307
Cylinder309 = x3d.Cylinder()
Cylinder309.height = 0.02
Cylinder309.radius = 0.025

Shape306.geometry = Cylinder309

Transform305.children.append(Shape306)

Transform299.children.append(Transform305)
Transform310 = x3d.Transform()
Transform310.rotation = [0,0,1,1.57]
Transform310.translation = [-0.028,0.462,0]
Transform311 = x3d.Transform()
Shape312 = x3d.Shape()
Shape312.DEF = "connectorToRegulator"
Appearance313 = x3d.Appearance()
Material314 = x3d.Material()
Material314.USE = "pressureColor"

Appearance313.material = Material314

Shape312.appearance = Appearance313
Cylinder315 = x3d.Cylinder()
Cylinder315.height = 0.03
Cylinder315.radius = 0.01

Shape312.geometry = Cylinder315

Transform311.children.append(Shape312)

Transform310.children.append(Transform311)
Transform316 = x3d.Transform()
Transform316.translation = [0,0.02,0]
Shape317 = x3d.Shape()
Shape317.DEF = "connectorToRegulatorTop"
Appearance318 = x3d.Appearance()
Material319 = x3d.Material()
Material319.USE = "top"

Appearance318.material = Material319

Shape317.appearance = Appearance318
Cylinder320 = x3d.Cylinder()
Cylinder320.height = 0.02
Cylinder320.radius = 0.02

Shape317.geometry = Cylinder320

Transform316.children.append(Shape317)

Transform310.children.append(Transform316)

Transform299.children.append(Transform310)

Group298.children.append(Transform299)

Transform282.children.append(Group298)
Transform321 = x3d.Transform()
Transform321.translation = [0,0.2,0]
Shape322 = x3d.Shape()
Shape322.DEF = "tankHoldBelt"
Appearance323 = x3d.Appearance()
Material324 = x3d.Material()
Material324.ambientIntensity = 0.3
Material324.diffuseColor = [0,0,0]

Appearance323.material = Material324

Shape322.appearance = Appearance323
Cylinder325 = x3d.Cylinder()
Cylinder325.height = 0.1
Cylinder325.radius = 0.115

Shape322.geometry = Cylinder325

Transform321.children.append(Shape322)

Transform282.children.append(Transform321)

fieldValue213.children.append(Transform282)

ProtoInstance211.fieldValue.append(fieldValue213)

fieldValue210.children.append(ProtoInstance211)
ProtoInstance326 = x3d.ProtoInstance()
ProtoInstance326.name = "Joint"
ProtoInstance326.DEF = "hanim_l_shoulder"
fieldValue327 = x3d.fieldValue()
fieldValue327.name = "name"
fieldValue327.value = "l_shoulder"

ProtoInstance326.fieldValue.append(fieldValue327)
fieldValue328 = x3d.fieldValue()
fieldValue328.name = "center"
fieldValue328.value = "0.167 1.36 -0.0518"

ProtoInstance326.fieldValue.append(fieldValue328)
fieldValue329 = x3d.fieldValue()
fieldValue329.name = "children"
ProtoInstance330 = x3d.ProtoInstance()
ProtoInstance330.name = "Segment"
ProtoInstance330.DEF = "hanim_l_upperarm"
fieldValue331 = x3d.fieldValue()
fieldValue331.name = "name"
fieldValue331.value = "l_upperarm"

ProtoInstance330.fieldValue.append(fieldValue331)
fieldValue332 = x3d.fieldValue()
fieldValue332.name = "children"
Transform333 = x3d.Transform()
Transform333.DEF = "l_upperarm_adjust"
Transform333.center = [0.182,1.22,-0.047]
Transform333.rotation = [1,0,0,0.119]
Transform333.translation = [0,0.0004203,-0.01665]
Shape334 = x3d.Shape()
Appearance335 = x3d.Appearance()
Material336 = x3d.Material()
Material336.USE = "WetShirtColor"

Appearance335.material = Material336

Shape334.appearance = Appearance335
IndexedFaceSet337 = x3d.IndexedFaceSet()
IndexedFaceSet337.coordIndex = [2,1,0,-1,2,3,1,-1,2,4,3,-1,2,0,5,-1,6,5,0,-1,7,2,5,-1,8,4,2,-1,8,3,4,-1,9,1,3,-1,10,0,1,-1,0,10,6,-1,1,9,10,-1,3,8,9,-1,2,7,8,-1,5,6,7,-1,11,7,6,-1,14,9,8,-1,15,10,9,-1,11,6,10,-1,10,15,11,-1,9,14,15,-1,8,13,14,-1,8,16,13,-1,7,11,12,-1,21,15,14,-1,15,17,11,-1,15,21,17,-1,16,19,13,-1,13,19,20,-1,21,14,20,-1,14,13,20,-1,12,17,18,-1,12,11,17,-1,12,18,16,-1,18,19,16,-1,12,16,7,-1,16,8,7,-1,19,18,17,-1,20,19,21,-1,19,17,21,-1]
IndexedFaceSet337.creaseAngle = 1.65
Coordinate338 = x3d.Coordinate()
Coordinate338.point = (0.1740,1.3700,-0.0625,0.1850,1.3800,-0.0395,0.1560,1.3900,-0.0464,0.1740,1.3700,-0.0158,0.1540,1.3700,-0.0185,0.1570,1.3800,-0.0733,0.1820,1.3300,-0.0728,0.1510,1.3300,-0.0937,0.1500,1.3400,-0.0008,0.1850,1.3300,-0.0003,0.2010,1.3300,-0.0411,0.1890,1.2600,-0.0808,0.1550,1.2600,-0.0867,0.1510,1.2600,-0.0008,0.1900,1.2600,-0.0040,0.2090,1.2600,-0.0427,0.1410,1.2600,-0.0421,0.2030,1.0800,-0.0744,0.1620,1.0500,-0.0561,0.1690,1.0800,-0.0089,0.2080,1.0700,-0.0013,0.2210,1.0800,-0.0352)

IndexedFaceSet337.coord = Coordinate338

Shape334.geometry = IndexedFaceSet337

Transform333.children.append(Shape334)

fieldValue332.children.append(Transform333)

ProtoInstance330.fieldValue.append(fieldValue332)

fieldValue329.children.append(ProtoInstance330)
ProtoInstance339 = x3d.ProtoInstance()
ProtoInstance339.name = "Joint"
ProtoInstance339.DEF = "hanim_l_elbow"
fieldValue340 = x3d.fieldValue()
fieldValue340.name = "name"
fieldValue340.value = "l_elbow"

ProtoInstance339.fieldValue.append(fieldValue340)
fieldValue341 = x3d.fieldValue()
fieldValue341.name = "center"
fieldValue341.value = "0.196 1.07 -0.0518"

ProtoInstance339.fieldValue.append(fieldValue341)
fieldValue342 = x3d.fieldValue()
fieldValue342.name = "children"
ProtoInstance343 = x3d.ProtoInstance()
ProtoInstance343.name = "Segment"
ProtoInstance343.DEF = "hanim_l_forearm"
fieldValue344 = x3d.fieldValue()
fieldValue344.name = "name"
fieldValue344.value = "l_forearm"

ProtoInstance343.fieldValue.append(fieldValue344)
fieldValue345 = x3d.fieldValue()
fieldValue345.name = "children"
Transform346 = x3d.Transform()
Transform346.DEF = "l_forearm_adjust"
Transform346.center = [0.198,0.961,-0.0405]
Transform346.rotation = [-1,0,0,0.1]
Transform346.translation = [0,0.003724,-0.0236]
Shape347 = x3d.Shape()
Appearance348 = x3d.Appearance()
Material349 = x3d.Material()
Material349.USE = "WetShirtColor"

Appearance348.material = Material349

Shape347.appearance = Appearance348
IndexedFaceSet350 = x3d.IndexedFaceSet()
IndexedFaceSet350.coordIndex = [2,1,0,-1,2,3,1,-1,2,4,3,-1,2,5,4,-1,2,6,5,-1,2,0,6,-1,7,6,0,-1,8,5,6,-1,9,4,5,-1,9,3,4,-1,10,1,3,-1,11,0,1,-1,0,11,7,-1,1,10,11,-1,3,9,10,-1,5,12,9,-1,5,8,12,-1,6,7,8,-1,17,16,15,-1,14,17,15,-1,14,18,17,-1,13,18,14,-1,16,17,10,-1,16,10,9,-1,15,16,9,-1,15,9,12,-1,18,13,7,-1,18,7,11,-1,13,14,8,-1,13,8,7,-1,14,15,8,-1,15,12,8,-1,17,18,10,-1,18,11,10,-1]
IndexedFaceSet350.creaseAngle = 1.75
Coordinate351 = x3d.Coordinate()
Coordinate351.point = (0.1770,1.0900,-0.0609,0.2020,1.1000,-0.0566,0.1890,1.1000,-0.0395,0.2130,1.1000,-0.0250,0.2030,1.1000,-0.0158,0.1820,1.0900,-0.0056,0.1670,1.0900,-0.0325,0.1760,1.0800,-0.0781,0.1600,1.0600,-0.0373,0.2140,1.0700,-0.0040,0.2280,1.0700,-0.0319,0.2080,1.0800,-0.0765,0.1790,1.0700,-0.0029,0.2100,0.8180,-0.0615,0.2010,0.8200,-0.0405,0.2050,0.8190,-0.0083,0.2240,0.8180,-0.0078,0.2370,0.8200,-0.0282,0.2310,0.8190,-0.0609)

IndexedFaceSet350.coord = Coordinate351

Shape347.geometry = IndexedFaceSet350

Transform346.children.append(Shape347)

fieldValue345.children.append(Transform346)

ProtoInstance343.fieldValue.append(fieldValue345)

fieldValue342.children.append(ProtoInstance343)
ProtoInstance352 = x3d.ProtoInstance()
ProtoInstance352.name = "Joint"
ProtoInstance352.DEF = "hanim_l_wrist"
fieldValue353 = x3d.fieldValue()
fieldValue353.name = "name"
fieldValue353.value = "l_wrist"

ProtoInstance352.fieldValue.append(fieldValue353)
fieldValue354 = x3d.fieldValue()
fieldValue354.name = "center"
fieldValue354.value = "0.213 0.811 -0.0338"

ProtoInstance352.fieldValue.append(fieldValue354)
fieldValue355 = x3d.fieldValue()
fieldValue355.name = "children"
ProtoInstance356 = x3d.ProtoInstance()
ProtoInstance356.name = "Segment"
ProtoInstance356.DEF = "hanim_l_hand"
fieldValue357 = x3d.fieldValue()
fieldValue357.name = "name"
fieldValue357.value = "l_hand"

ProtoInstance356.fieldValue.append(fieldValue357)
fieldValue358 = x3d.fieldValue()
fieldValue358.name = "children"
Transform359 = x3d.Transform()
Transform359.DEF = "l_hand_adjust"
Transform359.center = [0.213,0.811,-0.0338]
Transform359.rotation = [-0.06361,-0.9967,0.04988,1.333]
Transform359.translation = [0,0.005142,-0.008662]
Shape360 = x3d.Shape()
Appearance361 = x3d.Appearance()
Material362 = x3d.Material()
Material362.DEF = "Skin_Color"
Material362.ambientIntensity = 0.25
Material362.diffuseColor = [0.749,0.601,0.462]

Appearance361.material = Material362

Shape360.appearance = Appearance361
IndexedFaceSet363 = x3d.IndexedFaceSet()
IndexedFaceSet363.coordIndex = [2,1,0,-1,5,4,3,-1,3,7,6,-1,2,3,6,-1,7,9,8,-1,6,7,8,-1,9,11,10,-1,8,9,10,-1,11,13,12,-1,10,11,12,-1,13,15,14,-1,12,13,14,-1,15,17,16,-1,14,15,16,-1,17,19,18,-1,16,17,18,-1,19,21,20,-1,18,19,20,-1,31,4,1,-1,4,5,0,-1,1,4,0,-1,5,3,2,-1,0,5,2,-1,26,25,24,-1,26,24,23,-1,27,26,23,-1,28,27,23,-1,28,23,22,-1,29,28,22,-1,29,22,21,-1,30,29,21,-1,15,13,11,-1,17,15,11,-1,19,17,11,-1,19,11,9,-1,31,19,9,-1,31,9,7,-1,4,31,7,-1,4,7,3,-1,30,21,19,-1,31,30,19,-1,12,14,16,-1,10,12,16,-1,10,16,18,-1,8,10,18,-1,6,8,1,-1,2,6,1,-1,39,38,37,-1,37,38,40,-1,37,40,36,-1,36,40,41,-1,36,41,35,-1,35,41,42,-1,35,42,34,-1,34,42,43,-1,34,43,33,-1,33,43,44,-1,33,44,32,-1,20,32,44,-1,20,44,45,-1,20,45,46,-1,47,8,18,-1,47,18,20,-1,47,20,46,-1,8,47,1,-1,22,33,32,-1,23,35,34,-1,23,36,35,-1,37,24,25,-1,40,38,27,-1,29,43,42,-1,45,44,30,-1,47,31,1,-1,47,46,31,-1,29,30,43,-1,30,44,43,-1,45,31,46,-1,45,30,31,-1,28,29,41,-1,29,42,41,-1,28,40,27,-1,28,41,40,-1,26,27,39,-1,27,38,39,-1,25,39,37,-1,25,26,39,-1,24,36,23,-1,24,37,36,-1,23,34,22,-1,34,33,22,-1,22,32,21,-1,32,20,21,-1]
IndexedFaceSet363.creaseAngle = 1.48
Coordinate364 = x3d.Coordinate()
Coordinate364.point = (0.2110,0.8280,-0.0434,0.1940,0.8100,-0.0445,0.2370,0.8200,-0.0425,0.2360,0.8200,-0.0237,0.1940,0.8100,-0.0254,0.2100,0.8280,-0.0247,0.2520,0.8010,-0.0424,0.2520,0.8010,-0.0231,0.2690,0.7650,-0.0426,0.2680,0.7650,-0.0225,0.2730,0.7320,-0.0395,0.2720,0.7320,-0.0223,0.2700,0.7040,-0.0342,0.2700,0.7040,-0.0224,0.2620,0.7030,-0.0345,0.2610,0.7030,-0.0227,0.2560,0.7170,-0.0389,0.2560,0.7170,-0.0230,0.2550,0.7380,-0.0408,0.2550,0.7380,-0.0230,0.2510,0.7340,-0.0406,0.2510,0.7340,-0.0232,0.2510,0.6920,-0.0232,0.2480,0.6570,-0.0233,0.2400,0.6450,-0.0236,0.2260,0.6370,-0.0241,0.2130,0.6390,-0.0246,0.1970,0.6520,-0.0253,0.1880,0.6690,-0.0256,0.1840,0.6970,-0.0258,0.1830,0.7300,-0.0258,0.1870,0.7700,-0.0257,0.2440,0.6960,-0.0375,0.2440,0.6920,-0.0372,0.2420,0.6610,-0.0345,0.2410,0.6580,-0.0343,0.2410,0.6560,-0.0341,0.2310,0.6460,-0.0336,0.2060,0.6500,-0.0349,0.2180,0.6440,-0.0340,0.2050,0.6520,-0.0352,0.1980,0.6670,-0.0367,0.1950,0.6910,-0.0390,0.1940,0.6960,-0.0395,0.1930,0.7250,-0.0420,0.1930,0.7310,-0.0425,0.1970,0.7650,-0.0449,0.1970,0.7700,-0.0453)

IndexedFaceSet363.coord = Coordinate364

Shape360.geometry = IndexedFaceSet363

Transform359.children.append(Shape360)

fieldValue358.children.append(Transform359)

ProtoInstance356.fieldValue.append(fieldValue358)

fieldValue355.children.append(ProtoInstance356)

ProtoInstance352.fieldValue.append(fieldValue355)

fieldValue342.children.append(ProtoInstance352)

ProtoInstance339.fieldValue.append(fieldValue342)

fieldValue329.children.append(ProtoInstance339)

ProtoInstance326.fieldValue.append(fieldValue329)

fieldValue210.children.append(ProtoInstance326)
ProtoInstance365 = x3d.ProtoInstance()
ProtoInstance365.name = "Joint"
ProtoInstance365.DEF = "hanim_r_shoulder"
fieldValue366 = x3d.fieldValue()
fieldValue366.name = "name"
fieldValue366.value = "r_shoulder"

ProtoInstance365.fieldValue.append(fieldValue366)
fieldValue367 = x3d.fieldValue()
fieldValue367.name = "center"
fieldValue367.value = "-0.167 1.36 -0.0458"

ProtoInstance365.fieldValue.append(fieldValue367)
fieldValue368 = x3d.fieldValue()
fieldValue368.name = "children"
ProtoInstance369 = x3d.ProtoInstance()
ProtoInstance369.name = "Segment"
ProtoInstance369.DEF = "hanim_r_upperarm"
fieldValue370 = x3d.fieldValue()
fieldValue370.name = "name"
fieldValue370.value = "r_upperarm"

ProtoInstance369.fieldValue.append(fieldValue370)
fieldValue371 = x3d.fieldValue()
fieldValue371.name = "children"
Transform372 = x3d.Transform()
Transform372.DEF = "r_upperarm_adjust"
Transform372.center = [-0.182,1.22,-0.047]
Transform372.rotation = [1,0,0,0.0836]
Transform372.translation = [0,0.000589,-0.01169]
Shape373 = x3d.Shape()
Appearance374 = x3d.Appearance()
Material375 = x3d.Material()
Material375.USE = "WetShirtColor"

Appearance374.material = Material375

Shape373.appearance = Appearance374
IndexedFaceSet376 = x3d.IndexedFaceSet()
IndexedFaceSet376.coordIndex = [14,10,20,-1,10,13,20,-1,13,22,20,-1,19,14,20,-1,14,19,12,-1,19,20,24,-1,20,22,25,-1,22,13,25,-1,13,10,11,-1,10,14,5,-1,12,5,14,-1,5,11,10,-1,11,25,13,-1,25,24,20,-1,24,12,19,-1,12,24,9,-1,25,11,8,-1,11,5,2,-1,5,12,9,-1,9,2,5,-1,2,8,11,-1,8,23,25,-1,23,27,25,-1,21,9,24,-1,9,21,7,-1,27,23,18,-1,23,8,18,-1,8,2,6,-1,2,9,7,-1,7,1,2,-1,1,6,2,-1,6,18,8,-1,18,26,27,-1,16,7,21,-1,7,16,4,-1,16,26,17,-1,26,18,15,-1,18,6,3,-1,6,1,0,-1,1,7,0,-1,4,0,7,-1,0,3,6,-1,3,15,18,-1,15,17,26,-1,17,4,16,-1,3,0,15,-1,15,0,4,-1,15,4,17,-1,25,27,24,-1,27,21,24,-1,27,26,21,-1,26,16,21,-1]
IndexedFaceSet376.creaseAngle = 1.53
Coordinate377 = x3d.Coordinate()
Coordinate377.point = (-0.2210,1.0800,-0.0352,-0.2140,1.1400,-0.0405,-0.2090,1.2600,-0.0427,-0.2080,1.0700,-0.0013,-0.2030,1.0800,-0.0744,-0.2010,1.3300,-0.0411,-0.1980,1.1400,-0.0024,-0.1980,1.1300,-0.0760,-0.1900,1.2600,-0.0040,-0.1890,1.2600,-0.0808,-0.1850,1.3800,-0.0395,-0.1850,1.3300,-0.0003,-0.1820,1.3300,-0.0728,-0.1740,1.3700,-0.0158,-0.1740,1.3700,-0.0625,-0.1690,1.0800,-0.0089,-0.1670,1.1300,-0.0744,-0.1620,1.0500,-0.0561,-0.1600,1.1300,-0.0008,-0.1570,1.3800,-0.0733,-0.1560,1.3900,-0.0464,-0.1550,1.2600,-0.0867,-0.1540,1.3700,-0.0185,-0.1510,1.2600,-0.0008,-0.1510,1.3300,-0.0937,-0.1500,1.3400,-0.0008,-0.1500,1.1300,-0.0411,-0.1410,1.2600,-0.0421)

IndexedFaceSet376.coord = Coordinate377

Shape373.geometry = IndexedFaceSet376

Transform372.children.append(Shape373)

fieldValue371.children.append(Transform372)

ProtoInstance369.fieldValue.append(fieldValue371)

fieldValue368.children.append(ProtoInstance369)
ProtoInstance378 = x3d.ProtoInstance()
ProtoInstance378.name = "Joint"
ProtoInstance378.DEF = "hanim_r_elbow"
fieldValue379 = x3d.fieldValue()
fieldValue379.name = "name"
fieldValue379.value = "r_elbow"

ProtoInstance378.fieldValue.append(fieldValue379)
fieldValue380 = x3d.fieldValue()
fieldValue380.name = "center"
fieldValue380.value = "-0.192 1.07 -0.0498"

ProtoInstance378.fieldValue.append(fieldValue380)
fieldValue381 = x3d.fieldValue()
fieldValue381.name = "children"
ProtoInstance382 = x3d.ProtoInstance()
ProtoInstance382.name = "Segment"
ProtoInstance382.DEF = "hanim_r_forearm"
fieldValue383 = x3d.fieldValue()
fieldValue383.name = "name"
fieldValue383.value = "r_forearm"

ProtoInstance382.fieldValue.append(fieldValue383)
fieldValue384 = x3d.fieldValue()
fieldValue384.name = "children"
Transform385 = x3d.Transform()
Transform385.DEF = "r_forearm_adjust"
Transform385.center = [-0.198,0.961,-0.0397]
Transform385.rotation = [-1,0,0,0.1254]
Transform385.translation = [0,0.003466,-0.01065]
Shape386 = x3d.Shape()
Appearance387 = x3d.Appearance()
Material388 = x3d.Material()
Material388.USE = "WetShirtColor"

Appearance387.material = Material388

Shape386.appearance = Appearance387
IndexedFaceSet389 = x3d.IndexedFaceSet()
IndexedFaceSet389.coordIndex = [20,13,15,-1,13,8,15,-1,8,12,15,-1,12,18,15,-1,18,22,15,-1,22,20,15,-1,20,22,21,-1,22,18,24,-1,18,12,7,-1,12,8,7,-1,8,13,3,-1,13,20,10,-1,21,10,20,-1,10,3,13,-1,3,7,8,-1,7,19,18,-1,19,24,18,-1,24,21,22,-1,21,24,23,-1,24,19,16,-1,19,7,6,-1,7,3,1,-1,3,10,5,-1,10,21,17,-1,17,5,10,-1,5,1,3,-1,1,6,7,-1,6,16,19,-1,16,23,24,-1,23,17,21,-1,1,5,2,-1,5,17,9,-1,9,2,5,-1,1,4,6,-1,4,16,6,-1,23,9,17,-1,9,23,14,-1,23,16,11,-1,4,11,16,-1,11,14,23,-1,11,4,0,-1,11,0,14,-1,0,2,14,-1,14,2,9,-1,2,0,1,-1,0,4,1,-1]
IndexedFaceSet389.creaseAngle = 1.73
Coordinate390 = x3d.Coordinate()
Coordinate390.point = (-0.2370,0.8200,-0.0282,-0.2350,1.0200,-0.0330,-0.2310,0.8190,-0.0609,-0.2280,1.0700,-0.0319,-0.2240,0.8180,-0.0078,-0.2210,1.0100,-0.0744,-0.2180,1.0100,-0.0013,-0.2140,1.0700,-0.0040,-0.2130,1.1000,-0.0250,-0.2100,0.8180,-0.0615,-0.2080,1.0800,-0.0765,-0.2050,0.8190,-0.0083,-0.2030,1.1000,-0.0158,-0.2020,1.1000,-0.0566,-0.2010,0.8200,-0.0405,-0.1890,1.1000,-0.0395,-0.1830,1.0100,-0.0083,-0.1830,1.0100,-0.0781,-0.1820,1.0900,-0.0056,-0.1790,1.0700,-0.0029,-0.1770,1.0900,-0.0609,-0.1760,1.0800,-0.0781,-0.1670,1.0900,-0.0325,-0.1660,1.0000,-0.0405,-0.1600,1.0600,-0.0373)

IndexedFaceSet389.coord = Coordinate390

Shape386.geometry = IndexedFaceSet389

Transform385.children.append(Shape386)

fieldValue384.children.append(Transform385)

ProtoInstance382.fieldValue.append(fieldValue384)

fieldValue381.children.append(ProtoInstance382)
ProtoInstance391 = x3d.ProtoInstance()
ProtoInstance391.name = "Joint"
ProtoInstance391.DEF = "hanim_r_wrist"
fieldValue392 = x3d.fieldValue()
fieldValue392.name = "name"
fieldValue392.value = "r_wrist"

ProtoInstance391.fieldValue.append(fieldValue392)
fieldValue393 = x3d.fieldValue()
fieldValue393.name = "center"
fieldValue393.value = "-0.217 0.811 -0.0338"

ProtoInstance391.fieldValue.append(fieldValue393)
fieldValue394 = x3d.fieldValue()
fieldValue394.name = "children"
ProtoInstance395 = x3d.ProtoInstance()
ProtoInstance395.name = "Segment"
ProtoInstance395.DEF = "hanim_r_hand"
fieldValue396 = x3d.fieldValue()
fieldValue396.name = "name"
fieldValue396.value = "r_hand"

ProtoInstance395.fieldValue.append(fieldValue396)
fieldValue397 = x3d.fieldValue()
fieldValue397.name = "children"
Transform398 = x3d.Transform()
Transform398.DEF = "r_hand_adjust"
Transform398.center = [-0.217,0.811,-0.0338]
Transform398.rotation = [-0.09024,0.994,-0.0624,1.216]
Shape399 = x3d.Shape()
Appearance400 = x3d.Appearance()
Material401 = x3d.Material()
Material401.USE = "Skin_Color"

Appearance400.material = Material401

Shape399.appearance = Appearance400
IndexedFaceSet402 = x3d.IndexedFaceSet()
IndexedFaceSet402.coordIndex = [10,9,0,-1,11,30,31,-1,1,12,11,-1,1,11,0,-1,2,13,12,-1,2,12,1,-1,3,14,13,-1,3,13,2,-1,4,15,14,-1,4,14,3,-1,5,16,15,-1,5,15,4,-1,6,17,16,-1,6,16,5,-1,7,18,17,-1,7,17,6,-1,8,19,18,-1,8,18,7,-1,10,31,30,-1,10,30,9,-1,0,11,31,-1,0,31,10,-1,22,23,24,-1,21,22,24,-1,21,24,25,-1,21,25,26,-1,20,21,26,-1,20,26,27,-1,19,20,27,-1,19,27,28,-1,14,15,16,-1,14,16,17,-1,14,17,18,-1,13,14,18,-1,13,18,29,-1,12,13,29,-1,12,29,30,-1,11,12,30,-1,18,19,28,-1,18,28,29,-1,6,5,4,-1,6,4,3,-1,7,6,3,-1,7,3,2,-1,9,2,1,-1,9,1,0,-1,32,38,33,-1,33,38,39,-1,33,39,34,-1,34,39,40,-1,34,40,35,-1,35,40,41,-1,35,41,36,-1,36,41,42,-1,36,42,37,-1,37,42,43,-1,37,43,44,-1,44,43,8,-1,44,8,45,-1,45,8,46,-1,46,8,7,-1,46,7,2,-1,46,2,47,-1,9,47,2,-1,25,34,35,-1,25,33,34,-1,25,24,33,-1,24,32,33,-1,32,24,23,-1,40,39,21,-1,41,40,21,-1,43,19,8,-1,43,20,19,-1,43,42,20,-1,21,20,41,-1,20,42,41,-1,38,22,39,-1,22,21,39,-1,32,23,38,-1,23,22,38,-1,26,25,35,-1,27,36,37,-1,27,37,28,-1,37,44,28,-1,26,35,27,-1,35,36,27,-1,28,44,45,-1,29,46,47,-1,29,9,30,-1,29,47,9,-1,28,45,29,-1,45,46,29,-1]
IndexedFaceSet402.creaseAngle = 1.57
Coordinate403 = x3d.Coordinate()
Coordinate403.point = (-0.2370,0.8200,-0.0425,-0.2520,0.8010,-0.0424,-0.2690,0.7650,-0.0426,-0.2730,0.7320,-0.0395,-0.2700,0.7040,-0.0342,-0.2620,0.7030,-0.0345,-0.2560,0.7170,-0.0389,-0.2550,0.7380,-0.0408,-0.2510,0.7340,-0.0406,-0.1940,0.8100,-0.0445,-0.2110,0.8280,-0.0434,-0.2360,0.8200,-0.0237,-0.2520,0.8010,-0.0231,-0.2680,0.7650,-0.0225,-0.2720,0.7320,-0.0223,-0.2700,0.7040,-0.0224,-0.2610,0.7030,-0.0227,-0.2560,0.7170,-0.0230,-0.2550,0.7380,-0.0230,-0.2510,0.7340,-0.0232,-0.2510,0.6920,-0.0232,-0.2480,0.6570,-0.0233,-0.2400,0.6450,-0.0236,-0.2260,0.6370,-0.0241,-0.2130,0.6390,-0.0246,-0.1970,0.6520,-0.0253,-0.1880,0.6690,-0.0256,-0.1840,0.6970,-0.0258,-0.1830,0.7300,-0.0258,-0.1870,0.7700,-0.0257,-0.1940,0.8100,-0.0254,-0.2100,0.8280,-0.0247,-0.2210,0.6410,-0.0336,-0.2100,0.6500,-0.0348,-0.2060,0.6520,-0.0352,-0.1980,0.6670,-0.0368,-0.1930,0.6920,-0.0392,-0.1920,0.6960,-0.0396,-0.2310,0.6460,-0.0336,-0.2380,0.6560,-0.0342,-0.2400,0.6580,-0.0344,-0.2400,0.6620,-0.0347,-0.2430,0.6920,-0.0372,-0.2430,0.6960,-0.0376,-0.1920,0.7250,-0.0421,-0.1920,0.7300,-0.0426,-0.1950,0.7660,-0.0451,-0.1960,0.7700,-0.0454)

IndexedFaceSet402.coord = Coordinate403

Shape399.geometry = IndexedFaceSet402

Transform398.children.append(Shape399)

fieldValue397.children.append(Transform398)

ProtoInstance395.fieldValue.append(fieldValue397)

fieldValue394.children.append(ProtoInstance395)

ProtoInstance391.fieldValue.append(fieldValue394)

fieldValue381.children.append(ProtoInstance391)

ProtoInstance378.fieldValue.append(fieldValue381)

fieldValue368.children.append(ProtoInstance378)

ProtoInstance365.fieldValue.append(fieldValue368)

fieldValue210.children.append(ProtoInstance365)
ProtoInstance404 = x3d.ProtoInstance()
ProtoInstance404.name = "Joint"
ProtoInstance404.DEF = "hanim_vc4"
fieldValue405 = x3d.fieldValue()
fieldValue405.name = "name"
fieldValue405.value = "vc4"

ProtoInstance404.fieldValue.append(fieldValue405)
fieldValue406 = x3d.fieldValue()
fieldValue406.name = "center"
fieldValue406.value = "0 1.43 -0.0458"

ProtoInstance404.fieldValue.append(fieldValue406)
fieldValue407 = x3d.fieldValue()
fieldValue407.name = "children"
ProtoInstance408 = x3d.ProtoInstance()
ProtoInstance408.name = "Segment"
ProtoInstance408.DEF = "hanim_c4"
fieldValue409 = x3d.fieldValue()
fieldValue409.name = "name"
fieldValue409.value = "c4"

ProtoInstance408.fieldValue.append(fieldValue409)
fieldValue410 = x3d.fieldValue()
fieldValue410.name = "children"
Shape411 = x3d.Shape()
Appearance412 = x3d.Appearance()
Material413 = x3d.Material()
Material413.USE = "WetShirtColor"

Appearance412.material = Material413

Shape411.appearance = Appearance412
IndexedFaceSet414 = x3d.IndexedFaceSet()
IndexedFaceSet414.DEF = "neck"
IndexedFaceSet414.coordIndex = [6,5,2,-1,6,2,3,-1,5,4,1,-1,5,1,2,-1,4,7,0,-1,4,0,1,-1,11,10,9,-1,11,9,8,-1,10,13,12,-1,10,12,9,-1,13,15,14,-1,13,14,12,-1,6,3,11,-1,6,11,8,-1,7,14,15,-1,7,15,0,-1,2,10,11,-1,2,11,3,-1,2,1,13,-1,2,13,10,-1,1,0,15,-1,1,15,13,-1,9,5,6,-1,9,6,8,-1,9,12,4,-1,9,4,5,-1,12,14,7,-1,12,7,4,-1]
IndexedFaceSet414.creaseAngle = 1.91
Coordinate415 = x3d.Coordinate()
Coordinate415.point = (0.0105,1.5400,-0.1000,0.0357,1.5400,-0.0685,0.0382,1.5500,-0.0474,0.0105,1.5500,-0.0204,0.0373,1.4000,-0.0593,0.0577,1.4000,-0.0266,0.0158,1.4000,0.0051,0.0132,1.4100,-0.0824,-0.0158,1.4000,0.0051,-0.0577,1.4000,-0.0266,-0.0382,1.5500,-0.0474,-0.0105,1.5500,-0.0204,-0.0373,1.4000,-0.0593,-0.0357,1.5400,-0.0685,-0.0132,1.4100,-0.0824,-0.0105,1.5400,-0.1000)

IndexedFaceSet414.coord = Coordinate415

Shape411.geometry = IndexedFaceSet414

fieldValue410.children.append(Shape411)

ProtoInstance408.fieldValue.append(fieldValue410)

fieldValue407.children.append(ProtoInstance408)
ProtoInstance416 = x3d.ProtoInstance()
ProtoInstance416.name = "Joint"
ProtoInstance416.DEF = "hanim_skullbase"
fieldValue417 = x3d.fieldValue()
fieldValue417.name = "name"
fieldValue417.value = "skullbase"

ProtoInstance416.fieldValue.append(fieldValue417)
fieldValue418 = x3d.fieldValue()
fieldValue418.name = "center"
fieldValue418.value = "0 1.54 -0.0409"

ProtoInstance416.fieldValue.append(fieldValue418)
fieldValue419 = x3d.fieldValue()
fieldValue419.name = "children"
ProtoInstance420 = x3d.ProtoInstance()
ProtoInstance420.name = "Segment"
ProtoInstance420.DEF = "hanim_skull"
fieldValue421 = x3d.fieldValue()
fieldValue421.name = "name"
fieldValue421.value = "skull"

ProtoInstance420.fieldValue.append(fieldValue421)
fieldValue422 = x3d.fieldValue()
fieldValue422.name = "children"
Shape423 = x3d.Shape()
Appearance424 = x3d.Appearance()
Material425 = x3d.Material()
Material425.USE = "Skin_Color"

Appearance424.material = Material425

Shape423.appearance = Appearance424
IndexedFaceSet426 = x3d.IndexedFaceSet()
IndexedFaceSet426.DEF = "headIFS"
IndexedFaceSet426.colorIndex = [1,1,1,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,1,1,1,-1,1,1,1,-1,0,0,0,-1,1,1,1,-1,1,1,1,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,2,2,2,-1,2,2,2,-1,2,2,2,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,2,2,2,-1,2,2,2,-1,2,2,2,-1,0,0,0,-1,0,0,0,-1,2,2,2,-1,2,2,2,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,1,1,1,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,2,2,2,-1,2,2,2,-1,2,2,2,-1,2,2,2,-1,2,2,2,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,2,2,2,-1,2,2,2,-1,2,2,2,-1,0,0,0,-1,0,0,0,-1,2,2,2,-1,2,2,2,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,4,4,4,-1,0,0,0,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,0,0,0,-1,0,0,0,-1,4,4,4,-1,0,0,0,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,0,0,0,-1,0,0,0,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1]
IndexedFaceSet426.coordIndex = [48,87,58,-1,91,92,59,-1,59,92,88,-1,88,93,231,-1,232,86,233,-1,86,89,233,-1,89,57,56,-1,49,55,57,-1,102,86,96,-1,86,90,96,-1,97,95,96,-1,97,127,95,-1,41,96,154,-1,41,102,96,-1,99,102,41,-1,153,99,41,-1,102,40,86,-1,234,235,236,-1,87,237,58,-1,56,57,91,-1,87,234,237,-1,234,236,237,-1,89,49,57,-1,49,50,55,-1,40,89,86,-1,89,56,233,-1,232,90,86,-1,90,97,96,-1,92,93,88,-1,93,94,231,-1,232,231,94,-1,97,90,232,-1,96,42,154,-1,95,42,96,-1,53,46,45,-1,53,45,51,-1,53,51,92,-1,92,51,52,-1,92,52,93,-1,94,93,52,-1,94,52,4,-1,97,232,94,-1,54,47,46,-1,54,46,53,-1,55,47,54,-1,50,47,55,-1,34,33,50,-1,34,50,49,-1,35,34,49,-1,35,49,89,-1,35,89,40,-1,99,39,102,-1,39,35,40,-1,31,34,35,-1,31,35,32,-1,14,32,35,-1,14,35,39,-1,14,39,98,-1,137,38,153,-1,38,99,153,-1,38,98,99,-1,37,238,239,-1,11,238,37,-1,101,37,36,-1,241,141,242,-1,10,12,242,-1,12,13,14,-1,12,14,243,-1,13,15,32,-1,13,32,14,-1,15,16,31,-1,15,31,32,-1,2,70,10,-1,2,10,141,-1,70,69,12,-1,70,12,10,-1,69,68,13,-1,69,13,12,-1,68,67,15,-1,68,15,13,-1,67,66,16,-1,67,16,15,-1,98,39,99,-1,101,11,37,-1,100,101,36,-1,36,244,240,-1,141,10,242,-1,12,243,242,-1,36,37,239,-1,36,239,244,-1,57,55,91,-1,55,54,91,-1,39,40,102,-1,123,103,120,-1,114,122,104,-1,115,122,114,-1,208,105,115,-1,210,119,211,-1,210,106,119,-1,116,107,106,-1,107,108,117,-1,126,119,109,-1,126,110,119,-1,126,95,125,-1,95,127,125,-1,154,126,111,-1,126,109,111,-1,111,109,112,-1,111,112,153,-1,119,113,109,-1,207,213,214,-1,123,209,103,-1,213,212,214,-1,209,214,103,-1,209,207,214,-1,107,117,106,-1,108,118,117,-1,119,106,113,-1,210,116,106,-1,119,110,211,-1,126,125,110,-1,115,105,122,-1,208,124,105,-1,124,208,211,-1,211,110,125,-1,154,42,126,-1,126,42,95,-1,168,128,121,-1,170,168,121,-1,122,170,121,-1,172,170,122,-1,105,172,122,-1,172,105,124,-1,4,172,124,-1,124,211,125,-1,128,130,129,-1,121,128,129,-1,129,130,108,-1,108,130,118,-1,118,131,132,-1,117,118,132,-1,117,132,133,-1,106,117,133,-1,113,106,133,-1,109,152,112,-1,113,133,152,-1,133,132,134,-1,135,133,134,-1,133,135,136,-1,152,133,136,-1,148,152,136,-1,153,138,137,-1,153,112,138,-1,112,148,138,-1,219,217,139,-1,36,240,149,-1,139,217,140,-1,149,139,151,-1,36,149,100,-1,220,141,241,-1,220,150,142,-1,136,143,150,-1,221,136,150,-1,135,144,143,-1,136,135,143,-1,134,158,144,-1,135,134,144,-1,142,161,2,-1,141,142,2,-1,150,145,161,-1,142,150,161,-1,143,146,145,-1,150,143,145,-1,144,147,146,-1,143,144,146,-1,158,160,147,-1,144,158,147,-1,112,152,148,-1,139,140,151,-1,149,151,100,-1,240,218,149,-1,220,142,141,-1,220,221,150,-1,219,139,149,-1,218,219,149,-1,104,108,107,-1,104,129,108,-1,109,113,152,-1,153,41,111,-1,129,104,122,-1,129,122,121,-1,91,54,92,-1,54,53,92,-1,97,94,127,-1,127,94,4,-1,125,127,124,-1,127,4,124,-1,154,111,41,-1,31,30,33,-1,31,33,34,-1,16,17,30,-1,16,30,31,-1,66,65,17,-1,66,17,16,-1,2,73,156,-1,2,156,70,-1,156,72,66,-1,156,66,67,-1,156,67,68,-1,156,68,69,-1,156,69,70,-1,72,71,65,-1,72,65,66,-1,17,18,30,-1,45,44,51,-1,51,44,43,-1,51,43,52,-1,52,43,1,-1,52,1,4,-1,245,246,27,-1,245,27,3,-1,246,247,28,-1,246,28,27,-1,248,22,29,-1,248,29,28,-1,248,28,247,-1,27,26,0,-1,27,0,3,-1,27,28,25,-1,27,25,26,-1,29,24,25,-1,29,25,28,-1,22,23,24,-1,22,24,29,-1,249,250,22,-1,249,22,248,-1,250,60,23,-1,250,23,22,-1,17,254,18,-1,65,254,17,-1,71,64,65,-1,63,74,75,-1,63,75,61,-1,64,255,254,-1,75,62,61,-1,62,76,60,-1,76,77,23,-1,76,23,60,-1,77,24,23,-1,77,78,25,-1,77,25,24,-1,78,84,26,-1,78,26,25,-1,84,192,0,-1,84,0,26,-1,84,83,193,-1,84,193,192,-1,79,83,84,-1,79,84,78,-1,76,79,78,-1,76,78,77,-1,80,83,79,-1,80,204,83,-1,75,81,80,-1,81,85,204,-1,81,204,80,-1,74,81,75,-1,74,82,81,-1,82,5,85,-1,82,85,81,-1,155,8,71,-1,155,71,72,-1,8,6,64,-1,8,64,71,-1,6,7,255,-1,6,255,64,-1,7,9,256,-1,7,256,255,-1,9,257,256,-1,73,155,156,-1,155,72,156,-1,204,193,83,-1,64,254,65,-1,131,157,134,-1,132,131,134,-1,157,159,158,-1,134,157,158,-1,159,206,160,-1,158,159,160,-1,203,73,2,-1,161,203,2,-1,160,162,203,-1,147,160,203,-1,146,147,203,-1,145,146,203,-1,161,145,203,-1,206,163,162,-1,160,206,162,-1,157,164,159,-1,170,169,168,-1,171,169,170,-1,172,171,170,-1,1,171,172,-1,4,1,172,-1,173,227,245,-1,3,173,245,-1,174,226,227,-1,173,174,227,-1,176,175,215,-1,174,176,215,-1,226,174,215,-1,0,177,173,-1,3,0,173,-1,178,174,173,-1,177,178,173,-1,178,179,176,-1,174,178,176,-1,179,180,175,-1,176,179,175,-1,175,225,216,-1,215,175,216,-1,180,181,225,-1,175,180,225,-1,164,228,159,-1,159,228,206,-1,206,185,163,-1,187,186,184,-1,183,187,184,-1,228,229,185,-1,183,182,187,-1,181,188,182,-1,180,189,188,-1,181,180,188,-1,180,179,189,-1,178,190,189,-1,179,178,189,-1,177,191,190,-1,178,177,190,-1,0,192,191,-1,177,0,191,-1,193,205,191,-1,192,193,191,-1,191,205,194,-1,190,191,194,-1,190,194,188,-1,189,190,188,-1,194,205,195,-1,205,204,195,-1,195,196,187,-1,204,85,196,-1,195,204,196,-1,187,196,186,-1,196,197,186,-1,85,5,197,-1,196,85,197,-1,163,198,202,-1,162,163,202,-1,185,199,198,-1,163,185,198,-1,229,200,199,-1,185,229,199,-1,230,201,200,-1,229,230,200,-1,230,257,201,-1,203,202,73,-1,203,162,202,-1,205,193,204,-1,206,228,185,-1,198,8,155,-1,198,155,202,-1,155,73,202,-1,199,6,8,-1,199,8,198,-1,7,6,199,-1,7,199,200,-1,201,9,7,-1,201,7,200,-1,201,257,9,-1,188,194,195,-1,188,195,182,-1,195,187,182,-1,80,79,76,-1,80,62,75,-1,80,76,62,-1,47,50,33,-1,131,118,130,-1,20,21,47,-1,21,46,47,-1,20,33,19,-1,20,47,33,-1,33,30,19,-1,30,18,19,-1,62,60,251,-1,60,250,251,-1,252,61,251,-1,61,62,251,-1,252,63,61,-1,252,253,63,-1,166,130,167,-1,130,128,167,-1,166,131,130,-1,166,165,131,-1,165,157,131,-1,165,164,157,-1,224,181,182,-1,224,225,181,-1,224,183,223,-1,224,182,183,-1,183,184,223,-1,184,222,223,-1]
IndexedFaceSet426.creaseAngle = 0.7854
Coordinate427 = x3d.Coordinate()
Coordinate427.DEF = "Face"
Coordinate427.point = (0.0000,1.7080,-0.0435,0.0000,1.6550,0.0432,0.0000,1.4860,0.0233,0.0000,1.6940,0.0078,0.0000,1.6310,0.0510,0.0000,1.5240,-0.1020,0.0400,1.5100,-0.0728,0.0403,1.5140,-0.0825,0.0353,1.5020,-0.0501,0.0348,1.5170,-0.0927,0.0116,1.4940,0.0338,0.0195,1.5200,0.0342,0.0220,1.4940,0.0272,0.0273,1.4980,0.0221,0.0279,1.5280,0.0308,0.0338,1.5030,0.0124,0.0401,1.5090,0.0028,0.0512,1.5180,-0.0278,0.0587,1.5440,-0.0332,0.0643,1.5630,-0.0368,0.0673,1.5830,-0.0368,0.0677,1.6170,-0.0344,0.0664,1.6370,-0.0305,0.0682,1.6370,-0.0428,0.0631,1.6660,-0.0404,0.0530,1.6850,-0.0399,0.0314,1.7000,-0.0413,0.0292,1.6880,0.0091,0.0527,1.6740,-0.0017,0.0606,1.6600,-0.0101,0.0525,1.5410,-0.0136,0.0410,1.5270,0.0088,0.0353,1.5240,0.0210,0.0579,1.5570,-0.0043,0.0441,1.5390,0.0149,0.0375,1.5390,0.0266,0.0034,1.5240,0.0415,0.0148,1.5260,0.0391,0.0051,1.5320,0.0436,0.0244,1.5420,0.0358,0.0264,1.5500,0.0381,0.0061,1.5500,0.0545,0.0000,1.5590,0.0550,0.0296,1.6510,0.0396,0.0485,1.6430,0.0290,0.0586,1.6300,0.0180,0.0618,1.6140,0.0082,0.0619,1.6000,0.0027,0.0149,1.5830,0.0411,0.0528,1.5690,0.0282,0.0577,1.5800,0.0184,0.0464,1.6250,0.0370,0.0264,1.6280,0.0481,0.0556,1.6090,0.0258,0.0547,1.5990,0.0215,0.0532,1.5890,0.0207,0.0360,1.5800,0.0354,0.0460,1.5860,0.0290,0.0211,1.5920,0.0375,0.0343,1.5950,0.0329,0.0681,1.6170,-0.0611,0.0671,1.5640,-0.0700,0.0699,1.5940,-0.0824,0.0532,1.5360,-0.0592,0.0490,1.5210,-0.0513,0.0476,1.5140,-0.0311,0.0354,1.5030,-0.0009,0.0300,1.4980,0.0062,0.0231,1.4920,0.0163,0.0177,1.4880,0.0214,0.0138,1.4880,0.0248,0.0435,1.5120,-0.0399,0.0231,1.4990,-0.0209,0.0000,1.4870,-0.0180,0.0479,1.5310,-0.0897,0.0574,1.5550,-0.0982,0.0682,1.6220,-0.1070,0.0687,1.6550,-0.0847,0.0523,1.6780,-0.0964,0.0533,1.6310,-0.1239,0.0501,1.5810,-0.1193,0.0436,1.5510,-0.1067,0.0384,1.5280,-0.0965,0.0340,1.6360,-0.1304,0.0322,1.6850,-0.1024,0.0000,1.5570,-0.1126,0.0186,1.5660,0.0411,0.0249,1.5800,0.0387,0.0273,1.5960,0.0355,0.0432,1.5640,0.0364,0.0125,1.5770,0.0428,0.0435,1.5900,0.0282,0.0456,1.6010,0.0365,0.0291,1.6030,0.0427,0.0186,1.6000,0.0435,0.0000,1.5790,0.0489,0.0106,1.5580,0.0448,0.0055,1.5780,0.0457,0.0140,1.5310,0.0415,0.0104,1.5440,0.0427,0.0000,1.5150,0.0384,0.0080,1.5150,0.0377,0.0182,1.5500,0.0406,-0.0249,1.5800,0.0387,-0.0435,1.5900,0.0282,-0.0291,1.6030,0.0427,-0.0432,1.5640,0.0364,-0.0460,1.5860,0.0290,-0.0532,1.5890,0.0207,-0.0182,1.5500,0.0406,-0.0125,1.5770,0.0428,-0.0061,1.5500,0.0545,-0.0104,1.5440,0.0427,-0.0264,1.5500,0.0381,-0.0343,1.5950,0.0329,-0.0273,1.5960,0.0355,-0.0360,1.5800,0.0354,-0.0528,1.5690,0.0282,-0.0577,1.5800,0.0184,-0.0186,1.5660,0.0411,-0.0149,1.5830,0.0411,-0.0556,1.6090,0.0258,-0.0456,1.6010,0.0365,-0.0211,1.5920,0.0375,-0.0186,1.6000,0.0435,-0.0055,1.5780,0.0457,-0.0106,1.5580,0.0448,0.0000,1.5920,0.0469,-0.0618,1.6140,0.0082,-0.0547,1.5990,0.0215,-0.0619,1.6000,0.0027,-0.0579,1.5570,-0.0043,-0.0441,1.5390,0.0149,-0.0375,1.5390,0.0266,-0.0410,1.5270,0.0088,-0.0353,1.5240,0.0210,-0.0279,1.5280,0.0308,0.0000,1.5300,0.0424,-0.0051,1.5320,0.0436,-0.0148,1.5260,0.0391,-0.0195,1.5200,0.0342,0.0000,1.4950,0.0348,-0.0116,1.4940,0.0338,-0.0273,1.4980,0.0221,-0.0338,1.5030,0.0124,-0.0177,1.4880,0.0214,-0.0231,1.4920,0.0163,-0.0300,1.4980,0.0062,-0.0140,1.5310,0.0415,-0.0034,1.5240,0.0415,-0.0220,1.4940,0.0272,-0.0080,1.5150,0.0377,-0.0244,1.5420,0.0358,0.0000,1.5430,0.0443,0.0000,1.5550,0.0569,0.0230,1.4920,-0.0269,0.0073,1.4890,-0.0168,-0.0525,1.5410,-0.0136,-0.0401,1.5090,0.0028,-0.0512,1.5180,-0.0278,-0.0354,1.5030,-0.0009,-0.0138,1.4880,0.0248,-0.0231,1.4990,-0.0209,-0.0435,1.5120,-0.0399,-0.0587,1.5440,-0.0332,-0.0643,1.5630,-0.0368,-0.0673,1.5830,-0.0368,-0.0677,1.6170,-0.0344,-0.0586,1.6300,0.0180,-0.0485,1.6430,0.0290,-0.0464,1.6250,0.0370,-0.0296,1.6510,0.0396,-0.0264,1.6280,0.0481,-0.0292,1.6880,0.0091,-0.0527,1.6740,-0.0017,-0.0664,1.6370,-0.0305,-0.0606,1.6600,-0.0101,-0.0314,1.7000,-0.0413,-0.0530,1.6850,-0.0399,-0.0631,1.6660,-0.0404,-0.0682,1.6370,-0.0428,-0.0681,1.6170,-0.0611,-0.0699,1.5940,-0.0824,-0.0671,1.5640,-0.0700,-0.0532,1.5360,-0.0592,-0.0490,1.5210,-0.0513,-0.0479,1.5310,-0.0897,-0.0574,1.5550,-0.0982,-0.0682,1.6220,-0.1070,-0.0687,1.6550,-0.0847,-0.0523,1.6780,-0.0964,-0.0322,1.6850,-0.1024,0.0000,1.6900,-0.1047,0.0000,1.6400,-0.1342,-0.0533,1.6310,-0.1239,-0.0501,1.5810,-0.1193,-0.0436,1.5510,-0.1067,-0.0384,1.5280,-0.0965,-0.0353,1.5020,-0.0501,-0.0400,1.5100,-0.0728,-0.0403,1.5140,-0.0825,-0.0348,1.5170,-0.0927,-0.0230,1.4920,-0.0269,-0.0073,1.4890,-0.0168,0.0000,1.5880,-0.1329,-0.0340,1.6360,-0.1304,-0.0476,1.5140,-0.0311,-0.0343,1.5950,0.0329,-0.0211,1.5920,0.0375,-0.0273,1.5960,0.0355,-0.0249,1.5800,0.0387,-0.0149,1.5830,0.0411,-0.0460,1.5860,0.0290,-0.0435,1.5900,0.0282,-0.0360,1.5800,0.0354,-0.0586,1.6300,0.0180,-0.0618,1.6140,0.0082,-0.0279,1.5280,0.0308,-0.0051,1.5320,0.0436,-0.0140,1.5310,0.0415,-0.0080,1.5150,0.0377,-0.0195,1.5200,0.0342,-0.0587,1.5440,-0.0332,-0.0643,1.5630,-0.0368,-0.0673,1.5830,-0.0368,-0.0677,1.6170,-0.0344,-0.0485,1.6430,0.0290,-0.0296,1.6510,0.0396,-0.0532,1.5360,-0.0592,-0.0479,1.5310,-0.0897,-0.0384,1.5280,-0.0965,0.0211,1.5920,0.0375,0.0149,1.5830,0.0411,0.0249,1.5800,0.0387,0.0360,1.5800,0.0354,0.0435,1.5900,0.0282,0.0343,1.5950,0.0329,0.0273,1.5960,0.0355,0.0279,1.5280,0.0308,0.0140,1.5310,0.0415,0.0000,1.5300,0.0424,0.0000,1.5150,0.0384,0.0080,1.5150,0.0377,0.0195,1.5200,0.0342,0.0051,1.5320,0.0436,0.0000,1.6550,0.0432,0.0296,1.6510,0.0396,0.0485,1.6430,0.0290,0.0586,1.6300,0.0180,0.0618,1.6140,0.0082,0.0677,1.6170,-0.0344,0.0673,1.5830,-0.0368,0.0643,1.5630,-0.0368,0.0587,1.5440,-0.0332,0.0532,1.5360,-0.0592,0.0479,1.5310,-0.0897,0.0384,1.5280,-0.0965,0.0000,1.5240,-0.1020)

IndexedFaceSet426.coord = Coordinate427
Color428 = x3d.Color()
Color428.color = [0.749,0.601,0.462,0.1735,0.2602,0.749,0.6364,0.133,0.1526,0.4545,0.2759,0.1902,0,0,0.502]

IndexedFaceSet426.color = Color428

Shape423.geometry = IndexedFaceSet426

fieldValue422.children.append(Shape423)
Transform429 = x3d.Transform()
Transform429.DEF = "maskAndSnorkel"
Transform429.translation = [0,1.505,0.05]
Transform430 = x3d.Transform()
Shape431 = x3d.Shape()
Shape431.DEF = "maskFrame"
Appearance432 = x3d.Appearance()
Material433 = x3d.Material()
Material433.DEF = "frameColor"
Material433.diffuseColor = [0,0,0]

Appearance432.material = Material433

Shape431.appearance = Appearance432
IndexedFaceSet434 = x3d.IndexedFaceSet()
IndexedFaceSet434.coordIndex = [0,1,13,12,0,-1,1,2,14,13,1,-1,2,3,15,14,2,-1,3,4,16,15,3,-1,4,5,17,16,4,-1,5,6,18,17,5,-1,18,6,25,19,0,12,18,-1,0,19,20,11,0,-1,10,11,20,21,10,-1,9,10,21,22,9,-1,8,9,22,23,8,-1,23,24,7,8,23,-1,6,7,24,25,6,-1]
IndexedFaceSet434.creaseAngle = 1.45
IndexedFaceSet434.solid = False
Coordinate435 = x3d.Coordinate()
Coordinate435.point = (0.0000,0.0800,0.0000,0.0200,0.0500,0.0000,0.0500,0.0500,0.0000,0.0600,0.0600,0.0000,0.0600,0.0900,0.0000,0.0500,0.1000,0.0000,0.0000,0.1000,0.0000,-0.0500,0.1000,0.0000,-0.0600,0.0900,0.0000,-0.0600,0.0600,0.0000,-0.0500,0.0500,0.0000,-0.0200,0.0500,0.0000,0.0050,0.0800,0.0000,0.0200,0.0550,0.0000,0.0500,0.0550,0.0000,0.0550,0.0600,0.0000,0.0550,0.0900,0.0000,0.0450,0.0950,0.0000,0.0050,0.0950,0.0000,-0.0050,0.0800,0.0000,-0.0200,0.0550,0.0000,-0.0500,0.0550,0.0000,-0.0550,0.0600,0.0000,-0.0550,0.0900,0.0000,-0.0450,0.0950,0.0000,-0.0050,0.0950,0.0000)

IndexedFaceSet434.coord = Coordinate435

Shape431.geometry = IndexedFaceSet434

Transform430.children.append(Shape431)

Transform429.children.append(Transform430)
Transform436 = x3d.Transform()
Transform436.DEF = "snorkelHoldRing"
Transform436.translation = [0.075,0.075,-0.02]
Shape437 = x3d.Shape()
Appearance438 = x3d.Appearance()
Material439 = x3d.Material()
Material439.USE = "frameColor"

Appearance438.material = Material439

Shape437.appearance = Appearance438
Cylinder440 = x3d.Cylinder()
Cylinder440.height = 0.003
Cylinder440.radius = 0.015

Shape437.geometry = Cylinder440

Transform436.children.append(Shape437)

Transform429.children.append(Transform436)
Group441 = x3d.Group()
Group441.DEF = "snorkel"
Transform442 = x3d.Transform()
Transform442.translation = [0,-0.02,0]
Transform443 = x3d.Transform()
Transform443.scale = [0.9,0.9,0.9]
Transform443.translation = [0.035,-0.07,-0.02]
Shape444 = x3d.Shape()
Appearance445 = x3d.Appearance()
Material446 = x3d.Material()
Material446.DEF = "snorkelTube"
Material446.diffuseColor = [0.678,1,0.184]
Material446.transparency = 0.4

Appearance445.material = Material446

Shape444.appearance = Appearance445
Extrusion447 = x3d.Extrusion()
Extrusion447.crossSection = [0,0.013,0.00494,0.01196,0.00923,0.00923,0.01196,0.00494,0.013,0,0.01196,-0.00494,0.00923,-0.00923,0.00494,-0.01196,0,0.013,-0.00494,-0.01196,-0.00923,-0.00923,-0.01196,-0.00494,-0.013,0,-0.01196,0.00494,-0.00923,0.00923,-0.00494,0.01196,0,0.013]
Extrusion447.spine = (-0.0100,-0.0400,0.0000,0.0000,0.0000,0.0000,0.0300,0.0500,0.0000,0.0500,0.2000,0.0000,0.0300,0.4000,0.0300)

Shape444.geometry = Extrusion447

Transform443.children.append(Shape444)

Transform442.children.append(Transform443)
Transform448 = x3d.Transform()
Transform448.rotation = [0,0,1,1.57]
Transform448.scale = [0.9,0.9,0.9]
Transform448.translation = [0.01,-0.04,-0.02]
Shape449 = x3d.Shape()
Appearance450 = x3d.Appearance()
Material451 = x3d.Material()
Material451.DEF = "Mouthpiece"
Material451.diffuseColor = [0.678,1,0.8]
Material451.transparency = 0.4

Appearance450.material = Material451

Shape449.appearance = Appearance450
Extrusion452 = x3d.Extrusion()
Extrusion452.crossSection = [0,0.013,0.00494,0.01196,0.00923,0.00923,0.01196,0.00494,0.013,0,0.01196,-0.00494,0.00923,-0.00923,0.00494,-0.01196,0,0.013,-0.00494,-0.01196,-0.00923,-0.00923,-0.01196,-0.00494,-0.013,0,-0.01196,0.00494,-0.00923,0.00923,-0.00494,0.01196,0,0.013]
Extrusion452.spine = (-0.0100,-0.0300,0.0000,0.0000,0.0000,0.0000,0.0200,0.0100,0.0000)

Shape449.geometry = Extrusion452

Transform448.children.append(Shape449)

Transform442.children.append(Transform448)
Transform453 = x3d.Transform()
Transform453.rotation = [0,0,1,-0.85]
Transform453.scale = [0.9,0.9,0.9]
Transform453.translation = [0.005,-0.01,-0.02]
Shape454 = x3d.Shape()
Appearance455 = x3d.Appearance()
Material456 = x3d.Material()
Material456.USE = "Mouthpiece"

Appearance455.material = Material456

Shape454.appearance = Appearance455
Extrusion457 = x3d.Extrusion()
Extrusion457.crossSection = [0,0.013,0.00494,0.01196,0.00923,0.00923,0.01196,0.00494,0.013,0,0.01196,-0.00494,0.00923,-0.00923,0.00494,-0.01196,0,0.013]
Extrusion457.spine = (-0.0200,-0.0300,0.0000,-0.0100,-0.0300,0.0000,0.0000,-0.0175,0.0000,0.0000,-0.0135,0.0000,-0.0100,0.0000,0.0000,-0.0200,0.0000,0.0000)

Shape454.geometry = Extrusion457

Transform453.children.append(Shape454)

Transform442.children.append(Transform453)

Group441.children.append(Transform442)

Transform429.children.append(Group441)
Transform458 = x3d.Transform()
Shape459 = x3d.Shape()
Shape459.DEF = "maskLensR"
Appearance460 = x3d.Appearance()
Material461 = x3d.Material()
Material461.DEF = "plastic"
Material461.diffuseColor = [0.941,0.973,1]
Material461.transparency = 0.8

Appearance460.material = Material461

Shape459.appearance = Appearance460
IndexedFaceSet462 = x3d.IndexedFaceSet()
IndexedFaceSet462.coordIndex = [12,1314,15,16,17,18,12,-1]
IndexedFaceSet462.creaseAngle = 1.45
IndexedFaceSet462.solid = False
Coordinate463 = x3d.Coordinate()
Coordinate463.point = (0.0000,0.0800,0.0000,0.0200,0.0500,0.0000,0.0500,0.0500,0.0000,0.0600,0.0600,0.0000,0.0600,0.0900,0.0000,0.0500,0.1000,0.0000,0.0000,0.1000,0.0000,-0.0500,0.1000,0.0000,-0.0600,0.0900,0.0000,-0.0600,0.0600,0.0000,-0.0500,0.0500,0.0000,-0.0200,0.0500,0.0000,0.0050,0.0800,0.0000,0.0200,0.0550,0.0000,0.0500,0.0550,0.0000,0.0550,0.0600,0.0000,0.0550,0.0900,0.0000,0.0450,0.0950,0.0000,0.0050,0.0950,0.0000,-0.0050,0.0800,0.0000,-0.0200,0.0550,0.0000,-0.0500,0.0550,0.0000,-0.0550,0.0600,0.0000,-0.0550,0.0900,0.0000,-0.0450,0.0950,0.0000,-0.0050,0.0950,0.0000)

IndexedFaceSet462.coord = Coordinate463

Shape459.geometry = IndexedFaceSet462

Transform458.children.append(Shape459)

Transform429.children.append(Transform458)
Transform464 = x3d.Transform()
Shape465 = x3d.Shape()
Shape465.DEF = "maskLensL"
Appearance466 = x3d.Appearance()
Material467 = x3d.Material()
Material467.USE = "plastic"

Appearance466.material = Material467

Shape465.appearance = Appearance466
IndexedFaceSet468 = x3d.IndexedFaceSet()
IndexedFaceSet468.coordIndex = [19,20,21,22,23,24,25,19,-1]
IndexedFaceSet468.creaseAngle = 1.45
IndexedFaceSet468.solid = False
Coordinate469 = x3d.Coordinate()
Coordinate469.point = (0.0000,0.0800,0.0000,0.0200,0.0500,0.0000,0.0500,0.0500,0.0000,0.0600,0.0600,0.0000,0.0600,0.0900,0.0000,0.0500,0.1000,0.0000,0.0000,0.1000,0.0000,-0.0500,0.1000,0.0000,-0.0600,0.0900,0.0000,-0.0600,0.0600,0.0000,-0.0500,0.0500,0.0000,-0.0200,0.0500,0.0000,0.0050,0.0800,0.0000,0.0200,0.0550,0.0000,0.0500,0.0550,0.0000,0.0550,0.0600,0.0000,0.0550,0.0900,0.0000,0.0450,0.0950,0.0000,0.0050,0.0950,0.0000,-0.0050,0.0800,0.0000,-0.0200,0.0550,0.0000,-0.0500,0.0550,0.0000,-0.0550,0.0600,0.0000,-0.0550,0.0900,0.0000,-0.0450,0.0950,0.0000,-0.0050,0.0950,0.0000)

IndexedFaceSet468.coord = Coordinate469

Shape465.geometry = IndexedFaceSet468

Transform464.children.append(Shape465)

Transform429.children.append(Transform464)
Transform470 = x3d.Transform()
Shape471 = x3d.Shape()
Shape471.DEF = "nose"
Appearance472 = x3d.Appearance()
Material473 = x3d.Material()
Material473.DEF = "plasticFit"
Material473.diffuseColor = [0.678,1,0.184]
Material473.transparency = 0.7

Appearance472.material = Material473

Shape471.appearance = Appearance472
IndexedFaceSet474 = x3d.IndexedFaceSet()
IndexedFaceSet474.coordIndex = [0,37,26,0,-1,0,36,26,0,-1,36,37,26,36,-1,0,1,37,0,-1,0,11,36,0,-1]
IndexedFaceSet474.creaseAngle = 1.45
IndexedFaceSet474.solid = False
Coordinate475 = x3d.Coordinate()
Coordinate475.point = (0.0000,0.0800,0.0000,0.0200,0.0500,0.0000,0.0500,0.0500,0.0000,0.0600,0.0600,0.0000,0.0600,0.0900,0.0000,0.0500,0.1000,0.0000,0.0000,0.1000,0.0000,-0.0500,0.1000,0.0000,-0.0600,0.0900,0.0000,-0.0600,0.0600,0.0000,-0.0500,0.0500,0.0000,-0.0200,0.0500,0.0000,0.0050,0.0800,0.0000,0.0200,0.0550,0.0000,0.0500,0.0550,0.0000,0.0550,0.0600,0.0000,0.0550,0.0900,0.0000,0.0450,0.0950,0.0000,0.0050,0.0950,0.0000,-0.0050,0.0800,0.0000,-0.0200,0.0550,0.0000,-0.0500,0.0550,0.0000,-0.0550,0.0600,0.0000,-0.0550,0.0900,0.0000,-0.0450,0.0950,0.0000,-0.0050,0.0950,0.0000,0.0000,0.0400,0.0150,0.0500,0.0400,-0.0300,0.0600,0.0500,-0.0300,0.0700,0.0950,-0.0300,0.0550,0.1100,-0.0300,0.0000,0.1100,-0.0200,-0.0550,0.1100,-0.0300,-0.0700,0.0950,-0.0300,-0.0600,0.0500,-0.0300,-0.0500,0.0400,-0.0300,-0.0200,0.0400,-0.0200,0.0200,0.0400,-0.0200)

IndexedFaceSet474.coord = Coordinate475

Shape471.geometry = IndexedFaceSet474

Transform470.children.append(Shape471)

Transform429.children.append(Transform470)
Transform476 = x3d.Transform()
Shape477 = x3d.Shape()
Shape477.DEF = "faceFit"
Appearance478 = x3d.Appearance()
Material479 = x3d.Material()
Material479.USE = "plasticFit"

Appearance478.material = Material479

Shape477.appearance = Appearance478
IndexedFaceSet480 = x3d.IndexedFaceSet()
IndexedFaceSet480.coordIndex = [1,2,27,37,1,-1,2,3,28,27,2,-1,3,4,29,28,3,-1,4,5,30,29,4,-1,5,6,31,30,5,-1,6,7,32,31,6,-1,7,8,33,32,7,-1,8,9,34,33,8,-1,9,10,35,34,9,-1,10,11,36,35,10,-1]
IndexedFaceSet480.creaseAngle = 1.45
IndexedFaceSet480.solid = False
Coordinate481 = x3d.Coordinate()
Coordinate481.point = (0.0000,0.0800,0.0000,0.0200,0.0500,0.0000,0.0500,0.0500,0.0000,0.0600,0.0600,0.0000,0.0600,0.0900,0.0000,0.0500,0.1000,0.0000,0.0000,0.1000,0.0000,-0.0500,0.1000,0.0000,-0.0600,0.0900,0.0000,-0.0600,0.0600,0.0000,-0.0500,0.0500,0.0000,-0.0200,0.0500,0.0000,0.0050,0.0800,0.0000,0.0200,0.0550,0.0000,0.0500,0.0550,0.0000,0.0550,0.0600,0.0000,0.0550,0.0900,0.0000,0.0450,0.0950,0.0000,0.0050,0.0950,0.0000,-0.0050,0.0800,0.0000,-0.0200,0.0550,0.0000,-0.0500,0.0550,0.0000,-0.0550,0.0600,0.0000,-0.0550,0.0900,0.0000,-0.0450,0.0950,0.0000,-0.0050,0.0950,0.0000,0.0000,0.0500,0.0150,0.0500,0.0400,-0.0300,0.0600,0.0500,-0.0300,0.0700,0.0950,-0.0300,0.0550,0.1100,-0.0300,0.0000,0.1100,-0.0200,-0.0550,0.1100,-0.0300,-0.0700,0.0950,-0.0300,-0.0600,0.0500,-0.0300,-0.0500,0.0400,-0.0300,-0.0200,0.0400,-0.0200,0.0200,0.0400,-0.0200)

IndexedFaceSet480.coord = Coordinate481

Shape477.geometry = IndexedFaceSet480

Transform476.children.append(Shape477)

Transform429.children.append(Transform476)
Transform482 = x3d.Transform()
Shape483 = x3d.Shape()
Shape483.DEF = "belt"
Appearance484 = x3d.Appearance()
Material485 = x3d.Material()
Material485.USE = "plastic"

Appearance484.material = Material485

Shape483.appearance = Appearance484
IndexedFaceSet486 = x3d.IndexedFaceSet()
IndexedFaceSet486.coordIndex = [3,4,39,38,3,-1,8,9,40,41,8,-1,38,39,42,43,38,-1,40,41,44,45,40,-1,42,43,47,46,42,-1,44,45,47,46,44,-1]
IndexedFaceSet486.creaseAngle = 1.45
IndexedFaceSet486.solid = False
Coordinate487 = x3d.Coordinate()
Coordinate487.point = (0.0000,0.0800,0.0000,0.0200,0.0500,0.0000,0.0500,0.0500,0.0000,0.0600,0.0600,0.0000,0.0600,0.0900,0.0000,0.0500,0.1000,0.0000,0.0000,0.1000,0.0000,-0.0500,0.1000,0.0000,-0.0600,0.0900,0.0000,-0.0600,0.0600,0.0000,-0.0500,0.0500,0.0000,-0.0200,0.0500,0.0000,0.0050,0.0800,0.0000,0.0200,0.0550,0.0000,0.0500,0.0550,0.0000,0.0550,0.0600,0.0000,0.0550,0.0900,0.0000,0.0450,0.0950,0.0000,0.0050,0.0950,0.0000,-0.0050,0.0800,0.0000,-0.0200,0.0550,0.0000,-0.0500,0.0550,0.0000,-0.0550,0.0600,0.0000,-0.0550,0.0900,0.0000,-0.0450,0.0950,0.0000,-0.0050,0.0950,0.0000,0.0000,0.0500,0.0150,0.0500,0.0400,-0.0300,0.0600,0.0500,-0.0300,0.0700,0.0950,-0.0300,0.0550,0.1100,-0.0300,0.0000,0.1100,-0.0200,-0.0550,0.1100,-0.0300,-0.0700,0.0950,-0.0300,-0.0600,0.0500,-0.0300,-0.0500,0.0400,-0.0300,-0.0200,0.0400,-0.0200,0.0200,0.0400,-0.0200,0.0750,0.0600,-0.1350,0.0750,0.0900,-0.1350,-0.0750,0.0600,-0.1350,-0.0750,0.0900,-0.1350,0.0600,0.0900,-0.1650,0.0600,0.0600,-0.1650,-0.0600,0.0900,-0.1650,-0.0600,0.0600,-0.1650,0.0000,0.0900,-0.2000,0.0000,0.0600,-0.1750)

IndexedFaceSet486.coord = Coordinate487

Shape483.geometry = IndexedFaceSet486

Transform482.children.append(Shape483)

Transform429.children.append(Transform482)

fieldValue422.children.append(Transform429)
Transform488 = x3d.Transform()
Transform488.DEF = "mouthpiece"
Transform488.rotation = [0.86,-0.58,-0.58,2.09]
Transform488.translation = [0,1.508,0.05]
Transform489 = x3d.Transform()
Transform489.translation = [0,0.0018,0]
Shape490 = x3d.Shape()
Appearance491 = x3d.Appearance()
Material492 = x3d.Material()
Material492.DEF = "gray"
Material492.ambientIntensity = 0.3
Material492.diffuseColor = [0.9,0.9,0.89]
Material492.shininess = 0.1
Material492.specularColor = [0.5,0.5,0.5]

Appearance491.material = Material492

Shape490.appearance = Appearance491
Cylinder493 = x3d.Cylinder()
Cylinder493.height = 0.006
Cylinder493.radius = 0.015

Shape490.geometry = Cylinder493

Transform489.children.append(Shape490)

Transform488.children.append(Transform489)
Transform494 = x3d.Transform()
Shape495 = x3d.Shape()
Appearance496 = x3d.Appearance()
Material497 = x3d.Material()
Material497.DEF = "black"
Material497.diffuseColor = [0,0,0]

Appearance496.material = Material497

Shape495.appearance = Appearance496
Cone498 = x3d.Cone()
Cone498.bottomRadius = 0.03
Cone498.height = 0.01

Shape495.geometry = Cone498

Transform494.children.append(Shape495)

Transform488.children.append(Transform494)
Transform499 = x3d.Transform()
Transform499.translation = [0,-0.015,0]
Shape500 = x3d.Shape()
Appearance501 = x3d.Appearance()
Material502 = x3d.Material()
Material502.USE = "black"

Appearance501.material = Material502

Shape500.appearance = Appearance501
Cylinder503 = x3d.Cylinder()
Cylinder503.height = 0.02
Cylinder503.radius = 0.03

Shape500.geometry = Cylinder503

Transform499.children.append(Shape500)

Transform488.children.append(Transform499)
Transform504 = x3d.Transform()
Transform504.translation = [0,-0.025,0]
Shape505 = x3d.Shape()
Appearance506 = x3d.Appearance()
Material507 = x3d.Material()
Material507.USE = "black"

Appearance506.material = Material507

Shape505.appearance = Appearance506
Cylinder508 = x3d.Cylinder()
Cylinder508.height = 0.02
Cylinder508.radius = 0.015

Shape505.geometry = Cylinder508

Transform504.children.append(Shape505)

Transform488.children.append(Transform504)
Transform509 = x3d.Transform()
Transform509.rotation = [0,0,1,0.9]
Transform509.translation = [0,-0.04,0]
Shape510 = x3d.Shape()
Shape510.DEF = "mouthpiecePlastic"
Appearance511 = x3d.Appearance()
Material512 = x3d.Material()
Material512.diffuseColor = [1,1,1]
Material512.emissiveColor = [1,1,1]

Appearance511.material = Material512

Shape510.appearance = Appearance511
Box513 = x3d.Box()
Box513.size = [0.002,0.03,0.018]

Shape510.geometry = Box513

Transform509.children.append(Shape510)

Transform488.children.append(Transform509)
Transform514 = x3d.Transform()
Transform514.rotation = [0,0,1,-0.9]
Transform514.translation = [0,-0.04,0]
Shape515 = x3d.Shape()
Shape515.USE = "mouthpiecePlastic"

Transform514.children.append(Shape515)

Transform488.children.append(Transform514)
Transform516 = x3d.Transform()
Transform516.rotation = [1,0,0,1.57]
Transform516.translation = [0,-0.015,0.03]
Shape517 = x3d.Shape()
Appearance518 = x3d.Appearance()
Material519 = x3d.Material()
Material519.USE = "gray"

Appearance518.material = Material519

Shape517.appearance = Appearance518
Cylinder520 = x3d.Cylinder()
Cylinder520.height = 0.02
Cylinder520.radius = 0.0075

Shape517.geometry = Cylinder520

Transform516.children.append(Shape517)

Transform488.children.append(Transform516)
#x = 0, y = 50, z = -270
Transform521 = x3d.Transform()
Transform521.DEF = "airTube"
Transform521.rotation = [0,1,0,1.57]
Transform521.scale = [0.7,0.7,0.7]
Transform521.translation = [0,-0.02,0.055]
Transform522 = x3d.Transform()
Transform522.rotation = [-0.21,0.21,-0.95,4.67]
Shape523 = x3d.Shape()
Appearance524 = x3d.Appearance()
Material525 = x3d.Material()
Material525.diffuseColor = [0,0,0]

Appearance524.material = Material525

Shape523.appearance = Appearance524
Extrusion526 = x3d.Extrusion()
Extrusion526.crossSection = [0,0.013,0.00494,0.01196,0.00923,0.00923,0.01196,0.00494,0.013,0,0.01196,-0.00494,0.00923,-0.00923,0.00494,-0.01196,0,0.013,-0.00494,-0.01196,-0.00923,-0.00923,-0.01196,-0.00494,-0.013,0,-0.01196,0.00494,-0.00923,0.00923,-0.00494,0.01196,0,0.013]
Extrusion526.spine = (0.0050,-0.0300,0.0000,-0.0100,0.0200,0.0000,-0.0300,0.0800,0.0000,-0.0500,0.1400,0.0000,-0.0800,0.1900,0.0000,-0.1000,0.2200,0.0000,-0.1200,0.2500,0.0000,-0.1500,0.2700,0.0000,-0.1800,0.2800,0.0000,-0.2100,0.2900,0.0000,-0.2600,0.2800,0.0000,-0.2800,0.2600,0.0000,-0.3050,0.2300,0.0000,-0.3200,0.2000,0.0000,-0.3400,0.1600,0.0000,-0.3500,0.1200,0.0000,-0.3700,0.0400,0.0000,-0.3850,0.0000,0.0000,-0.3900,-0.0700,0.0000)

Shape523.geometry = Extrusion526

Transform522.children.append(Shape523)

Transform521.children.append(Transform522)

Transform488.children.append(Transform521)

fieldValue422.children.append(Transform488)
Transform527 = x3d.Transform()
Transform527.DEF = "Bubbles"
Transform527.scale = [0.35,0.35,0.35]
Transform527.translation = [0,1.508,0.05]
Group528 = x3d.Group()
Group528.DEF = "Bubble"
TimeSensor529 = x3d.TimeSensor()
TimeSensor529.DEF = "BubbleClock"
TimeSensor529.cycleInterval = 6
TimeSensor529.loop = True

Group528.children.append(TimeSensor529)
PositionInterpolator530 = x3d.PositionInterpolator()
PositionInterpolator530.DEF = "BubblePath1"
PositionInterpolator530.key = [0,0.5,0.8,0.9,1]
PositionInterpolator530.keyValue = (0.0000,0.0000,0.0000,0.7500,0.7500,0.7500,0.8600,0.8600,0.8600,0.9900,0.9980,0.9876,1.2720,1.9044,0.9509)

Group528.children.append(PositionInterpolator530)
PositionInterpolator531 = x3d.PositionInterpolator()
PositionInterpolator531.DEF = "BubblePath2"
PositionInterpolator531.key = [0,0.3,0.64,0.85,1]
PositionInterpolator531.keyValue = (0.1000,0.1000,0.1000,0.2000,0.4000,0.2500,0.3000,0.5000,0.4600,0.7500,0.5000,0.5750,0.0385,1.9890,1.0984)

Group528.children.append(PositionInterpolator531)
PositionInterpolator532 = x3d.PositionInterpolator()
PositionInterpolator532.DEF = "BubblePath3"
PositionInterpolator532.key = [0,0.1,0.45,0.7,1]
PositionInterpolator532.keyValue = (0.0100,0.0100,0.0100,0.2500,0.3500,0.0045,0.5500,0.6000,0.0055,0.6600,0.6650,0.0066,1.5550,1.0904,0.0057)

Group528.children.append(PositionInterpolator532)
PositionInterpolator533 = x3d.PositionInterpolator()
PositionInterpolator533.DEF = "BubblePath4"
PositionInterpolator533.key = [0,0.5,0.6,0.8,1]
PositionInterpolator533.keyValue = (0.0000,0.0000,0.0000,0.5000,0.5000,0.0050,0.6000,0.6000,0.0060,0.7500,0.7500,0.0075,1.9486,1.3983,0.0090)

Group528.children.append(PositionInterpolator533)
PositionInterpolator534 = x3d.PositionInterpolator()
PositionInterpolator534.DEF = "BubblePath5"
PositionInterpolator534.key = [0,0.25,0.35,0.65,1]
PositionInterpolator534.keyValue = (0.0000,0.0000,0.0000,0.5000,0.5000,0.0050,0.6000,0.6000,0.0060,0.7500,0.7500,0.0075,1.8444,1.2222,0.1000)

Group528.children.append(PositionInterpolator534)
PositionInterpolator535 = x3d.PositionInterpolator()
PositionInterpolator535.DEF = "BubblePath6"
PositionInterpolator535.key = [0,0.15,0.22235,0.55565,1]
PositionInterpolator535.keyValue = (0.0000,0.0000,0.0000,0.2350,0.3455,0.0055,0.3560,0.6760,0.0046,0.5675,0.7500,0.0075,1.0980,1.0343,0.1400)

Group528.children.append(PositionInterpolator535)
PositionInterpolator536 = x3d.PositionInterpolator()
PositionInterpolator536.DEF = "BubblePath7"
PositionInterpolator536.key = [0,0.2425,0.4535,0.6775,1]
PositionInterpolator536.keyValue = (0.0000,0.0000,0.0000,0.1235,0.2225,0.0034,0.7860,0.4560,0.0067,0.7456,0.7335,0.0023,0.0879,1.0220,0.1200)

Group528.children.append(PositionInterpolator536)
PositionInterpolator537 = x3d.PositionInterpolator()
PositionInterpolator537.DEF = "BubblePath8"
PositionInterpolator537.key = [0,0.1125,0.5535,0.97865,1]
PositionInterpolator537.keyValue = (0.0000,0.0000,0.0000,0.1235,0.0500,0.0013,0.5666,0.4346,0.0056,0.8975,0.3458,0.0099,1.8787,1.6860,0.8600)

Group528.children.append(PositionInterpolator537)
PositionInterpolator538 = x3d.PositionInterpolator()
PositionInterpolator538.DEF = "BubblePath9"
PositionInterpolator538.key = [0,0.0025,0.035,0.65,1]
PositionInterpolator538.keyValue = (0.0000,0.0000,0.0000,0.5220,0.5445,0.0057,0.6543,0.2260,0.0055,0.4557,0.4375,0.0067,1.8787,2.0000,0.1545)

Group528.children.append(PositionInterpolator538)
PositionInterpolator539 = x3d.PositionInterpolator()
PositionInterpolator539.DEF = "BubblePath10"
PositionInterpolator539.key = [0,0.00025,0.035,0.6895,1]
PositionInterpolator539.keyValue = (0.0000,0.0000,0.0000,0.8765,0.4450,0.0034,0.3336,0.4446,0.0056,0.7650,0.7500,0.0075,1.0000,1.0000,0.1000)

Group528.children.append(PositionInterpolator539)
Transform540 = x3d.Transform()
Transform541 = x3d.Transform()
Transform541.DEF = "bubble1"
Shape542 = x3d.Shape()
Appearance543 = x3d.Appearance()
Appearance543.DEF = "BubbleAppearance"
Material544 = x3d.Material()
Material544.diffuseColor = [1,1,1]
Material544.transparency = 0.8

Appearance543.material = Material544

Shape542.appearance = Appearance543
Sphere545 = x3d.Sphere()
Sphere545.radius = 0.025

Shape542.geometry = Sphere545

Transform541.children.append(Shape542)

Transform540.children.append(Transform541)
Transform546 = x3d.Transform()
Transform546.DEF = "bubble2"
Shape547 = x3d.Shape()
Appearance548 = x3d.Appearance()
Appearance548.USE = "BubbleAppearance"

Shape547.appearance = Appearance548
Sphere549 = x3d.Sphere()
Sphere549.radius = 0.055

Shape547.geometry = Sphere549

Transform546.children.append(Shape547)

Transform540.children.append(Transform546)
Transform550 = x3d.Transform()
Transform550.DEF = "bubble3"
Shape551 = x3d.Shape()
Appearance552 = x3d.Appearance()
Appearance552.USE = "BubbleAppearance"

Shape551.appearance = Appearance552
Sphere553 = x3d.Sphere()
Sphere553.radius = 0.065

Shape551.geometry = Sphere553

Transform550.children.append(Shape551)

Transform540.children.append(Transform550)
Transform554 = x3d.Transform()
Transform554.DEF = "bubble4"
Shape555 = x3d.Shape()
Appearance556 = x3d.Appearance()
Appearance556.USE = "BubbleAppearance"

Shape555.appearance = Appearance556
Sphere557 = x3d.Sphere()
Sphere557.radius = 0.015

Shape555.geometry = Sphere557

Transform554.children.append(Shape555)

Transform540.children.append(Transform554)
Transform558 = x3d.Transform()
Transform558.DEF = "bubble5"
Shape559 = x3d.Shape()
Appearance560 = x3d.Appearance()
Appearance560.USE = "BubbleAppearance"

Shape559.appearance = Appearance560
Sphere561 = x3d.Sphere()
Sphere561.radius = 0.075

Shape559.geometry = Sphere561

Transform558.children.append(Shape559)

Transform540.children.append(Transform558)
Transform562 = x3d.Transform()
Transform562.DEF = "bubble6"
Shape563 = x3d.Shape()
Appearance564 = x3d.Appearance()
Appearance564.USE = "BubbleAppearance"

Shape563.appearance = Appearance564
Sphere565 = x3d.Sphere()
Sphere565.radius = 0.005

Shape563.geometry = Sphere565

Transform562.children.append(Shape563)

Transform540.children.append(Transform562)
Transform566 = x3d.Transform()
Transform566.DEF = "bubble7"
Shape567 = x3d.Shape()
Appearance568 = x3d.Appearance()
Appearance568.USE = "BubbleAppearance"

Shape567.appearance = Appearance568
Sphere569 = x3d.Sphere()
Sphere569.radius = 0.035

Shape567.geometry = Sphere569

Transform566.children.append(Shape567)

Transform540.children.append(Transform566)
Transform570 = x3d.Transform()
Transform570.DEF = "bubble8"
Shape571 = x3d.Shape()
Appearance572 = x3d.Appearance()
Appearance572.USE = "BubbleAppearance"

Shape571.appearance = Appearance572
Sphere573 = x3d.Sphere()
Sphere573.radius = 0.05

Shape571.geometry = Sphere573

Transform570.children.append(Shape571)

Transform540.children.append(Transform570)
Transform574 = x3d.Transform()
Transform574.DEF = "bubble9"
Shape575 = x3d.Shape()
Appearance576 = x3d.Appearance()
Appearance576.USE = "BubbleAppearance"

Shape575.appearance = Appearance576
Sphere577 = x3d.Sphere()
Sphere577.radius = 0.045

Shape575.geometry = Sphere577

Transform574.children.append(Shape575)

Transform540.children.append(Transform574)
Transform578 = x3d.Transform()
Transform578.DEF = "bubble10"
Shape579 = x3d.Shape()
Appearance580 = x3d.Appearance()
Appearance580.USE = "BubbleAppearance"

Shape579.appearance = Appearance580
Sphere581 = x3d.Sphere()
Sphere581.radius = 0.035

Shape579.geometry = Sphere581

Transform578.children.append(Shape579)

Transform540.children.append(Transform578)
ROUTE582 = x3d.ROUTE()
ROUTE582.fromField = "fraction_changed"
ROUTE582.fromNode = "BubbleClock"
ROUTE582.toField = "set_fraction"
ROUTE582.toNode = "BubblePath1"

Transform540.children.append(ROUTE582)
ROUTE583 = x3d.ROUTE()
ROUTE583.fromField = "fraction_changed"
ROUTE583.fromNode = "BubbleClock"
ROUTE583.toField = "set_fraction"
ROUTE583.toNode = "BubblePath2"

Transform540.children.append(ROUTE583)
ROUTE584 = x3d.ROUTE()
ROUTE584.fromField = "fraction_changed"
ROUTE584.fromNode = "BubbleClock"
ROUTE584.toField = "set_fraction"
ROUTE584.toNode = "BubblePath3"

Transform540.children.append(ROUTE584)
ROUTE585 = x3d.ROUTE()
ROUTE585.fromField = "fraction_changed"
ROUTE585.fromNode = "BubbleClock"
ROUTE585.toField = "set_fraction"
ROUTE585.toNode = "BubblePath4"

Transform540.children.append(ROUTE585)
ROUTE586 = x3d.ROUTE()
ROUTE586.fromField = "fraction_changed"
ROUTE586.fromNode = "BubbleClock"
ROUTE586.toField = "set_fraction"
ROUTE586.toNode = "BubblePath5"

Transform540.children.append(ROUTE586)
ROUTE587 = x3d.ROUTE()
ROUTE587.fromField = "fraction_changed"
ROUTE587.fromNode = "BubbleClock"
ROUTE587.toField = "set_fraction"
ROUTE587.toNode = "BubblePath6"

Transform540.children.append(ROUTE587)
ROUTE588 = x3d.ROUTE()
ROUTE588.fromField = "fraction_changed"
ROUTE588.fromNode = "BubbleClock"
ROUTE588.toField = "set_fraction"
ROUTE588.toNode = "BubblePath7"

Transform540.children.append(ROUTE588)
ROUTE589 = x3d.ROUTE()
ROUTE589.fromField = "fraction_changed"
ROUTE589.fromNode = "BubbleClock"
ROUTE589.toField = "set_fraction"
ROUTE589.toNode = "BubblePath8"

Transform540.children.append(ROUTE589)
ROUTE590 = x3d.ROUTE()
ROUTE590.fromField = "fraction_changed"
ROUTE590.fromNode = "BubbleClock"
ROUTE590.toField = "set_fraction"
ROUTE590.toNode = "BubblePath9"

Transform540.children.append(ROUTE590)
ROUTE591 = x3d.ROUTE()
ROUTE591.fromField = "fraction_changed"
ROUTE591.fromNode = "BubbleClock"
ROUTE591.toField = "set_fraction"
ROUTE591.toNode = "BubblePath10"

Transform540.children.append(ROUTE591)
ROUTE592 = x3d.ROUTE()
ROUTE592.fromField = "value_changed"
ROUTE592.fromNode = "BubblePath1"
ROUTE592.toField = "set_translation"
ROUTE592.toNode = "bubble1"

Transform540.children.append(ROUTE592)
ROUTE593 = x3d.ROUTE()
ROUTE593.fromField = "value_changed"
ROUTE593.fromNode = "BubblePath2"
ROUTE593.toField = "set_translation"
ROUTE593.toNode = "bubble2"

Transform540.children.append(ROUTE593)
ROUTE594 = x3d.ROUTE()
ROUTE594.fromField = "value_changed"
ROUTE594.fromNode = "BubblePath3"
ROUTE594.toField = "set_translation"
ROUTE594.toNode = "bubble3"

Transform540.children.append(ROUTE594)
ROUTE595 = x3d.ROUTE()
ROUTE595.fromField = "value_changed"
ROUTE595.fromNode = "BubblePath4"
ROUTE595.toField = "set_translation"
ROUTE595.toNode = "bubble4"

Transform540.children.append(ROUTE595)
ROUTE596 = x3d.ROUTE()
ROUTE596.fromField = "value_changed"
ROUTE596.fromNode = "BubblePath5"
ROUTE596.toField = "set_translation"
ROUTE596.toNode = "bubble5"

Transform540.children.append(ROUTE596)
ROUTE597 = x3d.ROUTE()
ROUTE597.fromField = "value_changed"
ROUTE597.fromNode = "BubblePath6"
ROUTE597.toField = "set_translation"
ROUTE597.toNode = "bubble6"

Transform540.children.append(ROUTE597)
ROUTE598 = x3d.ROUTE()
ROUTE598.fromField = "value_changed"
ROUTE598.fromNode = "BubblePath7"
ROUTE598.toField = "set_translation"
ROUTE598.toNode = "bubble7"

Transform540.children.append(ROUTE598)
ROUTE599 = x3d.ROUTE()
ROUTE599.fromField = "value_changed"
ROUTE599.fromNode = "BubblePath8"
ROUTE599.toField = "set_translation"
ROUTE599.toNode = "bubble8"

Transform540.children.append(ROUTE599)
ROUTE600 = x3d.ROUTE()
ROUTE600.fromField = "value_changed"
ROUTE600.fromNode = "BubblePath9"
ROUTE600.toField = "set_translation"
ROUTE600.toNode = "bubble9"

Transform540.children.append(ROUTE600)
ROUTE601 = x3d.ROUTE()
ROUTE601.fromField = "value_changed"
ROUTE601.fromNode = "BubblePath10"
ROUTE601.toField = "set_translation"
ROUTE601.toNode = "bubble10"

Transform540.children.append(ROUTE601)

Group528.children.append(Transform540)

Transform527.children.append(Group528)

fieldValue422.children.append(Transform527)

ProtoInstance420.fieldValue.append(fieldValue422)

fieldValue419.children.append(ProtoInstance420)

ProtoInstance416.fieldValue.append(fieldValue419)

fieldValue407.children.append(ProtoInstance416)

ProtoInstance404.fieldValue.append(fieldValue407)

fieldValue210.children.append(ProtoInstance404)

ProtoInstance207.fieldValue.append(fieldValue210)

fieldValue96.children.append(ProtoInstance207)

ProtoInstance93.fieldValue.append(fieldValue96)

fieldValue92.children.append(ProtoInstance93)

ProtoInstance91.fieldValue.append(fieldValue92)

Transform89.children.append(ProtoInstance91)

Transform88.children.append(Transform89)

Group87.children.append(Transform88)

Group81.children.append(Group87)

LOD80.children.append(Group81)

Scene15.children.append(LOD80)
Script602 = x3d.Script()
Script602.DEF = "finWarpScript"
field603 = x3d.field()
field603.name = "set_rotationL"
field603.accessType = "inputOnly"
field603.type = "SFRotation"

Script602.field.append(field603)
field604 = x3d.field()
field604.name = "set_rotationR"
field604.accessType = "inputOnly"
field604.type = "SFRotation"

Script602.field.append(field604)
field605 = x3d.field()
field605.name = "fin_warpL"
field605.accessType = "outputOnly"
field605.type = "SFBool"

Script602.field.append(field605)
field606 = x3d.field()
field606.name = "fin_warpR"
field606.accessType = "outputOnly"
field606.type = "SFBool"

Script602.field.append(field606)

Script602.sourceCode = '''ecmascript:\n"+
"\n"+
"\n"+
"var positionX;\n"+
"var positionY;\n"+
"var positionZ;\n"+
"var rotation;\n"+
"\n"+
"function initialize()\n"+
"{\n"+
"    	positionX = 0.0;\n"+
"	positionY = 0.0;\n"+
"	positionZ = 0.0;\n"+
"	rotation = 0.0;\n"+
"}\n"+
"\n"+
"function set_rotationL( value, timeStamp)\n"+
"{\n"+
"	rotationFinL = new SFRotation(positionX, positionY, positionZ, rotation);\n"+
"	rotationFinL = value;\n"+
"	//print ('rotationFinL[0] ' + rotationFinL[0]);\n"+
"	if (rotationFinL[0] <= 0)\n"+
"	{\n"+
"		fin_warpL = 0;\n"+
"	}\n"+
"	else\n"+
"	{\n"+
"		fin_warpL = 1;\n"+
"	}\n"+
"	\n"+
"}\n"+
"\n"+
"function set_rotationR( value, timeStamp)\n"+
"{\n"+
"	rotationFinR = new SFRotation(positionX, positionY, positionZ, rotation);\n"+
"	rotationFinR = value;\n"+
"	//print ('rotationFin[0] ' + rotationFinR[0]);\n"+
"	if (rotationFinR[0] <= 0)\n"+
"	{\n"+
"		fin_warpR = 0;\n"+
"	}\n"+
"	else\n"+
"	{\n"+
"		fin_warpR = 1;\n"+
"	}\n"+
"	\n"+
"}'''

Scene15.children.append(Script602)
Group607 = x3d.Group()
Group607.DEF = "Animations"
Group608 = x3d.Group()
Group608.DEF = "Dive_Animation"
OrientationInterpolator609 = x3d.OrientationInterpolator()
OrientationInterpolator609.DEF = "r_ankle_RotationInterpolator_BasicDive"
OrientationInterpolator609.key = [0,0.125,0.2083,0.375,0.4583,0.5,0.6667,0.75,0.7917,0.9167,1]
OrientationInterpolator609.keyValue = (1.0000,0.0000,0.0000,0.8001,1.0000,0.0000,0.0000,0.8509,1.0000,0.0000,0.0000,0.8001,1.0000,0.0000,0.0000,0.8001,1.0000,0.0000,0.0000,0.8509,1.0000,0.0000,0.0000,0.8001,1.0000,0.0000,0.0000,0.8001,1.0000,0.0000,0.0000,0.8001,1.0000,0.0000,0.0000,0.8001,1.0000,0.0000,0.0000,0.8509,1.0000,0.0000,0.0000,0.8600)

Group608.children.append(OrientationInterpolator609)
OrientationInterpolator610 = x3d.OrientationInterpolator()
OrientationInterpolator610.DEF = "r_knee_RotationInterpolator_BasicDive"
OrientationInterpolator610.key = [0,0.125,0.2083,0.375,0.5,0.6667,0.9167,1]
OrientationInterpolator610.keyValue = (1.0000,0.0000,0.0000,0.8573,1.0000,0.0000,0.0000,0.5351,1.0000,0.0000,0.0000,0.1756,1.0000,0.0000,0.0000,0.1194,1.0000,0.0000,0.0000,0.3153,1.0000,0.0000,0.0000,0.0935,1.0000,0.0000,0.0000,0.0856,1.0000,0.0000,0.0000,0.8573)

Group608.children.append(OrientationInterpolator610)
OrientationInterpolator611 = x3d.OrientationInterpolator()
OrientationInterpolator611.DEF = "r_hip_RotationInterpolator_BasicDive"
OrientationInterpolator611.key = [0,0.125,0.2083,0.2917,0.5,0.7917,0.9167,1]
OrientationInterpolator611.keyValue = (-0.5831,0.0351,0.8116,0.1481,-0.9950,0.0230,0.0967,0.4683,-1.0000,0.0019,0.0080,0.4732,-0.9980,-0.0158,-0.0610,0.5079,-0.9131,-0.0624,-0.4030,0.3361,1.0000,0.0000,0.0000,0.2571,0.9891,-0.0280,0.1444,0.3879,-0.5831,0.0351,0.8116,0.1481)

Group608.children.append(OrientationInterpolator611)
OrientationInterpolator612 = x3d.OrientationInterpolator()
OrientationInterpolator612.DEF = "l_ankle_RotationInterpolator_BasicDive"
OrientationInterpolator612.key = [0,0.125,0.2083,0.375,0.4583,0.5,0.6667,0.75,0.7917,0.9167,1]
OrientationInterpolator612.keyValue = (1.0000,0.0000,0.0000,0.6001,1.0000,0.0000,0.0000,0.6509,1.0000,0.0000,0.0000,0.6001,1.0000,0.0000,0.0000,0.6001,1.0000,0.0000,0.0000,0.6509,1.0000,0.0000,0.0000,0.6001,1.0000,0.0000,0.0000,0.6001,1.0000,0.0000,0.0000,0.6509,1.0000,0.0000,0.0000,0.6001,1.0000,0.0000,0.0000,0.6509,1.0000,0.0000,0.0000,0.6001)

Group608.children.append(OrientationInterpolator612)
OrientationInterpolator613 = x3d.OrientationInterpolator()
OrientationInterpolator613.DEF = "l_knee_RotationInterpolator_BasicDive"
OrientationInterpolator613.key = [0,0.2083,0.375,0.5,0.6667,0.7917,0.9167,1]
OrientationInterpolator613.keyValue = (1.0000,0.0000,0.0000,0.3226,1.0000,0.0000,0.0000,0.1556,1.0000,0.0000,0.0000,0.0868,1.0000,0.0000,0.0000,0.8751,1.0000,0.0000,0.0000,1.1310,1.0000,0.0000,0.0000,0.0996,1.0000,0.0000,0.0000,0.3942,1.0000,0.0000,0.0000,0.3226)

Group608.children.append(OrientationInterpolator613)
OrientationInterpolator614 = x3d.OrientationInterpolator()
OrientationInterpolator614.DEF = "l_hip_RotationInterpolator_BasicDive"
OrientationInterpolator614.key = [0,0.25,0.375,0.6667,0.7917,0.9167,1]
OrientationInterpolator614.keyValue = (-0.8730,0.0609,0.4840,0.2865,0.9963,-0.0106,0.0848,0.2488,0.9965,0.0159,-0.0822,0.3836,-1.0000,0.0000,0.0000,0.5518,-0.9964,0.0223,0.0817,0.5351,-0.9809,0.0491,0.1881,0.5204,-0.8730,0.0609,0.4840,0.2865)

Group608.children.append(OrientationInterpolator614)
OrientationInterpolator615 = x3d.OrientationInterpolator()
OrientationInterpolator615.DEF = "lower_body_RotationInterpolator_BasicDive"
OrientationInterpolator615.key = [0,0.5,1]
OrientationInterpolator615.keyValue = (0.0000,0.0000,-1.0000,0.1056,0.0000,0.0000,1.0000,0.0902,0.0000,0.0000,-1.0000,0.1056)

Group608.children.append(OrientationInterpolator615)
#
OrientationInterpolator616 = x3d.OrientationInterpolator()
OrientationInterpolator616.DEF = "r_wrist_RotationInterpolator_BasicDive"
OrientationInterpolator616.key = [0,0.28,0.32,0.64,0.76,1]
OrientationInterpolator616.keyValue = (0.0000,0.0000,1.0000,0.0000,-0.0585,0.9839,-0.1688,1.8596,-0.0585,0.9839,-0.1688,1.8596,-0.0022,0.9980,-0.0630,1.4607,0.0000,1.0000,0.0000,0.4973,0.0000,0.0000,1.0000,0.0000)

Group608.children.append(OrientationInterpolator616)
OrientationInterpolator617 = x3d.OrientationInterpolator()
OrientationInterpolator617.DEF = "r_elbow_RotationInterpolator_BasicDive"
OrientationInterpolator617.key = [0,0.28,0.32,0.64,0.76,1]
OrientationInterpolator617.keyValue = (0.0000,0.0000,1.0000,0.0000,-1.0000,0.0000,0.0000,0.0415,-1.0000,0.0000,0.0000,0.0415,-1.0000,0.0000,0.0000,0.5855,-1.0000,0.0000,0.0000,0.5852,0.0000,0.0000,1.0000,0.0000)

Group608.children.append(OrientationInterpolator617)
OrientationInterpolator618 = x3d.OrientationInterpolator()
OrientationInterpolator618.DEF = "r_shoulder_RotationInterpolator_BasicDive"
OrientationInterpolator618.key = [0,0.45,0.64,0.76,0.88,1]
OrientationInterpolator618.keyValue = (0.0000,0.0000,1.0000,0.0000,0.9992,0.0204,0.0356,7.2000,0.9989,-0.0462,0.0052,4.0790,-0.8687,-0.2525,-0.4261,1.5010,-0.9410,-0.2893,-0.1754,0.4788,0.0000,0.0000,1.0000,0.0000)

Group608.children.append(OrientationInterpolator618)
OrientationInterpolator619 = x3d.OrientationInterpolator()
OrientationInterpolator619.DEF = "l_wrist_RotationInterpolator_BasicDive"
OrientationInterpolator619.key = [0,0.32,0.64,0.88,1]
OrientationInterpolator619.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0670,0.9800,-0.1280,4.1500,0.0670,0.9800,-0.1280,4.1500,0.0670,0.9800,-0.1280,4.1500,0.0000,0.0000,1.0000,0.0000)

Group608.children.append(OrientationInterpolator619)
OrientationInterpolator620 = x3d.OrientationInterpolator()
OrientationInterpolator620.DEF = "l_elbow_RotationInterpolator_BasicDive"
OrientationInterpolator620.key = [0,0.28,0.32,0.64,0.76,1]
OrientationInterpolator620.keyValue = (0.0000,0.0000,1.0000,0.0000,-1.0000,0.0000,0.0000,0.1229,-1.0000,0.0000,0.0000,0.1229,-1.0000,0.0000,0.0000,0.5976,-1.0000,0.0000,0.0000,0.3917,0.0000,0.0000,1.0000,0.0000)

Group608.children.append(OrientationInterpolator620)
OrientationInterpolator621 = x3d.OrientationInterpolator()
OrientationInterpolator621.DEF = "l_shoulder_RotationInterpolator_BasicDive"
OrientationInterpolator621.key = [0,0.25,0.375,0.6667,0.7917,0.9167,1]
OrientationInterpolator621.keyValue = (0.0000,0.0000,1.0000,0.1000,0.0000,0.0000,1.0000,0.2000,0.0000,0.0000,1.0000,0.2000,0.8600,0.2500,0.4200,0.5000,0.8600,0.2500,0.4200,0.8000,0.8600,0.2500,0.4200,0.4000,0.8600,0.2500,0.4200,0.2000)

Group608.children.append(OrientationInterpolator621)
#
OrientationInterpolator622 = x3d.OrientationInterpolator()
OrientationInterpolator622.DEF = "head_RotationInterpolator_BasicDive"
OrientationInterpolator622.key = [0,0.28,0.3,0.32,0.4,0.45,0.6,0.65,0.7,0.75,0.85,0.9,0.95,1]
OrientationInterpolator622.keyValue = (-1.0000,0.0000,0.0000,1.0000,-1.0000,0.0000,0.0000,1.0000,-1.0000,0.0000,0.0000,0.9990,-1.0000,0.0000,0.0000,0.9900,-1.0000,0.0000,0.0000,0.9900,-1.0000,0.0000,0.0000,0.9000,-1.0000,0.0000,0.0000,0.9000,-1.0000,0.0000,0.0000,0.9000,-1.0000,0.0000,0.0000,0.9000,-1.0000,0.0000,0.0000,0.9000,-1.0000,0.0000,0.0000,0.9000,-1.0000,0.0000,0.0000,0.9000,-1.0000,0.0000,0.0000,0.9000,-1.0000,0.0000,0.0000,1.0000)

Group608.children.append(OrientationInterpolator622)
OrientationInterpolator623 = x3d.OrientationInterpolator()
OrientationInterpolator623.DEF = "neck_RotationInterpolator_BasicDive"
OrientationInterpolator623.key = [0,1]
OrientationInterpolator623.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group608.children.append(OrientationInterpolator623)
OrientationInterpolator624 = x3d.OrientationInterpolator()
OrientationInterpolator624.DEF = "upper_body_RotationInterpolator_BasicDive"
OrientationInterpolator624.key = [0,0.2083,0.375,0.75,0.8333,1]
OrientationInterpolator624.keyValue = (0.0000,1.0000,0.0000,0.0826,-0.0197,-0.5974,0.8017,0.0823,0.0093,-0.9648,0.2627,0.1734,-0.0124,0.9549,-0.2968,0.0873,-0.0081,0.9691,-0.2463,0.1580,0.0000,1.0000,0.0000,0.0826)

Group608.children.append(OrientationInterpolator624)
OrientationInterpolator625 = x3d.OrientationInterpolator()
OrientationInterpolator625.DEF = "whole_body_RotationInterpolator_BasicDive"
OrientationInterpolator625.key = [0,1]
OrientationInterpolator625.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group608.children.append(OrientationInterpolator625)
PositionInterpolator626 = x3d.PositionInterpolator()
PositionInterpolator626.DEF = "whole_body_TranslationInterpolator_BasicDive"
PositionInterpolator626.key = [0,0.04167,0.125,0.1667,0.2083,0.25,0.2917,0.375,0.4583,0.5,0.5417,0.5833,0.625,0.7083,0.75,0.7917,0.875,0.9167,1]
PositionInterpolator626.keyValue = (0.0000,-0.0093,0.0000,0.0000,-0.0039,0.0000,0.0000,-0.0088,0.0000,0.0000,-0.0149,0.0000,0.0000,-0.0264,0.0000,0.0000,-0.0393,0.0000,0.0000,-0.0502,0.0000,0.0000,-0.0747,0.0000,0.0000,-0.0273,0.0000,0.0000,-0.0161,0.0000,0.0000,-0.0113,0.0000,0.0000,-0.0058,0.0000,0.0000,-0.0020,0.0000,0.0000,-0.0026,0.0000,0.0000,-0.0143,0.0000,0.0000,-0.0380,0.0000,0.0000,-0.0565,0.0000,0.0000,-0.0450,0.0000,0.0000,-0.0093,0.0000)

Group608.children.append(PositionInterpolator626)
TimeSensor627 = x3d.TimeSensor()
TimeSensor627.DEF = "Dive_Time"
TimeSensor627.cycleInterval = 7
TimeSensor627.loop = True
TimeSensor627.startTime = -1

Group608.children.append(TimeSensor627)
ProximitySensor628 = x3d.ProximitySensor()
ProximitySensor628.DEF = "TriggerProximitySensor"
ProximitySensor628.size = [50,50,50]

Group608.children.append(ProximitySensor628)

Group607.children.append(Group608)

Scene15.children.append(Group607)
ROUTE629 = x3d.ROUTE()
ROUTE629.fromField = "enterTime"
ROUTE629.fromNode = "TriggerProximitySensor"
ROUTE629.toField = "startTime"
ROUTE629.toNode = "Dive_Time"

Scene15.children.append(ROUTE629)
ROUTE630 = x3d.ROUTE()
ROUTE630.fromField = "fraction_changed"
ROUTE630.fromNode = "Dive_Time"
ROUTE630.toField = "set_fraction"
ROUTE630.toNode = "r_ankle_RotationInterpolator_BasicDive"

Scene15.children.append(ROUTE630)
ROUTE631 = x3d.ROUTE()
ROUTE631.fromField = "fraction_changed"
ROUTE631.fromNode = "Dive_Time"
ROUTE631.toField = "set_fraction"
ROUTE631.toNode = "r_knee_RotationInterpolator_BasicDive"

Scene15.children.append(ROUTE631)
ROUTE632 = x3d.ROUTE()
ROUTE632.fromField = "fraction_changed"
ROUTE632.fromNode = "Dive_Time"
ROUTE632.toField = "set_fraction"
ROUTE632.toNode = "r_hip_RotationInterpolator_BasicDive"

Scene15.children.append(ROUTE632)
ROUTE633 = x3d.ROUTE()
ROUTE633.fromField = "fraction_changed"
ROUTE633.fromNode = "Dive_Time"
ROUTE633.toField = "set_fraction"
ROUTE633.toNode = "l_ankle_RotationInterpolator_BasicDive"

Scene15.children.append(ROUTE633)
ROUTE634 = x3d.ROUTE()
ROUTE634.fromField = "fraction_changed"
ROUTE634.fromNode = "Dive_Time"
ROUTE634.toField = "set_fraction"
ROUTE634.toNode = "l_knee_RotationInterpolator_BasicDive"

Scene15.children.append(ROUTE634)
ROUTE635 = x3d.ROUTE()
ROUTE635.fromField = "fraction_changed"
ROUTE635.fromNode = "Dive_Time"
ROUTE635.toField = "set_fraction"
ROUTE635.toNode = "l_hip_RotationInterpolator_BasicDive"

Scene15.children.append(ROUTE635)
ROUTE636 = x3d.ROUTE()
ROUTE636.fromField = "fraction_changed"
ROUTE636.fromNode = "Dive_Time"
ROUTE636.toField = "set_fraction"
ROUTE636.toNode = "lower_body_RotationInterpolator_BasicDive"

Scene15.children.append(ROUTE636)
ROUTE637 = x3d.ROUTE()
ROUTE637.fromField = "fraction_changed"
ROUTE637.fromNode = "Dive_Time"
ROUTE637.toField = "set_fraction"
ROUTE637.toNode = "head_RotationInterpolator_BasicDive"

Scene15.children.append(ROUTE637)
ROUTE638 = x3d.ROUTE()
ROUTE638.fromField = "fraction_changed"
ROUTE638.fromNode = "Dive_Time"
ROUTE638.toField = "set_fraction"
ROUTE638.toNode = "neck_RotationInterpolator_BasicDive"

Scene15.children.append(ROUTE638)
ROUTE639 = x3d.ROUTE()
ROUTE639.fromField = "fraction_changed"
ROUTE639.fromNode = "Dive_Time"
ROUTE639.toField = "set_fraction"
ROUTE639.toNode = "upper_body_RotationInterpolator_BasicDive"

Scene15.children.append(ROUTE639)
ROUTE640 = x3d.ROUTE()
ROUTE640.fromField = "fraction_changed"
ROUTE640.fromNode = "Dive_Time"
ROUTE640.toField = "set_fraction"
ROUTE640.toNode = "whole_body_RotationInterpolator_BasicDive"

Scene15.children.append(ROUTE640)
ROUTE641 = x3d.ROUTE()
ROUTE641.fromField = "fraction_changed"
ROUTE641.fromNode = "Dive_Time"
ROUTE641.toField = "set_fraction"
ROUTE641.toNode = "whole_body_TranslationInterpolator_BasicDive"

Scene15.children.append(ROUTE641)
ROUTE642 = x3d.ROUTE()
ROUTE642.fromField = "value_changed"
ROUTE642.fromNode = "r_ankle_RotationInterpolator_BasicDive"
ROUTE642.toField = "set_rotation"
ROUTE642.toNode = "hanim_r_ankle"

Scene15.children.append(ROUTE642)
ROUTE643 = x3d.ROUTE()
ROUTE643.fromField = "value_changed"
ROUTE643.fromNode = "r_knee_RotationInterpolator_BasicDive"
ROUTE643.toField = "set_rotation"
ROUTE643.toNode = "hanim_r_knee"

Scene15.children.append(ROUTE643)
ROUTE644 = x3d.ROUTE()
ROUTE644.fromField = "value_changed"
ROUTE644.fromNode = "r_hip_RotationInterpolator_BasicDive"
ROUTE644.toField = "set_rotation"
ROUTE644.toNode = "hanim_r_hip"

Scene15.children.append(ROUTE644)
ROUTE645 = x3d.ROUTE()
ROUTE645.fromField = "value_changed"
ROUTE645.fromNode = "l_ankle_RotationInterpolator_BasicDive"
ROUTE645.toField = "set_rotation"
ROUTE645.toNode = "hanim_l_ankle"

Scene15.children.append(ROUTE645)
ROUTE646 = x3d.ROUTE()
ROUTE646.fromField = "value_changed"
ROUTE646.fromNode = "l_knee_RotationInterpolator_BasicDive"
ROUTE646.toField = "set_rotation"
ROUTE646.toNode = "hanim_l_knee"

Scene15.children.append(ROUTE646)
ROUTE647 = x3d.ROUTE()
ROUTE647.fromField = "value_changed"
ROUTE647.fromNode = "l_hip_RotationInterpolator_BasicDive"
ROUTE647.toField = "set_rotationL"
ROUTE647.toNode = "finWarpScript"

Scene15.children.append(ROUTE647)
ROUTE648 = x3d.ROUTE()
ROUTE648.fromField = "value_changed"
ROUTE648.fromNode = "l_hip_RotationInterpolator_BasicDive"
ROUTE648.toField = "set_rotationR"
ROUTE648.toNode = "finWarpScript"

Scene15.children.append(ROUTE648)
ROUTE649 = x3d.ROUTE()
ROUTE649.fromField = "fin_warpL"
ROUTE649.fromNode = "finWarpScript"
ROUTE649.toField = "finL"
ROUTE649.toNode = "FinScript"

Scene15.children.append(ROUTE649)
ROUTE650 = x3d.ROUTE()
ROUTE650.fromField = "fin_warpR"
ROUTE650.fromNode = "finWarpScript"
ROUTE650.toField = "finR"
ROUTE650.toNode = "FinScript"

Scene15.children.append(ROUTE650)
ROUTE651 = x3d.ROUTE()
ROUTE651.fromField = "value_changed"
ROUTE651.fromNode = "l_hip_RotationInterpolator_BasicDive"
ROUTE651.toField = "set_rotation"
ROUTE651.toNode = "hanim_l_hip"

Scene15.children.append(ROUTE651)
ROUTE652 = x3d.ROUTE()
ROUTE652.fromField = "value_changed"
ROUTE652.fromNode = "lower_body_RotationInterpolator_BasicDive"
ROUTE652.toField = "set_rotation"
ROUTE652.toNode = "hanim_sacroiliac"

Scene15.children.append(ROUTE652)
ROUTE653 = x3d.ROUTE()
ROUTE653.fromField = "value_changed"
ROUTE653.fromNode = "head_RotationInterpolator_BasicDive"
ROUTE653.toField = "set_rotation"
ROUTE653.toNode = "hanim_skullbase"

Scene15.children.append(ROUTE653)
ROUTE654 = x3d.ROUTE()
ROUTE654.fromField = "value_changed"
ROUTE654.fromNode = "neck_RotationInterpolator_BasicDive"
ROUTE654.toField = "set_rotation"
ROUTE654.toNode = "hanim_vc4"

Scene15.children.append(ROUTE654)
ROUTE655 = x3d.ROUTE()
ROUTE655.fromField = "value_changed"
ROUTE655.fromNode = "upper_body_RotationInterpolator_BasicDive"
ROUTE655.toField = "set_rotation"
ROUTE655.toNode = "hanim_vl1"

Scene15.children.append(ROUTE655)
ROUTE656 = x3d.ROUTE()
ROUTE656.fromField = "value_changed"
ROUTE656.fromNode = "whole_body_RotationInterpolator_BasicDive"
ROUTE656.toField = "set_rotation"
ROUTE656.toNode = "hanim_humanoid_root"

Scene15.children.append(ROUTE656)
ROUTE657 = x3d.ROUTE()
ROUTE657.fromField = "value_changed"
ROUTE657.fromNode = "whole_body_TranslationInterpolator_BasicDive"
ROUTE657.toField = "set_translation"
ROUTE657.toNode = "hanim_humanoid_root"

Scene15.children.append(ROUTE657)
ROUTE658 = x3d.ROUTE()
ROUTE658.fromField = "fraction_changed"
ROUTE658.fromNode = "Dive_Time"
ROUTE658.toField = "set_fraction"
ROUTE658.toNode = "r_wrist_RotationInterpolator_BasicDive"

Scene15.children.append(ROUTE658)
ROUTE659 = x3d.ROUTE()
ROUTE659.fromField = "fraction_changed"
ROUTE659.fromNode = "Dive_Time"
ROUTE659.toField = "set_fraction"
ROUTE659.toNode = "r_elbow_RotationInterpolator_BasicDive"

Scene15.children.append(ROUTE659)
ROUTE660 = x3d.ROUTE()
ROUTE660.fromField = "fraction_changed"
ROUTE660.fromNode = "Dive_Time"
ROUTE660.toField = "set_fraction"
ROUTE660.toNode = "r_shoulder_RotationInterpolator_BasicDive"

Scene15.children.append(ROUTE660)
ROUTE661 = x3d.ROUTE()
ROUTE661.fromField = "fraction_changed"
ROUTE661.fromNode = "Dive_Time"
ROUTE661.toField = "set_fraction"
ROUTE661.toNode = "l_wrist_RotationInterpolator_BasicDive"

Scene15.children.append(ROUTE661)
ROUTE662 = x3d.ROUTE()
ROUTE662.fromField = "fraction_changed"
ROUTE662.fromNode = "Dive_Time"
ROUTE662.toField = "set_fraction"
ROUTE662.toNode = "l_elbow_RotationInterpolator_BasicDive"

Scene15.children.append(ROUTE662)
ROUTE663 = x3d.ROUTE()
ROUTE663.fromField = "fraction_changed"
ROUTE663.fromNode = "Dive_Time"
ROUTE663.toField = "set_fraction"
ROUTE663.toNode = "l_shoulder_RotationInterpolator_BasicDive"

Scene15.children.append(ROUTE663)
ROUTE664 = x3d.ROUTE()
ROUTE664.fromField = "value_changed"
ROUTE664.fromNode = "r_wrist_RotationInterpolator_BasicDive"
ROUTE664.toField = "set_rotation"
ROUTE664.toNode = "hanim_r_wrist"

Scene15.children.append(ROUTE664)
ROUTE665 = x3d.ROUTE()
ROUTE665.fromField = "value_changed"
ROUTE665.fromNode = "r_elbow_RotationInterpolator_BasicDive"
ROUTE665.toField = "set_rotation"
ROUTE665.toNode = "hanim_r_elbow"

Scene15.children.append(ROUTE665)
ROUTE666 = x3d.ROUTE()
ROUTE666.fromField = "value_changed"
ROUTE666.fromNode = "r_shoulder_RotationInterpolator_BasicDive"
ROUTE666.toField = "set_rotation"
ROUTE666.toNode = "hanim_r_shoulder"

Scene15.children.append(ROUTE666)
ROUTE667 = x3d.ROUTE()
ROUTE667.fromField = "value_changed"
ROUTE667.fromNode = "l_wrist_RotationInterpolator_BasicDive"
ROUTE667.toField = "set_rotation"
ROUTE667.toNode = "hanim_l_wrist"

Scene15.children.append(ROUTE667)
ROUTE668 = x3d.ROUTE()
ROUTE668.fromField = "value_changed"
ROUTE668.fromNode = "l_elbow_RotationInterpolator_BasicDive"
ROUTE668.toField = "set_rotation"
ROUTE668.toNode = "hanim_l_elbow"

Scene15.children.append(ROUTE668)
ROUTE669 = x3d.ROUTE()
ROUTE669.fromField = "value_changed"
ROUTE669.fromNode = "l_shoulder_RotationInterpolator_BasicDive"
ROUTE669.toField = "set_rotation"
ROUTE669.toNode = "hanim_l_shoulder"

Scene15.children.append(ROUTE669)

X3D0.Scene = Scene15
f = open("././NancyDivingProtoInstances_RoundTrip.x3d", "w")
f.write(X3D0.XML())
f.close()
