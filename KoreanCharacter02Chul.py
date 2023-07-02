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
meta3.content = "KoreanCharacter02Chul.x3d"

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
meta13.content = "https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Characters/KoreanCharacter02Chul.x3d"

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
WorldInfo20.title = "KoreanCharacter02Chul.x3d"

Scene19.children.append(WorldInfo20)
NavigationInfo21 = x3d.NavigationInfo()
NavigationInfo21.speed = 1.5

Scene19.children.append(NavigationInfo21)
Viewpoint22 = x3d.Viewpoint()
Viewpoint22.centerOfRotation = [0,1,0]
Viewpoint22.description = "Chul"
Viewpoint22.position = [0,1,3]

Scene19.children.append(Viewpoint22)
HAnimHumanoid23 = x3d.HAnimHumanoid()
HAnimHumanoid23.name = "Chul"
HAnimHumanoid23.DEF = "hanim_Chul"
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
HAnimJoint31.center = [0,44.07,-1.034]
HAnimJoint31.ulimit = [0,0,0]
HAnimJoint31.llimit = [0,0,0]
HAnimSegment32 = x3d.HAnimSegment()
HAnimSegment32.name = "sacrum"
HAnimSegment32.DEF = "hanim_sacrum"
Transform33 = x3d.Transform()
Transform33.translation = [0,44.07,-1.034]
Shape34 = x3d.Shape()
Appearance35 = x3d.Appearance()
Material36 = x3d.Material()
Material36.diffuseColor = [0.588,0.588,0.588]

Appearance35.material = Material36
ImageTexture37 = x3d.ImageTexture()
ImageTexture37.DEF = "ChulTextureAtlas"
ImageTexture37.url = ["images/Chul.png","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Characters/images/Chul.png"]

Appearance35.texture = ImageTexture37

Shape34.appearance = Appearance35
IndexedFaceSet38 = x3d.IndexedFaceSet()
IndexedFaceSet38.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,5,-1,0,5,6,-1,0,6,7,-1,0,7,8,-1,0,8,9,-1,0,9,10,-1,0,10,11,-1,0,11,12,-1,0,12,1,-1,14,2,1,-1,1,13,14,-1,15,3,2,-1,2,14,15,-1,16,4,3,-1,3,15,16,-1,17,5,4,-1,4,16,17,-1,18,6,5,-1,5,17,18,-1,19,7,6,-1,6,18,19,-1,20,8,7,-1,7,19,20,-1,21,9,8,-1,8,20,21,-1,22,10,9,-1,9,21,22,-1,23,11,10,-1,10,22,23,-1,24,12,11,-1,11,23,24,-1,13,1,12,-1,12,24,13,-1,26,14,13,-1,13,25,26,-1,27,15,14,-1,14,26,27,-1,28,16,15,-1,15,27,28,-1,29,17,16,-1,16,28,29,-1,30,18,17,-1,17,29,30,-1,31,19,18,-1,18,30,31,-1,32,20,19,-1,19,31,32,-1,33,21,20,-1,20,32,33,-1,34,22,21,-1,21,33,34,-1,35,23,22,-1,22,34,35,-1,36,24,23,-1,23,35,36,-1,25,13,24,-1,24,36,25,-1,38,26,25,-1,25,37,38,-1,39,27,26,-1,26,38,39,-1,40,28,27,-1,27,39,40,-1,41,29,28,-1,28,40,41,-1,42,30,29,-1,29,41,42,-1,43,31,30,-1,30,42,43,-1,44,32,31,-1,31,43,44,-1,45,33,32,-1,32,44,45,-1,46,34,33,-1,33,45,46,-1,47,35,34,-1,34,46,47,-1,48,36,35,-1,35,47,48,-1,37,25,36,-1,36,48,37,-1,50,38,37,-1,37,49,50,-1,51,39,38,-1,38,50,51,-1,52,40,39,-1,39,51,52,-1,53,41,40,-1,40,52,53,-1,54,42,41,-1,41,53,54,-1,55,43,42,-1,42,54,55,-1,56,44,43,-1,43,55,56,-1,57,45,44,-1,44,56,57,-1,58,46,45,-1,45,57,58,-1,59,47,46,-1,46,58,59,-1,60,48,47,-1,47,59,60,-1,49,37,48,-1,48,60,49,-1,61,50,49,-1,61,51,50,-1,61,52,51,-1,61,53,52,-1,61,54,53,-1,61,55,54,-1,61,56,55,-1,61,57,56,-1,61,58,57,-1,61,59,58,-1,61,60,59,-1,61,49,60,-1]
IndexedFaceSet38.creaseAngle = 1.57
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
HAnimJoint41.name = "l_hip"
HAnimJoint41.DEF = "hanim_l_hip"
HAnimJoint41.center = [4.001,41.139999,-1.119]
HAnimJoint41.ulimit = [0,0,0]
HAnimJoint41.llimit = [0,0,0]
HAnimSegment42 = x3d.HAnimSegment()
HAnimSegment42.name = "l_thigh"
HAnimSegment42.DEF = "hanim_l_thigh"
Transform43 = x3d.Transform()
Transform43.translation = [4.001,41.139999,-1.119]
Shape44 = x3d.Shape()
Appearance45 = x3d.Appearance()
Material46 = x3d.Material()
Material46.diffuseColor = [0.588,0.588,0.588]

Appearance45.material = Material46
ImageTexture47 = x3d.ImageTexture()
ImageTexture47.USE = "ChulTextureAtlas"

Appearance45.texture = ImageTexture47

Shape44.appearance = Appearance45
IndexedFaceSet48 = x3d.IndexedFaceSet()
IndexedFaceSet48.coordIndex = [40,39,38,-1,38,37,36,-1,38,36,35,-1,40,38,35,-1,41,40,35,-1,0,1,8,-1,8,7,0,-1,1,2,9,-1,9,8,1,-1,2,3,10,-1,10,9,2,-1,3,4,11,-1,11,10,3,-1,4,5,12,-1,12,11,4,-1,5,6,13,-1,13,12,5,-1,6,0,7,-1,7,13,6,-1,7,8,15,-1,15,14,7,-1,8,9,16,-1,16,15,8,-1,9,10,17,-1,17,16,9,-1,10,11,18,-1,18,17,10,-1,11,12,19,-1,19,18,11,-1,12,13,20,-1,20,19,12,-1,13,7,14,-1,14,20,13,-1,14,15,107,-1,107,106,14,-1,15,16,108,-1,108,107,15,-1,16,17,109,-1,109,108,16,-1,17,18,110,-1,110,109,17,-1,18,19,111,-1,111,110,18,-1,19,20,112,-1,112,111,19,-1,20,14,106,-1,106,112,20,-1,29,28,106,-1,106,107,29,-1,30,29,107,-1,107,108,30,-1,31,30,108,-1,108,109,31,-1,32,31,109,-1,109,110,32,-1,33,32,110,-1,110,111,33,-1,34,33,111,-1,111,112,34,-1,28,34,112,-1,112,106,28,-1,35,36,1,-1,1,0,35,-1,36,37,2,-1,2,1,36,-1,37,38,3,-1,3,2,37,-1,38,39,4,-1,4,3,38,-1,39,40,5,-1,5,4,39,-1,40,41,6,-1,6,5,40,-1,41,35,0,-1,0,6,41,-1,113,43,21,-1,50,51,42,-1,115,113,22,-1,52,53,44,-1,116,115,23,-1,54,55,45,-1,117,116,24,-1,56,57,46,-1,118,117,25,-1,58,59,47,-1,119,118,26,-1,60,61,48,-1,43,119,27,-1,62,63,114,-1,122,64,65,-1,66,67,130,-1,121,68,69,-1,70,71,129,-1,123,72,73,-1,74,75,131,-1,124,76,77,-1,78,79,132,-1,125,80,81,-1,82,83,133,-1,126,84,85,-1,86,87,134,-1,127,88,89,-1,90,91,135,-1,43,113,140,-1,113,115,140,-1,115,116,140,-1,116,117,140,-1,117,118,140,-1,118,119,140,-1,119,43,140,-1,92,93,49,-1,94,95,120,-1,96,97,128,-1,98,99,136,-1,100,101,137,-1,102,103,138,-1,104,105,139,-1]
IndexedFaceSet48.creaseAngle = 1.57
IndexedFaceSet48.texCoordIndex = [5,4,3,-1,3,2,0,-1,3,0,1,-1,5,3,1,-1,6,5,1,-1,7,10,8,-1,8,9,7,-1,10,12,11,-1,11,8,10,-1,12,14,13,-1,13,11,12,-1,14,16,15,-1,15,13,14,-1,16,18,17,-1,17,15,16,-1,18,20,19,-1,19,17,18,-1,20,7,9,-1,9,19,20,-1,9,8,21,-1,21,22,9,-1,8,11,23,-1,23,21,8,-1,11,13,24,-1,24,23,11,-1,13,15,25,-1,25,24,13,-1,15,17,26,-1,26,25,15,-1,17,19,27,-1,27,26,17,-1,19,9,22,-1,22,27,19,-1,22,21,28,-1,28,29,22,-1,21,23,30,-1,30,28,21,-1,23,24,31,-1,31,30,23,-1,24,25,32,-1,32,31,24,-1,25,26,33,-1,33,32,25,-1,26,27,34,-1,34,33,26,-1,27,22,29,-1,29,34,27,-1,35,36,29,-1,29,28,35,-1,37,35,28,-1,28,30,37,-1,38,37,30,-1,30,31,38,-1,39,38,31,-1,31,32,39,-1,40,39,32,-1,32,33,40,-1,41,40,33,-1,33,34,41,-1,36,41,34,-1,34,29,36,-1,1,0,10,-1,10,7,1,-1,0,2,12,-1,12,10,0,-1,2,3,14,-1,14,12,2,-1,3,4,16,-1,16,14,3,-1,4,5,18,-1,18,16,4,-1,5,6,20,-1,20,18,5,-1,6,1,7,-1,7,20,6,-1,42,43,29,-1,29,28,42,-1,44,42,28,-1,28,30,44,-1,45,44,30,-1,30,31,45,-1,46,45,31,-1,31,32,46,-1,47,46,32,-1,32,33,47,-1,48,47,33,-1,33,34,48,-1,43,48,34,-1,34,29,43,-1,43,42,28,-1,28,29,43,-1,42,44,30,-1,30,28,42,-1,44,45,31,-1,31,30,44,-1,45,46,32,-1,32,31,45,-1,46,47,33,-1,33,32,46,-1,47,48,34,-1,34,33,47,-1,48,43,29,-1,29,34,48,-1,43,42,49,-1,42,44,49,-1,44,45,49,-1,45,46,49,-1,46,47,49,-1,47,48,49,-1,48,43,49,-1,42,43,49,-1,44,42,49,-1,45,44,49,-1,46,45,49,-1,47,46,49,-1,48,47,49,-1,43,48,49,-1]
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
HAnimJoint51.center = [4.315,25.190001,-1.119]
HAnimJoint51.ulimit = [0,0,0]
HAnimJoint51.llimit = [0,0,0]
HAnimSegment52 = x3d.HAnimSegment()
HAnimSegment52.name = "l_calf"
HAnimSegment52.DEF = "hanim_l_calf"
Transform53 = x3d.Transform()
Transform53.translation = [4.315,25.190001,-1.119]
Shape54 = x3d.Shape()
Appearance55 = x3d.Appearance()
Material56 = x3d.Material()
Material56.diffuseColor = [0.588,0.588,0.588]

Appearance55.material = Material56
ImageTexture57 = x3d.ImageTexture()
ImageTexture57.USE = "ChulTextureAtlas"

Appearance55.texture = ImageTexture57

Shape54.appearance = Appearance55
IndexedFaceSet58 = x3d.IndexedFaceSet()
IndexedFaceSet58.coordIndex = [40,39,38,-1,38,37,36,-1,38,36,35,-1,40,38,35,-1,41,40,35,-1,0,1,8,-1,8,7,0,-1,1,2,9,-1,9,8,1,-1,2,3,10,-1,10,9,2,-1,3,4,11,-1,11,10,3,-1,4,5,12,-1,12,11,4,-1,5,6,13,-1,13,12,5,-1,6,0,7,-1,7,13,6,-1,7,8,15,-1,15,14,7,-1,8,9,16,-1,16,15,8,-1,9,10,17,-1,17,16,9,-1,10,11,18,-1,18,17,10,-1,11,12,19,-1,19,18,11,-1,12,13,20,-1,20,19,12,-1,13,7,14,-1,14,20,13,-1,14,15,22,-1,22,21,14,-1,15,16,23,-1,23,22,15,-1,16,17,24,-1,24,23,16,-1,17,18,25,-1,25,24,17,-1,18,19,26,-1,26,25,18,-1,19,20,27,-1,27,26,19,-1,20,14,21,-1,21,27,20,-1,29,28,21,-1,21,22,29,-1,30,29,22,-1,22,23,30,-1,31,30,23,-1,23,24,31,-1,32,31,24,-1,24,25,32,-1,33,32,25,-1,25,26,33,-1,34,33,26,-1,26,27,34,-1,28,34,27,-1,27,21,28,-1,35,36,1,-1,1,0,35,-1,36,37,2,-1,2,1,36,-1,37,38,3,-1,3,2,37,-1,38,39,4,-1,4,3,38,-1,39,40,5,-1,5,4,39,-1,40,41,6,-1,6,5,40,-1,41,35,0,-1,0,6,41,-1]
IndexedFaceSet58.creaseAngle = 1.57
IndexedFaceSet58.texCoordIndex = [5,4,3,-1,3,2,0,-1,3,0,1,-1,5,3,1,-1,6,5,1,-1,7,10,8,-1,8,9,7,-1,10,12,11,-1,11,8,10,-1,12,14,13,-1,13,11,12,-1,14,16,15,-1,15,13,14,-1,16,18,17,-1,17,15,16,-1,18,20,19,-1,19,17,18,-1,20,7,9,-1,9,19,20,-1,9,8,21,-1,21,22,9,-1,8,11,23,-1,23,21,8,-1,11,13,24,-1,24,23,11,-1,13,15,25,-1,25,24,13,-1,15,17,26,-1,26,25,15,-1,17,19,27,-1,27,26,17,-1,19,9,22,-1,22,27,19,-1,22,21,28,-1,28,29,22,-1,21,23,30,-1,30,28,21,-1,23,24,31,-1,31,30,23,-1,24,25,32,-1,32,31,24,-1,25,26,33,-1,33,32,25,-1,26,27,34,-1,34,33,26,-1,27,22,29,-1,29,34,27,-1,35,36,29,-1,29,28,35,-1,37,35,28,-1,28,30,37,-1,38,37,30,-1,30,31,38,-1,39,38,31,-1,31,32,39,-1,40,39,32,-1,32,33,40,-1,41,40,33,-1,33,34,41,-1,36,41,34,-1,34,29,36,-1,1,0,10,-1,10,7,1,-1,0,2,12,-1,12,10,0,-1,2,3,14,-1,14,12,2,-1,3,4,16,-1,16,14,3,-1,4,5,18,-1,18,16,4,-1,5,6,20,-1,20,18,5,-1,6,1,7,-1,7,20,6,-1]
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
HAnimJoint61.center = [4.574,6.838,-1.463]
HAnimJoint61.ulimit = [0,0,0]
HAnimJoint61.llimit = [0,0,0]
HAnimSegment62 = x3d.HAnimSegment()
HAnimSegment62.name = "l_talus"
HAnimSegment62.DEF = "hanim_l_talus"
Transform63 = x3d.Transform()
Transform63.translation = [4.574,6.838,-1.463]
Shape64 = x3d.Shape()
Appearance65 = x3d.Appearance()
Material66 = x3d.Material()
Material66.diffuseColor = [0.588,0.588,0.588]

