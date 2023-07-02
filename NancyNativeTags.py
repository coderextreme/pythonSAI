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
meta3.content = "NancyNativeTags.x3d"

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.name = "creator"
meta4.content = "Cindy Ballreich"

head1.children.append(meta4)
meta5 = x3d.meta()
meta5.name = "translators"
meta5.content = "Tom Miller and Don Brutzman, NPS"

head1.children.append(meta5)
meta6 = x3d.meta()
meta6.name = "created"
meta6.content = "9 July 2000"

head1.children.append(meta6)
meta7 = x3d.meta()
meta7.name = "modified"
meta7.content = "4 July 2020"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.name = "info"
meta8.content = "need height, weight. not sure if we should ask a lady her age."

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "description"
meta9.content = "Canonical HAnim 1.1 specification example, using native X3D tags instead of ProtoDeclaration/ExternProtoDeclaration and ProtoInstance."

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "identifier"
meta10.content = "https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Legacy/NancyNativeTags.x3d"

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.name = "generator"
meta11.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"

head1.children.append(meta11)
meta12 = x3d.meta()
meta12.name = "license"
meta12.content = "../license.html"

head1.children.append(meta12)

X3D0.head = head1
Scene13 = x3d.Scene()
HAnimHumanoid14 = x3d.HAnimHumanoid()
HAnimHumanoid14.name = "Nancy"
HAnimHumanoid14.DEF = "hanim_Nancy"
HAnimHumanoid14.info = ["humanoidVersion=Nancy V1.2b","authorEmail=cindy@ballreich.net","authorName=Cindy Ballreich","copyright=1997 3Name3D / Yglesias Wallock Divekar Inc. all rights reserved.","creationDate=Tue Dec 30 08:30:08 PST 1997","gender=female","usageRestrictions=Noncommercial usage is ok if 3Name3D name and logo http://www.ballreich.net/vrml/HAnim/small_logo.gif is present and proper credit is given."]
HAnimHumanoid14.version = "2.0"
HAnimJoint15 = x3d.HAnimJoint()
HAnimJoint15.name = "humanoid_root"
HAnimJoint15.DEF = "hanim_humanoid_root"
HAnimJoint15.center = [-0.00405,0.855,-0.000113]
HAnimJoint15.ulimit = [0,0,0]
HAnimJoint15.llimit = [0,0,0]
HAnimJoint16 = x3d.HAnimJoint()
HAnimJoint16.name = "sacroiliac"
HAnimJoint16.DEF = "hanim_sacroiliac"
HAnimJoint16.center = [0,1.01,-0.0204]
HAnimJoint16.ulimit = [0,0,0]
HAnimJoint16.llimit = [0,0,0]
HAnimSegment17 = x3d.HAnimSegment()
HAnimSegment17.name = "pelvis"
HAnimSegment17.DEF = "hanim_pelvis"
Shape18 = x3d.Shape()
Appearance19 = x3d.Appearance()
Material20 = x3d.Material()
Material20.DEF = "Pants_Color"
Material20.ambientIntensity = 0.25
Material20.diffuseColor = [0.054,0.233,0.39]

Appearance19.material = Material20

Shape18.appearance = Appearance19
IndexedFaceSet21 = x3d.IndexedFaceSet()
IndexedFaceSet21.coordIndex = [0,1,40,-1,1,2,40,-1,2,3,40,-1,3,4,40,-1,4,5,40,-1,5,4,9,-1,4,3,8,-1,3,2,8,-1,2,1,6,-1,0,7,1,-1,7,6,1,-1,6,8,2,-1,9,4,10,-1,4,8,10,-1,8,6,12,-1,7,0,47,-1,50,5,9,-1,7,47,55,-1,55,13,7,-1,50,9,56,-1,9,10,14,-1,10,11,15,-1,11,12,16,-1,12,13,19,-1,13,55,17,-1,60,17,55,-1,17,19,13,-1,19,16,12,-1,16,15,11,-1,15,18,10,-1,14,56,9,-1,56,14,64,-1,17,60,20,-1,20,19,17,-1,21,64,14,-1,14,22,21,-1,15,16,24,-1,16,19,24,-1,19,20,26,-1,24,23,15,-1,64,21,69,-1,21,22,29,-1,19,26,25,-1,20,63,27,-1,27,26,20,-1,25,24,19,-1,30,29,22,-1,29,28,21,-1,28,69,21,-1,27,34,26,-1,69,28,79,-1,29,30,32,-1,30,23,33,-1,23,24,37,-1,25,26,34,-1,83,27,77,-1,37,33,23,-1,33,32,30,-1,31,79,28,-1,79,31,84,-1,32,33,36,-1,24,25,37,-1,34,27,83,-1,83,38,34,-1,34,37,25,-1,37,36,33,-1,36,35,32,-1,84,31,89,-1,31,35,89,-1,35,36,39,-1,36,37,39,-1,38,83,89,-1,89,39,38,-1,39,89,35,-1,40,41,0,-1,40,42,41,-1,40,43,42,-1,40,44,43,-1,40,45,44,-1,49,44,45,-1,48,43,44,-1,48,42,43,-1,46,41,42,-1,41,47,0,-1,41,46,47,-1,42,48,46,-1,51,44,49,-1,51,48,44,-1,48,52,53,-1,49,45,50,-1,56,49,50,-1,57,51,49,-1,58,53,52,-1,59,54,53,-1,62,55,54,-1,55,62,60,-1,54,59,62,-1,53,58,59,-1,51,61,58,-1,49,56,57,-1,64,57,56,-1,67,59,58,-1,68,62,59,-1,60,63,20,-1,60,62,63,-1,59,67,68,-1,58,61,67,-1,57,64,65,-1,65,66,57,-1,71,63,62,-1,69,65,64,-1,74,66,65,-1,78,68,67,-1,70,71,62,-1,63,72,27,-1,63,71,72,-1,68,78,76,-1,67,75,78,-1,66,74,75,-1,65,73,74,-1,65,69,73,-1,77,27,72,-1,71,82,72,-1,79,73,69,-1,81,75,74,-1,82,71,70,-1,77,72,83,-1,73,79,80,-1,84,80,79,-1,86,75,81,-1,83,72,82,-1,82,88,83,-1,70,87,82,-1,81,85,86,-1,89,80,84,-1,89,85,80,-1,90,86,85,-1,90,87,86,-1,89,83,88,-1,88,90,89,-1,85,89,90,-1,50,45,5,-1,45,40,5,-1,10,8,11,-1,8,12,11,-1,18,22,10,-1,22,14,10,-1,57,66,51,-1,66,61,51,-1,51,58,48,-1,58,52,48,-1,48,53,46,-1,53,54,46,-1,76,70,68,-1,70,62,68,-1,29,32,28,-1,28,32,31,-1,32,35,31,-1,85,81,80,-1,81,73,80,-1,81,74,73,-1,39,37,38,-1,37,34,38,-1,82,87,88,-1,87,90,88,-1,87,78,86,-1,78,75,86,-1,61,66,67,-1,66,75,67,-1,22,18,15,-1,23,30,15,-1,30,22,15,-1,13,12,7,-1,12,6,7,-1,46,54,47,-1,54,55,47,-1,87,76,78,-1,87,70,76,-1]
IndexedFaceSet21.creaseAngle = 1.14
Coordinate22 = x3d.Coordinate()

IndexedFaceSet21.coord = Coordinate22

Shape18.geometry = IndexedFaceSet21

HAnimSegment17.children.append(Shape18)

HAnimJoint16.children.append(HAnimSegment17)
HAnimJoint23 = x3d.HAnimJoint()
HAnimJoint23.name = "l_hip"
HAnimJoint23.DEF = "hanim_l_hip"
HAnimJoint23.center = [0.122,0.888271,-0.0693267]
HAnimJoint23.ulimit = [0,0,0]
HAnimJoint23.llimit = [0,0,0]
HAnimSegment24 = x3d.HAnimSegment()
HAnimSegment24.name = "l_thigh"
HAnimSegment24.DEF = "hanim_l_thigh"
Shape25 = x3d.Shape()
Appearance26 = x3d.Appearance()
Material27 = x3d.Material()
Material27.USE = "Pants_Color"

Appearance26.material = Material27

Shape25.appearance = Appearance26
IndexedFaceSet28 = x3d.IndexedFaceSet()
IndexedFaceSet28.coordIndex = [0,4,5,-1,3,4,0,-1,0,7,1,-1,0,8,7,-1,0,6,8,-1,0,5,6,-1,0,2,3,-1,0,1,2,-1,9,2,1,-1,10,3,2,-1,11,4,3,-1,12,5,4,-1,13,6,5,-1,15,7,8,-1,9,1,7,-1,7,15,9,-1,8,14,15,-1,5,16,13,-1,5,12,16,-1,4,11,12,-1,3,10,11,-1,2,9,10,-1,20,13,16,-1,18,11,10,-1,19,12,11,-1,20,16,12,-1,23,15,14,-1,15,23,24,-1,12,19,20,-1,11,18,19,-1,10,17,18,-1,26,18,17,-1,27,19,18,-1,27,20,19,-1,28,21,20,-1,29,23,22,-1,23,29,30,-1,20,32,28,-1,20,27,32,-1,18,26,27,-1,17,25,26,-1,25,31,30,-1,30,29,26,-1,30,26,25,-1,29,28,27,-1,29,27,26,-1,28,32,27,-1,22,23,14,-1,20,21,13,-1,21,22,13,-1,22,14,13,-1,9,15,24,-1,10,9,17,-1,9,24,17,-1,6,13,8,-1,13,14,8,-1,28,29,21,-1,29,22,21,-1,24,31,17,-1,31,25,17,-1,30,31,23,-1,31,24,23,-1]
IndexedFaceSet28.creaseAngle = 1.32
Coordinate29 = x3d.Coordinate()

IndexedFaceSet28.coord = Coordinate29

Shape25.geometry = IndexedFaceSet28

HAnimSegment24.children.append(Shape25)

HAnimJoint23.children.append(HAnimSegment24)
HAnimJoint30 = x3d.HAnimJoint()
HAnimJoint30.name = "l_knee"
HAnimJoint30.DEF = "hanim_l_knee"
HAnimJoint30.center = [0.0738,0.517,-0.0284]
HAnimJoint30.ulimit = [0,0,0]
HAnimJoint30.llimit = [0,0,0]
HAnimSegment31 = x3d.HAnimSegment()
HAnimSegment31.name = "l_calf"
HAnimSegment31.DEF = "hanim_l_calf"
Shape32 = x3d.Shape()
Appearance33 = x3d.Appearance()
Material34 = x3d.Material()
Material34.USE = "Pants_Color"

Appearance33.material = Material34

Shape32.appearance = Appearance33
IndexedFaceSet35 = x3d.IndexedFaceSet()
IndexedFaceSet35.coordIndex = [2,1,0,-1,2,3,1,-1,2,4,3,-1,2,5,4,-1,2,6,5,-1,2,7,6,-1,2,8,7,-1,2,0,8,-1,9,8,0,-1,10,6,7,-1,11,5,6,-1,12,4,5,-1,12,3,4,-1,13,1,3,-1,1,13,14,-1,3,12,13,-1,5,11,12,-1,6,10,11,-1,8,9,15,-1,22,13,12,-1,13,22,14,-1,17,15,9,-1,20,12,11,-1,21,22,12,-1,23,9,14,-1,9,23,16,-1,14,22,23,-1,12,20,21,-1,15,17,18,-1,9,16,17,-1,24,17,16,-1,25,18,17,-1,26,19,18,-1,27,20,19,-1,28,21,20,-1,29,22,21,-1,30,23,22,-1,31,16,23,-1,23,30,31,-1,22,29,30,-1,21,28,29,-1,20,27,28,-1,19,26,27,-1,18,25,26,-1,17,24,25,-1,16,31,24,-1,33,26,25,-1,36,29,28,-1,37,31,30,-1,29,36,30,-1,25,24,33,-1,31,37,24,-1,32,33,24,-1,24,37,32,-1,38,37,30,-1,30,36,38,-1,41,33,32,-1,42,39,34,-1,44,36,35,-1,45,38,36,-1,46,37,38,-1,38,45,46,-1,36,44,45,-1,35,43,44,-1,39,42,47,-1,32,40,41,-1,40,46,45,-1,41,40,45,-1,41,45,44,-1,44,43,42,-1,44,42,41,-1,43,47,42,-1,39,35,28,-1,35,36,28,-1,34,39,27,-1,39,28,27,-1,33,34,26,-1,34,27,26,-1,33,41,34,-1,41,42,34,-1,40,32,46,-1,32,37,46,-1,10,19,11,-1,19,20,11,-1,14,9,1,-1,9,0,1,-1,8,15,7,-1,7,15,10,-1,15,19,10,-1,15,18,19,-1,43,35,47,-1,35,39,47,-1]
IndexedFaceSet35.creaseAngle = 1.57
Coordinate36 = x3d.Coordinate()

IndexedFaceSet35.coord = Coordinate36

Shape32.geometry = IndexedFaceSet35

HAnimSegment31.children.append(Shape32)

HAnimJoint30.children.append(HAnimSegment31)
HAnimJoint37 = x3d.HAnimJoint()
HAnimJoint37.name = "l_ankle"
HAnimJoint37.DEF = "hanim_l_ankle"
HAnimJoint37.center = [0.0645,0.0719,-0.048]
HAnimJoint37.ulimit = [0,0,0]
HAnimJoint37.llimit = [0,0,0]
HAnimSegment38 = x3d.HAnimSegment()
HAnimSegment38.name = "l_hindfoot"
HAnimSegment38.DEF = "hanim_l_hindfoot"
Shape39 = x3d.Shape()
Appearance40 = x3d.Appearance()
Material41 = x3d.Material()
Material41.DEF = "Shoe_Color"
Material41.ambientIntensity = 0.25

Appearance40.material = Material41

Shape39.appearance = Appearance40
IndexedFaceSet42 = x3d.IndexedFaceSet()
IndexedFaceSet42.coordIndex = [2,1,0,-1,4,3,1,-1,2,4,1,-1,3,6,5,-1,1,3,5,-1,6,8,7,-1,5,6,7,-1,8,10,9,-1,7,8,9,-1,10,12,11,-1,9,10,11,-1,12,14,13,-1,11,12,13,-1,14,16,15,-1,13,14,15,-1,16,18,17,-1,15,16,17,-1,18,20,19,-1,17,18,19,-1,20,22,21,-1,19,20,21,-1,22,24,23,-1,21,22,23,-1,24,25,0,-1,23,24,0,-1,25,4,2,-1,0,25,2,-1,18,26,20,-1,16,26,18,-1,27,26,16,-1,14,27,16,-1,12,27,14,-1,28,27,12,-1,29,28,12,-1,10,29,12,-1,8,29,10,-1,6,37,8,-1,24,30,25,-1,31,30,24,-1,22,31,24,-1,32,31,22,-1,20,32,22,-1,33,32,20,-1,26,33,20,-1,34,33,26,-1,27,34,26,-1,35,34,27,-1,28,35,27,-1,29,35,28,-1,36,35,29,-1,8,36,29,-1,37,36,8,-1,6,38,37,-1,3,38,6,-1,39,38,3,-1,30,39,25,-1,41,40,30,-1,31,41,30,-1,42,41,31,-1,32,42,31,-1,43,42,32,-1,33,43,32,-1,44,43,33,-1,34,44,33,-1,45,44,34,-1,35,45,34,-1,46,45,35,-1,36,46,35,-1,47,46,36,-1,37,47,36,-1,38,47,37,-1,48,47,38,-1,49,48,38,-1,39,49,38,-1,40,49,39,-1,30,40,39,-1,48,49,50,-1,47,48,50,-1,46,47,50,-1,45,46,50,-1,44,45,50,-1,43,44,50,-1,42,43,50,-1,41,42,50,-1,40,41,50,-1,49,40,50,-1,11,13,15,-1,11,15,17,-1,9,11,17,-1,9,17,19,-1,7,9,19,-1,7,19,21,-1,5,7,21,-1,5,21,23,-1,5,23,0,-1,1,5,0,-1,3,4,39,-1,4,25,39,-1]
IndexedFaceSet42.creaseAngle = 1.57
Coordinate43 = x3d.Coordinate()

IndexedFaceSet42.coord = Coordinate43

Shape39.geometry = IndexedFaceSet42

HAnimSegment38.children.append(Shape39)

HAnimJoint37.children.append(HAnimSegment38)

HAnimJoint30.children.append(HAnimJoint37)

HAnimJoint23.children.append(HAnimJoint30)

HAnimJoint16.children.append(HAnimJoint23)
HAnimJoint44 = x3d.HAnimJoint()
HAnimJoint44.name = "r_hip"
HAnimJoint44.DEF = "hanim_r_hip"
HAnimJoint44.center = [-0.11,0.892362,-0.0732533]
HAnimJoint44.ulimit = [0,0,0]
HAnimJoint44.llimit = [0,0,0]
HAnimSegment45 = x3d.HAnimSegment()
HAnimSegment45.name = "r_thigh"
HAnimSegment45.DEF = "hanim_r_thigh"
Shape46 = x3d.Shape()
Appearance47 = x3d.Appearance()
Material48 = x3d.Material()
Material48.USE = "Pants_Color"

Appearance47.material = Material48

Shape46.appearance = Appearance47
IndexedFaceSet49 = x3d.IndexedFaceSet()
IndexedFaceSet49.coordIndex = [5,4,0,-1,0,4,3,-1,1,7,0,-1,7,8,0,-1,8,6,0,-1,6,5,0,-1,3,2,0,-1,2,1,0,-1,1,2,9,-1,2,3,10,-1,3,4,11,-1,4,5,12,-1,5,6,13,-1,8,7,15,-1,7,1,9,-1,9,15,7,-1,15,14,8,-1,13,16,5,-1,16,12,5,-1,12,11,4,-1,11,10,3,-1,10,9,2,-1,12,16,20,-1,13,14,22,-1,14,15,23,-1,24,23,15,-1,23,22,14,-1,20,19,12,-1,17,18,26,-1,18,19,27,-1,19,20,27,-1,20,21,28,-1,22,23,29,-1,30,29,23,-1,27,26,18,-1,26,25,17,-1,30,31,25,-1,25,26,29,-1,25,29,30,-1,26,27,28,-1,26,28,29,-1,27,20,28,-1,24,15,9,-1,22,21,13,-1,29,28,22,-1,28,21,22,-1,24,31,23,-1,31,30,23,-1,25,31,17,-1,31,24,17,-1,17,24,10,-1,24,9,10,-1,18,10,11,-1,18,17,10,-1,18,12,19,-1,18,11,12,-1,21,20,13,-1,20,16,13,-1,14,13,8,-1,13,6,8,-1]
IndexedFaceSet49.creaseAngle = 1.61
Coordinate50 = x3d.Coordinate()

IndexedFaceSet49.coord = Coordinate50

Shape46.geometry = IndexedFaceSet49

HAnimSegment45.children.append(Shape46)

HAnimJoint44.children.append(HAnimSegment45)
HAnimJoint51 = x3d.HAnimJoint()
HAnimJoint51.name = "r_knee"
HAnimJoint51.DEF = "hanim_r_knee"
HAnimJoint51.center = [-0.0699,0.51,-0.0166]
HAnimJoint51.ulimit = [0,0,0]
HAnimJoint51.llimit = [0,0,0]
HAnimSegment52 = x3d.HAnimSegment()
HAnimSegment52.name = "r_calf"
HAnimSegment52.DEF = "hanim_r_calf"
Shape53 = x3d.Shape()
Appearance54 = x3d.Appearance()
Material55 = x3d.Material()
Material55.USE = "Pants_Color"

Appearance54.material = Material55

