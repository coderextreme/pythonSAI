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
meta3.content = "KoreanCharacter03Hyun.x3d"

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
meta13.content = "https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Characters/KoreanCharacter03Hyun.x3d"

head1.children.append(meta13)
meta14 = x3d.meta()
meta14.name = "generator"
meta14.content = "3DS MAX, http://www.autodesk.com/products/autodesk-3ds-max/overview"

head1.children.append(meta14)
meta15 = x3d.meta()
meta15.name = "generator"
meta15.content = "Suwon University HAnim Editor"

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
WorldInfo20.title = "KoreanCharacter03Hyun.x3d"

Scene19.children.append(WorldInfo20)
NavigationInfo21 = x3d.NavigationInfo()
NavigationInfo21.speed = 1.5

Scene19.children.append(NavigationInfo21)
Viewpoint22 = x3d.Viewpoint()
Viewpoint22.centerOfRotation = [0,1,0]
Viewpoint22.description = "Hyun"
Viewpoint22.position = [0,1,3]

Scene19.children.append(Viewpoint22)
HAnimHumanoid23 = x3d.HAnimHumanoid()
HAnimHumanoid23.name = "Hyun"
HAnimHumanoid23.DEF = "hanim_Hyun"
HAnimHumanoid23.scale = [0.0225,0.0225,0.0225]
HAnimHumanoid23.version = "2.0"
#original HAnimHumanoid info='\"authorName=Chul Hee Jung and Myeong Won Lee\" \"authorEmail=myeongwonlee@gmail.com\" \"creationDate=31 March 2011\" \"humanoidVersion=2.0\" \"gender=male\" \"height=1.5\"'
MetadataSet24 = x3d.MetadataSet()
MetadataSet24.name = "HAnimHumanoid.info"
MetadataSet24.reference = "https://www.web3d.org/documents/specifications/19774/V2.0/Architecture/ObjectInterfaces.html#Humanoid"
MetadataString25 = x3d.MetadataString()
MetadataString25.name = "authorName"
MetadataString25.value = ["Chul Hee Jung and Myeong Won Lee"]

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
MetadataString28.value = ["male"]

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
HAnimJoint31.center = [0,31.43,-0.5601]
HAnimJoint31.ulimit = [0,0,0]
HAnimJoint31.llimit = [0,0,0]
HAnimSegment32 = x3d.HAnimSegment()
HAnimSegment32.name = "sacrum"
HAnimSegment32.DEF = "hanim_sacrum"
Transform33 = x3d.Transform()
Transform33.translation = [0,31.43,-0.5601]
Shape34 = x3d.Shape()
Appearance35 = x3d.Appearance()
Material36 = x3d.Material()
Material36.diffuseColor = [0.588,0.588,0.588]

Appearance35.material = Material36
ImageTexture37 = x3d.ImageTexture()
ImageTexture37.DEF = "HyunTextureAtlas"
ImageTexture37.url = ["images/Hyun.png","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Characters/images/Hyun.png"]

Appearance35.texture = ImageTexture37

Shape34.appearance = Appearance35
IndexedFaceSet38 = x3d.IndexedFaceSet()
IndexedFaceSet38.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,5,-1,0,5,6,-1,0,6,7,-1,0,7,8,-1,0,8,9,-1,0,9,10,-1,0,10,11,-1,0,11,12,-1,0,12,1,-1,1,13,14,-1,14,2,1,-1,2,14,15,-1,15,3,2,-1,3,15,16,-1,16,4,3,-1,4,16,17,-1,17,5,4,-1,5,17,18,-1,18,6,5,-1,6,18,19,-1,19,7,6,-1,7,19,20,-1,20,8,7,-1,8,20,21,-1,21,9,8,-1,9,21,22,-1,22,10,9,-1,10,22,23,-1,23,11,10,-1,11,23,24,-1,24,12,11,-1,12,24,13,-1,13,1,12,-1,13,25,26,-1,26,14,13,-1,14,26,27,-1,27,15,14,-1,15,27,28,-1,28,16,15,-1,16,28,29,-1,29,17,16,-1,17,29,30,-1,30,18,17,-1,18,30,31,-1,31,19,18,-1,19,31,32,-1,32,20,19,-1,20,32,33,-1,33,21,20,-1,21,33,34,-1,34,22,21,-1,22,34,35,-1,35,23,22,-1,23,35,36,-1,36,24,23,-1,24,36,25,-1,25,13,24,-1,25,37,38,-1,38,26,25,-1,26,38,39,-1,39,27,26,-1,27,39,40,-1,40,28,27,-1,28,40,41,-1,41,29,28,-1,29,41,42,-1,42,30,29,-1,30,42,43,-1,43,31,30,-1,31,43,44,-1,44,32,31,-1,32,44,45,-1,45,33,32,-1,33,45,46,-1,46,34,33,-1,34,46,47,-1,47,35,34,-1,35,47,48,-1,48,36,35,-1,36,48,37,-1,37,25,36,-1,37,49,50,-1,50,38,37,-1,38,50,51,-1,51,39,38,-1,39,51,52,-1,52,40,39,-1,40,52,53,-1,53,41,40,-1,41,53,54,-1,54,42,41,-1,42,54,55,-1,55,43,42,-1,43,55,56,-1,56,44,43,-1,44,56,57,-1,57,45,44,-1,45,57,58,-1,58,46,45,-1,46,58,59,-1,59,47,46,-1,47,59,60,-1,60,48,47,-1,48,60,49,-1,49,37,48,-1,61,50,49,-1,61,51,50,-1,61,52,51,-1,61,53,52,-1,61,54,53,-1,61,55,54,-1,61,56,55,-1,61,57,56,-1,61,58,57,-1,61,59,58,-1,61,60,59,-1,61,49,60,-1]
IndexedFaceSet38.creaseAngle = 1.57
IndexedFaceSet38.texCoordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,5,-1,0,5,6,-1,0,6,7,-1,0,7,8,-1,0,8,9,-1,0,9,10,-1,0,10,11,-1,0,11,12,-1,0,12,1,-1,1,13,14,-1,14,2,1,-1,2,14,15,-1,15,3,2,-1,3,15,16,-1,16,4,3,-1,4,16,17,-1,17,5,4,-1,5,17,18,-1,18,6,5,-1,6,18,19,-1,19,7,6,-1,7,19,20,-1,20,8,7,-1,8,20,21,-1,21,9,8,-1,9,21,22,-1,22,10,9,-1,10,22,23,-1,23,11,10,-1,11,23,24,-1,24,12,11,-1,12,24,13,-1,13,1,12,-1,13,25,26,-1,26,14,13,-1,14,26,27,-1,27,15,14,-1,15,27,28,-1,28,16,15,-1,16,28,29,-1,29,17,16,-1,17,29,30,-1,30,18,17,-1,18,30,31,-1,31,19,18,-1,19,31,32,-1,32,20,19,-1,20,32,33,-1,33,21,20,-1,21,33,34,-1,34,22,21,-1,22,34,35,-1,35,23,22,-1,23,35,36,-1,36,24,23,-1,24,36,25,-1,25,13,24,-1,25,37,38,-1,38,26,25,-1,26,38,39,-1,39,27,26,-1,27,39,40,-1,40,28,27,-1,28,40,41,-1,41,29,28,-1,29,41,42,-1,42,30,29,-1,30,42,43,-1,43,31,30,-1,31,43,44,-1,44,32,31,-1,32,44,45,-1,45,33,32,-1,33,45,46,-1,46,34,33,-1,34,46,47,-1,47,35,34,-1,35,47,48,-1,48,36,35,-1,36,48,37,-1,37,25,36,-1,37,49,50,-1,50,38,37,-1,38,50,51,-1,51,39,38,-1,39,51,52,-1,52,40,39,-1,40,52,53,-1,53,41,40,-1,41,53,54,-1,54,42,41,-1,42,54,55,-1,55,43,42,-1,43,55,56,-1,56,44,43,-1,44,56,57,-1,57,45,44,-1,45,57,58,-1,58,46,45,-1,46,58,59,-1,59,47,46,-1,47,59,60,-1,60,48,47,-1,48,60,49,-1,49,37,48,-1,61,50,49,-1,61,51,50,-1,61,52,51,-1,61,53,52,-1,61,54,53,-1,61,55,54,-1,61,56,55,-1,61,57,56,-1,61,58,57,-1,61,59,58,-1,61,60,59,-1,61,49,60,-1]
Coordinate39 = x3d.Coordinate()

IndexedFaceSet38.coord = Coordinate39
TextureCoordinate40 = x3d.TextureCoordinate()

IndexedFaceSet38.texCoord = TextureCoordinate40

Shape34.geometry = IndexedFaceSet38

Transform33.children.append(Shape34)

HAnimSegment32.children.append(Transform33)

HAnimJoint31.children.append(HAnimSegment32)
HAnimJoint41 = x3d.HAnimJoint()
HAnimJoint41.name = "l_hip"
HAnimJoint41.DEF = "hanim_l_hip"
HAnimJoint41.center = [3.551,29.33,-0.1267]
HAnimJoint41.ulimit = [0,0,0]
HAnimJoint41.llimit = [0,0,0]
HAnimSegment42 = x3d.HAnimSegment()
HAnimSegment42.name = "l_thigh"
HAnimSegment42.DEF = "hanim_l_thigh"
Transform43 = x3d.Transform()
Transform43.translation = [3.551,29.33,-0.1267]
Shape44 = x3d.Shape()
Appearance45 = x3d.Appearance()
Material46 = x3d.Material()
Material46.diffuseColor = [0.588,0.588,0.588]

Appearance45.material = Material46
ImageTexture47 = x3d.ImageTexture()
ImageTexture47.USE = "HyunTextureAtlas"

Appearance45.texture = ImageTexture47

Shape44.appearance = Appearance45
IndexedFaceSet48 = x3d.IndexedFaceSet()
IndexedFaceSet48.coordIndex = [31,30,29,-1,31,29,28,-1,28,34,33,-1,31,28,33,-1,31,33,32,-1,8,7,0,-1,0,1,8,-1,9,8,1,-1,1,2,9,-1,10,9,2,-1,2,3,10,-1,11,10,3,-1,3,4,11,-1,12,11,4,-1,4,5,12,-1,13,12,5,-1,5,6,13,-1,7,13,6,-1,6,0,7,-1,15,14,7,-1,7,8,15,-1,16,15,8,-1,8,9,16,-1,17,16,9,-1,9,10,17,-1,18,17,10,-1,10,11,18,-1,19,18,11,-1,11,12,19,-1,20,19,12,-1,12,13,20,-1,14,20,13,-1,13,7,14,-1,22,21,14,-1,14,15,22,-1,23,22,15,-1,15,16,23,-1,24,23,16,-1,16,17,24,-1,25,24,17,-1,17,18,25,-1,26,25,18,-1,18,19,26,-1,27,26,19,-1,19,20,27,-1,21,27,20,-1,20,14,21,-1,1,0,28,-1,28,29,1,-1,2,1,29,-1,29,30,2,-1,3,2,30,-1,30,31,3,-1,4,3,31,-1,31,32,4,-1,5,4,32,-1,32,33,5,-1,6,5,33,-1,33,34,6,-1,0,6,34,-1,34,28,0,-1,35,36,21,-1,21,22,35,-1,37,35,22,-1,22,23,37,-1,38,37,23,-1,23,24,38,-1,39,38,24,-1,24,25,39,-1,40,39,25,-1,25,26,40,-1,41,40,26,-1,26,27,41,-1,36,41,27,-1,27,21,36,-1,36,35,42,-1,35,37,42,-1,37,38,42,-1,38,39,42,-1,39,40,42,-1,40,41,42,-1,41,36,42,-1]
IndexedFaceSet48.creaseAngle = 1.57
IndexedFaceSet48.texCoordIndex = [3,2,0,-1,3,0,1,-1,1,6,5,-1,3,1,5,-1,3,5,4,-1,8,9,7,-1,7,10,8,-1,11,8,10,-1,10,12,11,-1,13,11,12,-1,12,14,13,-1,15,13,14,-1,14,16,15,-1,17,15,16,-1,16,18,17,-1,19,17,18,-1,18,20,19,-1,9,19,20,-1,20,7,9,-1,21,22,9,-1,9,8,21,-1,23,21,8,-1,8,11,23,-1,24,23,11,-1,11,13,24,-1,25,24,13,-1,13,15,25,-1,26,25,15,-1,15,17,26,-1,27,26,17,-1,17,19,27,-1,22,27,19,-1,19,9,22,-1,28,29,22,-1,22,21,28,-1,30,28,21,-1,21,23,30,-1,31,30,23,-1,23,24,31,-1,32,31,24,-1,24,25,32,-1,33,32,25,-1,25,26,33,-1,34,33,26,-1,26,27,34,-1,29,34,27,-1,27,22,29,-1,10,7,1,-1,1,0,10,-1,12,10,0,-1,0,2,12,-1,14,12,2,-1,2,3,14,-1,16,14,3,-1,3,4,16,-1,18,16,4,-1,4,5,18,-1,20,18,5,-1,5,6,20,-1,7,20,6,-1,6,1,7,-1,35,36,29,-1,29,28,35,-1,37,35,28,-1,28,30,37,-1,38,37,30,-1,30,31,38,-1,39,38,31,-1,31,32,39,-1,40,39,32,-1,32,33,40,-1,41,40,33,-1,33,34,41,-1,36,41,34,-1,34,29,36,-1,36,35,42,-1,35,37,42,-1,37,38,42,-1,38,39,42,-1,39,40,42,-1,40,41,42,-1,41,36,42,-1]
Coordinate49 = x3d.Coordinate()

IndexedFaceSet48.coord = Coordinate49
TextureCoordinate50 = x3d.TextureCoordinate()

IndexedFaceSet48.texCoord = TextureCoordinate50

Shape44.geometry = IndexedFaceSet48

Transform43.children.append(Shape44)

HAnimSegment42.children.append(Transform43)

HAnimJoint41.children.append(HAnimSegment42)
HAnimJoint51 = x3d.HAnimJoint()
HAnimJoint51.name = "l_knee"
HAnimJoint51.DEF = "hanim_l_knee"
HAnimJoint51.center = [3.71,15.48,-0.1446]
HAnimJoint51.ulimit = [0,0,0]
HAnimJoint51.llimit = [0,0,0]
HAnimSegment52 = x3d.HAnimSegment()
HAnimSegment52.name = "l_calf"
HAnimSegment52.DEF = "hanim_l_calf"
Transform53 = x3d.Transform()
Transform53.translation = [3.71,15.48,-0.1446]
Shape54 = x3d.Shape()
Appearance55 = x3d.Appearance()
Material56 = x3d.Material()
Material56.diffuseColor = [0.588,0.588,0.588]

Appearance55.material = Material56
ImageTexture57 = x3d.ImageTexture()
ImageTexture57.USE = "HyunTextureAtlas"

Appearance55.texture = ImageTexture57