Appearance65.material = Material66
ImageTexture67 = x3d.ImageTexture()
ImageTexture67.USE = "ChulTextureAtlas"

Appearance65.texture = ImageTexture67

Shape64.appearance = Appearance65
IndexedFaceSet68 = x3d.IndexedFaceSet()
IndexedFaceSet68.coordIndex = [0,4,1,-1,1,2,0,-1,3,5,0,-1,0,2,3,-1,6,9,7,-1,7,8,6,-1,8,7,10,-1,10,11,8,-1,12,20,9,-1,9,6,12,-1,21,20,12,-1,12,13,21,-1,11,10,14,-1,14,15,11,-1,15,14,16,-1,16,17,15,-1,9,1,4,-1,4,7,9,-1,7,4,0,-1,0,10,7,-1,10,0,5,-1,5,14,10,-1,14,5,3,-1,3,16,14,-1,6,8,19,-1,8,11,19,-1,12,6,19,-1,13,12,19,-1,11,15,19,-1,15,17,19,-1,17,18,19,-1,18,13,19,-1,13,18,22,-1,22,21,13,-1,18,17,16,-1,16,22,18,-1,24,25,26,-1,26,27,28,-1,24,26,28,-1,24,28,29,-1,24,29,30,-1,24,30,23,-1,2,1,24,-1,24,23,2,-1,1,9,25,-1,25,24,1,-1,9,20,26,-1,26,25,9,-1,20,21,27,-1,27,26,20,-1,21,22,28,-1,28,27,21,-1,22,16,29,-1,29,28,22,-1,16,3,30,-1,30,29,16,-1,3,2,23,-1,23,30,3,-1]
IndexedFaceSet68.creaseAngle = 1.57
IndexedFaceSet68.texCoordIndex = [0,4,1,-1,1,2,0,-1,3,5,0,-1,0,2,3,-1,6,9,7,-1,7,8,6,-1,8,7,10,-1,10,11,8,-1,12,20,9,-1,9,6,12,-1,21,20,12,-1,12,13,21,-1,11,10,14,-1,14,15,11,-1,15,14,16,-1,16,17,15,-1,9,1,4,-1,4,7,9,-1,7,4,0,-1,0,10,7,-1,10,0,5,-1,5,14,10,-1,14,5,3,-1,3,16,14,-1,6,8,19,-1,8,11,19,-1,12,6,19,-1,13,12,19,-1,11,15,19,-1,15,17,19,-1,17,18,19,-1,18,13,19,-1,13,18,22,-1,22,21,13,-1,18,17,16,-1,16,22,18,-1,24,25,26,-1,26,27,28,-1,24,26,28,-1,24,28,29,-1,24,29,30,-1,24,30,23,-1,2,1,24,-1,24,23,2,-1,1,9,25,-1,25,24,1,-1,9,20,26,-1,26,25,9,-1,20,21,27,-1,27,26,20,-1,21,22,28,-1,28,27,21,-1,22,16,29,-1,29,28,22,-1,16,3,30,-1,30,29,16,-1,3,2,23,-1,23,30,3,-1]
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
HAnimJoint71.center = [4.809,5.583,1.492]
HAnimJoint71.ulimit = [0,0,0]
HAnimJoint71.llimit = [0,0,0]
HAnimSegment72 = x3d.HAnimSegment()
HAnimSegment72.name = "l_tarsal_proximal_phalanx_2"
HAnimSegment72.DEF = "hanim_l_tarsal_proximal_phalanx_2"
Transform73 = x3d.Transform()
Transform73.translation = [4.809,5.583,1.492]
Shape74 = x3d.Shape()
Appearance75 = x3d.Appearance()
Material76 = x3d.Material()
Material76.diffuseColor = [0.588,0.588,0.588]

Appearance75.material = Material76
ImageTexture77 = x3d.ImageTexture()
ImageTexture77.USE = "ChulTextureAtlas"

Appearance75.texture = ImageTexture77

Shape74.appearance = Appearance75
IndexedFaceSet78 = x3d.IndexedFaceSet()
IndexedFaceSet78.coordIndex = [0,1,19,-1,19,18,0,-1,1,2,20,-1,20,19,1,-1,22,5,25,-1,4,24,25,-1,25,5,4,-1,3,0,18,-1,18,21,3,-1,6,9,7,-1,7,8,6,-1,22,20,2,-1,2,5,22,-1,6,11,10,-1,10,9,6,-1,0,13,12,-1,12,1,0,-1,1,12,14,-1,14,2,1,-1,3,4,15,-1,15,16,3,-1,5,17,15,-1,15,4,5,-1,3,16,13,-1,13,0,3,-1,2,14,17,-1,17,5,2,-1,15,6,8,-1,8,16,15,-1,16,8,7,-1,7,13,16,-1,13,7,9,-1,9,12,13,-1,15,17,11,-1,11,6,15,-1,12,9,10,-1,10,14,12,-1,14,10,11,-1,11,17,14,-1,4,3,23,-1,23,24,4,-1,23,3,21,-1,18,19,27,-1,27,26,18,-1,19,20,28,-1,28,27,19,-1,20,22,29,-1,29,28,20,-1,22,25,29,-1,23,21,30,-1,21,18,26,-1,26,30,21,-1,23,25,24,-1,29,25,23,-1,23,30,29,-1,27,28,29,-1,26,27,29,-1,30,26,29,-1]
IndexedFaceSet78.creaseAngle = 1.57
IndexedFaceSet78.texCoordIndex = [0,1,19,-1,19,18,0,-1,1,2,20,-1,20,19,1,-1,22,5,25,-1,4,24,25,-1,25,5,4,-1,3,0,18,-1,18,21,3,-1,6,9,7,-1,7,8,6,-1,22,20,2,-1,2,5,22,-1,6,11,10,-1,10,9,6,-1,0,13,12,-1,12,1,0,-1,1,12,14,-1,14,2,1,-1,3,4,15,-1,15,16,3,-1,5,17,15,-1,15,4,5,-1,3,16,13,-1,13,0,3,-1,2,14,17,-1,17,5,2,-1,15,6,8,-1,8,16,15,-1,16,8,7,-1,7,13,16,-1,13,7,9,-1,9,12,13,-1,15,17,11,-1,11,6,15,-1,12,9,10,-1,10,14,12,-1,14,10,11,-1,11,17,14,-1,4,3,23,-1,23,24,4,-1,23,3,21,-1,18,19,27,-1,27,26,18,-1,19,20,28,-1,28,27,19,-1,20,22,29,-1,29,28,20,-1,22,25,29,-1,23,21,30,-1,21,18,26,-1,26,30,21,-1,23,25,24,-1,29,25,23,-1,23,30,29,-1,27,28,29,-1,26,27,29,-1,30,26,29,-1]
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
HAnimJoint81.center = [-4.001,41.139999,-1.119]
HAnimJoint81.ulimit = [0,0,0]
HAnimJoint81.llimit = [0,0,0]
HAnimSegment82 = x3d.HAnimSegment()
HAnimSegment82.name = "r_thigh"
HAnimSegment82.DEF = "hanim_r_thigh"
Transform83 = x3d.Transform()
Transform83.translation = [-4.001,41.139999,-1.119]
Shape84 = x3d.Shape()
Appearance85 = x3d.Appearance()
Material86 = x3d.Material()
Material86.diffuseColor = [0.588,0.588,0.588]

Appearance85.material = Material86
ImageTexture87 = x3d.ImageTexture()
ImageTexture87.USE = "ChulTextureAtlas"

Appearance85.texture = ImageTexture87

Shape84.appearance = Appearance85
IndexedFaceSet88 = x3d.IndexedFaceSet()
IndexedFaceSet88.coordIndex = [36,37,38,-1,35,36,38,-1,38,39,40,-1,35,38,40,-1,41,35,40,-1,0,7,8,-1,8,1,0,-1,1,8,9,-1,9,2,1,-1,2,9,10,-1,10,3,2,-1,3,10,11,-1,11,4,3,-1,4,11,12,-1,12,5,4,-1,5,12,13,-1,13,6,5,-1,6,13,7,-1,7,0,6,-1,7,14,15,-1,15,8,7,-1,8,15,16,-1,16,9,8,-1,9,16,17,-1,17,10,9,-1,10,17,18,-1,18,11,10,-1,11,18,19,-1,19,12,11,-1,12,19,20,-1,20,13,12,-1,13,20,14,-1,14,7,13,-1,14,106,107,-1,107,15,14,-1,15,107,108,-1,108,16,15,-1,16,108,109,-1,109,17,16,-1,17,109,110,-1,110,18,17,-1,18,110,111,-1,111,19,18,-1,19,111,112,-1,112,20,19,-1,20,112,106,-1,106,14,20,-1,29,107,106,-1,106,28,29,-1,30,108,107,-1,107,29,30,-1,31,109,108,-1,108,30,31,-1,32,110,109,-1,109,31,32,-1,33,111,110,-1,110,32,33,-1,34,112,111,-1,111,33,34,-1,28,106,112,-1,112,34,28,-1,35,0,1,-1,1,36,35,-1,36,1,2,-1,2,37,36,-1,37,2,3,-1,3,38,37,-1,38,3,4,-1,4,39,38,-1,39,4,5,-1,5,40,39,-1,40,5,6,-1,6,41,40,-1,41,6,0,-1,0,35,41,-1,113,21,43,-1,50,42,51,-1,115,22,113,-1,52,44,53,-1,116,23,115,-1,54,45,55,-1,117,24,116,-1,56,46,57,-1,118,25,117,-1,58,47,59,-1,119,26,118,-1,60,48,61,-1,43,27,119,-1,62,114,63,-1,122,65,64,-1,66,130,67,-1,121,69,68,-1,70,129,71,-1,123,73,72,-1,74,131,75,-1,124,77,76,-1,78,132,79,-1,125,81,80,-1,82,133,83,-1,126,85,84,-1,86,134,87,-1,127,89,88,-1,90,135,91,-1,43,140,113,-1,113,140,115,-1,115,140,116,-1,116,140,117,-1,117,140,118,-1,118,140,119,-1,119,140,43,-1,92,49,93,-1,94,120,95,-1,96,128,97,-1,98,136,99,-1,100,137,101,-1,102,138,103,-1,104,139,105,-1]
IndexedFaceSet88.creaseAngle = 1.57
IndexedFaceSet88.texCoordIndex = [0,2,3,-1,1,0,3,-1,3,4,5,-1,1,3,5,-1,6,1,5,-1,7,9,8,-1,8,10,7,-1,10,8,11,-1,11,12,10,-1,12,11,13,-1,13,14,12,-1,14,13,15,-1,15,16,14,-1,16,15,17,-1,17,18,16,-1,18,17,19,-1,19,20,18,-1,20,19,9,-1,9,7,20,-1,9,22,21,-1,21,8,9,-1,8,21,23,-1,23,11,8,-1,11,23,24,-1,24,13,11,-1,13,24,25,-1,25,15,13,-1,15,25,26,-1,26,17,15,-1,17,26,27,-1,27,19,17,-1,19,27,22,-1,22,9,19,-1,22,29,28,-1,28,21,22,-1,21,28,30,-1,30,23,21,-1,23,30,31,-1,31,24,23,-1,24,31,32,-1,32,25,24,-1,25,32,33,-1,33,26,25,-1,26,33,34,-1,34,27,26,-1,27,34,29,-1,29,22,27,-1,35,28,29,-1,29,36,35,-1,37,30,28,-1,28,35,37,-1,38,31,30,-1,30,37,38,-1,39,32,31,-1,31,38,39,-1,40,33,32,-1,32,39,40,-1,41,34,33,-1,33,40,41,-1,36,29,34,-1,34,41,36,-1,1,7,10,-1,10,0,1,-1,0,10,12,-1,12,2,0,-1,2,12,14,-1,14,3,2,-1,3,14,16,-1,16,4,3,-1,4,16,18,-1,18,5,4,-1,5,18,20,-1,20,6,5,-1,6,20,7,-1,7,1,6,-1,42,29,43,-1,29,42,28,-1,44,28,42,-1,28,44,30,-1,45,30,44,-1,30,45,31,-1,46,31,45,-1,31,46,32,-1,47,32,46,-1,32,47,33,-1,48,33,47,-1,33,48,34,-1,43,34,48,-1,34,43,29,-1,43,28,42,-1,28,43,29,-1,42,30,44,-1,30,42,28,-1,44,31,45,-1,31,44,30,-1,45,32,46,-1,32,45,31,-1,46,33,47,-1,33,46,32,-1,47,34,48,-1,34,47,33,-1,48,29,43,-1,29,48,34,-1,43,49,42,-1,42,49,44,-1,44,49,45,-1,45,49,46,-1,46,49,47,-1,47,49,48,-1,48,49,43,-1,42,49,43,-1,44,49,42,-1,45,49,44,-1,46,49,45,-1,47,49,46,-1,48,49,47,-1,43,49,48,-1]
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
HAnimJoint91.center = [-4.315,25.190001,-1.119]
HAnimJoint91.ulimit = [0,0,0]
HAnimJoint91.llimit = [0,0,0]
HAnimSegment92 = x3d.HAnimSegment()
HAnimSegment92.name = "r_calf"
HAnimSegment92.DEF = "hanim_r_calf"
Transform93 = x3d.Transform()
Transform93.translation = [-4.315,25.190001,-1.119]
Shape94 = x3d.Shape()
Appearance95 = x3d.Appearance()
Material96 = x3d.Material()
Material96.diffuseColor = [0.588,0.588,0.588]

