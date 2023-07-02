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
meta3.content = "NancyDiving.x3d"

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.name = "description"
meta4.content = "Nancy having fun scuba diving!"

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
meta7.content = "17 December 2001"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.name = "modified"
meta8.content = "4 July 2020"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "hint"
meta9.content = "Default orientation along X axis (vice HAnim required Y axis) since diving posture is typically prone."

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "warning"
meta10.content = "problem with left arm animation"

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.name = "warning"
meta11.content = "Viewpoint nodes need to be made child nodes under HAnimHumanoid with containerField='viewpoints'."

head1.children.append(meta11)
meta12 = x3d.meta()
meta12.name = "identifier"
meta12.content = "https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Legacy/NancyDiving.x3d"

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
Background16 = x3d.Background()

Scene15.children.append(Background16)
Viewpoint17 = x3d.Viewpoint()
Viewpoint17.DEF = "DefaultViewpoint"
Viewpoint17.description = "Nancy diving, view from right side"
Viewpoint17.position = [0,0,3]

Scene15.children.append(Viewpoint17)
Group18 = x3d.Group()
Group18.DEF = "HighResolution"
Transform19 = x3d.Transform()
Transform19.rotation = [1,0,0,1.57]
Transform20 = x3d.Transform()
Transform20.rotation = [0,0,1,-1.57]
Group21 = x3d.Group()
Group21.DEF = "Viewpoints"
Viewpoint22 = x3d.Viewpoint()
Viewpoint22.description = "Nancy diving, view from below"
Viewpoint22.position = [0,0,4]

Group21.children.append(Viewpoint22)
Viewpoint23 = x3d.Viewpoint()
Viewpoint23.description = "Nancy diving, view from ahead"
Viewpoint23.orientation = [1,0,0,-1.57]
Viewpoint23.position = [0,3,0]

Group21.children.append(Viewpoint23)
Viewpoint24 = x3d.Viewpoint()
Viewpoint24.description = "Nancy diving, view from left side"
Viewpoint24.orientation = [-0.58,0.58,-0.58,2.09]
Viewpoint24.position = [3,0,0]

Group21.children.append(Viewpoint24)
Transform25 = x3d.Transform()
Transform25.rotation = [1,0,0,1.57]
Transform25.translation = [0,-3,-0.8]
Viewpoint26 = x3d.Viewpoint()
Viewpoint26.description = "Nancy diving view from behind"
Viewpoint26.orientation = [0,0,1,3.14]
Viewpoint26.position = [0,0,0]

Transform25.children.append(Viewpoint26)

Group21.children.append(Transform25)
Viewpoint27 = x3d.Viewpoint()
Viewpoint27.description = "Nancy diving view from above"
Viewpoint27.orientation = [0,1,0,3.14]
Viewpoint27.position = [0,0,-4]

Group21.children.append(Viewpoint27)
Transform28 = x3d.Transform()
Transform28.rotation = [1,0,0,1.57]
Transform28.translation = [0,0.45,-0.04]
Viewpoint29 = x3d.Viewpoint()
Viewpoint29.description = "Nancy diving, view through her goggles"
Viewpoint29.orientation = [0,0,1,3.14]
Viewpoint29.position = [0,0,0]

Transform28.children.append(Viewpoint29)

Group21.children.append(Transform28)

Transform20.children.append(Group21)
Transform30 = x3d.Transform()
Transform30.translation = [0,-1,0]
HAnimHumanoid31 = x3d.HAnimHumanoid()
HAnimHumanoid31.name = "Nancy"
HAnimHumanoid31.DEF = "hanim_Nancy"
HAnimHumanoid31.version = "2.0"
HAnimJoint32 = x3d.HAnimJoint()
HAnimJoint32.name = "humanoid_root"
HAnimJoint32.DEF = "hanim_humanoid_root"
HAnimJoint32.center = [-0.00405,0.855,-0.000113]
HAnimJoint32.ulimit = [0,0,0]
HAnimJoint32.llimit = [0,0,0]
HAnimJoint33 = x3d.HAnimJoint()
HAnimJoint33.name = "sacroiliac"
HAnimJoint33.DEF = "hanim_sacroiliac"
HAnimJoint33.center = [0,1.01,-0.0204]
HAnimJoint33.ulimit = [0,0,0]
HAnimJoint33.llimit = [0,0,0]
HAnimSegment34 = x3d.HAnimSegment()
HAnimSegment34.name = "pelvis"
HAnimSegment34.DEF = "hanim_pelvis"
Shape35 = x3d.Shape()
Appearance36 = x3d.Appearance()
Material37 = x3d.Material()
Material37.DEF = "Pants_Color"
Material37.diffuseColor = [0,0,0.502]

Appearance36.material = Material37

Shape35.appearance = Appearance36
IndexedFaceSet38 = x3d.IndexedFaceSet()
IndexedFaceSet38.coordIndex = [0,1,40,-1,1,2,40,-1,2,3,40,-1,3,4,40,-1,4,5,40,-1,5,4,9,-1,4,3,8,-1,3,2,8,-1,2,1,6,-1,0,7,1,-1,7,6,1,-1,6,8,2,-1,9,4,10,-1,4,8,10,-1,8,6,12,-1,7,0,47,-1,50,5,9,-1,7,47,55,-1,55,13,7,-1,50,9,56,-1,9,10,14,-1,10,11,15,-1,11,12,16,-1,12,13,19,-1,13,55,17,-1,60,17,55,-1,17,19,13,-1,19,16,12,-1,16,15,11,-1,15,18,10,-1,14,56,9,-1,56,14,64,-1,17,60,20,-1,20,19,17,-1,21,64,14,-1,14,22,21,-1,15,16,24,-1,16,19,24,-1,19,20,26,-1,24,23,15,-1,64,21,69,-1,21,22,29,-1,19,26,25,-1,20,63,27,-1,27,26,20,-1,25,24,19,-1,30,29,22,-1,29,28,21,-1,28,69,21,-1,27,34,26,-1,69,28,79,-1,29,30,32,-1,30,23,33,-1,23,24,37,-1,25,26,34,-1,83,27,77,-1,37,33,23,-1,33,32,30,-1,31,79,28,-1,79,31,84,-1,32,33,36,-1,24,25,37,-1,34,27,83,-1,83,38,34,-1,34,37,25,-1,37,36,33,-1,36,35,32,-1,84,31,89,-1,31,35,89,-1,35,36,39,-1,36,37,39,-1,38,83,89,-1,89,39,38,-1,39,89,35,-1,40,41,0,-1,40,42,41,-1,40,43,42,-1,40,44,43,-1,40,45,44,-1,49,44,45,-1,48,43,44,-1,48,42,43,-1,46,41,42,-1,41,47,0,-1,41,46,47,-1,42,48,46,-1,51,44,49,-1,51,48,44,-1,48,52,53,-1,49,45,50,-1,56,49,50,-1,57,51,49,-1,58,53,52,-1,59,54,53,-1,62,55,54,-1,55,62,60,-1,54,59,62,-1,53,58,59,-1,51,61,58,-1,49,56,57,-1,64,57,56,-1,67,59,58,-1,68,62,59,-1,60,63,20,-1,60,62,63,-1,59,67,68,-1,58,61,67,-1,57,64,65,-1,65,66,57,-1,71,63,62,-1,69,65,64,-1,74,66,65,-1,78,68,67,-1,70,71,62,-1,63,72,27,-1,63,71,72,-1,68,78,76,-1,67,75,78,-1,66,74,75,-1,65,73,74,-1,65,69,73,-1,77,27,72,-1,71,82,72,-1,79,73,69,-1,81,75,74,-1,82,71,70,-1,77,72,83,-1,73,79,80,-1,84,80,79,-1,86,75,81,-1,83,72,82,-1,82,88,83,-1,70,87,82,-1,81,85,86,-1,89,80,84,-1,89,85,80,-1,90,86,85,-1,90,87,86,-1,89,83,88,-1,88,90,89,-1,85,89,90,-1,50,45,5,-1,45,40,5,-1,10,8,11,-1,8,12,11,-1,18,22,10,-1,22,14,10,-1,57,66,51,-1,66,61,51,-1,51,58,48,-1,58,52,48,-1,48,53,46,-1,53,54,46,-1,76,70,68,-1,70,62,68,-1,29,32,28,-1,28,32,31,-1,32,35,31,-1,85,81,80,-1,81,73,80,-1,81,74,73,-1,39,37,38,-1,37,34,38,-1,82,87,88,-1,87,90,88,-1,87,78,86,-1,78,75,86,-1,61,66,67,-1,66,75,67,-1,22,18,15,-1,23,30,15,-1,30,22,15,-1,13,12,7,-1,12,6,7,-1,46,54,47,-1,54,55,47,-1,87,76,78,-1,87,70,76,-1]
IndexedFaceSet38.creaseAngle = 1.14
Coordinate39 = x3d.Coordinate()

IndexedFaceSet38.coord = Coordinate39

Shape35.geometry = IndexedFaceSet38

HAnimSegment34.children.append(Shape35)

HAnimJoint33.children.append(HAnimSegment34)
HAnimJoint40 = x3d.HAnimJoint()
HAnimJoint40.name = "l_hip"
HAnimJoint40.DEF = "hanim_l_hip"
HAnimJoint40.center = [0.122,0.888271,-0.0693267]
HAnimJoint40.ulimit = [0,0,0]
HAnimJoint40.llimit = [0,0,0]
HAnimSegment41 = x3d.HAnimSegment()
HAnimSegment41.name = "l_thigh"
HAnimSegment41.DEF = "hanim_l_thigh"
Shape42 = x3d.Shape()
Appearance43 = x3d.Appearance()
Material44 = x3d.Material()
Material44.USE = "Pants_Color"

Appearance43.material = Material44

Shape42.appearance = Appearance43
IndexedFaceSet45 = x3d.IndexedFaceSet()
IndexedFaceSet45.coordIndex = [0,4,5,-1,3,4,0,-1,0,7,1,-1,0,8,7,-1,0,6,8,-1,0,5,6,-1,0,2,3,-1,0,1,2,-1,9,2,1,-1,10,3,2,-1,11,4,3,-1,12,5,4,-1,13,6,5,-1,15,7,8,-1,9,1,7,-1,7,15,9,-1,8,14,15,-1,5,16,13,-1,5,12,16,-1,4,11,12,-1,3,10,11,-1,2,9,10,-1,20,13,16,-1,18,11,10,-1,19,12,11,-1,20,16,12,-1,23,15,14,-1,15,23,24,-1,12,19,20,-1,11,18,19,-1,10,17,18,-1,26,18,17,-1,27,19,18,-1,27,20,19,-1,28,21,20,-1,29,23,22,-1,23,29,30,-1,20,32,28,-1,20,27,32,-1,18,26,27,-1,17,25,26,-1,25,31,30,-1,30,29,26,-1,30,26,25,-1,29,28,27,-1,29,27,26,-1,28,32,27,-1,22,23,14,-1,20,21,13,-1,21,22,13,-1,22,14,13,-1,9,15,24,-1,10,9,17,-1,9,24,17,-1,6,13,8,-1,13,14,8,-1,28,29,21,-1,29,22,21,-1,24,31,17,-1,31,25,17,-1,30,31,23,-1,31,24,23,-1]
IndexedFaceSet45.creaseAngle = 1.32
Coordinate46 = x3d.Coordinate()

IndexedFaceSet45.coord = Coordinate46

Shape42.geometry = IndexedFaceSet45

HAnimSegment41.children.append(Shape42)

HAnimJoint40.children.append(HAnimSegment41)
HAnimJoint47 = x3d.HAnimJoint()
HAnimJoint47.name = "l_knee"
HAnimJoint47.DEF = "hanim_l_knee"
HAnimJoint47.center = [0.0738,0.517,-0.0284]
HAnimJoint47.ulimit = [0,0,0]
HAnimJoint47.llimit = [0,0,0]
HAnimSegment48 = x3d.HAnimSegment()
HAnimSegment48.name = "l_calf"
HAnimSegment48.DEF = "hanim_l_calf"
Shape49 = x3d.Shape()
Appearance50 = x3d.Appearance()
Material51 = x3d.Material()
Material51.USE = "Pants_Color"

Appearance50.material = Material51

Shape49.appearance = Appearance50
IndexedFaceSet52 = x3d.IndexedFaceSet()
IndexedFaceSet52.coordIndex = [2,1,0,-1,2,3,1,-1,2,4,3,-1,2,5,4,-1,2,6,5,-1,2,7,6,-1,2,8,7,-1,2,0,8,-1,9,8,0,-1,10,6,7,-1,11,5,6,-1,12,4,5,-1,12,3,4,-1,13,1,3,-1,1,13,14,-1,3,12,13,-1,5,11,12,-1,6,10,11,-1,8,9,15,-1,22,13,12,-1,13,22,14,-1,17,15,9,-1,20,12,11,-1,21,22,12,-1,23,9,14,-1,9,23,16,-1,14,22,23,-1,12,20,21,-1,15,17,18,-1,9,16,17,-1,24,17,16,-1,25,18,17,-1,26,19,18,-1,27,20,19,-1,28,21,20,-1,29,22,21,-1,30,23,22,-1,31,16,23,-1,23,30,31,-1,22,29,30,-1,21,28,29,-1,20,27,28,-1,19,26,27,-1,18,25,26,-1,17,24,25,-1,16,31,24,-1,33,26,25,-1,36,29,28,-1,37,31,30,-1,29,36,30,-1,25,24,33,-1,31,37,24,-1,32,33,24,-1,24,37,32,-1,38,37,30,-1,30,36,38,-1,41,33,32,-1,42,39,34,-1,44,36,35,-1,45,38,36,-1,46,37,38,-1,38,45,46,-1,36,44,45,-1,35,43,44,-1,39,42,47,-1,32,40,41,-1,40,46,45,-1,41,40,45,-1,41,45,44,-1,44,43,42,-1,44,42,41,-1,43,47,42,-1,39,35,28,-1,35,36,28,-1,34,39,27,-1,39,28,27,-1,33,34,26,-1,34,27,26,-1,33,41,34,-1,41,42,34,-1,40,32,46,-1,32,37,46,-1,10,19,11,-1,19,20,11,-1,14,9,1,-1,9,0,1,-1,8,15,7,-1,7,15,10,-1,15,19,10,-1,15,18,19,-1,43,35,47,-1,35,39,47,-1]
IndexedFaceSet52.creaseAngle = 1.57
Coordinate53 = x3d.Coordinate()

IndexedFaceSet52.coord = Coordinate53

Shape49.geometry = IndexedFaceSet52

HAnimSegment48.children.append(Shape49)