Shape54.appearance = Appearance55
IndexedFaceSet58 = x3d.IndexedFaceSet()
IndexedFaceSet58.coordIndex = [45,44,43,-1,45,43,42,-1,42,48,47,-1,45,42,47,-1,45,47,46,-1,8,7,0,-1,0,1,8,-1,9,8,1,-1,1,2,9,-1,10,9,2,-1,2,3,10,-1,11,10,3,-1,3,4,11,-1,12,11,4,-1,4,5,12,-1,13,12,5,-1,5,6,13,-1,7,13,6,-1,6,0,7,-1,15,14,7,-1,7,8,15,-1,16,15,8,-1,8,9,16,-1,17,16,9,-1,9,10,17,-1,18,17,10,-1,10,11,18,-1,19,18,11,-1,11,12,19,-1,20,19,12,-1,12,13,20,-1,14,20,13,-1,13,7,14,-1,22,21,14,-1,14,15,22,-1,23,22,15,-1,15,16,23,-1,24,23,16,-1,16,17,24,-1,25,24,17,-1,17,18,25,-1,26,25,18,-1,18,19,26,-1,27,26,19,-1,19,20,27,-1,21,27,20,-1,20,14,21,-1,58,59,60,-1,61,62,56,-1,60,61,56,-1,58,60,56,-1,58,56,57,-1,21,22,29,-1,29,28,21,-1,22,23,30,-1,30,29,22,-1,23,24,31,-1,31,30,23,-1,24,25,32,-1,32,31,24,-1,25,26,33,-1,33,32,25,-1,26,27,34,-1,34,33,26,-1,27,21,28,-1,28,34,27,-1,28,29,36,-1,36,35,28,-1,29,30,37,-1,37,36,29,-1,30,31,38,-1,38,37,30,-1,31,32,39,-1,39,38,31,-1,32,33,40,-1,40,39,32,-1,33,34,41,-1,41,40,33,-1,34,28,35,-1,35,41,34,-1,1,0,42,-1,42,43,1,-1,2,1,43,-1,43,44,2,-1,3,2,44,-1,44,45,3,-1,4,3,45,-1,45,46,4,-1,5,4,46,-1,46,47,5,-1,6,5,47,-1,47,48,6,-1,0,6,48,-1,48,42,0,-1,35,36,50,-1,50,49,35,-1,36,37,51,-1,51,50,36,-1,37,38,52,-1,52,51,37,-1,38,39,53,-1,53,52,38,-1,39,40,54,-1,54,53,39,-1,40,41,55,-1,55,54,40,-1,41,35,49,-1,49,55,41,-1,49,50,57,-1,57,56,49,-1,50,51,58,-1,58,57,50,-1,51,52,59,-1,59,58,51,-1,52,53,60,-1,60,59,52,-1,53,54,61,-1,61,60,53,-1,54,55,62,-1,62,61,54,-1,55,49,56,-1,56,62,55,-1]
IndexedFaceSet58.creaseAngle = 1.57
IndexedFaceSet58.texCoordIndex = [56,55,53,-1,56,53,52,-1,52,59,58,-1,56,52,58,-1,56,58,57,-1,8,7,0,-1,0,1,8,-1,9,8,1,-1,1,2,9,-1,10,9,2,-1,2,3,10,-1,11,10,3,-1,3,4,11,-1,12,11,4,-1,4,5,12,-1,29,12,5,-1,5,30,29,-1,7,13,6,-1,6,0,7,-1,15,14,7,-1,7,8,15,-1,16,15,8,-1,8,9,16,-1,17,16,9,-1,9,10,17,-1,18,17,10,-1,10,11,18,-1,19,18,11,-1,11,12,19,-1,31,19,12,-1,12,32,31,-1,14,20,13,-1,13,7,14,-1,22,21,14,-1,14,15,22,-1,23,22,15,-1,15,16,23,-1,24,23,16,-1,16,17,24,-1,25,24,17,-1,17,18,25,-1,26,25,18,-1,18,19,26,-1,33,26,19,-1,19,34,33,-1,21,27,20,-1,20,14,21,-1,71,72,73,-1,74,70,68,-1,73,74,68,-1,71,73,68,-1,71,68,69,-1,21,22,37,-1,37,36,21,-1,22,23,39,-1,39,37,22,-1,23,24,40,-1,40,39,23,-1,24,25,41,-1,41,40,24,-1,25,26,42,-1,42,41,25,-1,26,35,43,-1,43,42,26,-1,27,21,36,-1,36,38,27,-1,36,37,45,-1,45,44,36,-1,37,39,47,-1,47,45,37,-1,39,40,48,-1,48,47,39,-1,40,41,49,-1,49,48,40,-1,41,42,50,-1,50,49,41,-1,42,43,51,-1,51,50,42,-1,38,36,44,-1,44,46,38,-1,1,0,52,-1,52,53,1,-1,2,1,53,-1,53,55,2,-1,3,2,55,-1,55,56,3,-1,4,3,56,-1,56,57,4,-1,5,4,57,-1,57,58,5,-1,28,5,58,-1,58,59,28,-1,0,6,54,-1,54,52,0,-1,44,45,61,-1,61,60,44,-1,45,47,63,-1,63,61,45,-1,47,48,64,-1,64,63,47,-1,48,49,65,-1,65,64,48,-1,49,50,66,-1,66,65,49,-1,50,51,67,-1,67,66,50,-1,46,44,60,-1,60,62,46,-1,60,61,69,-1,69,68,60,-1,61,63,71,-1,71,69,61,-1,63,64,72,-1,72,71,63,-1,64,65,73,-1,73,72,64,-1,65,66,74,-1,74,73,65,-1,66,67,75,-1,75,74,66,-1,62,60,68,-1,68,70,62,-1]
Coordinate59 = x3d.Coordinate()

IndexedFaceSet58.coord = Coordinate59
TextureCoordinate60 = x3d.TextureCoordinate()

IndexedFaceSet58.texCoord = TextureCoordinate60

Shape54.geometry = IndexedFaceSet58

Transform53.children.append(Shape54)

HAnimSegment52.children.append(Transform53)

HAnimJoint51.children.append(HAnimSegment52)
HAnimJoint61 = x3d.HAnimJoint()
HAnimJoint61.name = "l_talocrural"
HAnimJoint61.DEF = "hanim_l_talocrural"
HAnimJoint61.center = [3.388,3.168,-0.537]
HAnimJoint61.ulimit = [0,0,0]
HAnimJoint61.llimit = [0,0,0]
HAnimSegment62 = x3d.HAnimSegment()
HAnimSegment62.name = "l_talus"
HAnimSegment62.DEF = "hanim_l_talus"
Transform63 = x3d.Transform()
Transform63.translation = [3.388,3.168,-0.537]
Shape64 = x3d.Shape()
Appearance65 = x3d.Appearance()
Material66 = x3d.Material()
Material66.diffuseColor = [0.588,0.588,0.588]

Appearance65.material = Material66
ImageTexture67 = x3d.ImageTexture()
ImageTexture67.USE = "HyunTextureAtlas"

Appearance65.texture = ImageTexture67

Shape64.appearance = Appearance65
IndexedFaceSet68 = x3d.IndexedFaceSet()
IndexedFaceSet68.coordIndex = [1,11,12,-1,3,4,5,-1,5,6,3,-1,1,0,4,-1,4,3,1,-1,0,2,5,-1,5,4,0,-1,11,1,3,-1,3,6,11,-1,18,2,0,-1,0,17,18,-1,0,1,25,-1,25,17,0,-1,25,1,12,-1,7,13,11,-1,8,6,5,-1,5,9,8,-1,7,8,9,-1,9,10,7,-1,10,9,5,-1,5,2,10,-1,11,6,8,-1,8,7,11,-1,18,21,10,-1,10,2,18,-1,10,21,27,-1,27,7,10,-1,27,13,7,-1,12,11,37,-1,37,35,12,-1,11,13,36,-1,36,37,11,-1,20,18,17,-1,17,14,20,-1,23,14,17,-1,17,25,23,-1,16,20,14,-1,14,15,16,-1,24,15,14,-1,14,23,24,-1,15,24,29,-1,29,16,15,-1,20,19,21,-1,21,18,20,-1,26,27,21,-1,21,19,26,-1,16,22,19,-1,19,20,16,-1,28,26,19,-1,19,22,28,-1,22,16,29,-1,29,28,22,-1,36,32,33,-1,34,30,31,-1,33,34,31,-1,36,33,31,-1,36,31,35,-1,24,23,31,-1,31,30,24,-1,23,25,35,-1,35,31,23,-1,27,26,32,-1,32,36,27,-1,26,28,33,-1,33,32,26,-1,28,29,34,-1,34,33,28,-1,29,24,30,-1,30,34,29,-1,36,35,37,-1,12,35,25,-1,27,36,13,-1]
IndexedFaceSet68.creaseAngle = 1.57
IndexedFaceSet68.texCoordIndex = [1,14,18,-1,3,4,5,-1,5,6,3,-1,1,0,4,-1,4,3,1,-1,0,2,5,-1,5,4,0,-1,14,1,3,-1,3,6,14,-1,19,2,0,-1,0,16,19,-1,0,1,17,-1,17,16,0,-1,17,1,18,-1,7,23,15,-1,9,8,11,-1,11,10,9,-1,7,9,10,-1,10,12,7,-1,12,10,11,-1,11,13,12,-1,15,8,9,-1,9,7,15,-1,20,21,12,-1,12,13,20,-1,12,21,22,-1,22,7,12,-1,22,23,7,-1,18,14,25,-1,25,24,18,-1,15,23,26,-1,26,25,15,-1,29,33,32,-1,32,27,29,-1,41,27,32,-1,32,43,41,-1,30,29,27,-1,27,28,30,-1,42,28,27,-1,27,41,42,-1,28,42,48,-1,48,31,28,-1,35,34,37,-1,37,36,35,-1,44,45,37,-1,37,34,44,-1,39,38,34,-1,34,35,39,-1,46,44,34,-1,34,38,46,-1,38,40,47,-1,47,46,38,-1,52,53,54,-1,55,49,50,-1,54,55,50,-1,52,54,50,-1,52,50,51,-1,42,41,50,-1,50,49,42,-1,41,43,51,-1,51,50,41,-1,45,44,53,-1,53,52,45,-1,44,46,54,-1,54,53,44,-1,46,47,55,-1,55,54,46,-1,48,42,49,-1,49,55,48,-1,52,51,56,-1,18,24,43,-1,22,52,23,-1]
Coordinate69 = x3d.Coordinate()

IndexedFaceSet68.coord = Coordinate69
TextureCoordinate70 = x3d.TextureCoordinate()

IndexedFaceSet68.texCoord = TextureCoordinate70

Shape64.geometry = IndexedFaceSet68

Transform63.children.append(Shape64)

HAnimSegment62.children.append(Transform63)

HAnimJoint61.children.append(HAnimSegment62)
HAnimJoint71 = x3d.HAnimJoint()
HAnimJoint71.name = "l_metatarsophalangeal_2"
HAnimJoint71.DEF = "hanim_l_metatarsophalangeal_2"
HAnimJoint71.center = [3.388,2.908,0.7441]
HAnimJoint71.ulimit = [0,0,0]
HAnimJoint71.llimit = [0,0,0]
HAnimSegment72 = x3d.HAnimSegment()
HAnimSegment72.name = "l_tarsal_proximal_phalanx_2"
HAnimSegment72.DEF = "hanim_l_tarsal_proximal_phalanx_2"
Transform73 = x3d.Transform()
Transform73.translation = [3.388,2.908,0.7441]
Shape74 = x3d.Shape()
Appearance75 = x3d.Appearance()
Material76 = x3d.Material()
Material76.diffuseColor = [0.588,0.588,0.588]

Appearance75.material = Material76
ImageTexture77 = x3d.ImageTexture()
ImageTexture77.USE = "HyunTextureAtlas"

Appearance75.texture = ImageTexture77

Shape74.appearance = Appearance75
IndexedFaceSet78 = x3d.IndexedFaceSet()
IndexedFaceSet78.coordIndex = [3,4,25,-1,3,25,26,-1,0,3,26,-1,1,0,26,-1,26,10,1,-1,1,10,12,-1,12,9,1,-1,2,34,25,-1,25,4,2,-1,31,8,6,-1,32,31,6,-1,5,32,6,-1,7,11,32,-1,32,5,7,-1,7,9,12,-1,12,11,7,-1,2,8,31,-1,31,34,2,-1,15,16,17,-1,15,17,18,-1,15,18,19,-1,14,15,19,-1,14,19,13,-1,0,1,14,-1,14,13,0,-1,1,9,15,-1,15,14,1,-1,9,7,16,-1,16,15,9,-1,7,5,17,-1,17,16,7,-1,5,6,18,-1,18,17,5,-1,6,3,19,-1,19,18,6,-1,3,0,13,-1,13,19,3,-1,6,8,2,-1,3,6,2,-1,4,3,2,-1,23,21,20,-1,20,24,23,-1,29,22,21,-1,21,23,29,-1,22,29,33,-1,20,21,26,-1,26,25,20,-1,26,21,22,-1,22,10,26,-1,10,22,33,-1,33,12,10,-1,34,24,20,-1,20,25,34,-1,23,24,28,-1,28,27,23,-1,29,23,27,-1,27,30,29,-1,30,33,29,-1,28,31,32,-1,32,27,28,-1,32,11,30,-1,30,27,32,-1,11,12,33,-1,33,30,11,-1,34,31,28,-1,28,24,34,-1]
IndexedFaceSet78.creaseAngle = 1.57
IndexedFaceSet78.texCoordIndex = [4,5,12,-1,4,12,13,-1,0,4,13,-1,1,0,13,-1,13,14,1,-1,1,14,19,-1,19,3,1,-1,2,21,12,-1,12,5,2,-1,15,10,7,-1,16,15,7,-1,6,16,7,-1,8,17,16,-1,16,6,8,-1,8,11,18,-1,18,17,8,-1,9,10,15,-1,15,20,9,-1,24,25,26,-1,24,26,27,-1,24,27,28,-1,23,24,28,-1,23,28,22,-1,0,1,23,-1,23,22,0,-1,1,3,24,-1,24,23,1,-1,11,8,25,-1,25,24,11,-1,8,6,26,-1,26,25,8,-1,6,7,27,-1,27,26,6,-1,7,4,28,-1,28,27,7,-1,4,0,22,-1,22,28,4,-1,7,10,9,-1,4,7,9,-1,5,4,9,-1,30,32,31,-1,31,29,30,-1,33,34,32,-1,32,30,33,-1,34,33,35,-1,31,32,37,-1,37,36,31,-1,37,32,34,-1,34,38,37,-1,38,34,35,-1,35,39,38,-1,40,29,31,-1,31,36,40,-1,41,44,43,-1,43,42,41,-1,45,41,42,-1,42,46,45,-1,46,50,45,-1,43,47,48,-1,48,42,43,-1,48,49,46,-1,46,42,48,-1,49,51,50,-1,50,46,49,-1,52,47,43,-1,43,44,52,-1]
Coordinate79 = x3d.Coordinate()

IndexedFaceSet78.coord = Coordinate79
TextureCoordinate80 = x3d.TextureCoordinate()

IndexedFaceSet78.texCoord = TextureCoordinate80

Shape74.geometry = IndexedFaceSet78

Transform73.children.append(Shape74)

HAnimSegment72.children.append(Transform73)

HAnimJoint71.children.append(HAnimSegment72)

HAnimJoint61.children.append(HAnimJoint71)

HAnimJoint51.children.append(HAnimJoint61)

HAnimJoint41.children.append(HAnimJoint51)

HAnimJoint31.children.append(HAnimJoint41)
HAnimJoint81 = x3d.HAnimJoint()
HAnimJoint81.name = "r_hip"
HAnimJoint81.DEF = "hanim_r_hip"
HAnimJoint81.center = [-3.551,29.33,-0.1267]
HAnimJoint81.ulimit = [0,0,0]
HAnimJoint81.llimit = [0,0,0]
HAnimSegment82 = x3d.HAnimSegment()
HAnimSegment82.name = "r_thigh"
HAnimSegment82.DEF = "hanim_r_thigh"
Transform83 = x3d.Transform()
Transform83.translation = [-3.551,29.33,-0.1267]
Shape84 = x3d.Shape()
Appearance85 = x3d.Appearance()
Material86 = x3d.Material()
Material86.diffuseColor = [0.588,0.588,0.588]

Appearance85.material = Material86
ImageTexture87 = x3d.ImageTexture()
ImageTexture87.USE = "HyunTextureAtlas"

Appearance85.texture = ImageTexture87