Appearance95.material = Material96
ImageTexture97 = x3d.ImageTexture()
ImageTexture97.USE = "ChulTextureAtlas"

Appearance95.texture = ImageTexture97

Shape94.appearance = Appearance95
IndexedFaceSet98 = x3d.IndexedFaceSet()
IndexedFaceSet98.coordIndex = [36,37,38,-1,35,36,38,-1,38,39,40,-1,35,38,40,-1,41,35,40,-1,0,7,8,-1,8,1,0,-1,1,8,9,-1,9,2,1,-1,2,9,10,-1,10,3,2,-1,3,10,11,-1,11,4,3,-1,4,11,12,-1,12,5,4,-1,5,12,13,-1,13,6,5,-1,6,13,7,-1,7,0,6,-1,7,14,15,-1,15,8,7,-1,8,15,16,-1,16,9,8,-1,9,16,17,-1,17,10,9,-1,10,17,18,-1,18,11,10,-1,11,18,19,-1,19,12,11,-1,12,19,20,-1,20,13,12,-1,13,20,14,-1,14,7,13,-1,14,21,22,-1,22,15,14,-1,15,22,23,-1,23,16,15,-1,16,23,24,-1,24,17,16,-1,17,24,25,-1,25,18,17,-1,18,25,26,-1,26,19,18,-1,19,26,27,-1,27,20,19,-1,20,27,21,-1,21,14,20,-1,29,22,21,-1,21,28,29,-1,30,23,22,-1,22,29,30,-1,31,24,23,-1,23,30,31,-1,32,25,24,-1,24,31,32,-1,33,26,25,-1,25,32,33,-1,34,27,26,-1,26,33,34,-1,28,21,27,-1,27,34,28,-1,35,0,1,-1,1,36,35,-1,36,1,2,-1,2,37,36,-1,37,2,3,-1,3,38,37,-1,38,3,4,-1,4,39,38,-1,39,4,5,-1,5,40,39,-1,40,5,6,-1,6,41,40,-1,41,6,0,-1,0,35,41,-1]
IndexedFaceSet98.creaseAngle = 1.57
IndexedFaceSet98.texCoordIndex = [0,2,3,-1,1,0,3,-1,3,4,5,-1,1,3,5,-1,6,1,5,-1,7,9,8,-1,8,10,7,-1,10,8,11,-1,11,12,10,-1,12,11,13,-1,13,14,12,-1,14,13,15,-1,15,16,14,-1,16,15,17,-1,17,18,16,-1,18,17,19,-1,19,20,18,-1,20,19,9,-1,9,7,20,-1,9,22,21,-1,21,8,9,-1,8,21,23,-1,23,11,8,-1,11,23,24,-1,24,13,11,-1,13,24,25,-1,25,15,13,-1,15,25,26,-1,26,17,15,-1,17,26,27,-1,27,19,17,-1,19,27,22,-1,22,9,19,-1,22,29,28,-1,28,21,22,-1,21,28,30,-1,30,23,21,-1,23,30,31,-1,31,24,23,-1,24,31,32,-1,32,25,24,-1,25,32,33,-1,33,26,25,-1,26,33,34,-1,34,27,26,-1,27,34,29,-1,29,22,27,-1,35,28,29,-1,29,36,35,-1,37,30,28,-1,28,35,37,-1,38,31,30,-1,30,37,38,-1,39,32,31,-1,31,38,39,-1,40,33,32,-1,32,39,40,-1,41,34,33,-1,33,40,41,-1,36,29,34,-1,34,41,36,-1,1,7,10,-1,10,0,1,-1,0,10,12,-1,12,2,0,-1,2,12,14,-1,14,3,2,-1,3,14,16,-1,16,4,3,-1,4,16,18,-1,18,5,4,-1,5,18,20,-1,20,6,5,-1,6,20,7,-1,7,1,6,-1]
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
HAnimJoint101.center = [-4.574,6.838,-1.463]
HAnimJoint101.ulimit = [0,0,0]
HAnimJoint101.llimit = [0,0,0]
HAnimSegment102 = x3d.HAnimSegment()
HAnimSegment102.name = "r_talus"
HAnimSegment102.DEF = "hanim_r_talus"
Transform103 = x3d.Transform()
Transform103.translation = [-4.574,6.838,-1.463]
Shape104 = x3d.Shape()
Appearance105 = x3d.Appearance()
Material106 = x3d.Material()
Material106.diffuseColor = [0.588,0.588,0.588]

Appearance105.material = Material106
ImageTexture107 = x3d.ImageTexture()
ImageTexture107.USE = "ChulTextureAtlas"

Appearance105.texture = ImageTexture107

Shape104.appearance = Appearance105
IndexedFaceSet108 = x3d.IndexedFaceSet()
IndexedFaceSet108.coordIndex = [0,2,1,-1,1,4,0,-1,3,2,0,-1,0,5,3,-1,6,8,7,-1,7,9,6,-1,8,11,10,-1,10,7,8,-1,12,6,9,-1,9,20,12,-1,21,13,12,-1,12,20,21,-1,11,15,14,-1,14,10,11,-1,15,17,16,-1,16,14,15,-1,9,7,4,-1,4,1,9,-1,7,10,0,-1,0,4,7,-1,10,14,5,-1,5,0,10,-1,14,16,3,-1,3,5,14,-1,6,19,8,-1,8,19,11,-1,12,19,6,-1,13,19,12,-1,11,19,15,-1,15,19,17,-1,17,19,18,-1,18,19,13,-1,13,21,22,-1,22,18,13,-1,18,22,16,-1,16,17,18,-1,24,23,30,-1,24,30,29,-1,24,29,28,-1,28,27,26,-1,24,28,26,-1,24,26,25,-1,2,23,24,-1,24,1,2,-1,1,24,25,-1,25,9,1,-1,9,25,26,-1,26,20,9,-1,20,26,27,-1,27,21,20,-1,21,27,28,-1,28,22,21,-1,22,28,29,-1,29,16,22,-1,16,29,30,-1,30,3,16,-1,3,30,23,-1,23,2,3,-1]
IndexedFaceSet108.creaseAngle = 1.57
IndexedFaceSet108.texCoordIndex = [0,2,1,-1,1,4,0,-1,3,2,0,-1,0,5,3,-1,6,8,7,-1,7,9,6,-1,8,11,10,-1,10,7,8,-1,12,6,9,-1,9,20,12,-1,21,13,12,-1,12,20,21,-1,11,15,14,-1,14,10,11,-1,15,17,16,-1,16,14,15,-1,9,7,4,-1,4,1,9,-1,7,10,0,-1,0,4,7,-1,10,14,5,-1,5,0,10,-1,14,16,3,-1,3,5,14,-1,6,19,8,-1,8,19,11,-1,12,19,6,-1,13,19,12,-1,11,19,15,-1,15,19,17,-1,17,19,18,-1,18,19,13,-1,13,21,22,-1,22,18,13,-1,18,22,16,-1,16,17,18,-1,24,23,30,-1,24,30,29,-1,24,29,28,-1,28,27,26,-1,24,28,26,-1,24,26,25,-1,2,23,24,-1,24,1,2,-1,1,24,25,-1,25,9,1,-1,9,25,26,-1,26,20,9,-1,20,26,27,-1,27,21,20,-1,21,27,28,-1,28,22,21,-1,22,28,29,-1,29,16,22,-1,16,29,30,-1,30,3,16,-1,3,30,23,-1,23,2,3,-1]
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
HAnimJoint111.center = [-4.809,5.583,1.492]
HAnimJoint111.ulimit = [0,0,0]
HAnimJoint111.llimit = [0,0,0]
HAnimSegment112 = x3d.HAnimSegment()
HAnimSegment112.name = "r_tarsal_proximal_phalanx_2"
HAnimSegment112.DEF = "hanim_r_tarsal_proximal_phalanx_2"
Transform113 = x3d.Transform()
Transform113.translation = [-4.809,5.583,1.492]
Shape114 = x3d.Shape()
Appearance115 = x3d.Appearance()
Material116 = x3d.Material()
Material116.diffuseColor = [0.588,0.588,0.588]

Appearance115.material = Material116
ImageTexture117 = x3d.ImageTexture()
ImageTexture117.USE = "ChulTextureAtlas"

Appearance115.texture = ImageTexture117

Shape114.appearance = Appearance115
IndexedFaceSet118 = x3d.IndexedFaceSet()
IndexedFaceSet118.coordIndex = [0,18,19,-1,19,1,0,-1,1,19,20,-1,20,2,1,-1,22,25,5,-1,4,5,25,-1,25,24,4,-1,3,21,18,-1,18,0,3,-1,6,8,7,-1,7,9,6,-1,22,5,2,-1,2,20,22,-1,6,9,10,-1,10,11,6,-1,0,1,12,-1,12,13,0,-1,1,2,14,-1,14,12,1,-1,3,16,15,-1,15,4,3,-1,5,4,15,-1,15,17,5,-1,3,0,13,-1,13,16,3,-1,2,5,17,-1,17,14,2,-1,15,16,8,-1,8,6,15,-1,16,13,7,-1,7,8,16,-1,13,12,9,-1,9,7,13,-1,15,6,11,-1,11,17,15,-1,12,14,10,-1,10,9,12,-1,14,17,11,-1,11,10,14,-1,4,24,23,-1,23,3,4,-1,23,21,3,-1,18,26,27,-1,27,19,18,-1,19,27,28,-1,28,20,19,-1,20,28,29,-1,29,22,20,-1,22,29,25,-1,23,30,21,-1,21,30,26,-1,26,18,21,-1,23,24,25,-1,29,30,23,-1,23,25,29,-1,29,28,27,-1,29,27,26,-1,30,29,26,-1]
IndexedFaceSet118.creaseAngle = 1.57
IndexedFaceSet118.texCoordIndex = [0,18,19,-1,19,1,0,-1,1,19,20,-1,20,2,1,-1,22,25,5,-1,4,5,25,-1,25,24,4,-1,3,21,18,-1,18,0,3,-1,6,8,7,-1,7,9,6,-1,22,5,2,-1,2,20,22,-1,6,9,10,-1,10,11,6,-1,0,1,12,-1,12,13,0,-1,1,2,14,-1,14,12,1,-1,3,16,15,-1,15,4,3,-1,5,4,15,-1,15,17,5,-1,3,0,13,-1,13,16,3,-1,2,5,17,-1,17,14,2,-1,15,16,8,-1,8,6,15,-1,16,13,7,-1,7,8,16,-1,13,12,9,-1,9,7,13,-1,15,6,11,-1,11,17,15,-1,12,14,10,-1,10,9,12,-1,14,17,11,-1,11,10,14,-1,4,24,23,-1,23,3,4,-1,23,21,3,-1,18,26,27,-1,27,19,18,-1,19,27,28,-1,28,20,19,-1,20,28,29,-1,29,22,20,-1,22,29,25,-1,23,30,21,-1,21,30,26,-1,26,18,21,-1,23,24,25,-1,29,30,23,-1,23,25,29,-1,29,28,27,-1,29,27,26,-1,30,29,26,-1]
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
HAnimJoint121.center = [0,38.639999,-1.034]
HAnimJoint121.ulimit = [0,0,0]
HAnimJoint121.llimit = [0,0,0]
HAnimSegment122 = x3d.HAnimSegment()
HAnimSegment122.name = "pelvis"
HAnimSegment122.DEF = "hanim_pelvis"
Transform123 = x3d.Transform()
Transform123.translation = [0,38.639999,-1.034]
Shape124 = x3d.Shape()
Appearance125 = x3d.Appearance()
Material126 = x3d.Material()
Material126.diffuseColor = [0.588,0.588,0.588]

Appearance125.material = Material126
ImageTexture127 = x3d.ImageTexture()
ImageTexture127.USE = "ChulTextureAtlas"

Appearance125.texture = ImageTexture127