HAnimJoint47.children.append(HAnimSegment48)
HAnimJoint54 = x3d.HAnimJoint()
HAnimJoint54.name = "l_ankle"
HAnimJoint54.DEF = "hanim_l_ankle"
HAnimJoint54.center = [0.0645,0.0719,-0.048]
HAnimJoint54.ulimit = [0,0,0]
HAnimJoint54.llimit = [0,0,0]
HAnimSegment55 = x3d.HAnimSegment()
HAnimSegment55.name = "l_hindfoot"
HAnimSegment55.DEF = "hanim_l_hindfoot"
Shape56 = x3d.Shape()
Appearance57 = x3d.Appearance()
Material58 = x3d.Material()
Material58.DEF = "Shoe_Color"
Material58.ambientIntensity = 0.25
Material58.diffuseColor = [0.753,1,0.243]

Appearance57.material = Material58

Shape56.appearance = Appearance57
IndexedFaceSet59 = x3d.IndexedFaceSet()
IndexedFaceSet59.coordIndex = [2,1,0,-1,4,3,1,-1,2,4,1,-1,3,6,5,-1,1,3,5,-1,6,8,7,-1,5,6,7,-1,8,10,9,-1,7,8,9,-1,10,12,11,-1,9,10,11,-1,12,14,13,-1,11,12,13,-1,14,16,15,-1,13,14,15,-1,16,18,17,-1,15,16,17,-1,18,20,19,-1,17,18,19,-1,20,22,21,-1,19,20,21,-1,22,24,23,-1,21,22,23,-1,24,25,0,-1,23,24,0,-1,25,4,2,-1,0,25,2,-1,18,26,20,-1,16,26,18,-1,27,26,16,-1,14,27,16,-1,12,27,14,-1,28,27,12,-1,29,28,12,-1,10,29,12,-1,8,29,10,-1,6,37,8,-1,24,30,25,-1,31,30,24,-1,22,31,24,-1,32,31,22,-1,20,32,22,-1,33,32,20,-1,26,33,20,-1,34,33,26,-1,27,34,26,-1,35,34,27,-1,28,35,27,-1,29,35,28,-1,36,35,29,-1,8,36,29,-1,37,36,8,-1,6,38,37,-1,3,38,6,-1,39,38,3,-1,30,39,25,-1,41,40,30,-1,31,41,30,-1,42,41,31,-1,32,42,31,-1,43,42,32,-1,33,43,32,-1,44,43,33,-1,34,44,33,-1,45,44,34,-1,35,45,34,-1,46,45,35,-1,36,46,35,-1,47,46,36,-1,37,47,36,-1,38,47,37,-1,48,47,38,-1,49,48,38,-1,39,49,38,-1,40,49,39,-1,30,40,39,-1,48,49,50,-1,47,48,50,-1,46,47,50,-1,45,46,50,-1,44,45,50,-1,43,44,50,-1,42,43,50,-1,41,42,50,-1,40,41,50,-1,49,40,50,-1,11,13,15,-1,11,15,17,-1,9,11,17,-1,9,17,19,-1,7,9,19,-1,7,19,21,-1,5,7,21,-1,5,21,23,-1,5,23,0,-1,1,5,0,-1,3,4,39,-1,4,25,39,-1]
IndexedFaceSet59.creaseAngle = 1.57
Coordinate60 = x3d.Coordinate()

IndexedFaceSet59.coord = Coordinate60

Shape56.geometry = IndexedFaceSet59

HAnimSegment55.children.append(Shape56)
Transform61 = x3d.Transform()
Transform61.scale = [0.015,0.015,0.015]
Transform62 = x3d.Transform()
Transform62.rotation = [0,0,1,1.57]
Transform62.translation = [6,-0.5,-7.5]
Shape63 = x3d.Shape()
Appearance64 = x3d.Appearance()
Material65 = x3d.Material()
Material65.diffuseColor = [0.753,1,0.243]

Appearance64.material = Material65

Shape63.appearance = Appearance64
Extrusion66 = x3d.Extrusion()
Extrusion66.DEF = "FinExtrusionLeft"
Extrusion66.ccw = False
Extrusion66.creaseAngle = 3.14

Shape63.geometry = Extrusion66

Transform62.children.append(Shape63)

Transform61.children.append(Transform62)

HAnimSegment55.children.append(Transform61)

HAnimJoint54.children.append(HAnimSegment55)

HAnimJoint47.children.append(HAnimJoint54)

HAnimJoint40.children.append(HAnimJoint47)

HAnimJoint33.children.append(HAnimJoint40)
HAnimJoint67 = x3d.HAnimJoint()
HAnimJoint67.name = "r_hip"
HAnimJoint67.DEF = "hanim_r_hip"
HAnimJoint67.center = [-0.11,0.892362,-0.0732533]
HAnimJoint67.ulimit = [0,0,0]
HAnimJoint67.llimit = [0,0,0]
HAnimSegment68 = x3d.HAnimSegment()
HAnimSegment68.name = "r_thigh"
HAnimSegment68.DEF = "hanim_r_thigh"
Shape69 = x3d.Shape()
Appearance70 = x3d.Appearance()
Material71 = x3d.Material()
Material71.USE = "Pants_Color"

Appearance70.material = Material71

Shape69.appearance = Appearance70
IndexedFaceSet72 = x3d.IndexedFaceSet()
IndexedFaceSet72.coordIndex = [5,4,0,-1,0,4,3,-1,1,7,0,-1,7,8,0,-1,8,6,0,-1,6,5,0,-1,3,2,0,-1,2,1,0,-1,1,2,9,-1,2,3,10,-1,3,4,11,-1,4,5,12,-1,5,6,13,-1,8,7,15,-1,7,1,9,-1,9,15,7,-1,15,14,8,-1,13,16,5,-1,16,12,5,-1,12,11,4,-1,11,10,3,-1,10,9,2,-1,12,16,20,-1,13,14,22,-1,14,15,23,-1,24,23,15,-1,23,22,14,-1,20,19,12,-1,17,18,26,-1,18,19,27,-1,19,20,27,-1,20,21,28,-1,22,23,29,-1,30,29,23,-1,27,26,18,-1,26,25,17,-1,30,31,25,-1,25,26,29,-1,25,29,30,-1,26,27,28,-1,26,28,29,-1,27,20,28,-1,24,15,9,-1,22,21,13,-1,29,28,22,-1,28,21,22,-1,24,31,23,-1,31,30,23,-1,25,31,17,-1,31,24,17,-1,17,24,10,-1,24,9,10,-1,18,10,11,-1,18,17,10,-1,18,12,19,-1,18,11,12,-1,21,20,13,-1,20,16,13,-1,14,13,8,-1,13,6,8,-1]
IndexedFaceSet72.creaseAngle = 1.61
Coordinate73 = x3d.Coordinate()

IndexedFaceSet72.coord = Coordinate73

Shape69.geometry = IndexedFaceSet72

HAnimSegment68.children.append(Shape69)

HAnimJoint67.children.append(HAnimSegment68)
HAnimJoint74 = x3d.HAnimJoint()
HAnimJoint74.name = "r_knee"
HAnimJoint74.DEF = "hanim_r_knee"
HAnimJoint74.center = [-0.0699,0.51,-0.0166]
HAnimJoint74.ulimit = [0,0,0]
HAnimJoint74.llimit = [0,0,0]
HAnimSegment75 = x3d.HAnimSegment()
HAnimSegment75.name = "r_calf"
HAnimSegment75.DEF = "hanim_r_calf"
Shape76 = x3d.Shape()
Appearance77 = x3d.Appearance()
Material78 = x3d.Material()
Material78.USE = "Pants_Color"

Appearance77.material = Material78

Shape76.appearance = Appearance77
IndexedFaceSet79 = x3d.IndexedFaceSet()
IndexedFaceSet79.coordIndex = [14,25,18,-1,25,32,18,-1,32,27,18,-1,27,22,18,-1,22,10,18,-1,10,6,18,-1,6,8,18,-1,8,14,18,-1,14,8,17,-1,6,10,9,-1,10,22,24,-1,22,27,39,-1,27,32,39,-1,32,25,42,-1,25,14,30,-1,17,30,14,-1,30,42,25,-1,42,39,32,-1,39,24,22,-1,24,9,10,-1,4,17,8,-1,39,42,43,-1,30,43,42,-1,17,4,1,-1,24,39,26,-1,39,43,44,-1,30,17,34,-1,16,34,17,-1,34,43,30,-1,44,26,39,-1,0,1,4,-1,1,16,17,-1,16,1,3,-1,1,0,2,-1,0,5,7,-1,5,26,28,-1,26,44,45,-1,44,43,46,-1,43,34,36,-1,34,16,15,-1,15,36,34,-1,36,46,43,-1,46,45,44,-1,45,28,26,-1,28,7,5,-1,7,2,0,-1,2,3,1,-1,3,15,16,-1,45,46,37,-1,36,15,20,-1,36,37,46,-1,13,2,7,-1,3,20,15,-1,3,2,13,-1,36,20,29,-1,29,37,36,-1,13,21,23,-1,21,33,23,-1,41,37,40,-1,37,29,31,-1,29,20,19,-1,19,31,29,-1,31,40,37,-1,40,38,41,-1,35,23,33,-1,23,12,13,-1,12,11,13,-1,31,19,11,-1,40,31,11,-1,40,11,12,-1,12,23,38,-1,12,38,40,-1,23,35,38,-1,28,21,7,-1,21,13,7,-1,45,33,28,-1,33,21,28,-1,33,45,41,-1,45,37,41,-1,33,41,35,-1,41,38,35,-1,20,3,47,-1,11,19,47,-1,19,20,47,-1,13,47,3,-1,13,11,47,-1,4,8,6,-1,26,5,24,-1,5,9,24,-1,6,9,4,-1,9,0,4,-1,9,5,0,-1]
IndexedFaceSet79.creaseAngle = 1.57
Coordinate80 = x3d.Coordinate()

IndexedFaceSet79.coord = Coordinate80

Shape76.geometry = IndexedFaceSet79

HAnimSegment75.children.append(Shape76)

HAnimJoint74.children.append(HAnimSegment75)
HAnimJoint81 = x3d.HAnimJoint()
HAnimJoint81.name = "r_ankle"
HAnimJoint81.DEF = "hanim_r_ankle"
HAnimJoint81.center = [-0.064,0.0753,-0.0412]
HAnimJoint81.ulimit = [0,0,0]
HAnimJoint81.llimit = [0,0,0]
HAnimSegment82 = x3d.HAnimSegment()
HAnimSegment82.name = "r_hindfoot"
HAnimSegment82.DEF = "hanim_r_hindfoot"
Shape83 = x3d.Shape()
Appearance84 = x3d.Appearance()
Material85 = x3d.Material()
Material85.USE = "Shoe_Color"

Appearance84.material = Material85

Shape83.appearance = Appearance84
IndexedFaceSet86 = x3d.IndexedFaceSet()
IndexedFaceSet86.coordIndex = [6,50,0,-1,50,8,7,-1,50,7,0,-1,1,9,8,-1,1,8,50,-1,49,10,9,-1,49,9,1,-1,46,11,10,-1,46,10,49,-1,2,12,11,-1,2,11,46,-1,3,13,12,-1,3,12,2,-1,4,14,13,-1,4,13,3,-1,45,14,4,-1,47,15,45,-1,19,15,47,-1,48,18,19,-1,5,16,18,-1,5,18,48,-1,6,17,16,-1,6,16,5,-1,0,7,17,-1,0,17,6,-1,14,20,21,-1,14,21,13,-1,13,21,12,-1,12,21,22,-1,12,22,11,-1,11,22,10,-1,17,23,16,-1,16,23,24,-1,16,24,18,-1,18,24,25,-1,18,25,19,-1,19,25,26,-1,19,26,15,-1,15,26,20,-1,20,26,27,-1,20,27,21,-1,21,27,28,-1,21,28,22,-1,22,28,29,-1,10,30,9,-1,9,30,31,-1,9,31,8,-1,8,31,32,-1,17,32,23,-1,23,33,34,-1,23,34,35,-1,23,35,24,-1,24,35,36,-1,24,36,25,-1,25,36,37,-1,25,37,26,-1,26,37,38,-1,26,38,27,-1,27,38,39,-1,27,39,28,-1,28,39,40,-1,28,40,29,-1,29,40,41,-1,29,41,30,-1,30,41,42,-1,30,42,31,-1,31,42,43,-1,31,43,32,-1,32,43,33,-1,32,33,23,-1,44,43,42,-1,44,42,41,-1,44,41,40,-1,44,40,39,-1,44,39,38,-1,44,38,37,-1,44,37,36,-1,44,36,35,-1,44,35,34,-1,44,34,33,-1,44,33,43,-1,4,3,2,-1,45,4,2,-1,45,2,46,-1,47,45,46,-1,48,46,49,-1,5,48,49,-1,5,49,1,-1,6,5,1,-1,6,1,50,-1,30,10,29,-1,10,22,29,-1,17,7,32,-1,7,8,32,-1,19,47,48,-1,47,46,48,-1,20,14,15,-1,14,45,15,-1]
IndexedFaceSet86.creaseAngle = 1.57
Coordinate87 = x3d.Coordinate()

IndexedFaceSet86.coord = Coordinate87

Shape83.geometry = IndexedFaceSet86

HAnimSegment82.children.append(Shape83)
Transform88 = x3d.Transform()
Transform88.scale = [0.015,0.015,0.015]
Transform89 = x3d.Transform()
Transform89.rotation = [0,0,1,1.57]
Transform89.translation = [-5,-0.5,-7.5]
Shape90 = x3d.Shape()
Appearance91 = x3d.Appearance()
Material92 = x3d.Material()
Material92.diffuseColor = [0.753,1,0.243]

Appearance91.material = Material92

Shape90.appearance = Appearance91
Extrusion93 = x3d.Extrusion()
Extrusion93.DEF = "FinExtrusionRight"
Extrusion93.ccw = False
Extrusion93.creaseAngle = 3.14

Shape90.geometry = Extrusion93

Transform89.children.append(Shape90)

Transform88.children.append(Transform89)

HAnimSegment82.children.append(Transform88)

HAnimJoint81.children.append(HAnimSegment82)

HAnimJoint74.children.append(HAnimJoint81)

HAnimJoint67.children.append(HAnimJoint74)

HAnimJoint33.children.append(HAnimJoint67)

HAnimJoint32.children.append(HAnimJoint33)
HAnimJoint94 = x3d.HAnimJoint()
HAnimJoint94.name = "vl1"
HAnimJoint94.DEF = "hanim_vl1"
HAnimJoint94.center = [-0.00405,1.07,-0.0275]
HAnimJoint94.ulimit = [0,0,0]
HAnimJoint94.llimit = [0,0,0]
HAnimSegment95 = x3d.HAnimSegment()
HAnimSegment95.name = "l1"
HAnimSegment95.DEF = "hanim_l1"
Transform96 = x3d.Transform()
Transform96.scale = [1.05,1.05,1.05]
Transform96.translation = [-0.00405,1.07,-0.0275]
Shape97 = x3d.Shape()
Appearance98 = x3d.Appearance()
Material99 = x3d.Material()
Material99.DEF = "WetShirtColor"
Material99.ambientIntensity = 0.25
Material99.diffuseColor = [0,0,0.502]