Shape84.appearance = Appearance85
IndexedFaceSet88 = x3d.IndexedFaceSet()
IndexedFaceSet88.coordIndex = [31,32,33,-1,33,34,28,-1,31,33,28,-1,31,28,29,-1,31,29,30,-1,8,1,0,-1,0,7,8,-1,9,2,1,-1,1,8,9,-1,10,3,2,-1,2,9,10,-1,11,4,3,-1,3,10,11,-1,12,5,4,-1,4,11,12,-1,13,6,5,-1,5,12,13,-1,7,0,6,-1,6,13,7,-1,15,8,7,-1,7,14,15,-1,16,9,8,-1,8,15,16,-1,17,10,9,-1,9,16,17,-1,18,11,10,-1,10,17,18,-1,19,12,11,-1,11,18,19,-1,20,13,12,-1,12,19,20,-1,14,7,13,-1,13,20,14,-1,22,15,14,-1,14,21,22,-1,23,16,15,-1,15,22,23,-1,24,17,16,-1,16,23,24,-1,25,18,17,-1,17,24,25,-1,26,19,18,-1,18,25,26,-1,27,20,19,-1,19,26,27,-1,21,14,20,-1,20,27,21,-1,1,29,28,-1,28,0,1,-1,2,30,29,-1,29,1,2,-1,3,31,30,-1,30,2,3,-1,4,32,31,-1,31,3,4,-1,5,33,32,-1,32,4,5,-1,6,34,33,-1,33,5,6,-1,0,28,34,-1,34,6,0,-1,35,22,21,-1,21,36,35,-1,37,23,22,-1,22,35,37,-1,38,24,23,-1,23,37,38,-1,39,25,24,-1,24,38,39,-1,40,26,25,-1,25,39,40,-1,41,27,26,-1,26,40,41,-1,36,21,27,-1,27,41,36,-1,36,42,35,-1,35,42,37,-1,37,42,38,-1,38,42,39,-1,39,42,40,-1,40,42,41,-1,41,42,36,-1]
IndexedFaceSet88.creaseAngle = 1.57
IndexedFaceSet88.texCoordIndex = [3,4,5,-1,5,6,1,-1,3,5,1,-1,3,1,0,-1,3,0,2,-1,8,10,7,-1,7,9,8,-1,11,12,10,-1,10,8,11,-1,13,14,12,-1,12,11,13,-1,15,16,14,-1,14,13,15,-1,17,18,16,-1,16,15,17,-1,19,20,18,-1,18,17,19,-1,9,7,20,-1,20,19,9,-1,21,8,9,-1,9,22,21,-1,23,11,8,-1,8,21,23,-1,24,13,11,-1,11,23,24,-1,25,15,13,-1,13,24,25,-1,26,17,15,-1,15,25,26,-1,27,19,17,-1,17,26,27,-1,22,9,19,-1,19,27,22,-1,28,21,22,-1,22,29,28,-1,30,23,21,-1,21,28,30,-1,31,24,23,-1,23,30,31,-1,32,25,24,-1,24,31,32,-1,33,26,25,-1,25,32,33,-1,34,27,26,-1,26,33,34,-1,29,22,27,-1,27,34,29,-1,10,0,1,-1,1,7,10,-1,12,2,0,-1,0,10,12,-1,14,3,2,-1,2,12,14,-1,16,4,3,-1,3,14,16,-1,18,5,4,-1,4,16,18,-1,20,6,5,-1,5,18,20,-1,7,1,6,-1,6,20,7,-1,35,28,29,-1,29,36,35,-1,37,30,28,-1,28,35,37,-1,38,31,30,-1,30,37,38,-1,39,32,31,-1,31,38,39,-1,40,33,32,-1,32,39,40,-1,41,34,33,-1,33,40,41,-1,36,29,34,-1,34,41,36,-1,36,42,35,-1,35,42,37,-1,37,42,38,-1,38,42,39,-1,39,42,40,-1,40,42,41,-1,41,42,36,-1]
Coordinate89 = x3d.Coordinate()

IndexedFaceSet88.coord = Coordinate89
TextureCoordinate90 = x3d.TextureCoordinate()

IndexedFaceSet88.texCoord = TextureCoordinate90

Shape84.geometry = IndexedFaceSet88

Transform83.children.append(Shape84)

HAnimSegment82.children.append(Transform83)

HAnimJoint81.children.append(HAnimSegment82)
HAnimJoint91 = x3d.HAnimJoint()
HAnimJoint91.name = "r_knee"
HAnimJoint91.DEF = "hanim_r_knee"
HAnimJoint91.center = [-3.71,15.48,-0.1446]
HAnimJoint91.ulimit = [0,0,0]
HAnimJoint91.llimit = [0,0,0]
HAnimSegment92 = x3d.HAnimSegment()
HAnimSegment92.name = "r_calf"
HAnimSegment92.DEF = "hanim_r_calf"
Transform93 = x3d.Transform()
Transform93.translation = [-3.71,15.48,-0.1446]
Shape94 = x3d.Shape()
Appearance95 = x3d.Appearance()
Material96 = x3d.Material()
Material96.diffuseColor = [0.588,0.588,0.588]

Appearance95.material = Material96
ImageTexture97 = x3d.ImageTexture()
ImageTexture97.USE = "HyunTextureAtlas"

Appearance95.texture = ImageTexture97

Shape94.appearance = Appearance95
IndexedFaceSet98 = x3d.IndexedFaceSet()
IndexedFaceSet98.coordIndex = [45,46,47,-1,47,48,42,-1,45,47,42,-1,45,42,43,-1,45,43,44,-1,8,1,0,-1,0,7,8,-1,9,2,1,-1,1,8,9,-1,10,3,2,-1,2,9,10,-1,11,4,3,-1,3,10,11,-1,12,5,4,-1,4,11,12,-1,13,6,5,-1,5,12,13,-1,7,0,6,-1,6,13,7,-1,15,8,7,-1,7,14,15,-1,16,9,8,-1,8,15,16,-1,17,10,9,-1,9,16,17,-1,18,11,10,-1,10,17,18,-1,19,12,11,-1,11,18,19,-1,20,13,12,-1,12,19,20,-1,14,7,13,-1,13,20,14,-1,22,15,14,-1,14,21,22,-1,23,16,15,-1,15,22,23,-1,24,17,16,-1,16,23,24,-1,25,18,17,-1,17,24,25,-1,26,19,18,-1,18,25,26,-1,27,20,19,-1,19,26,27,-1,21,14,20,-1,20,27,21,-1,58,57,56,-1,56,62,61,-1,56,61,60,-1,58,56,60,-1,58,60,59,-1,21,28,29,-1,29,22,21,-1,22,29,30,-1,30,23,22,-1,23,30,31,-1,31,24,23,-1,24,31,32,-1,32,25,24,-1,25,32,33,-1,33,26,25,-1,26,33,34,-1,34,27,26,-1,27,34,28,-1,28,21,27,-1,28,35,36,-1,36,29,28,-1,29,36,37,-1,37,30,29,-1,30,37,38,-1,38,31,30,-1,31,38,39,-1,39,32,31,-1,32,39,40,-1,40,33,32,-1,33,40,41,-1,41,34,33,-1,34,41,35,-1,35,28,34,-1,1,43,42,-1,42,0,1,-1,2,44,43,-1,43,1,2,-1,3,45,44,-1,44,2,3,-1,4,46,45,-1,45,3,4,-1,5,47,46,-1,46,4,5,-1,6,48,47,-1,47,5,6,-1,0,42,48,-1,48,6,0,-1,35,49,50,-1,50,36,35,-1,36,50,51,-1,51,37,36,-1,37,51,52,-1,52,38,37,-1,38,52,53,-1,53,39,38,-1,39,53,54,-1,54,40,39,-1,40,54,55,-1,55,41,40,-1,41,55,49,-1,49,35,41,-1,49,56,57,-1,57,50,49,-1,50,57,58,-1,58,51,50,-1,51,58,59,-1,59,52,51,-1,52,59,60,-1,60,53,52,-1,53,60,61,-1,61,54,53,-1,54,61,62,-1,62,55,54,-1,55,62,56,-1,56,49,55,-1]
IndexedFaceSet98.creaseAngle = 1.57
IndexedFaceSet98.texCoordIndex = [56,57,58,-1,58,59,52,-1,56,58,52,-1,56,52,53,-1,56,53,55,-1,8,1,0,-1,0,7,8,-1,9,2,1,-1,1,8,9,-1,10,3,2,-1,2,9,10,-1,11,4,3,-1,3,10,11,-1,12,5,4,-1,4,11,12,-1,29,30,5,-1,5,12,29,-1,7,0,6,-1,6,13,7,-1,15,8,7,-1,7,14,15,-1,16,9,8,-1,8,15,16,-1,17,10,9,-1,9,16,17,-1,18,11,10,-1,10,17,18,-1,19,12,11,-1,11,18,19,-1,31,32,12,-1,12,19,31,-1,14,7,13,-1,13,20,14,-1,22,15,14,-1,14,21,22,-1,23,16,15,-1,15,22,23,-1,24,17,16,-1,16,23,24,-1,25,18,17,-1,17,24,25,-1,26,19,18,-1,18,25,26,-1,33,34,19,-1,19,26,33,-1,21,14,20,-1,20,27,21,-1,71,69,68,-1,68,70,74,-1,68,74,73,-1,71,68,73,-1,71,73,72,-1,21,36,37,-1,37,22,21,-1,22,37,39,-1,39,23,22,-1,23,39,40,-1,40,24,23,-1,24,40,41,-1,41,25,24,-1,25,41,42,-1,42,26,25,-1,26,42,43,-1,43,35,26,-1,27,38,36,-1,36,21,27,-1,36,44,45,-1,45,37,36,-1,37,45,47,-1,47,39,37,-1,39,47,48,-1,48,40,39,-1,40,48,49,-1,49,41,40,-1,41,49,50,-1,50,42,41,-1,42,50,51,-1,51,43,42,-1,38,46,44,-1,44,36,38,-1,1,53,52,-1,52,0,1,-1,2,55,53,-1,53,1,2,-1,3,56,55,-1,55,2,3,-1,4,57,56,-1,56,3,4,-1,5,58,57,-1,57,4,5,-1,28,59,58,-1,58,5,28,-1,0,52,54,-1,54,6,0,-1,44,60,61,-1,61,45,44,-1,45,61,63,-1,63,47,45,-1,47,63,64,-1,64,48,47,-1,48,64,65,-1,65,49,48,-1,49,65,66,-1,66,50,49,-1,50,66,67,-1,67,51,50,-1,46,62,60,-1,60,44,46,-1,60,68,69,-1,69,61,60,-1,61,69,71,-1,71,63,61,-1,63,71,72,-1,72,64,63,-1,64,72,73,-1,73,65,64,-1,65,73,74,-1,74,66,65,-1,66,74,75,-1,75,67,66,-1,62,70,68,-1,68,60,62,-1]
Coordinate99 = x3d.Coordinate()

IndexedFaceSet98.coord = Coordinate99
TextureCoordinate100 = x3d.TextureCoordinate()

IndexedFaceSet98.texCoord = TextureCoordinate100

Shape94.geometry = IndexedFaceSet98

Transform93.children.append(Shape94)

HAnimSegment92.children.append(Transform93)

HAnimJoint91.children.append(HAnimSegment92)
HAnimJoint101 = x3d.HAnimJoint()
HAnimJoint101.name = "r_talocrural"
HAnimJoint101.DEF = "hanim_r_talocrural"
HAnimJoint101.center = [-3.388,3.168,-0.537]
HAnimJoint101.ulimit = [0,0,0]
HAnimJoint101.llimit = [0,0,0]
HAnimSegment102 = x3d.HAnimSegment()
HAnimSegment102.name = "r_talus"
HAnimSegment102.DEF = "hanim_r_talus"
Transform103 = x3d.Transform()
Transform103.translation = [-3.388,3.168,-0.537]
Shape104 = x3d.Shape()
Appearance105 = x3d.Appearance()
Material106 = x3d.Material()
Material106.diffuseColor = [0.588,0.588,0.588]

Appearance105.material = Material106
ImageTexture107 = x3d.ImageTexture()
ImageTexture107.USE = "HyunTextureAtlas"

Appearance105.texture = ImageTexture107

Shape104.appearance = Appearance105
IndexedFaceSet108 = x3d.IndexedFaceSet()
IndexedFaceSet108.coordIndex = [1,12,11,-1,3,6,5,-1,5,4,3,-1,1,3,4,-1,4,0,1,-1,0,4,5,-1,5,2,0,-1,11,6,3,-1,3,1,11,-1,18,17,0,-1,0,2,18,-1,0,17,25,-1,25,1,0,-1,25,12,1,-1,7,11,13,-1,8,9,5,-1,5,6,8,-1,7,10,9,-1,9,8,7,-1,10,2,5,-1,5,9,10,-1,11,7,8,-1,8,6,11,-1,18,2,10,-1,10,21,18,-1,10,7,27,-1,27,21,10,-1,27,7,13,-1,12,35,37,-1,37,11,12,-1,11,37,36,-1,36,13,11,-1,20,14,17,-1,17,18,20,-1,23,25,17,-1,17,14,23,-1,16,15,14,-1,14,20,16,-1,24,23,14,-1,14,15,24,-1,15,16,29,-1,29,24,15,-1,20,18,21,-1,21,19,20,-1,26,19,21,-1,21,27,26,-1,16,20,19,-1,19,22,16,-1,28,22,19,-1,19,26,28,-1,22,28,29,-1,29,16,22,-1,36,35,31,-1,31,30,34,-1,31,34,33,-1,36,31,33,-1,36,33,32,-1,24,30,31,-1,31,23,24,-1,23,31,35,-1,35,25,23,-1,27,36,32,-1,32,26,27,-1,26,32,33,-1,33,28,26,-1,28,33,34,-1,34,29,28,-1,29,34,30,-1,30,24,29,-1,36,37,35,-1,12,25,35,-1,27,13,36,-1]
IndexedFaceSet108.creaseAngle = 1.57
IndexedFaceSet108.texCoordIndex = [1,18,14,-1,3,6,5,-1,5,4,3,-1,1,3,4,-1,4,0,1,-1,0,4,5,-1,5,2,0,-1,14,6,3,-1,3,1,14,-1,19,16,0,-1,0,2,19,-1,0,16,17,-1,17,1,0,-1,17,18,1,-1,7,15,23,-1,9,10,11,-1,11,8,9,-1,7,12,10,-1,10,9,7,-1,12,13,11,-1,11,10,12,-1,15,7,9,-1,9,8,15,-1,20,13,12,-1,12,21,20,-1,12,7,22,-1,22,21,12,-1,22,7,23,-1,18,24,25,-1,25,14,18,-1,15,25,26,-1,26,23,15,-1,29,27,32,-1,32,33,29,-1,41,43,32,-1,32,27,41,-1,30,28,27,-1,27,29,30,-1,42,41,27,-1,27,28,42,-1,28,31,48,-1,48,42,28,-1,35,36,37,-1,37,34,35,-1,44,34,37,-1,37,45,44,-1,39,35,34,-1,34,38,39,-1,46,38,34,-1,34,44,46,-1,38,46,47,-1,47,40,38,-1,52,51,50,-1,50,49,55,-1,50,55,54,-1,52,50,54,-1,52,54,53,-1,42,49,50,-1,50,41,42,-1,41,50,51,-1,51,43,41,-1,45,52,53,-1,53,44,45,-1,44,53,54,-1,54,46,44,-1,46,54,55,-1,55,47,46,-1,48,55,49,-1,49,42,48,-1,52,56,51,-1,18,43,24,-1,22,23,52,-1]
Coordinate109 = x3d.Coordinate()

IndexedFaceSet108.coord = Coordinate109
TextureCoordinate110 = x3d.TextureCoordinate()

IndexedFaceSet108.texCoord = TextureCoordinate110

Shape104.geometry = IndexedFaceSet108

Transform103.children.append(Shape104)

HAnimSegment102.children.append(Transform103)

HAnimJoint101.children.append(HAnimSegment102)
HAnimJoint111 = x3d.HAnimJoint()
HAnimJoint111.name = "r_metatarsophalangeal_2"
HAnimJoint111.DEF = "hanim_r_metatarsophalangeal_2"
HAnimJoint111.center = [-3.388,2.908,0.7441]
HAnimJoint111.ulimit = [0,0,0]
HAnimJoint111.llimit = [0,0,0]
HAnimSegment112 = x3d.HAnimSegment()
HAnimSegment112.name = "r_tarsal_proximal_phalanx_2"
HAnimSegment112.DEF = "hanim_r_tarsal_proximal_phalanx_2"
Transform113 = x3d.Transform()
Transform113.translation = [-3.388,2.908,0.7441]
Shape114 = x3d.Shape()
Appearance115 = x3d.Appearance()
Material116 = x3d.Material()
Material116.diffuseColor = [0.588,0.588,0.588]

Appearance115.material = Material116
ImageTexture117 = x3d.ImageTexture()
ImageTexture117.USE = "HyunTextureAtlas"

Appearance115.texture = ImageTexture117