Shape124.appearance = Appearance125
IndexedFaceSet128 = x3d.IndexedFaceSet()
IndexedFaceSet128.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,5,-1,0,5,6,-1,0,6,7,-1,0,7,8,-1,0,8,9,-1,0,9,10,-1,0,10,11,-1,0,11,12,-1,0,12,1,-1,14,2,1,-1,1,13,14,-1,15,3,2,-1,2,14,15,-1,16,4,3,-1,3,15,16,-1,17,5,4,-1,4,16,17,-1,18,6,5,-1,5,17,18,-1,19,7,6,-1,6,18,19,-1,20,8,7,-1,7,19,20,-1,21,9,8,-1,8,20,21,-1,22,10,9,-1,9,21,22,-1,23,11,10,-1,10,22,23,-1,24,12,11,-1,11,23,24,-1,13,1,12,-1,12,24,13,-1,26,14,13,-1,13,25,26,-1,27,15,14,-1,14,26,27,-1,28,16,15,-1,15,27,28,-1,29,17,16,-1,16,28,29,-1,30,18,17,-1,17,29,30,-1,31,19,18,-1,18,30,31,-1,32,20,19,-1,19,31,32,-1,33,21,20,-1,20,32,33,-1,34,22,21,-1,21,33,34,-1,35,23,22,-1,22,34,35,-1,36,24,23,-1,23,35,36,-1,25,13,24,-1,24,36,25,-1,38,26,25,-1,25,37,38,-1,39,27,26,-1,26,38,39,-1,40,28,27,-1,27,39,40,-1,41,29,28,-1,28,40,41,-1,42,30,29,-1,29,41,42,-1,43,31,30,-1,30,42,43,-1,44,32,31,-1,31,43,44,-1,45,33,32,-1,32,44,45,-1,46,34,33,-1,33,45,46,-1,47,35,34,-1,34,46,47,-1,48,36,35,-1,35,47,48,-1,37,25,36,-1,36,48,37,-1,50,38,37,-1,37,49,50,-1,51,39,38,-1,38,50,51,-1,52,40,39,-1,39,51,52,-1,53,41,40,-1,40,52,53,-1,54,42,41,-1,41,53,54,-1,55,43,42,-1,42,54,55,-1,56,44,43,-1,43,55,56,-1,57,45,44,-1,44,56,57,-1,58,46,45,-1,45,57,58,-1,59,47,46,-1,46,58,59,-1,60,48,47,-1,47,59,60,-1,49,37,48,-1,48,60,49,-1,61,50,49,-1,61,51,50,-1,61,52,51,-1,61,53,52,-1,61,54,53,-1,61,55,54,-1,61,56,55,-1,61,57,56,-1,61,58,57,-1,61,59,58,-1,61,60,59,-1,61,49,60,-1]
IndexedFaceSet128.creaseAngle = 1.57
IndexedFaceSet128.texCoordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,5,-1,0,5,6,-1,0,6,7,-1,0,7,8,-1,0,8,9,-1,0,9,10,-1,0,10,11,-1,0,11,12,-1,0,12,1,-1,14,2,1,-1,1,13,14,-1,15,3,2,-1,2,14,15,-1,16,4,3,-1,3,15,16,-1,17,5,4,-1,4,16,17,-1,18,6,5,-1,5,17,18,-1,19,7,6,-1,6,18,19,-1,20,8,7,-1,7,19,20,-1,21,9,8,-1,8,20,21,-1,22,10,9,-1,9,21,22,-1,23,11,10,-1,10,22,23,-1,24,12,11,-1,11,23,24,-1,13,1,12,-1,12,24,13,-1,26,14,13,-1,13,25,26,-1,27,15,14,-1,14,26,27,-1,28,16,15,-1,15,27,28,-1,29,17,16,-1,16,28,29,-1,30,18,17,-1,17,29,30,-1,31,19,18,-1,18,30,31,-1,32,20,19,-1,19,31,32,-1,33,21,20,-1,20,32,33,-1,34,22,21,-1,21,33,34,-1,35,23,22,-1,22,34,35,-1,36,24,23,-1,23,35,36,-1,25,13,24,-1,24,36,25,-1,38,26,25,-1,25,37,38,-1,39,27,26,-1,26,38,39,-1,40,28,27,-1,27,39,40,-1,41,29,28,-1,28,40,41,-1,42,30,29,-1,29,41,42,-1,43,31,30,-1,30,42,43,-1,44,32,31,-1,31,43,44,-1,45,33,32,-1,32,44,45,-1,46,34,33,-1,33,45,46,-1,47,35,34,-1,34,46,47,-1,48,36,35,-1,35,47,48,-1,37,25,36,-1,36,48,37,-1,50,38,37,-1,37,49,50,-1,51,39,38,-1,38,50,51,-1,52,40,39,-1,39,51,52,-1,53,41,40,-1,40,52,53,-1,54,42,41,-1,41,53,54,-1,55,43,42,-1,42,54,55,-1,56,44,43,-1,43,55,56,-1,57,45,44,-1,44,56,57,-1,58,46,45,-1,45,57,58,-1,59,47,46,-1,46,58,59,-1,60,48,47,-1,47,59,60,-1,49,37,48,-1,48,60,49,-1,61,50,49,-1,61,51,50,-1,61,52,51,-1,61,53,52,-1,61,54,53,-1,61,55,54,-1,61,56,55,-1,61,57,56,-1,61,58,57,-1,61,59,58,-1,61,60,59,-1,61,49,60,-1]
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
HAnimJoint131.center = [7.699,59.419998,-1.567]
HAnimJoint131.ulimit = [0,0,0]
HAnimJoint131.llimit = [0,0,0]
HAnimSegment132 = x3d.HAnimSegment()
HAnimSegment132.name = "l_upperarm"
HAnimSegment132.DEF = "hanim_l_upperarm"
Transform133 = x3d.Transform()
Transform133.translation = [7.699,59.419998,-1.567]
Shape134 = x3d.Shape()
Appearance135 = x3d.Appearance()
Material136 = x3d.Material()
Material136.diffuseColor = [0.588,0.588,0.588]

Appearance135.material = Material136
ImageTexture137 = x3d.ImageTexture()
ImageTexture137.USE = "ChulTextureAtlas"

Appearance135.texture = ImageTexture137

Shape134.appearance = Appearance135
IndexedFaceSet138 = x3d.IndexedFaceSet()
IndexedFaceSet138.coordIndex = [0,1,2,-1,3,4,5,-1,2,1,6,-1,6,7,2,-1,7,6,8,-1,8,9,7,-1,9,8,5,-1,5,4,9,-1,0,11,10,-1,10,1,0,-1,5,13,12,-1,12,3,5,-1,6,1,10,-1,10,14,6,-1,6,14,15,-1,15,8,6,-1,8,15,13,-1,13,5,8,-1,12,17,16,-1,16,11,12,-1,10,11,16,-1,16,18,10,-1,13,19,17,-1,17,12,13,-1,10,18,20,-1,20,14,10,-1,15,14,20,-1,20,21,15,-1,13,15,21,-1,21,19,13,-1,17,23,22,-1,22,16,17,-1,18,16,22,-1,22,24,18,-1,19,25,23,-1,23,17,19,-1,18,24,26,-1,26,20,18,-1,21,20,26,-1,26,27,21,-1,19,21,27,-1,27,25,19,-1,23,29,28,-1,28,22,23,-1,22,28,30,-1,30,24,22,-1,25,31,29,-1,29,23,25,-1,24,30,32,-1,32,26,24,-1,26,32,33,-1,33,27,26,-1,27,33,31,-1,31,25,27,-1,29,35,34,-1,34,28,29,-1,28,34,36,-1,36,30,28,-1,31,37,35,-1,35,29,31,-1,30,36,38,-1,38,32,30,-1,32,38,39,-1,39,33,32,-1,33,39,37,-1,37,31,33,-1,0,2,40,-1,40,41,0,-1,4,3,42,-1,42,43,4,-1,2,7,44,-1,44,40,2,-1,7,9,45,-1,45,44,7,-1,9,4,43,-1,43,45,9,-1,3,12,46,-1,46,42,3,-1,12,11,47,-1,47,46,12,-1,41,40,48,-1,43,42,48,-1,40,44,48,-1,44,45,48,-1,45,43,48,-1,42,46,48,-1,46,47,48,-1,34,35,49,-1,36,34,49,-1,35,37,49,-1,38,36,49,-1,39,38,49,-1,37,39,49,-1]
IndexedFaceSet138.creaseAngle = 1.57
IndexedFaceSet138.texCoordIndex = [0,1,2,-1,3,4,5,-1,2,1,6,-1,6,7,2,-1,7,6,8,-1,8,9,7,-1,9,8,5,-1,5,4,9,-1,0,11,10,-1,10,1,0,-1,5,13,12,-1,12,3,5,-1,6,1,10,-1,10,14,6,-1,6,14,15,-1,15,8,6,-1,8,15,13,-1,13,5,8,-1,50,51,16,-1,16,11,50,-1,10,11,16,-1,16,18,10,-1,13,19,17,-1,17,12,13,-1,10,18,20,-1,20,14,10,-1,15,14,20,-1,20,21,15,-1,13,15,21,-1,21,19,13,-1,52,53,22,-1,22,16,52,-1,18,16,22,-1,22,24,18,-1,19,25,23,-1,23,17,19,-1,18,24,26,-1,26,20,18,-1,21,20,26,-1,26,27,21,-1,19,21,27,-1,27,25,19,-1,54,55,28,-1,28,22,54,-1,22,28,30,-1,30,24,22,-1,25,31,29,-1,29,23,25,-1,24,30,32,-1,32,26,24,-1,26,32,33,-1,33,27,26,-1,27,33,31,-1,31,25,27,-1,56,57,34,-1,34,28,56,-1,28,34,36,-1,36,30,28,-1,31,37,35,-1,35,29,31,-1,30,36,38,-1,38,32,30,-1,32,38,39,-1,39,33,32,-1,33,39,37,-1,37,31,33,-1,0,2,40,-1,40,41,0,-1,4,3,42,-1,42,43,4,-1,2,7,44,-1,44,40,2,-1,7,9,45,-1,45,69,7,-1,9,4,43,-1,43,45,9,-1,3,12,46,-1,46,42,3,-1,59,11,47,-1,47,58,59,-1,41,40,48,-1,60,61,48,-1,40,44,48,-1,44,62,48,-1,63,64,48,-1,65,66,48,-1,67,47,48,-1,34,68,49,-1,36,34,49,-1,35,37,49,-1,38,36,49,-1,39,38,49,-1,37,39,49,-1]
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
HAnimJoint141.center = [8.026,48.450001,-1.959]
HAnimJoint141.ulimit = [0,0,0]
HAnimJoint141.llimit = [0,0,0]
HAnimSegment142 = x3d.HAnimSegment()
HAnimSegment142.name = "l_forearm"
HAnimSegment142.DEF = "hanim_l_forearm"
Transform143 = x3d.Transform()
Transform143.translation = [8.026,48.450001,-1.959]
Shape144 = x3d.Shape()
Appearance145 = x3d.Appearance()
Material146 = x3d.Material()
Material146.diffuseColor = [0.588,0.588,0.588]

Appearance145.material = Material146
ImageTexture147 = x3d.ImageTexture()
ImageTexture147.USE = "ChulTextureAtlas"

Appearance145.texture = ImageTexture147

Shape144.appearance = Appearance145
IndexedFaceSet148 = x3d.IndexedFaceSet()
IndexedFaceSet148.coordIndex = [0,3,1,-1,1,2,0,-1,2,1,4,-1,4,5,2,-1,6,7,3,-1,3,0,6,-1,5,4,8,-1,8,9,5,-1,9,8,10,-1,10,11,9,-1,11,10,7,-1,7,6,11,-1,3,13,12,-1,12,1,3,-1,4,1,12,-1,12,14,4,-1,13,3,7,-1,7,15,13,-1,4,14,16,-1,16,8,4,-1,8,16,17,-1,17,10,8,-1,7,10,17,-1,17,15,7,-1,13,19,18,-1,18,12,13,-1,12,18,20,-1,20,14,12,-1,13,15,21,-1,21,19,13,-1,16,14,20,-1,20,22,16,-1,16,22,23,-1,23,17,16,-1,17,23,21,-1,21,15,17,-1,24,25,19,-1,19,21,24,-1,26,20,18,-1,18,27,26,-1,25,27,18,-1,18,19,25,-1,24,21,23,-1,23,28,24,-1,28,23,22,-1,22,29,28,-1,26,29,22,-1,22,20,26,-1,0,2,30,-1,30,31,0,-1,2,5,32,-1,32,30,2,-1,6,0,31,-1,31,33,6,-1,5,9,34,-1,34,32,5,-1,9,11,35,-1,35,34,9,-1,11,6,33,-1,33,35,11,-1,31,30,36,-1,30,32,36,-1,33,31,36,-1,32,34,36,-1,34,35,36,-1,35,33,36,-1,25,24,37,-1,26,27,37,-1,27,25,37,-1,24,28,37,-1,28,29,37,-1,29,26,37,-1]
IndexedFaceSet148.creaseAngle = 1.57
IndexedFaceSet148.texCoordIndex = [0,3,1,-1,1,2,0,-1,2,1,4,-1,4,5,2,-1,6,7,3,-1,3,0,6,-1,5,4,8,-1,8,9,5,-1,38,39,10,-1,10,11,38,-1,11,10,7,-1,7,6,11,-1,3,13,12,-1,12,1,3,-1,4,1,12,-1,12,14,4,-1,13,3,7,-1,7,15,13,-1,4,14,16,-1,16,8,4,-1,40,41,17,-1,17,10,40,-1,7,10,17,-1,17,15,7,-1,13,19,18,-1,18,12,13,-1,12,18,20,-1,20,14,12,-1,13,15,21,-1,21,19,13,-1,16,14,20,-1,20,22,16,-1,42,43,23,-1,23,17,42,-1,17,23,21,-1,21,15,17,-1,24,25,19,-1,19,21,24,-1,26,20,18,-1,18,27,26,-1,25,27,18,-1,18,19,25,-1,24,21,23,-1,23,28,24,-1,28,23,44,-1,44,45,28,-1,26,29,22,-1,22,20,26,-1,0,2,30,-1,30,31,0,-1,2,5,32,-1,32,30,2,-1,6,0,31,-1,31,33,6,-1,5,9,34,-1,34,32,5,-1,47,11,35,-1,35,46,47,-1,11,6,33,-1,33,35,11,-1,31,30,48,-1,30,32,36,-1,33,31,49,-1,32,34,36,-1,50,35,51,-1,35,33,52,-1,25,24,37,-1,26,27,37,-1,27,25,37,-1,24,28,37,-1,28,53,37,-1,29,26,37,-1]
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
HAnimJoint151.center = [7.617,37.689999,-1.663]
HAnimJoint151.ulimit = [0,0,0]
HAnimJoint151.llimit = [0,0,0]
HAnimSegment152 = x3d.HAnimSegment()
HAnimSegment152.name = "l_carpal"
HAnimSegment152.DEF = "hanim_l_carpal"
Transform153 = x3d.Transform()
Transform153.translation = [7.617,37.689999,-1.663]
Shape154 = x3d.Shape()
Appearance155 = x3d.Appearance()
Material156 = x3d.Material()
Material156.diffuseColor = [0.588,0.588,0.588]

Appearance155.material = Material156
ImageTexture157 = x3d.ImageTexture()
ImageTexture157.USE = "ChulTextureAtlas"

Appearance155.texture = ImageTexture157