Appearance98.material = Material99
ImageTexture100 = x3d.ImageTexture()
ImageTexture100.DEF = "small_logo_Tex"
ImageTexture100.url = ["small_logo.gif","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Legacy/small_logo.gif"]

Appearance98.texture = ImageTexture100

Shape97.appearance = Appearance98
IndexedFaceSet101 = x3d.IndexedFaceSet()
IndexedFaceSet101.coordIndex = [0,1,2,-1,3,0,2,-1,4,5,6,-1,6,7,4,-1,8,7,6,-1,6,9,8,-1,9,10,8,-1,6,5,11,-1,9,6,12,-1,11,12,6,-1,12,10,9,-1,7,8,13,-1,13,4,7,-1,14,15,16,-1,15,17,13,-1,4,13,17,-1,17,15,18,-1,13,19,15,-1,19,13,8,-1,19,16,15,-1,16,19,8,-1,17,20,4,-1,5,4,20,-1,18,21,17,-1,20,17,21,-1,16,22,14,-1,22,16,23,-1,8,23,16,-1,23,8,10,-1,24,25,26,-1,26,27,24,-1,25,28,26,-1,28,29,30,-1,30,26,28,-1,31,32,33,-1,32,25,33,-1,25,24,34,-1,33,25,34,-1,24,35,34,-1,27,35,24,-1,33,36,31,-1,27,26,37,-1,37,26,30,-1,38,37,30,-1,33,34,39,-1,39,34,35,-1,39,35,40,-1,41,38,30,-1,35,27,42,-1,37,42,27,-1,40,35,42,-1,42,37,43,-1,37,38,44,-1,44,43,37,-1,36,45,46,-1,36,33,45,-1,40,42,47,-1,43,47,42,-1,47,48,40,-1,39,40,48,-1,47,43,49,-1,43,44,49,-1,50,49,44,-1,51,46,52,-1,46,45,52,-1,52,45,53,-1,33,53,45,-1,33,39,53,-1,49,54,47,-1,48,47,54,-1,55,56,52,-1,57,52,53,-1,57,55,52,-1,58,57,53,-1,59,58,53,-1,53,39,59,-1,39,48,59,-1,59,48,54,-1,58,59,60,-1,54,49,61,-1,59,54,61,-1,60,59,61,-1,49,50,62,-1,63,62,50,-1,62,61,49,-1,64,63,50,-1,63,64,65,-1,65,62,63,-1,66,60,61,-1,62,65,67,-1,68,67,65,-1,64,69,70,-1,64,70,65,-1,70,68,65,-1,69,71,72,-1,72,70,69,-1,73,74,75,-1,66,76,60,-1,67,77,62,-1,62,77,61,-1,77,66,61,-1,66,77,78,-1,77,67,79,-1,79,67,68,-1,79,78,77,-1,68,70,80,-1,70,72,80,-1,80,79,68,-1,74,73,81,-1,73,76,82,-1,82,81,73,-1,76,66,83,-1,78,83,66,-1,83,82,76,-1,78,79,84,-1,79,80,84,-1,84,85,78,-1,86,84,80,-1,81,82,87,-1,87,88,81,-1,82,83,89,-1,83,78,89,-1,89,87,82,-1,78,85,89,-1,90,91,92,-1,92,93,90,-1,90,94,91,-1,95,96,94,-1,94,90,95,-1,29,96,97,-1,96,95,97,-1,97,30,29,-1,30,97,41,-1,41,97,95,-1,98,99,100,-1,98,91,99,-1,101,92,91,-1,98,101,91,-1,101,102,92,-1,92,102,93,-1,36,103,31,-1,51,103,36,46,-1,103,100,31,-1,100,103,98,-1,104,90,93,-1,90,104,95,-1,95,105,41,-1,104,105,95,-1,106,101,98,-1,102,101,106,-1,107,93,102,-1,93,107,104,-1,108,104,107,-1,107,109,108,-1,110,105,104,-1,104,108,110,-1,109,107,111,-1,107,102,111,-1,111,102,106,-1,111,112,109,-1,106,112,111,-1,113,110,108,-1,110,113,114,-1,51,52,115,-1,116,115,117,-1,117,106,116,-1,118,109,112,-1,119,108,109,-1,108,119,113,-1,109,118,119,-1,120,113,119,-1,119,121,120,-1,52,56,122,-1,122,115,52,-1,115,122,123,-1,117,124,125,-1,106,117,125,-1,118,112,106,125,-1,119,118,125,-1,121,119,125,-1,126,124,123,-1,127,114,113,-1,114,127,128,-1,113,120,127,-1,114,128,129,-1,130,126,123,-1,122,130,123,-1,131,120,121,-1,131,127,120,-1,132,129,128,-1,128,127,132,-1,74,81,133,-1,81,134,133,-1,121,135,131,-1,136,132,127,-1,132,136,137,-1,138,71,129,-1,138,129,132,-1,137,138,132,-1,139,72,71,-1,72,139,80,-1,71,138,139,-1,140,135,121,-1,140,121,125,-1,141,127,131,-1,127,141,136,-1,131,135,141,-1,142,141,135,-1,143,136,141,-1,136,143,137,-1,141,142,143,-1,144,138,137,-1,144,139,138,-1,143,144,137,-1,145,146,134,-1,145,140,146,-1,134,81,145,-1,147,135,140,-1,135,147,142,-1,140,145,147,-1,148,80,139,-1,80,148,86,-1,139,144,148,-1,149,143,142,-1,149,144,143,-1,142,150,149,-1,151,148,144,-1,144,149,151,-1,152,145,81,-1,81,88,152,-1,153,147,145,-1,153,142,147,-1,145,152,153,-1,153,150,142,-1,154,86,148,-1,148,151,154,-1,155,28,25,-1,155,29,28,-1,155,25,32,-1,155,32,31,-1,155,31,100,-1,155,100,99,-1,155,99,91,-1,155,91,94,-1,155,94,96,-1,155,96,29,-1,156,151,149,-1,156,154,151,-1,156,149,150,-1,156,150,153,-1,156,153,152,-1,156,152,88,-1,156,88,87,-1,156,87,89,-1,156,89,85,-1,156,85,84,-1,156,84,86,-1,156,86,154,-1,76,157,60,-1,76,73,158,157,-1,159,158,73,75,160,-1,161,56,55,-1,60,162,58,-1,162,60,157,-1,161,55,163,-1,57,164,163,55,-1,160,163,164,-1,160,164,159,-1,164,57,165,-1,164,165,159,-1,57,58,166,165,-1,166,58,162,-1,165,166,159,-1,166,162,157,158,159,-1,140,125,167,-1,124,168,125,-1,168,167,125,-1,124,169,168,-1,146,140,167,170,-1,168,170,167,-1,168,169,170,-1,146,170,171,-1,169,171,170,-1,172,134,146,171,-1,134,172,130,-1,169,124,126,173,-1,173,126,130,-1,169,173,172,171,-1,173,130,172,-1,122,74,133,174,-1,133,134,174,-1,130,122,174,-1,134,130,174,-1,122,56,175,74,-1,74,175,176,-1,175,56,161,176,-1,74,176,75,-1,176,161,163,-1,176,160,75,-1,176,163,160,-1,115,116,177,51,-1,106,98,177,116,-1,51,177,103,-1,177,98,103,-1]
IndexedFaceSet101.creaseAngle = 1.59
Coordinate102 = x3d.Coordinate()
Coordinate102.DEF = "pointValues"

IndexedFaceSet101.coord = Coordinate102
TextureCoordinate103 = x3d.TextureCoordinate()

IndexedFaceSet101.texCoord = TextureCoordinate103

Shape97.geometry = IndexedFaceSet101

Transform96.children.append(Shape97)

HAnimSegment95.children.append(Transform96)
Transform104 = x3d.Transform()
Transform104.scale = [1.25,1.1,1.3]
Transform104.translation = [-0.00405,1.07,-0.0275]
Group105 = x3d.Group()
Transform106 = x3d.Transform()
Transform106.translation = [0,-1.2,0]
Shape107 = x3d.Shape()
Appearance108 = x3d.Appearance()
Material109 = x3d.Material()
Material109.DEF = "BCLColor"
Material109.ambientIntensity = 0.25
Material109.diffuseColor = [0.0588,0.0588,0.0588]
Material109.shininess = 0.5

Appearance108.material = Material109

Shape107.appearance = Appearance108
IndexedFaceSet110 = x3d.IndexedFaceSet()
IndexedFaceSet110.coordIndex = [4,5,6,-1,6,7,4,-1,8,7,6,-1,6,9,8,-1,9,10,8,-1,6,5,11,-1,9,6,12,-1,11,12,6,-1,12,10,9,-1,7,8,13,-1,13,4,7,-1,14,15,16,-1,15,17,13,-1,4,13,17,-1,17,15,18,-1,13,19,15,-1,19,13,8,-1,19,16,15,-1,16,19,8,-1,17,20,4,-1,5,4,20,-1,18,21,17,-1,20,17,21,-1,16,22,14,-1,22,16,23,-1,8,23,16,-1,23,8,10,-1,24,25,26,-1,26,27,24,-1,25,28,26,-1,28,29,30,-1,30,26,28,-1,25,24,34,-1,33,25,34,-1,24,35,34,-1,27,35,24,-1,27,26,37,-1,37,26,30,-1,38,37,30,-1,33,34,39,-1,39,34,35,-1,41,38,30,-1,35,27,42,-1,37,42,27,-1,42,37,43,-1,37,38,44,-1,44,43,37,-1,43,47,42,-1,47,43,49,-1,43,44,49,-1,50,49,44,-1,33,39,53,-1,49,54,47,-1,59,58,53,-1,53,39,59,-1,58,59,60,-1,54,49,61,-1,49,50,62,-1,63,62,50,-1,62,61,49,-1,64,63,50,-1,63,64,65,-1,65,62,63,-1,66,60,61,-1,62,65,67,-1,68,67,65,-1,64,69,70,-1,64,70,65,-1,70,68,65,-1,69,71,72,-1,72,70,69,-1,66,76,60,-1,67,77,62,-1,62,77,61,-1,77,66,61,-1,66,77,78,-1,77,67,79,-1,79,67,68,-1,79,78,77,-1,68,70,80,-1,70,72,80,-1,80,79,68,-1,73,76,82,-1,76,66,83,-1,78,83,66,-1,83,82,76,-1,78,79,84,-1,79,80,84,-1,84,85,78,-1,86,84,80,-1,82,83,89,-1,83,78,89,-1,89,87,82,-1,78,85,89,-1,90,91,92,-1,92,93,90,-1,90,94,91,-1,95,96,94,-1,94,90,95,-1,29,96,97,-1,96,95,97,-1,97,30,29,-1,30,97,41,-1,41,97,95,-1,101,92,91,-1,98,101,91,-1,101,102,92,-1,92,102,93,-1,104,90,93,-1,90,104,95,-1,95,105,41,-1,104,105,95,-1,106,101,98,-1,102,101,106,-1,107,93,102,-1,93,107,104,-1,108,104,107,-1,107,109,108,-1,110,105,104,-1,104,108,110,-1,113,110,108,-1,110,113,114,-1,119,108,109,-1,108,119,113,-1,120,113,119,-1,119,121,120,-1,117,124,125,-1,106,117,125,-1,127,114,113,-1,114,127,128,-1,113,120,127,-1,114,128,129,-1,131,120,121,-1,131,127,120,-1,132,129,128,-1,128,127,132,-1,121,135,131,-1,136,132,127,-1,132,136,137,-1,138,71,129,-1,138,129,132,-1,137,138,132,-1,139,72,71,-1,72,139,80,-1,71,138,139,-1,140,135,121,-1,140,121,125,-1,141,127,131,-1,127,141,136,-1,131,135,141,-1,142,141,135,-1,143,136,141,-1,136,143,137,-1,141,142,143,-1,144,138,137,-1,144,139,138,-1,143,144,137,-1,145,140,146,-1,147,135,140,-1,135,147,142,-1,140,145,147,-1,148,80,139,-1,80,148,86,-1,139,144,148,-1,149,143,142,-1,149,144,143,-1,142,150,149,-1,151,148,144,-1,144,149,151,-1,153,147,145,-1,153,142,147,-1,145,152,153,-1,153,150,142,-1,154,86,148,-1,148,151,154,-1,76,157,60,-1,76,73,158,157,-1,60,162,58,-1,162,60,157,-1,166,58,162,-1,165,166,159,-1,166,162,157,158,159,-1,140,125,167,-1,124,168,125,-1,168,167,125,-1,124,169,168,-1,146,140,167,170,-1,168,170,167,-1,168,169,170,-1,146,170,171,-1,169,171,170,-1,98,117,106,-1]
IndexedFaceSet110.creaseAngle = 1.59
IndexedFaceSet110.solid = False
Coordinate111 = x3d.Coordinate()
Coordinate111.USE = "pointValues"

IndexedFaceSet110.coord = Coordinate111
TextureCoordinate112 = x3d.TextureCoordinate()

IndexedFaceSet110.texCoord = TextureCoordinate112

Shape107.geometry = IndexedFaceSet110

Transform106.children.append(Shape107)

Group105.children.append(Transform106)
Transform113 = x3d.Transform()
Transform113.rotation = [0,0,1,1.57]
Transform113.scale = [2,1.5,1.5]
Transform113.translation = [0.13,0.22,-0.1]
Transform114 = x3d.Transform()
Transform114.rotation = [1,0,0,1.4]
Shape115 = x3d.Shape()
Shape115.DEF = "BCLSnorkelPad"
Appearance116 = x3d.Appearance()
Material117 = x3d.Material()
Material117.USE = "BCLColor"

Appearance116.material = Material117

Shape115.appearance = Appearance116
Extrusion118 = x3d.Extrusion()

Shape115.geometry = Extrusion118

Transform114.children.append(Shape115)

Transform113.children.append(Transform114)

Group105.children.append(Transform113)
Transform119 = x3d.Transform()
Transform119.rotation = [-1,0,0,0.8]
Transform119.translation = [0.07,0.08,0.125]
Shape120 = x3d.Shape()
Appearance121 = x3d.Appearance()
Material122 = x3d.Material()
Material122.DEF = "BCLSnorkel"
Material122.diffuseColor = [0.25,0.25,0.25]
Material122.shininess = 0.5
Material122.transparency = 0.1

Appearance121.material = Material122

Shape120.appearance = Appearance121
Extrusion123 = x3d.Extrusion()

Shape120.geometry = Extrusion123

Transform119.children.append(Shape120)

Group105.children.append(Transform119)
Group124 = x3d.Group()
Group124.DEF = "buckle"
Transform125 = x3d.Transform()
Transform125.rotation = [-1,0,0,0.68]
Transform125.translation = [-0.08,0.1,0.029]
Shape126 = x3d.Shape()
Appearance127 = x3d.Appearance()
Appearance127.DEF = "buckleHolder"
Material128 = x3d.Material()
Material128.diffuseColor = [0.25,0.25,0.25]

Appearance127.material = Material128