Shape53.appearance = Appearance54
IndexedFaceSet56 = x3d.IndexedFaceSet()
IndexedFaceSet56.coordIndex = [14,25,18,-1,25,32,18,-1,32,27,18,-1,27,22,18,-1,22,10,18,-1,10,6,18,-1,6,8,18,-1,8,14,18,-1,14,8,17,-1,6,10,9,-1,10,22,24,-1,22,27,39,-1,27,32,39,-1,32,25,42,-1,25,14,30,-1,17,30,14,-1,30,42,25,-1,42,39,32,-1,39,24,22,-1,24,9,10,-1,4,17,8,-1,39,42,43,-1,30,43,42,-1,17,4,1,-1,24,39,26,-1,39,43,44,-1,30,17,34,-1,16,34,17,-1,34,43,30,-1,44,26,39,-1,0,1,4,-1,1,16,17,-1,16,1,3,-1,1,0,2,-1,0,5,7,-1,5,26,28,-1,26,44,45,-1,44,43,46,-1,43,34,36,-1,34,16,15,-1,15,36,34,-1,36,46,43,-1,46,45,44,-1,45,28,26,-1,28,7,5,-1,7,2,0,-1,2,3,1,-1,3,15,16,-1,45,46,37,-1,36,15,20,-1,36,37,46,-1,13,2,7,-1,3,20,15,-1,3,2,13,-1,36,20,29,-1,29,37,36,-1,13,21,23,-1,21,33,23,-1,41,37,40,-1,37,29,31,-1,29,20,19,-1,19,31,29,-1,31,40,37,-1,40,38,41,-1,35,23,33,-1,23,12,13,-1,12,11,13,-1,31,19,11,-1,40,31,11,-1,40,11,12,-1,12,23,38,-1,12,38,40,-1,23,35,38,-1,28,21,7,-1,21,13,7,-1,45,33,28,-1,33,21,28,-1,33,45,41,-1,45,37,41,-1,33,41,35,-1,41,38,35,-1,20,3,47,-1,11,19,47,-1,19,20,47,-1,13,47,3,-1,13,11,47,-1,4,8,6,-1,26,5,24,-1,5,9,24,-1,6,9,4,-1,9,0,4,-1,9,5,0,-1]
IndexedFaceSet56.creaseAngle = 1.57
Coordinate57 = x3d.Coordinate()

IndexedFaceSet56.coord = Coordinate57

Shape53.geometry = IndexedFaceSet56

HAnimSegment52.children.append(Shape53)

HAnimJoint51.children.append(HAnimSegment52)
HAnimJoint58 = x3d.HAnimJoint()
HAnimJoint58.name = "r_ankle"
HAnimJoint58.DEF = "hanim_r_ankle"
HAnimJoint58.center = [-0.064,0.0753,-0.0412]
HAnimJoint58.ulimit = [0,0,0]
HAnimJoint58.llimit = [0,0,0]
HAnimSegment59 = x3d.HAnimSegment()
HAnimSegment59.name = "r_hindfoot"
HAnimSegment59.DEF = "hanim_r_hindfoot"
Shape60 = x3d.Shape()
Appearance61 = x3d.Appearance()
Material62 = x3d.Material()
Material62.USE = "Shoe_Color"

Appearance61.material = Material62

Shape60.appearance = Appearance61
IndexedFaceSet63 = x3d.IndexedFaceSet()
IndexedFaceSet63.coordIndex = [6,50,0,-1,50,8,7,-1,50,7,0,-1,1,9,8,-1,1,8,50,-1,49,10,9,-1,49,9,1,-1,46,11,10,-1,46,10,49,-1,2,12,11,-1,2,11,46,-1,3,13,12,-1,3,12,2,-1,4,14,13,-1,4,13,3,-1,45,14,4,-1,47,15,45,-1,19,15,47,-1,48,18,19,-1,5,16,18,-1,5,18,48,-1,6,17,16,-1,6,16,5,-1,0,7,17,-1,0,17,6,-1,14,20,21,-1,14,21,13,-1,13,21,12,-1,12,21,22,-1,12,22,11,-1,11,22,10,-1,17,23,16,-1,16,23,24,-1,16,24,18,-1,18,24,25,-1,18,25,19,-1,19,25,26,-1,19,26,15,-1,15,26,20,-1,20,26,27,-1,20,27,21,-1,21,27,28,-1,21,28,22,-1,22,28,29,-1,10,30,9,-1,9,30,31,-1,9,31,8,-1,8,31,32,-1,17,32,23,-1,23,33,34,-1,23,34,35,-1,23,35,24,-1,24,35,36,-1,24,36,25,-1,25,36,37,-1,25,37,26,-1,26,37,38,-1,26,38,27,-1,27,38,39,-1,27,39,28,-1,28,39,40,-1,28,40,29,-1,29,40,41,-1,29,41,30,-1,30,41,42,-1,30,42,31,-1,31,42,43,-1,31,43,32,-1,32,43,33,-1,32,33,23,-1,44,43,42,-1,44,42,41,-1,44,41,40,-1,44,40,39,-1,44,39,38,-1,44,38,37,-1,44,37,36,-1,44,36,35,-1,44,35,34,-1,44,34,33,-1,44,33,43,-1,4,3,2,-1,45,4,2,-1,45,2,46,-1,47,45,46,-1,48,46,49,-1,5,48,49,-1,5,49,1,-1,6,5,1,-1,6,1,50,-1,30,10,29,-1,10,22,29,-1,17,7,32,-1,7,8,32,-1,19,47,48,-1,47,46,48,-1,20,14,15,-1,14,45,15,-1]
IndexedFaceSet63.creaseAngle = 1.57
Coordinate64 = x3d.Coordinate()

IndexedFaceSet63.coord = Coordinate64

Shape60.geometry = IndexedFaceSet63

HAnimSegment59.children.append(Shape60)

HAnimJoint58.children.append(HAnimSegment59)

HAnimJoint51.children.append(HAnimJoint58)

HAnimJoint44.children.append(HAnimJoint51)

HAnimJoint16.children.append(HAnimJoint44)

HAnimJoint15.children.append(HAnimJoint16)
HAnimJoint65 = x3d.HAnimJoint()
HAnimJoint65.name = "vl1"
HAnimJoint65.DEF = "hanim_vl1"
HAnimJoint65.center = [-0.00405,1.07,-0.0275]
HAnimJoint65.ulimit = [0,0,0]
HAnimJoint65.llimit = [0,0,0]
HAnimSegment66 = x3d.HAnimSegment()
HAnimSegment66.name = "l1"
HAnimSegment66.DEF = "hanim_l1"
Shape67 = x3d.Shape()
Appearance68 = x3d.Appearance()
Material69 = x3d.Material()
Material69.DEF = "Shirt_Color"
Material69.ambientIntensity = 0.25
Material69.diffuseColor = [0.6,0.0745,0.1137]

Appearance68.material = Material69
ImageTexture70 = x3d.ImageTexture()
ImageTexture70.DEF = "small_logo_Tex"
ImageTexture70.url = ["small_logo.gif","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Legacy/small_logo.gif"]

Appearance68.texture = ImageTexture70

Shape67.appearance = Appearance68
IndexedFaceSet71 = x3d.IndexedFaceSet()
IndexedFaceSet71.coordIndex = [0,1,2,-1,3,0,2,-1,4,5,6,-1,6,7,4,-1,8,7,6,-1,6,9,8,-1,9,10,8,-1,6,5,11,-1,9,6,12,-1,11,12,6,-1,12,10,9,-1,7,8,13,-1,13,4,7,-1,14,15,16,-1,15,17,13,-1,4,13,17,-1,17,15,18,-1,13,19,15,-1,19,13,8,-1,19,16,15,-1,16,19,8,-1,17,20,4,-1,5,4,20,-1,18,21,17,-1,20,17,21,-1,16,22,14,-1,22,16,23,-1,8,23,16,-1,23,8,10,-1,24,25,26,-1,26,27,24,-1,25,28,26,-1,28,29,30,-1,30,26,28,-1,31,32,33,-1,32,25,33,-1,25,24,34,-1,33,25,34,-1,24,35,34,-1,27,35,24,-1,33,36,31,-1,27,26,37,-1,37,26,30,-1,38,37,30,-1,33,34,39,-1,39,34,35,-1,39,35,40,-1,41,38,30,-1,35,27,42,-1,37,42,27,-1,40,35,42,-1,42,37,43,-1,37,38,44,-1,44,43,37,-1,36,45,46,-1,36,33,45,-1,40,42,47,-1,43,47,42,-1,47,48,40,-1,39,40,48,-1,47,43,49,-1,43,44,49,-1,50,49,44,-1,51,46,52,-1,46,45,52,-1,52,45,53,-1,33,53,45,-1,33,39,53,-1,49,54,47,-1,48,47,54,-1,55,56,52,-1,57,52,53,-1,57,55,52,-1,58,57,53,-1,59,58,53,-1,53,39,59,-1,39,48,59,-1,59,48,54,-1,58,59,60,-1,54,49,61,-1,59,54,61,-1,60,59,61,-1,49,50,62,-1,63,62,50,-1,62,61,49,-1,64,63,50,-1,63,64,65,-1,65,62,63,-1,66,60,61,-1,62,65,67,-1,68,67,65,-1,64,69,70,-1,64,70,65,-1,70,68,65,-1,69,71,72,-1,72,70,69,-1,73,74,75,-1,66,76,60,-1,67,77,62,-1,62,77,61,-1,77,66,61,-1,66,77,78,-1,77,67,79,-1,79,67,68,-1,79,78,77,-1,68,70,80,-1,70,72,80,-1,80,79,68,-1,74,73,81,-1,73,76,82,-1,82,81,73,-1,76,66,83,-1,78,83,66,-1,83,82,76,-1,78,79,84,-1,79,80,84,-1,84,85,78,-1,86,84,80,-1,81,82,87,-1,87,88,81,-1,82,83,89,-1,83,78,89,-1,89,87,82,-1,78,85,89,-1,90,91,92,-1,92,93,90,-1,90,94,91,-1,95,96,94,-1,94,90,95,-1,29,96,97,-1,96,95,97,-1,97,30,29,-1,30,97,41,-1,41,97,95,-1,98,99,100,-1,98,91,99,-1,101,92,91,-1,98,101,91,-1,101,102,92,-1,92,102,93,-1,36,103,31,-1,51,103,36,46,-1,103,100,31,-1,100,103,98,-1,104,90,93,-1,90,104,95,-1,95,105,41,-1,104,105,95,-1,106,101,98,-1,102,101,106,-1,107,93,102,-1,93,107,104,-1,108,104,107,-1,107,109,108,-1,110,105,104,-1,104,108,110,-1,109,107,111,-1,107,102,111,-1,111,102,106,-1,111,112,109,-1,106,112,111,-1,113,110,108,-1,110,113,114,-1,51,52,115,-1,116,115,117,-1,117,106,116,-1,118,109,112,-1,119,108,109,-1,108,119,113,-1,109,118,119,-1,120,113,119,-1,119,121,120,-1,52,56,122,-1,122,115,52,-1,115,122,123,-1,117,124,125,-1,106,117,125,-1,118,112,106,125,-1,119,118,125,-1,121,119,125,-1,126,124,123,-1,127,114,113,-1,114,127,128,-1,113,120,127,-1,114,128,129,-1,130,126,123,-1,122,130,123,-1,131,120,121,-1,131,127,120,-1,132,129,128,-1,128,127,132,-1,74,81,133,-1,81,134,133,-1,121,135,131,-1,136,132,127,-1,132,136,137,-1,138,71,129,-1,138,129,132,-1,137,138,132,-1,139,72,71,-1,72,139,80,-1,71,138,139,-1,140,135,121,-1,140,121,125,-1,141,127,131,-1,127,141,136,-1,131,135,141,-1,142,141,135,-1,143,136,141,-1,136,143,137,-1,141,142,143,-1,144,138,137,-1,144,139,138,-1,143,144,137,-1,145,146,134,-1,145,140,146,-1,134,81,145,-1,147,135,140,-1,135,147,142,-1,140,145,147,-1,148,80,139,-1,80,148,86,-1,139,144,148,-1,149,143,142,-1,149,144,143,-1,142,150,149,-1,151,148,144,-1,144,149,151,-1,152,145,81,-1,81,88,152,-1,153,147,145,-1,153,142,147,-1,145,152,153,-1,153,150,142,-1,154,86,148,-1,148,151,154,-1,155,28,25,-1,155,29,28,-1,155,25,32,-1,155,32,31,-1,155,31,100,-1,155,100,99,-1,155,99,91,-1,155,91,94,-1,155,94,96,-1,155,96,29,-1,156,151,149,-1,156,154,151,-1,156,149,150,-1,156,150,153,-1,156,153,152,-1,156,152,88,-1,156,88,87,-1,156,87,89,-1,156,89,85,-1,156,85,84,-1,156,84,86,-1,156,86,154,-1,76,157,60,-1,76,73,158,157,-1,159,158,73,75,160,-1,161,56,55,-1,60,162,58,-1,162,60,157,-1,161,55,163,-1,57,164,163,55,-1,160,163,164,-1,160,164,159,-1,164,57,165,-1,164,165,159,-1,57,58,166,165,-1,166,58,162,-1,165,166,159,-1,166,162,157,158,159,-1,140,125,167,-1,124,168,125,-1,168,167,125,-1,124,169,168,-1,146,140,167,170,-1,168,170,167,-1,168,169,170,-1,146,170,171,-1,169,171,170,-1,172,134,146,171,-1,134,172,130,-1,169,124,126,173,-1,173,126,130,-1,169,173,172,171,-1,173,130,172,-1,122,74,133,174,-1,133,134,174,-1,130,122,174,-1,134,130,174,-1,122,56,175,74,-1,74,175,176,-1,175,56,161,176,-1,74,176,75,-1,176,161,163,-1,176,160,75,-1,176,163,160,-1,115,116,177,51,-1,106,98,177,116,-1,51,177,103,-1,177,98,103,-1]
IndexedFaceSet71.creaseAngle = 1.59
Coordinate72 = x3d.Coordinate()

IndexedFaceSet71.coord = Coordinate72
TextureCoordinate73 = x3d.TextureCoordinate()

IndexedFaceSet71.texCoord = TextureCoordinate73

Shape67.geometry = IndexedFaceSet71

HAnimSegment66.children.append(Shape67)

HAnimJoint65.children.append(HAnimSegment66)
HAnimJoint74 = x3d.HAnimJoint()
HAnimJoint74.name = "l_shoulder"
HAnimJoint74.DEF = "hanim_l_shoulder"
HAnimJoint74.center = [0.167,1.36,-0.0518]
HAnimJoint74.ulimit = [0,0,0]
HAnimJoint74.llimit = [0,0,0]
HAnimSegment75 = x3d.HAnimSegment()
HAnimSegment75.name = "l_upperarm"
HAnimSegment75.DEF = "hanim_l_upperarm"
Transform76 = x3d.Transform()
Transform76.DEF = "l_upperarm_adjust"
Transform76.center = [0.182,1.22,-0.047]
Transform76.rotation = [1,0,0,0.119]
Transform76.translation = [0.167,1.36,-0.0518]
Shape77 = x3d.Shape()
Appearance78 = x3d.Appearance()
Material79 = x3d.Material()
Material79.DEF = "Skin_Color"
Material79.ambientIntensity = 0.25
Material79.diffuseColor = [0.749,0.601,0.462]

Appearance78.material = Material79

Shape77.appearance = Appearance78
IndexedFaceSet80 = x3d.IndexedFaceSet()
IndexedFaceSet80.coordIndex = [2,1,0,-1,2,3,1,-1,2,4,3,-1,2,0,5,-1,6,5,0,-1,7,2,5,-1,8,4,2,-1,8,3,4,-1,9,1,3,-1,10,0,1,-1,0,10,6,-1,1,9,10,-1,3,8,9,-1,2,7,8,-1,5,6,7,-1,11,7,6,-1,14,9,8,-1,15,10,9,-1,11,6,10,-1,10,15,11,-1,9,14,15,-1,8,13,14,-1,8,16,13,-1,7,11,12,-1,21,15,14,-1,15,17,11,-1,15,21,17,-1,16,19,13,-1,13,19,20,-1,21,14,20,-1,14,13,20,-1,12,17,18,-1,12,11,17,-1,12,18,16,-1,18,19,16,-1,12,16,7,-1,16,8,7,-1,19,18,17,-1,20,19,21,-1,19,17,21,-1]
IndexedFaceSet80.creaseAngle = 1.65
Coordinate81 = x3d.Coordinate()

IndexedFaceSet80.coord = Coordinate81

Shape77.geometry = IndexedFaceSet80

Transform76.children.append(Shape77)

HAnimSegment75.children.append(Transform76)

HAnimJoint74.children.append(HAnimSegment75)
HAnimJoint82 = x3d.HAnimJoint()
HAnimJoint82.name = "l_elbow"
HAnimJoint82.DEF = "hanim_l_elbow"
HAnimJoint82.center = [0.196,1.07,-0.0518]
HAnimJoint82.ulimit = [0,0,0]
HAnimJoint82.llimit = [0,0,0]
HAnimSegment83 = x3d.HAnimSegment()
HAnimSegment83.name = "l_forearm"
HAnimSegment83.DEF = "hanim_l_forearm"
Transform84 = x3d.Transform()
Transform84.DEF = "l_forearm_adjust"
Transform84.center = [0.198,0.961,-0.0405]
Transform84.rotation = [-1,0,0,0.1]
Transform84.translation = [0.196,1.07,-0.0518]
Shape85 = x3d.Shape()
Appearance86 = x3d.Appearance()
Material87 = x3d.Material()
Material87.USE = "Skin_Color"

Appearance86.material = Material87

Shape85.appearance = Appearance86
IndexedFaceSet88 = x3d.IndexedFaceSet()
IndexedFaceSet88.coordIndex = [2,1,0,-1,2,3,1,-1,2,4,3,-1,2,5,4,-1,2,6,5,-1,2,0,6,-1,7,6,0,-1,8,5,6,-1,9,4,5,-1,9,3,4,-1,10,1,3,-1,11,0,1,-1,0,11,7,-1,1,10,11,-1,3,9,10,-1,5,12,9,-1,5,8,12,-1,6,7,8,-1,17,16,15,-1,14,17,15,-1,14,18,17,-1,13,18,14,-1,16,17,10,-1,16,10,9,-1,15,16,9,-1,15,9,12,-1,18,13,7,-1,18,7,11,-1,13,14,8,-1,13,8,7,-1,14,15,8,-1,15,12,8,-1,17,18,10,-1,18,11,10,-1]
IndexedFaceSet88.creaseAngle = 1.75
Coordinate89 = x3d.Coordinate()

IndexedFaceSet88.coord = Coordinate89

Shape85.geometry = IndexedFaceSet88

Transform84.children.append(Shape85)

HAnimSegment83.children.append(Transform84)

HAnimJoint82.children.append(HAnimSegment83)
HAnimJoint90 = x3d.HAnimJoint()
HAnimJoint90.name = "l_wrist"
HAnimJoint90.DEF = "hanim_l_wrist"
HAnimJoint90.center = [0.213,0.811,-0.0338]
HAnimJoint90.ulimit = [0,0,0]
HAnimJoint90.llimit = [0,0,0]
HAnimSegment91 = x3d.HAnimSegment()
HAnimSegment91.name = "l_hand"
HAnimSegment91.DEF = "hanim_l_hand"
Transform92 = x3d.Transform()
Transform92.DEF = "l_hand_adjust"
Transform92.center = [0.213,0.811,-0.0338]
Transform92.rotation = [-0.06361,-0.9967,0.04988,1.333]
Transform92.translation = [0.213,0.811,-0.0338]
Shape93 = x3d.Shape()
Appearance94 = x3d.Appearance()
Material95 = x3d.Material()
Material95.USE = "Skin_Color"