Shape114.appearance = Appearance115
IndexedFaceSet118 = x3d.IndexedFaceSet()
IndexedFaceSet118.coordIndex = [25,4,3,-1,26,25,3,-1,0,26,3,-1,1,10,26,-1,26,0,1,-1,1,9,12,-1,12,10,1,-1,2,4,25,-1,25,34,2,-1,6,8,31,-1,6,31,32,-1,5,6,32,-1,7,5,32,-1,32,11,7,-1,7,11,12,-1,12,9,7,-1,2,34,31,-1,31,8,2,-1,14,13,19,-1,17,16,15,-1,18,17,15,-1,19,18,15,-1,14,19,15,-1,0,13,14,-1,14,1,0,-1,1,14,15,-1,15,9,1,-1,9,15,16,-1,16,7,9,-1,7,16,17,-1,17,5,7,-1,5,17,18,-1,18,6,5,-1,6,18,19,-1,19,3,6,-1,3,19,13,-1,13,0,3,-1,2,8,6,-1,2,6,3,-1,4,2,3,-1,23,24,20,-1,20,21,23,-1,29,23,21,-1,21,22,29,-1,22,33,29,-1,20,25,26,-1,26,21,20,-1,26,10,22,-1,22,21,26,-1,10,12,33,-1,33,22,10,-1,34,25,20,-1,20,24,34,-1,23,27,28,-1,28,24,23,-1,29,30,27,-1,27,23,29,-1,30,29,33,-1,28,27,32,-1,32,31,28,-1,32,27,30,-1,30,11,32,-1,11,30,33,-1,33,12,11,-1,34,24,28,-1,28,31,34,-1]
IndexedFaceSet118.creaseAngle = 1.57
IndexedFaceSet118.texCoordIndex = [12,5,4,-1,13,12,4,-1,0,13,4,-1,1,14,13,-1,13,0,1,-1,1,3,19,-1,19,14,1,-1,2,5,12,-1,12,21,2,-1,7,10,15,-1,7,15,16,-1,6,7,16,-1,8,6,16,-1,16,17,8,-1,8,17,18,-1,18,11,8,-1,9,20,15,-1,15,10,9,-1,23,22,28,-1,26,25,24,-1,27,26,24,-1,28,27,24,-1,23,28,24,-1,0,22,23,-1,23,1,0,-1,1,23,24,-1,24,3,1,-1,11,24,25,-1,25,8,11,-1,8,25,26,-1,26,6,8,-1,6,26,27,-1,27,7,6,-1,7,27,28,-1,28,4,7,-1,4,28,22,-1,22,0,4,-1,9,10,7,-1,9,7,4,-1,5,9,4,-1,30,29,31,-1,31,32,30,-1,33,30,32,-1,32,34,33,-1,34,35,33,-1,31,36,37,-1,37,32,31,-1,37,38,34,-1,34,32,37,-1,38,39,35,-1,35,34,38,-1,40,36,31,-1,31,29,40,-1,41,42,43,-1,43,44,41,-1,45,46,42,-1,42,41,45,-1,46,45,50,-1,43,42,48,-1,48,47,43,-1,48,42,46,-1,46,49,48,-1,49,46,50,-1,50,51,49,-1,52,44,43,-1,43,47,52,-1]
Coordinate119 = x3d.Coordinate()

IndexedFaceSet118.coord = Coordinate119
TextureCoordinate120 = x3d.TextureCoordinate()

IndexedFaceSet118.texCoord = TextureCoordinate120

Shape114.geometry = IndexedFaceSet118

Transform113.children.append(Shape114)

HAnimSegment112.children.append(Transform113)

HAnimJoint111.children.append(HAnimSegment112)

HAnimJoint101.children.append(HAnimJoint111)

HAnimJoint91.children.append(HAnimJoint101)

HAnimJoint81.children.append(HAnimJoint91)

HAnimJoint31.children.append(HAnimJoint81)
HAnimJoint121 = x3d.HAnimJoint()
HAnimJoint121.name = "sacroiliac"
HAnimJoint121.DEF = "hanim_sacroiliac"
HAnimJoint121.center = [0,26.58,-0.5601]
HAnimJoint121.ulimit = [0,0,0]
HAnimJoint121.llimit = [0,0,0]
HAnimSegment122 = x3d.HAnimSegment()
HAnimSegment122.name = "pelvis"
HAnimSegment122.DEF = "hanim_pelvis"
Transform123 = x3d.Transform()
Transform123.translation = [0,26.58,-0.5601]
Shape124 = x3d.Shape()
Appearance125 = x3d.Appearance()
Material126 = x3d.Material()
Material126.diffuseColor = [0.588,0.588,0.588]

Appearance125.material = Material126
ImageTexture127 = x3d.ImageTexture()
ImageTexture127.USE = "HyunTextureAtlas"

Appearance125.texture = ImageTexture127

Shape124.appearance = Appearance125
IndexedFaceSet128 = x3d.IndexedFaceSet()
IndexedFaceSet128.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,5,-1,0,5,6,-1,0,6,7,-1,0,7,8,-1,0,8,9,-1,0,9,10,-1,0,10,11,-1,0,11,12,-1,0,12,1,-1,1,13,14,-1,14,2,1,-1,2,14,15,-1,15,3,2,-1,3,15,16,-1,16,4,3,-1,4,16,17,-1,17,5,4,-1,5,17,18,-1,18,6,5,-1,6,18,19,-1,19,7,6,-1,7,19,20,-1,20,8,7,-1,8,20,21,-1,21,9,8,-1,9,21,22,-1,22,10,9,-1,10,22,23,-1,23,11,10,-1,11,23,24,-1,24,12,11,-1,12,24,13,-1,13,1,12,-1,13,25,26,-1,26,14,13,-1,14,26,27,-1,27,15,14,-1,15,27,28,-1,28,16,15,-1,16,28,29,-1,29,17,16,-1,17,29,30,-1,30,18,17,-1,18,30,31,-1,31,19,18,-1,19,31,32,-1,32,20,19,-1,20,32,33,-1,33,21,20,-1,21,33,34,-1,34,22,21,-1,22,34,35,-1,35,23,22,-1,23,35,36,-1,36,24,23,-1,24,36,25,-1,25,13,24,-1,25,37,38,-1,38,26,25,-1,26,38,39,-1,39,27,26,-1,27,39,40,-1,40,28,27,-1,28,40,41,-1,41,29,28,-1,29,41,42,-1,42,30,29,-1,30,42,43,-1,43,31,30,-1,31,43,44,-1,44,32,31,-1,32,44,45,-1,45,33,32,-1,33,45,46,-1,46,34,33,-1,34,46,47,-1,47,35,34,-1,35,47,48,-1,48,36,35,-1,36,48,37,-1,37,25,36,-1,37,49,50,-1,50,38,37,-1,38,50,51,-1,51,39,38,-1,39,51,52,-1,52,40,39,-1,40,52,53,-1,53,41,40,-1,41,53,54,-1,54,42,41,-1,42,54,55,-1,55,43,42,-1,43,55,56,-1,56,44,43,-1,44,56,57,-1,57,45,44,-1,45,57,58,-1,58,46,45,-1,46,58,59,-1,59,47,46,-1,47,59,60,-1,60,48,47,-1,48,60,49,-1,49,37,48,-1,61,50,49,-1,61,51,50,-1,61,52,51,-1,61,53,52,-1,61,54,53,-1,61,55,54,-1,61,56,55,-1,61,57,56,-1,61,58,57,-1,61,59,58,-1,61,60,59,-1,61,49,60,-1]
IndexedFaceSet128.creaseAngle = 1.57
IndexedFaceSet128.texCoordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,5,-1,0,5,6,-1,0,6,7,-1,0,7,8,-1,0,8,9,-1,0,9,10,-1,0,10,11,-1,0,11,12,-1,0,12,1,-1,1,13,14,-1,14,2,1,-1,2,14,15,-1,15,3,2,-1,3,15,16,-1,16,4,3,-1,4,16,17,-1,17,5,4,-1,5,17,18,-1,18,6,5,-1,6,18,19,-1,19,7,6,-1,7,19,20,-1,20,8,7,-1,8,20,21,-1,21,9,8,-1,9,21,22,-1,22,10,9,-1,10,22,23,-1,23,11,10,-1,11,23,24,-1,24,12,11,-1,12,24,13,-1,13,1,12,-1,13,25,26,-1,26,14,13,-1,14,26,27,-1,27,15,14,-1,15,27,28,-1,28,16,15,-1,16,28,29,-1,29,17,16,-1,17,29,30,-1,30,18,17,-1,18,30,31,-1,31,19,18,-1,19,31,32,-1,32,20,19,-1,20,32,33,-1,33,21,20,-1,21,33,34,-1,34,22,21,-1,22,34,35,-1,35,23,22,-1,23,35,36,-1,36,24,23,-1,24,36,25,-1,25,13,24,-1,25,37,38,-1,38,26,25,-1,26,38,39,-1,39,27,26,-1,27,39,40,-1,40,28,27,-1,28,40,41,-1,41,29,28,-1,29,41,42,-1,42,30,29,-1,30,42,43,-1,43,31,30,-1,31,43,44,-1,44,32,31,-1,32,44,45,-1,45,33,32,-1,33,45,46,-1,46,34,33,-1,34,46,47,-1,47,35,34,-1,35,47,48,-1,48,36,35,-1,36,48,37,-1,37,25,36,-1,37,49,50,-1,50,38,37,-1,38,50,51,-1,51,39,38,-1,39,51,52,-1,52,40,39,-1,40,52,53,-1,53,41,40,-1,41,53,54,-1,54,42,41,-1,42,54,55,-1,55,43,42,-1,43,55,56,-1,56,44,43,-1,44,56,57,-1,57,45,44,-1,45,57,58,-1,58,46,45,-1,46,58,59,-1,59,47,46,-1,47,59,60,-1,60,48,47,-1,48,60,49,-1,49,37,48,-1,61,50,49,-1,61,51,50,-1,61,52,51,-1,61,53,52,-1,61,54,53,-1,61,55,54,-1,61,56,55,-1,61,57,56,-1,61,58,57,-1,61,59,58,-1,61,60,59,-1,61,49,60,-1]
Coordinate129 = x3d.Coordinate()

IndexedFaceSet128.coord = Coordinate129
TextureCoordinate130 = x3d.TextureCoordinate()

IndexedFaceSet128.texCoord = TextureCoordinate130

Shape124.geometry = IndexedFaceSet128

Transform123.children.append(Shape124)

HAnimSegment122.children.append(Transform123)

HAnimJoint121.children.append(HAnimSegment122)
HAnimJoint131 = x3d.HAnimJoint()
HAnimJoint131.name = "l_shoulder"
HAnimJoint131.DEF = "hanim_l_shoulder"
HAnimJoint131.center = [5.502,45.779999,-0.3559]
HAnimJoint131.ulimit = [0,0,0]
HAnimJoint131.llimit = [0,0,0]
HAnimSegment132 = x3d.HAnimSegment()
HAnimSegment132.name = "l_upperarm"
HAnimSegment132.DEF = "hanim_l_upperarm"
Transform133 = x3d.Transform()
Transform133.translation = [5.502,45.779999,-0.3559]
Shape134 = x3d.Shape()
Appearance135 = x3d.Appearance()
Material136 = x3d.Material()
Material136.diffuseColor = [0.588,0.588,0.588]

Appearance135.material = Material136
ImageTexture137 = x3d.ImageTexture()
ImageTexture137.USE = "HyunTextureAtlas"

Appearance135.texture = ImageTexture137

Shape134.appearance = Appearance135
IndexedFaceSet138 = x3d.IndexedFaceSet()
IndexedFaceSet138.coordIndex = [2,1,0,-1,0,4,3,-1,2,0,3,-1,6,5,0,-1,0,1,6,-1,7,6,1,-1,1,2,7,-1,8,7,2,-1,2,3,8,-1,9,8,3,-1,3,4,9,-1,5,9,4,-1,4,0,5,-1,11,10,5,-1,5,6,11,-1,12,11,6,-1,6,7,12,-1,13,12,7,-1,7,8,13,-1,14,13,8,-1,8,9,14,-1,10,14,9,-1,9,5,10,-1,16,15,10,-1,10,11,16,-1,17,16,11,-1,11,12,17,-1,18,17,12,-1,12,13,18,-1,19,18,13,-1,13,14,19,-1,15,19,14,-1,14,10,15,-1,36,37,38,-1,38,39,35,-1,36,38,35,-1,15,16,21,-1,21,20,15,-1,16,17,22,-1,22,21,16,-1,17,18,23,-1,23,22,17,-1,18,19,24,-1,24,23,18,-1,19,15,20,-1,20,24,19,-1,20,21,26,-1,26,25,20,-1,21,22,27,-1,27,26,21,-1,22,23,28,-1,28,27,22,-1,23,24,29,-1,29,28,23,-1,24,20,25,-1,25,29,24,-1,25,26,31,-1,31,30,25,-1,26,27,32,-1,32,31,26,-1,27,28,33,-1,33,32,27,-1,28,29,34,-1,34,33,28,-1,29,25,30,-1,30,34,29,-1,30,31,36,-1,36,35,30,-1,31,32,37,-1,37,36,31,-1,32,33,38,-1,38,37,32,-1,33,34,39,-1,39,38,33,-1,34,30,35,-1,35,39,34,-1]
IndexedFaceSet138.creaseAngle = 1.57
IndexedFaceSet138.texCoordIndex = [2,0,1,-1,1,61,3,-1,2,1,3,-1,5,6,1,-1,1,0,5,-1,7,5,0,-1,0,2,7,-1,8,7,2,-1,2,3,8,-1,9,26,25,-1,25,4,9,-1,6,9,4,-1,4,1,6,-1,10,11,6,-1,6,5,10,-1,12,10,5,-1,5,7,12,-1,13,12,7,-1,7,8,13,-1,14,28,27,-1,27,9,14,-1,11,14,9,-1,9,6,11,-1,15,16,11,-1,11,10,15,-1,17,15,10,-1,10,12,17,-1,18,17,12,-1,12,13,18,-1,19,30,29,-1,29,14,19,-1,16,19,14,-1,14,11,16,-1,54,35,36,-1,36,37,53,-1,54,36,53,-1,16,15,20,-1,20,21,16,-1,15,17,22,-1,22,20,15,-1,17,18,23,-1,23,22,17,-1,31,19,24,-1,24,32,31,-1,19,16,21,-1,21,24,19,-1,38,39,40,-1,40,41,38,-1,55,42,43,-1,43,56,55,-1,42,44,45,-1,45,43,42,-1,44,46,47,-1,47,45,44,-1,46,38,41,-1,41,47,46,-1,41,40,48,-1,48,49,41,-1,57,43,50,-1,50,58,57,-1,43,45,51,-1,51,50,43,-1,45,47,52,-1,52,51,45,-1,47,41,49,-1,49,52,47,-1,49,48,34,-1,34,33,49,-1,59,50,35,-1,35,60,59,-1,50,51,36,-1,36,35,50,-1,51,52,37,-1,37,36,51,-1,52,49,33,-1,33,37,52,-1]
Coordinate139 = x3d.Coordinate()

IndexedFaceSet138.coord = Coordinate139
TextureCoordinate140 = x3d.TextureCoordinate()

IndexedFaceSet138.texCoord = TextureCoordinate140

Shape134.geometry = IndexedFaceSet138

Transform133.children.append(Shape134)

HAnimSegment132.children.append(Transform133)

HAnimJoint131.children.append(HAnimSegment132)
HAnimJoint141 = x3d.HAnimJoint()
HAnimJoint141.name = "l_elbow"
HAnimJoint141.DEF = "hanim_l_elbow"
HAnimJoint141.center = [6.735,35.669998,-0.4487]
HAnimJoint141.ulimit = [0,0,0]
HAnimJoint141.llimit = [0,0,0]
HAnimSegment142 = x3d.HAnimSegment()
HAnimSegment142.name = "l_forearm"
HAnimSegment142.DEF = "hanim_l_forearm"
Transform143 = x3d.Transform()
Transform143.translation = [6.735,35.669998,-0.4487]
Shape144 = x3d.Shape()
Appearance145 = x3d.Appearance()
Material146 = x3d.Material()
Material146.diffuseColor = [0.588,0.588,0.588]

Appearance145.material = Material146
ImageTexture147 = x3d.ImageTexture()
ImageTexture147.USE = "HyunTextureAtlas"

Appearance145.texture = ImageTexture147

Shape144.appearance = Appearance145
IndexedFaceSet148 = x3d.IndexedFaceSet()
IndexedFaceSet148.coordIndex = [3,2,1,-1,3,1,0,-1,3,0,4,-1,6,5,0,-1,0,1,6,-1,7,6,1,-1,1,2,7,-1,8,7,2,-1,2,3,8,-1,9,8,3,-1,3,4,9,-1,5,9,4,-1,4,0,5,-1,11,10,5,-1,5,6,11,-1,12,11,6,-1,6,7,12,-1,13,12,7,-1,7,8,13,-1,14,13,8,-1,8,9,14,-1,10,14,9,-1,9,5,10,-1,16,15,10,-1,10,11,16,-1,17,16,11,-1,11,12,17,-1,18,17,12,-1,12,13,18,-1,19,18,13,-1,13,14,19,-1,15,19,14,-1,14,10,15,-1,21,22,23,-1,23,24,20,-1,21,23,20,-1,15,16,21,-1,21,20,15,-1,16,17,22,-1,22,21,16,-1,17,18,23,-1,23,22,17,-1,18,19,24,-1,24,23,18,-1,19,15,20,-1,20,24,19,-1]
IndexedFaceSet148.creaseAngle = 1.57
IndexedFaceSet148.texCoordIndex = [3,2,25,-1,3,25,26,-1,3,26,4,-1,5,6,1,-1,1,0,5,-1,7,28,27,-1,27,2,7,-1,8,7,2,-1,2,3,8,-1,9,8,3,-1,3,4,9,-1,6,9,4,-1,4,1,6,-1,10,11,6,-1,6,5,10,-1,12,30,29,-1,29,7,12,-1,13,12,7,-1,7,8,13,-1,14,13,8,-1,8,9,14,-1,11,14,9,-1,9,6,11,-1,15,16,11,-1,11,10,15,-1,17,32,31,-1,31,12,17,-1,18,17,12,-1,12,13,18,-1,19,18,13,-1,13,14,19,-1,16,19,14,-1,14,11,16,-1,34,22,23,-1,23,24,33,-1,34,23,33,-1,16,15,21,-1,21,20,16,-1,35,17,22,-1,22,36,35,-1,17,18,23,-1,23,22,17,-1,18,19,24,-1,24,23,18,-1,19,16,20,-1,20,24,19,-1]
Coordinate149 = x3d.Coordinate()