Shape126.appearance = Appearance127
Box129 = x3d.Box()
Box129.size = [0.03,0.03,0.005]

Shape126.geometry = Box129

Transform125.children.append(Shape126)

Group124.children.append(Transform125)
Transform130 = x3d.Transform()
Transform130.rotation = [-1,0,0,0.68]
Transform130.translation = [0.03,0.1,0.027]
Shape131 = x3d.Shape()
Appearance132 = x3d.Appearance()
Appearance132.USE = "buckleHolder"

Shape131.appearance = Appearance132
Box133 = x3d.Box()
Box133.size = [0.15,0.03,0.001]

Shape131.geometry = Box133

Transform130.children.append(Shape131)

Group124.children.append(Transform130)
Transform134 = x3d.Transform()
Transform134.rotation = [-1,0,0,0.68]
Transform134.translation = [-0.045,0.1,0.028]
Shape135 = x3d.Shape()
Appearance136 = x3d.Appearance()
Appearance136.DEF = "pin"
Material137 = x3d.Material()

Appearance136.material = Material137

Shape135.appearance = Appearance136
Box138 = x3d.Box()
Box138.size = [0.02,0.028,0.005]

Shape135.geometry = Box138

Transform134.children.append(Shape135)

Group124.children.append(Transform134)
Transform139 = x3d.Transform()
Transform139.rotation = [0,0,1,1.57]
Transform139.translation = [-0.06,0.1,0.029]
Shape140 = x3d.Shape()
Appearance141 = x3d.Appearance()
Appearance141.USE = "pin"

Shape140.appearance = Appearance141
Cylinder142 = x3d.Cylinder()
Cylinder142.height = 0.02
Cylinder142.radius = 0.0024

Shape140.geometry = Cylinder142

Transform139.children.append(Shape140)

Group124.children.append(Transform139)
Transform143 = x3d.Transform()
Transform143.rotation = [0,0,1,1.57]
Transform143.translation = [-0.06,0.109,0.0217]
Shape144 = x3d.Shape()
Appearance145 = x3d.Appearance()
Appearance145.USE = "pin"

Shape144.appearance = Appearance145
Cylinder146 = x3d.Cylinder()
Cylinder146.height = 0.02
Cylinder146.radius = 0.0024

Shape144.geometry = Cylinder146

Transform143.children.append(Shape144)

Group124.children.append(Transform143)
Transform147 = x3d.Transform()
Transform147.rotation = [0,0,1,1.57]
Transform147.translation = [-0.06,0.091,0.036]
Shape148 = x3d.Shape()
Appearance149 = x3d.Appearance()
Appearance149.USE = "pin"

Shape148.appearance = Appearance149
Cylinder150 = x3d.Cylinder()
Cylinder150.height = 0.02
Cylinder150.radius = 0.0024

Shape148.geometry = Cylinder150

Transform147.children.append(Shape148)

Group124.children.append(Transform147)

Group105.children.append(Group124)
Group151 = x3d.Group()
Group151.DEF = "buckleBelt"
Transform152 = x3d.Transform()
Transform152.rotation = [0,1,0,-0.68]
Transform152.translation = [-0.07,-0.12,0.038]
Shape153 = x3d.Shape()
Appearance154 = x3d.Appearance()
Appearance154.USE = "buckleHolder"

Shape153.appearance = Appearance154
Box155 = x3d.Box()
Box155.size = [0.04,0.1,0.005]

Shape153.geometry = Box155

Transform152.children.append(Shape153)

Group151.children.append(Transform152)
Transform156 = x3d.Transform()
Transform156.translation = [0.005,-0.12,0.053]
Shape157 = x3d.Shape()
Appearance158 = x3d.Appearance()
Appearance158.USE = "buckleHolder"

Shape157.appearance = Appearance158
Box159 = x3d.Box()
Box159.size = [0.12,0.11,0.001]

Shape157.geometry = Box159

Transform156.children.append(Shape157)

Group151.children.append(Transform156)
Transform160 = x3d.Transform()
Transform160.rotation = [0,1,0,0.68]
Transform160.translation = [0.075,-0.12,0.038]
Shape161 = x3d.Shape()
Appearance162 = x3d.Appearance()
Appearance162.USE = "buckleHolder"

Shape161.appearance = Appearance162
Box163 = x3d.Box()
Box163.size = [0.04,0.1,0.005]

Shape161.geometry = Box163

Transform160.children.append(Shape161)

Group151.children.append(Transform160)

Group105.children.append(Group151)

Transform104.children.append(Group105)

HAnimSegment95.children.append(Transform104)
Transform164 = x3d.Transform()
Transform164.DEF = "ScubaTank"
Transform164.rotation = [0,1,0,3.14]
Transform164.scale = [0.8,0.8,0.8]
Transform164.translation = [-0.00405,1.07,-0.0275]
Inline165 = x3d.Inline()
Inline165.url = ["ScubaTank.x3d","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Legacy/ScubaTank.x3d","ScubaTank.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Legacy/ScubaTank.wrl"]

Transform164.children.append(Inline165)

HAnimSegment95.children.append(Transform164)

HAnimJoint94.children.append(HAnimSegment95)
HAnimJoint166 = x3d.HAnimJoint()
HAnimJoint166.name = "l_shoulder"
HAnimJoint166.DEF = "hanim_l_shoulder"
HAnimJoint166.center = [0.167,1.36,-0.0518]
HAnimJoint166.ulimit = [0,0,0]
HAnimJoint166.llimit = [0,0,0]
HAnimSegment167 = x3d.HAnimSegment()
HAnimSegment167.name = "l_upperarm"
HAnimSegment167.DEF = "hanim_l_upperarm"
Transform168 = x3d.Transform()
Transform168.DEF = "l_upperarm_adjust"
Transform168.center = [0.182,1.22,-0.047]
Transform168.rotation = [1,0,0,0.119]
Transform168.translation = [0.167,1.36,-0.0518]
Shape169 = x3d.Shape()
Appearance170 = x3d.Appearance()
Material171 = x3d.Material()
Material171.USE = "WetShirtColor"

Appearance170.material = Material171

Shape169.appearance = Appearance170
IndexedFaceSet172 = x3d.IndexedFaceSet()
IndexedFaceSet172.coordIndex = [2,1,0,-1,2,3,1,-1,2,4,3,-1,2,0,5,-1,6,5,0,-1,7,2,5,-1,8,4,2,-1,8,3,4,-1,9,1,3,-1,10,0,1,-1,0,10,6,-1,1,9,10,-1,3,8,9,-1,2,7,8,-1,5,6,7,-1,11,7,6,-1,14,9,8,-1,15,10,9,-1,11,6,10,-1,10,15,11,-1,9,14,15,-1,8,13,14,-1,8,16,13,-1,7,11,12,-1,21,15,14,-1,15,17,11,-1,15,21,17,-1,16,19,13,-1,13,19,20,-1,21,14,20,-1,14,13,20,-1,12,17,18,-1,12,11,17,-1,12,18,16,-1,18,19,16,-1,12,16,7,-1,16,8,7,-1,19,18,17,-1,20,19,21,-1,19,17,21,-1]
IndexedFaceSet172.creaseAngle = 1.65
Coordinate173 = x3d.Coordinate()

IndexedFaceSet172.coord = Coordinate173

Shape169.geometry = IndexedFaceSet172

Transform168.children.append(Shape169)

HAnimSegment167.children.append(Transform168)

HAnimJoint166.children.append(HAnimSegment167)
HAnimJoint174 = x3d.HAnimJoint()
HAnimJoint174.name = "l_elbow"
HAnimJoint174.DEF = "hanim_l_elbow"
HAnimJoint174.center = [0.196,1.07,-0.0518]
HAnimJoint174.ulimit = [0,0,0]
HAnimJoint174.llimit = [0,0,0]
HAnimSegment175 = x3d.HAnimSegment()
HAnimSegment175.name = "l_forearm"
HAnimSegment175.DEF = "hanim_l_forearm"
Transform176 = x3d.Transform()
Transform176.DEF = "l_forearm_adjust"
Transform176.center = [0.198,0.961,-0.0405]
Transform176.rotation = [-1,0,0,0.1]
Transform176.translation = [0.196,1.07,-0.0518]
Shape177 = x3d.Shape()
Appearance178 = x3d.Appearance()
Material179 = x3d.Material()
Material179.USE = "WetShirtColor"

Appearance178.material = Material179

Shape177.appearance = Appearance178
IndexedFaceSet180 = x3d.IndexedFaceSet()
IndexedFaceSet180.coordIndex = [2,1,0,-1,2,3,1,-1,2,4,3,-1,2,5,4,-1,2,6,5,-1,2,0,6,-1,7,6,0,-1,8,5,6,-1,9,4,5,-1,9,3,4,-1,10,1,3,-1,11,0,1,-1,0,11,7,-1,1,10,11,-1,3,9,10,-1,5,12,9,-1,5,8,12,-1,6,7,8,-1,17,16,15,-1,14,17,15,-1,14,18,17,-1,13,18,14,-1,16,17,10,-1,16,10,9,-1,15,16,9,-1,15,9,12,-1,18,13,7,-1,18,7,11,-1,13,14,8,-1,13,8,7,-1,14,15,8,-1,15,12,8,-1,17,18,10,-1,18,11,10,-1]
IndexedFaceSet180.creaseAngle = 1.75
Coordinate181 = x3d.Coordinate()

IndexedFaceSet180.coord = Coordinate181

Shape177.geometry = IndexedFaceSet180

Transform176.children.append(Shape177)

HAnimSegment175.children.append(Transform176)

HAnimJoint174.children.append(HAnimSegment175)
HAnimJoint182 = x3d.HAnimJoint()
HAnimJoint182.name = "l_wrist"
HAnimJoint182.DEF = "hanim_l_wrist"
HAnimJoint182.center = [0.213,0.811,-0.0338]
HAnimJoint182.ulimit = [0,0,0]
HAnimJoint182.llimit = [0,0,0]
HAnimSegment183 = x3d.HAnimSegment()
HAnimSegment183.name = "l_hand"
HAnimSegment183.DEF = "hanim_l_hand"
Transform184 = x3d.Transform()
Transform184.DEF = "l_hand_adjust"
Transform184.center = [0.213,0.811,-0.0338]
Transform184.rotation = [-0.06361,-0.9967,0.04988,1.333]
Transform184.translation = [0.213,0.811,-0.0338]
Shape185 = x3d.Shape()
Appearance186 = x3d.Appearance()
Material187 = x3d.Material()
Material187.DEF = "Skin_Color"
Material187.ambientIntensity = 0.25
Material187.diffuseColor = [0.749,0.601,0.462]

Appearance186.material = Material187

Shape185.appearance = Appearance186
IndexedFaceSet188 = x3d.IndexedFaceSet()
IndexedFaceSet188.coordIndex = [2,1,0,-1,5,4,3,-1,3,7,6,-1,2,3,6,-1,7,9,8,-1,6,7,8,-1,9,11,10,-1,8,9,10,-1,11,13,12,-1,10,11,12,-1,13,15,14,-1,12,13,14,-1,15,17,16,-1,14,15,16,-1,17,19,18,-1,16,17,18,-1,19,21,20,-1,18,19,20,-1,31,4,1,-1,4,5,0,-1,1,4,0,-1,5,3,2,-1,0,5,2,-1,26,25,24,-1,26,24,23,-1,27,26,23,-1,28,27,23,-1,28,23,22,-1,29,28,22,-1,29,22,21,-1,30,29,21,-1,15,13,11,-1,17,15,11,-1,19,17,11,-1,19,11,9,-1,31,19,9,-1,31,9,7,-1,4,31,7,-1,4,7,3,-1,30,21,19,-1,31,30,19,-1,12,14,16,-1,10,12,16,-1,10,16,18,-1,8,10,18,-1,6,8,1,-1,2,6,1,-1,39,38,37,-1,37,38,40,-1,37,40,36,-1,36,40,41,-1,36,41,35,-1,35,41,42,-1,35,42,34,-1,34,42,43,-1,34,43,33,-1,33,43,44,-1,33,44,32,-1,20,32,44,-1,20,44,45,-1,20,45,46,-1,47,8,18,-1,47,18,20,-1,47,20,46,-1,8,47,1,-1,22,33,32,-1,23,35,34,-1,23,36,35,-1,37,24,25,-1,40,38,27,-1,29,43,42,-1,45,44,30,-1,47,31,1,-1,47,46,31,-1,29,30,43,-1,30,44,43,-1,45,31,46,-1,45,30,31,-1,28,29,41,-1,29,42,41,-1,28,40,27,-1,28,41,40,-1,26,27,39,-1,27,38,39,-1,25,39,37,-1,25,26,39,-1,24,36,23,-1,24,37,36,-1,23,34,22,-1,34,33,22,-1,22,32,21,-1,32,20,21,-1]
IndexedFaceSet188.creaseAngle = 1.48
Coordinate189 = x3d.Coordinate()

IndexedFaceSet188.coord = Coordinate189

Shape185.geometry = IndexedFaceSet188

Transform184.children.append(Shape185)

HAnimSegment183.children.append(Transform184)

HAnimJoint182.children.append(HAnimSegment183)

HAnimJoint174.children.append(HAnimJoint182)

HAnimJoint166.children.append(HAnimJoint174)

HAnimJoint94.children.append(HAnimJoint166)
HAnimJoint190 = x3d.HAnimJoint()
HAnimJoint190.name = "r_shoulder"
HAnimJoint190.DEF = "hanim_r_shoulder"
HAnimJoint190.center = [-0.167,1.36,-0.0458]
HAnimJoint190.ulimit = [0,0,0]
HAnimJoint190.llimit = [0,0,0]
HAnimSegment191 = x3d.HAnimSegment()
HAnimSegment191.name = "r_upperarm"
HAnimSegment191.DEF = "hanim_r_upperarm"
Transform192 = x3d.Transform()
Transform192.DEF = "r_upperarm_adjust"
Transform192.center = [-0.182,1.22,-0.047]
Transform192.rotation = [1,0,0,0.0836]
Transform192.translation = [-0.167,1.36,-0.0458]
Shape193 = x3d.Shape()
Appearance194 = x3d.Appearance()
Material195 = x3d.Material()
Material195.USE = "WetShirtColor"

Appearance194.material = Material195

Shape193.appearance = Appearance194
IndexedFaceSet196 = x3d.IndexedFaceSet()
IndexedFaceSet196.coordIndex = [14,10,20,-1,10,13,20,-1,13,22,20,-1,19,14,20,-1,14,19,12,-1,19,20,24,-1,20,22,25,-1,22,13,25,-1,13,10,11,-1,10,14,5,-1,12,5,14,-1,5,11,10,-1,11,25,13,-1,25,24,20,-1,24,12,19,-1,12,24,9,-1,25,11,8,-1,11,5,2,-1,5,12,9,-1,9,2,5,-1,2,8,11,-1,8,23,25,-1,23,27,25,-1,21,9,24,-1,9,21,7,-1,27,23,18,-1,23,8,18,-1,8,2,6,-1,2,9,7,-1,7,1,2,-1,1,6,2,-1,6,18,8,-1,18,26,27,-1,16,7,21,-1,7,16,4,-1,16,26,17,-1,26,18,15,-1,18,6,3,-1,6,1,0,-1,1,7,0,-1,4,0,7,-1,0,3,6,-1,3,15,18,-1,15,17,26,-1,17,4,16,-1,3,0,15,-1,15,0,4,-1,15,4,17,-1,25,27,24,-1,27,21,24,-1,27,26,21,-1,26,16,21,-1]
IndexedFaceSet196.creaseAngle = 1.53
Coordinate197 = x3d.Coordinate()