Appearance94.material = Material95

Shape93.appearance = Appearance94
IndexedFaceSet96 = x3d.IndexedFaceSet()
IndexedFaceSet96.coordIndex = [2,1,0,-1,5,4,3,-1,3,7,6,-1,2,3,6,-1,7,9,8,-1,6,7,8,-1,9,11,10,-1,8,9,10,-1,11,13,12,-1,10,11,12,-1,13,15,14,-1,12,13,14,-1,15,17,16,-1,14,15,16,-1,17,19,18,-1,16,17,18,-1,19,21,20,-1,18,19,20,-1,31,4,1,-1,4,5,0,-1,1,4,0,-1,5,3,2,-1,0,5,2,-1,26,25,24,-1,26,24,23,-1,27,26,23,-1,28,27,23,-1,28,23,22,-1,29,28,22,-1,29,22,21,-1,30,29,21,-1,15,13,11,-1,17,15,11,-1,19,17,11,-1,19,11,9,-1,31,19,9,-1,31,9,7,-1,4,31,7,-1,4,7,3,-1,30,21,19,-1,31,30,19,-1,12,14,16,-1,10,12,16,-1,10,16,18,-1,8,10,18,-1,6,8,1,-1,2,6,1,-1,39,38,37,-1,37,38,40,-1,37,40,36,-1,36,40,41,-1,36,41,35,-1,35,41,42,-1,35,42,34,-1,34,42,43,-1,34,43,33,-1,33,43,44,-1,33,44,32,-1,20,32,44,-1,20,44,45,-1,20,45,46,-1,47,8,18,-1,47,18,20,-1,47,20,46,-1,8,47,1,-1,22,33,32,-1,23,35,34,-1,23,36,35,-1,37,24,25,-1,40,38,27,-1,29,43,42,-1,45,44,30,-1,47,31,1,-1,47,46,31,-1,29,30,43,-1,30,44,43,-1,45,31,46,-1,45,30,31,-1,28,29,41,-1,29,42,41,-1,28,40,27,-1,28,41,40,-1,26,27,39,-1,27,38,39,-1,25,39,37,-1,25,26,39,-1,24,36,23,-1,24,37,36,-1,23,34,22,-1,34,33,22,-1,22,32,21,-1,32,20,21,-1]
IndexedFaceSet96.creaseAngle = 1.48
Coordinate97 = x3d.Coordinate()

IndexedFaceSet96.coord = Coordinate97

Shape93.geometry = IndexedFaceSet96

Transform92.children.append(Shape93)

HAnimSegment91.children.append(Transform92)

HAnimJoint90.children.append(HAnimSegment91)

HAnimJoint82.children.append(HAnimJoint90)

HAnimJoint74.children.append(HAnimJoint82)

HAnimJoint65.children.append(HAnimJoint74)
HAnimJoint98 = x3d.HAnimJoint()
HAnimJoint98.name = "r_shoulder"
HAnimJoint98.DEF = "hanim_r_shoulder"
HAnimJoint98.center = [-0.167,1.36,-0.0458]
HAnimJoint98.ulimit = [0,0,0]
HAnimJoint98.llimit = [0,0,0]
HAnimSegment99 = x3d.HAnimSegment()
HAnimSegment99.name = "r_upperarm"
HAnimSegment99.DEF = "hanim_r_upperarm"
Transform100 = x3d.Transform()
Transform100.DEF = "r_upperarm_adjust"
Transform100.center = [-0.182,1.22,-0.047]
Transform100.rotation = [1,0,0,0.0836]
Transform100.translation = [-0.167,1.36,-0.0458]
Shape101 = x3d.Shape()
Appearance102 = x3d.Appearance()
Material103 = x3d.Material()
Material103.USE = "Skin_Color"

Appearance102.material = Material103

Shape101.appearance = Appearance102
IndexedFaceSet104 = x3d.IndexedFaceSet()
IndexedFaceSet104.coordIndex = [14,10,20,-1,10,13,20,-1,13,22,20,-1,19,14,20,-1,14,19,12,-1,19,20,24,-1,20,22,25,-1,22,13,25,-1,13,10,11,-1,10,14,5,-1,12,5,14,-1,5,11,10,-1,11,25,13,-1,25,24,20,-1,24,12,19,-1,12,24,9,-1,25,11,8,-1,11,5,2,-1,5,12,9,-1,9,2,5,-1,2,8,11,-1,8,23,25,-1,23,27,25,-1,21,9,24,-1,9,21,7,-1,27,23,18,-1,23,8,18,-1,8,2,6,-1,2,9,7,-1,7,1,2,-1,1,6,2,-1,6,18,8,-1,18,26,27,-1,16,7,21,-1,7,16,4,-1,16,26,17,-1,26,18,15,-1,18,6,3,-1,6,1,0,-1,1,7,0,-1,4,0,7,-1,0,3,6,-1,3,15,18,-1,15,17,26,-1,17,4,16,-1,3,0,15,-1,15,0,4,-1,15,4,17,-1,25,27,24,-1,27,21,24,-1,27,26,21,-1,26,16,21,-1]
IndexedFaceSet104.creaseAngle = 1.53
Coordinate105 = x3d.Coordinate()

IndexedFaceSet104.coord = Coordinate105

Shape101.geometry = IndexedFaceSet104

Transform100.children.append(Shape101)

HAnimSegment99.children.append(Transform100)

HAnimJoint98.children.append(HAnimSegment99)
HAnimJoint106 = x3d.HAnimJoint()
HAnimJoint106.name = "r_elbow"
HAnimJoint106.DEF = "hanim_r_elbow"
HAnimJoint106.center = [-0.192,1.07,-0.0498]
HAnimJoint106.ulimit = [0,0,0]
HAnimJoint106.llimit = [0,0,0]
HAnimSegment107 = x3d.HAnimSegment()
HAnimSegment107.name = "r_forearm"
HAnimSegment107.DEF = "hanim_r_forearm"
Transform108 = x3d.Transform()
Transform108.DEF = "r_forearm_adjust"
Transform108.center = [-0.198,0.961,-0.0397]
Transform108.rotation = [-1,0,0,0.1254]
Transform108.translation = [-0.192,1.07,-0.0498]
Shape109 = x3d.Shape()
Appearance110 = x3d.Appearance()
Material111 = x3d.Material()
Material111.USE = "Skin_Color"

Appearance110.material = Material111

Shape109.appearance = Appearance110
IndexedFaceSet112 = x3d.IndexedFaceSet()
IndexedFaceSet112.coordIndex = [20,13,15,-1,13,8,15,-1,8,12,15,-1,12,18,15,-1,18,22,15,-1,22,20,15,-1,20,22,21,-1,22,18,24,-1,18,12,7,-1,12,8,7,-1,8,13,3,-1,13,20,10,-1,21,10,20,-1,10,3,13,-1,3,7,8,-1,7,19,18,-1,19,24,18,-1,24,21,22,-1,21,24,23,-1,24,19,16,-1,19,7,6,-1,7,3,1,-1,3,10,5,-1,10,21,17,-1,17,5,10,-1,5,1,3,-1,1,6,7,-1,6,16,19,-1,16,23,24,-1,23,17,21,-1,1,5,2,-1,5,17,9,-1,9,2,5,-1,1,4,6,-1,4,16,6,-1,23,9,17,-1,9,23,14,-1,23,16,11,-1,4,11,16,-1,11,14,23,-1,11,4,0,-1,11,0,14,-1,0,2,14,-1,14,2,9,-1,2,0,1,-1,0,4,1,-1]
IndexedFaceSet112.creaseAngle = 1.73
Coordinate113 = x3d.Coordinate()

IndexedFaceSet112.coord = Coordinate113

Shape109.geometry = IndexedFaceSet112

Transform108.children.append(Shape109)

HAnimSegment107.children.append(Transform108)

HAnimJoint106.children.append(HAnimSegment107)
HAnimJoint114 = x3d.HAnimJoint()
HAnimJoint114.name = "r_wrist"
HAnimJoint114.DEF = "hanim_r_wrist"
HAnimJoint114.center = [-0.217,0.811,-0.0338]
HAnimJoint114.ulimit = [0,0,0]
HAnimJoint114.llimit = [0,0,0]
HAnimSegment115 = x3d.HAnimSegment()
HAnimSegment115.name = "r_hand"
HAnimSegment115.DEF = "hanim_r_hand"
Transform116 = x3d.Transform()
Transform116.DEF = "r_hand_adjust"
Transform116.center = [-0.217,0.811,-0.0338]
Transform116.rotation = [-0.09024,0.994,-0.0624,1.216]
Shape117 = x3d.Shape()
Appearance118 = x3d.Appearance()
Material119 = x3d.Material()
Material119.USE = "Skin_Color"

Appearance118.material = Material119

Shape117.appearance = Appearance118
IndexedFaceSet120 = x3d.IndexedFaceSet()
IndexedFaceSet120.coordIndex = [10,9,0,-1,11,30,31,-1,1,12,11,-1,1,11,0,-1,2,13,12,-1,2,12,1,-1,3,14,13,-1,3,13,2,-1,4,15,14,-1,4,14,3,-1,5,16,15,-1,5,15,4,-1,6,17,16,-1,6,16,5,-1,7,18,17,-1,7,17,6,-1,8,19,18,-1,8,18,7,-1,10,31,30,-1,10,30,9,-1,0,11,31,-1,0,31,10,-1,22,23,24,-1,21,22,24,-1,21,24,25,-1,21,25,26,-1,20,21,26,-1,20,26,27,-1,19,20,27,-1,19,27,28,-1,14,15,16,-1,14,16,17,-1,14,17,18,-1,13,14,18,-1,13,18,29,-1,12,13,29,-1,12,29,30,-1,11,12,30,-1,18,19,28,-1,18,28,29,-1,6,5,4,-1,6,4,3,-1,7,6,3,-1,7,3,2,-1,9,2,1,-1,9,1,0,-1,32,38,33,-1,33,38,39,-1,33,39,34,-1,34,39,40,-1,34,40,35,-1,35,40,41,-1,35,41,36,-1,36,41,42,-1,36,42,37,-1,37,42,43,-1,37,43,44,-1,44,43,8,-1,44,8,45,-1,45,8,46,-1,46,8,7,-1,46,7,2,-1,46,2,47,-1,9,47,2,-1,25,34,35,-1,25,33,34,-1,25,24,33,-1,24,32,33,-1,32,24,23,-1,40,39,21,-1,41,40,21,-1,43,19,8,-1,43,20,19,-1,43,42,20,-1,21,20,41,-1,20,42,41,-1,38,22,39,-1,22,21,39,-1,32,23,38,-1,23,22,38,-1,26,25,35,-1,27,36,37,-1,27,37,28,-1,37,44,28,-1,26,35,27,-1,35,36,27,-1,28,44,45,-1,29,46,47,-1,29,9,30,-1,29,47,9,-1,28,45,29,-1,45,46,29,-1]
IndexedFaceSet120.creaseAngle = 1.57
Coordinate121 = x3d.Coordinate()

IndexedFaceSet120.coord = Coordinate121

Shape117.geometry = IndexedFaceSet120

Transform116.children.append(Shape117)

HAnimSegment115.children.append(Transform116)

HAnimJoint114.children.append(HAnimSegment115)

HAnimJoint106.children.append(HAnimJoint114)

HAnimJoint98.children.append(HAnimJoint106)

HAnimJoint65.children.append(HAnimJoint98)
HAnimJoint122 = x3d.HAnimJoint()
HAnimJoint122.name = "vc4"
HAnimJoint122.DEF = "hanim_vc4"
HAnimJoint122.center = [0,1.43,-0.0458]
HAnimJoint122.ulimit = [0,0,0]
HAnimJoint122.llimit = [0,0,0]
HAnimSegment123 = x3d.HAnimSegment()
HAnimSegment123.name = "c4"
HAnimSegment123.DEF = "hanim_c4"
Shape124 = x3d.Shape()
Appearance125 = x3d.Appearance()
Material126 = x3d.Material()
Material126.USE = "Skin_Color"

Appearance125.material = Material126

Shape124.appearance = Appearance125
IndexedFaceSet127 = x3d.IndexedFaceSet()
IndexedFaceSet127.DEF = "neck"
IndexedFaceSet127.coordIndex = [6,5,2,-1,6,2,3,-1,5,4,1,-1,5,1,2,-1,4,7,0,-1,4,0,1,-1,11,10,9,-1,11,9,8,-1,10,13,12,-1,10,12,9,-1,13,15,14,-1,13,14,12,-1,6,3,11,-1,6,11,8,-1,7,14,15,-1,7,15,0,-1,2,10,11,-1,2,11,3,-1,2,1,13,-1,2,13,10,-1,1,0,15,-1,1,15,13,-1,9,5,6,-1,9,6,8,-1,9,12,4,-1,9,4,5,-1,12,14,7,-1,12,7,4,-1]
IndexedFaceSet127.creaseAngle = 1.91
Coordinate128 = x3d.Coordinate()

IndexedFaceSet127.coord = Coordinate128

Shape124.geometry = IndexedFaceSet127

HAnimSegment123.children.append(Shape124)

HAnimJoint122.children.append(HAnimSegment123)
HAnimJoint129 = x3d.HAnimJoint()
HAnimJoint129.name = "skullbase"
HAnimJoint129.DEF = "hanim_skullbase"
HAnimJoint129.center = [0,1.54,-0.0409]
HAnimJoint129.ulimit = [0,0,0]
HAnimJoint129.llimit = [0,0,0]
HAnimSegment130 = x3d.HAnimSegment()
HAnimSegment130.name = "skull"
HAnimSegment130.DEF = "hanim_skull"
Shape131 = x3d.Shape()
Appearance132 = x3d.Appearance()
Material133 = x3d.Material()
Material133.USE = "Skin_Color"

Appearance132.material = Material133

Shape131.appearance = Appearance132
IndexedFaceSet134 = x3d.IndexedFaceSet()
IndexedFaceSet134.DEF = "headIFS"
IndexedFaceSet134.colorIndex = [1,1,1,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,1,1,1,-1,1,1,1,-1,0,0,0,-1,1,1,1,-1,1,1,1,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,2,2,2,-1,2,2,2,-1,2,2,2,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,2,2,2,-1,2,2,2,-1,2,2,2,-1,0,0,0,-1,0,0,0,-1,2,2,2,-1,2,2,2,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,1,1,1,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,2,2,2,-1,2,2,2,-1,2,2,2,-1,2,2,2,-1,2,2,2,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,2,2,2,-1,2,2,2,-1,2,2,2,-1,0,0,0,-1,0,0,0,-1,2,2,2,-1,2,2,2,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,3,3,3,-1,3,3,3,-1,0,0,0,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,3,3,3,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,3,3,3,-1,3,3,3,-1,0,0,0,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,3,3,3,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,0,0,0,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1,3,3,3,-1]
IndexedFaceSet134.coordIndex = [48,87,58,-1,91,92,59,-1,59,92,88,-1,88,93,231,-1,232,86,233,-1,86,89,233,-1,89,57,56,-1,49,55,57,-1,102,86,96,-1,86,90,96,-1,97,95,96,-1,97,127,95,-1,41,96,154,-1,41,102,96,-1,99,102,41,-1,153,99,41,-1,102,40,86,-1,234,235,236,-1,87,237,58,-1,56,57,91,-1,87,234,237,-1,234,236,237,-1,89,49,57,-1,49,50,55,-1,40,89,86,-1,89,56,233,-1,232,90,86,-1,90,97,96,-1,92,93,88,-1,93,94,231,-1,232,231,94,-1,97,90,232,-1,96,42,154,-1,95,42,96,-1,53,46,45,-1,53,45,51,-1,53,51,92,-1,92,51,52,-1,92,52,93,-1,94,93,52,-1,94,52,4,-1,97,232,94,-1,54,47,46,-1,54,46,53,-1,55,47,54,-1,50,47,55,-1,34,33,50,-1,34,50,49,-1,35,34,49,-1,35,49,89,-1,35,89,40,-1,99,39,102,-1,39,35,40,-1,31,34,35,-1,31,35,32,-1,14,32,35,-1,14,35,39,-1,14,39,98,-1,137,38,153,-1,38,99,153,-1,38,98,99,-1,37,238,239,-1,11,238,37,-1,101,37,36,-1,241,141,242,-1,10,12,242,-1,12,13,14,-1,12,14,243,-1,13,15,32,-1,13,32,14,-1,15,16,31,-1,15,31,32,-1,2,70,10,-1,2,10,141,-1,70,69,12,-1,70,12,10,-1,69,68,13,-1,69,13,12,-1,68,67,15,-1,68,15,13,-1,67,66,16,-1,67,16,15,-1,98,39,99,-1,101,11,37,-1,100,101,36,-1,36,244,240,-1,141,10,242,-1,12,243,242,-1,36,37,239,-1,36,239,244,-1,57,55,91,-1,55,54,91,-1,39,40,102,-1,123,103,120,-1,114,122,104,-1,115,122,114,-1,208,105,115,-1,210,119,211,-1,210,106,119,-1,116,107,106,-1,107,108,117,-1,126,119,109,-1,126,110,119,-1,126,95,125,-1,95,127,125,-1,154,126,111,-1,126,109,111,-1,111,109,112,-1,111,112,153,-1,119,113,109,-1,207,213,214,-1,123,209,103,-1,213,212,214,-1,209,214,103,-1,209,207,214,-1,107,117,106,-1,108,118,117,-1,119,106,113,-1,210,116,106,-1,119,110,211,-1,126,125,110,-1,115,105,122,-1,208,124,105,-1,124,208,211,-1,211,110,125,-1,154,42,126,-1,126,42,95,-1,168,128,121,-1,170,168,121,-1,122,170,121,-1,172,170,122,-1,105,172,122,-1,172,105,124,-1,4,172,124,-1,124,211,125,-1,128,130,129,-1,121,128,129,-1,129,130,108,-1,108,130,118,-1,118,131,132,-1,117,118,132,-1,117,132,133,-1,106,117,133,-1,113,106,133,-1,109,152,112,-1,113,133,152,-1,133,132,134,-1,135,133,134,-1,133,135,136,-1,152,133,136,-1,148,152,136,-1,153,138,137,-1,153,112,138,-1,112,148,138,-1,219,217,139,-1,36,240,149,-1,139,217,140,-1,149,139,151,-1,36,149,100,-1,220,141,241,-1,220,150,142,-1,136,143,150,-1,221,136,150,-1,135,144,143,-1,136,135,143,-1,134,158,144,-1,135,134,144,-1,142,161,2,-1,141,142,2,-1,150,145,161,-1,142,150,161,-1,143,146,145,-1,150,143,145,-1,144,147,146,-1,143,144,146,-1,158,160,147,-1,144,158,147,-1,112,152,148,-1,139,140,151,-1,149,151,100,-1,240,218,149,-1,220,142,141,-1,220,221,150,-1,219,139,149,-1,218,219,149,-1,104,108,107,-1,104,129,108,-1,109,113,152,-1,153,41,111,-1,129,104,122,-1,129,122,121,-1,91,54,92,-1,54,53,92,-1,97,94,127,-1,127,94,4,-1,125,127,124,-1,127,4,124,-1,154,111,41,-1,31,30,33,-1,31,33,34,-1,16,17,30,-1,16,30,31,-1,66,65,17,-1,66,17,16,-1,2,73,156,-1,2,156,70,-1,156,72,66,-1,156,66,67,-1,156,67,68,-1,156,68,69,-1,156,69,70,-1,72,71,65,-1,72,65,66,-1,17,18,30,-1,45,44,51,-1,51,44,43,-1,51,43,52,-1,52,43,1,-1,52,1,4,-1,245,246,27,-1,245,27,3,-1,246,247,28,-1,246,28,27,-1,248,22,29,-1,248,29,28,-1,248,28,247,-1,27,26,0,-1,27,0,3,-1,27,28,25,-1,27,25,26,-1,29,24,25,-1,29,25,28,-1,22,23,24,-1,22,24,29,-1,249,250,22,-1,249,22,248,-1,250,60,23,-1,250,23,22,-1,17,254,18,-1,65,254,17,-1,71,64,65,-1,63,74,75,-1,63,75,61,-1,64,255,254,-1,75,62,61,-1,62,76,60,-1,76,77,23,-1,76,23,60,-1,77,24,23,-1,77,78,25,-1,77,25,24,-1,78,84,26,-1,78,26,25,-1,84,192,0,-1,84,0,26,-1,84,83,193,-1,84,193,192,-1,79,83,84,-1,79,84,78,-1,76,79,78,-1,76,78,77,-1,80,83,79,-1,80,204,83,-1,75,81,80,-1,81,85,204,-1,81,204,80,-1,74,81,75,-1,74,82,81,-1,82,5,85,-1,82,85,81,-1,155,8,71,-1,155,71,72,-1,8,6,64,-1,8,64,71,-1,6,7,255,-1,6,255,64,-1,7,9,256,-1,7,256,255,-1,9,257,256,-1,73,155,156,-1,155,72,156,-1,204,193,83,-1,64,254,65,-1,131,157,134,-1,132,131,134,-1,157,159,158,-1,134,157,158,-1,159,206,160,-1,158,159,160,-1,203,73,2,-1,161,203,2,-1,160,162,203,-1,147,160,203,-1,146,147,203,-1,145,146,203,-1,161,145,203,-1,206,163,162,-1,160,206,162,-1,157,164,159,-1,170,169,168,-1,171,169,170,-1,172,171,170,-1,1,171,172,-1,4,1,172,-1,173,227,245,-1,3,173,245,-1,174,226,227,-1,173,174,227,-1,176,175,215,-1,174,176,215,-1,226,174,215,-1,0,177,173,-1,3,0,173,-1,178,174,173,-1,177,178,173,-1,178,179,176,-1,174,178,176,-1,179,180,175,-1,176,179,175,-1,175,225,216,-1,215,175,216,-1,180,181,225,-1,175,180,225,-1,164,228,159,-1,159,228,206,-1,206,185,163,-1,187,186,184,-1,183,187,184,-1,228,229,185,-1,183,182,187,-1,181,188,182,-1,180,189,188,-1,181,180,188,-1,180,179,189,-1,178,190,189,-1,179,178,189,-1,177,191,190,-1,178,177,190,-1,0,192,191,-1,177,0,191,-1,193,205,191,-1,192,193,191,-1,191,205,194,-1,190,191,194,-1,190,194,188,-1,189,190,188,-1,194,205,195,-1,205,204,195,-1,195,196,187,-1,204,85,196,-1,195,204,196,-1,187,196,186,-1,196,197,186,-1,85,5,197,-1,196,85,197,-1,163,198,202,-1,162,163,202,-1,185,199,198,-1,163,185,198,-1,229,200,199,-1,185,229,199,-1,230,201,200,-1,229,230,200,-1,230,257,201,-1,203,202,73,-1,203,162,202,-1,205,193,204,-1,206,228,185,-1,198,8,155,-1,198,155,202,-1,155,73,202,-1,199,6,8,-1,199,8,198,-1,7,6,199,-1,7,199,200,-1,201,9,7,-1,201,7,200,-1,201,257,9,-1,188,194,195,-1,188,195,182,-1,195,187,182,-1,80,79,76,-1,80,62,75,-1,80,76,62,-1,47,50,33,-1,131,118,130,-1,20,21,47,-1,21,46,47,-1,20,33,19,-1,20,47,33,-1,33,30,19,-1,30,18,19,-1,62,60,251,-1,60,250,251,-1,252,61,251,-1,61,62,251,-1,252,63,61,-1,252,253,63,-1,166,130,167,-1,130,128,167,-1,166,131,130,-1,166,165,131,-1,165,157,131,-1,165,164,157,-1,224,181,182,-1,224,225,181,-1,224,183,223,-1,224,182,183,-1,183,184,223,-1,184,222,223,-1]
IndexedFaceSet134.creaseAngle = 0.7854
Coordinate135 = x3d.Coordinate()
Coordinate135.DEF = "Face"