IndexedFaceSet148.coord = Coordinate149
TextureCoordinate150 = x3d.TextureCoordinate()

IndexedFaceSet148.texCoord = TextureCoordinate150

Shape144.geometry = IndexedFaceSet148

Transform143.children.append(Shape144)

HAnimSegment142.children.append(Transform143)

HAnimJoint141.children.append(HAnimSegment142)
HAnimJoint151 = x3d.HAnimJoint()
HAnimJoint151.name = "l_radiocarpal"
HAnimJoint151.DEF = "hanim_l_radiocarpal"
HAnimJoint151.center = [6.432,27.83,-0.1589]
HAnimJoint151.ulimit = [0,0,0]
HAnimJoint151.llimit = [0,0,0]
HAnimSegment152 = x3d.HAnimSegment()
HAnimSegment152.name = "l_carpal"
HAnimSegment152.DEF = "hanim_l_carpal"
Transform153 = x3d.Transform()
Transform153.translation = [6.432,27.83,-0.1589]
Shape154 = x3d.Shape()
Appearance155 = x3d.Appearance()
Material156 = x3d.Material()
Material156.diffuseColor = [0.588,0.588,0.588]

Appearance155.material = Material156
ImageTexture157 = x3d.ImageTexture()
ImageTexture157.USE = "HyunTextureAtlas"

Appearance155.texture = ImageTexture157

Shape154.appearance = Appearance155
IndexedFaceSet158 = x3d.IndexedFaceSet()
IndexedFaceSet158.coordIndex = [0,2,4,-1,4,5,0,-1,3,1,6,-1,6,7,3,-1,5,6,1,-1,1,0,5,-1,5,4,8,-1,8,9,5,-1,7,6,10,-1,10,11,7,-1,6,5,9,-1,9,10,6,-1,9,8,12,-1,12,13,9,-1,11,10,14,-1,14,15,11,-1,10,9,13,-1,13,14,10,-1,4,2,16,-1,7,16,2,-1,2,3,7,-1,18,20,17,-1,17,19,18,-1,7,11,21,-1,21,16,7,-1,8,21,12,-1,11,15,12,-1,12,21,11,-1,15,14,13,-1,13,12,15,-1,19,17,8,-1,8,4,19,-1,18,19,4,-1,4,16,18,-1,20,18,16,-1,16,21,20,-1,17,20,21,-1,21,8,17,-1,22,27,23,-1,26,25,24,-1]
IndexedFaceSet158.creaseAngle = 1.57
IndexedFaceSet158.texCoordIndex = [5,7,4,-1,4,6,5,-1,1,0,2,-1,2,3,1,-1,15,17,14,-1,14,16,15,-1,6,4,8,-1,8,9,6,-1,39,41,38,-1,38,40,39,-1,36,37,18,-1,18,19,36,-1,9,8,10,-1,10,11,9,-1,40,38,42,-1,42,43,40,-1,19,18,20,-1,20,21,19,-1,22,24,23,-1,25,23,24,-1,24,26,25,-1,28,30,27,-1,27,29,28,-1,25,32,31,-1,31,23,25,-1,33,31,34,-1,32,35,34,-1,34,31,32,-1,35,21,20,-1,20,34,35,-1,12,13,8,-1,8,4,12,-1,28,29,22,-1,22,23,28,-1,30,28,23,-1,23,31,30,-1,27,30,31,-1,31,33,27,-1,14,24,26,-1,14,16,24,-1]
Coordinate159 = x3d.Coordinate()

IndexedFaceSet158.coord = Coordinate159
TextureCoordinate160 = x3d.TextureCoordinate()

IndexedFaceSet158.texCoord = TextureCoordinate160

Shape154.geometry = IndexedFaceSet158

Transform153.children.append(Shape154)

HAnimSegment152.children.append(Transform153)

HAnimJoint151.children.append(HAnimSegment152)

HAnimJoint141.children.append(HAnimJoint151)

HAnimJoint131.children.append(HAnimJoint141)

HAnimJoint121.children.append(HAnimJoint131)
HAnimJoint161 = x3d.HAnimJoint()
HAnimJoint161.name = "r_shoulder"
HAnimJoint161.DEF = "hanim_r_shoulder"
HAnimJoint161.center = [-5.502,45.779999,-0.3559]
HAnimJoint161.ulimit = [0,0,0]
HAnimJoint161.llimit = [0,0,0]
HAnimSegment162 = x3d.HAnimSegment()
HAnimSegment162.name = "r_upperarm"
HAnimSegment162.DEF = "hanim_r_upperarm"
Transform163 = x3d.Transform()
Transform163.translation = [-5.502,45.779999,-0.3559]
Shape164 = x3d.Shape()
Appearance165 = x3d.Appearance()
Material166 = x3d.Material()
Material166.diffuseColor = [0.588,0.588,0.588]

Appearance165.material = Material166
ImageTexture167 = x3d.ImageTexture()
ImageTexture167.USE = "HyunTextureAtlas"

Appearance165.texture = ImageTexture167

Shape164.appearance = Appearance165
IndexedFaceSet168 = x3d.IndexedFaceSet()
IndexedFaceSet168.coordIndex = [3,4,0,-1,2,3,0,-1,2,0,1,-1,6,1,0,-1,0,5,6,-1,7,2,1,-1,1,6,7,-1,8,3,2,-1,2,7,8,-1,9,4,3,-1,3,8,9,-1,5,0,4,-1,4,9,5,-1,11,6,5,-1,5,10,11,-1,12,7,6,-1,6,11,12,-1,13,8,7,-1,7,12,13,-1,14,9,8,-1,8,13,14,-1,10,5,9,-1,9,14,10,-1,16,11,10,-1,10,15,16,-1,17,12,11,-1,11,16,17,-1,18,13,12,-1,12,17,18,-1,19,14,13,-1,13,18,19,-1,15,10,14,-1,14,19,15,-1,35,39,38,-1,36,35,38,-1,36,38,37,-1,15,20,21,-1,21,16,15,-1,16,21,22,-1,22,17,16,-1,17,22,23,-1,23,18,17,-1,18,23,24,-1,24,19,18,-1,19,24,20,-1,20,15,19,-1,20,25,26,-1,26,21,20,-1,21,26,27,-1,27,22,21,-1,22,27,28,-1,28,23,22,-1,23,28,29,-1,29,24,23,-1,24,29,25,-1,25,20,24,-1,25,30,31,-1,31,26,25,-1,26,31,32,-1,32,27,26,-1,27,32,33,-1,33,28,27,-1,28,33,34,-1,34,29,28,-1,29,34,30,-1,30,25,29,-1,30,35,36,-1,36,31,30,-1,31,36,37,-1,37,32,31,-1,32,37,38,-1,38,33,32,-1,33,38,39,-1,39,34,33,-1,34,39,35,-1,35,30,34,-1]
IndexedFaceSet168.creaseAngle = 1.57
IndexedFaceSet168.texCoordIndex = [3,61,1,-1,2,3,1,-1,2,1,0,-1,5,0,1,-1,1,6,5,-1,7,2,0,-1,0,5,7,-1,8,3,2,-1,2,7,8,-1,9,4,25,-1,25,26,9,-1,6,1,4,-1,4,9,6,-1,10,5,6,-1,6,11,10,-1,12,7,5,-1,5,10,12,-1,13,8,7,-1,7,12,13,-1,14,9,27,-1,27,28,14,-1,11,6,9,-1,9,14,11,-1,15,10,11,-1,11,16,15,-1,17,12,10,-1,10,15,17,-1,18,13,12,-1,12,17,18,-1,19,14,29,-1,29,30,19,-1,16,11,14,-1,14,19,16,-1,53,37,36,-1,54,53,36,-1,54,36,35,-1,16,21,20,-1,20,15,16,-1,15,20,22,-1,22,17,15,-1,17,22,23,-1,23,18,17,-1,31,32,24,-1,24,19,31,-1,19,24,21,-1,21,16,19,-1,38,41,40,-1,40,39,38,-1,55,56,43,-1,43,42,55,-1,42,43,45,-1,45,44,42,-1,44,45,47,-1,47,46,44,-1,46,47,41,-1,41,38,46,-1,41,49,48,-1,48,40,41,-1,57,58,50,-1,50,43,57,-1,43,50,51,-1,51,45,43,-1,45,51,52,-1,52,47,45,-1,47,52,49,-1,49,41,47,-1,49,33,34,-1,34,48,49,-1,59,60,35,-1,35,50,59,-1,50,35,36,-1,36,51,50,-1,51,36,37,-1,37,52,51,-1,52,37,33,-1,33,49,52,-1]
Coordinate169 = x3d.Coordinate()

IndexedFaceSet168.coord = Coordinate169
TextureCoordinate170 = x3d.TextureCoordinate()

IndexedFaceSet168.texCoord = TextureCoordinate170

Shape164.geometry = IndexedFaceSet168

Transform163.children.append(Shape164)

HAnimSegment162.children.append(Transform163)

HAnimJoint161.children.append(HAnimSegment162)
HAnimJoint171 = x3d.HAnimJoint()
HAnimJoint171.name = "r_elbow"
HAnimJoint171.DEF = "hanim_r_elbow"
HAnimJoint171.center = [-6.735,35.669998,-0.4487]
HAnimJoint171.ulimit = [0,0,0]
HAnimJoint171.llimit = [0,0,0]
HAnimSegment172 = x3d.HAnimSegment()
HAnimSegment172.name = "r_forearm"
HAnimSegment172.DEF = "hanim_r_forearm"
Transform173 = x3d.Transform()
Transform173.translation = [-6.735,35.669998,-0.4487]
Shape174 = x3d.Shape()
Appearance175 = x3d.Appearance()
Material176 = x3d.Material()
Material176.diffuseColor = [0.588,0.588,0.588]

Appearance175.material = Material176
ImageTexture177 = x3d.ImageTexture()
ImageTexture177.USE = "HyunTextureAtlas"

Appearance175.texture = ImageTexture177

Shape174.appearance = Appearance175
IndexedFaceSet178 = x3d.IndexedFaceSet()
IndexedFaceSet178.coordIndex = [3,4,0,-1,3,0,1,-1,3,1,2,-1,6,1,0,-1,0,5,6,-1,7,2,1,-1,1,6,7,-1,8,3,2,-1,2,7,8,-1,9,4,3,-1,3,8,9,-1,5,0,4,-1,4,9,5,-1,11,6,5,-1,5,10,11,-1,12,7,6,-1,6,11,12,-1,13,8,7,-1,7,12,13,-1,14,9,8,-1,8,13,14,-1,10,5,9,-1,9,14,10,-1,16,11,10,-1,10,15,16,-1,17,12,11,-1,11,16,17,-1,18,13,12,-1,12,17,18,-1,19,14,13,-1,13,18,19,-1,15,10,14,-1,14,19,15,-1,20,24,23,-1,21,20,23,-1,21,23,22,-1,15,20,21,-1,21,16,15,-1,16,21,22,-1,22,17,16,-1,17,22,23,-1,23,18,17,-1,18,23,24,-1,24,19,18,-1,19,24,20,-1,20,15,19,-1]
IndexedFaceSet178.creaseAngle = 1.57
IndexedFaceSet178.texCoordIndex = [3,4,26,-1,3,26,25,-1,3,25,2,-1,5,0,1,-1,1,6,5,-1,7,2,27,-1,27,28,7,-1,8,3,2,-1,2,7,8,-1,9,4,3,-1,3,8,9,-1,6,1,4,-1,4,9,6,-1,10,5,6,-1,6,11,10,-1,12,7,29,-1,29,30,12,-1,13,8,7,-1,7,12,13,-1,14,9,8,-1,8,13,14,-1,11,6,9,-1,9,14,11,-1,15,10,11,-1,11,16,15,-1,17,12,31,-1,31,32,17,-1,18,13,12,-1,12,17,18,-1,19,14,13,-1,13,18,19,-1,16,11,14,-1,14,19,16,-1,33,24,23,-1,34,33,23,-1,34,23,22,-1,16,20,21,-1,21,15,16,-1,35,36,22,-1,22,17,35,-1,17,22,23,-1,23,18,17,-1,18,23,24,-1,24,19,18,-1,19,24,20,-1,20,16,19,-1]
Coordinate179 = x3d.Coordinate()

IndexedFaceSet178.coord = Coordinate179
TextureCoordinate180 = x3d.TextureCoordinate()

IndexedFaceSet178.texCoord = TextureCoordinate180

Shape174.geometry = IndexedFaceSet178

Transform173.children.append(Shape174)

HAnimSegment172.children.append(Transform173)

HAnimJoint171.children.append(HAnimSegment172)
HAnimJoint181 = x3d.HAnimJoint()
HAnimJoint181.name = "r_radiocarpal"
HAnimJoint181.DEF = "hanim_r_radiocarpal"
HAnimJoint181.center = [-6.432,27.83,-0.1589]
HAnimJoint181.ulimit = [0,0,0]
HAnimJoint181.llimit = [0,0,0]
HAnimSegment182 = x3d.HAnimSegment()
HAnimSegment182.name = "r_carpal"
HAnimSegment182.DEF = "hanim_r_carpal"
Transform183 = x3d.Transform()
Transform183.translation = [-6.432,27.83,-0.1589]
Shape184 = x3d.Shape()
Appearance185 = x3d.Appearance()
Material186 = x3d.Material()
Material186.diffuseColor = [0.588,0.588,0.588]

Appearance185.material = Material186
ImageTexture187 = x3d.ImageTexture()
ImageTexture187.USE = "HyunTextureAtlas"

Appearance185.texture = ImageTexture187

Shape184.appearance = Appearance185
IndexedFaceSet188 = x3d.IndexedFaceSet()
IndexedFaceSet188.coordIndex = [0,5,4,-1,4,2,0,-1,3,7,6,-1,6,1,3,-1,5,0,1,-1,1,6,5,-1,5,9,8,-1,8,4,5,-1,7,11,10,-1,10,6,7,-1,6,10,9,-1,9,5,6,-1,9,13,12,-1,12,8,9,-1,11,15,14,-1,14,10,11,-1,10,14,13,-1,13,9,10,-1,4,16,2,-1,7,3,2,-1,2,16,7,-1,18,19,17,-1,17,20,18,-1,7,16,21,-1,21,11,7,-1,8,12,21,-1,11,21,12,-1,12,15,11,-1,15,12,13,-1,13,14,15,-1,19,4,8,-1,8,17,19,-1,18,16,4,-1,4,19,18,-1,20,21,16,-1,16,18,20,-1,17,8,21,-1,21,20,17,-1,22,23,27,-1,26,24,25,-1]
IndexedFaceSet188.creaseAngle = 1.57
IndexedFaceSet188.texCoordIndex = [5,6,4,-1,4,7,5,-1,1,3,2,-1,2,0,1,-1,15,16,14,-1,14,17,15,-1,6,9,8,-1,8,4,6,-1,39,40,38,-1,38,41,39,-1,36,19,18,-1,18,37,36,-1,9,11,10,-1,10,8,9,-1,40,43,42,-1,42,38,40,-1,19,21,20,-1,20,18,19,-1,22,23,24,-1,25,26,24,-1,24,23,25,-1,28,29,27,-1,27,30,28,-1,25,23,31,-1,31,32,25,-1,33,34,31,-1,32,31,34,-1,34,35,32,-1,35,34,20,-1,20,21,35,-1,12,4,8,-1,8,13,12,-1,28,23,22,-1,22,29,28,-1,30,31,23,-1,23,28,30,-1,27,33,31,-1,31,30,27,-1,14,26,24,-1,14,24,16,-1]
Coordinate189 = x3d.Coordinate()

IndexedFaceSet188.coord = Coordinate189
TextureCoordinate190 = x3d.TextureCoordinate()

IndexedFaceSet188.texCoord = TextureCoordinate190

Shape184.geometry = IndexedFaceSet188

Transform183.children.append(Shape184)