IndexedFaceSet196.coord = Coordinate197

Shape193.geometry = IndexedFaceSet196

Transform192.children.append(Shape193)

HAnimSegment191.children.append(Transform192)

HAnimJoint190.children.append(HAnimSegment191)
HAnimJoint198 = x3d.HAnimJoint()
HAnimJoint198.name = "r_elbow"
HAnimJoint198.DEF = "hanim_r_elbow"
HAnimJoint198.center = [-0.192,1.07,-0.0498]
HAnimJoint198.ulimit = [0,0,0]
HAnimJoint198.llimit = [0,0,0]
HAnimSegment199 = x3d.HAnimSegment()
HAnimSegment199.name = "r_forearm"
HAnimSegment199.DEF = "hanim_r_forearm"
Transform200 = x3d.Transform()
Transform200.DEF = "r_forearm_adjust"
Transform200.center = [-0.198,0.961,-0.0397]
Transform200.rotation = [-1,0,0,0.1254]
Transform200.translation = [-0.192,1.07,-0.0498]
Shape201 = x3d.Shape()
Appearance202 = x3d.Appearance()
Material203 = x3d.Material()
Material203.USE = "WetShirtColor"

Appearance202.material = Material203

Shape201.appearance = Appearance202
IndexedFaceSet204 = x3d.IndexedFaceSet()
IndexedFaceSet204.coordIndex = [20,13,15,-1,13,8,15,-1,8,12,15,-1,12,18,15,-1,18,22,15,-1,22,20,15,-1,20,22,21,-1,22,18,24,-1,18,12,7,-1,12,8,7,-1,8,13,3,-1,13,20,10,-1,21,10,20,-1,10,3,13,-1,3,7,8,-1,7,19,18,-1,19,24,18,-1,24,21,22,-1,21,24,23,-1,24,19,16,-1,19,7,6,-1,7,3,1,-1,3,10,5,-1,10,21,17,-1,17,5,10,-1,5,1,3,-1,1,6,7,-1,6,16,19,-1,16,23,24,-1,23,17,21,-1,1,5,2,-1,5,17,9,-1,9,2,5,-1,1,4,6,-1,4,16,6,-1,23,9,17,-1,9,23,14,-1,23,16,11,-1,4,11,16,-1,11,14,23,-1,11,4,0,-1,11,0,14,-1,0,2,14,-1,14,2,9,-1,2,0,1,-1,0,4,1,-1]
IndexedFaceSet204.creaseAngle = 1.73
Coordinate205 = x3d.Coordinate()

IndexedFaceSet204.coord = Coordinate205

Shape201.geometry = IndexedFaceSet204

Transform200.children.append(Shape201)

HAnimSegment199.children.append(Transform200)

HAnimJoint198.children.append(HAnimSegment199)
HAnimJoint206 = x3d.HAnimJoint()
HAnimJoint206.name = "r_wrist"
HAnimJoint206.DEF = "hanim_r_wrist"
HAnimJoint206.center = [-0.217,0.811,-0.0338]
HAnimJoint206.ulimit = [0,0,0]
HAnimJoint206.llimit = [0,0,0]
HAnimSegment207 = x3d.HAnimSegment()
HAnimSegment207.name = "r_hand"
HAnimSegment207.DEF = "hanim_r_hand"
Transform208 = x3d.Transform()
Transform208.DEF = "r_hand_adjust"
Transform208.center = [-0.217,0.811,-0.0338]
Transform208.rotation = [-0.09024,0.994,-0.0624,1.216]
Shape209 = x3d.Shape()
Appearance210 = x3d.Appearance()
Material211 = x3d.Material()
Material211.USE = "Skin_Color"

Appearance210.material = Material211

Shape209.appearance = Appearance210
IndexedFaceSet212 = x3d.IndexedFaceSet()
IndexedFaceSet212.coordIndex = [10,9,0,-1,11,30,31,-1,1,12,11,-1,1,11,0,-1,2,13,12,-1,2,12,1,-1,3,14,13,-1,3,13,2,-1,4,15,14,-1,4,14,3,-1,5,16,15,-1,5,15,4,-1,6,17,16,-1,6,16,5,-1,7,18,17,-1,7,17,6,-1,8,19,18,-1,8,18,7,-1,10,31,30,-1,10,30,9,-1,0,11,31,-1,0,31,10,-1,22,23,24,-1,21,22,24,-1,21,24,25,-1,21,25,26,-1,20,21,26,-1,20,26,27,-1,19,20,27,-1,19,27,28,-1,14,15,16,-1,14,16,17,-1,14,17,18,-1,13,14,18,-1,13,18,29,-1,12,13,29,-1,12,29,30,-1,11,12,30,-1,18,19,28,-1,18,28,29,-1,6,5,4,-1,6,4,3,-1,7,6,3,-1,7,3,2,-1,9,2,1,-1,9,1,0,-1,32,38,33,-1,33,38,39,-1,33,39,34,-1,34,39,40,-1,34,40,35,-1,35,40,41,-1,35,41,36,-1,36,41,42,-1,36,42,37,-1,37,42,43,-1,37,43,44,-1,44,43,8,-1,44,8,45,-1,45,8,46,-1,46,8,7,-1,46,7,2,-1,46,2,47,-1,9,47,2,-1,25,34,35,-1,25,33,34,-1,25,24,33,-1,24,32,33,-1,32,24,23,-1,40,39,21,-1,41,40,21,-1,43,19,8,-1,43,20,19,-1,43,42,20,-1,21,20,41,-1,20,42,41,-1,38,22,39,-1,22,21,39,-1,32,23,38,-1,23,22,38,-1,26,25,35,-1,27,36,37,-1,27,37,28,-1,37,44,28,-1,26,35,27,-1,35,36,27,-1,28,44,45,-1,29,46,47,-1,29,9,30,-1,29,47,9,-1,28,45,29,-1,45,46,29,-1]
IndexedFaceSet212.creaseAngle = 1.57
Coordinate213 = x3d.Coordinate()

IndexedFaceSet212.coord = Coordinate213

Shape209.geometry = IndexedFaceSet212

Transform208.children.append(Shape209)

HAnimSegment207.children.append(Transform208)

HAnimJoint206.children.append(HAnimSegment207)

HAnimJoint198.children.append(HAnimJoint206)

HAnimJoint190.children.append(HAnimJoint198)

HAnimJoint94.children.append(HAnimJoint190)
HAnimJoint214 = x3d.HAnimJoint()
HAnimJoint214.name = "vc4"
HAnimJoint214.DEF = "hanim_vc4"
HAnimJoint214.center = [0,1.43,-0.0458]
HAnimJoint214.ulimit = [0,0,0]
HAnimJoint214.llimit = [0,0,0]
HAnimSegment215 = x3d.HAnimSegment()
HAnimSegment215.name = "c4"
HAnimSegment215.DEF = "hanim_c4"
Shape216 = x3d.Shape()
Appearance217 = x3d.Appearance()
Material218 = x3d.Material()
Material218.USE = "WetShirtColor"

Appearance217.material = Material218

Shape216.appearance = Appearance217
IndexedFaceSet219 = x3d.IndexedFaceSet()
IndexedFaceSet219.DEF = "neck"
IndexedFaceSet219.coordIndex = [6,5,2,-1,6,2,3,-1,5,4,1,-1,5,1,2,-1,4,7,0,-1,4,0,1,-1,11,10,9,-1,11,9,8,-1,10,13,12,-1,10,12,9,-1,13,15,14,-1,13,14,12,-1,6,3,11,-1,6,11,8,-1,7,14,15,-1,7,15,0,-1,2,10,11,-1,2,11,3,-1,2,1,13,-1,2,13,10,-1,1,0,15,-1,1,15,13,-1,9,5,6,-1,9,6,8,-1,9,12,4,-1,9,4,5,-1,12,14,7,-1,12,7,4,-1]
IndexedFaceSet219.creaseAngle = 1.91
Coordinate220 = x3d.Coordinate()

IndexedFaceSet219.coord = Coordinate220

Shape216.geometry = IndexedFaceSet219

HAnimSegment215.children.append(Shape216)

HAnimJoint214.children.append(HAnimSegment215)
HAnimJoint221 = x3d.HAnimJoint()
HAnimJoint221.name = "skullbase"
HAnimJoint221.DEF = "hanim_skullbase"
HAnimJoint221.center = [0,1.54,-0.0409]
HAnimJoint221.ulimit = [0,0,0]
HAnimJoint221.llimit = [0,0,0]
HAnimSegment222 = x3d.HAnimSegment()
HAnimSegment222.name = "skull"
HAnimSegment222.DEF = "hanim_skull"
Shape223 = x3d.Shape()
Appearance224 = x3d.Appearance()
Material225 = x3d.Material()
Material225.USE = "Skin_Color"

Appearance224.material = Material225

Shape223.appearance = Appearance224
IndexedFaceSet226 = x3d.IndexedFaceSet()
IndexedFaceSet226.DEF = "headIFS"
IndexedFaceSet226.colorIndex = [1,1,1,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,1,1,1,-1,1,1,1,-1,0,0,0,-1,1,1,1,-1,1,1,1,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,2,2,2,-1,2,2,2,-1,2,2,2,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,2,2,2,-1,2,2,2,-1,2,2,2,-1,0,0,0,-1,0,0,0,-1,2,2,2,-1,2,2,2,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,1,1,1,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,2,2,2,-1,2,2,2,-1,2,2,2,-1,2,2,2,-1,2,2,2,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,2,2,2,-1,2,2,2,-1,2,2,2,-1,0,0,0,-1,0,0,0,-1,2,2,2,-1,2,2,2,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,4,4,4,-1,0,0,0,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,0,0,0,-1,0,0,0,-1,4,4,4,-1,0,0,0,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,0,0,0,-1,0,0,0,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1,4,4,4,-1]
IndexedFaceSet226.coordIndex = [48,87,58,-1,91,92,59,-1,59,92,88,-1,88,93,231,-1,232,86,233,-1,86,89,233,-1,89,57,56,-1,49,55,57,-1,102,86,96,-1,86,90,96,-1,97,95,96,-1,97,127,95,-1,41,96,154,-1,41,102,96,-1,99,102,41,-1,153,99,41,-1,102,40,86,-1,234,235,236,-1,87,237,58,-1,56,57,91,-1,87,234,237,-1,234,236,237,-1,89,49,57,-1,49,50,55,-1,40,89,86,-1,89,56,233,-1,232,90,86,-1,90,97,96,-1,92,93,88,-1,93,94,231,-1,232,231,94,-1,97,90,232,-1,96,42,154,-1,95,42,96,-1,53,46,45,-1,53,45,51,-1,53,51,92,-1,92,51,52,-1,92,52,93,-1,94,93,52,-1,94,52,4,-1,97,232,94,-1,54,47,46,-1,54,46,53,-1,55,47,54,-1,50,47,55,-1,34,33,50,-1,34,50,49,-1,35,34,49,-1,35,49,89,-1,35,89,40,-1,99,39,102,-1,39,35,40,-1,31,34,35,-1,31,35,32,-1,14,32,35,-1,14,35,39,-1,14,39,98,-1,137,38,153,-1,38,99,153,-1,38,98,99,-1,37,238,239,-1,11,238,37,-1,101,37,36,-1,241,141,242,-1,10,12,242,-1,12,13,14,-1,12,14,243,-1,13,15,32,-1,13,32,14,-1,15,16,31,-1,15,31,32,-1,2,70,10,-1,2,10,141,-1,70,69,12,-1,70,12,10,-1,69,68,13,-1,69,13,12,-1,68,67,15,-1,68,15,13,-1,67,66,16,-1,67,16,15,-1,98,39,99,-1,101,11,37,-1,100,101,36,-1,36,244,240,-1,141,10,242,-1,12,243,242,-1,36,37,239,-1,36,239,244,-1,57,55,91,-1,55,54,91,-1,39,40,102,-1,123,103,120,-1,114,122,104,-1,115,122,114,-1,208,105,115,-1,210,119,211,-1,210,106,119,-1,116,107,106,-1,107,108,117,-1,126,119,109,-1,126,110,119,-1,126,95,125,-1,95,127,125,-1,154,126,111,-1,126,109,111,-1,111,109,112,-1,111,112,153,-1,119,113,109,-1,207,213,214,-1,123,209,103,-1,213,212,214,-1,209,214,103,-1,209,207,214,-1,107,117,106,-1,108,118,117,-1,119,106,113,-1,210,116,106,-1,119,110,211,-1,126,125,110,-1,115,105,122,-1,208,124,105,-1,124,208,211,-1,211,110,125,-1,154,42,126,-1,126,42,95,-1,168,128,121,-1,170,168,121,-1,122,170,121,-1,172,170,122,-1,105,172,122,-1,172,105,124,-1,4,172,124,-1,124,211,125,-1,128,130,129,-1,121,128,129,-1,129,130,108,-1,108,130,118,-1,118,131,132,-1,117,118,132,-1,117,132,133,-1,106,117,133,-1,113,106,133,-1,109,152,112,-1,113,133,152,-1,133,132,134,-1,135,133,134,-1,133,135,136,-1,152,133,136,-1,148,152,136,-1,153,138,137,-1,153,112,138,-1,112,148,138,-1,219,217,139,-1,36,240,149,-1,139,217,140,-1,149,139,151,-1,36,149,100,-1,220,141,241,-1,220,150,142,-1,136,143,150,-1,221,136,150,-1,135,144,143,-1,136,135,143,-1,134,158,144,-1,135,134,144,-1,142,161,2,-1,141,142,2,-1,150,145,161,-1,142,150,161,-1,143,146,145,-1,150,143,145,-1,144,147,146,-1,143,144,146,-1,158,160,147,-1,144,158,147,-1,112,152,148,-1,139,140,151,-1,149,151,100,-1,240,218,149,-1,220,142,141,-1,220,221,150,-1,219,139,149,-1,218,219,149,-1,104,108,107,-1,104,129,108,-1,109,113,152,-1,153,41,111,-1,129,104,122,-1,129,122,121,-1,91,54,92,-1,54,53,92,-1,97,94,127,-1,127,94,4,-1,125,127,124,-1,127,4,124,-1,154,111,41,-1,31,30,33,-1,31,33,34,-1,16,17,30,-1,16,30,31,-1,66,65,17,-1,66,17,16,-1,2,73,156,-1,2,156,70,-1,156,72,66,-1,156,66,67,-1,156,67,68,-1,156,68,69,-1,156,69,70,-1,72,71,65,-1,72,65,66,-1,17,18,30,-1,45,44,51,-1,51,44,43,-1,51,43,52,-1,52,43,1,-1,52,1,4,-1,245,246,27,-1,245,27,3,-1,246,247,28,-1,246,28,27,-1,248,22,29,-1,248,29,28,-1,248,28,247,-1,27,26,0,-1,27,0,3,-1,27,28,25,-1,27,25,26,-1,29,24,25,-1,29,25,28,-1,22,23,24,-1,22,24,29,-1,249,250,22,-1,249,22,248,-1,250,60,23,-1,250,23,22,-1,17,254,18,-1,65,254,17,-1,71,64,65,-1,63,74,75,-1,63,75,61,-1,64,255,254,-1,75,62,61,-1,62,76,60,-1,76,77,23,-1,76,23,60,-1,77,24,23,-1,77,78,25,-1,77,25,24,-1,78,84,26,-1,78,26,25,-1,84,192,0,-1,84,0,26,-1,84,83,193,-1,84,193,192,-1,79,83,84,-1,79,84,78,-1,76,79,78,-1,76,78,77,-1,80,83,79,-1,80,204,83,-1,75,81,80,-1,81,85,204,-1,81,204,80,-1,74,81,75,-1,74,82,81,-1,82,5,85,-1,82,85,81,-1,155,8,71,-1,155,71,72,-1,8,6,64,-1,8,64,71,-1,6,7,255,-1,6,255,64,-1,7,9,256,-1,7,256,255,-1,9,257,256,-1,73,155,156,-1,155,72,156,-1,204,193,83,-1,64,254,65,-1,131,157,134,-1,132,131,134,-1,157,159,158,-1,134,157,158,-1,159,206,160,-1,158,159,160,-1,203,73,2,-1,161,203,2,-1,160,162,203,-1,147,160,203,-1,146,147,203,-1,145,146,203,-1,161,145,203,-1,206,163,162,-1,160,206,162,-1,157,164,159,-1,170,169,168,-1,171,169,170,-1,172,171,170,-1,1,171,172,-1,4,1,172,-1,173,227,245,-1,3,173,245,-1,174,226,227,-1,173,174,227,-1,176,175,215,-1,174,176,215,-1,226,174,215,-1,0,177,173,-1,3,0,173,-1,178,174,173,-1,177,178,173,-1,178,179,176,-1,174,178,176,-1,179,180,175,-1,176,179,175,-1,175,225,216,-1,215,175,216,-1,180,181,225,-1,175,180,225,-1,164,228,159,-1,159,228,206,-1,206,185,163,-1,187,186,184,-1,183,187,184,-1,228,229,185,-1,183,182,187,-1,181,188,182,-1,180,189,188,-1,181,180,188,-1,180,179,189,-1,178,190,189,-1,179,178,189,-1,177,191,190,-1,178,177,190,-1,0,192,191,-1,177,0,191,-1,193,205,191,-1,192,193,191,-1,191,205,194,-1,190,191,194,-1,190,194,188,-1,189,190,188,-1,194,205,195,-1,205,204,195,-1,195,196,187,-1,204,85,196,-1,195,204,196,-1,187,196,186,-1,196,197,186,-1,85,5,197,-1,196,85,197,-1,163,198,202,-1,162,163,202,-1,185,199,198,-1,163,185,198,-1,229,200,199,-1,185,229,199,-1,230,201,200,-1,229,230,200,-1,230,257,201,-1,203,202,73,-1,203,162,202,-1,205,193,204,-1,206,228,185,-1,198,8,155,-1,198,155,202,-1,155,73,202,-1,199,6,8,-1,199,8,198,-1,7,6,199,-1,7,199,200,-1,201,9,7,-1,201,7,200,-1,201,257,9,-1,188,194,195,-1,188,195,182,-1,195,187,182,-1,80,79,76,-1,80,62,75,-1,80,76,62,-1,47,50,33,-1,131,118,130,-1,20,21,47,-1,21,46,47,-1,20,33,19,-1,20,47,33,-1,33,30,19,-1,30,18,19,-1,62,60,251,-1,60,250,251,-1,252,61,251,-1,61,62,251,-1,252,63,61,-1,252,253,63,-1,166,130,167,-1,130,128,167,-1,166,131,130,-1,166,165,131,-1,165,157,131,-1,165,164,157,-1,224,181,182,-1,224,225,181,-1,224,183,223,-1,224,182,183,-1,183,184,223,-1,184,222,223,-1]
Coordinate227 = x3d.Coordinate()
Coordinate227.DEF = "Face"