IndexedFaceSet134.coord = Coordinate135
Color136 = x3d.Color()

IndexedFaceSet134.color = Color136

Shape131.geometry = IndexedFaceSet134

HAnimSegment130.children.append(Shape131)

HAnimJoint129.children.append(HAnimSegment130)

HAnimJoint122.children.append(HAnimJoint129)

HAnimJoint65.children.append(HAnimJoint122)

HAnimJoint15.children.append(HAnimJoint65)

HAnimHumanoid14.skeleton.append(HAnimJoint15)
HAnimSite137 = x3d.HAnimSite()
HAnimSite137.name = "NancyNativeTags_view"
HAnimSite137.DEF = "hanim_NancyNativeTags_view"
Viewpoint138 = x3d.Viewpoint()
Viewpoint138.DEF = "InclinedView"
Viewpoint138.description = "Inclined View"
Viewpoint138.orientation = [-0.113,0.993,0.0347,0.671]
Viewpoint138.position = [1.62,1.05,2.06]

HAnimSite137.children.append(Viewpoint138)
Viewpoint139 = x3d.Viewpoint()
Viewpoint139.DEF = "FrontView"
Viewpoint139.description = "Front View"
Viewpoint139.position = [0,0.854,2.57665]

HAnimSite137.children.append(Viewpoint139)
Viewpoint140 = x3d.Viewpoint()
Viewpoint140.DEF = "SideView"
Viewpoint140.description = "Side View"
Viewpoint140.orientation = [0,1,0,1.57079]
Viewpoint140.position = [2.5929,0.854,0]

HAnimSite137.children.append(Viewpoint140)
Viewpoint141 = x3d.Viewpoint()
Viewpoint141.DEF = "TopView"
Viewpoint141.description = "Top View"
Viewpoint141.orientation = [1,0,0,-1.57079]
Viewpoint141.position = [0,3.4495,0]

HAnimSite137.children.append(Viewpoint141)

HAnimHumanoid14.viewpoints.append(HAnimSite137)
HAnimJoint142 = x3d.HAnimJoint()
HAnimJoint142.USE = "hanim_humanoid_root"

HAnimHumanoid14.joints.append(HAnimJoint142)
HAnimJoint143 = x3d.HAnimJoint()
HAnimJoint143.USE = "hanim_sacroiliac"

HAnimHumanoid14.joints.append(HAnimJoint143)
HAnimJoint144 = x3d.HAnimJoint()
HAnimJoint144.USE = "hanim_vl1"

HAnimHumanoid14.joints.append(HAnimJoint144)
HAnimJoint145 = x3d.HAnimJoint()
HAnimJoint145.USE = "hanim_vc4"

HAnimHumanoid14.joints.append(HAnimJoint145)
HAnimJoint146 = x3d.HAnimJoint()
HAnimJoint146.USE = "hanim_skullbase"

HAnimHumanoid14.joints.append(HAnimJoint146)
HAnimJoint147 = x3d.HAnimJoint()
HAnimJoint147.USE = "hanim_l_ankle"

HAnimHumanoid14.joints.append(HAnimJoint147)
HAnimJoint148 = x3d.HAnimJoint()
HAnimJoint148.USE = "hanim_r_ankle"

HAnimHumanoid14.joints.append(HAnimJoint148)
HAnimJoint149 = x3d.HAnimJoint()
HAnimJoint149.USE = "hanim_l_elbow"

HAnimHumanoid14.joints.append(HAnimJoint149)
HAnimJoint150 = x3d.HAnimJoint()
HAnimJoint150.USE = "hanim_r_elbow"

HAnimHumanoid14.joints.append(HAnimJoint150)
HAnimJoint151 = x3d.HAnimJoint()
HAnimJoint151.USE = "hanim_l_hip"

HAnimHumanoid14.joints.append(HAnimJoint151)
HAnimJoint152 = x3d.HAnimJoint()
HAnimJoint152.USE = "hanim_r_hip"

HAnimHumanoid14.joints.append(HAnimJoint152)
HAnimJoint153 = x3d.HAnimJoint()
HAnimJoint153.USE = "hanim_l_knee"

HAnimHumanoid14.joints.append(HAnimJoint153)
HAnimJoint154 = x3d.HAnimJoint()
HAnimJoint154.USE = "hanim_r_knee"

HAnimHumanoid14.joints.append(HAnimJoint154)
HAnimJoint155 = x3d.HAnimJoint()
HAnimJoint155.USE = "hanim_l_shoulder"

HAnimHumanoid14.joints.append(HAnimJoint155)
HAnimJoint156 = x3d.HAnimJoint()
HAnimJoint156.USE = "hanim_r_shoulder"

HAnimHumanoid14.joints.append(HAnimJoint156)
HAnimJoint157 = x3d.HAnimJoint()
HAnimJoint157.USE = "hanim_l_wrist"

HAnimHumanoid14.joints.append(HAnimJoint157)
HAnimJoint158 = x3d.HAnimJoint()
HAnimJoint158.USE = "hanim_r_wrist"

HAnimHumanoid14.joints.append(HAnimJoint158)
HAnimSegment159 = x3d.HAnimSegment()
HAnimSegment159.USE = "hanim_pelvis"

HAnimHumanoid14.segments.append(HAnimSegment159)
HAnimSegment160 = x3d.HAnimSegment()
HAnimSegment160.USE = "hanim_l1"

HAnimHumanoid14.segments.append(HAnimSegment160)
HAnimSegment161 = x3d.HAnimSegment()
HAnimSegment161.USE = "hanim_c4"

HAnimHumanoid14.segments.append(HAnimSegment161)
HAnimSegment162 = x3d.HAnimSegment()
HAnimSegment162.USE = "hanim_skull"

HAnimHumanoid14.segments.append(HAnimSegment162)
HAnimSegment163 = x3d.HAnimSegment()
HAnimSegment163.USE = "hanim_l_calf"

HAnimHumanoid14.segments.append(HAnimSegment163)
HAnimSegment164 = x3d.HAnimSegment()
HAnimSegment164.USE = "hanim_r_calf"

HAnimHumanoid14.segments.append(HAnimSegment164)
HAnimSegment165 = x3d.HAnimSegment()
HAnimSegment165.USE = "hanim_l_forearm"

HAnimHumanoid14.segments.append(HAnimSegment165)
HAnimSegment166 = x3d.HAnimSegment()
HAnimSegment166.USE = "hanim_r_forearm"

HAnimHumanoid14.segments.append(HAnimSegment166)
HAnimSegment167 = x3d.HAnimSegment()
HAnimSegment167.USE = "hanim_l_hand"

HAnimHumanoid14.segments.append(HAnimSegment167)
HAnimSegment168 = x3d.HAnimSegment()
HAnimSegment168.USE = "hanim_r_hand"

HAnimHumanoid14.segments.append(HAnimSegment168)
HAnimSegment169 = x3d.HAnimSegment()
HAnimSegment169.USE = "hanim_l_hindfoot"

HAnimHumanoid14.segments.append(HAnimSegment169)
HAnimSegment170 = x3d.HAnimSegment()
HAnimSegment170.USE = "hanim_r_hindfoot"

HAnimHumanoid14.segments.append(HAnimSegment170)
HAnimSegment171 = x3d.HAnimSegment()
HAnimSegment171.USE = "hanim_l_thigh"

HAnimHumanoid14.segments.append(HAnimSegment171)
HAnimSegment172 = x3d.HAnimSegment()
HAnimSegment172.USE = "hanim_r_thigh"

HAnimHumanoid14.segments.append(HAnimSegment172)
HAnimSegment173 = x3d.HAnimSegment()
HAnimSegment173.USE = "hanim_l_upperarm"

HAnimHumanoid14.segments.append(HAnimSegment173)
HAnimSegment174 = x3d.HAnimSegment()
HAnimSegment174.USE = "hanim_r_upperarm"

HAnimHumanoid14.segments.append(HAnimSegment174)

Scene13.children.append(HAnimHumanoid14)
WorldInfo175 = x3d.WorldInfo()
WorldInfo175.info = ["Copyright (c) 1997. 3Name3D / Yglesias Wallock Divekar, Inc."]
WorldInfo175.title = "Nancy - an HAnim compliant avatar by 3Name3D"

Scene13.children.append(WorldInfo175)
NavigationInfo176 = x3d.NavigationInfo()
NavigationInfo176.avatarSize = [0.15,1.53,0.75]
NavigationInfo176.speed = 0.5
NavigationInfo176.type = ["EXAMINE"]

Scene13.children.append(NavigationInfo176)
Group177 = x3d.Group()
Group177.DEF = "Interface"
Transform178 = x3d.Transform()
ProximitySensor179 = x3d.ProximitySensor()
ProximitySensor179.DEF = "HudProx"
ProximitySensor179.center = [0,20,0]
ProximitySensor179.size = [500,100,500]

Transform178.children.append(ProximitySensor179)

Group177.children.append(Transform178)
Collision180 = x3d.Collision()
Collision180.DEF = "HUD"
Collision180.enabled = False
Transform181 = x3d.Transform()
Transform181.DEF = "HudXform"
Transform182 = x3d.Transform()
Transform182.scale = [0.012,0.012,0.012]
Transform182.translation = [0.01107,-0.025,-0.08]
Transform183 = x3d.Transform()
Transform183.DEF = "Stand_Text"
TouchSensor184 = x3d.TouchSensor()
TouchSensor184.DEF = "Stand_Touch"
TouchSensor184.description = "click for behavior"

Transform183.children.append(TouchSensor184)
Shape185 = x3d.Shape()
Shape185.DEF = "Stand"
IndexedFaceSet186 = x3d.IndexedFaceSet()
IndexedFaceSet186.coordIndex = [1,30,29,-1,1,29,2,-1,31,47,46,-1,31,46,32,-1,78,77,80,-1,78,80,79,-1,96,113,112,-1,96,112,95,-1,95,112,111,-1,95,111,94,-1,94,111,110,-1,94,110,93,-1,93,110,109,-1,93,109,108,-1,93,108,100,-1,107,99,100,-1,107,100,108,-1,107,106,99,-1,106,105,98,-1,106,98,99,-1,104,97,98,-1,104,98,105,-1,103,102,104,-1,104,102,101,-1,104,101,97,-1,101,96,97,-1,101,97,101,-1,101,101,96,-1,96,101,113,-1,113,101,114,-1,115,86,85,-1,115,85,116,-1,117,87,84,-1,117,84,118,-1,119,83,120,-1,121,88,82,-1,121,82,122,-1,123,89,81,-1,123,81,124,-1,125,90,126,-1,127,92,128,-1,129,91,130,-1,54,49,50,-1,54,50,55,-1,76,75,74,-1,76,74,54,-1,54,74,73,-1,54,73,49,-1,49,73,48,-1,48,73,62,-1,48,62,61,-1,48,61,60,-1,48,60,53,-1,53,60,59,-1,53,59,53,-1,53,59,58,-1,53,58,52,-1,52,58,57,-1,52,57,51,-1,56,51,57,-1,56,55,50,-1,56,50,51,-1,62,73,72,-1,62,72,63,-1,63,72,71,-1,63,71,64,-1,64,71,70,-1,64,70,69,-1,64,69,65,-1,65,69,68,-1,65,68,67,-1,65,67,66,-1,131,40,39,-1,131,39,132,-1,133,43,42,-1,133,42,134,-1,135,37,36,-1,135,36,136,-1,137,41,38,-1,137,38,138,-1,139,44,35,-1,139,35,140,-1,141,34,142,-1,143,45,33,-1,143,33,144,-1,145,16,15,-1,145,15,146,-1,147,14,148,-1,149,17,13,-1,149,13,150,-1,151,18,12,-1,151,12,152,-1,153,19,11,-1,153,11,154,-1,155,20,10,-1,155,10,156,-1,157,9,158,-1,159,21,8,-1,159,8,160,-1,161,22,7,-1,161,7,162,-1,163,23,164,-1,165,24,6,-1,165,6,166,-1,167,25,5,-1,167,5,168,-1,169,26,170,-1,171,27,4,-1,171,4,172,-1,173,28,3,-1,173,3,174,-1,175,0,176,-1]
Coordinate187 = x3d.Coordinate()

IndexedFaceSet186.coord = Coordinate187

Shape185.geometry = IndexedFaceSet186
Appearance188 = x3d.Appearance()
Material189 = x3d.Material()
Material189.DEF = "text_color"
Material189.ambientIntensity = 0
Material189.diffuseColor = [0,0,0]
Material189.emissiveColor = [0.819,0.521,0.169]

Appearance188.material = Material189

Shape185.appearance = Appearance188

Transform183.children.append(Shape185)
Transform190 = x3d.Transform()
Transform190.scale = [84.89,77.52,77.52]
Transform190.translation = [0.04092,1.843,3.826]
Shape191 = x3d.Shape()
Shape191.DEF = "Stand_Back"
IndexedFaceSet192 = x3d.IndexedFaceSet()
IndexedFaceSet192.coordIndex = [0,2,3,-1,2,0,1,-1]
Coordinate193 = x3d.Coordinate()

IndexedFaceSet192.coord = Coordinate193

Shape191.geometry = IndexedFaceSet192
Appearance194 = x3d.Appearance()
Material195 = x3d.Material()
Material195.DEF = "Clear"
Material195.ambientIntensity = 0
Material195.diffuseColor = [0,0,0]
Material195.transparency = 1

Appearance194.material = Material195

Shape191.appearance = Appearance194

Transform190.children.append(Shape191)

Transform183.children.append(Transform190)

Transform182.children.append(Transform183)
Transform196 = x3d.Transform()
Transform196.DEF = "Walk_Text"
TouchSensor197 = x3d.TouchSensor()
TouchSensor197.DEF = "Walk_Touch"
TouchSensor197.description = "click for behavior"

Transform196.children.append(TouchSensor197)
Shape198 = x3d.Shape()
Shape198.DEF = "WALK"
IndexedFaceSet199 = x3d.IndexedFaceSet()
IndexedFaceSet199.coordIndex = [0,2,1,-1,3,2,0,-1,12,3,0,-1,4,3,12,-1,11,4,12,-1,5,4,11,-1,10,5,11,-1,6,5,10,-1,9,6,10,-1,7,6,9,-1,8,7,9,-1,15,14,13,-1,16,15,13,-1,19,18,17,-1,20,19,17,-1,27,20,17,-1,28,27,17,-1,26,20,27,-1,23,20,26,-1,21,20,23,-1,25,23,26,-1,22,21,23,-1,24,23,25,-1,29,30,31,-1,29,31,32,-1,33,34,35,-1,33,35,29,-1,29,35,36,-1,29,36,30,-1,30,36,37,-1,37,36,38,-1,37,38,39,-1,37,39,40,-1,37,40,41,-1,41,40,42,-1,41,42,41,-1,41,42,43,-1,41,43,44,-1,44,43,45,-1,44,45,46,-1,47,46,45,-1,47,32,31,-1,47,31,46,-1,38,36,48,-1,38,48,49,-1,49,48,50,-1,49,50,51,-1,51,50,52,-1,51,52,53,-1,51,53,54,-1,54,53,55,-1,54,55,56,-1,54,56,57,-1]
Coordinate200 = x3d.Coordinate()

IndexedFaceSet199.coord = Coordinate200

Shape198.geometry = IndexedFaceSet199
Appearance201 = x3d.Appearance()
Material202 = x3d.Material()
Material202.USE = "text_color"

Appearance201.material = Material202

Shape198.appearance = Appearance201