HAnimSegment182.children.append(Transform183)

HAnimJoint181.children.append(HAnimSegment182)

HAnimJoint171.children.append(HAnimJoint181)

HAnimJoint161.children.append(HAnimJoint171)

HAnimJoint121.children.append(HAnimJoint161)
HAnimJoint191 = x3d.HAnimJoint()
HAnimJoint191.name = "vl5"
HAnimJoint191.DEF = "hanim_vl5"
HAnimJoint191.center = [0,35.77,-0.5028]
HAnimJoint191.ulimit = [0,0,0]
HAnimJoint191.llimit = [0,0,0]
HAnimSegment192 = x3d.HAnimSegment()
HAnimSegment192.name = "l5"
HAnimSegment192.DEF = "hanim_l5"
Transform193 = x3d.Transform()
Transform193.translation = [0,35.77,-0.5028]
Shape194 = x3d.Shape()
Appearance195 = x3d.Appearance()
Material196 = x3d.Material()
Material196.diffuseColor = [0.588,0.588,0.588]

Appearance195.material = Material196
ImageTexture197 = x3d.ImageTexture()
ImageTexture197.USE = "HyunTextureAtlas"

Appearance195.texture = ImageTexture197

Shape194.appearance = Appearance195
IndexedFaceSet198 = x3d.IndexedFaceSet()
IndexedFaceSet198.coordIndex = [7,5,3,-1,3,4,7,-1,4,8,7,-1,9,10,1,-1,1,0,9,-1,11,9,0,-1,0,2,11,-1,67,16,15,-1,16,17,14,-1,14,15,16,-1,67,15,8,-1,7,8,15,-1,15,14,7,-1,67,206,16,-1,13,17,16,-1,16,206,13,-1,22,23,21,-1,21,20,22,-1,17,22,20,-1,20,14,17,-1,6,5,20,-1,20,21,6,-1,5,7,14,-1,14,20,5,-1,18,19,23,-1,23,22,18,-1,13,18,22,-1,22,17,13,-1,2,6,11,-1,30,31,28,-1,28,27,30,-1,32,30,27,-1,27,29,32,-1,23,32,29,-1,29,21,23,-1,10,9,27,-1,27,28,10,-1,9,11,29,-1,29,27,9,-1,11,6,21,-1,21,29,11,-1,24,25,31,-1,31,30,24,-1,26,24,30,-1,30,32,26,-1,19,26,32,-1,32,23,19,-1,68,207,206,-1,206,67,68,-1,36,35,24,-1,24,26,36,-1,69,208,207,-1,207,68,69,-1,208,38,34,-1,34,207,208,-1,207,34,39,-1,39,206,207,-1,19,40,26,-1,41,36,26,-1,26,40,41,-1,41,40,39,-1,39,34,41,-1,43,42,35,-1,35,36,43,-1,44,43,36,-1,36,41,44,-1,38,44,41,-1,41,34,38,-1,70,209,208,-1,208,69,70,-1,209,46,38,-1,38,208,209,-1,48,47,42,-1,42,43,48,-1,46,49,44,-1,44,38,46,-1,71,210,209,-1,209,70,71,-1,210,51,46,-1,46,209,210,-1,53,52,47,-1,47,48,53,-1,54,53,48,-1,48,49,54,-1,51,54,49,-1,49,46,51,-1,72,55,210,-1,210,71,72,-1,55,56,51,-1,51,210,55,-1,58,57,52,-1,52,53,58,-1,59,58,53,-1,53,54,59,-1,56,59,54,-1,54,51,56,-1,60,61,19,-1,19,18,60,-1,62,60,18,-1,18,13,62,-1,63,62,13,-1,13,39,63,-1,61,64,40,-1,40,19,61,-1,64,63,39,-1,39,40,64,-1,2,3,5,-1,2,5,6,-1,13,206,39,-1,43,44,49,-1,49,48,43,-1,60,62,63,-1,63,64,60,-1,60,64,61,-1,73,74,65,-1,65,66,73,-1,8,4,74,-1,74,73,8,-1,75,76,73,-1,73,66,75,-1,76,12,8,-1,8,73,76,-1,76,77,33,-1,178,179,212,-1,75,78,77,-1,77,76,75,-1,79,180,181,-1,33,77,213,-1,80,213,77,-1,77,78,80,-1,81,182,183,-1,37,213,214,-1,82,214,213,-1,213,80,82,-1,83,184,185,-1,45,214,215,-1,84,215,214,-1,214,82,84,-1,85,86,50,-1,50,215,85,-1,87,85,215,-1,215,84,87,-1,88,89,86,-1,86,85,88,-1,90,88,85,-1,85,87,90,-1,91,186,187,-1,188,189,216,-1,228,190,191,-1,50,86,230,-1,92,93,211,-1,211,230,92,-1,89,92,230,-1,230,86,89,-1,95,97,99,-1,99,96,95,-1,96,99,100,-1,101,1,10,-1,1,101,102,-1,102,94,1,-1,153,106,107,-1,105,108,107,-1,107,106,105,-1,153,100,106,-1,106,100,99,-1,99,105,106,-1,153,107,217,-1,107,108,104,-1,104,217,107,-1,112,114,113,-1,113,111,112,-1,111,113,108,-1,108,105,111,-1,111,97,98,-1,98,112,111,-1,105,99,97,-1,97,111,105,-1,114,110,109,-1,109,113,114,-1,113,109,104,-1,104,108,113,-1,94,102,98,-1,28,31,119,-1,119,117,28,-1,117,119,120,-1,120,118,117,-1,118,120,114,-1,114,112,118,-1,117,101,10,-1,10,28,117,-1,118,102,101,-1,101,117,118,-1,112,98,102,-1,102,118,112,-1,31,25,115,-1,115,119,31,-1,119,115,116,-1,116,120,119,-1,120,116,110,-1,110,114,120,-1,217,218,154,-1,154,153,217,-1,115,123,124,-1,124,116,115,-1,218,219,155,-1,155,154,218,-1,122,126,219,-1,219,218,122,-1,127,122,218,-1,218,217,127,-1,110,116,128,-1,116,124,129,-1,129,128,116,-1,127,128,129,-1,129,122,127,-1,123,130,131,-1,131,124,123,-1,124,131,132,-1,132,129,124,-1,129,132,126,-1,126,122,129,-1,219,220,156,-1,156,155,219,-1,126,134,220,-1,220,219,126,-1,130,135,136,-1,136,131,130,-1,132,137,134,-1,134,126,132,-1,220,221,157,-1,157,156,220,-1,134,139,221,-1,221,220,134,-1,135,140,141,-1,141,136,135,-1,136,141,142,-1,142,137,136,-1,137,142,139,-1,139,134,137,-1,221,143,158,-1,158,157,221,-1,139,144,143,-1,143,221,139,-1,140,145,146,-1,146,141,140,-1,141,146,147,-1,147,142,141,-1,142,147,144,-1,144,139,142,-1,110,149,148,-1,148,109,110,-1,109,148,150,-1,150,104,109,-1,104,150,151,-1,151,127,104,-1,128,152,149,-1,149,110,128,-1,127,151,152,-1,152,128,127,-1,94,97,95,-1,94,98,97,-1,104,127,217,-1,137,132,131,-1,131,136,137,-1,151,150,148,-1,148,152,151,-1,148,149,152,-1,65,160,159,-1,159,66,65,-1,160,96,100,-1,100,159,160,-1,159,161,75,-1,75,66,159,-1,100,103,161,-1,161,159,100,-1,161,121,162,-1,193,223,192,-1,162,78,75,-1,75,161,162,-1,163,194,195,-1,121,224,162,-1,162,224,80,-1,80,78,162,-1,164,196,197,-1,125,225,224,-1,224,225,82,-1,82,80,224,-1,165,198,199,-1,133,226,225,-1,225,226,84,-1,84,82,225,-1,138,167,166,-1,166,226,138,-1,226,166,87,-1,87,84,226,-1,167,169,168,-1,168,166,167,-1,166,168,90,-1,90,87,166,-1,170,200,201,-1,203,227,202,-1,229,204,205,-1,138,231,167,-1,222,172,171,-1,171,231,222,-1,231,171,169,-1,169,167,231,-1,173,174,35,-1,35,42,173,-1,175,173,42,-1,42,47,175,-1,176,175,47,-1,47,52,176,-1,177,176,52,-1,52,57,177,-1,24,35,174,-1,174,25,24,-1,25,174,123,-1,123,115,25,-1,174,173,130,-1,130,123,174,-1,173,175,135,-1,135,130,173,-1,175,176,140,-1,140,135,175,-1,176,177,145,-1,145,140,176,-1,237,238,233,-1,233,232,237,-1,239,237,232,-1,232,234,239,-1,240,239,234,-1,234,235,240,-1,241,240,235,-1,235,236,241,-1,244,245,242,-1,242,243,244,-1,245,241,236,-1,236,242,245,-1,233,238,250,-1,250,246,233,-1,246,250,251,-1,251,247,246,-1,247,251,252,-1,252,248,247,-1,248,252,253,-1,253,249,248,-1,254,255,244,-1,244,243,254,-1,249,253,255,-1,255,254,249,-1]
IndexedFaceSet198.creaseAngle = 1.57
IndexedFaceSet198.texCoordIndex = [179,180,181,-1,181,182,179,-1,182,183,179,-1,0,1,2,-1,2,3,0,-1,4,0,3,-1,3,5,4,-1,6,7,8,-1,7,10,11,-1,11,8,7,-1,9,8,12,-1,13,12,8,-1,8,11,13,-1,14,15,7,-1,16,10,7,-1,7,15,16,-1,17,18,19,-1,19,20,17,-1,10,17,20,-1,20,11,10,-1,21,22,20,-1,20,19,21,-1,22,13,11,-1,11,20,22,-1,23,24,18,-1,18,17,23,-1,16,23,17,-1,17,10,16,-1,5,21,4,-1,71,26,27,-1,27,72,71,-1,29,25,28,-1,28,30,29,-1,18,29,30,-1,30,19,18,-1,74,232,73,-1,73,27,74,-1,0,4,30,-1,30,28,0,-1,4,21,19,-1,19,30,4,-1,75,32,26,-1,26,76,75,-1,33,31,25,-1,25,29,33,-1,24,33,29,-1,29,18,24,-1,34,35,15,-1,15,14,34,-1,36,37,31,-1,31,33,36,-1,38,39,35,-1,35,34,38,-1,39,40,41,-1,41,35,39,-1,35,41,42,-1,42,15,35,-1,24,43,33,-1,44,36,33,-1,33,43,44,-1,44,43,42,-1,42,41,44,-1,45,46,37,-1,37,36,45,-1,47,45,36,-1,36,44,47,-1,40,47,44,-1,44,41,40,-1,48,49,39,-1,39,38,48,-1,49,50,40,-1,40,39,49,-1,51,52,46,-1,46,45,51,-1,50,53,47,-1,47,40,50,-1,54,55,49,-1,49,48,54,-1,55,56,50,-1,50,49,55,-1,57,58,52,-1,52,51,57,-1,59,57,51,-1,51,53,59,-1,56,59,53,-1,53,50,56,-1,60,61,55,-1,55,54,60,-1,61,62,56,-1,56,55,61,-1,63,64,58,-1,58,57,63,-1,65,63,57,-1,57,59,65,-1,62,65,59,-1,59,56,62,-1,66,67,24,-1,24,23,66,-1,68,66,23,-1,23,16,68,-1,69,68,16,-1,16,42,69,-1,67,70,43,-1,43,24,67,-1,70,69,42,-1,42,43,70,-1,184,181,180,-1,5,22,21,-1,16,15,42,-1,45,47,53,-1,53,51,45,-1,66,68,69,-1,69,70,66,-1,66,70,67,-1,185,186,187,-1,187,188,185,-1,183,182,186,-1,186,185,183,-1,189,190,185,-1,185,188,189,-1,190,191,183,-1,183,185,190,-1,190,192,193,-1,193,191,190,-1,189,194,192,-1,192,190,189,-1,195,196,193,-1,193,192,195,-1,197,195,192,-1,192,194,197,-1,198,199,196,-1,196,195,198,-1,200,198,195,-1,195,197,200,-1,201,202,199,-1,199,198,201,-1,203,201,198,-1,198,200,203,-1,204,205,202,-1,202,201,204,-1,206,204,201,-1,201,203,206,-1,207,208,205,-1,205,204,207,-1,209,207,204,-1,204,206,209,-1,79,80,59,-1,59,56,79,-1,81,82,77,-1,77,78,81,-1,83,84,80,-1,80,79,83,-1,85,86,81,-1,81,78,85,-1,211,212,210,-1,210,213,211,-1,213,210,214,-1,87,89,88,-1,90,87,91,-1,91,92,90,-1,93,95,94,-1,98,97,94,-1,94,95,98,-1,96,99,95,-1,95,99,100,-1,100,98,95,-1,101,94,102,-1,94,97,103,-1,103,102,94,-1,106,105,104,-1,104,107,106,-1,107,104,97,-1,97,98,107,-1,107,109,108,-1,108,106,107,-1,98,100,109,-1,109,107,98,-1,105,111,110,-1,110,104,105,-1,104,110,103,-1,103,97,104,-1,92,91,108,-1,114,113,158,-1,158,159,114,-1,115,112,116,-1,116,117,115,-1,117,116,105,-1,105,106,117,-1,160,233,161,-1,161,114,160,-1,117,91,87,-1,87,115,117,-1,106,108,91,-1,91,117,106,-1,113,119,162,-1,162,163,113,-1,112,118,120,-1,120,116,112,-1,116,120,111,-1,111,105,116,-1,102,122,121,-1,121,101,102,-1,118,124,123,-1,123,120,118,-1,122,126,125,-1,125,121,122,-1,128,127,126,-1,126,122,128,-1,129,128,122,-1,122,102,129,-1,111,120,130,-1,120,123,131,-1,131,130,120,-1,129,130,131,-1,131,128,129,-1,124,133,132,-1,132,123,124,-1,123,132,134,-1,134,131,123,-1,131,134,127,-1,127,128,131,-1,126,136,135,-1,135,125,126,-1,127,137,136,-1,136,126,127,-1,133,139,138,-1,138,132,133,-1,134,140,137,-1,137,127,134,-1,136,142,141,-1,141,135,136,-1,137,143,142,-1,142,136,137,-1,139,145,144,-1,144,138,139,-1,138,144,146,-1,146,140,138,-1,140,146,143,-1,143,137,140,-1,142,148,147,-1,147,141,142,-1,143,149,148,-1,148,142,143,-1,145,151,150,-1,150,144,145,-1,144,150,152,-1,152,146,144,-1,146,152,149,-1,149,143,146,-1,111,154,153,-1,153,110,111,-1,110,153,155,-1,155,103,110,-1,103,155,156,-1,156,129,103,-1,130,157,154,-1,154,111,130,-1,129,156,157,-1,157,130,129,-1,215,212,211,-1,92,108,109,-1,103,129,102,-1,140,134,132,-1,132,138,140,-1,156,155,153,-1,153,157,156,-1,153,154,157,-1,187,217,216,-1,216,188,187,-1,217,213,214,-1,214,216,217,-1,216,218,189,-1,189,188,216,-1,214,219,218,-1,218,216,214,-1,218,220,221,-1,220,218,219,-1,221,194,189,-1,189,218,221,-1,222,220,223,-1,220,222,221,-1,221,222,197,-1,197,194,221,-1,224,223,225,-1,223,224,222,-1,222,224,200,-1,200,197,222,-1,226,225,227,-1,225,226,224,-1,224,226,203,-1,203,200,224,-1,227,229,228,-1,228,226,227,-1,226,228,206,-1,206,203,226,-1,229,231,230,-1,230,228,229,-1,228,230,209,-1,209,206,228,-1,166,146,167,-1,146,166,143,-1,168,164,169,-1,164,168,165,-1,167,171,170,-1,170,166,167,-1,168,173,172,-1,172,165,168,-1,174,175,37,-1,37,46,174,-1,176,174,46,-1,46,52,176,-1,177,176,52,-1,52,58,177,-1,178,177,58,-1,58,64,178,-1,75,37,175,-1,175,32,75,-1,32,175,124,-1,124,162,32,-1,175,174,133,-1,133,124,175,-1,174,176,139,-1,139,133,174,-1,176,177,145,-1,145,139,176,-1,177,178,151,-1,151,145,177,-1,234,235,236,-1,236,237,234,-1,238,234,237,-1,237,239,238,-1,240,238,239,-1,239,241,240,-1,242,240,241,-1,241,243,242,-1,244,245,246,-1,246,247,244,-1,245,242,243,-1,243,246,245,-1,236,235,248,-1,248,249,236,-1,249,248,250,-1,250,251,249,-1,251,250,252,-1,252,253,251,-1,253,252,254,-1,254,255,253,-1,256,257,244,-1,244,247,256,-1,255,254,257,-1,257,256,255,-1]
Coordinate199 = x3d.Coordinate()