IndexedFaceSet226.coord = Coordinate227
Color228 = x3d.Color()

IndexedFaceSet226.color = Color228

Shape223.geometry = IndexedFaceSet226

HAnimSegment222.children.append(Shape223)
Transform229 = x3d.Transform()
Transform229.DEF = "maskAndSnorkel"
Transform229.translation = [0,1.54,-0.0409]
Inline230 = x3d.Inline()
Inline230.DEF = "MaskAndSnorkel"
Inline230.url = ["MaskAndSnorkel.x3d","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Legacy/MaskAndSnorkel.x3d","MaskAndSnorkel.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Legacy/MaskAndSnorkel.wrl"]

Transform229.children.append(Inline230)

HAnimSegment222.children.append(Transform229)
Transform231 = x3d.Transform()
Transform231.DEF = "mouthpiece"
Transform231.rotation = [0.86,-0.58,-0.58,2.09]
Transform231.translation = [0,1.54,-0.0409]
Transform232 = x3d.Transform()
Transform232.translation = [0,0.0018,0]
Shape233 = x3d.Shape()
Appearance234 = x3d.Appearance()
Material235 = x3d.Material()
Material235.DEF = "gray"
Material235.ambientIntensity = 0.3
Material235.diffuseColor = [0.9,0.9,0.89]
Material235.shininess = 0.1
Material235.specularColor = [0.5,0.5,0.5]

Appearance234.material = Material235

Shape233.appearance = Appearance234
Cylinder236 = x3d.Cylinder()
Cylinder236.height = 0.006
Cylinder236.radius = 0.015

Shape233.geometry = Cylinder236

Transform232.children.append(Shape233)

Transform231.children.append(Transform232)
Transform237 = x3d.Transform()
Shape238 = x3d.Shape()
Appearance239 = x3d.Appearance()
Material240 = x3d.Material()
Material240.DEF = "black"
Material240.diffuseColor = [0,0,0]

Appearance239.material = Material240

Shape238.appearance = Appearance239
Cone241 = x3d.Cone()
Cone241.bottomRadius = 0.03
Cone241.height = 0.01

Shape238.geometry = Cone241

Transform237.children.append(Shape238)

Transform231.children.append(Transform237)
Transform242 = x3d.Transform()
Transform242.translation = [0,-0.015,0]
Shape243 = x3d.Shape()
Appearance244 = x3d.Appearance()
Material245 = x3d.Material()
Material245.USE = "black"

Appearance244.material = Material245

Shape243.appearance = Appearance244
Cylinder246 = x3d.Cylinder()
Cylinder246.height = 0.02
Cylinder246.radius = 0.03

Shape243.geometry = Cylinder246

Transform242.children.append(Shape243)

Transform231.children.append(Transform242)
Transform247 = x3d.Transform()
Transform247.translation = [0,-0.025,0]
Shape248 = x3d.Shape()
Appearance249 = x3d.Appearance()
Material250 = x3d.Material()
Material250.USE = "black"

Appearance249.material = Material250

Shape248.appearance = Appearance249
Cylinder251 = x3d.Cylinder()
Cylinder251.height = 0.02
Cylinder251.radius = 0.015

Shape248.geometry = Cylinder251

Transform247.children.append(Shape248)

Transform231.children.append(Transform247)
Transform252 = x3d.Transform()
Transform252.rotation = [0,0,1,0.9]
Transform252.translation = [0,-0.04,0]
Shape253 = x3d.Shape()
Shape253.DEF = "mouthpiecePlastic"
Appearance254 = x3d.Appearance()
Material255 = x3d.Material()
Material255.diffuseColor = [1,1,1]
Material255.emissiveColor = [1,1,1]

Appearance254.material = Material255

Shape253.appearance = Appearance254
Box256 = x3d.Box()
Box256.size = [0.002,0.03,0.018]

Shape253.geometry = Box256

Transform252.children.append(Shape253)

Transform231.children.append(Transform252)
Transform257 = x3d.Transform()
Transform257.rotation = [0,0,1,-0.9]
Transform257.translation = [0,-0.04,0]
Shape258 = x3d.Shape()
Shape258.USE = "mouthpiecePlastic"

Transform257.children.append(Shape258)

Transform231.children.append(Transform257)
Transform259 = x3d.Transform()
Transform259.rotation = [1,0,0,1.57]
Transform259.translation = [0,-0.015,0.03]
Shape260 = x3d.Shape()
Appearance261 = x3d.Appearance()
Material262 = x3d.Material()
Material262.USE = "gray"

Appearance261.material = Material262

Shape260.appearance = Appearance261
Cylinder263 = x3d.Cylinder()
Cylinder263.height = 0.02
Cylinder263.radius = 0.0075

Shape260.geometry = Cylinder263

Transform259.children.append(Shape260)

Transform231.children.append(Transform259)
#x = 0, y = 50, z = -270
Transform264 = x3d.Transform()
Transform264.DEF = "airTube"
Transform264.rotation = [0,1,0,1.57]
Transform264.scale = [0.7,0.7,0.7]
Transform264.translation = [0,-0.02,0.055]
Transform265 = x3d.Transform()
Transform265.rotation = [-0.21,0.21,-0.95,4.67]
Shape266 = x3d.Shape()
Appearance267 = x3d.Appearance()
Material268 = x3d.Material()
Material268.diffuseColor = [0,0,0]

Appearance267.material = Material268

Shape266.appearance = Appearance267
Extrusion269 = x3d.Extrusion()

Shape266.geometry = Extrusion269

Transform265.children.append(Shape266)

Transform264.children.append(Transform265)

Transform231.children.append(Transform264)

HAnimSegment222.children.append(Transform231)
Transform270 = x3d.Transform()
Transform270.DEF = "Bubbles"
Transform270.scale = [0.35,0.35,0.35]
Transform270.translation = [0,1.54,-0.0409]
Inline271 = x3d.Inline()
Inline271.DEF = "bubbles"
Inline271.url = ["Bubbles.x3d","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Legacy/Bubbles.x3d","Bubbles.wrl","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Legacy/Bubbles.wrl"]

Transform270.children.append(Inline271)

HAnimSegment222.children.append(Transform270)

HAnimJoint221.children.append(HAnimSegment222)

HAnimJoint214.children.append(HAnimJoint221)

HAnimJoint94.children.append(HAnimJoint214)

HAnimJoint32.children.append(HAnimJoint94)

HAnimHumanoid31.skeleton.append(HAnimJoint32)
HAnimJoint272 = x3d.HAnimJoint()
HAnimJoint272.USE = "hanim_humanoid_root"

HAnimHumanoid31.joints.append(HAnimJoint272)
HAnimJoint273 = x3d.HAnimJoint()
HAnimJoint273.USE = "hanim_sacroiliac"

HAnimHumanoid31.joints.append(HAnimJoint273)
HAnimJoint274 = x3d.HAnimJoint()
HAnimJoint274.USE = "hanim_vl1"

HAnimHumanoid31.joints.append(HAnimJoint274)
HAnimJoint275 = x3d.HAnimJoint()
HAnimJoint275.USE = "hanim_vc4"

HAnimHumanoid31.joints.append(HAnimJoint275)
HAnimJoint276 = x3d.HAnimJoint()
HAnimJoint276.USE = "hanim_skullbase"

HAnimHumanoid31.joints.append(HAnimJoint276)
HAnimJoint277 = x3d.HAnimJoint()
HAnimJoint277.USE = "hanim_l_ankle"

HAnimHumanoid31.joints.append(HAnimJoint277)
HAnimJoint278 = x3d.HAnimJoint()
HAnimJoint278.USE = "hanim_r_ankle"

HAnimHumanoid31.joints.append(HAnimJoint278)
HAnimJoint279 = x3d.HAnimJoint()
HAnimJoint279.USE = "hanim_l_elbow"

HAnimHumanoid31.joints.append(HAnimJoint279)
HAnimJoint280 = x3d.HAnimJoint()
HAnimJoint280.USE = "hanim_r_elbow"

HAnimHumanoid31.joints.append(HAnimJoint280)
HAnimJoint281 = x3d.HAnimJoint()
HAnimJoint281.USE = "hanim_l_hip"

HAnimHumanoid31.joints.append(HAnimJoint281)
HAnimJoint282 = x3d.HAnimJoint()
HAnimJoint282.USE = "hanim_r_hip"

HAnimHumanoid31.joints.append(HAnimJoint282)
HAnimJoint283 = x3d.HAnimJoint()
HAnimJoint283.USE = "hanim_l_knee"

HAnimHumanoid31.joints.append(HAnimJoint283)
HAnimJoint284 = x3d.HAnimJoint()
HAnimJoint284.USE = "hanim_r_knee"

HAnimHumanoid31.joints.append(HAnimJoint284)
HAnimJoint285 = x3d.HAnimJoint()
HAnimJoint285.USE = "hanim_l_shoulder"

HAnimHumanoid31.joints.append(HAnimJoint285)
HAnimJoint286 = x3d.HAnimJoint()
HAnimJoint286.USE = "hanim_r_shoulder"

HAnimHumanoid31.joints.append(HAnimJoint286)
HAnimJoint287 = x3d.HAnimJoint()
HAnimJoint287.USE = "hanim_l_wrist"

HAnimHumanoid31.joints.append(HAnimJoint287)
HAnimJoint288 = x3d.HAnimJoint()
HAnimJoint288.USE = "hanim_r_wrist"

HAnimHumanoid31.joints.append(HAnimJoint288)
HAnimSegment289 = x3d.HAnimSegment()
HAnimSegment289.USE = "hanim_pelvis"

HAnimHumanoid31.segments.append(HAnimSegment289)
HAnimSegment290 = x3d.HAnimSegment()
HAnimSegment290.USE = "hanim_l1"

HAnimHumanoid31.segments.append(HAnimSegment290)
HAnimSegment291 = x3d.HAnimSegment()
HAnimSegment291.USE = "hanim_c4"

HAnimHumanoid31.segments.append(HAnimSegment291)
HAnimSegment292 = x3d.HAnimSegment()
HAnimSegment292.USE = "hanim_skull"

HAnimHumanoid31.segments.append(HAnimSegment292)
HAnimSegment293 = x3d.HAnimSegment()
HAnimSegment293.USE = "hanim_l_calf"

HAnimHumanoid31.segments.append(HAnimSegment293)
HAnimSegment294 = x3d.HAnimSegment()
HAnimSegment294.USE = "hanim_r_calf"