Shape154.appearance = Appearance155
IndexedFaceSet158 = x3d.IndexedFaceSet()
IndexedFaceSet158.coordIndex = [0,3,1,-1,1,2,0,-1,4,7,5,-1,5,6,4,-1,10,11,8,-1,8,9,10,-1,14,15,12,-1,12,13,14,-1,11,14,13,-1,13,8,11,-1,17,10,9,-1,9,16,17,-1,19,17,16,-1,16,18,19,-1,15,19,18,-1,18,12,15,-1,20,21,11,-1,11,10,20,-1,24,25,22,-1,22,23,24,-1,21,26,14,-1,14,11,21,-1,27,20,10,-1,10,17,27,-1,28,27,17,-1,17,19,28,-1,29,28,19,-1,19,15,29,-1,2,1,21,-1,21,20,2,-1,3,0,29,-1,29,26,3,-1,1,3,26,-1,26,21,1,-1,30,2,20,-1,20,27,30,-1,31,30,27,-1,27,28,31,-1,0,31,28,-1,28,29,0,-1,32,33,0,-1,0,2,32,-1,34,32,2,-1,2,30,34,-1,35,34,30,-1,30,31,35,-1,33,35,31,-1,31,0,33,-1,36,37,32,-1,32,34,36,-1,38,36,34,-1,34,35,38,-1,39,38,35,-1,35,33,39,-1,37,39,33,-1,33,32,37,-1,6,5,37,-1,37,36,6,-1,4,6,36,-1,36,38,4,-1,7,4,38,-1,38,39,7,-1,5,7,39,-1,39,37,5,-1,23,22,15,-1,15,14,23,-1,24,23,14,-1,14,26,24,-1,42,43,40,-1,40,41,42,-1,22,25,29,-1,29,15,22,-1,44,45,25,-1,25,24,44,-1,46,47,26,-1,26,29,46,-1,47,44,24,-1,24,26,47,-1,45,46,29,-1,29,25,45,-1,41,40,47,-1,47,46,41,-1,42,41,46,-1,46,45,42,-1,43,42,45,-1,45,44,43,-1,40,43,44,-1,44,47,40,-1,9,8,48,-1,13,12,48,-1,8,13,48,-1,16,9,48,-1,18,16,48,-1,12,18,48,-1]
IndexedFaceSet158.creaseAngle = 1.57
IndexedFaceSet158.texCoordIndex = [47,50,48,-1,48,49,47,-1,8,11,9,-1,9,10,8,-1,53,54,51,-1,51,52,53,-1,57,58,55,-1,55,56,57,-1,54,57,56,-1,56,51,54,-1,14,15,12,-1,12,13,14,-1,17,14,13,-1,13,16,17,-1,19,17,16,-1,16,18,19,-1,59,60,54,-1,54,53,59,-1,63,64,61,-1,61,62,63,-1,60,65,57,-1,57,54,60,-1,20,21,15,-1,15,14,20,-1,22,20,14,-1,14,17,22,-1,23,22,17,-1,17,19,23,-1,49,48,60,-1,60,59,49,-1,50,47,66,-1,66,65,50,-1,48,50,65,-1,65,60,48,-1,24,25,21,-1,21,20,24,-1,26,24,20,-1,20,22,26,-1,27,26,22,-1,22,23,27,-1,67,68,47,-1,47,49,67,-1,28,29,25,-1,25,24,28,-1,30,28,24,-1,24,26,30,-1,31,30,26,-1,26,27,31,-1,32,33,29,-1,29,28,32,-1,34,32,28,-1,28,30,34,-1,35,34,30,-1,30,31,35,-1,69,70,68,-1,68,67,69,-1,10,9,33,-1,33,32,10,-1,8,10,32,-1,32,34,8,-1,11,8,34,-1,34,35,11,-1,71,72,70,-1,70,69,71,-1,62,61,58,-1,58,57,62,-1,63,62,57,-1,57,65,63,-1,38,39,36,-1,36,37,38,-1,40,41,23,-1,23,19,40,-1,73,74,64,-1,64,63,73,-1,43,44,42,-1,42,23,43,-1,75,73,63,-1,63,65,75,-1,45,43,23,-1,23,41,45,-1,37,36,44,-1,44,43,37,-1,38,37,43,-1,43,45,38,-1,76,77,74,-1,74,73,76,-1,78,76,73,-1,73,75,78,-1,1,0,5,-1,3,2,6,-1,0,4,7,-1,13,12,46,-1,16,13,46,-1,18,16,46,-1]
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
HAnimJoint161.center = [-7.699,59.419998,-1.567]
HAnimJoint161.ulimit = [0,0,0]
HAnimJoint161.llimit = [0,0,0]
HAnimSegment162 = x3d.HAnimSegment()
HAnimSegment162.name = "r_upperarm"
HAnimSegment162.DEF = "hanim_r_upperarm"
Transform163 = x3d.Transform()
Transform163.translation = [-7.699,59.419998,-1.567]
Shape164 = x3d.Shape()
Appearance165 = x3d.Appearance()
Material166 = x3d.Material()
Material166.diffuseColor = [0.588,0.588,0.588]

Appearance165.material = Material166
ImageTexture167 = x3d.ImageTexture()
ImageTexture167.USE = "ChulTextureAtlas"

Appearance165.texture = ImageTexture167

Shape164.appearance = Appearance165
IndexedFaceSet168 = x3d.IndexedFaceSet()
IndexedFaceSet168.coordIndex = [0,2,1,-1,3,5,4,-1,2,7,6,-1,6,1,2,-1,7,9,8,-1,8,6,7,-1,9,4,5,-1,5,8,9,-1,0,1,10,-1,10,11,0,-1,5,3,12,-1,12,13,5,-1,6,14,10,-1,10,1,6,-1,6,8,15,-1,15,14,6,-1,8,5,13,-1,13,15,8,-1,12,11,16,-1,16,17,12,-1,10,18,16,-1,16,11,10,-1,13,12,17,-1,17,19,13,-1,10,14,20,-1,20,18,10,-1,15,21,20,-1,20,14,15,-1,13,19,21,-1,21,15,13,-1,17,16,22,-1,22,23,17,-1,18,24,22,-1,22,16,18,-1,19,17,23,-1,23,25,19,-1,18,20,26,-1,26,24,18,-1,21,27,26,-1,26,20,21,-1,19,25,27,-1,27,21,19,-1,23,22,28,-1,28,29,23,-1,22,24,30,-1,30,28,22,-1,25,23,29,-1,29,31,25,-1,24,26,32,-1,32,30,24,-1,26,27,33,-1,33,32,26,-1,27,25,31,-1,31,33,27,-1,29,28,34,-1,34,35,29,-1,28,30,36,-1,36,34,28,-1,31,29,35,-1,35,37,31,-1,30,32,38,-1,38,36,30,-1,32,33,39,-1,39,38,32,-1,33,31,37,-1,37,39,33,-1,0,41,40,-1,40,2,0,-1,4,43,42,-1,42,3,4,-1,2,40,44,-1,44,7,2,-1,7,44,45,-1,45,9,7,-1,9,45,43,-1,43,4,9,-1,3,42,46,-1,46,12,3,-1,12,46,47,-1,47,11,12,-1,41,48,40,-1,43,48,42,-1,40,48,44,-1,44,48,45,-1,45,48,43,-1,42,48,46,-1,46,48,47,-1,34,49,35,-1,36,49,34,-1,35,49,37,-1,38,49,36,-1,39,49,38,-1,37,49,39,-1]
IndexedFaceSet168.creaseAngle = 1.57
IndexedFaceSet168.texCoordIndex = [0,2,1,-1,3,5,4,-1,2,7,6,-1,6,1,2,-1,7,9,8,-1,8,6,7,-1,9,4,5,-1,5,8,9,-1,0,1,10,-1,10,11,0,-1,5,3,12,-1,12,13,5,-1,6,14,10,-1,10,1,6,-1,6,8,15,-1,15,14,6,-1,8,5,13,-1,13,15,8,-1,50,11,16,-1,16,51,50,-1,10,18,16,-1,16,11,10,-1,13,12,17,-1,17,19,13,-1,10,14,20,-1,20,18,10,-1,15,21,20,-1,20,14,15,-1,13,19,21,-1,21,15,13,-1,52,16,22,-1,22,53,52,-1,18,24,22,-1,22,16,18,-1,19,17,23,-1,23,25,19,-1,18,20,26,-1,26,24,18,-1,21,27,26,-1,26,20,21,-1,19,25,27,-1,27,21,19,-1,54,22,28,-1,28,55,54,-1,22,24,30,-1,30,28,22,-1,25,23,29,-1,29,31,25,-1,24,26,32,-1,32,30,24,-1,26,27,33,-1,33,32,26,-1,27,25,31,-1,31,33,27,-1,56,28,34,-1,34,57,56,-1,28,30,36,-1,36,34,28,-1,31,29,35,-1,35,37,31,-1,30,32,38,-1,38,36,30,-1,32,33,39,-1,39,38,32,-1,33,31,37,-1,37,39,33,-1,0,41,40,-1,40,2,0,-1,4,43,42,-1,42,3,4,-1,2,40,44,-1,44,7,2,-1,7,69,45,-1,45,9,7,-1,9,45,43,-1,43,4,9,-1,3,42,46,-1,46,12,3,-1,59,58,47,-1,47,11,59,-1,41,48,40,-1,60,48,61,-1,40,48,44,-1,44,48,62,-1,63,48,64,-1,65,48,66,-1,67,48,47,-1,34,49,68,-1,36,49,34,-1,35,49,37,-1,38,49,36,-1,39,49,38,-1,37,49,39,-1]
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
HAnimJoint171.center = [-8.026,48.450001,-1.959]
HAnimJoint171.ulimit = [0,0,0]
HAnimJoint171.llimit = [0,0,0]
HAnimSegment172 = x3d.HAnimSegment()
HAnimSegment172.name = "r_forearm"
HAnimSegment172.DEF = "hanim_r_forearm"
Transform173 = x3d.Transform()
Transform173.translation = [-8.026,48.450001,-1.959]
Shape174 = x3d.Shape()
Appearance175 = x3d.Appearance()
Material176 = x3d.Material()
Material176.diffuseColor = [0.588,0.588,0.588]

Appearance175.material = Material176
ImageTexture177 = x3d.ImageTexture()
ImageTexture177.USE = "ChulTextureAtlas"

Appearance175.texture = ImageTexture177

Shape174.appearance = Appearance175
IndexedFaceSet178 = x3d.IndexedFaceSet()
IndexedFaceSet178.coordIndex = [0,2,1,-1,1,3,0,-1,2,5,4,-1,4,1,2,-1,6,0,3,-1,3,7,6,-1,5,9,8,-1,8,4,5,-1,9,11,10,-1,10,8,9,-1,11,6,7,-1,7,10,11,-1,3,1,12,-1,12,13,3,-1,4,14,12,-1,12,1,4,-1,13,15,7,-1,7,3,13,-1,4,8,16,-1,16,14,4,-1,8,10,17,-1,17,16,8,-1,7,15,17,-1,17,10,7,-1,13,12,18,-1,18,19,13,-1,12,14,20,-1,20,18,12,-1,13,19,21,-1,21,15,13,-1,16,22,20,-1,20,14,16,-1,16,17,23,-1,23,22,16,-1,17,15,21,-1,21,23,17,-1,24,21,19,-1,19,25,24,-1,26,27,18,-1,18,20,26,-1,25,19,18,-1,18,27,25,-1,24,28,23,-1,23,21,24,-1,28,29,22,-1,22,23,28,-1,26,20,22,-1,22,29,26,-1,0,31,30,-1,30,2,0,-1,2,30,32,-1,32,5,2,-1,6,33,31,-1,31,0,6,-1,5,32,34,-1,34,9,5,-1,9,34,35,-1,35,11,9,-1,11,35,33,-1,33,6,11,-1,31,36,30,-1,30,36,32,-1,33,36,31,-1,32,36,34,-1,34,36,35,-1,35,36,33,-1,25,37,24,-1,26,37,27,-1,27,37,25,-1,24,37,28,-1,28,37,29,-1,29,37,26,-1]
IndexedFaceSet178.creaseAngle = 1.57
IndexedFaceSet178.texCoordIndex = [0,2,1,-1,1,3,0,-1,2,5,4,-1,4,1,2,-1,6,0,3,-1,3,7,6,-1,5,9,8,-1,8,4,5,-1,38,11,10,-1,10,39,38,-1,11,6,7,-1,7,10,11,-1,3,1,12,-1,12,13,3,-1,4,14,12,-1,12,1,4,-1,13,15,7,-1,7,3,13,-1,4,8,16,-1,16,14,4,-1,40,10,17,-1,17,41,40,-1,7,15,17,-1,17,10,7,-1,13,12,18,-1,18,19,13,-1,12,14,20,-1,20,18,12,-1,13,19,21,-1,21,15,13,-1,16,22,20,-1,20,14,16,-1,42,17,23,-1,23,43,42,-1,17,15,21,-1,21,23,17,-1,24,21,19,-1,19,25,24,-1,26,27,18,-1,18,20,26,-1,25,19,18,-1,18,27,25,-1,24,28,23,-1,23,21,24,-1,28,45,44,-1,44,23,28,-1,26,20,22,-1,22,29,26,-1,0,31,30,-1,30,2,0,-1,2,30,32,-1,32,5,2,-1,6,33,31,-1,31,0,6,-1,5,32,34,-1,34,9,5,-1,47,46,35,-1,35,11,47,-1,11,35,33,-1,33,6,11,-1,31,48,30,-1,30,36,32,-1,33,49,31,-1,32,36,34,-1,50,51,35,-1,35,52,33,-1,25,37,24,-1,26,37,27,-1,27,37,25,-1,24,37,28,-1,28,37,53,-1,29,37,26,-1]
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
HAnimJoint181.center = [-7.617,37.689999,-1.663]
HAnimJoint181.ulimit = [0,0,0]
HAnimJoint181.llimit = [0,0,0]
HAnimSegment182 = x3d.HAnimSegment()
HAnimSegment182.name = "r_carpal"
HAnimSegment182.DEF = "hanim_r_carpal"
Transform183 = x3d.Transform()
Transform183.translation = [-7.617,37.689999,-1.663]
Shape184 = x3d.Shape()
Appearance185 = x3d.Appearance()
Material186 = x3d.Material()
Material186.diffuseColor = [0.588,0.588,0.588]

Appearance185.material = Material186
ImageTexture187 = x3d.ImageTexture()
ImageTexture187.USE = "ChulTextureAtlas"

Appearance185.texture = ImageTexture187

