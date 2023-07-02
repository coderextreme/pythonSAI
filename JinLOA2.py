print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Immersive"
X3D0.version = "4.0"
head1 = x3d.head()
component2 = x3d.component()
component2.name = "HAnim"
component2.level = 1

head1.children.append(component2)
meta3 = x3d.meta()
meta3.name = "title"
meta3.content = "JinLOA2.x3d"

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.name = "creator"
meta4.content = "Jin Hoon Lee and Min Joo Lee"

head1.children.append(meta4)
meta5 = x3d.meta()
meta5.name = "translator"
meta5.content = "Chul Hee Jung and Myeong Won Lee"

head1.children.append(meta5)
meta6 = x3d.meta()
meta6.name = "created"
meta6.content = "31 March 2011"

head1.children.append(meta6)
meta7 = x3d.meta()
meta7.name = "translated"
meta7.content = "1 November 2014"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.name = "modified"
meta8.content = "23 December 2021"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "description"
meta9.content = "Articulated 3D game character designed with a general graphics tool, then converted into an X3D HAnim model."

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "reference"
meta10.content = "KoreanCharacter00ReadMe.txt"

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.name = "reference"
meta11.content = "KoreanCharacterHumanMotion_Infotech2014_140706.pdf"

head1.children.append(meta11)
meta12 = x3d.meta()
meta12.name = "reference"
meta12.content = "KoreanCharactersIllustrated.pdf"

head1.children.append(meta12)
meta13 = x3d.meta()
meta13.name = "identifier"
meta13.content = "https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Characters/JinLOA2.x3d"

head1.children.append(meta13)
meta14 = x3d.meta()
meta14.name = "generator"
meta14.content = "3DS MAX, http://www.autodesk.com/products/autodesk-3ds-max/overview"

head1.children.append(meta14)
meta15 = x3d.meta()
meta15.name = "generator"
meta15.content = "Suwon HAnim Converter"

head1.children.append(meta15)
meta16 = x3d.meta()
meta16.name = "generator"
meta16.content = "Gnu Image Manipulation Program, http://www.gimp.org"

head1.children.append(meta16)
meta17 = x3d.meta()
meta17.name = "generator"
meta17.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"

head1.children.append(meta17)
meta18 = x3d.meta()
meta18.name = "license"
meta18.content = "../license.html"

head1.children.append(meta18)

X3D0.head = head1
Scene19 = x3d.Scene()
WorldInfo20 = x3d.WorldInfo()
WorldInfo20.title = "JinLOA2.x3d"

Scene19.children.append(WorldInfo20)
NavigationInfo21 = x3d.NavigationInfo()
NavigationInfo21.speed = 1.5

Scene19.children.append(NavigationInfo21)
Viewpoint22 = x3d.Viewpoint()
Viewpoint22.centerOfRotation = [0,1,0]
Viewpoint22.description = "JinLOA2"
Viewpoint22.position = [0,1,3]

Scene19.children.append(Viewpoint22)
HAnimHumanoid23 = x3d.HAnimHumanoid()
HAnimHumanoid23.name = "JinLOA2"
HAnimHumanoid23.DEF = "hanim_JinLOA2"
HAnimHumanoid23.loa = 2
HAnimHumanoid23.scale = [0.0225,0.0225,0.0225]
HAnimHumanoid23.version = "2.0"
MetadataSet24 = x3d.MetadataSet()
MetadataSet24.name = "HAnimHumanoid.info"
MetadataSet24.reference = "https://www.web3d.org/documents/specifications/19774/V2.0/Architecture/ObjectInterfaces.html#Humanoid"
MetadataString25 = x3d.MetadataString()
MetadataString25.name = "authorName"
MetadataString25.value = ["Jin Hoon Lee and Min Joo Lee, Chul Hee Jung and Myeong Won Lee"]

if MetadataSet24.value is None:
    MetadataSet24.value = []
MetadataSet24.value.append(MetadataString25)
MetadataString26 = x3d.MetadataString()
MetadataString26.name = "authorEmail"
MetadataString26.value = ["myeongwonlee@gmail.com"]

if MetadataSet24.value is None:
    MetadataSet24.value = []
MetadataSet24.value.append(MetadataString26)
MetadataString27 = x3d.MetadataString()
MetadataString27.name = "creationDate"
MetadataString27.value = ["31 March 2011"]

if MetadataSet24.value is None:
    MetadataSet24.value = []
MetadataSet24.value.append(MetadataString27)
MetadataString28 = x3d.MetadataString()
MetadataString28.name = "gender"
MetadataString28.value = ["female"]

if MetadataSet24.value is None:
    MetadataSet24.value = []
MetadataSet24.value.append(MetadataString28)
MetadataFloat29 = x3d.MetadataFloat()
MetadataFloat29.name = "height"
MetadataFloat29.value = [1.5]

if MetadataSet24.value is None:
    MetadataSet24.value = []
MetadataSet24.value.append(MetadataFloat29)
MetadataString30 = x3d.MetadataString()
MetadataString30.name = "humanoidVersion"
MetadataString30.value = ["2.0"]

if MetadataSet24.value is None:
    MetadataSet24.value = []
MetadataSet24.value.append(MetadataString30)

HAnimHumanoid23.metadata = MetadataSet24
HAnimJoint31 = x3d.HAnimJoint()
HAnimJoint31.name = "humanoid_root"
HAnimJoint31.DEF = "hanim_humanoid_root"
HAnimJoint31.center = [0,35.799999,-0.7076]
HAnimJoint31.ulimit = [0,0,0]
HAnimJoint31.llimit = [0,0,0]
HAnimSegment32 = x3d.HAnimSegment()
HAnimSegment32.name = "sacrum"
HAnimSegment32.DEF = "hanim_sacrum"
Transform33 = x3d.Transform()
Transform33.translation = [0,35.799999,-0.7076]
Shape34 = x3d.Shape()
Appearance35 = x3d.Appearance()
Material36 = x3d.Material()
Material36.diffuseColor = [0.588,0.588,0.588]

Appearance35.material = Material36
ImageTexture37 = x3d.ImageTexture()
ImageTexture37.DEF = "JinLOA2TextureAtlas"
ImageTexture37.url = ["images/Jin.png","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Characters/images/Jin.png"]

Appearance35.texture = ImageTexture37

Shape34.appearance = Appearance35
IndexedFaceSet38 = x3d.IndexedFaceSet()
IndexedFaceSet38.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,5,-1,0,5,6,-1,0,6,7,-1,0,7,8,-1,0,8,9,-1,0,9,10,-1,0,10,11,-1,0,11,12,-1,0,12,1,-1,14,2,1,-1,1,13,14,-1,15,3,2,-1,2,14,15,-1,16,4,3,-1,3,15,16,-1,17,5,4,-1,4,16,17,-1,18,6,5,-1,5,17,18,-1,19,7,6,-1,6,18,19,-1,20,8,7,-1,7,19,20,-1,21,9,8,-1,8,20,21,-1,22,10,9,-1,9,21,22,-1,23,11,10,-1,10,22,23,-1,24,12,11,-1,11,23,24,-1,13,1,12,-1,12,24,13,-1,26,14,13,-1,13,25,26,-1,27,15,14,-1,14,26,27,-1,28,16,15,-1,15,27,28,-1,29,17,16,-1,16,28,29,-1,30,18,17,-1,17,29,30,-1,31,19,18,-1,18,30,31,-1,32,20,19,-1,19,31,32,-1,33,21,20,-1,20,32,33,-1,34,22,21,-1,21,33,34,-1,35,23,22,-1,22,34,35,-1,36,24,23,-1,23,35,36,-1,25,13,24,-1,24,36,25,-1,38,26,25,-1,25,37,38,-1,39,27,26,-1,26,38,39,-1,40,28,27,-1,27,39,40,-1,41,29,28,-1,28,40,41,-1,42,30,29,-1,29,41,42,-1,43,31,30,-1,30,42,43,-1,44,32,31,-1,31,43,44,-1,45,33,32,-1,32,44,45,-1,46,34,33,-1,33,45,46,-1,47,35,34,-1,34,46,47,-1,48,36,35,-1,35,47,48,-1,37,25,36,-1,36,48,37,-1,50,38,37,-1,37,49,50,-1,51,39,38,-1,38,50,51,-1,52,40,39,-1,39,51,52,-1,53,41,40,-1,40,52,53,-1,54,42,41,-1,41,53,54,-1,55,43,42,-1,42,54,55,-1,56,44,43,-1,43,55,56,-1,57,45,44,-1,44,56,57,-1,58,46,45,-1,45,57,58,-1,59,47,46,-1,46,58,59,-1,60,48,47,-1,47,59,60,-1,49,37,48,-1,48,60,49,-1,61,50,49,-1,61,51,50,-1,61,52,51,-1,61,53,52,-1,61,54,53,-1,61,55,54,-1,61,56,55,-1,61,57,56,-1,61,58,57,-1,61,59,58,-1,61,60,59,-1,61,49,60,-1]
IndexedFaceSet38.creaseAngle = 3.14159
IndexedFaceSet38.texCoordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,5,-1,0,5,6,-1,0,6,7,-1,0,7,8,-1,0,8,9,-1,0,9,10,-1,0,10,11,-1,0,11,12,-1,0,12,1,-1,14,2,1,-1,1,13,14,-1,15,3,2,-1,2,14,15,-1,16,4,3,-1,3,15,16,-1,17,5,4,-1,4,16,17,-1,18,6,5,-1,5,17,18,-1,19,7,6,-1,6,18,19,-1,20,8,7,-1,7,19,20,-1,21,9,8,-1,8,20,21,-1,22,10,9,-1,9,21,22,-1,23,11,10,-1,10,22,23,-1,24,12,11,-1,11,23,24,-1,13,1,12,-1,12,24,13,-1,26,14,13,-1,13,25,26,-1,27,15,14,-1,14,26,27,-1,28,16,15,-1,15,27,28,-1,29,17,16,-1,16,28,29,-1,30,18,17,-1,17,29,30,-1,31,19,18,-1,18,30,31,-1,32,20,19,-1,19,31,32,-1,33,21,20,-1,20,32,33,-1,34,22,21,-1,21,33,34,-1,35,23,22,-1,22,34,35,-1,36,24,23,-1,23,35,36,-1,25,13,24,-1,24,36,25,-1,38,26,25,-1,25,37,38,-1,39,27,26,-1,26,38,39,-1,40,28,27,-1,27,39,40,-1,41,29,28,-1,28,40,41,-1,42,30,29,-1,29,41,42,-1,43,31,30,-1,30,42,43,-1,44,32,31,-1,31,43,44,-1,45,33,32,-1,32,44,45,-1,46,34,33,-1,33,45,46,-1,47,35,34,-1,34,46,47,-1,48,36,35,-1,35,47,48,-1,37,25,36,-1,36,48,37,-1,50,38,37,-1,37,49,50,-1,51,39,38,-1,38,50,51,-1,52,40,39,-1,39,51,52,-1,53,41,40,-1,40,52,53,-1,54,42,41,-1,41,53,54,-1,55,43,42,-1,42,54,55,-1,56,44,43,-1,43,55,56,-1,57,45,44,-1,44,56,57,-1,58,46,45,-1,45,57,58,-1,59,47,46,-1,46,58,59,-1,60,48,47,-1,47,59,60,-1,49,37,48,-1,48,60,49,-1,61,50,49,-1,61,51,50,-1,61,52,51,-1,61,53,52,-1,61,54,53,-1,61,55,54,-1,61,56,55,-1,61,57,56,-1,61,58,57,-1,61,59,58,-1,61,60,59,-1,61,49,60,-1]
Coordinate39 = x3d.Coordinate()

IndexedFaceSet38.coord = Coordinate39
TextureCoordinate40 = x3d.TextureCoordinate()

IndexedFaceSet38.texCoord = TextureCoordinate40

Shape34.geometry = IndexedFaceSet38

Transform33.children.append(Shape34)

HAnimSegment32.children.append(Transform33)

HAnimJoint31.children.append(HAnimSegment32)
HAnimJoint41 = x3d.HAnimJoint()
HAnimJoint41.name = "sacroiliac"
HAnimJoint41.DEF = "hanim_sacroiliac"
HAnimJoint41.center = [0,30.530001,-0.7076]
HAnimJoint41.ulimit = [0,0,0]
HAnimJoint41.llimit = [0,0,0]
HAnimSegment42 = x3d.HAnimSegment()
HAnimSegment42.name = "pelvis"
HAnimSegment42.DEF = "hanim_pelvis"
Transform43 = x3d.Transform()
Transform43.translation = [0,30.530001,-0.7076]
Shape44 = x3d.Shape()
Appearance45 = x3d.Appearance()
Material46 = x3d.Material()
Material46.diffuseColor = [0.588,0.588,0.588]

Appearance45.material = Material46
ImageTexture47 = x3d.ImageTexture()
ImageTexture47.USE = "JinLOA2TextureAtlas"

Appearance45.texture = ImageTexture47

Shape44.appearance = Appearance45
IndexedFaceSet48 = x3d.IndexedFaceSet()
IndexedFaceSet48.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,5,-1,0,5,6,-1,0,6,7,-1,0,7,8,-1,0,8,9,-1,0,9,10,-1,0,10,11,-1,0,11,12,-1,0,12,1,-1,14,2,1,-1,1,13,14,-1,15,3,2,-1,2,14,15,-1,16,4,3,-1,3,15,16,-1,17,5,4,-1,4,16,17,-1,18,6,5,-1,5,17,18,-1,19,7,6,-1,6,18,19,-1,20,8,7,-1,7,19,20,-1,21,9,8,-1,8,20,21,-1,22,10,9,-1,9,21,22,-1,23,11,10,-1,10,22,23,-1,24,12,11,-1,11,23,24,-1,13,1,12,-1,12,24,13,-1,26,14,13,-1,13,25,26,-1,27,15,14,-1,14,26,27,-1,28,16,15,-1,15,27,28,-1,29,17,16,-1,16,28,29,-1,30,18,17,-1,17,29,30,-1,31,19,18,-1,18,30,31,-1,32,20,19,-1,19,31,32,-1,33,21,20,-1,20,32,33,-1,34,22,21,-1,21,33,34,-1,35,23,22,-1,22,34,35,-1,36,24,23,-1,23,35,36,-1,25,13,24,-1,24,36,25,-1,38,26,25,-1,25,37,38,-1,39,27,26,-1,26,38,39,-1,40,28,27,-1,27,39,40,-1,41,29,28,-1,28,40,41,-1,42,30,29,-1,29,41,42,-1,43,31,30,-1,30,42,43,-1,44,32,31,-1,31,43,44,-1,45,33,32,-1,32,44,45,-1,46,34,33,-1,33,45,46,-1,47,35,34,-1,34,46,47,-1,48,36,35,-1,35,47,48,-1,37,25,36,-1,36,48,37,-1,50,38,37,-1,37,49,50,-1,51,39,38,-1,38,50,51,-1,52,40,39,-1,39,51,52,-1,53,41,40,-1,40,52,53,-1,54,42,41,-1,41,53,54,-1,55,43,42,-1,42,54,55,-1,56,44,43,-1,43,55,56,-1,57,45,44,-1,44,56,57,-1,58,46,45,-1,45,57,58,-1,59,47,46,-1,46,58,59,-1,60,48,47,-1,47,59,60,-1,49,37,48,-1,48,60,49,-1,61,50,49,-1,61,51,50,-1,61,52,51,-1,61,53,52,-1,61,54,53,-1,61,55,54,-1,61,56,55,-1,61,57,56,-1,61,58,57,-1,61,59,58,-1,61,60,59,-1,61,49,60,-1]
IndexedFaceSet48.creaseAngle = 3.14159
IndexedFaceSet48.texCoordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,5,-1,0,5,6,-1,0,6,7,-1,0,7,8,-1,0,8,9,-1,0,9,10,-1,0,10,11,-1,0,11,12,-1,0,12,1,-1,14,2,1,-1,1,13,14,-1,15,3,2,-1,2,14,15,-1,16,4,3,-1,3,15,16,-1,17,5,4,-1,4,16,17,-1,18,6,5,-1,5,17,18,-1,19,7,6,-1,6,18,19,-1,20,8,7,-1,7,19,20,-1,21,9,8,-1,8,20,21,-1,22,10,9,-1,9,21,22,-1,23,11,10,-1,10,22,23,-1,24,12,11,-1,11,23,24,-1,13,1,12,-1,12,24,13,-1,26,14,13,-1,13,25,26,-1,27,15,14,-1,14,26,27,-1,28,16,15,-1,15,27,28,-1,29,17,16,-1,16,28,29,-1,30,18,17,-1,17,29,30,-1,31,19,18,-1,18,30,31,-1,32,20,19,-1,19,31,32,-1,33,21,20,-1,20,32,33,-1,34,22,21,-1,21,33,34,-1,35,23,22,-1,22,34,35,-1,36,24,23,-1,23,35,36,-1,25,13,24,-1,24,36,25,-1,38,26,25,-1,25,37,38,-1,39,27,26,-1,26,38,39,-1,40,28,27,-1,27,39,40,-1,41,29,28,-1,28,40,41,-1,42,30,29,-1,29,41,42,-1,43,31,30,-1,30,42,43,-1,44,32,31,-1,31,43,44,-1,45,33,32,-1,32,44,45,-1,46,34,33,-1,33,45,46,-1,47,35,34,-1,34,46,47,-1,48,36,35,-1,35,47,48,-1,37,25,36,-1,36,48,37,-1,50,38,37,-1,37,49,50,-1,51,39,38,-1,38,50,51,-1,52,40,39,-1,39,51,52,-1,53,41,40,-1,40,52,53,-1,54,42,41,-1,41,53,54,-1,55,43,42,-1,42,54,55,-1,56,44,43,-1,43,55,56,-1,57,45,44,-1,44,56,57,-1,58,46,45,-1,45,57,58,-1,59,47,46,-1,46,58,59,-1,60,48,47,-1,47,59,60,-1,49,37,48,-1,48,60,49,-1,61,50,49,-1,61,51,50,-1,61,52,51,-1,61,53,52,-1,61,54,53,-1,61,55,54,-1,61,56,55,-1,61,57,56,-1,61,58,57,-1,61,59,58,-1,61,60,59,-1,61,49,60,-1]
Coordinate49 = x3d.Coordinate()

IndexedFaceSet48.coord = Coordinate49
TextureCoordinate50 = x3d.TextureCoordinate()

IndexedFaceSet48.texCoord = TextureCoordinate50

Shape44.geometry = IndexedFaceSet48

Transform43.children.append(Shape44)

HAnimSegment42.children.append(Transform43)

HAnimJoint41.children.append(HAnimSegment42)
HAnimJoint51 = x3d.HAnimJoint()
HAnimJoint51.name = "l_hip"
HAnimJoint51.DEF = "hanim_l_hip"
HAnimJoint51.center = [4.207,35.830002,-0.8155]
HAnimJoint51.ulimit = [0,0,0]
HAnimJoint51.llimit = [0,0,0]
HAnimSegment52 = x3d.HAnimSegment()
HAnimSegment52.name = "l_thigh"
HAnimSegment52.DEF = "hanim_l_thigh"
Transform53 = x3d.Transform()
Transform53.translation = [4.207,35.830002,-0.8155]
Shape54 = x3d.Shape()
Appearance55 = x3d.Appearance()
Material56 = x3d.Material()
Material56.diffuseColor = [0.588,0.588,0.588]

Appearance55.material = Material56
ImageTexture57 = x3d.ImageTexture()
ImageTexture57.USE = "JinLOA2TextureAtlas"

Appearance55.texture = ImageTexture57

Shape54.appearance = Appearance55
IndexedFaceSet58 = x3d.IndexedFaceSet()
IndexedFaceSet58.coordIndex = [47,46,45,-1,45,44,43,-1,45,43,42,-1,47,45,42,-1,48,47,42,-1,0,1,8,-1,8,7,0,-1,1,2,9,-1,9,8,1,-1,2,3,10,-1,10,9,2,-1,3,4,11,-1,11,10,3,-1,4,5,12,-1,12,11,4,-1,5,6,13,-1,13,12,5,-1,6,0,7,-1,7,13,6,-1,7,8,15,-1,15,14,7,-1,8,9,16,-1,16,15,8,-1,9,10,17,-1,17,16,9,-1,10,11,18,-1,18,17,10,-1,11,12,19,-1,19,18,11,-1,12,13,20,-1,20,19,12,-1,13,7,14,-1,14,20,13,-1,14,15,22,-1,22,21,14,-1,15,16,23,-1,23,22,15,-1,16,17,24,-1,24,23,16,-1,17,18,25,-1,25,24,17,-1,18,19,26,-1,26,25,18,-1,19,20,27,-1,27,26,19,-1,20,14,21,-1,21,27,20,-1,56,57,58,-1,58,59,60,-1,58,60,61,-1,56,58,61,-1,62,56,61,-1,29,28,21,-1,21,22,29,-1,30,29,22,-1,22,23,30,-1,31,30,23,-1,23,24,31,-1,32,31,24,-1,24,25,32,-1,33,32,25,-1,25,26,33,-1,34,33,26,-1,26,27,34,-1,28,34,27,-1,27,21,28,-1,36,35,28,-1,28,29,36,-1,37,36,29,-1,29,30,37,-1,38,37,30,-1,30,31,38,-1,39,38,31,-1,31,32,39,-1,40,39,32,-1,32,33,40,-1,41,40,33,-1,33,34,41,-1,35,41,34,-1,34,28,35,-1,42,43,1,-1,1,0,42,-1,43,44,2,-1,2,1,43,-1,44,45,3,-1,3,2,44,-1,45,46,4,-1,4,3,45,-1,46,47,5,-1,5,4,46,-1,47,48,6,-1,6,5,47,-1,48,42,0,-1,0,6,48,-1,50,49,35,-1,35,36,50,-1,51,50,36,-1,36,37,51,-1,52,51,37,-1,37,38,52,-1,53,52,38,-1,38,39,53,-1,54,53,39,-1,39,40,54,-1,55,54,40,-1,40,41,55,-1,49,55,41,-1,41,35,49,-1,57,56,49,-1,49,50,57,-1,58,57,50,-1,50,51,58,-1,59,58,51,-1,51,52,59,-1,60,59,52,-1,52,53,60,-1,61,60,53,-1,53,54,61,-1,62,61,54,-1,54,55,62,-1,56,62,55,-1,55,49,56,-1]
IndexedFaceSet58.creaseAngle = 3.14159
IndexedFaceSet58.texCoordIndex = [5,4,3,-1,3,2,0,-1,3,0,1,-1,5,3,1,-1,6,5,1,-1,7,10,8,-1,8,9,7,-1,10,12,11,-1,11,8,10,-1,12,14,13,-1,13,11,12,-1,14,16,15,-1,15,13,14,-1,16,18,17,-1,17,15,16,-1,18,20,19,-1,19,17,18,-1,20,7,9,-1,9,19,20,-1,9,8,21,-1,21,22,9,-1,8,11,23,-1,23,21,8,-1,11,13,24,-1,24,23,11,-1,13,15,25,-1,25,24,13,-1,15,17,26,-1,26,25,15,-1,17,19,27,-1,27,26,17,-1,19,9,22,-1,22,27,19,-1,22,21,28,-1,28,29,22,-1,21,23,30,-1,30,28,21,-1,23,24,31,-1,31,30,23,-1,24,25,32,-1,32,31,24,-1,25,26,33,-1,33,32,25,-1,26,27,34,-1,34,33,26,-1,27,22,29,-1,29,34,27,-1,42,43,44,-1,44,45,46,-1,44,46,47,-1,42,44,47,-1,48,42,47,-1,35,36,29,-1,29,28,35,-1,37,35,28,-1,28,30,37,-1,38,37,30,-1,30,31,38,-1,39,38,31,-1,31,32,39,-1,40,39,32,-1,32,33,40,-1,41,40,33,-1,33,34,41,-1,36,41,34,-1,34,29,36,-1,51,52,49,-1,49,50,51,-1,54,51,50,-1,50,53,54,-1,56,54,53,-1,53,55,56,-1,58,56,55,-1,55,57,58,-1,60,58,57,-1,57,59,60,-1,62,60,59,-1,59,61,62,-1,52,62,61,-1,61,49,52,-1,1,0,10,-1,10,7,1,-1,0,2,12,-1,12,10,0,-1,2,3,14,-1,14,12,2,-1,3,4,16,-1,16,14,3,-1,4,5,18,-1,18,16,4,-1,5,6,20,-1,20,18,5,-1,6,1,7,-1,7,20,6,-1,63,64,52,-1,52,51,63,-1,65,63,51,-1,51,54,65,-1,66,65,54,-1,54,56,66,-1,67,66,56,-1,56,58,67,-1,68,67,58,-1,58,60,68,-1,69,68,60,-1,60,62,69,-1,64,69,62,-1,62,52,64,-1,43,42,64,-1,64,63,43,-1,44,43,63,-1,63,65,44,-1,45,44,65,-1,65,66,45,-1,46,45,66,-1,66,67,46,-1,47,46,67,-1,67,68,47,-1,48,47,68,-1,68,69,48,-1,42,48,69,-1,69,64,42,-1]
Coordinate59 = x3d.Coordinate()

IndexedFaceSet58.coord = Coordinate59
TextureCoordinate60 = x3d.TextureCoordinate()

IndexedFaceSet58.texCoord = TextureCoordinate60

Shape54.geometry = IndexedFaceSet58

Transform53.children.append(Shape54)

HAnimSegment52.children.append(Transform53)

HAnimJoint51.children.append(HAnimSegment52)
HAnimJoint61 = x3d.HAnimJoint()
HAnimJoint61.name = "l_knee"
HAnimJoint61.DEF = "hanim_l_knee"
HAnimJoint61.center = [4.116,17.26,-0.8639]
HAnimJoint61.ulimit = [0,0,0]
HAnimJoint61.llimit = [0,0,0]
HAnimSegment62 = x3d.HAnimSegment()
HAnimSegment62.name = "l_calf"
HAnimSegment62.DEF = "hanim_l_calf"
Transform63 = x3d.Transform()
Transform63.translation = [4.116,17.26,-0.8639]
Shape64 = x3d.Shape()
Appearance65 = x3d.Appearance()
Material66 = x3d.Material()
Material66.diffuseColor = [0.588,0.588,0.588]

Appearance65.material = Material66
ImageTexture67 = x3d.ImageTexture()
ImageTexture67.USE = "JinLOA2TextureAtlas"

Appearance65.texture = ImageTexture67

Shape64.appearance = Appearance65
IndexedFaceSet68 = x3d.IndexedFaceSet()
IndexedFaceSet68.coordIndex = [4,3,2,-1,5,4,2,-1,2,1,0,-1,5,2,0,-1,6,5,0,-1,9,8,7,-1,7,10,9,-1,12,11,8,-1,8,9,12,-1,14,13,11,-1,11,12,14,-1,16,15,13,-1,13,14,16,-1,18,17,15,-1,15,16,18,-1,20,19,17,-1,17,18,20,-1,10,7,19,-1,19,20,10,-1,21,9,10,-1,10,22,21,-1,23,12,9,-1,9,21,23,-1,24,14,12,-1,12,23,24,-1,25,16,14,-1,14,24,25,-1,26,18,16,-1,16,25,26,-1,27,20,18,-1,18,26,27,-1,22,10,20,-1,20,27,22,-1,1,21,22,-1,22,0,1,-1,2,23,21,-1,21,1,2,-1,3,24,23,-1,23,2,3,-1,4,25,24,-1,24,3,4,-1,5,26,25,-1,25,4,5,-1,6,27,26,-1,26,5,6,-1,0,22,27,-1,27,6,0,-1,8,29,28,-1,28,7,8,-1,11,30,29,-1,29,8,11,-1,13,31,30,-1,30,11,13,-1,15,32,31,-1,31,13,15,-1,17,33,32,-1,32,15,17,-1,19,34,33,-1,33,17,19,-1,7,28,34,-1,34,19,7,-1,29,36,35,-1,35,28,29,-1,30,37,36,-1,36,29,30,-1,31,38,37,-1,37,30,31,-1,32,39,38,-1,38,31,32,-1,33,40,39,-1,39,32,33,-1,34,41,40,-1,40,33,34,-1,28,35,41,-1,41,34,28,-1]
IndexedFaceSet68.creaseAngle = 3.14159
IndexedFaceSet68.texCoordIndex = [4,3,2,-1,5,4,2,-1,2,1,0,-1,5,2,0,-1,6,5,0,-1,9,8,7,-1,7,10,9,-1,12,11,8,-1,8,9,12,-1,14,13,11,-1,11,12,14,-1,16,15,13,-1,13,14,16,-1,18,17,15,-1,15,16,18,-1,20,19,17,-1,17,18,20,-1,10,7,19,-1,19,20,10,-1,21,9,10,-1,10,22,21,-1,23,12,9,-1,9,21,23,-1,24,14,12,-1,12,23,24,-1,25,16,14,-1,14,24,25,-1,26,18,16,-1,16,25,26,-1,27,20,18,-1,18,26,27,-1,22,10,20,-1,20,27,22,-1,1,21,22,-1,22,0,1,-1,2,23,21,-1,21,1,2,-1,3,24,23,-1,23,2,3,-1,4,25,24,-1,24,3,4,-1,5,26,25,-1,25,4,5,-1,6,27,26,-1,26,5,6,-1,0,22,27,-1,27,6,0,-1,8,29,28,-1,28,7,8,-1,11,30,29,-1,29,8,11,-1,13,31,30,-1,30,11,13,-1,15,32,31,-1,31,13,15,-1,17,33,32,-1,32,15,17,-1,19,34,33,-1,33,17,19,-1,7,28,34,-1,34,19,7,-1,29,36,35,-1,35,28,29,-1,30,37,36,-1,36,29,30,-1,31,38,37,-1,37,30,31,-1,32,39,38,-1,38,31,32,-1,33,40,39,-1,39,32,33,-1,34,41,40,-1,40,33,34,-1,28,35,41,-1,41,34,28,-1]
Coordinate69 = x3d.Coordinate()

IndexedFaceSet68.coord = Coordinate69
TextureCoordinate70 = x3d.TextureCoordinate()

IndexedFaceSet68.texCoord = TextureCoordinate70

Shape64.geometry = IndexedFaceSet68

Transform63.children.append(Shape64)

HAnimSegment62.children.append(Transform63)

HAnimJoint61.children.append(HAnimSegment62)
HAnimJoint71 = x3d.HAnimJoint()
HAnimJoint71.name = "l_talocrural"
HAnimJoint71.DEF = "hanim_l_talocrural"
HAnimJoint71.center = [3.854,3.939,-0.7038]
HAnimJoint71.ulimit = [0,0,0]
HAnimJoint71.llimit = [0,0,0]
HAnimSegment72 = x3d.HAnimSegment()
HAnimSegment72.name = "l_talus"
HAnimSegment72.DEF = "hanim_l_talus"
Transform73 = x3d.Transform()
Transform73.translation = [3.854,3.939,-0.7038]
Shape74 = x3d.Shape()
Appearance75 = x3d.Appearance()
Material76 = x3d.Material()
Material76.diffuseColor = [0.588,0.588,0.588]

Appearance75.material = Material76
ImageTexture77 = x3d.ImageTexture()
ImageTexture77.USE = "JinLOA2TextureAtlas"

Appearance75.texture = ImageTexture77

Shape74.appearance = Appearance75
IndexedFaceSet78 = x3d.IndexedFaceSet()
IndexedFaceSet78.coordIndex = [1,11,14,-1,3,4,5,-1,5,6,3,-1,1,0,4,-1,4,3,1,-1,0,2,5,-1,5,4,0,-1,11,1,3,-1,3,6,11,-1,15,2,0,-1,0,12,15,-1,0,1,13,-1,13,12,0,-1,13,1,14,-1,7,18,11,-1,8,6,5,-1,5,9,8,-1,7,8,9,-1,9,10,7,-1,10,9,5,-1,5,2,10,-1,11,6,8,-1,8,7,11,-1,15,16,10,-1,10,2,15,-1,10,16,17,-1,17,7,10,-1,17,18,7,-1,21,22,23,-1,23,24,25,-1,25,26,19,-1,23,25,19,-1,21,23,19,-1,20,21,19,-1,15,12,20,-1,20,19,15,-1,12,13,21,-1,21,20,12,-1,13,14,22,-1,22,21,13,-1,14,11,23,-1,23,22,14,-1,11,18,24,-1,24,23,11,-1,18,17,25,-1,25,24,18,-1,17,16,26,-1,26,25,17,-1,16,15,19,-1,19,26,16,-1]
IndexedFaceSet78.creaseAngle = 3.14159
IndexedFaceSet78.texCoordIndex = [1,14,18,-1,3,4,5,-1,5,6,3,-1,1,0,4,-1,4,3,1,-1,0,2,5,-1,5,4,0,-1,14,1,3,-1,3,6,14,-1,19,2,0,-1,0,16,19,-1,0,1,17,-1,17,16,0,-1,17,1,18,-1,7,23,15,-1,9,8,11,-1,11,10,9,-1,7,9,10,-1,10,12,7,-1,12,10,11,-1,11,13,12,-1,15,8,9,-1,9,7,15,-1,20,21,12,-1,12,13,20,-1,12,21,22,-1,22,7,12,-1,22,23,7,-1,26,27,28,-1,28,29,30,-1,30,31,24,-1,28,30,24,-1,26,28,24,-1,25,26,24,-1,19,16,25,-1,25,24,19,-1,16,17,26,-1,26,25,16,-1,17,18,27,-1,27,26,17,-1,18,14,28,-1,28,27,18,-1,15,23,29,-1,29,28,15,-1,23,22,30,-1,30,29,23,-1,22,21,31,-1,31,30,22,-1,21,20,24,-1,24,31,21,-1]
Coordinate79 = x3d.Coordinate()

IndexedFaceSet78.coord = Coordinate79
TextureCoordinate80 = x3d.TextureCoordinate()

IndexedFaceSet78.texCoord = TextureCoordinate80

Shape74.geometry = IndexedFaceSet78

Transform73.children.append(Shape74)

HAnimSegment72.children.append(Transform73)

HAnimJoint71.children.append(HAnimSegment72)
HAnimJoint81 = x3d.HAnimJoint()
HAnimJoint81.name = "l_tarsometatarsal_2"
HAnimJoint81.DEF = "hanim_l_tarsometatarsal_2"
HAnimJoint81.center = [3.854,3.336,-1.514]
HAnimJoint81.ulimit = [0,0,0]
HAnimJoint81.llimit = [0,0,0]
HAnimSegment82 = x3d.HAnimSegment()
HAnimSegment82.name = "l_metatarsal_2"
HAnimSegment82.DEF = "hanim_l_metatarsal_2"
Transform83 = x3d.Transform()
Transform83.translation = [3.854,3.336,-1.514]
Shape84 = x3d.Shape()
Appearance85 = x3d.Appearance()
Material86 = x3d.Material()
Material86.diffuseColor = [0.588,0.588,0.588]

Appearance85.material = Material86
ImageTexture87 = x3d.ImageTexture()
ImageTexture87.USE = "JinLOA2TextureAtlas"

Appearance85.texture = ImageTexture87

Shape84.appearance = Appearance85
IndexedFaceSet88 = x3d.IndexedFaceSet()
IndexedFaceSet88.coordIndex = [6,4,3,-1,3,0,6,-1,9,0,3,-1,3,11,9,-1,2,6,0,-1,0,1,2,-1,10,1,0,-1,0,9,10,-1,1,10,15,-1,15,2,1,-1,6,5,7,-1,7,4,6,-1,12,13,7,-1,7,5,12,-1,2,8,5,-1,5,6,2,-1,14,12,5,-1,5,8,14,-1,8,2,15,-1,15,14,8,-1,17,18,19,-1,17,19,20,-1,17,20,16,-1,24,25,26,-1,27,21,22,-1,26,27,22,-1,24,26,22,-1,24,22,23,-1,3,4,17,-1,17,16,3,-1,4,7,18,-1,18,17,4,-1,7,13,19,-1,19,18,7,-1,13,11,20,-1,20,19,13,-1,11,3,16,-1,16,20,11,-1,10,9,22,-1,22,21,10,-1,9,11,23,-1,23,22,9,-1,11,13,24,-1,24,23,11,-1,13,12,25,-1,25,24,13,-1,12,14,26,-1,26,25,12,-1,14,15,27,-1,27,26,14,-1,15,10,21,-1,21,27,15,-1]
IndexedFaceSet88.creaseAngle = 3.14159
IndexedFaceSet88.texCoordIndex = [2,6,5,-1,5,0,2,-1,14,0,5,-1,5,16,14,-1,3,2,0,-1,0,1,3,-1,15,1,0,-1,0,14,15,-1,1,15,21,-1,21,4,1,-1,8,7,10,-1,10,9,8,-1,17,18,10,-1,10,7,17,-1,12,11,7,-1,7,8,12,-1,19,17,7,-1,7,11,19,-1,11,13,20,-1,20,19,11,-1,23,24,25,-1,23,25,26,-1,23,26,22,-1,30,31,32,-1,33,27,28,-1,32,33,28,-1,30,32,28,-1,30,28,29,-1,5,6,23,-1,23,22,5,-1,9,10,24,-1,24,23,9,-1,10,18,25,-1,25,24,10,-1,18,16,26,-1,26,25,18,-1,16,5,22,-1,22,26,16,-1,15,14,28,-1,28,27,15,-1,14,16,29,-1,29,28,14,-1,16,18,30,-1,30,29,16,-1,18,17,31,-1,31,30,18,-1,17,19,32,-1,32,31,17,-1,19,20,33,-1,33,32,19,-1,21,15,27,-1,27,33,21,-1]
Coordinate89 = x3d.Coordinate()

IndexedFaceSet88.coord = Coordinate89
TextureCoordinate90 = x3d.TextureCoordinate()

IndexedFaceSet88.texCoord = TextureCoordinate90

Shape84.geometry = IndexedFaceSet88

Transform83.children.append(Shape84)

HAnimSegment82.children.append(Transform83)

HAnimJoint81.children.append(HAnimSegment82)
HAnimJoint91 = x3d.HAnimJoint()
HAnimJoint91.name = "l_metatarsophalangeal_2"
HAnimJoint91.DEF = "hanim_l_metatarsophalangeal_2"
HAnimJoint91.center = [3.854,3.64,0.7402]
HAnimJoint91.ulimit = [0,0,0]
HAnimJoint91.llimit = [0,0,0]
HAnimSegment92 = x3d.HAnimSegment()
HAnimSegment92.name = "l_tarsal_proximal_phalanx_2"
HAnimSegment92.DEF = "hanim_l_tarsal_proximal_phalanx_2"
Transform93 = x3d.Transform()
Transform93.translation = [3.854,3.64,0.7402]
Shape94 = x3d.Shape()
Appearance95 = x3d.Appearance()
Material96 = x3d.Material()
Material96.diffuseColor = [0.588,0.588,0.588]

Appearance95.material = Material96
ImageTexture97 = x3d.ImageTexture()
ImageTexture97.USE = "JinLOA2TextureAtlas"

Appearance95.texture = ImageTexture97

Shape94.appearance = Appearance95
IndexedFaceSet98 = x3d.IndexedFaceSet()
IndexedFaceSet98.coordIndex = [3,4,10,-1,3,10,11,-1,0,3,11,-1,1,0,11,-1,11,12,1,-1,1,12,16,-1,16,9,1,-1,2,17,10,-1,10,4,2,-1,13,8,6,-1,14,13,6,-1,5,14,6,-1,7,15,14,-1,14,5,7,-1,7,9,16,-1,16,15,7,-1,2,8,13,-1,13,17,2,-1,20,21,22,-1,20,22,23,-1,20,23,24,-1,19,20,24,-1,19,24,18,-1,26,27,28,-1,28,29,30,-1,26,28,30,-1,26,30,31,-1,26,31,32,-1,26,32,25,-1,0,1,19,-1,19,18,0,-1,1,9,20,-1,20,19,1,-1,9,7,21,-1,21,20,9,-1,7,5,22,-1,22,21,7,-1,5,6,23,-1,23,22,5,-1,6,3,24,-1,24,23,6,-1,3,0,18,-1,18,24,3,-1,11,10,26,-1,26,25,11,-1,10,17,27,-1,27,26,10,-1,17,13,28,-1,28,27,17,-1,13,14,29,-1,29,28,13,-1,14,15,30,-1,30,29,14,-1,15,16,31,-1,31,30,15,-1,16,12,32,-1,32,31,16,-1,12,11,25,-1,25,32,12,-1,6,8,2,-1,3,6,2,-1,4,3,2,-1]
IndexedFaceSet98.creaseAngle = 3.14159
IndexedFaceSet98.texCoordIndex = [4,5,12,-1,4,12,13,-1,0,4,13,-1,1,0,13,-1,13,14,1,-1,1,14,19,-1,19,3,1,-1,2,21,12,-1,12,5,2,-1,15,10,7,-1,16,15,7,-1,6,16,7,-1,8,17,16,-1,16,6,8,-1,8,11,18,-1,18,17,8,-1,9,10,15,-1,15,20,9,-1,24,25,26,-1,24,26,27,-1,24,27,28,-1,23,24,28,-1,23,28,22,-1,30,31,32,-1,32,33,34,-1,30,32,34,-1,30,34,35,-1,30,35,36,-1,30,36,29,-1,0,1,23,-1,23,22,0,-1,1,3,24,-1,24,23,1,-1,11,8,25,-1,25,24,11,-1,8,6,26,-1,26,25,8,-1,6,7,27,-1,27,26,6,-1,7,4,28,-1,28,27,7,-1,4,0,22,-1,22,28,4,-1,13,12,30,-1,30,29,13,-1,12,21,31,-1,31,30,12,-1,20,15,32,-1,32,31,20,-1,15,16,33,-1,33,32,15,-1,16,17,34,-1,34,33,16,-1,17,18,35,-1,35,34,17,-1,19,14,36,-1,36,35,19,-1,14,13,29,-1,29,36,14,-1,7,10,9,-1,4,7,9,-1,5,4,9,-1]
Coordinate99 = x3d.Coordinate()

IndexedFaceSet98.coord = Coordinate99
TextureCoordinate100 = x3d.TextureCoordinate()

IndexedFaceSet98.texCoord = TextureCoordinate100

Shape94.geometry = IndexedFaceSet98

Transform93.children.append(Shape94)

HAnimSegment92.children.append(Transform93)

HAnimJoint91.children.append(HAnimSegment92)
HAnimJoint101 = x3d.HAnimJoint()
HAnimJoint101.name = "l_tarsal_distal_interphalangeal_2"
HAnimJoint101.DEF = "hanim_l_tarsal_distal_interphalangeal_2"
HAnimJoint101.center = [3.854,1.956,1.682]
HAnimJoint101.ulimit = [0,0,0]
HAnimJoint101.llimit = [0,0,0]
HAnimSegment102 = x3d.HAnimSegment()
HAnimSegment102.name = "l_tarsal_distal_phalanx_2"
HAnimSegment102.DEF = "hanim_l_tarsal_distal_phalanx_2"
Transform103 = x3d.Transform()
Transform103.translation = [3.854,1.956,1.682]
Shape104 = x3d.Shape()
Appearance105 = x3d.Appearance()
Material106 = x3d.Material()
Material106.diffuseColor = [0.588,0.588,0.588]

Appearance105.material = Material106
ImageTexture107 = x3d.ImageTexture()
ImageTexture107.USE = "JinLOA2TextureAtlas"

Appearance105.texture = ImageTexture107

Shape104.appearance = Appearance105
IndexedFaceSet108 = x3d.IndexedFaceSet()
IndexedFaceSet108.coordIndex = [3,1,0,-1,0,4,3,-1,10,2,1,-1,1,3,10,-1,2,10,15,-1,0,1,6,-1,6,5,0,-1,6,1,2,-1,2,7,6,-1,7,2,15,-1,15,16,7,-1,17,4,0,-1,0,5,17,-1,3,4,9,-1,9,8,3,-1,10,3,8,-1,8,11,10,-1,11,15,10,-1,9,12,13,-1,13,8,9,-1,13,14,11,-1,11,8,13,-1,14,16,15,-1,15,11,14,-1,17,12,9,-1,9,4,17,-1,19,20,21,-1,21,22,23,-1,23,24,25,-1,21,23,25,-1,19,21,25,-1,19,25,18,-1,5,6,19,-1,19,18,5,-1,6,7,20,-1,20,19,6,-1,7,16,21,-1,21,20,7,-1,16,14,22,-1,22,21,16,-1,14,13,23,-1,23,22,14,-1,13,12,24,-1,24,23,13,-1,12,17,25,-1,25,24,12,-1,17,5,18,-1,18,25,17,-1]
IndexedFaceSet108.creaseAngle = 3.14159
IndexedFaceSet108.texCoordIndex = [1,3,2,-1,2,0,1,-1,4,5,3,-1,3,1,4,-1,5,4,6,-1,2,3,8,-1,8,7,2,-1,8,3,5,-1,5,9,8,-1,9,5,6,-1,6,10,9,-1,11,0,2,-1,2,7,11,-1,12,15,14,-1,14,13,12,-1,16,12,13,-1,13,17,16,-1,17,21,16,-1,14,18,19,-1,19,13,14,-1,19,20,17,-1,17,13,19,-1,20,22,21,-1,21,17,20,-1,23,18,14,-1,14,15,23,-1,25,26,27,-1,27,28,29,-1,29,30,31,-1,27,29,31,-1,25,27,31,-1,25,31,24,-1,7,8,25,-1,25,24,7,-1,8,9,26,-1,26,25,8,-1,9,10,27,-1,27,26,9,-1,22,20,28,-1,28,27,22,-1,20,19,29,-1,29,28,20,-1,19,18,30,-1,30,29,19,-1,18,23,31,-1,31,30,18,-1,11,7,24,-1,24,31,11,-1]
Coordinate109 = x3d.Coordinate()

IndexedFaceSet108.coord = Coordinate109
TextureCoordinate110 = x3d.TextureCoordinate()

IndexedFaceSet108.texCoord = TextureCoordinate110

Shape104.geometry = IndexedFaceSet108

Transform103.children.append(Shape104)

HAnimSegment102.children.append(Transform103)

HAnimJoint101.children.append(HAnimSegment102)

HAnimJoint91.children.append(HAnimJoint101)

HAnimJoint81.children.append(HAnimJoint91)

HAnimJoint71.children.append(HAnimJoint81)

HAnimJoint61.children.append(HAnimJoint71)

HAnimJoint51.children.append(HAnimJoint61)

HAnimJoint41.children.append(HAnimJoint51)
HAnimJoint111 = x3d.HAnimJoint()
HAnimJoint111.name = "r_hip"
HAnimJoint111.DEF = "hanim_r_hip"
HAnimJoint111.center = [-4.207,35.830002,-0.8155]
HAnimJoint111.ulimit = [0,0,0]
HAnimJoint111.llimit = [0,0,0]
HAnimSegment112 = x3d.HAnimSegment()
HAnimSegment112.name = "r_thigh"
HAnimSegment112.DEF = "hanim_r_thigh"
Transform113 = x3d.Transform()
Transform113.translation = [-4.207,35.830002,-0.8155]
Shape114 = x3d.Shape()
Appearance115 = x3d.Appearance()
Material116 = x3d.Material()
Material116.diffuseColor = [0.588,0.588,0.588]

Appearance115.material = Material116
ImageTexture117 = x3d.ImageTexture()
ImageTexture117.USE = "JinLOA2TextureAtlas"

Appearance115.texture = ImageTexture117

Shape114.appearance = Appearance115
IndexedFaceSet118 = x3d.IndexedFaceSet()
IndexedFaceSet118.coordIndex = [43,44,45,-1,42,43,45,-1,45,46,47,-1,42,45,47,-1,48,42,47,-1,0,7,8,-1,8,1,0,-1,1,8,9,-1,9,2,1,-1,2,9,10,-1,10,3,2,-1,3,10,11,-1,11,4,3,-1,4,11,12,-1,12,5,4,-1,5,12,13,-1,13,6,5,-1,6,13,7,-1,7,0,6,-1,7,14,15,-1,15,8,7,-1,8,15,16,-1,16,9,8,-1,9,16,17,-1,17,10,9,-1,10,17,18,-1,18,11,10,-1,11,18,19,-1,19,12,11,-1,12,19,20,-1,20,13,12,-1,13,20,14,-1,14,7,13,-1,14,21,22,-1,22,15,14,-1,15,22,23,-1,23,16,15,-1,16,23,24,-1,24,17,16,-1,17,24,25,-1,25,18,17,-1,18,25,26,-1,26,19,18,-1,19,26,27,-1,27,20,19,-1,20,27,21,-1,21,14,20,-1,60,59,58,-1,61,60,58,-1,58,57,56,-1,61,58,56,-1,62,61,56,-1,29,22,21,-1,21,28,29,-1,30,23,22,-1,22,29,30,-1,31,24,23,-1,23,30,31,-1,32,25,24,-1,24,31,32,-1,33,26,25,-1,25,32,33,-1,34,27,26,-1,26,33,34,-1,28,21,27,-1,27,34,28,-1,36,29,28,-1,28,35,36,-1,37,30,29,-1,29,36,37,-1,38,31,30,-1,30,37,38,-1,39,32,31,-1,31,38,39,-1,40,33,32,-1,32,39,40,-1,41,34,33,-1,33,40,41,-1,35,28,34,-1,34,41,35,-1,42,0,1,-1,1,43,42,-1,43,1,2,-1,2,44,43,-1,44,2,3,-1,3,45,44,-1,45,3,4,-1,4,46,45,-1,46,4,5,-1,5,47,46,-1,47,5,6,-1,6,48,47,-1,48,6,0,-1,0,42,48,-1,50,36,35,-1,35,49,50,-1,51,37,36,-1,36,50,51,-1,52,38,37,-1,37,51,52,-1,53,39,38,-1,38,52,53,-1,54,40,39,-1,39,53,54,-1,55,41,40,-1,40,54,55,-1,49,35,41,-1,41,55,49,-1,57,50,49,-1,49,56,57,-1,58,51,50,-1,50,57,58,-1,59,52,51,-1,51,58,59,-1,60,53,52,-1,52,59,60,-1,61,54,53,-1,53,60,61,-1,62,55,54,-1,54,61,62,-1,56,49,55,-1,55,62,56,-1]
IndexedFaceSet118.creaseAngle = 3.14159
IndexedFaceSet118.texCoordIndex = [0,2,3,-1,1,0,3,-1,3,4,5,-1,1,3,5,-1,6,1,5,-1,7,9,8,-1,8,10,7,-1,10,8,11,-1,11,12,10,-1,12,11,13,-1,13,14,12,-1,14,13,15,-1,15,16,14,-1,16,15,17,-1,17,18,16,-1,18,17,19,-1,19,20,18,-1,20,19,9,-1,9,7,20,-1,9,22,21,-1,21,8,9,-1,8,21,23,-1,23,11,8,-1,11,23,24,-1,24,13,11,-1,13,24,25,-1,25,15,13,-1,15,25,26,-1,26,17,15,-1,17,26,27,-1,27,19,17,-1,19,27,22,-1,22,9,19,-1,22,29,28,-1,28,21,22,-1,21,28,30,-1,30,23,21,-1,23,30,31,-1,31,24,23,-1,24,31,32,-1,32,25,24,-1,25,32,33,-1,33,26,25,-1,26,33,34,-1,34,27,26,-1,27,34,29,-1,29,22,27,-1,46,45,44,-1,47,46,44,-1,44,43,42,-1,47,44,42,-1,48,47,42,-1,35,28,29,-1,29,36,35,-1,37,30,28,-1,28,35,37,-1,38,31,30,-1,30,37,38,-1,39,32,31,-1,31,38,39,-1,40,33,32,-1,32,39,40,-1,41,34,33,-1,33,40,41,-1,36,29,34,-1,34,41,36,-1,51,50,49,-1,49,52,51,-1,54,53,50,-1,50,51,54,-1,56,55,53,-1,53,54,56,-1,58,57,55,-1,55,56,58,-1,60,59,57,-1,57,58,60,-1,62,61,59,-1,59,60,62,-1,52,49,61,-1,61,62,52,-1,1,7,10,-1,10,0,1,-1,0,10,12,-1,12,2,0,-1,2,12,14,-1,14,3,2,-1,3,14,16,-1,16,4,3,-1,4,16,18,-1,18,5,4,-1,5,18,20,-1,20,6,5,-1,6,20,7,-1,7,1,6,-1,63,51,52,-1,52,64,63,-1,65,54,51,-1,51,63,65,-1,66,56,54,-1,54,65,66,-1,67,58,56,-1,56,66,67,-1,68,60,58,-1,58,67,68,-1,69,62,60,-1,60,68,69,-1,64,52,62,-1,62,69,64,-1,43,63,64,-1,64,42,43,-1,44,65,63,-1,63,43,44,-1,45,66,65,-1,65,44,45,-1,46,67,66,-1,66,45,46,-1,47,68,67,-1,67,46,47,-1,48,69,68,-1,68,47,48,-1,42,64,69,-1,69,48,42,-1]
Coordinate119 = x3d.Coordinate()

IndexedFaceSet118.coord = Coordinate119
TextureCoordinate120 = x3d.TextureCoordinate()

IndexedFaceSet118.texCoord = TextureCoordinate120

Shape114.geometry = IndexedFaceSet118

Transform113.children.append(Shape114)

HAnimSegment112.children.append(Transform113)

HAnimJoint111.children.append(HAnimSegment112)
HAnimJoint121 = x3d.HAnimJoint()
HAnimJoint121.name = "r_knee"
HAnimJoint121.DEF = "hanim_r_knee"
HAnimJoint121.center = [-4.116,17.26,-0.8639]
HAnimJoint121.ulimit = [0,0,0]
HAnimJoint121.llimit = [0,0,0]
HAnimSegment122 = x3d.HAnimSegment()
HAnimSegment122.name = "r_calf"
HAnimSegment122.DEF = "hanim_r_calf"
Transform123 = x3d.Transform()
Transform123.translation = [-4.116,17.26,-0.8639]
Shape124 = x3d.Shape()
Appearance125 = x3d.Appearance()
Material126 = x3d.Material()
Material126.diffuseColor = [0.588,0.588,0.588]

Appearance125.material = Material126
ImageTexture127 = x3d.ImageTexture()
ImageTexture127.USE = "JinLOA2TextureAtlas"

Appearance125.texture = ImageTexture127

Shape124.appearance = Appearance125
IndexedFaceSet128 = x3d.IndexedFaceSet()
IndexedFaceSet128.coordIndex = [0,1,2,-1,2,3,4,-1,2,4,5,-1,0,2,5,-1,6,0,5,-1,9,10,7,-1,7,8,9,-1,12,9,8,-1,8,11,12,-1,14,12,11,-1,11,13,14,-1,16,14,13,-1,13,15,16,-1,18,16,15,-1,15,17,18,-1,20,18,17,-1,17,19,20,-1,10,20,19,-1,19,7,10,-1,21,22,10,-1,10,9,21,-1,23,21,9,-1,9,12,23,-1,24,23,12,-1,12,14,24,-1,25,24,14,-1,14,16,25,-1,26,25,16,-1,16,18,26,-1,27,26,18,-1,18,20,27,-1,22,27,20,-1,20,10,22,-1,1,0,22,-1,22,21,1,-1,2,1,21,-1,21,23,2,-1,3,2,23,-1,23,24,3,-1,4,3,24,-1,24,25,4,-1,5,4,25,-1,25,26,5,-1,6,5,26,-1,26,27,6,-1,0,6,27,-1,27,22,0,-1,8,7,28,-1,28,29,8,-1,11,8,29,-1,29,30,11,-1,13,11,30,-1,30,31,13,-1,15,13,31,-1,31,32,15,-1,17,15,32,-1,32,33,17,-1,19,17,33,-1,33,34,19,-1,7,19,34,-1,34,28,7,-1,29,28,35,-1,35,36,29,-1,30,29,36,-1,36,37,30,-1,31,30,37,-1,37,38,31,-1,32,31,38,-1,38,39,32,-1,33,32,39,-1,39,40,33,-1,34,33,40,-1,40,41,34,-1,28,34,41,-1,41,35,28,-1]
IndexedFaceSet128.creaseAngle = 3.14159
IndexedFaceSet128.texCoordIndex = [0,1,2,-1,2,3,4,-1,2,4,5,-1,0,2,5,-1,6,0,5,-1,9,10,7,-1,7,8,9,-1,12,9,8,-1,8,11,12,-1,14,12,11,-1,11,13,14,-1,16,14,13,-1,13,15,16,-1,18,16,15,-1,15,17,18,-1,20,18,17,-1,17,19,20,-1,10,20,19,-1,19,7,10,-1,21,22,10,-1,10,9,21,-1,23,21,9,-1,9,12,23,-1,24,23,12,-1,12,14,24,-1,25,24,14,-1,14,16,25,-1,26,25,16,-1,16,18,26,-1,27,26,18,-1,18,20,27,-1,22,27,20,-1,20,10,22,-1,1,0,22,-1,22,21,1,-1,2,1,21,-1,21,23,2,-1,3,2,23,-1,23,24,3,-1,4,3,24,-1,24,25,4,-1,5,4,25,-1,25,26,5,-1,6,5,26,-1,26,27,6,-1,0,6,27,-1,27,22,0,-1,8,7,28,-1,28,29,8,-1,11,8,29,-1,29,30,11,-1,13,11,30,-1,30,31,13,-1,15,13,31,-1,31,32,15,-1,17,15,32,-1,32,33,17,-1,19,17,33,-1,33,34,19,-1,7,19,34,-1,34,28,7,-1,29,28,35,-1,35,36,29,-1,30,29,36,-1,36,37,30,-1,31,30,37,-1,37,38,31,-1,32,31,38,-1,38,39,32,-1,33,32,39,-1,39,40,33,-1,34,33,40,-1,40,41,34,-1,28,34,41,-1,41,35,28,-1]
Coordinate129 = x3d.Coordinate()

IndexedFaceSet128.coord = Coordinate129
TextureCoordinate130 = x3d.TextureCoordinate()

IndexedFaceSet128.texCoord = TextureCoordinate130

Shape124.geometry = IndexedFaceSet128

Transform123.children.append(Shape124)

HAnimSegment122.children.append(Transform123)

HAnimJoint121.children.append(HAnimSegment122)
HAnimJoint131 = x3d.HAnimJoint()
HAnimJoint131.name = "r_talocrural"
HAnimJoint131.DEF = "hanim_r_talocrural"
HAnimJoint131.center = [-3.854,3.939,-0.7038]
HAnimJoint131.ulimit = [0,0,0]
HAnimJoint131.llimit = [0,0,0]
HAnimSegment132 = x3d.HAnimSegment()
HAnimSegment132.name = "r_talus"
HAnimSegment132.DEF = "hanim_r_talus"
Transform133 = x3d.Transform()
Transform133.translation = [-3.854,3.939,-0.7038]
Shape134 = x3d.Shape()
Appearance135 = x3d.Appearance()
Material136 = x3d.Material()
Material136.diffuseColor = [0.588,0.588,0.588]

Appearance135.material = Material136
ImageTexture137 = x3d.ImageTexture()
ImageTexture137.USE = "JinLOA2TextureAtlas"

Appearance135.texture = ImageTexture137

Shape134.appearance = Appearance135
IndexedFaceSet138 = x3d.IndexedFaceSet()
IndexedFaceSet138.coordIndex = [1,14,11,-1,3,6,5,-1,5,4,3,-1,1,3,4,-1,4,0,1,-1,0,4,5,-1,5,2,0,-1,11,6,3,-1,3,1,11,-1,15,12,0,-1,0,2,15,-1,0,12,13,-1,13,1,0,-1,13,14,1,-1,7,11,18,-1,8,9,5,-1,5,6,8,-1,7,10,9,-1,9,8,7,-1,10,2,5,-1,5,9,10,-1,11,7,8,-1,8,6,11,-1,15,2,10,-1,10,16,15,-1,10,7,17,-1,17,16,10,-1,17,7,18,-1,19,26,25,-1,25,24,23,-1,19,25,23,-1,23,22,21,-1,19,23,21,-1,20,19,21,-1,15,19,20,-1,20,12,15,-1,12,20,21,-1,21,13,12,-1,13,21,22,-1,22,14,13,-1,14,22,23,-1,23,11,14,-1,11,23,24,-1,24,18,11,-1,18,24,25,-1,25,17,18,-1,17,25,26,-1,26,16,17,-1,16,26,19,-1,19,15,16,-1]
IndexedFaceSet138.creaseAngle = 3.14159
IndexedFaceSet138.texCoordIndex = [1,18,14,-1,3,6,5,-1,5,4,3,-1,1,3,4,-1,4,0,1,-1,0,4,5,-1,5,2,0,-1,14,6,3,-1,3,1,14,-1,19,16,0,-1,0,2,19,-1,0,16,17,-1,17,1,0,-1,17,18,1,-1,7,15,23,-1,9,10,11,-1,11,8,9,-1,7,12,10,-1,10,9,7,-1,12,13,11,-1,11,10,12,-1,15,7,9,-1,9,8,15,-1,20,13,12,-1,12,21,20,-1,12,7,22,-1,22,21,12,-1,22,7,23,-1,24,31,30,-1,30,29,28,-1,24,30,28,-1,28,27,26,-1,24,28,26,-1,25,24,26,-1,19,24,25,-1,25,16,19,-1,16,25,26,-1,26,17,16,-1,17,26,27,-1,27,18,17,-1,18,27,28,-1,28,14,18,-1,15,28,29,-1,29,23,15,-1,23,29,30,-1,30,22,23,-1,22,30,31,-1,31,21,22,-1,21,31,24,-1,24,20,21,-1]
Coordinate139 = x3d.Coordinate()

IndexedFaceSet138.coord = Coordinate139
TextureCoordinate140 = x3d.TextureCoordinate()

IndexedFaceSet138.texCoord = TextureCoordinate140

Shape134.geometry = IndexedFaceSet138

Transform133.children.append(Shape134)

HAnimSegment132.children.append(Transform133)

HAnimJoint131.children.append(HAnimSegment132)
HAnimJoint141 = x3d.HAnimJoint()
HAnimJoint141.name = "r_tarsometatarsal_2"
HAnimJoint141.DEF = "hanim_r_tarsometatarsal_2"
HAnimJoint141.center = [-3.854,3.336,-1.514]
HAnimJoint141.ulimit = [0,0,0]
HAnimJoint141.llimit = [0,0,0]
HAnimSegment142 = x3d.HAnimSegment()
HAnimSegment142.name = "r_metatarsal_2"
HAnimSegment142.DEF = "hanim_r_metatarsal_2"
Transform143 = x3d.Transform()
Transform143.translation = [-3.854,3.336,-1.514]
Shape144 = x3d.Shape()
Appearance145 = x3d.Appearance()
Material146 = x3d.Material()
Material146.diffuseColor = [0.588,0.588,0.588]

Appearance145.material = Material146
ImageTexture147 = x3d.ImageTexture()
ImageTexture147.USE = "JinLOA2TextureAtlas"

Appearance145.texture = ImageTexture147

Shape144.appearance = Appearance145
IndexedFaceSet148 = x3d.IndexedFaceSet()
IndexedFaceSet148.coordIndex = [6,0,3,-1,3,4,6,-1,9,11,3,-1,3,0,9,-1,2,1,0,-1,0,6,2,-1,10,9,0,-1,0,1,10,-1,1,2,15,-1,15,10,1,-1,6,4,7,-1,7,5,6,-1,12,5,7,-1,7,13,12,-1,2,6,5,-1,5,8,2,-1,14,8,5,-1,5,12,14,-1,8,14,15,-1,15,2,8,-1,17,16,20,-1,17,20,19,-1,17,19,18,-1,24,23,22,-1,22,21,27,-1,22,27,26,-1,24,22,26,-1,24,26,25,-1,3,16,17,-1,17,4,3,-1,4,17,18,-1,18,7,4,-1,7,18,19,-1,19,13,7,-1,13,19,20,-1,20,11,13,-1,11,20,16,-1,16,3,11,-1,10,21,22,-1,22,9,10,-1,9,22,23,-1,23,11,9,-1,11,23,24,-1,24,13,11,-1,13,24,25,-1,25,12,13,-1,12,25,26,-1,26,14,12,-1,14,26,27,-1,27,15,14,-1,15,27,21,-1,21,10,15,-1]
IndexedFaceSet148.creaseAngle = 3.14159
IndexedFaceSet148.texCoordIndex = [2,0,5,-1,5,6,2,-1,14,16,5,-1,5,0,14,-1,3,1,0,-1,0,2,3,-1,15,14,0,-1,0,1,15,-1,1,4,21,-1,21,15,1,-1,8,9,10,-1,10,7,8,-1,17,7,10,-1,10,18,17,-1,12,8,7,-1,7,11,12,-1,19,11,7,-1,7,17,19,-1,11,19,20,-1,20,13,11,-1,23,22,26,-1,23,26,25,-1,23,25,24,-1,30,29,28,-1,28,27,33,-1,28,33,32,-1,30,28,32,-1,30,32,31,-1,5,22,23,-1,23,6,5,-1,9,23,24,-1,24,10,9,-1,10,24,25,-1,25,18,10,-1,18,25,26,-1,26,16,18,-1,16,26,22,-1,22,5,16,-1,15,27,28,-1,28,14,15,-1,14,28,29,-1,29,16,14,-1,16,29,30,-1,30,18,16,-1,18,30,31,-1,31,17,18,-1,17,31,32,-1,32,19,17,-1,19,32,33,-1,33,20,19,-1,21,33,27,-1,27,15,21,-1]
Coordinate149 = x3d.Coordinate()

IndexedFaceSet148.coord = Coordinate149
TextureCoordinate150 = x3d.TextureCoordinate()

IndexedFaceSet148.texCoord = TextureCoordinate150

Shape144.geometry = IndexedFaceSet148

Transform143.children.append(Shape144)

HAnimSegment142.children.append(Transform143)

HAnimJoint141.children.append(HAnimSegment142)
HAnimJoint151 = x3d.HAnimJoint()
HAnimJoint151.name = "r_metatarsophalangeal_2"
HAnimJoint151.DEF = "hanim_r_metatarsophalangeal_2"
HAnimJoint151.center = [-3.854,3.64,0.7402]
HAnimJoint151.ulimit = [0,0,0]
HAnimJoint151.llimit = [0,0,0]
HAnimSegment152 = x3d.HAnimSegment()
HAnimSegment152.name = "r_tarsal_proximal_phalanx_2"
HAnimSegment152.DEF = "hanim_r_tarsal_proximal_phalanx_2"
Transform153 = x3d.Transform()
Transform153.translation = [-3.854,3.64,0.7402]
Shape154 = x3d.Shape()
Appearance155 = x3d.Appearance()
Material156 = x3d.Material()
Material156.diffuseColor = [0.588,0.588,0.588]

Appearance155.material = Material156
ImageTexture157 = x3d.ImageTexture()
ImageTexture157.USE = "JinLOA2TextureAtlas"

Appearance155.texture = ImageTexture157

Shape154.appearance = Appearance155
IndexedFaceSet158 = x3d.IndexedFaceSet()
IndexedFaceSet158.coordIndex = [10,4,3,-1,11,10,3,-1,0,11,3,-1,1,12,11,-1,11,0,1,-1,1,9,16,-1,16,12,1,-1,2,4,10,-1,10,17,2,-1,6,8,13,-1,6,13,14,-1,5,6,14,-1,7,5,14,-1,14,15,7,-1,7,15,16,-1,16,9,7,-1,2,17,13,-1,13,8,2,-1,19,18,24,-1,22,21,20,-1,23,22,20,-1,24,23,20,-1,19,24,20,-1,26,25,32,-1,26,32,31,-1,26,31,30,-1,30,29,28,-1,26,30,28,-1,26,28,27,-1,0,18,19,-1,19,1,0,-1,1,19,20,-1,20,9,1,-1,9,20,21,-1,21,7,9,-1,7,21,22,-1,22,5,7,-1,5,22,23,-1,23,6,5,-1,6,23,24,-1,24,3,6,-1,3,24,18,-1,18,0,3,-1,11,25,26,-1,26,10,11,-1,10,26,27,-1,27,17,10,-1,17,27,28,-1,28,13,17,-1,13,28,29,-1,29,14,13,-1,14,29,30,-1,30,15,14,-1,15,30,31,-1,31,16,15,-1,16,31,32,-1,32,12,16,-1,12,32,25,-1,25,11,12,-1,2,8,6,-1,2,6,3,-1,4,2,3,-1]
IndexedFaceSet158.creaseAngle = 3.14159
IndexedFaceSet158.texCoordIndex = [12,5,4,-1,13,12,4,-1,0,13,4,-1,1,14,13,-1,13,0,1,-1,1,3,19,-1,19,14,1,-1,2,5,12,-1,12,21,2,-1,7,10,15,-1,7,15,16,-1,6,7,16,-1,8,6,16,-1,16,17,8,-1,8,17,18,-1,18,11,8,-1,9,20,15,-1,15,10,9,-1,23,22,28,-1,26,25,24,-1,27,26,24,-1,28,27,24,-1,23,28,24,-1,30,29,36,-1,30,36,35,-1,30,35,34,-1,34,33,32,-1,30,34,32,-1,30,32,31,-1,0,22,23,-1,23,1,0,-1,1,23,24,-1,24,3,1,-1,11,24,25,-1,25,8,11,-1,8,25,26,-1,26,6,8,-1,6,26,27,-1,27,7,6,-1,7,27,28,-1,28,4,7,-1,4,28,22,-1,22,0,4,-1,13,29,30,-1,30,12,13,-1,12,30,31,-1,31,21,12,-1,20,31,32,-1,32,15,20,-1,15,32,33,-1,33,16,15,-1,16,33,34,-1,34,17,16,-1,17,34,35,-1,35,18,17,-1,19,35,36,-1,36,14,19,-1,14,36,29,-1,29,13,14,-1,9,10,7,-1,9,7,4,-1,5,9,4,-1]
Coordinate159 = x3d.Coordinate()

IndexedFaceSet158.coord = Coordinate159
TextureCoordinate160 = x3d.TextureCoordinate()

IndexedFaceSet158.texCoord = TextureCoordinate160

Shape154.geometry = IndexedFaceSet158

Transform153.children.append(Shape154)

HAnimSegment152.children.append(Transform153)

HAnimJoint151.children.append(HAnimSegment152)
HAnimJoint161 = x3d.HAnimJoint()
HAnimJoint161.name = "r_tarsal_distal_interphalangeal_2"
HAnimJoint161.DEF = "hanim_r_tarsal_distal_interphalangeal_2"
HAnimJoint161.center = [-3.854,1.956,1.682]
HAnimJoint161.ulimit = [0,0,0]
HAnimJoint161.llimit = [0,0,0]
HAnimSegment162 = x3d.HAnimSegment()
HAnimSegment162.name = "r_tarsal_distal_phalanx_2"
HAnimSegment162.DEF = "hanim_r_tarsal_distal_phalanx_2"
Transform163 = x3d.Transform()
Transform163.translation = [-3.854,1.956,1.682]
Shape164 = x3d.Shape()
Appearance165 = x3d.Appearance()
Material166 = x3d.Material()
Material166.diffuseColor = [0.588,0.588,0.588]

Appearance165.material = Material166
ImageTexture167 = x3d.ImageTexture()
ImageTexture167.USE = "JinLOA2TextureAtlas"

Appearance165.texture = ImageTexture167

Shape164.appearance = Appearance165
IndexedFaceSet168 = x3d.IndexedFaceSet()
IndexedFaceSet168.coordIndex = [3,4,0,-1,0,1,3,-1,10,3,1,-1,1,2,10,-1,2,15,10,-1,0,5,6,-1,6,1,0,-1,6,7,2,-1,2,1,6,-1,7,16,15,-1,15,2,7,-1,17,5,0,-1,0,4,17,-1,3,8,9,-1,9,4,3,-1,10,11,8,-1,8,3,10,-1,11,10,15,-1,9,8,13,-1,13,12,9,-1,13,8,11,-1,11,14,13,-1,14,11,15,-1,15,16,14,-1,17,4,9,-1,9,12,17,-1,19,18,25,-1,25,24,23,-1,23,22,21,-1,25,23,21,-1,19,25,21,-1,19,21,20,-1,5,18,19,-1,19,6,5,-1,6,19,20,-1,20,7,6,-1,7,20,21,-1,21,16,7,-1,16,21,22,-1,22,14,16,-1,14,22,23,-1,23,13,14,-1,13,23,24,-1,24,12,13,-1,12,24,25,-1,25,17,12,-1,17,25,18,-1,18,5,17,-1]
IndexedFaceSet168.creaseAngle = 3.14159
IndexedFaceSet168.texCoordIndex = [1,0,2,-1,2,3,1,-1,4,1,3,-1,3,5,4,-1,5,6,4,-1,2,7,8,-1,8,3,2,-1,8,9,5,-1,5,3,8,-1,9,10,6,-1,6,5,9,-1,11,7,2,-1,2,0,11,-1,12,13,14,-1,14,15,12,-1,16,17,13,-1,13,12,16,-1,17,16,21,-1,14,13,19,-1,19,18,14,-1,19,13,17,-1,17,20,19,-1,20,17,21,-1,21,22,20,-1,23,15,14,-1,14,18,23,-1,25,24,31,-1,31,30,29,-1,29,28,27,-1,31,29,27,-1,25,31,27,-1,25,27,26,-1,7,24,25,-1,25,8,7,-1,8,25,26,-1,26,9,8,-1,9,26,27,-1,27,10,9,-1,22,27,28,-1,28,20,22,-1,20,28,29,-1,29,19,20,-1,19,29,30,-1,30,18,19,-1,18,30,31,-1,31,23,18,-1,11,31,24,-1,24,7,11,-1]
Coordinate169 = x3d.Coordinate()

IndexedFaceSet168.coord = Coordinate169
TextureCoordinate170 = x3d.TextureCoordinate()

IndexedFaceSet168.texCoord = TextureCoordinate170

Shape164.geometry = IndexedFaceSet168

Transform163.children.append(Shape164)

HAnimSegment162.children.append(Transform163)

HAnimJoint161.children.append(HAnimSegment162)

HAnimJoint151.children.append(HAnimJoint161)

HAnimJoint141.children.append(HAnimJoint151)

HAnimJoint131.children.append(HAnimJoint141)

HAnimJoint121.children.append(HAnimJoint131)

HAnimJoint111.children.append(HAnimJoint121)

HAnimJoint41.children.append(HAnimJoint111)

HAnimJoint31.children.append(HAnimJoint41)
HAnimJoint171 = x3d.HAnimJoint()
HAnimJoint171.name = "vl5"
HAnimJoint171.DEF = "hanim_vl5"
HAnimJoint171.center = [0,40.220001,-0.6117]
HAnimJoint171.ulimit = [0,0,0]
HAnimJoint171.llimit = [0,0,0]
HAnimSegment172 = x3d.HAnimSegment()
HAnimSegment172.name = "l5"
HAnimSegment172.DEF = "hanim_l5"
Transform173 = x3d.Transform()
Transform173.translation = [0,40.220001,-0.6117]
Shape174 = x3d.Shape()
Appearance175 = x3d.Appearance()
Material176 = x3d.Material()
Material176.diffuseColor = [0.588,0.588,0.588]

Appearance175.material = Material176
ImageTexture177 = x3d.ImageTexture()
ImageTexture177.USE = "JinLOA2TextureAtlas"

Appearance175.texture = ImageTexture177

Shape174.appearance = Appearance175
IndexedFaceSet178 = x3d.IndexedFaceSet()
IndexedFaceSet178.coordIndex = [0,10,11,-1,11,5,0,-1,1,0,5,-1,5,6,1,-1,2,3,8,-1,8,7,2,-1,3,4,9,-1,9,8,3,-1,4,1,6,-1,6,9,4,-1,2,7,26,-1,26,27,2,-1,8,5,11,-1,11,7,8,-1,9,6,5,-1,5,8,9,-1,11,10,13,-1,13,12,11,-1,7,11,12,-1,12,26,7,-1,16,15,14,-1,14,17,16,-1,19,18,15,-1,15,16,19,-1,22,21,20,-1,20,23,22,-1,23,20,24,-1,24,25,23,-1,25,24,18,-1,18,19,25,-1,22,27,26,-1,26,21,22,-1,20,21,14,-1,14,15,20,-1,24,20,15,-1,15,18,24,-1,14,12,13,-1,13,17,14,-1,21,26,12,-1,12,14,21,-1,29,30,31,-1,31,32,33,-1,29,31,33,-1,34,35,36,-1,33,34,36,-1,36,37,38,-1,38,39,40,-1,36,38,40,-1,33,36,40,-1,29,33,40,-1,29,40,41,-1,29,41,28,-1,10,0,29,-1,29,28,10,-1,0,1,30,-1,30,29,0,-1,1,4,31,-1,31,30,1,-1,4,3,32,-1,32,31,4,-1,3,2,33,-1,33,32,3,-1,2,27,34,-1,34,33,2,-1,27,22,35,-1,35,34,27,-1,22,23,36,-1,36,35,22,-1,23,25,37,-1,37,36,23,-1,25,19,38,-1,38,37,25,-1,19,16,39,-1,39,38,19,-1,16,17,40,-1,40,39,16,-1,17,13,41,-1,41,40,17,-1,13,10,28,-1,28,41,13,-1]
IndexedFaceSet178.creaseAngle = 3.14159
IndexedFaceSet178.texCoordIndex = [1,0,6,-1,6,7,1,-1,2,1,7,-1,7,8,2,-1,4,3,9,-1,9,10,4,-1,3,5,11,-1,11,9,3,-1,5,2,8,-1,8,11,5,-1,12,13,15,-1,15,14,12,-1,9,7,6,-1,6,10,9,-1,11,8,7,-1,7,9,11,-1,6,0,17,-1,17,18,6,-1,10,6,18,-1,18,16,10,-1,21,20,19,-1,19,22,21,-1,24,23,20,-1,20,21,24,-1,27,26,25,-1,25,28,27,-1,28,25,29,-1,29,30,28,-1,30,29,23,-1,23,24,30,-1,31,34,33,-1,33,32,31,-1,25,26,19,-1,19,20,25,-1,29,25,20,-1,20,23,29,-1,19,35,36,-1,36,22,19,-1,26,37,35,-1,35,19,26,-1,39,40,41,-1,41,42,43,-1,39,41,43,-1,44,45,46,-1,43,44,46,-1,46,47,48,-1,48,49,50,-1,46,48,50,-1,43,46,50,-1,39,43,50,-1,39,50,51,-1,39,51,38,-1,0,1,39,-1,39,38,0,-1,1,2,40,-1,40,39,1,-1,2,5,41,-1,41,40,2,-1,5,3,42,-1,42,41,5,-1,3,4,43,-1,43,42,3,-1,12,14,44,-1,44,43,12,-1,34,31,45,-1,45,44,34,-1,27,28,46,-1,46,45,27,-1,28,30,47,-1,47,46,28,-1,30,24,48,-1,48,47,30,-1,24,21,49,-1,49,48,24,-1,21,22,50,-1,50,49,21,-1,22,36,51,-1,51,50,22,-1,17,0,38,-1,38,51,17,-1]
Coordinate179 = x3d.Coordinate()

IndexedFaceSet178.coord = Coordinate179
TextureCoordinate180 = x3d.TextureCoordinate()

IndexedFaceSet178.texCoord = TextureCoordinate180

Shape174.geometry = IndexedFaceSet178

Transform173.children.append(Shape174)

HAnimSegment172.children.append(Transform173)

HAnimJoint171.children.append(HAnimSegment172)
HAnimJoint181 = x3d.HAnimJoint()
HAnimJoint181.name = "vl3"
HAnimJoint181.DEF = "hanim_vl3"
HAnimJoint181.center = [0,41.299999,-0.6117]
HAnimJoint181.ulimit = [0,0,0]
HAnimJoint181.llimit = [0,0,0]
HAnimSegment182 = x3d.HAnimSegment()
HAnimSegment182.name = "l3"
HAnimSegment182.DEF = "hanim_l3"
Transform183 = x3d.Transform()
Transform183.translation = [0,41.299999,-0.6117]
Shape184 = x3d.Shape()
Appearance185 = x3d.Appearance()
Material186 = x3d.Material()
Material186.diffuseColor = [0.588,0.588,0.588]

Appearance185.material = Material186
ImageTexture187 = x3d.ImageTexture()
ImageTexture187.USE = "JinLOA2TextureAtlas"

Appearance185.texture = ImageTexture187

Shape184.appearance = Appearance185
IndexedFaceSet188 = x3d.IndexedFaceSet()
IndexedFaceSet188.coordIndex = [1,17,21,-1,21,6,1,-1,0,15,16,-1,16,5,0,-1,7,47,20,-1,20,4,7,-1,4,0,9,-1,9,8,4,-1,0,5,10,-1,10,9,0,-1,5,3,11,-1,11,10,5,-1,3,2,12,-1,12,11,3,-1,2,1,13,-1,13,12,2,-1,1,6,40,-1,40,13,1,-1,7,4,8,-1,8,14,7,-1,20,15,0,-1,0,4,20,-1,17,1,2,-1,2,18,17,-1,19,18,2,-1,2,3,19,-1,16,19,3,-1,3,5,16,-1,15,20,23,-1,23,22,15,-1,20,47,50,-1,50,23,20,-1,21,17,24,-1,24,52,21,-1,17,18,25,-1,25,24,17,-1,18,19,26,-1,26,25,18,-1,19,16,27,-1,27,26,19,-1,16,15,22,-1,22,27,16,-1,28,6,21,-1,21,45,28,-1,45,44,32,-1,32,28,45,-1,46,43,31,-1,31,33,46,-1,30,35,34,-1,34,29,30,-1,29,34,36,-1,36,31,29,-1,31,36,37,-1,37,33,31,-1,33,37,38,-1,38,32,33,-1,32,38,39,-1,39,28,32,-1,28,39,40,-1,40,6,28,-1,7,14,35,-1,35,30,7,-1,41,30,29,-1,29,42,41,-1,29,31,43,-1,43,42,29,-1,46,33,32,-1,32,44,46,-1,47,7,30,-1,30,41,47,-1,42,49,48,-1,48,41,42,-1,41,48,50,-1,50,47,41,-1,21,52,51,-1,51,45,21,-1,45,51,53,-1,53,44,45,-1,44,53,54,-1,54,46,44,-1,46,54,55,-1,55,43,46,-1,43,55,49,-1,49,42,43,-1]
IndexedFaceSet188.creaseAngle = 3.14159
IndexedFaceSet188.texCoordIndex = [4,19,24,-1,24,7,4,-1,0,17,18,-1,18,2,0,-1,8,25,23,-1,23,1,8,-1,1,0,10,-1,10,9,1,-1,0,2,11,-1,11,10,0,-1,2,6,12,-1,12,11,2,-1,6,5,13,-1,13,12,6,-1,5,3,14,-1,14,13,5,-1,4,7,15,-1,15,14,4,-1,8,1,9,-1,9,16,8,-1,23,17,0,-1,0,1,23,-1,20,3,5,-1,5,21,20,-1,22,21,5,-1,5,6,22,-1,18,22,6,-1,6,2,18,-1,17,23,27,-1,27,26,17,-1,23,25,28,-1,28,27,23,-1,24,19,30,-1,30,29,24,-1,20,21,31,-1,31,30,20,-1,21,22,32,-1,32,31,21,-1,22,18,33,-1,33,32,22,-1,18,17,26,-1,26,33,18,-1,34,35,59,-1,59,58,34,-1,55,54,40,-1,40,39,55,-1,56,53,38,-1,38,41,56,-1,37,44,43,-1,43,36,37,-1,36,43,45,-1,45,38,36,-1,38,45,46,-1,46,41,38,-1,41,46,47,-1,47,40,41,-1,40,47,48,-1,48,39,40,-1,34,48,49,-1,49,35,34,-1,42,50,44,-1,44,37,42,-1,51,37,36,-1,36,52,51,-1,36,38,53,-1,53,52,36,-1,56,41,40,-1,40,54,56,-1,57,42,37,-1,37,51,57,-1,52,61,60,-1,60,51,52,-1,51,60,62,-1,62,57,51,-1,59,64,63,-1,63,58,59,-1,55,63,65,-1,65,54,55,-1,54,65,66,-1,66,56,54,-1,56,66,67,-1,67,53,56,-1,53,67,61,-1,61,52,53,-1]
Coordinate189 = x3d.Coordinate()

IndexedFaceSet188.coord = Coordinate189
TextureCoordinate190 = x3d.TextureCoordinate()

IndexedFaceSet188.texCoord = TextureCoordinate190

Shape184.geometry = IndexedFaceSet188

Transform183.children.append(Shape184)

HAnimSegment182.children.append(Transform183)

HAnimJoint181.children.append(HAnimSegment182)
HAnimJoint191 = x3d.HAnimJoint()
HAnimJoint191.name = "vl1"
HAnimJoint191.DEF = "hanim_vl1"
HAnimJoint191.center = [0,42.759998,-0.6117]
HAnimJoint191.ulimit = [0,0,0]
HAnimJoint191.llimit = [0,0,0]
HAnimSegment192 = x3d.HAnimSegment()
HAnimSegment192.name = "l1"
HAnimSegment192.DEF = "hanim_l1"
Transform193 = x3d.Transform()
Transform193.translation = [0,42.759998,-0.6117]
Shape194 = x3d.Shape()
Appearance195 = x3d.Appearance()
Material196 = x3d.Material()
Material196.diffuseColor = [0.588,0.588,0.588]

Appearance195.material = Material196
ImageTexture197 = x3d.ImageTexture()
ImageTexture197.USE = "JinLOA2TextureAtlas"

Appearance195.texture = ImageTexture197

Shape194.appearance = Appearance195
IndexedFaceSet198 = x3d.IndexedFaceSet()
IndexedFaceSet198.coordIndex = [7,0,1,-1,1,35,7,-1,33,2,0,-1,0,7,33,-1,34,8,3,-1,3,4,34,-1,32,5,2,-1,2,33,32,-1,35,1,6,-1,6,54,35,-1,32,34,4,-1,4,5,32,-1,8,45,17,-1,17,3,8,-1,47,48,10,-1,10,9,47,-1,11,47,9,-1,9,12,11,-1,51,14,13,-1,13,42,51,-1,15,11,12,-1,12,16,15,-1,48,54,6,-1,6,10,48,-1,15,16,14,-1,14,51,15,-1,42,13,17,-1,17,45,42,-1,1,0,19,-1,19,18,1,-1,0,2,20,-1,20,19,0,-1,2,5,21,-1,21,20,2,-1,5,4,22,-1,22,21,5,-1,4,3,23,-1,23,22,4,-1,3,17,24,-1,24,23,3,-1,17,13,25,-1,25,24,17,-1,13,14,26,-1,26,25,13,-1,14,16,27,-1,27,26,14,-1,16,12,28,-1,28,27,16,-1,12,9,29,-1,29,28,12,-1,9,10,30,-1,30,29,9,-1,10,6,31,-1,31,30,10,-1,6,1,18,-1,18,31,6,-1,8,37,44,-1,44,45,8,-1,7,35,40,-1,40,36,7,-1,41,33,7,-1,7,36,41,-1,8,34,38,-1,38,37,8,-1,34,32,39,-1,39,38,34,-1,39,32,33,-1,33,41,39,-1,35,54,55,-1,55,40,35,-1,42,45,44,-1,44,43,42,-1,47,46,49,-1,49,48,47,-1,50,46,47,-1,47,11,50,-1,42,43,52,-1,52,51,42,-1,51,52,53,-1,53,15,51,-1,53,50,11,-1,11,15,53,-1,48,49,55,-1,55,54,48,-1,36,40,57,-1,57,56,36,-1,40,55,58,-1,58,57,40,-1,55,49,59,-1,59,58,55,-1,49,46,60,-1,60,59,49,-1,46,50,61,-1,61,60,46,-1,50,53,62,-1,62,61,50,-1,53,52,63,-1,63,62,53,-1,52,43,64,-1,64,63,52,-1,43,44,65,-1,65,64,43,-1,44,37,66,-1,66,65,44,-1,37,38,67,-1,67,66,37,-1,38,39,68,-1,68,67,38,-1,39,41,69,-1,69,68,39,-1,41,36,56,-1,56,69,41,-1]
IndexedFaceSet198.creaseAngle = 3.14159
IndexedFaceSet198.texCoordIndex = [9,0,1,-1,1,17,9,-1,13,2,0,-1,0,9,13,-1,16,15,3,-1,3,5,16,-1,10,6,2,-1,2,13,10,-1,17,1,8,-1,8,11,17,-1,10,16,5,-1,5,6,10,-1,14,12,7,-1,7,4,14,-1,19,18,21,-1,21,20,19,-1,22,19,20,-1,20,23,22,-1,24,27,26,-1,26,25,24,-1,28,22,23,-1,23,29,28,-1,18,30,31,-1,31,21,18,-1,28,29,27,-1,27,24,28,-1,33,32,35,-1,35,34,33,-1,1,0,37,-1,37,36,1,-1,0,2,38,-1,38,37,0,-1,2,6,39,-1,39,38,2,-1,6,5,40,-1,40,39,6,-1,5,3,41,-1,41,40,5,-1,4,7,42,-1,42,41,4,-1,35,32,43,-1,43,42,35,-1,26,27,44,-1,44,43,26,-1,27,29,45,-1,45,44,27,-1,29,23,46,-1,46,45,29,-1,23,20,47,-1,47,46,23,-1,20,21,48,-1,48,47,20,-1,21,31,49,-1,49,48,21,-1,8,1,36,-1,36,49,8,-1,56,60,66,-1,66,57,56,-1,51,50,64,-1,64,59,51,-1,65,52,51,-1,51,59,65,-1,54,53,62,-1,62,61,54,-1,53,55,63,-1,63,62,53,-1,63,55,52,-1,52,65,63,-1,50,58,67,-1,67,64,50,-1,68,71,70,-1,70,69,68,-1,73,72,75,-1,75,74,73,-1,76,72,73,-1,73,77,76,-1,79,78,81,-1,81,80,79,-1,80,81,83,-1,83,82,80,-1,83,76,77,-1,77,82,83,-1,74,75,85,-1,85,84,74,-1,59,64,87,-1,87,86,59,-1,64,67,88,-1,88,87,64,-1,85,75,89,-1,89,88,85,-1,75,72,90,-1,90,89,75,-1,72,76,91,-1,91,90,72,-1,76,83,92,-1,92,91,76,-1,83,81,93,-1,93,92,83,-1,81,78,94,-1,94,93,81,-1,69,70,95,-1,95,94,69,-1,66,60,96,-1,96,95,66,-1,61,62,97,-1,97,96,61,-1,62,63,98,-1,98,97,62,-1,63,65,99,-1,99,98,63,-1,65,59,86,-1,86,99,65,-1]
Coordinate199 = x3d.Coordinate()

IndexedFaceSet198.coord = Coordinate199
TextureCoordinate200 = x3d.TextureCoordinate()

IndexedFaceSet198.texCoord = TextureCoordinate200

Shape194.geometry = IndexedFaceSet198

Transform193.children.append(Shape194)

HAnimSegment192.children.append(Transform193)

HAnimJoint191.children.append(HAnimSegment192)
HAnimJoint201 = x3d.HAnimJoint()
HAnimJoint201.name = "vt10"
HAnimJoint201.DEF = "hanim_vt10"
HAnimJoint201.center = [0,44.580002,-0.6127]
HAnimJoint201.ulimit = [0,0,0]
HAnimJoint201.llimit = [0,0,0]
HAnimSegment202 = x3d.HAnimSegment()
HAnimSegment202.name = "t10"
HAnimSegment202.DEF = "hanim_t10"
Transform203 = x3d.Transform()
Transform203.translation = [0,44.580002,-0.6127]
Shape204 = x3d.Shape()
Appearance205 = x3d.Appearance()
Material206 = x3d.Material()
Material206.diffuseColor = [0.588,0.588,0.588]

Appearance205.material = Material206
ImageTexture207 = x3d.ImageTexture()
ImageTexture207.USE = "JinLOA2TextureAtlas"

Appearance205.texture = ImageTexture207

Shape204.appearance = Appearance205
IndexedFaceSet208 = x3d.IndexedFaceSet()
IndexedFaceSet208.coordIndex = [0,3,9,-1,9,8,0,-1,3,4,10,-1,10,9,3,-1,4,2,11,-1,11,10,4,-1,2,1,12,-1,12,11,2,-1,1,5,13,-1,13,12,1,-1,5,7,14,-1,14,13,5,-1,6,0,8,-1,8,47,6,-1,19,18,5,-1,5,1,19,-1,20,19,1,-1,1,2,20,-1,20,2,4,-1,4,16,20,-1,21,0,6,-1,6,63,21,-1,63,17,15,-1,15,21,63,-1,15,3,0,-1,0,21,15,-1,18,53,7,-1,7,5,18,-1,16,4,3,-1,3,15,16,-1,19,20,27,-1,27,26,19,-1,53,18,25,-1,25,58,53,-1,22,15,17,-1,17,23,22,-1,24,16,15,-1,15,22,24,-1,18,19,26,-1,26,25,18,-1,20,16,24,-1,24,27,20,-1,17,63,64,-1,64,23,17,-1,22,23,29,-1,29,28,22,-1,23,64,30,-1,30,29,23,-1,58,25,31,-1,31,68,58,-1,25,26,32,-1,32,31,25,-1,26,27,33,-1,33,32,26,-1,27,24,34,-1,34,33,27,-1,24,22,28,-1,28,34,24,-1,39,42,41,-1,41,40,39,-1,40,41,43,-1,43,38,40,-1,38,43,44,-1,44,37,38,-1,37,44,45,-1,45,36,37,-1,36,45,46,-1,46,35,36,-1,35,46,14,-1,14,7,35,-1,6,47,42,-1,42,39,6,-1,54,36,35,-1,35,48,54,-1,49,37,36,-1,36,54,49,-1,38,37,49,-1,49,50,38,-1,6,39,51,-1,51,63,6,-1,63,51,60,-1,60,52,63,-1,39,40,60,-1,60,51,39,-1,7,53,48,-1,48,35,7,-1,40,38,50,-1,50,60,40,-1,54,56,55,-1,55,49,54,-1,53,58,57,-1,57,48,53,-1,59,61,52,-1,52,60,59,-1,62,59,60,-1,60,50,62,-1,48,57,56,-1,56,54,48,-1,49,55,62,-1,62,50,49,-1,52,61,64,-1,64,63,52,-1,59,66,65,-1,65,61,59,-1,61,65,30,-1,30,64,61,-1,58,68,67,-1,67,57,58,-1,57,67,69,-1,69,56,57,-1,56,69,70,-1,70,55,56,-1,55,70,71,-1,71,62,55,-1,62,71,66,-1,66,59,62,-1]
IndexedFaceSet208.creaseAngle = 3.14159
IndexedFaceSet208.texCoordIndex = [0,4,10,-1,10,9,0,-1,4,5,11,-1,11,10,4,-1,5,2,12,-1,12,11,5,-1,2,1,13,-1,13,12,2,-1,1,6,14,-1,14,13,1,-1,7,3,15,-1,15,14,7,-1,8,0,9,-1,9,16,8,-1,23,22,6,-1,6,1,23,-1,24,23,1,-1,1,2,24,-1,24,2,5,-1,5,20,24,-1,25,0,8,-1,8,27,25,-1,27,17,18,-1,18,25,27,-1,19,4,0,-1,0,25,19,-1,21,26,3,-1,3,7,21,-1,20,5,4,-1,4,19,20,-1,33,34,43,-1,43,42,33,-1,35,32,40,-1,40,44,35,-1,37,28,30,-1,30,38,37,-1,39,29,28,-1,28,37,39,-1,31,33,42,-1,42,41,31,-1,34,29,39,-1,39,43,34,-1,30,36,45,-1,45,38,30,-1,37,38,47,-1,47,46,37,-1,38,45,48,-1,48,47,38,-1,44,40,50,-1,50,49,44,-1,41,42,51,-1,51,50,41,-1,42,43,52,-1,52,51,42,-1,43,39,53,-1,53,52,43,-1,39,37,46,-1,46,53,39,-1,58,64,63,-1,63,60,58,-1,60,63,65,-1,65,57,60,-1,57,65,66,-1,66,56,57,-1,56,66,67,-1,67,55,56,-1,55,67,68,-1,68,54,55,-1,61,68,69,-1,69,62,61,-1,59,70,64,-1,64,58,59,-1,71,55,54,-1,54,72,71,-1,73,56,55,-1,55,71,73,-1,57,56,73,-1,73,74,57,-1,59,58,76,-1,76,75,59,-1,75,76,77,-1,77,78,75,-1,58,60,79,-1,79,76,58,-1,62,81,80,-1,80,61,62,-1,60,57,74,-1,74,79,60,-1,82,85,84,-1,84,83,82,-1,86,89,88,-1,88,87,86,-1,90,93,92,-1,92,91,90,-1,94,90,91,-1,91,95,94,-1,97,96,85,-1,85,82,97,-1,83,84,94,-1,94,95,83,-1,92,93,99,-1,99,98,92,-1,90,101,100,-1,100,93,90,-1,93,100,102,-1,102,99,93,-1,89,104,103,-1,103,88,89,-1,96,103,105,-1,105,85,96,-1,85,105,106,-1,106,84,85,-1,84,106,107,-1,107,94,84,-1,94,107,101,-1,101,90,94,-1]
Coordinate209 = x3d.Coordinate()

IndexedFaceSet208.coord = Coordinate209
TextureCoordinate210 = x3d.TextureCoordinate()

IndexedFaceSet208.texCoord = TextureCoordinate210

Shape204.geometry = IndexedFaceSet208

Transform203.children.append(Shape204)

HAnimSegment202.children.append(Transform203)

HAnimJoint201.children.append(HAnimSegment202)
HAnimJoint211 = x3d.HAnimJoint()
HAnimJoint211.name = "vt6"
HAnimJoint211.DEF = "hanim_vt6"
HAnimJoint211.center = [0,47.040001,-0.6117]
HAnimJoint211.ulimit = [0,0,0]
HAnimJoint211.llimit = [0,0,0]
HAnimSegment212 = x3d.HAnimSegment()
HAnimSegment212.name = "t6"
HAnimSegment212.DEF = "hanim_t6"
Transform213 = x3d.Transform()
Transform213.translation = [0,47.040001,-0.6117]
Shape214 = x3d.Shape()
Appearance215 = x3d.Appearance()
Material216 = x3d.Material()
Material216.diffuseColor = [0.588,0.588,0.588]

Appearance215.material = Material216
ImageTexture217 = x3d.ImageTexture()
ImageTexture217.USE = "JinLOA2TextureAtlas"

Appearance215.texture = ImageTexture217

Shape214.appearance = Appearance215
IndexedFaceSet218 = x3d.IndexedFaceSet()
IndexedFaceSet218.coordIndex = [0,18,53,-1,53,6,0,-1,3,5,9,-1,9,8,3,-1,5,1,10,-1,10,9,5,-1,1,2,11,-1,11,10,1,-1,2,4,12,-1,12,11,2,-1,4,0,13,-1,13,12,4,-1,0,6,46,-1,46,13,0,-1,7,3,8,-1,8,14,7,-1,17,1,5,-1,5,15,17,-1,16,3,7,-1,7,19,16,-1,0,4,20,-1,20,18,0,-1,4,2,21,-1,21,20,4,-1,21,2,1,-1,1,17,21,-1,16,15,5,-1,5,3,16,-1,18,20,23,-1,23,27,18,-1,25,15,16,-1,16,22,25,-1,27,57,53,-1,53,18,27,-1,25,26,17,-1,17,15,25,-1,23,20,21,-1,21,24,23,-1,21,17,26,-1,26,24,21,-1,22,16,19,-1,19,61,22,-1,25,22,29,-1,29,28,25,-1,22,61,64,-1,64,29,22,-1,57,27,30,-1,30,66,57,-1,27,23,31,-1,31,30,27,-1,23,24,32,-1,32,31,23,-1,24,26,33,-1,33,32,24,-1,26,25,28,-1,28,33,26,-1,6,53,52,-1,52,38,6,-1,39,48,49,-1,49,36,39,-1,39,38,52,-1,52,48,39,-1,35,41,40,-1,40,34,35,-1,34,40,42,-1,42,37,34,-1,37,42,43,-1,43,36,37,-1,36,43,44,-1,44,39,36,-1,39,44,45,-1,45,38,39,-1,38,45,46,-1,46,6,38,-1,7,14,41,-1,41,35,7,-1,47,51,34,-1,34,37,47,-1,19,7,35,-1,35,50,19,-1,47,37,36,-1,36,49,47,-1,35,34,51,-1,51,50,35,-1,60,58,47,-1,47,49,60,-1,50,51,55,-1,55,54,50,-1,53,57,56,-1,56,52,53,-1,47,58,55,-1,55,51,47,-1,59,48,52,-1,52,56,59,-1,60,49,48,-1,48,59,60,-1,54,61,19,-1,19,50,54,-1,55,63,62,-1,62,54,55,-1,54,62,64,-1,64,61,54,-1,57,66,65,-1,65,56,57,-1,56,65,67,-1,67,59,56,-1,59,67,68,-1,68,60,59,-1,60,68,69,-1,69,58,60,-1,58,69,63,-1,63,55,58,-1]
IndexedFaceSet218.creaseAngle = 3.14159
IndexedFaceSet218.texCoordIndex = [1,133,134,-1,134,5,1,-1,4,8,17,-1,17,16,4,-1,8,2,18,-1,18,17,8,-1,2,3,19,-1,19,18,2,-1,3,7,20,-1,20,19,3,-1,7,0,21,-1,21,20,7,-1,1,5,22,-1,22,21,1,-1,6,4,16,-1,16,23,6,-1,26,2,8,-1,8,24,26,-1,25,4,6,-1,6,30,25,-1,0,7,28,-1,28,27,0,-1,7,3,29,-1,29,28,7,-1,29,3,2,-1,2,26,29,-1,25,24,8,-1,8,4,25,-1,35,37,107,-1,107,108,35,-1,118,31,32,-1,32,115,118,-1,116,117,39,-1,39,36,116,-1,118,119,34,-1,34,31,118,-1,110,37,38,-1,38,109,110,-1,38,34,111,-1,111,112,38,-1,114,32,33,-1,33,113,114,-1,44,40,50,-1,50,49,44,-1,40,48,51,-1,51,50,40,-1,43,47,53,-1,53,52,43,-1,46,41,54,-1,54,53,46,-1,41,42,55,-1,55,54,41,-1,42,45,56,-1,56,55,42,-1,45,44,49,-1,49,56,45,-1,12,135,136,-1,136,11,12,-1,13,79,80,-1,80,9,13,-1,13,14,78,-1,78,79,13,-1,58,67,66,-1,66,57,58,-1,57,66,15,-1,15,10,57,-1,60,68,69,-1,69,59,60,-1,59,69,70,-1,70,64,59,-1,64,70,71,-1,71,65,64,-1,61,71,72,-1,72,62,61,-1,63,73,67,-1,67,58,63,-1,74,75,57,-1,57,10,74,-1,77,63,58,-1,58,76,77,-1,74,10,9,-1,9,80,74,-1,58,57,75,-1,75,76,58,-1,120,121,85,-1,85,88,120,-1,81,82,118,-1,118,122,81,-1,84,123,124,-1,124,83,84,-1,85,125,126,-1,126,82,85,-1,128,87,86,-1,86,127,128,-1,130,88,87,-1,87,129,130,-1,131,132,89,-1,89,81,131,-1,91,100,99,-1,99,90,91,-1,90,99,101,-1,101,98,90,-1,93,103,102,-1,102,92,93,-1,95,102,104,-1,104,96,95,-1,96,104,105,-1,105,97,96,-1,97,105,106,-1,106,94,97,-1,94,106,100,-1,100,91,94,-1]
Coordinate219 = x3d.Coordinate()

IndexedFaceSet218.coord = Coordinate219
TextureCoordinate220 = x3d.TextureCoordinate()

IndexedFaceSet218.texCoord = TextureCoordinate220

Shape214.geometry = IndexedFaceSet218

Transform213.children.append(Shape214)

HAnimSegment212.children.append(Transform213)

HAnimJoint211.children.append(HAnimSegment212)
HAnimJoint221 = x3d.HAnimJoint()
HAnimJoint221.name = "vt1"
HAnimJoint221.DEF = "hanim_vt1"
HAnimJoint221.center = [0,49.619999,-0.6117]
HAnimJoint221.ulimit = [0,0,0]
HAnimJoint221.llimit = [0,0,0]
HAnimSegment222 = x3d.HAnimSegment()
HAnimSegment222.name = "t1"
HAnimSegment222.DEF = "hanim_t1"
Transform223 = x3d.Transform()
Transform223.translation = [0,49.619999,-0.6117]
Shape224 = x3d.Shape()
Appearance225 = x3d.Appearance()
Material226 = x3d.Material()
Material226.diffuseColor = [0.588,0.588,0.588]

Appearance225.material = Material226
ImageTexture227 = x3d.ImageTexture()
ImageTexture227.USE = "JinLOA2TextureAtlas"

Appearance225.texture = ImageTexture227

Shape224.appearance = Appearance225
IndexedFaceSet228 = x3d.IndexedFaceSet()
IndexedFaceSet228.coordIndex = [1,5,3,-1,3,2,1,-1,5,6,3,-1,7,22,3,-1,3,6,7,-1,0,1,2,-1,76,36,34,-1,34,4,76,-1,5,1,9,-1,1,0,9,-1,30,78,9,-1,76,4,9,-1,4,5,9,-1,32,23,33,-1,33,43,32,-1,22,7,33,-1,33,23,22,-1,5,4,34,-1,34,6,5,-1,24,32,8,-1,78,30,11,-1,11,84,78,-1,30,0,12,-1,12,11,30,-1,14,13,15,-1,15,16,14,-1,13,22,23,-1,23,15,13,-1,10,2,13,-1,22,13,2,-1,2,3,22,-1,16,15,24,-1,24,8,16,-1,15,23,32,-1,32,24,15,-1,0,10,12,-1,18,17,20,-1,20,92,18,-1,17,19,21,-1,21,20,17,-1,19,14,16,-1,16,21,19,-1,17,18,84,-1,84,11,17,-1,19,17,11,-1,11,12,19,-1,12,14,19,-1,92,20,25,-1,25,97,92,-1,20,21,28,-1,28,25,20,-1,21,16,8,-1,8,28,21,-1,0,2,10,-1,12,10,14,-1,13,14,10,-1,100,31,27,-1,27,26,100,-1,25,28,27,-1,28,8,29,-1,28,29,26,-1,26,27,28,-1,27,31,97,-1,97,25,27,-1,9,0,30,-1,7,35,45,-1,45,33,7,-1,35,7,6,-1,6,34,35,-1,116,35,34,-1,34,36,116,-1,37,8,41,-1,41,40,37,-1,8,42,41,-1,26,37,40,-1,40,44,26,-1,39,32,43,-1,100,26,44,-1,44,111,100,-1,32,39,42,-1,42,8,32,-1,46,118,38,-1,38,45,46,-1,118,119,52,-1,52,38,118,-1,111,44,47,-1,47,50,111,-1,53,47,44,-1,44,40,53,-1,45,35,116,-1,116,46,45,-1,43,33,45,-1,45,38,43,-1,39,49,51,-1,51,42,39,-1,39,43,48,-1,48,49,39,-1,43,38,52,-1,52,48,43,-1,53,40,41,-1,51,53,41,-1,41,42,51,-1,47,54,122,-1,122,50,47,-1,119,58,57,-1,57,52,119,-1,60,55,49,-1,49,48,60,-1,56,59,53,-1,53,51,56,-1,53,59,54,-1,54,47,53,-1,48,52,57,-1,57,60,48,-1,51,49,55,-1,55,56,51,-1,60,57,62,-1,62,61,60,-1,57,58,134,-1,134,62,57,-1,122,54,63,-1,63,136,122,-1,54,59,64,-1,64,63,54,-1,59,56,65,-1,65,64,59,-1,56,55,66,-1,66,65,56,-1,55,60,61,-1,61,66,55,-1,69,68,67,-1,67,70,69,-1,70,67,71,-1,72,71,67,-1,67,73,72,-1,74,68,69,-1,103,36,76,-1,76,75,103,-1,70,9,69,-1,69,9,74,-1,77,9,78,-1,76,9,75,-1,75,9,70,-1,79,110,104,-1,104,80,79,-1,104,72,73,-1,73,80,104,-1,103,75,70,-1,70,71,103,-1,81,82,79,-1,78,84,83,-1,83,77,78,-1,77,83,85,-1,85,74,77,-1,88,87,86,-1,86,89,88,-1,89,86,80,-1,80,73,89,-1,90,89,68,-1,73,67,68,-1,68,89,73,-1,87,82,81,-1,81,86,87,-1,86,81,79,-1,79,80,86,-1,74,85,90,-1,18,92,91,-1,91,93,18,-1,93,91,94,-1,94,95,93,-1,94,98,82,-1,82,87,94,-1,93,83,84,-1,84,18,93,-1,95,85,83,-1,83,93,95,-1,85,95,88,-1,92,97,96,-1,96,91,92,-1,91,96,98,-1,98,94,91,-1,74,90,68,-1,85,88,90,-1,89,90,88,-1,100,99,101,-1,101,31,100,-1,96,101,98,-1,98,102,82,-1,98,101,99,-1,99,102,98,-1,101,96,97,-1,97,31,101,-1,9,77,74,-1,72,104,108,-1,108,105,72,-1,105,103,71,-1,71,72,105,-1,116,36,103,-1,103,105,116,-1,106,114,113,-1,113,82,106,-1,82,113,115,-1,99,112,114,-1,114,106,99,-1,109,110,79,-1,100,111,112,-1,112,99,100,-1,79,82,115,-1,115,109,79,-1,46,108,107,-1,107,118,46,-1,113,131,128,-1,128,115,113,-1,116,105,108,-1,108,46,116,-1,108,104,110,-1,110,107,108,-1,109,115,128,-1,128,127,109,-1,127,117,110,-1,110,109,127,-1,124,107,110,-1,110,117,124,-1,112,111,50,-1,50,120,112,-1,131,114,112,-1,112,120,131,-1,118,107,124,-1,124,119,118,-1,113,114,131,-1,120,50,122,-1,122,121,120,-1,119,124,123,-1,123,58,119,-1,125,117,127,-1,127,126,125,-1,129,128,131,-1,131,130,129,-1,131,120,121,-1,121,130,131,-1,117,125,123,-1,123,124,117,-1,128,129,126,-1,126,127,128,-1,125,133,132,-1,132,123,125,-1,123,132,134,-1,134,58,123,-1,122,136,135,-1,135,121,122,-1,121,135,137,-1,137,130,121,-1,130,137,138,-1,138,129,130,-1,129,138,139,-1,139,126,129,-1,126,139,133,-1,133,125,126,-1,87,88,95,-1,95,94,87,-1]
IndexedFaceSet228.creaseAngle = 3.14159
IndexedFaceSet228.texCoordIndex = [14,15,0,-1,0,16,14,-1,15,19,0,-1,21,10,11,-1,11,18,21,-1,5,2,1,-1,6,281,282,-1,282,4,6,-1,3,2,13,-1,2,5,13,-1,66,7,13,-1,6,4,17,-1,4,15,17,-1,20,9,70,-1,70,89,20,-1,10,21,70,-1,70,9,10,-1,15,4,283,-1,283,19,15,-1,12,20,22,-1,48,47,26,-1,26,27,48,-1,47,49,28,-1,28,26,47,-1,31,32,29,-1,29,30,31,-1,32,53,54,-1,54,29,32,-1,33,50,32,-1,53,32,50,-1,50,51,53,-1,30,29,55,-1,55,56,30,-1,29,54,52,-1,52,55,29,-1,49,33,28,-1,36,41,40,-1,40,35,36,-1,37,39,38,-1,38,34,37,-1,39,31,30,-1,30,38,39,-1,42,36,43,-1,43,45,42,-1,39,37,26,-1,26,28,39,-1,28,31,39,-1,35,44,57,-1,57,46,35,-1,34,38,65,-1,65,58,34,-1,38,30,56,-1,56,65,38,-1,49,50,33,-1,28,33,31,-1,32,31,33,-1,62,63,64,-1,64,61,62,-1,57,65,64,-1,65,56,60,-1,65,60,61,-1,61,64,65,-1,64,63,59,-1,59,57,64,-1,13,8,66,-1,71,72,93,-1,93,70,71,-1,72,71,73,-1,73,74,72,-1,94,72,74,-1,74,77,94,-1,81,76,87,-1,87,86,81,-1,76,88,87,-1,80,81,86,-1,86,90,80,-1,85,75,89,-1,78,79,91,-1,91,92,78,-1,75,85,88,-1,88,76,75,-1,97,107,96,-1,96,95,97,-1,24,118,114,-1,114,23,24,-1,106,105,109,-1,109,116,106,-1,115,110,104,-1,104,100,115,-1,95,288,98,-1,98,97,95,-1,89,70,93,-1,93,287,89,-1,99,117,112,-1,112,102,99,-1,99,103,113,-1,113,117,99,-1,103,23,114,-1,114,113,103,-1,115,100,101,-1,111,115,101,-1,101,102,111,-1,124,129,133,-1,133,121,124,-1,127,134,132,-1,132,126,127,-1,136,130,122,-1,122,125,136,-1,131,135,119,-1,119,123,131,-1,119,135,128,-1,128,120,119,-1,125,126,132,-1,132,136,125,-1,123,122,130,-1,130,131,123,-1,136,132,138,-1,138,137,136,-1,132,134,139,-1,139,138,132,-1,133,129,141,-1,141,140,133,-1,128,135,142,-1,142,141,128,-1,135,131,143,-1,143,142,135,-1,131,130,144,-1,144,143,131,-1,130,136,137,-1,137,144,130,-1,147,146,145,-1,145,148,147,-1,148,145,149,-1,152,151,150,-1,150,153,152,-1,154,156,155,-1,284,285,158,-1,158,157,284,-1,159,160,155,-1,155,160,154,-1,161,160,162,-1,158,163,157,-1,157,163,148,-1,164,215,210,-1,210,165,164,-1,210,152,153,-1,153,165,210,-1,286,157,148,-1,148,149,286,-1,166,167,164,-1,170,169,168,-1,168,171,170,-1,171,168,172,-1,172,173,171,-1,176,175,174,-1,174,177,176,-1,177,174,178,-1,178,179,177,-1,180,177,181,-1,179,182,181,-1,181,177,179,-1,175,184,183,-1,183,174,175,-1,174,183,185,-1,185,178,174,-1,173,172,180,-1,188,187,186,-1,186,189,188,-1,192,191,190,-1,190,193,192,-1,190,200,184,-1,184,175,190,-1,196,195,194,-1,194,188,196,-1,193,172,168,-1,168,192,193,-1,172,193,176,-1,187,198,197,-1,197,199,187,-1,191,201,200,-1,200,190,191,-1,173,180,181,-1,172,176,180,-1,177,180,176,-1,203,202,205,-1,205,204,203,-1,197,205,200,-1,200,206,184,-1,200,205,202,-1,202,206,200,-1,205,197,207,-1,207,204,205,-1,160,161,208,-1,211,210,209,-1,209,212,211,-1,212,214,213,-1,213,211,212,-1,218,217,214,-1,214,212,218,-1,219,222,221,-1,221,220,219,-1,220,221,223,-1,225,224,222,-1,222,219,225,-1,226,215,216,-1,228,227,230,-1,230,229,228,-1,216,220,223,-1,223,226,216,-1,234,233,232,-1,232,231,234,-1,239,249,253,-1,253,241,239,-1,243,289,233,-1,233,234,243,-1,209,210,215,-1,215,290,209,-1,235,241,254,-1,254,244,235,-1,244,245,236,-1,236,235,244,-1,246,25,236,-1,236,245,246,-1,238,237,248,-1,248,247,238,-1,249,240,242,-1,242,250,249,-1,251,25,246,-1,246,252,251,-1,239,240,249,-1,256,255,68,-1,68,67,256,-1,259,262,261,-1,261,260,259,-1,264,263,266,-1,266,69,264,-1,82,267,270,-1,270,83,82,-1,270,272,84,-1,84,83,270,-1,263,264,261,-1,261,262,263,-1,267,82,69,-1,69,266,267,-1,264,274,273,-1,273,261,264,-1,261,273,275,-1,275,260,261,-1,258,277,276,-1,276,257,258,-1,271,276,278,-1,278,269,271,-1,269,278,279,-1,279,268,269,-1,268,279,280,-1,280,265,268,-1,69,108,274,-1,274,264,69,-1,175,176,193,-1,193,190,175,-1]
Coordinate229 = x3d.Coordinate()

IndexedFaceSet228.coord = Coordinate229
TextureCoordinate230 = x3d.TextureCoordinate()

IndexedFaceSet228.texCoord = TextureCoordinate230

Shape224.geometry = IndexedFaceSet228

Transform223.children.append(Shape224)

HAnimSegment222.children.append(Transform223)

HAnimJoint221.children.append(HAnimSegment222)
HAnimJoint231 = x3d.HAnimJoint()
HAnimJoint231.name = "l_acromioclavicular"
HAnimJoint231.DEF = "hanim_l_acromioclavicular"
HAnimJoint231.center = [1.71,52.82,-0.6127]
HAnimJoint231.ulimit = [0,0,0]
HAnimJoint231.llimit = [0,0,0]
HAnimSegment232 = x3d.HAnimSegment()
HAnimSegment232.name = "l_clavicle"
HAnimSegment232.DEF = "hanim_l_clavicle"
Transform233 = x3d.Transform()
Transform233.translation = [1.71,52.82,-0.6127]
Shape234 = x3d.Shape()
Appearance235 = x3d.Appearance()
Material236 = x3d.Material()
Material236.diffuseColor = [0.588,0.588,0.588]

Appearance235.material = Material236
ImageTexture237 = x3d.ImageTexture()
ImageTexture237.USE = "JinLOA2TextureAtlas"

Appearance235.texture = ImageTexture237

Shape234.appearance = Appearance235
IndexedFaceSet238 = x3d.IndexedFaceSet()
IndexedFaceSet238.coordIndex = [9,6,1,-1,1,0,9,-1,6,5,2,-1,2,1,6,-1,8,3,2,-1,2,5,8,-1,8,7,4,-1,4,3,8,-1,9,0,4,-1,4,7,9,-1,2,3,4,-1,2,4,0,-1,1,2,0,-1,13,14,10,-1,12,13,10,-1,11,12,10,-1,6,9,11,-1,11,10,6,-1,9,7,12,-1,12,11,9,-1,7,8,13,-1,13,12,7,-1,8,5,14,-1,14,13,8,-1,5,6,10,-1,10,14,5,-1]
IndexedFaceSet238.creaseAngle = 3.14159
IndexedFaceSet238.texCoordIndex = [9,6,1,-1,1,0,9,-1,6,5,2,-1,2,1,6,-1,8,3,2,-1,2,5,8,-1,8,7,4,-1,4,3,8,-1,9,0,4,-1,4,7,9,-1,2,3,4,-1,2,4,0,-1,1,2,0,-1,13,14,10,-1,12,13,10,-1,11,12,10,-1,6,9,11,-1,11,10,6,-1,9,7,12,-1,12,11,9,-1,7,8,13,-1,13,12,7,-1,8,5,14,-1,14,13,8,-1,5,6,10,-1,10,14,5,-1]
Coordinate239 = x3d.Coordinate()

IndexedFaceSet238.coord = Coordinate239
TextureCoordinate240 = x3d.TextureCoordinate()

IndexedFaceSet238.texCoord = TextureCoordinate240

Shape234.geometry = IndexedFaceSet238

Transform233.children.append(Shape234)

HAnimSegment232.children.append(Transform233)

HAnimJoint231.children.append(HAnimSegment232)
HAnimJoint241 = x3d.HAnimJoint()
HAnimJoint241.name = "l_sternoclavicular"
HAnimJoint241.DEF = "hanim_l_sternoclavicular"
HAnimJoint241.center = [5.464,52.060001,-0.5732]
HAnimJoint241.ulimit = [0,0,0]
HAnimJoint241.llimit = [0,0,0]
HAnimSegment242 = x3d.HAnimSegment()
HAnimSegment242.name = "l_scapula"
HAnimSegment242.DEF = "hanim_l_scapula"
Transform243 = x3d.Transform()
Transform243.translation = [5.464,52.060001,-0.5732]
Shape244 = x3d.Shape()
Appearance245 = x3d.Appearance()
Material246 = x3d.Material()
Material246.diffuseColor = [0.588,0.588,0.588]

Appearance245.material = Material246
ImageTexture247 = x3d.ImageTexture()
ImageTexture247.USE = "JinLOA2TextureAtlas"

Appearance245.texture = ImageTexture247

Shape244.appearance = Appearance245
IndexedFaceSet248 = x3d.IndexedFaceSet()
IndexedFaceSet248.coordIndex = [5,4,0,-1,0,1,5,-1,4,3,2,-1,2,0,4,-1,3,9,6,-1,6,2,3,-1,7,5,1,-1,1,8,7,-1,6,8,0,-1,0,2,6,-1,0,8,1,-1,9,7,8,-1,8,6,9,-1,4,5,11,-1,11,10,4,-1,5,7,12,-1,12,11,5,-1,7,9,13,-1,13,12,7,-1,9,3,14,-1,14,13,9,-1,3,4,10,-1,10,14,3,-1,10,11,15,-1,11,12,15,-1,12,13,15,-1,13,14,15,-1,14,10,15,-1]
IndexedFaceSet248.creaseAngle = 3.14159
IndexedFaceSet248.texCoordIndex = [5,4,0,-1,0,1,5,-1,4,3,2,-1,2,0,4,-1,3,8,6,-1,6,2,3,-1,9,5,1,-1,1,7,9,-1,6,7,0,-1,0,2,6,-1,0,7,1,-1,12,13,11,-1,11,10,12,-1,4,5,15,-1,15,14,4,-1,5,9,16,-1,16,15,5,-1,13,12,17,-1,17,16,13,-1,8,3,18,-1,18,17,8,-1,3,4,14,-1,14,18,3,-1,14,15,19,-1,15,16,19,-1,16,17,19,-1,17,18,19,-1,18,14,19,-1]
Coordinate249 = x3d.Coordinate()

IndexedFaceSet248.coord = Coordinate249
TextureCoordinate250 = x3d.TextureCoordinate()

IndexedFaceSet248.texCoord = TextureCoordinate250

Shape244.geometry = IndexedFaceSet248

Transform243.children.append(Shape244)

HAnimSegment242.children.append(Transform243)

HAnimJoint241.children.append(HAnimSegment242)
HAnimJoint251 = x3d.HAnimJoint()
HAnimJoint251.name = "l_shoulder"
HAnimJoint251.DEF = "hanim_l_shoulder"
HAnimJoint251.center = [7.336,51.48,-0.1452]
HAnimJoint251.ulimit = [0,0,0]
HAnimJoint251.llimit = [0,0,0]
HAnimSegment252 = x3d.HAnimSegment()
HAnimSegment252.name = "l_upperarm"
HAnimSegment252.DEF = "hanim_l_upperarm"
Transform253 = x3d.Transform()
Transform253.translation = [7.336,51.48,-0.1452]
Shape254 = x3d.Shape()
Appearance255 = x3d.Appearance()
Material256 = x3d.Material()
Material256.diffuseColor = [0.588,0.588,0.588]

Appearance255.material = Material256
ImageTexture257 = x3d.ImageTexture()
ImageTexture257.USE = "JinLOA2TextureAtlas"

Appearance255.texture = ImageTexture257

Shape254.appearance = Appearance255
IndexedFaceSet258 = x3d.IndexedFaceSet()
IndexedFaceSet258.coordIndex = [2,1,0,-1,3,2,0,-1,4,3,0,-1,0,1,6,-1,6,5,0,-1,1,2,7,-1,7,6,1,-1,2,3,8,-1,8,7,2,-1,3,4,9,-1,9,8,3,-1,4,0,5,-1,5,9,4,-1,5,6,11,-1,11,10,5,-1,6,7,12,-1,12,11,6,-1,7,8,13,-1,13,12,7,-1,8,9,14,-1,14,13,8,-1,9,5,10,-1,10,14,9,-1,10,11,16,-1,16,15,10,-1,11,12,17,-1,17,16,11,-1,12,13,18,-1,18,17,12,-1,13,14,19,-1,19,18,13,-1,14,10,15,-1,15,19,14,-1,36,37,38,-1,35,36,38,-1,39,35,38,-1,21,20,15,-1,15,16,21,-1,22,21,16,-1,16,17,22,-1,23,22,17,-1,17,18,23,-1,24,23,18,-1,18,19,24,-1,20,24,19,-1,19,15,20,-1,26,25,20,-1,20,21,26,-1,27,26,21,-1,21,22,27,-1,28,27,22,-1,22,23,28,-1,29,28,23,-1,23,24,29,-1,25,29,24,-1,24,20,25,-1,31,30,25,-1,25,26,31,-1,32,31,26,-1,26,27,32,-1,33,32,27,-1,27,28,33,-1,34,33,28,-1,28,29,34,-1,30,34,29,-1,29,25,30,-1,36,35,30,-1,30,31,36,-1,37,36,31,-1,31,32,37,-1,38,37,32,-1,32,33,38,-1,39,38,33,-1,33,34,39,-1,35,39,34,-1,34,30,35,-1]
IndexedFaceSet258.creaseAngle = 3.14159
IndexedFaceSet258.texCoordIndex = [2,0,1,-1,3,2,1,-1,61,3,1,-1,1,0,5,-1,5,6,1,-1,0,2,7,-1,7,5,0,-1,2,3,8,-1,8,7,2,-1,25,4,9,-1,9,26,25,-1,4,1,6,-1,6,9,4,-1,6,5,10,-1,10,11,6,-1,5,7,12,-1,12,10,5,-1,7,8,13,-1,13,12,7,-1,27,9,14,-1,14,28,27,-1,9,6,11,-1,11,14,9,-1,11,10,15,-1,15,16,11,-1,10,12,17,-1,17,15,10,-1,12,13,18,-1,18,17,12,-1,29,14,19,-1,19,30,29,-1,14,11,16,-1,16,19,14,-1,54,35,36,-1,53,54,36,-1,37,53,36,-1,20,21,16,-1,16,15,20,-1,22,20,15,-1,15,17,22,-1,23,22,17,-1,17,18,23,-1,24,32,31,-1,31,19,24,-1,21,24,19,-1,19,16,21,-1,40,41,38,-1,38,39,40,-1,43,56,55,-1,55,42,43,-1,45,43,42,-1,42,44,45,-1,47,45,44,-1,44,46,47,-1,41,47,46,-1,46,38,41,-1,48,49,41,-1,41,40,48,-1,50,58,57,-1,57,43,50,-1,51,50,43,-1,43,45,51,-1,52,51,45,-1,45,47,52,-1,49,52,47,-1,47,41,49,-1,34,33,49,-1,49,48,34,-1,35,60,59,-1,59,50,35,-1,36,35,50,-1,50,51,36,-1,37,36,51,-1,51,52,37,-1,33,37,52,-1,52,49,33,-1]
Coordinate259 = x3d.Coordinate()

IndexedFaceSet258.coord = Coordinate259
TextureCoordinate260 = x3d.TextureCoordinate()

IndexedFaceSet258.texCoord = TextureCoordinate260

Shape254.geometry = IndexedFaceSet258

Transform253.children.append(Shape254)

HAnimSegment252.children.append(Transform253)

HAnimJoint251.children.append(HAnimSegment252)
HAnimJoint261 = x3d.HAnimJoint()
HAnimJoint261.name = "l_elbow"
HAnimJoint261.DEF = "hanim_l_elbow"
HAnimJoint261.center = [8.093,40.380001,-0.2502]
HAnimJoint261.ulimit = [0,0,0]
HAnimJoint261.llimit = [0,0,0]
HAnimSegment262 = x3d.HAnimSegment()
HAnimSegment262.name = "l_forearm"
HAnimSegment262.DEF = "hanim_l_forearm"
Transform263 = x3d.Transform()
Transform263.translation = [8.093,40.380001,-0.2502]
Shape264 = x3d.Shape()
Appearance265 = x3d.Appearance()
Material266 = x3d.Material()
Material266.diffuseColor = [0.588,0.588,0.588]

Appearance265.material = Material266
ImageTexture267 = x3d.ImageTexture()
ImageTexture267.USE = "JinLOA2TextureAtlas"

Appearance265.texture = ImageTexture267

Shape264.appearance = Appearance265
IndexedFaceSet268 = x3d.IndexedFaceSet()
IndexedFaceSet268.coordIndex = [2,1,0,-1,3,2,0,-1,4,3,0,-1,0,1,6,-1,6,5,0,-1,1,2,7,-1,7,6,1,-1,2,3,8,-1,8,7,2,-1,3,4,9,-1,9,8,3,-1,4,0,5,-1,5,9,4,-1,5,6,11,-1,11,10,5,-1,6,7,12,-1,12,11,6,-1,7,8,13,-1,13,12,7,-1,8,9,14,-1,14,13,8,-1,9,5,10,-1,10,14,9,-1,10,11,16,-1,16,15,10,-1,11,12,17,-1,17,16,11,-1,12,13,18,-1,18,17,12,-1,13,14,19,-1,19,18,13,-1,14,10,15,-1,15,19,14,-1,21,22,23,-1,20,21,23,-1,24,20,23,-1,21,20,15,-1,15,16,21,-1,22,21,16,-1,16,17,22,-1,23,22,17,-1,17,18,23,-1,24,23,18,-1,18,19,24,-1,20,24,19,-1,19,15,20,-1]
IndexedFaceSet268.creaseAngle = 3.14159
IndexedFaceSet268.texCoordIndex = [2,25,26,-1,3,2,26,-1,4,3,26,-1,0,1,6,-1,6,5,0,-1,27,2,7,-1,7,28,27,-1,2,3,8,-1,8,7,2,-1,3,4,9,-1,9,8,3,-1,4,0,5,-1,5,9,4,-1,5,6,11,-1,11,10,5,-1,29,7,12,-1,12,30,29,-1,7,8,13,-1,13,12,7,-1,8,9,14,-1,14,13,8,-1,9,5,10,-1,10,14,9,-1,10,11,16,-1,16,15,10,-1,31,12,17,-1,17,32,31,-1,12,13,18,-1,18,17,12,-1,13,14,19,-1,19,18,13,-1,14,10,15,-1,15,19,14,-1,34,22,23,-1,33,34,23,-1,24,33,23,-1,21,20,15,-1,15,16,21,-1,22,36,35,-1,35,17,22,-1,23,22,17,-1,17,18,23,-1,24,23,18,-1,18,19,24,-1,20,24,19,-1,19,15,20,-1]
Coordinate269 = x3d.Coordinate()

IndexedFaceSet268.coord = Coordinate269
TextureCoordinate270 = x3d.TextureCoordinate()

IndexedFaceSet268.texCoord = TextureCoordinate270

Shape264.geometry = IndexedFaceSet268

Transform263.children.append(Shape264)

HAnimSegment262.children.append(Transform263)

HAnimJoint261.children.append(HAnimSegment262)
HAnimJoint271 = x3d.HAnimJoint()
HAnimJoint271.name = "l_radiocarpal"
HAnimJoint271.DEF = "hanim_l_radiocarpal"
HAnimJoint271.center = [7.899,31.43,-0.3809]
HAnimJoint271.ulimit = [0,0,0]
HAnimJoint271.llimit = [0,0,0]
HAnimSegment272 = x3d.HAnimSegment()
HAnimSegment272.name = "l_carpal"
HAnimSegment272.DEF = "hanim_l_carpal"
Transform273 = x3d.Transform()
Transform273.translation = [7.899,31.43,-0.3809]
Shape274 = x3d.Shape()
Appearance275 = x3d.Appearance()
Material276 = x3d.Material()
Material276.diffuseColor = [0.588,0.588,0.588]

Appearance275.material = Material276
ImageTexture277 = x3d.ImageTexture()
ImageTexture277.USE = "JinLOA2TextureAtlas"

Appearance275.texture = ImageTexture277

Shape274.appearance = Appearance275
IndexedFaceSet278 = x3d.IndexedFaceSet()
IndexedFaceSet278.coordIndex = [36,37,38,-1,38,41,36,-1,44,45,54,-1,31,4,53,-1,53,30,31,-1,6,10,11,-1,11,7,6,-1,11,10,33,-1,33,32,11,-1,34,24,7,-1,7,11,34,-1,13,17,15,-1,15,27,13,-1,25,22,35,-1,30,5,20,-1,13,34,11,-1,11,32,13,-1,23,22,28,-1,28,29,23,-1,17,16,14,-1,14,15,17,-1,18,5,53,-1,53,19,18,-1,9,8,16,-1,16,17,9,-1,14,42,43,-1,43,15,14,-1,21,16,8,-1,8,33,21,-1,21,35,22,-1,22,23,21,-1,39,40,41,-1,41,38,39,-1,26,20,24,-1,27,12,20,-1,20,26,27,-1,3,30,12,-1,12,43,3,-1,0,54,28,-1,28,25,0,-1,13,32,9,-1,9,17,13,-1,28,31,29,-1,29,42,14,-1,14,23,29,-1,16,21,23,-1,23,14,16,-1,30,3,2,-1,2,31,30,-1,8,9,32,-1,32,33,8,-1,33,10,35,-1,35,21,33,-1,35,10,6,-1,6,25,35,-1,13,27,26,-1,26,34,13,-1,34,26,24,-1,1,0,47,-1,47,46,1,-1,25,48,47,-1,47,0,25,-1,25,6,49,-1,49,48,25,-1,6,7,50,-1,50,49,6,-1,24,51,50,-1,50,7,24,-1,24,1,46,-1,46,51,24,-1,2,3,43,-1,43,42,2,-1,15,43,12,-1,12,27,15,-1,29,31,2,-1,2,42,29,-1,18,44,52,-1,52,5,18,-1,28,22,25,-1,18,19,45,-1,45,44,18,-1,1,24,52,-1,52,44,1,-1,45,4,28,-1,28,4,31,-1,45,19,4,-1,37,36,46,-1,46,47,37,-1,48,38,37,-1,37,47,48,-1,39,38,48,-1,48,49,39,-1,40,39,49,-1,49,50,40,-1,51,41,40,-1,40,50,51,-1,36,41,51,-1,51,46,36,-1,24,20,52,-1,52,20,5,-1,53,5,30,-1,53,4,19,-1,54,45,28,-1,44,54,0,-1,0,1,44,-1,20,12,30,-1]
IndexedFaceSet278.creaseAngle = 3.14159
IndexedFaceSet278.texCoordIndex = [0,1,2,-1,2,3,0,-1,4,5,6,-1,8,9,10,-1,10,7,8,-1,12,13,14,-1,14,11,12,-1,14,13,15,-1,15,16,14,-1,17,18,11,-1,11,14,17,-1,20,21,22,-1,22,19,20,-1,23,24,25,-1,7,26,27,-1,20,17,14,-1,14,16,20,-1,28,24,29,-1,29,30,28,-1,21,31,32,-1,32,22,21,-1,33,26,10,-1,10,34,33,-1,35,36,31,-1,31,21,35,-1,32,37,38,-1,38,22,32,-1,39,31,36,-1,36,15,39,-1,39,25,24,-1,24,28,39,-1,40,41,3,-1,3,2,40,-1,42,27,18,-1,19,43,27,-1,27,42,19,-1,44,7,43,-1,43,38,44,-1,45,6,29,-1,29,23,45,-1,20,16,35,-1,35,21,20,-1,29,8,30,-1,30,37,32,-1,32,28,30,-1,31,39,28,-1,28,32,31,-1,7,44,46,-1,46,8,7,-1,36,35,16,-1,16,15,36,-1,15,13,25,-1,25,39,15,-1,25,13,12,-1,12,23,25,-1,20,19,42,-1,42,17,20,-1,17,42,18,-1,47,45,48,-1,48,49,47,-1,23,50,48,-1,48,45,23,-1,23,12,51,-1,51,50,23,-1,12,11,52,-1,52,51,12,-1,18,53,52,-1,52,11,18,-1,18,47,49,-1,49,53,18,-1,46,44,38,-1,38,37,46,-1,22,38,43,-1,43,19,22,-1,30,8,46,-1,46,37,30,-1,33,4,54,-1,54,26,33,-1,29,24,23,-1,33,34,5,-1,5,4,33,-1,47,18,54,-1,54,4,47,-1,5,9,29,-1,29,9,8,-1,5,34,9,-1,1,0,49,-1,49,48,1,-1,50,2,1,-1,1,48,50,-1,40,2,50,-1,50,51,40,-1,41,40,51,-1,51,52,41,-1,53,3,41,-1,41,52,53,-1,0,3,53,-1,53,49,0,-1,18,27,54,-1,54,27,26,-1,10,26,7,-1,10,9,34,-1,6,5,29,-1,4,6,45,-1,45,47,4,-1,27,43,7,-1]
Coordinate279 = x3d.Coordinate()

IndexedFaceSet278.coord = Coordinate279
TextureCoordinate280 = x3d.TextureCoordinate()

IndexedFaceSet278.texCoord = TextureCoordinate280

Shape274.geometry = IndexedFaceSet278

Transform273.children.append(Shape274)

HAnimSegment272.children.append(Transform273)

HAnimJoint271.children.append(HAnimSegment272)
HAnimJoint281 = x3d.HAnimJoint()
HAnimJoint281.name = "l_carpometacarpal_1"
HAnimJoint281.DEF = "hanim_l_carpometacarpal_1"
HAnimJoint281.center = [8.205,29.6,1.302]
HAnimJoint281.ulimit = [0,0,0]
HAnimJoint281.llimit = [0,0,0]
HAnimSegment282 = x3d.HAnimSegment()
HAnimSegment282.name = "l_metacarpal_1"
HAnimSegment282.DEF = "hanim_l_metacarpal_1"
Transform283 = x3d.Transform()
Transform283.translation = [8.205,29.6,1.302]
Shape284 = x3d.Shape()
Appearance285 = x3d.Appearance()
Material286 = x3d.Material()
Material286.diffuseColor = [0.588,0.588,0.588]

Appearance285.material = Material286
ImageTexture287 = x3d.ImageTexture()
ImageTexture287.USE = "JinLOA2TextureAtlas"

Appearance285.texture = ImageTexture287

Shape284.appearance = Appearance285
IndexedFaceSet288 = x3d.IndexedFaceSet()
IndexedFaceSet288.coordIndex = [0,1,3,-1,3,2,0,-1,0,5,4,-1,0,2,6,-1,6,5,0,-1,2,7,6,-1,2,3,8,-1,8,7,2,-1,3,9,8,-1,3,1,10,-1,10,9,3,-1,1,11,10,-1,1,0,4,-1,4,11,1,-1,4,5,13,-1,13,12,4,-1,5,6,14,-1,14,13,5,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,4,12,-1,12,19,11,-1,12,13,21,-1,21,20,12,-1,13,14,22,-1,22,21,13,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,12,20,-1,20,27,19,-1,20,21,29,-1,29,28,20,-1,21,22,30,-1,30,29,21,-1,22,23,31,-1,31,30,22,-1,23,24,32,-1,32,31,23,-1,24,25,33,-1,33,32,24,-1,25,26,34,-1,34,33,25,-1,26,27,35,-1,35,34,26,-1,27,20,28,-1,28,35,27,-1,36,28,29,-1,36,29,30,-1,36,30,31,-1,36,31,32,-1,36,32,33,-1,36,33,34,-1,36,34,35,-1,36,35,28,-1]
IndexedFaceSet288.creaseAngle = 3.14159
IndexedFaceSet288.texCoordIndex = [0,1,2,-1,2,3,0,-1,0,4,5,-1,0,3,6,-1,6,4,0,-1,3,7,6,-1,3,2,8,-1,8,7,3,-1,2,9,8,-1,2,1,10,-1,10,9,2,-1,1,11,10,-1,1,0,5,-1,5,11,1,-1,5,4,12,-1,12,13,5,-1,4,6,14,-1,14,12,4,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,5,13,-1,13,19,11,-1,13,12,20,-1,20,21,13,-1,12,14,22,-1,22,20,12,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,13,21,-1,21,27,19,-1,21,20,28,-1,28,29,21,-1,20,22,30,-1,30,28,20,-1,22,23,31,-1,31,30,22,-1,23,24,32,-1,32,31,23,-1,24,25,33,-1,33,32,24,-1,25,26,34,-1,34,33,25,-1,26,27,35,-1,35,34,26,-1,27,21,29,-1,29,35,27,-1,36,29,28,-1,36,28,30,-1,36,30,31,-1,36,31,32,-1,36,32,33,-1,36,33,34,-1,36,34,35,-1,36,35,29,-1]
Coordinate289 = x3d.Coordinate()

IndexedFaceSet288.coord = Coordinate289
TextureCoordinate290 = x3d.TextureCoordinate()

IndexedFaceSet288.texCoord = TextureCoordinate290

Shape284.geometry = IndexedFaceSet288

Transform283.children.append(Shape284)

HAnimSegment282.children.append(Transform283)

HAnimJoint281.children.append(HAnimSegment282)
HAnimJoint291 = x3d.HAnimJoint()
HAnimJoint291.name = "l_metacarpophalangeal_1"
HAnimJoint291.DEF = "hanim_l_metacarpophalangeal_1"
HAnimJoint291.center = [8.08,28.73,1.55]
HAnimJoint291.ulimit = [0,0,0]
HAnimJoint291.llimit = [0,0,0]
HAnimSegment292 = x3d.HAnimSegment()
HAnimSegment292.name = "l_carpal_proximal_phalanx_1"
HAnimSegment292.DEF = "hanim_l_carpal_proximal_phalanx_1"
Transform293 = x3d.Transform()
Transform293.translation = [8.08,28.73,1.55]
Shape294 = x3d.Shape()
Appearance295 = x3d.Appearance()
Material296 = x3d.Material()
Material296.diffuseColor = [0.588,0.588,0.588]

Appearance295.material = Material296
ImageTexture297 = x3d.ImageTexture()
ImageTexture297.USE = "JinLOA2TextureAtlas"

Appearance295.texture = ImageTexture297

Shape294.appearance = Appearance295
IndexedFaceSet298 = x3d.IndexedFaceSet()
IndexedFaceSet298.coordIndex = [0,1,3,-1,3,2,0,-1,0,5,4,-1,0,2,6,-1,6,5,0,-1,2,7,6,-1,2,3,8,-1,8,7,2,-1,3,9,8,-1,3,1,10,-1,10,9,3,-1,1,11,10,-1,1,0,4,-1,4,11,1,-1,4,5,13,-1,13,12,4,-1,5,6,14,-1,14,13,5,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,4,12,-1,12,19,11,-1,12,13,21,-1,21,20,12,-1,13,14,22,-1,22,21,13,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,12,20,-1,20,27,19,-1,20,21,29,-1,29,28,20,-1,21,22,30,-1,30,29,21,-1,22,23,31,-1,31,30,22,-1,23,24,32,-1,32,31,23,-1,24,25,33,-1,33,32,24,-1,25,26,34,-1,34,33,25,-1,26,27,35,-1,35,34,26,-1,27,20,28,-1,28,35,27,-1,36,28,29,-1,36,29,30,-1,36,30,31,-1,36,31,32,-1,36,32,33,-1,36,33,34,-1,36,34,35,-1,36,35,28,-1]
IndexedFaceSet298.creaseAngle = 3.14159
IndexedFaceSet298.texCoordIndex = [0,1,2,-1,2,3,0,-1,0,4,5,-1,0,3,6,-1,6,4,0,-1,3,7,6,-1,3,2,8,-1,8,7,3,-1,2,9,8,-1,2,1,10,-1,10,9,2,-1,1,11,10,-1,1,0,5,-1,5,11,1,-1,5,4,12,-1,12,13,5,-1,4,6,14,-1,14,12,4,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,5,13,-1,13,19,11,-1,13,12,20,-1,20,21,13,-1,12,14,22,-1,22,20,12,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,13,21,-1,21,27,19,-1,21,20,28,-1,28,29,21,-1,20,22,30,-1,30,28,20,-1,22,23,31,-1,31,30,22,-1,23,24,32,-1,32,31,23,-1,24,25,33,-1,33,32,24,-1,25,26,34,-1,34,33,25,-1,26,27,35,-1,35,34,26,-1,27,21,29,-1,29,35,27,-1,36,29,28,-1,36,28,30,-1,36,30,31,-1,36,31,32,-1,36,32,33,-1,36,33,34,-1,36,34,35,-1,36,35,29,-1]
Coordinate299 = x3d.Coordinate()

IndexedFaceSet298.coord = Coordinate299
TextureCoordinate300 = x3d.TextureCoordinate()

IndexedFaceSet298.texCoord = TextureCoordinate300

Shape294.geometry = IndexedFaceSet298

Transform293.children.append(Shape294)

HAnimSegment292.children.append(Transform293)

HAnimJoint291.children.append(HAnimSegment292)
HAnimJoint301 = x3d.HAnimJoint()
HAnimJoint301.name = "l_carpal_interphalangeal_1"
HAnimJoint301.DEF = "hanim_l_carpal_interphalangeal_1"
HAnimJoint301.center = [7.832,27.85,1.735]
HAnimJoint301.ulimit = [0,0,0]
HAnimJoint301.llimit = [0,0,0]
HAnimSegment302 = x3d.HAnimSegment()
HAnimSegment302.name = "l_carpal_distal_phalanx_1"
HAnimSegment302.DEF = "hanim_l_carpal_distal_phalanx_1"
Transform303 = x3d.Transform()
Transform303.translation = [7.832,27.85,1.735]
Shape304 = x3d.Shape()
Appearance305 = x3d.Appearance()
Material306 = x3d.Material()
Material306.diffuseColor = [0.588,0.588,0.588]

Appearance305.material = Material306
ImageTexture307 = x3d.ImageTexture()
ImageTexture307.USE = "JinLOA2TextureAtlas"

Appearance305.texture = ImageTexture307

Shape304.appearance = Appearance305
IndexedFaceSet308 = x3d.IndexedFaceSet()
IndexedFaceSet308.coordIndex = [0,1,3,-1,3,2,0,-1,0,5,4,-1,0,2,6,-1,6,5,0,-1,2,7,6,-1,2,3,8,-1,8,7,2,-1,3,9,8,-1,3,1,10,-1,10,9,3,-1,1,11,10,-1,1,0,4,-1,4,11,1,-1,4,5,13,-1,13,12,4,-1,5,6,14,-1,14,13,5,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,4,12,-1,12,19,11,-1,12,13,21,-1,21,20,12,-1,13,14,22,-1,22,21,13,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,12,20,-1,20,27,19,-1,28,20,21,-1,28,21,22,-1,28,22,23,-1,28,23,24,-1,28,24,25,-1,28,25,26,-1,28,26,27,-1,28,27,20,-1]
IndexedFaceSet308.creaseAngle = 3.14159
IndexedFaceSet308.texCoordIndex = [0,1,2,-1,2,3,0,-1,0,4,5,-1,0,3,6,-1,6,4,0,-1,3,7,6,-1,3,2,8,-1,8,7,3,-1,2,9,8,-1,2,1,10,-1,10,9,2,-1,1,11,10,-1,1,0,5,-1,5,11,1,-1,5,4,12,-1,12,13,5,-1,4,6,14,-1,14,12,4,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,5,13,-1,13,19,11,-1,13,12,20,-1,20,21,13,-1,12,14,22,-1,22,20,12,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,13,21,-1,21,27,19,-1,28,21,20,-1,28,20,22,-1,28,22,23,-1,28,23,24,-1,28,24,25,-1,28,25,26,-1,28,26,27,-1,28,27,21,-1]
Coordinate309 = x3d.Coordinate()

IndexedFaceSet308.coord = Coordinate309
TextureCoordinate310 = x3d.TextureCoordinate()

IndexedFaceSet308.texCoord = TextureCoordinate310

Shape304.geometry = IndexedFaceSet308

Transform303.children.append(Shape304)

HAnimSegment302.children.append(Transform303)

HAnimJoint301.children.append(HAnimSegment302)

HAnimJoint291.children.append(HAnimJoint301)

HAnimJoint281.children.append(HAnimJoint291)

HAnimJoint271.children.append(HAnimJoint281)
HAnimJoint311 = x3d.HAnimJoint()
HAnimJoint311.name = "l_carpometacarpal_2"
HAnimJoint311.DEF = "hanim_l_carpometacarpal_2"
HAnimJoint311.center = [8.376,28.549999,0.5997]
HAnimJoint311.ulimit = [0,0,0]
HAnimJoint311.llimit = [0,0,0]
HAnimSegment312 = x3d.HAnimSegment()
HAnimSegment312.name = "l_metacarpal_2"
HAnimSegment312.DEF = "hanim_l_metacarpal_2"
Transform313 = x3d.Transform()
Transform313.translation = [8.376,28.549999,0.5997]
Shape314 = x3d.Shape()
Appearance315 = x3d.Appearance()
Material316 = x3d.Material()
Material316.diffuseColor = [0.588,0.588,0.588]

Appearance315.material = Material316
ImageTexture317 = x3d.ImageTexture()
ImageTexture317.USE = "JinLOA2TextureAtlas"

Appearance315.texture = ImageTexture317

Shape314.appearance = Appearance315
IndexedFaceSet318 = x3d.IndexedFaceSet()
IndexedFaceSet318.coordIndex = [0,1,3,-1,3,2,0,-1,0,5,4,-1,0,2,6,-1,6,5,0,-1,2,7,6,-1,2,3,8,-1,8,7,2,-1,3,9,8,-1,3,1,10,-1,10,9,3,-1,1,11,10,-1,1,0,4,-1,4,11,1,-1,4,5,13,-1,13,12,4,-1,5,6,14,-1,14,13,5,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,4,12,-1,12,19,11,-1,12,13,21,-1,21,20,12,-1,13,14,22,-1,22,21,13,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,12,20,-1,20,27,19,-1,20,21,29,-1,29,28,20,-1,21,22,30,-1,30,29,21,-1,22,23,31,-1,31,30,22,-1,23,24,32,-1,32,31,23,-1,24,25,33,-1,33,32,24,-1,25,26,34,-1,34,33,25,-1,26,27,35,-1,35,34,26,-1,27,20,28,-1,28,35,27,-1,36,28,29,-1,36,29,30,-1,36,30,31,-1,36,31,32,-1,36,32,33,-1,36,33,34,-1,36,34,35,-1,36,35,28,-1]
IndexedFaceSet318.creaseAngle = 3.14159
IndexedFaceSet318.texCoordIndex = [0,1,2,-1,2,3,0,-1,0,4,5,-1,0,3,6,-1,6,4,0,-1,3,7,6,-1,3,2,8,-1,8,7,3,-1,2,9,8,-1,2,1,10,-1,10,9,2,-1,1,11,10,-1,1,0,5,-1,5,11,1,-1,5,4,12,-1,12,13,5,-1,4,6,14,-1,14,12,4,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,5,13,-1,13,19,11,-1,13,12,20,-1,20,21,13,-1,12,14,22,-1,22,20,12,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,13,21,-1,21,27,19,-1,21,20,28,-1,28,29,21,-1,20,22,30,-1,30,28,20,-1,22,23,31,-1,31,30,22,-1,23,24,32,-1,32,31,23,-1,24,25,33,-1,33,32,24,-1,25,26,34,-1,34,33,25,-1,26,27,35,-1,35,34,26,-1,27,21,29,-1,29,35,27,-1,36,29,28,-1,36,28,30,-1,36,30,31,-1,36,31,32,-1,36,32,33,-1,36,33,34,-1,36,34,35,-1,36,35,29,-1]
Coordinate319 = x3d.Coordinate()

IndexedFaceSet318.coord = Coordinate319
TextureCoordinate320 = x3d.TextureCoordinate()

IndexedFaceSet318.texCoord = TextureCoordinate320

Shape314.geometry = IndexedFaceSet318

Transform313.children.append(Shape314)

HAnimSegment312.children.append(Transform313)

HAnimJoint311.children.append(HAnimSegment312)
HAnimJoint321 = x3d.HAnimJoint()
HAnimJoint321.name = "l_metacarpophalangeal_2"
HAnimJoint321.DEF = "hanim_l_metacarpophalangeal_2"
HAnimJoint321.center = [8.52,27.24,0.6551]
HAnimJoint321.ulimit = [0,0,0]
HAnimJoint321.llimit = [0,0,0]
HAnimSegment322 = x3d.HAnimSegment()
HAnimSegment322.name = "l_carpal_proximal_phalanx_2"
HAnimSegment322.DEF = "hanim_l_carpal_proximal_phalanx_2"
Transform323 = x3d.Transform()
Transform323.translation = [8.52,27.24,0.6551]
Shape324 = x3d.Shape()
Appearance325 = x3d.Appearance()
Material326 = x3d.Material()
Material326.diffuseColor = [0.588,0.588,0.588]

Appearance325.material = Material326
ImageTexture327 = x3d.ImageTexture()
ImageTexture327.USE = "JinLOA2TextureAtlas"

Appearance325.texture = ImageTexture327

Shape324.appearance = Appearance325
IndexedFaceSet328 = x3d.IndexedFaceSet()
IndexedFaceSet328.coordIndex = [0,1,3,-1,3,2,0,-1,0,5,4,-1,0,2,6,-1,6,5,0,-1,2,7,6,-1,2,3,8,-1,8,7,2,-1,3,9,8,-1,3,1,10,-1,10,9,3,-1,1,11,10,-1,1,0,4,-1,4,11,1,-1,4,5,13,-1,13,12,4,-1,5,6,14,-1,14,13,5,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,4,12,-1,12,19,11,-1,12,13,21,-1,21,20,12,-1,13,14,22,-1,22,21,13,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,12,20,-1,20,27,19,-1,20,21,29,-1,29,28,20,-1,21,22,30,-1,30,29,21,-1,22,23,31,-1,31,30,22,-1,23,24,32,-1,32,31,23,-1,24,25,33,-1,33,32,24,-1,25,26,34,-1,34,33,25,-1,26,27,35,-1,35,34,26,-1,27,20,28,-1,28,35,27,-1,36,28,29,-1,36,29,30,-1,36,30,31,-1,36,31,32,-1,36,32,33,-1,36,33,34,-1,36,34,35,-1,36,35,28,-1]
IndexedFaceSet328.creaseAngle = 3.14159
IndexedFaceSet328.texCoordIndex = [0,1,2,-1,2,3,0,-1,0,4,5,-1,0,3,6,-1,6,4,0,-1,3,7,6,-1,3,2,8,-1,8,7,3,-1,2,9,8,-1,2,1,10,-1,10,9,2,-1,1,11,10,-1,1,0,5,-1,5,11,1,-1,5,4,12,-1,12,13,5,-1,4,6,14,-1,14,12,4,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,5,13,-1,13,19,11,-1,13,12,20,-1,20,21,13,-1,12,14,22,-1,22,20,12,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,13,21,-1,21,27,19,-1,21,20,28,-1,28,29,21,-1,20,22,30,-1,30,28,20,-1,22,23,31,-1,31,30,22,-1,23,24,32,-1,32,31,23,-1,24,25,33,-1,33,32,24,-1,25,26,34,-1,34,33,25,-1,26,27,35,-1,35,34,26,-1,27,21,29,-1,29,35,27,-1,36,29,28,-1,36,28,30,-1,36,30,31,-1,36,31,32,-1,36,32,33,-1,36,33,34,-1,36,34,35,-1,36,35,29,-1]
Coordinate329 = x3d.Coordinate()

IndexedFaceSet328.coord = Coordinate329
TextureCoordinate330 = x3d.TextureCoordinate()

IndexedFaceSet328.texCoord = TextureCoordinate330

Shape324.geometry = IndexedFaceSet328

Transform323.children.append(Shape324)

HAnimSegment322.children.append(Transform323)

HAnimJoint321.children.append(HAnimSegment322)
HAnimJoint331 = x3d.HAnimJoint()
HAnimJoint331.name = "l_carpal_proximal_interphalangeal_2"
HAnimJoint331.DEF = "hanim_l_carpal_proximal_interphalangeal_2"
HAnimJoint331.center = [8.45,26.1,0.6956]
HAnimJoint331.ulimit = [0,0,0]
HAnimJoint331.llimit = [0,0,0]
HAnimSegment332 = x3d.HAnimSegment()
HAnimSegment332.name = "l_carpal_middle_phalanx_2"
HAnimSegment332.DEF = "hanim_l_carpal_middle_phalanx_2"
Transform333 = x3d.Transform()
Transform333.translation = [8.45,26.1,0.6956]
Shape334 = x3d.Shape()
Appearance335 = x3d.Appearance()
Material336 = x3d.Material()
Material336.diffuseColor = [0.588,0.588,0.588]

Appearance335.material = Material336
ImageTexture337 = x3d.ImageTexture()
ImageTexture337.USE = "JinLOA2TextureAtlas"

Appearance335.texture = ImageTexture337

Shape334.appearance = Appearance335
IndexedFaceSet338 = x3d.IndexedFaceSet()
IndexedFaceSet338.coordIndex = [0,1,3,-1,3,2,0,-1,0,5,4,-1,0,2,6,-1,6,5,0,-1,2,7,6,-1,2,3,8,-1,8,7,2,-1,3,9,8,-1,3,1,10,-1,10,9,3,-1,1,11,10,-1,1,0,4,-1,4,11,1,-1,4,5,13,-1,13,12,4,-1,5,6,14,-1,14,13,5,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,4,12,-1,12,19,11,-1,12,13,21,-1,21,20,12,-1,13,14,22,-1,22,21,13,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,12,20,-1,20,27,19,-1,28,20,21,-1,28,21,22,-1,28,22,23,-1,28,23,24,-1,28,24,25,-1,28,25,26,-1,28,26,27,-1,28,27,20,-1]
IndexedFaceSet338.creaseAngle = 3.14159
IndexedFaceSet338.texCoordIndex = [0,1,2,-1,2,3,0,-1,0,4,5,-1,0,3,6,-1,6,4,0,-1,3,7,6,-1,3,2,8,-1,8,7,3,-1,2,9,8,-1,2,1,10,-1,10,9,2,-1,1,11,10,-1,1,0,5,-1,5,11,1,-1,5,4,12,-1,12,13,5,-1,4,6,14,-1,14,12,4,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,5,13,-1,13,19,11,-1,13,12,20,-1,20,21,13,-1,12,14,22,-1,22,20,12,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,13,21,-1,21,27,19,-1,28,21,20,-1,28,20,22,-1,28,22,23,-1,28,23,24,-1,28,24,25,-1,28,25,26,-1,28,26,27,-1,28,27,21,-1]
Coordinate339 = x3d.Coordinate()

IndexedFaceSet338.coord = Coordinate339
TextureCoordinate340 = x3d.TextureCoordinate()

IndexedFaceSet338.texCoord = TextureCoordinate340

Shape334.geometry = IndexedFaceSet338

Transform333.children.append(Shape334)

HAnimSegment332.children.append(Transform333)

HAnimJoint331.children.append(HAnimSegment332)
HAnimJoint341 = x3d.HAnimJoint()
HAnimJoint341.name = "l_carpal_distal_interphalangeal_2"
HAnimJoint341.DEF = "hanim_l_carpal_distal_interphalangeal_2"
HAnimJoint341.center = [8.192,25.17,0.7315]
HAnimJoint341.ulimit = [0,0,0]
HAnimJoint341.llimit = [0,0,0]
HAnimSegment342 = x3d.HAnimSegment()
HAnimSegment342.name = "l_carpal_distal_phalanx_2"
HAnimSegment342.DEF = "hanim_l_carpal_distal_phalanx_2"
Transform343 = x3d.Transform()
Transform343.translation = [8.192,25.17,0.7315]
Shape344 = x3d.Shape()
Appearance345 = x3d.Appearance()
Material346 = x3d.Material()
Material346.diffuseColor = [0.588,0.588,0.588]

Appearance345.material = Material346
ImageTexture347 = x3d.ImageTexture()
ImageTexture347.USE = "JinLOA2TextureAtlas"

Appearance345.texture = ImageTexture347

Shape344.appearance = Appearance345
IndexedFaceSet348 = x3d.IndexedFaceSet()
IndexedFaceSet348.coordIndex = [0,1,3,-1,3,2,0,-1,0,5,4,-1,0,2,6,-1,6,5,0,-1,2,7,6,-1,2,3,8,-1,8,7,2,-1,3,9,8,-1,3,1,10,-1,10,9,3,-1,1,11,10,-1,1,0,4,-1,4,11,1,-1,4,5,13,-1,13,12,4,-1,5,6,14,-1,14,13,5,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,4,12,-1,12,19,11,-1,12,13,21,-1,21,20,12,-1,13,14,22,-1,22,21,13,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,12,20,-1,20,27,19,-1,28,20,21,-1,28,21,22,-1,28,22,23,-1,28,23,24,-1,28,24,25,-1,28,25,26,-1,28,26,27,-1,28,27,20,-1]
IndexedFaceSet348.creaseAngle = 3.14159
IndexedFaceSet348.texCoordIndex = [0,1,2,-1,2,3,0,-1,0,4,5,-1,0,3,6,-1,6,4,0,-1,3,7,6,-1,3,2,8,-1,8,7,3,-1,2,9,8,-1,2,1,10,-1,10,9,2,-1,1,11,10,-1,1,0,5,-1,5,11,1,-1,5,4,12,-1,12,13,5,-1,4,6,14,-1,14,12,4,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,5,13,-1,13,19,11,-1,13,12,20,-1,20,21,13,-1,12,14,22,-1,22,20,12,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,13,21,-1,21,27,19,-1,28,21,20,-1,28,20,22,-1,28,22,23,-1,28,23,24,-1,28,24,25,-1,28,25,26,-1,28,26,27,-1,28,27,21,-1]
Coordinate349 = x3d.Coordinate()

IndexedFaceSet348.coord = Coordinate349
TextureCoordinate350 = x3d.TextureCoordinate()

IndexedFaceSet348.texCoord = TextureCoordinate350

Shape344.geometry = IndexedFaceSet348

Transform343.children.append(Shape344)

HAnimSegment342.children.append(Transform343)

HAnimJoint341.children.append(HAnimSegment342)

HAnimJoint331.children.append(HAnimJoint341)

HAnimJoint321.children.append(HAnimJoint331)

HAnimJoint311.children.append(HAnimJoint321)

HAnimJoint271.children.append(HAnimJoint311)
HAnimJoint351 = x3d.HAnimJoint()
HAnimJoint351.name = "l_carpometacarpal_3"
HAnimJoint351.DEF = "hanim_l_carpometacarpal_3"
HAnimJoint351.center = [8.344,28.65,-0.194]
HAnimJoint351.ulimit = [0,0,0]
HAnimJoint351.llimit = [0,0,0]
HAnimSegment352 = x3d.HAnimSegment()
HAnimSegment352.name = "l_metacarpal_3"
HAnimSegment352.DEF = "hanim_l_metacarpal_3"
Transform353 = x3d.Transform()
Transform353.translation = [8.344,28.65,-0.194]
Shape354 = x3d.Shape()
Appearance355 = x3d.Appearance()
Material356 = x3d.Material()
Material356.diffuseColor = [0.588,0.588,0.588]

Appearance355.material = Material356
ImageTexture357 = x3d.ImageTexture()
ImageTexture357.USE = "JinLOA2TextureAtlas"

Appearance355.texture = ImageTexture357

Shape354.appearance = Appearance355
IndexedFaceSet358 = x3d.IndexedFaceSet()
IndexedFaceSet358.coordIndex = [0,1,3,-1,3,2,0,-1,0,5,4,-1,0,2,6,-1,6,5,0,-1,2,7,6,-1,2,3,8,-1,8,7,2,-1,3,9,8,-1,3,1,10,-1,10,9,3,-1,1,11,10,-1,1,0,4,-1,4,11,1,-1,4,5,13,-1,13,12,4,-1,5,6,14,-1,14,13,5,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,4,12,-1,12,19,11,-1,12,13,21,-1,21,20,12,-1,13,14,22,-1,22,21,13,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,12,20,-1,20,27,19,-1,20,21,29,-1,29,28,20,-1,21,22,30,-1,30,29,21,-1,22,23,31,-1,31,30,22,-1,23,24,32,-1,32,31,23,-1,24,25,33,-1,33,32,24,-1,25,26,34,-1,34,33,25,-1,26,27,35,-1,35,34,26,-1,27,20,28,-1,28,35,27,-1,36,28,29,-1,36,29,30,-1,36,30,31,-1,36,31,32,-1,36,32,33,-1,36,33,34,-1,36,34,35,-1,36,35,28,-1]
IndexedFaceSet358.creaseAngle = 3.14159
IndexedFaceSet358.texCoordIndex = [0,1,2,-1,2,3,0,-1,0,4,5,-1,0,3,6,-1,6,4,0,-1,3,7,6,-1,3,2,8,-1,8,7,3,-1,2,9,8,-1,2,1,10,-1,10,9,2,-1,1,11,10,-1,1,0,5,-1,5,11,1,-1,5,4,12,-1,12,13,5,-1,4,6,14,-1,14,12,4,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,5,13,-1,13,19,11,-1,13,12,20,-1,20,21,13,-1,12,14,22,-1,22,20,12,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,13,21,-1,21,27,19,-1,21,20,28,-1,28,29,21,-1,20,22,30,-1,30,28,20,-1,22,23,31,-1,31,30,22,-1,23,24,32,-1,32,31,23,-1,24,25,33,-1,33,32,24,-1,25,26,34,-1,34,33,25,-1,26,27,35,-1,35,34,26,-1,27,21,29,-1,29,35,27,-1,36,29,28,-1,36,28,30,-1,36,30,31,-1,36,31,32,-1,36,32,33,-1,36,33,34,-1,36,34,35,-1,36,35,29,-1]
Coordinate359 = x3d.Coordinate()

IndexedFaceSet358.coord = Coordinate359
TextureCoordinate360 = x3d.TextureCoordinate()

IndexedFaceSet358.texCoord = TextureCoordinate360

Shape354.geometry = IndexedFaceSet358

Transform353.children.append(Shape354)

HAnimSegment352.children.append(Transform353)

HAnimJoint351.children.append(HAnimSegment352)
HAnimJoint361 = x3d.HAnimJoint()
HAnimJoint361.name = "l_metacarpophalangeal_3"
HAnimJoint361.DEF = "hanim_l_metacarpophalangeal_3"
HAnimJoint361.center = [8.52,27.26,-0.1959]
HAnimJoint361.ulimit = [0,0,0]
HAnimJoint361.llimit = [0,0,0]
HAnimSegment362 = x3d.HAnimSegment()
HAnimSegment362.name = "l_carpal_proximal_phalanx_3"
HAnimSegment362.DEF = "hanim_l_carpal_proximal_phalanx_3"
Transform363 = x3d.Transform()
Transform363.translation = [8.52,27.26,-0.1959]
Shape364 = x3d.Shape()
Appearance365 = x3d.Appearance()
Material366 = x3d.Material()
Material366.diffuseColor = [0.588,0.588,0.588]

Appearance365.material = Material366
ImageTexture367 = x3d.ImageTexture()
ImageTexture367.USE = "JinLOA2TextureAtlas"

Appearance365.texture = ImageTexture367

Shape364.appearance = Appearance365
IndexedFaceSet368 = x3d.IndexedFaceSet()
IndexedFaceSet368.coordIndex = [0,1,3,-1,3,2,0,-1,0,5,4,-1,0,2,6,-1,6,5,0,-1,2,7,6,-1,2,3,8,-1,8,7,2,-1,3,9,8,-1,3,1,10,-1,10,9,3,-1,1,11,10,-1,1,0,4,-1,4,11,1,-1,4,5,13,-1,13,12,4,-1,5,6,14,-1,14,13,5,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,4,12,-1,12,19,11,-1,12,13,21,-1,21,20,12,-1,13,14,22,-1,22,21,13,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,12,20,-1,20,27,19,-1,20,21,29,-1,29,28,20,-1,21,22,30,-1,30,29,21,-1,22,23,31,-1,31,30,22,-1,23,24,32,-1,32,31,23,-1,24,25,33,-1,33,32,24,-1,25,26,34,-1,34,33,25,-1,26,27,35,-1,35,34,26,-1,27,20,28,-1,28,35,27,-1,36,28,29,-1,36,29,30,-1,36,30,31,-1,36,31,32,-1,36,32,33,-1,36,33,34,-1,36,34,35,-1,36,35,28,-1]
IndexedFaceSet368.creaseAngle = 3.14159
IndexedFaceSet368.texCoordIndex = [0,1,2,-1,2,3,0,-1,0,4,5,-1,0,3,6,-1,6,4,0,-1,3,7,6,-1,3,2,8,-1,8,7,3,-1,2,9,8,-1,2,1,10,-1,10,9,2,-1,1,11,10,-1,1,0,5,-1,5,11,1,-1,5,4,12,-1,12,13,5,-1,4,6,14,-1,14,12,4,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,5,13,-1,13,19,11,-1,13,12,20,-1,20,21,13,-1,12,14,22,-1,22,20,12,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,13,21,-1,21,27,19,-1,21,20,28,-1,28,29,21,-1,20,22,30,-1,30,28,20,-1,22,23,31,-1,31,30,22,-1,23,24,32,-1,32,31,23,-1,24,25,33,-1,33,32,24,-1,25,26,34,-1,34,33,25,-1,26,27,35,-1,35,34,26,-1,27,21,29,-1,29,35,27,-1,36,29,28,-1,36,28,30,-1,36,30,31,-1,36,31,32,-1,36,32,33,-1,36,33,34,-1,36,34,35,-1,36,35,29,-1]
Coordinate369 = x3d.Coordinate()

IndexedFaceSet368.coord = Coordinate369
TextureCoordinate370 = x3d.TextureCoordinate()

IndexedFaceSet368.texCoord = TextureCoordinate370

Shape364.geometry = IndexedFaceSet368

Transform363.children.append(Shape364)

HAnimSegment362.children.append(Transform363)

HAnimJoint361.children.append(HAnimSegment362)
HAnimJoint371 = x3d.HAnimJoint()
HAnimJoint371.name = "l_carpal_proximal_interphalangeal_3"
HAnimJoint371.DEF = "hanim_l_carpal_proximal_interphalangeal_3"
HAnimJoint371.center = [8.477,26.07,-0.2214]
HAnimJoint371.ulimit = [0,0,0]
HAnimJoint371.llimit = [0,0,0]
HAnimSegment372 = x3d.HAnimSegment()
HAnimSegment372.name = "l_carpal_middle_phalanx_3"
HAnimSegment372.DEF = "hanim_l_carpal_middle_phalanx_3"
Transform373 = x3d.Transform()
Transform373.translation = [8.477,26.07,-0.2214]
Shape374 = x3d.Shape()
Appearance375 = x3d.Appearance()
Material376 = x3d.Material()
Material376.diffuseColor = [0.588,0.588,0.588]

Appearance375.material = Material376
ImageTexture377 = x3d.ImageTexture()
ImageTexture377.USE = "JinLOA2TextureAtlas"

Appearance375.texture = ImageTexture377

Shape374.appearance = Appearance375
IndexedFaceSet378 = x3d.IndexedFaceSet()
IndexedFaceSet378.coordIndex = [0,1,3,-1,3,2,0,-1,0,5,4,-1,0,2,6,-1,6,5,0,-1,2,7,6,-1,2,3,8,-1,8,7,2,-1,3,9,8,-1,3,1,10,-1,10,9,3,-1,1,11,10,-1,1,0,4,-1,4,11,1,-1,4,5,13,-1,13,12,4,-1,5,6,14,-1,14,13,5,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,4,12,-1,12,19,11,-1,12,13,21,-1,21,20,12,-1,13,14,22,-1,22,21,13,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,12,20,-1,20,27,19,-1,28,20,21,-1,28,21,22,-1,28,22,23,-1,28,23,24,-1,28,24,25,-1,28,25,26,-1,28,26,27,-1,28,27,20,-1]
IndexedFaceSet378.creaseAngle = 3.14159
IndexedFaceSet378.texCoordIndex = [0,1,2,-1,2,3,0,-1,0,4,5,-1,0,3,6,-1,6,4,0,-1,3,7,6,-1,3,2,8,-1,8,7,3,-1,2,9,8,-1,2,1,10,-1,10,9,2,-1,1,11,10,-1,1,0,5,-1,5,11,1,-1,5,4,12,-1,12,13,5,-1,4,6,14,-1,14,12,4,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,5,13,-1,13,19,11,-1,13,12,20,-1,20,21,13,-1,12,14,22,-1,22,20,12,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,13,21,-1,21,27,19,-1,28,21,20,-1,28,20,22,-1,28,22,23,-1,28,23,24,-1,28,24,25,-1,28,25,26,-1,28,26,27,-1,28,27,21,-1]
Coordinate379 = x3d.Coordinate()

IndexedFaceSet378.coord = Coordinate379
TextureCoordinate380 = x3d.TextureCoordinate()

IndexedFaceSet378.texCoord = TextureCoordinate380

Shape374.geometry = IndexedFaceSet378

Transform373.children.append(Shape374)

HAnimSegment372.children.append(Transform373)

HAnimJoint371.children.append(HAnimSegment372)
HAnimJoint381 = x3d.HAnimJoint()
HAnimJoint381.name = "l_carpal_distal_interphalangeal_3"
HAnimJoint381.DEF = "hanim_l_carpal_distal_interphalangeal_3"
HAnimJoint381.center = [8.25,25.030001,-0.2187]
HAnimJoint381.ulimit = [0,0,0]
HAnimJoint381.llimit = [0,0,0]
HAnimSegment382 = x3d.HAnimSegment()
HAnimSegment382.name = "l_carpal_distal_phalanx_3"
HAnimSegment382.DEF = "hanim_l_carpal_distal_phalanx_3"
Transform383 = x3d.Transform()
Transform383.translation = [8.25,25.030001,-0.2187]
Shape384 = x3d.Shape()
Appearance385 = x3d.Appearance()
Material386 = x3d.Material()
Material386.diffuseColor = [0.588,0.588,0.588]

Appearance385.material = Material386
ImageTexture387 = x3d.ImageTexture()
ImageTexture387.USE = "JinLOA2TextureAtlas"

Appearance385.texture = ImageTexture387

Shape384.appearance = Appearance385
IndexedFaceSet388 = x3d.IndexedFaceSet()
IndexedFaceSet388.coordIndex = [0,1,3,-1,3,2,0,-1,0,5,4,-1,0,2,6,-1,6,5,0,-1,2,7,6,-1,2,3,8,-1,8,7,2,-1,3,9,8,-1,3,1,10,-1,10,9,3,-1,1,11,10,-1,1,0,4,-1,4,11,1,-1,4,5,13,-1,13,12,4,-1,5,6,14,-1,14,13,5,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,4,12,-1,12,19,11,-1,12,13,21,-1,21,20,12,-1,13,14,22,-1,22,21,13,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,12,20,-1,20,27,19,-1,28,20,21,-1,28,21,22,-1,28,22,23,-1,28,23,24,-1,28,24,25,-1,28,25,26,-1,28,26,27,-1,28,27,20,-1]
IndexedFaceSet388.creaseAngle = 3.14159
IndexedFaceSet388.texCoordIndex = [0,1,2,-1,2,3,0,-1,0,4,5,-1,0,3,6,-1,6,4,0,-1,3,7,6,-1,3,2,8,-1,8,7,3,-1,2,9,8,-1,2,1,10,-1,10,9,2,-1,1,11,10,-1,1,0,5,-1,5,11,1,-1,5,4,12,-1,12,13,5,-1,4,6,14,-1,14,12,4,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,5,13,-1,13,19,11,-1,13,12,20,-1,20,21,13,-1,12,14,22,-1,22,20,12,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,13,21,-1,21,27,19,-1,28,21,20,-1,28,20,22,-1,28,22,23,-1,28,23,24,-1,28,24,25,-1,28,25,26,-1,28,26,27,-1,28,27,21,-1]
Coordinate389 = x3d.Coordinate()

IndexedFaceSet388.coord = Coordinate389
TextureCoordinate390 = x3d.TextureCoordinate()

IndexedFaceSet388.texCoord = TextureCoordinate390

Shape384.geometry = IndexedFaceSet388

Transform383.children.append(Shape384)

HAnimSegment382.children.append(Transform383)

HAnimJoint381.children.append(HAnimSegment382)

HAnimJoint371.children.append(HAnimJoint381)

HAnimJoint361.children.append(HAnimJoint371)

HAnimJoint351.children.append(HAnimJoint361)

HAnimJoint271.children.append(HAnimJoint351)
HAnimJoint391 = x3d.HAnimJoint()
HAnimJoint391.name = "l_carpometacarpal_4"
HAnimJoint391.DEF = "hanim_l_carpometacarpal_4"
HAnimJoint391.center = [8.339,28.57,-0.9243]
HAnimJoint391.ulimit = [0,0,0]
HAnimJoint391.llimit = [0,0,0]
HAnimSegment392 = x3d.HAnimSegment()
HAnimSegment392.name = "l_metacarpal_4"
HAnimSegment392.DEF = "hanim_l_metacarpal_4"
Transform393 = x3d.Transform()
Transform393.translation = [8.339,28.57,-0.9243]
Shape394 = x3d.Shape()
Appearance395 = x3d.Appearance()
Material396 = x3d.Material()
Material396.diffuseColor = [0.588,0.588,0.588]

Appearance395.material = Material396
ImageTexture397 = x3d.ImageTexture()
ImageTexture397.USE = "JinLOA2TextureAtlas"

Appearance395.texture = ImageTexture397

Shape394.appearance = Appearance395
IndexedFaceSet398 = x3d.IndexedFaceSet()
IndexedFaceSet398.coordIndex = [0,1,3,-1,3,2,0,-1,0,5,4,-1,0,2,6,-1,6,5,0,-1,2,7,6,-1,2,3,8,-1,8,7,2,-1,3,9,8,-1,3,1,10,-1,10,9,3,-1,1,11,10,-1,1,0,4,-1,4,11,1,-1,4,5,13,-1,13,12,4,-1,5,6,14,-1,14,13,5,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,4,12,-1,12,19,11,-1,12,13,21,-1,21,20,12,-1,13,14,22,-1,22,21,13,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,12,20,-1,20,27,19,-1,20,21,29,-1,29,28,20,-1,21,22,30,-1,30,29,21,-1,22,23,31,-1,31,30,22,-1,23,24,32,-1,32,31,23,-1,24,25,33,-1,33,32,24,-1,25,26,34,-1,34,33,25,-1,26,27,35,-1,35,34,26,-1,27,20,28,-1,28,35,27,-1,36,28,29,-1,36,29,30,-1,36,30,31,-1,36,31,32,-1,36,32,33,-1,36,33,34,-1,36,34,35,-1,36,35,28,-1]
IndexedFaceSet398.creaseAngle = 3.14159
IndexedFaceSet398.texCoordIndex = [0,1,2,-1,2,3,0,-1,0,4,5,-1,0,3,6,-1,6,4,0,-1,3,7,6,-1,3,2,8,-1,8,7,3,-1,2,9,8,-1,2,1,10,-1,10,9,2,-1,1,11,10,-1,1,0,5,-1,5,11,1,-1,5,4,12,-1,12,13,5,-1,4,6,14,-1,14,12,4,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,5,13,-1,13,19,11,-1,13,12,20,-1,20,21,13,-1,12,14,22,-1,22,20,12,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,13,21,-1,21,27,19,-1,21,20,28,-1,28,29,21,-1,20,22,30,-1,30,28,20,-1,22,23,31,-1,31,30,22,-1,23,24,32,-1,32,31,23,-1,24,25,33,-1,33,32,24,-1,25,26,34,-1,34,33,25,-1,26,27,35,-1,35,34,26,-1,27,21,29,-1,29,35,27,-1,36,29,28,-1,36,28,30,-1,36,30,31,-1,36,31,32,-1,36,32,33,-1,36,33,34,-1,36,34,35,-1,36,35,29,-1]
Coordinate399 = x3d.Coordinate()

IndexedFaceSet398.coord = Coordinate399
TextureCoordinate400 = x3d.TextureCoordinate()

IndexedFaceSet398.texCoord = TextureCoordinate400

Shape394.geometry = IndexedFaceSet398

Transform393.children.append(Shape394)

HAnimSegment392.children.append(Transform393)

HAnimJoint391.children.append(HAnimSegment392)
HAnimJoint401 = x3d.HAnimJoint()
HAnimJoint401.name = "l_metacarpophalangeal_4"
HAnimJoint401.DEF = "hanim_l_metacarpophalangeal_4"
HAnimJoint401.center = [8.428,27.299999,-0.9985]
HAnimJoint401.ulimit = [0,0,0]
HAnimJoint401.llimit = [0,0,0]
HAnimSegment402 = x3d.HAnimSegment()
HAnimSegment402.name = "l_carpal_proximal_phalanx_4"
HAnimSegment402.DEF = "hanim_l_carpal_proximal_phalanx_4"
Transform403 = x3d.Transform()
Transform403.translation = [8.428,27.299999,-0.9985]
Shape404 = x3d.Shape()
Appearance405 = x3d.Appearance()
Material406 = x3d.Material()
Material406.diffuseColor = [0.588,0.588,0.588]

Appearance405.material = Material406
ImageTexture407 = x3d.ImageTexture()
ImageTexture407.USE = "JinLOA2TextureAtlas"

Appearance405.texture = ImageTexture407

Shape404.appearance = Appearance405
IndexedFaceSet408 = x3d.IndexedFaceSet()
IndexedFaceSet408.coordIndex = [0,1,3,-1,3,2,0,-1,0,5,4,-1,0,2,6,-1,6,5,0,-1,2,7,6,-1,2,3,8,-1,8,7,2,-1,3,9,8,-1,3,1,10,-1,10,9,3,-1,1,11,10,-1,1,0,4,-1,4,11,1,-1,4,5,13,-1,13,12,4,-1,5,6,14,-1,14,13,5,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,4,12,-1,12,19,11,-1,12,13,21,-1,21,20,12,-1,13,14,22,-1,22,21,13,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,12,20,-1,20,27,19,-1,20,21,29,-1,29,28,20,-1,21,22,30,-1,30,29,21,-1,22,23,31,-1,31,30,22,-1,23,24,32,-1,32,31,23,-1,24,25,33,-1,33,32,24,-1,25,26,34,-1,34,33,25,-1,26,27,35,-1,35,34,26,-1,27,20,28,-1,28,35,27,-1,36,28,29,-1,36,29,30,-1,36,30,31,-1,36,31,32,-1,36,32,33,-1,36,33,34,-1,36,34,35,-1,36,35,28,-1]
IndexedFaceSet408.creaseAngle = 3.14159
IndexedFaceSet408.texCoordIndex = [0,1,2,-1,2,3,0,-1,0,4,5,-1,0,3,6,-1,6,4,0,-1,3,7,6,-1,3,2,8,-1,8,7,3,-1,2,9,8,-1,2,1,10,-1,10,9,2,-1,1,11,10,-1,1,0,5,-1,5,11,1,-1,5,4,12,-1,12,13,5,-1,4,6,14,-1,14,12,4,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,5,13,-1,13,19,11,-1,13,12,20,-1,20,21,13,-1,12,14,22,-1,22,20,12,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,13,21,-1,21,27,19,-1,21,20,28,-1,28,29,21,-1,20,22,30,-1,30,28,20,-1,22,23,31,-1,31,30,22,-1,23,24,32,-1,32,31,23,-1,24,25,33,-1,33,32,24,-1,25,26,34,-1,34,33,25,-1,26,27,35,-1,35,34,26,-1,27,21,29,-1,29,35,27,-1,36,29,28,-1,36,28,30,-1,36,30,31,-1,36,31,32,-1,36,32,33,-1,36,33,34,-1,36,34,35,-1,36,35,29,-1]
Coordinate409 = x3d.Coordinate()

IndexedFaceSet408.coord = Coordinate409
TextureCoordinate410 = x3d.TextureCoordinate()

IndexedFaceSet408.texCoord = TextureCoordinate410

Shape404.geometry = IndexedFaceSet408

Transform403.children.append(Shape404)

HAnimSegment402.children.append(Transform403)

HAnimJoint401.children.append(HAnimSegment402)
HAnimJoint411 = x3d.HAnimJoint()
HAnimJoint411.name = "l_carpal_proximal_interphalangeal_4"
HAnimJoint411.DEF = "hanim_l_carpal_proximal_interphalangeal_4"
HAnimJoint411.center = [8.428,26.290001,-1.034]
HAnimJoint411.ulimit = [0,0,0]
HAnimJoint411.llimit = [0,0,0]
HAnimSegment412 = x3d.HAnimSegment()
HAnimSegment412.name = "l_carpal_middle_phalanx_4"
HAnimSegment412.DEF = "hanim_l_carpal_middle_phalanx_4"
Transform413 = x3d.Transform()
Transform413.translation = [8.428,26.290001,-1.034]
Shape414 = x3d.Shape()
Appearance415 = x3d.Appearance()
Material416 = x3d.Material()
Material416.diffuseColor = [0.588,0.588,0.588]

Appearance415.material = Material416
ImageTexture417 = x3d.ImageTexture()
ImageTexture417.USE = "JinLOA2TextureAtlas"

Appearance415.texture = ImageTexture417

Shape414.appearance = Appearance415
IndexedFaceSet418 = x3d.IndexedFaceSet()
IndexedFaceSet418.coordIndex = [0,1,3,-1,3,2,0,-1,0,5,4,-1,0,2,6,-1,6,5,0,-1,2,7,6,-1,2,3,8,-1,8,7,2,-1,3,9,8,-1,3,1,10,-1,10,9,3,-1,1,11,10,-1,1,0,4,-1,4,11,1,-1,4,5,13,-1,13,12,4,-1,5,6,14,-1,14,13,5,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,4,12,-1,12,19,11,-1,12,13,21,-1,21,20,12,-1,13,14,22,-1,22,21,13,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,12,20,-1,20,27,19,-1,28,20,21,-1,28,21,22,-1,28,22,23,-1,28,23,24,-1,28,24,25,-1,28,25,26,-1,28,26,27,-1,28,27,20,-1]
IndexedFaceSet418.creaseAngle = 3.14159
IndexedFaceSet418.texCoordIndex = [0,1,2,-1,2,3,0,-1,0,4,5,-1,0,3,6,-1,6,4,0,-1,3,7,6,-1,3,2,8,-1,8,7,3,-1,2,9,8,-1,2,1,10,-1,10,9,2,-1,1,11,10,-1,1,0,5,-1,5,11,1,-1,5,4,12,-1,12,13,5,-1,4,6,14,-1,14,12,4,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,5,13,-1,13,19,11,-1,13,12,20,-1,20,21,13,-1,12,14,22,-1,22,20,12,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,13,21,-1,21,27,19,-1,28,21,20,-1,28,20,22,-1,28,22,23,-1,28,23,24,-1,28,24,25,-1,28,25,26,-1,28,26,27,-1,28,27,21,-1]
Coordinate419 = x3d.Coordinate()

IndexedFaceSet418.coord = Coordinate419
TextureCoordinate420 = x3d.TextureCoordinate()

IndexedFaceSet418.texCoord = TextureCoordinate420

Shape414.geometry = IndexedFaceSet418

Transform413.children.append(Shape414)

HAnimSegment412.children.append(Transform413)

HAnimJoint411.children.append(HAnimSegment412)
HAnimJoint421 = x3d.HAnimJoint()
HAnimJoint421.name = "l_carpal_distal_interphalangeal_4"
HAnimJoint421.DEF = "hanim_l_carpal_distal_interphalangeal_4"
HAnimJoint421.center = [8.192,25.309999,-1.124]
HAnimJoint421.ulimit = [0,0,0]
HAnimJoint421.llimit = [0,0,0]
HAnimSegment422 = x3d.HAnimSegment()
HAnimSegment422.name = "l_carpal_distal_phalanx_4"
HAnimSegment422.DEF = "hanim_l_carpal_distal_phalanx_4"
Transform423 = x3d.Transform()
Transform423.translation = [8.192,25.309999,-1.124]
Shape424 = x3d.Shape()
Appearance425 = x3d.Appearance()
Material426 = x3d.Material()
Material426.diffuseColor = [0.588,0.588,0.588]

Appearance425.material = Material426
ImageTexture427 = x3d.ImageTexture()
ImageTexture427.USE = "JinLOA2TextureAtlas"

Appearance425.texture = ImageTexture427

Shape424.appearance = Appearance425
IndexedFaceSet428 = x3d.IndexedFaceSet()
IndexedFaceSet428.coordIndex = [0,1,3,-1,3,2,0,-1,0,5,4,-1,0,2,6,-1,6,5,0,-1,2,7,6,-1,2,3,8,-1,8,7,2,-1,3,9,8,-1,3,1,10,-1,10,9,3,-1,1,11,10,-1,1,0,4,-1,4,11,1,-1,4,5,13,-1,13,12,4,-1,5,6,14,-1,14,13,5,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,4,12,-1,12,19,11,-1,12,13,21,-1,21,20,12,-1,13,14,22,-1,22,21,13,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,12,20,-1,20,27,19,-1,28,20,21,-1,28,21,22,-1,28,22,23,-1,28,23,24,-1,28,24,25,-1,28,25,26,-1,28,26,27,-1,28,27,20,-1]
IndexedFaceSet428.creaseAngle = 3.14159
IndexedFaceSet428.texCoordIndex = [0,1,2,-1,2,3,0,-1,0,4,5,-1,0,3,6,-1,6,4,0,-1,3,7,6,-1,3,2,8,-1,8,7,3,-1,2,9,8,-1,2,1,10,-1,10,9,2,-1,1,11,10,-1,1,0,5,-1,5,11,1,-1,5,4,12,-1,12,13,5,-1,4,6,14,-1,14,12,4,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,5,13,-1,13,19,11,-1,13,12,20,-1,20,21,13,-1,12,14,22,-1,22,20,12,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,13,21,-1,21,27,19,-1,28,21,20,-1,28,20,22,-1,28,22,23,-1,28,23,24,-1,28,24,25,-1,28,25,26,-1,28,26,27,-1,28,27,21,-1]
Coordinate429 = x3d.Coordinate()

IndexedFaceSet428.coord = Coordinate429
TextureCoordinate430 = x3d.TextureCoordinate()

IndexedFaceSet428.texCoord = TextureCoordinate430

Shape424.geometry = IndexedFaceSet428

Transform423.children.append(Shape424)

HAnimSegment422.children.append(Transform423)

HAnimJoint421.children.append(HAnimSegment422)

HAnimJoint411.children.append(HAnimJoint421)

HAnimJoint401.children.append(HAnimJoint411)

HAnimJoint391.children.append(HAnimJoint401)

HAnimJoint271.children.append(HAnimJoint391)
HAnimJoint431 = x3d.HAnimJoint()
HAnimJoint431.name = "l_carpometacarpal_5"
HAnimJoint431.DEF = "hanim_l_carpometacarpal_5"
HAnimJoint431.center = [8.197,28.370001,-1.528]
HAnimJoint431.ulimit = [0,0,0]
HAnimJoint431.llimit = [0,0,0]
HAnimSegment432 = x3d.HAnimSegment()
HAnimSegment432.name = "l_metacarpal_5"
HAnimSegment432.DEF = "hanim_l_metacarpal_5"
Transform433 = x3d.Transform()
Transform433.translation = [8.197,28.370001,-1.528]
Shape434 = x3d.Shape()
Appearance435 = x3d.Appearance()
Material436 = x3d.Material()
Material436.diffuseColor = [0.588,0.588,0.588]

Appearance435.material = Material436
ImageTexture437 = x3d.ImageTexture()
ImageTexture437.USE = "JinLOA2TextureAtlas"

Appearance435.texture = ImageTexture437

Shape434.appearance = Appearance435
IndexedFaceSet438 = x3d.IndexedFaceSet()
IndexedFaceSet438.coordIndex = [0,1,3,-1,3,2,0,-1,0,5,4,-1,0,2,6,-1,6,5,0,-1,2,7,6,-1,2,3,8,-1,8,7,2,-1,3,9,8,-1,3,1,10,-1,10,9,3,-1,1,11,10,-1,1,0,4,-1,4,11,1,-1,4,5,13,-1,13,12,4,-1,5,6,14,-1,14,13,5,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,4,12,-1,12,19,11,-1,12,13,21,-1,21,20,12,-1,13,14,22,-1,22,21,13,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,12,20,-1,20,27,19,-1,20,21,29,-1,29,28,20,-1,21,22,30,-1,30,29,21,-1,22,23,31,-1,31,30,22,-1,23,24,32,-1,32,31,23,-1,24,25,33,-1,33,32,24,-1,25,26,34,-1,34,33,25,-1,26,27,35,-1,35,34,26,-1,27,20,28,-1,28,35,27,-1,36,28,29,-1,36,29,30,-1,36,30,31,-1,36,31,32,-1,36,32,33,-1,36,33,34,-1,36,34,35,-1,36,35,28,-1]
IndexedFaceSet438.creaseAngle = 3.14159
IndexedFaceSet438.texCoordIndex = [0,1,2,-1,2,3,0,-1,0,4,5,-1,0,3,6,-1,6,4,0,-1,3,7,6,-1,3,2,8,-1,8,7,3,-1,2,9,8,-1,2,1,10,-1,10,9,2,-1,1,11,10,-1,1,0,5,-1,5,11,1,-1,5,4,12,-1,12,13,5,-1,4,6,14,-1,14,12,4,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,5,13,-1,13,19,11,-1,13,12,20,-1,20,21,13,-1,12,14,22,-1,22,20,12,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,13,21,-1,21,27,19,-1,21,20,28,-1,28,29,21,-1,20,22,30,-1,30,28,20,-1,22,23,31,-1,31,30,22,-1,23,24,32,-1,32,31,23,-1,24,25,33,-1,33,32,24,-1,25,26,34,-1,34,33,25,-1,26,27,35,-1,35,34,26,-1,27,21,29,-1,29,35,27,-1,36,29,28,-1,36,28,30,-1,36,30,31,-1,36,31,32,-1,36,32,33,-1,36,33,34,-1,36,34,35,-1,36,35,29,-1]
Coordinate439 = x3d.Coordinate()

IndexedFaceSet438.coord = Coordinate439
TextureCoordinate440 = x3d.TextureCoordinate()

IndexedFaceSet438.texCoord = TextureCoordinate440

Shape434.geometry = IndexedFaceSet438

Transform433.children.append(Shape434)

HAnimSegment432.children.append(Transform433)

HAnimJoint431.children.append(HAnimSegment432)
HAnimJoint441 = x3d.HAnimJoint()
HAnimJoint441.name = "l_metacarpophalangeal_5"
HAnimJoint441.DEF = "hanim_l_metacarpophalangeal_5"
HAnimJoint441.center = [8.334,27.5,-1.701]
HAnimJoint441.ulimit = [0,0,0]
HAnimJoint441.llimit = [0,0,0]
HAnimSegment442 = x3d.HAnimSegment()
HAnimSegment442.name = "l_carpal_proximal_phalanx_5"
HAnimSegment442.DEF = "hanim_l_carpal_proximal_phalanx_5"
Transform443 = x3d.Transform()
Transform443.translation = [8.334,27.5,-1.701]
Shape444 = x3d.Shape()
Appearance445 = x3d.Appearance()
Material446 = x3d.Material()
Material446.diffuseColor = [0.588,0.588,0.588]

Appearance445.material = Material446
ImageTexture447 = x3d.ImageTexture()
ImageTexture447.USE = "JinLOA2TextureAtlas"

Appearance445.texture = ImageTexture447

Shape444.appearance = Appearance445
IndexedFaceSet448 = x3d.IndexedFaceSet()
IndexedFaceSet448.coordIndex = [0,1,3,-1,3,2,0,-1,0,5,4,-1,0,2,6,-1,6,5,0,-1,2,7,6,-1,2,3,8,-1,8,7,2,-1,3,9,8,-1,3,1,10,-1,10,9,3,-1,1,11,10,-1,1,0,4,-1,4,11,1,-1,4,5,13,-1,13,12,4,-1,5,6,14,-1,14,13,5,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,4,12,-1,12,19,11,-1,12,13,21,-1,21,20,12,-1,13,14,22,-1,22,21,13,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,12,20,-1,20,27,19,-1,20,21,29,-1,29,28,20,-1,21,22,30,-1,30,29,21,-1,22,23,31,-1,31,30,22,-1,23,24,32,-1,32,31,23,-1,24,25,33,-1,33,32,24,-1,25,26,34,-1,34,33,25,-1,26,27,35,-1,35,34,26,-1,27,20,28,-1,28,35,27,-1,36,28,29,-1,36,29,30,-1,36,30,31,-1,36,31,32,-1,36,32,33,-1,36,33,34,-1,36,34,35,-1,36,35,28,-1]
IndexedFaceSet448.creaseAngle = 3.14159
IndexedFaceSet448.texCoordIndex = [0,1,2,-1,2,3,0,-1,0,4,5,-1,0,3,6,-1,6,4,0,-1,3,7,6,-1,3,2,8,-1,8,7,3,-1,2,9,8,-1,2,1,10,-1,10,9,2,-1,1,11,10,-1,1,0,5,-1,5,11,1,-1,5,4,12,-1,12,13,5,-1,4,6,14,-1,14,12,4,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,5,13,-1,13,19,11,-1,13,12,20,-1,20,21,13,-1,12,14,22,-1,22,20,12,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,13,21,-1,21,27,19,-1,21,20,28,-1,28,29,21,-1,20,22,30,-1,30,28,20,-1,22,23,31,-1,31,30,22,-1,23,24,32,-1,32,31,23,-1,24,25,33,-1,33,32,24,-1,25,26,34,-1,34,33,25,-1,26,27,35,-1,35,34,26,-1,27,21,29,-1,29,35,27,-1,36,29,28,-1,36,28,30,-1,36,30,31,-1,36,31,32,-1,36,32,33,-1,36,33,34,-1,36,34,35,-1,36,35,29,-1]
Coordinate449 = x3d.Coordinate()

IndexedFaceSet448.coord = Coordinate449
TextureCoordinate450 = x3d.TextureCoordinate()

IndexedFaceSet448.texCoord = TextureCoordinate450

Shape444.geometry = IndexedFaceSet448

Transform443.children.append(Shape444)

HAnimSegment442.children.append(Transform443)

HAnimJoint441.children.append(HAnimSegment442)
HAnimJoint451 = x3d.HAnimJoint()
HAnimJoint451.name = "l_carpal_proximal_interphalangeal_5"
HAnimJoint451.DEF = "hanim_l_carpal_proximal_interphalangeal_5"
HAnimJoint451.center = [8.338,26.780001,-1.768]
HAnimJoint451.ulimit = [0,0,0]
HAnimJoint451.llimit = [0,0,0]
HAnimSegment452 = x3d.HAnimSegment()
HAnimSegment452.name = "l_carpal_middle_phalanx_5"
HAnimSegment452.DEF = "hanim_l_carpal_middle_phalanx_5"
Transform453 = x3d.Transform()
Transform453.translation = [8.338,26.780001,-1.768]
Shape454 = x3d.Shape()
Appearance455 = x3d.Appearance()
Material456 = x3d.Material()
Material456.diffuseColor = [0.588,0.588,0.588]

Appearance455.material = Material456
ImageTexture457 = x3d.ImageTexture()
ImageTexture457.USE = "JinLOA2TextureAtlas"

Appearance455.texture = ImageTexture457

Shape454.appearance = Appearance455
IndexedFaceSet458 = x3d.IndexedFaceSet()
IndexedFaceSet458.coordIndex = [0,1,3,-1,3,2,0,-1,0,5,4,-1,0,2,6,-1,6,5,0,-1,2,7,6,-1,2,3,8,-1,8,7,2,-1,3,9,8,-1,3,1,10,-1,10,9,3,-1,1,11,10,-1,1,0,4,-1,4,11,1,-1,4,5,13,-1,13,12,4,-1,5,6,14,-1,14,13,5,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,4,12,-1,12,19,11,-1,12,13,21,-1,21,20,12,-1,13,14,22,-1,22,21,13,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,12,20,-1,20,27,19,-1,28,20,21,-1,28,21,22,-1,28,22,23,-1,28,23,24,-1,28,24,25,-1,28,25,26,-1,28,26,27,-1,28,27,20,-1]
IndexedFaceSet458.creaseAngle = 3.14159
IndexedFaceSet458.texCoordIndex = [0,1,2,-1,2,3,0,-1,0,4,5,-1,0,3,6,-1,6,4,0,-1,3,7,6,-1,3,2,8,-1,8,7,3,-1,2,9,8,-1,2,1,10,-1,10,9,2,-1,1,11,10,-1,1,0,5,-1,5,11,1,-1,5,4,12,-1,12,13,5,-1,4,6,14,-1,14,12,4,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,5,13,-1,13,19,11,-1,13,12,20,-1,20,21,13,-1,12,14,22,-1,22,20,12,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,13,21,-1,21,27,19,-1,28,21,20,-1,28,20,22,-1,28,22,23,-1,28,23,24,-1,28,24,25,-1,28,25,26,-1,28,26,27,-1,28,27,21,-1]
Coordinate459 = x3d.Coordinate()

IndexedFaceSet458.coord = Coordinate459
TextureCoordinate460 = x3d.TextureCoordinate()

IndexedFaceSet458.texCoord = TextureCoordinate460

Shape454.geometry = IndexedFaceSet458

Transform453.children.append(Shape454)

HAnimSegment452.children.append(Transform453)

HAnimJoint451.children.append(HAnimSegment452)
HAnimJoint461 = x3d.HAnimJoint()
HAnimJoint461.name = "l_carpal_distal_interphalangeal_5"
HAnimJoint461.DEF = "hanim_l_carpal_distal_interphalangeal_5"
HAnimJoint461.center = [8.153,26.040001,-1.886]
HAnimJoint461.ulimit = [0,0,0]
HAnimJoint461.llimit = [0,0,0]
HAnimSegment462 = x3d.HAnimSegment()
HAnimSegment462.name = "l_carpal_distal_phalanx_5"
HAnimSegment462.DEF = "hanim_l_carpal_distal_phalanx_5"
Transform463 = x3d.Transform()
Transform463.translation = [8.153,26.040001,-1.886]
Shape464 = x3d.Shape()
Appearance465 = x3d.Appearance()
Material466 = x3d.Material()
Material466.diffuseColor = [0.588,0.588,0.588]

Appearance465.material = Material466
ImageTexture467 = x3d.ImageTexture()
ImageTexture467.USE = "JinLOA2TextureAtlas"

Appearance465.texture = ImageTexture467

Shape464.appearance = Appearance465
IndexedFaceSet468 = x3d.IndexedFaceSet()
IndexedFaceSet468.coordIndex = [0,1,3,-1,3,2,0,-1,0,5,4,-1,0,2,6,-1,6,5,0,-1,2,7,6,-1,2,3,8,-1,8,7,2,-1,3,9,8,-1,3,1,10,-1,10,9,3,-1,1,11,10,-1,1,0,4,-1,4,11,1,-1,4,5,13,-1,13,12,4,-1,5,6,14,-1,14,13,5,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,4,12,-1,12,19,11,-1,12,13,21,-1,21,20,12,-1,13,14,22,-1,22,21,13,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,12,20,-1,20,27,19,-1,28,20,21,-1,28,21,22,-1,28,22,23,-1,28,23,24,-1,28,24,25,-1,28,25,26,-1,28,26,27,-1,28,27,20,-1]
IndexedFaceSet468.creaseAngle = 3.14159
IndexedFaceSet468.texCoordIndex = [0,1,2,-1,2,3,0,-1,0,4,5,-1,0,3,6,-1,6,4,0,-1,3,7,6,-1,3,2,8,-1,8,7,3,-1,2,9,8,-1,2,1,10,-1,10,9,2,-1,1,11,10,-1,1,0,5,-1,5,11,1,-1,5,4,12,-1,12,13,5,-1,4,6,14,-1,14,12,4,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,5,13,-1,13,19,11,-1,13,12,20,-1,20,21,13,-1,12,14,22,-1,22,20,12,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,13,21,-1,21,27,19,-1,28,21,20,-1,28,20,22,-1,28,22,23,-1,28,23,24,-1,28,24,25,-1,28,25,26,-1,28,26,27,-1,28,27,21,-1]
Coordinate469 = x3d.Coordinate()

IndexedFaceSet468.coord = Coordinate469
TextureCoordinate470 = x3d.TextureCoordinate()

IndexedFaceSet468.texCoord = TextureCoordinate470

Shape464.geometry = IndexedFaceSet468

Transform463.children.append(Shape464)

HAnimSegment462.children.append(Transform463)

HAnimJoint461.children.append(HAnimSegment462)

HAnimJoint451.children.append(HAnimJoint461)

HAnimJoint441.children.append(HAnimJoint451)

HAnimJoint431.children.append(HAnimJoint441)

HAnimJoint271.children.append(HAnimJoint431)

HAnimJoint261.children.append(HAnimJoint271)

HAnimJoint251.children.append(HAnimJoint261)

HAnimJoint241.children.append(HAnimJoint251)

HAnimJoint231.children.append(HAnimJoint241)

HAnimJoint221.children.append(HAnimJoint231)
HAnimJoint471 = x3d.HAnimJoint()
HAnimJoint471.name = "r_acromioclavicular"
HAnimJoint471.DEF = "hanim_r_acromioclavicular"
HAnimJoint471.center = [-1.71,52.82,-0.6127]
HAnimJoint471.ulimit = [0,0,0]
HAnimJoint471.llimit = [0,0,0]
HAnimSegment472 = x3d.HAnimSegment()
HAnimSegment472.name = "r_clavicle"
HAnimSegment472.DEF = "hanim_r_clavicle"
Transform473 = x3d.Transform()
Transform473.translation = [-1.71,52.82,-0.6127]
Shape474 = x3d.Shape()
Appearance475 = x3d.Appearance()
Material476 = x3d.Material()
Material476.diffuseColor = [0.588,0.588,0.588]

Appearance475.material = Material476
ImageTexture477 = x3d.ImageTexture()
ImageTexture477.USE = "JinLOA2TextureAtlas"

Appearance475.texture = ImageTexture477

Shape474.appearance = Appearance475
IndexedFaceSet478 = x3d.IndexedFaceSet()
IndexedFaceSet478.coordIndex = [9,0,1,-1,1,6,9,-1,6,1,2,-1,2,5,6,-1,8,5,2,-1,2,3,8,-1,8,3,4,-1,4,7,8,-1,9,7,4,-1,4,0,9,-1,4,3,2,-1,0,4,2,-1,1,0,2,-1,10,14,13,-1,10,13,12,-1,11,10,12,-1,6,10,11,-1,11,9,6,-1,9,11,12,-1,12,7,9,-1,7,12,13,-1,13,8,7,-1,8,13,14,-1,14,5,8,-1,5,14,10,-1,10,6,5,-1]
IndexedFaceSet478.creaseAngle = 3.14159
IndexedFaceSet478.texCoordIndex = [9,0,1,-1,1,6,9,-1,6,1,2,-1,2,5,6,-1,8,5,2,-1,2,3,8,-1,8,3,4,-1,4,7,8,-1,9,7,4,-1,4,0,9,-1,4,3,2,-1,0,4,2,-1,1,0,2,-1,10,14,13,-1,10,13,12,-1,11,10,12,-1,6,10,11,-1,11,9,6,-1,9,11,12,-1,12,7,9,-1,7,12,13,-1,13,8,7,-1,8,13,14,-1,14,5,8,-1,5,14,10,-1,10,6,5,-1]
Coordinate479 = x3d.Coordinate()

IndexedFaceSet478.coord = Coordinate479
TextureCoordinate480 = x3d.TextureCoordinate()

IndexedFaceSet478.texCoord = TextureCoordinate480

Shape474.geometry = IndexedFaceSet478

Transform473.children.append(Shape474)

HAnimSegment472.children.append(Transform473)

HAnimJoint471.children.append(HAnimSegment472)
HAnimJoint481 = x3d.HAnimJoint()
HAnimJoint481.name = "r_sternoclavicular"
HAnimJoint481.DEF = "hanim_r_sternoclavicular"
HAnimJoint481.center = [-5.464,52.060001,-0.5732]
HAnimJoint481.ulimit = [0,0,0]
HAnimJoint481.llimit = [0,0,0]
HAnimSegment482 = x3d.HAnimSegment()
HAnimSegment482.name = "r_scapula"
HAnimSegment482.DEF = "hanim_r_scapula"
Transform483 = x3d.Transform()
Transform483.translation = [-5.464,52.060001,-0.5732]
Shape484 = x3d.Shape()
Appearance485 = x3d.Appearance()
Material486 = x3d.Material()
Material486.diffuseColor = [0.588,0.588,0.588]

Appearance485.material = Material486
ImageTexture487 = x3d.ImageTexture()
ImageTexture487.USE = "JinLOA2TextureAtlas"

Appearance485.texture = ImageTexture487

Shape484.appearance = Appearance485
IndexedFaceSet488 = x3d.IndexedFaceSet()
IndexedFaceSet488.coordIndex = [5,1,0,-1,0,4,5,-1,4,0,2,-1,2,3,4,-1,3,2,6,-1,6,9,3,-1,7,8,1,-1,1,5,7,-1,6,2,0,-1,0,8,6,-1,0,1,8,-1,9,6,8,-1,8,7,9,-1,4,10,11,-1,11,5,4,-1,5,11,12,-1,12,7,5,-1,7,12,13,-1,13,9,7,-1,9,13,14,-1,14,3,9,-1,3,14,10,-1,10,4,3,-1,10,15,11,-1,11,15,12,-1,12,15,13,-1,13,15,14,-1,14,15,10,-1]
IndexedFaceSet488.creaseAngle = 3.14159
IndexedFaceSet488.texCoordIndex = [5,1,0,-1,0,4,5,-1,4,0,2,-1,2,3,4,-1,3,2,6,-1,6,8,3,-1,9,7,1,-1,1,5,9,-1,6,2,0,-1,0,7,6,-1,0,1,7,-1,12,10,11,-1,11,13,12,-1,4,14,15,-1,15,5,4,-1,5,15,16,-1,16,9,5,-1,13,16,17,-1,17,12,13,-1,8,17,18,-1,18,3,8,-1,3,18,14,-1,14,4,3,-1,14,19,15,-1,15,19,16,-1,16,19,17,-1,17,19,18,-1,18,19,14,-1]
Coordinate489 = x3d.Coordinate()

IndexedFaceSet488.coord = Coordinate489
TextureCoordinate490 = x3d.TextureCoordinate()

IndexedFaceSet488.texCoord = TextureCoordinate490

Shape484.geometry = IndexedFaceSet488

Transform483.children.append(Shape484)

HAnimSegment482.children.append(Transform483)

HAnimJoint481.children.append(HAnimSegment482)
HAnimJoint491 = x3d.HAnimJoint()
HAnimJoint491.name = "r_shoulder"
HAnimJoint491.DEF = "hanim_r_shoulder"
HAnimJoint491.center = [-7.336,51.48,-0.1452]
HAnimJoint491.ulimit = [0,0,0]
HAnimJoint491.llimit = [0,0,0]
HAnimSegment492 = x3d.HAnimSegment()
HAnimSegment492.name = "r_upperarm"
HAnimSegment492.DEF = "hanim_r_upperarm"
Transform493 = x3d.Transform()
Transform493.translation = [-7.336,51.48,-0.1452]
Shape494 = x3d.Shape()
Appearance495 = x3d.Appearance()
Material496 = x3d.Material()
Material496.diffuseColor = [0.588,0.588,0.588]

Appearance495.material = Material496
ImageTexture497 = x3d.ImageTexture()
ImageTexture497.USE = "JinLOA2TextureAtlas"

Appearance495.texture = ImageTexture497

Shape494.appearance = Appearance495
IndexedFaceSet498 = x3d.IndexedFaceSet()
IndexedFaceSet498.coordIndex = [0,1,2,-1,0,2,3,-1,4,0,3,-1,0,5,6,-1,6,1,0,-1,1,6,7,-1,7,2,1,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,9,4,3,-1,4,9,5,-1,5,0,4,-1,5,10,11,-1,11,6,5,-1,6,11,12,-1,12,7,6,-1,7,12,13,-1,13,8,7,-1,8,13,14,-1,14,9,8,-1,9,14,10,-1,10,5,9,-1,10,15,16,-1,16,11,10,-1,11,16,17,-1,17,12,11,-1,12,17,18,-1,18,13,12,-1,13,18,19,-1,19,14,13,-1,14,19,15,-1,15,10,14,-1,38,37,36,-1,38,36,35,-1,39,38,35,-1,21,16,15,-1,15,20,21,-1,22,17,16,-1,16,21,22,-1,23,18,17,-1,17,22,23,-1,24,19,18,-1,18,23,24,-1,20,15,19,-1,19,24,20,-1,26,21,20,-1,20,25,26,-1,27,22,21,-1,21,26,27,-1,28,23,22,-1,22,27,28,-1,29,24,23,-1,23,28,29,-1,25,20,24,-1,24,29,25,-1,31,26,25,-1,25,30,31,-1,32,27,26,-1,26,31,32,-1,33,28,27,-1,27,32,33,-1,34,29,28,-1,28,33,34,-1,30,25,29,-1,29,34,30,-1,36,31,30,-1,30,35,36,-1,37,32,31,-1,31,36,37,-1,38,33,32,-1,32,37,38,-1,39,34,33,-1,33,38,39,-1,35,30,34,-1,34,39,35,-1]
IndexedFaceSet498.creaseAngle = 3.14159
IndexedFaceSet498.texCoordIndex = [1,0,2,-1,1,2,3,-1,61,1,3,-1,1,6,5,-1,5,0,1,-1,0,5,7,-1,7,2,0,-1,2,7,8,-1,8,3,2,-1,25,26,9,-1,9,4,25,-1,4,9,6,-1,6,1,4,-1,6,11,10,-1,10,5,6,-1,5,10,12,-1,12,7,5,-1,7,12,13,-1,13,8,7,-1,27,28,14,-1,14,9,27,-1,9,14,11,-1,11,6,9,-1,11,16,15,-1,15,10,11,-1,10,15,17,-1,17,12,10,-1,12,17,18,-1,18,13,12,-1,29,30,19,-1,19,14,29,-1,14,19,16,-1,16,11,14,-1,36,35,54,-1,36,54,53,-1,37,36,53,-1,20,15,16,-1,16,21,20,-1,22,17,15,-1,15,20,22,-1,23,18,17,-1,17,22,23,-1,24,19,31,-1,31,32,24,-1,21,16,19,-1,19,24,21,-1,40,39,38,-1,38,41,40,-1,43,42,55,-1,55,56,43,-1,45,44,42,-1,42,43,45,-1,47,46,44,-1,44,45,47,-1,41,38,46,-1,46,47,41,-1,48,40,41,-1,41,49,48,-1,50,43,57,-1,57,58,50,-1,51,45,43,-1,43,50,51,-1,52,47,45,-1,45,51,52,-1,49,41,47,-1,47,52,49,-1,34,48,49,-1,49,33,34,-1,35,50,59,-1,59,60,35,-1,36,51,50,-1,50,35,36,-1,37,52,51,-1,51,36,37,-1,33,49,52,-1,52,37,33,-1]
Coordinate499 = x3d.Coordinate()

IndexedFaceSet498.coord = Coordinate499
TextureCoordinate500 = x3d.TextureCoordinate()

IndexedFaceSet498.texCoord = TextureCoordinate500

Shape494.geometry = IndexedFaceSet498

Transform493.children.append(Shape494)

HAnimSegment492.children.append(Transform493)

HAnimJoint491.children.append(HAnimSegment492)
HAnimJoint501 = x3d.HAnimJoint()
HAnimJoint501.name = "r_elbow"
HAnimJoint501.DEF = "hanim_r_elbow"
HAnimJoint501.center = [-8.093,40.380001,-0.2502]
HAnimJoint501.ulimit = [0,0,0]
HAnimJoint501.llimit = [0,0,0]
HAnimSegment502 = x3d.HAnimSegment()
HAnimSegment502.name = "r_forearm"
HAnimSegment502.DEF = "hanim_r_forearm"
Transform503 = x3d.Transform()
Transform503.translation = [-8.093,40.380001,-0.2502]
Shape504 = x3d.Shape()
Appearance505 = x3d.Appearance()
Material506 = x3d.Material()
Material506.diffuseColor = [0.588,0.588,0.588]

Appearance505.material = Material506
ImageTexture507 = x3d.ImageTexture()
ImageTexture507.USE = "JinLOA2TextureAtlas"

Appearance505.texture = ImageTexture507

Shape504.appearance = Appearance505
IndexedFaceSet508 = x3d.IndexedFaceSet()
IndexedFaceSet508.coordIndex = [0,1,2,-1,0,2,3,-1,4,0,3,-1,0,5,6,-1,6,1,0,-1,1,6,7,-1,7,2,1,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,9,4,3,-1,4,9,5,-1,5,0,4,-1,5,10,11,-1,11,6,5,-1,6,11,12,-1,12,7,6,-1,7,12,13,-1,13,8,7,-1,8,13,14,-1,14,9,8,-1,9,14,10,-1,10,5,9,-1,10,15,16,-1,16,11,10,-1,11,16,17,-1,17,12,11,-1,12,17,18,-1,18,13,12,-1,13,18,19,-1,19,14,13,-1,14,19,15,-1,15,10,14,-1,23,22,21,-1,23,21,20,-1,24,23,20,-1,21,16,15,-1,15,20,21,-1,22,17,16,-1,16,21,22,-1,23,18,17,-1,17,22,23,-1,24,19,18,-1,18,23,24,-1,20,15,19,-1,19,24,20,-1]
IndexedFaceSet508.creaseAngle = 3.14159
IndexedFaceSet508.texCoordIndex = [26,25,2,-1,26,2,3,-1,4,26,3,-1,0,5,6,-1,6,1,0,-1,27,28,7,-1,7,2,27,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,9,4,3,-1,4,9,5,-1,5,0,4,-1,5,10,11,-1,11,6,5,-1,29,30,12,-1,12,7,29,-1,7,12,13,-1,13,8,7,-1,8,13,14,-1,14,9,8,-1,9,14,10,-1,10,5,9,-1,10,15,16,-1,16,11,10,-1,31,32,17,-1,17,12,31,-1,12,17,18,-1,18,13,12,-1,13,18,19,-1,19,14,13,-1,14,19,15,-1,15,10,14,-1,23,22,34,-1,23,34,33,-1,24,23,33,-1,21,16,15,-1,15,20,21,-1,22,17,35,-1,35,36,22,-1,23,18,17,-1,17,22,23,-1,24,19,18,-1,18,23,24,-1,20,15,19,-1,19,24,20,-1]
Coordinate509 = x3d.Coordinate()

IndexedFaceSet508.coord = Coordinate509
TextureCoordinate510 = x3d.TextureCoordinate()

IndexedFaceSet508.texCoord = TextureCoordinate510

Shape504.geometry = IndexedFaceSet508

Transform503.children.append(Shape504)

HAnimSegment502.children.append(Transform503)

HAnimJoint501.children.append(HAnimSegment502)
HAnimJoint511 = x3d.HAnimJoint()
HAnimJoint511.name = "r_radiocarpal"
HAnimJoint511.DEF = "hanim_r_radiocarpal"
HAnimJoint511.center = [-7.899,31.43,-0.3809]
HAnimJoint511.ulimit = [0,0,0]
HAnimJoint511.llimit = [0,0,0]
HAnimSegment512 = x3d.HAnimSegment()
HAnimSegment512.name = "r_carpal"
HAnimSegment512.DEF = "hanim_r_carpal"
Transform513 = x3d.Transform()
Transform513.translation = [-7.899,31.43,-0.3809]
Shape514 = x3d.Shape()
Appearance515 = x3d.Appearance()
Material516 = x3d.Material()
Material516.diffuseColor = [0.588,0.588,0.588]

Appearance515.material = Material516
ImageTexture517 = x3d.ImageTexture()
ImageTexture517.USE = "JinLOA2TextureAtlas"

Appearance515.texture = ImageTexture517

Shape514.appearance = Appearance515
IndexedFaceSet518 = x3d.IndexedFaceSet()
IndexedFaceSet518.coordIndex = [36,41,38,-1,38,37,36,-1,44,54,45,-1,31,30,53,-1,53,4,31,-1,6,7,11,-1,11,10,6,-1,11,32,33,-1,33,10,11,-1,34,11,7,-1,7,24,34,-1,13,27,15,-1,15,17,13,-1,25,35,22,-1,30,20,5,-1,13,32,11,-1,11,34,13,-1,23,29,28,-1,28,22,23,-1,17,15,14,-1,14,16,17,-1,18,19,53,-1,53,5,18,-1,9,17,16,-1,16,8,9,-1,14,15,43,-1,43,42,14,-1,21,33,8,-1,8,16,21,-1,21,23,22,-1,22,35,21,-1,39,38,41,-1,41,40,39,-1,26,24,20,-1,27,26,20,-1,20,12,27,-1,3,43,12,-1,12,30,3,-1,0,25,28,-1,28,54,0,-1,13,17,9,-1,9,32,13,-1,28,29,31,-1,29,23,14,-1,14,42,29,-1,16,14,23,-1,23,21,16,-1,30,31,2,-1,2,3,30,-1,8,33,32,-1,32,9,8,-1,33,21,35,-1,35,10,33,-1,35,25,6,-1,6,10,35,-1,13,34,26,-1,26,27,13,-1,34,24,26,-1,1,46,47,-1,47,0,1,-1,25,0,47,-1,47,48,25,-1,25,48,49,-1,49,6,25,-1,6,49,50,-1,50,7,6,-1,24,7,50,-1,50,51,24,-1,24,51,46,-1,46,1,24,-1,2,42,43,-1,43,3,2,-1,15,27,12,-1,12,43,15,-1,29,42,2,-1,2,31,29,-1,18,5,52,-1,52,44,18,-1,28,25,22,-1,18,44,45,-1,45,19,18,-1,1,44,52,-1,52,24,1,-1,45,28,4,-1,28,31,4,-1,45,4,19,-1,37,47,46,-1,46,36,37,-1,48,47,37,-1,37,38,48,-1,39,49,48,-1,48,38,39,-1,40,50,49,-1,49,39,40,-1,51,50,40,-1,40,41,51,-1,36,46,51,-1,51,41,36,-1,24,52,20,-1,52,5,20,-1,53,30,5,-1,53,19,4,-1,54,28,45,-1,44,1,0,-1,0,54,44,-1,20,30,12,-1]
IndexedFaceSet518.creaseAngle = 3.14159
IndexedFaceSet518.texCoordIndex = [0,3,2,-1,2,1,0,-1,4,6,5,-1,8,7,10,-1,10,9,8,-1,12,11,14,-1,14,13,12,-1,14,16,15,-1,15,13,14,-1,17,14,11,-1,11,18,17,-1,20,19,22,-1,22,21,20,-1,23,25,24,-1,7,27,26,-1,20,16,14,-1,14,17,20,-1,28,30,29,-1,29,24,28,-1,21,22,32,-1,32,31,21,-1,33,34,10,-1,10,26,33,-1,35,21,31,-1,31,36,35,-1,32,22,38,-1,38,37,32,-1,39,15,36,-1,36,31,39,-1,39,28,24,-1,24,25,39,-1,40,2,3,-1,3,41,40,-1,42,18,27,-1,19,42,27,-1,27,43,19,-1,44,38,43,-1,43,7,44,-1,45,23,29,-1,29,6,45,-1,20,21,35,-1,35,16,20,-1,29,30,8,-1,30,28,32,-1,32,37,30,-1,31,32,28,-1,28,39,31,-1,7,8,46,-1,46,44,7,-1,36,15,16,-1,16,35,36,-1,15,39,25,-1,25,13,15,-1,25,23,12,-1,12,13,25,-1,20,17,42,-1,42,19,20,-1,17,18,42,-1,47,49,48,-1,48,45,47,-1,23,45,48,-1,48,50,23,-1,23,50,51,-1,51,12,23,-1,12,51,52,-1,52,11,12,-1,18,11,52,-1,52,53,18,-1,18,53,49,-1,49,47,18,-1,46,37,38,-1,38,44,46,-1,22,19,43,-1,43,38,22,-1,30,37,46,-1,46,8,30,-1,33,26,54,-1,54,4,33,-1,29,23,24,-1,33,4,5,-1,5,34,33,-1,47,4,54,-1,54,18,47,-1,5,29,9,-1,29,8,9,-1,5,9,34,-1,1,48,49,-1,49,0,1,-1,50,48,1,-1,1,2,50,-1,40,51,50,-1,50,2,40,-1,41,52,51,-1,51,40,41,-1,53,52,41,-1,41,3,53,-1,0,49,53,-1,53,3,0,-1,18,54,27,-1,54,26,27,-1,10,7,26,-1,10,34,9,-1,6,29,5,-1,4,47,45,-1,45,6,4,-1,27,7,43,-1]
Coordinate519 = x3d.Coordinate()

IndexedFaceSet518.coord = Coordinate519
TextureCoordinate520 = x3d.TextureCoordinate()

IndexedFaceSet518.texCoord = TextureCoordinate520

Shape514.geometry = IndexedFaceSet518

Transform513.children.append(Shape514)

HAnimSegment512.children.append(Transform513)

HAnimJoint511.children.append(HAnimSegment512)
HAnimJoint521 = x3d.HAnimJoint()
HAnimJoint521.name = "r_carpometacarpal_1"
HAnimJoint521.DEF = "hanim_r_carpometacarpal_1"
HAnimJoint521.center = [-8.205,29.6,1.302]
HAnimJoint521.ulimit = [0,0,0]
HAnimJoint521.llimit = [0,0,0]
HAnimSegment522 = x3d.HAnimSegment()
HAnimSegment522.name = "r_metacarpal_1"
HAnimSegment522.DEF = "hanim_r_metacarpal_1"
Transform523 = x3d.Transform()
Transform523.translation = [-8.205,29.6,1.302]
Shape524 = x3d.Shape()
Appearance525 = x3d.Appearance()
Material526 = x3d.Material()
Material526.diffuseColor = [0.588,0.588,0.588]

Appearance525.material = Material526
ImageTexture527 = x3d.ImageTexture()
ImageTexture527.USE = "JinLOA2TextureAtlas"

Appearance525.texture = ImageTexture527

Shape524.appearance = Appearance525
IndexedFaceSet528 = x3d.IndexedFaceSet()
IndexedFaceSet528.coordIndex = [0,2,3,-1,3,1,0,-1,0,4,5,-1,0,5,6,-1,6,2,0,-1,2,6,7,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,3,9,10,-1,10,1,3,-1,1,10,11,-1,1,11,4,-1,4,0,1,-1,4,12,13,-1,13,5,4,-1,5,13,14,-1,14,6,5,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,12,-1,12,4,11,-1,12,20,21,-1,21,13,12,-1,13,21,22,-1,22,14,13,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,20,-1,20,12,19,-1,20,28,29,-1,29,21,20,-1,21,29,30,-1,30,22,21,-1,22,30,31,-1,31,23,22,-1,23,31,32,-1,32,24,23,-1,24,32,33,-1,33,25,24,-1,25,33,34,-1,34,26,25,-1,26,34,35,-1,35,27,26,-1,27,35,28,-1,28,20,27,-1,36,29,28,-1,36,30,29,-1,36,31,30,-1,36,32,31,-1,36,33,32,-1,36,34,33,-1,36,35,34,-1,36,28,35,-1]
IndexedFaceSet528.creaseAngle = 3.14159
IndexedFaceSet528.texCoordIndex = [0,3,2,-1,2,1,0,-1,0,5,4,-1,0,4,6,-1,6,3,0,-1,3,6,7,-1,3,7,8,-1,8,2,3,-1,2,8,9,-1,2,9,10,-1,10,1,2,-1,1,10,11,-1,1,11,5,-1,5,0,1,-1,5,13,12,-1,12,4,5,-1,4,12,14,-1,14,6,4,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,13,-1,13,5,11,-1,13,21,20,-1,20,12,13,-1,12,20,22,-1,22,14,12,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,21,-1,21,13,19,-1,21,29,28,-1,28,20,21,-1,20,28,30,-1,30,22,20,-1,22,30,31,-1,31,23,22,-1,23,31,32,-1,32,24,23,-1,24,32,33,-1,33,25,24,-1,25,33,34,-1,34,26,25,-1,26,34,35,-1,35,27,26,-1,27,35,29,-1,29,21,27,-1,36,28,29,-1,36,30,28,-1,36,31,30,-1,36,32,31,-1,36,33,32,-1,36,34,33,-1,36,35,34,-1,36,29,35,-1]
Coordinate529 = x3d.Coordinate()

IndexedFaceSet528.coord = Coordinate529
TextureCoordinate530 = x3d.TextureCoordinate()

IndexedFaceSet528.texCoord = TextureCoordinate530

Shape524.geometry = IndexedFaceSet528

Transform523.children.append(Shape524)

HAnimSegment522.children.append(Transform523)

HAnimJoint521.children.append(HAnimSegment522)
HAnimJoint531 = x3d.HAnimJoint()
HAnimJoint531.name = "r_metacarpophalangeal_1"
HAnimJoint531.DEF = "hanim_r_metacarpophalangeal_1"
HAnimJoint531.center = [-8.08,28.73,1.55]
HAnimJoint531.ulimit = [0,0,0]
HAnimJoint531.llimit = [0,0,0]
HAnimSegment532 = x3d.HAnimSegment()
HAnimSegment532.name = "r_carpal_proximal_phalanx_1"
HAnimSegment532.DEF = "hanim_r_carpal_proximal_phalanx_1"
Transform533 = x3d.Transform()
Transform533.translation = [-8.08,28.73,1.55]
Shape534 = x3d.Shape()
Appearance535 = x3d.Appearance()
Material536 = x3d.Material()
Material536.diffuseColor = [0.588,0.588,0.588]

Appearance535.material = Material536
ImageTexture537 = x3d.ImageTexture()
ImageTexture537.USE = "JinLOA2TextureAtlas"

Appearance535.texture = ImageTexture537

Shape534.appearance = Appearance535
IndexedFaceSet538 = x3d.IndexedFaceSet()
IndexedFaceSet538.coordIndex = [0,2,3,-1,3,1,0,-1,0,4,5,-1,0,5,6,-1,6,2,0,-1,2,6,7,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,3,9,10,-1,10,1,3,-1,1,10,11,-1,1,11,4,-1,4,0,1,-1,4,12,13,-1,13,5,4,-1,5,13,14,-1,14,6,5,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,12,-1,12,4,11,-1,12,20,21,-1,21,13,12,-1,13,21,22,-1,22,14,13,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,20,-1,20,12,19,-1,20,28,29,-1,29,21,20,-1,21,29,30,-1,30,22,21,-1,22,30,31,-1,31,23,22,-1,23,31,32,-1,32,24,23,-1,24,32,33,-1,33,25,24,-1,25,33,34,-1,34,26,25,-1,26,34,35,-1,35,27,26,-1,27,35,28,-1,28,20,27,-1,36,29,28,-1,36,30,29,-1,36,31,30,-1,36,32,31,-1,36,33,32,-1,36,34,33,-1,36,35,34,-1,36,28,35,-1]
IndexedFaceSet538.creaseAngle = 3.14159
IndexedFaceSet538.texCoordIndex = [0,3,2,-1,2,1,0,-1,0,5,4,-1,0,4,6,-1,6,3,0,-1,3,6,7,-1,3,7,8,-1,8,2,3,-1,2,8,9,-1,2,9,10,-1,10,1,2,-1,1,10,11,-1,1,11,5,-1,5,0,1,-1,5,13,12,-1,12,4,5,-1,4,12,14,-1,14,6,4,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,13,-1,13,5,11,-1,13,21,20,-1,20,12,13,-1,12,20,22,-1,22,14,12,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,21,-1,21,13,19,-1,21,29,28,-1,28,20,21,-1,20,28,30,-1,30,22,20,-1,22,30,31,-1,31,23,22,-1,23,31,32,-1,32,24,23,-1,24,32,33,-1,33,25,24,-1,25,33,34,-1,34,26,25,-1,26,34,35,-1,35,27,26,-1,27,35,29,-1,29,21,27,-1,36,28,29,-1,36,30,28,-1,36,31,30,-1,36,32,31,-1,36,33,32,-1,36,34,33,-1,36,35,34,-1,36,29,35,-1]
Coordinate539 = x3d.Coordinate()

IndexedFaceSet538.coord = Coordinate539
TextureCoordinate540 = x3d.TextureCoordinate()

IndexedFaceSet538.texCoord = TextureCoordinate540

Shape534.geometry = IndexedFaceSet538

Transform533.children.append(Shape534)

HAnimSegment532.children.append(Transform533)

HAnimJoint531.children.append(HAnimSegment532)
HAnimJoint541 = x3d.HAnimJoint()
HAnimJoint541.name = "r_carpal_interphalangeal_1"
HAnimJoint541.DEF = "hanim_r_carpal_interphalangeal_1"
HAnimJoint541.center = [-7.832,27.85,1.735]
HAnimJoint541.ulimit = [0,0,0]
HAnimJoint541.llimit = [0,0,0]
HAnimSegment542 = x3d.HAnimSegment()
HAnimSegment542.name = "r_carpal_distal_phalanx_1"
HAnimSegment542.DEF = "hanim_r_carpal_distal_phalanx_1"
Transform543 = x3d.Transform()
Transform543.translation = [-7.832,27.85,1.735]
Shape544 = x3d.Shape()
Appearance545 = x3d.Appearance()
Material546 = x3d.Material()
Material546.diffuseColor = [0.588,0.588,0.588]

Appearance545.material = Material546
ImageTexture547 = x3d.ImageTexture()
ImageTexture547.USE = "JinLOA2TextureAtlas"

Appearance545.texture = ImageTexture547

Shape544.appearance = Appearance545
IndexedFaceSet548 = x3d.IndexedFaceSet()
IndexedFaceSet548.coordIndex = [0,2,3,-1,3,1,0,-1,0,4,5,-1,0,5,6,-1,6,2,0,-1,2,6,7,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,3,9,10,-1,10,1,3,-1,1,10,11,-1,1,11,4,-1,4,0,1,-1,4,12,13,-1,13,5,4,-1,5,13,14,-1,14,6,5,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,12,-1,12,4,11,-1,12,20,21,-1,21,13,12,-1,13,21,22,-1,22,14,13,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,20,-1,20,12,19,-1,28,21,20,-1,28,22,21,-1,28,23,22,-1,28,24,23,-1,28,25,24,-1,28,26,25,-1,28,27,26,-1,28,20,27,-1]
IndexedFaceSet548.creaseAngle = 3.14159
IndexedFaceSet548.texCoordIndex = [0,3,2,-1,2,1,0,-1,0,5,4,-1,0,4,6,-1,6,3,0,-1,3,6,7,-1,3,7,8,-1,8,2,3,-1,2,8,9,-1,2,9,10,-1,10,1,2,-1,1,10,11,-1,1,11,5,-1,5,0,1,-1,5,13,12,-1,12,4,5,-1,4,12,14,-1,14,6,4,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,13,-1,13,5,11,-1,13,21,20,-1,20,12,13,-1,12,20,22,-1,22,14,12,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,21,-1,21,13,19,-1,28,20,21,-1,28,22,20,-1,28,23,22,-1,28,24,23,-1,28,25,24,-1,28,26,25,-1,28,27,26,-1,28,21,27,-1]
Coordinate549 = x3d.Coordinate()

IndexedFaceSet548.coord = Coordinate549
TextureCoordinate550 = x3d.TextureCoordinate()

IndexedFaceSet548.texCoord = TextureCoordinate550

Shape544.geometry = IndexedFaceSet548

Transform543.children.append(Shape544)

HAnimSegment542.children.append(Transform543)

HAnimJoint541.children.append(HAnimSegment542)

HAnimJoint531.children.append(HAnimJoint541)

HAnimJoint521.children.append(HAnimJoint531)

HAnimJoint511.children.append(HAnimJoint521)
HAnimJoint551 = x3d.HAnimJoint()
HAnimJoint551.name = "r_carpometacarpal_2"
HAnimJoint551.DEF = "hanim_r_carpometacarpal_2"
HAnimJoint551.center = [-8.376,28.549999,0.5997]
HAnimJoint551.ulimit = [0,0,0]
HAnimJoint551.llimit = [0,0,0]
HAnimSegment552 = x3d.HAnimSegment()
HAnimSegment552.name = "r_metacarpal_2"
HAnimSegment552.DEF = "hanim_r_metacarpal_2"
Transform553 = x3d.Transform()
Transform553.translation = [-8.376,28.549999,0.5997]
Shape554 = x3d.Shape()
Appearance555 = x3d.Appearance()
Material556 = x3d.Material()
Material556.diffuseColor = [0.588,0.588,0.588]

Appearance555.material = Material556
ImageTexture557 = x3d.ImageTexture()
ImageTexture557.USE = "JinLOA2TextureAtlas"

Appearance555.texture = ImageTexture557

Shape554.appearance = Appearance555
IndexedFaceSet558 = x3d.IndexedFaceSet()
IndexedFaceSet558.coordIndex = [0,2,3,-1,3,1,0,-1,0,4,5,-1,0,5,6,-1,6,2,0,-1,2,6,7,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,3,9,10,-1,10,1,3,-1,1,10,11,-1,1,11,4,-1,4,0,1,-1,4,12,13,-1,13,5,4,-1,5,13,14,-1,14,6,5,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,12,-1,12,4,11,-1,12,20,21,-1,21,13,12,-1,13,21,22,-1,22,14,13,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,20,-1,20,12,19,-1,20,28,29,-1,29,21,20,-1,21,29,30,-1,30,22,21,-1,22,30,31,-1,31,23,22,-1,23,31,32,-1,32,24,23,-1,24,32,33,-1,33,25,24,-1,25,33,34,-1,34,26,25,-1,26,34,35,-1,35,27,26,-1,27,35,28,-1,28,20,27,-1,36,29,28,-1,36,30,29,-1,36,31,30,-1,36,32,31,-1,36,33,32,-1,36,34,33,-1,36,35,34,-1,36,28,35,-1]
IndexedFaceSet558.creaseAngle = 3.14159
IndexedFaceSet558.texCoordIndex = [0,3,2,-1,2,1,0,-1,0,5,4,-1,0,4,6,-1,6,3,0,-1,3,6,7,-1,3,7,8,-1,8,2,3,-1,2,8,9,-1,2,9,10,-1,10,1,2,-1,1,10,11,-1,1,11,5,-1,5,0,1,-1,5,13,12,-1,12,4,5,-1,4,12,14,-1,14,6,4,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,13,-1,13,5,11,-1,13,21,20,-1,20,12,13,-1,12,20,22,-1,22,14,12,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,21,-1,21,13,19,-1,21,29,28,-1,28,20,21,-1,20,28,30,-1,30,22,20,-1,22,30,31,-1,31,23,22,-1,23,31,32,-1,32,24,23,-1,24,32,33,-1,33,25,24,-1,25,33,34,-1,34,26,25,-1,26,34,35,-1,35,27,26,-1,27,35,29,-1,29,21,27,-1,36,28,29,-1,36,30,28,-1,36,31,30,-1,36,32,31,-1,36,33,32,-1,36,34,33,-1,36,35,34,-1,36,29,35,-1]
Coordinate559 = x3d.Coordinate()

IndexedFaceSet558.coord = Coordinate559
TextureCoordinate560 = x3d.TextureCoordinate()

IndexedFaceSet558.texCoord = TextureCoordinate560

Shape554.geometry = IndexedFaceSet558

Transform553.children.append(Shape554)

HAnimSegment552.children.append(Transform553)

HAnimJoint551.children.append(HAnimSegment552)
HAnimJoint561 = x3d.HAnimJoint()
HAnimJoint561.name = "r_metacarpophalangeal_2"
HAnimJoint561.DEF = "hanim_r_metacarpophalangeal_2"
HAnimJoint561.center = [-8.52,27.24,0.6551]
HAnimJoint561.ulimit = [0,0,0]
HAnimJoint561.llimit = [0,0,0]
HAnimSegment562 = x3d.HAnimSegment()
HAnimSegment562.name = "r_carpal_proximal_phalanx_2"
HAnimSegment562.DEF = "hanim_r_carpal_proximal_phalanx_2"
Transform563 = x3d.Transform()
Transform563.translation = [-8.52,27.24,0.6551]
Shape564 = x3d.Shape()
Appearance565 = x3d.Appearance()
Material566 = x3d.Material()
Material566.diffuseColor = [0.588,0.588,0.588]

Appearance565.material = Material566
ImageTexture567 = x3d.ImageTexture()
ImageTexture567.USE = "JinLOA2TextureAtlas"

Appearance565.texture = ImageTexture567

Shape564.appearance = Appearance565
IndexedFaceSet568 = x3d.IndexedFaceSet()
IndexedFaceSet568.coordIndex = [0,2,3,-1,3,1,0,-1,0,4,5,-1,0,5,6,-1,6,2,0,-1,2,6,7,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,3,9,10,-1,10,1,3,-1,1,10,11,-1,1,11,4,-1,4,0,1,-1,4,12,13,-1,13,5,4,-1,5,13,14,-1,14,6,5,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,12,-1,12,4,11,-1,12,20,21,-1,21,13,12,-1,13,21,22,-1,22,14,13,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,20,-1,20,12,19,-1,20,28,29,-1,29,21,20,-1,21,29,30,-1,30,22,21,-1,22,30,31,-1,31,23,22,-1,23,31,32,-1,32,24,23,-1,24,32,33,-1,33,25,24,-1,25,33,34,-1,34,26,25,-1,26,34,35,-1,35,27,26,-1,27,35,28,-1,28,20,27,-1,36,29,28,-1,36,30,29,-1,36,31,30,-1,36,32,31,-1,36,33,32,-1,36,34,33,-1,36,35,34,-1,36,28,35,-1]
IndexedFaceSet568.creaseAngle = 3.14159
IndexedFaceSet568.texCoordIndex = [0,3,2,-1,2,1,0,-1,0,5,4,-1,0,4,6,-1,6,3,0,-1,3,6,7,-1,3,7,8,-1,8,2,3,-1,2,8,9,-1,2,9,10,-1,10,1,2,-1,1,10,11,-1,1,11,5,-1,5,0,1,-1,5,13,12,-1,12,4,5,-1,4,12,14,-1,14,6,4,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,13,-1,13,5,11,-1,13,21,20,-1,20,12,13,-1,12,20,22,-1,22,14,12,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,21,-1,21,13,19,-1,21,29,28,-1,28,20,21,-1,20,28,30,-1,30,22,20,-1,22,30,31,-1,31,23,22,-1,23,31,32,-1,32,24,23,-1,24,32,33,-1,33,25,24,-1,25,33,34,-1,34,26,25,-1,26,34,35,-1,35,27,26,-1,27,35,29,-1,29,21,27,-1,36,28,29,-1,36,30,28,-1,36,31,30,-1,36,32,31,-1,36,33,32,-1,36,34,33,-1,36,35,34,-1,36,29,35,-1]
Coordinate569 = x3d.Coordinate()

IndexedFaceSet568.coord = Coordinate569
TextureCoordinate570 = x3d.TextureCoordinate()

IndexedFaceSet568.texCoord = TextureCoordinate570

Shape564.geometry = IndexedFaceSet568

Transform563.children.append(Shape564)

HAnimSegment562.children.append(Transform563)

HAnimJoint561.children.append(HAnimSegment562)
HAnimJoint571 = x3d.HAnimJoint()
HAnimJoint571.name = "r_carpal_proximal_interphalangeal_2"
HAnimJoint571.DEF = "hanim_r_carpal_proximal_interphalangeal_2"
HAnimJoint571.center = [-8.45,26.1,0.6956]
HAnimJoint571.ulimit = [0,0,0]
HAnimJoint571.llimit = [0,0,0]
HAnimSegment572 = x3d.HAnimSegment()
HAnimSegment572.name = "r_carpal_middle_phalanx_2"
HAnimSegment572.DEF = "hanim_r_carpal_middle_phalanx_2"
Transform573 = x3d.Transform()
Transform573.translation = [-8.45,26.1,0.6956]
Shape574 = x3d.Shape()
Appearance575 = x3d.Appearance()
Material576 = x3d.Material()
Material576.diffuseColor = [0.588,0.588,0.588]

Appearance575.material = Material576
ImageTexture577 = x3d.ImageTexture()
ImageTexture577.USE = "JinLOA2TextureAtlas"

Appearance575.texture = ImageTexture577

Shape574.appearance = Appearance575
IndexedFaceSet578 = x3d.IndexedFaceSet()
IndexedFaceSet578.coordIndex = [0,2,3,-1,3,1,0,-1,0,4,5,-1,0,5,6,-1,6,2,0,-1,2,6,7,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,3,9,10,-1,10,1,3,-1,1,10,11,-1,1,11,4,-1,4,0,1,-1,4,12,13,-1,13,5,4,-1,5,13,14,-1,14,6,5,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,12,-1,12,4,11,-1,12,20,21,-1,21,13,12,-1,13,21,22,-1,22,14,13,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,20,-1,20,12,19,-1,28,21,20,-1,28,22,21,-1,28,23,22,-1,28,24,23,-1,28,25,24,-1,28,26,25,-1,28,27,26,-1,28,20,27,-1]
IndexedFaceSet578.creaseAngle = 3.14159
IndexedFaceSet578.texCoordIndex = [0,3,2,-1,2,1,0,-1,0,5,4,-1,0,4,6,-1,6,3,0,-1,3,6,7,-1,3,7,8,-1,8,2,3,-1,2,8,9,-1,2,9,10,-1,10,1,2,-1,1,10,11,-1,1,11,5,-1,5,0,1,-1,5,13,12,-1,12,4,5,-1,4,12,14,-1,14,6,4,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,13,-1,13,5,11,-1,13,21,20,-1,20,12,13,-1,12,20,22,-1,22,14,12,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,21,-1,21,13,19,-1,28,20,21,-1,28,22,20,-1,28,23,22,-1,28,24,23,-1,28,25,24,-1,28,26,25,-1,28,27,26,-1,28,21,27,-1]
Coordinate579 = x3d.Coordinate()

IndexedFaceSet578.coord = Coordinate579
TextureCoordinate580 = x3d.TextureCoordinate()

IndexedFaceSet578.texCoord = TextureCoordinate580

Shape574.geometry = IndexedFaceSet578

Transform573.children.append(Shape574)

HAnimSegment572.children.append(Transform573)

HAnimJoint571.children.append(HAnimSegment572)
HAnimJoint581 = x3d.HAnimJoint()
HAnimJoint581.name = "r_carpal_distal_interphalangeal_2"
HAnimJoint581.DEF = "hanim_r_carpal_distal_interphalangeal_2"
HAnimJoint581.center = [-8.192,25.17,0.7315]
HAnimJoint581.ulimit = [0,0,0]
HAnimJoint581.llimit = [0,0,0]
HAnimSegment582 = x3d.HAnimSegment()
HAnimSegment582.name = "r_carpal_distal_phalanx_2"
HAnimSegment582.DEF = "hanim_r_carpal_distal_phalanx_2"
Transform583 = x3d.Transform()
Transform583.translation = [-8.192,25.17,0.7315]
Shape584 = x3d.Shape()
Appearance585 = x3d.Appearance()
Material586 = x3d.Material()
Material586.diffuseColor = [0.588,0.588,0.588]

Appearance585.material = Material586
ImageTexture587 = x3d.ImageTexture()
ImageTexture587.USE = "JinLOA2TextureAtlas"

Appearance585.texture = ImageTexture587

Shape584.appearance = Appearance585
IndexedFaceSet588 = x3d.IndexedFaceSet()
IndexedFaceSet588.coordIndex = [0,2,3,-1,3,1,0,-1,0,4,5,-1,0,5,6,-1,6,2,0,-1,2,6,7,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,3,9,10,-1,10,1,3,-1,1,10,11,-1,1,11,4,-1,4,0,1,-1,4,12,13,-1,13,5,4,-1,5,13,14,-1,14,6,5,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,12,-1,12,4,11,-1,12,20,21,-1,21,13,12,-1,13,21,22,-1,22,14,13,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,20,-1,20,12,19,-1,28,21,20,-1,28,22,21,-1,28,23,22,-1,28,24,23,-1,28,25,24,-1,28,26,25,-1,28,27,26,-1,28,20,27,-1]
IndexedFaceSet588.creaseAngle = 3.14159
IndexedFaceSet588.texCoordIndex = [0,3,2,-1,2,1,0,-1,0,5,4,-1,0,4,6,-1,6,3,0,-1,3,6,7,-1,3,7,8,-1,8,2,3,-1,2,8,9,-1,2,9,10,-1,10,1,2,-1,1,10,11,-1,1,11,5,-1,5,0,1,-1,5,13,12,-1,12,4,5,-1,4,12,14,-1,14,6,4,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,13,-1,13,5,11,-1,13,21,20,-1,20,12,13,-1,12,20,22,-1,22,14,12,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,21,-1,21,13,19,-1,28,20,21,-1,28,22,20,-1,28,23,22,-1,28,24,23,-1,28,25,24,-1,28,26,25,-1,28,27,26,-1,28,21,27,-1]
Coordinate589 = x3d.Coordinate()

IndexedFaceSet588.coord = Coordinate589
TextureCoordinate590 = x3d.TextureCoordinate()

IndexedFaceSet588.texCoord = TextureCoordinate590

Shape584.geometry = IndexedFaceSet588

Transform583.children.append(Shape584)

HAnimSegment582.children.append(Transform583)

HAnimJoint581.children.append(HAnimSegment582)

HAnimJoint571.children.append(HAnimJoint581)

HAnimJoint561.children.append(HAnimJoint571)

HAnimJoint551.children.append(HAnimJoint561)

HAnimJoint511.children.append(HAnimJoint551)
HAnimJoint591 = x3d.HAnimJoint()
HAnimJoint591.name = "r_carpometacarpal_3"
HAnimJoint591.DEF = "hanim_r_carpometacarpal_3"
HAnimJoint591.center = [-8.344,28.65,-0.194]
HAnimJoint591.ulimit = [0,0,0]
HAnimJoint591.llimit = [0,0,0]
HAnimSegment592 = x3d.HAnimSegment()
HAnimSegment592.name = "r_metacarpal_3"
HAnimSegment592.DEF = "hanim_r_metacarpal_3"
Transform593 = x3d.Transform()
Transform593.translation = [-8.344,28.65,-0.194]
Shape594 = x3d.Shape()
Appearance595 = x3d.Appearance()
Material596 = x3d.Material()
Material596.diffuseColor = [0.588,0.588,0.588]

Appearance595.material = Material596
ImageTexture597 = x3d.ImageTexture()
ImageTexture597.USE = "JinLOA2TextureAtlas"

Appearance595.texture = ImageTexture597

Shape594.appearance = Appearance595
IndexedFaceSet598 = x3d.IndexedFaceSet()
IndexedFaceSet598.coordIndex = [0,2,3,-1,3,1,0,-1,0,4,5,-1,0,5,6,-1,6,2,0,-1,2,6,7,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,3,9,10,-1,10,1,3,-1,1,10,11,-1,1,11,4,-1,4,0,1,-1,4,12,13,-1,13,5,4,-1,5,13,14,-1,14,6,5,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,12,-1,12,4,11,-1,12,20,21,-1,21,13,12,-1,13,21,22,-1,22,14,13,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,20,-1,20,12,19,-1,20,28,29,-1,29,21,20,-1,21,29,30,-1,30,22,21,-1,22,30,31,-1,31,23,22,-1,23,31,32,-1,32,24,23,-1,24,32,33,-1,33,25,24,-1,25,33,34,-1,34,26,25,-1,26,34,35,-1,35,27,26,-1,27,35,28,-1,28,20,27,-1,36,29,28,-1,36,30,29,-1,36,31,30,-1,36,32,31,-1,36,33,32,-1,36,34,33,-1,36,35,34,-1,36,28,35,-1]
IndexedFaceSet598.creaseAngle = 3.14159
IndexedFaceSet598.texCoordIndex = [0,3,2,-1,2,1,0,-1,0,5,4,-1,0,4,6,-1,6,3,0,-1,3,6,7,-1,3,7,8,-1,8,2,3,-1,2,8,9,-1,2,9,10,-1,10,1,2,-1,1,10,11,-1,1,11,5,-1,5,0,1,-1,5,13,12,-1,12,4,5,-1,4,12,14,-1,14,6,4,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,13,-1,13,5,11,-1,13,21,20,-1,20,12,13,-1,12,20,22,-1,22,14,12,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,21,-1,21,13,19,-1,21,29,28,-1,28,20,21,-1,20,28,30,-1,30,22,20,-1,22,30,31,-1,31,23,22,-1,23,31,32,-1,32,24,23,-1,24,32,33,-1,33,25,24,-1,25,33,34,-1,34,26,25,-1,26,34,35,-1,35,27,26,-1,27,35,29,-1,29,21,27,-1,36,28,29,-1,36,30,28,-1,36,31,30,-1,36,32,31,-1,36,33,32,-1,36,34,33,-1,36,35,34,-1,36,29,35,-1]
Coordinate599 = x3d.Coordinate()

IndexedFaceSet598.coord = Coordinate599
TextureCoordinate600 = x3d.TextureCoordinate()

IndexedFaceSet598.texCoord = TextureCoordinate600

Shape594.geometry = IndexedFaceSet598

Transform593.children.append(Shape594)

HAnimSegment592.children.append(Transform593)

HAnimJoint591.children.append(HAnimSegment592)
HAnimJoint601 = x3d.HAnimJoint()
HAnimJoint601.name = "r_metacarpophalangeal_3"
HAnimJoint601.DEF = "hanim_r_metacarpophalangeal_3"
HAnimJoint601.center = [-8.52,27.26,-0.1959]
HAnimJoint601.ulimit = [0,0,0]
HAnimJoint601.llimit = [0,0,0]
HAnimSegment602 = x3d.HAnimSegment()
HAnimSegment602.name = "r_carpal_proximal_phalanx_3"
HAnimSegment602.DEF = "hanim_r_carpal_proximal_phalanx_3"
Transform603 = x3d.Transform()
Transform603.translation = [-8.52,27.26,-0.1959]
Shape604 = x3d.Shape()
Appearance605 = x3d.Appearance()
Material606 = x3d.Material()
Material606.diffuseColor = [0.588,0.588,0.588]

Appearance605.material = Material606
ImageTexture607 = x3d.ImageTexture()
ImageTexture607.USE = "JinLOA2TextureAtlas"

Appearance605.texture = ImageTexture607

Shape604.appearance = Appearance605
IndexedFaceSet608 = x3d.IndexedFaceSet()
IndexedFaceSet608.coordIndex = [0,2,3,-1,3,1,0,-1,0,4,5,-1,0,5,6,-1,6,2,0,-1,2,6,7,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,3,9,10,-1,10,1,3,-1,1,10,11,-1,1,11,4,-1,4,0,1,-1,4,12,13,-1,13,5,4,-1,5,13,14,-1,14,6,5,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,12,-1,12,4,11,-1,12,20,21,-1,21,13,12,-1,13,21,22,-1,22,14,13,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,20,-1,20,12,19,-1,20,28,29,-1,29,21,20,-1,21,29,30,-1,30,22,21,-1,22,30,31,-1,31,23,22,-1,23,31,32,-1,32,24,23,-1,24,32,33,-1,33,25,24,-1,25,33,34,-1,34,26,25,-1,26,34,35,-1,35,27,26,-1,27,35,28,-1,28,20,27,-1,36,29,28,-1,36,30,29,-1,36,31,30,-1,36,32,31,-1,36,33,32,-1,36,34,33,-1,36,35,34,-1,36,28,35,-1]
IndexedFaceSet608.creaseAngle = 3.14159
IndexedFaceSet608.texCoordIndex = [0,3,2,-1,2,1,0,-1,0,5,4,-1,0,4,6,-1,6,3,0,-1,3,6,7,-1,3,7,8,-1,8,2,3,-1,2,8,9,-1,2,9,10,-1,10,1,2,-1,1,10,11,-1,1,11,5,-1,5,0,1,-1,5,13,12,-1,12,4,5,-1,4,12,14,-1,14,6,4,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,13,-1,13,5,11,-1,13,21,20,-1,20,12,13,-1,12,20,22,-1,22,14,12,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,21,-1,21,13,19,-1,21,29,28,-1,28,20,21,-1,20,28,30,-1,30,22,20,-1,22,30,31,-1,31,23,22,-1,23,31,32,-1,32,24,23,-1,24,32,33,-1,33,25,24,-1,25,33,34,-1,34,26,25,-1,26,34,35,-1,35,27,26,-1,27,35,29,-1,29,21,27,-1,36,28,29,-1,36,30,28,-1,36,31,30,-1,36,32,31,-1,36,33,32,-1,36,34,33,-1,36,35,34,-1,36,29,35,-1]
Coordinate609 = x3d.Coordinate()

IndexedFaceSet608.coord = Coordinate609
TextureCoordinate610 = x3d.TextureCoordinate()

IndexedFaceSet608.texCoord = TextureCoordinate610

Shape604.geometry = IndexedFaceSet608

Transform603.children.append(Shape604)

HAnimSegment602.children.append(Transform603)

HAnimJoint601.children.append(HAnimSegment602)
HAnimJoint611 = x3d.HAnimJoint()
HAnimJoint611.name = "r_carpal_proximal_interphalangeal_3"
HAnimJoint611.DEF = "hanim_r_carpal_proximal_interphalangeal_3"
HAnimJoint611.center = [-8.477,26.07,-0.2214]
HAnimJoint611.ulimit = [0,0,0]
HAnimJoint611.llimit = [0,0,0]
HAnimSegment612 = x3d.HAnimSegment()
HAnimSegment612.name = "r_carpal_middle_phalanx_3"
HAnimSegment612.DEF = "hanim_r_carpal_middle_phalanx_3"
Transform613 = x3d.Transform()
Transform613.translation = [-8.477,26.07,-0.2214]
Shape614 = x3d.Shape()
Appearance615 = x3d.Appearance()
Material616 = x3d.Material()
Material616.diffuseColor = [0.588,0.588,0.588]

Appearance615.material = Material616
ImageTexture617 = x3d.ImageTexture()
ImageTexture617.USE = "JinLOA2TextureAtlas"

Appearance615.texture = ImageTexture617

Shape614.appearance = Appearance615
IndexedFaceSet618 = x3d.IndexedFaceSet()
IndexedFaceSet618.coordIndex = [0,2,3,-1,3,1,0,-1,0,4,5,-1,0,5,6,-1,6,2,0,-1,2,6,7,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,3,9,10,-1,10,1,3,-1,1,10,11,-1,1,11,4,-1,4,0,1,-1,4,12,13,-1,13,5,4,-1,5,13,14,-1,14,6,5,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,12,-1,12,4,11,-1,12,20,21,-1,21,13,12,-1,13,21,22,-1,22,14,13,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,20,-1,20,12,19,-1,28,21,20,-1,28,22,21,-1,28,23,22,-1,28,24,23,-1,28,25,24,-1,28,26,25,-1,28,27,26,-1,28,20,27,-1]
IndexedFaceSet618.creaseAngle = 3.14159
IndexedFaceSet618.texCoordIndex = [0,3,2,-1,2,1,0,-1,0,5,4,-1,0,4,6,-1,6,3,0,-1,3,6,7,-1,3,7,8,-1,8,2,3,-1,2,8,9,-1,2,9,10,-1,10,1,2,-1,1,10,11,-1,1,11,5,-1,5,0,1,-1,5,13,12,-1,12,4,5,-1,4,12,14,-1,14,6,4,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,13,-1,13,5,11,-1,13,21,20,-1,20,12,13,-1,12,20,22,-1,22,14,12,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,21,-1,21,13,19,-1,28,20,21,-1,28,22,20,-1,28,23,22,-1,28,24,23,-1,28,25,24,-1,28,26,25,-1,28,27,26,-1,28,21,27,-1]
Coordinate619 = x3d.Coordinate()

IndexedFaceSet618.coord = Coordinate619
TextureCoordinate620 = x3d.TextureCoordinate()

IndexedFaceSet618.texCoord = TextureCoordinate620

Shape614.geometry = IndexedFaceSet618

Transform613.children.append(Shape614)

HAnimSegment612.children.append(Transform613)

HAnimJoint611.children.append(HAnimSegment612)
HAnimJoint621 = x3d.HAnimJoint()
HAnimJoint621.name = "r_carpal_distal_interphalangeal_3"
HAnimJoint621.DEF = "hanim_r_carpal_distal_interphalangeal_3"
HAnimJoint621.center = [-8.25,25.030001,-0.2187]
HAnimJoint621.ulimit = [0,0,0]
HAnimJoint621.llimit = [0,0,0]
HAnimSegment622 = x3d.HAnimSegment()
HAnimSegment622.name = "r_carpal_distal_phalanx_3"
HAnimSegment622.DEF = "hanim_r_carpal_distal_phalanx_3"
Transform623 = x3d.Transform()
Transform623.translation = [-8.25,25.030001,-0.2187]
Shape624 = x3d.Shape()
Appearance625 = x3d.Appearance()
Material626 = x3d.Material()
Material626.diffuseColor = [0.588,0.588,0.588]

Appearance625.material = Material626
ImageTexture627 = x3d.ImageTexture()
ImageTexture627.USE = "JinLOA2TextureAtlas"

Appearance625.texture = ImageTexture627

Shape624.appearance = Appearance625
IndexedFaceSet628 = x3d.IndexedFaceSet()
IndexedFaceSet628.coordIndex = [0,2,3,-1,3,1,0,-1,0,4,5,-1,0,5,6,-1,6,2,0,-1,2,6,7,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,3,9,10,-1,10,1,3,-1,1,10,11,-1,1,11,4,-1,4,0,1,-1,4,12,13,-1,13,5,4,-1,5,13,14,-1,14,6,5,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,12,-1,12,4,11,-1,12,20,21,-1,21,13,12,-1,13,21,22,-1,22,14,13,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,20,-1,20,12,19,-1,28,21,20,-1,28,22,21,-1,28,23,22,-1,28,24,23,-1,28,25,24,-1,28,26,25,-1,28,27,26,-1,28,20,27,-1]
IndexedFaceSet628.creaseAngle = 3.14159
IndexedFaceSet628.texCoordIndex = [0,3,2,-1,2,1,0,-1,0,5,4,-1,0,4,6,-1,6,3,0,-1,3,6,7,-1,3,7,8,-1,8,2,3,-1,2,8,9,-1,2,9,10,-1,10,1,2,-1,1,10,11,-1,1,11,5,-1,5,0,1,-1,5,13,12,-1,12,4,5,-1,4,12,14,-1,14,6,4,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,13,-1,13,5,11,-1,13,21,20,-1,20,12,13,-1,12,20,22,-1,22,14,12,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,21,-1,21,13,19,-1,28,20,21,-1,28,22,20,-1,28,23,22,-1,28,24,23,-1,28,25,24,-1,28,26,25,-1,28,27,26,-1,28,21,27,-1]
Coordinate629 = x3d.Coordinate()

IndexedFaceSet628.coord = Coordinate629
TextureCoordinate630 = x3d.TextureCoordinate()

IndexedFaceSet628.texCoord = TextureCoordinate630

Shape624.geometry = IndexedFaceSet628

Transform623.children.append(Shape624)

HAnimSegment622.children.append(Transform623)

HAnimJoint621.children.append(HAnimSegment622)

HAnimJoint611.children.append(HAnimJoint621)

HAnimJoint601.children.append(HAnimJoint611)

HAnimJoint591.children.append(HAnimJoint601)

HAnimJoint511.children.append(HAnimJoint591)
HAnimJoint631 = x3d.HAnimJoint()
HAnimJoint631.name = "r_carpometacarpal_4"
HAnimJoint631.DEF = "hanim_r_carpometacarpal_4"
HAnimJoint631.center = [-8.339,28.57,-0.9243]
HAnimJoint631.ulimit = [0,0,0]
HAnimJoint631.llimit = [0,0,0]
HAnimSegment632 = x3d.HAnimSegment()
HAnimSegment632.name = "r_metacarpal_4"
HAnimSegment632.DEF = "hanim_r_metacarpal_4"
Transform633 = x3d.Transform()
Transform633.translation = [-8.339,28.57,-0.9243]
Shape634 = x3d.Shape()
Appearance635 = x3d.Appearance()
Material636 = x3d.Material()
Material636.diffuseColor = [0.588,0.588,0.588]

Appearance635.material = Material636
ImageTexture637 = x3d.ImageTexture()
ImageTexture637.USE = "JinLOA2TextureAtlas"

Appearance635.texture = ImageTexture637

Shape634.appearance = Appearance635
IndexedFaceSet638 = x3d.IndexedFaceSet()
IndexedFaceSet638.coordIndex = [0,2,3,-1,3,1,0,-1,0,4,5,-1,0,5,6,-1,6,2,0,-1,2,6,7,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,3,9,10,-1,10,1,3,-1,1,10,11,-1,1,11,4,-1,4,0,1,-1,4,12,13,-1,13,5,4,-1,5,13,14,-1,14,6,5,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,12,-1,12,4,11,-1,12,20,21,-1,21,13,12,-1,13,21,22,-1,22,14,13,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,20,-1,20,12,19,-1,20,28,29,-1,29,21,20,-1,21,29,30,-1,30,22,21,-1,22,30,31,-1,31,23,22,-1,23,31,32,-1,32,24,23,-1,24,32,33,-1,33,25,24,-1,25,33,34,-1,34,26,25,-1,26,34,35,-1,35,27,26,-1,27,35,28,-1,28,20,27,-1,36,29,28,-1,36,30,29,-1,36,31,30,-1,36,32,31,-1,36,33,32,-1,36,34,33,-1,36,35,34,-1,36,28,35,-1]
IndexedFaceSet638.creaseAngle = 3.14159
IndexedFaceSet638.texCoordIndex = [0,3,2,-1,2,1,0,-1,0,5,4,-1,0,4,6,-1,6,3,0,-1,3,6,7,-1,3,7,8,-1,8,2,3,-1,2,8,9,-1,2,9,10,-1,10,1,2,-1,1,10,11,-1,1,11,5,-1,5,0,1,-1,5,13,12,-1,12,4,5,-1,4,12,14,-1,14,6,4,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,13,-1,13,5,11,-1,13,21,20,-1,20,12,13,-1,12,20,22,-1,22,14,12,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,21,-1,21,13,19,-1,21,29,28,-1,28,20,21,-1,20,28,30,-1,30,22,20,-1,22,30,31,-1,31,23,22,-1,23,31,32,-1,32,24,23,-1,24,32,33,-1,33,25,24,-1,25,33,34,-1,34,26,25,-1,26,34,35,-1,35,27,26,-1,27,35,29,-1,29,21,27,-1,36,28,29,-1,36,30,28,-1,36,31,30,-1,36,32,31,-1,36,33,32,-1,36,34,33,-1,36,35,34,-1,36,29,35,-1]
Coordinate639 = x3d.Coordinate()

IndexedFaceSet638.coord = Coordinate639
TextureCoordinate640 = x3d.TextureCoordinate()

IndexedFaceSet638.texCoord = TextureCoordinate640

Shape634.geometry = IndexedFaceSet638

Transform633.children.append(Shape634)

HAnimSegment632.children.append(Transform633)

HAnimJoint631.children.append(HAnimSegment632)
HAnimJoint641 = x3d.HAnimJoint()
HAnimJoint641.name = "r_metacarpophalangeal_4"
HAnimJoint641.DEF = "hanim_r_metacarpophalangeal_4"
HAnimJoint641.center = [-8.428,27.299999,-0.9985]
HAnimJoint641.ulimit = [0,0,0]
HAnimJoint641.llimit = [0,0,0]
HAnimSegment642 = x3d.HAnimSegment()
HAnimSegment642.name = "r_carpal_proximal_phalanx_4"
HAnimSegment642.DEF = "hanim_r_carpal_proximal_phalanx_4"
Transform643 = x3d.Transform()
Transform643.translation = [-8.428,27.299999,-0.9985]
Shape644 = x3d.Shape()
Appearance645 = x3d.Appearance()
Material646 = x3d.Material()
Material646.diffuseColor = [0.588,0.588,0.588]

Appearance645.material = Material646
ImageTexture647 = x3d.ImageTexture()
ImageTexture647.USE = "JinLOA2TextureAtlas"

Appearance645.texture = ImageTexture647

Shape644.appearance = Appearance645
IndexedFaceSet648 = x3d.IndexedFaceSet()
IndexedFaceSet648.coordIndex = [0,2,3,-1,3,1,0,-1,0,4,5,-1,0,5,6,-1,6,2,0,-1,2,6,7,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,3,9,10,-1,10,1,3,-1,1,10,11,-1,1,11,4,-1,4,0,1,-1,4,12,13,-1,13,5,4,-1,5,13,14,-1,14,6,5,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,12,-1,12,4,11,-1,12,20,21,-1,21,13,12,-1,13,21,22,-1,22,14,13,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,20,-1,20,12,19,-1,20,28,29,-1,29,21,20,-1,21,29,30,-1,30,22,21,-1,22,30,31,-1,31,23,22,-1,23,31,32,-1,32,24,23,-1,24,32,33,-1,33,25,24,-1,25,33,34,-1,34,26,25,-1,26,34,35,-1,35,27,26,-1,27,35,28,-1,28,20,27,-1,36,29,28,-1,36,30,29,-1,36,31,30,-1,36,32,31,-1,36,33,32,-1,36,34,33,-1,36,35,34,-1,36,28,35,-1]
IndexedFaceSet648.creaseAngle = 3.14159
IndexedFaceSet648.texCoordIndex = [0,3,2,-1,2,1,0,-1,0,5,4,-1,0,4,6,-1,6,3,0,-1,3,6,7,-1,3,7,8,-1,8,2,3,-1,2,8,9,-1,2,9,10,-1,10,1,2,-1,1,10,11,-1,1,11,5,-1,5,0,1,-1,5,13,12,-1,12,4,5,-1,4,12,14,-1,14,6,4,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,13,-1,13,5,11,-1,13,21,20,-1,20,12,13,-1,12,20,22,-1,22,14,12,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,21,-1,21,13,19,-1,21,29,28,-1,28,20,21,-1,20,28,30,-1,30,22,20,-1,22,30,31,-1,31,23,22,-1,23,31,32,-1,32,24,23,-1,24,32,33,-1,33,25,24,-1,25,33,34,-1,34,26,25,-1,26,34,35,-1,35,27,26,-1,27,35,29,-1,29,21,27,-1,36,28,29,-1,36,30,28,-1,36,31,30,-1,36,32,31,-1,36,33,32,-1,36,34,33,-1,36,35,34,-1,36,29,35,-1]
Coordinate649 = x3d.Coordinate()

IndexedFaceSet648.coord = Coordinate649
TextureCoordinate650 = x3d.TextureCoordinate()

IndexedFaceSet648.texCoord = TextureCoordinate650

Shape644.geometry = IndexedFaceSet648

Transform643.children.append(Shape644)

HAnimSegment642.children.append(Transform643)

HAnimJoint641.children.append(HAnimSegment642)
HAnimJoint651 = x3d.HAnimJoint()
HAnimJoint651.name = "r_carpal_proximal_interphalangeal_4"
HAnimJoint651.DEF = "hanim_r_carpal_proximal_interphalangeal_4"
HAnimJoint651.center = [-8.428,26.290001,-1.034]
HAnimJoint651.ulimit = [0,0,0]
HAnimJoint651.llimit = [0,0,0]
HAnimSegment652 = x3d.HAnimSegment()
HAnimSegment652.name = "r_carpal_middle_phalanx_4"
HAnimSegment652.DEF = "hanim_r_carpal_middle_phalanx_4"
Transform653 = x3d.Transform()
Transform653.translation = [-8.428,26.290001,-1.034]
Shape654 = x3d.Shape()
Appearance655 = x3d.Appearance()
Material656 = x3d.Material()
Material656.diffuseColor = [0.588,0.588,0.588]

Appearance655.material = Material656
ImageTexture657 = x3d.ImageTexture()
ImageTexture657.USE = "JinLOA2TextureAtlas"

Appearance655.texture = ImageTexture657

Shape654.appearance = Appearance655
IndexedFaceSet658 = x3d.IndexedFaceSet()
IndexedFaceSet658.coordIndex = [0,2,3,-1,3,1,0,-1,0,4,5,-1,0,5,6,-1,6,2,0,-1,2,6,7,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,3,9,10,-1,10,1,3,-1,1,10,11,-1,1,11,4,-1,4,0,1,-1,4,12,13,-1,13,5,4,-1,5,13,14,-1,14,6,5,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,12,-1,12,4,11,-1,12,20,21,-1,21,13,12,-1,13,21,22,-1,22,14,13,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,20,-1,20,12,19,-1,28,21,20,-1,28,22,21,-1,28,23,22,-1,28,24,23,-1,28,25,24,-1,28,26,25,-1,28,27,26,-1,28,20,27,-1]
IndexedFaceSet658.creaseAngle = 3.14159
IndexedFaceSet658.texCoordIndex = [0,3,2,-1,2,1,0,-1,0,5,4,-1,0,4,6,-1,6,3,0,-1,3,6,7,-1,3,7,8,-1,8,2,3,-1,2,8,9,-1,2,9,10,-1,10,1,2,-1,1,10,11,-1,1,11,5,-1,5,0,1,-1,5,13,12,-1,12,4,5,-1,4,12,14,-1,14,6,4,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,13,-1,13,5,11,-1,13,21,20,-1,20,12,13,-1,12,20,22,-1,22,14,12,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,21,-1,21,13,19,-1,28,20,21,-1,28,22,20,-1,28,23,22,-1,28,24,23,-1,28,25,24,-1,28,26,25,-1,28,27,26,-1,28,21,27,-1]
Coordinate659 = x3d.Coordinate()

IndexedFaceSet658.coord = Coordinate659
TextureCoordinate660 = x3d.TextureCoordinate()

IndexedFaceSet658.texCoord = TextureCoordinate660

Shape654.geometry = IndexedFaceSet658

Transform653.children.append(Shape654)

HAnimSegment652.children.append(Transform653)

HAnimJoint651.children.append(HAnimSegment652)
HAnimJoint661 = x3d.HAnimJoint()
HAnimJoint661.name = "r_carpal_distal_interphalangeal_4"
HAnimJoint661.DEF = "hanim_r_carpal_distal_interphalangeal_4"
HAnimJoint661.center = [-8.192,25.309999,-1.124]
HAnimJoint661.ulimit = [0,0,0]
HAnimJoint661.llimit = [0,0,0]
HAnimSegment662 = x3d.HAnimSegment()
HAnimSegment662.name = "r_carpal_distal_phalanx_4"
HAnimSegment662.DEF = "hanim_r_carpal_distal_phalanx_4"
Transform663 = x3d.Transform()
Transform663.translation = [-8.192,25.309999,-1.124]
Shape664 = x3d.Shape()
Appearance665 = x3d.Appearance()
Material666 = x3d.Material()
Material666.diffuseColor = [0.588,0.588,0.588]

Appearance665.material = Material666
ImageTexture667 = x3d.ImageTexture()
ImageTexture667.USE = "JinLOA2TextureAtlas"

Appearance665.texture = ImageTexture667

Shape664.appearance = Appearance665
IndexedFaceSet668 = x3d.IndexedFaceSet()
IndexedFaceSet668.coordIndex = [0,2,3,-1,3,1,0,-1,0,4,5,-1,0,5,6,-1,6,2,0,-1,2,6,7,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,3,9,10,-1,10,1,3,-1,1,10,11,-1,1,11,4,-1,4,0,1,-1,4,12,13,-1,13,5,4,-1,5,13,14,-1,14,6,5,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,12,-1,12,4,11,-1,12,20,21,-1,21,13,12,-1,13,21,22,-1,22,14,13,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,20,-1,20,12,19,-1,28,21,20,-1,28,22,21,-1,28,23,22,-1,28,24,23,-1,28,25,24,-1,28,26,25,-1,28,27,26,-1,28,20,27,-1]
IndexedFaceSet668.creaseAngle = 3.14159
IndexedFaceSet668.texCoordIndex = [0,3,2,-1,2,1,0,-1,0,5,4,-1,0,4,6,-1,6,3,0,-1,3,6,7,-1,3,7,8,-1,8,2,3,-1,2,8,9,-1,2,9,10,-1,10,1,2,-1,1,10,11,-1,1,11,5,-1,5,0,1,-1,5,13,12,-1,12,4,5,-1,4,12,14,-1,14,6,4,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,13,-1,13,5,11,-1,13,21,20,-1,20,12,13,-1,12,20,22,-1,22,14,12,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,21,-1,21,13,19,-1,28,20,21,-1,28,22,20,-1,28,23,22,-1,28,24,23,-1,28,25,24,-1,28,26,25,-1,28,27,26,-1,28,21,27,-1]
Coordinate669 = x3d.Coordinate()

IndexedFaceSet668.coord = Coordinate669
TextureCoordinate670 = x3d.TextureCoordinate()

IndexedFaceSet668.texCoord = TextureCoordinate670

Shape664.geometry = IndexedFaceSet668

Transform663.children.append(Shape664)

HAnimSegment662.children.append(Transform663)

HAnimJoint661.children.append(HAnimSegment662)

HAnimJoint651.children.append(HAnimJoint661)

HAnimJoint641.children.append(HAnimJoint651)

HAnimJoint631.children.append(HAnimJoint641)

HAnimJoint511.children.append(HAnimJoint631)
HAnimJoint671 = x3d.HAnimJoint()
HAnimJoint671.name = "r_carpometacarpal_5"
HAnimJoint671.DEF = "hanim_r_carpometacarpal_5"
HAnimJoint671.center = [-8.197,28.370001,-1.528]
HAnimJoint671.ulimit = [0,0,0]
HAnimJoint671.llimit = [0,0,0]
HAnimSegment672 = x3d.HAnimSegment()
HAnimSegment672.name = "r_metacarpal_5"
HAnimSegment672.DEF = "hanim_r_metacarpal_5"
Transform673 = x3d.Transform()
Transform673.translation = [-8.197,28.370001,-1.528]
Shape674 = x3d.Shape()
Appearance675 = x3d.Appearance()
Material676 = x3d.Material()
Material676.diffuseColor = [0.588,0.588,0.588]

Appearance675.material = Material676
ImageTexture677 = x3d.ImageTexture()
ImageTexture677.USE = "JinLOA2TextureAtlas"

Appearance675.texture = ImageTexture677

Shape674.appearance = Appearance675
IndexedFaceSet678 = x3d.IndexedFaceSet()
IndexedFaceSet678.coordIndex = [0,2,3,-1,3,1,0,-1,0,4,5,-1,0,5,6,-1,6,2,0,-1,2,6,7,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,3,9,10,-1,10,1,3,-1,1,10,11,-1,1,11,4,-1,4,0,1,-1,4,12,13,-1,13,5,4,-1,5,13,14,-1,14,6,5,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,12,-1,12,4,11,-1,12,20,21,-1,21,13,12,-1,13,21,22,-1,22,14,13,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,20,-1,20,12,19,-1,20,28,29,-1,29,21,20,-1,21,29,30,-1,30,22,21,-1,22,30,31,-1,31,23,22,-1,23,31,32,-1,32,24,23,-1,24,32,33,-1,33,25,24,-1,25,33,34,-1,34,26,25,-1,26,34,35,-1,35,27,26,-1,27,35,28,-1,28,20,27,-1,36,29,28,-1,36,30,29,-1,36,31,30,-1,36,32,31,-1,36,33,32,-1,36,34,33,-1,36,35,34,-1,36,28,35,-1]
IndexedFaceSet678.creaseAngle = 3.14159
IndexedFaceSet678.texCoordIndex = [0,3,2,-1,2,1,0,-1,0,5,4,-1,0,4,6,-1,6,3,0,-1,3,6,7,-1,3,7,8,-1,8,2,3,-1,2,8,9,-1,2,9,10,-1,10,1,2,-1,1,10,11,-1,1,11,5,-1,5,0,1,-1,5,13,12,-1,12,4,5,-1,4,12,14,-1,14,6,4,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,13,-1,13,5,11,-1,13,21,20,-1,20,12,13,-1,12,20,22,-1,22,14,12,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,21,-1,21,13,19,-1,21,29,28,-1,28,20,21,-1,20,28,30,-1,30,22,20,-1,22,30,31,-1,31,23,22,-1,23,31,32,-1,32,24,23,-1,24,32,33,-1,33,25,24,-1,25,33,34,-1,34,26,25,-1,26,34,35,-1,35,27,26,-1,27,35,29,-1,29,21,27,-1,36,28,29,-1,36,30,28,-1,36,31,30,-1,36,32,31,-1,36,33,32,-1,36,34,33,-1,36,35,34,-1,36,29,35,-1]
Coordinate679 = x3d.Coordinate()

IndexedFaceSet678.coord = Coordinate679
TextureCoordinate680 = x3d.TextureCoordinate()

IndexedFaceSet678.texCoord = TextureCoordinate680

Shape674.geometry = IndexedFaceSet678

Transform673.children.append(Shape674)

HAnimSegment672.children.append(Transform673)

HAnimJoint671.children.append(HAnimSegment672)
HAnimJoint681 = x3d.HAnimJoint()
HAnimJoint681.name = "r_metacarpophalangeal_5"
HAnimJoint681.DEF = "hanim_r_metacarpophalangeal_5"
HAnimJoint681.center = [-8.334,27.5,-1.701]
HAnimJoint681.ulimit = [0,0,0]
HAnimJoint681.llimit = [0,0,0]
HAnimSegment682 = x3d.HAnimSegment()
HAnimSegment682.name = "r_carpal_proximal_phalanx_5"
HAnimSegment682.DEF = "hanim_r_carpal_proximal_phalanx_5"
Transform683 = x3d.Transform()
Transform683.translation = [-8.334,27.5,-1.701]
Shape684 = x3d.Shape()
Appearance685 = x3d.Appearance()
Material686 = x3d.Material()
Material686.diffuseColor = [0.588,0.588,0.588]

Appearance685.material = Material686
ImageTexture687 = x3d.ImageTexture()
ImageTexture687.USE = "JinLOA2TextureAtlas"

Appearance685.texture = ImageTexture687

Shape684.appearance = Appearance685
IndexedFaceSet688 = x3d.IndexedFaceSet()
IndexedFaceSet688.coordIndex = [0,2,3,-1,3,1,0,-1,0,4,5,-1,0,5,6,-1,6,2,0,-1,2,6,7,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,3,9,10,-1,10,1,3,-1,1,10,11,-1,1,11,4,-1,4,0,1,-1,4,12,13,-1,13,5,4,-1,5,13,14,-1,14,6,5,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,12,-1,12,4,11,-1,12,20,21,-1,21,13,12,-1,13,21,22,-1,22,14,13,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,20,-1,20,12,19,-1,20,28,29,-1,29,21,20,-1,21,29,30,-1,30,22,21,-1,22,30,31,-1,31,23,22,-1,23,31,32,-1,32,24,23,-1,24,32,33,-1,33,25,24,-1,25,33,34,-1,34,26,25,-1,26,34,35,-1,35,27,26,-1,27,35,28,-1,28,20,27,-1,36,29,28,-1,36,30,29,-1,36,31,30,-1,36,32,31,-1,36,33,32,-1,36,34,33,-1,36,35,34,-1,36,28,35,-1]
IndexedFaceSet688.creaseAngle = 3.14159
IndexedFaceSet688.texCoordIndex = [0,3,2,-1,2,1,0,-1,0,5,4,-1,0,4,6,-1,6,3,0,-1,3,6,7,-1,3,7,8,-1,8,2,3,-1,2,8,9,-1,2,9,10,-1,10,1,2,-1,1,10,11,-1,1,11,5,-1,5,0,1,-1,5,13,12,-1,12,4,5,-1,4,12,14,-1,14,6,4,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,13,-1,13,5,11,-1,13,21,20,-1,20,12,13,-1,12,20,22,-1,22,14,12,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,21,-1,21,13,19,-1,21,29,28,-1,28,20,21,-1,20,28,30,-1,30,22,20,-1,22,30,31,-1,31,23,22,-1,23,31,32,-1,32,24,23,-1,24,32,33,-1,33,25,24,-1,25,33,34,-1,34,26,25,-1,26,34,35,-1,35,27,26,-1,27,35,29,-1,29,21,27,-1,36,28,29,-1,36,30,28,-1,36,31,30,-1,36,32,31,-1,36,33,32,-1,36,34,33,-1,36,35,34,-1,36,29,35,-1]
Coordinate689 = x3d.Coordinate()

IndexedFaceSet688.coord = Coordinate689
TextureCoordinate690 = x3d.TextureCoordinate()

IndexedFaceSet688.texCoord = TextureCoordinate690

Shape684.geometry = IndexedFaceSet688

Transform683.children.append(Shape684)

HAnimSegment682.children.append(Transform683)

HAnimJoint681.children.append(HAnimSegment682)
HAnimJoint691 = x3d.HAnimJoint()
HAnimJoint691.name = "r_carpal_proximal_interphalangeal_5"
HAnimJoint691.DEF = "hanim_r_carpal_proximal_interphalangeal_5"
HAnimJoint691.center = [-8.338,26.780001,-1.768]
HAnimJoint691.ulimit = [0,0,0]
HAnimJoint691.llimit = [0,0,0]
HAnimSegment692 = x3d.HAnimSegment()
HAnimSegment692.name = "r_carpal_middle_phalanx_5"
HAnimSegment692.DEF = "hanim_r_carpal_middle_phalanx_5"
Transform693 = x3d.Transform()
Transform693.translation = [-8.338,26.780001,-1.768]
Shape694 = x3d.Shape()
Appearance695 = x3d.Appearance()
Material696 = x3d.Material()
Material696.diffuseColor = [0.588,0.588,0.588]

Appearance695.material = Material696
ImageTexture697 = x3d.ImageTexture()
ImageTexture697.USE = "JinLOA2TextureAtlas"

Appearance695.texture = ImageTexture697

Shape694.appearance = Appearance695
IndexedFaceSet698 = x3d.IndexedFaceSet()
IndexedFaceSet698.coordIndex = [0,2,3,-1,3,1,0,-1,0,4,5,-1,0,5,6,-1,6,2,0,-1,2,6,7,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,3,9,10,-1,10,1,3,-1,1,10,11,-1,1,11,4,-1,4,0,1,-1,4,12,13,-1,13,5,4,-1,5,13,14,-1,14,6,5,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,12,-1,12,4,11,-1,12,20,21,-1,21,13,12,-1,13,21,22,-1,22,14,13,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,20,-1,20,12,19,-1,28,21,20,-1,28,22,21,-1,28,23,22,-1,28,24,23,-1,28,25,24,-1,28,26,25,-1,28,27,26,-1,28,20,27,-1]
IndexedFaceSet698.creaseAngle = 3.14159
IndexedFaceSet698.texCoordIndex = [0,3,2,-1,2,1,0,-1,0,5,4,-1,0,4,6,-1,6,3,0,-1,3,6,7,-1,3,7,8,-1,8,2,3,-1,2,8,9,-1,2,9,10,-1,10,1,2,-1,1,10,11,-1,1,11,5,-1,5,0,1,-1,5,13,12,-1,12,4,5,-1,4,12,14,-1,14,6,4,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,13,-1,13,5,11,-1,13,21,20,-1,20,12,13,-1,12,20,22,-1,22,14,12,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,21,-1,21,13,19,-1,28,20,21,-1,28,22,20,-1,28,23,22,-1,28,24,23,-1,28,25,24,-1,28,26,25,-1,28,27,26,-1,28,21,27,-1]
Coordinate699 = x3d.Coordinate()

IndexedFaceSet698.coord = Coordinate699
TextureCoordinate700 = x3d.TextureCoordinate()

IndexedFaceSet698.texCoord = TextureCoordinate700

Shape694.geometry = IndexedFaceSet698

Transform693.children.append(Shape694)

HAnimSegment692.children.append(Transform693)

HAnimJoint691.children.append(HAnimSegment692)
HAnimJoint701 = x3d.HAnimJoint()
HAnimJoint701.name = "r_carpal_distal_interphalangeal_5"
HAnimJoint701.DEF = "hanim_r_carpal_distal_interphalangeal_5"
HAnimJoint701.center = [-8.153,26.040001,-1.886]
HAnimJoint701.ulimit = [0,0,0]
HAnimJoint701.llimit = [0,0,0]
HAnimSegment702 = x3d.HAnimSegment()
HAnimSegment702.name = "r_carpal_distal_phalanx_5"
HAnimSegment702.DEF = "hanim_r_carpal_distal_phalanx_5"
Transform703 = x3d.Transform()
Transform703.translation = [-8.153,26.040001,-1.886]
Shape704 = x3d.Shape()
Appearance705 = x3d.Appearance()
Material706 = x3d.Material()
Material706.diffuseColor = [0.588,0.588,0.588]

Appearance705.material = Material706
ImageTexture707 = x3d.ImageTexture()
ImageTexture707.USE = "JinLOA2TextureAtlas"

Appearance705.texture = ImageTexture707

Shape704.appearance = Appearance705
IndexedFaceSet708 = x3d.IndexedFaceSet()
IndexedFaceSet708.coordIndex = [0,2,3,-1,3,1,0,-1,0,4,5,-1,0,5,6,-1,6,2,0,-1,2,6,7,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,3,9,10,-1,10,1,3,-1,1,10,11,-1,1,11,4,-1,4,0,1,-1,4,12,13,-1,13,5,4,-1,5,13,14,-1,14,6,5,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,12,-1,12,4,11,-1,12,20,21,-1,21,13,12,-1,13,21,22,-1,22,14,13,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,20,-1,20,12,19,-1,28,21,20,-1,28,22,21,-1,28,23,22,-1,28,24,23,-1,28,25,24,-1,28,26,25,-1,28,27,26,-1,28,20,27,-1]
IndexedFaceSet708.creaseAngle = 3.14159
IndexedFaceSet708.texCoordIndex = [0,3,2,-1,2,1,0,-1,0,5,4,-1,0,4,6,-1,6,3,0,-1,3,6,7,-1,3,7,8,-1,8,2,3,-1,2,8,9,-1,2,9,10,-1,10,1,2,-1,1,10,11,-1,1,11,5,-1,5,0,1,-1,5,13,12,-1,12,4,5,-1,4,12,14,-1,14,6,4,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,13,-1,13,5,11,-1,13,21,20,-1,20,12,13,-1,12,20,22,-1,22,14,12,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,21,-1,21,13,19,-1,28,20,21,-1,28,22,20,-1,28,23,22,-1,28,24,23,-1,28,25,24,-1,28,26,25,-1,28,27,26,-1,28,21,27,-1]
Coordinate709 = x3d.Coordinate()

IndexedFaceSet708.coord = Coordinate709
TextureCoordinate710 = x3d.TextureCoordinate()

IndexedFaceSet708.texCoord = TextureCoordinate710

Shape704.geometry = IndexedFaceSet708

Transform703.children.append(Shape704)

HAnimSegment702.children.append(Transform703)

HAnimJoint701.children.append(HAnimSegment702)

HAnimJoint691.children.append(HAnimJoint701)

HAnimJoint681.children.append(HAnimJoint691)

HAnimJoint671.children.append(HAnimJoint681)

HAnimJoint511.children.append(HAnimJoint671)

HAnimJoint501.children.append(HAnimJoint511)

HAnimJoint491.children.append(HAnimJoint501)

HAnimJoint481.children.append(HAnimJoint491)

HAnimJoint471.children.append(HAnimJoint481)

HAnimJoint221.children.append(HAnimJoint471)
HAnimJoint711 = x3d.HAnimJoint()
HAnimJoint711.name = "vc4"
HAnimJoint711.DEF = "hanim_vc4"
HAnimJoint711.center = [0,54.419998,-0.6695]
HAnimJoint711.ulimit = [0,0,0]
HAnimJoint711.llimit = [0,0,0]
HAnimSegment712 = x3d.HAnimSegment()
HAnimSegment712.name = "c4"
HAnimSegment712.DEF = "hanim_c4"
Transform713 = x3d.Transform()
Transform713.translation = [0,54.419998,-0.6695]
Shape714 = x3d.Shape()
Appearance715 = x3d.Appearance()
Material716 = x3d.Material()
Material716.diffuseColor = [0.588,0.588,0.588]

Appearance715.material = Material716
ImageTexture717 = x3d.ImageTexture()
ImageTexture717.USE = "JinLOA2TextureAtlas"

Appearance715.texture = ImageTexture717

Shape714.appearance = Appearance715
IndexedFaceSet718 = x3d.IndexedFaceSet()
IndexedFaceSet718.coordIndex = [1,12,13,-1,13,0,1,-1,2,0,13,-1,13,14,2,-1,2,14,15,-1,15,3,2,-1,3,15,16,-1,16,4,3,-1,6,17,18,-1,18,5,6,-1,4,16,17,-1,17,6,4,-1,19,12,1,-1,1,7,19,-1,8,20,19,-1,19,7,8,-1,21,20,8,-1,8,9,21,-1,22,21,9,-1,9,10,22,-1,18,23,11,-1,11,5,18,-1,23,22,10,-1,10,11,23,-1,26,27,28,-1,28,29,30,-1,30,31,32,-1,28,30,32,-1,32,33,34,-1,34,35,24,-1,32,34,24,-1,28,32,24,-1,26,28,24,-1,25,26,24,-1,13,12,25,-1,25,24,13,-1,12,19,26,-1,26,25,12,-1,19,20,27,-1,27,26,19,-1,20,21,28,-1,28,27,20,-1,21,22,29,-1,29,28,21,-1,22,23,30,-1,30,29,22,-1,23,18,31,-1,31,30,23,-1,18,17,32,-1,32,31,18,-1,17,16,33,-1,33,32,17,-1,16,15,34,-1,34,33,16,-1,15,14,35,-1,35,34,15,-1,14,13,24,-1,24,35,14,-1,38,39,40,-1,40,41,42,-1,42,43,44,-1,40,42,44,-1,44,45,46,-1,46,47,36,-1,44,46,36,-1,40,44,36,-1,38,40,36,-1,37,38,36,-1,1,0,37,-1,37,36,1,-1,0,2,38,-1,38,37,0,-1,2,3,39,-1,39,38,2,-1,3,4,40,-1,40,39,3,-1,4,6,41,-1,41,40,4,-1,6,5,42,-1,42,41,6,-1,5,11,43,-1,43,42,5,-1,11,10,44,-1,44,43,11,-1,10,9,45,-1,45,44,10,-1,9,8,46,-1,46,45,9,-1,8,7,47,-1,47,46,8,-1,7,1,36,-1,36,47,7,-1]
IndexedFaceSet718.creaseAngle = 3.14159
IndexedFaceSet718.texCoordIndex = [1,12,13,-1,13,0,1,-1,2,0,13,-1,13,14,2,-1,2,14,15,-1,15,3,2,-1,3,15,16,-1,16,4,3,-1,6,17,18,-1,18,5,6,-1,4,16,17,-1,17,6,4,-1,19,12,1,-1,1,7,19,-1,8,20,19,-1,19,7,8,-1,21,20,8,-1,8,9,21,-1,22,21,9,-1,9,10,22,-1,18,23,11,-1,11,5,18,-1,23,22,10,-1,10,11,23,-1,26,27,28,-1,28,29,30,-1,30,31,32,-1,28,30,32,-1,32,33,34,-1,34,35,24,-1,32,34,24,-1,28,32,24,-1,26,28,24,-1,25,26,24,-1,13,12,25,-1,25,24,13,-1,12,19,26,-1,26,25,12,-1,19,20,27,-1,27,26,19,-1,20,21,28,-1,28,27,20,-1,21,22,29,-1,29,28,21,-1,22,23,30,-1,30,29,22,-1,23,18,31,-1,31,30,23,-1,18,17,32,-1,32,31,18,-1,17,16,33,-1,33,32,17,-1,16,15,34,-1,34,33,16,-1,15,14,35,-1,35,34,15,-1,14,13,24,-1,24,35,14,-1,38,39,40,-1,40,41,42,-1,42,43,44,-1,40,42,44,-1,44,45,46,-1,46,47,36,-1,44,46,36,-1,40,44,36,-1,38,40,36,-1,37,38,36,-1,1,0,37,-1,37,36,1,-1,0,2,38,-1,38,37,0,-1,2,3,39,-1,39,38,2,-1,3,4,40,-1,40,39,3,-1,4,6,41,-1,41,40,4,-1,6,5,42,-1,42,41,6,-1,5,11,43,-1,43,42,5,-1,11,10,44,-1,44,43,11,-1,10,9,45,-1,45,44,10,-1,9,8,46,-1,46,45,9,-1,8,7,47,-1,47,46,8,-1,7,1,36,-1,36,47,7,-1]
Coordinate719 = x3d.Coordinate()

IndexedFaceSet718.coord = Coordinate719
TextureCoordinate720 = x3d.TextureCoordinate()

IndexedFaceSet718.texCoord = TextureCoordinate720

Shape714.geometry = IndexedFaceSet718

Transform713.children.append(Shape714)

HAnimSegment712.children.append(Transform713)

HAnimJoint711.children.append(HAnimSegment712)
HAnimJoint721 = x3d.HAnimJoint()
HAnimJoint721.name = "vc2"
HAnimJoint721.DEF = "hanim_vc2"
HAnimJoint721.center = [0,56.02,-0.6695]
HAnimJoint721.ulimit = [0,0,0]
HAnimJoint721.llimit = [0,0,0]
HAnimSegment722 = x3d.HAnimSegment()
HAnimSegment722.name = "c2"
HAnimSegment722.DEF = "hanim_c2"
Transform723 = x3d.Transform()
Transform723.translation = [0,56.02,-0.6695]
Shape724 = x3d.Shape()
Appearance725 = x3d.Appearance()
Material726 = x3d.Material()
Material726.diffuseColor = [0.588,0.588,0.588]

Appearance725.material = Material726
ImageTexture727 = x3d.ImageTexture()
ImageTexture727.USE = "JinLOA2TextureAtlas"

Appearance725.texture = ImageTexture727

Shape724.appearance = Appearance725
IndexedFaceSet728 = x3d.IndexedFaceSet()
IndexedFaceSet728.coordIndex = [12,1,0,-1,0,13,12,-1,0,2,14,-1,14,13,0,-1,14,2,3,-1,3,15,14,-1,15,3,4,-1,4,16,15,-1,17,5,6,-1,6,18,17,-1,4,5,17,-1,17,16,4,-1,7,1,12,-1,12,19,7,-1,20,8,7,-1,7,19,20,-1,9,8,20,-1,20,21,9,-1,10,9,21,-1,21,22,10,-1,6,11,23,-1,23,18,6,-1,23,11,10,-1,10,22,23,-1,26,27,28,-1,28,29,30,-1,30,31,32,-1,28,30,32,-1,32,33,34,-1,34,35,24,-1,32,34,24,-1,28,32,24,-1,26,28,24,-1,25,26,24,-1,12,13,25,-1,25,24,12,-1,13,14,26,-1,26,25,13,-1,14,15,27,-1,27,26,14,-1,15,16,28,-1,28,27,15,-1,16,17,29,-1,29,28,16,-1,17,18,30,-1,30,29,17,-1,18,23,31,-1,31,30,18,-1,23,22,32,-1,32,31,23,-1,22,21,33,-1,33,32,22,-1,21,20,34,-1,34,33,21,-1,20,19,35,-1,35,34,20,-1,19,12,24,-1,24,35,19,-1,38,39,40,-1,40,41,42,-1,42,43,44,-1,40,42,44,-1,44,45,46,-1,46,47,36,-1,44,46,36,-1,40,44,36,-1,38,40,36,-1,37,38,36,-1,0,1,37,-1,37,36,0,-1,1,7,38,-1,38,37,1,-1,7,8,39,-1,39,38,7,-1,8,9,40,-1,40,39,8,-1,9,10,41,-1,41,40,9,-1,10,11,42,-1,42,41,10,-1,11,6,43,-1,43,42,11,-1,6,5,44,-1,44,43,6,-1,5,4,45,-1,45,44,5,-1,4,3,46,-1,46,45,4,-1,3,2,47,-1,47,46,3,-1,2,0,36,-1,36,47,2,-1]
IndexedFaceSet728.creaseAngle = 3.14159
IndexedFaceSet728.texCoordIndex = [12,1,0,-1,0,13,12,-1,0,2,14,-1,14,13,0,-1,14,2,3,-1,3,15,14,-1,15,3,4,-1,4,16,15,-1,17,5,6,-1,6,18,17,-1,4,5,17,-1,17,16,4,-1,7,1,12,-1,12,19,7,-1,20,8,7,-1,7,19,20,-1,9,8,20,-1,20,21,9,-1,10,9,21,-1,21,22,10,-1,6,11,23,-1,23,18,6,-1,23,11,10,-1,10,22,23,-1,26,27,28,-1,28,29,30,-1,30,31,32,-1,28,30,32,-1,32,33,34,-1,34,35,24,-1,32,34,24,-1,28,32,24,-1,26,28,24,-1,25,26,24,-1,12,13,25,-1,25,24,12,-1,13,14,26,-1,26,25,13,-1,14,15,27,-1,27,26,14,-1,15,16,28,-1,28,27,15,-1,16,17,29,-1,29,28,16,-1,17,18,30,-1,30,29,17,-1,18,23,31,-1,31,30,18,-1,23,22,32,-1,32,31,23,-1,22,21,33,-1,33,32,22,-1,21,20,34,-1,34,33,21,-1,20,19,35,-1,35,34,20,-1,19,12,24,-1,24,35,19,-1,38,39,40,-1,40,41,42,-1,42,43,44,-1,40,42,44,-1,44,45,46,-1,46,47,36,-1,44,46,36,-1,40,44,36,-1,38,40,36,-1,37,38,36,-1,0,1,37,-1,37,36,0,-1,1,7,38,-1,38,37,1,-1,7,8,39,-1,39,38,7,-1,8,9,40,-1,40,39,8,-1,9,10,41,-1,41,40,9,-1,10,11,42,-1,42,41,10,-1,11,6,43,-1,43,42,11,-1,6,5,44,-1,44,43,6,-1,5,4,45,-1,45,44,5,-1,4,3,46,-1,46,45,4,-1,3,2,47,-1,47,46,3,-1,2,0,36,-1,36,47,2,-1]
Coordinate729 = x3d.Coordinate()

IndexedFaceSet728.coord = Coordinate729
TextureCoordinate730 = x3d.TextureCoordinate()

IndexedFaceSet728.texCoord = TextureCoordinate730

Shape724.geometry = IndexedFaceSet728

Transform723.children.append(Shape724)

HAnimSegment722.children.append(Transform723)

HAnimJoint721.children.append(HAnimSegment722)
HAnimJoint731 = x3d.HAnimJoint()
HAnimJoint731.name = "skullbase"
HAnimJoint731.DEF = "hanim_skullbase"
HAnimJoint731.center = [0,57.43,-0.6863]
HAnimJoint731.ulimit = [0,0,0]
HAnimJoint731.llimit = [0,0,0]
HAnimSegment732 = x3d.HAnimSegment()
HAnimSegment732.name = "skull"
HAnimSegment732.DEF = "hanim_skull"
Transform733 = x3d.Transform()
Transform733.translation = [0,57.43,-0.6863]
Shape734 = x3d.Shape()
Appearance735 = x3d.Appearance()
Material736 = x3d.Material()
Material736.diffuseColor = [0.588,0.588,0.588]

Appearance735.material = Material736
ImageTexture737 = x3d.ImageTexture()
ImageTexture737.USE = "JinLOA2TextureAtlas"

Appearance735.texture = ImageTexture737

Shape734.appearance = Appearance735
IndexedFaceSet738 = x3d.IndexedFaceSet()
IndexedFaceSet738.coordIndex = [58,44,47,-1,47,49,58,-1,49,60,59,-1,59,1,49,-1,56,48,47,-1,47,44,56,-1,50,51,59,-1,59,60,50,-1,173,168,58,-1,58,49,173,-1,171,173,49,-1,49,1,171,-1,14,12,18,-1,18,15,14,-1,162,160,14,-1,14,15,162,-1,16,57,33,-1,21,18,12,-1,18,79,19,-1,80,20,19,-1,11,10,79,-1,18,21,79,-1,11,79,21,-1,21,12,78,-1,11,21,22,-1,321,345,320,-1,322,323,346,-1,80,25,24,-1,24,20,80,-1,26,38,24,-1,23,13,38,-1,20,77,18,-1,18,19,20,-1,38,29,30,-1,30,23,38,-1,27,30,29,-1,27,28,30,-1,30,28,23,-1,33,31,16,-1,31,37,16,-1,28,34,23,-1,17,35,36,-1,36,28,17,-1,33,36,35,-1,17,32,35,-1,32,33,35,-1,33,34,36,-1,36,34,28,-1,10,19,79,-1,4,40,37,-1,40,42,41,-1,40,41,37,-1,40,4,42,-1,56,43,4,-1,4,46,56,-1,45,43,56,-1,56,44,45,-1,43,45,4,-1,48,56,46,-1,46,3,48,-1,50,60,3,-1,51,50,3,-1,3,2,51,-1,58,168,52,-1,52,168,170,-1,61,52,170,-1,4,45,52,-1,52,61,4,-1,52,45,44,-1,44,58,52,-1,61,170,53,-1,170,165,39,-1,39,53,170,-1,4,61,53,-1,53,42,4,-1,53,39,41,-1,41,42,53,-1,165,57,39,-1,13,23,54,-1,16,37,57,-1,41,39,57,-1,37,41,57,-1,57,165,166,-1,54,166,13,-1,33,57,34,-1,34,57,54,-1,34,54,23,-1,166,162,55,-1,55,162,15,-1,77,55,15,-1,15,18,77,-1,166,77,13,-1,77,166,55,-1,13,77,24,-1,24,38,13,-1,20,24,77,-1,54,57,166,-1,47,60,49,-1,48,3,47,-1,3,60,47,-1,3,63,2,-1,72,62,63,-1,3,65,63,-1,3,46,64,-1,64,66,3,-1,6,66,64,-1,3,66,65,-1,6,73,8,-1,8,73,67,-1,6,75,73,-1,5,71,73,-1,73,75,5,-1,6,70,75,-1,64,46,69,-1,75,70,69,-1,75,69,344,-1,2,63,62,-1,8,66,6,-1,63,8,72,-1,9,74,71,-1,68,74,9,-1,74,8,67,-1,68,72,74,-1,72,8,74,-1,67,71,74,-1,67,73,71,-1,65,8,63,-1,65,66,8,-1,70,6,64,-1,70,64,69,-1,4,0,344,-1,69,46,4,-1,69,4,344,-1,76,344,0,-1,5,76,0,-1,5,75,76,-1,75,344,76,-1,133,125,123,-1,123,120,133,-1,125,1,59,-1,59,134,125,-1,131,120,123,-1,123,124,131,-1,126,134,59,-1,59,51,126,-1,172,125,133,-1,133,167,172,-1,171,1,125,-1,125,172,171,-1,14,91,94,-1,94,12,14,-1,161,91,14,-1,14,160,161,-1,109,132,92,-1,12,94,97,-1,95,149,94,-1,95,96,150,-1,149,88,89,-1,149,97,94,-1,97,149,89,-1,78,12,97,-1,98,97,89,-1,325,348,324,-1,354,326,327,-1,150,96,100,-1,100,101,150,-1,100,114,102,-1,114,90,99,-1,96,95,94,-1,94,148,96,-1,114,99,106,-1,106,105,114,-1,105,106,103,-1,106,104,103,-1,99,104,106,-1,92,107,109,-1,92,113,107,-1,99,110,104,-1,93,104,112,-1,112,111,93,-1,111,112,109,-1,111,108,93,-1,111,109,108,-1,112,110,109,-1,104,110,112,-1,149,95,88,-1,113,116,83,-1,117,118,116,-1,113,117,116,-1,118,83,116,-1,131,122,83,-1,83,119,131,-1,121,120,131,-1,131,119,121,-1,83,121,119,-1,124,82,122,-1,122,131,124,-1,82,134,126,-1,51,2,82,-1,82,126,51,-1,127,167,133,-1,169,167,127,-1,169,127,135,-1,83,135,127,-1,127,121,83,-1,127,133,120,-1,120,121,127,-1,128,169,135,-1,169,128,115,-1,115,163,169,-1,83,118,128,-1,128,135,83,-1,128,118,117,-1,117,115,128,-1,115,132,163,-1,129,99,90,-1,132,113,92,-1,132,115,117,-1,132,117,113,-1,164,163,132,-1,90,164,129,-1,110,132,109,-1,129,132,110,-1,99,129,110,-1,130,161,164,-1,91,161,130,-1,148,94,91,-1,91,130,148,-1,90,148,164,-1,130,164,148,-1,90,114,100,-1,100,148,90,-1,148,100,96,-1,164,132,129,-1,125,134,123,-1,123,82,124,-1,123,134,82,-1,2,136,82,-1,136,62,72,-1,136,138,82,-1,82,139,137,-1,137,122,82,-1,137,139,85,-1,138,139,82,-1,87,144,85,-1,140,144,87,-1,144,146,85,-1,84,146,144,-1,144,143,84,-1,146,142,85,-1,141,122,137,-1,141,142,146,-1,347,141,146,-1,62,136,2,-1,85,139,87,-1,72,87,136,-1,143,145,9,-1,9,145,68,-1,145,140,87,-1,68,145,72,-1,72,145,87,-1,145,143,140,-1,143,144,140,-1,136,87,138,-1,87,139,138,-1,137,85,142,-1,141,137,142,-1,347,81,83,-1,83,122,141,-1,347,83,141,-1,81,347,147,-1,81,147,84,-1,147,146,84,-1,147,347,146,-1,162,166,152,-1,151,160,162,-1,162,152,151,-1,152,166,165,-1,165,154,152,-1,154,165,170,-1,170,156,154,-1,152,154,155,-1,155,151,152,-1,156,153,155,-1,155,154,156,-1,173,156,170,-1,170,168,173,-1,171,153,156,-1,156,173,171,-1,157,164,161,-1,151,157,161,-1,161,160,151,-1,157,158,163,-1,163,164,157,-1,158,159,169,-1,169,163,158,-1,157,151,155,-1,155,158,157,-1,159,158,155,-1,155,153,159,-1,172,167,169,-1,169,159,172,-1,171,172,159,-1,159,153,171,-1,355,237,223,-1,174,236,237,-1,236,174,175,-1,179,238,176,-1,179,176,177,-1,179,177,178,-1,178,174,179,-1,174,178,175,-1,180,226,236,-1,238,180,236,-1,180,230,226,-1,237,236,223,-1,223,236,218,-1,225,355,223,-1,223,224,225,-1,328,329,239,-1,330,331,350,-1,228,227,219,-1,219,222,228,-1,236,226,218,-1,174,237,0,-1,0,237,355,-1,0,179,174,-1,318,355,225,-1,220,228,222,-1,221,228,220,-1,5,0,355,-1,218,182,223,-1,183,223,182,-1,181,183,185,-1,181,185,242,-1,213,212,244,-1,244,246,213,-1,213,246,245,-1,245,214,213,-1,245,247,184,-1,184,214,245,-1,214,184,206,-1,206,207,214,-1,217,319,225,-1,225,224,217,-1,183,181,217,-1,217,224,183,-1,224,223,183,-1,226,209,218,-1,218,209,184,-1,182,185,183,-1,218,184,182,-1,207,208,232,-1,232,214,207,-1,232,215,214,-1,209,206,184,-1,186,192,190,-1,190,188,186,-1,197,192,208,-1,208,207,197,-1,190,222,219,-1,219,188,190,-1,194,195,190,-1,226,189,209,-1,187,189,226,-1,192,186,208,-1,191,216,205,-1,196,205,216,-1,195,196,216,-1,196,195,194,-1,209,189,198,-1,199,197,207,-1,207,206,199,-1,233,234,197,-1,197,199,233,-1,209,198,199,-1,199,206,209,-1,233,199,198,-1,198,200,233,-1,248,194,202,-1,201,205,250,-1,248,249,196,-1,196,194,248,-1,196,249,250,-1,250,205,196,-1,234,203,197,-1,203,192,197,-1,194,190,202,-1,200,198,189,-1,189,204,200,-1,202,190,192,-1,202,192,203,-1,205,210,191,-1,210,205,201,-1,220,222,193,-1,204,189,187,-1,187,210,204,-1,210,201,204,-1,210,187,191,-1,195,211,190,-1,195,193,211,-1,193,222,211,-1,211,222,190,-1,215,212,213,-1,213,214,215,-1,230,187,226,-1,230,191,187,-1,229,221,230,-1,229,228,221,-1,9,355,318,-1,5,355,71,-1,71,355,9,-1,231,247,185,-1,182,231,185,-1,184,231,182,-1,184,247,231,-1,238,230,180,-1,230,221,191,-1,221,235,191,-1,191,235,216,-1,221,220,235,-1,193,235,220,-1,216,235,193,-1,193,195,216,-1,250,249,233,-1,203,234,248,-1,234,233,249,-1,250,233,200,-1,249,248,234,-1,243,241,240,-1,241,243,247,-1,204,201,250,-1,200,204,250,-1,203,248,202,-1,247,243,242,-1,247,242,185,-1,332,333,349,-1,334,335,7,-1,292,304,353,-1,304,303,251,-1,252,251,303,-1,253,305,256,-1,254,253,256,-1,256,251,255,-1,255,254,256,-1,252,255,251,-1,303,295,257,-1,303,257,305,-1,295,298,257,-1,292,303,304,-1,288,303,292,-1,294,352,292,-1,292,353,294,-1,336,337,293,-1,306,338,339,-1,296,291,219,-1,219,227,296,-1,288,295,303,-1,81,304,251,-1,353,304,81,-1,251,256,81,-1,294,353,317,-1,291,296,289,-1,289,296,290,-1,353,81,84,-1,292,258,288,-1,258,292,259,-1,261,259,181,-1,242,261,181,-1,285,309,244,-1,244,212,285,-1,285,286,308,-1,308,309,285,-1,308,286,260,-1,260,310,308,-1,286,281,280,-1,280,260,286,-1,217,352,294,-1,294,319,217,-1,259,352,217,-1,217,181,259,-1,259,292,352,-1,288,282,295,-1,260,282,288,-1,259,261,258,-1,258,260,288,-1,281,286,232,-1,232,208,281,-1,286,215,232,-1,260,280,282,-1,186,188,264,-1,264,266,186,-1,271,281,208,-1,208,266,271,-1,264,188,219,-1,219,291,264,-1,264,269,268,-1,282,263,295,-1,295,263,262,-1,208,186,266,-1,279,287,265,-1,287,279,270,-1,287,270,269,-1,268,269,270,-1,272,263,282,-1,273,280,281,-1,281,271,273,-1,300,273,271,-1,271,301,300,-1,282,280,273,-1,273,272,282,-1,300,274,272,-1,272,273,300,-1,276,268,311,-1,313,279,275,-1,311,268,270,-1,270,312,311,-1,270,279,313,-1,313,312,270,-1,271,277,301,-1,271,266,277,-1,276,264,268,-1,274,278,263,-1,263,272,274,-1,266,264,276,-1,277,266,276,-1,265,283,279,-1,275,279,283,-1,267,291,289,-1,278,283,262,-1,262,263,278,-1,278,275,283,-1,265,262,283,-1,264,284,269,-1,284,267,269,-1,284,291,267,-1,264,291,284,-1,285,212,215,-1,215,286,285,-1,295,262,298,-1,262,265,298,-1,298,290,297,-1,290,296,297,-1,317,353,9,-1,143,353,84,-1,9,353,143,-1,261,310,299,-1,261,299,258,-1,258,299,260,-1,299,310,260,-1,257,298,305,-1,265,290,298,-1,265,302,290,-1,287,302,265,-1,302,289,290,-1,289,302,267,-1,287,269,267,-1,267,302,287,-1,300,312,313,-1,311,301,277,-1,312,300,301,-1,274,300,313,-1,301,311,312,-1,240,307,243,-1,310,243,307,-1,313,275,278,-1,313,278,274,-1,276,311,277,-1,242,243,310,-1,261,242,310,-1,351,340,341,-1,86,342,343,-1,244,314,315,-1,315,246,244,-1,246,315,247,-1,247,245,246,-1,244,309,316,-1,316,314,244,-1,309,308,310,-1,310,316,309,-1,175,176,238,-1,238,236,175,-1,177,176,175,-1,175,178,177,-1,252,303,305,-1,305,253,252,-1,254,255,252,-1,252,253,254,-1,318,225,319,-1,319,9,318,-1,317,9,319,-1,319,294,317,-1]
IndexedFaceSet738.creaseAngle = 3.14159
IndexedFaceSet738.texCoordIndex = [0,3,2,-1,2,1,0,-1,1,6,5,-1,5,4,1,-1,7,8,2,-1,2,3,7,-1,9,10,5,-1,5,6,9,-1,11,12,0,-1,0,1,11,-1,13,11,1,-1,1,4,13,-1,14,17,16,-1,16,15,14,-1,18,19,14,-1,14,15,18,-1,22,21,20,-1,23,16,17,-1,16,25,24,-1,27,26,24,-1,29,28,25,-1,16,23,25,-1,29,25,23,-1,31,17,30,-1,29,23,32,-1,33,32,31,-1,33,31,30,-1,27,35,34,-1,34,26,27,-1,37,36,34,-1,39,38,36,-1,26,40,16,-1,16,24,26,-1,36,42,41,-1,41,39,36,-1,43,41,42,-1,43,44,41,-1,41,44,39,-1,20,45,22,-1,45,46,22,-1,44,47,39,-1,48,50,49,-1,49,44,48,-1,20,49,50,-1,48,51,50,-1,51,20,50,-1,20,47,49,-1,49,47,44,-1,28,24,25,-1,53,52,46,-1,52,55,54,-1,52,54,46,-1,52,53,55,-1,7,57,53,-1,53,56,7,-1,58,57,7,-1,7,59,58,-1,57,58,53,-1,8,7,56,-1,56,60,8,-1,9,6,60,-1,10,9,60,-1,60,61,10,-1,0,12,62,-1,62,12,63,-1,64,62,63,-1,53,58,62,-1,62,64,53,-1,62,58,59,-1,59,0,62,-1,64,63,65,-1,63,67,66,-1,66,65,63,-1,53,64,65,-1,65,55,53,-1,65,66,54,-1,54,55,65,-1,67,21,66,-1,38,39,68,-1,22,46,21,-1,54,66,21,-1,46,54,21,-1,21,67,69,-1,68,69,38,-1,20,21,47,-1,47,21,68,-1,47,68,39,-1,69,18,70,-1,70,18,15,-1,40,70,15,-1,15,16,40,-1,69,71,38,-1,71,69,70,-1,38,71,34,-1,34,36,38,-1,26,34,71,-1,68,21,69,-1,2,6,1,-1,8,60,2,-1,60,6,2,-1,74,73,72,-1,77,76,75,-1,74,78,73,-1,74,81,80,-1,80,79,74,-1,82,79,80,-1,74,79,78,-1,82,84,83,-1,83,84,85,-1,82,86,84,-1,87,90,89,-1,89,88,87,-1,92,91,88,-1,80,81,93,-1,88,91,94,-1,86,93,95,-1,72,73,96,-1,83,79,82,-1,73,83,97,-1,100,99,98,-1,103,102,101,-1,99,83,85,-1,104,97,99,-1,97,83,99,-1,105,90,102,-1,105,89,90,-1,107,106,75,-1,107,108,106,-1,109,82,80,-1,109,80,93,-1,112,111,110,-1,93,81,113,-1,93,113,95,-1,114,110,111,-1,115,114,111,-1,87,86,116,-1,86,95,116,-1,117,120,119,-1,119,118,117,-1,120,123,122,-1,122,121,120,-1,124,118,119,-1,119,125,124,-1,126,121,122,-1,122,127,126,-1,128,120,117,-1,117,129,128,-1,130,123,120,-1,120,128,130,-1,14,132,131,-1,131,17,14,-1,133,132,14,-1,14,19,133,-1,136,135,134,-1,17,131,137,-1,139,138,131,-1,139,141,140,-1,138,143,142,-1,138,137,131,-1,137,138,142,-1,30,17,144,-1,145,137,142,-1,144,145,146,-1,30,144,146,-1,140,141,148,-1,148,147,140,-1,148,150,149,-1,150,152,151,-1,141,139,131,-1,131,153,141,-1,150,151,155,-1,155,154,150,-1,154,155,156,-1,155,157,156,-1,151,157,155,-1,134,158,136,-1,134,159,158,-1,151,160,157,-1,161,157,163,-1,163,162,161,-1,162,163,136,-1,162,164,161,-1,162,136,164,-1,163,160,136,-1,157,160,163,-1,138,139,143,-1,159,166,165,-1,168,167,166,-1,159,168,166,-1,167,165,166,-1,124,170,165,-1,165,169,124,-1,171,172,124,-1,124,169,171,-1,165,171,169,-1,125,173,170,-1,170,124,125,-1,173,121,126,-1,127,174,173,-1,173,126,127,-1,175,129,117,-1,176,129,175,-1,176,175,177,-1,165,177,175,-1,175,171,165,-1,175,117,172,-1,172,171,175,-1,178,176,177,-1,176,178,180,-1,180,179,176,-1,165,167,178,-1,178,177,165,-1,178,167,168,-1,168,180,178,-1,180,135,179,-1,181,151,152,-1,135,159,134,-1,135,180,168,-1,135,168,159,-1,182,179,135,-1,152,182,181,-1,160,135,136,-1,181,135,160,-1,151,181,160,-1,183,133,182,-1,132,133,183,-1,153,131,132,-1,132,183,153,-1,152,184,182,-1,183,182,184,-1,152,150,148,-1,148,184,152,-1,184,148,141,-1,182,135,181,-1,120,121,119,-1,119,173,125,-1,119,121,173,-1,72,186,185,-1,187,76,77,-1,186,188,185,-1,185,191,190,-1,190,189,185,-1,190,191,192,-1,188,191,185,-1,194,193,192,-1,195,193,194,-1,193,196,192,-1,197,200,199,-1,199,198,197,-1,200,202,201,-1,203,189,190,-1,204,202,200,-1,205,203,196,-1,96,186,72,-1,192,191,194,-1,97,194,186,-1,207,206,100,-1,101,208,103,-1,206,195,194,-1,104,206,97,-1,97,206,194,-1,208,198,209,-1,198,199,209,-1,187,211,210,-1,211,212,210,-1,190,192,213,-1,203,190,213,-1,216,215,214,-1,217,189,203,-1,205,217,203,-1,215,216,218,-1,215,218,219,-1,220,196,197,-1,220,205,196,-1,18,69,221,-1,222,19,18,-1,18,221,222,-1,221,69,67,-1,67,223,221,-1,223,67,63,-1,63,224,223,-1,221,223,225,-1,225,222,221,-1,224,226,225,-1,225,223,224,-1,11,224,63,-1,63,12,11,-1,13,226,224,-1,224,11,13,-1,227,182,133,-1,222,227,133,-1,133,19,222,-1,227,228,179,-1,179,182,227,-1,228,229,176,-1,176,179,228,-1,227,222,225,-1,225,228,227,-1,229,228,225,-1,225,230,229,-1,128,129,176,-1,176,229,128,-1,130,128,229,-1,229,230,130,-1,233,232,231,-1,235,234,232,-1,234,235,236,-1,239,238,237,-1,239,237,240,-1,239,240,241,-1,241,235,239,-1,235,241,236,-1,243,242,234,-1,238,243,234,-1,243,244,242,-1,232,234,231,-1,231,234,245,-1,246,233,231,-1,231,247,246,-1,247,246,233,-1,231,247,233,-1,248,251,250,-1,250,249,248,-1,234,242,245,-1,235,232,252,-1,252,232,233,-1,252,239,235,-1,253,233,246,-1,254,248,249,-1,255,248,254,-1,256,252,233,-1,245,257,231,-1,258,231,257,-1,261,260,259,-1,261,259,262,-1,263,266,265,-1,265,264,263,-1,263,264,268,-1,268,267,263,-1,268,270,269,-1,269,267,268,-1,267,269,272,-1,272,271,267,-1,273,274,246,-1,246,247,273,-1,258,275,273,-1,273,247,258,-1,247,231,258,-1,278,277,276,-1,276,277,269,-1,279,259,260,-1,276,269,279,-1,271,281,280,-1,280,267,271,-1,280,282,267,-1,277,272,269,-1,284,287,286,-1,286,285,284,-1,288,287,281,-1,281,271,288,-1,286,249,250,-1,250,285,286,-1,290,289,286,-1,278,291,277,-1,292,291,278,-1,287,284,283,-1,295,294,293,-1,296,293,294,-1,289,296,294,-1,296,289,290,-1,277,291,297,-1,298,288,271,-1,271,272,298,-1,299,300,288,-1,288,298,299,-1,277,297,298,-1,298,272,277,-1,299,298,297,-1,297,301,299,-1,303,290,302,-1,305,293,304,-1,303,306,296,-1,296,290,303,-1,296,306,304,-1,304,293,296,-1,300,307,288,-1,307,287,288,-1,290,286,302,-1,301,297,291,-1,291,308,301,-1,302,286,287,-1,309,287,307,-1,293,310,295,-1,310,293,305,-1,254,249,311,-1,308,291,292,-1,292,310,308,-1,310,305,308,-1,310,292,295,-1,289,312,286,-1,289,311,312,-1,311,249,312,-1,312,249,286,-1,282,266,263,-1,263,267,282,-1,313,292,278,-1,313,295,292,-1,314,255,313,-1,314,248,255,-1,315,233,253,-1,256,233,316,-1,316,233,315,-1,317,270,259,-1,279,317,259,-1,269,317,279,-1,269,270,317,-1,238,244,243,-1,313,255,295,-1,255,318,295,-1,295,318,294,-1,255,254,318,-1,311,318,254,-1,294,318,311,-1,311,289,294,-1,304,306,299,-1,307,300,303,-1,300,299,306,-1,304,299,301,-1,306,303,300,-1,321,320,319,-1,320,321,270,-1,308,305,304,-1,301,308,304,-1,307,303,309,-1,270,321,262,-1,270,262,259,-1,252,322,239,-1,252,256,322,-1,231,232,233,-1,232,234,235,-1,236,235,234,-1,237,238,239,-1,240,237,239,-1,239,235,241,-1,241,240,239,-1,236,241,235,-1,234,242,243,-1,234,243,238,-1,242,244,243,-1,231,234,232,-1,245,234,231,-1,246,247,231,-1,231,233,246,-1,233,246,247,-1,233,247,231,-1,323,324,250,-1,250,251,323,-1,245,242,234,-1,252,232,235,-1,233,232,252,-1,235,239,252,-1,246,233,253,-1,324,323,325,-1,325,323,326,-1,233,252,256,-1,231,257,245,-1,257,231,258,-1,329,328,327,-1,330,329,327,-1,331,332,265,-1,265,266,331,-1,331,334,333,-1,333,332,331,-1,333,334,336,-1,336,335,333,-1,334,338,337,-1,337,336,334,-1,273,247,246,-1,246,274,273,-1,258,247,273,-1,273,275,258,-1,258,231,247,-1,341,340,339,-1,336,340,341,-1,328,329,342,-1,342,336,341,-1,338,334,280,-1,280,343,338,-1,334,282,280,-1,336,337,340,-1,284,285,345,-1,345,344,284,-1,346,338,343,-1,343,344,346,-1,345,285,250,-1,250,324,345,-1,345,348,347,-1,340,349,339,-1,339,349,350,-1,283,284,344,-1,353,352,351,-1,352,353,354,-1,352,354,348,-1,347,348,354,-1,355,349,340,-1,356,337,338,-1,338,346,356,-1,357,356,346,-1,346,358,357,-1,340,337,356,-1,356,355,340,-1,357,359,355,-1,355,356,357,-1,361,347,360,-1,363,353,362,-1,360,347,354,-1,354,364,360,-1,354,353,363,-1,363,364,354,-1,346,365,358,-1,346,344,365,-1,361,345,347,-1,359,366,349,-1,349,355,359,-1,344,345,361,-1,365,344,367,-1,351,368,353,-1,362,353,368,-1,369,324,325,-1,366,368,350,-1,350,349,366,-1,366,362,368,-1,351,350,368,-1,345,370,348,-1,370,369,348,-1,370,324,369,-1,345,324,370,-1,331,266,282,-1,282,334,331,-1,339,350,371,-1,350,351,371,-1,371,326,372,-1,326,323,372,-1,253,233,315,-1,316,233,256,-1,315,233,316,-1,329,335,373,-1,329,373,342,-1,342,373,336,-1,373,335,336,-1,243,244,238,-1,351,326,371,-1,351,374,326,-1,352,374,351,-1,374,325,326,-1,325,374,369,-1,352,348,369,-1,369,374,352,-1,357,364,363,-1,360,358,365,-1,364,357,358,-1,359,357,363,-1,358,360,364,-1,319,376,375,-1,335,375,376,-1,363,362,366,-1,363,366,359,-1,367,360,365,-1,330,375,335,-1,329,330,335,-1,239,322,252,-1,322,256,252,-1,265,378,377,-1,377,264,265,-1,264,377,270,-1,270,268,264,-1,265,332,379,-1,379,378,265,-1,332,333,335,-1,335,379,332,-1,380,383,382,-1,382,381,380,-1,384,383,380,-1,380,385,384,-1,380,381,382,-1,382,383,380,-1,384,385,380,-1,380,383,384,-1,388,389,386,-1,386,387,388,-1,391,387,386,-1,386,390,391,-1]
Coordinate739 = x3d.Coordinate()

IndexedFaceSet738.coord = Coordinate739
TextureCoordinate740 = x3d.TextureCoordinate()

IndexedFaceSet738.texCoord = TextureCoordinate740

Shape734.geometry = IndexedFaceSet738

Transform733.children.append(Shape734)

HAnimSegment732.children.append(Transform733)

HAnimJoint731.children.append(HAnimSegment732)

HAnimJoint721.children.append(HAnimJoint731)

HAnimJoint711.children.append(HAnimJoint721)

HAnimJoint221.children.append(HAnimJoint711)

HAnimJoint211.children.append(HAnimJoint221)

HAnimJoint201.children.append(HAnimJoint211)

HAnimJoint191.children.append(HAnimJoint201)

HAnimJoint181.children.append(HAnimJoint191)

HAnimJoint171.children.append(HAnimJoint181)

HAnimJoint31.children.append(HAnimJoint171)

HAnimHumanoid23.skeleton.append(HAnimJoint31)
HAnimJoint741 = x3d.HAnimJoint()
HAnimJoint741.USE = "hanim_humanoid_root"

HAnimHumanoid23.joints.append(HAnimJoint741)
HAnimJoint742 = x3d.HAnimJoint()
HAnimJoint742.USE = "hanim_sacroiliac"

HAnimHumanoid23.joints.append(HAnimJoint742)
HAnimJoint743 = x3d.HAnimJoint()
HAnimJoint743.USE = "hanim_vl5"

HAnimHumanoid23.joints.append(HAnimJoint743)
HAnimJoint744 = x3d.HAnimJoint()
HAnimJoint744.USE = "hanim_vl3"

HAnimHumanoid23.joints.append(HAnimJoint744)
HAnimJoint745 = x3d.HAnimJoint()
HAnimJoint745.USE = "hanim_vl1"

HAnimHumanoid23.joints.append(HAnimJoint745)
HAnimJoint746 = x3d.HAnimJoint()
HAnimJoint746.USE = "hanim_vt10"

HAnimHumanoid23.joints.append(HAnimJoint746)
HAnimJoint747 = x3d.HAnimJoint()
HAnimJoint747.USE = "hanim_vt6"

HAnimHumanoid23.joints.append(HAnimJoint747)
HAnimJoint748 = x3d.HAnimJoint()
HAnimJoint748.USE = "hanim_vt1"

HAnimHumanoid23.joints.append(HAnimJoint748)
HAnimJoint749 = x3d.HAnimJoint()
HAnimJoint749.USE = "hanim_vc4"

HAnimHumanoid23.joints.append(HAnimJoint749)
HAnimJoint750 = x3d.HAnimJoint()
HAnimJoint750.USE = "hanim_vc2"

HAnimHumanoid23.joints.append(HAnimJoint750)
HAnimJoint751 = x3d.HAnimJoint()
HAnimJoint751.USE = "hanim_skullbase"

HAnimHumanoid23.joints.append(HAnimJoint751)
HAnimJoint752 = x3d.HAnimJoint()
HAnimJoint752.USE = "hanim_l_acromioclavicular"

HAnimHumanoid23.joints.append(HAnimJoint752)
HAnimJoint753 = x3d.HAnimJoint()
HAnimJoint753.USE = "hanim_r_acromioclavicular"

HAnimHumanoid23.joints.append(HAnimJoint753)
HAnimJoint754 = x3d.HAnimJoint()
HAnimJoint754.USE = "hanim_l_carpal_distal_interphalangeal_2"

HAnimHumanoid23.joints.append(HAnimJoint754)
HAnimJoint755 = x3d.HAnimJoint()
HAnimJoint755.USE = "hanim_r_carpal_distal_interphalangeal_2"

HAnimHumanoid23.joints.append(HAnimJoint755)
HAnimJoint756 = x3d.HAnimJoint()
HAnimJoint756.USE = "hanim_l_carpal_distal_interphalangeal_3"

HAnimHumanoid23.joints.append(HAnimJoint756)
HAnimJoint757 = x3d.HAnimJoint()
HAnimJoint757.USE = "hanim_r_carpal_distal_interphalangeal_3"

HAnimHumanoid23.joints.append(HAnimJoint757)
HAnimJoint758 = x3d.HAnimJoint()
HAnimJoint758.USE = "hanim_l_carpal_distal_interphalangeal_4"

HAnimHumanoid23.joints.append(HAnimJoint758)
HAnimJoint759 = x3d.HAnimJoint()
HAnimJoint759.USE = "hanim_r_carpal_distal_interphalangeal_4"

HAnimHumanoid23.joints.append(HAnimJoint759)
HAnimJoint760 = x3d.HAnimJoint()
HAnimJoint760.USE = "hanim_l_carpal_distal_interphalangeal_5"

HAnimHumanoid23.joints.append(HAnimJoint760)
HAnimJoint761 = x3d.HAnimJoint()
HAnimJoint761.USE = "hanim_r_carpal_distal_interphalangeal_5"

HAnimHumanoid23.joints.append(HAnimJoint761)
HAnimJoint762 = x3d.HAnimJoint()
HAnimJoint762.USE = "hanim_l_carpal_interphalangeal_1"

HAnimHumanoid23.joints.append(HAnimJoint762)
HAnimJoint763 = x3d.HAnimJoint()
HAnimJoint763.USE = "hanim_r_carpal_interphalangeal_1"

HAnimHumanoid23.joints.append(HAnimJoint763)
HAnimJoint764 = x3d.HAnimJoint()
HAnimJoint764.USE = "hanim_l_carpal_proximal_interphalangeal_2"

HAnimHumanoid23.joints.append(HAnimJoint764)
HAnimJoint765 = x3d.HAnimJoint()
HAnimJoint765.USE = "hanim_r_carpal_proximal_interphalangeal_2"

HAnimHumanoid23.joints.append(HAnimJoint765)
HAnimJoint766 = x3d.HAnimJoint()
HAnimJoint766.USE = "hanim_l_carpal_proximal_interphalangeal_3"

HAnimHumanoid23.joints.append(HAnimJoint766)
HAnimJoint767 = x3d.HAnimJoint()
HAnimJoint767.USE = "hanim_r_carpal_proximal_interphalangeal_3"

HAnimHumanoid23.joints.append(HAnimJoint767)
HAnimJoint768 = x3d.HAnimJoint()
HAnimJoint768.USE = "hanim_l_carpal_proximal_interphalangeal_4"

HAnimHumanoid23.joints.append(HAnimJoint768)
HAnimJoint769 = x3d.HAnimJoint()
HAnimJoint769.USE = "hanim_r_carpal_proximal_interphalangeal_4"

HAnimHumanoid23.joints.append(HAnimJoint769)
HAnimJoint770 = x3d.HAnimJoint()
HAnimJoint770.USE = "hanim_l_carpal_proximal_interphalangeal_5"

HAnimHumanoid23.joints.append(HAnimJoint770)
HAnimJoint771 = x3d.HAnimJoint()
HAnimJoint771.USE = "hanim_r_carpal_proximal_interphalangeal_5"

HAnimHumanoid23.joints.append(HAnimJoint771)
HAnimJoint772 = x3d.HAnimJoint()
HAnimJoint772.USE = "hanim_l_carpometacarpal_1"

HAnimHumanoid23.joints.append(HAnimJoint772)
HAnimJoint773 = x3d.HAnimJoint()
HAnimJoint773.USE = "hanim_r_carpometacarpal_1"

HAnimHumanoid23.joints.append(HAnimJoint773)
HAnimJoint774 = x3d.HAnimJoint()
HAnimJoint774.USE = "hanim_l_carpometacarpal_2"

HAnimHumanoid23.joints.append(HAnimJoint774)
HAnimJoint775 = x3d.HAnimJoint()
HAnimJoint775.USE = "hanim_r_carpometacarpal_2"

HAnimHumanoid23.joints.append(HAnimJoint775)
HAnimJoint776 = x3d.HAnimJoint()
HAnimJoint776.USE = "hanim_l_carpometacarpal_3"

HAnimHumanoid23.joints.append(HAnimJoint776)
HAnimJoint777 = x3d.HAnimJoint()
HAnimJoint777.USE = "hanim_r_carpometacarpal_3"

HAnimHumanoid23.joints.append(HAnimJoint777)
HAnimJoint778 = x3d.HAnimJoint()
HAnimJoint778.USE = "hanim_l_carpometacarpal_4"

HAnimHumanoid23.joints.append(HAnimJoint778)
HAnimJoint779 = x3d.HAnimJoint()
HAnimJoint779.USE = "hanim_r_carpometacarpal_4"

HAnimHumanoid23.joints.append(HAnimJoint779)
HAnimJoint780 = x3d.HAnimJoint()
HAnimJoint780.USE = "hanim_l_carpometacarpal_5"

HAnimHumanoid23.joints.append(HAnimJoint780)
HAnimJoint781 = x3d.HAnimJoint()
HAnimJoint781.USE = "hanim_r_carpometacarpal_5"

HAnimHumanoid23.joints.append(HAnimJoint781)
HAnimJoint782 = x3d.HAnimJoint()
HAnimJoint782.USE = "hanim_l_elbow"

HAnimHumanoid23.joints.append(HAnimJoint782)
HAnimJoint783 = x3d.HAnimJoint()
HAnimJoint783.USE = "hanim_r_elbow"

HAnimHumanoid23.joints.append(HAnimJoint783)
HAnimJoint784 = x3d.HAnimJoint()
HAnimJoint784.USE = "hanim_l_hip"

HAnimHumanoid23.joints.append(HAnimJoint784)
HAnimJoint785 = x3d.HAnimJoint()
HAnimJoint785.USE = "hanim_r_hip"

HAnimHumanoid23.joints.append(HAnimJoint785)
HAnimJoint786 = x3d.HAnimJoint()
HAnimJoint786.USE = "hanim_l_knee"

HAnimHumanoid23.joints.append(HAnimJoint786)
HAnimJoint787 = x3d.HAnimJoint()
HAnimJoint787.USE = "hanim_r_knee"

HAnimHumanoid23.joints.append(HAnimJoint787)
HAnimJoint788 = x3d.HAnimJoint()
HAnimJoint788.USE = "hanim_l_metacarpophalangeal_1"

HAnimHumanoid23.joints.append(HAnimJoint788)
HAnimJoint789 = x3d.HAnimJoint()
HAnimJoint789.USE = "hanim_r_metacarpophalangeal_1"

HAnimHumanoid23.joints.append(HAnimJoint789)
HAnimJoint790 = x3d.HAnimJoint()
HAnimJoint790.USE = "hanim_l_metacarpophalangeal_2"

HAnimHumanoid23.joints.append(HAnimJoint790)
HAnimJoint791 = x3d.HAnimJoint()
HAnimJoint791.USE = "hanim_r_metacarpophalangeal_2"

HAnimHumanoid23.joints.append(HAnimJoint791)
HAnimJoint792 = x3d.HAnimJoint()
HAnimJoint792.USE = "hanim_l_metacarpophalangeal_3"

HAnimHumanoid23.joints.append(HAnimJoint792)
HAnimJoint793 = x3d.HAnimJoint()
HAnimJoint793.USE = "hanim_r_metacarpophalangeal_3"

HAnimHumanoid23.joints.append(HAnimJoint793)
HAnimJoint794 = x3d.HAnimJoint()
HAnimJoint794.USE = "hanim_l_metacarpophalangeal_4"

HAnimHumanoid23.joints.append(HAnimJoint794)
HAnimJoint795 = x3d.HAnimJoint()
HAnimJoint795.USE = "hanim_r_metacarpophalangeal_4"

HAnimHumanoid23.joints.append(HAnimJoint795)
HAnimJoint796 = x3d.HAnimJoint()
HAnimJoint796.USE = "hanim_l_metacarpophalangeal_5"

HAnimHumanoid23.joints.append(HAnimJoint796)
HAnimJoint797 = x3d.HAnimJoint()
HAnimJoint797.USE = "hanim_r_metacarpophalangeal_5"

HAnimHumanoid23.joints.append(HAnimJoint797)
HAnimJoint798 = x3d.HAnimJoint()
HAnimJoint798.USE = "hanim_l_metatarsophalangeal_2"

HAnimHumanoid23.joints.append(HAnimJoint798)
HAnimJoint799 = x3d.HAnimJoint()
HAnimJoint799.USE = "hanim_r_metatarsophalangeal_2"

HAnimHumanoid23.joints.append(HAnimJoint799)
HAnimJoint800 = x3d.HAnimJoint()
HAnimJoint800.USE = "hanim_l_radiocarpal"

HAnimHumanoid23.joints.append(HAnimJoint800)
HAnimJoint801 = x3d.HAnimJoint()
HAnimJoint801.USE = "hanim_r_radiocarpal"

HAnimHumanoid23.joints.append(HAnimJoint801)
HAnimJoint802 = x3d.HAnimJoint()
HAnimJoint802.USE = "hanim_l_shoulder"

HAnimHumanoid23.joints.append(HAnimJoint802)
HAnimJoint803 = x3d.HAnimJoint()
HAnimJoint803.USE = "hanim_r_shoulder"

HAnimHumanoid23.joints.append(HAnimJoint803)
HAnimJoint804 = x3d.HAnimJoint()
HAnimJoint804.USE = "hanim_l_sternoclavicular"

HAnimHumanoid23.joints.append(HAnimJoint804)
HAnimJoint805 = x3d.HAnimJoint()
HAnimJoint805.USE = "hanim_r_sternoclavicular"

HAnimHumanoid23.joints.append(HAnimJoint805)
HAnimJoint806 = x3d.HAnimJoint()
HAnimJoint806.USE = "hanim_l_talocrural"

HAnimHumanoid23.joints.append(HAnimJoint806)
HAnimJoint807 = x3d.HAnimJoint()
HAnimJoint807.USE = "hanim_r_talocrural"

HAnimHumanoid23.joints.append(HAnimJoint807)
HAnimJoint808 = x3d.HAnimJoint()
HAnimJoint808.USE = "hanim_l_tarsal_distal_interphalangeal_2"

HAnimHumanoid23.joints.append(HAnimJoint808)
HAnimJoint809 = x3d.HAnimJoint()
HAnimJoint809.USE = "hanim_r_tarsal_distal_interphalangeal_2"

HAnimHumanoid23.joints.append(HAnimJoint809)
HAnimJoint810 = x3d.HAnimJoint()
HAnimJoint810.USE = "hanim_l_tarsometatarsal_2"

HAnimHumanoid23.joints.append(HAnimJoint810)
HAnimJoint811 = x3d.HAnimJoint()
HAnimJoint811.USE = "hanim_r_tarsometatarsal_2"

HAnimHumanoid23.joints.append(HAnimJoint811)
HAnimSegment812 = x3d.HAnimSegment()
HAnimSegment812.USE = "hanim_sacrum"

HAnimHumanoid23.segments.append(HAnimSegment812)
HAnimSegment813 = x3d.HAnimSegment()
HAnimSegment813.USE = "hanim_pelvis"

HAnimHumanoid23.segments.append(HAnimSegment813)
HAnimSegment814 = x3d.HAnimSegment()
HAnimSegment814.USE = "hanim_l5"

HAnimHumanoid23.segments.append(HAnimSegment814)
HAnimSegment815 = x3d.HAnimSegment()
HAnimSegment815.USE = "hanim_l3"

HAnimHumanoid23.segments.append(HAnimSegment815)
HAnimSegment816 = x3d.HAnimSegment()
HAnimSegment816.USE = "hanim_l1"

HAnimHumanoid23.segments.append(HAnimSegment816)
HAnimSegment817 = x3d.HAnimSegment()
HAnimSegment817.USE = "hanim_t10"

HAnimHumanoid23.segments.append(HAnimSegment817)
HAnimSegment818 = x3d.HAnimSegment()
HAnimSegment818.USE = "hanim_t6"

HAnimHumanoid23.segments.append(HAnimSegment818)
HAnimSegment819 = x3d.HAnimSegment()
HAnimSegment819.USE = "hanim_t1"

HAnimHumanoid23.segments.append(HAnimSegment819)
HAnimSegment820 = x3d.HAnimSegment()
HAnimSegment820.USE = "hanim_c4"

HAnimHumanoid23.segments.append(HAnimSegment820)
HAnimSegment821 = x3d.HAnimSegment()
HAnimSegment821.USE = "hanim_c2"

HAnimHumanoid23.segments.append(HAnimSegment821)
HAnimSegment822 = x3d.HAnimSegment()
HAnimSegment822.USE = "hanim_skull"

HAnimHumanoid23.segments.append(HAnimSegment822)
HAnimSegment823 = x3d.HAnimSegment()
HAnimSegment823.USE = "hanim_l_calf"

HAnimHumanoid23.segments.append(HAnimSegment823)
HAnimSegment824 = x3d.HAnimSegment()
HAnimSegment824.USE = "hanim_r_calf"

HAnimHumanoid23.segments.append(HAnimSegment824)
HAnimSegment825 = x3d.HAnimSegment()
HAnimSegment825.USE = "hanim_l_carpal"

HAnimHumanoid23.segments.append(HAnimSegment825)
HAnimSegment826 = x3d.HAnimSegment()
HAnimSegment826.USE = "hanim_r_carpal"

HAnimHumanoid23.segments.append(HAnimSegment826)
HAnimSegment827 = x3d.HAnimSegment()
HAnimSegment827.USE = "hanim_l_carpal_distal_phalanx_1"

HAnimHumanoid23.segments.append(HAnimSegment827)
HAnimSegment828 = x3d.HAnimSegment()
HAnimSegment828.USE = "hanim_r_carpal_distal_phalanx_1"

HAnimHumanoid23.segments.append(HAnimSegment828)
HAnimSegment829 = x3d.HAnimSegment()
HAnimSegment829.USE = "hanim_l_carpal_distal_phalanx_2"

HAnimHumanoid23.segments.append(HAnimSegment829)
HAnimSegment830 = x3d.HAnimSegment()
HAnimSegment830.USE = "hanim_r_carpal_distal_phalanx_2"

HAnimHumanoid23.segments.append(HAnimSegment830)
HAnimSegment831 = x3d.HAnimSegment()
HAnimSegment831.USE = "hanim_l_carpal_distal_phalanx_3"

HAnimHumanoid23.segments.append(HAnimSegment831)
HAnimSegment832 = x3d.HAnimSegment()
HAnimSegment832.USE = "hanim_r_carpal_distal_phalanx_3"

HAnimHumanoid23.segments.append(HAnimSegment832)
HAnimSegment833 = x3d.HAnimSegment()
HAnimSegment833.USE = "hanim_l_carpal_distal_phalanx_4"

HAnimHumanoid23.segments.append(HAnimSegment833)
HAnimSegment834 = x3d.HAnimSegment()
HAnimSegment834.USE = "hanim_r_carpal_distal_phalanx_4"

HAnimHumanoid23.segments.append(HAnimSegment834)
HAnimSegment835 = x3d.HAnimSegment()
HAnimSegment835.USE = "hanim_l_carpal_distal_phalanx_5"

HAnimHumanoid23.segments.append(HAnimSegment835)
HAnimSegment836 = x3d.HAnimSegment()
HAnimSegment836.USE = "hanim_r_carpal_distal_phalanx_5"

HAnimHumanoid23.segments.append(HAnimSegment836)
HAnimSegment837 = x3d.HAnimSegment()
HAnimSegment837.USE = "hanim_l_carpal_middle_phalanx_2"

HAnimHumanoid23.segments.append(HAnimSegment837)
HAnimSegment838 = x3d.HAnimSegment()
HAnimSegment838.USE = "hanim_r_carpal_middle_phalanx_2"

HAnimHumanoid23.segments.append(HAnimSegment838)
HAnimSegment839 = x3d.HAnimSegment()
HAnimSegment839.USE = "hanim_l_carpal_middle_phalanx_3"

HAnimHumanoid23.segments.append(HAnimSegment839)
HAnimSegment840 = x3d.HAnimSegment()
HAnimSegment840.USE = "hanim_r_carpal_middle_phalanx_3"

HAnimHumanoid23.segments.append(HAnimSegment840)
HAnimSegment841 = x3d.HAnimSegment()
HAnimSegment841.USE = "hanim_l_carpal_middle_phalanx_4"

HAnimHumanoid23.segments.append(HAnimSegment841)
HAnimSegment842 = x3d.HAnimSegment()
HAnimSegment842.USE = "hanim_r_carpal_middle_phalanx_4"

HAnimHumanoid23.segments.append(HAnimSegment842)
HAnimSegment843 = x3d.HAnimSegment()
HAnimSegment843.USE = "hanim_l_carpal_middle_phalanx_5"

HAnimHumanoid23.segments.append(HAnimSegment843)
HAnimSegment844 = x3d.HAnimSegment()
HAnimSegment844.USE = "hanim_r_carpal_middle_phalanx_5"

HAnimHumanoid23.segments.append(HAnimSegment844)
HAnimSegment845 = x3d.HAnimSegment()
HAnimSegment845.USE = "hanim_l_carpal_proximal_phalanx_1"

HAnimHumanoid23.segments.append(HAnimSegment845)
HAnimSegment846 = x3d.HAnimSegment()
HAnimSegment846.USE = "hanim_r_carpal_proximal_phalanx_1"

HAnimHumanoid23.segments.append(HAnimSegment846)
HAnimSegment847 = x3d.HAnimSegment()
HAnimSegment847.USE = "hanim_l_carpal_proximal_phalanx_2"

HAnimHumanoid23.segments.append(HAnimSegment847)
HAnimSegment848 = x3d.HAnimSegment()
HAnimSegment848.USE = "hanim_r_carpal_proximal_phalanx_2"

HAnimHumanoid23.segments.append(HAnimSegment848)
HAnimSegment849 = x3d.HAnimSegment()
HAnimSegment849.USE = "hanim_l_carpal_proximal_phalanx_3"

HAnimHumanoid23.segments.append(HAnimSegment849)
HAnimSegment850 = x3d.HAnimSegment()
HAnimSegment850.USE = "hanim_r_carpal_proximal_phalanx_3"

HAnimHumanoid23.segments.append(HAnimSegment850)
HAnimSegment851 = x3d.HAnimSegment()
HAnimSegment851.USE = "hanim_l_carpal_proximal_phalanx_4"

HAnimHumanoid23.segments.append(HAnimSegment851)
HAnimSegment852 = x3d.HAnimSegment()
HAnimSegment852.USE = "hanim_r_carpal_proximal_phalanx_4"

HAnimHumanoid23.segments.append(HAnimSegment852)
HAnimSegment853 = x3d.HAnimSegment()
HAnimSegment853.USE = "hanim_l_carpal_proximal_phalanx_5"

HAnimHumanoid23.segments.append(HAnimSegment853)
HAnimSegment854 = x3d.HAnimSegment()
HAnimSegment854.USE = "hanim_r_carpal_proximal_phalanx_5"

HAnimHumanoid23.segments.append(HAnimSegment854)
HAnimSegment855 = x3d.HAnimSegment()
HAnimSegment855.USE = "hanim_l_clavicle"

HAnimHumanoid23.segments.append(HAnimSegment855)
HAnimSegment856 = x3d.HAnimSegment()
HAnimSegment856.USE = "hanim_r_clavicle"

HAnimHumanoid23.segments.append(HAnimSegment856)
HAnimSegment857 = x3d.HAnimSegment()
HAnimSegment857.USE = "hanim_l_forearm"

HAnimHumanoid23.segments.append(HAnimSegment857)
HAnimSegment858 = x3d.HAnimSegment()
HAnimSegment858.USE = "hanim_r_forearm"

HAnimHumanoid23.segments.append(HAnimSegment858)
HAnimSegment859 = x3d.HAnimSegment()
HAnimSegment859.USE = "hanim_l_metacarpal_1"

HAnimHumanoid23.segments.append(HAnimSegment859)
HAnimSegment860 = x3d.HAnimSegment()
HAnimSegment860.USE = "hanim_r_metacarpal_1"

HAnimHumanoid23.segments.append(HAnimSegment860)
HAnimSegment861 = x3d.HAnimSegment()
HAnimSegment861.USE = "hanim_l_metacarpal_2"

HAnimHumanoid23.segments.append(HAnimSegment861)
HAnimSegment862 = x3d.HAnimSegment()
HAnimSegment862.USE = "hanim_r_metacarpal_2"

HAnimHumanoid23.segments.append(HAnimSegment862)
HAnimSegment863 = x3d.HAnimSegment()
HAnimSegment863.USE = "hanim_l_metacarpal_3"

HAnimHumanoid23.segments.append(HAnimSegment863)
HAnimSegment864 = x3d.HAnimSegment()
HAnimSegment864.USE = "hanim_r_metacarpal_3"

HAnimHumanoid23.segments.append(HAnimSegment864)
HAnimSegment865 = x3d.HAnimSegment()
HAnimSegment865.USE = "hanim_l_metacarpal_4"

HAnimHumanoid23.segments.append(HAnimSegment865)
HAnimSegment866 = x3d.HAnimSegment()
HAnimSegment866.USE = "hanim_r_metacarpal_4"

HAnimHumanoid23.segments.append(HAnimSegment866)
HAnimSegment867 = x3d.HAnimSegment()
HAnimSegment867.USE = "hanim_l_metacarpal_5"

HAnimHumanoid23.segments.append(HAnimSegment867)
HAnimSegment868 = x3d.HAnimSegment()
HAnimSegment868.USE = "hanim_r_metacarpal_5"

HAnimHumanoid23.segments.append(HAnimSegment868)
HAnimSegment869 = x3d.HAnimSegment()
HAnimSegment869.USE = "hanim_r_metatarsal_2"

HAnimHumanoid23.segments.append(HAnimSegment869)
HAnimSegment870 = x3d.HAnimSegment()
HAnimSegment870.USE = "hanim_l_metatarsal_2"

HAnimHumanoid23.segments.append(HAnimSegment870)
HAnimSegment871 = x3d.HAnimSegment()
HAnimSegment871.USE = "hanim_l_scapula"

HAnimHumanoid23.segments.append(HAnimSegment871)
HAnimSegment872 = x3d.HAnimSegment()
HAnimSegment872.USE = "hanim_r_scapula"

HAnimHumanoid23.segments.append(HAnimSegment872)
HAnimSegment873 = x3d.HAnimSegment()
HAnimSegment873.USE = "hanim_l_talus"

HAnimHumanoid23.segments.append(HAnimSegment873)
HAnimSegment874 = x3d.HAnimSegment()
HAnimSegment874.USE = "hanim_r_talus"

HAnimHumanoid23.segments.append(HAnimSegment874)
HAnimSegment875 = x3d.HAnimSegment()
HAnimSegment875.USE = "hanim_l_tarsal_distal_phalanx_2"

HAnimHumanoid23.segments.append(HAnimSegment875)
HAnimSegment876 = x3d.HAnimSegment()
HAnimSegment876.USE = "hanim_r_tarsal_distal_phalanx_2"

HAnimHumanoid23.segments.append(HAnimSegment876)
HAnimSegment877 = x3d.HAnimSegment()
HAnimSegment877.USE = "hanim_l_tarsal_proximal_phalanx_2"

HAnimHumanoid23.segments.append(HAnimSegment877)
HAnimSegment878 = x3d.HAnimSegment()
HAnimSegment878.USE = "hanim_r_tarsal_proximal_phalanx_2"

HAnimHumanoid23.segments.append(HAnimSegment878)
HAnimSegment879 = x3d.HAnimSegment()
HAnimSegment879.USE = "hanim_l_thigh"

HAnimHumanoid23.segments.append(HAnimSegment879)
HAnimSegment880 = x3d.HAnimSegment()
HAnimSegment880.USE = "hanim_r_thigh"

HAnimHumanoid23.segments.append(HAnimSegment880)
HAnimSegment881 = x3d.HAnimSegment()
HAnimSegment881.USE = "hanim_l_upperarm"

HAnimHumanoid23.segments.append(HAnimSegment881)
HAnimSegment882 = x3d.HAnimSegment()
HAnimSegment882.USE = "hanim_r_upperarm"

HAnimHumanoid23.segments.append(HAnimSegment882)

Scene19.children.append(HAnimHumanoid23)

X3D0.Scene = Scene19
f = open("././JinLOA2_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