HAnimHumanoid31.segments.append(HAnimSegment294)
HAnimSegment295 = x3d.HAnimSegment()
HAnimSegment295.USE = "hanim_l_forearm"

HAnimHumanoid31.segments.append(HAnimSegment295)
HAnimSegment296 = x3d.HAnimSegment()
HAnimSegment296.USE = "hanim_r_forearm"

HAnimHumanoid31.segments.append(HAnimSegment296)
HAnimSegment297 = x3d.HAnimSegment()
HAnimSegment297.USE = "hanim_l_hand"

HAnimHumanoid31.segments.append(HAnimSegment297)
HAnimSegment298 = x3d.HAnimSegment()
HAnimSegment298.USE = "hanim_r_hand"

HAnimHumanoid31.segments.append(HAnimSegment298)
HAnimSegment299 = x3d.HAnimSegment()
HAnimSegment299.USE = "hanim_l_hindfoot"

HAnimHumanoid31.segments.append(HAnimSegment299)
HAnimSegment300 = x3d.HAnimSegment()
HAnimSegment300.USE = "hanim_r_hindfoot"

HAnimHumanoid31.segments.append(HAnimSegment300)
HAnimSegment301 = x3d.HAnimSegment()
HAnimSegment301.USE = "hanim_l_thigh"

HAnimHumanoid31.segments.append(HAnimSegment301)
HAnimSegment302 = x3d.HAnimSegment()
HAnimSegment302.USE = "hanim_r_thigh"

HAnimHumanoid31.segments.append(HAnimSegment302)
HAnimSegment303 = x3d.HAnimSegment()
HAnimSegment303.USE = "hanim_l_upperarm"

HAnimHumanoid31.segments.append(HAnimSegment303)
HAnimSegment304 = x3d.HAnimSegment()
HAnimSegment304.USE = "hanim_r_upperarm"

HAnimHumanoid31.segments.append(HAnimSegment304)

Transform30.children.append(HAnimHumanoid31)

Transform20.children.append(Transform30)

Transform19.children.append(Transform20)

Group18.children.append(Transform19)

Scene15.children.append(Group18)
Script305 = x3d.Script()
Script305.DEF = "finWarpScript"
field306 = x3d.field()
field306.name = "set_rotationLeft"
field306.accessType = "inputOnly"
field306.type = "SFRotation"

Script305.field.append(field306)
field307 = x3d.field()
field307.name = "set_rotationRight"
field307.accessType = "inputOnly"
field307.type = "SFRotation"

Script305.field.append(field307)
field308 = x3d.field()
field308.name = "finWarpLeft"
field308.accessType = "outputOnly"
field308.type = "SFBool"

Script305.field.append(field308)
field309 = x3d.field()
field309.name = "finWarpRight"
field309.accessType = "outputOnly"
field309.type = "SFBool"

Script305.field.append(field309)

Script305.sourceCode = '''ecmascript:\n"+
"function set_rotationLeft(rotationValue, timeStamp)\n"+
"{\n"+
"	if (rotationValue[0] <= 0)\n"+
"	{\n"+
"		finWarpLeft = false;\n"+
"	}\n"+
"	else\n"+
"	{\n"+
"		finWarpLeft = true;\n"+
"	}\n"+
"//	print ('Left  rotationValue[0] ' + rotationValue[0] + ', finWarpLeft=' + finWarpLeft);\n"+
"}\n"+
"\n"+
"function set_rotationRight(rotationValue, timeStamp)\n"+
"{\n"+
"	if (rotationValue[0] <= 0)\n"+
"	{\n"+
"		finWarpRight = false;\n"+
"	}\n"+
"	else\n"+
"	{\n"+
"		finWarpRight = true;\n"+
"	}\n"+
"//	print ('Right rotationValue[0] ' + rotationValue[0] + ', finWarpRight=' + finWarpRight);\n"+
"}'''

Scene15.children.append(Script305)
#Fins animation
ProximitySensor310 = x3d.ProximitySensor()
ProximitySensor310.DEF = "FinTriggerProximitySensor"
ProximitySensor310.size = [15,15,15]

Scene15.children.append(ProximitySensor310)
TimeSensor311 = x3d.TimeSensor()
TimeSensor311.DEF = "FinClock"
TimeSensor311.cycleInterval = 7
TimeSensor311.loop = True

Scene15.children.append(TimeSensor311)
Group312 = x3d.Group()
Script313 = x3d.Script()
Script313.DEF = "FinScript"
field314 = x3d.field()
field314.name = "keyValueRight"
field314.accessType = "outputOnly"
field314.type = "MFVec3f"

Script313.field.append(field314)
field315 = x3d.field()
field315.name = "keyValueLeft"
field315.accessType = "outputOnly"
field315.type = "MFVec3f"

Script313.field.append(field315)
field316 = x3d.field()
field316.name = "set_fraction"
field316.accessType = "inputOnly"
field316.type = "SFFloat"

Script313.field.append(field316)
field317 = x3d.field()
field317.name = "finL"
field317.accessType = "inputOnly"
field317.type = "SFBool"

Script313.field.append(field317)
field318 = x3d.field()
field318.name = "finR"
field318.accessType = "inputOnly"
field318.type = "SFBool"

Script313.field.append(field318)
field319 = x3d.field()
field319.name = "finWarpL"
field319.accessType = "initializeOnly"
field319.type = "SFInt32"
field319.value = 0

Script313.field.append(field319)
field320 = x3d.field()
field320.name = "finWarpR"
field320.accessType = "initializeOnly"
field320.type = "SFInt32"
field320.value = 0

Script313.field.append(field320)
field321 = x3d.field()
field321.name = "traceEnabled"
field321.accessType = "initializeOnly"
field321.type = "SFBool"
field321.value = False

Script313.field.append(field321)

Script313.sourceCode = '''ecmascript:\n"+
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
"}\n"+
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
" {\n"+
"	if (finWarpL == 1)\n"+
"	{\n"+
"		// level 3 (warp outside) Left\n"+
"		kVL7 = new SFVec3f(1.25, 0, 25);\n"+
"		kVL8 = new SFVec3f(2.5, 0, 30);\n"+
" 		kVL9 = new SFVec3f(3.25, 0, 34);\n"+
"	}\n"+
"	else\n"+
"	{\n"+
"		// level -2 (warp inside) Left\n"+
"		kVL7 = new SFVec3f(-1.25, 0, 25);\n"+
"		kVL8 = new SFVec3f(-2.5, 0, 30);\n"+
" 		kVL9 = new SFVec3f(-3.25, 0, 34);\n"+
"	}\n"+
"\n"+
"	if (finWarpR == 0)\n"+
"	{\n"+
"		// level  1 (warp outside ) Right\n"+
"		kVR7 = new SFVec3f(1.25, 0, 25);\n"+
"		kVR8 = new SFVec3f(2.5, 0, 30);\n"+
" 		kVR9 = new SFVec3f(3.25, 0, 34);\n"+
"\n"+
"	}\n"+
"	else\n"+
"	{\n"+
"		// level  -2 ( warp inside) Right\n"+
"		kVR7 = new SFVec3f(-1.25, 0, 25);\n"+
"		kVR8 = new SFVec3f(-2.5, 0, 30);\n"+
" 		kVR9 = new SFVec3f(-3.25, 0, 34);\n"+
"	}\n"+
"\n"+
"	// Left Fin (fixed spine)\n"+
"	kVL1 = new SFVec3f(0, 0, 1);\n"+
"	kVL2 = new SFVec3f(0, 0, 5);\n"+
"	kVL3 = new SFVec3f(0, 0, 8);\n"+
"	kVL4 = new SFVec3f(0, 0, 12);\n"+
"	kVL5 = new SFVec3f(0, 0, 15);\n"+
"	kVL6 = new SFVec3f(0, 0, 18);\n"+
"	keyValueLeft = new MFVec3f(kVL1, kVL2, kVL3, kVL4, kVL5, kVL6, kVL7, kVL8, kVL9);\n"+
"\n"+
"	// Right Fin (fixed spine)\n"+
"	kVR1 = new SFVec3f(0, 0, 1);\n"+
"	kVR2 = new SFVec3f(0, 0, 5);\n"+
"	kVR3 = new SFVec3f(0, 0, 8);\n"+
"	kVR4 = new SFVec3f(0, 0, 12);\n"+
"	kVR5 = new SFVec3f(0, 0, 15);\n"+
"	kVR6 = new SFVec3f(0, 0, 18);\n"+
"	keyValueRight = new MFVec3f(kVR1, kVR2, kVR3, kVR4, kVR5, kVR6, kVR7, kVR8, kVR9);\n"+
"\n"+
"	//tracePrint ('keyValueLeft =' + keyValueLeft);\n"+
"	//tracePrint ('keyValueRight=' + keyValueRight);\n"+
"}\n"+
"\n"+
"function set_fraction (value, timeStamp)\n"+
"{\n"+
"	finMove(value);\n"+
"	//tracePrint('time fraction =' + value);\n"+
"}\n"+
"\n"+
"function tracePrint (outputString)\n"+
"{\n"+
"	if (traceEnabled) Browser.print ('[Fin Move]' + outputString);\n"+
"}'''

Group312.children.append(Script313)
ROUTE322 = x3d.ROUTE()
ROUTE322.fromField = "finWarpLeft"
ROUTE322.fromNode = "finWarpScript"
ROUTE322.toField = "finL"
ROUTE322.toNode = "FinScript"

Group312.children.append(ROUTE322)
ROUTE323 = x3d.ROUTE()
ROUTE323.fromField = "finWarpRight"
ROUTE323.fromNode = "finWarpScript"
ROUTE323.toField = "finR"
ROUTE323.toNode = "FinScript"

Group312.children.append(ROUTE323)
ROUTE324 = x3d.ROUTE()
ROUTE324.fromField = "isActive"
ROUTE324.fromNode = "FinTriggerProximitySensor"
ROUTE324.toField = "enabled"
ROUTE324.toNode = "FinClock"

Group312.children.append(ROUTE324)
ROUTE325 = x3d.ROUTE()
ROUTE325.fromField = "fraction_changed"
ROUTE325.fromNode = "FinClock"
ROUTE325.toField = "set_fraction"
ROUTE325.toNode = "FinScript"

Group312.children.append(ROUTE325)
ROUTE326 = x3d.ROUTE()
ROUTE326.fromField = "keyValueRight"
ROUTE326.fromNode = "FinScript"
ROUTE326.toField = "set_spine"
ROUTE326.toNode = "FinExtrusionRight"

Group312.children.append(ROUTE326)
ROUTE327 = x3d.ROUTE()
ROUTE327.fromField = "keyValueLeft"
ROUTE327.fromNode = "FinScript"
ROUTE327.toField = "set_spine"
ROUTE327.toNode = "FinExtrusionLeft"

Group312.children.append(ROUTE327)

Scene15.children.append(Group312)
NavigationInfo328 = x3d.NavigationInfo()
NavigationInfo328.avatarSize = [0.15,1.53,0.75]
NavigationInfo328.speed = 0.5

Scene15.children.append(NavigationInfo328)
WorldInfo329 = x3d.WorldInfo()
WorldInfo329.info = ["Copyright (c) 1997. 3Name3D / Yglesias Wallock Divekar, Inc."]
WorldInfo329.title = "Nancy - an HAnim compliant avatar by 3Name3D"

Scene15.children.append(WorldInfo329)
Group330 = x3d.Group()
Group330.DEF = "Animations"
Group331 = x3d.Group()
Group331.DEF = "Dive_Animation"
OrientationInterpolator332 = x3d.OrientationInterpolator()
OrientationInterpolator332.DEF = "r_ankle_RotationInterpolator_BasicDive"
OrientationInterpolator332.key = [0,0.125,0.2083,0.375,0.4583,0.5,0.6667,0.75,0.7917,0.9167,1]

Group331.children.append(OrientationInterpolator332)
OrientationInterpolator333 = x3d.OrientationInterpolator()
OrientationInterpolator333.DEF = "r_knee_RotationInterpolator_BasicDive"
OrientationInterpolator333.key = [0,0.125,0.2083,0.375,0.5,0.6667,0.9167,1]

Group331.children.append(OrientationInterpolator333)
OrientationInterpolator334 = x3d.OrientationInterpolator()
OrientationInterpolator334.DEF = "r_hip_RotationInterpolator_BasicDive"
OrientationInterpolator334.key = [0,0.125,0.2083,0.2917,0.5,0.7917,0.9167,1]

Group331.children.append(OrientationInterpolator334)
OrientationInterpolator335 = x3d.OrientationInterpolator()
OrientationInterpolator335.DEF = "l_ankle_RotationInterpolator_BasicDive"
OrientationInterpolator335.key = [0,0.125,0.2083,0.375,0.4583,0.5,0.6667,0.75,0.7917,0.9167,1]

Group331.children.append(OrientationInterpolator335)
OrientationInterpolator336 = x3d.OrientationInterpolator()
OrientationInterpolator336.DEF = "l_knee_RotationInterpolator_BasicDive"
OrientationInterpolator336.key = [0,0.2083,0.375,0.5,0.6667,0.7917,0.9167,1]

Group331.children.append(OrientationInterpolator336)
OrientationInterpolator337 = x3d.OrientationInterpolator()
OrientationInterpolator337.DEF = "l_hip_RotationInterpolator_BasicDive"
OrientationInterpolator337.key = [0,0.25,0.375,0.6667,0.7917,0.9167,1]

Group331.children.append(OrientationInterpolator337)
OrientationInterpolator338 = x3d.OrientationInterpolator()
OrientationInterpolator338.DEF = "lower_body_RotationInterpolator_BasicDive"
OrientationInterpolator338.key = [0,0.5,1]

Group331.children.append(OrientationInterpolator338)
#
OrientationInterpolator339 = x3d.OrientationInterpolator()
OrientationInterpolator339.DEF = "r_wrist_RotationInterpolator_BasicDive"
OrientationInterpolator339.key = [0,0.28,0.32,0.64,0.76,1]

Group331.children.append(OrientationInterpolator339)
OrientationInterpolator340 = x3d.OrientationInterpolator()
OrientationInterpolator340.DEF = "r_elbow_RotationInterpolator_BasicDive"
OrientationInterpolator340.key = [0,0.28,0.32,0.64,0.76,1]

Group331.children.append(OrientationInterpolator340)
OrientationInterpolator341 = x3d.OrientationInterpolator()
OrientationInterpolator341.DEF = "r_shoulder_RotationInterpolator_BasicDive"
OrientationInterpolator341.key = [0,0.45,0.64,0.76,0.88,1]

Group331.children.append(OrientationInterpolator341)
OrientationInterpolator342 = x3d.OrientationInterpolator()
OrientationInterpolator342.DEF = "l_wrist_RotationInterpolator_BasicDive"
OrientationInterpolator342.key = [0,0.32,0.64,0.88,1]

Group331.children.append(OrientationInterpolator342)
OrientationInterpolator343 = x3d.OrientationInterpolator()
OrientationInterpolator343.DEF = "l_elbow_RotationInterpolator_BasicDive"
OrientationInterpolator343.key = [0,0.28,0.32,0.64,0.76,1]