Shape184.appearance = Appearance185
IndexedFaceSet188 = x3d.IndexedFaceSet()
IndexedFaceSet188.coordIndex = [0,2,1,-1,1,3,0,-1,4,6,5,-1,5,7,4,-1,10,9,8,-1,8,11,10,-1,14,13,12,-1,12,15,14,-1,11,8,13,-1,13,14,11,-1,17,16,9,-1,9,10,17,-1,19,18,16,-1,16,17,19,-1,15,12,18,-1,18,19,15,-1,20,10,11,-1,11,21,20,-1,24,23,22,-1,22,25,24,-1,21,11,14,-1,14,26,21,-1,27,17,10,-1,10,20,27,-1,28,19,17,-1,17,27,28,-1,29,15,19,-1,19,28,29,-1,2,20,21,-1,21,1,2,-1,3,26,29,-1,29,0,3,-1,1,21,26,-1,26,3,1,-1,30,27,20,-1,20,2,30,-1,31,28,27,-1,27,30,31,-1,0,29,28,-1,28,31,0,-1,32,2,0,-1,0,33,32,-1,34,30,2,-1,2,32,34,-1,35,31,30,-1,30,34,35,-1,33,0,31,-1,31,35,33,-1,36,34,32,-1,32,37,36,-1,38,35,34,-1,34,36,38,-1,39,33,35,-1,35,38,39,-1,37,32,33,-1,33,39,37,-1,6,36,37,-1,37,5,6,-1,4,38,36,-1,36,6,4,-1,7,39,38,-1,38,4,7,-1,5,37,39,-1,39,7,5,-1,23,14,15,-1,15,22,23,-1,24,26,14,-1,14,23,24,-1,42,41,40,-1,40,43,42,-1,22,15,29,-1,29,25,22,-1,44,24,25,-1,25,45,44,-1,46,29,26,-1,26,47,46,-1,47,26,24,-1,24,44,47,-1,45,25,29,-1,29,46,45,-1,41,46,47,-1,47,40,41,-1,42,45,46,-1,46,41,42,-1,43,44,45,-1,45,42,43,-1,40,47,44,-1,44,43,40,-1,9,48,8,-1,13,48,12,-1,8,48,13,-1,16,48,9,-1,18,48,16,-1,12,48,18,-1]
IndexedFaceSet188.creaseAngle = 1.57
IndexedFaceSet188.texCoordIndex = [47,49,48,-1,48,50,47,-1,8,10,9,-1,9,11,8,-1,53,52,51,-1,51,54,53,-1,57,56,55,-1,55,58,57,-1,54,51,56,-1,56,57,54,-1,14,13,12,-1,12,15,14,-1,17,16,13,-1,13,14,17,-1,19,18,16,-1,16,17,19,-1,59,53,54,-1,54,60,59,-1,63,62,61,-1,61,64,63,-1,60,54,57,-1,57,65,60,-1,20,14,15,-1,15,21,20,-1,22,17,14,-1,14,20,22,-1,23,19,17,-1,17,22,23,-1,49,59,60,-1,60,48,49,-1,50,65,66,-1,66,47,50,-1,48,60,65,-1,65,50,48,-1,24,20,21,-1,21,25,24,-1,26,22,20,-1,20,24,26,-1,27,23,22,-1,22,26,27,-1,67,49,47,-1,47,68,67,-1,28,24,25,-1,25,29,28,-1,30,26,24,-1,24,28,30,-1,31,27,26,-1,26,30,31,-1,32,28,29,-1,29,33,32,-1,34,30,28,-1,28,32,34,-1,35,31,30,-1,30,34,35,-1,69,67,68,-1,68,70,69,-1,10,32,33,-1,33,9,10,-1,8,34,32,-1,32,10,8,-1,11,35,34,-1,34,8,11,-1,71,69,70,-1,70,72,71,-1,62,57,58,-1,58,61,62,-1,63,65,57,-1,57,62,63,-1,38,37,36,-1,36,39,38,-1,40,19,23,-1,23,41,40,-1,73,63,64,-1,64,74,73,-1,43,23,42,-1,42,44,43,-1,75,65,63,-1,63,73,75,-1,45,41,23,-1,23,43,45,-1,37,43,44,-1,44,36,37,-1,38,45,43,-1,43,37,38,-1,76,73,74,-1,74,77,76,-1,78,75,73,-1,73,76,78,-1,1,5,0,-1,3,6,2,-1,0,7,4,-1,13,46,12,-1,16,46,13,-1,18,46,16,-1]
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
HAnimJoint191.center = [0,47.330002,-0.5744]
HAnimJoint191.ulimit = [0,0,0]
HAnimJoint191.llimit = [0,0,0]
HAnimSegment192 = x3d.HAnimSegment()
HAnimSegment192.name = "l5"
HAnimSegment192.DEF = "hanim_l5"
Transform193 = x3d.Transform()
Transform193.translation = [0,47.330002,-0.5744]
Shape194 = x3d.Shape()
Appearance195 = x3d.Appearance()
Material196 = x3d.Material()
Material196.diffuseColor = [0.588,0.588,0.588]

Appearance195.material = Material196
ImageTexture197 = x3d.ImageTexture()
ImageTexture197.USE = "ChulTextureAtlas"

Appearance195.texture = ImageTexture197

Shape194.appearance = Appearance195
IndexedFaceSet198 = x3d.IndexedFaceSet()
IndexedFaceSet198.coordIndex = [17,152,154,-1,154,25,17,-1,17,25,8,-1,8,4,17,-1,25,154,20,-1,20,181,25,-1,6,8,25,-1,25,181,6,-1,19,5,9,-1,9,26,19,-1,18,19,26,-1,26,27,18,-1,9,7,23,-1,23,26,9,-1,26,23,22,-1,22,27,26,-1,150,6,181,-1,181,3,150,-1,151,2,23,-1,23,7,151,-1,152,28,30,-1,30,18,152,-1,18,30,31,-1,31,19,18,-1,152,17,29,-1,29,28,152,-1,19,31,11,-1,11,5,19,-1,4,10,29,-1,29,17,4,-1,28,155,34,-1,34,30,28,-1,30,34,35,-1,35,31,30,-1,28,29,33,-1,33,155,28,-1,31,35,13,-1,13,11,31,-1,10,12,33,-1,33,29,10,-1,155,36,38,-1,38,34,155,-1,35,34,38,-1,38,39,35,-1,33,37,36,-1,36,155,33,-1,35,39,15,-1,15,13,35,-1,33,12,14,-1,14,37,33,-1,20,42,43,-1,43,22,20,-1,152,40,44,-1,44,154,152,-1,154,44,42,-1,42,20,154,-1,27,45,41,-1,41,18,27,-1,22,43,45,-1,45,27,22,-1,18,41,40,-1,40,152,18,-1,50,47,16,-1,108,109,158,-1,21,174,24,-1,110,111,153,-1,46,48,32,-1,156,112,113,-1,32,48,49,-1,115,157,114,-1,2,3,181,-1,53,116,117,-1,161,2,51,-1,2,151,52,-1,52,51,2,-1,22,23,181,-1,181,20,22,-1,181,23,2,-1,16,47,173,-1,119,182,118,-1,2,150,3,-1,121,0,120,-1,43,42,54,-1,54,55,43,-1,44,54,42,-1,45,43,55,-1,45,55,54,-1,54,44,45,-1,41,45,44,-1,44,40,41,-1,38,36,56,-1,56,57,38,-1,39,38,57,-1,57,58,39,-1,36,37,59,-1,59,56,36,-1,15,39,58,-1,58,60,15,-1,37,14,61,-1,61,59,37,-1,57,56,62,-1,58,57,62,-1,56,59,62,-1,60,58,62,-1,59,61,62,-1,178,162,66,-1,66,74,178,-1,8,74,66,-1,66,4,8,-1,69,178,74,-1,74,177,69,-1,74,8,6,-1,6,177,74,-1,9,5,68,-1,68,75,9,-1,75,68,67,-1,67,76,75,-1,72,7,9,-1,9,75,72,-1,71,72,75,-1,75,76,71,-1,177,6,150,-1,150,64,177,-1,72,63,151,-1,151,7,72,-1,79,77,162,-1,162,67,79,-1,80,79,67,-1,67,68,80,-1,78,66,162,-1,162,77,78,-1,11,80,68,-1,68,5,11,-1,78,10,4,-1,4,66,78,-1,83,165,77,-1,77,79,83,-1,84,83,79,-1,79,80,84,-1,82,78,77,-1,77,165,82,-1,13,84,80,-1,80,11,13,-1,82,12,10,-1,10,78,82,-1,87,85,165,-1,165,83,87,-1,87,83,84,-1,84,88,87,-1,85,86,82,-1,82,165,85,-1,15,88,84,-1,84,13,15,-1,14,12,82,-1,82,86,14,-1,92,91,69,-1,69,71,92,-1,93,89,162,-1,162,178,93,-1,91,93,178,-1,178,69,91,-1,90,94,76,-1,76,67,90,-1,94,92,71,-1,71,76,94,-1,89,90,67,-1,67,162,89,-1,99,65,96,-1,123,168,122,-1,70,73,180,-1,164,124,125,-1,95,81,97,-1,166,126,127,-1,81,98,97,-1,128,129,167,-1,63,177,64,-1,101,130,131,-1,170,100,63,-1,52,151,63,-1,63,100,52,-1,177,72,71,-1,71,69,177,-1,177,63,72,-1,65,179,96,-1,132,133,183,-1,63,64,150,-1,134,135,171,-1,102,91,92,-1,92,103,102,-1,93,91,102,-1,94,103,92,-1,102,103,94,-1,94,93,102,-1,93,94,90,-1,90,89,93,-1,104,85,87,-1,87,105,104,-1,105,87,88,-1,88,106,105,-1,107,86,85,-1,85,104,107,-1,106,88,15,-1,15,60,106,-1,61,14,86,-1,86,107,61,-1,105,62,104,-1,106,62,105,-1,104,62,107,-1,60,62,106,-1,107,62,61,-1,100,170,163,-1,169,136,137,-1,176,138,139,-1,140,141,172,-1,159,142,143,-1,175,144,145,-1,160,146,147,-1,148,149,1,-1,185,184,189,-1,189,190,185,-1,184,186,191,-1,191,189,184,-1,186,187,192,-1,192,191,186,-1,187,188,193,-1,193,192,187,-1,194,195,196,-1,196,197,194,-1,188,194,197,-1,197,193,188,-1,202,198,185,-1,185,190,202,-1,203,199,198,-1,198,202,203,-1,204,200,199,-1,199,203,204,-1,205,201,200,-1,200,204,205,-1,196,195,206,-1,206,207,196,-1,207,206,201,-1,201,205,207,-1]
IndexedFaceSet198.creaseAngle = 1.57
IndexedFaceSet198.texCoordIndex = [2,3,0,-1,0,1,2,-1,2,1,4,-1,4,5,2,-1,1,0,6,-1,6,7,1,-1,8,4,1,-1,1,7,8,-1,38,39,36,-1,36,37,38,-1,41,38,37,-1,37,40,41,-1,36,43,42,-1,42,37,36,-1,37,42,44,-1,44,40,37,-1,9,8,7,-1,7,10,9,-1,45,46,42,-1,42,43,45,-1,47,49,48,-1,48,41,47,-1,41,48,50,-1,50,38,41,-1,3,2,11,-1,11,12,3,-1,38,50,51,-1,51,39,38,-1,5,13,11,-1,11,2,5,-1,49,53,52,-1,52,48,49,-1,48,52,54,-1,54,50,48,-1,12,11,14,-1,14,15,12,-1,50,54,55,-1,55,51,50,-1,13,16,14,-1,14,11,13,-1,53,57,56,-1,56,52,53,-1,54,52,56,-1,56,58,54,-1,14,18,17,-1,17,15,14,-1,54,58,59,-1,59,55,54,-1,14,16,19,-1,19,18,14,-1,60,62,61,-1,61,44,60,-1,47,65,63,-1,63,64,47,-1,64,63,62,-1,62,60,64,-1,40,67,66,-1,66,41,40,-1,44,61,67,-1,67,40,44,-1,41,66,65,-1,65,47,41,-1,68,69,47,-1,47,64,68,-1,70,68,64,-1,64,60,70,-1,71,72,53,-1,71,53,49,-1,53,72,73,-1,53,73,57,-1,20,10,7,-1,74,70,46,-1,74,46,75,-1,46,45,76,-1,76,75,46,-1,44,42,70,-1,70,60,44,-1,70,42,46,-1,47,69,71,-1,47,71,49,-1,20,9,10,-1,21,9,20,-1,61,62,77,-1,77,78,61,-1,63,77,62,-1,67,61,78,-1,67,78,77,-1,77,63,67,-1,66,67,63,-1,63,65,66,-1,56,57,79,-1,79,80,56,-1,58,56,80,-1,80,81,58,-1,57,83,82,-1,82,79,57,-1,59,58,81,-1,81,84,59,-1,83,129,128,-1,128,82,83,-1,80,79,87,-1,81,80,87,-1,79,82,87,-1,84,81,87,-1,82,130,87,-1,22,25,23,-1,23,24,22,-1,4,24,23,-1,23,5,4,-1,26,22,24,-1,24,27,26,-1,24,4,8,-1,8,27,24,-1,36,39,88,-1,88,89,36,-1,89,88,90,-1,90,91,89,-1,92,43,36,-1,36,89,92,-1,93,92,89,-1,89,91,93,-1,27,8,9,-1,9,28,27,-1,92,94,45,-1,45,43,92,-1,96,97,95,-1,95,90,96,-1,98,96,90,-1,90,88,98,-1,29,23,25,-1,25,30,29,-1,51,98,88,-1,88,39,51,-1,29,13,5,-1,5,23,29,-1,99,100,97,-1,97,96,99,-1,101,99,96,-1,96,98,101,-1,31,29,30,-1,30,32,31,-1,55,101,98,-1,98,51,55,-1,31,16,13,-1,13,29,31,-1,102,103,100,-1,100,99,102,-1,102,99,101,-1,101,104,102,-1,33,34,31,-1,31,32,33,-1,59,104,101,-1,101,55,59,-1,19,16,31,-1,31,34,19,-1,106,107,105,-1,105,93,106,-1,109,110,95,-1,95,108,109,-1,107,109,108,-1,108,105,107,-1,111,112,91,-1,91,90,111,-1,112,106,93,-1,93,91,112,-1,110,111,90,-1,90,95,110,-1,113,95,114,-1,95,113,108,-1,115,108,113,-1,108,115,105,-1,116,100,117,-1,116,97,100,-1,100,118,117,-1,100,103,118,-1,35,27,28,-1,119,94,115,-1,119,120,94,-1,76,45,94,-1,94,120,76,-1,115,92,93,-1,93,105,115,-1,115,94,92,-1,95,116,114,-1,95,97,116,-1,35,28,9,-1,21,35,9,-1,121,107,106,-1,106,122,121,-1,109,107,121,-1,112,122,106,-1,121,122,112,-1,112,109,121,-1,109,112,111,-1,111,110,109,-1,123,103,102,-1,102,124,123,-1,124,102,104,-1,104,125,124,-1,126,127,103,-1,103,123,126,-1,125,104,59,-1,59,84,125,-1,85,86,127,-1,127,126,85,-1,124,87,123,-1,125,87,124,-1,123,87,126,-1,84,87,125,-1,126,87,85,-1,120,119,115,-1,120,115,94,-1,74,75,46,-1,74,46,70,-1,75,76,45,-1,75,45,46,-1,76,120,94,-1,76,94,45,-1,132,131,136,-1,136,137,132,-1,131,133,138,-1,138,136,131,-1,133,134,139,-1,139,138,133,-1,134,135,140,-1,140,139,134,-1,141,142,143,-1,143,144,141,-1,135,141,144,-1,144,140,135,-1,149,145,132,-1,132,137,149,-1,150,146,145,-1,145,149,150,-1,151,147,146,-1,146,150,151,-1,152,148,147,-1,147,151,152,-1,143,142,153,-1,153,154,143,-1,154,153,148,-1,148,152,154,-1]
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
HAnimJoint201.center = [0,65.510002,-1.446]
HAnimJoint201.ulimit = [0,0,0]
HAnimJoint201.llimit = [0,0,0]
HAnimSegment202 = x3d.HAnimSegment()
HAnimSegment202.name = "skull"
HAnimSegment202.DEF = "hanim_skull"
Transform203 = x3d.Transform()
Transform203.translation = [0,65.510002,-1.446]
Shape204 = x3d.Shape()
Appearance205 = x3d.Appearance()
Material206 = x3d.Material()
Material206.diffuseColor = [0.588,0.588,0.588]