IndexedFaceSet198.coord = Coordinate199
TextureCoordinate200 = x3d.TextureCoordinate()

IndexedFaceSet198.texCoord = TextureCoordinate200

Shape194.geometry = IndexedFaceSet198

Transform193.children.append(Shape194)

HAnimSegment192.children.append(Transform193)

HAnimJoint191.children.append(HAnimSegment192)
HAnimJoint201 = x3d.HAnimJoint()
HAnimJoint201.name = "skullbase"
HAnimJoint201.DEF = "hanim_skullbase"
HAnimJoint201.center = [0,49.98,-0.5228]
HAnimJoint201.ulimit = [0,0,0]
HAnimJoint201.llimit = [0,0,0]
HAnimSegment202 = x3d.HAnimSegment()
HAnimSegment202.name = "skull"
HAnimSegment202.DEF = "hanim_skull"
Transform203 = x3d.Transform()
Transform203.translation = [0,49.98,-0.5228]
Shape204 = x3d.Shape()
Appearance205 = x3d.Appearance()
Material206 = x3d.Material()
Material206.diffuseColor = [0.588,0.588,0.588]

Appearance205.material = Material206
ImageTexture207 = x3d.ImageTexture()
ImageTexture207.USE = "HyunTextureAtlas"

Appearance205.texture = ImageTexture207

Shape204.appearance = Appearance205
IndexedFaceSet208 = x3d.IndexedFaceSet()
IndexedFaceSet208.coordIndex = [118,28,42,-1,42,25,118,-1,26,40,27,-1,39,38,24,-1,24,23,39,-1,58,22,24,-1,24,38,58,-1,120,41,28,-1,28,118,120,-1,295,56,30,-1,30,32,295,-1,56,37,31,-1,29,31,35,-1,35,33,29,-1,29,33,34,-1,34,30,29,-1,30,34,36,-1,36,32,30,-1,37,35,31,-1,295,32,36,-1,40,33,35,-1,44,36,34,-1,37,40,35,-1,295,36,44,-1,57,58,38,-1,39,40,38,-1,27,39,23,-1,23,20,27,-1,40,39,27,-1,294,48,41,-1,41,19,294,-1,28,41,48,-1,48,49,28,-1,28,49,50,-1,50,42,28,-1,19,293,294,-1,54,48,294,-1,294,17,54,-1,17,294,293,-1,119,52,295,-1,90,93,45,-1,45,92,90,-1,14,81,45,-1,45,93,14,-1,16,72,14,-1,97,96,46,-1,95,97,46,-1,46,88,95,-1,96,90,46,-1,92,46,90,-1,92,87,46,-1,117,91,47,-1,47,103,117,-1,86,47,87,-1,87,102,86,-1,86,116,103,-1,103,47,86,-1,87,47,91,-1,49,53,51,-1,49,48,54,-1,54,53,49,-1,16,22,58,-1,58,72,16,-1,73,68,51,-1,51,53,73,-1,52,51,68,-1,68,295,52,-1,53,54,75,-1,75,74,53,-1,73,53,74,-1,75,54,76,-1,65,69,56,-1,56,69,70,-1,70,37,56,-1,37,70,71,-1,71,57,37,-1,66,64,67,-1,77,67,64,-1,65,64,66,-1,66,69,65,-1,67,59,60,-1,67,82,59,-1,82,111,59,-1,60,59,104,-1,104,59,62,-1,111,61,59,-1,61,63,59,-1,62,59,63,-1,77,64,65,-1,65,78,77,-1,68,73,78,-1,78,65,68,-1,69,66,79,-1,79,70,69,-1,70,79,80,-1,80,71,70,-1,14,72,81,-1,73,74,83,-1,83,78,73,-1,74,75,109,-1,109,83,74,-1,75,76,114,-1,114,109,75,-1,4,115,15,-1,76,15,115,-1,115,114,76,-1,60,66,67,-1,66,60,105,-1,82,67,77,-1,77,84,82,-1,78,83,84,-1,84,77,78,-1,105,106,79,-1,79,66,105,-1,106,100,80,-1,80,79,106,-1,110,111,82,-1,82,84,110,-1,110,84,83,-1,83,109,110,-1,113,85,108,-1,108,107,113,-1,85,99,116,-1,116,86,85,-1,89,88,87,-1,94,95,88,-1,88,89,94,-1,89,91,117,-1,117,94,89,-1,91,89,87,-1,14,93,13,-1,9,12,90,-1,90,96,9,-1,12,13,93,-1,93,90,12,-1,94,11,10,-1,10,95,94,-1,11,94,117,-1,117,0,11,-1,8,97,95,-1,95,10,8,-1,8,9,96,-1,96,97,8,-1,1,99,7,-1,3,6,98,-1,98,112,3,-1,7,99,98,-1,98,6,7,-1,113,112,98,-1,108,101,100,-1,100,106,108,-1,113,98,85,-1,99,85,98,-1,103,116,2,-1,2,5,103,-1,5,0,117,-1,117,103,5,-1,62,113,107,-1,107,104,62,-1,108,106,105,-1,105,107,108,-1,110,109,114,-1,114,115,110,-1,3,112,115,-1,115,4,3,-1,61,111,110,-1,110,115,61,-1,61,115,112,-1,112,63,61,-1,62,63,112,-1,112,113,62,-1,2,116,1,-1,116,99,1,-1,86,102,85,-1,102,101,108,-1,85,102,108,-1,57,38,40,-1,37,57,40,-1,105,60,104,-1,107,105,104,-1,15,76,54,-1,17,15,54,-1,87,88,46,-1,41,120,21,-1,19,41,21,-1,72,58,122,-1,123,100,101,-1,101,121,123,-1,100,123,124,-1,124,80,100,-1,80,124,122,-1,122,71,80,-1,101,87,121,-1,57,71,122,-1,58,57,122,-1,121,92,45,-1,45,123,121,-1,123,45,81,-1,81,124,123,-1,124,81,72,-1,72,122,124,-1,87,92,121,-1,87,101,102,-1,40,26,44,-1,119,295,44,-1,44,34,33,-1,40,44,33,-1,29,30,56,-1,31,29,56,-1,68,65,56,-1,295,68,56,-1,55,147,131,-1,132,131,147,-1,147,140,132,-1,132,140,141,-1,141,133,132,-1,133,141,142,-1,142,134,133,-1,134,142,125,-1,125,130,134,-1,129,135,18,-1,277,278,296,-1,137,279,280,-1,281,282,297,-1,304,136,49,-1,49,136,146,-1,146,52,49,-1,52,146,147,-1,298,283,284,-1,136,145,146,-1,128,126,143,-1,143,144,139,-1,145,139,144,-1,139,128,143,-1,136,139,145,-1,135,138,304,-1,304,43,135,-1,129,127,138,-1,138,135,129,-1,138,139,136,-1,136,304,138,-1,138,127,128,-1,128,139,138,-1,143,126,125,-1,125,142,143,-1,144,143,142,-1,142,141,144,-1,145,144,141,-1,141,140,145,-1,146,145,140,-1,140,147,146,-1,52,119,42,-1,42,50,52,-1,148,149,118,-1,118,25,148,-1,149,150,120,-1,120,118,149,-1,150,151,21,-1,21,120,150,-1,26,152,149,-1,149,148,26,-1,152,153,150,-1,150,149,152,-1,153,154,151,-1,151,150,153,-1,26,27,152,-1,153,152,27,-1,27,20,154,-1,154,153,27,-1,42,119,148,-1,148,25,42,-1,148,119,26,-1,119,44,26,-1,49,52,50,-1,172,158,248,-1,248,155,172,-1,156,157,170,-1,24,168,169,-1,169,23,24,-1,24,22,188,-1,188,168,24,-1,158,171,250,-1,250,248,158,-1,160,186,300,-1,300,162,160,-1,186,161,167,-1,165,161,159,-1,159,163,165,-1,164,163,159,-1,159,160,164,-1,166,164,160,-1,160,162,166,-1,167,161,165,-1,300,166,162,-1,170,165,163,-1,174,164,166,-1,167,165,170,-1,300,174,166,-1,187,168,188,-1,169,168,170,-1,23,169,157,-1,157,20,23,-1,170,157,169,-1,171,178,299,-1,299,19,171,-1,178,171,158,-1,158,179,178,-1,180,179,158,-1,158,172,180,-1,19,299,293,-1,299,178,184,-1,184,17,299,-1,17,293,299,-1,249,300,182,-1,175,223,220,-1,220,222,175,-1,175,211,14,-1,14,223,175,-1,16,14,202,-1,227,176,226,-1,176,227,225,-1,225,218,176,-1,226,176,220,-1,222,220,176,-1,222,176,217,-1,177,221,247,-1,247,233,177,-1,216,217,177,-1,217,216,232,-1,233,246,216,-1,216,177,233,-1,217,221,177,-1,179,181,183,-1,184,178,179,-1,179,183,184,-1,188,22,16,-1,16,202,188,-1,203,181,198,-1,181,203,183,-1,198,181,182,-1,182,300,198,-1,183,205,184,-1,205,183,204,-1,203,204,183,-1,205,206,184,-1,195,186,199,-1,200,199,186,-1,186,167,200,-1,201,200,167,-1,167,187,201,-1,196,197,194,-1,207,194,197,-1,196,194,195,-1,195,199,196,-1,197,190,189,-1,197,189,212,-1,212,189,241,-1,190,234,189,-1,234,192,189,-1,241,189,191,-1,191,189,193,-1,192,193,189,-1,195,194,207,-1,207,208,195,-1,208,203,198,-1,198,195,208,-1,209,196,199,-1,199,200,209,-1,210,209,200,-1,200,201,210,-1,14,211,202,-1,213,204,203,-1,203,208,213,-1,239,205,204,-1,204,213,239,-1,244,206,205,-1,205,239,244,-1,4,15,245,-1,245,15,206,-1,206,244,245,-1,190,197,196,-1,196,235,190,-1,207,197,212,-1,212,214,207,-1,214,213,208,-1,208,207,214,-1,209,236,235,-1,235,196,209,-1,210,230,236,-1,236,209,210,-1,212,241,240,-1,240,214,212,-1,213,214,240,-1,240,239,213,-1,238,215,243,-1,243,237,238,-1,246,229,215,-1,215,216,246,-1,219,217,218,-1,218,225,224,-1,224,219,218,-1,247,221,219,-1,219,224,247,-1,221,217,219,-1,14,13,223,-1,220,12,9,-1,9,226,220,-1,223,13,12,-1,12,220,223,-1,10,11,224,-1,224,225,10,-1,247,224,11,-1,11,0,247,-1,225,227,8,-1,8,10,225,-1,226,9,8,-1,8,227,226,-1,1,7,229,-1,228,6,3,-1,3,242,228,-1,228,229,7,-1,7,6,228,-1,243,228,242,-1,230,231,238,-1,238,236,230,-1,243,215,228,-1,229,228,215,-1,2,246,233,-1,233,5,2,-1,247,0,5,-1,5,233,247,-1,237,243,192,-1,192,234,237,-1,235,236,238,-1,238,237,235,-1,244,239,240,-1,240,245,244,-1,245,242,3,-1,3,4,245,-1,240,241,191,-1,191,245,240,-1,242,245,191,-1,191,193,242,-1,242,193,192,-1,192,243,242,-1,2,1,246,-1,246,1,229,-1,216,215,232,-1,232,238,231,-1,215,238,232,-1,187,170,168,-1,167,170,187,-1,235,234,190,-1,237,234,235,-1,15,184,206,-1,17,184,15,-1,217,176,218,-1,171,21,250,-1,19,21,171,-1,202,252,188,-1,231,230,253,-1,253,251,231,-1,254,253,230,-1,230,210,254,-1,252,254,210,-1,210,201,252,-1,231,251,217,-1,187,252,201,-1,188,252,187,-1,175,222,251,-1,251,253,175,-1,211,175,253,-1,253,254,211,-1,202,211,254,-1,254,252,202,-1,217,251,222,-1,217,232,231,-1,170,174,156,-1,249,174,300,-1,174,163,164,-1,170,163,174,-1,159,186,160,-1,161,186,159,-1,198,186,195,-1,300,186,198,-1,185,255,271,-1,271,255,256,-1,256,264,271,-1,265,264,256,-1,256,257,265,-1,266,265,257,-1,257,258,266,-1,125,266,258,-1,258,130,125,-1,129,18,301,-1,286,259,285,-1,261,287,288,-1,290,302,289,-1,305,179,260,-1,270,260,179,-1,179,182,270,-1,182,271,270,-1,303,291,292,-1,260,270,269,-1,128,267,126,-1,267,263,268,-1,269,268,263,-1,263,267,128,-1,260,269,263,-1,305,262,301,-1,301,173,305,-1,262,127,129,-1,129,301,262,-1,260,263,262,-1,262,305,260,-1,128,127,262,-1,262,263,128,-1,125,126,267,-1,267,266,125,-1,266,267,268,-1,268,265,266,-1,265,268,269,-1,269,264,265,-1,264,269,270,-1,270,271,264,-1,172,249,182,-1,182,180,172,-1,248,273,272,-1,272,155,248,-1,250,274,273,-1,273,248,250,-1,21,151,274,-1,274,250,21,-1,273,275,156,-1,156,272,273,-1,274,276,275,-1,275,273,274,-1,151,154,276,-1,276,274,151,-1,156,275,157,-1,276,157,275,-1,154,20,157,-1,157,276,154,-1,272,249,172,-1,172,155,272,-1,272,156,249,-1,249,156,174,-1,179,180,182,-1]
IndexedFaceSet208.creaseAngle = 1.57
IndexedFaceSet208.texCoordIndex = [255,256,257,-1,257,258,255,-1,259,260,261,-1,0,1,2,-1,2,3,0,-1,4,5,2,-1,2,1,4,-1,262,263,256,-1,256,255,262,-1,6,7,8,-1,8,9,6,-1,7,10,11,-1,12,11,13,-1,13,14,12,-1,12,14,15,-1,15,8,12,-1,8,15,16,-1,16,9,8,-1,10,13,11,-1,6,9,16,-1,17,14,13,-1,18,16,15,-1,10,17,13,-1,6,16,18,-1,19,4,1,-1,0,17,1,-1,261,264,265,-1,265,266,261,-1,260,264,261,-1,267,268,263,-1,263,269,267,-1,256,263,268,-1,268,270,256,-1,256,270,271,-1,271,257,256,-1,269,272,267,-1,186,187,188,-1,188,189,186,-1,189,188,190,-1,273,274,275,-1,20,21,22,-1,22,23,20,-1,24,25,22,-1,22,21,24,-1,26,27,24,-1,28,29,30,-1,31,28,30,-1,30,32,31,-1,29,20,30,-1,23,30,20,-1,23,33,30,-1,34,35,36,-1,36,37,34,-1,38,36,33,-1,33,39,38,-1,38,40,37,-1,37,36,38,-1,33,36,35,-1,191,192,193,-1,191,187,186,-1,186,192,191,-1,26,5,4,-1,4,27,26,-1,194,195,193,-1,193,192,194,-1,196,193,195,-1,195,197,196,-1,192,186,198,-1,198,199,192,-1,194,192,199,-1,198,186,200,-1,41,42,7,-1,7,42,43,-1,43,10,7,-1,10,43,44,-1,44,19,10,-1,45,46,47,-1,48,47,46,-1,41,46,45,-1,45,42,41,-1,47,49,50,-1,47,51,49,-1,51,52,49,-1,50,49,53,-1,53,49,54,-1,52,55,49,-1,55,56,49,-1,54,49,56,-1,48,46,41,-1,41,57,48,-1,58,59,57,-1,57,41,58,-1,42,45,60,-1,60,43,42,-1,43,60,61,-1,61,44,43,-1,24,27,25,-1,59,62,63,-1,63,57,59,-1,62,64,65,-1,65,63,62,-1,64,66,67,-1,67,65,64,-1,68,69,70,-1,66,70,69,-1,69,67,66,-1,50,45,47,-1,45,50,71,-1,51,47,48,-1,48,72,51,-1,57,63,72,-1,72,48,57,-1,71,73,60,-1,60,45,71,-1,73,74,61,-1,61,60,73,-1,75,52,51,-1,51,72,75,-1,75,72,63,-1,63,65,75,-1,76,77,78,-1,78,79,76,-1,77,80,40,-1,40,38,77,-1,81,32,33,-1,82,31,32,-1,32,81,82,-1,81,35,34,-1,34,82,81,-1,35,81,33,-1,24,21,83,-1,84,85,20,-1,20,29,84,-1,85,83,21,-1,21,20,85,-1,82,86,87,-1,87,31,82,-1,86,82,34,-1,34,88,86,-1,89,28,31,-1,31,87,89,-1,89,84,29,-1,29,28,89,-1,90,80,91,-1,92,93,94,-1,94,95,92,-1,91,80,94,-1,94,93,91,-1,76,95,94,-1,78,96,74,-1,74,73,78,-1,76,94,77,-1,80,77,94,-1,37,40,97,-1,97,98,37,-1,98,88,34,-1,34,37,98,-1,54,76,79,-1,79,53,54,-1,78,73,71,-1,71,79,78,-1,75,65,67,-1,67,69,75,-1,92,95,69,-1,69,68,92,-1,55,52,75,-1,75,69,55,-1,55,69,95,-1,95,56,55,-1,54,56,95,-1,95,76,54,-1,97,40,90,-1,40,80,90,-1,38,39,77,-1,39,96,78,-1,77,39,78,-1,19,1,17,-1,10,19,17,-1,71,50,53,-1,79,71,53,-1,201,200,186,-1,189,201,186,-1,33,32,30,-1,263,262,276,-1,269,263,276,-1,27,4,99,-1,100,74,96,-1,96,101,100,-1,74,100,102,-1,102,61,74,-1,61,102,99,-1,99,44,61,-1,96,33,101,-1,19,44,99,-1,4,19,99,-1,101,23,22,-1,22,100,101,-1,100,22,25,-1,25,102,100,-1,102,25,27,-1,27,99,102,-1,33,23,101,-1,33,96,39,-1,260,259,277,-1,273,275,277,-1,18,15,14,-1,17,18,14,-1,12,8,7,-1,11,12,7,-1,58,41,7,-1,6,58,7,-1,197,202,203,-1,204,203,202,-1,202,205,204,-1,204,205,206,-1,206,207,204,-1,207,206,208,-1,208,209,207,-1,209,208,210,-1,210,211,209,-1,212,213,190,-1,188,190,213,-1,214,187,188,-1,191,187,214,-1,214,215,191,-1,191,215,216,-1,216,196,191,-1,196,216,202,-1,202,197,196,-1,215,217,216,-1,218,219,220,-1,220,221,222,-1,217,222,221,-1,222,218,220,-1,215,222,217,-1,213,223,214,-1,214,188,213,-1,212,224,223,-1,223,213,212,-1,223,222,215,-1,215,214,223,-1,223,224,218,-1,218,222,223,-1,220,219,210,-1,210,208,220,-1,221,220,208,-1,208,206,221,-1,217,221,206,-1,206,205,217,-1,216,217,205,-1,205,202,216,-1,274,273,257,-1,257,271,274,-1,278,279,255,-1,255,258,278,-1,279,280,262,-1,262,255,279,-1,280,281,276,-1,276,262,280,-1,259,282,279,-1,279,278,259,-1,282,283,280,-1,280,279,282,-1,283,284,281,-1,281,280,283,-1,259,261,282,-1,283,282,261,-1,261,266,284,-1,284,283,261,-1,257,273,278,-1,278,258,257,-1,278,273,259,-1,273,277,259,-1,270,274,271,-1,286,287,285,-1,285,288,286,-1,289,290,291,-1,2,104,103,-1,103,3,2,-1,2,5,105,-1,105,104,2,-1,287,293,292,-1,292,285,287,-1,107,108,106,-1,106,109,107,-1,108,110,111,-1,113,110,112,-1,112,114,113,-1,115,114,112,-1,112,107,115,-1,116,115,107,-1,107,109,116,-1,111,110,113,-1,106,116,109,-1,117,113,114,-1,118,115,116,-1,111,113,117,-1,106,118,116,-1,119,104,105,-1,103,104,117,-1,265,294,290,-1,290,266,265,-1,291,290,294,-1,293,296,295,-1,295,269,293,-1,296,293,287,-1,287,297,296,-1,298,297,287,-1,287,286,298,-1,269,295,272,-1,226,227,225,-1,225,189,226,-1,189,190,226,-1,299,300,301,-1,121,122,120,-1,120,123,121,-1,121,124,24,-1,24,122,121,-1,26,24,125,-1,126,127,128,-1,127,126,129,-1,129,130,127,-1,128,127,120,-1,123,120,127,-1,123,127,131,-1,133,134,132,-1,132,135,133,-1,136,131,133,-1,131,136,137,-1,135,138,136,-1,136,133,135,-1,131,134,133,-1,228,229,230,-1,225,227,228,-1,228,230,225,-1,105,5,26,-1,26,125,105,-1,231,229,232,-1,229,231,230,-1,232,229,233,-1,233,234,232,-1,230,235,225,-1,235,230,236,-1,231,236,230,-1,235,237,225,-1,139,108,140,-1,141,140,108,-1,108,111,141,-1,142,141,111,-1,111,119,142,-1,143,144,145,-1,146,145,144,-1,143,145,139,-1,139,140,143,-1,144,147,148,-1,144,148,149,-1,149,148,150,-1,147,151,148,-1,151,152,148,-1,150,148,153,-1,153,148,154,-1,152,154,148,-1,139,145,146,-1,146,155,139,-1,155,157,156,-1,156,139,155,-1,158,143,140,-1,140,141,158,-1,159,158,141,-1,141,142,159,-1,24,124,125,-1,160,161,157,-1,157,155,160,-1,162,163,161,-1,161,160,162,-1,164,165,163,-1,163,162,164,-1,68,70,166,-1,166,70,165,-1,165,164,166,-1,147,144,143,-1,143,167,147,-1,146,144,149,-1,149,168,146,-1,168,160,155,-1,155,146,168,-1,158,169,167,-1,167,143,158,-1,159,170,169,-1,169,158,159,-1,149,150,171,-1,171,168,149,-1,160,168,171,-1,171,162,160,-1,173,174,172,-1,172,175,173,-1,138,176,174,-1,174,136,138,-1,177,131,130,-1,130,129,178,-1,178,177,130,-1,132,134,177,-1,177,178,132,-1,134,131,177,-1,24,83,122,-1,120,85,84,-1,84,128,120,-1,122,83,85,-1,85,120,122,-1,87,86,178,-1,178,129,87,-1,132,178,86,-1,86,88,132,-1,129,126,89,-1,89,87,129,-1,128,84,89,-1,89,126,128,-1,90,91,176,-1,179,93,92,-1,92,180,179,-1,179,176,91,-1,91,93,179,-1,172,179,180,-1,170,181,173,-1,173,169,170,-1,172,174,179,-1,176,179,174,-1,97,138,135,-1,135,98,97,-1,132,88,98,-1,98,135,132,-1,175,172,152,-1,152,151,175,-1,167,169,173,-1,173,175,167,-1,164,162,171,-1,171,166,164,-1,166,180,92,-1,92,68,166,-1,171,150,153,-1,153,166,171,-1,180,166,153,-1,153,154,180,-1,180,154,152,-1,152,172,180,-1,97,90,138,-1,138,90,176,-1,136,174,137,-1,137,173,181,-1,174,173,137,-1,119,117,104,-1,111,117,119,-1,167,151,147,-1,175,151,167,-1,201,225,237,-1,189,225,201,-1,131,127,130,-1,293,276,292,-1,269,276,293,-1,125,182,105,-1,181,170,183,-1,183,184,181,-1,185,183,170,-1,170,159,185,-1,182,185,159,-1,159,142,182,-1,181,184,131,-1,119,182,142,-1,105,182,119,-1,121,123,184,-1,184,183,121,-1,124,121,183,-1,183,185,124,-1,125,124,185,-1,185,182,125,-1,131,184,123,-1,131,137,181,-1,291,302,289,-1,299,302,300,-1,118,114,115,-1,117,114,118,-1,112,108,107,-1,110,108,112,-1,156,108,139,-1,106,108,156,-1,234,238,239,-1,239,238,240,-1,240,241,239,-1,242,241,240,-1,240,243,242,-1,244,242,243,-1,243,245,244,-1,210,244,245,-1,245,211,210,-1,212,190,246,-1,226,246,190,-1,247,226,227,-1,228,247,227,-1,247,228,248,-1,249,248,228,-1,228,233,249,-1,233,239,249,-1,239,233,234,-1,248,249,250,-1,218,251,219,-1,251,252,253,-1,250,253,252,-1,252,251,218,-1,248,250,252,-1,247,254,246,-1,246,226,247,-1,254,224,212,-1,212,246,254,-1,248,252,254,-1,254,247,248,-1,218,224,254,-1,254,252,218,-1,210,219,251,-1,251,244,210,-1,244,251,253,-1,253,242,244,-1,242,253,250,-1,250,241,242,-1,241,250,249,-1,249,239,241,-1,286,299,301,-1,301,298,286,-1,285,304,303,-1,303,288,285,-1,292,305,304,-1,304,285,292,-1,276,281,305,-1,305,292,276,-1,304,306,289,-1,289,303,304,-1,305,307,306,-1,306,304,305,-1,281,284,307,-1,307,305,281,-1,289,306,290,-1,307,290,306,-1,284,266,290,-1,290,307,284,-1,303,299,286,-1,286,288,303,-1,303,289,299,-1,299,289,302,-1,297,298,301,-1]
Coordinate209 = x3d.Coordinate()

