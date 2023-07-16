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
meta3.content = "KoreanCharacterMotionAnnexD01Jin.x3d"

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
meta8.content = "7 January 2023"

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
meta13.name = "specificationSection"
meta13.content = "HAnim 2.0 Part 2: Humanoid animation (HAnim) motion data animation, Annex D (informative) Examples of HAnim motion data animation using a Motion object"

head1.children.append(meta13)
meta14 = x3d.meta()
meta14.name = "specificationUrl"
meta14.content = "https://www.web3d.org/documents/specifications/19774/V2.0/MotionDataAnimation/ExampleMocapAnimationMotionObject.html"

head1.children.append(meta14)
meta15 = x3d.meta()
meta15.name = "identifier"
meta15.content = "https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Specifications/KoreanCharacterMotionAnnexD01Jin.x3d"

head1.children.append(meta15)
meta16 = x3d.meta()
meta16.name = "generator"
meta16.content = "3DS MAX, http://www.autodesk.com/products/autodesk-3ds-max/overview"

head1.children.append(meta16)
meta17 = x3d.meta()
meta17.name = "generator"
meta17.content = "Suwon HAnim Converter"

head1.children.append(meta17)
meta18 = x3d.meta()
meta18.name = "generator"
meta18.content = "Gnu Image Manipulation Program, http://www.gimp.org"

head1.children.append(meta18)
meta19 = x3d.meta()
meta19.name = "generator"
meta19.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"

head1.children.append(meta19)
meta20 = x3d.meta()
meta20.name = "license"
meta20.content = "../license.html"

head1.children.append(meta20)

X3D0.head = head1
Scene21 = x3d.Scene()
WorldInfo22 = x3d.WorldInfo()
WorldInfo22.title = "KoreanCharacterMotionAnnexD01Jin.x3d"

Scene21.children.append(WorldInfo22)
NavigationInfo23 = x3d.NavigationInfo()
NavigationInfo23.speed = 1.5

Scene21.children.append(NavigationInfo23)
Viewpoint24 = x3d.Viewpoint()
Viewpoint24.centerOfRotation = [0,1,0]
Viewpoint24.description = "AnnexD01Jin"
Viewpoint24.position = [0,1,3]

Scene21.children.append(Viewpoint24)
HAnimHumanoid25 = x3d.HAnimHumanoid()
HAnimHumanoid25.name = "AnnexD01Jin"
HAnimHumanoid25.DEF = "hanim_AnnexD01Jin"
HAnimHumanoid25.scale = [0.0225,0.0225,0.0225]
HAnimHumanoid25.version = "2.0"
#original HAnimHumanoid info='\"humanoidVersion=2.0\"'
MetadataSet26 = x3d.MetadataSet()
MetadataSet26.name = "HAnimHumanoid.info"
MetadataSet26.reference = "https://www.web3d.org/documents/specifications/19774/V2.0/Architecture/ObjectInterfaces.html#Humanoid"
MetadataString27 = x3d.MetadataString()
MetadataString27.name = "humanoidVersion"
MetadataString27.value = ["2.0"]

if MetadataSet26.value is None:
    MetadataSet26.value = []
MetadataSet26.value.append(MetadataString27)

HAnimHumanoid25.metadata = MetadataSet26
HAnimJoint28 = x3d.HAnimJoint()
HAnimJoint28.name = "humanoid_root"
HAnimJoint28.DEF = "hanim_humanoid_root"
HAnimJoint28.center = [0,30.53,-0.7076]
HAnimJoint28.ulimit = [0,0,0]
HAnimJoint28.llimit = [0,0,0]
HAnimSegment29 = x3d.HAnimSegment()
HAnimSegment29.name = "sacrum"
HAnimSegment29.DEF = "hanim_sacrum"
Transform30 = x3d.Transform()
Transform30.translation = [0,30.53,-0.7076]
Shape31 = x3d.Shape()
Appearance32 = x3d.Appearance()
Material33 = x3d.Material()
Material33.diffuseColor = [0.588,0.588,0.588]

Appearance32.material = Material33
ImageTexture34 = x3d.ImageTexture()
ImageTexture34.DEF = "Annex01JinTextureAtlas"
ImageTexture34.url = ["Jin.png","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/HAnimSpecification/Jin.png"]

Appearance32.texture = ImageTexture34

Shape31.appearance = Appearance32
IndexedFaceSet35 = x3d.IndexedFaceSet()
IndexedFaceSet35.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,5,-1,0,5,6,-1,0,6,7,-1,0,7,8,-1,0,8,9,-1,0,9,10,-1,0,10,11,-1,0,11,12,-1,0,12,1,-1,14,2,1,-1,1,13,14,-1,15,3,2,-1,2,14,15,-1,16,4,3,-1,3,15,16,-1,17,5,4,-1,4,16,17,-1,18,6,5,-1,5,17,18,-1,19,7,6,-1,6,18,19,-1,20,8,7,-1,7,19,20,-1,21,9,8,-1,8,20,21,-1,22,10,9,-1,9,21,22,-1,23,11,10,-1,10,22,23,-1,24,12,11,-1,11,23,24,-1,13,1,12,-1,12,24,13,-1,26,14,13,-1,13,25,26,-1,27,15,14,-1,14,26,27,-1,28,16,15,-1,15,27,28,-1,29,17,16,-1,16,28,29,-1,30,18,17,-1,17,29,30,-1,31,19,18,-1,18,30,31,-1,32,20,19,-1,19,31,32,-1,33,21,20,-1,20,32,33,-1,34,22,21,-1,21,33,34,-1,35,23,22,-1,22,34,35,-1,36,24,23,-1,23,35,36,-1,25,13,24,-1,24,36,25,-1,38,26,25,-1,25,37,38,-1,39,27,26,-1,26,38,39,-1,40,28,27,-1,27,39,40,-1,41,29,28,-1,28,40,41,-1,42,30,29,-1,29,41,42,-1,43,31,30,-1,30,42,43,-1,44,32,31,-1,31,43,44,-1,45,33,32,-1,32,44,45,-1,46,34,33,-1,33,45,46,-1,47,35,34,-1,34,46,47,-1,48,36,35,-1,35,47,48,-1,37,25,36,-1,36,48,37,-1,50,38,37,-1,37,49,50,-1,51,39,38,-1,38,50,51,-1,52,40,39,-1,39,51,52,-1,53,41,40,-1,40,52,53,-1,54,42,41,-1,41,53,54,-1,55,43,42,-1,42,54,55,-1,56,44,43,-1,43,55,56,-1,57,45,44,-1,44,56,57,-1,58,46,45,-1,45,57,58,-1,59,47,46,-1,46,58,59,-1,60,48,47,-1,47,59,60,-1,49,37,48,-1,48,60,49,-1,61,50,49,-1,61,51,50,-1,61,52,51,-1,61,53,52,-1,61,54,53,-1,61,55,54,-1,61,56,55,-1,61,57,56,-1,61,58,57,-1,61,59,58,-1,61,60,59,-1,61,49,60,-1]
IndexedFaceSet35.creaseAngle = 3.14159
IndexedFaceSet35.texCoordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,5,-1,0,5,6,-1,0,6,7,-1,0,7,8,-1,0,8,9,-1,0,9,10,-1,0,10,11,-1,0,11,12,-1,0,12,1,-1,14,2,1,-1,1,13,14,-1,15,3,2,-1,2,14,15,-1,16,4,3,-1,3,15,16,-1,17,5,4,-1,4,16,17,-1,18,6,5,-1,5,17,18,-1,19,7,6,-1,6,18,19,-1,20,8,7,-1,7,19,20,-1,21,9,8,-1,8,20,21,-1,22,10,9,-1,9,21,22,-1,23,11,10,-1,10,22,23,-1,24,12,11,-1,11,23,24,-1,13,1,12,-1,12,24,13,-1,26,14,13,-1,13,25,26,-1,27,15,14,-1,14,26,27,-1,28,16,15,-1,15,27,28,-1,29,17,16,-1,16,28,29,-1,30,18,17,-1,17,29,30,-1,31,19,18,-1,18,30,31,-1,32,20,19,-1,19,31,32,-1,33,21,20,-1,20,32,33,-1,34,22,21,-1,21,33,34,-1,35,23,22,-1,22,34,35,-1,36,24,23,-1,23,35,36,-1,25,13,24,-1,24,36,25,-1,38,26,25,-1,25,37,38,-1,39,27,26,-1,26,38,39,-1,40,28,27,-1,27,39,40,-1,41,29,28,-1,28,40,41,-1,42,30,29,-1,29,41,42,-1,43,31,30,-1,30,42,43,-1,44,32,31,-1,31,43,44,-1,45,33,32,-1,32,44,45,-1,46,34,33,-1,33,45,46,-1,47,35,34,-1,34,46,47,-1,48,36,35,-1,35,47,48,-1,37,25,36,-1,36,48,37,-1,50,38,37,-1,37,49,50,-1,51,39,38,-1,38,50,51,-1,52,40,39,-1,39,51,52,-1,53,41,40,-1,40,52,53,-1,54,42,41,-1,41,53,54,-1,55,43,42,-1,42,54,55,-1,56,44,43,-1,43,55,56,-1,57,45,44,-1,44,56,57,-1,58,46,45,-1,45,57,58,-1,59,47,46,-1,46,58,59,-1,60,48,47,-1,47,59,60,-1,49,37,48,-1,48,60,49,-1,61,50,49,-1,61,51,50,-1,61,52,51,-1,61,53,52,-1,61,54,53,-1,61,55,54,-1,61,56,55,-1,61,57,56,-1,61,58,57,-1,61,59,58,-1,61,60,59,-1,61,49,60,-1]
Coordinate36 = x3d.Coordinate()

IndexedFaceSet35.coord = Coordinate36
TextureCoordinate37 = x3d.TextureCoordinate()

IndexedFaceSet35.texCoord = TextureCoordinate37

Shape31.geometry = IndexedFaceSet35

Transform30.children.append(Shape31)

HAnimSegment29.children.append(Transform30)

HAnimJoint28.children.append(HAnimSegment29)
HAnimJoint38 = x3d.HAnimJoint()
HAnimJoint38.name = "sacroiliac"
HAnimJoint38.DEF = "hanim_sacroiliac"
HAnimJoint38.center = [0,35.8,-0.7076]
HAnimJoint38.ulimit = [0,0,0]
HAnimJoint38.llimit = [0,0,0]
HAnimSegment39 = x3d.HAnimSegment()
HAnimSegment39.name = "pelvis"
HAnimSegment39.DEF = "hanim_pelvis"
Transform40 = x3d.Transform()
Transform40.translation = [0,35.8,-0.7076]
Shape41 = x3d.Shape()
Appearance42 = x3d.Appearance()
Material43 = x3d.Material()
Material43.diffuseColor = [0.588,0.588,0.588]

Appearance42.material = Material43
ImageTexture44 = x3d.ImageTexture()
ImageTexture44.USE = "Annex01JinTextureAtlas"

Appearance42.texture = ImageTexture44

Shape41.appearance = Appearance42
IndexedFaceSet45 = x3d.IndexedFaceSet()
IndexedFaceSet45.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,5,-1,0,5,6,-1,0,6,7,-1,0,7,8,-1,0,8,9,-1,0,9,10,-1,0,10,11,-1,0,11,12,-1,0,12,1,-1,14,2,1,-1,1,13,14,-1,15,3,2,-1,2,14,15,-1,16,4,3,-1,3,15,16,-1,17,5,4,-1,4,16,17,-1,18,6,5,-1,5,17,18,-1,19,7,6,-1,6,18,19,-1,20,8,7,-1,7,19,20,-1,21,9,8,-1,8,20,21,-1,22,10,9,-1,9,21,22,-1,23,11,10,-1,10,22,23,-1,24,12,11,-1,11,23,24,-1,13,1,12,-1,12,24,13,-1,26,14,13,-1,13,25,26,-1,27,15,14,-1,14,26,27,-1,28,16,15,-1,15,27,28,-1,29,17,16,-1,16,28,29,-1,30,18,17,-1,17,29,30,-1,31,19,18,-1,18,30,31,-1,32,20,19,-1,19,31,32,-1,33,21,20,-1,20,32,33,-1,34,22,21,-1,21,33,34,-1,35,23,22,-1,22,34,35,-1,36,24,23,-1,23,35,36,-1,25,13,24,-1,24,36,25,-1,38,26,25,-1,25,37,38,-1,39,27,26,-1,26,38,39,-1,40,28,27,-1,27,39,40,-1,41,29,28,-1,28,40,41,-1,42,30,29,-1,29,41,42,-1,43,31,30,-1,30,42,43,-1,44,32,31,-1,31,43,44,-1,45,33,32,-1,32,44,45,-1,46,34,33,-1,33,45,46,-1,47,35,34,-1,34,46,47,-1,48,36,35,-1,35,47,48,-1,37,25,36,-1,36,48,37,-1,50,38,37,-1,37,49,50,-1,51,39,38,-1,38,50,51,-1,52,40,39,-1,39,51,52,-1,53,41,40,-1,40,52,53,-1,54,42,41,-1,41,53,54,-1,55,43,42,-1,42,54,55,-1,56,44,43,-1,43,55,56,-1,57,45,44,-1,44,56,57,-1,58,46,45,-1,45,57,58,-1,59,47,46,-1,46,58,59,-1,60,48,47,-1,47,59,60,-1,49,37,48,-1,48,60,49,-1,61,50,49,-1,61,51,50,-1,61,52,51,-1,61,53,52,-1,61,54,53,-1,61,55,54,-1,61,56,55,-1,61,57,56,-1,61,58,57,-1,61,59,58,-1,61,60,59,-1,61,49,60,-1]
IndexedFaceSet45.creaseAngle = 3.14159
IndexedFaceSet45.texCoordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,5,-1,0,5,6,-1,0,6,7,-1,0,7,8,-1,0,8,9,-1,0,9,10,-1,0,10,11,-1,0,11,12,-1,0,12,1,-1,14,2,1,-1,1,13,14,-1,15,3,2,-1,2,14,15,-1,16,4,3,-1,3,15,16,-1,17,5,4,-1,4,16,17,-1,18,6,5,-1,5,17,18,-1,19,7,6,-1,6,18,19,-1,20,8,7,-1,7,19,20,-1,21,9,8,-1,8,20,21,-1,22,10,9,-1,9,21,22,-1,23,11,10,-1,10,22,23,-1,24,12,11,-1,11,23,24,-1,13,1,12,-1,12,24,13,-1,26,14,13,-1,13,25,26,-1,27,15,14,-1,14,26,27,-1,28,16,15,-1,15,27,28,-1,29,17,16,-1,16,28,29,-1,30,18,17,-1,17,29,30,-1,31,19,18,-1,18,30,31,-1,32,20,19,-1,19,31,32,-1,33,21,20,-1,20,32,33,-1,34,22,21,-1,21,33,34,-1,35,23,22,-1,22,34,35,-1,36,24,23,-1,23,35,36,-1,25,13,24,-1,24,36,25,-1,38,26,25,-1,25,37,38,-1,39,27,26,-1,26,38,39,-1,40,28,27,-1,27,39,40,-1,41,29,28,-1,28,40,41,-1,42,30,29,-1,29,41,42,-1,43,31,30,-1,30,42,43,-1,44,32,31,-1,31,43,44,-1,45,33,32,-1,32,44,45,-1,46,34,33,-1,33,45,46,-1,47,35,34,-1,34,46,47,-1,48,36,35,-1,35,47,48,-1,37,25,36,-1,36,48,37,-1,50,38,37,-1,37,49,50,-1,51,39,38,-1,38,50,51,-1,52,40,39,-1,39,51,52,-1,53,41,40,-1,40,52,53,-1,54,42,41,-1,41,53,54,-1,55,43,42,-1,42,54,55,-1,56,44,43,-1,43,55,56,-1,57,45,44,-1,44,56,57,-1,58,46,45,-1,45,57,58,-1,59,47,46,-1,46,58,59,-1,60,48,47,-1,47,59,60,-1,49,37,48,-1,48,60,49,-1,61,50,49,-1,61,51,50,-1,61,52,51,-1,61,53,52,-1,61,54,53,-1,61,55,54,-1,61,56,55,-1,61,57,56,-1,61,58,57,-1,61,59,58,-1,61,60,59,-1,61,49,60,-1]
Coordinate46 = x3d.Coordinate()

IndexedFaceSet45.coord = Coordinate46
TextureCoordinate47 = x3d.TextureCoordinate()

IndexedFaceSet45.texCoord = TextureCoordinate47

Shape41.geometry = IndexedFaceSet45

Transform40.children.append(Shape41)

HAnimSegment39.children.append(Transform40)

HAnimJoint38.children.append(HAnimSegment39)
HAnimJoint48 = x3d.HAnimJoint()
HAnimJoint48.name = "l_hip"
HAnimJoint48.DEF = "hanim_l_hip"
HAnimJoint48.center = [4.207,32.02,-0.8155]
HAnimJoint48.ulimit = [0,0,0]
HAnimJoint48.llimit = [0,0,0]
HAnimSegment49 = x3d.HAnimSegment()
HAnimSegment49.name = "l_thigh"
HAnimSegment49.DEF = "hanim_l_thigh"
Transform50 = x3d.Transform()
Transform50.translation = [4.207,32.02,-0.8155]
Shape51 = x3d.Shape()
Appearance52 = x3d.Appearance()
Material53 = x3d.Material()
Material53.diffuseColor = [0.588,0.588,0.588]

Appearance52.material = Material53
ImageTexture54 = x3d.ImageTexture()
ImageTexture54.USE = "Annex01JinTextureAtlas"

Appearance52.texture = ImageTexture54

Shape51.appearance = Appearance52
IndexedFaceSet55 = x3d.IndexedFaceSet()
IndexedFaceSet55.coordIndex = [47,46,45,-1,45,44,43,-1,45,43,42,-1,47,45,42,-1,48,47,42,-1,0,1,8,-1,8,7,0,-1,1,2,9,-1,9,8,1,-1,2,3,10,-1,10,9,2,-1,3,4,11,-1,11,10,3,-1,4,5,12,-1,12,11,4,-1,5,6,13,-1,13,12,5,-1,6,0,7,-1,7,13,6,-1,7,8,15,-1,15,14,7,-1,8,9,16,-1,16,15,8,-1,9,10,17,-1,17,16,9,-1,10,11,18,-1,18,17,10,-1,11,12,19,-1,19,18,11,-1,12,13,20,-1,20,19,12,-1,13,7,14,-1,14,20,13,-1,14,15,22,-1,22,21,14,-1,15,16,23,-1,23,22,15,-1,16,17,24,-1,24,23,16,-1,17,18,25,-1,25,24,17,-1,18,19,26,-1,26,25,18,-1,19,20,27,-1,27,26,19,-1,20,14,21,-1,21,27,20,-1,56,57,58,-1,58,59,60,-1,58,60,61,-1,56,58,61,-1,62,56,61,-1,29,28,21,-1,21,22,29,-1,30,29,22,-1,22,23,30,-1,31,30,23,-1,23,24,31,-1,32,31,24,-1,24,25,32,-1,33,32,25,-1,25,26,33,-1,34,33,26,-1,26,27,34,-1,28,34,27,-1,27,21,28,-1,36,35,28,-1,28,29,36,-1,37,36,29,-1,29,30,37,-1,38,37,30,-1,30,31,38,-1,39,38,31,-1,31,32,39,-1,40,39,32,-1,32,33,40,-1,41,40,33,-1,33,34,41,-1,35,41,34,-1,34,28,35,-1,42,43,1,-1,1,0,42,-1,43,44,2,-1,2,1,43,-1,44,45,3,-1,3,2,44,-1,45,46,4,-1,4,3,45,-1,46,47,5,-1,5,4,46,-1,47,48,6,-1,6,5,47,-1,48,42,0,-1,0,6,48,-1,50,49,35,-1,35,36,50,-1,51,50,36,-1,36,37,51,-1,52,51,37,-1,37,38,52,-1,53,52,38,-1,38,39,53,-1,54,53,39,-1,39,40,54,-1,55,54,40,-1,40,41,55,-1,49,55,41,-1,41,35,49,-1,57,56,49,-1,49,50,57,-1,58,57,50,-1,50,51,58,-1,59,58,51,-1,51,52,59,-1,60,59,52,-1,52,53,60,-1,61,60,53,-1,53,54,61,-1,62,61,54,-1,54,55,62,-1,56,62,55,-1,55,49,56,-1]
IndexedFaceSet55.creaseAngle = 3.14159
IndexedFaceSet55.texCoordIndex = [5,4,3,-1,3,2,0,-1,3,0,1,-1,5,3,1,-1,6,5,1,-1,7,10,8,-1,8,9,7,-1,10,12,11,-1,11,8,10,-1,12,14,13,-1,13,11,12,-1,14,16,15,-1,15,13,14,-1,16,18,17,-1,17,15,16,-1,18,20,19,-1,19,17,18,-1,20,7,9,-1,9,19,20,-1,9,8,21,-1,21,22,9,-1,8,11,23,-1,23,21,8,-1,11,13,24,-1,24,23,11,-1,13,15,25,-1,25,24,13,-1,15,17,26,-1,26,25,15,-1,17,19,27,-1,27,26,17,-1,19,9,22,-1,22,27,19,-1,22,21,28,-1,28,29,22,-1,21,23,30,-1,30,28,21,-1,23,24,31,-1,31,30,23,-1,24,25,32,-1,32,31,24,-1,25,26,33,-1,33,32,25,-1,26,27,34,-1,34,33,26,-1,27,22,29,-1,29,34,27,-1,42,43,44,-1,44,45,46,-1,44,46,47,-1,42,44,47,-1,48,42,47,-1,35,36,29,-1,29,28,35,-1,37,35,28,-1,28,30,37,-1,38,37,30,-1,30,31,38,-1,39,38,31,-1,31,32,39,-1,40,39,32,-1,32,33,40,-1,41,40,33,-1,33,34,41,-1,36,41,34,-1,34,29,36,-1,51,52,49,-1,49,50,51,-1,54,51,50,-1,50,53,54,-1,56,54,53,-1,53,55,56,-1,58,56,55,-1,55,57,58,-1,60,58,57,-1,57,59,60,-1,62,60,59,-1,59,61,62,-1,52,62,61,-1,61,49,52,-1,1,0,10,-1,10,7,1,-1,0,2,12,-1,12,10,0,-1,2,3,14,-1,14,12,2,-1,3,4,16,-1,16,14,3,-1,4,5,18,-1,18,16,4,-1,5,6,20,-1,20,18,5,-1,6,1,7,-1,7,20,6,-1,63,64,52,-1,52,51,63,-1,65,63,51,-1,51,54,65,-1,66,65,54,-1,54,56,66,-1,67,66,56,-1,56,58,67,-1,68,67,58,-1,58,60,68,-1,69,68,60,-1,60,62,69,-1,64,69,62,-1,62,52,64,-1,43,42,64,-1,64,63,43,-1,44,43,63,-1,63,65,44,-1,45,44,65,-1,65,66,45,-1,46,45,66,-1,66,67,46,-1,47,46,67,-1,67,68,47,-1,48,47,68,-1,68,69,48,-1,42,48,69,-1,69,64,42,-1]
Coordinate56 = x3d.Coordinate()

IndexedFaceSet55.coord = Coordinate56
TextureCoordinate57 = x3d.TextureCoordinate()

IndexedFaceSet55.texCoord = TextureCoordinate57

Shape51.geometry = IndexedFaceSet55

Transform50.children.append(Shape51)

HAnimSegment49.children.append(Transform50)

HAnimJoint48.children.append(HAnimSegment49)
HAnimJoint58 = x3d.HAnimJoint()
HAnimJoint58.name = "l_knee"
HAnimJoint58.DEF = "hanim_l_knee"
HAnimJoint58.center = [4.116,17.26,-0.8639]
HAnimJoint58.ulimit = [0,0,0]
HAnimJoint58.llimit = [0,0,0]
HAnimSegment59 = x3d.HAnimSegment()
HAnimSegment59.name = "l_calf"
HAnimSegment59.DEF = "hanim_l_calf"
Transform60 = x3d.Transform()
Transform60.translation = [4.116,17.26,-0.8639]
Shape61 = x3d.Shape()
Appearance62 = x3d.Appearance()
Material63 = x3d.Material()
Material63.diffuseColor = [0.588,0.588,0.588]

Appearance62.material = Material63
ImageTexture64 = x3d.ImageTexture()
ImageTexture64.USE = "Annex01JinTextureAtlas"

Appearance62.texture = ImageTexture64

Shape61.appearance = Appearance62
IndexedFaceSet65 = x3d.IndexedFaceSet()
IndexedFaceSet65.coordIndex = [4,3,2,-1,5,4,2,-1,2,1,0,-1,5,2,0,-1,6,5,0,-1,9,8,7,-1,7,10,9,-1,12,11,8,-1,8,9,12,-1,14,13,11,-1,11,12,14,-1,16,15,13,-1,13,14,16,-1,18,17,15,-1,15,16,18,-1,20,19,17,-1,17,18,20,-1,10,7,19,-1,19,20,10,-1,21,9,10,-1,10,22,21,-1,23,12,9,-1,9,21,23,-1,24,14,12,-1,12,23,24,-1,25,16,14,-1,14,24,25,-1,26,18,16,-1,16,25,26,-1,27,20,18,-1,18,26,27,-1,22,10,20,-1,20,27,22,-1,1,21,22,-1,22,0,1,-1,2,23,21,-1,21,1,2,-1,3,24,23,-1,23,2,3,-1,4,25,24,-1,24,3,4,-1,5,26,25,-1,25,4,5,-1,6,27,26,-1,26,5,6,-1,0,22,27,-1,27,6,0,-1,8,29,28,-1,28,7,8,-1,11,30,29,-1,29,8,11,-1,13,31,30,-1,30,11,13,-1,15,32,31,-1,31,13,15,-1,17,33,32,-1,32,15,17,-1,19,34,33,-1,33,17,19,-1,7,28,34,-1,34,19,7,-1,29,36,35,-1,35,28,29,-1,30,37,36,-1,36,29,30,-1,31,38,37,-1,37,30,31,-1,32,39,38,-1,38,31,32,-1,33,40,39,-1,39,32,33,-1,34,41,40,-1,40,33,34,-1,28,35,41,-1,41,34,28,-1]
IndexedFaceSet65.creaseAngle = 3.14159
IndexedFaceSet65.texCoordIndex = [4,3,2,-1,5,4,2,-1,2,1,0,-1,5,2,0,-1,6,5,0,-1,9,8,7,-1,7,10,9,-1,12,11,8,-1,8,9,12,-1,14,13,11,-1,11,12,14,-1,16,15,13,-1,13,14,16,-1,18,17,15,-1,15,16,18,-1,20,19,17,-1,17,18,20,-1,10,7,19,-1,19,20,10,-1,21,9,10,-1,10,22,21,-1,23,12,9,-1,9,21,23,-1,24,14,12,-1,12,23,24,-1,25,16,14,-1,14,24,25,-1,26,18,16,-1,16,25,26,-1,27,20,18,-1,18,26,27,-1,22,10,20,-1,20,27,22,-1,1,21,22,-1,22,0,1,-1,2,23,21,-1,21,1,2,-1,3,24,23,-1,23,2,3,-1,4,25,24,-1,24,3,4,-1,5,26,25,-1,25,4,5,-1,6,27,26,-1,26,5,6,-1,0,22,27,-1,27,6,0,-1,8,29,28,-1,28,7,8,-1,11,30,29,-1,29,8,11,-1,13,31,30,-1,30,11,13,-1,15,32,31,-1,31,13,15,-1,17,33,32,-1,32,15,17,-1,19,34,33,-1,33,17,19,-1,7,28,34,-1,34,19,7,-1,29,36,35,-1,35,28,29,-1,30,37,36,-1,36,29,30,-1,31,38,37,-1,37,30,31,-1,32,39,38,-1,38,31,32,-1,33,40,39,-1,39,32,33,-1,34,41,40,-1,40,33,34,-1,28,35,41,-1,41,34,28,-1]
Coordinate66 = x3d.Coordinate()

IndexedFaceSet65.coord = Coordinate66
TextureCoordinate67 = x3d.TextureCoordinate()

IndexedFaceSet65.texCoord = TextureCoordinate67

Shape61.geometry = IndexedFaceSet65

Transform60.children.append(Shape61)

HAnimSegment59.children.append(Transform60)

HAnimJoint58.children.append(HAnimSegment59)
HAnimJoint68 = x3d.HAnimJoint()
HAnimJoint68.name = "l_talocrural"
HAnimJoint68.DEF = "hanim_l_talocrural"
HAnimJoint68.center = [3.854,3.939,-0.7038]
HAnimJoint68.ulimit = [0,0,0]
HAnimJoint68.llimit = [0,0,0]
HAnimSegment69 = x3d.HAnimSegment()
HAnimSegment69.name = "l_talus"
HAnimSegment69.DEF = "hanim_l_talus"
Transform70 = x3d.Transform()
Transform70.translation = [3.854,3.939,-0.7038]
Shape71 = x3d.Shape()
Appearance72 = x3d.Appearance()
Material73 = x3d.Material()
Material73.diffuseColor = [0.588,0.588,0.588]

Appearance72.material = Material73
ImageTexture74 = x3d.ImageTexture()
ImageTexture74.USE = "Annex01JinTextureAtlas"

Appearance72.texture = ImageTexture74

Shape71.appearance = Appearance72
IndexedFaceSet75 = x3d.IndexedFaceSet()
IndexedFaceSet75.coordIndex = [1,11,14,-1,3,4,5,-1,5,6,3,-1,1,0,4,-1,4,3,1,-1,0,2,5,-1,5,4,0,-1,11,1,3,-1,3,6,11,-1,15,2,0,-1,0,12,15,-1,0,1,13,-1,13,12,0,-1,13,1,14,-1,7,18,11,-1,8,6,5,-1,5,9,8,-1,7,8,9,-1,9,10,7,-1,10,9,5,-1,5,2,10,-1,11,6,8,-1,8,7,11,-1,15,16,10,-1,10,2,15,-1,10,16,17,-1,17,7,10,-1,17,18,7,-1,21,22,23,-1,23,24,25,-1,25,26,19,-1,23,25,19,-1,21,23,19,-1,20,21,19,-1,15,12,20,-1,20,19,15,-1,12,13,21,-1,21,20,12,-1,13,14,22,-1,22,21,13,-1,14,11,23,-1,23,22,14,-1,11,18,24,-1,24,23,11,-1,18,17,25,-1,25,24,18,-1,17,16,26,-1,26,25,17,-1,16,15,19,-1,19,26,16,-1,33,31,30,-1,30,27,33,-1,36,27,30,-1,30,38,36,-1,29,33,27,-1,27,28,29,-1,37,28,27,-1,27,36,37,-1,28,37,42,-1,42,29,28,-1,33,32,34,-1,34,31,33,-1,39,40,34,-1,34,32,39,-1,29,35,32,-1,32,33,29,-1,41,39,32,-1,32,35,41,-1,35,29,42,-1,42,41,35,-1,44,45,46,-1,44,46,47,-1,44,47,43,-1,51,52,53,-1,54,48,49,-1,53,54,49,-1,51,53,49,-1,51,49,50,-1,30,31,44,-1,44,43,30,-1,31,34,45,-1,45,44,31,-1,34,40,46,-1,46,45,34,-1,40,38,47,-1,47,46,40,-1,38,30,43,-1,43,47,38,-1,37,36,49,-1,49,48,37,-1,36,38,50,-1,50,49,36,-1,38,40,51,-1,51,50,38,-1,40,39,52,-1,52,51,40,-1,39,41,53,-1,53,52,39,-1,41,42,54,-1,54,53,41,-1,42,37,48,-1,48,54,42,-1]
IndexedFaceSet75.creaseAngle = 3.14159
IndexedFaceSet75.texCoordIndex = [1,14,18,-1,3,4,5,-1,5,6,3,-1,1,0,4,-1,4,3,1,-1,0,2,5,-1,5,4,0,-1,14,1,3,-1,3,6,14,-1,19,2,0,-1,0,16,19,-1,0,1,17,-1,17,16,0,-1,17,1,18,-1,7,23,15,-1,9,8,11,-1,11,10,9,-1,7,9,10,-1,10,12,7,-1,12,10,11,-1,11,13,12,-1,15,8,9,-1,9,7,15,-1,20,21,12,-1,12,13,20,-1,12,21,22,-1,22,7,12,-1,22,23,7,-1,26,27,28,-1,28,29,30,-1,30,31,24,-1,28,30,24,-1,26,28,24,-1,25,26,24,-1,19,16,25,-1,25,24,19,-1,16,17,26,-1,26,25,16,-1,17,18,27,-1,27,26,17,-1,18,14,28,-1,28,27,18,-1,15,23,29,-1,29,28,15,-1,23,22,30,-1,30,29,23,-1,22,21,31,-1,31,30,22,-1,21,20,24,-1,24,31,21,-1,34,38,37,-1,37,32,34,-1,46,32,37,-1,37,48,46,-1,35,34,32,-1,32,33,35,-1,47,33,32,-1,32,46,47,-1,33,47,53,-1,53,36,33,-1,40,39,42,-1,42,41,40,-1,49,50,42,-1,42,39,49,-1,44,43,39,-1,39,40,44,-1,51,49,39,-1,39,43,51,-1,43,45,52,-1,52,51,43,-1,55,56,57,-1,55,57,58,-1,55,58,54,-1,62,63,64,-1,65,59,60,-1,64,65,60,-1,62,64,60,-1,62,60,61,-1,37,38,55,-1,55,54,37,-1,41,42,56,-1,56,55,41,-1,42,50,57,-1,57,56,42,-1,50,48,58,-1,58,57,50,-1,48,37,54,-1,54,58,48,-1,47,46,60,-1,60,59,47,-1,46,48,61,-1,61,60,46,-1,48,50,62,-1,62,61,48,-1,50,49,63,-1,63,62,50,-1,49,51,64,-1,64,63,49,-1,51,52,65,-1,65,64,51,-1,53,47,59,-1,59,65,53,-1]
Coordinate76 = x3d.Coordinate()

IndexedFaceSet75.coord = Coordinate76
TextureCoordinate77 = x3d.TextureCoordinate()

IndexedFaceSet75.texCoord = TextureCoordinate77

Shape71.geometry = IndexedFaceSet75

Transform70.children.append(Shape71)

HAnimSegment69.children.append(Transform70)

HAnimJoint68.children.append(HAnimSegment69)
HAnimJoint78 = x3d.HAnimJoint()
HAnimJoint78.name = "l_metatarsophalangeal_2"
HAnimJoint78.DEF = "hanim_l_metatarsophalangeal_2"
HAnimJoint78.center = [3.854,3.64,0.7402]
HAnimJoint78.ulimit = [0,0,0]
HAnimJoint78.llimit = [0,0,0]
HAnimSegment79 = x3d.HAnimSegment()
HAnimSegment79.name = "l_tarsal_proximal_phalanx_2"
HAnimSegment79.DEF = "hanim_l_tarsal_proximal_phalanx_2"
Transform80 = x3d.Transform()
Transform80.translation = [3.854,3.64,0.7402]
Shape81 = x3d.Shape()
Appearance82 = x3d.Appearance()
Material83 = x3d.Material()
Material83.diffuseColor = [0.588,0.588,0.588]

Appearance82.material = Material83
ImageTexture84 = x3d.ImageTexture()
ImageTexture84.USE = "Annex01JinTextureAtlas"

Appearance82.texture = ImageTexture84

Shape81.appearance = Appearance82
IndexedFaceSet85 = x3d.IndexedFaceSet()
IndexedFaceSet85.coordIndex = [3,4,10,-1,3,10,11,-1,0,3,11,-1,1,0,11,-1,11,12,1,-1,1,12,16,-1,16,9,1,-1,2,17,10,-1,10,4,2,-1,13,8,6,-1,14,13,6,-1,5,14,6,-1,7,15,14,-1,14,5,7,-1,7,9,16,-1,16,15,7,-1,2,8,13,-1,13,17,2,-1,20,21,22,-1,20,22,23,-1,20,23,24,-1,19,20,24,-1,19,24,18,-1,0,1,19,-1,19,18,0,-1,1,9,20,-1,20,19,1,-1,9,7,21,-1,21,20,9,-1,7,5,22,-1,22,21,7,-1,5,6,23,-1,23,22,5,-1,6,3,24,-1,24,23,6,-1,3,0,18,-1,18,24,3,-1,6,8,2,-1,3,6,2,-1,4,3,2,-1,28,26,25,-1,25,29,28,-1,35,27,26,-1,26,28,35,-1,27,35,40,-1,25,26,31,-1,31,30,25,-1,31,26,27,-1,27,32,31,-1,32,27,40,-1,40,41,32,-1,42,29,25,-1,25,30,42,-1,28,29,34,-1,34,33,28,-1,35,28,33,-1,33,36,35,-1,36,40,35,-1,34,37,38,-1,38,33,34,-1,38,39,36,-1,36,33,38,-1,39,41,40,-1,40,36,39,-1,42,37,34,-1,34,29,42,-1]
IndexedFaceSet85.creaseAngle = 3.14159
IndexedFaceSet85.texCoordIndex = [4,5,12,-1,4,12,13,-1,0,4,13,-1,1,0,13,-1,13,14,1,-1,1,14,19,-1,19,3,1,-1,2,21,12,-1,12,5,2,-1,15,10,7,-1,16,15,7,-1,6,16,7,-1,8,17,16,-1,16,6,8,-1,8,11,18,-1,18,17,8,-1,9,10,15,-1,15,20,9,-1,24,25,26,-1,24,26,27,-1,24,27,28,-1,23,24,28,-1,23,28,22,-1,0,1,23,-1,23,22,0,-1,1,3,24,-1,24,23,1,-1,11,8,25,-1,25,24,11,-1,8,6,26,-1,26,25,8,-1,6,7,27,-1,27,26,6,-1,7,4,28,-1,28,27,7,-1,4,0,22,-1,22,28,4,-1,7,10,9,-1,4,7,9,-1,5,4,9,-1,30,32,31,-1,31,29,30,-1,33,34,32,-1,32,30,33,-1,34,33,35,-1,31,32,37,-1,37,36,31,-1,37,32,34,-1,34,38,37,-1,38,34,35,-1,35,39,38,-1,40,29,31,-1,31,36,40,-1,41,44,43,-1,43,42,41,-1,45,41,42,-1,42,46,45,-1,46,50,45,-1,43,47,48,-1,48,42,43,-1,48,49,46,-1,46,42,48,-1,49,51,50,-1,50,46,49,-1,52,47,43,-1,43,44,52,-1]
Coordinate86 = x3d.Coordinate()

IndexedFaceSet85.coord = Coordinate86
TextureCoordinate87 = x3d.TextureCoordinate()

IndexedFaceSet85.texCoord = TextureCoordinate87

Shape81.geometry = IndexedFaceSet85

Transform80.children.append(Shape81)

HAnimSegment79.children.append(Transform80)

HAnimJoint78.children.append(HAnimSegment79)

HAnimJoint68.children.append(HAnimJoint78)

HAnimJoint58.children.append(HAnimJoint68)

HAnimJoint48.children.append(HAnimJoint58)

HAnimJoint38.children.append(HAnimJoint48)
HAnimJoint88 = x3d.HAnimJoint()
HAnimJoint88.name = "r_hip"
HAnimJoint88.DEF = "hanim_r_hip"
HAnimJoint88.center = [-4.207,32.02,-0.8155]
HAnimJoint88.ulimit = [0,0,0]
HAnimJoint88.llimit = [0,0,0]
HAnimSegment89 = x3d.HAnimSegment()
HAnimSegment89.name = "r_thigh"
HAnimSegment89.DEF = "hanim_r_thigh"
Transform90 = x3d.Transform()
Transform90.translation = [-4.207,32.02,-0.8155]
Shape91 = x3d.Shape()
Appearance92 = x3d.Appearance()
Material93 = x3d.Material()
Material93.diffuseColor = [0.588,0.588,0.588]

Appearance92.material = Material93
ImageTexture94 = x3d.ImageTexture()
ImageTexture94.USE = "Annex01JinTextureAtlas"

Appearance92.texture = ImageTexture94

Shape91.appearance = Appearance92
IndexedFaceSet95 = x3d.IndexedFaceSet()
IndexedFaceSet95.coordIndex = [43,44,45,-1,42,43,45,-1,45,46,47,-1,42,45,47,-1,48,42,47,-1,0,7,8,-1,8,1,0,-1,1,8,9,-1,9,2,1,-1,2,9,10,-1,10,3,2,-1,3,10,11,-1,11,4,3,-1,4,11,12,-1,12,5,4,-1,5,12,13,-1,13,6,5,-1,6,13,7,-1,7,0,6,-1,7,14,15,-1,15,8,7,-1,8,15,16,-1,16,9,8,-1,9,16,17,-1,17,10,9,-1,10,17,18,-1,18,11,10,-1,11,18,19,-1,19,12,11,-1,12,19,20,-1,20,13,12,-1,13,20,14,-1,14,7,13,-1,14,21,22,-1,22,15,14,-1,15,22,23,-1,23,16,15,-1,16,23,24,-1,24,17,16,-1,17,24,25,-1,25,18,17,-1,18,25,26,-1,26,19,18,-1,19,26,27,-1,27,20,19,-1,20,27,21,-1,21,14,20,-1,60,59,58,-1,61,60,58,-1,58,57,56,-1,61,58,56,-1,62,61,56,-1,29,22,21,-1,21,28,29,-1,30,23,22,-1,22,29,30,-1,31,24,23,-1,23,30,31,-1,32,25,24,-1,24,31,32,-1,33,26,25,-1,25,32,33,-1,34,27,26,-1,26,33,34,-1,28,21,27,-1,27,34,28,-1,36,29,28,-1,28,35,36,-1,37,30,29,-1,29,36,37,-1,38,31,30,-1,30,37,38,-1,39,32,31,-1,31,38,39,-1,40,33,32,-1,32,39,40,-1,41,34,33,-1,33,40,41,-1,35,28,34,-1,34,41,35,-1,42,0,1,-1,1,43,42,-1,43,1,2,-1,2,44,43,-1,44,2,3,-1,3,45,44,-1,45,3,4,-1,4,46,45,-1,46,4,5,-1,5,47,46,-1,47,5,6,-1,6,48,47,-1,48,6,0,-1,0,42,48,-1,50,36,35,-1,35,49,50,-1,51,37,36,-1,36,50,51,-1,52,38,37,-1,37,51,52,-1,53,39,38,-1,38,52,53,-1,54,40,39,-1,39,53,54,-1,55,41,40,-1,40,54,55,-1,49,35,41,-1,41,55,49,-1,57,50,49,-1,49,56,57,-1,58,51,50,-1,50,57,58,-1,59,52,51,-1,51,58,59,-1,60,53,52,-1,52,59,60,-1,61,54,53,-1,53,60,61,-1,62,55,54,-1,54,61,62,-1,56,49,55,-1,55,62,56,-1]
IndexedFaceSet95.creaseAngle = 3.14159
IndexedFaceSet95.texCoordIndex = [0,2,3,-1,1,0,3,-1,3,4,5,-1,1,3,5,-1,6,1,5,-1,7,9,8,-1,8,10,7,-1,10,8,11,-1,11,12,10,-1,12,11,13,-1,13,14,12,-1,14,13,15,-1,15,16,14,-1,16,15,17,-1,17,18,16,-1,18,17,19,-1,19,20,18,-1,20,19,9,-1,9,7,20,-1,9,22,21,-1,21,8,9,-1,8,21,23,-1,23,11,8,-1,11,23,24,-1,24,13,11,-1,13,24,25,-1,25,15,13,-1,15,25,26,-1,26,17,15,-1,17,26,27,-1,27,19,17,-1,19,27,22,-1,22,9,19,-1,22,29,28,-1,28,21,22,-1,21,28,30,-1,30,23,21,-1,23,30,31,-1,31,24,23,-1,24,31,32,-1,32,25,24,-1,25,32,33,-1,33,26,25,-1,26,33,34,-1,34,27,26,-1,27,34,29,-1,29,22,27,-1,46,45,44,-1,47,46,44,-1,44,43,42,-1,47,44,42,-1,48,47,42,-1,35,28,29,-1,29,36,35,-1,37,30,28,-1,28,35,37,-1,38,31,30,-1,30,37,38,-1,39,32,31,-1,31,38,39,-1,40,33,32,-1,32,39,40,-1,41,34,33,-1,33,40,41,-1,36,29,34,-1,34,41,36,-1,51,50,49,-1,49,52,51,-1,54,53,50,-1,50,51,54,-1,56,55,53,-1,53,54,56,-1,58,57,55,-1,55,56,58,-1,60,59,57,-1,57,58,60,-1,62,61,59,-1,59,60,62,-1,52,49,61,-1,61,62,52,-1,1,7,10,-1,10,0,1,-1,0,10,12,-1,12,2,0,-1,2,12,14,-1,14,3,2,-1,3,14,16,-1,16,4,3,-1,4,16,18,-1,18,5,4,-1,5,18,20,-1,20,6,5,-1,6,20,7,-1,7,1,6,-1,63,51,52,-1,52,64,63,-1,65,54,51,-1,51,63,65,-1,66,56,54,-1,54,65,66,-1,67,58,56,-1,56,66,67,-1,68,60,58,-1,58,67,68,-1,69,62,60,-1,60,68,69,-1,64,52,62,-1,62,69,64,-1,43,63,64,-1,64,42,43,-1,44,65,63,-1,63,43,44,-1,45,66,65,-1,65,44,45,-1,46,67,66,-1,66,45,46,-1,47,68,67,-1,67,46,47,-1,48,69,68,-1,68,47,48,-1,42,64,69,-1,69,48,42,-1]
Coordinate96 = x3d.Coordinate()

IndexedFaceSet95.coord = Coordinate96
TextureCoordinate97 = x3d.TextureCoordinate()

IndexedFaceSet95.texCoord = TextureCoordinate97

Shape91.geometry = IndexedFaceSet95

Transform90.children.append(Shape91)

HAnimSegment89.children.append(Transform90)

HAnimJoint88.children.append(HAnimSegment89)
HAnimJoint98 = x3d.HAnimJoint()
HAnimJoint98.name = "r_knee"
HAnimJoint98.DEF = "hanim_r_knee"
HAnimJoint98.center = [-4.116,17.26,-0.8639]
HAnimJoint98.ulimit = [0,0,0]
HAnimJoint98.llimit = [0,0,0]
HAnimSegment99 = x3d.HAnimSegment()
HAnimSegment99.name = "r_calf"
HAnimSegment99.DEF = "hanim_r_calf"
Transform100 = x3d.Transform()
Transform100.translation = [-4.116,17.26,-0.8639]
Shape101 = x3d.Shape()
Appearance102 = x3d.Appearance()
Material103 = x3d.Material()
Material103.diffuseColor = [0.588,0.588,0.588]

Appearance102.material = Material103
ImageTexture104 = x3d.ImageTexture()
ImageTexture104.USE = "Annex01JinTextureAtlas"

Appearance102.texture = ImageTexture104

Shape101.appearance = Appearance102
IndexedFaceSet105 = x3d.IndexedFaceSet()
IndexedFaceSet105.coordIndex = [0,1,2,-1,2,3,4,-1,2,4,5,-1,0,2,5,-1,6,0,5,-1,9,10,7,-1,7,8,9,-1,12,9,8,-1,8,11,12,-1,14,12,11,-1,11,13,14,-1,16,14,13,-1,13,15,16,-1,18,16,15,-1,15,17,18,-1,20,18,17,-1,17,19,20,-1,10,20,19,-1,19,7,10,-1,21,22,10,-1,10,9,21,-1,23,21,9,-1,9,12,23,-1,24,23,12,-1,12,14,24,-1,25,24,14,-1,14,16,25,-1,26,25,16,-1,16,18,26,-1,27,26,18,-1,18,20,27,-1,22,27,20,-1,20,10,22,-1,1,0,22,-1,22,21,1,-1,2,1,21,-1,21,23,2,-1,3,2,23,-1,23,24,3,-1,4,3,24,-1,24,25,4,-1,5,4,25,-1,25,26,5,-1,6,5,26,-1,26,27,6,-1,0,6,27,-1,27,22,0,-1,8,7,28,-1,28,29,8,-1,11,8,29,-1,29,30,11,-1,13,11,30,-1,30,31,13,-1,15,13,31,-1,31,32,15,-1,17,15,32,-1,32,33,17,-1,19,17,33,-1,33,34,19,-1,7,19,34,-1,34,28,7,-1,29,28,35,-1,35,36,29,-1,30,29,36,-1,36,37,30,-1,31,30,37,-1,37,38,31,-1,32,31,38,-1,38,39,32,-1,33,32,39,-1,39,40,33,-1,34,33,40,-1,40,41,34,-1,28,34,41,-1,41,35,28,-1]
IndexedFaceSet105.creaseAngle = 3.14159
IndexedFaceSet105.texCoordIndex = [0,1,2,-1,2,3,4,-1,2,4,5,-1,0,2,5,-1,6,0,5,-1,9,10,7,-1,7,8,9,-1,12,9,8,-1,8,11,12,-1,14,12,11,-1,11,13,14,-1,16,14,13,-1,13,15,16,-1,18,16,15,-1,15,17,18,-1,20,18,17,-1,17,19,20,-1,10,20,19,-1,19,7,10,-1,21,22,10,-1,10,9,21,-1,23,21,9,-1,9,12,23,-1,24,23,12,-1,12,14,24,-1,25,24,14,-1,14,16,25,-1,26,25,16,-1,16,18,26,-1,27,26,18,-1,18,20,27,-1,22,27,20,-1,20,10,22,-1,1,0,22,-1,22,21,1,-1,2,1,21,-1,21,23,2,-1,3,2,23,-1,23,24,3,-1,4,3,24,-1,24,25,4,-1,5,4,25,-1,25,26,5,-1,6,5,26,-1,26,27,6,-1,0,6,27,-1,27,22,0,-1,8,7,28,-1,28,29,8,-1,11,8,29,-1,29,30,11,-1,13,11,30,-1,30,31,13,-1,15,13,31,-1,31,32,15,-1,17,15,32,-1,32,33,17,-1,19,17,33,-1,33,34,19,-1,7,19,34,-1,34,28,7,-1,29,28,35,-1,35,36,29,-1,30,29,36,-1,36,37,30,-1,31,30,37,-1,37,38,31,-1,32,31,38,-1,38,39,32,-1,33,32,39,-1,39,40,33,-1,34,33,40,-1,40,41,34,-1,28,34,41,-1,41,35,28,-1]
Coordinate106 = x3d.Coordinate()

IndexedFaceSet105.coord = Coordinate106
TextureCoordinate107 = x3d.TextureCoordinate()

IndexedFaceSet105.texCoord = TextureCoordinate107

Shape101.geometry = IndexedFaceSet105

Transform100.children.append(Shape101)

HAnimSegment99.children.append(Transform100)

HAnimJoint98.children.append(HAnimSegment99)
HAnimJoint108 = x3d.HAnimJoint()
HAnimJoint108.name = "r_talocrural"
HAnimJoint108.DEF = "hanim_r_talocrural"
HAnimJoint108.center = [-3.854,3.939,-0.7038]
HAnimJoint108.ulimit = [0,0,0]
HAnimJoint108.llimit = [0,0,0]
HAnimSegment109 = x3d.HAnimSegment()
HAnimSegment109.name = "r_talus"
HAnimSegment109.DEF = "hanim_r_talus"
Transform110 = x3d.Transform()
Transform110.translation = [-3.854,3.939,-0.7038]
Shape111 = x3d.Shape()
Appearance112 = x3d.Appearance()
Material113 = x3d.Material()
Material113.diffuseColor = [0.588,0.588,0.588]

Appearance112.material = Material113
ImageTexture114 = x3d.ImageTexture()
ImageTexture114.USE = "Annex01JinTextureAtlas"

Appearance112.texture = ImageTexture114

Shape111.appearance = Appearance112
IndexedFaceSet115 = x3d.IndexedFaceSet()
IndexedFaceSet115.coordIndex = [1,14,11,-1,3,6,5,-1,5,4,3,-1,1,3,4,-1,4,0,1,-1,0,4,5,-1,5,2,0,-1,11,6,3,-1,3,1,11,-1,15,12,0,-1,0,2,15,-1,0,12,13,-1,13,1,0,-1,13,14,1,-1,7,11,18,-1,8,9,5,-1,5,6,8,-1,7,10,9,-1,9,8,7,-1,10,2,5,-1,5,9,10,-1,11,7,8,-1,8,6,11,-1,15,2,10,-1,10,16,15,-1,10,7,17,-1,17,16,10,-1,17,7,18,-1,19,26,25,-1,25,24,23,-1,19,25,23,-1,23,22,21,-1,19,23,21,-1,20,19,21,-1,15,19,20,-1,20,12,15,-1,12,20,21,-1,21,13,12,-1,13,21,22,-1,22,14,13,-1,14,22,23,-1,23,11,14,-1,11,23,24,-1,24,18,11,-1,18,24,25,-1,25,17,18,-1,17,25,26,-1,26,16,17,-1,16,26,19,-1,19,15,16,-1,33,27,30,-1,30,31,33,-1,36,38,30,-1,30,27,36,-1,29,28,27,-1,27,33,29,-1,37,36,27,-1,27,28,37,-1,28,29,42,-1,42,37,28,-1,33,31,34,-1,34,32,33,-1,39,32,34,-1,34,40,39,-1,29,33,32,-1,32,35,29,-1,41,35,32,-1,32,39,41,-1,35,41,42,-1,42,29,35,-1,44,43,47,-1,44,47,46,-1,44,46,45,-1,51,50,49,-1,49,48,54,-1,49,54,53,-1,51,49,53,-1,51,53,52,-1,30,43,44,-1,44,31,30,-1,31,44,45,-1,45,34,31,-1,34,45,46,-1,46,40,34,-1,40,46,47,-1,47,38,40,-1,38,47,43,-1,43,30,38,-1,37,48,49,-1,49,36,37,-1,36,49,50,-1,50,38,36,-1,38,50,51,-1,51,40,38,-1,40,51,52,-1,52,39,40,-1,39,52,53,-1,53,41,39,-1,41,53,54,-1,54,42,41,-1,42,54,48,-1,48,37,42,-1]
IndexedFaceSet115.creaseAngle = 3.14159
IndexedFaceSet115.texCoordIndex = [1,18,14,-1,3,6,5,-1,5,4,3,-1,1,3,4,-1,4,0,1,-1,0,4,5,-1,5,2,0,-1,14,6,3,-1,3,1,14,-1,19,16,0,-1,0,2,19,-1,0,16,17,-1,17,1,0,-1,17,18,1,-1,7,15,23,-1,9,10,11,-1,11,8,9,-1,7,12,10,-1,10,9,7,-1,12,13,11,-1,11,10,12,-1,15,7,9,-1,9,8,15,-1,20,13,12,-1,12,21,20,-1,12,7,22,-1,22,21,12,-1,22,7,23,-1,24,31,30,-1,30,29,28,-1,24,30,28,-1,28,27,26,-1,24,28,26,-1,25,24,26,-1,19,24,25,-1,25,16,19,-1,16,25,26,-1,26,17,16,-1,17,26,27,-1,27,18,17,-1,18,27,28,-1,28,14,18,-1,15,28,29,-1,29,23,15,-1,23,29,30,-1,30,22,23,-1,22,30,31,-1,31,21,22,-1,21,31,24,-1,24,20,21,-1,34,32,37,-1,37,38,34,-1,46,48,37,-1,37,32,46,-1,35,33,32,-1,32,34,35,-1,47,46,32,-1,32,33,47,-1,33,36,53,-1,53,47,33,-1,40,41,42,-1,42,39,40,-1,49,39,42,-1,42,50,49,-1,44,40,39,-1,39,43,44,-1,51,43,39,-1,39,49,51,-1,43,51,52,-1,52,45,43,-1,55,54,58,-1,55,58,57,-1,55,57,56,-1,62,61,60,-1,60,59,65,-1,60,65,64,-1,62,60,64,-1,62,64,63,-1,37,54,55,-1,55,38,37,-1,41,55,56,-1,56,42,41,-1,42,56,57,-1,57,50,42,-1,50,57,58,-1,58,48,50,-1,48,58,54,-1,54,37,48,-1,47,59,60,-1,60,46,47,-1,46,60,61,-1,61,48,46,-1,48,61,62,-1,62,50,48,-1,50,62,63,-1,63,49,50,-1,49,63,64,-1,64,51,49,-1,51,64,65,-1,65,52,51,-1,53,65,59,-1,59,47,53,-1]
Coordinate116 = x3d.Coordinate()

IndexedFaceSet115.coord = Coordinate116
TextureCoordinate117 = x3d.TextureCoordinate()

IndexedFaceSet115.texCoord = TextureCoordinate117

Shape111.geometry = IndexedFaceSet115

Transform110.children.append(Shape111)

HAnimSegment109.children.append(Transform110)

HAnimJoint108.children.append(HAnimSegment109)
HAnimJoint118 = x3d.HAnimJoint()
HAnimJoint118.name = "r_metatarsophalangeal_2"
HAnimJoint118.DEF = "hanim_r_metatarsophalangeal_2"
HAnimJoint118.center = [-3.854,3.64,0.7402]
HAnimJoint118.ulimit = [0,0,0]
HAnimJoint118.llimit = [0,0,0]
HAnimSegment119 = x3d.HAnimSegment()
HAnimSegment119.name = "r_tarsal_proximal_phalanx_2"
HAnimSegment119.DEF = "hanim_r_tarsal_proximal_phalanx_2"
Transform120 = x3d.Transform()
Transform120.translation = [-3.854,3.64,0.7402]
Shape121 = x3d.Shape()
Appearance122 = x3d.Appearance()
Material123 = x3d.Material()
Material123.diffuseColor = [0.588,0.588,0.588]

Appearance122.material = Material123
ImageTexture124 = x3d.ImageTexture()
ImageTexture124.USE = "Annex01JinTextureAtlas"

Appearance122.texture = ImageTexture124

Shape121.appearance = Appearance122
IndexedFaceSet125 = x3d.IndexedFaceSet()
IndexedFaceSet125.coordIndex = [10,4,3,-1,11,10,3,-1,0,11,3,-1,1,12,11,-1,11,0,1,-1,1,9,16,-1,16,12,1,-1,2,4,10,-1,10,17,2,-1,6,8,13,-1,6,13,14,-1,5,6,14,-1,7,5,14,-1,14,15,7,-1,7,15,16,-1,16,9,7,-1,2,17,13,-1,13,8,2,-1,19,18,24,-1,22,21,20,-1,23,22,20,-1,24,23,20,-1,19,24,20,-1,0,18,19,-1,19,1,0,-1,1,19,20,-1,20,9,1,-1,9,20,21,-1,21,7,9,-1,7,21,22,-1,22,5,7,-1,5,22,23,-1,23,6,5,-1,6,23,24,-1,24,3,6,-1,3,24,18,-1,18,0,3,-1,2,8,6,-1,2,6,3,-1,4,2,3,-1,28,29,25,-1,25,26,28,-1,35,28,26,-1,26,27,35,-1,27,40,35,-1,25,30,31,-1,31,26,25,-1,31,32,27,-1,27,26,31,-1,32,41,40,-1,40,27,32,-1,42,30,25,-1,25,29,42,-1,28,33,34,-1,34,29,28,-1,35,36,33,-1,33,28,35,-1,36,35,40,-1,34,33,38,-1,38,37,34,-1,38,33,36,-1,36,39,38,-1,39,36,40,-1,40,41,39,-1,42,29,34,-1,34,37,42,-1]
IndexedFaceSet125.creaseAngle = 3.14159
IndexedFaceSet125.texCoordIndex = [12,5,4,-1,13,12,4,-1,0,13,4,-1,1,14,13,-1,13,0,1,-1,1,3,19,-1,19,14,1,-1,2,5,12,-1,12,21,2,-1,7,10,15,-1,7,15,16,-1,6,7,16,-1,8,6,16,-1,16,17,8,-1,8,17,18,-1,18,11,8,-1,9,20,15,-1,15,10,9,-1,23,22,28,-1,26,25,24,-1,27,26,24,-1,28,27,24,-1,23,28,24,-1,0,22,23,-1,23,1,0,-1,1,23,24,-1,24,3,1,-1,11,24,25,-1,25,8,11,-1,8,25,26,-1,26,6,8,-1,6,26,27,-1,27,7,6,-1,7,27,28,-1,28,4,7,-1,4,28,22,-1,22,0,4,-1,9,10,7,-1,9,7,4,-1,5,9,4,-1,30,29,31,-1,31,32,30,-1,33,30,32,-1,32,34,33,-1,34,35,33,-1,31,36,37,-1,37,32,31,-1,37,38,34,-1,34,32,37,-1,38,39,35,-1,35,34,38,-1,40,36,31,-1,31,29,40,-1,41,42,43,-1,43,44,41,-1,45,46,42,-1,42,41,45,-1,46,45,50,-1,43,42,48,-1,48,47,43,-1,48,42,46,-1,46,49,48,-1,49,46,50,-1,50,51,49,-1,52,44,43,-1,43,47,52,-1]
Coordinate126 = x3d.Coordinate()

IndexedFaceSet125.coord = Coordinate126
TextureCoordinate127 = x3d.TextureCoordinate()

IndexedFaceSet125.texCoord = TextureCoordinate127

Shape121.geometry = IndexedFaceSet125

Transform120.children.append(Shape121)

HAnimSegment119.children.append(Transform120)

HAnimJoint118.children.append(HAnimSegment119)

HAnimJoint108.children.append(HAnimJoint118)

HAnimJoint98.children.append(HAnimJoint108)

HAnimJoint88.children.append(HAnimJoint98)

HAnimJoint38.children.append(HAnimJoint88)
HAnimJoint128 = x3d.HAnimJoint()
HAnimJoint128.name = "vl5"
HAnimJoint128.DEF = "hanim_vl5"
HAnimJoint128.center = [0,40.23,-0.8527]
HAnimJoint128.ulimit = [0,0,0]
HAnimJoint128.llimit = [0,0,0]
HAnimSegment129 = x3d.HAnimSegment()
HAnimSegment129.name = "l5"
HAnimSegment129.DEF = "hanim_l5"
Transform130 = x3d.Transform()
Transform130.translation = [0,40.23,-0.8527]
Shape131 = x3d.Shape()
Appearance132 = x3d.Appearance()
Material133 = x3d.Material()
Material133.diffuseColor = [0.588,0.588,0.588]

Appearance132.material = Material133
ImageTexture134 = x3d.ImageTexture()
ImageTexture134.USE = "Annex01JinTextureAtlas"

Appearance132.texture = ImageTexture134

Shape131.appearance = Appearance132
IndexedFaceSet135 = x3d.IndexedFaceSet()
IndexedFaceSet135.coordIndex = [3,4,7,-1,7,5,3,-1,4,66,68,-1,68,8,4,-1,4,8,7,-1,1,0,9,-1,9,10,1,-1,0,2,11,-1,11,9,0,-1,15,71,73,-1,73,16,15,-1,14,15,16,-1,16,17,14,-1,71,15,8,-1,8,68,71,-1,15,14,7,-1,7,8,15,-1,73,72,69,-1,69,70,73,-1,16,73,70,-1,70,12,16,-1,16,12,13,-1,13,17,16,-1,21,20,22,-1,22,23,21,-1,20,14,17,-1,17,22,20,-1,20,21,6,-1,6,5,20,-1,14,20,5,-1,5,7,14,-1,23,22,18,-1,18,19,23,-1,22,17,13,-1,13,18,22,-1,2,6,11,-1,28,27,30,-1,30,31,28,-1,27,29,32,-1,32,30,27,-1,29,21,23,-1,23,32,29,-1,27,28,10,-1,10,9,27,-1,29,27,9,-1,9,11,29,-1,21,29,11,-1,11,6,21,-1,31,30,24,-1,24,25,31,-1,30,32,26,-1,26,24,30,-1,32,23,19,-1,19,26,32,-1,12,70,74,-1,74,33,12,-1,24,26,36,-1,36,35,24,-1,33,74,75,-1,75,37,33,-1,34,33,37,-1,37,38,34,-1,39,12,33,-1,33,34,39,-1,19,40,26,-1,26,40,41,-1,41,36,26,-1,39,34,41,-1,41,40,39,-1,35,36,43,-1,43,42,35,-1,36,41,44,-1,44,43,36,-1,41,34,38,-1,38,44,41,-1,37,75,76,-1,76,45,37,-1,38,37,45,-1,45,46,38,-1,42,43,48,-1,48,47,42,-1,44,38,46,-1,46,49,44,-1,45,76,77,-1,77,50,45,-1,46,45,50,-1,50,51,46,-1,47,48,53,-1,53,52,47,-1,48,49,54,-1,54,53,48,-1,49,46,51,-1,51,54,49,-1,50,77,78,-1,78,55,50,-1,51,50,55,-1,55,56,51,-1,52,53,58,-1,58,57,52,-1,53,54,59,-1,59,58,53,-1,54,51,56,-1,56,59,54,-1,19,18,60,-1,60,61,19,-1,18,13,62,-1,62,60,18,-1,13,39,63,-1,63,62,13,-1,40,19,61,-1,61,64,40,-1,39,40,64,-1,64,63,39,-1,2,3,5,-1,2,5,6,-1,13,12,39,-1,25,24,35,-1,70,69,74,-1,67,68,66,-1,66,65,67,-1,79,71,68,-1,68,67,79,-1,72,73,71,-1,71,79,72,-1,49,48,43,-1,43,44,49,-1,63,64,60,-1,60,62,63,-1,60,64,61,-1,86,83,82,-1,82,84,86,-1,141,140,83,-1,83,87,141,-1,83,86,87,-1,88,80,1,-1,1,10,88,-1,89,81,80,-1,80,88,89,-1,144,143,93,-1,93,94,144,-1,94,93,92,-1,92,95,94,-1,87,93,143,-1,143,141,87,-1,86,92,93,-1,93,87,86,-1,69,72,144,-1,144,142,69,-1,142,144,94,-1,94,90,142,-1,91,90,94,-1,94,95,91,-1,100,98,99,-1,99,101,100,-1,95,92,98,-1,98,100,95,-1,85,99,98,-1,98,84,85,-1,84,98,92,-1,92,86,84,-1,96,100,101,-1,101,97,96,-1,91,95,100,-1,100,96,91,-1,81,89,85,-1,106,104,28,-1,28,31,106,-1,107,105,104,-1,104,106,107,-1,101,99,105,-1,105,107,101,-1,10,28,104,-1,104,88,10,-1,88,104,105,-1,105,89,88,-1,89,105,99,-1,99,85,89,-1,102,106,31,-1,31,25,102,-1,103,107,106,-1,106,102,103,-1,97,101,107,-1,107,103,97,-1,145,142,90,-1,90,108,145,-1,111,103,102,-1,102,110,111,-1,146,145,108,-1,108,112,146,-1,112,108,109,-1,109,113,112,-1,108,90,114,-1,114,109,108,-1,97,103,115,-1,116,115,103,-1,103,111,116,-1,116,109,114,-1,114,115,116,-1,118,111,110,-1,110,117,118,-1,119,116,111,-1,111,118,119,-1,113,109,116,-1,116,119,113,-1,147,146,112,-1,112,120,147,-1,120,112,113,-1,113,121,120,-1,123,118,117,-1,117,122,123,-1,121,113,119,-1,119,124,121,-1,148,147,120,-1,120,125,148,-1,125,120,121,-1,121,126,125,-1,128,123,122,-1,122,127,128,-1,129,124,123,-1,123,128,129,-1,126,121,124,-1,124,129,126,-1,149,148,125,-1,125,130,149,-1,130,125,126,-1,126,131,130,-1,133,128,127,-1,127,132,133,-1,134,129,128,-1,128,133,134,-1,131,126,129,-1,129,134,131,-1,135,96,97,-1,97,136,135,-1,137,91,96,-1,96,135,137,-1,138,114,91,-1,91,137,138,-1,136,97,115,-1,115,139,136,-1,139,115,114,-1,114,138,139,-1,81,84,82,-1,81,85,84,-1,91,114,90,-1,25,110,102,-1,142,145,69,-1,140,141,67,-1,67,65,140,-1,141,143,79,-1,79,67,141,-1,143,144,72,-1,72,79,143,-1,118,123,124,-1,124,119,118,-1,135,139,138,-1,138,137,135,-1,135,136,139,-1,25,35,110,-1,117,110,35,-1,35,42,117,-1,47,122,117,-1,117,42,47,-1,127,122,47,-1,47,52,127,-1,132,127,52,-1,52,57,132,-1,69,145,74,-1,75,74,145,-1,145,146,75,-1,76,75,146,-1,146,147,76,-1,77,76,147,-1,147,148,77,-1,78,77,148,-1,148,149,78,-1,57,78,149,-1,149,132,57,-1,58,55,78,-1,78,57,58,-1,59,56,55,-1,55,58,59,-1,132,149,130,-1,130,133,132,-1,133,130,131,-1,131,134,133,-1,151,150,155,-1,155,156,151,-1,150,152,157,-1,157,155,150,-1,152,153,158,-1,158,157,152,-1,153,154,159,-1,159,158,153,-1,160,161,162,-1,162,163,160,-1,154,160,163,-1,163,159,154,-1,168,164,151,-1,151,156,168,-1,169,165,164,-1,164,168,169,-1,170,166,165,-1,165,169,170,-1,171,167,166,-1,166,170,171,-1,162,161,172,-1,172,173,162,-1,173,172,167,-1,167,171,173,-1,4,3,158,-1,158,159,4,-1,66,4,159,-1,159,163,66,-1,0,1,156,-1,156,155,0,-1,2,0,155,-1,155,157,2,-1,3,2,157,-1,157,158,3,-1,65,66,163,-1,163,162,65,-1,82,83,171,-1,171,170,82,-1,83,140,173,-1,173,171,83,-1,1,80,168,-1,168,156,1,-1,80,81,169,-1,169,168,80,-1,81,82,170,-1,170,169,81,-1,140,65,162,-1,162,173,140,-1]
IndexedFaceSet135.creaseAngle = 3.14159
IndexedFaceSet135.texCoordIndex = [2,3,0,-1,0,1,2,-1,3,6,4,-1,4,5,3,-1,3,5,0,-1,20,21,18,-1,18,19,20,-1,21,23,22,-1,22,18,21,-1,26,27,24,-1,24,25,26,-1,29,26,25,-1,25,28,29,-1,27,26,30,-1,30,31,27,-1,26,29,32,-1,32,30,26,-1,24,35,33,-1,33,34,24,-1,25,24,34,-1,34,36,25,-1,25,36,37,-1,37,28,25,-1,40,41,38,-1,38,39,40,-1,41,29,28,-1,28,38,41,-1,41,40,42,-1,42,43,41,-1,29,41,43,-1,43,32,29,-1,39,38,44,-1,44,45,39,-1,38,28,37,-1,37,44,38,-1,23,42,22,-1,48,162,161,-1,161,47,48,-1,49,51,50,-1,50,46,49,-1,51,40,39,-1,39,50,51,-1,163,48,164,-1,164,181,163,-1,51,49,18,-1,18,22,51,-1,40,51,22,-1,22,42,40,-1,47,166,165,-1,165,53,47,-1,46,50,54,-1,54,52,46,-1,50,39,45,-1,45,54,50,-1,36,34,55,-1,55,56,36,-1,52,54,57,-1,57,58,52,-1,56,55,59,-1,59,60,56,-1,62,56,60,-1,60,61,62,-1,63,36,56,-1,56,62,63,-1,45,64,54,-1,54,64,65,-1,65,57,54,-1,63,62,65,-1,65,64,63,-1,58,57,66,-1,66,67,58,-1,57,65,68,-1,68,66,57,-1,65,62,61,-1,61,68,65,-1,60,59,69,-1,69,70,60,-1,61,60,70,-1,70,71,61,-1,67,66,72,-1,72,73,67,-1,68,61,71,-1,71,74,68,-1,70,69,75,-1,75,76,70,-1,71,70,76,-1,76,77,71,-1,73,72,78,-1,78,79,73,-1,72,74,80,-1,80,78,72,-1,74,71,77,-1,77,80,74,-1,76,75,81,-1,81,82,76,-1,77,76,82,-1,82,83,77,-1,79,78,84,-1,84,85,79,-1,78,80,86,-1,86,84,78,-1,80,77,83,-1,83,86,80,-1,45,44,87,-1,87,88,45,-1,44,37,89,-1,89,87,44,-1,37,63,90,-1,90,89,37,-1,64,45,88,-1,88,91,64,-1,63,64,91,-1,91,90,63,-1,7,2,1,-1,23,43,42,-1,37,36,63,-1,53,167,168,-1,34,33,55,-1,9,4,6,-1,6,8,9,-1,93,27,31,-1,31,92,93,-1,35,24,27,-1,27,93,35,-1,74,72,66,-1,66,68,74,-1,90,91,87,-1,87,89,90,-1,87,91,88,-1,10,11,12,-1,12,13,10,-1,14,15,11,-1,11,16,14,-1,11,10,16,-1,94,95,169,-1,169,170,94,-1,96,97,95,-1,95,94,96,-1,98,101,99,-1,99,100,98,-1,100,99,102,-1,102,103,100,-1,104,99,101,-1,101,105,104,-1,106,102,99,-1,99,104,106,-1,33,35,98,-1,98,107,33,-1,107,98,100,-1,100,108,107,-1,109,108,100,-1,100,103,109,-1,110,113,111,-1,111,112,110,-1,103,102,113,-1,113,110,103,-1,114,111,113,-1,113,115,114,-1,115,113,102,-1,102,106,115,-1,116,110,112,-1,112,117,116,-1,109,103,110,-1,110,116,109,-1,97,96,114,-1,118,119,48,-1,48,47,118,-1,120,121,119,-1,119,118,120,-1,112,111,121,-1,121,120,112,-1,171,48,119,-1,119,94,171,-1,94,119,121,-1,121,96,94,-1,96,121,111,-1,111,114,96,-1,122,118,47,-1,47,53,122,-1,123,120,118,-1,118,122,123,-1,117,112,120,-1,120,123,117,-1,124,107,108,-1,108,125,124,-1,126,123,122,-1,122,127,126,-1,128,124,125,-1,125,129,128,-1,129,125,130,-1,130,131,129,-1,125,108,132,-1,132,130,125,-1,117,123,133,-1,134,133,123,-1,123,126,134,-1,134,130,132,-1,132,133,134,-1,135,126,127,-1,127,136,135,-1,137,134,126,-1,126,135,137,-1,131,130,134,-1,134,137,131,-1,138,128,129,-1,129,139,138,-1,139,129,131,-1,131,140,139,-1,141,135,136,-1,136,142,141,-1,140,131,137,-1,137,143,140,-1,144,138,139,-1,139,145,144,-1,145,139,140,-1,140,146,145,-1,147,141,142,-1,142,148,147,-1,149,143,141,-1,141,147,149,-1,146,140,143,-1,143,149,146,-1,150,144,145,-1,145,151,150,-1,151,145,146,-1,146,152,151,-1,153,147,148,-1,148,154,153,-1,155,149,147,-1,147,153,155,-1,152,146,149,-1,149,155,152,-1,156,116,117,-1,117,157,156,-1,158,109,116,-1,116,156,158,-1,159,132,109,-1,109,158,159,-1,157,117,133,-1,133,160,157,-1,160,133,132,-1,132,159,160,-1,17,13,12,-1,97,114,115,-1,109,132,108,-1,53,127,122,-1,107,124,33,-1,15,14,9,-1,9,8,15,-1,105,101,93,-1,93,92,105,-1,101,98,35,-1,35,93,101,-1,135,141,143,-1,143,137,135,-1,156,160,159,-1,159,158,156,-1,156,157,160,-1,53,172,127,-1,136,127,173,-1,173,174,136,-1,176,142,136,-1,136,175,176,-1,148,142,177,-1,177,178,148,-1,154,148,179,-1,179,180,154,-1,33,124,55,-1,59,55,124,-1,124,128,59,-1,69,59,128,-1,128,138,69,-1,75,69,138,-1,138,144,75,-1,81,75,144,-1,144,150,81,-1,85,81,150,-1,150,182,85,-1,84,82,81,-1,81,85,84,-1,86,83,82,-1,82,84,86,-1,154,150,151,-1,151,153,154,-1,153,151,152,-1,152,155,153,-1,185,186,183,-1,183,184,185,-1,186,188,187,-1,187,183,186,-1,188,190,189,-1,189,187,188,-1,190,192,191,-1,191,189,190,-1,195,196,193,-1,193,194,195,-1,192,195,194,-1,194,191,192,-1,197,198,185,-1,185,184,197,-1,199,200,198,-1,198,197,199,-1,201,202,200,-1,200,199,201,-1,203,204,202,-1,202,201,203,-1,193,196,205,-1,205,206,193,-1,206,205,204,-1,204,203,206,-1,3,2,189,-1,189,191,3,-1,6,3,191,-1,191,194,6,-1,207,208,184,-1,184,183,207,-1,7,207,183,-1,183,187,7,-1,2,7,187,-1,187,189,2,-1,8,6,194,-1,194,193,8,-1,12,11,203,-1,203,201,12,-1,11,15,206,-1,206,203,11,-1,208,209,197,-1,197,184,208,-1,209,17,199,-1,199,197,209,-1,17,12,201,-1,201,199,17,-1,15,8,193,-1,193,206,15,-1]
Coordinate136 = x3d.Coordinate()

IndexedFaceSet135.coord = Coordinate136
TextureCoordinate137 = x3d.TextureCoordinate()

IndexedFaceSet135.texCoord = TextureCoordinate137

Shape131.geometry = IndexedFaceSet135

Transform130.children.append(Shape131)

HAnimSegment129.children.append(Transform130)

HAnimJoint128.children.append(HAnimSegment129)
HAnimJoint138 = x3d.HAnimJoint()
HAnimJoint138.name = "skullbase"
HAnimJoint138.DEF = "hanim_skullbase"
HAnimJoint138.center = [0,57.43,-0.6863]
HAnimJoint138.ulimit = [0,0,0]
HAnimJoint138.llimit = [0,0,0]
HAnimSegment139 = x3d.HAnimSegment()
HAnimSegment139.name = "skull"
HAnimSegment139.DEF = "hanim_skull"
Transform140 = x3d.Transform()
Transform140.translation = [0,57.43,-0.6863]
Shape141 = x3d.Shape()
Appearance142 = x3d.Appearance()
Material143 = x3d.Material()
Material143.diffuseColor = [0.588,0.588,0.588]

Appearance142.material = Material143
ImageTexture144 = x3d.ImageTexture()
ImageTexture144.USE = "Annex01JinTextureAtlas"

Appearance142.texture = ImageTexture144

Shape141.appearance = Appearance142
IndexedFaceSet145 = x3d.IndexedFaceSet()
IndexedFaceSet145.coordIndex = [58,44,47,-1,47,49,58,-1,49,60,59,-1,59,1,49,-1,56,48,47,-1,47,44,56,-1,50,51,59,-1,59,60,50,-1,173,168,58,-1,58,49,173,-1,171,173,49,-1,49,1,171,-1,14,12,18,-1,18,15,14,-1,162,160,14,-1,14,15,162,-1,16,57,33,-1,21,18,12,-1,18,79,19,-1,80,20,19,-1,11,10,79,-1,18,21,79,-1,11,79,21,-1,21,12,78,-1,11,21,22,-1,321,345,320,-1,322,323,346,-1,80,25,24,-1,24,20,80,-1,26,38,24,-1,23,13,38,-1,20,77,18,-1,18,19,20,-1,38,29,30,-1,30,23,38,-1,27,30,29,-1,27,28,30,-1,30,28,23,-1,33,31,16,-1,31,37,16,-1,28,34,23,-1,17,35,36,-1,36,28,17,-1,33,36,35,-1,17,32,35,-1,32,33,35,-1,33,34,36,-1,36,34,28,-1,10,19,79,-1,4,40,37,-1,40,42,41,-1,40,41,37,-1,40,4,42,-1,56,43,4,-1,4,46,56,-1,45,43,56,-1,56,44,45,-1,43,45,4,-1,48,56,46,-1,46,3,48,-1,50,60,3,-1,51,50,3,-1,3,2,51,-1,58,168,52,-1,52,168,170,-1,61,52,170,-1,4,45,52,-1,52,61,4,-1,52,45,44,-1,44,58,52,-1,61,170,53,-1,170,165,39,-1,39,53,170,-1,4,61,53,-1,53,42,4,-1,53,39,41,-1,41,42,53,-1,165,57,39,-1,13,23,54,-1,16,37,57,-1,41,39,57,-1,37,41,57,-1,57,165,166,-1,54,166,13,-1,33,57,34,-1,34,57,54,-1,34,54,23,-1,166,162,55,-1,55,162,15,-1,77,55,15,-1,15,18,77,-1,166,77,13,-1,77,166,55,-1,13,77,24,-1,24,38,13,-1,20,24,77,-1,54,57,166,-1,47,60,49,-1,48,3,47,-1,3,60,47,-1,3,63,2,-1,72,62,63,-1,3,65,63,-1,3,46,64,-1,64,66,3,-1,6,66,64,-1,3,66,65,-1,6,73,8,-1,8,73,67,-1,6,75,73,-1,5,71,73,-1,73,75,5,-1,6,70,75,-1,64,46,69,-1,75,70,69,-1,75,69,344,-1,2,63,62,-1,8,66,6,-1,63,8,72,-1,9,74,71,-1,68,74,9,-1,74,8,67,-1,68,72,74,-1,72,8,74,-1,67,71,74,-1,67,73,71,-1,65,8,63,-1,65,66,8,-1,70,6,64,-1,70,64,69,-1,4,0,344,-1,69,46,4,-1,69,4,344,-1,76,344,0,-1,5,76,0,-1,5,75,76,-1,75,344,76,-1,133,125,123,-1,123,120,133,-1,125,1,59,-1,59,134,125,-1,131,120,123,-1,123,124,131,-1,126,134,59,-1,59,51,126,-1,172,125,133,-1,133,167,172,-1,171,1,125,-1,125,172,171,-1,14,91,94,-1,94,12,14,-1,161,91,14,-1,14,160,161,-1,109,132,92,-1,12,94,97,-1,95,149,94,-1,95,96,150,-1,149,88,89,-1,149,97,94,-1,97,149,89,-1,78,12,97,-1,98,97,89,-1,325,348,324,-1,354,326,327,-1,150,96,100,-1,100,101,150,-1,100,114,102,-1,114,90,99,-1,96,95,94,-1,94,148,96,-1,114,99,106,-1,106,105,114,-1,105,106,103,-1,106,104,103,-1,99,104,106,-1,92,107,109,-1,92,113,107,-1,99,110,104,-1,93,104,112,-1,112,111,93,-1,111,112,109,-1,111,108,93,-1,111,109,108,-1,112,110,109,-1,104,110,112,-1,149,95,88,-1,113,116,83,-1,117,118,116,-1,113,117,116,-1,118,83,116,-1,131,122,83,-1,83,119,131,-1,121,120,131,-1,131,119,121,-1,83,121,119,-1,124,82,122,-1,122,131,124,-1,82,134,126,-1,51,2,82,-1,82,126,51,-1,127,167,133,-1,169,167,127,-1,169,127,135,-1,83,135,127,-1,127,121,83,-1,127,133,120,-1,120,121,127,-1,128,169,135,-1,169,128,115,-1,115,163,169,-1,83,118,128,-1,128,135,83,-1,128,118,117,-1,117,115,128,-1,115,132,163,-1,129,99,90,-1,132,113,92,-1,132,115,117,-1,132,117,113,-1,164,163,132,-1,90,164,129,-1,110,132,109,-1,129,132,110,-1,99,129,110,-1,130,161,164,-1,91,161,130,-1,148,94,91,-1,91,130,148,-1,90,148,164,-1,130,164,148,-1,90,114,100,-1,100,148,90,-1,148,100,96,-1,164,132,129,-1,125,134,123,-1,123,82,124,-1,123,134,82,-1,2,136,82,-1,136,62,72,-1,136,138,82,-1,82,139,137,-1,137,122,82,-1,137,139,85,-1,138,139,82,-1,87,144,85,-1,140,144,87,-1,144,146,85,-1,84,146,144,-1,144,143,84,-1,146,142,85,-1,141,122,137,-1,141,142,146,-1,347,141,146,-1,62,136,2,-1,85,139,87,-1,72,87,136,-1,143,145,9,-1,9,145,68,-1,145,140,87,-1,68,145,72,-1,72,145,87,-1,145,143,140,-1,143,144,140,-1,136,87,138,-1,87,139,138,-1,137,85,142,-1,141,137,142,-1,347,81,83,-1,83,122,141,-1,347,83,141,-1,81,347,147,-1,81,147,84,-1,147,146,84,-1,147,347,146,-1,162,166,152,-1,151,160,162,-1,162,152,151,-1,152,166,165,-1,165,154,152,-1,154,165,170,-1,170,156,154,-1,152,154,155,-1,155,151,152,-1,156,153,155,-1,155,154,156,-1,173,156,170,-1,170,168,173,-1,171,153,156,-1,156,173,171,-1,157,164,161,-1,151,157,161,-1,161,160,151,-1,157,158,163,-1,163,164,157,-1,158,159,169,-1,169,163,158,-1,157,151,155,-1,155,158,157,-1,159,158,155,-1,155,153,159,-1,172,167,169,-1,169,159,172,-1,171,172,159,-1,159,153,171,-1,355,237,223,-1,174,236,237,-1,236,174,175,-1,179,238,176,-1,179,176,177,-1,179,177,178,-1,178,174,179,-1,174,178,175,-1,180,226,236,-1,238,180,236,-1,180,230,226,-1,237,236,223,-1,223,236,218,-1,225,355,223,-1,223,224,225,-1,328,329,239,-1,330,331,350,-1,228,227,219,-1,219,222,228,-1,236,226,218,-1,174,237,0,-1,0,237,355,-1,0,179,174,-1,318,355,225,-1,220,228,222,-1,221,228,220,-1,5,0,355,-1,218,182,223,-1,183,223,182,-1,181,183,185,-1,181,185,242,-1,213,212,244,-1,244,246,213,-1,213,246,245,-1,245,214,213,-1,245,247,184,-1,184,214,245,-1,214,184,206,-1,206,207,214,-1,217,319,225,-1,225,224,217,-1,183,181,217,-1,217,224,183,-1,224,223,183,-1,226,209,218,-1,218,209,184,-1,182,185,183,-1,218,184,182,-1,207,208,232,-1,232,214,207,-1,232,215,214,-1,209,206,184,-1,186,192,190,-1,190,188,186,-1,197,192,208,-1,208,207,197,-1,190,222,219,-1,219,188,190,-1,194,195,190,-1,226,189,209,-1,187,189,226,-1,192,186,208,-1,191,216,205,-1,196,205,216,-1,195,196,216,-1,196,195,194,-1,209,189,198,-1,199,197,207,-1,207,206,199,-1,233,234,197,-1,197,199,233,-1,209,198,199,-1,199,206,209,-1,233,199,198,-1,198,200,233,-1,248,194,202,-1,201,205,250,-1,248,249,196,-1,196,194,248,-1,196,249,250,-1,250,205,196,-1,234,203,197,-1,203,192,197,-1,194,190,202,-1,200,198,189,-1,189,204,200,-1,202,190,192,-1,202,192,203,-1,205,210,191,-1,210,205,201,-1,220,222,193,-1,204,189,187,-1,187,210,204,-1,210,201,204,-1,210,187,191,-1,195,211,190,-1,195,193,211,-1,193,222,211,-1,211,222,190,-1,215,212,213,-1,213,214,215,-1,230,187,226,-1,230,191,187,-1,229,221,230,-1,229,228,221,-1,9,355,318,-1,5,355,71,-1,71,355,9,-1,231,247,185,-1,182,231,185,-1,184,231,182,-1,184,247,231,-1,238,230,180,-1,230,221,191,-1,221,235,191,-1,191,235,216,-1,221,220,235,-1,193,235,220,-1,216,235,193,-1,193,195,216,-1,250,249,233,-1,203,234,248,-1,234,233,249,-1,250,233,200,-1,249,248,234,-1,243,241,240,-1,241,243,247,-1,204,201,250,-1,200,204,250,-1,203,248,202,-1,247,243,242,-1,247,242,185,-1,332,333,349,-1,334,335,7,-1,292,304,353,-1,304,303,251,-1,252,251,303,-1,253,305,256,-1,254,253,256,-1,256,251,255,-1,255,254,256,-1,252,255,251,-1,303,295,257,-1,303,257,305,-1,295,298,257,-1,292,303,304,-1,288,303,292,-1,294,352,292,-1,292,353,294,-1,336,337,293,-1,306,338,339,-1,296,291,219,-1,219,227,296,-1,288,295,303,-1,81,304,251,-1,353,304,81,-1,251,256,81,-1,294,353,317,-1,291,296,289,-1,289,296,290,-1,353,81,84,-1,292,258,288,-1,258,292,259,-1,261,259,181,-1,242,261,181,-1,285,309,244,-1,244,212,285,-1,285,286,308,-1,308,309,285,-1,308,286,260,-1,260,310,308,-1,286,281,280,-1,280,260,286,-1,217,352,294,-1,294,319,217,-1,259,352,217,-1,217,181,259,-1,259,292,352,-1,288,282,295,-1,260,282,288,-1,259,261,258,-1,258,260,288,-1,281,286,232,-1,232,208,281,-1,286,215,232,-1,260,280,282,-1,186,188,264,-1,264,266,186,-1,271,281,208,-1,208,266,271,-1,264,188,219,-1,219,291,264,-1,264,269,268,-1,282,263,295,-1,295,263,262,-1,208,186,266,-1,279,287,265,-1,287,279,270,-1,287,270,269,-1,268,269,270,-1,272,263,282,-1,273,280,281,-1,281,271,273,-1,300,273,271,-1,271,301,300,-1,282,280,273,-1,273,272,282,-1,300,274,272,-1,272,273,300,-1,276,268,311,-1,313,279,275,-1,311,268,270,-1,270,312,311,-1,270,279,313,-1,313,312,270,-1,271,277,301,-1,271,266,277,-1,276,264,268,-1,274,278,263,-1,263,272,274,-1,266,264,276,-1,277,266,276,-1,265,283,279,-1,275,279,283,-1,267,291,289,-1,278,283,262,-1,262,263,278,-1,278,275,283,-1,265,262,283,-1,264,284,269,-1,284,267,269,-1,284,291,267,-1,264,291,284,-1,285,212,215,-1,215,286,285,-1,295,262,298,-1,262,265,298,-1,298,290,297,-1,290,296,297,-1,317,353,9,-1,143,353,84,-1,9,353,143,-1,261,310,299,-1,261,299,258,-1,258,299,260,-1,299,310,260,-1,257,298,305,-1,265,290,298,-1,265,302,290,-1,287,302,265,-1,302,289,290,-1,289,302,267,-1,287,269,267,-1,267,302,287,-1,300,312,313,-1,311,301,277,-1,312,300,301,-1,274,300,313,-1,301,311,312,-1,240,307,243,-1,310,243,307,-1,313,275,278,-1,313,278,274,-1,276,311,277,-1,242,243,310,-1,261,242,310,-1,351,340,341,-1,86,342,343,-1,244,314,315,-1,315,246,244,-1,246,315,247,-1,247,245,246,-1,244,309,316,-1,316,314,244,-1,309,308,310,-1,310,316,309,-1,175,176,238,-1,238,236,175,-1,177,176,175,-1,175,178,177,-1,252,303,305,-1,305,253,252,-1,254,255,252,-1,252,253,254,-1,318,225,319,-1,319,9,318,-1,317,9,319,-1,319,294,317,-1]
IndexedFaceSet145.creaseAngle = 3.14159
IndexedFaceSet145.texCoordIndex = [0,3,2,-1,2,1,0,-1,1,6,5,-1,5,4,1,-1,7,8,2,-1,2,3,7,-1,9,10,5,-1,5,6,9,-1,11,12,0,-1,0,1,11,-1,13,11,1,-1,1,4,13,-1,14,17,16,-1,16,15,14,-1,18,19,14,-1,14,15,18,-1,22,21,20,-1,23,16,17,-1,16,25,24,-1,27,26,24,-1,29,28,25,-1,16,23,25,-1,29,25,23,-1,31,17,30,-1,29,23,32,-1,33,32,31,-1,33,31,30,-1,27,35,34,-1,34,26,27,-1,37,36,34,-1,39,38,36,-1,26,40,16,-1,16,24,26,-1,36,42,41,-1,41,39,36,-1,43,41,42,-1,43,44,41,-1,41,44,39,-1,20,45,22,-1,45,46,22,-1,44,47,39,-1,48,50,49,-1,49,44,48,-1,20,49,50,-1,48,51,50,-1,51,20,50,-1,20,47,49,-1,49,47,44,-1,28,24,25,-1,53,52,46,-1,52,55,54,-1,52,54,46,-1,52,53,55,-1,7,57,53,-1,53,56,7,-1,58,57,7,-1,7,59,58,-1,57,58,53,-1,8,7,56,-1,56,60,8,-1,9,6,60,-1,10,9,60,-1,60,61,10,-1,0,12,62,-1,62,12,63,-1,64,62,63,-1,53,58,62,-1,62,64,53,-1,62,58,59,-1,59,0,62,-1,64,63,65,-1,63,67,66,-1,66,65,63,-1,53,64,65,-1,65,55,53,-1,65,66,54,-1,54,55,65,-1,67,21,66,-1,38,39,68,-1,22,46,21,-1,54,66,21,-1,46,54,21,-1,21,67,69,-1,68,69,38,-1,20,21,47,-1,47,21,68,-1,47,68,39,-1,69,18,70,-1,70,18,15,-1,40,70,15,-1,15,16,40,-1,69,71,38,-1,71,69,70,-1,38,71,34,-1,34,36,38,-1,26,34,71,-1,68,21,69,-1,2,6,1,-1,8,60,2,-1,60,6,2,-1,74,73,72,-1,77,76,75,-1,74,78,73,-1,74,81,80,-1,80,79,74,-1,82,79,80,-1,74,79,78,-1,82,84,83,-1,83,84,85,-1,82,86,84,-1,87,90,89,-1,89,88,87,-1,92,91,88,-1,80,81,93,-1,88,91,94,-1,86,93,95,-1,72,73,96,-1,83,79,82,-1,73,83,97,-1,100,99,98,-1,103,102,101,-1,99,83,85,-1,104,97,99,-1,97,83,99,-1,105,90,102,-1,105,89,90,-1,107,106,75,-1,107,108,106,-1,109,82,80,-1,109,80,93,-1,112,111,110,-1,93,81,113,-1,93,113,95,-1,114,110,111,-1,115,114,111,-1,87,86,116,-1,86,95,116,-1,117,120,119,-1,119,118,117,-1,120,123,122,-1,122,121,120,-1,124,118,119,-1,119,125,124,-1,126,121,122,-1,122,127,126,-1,128,120,117,-1,117,129,128,-1,130,123,120,-1,120,128,130,-1,14,132,131,-1,131,17,14,-1,133,132,14,-1,14,19,133,-1,136,135,134,-1,17,131,137,-1,139,138,131,-1,139,141,140,-1,138,143,142,-1,138,137,131,-1,137,138,142,-1,30,17,144,-1,145,137,142,-1,144,145,146,-1,30,144,146,-1,140,141,148,-1,148,147,140,-1,148,150,149,-1,150,152,151,-1,141,139,131,-1,131,153,141,-1,150,151,155,-1,155,154,150,-1,154,155,156,-1,155,157,156,-1,151,157,155,-1,134,158,136,-1,134,159,158,-1,151,160,157,-1,161,157,163,-1,163,162,161,-1,162,163,136,-1,162,164,161,-1,162,136,164,-1,163,160,136,-1,157,160,163,-1,138,139,143,-1,159,166,165,-1,168,167,166,-1,159,168,166,-1,167,165,166,-1,124,170,165,-1,165,169,124,-1,171,172,124,-1,124,169,171,-1,165,171,169,-1,125,173,170,-1,170,124,125,-1,173,121,126,-1,127,174,173,-1,173,126,127,-1,175,129,117,-1,176,129,175,-1,176,175,177,-1,165,177,175,-1,175,171,165,-1,175,117,172,-1,172,171,175,-1,178,176,177,-1,176,178,180,-1,180,179,176,-1,165,167,178,-1,178,177,165,-1,178,167,168,-1,168,180,178,-1,180,135,179,-1,181,151,152,-1,135,159,134,-1,135,180,168,-1,135,168,159,-1,182,179,135,-1,152,182,181,-1,160,135,136,-1,181,135,160,-1,151,181,160,-1,183,133,182,-1,132,133,183,-1,153,131,132,-1,132,183,153,-1,152,184,182,-1,183,182,184,-1,152,150,148,-1,148,184,152,-1,184,148,141,-1,182,135,181,-1,120,121,119,-1,119,173,125,-1,119,121,173,-1,72,186,185,-1,187,76,77,-1,186,188,185,-1,185,191,190,-1,190,189,185,-1,190,191,192,-1,188,191,185,-1,194,193,192,-1,195,193,194,-1,193,196,192,-1,197,200,199,-1,199,198,197,-1,200,202,201,-1,203,189,190,-1,204,202,200,-1,205,203,196,-1,96,186,72,-1,192,191,194,-1,97,194,186,-1,207,206,100,-1,101,208,103,-1,206,195,194,-1,104,206,97,-1,97,206,194,-1,208,198,209,-1,198,199,209,-1,187,211,210,-1,211,212,210,-1,190,192,213,-1,203,190,213,-1,216,215,214,-1,217,189,203,-1,205,217,203,-1,215,216,218,-1,215,218,219,-1,220,196,197,-1,220,205,196,-1,18,69,221,-1,222,19,18,-1,18,221,222,-1,221,69,67,-1,67,223,221,-1,223,67,63,-1,63,224,223,-1,221,223,225,-1,225,222,221,-1,224,226,225,-1,225,223,224,-1,11,224,63,-1,63,12,11,-1,13,226,224,-1,224,11,13,-1,227,182,133,-1,222,227,133,-1,133,19,222,-1,227,228,179,-1,179,182,227,-1,228,229,176,-1,176,179,228,-1,227,222,225,-1,225,228,227,-1,229,228,225,-1,225,230,229,-1,128,129,176,-1,176,229,128,-1,130,128,229,-1,229,230,130,-1,233,232,231,-1,235,234,232,-1,234,235,236,-1,239,238,237,-1,239,237,240,-1,239,240,241,-1,241,235,239,-1,235,241,236,-1,243,242,234,-1,238,243,234,-1,243,244,242,-1,232,234,231,-1,231,234,245,-1,246,233,231,-1,231,247,246,-1,247,246,233,-1,231,247,233,-1,248,251,250,-1,250,249,248,-1,234,242,245,-1,235,232,252,-1,252,232,233,-1,252,239,235,-1,253,233,246,-1,254,248,249,-1,255,248,254,-1,256,252,233,-1,245,257,231,-1,258,231,257,-1,261,260,259,-1,261,259,262,-1,263,266,265,-1,265,264,263,-1,263,264,268,-1,268,267,263,-1,268,270,269,-1,269,267,268,-1,267,269,272,-1,272,271,267,-1,273,274,246,-1,246,247,273,-1,258,275,273,-1,273,247,258,-1,247,231,258,-1,278,277,276,-1,276,277,269,-1,279,259,260,-1,276,269,279,-1,271,281,280,-1,280,267,271,-1,280,282,267,-1,277,272,269,-1,284,287,286,-1,286,285,284,-1,288,287,281,-1,281,271,288,-1,286,249,250,-1,250,285,286,-1,290,289,286,-1,278,291,277,-1,292,291,278,-1,287,284,283,-1,295,294,293,-1,296,293,294,-1,289,296,294,-1,296,289,290,-1,277,291,297,-1,298,288,271,-1,271,272,298,-1,299,300,288,-1,288,298,299,-1,277,297,298,-1,298,272,277,-1,299,298,297,-1,297,301,299,-1,303,290,302,-1,305,293,304,-1,303,306,296,-1,296,290,303,-1,296,306,304,-1,304,293,296,-1,300,307,288,-1,307,287,288,-1,290,286,302,-1,301,297,291,-1,291,308,301,-1,302,286,287,-1,309,287,307,-1,293,310,295,-1,310,293,305,-1,254,249,311,-1,308,291,292,-1,292,310,308,-1,310,305,308,-1,310,292,295,-1,289,312,286,-1,289,311,312,-1,311,249,312,-1,312,249,286,-1,282,266,263,-1,263,267,282,-1,313,292,278,-1,313,295,292,-1,314,255,313,-1,314,248,255,-1,315,233,253,-1,256,233,316,-1,316,233,315,-1,317,270,259,-1,279,317,259,-1,269,317,279,-1,269,270,317,-1,238,244,243,-1,313,255,295,-1,255,318,295,-1,295,318,294,-1,255,254,318,-1,311,318,254,-1,294,318,311,-1,311,289,294,-1,304,306,299,-1,307,300,303,-1,300,299,306,-1,304,299,301,-1,306,303,300,-1,321,320,319,-1,320,321,270,-1,308,305,304,-1,301,308,304,-1,307,303,309,-1,270,321,262,-1,270,262,259,-1,252,322,239,-1,252,256,322,-1,231,232,233,-1,232,234,235,-1,236,235,234,-1,237,238,239,-1,240,237,239,-1,239,235,241,-1,241,240,239,-1,236,241,235,-1,234,242,243,-1,234,243,238,-1,242,244,243,-1,231,234,232,-1,245,234,231,-1,246,247,231,-1,231,233,246,-1,233,246,247,-1,233,247,231,-1,323,324,250,-1,250,251,323,-1,245,242,234,-1,252,232,235,-1,233,232,252,-1,235,239,252,-1,246,233,253,-1,324,323,325,-1,325,323,326,-1,233,252,256,-1,231,257,245,-1,257,231,258,-1,329,328,327,-1,330,329,327,-1,331,332,265,-1,265,266,331,-1,331,334,333,-1,333,332,331,-1,333,334,336,-1,336,335,333,-1,334,338,337,-1,337,336,334,-1,273,247,246,-1,246,274,273,-1,258,247,273,-1,273,275,258,-1,258,231,247,-1,341,340,339,-1,336,340,341,-1,328,329,342,-1,342,336,341,-1,338,334,280,-1,280,343,338,-1,334,282,280,-1,336,337,340,-1,284,285,345,-1,345,344,284,-1,346,338,343,-1,343,344,346,-1,345,285,250,-1,250,324,345,-1,345,348,347,-1,340,349,339,-1,339,349,350,-1,283,284,344,-1,353,352,351,-1,352,353,354,-1,352,354,348,-1,347,348,354,-1,355,349,340,-1,356,337,338,-1,338,346,356,-1,357,356,346,-1,346,358,357,-1,340,337,356,-1,356,355,340,-1,357,359,355,-1,355,356,357,-1,361,347,360,-1,363,353,362,-1,360,347,354,-1,354,364,360,-1,354,353,363,-1,363,364,354,-1,346,365,358,-1,346,344,365,-1,361,345,347,-1,359,366,349,-1,349,355,359,-1,344,345,361,-1,365,344,367,-1,351,368,353,-1,362,353,368,-1,369,324,325,-1,366,368,350,-1,350,349,366,-1,366,362,368,-1,351,350,368,-1,345,370,348,-1,370,369,348,-1,370,324,369,-1,345,324,370,-1,331,266,282,-1,282,334,331,-1,339,350,371,-1,350,351,371,-1,371,326,372,-1,326,323,372,-1,253,233,315,-1,316,233,256,-1,315,233,316,-1,329,335,373,-1,329,373,342,-1,342,373,336,-1,373,335,336,-1,243,244,238,-1,351,326,371,-1,351,374,326,-1,352,374,351,-1,374,325,326,-1,325,374,369,-1,352,348,369,-1,369,374,352,-1,357,364,363,-1,360,358,365,-1,364,357,358,-1,359,357,363,-1,358,360,364,-1,319,376,375,-1,335,375,376,-1,363,362,366,-1,363,366,359,-1,367,360,365,-1,330,375,335,-1,329,330,335,-1,239,322,252,-1,322,256,252,-1,265,378,377,-1,377,264,265,-1,264,377,270,-1,270,268,264,-1,265,332,379,-1,379,378,265,-1,332,333,335,-1,335,379,332,-1,380,383,382,-1,382,381,380,-1,384,383,380,-1,380,385,384,-1,380,381,382,-1,382,383,380,-1,384,385,380,-1,380,383,384,-1,253,246,274,-1,274,100,253,-1,253,100,274,-1,274,246,253,-1]
Coordinate146 = x3d.Coordinate()

IndexedFaceSet145.coord = Coordinate146
TextureCoordinate147 = x3d.TextureCoordinate()

IndexedFaceSet145.texCoord = TextureCoordinate147

Shape141.geometry = IndexedFaceSet145

Transform140.children.append(Shape141)

HAnimSegment139.children.append(Transform140)

HAnimJoint138.children.append(HAnimSegment139)

HAnimJoint128.children.append(HAnimJoint138)
HAnimJoint148 = x3d.HAnimJoint()
HAnimJoint148.name = "l_shoulder"
HAnimJoint148.DEF = "hanim_l_shoulder"
HAnimJoint148.center = [5.975,52,-0.1452]
HAnimJoint148.ulimit = [0,0,0]
HAnimJoint148.llimit = [0,0,0]
HAnimSegment149 = x3d.HAnimSegment()
HAnimSegment149.name = "l_upperarm"
HAnimSegment149.DEF = "hanim_l_upperarm"
Transform150 = x3d.Transform()
Transform150.translation = [5.975,52,-0.1452]
Shape151 = x3d.Shape()
Appearance152 = x3d.Appearance()
Material153 = x3d.Material()
Material153.diffuseColor = [0.588,0.588,0.588]

Appearance152.material = Material153
ImageTexture154 = x3d.ImageTexture()
ImageTexture154.USE = "Annex01JinTextureAtlas"

Appearance152.texture = ImageTexture154

Shape151.appearance = Appearance152
IndexedFaceSet155 = x3d.IndexedFaceSet()
IndexedFaceSet155.coordIndex = [2,1,0,-1,3,2,0,-1,4,3,0,-1,0,1,6,-1,6,5,0,-1,1,2,7,-1,7,6,1,-1,2,3,8,-1,8,7,2,-1,3,4,9,-1,9,8,3,-1,4,0,5,-1,5,9,4,-1,5,6,11,-1,11,10,5,-1,6,7,12,-1,12,11,6,-1,7,8,13,-1,13,12,7,-1,8,9,14,-1,14,13,8,-1,9,5,10,-1,10,14,9,-1,10,11,16,-1,16,15,10,-1,11,12,17,-1,17,16,11,-1,12,13,18,-1,18,17,12,-1,13,14,19,-1,19,18,13,-1,14,10,15,-1,15,19,14,-1,36,37,38,-1,35,36,38,-1,39,35,38,-1,21,20,15,-1,15,16,21,-1,22,21,16,-1,16,17,22,-1,23,22,17,-1,17,18,23,-1,24,23,18,-1,18,19,24,-1,20,24,19,-1,19,15,20,-1,26,25,20,-1,20,21,26,-1,27,26,21,-1,21,22,27,-1,28,27,22,-1,22,23,28,-1,29,28,23,-1,23,24,29,-1,25,29,24,-1,24,20,25,-1,31,30,25,-1,25,26,31,-1,32,31,26,-1,26,27,32,-1,33,32,27,-1,27,28,33,-1,34,33,28,-1,28,29,34,-1,30,34,29,-1,29,25,30,-1,36,35,30,-1,30,31,36,-1,37,36,31,-1,31,32,37,-1,38,37,32,-1,32,33,38,-1,39,38,33,-1,33,34,39,-1,35,39,34,-1,34,30,35,-1]
IndexedFaceSet155.creaseAngle = 3.14159
IndexedFaceSet155.texCoordIndex = [2,0,1,-1,3,2,1,-1,61,3,1,-1,1,0,5,-1,5,6,1,-1,0,2,7,-1,7,5,0,-1,2,3,8,-1,8,7,2,-1,25,4,9,-1,9,26,25,-1,4,1,6,-1,6,9,4,-1,6,5,10,-1,10,11,6,-1,5,7,12,-1,12,10,5,-1,7,8,13,-1,13,12,7,-1,27,9,14,-1,14,28,27,-1,9,6,11,-1,11,14,9,-1,11,10,15,-1,15,16,11,-1,10,12,17,-1,17,15,10,-1,12,13,18,-1,18,17,12,-1,29,14,19,-1,19,30,29,-1,14,11,16,-1,16,19,14,-1,54,35,36,-1,53,54,36,-1,37,53,36,-1,20,21,16,-1,16,15,20,-1,22,20,15,-1,15,17,22,-1,23,22,17,-1,17,18,23,-1,24,32,31,-1,31,19,24,-1,21,24,19,-1,19,16,21,-1,40,41,38,-1,38,39,40,-1,43,56,55,-1,55,42,43,-1,45,43,42,-1,42,44,45,-1,47,45,44,-1,44,46,47,-1,41,47,46,-1,46,38,41,-1,48,49,41,-1,41,40,48,-1,50,58,57,-1,57,43,50,-1,51,50,43,-1,43,45,51,-1,52,51,45,-1,45,47,52,-1,49,52,47,-1,47,41,49,-1,34,33,49,-1,49,48,34,-1,35,60,59,-1,59,50,35,-1,36,35,50,-1,50,51,36,-1,37,36,51,-1,51,52,37,-1,33,37,52,-1,52,49,33,-1]
Coordinate156 = x3d.Coordinate()

IndexedFaceSet155.coord = Coordinate156
TextureCoordinate157 = x3d.TextureCoordinate()

IndexedFaceSet155.texCoord = TextureCoordinate157

Shape151.geometry = IndexedFaceSet155

Transform150.children.append(Shape151)

HAnimSegment149.children.append(Transform150)

HAnimJoint148.children.append(HAnimSegment149)
HAnimJoint158 = x3d.HAnimJoint()
HAnimJoint158.name = "l_elbow"
HAnimJoint158.DEF = "hanim_l_elbow"
HAnimJoint158.center = [8.093,40.38,-0.2502]
HAnimJoint158.ulimit = [0,0,0]
HAnimJoint158.llimit = [0,0,0]
HAnimSegment159 = x3d.HAnimSegment()
HAnimSegment159.name = "l_forearm"
HAnimSegment159.DEF = "hanim_l_forearm"
Transform160 = x3d.Transform()
Transform160.translation = [8.093,40.38,-0.2502]
Shape161 = x3d.Shape()
Appearance162 = x3d.Appearance()
Material163 = x3d.Material()
Material163.diffuseColor = [0.588,0.588,0.588]

Appearance162.material = Material163
ImageTexture164 = x3d.ImageTexture()
ImageTexture164.USE = "Annex01JinTextureAtlas"

Appearance162.texture = ImageTexture164

Shape161.appearance = Appearance162
IndexedFaceSet165 = x3d.IndexedFaceSet()
IndexedFaceSet165.coordIndex = [2,1,0,-1,3,2,0,-1,4,3,0,-1,0,1,6,-1,6,5,0,-1,1,2,7,-1,7,6,1,-1,2,3,8,-1,8,7,2,-1,3,4,9,-1,9,8,3,-1,4,0,5,-1,5,9,4,-1,5,6,11,-1,11,10,5,-1,6,7,12,-1,12,11,6,-1,7,8,13,-1,13,12,7,-1,8,9,14,-1,14,13,8,-1,9,5,10,-1,10,14,9,-1,10,11,16,-1,16,15,10,-1,11,12,17,-1,17,16,11,-1,12,13,18,-1,18,17,12,-1,13,14,19,-1,19,18,13,-1,14,10,15,-1,15,19,14,-1,21,22,23,-1,20,21,23,-1,24,20,23,-1,21,20,15,-1,15,16,21,-1,22,21,16,-1,16,17,22,-1,23,22,17,-1,17,18,23,-1,24,23,18,-1,18,19,24,-1,20,24,19,-1,19,15,20,-1]
IndexedFaceSet165.creaseAngle = 3.14159
IndexedFaceSet165.texCoordIndex = [2,25,26,-1,3,2,26,-1,4,3,26,-1,0,1,6,-1,6,5,0,-1,27,2,7,-1,7,28,27,-1,2,3,8,-1,8,7,2,-1,3,4,9,-1,9,8,3,-1,4,0,5,-1,5,9,4,-1,5,6,11,-1,11,10,5,-1,29,7,12,-1,12,30,29,-1,7,8,13,-1,13,12,7,-1,8,9,14,-1,14,13,8,-1,9,5,10,-1,10,14,9,-1,10,11,16,-1,16,15,10,-1,31,12,17,-1,17,32,31,-1,12,13,18,-1,18,17,12,-1,13,14,19,-1,19,18,13,-1,14,10,15,-1,15,19,14,-1,34,22,23,-1,33,34,23,-1,24,33,23,-1,21,20,15,-1,15,16,21,-1,22,36,35,-1,35,17,22,-1,23,22,17,-1,17,18,23,-1,24,23,18,-1,18,19,24,-1,20,24,19,-1,19,15,20,-1]
Coordinate166 = x3d.Coordinate()

IndexedFaceSet165.coord = Coordinate166
TextureCoordinate167 = x3d.TextureCoordinate()

IndexedFaceSet165.texCoord = TextureCoordinate167

Shape161.geometry = IndexedFaceSet165

Transform160.children.append(Shape161)

HAnimSegment159.children.append(Transform160)

HAnimJoint158.children.append(HAnimSegment159)
HAnimJoint168 = x3d.HAnimJoint()
HAnimJoint168.name = "l_radiocarpal"
HAnimJoint168.DEF = "hanim_l_radiocarpal"
HAnimJoint168.center = [7.808,31.46,-0.05849]
HAnimJoint168.ulimit = [0,0,0]
HAnimJoint168.llimit = [0,0,0]
HAnimSegment169 = x3d.HAnimSegment()
HAnimSegment169.name = "l_carpal"
HAnimSegment169.DEF = "hanim_l_carpal"
Transform170 = x3d.Transform()
Transform170.translation = [7.808,31.46,-0.05849]
Shape171 = x3d.Shape()
Appearance172 = x3d.Appearance()
Material173 = x3d.Material()
Material173.diffuseColor = [0.588,0.588,0.588]

Appearance172.material = Material173
ImageTexture174 = x3d.ImageTexture()
ImageTexture174.USE = "Annex01JinTextureAtlas"

Appearance172.texture = ImageTexture174

Shape171.appearance = Appearance172
IndexedFaceSet175 = x3d.IndexedFaceSet()
IndexedFaceSet175.coordIndex = [4,5,0,-1,0,2,4,-1,6,7,3,-1,3,1,6,-1,1,0,5,-1,5,6,1,-1,8,9,5,-1,5,4,8,-1,10,11,7,-1,7,6,10,-1,9,10,6,-1,6,5,9,-1,12,13,9,-1,9,8,12,-1,14,15,11,-1,11,10,14,-1,13,14,10,-1,10,9,13,-1,4,2,16,-1,2,3,7,-1,7,16,2,-1,17,19,18,-1,18,20,17,-1,21,16,7,-1,7,11,21,-1,8,21,12,-1,12,21,11,-1,11,15,12,-1,13,12,15,-1,15,14,13,-1,8,4,19,-1,19,17,8,-1,4,16,18,-1,18,19,4,-1,16,21,20,-1,20,18,16,-1,21,8,17,-1,17,20,21,-1,22,27,23,-1,26,25,24,-1]
IndexedFaceSet175.creaseAngle = 3.14159
IndexedFaceSet175.texCoordIndex = [4,6,5,-1,5,7,4,-1,2,3,1,-1,1,0,2,-1,14,16,15,-1,15,17,14,-1,8,9,6,-1,6,4,8,-1,38,40,39,-1,39,41,38,-1,18,19,36,-1,36,37,18,-1,10,11,9,-1,9,8,10,-1,42,43,40,-1,40,38,42,-1,20,21,19,-1,19,18,20,-1,22,24,23,-1,24,26,25,-1,25,23,24,-1,27,29,28,-1,28,30,27,-1,31,23,25,-1,25,32,31,-1,33,31,34,-1,34,31,32,-1,32,35,34,-1,20,34,35,-1,35,21,20,-1,8,4,12,-1,12,13,8,-1,22,23,28,-1,28,29,22,-1,23,31,30,-1,30,28,23,-1,31,33,27,-1,27,30,31,-1,14,24,26,-1,14,16,24,-1]
Coordinate176 = x3d.Coordinate()

IndexedFaceSet175.coord = Coordinate176
TextureCoordinate177 = x3d.TextureCoordinate()

IndexedFaceSet175.texCoord = TextureCoordinate177

Shape171.geometry = IndexedFaceSet175

Transform170.children.append(Shape171)

HAnimSegment169.children.append(Transform170)

HAnimJoint168.children.append(HAnimSegment169)

HAnimJoint158.children.append(HAnimJoint168)

HAnimJoint148.children.append(HAnimJoint158)

HAnimJoint128.children.append(HAnimJoint148)
HAnimJoint178 = x3d.HAnimJoint()
HAnimJoint178.name = "r_shoulder"
HAnimJoint178.DEF = "hanim_r_shoulder"
HAnimJoint178.center = [-5.975,52,-0.1452]
HAnimJoint178.ulimit = [0,0,0]
HAnimJoint178.llimit = [0,0,0]
HAnimSegment179 = x3d.HAnimSegment()
HAnimSegment179.name = "r_upperarm"
HAnimSegment179.DEF = "hanim_r_upperarm"
Transform180 = x3d.Transform()
Transform180.translation = [-5.975,52,-0.1452]
Shape181 = x3d.Shape()
Appearance182 = x3d.Appearance()
Material183 = x3d.Material()
Material183.diffuseColor = [0.588,0.588,0.588]

Appearance182.material = Material183
ImageTexture184 = x3d.ImageTexture()
ImageTexture184.USE = "Annex01JinTextureAtlas"

Appearance182.texture = ImageTexture184

Shape181.appearance = Appearance182
IndexedFaceSet185 = x3d.IndexedFaceSet()
IndexedFaceSet185.coordIndex = [0,1,2,-1,0,2,3,-1,4,0,3,-1,0,5,6,-1,6,1,0,-1,1,6,7,-1,7,2,1,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,9,4,3,-1,4,9,5,-1,5,0,4,-1,5,10,11,-1,11,6,5,-1,6,11,12,-1,12,7,6,-1,7,12,13,-1,13,8,7,-1,8,13,14,-1,14,9,8,-1,9,14,10,-1,10,5,9,-1,10,15,16,-1,16,11,10,-1,11,16,17,-1,17,12,11,-1,12,17,18,-1,18,13,12,-1,13,18,19,-1,19,14,13,-1,14,19,15,-1,15,10,14,-1,38,37,36,-1,38,36,35,-1,39,38,35,-1,21,16,15,-1,15,20,21,-1,22,17,16,-1,16,21,22,-1,23,18,17,-1,17,22,23,-1,24,19,18,-1,18,23,24,-1,20,15,19,-1,19,24,20,-1,26,21,20,-1,20,25,26,-1,27,22,21,-1,21,26,27,-1,28,23,22,-1,22,27,28,-1,29,24,23,-1,23,28,29,-1,25,20,24,-1,24,29,25,-1,31,26,25,-1,25,30,31,-1,32,27,26,-1,26,31,32,-1,33,28,27,-1,27,32,33,-1,34,29,28,-1,28,33,34,-1,30,25,29,-1,29,34,30,-1,36,31,30,-1,30,35,36,-1,37,32,31,-1,31,36,37,-1,38,33,32,-1,32,37,38,-1,39,34,33,-1,33,38,39,-1,35,30,34,-1,34,39,35,-1]
IndexedFaceSet185.creaseAngle = 3.14159
IndexedFaceSet185.texCoordIndex = [1,0,2,-1,1,2,3,-1,61,1,3,-1,1,6,5,-1,5,0,1,-1,0,5,7,-1,7,2,0,-1,2,7,8,-1,8,3,2,-1,25,26,9,-1,9,4,25,-1,4,9,6,-1,6,1,4,-1,6,11,10,-1,10,5,6,-1,5,10,12,-1,12,7,5,-1,7,12,13,-1,13,8,7,-1,27,28,14,-1,14,9,27,-1,9,14,11,-1,11,6,9,-1,11,16,15,-1,15,10,11,-1,10,15,17,-1,17,12,10,-1,12,17,18,-1,18,13,12,-1,29,30,19,-1,19,14,29,-1,14,19,16,-1,16,11,14,-1,36,35,54,-1,36,54,53,-1,37,36,53,-1,20,15,16,-1,16,21,20,-1,22,17,15,-1,15,20,22,-1,23,18,17,-1,17,22,23,-1,24,19,31,-1,31,32,24,-1,21,16,19,-1,19,24,21,-1,40,39,38,-1,38,41,40,-1,43,42,55,-1,55,56,43,-1,45,44,42,-1,42,43,45,-1,47,46,44,-1,44,45,47,-1,41,38,46,-1,46,47,41,-1,48,40,41,-1,41,49,48,-1,50,43,57,-1,57,58,50,-1,51,45,43,-1,43,50,51,-1,52,47,45,-1,45,51,52,-1,49,41,47,-1,47,52,49,-1,34,48,49,-1,49,33,34,-1,35,50,59,-1,59,60,35,-1,36,51,50,-1,50,35,36,-1,37,52,51,-1,51,36,37,-1,33,49,52,-1,52,37,33,-1]
Coordinate186 = x3d.Coordinate()

IndexedFaceSet185.coord = Coordinate186
TextureCoordinate187 = x3d.TextureCoordinate()

IndexedFaceSet185.texCoord = TextureCoordinate187

Shape181.geometry = IndexedFaceSet185

Transform180.children.append(Shape181)

HAnimSegment179.children.append(Transform180)

HAnimJoint178.children.append(HAnimSegment179)
HAnimJoint188 = x3d.HAnimJoint()
HAnimJoint188.name = "r_elbow"
HAnimJoint188.DEF = "hanim_r_elbow"
HAnimJoint188.center = [-8.093,40.38,-0.2502]
HAnimJoint188.ulimit = [0,0,0]
HAnimJoint188.llimit = [0,0,0]
HAnimSegment189 = x3d.HAnimSegment()
HAnimSegment189.name = "r_forearm"
HAnimSegment189.DEF = "hanim_r_forearm"
Transform190 = x3d.Transform()
Transform190.translation = [-8.093,40.38,-0.2502]
Shape191 = x3d.Shape()
Appearance192 = x3d.Appearance()
Material193 = x3d.Material()
Material193.diffuseColor = [0.588,0.588,0.588]

Appearance192.material = Material193
ImageTexture194 = x3d.ImageTexture()
ImageTexture194.USE = "Annex01JinTextureAtlas"

Appearance192.texture = ImageTexture194

Shape191.appearance = Appearance192
IndexedFaceSet195 = x3d.IndexedFaceSet()
IndexedFaceSet195.coordIndex = [0,1,2,-1,0,2,3,-1,4,0,3,-1,0,5,6,-1,6,1,0,-1,1,6,7,-1,7,2,1,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,9,4,3,-1,4,9,5,-1,5,0,4,-1,5,10,11,-1,11,6,5,-1,6,11,12,-1,12,7,6,-1,7,12,13,-1,13,8,7,-1,8,13,14,-1,14,9,8,-1,9,14,10,-1,10,5,9,-1,10,15,16,-1,16,11,10,-1,11,16,17,-1,17,12,11,-1,12,17,18,-1,18,13,12,-1,13,18,19,-1,19,14,13,-1,14,19,15,-1,15,10,14,-1,23,22,21,-1,23,21,20,-1,24,23,20,-1,21,16,15,-1,15,20,21,-1,22,17,16,-1,16,21,22,-1,23,18,17,-1,17,22,23,-1,24,19,18,-1,18,23,24,-1,20,15,19,-1,19,24,20,-1]
IndexedFaceSet195.creaseAngle = 3.14159
IndexedFaceSet195.texCoordIndex = [26,25,2,-1,26,2,3,-1,4,26,3,-1,0,5,6,-1,6,1,0,-1,27,28,7,-1,7,2,27,-1,2,7,8,-1,8,3,2,-1,3,8,9,-1,9,4,3,-1,4,9,5,-1,5,0,4,-1,5,10,11,-1,11,6,5,-1,29,30,12,-1,12,7,29,-1,7,12,13,-1,13,8,7,-1,8,13,14,-1,14,9,8,-1,9,14,10,-1,10,5,9,-1,10,15,16,-1,16,11,10,-1,31,32,17,-1,17,12,31,-1,12,17,18,-1,18,13,12,-1,13,18,19,-1,19,14,13,-1,14,19,15,-1,15,10,14,-1,23,22,34,-1,23,34,33,-1,24,23,33,-1,21,16,15,-1,15,20,21,-1,22,17,35,-1,35,36,22,-1,23,18,17,-1,17,22,23,-1,24,19,18,-1,18,23,24,-1,20,15,19,-1,19,24,20,-1]
Coordinate196 = x3d.Coordinate()

IndexedFaceSet195.coord = Coordinate196
TextureCoordinate197 = x3d.TextureCoordinate()

IndexedFaceSet195.texCoord = TextureCoordinate197

Shape191.geometry = IndexedFaceSet195

Transform190.children.append(Shape191)

HAnimSegment189.children.append(Transform190)

HAnimJoint188.children.append(HAnimSegment189)
HAnimJoint198 = x3d.HAnimJoint()
HAnimJoint198.name = "r_radiocarpal"
HAnimJoint198.DEF = "hanim_r_radiocarpal"
HAnimJoint198.center = [-7.808,31.46,-0.05849]
HAnimJoint198.ulimit = [0,0,0]
HAnimJoint198.llimit = [0,0,0]
HAnimSegment199 = x3d.HAnimSegment()
HAnimSegment199.name = "r_carpal"
HAnimSegment199.DEF = "hanim_r_carpal"
Transform200 = x3d.Transform()
Transform200.translation = [-7.808,31.46,-0.05849]
Shape201 = x3d.Shape()
Appearance202 = x3d.Appearance()
Material203 = x3d.Material()
Material203.diffuseColor = [0.588,0.588,0.588]

Appearance202.material = Material203
ImageTexture204 = x3d.ImageTexture()
ImageTexture204.USE = "Annex01JinTextureAtlas"

Appearance202.texture = ImageTexture204

Shape201.appearance = Appearance202
IndexedFaceSet205 = x3d.IndexedFaceSet()
IndexedFaceSet205.coordIndex = [4,2,0,-1,0,5,4,-1,6,1,3,-1,3,7,6,-1,1,6,5,-1,5,0,1,-1,8,4,5,-1,5,9,8,-1,10,6,7,-1,7,11,10,-1,9,5,6,-1,6,10,9,-1,12,8,9,-1,9,13,12,-1,14,10,11,-1,11,15,14,-1,13,9,10,-1,10,14,13,-1,4,16,2,-1,2,16,7,-1,7,3,2,-1,17,20,18,-1,18,19,17,-1,21,11,7,-1,7,16,21,-1,8,12,21,-1,12,15,11,-1,11,21,12,-1,13,14,15,-1,15,12,13,-1,8,17,19,-1,19,4,8,-1,4,19,18,-1,18,16,4,-1,16,18,20,-1,20,21,16,-1,21,20,17,-1,17,8,21,-1,22,23,27,-1,26,24,25,-1]
IndexedFaceSet205.creaseAngle = 3.14159
IndexedFaceSet205.texCoordIndex = [4,7,5,-1,5,6,4,-1,2,0,1,-1,1,3,2,-1,14,17,15,-1,15,16,14,-1,8,4,6,-1,6,9,8,-1,38,41,39,-1,39,40,38,-1,18,37,36,-1,36,19,18,-1,10,8,9,-1,9,11,10,-1,42,38,40,-1,40,43,42,-1,20,18,19,-1,19,21,20,-1,22,23,24,-1,24,23,25,-1,25,26,24,-1,27,30,28,-1,28,29,27,-1,31,32,25,-1,25,23,31,-1,33,34,31,-1,34,35,32,-1,32,31,34,-1,20,21,35,-1,35,34,20,-1,8,13,12,-1,12,4,8,-1,22,29,28,-1,28,23,22,-1,23,28,30,-1,30,31,23,-1,31,30,27,-1,27,33,31,-1,14,26,24,-1,14,24,16,-1]
Coordinate206 = x3d.Coordinate()

IndexedFaceSet205.coord = Coordinate206
TextureCoordinate207 = x3d.TextureCoordinate()

IndexedFaceSet205.texCoord = TextureCoordinate207

Shape201.geometry = IndexedFaceSet205

Transform200.children.append(Shape201)

HAnimSegment199.children.append(Transform200)

HAnimJoint198.children.append(HAnimSegment199)

HAnimJoint188.children.append(HAnimJoint198)

HAnimJoint178.children.append(HAnimJoint188)

HAnimJoint128.children.append(HAnimJoint178)

HAnimJoint38.children.append(HAnimJoint128)

HAnimJoint28.children.append(HAnimJoint38)

HAnimHumanoid25.skeleton.append(HAnimJoint28)
HAnimJoint208 = x3d.HAnimJoint()
HAnimJoint208.USE = "hanim_humanoid_root"

HAnimHumanoid25.joints.append(HAnimJoint208)
HAnimJoint209 = x3d.HAnimJoint()
HAnimJoint209.USE = "hanim_sacroiliac"

HAnimHumanoid25.joints.append(HAnimJoint209)
HAnimJoint210 = x3d.HAnimJoint()
HAnimJoint210.USE = "hanim_vl5"

HAnimHumanoid25.joints.append(HAnimJoint210)
HAnimJoint211 = x3d.HAnimJoint()
HAnimJoint211.USE = "hanim_skullbase"

HAnimHumanoid25.joints.append(HAnimJoint211)
HAnimJoint212 = x3d.HAnimJoint()
HAnimJoint212.USE = "hanim_l_elbow"

HAnimHumanoid25.joints.append(HAnimJoint212)
HAnimJoint213 = x3d.HAnimJoint()
HAnimJoint213.USE = "hanim_r_elbow"

HAnimHumanoid25.joints.append(HAnimJoint213)
HAnimJoint214 = x3d.HAnimJoint()
HAnimJoint214.USE = "hanim_l_hip"

HAnimHumanoid25.joints.append(HAnimJoint214)
HAnimJoint215 = x3d.HAnimJoint()
HAnimJoint215.USE = "hanim_r_hip"

HAnimHumanoid25.joints.append(HAnimJoint215)
HAnimJoint216 = x3d.HAnimJoint()
HAnimJoint216.USE = "hanim_l_knee"

HAnimHumanoid25.joints.append(HAnimJoint216)
HAnimJoint217 = x3d.HAnimJoint()
HAnimJoint217.USE = "hanim_r_knee"

HAnimHumanoid25.joints.append(HAnimJoint217)
HAnimJoint218 = x3d.HAnimJoint()
HAnimJoint218.USE = "hanim_l_metatarsophalangeal_2"

HAnimHumanoid25.joints.append(HAnimJoint218)
HAnimJoint219 = x3d.HAnimJoint()
HAnimJoint219.USE = "hanim_r_metatarsophalangeal_2"

HAnimHumanoid25.joints.append(HAnimJoint219)
HAnimJoint220 = x3d.HAnimJoint()
HAnimJoint220.USE = "hanim_l_radiocarpal"

HAnimHumanoid25.joints.append(HAnimJoint220)
HAnimJoint221 = x3d.HAnimJoint()
HAnimJoint221.USE = "hanim_r_radiocarpal"

HAnimHumanoid25.joints.append(HAnimJoint221)
HAnimJoint222 = x3d.HAnimJoint()
HAnimJoint222.USE = "hanim_l_shoulder"

HAnimHumanoid25.joints.append(HAnimJoint222)
HAnimJoint223 = x3d.HAnimJoint()
HAnimJoint223.USE = "hanim_r_shoulder"

HAnimHumanoid25.joints.append(HAnimJoint223)
HAnimJoint224 = x3d.HAnimJoint()
HAnimJoint224.USE = "hanim_l_talocrural"

HAnimHumanoid25.joints.append(HAnimJoint224)
HAnimJoint225 = x3d.HAnimJoint()
HAnimJoint225.USE = "hanim_r_talocrural"

HAnimHumanoid25.joints.append(HAnimJoint225)
HAnimSegment226 = x3d.HAnimSegment()
HAnimSegment226.USE = "hanim_sacrum"

HAnimHumanoid25.segments.append(HAnimSegment226)
HAnimSegment227 = x3d.HAnimSegment()
HAnimSegment227.USE = "hanim_pelvis"

HAnimHumanoid25.segments.append(HAnimSegment227)
HAnimSegment228 = x3d.HAnimSegment()
HAnimSegment228.USE = "hanim_l5"

HAnimHumanoid25.segments.append(HAnimSegment228)
HAnimSegment229 = x3d.HAnimSegment()
HAnimSegment229.USE = "hanim_skull"

HAnimHumanoid25.segments.append(HAnimSegment229)
HAnimSegment230 = x3d.HAnimSegment()
HAnimSegment230.USE = "hanim_l_calf"

HAnimHumanoid25.segments.append(HAnimSegment230)
HAnimSegment231 = x3d.HAnimSegment()
HAnimSegment231.USE = "hanim_r_calf"

HAnimHumanoid25.segments.append(HAnimSegment231)
HAnimSegment232 = x3d.HAnimSegment()
HAnimSegment232.USE = "hanim_l_carpal"

HAnimHumanoid25.segments.append(HAnimSegment232)
HAnimSegment233 = x3d.HAnimSegment()
HAnimSegment233.USE = "hanim_r_carpal"

HAnimHumanoid25.segments.append(HAnimSegment233)
HAnimSegment234 = x3d.HAnimSegment()
HAnimSegment234.USE = "hanim_l_forearm"

HAnimHumanoid25.segments.append(HAnimSegment234)
HAnimSegment235 = x3d.HAnimSegment()
HAnimSegment235.USE = "hanim_r_forearm"

HAnimHumanoid25.segments.append(HAnimSegment235)
HAnimSegment236 = x3d.HAnimSegment()
HAnimSegment236.USE = "hanim_l_talus"

HAnimHumanoid25.segments.append(HAnimSegment236)
HAnimSegment237 = x3d.HAnimSegment()
HAnimSegment237.USE = "hanim_r_talus"

HAnimHumanoid25.segments.append(HAnimSegment237)
HAnimSegment238 = x3d.HAnimSegment()
HAnimSegment238.USE = "hanim_l_tarsal_proximal_phalanx_2"

HAnimHumanoid25.segments.append(HAnimSegment238)
HAnimSegment239 = x3d.HAnimSegment()
HAnimSegment239.USE = "hanim_r_tarsal_proximal_phalanx_2"

HAnimHumanoid25.segments.append(HAnimSegment239)
HAnimSegment240 = x3d.HAnimSegment()
HAnimSegment240.USE = "hanim_l_thigh"

HAnimHumanoid25.segments.append(HAnimSegment240)
HAnimSegment241 = x3d.HAnimSegment()
HAnimSegment241.USE = "hanim_r_thigh"

HAnimHumanoid25.segments.append(HAnimSegment241)
HAnimSegment242 = x3d.HAnimSegment()
HAnimSegment242.USE = "hanim_l_upperarm"

HAnimHumanoid25.segments.append(HAnimSegment242)
HAnimSegment243 = x3d.HAnimSegment()
HAnimSegment243.USE = "hanim_r_upperarm"

HAnimHumanoid25.segments.append(HAnimSegment243)
HAnimMotion244 = x3d.HAnimMotion()
HAnimMotion244.name = "motion_animation"
HAnimMotion244.DEF = "hanim_motion_animation"
HAnimMotion244.channels = [" Xposition Yposition Zposition Zrotation Xrotation Yrotation 3 Zrotation Xrotation Yrotation 3 Zrotation Xrotation Yrotation 3 Zrotation Xrotation Yrotation 3 Zrotation Xrotation Yrotation 3 Zrotation Xrotation Yrotation 3 Zrotation Xrotation Yrotation 3 Zrotation Xrotation Yrotation 3 Zrotation Xrotation Yrotation 3 Zrotation Xrotation Yrotation 3 Zrotation Xrotation Yrotation 3 Zrotation Xrotation Yrotation 3 Zrotation Xrotation Yrotation 3 Zrotation Xrotation Yrotation 3 Zrotation Xrotation Yrotation 3 Zrotation Xrotation Yrotation 3 Zrotation Xrotation Yrotation 3 Zrotation Xrotation Yrotatio"]
HAnimMotion244.enabled = False
HAnimMotion244.totalFrameCount = 392
HAnimMotion244.joints = ["umanoidRoot l_hip l_knee l_talocrural r_hip r_knee r_talocrural vl5 IGNORED l_shoulder l_elbow l_radiocarpal IGNORED r_shoulder r_elbow r_radiocarpal IGNORED skullbas"]
HAnimMotion244.values = [102.2373,37.3864,-30.7042,25.99,9.39,-76.67,29.91,-61.78,39.39,0.15,30.83,-0.15,-0.26,-28.19,0.29,3.19,-14.91,-9.78,-0.14,22.8,0.13,-3.32,-36.05,-1.04,0.79,-28.37,9.52,0,0,0,69.07,-22.04,21.58,0.35,-54.3,0.53,29.27,-0.43,-13.04,0,0,0,-44.97,18.14,-34.93,-0.56,-68.67,-0.77,-31.17,-1.1,19.42,-5.97,-15.92,-8.18,10.67,17.77,-18.05,101.0132,37.513,-29.6601,26.2,9.76,-74.59,24.96,-62.35,33.97,0.15,31.9,-0.16,-0.85,-23.93,0.31,2.67,-11.32,-9.2,-0.14,19.06,0.12,-1.61,-32.41,-0.58,1.74,-30.18,9.77,0,0,0,67.84,-21.19,21.33,0.33,-51.75,0.51,27.86,-0.57,-11.96,0,0,0,-46.55,18.1,-36.7,-0.51,-66.51,-0.72,-30.61,-1.04,18.43,-7.18,-15.52,-8.48,10.58,18.63,-18.73,99.8019,37.6292,-28.4775,26.15,9.4,-72.64,18.33,-61.82,27.66,0.15,32.96,-0.16,-1.23,-21.18,0.38,1.45,-7.38,-9.4,-0.13,15.62,0.11,1.15,-27.53,-0.28,2.14,-32.68,10,0,0,0,66.23,-19.31,19.35,0.31,-49.16,0.49,26.22,-0.64,-10.92,0,0,0,-47.88,18.84,-35.88,-0.49,-65.33,-0.69,-30.28,-1,17.89,-7.84,-13.32,-8.37,10.39,19.02,-19.18,98.5371,37.8909,-27.3094,25.87,8.5,-71.67,16.58,-58.87,32.26,0.15,33.83,-0.16,-1,-19.18,0.4,-0.12,-3.92,-9.35,-0.13,13.48,0.11,4.16,-21.97,-0.55,1.31,-34,10.78,0,0,0,66.31,-18.11,18.2,0.29,-46.27,0.46,24.47,-0.58,-9.83,0,0,0,-47.65,18.25,-36.23,-0.46,-63.71,-0.66,-29.76,-0.95,17.16,-7.75,-11.48,-8.42,10.67,19.42,-20.03,97.3524,38.1439,-26.1283,25.41,7.45,-70.56,13.04,-55.97,32.74,0.15,34.22,-0.17,-0.68,-18.05,0.39,-1.94,-2.61,-9.49,-0.13,15.44,0.11,6.09,-17.49,-1.13,-0.19,-34.84,10.89,0,0,0,67.12,-16.77,17.43,0.28,-43.59,0.44,22.94,-0.46,-8.88,0,0,0,-46.9,17.43,-37.05,-0.43,-61.49,-0.63,-28.93,-0.86,16.18,-7.47,-9.75,-8.54,10.76,19.57,-20.81,96.2173,38.4056,-24.9244,24.69,6.66,-68.89,7.37,-53.15,27.51,0.15,33.76,-0.16,-0.61,-18.05,0.38,-3.72,-2.15,-10.11,-0.14,19.14,0.12,7.49,-13.64,-1.82,-2.03,-34.13,10.04,0,0,0,67.56,-16.62,19.5,0.27,-41.5,0.43,21.74,-0.34,-8.16,0,0,0,-45.96,15.73,-39.13,-0.39,-58.68,-0.59,-27.81,-0.72,14.98,-7.27,-9.14,-8.81,10.66,19.49,-21.42,95.1761,38.6924,-23.7938,24.15,6.42,-66.71,2.82,-50.48,23.33,0.15,32.73,-0.16,-0.47,-18.01,0.36,-4.97,-2.42,-10.52,-0.14,23.12,0.13,9.59,-8.81,-3.08,-2.43,-35.2,8.98,0,0,0,66.08,-15.05,19.34,0.27,-40.97,0.43,21.31,-0.27,-7.99,0,0,0,-46.61,15.23,-38.76,-0.38,-57.27,-0.57,-27.29,-0.66,14.38,-7.51,-6.45,-8.69,10.34,19.29,-21.8,94.1762,38.9317,-22.7185,23.12,5.98,-64.14,-0.64,-46.82,21.66,0.15,31.49,-0.16,-0.24,-18.64,0.33,-6.39,-2.5,-12.36,-0.14,27.19,0.14,12.08,-3.47,-4.99,-3.87,-35.12,7.85,0,0,0,65.09,-14.87,19.12,0.27,-40.69,0.43,21.06,-0.21,-7.91,0,0,0,-46.35,15.01,-39.01,-0.36,-55.89,-0.55,-26.78,-0.6,13.8,-7.31,-4.03,-8.75,10.55,18.89,-22.62,93.2366,39.1289,-21.7609,21.45,6.18,-62.86,-1.97,-43.09,19.07,0.15,30.63,-0.15,-0.37,-19.86,0.34,-6.65,-2.81,-12.07,-0.15,31.11,0.16,13.48,0.96,-6.6,-3.2,-34.37,8.5,0,0,0,63.73,-14.81,18.79,0.27,-40.8,0.43,20.99,-0.17,-7.96,0,0,0,-45.98,14.78,-38.15,-0.35,-54.48,-0.54,-26.16,-0.51,13.23,-7.35,-2.07,-8.79,10.83,18.39,-23.36,92.3888,39.3091,-20.882,19.91,6.61,-61.14,-2.8,-39.87,17.37,0.15,30.07,-0.15,-0.39,-20.96,0.33,-7.16,-3.88,-12.65,-0.16,34.78,0.17,14.2,5.59,-8.07,-2.13,-34.16,8.98,0,0,0,62.06,-14.08,17.05,0.27,-41.44,0.43,21.2,-0.16,-8.19,0,0,0,-45.94,14.76,-36.67,-0.35,-54.3,-0.53,-26.12,-0.51,13.15,-7.92,0.86,-8.72,11.42,17.57,-24.43,91.5813,39.4364,-20.0691,18.04,6.98,-59.5,-2.94,-36.77,16.03,0.15,30.04,-0.15,-0.44,-21.88,0.33,-7.09,-4.66,-11.68,-0.16,38.33,0.18,13.82,9.33,-8.68,-0.98,-33.13,9.48,0,0,0,60.8,-13.97,16.16,0.27,-41.75,0.43,21.16,-0.09,-8.32,0,0,0,-46.05,14.11,-36.09,-0.34,-53.3,-0.52,-25.65,-0.43,12.75,-8.46,2.9,-8.66,12.07,17.16,-25.41,90.8459,39.3922,-19.3562,16.11,7.21,-57.54,-3.34,-34.04,13.83,0.15,30.45,-0.15,-0.54,-22.99,0.32,-7.1,-4.73,-11.05,-0.17,41.88,0.19,10.54,9.27,-6.58,-1.07,-31.24,9.59,0,0,0,60.87,-14.6,15.39,0.27,-42.26,0.44,21.22,-0.02,-8.53,0,0,0,-45.12,13.77,-35.61,-0.34,-53.57,-0.53,-25.63,-0.4,12.88,-7.97,3.69,-9.09,12.59,16.74,-26.65,90.1361,39.4038,-18.6673,14.17,6.77,-56.09,-3.89,-31.01,11.17,0.15,30.84,-0.16,-0.67,-24.18,0.31,-7.5,-6.13,-10.33,-0.18,46.01,0.21,8.78,11.25,-5.75,-1.02,-28.88,9.92,0,0,0,60.82,-14.9,15.28,0.28,-42.91,0.44,21.37,0.02,-8.78,0,0,0,-44.75,13.25,-34.4,-0.35,-54.73,-0.54,-25.88,-0.38,13.38,-7.81,4.44,-9.28,13.2,16.07,-27.54,89.5959,39.3571,-18.1248,12.97,6.41,-54.5,-3.9,-28.77,11.47,0.15,31.06,-0.16,-0.78,-25.06,0.3,-8.13,-9.16,-9.76,-0.2,50.94,0.24,7.17,12.89,-4.87,-1.43,-27.9,10.17,0,0,0,60.84,-14.63,14.23,0.28,-44.13,0.45,21.82,0.02,-9.23,0,0,0,-44.1,13.58,-31.86,-0.37,-56.24,-0.56,-26.19,-0.35,14.04,-7.34,5.95,-9.6,13.4,15.13,-28.59,89.2018,39.2414,-17.574,11.79,5.12,-52.41,-4.98,-26.13,11.15,0.15,31.15,-0.16,-0.91,-25.81,0.28,-10.13,-11.73,-10.91,-0.23,56.18,0.27,5.49,13.09,-3.75,-2.6,-24.79,9.51,0,0,0,60.45,-14.62,14.45,0.29,-45.61,0.46,22.38,-0.01,-9.79,0,0,0,-44.25,12.52,-29.24,-0.38,-57.59,-0.57,-26.52,-0.35,14.63,-7.56,5.79,-9.83,13.87,14.57,-29.29,88.8635,39.1751,-17.1212,10.43,3.76,-50.36,-6.1,-23.49,9.21,0.15,31.35,-0.16,-1.02,-26.48,0.26,-11.78,-14.49,-11.76,-0.27,61.34,0.31,4.62,12.66,-3.12,-3.91,-21.25,8.65,0,0,0,60.62,-14.57,14.82,0.3,-46.77,0.47,23,-0.12,-10.2,0,0,0,-44.37,11.71,-26.33,-0.4,-59.5,-0.6,-27.14,-0.44,15.45,-7.72,5.78,-9.61,14.86,13.92,-29.53,88.6095,39.0886,-16.8331,9.11,2.95,-48.7,-6.36,-21.76,8.14,0.15,32.05,-0.16,-1.13,-27.03,0.24,-12.66,-18.42,-12.07,-0.32,66.47,0.37,4.36,11.81,-2.88,-3.85,-18.38,8.31,0,0,0,59.86,-14.2,14.71,0.3,-47.82,0.48,23.82,-0.33,-10.54,0,0,0,-45.22,11.37,-22.42,-0.43,-61.81,-0.63,-27.88,-0.56,16.46,-8.35,6.01,-9.43,15.42,13.45,-29.73,88.4366,38.9708,-16.6867,8.01,2.21,-47.56,-6.32,-20.85,7.49,0.15,33.37,-0.16,-1.23,-27.37,0.23,-13.58,-23.4,-12.14,-0.4,71.41,0.46,4.19,12.13,-2.77,-3.73,-14.87,7.89,0,0,0,59.19,-14.02,16.38,0.3,-48.2,0.48,24.61,-0.53,-10.62,0,0,0,-46.17,9.55,-19.17,-0.46,-63.85,-0.67,-28.54,-0.68,17.35,-9.04,5.08,-9.44,15.72,13.32,-29.71,88.3473,38.7864,-16.5983,7.19,1.65,-46.29,-6.38,-20.61,6.65,0.16,35.24,-0.17,-1.39,-28.15,0.2,-15.15,-28.53,-13.27,-0.52,75.66,0.58,4.04,10.02,-2.54,-4.39,-11.69,7.02,0,0,0,59.23,-13.66,17.56,0.31,-48.33,0.48,25.43,-0.63,-10.61,0,0,0,-46.53,7.2,-16.91,-0.5,-65.8,-0.7,-29.3,-0.84,18.2,-8.96,4.04,-9.47,15.87,12.9,-29.36,88.2985,38.5674,-16.6196,6.57,1.59,-45.41,-5.98,-21.16,6.2,0.16,37.52,-0.18,-1.6,-29.16,0.14,-16.42,-34.12,-14.39,-0.65,78.7,0.72,4.04,8.4,-2.42,-4.51,-9.33,6.34,0,0,0,59.22,-13.06,18.94,0.31,-48.44,0.48,26.18,-0.6,-10.63,0,0,0,-47.24,4.98,-14.45,-0.54,-67.78,-0.75,-30.26,-1.02,19.06,-9.09,2.88,-9.39,15.89,12.84,-28.76,88.2626,38.3273,-16.6708,6.42,1.63,-45.74,-5.51,-22.23,7,0.17,40.02,-0.19,-1.81,-30.35,0.08,-17.55,-40.14,-14.82,-0.75,80.15,0.82,4.17,7.34,-2.42,-4.39,-7.63,6.08,0,0,0,59.03,-11.63,21.06,0.31,-48.99,0.49,26.86,-0.53,-10.85,0,0,0,-48.66,2.03,-11.83,-0.56,-68.8,-0.78,-31.16,-1.11,19.48,-9.68,1.8,-9.02,16.02,12.65,-27.73,88.2208,38.0047,-16.7127,6.76,1.76,-46.54,-5.47,-23.79,7.61,0.17,42.64,-0.2,-1.87,-31.57,0.03,-18.8,-45.41,-15.44,-0.71,79.53,0.77,3.07,3.55,-1.6,-4.98,-6.01,6.11,0,0,0,59.31,-10.68,24.32,0.31,-49.76,0.49,27.48,-0.46,-11.17,0,0,0,-49.75,-1.61,-10.26,-0.57,-69.22,-0.79,-31.92,-1.08,19.66,-9.75,0.18,-8.9,16.05,12.1,-26.69,88.1571,37.651,-16.7239,7.8,1.66,-48.09,-6.03,-25.39,7.93,0.18,44.78,-0.21,-1.86,-33.11,-0.03,-20,-50.28,-15.72,-0.55,76.59,0.62,1.61,-1.95,-0.7,-5.76,-5.38,7.1,0,0,0,59.22,-9.57,26.84,0.32,-50.59,0.5,28.03,-0.38,-11.51,0,0,0,-51,-4.95,-9.31,-0.58,-69.49,-0.79,-32.52,-0.97,19.8,-10.35,-1.5,-8.85,16.13,12.23,-25.94,88.1025,37.3989,-16.7136,9.48,2.04,-50.26,-6.34,-27.51,8.74,0.19,46.36,-0.21,-1.79,-34.25,-0.06,-21.26,-55.47,-16.88,-0.4,71.32,0.46,0.9,-4.05,-0.39,-6.35,-6.14,8.37,0,0,0,59.18,-7.74,28.88,0.32,-51.17,0.5,28.47,-0.29,-11.76,0,0,0,-51.65,-8.25,-9.21,-0.58,-69.48,-0.79,-32.93,-0.85,19.81,-10.91,-2.84,-8.64,16.08,12.33,-24.93,87.9962,37.1696,-16.6837,11.4,2.08,-52.93,-6.62,-29.31,10.21,0.19,47.35,-0.22,-1.67,-35,-0.06,-22.56,-59.2,-19.24,-0.3,64.46,0.35,0.94,-5.24,-0.4,-7.55,-6.35,9.88,0,0,0,59.3,-6.18,31.78,0.33,-51.51,0.51,28.76,-0.21,-11.92,0,0,0,-51.81,-12.21,-9.87,-0.56,-68.89,-0.78,-33.2,-0.68,19.57,-11.27,-4.54,-8.64,16.02,11.53,-23.85,87.7643,37.0833,-16.5464,12.93,2.06,-55.91,-6.72,-30.19,11.53,0.19,47.61,-0.22,-1.43,-35.85,-0.04,-22.6,-61.49,-21.53,-0.23,56.34,0.27,1.36,-4.24,-0.61,-7.41,-6.4,11.4,0,0,0,58.14,-4.32,34.78,0.33,-51.76,0.51,28.98,-0.15,-12.03,0,0,0,-53.22,-16.18,-10.18,-0.54,-68.11,-0.76,-33.42,-0.46,19.25,-12.83,-6.19,-8.53,16.29,11.34,-22.8,87.518,37.0526,-16.4667,14.67,2.13,-58.44,-6.92,-31.14,12.33,0.19,47.32,-0.22,-1.17,-36.4,0.01,-22.81,-63.61,-24.1,-0.19,48.39,0.22,2,-2,-0.97,-8.09,-7.68,12.9,0,0,0,58.15,-2.72,36.53,0.33,-51.49,0.51,29.02,-0.08,-11.93,0,0,0,-53.19,-18.96,-10.25,-0.53,-67.29,-0.74,-33.58,-0.23,18.92,-12.9,-7.12,-8.5,15.69,11.21,-21.93,87.198,37.0751,-16.3576,15.97,2.13,-60.04,-7.29,-31.51,12.34,0.19,46.74,-0.21,-0.91,-36.37,0.07,-23.51,-64.79,-26.48,-0.17,41.71,0.19,2.87,-0.46,-1.44,-8.43,-8.75,13.6,0,0,0,57.72,-1.27,38.4,0.33,-51.37,0.51,29.08,-0.02,-11.9,0,0,0,-53.32,-21.15,-8.99,-0.51,-66.46,-0.72,-33.6,-0.07,18.58,-13.16,-7.95,-8.48,15.29,11.56,-21.36,86.7742,37.1565,-16.2769,16.95,2.36,-61.67,-7.26,-31.48,12.23,0.18,45.76,-0.21,-0.76,-36.12,0.11,-21.85,-65.95,-24.35,-0.16,36.47,0.17,4.48,-0.46,-2.19,-8.19,-9.43,14.65,0,0,0,57.01,-0.61,39.98,0.32,-51.2,0.5,29.08,0.02,-11.84,0,0,0,-53.78,-22.86,-7.5,-0.5,-66.06,-0.71,-33.61,0.01,18.41,-13.44,-8.82,-8.63,15.03,11.84,-21.16,86.2933,37.2549,-16.1715,17.93,2.39,-62.86,-7.67,-30.98,11.62,0.18,44.3,-0.2,-0.54,-36.16,0.16,-19.07,-67.15,-17.25,-0.15,32.85,0.16,6.74,-1.87,-3.05,-8.29,-10.39,15.57,0,0,0,56.83,-0.09,40.2,0.32,-51.01,0.5,29,0.01,-11.76,0,0,0,-53.93,-23.55,-5.41,-0.51,-66.58,-0.72,-33.73,0,18.65,-13.56,-9.07,-8.78,15.07,11.98,-21.35,85.7143,37.3685,-16.0444,18.56,2.45,-63.62,-8.13,-29.95,10.42,0.17,42.65,-0.2,-0.15,-36.19,0.25,-13.89,-67.73,-4.24,-0.15,30.65,0.15,9.25,-4.68,-3.67,-8.16,-11.05,16.12,0,0,0,56.55,0.46,40.37,0.32,-50.93,0.5,28.95,0,-11.72,0,0,0,-54.49,-23.86,-2.51,-0.53,-67.44,-0.74,-33.83,-0.08,19.03,-13.43,-9.63,-8.99,14.58,12.58,-21.48,85.0774,37.4994,-15.9003,19.16,2.77,-64.17,-8.43,-28.9,8.99,0.17,41.02,-0.19,0.22,-36.23,0.34,-12.25,-68.15,0.61,-0.15,29.45,0.15,9.94,-7.66,-3.39,-7.75,-12.17,16.53,0,0,0,56.24,0.98,40.69,0.32,-50.79,0.5,28.83,-0.04,-11.65,0,0,0,-54.83,-23.9,0.4,-0.54,-67.71,-0.75,-33.65,-0.26,19.12,-13.25,-9.94,-9.15,14.13,13.15,-21.65,84.3668,37.562,-15.7648,19.99,2.94,-64.76,-8.5,-27.85,8.56,0.17,39.4,-0.18,0.45,-36.3,0.4,-12.5,-68.55,-0.1,-0.15,29.07,0.15,8.97,-11.59,-2.43,-7.85,-14.01,17.13,0,0,0,56.73,1.43,40.85,0.32,-50.24,0.5,28.53,-0.1,-11.42,0,0,0,-54.57,-23.35,3.7,-0.54,-67.95,-0.75,-33.28,-0.51,19.16,-12.63,-9.51,-9.19,14,13.28,-21.97,83.5838,37.584,-15.6535,20.91,3.11,-65.2,-8.45,-26.74,8.53,0.16,37.69,-0.18,0.66,-36.64,0.45,-12.45,-68.96,-0.64,-0.15,29.25,0.15,7.82,-14.96,-1.66,-7.74,-15.67,17.76,0,0,0,56.8,1.64,41.29,0.31,-49.77,0.49,28.24,-0.16,-11.22,0,0,0,-55.25,-22.54,6.94,-0.54,-67.81,-0.75,-32.78,-0.73,19.05,-12.68,-9.58,-9.41,14.36,13.88,-22.68,82.7104,37.6562,-15.525,21.63,3.34,-65.48,-8.24,-25.35,8.45,0.16,35.86,-0.17,0.72,-36.57,0.47,-12.65,-68.98,-1.58,-0.15,29.59,0.15,6.47,-17.69,-1.08,-7.54,-17.08,18.28,0,0,0,56.9,1.85,41.6,0.31,-49.53,0.49,28.07,-0.19,-11.11,0,0,0,-56.11,-21.71,9.53,-0.51,-66.72,-0.72,-31.87,-0.92,18.5,-12.71,-9.44,-9.63,14.65,13.69,-23.21,81.7785,37.7181,-15.4031,22.16,3.48,-65.26,-7.98,-23.64,8.53,0.15,34,-0.16,0.62,-36.25,0.44,-13.95,-68.33,-3.71,-0.15,29.87,0.15,5.06,-20.09,-0.67,-7.78,-18.52,18.4,0,0,0,57.5,1.67,42.11,0.31,-49.11,0.49,27.77,-0.26,-10.94,0,0,0,-56.67,-20.67,11.73,-0.47,-64.14,-0.67,-30.44,-0.97,17.33,-12.54,-9.22,-9.89,14.89,14.01,-24,80.7702,37.7606,-15.2427,22.76,3.73,-64.61,-7.78,-21.92,7.98,0.15,32.11,-0.16,0.47,-35.7,0.41,-16.03,-67.44,-6.77,-0.15,30.06,0.15,3.31,-23.04,-0.35,-8.04,-20.12,18.09,0,0,0,58.17,1.52,42.17,0.31,-48.79,0.48,27.48,-0.32,-10.8,0,0,0,-57.36,-19.58,13.17,-0.43,-61.55,-0.63,-28.97,-0.87,16.21,-12.46,-8.77,-10.07,15.08,14.24,-24.71,79.6064,37.791,-15.0872,22.97,4.1,-64.01,-7.11,-19.71,7.69,0.15,30.18,-0.15,0.29,-35.13,0.36,-16.83,-65.97,-8.87,-0.15,30.11,0.15,1.1,-26.62,-0.23,-8.31,-21.41,18,0,0,0,59.09,1.27,41.63,0.31,-48.49,0.48,27.17,-0.39,-10.67,0,0,0,-57.94,-18.27,13.91,-0.4,-59.77,-0.6,-27.9,-0.7,15.48,-12.27,-8.61,-10.34,15.22,14.43,-25.4,78.3476,37.8095,-14.9414,23.35,4.43,-63.25,-6.41,-17.6,7.9,0.15,28.25,-0.15,0.05,-34.18,0.32,-17.99,-64.44,-11.23,-0.15,30.16,0.15,-0.73,-29.56,-0.36,-8.27,-23.17,17.59,0,0,0,59.5,1.67,40.77,0.31,-48.31,0.48,26.87,-0.46,-10.59,0,0,0,-59.03,-16.76,15.36,-0.39,-58.51,-0.58,-27.07,-0.5,14.99,-12.28,-7.95,-10.35,15.27,14.68,-25.84,76.9685,37.7749,-14.7762,23.77,4.61,-62.55,-5.83,-15.33,7.41,0.14,26.37,-0.14,-0.12,-33.03,0.29,-19.08,-62.73,-13.34,-0.15,30.14,0.15,-1.8,-31.45,-0.53,-8.58,-24.85,17.38,0,0,0,60.17,1.57,40.17,0.3,-48.06,0.48,26.61,-0.5,-10.48,0,0,0,-60.13,-15.12,16.77,-0.38,-58.01,-0.58,-26.59,-0.34,14.83,-12.12,-7.5,-10.54,15.19,14.83,-26.41,75.4827,37.7198,-14.6104,24.15,4.92,-61.47,-5.1,-12.86,6.17,0.14,24.18,-0.14,-0.33,-31.39,0.27,-20.43,-60.93,-15.97,-0.15,30.48,0.15,-2.24,-32.55,-0.64,-9.27,-27.1,16.76,0,0,0,61.3,1.29,39.24,0.3,-47.74,0.48,26.22,-0.55,-10.36,0,0,0,-60.48,-13.32,18.47,-0.38,-57.72,-0.57,-26.19,-0.16,14.75,-11.49,-6.7,-10.6,14.97,15.14,-26.89,73.8344,37.854,-14.4894,24.1,5.87,-60.11,-3.58,-10.08,5.36,0.14,21.36,-0.13,-0.63,-28.8,0.26,-20.3,-59.57,-18.16,-0.15,31.78,0.16,-1.55,-31.26,-0.48,-8.93,-30.28,16.12,0,0,0,61.99,1.35,37.43,0.3,-47.66,0.47,25.85,-0.6,-10.33,0,0,0,-60.89,-10.69,21.57,-0.39,-58.2,-0.58,-26.1,-0.02,15.01,-11.24,-4.96,-10.42,15.03,15.76,-27.51,72.1085,38.1202,-14.391,23.82,6.85,-59.44,-1.86,-7.29,4.16,0.14,18.42,-0.12,-1.17,-24.66,0.31,-18.24,-58.67,-18.56,-0.15,33.14,0.16,0.18,-27.82,-0.24,-8.35,-33.06,16.11,0,0,0,62.86,0.79,36.38,0.3,-47.64,0.47,25.58,-0.62,-10.33,0,0,0,-61.37,-8.52,25.13,-0.4,-59.45,-0.6,-26.34,0.01,15.58,-11,-3.42,-10.27,15.28,16.35,-28.15,70.3796,38.4528,-14.3253,23.28,7.32,-59.31,-0.58,-4.86,2.27,0.13,17.03,-0.12,-2.2,-19.44,0.52,-15.57,-57.18,-17.9,-0.15,34.03,0.17,1.85,-24.18,-0.24,-7.59,-34.75,16.75,0,0,0,63.04,0.51,35.54,0.31,-48.46,0.48,25.55,-0.63,-10.66,0,0,0,-62,-6.58,28.5,-0.44,-62.38,-0.64,-27.05,-0.03,16.89,-11.2,-2.67,-10.2,15.85,16.97,-28.82,68.6263,38.6937,-14.3449,21.83,8.04,-59.18,1.5,-3.32,2.24,0.14,18.51,-0.12,-3.38,-14.77,0.92,-12.98,-54.24,-20.07,-0.16,34.37,0.17,2.66,-21.64,-0.36,-6.29,-35.31,17.03,0,0,0,62.91,0.53,35.2,0.31,-49.45,0.49,25.59,-0.63,-11.07,0,0,0,-62.28,-5.72,30.79,-0.48,-65,-0.69,-27.62,-0.07,18.1,-10.88,-2.45,-10.34,15.59,17.17,-29.03,66.9122,38.969,-14.4053,20.22,8.67,-58.72,3.28,-2.84,2.18,0.14,21.81,-0.13,-4.89,-10.3,1.6,-10.89,-50.84,-23.53,-0.16,34.23,0.17,2.48,-21.28,-0.37,-5.29,-35.53,17.07,0,0,0,62.48,0.2,34.64,0.32,-50.43,0.5,25.76,-0.63,-11.47,0,0,0,-62.32,-4.99,32.68,-0.52,-66.88,-0.73,-28.02,-0.12,18.97,-10.15,-2.07,-10.49,15.4,17.31,-29.29,65.3395,39.269,-14.445,19.21,8.58,-57.89,3.72,-3.2,2.89,0.14,25.42,-0.14,-6.95,-5.79,2.71,-8.59,-47.82,-23.18,-0.15,33.85,0.16,2.3,-21.62,-0.35,-5.37,-35.67,16.58,0,0,0,62,-0.28,33.89,0.32,-51.3,0.51,26.02,-0.64,-11.83,0,0,0,-62.45,-3.74,34.48,-0.59,-69.89,-0.81,-28.69,-0.27,20.36,-9.6,-1.5,-10.57,15.57,17.44,-29.71,63.9115,39.5229,-14.5369,18.59,8.27,-56.96,3.57,-4.41,4.36,0.15,28.92,-0.15,-8.88,-2.31,3.94,-6.9,-45.19,-22.23,-0.15,33.53,0.16,2.14,-21.99,-0.33,-6.74,-35.26,15.6,0,0,0,62.09,-1.49,33.43,0.33,-51.72,0.51,26.21,-0.66,-11.99,0,0,0,-62.03,-2.59,34.86,-0.68,-72.75,-0.91,-29.31,-0.45,21.68,-8.96,-1.64,-10.83,16.06,17.35,-30.27,62.6141,39.6352,-14.7195,17.19,8.72,-56.2,4.68,-6,6.74,0.15,32.41,-0.16,-8.1,-3.39,3.46,-4,-42.7,-21.02,-0.15,33.41,0.16,1.82,-22.75,-0.28,-6.66,-34.55,14.56,0,0,0,61.99,-2.23,32.75,0.33,-52.01,0.51,26.44,-0.68,-12.1,0,0,0,-61.6,-2.05,35.31,-0.78,-74.99,-1.01,-29.94,-0.7,22.69,-8.48,-1.33,-10.9,16.42,17.04,-30.6,61.5609,39.6687,-14.9009,16.57,8.13,-55.97,3.97,-7.76,8.73,0.16,35.12,-0.17,-6.38,-6.81,2.38,-2.46,-41.04,-19.26,-0.15,34.08,0.17,1.49,-23.54,-0.25,-7.49,-33.2,13.39,0,0,0,61.52,-2.81,32.43,0.33,-52.31,0.51,26.76,-0.7,-12.21,0,0,0,-61.39,-2.43,35.26,-0.89,-76.75,-1.11,-30.52,-0.93,23.48,-8.28,-1.37,-10.9,16.45,16.58,-30.5,60.6604,39.6625,-15.0743,15.65,7.08,-55.99,2.69,-8.81,10.27,0.16,36.89,-0.17,-4.84,-10.6,1.54,-1.42,-39.3,-17.76,-0.16,35.18,0.17,1.19,-24.18,-0.22,-7.95,-30.82,12.56,0,0,0,60.65,-3.46,31.71,0.33,-52.34,0.51,27.01,-0.7,-12.21,0,0,0,-61.77,-3.21,35.02,-1.04,-78.72,-1.27,-31.08,-1.14,24.38,-8.56,-1.42,-10.77,16.67,15.71,-30.27,59.8265,39.7043,-15.3276,14.03,6.74,-56.34,2.6,-9.5,11.21,0.16,37.6,-0.18,-3.12,-14.38,0.87,0.33,-37.69,-16.77,-0.16,36.51,0.17,1.33,-23.5,-0.23,-6.88,-28.21,11.99,0,0,0,59.38,-4.06,30.92,0.33,-52.33,0.51,27.19,-0.7,-12.2,0,0,0,-62.43,-4.34,34.99,-1.28,-80.85,-1.51,-31.72,-1.35,25.35,-8.82,-1.33,-10.49,16.75,14.8,-29.72,59.2182,39.8128,-15.6466,13.09,5.8,-56.82,1.55,-10.93,9.8,0.16,37.06,-0.18,-1.49,-17.48,0.49,1.07,-37.31,-15.45,-0.16,38.77,0.18,1.85,-21.81,-0.28,-6.81,-25.43,10.94,0,0,0,58.3,-4.41,29.76,0.33,-52.4,0.52,27.41,-0.69,-12.23,0,0,0,-63.06,-6.7,34.5,-1.48,-82.12,-1.72,-32.31,-1.5,25.92,-8.93,-1.45,-10.16,16.73,13.94,-28.91,58.8661,39.9087,-15.9749,12.63,4.57,-57.34,-0.34,-13.19,6.96,0.16,36.09,-0.17,-0.51,-20.41,0.34,0.1,-37.93,-16.38,-0.17,41.8,0.19,2.49,-19.52,-0.4,-7.31,-22.49,9.61,0,0,0,57.24,-4.85,28.68,0.33,-52.44,0.52,27.71,-0.65,-12.24,0,0,0,-63.66,-9.38,33.62,-1.74,-83.31,-1.98,-32.86,-1.59,26.46,-8.88,-1.75,-9.81,16.97,13.16,-28.13,58.7053,39.9326,-16.4452,11.91,3.89,-58.46,-1.58,-15.74,3.48,0.16,35.46,-0.17,-0.36,-22.26,0.32,-0.53,-39.27,-18.11,-0.18,45.16,0.21,3.22,-16.32,-0.64,-6.84,-19.56,9.34,0,0,0,55.96,-5.93,27.65,0.33,-52.55,0.52,28.03,-0.6,-12.29,0,0,0,-64.36,-11.75,32.49,-2.22,-84.75,-2.46,-33.42,-1.66,27.14,-8.91,-2.17,-9.72,17.27,12.3,-27.76,58.7,40.0081,-17.0948,11.13,3.38,-60.54,-1.87,-18.36,0.74,0.16,35.64,-0.17,-0.28,-22.27,0.31,-0.91,-41.33,-19.84,-0.19,48.76,0.22,3.99,-11.33,-1.11,-6.27,-15.72,9.5,0,0,0,55.36,-7.31,27.66,0.33,-52.48,0.52,28.24,-0.55,-12.26,0,0,0,-65.13,-14.85,30.63,-3.25,-86.41,-3.49,-33.98,-1.68,27.95,-8.47,-4.21,-9.89,17.32,11.98,-27.09,58.846,39.9627,-17.9005,10.89,3.17,-64.26,-1.23,-21.45,-0.9,0.16,36.92,-0.17,0.1,-20.86,0.3,-1.36,-44.7,-21.32,-0.21,52.59,0.25,3.91,-4.69,-1.55,-5.19,-12.45,11.18,0,0,0,55.07,-8.1,28.18,0.33,-52.56,0.52,28.51,-0.47,-12.3,0,0,0,-66.53,-18.34,28.63,-4.37,-87.33,-4.61,-34.45,-1.65,28.41,-8.27,-6.62,-10,17.29,11.31,-26.02,59.115,39.7143,-18.7173,11.6,2.89,-69.14,-0.22,-23.89,-1,0.16,38.76,-0.18,0.07,-21.17,0.3,-3.11,-49,-24.08,-0.23,56.38,0.27,2.07,2.52,-1.12,-4.44,-10.47,13.56,0,0,0,55.47,-7.9,29.29,0.33,-52.35,0.51,28.67,-0.39,-12.23,0,0,0,-68.38,-21.95,26.96,-7.31,-88.4,-7.56,-34.89,-1.59,28.95,-8.48,-9.2,-10.16,17.44,10.72,-24.97,59.4025,39.2844,-19.4436,12.95,2.39,-74.27,0.36,-25.55,0.29,0.17,40.67,-0.19,-0.71,-24.42,0.29,-6.32,-52.74,-28.15,-0.25,58.46,0.29,-2.15,8.07,1.16,-4.5,-9.63,16.45,0,0,0,56.47,-7.43,30.46,0.33,-52.13,0.51,28.81,-0.3,-12.15,0,0,0,-69.61,-25.55,25.21,-9.12,-88.72,-9.37,-35.22,-1.49,29.13,-8.67,-11.53,-10.62,17.63,10.07,-24.53,59.6259,38.8554,-20.0763,14.52,1.66,-78.97,0.36,-27.14,1.57,0.17,42.8,-0.2,-0.97,-27.44,0.23,-10.5,-54.95,-33.52,-0.24,57.5,0.28,-7.16,7.84,4.07,-5.44,-9.75,19.47,0,0,0,58.08,-7.5,32.45,0.32,-50.69,0.5,28.48,-0.21,-11.58,0,0,0,-69.03,-28.87,23.38,-5.35,-87.82,-5.6,-35.46,-1.33,28.72,-8.67,-13.21,-11.07,18.1,9.27,-24.43,59.7757,38.3569,-20.6441,16.54,0.81,-82.58,0.26,-29.34,2.67,0.18,44.75,-0.21,-0.8,-29.93,0.2,-15.63,-56.11,-40.9,-0.22,54.53,0.26,-5.01,-0.93,2.05,-6.07,-10.79,21.67,0,0,0,58.75,-8.12,35.34,0.31,-48.38,0.48,27.78,-0.12,-10.67,0,0,0,-68.07,-31.87,21.82,-2.72,-85.72,-2.97,-35.66,-1.09,27.72,-9.35,-13.98,-11.46,18.3,8.72,-24.46,59.8139,38.0255,-21.2329,18.38,-0.23,-85.44,0.97,-30.99,4.39,0.18,45.55,-0.21,-0.7,-31.78,0.19,-20.47,-56.48,-46.83,-0.2,50.44,0.23,-1.07,-9.52,0.16,-7.73,-11.76,23.31,0,0,0,60.15,-9.36,38.85,0.29,-45.79,0.46,26.92,-0.04,-9.68,0,0,0,-66.09,-34.78,19.34,-1.51,-82.29,-1.75,-35.74,-0.76,26.1,-9.2,-15.16,-12.07,18.42,8.99,-25.1,59.7365,37.9621,-21.8784,19.55,-1.15,-87.47,2.22,-31.47,6.53,0.18,45.16,-0.21,-0.77,-32.15,0.17,-24.55,-55.86,-50.55,-0.18,45.34,0.21,0.98,-14,-0.35,-8.61,-12.4,23.93,0,0,0,60.85,-9.63,41.84,0.28,-43.41,0.44,26.1,0.04,-8.8,0,0,0,-64,-37.13,17.11,-1.03,-78.68,-1.27,-35.6,-0.46,24.38,-9.78,-15.61,-12.46,19.3,9.01,-25.6,59.6176,38.0082,-22.5451,20.76,-2.27,-89.43,3.13,-31.45,8.63,0.18,43.78,-0.2,-0.8,-31.89,0.17,-26.99,-55.64,-49.08,-0.17,39.99,0.19,2.56,-16.74,-0.56,-9.55,-13.34,24.17,0,0,0,61.28,-9.66,45.15,0.27,-41.09,0.43,25.15,0.06,-7.96,0,0,0,-61.78,-38.84,14.95,-0.76,-74.53,-0.99,-35.19,-0.21,22.41,-10.33,-15.95,-12.63,19.85,9.11,-25.69,59.4223,38.1441,-23.2144,21.71,-3.53,-91.46,3.71,-30.45,10.61,0.17,41.33,-0.19,-0.78,-31.68,0.18,-27.54,-55.9,-41.83,-0.16,35.35,0.17,4.03,-18.75,-0.65,-10.1,-14.67,24.84,0,0,0,60.75,-9.42,47.26,0.26,-39.75,0.42,24.45,0,-7.48,0,0,0,-60.4,-38.54,13.37,-0.62,-70.93,-0.84,-34.74,0.02,20.73,-10.88,-16.01,-12.78,20,9.45,-25.91,59.1306,38.2451,-23.919,22.5,-4.83,-93.1,3.56,-29.05,10.93,0.16,38.48,-0.18,-0.61,-31.52,0.21,-25.77,-56.91,-27.01,-0.15,31.99,0.16,3.95,-22.91,-0.36,-10.74,-15.8,24.83,0,0,0,60.72,-8.8,48.77,0.26,-38.04,0.41,23.6,-0.04,-6.89,0,0,0,-59.95,-37.34,11.34,-0.54,-67.74,-0.75,-34.26,0.22,19.27,-11.14,-16.22,-12.87,20.11,9.51,-25.93,58.7591,38.1628,-24.733,23.23,-6.28,-94.87,3.41,-27.58,10.73,0.16,36.04,-0.17,-0.35,-31.77,0.25,-27.27,-57.08,-22.06,-0.15,29.89,0.15,-2.72,-32.41,-0.72,-11.18,-17.27,24.76,0,0,0,60.79,-7.14,47.19,0.25,-36.53,0.4,22.97,-0.02,-6.4,0,0,0,-59.04,-35.14,8.85,-0.46,-63.91,-0.67,-33.46,0.35,17.51,-11.42,-16.26,-12.69,20.47,9.91,-25.7,58.3187,37.9867,-25.6619,23.88,-7.54,-97.11,3.69,-25.85,10.21,0.15,33.79,-0.16,0.07,-32.18,0.31,-31.62,-56.41,-30.67,-0.15,29.01,0.15,-7.56,-37.89,-2.28,-10.88,-18.69,24.6,0,0,0,60.33,-7.05,50.99,0.25,-34.22,0.39,21.52,-0.17,-5.65,0,0,0,-58.63,-32.72,6.62,-0.4,-59.89,-0.6,-32.46,0.45,15.69,-11.67,-16.56,-12.3,20.8,10.46,-24.97,57.8055,37.8835,-26.6825,24.74,-8.88,-100.17,4.04,-23.82,9.73,0.15,30.89,-0.16,0.54,-32.06,0.39,-32.76,-57.16,-36.69,-0.15,30.1,0.15,-9.77,-39.88,-3.22,-11.26,-20.8,24.38,0,0,0,61.02,-6.17,51.43,0.24,-32.19,0.38,20.17,-0.28,-5.04,0,0,0,-57.33,-29.63,4.44,-0.37,-56.78,-0.56,-31.6,0.52,14.33,-10.91,-17.3,-11.77,21.18,11.12,-24.02,57.1241,37.8049,-27.7955,24.69,-10.95,-103.85,3.7,-19.97,10.46,0.14,26.6,-0.14,0.55,-31,0.38,-32.27,-58.41,-40.58,-0.15,33.04,0.16,-12.45,-41.64,-4.42,-12.1,-22.66,24.28,0,0,0,61.77,-4.79,49.94,0.24,-31.04,0.37,19.33,-0.33,-4.71,0,0,0,-56.04,-26.17,2.68,-0.34,-53.64,-0.53,-30.63,0.56,12.99,-10.04,-17.6,-10.87,21.32,11.51,-22.54,56.4119,37.7886,-29.0674,24.53,-13.16,-107.54,3.41,-15.53,12.03,0.14,21.21,-0.13,-0.23,-28.44,0.3,-32.58,-60.23,-45.05,-0.16,36.44,0.17,-11.75,-40.8,-3.98,-12.98,-24.78,23.33,0,0,0,62.37,-3.75,48.9,0.23,-29.91,0.37,18.3,-0.39,-4.4,0,0,0,-54.75,-22.57,1.66,-0.32,-50.45,-0.5,-29.56,0.58,11.66,-9.12,-17.59,-9.61,21.37,12.13,-20.64,55.5992,37.8731,-30.4708,23.88,-15.15,-111.13,3.28,-10.8,13,0.13,16.21,-0.12,-1.85,-23.9,0.33,-33.01,-60.67,-49.57,-0.16,39.03,0.18,-4.34,-33.67,-1.01,-13.71,-26.45,21.93,0,0,0,62.58,-3.54,47.38,0.23,-28.79,0.36,17.26,-0.4,-4.12,0,0,0,-53.57,-18.64,0.58,-0.3,-47.62,-0.47,-28.44,0.51,10.5,-8.25,-17.18,-8.1,21.41,12.63,-18.48,54.7932,37.9653,-31.9957,22.85,-16.38,-115.16,4.72,-7.94,13.49,0.13,16.08,-0.12,-2.99,-18.97,0.62,-31.09,-59.72,-52.52,-0.17,40.65,0.19,0.81,-26.56,-0.17,-13.99,-28.34,20.77,0,0,0,62.53,-4.24,46.19,0.23,-28.41,0.36,16.83,-0.38,-4.03,0,0,0,-51.47,-13.78,-1.24,-0.29,-45.62,-0.46,-27.59,0.44,9.71,-6.38,-16.4,-6.31,20.84,13.34,-16.05,54.0626,38.0846,-33.5978,21.31,-16.73,-120.06,8,-7.49,13.63,0.14,22.01,-0.13,-3.16,-13.14,0.98,-24.61,-58.04,-49.71,-0.17,41.05,0.19,2.05,-23.73,-0.21,-12.97,-29.06,20.18,0,0,0,61.51,-5.6,46.38,0.23,-27.65,0.36,16.26,-0.36,-3.85,0,0,0,-49.49,-8.36,-2.34,-0.29,-44.88,-0.45,-27.19,0.36,9.41,-4.36,-16.06,-4.63,19.43,13.94,-13.24,53.353,38.5164,-35.2325,19.35,-17.22,-125.29,10.93,-8.77,11.56,0.15,30.2,-0.15,-2.29,-3.1,1.2,-15.84,-55.74,-40.7,-0.17,39.91,0.19,1.99,-23.16,-0.23,-11.52,-28.59,19.73,0,0,0,59.92,-7.4,46.3,0.23,-26.3,0.35,15.43,-0.33,-3.52,0,0,0,-48.75,-3.47,-6.76,-0.28,-43.67,-0.45,-26.7,0.35,8.95,-3.36,-16.1,-3.08,18.51,14.51,-10.39,52.9042,38.8791,-36.7213,17.56,-18.25,-129.31,13.22,-12.61,9.64,0.16,38.82,-0.18,1.71,8.41,-0.73,-9.19,-53.53,-32.1,-0.16,38.46,0.18,1.48,-23.95,-0.21,-11.46,-27.96,17.58,0,0,0,58.69,-9.44,43.41,0.23,-25.79,0.35,14.94,-0.28,-3.41,0,0,0,-48.19,1.51,-11.08,-0.28,-43.09,-0.44,-26.41,0.32,8.73,-2.37,-15.97,-1.77,17.72,14.82,-7.97,52.4626,39.0298,-38.0505,15.67,-19.11,-134.46,14.16,-16.05,9.2,0.19,46.8,-0.21,2.96,9.41,-1.52,-3.79,-51.19,-25.19,-0.16,37.43,0.18,0.85,-25.05,-0.19,-11.7,-27.13,16.25,0,0,0,58.41,-12.9,41.63,0.22,-25,0.35,14.16,-0.18,-3.25,0,0,0,-46.89,6.33,-16.34,-0.27,-42.38,-0.44,-26,0.24,8.46,-1.28,-16.35,-1.08,17.53,14.85,-6.62,52.1216,39.0972,-39.2721,13.74,-19.81,-140.92,14.67,-18.99,10.11,0.21,53.06,-0.25,0.81,5.11,-0.16,0.88,-48.73,-19.73,-0.16,36.72,0.17,0.5,-25.73,-0.19,-10.62,-25.6,15.26,0,0,0,57.75,-16.19,40.81,0.22,-24.11,0.34,13.38,-0.06,-3.07,0,0,0,-46.71,9.56,-21.01,-0.27,-41.46,-0.43,-25.52,0.18,8.11,-1.02,-17,-0.8,17.17,14.77,-5.76,51.8434,39.1204,-40.4089,10.85,-20.95,-148.67,14.26,-21.69,12.15,0.23,56.42,-0.27,-1.23,-0.23,0.81,3.99,-46.43,-14.9,-0.16,36.37,0.17,0.49,-25.8,-0.19,-10.85,-24.61,14.2,0,0,0,58.12,-19.15,38.88,0.22,-23.29,0.34,12.62,0.08,-2.92,0,0,0,-45.82,12.27,-24.94,-0.27,-40.69,-0.43,-25.01,0.08,7.82,-0.31,-16.86,-1.01,17.33,14.41,-6.26,51.6546,39.1343,-41.3575,8.45,-22.08,-156.25,13.98,-25.43,13.03,0.23,56.79,-0.27,-2.15,-6.27,1,6.41,-44.91,-11.38,-0.16,36.23,0.17,0.62,-25.61,-0.19,-10.72,-24.32,11.82,0,0,0,58.75,-20.99,35.7,0.22,-22.87,0.34,12.23,0.17,-2.84,0,0,0,-45.5,14.06,-26.89,-0.26,-39.42,-0.42,-24.24,-0.03,7.36,0.21,-15.82,-1.92,18.09,13.42,-8.4,51.3506,39.1164,-42.2798,4.73,-22.86,-165.23,12.11,-28.24,12.49,0.22,54.49,-0.26,-2.61,-12.5,0.85,7.15,-43.15,-8.47,-0.16,36.58,0.17,0.78,-25.34,-0.19,-9.68,-24.94,8.63,0,0,0,57.59,-19.87,31.34,0.22,-23.65,0.34,12.54,0.21,-3.03,0,0,0,-47.3,14.95,-26.01,-0.26,-38.41,-0.41,-23.64,-0.11,7.01,0.11,-13.44,-2.58,18.42,13.62,-10.57,51.0678,39.055,-43.1676,1.05,-22.8,-175.41,10.71,-30.61,10.68,0.21,51.41,-0.24,-2.32,-18.08,0.55,8.49,-41.4,-4.3,-0.16,37.25,0.18,0.89,-25.12,-0.19,-7.04,-25.39,6.6,0,0,0,55.44,-19.5,29.49,0.22,-24.11,0.34,12.54,0.35,-3.16,0,0,0,-50.3,15.32,-24.14,-0.26,-37.83,-0.41,-23.1,-0.21,6.8,-1.6,-10.66,-3.4,19.44,13.62,-13.3,50.7091,39.0129,-43.7992,-2.73,-22.85,174.05,9.32,-34.07,7.19,0.19,48.5,-0.22,-1.34,-22.4,0.33,9.63,-40.77,0.64,-0.16,37.98,0.18,0.98,-24.64,-0.19,-7.71,-25.19,5.29,0,0,0,56.71,-21.41,26.31,0.22,-24.81,0.35,12.91,0.34,-3.32,0,0,0,-49.54,15.83,-24.83,-0.25,-36.75,-0.4,-22.04,-0.37,6.44,-1.34,-9.24,-5.23,20.94,12.87,-17.53,50.3041,39.0696,-44.4118,-6.94,-22.08,162.51,8.02,-36.86,2.36,0.18,45.22,-0.21,-0.71,-24.43,0.29,10.5,-40.36,6.27,-0.16,38.78,0.18,0.97,-23.49,-0.21,-6.59,-24.49,3.8,0,0,0,56.06,-21.43,24.8,0.23,-26.29,0.35,13.56,0.4,-3.69,0,0,0,-51.1,14.12,-24.59,-0.25,-34.89,-0.39,-20.53,-0.44,5.86,-2.54,-8.35,-6.09,22.09,12.41,-21.25,49.8465,39.233,-44.9951,-11.28,-20.23,150.7,7.24,-38.77,-1.96,0.17,41.01,-0.19,-1,-23.25,0.31,10.71,-40.55,10.93,-0.17,40.01,0.19,0.66,-21.46,-0.22,-5.35,-23.4,3,0,0,0,55.36,-21.36,22.14,0.23,-27.63,0.36,14.19,0.41,-4.03,0,0,0,-53.16,12.89,-22.78,-0.24,-33.87,-0.39,-19.49,-0.43,5.57,-4.91,-7.26,-7.6,23.73,11.57,-24.86,49.3448,39.3526,-45.6078,-15.9,-17.53,138.24,6.86,-40.13,-4.11,0.16,36.43,-0.17,-0.98,-22.29,0.34,9.9,-41.79,12.59,-0.17,41.54,0.19,0.05,-19.58,-0.19,-6.16,-23.25,2.57,0,0,0,55.91,-21.95,19.61,0.23,-28.65,0.36,14.7,0.4,-4.3,0,0,0,-53.23,12.15,-20.89,-0.24,-32.91,-0.38,-18.39,-0.34,5.32,-5.52,-6.4,-9,25.59,11.8,-28.73,48.8816,39.5165,-46.2072,-19.54,-14.42,126.22,7.26,-41.02,-4.97,0.15,33.61,-0.16,-0.89,-20.98,0.36,9.06,-42.79,11.19,-0.17,42.08,0.19,-0.58,-18,-0.11,-6.29,-22.88,2.04,0,0,0,56.89,-21.86,17.39,0.23,-30.01,0.37,15.31,0.43,-4.68,0,0,0,-53.4,11.04,-19.16,-0.24,-32.39,-0.38,-17.62,-0.19,5.22,-5.91,-5.95,-10.24,27.03,11.63,-31.8,48.3814,39.6968,-46.8359,-21.9,-10.33,114.74,7.73,-40.32,-4.5,0.15,33.82,-0.16,-0.92,-19.41,0.39,7.2,-42.53,7.93,-0.17,40.86,0.19,-0.88,-17.6,-0.08,-6.08,-22.69,1.81,0,0,0,56.93,-20.73,14.35,0.24,-32.06,0.38,16.12,0.52,-5.29,0,0,0,-54.32,10.81,-16.31,-0.24,-32.71,-0.38,-17.43,-0.07,5.35,-6.5,-4.67,-11.05,28.22,11.24,-34.48,47.8017,39.7381,-47.5066,-23.52,-6.26,102.87,8.76,-39.37,-2,0.16,35.92,-0.17,-1,-19.75,0.39,4.68,-42.27,3.41,-0.16,38.07,0.18,-0.31,-20.22,-0.18,-5.16,-22.3,2.34,0,0,0,56.73,-19.3,11.49,0.25,-34.67,0.39,17.2,0.59,-6.1,0,0,0,-55.51,9.83,-14.02,-0.24,-33.78,-0.39,-17.62,0.06,5.7,-6.97,-4.57,-11.9,29.05,11.59,-36.46,47.2178,39.6207,-48.2111,-24.94,-1.29,90.42,9.29,-38.17,1.05,0.16,37.24,-0.18,-1.11,-21.86,0.35,2.03,-43.21,1.19,-0.16,35.34,0.17,0.98,-23.74,-0.23,-4.23,-23.22,3.73,0,0,0,55.44,-16.58,7.5,0.26,-37.98,0.41,18.56,0.63,-7.19,0,0,0,-57.17,8.99,-10.51,-0.25,-36.03,-0.4,-18.43,0.15,6.43,-7.55,-3.78,-12.19,29.31,11.62,-37.59,46.7302,39.6142,-48.9733,-25.03,4.68,78.36,8.48,-35.91,3.84,0.16,36.4,-0.17,-1.13,-23.14,0.32,-0.44,-45.48,1.1,-0.15,34.1,0.17,1.23,-24.2,-0.22,-5.38,-23.95,5.22,0,0,0,55.87,-14.16,1.92,0.27,-41.34,0.43,19.92,0.62,-8.36,0,0,0,-57.34,8.86,-7.39,-0.26,-39.11,-0.42,-19.6,0.21,7.48,-6.4,-3.31,-12.33,28.89,11.32,-37.81,46.23,39.7185,-49.4925,-24.05,9.29,67.6,8.44,-33.56,6.73,0.16,34.53,-0.17,-1.1,-24.02,0.31,-0.77,-47.2,2.84,-0.15,34.02,0.16,1.33,-24.4,-0.22,-6.48,-25.52,5.61,0,0,0,55.27,-13.04,-0.56,0.28,-42.92,0.44,20.35,0.8,-8.98,0,0,0,-56.96,9.97,-3.4,-0.28,-42.47,-0.44,-20.8,0.27,8.69,-4.66,-1.03,-11.68,28.6,10.32,-37.69,45.7788,39.6966,-50.043,-21.97,13.58,57.86,7.37,-31.25,6.85,0.15,32.72,-0.16,-0.95,-25.3,0.29,-3.07,-48.11,-0.29,-0.16,34.37,0.17,1.61,-27.58,-0.12,-4.27,-24.1,4.58,0,0,0,50.96,-12.25,0,0.29,-44.73,0.45,21.01,0.8,-9.66,0,0,0,-61.01,7.98,0.36,-0.29,-45.72,-0.46,-21.98,0.27,9.9,-7.34,-3.11,-10.99,27.78,12.16,-35.14,45.2831,39.6018,-50.4975,-19.64,16.54,48.22,7.63,-29.4,7.49,0.15,31.55,-0.16,-0.87,-26.36,0.27,-4.16,-48.56,-2.99,-0.16,34.32,0.17,0.82,-29.26,-0.15,-5.15,-23.43,4.18,0,0,0,51.13,-13.73,-1.91,0.29,-45.82,0.46,21.52,0.69,-10.04,0,0,0,-60.6,8.43,2.16,-0.31,-49.04,-0.49,-23.11,0.26,11.21,-5.67,-4.57,-10.74,26.23,13.49,-33.23,44.7979,39.6763,-50.9185,-16.56,19.43,38.39,7.33,-27.9,8.16,0.15,30.36,-0.15,-0.94,-26.26,0.27,-4.09,-49.07,-1.08,-0.15,34.2,0.17,0.54,-27.49,-0.19,-5.29,-23.26,3.47,0,0,0,50.55,-14.36,-3.8,0.3,-46.86,0.47,22.05,0.53,-10.41,0,0,0,-61.72,8.57,4.72,-0.33,-52.34,-0.51,-24.25,0.17,12.54,-5.23,-5.27,-9.48,24.51,14.3,-29.86,44.3631,39.6863,-51.2617,-12.91,21.6,28.83,6.86,-26.08,9.56,0.15,29.27,-0.15,-0.97,-26.75,0.26,-5.45,-49.47,-2.04,-0.15,34.11,0.17,0.86,-25.92,-0.2,-6,-22.98,2.47,0,0,0,51.1,-15.27,-6.63,0.3,-47.81,0.48,22.66,0.3,-10.72,0,0,0,-62.09,9.09,6.41,-0.36,-55.56,-0.55,-25.32,0.05,13.87,-4.37,-6.06,-8.09,22.31,14.95,-25.97,43.8857,39.5351,-51.605,-8.3,23.64,18.21,5.71,-24.37,10.98,0.15,28.06,-0.15,-0.95,-27.3,0.25,-6.99,-50.96,-3.5,-0.16,34.37,0.17,0.81,-26.06,-0.2,-7.04,-24.05,2.32,0,0,0,51.43,-15.51,-9.49,0.31,-49.2,0.49,23.47,0.05,-11.21,0,0,0,-62.34,10.34,7.52,-0.39,-58.71,-0.59,-26.44,-0.17,15.19,-3.4,-5.72,-6.18,20.24,15.03,-21.61,43.4761,39.3586,-51.8376,-2.13,25.04,7.26,3.07,-22.31,11.32,0.14,26.08,-0.14,-0.98,-27.18,0.26,-8.79,-53,-2.47,-0.16,35.17,0.17,0.5,-26.92,-0.2,-9.04,-24.92,1.76,0,0,0,51.31,-16.03,-10.88,0.32,-50.72,0.5,24.31,-0.16,-11.77,0,0,0,-62.54,10.7,7.54,-0.42,-60.98,-0.62,-27.41,-0.43,16.13,-2.65,-6.13,-4.4,18.22,15.65,-17.26,42.9655,39.2546,-51.8869,2.46,25.1,-2.24,1.99,-20.06,12.19,0.14,24.07,-0.14,-1.02,-27.45,0.25,-8.59,-54.67,0.08,-0.16,35.65,0.17,-0.26,-28.56,-0.25,-9.77,-24.67,0.92,0,0,0,51.35,-17.8,-11.45,0.33,-52.23,0.51,25.12,-0.34,-12.34,0,0,0,-62.51,11.64,6.57,-0.45,-63.27,-0.65,-28.52,-0.71,17.07,-2.14,-7.64,-2.95,16.42,16.71,-13.31,42.401,39.1349,-51.787,6.17,24.54,-10.86,1.52,-17.73,12.85,0.14,21.99,-0.13,-1.07,-26.95,0.26,-9.04,-56.16,-2.63,-0.16,36.35,0.17,-1.72,-31.51,-0.46,-9.8,-24.88,0.63,0,0,0,51.16,-20.07,-13.05,0.34,-53.46,0.53,25.95,-0.52,-12.79,0,0,0,-62.39,13.32,5.38,-0.47,-64.47,-0.68,-29.45,-0.91,17.54,-2.25,-8.51,-1.68,15.35,17.33,-10.26,41.7905,38.9801,-51.5714,9.91,23.43,-19.48,0.52,-14.82,14.01,0.14,19.57,-0.12,-1.1,-26.88,0.27,-11.25,-57.54,-9.16,-0.16,37.47,0.18,-2.09,-32.06,-0.53,-9.94,-25.47,0.62,0,0,0,50.68,-21.86,-14.82,0.35,-55.01,0.54,27,-0.69,-13.38,0,0,0,-62.01,15.13,4.36,-0.48,-64.82,-0.68,-30.23,-0.99,17.65,-2.17,-9.32,-0.42,14.22,18.02,-7.27,41.0324,39.0249,-51.2179,12.82,22.38,-27.11,0.04,-12.68,12.97,0.13,17.66,-0.12,-1.09,-25.3,0.3,-11.75,-58.21,-11.35,-0.16,37.68,0.18,-2.4,-32.43,-0.59,-9.41,-25.98,0.18,0,0,0,49.31,-23.49,-16.22,0.37,-56.66,0.56,28.04,-0.79,-14.04,0,0,0,-61.47,17.17,2.66,-0.49,-65.38,-0.69,-30.97,-0.98,17.88,-1.88,-10.72,0.84,12.83,19.09,-4.08,40.0884,38.7883,-50.7749,15.19,20.63,-34.02,-0.68,-10.5,11.48,0.13,17.63,-0.12,-1.11,-25.27,0.3,-10.61,-57.67,-8.14,-0.16,36.49,0.17,-3.1,-34.01,-0.8,-9.23,-25.28,-1.61,0,0,0,49.1,-24.47,-16.71,0.39,-58.66,0.59,29.13,-0.83,-14.88,0,0,0,-59.84,17.4,-0.35,-0.48,-64.92,-0.69,-31.39,-0.89,17.68,0.21,-13.01,2.31,9.5,20.61,0.34,38.9683,38.5227,-50.1689,16.39,18.54,-40.33,-1.23,-7.63,10.36,0.13,18.31,-0.12,-1.17,-24.85,0.31,-9.11,-55.61,-4.95,-0.16,35.33,0.17,-2.97,-33.84,-0.78,-8.46,-25.52,-4.17,0,0,0,48.66,-23.17,-17.82,0.42,-61.01,0.62,30.23,-0.83,-15.91,0,0,0,-59.22,17.58,-0.6,-0.51,-66.37,-0.72,-32.39,-0.73,18.37,3.16,-12.94,4.28,5.1,21.94,5.66,37.7792,38.3447,-49.483,17.3,16.5,-46.71,-2.32,-4.56,9.36,0.14,18.45,-0.12,-1.35,-23.27,0.35,-11.9,-53.97,-18.49,-0.16,35.67,0.17,-0.41,-28.54,-0.26,-6.62,-26.44,-4.42,0,0,0,46.58,-23.29,-20.05,0.44,-62.36,0.64,30.95,-0.79,-16.52,0,0,0,-58.66,18.1,-4.2,-0.5,-66.17,-0.71,-32.71,-0.57,18.31,4.01,-11.25,5.75,2.2,21.82,9.59,36.4364,38.3161,-48.8838,17.64,14.94,-53.16,-2.89,-1.81,10.12,0.14,18.64,-0.12,-1.77,-20.58,0.44,-10.31,-52.83,-23.45,-0.16,36.64,0.17,1.14,-23.52,-0.23,-3.98,-26.71,-3.84,0,0,0,44.19,-24.15,-21.34,0.46,-63.65,0.66,31.56,-0.73,-17.12,0,0,0,-58.09,17.95,-8.73,-0.51,-66.41,-0.72,-33.09,-0.4,18.47,4.7,-10,7.05,-0.25,21.5,13.17,35.066,38.414,-48.2974,17.55,13.19,-59.2,-3.33,-0.66,11.07,0.14,21.79,-0.13,-2.2,-17.22,0.61,-3.77,-51.57,-15.41,-0.16,37.17,0.18,1.08,-22.39,-0.24,-1,-27.72,-3.91,0,0,0,40.17,-23.54,-21.98,0.47,-64.34,0.67,31.97,-0.66,-17.44,0,0,0,-57.78,17.99,-12.12,-0.54,-67.98,-0.75,-33.74,-0.24,19.25,4.46,-6.24,8.27,-2.32,19.79,16.76,33.6678,38.511,-47.8135,16.22,11.9,-64.24,-2.19,-1,12.18,0.15,28.34,-0.15,-2.56,-11.61,0.92,4.16,-48.17,-3.02,-0.16,36.47,0.17,0.78,-23.81,-0.21,1.42,-27.32,-4.71,0,0,0,36.68,-23.42,-22.67,0.47,-64.16,0.67,32.22,-0.54,-17.39,0,0,0,-55.51,17.74,-17.01,-0.57,-68.97,-0.78,-34.21,-0.07,19.76,4.32,-3.32,9.12,-3.73,18.74,19.45,32.3765,38.6917,-47.2772,15.47,10.36,-67.6,-1.37,-2.97,13.1,0.16,35.66,-0.17,-2.61,-3.83,1.29,7.45,-44.88,4.74,-0.16,35.42,0.17,0.97,-25.09,-0.19,0.41,-25.72,-7.06,0,0,0,35.2,-25.4,-23.79,0.44,-62.56,0.64,32.15,-0.34,-16.7,0,0,0,-51.26,17.23,-23.21,-0.57,-69,-0.78,-34.46,0.14,19.84,6.15,-2.68,9.52,-5.04,18.66,21.25,31.1465,38.9194,-46.787,15.3,8.88,-70.62,-0.54,-5.48,14.95,0.17,41.4,-0.19,-2.48,4.56,1.58,9.03,-42.29,9.1,-0.16,35,0.17,1.07,-24.07,-0.21,-0.49,-25.23,-9.52,0,0,0,33.13,-27.03,-24.54,0.41,-60.06,0.6,31.75,-0.14,-15.62,0,0,0,-48.99,17.66,-27.46,-0.56,-68.63,-0.77,-34.56,0.32,19.72,6.51,-1.41,10.07,-5.37,18.09,22.75,30.0458,39.0551,-46.311,15.37,7.37,-73.86,0.14,-7.72,17.62,0.18,45.47,-0.21,-2.59,7.29,1.75,9.29,-40.56,10.15,-0.16,35.52,0.17,0.76,-21.91,-0.24,-0.82,-25.05,-10.83,0,0,0,30.75,-28.86,-25.27,0.38,-58.04,0.58,31.32,-0.02,-14.75,0,0,0,-48.44,19.52,-30.35,-0.53,-67.33,-0.74,-34.4,0.46,19.14,5.76,-0.8,10.62,-5.95,17.64,24.12,29.0578,39.1133,-45.7945,15.06,5.6,-77.24,0.53,-9.42,20.41,0.19,48.86,-0.23,-3.86,2.72,2.18,9.12,-38.87,11.31,-0.16,36.64,0.17,0.56,-20.95,-0.24,-2.95,-23.57,-10.79,0,0,0,30.77,-31.53,-27.15,0.37,-56.93,0.56,31.07,0.05,-14.27,0,0,0,-46.09,23.06,-33.74,-0.49,-65.66,-0.7,-34.07,0.53,18.37,6.6,-0.91,10.81,-6.45,16.82,24.76,28.2042,39.0912,-45.2913,14.88,4.12,-79.59,1.67,-12.57,22.67,0.21,52.89,-0.25,-4.78,-3.51,2.12,9.62,-37.02,15.73,-0.16,37.94,0.18,0.91,-22.45,-0.22,-5.06,-21.71,-10.66,0,0,0,31.18,-34.34,-29.01,0.37,-56.39,0.56,30.92,0.06,-14.04,0,0,0,-43.45,25.94,-38.2,-0.45,-63.45,-0.66,-33.55,0.57,17.36,6.93,-1.42,11.1,-6.23,15.9,25,27.4721,39.1076,-44.8127,14.97,3.88,-79.88,4.55,-17.56,23.8,0.24,57.45,-0.28,-4.85,-7.17,1.82,9.9,-35.91,17.81,-0.17,39.07,0.18,1.1,-23.55,-0.2,-5.85,-20.54,-11.95,0,0,0,30.87,-36.25,-30.63,0.37,-56.71,0.56,30.94,0.01,-14.17,0,0,0,-41.34,28.83,-41.34,-0.45,-62.86,-0.65,-33.4,0.57,17.08,6.44,-1.8,11.3,-6.04,14.95,25.06,26.8197,39.0918,-44.3227,14.85,4.32,-78.93,8.21,-22.96,24.4,0.27,61.35,-0.31,-4.05,-11.53,1.24,9.63,-35.05,17.34,-0.17,39.75,0.19,1.21,-24.63,-0.17,-6.31,-18.69,-13.6,0,0,0,32.08,-38.11,-32.45,0.38,-57.96,0.58,31.25,-0.05,-14.7,0,0,0,-38.48,31.54,-44.16,-0.45,-62.91,-0.65,-33.4,0.55,17.1,6.38,-2.56,11.26,-6.28,13.59,24.8,26.2458,39.0194,-43.8361,14.81,5.19,-77.18,12.19,-29.23,24.95,0.3,64.33,-0.35,-3.59,-14.32,0.94,9.01,-34.18,15.83,-0.17,40.13,0.19,1.33,-26.3,-0.13,-6.08,-16.84,-15.64,0,0,0,34.28,-39.43,-33.21,0.41,-60.28,0.61,31.77,-0.17,-15.71,0,0,0,-36.62,31.92,-47.45,-0.41,-60.51,-0.61,-32.59,0.41,15.96,6.19,-3.65,11.1,-6.77,12.66,24.39,25.6555,38.9993,-43.4016,14.69,6.35,-75.39,16.45,-35.12,26.28,0.31,65.79,-0.36,-3.51,-14.81,0.89,8.92,-33.38,13.58,-0.17,40.74,0.19,1.23,-26.79,-0.12,-5.72,-15.74,-17.05,0,0,0,36.74,-39.99,-33.67,0.45,-62.85,0.65,32.34,-0.27,-16.85,0,0,0,-35.03,33.89,-47.64,-0.39,-58.68,-0.59,-31.82,0.2,15.08,6.09,-4.09,10.67,-6.64,11.77,23.32,25.1007,38.8559,-42.9273,14.62,7.25,-73.33,19.76,-40.72,27.13,0.3,64.86,-0.35,-2.96,-16.31,0.71,8.6,-32.44,11.66,-0.17,41.44,0.19,1.07,-28.51,-0.08,-5.08,-15.02,-18.25,0,0,0,39.16,-40.27,-33.03,0.49,-65.49,0.7,32.9,-0.37,-18.04,0,0,0,-34.26,35.53,-47.98,-0.37,-56.55,-0.56,-30.93,0.04,14.11,5.54,-4.46,10.19,-6.35,11.27,22.17,24.544,38.62,-42.4812,14.76,8.49,-70.93,22.83,-46.45,27.97,0.27,61.44,-0.31,-2.23,-18.34,0.52,8.72,-31.82,10.47,-0.17,42.02,0.19,0.71,-31.03,-0.08,-4.2,-14.44,-19.56,0,0,0,42.29,-40.42,-30.75,0.54,-67.78,0.75,33.37,-0.44,-19.1,0,0,0,-33.53,35.66,-49.98,-0.35,-54.33,-0.53,-29.9,-0.14,13.11,5.27,-5.36,9.73,-6.03,11.09,20.92,23.9156,38.3802,-42.0024,15.36,9.45,-68.99,25.67,-51.42,30.4,0.23,55.9,-0.27,-1.84,-19.69,0.44,8.54,-31.65,9.22,-0.18,42.95,0.2,0.28,-32.84,-0.12,-3.36,-14.46,-20.09,0,0,0,44.86,-40.48,-27.61,0.56,-68.83,0.78,33.64,-0.43,-19.6,0,0,0,-32.89,35.63,-51.71,-0.34,-53.89,-0.53,-29.45,-0.29,12.89,4.83,-6.1,9.27,-5.42,10.68,19.62,23.2286,38.1738,-41.4466,16.04,10.18,-67.67,28.32,-55.25,33.25,0.2,49.23,-0.23,-1.75,-20.01,0.42,8.2,-31.53,7.34,-0.18,44.11,0.2,-0.21,-34.46,-0.2,-2.85,-15.31,-20.2,0,0,0,46.78,-39.26,-24.16,0.57,-69.11,0.78,33.77,-0.4,-19.74,0,0,0,-33.37,35.72,-52.09,-0.34,-53.79,-0.53,-29.14,-0.41,12.83,4.4,-6.09,8.73,-4.97,10.61,18.43,22.4888,37.9068,-40.8409,16.64,11.2,-66.55,31.01,-58.53,35.78,0.17,42.62,-0.2,-1.64,-20.97,0.4,8.24,-31.21,6.36,-0.18,44.99,0.21,-0.78,-36.27,-0.33,-2.11,-16.06,-19.99,0,0,0,48.94,-37.72,-20.1,0.56,-68.87,0.78,33.79,-0.35,-19.64,0,0,0,-34.24,35.66,-50.96,-0.35,-54.24,-0.53,-28.98,-0.52,13,3.98,-6.66,8.23,-4.41,11.18,17.21,21.6038,37.5988,-40.2299,16.41,12.74,-65.56,34.23,-60.99,36.89,0.16,36.89,-0.17,-1.57,-22.12,0.36,9.36,-29.84,6.4,-0.18,45.11,0.21,-1.45,-37.93,-0.53,-1.22,-15.63,-18.86,0,0,0,51.76,-36.81,-16.08,0.54,-67.7,0.75,33.55,-0.32,-19.1,0,0,0,-32.97,35.83,-49.75,-0.37,-56.65,-0.56,-29.43,-0.65,14.01,4.74,-8.03,7.68,-3.92,11.67,15.64,20.7239,37.2989,-39.4687,16.68,13.58,-65.21,35.34,-63.09,34.25,0.15,31.89,-0.16,-1.3,-24.39,0.3,9.53,-28.26,6.47,-0.18,44.66,0.21,-2.15,-39.63,-0.78,-0.58,-15.57,-17.21,0,0,0,53.97,-35.78,-11.58,0.49,-65.39,0.69,33.15,-0.2,-18.04,0,0,0,-32.64,35.2,-49.24,-0.39,-58.84,-0.59,-29.77,-0.76,14.95,5.06,-9.17,7.05,-3.7,11.73,14.11,19.8961,37.0641,-38.4948,17.28,14.33,-65.27,37.35,-64.61,33.05,0.14,27.79,-0.15,-0.62,-26.97,0.28,9.18,-26.44,6.95,-0.18,43.4,0.2,-2.78,-40.95,-1.04,0.41,-15.89,-15.67,0,0,0,55.87,-34.01,-7,0.45,-62.94,0.65,32.69,-0.07,-16.94,0,0,0,-33.66,33.99,-47.49,-0.41,-60.7,-0.61,-30.03,-0.84,15.77,4.76,-10.32,6.67,-3.13,11.73,13.01,18.8963,36.8621,-37.4696,17.28,15.2,-64.94,41.22,-64.51,38.16,0.14,24.95,-0.14,-0.28,-28.34,0.3,8.7,-23.76,6.39,-0.17,41.6,0.19,-3.03,-41.87,-1.18,1.45,-16.8,-14.23,0,0,0,56.47,-31.87,-3.48,0.41,-59.91,0.6,32,0.06,-15.6,0,0,0,-35.53,33.34,-45.61,-0.44,-62.36,-0.64,-30.17,-0.91,16.52,3.93,-10.46,6.16,-2.6,11.69,11.95,17.8844,36.6511,-36.2742,18,15.46,-64.63,41.39,-64.78,40.95,0.14,23.63,-0.13,0.29,-29.87,0.36,7.2,-21.53,5.72,-0.17,40.07,0.19,-3.17,-42.11,-1.24,1.56,-18.59,-12.76,0,0,0,56.41,-29.6,-0.47,0.37,-56.74,0.56,31.19,0.18,-14.22,0,0,0,-37.81,33.19,-43.33,-0.46,-63.89,-0.67,-30.26,-0.97,17.21,3.24,-10.22,5.57,-2.34,11.88,10.88,16.798,36.4453,-34.9399,18.43,16.11,-64.03,39.66,-64.62,41.59,0.14,22.8,-0.13,0.29,-30.04,0.36,6.05,-18.96,4.71,-0.16,38.51,0.18,-3.17,-41.75,-1.23,1.8,-19.91,-11.1,0,0,0,57.04,-28.05,2.51,0.34,-53.48,0.53,30.26,0.28,-12.85,0,0,0,-39.38,32.55,-41.86,-0.47,-64.32,-0.67,-30.11,-0.98,17.42,3.02,-10.79,4.97,-2.2,12.41,9.67,15.6205,36.2541,-33.3761,19,16.15,-63.33,35.92,-63.8,40.84,0.14,22.3,-0.13,0.23,-30.32,0.35,4.01,-15.96,3.69,-0.16,36.4,0.17,-2.75,-40.6,-1.05,2.11,-20.72,-9.69,0,0,0,57.28,-27.03,6.48,0.31,-49.78,0.49,29.02,0.33,-11.33,0,0,0,-41.61,30.63,-40.35,-0.47,-64.16,-0.67,-29.8,-0.96,17.37,2.32,-11.88,4.48,-2.32,12.75,8.78,14.3325,36.1471,-31.6177,19.59,16.06,-63.26,34.21,-63.08,42.15,0.14,23.6,-0.13,-0.29,-28.92,0.3,2.05,-11.8,3.31,-0.15,32.66,0.16,-2.19,-38.78,-0.82,2.95,-22.06,-8.04,0,0,0,57.1,-24.58,9.3,0.3,-47.16,0.47,28.07,0.35,-10.29,0,0,0,-44.57,28.43,-38.43,-0.45,-63.43,-0.66,-29.54,-0.93,17.04,1.21,-12.72,4.1,-2.08,13.3,8.09,13.0421,36.3681,-29.7537,21,15.51,-62.97,31.84,-63.87,43.62,0.14,26.4,-0.14,-0.94,-21.82,0.36,-0.52,-7.96,3.63,-0.15,28.1,0.15,-1.11,-34.32,-0.46,1.66,-24.74,-6.57,0,0,0,57.7,-22.15,10.59,0.29,-44.75,0.45,27.11,0.34,-9.36,0,0,0,-45.76,27.21,-37.44,-0.44,-62.47,-0.64,-29.29,-0.9,16.61,0.83,-13.16,3.32,-1.64,14.37,6.48,11.8229,36.6133,-27.8353,22.62,14.54,-61.9,26.84,-64.59,42.9,0.15,29.02,-0.15,-0.88,-14.26,0.48,-3.49,-4.77,3.52,-0.14,24.74,0.14,0.6,-27.74,-0.24,-0.37,-26.12,-5.63,0,0,0,58.14,-20.87,12.74,0.28,-42.96,0.44,26.33,0.3,-8.68,0,0,0,-45.35,24.99,-38.51,-0.42,-61.07,-0.62,-28.93,-0.86,15.98,0.41,-15.24,2.44,-1.22,15.78,4.63,10.5775,37.0693,-25.9389,23.45,13.56,-61.07,22.99,-63.17,43.64,0.15,31.14,-0.16,-0.11,-8.48,0.34,-5.6,-2.47,2.62,-0.14,23.38,0.13,2.75,-20.06,-0.51,-1.58,-27.7,-4.28,0,0,0,57.42,-18.97,14.51,0.27,-42.04,0.43,25.92,0.28,-8.34,0,0,0,-45.15,23.35,-38.41,-0.4,-59.6,-0.6,-28.59,-0.83,15.33,-0.55,-15.72,1.66,-0.55,16.81,3.07,9.3574,37.6923,-24.1436,23.43,12.51,-60.97,18.76,-60.59,41.23,0.15,32.58,-0.16,0.26,-7.48,0.22,-6.71,-0.89,1.13,-0.14,23.52,0.13,5.43,-11.54,-1.59,-2.76,-28.97,-2.1,0,0,0,57.34,-17.41,15.85,0.27,-41.25,0.43,25.53,0.24,-8.05,0,0,0,-44.15,22.15,-38.43,-0.38,-57.68,-0.57,-28.12,-0.79,14.49,-1.17,-15.31,0.79,0.57,17.82,1.13,8.2295,38.2984,-22.5075,23.19,12.13,-60.82,13.95,-58.08,36.26,0.15,32.98,-0.16,0.04,-9.05,0.29,-6.55,-0.72,-1.94,-0.14,24.29,0.14,9.61,-2.21,-4.24,-2.88,-29.38,-0.66,0,0,0,57.32,-15.86,18.1,0.27,-40.63,0.43,25.1,0.14,-7.81,0,0,0,-43.41,19.75,-38.28,-0.36,-55.73,-0.55,-27.83,-0.77,13.64,-1.94,-15.56,-0.02,1.25,18.6,-0.55,7.1534,38.8495,-21.0311,22.69,12.09,-60.83,10.38,-55.21,32,0.15,32.45,-0.16,-0.22,-10.41,0.36,-5.69,-1.84,-4.15,-0.14,25.82,0.14,13.07,3.68,-7.05,-2.78,-29.75,0.95,0,0,0,57.7,-14.46,19.37,0.27,-40.8,0.43,25.13,0.11,-7.87,0,0,0,-42.5,17.94,-38.02,-0.34,-53.73,-0.53,-27.49,-0.73,12.78,-2.53,-15.11,-1.07,2.46,19.08,-2.89,6.1534,39.2915,-19.633,22.06,11.42,-61.07,7.12,-51.74,28.58,0.15,31.73,-0.16,-0.5,-11.99,0.42,-5.38,-3.37,-5.82,-0.15,28.14,0.15,13.06,4.65,-7.25,-2.16,-29.55,2.81,0,0,0,57.59,-12.89,19.93,0.27,-41.54,0.43,25.43,0.11,-8.13,0,0,0,-42.67,15.95,-37.76,-0.33,-52.38,-0.52,-27.3,-0.69,12.22,-3.61,-14.13,-2.01,3.49,19.43,-5.04,5.2248,39.5887,-18.3249,21.16,10.57,-61.14,4.85,-48.22,27.05,0.15,31.39,-0.16,-0.58,-13.26,0.43,-4.96,-4.6,-8.67,-0.15,30.75,0.15,12.29,3.21,-6.5,-1.53,-29.38,5.49,0,0,0,57.49,-12.65,20.16,0.27,-41.64,0.43,25.35,0.04,-8.15,0,0,0,-43.06,15.11,-37.91,-0.33,-51.69,-0.51,-27.4,-0.65,11.93,-5.6,-12.32,-3.15,5.64,19.34,-8.15,4.3925,39.7717,-17.13,20.26,9.7,-60.92,2.66,-45.02,25.53,0.15,31.29,-0.16,-0.63,-14.75,0.42,-4.63,-5.88,-11.11,-0.15,33.56,0.16,11.48,1.5,-5.72,-1.72,-29.72,7.45,0,0,0,58.15,-12.34,20.2,0.27,-41.84,0.43,25.41,0.02,-8.22,0,0,0,-42.85,15,-37.15,-0.33,-52.42,-0.52,-27.92,-0.61,12.23,-6.34,-9.69,-4.11,7.28,19.02,-11.09,3.6606,39.8947,-16.0095,19.38,8.89,-59.81,0.05,-42.28,23.12,0.15,31.46,-0.16,-0.66,-15.52,0.42,-4.3,-6.99,-13.05,-0.16,36.16,0.17,10.08,-1.16,-4.54,-1.88,-29.71,7.7,0,0,0,58.64,-11.4,20.05,0.28,-42.46,0.44,25.68,0.03,-8.45,0,0,0,-43,14.87,-35.21,-0.35,-54.05,-0.53,-28.74,-0.57,12.91,-6.76,-7.42,-4.74,8.27,18.8,-13.21,3.0128,40.0375,-15.0004,18.29,8.74,-58,-0.9,-40.2,23.05,0.15,32.23,-0.16,-0.33,-14.84,0.37,-3.34,-7.77,-14.37,-0.16,37.94,0.18,8.65,-3.48,-3.54,-1.55,-29.73,7.61,0,0,0,58.4,-11.32,20.03,0.28,-42.97,0.44,25.84,0,-8.63,0,0,0,-43.3,15.17,-33.69,-0.36,-56.06,-0.55,-29.68,-0.51,13.78,-7.47,-5.01,-5.25,9.17,18.3,-15.17,2.4672,40.1832,-14.0707,17.01,8.47,-56.2,-2.03,-38.29,21.58,0.15,33.38,-0.16,-0.23,-14.59,0.35,-2.45,-8.26,-14.33,-0.16,38.7,0.18,6.75,-5.98,-2.49,-1.92,-28.82,8.36,0,0,0,58.6,-12.85,20.08,0.28,-43.21,0.44,25.97,0.01,-8.72,0,0,0,-42.58,15.81,-34.21,-0.38,-58.08,-0.58,-30.52,-0.46,14.67,-7.91,-2.94,-6.06,10.5,17,-17.81,2.0022,40.2949,-13.2202,15.69,8.22,-54.85,-2.71,-36.77,20.3,0.16,34.98,-0.17,-0.24,-14.3,0.35,-1.52,-8.92,-12.08,-0.16,38.15,0.18,3.67,-10.64,-1.12,-1.49,-27.97,8.85,0,0,0,58.4,-13.1,20.28,0.28,-43.61,0.45,26.16,0.03,-8.87,0,0,0,-42.4,16.27,-33.7,-0.41,-60.63,-0.61,-31.48,-0.39,15.81,-8.19,-1.17,-6.52,11.15,16.09,-19.45,1.6324,40.3547,-12.4736,14.54,7.82,-53.74,-3.19,-35.75,19.47,0.16,37.1,-0.18,-0.24,-13.56,0.35,-0.48,-10.31,-7.72,-0.16,36.52,0.17,1.42,-16.63,-0.41,-1.04,-26.87,8.88,0,0,0,58.18,-12.73,20.81,0.28,-43.83,0.45,26.25,0.03,-8.95,0,0,0,-42.75,15.57,-33.26,-0.44,-62.22,-0.64,-32.11,-0.3,16.55,-8.16,-0.03,-6.73,11.2,15.6,-20.15,1.3792,40.3867,-11.7935,13.54,7.43,-52.39,-3.49,-35.42,18.98,0.17,39.77,-0.19,-0.11,-12.26,0.32,0.25,-12.21,-4.19,-0.16,34.87,0.17,0.74,-21.48,-0.26,-0.9,-25.18,8.8,0,0,0,58.05,-12.95,21.38,0.28,-43.94,0.45,26.25,0,-8.99,0,0,0,-42.88,13.68,-34.92,-0.45,-63.44,-0.66,-32.43,-0.32,17.11,-8.37,0.5,-6.98,11.36,15.18,-20.85,1.3087,40.352,-11.1891,12.4,7.04,-50.39,-3.88,-35.58,18.24,0.18,42.94,-0.2,0.1,-10.47,0.27,0.57,-14.08,-2.25,-0.16,34.3,0.17,0.82,-25.08,-0.21,-1.5,-23.29,7.95,0,0,0,58.71,-13.28,21.72,0.28,-44.08,0.45,26.31,0.01,-9.04,0,0,0,-42.7,13.73,-34.14,-0.48,-64.94,-0.69,-32.96,-0.25,17.82,-8.07,1,-7.3,11.56,14.06,-21.52,1.4267,40.3905,-10.7002,11.34,6.36,-48.38,-3.95,-36.22,18.78,0.19,46.49,-0.21,0.57,-6.83,0.1,0.01,-15.87,-1.97,-0.16,34.94,0.17,0.82,-25.03,-0.21,-1.68,-20.74,7.53,0,0,0,58.64,-13.73,21.58,0.29,-44.73,0.45,26.68,0.07,-9.3,0,0,0,-43.39,14.3,-32.96,-0.5,-65.99,-0.71,-33.39,-0.14,18.33,-8.66,0.97,-7.63,12.18,13.11,-22.42,1.6265,40.4041,-10.3868,9.62,6.27,-46.52,-2.05,-37.54,20.98,0.2,50.87,-0.24,1.27,-2.24,-0.24,0.5,-16.44,-2.49,-0.16,35.72,0.17,0.73,-23.28,-0.23,-1.11,-17.7,7.66,0,0,0,58.65,-14.77,21.42,0.29,-45.35,0.46,27.02,0.12,-9.54,0,0,0,-43.5,14.52,-33.18,-0.51,-66.72,-0.72,-33.66,-0.08,18.7,-8.85,0.45,-8.16,12.68,12.15,-23.39,1.8829,40.2693,-10.1995,8.38,6.6,-44.49,0.93,-40,25.28,0.23,56.06,-0.27,1.5,2.5,-0.47,1.53,-16.1,-2.91,-0.16,36.39,0.17,0.77,-23.76,-0.21,0.06,-14.47,7.01,0,0,0,58.29,-15.45,21.86,0.29,-46.07,0.46,27.33,0.13,-9.82,0,0,0,-44.38,14.43,-33.06,-0.55,-68.3,-0.76,-34.15,0.01,19.47,-9.59,-1.5,-8.86,12.51,11.22,-23.71,2.1953,39.7628,-10.105,8.24,7.39,-42.7,3.78,-43.3,30.69,0.26,60.66,-0.31,0.41,3.38,0.06,2.63,-16.4,-3.59,-0.16,36.94,0.17,0.75,-26.51,-0.17,1.25,-12.38,6.21,0,0,0,57.87,-15.52,21.87,0.3,-47.05,0.47,27.68,0.11,-10.19,0,0,0,-45.7,14.63,-31.83,-0.61,-70.47,-0.82,-34.62,0,20.51,-11.12,-3.7,-9.57,12.55,10.1,-23.88,2.4501,39.2585,-9.9981,8.55,8.89,-41.41,7.44,-47.15,35.55,0.28,62.43,-0.32,1.34,2.42,-0.39,3.82,-17.3,-3.59,-0.16,37.36,0.18,0.32,-30.18,-0.16,1.54,-11.63,5.99,0,0,0,58.41,-15.62,21.66,0.3,-48.24,0.48,28.03,0.04,-10.65,0,0,0,-45.05,14.85,-31.77,-0.67,-72.43,-0.89,-34.88,-0.13,21.42,-11.29,-5.94,-10.33,12.96,9.22,-24.3,2.7217,38.7427,-9.883,9.14,10.62,-40.84,11.4,-50.97,39.66,0.26,60.74,-0.31,2.69,-2.61,-0.81,4.33,-19.02,-3.99,-0.16,38.27,0.18,-0.27,-33.61,-0.24,2.44,-11.97,5.63,0,0,0,57.69,-14.07,21.62,0.32,-50.24,0.5,28.59,-0.06,-11.42,0,0,0,-45.1,14.28,-31.14,-0.73,-73.82,-0.95,-34.95,-0.3,22.04,-11.67,-7.87,-10.89,12.86,8.74,-24.27,2.95,38.3257,-9.6521,9.62,11.98,-40.39,14.39,-53.6,42.43,0.23,56.83,-0.27,1.39,-9.3,-0.11,4.23,-20.97,-4.39,-0.17,40.29,0.19,-0.62,-35.75,-0.32,3.29,-11.9,5.43,0,0,0,56.52,-12.55,22.33,0.33,-52.51,0.52,29.21,-0.17,-12.34,0,0,0,-45.01,13.2,-30.59,-0.78,-74.96,-1.01,-34.93,-0.46,22.55,-12.25,-9.61,-11.51,12.66,8.57,-24.42,3.1452,38.0562,-9.2718,10.17,12.87,-39.52,15.07,-54.96,43.47,0.21,51.55,-0.24,-0.21,-14.65,0.32,2.92,-22.71,-6.34,-0.17,42.46,0.2,-0.31,-36.66,-0.24,3.18,-11.66,5.14,0,0,0,55.86,-11.74,23.24,0.35,-54.06,0.53,29.58,-0.26,-12.97,0,0,0,-44.48,11.81,-30.8,-0.78,-74.97,-1.01,-34.77,-0.57,22.53,-12.46,-10.71,-11.96,13.27,8.6,-24.93,3.2698,38.008,-8.7952,10.19,13.9,-38.02,15.48,-56.33,41.39,0.18,45.82,-0.21,-0.92,-16.64,0.42,2.07,-23.35,-8.22,-0.18,43.26,0.2,-0.08,-36.54,-0.18,4.2,-12.56,4.62,0,0,0,54.53,-10.4,22.99,0.35,-54.46,0.54,29.49,-0.36,-13.12,0,0,0,-45.11,11.16,-30.21,-0.71,-73.39,-0.93,-34.32,-0.64,21.74,-12.89,-10.37,-12.1,13.23,8.96,-25.36,3.279,38.0281,-8.2024,9.44,14.93,-36,15.47,-57.25,37.14,0.17,40.55,-0.19,-1.24,-18.27,0.44,2.17,-22.57,-9.53,-0.17,42.51,0.2,-0.11,-36.26,-0.19,4.66,-10.74,4.3,0,0,0,55.18,-11.35,24.57,0.34,-53.77,0.53,28.92,-0.49,-12.81,0,0,0,-44.47,8.43,-32.5,-0.62,-70.85,-0.84,-33.65,-0.69,20.5,-13.07,-11.76,-13.03,13.62,8.76,-26.46,3.1839,38.0107,-7.4895,8.56,16,-34.31,16.54,-57.85,34.42,0.16,36.06,-0.17,-1.3,-20.11,0.4,3.1,-20.98,-9.53,-0.17,40.69,0.19,-0.44,-36.08,-0.27,5.37,-10.91,4.29,0,0,0,55.9,-10.28,24.42,0.34,-53.25,0.52,28.55,-0.54,-12.58,0,0,0,-44.03,7.42,-33.72,-0.56,-68.78,-0.77,-33.13,-0.69,19.51,-12.81,-11.53,-13.46,13.87,8.51,-27.45,3.0723,38.0215,-6.6696,8.17,17.25,-33.24,18.04,-58.71,32.01,0.15,32.6,-0.16,-1.21,-22.15,0.36,4.05,-19.24,-8.88,-0.16,37.86,0.18,-0.73,-35.97,-0.35,6.09,-12.09,5.04,0,0,0,56.31,-8.71,24.21,0.34,-52.77,0.52,28.26,-0.57,-12.38,0,0,0,-43.97,6.84,-35,-0.51,-66.42,-0.72,-32.49,-0.7,18.4,-12.76,-10.96,-13.72,13.99,8.66,-28.32,2.8782,38.0507,-5.7301,7.43,18.82,-32.23,18.28,-59.77,24.15,0.15,30.49,-0.15,-0.86,-24.91,0.3,5.48,-17.01,-8.14,-0.16,34.31,0.17,-1,-35.82,-0.43,7.29,-13.23,6.45,0,0,0,56.61,-7.85,24.94,0.33,-51.46,0.51,27.37,-0.64,-11.84,0,0,0,-43.79,5.86,-37.32,-0.45,-63.3,-0.66,-31.46,-0.73,16.96,-13.06,-10.67,-14.21,14.38,9.11,-29.61,2.7892,38.033,-4.6896,8.21,19.57,-31.79,19.4,-60.5,24.09,0.15,29.82,-0.15,-0.26,-26.9,0.3,5.37,-15.05,-6.29,-0.15,30.99,0.16,-1.33,-35.14,-0.51,6.66,-15.49,8.11,0,0,0,57.28,-6.1,24.7,0.31,-49.84,0.49,26.35,-0.65,-11.19,0,0,0,-43.12,6.21,-38.4,-0.43,-61.54,-0.63,-30.8,-0.75,16.15,-13.33,-9.39,-14.47,15.13,9.37,-31.05,2.6445,38.0394,-3.3093,8.96,20.48,-30.4,20.18,-60.19,29.06,0.15,30.41,-0.15,0.22,-28,0.33,4.4,-12.64,-6.72,-0.14,27.8,0.15,-1.33,-34.46,-0.51,6,-17.89,8.77,0,0,0,57.92,-4.22,24.83,0.3,-47.85,0.48,25.24,-0.62,-10.43,0,0,0,-42.82,6.07,-39.53,-0.41,-60.21,-0.61,-30.33,-0.75,15.56,-14.02,-8.18,-14.68,16.01,9.48,-32.35,2.5369,37.9125,-1.8651,9.61,21.49,-28.92,19.98,-59.53,33.11,0.15,31.71,-0.16,0.16,-27.76,0.32,3.6,-10.25,-6.33,-0.14,24.64,0.14,-1.24,-33.7,-0.5,5.01,-20.84,9.77,0,0,0,59.08,-2.77,24.7,0.29,-45.71,0.46,24.12,-0.56,-9.63,0,0,0,-41.97,6.57,-40.63,-0.4,-59.57,-0.6,-30.04,-0.76,15.28,-14.09,-6.59,-14.95,16.55,9.78,-34.05,2.4491,37.8452,-0.1719,10.22,22.02,-27.04,19.75,-58.23,39.25,0.15,32.96,-0.16,-0.77,-24.71,0.3,2.48,-7.13,-6.39,-0.14,21.3,0.13,-0.64,-31.75,-0.4,3.93,-22.93,10.47,0,0,0,59.47,-2.37,26.58,0.28,-43.67,0.45,23.11,-0.49,-8.89,0,0,0,-41.66,6.67,-41.55,-0.4,-59.28,-0.59,-29.89,-0.77,15.15,-14.64,-5.77,-15.33,17.51,10.78,-35.92,2.3624,37.9482,1.6278,10.57,22.61,-24.57,18.32,-57.32,43.2,0.16,34.26,-0.17,-1.14,-20.46,0.39,1.72,-3.62,-6.42,-0.13,17.48,0.12,0.99,-27.54,-0.28,2.46,-25.47,10.41,0,0,0,60.08,-2.2,29.54,0.27,-42.06,0.43,22.39,-0.45,-8.32,0,0,0,-41.21,6.27,-43.12,-0.39,-58.31,-0.58,-29.57,-0.76,14.72,-14.22,-4.57,-15.67,17.95,11.32,-37.61,2.3278,38.0972,3.4896,10.39,22.64,-21.66,13.73,-56.41,39.59,0.16,35.35,-0.17,-1.04,-17.6,0.43,0.77,-0.21,-6.64,-0.13,15.6,0.11,3.06,-22.17,-0.48,1.19,-27.99,10.52,0,0,0,60.29,-1.66,30.87,0.27,-41.58,0.43,22.22,-0.45,-8.14,0,0,0,-40.74,6.08,-44.21,-0.37,-57.17,-0.57,-29.16,-0.75,14.23,-13.49,-1.8,-15.85,18.32,10.65,-39.53,2.3872,38.31,5.3158,10.47,21.82,-18.95,7.3,-54.11,33.46,0.16,35.88,-0.17,-0.91,-17.39,0.42,-1.15,0.35,-6.84,-0.14,19.8,0.12,4.16,-17.74,-0.83,-0.5,-29.33,11.33,0,0,0,59.93,-1.46,31.47,0.27,-41.79,0.43,22.35,-0.46,-8.22,0,0,0,-40.02,6.47,-44.35,-0.37,-56.5,-0.56,-28.93,-0.74,13.94,-13.03,0.72,-16.15,19.17,10.35,-41.88,2.4305,38.5984,7.0077,9.81,20.98,-16.27,2.81,-50.82,28.77,0.16,35.44,-0.17,-0.76,-18.32,0.39,-2.48,-0.64,-7.65,-0.14,26.29,0.14,5.5,-11.83,-1.55,-0.74,-29.02,11.96,0,0,0,58.98,-0.59,32.17,0.27,-41.89,0.43,22.52,-0.48,-8.24,0,0,0,-39.4,5.2,-44.03,-0.37,-56.33,-0.56,-28.85,-0.74,13.87,-13.37,1.66,-16.33,19.94,10.53,-43.26,2.4466,38.9294,8.5783,8.17,20.22,-13.52,0.63,-47.18,25.65,0.16,34.58,-0.17,-0.64,-19.13,0.37,-3.09,-2.45,-8.56,-0.15,33.14,0.16,6.9,-4.26,-2.79,0.36,-28.1,12.62,0,0,0,57.82,0.45,33.32,0.27,-41.69,0.43,22.49,-0.49,-8.16,0,0,0,-39.09,2.53,-43.47,-0.35,-55.1,-0.54,-28.36,-0.73,13.35,-13.68,2.77,-16.26,20.29,10.35,-43.99,2.5398,39.2093,10.0645,6.95,19.17,-10.64,-1.94,-43.33,22.01,0.15,33.38,-0.16,-0.57,-19.91,0.35,-4.39,-4.8,-9.51,-0.17,39.54,0.18,7.3,3.74,-3.93,0.57,-27.47,13.38,0,0,0,57.24,0.85,33.83,0.27,-41.36,0.43,22.41,-0.49,-8.05,0,0,0,-38.44,1.22,-41.1,-0.34,-53.77,-0.53,-27.98,-0.7,12.79,-13.16,4.6,-16.2,20.3,10.21,-44.9,2.659,39.3727,11.3605,5.88,18.04,-7.72,-4.19,-39.8,18.24,0.15,32.49,-0.16,-0.58,-20.94,0.34,-5.89,-7.9,-10.12,-0.18,45.29,0.21,5.34,8.17,-3.28,0.87,-26.51,14.05,0,0,0,56.48,0.83,34.69,0.27,-41.22,0.43,22.43,-0.5,-7.99,0,0,0,-37.52,-0.38,-39.79,-0.34,-52.68,-0.52,-27.5,-0.69,12.34,-12.74,6.2,-16.04,20.03,10.17,-45.34,2.8,39.4226,12.4365,5.08,17.05,-4.98,-5.63,-37.15,16.1,0.15,32.3,-0.16,-0.58,-21.49,0.34,-7.75,-11.71,-11.27,-0.2,50.98,0.24,3.58,8.69,-2.25,1.38,-24.67,14.64,0,0,0,55.23,0.67,35.88,0.27,-41.11,0.43,22.37,-0.5,-7.95,0,0,0,-37.12,-2.7,-37.57,-0.32,-51.14,-0.5,-26.79,-0.68,11.72,-12.88,6.84,-15.65,19.98,10.17,-45,2.9641,39.3767,13.2908,4.49,16.09,-2.42,-7.14,-35.05,13.28,0.15,32.76,-0.16,-0.61,-22.47,0.33,-10.06,-16.05,-13.05,-0.24,56.95,0.28,3.78,6.27,-2.2,1.61,-22.46,15.22,0,0,0,54.45,0.67,35.8,0.27,-40.79,0.43,22.23,-0.49,-7.84,0,0,0,-37.08,-4.93,-34.53,-0.31,-49.79,-0.49,-26.26,-0.65,11.18,-12.84,7.06,-15,19.53,10.37,-43.71,3.1181,39.2686,14.0183,4.13,14.76,-0.18,-8.5,-32.91,10.1,0.15,33.55,-0.16,-0.65,-23.3,0.32,-12.64,-20.36,-14.54,-0.28,62.34,0.32,4.6,0.91,-2.21,1.05,-19.47,16.06,0,0,0,54.7,0.38,34.7,0.27,-40.34,0.42,22.07,-0.49,-7.68,0,0,0,-36.56,-7.11,-31.26,-0.31,-48.54,-0.48,-25.62,-0.63,10.69,-12.34,6.85,-14.3,18.91,10.72,-41.9,3.2473,39.1772,14.683,3.85,13.14,1.6,-9.54,-30.53,7.43,0.16,34.44,-0.17,-0.68,-24.53,0.3,-14.69,-24.88,-14.69,-0.32,66.14,0.37,5.13,-4.52,-1.95,1.16,-16.34,16.9,0,0,0,54.33,1.25,33.17,0.27,-40.59,0.43,22.18,-0.49,-7.77,0,0,0,-37.02,-8.89,-25.6,-0.3,-47.03,-0.47,-24.87,-0.6,10.12,-12.3,6.8,-12.98,18.31,11.94,-39.33,3.3836,39.0366,15.2776,4.06,11.72,3.45,-10.73,-28.53,5.34,0.16,35.49,-0.17,-0.7,-25.65,0.28,-16.93,-29.44,-14.6,-0.34,68.19,0.4,5.07,-9.02,-1.5,0.63,-13.09,17.43,0,0,0,54.09,1.28,33.12,0.27,-40.6,0.43,22.13,-0.48,-7.78,0,0,0,-37.95,-10.52,-18.19,-0.3,-46.73,-0.47,-24.75,-0.6,10,-11.73,6.37,-11.74,17.48,13.72,-36.56,3.4224,38.8236,15.768,3.82,11.25,5.6,-11.39,-27.99,3.47,0.16,37.05,-0.18,-0.71,-26.81,0.26,-18.69,-34.4,-14.75,-0.35,68.53,0.4,4.51,-11.79,-1.11,0.3,-10.88,17.15,0,0,0,54.23,1.67,33.84,0.27,-40.76,0.43,22.18,-0.48,-7.83,0,0,0,-39,-12.32,-11.01,-0.3,-47.52,-0.47,-24.98,-0.6,10.31,-11.35,5.87,-10.18,17.4,16.12,-33.82,3.4248,38.5661,16.2219,3.35,11.22,7.24,-11.53,-28.04,2.75,0.16,38.81,-0.18,-0.73,-28.3,0.24,-19.99,-39.45,-14.07,-0.32,66.44,0.37,3.35,-13.7,-0.72,0.1,-8.85,17.43,0,0,0,54.45,2.07,34.78,0.27,-40.92,0.43,22.32,-0.5,-7.88,0,0,0,-40.47,-13.77,-4.56,-0.31,-49.33,-0.49,-25.52,-0.63,11.02,-11.02,4.93,-8.62,17.44,18.26,-30.93,3.438,38.3701,16.6982,3.18,11.44,8.57,-11.8,-28.16,1.91,0.17,40.13,-0.19,-0.78,-29.4,0.22,-20.78,-43.96,-12.63,-0.27,61.61,0.32,2.47,-14.41,-0.54,0.47,-7.67,17.92,0,0,0,53.87,3.49,35.28,0.27,-41.53,0.43,22.79,-0.52,-8.09,0,0,0,-43.19,-14.35,2.11,-0.33,-51.39,-0.51,-26.1,-0.65,11.86,-11,4.5,-7.24,16.79,20.07,-28.17,3.5157,38.2403,17.1326,3.5,12.43,9.53,-12.71,-28.5,0.93,0.17,40.55,-0.19,-0.85,-30.24,0.2,-21.96,-48.53,-11.45,-0.22,54.9,0.26,2.35,-12.76,-0.62,0.06,-7.09,18.38,0,0,0,53.24,5.05,36.31,0.27,-42.24,0.44,23.4,-0.54,-8.32,0,0,0,-45.94,-15.05,7.96,-0.34,-53.92,-0.53,-26.76,-0.68,12.91,-10.73,3.62,-6.4,15.85,21.27,-25.78,3.5558,38.2248,17.5883,3.37,13.62,10.06,-12.89,-28.8,0.63,0.17,40.39,-0.19,-0.95,-30.91,0.17,-21.66,-52.46,-9.21,-0.19,46.99,0.22,2.95,-9.71,-0.96,-0.72,-5.96,19.16,0,0,0,53.13,5.81,37.98,0.28,-42.61,0.44,24.02,-0.51,-8.44,0,0,0,-48.17,-16.43,11.11,-0.38,-57.38,-0.57,-27.82,-0.76,14.38,-10.34,1.53,-6.03,15.18,21.69,-23.79,3.5636,38.214,18.016,3.08,15.36,10.64,-13.05,-29.6,0.31,0.17,40.11,-0.19,-1.01,-31.43,0.15,-21.4,-56.27,-7.27,-0.17,39.35,0.18,4.37,-6.65,-1.64,-0.93,-6.93,19.92,0,0,0,52.81,8.26,36.99,0.28,-43.5,0.44,24.81,-0.45,-8.76,0,0,0,-50.13,-16.48,13.89,-0.43,-61.69,-0.63,-29.06,-0.88,16.26,-10.29,0.48,-5.7,14.74,21.82,-22.51,3.592,38.1795,18.4557,2.32,17,11.41,-12.9,-30.45,-0.32,0.17,40,-0.19,-1.07,-32.12,0.13,-20.6,-59.72,-4.71,-0.15,33.12,0.16,6.16,-6.14,-2.33,-1.15,-6.99,21.3,0,0,0,52.52,8.72,37.72,0.28,-43.39,0.44,24.94,-0.41,-8.72,0,0,0,-51.9,-16.38,13.39,-0.48,-65.19,-0.69,-30.03,-0.98,17.84,-10.93,-1.4,-5.98,15.11,21.31,-22.54,3.5993,38.1311,18.9528,1.58,18.5,11.81,-12.63,-31.28,-0.93,0.17,40.08,-0.19,-1.07,-32.7,0.12,-16.36,-62.79,5.51,-0.15,28.78,0.15,8.09,-8.93,-2.61,-0.52,-7.57,21.51,0,0,0,51.6,11.57,37.16,0.28,-43.53,0.44,25.29,-0.33,-8.78,0,0,0,-54.22,-16.92,14.52,-0.55,-68.47,-0.77,-31.14,-1.1,19.33,-11.89,-2.53,-5.87,14.98,20.68,-21.82,3.6176,38.0196,19.5398,1.41,20.09,11.95,-12.85,-31.95,-1.51,0.17,40.17,-0.19,-1.08,-33.54,0.1,-16.71,-65.98,4.78,-0.14,26.31,0.14,6.95,-13.38,-1.72,-1.02,-8.98,22.14,0,0,0,51.65,13.46,37.04,0.28,-43.27,0.44,25.4,-0.25,-8.7,0,0,0,-55.87,-16.72,15.72,-0.62,-70.94,-0.84,-32.11,-1.14,20.47,-11.86,-3.07,-6.01,14.59,19.95,-21.39,3.6149,37.9031,20.2047,0.67,21.32,12.46,-12.44,-32.24,-2.02,0.17,40.21,-0.19,-1.05,-34.48,0.09,-15.31,-68.06,4.93,-0.14,25.31,0.14,5.27,-18.12,-0.91,-0.71,-9.8,22.48,0,0,0,50.94,14.14,38.62,0.28,-42.73,0.44,25.25,-0.22,-8.51,0,0,0,-57.53,-16.92,15.99,-0.67,-72.47,-0.89,-32.79,-1.13,21.19,-12.14,-3.89,-6.31,14.08,19.36,-21.17,3.6715,37.8701,20.9511,0.24,22.41,13.16,-12.57,-31.84,-2.95,0.17,39.66,-0.18,-0.99,-35.01,0.09,-14.26,-69.08,4.88,-0.14,25.42,0.14,5.02,-18.83,-0.82,-1.02,-9.94,22.75,0,0,0,50.22,13.81,40.1,0.27,-42.34,0.44,25.2,-0.18,-8.37,0,0,0,-59.09,-17.22,15.39,-0.72,-73.66,-0.94,-33.37,-1.07,21.78,-12.55,-5.12,-6.81,14.26,18.43,-21.41,3.719,37.8706,21.8221,-0.24,23.29,14.04,-12.47,-30.94,-3.63,0.16,38.74,-0.18,-0.95,-35.33,0.09,-13.22,-69.31,4.74,-0.14,25.86,0.14,5.08,-18.43,-0.86,-1.1,-10.54,22.79,0,0,0,49.56,13.85,40.84,0.27,-42.08,0.43,25.16,-0.15,-8.28,0,0,0,-59.87,-16.95,14.88,-0.77,-74.75,-1,-33.83,-1.01,22.31,-12.49,-5.64,-7.26,14.07,17.5,-21.61,3.7728,37.8436,22.8402,-0.99,24.11,15.55,-12.08,-29.85,-4.1,0.16,37.72,-0.18,-1.06,-35.41,0.07,-12.94,-69,3.48,-0.14,26.19,0.14,4.18,-19.9,-0.64,-0.59,-11.82,22.29,0,0,0,48.91,14.19,41.41,0.27,-41.94,0.43,25.13,-0.13,-8.23,0,0,0,-60.39,-16.52,14.88,-0.81,-75.48,-1.04,-34.16,-0.94,22.68,-12.56,-5.41,-7.52,13.86,17.03,-21.95,3.8347,37.8483,23.9696,-2.03,24.84,17.37,-11.4,-28.51,-4.72,0.16,36.67,-0.17,-1.18,-35.72,0.04,-12.97,-68.08,1.66,-0.14,26.2,0.14,3.27,-21.32,-0.48,-0.21,-14.06,22.54,0,0,0,49.51,14.13,40.46,0.27,-41.85,0.43,25.1,-0.13,-8.2,0,0,0,-59.9,-14.57,14.72,-0.85,-76.2,-1.08,-34.44,-0.89,23.05,-12.51,-4.1,-7.71,14.22,15.6,-22.68,3.9437,37.7229,25.1989,-2.4,25.84,18.99,-11.42,-27.03,-5.8,0.16,35.57,-0.17,-1.26,-35.84,0.02,-13.86,-67.03,-0.36,-0.14,26.07,0.14,2.02,-24.01,-0.31,-1.51,-16.01,22.84,0,0,0,50.9,12.9,40.13,0.27,-41.6,0.43,25.03,-0.11,-8.12,0,0,0,-58.71,-13.01,13.43,-0.9,-76.93,-1.13,-34.73,-0.82,23.42,-11.73,-4.28,-8.6,14.58,15.43,-24.34,4.0461,37.656,26.5171,-2.79,26.8,20.52,-10.99,-25.48,-5.92,0.16,34.23,-0.17,-1.44,-35.7,-0.02,-14.8,-65.89,-2.36,-0.14,26,0.14,1.15,-26.14,-0.26,-3.87,-16.74,23.14,0,0,0,52.61,9.82,41.74,0.27,-41.08,0.43,24.83,-0.1,-7.93,0,0,0,-57.46,-12.14,10.7,-0.91,-77.04,-1.13,-34.86,-0.76,23.49,-11.06,-5.95,-9.82,15.2,14.98,-25.96,4.1307,37.6234,27.9755,-4.03,27.58,22.59,-9.46,-23.73,-5.16,0.15,32.28,-0.16,-1.77,-35,-0.06,-15.18,-64.84,-4.59,-0.14,26.59,0.14,0.6,-27.64,-0.26,-4.58,-17.87,22.87,0,0,0,53.61,7.69,42.97,0.27,-40.78,0.43,24.68,-0.11,-7.82,0,0,0,-57.02,-11.59,8.86,-0.89,-76.75,-1.11,-34.93,-0.69,23.37,-11.27,-7.3,-10.65,15.82,15.12,-27.15,4.1955,37.7839,29.6154,-6.08,27.74,25.06,-7.16,-21.23,-5.24,0.15,29.64,-0.15,-1.69,-33.45,0.01,-14.29,-64.06,-6.5,-0.15,28.01,0.15,0.99,-26.13,-0.25,-2.22,-20.77,22.17,0,0,0,53.3,8.7,41.95,0.27,-41.12,0.43,24.77,-0.14,-7.94,0,0,0,-57.76,-10.19,10.37,-0.87,-76.5,-1.1,-35,-0.61,23.27,-11.89,-6.39,-10.43,15.46,15.29,-27.09,4.2862,38.0082,31.2927,-7.85,27.87,27.31,-5.17,-18.44,-5.31,0.14,26.56,-0.14,-1.3,-30.96,0.14,-13.51,-63.75,-8.28,-0.15,30.15,0.15,2.03,-21.75,-0.36,-0.19,-24.58,21.75,0,0,0,53.27,10.15,39.94,0.27,-41.92,0.43,25.04,-0.17,-8.22,0,0,0,-57.76,-8.22,12.65,-0.85,-76.2,-1.08,-34.93,-0.62,23.12,-11.95,-5.52,-10.22,14.77,16.56,-27.11,4.4044,38.2594,33.0175,-9.13,27.49,29.57,-3.65,-15.29,-5.14,0.14,24.05,-0.14,-0.9,-27.36,0.26,-13.4,-62.68,-10.54,-0.15,32.28,0.16,2.95,-17.5,-0.62,0.47,-26.69,21.24,0,0,0,53.53,9.62,39.29,0.27,-42.34,0.44,25.07,-0.23,-8.36,0,0,0,-56.86,-6.54,13.27,-0.83,-75.85,-1.06,-34.82,-0.65,22.94,-12.06,-5.74,-10.38,14.86,17.77,-27.67,4.5273,38.5699,34.773,-10.83,26.12,32.16,-1.72,-12.49,-4.41,0.14,23.26,-0.13,-0.95,-23.07,0.34,-11.99,-60.32,-12.51,-0.15,33.61,0.16,3.25,-15.69,-0.76,2.18,-28.02,20.51,0,0,0,53.26,9.28,38.13,0.28,-42.54,0.44,24.93,-0.31,-8.43,0,0,0,-56.46,-4.91,14.38,-0.81,-75.57,-1.04,-34.73,-0.67,22.79,-12.21,-5.85,-10.37,14.63,19.02,-27.84,4.6217,38.9345,36.4757,-12.39,24.57,34.95,-0.09,-10.86,-2.95,0.14,24.49,-0.14,-1.72,-18.12,0.51,-10.71,-57.14,-15.16,-0.15,34.07,0.17,2.98,-16.37,-0.67,3.3,-29.1,19.8,0,0,0,53.24,8.5,35.94,0.28,-42.59,0.44,24.68,-0.39,-8.44,0,0,0,-56.11,-3.07,15.54,-0.79,-75.18,-1.02,-34.57,-0.72,22.59,-11.67,-5.64,-10.48,14.26,19.93,-28.1,4.7369,39.3124,38.0858,-13.34,22.98,38.08,0.68,-9.96,-1.44,0.14,26.53,-0.14,-3.3,-13.09,1,-9.49,-53.48,-16.34,-0.15,34.05,0.17,2.71,-18.04,-0.55,4.07,-29.74,18.52,0,0,0,52.74,7.04,35.31,0.27,-41.74,0.43,23.86,-0.48,-8.13,0,0,0,-56.51,-0.69,17.03,-0.82,-75.65,-1.05,-34.45,-0.83,22.79,-11.3,-5.28,-10.63,13.97,20.47,-28.44,4.9208,39.6504,39.5876,-13.58,21.92,41.67,0.14,-9.57,0.1,0.15,28.04,-0.15,-5.65,-8.27,2,-9.44,-50.16,-17.15,-0.15,34.17,0.17,2.49,-19.76,-0.44,3.54,-29.06,16.34,0,0,0,52.36,4.44,35.42,0.27,-39.97,0.42,22.54,-0.51,-7.52,0,0,0,-57.37,0.44,17.16,-0.82,-75.66,-1.05,-34.13,-0.97,22.76,-11.45,-5.55,-10.95,14.18,20.34,-29.01,5.0441,39.8583,40.9975,-14.2,20.53,45.07,0.22,-9.68,2.6,0.15,29.35,-0.15,-6.78,-6.19,2.6,-7.26,-47.35,-14.85,-0.16,34.28,0.17,2.17,-21.66,-0.33,3.05,-29.47,14.25,0,0,0,53.4,2.88,33.7,0.26,-38.65,0.41,21.57,-0.48,-7.1,0,0,0,-57.32,1.07,17.86,-0.73,-73.86,-0.95,-33.36,-1.09,21.87,-10.62,-4.15,-10.99,13.92,20.08,-29.35,5.1273,39.9544,42.2346,-14.8,18.8,47.75,0.29,-9.99,4.88,0.15,30.8,-0.15,-6.07,-7.12,2.25,-5.47,-44.78,-15.05,-0.16,34.58,0.17,1.74,-22.93,-0.27,2.91,-29.82,12.57,0,0,0,54.67,1.55,31.86,0.26,-38.17,0.41,21.16,-0.46,-6.95,0,0,0,-57.71,1.71,19.36,-0.67,-72.38,-0.89,-32.46,-1.17,21.15,-9.5,-2.21,-10.83,14.01,19.89,-29.68,5.2267,40.0289,43.2729,-14.98,17.14,49.86,-0.37,-10.32,7.06,0.15,32.14,-0.16,-4.96,-8.96,1.72,-4.73,-42.59,-16.95,-0.16,35.4,0.17,1.47,-23.44,-0.24,3.42,-29.5,11.4,0,0,0,54.69,0.12,30.61,0.26,-38.21,0.41,21.08,-0.45,-6.97,0,0,0,-58.56,1.45,19.92,-0.6,-70.26,-0.82,-31.34,-1.15,20.17,-9.28,-0.19,-10.38,14.38,19.61,-29.79,5.2934,40.0853,44.1809,-14.73,15.57,51.58,-1.51,-10.56,8.93,0.15,33.17,-0.16,-3.77,-10.57,1.27,-4.41,-40.72,-19.18,-0.16,36.68,0.17,1.35,-23.53,-0.23,3.45,-28.37,10.48,0,0,0,54.66,-1.93,30.02,0.26,-38.43,0.41,21.19,-0.45,-7.04,0,0,0,-58.99,1.15,18.9,-0.55,-68.45,-0.77,-30.42,-1.04,19.36,-8.55,1.4,-10.03,14.4,19.25,-29.58,5.3278,40.152,44.9569,-14.18,14.09,53.68,-3.1,-10.81,9.82,0.15,33.85,-0.16,-2.44,-12.06,0.86,-4.61,-39.03,-21.23,-0.16,38.26,0.18,1.3,-23.52,-0.21,3.24,-26.73,9.21,0,0,0,54.62,-3.67,28.82,0.26,-38.97,0.42,21.47,-0.47,-7.22,0,0,0,-59.5,1.21,17.3,-0.53,-67.48,-0.74,-29.72,-0.91,18.97,-7.97,2.94,-9.68,14.31,18.77,-29.27,5.2803,40.1651,45.632,-13.44,12.3,56.32,-4.6,-11.08,10.49,0.16,34.52,-0.17,-1.25,-13.55,0.55,-4.37,-37.47,-22.16,-0.17,40.16,0.19,1.1,-23.98,-0.19,3.18,-24.7,7.37,0,0,0,54.8,-4.83,26.46,0.26,-39.55,0.42,21.79,-0.48,-7.41,0,0,0,-59.96,1.83,16.09,-0.53,-67.44,-0.74,-29.18,-0.73,19.02,-7.46,4.47,-9.24,14.06,18.41,-28.72,5.1275,40.0739,46.2454,-12.92,10.24,58.83,-5.34,-11.85,11.66,0.16,35.11,-0.17,-0.27,-15.08,0.35,-3.84,-36.42,-23.22,-0.17,42.47,0.2,1.18,-23.65,-0.18,3.36,-22.79,5.72,0,0,0,55.48,-6.02,23.92,0.27,-39.98,0.42,22.06,-0.49,-7.55,0,0,0,-60.23,2.13,14.87,-0.53,-67.33,-0.74,-28.89,-0.61,19.01,-6.75,6.09,-8.83,14.05,17.89,-28.3,4.9142,40.0413,46.6999,-12.21,8.59,61.34,-6.07,-13.23,12.73,0.16,35.79,-0.17,0.38,-16.49,0.25,-4.22,-35.99,-24.89,-0.18,45.1,0.21,1.62,-22.44,-0.21,3.5,-20.92,4.02,0,0,0,55.92,-7.05,21.83,0.27,-40.42,0.42,22.29,-0.5,-7.7,0,0,0,-60.84,2.32,14.24,-0.54,-68.1,-0.76,-28.88,-0.55,19.4,-6.28,7.68,-8.41,14.2,16.96,-27.98,4.5876,40.0755,47.0648,-11.44,7.15,63.47,-6.51,-14.76,13.37,0.16,37.32,-0.18,0.39,-16.45,0.24,-4.69,-36.05,-26.29,-0.19,47.93,0.22,2.39,-20.27,-0.31,3.82,-17.59,2.73,0,0,0,56.38,-8.41,20.91,0.27,-41.55,0.43,22.84,-0.52,-8.09,0,0,0,-61.48,2.19,12.16,-0.6,-70.3,-0.82,-29.22,-0.57,20.45,-6.32,6.93,-8.31,14.5,16.39,-27.72,4.1273,40.2354,47.3057,-10.6,5.82,65.26,-6.55,-16,12.49,0.17,39.42,-0.18,0.32,-13.53,0.23,-5.45,-37.28,-26.55,-0.21,51.72,0.24,3.96,-15.78,-0.75,4.41,-14.33,2.01,0,0,0,56.93,-9.59,19.97,0.28,-42.56,0.44,23.37,-0.54,-8.44,0,0,0,-62.39,2.6,10.56,-0.73,-73.75,-0.95,-29.82,-0.69,22.09,-6.81,5.86,-8.19,15.03,16.1,-27.58,3.5789,40.1757,47.4787,-10.16,4.83,66.29,-6.48,-16.36,10.55,0.17,40.44,-0.19,0.06,-14.22,0.29,-7.03,-40.45,-26.58,-0.24,57.02,0.28,5.68,-9.8,-1.64,5.15,-11.93,1.67,0,0,0,57.67,-9.72,19.44,0.28,-43.49,0.44,23.88,-0.56,-8.77,0,0,0,-63.57,2.12,8.7,-0.87,-76.56,-1.1,-30.45,-0.9,23.39,-7.45,4.8,-7.75,15.44,16.01,-26.8,3.0221,39.8305,47.6265,-10.26,4.95,66.4,-6.89,-16.16,9.72,0.17,40.01,-0.19,-0.4,-18.58,0.34,-10.02,-45.35,-26.74,-0.28,62.32,0.32,6.36,-3.5,-2.54,4.94,-10.31,2.05,0,0,0,58.82,-9.24,19.83,0.29,-44.77,0.45,24.57,-0.57,-9.24,0,0,0,-64.45,0.76,6.24,-1.07,-79.09,-1.31,-31.07,-1.13,24.56,-7.73,2.98,-7.41,15.63,16.32,-25.68,2.5153,39.4198,47.8171,-11.05,5.57,66.43,-7.27,-16.72,9.08,0.17,39.31,-0.18,-0.63,-22.41,0.32,-13.2,-50.15,-26.73,-0.3,64.29,0.34,3.77,-1.63,-1.65,3.82,-9.88,2.95,0,0,0,60.43,-8.96,21.12,0.29,-46,0.46,25.25,-0.57,-9.7,0,0,0,-64.19,-0.41,3.2,-1.24,-80.57,-1.47,-31.66,-1.33,25.22,-7.13,1.46,-7.29,15.67,16.46,-24.79,2.0973,38.9568,48.0215,-12.14,6.28,66.38,-7.98,-16.92,8.39,0.16,38.31,-0.18,-0.66,-27.69,0.25,-15.55,-54.29,-26.12,-0.27,61.98,0.32,0.9,-3.15,-0.43,3.23,-10.2,4.35,0,0,0,61.16,-8.51,22.2,0.3,-47.18,0.47,25.93,-0.56,-10.14,0,0,0,-63.93,-0.75,0.16,-1.43,-81.82,-1.66,-32.3,-1.49,25.77,-7.46,-0.09,-7.07,16.34,17.36,-24.41,1.7998,38.6983,48.2684,-13.24,6.63,66.01,-8.33,-17.13,7.11,0.16,36.87,-0.17,-0.36,-30.48,0.26,-15.76,-56.9,-24.24,-0.23,56.31,0.27,0.5,-4.73,-0.28,3.69,-10.28,5.99,0,0,0,60.75,-7.83,24.2,0.3,-48.15,0.48,26.5,-0.53,-10.52,0,0,0,-64.21,-1.45,-2.89,-1.45,-81.95,-1.69,-32.97,-1.55,25.78,-7.93,-1.68,-7,15.66,17.9,-23.38,1.6086,38.6394,48.5393,-14.23,7.5,65.48,-8.67,-17.23,6.77,0.16,34.83,-0.17,-0.18,-31.87,0.28,-15.08,-58.63,-20.22,-0.19,48.78,0.22,1.37,-4.44,-0.64,3.07,-10.46,7.65,0,0,0,60.8,-7.21,26.61,0.31,-48.8,0.48,26.98,-0.49,-10.78,0,0,0,-63.37,-2.5,-6.02,-1.33,-81.19,-1.56,-33.58,-1.48,25.39,-7.95,-3.03,-7.07,15.21,17.87,-22.69,1.4792,38.6235,48.8761,-15.75,8.21,65.14,-8.14,-17.62,7.25,0.15,32.65,-0.16,-0.14,-32.97,0.28,-13.5,-59.99,-14.52,-0.17,40.73,0.19,2.5,-3.6,-1.14,2.34,-11.62,8.97,0,0,0,61.4,-6.33,29.06,0.31,-48.81,0.48,27.24,-0.41,-10.79,0,0,0,-61.54,-4.09,-8.88,-1.13,-79.61,-1.36,-34.02,-1.31,24.63,-7.1,-4.25,-7.02,14.56,18.45,-21.77,1.4713,38.6182,49.1977,-17.4,8.9,65.19,-7.76,-18.04,7.4,0.15,30.58,-0.15,-0.19,-33.4,0.27,-12.15,-61.2,-7.63,-0.15,34.13,0.17,3.8,-3.85,-1.67,2.14,-13.32,10.06,0,0,0,61.47,-5.37,31.38,0.31,-48.39,0.48,27.3,-0.33,-10.64,0,0,0,-60.34,-5.26,-11.44,-0.98,-78.08,-1.21,-34.42,-1.07,23.93,-6.99,-5.08,-6.56,14.65,19.51,-20.85,1.619,38.5672,49.4851,-18.02,10.34,65.04,-8.64,-17.65,7.29,0.15,28.42,-0.15,-0.23,-33.85,0.27,-10.92,-62.11,2.49,-0.15,30.28,0.15,5.24,-6.65,-1.98,1.4,-14.46,11.35,0,0,0,60.97,-4.89,34.12,0.3,-47.32,0.47,27.03,-0.27,-10.23,0,0,0,-59.89,-5.97,-13.74,-0.87,-76.56,-1.1,-34.7,-0.79,23.25,-7.49,-6.1,-6.14,14.05,21.02,-19.75,1.8004,38.4258,49.863,-18.6,11.41,64.38,-8.86,-17.29,7.77,0.14,26.79,-0.14,-0.22,-34.53,0.27,-8.76,-62.66,11.71,-0.15,28.27,0.15,5.26,-11.73,-1.51,1.03,-15.35,13.04,0,0,0,60.56,-4.06,36.28,0.3,-46.53,0.47,26.87,-0.21,-9.93,0,0,0,-59.76,-6.68,-15.77,-0.79,-75.03,-1.01,-34.84,-0.54,22.57,-7.98,-7.08,-5.72,13.66,21.87,-18.67,2.0684,38.3156,50.3002,-19.28,12.23,63.97,-8.72,-16.98,8.43,0.14,25.56,-0.14,-0.31,-34.94,0.25,-9.05,-63.02,13.59,-0.14,27.29,0.14,4.04,-16.35,-0.88,0.57,-16.16,14.46,0,0,0,60.48,-3.86,39.26,0.29,-45.39,0.46,26.46,-0.18,-9.5,0,0,0,-59.26,-7.8,-18.76,-0.67,-72.33,-0.89,-34.63,-0.31,21.31,-7.75,-8.52,-5.36,12.82,23.01,-17.28,2.425,38.261,50.78,-20.05,13.05,63.98,-8.67,-16.68,8.5,0.14,24.44,-0.14,-0.4,-34.88,0.23,-9.51,-63.23,15.05,-0.14,27.05,0.14,3.26,-19.11,-0.6,0.6,-18.02,15.39,0,0,0,59.85,-2.51,40.44,0.29,-44.99,0.45,26.37,-0.15,-9.35,0,0,0,-58.76,-8.17,-20.83,-0.59,-69.7,-0.8,-34.35,-0.09,20.11,-7.37,-8.19,-4.72,11.62,23.15,-15.62,2.8712,38.1955,51.3315,-21.24,13.49,64.68,-8.15,-16.56,8.31,0.14,23.7,-0.13,-0.51,-34.8,0.21,-9.97,-63.13,15.7,-0.14,26.96,0.14,2.45,-21.58,-0.4,1.11,-20.51,15.7,0,0,0,59.33,-0.86,40.74,0.29,-44.67,0.45,26.34,-0.1,-9.24,0,0,0,-58.25,-7.8,-21.96,-0.54,-67.74,-0.75,-34.13,0.1,19.23,-7.16,-7.65,-4.07,10.83,23.65,-14.28,3.4017,38.0932,52.012,-22.55,13.54,65.54,-7.12,-16.39,8.09,0.14,23.28,-0.13,-0.6,-34.6,0.19,-9.56,-62.54,16.68,-0.14,26.66,0.14,1.46,-24.56,-0.27,1.12,-21.9,16.43,0,0,0,59.47,-1.54,42.19,0.28,-43.94,0.45,26.03,-0.11,-8.97,0,0,0,-57.66,-7.37,-24.33,-0.49,-65.72,-0.7,-33.82,0.26,18.32,-6.88,-8.04,-3.83,10.7,24.28,-13.76,4.0453,37.9331,52.8088,-23.77,13.52,66.36,-6.03,-15.9,8.1,0.14,22.87,-0.13,-0.68,-34.61,0.18,-8.94,-61.51,17.9,-0.14,26.26,0.14,0.84,-27.18,-0.24,2.01,-23.91,16.84,0,0,0,58.81,-1.12,42.65,0.28,-43.73,0.45,25.87,-0.14,-8.88,0,0,0,-57.64,-6.59,-24.96,-0.46,-63.9,-0.67,-33.5,0.4,17.51,-6.87,-7.82,-3.27,10.35,25.07,-12.78,4.8526,37.789,53.6876,-24.58,13.47,67.36,-5.3,-14.34,7.07,0.14,21.51,-0.13,-0.64,-33.92,0.2,-7.71,-60.48,19.59,-0.14,26.76,0.14,0.74,-29,-0.21,1.78,-25.9,17.35,0,0,0,59.21,-1.48,41.97,0.28,-43.44,0.44,25.68,-0.17,-8.77,0,0,0,-56.88,-5.11,-25.69,-0.44,-62.59,-0.64,-33.26,0.5,16.94,-6.39,-7.17,-2.96,10.14,25.59,-12.3,5.8306,37.8369,54.6163,-25.29,13.18,68.39,-4.56,-12.09,5.29,0.14,19.32,-0.12,-0.58,-32.26,0.23,-5.54,-59.85,21.85,-0.15,28.01,0.15,1.29,-26.22,-0.22,2.11,-28.19,17.63,0,0,0,59.12,-1.45,40.8,0.28,-43.5,0.44,25.59,-0.22,-8.79,0,0,0,-56.16,-4.05,-26.08,-0.43,-61.58,-0.63,-32.98,0.49,16.47,-6.21,-6.17,-2.6,9.84,26.44,-11.87,6.8577,37.9418,55.5889,-25.64,12.31,68.66,-3.35,-9.45,3.25,0.13,17.32,-0.12,-0.73,-29.37,0.25,-1.75,-58.95,25.37,-0.15,29.34,0.15,1.72,-22.54,-0.31,2.54,-28.93,19,0,0,0,58.93,-3.14,40.45,0.28,-43.8,0.45,25.49,-0.3,-8.89,0,0,0,-55.11,-3.34,-27.03,-0.42,-60.86,-0.62,-32.72,0.43,16.13,-5.88,-6.09,-2.46,9.92,27.21,-11.75,7.9273,38.0802,56.5295,-25,11.28,68.6,-2.36,-6.83,2.17,0.13,17.26,-0.12,-1.08,-26.53,0.28,-1.13,-57.55,21.36,-0.15,30.67,0.15,1.68,-20.28,-0.37,3.25,-29.18,19.96,0,0,0,57.76,-3.67,39.16,0.28,-44.29,0.45,25.39,-0.4,-9.06,0,0,0,-53.61,-3.04,-26.56,-0.41,-60.64,-0.61,-32.54,0.32,16,-5.09,-4.88,-2.13,8.88,27.52,-10.69,9.0229,38.2984,57.442,-23.76,10.05,68.95,-1.39,-5.25,1.34,0.14,20.04,-0.13,-1.57,-23.15,0.35,-2.27,-55.05,14.66,-0.15,31.94,0.16,1.33,-20.49,-0.33,3.52,-29.11,19.88,0,0,0,56.56,-3.37,37.52,0.29,-44.57,0.45,25.29,-0.45,-9.16,0,0,0,-51.87,-2.85,-25.13,-0.41,-60.29,-0.61,-32.22,0.14,15.79,-4.25,-3.25,-1.81,8,27.93,-9.75,10.1302,38.6322,58.2892,-22.23,8.95,70.01,-0.69,-5.21,1.4,0.14,25.22,-0.14,-2.49,-17.89,0.61,-3.41,-51.4,10.19,-0.15,32.47,0.16,1.24,-21.93,-0.29,4.1,-27.84,19.66,0,0,0,54.33,-3.4,35.78,0.28,-44.36,0.45,24.92,-0.51,-9.08,0,0,0,-51.59,-2.75,-23.36,-0.4,-59.56,-0.6,-31.64,-0.11,15.4,-4.44,-1.91,-1.44,7.38,28,-9.03,11.2178,39.0292,59.0344,-20.79,7.94,71.62,-0.2,-6.65,1.57,0.15,32.17,-0.16,-3.75,-12.14,1.16,-4.45,-47.26,6.55,-0.15,32.17,0.16,1.21,-22.8,-0.27,4.16,-26.44,18.92,0,0,0,53.07,-3.74,33.88,0.28,-43.23,0.44,24.16,-0.53,-8.67,0,0,0,-51.39,-2.73,-21.51,-0.39,-58.28,-0.58,-30.86,-0.33,14.78,-4.33,-0.63,-1.37,6.7,27.58,-8.63,12.2341,39.3602,59.7526,-20.02,6.34,73.37,1.23,-9.79,2.38,0.17,40.05,-0.19,-5.84,-5.14,2.38,-3.85,-43.4,4.75,-0.15,31.47,0.16,1.19,-23.19,-0.26,5.38,-24.7,18,0,0,0,51.85,-4.51,33.09,0.27,-41.79,0.43,23.29,-0.53,-8.16,0,0,0,-52.15,-3.81,-20.34,-0.36,-56.07,-0.55,-29.79,-0.47,13.79,-4.87,0.1,-1.18,6.27,26.84,-8.22,13.1666,39.5168,60.3715,-19.18,4.92,75.22,2.43,-13.58,3.14,0.19,47.56,-0.22,-8.03,1.41,4.09,-2.84,-39.92,4.65,-0.15,31.13,0.16,1.2,-23.65,-0.26,5.44,-23.42,16.78,0,0,0,52.13,-5.34,31.89,0.27,-40.72,0.43,22.64,-0.52,-7.79,0,0,0,-51.91,-4.81,-19.66,-0.34,-53.82,-0.53,-28.66,-0.57,12.82,-4.38,0.95,-1.18,5.92,26.34,-7.91,13.9865,39.5462,60.8782,-18.19,3.11,77.26,3.85,-17.78,3.15,0.22,54.11,-0.26,-7.15,3.57,3.93,-1.88,-36.76,3.44,-0.15,31.25,0.16,1.2,-24.3,-0.24,6.02,-21.72,16.07,0,0,0,52.23,-6.42,30.07,0.27,-40.45,0.42,22.43,-0.51,-7.7,0,0,0,-51.86,-5.49,-19.81,-0.33,-51.53,-0.51,-27.47,-0.63,11.87,-4.28,1.66,-1.27,5.94,25.75,-8.11,14.6954,39.4877,61.2919,-17.1,1.34,79.06,4.92,-21.93,3.46,0.25,59.25,-0.29,-5.13,0.94,2.65,-0.93,-34.15,1.9,-0.15,32,0.16,1.19,-25.21,-0.21,6.74,-19.9,16.9,0,0,0,52.07,-8.74,27.82,0.27,-40.55,0.43,22.29,-0.5,-7.75,0,0,0,-51.54,-4.61,-20.54,-0.32,-50.08,-0.49,-26.52,-0.65,11.29,-4.59,2.49,-1.52,7.04,25.12,-9.52,15.3243,39.3455,61.5863,-15.72,0.45,80.87,4.97,-25.67,4.72,0.28,62.47,-0.32,-3.53,-5.48,1.5,-0.54,-32.17,1.42,-0.15,33.79,0.16,1.12,-26.5,-0.17,6.86,-17.46,16.83,0,0,0,51.63,-10.52,26.43,0.27,-40.68,0.43,22.04,-0.47,-7.81,0,0,0,-51.63,-4.58,-20.73,-0.31,-48.68,-0.48,-25.66,-0.64,10.75,-4.6,2.92,-1.77,6.75,24.15,-9.75,15.8459,39.1522,61.8186,-14.41,-0.26,83.09,4.82,-29.54,5.82,0.29,63.76,-0.34,-2.52,-12.14,0.84,-0.07,-30.69,1.37,-0.16,36.22,0.17,0.92,-27.88,-0.14,7.43,-14.25,16.81,0,0,0,50.58,-12.52,24.54,0.27,-41.12,0.43,22.03,-0.44,-7.98,0,0,0,-52.5,-4.69,-21.07,-0.3,-47.65,-0.47,-24.97,-0.6,10.36,-5.49,2.46,-2.14,6.39,23.33,-10.27,16.279,38.9275,62.0158,-13.52,-1.28,86.1,5.04,-33.63,6.79,0.28,63.26,-0.33,-1.92,-17.27,0.52,0.57,-29.82,0.44,-0.16,38.84,0.18,0.58,-28.92,-0.14,7.67,-11.67,16.7,0,0,0,50.47,-15.51,22.57,0.27,-41.29,0.43,22.01,-0.43,-8.05,0,0,0,-52.56,-3.86,-22.03,-0.3,-47.27,-0.47,-24.52,-0.56,10.24,-5.83,1.5,-2.7,6.65,23.17,-11.35,16.6549,38.7006,62.1397,-12.73,-2.04,90.16,4.88,-37.63,7.42,0.26,60.7,-0.31,-1.44,-20.5,0.37,0.2,-29.2,-2.06,-0.17,41.38,0.19,0.2,-29.97,-0.15,7.53,-9.15,15.33,0,0,0,50.75,-18.37,21.05,0.27,-42.02,0.43,22.24,-0.42,-8.31,0,0,0,-52.8,-3.07,-23.24,-0.3,-46.73,-0.47,-24.05,-0.5,10.06,-5.71,0.53,-3.46,6.86,22.21,-12.52,16.9905,38.5304,62.338,-12.42,-4.06,94.4,6.57,-41.82,8.7,0.23,56.34,-0.27,-1.21,-21.89,0.33,1.27,-28.72,-4.46,-0.18,42.95,0.2,-0.21,-30.87,-0.19,9.01,-8.24,13.93,0,0,0,50.93,-20.21,18.25,0.28,-43.43,0.44,22.69,-0.42,-8.83,0,0,0,-52.68,-1.23,-23.74,-0.3,-47.29,-0.47,-23.98,-0.44,10.3,-5.79,-0.15,-4.15,7.43,21.95,-14,17.3807,38.4383,62.5069,-11.99,-5.91,99.14,7.67,-45.41,9.51,0.2,49.94,-0.23,-1.41,-20.47,0.39,2.14,-27.9,-7.03,-0.18,43.9,0.2,-0.74,-31.85,-0.27,10.66,-7.95,12.43,0,0,0,50.7,-22.07,15.36,0.29,-45.16,0.46,23.41,-0.46,-9.47,0,0,0,-52.98,1.43,-24.42,-0.31,-48.44,-0.48,-24.16,-0.39,10.77,-6.25,-0.42,-4.83,8.63,21.79,-16.04,17.7798,38.3209,62.4744,-11.93,-6.1,104.22,6.73,-48.3,10.92,0.17,41.78,-0.19,-1.89,-15.2,0.62,0.77,-27.43,-10.55,-0.18,45.08,0.21,-1.29,-32.96,-0.37,10.21,-7.83,10.66,0,0,0,51.39,-24.96,13.49,0.29,-46.33,0.46,24.08,-0.53,-9.89,0,0,0,-52.89,4.25,-24.72,-0.32,-51.14,-0.5,-24.86,-0.35,11.88,-5.99,-0.88,-5.72,9.27,21.22,-17.8,18.1493,38.1356,62.3953,-12.17,-6.67,109.2,6.18,-51.42,13.19,0.15,33.75,-0.16,-1.58,-7.67,0.79,-0.14,-27.03,-13.65,-0.18,45.76,0.21,-2.19,-34.78,-0.59,9.62,-7.79,8.53,0,0,0,52.82,-28.23,12.69,0.3,-47.11,0.47,24.75,-0.59,-10.16,0,0,0,-52.43,7.01,-25.42,-0.35,-54.98,-0.54,-26.04,-0.42,13.47,-5.01,-1.8,-6.67,9.26,20.71,-19.04,18.5327,37.9266,62.3306,-12.51,-8.2,113.7,7,-55.31,15.58,0.14,27.66,-0.15,0.12,-2.99,0.26,0.43,-26.59,-15.53,-0.18,45.54,0.21,-3.55,-36.99,-1.01,10.6,-8.35,7.13,0,0,0,52.83,-31.22,11.79,0.31,-48.41,0.48,25.56,-0.63,-10.64,0,0,0,-52.34,9.7,-28.06,-0.39,-58.94,-0.59,-27.24,-0.53,15.17,-5.38,-2.33,-7.31,10.43,19.49,-20.68,18.8784,37.7787,62.1958,-12.99,-9.63,117.48,6.76,-59.4,13.81,0.14,24.32,-0.14,0.19,-5.62,0.25,0.87,-26.59,-17.04,-0.18,45.32,0.21,-4.74,-38.36,-1.43,11.58,-10.51,5.88,0,0,0,52.43,-33.27,11.28,0.31,-48.77,0.48,25.99,-0.63,-10.77,0,0,0,-52.74,12.49,-29.49,-0.44,-62.51,-0.64,-28.49,-0.74,16.71,-5.73,-1.47,-7.54,11.08,18.32,-21.65,19.2678,37.6863,62.0194,-12.92,-10.81,120.24,6.79,-62.39,10.29,0.14,23.66,-0.13,-1.47,-11.91,0.66,1.55,-26.24,-18.53,-0.18,45.51,0.21,-5.44,-38.75,-1.65,12.12,-11.46,5.04,0,0,0,52.62,-34.98,11.52,0.31,-49.7,0.49,26.59,-0.63,-11.13,0,0,0,-53.09,14.68,-30.19,-0.48,-64.75,-0.68,-29.45,-0.9,17.67,-5.66,-1.57,-7.85,11.45,18.12,-22.37,19.7018,37.5851,61.8244,-12.64,-11.59,122.51,7.17,-64.15,7.58,0.14,24.52,-0.14,-2.39,-16.6,0.66,2.07,-25.8,-19.14,-0.18,45.84,0.21,-5.94,-38.83,-1.8,11.77,-10.84,4.69,0,0,0,53.93,-37.6,12.55,0.32,-50.36,0.5,27.07,-0.61,-11.39,0,0,0,-52.3,15.48,-33.24,-0.49,-65.72,-0.7,-30.09,-0.99,18.08,-4.85,-2.86,-8.46,11.6,18.16,-23.08,20.0708,37.5055,61.5065,-12.57,-12.25,124.83,7.18,-65.74,4.67,0.14,26.08,-0.14,-3.12,-16.09,0.79,2.08,-24.87,-20.19,-0.18,45.28,0.21,-6.44,-39.27,-1.99,12.25,-10.68,3.35,0,0,0,54.61,-38.86,14.1,0.32,-50.55,0.5,27.35,-0.57,-11.47,0,0,0,-53.01,15.7,-34.61,-0.5,-66.24,-0.71,-30.73,-1.03,18.29,-4.7,-3.85,-8.69,10.91,18.04,-22.8,20.5723,37.4686,61.0863,-12.6,-12.67,126.17,9.09,-66.64,4.1,0.14,27.59,-0.15,-3.84,-14.03,1.05,2.56,-23.36,-20.21,-0.18,43.88,0.2,-7.28,-40,-2.34,12.49,-11.24,2.83,0,0,0,55.22,-39.37,14.93,0.32,-50.4,0.5,27.47,-0.53,-11.41,0,0,0,-53.75,16.24,-35.33,-0.51,-66.5,-0.72,-31.29,-1.01,18.4,-4.79,-4.21,-8.59,10.63,18.52,-22.43,21.0716,37.3708,60.5259,-13.03,-13.06,127.11,11.43,-66.9,4.28,0.15,28.2,-0.15,-3.87,-13.55,1.09,2.51,-22.07,-19.72,-0.17,42.67,0.2,-7.65,-40.24,-2.5,11.43,-13,3.1,0,0,0,56.24,-39.43,14.63,0.32,-50.42,0.5,27.67,-0.48,-11.43,0,0,0,-53.28,17.38,-36.17,-0.51,-66.57,-0.72,-31.73,-0.94,18.43,-4.22,-3.09,-8.56,10.87,18.22,-22.74,21.7041,37.2631,59.8828,-12.75,-13.89,127.85,13.51,-66.34,1.95,0.15,28.36,-0.15,-4.4,-13.25,1.22,3.23,-20.34,-19.74,-0.17,41.39,0.19,-7.83,-40.21,-2.55,11.18,-14.29,3.48,0,0,0,57.22,-38.88,14.19,0.32,-50.87,0.5,27.95,-0.44,-11.61,0,0,0,-52.86,18.15,-37.02,-0.51,-66.41,-0.72,-32.14,-0.82,18.38,-3.81,-2.43,-8.56,11.2,17.85,-23.03,22.2574,37.1836,59.0979,-13.35,-14.19,128.37,13.97,-65.77,-0.36,0.15,28.31,-0.15,-4.57,-14.28,1.17,2.71,-18.82,-19.96,-0.17,40.02,0.19,-7.68,-39.98,-2.48,10.36,-15.22,3.59,0,0,0,58.22,-38.26,14.76,0.32,-51.19,0.5,28.12,-0.43,-11.75,0,0,0,-52.94,17.99,-37.94,-0.49,-65.74,-0.7,-32.47,-0.62,18.1,-3.54,-3.05,-8.6,11.05,18.07,-22.82,22.866,37.0894,58.2063,-13.88,-15.24,128.92,14.26,-65.42,-2.94,0.15,28.05,-0.15,-3.78,-18.23,0.74,2.66,-17.35,-20.24,-0.16,38.12,0.18,-7.39,-39.56,-2.34,10.77,-17,4.18,0,0,0,58,-37.59,14.91,0.33,-51.5,0.51,28.37,-0.38,-11.88,0,0,0,-53.55,18.26,-38.35,-0.49,-65.48,-0.7,-32.92,-0.36,18.04,-3.92,-3.29,-8.59,11.5,17.96,-23.02,23.5245,36.9678,57.1564,-14.36,-16.08,129.41,17.06,-64.73,2.29,0.14,27.45,-0.15,-1.97,-22.58,0.37,2.72,-15.31,-19.84,-0.16,35.65,0.17,-6.88,-38.65,-2.09,11.24,-19.16,4.85,0,0,0,56.86,-36.25,14.3,0.33,-52.01,0.51,28.67,-0.34,-12.1,0,0,0,-54.2,18.48,-39.57,-0.47,-64.13,-0.67,-32.89,-0.15,17.47,-4.3,-3.31,-8.61,11.6,17.94,-23.15,24.2698,36.8855,55.9054,-14.34,-17.34,129.57,20.37,-63.58,7.58,0.14,27.1,-0.14,-0.64,-25.9,0.3,3.31,-12.49,-19.54,-0.15,32.46,0.16,-5.56,-36.77,-1.55,11.89,-21.18,6.18,0,0,0,56.05,-35.26,13.49,0.33,-52.23,0.51,28.74,-0.34,-12.19,0,0,0,-53.94,18.84,-41.14,-0.44,-62.54,-0.64,-32.76,0.07,16.79,-3.93,-2.95,-8.77,11.47,17.77,-23.42,25.0345,36.8337,54.4716,-14.67,-18.49,129.8,21.64,-62.69,11.34,0.14,27.79,-0.15,-0.03,-27.84,0.31,3.57,-9.54,-19.04,-0.15,28.6,0.15,-3.59,-33.55,-0.88,12.14,-23.47,7.48,0,0,0,55.23,-34.35,12.91,0.33,-52.38,0.52,28.74,-0.36,-12.25,0,0,0,-53.42,19.1,-42.74,-0.42,-61.29,-0.62,-32.65,0.26,16.28,-3.85,-2.64,-8.96,11.71,17.99,-24,25.8538,37.0016,52.9102,-15.18,-20.24,129.83,23.31,-63.04,15.37,0.15,29.65,-0.15,-0.74,-25.43,0.3,4.08,-6.69,-17.76,-0.14,24.15,0.14,-0.43,-27.99,-0.29,13.64,-26.49,8.6,0,0,0,53.96,-32.24,12.3,0.33,-52.61,0.52,28.78,-0.38,-12.34,0,0,0,-53.39,18.64,-43.47,-0.41,-60.6,-0.61,-32.59,0.38,15.99,-4.19,-2.25,-8.88,11.63,18.5,-24.02,26.5806,37.2304,51.2077,-16.24,-20.88,130.61,21.47,-63.74,17.03,0.15,31.59,-0.16,-1.51,-20.29,0.42,3.32,-4.05,-17.04,-0.14,20.02,0.13,3.09,-21.52,-0.45,12.63,-29.47,8.61,0,0,0,53.48,-30.69,11.74,0.33,-52.67,0.52,28.75,-0.4,-12.36,0,0,0,-52.22,18.75,-43.9,-0.41,-60.44,-0.61,-32.6,0.43,15.94,-3.74,-1.77,-9.02,11.68,19.14,-24.44,27.2736,37.5068,49.3843,-17.51,-20.03,131.14,17.22,-62.64,17.65,0.15,32.35,-0.16,-1.58,-15.64,0.56,1.03,-1.63,-16.35,-0.13,17.47,0.12,7.04,-14.4,-1.63,10.71,-31.04,8.85,0,0,0,52.74,-29.62,11.65,0.34,-52.75,0.52,28.77,-0.41,-12.39,0,0,0,-51.37,19.32,-43.55,-0.42,-61.33,-0.62,-32.84,0.43,16.34,-4.02,-1.35,-9.19,12.12,18.96,-25.16,27.8944,37.9923,47.5039,-19.41,-17.25,130.74,12.89,-58.94,22.59,0.15,31.9,-0.16,-0.75,-13.02,0.47,-3.36,-0.2,-14.82,-0.13,17.58,0.12,11.14,-7.27,-3.91,7.63,-31.65,9.35,0,0,0,51.99,-28.33,12.01,0.34,-52.82,0.52,28.83,-0.39,-12.43,0,0,0,-51.06,19.34,-42.33,-0.44,-62.24,-0.64,-32.98,0.32,16.73,-4.42,-1.16,-9.21,12.28,19.39,-25.46,28.5293,38.4813,45.7656,-20.46,-15.67,129.83,10.24,-55.63,25.48,0.15,31.43,-0.16,-0.11,-12.27,0.33,-6.04,-0.07,-12.37,-0.14,18.62,0.12,15.96,-0.16,-7.61,5.89,-32.42,10.31,0,0,0,52.09,-27.1,12.8,0.33,-52.66,0.52,28.79,-0.39,-12.36,0,0,0,-50.35,19.99,-39.23,-0.46,-63.61,-0.66,-33.23,0.22,17.33,-4.51,-0.79,-9.1,12.55,19.82,-25.6,29.1749,38.9516,44.1918,-20.61,-15.28,129.04,8.27,-53.04,24.85,0.15,31.3,-0.16,-0.05,-12.84,0.32,-6.79,-0.26,-9.06,-0.14,19.22,0.12,20.4,5.1,-11.73,5.75,-32.94,11.07,0,0,0,52.38,-25.65,13.71,0.34,-52.79,0.52,28.83,-0.39,-12.41,0,0,0,-50.18,19.66,-36.79,-0.45,-63.14,-0.65,-32.89,0.04,17.06,-4.61,-0.58,-8.93,12.93,20.4,-25.68,29.7652,39.2597,42.7455,-20.7,-14.7,127.88,6.6,-50.47,24.25,0.15,31.15,-0.16,-0.24,-14.35,0.36,-7.77,-0.73,-6.9,-0.14,20.24,0.13,19.52,5.72,-11.39,5.81,-33.29,11.94,0,0,0,52.93,-23.8,14.58,0.34,-52.84,0.52,28.82,-0.4,-12.43,0,0,0,-50.31,19.28,-33.62,-0.44,-62.29,-0.64,-32.31,-0.2,16.61,-4.34,0.03,-8.63,12.83,20.88,-25.25,30.294,39.472,41.439,-20.63,-14.03,127.01,5.5,-47.83,24.96,0.15,30.98,-0.16,-0.24,-15.57,0.35,-8.62,-1.51,-6.94,-0.14,22.18,0.13,16.99,5.89,-9.89,5.16,-33.11,12.7,0,0,0,54.53,-23.19,15.69,0.33,-52.03,0.51,28.49,-0.41,-12.1,0,0,0,-49.9,19.24,-31.44,-0.43,-61.89,-0.63,-32.02,-0.3,16.4,-3.59,0.32,-8.59,12.61,21.1,-24.98,30.7994,39.631,40.2409,-20.15,-13.29,126.92,3.98,-45.12,24.83,0.15,30.7,-0.15,-0.23,-16.63,0.34,-9.01,-2.13,-7.75,-0.14,24.68,0.14,14.88,6.23,-8.7,5.26,-32.46,12.68,0,0,0,55.46,-21.98,16.92,0.33,-51.49,0.51,28.19,-0.45,-11.87,0,0,0,-51.06,18.61,-29.3,-0.42,-60.98,-0.62,-31.61,-0.37,15.98,-4.02,0.87,-8.17,12.64,21.04,-24.5,31.2515,39.7589,39.1071,-19.76,-12.64,127.21,1.73,-42.85,22.83,0.15,30.47,-0.15,-0.36,-17.46,0.36,-9.11,-3.01,-8.74,-0.14,27.31,0.14,13.47,6.09,-7.81,4.68,-31.93,12.69,0,0,0,57.1,-21.67,17.85,0.32,-50.63,0.5,27.8,-0.46,-11.51,0,0,0,-51.79,17.86,-28.72,-0.39,-59.05,-0.59,-30.73,-0.5,15.08,-4,1.63,-7.96,12.81,20.58,-24.43,31.6598,39.8458,38.0846,-19.17,-12.2,127.57,-0.07,-40.9,20.58,0.15,30.62,-0.15,-0.5,-17.93,0.37,-8.55,-3.94,-9.98,-0.15,29.73,0.15,12.65,5.03,-7.1,4.32,-31.95,12.7,0,0,0,58.52,-21.46,18.35,0.31,-49.73,0.49,27.51,-0.44,-11.16,0,0,0,-52.27,18.2,-26.62,-0.39,-58.45,-0.58,-30.18,-0.62,14.8,-3.42,3.01,-7.8,12.64,20.28,-24.26,32.0174,39.9494,37.1567,-18.68,-11.61,127.71,-1.2,-39.12,20.11,0.15,30.95,-0.16,-0.48,-17.91,0.37,-7.86,-5.12,-10.56,-0.15,32.23,0.16,12.26,3.63,-6.57,3.48,-31.14,13.16,0,0,0,59.83,-21.88,19.28,0.31,-49.56,0.49,27.5,-0.43,-11.09,0,0,0,-51.83,18.51,-25.01,-0.39,-59.04,-0.59,-30.08,-0.71,15.05,-2.85,3.69,-7.75,12.81,19.81,-24.31,32.2952,40.0948,36.33,-18.21,-10.72,127.97,-2.23,-37.38,20.24,0.15,31.31,-0.16,-0.34,-17.23,0.35,-7.37,-6.36,-10.98,-0.16,34.92,0.17,11.65,2.59,-6.02,0.97,-30.28,13.35,0,0,0,62.46,-22.46,19.48,0.31,-49.54,0.49,27.48,-0.43,-11.08,0,0,0,-49.52,18.74,-24.49,-0.4,-59.5,-0.6,-29.93,-0.78,15.24,-0.96,4.45,-7.98,13.09,19.13,-24.65,32.5257,40.2469,35.6342,-17.31,-10.63,128.55,-2.23,-36.1,20.52,0.15,32,-0.16,-0.16,-16.4,0.33,-5.95,-7.78,-11.28,-0.16,37.36,0.18,10.36,1.61,-5.17,1.6,-29.13,13.1,0,0,0,62.41,-21.11,19.83,0.32,-49.95,0.49,27.59,-0.44,-11.24,0,0,0,-50,17.48,-22.99,-0.39,-58.81,-0.59,-29.48,-0.8,14.94,-1.64,5.18,-7.48,13.31,19.14,-24.26,32.6661,40.3975,34.9671,-16.85,-10.01,129.14,-3.04,-35.1,20.15,0.15,32.82,-0.16,0.02,-15.18,0.3,-5.14,-9.02,-11.11,-0.17,39.32,0.18,8.67,0.02,-4.09,1.22,-27.71,12.85,0,0,0,62.91,-20.09,19.82,0.32,-49.96,0.49,27.55,-0.46,-11.24,0,0,0,-50.27,16.38,-21.3,-0.38,-57.9,-0.58,-28.97,-0.81,14.55,-2.2,5.63,-7.05,13.82,18.97,-24.12,32.7464,40.4265,34.4113,-16.14,-9.45,129.85,-3.5,-34.42,20.3,0.15,34.2,-0.17,0.13,-14.46,0.28,-4.01,-9.66,-10.25,-0.17,40.09,0.19,5.82,-3.95,-2.38,0.88,-25.87,12.56,0,0,0,63.43,-19.29,19.76,0.32,-49.97,0.49,27.34,-0.52,-11.24,0,0,0,-50.32,14.99,-20.47,-0.37,-56.8,-0.56,-28.27,-0.8,14.09,-2.44,5.73,-6.77,13.96,18.52,-23.78,32.7435,40.4539,33.8623,-15.54,-8.68,130.67,-4.25,-34.13,19.32,0.16,36.19,-0.17,0.29,-13.02,0.24,-3.24,-10.45,-9.14,-0.17,39.88,0.19,2.59,-9.71,-0.89,0.27,-24.07,12.28,0,0,0,64.04,-18.1,19.22,0.32,-50.04,0.49,26.99,-0.6,-11.26,0,0,0,-50.62,13.78,-20.21,-0.36,-56.15,-0.55,-27.74,-0.77,13.83,-2.26,6.02,-6.73,13.78,17.86,-23.57,32.6426,40.2819,33.4597,-14.88,-7.99,131.79,-4.4,-34.34,20.69,0.16,38.46,-0.18,0.54,-12.13,0.18,-1.99,-12.08,-7.01,-0.17,39.23,0.18,0.7,-15.95,-0.3,-0.19,-22.2,11.94,0,0,0,64.79,-16.9,18.49,0.32,-49.94,0.49,26.65,-0.64,-11.23,0,0,0,-51.09,12.95,-18.93,-0.37,-56.4,-0.56,-27.57,-0.74,13.96,-2.47,6.13,-6.56,14.04,17.46,-23.51,32.4531,40.1653,33.1296,-14.47,-7.09,132.74,-4.72,-34.87,21.26,0.17,40.9,-0.19,0.95,-10.08,0.04,-0.93,-13.97,-4.61,-0.16,38.43,0.18,0.53,-21.29,-0.23,-0.9,-20.2,11.7,0,0,0,65.73,-15.58,17.65,0.31,-49.77,0.49,26.43,-0.65,-11.16,0,0,0,-51.61,12,-18.11,-0.37,-56.93,-0.56,-27.58,-0.73,14.2,-2.75,5.86,-6.39,14.22,17.11,-23.3,32.168,40.1628,32.8488,-13.96,-6.58,133.79,-5.04,-35.63,19.95,0.18,43.51,-0.2,1.54,-8,-0.17,-0.31,-15.5,-4.08,-0.16,37.82,0.18,0.75,-24.14,-0.2,-1.92,-17.26,11.63,0,0,0,67.25,-15.57,18.32,0.31,-49.22,0.49,26.17,-0.64,-10.95,0,0,0,-51.46,10.66,-18.87,-0.38,-57.68,-0.57,-27.74,-0.74,14.52,-2.59,4.42,-6.5,14.31,16.45,-23.02,31.7956,40.1679,32.6524,-13.29,-6.45,134.69,-4.38,-36.74,20.77,0.18,46.05,-0.21,2.29,-5.33,-0.52,-0.07,-16.39,-4.96,-0.16,37.61,0.18,0.78,-24.64,-0.2,-1.83,-14.59,11.81,0,0,0,67.81,-15.48,19.34,0.31,-48.91,0.48,26.2,-0.63,-10.82,0,0,0,-52.03,9.04,-20.58,-0.38,-58.08,-0.58,-27.84,-0.75,14.7,-2.61,2.88,-6.71,13.36,16.26,-22.27,31.3349,40.1856,32.5772,-12.63,-6.72,135.56,-2.91,-38.64,22.63,0.19,48.87,-0.23,3.45,-1.54,-1.17,0.58,-16.45,-5.21,-0.16,36.91,0.17,0.77,-24.17,-0.21,-0.7,-13.4,12.1,0,0,0,67.51,-14.83,19.27,0.31,-48.67,0.48,26.38,-0.59,-10.72,0,0,0,-53.35,8.94,-20.71,-0.4,-59.15,-0.59,-28.28,-0.8,15.15,-3.39,2.38,-6.64,12.94,16.11,-21.83,30.8149,40.0558,32.5726,-12.38,-7.2,136.33,-0.98,-41.35,25.18,0.21,52.16,-0.24,5.03,2.68,-2.21,1.55,-16.01,-4.42,-0.16,35.45,0.17,0.78,-25.82,-0.19,0.12,-12.31,12.38,0,0,0,67.58,-14.17,19.41,0.31,-48.49,0.48,26.56,-0.55,-10.65,0,0,0,-54.33,8.52,-21.72,-0.41,-60.05,-0.6,-28.81,-0.85,15.52,-4.41,1.11,-6.47,12.86,16.28,-21.22,30.2205,39.8031,32.6488,-12.94,-8.14,136.99,1.15,-45.27,28.4,0.23,55.59,-0.27,6.84,7.19,-3.64,2.42,-16.44,-3.27,-0.15,34.03,0.17,0.57,-28.06,-0.18,0.54,-12.14,12.55,0,0,0,67.75,-13.29,19.56,0.31,-48.58,0.48,26.87,-0.49,-10.69,0,0,0,-54.9,8.32,-23.17,-0.42,-61.39,-0.62,-29.64,-0.9,16.09,-5.19,-0.29,-6.37,12.26,16.19,-20.28,29.5983,39.4419,32.817,-13.35,-9.85,137.59,4.98,-49.81,32.5,0.25,59.01,-0.29,8.79,11.75,-5.42,3.71,-18.08,-3.01,-0.15,33.55,0.16,0.12,-30.4,-0.21,2.1,-12.09,12.19,0,0,0,67.23,-12.04,20.56,0.31,-48.92,0.48,27.28,-0.41,-10.83,0,0,0,-56,7.39,-24.71,-0.44,-62.28,-0.64,-30.42,-0.88,16.48,-6.28,-2.08,-6.09,11.48,16.04,-18.78,28.9816,39.0178,32.9108,-14.26,-10.77,137.52,9.28,-52.99,37.75,0.27,61.58,-0.32,10.6,14.11,-7.01,3.67,-20.06,-2.59,-0.16,34.42,0.17,-0.55,-33.58,-0.32,2.87,-11.7,12.41,0,0,0,66.14,-11.29,22.22,0.31,-49.15,0.49,27.62,-0.32,-10.94,0,0,0,-56.7,6.16,-26.64,-0.44,-62.46,-0.64,-31.02,-0.78,16.57,-7.49,-4.01,-5.87,10.79,15.95,-17.42,28.4403,38.6305,32.9908,-15.06,-11.66,136.72,14.98,-54.7,43.76,0.28,62.47,-0.32,10.57,10.95,-6.47,3.78,-22.32,-2.13,-0.16,35.87,0.17,-1.23,-36.12,-0.49,3.43,-11.47,13.43,0,0,0,65.2,-10.4,23.72,0.31,-49.19,0.49,27.9,-0.21,-10.97,0,0,0,-56.46,4.86,-28.98,-0.43,-61.72,-0.63,-31.33,-0.6,16.26,-8.24,-5.52,-5.75,10.22,16.26,-16.48,28.0119,38.4446,33.01,-15.66,-13.06,135.86,20.53,-55.37,48.59,0.26,60.84,-0.31,6.09,1.79,-2.65,4.38,-24.7,-1.67,-0.16,37.18,0.18,-1.54,-37.06,-0.58,4.7,-11.96,14.1,0,0,0,63.97,-8.4,25.17,0.31,-49.05,0.49,28.06,-0.11,-10.94,0,0,0,-56.37,3.29,-30.85,-0.41,-60.21,-0.61,-31.38,-0.37,15.63,-8.56,-6.62,-5.38,8.72,16.57,-14.76,27.5615,38.4135,32.8219,-16.72,-13.27,136.01,21.08,-55.09,49.27,0.23,56.31,-0.27,1.65,-7.56,-0.24,3.11,-26.25,-1.74,-0.16,38.15,0.18,-1.75,-37.5,-0.64,4.25,-11.61,13.93,0,0,0,62.73,-7.09,27.46,0.31,-48.42,0.48,27.95,-0.03,-10.7,0,0,0,-56.1,2.01,-32.83,-0.39,-58.66,-0.59,-31.33,-0.13,14.99,-8.95,-8.32,-5.08,7.7,16.81,-13.24,27.1924,38.434,32.5575,-17.15,-14.26,136.92,20.88,-55.1,46.87,0.2,50.37,-0.23,-0.52,-13.32,0.39,2.48,-27.32,-2.29,-0.16,38.25,0.18,-2,-37.85,-0.72,4.99,-11.51,13.27,0,0,0,61,-5.66,29.36,0.3,-47.35,0.47,27.7,0.05,-10.3,0,0,0,-56.47,0.77,-35.08,-0.37,-56.37,-0.56,-30.88,0.04,14.03,-9.13,-9.99,-4.65,6.43,17.66,-11.59,26.8863,38.4632,32.1981,-17.32,-15.28,138.34,20.36,-55.14,43.88,0.18,44.09,-0.2,-1.45,-16.14,0.51,1.65,-27.72,-3.64,-0.16,37.66,0.18,-2.05,-37.88,-0.73,5.54,-11.63,13.26,0,0,0,59.88,-4.78,30.01,0.29,-45.78,0.46,27.13,0.08,-9.7,0,0,0,-56.58,0.96,-37.57,-0.35,-54.11,-0.53,-30.36,0.2,13.1,-9.1,-11.16,-4.53,5.25,18.11,-10.69,26.6578,38.5147,31.738,-17.16,-16.47,140.16,19.81,-55.25,40.76,0.16,38.21,-0.18,-1.81,-18.2,0.5,1.1,-27.49,-4.87,-0.16,36.63,0.17,-2.14,-37.87,-0.76,6.68,-12,13.55,0,0,0,58.78,-3.17,29.5,0.28,-44.26,0.45,26.52,0.08,-9.12,0,0,0,-57.08,1.54,-40.29,-0.33,-51.84,-0.51,-29.75,0.32,12.17,-9.43,-11.6,-4.49,4.52,18.12,-10.21,26.524,38.5079,31.1817,-16.32,-17.84,142.88,19.39,-55.67,38.65,0.15,33.28,-0.16,-1.91,-20,0.46,1.14,-26.51,-6.27,-0.16,35.34,0.17,-2.41,-37.96,-0.84,7.08,-12.58,13.81,0,0,0,59.32,-2.48,29.83,0.27,-41.58,0.43,25.32,0.04,-8.13,0,0,0,-56.16,2.49,-44.19,-0.31,-49.8,-0.49,-29.1,0.39,11.35,-8.91,-12.05,-4.71,4.03,18.48,-10.43,26.4147,38.4718,30.5179,-15.37,-19.09,145.89,17.92,-56.61,34.96,0.15,29.6,-0.15,-1.87,-21.99,0.39,1.31,-25.22,-7.24,-0.15,33.9,0.16,-2.91,-38.1,-0.99,7.68,-13.19,14.32,0,0,0,59.09,-1.46,30.32,0.27,-40.28,0.42,24.65,-0.02,-7.66,0,0,0,-55.56,3.88,-47.61,-0.3,-48.16,-0.48,-28.59,0.47,10.71,-8.75,-12.31,-4.99,3.24,18.61,-10.62,26.354,38.4308,29.7643,-14.16,-20.28,148.96,16.93,-57.6,32.92,0.14,27.47,-0.15,-1.52,-24.23,0.31,1.72,-23.57,-8.17,-0.15,32.2,0.16,-3.44,-38.26,-1.15,8.49,-13.74,15.51,0,0,0,58.04,-0.17,30.11,0.27,-40.4,0.42,24.58,-0.08,-7.7,0,0,0,-55.17,5.42,-51.13,-0.3,-46.76,-0.47,-28.17,0.56,10.18,-9.47,-12.37,-5.43,3.48,18.2,-11.44,26.3278,38.3991,28.9415,-12.84,-21.19,152.06,16.85,-57.84,36.06,0.14,26.9,-0.14,-0.41,-27.38,0.29,2.3,-21.55,-8.55,-0.15,30.39,0.15,-3.88,-38.01,-1.26,9.88,-15.03,16.16,0,0,0,56.62,2.41,30.15,0.27,-40.01,0.42,24.22,-0.16,-7.55,0,0,0,-55.49,5.79,-53.33,-0.29,-45.09,-0.46,-27.52,0.55,9.53,-10.15,-12.04,-5.27,3.42,18.61,-11.28,26.2832,38.3676,28.0625,-11.31,-22.6,155.4,16.57,-58.46,38.78,0.14,27.6,-0.15,0.76,-29.87,0.4,3.16,-19.91,-9.61,-0.15,28.56,0.15,-4.05,-37.49,-1.28,11.17,-17.76,17.25,0,0,0,55.92,5.31,29.82,0.27,-39.98,0.42,24.09,-0.21,-7.53,0,0,0,-55.2,6.82,-54.2,-0.28,-43.31,-0.44,-26.71,0.47,8.85,-10.1,-10.91,-5.02,3.24,19.23,-11.15,26.2289,38.2572,27.0304,-10.07,-23.82,158.21,16.62,-58.55,42.28,0.15,29.39,-0.15,1.47,-31.41,0.52,3.46,-18.01,-11.08,-0.14,26.61,0.14,-3.79,-36.75,-1.17,10.72,-19.92,19.05,0,0,0,56.33,6.89,29.05,0.27,-40.28,0.42,24.16,-0.23,-7.63,0,0,0,-53.41,8.21,-53.35,-0.28,-42.49,-0.44,-26.28,0.4,8.53,-9.64,-10.66,-5.11,4.18,20.26,-11.98,26.2533,38.1557,25.8334,-9.12,-24.41,160.3,17.39,-57.59,47.23,0.15,32,-0.16,1.57,-31.85,0.54,3.79,-15.16,-11.27,-0.14,23.99,0.14,-3.43,-35.73,-1.04,10.44,-21.28,20.98,0,0,0,55.86,8.37,28.39,0.27,-40.3,0.42,23.91,-0.32,-7.63,0,0,0,-52.01,8.82,-51.19,-0.27,-42.05,-0.43,-25.94,0.3,8.35,-9.76,-10.77,-5.11,4.91,20.95,-12.43,26.2671,38.1671,24.5054,-8.22,-24.62,162.32,17.82,-56.39,50.97,0.16,34.51,-0.17,1.13,-30.81,0.45,4.11,-11.83,-11.71,-0.14,20.97,0.13,-2.47,-33.65,-0.75,9.45,-22.98,23.03,0,0,0,55.84,9.3,28.25,0.27,-40.29,0.42,23.48,-0.42,-7.62,0,0,0,-49.63,9,-49.96,-0.27,-41.63,-0.43,-25.53,0.14,8.17,-9.19,-10.54,-5.47,4.9,20.68,-12.48,26.1875,38.1702,23.1836,-6.95,-24.9,165.32,16.71,-56.23,49.58,0.16,36.34,-0.17,0.3,-28.43,0.33,4.25,-8.86,-12.69,-0.14,18.94,0.12,-0.8,-30.5,-0.42,8.46,-25.28,24.8,0,0,0,55.08,9.85,27.28,0.27,-41.69,0.43,23.63,-0.5,-8.12,0,0,0,-46.94,9.57,-49.01,-0.27,-41,-0.43,-25.02,0.01,7.92,-8.63,-9.82,-5.29,5.06,19.84,-12.25,26.0563,38.2059,21.8355,-5.21,-24.92,169.47,13.43,-56.2,44.16,0.16,37.75,-0.18,-0.43,-25.4,0.29,4.05,-6.71,-14.1,-0.14,19.3,0.12,0.65,-27.22,-0.28,6.99,-26.8,25.95,0,0,0,53.65,9,26.82,0.28,-43.14,0.44,23.86,-0.55,-8.64,0,0,0,-43.88,10.13,-48.17,-0.27,-40.37,-0.42,-24.65,-0.04,7.69,-7.45,-9.87,-4.69,4.94,19.16,-11,25.9384,38.3904,20.4835,-2.7,-24.84,174.55,9.73,-55.25,37.8,0.16,38.49,-0.18,-1.07,-22.3,0.34,3.88,-5.93,-15.19,-0.14,22.41,0.13,2.17,-22.59,-0.35,6.63,-27.49,26.74,0,0,0,51.33,7.51,27.22,0.28,-43.23,0.44,23.64,-0.55,-8.68,0,0,0,-41.32,9.46,-48.11,-0.26,-39.88,-0.42,-24.29,-0.1,7.51,-6.72,-10.5,-3.67,4.37,18.81,-8.72,25.7911,38.6536,19.0948,-0.31,-24.09,179.36,5.76,-52.97,31.02,0.16,38.12,-0.18,-1.07,-21.67,0.35,2.5,-6.24,-15.4,-0.15,28.07,0.15,3.51,-15.92,-0.79,5.58,-28.48,27.72,0,0,0,50.31,5.84,27.66,0.27,-42.36,0.44,23.05,-0.53,-8.38,0,0,0,-37.81,8.48,-48.46,-0.26,-39.26,-0.42,-23.79,-0.2,7.29,-5.1,-10.88,-2.32,4.03,19,-6.07,25.5588,38.8839,17.6704,2.2,-22.96,-175.61,2.43,-50.17,24.55,0.16,37.45,-0.18,-0.8,-22.6,0.33,-0.06,-7.35,-14.8,-0.16,34.51,0.17,2.5,-7.27,-1,4.53,-28.46,27.98,0,0,0,49.2,4.39,29.2,0.27,-41.4,0.43,22.33,-0.48,-8.07,0,0,0,-35.28,5.93,-49.02,-0.26,-37.98,-0.41,-23.01,-0.27,6.85,-3.54,-12.32,-0.57,3.87,19.87,-2.71,25.2727,38.9832,16.3996,4.34,-21.88,-170.65,-0.22,-47.76,19.05,0.16,37.21,-0.18,-0.69,-23.12,0.32,-3.07,-9.46,-13.4,-0.17,40.16,0.19,-3.03,2.75,1.32,4.47,-28.51,29.15,0,0,0,47.46,3.04,30.5,0.27,-40.47,0.42,21.63,-0.41,-7.77,0,0,0,-34.08,3.99,-48.59,-0.26,-37.32,-0.41,-22.53,-0.31,6.62,-2.76,-12.73,1.12,3.13,20.29,0.69,24.9763,39.0951,15.273,6.29,-20.82,-166,-1.43,-45.42,15.91,0.16,37.01,-0.18,-0.67,-23.25,0.31,-5.55,-11.15,-12.71,-0.18,44.83,0.21,-5.6,6.98,3.02,3.1,-29.32,30.4,0,0,0,47.4,1.62,30.86,0.27,-40.28,0.42,21.33,-0.35,-7.72,0,0,0,-31.53,1.81,-47.79,-0.25,-36.81,-0.4,-21.99,-0.38,6.46,-0.22,-12.55,2.66,1.88,20.08,4.01,24.5693,39.1959,14.2938,8.37,-19.76,-160.04,-3.09,-43.37,12.77,0.16,36.07,-0.17,-0.7,-22.8,0.32,-8.29,-12.34,-13.84,-0.19,48.81,0.22,-1.88,5.06,0.87,2.13,-30.33,30.66,0,0,0,46.65,0.09,30.7,0.27,-40.3,0.42,21.12,-0.29,-7.75,0,0,0,-29.75,0.43,-44.57,-0.25,-36.99,-0.4,-21.81,-0.43,6.52,1.81,-11.59,3.95,0.19,20.06,7.09,24.2157,39.4038,13.404,10.8,-17.83,-153.51,-4.06,-40.71,8.7,0.16,34.72,-0.17,-0.72,-22.2,0.33,-10.03,-13.4,-13.91,-0.21,51.49,0.24,1.69,4.6,-1.01,2.04,-29.72,30.77,0,0,0,44.87,-2.77,30.81,0.27,-40.31,0.42,20.86,-0.19,-7.79,0,0,0,-29.22,-1.53,-40.26,-0.25,-37.05,-0.4,-21.56,-0.46,6.54,2.98,-11.46,4.69,-1.76,20.61,9.3,23.803,39.6137,12.6299,13.09,-15.59,-145.72,-5.29,-38.3,4.04,0.15,33.49,-0.16,-0.66,-21.34,0.34,-11.43,-14.31,-13.54,-0.21,52.4,0.24,4.45,5.93,-2.56,2.16,-29.43,30.77,0,0,0,42.01,-5.98,29.52,0.27,-41.22,0.43,20.93,-0.07,-8.14,0,0,0,-29.04,-2.68,-36.11,-0.26,-37.58,-0.41,-21.54,-0.48,6.72,2.66,-10.57,4.73,-2.35,21.1,9.73,23.4455,39.7703,11.9335,15.41,-12.74,-137.31,-5.67,-36.46,-0.48,0.15,33,-0.16,-0.46,-20.49,0.34,-11.83,-15.1,-12.17,-0.21,52.13,0.24,5.57,5.67,-3.15,1.92,-29.34,30.25,0,0,0,39.55,-9.04,26.15,0.28,-42.63,0.44,21.27,0.02,-8.68,0,0,0,-28,-3.74,-32.59,-0.26,-38.62,-0.41,-21.72,-0.49,7.08,2.78,-9.43,4.13,-2.11,20.6,8.63,23.1333,39.8347,11.4253,17.29,-9.7,-127.89,-6.88,-35.48,-6.57,0.15,33.16,-0.16,-0.23,-19.62,0.33,-12.32,-16.1,-10.56,-0.21,51.54,0.24,6.04,3.76,-3.22,0.96,-28.39,29.27,0,0,0,36.71,-13.23,21.19,0.28,-44.03,0.45,21.69,0.07,-9.21,0,0,0,-27.44,-4.93,-29.05,-0.26,-39.83,-0.42,-21.94,-0.49,7.5,1.77,-9.21,2.79,-0.65,20.31,5.45,22.8629,39.8676,10.9472,18.87,-5.93,-117.98,-7.73,-34.77,-12.82,0.15,33.79,-0.16,0.01,-19.06,0.31,-12.04,-16.7,-8.74,-0.2,50.71,0.24,6.28,1.5,-3.1,1.35,-27.7,28.7,0,0,0,32.34,-16.62,14.42,0.29,-46.01,0.46,22.26,0.15,-9.98,0,0,0,-27.26,-4.89,-24.68,-0.27,-41.73,-0.43,-22.44,-0.48,8.18,-0.5,-7.69,1.09,1.84,19.19,1.06,22.6253,39.9662,10.5168,19.88,-1.64,-107.59,-7.78,-34.17,-16.26,0.16,34.69,-0.17,0.48,-18.14,0.25,-11.53,-17.35,-7.21,-0.2,49.73,0.23,6.27,1.21,-3.07,1.53,-26.33,27.12,0,0,0,27.8,-20.3,7.62,0.3,-47.45,0.47,22.59,0.26,-10.57,0,0,0,-26.73,-5.76,-20.69,-0.28,-43.8,-0.45,-22.99,-0.46,8.95,-2.42,-7.06,-0.85,3.82,18.42,-3.6,22.419,40.1017,10.0906,19.99,3.02,-97.09,-6.96,-33.15,-15.67,0.16,35.69,-0.17,0.6,-17.67,0.23,-10.44,-17.86,-5.35,-0.2,48.96,0.23,6.26,2.09,-3.17,1.81,-25.16,26.25,0,0,0,22.91,-24.21,-0.26,0.3,-48.12,0.48,22.72,0.33,-10.86,0,0,0,-25.39,-5.53,-16.4,-0.3,-46.72,-0.47,-23.78,-0.43,10.08,-4.61,-5.91,-3.18,6.66,17.25,-9.52,22.2604,40.1602,9.6862,19.11,7.46,-86.71,-5.55,-31.54,-11.23,0.16,36.27,-0.17,0.25,-18.19,0.28,-9.5,-18.17,-3.76,-0.2,49.01,0.23,5.68,1.04,-2.78,2.48,-24.73,24.16,0,0,0,18.4,-24.72,-7.84,0.32,-49.87,0.49,23.07,0.52,-11.61,0,0,0,-23.99,-5.9,-10.07,-0.31,-48.64,-0.48,-24.21,-0.38,10.85,-6.15,-3.63,-4.97,9.05,15.57,-14.46,22.1453,40.1918,9.4551,17.97,10.4,-76.58,-5.3,-29.5,-5,0.16,36.03,-0.17,-0.21,-19.22,0.33,-10.49,-19.32,-3.3,-0.2,50.21,0.23,5.32,0.48,-2.55,2,-24.06,21.89,0,0,0,14.42,-25.21,-15.27,0.32,-51.29,0.5,23.34,0.69,-12.24,0,0,0,-23.03,-7.22,-4.06,-0.31,-49.73,-0.49,-24.3,-0.29,11.32,-7.34,-2.28,-6.79,10.94,14.06,-19.13,22.0239,40.1912,9.2419,16.26,13.9,-65.62,-4.69,-27.98,-0.38,0.16,35.72,-0.17,-0.54,-20.2,0.35,-10.96,-20.28,-3.87,-0.21,51.78,0.24,5.26,0.96,-2.56,1.17,-23.69,18.64,0,0,0,11.67,-25.92,-22.75,0.33,-51.93,0.51,23.42,0.81,-12.54,0,0,0,-21.24,-8.67,1.68,-0.32,-51,-0.5,-24.43,-0.18,11.88,-7.67,-1.08,-8.66,12.79,12.55,-23.84,22.0302,40.1115,9.0939,14.14,17.01,-53.59,-4.89,-27.13,1.95,0.16,35.34,-0.17,-0.71,-21.11,0.35,-12.25,-20.83,-5.58,-0.22,53.69,0.25,4.68,0.64,-2.26,0.24,-23.25,15.43,0,0,0,8.76,-26.75,-31.35,0.33,-52.33,0.51,23.4,0.97,-12.75,0,0,0,-20.15,-9.84,6.68,-0.33,-52.45,-0.52,-24.67,-0.08,12.51,-8.51,0.27,-10.66,14.87,10.85,-29.03,22.0498,40.0369,8.9058,11.4,19.81,-41.61,-4.68,-26.48,4.36,0.16,34.82,-0.17,-0.77,-22.17,0.33,-13.12,-21.77,-6.41,-0.23,56.06,0.27,4.36,0.76,-2.11,0.54,-22.98,12.56,0,0,0,5.7,-26.98,-39.94,0.34,-52.97,0.52,23.53,1.05,-13.04,0,0,0,-20.73,-10.6,12.98,-0.35,-54.27,-0.53,-25.11,-0.04,13.29,-9.87,1.54,-12.23,16.92,9.59,-33.54,22.0744,39.9496,8.6681,8.11,21.95,-29.9,-4.44,-26.01,6.13,0.16,34.28,-0.17,-0.81,-22.97,0.32,-13.84,-22.96,-6.65,-0.25,58.67,0.29,4.33,0.85,-2.09,1.59,-22.52,10.22,0,0,0,2.96,-26.99,-47.79,0.34,-53.79,0.53,23.73,1.11,-13.4,0,0,0,-22.27,-11.46,19.61,-0.37,-56.3,-0.56,-25.6,-0.01,14.18,-11.49,2.4,-13.57,18.76,8.74,-37.44,22.1145,39.8982,8.467,4.78,23.31,-18.2,-4.76,-25.7,6.59,0.15,33.72,-0.16,-0.85,-23.28,0.32,-14.98,-24,-7.16,-0.26,60.98,0.31,4.72,0.67,-2.25,1.48,-22.12,8.1,0,0,0,2.11,-27.15,-56.18,0.35,-54.95,0.54,24,1.2,-13.92,0,0,0,-23.42,-12.18,25.79,-0.39,-58.71,-0.59,-26.19,0,15.24,-12.13,2.82,-14.75,20.44,8.37,-40.81,22.1444,39.9035,8.3134,1.43,23.89,-6.71,-5.37,-25.11,6.13,0.15,33,-0.16,-0.88,-23.37,0.32,-16.11,-24.87,-7.59,-0.28,62.98,0.33,5.41,0.6,-2.56,1.28,-21.55,5.92,0,0,0,2.49,-27.93,-64.57,0.37,-56.36,0.56,24.4,1.19,-14.53,0,0,0,-25.18,-12.91,31.83,-0.43,-61.68,-0.63,-26.85,0.01,16.59,-12.27,3,-15.56,20.9,7.83,-42.55,22.1339,39.909,8.1595,-1.79,24.01,3.73,-5.79,-24.66,5.83,0.15,32.31,-0.16,-0.91,-23.55,0.32,-17.01,-26.42,-7.45,-0.3,64.77,0.35,6,0.41,-2.8,1.34,-20.58,4.58,0,0,0,4.01,-29.8,-72.46,0.39,-58.39,0.58,25,1.1,-15.41,0,0,0,-26.95,-14.5,37.21,-0.47,-64.39,-0.68,-27.44,-0.02,17.83,-12.7,2.39,-16.17,21.06,7.61,-43.37,22.024,39.8951,8.0295,-4.92,23.79,13.3,-5.77,-24.46,6.18,0.15,31.83,-0.16,-0.93,-23.67,0.32,-17.65,-28.52,-7.29,-0.32,66.14,0.37,6.22,-0.52,-2.8,1.19,-19.8,4.42,0,0,0,6.37,-32.42,-79.82,0.42,-61,0.62,25.73,0.99,-16.56,0,0,0,-28.38,-15.53,41.38,-0.55,-68.36,-0.76,-28.27,-0.13,19.67,-12.92,1.95,-16.26,21.01,7.67,-43.26,21.8457,39.855,8.0101,-8.11,22.92,21.97,-5.28,-24.12,6.91,0.15,31.67,-0.16,-0.9,-24.52,0.3,-17.72,-30.76,-7.08,-0.32,66.75,0.38,6.06,-2.55,-2.51,1.75,-19.05,4.26,0,0,0,9.1,-35.01,-84.12,0.46,-63.92,0.67,26.59,0.71,-17.83,0,0,0,-29.93,-16.87,45.6,-0.68,-72.62,-0.9,-29.1,-0.31,21.66,-12.72,0.9,-15.72,19.59,8.44,-41.05,21.7194,39.671,7.9317,-10.47,22.1,29.49,-5.66,-24,7.07,0.15,31.75,-0.16,-0.72,-26.15,0.28,-19.17,-33.6,-8.39,-0.32,66.49,0.37,5.42,-6.03,-1.91,1.65,-19.01,5.13,0,0,0,11.89,-37.02,-86.85,0.53,-67.45,0.74,27.65,0.29,-19.36,0,0,0,-31.46,-17.36,48.75,-0.93,-77.44,-1.16,-29.89,-0.55,23.96,-12.22,0.55,-14.89,17.99,8.84,-38.55,21.5138,39.38,7.9104,-13.08,21,36.47,-5.39,-24.34,7.47,0.15,32.29,-0.16,-0.29,-28.4,0.28,-20.34,-36.77,-10.11,-0.3,64.93,0.35,4.12,-11.21,-1.07,2.53,-19.08,5.71,0,0,0,14.97,-38.74,-86.67,0.62,-70.98,0.84,28.69,-0.16,-20.92,0,0,0,-33.06,-18.57,50.94,-1.49,-82.19,-1.73,-30.51,-0.8,26.24,-11.97,-0.62,-13.7,15.74,9.8,-34.73,21.2717,39.0405,8.0445,-14.57,20.01,42.05,-5.55,-24.3,7.67,0.15,32.78,-0.16,0.41,-30.8,0.36,-21.55,-39.92,-10.47,-0.27,61.83,0.32,2.75,-16.2,-0.49,3.42,-18.49,6.6,0,0,0,17.77,-39.98,-84.07,0.76,-74.41,0.98,29.84,-0.67,-22.42,0,0,0,-35.06,-20.2,52.21,-3.43,-86.6,-3.67,-31.14,-1.16,28.34,-12.71,-2.4,-12.34,14,11.15,-30.74,21.1117,38.7274,8.3147,-15.85,18.99,47.13,-5.39,-24.2,8.08,0.15,33.18,-0.16,1.13,-32.96,0.49,-22.62,-42.74,-10.79,-0.24,56.97,0.28,1.82,-20.06,-0.24,3.32,-18.4,8.03,0,0,0,20.68,-40.22,-80.92,0.94,-77.47,1.17,30.99,-1.11,-23.76,0,0,0,-35.38,-20.47,51.97,-167.03,-89.1,-167.28,-31.73,-1.55,30.36,-12.15,-3.45,-10.98,12.12,11.91,-26.93,21.008,38.4352,8.7134,-16.89,18.24,51.33,-5.04,-24.15,8.82,0.15,33.56,-0.16,1.74,-34.78,0.65,-23.62,-45.65,-10.97,-0.2,50.78,0.24,1.3,-23.17,-0.15,2.99,-18.36,9.25,0,0,0,23.77,-39.62,-76.07,1.19,-80.2,1.43,32.02,-1.41,-24.99,0,0,0,-34.73,-20.93,51.41,-177.28,-85.72,-177.54,-32.31,-1.89,31.94,-11.6,-4.55,-9.45,10.24,12.73,-22.88,20.9963,38.2245,9.1848,-17.52,17.92,54.91,-4.94,-23.87,8.95,0.15,33.47,-0.16,2.01,-35.55,0.74,-24.44,-48.37,-10.07,-0.18,43.84,0.2,1.23,-24.42,-0.16,1.57,-18.31,10.69,0,0,0,26.81,-38.86,-71.11,1.45,-81.96,1.69,32.92,-1.55,-25.79,0,0,0,-32.91,-21.07,49.74,-178.28,-83.24,-178.54,-32.9,-2.13,33.09,-10.95,-5.19,-8.25,9,12.82,-19.81,21.0559,38.1626,9.8399,-17.98,17.29,58.34,-4.64,-22.82,8.83,0.15,32.55,-0.16,2.21,-35.68,0.79,-23.03,-50.03,-5.08,-0.16,37.42,0.18,1.34,-23.93,-0.21,0.1,-18.2,11.62,0,0,0,29.5,-37.15,-65.82,1.8,-83.52,2.04,33.66,-1.59,-26.53,0,0,0,-30.54,-20.68,47.51,-178.61,-81.6,-178.88,-33.41,-2.24,33.84,-10.21,-6.39,-7.12,7.81,13.76,-16.95,21.1956,38.1785,10.6053,-18.35,16.23,62.18,-4.25,-21.15,7.59,0.15,30.96,-0.16,2.47,-35.45,0.84,-20.73,-50.41,1.18,-0.15,33.71,0.16,1.6,-22.52,-0.28,-0.4,-18.09,11.65,0,0,0,30.75,-34.85,-59.88,2.11,-84.48,2.35,34.26,-1.54,-27,0,0,0,-29.4,-19.69,45.45,-178.84,-79.92,-179.11,-33.84,-2.29,34.64,-10.52,-7.28,-6.19,7.33,15.06,-14.99,21.3842,38.2577,11.3985,-18.42,14.98,66.13,-3.67,-19.15,5.25,0.15,29.27,-0.15,2.36,-34.7,0.78,-19.35,-49.94,4.17,-0.15,34.16,0.17,1.71,-21.23,-0.33,-1.39,-17.94,11.3,0,0,0,32.12,-32.63,-54.03,2.24,-84.79,2.48,34.71,-1.44,-27.18,0,0,0,-28.03,-17.9,42.35,-178.96,-78.77,-179.23,-34.21,-2.28,35.2,-10.32,-7.08,-5.67,7.41,15.07,-14.12,21.5486,38.2354,12.2489,-18.51,13.82,69.93,-2.38,-17.72,3.43,0.15,28.07,-0.15,2.04,-34,0.69,-18.61,-49.12,3.91,-0.16,37.3,0.18,1.64,-22.61,-0.26,-2.65,-18.37,10.98,0,0,0,33.45,-30.66,-48.65,2.04,-84.3,2.29,35.02,-1.3,-26.96,0,0,0,-26.86,-15.67,38.81,-178.96,-78.7,-179.24,-34.61,-2.18,35.25,-10.13,-6.56,-5.39,7.95,15.58,-14.12,21.6982,38.1567,13.1877,-18.95,12.24,73.2,-0.42,-17.04,1.62,0.14,27.58,-0.15,2.06,-33.63,0.68,-17.09,-48.53,3.08,-0.17,40.38,0.19,1.42,-24.76,-0.17,-3.36,-18.9,10.48,0,0,0,34.79,-28.55,-42.39,1.84,-83.66,2.08,35.23,-1.16,-26.68,0,0,0,-26.07,-13.6,34.74,-178.92,-79.14,-179.19,-35,-2.04,35.06,-9.71,-6.59,-5.24,8.7,16.53,-14.43,21.8841,38.0928,14.1571,-19.31,10.46,75.51,1.88,-16.27,0.04,0.14,27.39,-0.14,2.11,-33.42,0.69,-14.89,-47.89,2.35,-0.17,42.52,0.2,1.11,-26.64,-0.12,-2.85,-19.14,9.82,0,0,0,35.77,-26.38,-35.11,1.44,-81.88,1.68,35.29,-0.99,-25.83,0,0,0,-26.17,-12.01,30.65,-178.82,-80.07,-179.09,-35.36,-1.87,34.64,-9.5,-6.56,-4.85,9.02,16.45,-13.85,22.063,38.0408,15.1097,-19.46,9.13,76.87,4.1,-15.64,0.43,0.14,27.23,-0.14,1.96,-32.67,0.63,-12.63,-47.31,2,-0.18,44.03,0.2,0.8,-28.37,-0.1,-2.66,-19.81,10.1,0,0,0,36.57,-23.93,-28.34,1.17,-79.97,1.4,35.22,-0.85,-24.92,0,0,0,-26.31,-9.62,26.05,-178.61,-81.59,-178.88,-35.76,-1.63,33.94,-8.99,-6.39,-4.59,8.99,16.7,-13.44,22.2688,38.0244,16.0233,-19.42,8.21,77.52,5.62,-14.9,1.24,0.14,27.3,-0.14,1.91,-31.78,0.59,-10.65,-46.76,1.51,-0.18,45.1,0.21,0.57,-29.65,-0.1,-3.18,-20.81,10.97,0,0,0,37.92,-21.24,-22.24,1.01,-78.42,1.24,35.1,-0.76,-24.17,0,0,0,-26.05,-6.28,21,-178.23,-83.42,-178.49,-36.12,-1.37,33.1,-8.11,-6.23,-4.49,9.07,17.08,-13.38,22.4867,38.064,16.9091,-19.47,7.56,78.07,6.9,-14.7,3.38,0.15,27.98,-0.15,1.61,-30.53,0.51,-9.02,-46.16,0.8,-0.18,45.64,0.21,0.44,-30.55,-0.1,-3.72,-20.89,11,0,0,0,39.85,-19.26,-15.19,0.83,-75.89,1.06,34.88,-0.62,-22.97,0,0,0,-26.44,-4.79,15.88,-176.56,-86.61,-176.82,-36.42,-1.05,31.58,-7.48,-7.06,-4.34,9.54,17.54,-13.15,22.6807,38.1492,17.7339,-19.69,6.88,78.67,8,-15.23,4.34,0.15,29.62,-0.15,1.08,-28.78,0.41,-7.4,-45.41,0.19,-0.18,45.39,0.21,0.34,-31.04,-0.11,-3.6,-21.26,10.87,0,0,0,41.61,-16.94,-9.07,0.67,-72.4,0.89,34.41,-0.46,-21.31,0,0,0,-27.25,-3.28,10.36,-37.17,-89.66,-37.42,-36.59,-0.73,29.84,-7.33,-7.53,-4.16,9.97,17.89,-12.95,22.8953,38.3277,18.5113,-19.75,5.63,79.27,9.45,-16.35,4.6,0.15,32.47,-0.16,0.57,-27.37,0.34,-5.5,-43.87,-0.77,-0.18,44.23,0.2,0.35,-31,-0.12,-2.98,-21.52,10.84,0,0,0,43.55,-14.94,-3.92,0.55,-68.42,0.77,33.73,-0.32,-19.43,0,0,0,-28.5,-1.18,4.79,-2.76,-85.77,-3,-36.61,-0.4,27.95,-6.9,-7.66,-4.05,9.94,18.04,-12.71,23.1065,38.5377,19.278,-19.8,4.41,79.65,10.87,-18.31,5.14,0.16,36.49,-0.17,-0.37,-25.37,0.29,-3.26,-42.12,-0.87,-0.17,42.47,0.2,0.37,-30.72,-0.13,-2.2,-21.47,11.37,0,0,0,45.71,-13.44,0.27,0.47,-64.42,0.68,32.9,-0.2,-17.59,0,0,0,-30.24,1,-0.34,-1.44,-81.88,-1.68,-36.41,-0.16,26.08,-6.49,-8.06,-4.15,9.88,18.15,-12.74,23.297,38.7691,19.952,-19.45,3.28,79.96,11.95,-20.61,4.37,0.17,41.32,-0.19,-2,-22.12,0.37,-1.09,-40.07,-0.71,-0.17,40.5,0.19,0.42,-30.04,-0.14,-0.63,-20.25,11.5,0,0,0,47.11,-11.58,4.4,0.41,-60.65,0.61,31.95,-0.12,-15.89,0,0,0,-33.58,2.28,-4.46,-0.95,-77.65,-1.18,-36.11,0.14,24.06,-7.11,-9.07,-4.08,9.81,18.39,-12.35,23.5309,38.9767,20.4916,-18.7,2.65,80.46,11.72,-22.88,2.41,0.19,46.28,-0.21,-3.2,-19.13,0.59,0.15,-37.68,-0.58,-0.16,38.73,0.18,0.44,-29.7,-0.15,0.24,-19.28,11.85,0,0,0,48.71,-9.45,6.69,0.38,-57.57,0.57,31.09,-0.07,-14.53,0,0,0,-36.29,3.66,-9.44,-0.66,-72.1,-0.88,-35.37,0.4,21.42,-7.84,-8.89,-4.05,10,18.37,-12.45,23.756,39.1287,20.9569,-18.26,2,80.96,11.07,-25.47,0.65,0.2,51.01,-0.24,-3.91,-16.72,0.83,1.14,-35.76,-0.84,-0.16,37.09,0.18,0.44,-29.6,-0.16,0.1,-18.62,12.05,0,0,0,50.93,-9.4,10.8,0.33,-52.61,0.52,29.45,-0.06,-12.4,0,0,0,-38.15,4.9,-13.66,-0.51,-66.38,-0.72,-34.32,0.61,18.74,-7.11,-8.84,-4.18,10,19.14,-12.85,23.9996,39.2795,21.3769,-18.03,1.56,81.13,10.04,-28.08,-0.46,0.22,55.04,-0.26,-4.53,-14.31,1.12,1.59,-34.2,-1.97,-0.16,35.51,0.17,0.52,-29.57,-0.16,0.59,-18.85,12.56,0,0,0,52.54,-8.68,14.2,0.31,-48.34,0.48,27.81,-0.09,-10.66,0,0,0,-40.65,6.08,-17.24,-0.42,-61.19,-0.62,-33.1,0.74,16.36,-6.45,-7.89,-3.97,9.96,20.14,-12.87,24.249,39.3907,21.781,-17.91,1.18,80.62,9.26,-30.21,-0.27,0.24,58.05,-0.28,-4.81,-13.16,1.28,2.11,-32.72,-3.39,-0.15,33.94,0.16,0.6,-30.01,-0.16,1.09,-19.38,13.62,0,0,0,54.25,-7.98,17.66,0.29,-44.73,0.45,26.17,-0.19,-9.25,0,0,0,-42.79,7.03,-20.94,-0.37,-56.45,-0.56,-31.74,0.76,14.25,-5.45,-6.64,-3.8,9.7,20.68,-12.77,24.4782,39.4721,22.1146,-17.6,1.69,79.26,7.8,-31.57,0.83,0.25,59.69,-0.3,-5,-12.96,1.33,2.01,-31.69,-4.03,-0.15,32.95,0.16,0.71,-30.44,-0.14,1.89,-19.39,15.71,0,0,0,55.18,-7.43,21.1,0.27,-41.52,0.43,24.51,-0.3,-8.06,0,0,0,-45.94,7.41,-24.56,-0.32,-51.12,-0.5,-30,0.78,11.99,-5.59,-5.26,-3.76,9.57,20.67,-13.01,24.6045,39.4789,22.4041,-17.39,2.54,77.73,6.57,-32.87,2.59,0.26,60.09,-0.3,-4.54,-14.09,1.14,1.73,-31.59,-4.19,-0.15,33.03,0.16,0.84,-30.65,-0.13,1.76,-19.43,17.95,0,0,0,56.8,-7.05,23.87,0.26,-38.8,0.41,22.89,-0.4,-7.11,0,0,0,-48.26,7.61,-28.58,-0.3,-46.77,-0.47,-28.33,0.7,10.21,-5.63,-4.51,-3.84,10.01,20.9,-13.64,24.7111,39.3893,22.6047,-16.88,3.83,76.76,4.96,-33.78,3.96,0.25,59.29,-0.29,-3.12,-17.13,0.69,0.74,-31.91,-4.09,-0.16,34.34,0.17,0.91,-31.23,-0.1,0.17,-19.42,18.98,0,0,0,59.53,-6.17,25.7,0.25,-36.08,0.4,21.18,-0.45,-6.23,0,0,0,-49.67,7.18,-32.69,-0.28,-43.13,-0.44,-26.63,0.47,8.78,-4.74,-4.11,-3.94,10,21.18,-13.84,24.862,39.1769,22.784,-16.29,4.54,76.59,3.81,-34.35,4.52,0.24,57.71,-0.28,-1.81,-20.55,0.4,-0.19,-32.05,-4.68,-0.16,36.08,0.17,0.95,-32.62,-0.06,-0.29,-19.43,20.01,0,0,0,61.54,-5.85,26.12,0.24,-33.21,0.38,19.45,-0.44,-5.36,0,0,0,-51.96,7.93,-35.33,-0.27,-40.07,-0.42,-24.95,0.2,7.63,-4.97,-2.8,-4.04,10.8,21.07,-14.84,25.0501,38.9849,22.9234,-16.06,4.56,77.78,3.11,-35.2,4.1,0.23,55.61,-0.27,-1.07,-23.1,0.3,-0.89,-31.95,-6.12,-0.16,37.53,0.18,0.91,-34.29,-0.02,-0.09,-19.17,19.64,0,0,0,62.97,-6.22,27.05,0.23,-30.07,0.37,17.53,-0.39,-4.48,0,0,0,-54.84,8.44,-36.66,-0.26,-37.58,-0.41,-23.25,-0.11,6.73,-5.25,-1.85,-4.15,11.32,21.3,-15.71,25.2661,38.8408,23.0518,-16.34,4.05,79.68,2.91,-36.35,3.33,0.21,53.25,-0.25,-0.6,-25.28,0.27,-1.02,-31.9,-7.55,-0.16,38.39,0.18,0.75,-35.33,-0.03,-0.01,-19.2,18.56,0,0,0,64.82,-7.49,30.16,0.23,-26.75,0.35,15.3,-0.26,-3.65,0,0,0,-57,8.71,-38.03,-0.25,-35.3,-0.4,-21.39,-0.35,5.98,-5.04,-1.44,-4.52,11.88,21.94,-16.9,25.448,38.7616,23.2618,-17.14,2.02,82.01,4.65,-37.96,2.93,0.21,51.5,-0.24,-0.27,-27.07,0.27,0.73,-31.67,-8.41,-0.16,38.35,0.18,0.48,-35.81,-0.09,1.36,-20.18,17.08,0,0,0,66.08,-7.88,31.57,0.23,-25.71,0.35,14.44,-0.16,-3.43,0,0,0,-58.56,9.86,-37.79,-0.24,-33.25,-0.38,-19.67,-0.43,5.36,-4.6,-0.5,-4.85,12.54,22.42,-18.14,25.6208,38.697,23.4515,-17.79,-0.22,84.96,6.68,-39.72,3.26,0.2,50.64,-0.23,-0.24,-27.76,0.27,2.57,-31.2,-9.06,-0.16,37.88,0.18,-0.01,-36.44,-0.2,2.56,-20.77,14.75,0,0,0,67.19,-8.18,32.27,0.23,-25.64,0.35,14.32,-0.13,-3.42,0,0,0,-60,10.97,-36.84,-0.24,-31.51,-0.38,-18.28,-0.4,4.88,-4.16,-0.06,-5.25,13.04,22.44,-19.21,25.8587,38.5874,23.5835,-17.92,-2.19,88.07,8.29,-41.18,3.8,0.2,50.33,-0.23,-0.31,-28.24,0.26,3.58,-30.36,-10.69,-0.16,37.24,0.18,-0.33,-36.97,-0.28,3.87,-21.15,12.22,0,0,0,67.67,-8.29,32.45,0.23,-25.83,0.35,14.35,-0.11,-3.47,0,0,0,-61.59,11.79,-36.8,-0.23,-29.88,-0.37,-17.12,-0.34,4.45,-4.1,0.51,-5.59,13.39,22.02,-20.15,26.142,38.4649,23.7013,-17.97,-4.7,91.12,10.28,-42.86,3.72,0.2,50.28,-0.23,-0.49,-29.2,0.24,4.71,-29.29,-13,-0.16,36.34,0.17,-0.47,-37.78,-0.32,5.85,-21.54,10.3,0,0,0,67.68,-9.17,32.51,0.23,-25.96,0.35,14.35,-0.09,-3.51,0,0,0,-62.53,13.09,-36.97,-0.23,-29.44,-0.37,-16.83,-0.32,4.34,-4.02,1.19,-6.18,13.42,21.68,-21.38,26.3963,38.2861,23.6894,-18.18,-6.26,93.02,11.32,-44.09,3.62,0.2,49.88,-0.23,-0.76,-31.37,0.18,5.21,-28.76,-14.38,-0.16,35.84,0.17,-0.58,-38.72,-0.36,7.67,-22.2,10,0,0,0,67.28,-10.16,31.27,0.23,-26.02,0.35,14.32,-0.07,-3.53,0,0,0,-63.42,14.19,-37.91,-0.23,-29.55,-0.37,-16.86,-0.32,4.37,-4.38,2.36,-6.57,13.9,21.09,-22.8,26.6871,38.1902,23.5277,-18.12,-6.17,93.91,10.52,-44.19,2.97,0.19,48.54,-0.22,-1.38,-33.13,0.05,4.57,-28.34,-14.67,-0.16,36.23,0.17,-0.81,-39.41,-0.43,8.11,-22.07,10.13,0,0,0,66.97,-10.7,30.45,0.23,-25.92,0.35,14.17,-0.02,-3.51,0,0,0,-63.89,14.41,-39.19,-0.23,-29.61,-0.37,-16.81,-0.31,4.39,-4.89,3.03,-6.74,14.28,20.76,-23.68,27.0199,38.1945,23.2486,-17.63,-5.09,94.51,8.32,-43.3,1.97,0.19,46.5,-0.21,-2.37,-34.33,-0.17,3.6,-27.95,-13.19,-0.16,37.5,0.18,-1.46,-39.54,-0.62,6.7,-21.72,9.26,0,0,0,67.38,-10.12,29.51,0.23,-26.41,0.35,14.45,-0.04,-3.63,0,0,0,-63.19,14.12,-40.13,-0.23,-29.93,-0.37,-16.87,-0.29,4.49,-4.15,3.81,-6.77,14.09,20.67,-23.64,27.3237,38.173,22.8893,-17.15,-4.02,95.14,6.26,-42.48,2.27,0.18,44.96,-0.21,-3.16,-33.94,-0.3,2.68,-27.84,-11.86,-0.17,39.27,0.18,-2.18,-39.6,-0.82,5.19,-21.44,8.63,0,0,0,68.19,-10.54,29.58,0.23,-26.61,0.35,14.52,-0.03,-3.68,0,0,0,-62.26,14.59,-40.23,-0.24,-31.18,-0.37,-17.4,-0.28,4.84,-4.19,5.17,-6.6,14.65,19.92,-24.11,27.6029,38.1876,22.4047,-16.49,-1.93,95.74,2.34,-41.14,1.44,0.18,44.19,-0.2,-2.66,-31.22,-0.07,0.18,-27.78,-11.12,-0.17,41.79,0.19,-2.86,-39.94,-1.03,2.97,-20.58,7.82,0,0,0,68.87,-11,30.76,0.23,-26.69,0.35,14.45,0.01,-3.71,0,0,0,-61.87,15.19,-39.14,-0.24,-33.07,-0.38,-18.2,-0.28,5.4,-5.03,6.29,-6.43,15.05,19.16,-24.63,27.8734,38.149,21.7721,-15.77,1.63,95.59,-2.59,-38.99,0.84,0.18,43.27,-0.2,-2.14,-29.29,0.08,-3.81,-28.4,-9.72,-0.18,45.69,0.21,-3.34,-39.89,-1.15,-0.98,-19.23,7.21,0,0,0,70.22,-10.68,30.67,0.23,-27.18,0.36,14.73,0,-3.83,0,0,0,-61.37,14.68,-39.52,-0.25,-34.43,-0.39,-18.63,-0.23,5.82,-5.45,7.16,-6.07,15.67,18.43,-24.76,28.1257,38.1117,21.2546,-15.18,5.03,95.15,-6.01,-36.92,2.33,0.17,41.98,-0.19,-2.11,-28.7,0.11,-7.54,-29.69,-8.21,-0.2,49.78,0.23,-3.31,-38.54,-1.04,-4.64,-17.91,6.41,0,0,0,71.48,-10.06,31.48,0.23,-27.8,0.36,15,0.01,-4,0,0,0,-60.89,13.97,-38.32,-0.25,-36.96,-0.4,-19.61,-0.21,6.64,-5.59,7.57,-5.52,16.01,18.11,-24.18,28.3897,38.1114,20.9591,-14.52,7.48,94.06,-7.42,-35.06,5.11,0.17,40.86,-0.19,-2.17,-28.28,0.12,-9.01,-31.17,-4.64,-0.21,51.38,0.24,-3.2,-38.53,-1,-7.38,-17.02,6.32,0,0,0,72.21,-9.4,31.76,0.23,-28.99,0.36,15.62,-0.02,-4.3,0,0,0,-59.4,13.99,-36.01,-0.27,-41.16,-0.43,-21.3,-0.24,8.07,-5.48,8.08,-5.07,16.26,17.84,-23.67,28.6441,38.1904,20.8512,-13.97,7.59,93.31,-7.07,-33.92,6.38,0.17,40.55,-0.19,-2.1,-28,0.14,-7.08,-32.02,0.05,-0.2,50.19,0.23,-3.65,-39.81,-1.22,-7.73,-15.76,5.63,0,0,0,72.23,-8.82,32.96,0.23,-30.06,0.37,16.15,-0.03,-4.59,0,0,0,-57.9,13.22,-34.64,-0.29,-44.65,-0.45,-22.52,-0.23,9.35,-5.38,7.44,-4.91,16.16,17.81,-23.01,28.7943,38.2202,20.801,-13.87,6.86,92.98,-6.73,-33.87,5.67,0.17,40.98,-0.19,-1.96,-27.9,0.15,-5.66,-31.88,1.48,-0.19,48.82,0.22,-3.47,-39.03,-1.12,-6.31,-15.27,4.67,0,0,0,71.11,-8.29,34.37,0.24,-30.46,0.37,16.27,0,-4.71,0,0,0,-58.04,12.31,-32.68,-0.3,-46.69,-0.47,-23.17,-0.21,10.14,-5.91,6.92,-4.65,15.87,17.97,-22.31,28.8848,38.2275,20.7963,-13.46,5.95,92.9,-6.19,-33.77,4.51,0.17,41.51,-0.19,-1.8,-27.61,0.17,-5.86,-31.03,-0.98,-0.19,47.84,0.22,-2.75,-38.65,-0.91,-4.74,-14.94,3.77,0,0,0,70.18,-7.62,34.22,0.24,-30.69,0.37,16.39,-0.01,-4.77,0,0,0,-58.38,11.83,-31.16,-0.3,-48.04,-0.48,-23.58,-0.2,10.67,-5.98,6.77,-4.73,14.71,17.32,-21.45,28.9212,38.2983,20.8526,-13.07,5.4,91.84,-5.24,-33.32,4.83,0.17,41.39,-0.19,-1.75,-27.74,0.17,-5.98,-30.61,-2.91,-0.19,47.08,0.22,-1.91,-38.05,-0.66,-3.38,-14.11,3.78,0,0,0,69.57,-7.35,34.14,0.24,-30.47,0.37,16.29,-0.01,-4.71,0,0,0,-58.57,10.79,-30.72,-0.31,-48.85,-0.48,-23.82,-0.2,11,-5.81,5.73,-4.89,13.53,16.69,-20.38,28.8914,38.392,20.9495,-12.97,5.68,90.38,-4.94,-32.76,5.32,0.17,40.66,-0.19,-1.76,-28.18,0.16,-5.83,-30.86,-2.89,-0.19,46.73,0.21,-1.35,-36.94,-0.48,-2.97,-13.59,4.11,0,0,0,69.27,-7.1,34.39,0.23,-29.81,0.37,15.93,0.02,-4.53,0,0,0,-58.76,9.97,-29.78,-0.31,-49.31,-0.49,-24.03,-0.23,11.17,-5.97,4.92,-4.68,13.54,16.19,-19.7,28.8126,38.4839,21.0772,-12.95,5.7,89.33,-4.37,-32.47,5.73,0.17,40.2,-0.19,-1.74,-28.43,0.15,-4.82,-30.91,-1.47,-0.19,46.24,0.21,-1.31,-36.51,-0.46,-2.79,-13.09,4.43,0,0,0,69.34,-7.44,34.28,0.23,-29.38,0.37,15.73,0.02,-4.42,0,0,0,-58.5,9.5,-29.43,-0.31,-49.04,-0.49,-23.96,-0.23,11.06,-5.91,4.07,-4.72,13.76,15.72,-19.54,28.6925,38.4975,21.2151,-13.19,4.67,89.04,-3.13,-33.01,5.5,0.17,40.48,-0.19,-1.65,-28.35,0.16,-3.01,-30.83,-0.28,-0.18,45.34,0.21,-1.43,-36.34,-0.49,-1.78,-13,4.24,0,0,0,69.34,-7.78,33.76,0.23,-29.13,0.36,15.59,0.03,-4.35,0,0,0,-58.46,9.46,-29.08,-0.3,-48.07,-0.48,-23.6,-0.21,10.68,-5.59,3.47,-4.76,13.58,15.31,-19.16,28.5611,38.5198,21.3083,-13.64,3.38,88.98,-1.95,-33.87,4.79,0.17,40.81,-0.19,-1.59,-28.4,0.16,-1.91,-31.06,-1.01,-0.18,44.42,0.2,-1.25,-36.06,-0.45,-0.4,-12.92,4.31,0,0,0,69.15,-8.35,32.88,0.23,-29.02,0.36,15.5,0.04,-4.33,0,0,0,-58.75,9.8,-29.17,-0.3,-46.77,-0.47,-23.15,-0.2,10.18,-5.33,2.59,-4.94,13.32,14.98,-18.93,28.4278,38.568,21.3236,-13.9,3.26,88.42,-1.91,-34.02,4.44,0.17,40.45,-0.19,-1.54,-28.83,0.16,-2.24,-31.49,-2.26,-0.18,43.97,0.2,-0.89,-35.8,-0.36,0.18,-12.61,4.34,0,0,0,68.41,-8.23,32.63,0.23,-29.1,0.36,15.5,0.06,-4.35,0,0,0,-59.12,9.16,-29.24,-0.29,-45.25,-0.46,-22.65,-0.2,9.59,-5.63,1.47,-5.1,13.31,15.02,-18.89,28.2801,38.6196,21.3633,-14.15,4.01,87.52,-2.46,-33.94,4.17,0.17,39.58,-0.18,-1.46,-29.13,0.16,-2.78,-32.22,-2.22,-0.18,43.97,0.2,-0.63,-35.41,-0.3,-0.53,-12.43,4.69,0,0,0,68.22,-7.93,32.74,0.23,-28.86,0.36,15.27,0.12,-4.3,0,0,0,-58.74,8.36,-29.7,-0.28,-43.67,-0.45,-22.08,-0.19,9,-5.53,0.13,-5.27,13.31,15.53,-18.79,28.1109,38.6731,21.4354,-14.72,4.85,87.05,-2.83,-34.3,4.68,0.16,38.95,-0.18,-1.47,-29.37,0.15,-2.86,-33.1,-1.03,-0.18,43.92,0.2,-0.74,-35.52,-0.33,-1.33,-12.6,4.6,0,0,0,68.11,-7.76,32.76,0.23,-28.19,0.36,14.87,0.17,-4.13,0,0,0,-58.6,7.8,-30.09,-0.27,-41.92,-0.43,-21.38,-0.16,8.37,-5.56,-1.18,-5.28,13.15,15.81,-18.31,27.9165,38.68,21.5743,-15.81,3.93,86.81,-1.53,-35.76,4.69,0.17,39.33,-0.18,-1.39,-29.27,0.16,-1.05,-33.96,0.22,-0.18,43.14,0.2,-0.9,-35.51,-0.37,-0.77,-13.76,4.87,0,0,0,68.11,-8.05,31.77,0.23,-27.8,0.36,14.71,0.15,-4.03,0,0,0,-58.22,8.3,-30.5,-0.26,-39.83,-0.42,-20.53,-0.13,7.63,-5.23,-1.95,-5.46,13.03,16.26,-18.34,27.7738,38.7097,21.6979,-16.71,2.32,86.28,0.06,-37.19,3.36,0.17,40.04,-0.19,-1.22,-29.19,0.18,0.89,-34.42,0.2,-0.17,41.95,0.19,-0.72,-35.15,-0.33,1.3,-14.24,6.03,0,0,0,67.25,-9.43,32.45,0.23,-26.96,0.35,14.21,0.2,-3.82,0,0,0,-58.82,9,-31.25,-0.26,-37.52,-0.41,-19.6,-0.12,6.85,-5.7,-3.04,-5.78,12.73,16.09,-18.43,27.6609,38.7598,21.698,-17.08,2.27,85.54,0.05,-37.63,2.51,0.17,39.94,-0.19,-1.11,-29.27,0.19,0.89,-34.93,-0.21,-0.17,41.45,0.19,-0.38,-34.54,-0.26,1.68,-14.16,6.87,0,0,0,66.16,-9.87,32.2,0.23,-26.62,0.35,14.01,0.22,-3.74,0,0,0,-59.01,8.82,-32.12,-0.25,-35.26,-0.4,-18.69,-0.13,6.12,-5.68,-4.3,-5.97,12.31,15.97,-18.1,27.5613,38.7806,21.7396,-17.18,3.24,84.9,-0.71,-37.43,2.53,0.17,39.23,-0.18,-1.05,-29.4,0.19,0.11,-35.55,-0.41,-0.17,41.61,0.19,-0.18,-34.05,-0.21,0.72,-13.72,7.14,0,0,0,65.27,-9.88,31.77,0.23,-25.84,0.35,13.55,0.27,-3.55,0,0,0,-58.63,7.81,-33.24,-0.24,-33.01,-0.38,-17.7,-0.12,5.42,-5.51,-5.82,-6.1,12.05,16.27,-17.75,27.5089,38.8255,21.8695,-17.51,3.65,84.79,-0.66,-37.47,3.13,0.16,38.69,-0.18,-1.04,-29.23,0.2,0.02,-35.9,-0.35,-0.17,41.47,0.19,-0.09,-33.87,-0.2,-0.04,-13.91,6.65,0,0,0,64.51,-9.78,31.29,0.22,-24.71,0.35,12.9,0.31,-3.29,0,0,0,-57.73,6.73,-34.19,-0.24,-30.73,-0.37,-16.58,-0.08,4.77,-5.33,-6.55,-6.19,12.2,16,-17.7,27.493,38.8904,22.0353,-17.83,2.87,84.71,0.32,-37.7,2.89,0.16,38.67,-0.18,-0.95,-28.61,0.22,1.08,-35.67,-0.42,-0.17,40.6,0.19,0,-33.54,-0.19,0.62,-14.38,6.56,0,0,0,62.55,-9.74,28.61,0.22,-24.58,0.34,12.97,0.24,-3.25,0,0,0,-57.11,7.02,-32.49,-0.23,-29.06,-0.36,-15.8,-0.08,4.31,-5.8,-6.73,-6.25,12.85,15.59,-18.01,27.4537,38.967,22.1202,-18.22,2.16,84.15,0.69,-37.98,1.11,0.16,38.64,-0.18,-0.77,-28.4,0.24,2.23,-35.61,0.09,-0.17,39.63,0.18,0.09,-32.94,-0.17,1.47,-14.56,7.55,0,0,0,59.23,-11.08,26.58,0.22,-24.47,0.34,12.98,0.2,-3.21,0,0,0,-56.35,7.98,-30.03,-0.23,-27.67,-0.36,-15.18,-0.09,3.94,-6,-7.25,-6.58,12.51,15.19,-18.21,27.4298,39.0193,22.0888,-18.42,2.73,83.24,0.04,-37.86,0.29,0.16,38.13,-0.18,-0.66,-28.32,0.25,1.96,-35.9,0.35,-0.17,39.18,0.18,0.22,-32.31,-0.16,1.01,-14.43,8.74,0,0,0,54.92,-12.12,24.15,0.22,-24.15,0.34,12.73,0.25,-3.15,0,0,0,-54.56,8.3,-28.44,-0.23,-26.65,-0.35,-14.66,-0.08,3.68,-6.17,-8.34,-6.95,12,14.98,-18.25,27.4069,39.0765,22.0586,-18.67,3.47,82.74,-0.38,-37.83,0.63,0.16,37.39,-0.18,-0.66,-27.92,0.25,1.52,-36.26,0.67,-0.16,38.88,0.18,0.3,-31.85,-0.15,-0.03,-14.55,8.86,0,0,0,50.08,-11.49,19.49,0.22,-23.83,0.34,12.57,0.25,-3.07,0,0,0,-51.38,8.05,-25.73,-0.23,-25.5,-0.35,-14.09,-0.08,3.4,-6.41,-9.28,-7.04,12.05,14.94,-18.11,27.4224,39.1507,22.0999,-18.83,3.44,82.77,-0.17,-37.65,0.92,0.16,36.83,-0.17,-0.69,-27.72,0.25,1.78,-36.07,1.25,-0.16,38.36,0.18,0.27,-31.78,-0.16,-0.54,-14.41,8.18,0,0,0,44.25,-10.95,15.33,0.22,-22.84,0.34,12.08,0.24,-2.85,0,0,0,-46.93,7.07,-22.61,-0.22,-24.36,-0.34,-13.52,-0.07,3.13,-6.57,-10.26,-7.09,12.01,14.8,-17.81,27.4059,39.1853,22.1048,-19.11,3.23,82.87,-0.16,-37.82,0.37,0.16,36.58,-0.17,-0.67,-27.52,0.26,2.03,-36.05,1.4,-0.16,37.86,0.18,0.25,-31.84,-0.17,-0.72,-14.33,7.53,0,0,0,37.04,-10.99,13.53,0.22,-21.47,0.33,11.31,0.28,-2.57,0,0,0,-41.34,5.67,-19.53,-0.22,-23.45,-0.34,-13.12,-0.09,2.92,-6.75,-11.4,-7.2,11.94,14.87,-17.59,27.3798,39.1916,22.0812,-19.36,3.27,82.49,-0.07,-38.02,0.6,0.16,36.49,-0.17,-0.65,-27.56,0.26,2.24,-36.29,1.84,-0.16,37.65,0.18,0.26,-31.77,-0.17,-1.14,-14.27,7.75,0,0,0,28.69,-11,11.22,0.22,-20.78,0.33,11.08,0.21,-2.41,0,0,0,-34.42,4.36,-17.43,-0.22,-22.83,-0.34,-12.93,-0.13,2.77,-6.31,-12.46,-7.3,11.14,14.75,-17.16,27.3284,39.1945,22.0499,-19.4,3.61,81.68,0.37,-38.04,2.15,0.16,36.33,-0.17,-0.68,-27.53,0.26,2.54,-36.64,2.97,-0.16,37.78,0.18,0.33,-31.42,-0.16,-1.73,-14.05,8.37,0,0,0,19.39,-10.48,8.95,0.22,-20.18,0.33,11.04,0.07,-2.27,0,0,0,-26.39,2.91,-16.14,-0.22,-22.52,-0.34,-12.95,-0.19,2.69,-6.14,-13.26,-7.3,10.97,14.64,-16.85,27.2779,39.1985,21.9557,-19.3,4.49,81.12,-0.29,-37.92,2.65,0.16,35.98,-0.17,-0.67,-27.44,0.26,1.81,-37.07,3.16,-0.16,38.12,0.18,0.41,-31.12,-0.15,-2.41,-13.22,8.19,0,0,0,9.59,-10.8,7.96,0.21,-17.89,0.32,10.12,-0.04,-1.82,0,0,0,-18.47,0.51,-13.18,-0.22,-22.13,-0.33,-13.13,-0.27,2.58,-6.44,-14.6,-7.2,10.62,14.57,-16.07,27.2434,39.2111,21.9123,-19.04,4.68,81.56,-0.81,-37.65,2.37,0.16,35.66,-0.17,-0.7,-27.14,0.26,1.36,-36.88,3.04,-0.16,38.2,0.18,0.37,-31.18,-0.15,-2.93,-11.81,6.99,0,0,0,0.67,-11.8,5.78,0.21,-15.3,0.31,8.86,-0.09,-1.39,0,0,0,-10.08,-2.69,-10.61,-0.22,-21.22,-0.33,-12.99,-0.32,2.37,-6.54,-16.28,-7.07,10.57,14.2,-15.19,27.202,39.2476,21.9007,-18.87,4.28,82.39,-0.99,-37.55,1.32,0.16,35.51,-0.17,-0.72,-26.74,0.27,1.42,-36.48,2.81,-0.16,38,0.18,0.28,-31.34,-0.16,-3.08,-10.38,5.48,0,0,0,-7.42,-12.07,-2.62,0.21,-15.15,0.31,9.2,-0.21,-1.34,0,0,0,-1.88,-6,-6.46,-0.22,-20.17,-0.33,-12.76,-0.34,2.15,-6.2,-17.91,-6.8,10.19,13.74,-14.07,27.0792,39.2518,21.8874,-19.16,4.09,82.58,-0.86,-38,1.18,0.16,35.5,-0.17,-0.72,-26.6,0.27,1.54,-36.81,2.64,-0.16,37.89,0.18,0.3,-31.26,-0.16,-3.32,-9.3,4.95,0,0,0,-13.95,-13.3,-15.16,0.21,-15.52,0.31,10.06,-0.31,-1.36,0,0,0,5.43,-9.44,0.82,-0.22,-20.02,-0.33,-13.25,-0.33,2.1,-5.28,-19.73,-6.21,9.16,13.34,-12.39,26.8773,39.2463,21.8566,-19.77,4.53,81.43,-0.39,-38.89,2.52,0.16,35.56,-0.17,-0.72,-26.49,0.27,1.65,-38.04,3.03,-0.16,37.97,0.18,0.47,-30.66,-0.14,-3.44,-9,6.19,0,0,0,-18.93,-15.87,-30.92,0.21,-15.31,0.31,10.56,-0.31,-1.3,0,0,0,10.78,-12.95,11.45,-0.22,-20.59,-0.33,-14.22,-0.23,2.19,-4.91,-21.14,-5.54,8.51,13.49,-10.77]

HAnimHumanoid25.motions.append(HAnimMotion244)

Scene21.children.append(HAnimHumanoid25)

X3D0.Scene = Scene21
f = open("././KoreanCharacterMotionAnnexD01Jin_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