Transform196.children.append(Shape198)
Transform203 = x3d.Transform()
Transform203.scale = [81.3,81.3,81.31]
Transform203.translation = [-0.0414,1.941,4.015]
Shape204 = x3d.Shape()
Shape204.DEF = "Walk_Back"
IndexedFaceSet205 = x3d.IndexedFaceSet()
IndexedFaceSet205.coordIndex = [1,3,0,-1,3,1,2,-1]
Coordinate206 = x3d.Coordinate()

IndexedFaceSet205.coord = Coordinate206

Shape204.geometry = IndexedFaceSet205
Appearance207 = x3d.Appearance()
Material208 = x3d.Material()
Material208.USE = "Clear"

Appearance207.material = Material208

Shape204.appearance = Appearance207

Transform203.children.append(Shape204)

Transform196.children.append(Transform203)

Transform182.children.append(Transform196)
Transform209 = x3d.Transform()
Transform209.DEF = "Run_Text"
TouchSensor210 = x3d.TouchSensor()
TouchSensor210.DEF = "Run_Touch"
TouchSensor210.description = "click for behavior"

Transform209.children.append(TouchSensor210)
Shape211 = x3d.Shape()
Shape211.DEF = "Run"
IndexedFaceSet212 = x3d.IndexedFaceSet()
IndexedFaceSet212.coordIndex = [24,26,25,-1,53,39,54,-1,17,1,0,-1,17,0,16,-1,0,14,16,-1,0,15,14,-1,14,13,22,-1,14,22,16,-1,13,12,21,-1,13,21,22,-1,12,6,21,-1,12,11,7,-1,12,7,6,-1,11,8,7,-1,10,8,11,-1,10,9,8,-1,6,5,21,-1,5,4,20,-1,5,20,21,-1,4,3,19,-1,4,19,20,-1,3,2,18,-1,3,18,19,-1,18,2,1,-1,18,1,17,-1,55,32,31,-1,55,31,56,-1,57,33,30,-1,57,30,58,-1,59,29,60,-1,61,34,28,-1,61,28,62,-1,63,35,27,-1,63,27,64,-1,65,36,66,-1,67,38,68,-1,69,37,70,-1,71,23,72,-1,73,48,47,-1,73,47,74,-1,75,49,46,-1,75,46,76,-1,77,45,78,-1,79,50,44,-1,79,44,80,-1,81,51,43,-1,81,43,82,-1,83,41,84,-1,85,40,86,-1,87,52,88,-1,89,42,90,-1]
Coordinate213 = x3d.Coordinate()

IndexedFaceSet212.coord = Coordinate213

Shape211.geometry = IndexedFaceSet212
Appearance214 = x3d.Appearance()
Material215 = x3d.Material()
Material215.USE = "text_color"

Appearance214.material = Material215

Shape211.appearance = Appearance214

Transform209.children.append(Shape211)
Transform216 = x3d.Transform()
Transform216.scale = [82.47,82.47,82.48]
Transform216.translation = [-0.01579,1.968,4.074]
Shape217 = x3d.Shape()
Shape217.DEF = "Run_Back"
IndexedFaceSet218 = x3d.IndexedFaceSet()
IndexedFaceSet218.coordIndex = [0,2,3,-1,2,0,1,-1]
Coordinate219 = x3d.Coordinate()

IndexedFaceSet218.coord = Coordinate219

Shape217.geometry = IndexedFaceSet218
Appearance220 = x3d.Appearance()
Material221 = x3d.Material()
Material221.USE = "Clear"

Appearance220.material = Material221

Shape217.appearance = Appearance220

Transform216.children.append(Shape217)

Transform209.children.append(Transform216)

Transform182.children.append(Transform209)
Transform222 = x3d.Transform()
Transform222.DEF = "Jump_Text"
TouchSensor223 = x3d.TouchSensor()
TouchSensor223.DEF = "Jump_Touch"
TouchSensor223.description = "click for behavior"

Transform222.children.append(TouchSensor223)
Shape224 = x3d.Shape()
Shape224.DEF = "Jump"
IndexedFaceSet225 = x3d.IndexedFaceSet()
IndexedFaceSet225.coordIndex = [1,0,14,-1,1,14,2,-1,16,15,18,-1,16,18,17,-1,64,65,66,-1,67,68,69,-1,67,69,70,-1,71,72,73,-1,71,73,74,-1,75,76,77,-1,78,79,80,-1,78,80,81,-1,82,83,84,-1,82,84,85,-1,86,87,88,-1,89,90,91,-1,92,93,94,-1,95,96,97,-1,98,7,6,-1,98,6,99,-1,100,8,5,-1,100,5,101,-1,102,9,4,-1,102,4,103,-1,104,10,105,-1,106,11,3,-1,106,3,107,-1,108,12,109,-1,110,13,111,-1,112,27,26,-1,112,26,113,-1,114,28,25,-1,114,25,115,-1,116,24,117,-1,118,29,23,-1,118,23,119,-1,120,30,22,-1,120,22,121,-1,122,31,123,-1,124,34,33,-1,124,33,125,-1,126,35,32,-1,126,32,127,-1,128,21,129,-1,130,36,20,-1,130,20,131,-1,132,37,19,-1,132,19,133,-1,134,38,135,-1,136,40,137,-1,138,39,139,-1,53,58,59,-1,53,59,54,-1,53,52,58,-1,52,51,57,-1,52,57,58,-1,51,50,56,-1,51,56,57,-1,50,49,56,-1,49,48,63,-1,49,63,56,-1,48,47,63,-1,63,47,46,-1,63,46,62,-1,62,46,45,-1,62,45,44,-1,62,44,61,-1,61,44,60,-1,54,59,60,-1,44,43,42,-1,60,44,42,-1,41,55,54,-1,41,54,60,-1,41,60,42,-1]
Coordinate226 = x3d.Coordinate()

IndexedFaceSet225.coord = Coordinate226

Shape224.geometry = IndexedFaceSet225
Appearance227 = x3d.Appearance()
Material228 = x3d.Material()
Material228.USE = "text_color"

Appearance227.material = Material228

Shape224.appearance = Appearance227

Transform222.children.append(Shape224)
Transform229 = x3d.Transform()
Transform229.scale = [83.79,83.79,83.79]
Transform229.translation = [-0.008979,1.99,4.14]
Shape230 = x3d.Shape()
Shape230.DEF = "Jump_Back"
IndexedFaceSet231 = x3d.IndexedFaceSet()
IndexedFaceSet231.coordIndex = [0,2,3,-1,2,0,1,-1]
Coordinate232 = x3d.Coordinate()

IndexedFaceSet231.coord = Coordinate232

Shape230.geometry = IndexedFaceSet231
Appearance233 = x3d.Appearance()
Material234 = x3d.Material()
Material234.USE = "Clear"

Appearance233.material = Material234

Shape230.appearance = Appearance233

Transform229.children.append(Shape230)

Transform222.children.append(Transform229)

Transform182.children.append(Transform222)

Transform181.children.append(Transform182)

Collision180.proxy = Transform181

Group177.children.append(Collision180)
Transform235 = x3d.Transform()
Transform235.DEF = "Floor"
Transform235.scale = [1,0.0125,1]
Transform235.translation = [0,-0.0125,0]
Shape236 = x3d.Shape()
Box237 = x3d.Box()

Shape236.geometry = Box237
Appearance238 = x3d.Appearance()
Material239 = x3d.Material()

Appearance238.material = Material239

Shape236.appearance = Appearance238

Transform235.children.append(Shape236)

Group177.children.append(Transform235)

Scene13.children.append(Group177)
Group240 = x3d.Group()
Group240.DEF = "Animations"
Group241 = x3d.Group()
Group241.DEF = "Stand_Animation"
OrientationInterpolator242 = x3d.OrientationInterpolator()
OrientationInterpolator242.DEF = "r_ankle_RotationInterpolator_Stand"
OrientationInterpolator242.key = [0,1]

Group241.children.append(OrientationInterpolator242)
OrientationInterpolator243 = x3d.OrientationInterpolator()
OrientationInterpolator243.DEF = "r_knee_RotationInterpolator_Stand"
OrientationInterpolator243.key = [0,1]

Group241.children.append(OrientationInterpolator243)
OrientationInterpolator244 = x3d.OrientationInterpolator()
OrientationInterpolator244.DEF = "r_hip_RotationInterpolator_Stand"
OrientationInterpolator244.key = [0,1]

Group241.children.append(OrientationInterpolator244)
OrientationInterpolator245 = x3d.OrientationInterpolator()
OrientationInterpolator245.DEF = "l_ankle_RotationInterpolator_Stand"
OrientationInterpolator245.key = [0,1]

Group241.children.append(OrientationInterpolator245)
OrientationInterpolator246 = x3d.OrientationInterpolator()
OrientationInterpolator246.DEF = "l_knee_RotationInterpolator_Stand"
OrientationInterpolator246.key = [0,1]

Group241.children.append(OrientationInterpolator246)
OrientationInterpolator247 = x3d.OrientationInterpolator()
OrientationInterpolator247.DEF = "l_hip_RotationInterpolator_Stand"
OrientationInterpolator247.key = [0,1]

Group241.children.append(OrientationInterpolator247)
OrientationInterpolator248 = x3d.OrientationInterpolator()
OrientationInterpolator248.DEF = "lower_body_RotationInterpolator_Stand"
OrientationInterpolator248.key = [0,1]

Group241.children.append(OrientationInterpolator248)
OrientationInterpolator249 = x3d.OrientationInterpolator()
OrientationInterpolator249.DEF = "r_wrist_RotationInterpolator_Stand"
OrientationInterpolator249.key = [0,1]

Group241.children.append(OrientationInterpolator249)
OrientationInterpolator250 = x3d.OrientationInterpolator()
OrientationInterpolator250.DEF = "r_elbow_RotationInterpolator_Stand"
OrientationInterpolator250.key = [0,1]

Group241.children.append(OrientationInterpolator250)
OrientationInterpolator251 = x3d.OrientationInterpolator()
OrientationInterpolator251.DEF = "r_shoulder_RotationInterpolator_Stand"
OrientationInterpolator251.key = [0,1]

Group241.children.append(OrientationInterpolator251)
OrientationInterpolator252 = x3d.OrientationInterpolator()
OrientationInterpolator252.DEF = "l_wrist_RotationInterpolator_Stand"
OrientationInterpolator252.key = [0,1]

Group241.children.append(OrientationInterpolator252)
OrientationInterpolator253 = x3d.OrientationInterpolator()
OrientationInterpolator253.DEF = "l_elbow_RotationInterpolator_Stand"
OrientationInterpolator253.key = [0,1]

Group241.children.append(OrientationInterpolator253)
OrientationInterpolator254 = x3d.OrientationInterpolator()
OrientationInterpolator254.DEF = "l_shoulder_RotationInterpolator_Stand"
OrientationInterpolator254.key = [0,1]

Group241.children.append(OrientationInterpolator254)
OrientationInterpolator255 = x3d.OrientationInterpolator()
OrientationInterpolator255.DEF = "head_RotationInterpolator_Stand"
OrientationInterpolator255.key = [0,1]

Group241.children.append(OrientationInterpolator255)
OrientationInterpolator256 = x3d.OrientationInterpolator()
OrientationInterpolator256.DEF = "neck_RotationInterpolator_Stand"
OrientationInterpolator256.key = [0,1]

Group241.children.append(OrientationInterpolator256)
OrientationInterpolator257 = x3d.OrientationInterpolator()
OrientationInterpolator257.DEF = "upper_body_RotationInterpolator_Stand"
OrientationInterpolator257.key = [0,1]

Group241.children.append(OrientationInterpolator257)
OrientationInterpolator258 = x3d.OrientationInterpolator()
OrientationInterpolator258.DEF = "whole_body_RotationInterpolator_Stand"
OrientationInterpolator258.key = [0,1]

Group241.children.append(OrientationInterpolator258)
PositionInterpolator259 = x3d.PositionInterpolator()
PositionInterpolator259.DEF = "whole_body_TranslationInterpolator_Stand"
PositionInterpolator259.key = [0,1]

Group241.children.append(PositionInterpolator259)
TimeSensor260 = x3d.TimeSensor()
TimeSensor260.DEF = "Stand_Time"
TimeSensor260.cycleInterval = 0.009999999776482582

Group241.children.append(TimeSensor260)

Group240.children.append(Group241)
Group261 = x3d.Group()
Group261.DEF = "Walk_Animation"
OrientationInterpolator262 = x3d.OrientationInterpolator()
OrientationInterpolator262.DEF = "r_ankle_RotationInterpolator_BasicWalk"
OrientationInterpolator262.key = [0,0.125,0.2083,0.375,0.4583,0.5,0.6667,0.75,0.7917,0.9167,1]

Group261.children.append(OrientationInterpolator262)
OrientationInterpolator263 = x3d.OrientationInterpolator()
OrientationInterpolator263.DEF = "r_knee_RotationInterpolator_BasicWalk"
OrientationInterpolator263.key = [0,0.125,0.2083,0.2917,0.375,0.5,0.6667,0.7917,0.9167,1]

Group261.children.append(OrientationInterpolator263)
OrientationInterpolator264 = x3d.OrientationInterpolator()
OrientationInterpolator264.DEF = "r_hip_RotationInterpolator_BasicWalk"
OrientationInterpolator264.key = [0,0.125,0.2083,0.2917,0.375,0.5,0.6667,0.7917,0.9167,1]

Group261.children.append(OrientationInterpolator264)
OrientationInterpolator265 = x3d.OrientationInterpolator()
OrientationInterpolator265.DEF = "l_ankle_RotationInterpolator_BasicWalk"
OrientationInterpolator265.key = [0,0.125,0.2083,0.375,0.6667,0.9167,1]

Group261.children.append(OrientationInterpolator265)
OrientationInterpolator266 = x3d.OrientationInterpolator()
OrientationInterpolator266.DEF = "l_knee_RotationInterpolator_BasicWalk"
OrientationInterpolator266.key = [0,0.2083,0.375,0.5,0.6667,0.7917,0.9167,1]

Group261.children.append(OrientationInterpolator266)
OrientationInterpolator267 = x3d.OrientationInterpolator()
OrientationInterpolator267.DEF = "l_hip_RotationInterpolator_BasicWalk"
OrientationInterpolator267.key = [0,0.25,0.375,0.5,0.6667,0.7917,0.9167,1]

Group261.children.append(OrientationInterpolator267)
OrientationInterpolator268 = x3d.OrientationInterpolator()
OrientationInterpolator268.DEF = "lower_body_RotationInterpolator_BasicWalk"
OrientationInterpolator268.key = [0,0.5,1]

Group261.children.append(OrientationInterpolator268)
OrientationInterpolator269 = x3d.OrientationInterpolator()
OrientationInterpolator269.DEF = "r_wrist_RotationInterpolator_BasicWalk"
OrientationInterpolator269.key = [0,0.375,0.9167,1]

Group261.children.append(OrientationInterpolator269)
OrientationInterpolator270 = x3d.OrientationInterpolator()
OrientationInterpolator270.DEF = "r_elbow_RotationInterpolator_BasicWalk"
OrientationInterpolator270.key = [0,0.375,0.9167,1]

Group261.children.append(OrientationInterpolator270)
OrientationInterpolator271 = x3d.OrientationInterpolator()
OrientationInterpolator271.DEF = "r_shoulder_RotationInterpolator_BasicWalk"
OrientationInterpolator271.key = [0,0.375,0.9167,1]

Group261.children.append(OrientationInterpolator271)
OrientationInterpolator272 = x3d.OrientationInterpolator()
OrientationInterpolator272.DEF = "l_wrist_RotationInterpolator_BasicWalk"
OrientationInterpolator272.key = [0,0.375,0.9167,1]

Group261.children.append(OrientationInterpolator272)
OrientationInterpolator273 = x3d.OrientationInterpolator()
OrientationInterpolator273.DEF = "l_elbow_RotationInterpolator_BasicWalk"
OrientationInterpolator273.key = [0,0.375,0.9167,1]

Group261.children.append(OrientationInterpolator273)
OrientationInterpolator274 = x3d.OrientationInterpolator()
OrientationInterpolator274.DEF = "l_shoulder_RotationInterpolator_BasicWalk"
OrientationInterpolator274.key = [0,0.375,0.9167,1]

Group261.children.append(OrientationInterpolator274)
OrientationInterpolator275 = x3d.OrientationInterpolator()
OrientationInterpolator275.DEF = "head_RotationInterpolator_BasicWalk"
OrientationInterpolator275.key = [0,0.375,0.4167,0.5,0.5833,0.6667,0.75,0.8333,0.9167,1]

Group261.children.append(OrientationInterpolator275)
OrientationInterpolator276 = x3d.OrientationInterpolator()
OrientationInterpolator276.DEF = "neck_RotationInterpolator_BasicWalk"
OrientationInterpolator276.key = [0,1]

Group261.children.append(OrientationInterpolator276)
OrientationInterpolator277 = x3d.OrientationInterpolator()
OrientationInterpolator277.DEF = "upper_body_RotationInterpolator_BasicWalk"
OrientationInterpolator277.key = [0,0.2083,0.375,0.75,0.8333,1]

Group261.children.append(OrientationInterpolator277)
OrientationInterpolator278 = x3d.OrientationInterpolator()
OrientationInterpolator278.DEF = "whole_body_RotationInterpolator_BasicWalk"
OrientationInterpolator278.key = [0,1]

Group261.children.append(OrientationInterpolator278)
PositionInterpolator279 = x3d.PositionInterpolator()
PositionInterpolator279.DEF = "whole_body_TranslationInterpolator_BasicWalk"
PositionInterpolator279.key = [0,0.04167,0.125,0.1667,0.2083,0.25,0.2917,0.375,0.4583,0.5,0.5417,0.5833,0.625,0.7083,0.75,0.7917,0.875,0.9167,1]

Group261.children.append(PositionInterpolator279)
TimeSensor280 = x3d.TimeSensor()
TimeSensor280.DEF = "Walk_Time"
TimeSensor280.cycleInterval = 2
TimeSensor280.loop = True
TimeSensor280.startTime = -1

Group261.children.append(TimeSensor280)

Group240.children.append(Group261)
Group281 = x3d.Group()
Group281.DEF = "Run_Animation"
OrientationInterpolator282 = x3d.OrientationInterpolator()
OrientationInterpolator282.DEF = "r_ankle_RotationInterpolator_Run"
OrientationInterpolator282.key = [0,0.4909,0.7091,0.8,0.8182,1]

Group281.children.append(OrientationInterpolator282)
OrientationInterpolator283 = x3d.OrientationInterpolator()
OrientationInterpolator283.DEF = "r_knee_RotationInterpolator_Run"
OrientationInterpolator283.key = [0,0.03636,0.2182,0.4909,0.7455,1]

Group281.children.append(OrientationInterpolator283)
OrientationInterpolator284 = x3d.OrientationInterpolator()
OrientationInterpolator284.DEF = "r_hip_RotationInterpolator_Run"
OrientationInterpolator284.key = [0,0.2182,0.4909,0.7455,1]

Group281.children.append(OrientationInterpolator284)
OrientationInterpolator285 = x3d.OrientationInterpolator()
OrientationInterpolator285.DEF = "l_ankle_RotationInterpolator_Run"
OrientationInterpolator285.key = [0,0.2182,0.3091,0.4909,1]

Group281.children.append(OrientationInterpolator285)
OrientationInterpolator286 = x3d.OrientationInterpolator()
OrientationInterpolator286.DEF = "l_knee_RotationInterpolator_Run"
OrientationInterpolator286.key = [0,0.2182,0.4909,0.7455,1]

Group281.children.append(OrientationInterpolator286)
OrientationInterpolator287 = x3d.OrientationInterpolator()
OrientationInterpolator287.DEF = "l_hip_RotationInterpolator_Run"
OrientationInterpolator287.key = [0,0.2182,0.4909,0.7455,1]