IndexedFaceSet208.coord = Coordinate209
TextureCoordinate210 = x3d.TextureCoordinate()

IndexedFaceSet208.texCoord = TextureCoordinate210

Shape204.geometry = IndexedFaceSet208

Transform203.children.append(Shape204)

HAnimSegment202.children.append(Transform203)

HAnimJoint201.children.append(HAnimSegment202)

HAnimJoint191.children.append(HAnimJoint201)

HAnimJoint121.children.append(HAnimJoint191)

HAnimJoint31.children.append(HAnimJoint121)

HAnimHumanoid23.skeleton.append(HAnimJoint31)
HAnimJoint211 = x3d.HAnimJoint()
HAnimJoint211.USE = "hanim_humanoid_root"

HAnimHumanoid23.joints.append(HAnimJoint211)
HAnimJoint212 = x3d.HAnimJoint()
HAnimJoint212.USE = "hanim_sacroiliac"

HAnimHumanoid23.joints.append(HAnimJoint212)
HAnimJoint213 = x3d.HAnimJoint()
HAnimJoint213.USE = "hanim_skullbase"

HAnimHumanoid23.joints.append(HAnimJoint213)
HAnimJoint214 = x3d.HAnimJoint()
HAnimJoint214.USE = "hanim_vl5"

HAnimHumanoid23.joints.append(HAnimJoint214)
HAnimJoint215 = x3d.HAnimJoint()
HAnimJoint215.USE = "hanim_l_elbow"

HAnimHumanoid23.joints.append(HAnimJoint215)
HAnimJoint216 = x3d.HAnimJoint()
HAnimJoint216.USE = "hanim_r_elbow"

HAnimHumanoid23.joints.append(HAnimJoint216)
HAnimJoint217 = x3d.HAnimJoint()
HAnimJoint217.USE = "hanim_l_hip"

HAnimHumanoid23.joints.append(HAnimJoint217)
HAnimJoint218 = x3d.HAnimJoint()
HAnimJoint218.USE = "hanim_r_hip"

HAnimHumanoid23.joints.append(HAnimJoint218)
HAnimJoint219 = x3d.HAnimJoint()
HAnimJoint219.USE = "hanim_l_knee"

HAnimHumanoid23.joints.append(HAnimJoint219)
HAnimJoint220 = x3d.HAnimJoint()
HAnimJoint220.USE = "hanim_r_knee"

HAnimHumanoid23.joints.append(HAnimJoint220)
HAnimJoint221 = x3d.HAnimJoint()
HAnimJoint221.USE = "hanim_l_metatarsophalangeal_2"

HAnimHumanoid23.joints.append(HAnimJoint221)
HAnimJoint222 = x3d.HAnimJoint()
HAnimJoint222.USE = "hanim_r_metatarsophalangeal_2"

HAnimHumanoid23.joints.append(HAnimJoint222)
HAnimJoint223 = x3d.HAnimJoint()
HAnimJoint223.USE = "hanim_l_radiocarpal"

HAnimHumanoid23.joints.append(HAnimJoint223)
HAnimJoint224 = x3d.HAnimJoint()
HAnimJoint224.USE = "hanim_r_radiocarpal"

HAnimHumanoid23.joints.append(HAnimJoint224)
HAnimJoint225 = x3d.HAnimJoint()
HAnimJoint225.USE = "hanim_l_shoulder"

HAnimHumanoid23.joints.append(HAnimJoint225)
HAnimJoint226 = x3d.HAnimJoint()
HAnimJoint226.USE = "hanim_r_shoulder"

HAnimHumanoid23.joints.append(HAnimJoint226)
HAnimJoint227 = x3d.HAnimJoint()
HAnimJoint227.USE = "hanim_l_talocrural"

HAnimHumanoid23.joints.append(HAnimJoint227)
HAnimJoint228 = x3d.HAnimJoint()
HAnimJoint228.USE = "hanim_r_talocrural"

HAnimHumanoid23.joints.append(HAnimJoint228)
HAnimSegment229 = x3d.HAnimSegment()
HAnimSegment229.USE = "hanim_l5"

HAnimHumanoid23.segments.append(HAnimSegment229)
HAnimSegment230 = x3d.HAnimSegment()
HAnimSegment230.USE = "hanim_pelvis"

HAnimHumanoid23.segments.append(HAnimSegment230)
HAnimSegment231 = x3d.HAnimSegment()
HAnimSegment231.USE = "hanim_sacrum"

HAnimHumanoid23.segments.append(HAnimSegment231)
HAnimSegment232 = x3d.HAnimSegment()
HAnimSegment232.USE = "hanim_skull"

HAnimHumanoid23.segments.append(HAnimSegment232)
HAnimSegment233 = x3d.HAnimSegment()
HAnimSegment233.USE = "hanim_l_calf"

HAnimHumanoid23.segments.append(HAnimSegment233)
HAnimSegment234 = x3d.HAnimSegment()
HAnimSegment234.USE = "hanim_r_calf"

HAnimHumanoid23.segments.append(HAnimSegment234)
HAnimSegment235 = x3d.HAnimSegment()
HAnimSegment235.USE = "hanim_l_carpal"

HAnimHumanoid23.segments.append(HAnimSegment235)
HAnimSegment236 = x3d.HAnimSegment()
HAnimSegment236.USE = "hanim_r_carpal"

HAnimHumanoid23.segments.append(HAnimSegment236)
HAnimSegment237 = x3d.HAnimSegment()
HAnimSegment237.USE = "hanim_l_forearm"

HAnimHumanoid23.segments.append(HAnimSegment237)
HAnimSegment238 = x3d.HAnimSegment()
HAnimSegment238.USE = "hanim_r_forearm"

HAnimHumanoid23.segments.append(HAnimSegment238)
HAnimSegment239 = x3d.HAnimSegment()
HAnimSegment239.USE = "hanim_l_talus"

HAnimHumanoid23.segments.append(HAnimSegment239)
HAnimSegment240 = x3d.HAnimSegment()
HAnimSegment240.USE = "hanim_r_talus"

HAnimHumanoid23.segments.append(HAnimSegment240)
HAnimSegment241 = x3d.HAnimSegment()
HAnimSegment241.USE = "hanim_l_tarsal_proximal_phalanx_2"

HAnimHumanoid23.segments.append(HAnimSegment241)
HAnimSegment242 = x3d.HAnimSegment()
HAnimSegment242.USE = "hanim_r_tarsal_proximal_phalanx_2"

HAnimHumanoid23.segments.append(HAnimSegment242)
HAnimSegment243 = x3d.HAnimSegment()
HAnimSegment243.USE = "hanim_l_thigh"

HAnimHumanoid23.segments.append(HAnimSegment243)
HAnimSegment244 = x3d.HAnimSegment()
HAnimSegment244.USE = "hanim_r_thigh"

HAnimHumanoid23.segments.append(HAnimSegment244)
HAnimSegment245 = x3d.HAnimSegment()
HAnimSegment245.USE = "hanim_l_upperarm"

HAnimHumanoid23.segments.append(HAnimSegment245)
HAnimSegment246 = x3d.HAnimSegment()
HAnimSegment246.USE = "hanim_r_upperarm"

HAnimHumanoid23.segments.append(HAnimSegment246)

Scene19.children.append(HAnimHumanoid23)

X3D0.Scene = Scene19
f = open("././KoreanCharacter03Hyun_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