Group331.children.append(OrientationInterpolator343)
OrientationInterpolator344 = x3d.OrientationInterpolator()
OrientationInterpolator344.DEF = "l_shoulder_RotationInterpolator_BasicDive"
OrientationInterpolator344.key = [0,0.25,0.375,0.6667,0.7917,0.9167,1]

Group331.children.append(OrientationInterpolator344)
#
OrientationInterpolator345 = x3d.OrientationInterpolator()
OrientationInterpolator345.DEF = "head_RotationInterpolator_BasicDive"
OrientationInterpolator345.key = [0,0.28,0.3,0.32,0.4,0.45,0.6,0.65,0.7,0.75,0.85,0.9,0.95,1]

Group331.children.append(OrientationInterpolator345)
OrientationInterpolator346 = x3d.OrientationInterpolator()
OrientationInterpolator346.DEF = "neck_RotationInterpolator_BasicDive"
OrientationInterpolator346.key = [0,1]

Group331.children.append(OrientationInterpolator346)
OrientationInterpolator347 = x3d.OrientationInterpolator()
OrientationInterpolator347.DEF = "upper_body_RotationInterpolator_BasicDive"
OrientationInterpolator347.key = [0,0.2083,0.375,0.75,0.8333,1]

Group331.children.append(OrientationInterpolator347)
OrientationInterpolator348 = x3d.OrientationInterpolator()
OrientationInterpolator348.DEF = "whole_body_RotationInterpolator_BasicDive"
OrientationInterpolator348.key = [0,1]

Group331.children.append(OrientationInterpolator348)
PositionInterpolator349 = x3d.PositionInterpolator()
PositionInterpolator349.DEF = "whole_body_TranslationInterpolator_BasicDive"
PositionInterpolator349.key = [0,0.04167,0.125,0.1667,0.2083,0.25,0.2917,0.375,0.4583,0.5,0.5417,0.5833,0.625,0.7083,0.75,0.7917,0.875,0.9167,1]

Group331.children.append(PositionInterpolator349)
TimeSensor350 = x3d.TimeSensor()
TimeSensor350.DEF = "Dive_Time"
TimeSensor350.cycleInterval = 7
TimeSensor350.loop = True
TimeSensor350.startTime = -1

Group331.children.append(TimeSensor350)
ProximitySensor351 = x3d.ProximitySensor()
ProximitySensor351.DEF = "TriggerProximitySensor"
ProximitySensor351.size = [50,50,50]

Group331.children.append(ProximitySensor351)

Group330.children.append(Group331)

Scene15.children.append(Group330)
ROUTE352 = x3d.ROUTE()
ROUTE352.fromField = "enterTime"
ROUTE352.fromNode = "TriggerProximitySensor"
ROUTE352.toField = "startTime"
ROUTE352.toNode = "Dive_Time"

Scene15.children.append(ROUTE352)
ROUTE353 = x3d.ROUTE()
ROUTE353.fromField = "fraction_changed"
ROUTE353.fromNode = "Dive_Time"
ROUTE353.toField = "set_fraction"
ROUTE353.toNode = "r_ankle_RotationInterpolator_BasicDive"

Scene15.children.append(ROUTE353)
ROUTE354 = x3d.ROUTE()
ROUTE354.fromField = "fraction_changed"
ROUTE354.fromNode = "Dive_Time"
ROUTE354.toField = "set_fraction"
ROUTE354.toNode = "r_knee_RotationInterpolator_BasicDive"

Scene15.children.append(ROUTE354)
ROUTE355 = x3d.ROUTE()
ROUTE355.fromField = "fraction_changed"
ROUTE355.fromNode = "Dive_Time"
ROUTE355.toField = "set_fraction"
ROUTE355.toNode = "r_hip_RotationInterpolator_BasicDive"

Scene15.children.append(ROUTE355)
ROUTE356 = x3d.ROUTE()
ROUTE356.fromField = "fraction_changed"
ROUTE356.fromNode = "Dive_Time"
ROUTE356.toField = "set_fraction"
ROUTE356.toNode = "l_ankle_RotationInterpolator_BasicDive"

Scene15.children.append(ROUTE356)
ROUTE357 = x3d.ROUTE()
ROUTE357.fromField = "fraction_changed"
ROUTE357.fromNode = "Dive_Time"
ROUTE357.toField = "set_fraction"
ROUTE357.toNode = "l_knee_RotationInterpolator_BasicDive"

Scene15.children.append(ROUTE357)
ROUTE358 = x3d.ROUTE()
ROUTE358.fromField = "fraction_changed"
ROUTE358.fromNode = "Dive_Time"
ROUTE358.toField = "set_fraction"
ROUTE358.toNode = "l_hip_RotationInterpolator_BasicDive"

Scene15.children.append(ROUTE358)
ROUTE359 = x3d.ROUTE()
ROUTE359.fromField = "fraction_changed"
ROUTE359.fromNode = "Dive_Time"
ROUTE359.toField = "set_fraction"
ROUTE359.toNode = "lower_body_RotationInterpolator_BasicDive"

Scene15.children.append(ROUTE359)
ROUTE360 = x3d.ROUTE()
ROUTE360.fromField = "fraction_changed"
ROUTE360.fromNode = "Dive_Time"
ROUTE360.toField = "set_fraction"
ROUTE360.toNode = "head_RotationInterpolator_BasicDive"

Scene15.children.append(ROUTE360)
ROUTE361 = x3d.ROUTE()
ROUTE361.fromField = "fraction_changed"
ROUTE361.fromNode = "Dive_Time"
ROUTE361.toField = "set_fraction"
ROUTE361.toNode = "neck_RotationInterpolator_BasicDive"

Scene15.children.append(ROUTE361)
ROUTE362 = x3d.ROUTE()
ROUTE362.fromField = "fraction_changed"
ROUTE362.fromNode = "Dive_Time"
ROUTE362.toField = "set_fraction"
ROUTE362.toNode = "upper_body_RotationInterpolator_BasicDive"

Scene15.children.append(ROUTE362)
ROUTE363 = x3d.ROUTE()
ROUTE363.fromField = "fraction_changed"
ROUTE363.fromNode = "Dive_Time"
ROUTE363.toField = "set_fraction"
ROUTE363.toNode = "whole_body_RotationInterpolator_BasicDive"

Scene15.children.append(ROUTE363)
ROUTE364 = x3d.ROUTE()
ROUTE364.fromField = "fraction_changed"
ROUTE364.fromNode = "Dive_Time"
ROUTE364.toField = "set_fraction"
ROUTE364.toNode = "whole_body_TranslationInterpolator_BasicDive"

Scene15.children.append(ROUTE364)
ROUTE365 = x3d.ROUTE()
ROUTE365.fromField = "value_changed"
ROUTE365.fromNode = "r_ankle_RotationInterpolator_BasicDive"
ROUTE365.toField = "set_rotation"
ROUTE365.toNode = "hanim_r_ankle"

Scene15.children.append(ROUTE365)
ROUTE366 = x3d.ROUTE()
ROUTE366.fromField = "value_changed"
ROUTE366.fromNode = "r_knee_RotationInterpolator_BasicDive"
ROUTE366.toField = "set_rotation"
ROUTE366.toNode = "hanim_r_knee"

Scene15.children.append(ROUTE366)
ROUTE367 = x3d.ROUTE()
ROUTE367.fromField = "value_changed"
ROUTE367.fromNode = "r_hip_RotationInterpolator_BasicDive"
ROUTE367.toField = "set_rotation"
ROUTE367.toNode = "hanim_r_hip"

Scene15.children.append(ROUTE367)
ROUTE368 = x3d.ROUTE()
ROUTE368.fromField = "value_changed"
ROUTE368.fromNode = "l_ankle_RotationInterpolator_BasicDive"
ROUTE368.toField = "set_rotation"
ROUTE368.toNode = "hanim_l_ankle"

Scene15.children.append(ROUTE368)
ROUTE369 = x3d.ROUTE()
ROUTE369.fromField = "value_changed"
ROUTE369.fromNode = "l_knee_RotationInterpolator_BasicDive"
ROUTE369.toField = "set_rotation"
ROUTE369.toNode = "hanim_l_knee"

Scene15.children.append(ROUTE369)
ROUTE370 = x3d.ROUTE()
ROUTE370.fromField = "value_changed"
ROUTE370.fromNode = "l_hip_RotationInterpolator_BasicDive"
ROUTE370.toField = "set_rotationLeft"
ROUTE370.toNode = "finWarpScript"

Scene15.children.append(ROUTE370)
ROUTE371 = x3d.ROUTE()
ROUTE371.fromField = "value_changed"
ROUTE371.fromNode = "l_hip_RotationInterpolator_BasicDive"
ROUTE371.toField = "set_rotationRight"
ROUTE371.toNode = "finWarpScript"

Scene15.children.append(ROUTE371)
ROUTE372 = x3d.ROUTE()
ROUTE372.fromField = "value_changed"
ROUTE372.fromNode = "l_hip_RotationInterpolator_BasicDive"
ROUTE372.toField = "set_rotation"
ROUTE372.toNode = "hanim_l_hip"

Scene15.children.append(ROUTE372)
ROUTE373 = x3d.ROUTE()
ROUTE373.fromField = "value_changed"
ROUTE373.fromNode = "lower_body_RotationInterpolator_BasicDive"
ROUTE373.toField = "set_rotation"
ROUTE373.toNode = "hanim_sacroiliac"

Scene15.children.append(ROUTE373)
ROUTE374 = x3d.ROUTE()
ROUTE374.fromField = "value_changed"
ROUTE374.fromNode = "head_RotationInterpolator_BasicDive"
ROUTE374.toField = "set_rotation"
ROUTE374.toNode = "hanim_skullbase"

Scene15.children.append(ROUTE374)
ROUTE375 = x3d.ROUTE()
ROUTE375.fromField = "value_changed"
ROUTE375.fromNode = "neck_RotationInterpolator_BasicDive"
ROUTE375.toField = "set_rotation"
ROUTE375.toNode = "hanim_vc4"

Scene15.children.append(ROUTE375)
ROUTE376 = x3d.ROUTE()
ROUTE376.fromField = "value_changed"
ROUTE376.fromNode = "upper_body_RotationInterpolator_BasicDive"
ROUTE376.toField = "set_rotation"
ROUTE376.toNode = "hanim_vl1"

Scene15.children.append(ROUTE376)
ROUTE377 = x3d.ROUTE()
ROUTE377.fromField = "value_changed"
ROUTE377.fromNode = "whole_body_RotationInterpolator_BasicDive"
ROUTE377.toField = "set_rotation"
ROUTE377.toNode = "hanim_humanoid_root"

Scene15.children.append(ROUTE377)
ROUTE378 = x3d.ROUTE()
ROUTE378.fromField = "value_changed"
ROUTE378.fromNode = "whole_body_TranslationInterpolator_BasicDive"
ROUTE378.toField = "set_translation"
ROUTE378.toNode = "hanim_humanoid_root"

Scene15.children.append(ROUTE378)
ROUTE379 = x3d.ROUTE()
ROUTE379.fromField = "fraction_changed"
ROUTE379.fromNode = "Dive_Time"
ROUTE379.toField = "set_fraction"
ROUTE379.toNode = "r_wrist_RotationInterpolator_BasicDive"

Scene15.children.append(ROUTE379)
ROUTE380 = x3d.ROUTE()
ROUTE380.fromField = "fraction_changed"
ROUTE380.fromNode = "Dive_Time"
ROUTE380.toField = "set_fraction"
ROUTE380.toNode = "r_elbow_RotationInterpolator_BasicDive"

Scene15.children.append(ROUTE380)
ROUTE381 = x3d.ROUTE()
ROUTE381.fromField = "fraction_changed"
ROUTE381.fromNode = "Dive_Time"
ROUTE381.toField = "set_fraction"
ROUTE381.toNode = "r_shoulder_RotationInterpolator_BasicDive"

Scene15.children.append(ROUTE381)
ROUTE382 = x3d.ROUTE()
ROUTE382.fromField = "fraction_changed"
ROUTE382.fromNode = "Dive_Time"
ROUTE382.toField = "set_fraction"
ROUTE382.toNode = "l_wrist_RotationInterpolator_BasicDive"

Scene15.children.append(ROUTE382)
ROUTE383 = x3d.ROUTE()
ROUTE383.fromField = "fraction_changed"
ROUTE383.fromNode = "Dive_Time"
ROUTE383.toField = "set_fraction"
ROUTE383.toNode = "l_elbow_RotationInterpolator_BasicDive"

Scene15.children.append(ROUTE383)
ROUTE384 = x3d.ROUTE()
ROUTE384.fromField = "fraction_changed"
ROUTE384.fromNode = "Dive_Time"
ROUTE384.toField = "set_fraction"
ROUTE384.toNode = "l_shoulder_RotationInterpolator_BasicDive"

Scene15.children.append(ROUTE384)
ROUTE385 = x3d.ROUTE()
ROUTE385.fromField = "value_changed"
ROUTE385.fromNode = "r_wrist_RotationInterpolator_BasicDive"
ROUTE385.toField = "set_rotation"
ROUTE385.toNode = "hanim_r_wrist"

Scene15.children.append(ROUTE385)
ROUTE386 = x3d.ROUTE()
ROUTE386.fromField = "value_changed"
ROUTE386.fromNode = "r_elbow_RotationInterpolator_BasicDive"
ROUTE386.toField = "set_rotation"
ROUTE386.toNode = "hanim_r_elbow"

Scene15.children.append(ROUTE386)
ROUTE387 = x3d.ROUTE()
ROUTE387.fromField = "value_changed"
ROUTE387.fromNode = "r_shoulder_RotationInterpolator_BasicDive"
ROUTE387.toField = "set_rotation"
ROUTE387.toNode = "hanim_r_shoulder"

Scene15.children.append(ROUTE387)
ROUTE388 = x3d.ROUTE()
ROUTE388.fromField = "value_changed"
ROUTE388.fromNode = "l_wrist_RotationInterpolator_BasicDive"
ROUTE388.toField = "set_rotation"
ROUTE388.toNode = "hanim_l_wrist"

Scene15.children.append(ROUTE388)
ROUTE389 = x3d.ROUTE()
ROUTE389.fromField = "value_changed"
ROUTE389.fromNode = "l_elbow_RotationInterpolator_BasicDive"
ROUTE389.toField = "set_rotation"
ROUTE389.toNode = "hanim_l_elbow"

Scene15.children.append(ROUTE389)
ROUTE390 = x3d.ROUTE()
ROUTE390.fromField = "value_changed"
ROUTE390.fromNode = "l_shoulder_RotationInterpolator_BasicDive"
ROUTE390.toField = "set_rotation"
ROUTE390.toNode = "hanim_l_shoulder"

Scene15.children.append(ROUTE390)

X3D0.Scene = Scene15
f = open("././NancyDiving_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
