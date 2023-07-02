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
meta3.content = "JinLOA3.x3d"

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
meta8.content = "27 January 2023"

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
meta13.content = "https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Characters/JinLOA3.x3d"

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
WorldInfo20.title = "JinLOA3.x3d"

Scene19.children.append(WorldInfo20)
NavigationInfo21 = x3d.NavigationInfo()
NavigationInfo21.speed = 1.5

Scene19.children.append(NavigationInfo21)
Viewpoint22 = x3d.Viewpoint()
Viewpoint22.centerOfRotation = [0,1,0]
Viewpoint22.description = "JinLOA3"
Viewpoint22.position = [0,1,3]

Scene19.children.append(Viewpoint22)
HAnimHumanoid23 = x3d.HAnimHumanoid()
HAnimHumanoid23.name = "JinLOA3"
HAnimHumanoid23.DEF = "hanim_JinLOA3"
HAnimHumanoid23.loa = 3
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
ImageTexture37.DEF = "JinLOA3TextureAtlas"
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
ImageTexture47.USE = "JinLOA3TextureAtlas"

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
ImageTexture57.USE = "JinLOA3TextureAtlas"

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
ImageTexture67.USE = "JinLOA3TextureAtlas"

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
ImageTexture77.USE = "JinLOA3TextureAtlas"

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
ImageTexture87.USE = "JinLOA3TextureAtlas"

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
ImageTexture97.USE = "JinLOA3TextureAtlas"

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
ImageTexture107.USE = "JinLOA3TextureAtlas"

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
ImageTexture117.USE = "JinLOA3TextureAtlas"

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
ImageTexture127.USE = "JinLOA3TextureAtlas"

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
ImageTexture137.USE = "JinLOA3TextureAtlas"

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
ImageTexture147.USE = "JinLOA3TextureAtlas"

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
ImageTexture157.USE = "JinLOA3TextureAtlas"

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
ImageTexture167.USE = "JinLOA3TextureAtlas"

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
ImageTexture177.USE = "JinLOA3TextureAtlas"

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
HAnimJoint181.name = "vl4"
HAnimJoint181.DEF = "hanim_vl4"
HAnimJoint181.center = [0,41.299999,-0.6117]
HAnimJoint181.ulimit = [0,0,0]
HAnimJoint181.llimit = [0,0,0]
HAnimSegment182 = x3d.HAnimSegment()
HAnimSegment182.name = "l4"
HAnimSegment182.DEF = "hanim_l4"
Transform183 = x3d.Transform()
Transform183.translation = [0,41.299999,-0.6117]
Shape184 = x3d.Shape()
Appearance185 = x3d.Appearance()
Material186 = x3d.Material()
Material186.diffuseColor = [0.588,0.588,0.588]

Appearance185.material = Material186
ImageTexture187 = x3d.ImageTexture()
ImageTexture187.USE = "JinLOA3TextureAtlas"

Appearance185.texture = ImageTexture187

Shape184.appearance = Appearance185
IndexedFaceSet188 = x3d.IndexedFaceSet()
IndexedFaceSet188.coordIndex = [11,6,0,-1,0,3,11,-1,7,1,0,-1,0,6,7,-1,9,8,2,-1,2,4,9,-1,10,9,4,-1,4,5,10,-1,10,5,1,-1,1,7,10,-1,25,11,3,-1,3,26,25,-1,2,8,12,-1,12,27,2,-1,13,16,15,-1,15,14,13,-1,17,14,15,-1,15,18,17,-1,19,22,21,-1,21,20,19,-1,23,24,22,-1,22,19,23,-1,23,17,18,-1,18,24,23,-1,25,26,16,-1,16,13,25,-1,21,27,12,-1,12,20,21,-1,29,30,31,-1,31,32,33,-1,29,31,33,-1,34,35,36,-1,33,34,36,-1,36,37,38,-1,38,39,40,-1,36,38,40,-1,33,36,40,-1,29,33,40,-1,29,40,41,-1,29,41,28,-1,44,45,46,-1,46,47,48,-1,44,46,48,-1,48,49,50,-1,48,50,51,-1,51,52,53,-1,53,54,55,-1,51,53,55,-1,48,51,55,-1,44,48,55,-1,43,44,55,-1,43,55,42,-1,3,0,29,-1,29,28,3,-1,0,1,30,-1,30,29,0,-1,1,5,31,-1,31,30,1,-1,5,4,32,-1,32,31,5,-1,4,2,33,-1,33,32,4,-1,2,27,34,-1,34,33,2,-1,27,21,35,-1,35,34,27,-1,21,22,36,-1,36,35,21,-1,22,24,37,-1,37,36,22,-1,24,18,38,-1,38,37,24,-1,18,15,39,-1,39,38,18,-1,15,16,40,-1,40,39,15,-1,16,26,41,-1,41,40,16,-1,26,3,28,-1,28,41,26,-1,6,11,43,-1,43,42,6,-1,11,25,44,-1,44,43,11,-1,25,13,45,-1,45,44,25,-1,13,14,46,-1,46,45,13,-1,14,17,47,-1,47,46,14,-1,17,23,48,-1,48,47,17,-1,23,19,49,-1,49,48,23,-1,19,20,50,-1,50,49,19,-1,20,12,51,-1,51,50,20,-1,12,8,52,-1,52,51,12,-1,8,9,53,-1,53,52,8,-1,9,10,54,-1,54,53,9,-1,10,7,55,-1,55,54,10,-1,7,6,42,-1,42,55,7,-1]
IndexedFaceSet188.creaseAngle = 3.14159
IndexedFaceSet188.texCoordIndex = [15,9,0,-1,0,4,15,-1,10,1,0,-1,0,9,10,-1,13,12,2,-1,2,5,13,-1,14,13,5,-1,5,6,14,-1,14,6,1,-1,1,10,14,-1,17,15,4,-1,4,7,17,-1,3,11,16,-1,16,8,3,-1,18,21,20,-1,20,19,18,-1,22,19,20,-1,20,23,22,-1,24,27,26,-1,26,25,24,-1,28,29,27,-1,27,24,28,-1,28,22,23,-1,23,29,28,-1,30,31,21,-1,21,18,30,-1,32,35,34,-1,34,33,32,-1,37,38,39,-1,39,40,41,-1,37,39,41,-1,42,43,44,-1,41,42,44,-1,44,45,46,-1,46,47,48,-1,44,46,48,-1,41,44,48,-1,37,41,48,-1,37,48,49,-1,37,49,36,-1,52,53,54,-1,54,55,56,-1,52,54,56,-1,56,57,58,-1,56,58,59,-1,59,60,61,-1,61,62,63,-1,59,61,63,-1,56,59,63,-1,52,56,63,-1,51,52,63,-1,51,63,50,-1,4,0,37,-1,37,36,4,-1,0,1,38,-1,38,37,0,-1,1,6,39,-1,39,38,1,-1,6,5,40,-1,40,39,6,-1,5,2,41,-1,41,40,5,-1,3,8,42,-1,42,41,3,-1,35,32,43,-1,43,42,35,-1,26,27,44,-1,44,43,26,-1,27,29,45,-1,45,44,27,-1,29,23,46,-1,46,45,29,-1,23,20,47,-1,47,46,23,-1,20,21,48,-1,48,47,20,-1,21,31,49,-1,49,48,21,-1,7,4,36,-1,36,49,7,-1,9,15,51,-1,51,50,9,-1,15,17,52,-1,52,51,15,-1,30,18,53,-1,53,52,30,-1,18,19,54,-1,54,53,18,-1,19,22,55,-1,55,54,19,-1,22,28,56,-1,56,55,22,-1,28,24,57,-1,57,56,28,-1,24,25,58,-1,58,57,24,-1,33,34,59,-1,59,58,33,-1,16,11,60,-1,60,59,16,-1,12,13,61,-1,61,60,12,-1,13,14,62,-1,62,61,13,-1,14,10,63,-1,63,62,14,-1,10,9,50,-1,50,63,10,-1]
Coordinate189 = x3d.Coordinate()

IndexedFaceSet188.coord = Coordinate189
TextureCoordinate190 = x3d.TextureCoordinate()

IndexedFaceSet188.texCoord = TextureCoordinate190

Shape184.geometry = IndexedFaceSet188

Transform183.children.append(Shape184)

HAnimSegment182.children.append(Transform183)

HAnimJoint181.children.append(HAnimSegment182)
HAnimJoint191 = x3d.HAnimJoint()
HAnimJoint191.name = "vl3"
HAnimJoint191.DEF = "hanim_vl3"
HAnimJoint191.center = [0,42.029999,-0.6117]
HAnimJoint191.ulimit = [0,0,0]
HAnimJoint191.llimit = [0,0,0]
HAnimSegment192 = x3d.HAnimSegment()
HAnimSegment192.name = "l3"
HAnimSegment192.DEF = "hanim_l3"
Transform193 = x3d.Transform()
Transform193.translation = [0,42.029999,-0.6117]
Shape194 = x3d.Shape()
Appearance195 = x3d.Appearance()
Material196 = x3d.Material()
Material196.diffuseColor = [0.588,0.588,0.588]

Appearance195.material = Material196
ImageTexture197 = x3d.ImageTexture()
ImageTexture197.USE = "JinLOA3TextureAtlas"

Appearance195.texture = ImageTexture197

Shape194.appearance = Appearance195
IndexedFaceSet198 = x3d.IndexedFaceSet()
IndexedFaceSet198.coordIndex = [1,8,15,-1,15,16,1,-1,0,4,9,-1,9,6,0,-1,7,5,0,-1,0,6,7,-1,1,2,10,-1,10,8,1,-1,2,3,11,-1,11,10,2,-1,11,3,5,-1,5,7,11,-1,4,27,12,-1,12,9,4,-1,13,16,15,-1,15,14,13,-1,18,17,20,-1,20,19,18,-1,21,17,18,-1,18,22,21,-1,13,14,24,-1,24,23,13,-1,23,24,26,-1,26,25,23,-1,26,21,22,-1,22,25,26,-1,19,20,12,-1,12,27,19,-1,29,30,31,-1,31,32,33,-1,29,31,33,-1,34,35,36,-1,33,34,36,-1,36,37,38,-1,38,39,40,-1,36,38,40,-1,33,36,40,-1,29,33,40,-1,29,40,41,-1,29,41,28,-1,44,45,46,-1,46,47,48,-1,44,46,48,-1,48,49,50,-1,48,50,51,-1,51,52,53,-1,53,54,55,-1,51,53,55,-1,48,51,55,-1,44,48,55,-1,43,44,55,-1,43,55,42,-1,4,0,29,-1,29,28,4,-1,0,5,30,-1,30,29,0,-1,5,3,31,-1,31,30,5,-1,3,2,32,-1,32,31,3,-1,2,1,33,-1,33,32,2,-1,1,16,34,-1,34,33,1,-1,16,13,35,-1,35,34,16,-1,13,23,36,-1,36,35,13,-1,23,25,37,-1,37,36,23,-1,25,22,38,-1,38,37,25,-1,22,18,39,-1,39,38,22,-1,18,19,40,-1,40,39,18,-1,19,27,41,-1,41,40,19,-1,27,4,28,-1,28,41,27,-1,6,9,43,-1,43,42,6,-1,9,12,44,-1,44,43,9,-1,12,20,45,-1,45,44,12,-1,20,17,46,-1,46,45,20,-1,17,21,47,-1,47,46,17,-1,21,26,48,-1,48,47,21,-1,26,24,49,-1,49,48,26,-1,24,14,50,-1,50,49,24,-1,14,15,51,-1,51,50,14,-1,15,8,52,-1,52,51,15,-1,8,10,53,-1,53,52,8,-1,10,11,54,-1,54,53,10,-1,11,7,55,-1,55,54,11,-1,7,6,42,-1,42,55,7,-1]
IndexedFaceSet198.creaseAngle = 3.14159
IndexedFaceSet198.texCoordIndex = [4,11,17,-1,17,7,4,-1,0,1,13,-1,13,9,0,-1,10,2,0,-1,0,9,10,-1,3,5,14,-1,14,12,3,-1,5,6,15,-1,15,14,5,-1,15,6,2,-1,2,10,15,-1,1,8,16,-1,16,13,1,-1,18,21,20,-1,20,19,18,-1,23,22,25,-1,25,24,23,-1,26,22,23,-1,23,27,26,-1,29,28,31,-1,31,30,29,-1,30,31,33,-1,33,32,30,-1,33,26,27,-1,27,32,33,-1,24,25,35,-1,35,34,24,-1,37,38,39,-1,39,40,41,-1,37,39,41,-1,42,43,44,-1,41,42,44,-1,44,45,46,-1,46,47,48,-1,44,46,48,-1,41,44,48,-1,37,41,48,-1,37,48,49,-1,37,49,36,-1,52,53,54,-1,54,55,56,-1,52,54,56,-1,56,57,58,-1,56,58,59,-1,59,60,61,-1,61,62,63,-1,59,61,63,-1,56,59,63,-1,52,56,63,-1,51,52,63,-1,51,63,50,-1,1,0,37,-1,37,36,1,-1,0,2,38,-1,38,37,0,-1,2,6,39,-1,39,38,2,-1,6,5,40,-1,40,39,6,-1,5,3,41,-1,41,40,5,-1,4,7,42,-1,42,41,4,-1,21,18,43,-1,43,42,21,-1,29,30,44,-1,44,43,29,-1,30,32,45,-1,45,44,30,-1,32,27,46,-1,46,45,32,-1,27,23,47,-1,47,46,27,-1,23,24,48,-1,48,47,23,-1,24,34,49,-1,49,48,24,-1,8,1,36,-1,36,49,8,-1,9,13,51,-1,51,50,9,-1,13,16,52,-1,52,51,13,-1,35,25,53,-1,53,52,35,-1,25,22,54,-1,54,53,25,-1,22,26,55,-1,55,54,22,-1,26,33,56,-1,56,55,26,-1,33,31,57,-1,57,56,33,-1,31,28,58,-1,58,57,31,-1,19,20,59,-1,59,58,19,-1,17,11,60,-1,60,59,17,-1,12,14,61,-1,61,60,12,-1,14,15,62,-1,62,61,14,-1,15,10,63,-1,63,62,15,-1,10,9,50,-1,50,63,10,-1]
Coordinate199 = x3d.Coordinate()

IndexedFaceSet198.coord = Coordinate199
TextureCoordinate200 = x3d.TextureCoordinate()

IndexedFaceSet198.texCoord = TextureCoordinate200

Shape194.geometry = IndexedFaceSet198

Transform193.children.append(Shape194)

HAnimSegment192.children.append(Transform193)

HAnimJoint191.children.append(HAnimSegment192)
HAnimJoint201 = x3d.HAnimJoint()
HAnimJoint201.name = "vl2"
HAnimJoint201.DEF = "hanim_vl2"
HAnimJoint201.center = [0,42.759998,-0.6117]
HAnimJoint201.ulimit = [0,0,0]
HAnimJoint201.llimit = [0,0,0]
HAnimSegment202 = x3d.HAnimSegment()
HAnimSegment202.name = "l2"
HAnimSegment202.DEF = "hanim_l2"
Transform203 = x3d.Transform()
Transform203.translation = [0,42.759998,-0.6117]
Shape204 = x3d.Shape()
Appearance205 = x3d.Appearance()
Material206 = x3d.Material()
Material206.diffuseColor = [0.588,0.588,0.588]

Appearance205.material = Material206
ImageTexture207 = x3d.ImageTexture()
ImageTexture207.USE = "JinLOA3TextureAtlas"

Appearance205.texture = ImageTexture207

Shape204.appearance = Appearance205
IndexedFaceSet208 = x3d.IndexedFaceSet()
IndexedFaceSet208.coordIndex = [3,7,14,-1,14,15,3,-1,0,5,10,-1,10,6,0,-1,11,2,0,-1,0,6,11,-1,3,4,8,-1,8,7,3,-1,4,1,9,-1,9,8,4,-1,9,1,2,-1,2,11,9,-1,5,26,27,-1,27,10,5,-1,12,15,14,-1,14,13,12,-1,17,16,19,-1,19,18,17,-1,20,16,17,-1,17,21,20,-1,12,13,23,-1,23,22,12,-1,22,23,25,-1,25,24,22,-1,25,20,21,-1,21,24,25,-1,18,19,27,-1,27,26,18,-1,29,30,31,-1,31,32,33,-1,33,34,35,-1,31,33,35,-1,35,36,37,-1,37,38,39,-1,35,37,39,-1,31,35,39,-1,39,40,41,-1,31,39,41,-1,29,31,41,-1,29,41,28,-1,44,45,46,-1,46,47,48,-1,44,46,48,-1,48,49,50,-1,48,50,51,-1,51,52,53,-1,53,54,55,-1,51,53,55,-1,48,51,55,-1,44,48,55,-1,43,44,55,-1,43,55,42,-1,5,0,29,-1,29,28,5,-1,0,2,30,-1,30,29,0,-1,2,1,31,-1,31,30,2,-1,1,4,32,-1,32,31,1,-1,4,3,33,-1,33,32,4,-1,3,15,34,-1,34,33,3,-1,15,12,35,-1,35,34,15,-1,12,22,36,-1,36,35,12,-1,22,24,37,-1,37,36,22,-1,24,21,38,-1,38,37,24,-1,21,17,39,-1,39,38,21,-1,17,18,40,-1,40,39,17,-1,18,26,41,-1,41,40,18,-1,26,5,28,-1,28,41,26,-1,6,10,43,-1,43,42,6,-1,10,27,44,-1,44,43,10,-1,27,19,45,-1,45,44,27,-1,19,16,46,-1,46,45,19,-1,16,20,47,-1,47,46,16,-1,20,25,48,-1,48,47,20,-1,25,23,49,-1,49,48,25,-1,23,13,50,-1,50,49,23,-1,13,14,51,-1,51,50,13,-1,14,7,52,-1,52,51,14,-1,7,8,53,-1,53,52,7,-1,8,9,54,-1,54,53,8,-1,9,11,55,-1,55,54,9,-1,11,6,42,-1,42,55,11,-1]
IndexedFaceSet208.creaseAngle = 3.14159
IndexedFaceSet208.texCoordIndex = [6,10,16,-1,16,7,6,-1,1,0,14,-1,14,9,1,-1,15,2,1,-1,1,9,15,-1,4,3,12,-1,12,11,4,-1,3,5,13,-1,13,12,3,-1,13,5,2,-1,2,15,13,-1,0,8,17,-1,17,14,0,-1,18,21,20,-1,20,19,18,-1,23,22,25,-1,25,24,23,-1,26,22,23,-1,23,27,26,-1,29,28,31,-1,31,30,29,-1,30,31,33,-1,33,32,30,-1,33,26,27,-1,27,32,33,-1,24,25,35,-1,35,34,24,-1,37,38,39,-1,39,40,41,-1,41,42,43,-1,39,41,43,-1,43,44,45,-1,45,46,47,-1,43,45,47,-1,39,43,47,-1,47,48,49,-1,39,47,49,-1,37,39,49,-1,37,49,36,-1,52,53,54,-1,54,55,56,-1,52,54,56,-1,56,57,58,-1,56,58,59,-1,59,60,61,-1,61,62,63,-1,59,61,63,-1,56,59,63,-1,52,56,63,-1,51,52,63,-1,51,63,50,-1,0,1,37,-1,37,36,0,-1,1,2,38,-1,38,37,1,-1,2,5,39,-1,39,38,2,-1,5,3,40,-1,40,39,5,-1,3,4,41,-1,41,40,3,-1,6,7,42,-1,42,41,6,-1,21,18,43,-1,43,42,21,-1,29,30,44,-1,44,43,29,-1,30,32,45,-1,45,44,30,-1,32,27,46,-1,46,45,32,-1,27,23,47,-1,47,46,27,-1,23,24,48,-1,48,47,23,-1,24,34,49,-1,49,48,24,-1,8,0,36,-1,36,49,8,-1,9,14,51,-1,51,50,9,-1,14,17,52,-1,52,51,14,-1,35,25,53,-1,53,52,35,-1,25,22,54,-1,54,53,25,-1,22,26,55,-1,55,54,22,-1,26,33,56,-1,56,55,26,-1,33,31,57,-1,57,56,33,-1,31,28,58,-1,58,57,31,-1,19,20,59,-1,59,58,19,-1,16,10,60,-1,60,59,16,-1,11,12,61,-1,61,60,11,-1,12,13,62,-1,62,61,12,-1,13,15,63,-1,63,62,13,-1,15,9,50,-1,50,63,15,-1]
Coordinate209 = x3d.Coordinate()

IndexedFaceSet208.coord = Coordinate209
TextureCoordinate210 = x3d.TextureCoordinate()

IndexedFaceSet208.texCoord = TextureCoordinate210

Shape204.geometry = IndexedFaceSet208

Transform203.children.append(Shape204)

HAnimSegment202.children.append(Transform203)

HAnimJoint201.children.append(HAnimSegment202)
HAnimJoint211 = x3d.HAnimJoint()
HAnimJoint211.name = "vl1"
HAnimJoint211.DEF = "hanim_vl1"
HAnimJoint211.center = [0,43.52,-0.6117]
HAnimJoint211.ulimit = [0,0,0]
HAnimJoint211.llimit = [0,0,0]
HAnimSegment212 = x3d.HAnimSegment()
HAnimSegment212.name = "l1"
HAnimSegment212.DEF = "hanim_l1"
Transform213 = x3d.Transform()
Transform213.translation = [0,43.52,-0.6117]
Shape214 = x3d.Shape()
Appearance215 = x3d.Appearance()
Material216 = x3d.Material()
Material216.diffuseColor = [0.588,0.588,0.588]

Appearance215.material = Material216
ImageTexture217 = x3d.ImageTexture()
ImageTexture217.USE = "JinLOA3TextureAtlas"

Appearance215.texture = ImageTexture217

Shape214.appearance = Appearance215
IndexedFaceSet218 = x3d.IndexedFaceSet()
IndexedFaceSet218.coordIndex = [7,0,1,-1,1,14,7,-1,11,2,0,-1,0,7,11,-1,13,12,3,-1,3,4,13,-1,8,5,2,-1,2,11,8,-1,14,1,6,-1,6,9,14,-1,8,13,4,-1,4,5,8,-1,12,10,27,-1,27,3,12,-1,16,15,18,-1,18,17,16,-1,19,16,17,-1,17,20,19,-1,21,24,23,-1,23,22,21,-1,25,19,20,-1,20,26,25,-1,15,9,6,-1,6,18,15,-1,25,26,24,-1,24,21,25,-1,22,23,27,-1,27,10,22,-1,29,30,31,-1,31,32,33,-1,33,34,35,-1,31,33,35,-1,35,36,37,-1,37,38,39,-1,35,37,39,-1,31,35,39,-1,39,40,41,-1,31,39,41,-1,29,31,41,-1,29,41,28,-1,44,45,46,-1,43,44,46,-1,46,47,48,-1,48,49,50,-1,46,48,50,-1,50,51,52,-1,52,53,54,-1,50,52,54,-1,46,50,54,-1,43,46,54,-1,43,54,55,-1,43,55,42,-1,1,0,29,-1,29,28,1,-1,0,2,30,-1,30,29,0,-1,2,5,31,-1,31,30,2,-1,5,4,32,-1,32,31,5,-1,4,3,33,-1,33,32,4,-1,3,27,34,-1,34,33,3,-1,27,23,35,-1,35,34,27,-1,23,24,36,-1,36,35,23,-1,24,26,37,-1,37,36,24,-1,26,20,38,-1,38,37,26,-1,20,17,39,-1,39,38,20,-1,17,18,40,-1,40,39,17,-1,18,6,41,-1,41,40,18,-1,6,1,28,-1,28,41,6,-1,7,14,43,-1,43,42,7,-1,14,9,44,-1,44,43,14,-1,9,15,45,-1,45,44,9,-1,15,16,46,-1,46,45,15,-1,16,19,47,-1,47,46,16,-1,19,25,48,-1,48,47,19,-1,25,21,49,-1,49,48,25,-1,21,22,50,-1,50,49,21,-1,22,10,51,-1,51,50,22,-1,10,12,52,-1,52,51,10,-1,12,13,53,-1,53,52,12,-1,13,8,54,-1,54,53,13,-1,8,11,55,-1,55,54,8,-1,11,7,42,-1,42,55,11,-1]
IndexedFaceSet218.creaseAngle = 3.14159
IndexedFaceSet218.texCoordIndex = [9,0,1,-1,1,17,9,-1,13,2,0,-1,0,9,13,-1,16,15,3,-1,3,5,16,-1,10,6,2,-1,2,13,10,-1,17,1,8,-1,8,11,17,-1,10,16,5,-1,5,6,10,-1,14,12,7,-1,7,4,14,-1,19,18,21,-1,21,20,19,-1,22,19,20,-1,20,23,22,-1,24,27,26,-1,26,25,24,-1,28,22,23,-1,23,29,28,-1,18,30,31,-1,31,21,18,-1,28,29,27,-1,27,24,28,-1,33,32,35,-1,35,34,33,-1,37,38,39,-1,39,40,41,-1,41,42,43,-1,39,41,43,-1,43,44,45,-1,45,46,47,-1,43,45,47,-1,39,43,47,-1,47,48,49,-1,39,47,49,-1,37,39,49,-1,37,49,36,-1,52,53,54,-1,51,52,54,-1,54,55,56,-1,56,57,58,-1,54,56,58,-1,58,59,60,-1,60,61,62,-1,58,60,62,-1,54,58,62,-1,51,54,62,-1,51,62,63,-1,51,63,50,-1,1,0,37,-1,37,36,1,-1,0,2,38,-1,38,37,0,-1,2,6,39,-1,39,38,2,-1,6,5,40,-1,40,39,6,-1,5,3,41,-1,41,40,5,-1,4,7,42,-1,42,41,4,-1,35,32,43,-1,43,42,35,-1,26,27,44,-1,44,43,26,-1,27,29,45,-1,45,44,27,-1,29,23,46,-1,46,45,29,-1,23,20,47,-1,47,46,23,-1,20,21,48,-1,48,47,20,-1,21,31,49,-1,49,48,21,-1,8,1,36,-1,36,49,8,-1,9,17,51,-1,51,50,9,-1,17,11,52,-1,52,51,17,-1,30,18,53,-1,53,52,30,-1,18,19,54,-1,54,53,18,-1,19,22,55,-1,55,54,19,-1,22,28,56,-1,56,55,22,-1,28,24,57,-1,57,56,28,-1,24,25,58,-1,58,57,24,-1,33,34,59,-1,59,58,33,-1,12,14,60,-1,60,59,12,-1,15,16,61,-1,61,60,15,-1,16,10,62,-1,62,61,16,-1,10,13,63,-1,63,62,10,-1,13,9,50,-1,50,63,13,-1]
Coordinate219 = x3d.Coordinate()

IndexedFaceSet218.coord = Coordinate219
TextureCoordinate220 = x3d.TextureCoordinate()

IndexedFaceSet218.texCoord = TextureCoordinate220

Shape214.geometry = IndexedFaceSet218

Transform213.children.append(Shape214)

HAnimSegment212.children.append(Transform213)

HAnimJoint211.children.append(HAnimSegment212)
HAnimJoint221 = x3d.HAnimJoint()
HAnimJoint221.name = "vt12"
HAnimJoint221.DEF = "hanim_vt12"
HAnimJoint221.center = [0,44.57,-0.6117]
HAnimJoint221.ulimit = [0,0,0]
HAnimJoint221.llimit = [0,0,0]
HAnimSegment222 = x3d.HAnimSegment()
HAnimSegment222.name = "t12"
HAnimSegment222.DEF = "hanim_t12"
Transform223 = x3d.Transform()
Transform223.translation = [0,44.57,-0.6117]
Shape224 = x3d.Shape()
Appearance225 = x3d.Appearance()
Material226 = x3d.Material()
Material226.diffuseColor = [0.588,0.588,0.588]

Appearance225.material = Material226
ImageTexture227 = x3d.ImageTexture()
ImageTexture227.USE = "JinLOA3TextureAtlas"

Appearance225.texture = ImageTexture227

Shape224.appearance = Appearance225
IndexedFaceSet228 = x3d.IndexedFaceSet()
IndexedFaceSet228.coordIndex = [4,5,11,-1,11,10,4,-1,17,3,9,-1,9,20,17,-1,6,0,2,-1,2,7,6,-1,8,1,0,-1,0,6,8,-1,3,4,10,-1,10,9,3,-1,5,1,8,-1,8,11,5,-1,2,27,12,-1,12,7,2,-1,13,16,15,-1,15,14,13,-1,17,20,19,-1,19,18,17,-1,21,24,23,-1,23,22,21,-1,25,21,22,-1,22,26,25,-1,18,19,16,-1,16,13,18,-1,14,15,25,-1,25,26,14,-1,23,24,12,-1,12,27,23,-1,29,30,31,-1,31,32,33,-1,33,34,35,-1,31,33,35,-1,35,36,37,-1,37,38,39,-1,35,37,39,-1,31,35,39,-1,39,40,41,-1,31,39,41,-1,29,31,41,-1,29,41,28,-1,44,45,46,-1,43,44,46,-1,46,47,48,-1,48,49,50,-1,46,48,50,-1,50,51,52,-1,52,53,54,-1,50,52,54,-1,46,50,54,-1,43,46,54,-1,43,54,55,-1,43,55,42,-1,2,0,29,-1,29,28,2,-1,0,1,30,-1,30,29,0,-1,1,5,31,-1,31,30,1,-1,5,4,32,-1,32,31,5,-1,4,3,33,-1,33,32,4,-1,3,17,34,-1,34,33,3,-1,17,18,35,-1,35,34,17,-1,18,13,36,-1,36,35,18,-1,13,14,37,-1,37,36,13,-1,14,26,38,-1,38,37,14,-1,26,22,39,-1,39,38,26,-1,22,23,40,-1,40,39,22,-1,23,27,41,-1,41,40,23,-1,27,2,28,-1,28,41,27,-1,6,7,43,-1,43,42,6,-1,7,12,44,-1,44,43,7,-1,12,24,45,-1,45,44,12,-1,24,21,46,-1,46,45,24,-1,21,25,47,-1,47,46,21,-1,25,15,48,-1,48,47,25,-1,15,16,49,-1,49,48,15,-1,16,19,50,-1,50,49,16,-1,19,20,51,-1,51,50,19,-1,20,9,52,-1,52,51,20,-1,9,10,53,-1,53,52,9,-1,10,11,54,-1,54,53,10,-1,11,8,55,-1,55,54,11,-1,8,6,42,-1,42,55,8,-1]
IndexedFaceSet228.creaseAngle = 3.14159
IndexedFaceSet228.texCoordIndex = [5,6,15,-1,15,14,5,-1,7,4,12,-1,12,16,7,-1,9,0,2,-1,2,10,9,-1,11,1,0,-1,0,9,11,-1,3,5,14,-1,14,13,3,-1,6,1,11,-1,11,15,6,-1,2,8,17,-1,17,10,2,-1,18,21,20,-1,20,19,18,-1,22,25,24,-1,24,23,22,-1,26,29,28,-1,28,27,26,-1,30,26,27,-1,27,31,30,-1,33,32,21,-1,21,18,33,-1,19,20,30,-1,30,31,19,-1,28,29,35,-1,35,34,28,-1,37,38,39,-1,39,40,41,-1,41,42,43,-1,39,41,43,-1,43,44,45,-1,45,46,47,-1,43,45,47,-1,39,43,47,-1,47,48,49,-1,39,47,49,-1,37,39,49,-1,37,49,36,-1,52,53,54,-1,51,52,54,-1,54,55,56,-1,56,57,58,-1,54,56,58,-1,58,59,60,-1,60,61,62,-1,58,60,62,-1,54,58,62,-1,51,54,62,-1,51,62,63,-1,51,63,50,-1,2,0,37,-1,37,36,2,-1,0,1,38,-1,38,37,0,-1,1,6,39,-1,39,38,1,-1,6,5,40,-1,40,39,6,-1,5,3,41,-1,41,40,5,-1,4,7,42,-1,42,41,4,-1,22,23,43,-1,43,42,22,-1,33,18,44,-1,44,43,33,-1,18,19,45,-1,45,44,18,-1,19,31,46,-1,46,45,19,-1,31,27,47,-1,47,46,31,-1,27,28,48,-1,48,47,27,-1,28,34,49,-1,49,48,28,-1,8,2,36,-1,36,49,8,-1,9,10,51,-1,51,50,9,-1,10,17,52,-1,52,51,10,-1,35,29,53,-1,53,52,35,-1,29,26,54,-1,54,53,29,-1,26,30,55,-1,55,54,26,-1,30,20,56,-1,56,55,30,-1,20,21,57,-1,57,56,20,-1,21,32,58,-1,58,57,21,-1,24,25,59,-1,59,58,24,-1,16,12,60,-1,60,59,16,-1,13,14,61,-1,61,60,13,-1,14,15,62,-1,62,61,14,-1,15,11,63,-1,63,62,15,-1,11,9,50,-1,50,63,11,-1]
Coordinate229 = x3d.Coordinate()

IndexedFaceSet228.coord = Coordinate229
TextureCoordinate230 = x3d.TextureCoordinate()

IndexedFaceSet228.texCoord = TextureCoordinate230

Shape224.geometry = IndexedFaceSet228

Transform223.children.append(Shape224)

HAnimSegment222.children.append(Transform223)

HAnimJoint221.children.append(HAnimSegment222)
HAnimJoint231 = x3d.HAnimJoint()
HAnimJoint231.name = "vt11"
HAnimJoint231.DEF = "hanim_vt11"
HAnimJoint231.center = [0,45.610001,-0.6117]
HAnimJoint231.ulimit = [0,0,0]
HAnimJoint231.llimit = [0,0,0]
HAnimSegment232 = x3d.HAnimSegment()
HAnimSegment232.name = "t11"
HAnimSegment232.DEF = "hanim_t11"
Transform233 = x3d.Transform()
Transform233.translation = [0,45.610001,-0.6117]
Shape234 = x3d.Shape()
Appearance235 = x3d.Appearance()
Material236 = x3d.Material()
Material236.diffuseColor = [0.588,0.588,0.588]

Appearance235.material = Material236
ImageTexture237 = x3d.ImageTexture()
ImageTexture237.USE = "JinLOA3TextureAtlas"

Appearance235.texture = ImageTexture237

Shape234.appearance = Appearance235
IndexedFaceSet238 = x3d.IndexedFaceSet()
IndexedFaceSet238.coordIndex = [4,3,10,-1,10,12,4,-1,5,4,12,-1,12,13,5,-1,5,13,9,-1,9,1,5,-1,6,11,14,-1,14,7,6,-1,7,2,0,-1,0,6,7,-1,11,6,0,-1,0,8,11,-1,3,28,29,-1,29,10,3,-1,8,0,1,-1,1,9,8,-1,15,18,17,-1,17,16,15,-1,19,20,18,-1,18,15,19,-1,19,21,22,-1,22,20,19,-1,23,7,14,-1,14,24,23,-1,7,23,25,-1,25,26,7,-1,24,27,25,-1,25,23,24,-1,16,17,29,-1,29,28,16,-1,27,22,21,-1,21,25,27,-1,32,33,34,-1,31,32,34,-1,34,35,36,-1,36,37,38,-1,34,36,38,-1,38,39,40,-1,40,41,42,-1,38,40,42,-1,34,38,42,-1,31,34,42,-1,31,42,43,-1,31,43,30,-1,45,46,47,-1,47,48,49,-1,49,50,51,-1,47,49,51,-1,51,52,53,-1,53,54,55,-1,51,53,55,-1,47,51,55,-1,55,56,57,-1,47,55,57,-1,45,47,57,-1,45,57,44,-1,0,2,31,-1,31,30,0,-1,2,7,32,-1,32,31,2,-1,7,26,33,-1,33,32,7,-1,26,25,34,-1,34,33,26,-1,25,21,35,-1,35,34,25,-1,21,19,36,-1,36,35,21,-1,19,15,37,-1,37,36,19,-1,15,16,38,-1,38,37,15,-1,16,28,39,-1,39,38,16,-1,28,3,40,-1,40,39,28,-1,3,4,41,-1,41,40,3,-1,4,5,42,-1,42,41,4,-1,5,1,43,-1,43,42,5,-1,1,0,30,-1,30,43,1,-1,12,10,45,-1,45,44,12,-1,10,29,46,-1,46,45,10,-1,29,17,47,-1,47,46,29,-1,17,18,48,-1,48,47,17,-1,18,20,49,-1,49,48,18,-1,20,22,50,-1,50,49,20,-1,22,27,51,-1,51,50,22,-1,27,24,52,-1,52,51,27,-1,24,14,53,-1,53,52,24,-1,14,11,54,-1,54,53,14,-1,11,8,55,-1,55,54,11,-1,8,9,56,-1,56,55,8,-1,9,13,57,-1,57,56,9,-1,13,12,44,-1,44,57,13,-1]
IndexedFaceSet238.creaseAngle = 3.14159
IndexedFaceSet238.texCoordIndex = [6,5,14,-1,14,16,6,-1,7,6,16,-1,16,17,7,-1,7,17,12,-1,12,3,7,-1,8,15,18,-1,18,10,8,-1,10,0,1,-1,1,8,10,-1,15,8,2,-1,2,11,15,-1,4,9,19,-1,19,13,4,-1,11,2,3,-1,3,12,11,-1,20,23,22,-1,22,21,20,-1,24,25,23,-1,23,20,24,-1,24,26,27,-1,27,25,24,-1,29,28,31,-1,31,30,29,-1,28,29,32,-1,32,33,28,-1,30,35,34,-1,34,29,30,-1,37,36,39,-1,39,38,37,-1,35,27,26,-1,26,34,35,-1,42,43,44,-1,41,42,44,-1,44,45,46,-1,46,47,48,-1,44,46,48,-1,48,49,50,-1,50,51,52,-1,48,50,52,-1,44,48,52,-1,41,44,52,-1,41,52,53,-1,41,53,40,-1,55,56,57,-1,57,58,59,-1,59,60,61,-1,57,59,61,-1,61,62,63,-1,63,64,65,-1,61,63,65,-1,57,61,65,-1,65,66,67,-1,57,65,67,-1,55,57,67,-1,55,67,54,-1,1,0,41,-1,41,40,1,-1,0,10,42,-1,42,41,0,-1,28,33,43,-1,43,42,28,-1,33,32,44,-1,44,43,33,-1,34,26,45,-1,45,44,34,-1,26,24,46,-1,46,45,26,-1,24,20,47,-1,47,46,24,-1,20,21,48,-1,48,47,20,-1,37,38,49,-1,49,48,37,-1,9,4,50,-1,50,49,9,-1,5,6,51,-1,51,50,5,-1,6,7,52,-1,52,51,6,-1,7,3,53,-1,53,52,7,-1,3,2,40,-1,40,53,3,-1,16,14,55,-1,55,54,16,-1,13,19,56,-1,56,55,13,-1,39,36,57,-1,57,56,39,-1,22,23,58,-1,58,57,22,-1,23,25,59,-1,59,58,23,-1,25,27,60,-1,60,59,25,-1,27,35,61,-1,61,60,27,-1,35,30,62,-1,62,61,35,-1,30,31,63,-1,63,62,30,-1,18,15,64,-1,64,63,18,-1,15,11,65,-1,65,64,15,-1,11,12,66,-1,66,65,11,-1,12,17,67,-1,67,66,12,-1,17,16,54,-1,54,67,17,-1]
Coordinate239 = x3d.Coordinate()

IndexedFaceSet238.coord = Coordinate239
TextureCoordinate240 = x3d.TextureCoordinate()

IndexedFaceSet238.texCoord = TextureCoordinate240

Shape234.geometry = IndexedFaceSet238

Transform233.children.append(Shape234)

HAnimSegment232.children.append(Transform233)

HAnimJoint231.children.append(HAnimSegment232)
HAnimJoint241 = x3d.HAnimJoint()
HAnimJoint241.name = "vt10"
HAnimJoint241.DEF = "hanim_vt10"
HAnimJoint241.center = [0,46.369999,-0.6127]
HAnimJoint241.ulimit = [0,0,0]
HAnimJoint241.llimit = [0,0,0]
HAnimSegment242 = x3d.HAnimSegment()
HAnimSegment242.name = "t10"
HAnimSegment242.DEF = "hanim_t10"
Transform243 = x3d.Transform()
Transform243.translation = [0,46.369999,-0.6127]
Shape244 = x3d.Shape()
Appearance245 = x3d.Appearance()
Material246 = x3d.Material()
Material246.diffuseColor = [0.588,0.588,0.588]

Appearance245.material = Material246
ImageTexture247 = x3d.ImageTexture()
ImageTexture247.USE = "JinLOA3TextureAtlas"

Appearance245.texture = ImageTexture247

Shape244.appearance = Appearance245
IndexedFaceSet248 = x3d.IndexedFaceSet()
IndexedFaceSet248.coordIndex = [11,7,4,-1,4,2,11,-1,7,8,5,-1,5,4,7,-1,8,10,1,-1,1,5,8,-1,3,6,12,-1,12,23,3,-1,6,3,0,-1,0,9,6,-1,2,26,27,-1,27,11,2,-1,0,1,10,-1,10,9,0,-1,14,13,16,-1,16,15,14,-1,15,16,18,-1,18,17,15,-1,17,18,20,-1,20,19,17,-1,21,23,12,-1,12,22,21,-1,22,25,24,-1,24,21,22,-1,13,14,27,-1,27,26,13,-1,24,25,19,-1,19,20,24,-1,29,30,31,-1,31,32,33,-1,29,31,33,-1,34,35,36,-1,33,34,36,-1,36,37,38,-1,38,39,40,-1,36,38,40,-1,33,36,40,-1,29,33,40,-1,29,40,41,-1,29,41,28,-1,44,45,46,-1,46,47,48,-1,48,49,50,-1,46,48,50,-1,50,51,52,-1,52,53,54,-1,50,52,54,-1,54,55,42,-1,50,54,42,-1,46,50,42,-1,44,46,42,-1,43,44,42,-1,2,4,29,-1,29,28,2,-1,4,5,30,-1,30,29,4,-1,5,1,31,-1,31,30,5,-1,1,0,32,-1,32,31,1,-1,0,3,33,-1,33,32,0,-1,3,23,34,-1,34,33,3,-1,23,21,35,-1,35,34,23,-1,21,24,36,-1,36,35,21,-1,24,20,37,-1,37,36,24,-1,20,18,38,-1,38,37,20,-1,18,16,39,-1,39,38,18,-1,16,13,40,-1,40,39,16,-1,13,26,41,-1,41,40,13,-1,26,2,28,-1,28,41,26,-1,6,9,43,-1,43,42,6,-1,9,10,44,-1,44,43,9,-1,10,8,45,-1,45,44,10,-1,8,7,46,-1,46,45,8,-1,7,11,47,-1,47,46,7,-1,11,27,48,-1,48,47,11,-1,27,14,49,-1,49,48,27,-1,14,15,50,-1,50,49,14,-1,15,17,51,-1,51,50,15,-1,17,19,52,-1,52,51,17,-1,19,25,53,-1,53,52,19,-1,25,22,54,-1,54,53,25,-1,22,12,55,-1,55,54,22,-1,12,6,42,-1,42,55,12,-1]
IndexedFaceSet248.creaseAngle = 3.14159
IndexedFaceSet248.texCoordIndex = [15,10,5,-1,5,2,15,-1,10,11,6,-1,6,5,10,-1,11,14,1,-1,1,6,11,-1,4,9,17,-1,17,7,4,-1,9,4,0,-1,0,13,9,-1,3,8,12,-1,12,16,3,-1,0,1,14,-1,14,13,0,-1,19,18,21,-1,21,20,19,-1,20,21,23,-1,23,22,20,-1,22,23,25,-1,25,24,22,-1,26,29,28,-1,28,27,26,-1,27,31,30,-1,30,26,27,-1,33,32,35,-1,35,34,33,-1,30,31,24,-1,24,25,30,-1,37,38,39,-1,39,40,41,-1,37,39,41,-1,42,43,44,-1,41,42,44,-1,44,45,46,-1,46,47,48,-1,44,46,48,-1,41,44,48,-1,37,41,48,-1,37,48,49,-1,37,49,36,-1,52,53,54,-1,54,55,56,-1,56,57,58,-1,54,56,58,-1,58,59,60,-1,60,61,62,-1,58,60,62,-1,62,63,50,-1,58,62,50,-1,54,58,50,-1,52,54,50,-1,51,52,50,-1,2,5,37,-1,37,36,2,-1,5,6,38,-1,38,37,5,-1,6,1,39,-1,39,38,6,-1,1,0,40,-1,40,39,1,-1,0,4,41,-1,41,40,0,-1,4,7,42,-1,42,41,4,-1,29,26,43,-1,43,42,29,-1,26,30,44,-1,44,43,26,-1,30,25,45,-1,45,44,30,-1,25,23,46,-1,46,45,25,-1,23,21,47,-1,47,46,23,-1,21,18,48,-1,48,47,21,-1,33,34,49,-1,49,48,33,-1,8,3,36,-1,36,49,8,-1,9,13,51,-1,51,50,9,-1,13,14,52,-1,52,51,13,-1,14,11,53,-1,53,52,14,-1,11,10,54,-1,54,53,11,-1,10,15,55,-1,55,54,10,-1,16,12,56,-1,56,55,16,-1,35,32,57,-1,57,56,35,-1,19,20,58,-1,58,57,19,-1,20,22,59,-1,59,58,20,-1,22,24,60,-1,60,59,22,-1,24,31,61,-1,61,60,24,-1,31,27,62,-1,62,61,31,-1,27,28,63,-1,63,62,27,-1,17,9,50,-1,50,63,17,-1]
Coordinate249 = x3d.Coordinate()

IndexedFaceSet248.coord = Coordinate249
TextureCoordinate250 = x3d.TextureCoordinate()

IndexedFaceSet248.texCoord = TextureCoordinate250

Shape244.geometry = IndexedFaceSet248

Transform243.children.append(Shape244)

HAnimSegment242.children.append(Transform243)

HAnimJoint241.children.append(HAnimSegment242)
HAnimJoint251 = x3d.HAnimJoint()
HAnimJoint251.name = "vt9"
HAnimJoint251.DEF = "hanim_vt9"
HAnimJoint251.center = [0,47.029999,-0.6117]
HAnimJoint251.ulimit = [0,0,0]
HAnimJoint251.llimit = [0,0,0]
HAnimSegment252 = x3d.HAnimSegment()
HAnimSegment252.name = "t9"
HAnimSegment252.DEF = "hanim_t9"
Transform253 = x3d.Transform()
Transform253.translation = [0,47.029999,-0.6117]
Shape254 = x3d.Shape()
Appearance255 = x3d.Appearance()
Material256 = x3d.Material()
Material256.diffuseColor = [0.588,0.588,0.588]

Appearance255.material = Material256
ImageTexture257 = x3d.ImageTexture()
ImageTexture257.USE = "JinLOA3TextureAtlas"

Appearance255.texture = ImageTexture257

Shape254.appearance = Appearance255
IndexedFaceSet258 = x3d.IndexedFaceSet()
IndexedFaceSet258.coordIndex = [7,0,3,-1,3,10,7,-1,5,20,21,-1,21,12,5,-1,3,4,11,-1,11,10,3,-1,12,8,1,-1,1,5,12,-1,8,9,2,-1,2,1,8,-1,9,11,4,-1,4,2,9,-1,0,7,13,-1,13,6,0,-1,14,17,16,-1,16,15,14,-1,19,18,21,-1,21,20,19,-1,16,17,23,-1,23,22,16,-1,18,19,25,-1,25,24,18,-1,24,25,27,-1,27,26,24,-1,26,27,22,-1,22,23,26,-1,15,6,13,-1,13,14,15,-1,30,31,32,-1,32,33,34,-1,34,35,36,-1,32,34,36,-1,36,37,38,-1,38,39,40,-1,36,38,40,-1,40,41,28,-1,36,40,28,-1,32,36,28,-1,30,32,28,-1,29,30,28,-1,43,44,45,-1,45,46,47,-1,43,45,47,-1,47,48,49,-1,47,49,50,-1,50,51,52,-1,52,53,54,-1,50,52,54,-1,47,50,54,-1,43,47,54,-1,43,54,55,-1,43,55,42,-1,3,0,29,-1,29,28,3,-1,0,6,30,-1,30,29,0,-1,6,15,31,-1,31,30,6,-1,15,16,32,-1,32,31,15,-1,16,22,33,-1,33,32,16,-1,22,27,34,-1,34,33,22,-1,27,25,35,-1,35,34,27,-1,25,19,36,-1,36,35,25,-1,19,20,37,-1,37,36,19,-1,20,5,38,-1,38,37,20,-1,5,1,39,-1,39,38,5,-1,1,2,40,-1,40,39,1,-1,2,4,41,-1,41,40,2,-1,4,3,28,-1,28,41,4,-1,8,12,43,-1,43,42,8,-1,12,21,44,-1,44,43,12,-1,21,18,45,-1,45,44,21,-1,18,24,46,-1,46,45,18,-1,24,26,47,-1,47,46,24,-1,26,23,48,-1,48,47,26,-1,23,17,49,-1,49,48,23,-1,17,14,50,-1,50,49,17,-1,14,13,51,-1,51,50,14,-1,13,7,52,-1,52,51,13,-1,7,10,53,-1,53,52,7,-1,10,11,54,-1,54,53,10,-1,11,9,55,-1,55,54,11,-1,9,8,42,-1,42,55,9,-1]
IndexedFaceSet258.creaseAngle = 3.14159
IndexedFaceSet258.texCoordIndex = [9,0,4,-1,4,12,9,-1,7,3,17,-1,17,15,7,-1,4,5,13,-1,13,12,4,-1,14,10,1,-1,1,6,14,-1,10,11,2,-1,2,1,10,-1,11,13,5,-1,5,2,11,-1,0,9,16,-1,16,8,0,-1,18,21,20,-1,20,19,18,-1,23,22,25,-1,25,24,23,-1,20,21,27,-1,27,26,20,-1,29,28,31,-1,31,30,29,-1,30,31,33,-1,33,32,30,-1,32,33,26,-1,26,27,32,-1,19,35,34,-1,34,18,19,-1,38,39,40,-1,40,41,42,-1,42,43,44,-1,40,42,44,-1,44,45,46,-1,46,47,48,-1,44,46,48,-1,48,49,36,-1,44,48,36,-1,40,44,36,-1,38,40,36,-1,37,38,36,-1,51,52,53,-1,53,54,55,-1,51,53,55,-1,55,56,57,-1,55,57,58,-1,58,59,60,-1,60,61,62,-1,58,60,62,-1,55,58,62,-1,51,55,62,-1,51,62,63,-1,51,63,50,-1,4,0,37,-1,37,36,4,-1,0,8,38,-1,38,37,0,-1,35,19,39,-1,39,38,35,-1,19,20,40,-1,40,39,19,-1,20,26,41,-1,41,40,20,-1,26,33,42,-1,42,41,26,-1,33,31,43,-1,43,42,33,-1,31,28,44,-1,44,43,31,-1,23,24,45,-1,45,44,23,-1,3,7,46,-1,46,45,3,-1,6,1,47,-1,47,46,6,-1,1,2,48,-1,48,47,1,-1,2,5,49,-1,49,48,2,-1,5,4,36,-1,36,49,5,-1,10,14,51,-1,51,50,10,-1,15,17,52,-1,52,51,15,-1,25,22,53,-1,53,52,25,-1,29,30,54,-1,54,53,29,-1,30,32,55,-1,55,54,30,-1,32,27,56,-1,56,55,32,-1,27,21,57,-1,57,56,27,-1,21,18,58,-1,58,57,21,-1,18,34,59,-1,59,58,18,-1,16,9,60,-1,60,59,16,-1,9,12,61,-1,61,60,9,-1,12,13,62,-1,62,61,12,-1,13,11,63,-1,63,62,13,-1,11,10,50,-1,50,63,11,-1]
Coordinate259 = x3d.Coordinate()

IndexedFaceSet258.coord = Coordinate259
TextureCoordinate260 = x3d.TextureCoordinate()

IndexedFaceSet258.texCoord = TextureCoordinate260

Shape254.geometry = IndexedFaceSet258

Transform253.children.append(Shape254)

HAnimSegment252.children.append(Transform253)

HAnimJoint251.children.append(HAnimSegment252)
HAnimJoint261 = x3d.HAnimJoint()
HAnimJoint261.name = "vt8"
HAnimJoint261.DEF = "hanim_vt8"
HAnimJoint261.center = [0,47.68,-0.6117]
HAnimJoint261.ulimit = [0,0,0]
HAnimJoint261.llimit = [0,0,0]
HAnimSegment262 = x3d.HAnimSegment()
HAnimSegment262.name = "t8"
HAnimSegment262.DEF = "hanim_t8"
Transform263 = x3d.Transform()
Transform263.translation = [0,47.68,-0.6117]
Shape264 = x3d.Shape()
Appearance265 = x3d.Appearance()
Material266 = x3d.Material()
Material266.diffuseColor = [0.588,0.588,0.588]

Appearance265.material = Material266
ImageTexture267 = x3d.ImageTexture()
ImageTexture267.USE = "JinLOA3TextureAtlas"

Appearance265.texture = ImageTexture267

Shape264.appearance = Appearance265
IndexedFaceSet268 = x3d.IndexedFaceSet()
IndexedFaceSet268.coordIndex = [4,0,9,-1,9,3,4,-1,11,19,20,-1,20,6,11,-1,9,10,5,-1,5,3,9,-1,6,7,1,-1,1,11,6,-1,7,8,2,-1,2,1,7,-1,8,5,10,-1,10,2,8,-1,0,4,12,-1,12,27,0,-1,13,16,15,-1,15,14,13,-1,18,17,20,-1,20,19,18,-1,15,16,22,-1,22,21,15,-1,17,18,24,-1,24,23,17,-1,23,24,26,-1,26,25,23,-1,25,26,21,-1,21,22,25,-1,14,27,12,-1,12,13,14,-1,29,30,31,-1,31,32,33,-1,33,34,35,-1,31,33,35,-1,35,36,37,-1,37,38,39,-1,35,37,39,-1,31,35,39,-1,39,40,41,-1,31,39,41,-1,29,31,41,-1,29,41,28,-1,43,44,45,-1,45,46,47,-1,47,48,49,-1,45,47,49,-1,49,50,51,-1,51,52,53,-1,49,51,53,-1,45,49,53,-1,53,54,55,-1,45,53,55,-1,43,45,55,-1,43,55,42,-1,11,1,29,-1,29,28,11,-1,1,2,30,-1,30,29,1,-1,2,10,31,-1,31,30,2,-1,10,9,32,-1,32,31,10,-1,9,0,33,-1,33,32,9,-1,0,27,34,-1,34,33,0,-1,27,14,35,-1,35,34,27,-1,14,15,36,-1,36,35,14,-1,15,21,37,-1,37,36,15,-1,21,26,38,-1,38,37,21,-1,26,24,39,-1,39,38,26,-1,24,18,40,-1,40,39,24,-1,18,19,41,-1,41,40,18,-1,19,11,28,-1,28,41,19,-1,12,4,43,-1,43,42,12,-1,4,3,44,-1,44,43,4,-1,3,5,45,-1,45,44,3,-1,5,8,46,-1,46,45,5,-1,8,7,47,-1,47,46,8,-1,7,6,48,-1,48,47,7,-1,6,20,49,-1,49,48,6,-1,20,17,50,-1,50,49,20,-1,17,23,51,-1,51,50,17,-1,23,25,52,-1,52,51,23,-1,25,22,53,-1,53,52,25,-1,22,16,54,-1,54,53,22,-1,16,13,55,-1,55,54,16,-1,13,12,42,-1,42,55,13,-1]
IndexedFaceSet268.creaseAngle = 3.14159
IndexedFaceSet268.texCoordIndex = [1,14,9,-1,9,0,1,-1,11,13,8,-1,8,5,11,-1,9,10,3,-1,3,0,9,-1,4,6,16,-1,16,12,4,-1,6,7,17,-1,17,16,6,-1,7,3,10,-1,10,17,7,-1,14,1,2,-1,2,15,14,-1,18,21,20,-1,20,19,18,-1,23,22,25,-1,25,24,23,-1,20,21,27,-1,27,26,20,-1,29,28,31,-1,31,30,29,-1,30,31,33,-1,33,32,30,-1,32,33,26,-1,26,27,32,-1,19,35,34,-1,34,18,19,-1,37,38,39,-1,39,40,41,-1,41,42,43,-1,39,41,43,-1,43,44,45,-1,45,46,47,-1,43,45,47,-1,39,43,47,-1,47,48,49,-1,39,47,49,-1,37,39,49,-1,37,49,36,-1,51,52,53,-1,53,54,55,-1,55,56,57,-1,53,55,57,-1,57,58,59,-1,59,60,61,-1,57,59,61,-1,53,57,61,-1,61,62,63,-1,53,61,63,-1,51,53,63,-1,51,63,50,-1,12,16,37,-1,37,36,12,-1,16,17,38,-1,38,37,16,-1,17,10,39,-1,39,38,17,-1,10,9,40,-1,40,39,10,-1,9,14,41,-1,41,40,9,-1,14,15,42,-1,42,41,14,-1,35,19,43,-1,43,42,35,-1,19,20,44,-1,44,43,19,-1,20,26,45,-1,45,44,20,-1,26,33,46,-1,46,45,26,-1,33,31,47,-1,47,46,33,-1,31,28,48,-1,48,47,31,-1,23,24,49,-1,49,48,23,-1,13,11,36,-1,36,49,13,-1,2,1,51,-1,51,50,2,-1,1,0,52,-1,52,51,1,-1,0,3,53,-1,53,52,0,-1,3,7,54,-1,54,53,3,-1,7,6,55,-1,55,54,7,-1,6,4,56,-1,56,55,6,-1,5,8,57,-1,57,56,5,-1,25,22,58,-1,58,57,25,-1,29,30,59,-1,59,58,29,-1,30,32,60,-1,60,59,30,-1,32,27,61,-1,61,60,32,-1,27,21,62,-1,62,61,27,-1,21,18,63,-1,63,62,21,-1,18,34,50,-1,50,63,18,-1]
Coordinate269 = x3d.Coordinate()

IndexedFaceSet268.coord = Coordinate269
TextureCoordinate270 = x3d.TextureCoordinate()

IndexedFaceSet268.texCoord = TextureCoordinate270

Shape264.geometry = IndexedFaceSet268

Transform263.children.append(Shape264)

HAnimSegment262.children.append(Transform263)

HAnimJoint261.children.append(HAnimSegment262)
HAnimJoint271 = x3d.HAnimJoint()
HAnimJoint271.name = "vt7"
HAnimJoint271.DEF = "hanim_vt7"
HAnimJoint271.center = [0,48.369999,-0.6117]
HAnimJoint271.ulimit = [0,0,0]
HAnimJoint271.llimit = [0,0,0]
HAnimSegment272 = x3d.HAnimSegment()
HAnimSegment272.name = "t7"
HAnimSegment272.DEF = "hanim_t7"
Transform273 = x3d.Transform()
Transform273.translation = [0,48.369999,-0.6117]
Shape274 = x3d.Shape()
Appearance275 = x3d.Appearance()
Material276 = x3d.Material()
Material276.diffuseColor = [0.588,0.588,0.588]

Appearance275.material = Material276
ImageTexture277 = x3d.ImageTexture()
ImageTexture277.USE = "JinLOA3TextureAtlas"

Appearance275.texture = ImageTexture277

Shape274.appearance = Appearance275
IndexedFaceSet278 = x3d.IndexedFaceSet()
IndexedFaceSet278.coordIndex = [0,2,6,-1,6,8,0,-1,9,18,19,-1,19,1,9,-1,7,5,22,-1,22,23,7,-1,1,3,10,-1,10,9,1,-1,3,4,11,-1,11,10,3,-1,4,0,8,-1,8,11,4,-1,5,7,6,-1,6,2,5,-1,13,12,15,-1,15,14,13,-1,17,16,19,-1,19,18,17,-1,20,23,22,-1,22,21,20,-1,16,17,25,-1,25,24,16,-1,24,25,27,-1,27,26,24,-1,26,27,12,-1,12,13,26,-1,21,14,15,-1,15,20,21,-1,30,31,32,-1,32,33,34,-1,34,35,36,-1,32,34,36,-1,36,37,38,-1,38,39,40,-1,36,38,40,-1,40,41,28,-1,36,40,28,-1,32,36,28,-1,30,32,28,-1,29,30,28,-1,44,45,46,-1,46,47,48,-1,48,49,50,-1,46,48,50,-1,50,51,52,-1,52,53,54,-1,50,52,54,-1,46,50,54,-1,54,55,42,-1,46,54,42,-1,44,46,42,-1,43,44,42,-1,1,19,29,-1,29,28,1,-1,19,16,30,-1,30,29,19,-1,16,24,31,-1,31,30,16,-1,24,26,32,-1,32,31,24,-1,26,13,33,-1,33,32,26,-1,13,14,34,-1,34,33,13,-1,14,21,35,-1,35,34,14,-1,21,22,36,-1,36,35,21,-1,22,5,37,-1,37,36,22,-1,5,2,38,-1,38,37,5,-1,2,0,39,-1,39,38,2,-1,0,4,40,-1,40,39,0,-1,4,3,41,-1,41,40,4,-1,3,1,28,-1,28,41,3,-1,7,23,43,-1,43,42,7,-1,23,20,44,-1,44,43,23,-1,20,15,45,-1,45,44,20,-1,15,12,46,-1,46,45,15,-1,12,27,47,-1,47,46,12,-1,27,25,48,-1,48,47,27,-1,25,17,49,-1,49,48,25,-1,17,18,50,-1,50,49,17,-1,18,9,51,-1,51,50,18,-1,9,10,52,-1,52,51,9,-1,10,11,53,-1,53,52,10,-1,11,8,54,-1,54,53,11,-1,8,6,55,-1,55,54,8,-1,6,7,42,-1,42,55,6,-1]
IndexedFaceSet278.creaseAngle = 3.14159
IndexedFaceSet278.texCoordIndex = [3,8,9,-1,9,11,3,-1,13,16,6,-1,6,5,13,-1,10,0,7,-1,7,17,10,-1,2,1,14,-1,14,12,2,-1,1,4,15,-1,15,14,1,-1,4,3,11,-1,11,15,4,-1,0,10,9,-1,9,8,0,-1,19,18,21,-1,21,20,19,-1,23,22,25,-1,25,24,23,-1,26,29,28,-1,28,27,26,-1,31,30,33,-1,33,32,31,-1,32,33,35,-1,35,34,32,-1,34,35,18,-1,18,19,34,-1,27,20,21,-1,21,26,27,-1,38,39,40,-1,40,41,42,-1,42,43,44,-1,40,42,44,-1,44,45,46,-1,46,47,48,-1,44,46,48,-1,48,49,36,-1,44,48,36,-1,40,44,36,-1,38,40,36,-1,37,38,36,-1,52,53,54,-1,54,55,56,-1,56,57,58,-1,54,56,58,-1,58,59,60,-1,60,61,62,-1,58,60,62,-1,54,58,62,-1,62,63,50,-1,54,62,50,-1,52,54,50,-1,51,52,50,-1,5,6,37,-1,37,36,5,-1,25,22,38,-1,38,37,25,-1,31,32,39,-1,39,38,31,-1,32,34,40,-1,40,39,32,-1,34,19,41,-1,41,40,34,-1,19,20,42,-1,42,41,19,-1,20,27,43,-1,43,42,20,-1,27,28,44,-1,44,43,27,-1,7,0,45,-1,45,44,7,-1,0,8,46,-1,46,45,0,-1,8,3,47,-1,47,46,8,-1,3,4,48,-1,48,47,3,-1,4,1,49,-1,49,48,4,-1,1,2,36,-1,36,49,1,-1,10,17,51,-1,51,50,10,-1,29,26,52,-1,52,51,29,-1,26,21,53,-1,53,52,26,-1,21,18,54,-1,54,53,21,-1,18,35,55,-1,55,54,18,-1,35,33,56,-1,56,55,35,-1,33,30,57,-1,57,56,33,-1,23,24,58,-1,58,57,23,-1,16,13,59,-1,59,58,16,-1,12,14,60,-1,60,59,12,-1,14,15,61,-1,61,60,14,-1,15,11,62,-1,62,61,15,-1,11,9,63,-1,63,62,11,-1,9,10,50,-1,50,63,9,-1]
Coordinate279 = x3d.Coordinate()

IndexedFaceSet278.coord = Coordinate279
TextureCoordinate280 = x3d.TextureCoordinate()

IndexedFaceSet278.texCoord = TextureCoordinate280

Shape274.geometry = IndexedFaceSet278

Transform273.children.append(Shape274)

HAnimSegment272.children.append(Transform273)

HAnimJoint271.children.append(HAnimSegment272)
HAnimJoint281 = x3d.HAnimJoint()
HAnimJoint281.name = "vt6"
HAnimJoint281.DEF = "hanim_vt6"
HAnimJoint281.center = [0,48.950001,-0.6117]
HAnimJoint281.ulimit = [0,0,0]
HAnimJoint281.llimit = [0,0,0]
HAnimSegment282 = x3d.HAnimSegment()
HAnimSegment282.name = "t6"
HAnimSegment282.DEF = "hanim_t6"
Transform283 = x3d.Transform()
Transform283.translation = [0,48.950001,-0.6117]
Shape284 = x3d.Shape()
Appearance285 = x3d.Appearance()
Material286 = x3d.Material()
Material286.diffuseColor = [0.588,0.588,0.588]

Appearance285.material = Material286
ImageTexture287 = x3d.ImageTexture()
ImageTexture287.USE = "JinLOA3TextureAtlas"

Appearance285.texture = ImageTexture287

Shape284.appearance = Appearance285
IndexedFaceSet288 = x3d.IndexedFaceSet()
IndexedFaceSet288.coordIndex = [12,9,5,-1,5,3,12,-1,2,1,6,-1,6,11,2,-1,0,7,23,-1,23,24,0,-1,25,8,12,-1,12,3,25,-1,9,6,1,-1,1,5,9,-1,11,10,4,-1,4,2,11,-1,4,10,7,-1,7,0,4,-1,13,16,15,-1,15,14,13,-1,18,17,20,-1,20,19,18,-1,21,24,23,-1,23,22,21,-1,25,16,13,-1,13,8,25,-1,14,15,19,-1,19,20,14,-1,17,18,27,-1,27,26,17,-1,27,21,22,-1,22,26,27,-1,30,31,32,-1,32,33,34,-1,34,35,36,-1,32,34,36,-1,36,37,38,-1,38,39,40,-1,36,38,40,-1,40,41,28,-1,36,40,28,-1,32,36,28,-1,30,32,28,-1,29,30,28,-1,44,45,46,-1,46,47,48,-1,48,49,50,-1,46,48,50,-1,50,51,52,-1,52,53,54,-1,50,52,54,-1,54,55,42,-1,50,54,42,-1,46,50,42,-1,44,46,42,-1,43,44,42,-1,3,5,29,-1,29,28,3,-1,5,1,30,-1,30,29,5,-1,1,2,31,-1,31,30,1,-1,2,4,32,-1,32,31,2,-1,4,0,33,-1,33,32,4,-1,0,24,34,-1,34,33,0,-1,24,21,35,-1,35,34,24,-1,21,27,36,-1,36,35,21,-1,27,18,37,-1,37,36,27,-1,18,19,38,-1,38,37,18,-1,19,15,39,-1,39,38,19,-1,15,16,40,-1,40,39,15,-1,16,25,41,-1,41,40,16,-1,25,3,28,-1,28,41,25,-1,23,7,43,-1,43,42,23,-1,7,10,44,-1,44,43,7,-1,10,11,45,-1,45,44,10,-1,11,6,46,-1,46,45,11,-1,6,9,47,-1,47,46,6,-1,9,12,48,-1,48,47,9,-1,12,8,49,-1,49,48,12,-1,8,13,50,-1,50,49,8,-1,13,14,51,-1,51,50,13,-1,14,20,52,-1,52,51,14,-1,20,17,53,-1,53,52,20,-1,17,26,54,-1,54,53,17,-1,26,22,55,-1,55,54,26,-1,22,23,42,-1,42,55,22,-1]
IndexedFaceSet288.creaseAngle = 3.14159
IndexedFaceSet288.texCoordIndex = [17,13,8,-1,8,4,17,-1,3,2,9,-1,9,16,3,-1,1,10,14,-1,14,5,1,-1,6,12,17,-1,17,4,6,-1,13,9,2,-1,2,8,13,-1,16,15,7,-1,7,3,16,-1,7,15,11,-1,11,0,7,-1,18,21,20,-1,20,19,18,-1,23,22,25,-1,25,24,23,-1,26,29,28,-1,28,27,26,-1,30,21,18,-1,18,31,30,-1,19,20,24,-1,24,25,19,-1,22,23,33,-1,33,32,22,-1,33,35,34,-1,34,32,33,-1,38,39,40,-1,40,41,42,-1,42,43,44,-1,40,42,44,-1,44,45,46,-1,46,47,48,-1,44,46,48,-1,48,49,36,-1,44,48,36,-1,40,44,36,-1,38,40,36,-1,37,38,36,-1,52,53,54,-1,54,55,56,-1,56,57,58,-1,54,56,58,-1,58,59,60,-1,60,61,62,-1,58,60,62,-1,62,63,50,-1,58,62,50,-1,54,58,50,-1,52,54,50,-1,51,52,50,-1,4,8,37,-1,37,36,4,-1,8,2,38,-1,38,37,8,-1,2,3,39,-1,39,38,2,-1,3,7,40,-1,40,39,3,-1,7,0,41,-1,41,40,7,-1,1,5,42,-1,42,41,1,-1,29,26,43,-1,43,42,29,-1,35,33,44,-1,44,43,35,-1,33,23,45,-1,45,44,33,-1,23,24,46,-1,46,45,23,-1,24,20,47,-1,47,46,24,-1,20,21,48,-1,48,47,20,-1,21,30,49,-1,49,48,21,-1,6,4,36,-1,36,49,6,-1,14,10,51,-1,51,50,14,-1,11,15,52,-1,52,51,11,-1,15,16,53,-1,53,52,15,-1,16,9,54,-1,54,53,16,-1,9,13,55,-1,55,54,9,-1,13,17,56,-1,56,55,13,-1,17,12,57,-1,57,56,17,-1,31,18,58,-1,58,57,31,-1,18,19,59,-1,59,58,18,-1,19,25,60,-1,60,59,19,-1,25,22,61,-1,61,60,25,-1,22,32,62,-1,62,61,22,-1,32,34,63,-1,63,62,32,-1,27,28,50,-1,50,63,27,-1]
Coordinate289 = x3d.Coordinate()

IndexedFaceSet288.coord = Coordinate289
TextureCoordinate290 = x3d.TextureCoordinate()

IndexedFaceSet288.texCoord = TextureCoordinate290

Shape284.geometry = IndexedFaceSet288

Transform283.children.append(Shape284)

HAnimSegment282.children.append(Transform283)

HAnimJoint281.children.append(HAnimSegment282)
HAnimJoint291 = x3d.HAnimJoint()
HAnimJoint291.name = "vt5"
HAnimJoint291.DEF = "hanim_vt5"
HAnimJoint291.center = [0,49.639999,-0.6117]
HAnimJoint291.ulimit = [0,0,0]
HAnimJoint291.llimit = [0,0,0]
HAnimSegment292 = x3d.HAnimSegment()
HAnimSegment292.name = "t5"
HAnimSegment292.DEF = "hanim_t5"
Transform293 = x3d.Transform()
Transform293.translation = [0,49.639999,-0.6117]
Shape294 = x3d.Shape()
Appearance295 = x3d.Appearance()
Material296 = x3d.Material()
Material296.diffuseColor = [0.588,0.588,0.588]

Appearance295.material = Material296
ImageTexture297 = x3d.ImageTexture()
ImageTexture297.USE = "JinLOA3TextureAtlas"

Appearance295.texture = ImageTexture297

Shape294.appearance = Appearance295
IndexedFaceSet298 = x3d.IndexedFaceSet()
IndexedFaceSet298.coordIndex = [0,6,16,-1,16,13,0,-1,17,10,9,-1,9,3,17,-1,12,7,5,-1,5,2,12,-1,8,11,4,-1,4,1,8,-1,4,11,6,-1,6,0,4,-1,2,3,9,-1,9,12,2,-1,1,5,7,-1,7,8,1,-1,14,13,16,-1,16,15,14,-1,17,19,18,-1,18,10,17,-1,21,20,23,-1,23,22,21,-1,25,24,27,-1,27,26,25,-1,27,14,15,-1,15,26,27,-1,20,21,18,-1,18,19,20,-1,24,25,22,-1,22,23,24,-1,30,31,32,-1,32,33,34,-1,34,35,36,-1,32,34,36,-1,36,37,38,-1,38,39,40,-1,36,38,40,-1,40,41,28,-1,36,40,28,-1,32,36,28,-1,30,32,28,-1,29,30,28,-1,44,45,46,-1,46,47,48,-1,48,49,50,-1,46,48,50,-1,50,51,52,-1,52,53,54,-1,50,52,54,-1,54,55,42,-1,50,54,42,-1,46,50,42,-1,44,46,42,-1,43,44,42,-1,3,2,29,-1,29,28,3,-1,2,5,30,-1,30,29,2,-1,5,1,31,-1,31,30,5,-1,1,4,32,-1,32,31,1,-1,4,0,33,-1,33,32,4,-1,0,13,34,-1,34,33,0,-1,13,14,35,-1,35,34,13,-1,14,27,36,-1,36,35,14,-1,27,24,37,-1,37,36,27,-1,24,23,38,-1,38,37,24,-1,23,20,39,-1,39,38,23,-1,20,19,40,-1,40,39,20,-1,19,17,41,-1,41,40,19,-1,17,3,28,-1,28,41,17,-1,12,9,43,-1,43,42,12,-1,9,10,44,-1,44,43,9,-1,10,18,45,-1,45,44,10,-1,18,21,46,-1,46,45,18,-1,21,22,47,-1,47,46,21,-1,22,25,48,-1,48,47,22,-1,25,26,49,-1,49,48,25,-1,26,15,50,-1,50,49,26,-1,15,16,51,-1,51,50,15,-1,16,6,52,-1,52,51,16,-1,6,11,53,-1,53,52,6,-1,11,8,54,-1,54,53,11,-1,8,7,55,-1,55,54,8,-1,7,12,42,-1,42,55,7,-1]
IndexedFaceSet298.creaseAngle = 3.14159
IndexedFaceSet298.texCoordIndex = [5,10,14,-1,14,2,5,-1,8,15,13,-1,13,7,8,-1,17,11,3,-1,3,6,17,-1,12,16,0,-1,0,4,12,-1,0,16,9,-1,9,1,0,-1,6,7,13,-1,13,17,6,-1,4,3,11,-1,11,12,4,-1,19,18,21,-1,21,20,19,-1,22,25,24,-1,24,23,22,-1,27,26,29,-1,29,28,27,-1,31,30,33,-1,33,32,31,-1,33,35,34,-1,34,32,33,-1,26,27,24,-1,24,25,26,-1,30,31,28,-1,28,29,30,-1,38,39,40,-1,40,41,42,-1,42,43,44,-1,40,42,44,-1,44,45,46,-1,46,47,48,-1,44,46,48,-1,48,49,36,-1,44,48,36,-1,40,44,36,-1,38,40,36,-1,37,38,36,-1,52,53,54,-1,54,55,56,-1,56,57,58,-1,54,56,58,-1,58,59,60,-1,60,61,62,-1,58,60,62,-1,62,63,50,-1,58,62,50,-1,54,58,50,-1,52,54,50,-1,51,52,50,-1,7,6,37,-1,37,36,7,-1,6,3,38,-1,38,37,6,-1,3,4,39,-1,39,38,3,-1,4,0,40,-1,40,39,4,-1,0,1,41,-1,41,40,0,-1,5,2,42,-1,42,41,5,-1,18,19,43,-1,43,42,18,-1,35,33,44,-1,44,43,35,-1,33,30,45,-1,45,44,33,-1,30,29,46,-1,46,45,30,-1,29,26,47,-1,47,46,29,-1,26,25,48,-1,48,47,26,-1,25,22,49,-1,49,48,25,-1,8,7,36,-1,36,49,8,-1,17,13,51,-1,51,50,17,-1,13,15,52,-1,52,51,13,-1,23,24,53,-1,53,52,23,-1,24,27,54,-1,54,53,24,-1,27,28,55,-1,55,54,27,-1,28,31,56,-1,56,55,28,-1,31,32,57,-1,57,56,31,-1,32,34,58,-1,58,57,32,-1,20,21,59,-1,59,58,20,-1,14,10,60,-1,60,59,14,-1,9,16,61,-1,61,60,9,-1,16,12,62,-1,62,61,16,-1,12,11,63,-1,63,62,12,-1,11,17,50,-1,50,63,11,-1]
Coordinate299 = x3d.Coordinate()

IndexedFaceSet298.coord = Coordinate299
TextureCoordinate300 = x3d.TextureCoordinate()

IndexedFaceSet298.texCoord = TextureCoordinate300

Shape294.geometry = IndexedFaceSet298

Transform293.children.append(Shape294)

HAnimSegment292.children.append(Transform293)

HAnimJoint291.children.append(HAnimSegment292)
HAnimJoint301 = x3d.HAnimJoint()
HAnimJoint301.name = "vt4"
HAnimJoint301.DEF = "hanim_vt4"
HAnimJoint301.center = [0,50.310001,-0.6117]
HAnimJoint301.ulimit = [0,0,0]
HAnimJoint301.llimit = [0,0,0]
HAnimSegment302 = x3d.HAnimSegment()
HAnimSegment302.name = "t4"
HAnimSegment302.DEF = "hanim_t4"
Transform303 = x3d.Transform()
Transform303.translation = [0,50.310001,-0.6117]
Shape304 = x3d.Shape()
Appearance305 = x3d.Appearance()
Material306 = x3d.Material()
Material306.diffuseColor = [0.588,0.588,0.588]

Appearance305.material = Material306
ImageTexture307 = x3d.ImageTexture()
ImageTexture307.USE = "JinLOA3TextureAtlas"

Appearance305.texture = ImageTexture307

Shape304.appearance = Appearance305
IndexedFaceSet308 = x3d.IndexedFaceSet()
IndexedFaceSet308.coordIndex = [2,3,9,-1,9,12,2,-1,3,0,10,-1,10,9,3,-1,7,20,21,-1,21,4,7,-1,11,7,4,-1,4,5,11,-1,25,26,10,-1,10,0,25,-1,6,11,5,-1,11,6,1,-1,1,8,11,-1,2,12,8,-1,8,1,2,-1,14,13,16,-1,16,15,14,-1,15,16,18,-1,18,17,15,-1,19,22,21,-1,21,20,19,-1,23,24,22,-1,22,19,23,-1,25,17,18,-1,18,26,25,-1,27,24,23,-1,23,29,28,-1,28,27,23,-1,14,28,29,-1,29,13,14,-1,31,32,33,-1,31,33,34,-1,34,35,36,-1,36,37,38,-1,34,36,38,-1,31,34,38,-1,38,39,40,-1,40,41,42,-1,38,40,42,-1,31,38,42,-1,42,43,44,-1,31,42,44,-1,31,44,45,-1,31,45,30,-1,48,49,50,-1,50,51,52,-1,52,53,54,-1,50,52,54,-1,54,55,56,-1,56,57,58,-1,54,56,58,-1,58,59,46,-1,54,58,46,-1,50,54,46,-1,48,50,46,-1,47,48,46,-1,3,2,31,-1,31,30,3,-1,2,1,32,-1,32,31,2,-1,1,6,33,-1,33,32,1,-1,6,5,34,-1,34,33,6,-1,5,4,35,-1,35,34,5,-1,4,21,36,-1,36,35,4,-1,21,22,37,-1,37,36,21,-1,22,24,38,-1,38,37,22,-1,24,27,39,-1,39,38,24,-1,27,28,40,-1,40,39,27,-1,28,14,41,-1,41,40,28,-1,14,15,42,-1,42,41,14,-1,15,17,43,-1,43,42,15,-1,17,25,44,-1,44,43,17,-1,25,0,45,-1,45,44,25,-1,0,3,30,-1,30,45,0,-1,9,10,47,-1,47,46,9,-1,10,26,48,-1,48,47,10,-1,26,18,49,-1,49,48,26,-1,18,16,50,-1,50,49,18,-1,16,13,51,-1,51,50,16,-1,13,29,52,-1,52,51,13,-1,29,23,53,-1,53,52,29,-1,23,19,54,-1,54,53,23,-1,19,20,55,-1,55,54,19,-1,20,7,56,-1,56,55,20,-1,7,11,57,-1,57,56,7,-1,11,8,58,-1,58,57,11,-1,8,12,59,-1,59,58,8,-1,12,9,46,-1,46,59,12,-1]
IndexedFaceSet308.creaseAngle = 3.14159
IndexedFaceSet308.texCoordIndex = [3,4,14,-1,14,18,3,-1,4,1,15,-1,15,14,4,-1,10,17,7,-1,7,6,10,-1,16,11,5,-1,5,8,16,-1,0,19,15,-1,15,1,0,-1,9,16,8,-1,16,9,2,-1,2,12,16,-1,3,18,13,-1,13,2,3,-1,21,20,23,-1,23,22,21,-1,22,23,25,-1,25,24,22,-1,26,29,28,-1,28,27,26,-1,30,33,32,-1,32,31,30,-1,34,24,25,-1,25,35,34,-1,36,33,30,-1,30,38,37,-1,37,36,30,-1,21,37,39,-1,39,20,21,-1,41,42,43,-1,41,43,44,-1,44,45,46,-1,46,47,48,-1,44,46,48,-1,41,44,48,-1,48,49,50,-1,50,51,52,-1,48,50,52,-1,41,48,52,-1,52,53,54,-1,41,52,54,-1,41,54,55,-1,41,55,40,-1,58,59,60,-1,60,61,62,-1,62,63,64,-1,60,62,64,-1,64,65,66,-1,66,67,68,-1,64,66,68,-1,68,69,56,-1,64,68,56,-1,60,64,56,-1,58,60,56,-1,57,58,56,-1,4,3,41,-1,41,40,4,-1,3,2,42,-1,42,41,3,-1,2,9,43,-1,43,42,2,-1,9,8,44,-1,44,43,9,-1,8,5,45,-1,45,44,8,-1,6,7,46,-1,46,45,6,-1,28,29,47,-1,47,46,28,-1,32,33,48,-1,48,47,32,-1,33,36,49,-1,49,48,33,-1,36,37,50,-1,50,49,36,-1,37,21,51,-1,51,50,37,-1,21,22,52,-1,52,51,21,-1,22,24,53,-1,53,52,22,-1,24,34,54,-1,54,53,24,-1,0,1,55,-1,55,54,0,-1,1,4,40,-1,40,55,1,-1,14,15,57,-1,57,56,14,-1,15,19,58,-1,58,57,15,-1,35,25,59,-1,59,58,35,-1,25,23,60,-1,60,59,25,-1,23,20,61,-1,61,60,23,-1,20,39,62,-1,62,61,20,-1,38,30,63,-1,63,62,38,-1,30,31,64,-1,64,63,30,-1,26,27,65,-1,65,64,26,-1,17,10,66,-1,66,65,17,-1,11,16,67,-1,67,66,11,-1,16,12,68,-1,68,67,16,-1,13,18,69,-1,69,68,13,-1,18,14,56,-1,56,69,18,-1]
Coordinate309 = x3d.Coordinate()

IndexedFaceSet308.coord = Coordinate309
TextureCoordinate310 = x3d.TextureCoordinate()

IndexedFaceSet308.texCoord = TextureCoordinate310

Shape304.geometry = IndexedFaceSet308

Transform303.children.append(Shape304)

HAnimSegment302.children.append(Transform303)

HAnimJoint301.children.append(HAnimSegment302)
HAnimJoint311 = x3d.HAnimJoint()
HAnimJoint311.name = "vt3"
HAnimJoint311.DEF = "hanim_vt3"
HAnimJoint311.center = [0,51.130001,-0.6117]
HAnimJoint311.ulimit = [0,0,0]
HAnimJoint311.llimit = [0,0,0]
HAnimSegment312 = x3d.HAnimSegment()
HAnimSegment312.name = "t3"
HAnimSegment312.DEF = "hanim_t3"
Transform313 = x3d.Transform()
Transform313.translation = [0,51.130001,-0.6117]
Shape314 = x3d.Shape()
Appearance315 = x3d.Appearance()
Material316 = x3d.Material()
Material316.diffuseColor = [0.588,0.588,0.588]

Appearance315.material = Material316
ImageTexture317 = x3d.ImageTexture()
ImageTexture317.USE = "JinLOA3TextureAtlas"

Appearance315.texture = ImageTexture317

Shape314.appearance = Appearance315
IndexedFaceSet318 = x3d.IndexedFaceSet()
IndexedFaceSet318.coordIndex = [16,15,0,-1,0,7,16,-1,0,15,8,-1,1,5,11,-1,11,10,1,-1,18,6,12,-1,12,17,18,-1,14,13,2,-1,2,3,14,-1,9,14,3,-1,3,4,9,-1,11,5,0,-1,0,8,11,-1,13,12,6,-1,6,2,13,-1,49,16,7,-1,7,0,5,-1,1,10,9,-1,9,4,1,-1,3,2,20,-1,20,19,3,-1,2,6,21,-1,21,20,2,-1,6,18,53,-1,53,21,6,-1,7,5,23,-1,23,22,7,-1,5,1,24,-1,24,23,5,-1,1,4,25,-1,25,24,1,-1,4,3,19,-1,19,25,4,-1,10,11,27,-1,27,26,10,-1,11,8,28,-1,28,27,11,-1,8,15,29,-1,29,28,8,-1,17,12,30,-1,30,62,17,-1,12,13,31,-1,31,30,12,-1,13,14,32,-1,32,31,13,-1,14,9,33,-1,33,32,14,-1,9,10,26,-1,26,33,9,-1,16,35,34,-1,34,15,16,-1,34,36,15,-1,38,37,40,-1,40,39,38,-1,18,17,42,-1,42,41,18,-1,44,43,46,-1,46,45,44,-1,48,47,43,-1,43,44,48,-1,40,36,34,-1,34,39,40,-1,45,46,41,-1,41,42,45,-1,49,35,16,-1,35,39,34,-1,38,47,48,-1,48,37,38,-1,43,51,50,-1,50,46,43,-1,46,50,52,-1,52,41,46,-1,41,52,53,-1,53,18,41,-1,35,55,54,-1,54,39,35,-1,39,54,56,-1,56,38,39,-1,38,56,57,-1,57,47,38,-1,47,57,51,-1,51,43,47,-1,37,59,58,-1,58,40,37,-1,40,58,60,-1,60,36,40,-1,36,60,29,-1,29,15,36,-1,17,62,61,-1,61,42,17,-1,42,61,63,-1,63,45,42,-1,45,63,64,-1,64,44,45,-1,44,64,65,-1,65,48,44,-1,48,65,59,-1,59,37,48,-1,27,28,29,-1,29,60,58,-1,58,59,65,-1,29,58,65,-1,65,64,63,-1,63,61,62,-1,65,63,62,-1,62,30,31,-1,31,32,33,-1,62,31,33,-1,65,62,33,-1,29,65,33,-1,27,29,33,-1,27,33,26,-1]
IndexedFaceSet318.creaseAngle = 3.14159
IndexedFaceSet318.texCoordIndex = [2,12,1,-1,1,0,2,-1,1,12,13,-1,4,8,16,-1,16,15,4,-1,11,10,17,-1,17,19,11,-1,21,20,5,-1,5,6,21,-1,14,21,6,-1,6,7,14,-1,16,8,1,-1,1,13,16,-1,20,18,9,-1,9,5,20,-1,3,2,0,-1,0,1,8,-1,4,15,14,-1,14,7,4,-1,6,5,23,-1,23,22,6,-1,5,9,24,-1,24,23,5,-1,10,11,25,-1,25,24,10,-1,0,8,27,-1,27,26,0,-1,8,4,28,-1,28,27,8,-1,4,7,29,-1,29,28,4,-1,7,6,22,-1,22,29,7,-1,15,16,31,-1,31,30,15,-1,16,13,32,-1,32,31,16,-1,13,12,33,-1,33,32,13,-1,19,17,35,-1,35,34,19,-1,18,20,36,-1,36,35,18,-1,20,21,37,-1,37,36,20,-1,21,14,38,-1,38,37,21,-1,14,15,30,-1,30,38,14,-1,42,41,40,-1,40,39,42,-1,40,43,39,-1,45,44,47,-1,47,46,45,-1,49,48,51,-1,51,50,49,-1,53,52,55,-1,55,54,53,-1,57,56,52,-1,52,53,57,-1,47,43,40,-1,40,46,47,-1,54,55,59,-1,59,58,54,-1,60,41,42,-1,41,46,40,-1,45,56,57,-1,57,44,45,-1,52,62,61,-1,61,55,52,-1,55,61,63,-1,63,59,55,-1,50,63,64,-1,64,49,50,-1,41,66,65,-1,65,46,41,-1,46,65,67,-1,67,45,46,-1,45,67,68,-1,68,56,45,-1,56,68,62,-1,62,52,56,-1,44,70,69,-1,69,47,44,-1,47,69,71,-1,71,43,47,-1,43,71,72,-1,72,39,43,-1,48,74,73,-1,73,51,48,-1,58,73,75,-1,75,54,58,-1,54,75,76,-1,76,53,54,-1,53,76,77,-1,77,57,53,-1,57,77,70,-1,70,44,57,-1,31,32,33,-1,33,71,69,-1,69,70,77,-1,33,69,77,-1,77,76,75,-1,75,73,74,-1,77,75,74,-1,74,35,36,-1,36,37,38,-1,74,36,38,-1,77,74,38,-1,33,77,38,-1,31,33,38,-1,31,38,30,-1]
Coordinate319 = x3d.Coordinate()

IndexedFaceSet318.coord = Coordinate319
TextureCoordinate320 = x3d.TextureCoordinate()

IndexedFaceSet318.texCoord = TextureCoordinate320

Shape314.geometry = IndexedFaceSet318

Transform313.children.append(Shape314)

HAnimSegment312.children.append(Transform313)

HAnimJoint311.children.append(HAnimSegment312)
HAnimJoint321 = x3d.HAnimJoint()
HAnimJoint321.name = "vt2"
HAnimJoint321.DEF = "hanim_vt2"
HAnimJoint321.center = [0,52.23,-0.6127]
HAnimJoint321.ulimit = [0,0,0]
HAnimJoint321.llimit = [0,0,0]
HAnimSegment322 = x3d.HAnimSegment()
HAnimSegment322.name = "t2"
HAnimSegment322.DEF = "hanim_t2"
Transform323 = x3d.Transform()
Transform323.translation = [0,52.23,-0.6127]
Shape324 = x3d.Shape()
Appearance325 = x3d.Appearance()
Material326 = x3d.Material()
Material326.diffuseColor = [0.588,0.588,0.588]

Appearance325.material = Material326
ImageTexture327 = x3d.ImageTexture()
ImageTexture327.USE = "JinLOA3TextureAtlas"

Appearance325.texture = ImageTexture327

Shape324.appearance = Appearance325
IndexedFaceSet328 = x3d.IndexedFaceSet()
IndexedFaceSet328.coordIndex = [1,5,12,-1,7,2,19,-1,19,0,7,-1,0,11,7,-1,2,7,5,-1,5,1,2,-1,17,0,19,-1,0,17,6,-1,6,11,0,-1,20,2,1,-1,1,4,20,-1,2,20,19,-1,10,9,15,-1,15,14,10,-1,9,16,15,-1,8,10,14,-1,14,18,8,-1,13,6,17,-1,3,8,18,-1,18,21,3,-1,51,4,1,-1,1,12,51,-1,6,13,16,-1,16,9,6,-1,6,9,23,-1,23,22,6,-1,9,10,24,-1,24,23,9,-1,10,8,25,-1,25,24,10,-1,8,3,56,-1,56,25,8,-1,14,15,27,-1,27,26,14,-1,15,16,28,-1,28,27,15,-1,16,13,29,-1,29,28,16,-1,13,17,30,-1,30,29,13,-1,17,19,31,-1,31,30,17,-1,19,20,63,-1,63,31,19,-1,21,18,32,-1,32,65,21,-1,18,14,26,-1,26,32,18,-1,33,35,34,-1,38,37,36,-1,36,39,38,-1,37,38,40,-1,39,33,34,-1,34,38,39,-1,41,36,37,-1,37,40,42,-1,42,41,37,-1,20,4,33,-1,33,39,20,-1,39,36,20,-1,43,46,45,-1,45,44,43,-1,44,45,47,-1,49,48,46,-1,46,43,49,-1,50,41,42,-1,3,21,48,-1,48,49,3,-1,51,35,33,-1,33,4,51,-1,42,44,47,-1,47,50,42,-1,42,53,52,-1,52,44,42,-1,44,52,54,-1,54,43,44,-1,43,54,55,-1,55,49,43,-1,49,55,56,-1,56,3,49,-1,46,58,57,-1,57,45,46,-1,45,57,59,-1,59,47,45,-1,47,59,60,-1,60,50,47,-1,50,60,61,-1,61,41,50,-1,41,61,62,-1,62,36,41,-1,36,62,63,-1,63,20,36,-1,21,65,64,-1,64,48,21,-1,48,64,58,-1,58,46,48,-1,28,29,30,-1,31,63,62,-1,30,31,62,-1,62,61,60,-1,60,59,57,-1,62,60,57,-1,62,57,58,-1,58,64,65,-1,65,32,26,-1,58,65,26,-1,62,58,26,-1,30,62,26,-1,28,30,26,-1,27,28,26,-1]
IndexedFaceSet328.creaseAngle = 3.14159
IndexedFaceSet328.texCoordIndex = [0,1,16,-1,4,5,26,-1,26,3,4,-1,3,15,4,-1,5,4,6,-1,6,7,5,-1,22,3,26,-1,3,22,8,-1,8,15,3,-1,27,5,7,-1,7,10,27,-1,5,27,26,-1,14,9,20,-1,20,19,14,-1,9,21,20,-1,13,14,19,-1,19,23,13,-1,18,8,22,-1,11,12,24,-1,24,25,11,-1,17,2,0,-1,0,16,17,-1,8,18,21,-1,21,9,8,-1,8,9,29,-1,29,28,8,-1,9,14,30,-1,30,29,9,-1,14,13,31,-1,31,30,14,-1,12,11,32,-1,32,31,12,-1,19,20,34,-1,34,33,19,-1,20,21,35,-1,35,34,20,-1,21,18,36,-1,36,35,21,-1,18,22,37,-1,37,36,18,-1,22,26,38,-1,38,37,22,-1,26,27,39,-1,39,38,26,-1,25,24,41,-1,41,40,25,-1,23,19,33,-1,33,41,23,-1,42,44,43,-1,47,46,45,-1,45,48,47,-1,46,47,49,-1,48,51,50,-1,50,47,48,-1,52,45,46,-1,46,49,53,-1,53,52,46,-1,55,54,51,-1,51,48,55,-1,48,45,55,-1,56,59,58,-1,58,57,56,-1,57,58,60,-1,62,61,59,-1,59,56,62,-1,63,52,53,-1,65,64,67,-1,67,66,65,-1,68,44,42,-1,42,69,68,-1,53,57,60,-1,60,63,53,-1,53,71,70,-1,70,57,53,-1,57,70,72,-1,72,56,57,-1,56,72,73,-1,73,62,56,-1,66,73,74,-1,74,65,66,-1,59,76,75,-1,75,58,59,-1,58,75,77,-1,77,60,58,-1,60,77,78,-1,78,63,60,-1,63,78,79,-1,79,52,63,-1,52,79,80,-1,80,45,52,-1,45,80,81,-1,81,55,45,-1,64,83,82,-1,82,67,64,-1,61,82,76,-1,76,59,61,-1,35,36,37,-1,38,39,80,-1,37,38,80,-1,80,79,78,-1,78,77,75,-1,80,78,75,-1,80,75,76,-1,76,82,83,-1,83,41,33,-1,76,83,33,-1,80,76,33,-1,37,80,33,-1,35,37,33,-1,34,35,33,-1]
Coordinate329 = x3d.Coordinate()

IndexedFaceSet328.coord = Coordinate329
TextureCoordinate330 = x3d.TextureCoordinate()

IndexedFaceSet328.texCoord = TextureCoordinate330

Shape324.geometry = IndexedFaceSet328

Transform323.children.append(Shape324)

HAnimSegment322.children.append(Transform323)

HAnimJoint321.children.append(HAnimSegment322)
HAnimJoint331 = x3d.HAnimJoint()
HAnimJoint331.name = "vt1"
HAnimJoint331.DEF = "hanim_vt1"
HAnimJoint331.center = [0,53.290001,-0.6117]
HAnimJoint331.ulimit = [0,0,0]
HAnimJoint331.llimit = [0,0,0]
HAnimSegment332 = x3d.HAnimSegment()
HAnimSegment332.name = "t1"
HAnimSegment332.DEF = "hanim_t1"
Transform333 = x3d.Transform()
Transform333.translation = [0,53.290001,-0.6117]
Shape334 = x3d.Shape()
Appearance335 = x3d.Appearance()
Material336 = x3d.Material()
Material336.diffuseColor = [0.588,0.588,0.588]

Appearance335.material = Material336
ImageTexture337 = x3d.ImageTexture()
ImageTexture337.USE = "JinLOA3TextureAtlas"

Appearance335.texture = ImageTexture337

Shape334.appearance = Appearance335
IndexedFaceSet338 = x3d.IndexedFaceSet()
IndexedFaceSet338.coordIndex = [1,5,3,-1,3,2,1,-1,5,6,3,-1,7,27,3,-1,3,6,7,-1,0,1,2,-1,43,11,10,-1,10,4,43,-1,5,1,12,-1,1,0,12,-1,35,26,12,-1,43,4,12,-1,4,5,12,-1,72,28,9,-1,9,28,27,-1,27,7,9,-1,5,4,10,-1,10,6,5,-1,29,72,8,-1,26,35,14,-1,14,49,26,-1,35,0,15,-1,15,14,35,-1,17,16,18,-1,18,19,17,-1,16,27,28,-1,28,18,16,-1,13,2,16,-1,27,16,2,-1,2,3,27,-1,19,18,29,-1,29,8,19,-1,18,28,72,-1,72,29,18,-1,0,13,15,-1,21,20,23,-1,23,61,21,-1,20,22,24,-1,24,23,20,-1,22,17,19,-1,19,24,22,-1,20,21,49,-1,49,14,20,-1,22,20,14,-1,14,15,22,-1,15,17,22,-1,61,23,30,-1,30,25,61,-1,23,24,33,-1,33,30,23,-1,24,19,8,-1,8,33,24,-1,0,2,13,-1,15,13,17,-1,16,17,13,-1,68,69,32,-1,32,31,68,-1,30,33,32,-1,33,8,34,-1,33,34,31,-1,31,32,33,-1,32,69,25,-1,25,30,32,-1,12,0,35,-1,37,36,58,-1,58,38,37,-1,38,58,39,-1,40,39,58,-1,58,41,40,-1,51,36,37,-1,43,42,44,-1,44,11,43,-1,38,12,37,-1,37,12,51,-1,45,12,26,-1,43,12,42,-1,42,12,38,-1,73,47,56,-1,47,40,41,-1,41,56,47,-1,38,39,44,-1,44,42,38,-1,46,59,73,-1,26,49,48,-1,48,45,26,-1,45,48,50,-1,50,51,45,-1,54,53,52,-1,52,55,54,-1,55,52,56,-1,56,41,55,-1,57,55,36,-1,41,58,36,-1,36,55,41,-1,53,59,46,-1,46,52,53,-1,52,46,73,-1,73,56,52,-1,51,50,57,-1,21,61,60,-1,60,62,21,-1,62,60,63,-1,63,64,62,-1,64,63,53,-1,53,54,64,-1,62,48,49,-1,49,21,62,-1,64,50,48,-1,48,62,64,-1,50,64,54,-1,61,25,65,-1,65,60,61,-1,60,65,66,-1,66,63,60,-1,63,66,59,-1,59,53,63,-1,51,57,36,-1,50,54,57,-1,55,57,54,-1,68,67,70,-1,70,69,68,-1,65,70,66,-1,66,71,59,-1,66,70,67,-1,67,71,66,-1,70,65,25,-1,25,69,70,-1,12,45,51,-1,81,82,83,-1,81,83,84,-1,81,84,85,-1,85,86,87,-1,81,85,87,-1,88,89,90,-1,88,90,91,-1,87,88,91,-1,91,74,75,-1,91,75,76,-1,87,91,76,-1,87,76,77,-1,81,87,77,-1,81,77,78,-1,81,78,79,-1,81,79,80,-1,7,6,75,-1,75,74,7,-1,6,10,76,-1,76,75,6,-1,10,11,77,-1,77,76,10,-1,11,44,78,-1,78,77,11,-1,44,39,79,-1,79,78,44,-1,39,40,80,-1,80,79,39,-1,40,47,81,-1,81,80,40,-1,47,73,82,-1,82,81,47,-1,73,59,83,-1,83,82,73,-1,59,71,84,-1,84,83,59,-1,71,67,85,-1,85,84,71,-1,67,68,86,-1,86,85,67,-1,68,31,87,-1,87,86,68,-1,31,34,88,-1,88,87,31,-1,34,8,89,-1,89,88,34,-1,8,72,90,-1,90,89,8,-1,72,9,91,-1,91,90,72,-1,9,7,74,-1,74,91,9,-1]
IndexedFaceSet338.creaseAngle = 3.14159
IndexedFaceSet338.texCoordIndex = [14,15,0,-1,0,16,14,-1,15,19,0,-1,21,10,11,-1,11,18,21,-1,5,2,1,-1,6,25,24,-1,24,4,6,-1,3,2,13,-1,2,5,13,-1,66,7,13,-1,6,4,17,-1,4,15,17,-1,20,9,23,-1,23,9,10,-1,10,21,23,-1,15,4,24,-1,24,19,15,-1,12,20,22,-1,48,47,26,-1,26,27,48,-1,47,49,28,-1,28,26,47,-1,31,32,29,-1,29,30,31,-1,32,53,54,-1,54,29,32,-1,33,50,32,-1,53,32,50,-1,50,51,53,-1,30,29,55,-1,55,56,30,-1,29,54,52,-1,52,55,29,-1,49,33,28,-1,36,41,40,-1,40,35,36,-1,37,39,38,-1,38,34,37,-1,39,31,30,-1,30,38,39,-1,42,36,43,-1,43,45,42,-1,39,37,26,-1,26,28,39,-1,28,31,39,-1,35,44,57,-1,57,46,35,-1,34,38,65,-1,65,58,34,-1,38,30,56,-1,56,65,38,-1,49,50,33,-1,28,33,31,-1,32,31,33,-1,62,63,64,-1,64,61,62,-1,57,65,64,-1,65,56,60,-1,65,60,61,-1,61,64,65,-1,64,63,59,-1,59,57,64,-1,13,8,66,-1,69,68,67,-1,67,70,69,-1,70,67,71,-1,74,73,72,-1,72,75,74,-1,76,78,77,-1,80,79,82,-1,82,81,80,-1,83,84,77,-1,77,84,76,-1,85,84,86,-1,80,87,79,-1,79,87,70,-1,132,90,89,-1,90,74,75,-1,75,89,90,-1,70,71,82,-1,82,79,70,-1,88,91,132,-1,94,93,92,-1,92,95,94,-1,95,92,96,-1,96,97,95,-1,100,99,98,-1,98,101,100,-1,101,98,102,-1,102,103,101,-1,104,101,105,-1,103,106,105,-1,105,101,103,-1,99,108,107,-1,107,98,99,-1,98,107,109,-1,109,102,98,-1,97,96,104,-1,112,111,110,-1,110,113,112,-1,116,115,114,-1,114,117,116,-1,117,114,99,-1,99,100,117,-1,120,119,118,-1,118,112,120,-1,117,96,92,-1,92,116,117,-1,96,117,100,-1,111,122,121,-1,121,123,111,-1,115,125,124,-1,124,114,115,-1,114,124,108,-1,108,99,114,-1,97,104,105,-1,96,100,104,-1,101,104,100,-1,127,126,129,-1,129,128,127,-1,121,129,124,-1,124,130,108,-1,124,129,126,-1,126,130,124,-1,129,121,131,-1,131,128,129,-1,84,85,133,-1,141,142,143,-1,141,143,144,-1,141,144,145,-1,145,146,147,-1,141,145,147,-1,148,149,150,-1,148,150,151,-1,147,148,151,-1,151,134,135,-1,151,135,136,-1,147,151,136,-1,147,136,137,-1,141,147,137,-1,141,137,138,-1,141,138,139,-1,141,139,140,-1,21,18,135,-1,135,134,21,-1,19,24,136,-1,136,135,19,-1,24,25,137,-1,137,136,24,-1,81,82,138,-1,138,137,81,-1,82,71,139,-1,139,138,82,-1,73,74,140,-1,140,139,73,-1,74,90,141,-1,141,140,74,-1,90,132,142,-1,142,141,90,-1,132,91,143,-1,143,142,132,-1,108,130,144,-1,144,143,108,-1,130,126,145,-1,145,144,130,-1,126,127,146,-1,146,145,126,-1,62,61,147,-1,147,146,62,-1,61,60,148,-1,148,147,61,-1,60,56,149,-1,149,148,60,-1,22,20,150,-1,150,149,22,-1,20,23,151,-1,151,150,20,-1,23,21,134,-1,134,151,23,-1]
Coordinate339 = x3d.Coordinate()

IndexedFaceSet338.coord = Coordinate339
TextureCoordinate340 = x3d.TextureCoordinate()

IndexedFaceSet338.texCoord = TextureCoordinate340

Shape334.geometry = IndexedFaceSet338

Transform333.children.append(Shape334)

HAnimSegment332.children.append(Transform333)

HAnimJoint331.children.append(HAnimSegment332)
HAnimJoint341 = x3d.HAnimJoint()
HAnimJoint341.name = "vc7"
HAnimJoint341.DEF = "hanim_vc7"
HAnimJoint341.center = [0,54.450001,-0.6695]
HAnimJoint341.ulimit = [0,0,0]
HAnimJoint341.llimit = [0,0,0]
HAnimSegment342 = x3d.HAnimSegment()
HAnimSegment342.name = "c7"
HAnimSegment342.DEF = "hanim_c7"
Transform343 = x3d.Transform()
Transform343.translation = [0,54.450001,-0.6695]
Shape344 = x3d.Shape()
Appearance345 = x3d.Appearance()
Material346 = x3d.Material()
Material346.diffuseColor = [0.588,0.588,0.588]

Appearance345.material = Material346
ImageTexture347 = x3d.ImageTexture()
ImageTexture347.USE = "JinLOA3TextureAtlas"

Appearance345.texture = ImageTexture347

Shape344.appearance = Appearance345
IndexedFaceSet348 = x3d.IndexedFaceSet()
IndexedFaceSet348.coordIndex = [5,6,33,-1,33,28,5,-1,34,32,1,-1,1,7,34,-1,30,34,7,-1,7,8,30,-1,28,29,11,-1,11,5,28,-1,29,35,10,-1,10,11,29,-1,14,15,16,-1,16,17,18,-1,18,19,20,-1,16,18,20,-1,20,21,22,-1,22,23,12,-1,20,22,12,-1,16,20,12,-1,14,16,12,-1,13,14,12,-1,1,0,13,-1,13,12,1,-1,0,2,14,-1,14,13,0,-1,2,3,15,-1,15,14,2,-1,3,4,16,-1,16,15,3,-1,4,6,17,-1,17,16,4,-1,6,5,18,-1,18,17,6,-1,5,11,19,-1,19,18,5,-1,11,10,20,-1,20,19,11,-1,10,9,21,-1,21,20,10,-1,9,8,22,-1,22,21,9,-1,8,7,23,-1,23,22,8,-1,7,1,12,-1,12,23,7,-1,0,1,32,-1,32,24,0,-1,2,0,24,-1,24,25,2,-1,3,2,25,-1,25,26,3,-1,4,3,26,-1,26,27,4,-1,6,4,27,-1,27,33,6,-1,8,9,31,-1,31,30,8,-1,9,10,35,-1,35,31,9,-1,38,39,40,-1,40,41,42,-1,42,43,44,-1,40,42,44,-1,44,45,46,-1,46,47,36,-1,44,46,36,-1,40,44,36,-1,38,40,36,-1,37,38,36,-1,24,32,37,-1,37,36,24,-1,32,34,38,-1,38,37,32,-1,34,30,39,-1,39,38,34,-1,30,31,40,-1,40,39,30,-1,31,35,41,-1,41,40,31,-1,35,29,42,-1,42,41,35,-1,29,28,43,-1,43,42,29,-1,28,33,44,-1,44,43,28,-1,33,27,45,-1,45,44,33,-1,27,26,46,-1,46,45,27,-1,26,25,47,-1,47,46,26,-1,25,24,36,-1,36,47,25,-1]
IndexedFaceSet348.creaseAngle = 3.14159
IndexedFaceSet348.texCoordIndex = [5,6,33,-1,33,28,5,-1,34,32,1,-1,1,7,34,-1,30,34,7,-1,7,8,30,-1,28,29,11,-1,11,5,28,-1,29,35,10,-1,10,11,29,-1,14,15,16,-1,16,17,18,-1,18,19,20,-1,16,18,20,-1,20,21,22,-1,22,23,12,-1,20,22,12,-1,16,20,12,-1,14,16,12,-1,13,14,12,-1,1,0,13,-1,13,12,1,-1,0,2,14,-1,14,13,0,-1,2,3,15,-1,15,14,2,-1,3,4,16,-1,16,15,3,-1,4,6,17,-1,17,16,4,-1,6,5,18,-1,18,17,6,-1,5,11,19,-1,19,18,5,-1,11,10,20,-1,20,19,11,-1,10,9,21,-1,21,20,10,-1,9,8,22,-1,22,21,9,-1,8,7,23,-1,23,22,8,-1,7,1,12,-1,12,23,7,-1,0,1,32,-1,32,24,0,-1,2,0,24,-1,24,25,2,-1,3,2,25,-1,25,26,3,-1,4,3,26,-1,26,27,4,-1,6,4,27,-1,27,33,6,-1,8,9,31,-1,31,30,8,-1,9,10,35,-1,35,31,9,-1,38,39,40,-1,40,41,42,-1,42,43,44,-1,40,42,44,-1,44,45,46,-1,46,47,36,-1,44,46,36,-1,40,44,36,-1,38,40,36,-1,37,38,36,-1,24,32,37,-1,37,36,24,-1,32,34,38,-1,38,37,32,-1,34,30,39,-1,39,38,34,-1,30,31,40,-1,40,39,30,-1,31,35,41,-1,41,40,31,-1,35,29,42,-1,42,41,35,-1,29,28,43,-1,43,42,29,-1,28,33,44,-1,44,43,28,-1,33,27,45,-1,45,44,33,-1,27,26,46,-1,46,45,27,-1,26,25,47,-1,47,46,26,-1,25,24,36,-1,36,47,25,-1]
Coordinate349 = x3d.Coordinate()

IndexedFaceSet348.coord = Coordinate349
TextureCoordinate350 = x3d.TextureCoordinate()

IndexedFaceSet348.texCoord = TextureCoordinate350

Shape344.geometry = IndexedFaceSet348

Transform343.children.append(Shape344)

HAnimSegment342.children.append(Transform343)

HAnimJoint341.children.append(HAnimSegment342)
HAnimJoint351 = x3d.HAnimJoint()
HAnimJoint351.name = "vc6"
HAnimJoint351.DEF = "hanim_vc6"
HAnimJoint351.center = [0,54.98,-0.6695]
HAnimJoint351.ulimit = [0,0,0]
HAnimJoint351.llimit = [0,0,0]
HAnimSegment352 = x3d.HAnimSegment()
HAnimSegment352.name = "c6"
HAnimSegment352.DEF = "hanim_c6"
Transform353 = x3d.Transform()
Transform353.translation = [0,54.98,-0.6695]
Shape354 = x3d.Shape()
Appearance355 = x3d.Appearance()
Material356 = x3d.Material()
Material356.diffuseColor = [0.588,0.588,0.588]

Appearance355.material = Material356
ImageTexture357 = x3d.ImageTexture()
ImageTexture357.USE = "JinLOA3TextureAtlas"

Appearance355.texture = ImageTexture357

Shape354.appearance = Appearance355
IndexedFaceSet358 = x3d.IndexedFaceSet()
IndexedFaceSet358.coordIndex = [12,20,8,-1,8,0,12,-1,13,12,0,-1,0,1,13,-1,14,13,1,-1,1,2,14,-1,15,14,2,-1,2,3,15,-1,21,15,3,-1,3,9,21,-1,18,19,7,-1,7,6,18,-1,19,23,11,-1,11,7,19,-1,16,21,9,-1,9,4,16,-1,20,22,10,-1,10,8,20,-1,22,18,6,-1,6,10,22,-1,17,16,4,-1,4,5,17,-1,23,17,5,-1,5,11,23,-1,26,27,28,-1,28,29,30,-1,30,31,32,-1,28,30,32,-1,32,33,34,-1,34,35,24,-1,32,34,24,-1,28,32,24,-1,26,28,24,-1,25,26,24,-1,38,39,40,-1,40,41,42,-1,42,43,44,-1,40,42,44,-1,44,45,46,-1,46,47,36,-1,44,46,36,-1,40,44,36,-1,38,40,36,-1,37,38,36,-1,0,8,25,-1,25,24,0,-1,8,10,26,-1,26,25,8,-1,10,6,27,-1,27,26,10,-1,6,7,28,-1,28,27,6,-1,7,11,29,-1,29,28,7,-1,11,5,30,-1,30,29,11,-1,5,4,31,-1,31,30,5,-1,4,9,32,-1,32,31,4,-1,9,3,33,-1,33,32,9,-1,3,2,34,-1,34,33,3,-1,2,1,35,-1,35,34,2,-1,1,0,24,-1,24,35,1,-1,20,12,37,-1,37,36,20,-1,12,13,38,-1,38,37,12,-1,13,14,39,-1,39,38,13,-1,14,15,40,-1,40,39,14,-1,15,21,41,-1,41,40,15,-1,21,16,42,-1,42,41,21,-1,16,17,43,-1,43,42,16,-1,17,23,44,-1,44,43,17,-1,23,19,45,-1,45,44,23,-1,19,18,46,-1,46,45,19,-1,18,22,47,-1,47,46,18,-1,22,20,36,-1,36,47,22,-1]
IndexedFaceSet358.creaseAngle = 3.14159
IndexedFaceSet358.texCoordIndex = [12,20,8,-1,8,0,12,-1,13,12,0,-1,0,1,13,-1,14,13,1,-1,1,2,14,-1,15,14,2,-1,2,3,15,-1,21,15,3,-1,3,9,21,-1,18,19,7,-1,7,6,18,-1,19,23,11,-1,11,7,19,-1,16,21,9,-1,9,4,16,-1,20,22,10,-1,10,8,20,-1,22,18,6,-1,6,10,22,-1,17,16,4,-1,4,5,17,-1,23,17,5,-1,5,11,23,-1,26,27,28,-1,28,29,30,-1,30,31,32,-1,28,30,32,-1,32,33,34,-1,34,35,24,-1,32,34,24,-1,28,32,24,-1,26,28,24,-1,25,26,24,-1,38,39,40,-1,40,41,42,-1,42,43,44,-1,40,42,44,-1,44,45,46,-1,46,47,36,-1,44,46,36,-1,40,44,36,-1,38,40,36,-1,37,38,36,-1,0,8,25,-1,25,24,0,-1,8,10,26,-1,26,25,8,-1,10,6,27,-1,27,26,10,-1,6,7,28,-1,28,27,6,-1,7,11,29,-1,29,28,7,-1,11,5,30,-1,30,29,11,-1,5,4,31,-1,31,30,5,-1,4,9,32,-1,32,31,4,-1,9,3,33,-1,33,32,9,-1,3,2,34,-1,34,33,3,-1,2,1,35,-1,35,34,2,-1,1,0,24,-1,24,35,1,-1,20,12,37,-1,37,36,20,-1,12,13,38,-1,38,37,12,-1,13,14,39,-1,39,38,13,-1,14,15,40,-1,40,39,14,-1,15,21,41,-1,41,40,15,-1,21,16,42,-1,42,41,21,-1,16,17,43,-1,43,42,16,-1,17,23,44,-1,44,43,17,-1,23,19,45,-1,45,44,23,-1,19,18,46,-1,46,45,19,-1,18,22,47,-1,47,46,18,-1,22,20,36,-1,36,47,22,-1]
Coordinate359 = x3d.Coordinate()

IndexedFaceSet358.coord = Coordinate359
TextureCoordinate360 = x3d.TextureCoordinate()

IndexedFaceSet358.texCoord = TextureCoordinate360

Shape354.geometry = IndexedFaceSet358

Transform353.children.append(Shape354)

HAnimSegment352.children.append(Transform353)

HAnimJoint351.children.append(HAnimSegment352)
HAnimJoint361 = x3d.HAnimJoint()
HAnimJoint361.name = "vc5"
HAnimJoint361.DEF = "hanim_vc5"
HAnimJoint361.center = [0,55.540001,-0.6695]
HAnimJoint361.ulimit = [0,0,0]
HAnimJoint361.llimit = [0,0,0]
HAnimSegment362 = x3d.HAnimSegment()
HAnimSegment362.name = "c5"
HAnimSegment362.DEF = "hanim_c5"
Transform363 = x3d.Transform()
Transform363.translation = [0,55.540001,-0.6695]
Shape364 = x3d.Shape()
Appearance365 = x3d.Appearance()
Material366 = x3d.Material()
Material366.diffuseColor = [0.588,0.588,0.588]

Appearance365.material = Material366
ImageTexture367 = x3d.ImageTexture()
ImageTexture367.USE = "JinLOA3TextureAtlas"

Appearance365.texture = ImageTexture367

Shape364.appearance = Appearance365
IndexedFaceSet368 = x3d.IndexedFaceSet()
IndexedFaceSet368.coordIndex = [12,20,8,-1,8,0,12,-1,13,12,0,-1,0,1,13,-1,14,13,1,-1,1,2,14,-1,15,14,2,-1,2,3,15,-1,21,15,3,-1,3,9,21,-1,18,19,7,-1,7,6,18,-1,19,23,11,-1,11,7,19,-1,16,21,9,-1,9,4,16,-1,20,22,10,-1,10,8,20,-1,22,18,6,-1,6,10,22,-1,17,16,4,-1,4,5,17,-1,23,17,5,-1,5,11,23,-1,26,27,28,-1,28,29,30,-1,30,31,32,-1,28,30,32,-1,32,33,34,-1,34,35,24,-1,32,34,24,-1,28,32,24,-1,26,28,24,-1,25,26,24,-1,38,39,40,-1,40,41,42,-1,42,43,44,-1,40,42,44,-1,44,45,46,-1,46,47,36,-1,44,46,36,-1,40,44,36,-1,38,40,36,-1,37,38,36,-1,0,8,25,-1,25,24,0,-1,8,10,26,-1,26,25,8,-1,10,6,27,-1,27,26,10,-1,6,7,28,-1,28,27,6,-1,7,11,29,-1,29,28,7,-1,11,5,30,-1,30,29,11,-1,5,4,31,-1,31,30,5,-1,4,9,32,-1,32,31,4,-1,9,3,33,-1,33,32,9,-1,3,2,34,-1,34,33,3,-1,2,1,35,-1,35,34,2,-1,1,0,24,-1,24,35,1,-1,20,12,37,-1,37,36,20,-1,12,13,38,-1,38,37,12,-1,13,14,39,-1,39,38,13,-1,14,15,40,-1,40,39,14,-1,15,21,41,-1,41,40,15,-1,21,16,42,-1,42,41,21,-1,16,17,43,-1,43,42,16,-1,17,23,44,-1,44,43,17,-1,23,19,45,-1,45,44,23,-1,19,18,46,-1,46,45,19,-1,18,22,47,-1,47,46,18,-1,22,20,36,-1,36,47,22,-1]
IndexedFaceSet368.creaseAngle = 3.14159
IndexedFaceSet368.texCoordIndex = [12,20,8,-1,8,0,12,-1,13,12,0,-1,0,1,13,-1,14,13,1,-1,1,2,14,-1,15,14,2,-1,2,3,15,-1,21,15,3,-1,3,9,21,-1,18,19,7,-1,7,6,18,-1,19,23,11,-1,11,7,19,-1,16,21,9,-1,9,4,16,-1,20,22,10,-1,10,8,20,-1,22,18,6,-1,6,10,22,-1,17,16,4,-1,4,5,17,-1,23,17,5,-1,5,11,23,-1,26,27,28,-1,28,29,30,-1,30,31,32,-1,28,30,32,-1,32,33,34,-1,34,35,24,-1,32,34,24,-1,28,32,24,-1,26,28,24,-1,25,26,24,-1,38,39,40,-1,40,41,42,-1,42,43,44,-1,40,42,44,-1,44,45,46,-1,46,47,36,-1,44,46,36,-1,40,44,36,-1,38,40,36,-1,37,38,36,-1,0,8,25,-1,25,24,0,-1,8,10,26,-1,26,25,8,-1,10,6,27,-1,27,26,10,-1,6,7,28,-1,28,27,6,-1,7,11,29,-1,29,28,7,-1,11,5,30,-1,30,29,11,-1,5,4,31,-1,31,30,5,-1,4,9,32,-1,32,31,4,-1,9,3,33,-1,33,32,9,-1,3,2,34,-1,34,33,3,-1,2,1,35,-1,35,34,2,-1,1,0,24,-1,24,35,1,-1,20,12,37,-1,37,36,20,-1,12,13,38,-1,38,37,12,-1,13,14,39,-1,39,38,13,-1,14,15,40,-1,40,39,14,-1,15,21,41,-1,41,40,15,-1,21,16,42,-1,42,41,21,-1,16,17,43,-1,43,42,16,-1,17,23,44,-1,44,43,17,-1,23,19,45,-1,45,44,23,-1,19,18,46,-1,46,45,19,-1,18,22,47,-1,47,46,18,-1,22,20,36,-1,36,47,22,-1]
Coordinate369 = x3d.Coordinate()

IndexedFaceSet368.coord = Coordinate369
TextureCoordinate370 = x3d.TextureCoordinate()

IndexedFaceSet368.texCoord = TextureCoordinate370

Shape364.geometry = IndexedFaceSet368

Transform363.children.append(Shape364)

HAnimSegment362.children.append(Transform363)

HAnimJoint361.children.append(HAnimSegment362)
HAnimJoint371 = x3d.HAnimJoint()
HAnimJoint371.name = "vc4"
HAnimJoint371.DEF = "hanim_vc4"
HAnimJoint371.center = [0,56.080002,-0.6695]
HAnimJoint371.ulimit = [0,0,0]
HAnimJoint371.llimit = [0,0,0]
HAnimSegment372 = x3d.HAnimSegment()
HAnimSegment372.name = "c4"
HAnimSegment372.DEF = "hanim_c4"
Transform373 = x3d.Transform()
Transform373.translation = [0,56.080002,-0.6695]
Shape374 = x3d.Shape()
Appearance375 = x3d.Appearance()
Material376 = x3d.Material()
Material376.diffuseColor = [0.588,0.588,0.588]

Appearance375.material = Material376
ImageTexture377 = x3d.ImageTexture()
ImageTexture377.USE = "JinLOA3TextureAtlas"

Appearance375.texture = ImageTexture377

Shape374.appearance = Appearance375
IndexedFaceSet378 = x3d.IndexedFaceSet()
IndexedFaceSet378.coordIndex = [12,20,8,-1,8,0,12,-1,13,12,0,-1,0,1,13,-1,14,13,1,-1,1,2,14,-1,15,14,2,-1,2,3,15,-1,21,15,3,-1,3,9,21,-1,18,19,7,-1,7,6,18,-1,19,23,11,-1,11,7,19,-1,9,4,16,-1,16,21,9,-1,10,8,20,-1,20,22,10,-1,6,10,22,-1,22,18,6,-1,4,5,17,-1,17,16,4,-1,5,11,23,-1,23,17,5,-1,26,27,28,-1,28,29,30,-1,30,31,32,-1,28,30,32,-1,32,33,34,-1,34,35,24,-1,32,34,24,-1,28,32,24,-1,26,28,24,-1,25,26,24,-1,38,39,40,-1,40,41,42,-1,42,43,44,-1,40,42,44,-1,44,45,46,-1,46,47,36,-1,44,46,36,-1,40,44,36,-1,38,40,36,-1,37,38,36,-1,0,8,25,-1,25,24,0,-1,8,10,26,-1,26,25,8,-1,10,6,27,-1,27,26,10,-1,6,7,28,-1,28,27,6,-1,7,11,29,-1,29,28,7,-1,11,5,30,-1,30,29,11,-1,5,4,31,-1,31,30,5,-1,4,9,32,-1,32,31,4,-1,9,3,33,-1,33,32,9,-1,3,2,34,-1,34,33,3,-1,2,1,35,-1,35,34,2,-1,1,0,24,-1,24,35,1,-1,20,12,37,-1,37,36,20,-1,12,13,38,-1,38,37,12,-1,13,14,39,-1,39,38,13,-1,14,15,40,-1,40,39,14,-1,15,21,41,-1,41,40,15,-1,21,16,42,-1,42,41,21,-1,16,17,43,-1,43,42,16,-1,17,23,44,-1,44,43,17,-1,23,19,45,-1,45,44,23,-1,19,18,46,-1,46,45,19,-1,18,22,47,-1,47,46,18,-1,22,20,36,-1,36,47,22,-1]
IndexedFaceSet378.creaseAngle = 3.14159
IndexedFaceSet378.texCoordIndex = [12,20,8,-1,8,0,12,-1,13,12,0,-1,0,1,13,-1,14,13,1,-1,1,2,14,-1,15,14,2,-1,2,3,15,-1,21,15,3,-1,3,9,21,-1,18,19,7,-1,7,6,18,-1,19,23,11,-1,11,7,19,-1,9,4,16,-1,16,21,9,-1,10,8,20,-1,20,22,10,-1,6,10,22,-1,22,18,6,-1,4,5,17,-1,17,16,4,-1,5,11,23,-1,23,17,5,-1,26,27,28,-1,28,29,30,-1,30,31,32,-1,28,30,32,-1,32,33,34,-1,34,35,24,-1,32,34,24,-1,28,32,24,-1,26,28,24,-1,25,26,24,-1,38,39,40,-1,40,41,42,-1,42,43,44,-1,40,42,44,-1,44,45,46,-1,46,47,36,-1,44,46,36,-1,40,44,36,-1,38,40,36,-1,37,38,36,-1,0,8,25,-1,25,24,0,-1,8,10,26,-1,26,25,8,-1,10,6,27,-1,27,26,10,-1,6,7,28,-1,28,27,6,-1,7,11,29,-1,29,28,7,-1,11,5,30,-1,30,29,11,-1,5,4,31,-1,31,30,5,-1,4,9,32,-1,32,31,4,-1,9,3,33,-1,33,32,9,-1,3,2,34,-1,34,33,3,-1,2,1,35,-1,35,34,2,-1,1,0,24,-1,24,35,1,-1,20,12,37,-1,37,36,20,-1,12,13,38,-1,38,37,12,-1,13,14,39,-1,39,38,13,-1,14,15,40,-1,40,39,14,-1,15,21,41,-1,41,40,15,-1,21,16,42,-1,42,41,21,-1,16,17,43,-1,43,42,16,-1,17,23,44,-1,44,43,17,-1,23,19,45,-1,45,44,23,-1,19,18,46,-1,46,45,19,-1,18,22,47,-1,47,46,18,-1,22,20,36,-1,36,47,22,-1]
Coordinate379 = x3d.Coordinate()

IndexedFaceSet378.coord = Coordinate379
TextureCoordinate380 = x3d.TextureCoordinate()

IndexedFaceSet378.texCoord = TextureCoordinate380

Shape374.geometry = IndexedFaceSet378

Transform373.children.append(Shape374)

HAnimSegment372.children.append(Transform373)

HAnimJoint371.children.append(HAnimSegment372)
HAnimJoint381 = x3d.HAnimJoint()
HAnimJoint381.name = "vc3"
HAnimJoint381.DEF = "hanim_vc3"
HAnimJoint381.center = [0,56.66,-0.6695]
HAnimJoint381.ulimit = [0,0,0]
HAnimJoint381.llimit = [0,0,0]
HAnimSegment382 = x3d.HAnimSegment()
HAnimSegment382.name = "c3"
HAnimSegment382.DEF = "hanim_c3"
Transform383 = x3d.Transform()
Transform383.translation = [0,56.66,-0.6695]
Shape384 = x3d.Shape()
Appearance385 = x3d.Appearance()
Material386 = x3d.Material()
Material386.diffuseColor = [0.588,0.588,0.588]

Appearance385.material = Material386
ImageTexture387 = x3d.ImageTexture()
ImageTexture387.USE = "JinLOA3TextureAtlas"

Appearance385.texture = ImageTexture387

Shape384.appearance = Appearance385
IndexedFaceSet388 = x3d.IndexedFaceSet()
IndexedFaceSet388.coordIndex = [8,0,12,-1,12,20,8,-1,0,1,13,-1,13,12,0,-1,1,2,14,-1,14,13,1,-1,2,3,15,-1,15,14,2,-1,3,9,21,-1,21,15,3,-1,7,6,18,-1,18,19,7,-1,11,7,19,-1,19,23,11,-1,9,4,16,-1,16,21,9,-1,10,8,20,-1,20,22,10,-1,6,10,22,-1,22,18,6,-1,4,5,17,-1,17,16,4,-1,5,11,23,-1,23,17,5,-1,26,27,28,-1,28,29,30,-1,30,31,32,-1,28,30,32,-1,32,33,34,-1,34,35,24,-1,32,34,24,-1,28,32,24,-1,26,28,24,-1,25,26,24,-1,38,39,40,-1,40,41,42,-1,42,43,44,-1,40,42,44,-1,44,45,46,-1,46,47,36,-1,44,46,36,-1,40,44,36,-1,38,40,36,-1,37,38,36,-1,0,8,25,-1,25,24,0,-1,8,10,26,-1,26,25,8,-1,10,6,27,-1,27,26,10,-1,6,7,28,-1,28,27,6,-1,7,11,29,-1,29,28,7,-1,11,5,30,-1,30,29,11,-1,5,4,31,-1,31,30,5,-1,4,9,32,-1,32,31,4,-1,9,3,33,-1,33,32,9,-1,3,2,34,-1,34,33,3,-1,2,1,35,-1,35,34,2,-1,1,0,24,-1,24,35,1,-1,20,12,37,-1,37,36,20,-1,12,13,38,-1,38,37,12,-1,13,14,39,-1,39,38,13,-1,14,15,40,-1,40,39,14,-1,15,21,41,-1,41,40,15,-1,21,16,42,-1,42,41,21,-1,16,17,43,-1,43,42,16,-1,17,23,44,-1,44,43,17,-1,23,19,45,-1,45,44,23,-1,19,18,46,-1,46,45,19,-1,18,22,47,-1,47,46,18,-1,22,20,36,-1,36,47,22,-1]
IndexedFaceSet388.creaseAngle = 3.14159
IndexedFaceSet388.texCoordIndex = [8,0,12,-1,12,20,8,-1,0,1,13,-1,13,12,0,-1,1,2,14,-1,14,13,1,-1,2,3,15,-1,15,14,2,-1,3,9,21,-1,21,15,3,-1,7,6,18,-1,18,19,7,-1,11,7,19,-1,19,23,11,-1,9,4,16,-1,16,21,9,-1,10,8,20,-1,20,22,10,-1,6,10,22,-1,22,18,6,-1,4,5,17,-1,17,16,4,-1,5,11,23,-1,23,17,5,-1,26,27,28,-1,28,29,30,-1,30,31,32,-1,28,30,32,-1,32,33,34,-1,34,35,24,-1,32,34,24,-1,28,32,24,-1,26,28,24,-1,25,26,24,-1,38,39,40,-1,40,41,42,-1,42,43,44,-1,40,42,44,-1,44,45,46,-1,46,47,36,-1,44,46,36,-1,40,44,36,-1,38,40,36,-1,37,38,36,-1,0,8,25,-1,25,24,0,-1,8,10,26,-1,26,25,8,-1,10,6,27,-1,27,26,10,-1,6,7,28,-1,28,27,6,-1,7,11,29,-1,29,28,7,-1,11,5,30,-1,30,29,11,-1,5,4,31,-1,31,30,5,-1,4,9,32,-1,32,31,4,-1,9,3,33,-1,33,32,9,-1,3,2,34,-1,34,33,3,-1,2,1,35,-1,35,34,2,-1,1,0,24,-1,24,35,1,-1,20,12,37,-1,37,36,20,-1,12,13,38,-1,38,37,12,-1,13,14,39,-1,39,38,13,-1,14,15,40,-1,40,39,14,-1,15,21,41,-1,41,40,15,-1,21,16,42,-1,42,41,21,-1,16,17,43,-1,43,42,16,-1,17,23,44,-1,44,43,17,-1,23,19,45,-1,45,44,23,-1,19,18,46,-1,46,45,19,-1,18,22,47,-1,47,46,18,-1,22,20,36,-1,36,47,22,-1]
Coordinate389 = x3d.Coordinate()

IndexedFaceSet388.coord = Coordinate389
TextureCoordinate390 = x3d.TextureCoordinate()

IndexedFaceSet388.texCoord = TextureCoordinate390

Shape384.geometry = IndexedFaceSet388

Transform383.children.append(Shape384)

HAnimSegment382.children.append(Transform383)

HAnimJoint381.children.append(HAnimSegment382)
HAnimJoint391 = x3d.HAnimJoint()
HAnimJoint391.name = "vc2"
HAnimJoint391.DEF = "hanim_vc2"
HAnimJoint391.center = [0,57.169998,-0.6695]
HAnimJoint391.ulimit = [0,0,0]
HAnimJoint391.llimit = [0,0,0]
HAnimSegment392 = x3d.HAnimSegment()
HAnimSegment392.name = "c2"
HAnimSegment392.DEF = "hanim_c2"
Transform393 = x3d.Transform()
Transform393.translation = [0,57.169998,-0.6695]
Shape394 = x3d.Shape()
Appearance395 = x3d.Appearance()
Material396 = x3d.Material()
Material396.diffuseColor = [0.588,0.588,0.588]

Appearance395.material = Material396
ImageTexture397 = x3d.ImageTexture()
ImageTexture397.USE = "JinLOA3TextureAtlas"

Appearance395.texture = ImageTexture397

Shape394.appearance = Appearance395
IndexedFaceSet398 = x3d.IndexedFaceSet()
IndexedFaceSet398.coordIndex = [14,15,16,-1,16,17,18,-1,18,19,20,-1,16,18,20,-1,20,21,22,-1,22,23,12,-1,20,22,12,-1,16,20,12,-1,14,16,12,-1,13,14,12,-1,0,1,13,-1,13,12,0,-1,1,7,14,-1,14,13,1,-1,7,8,15,-1,15,14,7,-1,8,9,16,-1,16,15,8,-1,9,10,17,-1,17,16,9,-1,10,11,18,-1,18,17,10,-1,11,6,19,-1,19,18,11,-1,6,5,20,-1,20,19,6,-1,5,4,21,-1,21,20,5,-1,4,3,22,-1,22,21,4,-1,3,2,23,-1,23,22,3,-1,2,0,12,-1,12,23,2,-1,1,0,24,-1,24,32,1,-1,0,2,25,-1,25,24,0,-1,2,3,26,-1,26,25,2,-1,3,4,27,-1,27,26,3,-1,4,5,33,-1,33,27,4,-1,9,8,30,-1,30,31,9,-1,10,9,31,-1,31,35,10,-1,5,6,28,-1,28,33,5,-1,7,1,32,-1,32,34,7,-1,8,7,34,-1,34,30,8,-1,6,11,29,-1,29,28,6,-1,11,10,35,-1,35,29,11,-1,38,39,40,-1,40,41,42,-1,42,43,44,-1,40,42,44,-1,44,45,46,-1,46,47,36,-1,44,46,36,-1,40,44,36,-1,38,40,36,-1,37,38,36,-1,32,24,37,-1,37,36,32,-1,24,25,38,-1,38,37,24,-1,25,26,39,-1,39,38,25,-1,26,27,40,-1,40,39,26,-1,27,33,41,-1,41,40,27,-1,33,28,42,-1,42,41,33,-1,28,29,43,-1,43,42,28,-1,29,35,44,-1,44,43,29,-1,35,31,45,-1,45,44,35,-1,31,30,46,-1,46,45,31,-1,30,34,47,-1,47,46,30,-1,34,32,36,-1,36,47,34,-1]
IndexedFaceSet398.creaseAngle = 3.14159
IndexedFaceSet398.texCoordIndex = [14,15,16,-1,16,17,18,-1,18,19,20,-1,16,18,20,-1,20,21,22,-1,22,23,12,-1,20,22,12,-1,16,20,12,-1,14,16,12,-1,13,14,12,-1,0,1,13,-1,13,12,0,-1,1,7,14,-1,14,13,1,-1,7,8,15,-1,15,14,7,-1,8,9,16,-1,16,15,8,-1,9,10,17,-1,17,16,9,-1,10,11,18,-1,18,17,10,-1,11,6,19,-1,19,18,11,-1,6,5,20,-1,20,19,6,-1,5,4,21,-1,21,20,5,-1,4,3,22,-1,22,21,4,-1,3,2,23,-1,23,22,3,-1,2,0,12,-1,12,23,2,-1,1,0,24,-1,24,32,1,-1,0,2,25,-1,25,24,0,-1,2,3,26,-1,26,25,2,-1,3,4,27,-1,27,26,3,-1,4,5,33,-1,33,27,4,-1,9,8,30,-1,30,31,9,-1,10,9,31,-1,31,35,10,-1,5,6,28,-1,28,33,5,-1,7,1,32,-1,32,34,7,-1,8,7,34,-1,34,30,8,-1,6,11,29,-1,29,28,6,-1,11,10,35,-1,35,29,11,-1,38,39,40,-1,40,41,42,-1,42,43,44,-1,40,42,44,-1,44,45,46,-1,46,47,36,-1,44,46,36,-1,40,44,36,-1,38,40,36,-1,37,38,36,-1,32,24,37,-1,37,36,32,-1,24,25,38,-1,38,37,24,-1,25,26,39,-1,39,38,25,-1,26,27,40,-1,40,39,26,-1,27,33,41,-1,41,40,27,-1,33,28,42,-1,42,41,33,-1,28,29,43,-1,43,42,28,-1,29,35,44,-1,44,43,29,-1,35,31,45,-1,45,44,35,-1,31,30,46,-1,46,45,31,-1,30,34,47,-1,47,46,30,-1,34,32,36,-1,36,47,34,-1]
Coordinate399 = x3d.Coordinate()

IndexedFaceSet398.coord = Coordinate399
TextureCoordinate400 = x3d.TextureCoordinate()

IndexedFaceSet398.texCoord = TextureCoordinate400

Shape394.geometry = IndexedFaceSet398

Transform393.children.append(Shape394)

HAnimSegment392.children.append(Transform393)

HAnimJoint391.children.append(HAnimSegment392)
HAnimJoint401 = x3d.HAnimJoint()
HAnimJoint401.name = "vc1"
HAnimJoint401.DEF = "hanim_vc1"
HAnimJoint401.center = [0,57.689999,-0.6695]
HAnimJoint401.ulimit = [0,0,0]
HAnimJoint401.llimit = [0,0,0]
HAnimSegment402 = x3d.HAnimSegment()
HAnimSegment402.name = "c1"
HAnimSegment402.DEF = "hanim_c1"
Transform403 = x3d.Transform()
Transform403.translation = [0,57.689999,-0.6695]
Shape404 = x3d.Shape()
Appearance405 = x3d.Appearance()
Material406 = x3d.Material()
Material406.diffuseColor = [0.588,0.588,0.588]

Appearance405.material = Material406
ImageTexture407 = x3d.ImageTexture()
ImageTexture407.USE = "JinLOA3TextureAtlas"

Appearance405.texture = ImageTexture407

Shape404.appearance = Appearance405
IndexedFaceSet408 = x3d.IndexedFaceSet()
IndexedFaceSet408.coordIndex = [8,0,12,-1,12,20,8,-1,0,1,13,-1,13,12,0,-1,1,2,14,-1,14,13,1,-1,2,3,15,-1,15,14,2,-1,3,9,21,-1,21,15,3,-1,7,6,18,-1,18,19,7,-1,11,7,19,-1,19,23,11,-1,9,4,16,-1,16,21,9,-1,10,8,20,-1,20,22,10,-1,6,10,22,-1,22,18,6,-1,4,5,17,-1,17,16,4,-1,5,11,23,-1,23,17,5,-1,26,27,28,-1,28,29,30,-1,30,31,32,-1,28,30,32,-1,32,33,34,-1,34,35,24,-1,32,34,24,-1,28,32,24,-1,26,28,24,-1,25,26,24,-1,38,39,40,-1,40,41,42,-1,42,43,44,-1,40,42,44,-1,44,45,46,-1,46,47,36,-1,44,46,36,-1,40,44,36,-1,38,40,36,-1,37,38,36,-1,0,8,25,-1,25,24,0,-1,8,10,26,-1,26,25,8,-1,10,6,27,-1,27,26,10,-1,6,7,28,-1,28,27,6,-1,7,11,29,-1,29,28,7,-1,11,5,30,-1,30,29,11,-1,5,4,31,-1,31,30,5,-1,4,9,32,-1,32,31,4,-1,9,3,33,-1,33,32,9,-1,3,2,34,-1,34,33,3,-1,2,1,35,-1,35,34,2,-1,1,0,24,-1,24,35,1,-1,20,12,37,-1,37,36,20,-1,12,13,38,-1,38,37,12,-1,13,14,39,-1,39,38,13,-1,14,15,40,-1,40,39,14,-1,15,21,41,-1,41,40,15,-1,21,16,42,-1,42,41,21,-1,16,17,43,-1,43,42,16,-1,17,23,44,-1,44,43,17,-1,23,19,45,-1,45,44,23,-1,19,18,46,-1,46,45,19,-1,18,22,47,-1,47,46,18,-1,22,20,36,-1,36,47,22,-1]
IndexedFaceSet408.creaseAngle = 3.14159
IndexedFaceSet408.texCoordIndex = [8,0,12,-1,12,20,8,-1,0,1,13,-1,13,12,0,-1,1,2,14,-1,14,13,1,-1,2,3,15,-1,15,14,2,-1,3,9,21,-1,21,15,3,-1,7,6,18,-1,18,19,7,-1,11,7,19,-1,19,23,11,-1,9,4,16,-1,16,21,9,-1,10,8,20,-1,20,22,10,-1,6,10,22,-1,22,18,6,-1,4,5,17,-1,17,16,4,-1,5,11,23,-1,23,17,5,-1,26,27,28,-1,28,29,30,-1,30,31,32,-1,28,30,32,-1,32,33,34,-1,34,35,24,-1,32,34,24,-1,28,32,24,-1,26,28,24,-1,25,26,24,-1,38,39,40,-1,40,41,42,-1,42,43,44,-1,40,42,44,-1,44,45,46,-1,46,47,36,-1,44,46,36,-1,40,44,36,-1,38,40,36,-1,37,38,36,-1,0,8,25,-1,25,24,0,-1,8,10,26,-1,26,25,8,-1,10,6,27,-1,27,26,10,-1,6,7,28,-1,28,27,6,-1,7,11,29,-1,29,28,7,-1,11,5,30,-1,30,29,11,-1,5,4,31,-1,31,30,5,-1,4,9,32,-1,32,31,4,-1,9,3,33,-1,33,32,9,-1,3,2,34,-1,34,33,3,-1,2,1,35,-1,35,34,2,-1,1,0,24,-1,24,35,1,-1,20,12,37,-1,37,36,20,-1,12,13,38,-1,38,37,12,-1,13,14,39,-1,39,38,13,-1,14,15,40,-1,40,39,14,-1,15,21,41,-1,41,40,15,-1,21,16,42,-1,42,41,21,-1,16,17,43,-1,43,42,16,-1,17,23,44,-1,44,43,17,-1,23,19,45,-1,45,44,23,-1,19,18,46,-1,46,45,19,-1,18,22,47,-1,47,46,18,-1,22,20,36,-1,36,47,22,-1]
Coordinate409 = x3d.Coordinate()

IndexedFaceSet408.coord = Coordinate409
TextureCoordinate410 = x3d.TextureCoordinate()

IndexedFaceSet408.texCoord = TextureCoordinate410

Shape404.geometry = IndexedFaceSet408

Transform403.children.append(Shape404)

HAnimSegment402.children.append(Transform403)

HAnimJoint401.children.append(HAnimSegment402)
HAnimJoint411 = x3d.HAnimJoint()
HAnimJoint411.name = "skullbase"
HAnimJoint411.DEF = "hanim_skullbase"
HAnimJoint411.center = [0,57.43,-0.6863]
HAnimJoint411.ulimit = [0,0,0]
HAnimJoint411.llimit = [0,0,0]
HAnimSegment412 = x3d.HAnimSegment()
HAnimSegment412.name = "skull"
HAnimSegment412.DEF = "hanim_skull"
Transform413 = x3d.Transform()
Transform413.translation = [0,57.43,-0.6863]
Shape414 = x3d.Shape()
Appearance415 = x3d.Appearance()
Material416 = x3d.Material()
Material416.diffuseColor = [0.588,0.588,0.588]

Appearance415.material = Material416
ImageTexture417 = x3d.ImageTexture()
ImageTexture417.USE = "JinLOA3TextureAtlas"

Appearance415.texture = ImageTexture417

Shape414.appearance = Appearance415
IndexedFaceSet418 = x3d.IndexedFaceSet()
IndexedFaceSet418.coordIndex = [51,38,41,-1,41,43,51,-1,43,52,171,-1,171,151,43,-1,49,42,41,-1,41,38,49,-1,44,186,171,-1,171,52,44,-1,78,76,51,-1,51,43,78,-1,189,78,43,-1,43,151,189,-1,9,172,13,-1,13,10,9,-1,73,193,9,-1,9,10,73,-1,11,50,27,-1,16,13,172,-1,13,67,14,-1,68,15,14,-1,7,6,67,-1,13,16,67,-1,7,67,16,-1,16,172,173,-1,7,16,136,-1,7,136,130,-1,131,132,173,-1,68,19,18,-1,18,15,68,-1,20,32,18,-1,17,8,32,-1,15,66,13,-1,13,14,15,-1,32,23,24,-1,24,17,32,-1,21,24,23,-1,21,22,24,-1,24,22,17,-1,27,25,11,-1,25,31,11,-1,22,28,17,-1,27,30,29,-1,12,26,29,-1,26,27,29,-1,27,28,30,-1,30,28,22,-1,6,14,67,-1,1,34,31,-1,34,36,35,-1,34,35,31,-1,34,1,36,-1,49,37,1,-1,1,40,49,-1,39,37,49,-1,49,38,39,-1,37,39,1,-1,42,49,40,-1,40,0,42,-1,44,52,0,-1,186,44,0,-1,0,149,186,-1,51,76,45,-1,45,76,77,-1,53,45,77,-1,1,39,45,-1,45,53,1,-1,45,39,38,-1,38,51,45,-1,53,77,46,-1,77,74,33,-1,33,46,77,-1,1,53,46,-1,46,36,1,-1,46,33,35,-1,35,36,46,-1,74,50,33,-1,8,17,47,-1,11,31,50,-1,35,33,50,-1,31,35,50,-1,50,74,75,-1,47,75,8,-1,27,50,28,-1,28,50,47,-1,28,47,17,-1,75,73,48,-1,48,73,10,-1,66,48,10,-1,10,13,66,-1,75,66,8,-1,66,75,48,-1,8,66,18,-1,18,32,8,-1,15,18,66,-1,47,50,75,-1,41,52,43,-1,42,0,41,-1,0,52,41,-1,0,54,149,-1,244,245,54,-1,0,56,54,-1,0,40,55,-1,55,57,0,-1,3,57,55,-1,0,57,56,-1,3,62,5,-1,5,62,58,-1,3,64,62,-1,2,61,62,-1,62,64,2,-1,3,60,64,-1,55,40,59,-1,64,60,59,-1,64,59,135,-1,149,54,245,-1,5,57,3,-1,54,5,244,-1,152,63,61,-1,153,63,152,-1,63,5,58,-1,153,244,63,-1,244,5,63,-1,58,61,63,-1,58,62,61,-1,56,5,54,-1,56,57,5,-1,60,3,55,-1,60,55,59,-1,1,133,135,-1,59,40,1,-1,59,1,135,-1,65,135,133,-1,2,65,133,-1,2,64,65,-1,64,135,65,-1,73,75,69,-1,263,193,73,-1,73,69,263,-1,69,75,74,-1,74,71,69,-1,71,74,77,-1,77,72,71,-1,69,71,266,-1,266,263,69,-1,72,70,266,-1,266,71,72,-1,78,72,77,-1,77,76,78,-1,189,70,72,-1,72,78,189,-1,138,123,113,-1,79,122,123,-1,122,79,80,-1,137,124,81,-1,137,81,82,-1,137,82,83,-1,83,79,137,-1,79,83,80,-1,84,116,122,-1,124,84,122,-1,84,119,116,-1,123,122,113,-1,113,122,109,-1,115,138,113,-1,113,114,115,-1,117,286,158,-1,158,112,117,-1,122,116,109,-1,79,123,133,-1,133,123,138,-1,133,137,79,-1,129,138,115,-1,110,117,112,-1,111,117,110,-1,2,133,138,-1,109,85,113,-1,86,113,85,-1,107,294,160,-1,160,126,107,-1,107,126,125,-1,125,108,107,-1,125,127,87,-1,87,108,125,-1,108,87,103,-1,103,104,108,-1,114,301,154,-1,154,115,114,-1,302,114,86,-1,86,159,302,-1,114,113,86,-1,116,105,109,-1,109,105,87,-1,85,88,86,-1,109,87,85,-1,104,174,305,-1,305,108,104,-1,305,175,108,-1,105,103,87,-1,307,91,170,-1,170,150,307,-1,174,104,95,-1,95,162,174,-1,311,150,170,-1,170,177,311,-1,116,90,105,-1,89,90,116,-1,94,168,167,-1,167,93,94,-1,105,90,96,-1,97,95,104,-1,104,103,97,-1,120,121,95,-1,95,97,120,-1,105,96,97,-1,97,103,105,-1,120,97,96,-1,96,98,120,-1,121,100,95,-1,163,91,162,-1,93,170,99,-1,98,96,90,-1,90,101,98,-1,99,163,100,-1,110,112,92,-1,101,90,89,-1,89,106,101,-1,92,112,165,-1,165,177,170,-1,175,294,107,-1,107,108,175,-1,119,89,116,-1,118,111,119,-1,118,117,111,-1,152,138,129,-1,2,138,61,-1,61,138,152,-1,87,127,88,-1,88,85,87,-1,124,119,84,-1,119,111,164,-1,111,166,164,-1,111,110,166,-1,92,166,110,-1,133,4,137,-1,133,134,4,-1,160,176,128,-1,128,126,160,-1,126,128,127,-1,127,125,126,-1,80,81,124,-1,124,122,80,-1,82,81,80,-1,80,83,82,-1,129,115,154,-1,154,152,129,-1,94,140,139,-1,139,102,94,-1,93,141,140,-1,140,94,93,-1,99,142,141,-1,141,93,99,-1,100,143,142,-1,142,99,100,-1,121,144,143,-1,143,100,121,-1,120,145,144,-1,144,121,120,-1,98,146,145,-1,145,120,98,-1,101,147,146,-1,146,98,101,-1,106,148,147,-1,147,101,106,-1,106,102,139,-1,139,148,106,-1,114,302,301,-1,88,127,155,-1,155,157,88,-1,127,161,156,-1,156,155,127,-1,352,353,156,-1,156,161,352,-1,156,353,354,-1,155,156,354,-1,155,354,157,-1,127,128,161,-1,161,128,176,-1,176,352,161,-1,168,94,102,-1,102,169,168,-1,170,93,167,-1,169,102,106,-1,106,164,169,-1,170,91,99,-1,99,91,163,-1,100,163,162,-1,162,95,100,-1,91,307,174,-1,174,162,91,-1,164,106,89,-1,164,89,119,-1,165,170,167,-1,92,165,167,-1,167,168,92,-1,166,92,168,-1,168,169,166,-1,164,166,169,-1,165,112,177,-1,177,112,158,-1,158,311,177,-1,180,179,178,-1,178,181,180,-1,179,151,171,-1,171,182,179,-1,183,181,178,-1,178,184,183,-1,185,182,171,-1,171,186,185,-1,187,179,180,-1,180,188,187,-1,189,151,179,-1,179,187,189,-1,9,191,190,-1,190,172,9,-1,192,191,9,-1,9,193,192,-1,194,196,195,-1,197,172,190,-1,190,199,198,-1,200,199,201,-1,202,198,203,-1,190,198,197,-1,202,197,198,-1,197,173,172,-1,202,204,197,-1,202,205,204,-1,206,173,207,-1,200,201,208,-1,208,209,200,-1,210,208,211,-1,212,211,213,-1,201,199,190,-1,190,214,201,-1,211,212,215,-1,215,216,211,-1,217,216,215,-1,217,215,218,-1,215,212,218,-1,196,194,219,-1,219,194,220,-1,218,212,221,-1,196,223,222,-1,224,223,225,-1,225,223,196,-1,196,222,221,-1,222,218,221,-1,203,198,199,-1,226,220,227,-1,227,229,228,-1,227,220,229,-1,227,228,226,-1,183,230,226,-1,226,231,183,-1,232,181,183,-1,183,231,232,-1,231,226,232,-1,184,233,230,-1,230,183,184,-1,185,233,182,-1,186,149,233,-1,233,185,186,-1,180,234,188,-1,234,235,188,-1,236,235,234,-1,226,236,234,-1,234,232,226,-1,234,180,181,-1,181,232,234,-1,236,237,235,-1,235,237,238,-1,238,239,235,-1,226,228,237,-1,237,236,226,-1,237,228,229,-1,229,238,237,-1,239,238,195,-1,213,240,212,-1,194,195,220,-1,229,195,238,-1,220,195,229,-1,195,241,239,-1,240,213,241,-1,196,221,195,-1,221,240,195,-1,221,212,240,-1,241,242,192,-1,242,191,192,-1,214,190,191,-1,191,242,214,-1,241,213,214,-1,214,242,241,-1,213,211,208,-1,208,214,213,-1,201,214,208,-1,240,241,195,-1,178,179,182,-1,184,178,233,-1,233,178,182,-1,233,149,243,-1,244,243,245,-1,233,243,246,-1,233,248,247,-1,247,230,233,-1,249,247,248,-1,233,246,248,-1,249,251,250,-1,251,252,250,-1,249,250,253,-1,254,253,250,-1,250,255,254,-1,249,253,256,-1,247,257,230,-1,253,257,256,-1,253,258,257,-1,149,245,243,-1,251,249,248,-1,243,244,251,-1,152,255,259,-1,153,152,259,-1,259,252,251,-1,153,259,244,-1,244,259,251,-1,252,259,255,-1,252,255,250,-1,246,243,251,-1,246,251,248,-1,256,247,249,-1,256,257,247,-1,226,258,260,-1,257,226,230,-1,257,258,226,-1,261,260,258,-1,254,260,261,-1,254,261,253,-1,253,261,258,-1,192,262,241,-1,263,262,192,-1,192,193,263,-1,262,264,239,-1,239,241,262,-1,264,265,235,-1,235,239,264,-1,262,263,266,-1,266,264,262,-1,265,264,266,-1,266,70,265,-1,187,188,235,-1,235,265,187,-1,189,187,265,-1,265,70,189,-1,267,269,268,-1,270,268,271,-1,271,272,270,-1,273,275,274,-1,273,276,275,-1,273,270,277,-1,277,276,273,-1,270,272,277,-1,278,271,279,-1,274,271,278,-1,278,279,280,-1,268,269,271,-1,269,281,271,-1,283,282,269,-1,269,267,283,-1,285,284,158,-1,158,286,285,-1,271,281,279,-1,270,260,268,-1,260,267,268,-1,260,270,273,-1,287,283,267,-1,288,284,285,-1,289,288,285,-1,254,267,260,-1,281,269,290,-1,291,290,269,-1,293,292,160,-1,160,294,293,-1,293,296,295,-1,295,292,293,-1,295,296,297,-1,297,298,295,-1,296,300,299,-1,299,297,296,-1,282,283,154,-1,154,301,282,-1,302,159,291,-1,291,282,302,-1,282,291,269,-1,279,281,303,-1,281,297,303,-1,290,291,304,-1,281,290,297,-1,300,296,305,-1,305,174,300,-1,305,296,175,-1,303,297,299,-1,307,150,306,-1,306,308,307,-1,174,310,309,-1,309,300,174,-1,311,312,306,-1,306,150,311,-1,279,303,313,-1,314,279,313,-1,315,318,317,-1,317,316,315,-1,303,319,313,-1,320,299,300,-1,300,309,320,-1,321,320,309,-1,309,322,321,-1,303,299,320,-1,320,319,303,-1,321,323,319,-1,319,320,321,-1,322,309,324,-1,325,310,308,-1,318,326,306,-1,323,327,313,-1,313,319,323,-1,326,324,325,-1,288,328,284,-1,327,329,314,-1,314,313,327,-1,328,330,284,-1,330,306,312,-1,175,293,294,-1,293,175,296,-1,280,279,314,-1,331,280,289,-1,331,289,285,-1,152,287,267,-1,254,255,267,-1,255,152,267,-1,297,290,304,-1,304,298,297,-1,274,278,280,-1,280,332,289,-1,289,332,333,-1,289,333,288,-1,328,288,333,-1,260,273,334,-1,260,334,335,-1,160,292,336,-1,336,176,160,-1,292,295,298,-1,298,336,292,-1,272,271,274,-1,274,275,272,-1,276,277,272,-1,272,275,276,-1,287,152,154,-1,154,283,287,-1,315,337,339,-1,339,338,315,-1,318,315,338,-1,338,340,318,-1,326,318,340,-1,340,341,326,-1,324,326,341,-1,341,342,324,-1,322,324,342,-1,342,343,322,-1,321,322,343,-1,343,344,321,-1,323,321,344,-1,344,345,323,-1,327,323,345,-1,345,346,327,-1,329,327,346,-1,346,347,329,-1,329,347,339,-1,339,337,329,-1,282,301,302,-1,304,349,348,-1,348,298,304,-1,298,348,351,-1,351,350,298,-1,352,350,351,-1,351,353,352,-1,348,349,354,-1,354,353,351,-1,348,354,351,-1,298,350,336,-1,350,352,176,-1,176,336,350,-1,316,355,337,-1,337,315,316,-1,306,317,318,-1,355,332,329,-1,329,337,355,-1,306,326,308,-1,326,325,308,-1,324,309,310,-1,310,325,324,-1,308,310,174,-1,174,307,308,-1,332,314,329,-1,332,280,314,-1,330,317,306,-1,328,316,317,-1,317,330,328,-1,333,355,316,-1,316,328,333,-1,332,355,333,-1,330,312,284,-1,312,311,158,-1,158,284,312,-1]
IndexedFaceSet418.creaseAngle = 3.14159
IndexedFaceSet418.texCoordIndex = [0,3,2,-1,2,1,0,-1,1,6,5,-1,5,4,1,-1,7,8,2,-1,2,3,7,-1,9,10,5,-1,5,6,9,-1,11,12,0,-1,0,1,11,-1,13,11,1,-1,1,4,13,-1,14,17,16,-1,16,15,14,-1,18,19,14,-1,14,15,18,-1,22,21,20,-1,23,16,17,-1,16,25,24,-1,27,26,24,-1,29,28,25,-1,16,23,25,-1,29,25,23,-1,31,17,30,-1,29,23,32,-1,33,32,31,-1,33,31,30,-1,27,35,34,-1,34,26,27,-1,37,36,34,-1,39,38,36,-1,26,40,16,-1,16,24,26,-1,36,42,41,-1,41,39,36,-1,43,41,42,-1,43,44,41,-1,41,44,39,-1,20,45,22,-1,45,46,22,-1,44,47,39,-1,20,49,50,-1,48,51,50,-1,51,20,50,-1,20,47,49,-1,49,47,44,-1,28,24,25,-1,53,52,46,-1,52,55,54,-1,52,54,46,-1,52,53,55,-1,7,57,53,-1,53,56,7,-1,58,57,7,-1,7,59,58,-1,57,58,53,-1,8,7,56,-1,56,60,8,-1,9,6,60,-1,10,9,60,-1,60,61,10,-1,0,12,62,-1,62,12,63,-1,64,62,63,-1,53,58,62,-1,62,64,53,-1,62,58,59,-1,59,0,62,-1,64,63,65,-1,63,67,66,-1,66,65,63,-1,53,64,65,-1,65,55,53,-1,65,66,54,-1,54,55,65,-1,67,21,66,-1,38,39,68,-1,22,46,21,-1,54,66,21,-1,46,54,21,-1,21,67,69,-1,68,69,38,-1,20,21,47,-1,47,21,68,-1,47,68,39,-1,69,18,70,-1,70,18,15,-1,40,70,15,-1,15,16,40,-1,69,71,38,-1,71,69,70,-1,38,71,34,-1,34,36,38,-1,26,34,71,-1,68,21,69,-1,2,6,1,-1,8,60,2,-1,60,6,2,-1,74,73,72,-1,77,76,75,-1,74,78,73,-1,74,81,80,-1,80,79,74,-1,82,79,80,-1,74,79,78,-1,82,84,83,-1,83,84,85,-1,82,86,84,-1,87,90,89,-1,89,88,87,-1,92,91,88,-1,80,81,93,-1,88,91,94,-1,86,93,95,-1,72,73,96,-1,83,79,82,-1,73,83,97,-1,100,99,98,-1,103,102,101,-1,99,83,85,-1,104,97,99,-1,97,83,99,-1,105,90,102,-1,105,89,90,-1,107,106,75,-1,107,108,106,-1,109,82,80,-1,109,80,93,-1,112,111,110,-1,93,81,113,-1,93,113,95,-1,114,110,111,-1,115,114,111,-1,87,86,116,-1,86,95,116,-1,18,69,117,-1,118,19,18,-1,18,117,118,-1,117,69,67,-1,67,119,117,-1,119,67,63,-1,63,120,119,-1,117,119,121,-1,121,118,117,-1,120,122,121,-1,121,119,120,-1,11,120,63,-1,63,12,11,-1,13,122,120,-1,120,11,13,-1,125,124,123,-1,127,126,124,-1,126,127,128,-1,131,130,129,-1,131,129,132,-1,131,132,133,-1,133,127,131,-1,127,133,128,-1,135,134,126,-1,130,135,126,-1,135,136,134,-1,124,126,123,-1,123,126,137,-1,138,125,123,-1,123,139,138,-1,140,143,142,-1,142,141,140,-1,126,134,137,-1,127,124,144,-1,144,124,125,-1,144,131,127,-1,145,125,138,-1,146,140,141,-1,147,140,146,-1,148,144,125,-1,137,149,123,-1,150,123,149,-1,153,156,155,-1,155,154,153,-1,153,154,158,-1,158,157,153,-1,158,160,159,-1,159,157,158,-1,157,159,162,-1,162,161,157,-1,139,215,164,-1,164,138,139,-1,163,139,150,-1,150,165,163,-1,139,123,150,-1,168,167,166,-1,166,167,159,-1,169,151,152,-1,166,159,169,-1,161,172,170,-1,170,157,161,-1,170,171,157,-1,167,162,159,-1,173,176,236,-1,236,174,173,-1,172,161,177,-1,177,233,172,-1,241,174,236,-1,236,240,241,-1,168,180,167,-1,181,180,168,-1,183,238,237,-1,237,231,183,-1,167,180,186,-1,187,177,161,-1,161,162,187,-1,188,189,177,-1,177,187,188,-1,167,186,187,-1,187,162,167,-1,188,187,186,-1,186,190,188,-1,189,192,177,-1,234,176,233,-1,231,175,191,-1,190,186,180,-1,180,193,190,-1,191,234,192,-1,146,141,195,-1,193,180,181,-1,181,194,193,-1,195,141,196,-1,196,240,236,-1,171,156,153,-1,153,157,171,-1,197,181,168,-1,198,147,242,-1,198,140,147,-1,199,125,145,-1,148,125,200,-1,200,125,199,-1,159,160,151,-1,151,169,159,-1,130,136,135,-1,242,147,184,-1,147,201,184,-1,147,146,201,-1,195,201,146,-1,144,202,131,-1,144,148,202,-1,155,204,203,-1,203,154,155,-1,154,203,160,-1,160,158,154,-1,205,208,207,-1,207,206,205,-1,209,208,205,-1,205,210,209,-1,213,214,211,-1,211,212,213,-1,191,191,192,-1,192,192,191,-1,191,191,191,-1,191,191,191,-1,191,191,191,-1,191,191,191,-1,192,192,191,-1,191,191,192,-1,189,189,192,-1,192,192,189,-1,188,188,189,-1,189,189,188,-1,190,190,188,-1,188,188,190,-1,193,193,190,-1,190,190,193,-1,194,194,193,-1,193,193,194,-1,194,232,232,-1,232,194,194,-1,139,163,215,-1,222,223,217,-1,217,216,222,-1,223,229,218,-1,218,217,223,-1,228,219,218,-1,218,229,228,-1,218,219,221,-1,217,218,221,-1,217,221,220,-1,224,225,226,-1,226,225,227,-1,227,230,226,-1,238,183,232,-1,232,239,238,-1,175,231,237,-1,239,232,194,-1,194,178,239,-1,175,176,191,-1,191,176,234,-1,192,234,233,-1,233,177,192,-1,176,173,172,-1,172,233,176,-1,178,194,181,-1,184,235,242,-1,196,236,179,-1,195,196,179,-1,179,182,195,-1,201,195,182,-1,182,185,201,-1,184,201,185,-1,196,141,240,-1,240,141,142,-1,142,241,240,-1,245,244,243,-1,243,246,245,-1,244,248,247,-1,247,249,244,-1,250,246,243,-1,243,251,250,-1,252,249,247,-1,247,253,252,-1,254,244,245,-1,245,255,254,-1,256,248,244,-1,244,254,256,-1,259,258,257,-1,257,260,259,-1,261,258,259,-1,259,262,261,-1,263,265,264,-1,266,260,257,-1,257,268,267,-1,269,268,270,-1,271,267,272,-1,257,267,266,-1,271,266,267,-1,273,274,260,-1,271,275,266,-1,276,273,275,-1,276,274,273,-1,269,270,277,-1,277,278,269,-1,279,277,280,-1,281,280,282,-1,270,268,257,-1,257,283,270,-1,280,281,284,-1,284,285,280,-1,286,285,284,-1,286,284,287,-1,284,281,287,-1,265,263,288,-1,288,263,289,-1,287,281,290,-1,265,292,291,-1,293,292,294,-1,294,292,265,-1,265,291,290,-1,291,287,290,-1,272,267,268,-1,295,289,296,-1,296,298,297,-1,296,289,298,-1,296,297,295,-1,250,299,295,-1,295,300,250,-1,302,301,250,-1,250,300,302,-1,300,295,302,-1,251,303,299,-1,299,250,251,-1,252,303,249,-1,253,304,303,-1,303,252,253,-1,245,305,255,-1,305,306,255,-1,307,306,305,-1,295,307,305,-1,305,302,295,-1,305,245,301,-1,301,302,305,-1,307,308,306,-1,306,308,309,-1,309,310,306,-1,295,297,308,-1,308,307,295,-1,308,297,298,-1,298,309,308,-1,310,309,264,-1,282,311,281,-1,263,264,289,-1,298,264,309,-1,289,264,298,-1,264,312,310,-1,311,282,312,-1,265,290,264,-1,290,311,264,-1,290,281,311,-1,312,313,261,-1,313,258,261,-1,283,257,258,-1,258,313,283,-1,312,282,314,-1,314,313,312,-1,282,280,277,-1,277,314,282,-1,270,314,277,-1,311,312,264,-1,243,244,249,-1,251,243,303,-1,303,243,249,-1,315,317,316,-1,318,320,319,-1,315,316,321,-1,315,323,322,-1,322,324,315,-1,325,322,323,-1,315,321,323,-1,325,327,326,-1,327,328,326,-1,325,326,329,-1,332,331,330,-1,330,333,332,-1,334,331,335,-1,322,336,324,-1,331,337,335,-1,329,338,336,-1,317,339,316,-1,327,325,323,-1,316,340,327,-1,341,343,342,-1,344,346,345,-1,342,328,327,-1,347,342,340,-1,340,342,327,-1,348,345,333,-1,348,333,330,-1,349,320,350,-1,349,350,351,-1,352,322,325,-1,352,336,322,-1,353,355,354,-1,336,356,324,-1,336,338,356,-1,357,354,355,-1,358,354,357,-1,332,359,329,-1,329,359,338,-1,261,360,312,-1,361,360,261,-1,261,262,361,-1,360,362,310,-1,310,312,360,-1,362,363,306,-1,306,310,362,-1,360,361,364,-1,364,362,360,-1,363,362,364,-1,364,365,363,-1,254,255,306,-1,306,363,254,-1,256,254,363,-1,363,365,256,-1,366,368,367,-1,369,367,370,-1,370,371,369,-1,372,374,373,-1,372,375,374,-1,372,369,376,-1,376,375,372,-1,369,371,376,-1,377,370,378,-1,373,370,377,-1,377,378,379,-1,367,368,370,-1,368,380,370,-1,382,381,368,-1,368,366,382,-1,385,384,383,-1,383,386,385,-1,370,380,378,-1,369,387,367,-1,387,366,367,-1,387,369,372,-1,388,382,366,-1,389,384,385,-1,390,389,385,-1,391,366,387,-1,380,368,392,-1,393,392,368,-1,396,395,394,-1,394,397,396,-1,396,399,398,-1,398,395,396,-1,398,399,400,-1,400,401,398,-1,399,403,402,-1,402,400,399,-1,381,382,405,-1,405,404,381,-1,406,407,393,-1,393,381,406,-1,381,393,368,-1,408,410,409,-1,410,400,409,-1,411,413,412,-1,410,411,400,-1,403,399,414,-1,414,415,403,-1,414,399,416,-1,409,400,402,-1,419,418,417,-1,417,420,419,-1,415,422,421,-1,421,403,415,-1,423,424,417,-1,417,418,423,-1,408,409,425,-1,426,408,425,-1,427,430,429,-1,429,428,427,-1,409,431,425,-1,432,402,403,-1,403,421,432,-1,433,432,421,-1,421,434,433,-1,409,402,432,-1,432,431,409,-1,433,435,431,-1,431,432,433,-1,434,421,436,-1,437,422,420,-1,430,439,438,-1,435,440,425,-1,425,431,435,-1,439,436,437,-1,389,441,384,-1,440,442,426,-1,426,425,440,-1,441,443,384,-1,443,417,424,-1,416,396,397,-1,396,416,399,-1,444,408,426,-1,445,446,390,-1,445,390,385,-1,447,388,366,-1,391,448,366,-1,448,447,366,-1,400,411,412,-1,412,401,400,-1,373,377,379,-1,446,449,390,-1,390,449,450,-1,390,450,389,-1,441,389,450,-1,387,372,451,-1,387,451,391,-1,394,395,452,-1,452,453,394,-1,395,398,401,-1,401,452,395,-1,456,455,454,-1,454,457,456,-1,459,458,456,-1,456,457,459,-1,462,461,460,-1,460,463,462,-1,439,436,436,-1,436,439,439,-1,439,439,439,-1,439,439,439,-1,439,439,439,-1,439,439,439,-1,436,439,439,-1,439,436,436,-1,434,436,436,-1,436,434,434,-1,433,434,434,-1,434,433,433,-1,435,433,433,-1,433,435,435,-1,440,435,435,-1,435,440,440,-1,442,440,440,-1,440,442,442,-1,442,442,464,-1,464,464,442,-1,381,404,406,-1,465,468,467,-1,467,466,465,-1,466,467,470,-1,470,469,466,-1,471,469,470,-1,470,472,471,-1,467,474,473,-1,473,472,470,-1,467,473,470,-1,475,477,476,-1,477,479,478,-1,478,476,477,-1,428,480,464,-1,464,427,428,-1,438,429,430,-1,480,481,442,-1,442,464,480,-1,438,439,420,-1,439,437,420,-1,436,421,422,-1,422,437,436,-1,420,422,415,-1,415,419,420,-1,481,426,442,-1,449,446,482,-1,443,483,417,-1,441,484,483,-1,483,443,441,-1,450,485,484,-1,484,441,450,-1,449,485,450,-1,443,424,384,-1,424,423,383,-1,383,384,424,-1]
Coordinate419 = x3d.Coordinate()

IndexedFaceSet418.coord = Coordinate419
TextureCoordinate420 = x3d.TextureCoordinate()

IndexedFaceSet418.texCoord = TextureCoordinate420

Shape414.geometry = IndexedFaceSet418

Transform413.children.append(Shape414)

HAnimSegment412.children.append(Transform413)

HAnimJoint411.children.append(HAnimSegment412)
HAnimJoint421 = x3d.HAnimJoint()
HAnimJoint421.name = "l_eyelid_joint"
HAnimJoint421.DEF = "hanim_l_eyelid_joint"
HAnimJoint421.center = [2.245,62.400002,1.464]
HAnimJoint421.ulimit = [0,0,0]
HAnimJoint421.llimit = [0,0,0]
HAnimSegment422 = x3d.HAnimSegment()
HAnimSegment422.name = "l_eyelid"
HAnimSegment422.DEF = "hanim_l_eyelid"
Transform423 = x3d.Transform()
Transform423.rotation = [1,0,0,-0.5236]
Transform423.translation = [2.245,62.400002,1.464]
Shape424 = x3d.Shape()
Appearance425 = x3d.Appearance()
Material426 = x3d.Material()
Material426.diffuseColor = [0.588,0.588,0.588]

Appearance425.material = Material426
ImageTexture427 = x3d.ImageTexture()
ImageTexture427.USE = "JinLOA3TextureAtlas"

Appearance425.texture = ImageTexture427

Shape424.appearance = Appearance425
IndexedFaceSet428 = x3d.IndexedFaceSet()
IndexedFaceSet428.coordIndex = [0,1,25,-1,25,24,0,-1,2,26,25,-1,25,1,2,-1,2,3,8,-1,8,26,2,-1,10,27,9,-1,9,4,10,-1,10,0,24,-1,24,27,10,-1,1,0,12,-1,12,13,1,-1,2,1,13,-1,13,14,2,-1,3,2,14,-1,14,15,3,-1,10,4,16,-1,16,22,10,-1,5,6,18,-1,18,17,5,-1,6,7,19,-1,19,18,6,-1,7,8,20,-1,20,19,7,-1,9,11,23,-1,23,21,9,-1,8,3,15,-1,15,20,8,-1,4,9,21,-1,21,16,4,-1,0,10,22,-1,22,12,0,-1,11,5,17,-1,17,23,11,-1,6,5,24,-1,24,25,6,-1,7,6,25,-1,25,26,7,-1,5,11,27,-1,27,24,5,-1,27,11,9,-1,8,7,26,-1]
IndexedFaceSet428.creaseAngle = 3.14159
IndexedFaceSet428.texCoordIndex = [0,1,2,-1,2,3,0,-1,4,5,2,-1,2,1,4,-1,4,6,7,-1,7,5,4,-1,9,10,11,-1,11,8,9,-1,9,0,3,-1,3,10,9,-1,1,0,12,-1,12,13,1,-1,4,1,13,-1,13,14,4,-1,6,4,14,-1,14,15,6,-1,9,8,16,-1,16,17,9,-1,18,19,20,-1,20,21,18,-1,19,22,23,-1,23,20,19,-1,22,7,24,-1,24,23,22,-1,11,25,26,-1,26,27,11,-1,7,6,15,-1,15,24,7,-1,8,11,27,-1,27,16,8,-1,0,9,17,-1,17,12,0,-1,25,18,21,-1,21,26,25,-1,19,18,3,-1,3,2,19,-1,22,19,2,-1,2,5,22,-1,18,25,10,-1,10,3,18,-1,10,25,11,-1,7,22,5,-1]
Coordinate429 = x3d.Coordinate()

IndexedFaceSet428.coord = Coordinate429
TextureCoordinate430 = x3d.TextureCoordinate()

IndexedFaceSet428.texCoord = TextureCoordinate430

Shape424.geometry = IndexedFaceSet428

Transform423.children.append(Shape424)

HAnimSegment422.children.append(Transform423)

HAnimJoint421.children.append(HAnimSegment422)

HAnimJoint411.children.append(HAnimJoint421)
HAnimJoint431 = x3d.HAnimJoint()
HAnimJoint431.name = "r_eyelid_joint"
HAnimJoint431.DEF = "hanim_r_eyelid_joint"
HAnimJoint431.center = [-2.245,62.400002,1.464]
HAnimJoint431.ulimit = [0,0,0]
HAnimJoint431.llimit = [0,0,0]
HAnimSegment432 = x3d.HAnimSegment()
HAnimSegment432.name = "r_eyelid"
HAnimSegment432.DEF = "hanim_r_eyelid"
Transform433 = x3d.Transform()
Transform433.rotation = [1,0,0,-0.5236]
Transform433.translation = [-2.245,62.400002,1.464]
Shape434 = x3d.Shape()
Appearance435 = x3d.Appearance()
Material436 = x3d.Material()
Material436.diffuseColor = [0.588,0.588,0.588]

Appearance435.material = Material436
ImageTexture437 = x3d.ImageTexture()
ImageTexture437.USE = "JinLOA3TextureAtlas"

Appearance435.texture = ImageTexture437

Shape434.appearance = Appearance435
IndexedFaceSet438 = x3d.IndexedFaceSet()
IndexedFaceSet438.coordIndex = [0,24,25,-1,25,1,0,-1,2,1,25,-1,25,26,2,-1,2,26,8,-1,8,3,2,-1,10,4,9,-1,9,27,10,-1,10,27,24,-1,24,0,10,-1,1,13,12,-1,12,0,1,-1,2,14,13,-1,13,1,2,-1,3,15,14,-1,14,2,3,-1,10,22,16,-1,16,4,10,-1,5,17,18,-1,18,6,5,-1,6,18,19,-1,19,7,6,-1,7,19,20,-1,20,8,7,-1,9,21,23,-1,23,11,9,-1,8,20,15,-1,15,3,8,-1,4,16,21,-1,21,9,4,-1,0,12,22,-1,22,10,0,-1,11,23,17,-1,17,5,11,-1,6,25,24,-1,24,5,6,-1,7,26,25,-1,25,6,7,-1,5,24,27,-1,27,11,5,-1,27,9,11,-1,8,26,7,-1]
IndexedFaceSet438.creaseAngle = 3.14159
IndexedFaceSet438.texCoordIndex = [0,3,2,-1,2,1,0,-1,4,1,2,-1,2,5,4,-1,4,5,7,-1,7,6,4,-1,9,8,11,-1,11,10,9,-1,9,10,3,-1,3,0,9,-1,1,13,12,-1,12,0,1,-1,4,14,13,-1,13,1,4,-1,6,15,14,-1,14,4,6,-1,9,17,16,-1,16,8,9,-1,18,21,20,-1,20,19,18,-1,19,20,23,-1,23,22,19,-1,22,23,24,-1,24,7,22,-1,11,27,26,-1,26,25,11,-1,7,24,15,-1,15,6,7,-1,8,16,27,-1,27,11,8,-1,0,12,17,-1,17,9,0,-1,25,26,21,-1,21,18,25,-1,19,2,3,-1,3,18,19,-1,22,5,2,-1,2,19,22,-1,18,3,10,-1,10,25,18,-1,10,11,25,-1,7,5,22,-1]
Coordinate439 = x3d.Coordinate()

IndexedFaceSet438.coord = Coordinate439
TextureCoordinate440 = x3d.TextureCoordinate()

IndexedFaceSet438.texCoord = TextureCoordinate440

Shape434.geometry = IndexedFaceSet438

Transform433.children.append(Shape434)

HAnimSegment432.children.append(Transform433)

HAnimJoint431.children.append(HAnimSegment432)

HAnimJoint411.children.append(HAnimJoint431)
HAnimJoint441 = x3d.HAnimJoint()
HAnimJoint441.name = "l_eyeball_joint"
HAnimJoint441.DEF = "hanim_l_eyeball_joint"
HAnimJoint441.center = [2.139,61.529999,3.691]
HAnimJoint441.ulimit = [0,0,0]
HAnimJoint441.llimit = [0,0,0]
HAnimSegment442 = x3d.HAnimSegment()
HAnimSegment442.name = "l_eyeball"
HAnimSegment442.DEF = "hanim_l_eyeball"
Transform443 = x3d.Transform()
Transform443.translation = [2.139,61.529999,3.691]
Shape444 = x3d.Shape()
Appearance445 = x3d.Appearance()
Material446 = x3d.Material()
Material446.diffuseColor = [0.588,0.588,0.588]

Appearance445.material = Material446
ImageTexture447 = x3d.ImageTexture()
ImageTexture447.USE = "JinLOA3TextureAtlas"

Appearance445.texture = ImageTexture447

Shape444.appearance = Appearance445
IndexedFaceSet448 = x3d.IndexedFaceSet()
IndexedFaceSet448.coordIndex = [1,6,16,-1,16,11,1,-1,0,1,11,-1,11,10,0,-1,8,9,19,-1,19,18,8,-1,2,8,18,-1,18,12,2,-1,3,0,10,-1,10,13,3,-1,9,4,14,-1,14,19,9,-1,5,2,12,-1,12,15,5,-1,4,3,13,-1,13,14,4,-1,6,7,17,-1,17,16,6,-1,7,5,15,-1,15,17,7,-1,11,16,21,-1,21,20,11,-1,16,17,22,-1,22,21,16,-1,17,15,23,-1,23,22,17,-1,15,12,24,-1,24,23,15,-1,12,18,25,-1,25,24,12,-1,18,19,26,-1,26,25,18,-1,19,14,27,-1,27,26,19,-1,14,13,28,-1,28,27,14,-1,13,10,29,-1,29,28,13,-1,10,11,20,-1,20,29,10,-1,6,1,30,-1,1,0,30,-1,0,3,30,-1,3,4,30,-1,4,9,30,-1,9,8,30,-1,8,2,30,-1,2,5,30,-1,5,7,30,-1,7,6,30,-1]
IndexedFaceSet448.creaseAngle = 3.14159
IndexedFaceSet448.texCoordIndex = [4,9,13,-1,13,14,4,-1,3,4,14,-1,14,15,3,-1,11,12,16,-1,16,17,11,-1,5,11,17,-1,17,18,5,-1,6,3,15,-1,15,6,6,-1,12,7,19,-1,19,16,12,-1,8,5,18,-1,18,20,8,-1,7,6,21,-1,21,19,7,-1,9,10,22,-1,22,13,9,-1,10,8,20,-1,20,22,10,-1,14,13,24,-1,24,23,14,-1,13,22,25,-1,25,24,13,-1,22,20,26,-1,26,25,22,-1,20,18,27,-1,27,26,20,-1,18,17,28,-1,28,27,18,-1,17,16,29,-1,29,28,17,-1,16,19,30,-1,30,29,16,-1,19,21,31,-1,31,30,19,-1,6,15,32,-1,32,31,6,-1,15,14,23,-1,23,32,15,-1,36,1,40,-1,1,0,40,-1,0,33,40,-1,33,34,40,-1,34,39,40,-1,39,38,40,-1,38,2,40,-1,2,35,40,-1,35,37,40,-1,37,36,40,-1]
Coordinate449 = x3d.Coordinate()

IndexedFaceSet448.coord = Coordinate449
TextureCoordinate450 = x3d.TextureCoordinate()

IndexedFaceSet448.texCoord = TextureCoordinate450

Shape444.geometry = IndexedFaceSet448

Transform443.children.append(Shape444)

HAnimSegment442.children.append(Transform443)

HAnimJoint441.children.append(HAnimSegment442)

HAnimJoint411.children.append(HAnimJoint441)
HAnimJoint451 = x3d.HAnimJoint()
HAnimJoint451.name = "r_eyeball_joint"
HAnimJoint451.DEF = "hanim_r_eyeball_joint"
HAnimJoint451.center = [-2.139,61.529999,3.691]
HAnimJoint451.ulimit = [0,0,0]
HAnimJoint451.llimit = [0,0,0]
HAnimSegment452 = x3d.HAnimSegment()
HAnimSegment452.name = "r_eyeball"
HAnimSegment452.DEF = "hanim_r_eyeball"
Transform453 = x3d.Transform()
Transform453.translation = [-2.139,61.529999,3.691]
Shape454 = x3d.Shape()
Appearance455 = x3d.Appearance()
Material456 = x3d.Material()
Material456.diffuseColor = [0.588,0.588,0.588]

Appearance455.material = Material456
ImageTexture457 = x3d.ImageTexture()
ImageTexture457.USE = "JinLOA3TextureAtlas"

Appearance455.texture = ImageTexture457

Shape454.appearance = Appearance455
IndexedFaceSet458 = x3d.IndexedFaceSet()
IndexedFaceSet458.coordIndex = [1,11,16,-1,16,6,1,-1,0,10,11,-1,11,1,0,-1,8,18,19,-1,19,9,8,-1,2,12,18,-1,18,8,2,-1,3,13,10,-1,10,0,3,-1,9,19,14,-1,14,4,9,-1,5,15,12,-1,12,2,5,-1,4,14,13,-1,13,3,4,-1,6,16,17,-1,17,7,6,-1,7,17,15,-1,15,5,7,-1,11,20,21,-1,21,16,11,-1,16,21,22,-1,22,17,16,-1,17,22,23,-1,23,15,17,-1,15,23,24,-1,24,12,15,-1,12,24,25,-1,25,18,12,-1,18,25,26,-1,26,19,18,-1,19,26,27,-1,27,14,19,-1,14,27,28,-1,28,13,14,-1,13,28,29,-1,29,10,13,-1,10,29,20,-1,20,11,10,-1,6,30,1,-1,1,30,0,-1,0,30,3,-1,3,30,4,-1,4,30,9,-1,9,30,8,-1,8,30,2,-1,2,30,5,-1,5,30,7,-1,7,30,6,-1]
IndexedFaceSet458.creaseAngle = 3.14159
IndexedFaceSet458.texCoordIndex = [4,14,13,-1,13,9,4,-1,3,15,14,-1,14,4,3,-1,11,17,16,-1,16,12,11,-1,5,18,17,-1,17,11,5,-1,6,6,15,-1,15,3,6,-1,12,16,19,-1,19,7,12,-1,8,20,18,-1,18,5,8,-1,7,19,21,-1,21,6,7,-1,9,13,22,-1,22,10,9,-1,10,22,20,-1,20,8,10,-1,14,23,24,-1,24,13,14,-1,13,24,25,-1,25,22,13,-1,22,25,26,-1,26,20,22,-1,20,26,27,-1,27,18,20,-1,18,27,28,-1,28,17,18,-1,17,28,29,-1,29,16,17,-1,16,29,30,-1,30,19,16,-1,19,30,31,-1,31,21,19,-1,6,31,32,-1,32,15,6,-1,15,32,23,-1,23,14,15,-1,36,40,1,-1,1,40,0,-1,0,40,33,-1,33,40,34,-1,34,40,39,-1,39,40,38,-1,38,40,2,-1,2,40,35,-1,35,40,37,-1,37,40,36,-1]
Coordinate459 = x3d.Coordinate()

IndexedFaceSet458.coord = Coordinate459
TextureCoordinate460 = x3d.TextureCoordinate()

IndexedFaceSet458.texCoord = TextureCoordinate460

Shape454.geometry = IndexedFaceSet458

Transform453.children.append(Shape454)

HAnimSegment452.children.append(Transform453)

HAnimJoint451.children.append(HAnimSegment452)

HAnimJoint411.children.append(HAnimJoint451)
HAnimJoint461 = x3d.HAnimJoint()
HAnimJoint461.name = "l_eyebrow_joint"
HAnimJoint461.DEF = "hanim_l_eyebrow_joint"
HAnimJoint461.center = [0.9666,61.93,4.753]
HAnimJoint461.ulimit = [0,0,0]
HAnimJoint461.llimit = [0,0,0]
HAnimSegment462 = x3d.HAnimSegment()
HAnimSegment462.name = "l_eyebrow"
HAnimSegment462.DEF = "hanim_l_eyebrow"
Transform463 = x3d.Transform()
Transform463.translation = [0.9666,61.93,4.753]
Shape464 = x3d.Shape()
Appearance465 = x3d.Appearance()
Material466 = x3d.Material()
Material466.diffuseColor = [0.588,0.588,0.588]

Appearance465.material = Material466
ImageTexture467 = x3d.ImageTexture()
ImageTexture467.USE = "JinLOA3TextureAtlas"

Appearance465.texture = ImageTexture467

Shape464.appearance = Appearance465
IndexedFaceSet468 = x3d.IndexedFaceSet()
IndexedFaceSet468.coordIndex = [2,20,21,-1,21,7,2,-1,4,3,8,-1,8,10,4,-1,3,2,7,-1,7,8,3,-1,2,1,5,-1,5,20,2,-1,4,6,3,-1,3,6,1,-1,1,2,3,-1,5,1,12,-1,12,14,5,-1,0,5,14,-1,14,11,0,-1,6,4,13,-1,13,15,6,-1,1,6,15,-1,15,12,1,-1,8,7,16,-1,16,17,8,-1,21,22,16,-1,16,7,21,-1,9,0,11,-1,11,18,9,-1,4,10,19,-1,19,13,4,-1,10,8,17,-1,17,19,10,-1,20,0,9,-1,9,21,20,-1,5,0,20,-1,21,9,18,-1,18,22,21,-1]
IndexedFaceSet468.creaseAngle = 3.14159
IndexedFaceSet468.texCoordIndex = [0,20,21,-1,21,7,0,-1,3,1,8,-1,8,10,3,-1,1,0,7,-1,7,8,1,-1,0,4,5,-1,5,20,0,-1,3,6,1,-1,1,6,4,-1,4,0,1,-1,5,4,11,-1,11,12,5,-1,2,5,12,-1,12,14,2,-1,6,3,15,-1,15,16,6,-1,4,6,16,-1,16,11,4,-1,8,7,13,-1,13,17,8,-1,21,22,13,-1,13,7,21,-1,9,2,14,-1,14,18,9,-1,3,10,19,-1,19,15,3,-1,10,8,17,-1,17,19,10,-1,20,2,9,-1,9,21,20,-1,5,2,20,-1,21,9,18,-1,18,22,21,-1]
Coordinate469 = x3d.Coordinate()

IndexedFaceSet468.coord = Coordinate469
TextureCoordinate470 = x3d.TextureCoordinate()

IndexedFaceSet468.texCoord = TextureCoordinate470

Shape464.geometry = IndexedFaceSet468

Transform463.children.append(Shape464)

HAnimSegment462.children.append(Transform463)

HAnimJoint461.children.append(HAnimSegment462)

HAnimJoint411.children.append(HAnimJoint461)
HAnimJoint471 = x3d.HAnimJoint()
HAnimJoint471.name = "r_eyebrow_joint"
HAnimJoint471.DEF = "hanim_r_eyebrow_joint"
HAnimJoint471.center = [-0.9666,61.93,4.753]
HAnimJoint471.ulimit = [0,0,0]
HAnimJoint471.llimit = [0,0,0]
HAnimSegment472 = x3d.HAnimSegment()
HAnimSegment472.name = "r_eyebrow"
HAnimSegment472.DEF = "hanim_r_eyebrow"
Transform473 = x3d.Transform()
Transform473.translation = [-0.9666,61.93,4.753]
Shape474 = x3d.Shape()
Appearance475 = x3d.Appearance()
Material476 = x3d.Material()
Material476.diffuseColor = [0.588,0.588,0.588]

Appearance475.material = Material476
ImageTexture477 = x3d.ImageTexture()
ImageTexture477.USE = "JinLOA3TextureAtlas"

Appearance475.texture = ImageTexture477

Shape474.appearance = Appearance475
IndexedFaceSet478 = x3d.IndexedFaceSet()
IndexedFaceSet478.coordIndex = [2,7,21,-1,21,20,2,-1,4,10,8,-1,8,3,4,-1,3,8,7,-1,7,2,3,-1,2,20,5,-1,5,1,2,-1,4,3,6,-1,3,2,1,-1,1,6,3,-1,5,14,12,-1,12,1,5,-1,0,11,14,-1,14,5,0,-1,6,15,13,-1,13,4,6,-1,1,12,15,-1,15,6,1,-1,8,17,16,-1,16,7,8,-1,21,7,16,-1,16,22,21,-1,9,18,11,-1,11,0,9,-1,4,13,19,-1,19,10,4,-1,10,19,17,-1,17,8,10,-1,20,21,9,-1,9,0,20,-1,5,20,0,-1,21,22,18,-1,18,9,21,-1]
IndexedFaceSet478.creaseAngle = 3.14159
IndexedFaceSet478.texCoordIndex = [0,7,21,-1,21,20,0,-1,3,10,8,-1,8,1,3,-1,1,8,7,-1,7,0,1,-1,0,20,5,-1,5,4,0,-1,3,1,6,-1,1,0,4,-1,4,6,1,-1,5,12,11,-1,11,4,5,-1,2,14,12,-1,12,5,2,-1,6,16,15,-1,15,3,6,-1,4,11,16,-1,16,6,4,-1,8,17,13,-1,13,7,8,-1,21,7,13,-1,13,22,21,-1,9,18,14,-1,14,2,9,-1,3,15,19,-1,19,10,3,-1,10,19,17,-1,17,8,10,-1,20,21,9,-1,9,2,20,-1,5,20,2,-1,21,22,18,-1,18,9,21,-1]
Coordinate479 = x3d.Coordinate()

IndexedFaceSet478.coord = Coordinate479
TextureCoordinate480 = x3d.TextureCoordinate()

IndexedFaceSet478.texCoord = TextureCoordinate480

Shape474.geometry = IndexedFaceSet478

Transform473.children.append(Shape474)

HAnimSegment472.children.append(Transform473)

HAnimJoint471.children.append(HAnimSegment472)

HAnimJoint411.children.append(HAnimJoint471)
HAnimJoint481 = x3d.HAnimJoint()
HAnimJoint481.name = "temporomandibular"
HAnimJoint481.DEF = "hanim_temporomandibular"
HAnimJoint481.center = [0,57.450001,0.6835]
HAnimJoint481.ulimit = [0,0,0]
HAnimJoint481.llimit = [0,0,0]
HAnimSegment482 = x3d.HAnimSegment()
HAnimSegment482.name = "jaw"
HAnimSegment482.DEF = "hanim_jaw"
Transform483 = x3d.Transform()
Transform483.translation = [0,57.450001,0.6835]
Shape484 = x3d.Shape()
Appearance485 = x3d.Appearance()
Material486 = x3d.Material()
Material486.diffuseColor = [0.588,0.588,0.588]

Appearance485.material = Material486
ImageTexture487 = x3d.ImageTexture()
ImageTexture487.USE = "JinLOA3TextureAtlas"

Appearance485.texture = ImageTexture487

Shape484.appearance = Appearance485
IndexedFaceSet488 = x3d.IndexedFaceSet()
IndexedFaceSet488.coordIndex = [0,2,12,-1,13,3,15,-1,3,13,4,-1,4,13,12,-1,4,12,2,-1,1,0,18,-1,18,9,1,-1,4,2,10,-1,10,6,8,-1,4,10,8,-1,3,7,24,-1,24,15,3,-1,4,8,7,-1,7,3,4,-1,5,26,24,-1,24,7,5,-1,8,6,5,-1,5,7,8,-1,0,1,2,-1,2,1,9,-1,9,10,2,-1,0,12,11,-1,13,15,14,-1,14,16,13,-1,16,12,13,-1,16,11,12,-1,17,19,18,-1,18,0,17,-1,22,21,20,-1,16,22,20,-1,16,20,11,-1,14,15,24,-1,24,23,14,-1,16,14,23,-1,23,22,16,-1,25,23,24,-1,24,26,25,-1,22,23,25,-1,25,21,22,-1,0,11,17,-1,11,20,19,-1,19,17,11,-1]
IndexedFaceSet488.creaseAngle = 3.14159
IndexedFaceSet488.texCoordIndex = [0,2,3,-1,4,5,6,-1,5,4,7,-1,7,4,3,-1,7,3,2,-1,1,0,0,-1,0,8,1,-1,7,2,2,-1,2,9,16,-1,7,2,16,-1,5,13,14,-1,14,6,5,-1,7,15,13,-1,13,5,7,-1,11,12,17,-1,17,10,11,-1,18,19,11,-1,11,10,18,-1,0,20,2,-1,2,20,21,-1,21,2,2,-1,0,22,2,-1,23,25,24,-1,24,26,23,-1,26,22,23,-1,26,2,22,-1,27,28,0,-1,0,0,27,-1,30,29,2,-1,26,30,2,-1,26,2,2,-1,24,25,32,-1,32,31,24,-1,26,24,31,-1,31,33,26,-1,35,34,37,-1,37,36,35,-1,38,34,35,-1,35,39,38,-1,0,2,40,-1,2,2,41,-1,41,40,2,-1]
Coordinate489 = x3d.Coordinate()

IndexedFaceSet488.coord = Coordinate489
TextureCoordinate490 = x3d.TextureCoordinate()

IndexedFaceSet488.texCoord = TextureCoordinate490

Shape484.geometry = IndexedFaceSet488

Transform483.children.append(Shape484)

HAnimSegment482.children.append(Transform483)

HAnimJoint481.children.append(HAnimSegment482)

HAnimJoint411.children.append(HAnimJoint481)

HAnimJoint401.children.append(HAnimJoint411)

HAnimJoint391.children.append(HAnimJoint401)

HAnimJoint381.children.append(HAnimJoint391)

HAnimJoint371.children.append(HAnimJoint381)

HAnimJoint361.children.append(HAnimJoint371)

HAnimJoint351.children.append(HAnimJoint361)

HAnimJoint341.children.append(HAnimJoint351)

HAnimJoint331.children.append(HAnimJoint341)
HAnimJoint491 = x3d.HAnimJoint()
HAnimJoint491.name = "l_sternoclavicular"
HAnimJoint491.DEF = "hanim_l_sternoclavicular"
HAnimJoint491.center = [1.71,52.82,-0.6127]
HAnimJoint491.ulimit = [0,0,0]
HAnimJoint491.llimit = [0,0,0]
HAnimSegment492 = x3d.HAnimSegment()
HAnimSegment492.name = "l_clavicle"
HAnimSegment492.DEF = "hanim_l_clavicle"
Transform493 = x3d.Transform()
Transform493.translation = [1.71,52.82,-0.6127]
Shape494 = x3d.Shape()
Appearance495 = x3d.Appearance()
Material496 = x3d.Material()
Material496.diffuseColor = [0.588,0.588,0.588]

Appearance495.material = Material496
ImageTexture497 = x3d.ImageTexture()
ImageTexture497.USE = "JinLOA3TextureAtlas"

Appearance495.texture = ImageTexture497

Shape494.appearance = Appearance495
IndexedFaceSet498 = x3d.IndexedFaceSet()
IndexedFaceSet498.coordIndex = [9,6,1,-1,1,0,9,-1,6,5,2,-1,2,1,6,-1,8,3,2,-1,2,5,8,-1,8,7,4,-1,4,3,8,-1,9,0,4,-1,4,7,9,-1,2,3,4,-1,2,4,0,-1,1,2,0,-1,13,14,10,-1,12,13,10,-1,11,12,10,-1,6,9,11,-1,11,10,6,-1,9,7,12,-1,12,11,9,-1,7,8,13,-1,13,12,7,-1,8,5,14,-1,14,13,8,-1,5,6,10,-1,10,14,5,-1]
IndexedFaceSet498.creaseAngle = 3.14159
IndexedFaceSet498.texCoordIndex = [9,6,1,-1,1,0,9,-1,6,5,2,-1,2,1,6,-1,8,3,2,-1,2,5,8,-1,8,7,4,-1,4,3,8,-1,9,0,4,-1,4,7,9,-1,2,3,4,-1,2,4,0,-1,1,2,0,-1,13,14,10,-1,12,13,10,-1,11,12,10,-1,6,9,11,-1,11,10,6,-1,9,7,12,-1,12,11,9,-1,7,8,13,-1,13,12,7,-1,8,5,14,-1,14,13,8,-1,5,6,10,-1,10,14,5,-1]
Coordinate499 = x3d.Coordinate()

IndexedFaceSet498.coord = Coordinate499
TextureCoordinate500 = x3d.TextureCoordinate()

IndexedFaceSet498.texCoord = TextureCoordinate500

Shape494.geometry = IndexedFaceSet498

Transform493.children.append(Shape494)

HAnimSegment492.children.append(Transform493)

HAnimJoint491.children.append(HAnimSegment492)
HAnimJoint501 = x3d.HAnimJoint()
HAnimJoint501.name = "l_acromioclavicular"
HAnimJoint501.DEF = "hanim_l_acromioclavicular"
HAnimJoint501.center = [5.464,52.060001,-0.5732]
HAnimJoint501.ulimit = [0,0,0]
HAnimJoint501.llimit = [0,0,0]
HAnimSegment502 = x3d.HAnimSegment()
HAnimSegment502.name = "l_scapula"
HAnimSegment502.DEF = "hanim_l_scapula"
Transform503 = x3d.Transform()
Transform503.translation = [5.464,52.060001,-0.5732]
Shape504 = x3d.Shape()
Appearance505 = x3d.Appearance()
Material506 = x3d.Material()
Material506.diffuseColor = [0.588,0.588,0.588]

Appearance505.material = Material506
ImageTexture507 = x3d.ImageTexture()
ImageTexture507.USE = "JinLOA3TextureAtlas"

Appearance505.texture = ImageTexture507

Shape504.appearance = Appearance505
IndexedFaceSet508 = x3d.IndexedFaceSet()
IndexedFaceSet508.coordIndex = [5,4,0,-1,0,1,5,-1,4,3,2,-1,2,0,4,-1,3,9,6,-1,6,2,3,-1,7,5,1,-1,1,8,7,-1,6,8,0,-1,0,2,6,-1,0,8,1,-1,9,7,8,-1,8,6,9,-1,4,5,11,-1,11,10,4,-1,5,7,12,-1,12,11,5,-1,7,9,13,-1,13,12,7,-1,9,3,14,-1,14,13,9,-1,3,4,10,-1,10,14,3,-1,10,11,15,-1,11,12,15,-1,12,13,15,-1,13,14,15,-1,14,10,15,-1]
IndexedFaceSet508.creaseAngle = 3.14159
IndexedFaceSet508.texCoordIndex = [5,4,0,-1,0,1,5,-1,4,3,2,-1,2,0,4,-1,3,8,6,-1,6,2,3,-1,9,5,1,-1,1,7,9,-1,6,7,0,-1,0,2,6,-1,0,7,1,-1,12,13,11,-1,11,10,12,-1,4,5,15,-1,15,14,4,-1,5,9,16,-1,16,15,5,-1,13,12,17,-1,17,16,13,-1,8,3,18,-1,18,17,8,-1,3,4,14,-1,14,18,3,-1,14,15,19,-1,15,16,19,-1,16,17,19,-1,17,18,19,-1,18,14,19,-1]
Coordinate509 = x3d.Coordinate()

IndexedFaceSet508.coord = Coordinate509
TextureCoordinate510 = x3d.TextureCoordinate()

IndexedFaceSet508.texCoord = TextureCoordinate510

Shape504.geometry = IndexedFaceSet508

Transform503.children.append(Shape504)

HAnimSegment502.children.append(Transform503)

HAnimJoint501.children.append(HAnimSegment502)
HAnimJoint511 = x3d.HAnimJoint()
HAnimJoint511.name = "l_shoulder"
HAnimJoint511.DEF = "hanim_l_shoulder"
HAnimJoint511.center = [7.336,51.48,-0.1452]
HAnimJoint511.ulimit = [0,0,0]
HAnimJoint511.llimit = [0,0,0]
HAnimSegment512 = x3d.HAnimSegment()
HAnimSegment512.name = "l_upperarm"
HAnimSegment512.DEF = "hanim_l_upperarm"
Transform513 = x3d.Transform()
Transform513.translation = [7.336,51.48,-0.1452]
Shape514 = x3d.Shape()
Appearance515 = x3d.Appearance()
Material516 = x3d.Material()
Material516.diffuseColor = [0.588,0.588,0.588]

Appearance515.material = Material516
ImageTexture517 = x3d.ImageTexture()
ImageTexture517.USE = "JinLOA3TextureAtlas"

Appearance515.texture = ImageTexture517

Shape514.appearance = Appearance515
IndexedFaceSet518 = x3d.IndexedFaceSet()
IndexedFaceSet518.coordIndex = [2,1,0,-1,3,2,0,-1,4,3,0,-1,0,1,6,-1,6,5,0,-1,1,2,7,-1,7,6,1,-1,2,3,8,-1,8,7,2,-1,3,4,9,-1,9,8,3,-1,4,0,5,-1,5,9,4,-1,5,6,11,-1,11,10,5,-1,6,7,12,-1,12,11,6,-1,7,8,13,-1,13,12,7,-1,8,9,14,-1,14,13,8,-1,9,5,10,-1,10,14,9,-1,10,11,16,-1,16,15,10,-1,11,12,17,-1,17,16,11,-1,12,13,18,-1,18,17,12,-1,13,14,19,-1,19,18,13,-1,14,10,15,-1,15,19,14,-1,36,37,38,-1,35,36,38,-1,39,35,38,-1,21,20,15,-1,15,16,21,-1,22,21,16,-1,16,17,22,-1,23,22,17,-1,17,18,23,-1,24,23,18,-1,18,19,24,-1,20,24,19,-1,19,15,20,-1,26,25,20,-1,20,21,26,-1,27,26,21,-1,21,22,27,-1,28,27,22,-1,22,23,28,-1,29,28,23,-1,23,24,29,-1,25,29,24,-1,24,20,25,-1,31,30,25,-1,25,26,31,-1,32,31,26,-1,26,27,32,-1,33,32,27,-1,27,28,33,-1,34,33,28,-1,28,29,34,-1,30,34,29,-1,29,25,30,-1,36,35,30,-1,30,31,36,-1,37,36,31,-1,31,32,37,-1,38,37,32,-1,32,33,38,-1,39,38,33,-1,33,34,39,-1,35,39,34,-1,34,30,35,-1]
IndexedFaceSet518.creaseAngle = 3.14159
IndexedFaceSet518.texCoordIndex = [2,0,1,-1,3,2,1,-1,61,3,1,-1,1,0,5,-1,5,6,1,-1,0,2,7,-1,7,5,0,-1,2,3,8,-1,8,7,2,-1,25,4,9,-1,9,26,25,-1,4,1,6,-1,6,9,4,-1,6,5,10,-1,10,11,6,-1,5,7,12,-1,12,10,5,-1,7,8,13,-1,13,12,7,-1,27,9,14,-1,14,28,27,-1,9,6,11,-1,11,14,9,-1,11,10,15,-1,15,16,11,-1,10,12,17,-1,17,15,10,-1,12,13,18,-1,18,17,12,-1,29,14,19,-1,19,30,29,-1,14,11,16,-1,16,19,14,-1,54,35,36,-1,53,54,36,-1,37,53,36,-1,20,21,16,-1,16,15,20,-1,22,20,15,-1,15,17,22,-1,23,22,17,-1,17,18,23,-1,24,32,31,-1,31,19,24,-1,21,24,19,-1,19,16,21,-1,40,41,38,-1,38,39,40,-1,43,56,55,-1,55,42,43,-1,45,43,42,-1,42,44,45,-1,47,45,44,-1,44,46,47,-1,41,47,46,-1,46,38,41,-1,48,49,41,-1,41,40,48,-1,50,58,57,-1,57,43,50,-1,51,50,43,-1,43,45,51,-1,52,51,45,-1,45,47,52,-1,49,52,47,-1,47,41,49,-1,34,33,49,-1,49,48,34,-1,35,60,59,-1,59,50,35,-1,36,35,50,-1,50,51,36,-1,37,36,51,-1,51,52,37,-1,33,37,52,-1,52,49,33,-1]
Coordinate519 = x3d.Coordinate()

IndexedFaceSet518.coord = Coordinate519
TextureCoordinate520 = x3d.TextureCoordinate()

IndexedFaceSet518.texCoord = TextureCoordinate520

Shape514.geometry = IndexedFaceSet518

Transform513.children.append(Shape514)

HAnimSegment512.children.append(Transform513)

HAnimJoint511.children.append(HAnimSegment512)
HAnimJoint521 = x3d.HAnimJoint()
HAnimJoint521.name = "l_elbow"
HAnimJoint521.DEF = "hanim_l_elbow"
HAnimJoint521.center = [8.093,40.380001,-0.2502]
HAnimJoint521.ulimit = [0,0,0]
HAnimJoint521.llimit = [0,0,0]
HAnimSegment522 = x3d.HAnimSegment()
HAnimSegment522.name = "l_forearm"
HAnimSegment522.DEF = "hanim_l_forearm"
Transform523 = x3d.Transform()
Transform523.translation = [8.093,40.380001,-0.2502]
Shape524 = x3d.Shape()
Appearance525 = x3d.Appearance()
Material526 = x3d.Material()
Material526.diffuseColor = [0.588,0.588,0.588]

Appearance525.material = Material526
ImageTexture527 = x3d.ImageTexture()
ImageTexture527.USE = "JinLOA3TextureAtlas"

Appearance525.texture = ImageTexture527

Shape524.appearance = Appearance525
IndexedFaceSet528 = x3d.IndexedFaceSet()
IndexedFaceSet528.coordIndex = [2,1,0,-1,3,2,0,-1,4,3,0,-1,0,1,6,-1,6,5,0,-1,1,2,7,-1,7,6,1,-1,2,3,8,-1,8,7,2,-1,3,4,9,-1,9,8,3,-1,4,0,5,-1,5,9,4,-1,5,6,11,-1,11,10,5,-1,6,7,12,-1,12,11,6,-1,7,8,13,-1,13,12,7,-1,8,9,14,-1,14,13,8,-1,9,5,10,-1,10,14,9,-1,10,11,16,-1,16,15,10,-1,11,12,17,-1,17,16,11,-1,12,13,18,-1,18,17,12,-1,13,14,19,-1,19,18,13,-1,14,10,15,-1,15,19,14,-1,21,22,23,-1,20,21,23,-1,24,20,23,-1,21,20,15,-1,15,16,21,-1,22,21,16,-1,16,17,22,-1,23,22,17,-1,17,18,23,-1,24,23,18,-1,18,19,24,-1,20,24,19,-1,19,15,20,-1]
IndexedFaceSet528.creaseAngle = 3.14159
IndexedFaceSet528.texCoordIndex = [2,25,26,-1,3,2,26,-1,4,3,26,-1,0,1,6,-1,6,5,0,-1,27,2,7,-1,7,28,27,-1,2,3,8,-1,8,7,2,-1,3,4,9,-1,9,8,3,-1,4,0,5,-1,5,9,4,-1,5,6,11,-1,11,10,5,-1,29,7,12,-1,12,30,29,-1,7,8,13,-1,13,12,7,-1,8,9,14,-1,14,13,8,-1,9,5,10,-1,10,14,9,-1,10,11,16,-1,16,15,10,-1,31,12,17,-1,17,32,31,-1,12,13,18,-1,18,17,12,-1,13,14,19,-1,19,18,13,-1,14,10,15,-1,15,19,14,-1,34,22,23,-1,33,34,23,-1,24,33,23,-1,21,20,15,-1,15,16,21,-1,22,36,35,-1,35,17,22,-1,23,22,17,-1,17,18,23,-1,24,23,18,-1,18,19,24,-1,20,24,19,-1,19,15,20,-1]
Coordinate529 = x3d.Coordinate()

IndexedFaceSet528.coord = Coordinate529
TextureCoordinate530 = x3d.TextureCoordinate()

IndexedFaceSet528.texCoord = TextureCoordinate530

Shape524.geometry = IndexedFaceSet528

Transform523.children.append(Shape524)

HAnimSegment522.children.append(Transform523)

HAnimJoint521.children.append(HAnimSegment522)
HAnimJoint531 = x3d.HAnimJoint()
HAnimJoint531.name = "l_radiocarpal"
HAnimJoint531.DEF = "hanim_l_radiocarpal"
HAnimJoint531.center = [7.899,31.43,-0.3809]
HAnimJoint531.ulimit = [0,0,0]
HAnimJoint531.llimit = [0,0,0]
HAnimSegment532 = x3d.HAnimSegment()
HAnimSegment532.name = "l_carpal"
HAnimSegment532.DEF = "hanim_l_carpal"
Transform533 = x3d.Transform()
Transform533.translation = [7.899,31.43,-0.3809]
Shape534 = x3d.Shape()
Appearance535 = x3d.Appearance()
Material536 = x3d.Material()
Material536.diffuseColor = [0.588,0.588,0.588]

Appearance535.material = Material536
ImageTexture537 = x3d.ImageTexture()
ImageTexture537.USE = "JinLOA3TextureAtlas"

Appearance535.texture = ImageTexture537

Shape534.appearance = Appearance535
IndexedFaceSet538 = x3d.IndexedFaceSet()
IndexedFaceSet538.coordIndex = [36,37,38,-1,38,41,36,-1,44,45,54,-1,31,4,53,-1,53,30,31,-1,6,10,11,-1,11,7,6,-1,11,10,33,-1,33,32,11,-1,34,24,7,-1,7,11,34,-1,13,17,15,-1,15,27,13,-1,25,22,35,-1,30,5,20,-1,13,34,11,-1,11,32,13,-1,23,22,28,-1,28,29,23,-1,17,16,14,-1,14,15,17,-1,18,5,53,-1,53,19,18,-1,9,8,16,-1,16,17,9,-1,14,42,43,-1,43,15,14,-1,21,16,8,-1,8,33,21,-1,21,35,22,-1,22,23,21,-1,39,40,41,-1,41,38,39,-1,26,20,24,-1,27,12,20,-1,20,26,27,-1,3,30,12,-1,12,43,3,-1,0,54,28,-1,28,25,0,-1,13,32,9,-1,9,17,13,-1,28,31,29,-1,29,42,14,-1,14,23,29,-1,16,21,23,-1,23,14,16,-1,30,3,2,-1,2,31,30,-1,8,9,32,-1,32,33,8,-1,33,10,35,-1,35,21,33,-1,35,10,6,-1,6,25,35,-1,13,27,26,-1,26,34,13,-1,34,26,24,-1,1,0,47,-1,47,46,1,-1,25,48,47,-1,47,0,25,-1,25,6,49,-1,49,48,25,-1,6,7,50,-1,50,49,6,-1,24,51,50,-1,50,7,24,-1,24,1,46,-1,46,51,24,-1,2,3,43,-1,43,42,2,-1,15,43,12,-1,12,27,15,-1,29,31,2,-1,2,42,29,-1,18,44,52,-1,52,5,18,-1,28,22,25,-1,18,19,45,-1,45,44,18,-1,1,24,52,-1,52,44,1,-1,45,4,28,-1,28,4,31,-1,45,19,4,-1,37,36,46,-1,46,47,37,-1,48,38,37,-1,37,47,48,-1,39,38,48,-1,48,49,39,-1,40,39,49,-1,49,50,40,-1,51,41,40,-1,40,50,51,-1,36,41,51,-1,51,46,36,-1,24,20,52,-1,52,20,5,-1,53,5,30,-1,53,4,19,-1,54,45,28,-1,44,54,0,-1,0,1,44,-1,20,12,30,-1]
IndexedFaceSet538.creaseAngle = 3.14159
IndexedFaceSet538.texCoordIndex = [0,1,2,-1,2,3,0,-1,4,5,6,-1,8,9,10,-1,10,7,8,-1,12,13,14,-1,14,11,12,-1,14,13,15,-1,15,16,14,-1,17,18,11,-1,11,14,17,-1,20,21,22,-1,22,19,20,-1,23,24,25,-1,7,26,27,-1,20,17,14,-1,14,16,20,-1,28,24,29,-1,29,30,28,-1,21,31,32,-1,32,22,21,-1,33,26,10,-1,10,34,33,-1,35,36,31,-1,31,21,35,-1,32,37,38,-1,38,22,32,-1,39,31,36,-1,36,15,39,-1,39,25,24,-1,24,28,39,-1,40,41,3,-1,3,2,40,-1,42,27,18,-1,19,43,27,-1,27,42,19,-1,44,7,43,-1,43,38,44,-1,45,6,29,-1,29,23,45,-1,20,16,35,-1,35,21,20,-1,29,8,30,-1,30,37,32,-1,32,28,30,-1,31,39,28,-1,28,32,31,-1,7,44,46,-1,46,8,7,-1,36,35,16,-1,16,15,36,-1,15,13,25,-1,25,39,15,-1,25,13,12,-1,12,23,25,-1,20,19,42,-1,42,17,20,-1,17,42,18,-1,47,45,48,-1,48,49,47,-1,23,50,48,-1,48,45,23,-1,23,12,51,-1,51,50,23,-1,12,11,52,-1,52,51,12,-1,18,53,52,-1,52,11,18,-1,18,47,49,-1,49,53,18,-1,46,44,38,-1,38,37,46,-1,22,38,43,-1,43,19,22,-1,30,8,46,-1,46,37,30,-1,33,4,54,-1,54,26,33,-1,29,24,23,-1,33,34,5,-1,5,4,33,-1,47,18,54,-1,54,4,47,-1,5,9,29,-1,29,9,8,-1,5,34,9,-1,1,0,49,-1,49,48,1,-1,50,2,1,-1,1,48,50,-1,40,2,50,-1,50,51,40,-1,41,40,51,-1,51,52,41,-1,53,3,41,-1,41,52,53,-1,0,3,53,-1,53,49,0,-1,18,27,54,-1,54,27,26,-1,10,26,7,-1,10,9,34,-1,6,5,29,-1,4,6,45,-1,45,47,4,-1,27,43,7,-1]
Coordinate539 = x3d.Coordinate()

IndexedFaceSet538.coord = Coordinate539
TextureCoordinate540 = x3d.TextureCoordinate()

IndexedFaceSet538.texCoord = TextureCoordinate540

Shape534.geometry = IndexedFaceSet538

Transform533.children.append(Shape534)

HAnimSegment532.children.append(Transform533)

HAnimJoint531.children.append(HAnimSegment532)
HAnimJoint541 = x3d.HAnimJoint()
HAnimJoint541.name = "l_carpometacarpal_1"
HAnimJoint541.DEF = "hanim_l_carpometacarpal_1"
HAnimJoint541.center = [8.205,29.6,1.302]
HAnimJoint541.ulimit = [0,0,0]
HAnimJoint541.llimit = [0,0,0]
HAnimSegment542 = x3d.HAnimSegment()
HAnimSegment542.name = "l_metacarpal_1"
HAnimSegment542.DEF = "hanim_l_metacarpal_1"
Transform543 = x3d.Transform()
Transform543.translation = [8.205,29.6,1.302]
Shape544 = x3d.Shape()
Appearance545 = x3d.Appearance()
Material546 = x3d.Material()
Material546.diffuseColor = [0.588,0.588,0.588]

Appearance545.material = Material546
ImageTexture547 = x3d.ImageTexture()
ImageTexture547.USE = "JinLOA3TextureAtlas"

Appearance545.texture = ImageTexture547

Shape544.appearance = Appearance545
IndexedFaceSet548 = x3d.IndexedFaceSet()
IndexedFaceSet548.coordIndex = [0,1,3,-1,3,2,0,-1,0,5,4,-1,0,2,6,-1,6,5,0,-1,2,7,6,-1,2,3,8,-1,8,7,2,-1,3,9,8,-1,3,1,10,-1,10,9,3,-1,1,11,10,-1,1,0,4,-1,4,11,1,-1,4,5,13,-1,13,12,4,-1,5,6,14,-1,14,13,5,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,4,12,-1,12,19,11,-1,12,13,21,-1,21,20,12,-1,13,14,22,-1,22,21,13,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,12,20,-1,20,27,19,-1,20,21,29,-1,29,28,20,-1,21,22,30,-1,30,29,21,-1,22,23,31,-1,31,30,22,-1,23,24,32,-1,32,31,23,-1,24,25,33,-1,33,32,24,-1,25,26,34,-1,34,33,25,-1,26,27,35,-1,35,34,26,-1,27,20,28,-1,28,35,27,-1,36,28,29,-1,36,29,30,-1,36,30,31,-1,36,31,32,-1,36,32,33,-1,36,33,34,-1,36,34,35,-1,36,35,28,-1]
IndexedFaceSet548.creaseAngle = 3.14159
IndexedFaceSet548.texCoordIndex = [0,1,2,-1,2,3,0,-1,0,4,5,-1,0,3,6,-1,6,4,0,-1,3,7,6,-1,3,2,8,-1,8,7,3,-1,2,9,8,-1,2,1,10,-1,10,9,2,-1,1,11,10,-1,1,0,5,-1,5,11,1,-1,5,4,12,-1,12,13,5,-1,4,6,14,-1,14,12,4,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,5,13,-1,13,19,11,-1,13,12,20,-1,20,21,13,-1,12,14,22,-1,22,20,12,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,13,21,-1,21,27,19,-1,21,20,28,-1,28,29,21,-1,20,22,30,-1,30,28,20,-1,22,23,31,-1,31,30,22,-1,23,24,32,-1,32,31,23,-1,24,25,33,-1,33,32,24,-1,25,26,34,-1,34,33,25,-1,26,27,35,-1,35,34,26,-1,27,21,29,-1,29,35,27,-1,36,29,28,-1,36,28,30,-1,36,30,31,-1,36,31,32,-1,36,32,33,-1,36,33,34,-1,36,34,35,-1,36,35,29,-1]
Coordinate549 = x3d.Coordinate()

IndexedFaceSet548.coord = Coordinate549
TextureCoordinate550 = x3d.TextureCoordinate()

IndexedFaceSet548.texCoord = TextureCoordinate550

Shape544.geometry = IndexedFaceSet548

Transform543.children.append(Shape544)

HAnimSegment542.children.append(Transform543)

HAnimJoint541.children.append(HAnimSegment542)
HAnimJoint551 = x3d.HAnimJoint()
HAnimJoint551.name = "l_metacarpophalangeal_1"
HAnimJoint551.DEF = "hanim_l_metacarpophalangeal_1"
HAnimJoint551.center = [8.08,28.73,1.55]
HAnimJoint551.ulimit = [0,0,0]
HAnimJoint551.llimit = [0,0,0]
HAnimSegment552 = x3d.HAnimSegment()
HAnimSegment552.name = "l_carpal_proximal_phalanx_1"
HAnimSegment552.DEF = "hanim_l_carpal_proximal_phalanx_1"
Transform553 = x3d.Transform()
Transform553.translation = [8.08,28.73,1.55]
Shape554 = x3d.Shape()
Appearance555 = x3d.Appearance()
Material556 = x3d.Material()
Material556.diffuseColor = [0.588,0.588,0.588]

Appearance555.material = Material556
ImageTexture557 = x3d.ImageTexture()
ImageTexture557.USE = "JinLOA3TextureAtlas"

Appearance555.texture = ImageTexture557

Shape554.appearance = Appearance555
IndexedFaceSet558 = x3d.IndexedFaceSet()
IndexedFaceSet558.coordIndex = [0,1,3,-1,3,2,0,-1,0,5,4,-1,0,2,6,-1,6,5,0,-1,2,7,6,-1,2,3,8,-1,8,7,2,-1,3,9,8,-1,3,1,10,-1,10,9,3,-1,1,11,10,-1,1,0,4,-1,4,11,1,-1,4,5,13,-1,13,12,4,-1,5,6,14,-1,14,13,5,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,4,12,-1,12,19,11,-1,12,13,21,-1,21,20,12,-1,13,14,22,-1,22,21,13,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,12,20,-1,20,27,19,-1,20,21,29,-1,29,28,20,-1,21,22,30,-1,30,29,21,-1,22,23,31,-1,31,30,22,-1,23,24,32,-1,32,31,23,-1,24,25,33,-1,33,32,24,-1,25,26,34,-1,34,33,25,-1,26,27,35,-1,35,34,26,-1,27,20,28,-1,28,35,27,-1,36,28,29,-1,36,29,30,-1,36,30,31,-1,36,31,32,-1,36,32,33,-1,36,33,34,-1,36,34,35,-1,36,35,28,-1]
IndexedFaceSet558.creaseAngle = 3.14159
IndexedFaceSet558.texCoordIndex = [0,1,2,-1,2,3,0,-1,0,4,5,-1,0,3,6,-1,6,4,0,-1,3,7,6,-1,3,2,8,-1,8,7,3,-1,2,9,8,-1,2,1,10,-1,10,9,2,-1,1,11,10,-1,1,0,5,-1,5,11,1,-1,5,4,12,-1,12,13,5,-1,4,6,14,-1,14,12,4,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,5,13,-1,13,19,11,-1,13,12,20,-1,20,21,13,-1,12,14,22,-1,22,20,12,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,13,21,-1,21,27,19,-1,21,20,28,-1,28,29,21,-1,20,22,30,-1,30,28,20,-1,22,23,31,-1,31,30,22,-1,23,24,32,-1,32,31,23,-1,24,25,33,-1,33,32,24,-1,25,26,34,-1,34,33,25,-1,26,27,35,-1,35,34,26,-1,27,21,29,-1,29,35,27,-1,36,29,28,-1,36,28,30,-1,36,30,31,-1,36,31,32,-1,36,32,33,-1,36,33,34,-1,36,34,35,-1,36,35,29,-1]
Coordinate559 = x3d.Coordinate()

IndexedFaceSet558.coord = Coordinate559
TextureCoordinate560 = x3d.TextureCoordinate()

IndexedFaceSet558.texCoord = TextureCoordinate560

Shape554.geometry = IndexedFaceSet558

Transform553.children.append(Shape554)

HAnimSegment552.children.append(Transform553)

HAnimJoint551.children.append(HAnimSegment552)
HAnimJoint561 = x3d.HAnimJoint()
HAnimJoint561.name = "l_carpal_interphalangeal_1"
HAnimJoint561.DEF = "hanim_l_carpal_interphalangeal_1"
HAnimJoint561.center = [7.832,27.85,1.735]
HAnimJoint561.ulimit = [0,0,0]
HAnimJoint561.llimit = [0,0,0]
HAnimSegment562 = x3d.HAnimSegment()
HAnimSegment562.name = "l_carpal_distal_phalanx_1"
HAnimSegment562.DEF = "hanim_l_carpal_distal_phalanx_1"
Transform563 = x3d.Transform()
Transform563.translation = [7.832,27.85,1.735]
Shape564 = x3d.Shape()
Appearance565 = x3d.Appearance()
Material566 = x3d.Material()
Material566.diffuseColor = [0.588,0.588,0.588]

Appearance565.material = Material566
ImageTexture567 = x3d.ImageTexture()
ImageTexture567.USE = "JinLOA3TextureAtlas"

Appearance565.texture = ImageTexture567

Shape564.appearance = Appearance565
IndexedFaceSet568 = x3d.IndexedFaceSet()
IndexedFaceSet568.coordIndex = [0,1,3,-1,3,2,0,-1,0,5,4,-1,0,2,6,-1,6,5,0,-1,2,7,6,-1,2,3,8,-1,8,7,2,-1,3,9,8,-1,3,1,10,-1,10,9,3,-1,1,11,10,-1,1,0,4,-1,4,11,1,-1,4,5,13,-1,13,12,4,-1,5,6,14,-1,14,13,5,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,4,12,-1,12,19,11,-1,12,13,21,-1,21,20,12,-1,13,14,22,-1,22,21,13,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,12,20,-1,20,27,19,-1,28,20,21,-1,28,21,22,-1,28,22,23,-1,28,23,24,-1,28,24,25,-1,28,25,26,-1,28,26,27,-1,28,27,20,-1]
IndexedFaceSet568.creaseAngle = 3.14159
IndexedFaceSet568.texCoordIndex = [0,1,2,-1,2,3,0,-1,0,4,5,-1,0,3,6,-1,6,4,0,-1,3,7,6,-1,3,2,8,-1,8,7,3,-1,2,9,8,-1,2,1,10,-1,10,9,2,-1,1,11,10,-1,1,0,5,-1,5,11,1,-1,5,4,12,-1,12,13,5,-1,4,6,14,-1,14,12,4,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,5,13,-1,13,19,11,-1,13,12,20,-1,20,21,13,-1,12,14,22,-1,22,20,12,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,13,21,-1,21,27,19,-1,28,21,20,-1,28,20,22,-1,28,22,23,-1,28,23,24,-1,28,24,25,-1,28,25,26,-1,28,26,27,-1,28,27,21,-1]
Coordinate569 = x3d.Coordinate()

IndexedFaceSet568.coord = Coordinate569
TextureCoordinate570 = x3d.TextureCoordinate()

IndexedFaceSet568.texCoord = TextureCoordinate570

Shape564.geometry = IndexedFaceSet568

Transform563.children.append(Shape564)

HAnimSegment562.children.append(Transform563)

HAnimJoint561.children.append(HAnimSegment562)

HAnimJoint551.children.append(HAnimJoint561)

HAnimJoint541.children.append(HAnimJoint551)

HAnimJoint531.children.append(HAnimJoint541)
HAnimJoint571 = x3d.HAnimJoint()
HAnimJoint571.name = "l_carpometacarpal_2"
HAnimJoint571.DEF = "hanim_l_carpometacarpal_2"
HAnimJoint571.center = [8.376,28.549999,0.5997]
HAnimJoint571.ulimit = [0,0,0]
HAnimJoint571.llimit = [0,0,0]
HAnimSegment572 = x3d.HAnimSegment()
HAnimSegment572.name = "l_metacarpal_2"
HAnimSegment572.DEF = "hanim_l_metacarpal_2"
Transform573 = x3d.Transform()
Transform573.translation = [8.376,28.549999,0.5997]
Shape574 = x3d.Shape()
Appearance575 = x3d.Appearance()
Material576 = x3d.Material()
Material576.diffuseColor = [0.588,0.588,0.588]

Appearance575.material = Material576
ImageTexture577 = x3d.ImageTexture()
ImageTexture577.USE = "JinLOA3TextureAtlas"

Appearance575.texture = ImageTexture577

Shape574.appearance = Appearance575
IndexedFaceSet578 = x3d.IndexedFaceSet()
IndexedFaceSet578.coordIndex = [0,1,3,-1,3,2,0,-1,0,5,4,-1,0,2,6,-1,6,5,0,-1,2,7,6,-1,2,3,8,-1,8,7,2,-1,3,9,8,-1,3,1,10,-1,10,9,3,-1,1,11,10,-1,1,0,4,-1,4,11,1,-1,4,5,13,-1,13,12,4,-1,5,6,14,-1,14,13,5,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,4,12,-1,12,19,11,-1,12,13,21,-1,21,20,12,-1,13,14,22,-1,22,21,13,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,12,20,-1,20,27,19,-1,20,21,29,-1,29,28,20,-1,21,22,30,-1,30,29,21,-1,22,23,31,-1,31,30,22,-1,23,24,32,-1,32,31,23,-1,24,25,33,-1,33,32,24,-1,25,26,34,-1,34,33,25,-1,26,27,35,-1,35,34,26,-1,27,20,28,-1,28,35,27,-1,36,28,29,-1,36,29,30,-1,36,30,31,-1,36,31,32,-1,36,32,33,-1,36,33,34,-1,36,34,35,-1,36,35,28,-1]
IndexedFaceSet578.creaseAngle = 3.14159
IndexedFaceSet578.texCoordIndex = [0,1,2,-1,2,3,0,-1,0,4,5,-1,0,3,6,-1,6,4,0,-1,3,7,6,-1,3,2,8,-1,8,7,3,-1,2,9,8,-1,2,1,10,-1,10,9,2,-1,1,11,10,-1,1,0,5,-1,5,11,1,-1,5,4,12,-1,12,13,5,-1,4,6,14,-1,14,12,4,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,5,13,-1,13,19,11,-1,13,12,20,-1,20,21,13,-1,12,14,22,-1,22,20,12,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,13,21,-1,21,27,19,-1,21,20,28,-1,28,29,21,-1,20,22,30,-1,30,28,20,-1,22,23,31,-1,31,30,22,-1,23,24,32,-1,32,31,23,-1,24,25,33,-1,33,32,24,-1,25,26,34,-1,34,33,25,-1,26,27,35,-1,35,34,26,-1,27,21,29,-1,29,35,27,-1,36,29,28,-1,36,28,30,-1,36,30,31,-1,36,31,32,-1,36,32,33,-1,36,33,34,-1,36,34,35,-1,36,35,29,-1]
Coordinate579 = x3d.Coordinate()

IndexedFaceSet578.coord = Coordinate579
TextureCoordinate580 = x3d.TextureCoordinate()

IndexedFaceSet578.texCoord = TextureCoordinate580

Shape574.geometry = IndexedFaceSet578

Transform573.children.append(Shape574)

HAnimSegment572.children.append(Transform573)

HAnimJoint571.children.append(HAnimSegment572)
HAnimJoint581 = x3d.HAnimJoint()
HAnimJoint581.name = "l_metacarpophalangeal_2"
HAnimJoint581.DEF = "hanim_l_metacarpophalangeal_2"
HAnimJoint581.center = [8.52,27.24,0.6551]
HAnimJoint581.ulimit = [0,0,0]
HAnimJoint581.llimit = [0,0,0]
HAnimSegment582 = x3d.HAnimSegment()
HAnimSegment582.name = "l_carpal_proximal_phalanx_2"
HAnimSegment582.DEF = "hanim_l_carpal_proximal_phalanx_2"
Transform583 = x3d.Transform()
Transform583.translation = [8.52,27.24,0.6551]
Shape584 = x3d.Shape()
Appearance585 = x3d.Appearance()
Material586 = x3d.Material()
Material586.diffuseColor = [0.588,0.588,0.588]

Appearance585.material = Material586
ImageTexture587 = x3d.ImageTexture()
ImageTexture587.USE = "JinLOA3TextureAtlas"

Appearance585.texture = ImageTexture587

Shape584.appearance = Appearance585
IndexedFaceSet588 = x3d.IndexedFaceSet()
IndexedFaceSet588.coordIndex = [0,1,3,-1,3,2,0,-1,0,5,4,-1,0,2,6,-1,6,5,0,-1,2,7,6,-1,2,3,8,-1,8,7,2,-1,3,9,8,-1,3,1,10,-1,10,9,3,-1,1,11,10,-1,1,0,4,-1,4,11,1,-1,4,5,13,-1,13,12,4,-1,5,6,14,-1,14,13,5,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,4,12,-1,12,19,11,-1,12,13,21,-1,21,20,12,-1,13,14,22,-1,22,21,13,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,12,20,-1,20,27,19,-1,20,21,29,-1,29,28,20,-1,21,22,30,-1,30,29,21,-1,22,23,31,-1,31,30,22,-1,23,24,32,-1,32,31,23,-1,24,25,33,-1,33,32,24,-1,25,26,34,-1,34,33,25,-1,26,27,35,-1,35,34,26,-1,27,20,28,-1,28,35,27,-1,36,28,29,-1,36,29,30,-1,36,30,31,-1,36,31,32,-1,36,32,33,-1,36,33,34,-1,36,34,35,-1,36,35,28,-1]
IndexedFaceSet588.creaseAngle = 3.14159
IndexedFaceSet588.texCoordIndex = [0,1,2,-1,2,3,0,-1,0,4,5,-1,0,3,6,-1,6,4,0,-1,3,7,6,-1,3,2,8,-1,8,7,3,-1,2,9,8,-1,2,1,10,-1,10,9,2,-1,1,11,10,-1,1,0,5,-1,5,11,1,-1,5,4,12,-1,12,13,5,-1,4,6,14,-1,14,12,4,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,5,13,-1,13,19,11,-1,13,12,20,-1,20,21,13,-1,12,14,22,-1,22,20,12,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,13,21,-1,21,27,19,-1,21,20,28,-1,28,29,21,-1,20,22,30,-1,30,28,20,-1,22,23,31,-1,31,30,22,-1,23,24,32,-1,32,31,23,-1,24,25,33,-1,33,32,24,-1,25,26,34,-1,34,33,25,-1,26,27,35,-1,35,34,26,-1,27,21,29,-1,29,35,27,-1,36,29,28,-1,36,28,30,-1,36,30,31,-1,36,31,32,-1,36,32,33,-1,36,33,34,-1,36,34,35,-1,36,35,29,-1]
Coordinate589 = x3d.Coordinate()

IndexedFaceSet588.coord = Coordinate589
TextureCoordinate590 = x3d.TextureCoordinate()

IndexedFaceSet588.texCoord = TextureCoordinate590

Shape584.geometry = IndexedFaceSet588

Transform583.children.append(Shape584)

HAnimSegment582.children.append(Transform583)

HAnimJoint581.children.append(HAnimSegment582)
HAnimJoint591 = x3d.HAnimJoint()
HAnimJoint591.name = "l_carpal_proximal_interphalangeal_2"
HAnimJoint591.DEF = "hanim_l_carpal_proximal_interphalangeal_2"
HAnimJoint591.center = [8.45,26.1,0.6956]
HAnimJoint591.ulimit = [0,0,0]
HAnimJoint591.llimit = [0,0,0]
HAnimSegment592 = x3d.HAnimSegment()
HAnimSegment592.name = "l_carpal_middle_phalanx_2"
HAnimSegment592.DEF = "hanim_l_carpal_middle_phalanx_2"
Transform593 = x3d.Transform()
Transform593.translation = [8.45,26.1,0.6956]
Shape594 = x3d.Shape()
Appearance595 = x3d.Appearance()
Material596 = x3d.Material()
Material596.diffuseColor = [0.588,0.588,0.588]

Appearance595.material = Material596
ImageTexture597 = x3d.ImageTexture()
ImageTexture597.USE = "JinLOA3TextureAtlas"

Appearance595.texture = ImageTexture597

Shape594.appearance = Appearance595
IndexedFaceSet598 = x3d.IndexedFaceSet()
IndexedFaceSet598.coordIndex = [0,1,3,-1,3,2,0,-1,0,5,4,-1,0,2,6,-1,6,5,0,-1,2,7,6,-1,2,3,8,-1,8,7,2,-1,3,9,8,-1,3,1,10,-1,10,9,3,-1,1,11,10,-1,1,0,4,-1,4,11,1,-1,4,5,13,-1,13,12,4,-1,5,6,14,-1,14,13,5,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,4,12,-1,12,19,11,-1,12,13,21,-1,21,20,12,-1,13,14,22,-1,22,21,13,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,12,20,-1,20,27,19,-1,28,20,21,-1,28,21,22,-1,28,22,23,-1,28,23,24,-1,28,24,25,-1,28,25,26,-1,28,26,27,-1,28,27,20,-1]
IndexedFaceSet598.creaseAngle = 3.14159
IndexedFaceSet598.texCoordIndex = [0,1,2,-1,2,3,0,-1,0,4,5,-1,0,3,6,-1,6,4,0,-1,3,7,6,-1,3,2,8,-1,8,7,3,-1,2,9,8,-1,2,1,10,-1,10,9,2,-1,1,11,10,-1,1,0,5,-1,5,11,1,-1,5,4,12,-1,12,13,5,-1,4,6,14,-1,14,12,4,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,5,13,-1,13,19,11,-1,13,12,20,-1,20,21,13,-1,12,14,22,-1,22,20,12,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,13,21,-1,21,27,19,-1,28,21,20,-1,28,20,22,-1,28,22,23,-1,28,23,24,-1,28,24,25,-1,28,25,26,-1,28,26,27,-1,28,27,21,-1]
Coordinate599 = x3d.Coordinate()

IndexedFaceSet598.coord = Coordinate599
TextureCoordinate600 = x3d.TextureCoordinate()

IndexedFaceSet598.texCoord = TextureCoordinate600

Shape594.geometry = IndexedFaceSet598

Transform593.children.append(Shape594)

HAnimSegment592.children.append(Transform593)

HAnimJoint591.children.append(HAnimSegment592)
HAnimJoint601 = x3d.HAnimJoint()
HAnimJoint601.name = "l_carpal_distal_interphalangeal_2"
HAnimJoint601.DEF = "hanim_l_carpal_distal_interphalangeal_2"
HAnimJoint601.center = [8.192,25.17,0.7315]
HAnimJoint601.ulimit = [0,0,0]
HAnimJoint601.llimit = [0,0,0]
HAnimSegment602 = x3d.HAnimSegment()
HAnimSegment602.name = "l_carpal_distal_phalanx_2"
HAnimSegment602.DEF = "hanim_l_carpal_distal_phalanx_2"
Transform603 = x3d.Transform()
Transform603.translation = [8.192,25.17,0.7315]
Shape604 = x3d.Shape()
Appearance605 = x3d.Appearance()
Material606 = x3d.Material()
Material606.diffuseColor = [0.588,0.588,0.588]

Appearance605.material = Material606
ImageTexture607 = x3d.ImageTexture()
ImageTexture607.USE = "JinLOA3TextureAtlas"

Appearance605.texture = ImageTexture607

Shape604.appearance = Appearance605
IndexedFaceSet608 = x3d.IndexedFaceSet()
IndexedFaceSet608.coordIndex = [0,1,3,-1,3,2,0,-1,0,5,4,-1,0,2,6,-1,6,5,0,-1,2,7,6,-1,2,3,8,-1,8,7,2,-1,3,9,8,-1,3,1,10,-1,10,9,3,-1,1,11,10,-1,1,0,4,-1,4,11,1,-1,4,5,13,-1,13,12,4,-1,5,6,14,-1,14,13,5,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,4,12,-1,12,19,11,-1,12,13,21,-1,21,20,12,-1,13,14,22,-1,22,21,13,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,12,20,-1,20,27,19,-1,28,20,21,-1,28,21,22,-1,28,22,23,-1,28,23,24,-1,28,24,25,-1,28,25,26,-1,28,26,27,-1,28,27,20,-1]
IndexedFaceSet608.creaseAngle = 3.14159
IndexedFaceSet608.texCoordIndex = [0,1,2,-1,2,3,0,-1,0,4,5,-1,0,3,6,-1,6,4,0,-1,3,7,6,-1,3,2,8,-1,8,7,3,-1,2,9,8,-1,2,1,10,-1,10,9,2,-1,1,11,10,-1,1,0,5,-1,5,11,1,-1,5,4,12,-1,12,13,5,-1,4,6,14,-1,14,12,4,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,5,13,-1,13,19,11,-1,13,12,20,-1,20,21,13,-1,12,14,22,-1,22,20,12,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,13,21,-1,21,27,19,-1,28,21,20,-1,28,20,22,-1,28,22,23,-1,28,23,24,-1,28,24,25,-1,28,25,26,-1,28,26,27,-1,28,27,21,-1]
Coordinate609 = x3d.Coordinate()

IndexedFaceSet608.coord = Coordinate609
TextureCoordinate610 = x3d.TextureCoordinate()

IndexedFaceSet608.texCoord = TextureCoordinate610

Shape604.geometry = IndexedFaceSet608

Transform603.children.append(Shape604)

HAnimSegment602.children.append(Transform603)

HAnimJoint601.children.append(HAnimSegment602)

HAnimJoint591.children.append(HAnimJoint601)

HAnimJoint581.children.append(HAnimJoint591)

HAnimJoint571.children.append(HAnimJoint581)

HAnimJoint531.children.append(HAnimJoint571)
HAnimJoint611 = x3d.HAnimJoint()
HAnimJoint611.name = "l_carpometacarpal_3"
HAnimJoint611.DEF = "hanim_l_carpometacarpal_3"
HAnimJoint611.center = [8.344,28.65,-0.194]
HAnimJoint611.ulimit = [0,0,0]
HAnimJoint611.llimit = [0,0,0]
HAnimSegment612 = x3d.HAnimSegment()
HAnimSegment612.name = "l_metacarpal_3"
HAnimSegment612.DEF = "hanim_l_metacarpal_3"
Transform613 = x3d.Transform()
Transform613.translation = [8.344,28.65,-0.194]
Shape614 = x3d.Shape()
Appearance615 = x3d.Appearance()
Material616 = x3d.Material()
Material616.diffuseColor = [0.588,0.588,0.588]

Appearance615.material = Material616
ImageTexture617 = x3d.ImageTexture()
ImageTexture617.USE = "JinLOA3TextureAtlas"

Appearance615.texture = ImageTexture617

Shape614.appearance = Appearance615
IndexedFaceSet618 = x3d.IndexedFaceSet()
IndexedFaceSet618.coordIndex = [0,1,3,-1,3,2,0,-1,0,5,4,-1,0,2,6,-1,6,5,0,-1,2,7,6,-1,2,3,8,-1,8,7,2,-1,3,9,8,-1,3,1,10,-1,10,9,3,-1,1,11,10,-1,1,0,4,-1,4,11,1,-1,4,5,13,-1,13,12,4,-1,5,6,14,-1,14,13,5,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,4,12,-1,12,19,11,-1,12,13,21,-1,21,20,12,-1,13,14,22,-1,22,21,13,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,12,20,-1,20,27,19,-1,20,21,29,-1,29,28,20,-1,21,22,30,-1,30,29,21,-1,22,23,31,-1,31,30,22,-1,23,24,32,-1,32,31,23,-1,24,25,33,-1,33,32,24,-1,25,26,34,-1,34,33,25,-1,26,27,35,-1,35,34,26,-1,27,20,28,-1,28,35,27,-1,36,28,29,-1,36,29,30,-1,36,30,31,-1,36,31,32,-1,36,32,33,-1,36,33,34,-1,36,34,35,-1,36,35,28,-1]
IndexedFaceSet618.creaseAngle = 3.14159
IndexedFaceSet618.texCoordIndex = [0,1,2,-1,2,3,0,-1,0,4,5,-1,0,3,6,-1,6,4,0,-1,3,7,6,-1,3,2,8,-1,8,7,3,-1,2,9,8,-1,2,1,10,-1,10,9,2,-1,1,11,10,-1,1,0,5,-1,5,11,1,-1,5,4,12,-1,12,13,5,-1,4,6,14,-1,14,12,4,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,5,13,-1,13,19,11,-1,13,12,20,-1,20,21,13,-1,12,14,22,-1,22,20,12,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,13,21,-1,21,27,19,-1,21,20,28,-1,28,29,21,-1,20,22,30,-1,30,28,20,-1,22,23,31,-1,31,30,22,-1,23,24,32,-1,32,31,23,-1,24,25,33,-1,33,32,24,-1,25,26,34,-1,34,33,25,-1,26,27,35,-1,35,34,26,-1,27,21,29,-1,29,35,27,-1,36,29,28,-1,36,28,30,-1,36,30,31,-1,36,31,32,-1,36,32,33,-1,36,33,34,-1,36,34,35,-1,36,35,29,-1]
Coordinate619 = x3d.Coordinate()

IndexedFaceSet618.coord = Coordinate619
TextureCoordinate620 = x3d.TextureCoordinate()

IndexedFaceSet618.texCoord = TextureCoordinate620

Shape614.geometry = IndexedFaceSet618

Transform613.children.append(Shape614)

HAnimSegment612.children.append(Transform613)

HAnimJoint611.children.append(HAnimSegment612)
HAnimJoint621 = x3d.HAnimJoint()
HAnimJoint621.name = "l_metacarpophalangeal_3"
HAnimJoint621.DEF = "hanim_l_metacarpophalangeal_3"
HAnimJoint621.center = [8.52,27.26,-0.1959]
HAnimJoint621.ulimit = [0,0,0]
HAnimJoint621.llimit = [0,0,0]
HAnimSegment622 = x3d.HAnimSegment()
HAnimSegment622.name = "l_carpal_proximal_phalanx_3"
HAnimSegment622.DEF = "hanim_l_carpal_proximal_phalanx_3"
Transform623 = x3d.Transform()
Transform623.translation = [8.52,27.26,-0.1959]
Shape624 = x3d.Shape()
Appearance625 = x3d.Appearance()
Material626 = x3d.Material()
Material626.diffuseColor = [0.588,0.588,0.588]

Appearance625.material = Material626
ImageTexture627 = x3d.ImageTexture()
ImageTexture627.USE = "JinLOA3TextureAtlas"

Appearance625.texture = ImageTexture627

Shape624.appearance = Appearance625
IndexedFaceSet628 = x3d.IndexedFaceSet()
IndexedFaceSet628.coordIndex = [0,1,3,-1,3,2,0,-1,0,5,4,-1,0,2,6,-1,6,5,0,-1,2,7,6,-1,2,3,8,-1,8,7,2,-1,3,9,8,-1,3,1,10,-1,10,9,3,-1,1,11,10,-1,1,0,4,-1,4,11,1,-1,4,5,13,-1,13,12,4,-1,5,6,14,-1,14,13,5,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,4,12,-1,12,19,11,-1,12,13,21,-1,21,20,12,-1,13,14,22,-1,22,21,13,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,12,20,-1,20,27,19,-1,20,21,29,-1,29,28,20,-1,21,22,30,-1,30,29,21,-1,22,23,31,-1,31,30,22,-1,23,24,32,-1,32,31,23,-1,24,25,33,-1,33,32,24,-1,25,26,34,-1,34,33,25,-1,26,27,35,-1,35,34,26,-1,27,20,28,-1,28,35,27,-1,36,28,29,-1,36,29,30,-1,36,30,31,-1,36,31,32,-1,36,32,33,-1,36,33,34,-1,36,34,35,-1,36,35,28,-1]
IndexedFaceSet628.creaseAngle = 3.14159
IndexedFaceSet628.texCoordIndex = [0,1,2,-1,2,3,0,-1,0,4,5,-1,0,3,6,-1,6,4,0,-1,3,7,6,-1,3,2,8,-1,8,7,3,-1,2,9,8,-1,2,1,10,-1,10,9,2,-1,1,11,10,-1,1,0,5,-1,5,11,1,-1,5,4,12,-1,12,13,5,-1,4,6,14,-1,14,12,4,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,5,13,-1,13,19,11,-1,13,12,20,-1,20,21,13,-1,12,14,22,-1,22,20,12,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,13,21,-1,21,27,19,-1,21,20,28,-1,28,29,21,-1,20,22,30,-1,30,28,20,-1,22,23,31,-1,31,30,22,-1,23,24,32,-1,32,31,23,-1,24,25,33,-1,33,32,24,-1,25,26,34,-1,34,33,25,-1,26,27,35,-1,35,34,26,-1,27,21,29,-1,29,35,27,-1,36,29,28,-1,36,28,30,-1,36,30,31,-1,36,31,32,-1,36,32,33,-1,36,33,34,-1,36,34,35,-1,36,35,29,-1]
Coordinate629 = x3d.Coordinate()

IndexedFaceSet628.coord = Coordinate629
TextureCoordinate630 = x3d.TextureCoordinate()

IndexedFaceSet628.texCoord = TextureCoordinate630

Shape624.geometry = IndexedFaceSet628

Transform623.children.append(Shape624)

HAnimSegment622.children.append(Transform623)

HAnimJoint621.children.append(HAnimSegment622)
HAnimJoint631 = x3d.HAnimJoint()
HAnimJoint631.name = "l_carpal_proximal_interphalangeal_3"
HAnimJoint631.DEF = "hanim_l_carpal_proximal_interphalangeal_3"
HAnimJoint631.center = [8.477,26.07,-0.2214]
HAnimJoint631.ulimit = [0,0,0]
HAnimJoint631.llimit = [0,0,0]
HAnimSegment632 = x3d.HAnimSegment()
HAnimSegment632.name = "l_carpal_middle_phalanx_3"
HAnimSegment632.DEF = "hanim_l_carpal_middle_phalanx_3"
Transform633 = x3d.Transform()
Transform633.translation = [8.477,26.07,-0.2214]
Shape634 = x3d.Shape()
Appearance635 = x3d.Appearance()
Material636 = x3d.Material()
Material636.diffuseColor = [0.588,0.588,0.588]

Appearance635.material = Material636
ImageTexture637 = x3d.ImageTexture()
ImageTexture637.USE = "JinLOA3TextureAtlas"

Appearance635.texture = ImageTexture637

Shape634.appearance = Appearance635
IndexedFaceSet638 = x3d.IndexedFaceSet()
IndexedFaceSet638.coordIndex = [0,1,3,-1,3,2,0,-1,0,5,4,-1,0,2,6,-1,6,5,0,-1,2,7,6,-1,2,3,8,-1,8,7,2,-1,3,9,8,-1,3,1,10,-1,10,9,3,-1,1,11,10,-1,1,0,4,-1,4,11,1,-1,4,5,13,-1,13,12,4,-1,5,6,14,-1,14,13,5,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,4,12,-1,12,19,11,-1,12,13,21,-1,21,20,12,-1,13,14,22,-1,22,21,13,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,12,20,-1,20,27,19,-1,28,20,21,-1,28,21,22,-1,28,22,23,-1,28,23,24,-1,28,24,25,-1,28,25,26,-1,28,26,27,-1,28,27,20,-1]
IndexedFaceSet638.creaseAngle = 3.14159
IndexedFaceSet638.texCoordIndex = [0,1,2,-1,2,3,0,-1,0,4,5,-1,0,3,6,-1,6,4,0,-1,3,7,6,-1,3,2,8,-1,8,7,3,-1,2,9,8,-1,2,1,10,-1,10,9,2,-1,1,11,10,-1,1,0,5,-1,5,11,1,-1,5,4,12,-1,12,13,5,-1,4,6,14,-1,14,12,4,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,5,13,-1,13,19,11,-1,13,12,20,-1,20,21,13,-1,12,14,22,-1,22,20,12,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,13,21,-1,21,27,19,-1,28,21,20,-1,28,20,22,-1,28,22,23,-1,28,23,24,-1,28,24,25,-1,28,25,26,-1,28,26,27,-1,28,27,21,-1]
Coordinate639 = x3d.Coordinate()

IndexedFaceSet638.coord = Coordinate639
TextureCoordinate640 = x3d.TextureCoordinate()

IndexedFaceSet638.texCoord = TextureCoordinate640

Shape634.geometry = IndexedFaceSet638

Transform633.children.append(Shape634)

HAnimSegment632.children.append(Transform633)

HAnimJoint631.children.append(HAnimSegment632)
HAnimJoint641 = x3d.HAnimJoint()
HAnimJoint641.name = "l_carpal_distal_interphalangeal_3"
HAnimJoint641.DEF = "hanim_l_carpal_distal_interphalangeal_3"
HAnimJoint641.center = [8.25,25.030001,-0.2187]
HAnimJoint641.ulimit = [0,0,0]
HAnimJoint641.llimit = [0,0,0]
HAnimSegment642 = x3d.HAnimSegment()
HAnimSegment642.name = "l_carpal_distal_phalanx_3"
HAnimSegment642.DEF = "hanim_l_carpal_distal_phalanx_3"
Transform643 = x3d.Transform()
Transform643.translation = [8.25,25.030001,-0.2187]
Shape644 = x3d.Shape()
Appearance645 = x3d.Appearance()
Material646 = x3d.Material()
Material646.diffuseColor = [0.588,0.588,0.588]

Appearance645.material = Material646
ImageTexture647 = x3d.ImageTexture()
ImageTexture647.USE = "JinLOA3TextureAtlas"

Appearance645.texture = ImageTexture647

Shape644.appearance = Appearance645
IndexedFaceSet648 = x3d.IndexedFaceSet()
IndexedFaceSet648.coordIndex = [0,1,3,-1,3,2,0,-1,0,5,4,-1,0,2,6,-1,6,5,0,-1,2,7,6,-1,2,3,8,-1,8,7,2,-1,3,9,8,-1,3,1,10,-1,10,9,3,-1,1,11,10,-1,1,0,4,-1,4,11,1,-1,4,5,13,-1,13,12,4,-1,5,6,14,-1,14,13,5,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,4,12,-1,12,19,11,-1,12,13,21,-1,21,20,12,-1,13,14,22,-1,22,21,13,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,12,20,-1,20,27,19,-1,28,20,21,-1,28,21,22,-1,28,22,23,-1,28,23,24,-1,28,24,25,-1,28,25,26,-1,28,26,27,-1,28,27,20,-1]
IndexedFaceSet648.creaseAngle = 3.14159
IndexedFaceSet648.texCoordIndex = [0,1,2,-1,2,3,0,-1,0,4,5,-1,0,3,6,-1,6,4,0,-1,3,7,6,-1,3,2,8,-1,8,7,3,-1,2,9,8,-1,2,1,10,-1,10,9,2,-1,1,11,10,-1,1,0,5,-1,5,11,1,-1,5,4,12,-1,12,13,5,-1,4,6,14,-1,14,12,4,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,5,13,-1,13,19,11,-1,13,12,20,-1,20,21,13,-1,12,14,22,-1,22,20,12,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,13,21,-1,21,27,19,-1,28,21,20,-1,28,20,22,-1,28,22,23,-1,28,23,24,-1,28,24,25,-1,28,25,26,-1,28,26,27,-1,28,27,21,-1]
Coordinate649 = x3d.Coordinate()

IndexedFaceSet648.coord = Coordinate649
TextureCoordinate650 = x3d.TextureCoordinate()

IndexedFaceSet648.texCoord = TextureCoordinate650

Shape644.geometry = IndexedFaceSet648

Transform643.children.append(Shape644)

HAnimSegment642.children.append(Transform643)

HAnimJoint641.children.append(HAnimSegment642)

HAnimJoint631.children.append(HAnimJoint641)

HAnimJoint621.children.append(HAnimJoint631)

HAnimJoint611.children.append(HAnimJoint621)

HAnimJoint531.children.append(HAnimJoint611)
HAnimJoint651 = x3d.HAnimJoint()
HAnimJoint651.name = "l_carpometacarpal_4"
HAnimJoint651.DEF = "hanim_l_carpometacarpal_4"
HAnimJoint651.center = [8.339,28.57,-0.9243]
HAnimJoint651.ulimit = [0,0,0]
HAnimJoint651.llimit = [0,0,0]
HAnimSegment652 = x3d.HAnimSegment()
HAnimSegment652.name = "l_metacarpal_4"
HAnimSegment652.DEF = "hanim_l_metacarpal_4"
Transform653 = x3d.Transform()
Transform653.translation = [8.339,28.57,-0.9243]
Shape654 = x3d.Shape()
Appearance655 = x3d.Appearance()
Material656 = x3d.Material()
Material656.diffuseColor = [0.588,0.588,0.588]

Appearance655.material = Material656
ImageTexture657 = x3d.ImageTexture()
ImageTexture657.USE = "JinLOA3TextureAtlas"

Appearance655.texture = ImageTexture657

Shape654.appearance = Appearance655
IndexedFaceSet658 = x3d.IndexedFaceSet()
IndexedFaceSet658.coordIndex = [0,1,3,-1,3,2,0,-1,0,5,4,-1,0,2,6,-1,6,5,0,-1,2,7,6,-1,2,3,8,-1,8,7,2,-1,3,9,8,-1,3,1,10,-1,10,9,3,-1,1,11,10,-1,1,0,4,-1,4,11,1,-1,4,5,13,-1,13,12,4,-1,5,6,14,-1,14,13,5,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,4,12,-1,12,19,11,-1,12,13,21,-1,21,20,12,-1,13,14,22,-1,22,21,13,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,12,20,-1,20,27,19,-1,20,21,29,-1,29,28,20,-1,21,22,30,-1,30,29,21,-1,22,23,31,-1,31,30,22,-1,23,24,32,-1,32,31,23,-1,24,25,33,-1,33,32,24,-1,25,26,34,-1,34,33,25,-1,26,27,35,-1,35,34,26,-1,27,20,28,-1,28,35,27,-1,36,28,29,-1,36,29,30,-1,36,30,31,-1,36,31,32,-1,36,32,33,-1,36,33,34,-1,36,34,35,-1,36,35,28,-1]
IndexedFaceSet658.creaseAngle = 3.14159
IndexedFaceSet658.texCoordIndex = [0,1,2,-1,2,3,0,-1,0,4,5,-1,0,3,6,-1,6,4,0,-1,3,7,6,-1,3,2,8,-1,8,7,3,-1,2,9,8,-1,2,1,10,-1,10,9,2,-1,1,11,10,-1,1,0,5,-1,5,11,1,-1,5,4,12,-1,12,13,5,-1,4,6,14,-1,14,12,4,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,5,13,-1,13,19,11,-1,13,12,20,-1,20,21,13,-1,12,14,22,-1,22,20,12,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,13,21,-1,21,27,19,-1,21,20,28,-1,28,29,21,-1,20,22,30,-1,30,28,20,-1,22,23,31,-1,31,30,22,-1,23,24,32,-1,32,31,23,-1,24,25,33,-1,33,32,24,-1,25,26,34,-1,34,33,25,-1,26,27,35,-1,35,34,26,-1,27,21,29,-1,29,35,27,-1,36,29,28,-1,36,28,30,-1,36,30,31,-1,36,31,32,-1,36,32,33,-1,36,33,34,-1,36,34,35,-1,36,35,29,-1]
Coordinate659 = x3d.Coordinate()

IndexedFaceSet658.coord = Coordinate659
TextureCoordinate660 = x3d.TextureCoordinate()

IndexedFaceSet658.texCoord = TextureCoordinate660

Shape654.geometry = IndexedFaceSet658

Transform653.children.append(Shape654)

HAnimSegment652.children.append(Transform653)

HAnimJoint651.children.append(HAnimSegment652)
HAnimJoint661 = x3d.HAnimJoint()
HAnimJoint661.name = "l_metacarpophalangeal_4"
HAnimJoint661.DEF = "hanim_l_metacarpophalangeal_4"
HAnimJoint661.center = [8.428,27.299999,-0.9985]
HAnimJoint661.ulimit = [0,0,0]
HAnimJoint661.llimit = [0,0,0]
HAnimSegment662 = x3d.HAnimSegment()
HAnimSegment662.name = "l_carpal_proximal_phalanx_4"
HAnimSegment662.DEF = "hanim_l_carpal_proximal_phalanx_4"
Transform663 = x3d.Transform()
Transform663.translation = [8.428,27.299999,-0.9985]
Shape664 = x3d.Shape()
Appearance665 = x3d.Appearance()
Material666 = x3d.Material()
Material666.diffuseColor = [0.588,0.588,0.588]

Appearance665.material = Material666
ImageTexture667 = x3d.ImageTexture()
ImageTexture667.USE = "JinLOA3TextureAtlas"

Appearance665.texture = ImageTexture667

Shape664.appearance = Appearance665
IndexedFaceSet668 = x3d.IndexedFaceSet()
IndexedFaceSet668.coordIndex = [0,1,3,-1,3,2,0,-1,0,5,4,-1,0,2,6,-1,6,5,0,-1,2,7,6,-1,2,3,8,-1,8,7,2,-1,3,9,8,-1,3,1,10,-1,10,9,3,-1,1,11,10,-1,1,0,4,-1,4,11,1,-1,4,5,13,-1,13,12,4,-1,5,6,14,-1,14,13,5,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,4,12,-1,12,19,11,-1,12,13,21,-1,21,20,12,-1,13,14,22,-1,22,21,13,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,12,20,-1,20,27,19,-1,20,21,29,-1,29,28,20,-1,21,22,30,-1,30,29,21,-1,22,23,31,-1,31,30,22,-1,23,24,32,-1,32,31,23,-1,24,25,33,-1,33,32,24,-1,25,26,34,-1,34,33,25,-1,26,27,35,-1,35,34,26,-1,27,20,28,-1,28,35,27,-1,36,28,29,-1,36,29,30,-1,36,30,31,-1,36,31,32,-1,36,32,33,-1,36,33,34,-1,36,34,35,-1,36,35,28,-1]
IndexedFaceSet668.creaseAngle = 3.14159
IndexedFaceSet668.texCoordIndex = [0,1,2,-1,2,3,0,-1,0,4,5,-1,0,3,6,-1,6,4,0,-1,3,7,6,-1,3,2,8,-1,8,7,3,-1,2,9,8,-1,2,1,10,-1,10,9,2,-1,1,11,10,-1,1,0,5,-1,5,11,1,-1,5,4,12,-1,12,13,5,-1,4,6,14,-1,14,12,4,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,5,13,-1,13,19,11,-1,13,12,20,-1,20,21,13,-1,12,14,22,-1,22,20,12,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,13,21,-1,21,27,19,-1,21,20,28,-1,28,29,21,-1,20,22,30,-1,30,28,20,-1,22,23,31,-1,31,30,22,-1,23,24,32,-1,32,31,23,-1,24,25,33,-1,33,32,24,-1,25,26,34,-1,34,33,25,-1,26,27,35,-1,35,34,26,-1,27,21,29,-1,29,35,27,-1,36,29,28,-1,36,28,30,-1,36,30,31,-1,36,31,32,-1,36,32,33,-1,36,33,34,-1,36,34,35,-1,36,35,29,-1]
Coordinate669 = x3d.Coordinate()

IndexedFaceSet668.coord = Coordinate669
TextureCoordinate670 = x3d.TextureCoordinate()

IndexedFaceSet668.texCoord = TextureCoordinate670

Shape664.geometry = IndexedFaceSet668

Transform663.children.append(Shape664)

HAnimSegment662.children.append(Transform663)

HAnimJoint661.children.append(HAnimSegment662)
HAnimJoint671 = x3d.HAnimJoint()
HAnimJoint671.name = "l_carpal_proximal_interphalangeal_4"
HAnimJoint671.DEF = "hanim_l_carpal_proximal_interphalangeal_4"
HAnimJoint671.center = [8.428,26.290001,-1.034]
HAnimJoint671.ulimit = [0,0,0]
HAnimJoint671.llimit = [0,0,0]
HAnimSegment672 = x3d.HAnimSegment()
HAnimSegment672.name = "l_carpal_middle_phalanx_4"
HAnimSegment672.DEF = "hanim_l_carpal_middle_phalanx_4"
Transform673 = x3d.Transform()
Transform673.translation = [8.428,26.290001,-1.034]
Shape674 = x3d.Shape()
Appearance675 = x3d.Appearance()
Material676 = x3d.Material()
Material676.diffuseColor = [0.588,0.588,0.588]

Appearance675.material = Material676
ImageTexture677 = x3d.ImageTexture()
ImageTexture677.USE = "JinLOA3TextureAtlas"

Appearance675.texture = ImageTexture677

Shape674.appearance = Appearance675
IndexedFaceSet678 = x3d.IndexedFaceSet()
IndexedFaceSet678.coordIndex = [0,1,3,-1,3,2,0,-1,0,5,4,-1,0,2,6,-1,6,5,0,-1,2,7,6,-1,2,3,8,-1,8,7,2,-1,3,9,8,-1,3,1,10,-1,10,9,3,-1,1,11,10,-1,1,0,4,-1,4,11,1,-1,4,5,13,-1,13,12,4,-1,5,6,14,-1,14,13,5,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,4,12,-1,12,19,11,-1,12,13,21,-1,21,20,12,-1,13,14,22,-1,22,21,13,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,12,20,-1,20,27,19,-1,28,20,21,-1,28,21,22,-1,28,22,23,-1,28,23,24,-1,28,24,25,-1,28,25,26,-1,28,26,27,-1,28,27,20,-1]
IndexedFaceSet678.creaseAngle = 3.14159
IndexedFaceSet678.texCoordIndex = [0,1,2,-1,2,3,0,-1,0,4,5,-1,0,3,6,-1,6,4,0,-1,3,7,6,-1,3,2,8,-1,8,7,3,-1,2,9,8,-1,2,1,10,-1,10,9,2,-1,1,11,10,-1,1,0,5,-1,5,11,1,-1,5,4,12,-1,12,13,5,-1,4,6,14,-1,14,12,4,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,5,13,-1,13,19,11,-1,13,12,20,-1,20,21,13,-1,12,14,22,-1,22,20,12,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,13,21,-1,21,27,19,-1,28,21,20,-1,28,20,22,-1,28,22,23,-1,28,23,24,-1,28,24,25,-1,28,25,26,-1,28,26,27,-1,28,27,21,-1]
Coordinate679 = x3d.Coordinate()

IndexedFaceSet678.coord = Coordinate679
TextureCoordinate680 = x3d.TextureCoordinate()

IndexedFaceSet678.texCoord = TextureCoordinate680

Shape674.geometry = IndexedFaceSet678

Transform673.children.append(Shape674)

HAnimSegment672.children.append(Transform673)

HAnimJoint671.children.append(HAnimSegment672)
HAnimJoint681 = x3d.HAnimJoint()
HAnimJoint681.name = "l_carpal_distal_interphalangeal_4"
HAnimJoint681.DEF = "hanim_l_carpal_distal_interphalangeal_4"
HAnimJoint681.center = [8.192,25.309999,-1.124]
HAnimJoint681.ulimit = [0,0,0]
HAnimJoint681.llimit = [0,0,0]
HAnimSegment682 = x3d.HAnimSegment()
HAnimSegment682.name = "l_carpal_distal_phalanx_4"
HAnimSegment682.DEF = "hanim_l_carpal_distal_phalanx_4"
Transform683 = x3d.Transform()
Transform683.translation = [8.192,25.309999,-1.124]
Shape684 = x3d.Shape()
Appearance685 = x3d.Appearance()
Material686 = x3d.Material()
Material686.diffuseColor = [0.588,0.588,0.588]

Appearance685.material = Material686
ImageTexture687 = x3d.ImageTexture()
ImageTexture687.USE = "JinLOA3TextureAtlas"

Appearance685.texture = ImageTexture687

Shape684.appearance = Appearance685
IndexedFaceSet688 = x3d.IndexedFaceSet()
IndexedFaceSet688.coordIndex = [0,1,3,-1,3,2,0,-1,0,5,4,-1,0,2,6,-1,6,5,0,-1,2,7,6,-1,2,3,8,-1,8,7,2,-1,3,9,8,-1,3,1,10,-1,10,9,3,-1,1,11,10,-1,1,0,4,-1,4,11,1,-1,4,5,13,-1,13,12,4,-1,5,6,14,-1,14,13,5,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,4,12,-1,12,19,11,-1,12,13,21,-1,21,20,12,-1,13,14,22,-1,22,21,13,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,12,20,-1,20,27,19,-1,28,20,21,-1,28,21,22,-1,28,22,23,-1,28,23,24,-1,28,24,25,-1,28,25,26,-1,28,26,27,-1,28,27,20,-1]
IndexedFaceSet688.creaseAngle = 3.14159
IndexedFaceSet688.texCoordIndex = [0,1,2,-1,2,3,0,-1,0,4,5,-1,0,3,6,-1,6,4,0,-1,3,7,6,-1,3,2,8,-1,8,7,3,-1,2,9,8,-1,2,1,10,-1,10,9,2,-1,1,11,10,-1,1,0,5,-1,5,11,1,-1,5,4,12,-1,12,13,5,-1,4,6,14,-1,14,12,4,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,5,13,-1,13,19,11,-1,13,12,20,-1,20,21,13,-1,12,14,22,-1,22,20,12,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,13,21,-1,21,27,19,-1,28,21,20,-1,28,20,22,-1,28,22,23,-1,28,23,24,-1,28,24,25,-1,28,25,26,-1,28,26,27,-1,28,27,21,-1]
Coordinate689 = x3d.Coordinate()

IndexedFaceSet688.coord = Coordinate689
TextureCoordinate690 = x3d.TextureCoordinate()

IndexedFaceSet688.texCoord = TextureCoordinate690

Shape684.geometry = IndexedFaceSet688

Transform683.children.append(Shape684)

HAnimSegment682.children.append(Transform683)

HAnimJoint681.children.append(HAnimSegment682)

HAnimJoint671.children.append(HAnimJoint681)

HAnimJoint661.children.append(HAnimJoint671)

HAnimJoint651.children.append(HAnimJoint661)

HAnimJoint531.children.append(HAnimJoint651)
HAnimJoint691 = x3d.HAnimJoint()
HAnimJoint691.name = "l_carpometacarpal_5"
HAnimJoint691.DEF = "hanim_l_carpometacarpal_5"
HAnimJoint691.center = [8.197,28.370001,-1.528]
HAnimJoint691.ulimit = [0,0,0]
HAnimJoint691.llimit = [0,0,0]
HAnimSegment692 = x3d.HAnimSegment()
HAnimSegment692.name = "l_metacarpal_5"
HAnimSegment692.DEF = "hanim_l_metacarpal_5"
Transform693 = x3d.Transform()
Transform693.translation = [8.197,28.370001,-1.528]
Shape694 = x3d.Shape()
Appearance695 = x3d.Appearance()
Material696 = x3d.Material()
Material696.diffuseColor = [0.588,0.588,0.588]

Appearance695.material = Material696
ImageTexture697 = x3d.ImageTexture()
ImageTexture697.USE = "JinLOA3TextureAtlas"

Appearance695.texture = ImageTexture697

Shape694.appearance = Appearance695
IndexedFaceSet698 = x3d.IndexedFaceSet()
IndexedFaceSet698.coordIndex = [0,1,3,-1,3,2,0,-1,0,5,4,-1,0,2,6,-1,6,5,0,-1,2,7,6,-1,2,3,8,-1,8,7,2,-1,3,9,8,-1,3,1,10,-1,10,9,3,-1,1,11,10,-1,1,0,4,-1,4,11,1,-1,4,5,13,-1,13,12,4,-1,5,6,14,-1,14,13,5,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,4,12,-1,12,19,11,-1,12,13,21,-1,21,20,12,-1,13,14,22,-1,22,21,13,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,12,20,-1,20,27,19,-1,20,21,29,-1,29,28,20,-1,21,22,30,-1,30,29,21,-1,22,23,31,-1,31,30,22,-1,23,24,32,-1,32,31,23,-1,24,25,33,-1,33,32,24,-1,25,26,34,-1,34,33,25,-1,26,27,35,-1,35,34,26,-1,27,20,28,-1,28,35,27,-1,36,28,29,-1,36,29,30,-1,36,30,31,-1,36,31,32,-1,36,32,33,-1,36,33,34,-1,36,34,35,-1,36,35,28,-1]
IndexedFaceSet698.creaseAngle = 3.14159
IndexedFaceSet698.texCoordIndex = [0,1,2,-1,2,3,0,-1,0,4,5,-1,0,3,6,-1,6,4,0,-1,3,7,6,-1,3,2,8,-1,8,7,3,-1,2,9,8,-1,2,1,10,-1,10,9,2,-1,1,11,10,-1,1,0,5,-1,5,11,1,-1,5,4,12,-1,12,13,5,-1,4,6,14,-1,14,12,4,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,5,13,-1,13,19,11,-1,13,12,20,-1,20,21,13,-1,12,14,22,-1,22,20,12,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,13,21,-1,21,27,19,-1,21,20,28,-1,28,29,21,-1,20,22,30,-1,30,28,20,-1,22,23,31,-1,31,30,22,-1,23,24,32,-1,32,31,23,-1,24,25,33,-1,33,32,24,-1,25,26,34,-1,34,33,25,-1,26,27,35,-1,35,34,26,-1,27,21,29,-1,29,35,27,-1,36,29,28,-1,36,28,30,-1,36,30,31,-1,36,31,32,-1,36,32,33,-1,36,33,34,-1,36,34,35,-1,36,35,29,-1]
Coordinate699 = x3d.Coordinate()

IndexedFaceSet698.coord = Coordinate699
TextureCoordinate700 = x3d.TextureCoordinate()

IndexedFaceSet698.texCoord = TextureCoordinate700

Shape694.geometry = IndexedFaceSet698

Transform693.children.append(Shape694)

HAnimSegment692.children.append(Transform693)

HAnimJoint691.children.append(HAnimSegment692)
HAnimJoint701 = x3d.HAnimJoint()
HAnimJoint701.name = "l_metacarpophalangeal_5"
HAnimJoint701.DEF = "hanim_l_metacarpophalangeal_5"
HAnimJoint701.center = [8.334,27.5,-1.701]
HAnimJoint701.ulimit = [0,0,0]
HAnimJoint701.llimit = [0,0,0]
HAnimSegment702 = x3d.HAnimSegment()
HAnimSegment702.name = "l_carpal_proximal_phalanx_5"
HAnimSegment702.DEF = "hanim_l_carpal_proximal_phalanx_5"
Transform703 = x3d.Transform()
Transform703.translation = [8.334,27.5,-1.701]
Shape704 = x3d.Shape()
Appearance705 = x3d.Appearance()
Material706 = x3d.Material()
Material706.diffuseColor = [0.588,0.588,0.588]

Appearance705.material = Material706
ImageTexture707 = x3d.ImageTexture()
ImageTexture707.USE = "JinLOA3TextureAtlas"

Appearance705.texture = ImageTexture707

Shape704.appearance = Appearance705
IndexedFaceSet708 = x3d.IndexedFaceSet()
IndexedFaceSet708.coordIndex = [0,1,3,-1,3,2,0,-1,0,5,4,-1,0,2,6,-1,6,5,0,-1,2,7,6,-1,2,3,8,-1,8,7,2,-1,3,9,8,-1,3,1,10,-1,10,9,3,-1,1,11,10,-1,1,0,4,-1,4,11,1,-1,4,5,13,-1,13,12,4,-1,5,6,14,-1,14,13,5,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,4,12,-1,12,19,11,-1,12,13,21,-1,21,20,12,-1,13,14,22,-1,22,21,13,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,12,20,-1,20,27,19,-1,20,21,29,-1,29,28,20,-1,21,22,30,-1,30,29,21,-1,22,23,31,-1,31,30,22,-1,23,24,32,-1,32,31,23,-1,24,25,33,-1,33,32,24,-1,25,26,34,-1,34,33,25,-1,26,27,35,-1,35,34,26,-1,27,20,28,-1,28,35,27,-1,36,28,29,-1,36,29,30,-1,36,30,31,-1,36,31,32,-1,36,32,33,-1,36,33,34,-1,36,34,35,-1,36,35,28,-1]
IndexedFaceSet708.creaseAngle = 3.14159
IndexedFaceSet708.texCoordIndex = [0,1,2,-1,2,3,0,-1,0,4,5,-1,0,3,6,-1,6,4,0,-1,3,7,6,-1,3,2,8,-1,8,7,3,-1,2,9,8,-1,2,1,10,-1,10,9,2,-1,1,11,10,-1,1,0,5,-1,5,11,1,-1,5,4,12,-1,12,13,5,-1,4,6,14,-1,14,12,4,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,5,13,-1,13,19,11,-1,13,12,20,-1,20,21,13,-1,12,14,22,-1,22,20,12,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,13,21,-1,21,27,19,-1,21,20,28,-1,28,29,21,-1,20,22,30,-1,30,28,20,-1,22,23,31,-1,31,30,22,-1,23,24,32,-1,32,31,23,-1,24,25,33,-1,33,32,24,-1,25,26,34,-1,34,33,25,-1,26,27,35,-1,35,34,26,-1,27,21,29,-1,29,35,27,-1,36,29,28,-1,36,28,30,-1,36,30,31,-1,36,31,32,-1,36,32,33,-1,36,33,34,-1,36,34,35,-1,36,35,29,-1]
Coordinate709 = x3d.Coordinate()

IndexedFaceSet708.coord = Coordinate709
TextureCoordinate710 = x3d.TextureCoordinate()

IndexedFaceSet708.texCoord = TextureCoordinate710

Shape704.geometry = IndexedFaceSet708

Transform703.children.append(Shape704)

HAnimSegment702.children.append(Transform703)

HAnimJoint701.children.append(HAnimSegment702)
HAnimJoint711 = x3d.HAnimJoint()
HAnimJoint711.name = "l_carpal_proximal_interphalangeal_5"
HAnimJoint711.DEF = "hanim_l_carpal_proximal_interphalangeal_5"
HAnimJoint711.center = [8.338,26.780001,-1.768]
HAnimJoint711.ulimit = [0,0,0]
HAnimJoint711.llimit = [0,0,0]
HAnimSegment712 = x3d.HAnimSegment()
HAnimSegment712.name = "l_carpal_middle_phalanx_5"
HAnimSegment712.DEF = "hanim_l_carpal_middle_phalanx_5"
Transform713 = x3d.Transform()
Transform713.translation = [8.338,26.780001,-1.768]
Shape714 = x3d.Shape()
Appearance715 = x3d.Appearance()
Material716 = x3d.Material()
Material716.diffuseColor = [0.588,0.588,0.588]

Appearance715.material = Material716
ImageTexture717 = x3d.ImageTexture()
ImageTexture717.USE = "JinLOA3TextureAtlas"

Appearance715.texture = ImageTexture717

Shape714.appearance = Appearance715
IndexedFaceSet718 = x3d.IndexedFaceSet()
IndexedFaceSet718.coordIndex = [0,1,3,-1,3,2,0,-1,0,5,4,-1,0,2,6,-1,6,5,0,-1,2,7,6,-1,2,3,8,-1,8,7,2,-1,3,9,8,-1,3,1,10,-1,10,9,3,-1,1,11,10,-1,1,0,4,-1,4,11,1,-1,4,5,13,-1,13,12,4,-1,5,6,14,-1,14,13,5,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,4,12,-1,12,19,11,-1,12,13,21,-1,21,20,12,-1,13,14,22,-1,22,21,13,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,12,20,-1,20,27,19,-1,28,20,21,-1,28,21,22,-1,28,22,23,-1,28,23,24,-1,28,24,25,-1,28,25,26,-1,28,26,27,-1,28,27,20,-1]
IndexedFaceSet718.creaseAngle = 3.14159
IndexedFaceSet718.texCoordIndex = [0,1,2,-1,2,3,0,-1,0,4,5,-1,0,3,6,-1,6,4,0,-1,3,7,6,-1,3,2,8,-1,8,7,3,-1,2,9,8,-1,2,1,10,-1,10,9,2,-1,1,11,10,-1,1,0,5,-1,5,11,1,-1,5,4,12,-1,12,13,5,-1,4,6,14,-1,14,12,4,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,5,13,-1,13,19,11,-1,13,12,20,-1,20,21,13,-1,12,14,22,-1,22,20,12,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,13,21,-1,21,27,19,-1,28,21,20,-1,28,20,22,-1,28,22,23,-1,28,23,24,-1,28,24,25,-1,28,25,26,-1,28,26,27,-1,28,27,21,-1]
Coordinate719 = x3d.Coordinate()

IndexedFaceSet718.coord = Coordinate719
TextureCoordinate720 = x3d.TextureCoordinate()

IndexedFaceSet718.texCoord = TextureCoordinate720

Shape714.geometry = IndexedFaceSet718

Transform713.children.append(Shape714)

HAnimSegment712.children.append(Transform713)

HAnimJoint711.children.append(HAnimSegment712)
HAnimJoint721 = x3d.HAnimJoint()
HAnimJoint721.name = "l_carpal_distal_interphalangeal_5"
HAnimJoint721.DEF = "hanim_l_carpal_distal_interphalangeal_5"
HAnimJoint721.center = [8.153,26.040001,-1.886]
HAnimJoint721.ulimit = [0,0,0]
HAnimJoint721.llimit = [0,0,0]
HAnimSegment722 = x3d.HAnimSegment()
HAnimSegment722.name = "l_carpal_distal_phalanx_5"
HAnimSegment722.DEF = "hanim_l_carpal_distal_phalanx_5"
Transform723 = x3d.Transform()
Transform723.translation = [8.153,26.040001,-1.886]
Shape724 = x3d.Shape()
Appearance725 = x3d.Appearance()
Material726 = x3d.Material()
Material726.diffuseColor = [0.588,0.588,0.588]

Appearance725.material = Material726
ImageTexture727 = x3d.ImageTexture()
ImageTexture727.USE = "JinLOA3TextureAtlas"

Appearance725.texture = ImageTexture727

Shape724.appearance = Appearance725
IndexedFaceSet728 = x3d.IndexedFaceSet()
IndexedFaceSet728.coordIndex = [0,1,3,-1,3,2,0,-1,0,5,4,-1,0,2,6,-1,6,5,0,-1,2,7,6,-1,2,3,8,-1,8,7,2,-1,3,9,8,-1,3,1,10,-1,10,9,3,-1,1,11,10,-1,1,0,4,-1,4,11,1,-1,4,5,13,-1,13,12,4,-1,5,6,14,-1,14,13,5,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,4,12,-1,12,19,11,-1,12,13,21,-1,21,20,12,-1,13,14,22,-1,22,21,13,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,12,20,-1,20,27,19,-1,28,20,21,-1,28,21,22,-1,28,22,23,-1,28,23,24,-1,28,24,25,-1,28,25,26,-1,28,26,27,-1,28,27,20,-1]
IndexedFaceSet728.creaseAngle = 3.14159
IndexedFaceSet728.texCoordIndex = [0,1,2,-1,2,3,0,-1,0,4,5,-1,0,3,6,-1,6,4,0,-1,3,7,6,-1,3,2,8,-1,8,7,3,-1,2,9,8,-1,2,1,10,-1,10,9,2,-1,1,11,10,-1,1,0,5,-1,5,11,1,-1,5,4,12,-1,12,13,5,-1,4,6,14,-1,14,12,4,-1,6,7,15,-1,15,14,6,-1,7,8,16,-1,16,15,7,-1,8,9,17,-1,17,16,8,-1,9,10,18,-1,18,17,9,-1,10,11,19,-1,19,18,10,-1,11,5,13,-1,13,19,11,-1,13,12,20,-1,20,21,13,-1,12,14,22,-1,22,20,12,-1,14,15,23,-1,23,22,14,-1,15,16,24,-1,24,23,15,-1,16,17,25,-1,25,24,16,-1,17,18,26,-1,26,25,17,-1,18,19,27,-1,27,26,18,-1,19,13,21,-1,21,27,19,-1,28,21,20,-1,28,20,22,-1,28,22,23,-1,28,23,24,-1,28,24,25,-1,28,25,26,-1,28,26,27,-1,28,27,21,-1]
Coordinate729 = x3d.Coordinate()

IndexedFaceSet728.coord = Coordinate729
TextureCoordinate730 = x3d.TextureCoordinate()

IndexedFaceSet728.texCoord = TextureCoordinate730

Shape724.geometry = IndexedFaceSet728

Transform723.children.append(Shape724)

HAnimSegment722.children.append(Transform723)

HAnimJoint721.children.append(HAnimSegment722)

HAnimJoint711.children.append(HAnimJoint721)

HAnimJoint701.children.append(HAnimJoint711)

HAnimJoint691.children.append(HAnimJoint701)

HAnimJoint531.children.append(HAnimJoint691)

HAnimJoint521.children.append(HAnimJoint531)

HAnimJoint511.children.append(HAnimJoint521)

HAnimJoint501.children.append(HAnimJoint511)

HAnimJoint491.children.append(HAnimJoint501)

HAnimJoint331.children.append(HAnimJoint491)
HAnimJoint731 = x3d.HAnimJoint()
HAnimJoint731.name = "r_sternoclavicular"
HAnimJoint731.DEF = "hanim_r_sternoclavicular"
HAnimJoint731.center = [-1.71,52.82,-0.6127]
HAnimJoint731.ulimit = [0,0,0]
HAnimJoint731.llimit = [0,0,0]
HAnimSegment732 = x3d.HAnimSegment()
HAnimSegment732.name = "r_clavicle"
HAnimSegment732.DEF = "hanim_r_clavicle"
Transform733 = x3d.Transform()
Transform733.translation = [-1.71,52.82,-0.6127]
Shape734 = x3d.Shape()
Appearance735 = x3d.Appearance()
Material736 = x3d.Material()
Material736.diffuseColor = [0.588,0.588,0.588]

Appearance735.material = Material736
ImageTexture737 = x3d.ImageTexture()
ImageTexture737.USE = "JinLOA3TextureAtlas"

Appearance735.texture = ImageTexture737

Shape734.appearance = Appearance735
IndexedFaceSet738 = x3d.IndexedFaceSet()
IndexedFaceSet738.coordIndex = [9,0,1,-1,1,6,9,-1,6,1,2,-1,2,5,6,-1,8,5,2,-1,2,3,8,-1,8,3,4,-1,4,7,8,-1,9,7,4,-1,4,0,9,-1,4,3,2,-1,0,4,2,-1,1,0,2,-1,10,14,13,-1,10,13,12,-1,11,10,12,-1,6,10,11,-1,11,9,6,-1,9,11,12,-1,12,7,9,-1,7,12,13,-1,13,8,7,-1,8,13,14,-1,14,5,8,-1,5,14,10,-1,10,6,5,-1]
IndexedFaceSet738.creaseAngle = 3.14159
IndexedFaceSet738.texCoordIndex = [9,0,1,-1,1,6,9,-1,6,1,2,-1,2,5,6,-1,8,5,2,-1,2,3,8,-1,8,3,4,-1,4,7,8,-1,9,7,4,-1,4,0,9,-1,4,3,2,-1,0,4,2,-1,1,0,2,-1,10,14,13,-1,10,13,12,-1,11,10,12,-1,6,10,11,-1,11,9,6,-1,9,11,12,-1,12,7,9,-1,7,12,13,-1,13,8,7,-1,8,13,14,-1,14,5,8,-1,5,14,10,-1,10,6,5,-1]
Coordinate739 = x3d.Coordinate()

IndexedFaceSet738.coord = Coordinate739
TextureCoordinate740 = x3d.TextureCoordinate()

IndexedFaceSet738.texCoord = TextureCoordinate740

Shape734.geometry = IndexedFaceSet738

Transform733.children.append(Shape734)

HAnimSegment732.children.append(Transform733)

HAnimJoint731.children.append(HAnimSegment732)
HAnimJoint741 = x3d.HAnimJoint()
HAnimJoint741.name = "r_acromioclavicular"
HAnimJoint741.DEF = "hanim_r_acromioclavicular"
HAnimJoint741.center = [-5.464,52.060001,-0.5732]
HAnimJoint741.ulimit = [0,0,0]
HAnimJoint741.llimit = [0,0,0]
HAnimSegment742 = x3d.HAnimSegment()
HAnimSegment742.name = "r_scapula"
HAnimSegment742.DEF = "hanim_r_scapula"
Transform743 = x3d.Transform()
Transform743.translation = [-5.464,52.060001,-0.5732]
Shape744 = x3d.Shape()
Appearance745 = x3d.Appearance()
Material746 = x3d.Material()
Material746.diffuseColor = [0.588,0.588,0.588]

Appearance745.material = Material746
ImageTexture747 = x3d.ImageTexture()
ImageTexture747.USE = "JinLOA3TextureAtlas"

Appearance745.texture = ImageTexture747

Shape744.appearance = Appearance745
IndexedFaceSet748 = x3d.IndexedFaceSet()
IndexedFaceSet748.coordIndex = [5,1,0,-1,0,4,5,-1,4,0,2,-1,2,3,4,-1,3,2,6,-1,6,9,3,-1,7,8,1,-1,1,5,7,-1,6,2,0,-1,0,8,6,-1,0,1,8,-1,9,6,8,-1,8,7,9,-1,4,10,11,-1,11,5,4,-1,5,11,12,-1,12,7,5,-1,7,12,13,-1,13,9,7,-1,9,13,14,-1,14,3,9,-1,3,14,10,-1,10,4,3,-1,10,15,11,-1,11,15,12,-1,12,15,13,-1,13,15,14,-1,14,15,10,-1]
IndexedFaceSet748.creaseAngle = 3.14159
IndexedFaceSet748.texCoordIndex = [5,1,0,-1,0,4,5,-1,4,0,2,-1,2,3,4,-1,3,2,6,-1,6,8,3,-1,9,7,1,-1,1,5,9,-1,6,2,0,-1,0,7,6,-1,0,1,7,-1,12,10,11,-1,11,13,12,-1,4,14,15,-1,15,5,4,-1,5,15,16,-1,16,9,5,-1,13,16,17,-1,17,12,13,-1,8,17,18,-1,18,3,8,-1,3,18,14,-1,14,4,3,-1,14,19,15,-1,15,19,16,-1,16,19,17,-1,17,19,18,-1,18,19,14,-1]
Coordinate749 = x3d.Coordinate()

IndexedFaceSet748.coord = Coordinate749
TextureCoordinate750 = x3d.TextureCoordinate()

IndexedFaceSet748.texCoord = TextureCoordinate750

Shape744.geometry = IndexedFaceSet748

Transform743.children.append(Shape744)

HAnimSegment742.children.append(Transform743)

HAnimJoint741.children.append(HAnimSegment742)
HAnimJoint751 = x3d.HAnimJoint()
HAnimJoint751.name = "r_shoulder"
HAnimJoint751.DEF = "hanim_r_shoulder"
HAnimJoint751.center = [-7.336,51.48,-0.1452]
HAnimJoint751.ulimit = [0,0,0]
HAnimJoint751.llimit = [0,0,0]
HAnimSegment752 = x3d.HAnimSegment()
HAnimSegment752.name = "r_upperarm"
HAnimSegment752.DEF = "hanim_r_upperarm"
Transform753 = x3d.Transform()
Transform753.translation = [-7.336,51.48,-0.1452]
Shape754 = x3d.Shape()
Appearance755 = x3d.Appearance()
Material756 = x3d.Material()
Material756.diffuseColor = [0.588,0.588,0.588]

Appearance755.material = Material756
ImageTexture757 = x3d.ImageTexture()
ImageTexture757.USE = "JinLOA3TextureAtlas"

Appearance755.texture = ImageTexture757

Shape754.appearance = Appearance755
IndexedFaceSet758 = x3d.IndexedFaceSet()
IndexedFaceSet758.coordIndex = [0,1,2,-1,0,2,3,-1,4,0,3,-1,0,5,6,-1,6,1,0,-1,1,6,7,-1,7,2,1,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,9,4,3,-1,4,9,5,-1,5,0,4,-1,5,10,11,-1,11,6,5,-1,6,11,12,-1,12,7,6,-1,7,12,13,-1,13,8,7,-1,8,13,14,-1,14,9,8,-1,9,14,10,-1,10,5,9,-1,10,15,16,-1,16,11,10,-1,11,16,17,-1,17,12,11,-1,12,17,18,-1,18,13,12,-1,13,18,19,-1,19,14,13,-1,14,19,15,-1,15,10,14,-1,38,37,36,-1,38,36,35,-1,39,38,35,-1,21,16,15,-1,15,20,21,-1,22,17,16,-1,16,21,22,-1,23,18,17,-1,17,22,23,-1,24,19,18,-1,18,23,24,-1,20,15,19,-1,19,24,20,-1,26,21,20,-1,20,25,26,-1,27,22,21,-1,21,26,27,-1,28,23,22,-1,22,27,28,-1,29,24,23,-1,23,28,29,-1,25,20,24,-1,24,29,25,-1,31,26,25,-1,25,30,31,-1,32,27,26,-1,26,31,32,-1,33,28,27,-1,27,32,33,-1,34,29,28,-1,28,33,34,-1,30,25,29,-1,29,34,30,-1,36,31,30,-1,30,35,36,-1,37,32,31,-1,31,36,37,-1,38,33,32,-1,32,37,38,-1,39,34,33,-1,33,38,39,-1,35,30,34,-1,34,39,35,-1]
IndexedFaceSet758.creaseAngle = 3.14159
IndexedFaceSet758.texCoordIndex = [1,0,2,-1,1,2,3,-1,61,1,3,-1,1,6,5,-1,5,0,1,-1,0,5,7,-1,7,2,0,-1,2,7,8,-1,8,3,2,-1,25,26,9,-1,9,4,25,-1,4,9,6,-1,6,1,4,-1,6,11,10,-1,10,5,6,-1,5,10,12,-1,12,7,5,-1,7,12,13,-1,13,8,7,-1,27,28,14,-1,14,9,27,-1,9,14,11,-1,11,6,9,-1,11,16,15,-1,15,10,11,-1,10,15,17,-1,17,12,10,-1,12,17,18,-1,18,13,12,-1,29,30,19,-1,19,14,29,-1,14,19,16,-1,16,11,14,-1,36,35,54,-1,36,54,53,-1,37,36,53,-1,20,15,16,-1,16,21,20,-1,22,17,15,-1,15,20,22,-1,23,18,17,-1,17,22,23,-1,24,19,31,-1,31,32,24,-1,21,16,19,-1,19,24,21,-1,40,39,38,-1,38,41,40,-1,43,42,55,-1,55,56,43,-1,45,44,42,-1,42,43,45,-1,47,46,44,-1,44,45,47,-1,41,38,46,-1,46,47,41,-1,48,40,41,-1,41,49,48,-1,50,43,57,-1,57,58,50,-1,51,45,43,-1,43,50,51,-1,52,47,45,-1,45,51,52,-1,49,41,47,-1,47,52,49,-1,34,48,49,-1,49,33,34,-1,35,50,59,-1,59,60,35,-1,36,51,50,-1,50,35,36,-1,37,52,51,-1,51,36,37,-1,33,49,52,-1,52,37,33,-1]
Coordinate759 = x3d.Coordinate()

IndexedFaceSet758.coord = Coordinate759
TextureCoordinate760 = x3d.TextureCoordinate()

IndexedFaceSet758.texCoord = TextureCoordinate760

Shape754.geometry = IndexedFaceSet758

Transform753.children.append(Shape754)

HAnimSegment752.children.append(Transform753)

HAnimJoint751.children.append(HAnimSegment752)
HAnimJoint761 = x3d.HAnimJoint()
HAnimJoint761.name = "r_elbow"
HAnimJoint761.DEF = "hanim_r_elbow"
HAnimJoint761.center = [-8.093,40.380001,-0.2502]
HAnimJoint761.ulimit = [0,0,0]
HAnimJoint761.llimit = [0,0,0]
HAnimSegment762 = x3d.HAnimSegment()
HAnimSegment762.name = "r_forearm"
HAnimSegment762.DEF = "hanim_r_forearm"
Transform763 = x3d.Transform()
Transform763.translation = [-8.093,40.380001,-0.2502]
Shape764 = x3d.Shape()
Appearance765 = x3d.Appearance()
Material766 = x3d.Material()
Material766.diffuseColor = [0.588,0.588,0.588]

Appearance765.material = Material766
ImageTexture767 = x3d.ImageTexture()
ImageTexture767.USE = "JinLOA3TextureAtlas"

Appearance765.texture = ImageTexture767

Shape764.appearance = Appearance765
IndexedFaceSet768 = x3d.IndexedFaceSet()
IndexedFaceSet768.coordIndex = [0,1,2,-1,0,2,3,-1,4,0,3,-1,0,5,6,-1,6,1,0,-1,1,6,7,-1,7,2,1,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,9,4,3,-1,4,9,5,-1,5,0,4,-1,5,10,11,-1,11,6,5,-1,6,11,12,-1,12,7,6,-1,7,12,13,-1,13,8,7,-1,8,13,14,-1,14,9,8,-1,9,14,10,-1,10,5,9,-1,10,15,16,-1,16,11,10,-1,11,16,17,-1,17,12,11,-1,12,17,18,-1,18,13,12,-1,13,18,19,-1,19,14,13,-1,14,19,15,-1,15,10,14,-1,23,22,21,-1,23,21,20,-1,24,23,20,-1,21,16,15,-1,15,20,21,-1,22,17,16,-1,16,21,22,-1,23,18,17,-1,17,22,23,-1,24,19,18,-1,18,23,24,-1,20,15,19,-1,19,24,20,-1]
IndexedFaceSet768.creaseAngle = 3.14159
IndexedFaceSet768.texCoordIndex = [26,25,2,-1,26,2,3,-1,4,26,3,-1,0,5,6,-1,6,1,0,-1,27,28,7,-1,7,2,27,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,9,4,3,-1,4,9,5,-1,5,0,4,-1,5,10,11,-1,11,6,5,-1,29,30,12,-1,12,7,29,-1,7,12,13,-1,13,8,7,-1,8,13,14,-1,14,9,8,-1,9,14,10,-1,10,5,9,-1,10,15,16,-1,16,11,10,-1,31,32,17,-1,17,12,31,-1,12,17,18,-1,18,13,12,-1,13,18,19,-1,19,14,13,-1,14,19,15,-1,15,10,14,-1,23,22,34,-1,23,34,33,-1,24,23,33,-1,21,16,15,-1,15,20,21,-1,22,17,35,-1,35,36,22,-1,23,18,17,-1,17,22,23,-1,24,19,18,-1,18,23,24,-1,20,15,19,-1,19,24,20,-1]
Coordinate769 = x3d.Coordinate()

IndexedFaceSet768.coord = Coordinate769
TextureCoordinate770 = x3d.TextureCoordinate()

IndexedFaceSet768.texCoord = TextureCoordinate770

Shape764.geometry = IndexedFaceSet768

Transform763.children.append(Shape764)

HAnimSegment762.children.append(Transform763)

HAnimJoint761.children.append(HAnimSegment762)
HAnimJoint771 = x3d.HAnimJoint()
HAnimJoint771.name = "r_radiocarpal"
HAnimJoint771.DEF = "hanim_r_radiocarpal"
HAnimJoint771.center = [-7.899,31.43,-0.3809]
HAnimJoint771.ulimit = [0,0,0]
HAnimJoint771.llimit = [0,0,0]
HAnimSegment772 = x3d.HAnimSegment()
HAnimSegment772.name = "r_carpal"
HAnimSegment772.DEF = "hanim_r_carpal"
Transform773 = x3d.Transform()
Transform773.translation = [-7.899,31.43,-0.3809]
Shape774 = x3d.Shape()
Appearance775 = x3d.Appearance()
Material776 = x3d.Material()
Material776.diffuseColor = [0.588,0.588,0.588]

Appearance775.material = Material776
ImageTexture777 = x3d.ImageTexture()
ImageTexture777.USE = "JinLOA3TextureAtlas"

Appearance775.texture = ImageTexture777

Shape774.appearance = Appearance775
IndexedFaceSet778 = x3d.IndexedFaceSet()
IndexedFaceSet778.coordIndex = [36,41,38,-1,38,37,36,-1,44,54,45,-1,31,30,53,-1,53,4,31,-1,6,7,11,-1,11,10,6,-1,11,32,33,-1,33,10,11,-1,34,11,7,-1,7,24,34,-1,13,27,15,-1,15,17,13,-1,25,35,22,-1,30,20,5,-1,13,32,11,-1,11,34,13,-1,23,29,28,-1,28,22,23,-1,17,15,14,-1,14,16,17,-1,18,19,53,-1,53,5,18,-1,9,17,16,-1,16,8,9,-1,14,15,43,-1,43,42,14,-1,21,33,8,-1,8,16,21,-1,21,23,22,-1,22,35,21,-1,39,38,41,-1,41,40,39,-1,26,24,20,-1,27,26,20,-1,20,12,27,-1,3,43,12,-1,12,30,3,-1,0,25,28,-1,28,54,0,-1,13,17,9,-1,9,32,13,-1,28,29,31,-1,29,23,14,-1,14,42,29,-1,16,14,23,-1,23,21,16,-1,30,31,2,-1,2,3,30,-1,8,33,32,-1,32,9,8,-1,33,21,35,-1,35,10,33,-1,35,25,6,-1,6,10,35,-1,13,34,26,-1,26,27,13,-1,34,24,26,-1,1,46,47,-1,47,0,1,-1,25,0,47,-1,47,48,25,-1,25,48,49,-1,49,6,25,-1,6,49,50,-1,50,7,6,-1,24,7,50,-1,50,51,24,-1,24,51,46,-1,46,1,24,-1,2,42,43,-1,43,3,2,-1,15,27,12,-1,12,43,15,-1,29,42,2,-1,2,31,29,-1,18,5,52,-1,52,44,18,-1,28,25,22,-1,18,44,45,-1,45,19,18,-1,1,44,52,-1,52,24,1,-1,45,28,4,-1,28,31,4,-1,45,4,19,-1,37,47,46,-1,46,36,37,-1,48,47,37,-1,37,38,48,-1,39,49,48,-1,48,38,39,-1,40,50,49,-1,49,39,40,-1,51,50,40,-1,40,41,51,-1,36,46,51,-1,51,41,36,-1,24,52,20,-1,52,5,20,-1,53,30,5,-1,53,19,4,-1,54,28,45,-1,44,1,0,-1,0,54,44,-1,20,30,12,-1]
IndexedFaceSet778.creaseAngle = 3.14159
IndexedFaceSet778.texCoordIndex = [0,3,2,-1,2,1,0,-1,4,6,5,-1,8,7,10,-1,10,9,8,-1,12,11,14,-1,14,13,12,-1,14,16,15,-1,15,13,14,-1,17,14,11,-1,11,18,17,-1,20,19,22,-1,22,21,20,-1,23,25,24,-1,7,27,26,-1,20,16,14,-1,14,17,20,-1,28,30,29,-1,29,24,28,-1,21,22,32,-1,32,31,21,-1,33,34,10,-1,10,26,33,-1,35,21,31,-1,31,36,35,-1,32,22,38,-1,38,37,32,-1,39,15,36,-1,36,31,39,-1,39,28,24,-1,24,25,39,-1,40,2,3,-1,3,41,40,-1,42,18,27,-1,19,42,27,-1,27,43,19,-1,44,38,43,-1,43,7,44,-1,45,23,29,-1,29,6,45,-1,20,21,35,-1,35,16,20,-1,29,30,8,-1,30,28,32,-1,32,37,30,-1,31,32,28,-1,28,39,31,-1,7,8,46,-1,46,44,7,-1,36,15,16,-1,16,35,36,-1,15,39,25,-1,25,13,15,-1,25,23,12,-1,12,13,25,-1,20,17,42,-1,42,19,20,-1,17,18,42,-1,47,49,48,-1,48,45,47,-1,23,45,48,-1,48,50,23,-1,23,50,51,-1,51,12,23,-1,12,51,52,-1,52,11,12,-1,18,11,52,-1,52,53,18,-1,18,53,49,-1,49,47,18,-1,46,37,38,-1,38,44,46,-1,22,19,43,-1,43,38,22,-1,30,37,46,-1,46,8,30,-1,33,26,54,-1,54,4,33,-1,29,23,24,-1,33,4,5,-1,5,34,33,-1,47,4,54,-1,54,18,47,-1,5,29,9,-1,29,8,9,-1,5,9,34,-1,1,48,49,-1,49,0,1,-1,50,48,1,-1,1,2,50,-1,40,51,50,-1,50,2,40,-1,41,52,51,-1,51,40,41,-1,53,52,41,-1,41,3,53,-1,0,49,53,-1,53,3,0,-1,18,54,27,-1,54,26,27,-1,10,7,26,-1,10,34,9,-1,6,29,5,-1,4,47,45,-1,45,6,4,-1,27,7,43,-1]
Coordinate779 = x3d.Coordinate()

IndexedFaceSet778.coord = Coordinate779
TextureCoordinate780 = x3d.TextureCoordinate()

IndexedFaceSet778.texCoord = TextureCoordinate780

Shape774.geometry = IndexedFaceSet778

Transform773.children.append(Shape774)

HAnimSegment772.children.append(Transform773)

HAnimJoint771.children.append(HAnimSegment772)
HAnimJoint781 = x3d.HAnimJoint()
HAnimJoint781.name = "r_carpometacarpal_1"
HAnimJoint781.DEF = "hanim_r_carpometacarpal_1"
HAnimJoint781.center = [-8.205,29.6,1.302]
HAnimJoint781.ulimit = [0,0,0]
HAnimJoint781.llimit = [0,0,0]
HAnimSegment782 = x3d.HAnimSegment()
HAnimSegment782.name = "r_metacarpal_1"
HAnimSegment782.DEF = "hanim_r_metacarpal_1"
Transform783 = x3d.Transform()
Transform783.translation = [-8.205,29.6,1.302]
Shape784 = x3d.Shape()
Appearance785 = x3d.Appearance()
Material786 = x3d.Material()
Material786.diffuseColor = [0.588,0.588,0.588]

Appearance785.material = Material786
ImageTexture787 = x3d.ImageTexture()
ImageTexture787.USE = "JinLOA3TextureAtlas"

Appearance785.texture = ImageTexture787

Shape784.appearance = Appearance785
IndexedFaceSet788 = x3d.IndexedFaceSet()
IndexedFaceSet788.coordIndex = [0,2,3,-1,3,1,0,-1,0,4,5,-1,0,5,6,-1,6,2,0,-1,2,6,7,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,3,9,10,-1,10,1,3,-1,1,10,11,-1,1,11,4,-1,4,0,1,-1,4,12,13,-1,13,5,4,-1,5,13,14,-1,14,6,5,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,12,-1,12,4,11,-1,12,20,21,-1,21,13,12,-1,13,21,22,-1,22,14,13,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,20,-1,20,12,19,-1,20,28,29,-1,29,21,20,-1,21,29,30,-1,30,22,21,-1,22,30,31,-1,31,23,22,-1,23,31,32,-1,32,24,23,-1,24,32,33,-1,33,25,24,-1,25,33,34,-1,34,26,25,-1,26,34,35,-1,35,27,26,-1,27,35,28,-1,28,20,27,-1,36,29,28,-1,36,30,29,-1,36,31,30,-1,36,32,31,-1,36,33,32,-1,36,34,33,-1,36,35,34,-1,36,28,35,-1]
IndexedFaceSet788.creaseAngle = 3.14159
IndexedFaceSet788.texCoordIndex = [0,3,2,-1,2,1,0,-1,0,5,4,-1,0,4,6,-1,6,3,0,-1,3,6,7,-1,3,7,8,-1,8,2,3,-1,2,8,9,-1,2,9,10,-1,10,1,2,-1,1,10,11,-1,1,11,5,-1,5,0,1,-1,5,13,12,-1,12,4,5,-1,4,12,14,-1,14,6,4,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,13,-1,13,5,11,-1,13,21,20,-1,20,12,13,-1,12,20,22,-1,22,14,12,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,21,-1,21,13,19,-1,21,29,28,-1,28,20,21,-1,20,28,30,-1,30,22,20,-1,22,30,31,-1,31,23,22,-1,23,31,32,-1,32,24,23,-1,24,32,33,-1,33,25,24,-1,25,33,34,-1,34,26,25,-1,26,34,35,-1,35,27,26,-1,27,35,29,-1,29,21,27,-1,36,28,29,-1,36,30,28,-1,36,31,30,-1,36,32,31,-1,36,33,32,-1,36,34,33,-1,36,35,34,-1,36,29,35,-1]
Coordinate789 = x3d.Coordinate()

IndexedFaceSet788.coord = Coordinate789
TextureCoordinate790 = x3d.TextureCoordinate()

IndexedFaceSet788.texCoord = TextureCoordinate790

Shape784.geometry = IndexedFaceSet788

Transform783.children.append(Shape784)

HAnimSegment782.children.append(Transform783)

HAnimJoint781.children.append(HAnimSegment782)
HAnimJoint791 = x3d.HAnimJoint()
HAnimJoint791.name = "r_metacarpophalangeal_1"
HAnimJoint791.DEF = "hanim_r_metacarpophalangeal_1"
HAnimJoint791.center = [-8.08,28.73,1.55]
HAnimJoint791.ulimit = [0,0,0]
HAnimJoint791.llimit = [0,0,0]
HAnimSegment792 = x3d.HAnimSegment()
HAnimSegment792.name = "r_carpal_proximal_phalanx_1"
HAnimSegment792.DEF = "hanim_r_carpal_proximal_phalanx_1"
Transform793 = x3d.Transform()
Transform793.translation = [-8.08,28.73,1.55]
Shape794 = x3d.Shape()
Appearance795 = x3d.Appearance()
Material796 = x3d.Material()
Material796.diffuseColor = [0.588,0.588,0.588]

Appearance795.material = Material796
ImageTexture797 = x3d.ImageTexture()
ImageTexture797.USE = "JinLOA3TextureAtlas"

Appearance795.texture = ImageTexture797

Shape794.appearance = Appearance795
IndexedFaceSet798 = x3d.IndexedFaceSet()
IndexedFaceSet798.coordIndex = [0,2,3,-1,3,1,0,-1,0,4,5,-1,0,5,6,-1,6,2,0,-1,2,6,7,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,3,9,10,-1,10,1,3,-1,1,10,11,-1,1,11,4,-1,4,0,1,-1,4,12,13,-1,13,5,4,-1,5,13,14,-1,14,6,5,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,12,-1,12,4,11,-1,12,20,21,-1,21,13,12,-1,13,21,22,-1,22,14,13,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,20,-1,20,12,19,-1,20,28,29,-1,29,21,20,-1,21,29,30,-1,30,22,21,-1,22,30,31,-1,31,23,22,-1,23,31,32,-1,32,24,23,-1,24,32,33,-1,33,25,24,-1,25,33,34,-1,34,26,25,-1,26,34,35,-1,35,27,26,-1,27,35,28,-1,28,20,27,-1,36,29,28,-1,36,30,29,-1,36,31,30,-1,36,32,31,-1,36,33,32,-1,36,34,33,-1,36,35,34,-1,36,28,35,-1]
IndexedFaceSet798.creaseAngle = 3.14159
IndexedFaceSet798.texCoordIndex = [0,3,2,-1,2,1,0,-1,0,5,4,-1,0,4,6,-1,6,3,0,-1,3,6,7,-1,3,7,8,-1,8,2,3,-1,2,8,9,-1,2,9,10,-1,10,1,2,-1,1,10,11,-1,1,11,5,-1,5,0,1,-1,5,13,12,-1,12,4,5,-1,4,12,14,-1,14,6,4,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,13,-1,13,5,11,-1,13,21,20,-1,20,12,13,-1,12,20,22,-1,22,14,12,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,21,-1,21,13,19,-1,21,29,28,-1,28,20,21,-1,20,28,30,-1,30,22,20,-1,22,30,31,-1,31,23,22,-1,23,31,32,-1,32,24,23,-1,24,32,33,-1,33,25,24,-1,25,33,34,-1,34,26,25,-1,26,34,35,-1,35,27,26,-1,27,35,29,-1,29,21,27,-1,36,28,29,-1,36,30,28,-1,36,31,30,-1,36,32,31,-1,36,33,32,-1,36,34,33,-1,36,35,34,-1,36,29,35,-1]
Coordinate799 = x3d.Coordinate()

IndexedFaceSet798.coord = Coordinate799
TextureCoordinate800 = x3d.TextureCoordinate()

IndexedFaceSet798.texCoord = TextureCoordinate800

Shape794.geometry = IndexedFaceSet798

Transform793.children.append(Shape794)

HAnimSegment792.children.append(Transform793)

HAnimJoint791.children.append(HAnimSegment792)
HAnimJoint801 = x3d.HAnimJoint()
HAnimJoint801.name = "r_carpal_interphalangeal_1"
HAnimJoint801.DEF = "hanim_r_carpal_interphalangeal_1"
HAnimJoint801.center = [-7.832,27.85,1.735]
HAnimJoint801.ulimit = [0,0,0]
HAnimJoint801.llimit = [0,0,0]
HAnimSegment802 = x3d.HAnimSegment()
HAnimSegment802.name = "r_carpal_distal_phalanx_1"
HAnimSegment802.DEF = "hanim_r_carpal_distal_phalanx_1"
Transform803 = x3d.Transform()
Transform803.translation = [-7.832,27.85,1.735]
Shape804 = x3d.Shape()
Appearance805 = x3d.Appearance()
Material806 = x3d.Material()
Material806.diffuseColor = [0.588,0.588,0.588]

Appearance805.material = Material806
ImageTexture807 = x3d.ImageTexture()
ImageTexture807.USE = "JinLOA3TextureAtlas"

Appearance805.texture = ImageTexture807

Shape804.appearance = Appearance805
IndexedFaceSet808 = x3d.IndexedFaceSet()
IndexedFaceSet808.coordIndex = [0,2,3,-1,3,1,0,-1,0,4,5,-1,0,5,6,-1,6,2,0,-1,2,6,7,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,3,9,10,-1,10,1,3,-1,1,10,11,-1,1,11,4,-1,4,0,1,-1,4,12,13,-1,13,5,4,-1,5,13,14,-1,14,6,5,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,12,-1,12,4,11,-1,12,20,21,-1,21,13,12,-1,13,21,22,-1,22,14,13,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,20,-1,20,12,19,-1,28,21,20,-1,28,22,21,-1,28,23,22,-1,28,24,23,-1,28,25,24,-1,28,26,25,-1,28,27,26,-1,28,20,27,-1]
IndexedFaceSet808.creaseAngle = 3.14159
IndexedFaceSet808.texCoordIndex = [0,3,2,-1,2,1,0,-1,0,5,4,-1,0,4,6,-1,6,3,0,-1,3,6,7,-1,3,7,8,-1,8,2,3,-1,2,8,9,-1,2,9,10,-1,10,1,2,-1,1,10,11,-1,1,11,5,-1,5,0,1,-1,5,13,12,-1,12,4,5,-1,4,12,14,-1,14,6,4,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,13,-1,13,5,11,-1,13,21,20,-1,20,12,13,-1,12,20,22,-1,22,14,12,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,21,-1,21,13,19,-1,28,20,21,-1,28,22,20,-1,28,23,22,-1,28,24,23,-1,28,25,24,-1,28,26,25,-1,28,27,26,-1,28,21,27,-1]
Coordinate809 = x3d.Coordinate()

IndexedFaceSet808.coord = Coordinate809
TextureCoordinate810 = x3d.TextureCoordinate()

IndexedFaceSet808.texCoord = TextureCoordinate810

Shape804.geometry = IndexedFaceSet808

Transform803.children.append(Shape804)

HAnimSegment802.children.append(Transform803)

HAnimJoint801.children.append(HAnimSegment802)

HAnimJoint791.children.append(HAnimJoint801)

HAnimJoint781.children.append(HAnimJoint791)

HAnimJoint771.children.append(HAnimJoint781)
HAnimJoint811 = x3d.HAnimJoint()
HAnimJoint811.name = "r_carpometacarpal_2"
HAnimJoint811.DEF = "hanim_r_carpometacarpal_2"
HAnimJoint811.center = [-8.376,28.549999,0.5997]
HAnimJoint811.ulimit = [0,0,0]
HAnimJoint811.llimit = [0,0,0]
HAnimSegment812 = x3d.HAnimSegment()
HAnimSegment812.name = "r_metacarpal_2"
HAnimSegment812.DEF = "hanim_r_metacarpal_2"
Transform813 = x3d.Transform()
Transform813.translation = [-8.376,28.549999,0.5997]
Shape814 = x3d.Shape()
Appearance815 = x3d.Appearance()
Material816 = x3d.Material()
Material816.diffuseColor = [0.588,0.588,0.588]

Appearance815.material = Material816
ImageTexture817 = x3d.ImageTexture()
ImageTexture817.USE = "JinLOA3TextureAtlas"

Appearance815.texture = ImageTexture817

Shape814.appearance = Appearance815
IndexedFaceSet818 = x3d.IndexedFaceSet()
IndexedFaceSet818.coordIndex = [0,2,3,-1,3,1,0,-1,0,4,5,-1,0,5,6,-1,6,2,0,-1,2,6,7,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,3,9,10,-1,10,1,3,-1,1,10,11,-1,1,11,4,-1,4,0,1,-1,4,12,13,-1,13,5,4,-1,5,13,14,-1,14,6,5,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,12,-1,12,4,11,-1,12,20,21,-1,21,13,12,-1,13,21,22,-1,22,14,13,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,20,-1,20,12,19,-1,20,28,29,-1,29,21,20,-1,21,29,30,-1,30,22,21,-1,22,30,31,-1,31,23,22,-1,23,31,32,-1,32,24,23,-1,24,32,33,-1,33,25,24,-1,25,33,34,-1,34,26,25,-1,26,34,35,-1,35,27,26,-1,27,35,28,-1,28,20,27,-1,36,29,28,-1,36,30,29,-1,36,31,30,-1,36,32,31,-1,36,33,32,-1,36,34,33,-1,36,35,34,-1,36,28,35,-1]
IndexedFaceSet818.creaseAngle = 3.14159
IndexedFaceSet818.texCoordIndex = [0,3,2,-1,2,1,0,-1,0,5,4,-1,0,4,6,-1,6,3,0,-1,3,6,7,-1,3,7,8,-1,8,2,3,-1,2,8,9,-1,2,9,10,-1,10,1,2,-1,1,10,11,-1,1,11,5,-1,5,0,1,-1,5,13,12,-1,12,4,5,-1,4,12,14,-1,14,6,4,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,13,-1,13,5,11,-1,13,21,20,-1,20,12,13,-1,12,20,22,-1,22,14,12,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,21,-1,21,13,19,-1,21,29,28,-1,28,20,21,-1,20,28,30,-1,30,22,20,-1,22,30,31,-1,31,23,22,-1,23,31,32,-1,32,24,23,-1,24,32,33,-1,33,25,24,-1,25,33,34,-1,34,26,25,-1,26,34,35,-1,35,27,26,-1,27,35,29,-1,29,21,27,-1,36,28,29,-1,36,30,28,-1,36,31,30,-1,36,32,31,-1,36,33,32,-1,36,34,33,-1,36,35,34,-1,36,29,35,-1]
Coordinate819 = x3d.Coordinate()

IndexedFaceSet818.coord = Coordinate819
TextureCoordinate820 = x3d.TextureCoordinate()

IndexedFaceSet818.texCoord = TextureCoordinate820

Shape814.geometry = IndexedFaceSet818

Transform813.children.append(Shape814)

HAnimSegment812.children.append(Transform813)

HAnimJoint811.children.append(HAnimSegment812)
HAnimJoint821 = x3d.HAnimJoint()
HAnimJoint821.name = "r_metacarpophalangeal_2"
HAnimJoint821.DEF = "hanim_r_metacarpophalangeal_2"
HAnimJoint821.center = [-8.52,27.24,0.6551]
HAnimJoint821.ulimit = [0,0,0]
HAnimJoint821.llimit = [0,0,0]
HAnimSegment822 = x3d.HAnimSegment()
HAnimSegment822.name = "r_carpal_proximal_phalanx_2"
HAnimSegment822.DEF = "hanim_r_carpal_proximal_phalanx_2"
Transform823 = x3d.Transform()
Transform823.translation = [-8.52,27.24,0.6551]
Shape824 = x3d.Shape()
Appearance825 = x3d.Appearance()
Material826 = x3d.Material()
Material826.diffuseColor = [0.588,0.588,0.588]

Appearance825.material = Material826
ImageTexture827 = x3d.ImageTexture()
ImageTexture827.USE = "JinLOA3TextureAtlas"

Appearance825.texture = ImageTexture827

Shape824.appearance = Appearance825
IndexedFaceSet828 = x3d.IndexedFaceSet()
IndexedFaceSet828.coordIndex = [0,2,3,-1,3,1,0,-1,0,4,5,-1,0,5,6,-1,6,2,0,-1,2,6,7,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,3,9,10,-1,10,1,3,-1,1,10,11,-1,1,11,4,-1,4,0,1,-1,4,12,13,-1,13,5,4,-1,5,13,14,-1,14,6,5,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,12,-1,12,4,11,-1,12,20,21,-1,21,13,12,-1,13,21,22,-1,22,14,13,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,20,-1,20,12,19,-1,20,28,29,-1,29,21,20,-1,21,29,30,-1,30,22,21,-1,22,30,31,-1,31,23,22,-1,23,31,32,-1,32,24,23,-1,24,32,33,-1,33,25,24,-1,25,33,34,-1,34,26,25,-1,26,34,35,-1,35,27,26,-1,27,35,28,-1,28,20,27,-1,36,29,28,-1,36,30,29,-1,36,31,30,-1,36,32,31,-1,36,33,32,-1,36,34,33,-1,36,35,34,-1,36,28,35,-1]
IndexedFaceSet828.creaseAngle = 3.14159
IndexedFaceSet828.texCoordIndex = [0,3,2,-1,2,1,0,-1,0,5,4,-1,0,4,6,-1,6,3,0,-1,3,6,7,-1,3,7,8,-1,8,2,3,-1,2,8,9,-1,2,9,10,-1,10,1,2,-1,1,10,11,-1,1,11,5,-1,5,0,1,-1,5,13,12,-1,12,4,5,-1,4,12,14,-1,14,6,4,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,13,-1,13,5,11,-1,13,21,20,-1,20,12,13,-1,12,20,22,-1,22,14,12,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,21,-1,21,13,19,-1,21,29,28,-1,28,20,21,-1,20,28,30,-1,30,22,20,-1,22,30,31,-1,31,23,22,-1,23,31,32,-1,32,24,23,-1,24,32,33,-1,33,25,24,-1,25,33,34,-1,34,26,25,-1,26,34,35,-1,35,27,26,-1,27,35,29,-1,29,21,27,-1,36,28,29,-1,36,30,28,-1,36,31,30,-1,36,32,31,-1,36,33,32,-1,36,34,33,-1,36,35,34,-1,36,29,35,-1]
Coordinate829 = x3d.Coordinate()

IndexedFaceSet828.coord = Coordinate829
TextureCoordinate830 = x3d.TextureCoordinate()

IndexedFaceSet828.texCoord = TextureCoordinate830

Shape824.geometry = IndexedFaceSet828

Transform823.children.append(Shape824)

HAnimSegment822.children.append(Transform823)

HAnimJoint821.children.append(HAnimSegment822)
HAnimJoint831 = x3d.HAnimJoint()
HAnimJoint831.name = "r_carpal_proximal_interphalangeal_2"
HAnimJoint831.DEF = "hanim_r_carpal_proximal_interphalangeal_2"
HAnimJoint831.center = [-8.45,26.1,0.6956]
HAnimJoint831.ulimit = [0,0,0]
HAnimJoint831.llimit = [0,0,0]
HAnimSegment832 = x3d.HAnimSegment()
HAnimSegment832.name = "r_carpal_middle_phalanx_2"
HAnimSegment832.DEF = "hanim_r_carpal_middle_phalanx_2"
Transform833 = x3d.Transform()
Transform833.translation = [-8.45,26.1,0.6956]
Shape834 = x3d.Shape()
Appearance835 = x3d.Appearance()
Material836 = x3d.Material()
Material836.diffuseColor = [0.588,0.588,0.588]

Appearance835.material = Material836
ImageTexture837 = x3d.ImageTexture()
ImageTexture837.USE = "JinLOA3TextureAtlas"

Appearance835.texture = ImageTexture837

Shape834.appearance = Appearance835
IndexedFaceSet838 = x3d.IndexedFaceSet()
IndexedFaceSet838.coordIndex = [0,2,3,-1,3,1,0,-1,0,4,5,-1,0,5,6,-1,6,2,0,-1,2,6,7,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,3,9,10,-1,10,1,3,-1,1,10,11,-1,1,11,4,-1,4,0,1,-1,4,12,13,-1,13,5,4,-1,5,13,14,-1,14,6,5,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,12,-1,12,4,11,-1,12,20,21,-1,21,13,12,-1,13,21,22,-1,22,14,13,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,20,-1,20,12,19,-1,28,21,20,-1,28,22,21,-1,28,23,22,-1,28,24,23,-1,28,25,24,-1,28,26,25,-1,28,27,26,-1,28,20,27,-1]
IndexedFaceSet838.creaseAngle = 3.14159
IndexedFaceSet838.texCoordIndex = [0,3,2,-1,2,1,0,-1,0,5,4,-1,0,4,6,-1,6,3,0,-1,3,6,7,-1,3,7,8,-1,8,2,3,-1,2,8,9,-1,2,9,10,-1,10,1,2,-1,1,10,11,-1,1,11,5,-1,5,0,1,-1,5,13,12,-1,12,4,5,-1,4,12,14,-1,14,6,4,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,13,-1,13,5,11,-1,13,21,20,-1,20,12,13,-1,12,20,22,-1,22,14,12,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,21,-1,21,13,19,-1,28,20,21,-1,28,22,20,-1,28,23,22,-1,28,24,23,-1,28,25,24,-1,28,26,25,-1,28,27,26,-1,28,21,27,-1]
Coordinate839 = x3d.Coordinate()

IndexedFaceSet838.coord = Coordinate839
TextureCoordinate840 = x3d.TextureCoordinate()

IndexedFaceSet838.texCoord = TextureCoordinate840

Shape834.geometry = IndexedFaceSet838

Transform833.children.append(Shape834)

HAnimSegment832.children.append(Transform833)

HAnimJoint831.children.append(HAnimSegment832)
HAnimJoint841 = x3d.HAnimJoint()
HAnimJoint841.name = "r_carpal_distal_interphalangeal_2"
HAnimJoint841.DEF = "hanim_r_carpal_distal_interphalangeal_2"
HAnimJoint841.center = [-8.192,25.17,0.7315]
HAnimJoint841.ulimit = [0,0,0]
HAnimJoint841.llimit = [0,0,0]
HAnimSegment842 = x3d.HAnimSegment()
HAnimSegment842.name = "r_carpal_distal_phalanx_2"
HAnimSegment842.DEF = "hanim_r_carpal_distal_phalanx_2"
Transform843 = x3d.Transform()
Transform843.translation = [-8.192,25.17,0.7315]
Shape844 = x3d.Shape()
Appearance845 = x3d.Appearance()
Material846 = x3d.Material()
Material846.diffuseColor = [0.588,0.588,0.588]

Appearance845.material = Material846
ImageTexture847 = x3d.ImageTexture()
ImageTexture847.USE = "JinLOA3TextureAtlas"

Appearance845.texture = ImageTexture847

Shape844.appearance = Appearance845
IndexedFaceSet848 = x3d.IndexedFaceSet()
IndexedFaceSet848.coordIndex = [0,2,3,-1,3,1,0,-1,0,4,5,-1,0,5,6,-1,6,2,0,-1,2,6,7,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,3,9,10,-1,10,1,3,-1,1,10,11,-1,1,11,4,-1,4,0,1,-1,4,12,13,-1,13,5,4,-1,5,13,14,-1,14,6,5,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,12,-1,12,4,11,-1,12,20,21,-1,21,13,12,-1,13,21,22,-1,22,14,13,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,20,-1,20,12,19,-1,28,21,20,-1,28,22,21,-1,28,23,22,-1,28,24,23,-1,28,25,24,-1,28,26,25,-1,28,27,26,-1,28,20,27,-1]
IndexedFaceSet848.creaseAngle = 3.14159
IndexedFaceSet848.texCoordIndex = [0,3,2,-1,2,1,0,-1,0,5,4,-1,0,4,6,-1,6,3,0,-1,3,6,7,-1,3,7,8,-1,8,2,3,-1,2,8,9,-1,2,9,10,-1,10,1,2,-1,1,10,11,-1,1,11,5,-1,5,0,1,-1,5,13,12,-1,12,4,5,-1,4,12,14,-1,14,6,4,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,13,-1,13,5,11,-1,13,21,20,-1,20,12,13,-1,12,20,22,-1,22,14,12,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,21,-1,21,13,19,-1,28,20,21,-1,28,22,20,-1,28,23,22,-1,28,24,23,-1,28,25,24,-1,28,26,25,-1,28,27,26,-1,28,21,27,-1]
Coordinate849 = x3d.Coordinate()

IndexedFaceSet848.coord = Coordinate849
TextureCoordinate850 = x3d.TextureCoordinate()

IndexedFaceSet848.texCoord = TextureCoordinate850

Shape844.geometry = IndexedFaceSet848

Transform843.children.append(Shape844)

HAnimSegment842.children.append(Transform843)

HAnimJoint841.children.append(HAnimSegment842)

HAnimJoint831.children.append(HAnimJoint841)

HAnimJoint821.children.append(HAnimJoint831)

HAnimJoint811.children.append(HAnimJoint821)

HAnimJoint771.children.append(HAnimJoint811)
HAnimJoint851 = x3d.HAnimJoint()
HAnimJoint851.name = "r_carpometacarpal_3"
HAnimJoint851.DEF = "hanim_r_carpometacarpal_3"
HAnimJoint851.center = [-8.344,28.65,-0.194]
HAnimJoint851.ulimit = [0,0,0]
HAnimJoint851.llimit = [0,0,0]
HAnimSegment852 = x3d.HAnimSegment()
HAnimSegment852.name = "r_metacarpal_3"
HAnimSegment852.DEF = "hanim_r_metacarpal_3"
Transform853 = x3d.Transform()
Transform853.translation = [-8.344,28.65,-0.194]
Shape854 = x3d.Shape()
Appearance855 = x3d.Appearance()
Material856 = x3d.Material()
Material856.diffuseColor = [0.588,0.588,0.588]

Appearance855.material = Material856
ImageTexture857 = x3d.ImageTexture()
ImageTexture857.USE = "JinLOA3TextureAtlas"

Appearance855.texture = ImageTexture857

Shape854.appearance = Appearance855
IndexedFaceSet858 = x3d.IndexedFaceSet()
IndexedFaceSet858.coordIndex = [0,2,3,-1,3,1,0,-1,0,4,5,-1,0,5,6,-1,6,2,0,-1,2,6,7,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,3,9,10,-1,10,1,3,-1,1,10,11,-1,1,11,4,-1,4,0,1,-1,4,12,13,-1,13,5,4,-1,5,13,14,-1,14,6,5,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,12,-1,12,4,11,-1,12,20,21,-1,21,13,12,-1,13,21,22,-1,22,14,13,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,20,-1,20,12,19,-1,20,28,29,-1,29,21,20,-1,21,29,30,-1,30,22,21,-1,22,30,31,-1,31,23,22,-1,23,31,32,-1,32,24,23,-1,24,32,33,-1,33,25,24,-1,25,33,34,-1,34,26,25,-1,26,34,35,-1,35,27,26,-1,27,35,28,-1,28,20,27,-1,36,29,28,-1,36,30,29,-1,36,31,30,-1,36,32,31,-1,36,33,32,-1,36,34,33,-1,36,35,34,-1,36,28,35,-1]
IndexedFaceSet858.creaseAngle = 3.14159
IndexedFaceSet858.texCoordIndex = [0,3,2,-1,2,1,0,-1,0,5,4,-1,0,4,6,-1,6,3,0,-1,3,6,7,-1,3,7,8,-1,8,2,3,-1,2,8,9,-1,2,9,10,-1,10,1,2,-1,1,10,11,-1,1,11,5,-1,5,0,1,-1,5,13,12,-1,12,4,5,-1,4,12,14,-1,14,6,4,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,13,-1,13,5,11,-1,13,21,20,-1,20,12,13,-1,12,20,22,-1,22,14,12,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,21,-1,21,13,19,-1,21,29,28,-1,28,20,21,-1,20,28,30,-1,30,22,20,-1,22,30,31,-1,31,23,22,-1,23,31,32,-1,32,24,23,-1,24,32,33,-1,33,25,24,-1,25,33,34,-1,34,26,25,-1,26,34,35,-1,35,27,26,-1,27,35,29,-1,29,21,27,-1,36,28,29,-1,36,30,28,-1,36,31,30,-1,36,32,31,-1,36,33,32,-1,36,34,33,-1,36,35,34,-1,36,29,35,-1]
Coordinate859 = x3d.Coordinate()

IndexedFaceSet858.coord = Coordinate859
TextureCoordinate860 = x3d.TextureCoordinate()

IndexedFaceSet858.texCoord = TextureCoordinate860

Shape854.geometry = IndexedFaceSet858

Transform853.children.append(Shape854)

HAnimSegment852.children.append(Transform853)

HAnimJoint851.children.append(HAnimSegment852)
HAnimJoint861 = x3d.HAnimJoint()
HAnimJoint861.name = "r_metacarpophalangeal_3"
HAnimJoint861.DEF = "hanim_r_metacarpophalangeal_3"
HAnimJoint861.center = [-8.52,27.26,-0.1959]
HAnimJoint861.ulimit = [0,0,0]
HAnimJoint861.llimit = [0,0,0]
HAnimSegment862 = x3d.HAnimSegment()
HAnimSegment862.name = "r_carpal_proximal_phalanx_3"
HAnimSegment862.DEF = "hanim_r_carpal_proximal_phalanx_3"
Transform863 = x3d.Transform()
Transform863.translation = [-8.52,27.26,-0.1959]
Shape864 = x3d.Shape()
Appearance865 = x3d.Appearance()
Material866 = x3d.Material()
Material866.diffuseColor = [0.588,0.588,0.588]

Appearance865.material = Material866
ImageTexture867 = x3d.ImageTexture()
ImageTexture867.USE = "JinLOA3TextureAtlas"

Appearance865.texture = ImageTexture867

Shape864.appearance = Appearance865
IndexedFaceSet868 = x3d.IndexedFaceSet()
IndexedFaceSet868.coordIndex = [0,2,3,-1,3,1,0,-1,0,4,5,-1,0,5,6,-1,6,2,0,-1,2,6,7,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,3,9,10,-1,10,1,3,-1,1,10,11,-1,1,11,4,-1,4,0,1,-1,4,12,13,-1,13,5,4,-1,5,13,14,-1,14,6,5,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,12,-1,12,4,11,-1,12,20,21,-1,21,13,12,-1,13,21,22,-1,22,14,13,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,20,-1,20,12,19,-1,20,28,29,-1,29,21,20,-1,21,29,30,-1,30,22,21,-1,22,30,31,-1,31,23,22,-1,23,31,32,-1,32,24,23,-1,24,32,33,-1,33,25,24,-1,25,33,34,-1,34,26,25,-1,26,34,35,-1,35,27,26,-1,27,35,28,-1,28,20,27,-1,36,29,28,-1,36,30,29,-1,36,31,30,-1,36,32,31,-1,36,33,32,-1,36,34,33,-1,36,35,34,-1,36,28,35,-1]
IndexedFaceSet868.creaseAngle = 3.14159
IndexedFaceSet868.texCoordIndex = [0,3,2,-1,2,1,0,-1,0,5,4,-1,0,4,6,-1,6,3,0,-1,3,6,7,-1,3,7,8,-1,8,2,3,-1,2,8,9,-1,2,9,10,-1,10,1,2,-1,1,10,11,-1,1,11,5,-1,5,0,1,-1,5,13,12,-1,12,4,5,-1,4,12,14,-1,14,6,4,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,13,-1,13,5,11,-1,13,21,20,-1,20,12,13,-1,12,20,22,-1,22,14,12,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,21,-1,21,13,19,-1,21,29,28,-1,28,20,21,-1,20,28,30,-1,30,22,20,-1,22,30,31,-1,31,23,22,-1,23,31,32,-1,32,24,23,-1,24,32,33,-1,33,25,24,-1,25,33,34,-1,34,26,25,-1,26,34,35,-1,35,27,26,-1,27,35,29,-1,29,21,27,-1,36,28,29,-1,36,30,28,-1,36,31,30,-1,36,32,31,-1,36,33,32,-1,36,34,33,-1,36,35,34,-1,36,29,35,-1]
Coordinate869 = x3d.Coordinate()

IndexedFaceSet868.coord = Coordinate869
TextureCoordinate870 = x3d.TextureCoordinate()

IndexedFaceSet868.texCoord = TextureCoordinate870

Shape864.geometry = IndexedFaceSet868

Transform863.children.append(Shape864)

HAnimSegment862.children.append(Transform863)

HAnimJoint861.children.append(HAnimSegment862)
HAnimJoint871 = x3d.HAnimJoint()
HAnimJoint871.name = "r_carpal_proximal_interphalangeal_3"
HAnimJoint871.DEF = "hanim_r_carpal_proximal_interphalangeal_3"
HAnimJoint871.center = [-8.477,26.07,-0.2214]
HAnimJoint871.ulimit = [0,0,0]
HAnimJoint871.llimit = [0,0,0]
HAnimSegment872 = x3d.HAnimSegment()
HAnimSegment872.name = "r_carpal_middle_phalanx_3"
HAnimSegment872.DEF = "hanim_r_carpal_middle_phalanx_3"
Transform873 = x3d.Transform()
Transform873.translation = [-8.477,26.07,-0.2214]
Shape874 = x3d.Shape()
Appearance875 = x3d.Appearance()
Material876 = x3d.Material()
Material876.diffuseColor = [0.588,0.588,0.588]

Appearance875.material = Material876
ImageTexture877 = x3d.ImageTexture()
ImageTexture877.USE = "JinLOA3TextureAtlas"

Appearance875.texture = ImageTexture877

Shape874.appearance = Appearance875
IndexedFaceSet878 = x3d.IndexedFaceSet()
IndexedFaceSet878.coordIndex = [0,2,3,-1,3,1,0,-1,0,4,5,-1,0,5,6,-1,6,2,0,-1,2,6,7,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,3,9,10,-1,10,1,3,-1,1,10,11,-1,1,11,4,-1,4,0,1,-1,4,12,13,-1,13,5,4,-1,5,13,14,-1,14,6,5,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,12,-1,12,4,11,-1,12,20,21,-1,21,13,12,-1,13,21,22,-1,22,14,13,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,20,-1,20,12,19,-1,28,21,20,-1,28,22,21,-1,28,23,22,-1,28,24,23,-1,28,25,24,-1,28,26,25,-1,28,27,26,-1,28,20,27,-1]
IndexedFaceSet878.creaseAngle = 3.14159
IndexedFaceSet878.texCoordIndex = [0,3,2,-1,2,1,0,-1,0,5,4,-1,0,4,6,-1,6,3,0,-1,3,6,7,-1,3,7,8,-1,8,2,3,-1,2,8,9,-1,2,9,10,-1,10,1,2,-1,1,10,11,-1,1,11,5,-1,5,0,1,-1,5,13,12,-1,12,4,5,-1,4,12,14,-1,14,6,4,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,13,-1,13,5,11,-1,13,21,20,-1,20,12,13,-1,12,20,22,-1,22,14,12,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,21,-1,21,13,19,-1,28,20,21,-1,28,22,20,-1,28,23,22,-1,28,24,23,-1,28,25,24,-1,28,26,25,-1,28,27,26,-1,28,21,27,-1]
Coordinate879 = x3d.Coordinate()

IndexedFaceSet878.coord = Coordinate879
TextureCoordinate880 = x3d.TextureCoordinate()

IndexedFaceSet878.texCoord = TextureCoordinate880

Shape874.geometry = IndexedFaceSet878

Transform873.children.append(Shape874)

HAnimSegment872.children.append(Transform873)

HAnimJoint871.children.append(HAnimSegment872)
HAnimJoint881 = x3d.HAnimJoint()
HAnimJoint881.name = "r_carpal_distal_interphalangeal_3"
HAnimJoint881.DEF = "hanim_r_carpal_distal_interphalangeal_3"
HAnimJoint881.center = [-8.25,25.030001,-0.2187]
HAnimJoint881.ulimit = [0,0,0]
HAnimJoint881.llimit = [0,0,0]
HAnimSegment882 = x3d.HAnimSegment()
HAnimSegment882.name = "r_carpal_distal_phalanx_3"
HAnimSegment882.DEF = "hanim_r_carpal_distal_phalanx_3"
Transform883 = x3d.Transform()
Transform883.translation = [-8.25,25.030001,-0.2187]
Shape884 = x3d.Shape()
Appearance885 = x3d.Appearance()
Material886 = x3d.Material()
Material886.diffuseColor = [0.588,0.588,0.588]

Appearance885.material = Material886
ImageTexture887 = x3d.ImageTexture()
ImageTexture887.USE = "JinLOA3TextureAtlas"

Appearance885.texture = ImageTexture887

Shape884.appearance = Appearance885
IndexedFaceSet888 = x3d.IndexedFaceSet()
IndexedFaceSet888.coordIndex = [0,2,3,-1,3,1,0,-1,0,4,5,-1,0,5,6,-1,6,2,0,-1,2,6,7,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,3,9,10,-1,10,1,3,-1,1,10,11,-1,1,11,4,-1,4,0,1,-1,4,12,13,-1,13,5,4,-1,5,13,14,-1,14,6,5,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,12,-1,12,4,11,-1,12,20,21,-1,21,13,12,-1,13,21,22,-1,22,14,13,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,20,-1,20,12,19,-1,28,21,20,-1,28,22,21,-1,28,23,22,-1,28,24,23,-1,28,25,24,-1,28,26,25,-1,28,27,26,-1,28,20,27,-1]
IndexedFaceSet888.creaseAngle = 3.14159
IndexedFaceSet888.texCoordIndex = [0,3,2,-1,2,1,0,-1,0,5,4,-1,0,4,6,-1,6,3,0,-1,3,6,7,-1,3,7,8,-1,8,2,3,-1,2,8,9,-1,2,9,10,-1,10,1,2,-1,1,10,11,-1,1,11,5,-1,5,0,1,-1,5,13,12,-1,12,4,5,-1,4,12,14,-1,14,6,4,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,13,-1,13,5,11,-1,13,21,20,-1,20,12,13,-1,12,20,22,-1,22,14,12,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,21,-1,21,13,19,-1,28,20,21,-1,28,22,20,-1,28,23,22,-1,28,24,23,-1,28,25,24,-1,28,26,25,-1,28,27,26,-1,28,21,27,-1]
Coordinate889 = x3d.Coordinate()

IndexedFaceSet888.coord = Coordinate889
TextureCoordinate890 = x3d.TextureCoordinate()

IndexedFaceSet888.texCoord = TextureCoordinate890

Shape884.geometry = IndexedFaceSet888

Transform883.children.append(Shape884)

HAnimSegment882.children.append(Transform883)

HAnimJoint881.children.append(HAnimSegment882)

HAnimJoint871.children.append(HAnimJoint881)

HAnimJoint861.children.append(HAnimJoint871)

HAnimJoint851.children.append(HAnimJoint861)

HAnimJoint771.children.append(HAnimJoint851)
HAnimJoint891 = x3d.HAnimJoint()
HAnimJoint891.name = "r_carpometacarpal_4"
HAnimJoint891.DEF = "hanim_r_carpometacarpal_4"
HAnimJoint891.center = [-8.339,28.57,-0.9243]
HAnimJoint891.ulimit = [0,0,0]
HAnimJoint891.llimit = [0,0,0]
HAnimSegment892 = x3d.HAnimSegment()
HAnimSegment892.name = "r_metacarpal_4"
HAnimSegment892.DEF = "hanim_r_metacarpal_4"
Transform893 = x3d.Transform()
Transform893.translation = [-8.339,28.57,-0.9243]
Shape894 = x3d.Shape()
Appearance895 = x3d.Appearance()
Material896 = x3d.Material()
Material896.diffuseColor = [0.588,0.588,0.588]

Appearance895.material = Material896
ImageTexture897 = x3d.ImageTexture()
ImageTexture897.USE = "JinLOA3TextureAtlas"

Appearance895.texture = ImageTexture897

Shape894.appearance = Appearance895
IndexedFaceSet898 = x3d.IndexedFaceSet()
IndexedFaceSet898.coordIndex = [0,2,3,-1,3,1,0,-1,0,4,5,-1,0,5,6,-1,6,2,0,-1,2,6,7,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,3,9,10,-1,10,1,3,-1,1,10,11,-1,1,11,4,-1,4,0,1,-1,4,12,13,-1,13,5,4,-1,5,13,14,-1,14,6,5,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,12,-1,12,4,11,-1,12,20,21,-1,21,13,12,-1,13,21,22,-1,22,14,13,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,20,-1,20,12,19,-1,20,28,29,-1,29,21,20,-1,21,29,30,-1,30,22,21,-1,22,30,31,-1,31,23,22,-1,23,31,32,-1,32,24,23,-1,24,32,33,-1,33,25,24,-1,25,33,34,-1,34,26,25,-1,26,34,35,-1,35,27,26,-1,27,35,28,-1,28,20,27,-1,36,29,28,-1,36,30,29,-1,36,31,30,-1,36,32,31,-1,36,33,32,-1,36,34,33,-1,36,35,34,-1,36,28,35,-1]
IndexedFaceSet898.creaseAngle = 3.14159
IndexedFaceSet898.texCoordIndex = [0,3,2,-1,2,1,0,-1,0,5,4,-1,0,4,6,-1,6,3,0,-1,3,6,7,-1,3,7,8,-1,8,2,3,-1,2,8,9,-1,2,9,10,-1,10,1,2,-1,1,10,11,-1,1,11,5,-1,5,0,1,-1,5,13,12,-1,12,4,5,-1,4,12,14,-1,14,6,4,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,13,-1,13,5,11,-1,13,21,20,-1,20,12,13,-1,12,20,22,-1,22,14,12,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,21,-1,21,13,19,-1,21,29,28,-1,28,20,21,-1,20,28,30,-1,30,22,20,-1,22,30,31,-1,31,23,22,-1,23,31,32,-1,32,24,23,-1,24,32,33,-1,33,25,24,-1,25,33,34,-1,34,26,25,-1,26,34,35,-1,35,27,26,-1,27,35,29,-1,29,21,27,-1,36,28,29,-1,36,30,28,-1,36,31,30,-1,36,32,31,-1,36,33,32,-1,36,34,33,-1,36,35,34,-1,36,29,35,-1]
Coordinate899 = x3d.Coordinate()

IndexedFaceSet898.coord = Coordinate899
TextureCoordinate900 = x3d.TextureCoordinate()

IndexedFaceSet898.texCoord = TextureCoordinate900

Shape894.geometry = IndexedFaceSet898

Transform893.children.append(Shape894)

HAnimSegment892.children.append(Transform893)

HAnimJoint891.children.append(HAnimSegment892)
HAnimJoint901 = x3d.HAnimJoint()
HAnimJoint901.name = "r_metacarpophalangeal_4"
HAnimJoint901.DEF = "hanim_r_metacarpophalangeal_4"
HAnimJoint901.center = [-8.428,27.299999,-0.9985]
HAnimJoint901.ulimit = [0,0,0]
HAnimJoint901.llimit = [0,0,0]
HAnimSegment902 = x3d.HAnimSegment()
HAnimSegment902.name = "r_carpal_proximal_phalanx_4"
HAnimSegment902.DEF = "hanim_r_carpal_proximal_phalanx_4"
Transform903 = x3d.Transform()
Transform903.translation = [-8.428,27.299999,-0.9985]
Shape904 = x3d.Shape()
Appearance905 = x3d.Appearance()
Material906 = x3d.Material()
Material906.diffuseColor = [0.588,0.588,0.588]

Appearance905.material = Material906
ImageTexture907 = x3d.ImageTexture()
ImageTexture907.USE = "JinLOA3TextureAtlas"

Appearance905.texture = ImageTexture907

Shape904.appearance = Appearance905
IndexedFaceSet908 = x3d.IndexedFaceSet()
IndexedFaceSet908.coordIndex = [0,2,3,-1,3,1,0,-1,0,4,5,-1,0,5,6,-1,6,2,0,-1,2,6,7,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,3,9,10,-1,10,1,3,-1,1,10,11,-1,1,11,4,-1,4,0,1,-1,4,12,13,-1,13,5,4,-1,5,13,14,-1,14,6,5,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,12,-1,12,4,11,-1,12,20,21,-1,21,13,12,-1,13,21,22,-1,22,14,13,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,20,-1,20,12,19,-1,20,28,29,-1,29,21,20,-1,21,29,30,-1,30,22,21,-1,22,30,31,-1,31,23,22,-1,23,31,32,-1,32,24,23,-1,24,32,33,-1,33,25,24,-1,25,33,34,-1,34,26,25,-1,26,34,35,-1,35,27,26,-1,27,35,28,-1,28,20,27,-1,36,29,28,-1,36,30,29,-1,36,31,30,-1,36,32,31,-1,36,33,32,-1,36,34,33,-1,36,35,34,-1,36,28,35,-1]
IndexedFaceSet908.creaseAngle = 3.14159
IndexedFaceSet908.texCoordIndex = [0,3,2,-1,2,1,0,-1,0,5,4,-1,0,4,6,-1,6,3,0,-1,3,6,7,-1,3,7,8,-1,8,2,3,-1,2,8,9,-1,2,9,10,-1,10,1,2,-1,1,10,11,-1,1,11,5,-1,5,0,1,-1,5,13,12,-1,12,4,5,-1,4,12,14,-1,14,6,4,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,13,-1,13,5,11,-1,13,21,20,-1,20,12,13,-1,12,20,22,-1,22,14,12,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,21,-1,21,13,19,-1,21,29,28,-1,28,20,21,-1,20,28,30,-1,30,22,20,-1,22,30,31,-1,31,23,22,-1,23,31,32,-1,32,24,23,-1,24,32,33,-1,33,25,24,-1,25,33,34,-1,34,26,25,-1,26,34,35,-1,35,27,26,-1,27,35,29,-1,29,21,27,-1,36,28,29,-1,36,30,28,-1,36,31,30,-1,36,32,31,-1,36,33,32,-1,36,34,33,-1,36,35,34,-1,36,29,35,-1]
Coordinate909 = x3d.Coordinate()

IndexedFaceSet908.coord = Coordinate909
TextureCoordinate910 = x3d.TextureCoordinate()

IndexedFaceSet908.texCoord = TextureCoordinate910

Shape904.geometry = IndexedFaceSet908

Transform903.children.append(Shape904)

HAnimSegment902.children.append(Transform903)

HAnimJoint901.children.append(HAnimSegment902)
HAnimJoint911 = x3d.HAnimJoint()
HAnimJoint911.name = "r_carpal_proximal_interphalangeal_4"
HAnimJoint911.DEF = "hanim_r_carpal_proximal_interphalangeal_4"
HAnimJoint911.center = [-8.428,26.290001,-1.034]
HAnimJoint911.ulimit = [0,0,0]
HAnimJoint911.llimit = [0,0,0]
HAnimSegment912 = x3d.HAnimSegment()
HAnimSegment912.name = "r_carpal_middle_phalanx_4"
HAnimSegment912.DEF = "hanim_r_carpal_middle_phalanx_4"
Transform913 = x3d.Transform()
Transform913.translation = [-8.428,26.290001,-1.034]
Shape914 = x3d.Shape()
Appearance915 = x3d.Appearance()
Material916 = x3d.Material()
Material916.diffuseColor = [0.588,0.588,0.588]

Appearance915.material = Material916
ImageTexture917 = x3d.ImageTexture()
ImageTexture917.USE = "JinLOA3TextureAtlas"

Appearance915.texture = ImageTexture917

Shape914.appearance = Appearance915
IndexedFaceSet918 = x3d.IndexedFaceSet()
IndexedFaceSet918.coordIndex = [0,2,3,-1,3,1,0,-1,0,4,5,-1,0,5,6,-1,6,2,0,-1,2,6,7,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,3,9,10,-1,10,1,3,-1,1,10,11,-1,1,11,4,-1,4,0,1,-1,4,12,13,-1,13,5,4,-1,5,13,14,-1,14,6,5,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,12,-1,12,4,11,-1,12,20,21,-1,21,13,12,-1,13,21,22,-1,22,14,13,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,20,-1,20,12,19,-1,28,21,20,-1,28,22,21,-1,28,23,22,-1,28,24,23,-1,28,25,24,-1,28,26,25,-1,28,27,26,-1,28,20,27,-1]
IndexedFaceSet918.creaseAngle = 3.14159
IndexedFaceSet918.texCoordIndex = [0,3,2,-1,2,1,0,-1,0,5,4,-1,0,4,6,-1,6,3,0,-1,3,6,7,-1,3,7,8,-1,8,2,3,-1,2,8,9,-1,2,9,10,-1,10,1,2,-1,1,10,11,-1,1,11,5,-1,5,0,1,-1,5,13,12,-1,12,4,5,-1,4,12,14,-1,14,6,4,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,13,-1,13,5,11,-1,13,21,20,-1,20,12,13,-1,12,20,22,-1,22,14,12,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,21,-1,21,13,19,-1,28,20,21,-1,28,22,20,-1,28,23,22,-1,28,24,23,-1,28,25,24,-1,28,26,25,-1,28,27,26,-1,28,21,27,-1]
Coordinate919 = x3d.Coordinate()

IndexedFaceSet918.coord = Coordinate919
TextureCoordinate920 = x3d.TextureCoordinate()

IndexedFaceSet918.texCoord = TextureCoordinate920

Shape914.geometry = IndexedFaceSet918

Transform913.children.append(Shape914)

HAnimSegment912.children.append(Transform913)

HAnimJoint911.children.append(HAnimSegment912)
HAnimJoint921 = x3d.HAnimJoint()
HAnimJoint921.name = "r_carpal_distal_interphalangeal_4"
HAnimJoint921.DEF = "hanim_r_carpal_distal_interphalangeal_4"
HAnimJoint921.center = [-8.192,25.309999,-1.124]
HAnimJoint921.ulimit = [0,0,0]
HAnimJoint921.llimit = [0,0,0]
HAnimSegment922 = x3d.HAnimSegment()
HAnimSegment922.name = "r_carpal_distal_phalanx_4"
HAnimSegment922.DEF = "hanim_r_carpal_distal_phalanx_4"
Transform923 = x3d.Transform()
Transform923.translation = [-8.192,25.309999,-1.124]
Shape924 = x3d.Shape()
Appearance925 = x3d.Appearance()
Material926 = x3d.Material()
Material926.diffuseColor = [0.588,0.588,0.588]

Appearance925.material = Material926
ImageTexture927 = x3d.ImageTexture()
ImageTexture927.USE = "JinLOA3TextureAtlas"

Appearance925.texture = ImageTexture927

Shape924.appearance = Appearance925
IndexedFaceSet928 = x3d.IndexedFaceSet()
IndexedFaceSet928.coordIndex = [0,2,3,-1,3,1,0,-1,0,4,5,-1,0,5,6,-1,6,2,0,-1,2,6,7,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,3,9,10,-1,10,1,3,-1,1,10,11,-1,1,11,4,-1,4,0,1,-1,4,12,13,-1,13,5,4,-1,5,13,14,-1,14,6,5,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,12,-1,12,4,11,-1,12,20,21,-1,21,13,12,-1,13,21,22,-1,22,14,13,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,20,-1,20,12,19,-1,28,21,20,-1,28,22,21,-1,28,23,22,-1,28,24,23,-1,28,25,24,-1,28,26,25,-1,28,27,26,-1,28,20,27,-1]
IndexedFaceSet928.creaseAngle = 3.14159
IndexedFaceSet928.texCoordIndex = [0,3,2,-1,2,1,0,-1,0,5,4,-1,0,4,6,-1,6,3,0,-1,3,6,7,-1,3,7,8,-1,8,2,3,-1,2,8,9,-1,2,9,10,-1,10,1,2,-1,1,10,11,-1,1,11,5,-1,5,0,1,-1,5,13,12,-1,12,4,5,-1,4,12,14,-1,14,6,4,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,13,-1,13,5,11,-1,13,21,20,-1,20,12,13,-1,12,20,22,-1,22,14,12,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,21,-1,21,13,19,-1,28,20,21,-1,28,22,20,-1,28,23,22,-1,28,24,23,-1,28,25,24,-1,28,26,25,-1,28,27,26,-1,28,21,27,-1]
Coordinate929 = x3d.Coordinate()

IndexedFaceSet928.coord = Coordinate929
TextureCoordinate930 = x3d.TextureCoordinate()

IndexedFaceSet928.texCoord = TextureCoordinate930

Shape924.geometry = IndexedFaceSet928

Transform923.children.append(Shape924)

HAnimSegment922.children.append(Transform923)

HAnimJoint921.children.append(HAnimSegment922)

HAnimJoint911.children.append(HAnimJoint921)

HAnimJoint901.children.append(HAnimJoint911)

HAnimJoint891.children.append(HAnimJoint901)

HAnimJoint771.children.append(HAnimJoint891)
HAnimJoint931 = x3d.HAnimJoint()
HAnimJoint931.name = "r_carpometacarpal_5"
HAnimJoint931.DEF = "hanim_r_carpometacarpal_5"
HAnimJoint931.center = [-8.197,28.370001,-1.528]
HAnimJoint931.ulimit = [0,0,0]
HAnimJoint931.llimit = [0,0,0]
HAnimSegment932 = x3d.HAnimSegment()
HAnimSegment932.name = "r_metacarpal_5"
HAnimSegment932.DEF = "hanim_r_metacarpal_5"
Transform933 = x3d.Transform()
Transform933.translation = [-8.197,28.370001,-1.528]
Shape934 = x3d.Shape()
Appearance935 = x3d.Appearance()
Material936 = x3d.Material()
Material936.diffuseColor = [0.588,0.588,0.588]

Appearance935.material = Material936
ImageTexture937 = x3d.ImageTexture()
ImageTexture937.USE = "JinLOA3TextureAtlas"

Appearance935.texture = ImageTexture937

Shape934.appearance = Appearance935
IndexedFaceSet938 = x3d.IndexedFaceSet()
IndexedFaceSet938.coordIndex = [0,2,3,-1,3,1,0,-1,0,4,5,-1,0,5,6,-1,6,2,0,-1,2,6,7,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,3,9,10,-1,10,1,3,-1,1,10,11,-1,1,11,4,-1,4,0,1,-1,4,12,13,-1,13,5,4,-1,5,13,14,-1,14,6,5,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,12,-1,12,4,11,-1,12,20,21,-1,21,13,12,-1,13,21,22,-1,22,14,13,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,20,-1,20,12,19,-1,20,28,29,-1,29,21,20,-1,21,29,30,-1,30,22,21,-1,22,30,31,-1,31,23,22,-1,23,31,32,-1,32,24,23,-1,24,32,33,-1,33,25,24,-1,25,33,34,-1,34,26,25,-1,26,34,35,-1,35,27,26,-1,27,35,28,-1,28,20,27,-1,36,29,28,-1,36,30,29,-1,36,31,30,-1,36,32,31,-1,36,33,32,-1,36,34,33,-1,36,35,34,-1,36,28,35,-1]
IndexedFaceSet938.creaseAngle = 3.14159
IndexedFaceSet938.texCoordIndex = [0,3,2,-1,2,1,0,-1,0,5,4,-1,0,4,6,-1,6,3,0,-1,3,6,7,-1,3,7,8,-1,8,2,3,-1,2,8,9,-1,2,9,10,-1,10,1,2,-1,1,10,11,-1,1,11,5,-1,5,0,1,-1,5,13,12,-1,12,4,5,-1,4,12,14,-1,14,6,4,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,13,-1,13,5,11,-1,13,21,20,-1,20,12,13,-1,12,20,22,-1,22,14,12,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,21,-1,21,13,19,-1,21,29,28,-1,28,20,21,-1,20,28,30,-1,30,22,20,-1,22,30,31,-1,31,23,22,-1,23,31,32,-1,32,24,23,-1,24,32,33,-1,33,25,24,-1,25,33,34,-1,34,26,25,-1,26,34,35,-1,35,27,26,-1,27,35,29,-1,29,21,27,-1,36,28,29,-1,36,30,28,-1,36,31,30,-1,36,32,31,-1,36,33,32,-1,36,34,33,-1,36,35,34,-1,36,29,35,-1]
Coordinate939 = x3d.Coordinate()

IndexedFaceSet938.coord = Coordinate939
TextureCoordinate940 = x3d.TextureCoordinate()

IndexedFaceSet938.texCoord = TextureCoordinate940

Shape934.geometry = IndexedFaceSet938

Transform933.children.append(Shape934)

HAnimSegment932.children.append(Transform933)

HAnimJoint931.children.append(HAnimSegment932)
HAnimJoint941 = x3d.HAnimJoint()
HAnimJoint941.name = "r_metacarpophalangeal_5"
HAnimJoint941.DEF = "hanim_r_metacarpophalangeal_5"
HAnimJoint941.center = [-8.334,27.5,-1.701]
HAnimJoint941.ulimit = [0,0,0]
HAnimJoint941.llimit = [0,0,0]
HAnimSegment942 = x3d.HAnimSegment()
HAnimSegment942.name = "r_carpal_proximal_phalanx_5"
HAnimSegment942.DEF = "hanim_r_carpal_proximal_phalanx_5"
Transform943 = x3d.Transform()
Transform943.translation = [-8.334,27.5,-1.701]
Shape944 = x3d.Shape()
Appearance945 = x3d.Appearance()
Material946 = x3d.Material()
Material946.diffuseColor = [0.588,0.588,0.588]

Appearance945.material = Material946
ImageTexture947 = x3d.ImageTexture()
ImageTexture947.USE = "JinLOA3TextureAtlas"

Appearance945.texture = ImageTexture947

Shape944.appearance = Appearance945
IndexedFaceSet948 = x3d.IndexedFaceSet()
IndexedFaceSet948.coordIndex = [0,2,3,-1,3,1,0,-1,0,4,5,-1,0,5,6,-1,6,2,0,-1,2,6,7,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,3,9,10,-1,10,1,3,-1,1,10,11,-1,1,11,4,-1,4,0,1,-1,4,12,13,-1,13,5,4,-1,5,13,14,-1,14,6,5,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,12,-1,12,4,11,-1,12,20,21,-1,21,13,12,-1,13,21,22,-1,22,14,13,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,20,-1,20,12,19,-1,20,28,29,-1,29,21,20,-1,21,29,30,-1,30,22,21,-1,22,30,31,-1,31,23,22,-1,23,31,32,-1,32,24,23,-1,24,32,33,-1,33,25,24,-1,25,33,34,-1,34,26,25,-1,26,34,35,-1,35,27,26,-1,27,35,28,-1,28,20,27,-1,36,29,28,-1,36,30,29,-1,36,31,30,-1,36,32,31,-1,36,33,32,-1,36,34,33,-1,36,35,34,-1,36,28,35,-1]
IndexedFaceSet948.creaseAngle = 3.14159
IndexedFaceSet948.texCoordIndex = [0,3,2,-1,2,1,0,-1,0,5,4,-1,0,4,6,-1,6,3,0,-1,3,6,7,-1,3,7,8,-1,8,2,3,-1,2,8,9,-1,2,9,10,-1,10,1,2,-1,1,10,11,-1,1,11,5,-1,5,0,1,-1,5,13,12,-1,12,4,5,-1,4,12,14,-1,14,6,4,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,13,-1,13,5,11,-1,13,21,20,-1,20,12,13,-1,12,20,22,-1,22,14,12,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,21,-1,21,13,19,-1,21,29,28,-1,28,20,21,-1,20,28,30,-1,30,22,20,-1,22,30,31,-1,31,23,22,-1,23,31,32,-1,32,24,23,-1,24,32,33,-1,33,25,24,-1,25,33,34,-1,34,26,25,-1,26,34,35,-1,35,27,26,-1,27,35,29,-1,29,21,27,-1,36,28,29,-1,36,30,28,-1,36,31,30,-1,36,32,31,-1,36,33,32,-1,36,34,33,-1,36,35,34,-1,36,29,35,-1]
Coordinate949 = x3d.Coordinate()

IndexedFaceSet948.coord = Coordinate949
TextureCoordinate950 = x3d.TextureCoordinate()

IndexedFaceSet948.texCoord = TextureCoordinate950

Shape944.geometry = IndexedFaceSet948

Transform943.children.append(Shape944)

HAnimSegment942.children.append(Transform943)

HAnimJoint941.children.append(HAnimSegment942)
HAnimJoint951 = x3d.HAnimJoint()
HAnimJoint951.name = "r_carpal_proximal_interphalangeal_5"
HAnimJoint951.DEF = "hanim_r_carpal_proximal_interphalangeal_5"
HAnimJoint951.center = [-8.338,26.780001,-1.768]
HAnimJoint951.ulimit = [0,0,0]
HAnimJoint951.llimit = [0,0,0]
HAnimSegment952 = x3d.HAnimSegment()
HAnimSegment952.name = "r_carpal_middle_phalanx_5"
HAnimSegment952.DEF = "hanim_r_carpal_middle_phalanx_5"
Transform953 = x3d.Transform()
Transform953.translation = [-8.338,26.780001,-1.768]
Shape954 = x3d.Shape()
Appearance955 = x3d.Appearance()
Material956 = x3d.Material()
Material956.diffuseColor = [0.588,0.588,0.588]

Appearance955.material = Material956
ImageTexture957 = x3d.ImageTexture()
ImageTexture957.USE = "JinLOA3TextureAtlas"

Appearance955.texture = ImageTexture957

Shape954.appearance = Appearance955
IndexedFaceSet958 = x3d.IndexedFaceSet()
IndexedFaceSet958.coordIndex = [0,2,3,-1,3,1,0,-1,0,4,5,-1,0,5,6,-1,6,2,0,-1,2,6,7,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,3,9,10,-1,10,1,3,-1,1,10,11,-1,1,11,4,-1,4,0,1,-1,4,12,13,-1,13,5,4,-1,5,13,14,-1,14,6,5,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,12,-1,12,4,11,-1,12,20,21,-1,21,13,12,-1,13,21,22,-1,22,14,13,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,20,-1,20,12,19,-1,28,21,20,-1,28,22,21,-1,28,23,22,-1,28,24,23,-1,28,25,24,-1,28,26,25,-1,28,27,26,-1,28,20,27,-1]
IndexedFaceSet958.creaseAngle = 3.14159
IndexedFaceSet958.texCoordIndex = [0,3,2,-1,2,1,0,-1,0,5,4,-1,0,4,6,-1,6,3,0,-1,3,6,7,-1,3,7,8,-1,8,2,3,-1,2,8,9,-1,2,9,10,-1,10,1,2,-1,1,10,11,-1,1,11,5,-1,5,0,1,-1,5,13,12,-1,12,4,5,-1,4,12,14,-1,14,6,4,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,13,-1,13,5,11,-1,13,21,20,-1,20,12,13,-1,12,20,22,-1,22,14,12,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,21,-1,21,13,19,-1,28,20,21,-1,28,22,20,-1,28,23,22,-1,28,24,23,-1,28,25,24,-1,28,26,25,-1,28,27,26,-1,28,21,27,-1]
Coordinate959 = x3d.Coordinate()

IndexedFaceSet958.coord = Coordinate959
TextureCoordinate960 = x3d.TextureCoordinate()

IndexedFaceSet958.texCoord = TextureCoordinate960

Shape954.geometry = IndexedFaceSet958

Transform953.children.append(Shape954)

HAnimSegment952.children.append(Transform953)

HAnimJoint951.children.append(HAnimSegment952)
HAnimJoint961 = x3d.HAnimJoint()
HAnimJoint961.name = "r_carpal_distal_interphalangeal_5"
HAnimJoint961.DEF = "hanim_r_carpal_distal_interphalangeal_5"
HAnimJoint961.center = [-8.153,26.040001,-1.886]
HAnimJoint961.ulimit = [0,0,0]
HAnimJoint961.llimit = [0,0,0]
HAnimSegment962 = x3d.HAnimSegment()
HAnimSegment962.name = "r_carpal_distal_phalanx_5"
HAnimSegment962.DEF = "hanim_r_carpal_distal_phalanx_5"
Transform963 = x3d.Transform()
Transform963.translation = [-8.153,26.040001,-1.886]
Shape964 = x3d.Shape()
Appearance965 = x3d.Appearance()
Material966 = x3d.Material()
Material966.diffuseColor = [0.588,0.588,0.588]

Appearance965.material = Material966
ImageTexture967 = x3d.ImageTexture()
ImageTexture967.USE = "JinLOA3TextureAtlas"

Appearance965.texture = ImageTexture967

Shape964.appearance = Appearance965
IndexedFaceSet968 = x3d.IndexedFaceSet()
IndexedFaceSet968.coordIndex = [0,2,3,-1,3,1,0,-1,0,4,5,-1,0,5,6,-1,6,2,0,-1,2,6,7,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,3,9,10,-1,10,1,3,-1,1,10,11,-1,1,11,4,-1,4,0,1,-1,4,12,13,-1,13,5,4,-1,5,13,14,-1,14,6,5,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,12,-1,12,4,11,-1,12,20,21,-1,21,13,12,-1,13,21,22,-1,22,14,13,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,20,-1,20,12,19,-1,28,21,20,-1,28,22,21,-1,28,23,22,-1,28,24,23,-1,28,25,24,-1,28,26,25,-1,28,27,26,-1,28,20,27,-1]
IndexedFaceSet968.creaseAngle = 3.14159
IndexedFaceSet968.texCoordIndex = [0,3,2,-1,2,1,0,-1,0,5,4,-1,0,4,6,-1,6,3,0,-1,3,6,7,-1,3,7,8,-1,8,2,3,-1,2,8,9,-1,2,9,10,-1,10,1,2,-1,1,10,11,-1,1,11,5,-1,5,0,1,-1,5,13,12,-1,12,4,5,-1,4,12,14,-1,14,6,4,-1,6,14,15,-1,15,7,6,-1,7,15,16,-1,16,8,7,-1,8,16,17,-1,17,9,8,-1,9,17,18,-1,18,10,9,-1,10,18,19,-1,19,11,10,-1,11,19,13,-1,13,5,11,-1,13,21,20,-1,20,12,13,-1,12,20,22,-1,22,14,12,-1,14,22,23,-1,23,15,14,-1,15,23,24,-1,24,16,15,-1,16,24,25,-1,25,17,16,-1,17,25,26,-1,26,18,17,-1,18,26,27,-1,27,19,18,-1,19,27,21,-1,21,13,19,-1,28,20,21,-1,28,22,20,-1,28,23,22,-1,28,24,23,-1,28,25,24,-1,28,26,25,-1,28,27,26,-1,28,21,27,-1]
Coordinate969 = x3d.Coordinate()

IndexedFaceSet968.coord = Coordinate969
TextureCoordinate970 = x3d.TextureCoordinate()

IndexedFaceSet968.texCoord = TextureCoordinate970

Shape964.geometry = IndexedFaceSet968

Transform963.children.append(Shape964)

HAnimSegment962.children.append(Transform963)

HAnimJoint961.children.append(HAnimSegment962)

HAnimJoint951.children.append(HAnimJoint961)

HAnimJoint941.children.append(HAnimJoint951)

HAnimJoint931.children.append(HAnimJoint941)

HAnimJoint771.children.append(HAnimJoint931)

HAnimJoint761.children.append(HAnimJoint771)

HAnimJoint751.children.append(HAnimJoint761)

HAnimJoint741.children.append(HAnimJoint751)

HAnimJoint731.children.append(HAnimJoint741)

HAnimJoint331.children.append(HAnimJoint731)

HAnimJoint321.children.append(HAnimJoint331)

HAnimJoint311.children.append(HAnimJoint321)

HAnimJoint301.children.append(HAnimJoint311)

HAnimJoint291.children.append(HAnimJoint301)

HAnimJoint281.children.append(HAnimJoint291)

HAnimJoint271.children.append(HAnimJoint281)

HAnimJoint261.children.append(HAnimJoint271)

HAnimJoint251.children.append(HAnimJoint261)

HAnimJoint241.children.append(HAnimJoint251)

HAnimJoint231.children.append(HAnimJoint241)

HAnimJoint221.children.append(HAnimJoint231)

HAnimJoint211.children.append(HAnimJoint221)

HAnimJoint201.children.append(HAnimJoint211)

HAnimJoint191.children.append(HAnimJoint201)

HAnimJoint181.children.append(HAnimJoint191)

HAnimJoint171.children.append(HAnimJoint181)

HAnimJoint31.children.append(HAnimJoint171)

HAnimHumanoid23.skeleton.append(HAnimJoint31)
HAnimJoint971 = x3d.HAnimJoint()
HAnimJoint971.USE = "hanim_humanoid_root"

HAnimHumanoid23.joints.append(HAnimJoint971)
HAnimJoint972 = x3d.HAnimJoint()
HAnimJoint972.USE = "hanim_sacroiliac"

HAnimHumanoid23.joints.append(HAnimJoint972)
HAnimJoint973 = x3d.HAnimJoint()
HAnimJoint973.USE = "hanim_vl5"

HAnimHumanoid23.joints.append(HAnimJoint973)
HAnimJoint974 = x3d.HAnimJoint()
HAnimJoint974.USE = "hanim_vl4"

HAnimHumanoid23.joints.append(HAnimJoint974)
HAnimJoint975 = x3d.HAnimJoint()
HAnimJoint975.USE = "hanim_vl3"

HAnimHumanoid23.joints.append(HAnimJoint975)
HAnimJoint976 = x3d.HAnimJoint()
HAnimJoint976.USE = "hanim_vl2"

HAnimHumanoid23.joints.append(HAnimJoint976)
HAnimJoint977 = x3d.HAnimJoint()
HAnimJoint977.USE = "hanim_vl1"

HAnimHumanoid23.joints.append(HAnimJoint977)
HAnimJoint978 = x3d.HAnimJoint()
HAnimJoint978.USE = "hanim_vt12"

HAnimHumanoid23.joints.append(HAnimJoint978)
HAnimJoint979 = x3d.HAnimJoint()
HAnimJoint979.USE = "hanim_vt11"

HAnimHumanoid23.joints.append(HAnimJoint979)
HAnimJoint980 = x3d.HAnimJoint()
HAnimJoint980.USE = "hanim_vt10"

HAnimHumanoid23.joints.append(HAnimJoint980)
HAnimJoint981 = x3d.HAnimJoint()
HAnimJoint981.USE = "hanim_vt9"

HAnimHumanoid23.joints.append(HAnimJoint981)
HAnimJoint982 = x3d.HAnimJoint()
HAnimJoint982.USE = "hanim_vt8"

HAnimHumanoid23.joints.append(HAnimJoint982)
HAnimJoint983 = x3d.HAnimJoint()
HAnimJoint983.USE = "hanim_vt7"

HAnimHumanoid23.joints.append(HAnimJoint983)
HAnimJoint984 = x3d.HAnimJoint()
HAnimJoint984.USE = "hanim_vt6"

HAnimHumanoid23.joints.append(HAnimJoint984)
HAnimJoint985 = x3d.HAnimJoint()
HAnimJoint985.USE = "hanim_vt5"

HAnimHumanoid23.joints.append(HAnimJoint985)
HAnimJoint986 = x3d.HAnimJoint()
HAnimJoint986.USE = "hanim_vt4"

HAnimHumanoid23.joints.append(HAnimJoint986)
HAnimJoint987 = x3d.HAnimJoint()
HAnimJoint987.USE = "hanim_vt3"

HAnimHumanoid23.joints.append(HAnimJoint987)
HAnimJoint988 = x3d.HAnimJoint()
HAnimJoint988.USE = "hanim_vt2"

HAnimHumanoid23.joints.append(HAnimJoint988)
HAnimJoint989 = x3d.HAnimJoint()
HAnimJoint989.USE = "hanim_vt1"

HAnimHumanoid23.joints.append(HAnimJoint989)
HAnimJoint990 = x3d.HAnimJoint()
HAnimJoint990.USE = "hanim_vc7"

HAnimHumanoid23.joints.append(HAnimJoint990)
HAnimJoint991 = x3d.HAnimJoint()
HAnimJoint991.USE = "hanim_vc6"

HAnimHumanoid23.joints.append(HAnimJoint991)
HAnimJoint992 = x3d.HAnimJoint()
HAnimJoint992.USE = "hanim_vc5"

HAnimHumanoid23.joints.append(HAnimJoint992)
HAnimJoint993 = x3d.HAnimJoint()
HAnimJoint993.USE = "hanim_vc4"

HAnimHumanoid23.joints.append(HAnimJoint993)
HAnimJoint994 = x3d.HAnimJoint()
HAnimJoint994.USE = "hanim_vc3"

HAnimHumanoid23.joints.append(HAnimJoint994)
HAnimJoint995 = x3d.HAnimJoint()
HAnimJoint995.USE = "hanim_vc2"

HAnimHumanoid23.joints.append(HAnimJoint995)
HAnimJoint996 = x3d.HAnimJoint()
HAnimJoint996.USE = "hanim_vc1"

HAnimHumanoid23.joints.append(HAnimJoint996)
HAnimJoint997 = x3d.HAnimJoint()
HAnimJoint997.USE = "hanim_skullbase"

HAnimHumanoid23.joints.append(HAnimJoint997)
HAnimJoint998 = x3d.HAnimJoint()
HAnimJoint998.USE = "hanim_temporomandibular"

HAnimHumanoid23.joints.append(HAnimJoint998)
HAnimJoint999 = x3d.HAnimJoint()
HAnimJoint999.USE = "hanim_l_acromioclavicular"

HAnimHumanoid23.joints.append(HAnimJoint999)
HAnimJoint1000 = x3d.HAnimJoint()
HAnimJoint1000.USE = "hanim_r_acromioclavicular"

HAnimHumanoid23.joints.append(HAnimJoint1000)
HAnimJoint1001 = x3d.HAnimJoint()
HAnimJoint1001.USE = "hanim_l_carpal_distal_interphalangeal_2"

HAnimHumanoid23.joints.append(HAnimJoint1001)
HAnimJoint1002 = x3d.HAnimJoint()
HAnimJoint1002.USE = "hanim_r_carpal_distal_interphalangeal_2"

HAnimHumanoid23.joints.append(HAnimJoint1002)
HAnimJoint1003 = x3d.HAnimJoint()
HAnimJoint1003.USE = "hanim_l_carpal_distal_interphalangeal_3"

HAnimHumanoid23.joints.append(HAnimJoint1003)
HAnimJoint1004 = x3d.HAnimJoint()
HAnimJoint1004.USE = "hanim_r_carpal_distal_interphalangeal_3"

HAnimHumanoid23.joints.append(HAnimJoint1004)
HAnimJoint1005 = x3d.HAnimJoint()
HAnimJoint1005.USE = "hanim_l_carpal_distal_interphalangeal_4"

HAnimHumanoid23.joints.append(HAnimJoint1005)
HAnimJoint1006 = x3d.HAnimJoint()
HAnimJoint1006.USE = "hanim_r_carpal_distal_interphalangeal_4"

HAnimHumanoid23.joints.append(HAnimJoint1006)
HAnimJoint1007 = x3d.HAnimJoint()
HAnimJoint1007.USE = "hanim_l_carpal_distal_interphalangeal_5"

HAnimHumanoid23.joints.append(HAnimJoint1007)
HAnimJoint1008 = x3d.HAnimJoint()
HAnimJoint1008.USE = "hanim_r_carpal_distal_interphalangeal_5"

HAnimHumanoid23.joints.append(HAnimJoint1008)
HAnimJoint1009 = x3d.HAnimJoint()
HAnimJoint1009.USE = "hanim_l_carpal_interphalangeal_1"

HAnimHumanoid23.joints.append(HAnimJoint1009)
HAnimJoint1010 = x3d.HAnimJoint()
HAnimJoint1010.USE = "hanim_r_carpal_interphalangeal_1"

HAnimHumanoid23.joints.append(HAnimJoint1010)
HAnimJoint1011 = x3d.HAnimJoint()
HAnimJoint1011.USE = "hanim_l_carpal_proximal_interphalangeal_2"

HAnimHumanoid23.joints.append(HAnimJoint1011)
HAnimJoint1012 = x3d.HAnimJoint()
HAnimJoint1012.USE = "hanim_r_carpal_proximal_interphalangeal_2"

HAnimHumanoid23.joints.append(HAnimJoint1012)
HAnimJoint1013 = x3d.HAnimJoint()
HAnimJoint1013.USE = "hanim_l_carpal_proximal_interphalangeal_3"

HAnimHumanoid23.joints.append(HAnimJoint1013)
HAnimJoint1014 = x3d.HAnimJoint()
HAnimJoint1014.USE = "hanim_r_carpal_proximal_interphalangeal_3"

HAnimHumanoid23.joints.append(HAnimJoint1014)
HAnimJoint1015 = x3d.HAnimJoint()
HAnimJoint1015.USE = "hanim_l_carpal_proximal_interphalangeal_4"

HAnimHumanoid23.joints.append(HAnimJoint1015)
HAnimJoint1016 = x3d.HAnimJoint()
HAnimJoint1016.USE = "hanim_r_carpal_proximal_interphalangeal_4"

HAnimHumanoid23.joints.append(HAnimJoint1016)
HAnimJoint1017 = x3d.HAnimJoint()
HAnimJoint1017.USE = "hanim_l_carpal_proximal_interphalangeal_5"

HAnimHumanoid23.joints.append(HAnimJoint1017)
HAnimJoint1018 = x3d.HAnimJoint()
HAnimJoint1018.USE = "hanim_r_carpal_proximal_interphalangeal_5"

HAnimHumanoid23.joints.append(HAnimJoint1018)
HAnimJoint1019 = x3d.HAnimJoint()
HAnimJoint1019.USE = "hanim_l_carpometacarpal_1"

HAnimHumanoid23.joints.append(HAnimJoint1019)
HAnimJoint1020 = x3d.HAnimJoint()
HAnimJoint1020.USE = "hanim_r_carpometacarpal_1"

HAnimHumanoid23.joints.append(HAnimJoint1020)
HAnimJoint1021 = x3d.HAnimJoint()
HAnimJoint1021.USE = "hanim_l_carpometacarpal_2"

HAnimHumanoid23.joints.append(HAnimJoint1021)
HAnimJoint1022 = x3d.HAnimJoint()
HAnimJoint1022.USE = "hanim_r_carpometacarpal_2"

HAnimHumanoid23.joints.append(HAnimJoint1022)
HAnimJoint1023 = x3d.HAnimJoint()
HAnimJoint1023.USE = "hanim_l_carpometacarpal_3"

HAnimHumanoid23.joints.append(HAnimJoint1023)
HAnimJoint1024 = x3d.HAnimJoint()
HAnimJoint1024.USE = "hanim_r_carpometacarpal_3"

HAnimHumanoid23.joints.append(HAnimJoint1024)
HAnimJoint1025 = x3d.HAnimJoint()
HAnimJoint1025.USE = "hanim_l_carpometacarpal_4"

HAnimHumanoid23.joints.append(HAnimJoint1025)
HAnimJoint1026 = x3d.HAnimJoint()
HAnimJoint1026.USE = "hanim_r_carpometacarpal_4"

HAnimHumanoid23.joints.append(HAnimJoint1026)
HAnimJoint1027 = x3d.HAnimJoint()
HAnimJoint1027.USE = "hanim_l_carpometacarpal_5"

HAnimHumanoid23.joints.append(HAnimJoint1027)
HAnimJoint1028 = x3d.HAnimJoint()
HAnimJoint1028.USE = "hanim_r_carpometacarpal_5"

HAnimHumanoid23.joints.append(HAnimJoint1028)
HAnimJoint1029 = x3d.HAnimJoint()
HAnimJoint1029.USE = "hanim_l_elbow"

HAnimHumanoid23.joints.append(HAnimJoint1029)
HAnimJoint1030 = x3d.HAnimJoint()
HAnimJoint1030.USE = "hanim_r_elbow"

HAnimHumanoid23.joints.append(HAnimJoint1030)
HAnimJoint1031 = x3d.HAnimJoint()
HAnimJoint1031.USE = "hanim_l_eyeball_joint"

HAnimHumanoid23.joints.append(HAnimJoint1031)
HAnimJoint1032 = x3d.HAnimJoint()
HAnimJoint1032.USE = "hanim_r_eyeball_joint"

HAnimHumanoid23.joints.append(HAnimJoint1032)
HAnimJoint1033 = x3d.HAnimJoint()
HAnimJoint1033.USE = "hanim_l_eyebrow_joint"

HAnimHumanoid23.joints.append(HAnimJoint1033)
HAnimJoint1034 = x3d.HAnimJoint()
HAnimJoint1034.USE = "hanim_r_eyebrow_joint"

HAnimHumanoid23.joints.append(HAnimJoint1034)
HAnimJoint1035 = x3d.HAnimJoint()
HAnimJoint1035.USE = "hanim_l_eyelid_joint"

HAnimHumanoid23.joints.append(HAnimJoint1035)
HAnimJoint1036 = x3d.HAnimJoint()
HAnimJoint1036.USE = "hanim_r_eyelid_joint"

HAnimHumanoid23.joints.append(HAnimJoint1036)
HAnimJoint1037 = x3d.HAnimJoint()
HAnimJoint1037.USE = "hanim_l_hip"

HAnimHumanoid23.joints.append(HAnimJoint1037)
HAnimJoint1038 = x3d.HAnimJoint()
HAnimJoint1038.USE = "hanim_r_hip"

HAnimHumanoid23.joints.append(HAnimJoint1038)
HAnimJoint1039 = x3d.HAnimJoint()
HAnimJoint1039.USE = "hanim_l_knee"

HAnimHumanoid23.joints.append(HAnimJoint1039)
HAnimJoint1040 = x3d.HAnimJoint()
HAnimJoint1040.USE = "hanim_r_knee"

HAnimHumanoid23.joints.append(HAnimJoint1040)
HAnimJoint1041 = x3d.HAnimJoint()
HAnimJoint1041.USE = "hanim_l_metacarpophalangeal_1"

HAnimHumanoid23.joints.append(HAnimJoint1041)
HAnimJoint1042 = x3d.HAnimJoint()
HAnimJoint1042.USE = "hanim_r_metacarpophalangeal_1"

HAnimHumanoid23.joints.append(HAnimJoint1042)
HAnimJoint1043 = x3d.HAnimJoint()
HAnimJoint1043.USE = "hanim_l_metacarpophalangeal_2"

HAnimHumanoid23.joints.append(HAnimJoint1043)
HAnimJoint1044 = x3d.HAnimJoint()
HAnimJoint1044.USE = "hanim_r_metacarpophalangeal_2"

HAnimHumanoid23.joints.append(HAnimJoint1044)
HAnimJoint1045 = x3d.HAnimJoint()
HAnimJoint1045.USE = "hanim_l_metacarpophalangeal_3"

HAnimHumanoid23.joints.append(HAnimJoint1045)
HAnimJoint1046 = x3d.HAnimJoint()
HAnimJoint1046.USE = "hanim_r_metacarpophalangeal_3"

HAnimHumanoid23.joints.append(HAnimJoint1046)
HAnimJoint1047 = x3d.HAnimJoint()
HAnimJoint1047.USE = "hanim_l_metacarpophalangeal_4"

HAnimHumanoid23.joints.append(HAnimJoint1047)
HAnimJoint1048 = x3d.HAnimJoint()
HAnimJoint1048.USE = "hanim_r_metacarpophalangeal_4"

HAnimHumanoid23.joints.append(HAnimJoint1048)
HAnimJoint1049 = x3d.HAnimJoint()
HAnimJoint1049.USE = "hanim_l_metacarpophalangeal_5"

HAnimHumanoid23.joints.append(HAnimJoint1049)
HAnimJoint1050 = x3d.HAnimJoint()
HAnimJoint1050.USE = "hanim_r_metacarpophalangeal_5"

HAnimHumanoid23.joints.append(HAnimJoint1050)
HAnimJoint1051 = x3d.HAnimJoint()
HAnimJoint1051.USE = "hanim_l_metatarsophalangeal_2"

HAnimHumanoid23.joints.append(HAnimJoint1051)
HAnimJoint1052 = x3d.HAnimJoint()
HAnimJoint1052.USE = "hanim_r_metatarsophalangeal_2"

HAnimHumanoid23.joints.append(HAnimJoint1052)
HAnimJoint1053 = x3d.HAnimJoint()
HAnimJoint1053.USE = "hanim_l_radiocarpal"

HAnimHumanoid23.joints.append(HAnimJoint1053)
HAnimJoint1054 = x3d.HAnimJoint()
HAnimJoint1054.USE = "hanim_r_radiocarpal"

HAnimHumanoid23.joints.append(HAnimJoint1054)
HAnimJoint1055 = x3d.HAnimJoint()
HAnimJoint1055.USE = "hanim_l_shoulder"

HAnimHumanoid23.joints.append(HAnimJoint1055)
HAnimJoint1056 = x3d.HAnimJoint()
HAnimJoint1056.USE = "hanim_r_shoulder"

HAnimHumanoid23.joints.append(HAnimJoint1056)
HAnimJoint1057 = x3d.HAnimJoint()
HAnimJoint1057.USE = "hanim_l_sternoclavicular"

HAnimHumanoid23.joints.append(HAnimJoint1057)
HAnimJoint1058 = x3d.HAnimJoint()
HAnimJoint1058.USE = "hanim_r_sternoclavicular"

HAnimHumanoid23.joints.append(HAnimJoint1058)
HAnimJoint1059 = x3d.HAnimJoint()
HAnimJoint1059.USE = "hanim_l_talocrural"

HAnimHumanoid23.joints.append(HAnimJoint1059)
HAnimJoint1060 = x3d.HAnimJoint()
HAnimJoint1060.USE = "hanim_r_talocrural"

HAnimHumanoid23.joints.append(HAnimJoint1060)
HAnimJoint1061 = x3d.HAnimJoint()
HAnimJoint1061.USE = "hanim_l_tarsal_distal_interphalangeal_2"

HAnimHumanoid23.joints.append(HAnimJoint1061)
HAnimJoint1062 = x3d.HAnimJoint()
HAnimJoint1062.USE = "hanim_r_tarsal_distal_interphalangeal_2"

HAnimHumanoid23.joints.append(HAnimJoint1062)
HAnimJoint1063 = x3d.HAnimJoint()
HAnimJoint1063.USE = "hanim_l_tarsometatarsal_2"

HAnimHumanoid23.joints.append(HAnimJoint1063)
HAnimJoint1064 = x3d.HAnimJoint()
HAnimJoint1064.USE = "hanim_r_tarsometatarsal_2"

HAnimHumanoid23.joints.append(HAnimJoint1064)
HAnimSegment1065 = x3d.HAnimSegment()
HAnimSegment1065.USE = "hanim_sacrum"

HAnimHumanoid23.segments.append(HAnimSegment1065)
HAnimSegment1066 = x3d.HAnimSegment()
HAnimSegment1066.USE = "hanim_pelvis"

HAnimHumanoid23.segments.append(HAnimSegment1066)
HAnimSegment1067 = x3d.HAnimSegment()
HAnimSegment1067.USE = "hanim_l5"

HAnimHumanoid23.segments.append(HAnimSegment1067)
HAnimSegment1068 = x3d.HAnimSegment()
HAnimSegment1068.USE = "hanim_l4"

HAnimHumanoid23.segments.append(HAnimSegment1068)
HAnimSegment1069 = x3d.HAnimSegment()
HAnimSegment1069.USE = "hanim_l3"

HAnimHumanoid23.segments.append(HAnimSegment1069)
HAnimSegment1070 = x3d.HAnimSegment()
HAnimSegment1070.USE = "hanim_l2"

HAnimHumanoid23.segments.append(HAnimSegment1070)
HAnimSegment1071 = x3d.HAnimSegment()
HAnimSegment1071.USE = "hanim_l1"

HAnimHumanoid23.segments.append(HAnimSegment1071)
HAnimSegment1072 = x3d.HAnimSegment()
HAnimSegment1072.USE = "hanim_t12"

HAnimHumanoid23.segments.append(HAnimSegment1072)
HAnimSegment1073 = x3d.HAnimSegment()
HAnimSegment1073.USE = "hanim_t11"

HAnimHumanoid23.segments.append(HAnimSegment1073)
HAnimSegment1074 = x3d.HAnimSegment()
HAnimSegment1074.USE = "hanim_t10"

HAnimHumanoid23.segments.append(HAnimSegment1074)
HAnimSegment1075 = x3d.HAnimSegment()
HAnimSegment1075.USE = "hanim_t9"

HAnimHumanoid23.segments.append(HAnimSegment1075)
HAnimSegment1076 = x3d.HAnimSegment()
HAnimSegment1076.USE = "hanim_t8"

HAnimHumanoid23.segments.append(HAnimSegment1076)
HAnimSegment1077 = x3d.HAnimSegment()
HAnimSegment1077.USE = "hanim_t7"

HAnimHumanoid23.segments.append(HAnimSegment1077)
HAnimSegment1078 = x3d.HAnimSegment()
HAnimSegment1078.USE = "hanim_t6"

HAnimHumanoid23.segments.append(HAnimSegment1078)
HAnimSegment1079 = x3d.HAnimSegment()
HAnimSegment1079.USE = "hanim_t5"

HAnimHumanoid23.segments.append(HAnimSegment1079)
HAnimSegment1080 = x3d.HAnimSegment()
HAnimSegment1080.USE = "hanim_t4"

HAnimHumanoid23.segments.append(HAnimSegment1080)
HAnimSegment1081 = x3d.HAnimSegment()
HAnimSegment1081.USE = "hanim_t3"

HAnimHumanoid23.segments.append(HAnimSegment1081)
HAnimSegment1082 = x3d.HAnimSegment()
HAnimSegment1082.USE = "hanim_t2"

HAnimHumanoid23.segments.append(HAnimSegment1082)
HAnimSegment1083 = x3d.HAnimSegment()
HAnimSegment1083.USE = "hanim_t1"

HAnimHumanoid23.segments.append(HAnimSegment1083)
HAnimSegment1084 = x3d.HAnimSegment()
HAnimSegment1084.USE = "hanim_c7"

HAnimHumanoid23.segments.append(HAnimSegment1084)
HAnimSegment1085 = x3d.HAnimSegment()
HAnimSegment1085.USE = "hanim_c6"

HAnimHumanoid23.segments.append(HAnimSegment1085)
HAnimSegment1086 = x3d.HAnimSegment()
HAnimSegment1086.USE = "hanim_c5"

HAnimHumanoid23.segments.append(HAnimSegment1086)
HAnimSegment1087 = x3d.HAnimSegment()
HAnimSegment1087.USE = "hanim_c4"

HAnimHumanoid23.segments.append(HAnimSegment1087)
HAnimSegment1088 = x3d.HAnimSegment()
HAnimSegment1088.USE = "hanim_c3"

HAnimHumanoid23.segments.append(HAnimSegment1088)
HAnimSegment1089 = x3d.HAnimSegment()
HAnimSegment1089.USE = "hanim_c2"

HAnimHumanoid23.segments.append(HAnimSegment1089)
HAnimSegment1090 = x3d.HAnimSegment()
HAnimSegment1090.USE = "hanim_c1"

HAnimHumanoid23.segments.append(HAnimSegment1090)
HAnimSegment1091 = x3d.HAnimSegment()
HAnimSegment1091.USE = "hanim_skull"

HAnimHumanoid23.segments.append(HAnimSegment1091)
HAnimSegment1092 = x3d.HAnimSegment()
HAnimSegment1092.USE = "hanim_jaw"

HAnimHumanoid23.segments.append(HAnimSegment1092)
HAnimSegment1093 = x3d.HAnimSegment()
HAnimSegment1093.USE = "hanim_l_calf"

HAnimHumanoid23.segments.append(HAnimSegment1093)
HAnimSegment1094 = x3d.HAnimSegment()
HAnimSegment1094.USE = "hanim_r_calf"

HAnimHumanoid23.segments.append(HAnimSegment1094)
HAnimSegment1095 = x3d.HAnimSegment()
HAnimSegment1095.USE = "hanim_l_carpal"

HAnimHumanoid23.segments.append(HAnimSegment1095)
HAnimSegment1096 = x3d.HAnimSegment()
HAnimSegment1096.USE = "hanim_r_carpal"

HAnimHumanoid23.segments.append(HAnimSegment1096)
HAnimSegment1097 = x3d.HAnimSegment()
HAnimSegment1097.USE = "hanim_l_carpal_distal_phalanx_1"

HAnimHumanoid23.segments.append(HAnimSegment1097)
HAnimSegment1098 = x3d.HAnimSegment()
HAnimSegment1098.USE = "hanim_r_carpal_distal_phalanx_1"

HAnimHumanoid23.segments.append(HAnimSegment1098)
HAnimSegment1099 = x3d.HAnimSegment()
HAnimSegment1099.USE = "hanim_l_carpal_distal_phalanx_2"

HAnimHumanoid23.segments.append(HAnimSegment1099)
HAnimSegment1100 = x3d.HAnimSegment()
HAnimSegment1100.USE = "hanim_r_carpal_distal_phalanx_2"

HAnimHumanoid23.segments.append(HAnimSegment1100)
HAnimSegment1101 = x3d.HAnimSegment()
HAnimSegment1101.USE = "hanim_l_carpal_distal_phalanx_3"

HAnimHumanoid23.segments.append(HAnimSegment1101)
HAnimSegment1102 = x3d.HAnimSegment()
HAnimSegment1102.USE = "hanim_r_carpal_distal_phalanx_3"

HAnimHumanoid23.segments.append(HAnimSegment1102)
HAnimSegment1103 = x3d.HAnimSegment()
HAnimSegment1103.USE = "hanim_l_carpal_distal_phalanx_4"

HAnimHumanoid23.segments.append(HAnimSegment1103)
HAnimSegment1104 = x3d.HAnimSegment()
HAnimSegment1104.USE = "hanim_r_carpal_distal_phalanx_4"

HAnimHumanoid23.segments.append(HAnimSegment1104)
HAnimSegment1105 = x3d.HAnimSegment()
HAnimSegment1105.USE = "hanim_l_carpal_distal_phalanx_5"

HAnimHumanoid23.segments.append(HAnimSegment1105)
HAnimSegment1106 = x3d.HAnimSegment()
HAnimSegment1106.USE = "hanim_r_carpal_distal_phalanx_5"

HAnimHumanoid23.segments.append(HAnimSegment1106)
HAnimSegment1107 = x3d.HAnimSegment()
HAnimSegment1107.USE = "hanim_l_carpal_middle_phalanx_2"

HAnimHumanoid23.segments.append(HAnimSegment1107)
HAnimSegment1108 = x3d.HAnimSegment()
HAnimSegment1108.USE = "hanim_r_carpal_middle_phalanx_2"

HAnimHumanoid23.segments.append(HAnimSegment1108)
HAnimSegment1109 = x3d.HAnimSegment()
HAnimSegment1109.USE = "hanim_l_carpal_middle_phalanx_3"

HAnimHumanoid23.segments.append(HAnimSegment1109)
HAnimSegment1110 = x3d.HAnimSegment()
HAnimSegment1110.USE = "hanim_r_carpal_middle_phalanx_3"

HAnimHumanoid23.segments.append(HAnimSegment1110)
HAnimSegment1111 = x3d.HAnimSegment()
HAnimSegment1111.USE = "hanim_l_carpal_middle_phalanx_4"

HAnimHumanoid23.segments.append(HAnimSegment1111)
HAnimSegment1112 = x3d.HAnimSegment()
HAnimSegment1112.USE = "hanim_r_carpal_middle_phalanx_4"

HAnimHumanoid23.segments.append(HAnimSegment1112)
HAnimSegment1113 = x3d.HAnimSegment()
HAnimSegment1113.USE = "hanim_l_carpal_middle_phalanx_5"

HAnimHumanoid23.segments.append(HAnimSegment1113)
HAnimSegment1114 = x3d.HAnimSegment()
HAnimSegment1114.USE = "hanim_r_carpal_middle_phalanx_5"

HAnimHumanoid23.segments.append(HAnimSegment1114)
HAnimSegment1115 = x3d.HAnimSegment()
HAnimSegment1115.USE = "hanim_l_carpal_proximal_phalanx_1"

HAnimHumanoid23.segments.append(HAnimSegment1115)
HAnimSegment1116 = x3d.HAnimSegment()
HAnimSegment1116.USE = "hanim_r_carpal_proximal_phalanx_1"

HAnimHumanoid23.segments.append(HAnimSegment1116)
HAnimSegment1117 = x3d.HAnimSegment()
HAnimSegment1117.USE = "hanim_l_carpal_proximal_phalanx_2"

HAnimHumanoid23.segments.append(HAnimSegment1117)
HAnimSegment1118 = x3d.HAnimSegment()
HAnimSegment1118.USE = "hanim_r_carpal_proximal_phalanx_2"

HAnimHumanoid23.segments.append(HAnimSegment1118)
HAnimSegment1119 = x3d.HAnimSegment()
HAnimSegment1119.USE = "hanim_l_carpal_proximal_phalanx_3"

HAnimHumanoid23.segments.append(HAnimSegment1119)
HAnimSegment1120 = x3d.HAnimSegment()
HAnimSegment1120.USE = "hanim_r_carpal_proximal_phalanx_3"

HAnimHumanoid23.segments.append(HAnimSegment1120)
HAnimSegment1121 = x3d.HAnimSegment()
HAnimSegment1121.USE = "hanim_l_carpal_proximal_phalanx_4"

HAnimHumanoid23.segments.append(HAnimSegment1121)
HAnimSegment1122 = x3d.HAnimSegment()
HAnimSegment1122.USE = "hanim_r_carpal_proximal_phalanx_4"

HAnimHumanoid23.segments.append(HAnimSegment1122)
HAnimSegment1123 = x3d.HAnimSegment()
HAnimSegment1123.USE = "hanim_l_carpal_proximal_phalanx_5"

HAnimHumanoid23.segments.append(HAnimSegment1123)
HAnimSegment1124 = x3d.HAnimSegment()
HAnimSegment1124.USE = "hanim_r_carpal_proximal_phalanx_5"

HAnimHumanoid23.segments.append(HAnimSegment1124)
HAnimSegment1125 = x3d.HAnimSegment()
HAnimSegment1125.USE = "hanim_l_clavicle"

HAnimHumanoid23.segments.append(HAnimSegment1125)
HAnimSegment1126 = x3d.HAnimSegment()
HAnimSegment1126.USE = "hanim_r_clavicle"

HAnimHumanoid23.segments.append(HAnimSegment1126)
HAnimSegment1127 = x3d.HAnimSegment()
HAnimSegment1127.USE = "hanim_l_eyeball"

HAnimHumanoid23.segments.append(HAnimSegment1127)
HAnimSegment1128 = x3d.HAnimSegment()
HAnimSegment1128.USE = "hanim_r_eyeball"

HAnimHumanoid23.segments.append(HAnimSegment1128)
HAnimSegment1129 = x3d.HAnimSegment()
HAnimSegment1129.USE = "hanim_l_eyebrow"

HAnimHumanoid23.segments.append(HAnimSegment1129)
HAnimSegment1130 = x3d.HAnimSegment()
HAnimSegment1130.USE = "hanim_r_eyebrow"

HAnimHumanoid23.segments.append(HAnimSegment1130)
HAnimSegment1131 = x3d.HAnimSegment()
HAnimSegment1131.USE = "hanim_l_eyelid"

HAnimHumanoid23.segments.append(HAnimSegment1131)
HAnimSegment1132 = x3d.HAnimSegment()
HAnimSegment1132.USE = "hanim_r_eyelid"

HAnimHumanoid23.segments.append(HAnimSegment1132)
HAnimSegment1133 = x3d.HAnimSegment()
HAnimSegment1133.USE = "hanim_l_forearm"

HAnimHumanoid23.segments.append(HAnimSegment1133)
HAnimSegment1134 = x3d.HAnimSegment()
HAnimSegment1134.USE = "hanim_r_forearm"

HAnimHumanoid23.segments.append(HAnimSegment1134)
HAnimSegment1135 = x3d.HAnimSegment()
HAnimSegment1135.USE = "hanim_l_metacarpal_1"

HAnimHumanoid23.segments.append(HAnimSegment1135)
HAnimSegment1136 = x3d.HAnimSegment()
HAnimSegment1136.USE = "hanim_r_metacarpal_1"

HAnimHumanoid23.segments.append(HAnimSegment1136)
HAnimSegment1137 = x3d.HAnimSegment()
HAnimSegment1137.USE = "hanim_l_metacarpal_2"

HAnimHumanoid23.segments.append(HAnimSegment1137)
HAnimSegment1138 = x3d.HAnimSegment()
HAnimSegment1138.USE = "hanim_r_metacarpal_2"

HAnimHumanoid23.segments.append(HAnimSegment1138)
HAnimSegment1139 = x3d.HAnimSegment()
HAnimSegment1139.USE = "hanim_l_metacarpal_3"

HAnimHumanoid23.segments.append(HAnimSegment1139)
HAnimSegment1140 = x3d.HAnimSegment()
HAnimSegment1140.USE = "hanim_r_metacarpal_3"

HAnimHumanoid23.segments.append(HAnimSegment1140)
HAnimSegment1141 = x3d.HAnimSegment()
HAnimSegment1141.USE = "hanim_l_metacarpal_4"

HAnimHumanoid23.segments.append(HAnimSegment1141)
HAnimSegment1142 = x3d.HAnimSegment()
HAnimSegment1142.USE = "hanim_r_metacarpal_4"

HAnimHumanoid23.segments.append(HAnimSegment1142)
HAnimSegment1143 = x3d.HAnimSegment()
HAnimSegment1143.USE = "hanim_l_metacarpal_5"

HAnimHumanoid23.segments.append(HAnimSegment1143)
HAnimSegment1144 = x3d.HAnimSegment()
HAnimSegment1144.USE = "hanim_r_metacarpal_5"

HAnimHumanoid23.segments.append(HAnimSegment1144)
HAnimSegment1145 = x3d.HAnimSegment()
HAnimSegment1145.USE = "hanim_r_metatarsal_2"

HAnimHumanoid23.segments.append(HAnimSegment1145)
HAnimSegment1146 = x3d.HAnimSegment()
HAnimSegment1146.USE = "hanim_l_metatarsal_2"

HAnimHumanoid23.segments.append(HAnimSegment1146)
HAnimSegment1147 = x3d.HAnimSegment()
HAnimSegment1147.USE = "hanim_l_scapula"

HAnimHumanoid23.segments.append(HAnimSegment1147)
HAnimSegment1148 = x3d.HAnimSegment()
HAnimSegment1148.USE = "hanim_r_scapula"

HAnimHumanoid23.segments.append(HAnimSegment1148)
HAnimSegment1149 = x3d.HAnimSegment()
HAnimSegment1149.USE = "hanim_l_talus"

HAnimHumanoid23.segments.append(HAnimSegment1149)
HAnimSegment1150 = x3d.HAnimSegment()
HAnimSegment1150.USE = "hanim_r_talus"

HAnimHumanoid23.segments.append(HAnimSegment1150)
HAnimSegment1151 = x3d.HAnimSegment()
HAnimSegment1151.USE = "hanim_l_tarsal_distal_phalanx_2"

HAnimHumanoid23.segments.append(HAnimSegment1151)
HAnimSegment1152 = x3d.HAnimSegment()
HAnimSegment1152.USE = "hanim_r_tarsal_distal_phalanx_2"

HAnimHumanoid23.segments.append(HAnimSegment1152)
HAnimSegment1153 = x3d.HAnimSegment()
HAnimSegment1153.USE = "hanim_l_tarsal_proximal_phalanx_2"

HAnimHumanoid23.segments.append(HAnimSegment1153)
HAnimSegment1154 = x3d.HAnimSegment()
HAnimSegment1154.USE = "hanim_r_tarsal_proximal_phalanx_2"

HAnimHumanoid23.segments.append(HAnimSegment1154)
HAnimSegment1155 = x3d.HAnimSegment()
HAnimSegment1155.USE = "hanim_l_thigh"

HAnimHumanoid23.segments.append(HAnimSegment1155)
HAnimSegment1156 = x3d.HAnimSegment()
HAnimSegment1156.USE = "hanim_r_thigh"

HAnimHumanoid23.segments.append(HAnimSegment1156)
HAnimSegment1157 = x3d.HAnimSegment()
HAnimSegment1157.USE = "hanim_l_upperarm"

HAnimHumanoid23.segments.append(HAnimSegment1157)
HAnimSegment1158 = x3d.HAnimSegment()
HAnimSegment1158.USE = "hanim_r_upperarm"

HAnimHumanoid23.segments.append(HAnimSegment1158)

Scene19.children.append(HAnimHumanoid23)

X3D0.Scene = Scene19
f = open("././JinLOA3_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