Group281.children.append(OrientationInterpolator287)
OrientationInterpolator288 = x3d.OrientationInterpolator()
OrientationInterpolator288.DEF = "lower_body_RotationInterpolator_Run"
OrientationInterpolator288.key = [0,1]

Group281.children.append(OrientationInterpolator288)
OrientationInterpolator289 = x3d.OrientationInterpolator()
OrientationInterpolator289.DEF = "r_wrist_RotationInterpolator_Run"
OrientationInterpolator289.key = [0,1]

Group281.children.append(OrientationInterpolator289)
OrientationInterpolator290 = x3d.OrientationInterpolator()
OrientationInterpolator290.DEF = "r_elbow_RotationInterpolator_Run"
OrientationInterpolator290.key = [0,0.2182,0.4909,0.7455,1]

Group281.children.append(OrientationInterpolator290)
OrientationInterpolator291 = x3d.OrientationInterpolator()
OrientationInterpolator291.DEF = "r_shoulder_RotationInterpolator_Run"
OrientationInterpolator291.key = [0,0.2182,0.4909,0.7455,1]

Group281.children.append(OrientationInterpolator291)
OrientationInterpolator292 = x3d.OrientationInterpolator()
OrientationInterpolator292.DEF = "l_wrist_RotationInterpolator_Run"
OrientationInterpolator292.key = [0,1]

Group281.children.append(OrientationInterpolator292)
OrientationInterpolator293 = x3d.OrientationInterpolator()
OrientationInterpolator293.DEF = "l_elbow_RotationInterpolator_Run"
OrientationInterpolator293.key = [0,0.2182,0.4909,0.7455,1]

Group281.children.append(OrientationInterpolator293)
OrientationInterpolator294 = x3d.OrientationInterpolator()
OrientationInterpolator294.DEF = "l_shoulder_RotationInterpolator_Run"
OrientationInterpolator294.key = [0,0.2182,0.4909,0.7455,1]

Group281.children.append(OrientationInterpolator294)
OrientationInterpolator295 = x3d.OrientationInterpolator()
OrientationInterpolator295.DEF = "head_RotationInterpolator_Run"
OrientationInterpolator295.key = [0,0.4909,1]

Group281.children.append(OrientationInterpolator295)
OrientationInterpolator296 = x3d.OrientationInterpolator()
OrientationInterpolator296.DEF = "neck_RotationInterpolator_Run"
OrientationInterpolator296.key = [0,1]

Group281.children.append(OrientationInterpolator296)
OrientationInterpolator297 = x3d.OrientationInterpolator()
OrientationInterpolator297.DEF = "upper_body_RotationInterpolator_Run"
OrientationInterpolator297.key = [0,0.2545,0.4909,0.7636,1]

Group281.children.append(OrientationInterpolator297)
OrientationInterpolator298 = x3d.OrientationInterpolator()
OrientationInterpolator298.DEF = "whole_body_RotationInterpolator_Run"
OrientationInterpolator298.key = [0,1]

Group281.children.append(OrientationInterpolator298)
PositionInterpolator299 = x3d.PositionInterpolator()
PositionInterpolator299.DEF = "whole_body_TranslationInterpolator_Run"
PositionInterpolator299.key = [0,0.2182,0.2909,0.3091,0.7091,0.8,0.8182,1]

Group281.children.append(PositionInterpolator299)
TimeSensor300 = x3d.TimeSensor()
TimeSensor300.DEF = "Run_Time"
TimeSensor300.loop = True
TimeSensor300.startTime = -1

Group281.children.append(TimeSensor300)

Group240.children.append(Group281)
Group301 = x3d.Group()
Group301.DEF = "Jump_Animation"
OrientationInterpolator302 = x3d.OrientationInterpolator()
OrientationInterpolator302.DEF = "r_ankle_RotationInterpolator_Jump"
OrientationInterpolator302.key = [0,0.28,0.32,0.36,0.4,0.44,0.48,0.64,0.76,0.84,0.88,0.92,0.96,1]

Group301.children.append(OrientationInterpolator302)
OrientationInterpolator303 = x3d.OrientationInterpolator()
OrientationInterpolator303.DEF = "r_knee_RotationInterpolator_Jump"
OrientationInterpolator303.key = [0,0.28,0.32,0.48,0.64,0.76,0.88,1]

Group301.children.append(OrientationInterpolator303)
OrientationInterpolator304 = x3d.OrientationInterpolator()
OrientationInterpolator304.DEF = "r_hip_RotationInterpolator_Jump"
OrientationInterpolator304.key = [0,0.28,0.32,0.36,0.4,0.44,0.48,0.64,0.76,0.88,1]

Group301.children.append(OrientationInterpolator304)
OrientationInterpolator305 = x3d.OrientationInterpolator()
OrientationInterpolator305.DEF = "l_ankle_RotationInterpolator_Jump"
OrientationInterpolator305.key = [0,0.28,0.32,0.36,0.4,0.44,0.48,0.64,0.76,0.84,0.88,0.92,0.96,1]

Group301.children.append(OrientationInterpolator305)
OrientationInterpolator306 = x3d.OrientationInterpolator()
OrientationInterpolator306.DEF = "l_knee_RotationInterpolator_Jump"
OrientationInterpolator306.key = [0,0.28,0.32,0.48,0.64,0.76,0.88,1]

Group301.children.append(OrientationInterpolator306)
OrientationInterpolator307 = x3d.OrientationInterpolator()
OrientationInterpolator307.DEF = "l_hip_RotationInterpolator_Jump"
OrientationInterpolator307.key = [0,0.28,0.32,0.36,0.4,0.44,0.48,0.64,0.76,0.88,1]

Group301.children.append(OrientationInterpolator307)
OrientationInterpolator308 = x3d.OrientationInterpolator()
OrientationInterpolator308.DEF = "lower_body_RotationInterpolator_Jump"
OrientationInterpolator308.key = [0,0.28,0.32,0.48,0.76,1]

Group301.children.append(OrientationInterpolator308)
OrientationInterpolator309 = x3d.OrientationInterpolator()
OrientationInterpolator309.DEF = "r_wrist_RotationInterpolator_Jump"
OrientationInterpolator309.key = [0,0.28,0.32,0.64,0.76,1]

Group301.children.append(OrientationInterpolator309)
OrientationInterpolator310 = x3d.OrientationInterpolator()
OrientationInterpolator310.DEF = "r_elbow_RotationInterpolator_Jump"
OrientationInterpolator310.key = [0,0.28,0.32,0.64,0.76,1]

Group301.children.append(OrientationInterpolator310)
OrientationInterpolator311 = x3d.OrientationInterpolator()
OrientationInterpolator311.DEF = "r_shoulder_RotationInterpolator_Jump"
OrientationInterpolator311.key = [0,0.28,0.32,0.64,0.76,0.88,1]

Group301.children.append(OrientationInterpolator311)
OrientationInterpolator312 = x3d.OrientationInterpolator()
OrientationInterpolator312.DEF = "l_wrist_RotationInterpolator_Jump"
OrientationInterpolator312.key = [0,0.28,0.32,0.64,0.76,0.88,1]

Group301.children.append(OrientationInterpolator312)
OrientationInterpolator313 = x3d.OrientationInterpolator()
OrientationInterpolator313.DEF = "l_elbow_RotationInterpolator_Jump"
OrientationInterpolator313.key = [0,0.28,0.32,0.64,0.76,1]

Group301.children.append(OrientationInterpolator313)
OrientationInterpolator314 = x3d.OrientationInterpolator()
OrientationInterpolator314.DEF = "l_shoulder_RotationInterpolator_Jump"
OrientationInterpolator314.key = [0,0.28,0.32,0.64,0.76,0.88,1]

Group301.children.append(OrientationInterpolator314)
OrientationInterpolator315 = x3d.OrientationInterpolator()
OrientationInterpolator315.DEF = "head_RotationInterpolator_Jump"
OrientationInterpolator315.key = [0,0.28,0.32,0.48,0.76,1]

Group301.children.append(OrientationInterpolator315)
OrientationInterpolator316 = x3d.OrientationInterpolator()
OrientationInterpolator316.DEF = "neck_RotationInterpolator_Jump"
OrientationInterpolator316.key = [0,0.28,0.32,0.48,0.76,1]

Group301.children.append(OrientationInterpolator316)
OrientationInterpolator317 = x3d.OrientationInterpolator()
OrientationInterpolator317.DEF = "upper_body_RotationInterpolator_Jump"
OrientationInterpolator317.key = [0,0.28,0.32,0.48,0.76,0.88,1]

Group301.children.append(OrientationInterpolator317)
OrientationInterpolator318 = x3d.OrientationInterpolator()
OrientationInterpolator318.DEF = "whole_body_RotationInterpolator_Jump"
OrientationInterpolator318.key = [0,0.28,0.32,0.48,0.64,0.76,1]

Group301.children.append(OrientationInterpolator318)
PositionInterpolator319 = x3d.PositionInterpolator()
PositionInterpolator319.DEF = "whole_body_TranslationInterpolator_Jump"
PositionInterpolator319.key = [0,0.04,0.08,0.12,0.16,0.2,0.24,0.28,0.32,0.36,0.4,0.44,0.48,0.64,0.76,0.8,0.84,0.88,0.92,0.96,1]

Group301.children.append(PositionInterpolator319)
TimeSensor320 = x3d.TimeSensor()
TimeSensor320.DEF = "Jump_Time"
TimeSensor320.cycleInterval = 2
TimeSensor320.startTime = -1

Group301.children.append(TimeSensor320)

Group240.children.append(Group301)

Scene13.children.append(Group240)
ROUTE321 = x3d.ROUTE()
ROUTE321.fromField = "position_changed"
ROUTE321.fromNode = "HudProx"
ROUTE321.toField = "set_translation"
ROUTE321.toNode = "HudXform"

Scene13.children.append(ROUTE321)
ROUTE322 = x3d.ROUTE()
ROUTE322.fromField = "orientation_changed"
ROUTE322.fromNode = "HudProx"
ROUTE322.toField = "set_rotation"
ROUTE322.toNode = "HudXform"

Scene13.children.append(ROUTE322)
ROUTE323 = x3d.ROUTE()
ROUTE323.fromField = "touchTime"
ROUTE323.fromNode = "Stand_Touch"
ROUTE323.toField = "stopTime"
ROUTE323.toNode = "Walk_Time"

Scene13.children.append(ROUTE323)
ROUTE324 = x3d.ROUTE()
ROUTE324.fromField = "touchTime"
ROUTE324.fromNode = "Stand_Touch"
ROUTE324.toField = "stopTime"
ROUTE324.toNode = "Run_Time"

Scene13.children.append(ROUTE324)
ROUTE325 = x3d.ROUTE()
ROUTE325.fromField = "touchTime"
ROUTE325.fromNode = "Stand_Touch"
ROUTE325.toField = "stopTime"
ROUTE325.toNode = "Jump_Time"

Scene13.children.append(ROUTE325)
ROUTE326 = x3d.ROUTE()
ROUTE326.fromField = "touchTime"
ROUTE326.fromNode = "Stand_Touch"
ROUTE326.toField = "startTime"
ROUTE326.toNode = "Stand_Time"

Scene13.children.append(ROUTE326)
ROUTE327 = x3d.ROUTE()
ROUTE327.fromField = "touchTime"
ROUTE327.fromNode = "Walk_Touch"
ROUTE327.toField = "stopTime"
ROUTE327.toNode = "Stand_Time"

Scene13.children.append(ROUTE327)
ROUTE328 = x3d.ROUTE()
ROUTE328.fromField = "touchTime"
ROUTE328.fromNode = "Walk_Touch"
ROUTE328.toField = "stopTime"
ROUTE328.toNode = "Run_Time"

Scene13.children.append(ROUTE328)
ROUTE329 = x3d.ROUTE()
ROUTE329.fromField = "touchTime"
ROUTE329.fromNode = "Walk_Touch"
ROUTE329.toField = "stopTime"
ROUTE329.toNode = "Jump_Time"

Scene13.children.append(ROUTE329)
ROUTE330 = x3d.ROUTE()
ROUTE330.fromField = "touchTime"
ROUTE330.fromNode = "Walk_Touch"
ROUTE330.toField = "startTime"
ROUTE330.toNode = "Walk_Time"

Scene13.children.append(ROUTE330)
ROUTE331 = x3d.ROUTE()
ROUTE331.fromField = "touchTime"
ROUTE331.fromNode = "Run_Touch"
ROUTE331.toField = "stopTime"
ROUTE331.toNode = "Stand_Time"

Scene13.children.append(ROUTE331)
ROUTE332 = x3d.ROUTE()
ROUTE332.fromField = "touchTime"
ROUTE332.fromNode = "Run_Touch"
ROUTE332.toField = "stopTime"
ROUTE332.toNode = "Walk_Time"

Scene13.children.append(ROUTE332)
ROUTE333 = x3d.ROUTE()
ROUTE333.fromField = "touchTime"
ROUTE333.fromNode = "Run_Touch"
ROUTE333.toField = "stopTime"
ROUTE333.toNode = "Jump_Time"

Scene13.children.append(ROUTE333)
ROUTE334 = x3d.ROUTE()
ROUTE334.fromField = "touchTime"
ROUTE334.fromNode = "Run_Touch"
ROUTE334.toField = "startTime"
ROUTE334.toNode = "Run_Time"

Scene13.children.append(ROUTE334)
ROUTE335 = x3d.ROUTE()
ROUTE335.fromField = "touchTime"
ROUTE335.fromNode = "Jump_Touch"
ROUTE335.toField = "stopTime"
ROUTE335.toNode = "Stand_Time"

Scene13.children.append(ROUTE335)
ROUTE336 = x3d.ROUTE()
ROUTE336.fromField = "touchTime"
ROUTE336.fromNode = "Jump_Touch"
ROUTE336.toField = "stopTime"
ROUTE336.toNode = "Walk_Time"

Scene13.children.append(ROUTE336)
ROUTE337 = x3d.ROUTE()
ROUTE337.fromField = "touchTime"
ROUTE337.fromNode = "Jump_Touch"
ROUTE337.toField = "stopTime"
ROUTE337.toNode = "Run_Time"

Scene13.children.append(ROUTE337)
ROUTE338 = x3d.ROUTE()
ROUTE338.fromField = "touchTime"
ROUTE338.fromNode = "Jump_Touch"
ROUTE338.toField = "startTime"
ROUTE338.toNode = "Jump_Time"

Scene13.children.append(ROUTE338)
ROUTE339 = x3d.ROUTE()
ROUTE339.fromField = "fraction_changed"
ROUTE339.fromNode = "Stand_Time"
ROUTE339.toField = "set_fraction"
ROUTE339.toNode = "r_ankle_RotationInterpolator_Stand"

Scene13.children.append(ROUTE339)
ROUTE340 = x3d.ROUTE()
ROUTE340.fromField = "fraction_changed"
ROUTE340.fromNode = "Stand_Time"
ROUTE340.toField = "set_fraction"
ROUTE340.toNode = "r_knee_RotationInterpolator_Stand"

Scene13.children.append(ROUTE340)
ROUTE341 = x3d.ROUTE()
ROUTE341.fromField = "fraction_changed"
ROUTE341.fromNode = "Stand_Time"
ROUTE341.toField = "set_fraction"
ROUTE341.toNode = "r_hip_RotationInterpolator_Stand"

Scene13.children.append(ROUTE341)
ROUTE342 = x3d.ROUTE()
ROUTE342.fromField = "fraction_changed"
ROUTE342.fromNode = "Stand_Time"
ROUTE342.toField = "set_fraction"
ROUTE342.toNode = "l_ankle_RotationInterpolator_Stand"

Scene13.children.append(ROUTE342)
ROUTE343 = x3d.ROUTE()
ROUTE343.fromField = "fraction_changed"
ROUTE343.fromNode = "Stand_Time"
ROUTE343.toField = "set_fraction"
ROUTE343.toNode = "l_knee_RotationInterpolator_Stand"

Scene13.children.append(ROUTE343)
ROUTE344 = x3d.ROUTE()
ROUTE344.fromField = "fraction_changed"
ROUTE344.fromNode = "Stand_Time"
ROUTE344.toField = "set_fraction"
ROUTE344.toNode = "l_hip_RotationInterpolator_Stand"

Scene13.children.append(ROUTE344)
ROUTE345 = x3d.ROUTE()
ROUTE345.fromField = "fraction_changed"
ROUTE345.fromNode = "Stand_Time"
ROUTE345.toField = "set_fraction"
ROUTE345.toNode = "lower_body_RotationInterpolator_Stand"

Scene13.children.append(ROUTE345)
ROUTE346 = x3d.ROUTE()
ROUTE346.fromField = "fraction_changed"
ROUTE346.fromNode = "Stand_Time"
ROUTE346.toField = "set_fraction"
ROUTE346.toNode = "r_wrist_RotationInterpolator_Stand"

Scene13.children.append(ROUTE346)
ROUTE347 = x3d.ROUTE()
ROUTE347.fromField = "fraction_changed"
ROUTE347.fromNode = "Stand_Time"
ROUTE347.toField = "set_fraction"
ROUTE347.toNode = "r_elbow_RotationInterpolator_Stand"

Scene13.children.append(ROUTE347)
ROUTE348 = x3d.ROUTE()
ROUTE348.fromField = "fraction_changed"
ROUTE348.fromNode = "Stand_Time"
ROUTE348.toField = "set_fraction"
ROUTE348.toNode = "r_shoulder_RotationInterpolator_Stand"

Scene13.children.append(ROUTE348)
ROUTE349 = x3d.ROUTE()
ROUTE349.fromField = "fraction_changed"
ROUTE349.fromNode = "Stand_Time"
ROUTE349.toField = "set_fraction"
ROUTE349.toNode = "l_wrist_RotationInterpolator_Stand"

Scene13.children.append(ROUTE349)
ROUTE350 = x3d.ROUTE()
ROUTE350.fromField = "fraction_changed"
ROUTE350.fromNode = "Stand_Time"
ROUTE350.toField = "set_fraction"
ROUTE350.toNode = "l_elbow_RotationInterpolator_Stand"

Scene13.children.append(ROUTE350)
ROUTE351 = x3d.ROUTE()
ROUTE351.fromField = "fraction_changed"
ROUTE351.fromNode = "Stand_Time"
ROUTE351.toField = "set_fraction"
ROUTE351.toNode = "l_shoulder_RotationInterpolator_Stand"

Scene13.children.append(ROUTE351)
ROUTE352 = x3d.ROUTE()
ROUTE352.fromField = "fraction_changed"
ROUTE352.fromNode = "Stand_Time"
ROUTE352.toField = "set_fraction"
ROUTE352.toNode = "head_RotationInterpolator_Stand"

Scene13.children.append(ROUTE352)
ROUTE353 = x3d.ROUTE()
ROUTE353.fromField = "fraction_changed"
ROUTE353.fromNode = "Stand_Time"
ROUTE353.toField = "set_fraction"
ROUTE353.toNode = "neck_RotationInterpolator_Stand"

Scene13.children.append(ROUTE353)
ROUTE354 = x3d.ROUTE()
ROUTE354.fromField = "fraction_changed"
ROUTE354.fromNode = "Stand_Time"
ROUTE354.toField = "set_fraction"
ROUTE354.toNode = "upper_body_RotationInterpolator_Stand"

Scene13.children.append(ROUTE354)
ROUTE355 = x3d.ROUTE()
ROUTE355.fromField = "fraction_changed"
ROUTE355.fromNode = "Stand_Time"
ROUTE355.toField = "set_fraction"
ROUTE355.toNode = "whole_body_RotationInterpolator_Stand"