Appearance205.material = Material206
ImageTexture207 = x3d.ImageTexture()
ImageTexture207.USE = "ChulTextureAtlas"

Appearance205.texture = ImageTexture207

Shape204.appearance = Appearance205
IndexedFaceSet208 = x3d.IndexedFaceSet()
IndexedFaceSet208.coordIndex = [58,44,47,-1,47,49,58,-1,49,60,59,-1,59,1,49,-1,56,48,47,-1,47,44,56,-1,50,51,59,-1,59,60,50,-1,173,168,58,-1,58,49,173,-1,171,173,49,-1,49,1,171,-1,14,12,18,-1,18,15,14,-1,162,160,14,-1,14,15,162,-1,16,57,33,-1,21,18,12,-1,18,79,19,-1,80,20,19,-1,11,10,79,-1,18,21,79,-1,11,79,21,-1,21,12,78,-1,11,21,22,-1,321,345,320,-1,322,323,346,-1,80,25,24,-1,24,20,80,-1,26,38,24,-1,23,13,38,-1,20,77,18,-1,18,19,20,-1,38,29,30,-1,30,23,38,-1,27,30,29,-1,27,28,30,-1,30,28,23,-1,33,31,16,-1,31,37,16,-1,28,34,23,-1,17,35,36,-1,36,28,17,-1,33,36,35,-1,17,32,35,-1,32,33,35,-1,33,34,36,-1,36,34,28,-1,10,19,79,-1,4,40,37,-1,40,42,41,-1,40,41,37,-1,40,4,42,-1,56,43,4,-1,4,46,56,-1,45,43,56,-1,56,44,45,-1,43,45,4,-1,48,56,46,-1,46,3,48,-1,50,60,3,-1,51,50,3,-1,3,2,51,-1,58,168,52,-1,52,168,170,-1,61,52,170,-1,4,45,52,-1,52,61,4,-1,52,45,44,-1,44,58,52,-1,61,170,53,-1,170,165,39,-1,39,53,170,-1,4,61,53,-1,53,42,4,-1,53,39,41,-1,41,42,53,-1,165,57,39,-1,13,23,54,-1,16,37,57,-1,41,39,57,-1,37,41,57,-1,57,165,166,-1,54,166,13,-1,33,57,34,-1,34,57,54,-1,34,54,23,-1,166,162,55,-1,55,162,15,-1,77,55,15,-1,15,18,77,-1,166,77,13,-1,77,166,55,-1,13,77,24,-1,24,38,13,-1,20,24,77,-1,54,57,166,-1,47,60,49,-1,48,3,47,-1,3,60,47,-1,3,63,2,-1,72,62,63,-1,3,65,63,-1,3,46,64,-1,64,66,3,-1,6,66,64,-1,3,66,65,-1,6,73,8,-1,8,73,67,-1,6,75,73,-1,5,71,73,-1,73,75,5,-1,6,70,75,-1,64,46,69,-1,75,70,69,-1,75,69,344,-1,2,63,62,-1,8,66,6,-1,63,8,72,-1,9,74,71,-1,68,74,9,-1,74,8,67,-1,68,72,74,-1,72,8,74,-1,67,71,74,-1,67,73,71,-1,65,8,63,-1,65,66,8,-1,70,6,64,-1,70,64,69,-1,4,0,344,-1,69,46,4,-1,69,4,344,-1,76,344,0,-1,5,76,0,-1,5,75,76,-1,75,344,76,-1,133,125,123,-1,123,120,133,-1,125,1,59,-1,59,134,125,-1,131,120,123,-1,123,124,131,-1,126,134,59,-1,59,51,126,-1,172,125,133,-1,133,167,172,-1,171,1,125,-1,125,172,171,-1,14,91,94,-1,94,12,14,-1,161,91,14,-1,14,160,161,-1,109,132,92,-1,12,94,97,-1,95,149,94,-1,95,96,150,-1,149,88,89,-1,149,97,94,-1,97,149,89,-1,78,12,97,-1,98,97,89,-1,325,348,324,-1,354,326,327,-1,150,96,100,-1,100,101,150,-1,100,114,102,-1,114,90,99,-1,96,95,94,-1,94,148,96,-1,114,99,106,-1,106,105,114,-1,105,106,103,-1,106,104,103,-1,99,104,106,-1,92,107,109,-1,92,113,107,-1,99,110,104,-1,93,104,112,-1,112,111,93,-1,111,112,109,-1,111,108,93,-1,111,109,108,-1,112,110,109,-1,104,110,112,-1,149,95,88,-1,113,116,83,-1,117,118,116,-1,113,117,116,-1,118,83,116,-1,131,122,83,-1,83,119,131,-1,121,120,131,-1,131,119,121,-1,83,121,119,-1,124,82,122,-1,122,131,124,-1,82,134,126,-1,51,2,82,-1,82,126,51,-1,127,167,133,-1,169,167,127,-1,169,127,135,-1,83,135,127,-1,127,121,83,-1,127,133,120,-1,120,121,127,-1,128,169,135,-1,169,128,115,-1,115,163,169,-1,83,118,128,-1,128,135,83,-1,128,118,117,-1,117,115,128,-1,115,132,163,-1,129,99,90,-1,132,113,92,-1,132,115,117,-1,132,117,113,-1,164,163,132,-1,90,164,129,-1,110,132,109,-1,129,132,110,-1,99,129,110,-1,130,161,164,-1,91,161,130,-1,148,94,91,-1,91,130,148,-1,90,148,164,-1,130,164,148,-1,90,114,100,-1,100,148,90,-1,148,100,96,-1,164,132,129,-1,125,134,123,-1,123,82,124,-1,123,134,82,-1,2,136,82,-1,136,62,72,-1,136,138,82,-1,82,139,137,-1,137,122,82,-1,137,139,85,-1,138,139,82,-1,87,144,85,-1,140,144,87,-1,144,146,85,-1,84,146,144,-1,144,143,84,-1,146,142,85,-1,141,122,137,-1,141,142,146,-1,347,141,146,-1,62,136,2,-1,85,139,87,-1,72,87,136,-1,143,145,9,-1,9,145,68,-1,145,140,87,-1,68,145,72,-1,72,145,87,-1,145,143,140,-1,143,144,140,-1,136,87,138,-1,87,139,138,-1,137,85,142,-1,141,137,142,-1,347,81,83,-1,83,122,141,-1,347,83,141,-1,81,347,147,-1,81,147,84,-1,147,146,84,-1,147,347,146,-1,162,166,152,-1,151,160,162,-1,162,152,151,-1,152,166,165,-1,165,154,152,-1,154,165,170,-1,170,156,154,-1,152,154,155,-1,155,151,152,-1,156,153,155,-1,155,154,156,-1,173,156,170,-1,170,168,173,-1,171,153,156,-1,156,173,171,-1,157,164,161,-1,151,157,161,-1,161,160,151,-1,157,158,163,-1,163,164,157,-1,158,159,169,-1,169,163,158,-1,157,151,155,-1,155,158,157,-1,159,158,155,-1,155,153,159,-1,172,167,169,-1,169,159,172,-1,171,172,159,-1,159,153,171,-1,355,237,223,-1,174,236,237,-1,236,174,175,-1,179,238,176,-1,179,176,177,-1,179,177,178,-1,178,174,179,-1,174,178,175,-1,180,226,236,-1,238,180,236,-1,180,230,226,-1,237,236,223,-1,223,236,218,-1,225,355,223,-1,223,224,225,-1,328,329,239,-1,330,331,350,-1,228,227,219,-1,219,222,228,-1,236,226,218,-1,174,237,0,-1,0,237,355,-1,0,179,174,-1,318,355,225,-1,220,228,222,-1,221,228,220,-1,5,0,355,-1,218,182,223,-1,183,223,182,-1,181,183,185,-1,181,185,242,-1,213,212,244,-1,244,246,213,-1,213,246,245,-1,245,214,213,-1,245,247,184,-1,184,214,245,-1,214,184,206,-1,206,207,214,-1,217,319,225,-1,225,224,217,-1,183,181,217,-1,217,224,183,-1,224,223,183,-1,226,209,218,-1,218,209,184,-1,182,185,183,-1,218,184,182,-1,207,208,232,-1,232,214,207,-1,232,215,214,-1,209,206,184,-1,186,192,190,-1,190,188,186,-1,197,192,208,-1,208,207,197,-1,190,222,219,-1,219,188,190,-1,194,195,190,-1,226,189,209,-1,187,189,226,-1,192,186,208,-1,191,216,205,-1,196,205,216,-1,195,196,216,-1,196,195,194,-1,209,189,198,-1,199,197,207,-1,207,206,199,-1,233,234,197,-1,197,199,233,-1,209,198,199,-1,199,206,209,-1,233,199,198,-1,198,200,233,-1,248,194,202,-1,201,205,250,-1,248,249,196,-1,196,194,248,-1,196,249,250,-1,250,205,196,-1,234,203,197,-1,203,192,197,-1,194,190,202,-1,200,198,189,-1,189,204,200,-1,202,190,192,-1,202,192,203,-1,205,210,191,-1,210,205,201,-1,220,222,193,-1,204,189,187,-1,187,210,204,-1,210,201,204,-1,210,187,191,-1,195,211,190,-1,195,193,211,-1,193,222,211,-1,211,222,190,-1,215,212,213,-1,213,214,215,-1,230,187,226,-1,230,191,187,-1,229,221,230,-1,229,228,221,-1,9,355,318,-1,5,355,71,-1,71,355,9,-1,231,247,185,-1,182,231,185,-1,184,231,182,-1,184,247,231,-1,238,230,180,-1,230,221,191,-1,221,235,191,-1,191,235,216,-1,221,220,235,-1,193,235,220,-1,216,235,193,-1,193,195,216,-1,250,249,233,-1,203,234,248,-1,234,233,249,-1,250,233,200,-1,249,248,234,-1,243,241,240,-1,241,243,247,-1,204,201,250,-1,200,204,250,-1,203,248,202,-1,247,243,242,-1,247,242,185,-1,332,333,349,-1,334,335,7,-1,292,304,353,-1,304,303,251,-1,252,251,303,-1,253,305,256,-1,254,253,256,-1,256,251,255,-1,255,254,256,-1,252,255,251,-1,303,295,257,-1,303,257,305,-1,295,298,257,-1,292,303,304,-1,288,303,292,-1,294,352,292,-1,292,353,294,-1,336,337,293,-1,306,338,339,-1,296,291,219,-1,219,227,296,-1,288,295,303,-1,81,304,251,-1,353,304,81,-1,251,256,81,-1,294,353,317,-1,291,296,289,-1,289,296,290,-1,353,81,84,-1,292,258,288,-1,258,292,259,-1,261,259,181,-1,242,261,181,-1,285,309,244,-1,244,212,285,-1,285,286,308,-1,308,309,285,-1,308,286,260,-1,260,310,308,-1,286,281,280,-1,280,260,286,-1,217,352,294,-1,294,319,217,-1,259,352,217,-1,217,181,259,-1,259,292,352,-1,288,282,295,-1,260,282,288,-1,259,261,258,-1,258,260,288,-1,281,286,232,-1,232,208,281,-1,286,215,232,-1,260,280,282,-1,186,188,264,-1,264,266,186,-1,271,281,208,-1,208,266,271,-1,264,188,219,-1,219,291,264,-1,264,269,268,-1,282,263,295,-1,295,263,262,-1,208,186,266,-1,279,287,265,-1,287,279,270,-1,287,270,269,-1,268,269,270,-1,272,263,282,-1,273,280,281,-1,281,271,273,-1,300,273,271,-1,271,301,300,-1,282,280,273,-1,273,272,282,-1,300,274,272,-1,272,273,300,-1,276,268,311,-1,313,279,275,-1,311,268,270,-1,270,312,311,-1,270,279,313,-1,313,312,270,-1,271,277,301,-1,271,266,277,-1,276,264,268,-1,274,278,263,-1,263,272,274,-1,266,264,276,-1,277,266,276,-1,265,283,279,-1,275,279,283,-1,267,291,289,-1,278,283,262,-1,262,263,278,-1,278,275,283,-1,265,262,283,-1,264,284,269,-1,284,267,269,-1,284,291,267,-1,264,291,284,-1,285,212,215,-1,215,286,285,-1,295,262,298,-1,262,265,298,-1,298,290,297,-1,290,296,297,-1,317,353,9,-1,143,353,84,-1,9,353,143,-1,261,310,299,-1,261,299,258,-1,258,299,260,-1,299,310,260,-1,257,298,305,-1,265,290,298,-1,265,302,290,-1,287,302,265,-1,302,289,290,-1,289,302,267,-1,287,269,267,-1,267,302,287,-1,300,312,313,-1,311,301,277,-1,312,300,301,-1,274,300,313,-1,301,311,312,-1,240,307,243,-1,310,243,307,-1,313,275,278,-1,313,278,274,-1,276,311,277,-1,242,243,310,-1,261,242,310,-1,351,340,341,-1,86,342,343,-1,244,314,315,-1,315,246,244,-1,246,315,247,-1,247,245,246,-1,244,309,316,-1,316,314,244,-1,309,308,310,-1,310,316,309,-1,175,176,238,-1,238,236,175,-1,177,176,175,-1,175,178,177,-1,252,303,305,-1,305,253,252,-1,254,255,252,-1,252,253,254,-1,318,225,319,-1,319,9,318,-1,317,9,319,-1,319,294,317,-1]
IndexedFaceSet208.creaseAngle = 1.57
IndexedFaceSet208.texCoordIndex = [0,3,2,-1,2,1,0,-1,1,6,5,-1,5,4,1,-1,7,8,2,-1,2,3,7,-1,9,10,5,-1,5,6,9,-1,11,12,0,-1,0,1,11,-1,13,11,1,-1,1,4,13,-1,14,17,16,-1,16,15,14,-1,18,19,14,-1,14,15,18,-1,22,21,20,-1,23,16,17,-1,16,25,24,-1,27,26,24,-1,29,28,25,-1,16,23,25,-1,29,25,23,-1,31,17,30,-1,29,23,32,-1,33,32,31,-1,33,31,30,-1,27,35,34,-1,34,26,27,-1,37,36,34,-1,39,38,36,-1,26,40,16,-1,16,24,26,-1,36,42,41,-1,41,39,36,-1,43,41,42,-1,43,44,41,-1,41,44,39,-1,20,45,22,-1,45,46,22,-1,44,47,39,-1,48,50,49,-1,49,44,48,-1,20,49,50,-1,48,51,50,-1,51,20,50,-1,20,47,49,-1,49,47,44,-1,28,24,25,-1,53,52,46,-1,52,55,54,-1,52,54,46,-1,52,53,55,-1,7,57,53,-1,53,56,7,-1,58,57,7,-1,7,59,58,-1,57,58,53,-1,8,7,56,-1,56,60,8,-1,9,6,60,-1,10,9,60,-1,60,61,10,-1,0,12,62,-1,62,12,63,-1,64,62,63,-1,53,58,62,-1,62,64,53,-1,62,58,59,-1,59,0,62,-1,64,63,65,-1,63,67,66,-1,66,65,63,-1,53,64,65,-1,65,55,53,-1,65,66,54,-1,54,55,65,-1,67,21,66,-1,38,39,68,-1,22,46,21,-1,54,66,21,-1,46,54,21,-1,21,67,69,-1,68,69,38,-1,20,21,47,-1,47,21,68,-1,47,68,39,-1,69,18,70,-1,70,18,15,-1,40,70,15,-1,15,16,40,-1,69,71,38,-1,71,69,70,-1,38,71,34,-1,34,36,38,-1,26,34,71,-1,68,21,69,-1,2,6,1,-1,8,60,2,-1,60,6,2,-1,74,73,72,-1,77,76,75,-1,74,78,73,-1,74,81,80,-1,80,79,74,-1,82,79,80,-1,74,79,78,-1,82,84,83,-1,83,84,85,-1,82,86,84,-1,87,90,89,-1,89,88,87,-1,92,91,88,-1,80,81,93,-1,88,91,94,-1,86,93,95,-1,72,73,96,-1,83,79,82,-1,73,83,97,-1,100,99,98,-1,103,102,101,-1,99,83,85,-1,104,97,99,-1,97,83,99,-1,105,90,102,-1,105,89,90,-1,107,106,75,-1,107,108,106,-1,109,82,80,-1,109,80,93,-1,112,111,110,-1,93,81,113,-1,93,113,95,-1,114,110,111,-1,115,114,111,-1,87,86,116,-1,86,95,116,-1,117,120,119,-1,119,118,117,-1,120,123,122,-1,122,121,120,-1,124,118,119,-1,119,125,124,-1,126,121,122,-1,122,127,126,-1,128,120,117,-1,117,129,128,-1,130,123,120,-1,120,128,130,-1,14,132,131,-1,131,17,14,-1,133,132,14,-1,14,19,133,-1,136,135,134,-1,17,131,137,-1,139,138,131,-1,139,141,140,-1,138,143,142,-1,138,137,131,-1,137,138,142,-1,30,17,144,-1,145,137,142,-1,144,145,146,-1,30,144,146,-1,140,141,148,-1,148,147,140,-1,148,150,149,-1,150,152,151,-1,141,139,131,-1,131,153,141,-1,150,151,155,-1,155,154,150,-1,154,155,156,-1,155,157,156,-1,151,157,155,-1,134,158,136,-1,134,159,158,-1,151,160,157,-1,161,157,163,-1,163,162,161,-1,162,163,136,-1,162,164,161,-1,162,136,164,-1,163,160,136,-1,157,160,163,-1,138,139,143,-1,159,166,165,-1,168,167,166,-1,159,168,166,-1,167,165,166,-1,124,170,165,-1,165,169,124,-1,171,172,124,-1,124,169,171,-1,165,171,169,-1,125,173,170,-1,170,124,125,-1,173,121,126,-1,127,174,173,-1,173,126,127,-1,175,129,117,-1,176,129,175,-1,176,175,177,-1,165,177,175,-1,175,171,165,-1,175,117,172,-1,172,171,175,-1,178,176,177,-1,176,178,180,-1,180,179,176,-1,165,167,178,-1,178,177,165,-1,178,167,168,-1,168,180,178,-1,180,135,179,-1,181,151,152,-1,135,159,134,-1,135,180,168,-1,135,168,159,-1,182,179,135,-1,152,182,181,-1,160,135,136,-1,181,135,160,-1,151,181,160,-1,183,133,182,-1,132,133,183,-1,153,131,132,-1,132,183,153,-1,152,184,182,-1,183,182,184,-1,152,150,148,-1,148,184,152,-1,184,148,141,-1,182,135,181,-1,120,121,119,-1,119,173,125,-1,119,121,173,-1,72,186,185,-1,187,76,77,-1,186,188,185,-1,185,191,190,-1,190,189,185,-1,190,191,192,-1,188,191,185,-1,194,193,192,-1,195,193,194,-1,193,196,192,-1,197,200,199,-1,199,198,197,-1,200,202,201,-1,203,189,190,-1,204,202,200,-1,205,203,196,-1,96,186,72,-1,192,191,194,-1,97,194,186,-1,207,206,100,-1,101,208,103,-1,206,195,194,-1,104,206,97,-1,97,206,194,-1,208,198,209,-1,198,199,209,-1,187,211,210,-1,211,212,210,-1,190,192,213,-1,203,190,213,-1,216,215,214,-1,217,189,203,-1,205,217,203,-1,215,216,218,-1,215,218,219,-1,220,196,197,-1,220,205,196,-1,18,69,221,-1,222,19,18,-1,18,221,222,-1,221,69,67,-1,67,223,221,-1,223,67,63,-1,63,224,223,-1,221,223,225,-1,225,222,221,-1,224,226,225,-1,225,223,224,-1,11,224,63,-1,63,12,11,-1,13,226,224,-1,224,11,13,-1,227,182,133,-1,222,227,133,-1,133,19,222,-1,227,228,179,-1,179,182,227,-1,228,229,176,-1,176,179,228,-1,227,222,225,-1,225,228,227,-1,229,228,225,-1,225,230,229,-1,128,129,176,-1,176,229,128,-1,130,128,229,-1,229,230,130,-1,233,232,231,-1,235,234,232,-1,234,235,236,-1,239,238,237,-1,239,237,240,-1,239,240,241,-1,241,235,239,-1,235,241,236,-1,243,242,234,-1,238,243,234,-1,243,244,242,-1,232,234,231,-1,231,234,245,-1,246,233,231,-1,231,247,246,-1,247,246,233,-1,231,247,233,-1,248,251,250,-1,250,249,248,-1,234,242,245,-1,235,232,252,-1,252,232,233,-1,252,239,235,-1,253,233,246,-1,254,248,249,-1,255,248,254,-1,256,252,233,-1,245,257,231,-1,258,231,257,-1,261,260,259,-1,261,259,262,-1,263,266,265,-1,265,264,263,-1,263,264,268,-1,268,267,263,-1,268,270,269,-1,269,267,268,-1,267,269,272,-1,272,271,267,-1,273,274,246,-1,246,247,273,-1,258,275,273,-1,273,247,258,-1,247,231,258,-1,278,277,276,-1,276,277,269,-1,279,259,260,-1,276,269,279,-1,271,281,280,-1,280,267,271,-1,280,282,267,-1,277,272,269,-1,284,287,286,-1,286,285,284,-1,288,287,281,-1,281,271,288,-1,286,249,250,-1,250,285,286,-1,290,289,286,-1,278,291,277,-1,292,291,278,-1,287,284,283,-1,295,294,293,-1,296,293,294,-1,289,296,294,-1,296,289,290,-1,277,291,297,-1,298,288,271,-1,271,272,298,-1,299,300,288,-1,288,298,299,-1,277,297,298,-1,298,272,277,-1,299,298,297,-1,297,301,299,-1,303,290,302,-1,305,293,304,-1,303,306,296,-1,296,290,303,-1,296,306,304,-1,304,293,296,-1,300,307,288,-1,307,287,288,-1,290,286,302,-1,301,297,291,-1,291,308,301,-1,302,286,287,-1,309,287,307,-1,293,310,295,-1,310,293,305,-1,254,249,311,-1,308,291,292,-1,292,310,308,-1,310,305,308,-1,310,292,295,-1,289,312,286,-1,289,311,312,-1,311,249,312,-1,312,249,286,-1,282,266,263,-1,263,267,282,-1,313,292,278,-1,313,295,292,-1,314,255,313,-1,314,248,255,-1,315,233,253,-1,256,233,316,-1,316,233,315,-1,317,270,259,-1,279,317,259,-1,269,317,279,-1,269,270,317,-1,238,244,243,-1,313,255,295,-1,255,318,295,-1,295,318,294,-1,255,254,318,-1,311,318,254,-1,294,318,311,-1,311,289,294,-1,304,306,299,-1,307,300,303,-1,300,299,306,-1,304,299,301,-1,306,303,300,-1,321,320,319,-1,320,321,270,-1,308,305,304,-1,301,308,304,-1,307,303,309,-1,270,321,262,-1,270,262,259,-1,252,322,239,-1,252,256,322,-1,231,232,233,-1,232,234,235,-1,236,235,234,-1,237,238,239,-1,240,237,239,-1,239,235,241,-1,241,240,239,-1,236,241,235,-1,234,242,243,-1,234,243,238,-1,242,244,243,-1,231,234,232,-1,245,234,231,-1,246,247,231,-1,231,233,246,-1,233,246,247,-1,233,247,231,-1,323,324,250,-1,250,251,323,-1,245,242,234,-1,252,232,235,-1,233,232,252,-1,235,239,252,-1,246,233,253,-1,324,323,325,-1,325,323,326,-1,233,252,256,-1,231,257,245,-1,257,231,258,-1,329,328,327,-1,330,329,327,-1,331,332,265,-1,265,266,331,-1,331,334,333,-1,333,332,331,-1,333,334,336,-1,336,335,333,-1,334,338,337,-1,337,336,334,-1,273,247,246,-1,246,274,273,-1,258,247,273,-1,273,275,258,-1,258,231,247,-1,341,340,339,-1,336,340,341,-1,328,329,342,-1,342,336,341,-1,338,334,280,-1,280,343,338,-1,334,282,280,-1,336,337,340,-1,284,285,345,-1,345,344,284,-1,346,338,343,-1,343,344,346,-1,345,285,250,-1,250,324,345,-1,345,348,347,-1,340,349,339,-1,339,349,350,-1,283,284,344,-1,353,352,351,-1,352,353,354,-1,352,354,348,-1,347,348,354,-1,355,349,340,-1,356,337,338,-1,338,346,356,-1,357,356,346,-1,346,358,357,-1,340,337,356,-1,356,355,340,-1,357,359,355,-1,355,356,357,-1,361,347,360,-1,363,353,362,-1,360,347,354,-1,354,364,360,-1,354,353,363,-1,363,364,354,-1,346,365,358,-1,346,344,365,-1,361,345,347,-1,359,366,349,-1,349,355,359,-1,344,345,361,-1,365,344,367,-1,351,368,353,-1,362,353,368,-1,369,324,325,-1,366,368,350,-1,350,349,366,-1,366,362,368,-1,351,350,368,-1,345,370,348,-1,370,369,348,-1,370,324,369,-1,345,324,370,-1,331,266,282,-1,282,334,331,-1,339,350,371,-1,350,351,371,-1,371,326,372,-1,326,323,372,-1,253,233,315,-1,316,233,256,-1,315,233,316,-1,329,335,373,-1,329,373,342,-1,342,373,336,-1,373,335,336,-1,243,244,238,-1,351,326,371,-1,351,374,326,-1,352,374,351,-1,374,325,326,-1,325,374,369,-1,352,348,369,-1,369,374,352,-1,357,364,363,-1,360,358,365,-1,364,357,358,-1,359,357,363,-1,358,360,364,-1,319,376,375,-1,335,375,376,-1,363,362,366,-1,363,366,359,-1,367,360,365,-1,330,375,335,-1,329,330,335,-1,239,322,252,-1,322,256,252,-1,265,378,377,-1,377,264,265,-1,264,377,270,-1,270,268,264,-1,265,332,379,-1,379,378,265,-1,332,333,335,-1,335,379,332,-1,380,383,382,-1,382,381,380,-1,384,383,380,-1,380,385,384,-1,380,381,382,-1,382,383,380,-1,384,385,380,-1,380,383,384,-1,253,246,274,-1,274,100,253,-1,253,100,274,-1,274,246,253,-1]
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
f = open("././KoreanCharacter02Chul_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