Scene13.children.append(ROUTE355)
ROUTE356 = x3d.ROUTE()
ROUTE356.fromField = "fraction_changed"
ROUTE356.fromNode = "Stand_Time"
ROUTE356.toField = "set_fraction"
ROUTE356.toNode = "whole_body_TranslationInterpolator_Stand"

Scene13.children.append(ROUTE356)
ROUTE357 = x3d.ROUTE()
ROUTE357.fromField = "value_changed"
ROUTE357.fromNode = "r_ankle_RotationInterpolator_Stand"
ROUTE357.toField = "set_rotation"
ROUTE357.toNode = "hanim_r_ankle"

Scene13.children.append(ROUTE357)
ROUTE358 = x3d.ROUTE()
ROUTE358.fromField = "value_changed"
ROUTE358.fromNode = "r_knee_RotationInterpolator_Stand"
ROUTE358.toField = "set_rotation"
ROUTE358.toNode = "hanim_r_knee"

Scene13.children.append(ROUTE358)
ROUTE359 = x3d.ROUTE()
ROUTE359.fromField = "value_changed"
ROUTE359.fromNode = "r_hip_RotationInterpolator_Stand"
ROUTE359.toField = "set_rotation"
ROUTE359.toNode = "hanim_r_hip"

Scene13.children.append(ROUTE359)
ROUTE360 = x3d.ROUTE()
ROUTE360.fromField = "value_changed"
ROUTE360.fromNode = "l_ankle_RotationInterpolator_Stand"
ROUTE360.toField = "set_rotation"
ROUTE360.toNode = "hanim_l_ankle"

Scene13.children.append(ROUTE360)
ROUTE361 = x3d.ROUTE()
ROUTE361.fromField = "value_changed"
ROUTE361.fromNode = "l_knee_RotationInterpolator_Stand"
ROUTE361.toField = "set_rotation"
ROUTE361.toNode = "hanim_l_knee"

Scene13.children.append(ROUTE361)
ROUTE362 = x3d.ROUTE()
ROUTE362.fromField = "value_changed"
ROUTE362.fromNode = "l_hip_RotationInterpolator_Stand"
ROUTE362.toField = "set_rotation"
ROUTE362.toNode = "hanim_l_hip"

Scene13.children.append(ROUTE362)
ROUTE363 = x3d.ROUTE()
ROUTE363.fromField = "value_changed"
ROUTE363.fromNode = "lower_body_RotationInterpolator_Stand"
ROUTE363.toField = "set_rotation"
ROUTE363.toNode = "hanim_sacroiliac"

Scene13.children.append(ROUTE363)
ROUTE364 = x3d.ROUTE()
ROUTE364.fromField = "value_changed"
ROUTE364.fromNode = "r_wrist_RotationInterpolator_Stand"
ROUTE364.toField = "set_rotation"
ROUTE364.toNode = "hanim_r_wrist"

Scene13.children.append(ROUTE364)
ROUTE365 = x3d.ROUTE()
ROUTE365.fromField = "value_changed"
ROUTE365.fromNode = "r_elbow_RotationInterpolator_Stand"
ROUTE365.toField = "set_rotation"
ROUTE365.toNode = "hanim_r_elbow"

Scene13.children.append(ROUTE365)
ROUTE366 = x3d.ROUTE()
ROUTE366.fromField = "value_changed"
ROUTE366.fromNode = "r_shoulder_RotationInterpolator_Stand"
ROUTE366.toField = "set_rotation"
ROUTE366.toNode = "hanim_r_shoulder"

Scene13.children.append(ROUTE366)
ROUTE367 = x3d.ROUTE()
ROUTE367.fromField = "value_changed"
ROUTE367.fromNode = "l_wrist_RotationInterpolator_Stand"
ROUTE367.toField = "set_rotation"
ROUTE367.toNode = "hanim_l_wrist"

Scene13.children.append(ROUTE367)
ROUTE368 = x3d.ROUTE()
ROUTE368.fromField = "value_changed"
ROUTE368.fromNode = "l_elbow_RotationInterpolator_Stand"
ROUTE368.toField = "set_rotation"
ROUTE368.toNode = "hanim_l_elbow"

Scene13.children.append(ROUTE368)
ROUTE369 = x3d.ROUTE()
ROUTE369.fromField = "value_changed"
ROUTE369.fromNode = "l_shoulder_RotationInterpolator_Stand"
ROUTE369.toField = "set_rotation"
ROUTE369.toNode = "hanim_l_shoulder"

Scene13.children.append(ROUTE369)
ROUTE370 = x3d.ROUTE()
ROUTE370.fromField = "value_changed"
ROUTE370.fromNode = "head_RotationInterpolator_Stand"
ROUTE370.toField = "set_rotation"
ROUTE370.toNode = "hanim_skullbase"

Scene13.children.append(ROUTE370)
ROUTE371 = x3d.ROUTE()
ROUTE371.fromField = "value_changed"
ROUTE371.fromNode = "neck_RotationInterpolator_Stand"
ROUTE371.toField = "set_rotation"
ROUTE371.toNode = "hanim_vc4"

Scene13.children.append(ROUTE371)
ROUTE372 = x3d.ROUTE()
ROUTE372.fromField = "value_changed"
ROUTE372.fromNode = "upper_body_RotationInterpolator_Stand"
ROUTE372.toField = "set_rotation"
ROUTE372.toNode = "hanim_vl1"

Scene13.children.append(ROUTE372)
ROUTE373 = x3d.ROUTE()
ROUTE373.fromField = "value_changed"
ROUTE373.fromNode = "whole_body_RotationInterpolator_Stand"
ROUTE373.toField = "set_rotation"
ROUTE373.toNode = "hanim_humanoid_root"

Scene13.children.append(ROUTE373)
ROUTE374 = x3d.ROUTE()
ROUTE374.fromField = "value_changed"
ROUTE374.fromNode = "whole_body_TranslationInterpolator_Stand"
ROUTE374.toField = "set_translation"
ROUTE374.toNode = "hanim_humanoid_root"

Scene13.children.append(ROUTE374)
ROUTE375 = x3d.ROUTE()
ROUTE375.fromField = "fraction_changed"
ROUTE375.fromNode = "Walk_Time"
ROUTE375.toField = "set_fraction"
ROUTE375.toNode = "r_ankle_RotationInterpolator_BasicWalk"

Scene13.children.append(ROUTE375)
ROUTE376 = x3d.ROUTE()
ROUTE376.fromField = "fraction_changed"
ROUTE376.fromNode = "Walk_Time"
ROUTE376.toField = "set_fraction"
ROUTE376.toNode = "r_knee_RotationInterpolator_BasicWalk"

Scene13.children.append(ROUTE376)
ROUTE377 = x3d.ROUTE()
ROUTE377.fromField = "fraction_changed"
ROUTE377.fromNode = "Walk_Time"
ROUTE377.toField = "set_fraction"
ROUTE377.toNode = "r_hip_RotationInterpolator_BasicWalk"

Scene13.children.append(ROUTE377)
ROUTE378 = x3d.ROUTE()
ROUTE378.fromField = "fraction_changed"
ROUTE378.fromNode = "Walk_Time"
ROUTE378.toField = "set_fraction"
ROUTE378.toNode = "l_ankle_RotationInterpolator_BasicWalk"

Scene13.children.append(ROUTE378)
ROUTE379 = x3d.ROUTE()
ROUTE379.fromField = "fraction_changed"
ROUTE379.fromNode = "Walk_Time"
ROUTE379.toField = "set_fraction"
ROUTE379.toNode = "l_knee_RotationInterpolator_BasicWalk"

Scene13.children.append(ROUTE379)
ROUTE380 = x3d.ROUTE()
ROUTE380.fromField = "fraction_changed"
ROUTE380.fromNode = "Walk_Time"
ROUTE380.toField = "set_fraction"
ROUTE380.toNode = "l_hip_RotationInterpolator_BasicWalk"

Scene13.children.append(ROUTE380)
ROUTE381 = x3d.ROUTE()
ROUTE381.fromField = "fraction_changed"
ROUTE381.fromNode = "Walk_Time"
ROUTE381.toField = "set_fraction"
ROUTE381.toNode = "lower_body_RotationInterpolator_BasicWalk"

Scene13.children.append(ROUTE381)
ROUTE382 = x3d.ROUTE()
ROUTE382.fromField = "fraction_changed"
ROUTE382.fromNode = "Walk_Time"
ROUTE382.toField = "set_fraction"
ROUTE382.toNode = "r_wrist_RotationInterpolator_BasicWalk"

Scene13.children.append(ROUTE382)
ROUTE383 = x3d.ROUTE()
ROUTE383.fromField = "fraction_changed"
ROUTE383.fromNode = "Walk_Time"
ROUTE383.toField = "set_fraction"
ROUTE383.toNode = "r_elbow_RotationInterpolator_BasicWalk"

Scene13.children.append(ROUTE383)
ROUTE384 = x3d.ROUTE()
ROUTE384.fromField = "fraction_changed"
ROUTE384.fromNode = "Walk_Time"
ROUTE384.toField = "set_fraction"
ROUTE384.toNode = "r_shoulder_RotationInterpolator_BasicWalk"

Scene13.children.append(ROUTE384)
ROUTE385 = x3d.ROUTE()
ROUTE385.fromField = "fraction_changed"
ROUTE385.fromNode = "Walk_Time"
ROUTE385.toField = "set_fraction"
ROUTE385.toNode = "l_wrist_RotationInterpolator_BasicWalk"

Scene13.children.append(ROUTE385)
ROUTE386 = x3d.ROUTE()
ROUTE386.fromField = "fraction_changed"
ROUTE386.fromNode = "Walk_Time"
ROUTE386.toField = "set_fraction"
ROUTE386.toNode = "l_elbow_RotationInterpolator_BasicWalk"

Scene13.children.append(ROUTE386)
ROUTE387 = x3d.ROUTE()
ROUTE387.fromField = "fraction_changed"
ROUTE387.fromNode = "Walk_Time"
ROUTE387.toField = "set_fraction"
ROUTE387.toNode = "l_shoulder_RotationInterpolator_BasicWalk"

Scene13.children.append(ROUTE387)
ROUTE388 = x3d.ROUTE()
ROUTE388.fromField = "fraction_changed"
ROUTE388.fromNode = "Walk_Time"
ROUTE388.toField = "set_fraction"
ROUTE388.toNode = "head_RotationInterpolator_BasicWalk"

Scene13.children.append(ROUTE388)
ROUTE389 = x3d.ROUTE()
ROUTE389.fromField = "fraction_changed"
ROUTE389.fromNode = "Walk_Time"
ROUTE389.toField = "set_fraction"
ROUTE389.toNode = "neck_RotationInterpolator_BasicWalk"

Scene13.children.append(ROUTE389)
ROUTE390 = x3d.ROUTE()
ROUTE390.fromField = "fraction_changed"
ROUTE390.fromNode = "Walk_Time"
ROUTE390.toField = "set_fraction"
ROUTE390.toNode = "upper_body_RotationInterpolator_BasicWalk"

Scene13.children.append(ROUTE390)
ROUTE391 = x3d.ROUTE()
ROUTE391.fromField = "fraction_changed"
ROUTE391.fromNode = "Walk_Time"
ROUTE391.toField = "set_fraction"
ROUTE391.toNode = "whole_body_RotationInterpolator_BasicWalk"

Scene13.children.append(ROUTE391)
ROUTE392 = x3d.ROUTE()
ROUTE392.fromField = "fraction_changed"
ROUTE392.fromNode = "Walk_Time"
ROUTE392.toField = "set_fraction"
ROUTE392.toNode = "whole_body_TranslationInterpolator_BasicWalk"

Scene13.children.append(ROUTE392)
ROUTE393 = x3d.ROUTE()
ROUTE393.fromField = "value_changed"
ROUTE393.fromNode = "r_ankle_RotationInterpolator_BasicWalk"
ROUTE393.toField = "set_rotation"
ROUTE393.toNode = "hanim_r_ankle"

Scene13.children.append(ROUTE393)
ROUTE394 = x3d.ROUTE()
ROUTE394.fromField = "value_changed"
ROUTE394.fromNode = "r_knee_RotationInterpolator_BasicWalk"
ROUTE394.toField = "set_rotation"
ROUTE394.toNode = "hanim_r_knee"

Scene13.children.append(ROUTE394)
ROUTE395 = x3d.ROUTE()
ROUTE395.fromField = "value_changed"
ROUTE395.fromNode = "r_hip_RotationInterpolator_BasicWalk"
ROUTE395.toField = "set_rotation"
ROUTE395.toNode = "hanim_r_hip"

Scene13.children.append(ROUTE395)
ROUTE396 = x3d.ROUTE()
ROUTE396.fromField = "value_changed"
ROUTE396.fromNode = "l_ankle_RotationInterpolator_BasicWalk"
ROUTE396.toField = "set_rotation"
ROUTE396.toNode = "hanim_l_ankle"

Scene13.children.append(ROUTE396)
ROUTE397 = x3d.ROUTE()
ROUTE397.fromField = "value_changed"
ROUTE397.fromNode = "l_knee_RotationInterpolator_BasicWalk"
ROUTE397.toField = "set_rotation"
ROUTE397.toNode = "hanim_l_knee"

Scene13.children.append(ROUTE397)
ROUTE398 = x3d.ROUTE()
ROUTE398.fromField = "value_changed"
ROUTE398.fromNode = "l_hip_RotationInterpolator_BasicWalk"
ROUTE398.toField = "set_rotation"
ROUTE398.toNode = "hanim_l_hip"

Scene13.children.append(ROUTE398)
ROUTE399 = x3d.ROUTE()
ROUTE399.fromField = "value_changed"
ROUTE399.fromNode = "lower_body_RotationInterpolator_BasicWalk"
ROUTE399.toField = "set_rotation"
ROUTE399.toNode = "hanim_sacroiliac"

Scene13.children.append(ROUTE399)
ROUTE400 = x3d.ROUTE()
ROUTE400.fromField = "value_changed"
ROUTE400.fromNode = "r_wrist_RotationInterpolator_BasicWalk"
ROUTE400.toField = "set_rotation"
ROUTE400.toNode = "hanim_r_wrist"

Scene13.children.append(ROUTE400)
ROUTE401 = x3d.ROUTE()
ROUTE401.fromField = "value_changed"
ROUTE401.fromNode = "r_elbow_RotationInterpolator_BasicWalk"
ROUTE401.toField = "set_rotation"
ROUTE401.toNode = "hanim_r_elbow"

Scene13.children.append(ROUTE401)
ROUTE402 = x3d.ROUTE()
ROUTE402.fromField = "value_changed"
ROUTE402.fromNode = "r_shoulder_RotationInterpolator_BasicWalk"
ROUTE402.toField = "set_rotation"
ROUTE402.toNode = "hanim_r_shoulder"

Scene13.children.append(ROUTE402)
ROUTE403 = x3d.ROUTE()
ROUTE403.fromField = "value_changed"
ROUTE403.fromNode = "l_wrist_RotationInterpolator_BasicWalk"
ROUTE403.toField = "set_rotation"
ROUTE403.toNode = "hanim_l_wrist"

Scene13.children.append(ROUTE403)
ROUTE404 = x3d.ROUTE()
ROUTE404.fromField = "value_changed"
ROUTE404.fromNode = "l_elbow_RotationInterpolator_BasicWalk"
ROUTE404.toField = "set_rotation"
ROUTE404.toNode = "hanim_l_elbow"

Scene13.children.append(ROUTE404)
ROUTE405 = x3d.ROUTE()
ROUTE405.fromField = "value_changed"
ROUTE405.fromNode = "l_shoulder_RotationInterpolator_BasicWalk"
ROUTE405.toField = "set_rotation"
ROUTE405.toNode = "hanim_l_shoulder"

Scene13.children.append(ROUTE405)
ROUTE406 = x3d.ROUTE()
ROUTE406.fromField = "value_changed"
ROUTE406.fromNode = "head_RotationInterpolator_BasicWalk"
ROUTE406.toField = "set_rotation"
ROUTE406.toNode = "hanim_skullbase"

Scene13.children.append(ROUTE406)
ROUTE407 = x3d.ROUTE()
ROUTE407.fromField = "value_changed"
ROUTE407.fromNode = "neck_RotationInterpolator_BasicWalk"
ROUTE407.toField = "set_rotation"
ROUTE407.toNode = "hanim_vc4"

Scene13.children.append(ROUTE407)
ROUTE408 = x3d.ROUTE()
ROUTE408.fromField = "value_changed"
ROUTE408.fromNode = "upper_body_RotationInterpolator_BasicWalk"
ROUTE408.toField = "set_rotation"
ROUTE408.toNode = "hanim_vl1"

Scene13.children.append(ROUTE408)
ROUTE409 = x3d.ROUTE()
ROUTE409.fromField = "value_changed"
ROUTE409.fromNode = "whole_body_RotationInterpolator_BasicWalk"
ROUTE409.toField = "set_rotation"
ROUTE409.toNode = "hanim_humanoid_root"

Scene13.children.append(ROUTE409)
ROUTE410 = x3d.ROUTE()
ROUTE410.fromField = "value_changed"
ROUTE410.fromNode = "whole_body_TranslationInterpolator_BasicWalk"
ROUTE410.toField = "set_translation"
ROUTE410.toNode = "hanim_humanoid_root"

Scene13.children.append(ROUTE410)
ROUTE411 = x3d.ROUTE()
ROUTE411.fromField = "fraction_changed"
ROUTE411.fromNode = "Run_Time"
ROUTE411.toField = "set_fraction"
ROUTE411.toNode = "r_ankle_RotationInterpolator_Run"

Scene13.children.append(ROUTE411)
ROUTE412 = x3d.ROUTE()
ROUTE412.fromField = "fraction_changed"
ROUTE412.fromNode = "Run_Time"
ROUTE412.toField = "set_fraction"
ROUTE412.toNode = "r_knee_RotationInterpolator_Run"

Scene13.children.append(ROUTE412)
ROUTE413 = x3d.ROUTE()
ROUTE413.fromField = "fraction_changed"
ROUTE413.fromNode = "Run_Time"
ROUTE413.toField = "set_fraction"
ROUTE413.toNode = "r_hip_RotationInterpolator_Run"

Scene13.children.append(ROUTE413)
ROUTE414 = x3d.ROUTE()
ROUTE414.fromField = "fraction_changed"
ROUTE414.fromNode = "Run_Time"
ROUTE414.toField = "set_fraction"
ROUTE414.toNode = "l_ankle_RotationInterpolator_Run"

Scene13.children.append(ROUTE414)
ROUTE415 = x3d.ROUTE()
ROUTE415.fromField = "fraction_changed"
ROUTE415.fromNode = "Run_Time"
ROUTE415.toField = "set_fraction"
ROUTE415.toNode = "l_knee_RotationInterpolator_Run"

Scene13.children.append(ROUTE415)
ROUTE416 = x3d.ROUTE()
ROUTE416.fromField = "fraction_changed"
ROUTE416.fromNode = "Run_Time"
ROUTE416.toField = "set_fraction"
ROUTE416.toNode = "l_hip_RotationInterpolator_Run"

Scene13.children.append(ROUTE416)
ROUTE417 = x3d.ROUTE()
ROUTE417.fromField = "fraction_changed"
ROUTE417.fromNode = "Run_Time"
ROUTE417.toField = "set_fraction"
ROUTE417.toNode = "lower_body_RotationInterpolator_Run"

Scene13.children.append(ROUTE417)
ROUTE418 = x3d.ROUTE()
ROUTE418.fromField = "fraction_changed"
ROUTE418.fromNode = "Run_Time"
ROUTE418.toField = "set_fraction"
ROUTE418.toNode = "r_wrist_RotationInterpolator_Run"

Scene13.children.append(ROUTE418)
ROUTE419 = x3d.ROUTE()
ROUTE419.fromField = "fraction_changed"
ROUTE419.fromNode = "Run_Time"
ROUTE419.toField = "set_fraction"
ROUTE419.toNode = "r_elbow_RotationInterpolator_Run"

Scene13.children.append(ROUTE419)
ROUTE420 = x3d.ROUTE()
ROUTE420.fromField = "fraction_changed"
ROUTE420.fromNode = "Run_Time"
ROUTE420.toField = "set_fraction"
ROUTE420.toNode = "r_shoulder_RotationInterpolator_Run"

Scene13.children.append(ROUTE420)
ROUTE421 = x3d.ROUTE()
ROUTE421.fromField = "fraction_changed"
ROUTE421.fromNode = "Run_Time"
ROUTE421.toField = "set_fraction"
ROUTE421.toNode = "l_wrist_RotationInterpolator_Run"

Scene13.children.append(ROUTE421)
ROUTE422 = x3d.ROUTE()
ROUTE422.fromField = "fraction_changed"
ROUTE422.fromNode = "Run_Time"
ROUTE422.toField = "set_fraction"
ROUTE422.toNode = "l_elbow_RotationInterpolator_Run"

Scene13.children.append(ROUTE422)
ROUTE423 = x3d.ROUTE()
ROUTE423.fromField = "fraction_changed"
ROUTE423.fromNode = "Run_Time"
ROUTE423.toField = "set_fraction"
ROUTE423.toNode = "l_shoulder_RotationInterpolator_Run"

Scene13.children.append(ROUTE423)
ROUTE424 = x3d.ROUTE()
ROUTE424.fromField = "fraction_changed"
ROUTE424.fromNode = "Run_Time"
ROUTE424.toField = "set_fraction"
ROUTE424.toNode = "head_RotationInterpolator_Run"

Scene13.children.append(ROUTE424)
ROUTE425 = x3d.ROUTE()
ROUTE425.fromField = "fraction_changed"
ROUTE425.fromNode = "Run_Time"
ROUTE425.toField = "set_fraction"
ROUTE425.toNode = "neck_RotationInterpolator_Run"

Scene13.children.append(ROUTE425)
ROUTE426 = x3d.ROUTE()
ROUTE426.fromField = "fraction_changed"
ROUTE426.fromNode = "Run_Time"
ROUTE426.toField = "set_fraction"
ROUTE426.toNode = "upper_body_RotationInterpolator_Run"

Scene13.children.append(ROUTE426)
ROUTE427 = x3d.ROUTE()
ROUTE427.fromField = "fraction_changed"
ROUTE427.fromNode = "Run_Time"
ROUTE427.toField = "set_fraction"
ROUTE427.toNode = "whole_body_RotationInterpolator_Run"

Scene13.children.append(ROUTE427)
ROUTE428 = x3d.ROUTE()
ROUTE428.fromField = "fraction_changed"
ROUTE428.fromNode = "Run_Time"
ROUTE428.toField = "set_fraction"
ROUTE428.toNode = "whole_body_TranslationInterpolator_Run"

Scene13.children.append(ROUTE428)
ROUTE429 = x3d.ROUTE()
ROUTE429.fromField = "value_changed"
ROUTE429.fromNode = "r_ankle_RotationInterpolator_Run"
ROUTE429.toField = "set_rotation"
ROUTE429.toNode = "hanim_r_ankle"

Scene13.children.append(ROUTE429)
ROUTE430 = x3d.ROUTE()
ROUTE430.fromField = "value_changed"
ROUTE430.fromNode = "r_knee_RotationInterpolator_Run"
ROUTE430.toField = "set_rotation"
ROUTE430.toNode = "hanim_r_knee"

Scene13.children.append(ROUTE430)
ROUTE431 = x3d.ROUTE()
ROUTE431.fromField = "value_changed"
ROUTE431.fromNode = "r_hip_RotationInterpolator_Run"
ROUTE431.toField = "set_rotation"
ROUTE431.toNode = "hanim_r_hip"

Scene13.children.append(ROUTE431)
ROUTE432 = x3d.ROUTE()
ROUTE432.fromField = "value_changed"
ROUTE432.fromNode = "l_ankle_RotationInterpolator_Run"
ROUTE432.toField = "set_rotation"
ROUTE432.toNode = "hanim_l_ankle"

Scene13.children.append(ROUTE432)
ROUTE433 = x3d.ROUTE()
ROUTE433.fromField = "value_changed"
ROUTE433.fromNode = "l_knee_RotationInterpolator_Run"
ROUTE433.toField = "set_rotation"
ROUTE433.toNode = "hanim_l_knee"

Scene13.children.append(ROUTE433)
ROUTE434 = x3d.ROUTE()
ROUTE434.fromField = "value_changed"
ROUTE434.fromNode = "l_hip_RotationInterpolator_Run"
ROUTE434.toField = "set_rotation"
ROUTE434.toNode = "hanim_l_hip"

Scene13.children.append(ROUTE434)
ROUTE435 = x3d.ROUTE()
ROUTE435.fromField = "value_changed"
ROUTE435.fromNode = "lower_body_RotationInterpolator_Run"
ROUTE435.toField = "set_rotation"
ROUTE435.toNode = "hanim_sacroiliac"

Scene13.children.append(ROUTE435)
ROUTE436 = x3d.ROUTE()
ROUTE436.fromField = "value_changed"
ROUTE436.fromNode = "r_wrist_RotationInterpolator_Run"
ROUTE436.toField = "set_rotation"
ROUTE436.toNode = "hanim_r_wrist"

Scene13.children.append(ROUTE436)
ROUTE437 = x3d.ROUTE()
ROUTE437.fromField = "value_changed"
ROUTE437.fromNode = "r_elbow_RotationInterpolator_Run"
ROUTE437.toField = "set_rotation"
ROUTE437.toNode = "hanim_r_elbow"

Scene13.children.append(ROUTE437)
ROUTE438 = x3d.ROUTE()
ROUTE438.fromField = "value_changed"
ROUTE438.fromNode = "r_shoulder_RotationInterpolator_Run"
ROUTE438.toField = "set_rotation"
ROUTE438.toNode = "hanim_r_shoulder"

Scene13.children.append(ROUTE438)
ROUTE439 = x3d.ROUTE()
ROUTE439.fromField = "value_changed"
ROUTE439.fromNode = "l_wrist_RotationInterpolator_Run"
ROUTE439.toField = "set_rotation"
ROUTE439.toNode = "hanim_l_wrist"

Scene13.children.append(ROUTE439)
ROUTE440 = x3d.ROUTE()
ROUTE440.fromField = "value_changed"
ROUTE440.fromNode = "l_elbow_RotationInterpolator_Run"
ROUTE440.toField = "set_rotation"
ROUTE440.toNode = "hanim_l_elbow"

Scene13.children.append(ROUTE440)
ROUTE441 = x3d.ROUTE()
ROUTE441.fromField = "value_changed"
ROUTE441.fromNode = "l_shoulder_RotationInterpolator_Run"
ROUTE441.toField = "set_rotation"
ROUTE441.toNode = "hanim_l_shoulder"

Scene13.children.append(ROUTE441)
ROUTE442 = x3d.ROUTE()
ROUTE442.fromField = "value_changed"
ROUTE442.fromNode = "head_RotationInterpolator_Run"
ROUTE442.toField = "set_rotation"
ROUTE442.toNode = "hanim_skullbase"

Scene13.children.append(ROUTE442)
ROUTE443 = x3d.ROUTE()
ROUTE443.fromField = "value_changed"
ROUTE443.fromNode = "neck_RotationInterpolator_Run"
ROUTE443.toField = "set_rotation"
ROUTE443.toNode = "hanim_vc4"

Scene13.children.append(ROUTE443)
ROUTE444 = x3d.ROUTE()
ROUTE444.fromField = "value_changed"
ROUTE444.fromNode = "upper_body_RotationInterpolator_Run"
ROUTE444.toField = "set_rotation"
ROUTE444.toNode = "hanim_vl1"

Scene13.children.append(ROUTE444)
ROUTE445 = x3d.ROUTE()
ROUTE445.fromField = "value_changed"
ROUTE445.fromNode = "whole_body_RotationInterpolator_Run"
ROUTE445.toField = "set_rotation"
ROUTE445.toNode = "hanim_humanoid_root"

Scene13.children.append(ROUTE445)
ROUTE446 = x3d.ROUTE()
ROUTE446.fromField = "value_changed"
ROUTE446.fromNode = "whole_body_TranslationInterpolator_Run"
ROUTE446.toField = "set_translation"
ROUTE446.toNode = "hanim_humanoid_root"

Scene13.children.append(ROUTE446)
ROUTE447 = x3d.ROUTE()
ROUTE447.fromField = "fraction_changed"
ROUTE447.fromNode = "Jump_Time"
ROUTE447.toField = "set_fraction"
ROUTE447.toNode = "r_ankle_RotationInterpolator_Jump"

Scene13.children.append(ROUTE447)
ROUTE448 = x3d.ROUTE()
ROUTE448.fromField = "fraction_changed"
ROUTE448.fromNode = "Jump_Time"
ROUTE448.toField = "set_fraction"
ROUTE448.toNode = "r_knee_RotationInterpolator_Jump"

Scene13.children.append(ROUTE448)
ROUTE449 = x3d.ROUTE()
ROUTE449.fromField = "fraction_changed"
ROUTE449.fromNode = "Jump_Time"
ROUTE449.toField = "set_fraction"
ROUTE449.toNode = "r_hip_RotationInterpolator_Jump"

Scene13.children.append(ROUTE449)
ROUTE450 = x3d.ROUTE()
ROUTE450.fromField = "fraction_changed"
ROUTE450.fromNode = "Jump_Time"
ROUTE450.toField = "set_fraction"
ROUTE450.toNode = "l_ankle_RotationInterpolator_Jump"

Scene13.children.append(ROUTE450)
ROUTE451 = x3d.ROUTE()
ROUTE451.fromField = "fraction_changed"
ROUTE451.fromNode = "Jump_Time"
ROUTE451.toField = "set_fraction"
ROUTE451.toNode = "l_knee_RotationInterpolator_Jump"

Scene13.children.append(ROUTE451)
ROUTE452 = x3d.ROUTE()
ROUTE452.fromField = "fraction_changed"
ROUTE452.fromNode = "Jump_Time"
ROUTE452.toField = "set_fraction"
ROUTE452.toNode = "l_hip_RotationInterpolator_Jump"

Scene13.children.append(ROUTE452)
ROUTE453 = x3d.ROUTE()
ROUTE453.fromField = "fraction_changed"
ROUTE453.fromNode = "Jump_Time"
ROUTE453.toField = "set_fraction"
ROUTE453.toNode = "lower_body_RotationInterpolator_Jump"

Scene13.children.append(ROUTE453)
ROUTE454 = x3d.ROUTE()
ROUTE454.fromField = "fraction_changed"
ROUTE454.fromNode = "Jump_Time"
ROUTE454.toField = "set_fraction"
ROUTE454.toNode = "r_wrist_RotationInterpolator_Jump"

Scene13.children.append(ROUTE454)
ROUTE455 = x3d.ROUTE()
ROUTE455.fromField = "fraction_changed"
ROUTE455.fromNode = "Jump_Time"
ROUTE455.toField = "set_fraction"
ROUTE455.toNode = "r_elbow_RotationInterpolator_Jump"

Scene13.children.append(ROUTE455)
ROUTE456 = x3d.ROUTE()
ROUTE456.fromField = "fraction_changed"
ROUTE456.fromNode = "Jump_Time"
ROUTE456.toField = "set_fraction"
ROUTE456.toNode = "r_shoulder_RotationInterpolator_Jump"

Scene13.children.append(ROUTE456)
ROUTE457 = x3d.ROUTE()
ROUTE457.fromField = "fraction_changed"
ROUTE457.fromNode = "Jump_Time"
ROUTE457.toField = "set_fraction"
ROUTE457.toNode = "l_wrist_RotationInterpolator_Jump"

Scene13.children.append(ROUTE457)
ROUTE458 = x3d.ROUTE()
ROUTE458.fromField = "fraction_changed"
ROUTE458.fromNode = "Jump_Time"
ROUTE458.toField = "set_fraction"
ROUTE458.toNode = "l_elbow_RotationInterpolator_Jump"

Scene13.children.append(ROUTE458)
ROUTE459 = x3d.ROUTE()
ROUTE459.fromField = "fraction_changed"
ROUTE459.fromNode = "Jump_Time"
ROUTE459.toField = "set_fraction"
ROUTE459.toNode = "l_shoulder_RotationInterpolator_Jump"

Scene13.children.append(ROUTE459)
ROUTE460 = x3d.ROUTE()
ROUTE460.fromField = "fraction_changed"
ROUTE460.fromNode = "Jump_Time"
ROUTE460.toField = "set_fraction"
ROUTE460.toNode = "head_RotationInterpolator_Jump"

Scene13.children.append(ROUTE460)
ROUTE461 = x3d.ROUTE()
ROUTE461.fromField = "fraction_changed"
ROUTE461.fromNode = "Jump_Time"
ROUTE461.toField = "set_fraction"
ROUTE461.toNode = "neck_RotationInterpolator_Jump"

Scene13.children.append(ROUTE461)
ROUTE462 = x3d.ROUTE()
ROUTE462.fromField = "fraction_changed"
ROUTE462.fromNode = "Jump_Time"
ROUTE462.toField = "set_fraction"
ROUTE462.toNode = "upper_body_RotationInterpolator_Jump"

Scene13.children.append(ROUTE462)
ROUTE463 = x3d.ROUTE()
ROUTE463.fromField = "fraction_changed"
ROUTE463.fromNode = "Jump_Time"
ROUTE463.toField = "set_fraction"
ROUTE463.toNode = "whole_body_RotationInterpolator_Jump"

Scene13.children.append(ROUTE463)
ROUTE464 = x3d.ROUTE()
ROUTE464.fromField = "fraction_changed"
ROUTE464.fromNode = "Jump_Time"
ROUTE464.toField = "set_fraction"
ROUTE464.toNode = "whole_body_TranslationInterpolator_Jump"

Scene13.children.append(ROUTE464)
ROUTE465 = x3d.ROUTE()
ROUTE465.fromField = "value_changed"
ROUTE465.fromNode = "r_ankle_RotationInterpolator_Jump"
ROUTE465.toField = "set_rotation"
ROUTE465.toNode = "hanim_r_ankle"

Scene13.children.append(ROUTE465)
ROUTE466 = x3d.ROUTE()
ROUTE466.fromField = "value_changed"
ROUTE466.fromNode = "r_knee_RotationInterpolator_Jump"
ROUTE466.toField = "set_rotation"
ROUTE466.toNode = "hanim_r_knee"

Scene13.children.append(ROUTE466)
ROUTE467 = x3d.ROUTE()
ROUTE467.fromField = "value_changed"
ROUTE467.fromNode = "r_hip_RotationInterpolator_Jump"
ROUTE467.toField = "set_rotation"
ROUTE467.toNode = "hanim_r_hip"

Scene13.children.append(ROUTE467)
ROUTE468 = x3d.ROUTE()
ROUTE468.fromField = "value_changed"
ROUTE468.fromNode = "l_ankle_RotationInterpolator_Jump"
ROUTE468.toField = "set_rotation"
ROUTE468.toNode = "hanim_l_ankle"

Scene13.children.append(ROUTE468)
ROUTE469 = x3d.ROUTE()
ROUTE469.fromField = "value_changed"
ROUTE469.fromNode = "l_knee_RotationInterpolator_Jump"
ROUTE469.toField = "set_rotation"
ROUTE469.toNode = "hanim_l_knee"

Scene13.children.append(ROUTE469)
ROUTE470 = x3d.ROUTE()
ROUTE470.fromField = "value_changed"
ROUTE470.fromNode = "l_hip_RotationInterpolator_Jump"
ROUTE470.toField = "set_rotation"
ROUTE470.toNode = "hanim_l_hip"

Scene13.children.append(ROUTE470)
ROUTE471 = x3d.ROUTE()
ROUTE471.fromField = "value_changed"
ROUTE471.fromNode = "lower_body_RotationInterpolator_Jump"
ROUTE471.toField = "set_rotation"
ROUTE471.toNode = "hanim_sacroiliac"

Scene13.children.append(ROUTE471)
ROUTE472 = x3d.ROUTE()
ROUTE472.fromField = "value_changed"
ROUTE472.fromNode = "r_wrist_RotationInterpolator_Jump"
ROUTE472.toField = "set_rotation"
ROUTE472.toNode = "hanim_r_wrist"

Scene13.children.append(ROUTE472)
ROUTE473 = x3d.ROUTE()
ROUTE473.fromField = "value_changed"
ROUTE473.fromNode = "r_elbow_RotationInterpolator_Jump"
ROUTE473.toField = "set_rotation"
ROUTE473.toNode = "hanim_r_elbow"

Scene13.children.append(ROUTE473)
ROUTE474 = x3d.ROUTE()
ROUTE474.fromField = "value_changed"
ROUTE474.fromNode = "r_shoulder_RotationInterpolator_Jump"
ROUTE474.toField = "set_rotation"
ROUTE474.toNode = "hanim_r_shoulder"

Scene13.children.append(ROUTE474)
ROUTE475 = x3d.ROUTE()
ROUTE475.fromField = "value_changed"
ROUTE475.fromNode = "l_wrist_RotationInterpolator_Jump"
ROUTE475.toField = "set_rotation"
ROUTE475.toNode = "hanim_l_wrist"

Scene13.children.append(ROUTE475)
ROUTE476 = x3d.ROUTE()
ROUTE476.fromField = "value_changed"
ROUTE476.fromNode = "l_elbow_RotationInterpolator_Jump"
ROUTE476.toField = "set_rotation"
ROUTE476.toNode = "hanim_l_elbow"

Scene13.children.append(ROUTE476)
ROUTE477 = x3d.ROUTE()
ROUTE477.fromField = "value_changed"
ROUTE477.fromNode = "l_shoulder_RotationInterpolator_Jump"
ROUTE477.toField = "set_rotation"
ROUTE477.toNode = "hanim_l_shoulder"

Scene13.children.append(ROUTE477)
ROUTE478 = x3d.ROUTE()
ROUTE478.fromField = "value_changed"
ROUTE478.fromNode = "head_RotationInterpolator_Jump"
ROUTE478.toField = "set_rotation"
ROUTE478.toNode = "hanim_skullbase"

Scene13.children.append(ROUTE478)
ROUTE479 = x3d.ROUTE()
ROUTE479.fromField = "value_changed"
ROUTE479.fromNode = "neck_RotationInterpolator_Jump"
ROUTE479.toField = "set_rotation"
ROUTE479.toNode = "hanim_vc4"

Scene13.children.append(ROUTE479)
ROUTE480 = x3d.ROUTE()
ROUTE480.fromField = "value_changed"
ROUTE480.fromNode = "upper_body_RotationInterpolator_Jump"
ROUTE480.toField = "set_rotation"
ROUTE480.toNode = "hanim_vl1"

Scene13.children.append(ROUTE480)
ROUTE481 = x3d.ROUTE()
ROUTE481.fromField = "value_changed"
ROUTE481.fromNode = "whole_body_RotationInterpolator_Jump"
ROUTE481.toField = "set_rotation"
ROUTE481.toNode = "hanim_humanoid_root"

Scene13.children.append(ROUTE481)
ROUTE482 = x3d.ROUTE()
ROUTE482.fromField = "value_changed"
ROUTE482.fromNode = "whole_body_TranslationInterpolator_Jump"
ROUTE482.toField = "set_translation"
ROUTE482.toNode = "hanim_humanoid_root"

Scene13.children.append(ROUTE482)

X3D0.Scene = Scene13
f = open("././NancyNativeTags_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
