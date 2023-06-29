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
meta3.content = "WinterAndSpringTest.x3d"

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.name = "description"
meta4.content = "3D Male Scan combined with JoeKick, 3 Korean characters Ru,Mi,Min from HAnim, CCBYSA music plus designs from Rhino. MaleScan modified in Cinema4D for articulation and translations, geometric values from Rhino, txt file for centers. Models vary. HAnim version 2 LOA-3 Humanoids with textured skin, 3 Korean characters, plus scan. Math for lines and intersections."

head1.children.append(meta4)
meta5 = x3d.meta()
meta5.name = "creator"
meta5.content = "Carol McDonald, Katy Schildmeyer, Joe D. Williams and Don Brutzman"

head1.children.append(meta5)
meta6 = x3d.meta()
meta6.name = "created"
meta6.content = "May through September 2023"

head1.children.append(meta6)
meta7 = x3d.meta()
meta7.name = "modified"
meta7.content = "2 June 2023"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.name = "reference"
meta8.content = "https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Characters/KoreanCharacter09Ru.x3d"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "reference"
meta9.content = "https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Characters/KoreanCharacter10Mi.x3d"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "reference"
meta10.content = "https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Characters/KoreanCharacter11Min.x3d"

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.name = "identifier"
meta11.content = "https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Characters/WinterAndSpringTest.x3d"

head1.children.append(meta11)
meta12 = x3d.meta()
meta12.name = "license"
meta12.content = "../license.html"

head1.children.append(meta12)

X3D0.head = head1
Scene13 = x3d.Scene()
WorldInfo14 = x3d.WorldInfo()
WorldInfo14.info = ["X3D Humanoid LOA3 skeleton plus others","Lots points"]
WorldInfo14.title = "X3D HANIM LOA3 (modified) Skeleton, Lots points Skin, texcoords, Displacer, translations"

Scene13.children.append(WorldInfo14)
NavigationInfo15 = x3d.NavigationInfo()
NavigationInfo15.DEF = "Start_NavigationInfo"
NavigationInfo15.headlight = False

Scene13.children.append(NavigationInfo15)
Viewpoint16 = x3d.Viewpoint()
Viewpoint16.centerOfRotation = [0,1,0]
Viewpoint16.description = "Male"
Viewpoint16.position = [0,1,-2]

Scene13.children.append(Viewpoint16)
Background17 = x3d.Background()
Background17.DEF = "gray_Background"

Scene13.children.append(Background17)
Background18 = x3d.Background()
Background18.DEF = "dark_gray_Background"

Scene13.children.append(Background18)
Background19 = x3d.Background()
Background19.DEF = "black_Background"

Scene13.children.append(Background19)
Background20 = x3d.Background()
Background20.DEF = "blue_Background"

Scene13.children.append(Background20)
SpotLight21 = x3d.SpotLight()
SpotLight21.DEF = "light1"
SpotLight21.ambientIntensity = 0.7
SpotLight21.beamWidth = 1.5
SpotLight21.color = [0.8,0.8,1]
SpotLight21.cutOffAngle = 0.6
SpotLight21.direction = [0,0,0]
SpotLight21.location = [0,3,3]
SpotLight21.radius = 10

Scene13.children.append(SpotLight21)
PointLight22 = x3d.PointLight()
PointLight22.DEF = "light2"
PointLight22.ambientIntensity = 0.7
PointLight22.color = [0.8,0.8,1]
PointLight22.location = [0,10,-7]

Scene13.children.append(PointLight22)
#External from the Humanoid viewpoints
Viewpoint23 = x3d.Viewpoint()
Viewpoint23.DEF = "Scene_InclinedView"
Viewpoint23.centerOfRotation = [0,0.85,0]
Viewpoint23.description = "Scene_Inclined View"
Viewpoint23.orientation = [-0.113,0.993,0.0347,0.671]
Viewpoint23.position = [1.62,1.05,3.06]

Scene13.children.append(Viewpoint23)
Viewpoint24 = x3d.Viewpoint()
Viewpoint24.DEF = "Scene_IFrontView"
Viewpoint24.centerOfRotation = [0,0.8,0]
Viewpoint24.description = "Scene_Front View"
Viewpoint24.position = [0,0.8,2.58]

Scene13.children.append(Viewpoint24)
Viewpoint25 = x3d.Viewpoint()
Viewpoint25.DEF = "Scene_OldMan_ISideView"
Viewpoint25.centerOfRotation = [0,0.8,0]
Viewpoint25.description = "Scene_Side View"
Viewpoint25.orientation = [0,1,0,1.5708]
Viewpoint25.position = [-2.6,1.5,1]

Scene13.children.append(Viewpoint25)
Viewpoint26 = x3d.Viewpoint()
Viewpoint26.DEF = "Scene_ISideView"
Viewpoint26.centerOfRotation = [0,0.8,0]
Viewpoint26.description = "Scene_Side View"
Viewpoint26.orientation = [0,1,0,1.5708]
Viewpoint26.position = [-5,1.5,1]

Scene13.children.append(Viewpoint26)
Viewpoint27 = x3d.Viewpoint()
Viewpoint27.DEF = "Scene_Full_ISideView"
Viewpoint27.centerOfRotation = [0,0.8,0]
Viewpoint27.description = "Scene_Side View"
Viewpoint27.orientation = [0,1,0,1.5708]
Viewpoint27.position = [-10,1.5,1]

Scene13.children.append(Viewpoint27)
Viewpoint28 = x3d.Viewpoint()
Viewpoint28.DEF = "Scene_OneBush_ISideView"
Viewpoint28.centerOfRotation = [0,0.8,0]
Viewpoint28.description = "Scene_Side View"
Viewpoint28.orientation = [0,1,0,1.5708]
Viewpoint28.position = [-20,1.5,1]

Scene13.children.append(Viewpoint28)
Viewpoint29 = x3d.Viewpoint()
Viewpoint29.DEF = "Scene_TwoBush_ISideView"
Viewpoint29.centerOfRotation = [0,0.8,0]
Viewpoint29.description = "Scene_Side View"
Viewpoint29.orientation = [0,1,0,1.5708]
Viewpoint29.position = [-10,1.5,1]

Scene13.children.append(Viewpoint29)
Viewpoint30 = x3d.Viewpoint()
Viewpoint30.DEF = "Scene_BackView"
Viewpoint30.centerOfRotation = [0,1.5,0]
Viewpoint30.description = "Scene_Back View"
Viewpoint30.orientation = [0,1,0,3.14]
Viewpoint30.position = [0,1.5,-5]

Scene13.children.append(Viewpoint30)
Viewpoint31 = x3d.Viewpoint()
Viewpoint31.DEF = "Scene_OldMan_BackView"
Viewpoint31.centerOfRotation = [0,1.5,0]
Viewpoint31.description = "Scene_Back View"
Viewpoint31.orientation = [0,1,0,3.14]
Viewpoint31.position = [0,1.5,-2.5]

Scene13.children.append(Viewpoint31)
Viewpoint32 = x3d.Viewpoint()
Viewpoint32.DEF = "Scene_Full_BackView"
Viewpoint32.centerOfRotation = [0,1.5,0]
Viewpoint32.description = "Scene_Back View"
Viewpoint32.orientation = [0,1,15,3.14]
Viewpoint32.position = [0,1.5,-20]

Scene13.children.append(Viewpoint32)
Viewpoint33 = x3d.Viewpoint()
Viewpoint33.DEF = "Scene_TopView"
Viewpoint33.centerOfRotation = [0,1.5,0]
Viewpoint33.description = "Scene_Top View"
Viewpoint33.orientation = [1,0,0,-1.5708]
Viewpoint33.position = [0,3.5,0]

Scene13.children.append(Viewpoint33)
Group34 = x3d.Group()
Group34.DEF = "OldMan_Humanoid"
HAnimHumanoid35 = x3d.HAnimHumanoid()
HAnimHumanoid35.name = "Walk"
HAnimHumanoid35.DEF = "OldMan"
HAnimHumanoid35.loa = 3
HAnimHumanoid35.version = "2.0"
MetadataSet36 = x3d.MetadataSet()
MetadataSet36.name = "warnings"
MetadataSet36.reference = "HAnim"
MetadataString37 = x3d.MetadataString()
MetadataString37.name = "SymmetricalLeftRight"
MetadataString37.reference = "correction options: ignore, warn, average, left, right, largest, smallest"
MetadataString37.value = ["ignore"]

MetadataSet36.value = MetadataString37

HAnimHumanoid35.metadata = MetadataSet36
HAnimJoint38 = x3d.HAnimJoint()
HAnimJoint38.name = "humanoid_root"
HAnimJoint38.DEF = "OldMan_humanoid_root"
HAnimJoint38.ulimit = [0,0,0]
HAnimJoint38.llimit = [0,0,0]
#TODO center='x 0.9155 z'
HAnimSegment39 = x3d.HAnimSegment()
HAnimSegment39.name = "sacrum"
HAnimSegment39.DEF = "OldMan_sacrum"
HAnimSite40 = x3d.HAnimSite()
HAnimSite40.name = "RootBack_view"
HAnimSite40.DEF = "OldMan_RootBack_view"
Transform41 = x3d.Transform()
Transform41.DEF = "hanimcordsys"
Transform41.scale = [0.175,0.175,0.175]
Viewpoint42 = x3d.Viewpoint()
Viewpoint42.DEF = "ViewBodyRootAxes"
Viewpoint42.description = "Joe_HAnim Root HAnimSite Coordinate Axes View"

Transform41.children.append(Viewpoint42)
Shape43 = x3d.Shape()
Shape43.DEF = "AxisLinesShape"
#RGB lines showing XYZ axes
IndexedLineSet44 = x3d.IndexedLineSet()
IndexedLineSet44.colorIndex = [0,1,2]
IndexedLineSet44.colorPerVertex = False
IndexedLineSet44.coordIndex = [0,1,-1,0,2,-1,0,3,-1]
Coordinate45 = x3d.Coordinate()
Coordinate45.point = (0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000)

IndexedLineSet44.coord = Coordinate45
Color46 = x3d.Color()
Color46.color = [1,0,0,0,0.6,0,0,0,1]

IndexedLineSet44.color = Color46

Shape43.geometry = IndexedLineSet44

Transform41.children.append(Shape43)
Shape47 = x3d.Shape()
Shape47.DEF = "OldMan_Shape"
Appearance48 = x3d.Appearance()
Appearance48.DEF = "OldMan_skin_Appearance"
Material49 = x3d.Material()
Material49.DEF = "OldMan_skin_Material"
Material49.diffuseColor = [0.3,0.3,0.6]
Material49.emissiveColor = [0.3,0.3,0.6]

Appearance48.material = Material49
ImageTexture50 = x3d.ImageTexture()
ImageTexture50.DEF = "OldManSkinImageTexture"
ImageTexture50.url = ["OldManBodyTexture29.png","https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Characters/JoeBodyTexture29.png"]

Appearance48.texture = ImageTexture50
TextureTransform51 = x3d.TextureTransform()
TextureTransform51.DEF = "KickTextureTransform"

Appearance48.textureTransform = TextureTransform51

Shape47.appearance = Appearance48
IndexedFaceSet52 = x3d.IndexedFaceSet()
IndexedFaceSet52.DEF = "OldMan_skin_IndexedFaceSet"

Shape47.geometry = IndexedFaceSet52

Transform41.skin.append(Shape47)

HAnimSite40.children.append(Transform41)

HAnimSegment39.children.append(HAnimSite40)

HAnimJoint38.children.append(HAnimSegment39)
HAnimJoint53 = x3d.HAnimJoint()
HAnimJoint53.name = "sacroiliac"
HAnimJoint53.DEF = "OldMan_sacroiliac"
HAnimJoint53.ulimit = [0,0,0]
HAnimJoint53.llimit = [0,0,0]
#TODO center='x 0.952 z'
#High hip
HAnimJoint54 = x3d.HAnimJoint()
HAnimJoint54.name = "l_hip"
HAnimJoint54.DEF = "OldMan_l_hip"
HAnimJoint54.ulimit = [0,0,0]
HAnimJoint54.llimit = [0,0,0]
#TODO center='x 0.879 z' Low hip
HAnimJoint55 = x3d.HAnimJoint()
HAnimJoint55.name = "l_knee"
HAnimJoint55.DEF = "OldMan_l_knee"
HAnimJoint55.ulimit = [0,0,0]
HAnimJoint55.llimit = [0,0,0]
#center='x 0.461 z'
HAnimJoint56 = x3d.HAnimJoint()
HAnimJoint56.name = "l_talocrural"
HAnimJoint56.DEF = "OldMan_l_talocrural"
HAnimJoint56.ulimit = [0,0,0]
HAnimJoint56.llimit = [0,0,0]
#Ankle
HAnimJoint57 = x3d.HAnimJoint()
HAnimJoint57.name = "l_tarsometatarsal_2"
HAnimJoint57.DEF = "Joe_l_tarsometatarsal_2"
HAnimJoint57.ulimit = [0,0,0]
HAnimJoint57.llimit = [0,0,0]
HAnimJoint58 = x3d.HAnimJoint()
HAnimJoint58.name = "l_metatarsophalangeal_2"
HAnimJoint58.DEF = "Joe_l_metatarsophalangeal_2"
HAnimJoint58.ulimit = [0,0,0]
HAnimJoint58.llimit = [0,0,0]
HAnimJoint59 = x3d.HAnimJoint()
HAnimJoint59.name = "l_tarsal_distal_interphalangeal_2"
HAnimJoint59.DEF = "Joe_l_tarsal_distal_interphalangeal_2"
HAnimJoint59.center = [0.115,0.02,0.122]
HAnimJoint59.ulimit = [0,0,0]
HAnimJoint59.llimit = [0,0,0]

HAnimJoint58.children.append(HAnimJoint59)

HAnimJoint57.children.append(HAnimJoint58)

HAnimJoint56.children.append(HAnimJoint57)

HAnimJoint55.children.append(HAnimJoint56)

HAnimJoint54.children.append(HAnimJoint55)
HAnimJoint60 = x3d.HAnimJoint()
HAnimJoint60.name = "l_hip"
HAnimJoint60.DEF = "OldMan_r_hip"
HAnimJoint60.ulimit = [0,0,0]
HAnimJoint60.llimit = [0,0,0]
#Low hip
HAnimJoint61 = x3d.HAnimJoint()
HAnimJoint61.name = "l_knee"
HAnimJoint61.DEF = "OldMan_r_knee"
HAnimJoint61.ulimit = [0,0,0]
HAnimJoint61.llimit = [0,0,0]

HAnimJoint60.children.append(HAnimJoint61)
HAnimJoint62 = x3d.HAnimJoint()
HAnimJoint62.name = "l_talocrural"
HAnimJoint62.DEF = "OldMan_r_talocrural"
HAnimJoint62.ulimit = [0,0,0]
HAnimJoint62.llimit = [0,0,0]
#Ankle
HAnimJoint63 = x3d.HAnimJoint()
HAnimJoint63.name = "r_tarsometatarsal_2"
HAnimJoint63.DEF = "Joe_r_tarsometatarsal_2"
HAnimJoint63.center = [-0.1,0.015,-0.01]
HAnimJoint63.skinCoordIndex = [374,375,376]
HAnimJoint63.skinCoordWeight = [1,1,1]
HAnimJoint63.ulimit = [0,0,0]
HAnimJoint63.llimit = [0,0,0]
HAnimJoint64 = x3d.HAnimJoint()
HAnimJoint64.name = "r_metatarsophalangeal_2"
HAnimJoint64.DEF = "Joe_r_metatarsophalangeal_2"
HAnimJoint64.center = [-0.115,0.037,0.09]
HAnimJoint64.skinCoordIndex = [377,378,379,380]
HAnimJoint64.skinCoordWeight = [1,1,1,1]
HAnimJoint64.ulimit = [0,0,0]
HAnimJoint64.llimit = [0,0,0]
HAnimJoint65 = x3d.HAnimJoint()
HAnimJoint65.name = "r_tarsal_distal_interphalangeal_2"
HAnimJoint65.DEF = "Joe_r_tarsal_distal_interphalangeal_2"
HAnimJoint65.center = [-0.1,0.01,0.14]
HAnimJoint65.skinCoordIndex = [381,382,383,384,385,386,387,388,389]
HAnimJoint65.skinCoordWeight = [1,1,1,1,1,1,1,1,1]
HAnimJoint65.ulimit = [0,0,0]
HAnimJoint65.llimit = [0,0,0]

HAnimJoint64.children.append(HAnimJoint65)

HAnimJoint63.children.append(HAnimJoint64)

HAnimJoint62.children.append(HAnimJoint63)

HAnimJoint60.children.append(HAnimJoint62)

HAnimJoint54.children.append(HAnimJoint60)

HAnimJoint53.children.append(HAnimJoint54)
HAnimJoint66 = x3d.HAnimJoint()
HAnimJoint66.name = "vl5"
HAnimJoint66.DEF = "OldMan_vl5"
HAnimJoint66.ulimit = [0,0,0]
HAnimJoint66.llimit = [0,0,0]
#Abdomen
HAnimJoint67 = x3d.HAnimJoint()
HAnimJoint67.name = "vl4"
HAnimJoint67.DEF = "MeshName_vl4"
HAnimJoint67.ulimit = [0,0,0]
HAnimJoint67.llimit = [0,0,0]
HAnimJoint68 = x3d.HAnimJoint()
HAnimJoint68.name = "vl3"
HAnimJoint68.DEF = "OldMan_vl3"
HAnimJoint68.ulimit = [0,0,0]
HAnimJoint68.llimit = [0,0,0]
#center='x 1.098 z'
#Low=' ist='
HAnimJoint69 = x3d.HAnimJoint()
HAnimJoint69.name = "vl2"
HAnimJoint69.DEF = "MeshName_vl2"
HAnimJoint69.ulimit = [0,0,0]
HAnimJoint69.llimit = [0,0,0]
HAnimJoint70 = x3d.HAnimJoint()
HAnimJoint70.name = "vl1"
HAnimJoint70.DEF = "OldMan_vl1"
HAnimJoint70.ulimit = [0,0,0]
HAnimJoint70.llimit = [0,0,0]
#center='x 1.171 z'
#High waist
HAnimJoint71 = x3d.HAnimJoint()
HAnimJoint71.name = "vt12"
HAnimJoint71.DEF = "MeshName_vt12"
HAnimJoint71.ulimit = [0,0,0]
HAnimJoint71.llimit = [0,0,0]
HAnimJoint72 = x3d.HAnimJoint()
HAnimJoint72.name = "vt11"
HAnimJoint72.DEF = "OldMan_vt11"
HAnimJoint72.ulimit = [0,0,0]
HAnimJoint72.llimit = [0,0,0]
#Ribcage='
HAnimJoint73 = x3d.HAnimJoint()
HAnimJoint73.name = "vt10"
HAnimJoint73.DEF = "MeshName_vt10"
HAnimJoint73.ulimit = [0,0,0]
HAnimJoint73.llimit = [0,0,0]
HAnimJoint74 = x3d.HAnimJoint()
HAnimJoint74.name = "vt9"
HAnimJoint74.DEF = "MeshName_vt9"
HAnimJoint74.ulimit = [0,0,0]
HAnimJoint74.llimit = [0,0,0]
HAnimJoint75 = x3d.HAnimJoint()
HAnimJoint75.name = "vt8"
HAnimJoint75.DEF = "MeshName_vt8"
HAnimJoint75.ulimit = [0,0,0]
HAnimJoint75.llimit = [0,0,0]
HAnimJoint76 = x3d.HAnimJoint()
HAnimJoint76.name = "vt7"
HAnimJoint76.DEF = "OldMan_vt7"
HAnimJoint76.ulimit = [0,0,0]
HAnimJoint76.llimit = [0,0,0]
#Sternum='
HAnimJoint77 = x3d.HAnimJoint()
HAnimJoint77.name = "vt6"
HAnimJoint77.DEF = "MeshName_vt6"
HAnimJoint77.ulimit = [0,0,0]
HAnimJoint77.llimit = [0,0,0]
HAnimJoint78 = x3d.HAnimJoint()
HAnimJoint78.name = "vt5"
HAnimJoint78.DEF = "MeshName_vt5"
HAnimJoint78.ulimit = [0,0,0]
HAnimJoint78.llimit = [0,0,0]
HAnimJoint79 = x3d.HAnimJoint()
HAnimJoint79.name = "vt4"
HAnimJoint79.DEF = "OldMan_vt4"
HAnimJoint79.ulimit = [0,0,0]
HAnimJoint79.llimit = [0,0,0]
#Chest
HAnimJoint80 = x3d.HAnimJoint()
HAnimJoint80.name = "vt3"
HAnimJoint80.DEF = "MeshName_vt3"
HAnimJoint80.ulimit = [0,0,0]
HAnimJoint80.llimit = [0,0,0]
HAnimJoint81 = x3d.HAnimJoint()
HAnimJoint81.name = "vt2"
HAnimJoint81.DEF = "OldMan_vt2"
HAnimJoint81.ulimit = [0,0,0]
HAnimJoint81.llimit = [0,0,0]
#High Chest
HAnimJoint82 = x3d.HAnimJoint()
HAnimJoint82.name = "vt1"
HAnimJoint82.DEF = "MeshName_vt1"
HAnimJoint82.ulimit = [0,0,0]
HAnimJoint82.llimit = [0,0,0]
HAnimJoint83 = x3d.HAnimJoint()
HAnimJoint83.name = "vc7"
HAnimJoint83.DEF = "OldMan_vc7"
HAnimJoint83.ulimit = [0,0,0]
HAnimJoint83.llimit = [0,0,0]
#Low neck
HAnimJoint84 = x3d.HAnimJoint()
HAnimJoint84.name = "vc6"
HAnimJoint84.DEF = "MeshName_vc6"
HAnimJoint84.ulimit = [0,0,0]
HAnimJoint84.llimit = [0,0,0]
HAnimJoint85 = x3d.HAnimJoint()
HAnimJoint85.name = "vc5"
HAnimJoint85.DEF = "MeshName_vc5"
HAnimJoint85.ulimit = [0,0,0]
HAnimJoint85.llimit = [0,0,0]
HAnimJoint86 = x3d.HAnimJoint()
HAnimJoint86.name = "vc4"
HAnimJoint86.DEF = "OldMan_vc4"
HAnimJoint86.ulimit = [0,0,0]
HAnimJoint86.llimit = [0,0,0]
#Mid=' ck='
HAnimJoint87 = x3d.HAnimJoint()
HAnimJoint87.name = "vc3"
HAnimJoint87.DEF = "MeshName_vc3"
HAnimJoint87.ulimit = [0,0,0]
HAnimJoint87.llimit = [0,0,0]
HAnimJoint88 = x3d.HAnimJoint()
HAnimJoint88.name = "vc2"
HAnimJoint88.DEF = "MeshName_vc2"
HAnimJoint88.ulimit = [0,0,0]
HAnimJoint88.llimit = [0,0,0]
HAnimJoint89 = x3d.HAnimJoint()
HAnimJoint89.name = "vc1"
HAnimJoint89.DEF = "OldMan_vc1"
HAnimJoint89.ulimit = [0,0,0]
HAnimJoint89.llimit = [0,0,0]
#High=' ck='
HAnimJoint90 = x3d.HAnimJoint()
HAnimJoint90.name = "skullbase"
HAnimJoint90.DEF = "OldMan_skullbase"
HAnimJoint90.ulimit = [0,0,0]
HAnimJoint90.llimit = [0,0,0]
HAnimDisplacer91 = x3d.HAnimDisplacer()
HAnimDisplacer91.name = "skull_tip_raiser_action"
HAnimDisplacer91.DEF = "Joe_skull_tip_raiser_action"
HAnimDisplacer91.coordIndex = [0,1,2,3,4,5,6,7,8,9]
HAnimDisplacer91.displacements = (0.0000,0.1500,0.0000,0.0000,0.0000,0.1500,-0.1000,0.0000,0.1500,0.1000,0.0000,0.0500,0.0000,-0.0200,0.0500,-0.1500,0.0000,0.0000,-0.0500,0.0000,0.0000,0.1500,0.0000,0.0000,0.0500,0.0000,0.0000,0.0000,0.0000,-0.1500)

HAnimJoint90.displacers.append(HAnimDisplacer91)
HAnimJoint92 = x3d.HAnimJoint()
HAnimJoint92.name = "l_eyelid_joint"
HAnimJoint92.DEF = "OldMan_l_eyelid_joint"
HAnimJoint92.ulimit = [0,0,0]
HAnimJoint92.llimit = [0,0,0]

HAnimJoint90.children.append(HAnimJoint92)
HAnimJoint93 = x3d.HAnimJoint()
HAnimJoint93.name = "l_eyeball_joint"
HAnimJoint93.DEF = "OldMan_l_eyeball_joint"
HAnimJoint93.ulimit = [0,0,0]
HAnimJoint93.llimit = [0,0,0]

HAnimJoint90.children.append(HAnimJoint93)
HAnimJoint94 = x3d.HAnimJoint()
HAnimJoint94.name = "l_eyebrow_joint"
HAnimJoint94.DEF = "OldMan_l_eyebrow_joint"
HAnimJoint94.ulimit = [0,0,0]
HAnimJoint94.llimit = [0,0,0]

HAnimJoint90.children.append(HAnimJoint94)
HAnimJoint95 = x3d.HAnimJoint()
HAnimJoint95.name = "r_eyelid_joint"
HAnimJoint95.DEF = "OldMan_r_eyelid_joint"
HAnimJoint95.ulimit = [0,0,0]
HAnimJoint95.llimit = [0,0,0]

HAnimJoint90.children.append(HAnimJoint95)
HAnimJoint96 = x3d.HAnimJoint()
HAnimJoint96.name = "r_eyeball_joint"
HAnimJoint96.DEF = "OldMan_r_eyeball_joint"
HAnimJoint96.ulimit = [0,0,0]
HAnimJoint96.llimit = [0,0,0]

HAnimJoint90.children.append(HAnimJoint96)
HAnimJoint97 = x3d.HAnimJoint()
HAnimJoint97.name = "r_eyebrow_joint"
HAnimJoint97.DEF = "OldMan_r_eyebrow_joint"
HAnimJoint97.ulimit = [0,0,0]
HAnimJoint97.llimit = [0,0,0]

HAnimJoint90.children.append(HAnimJoint97)
HAnimJoint98 = x3d.HAnimJoint()
HAnimJoint98.name = "temporomandibular"
HAnimJoint98.DEF = "OldMan_temporomandibular"
HAnimJoint98.ulimit = [0,0,0]
HAnimJoint98.llimit = [0,0,0]

HAnimJoint90.children.append(HAnimJoint98)

HAnimJoint89.children.append(HAnimJoint90)

HAnimJoint88.children.append(HAnimJoint89)

HAnimJoint87.children.append(HAnimJoint88)

HAnimJoint86.children.append(HAnimJoint87)

HAnimJoint85.children.append(HAnimJoint86)

HAnimJoint84.children.append(HAnimJoint85)

HAnimJoint83.children.append(HAnimJoint84)

HAnimJoint82.children.append(HAnimJoint83)
HAnimJoint99 = x3d.HAnimJoint()
HAnimJoint99.DEF = "OldMan_l_acromioclavicular"
HAnimJoint99.ulimit = [0,0,0]
HAnimJoint99.llimit = [0,0,0]
HAnimJoint100 = x3d.HAnimJoint()
HAnimJoint100.name = "l_acromioclavicular"
HAnimJoint100.DEF = "OldMan_l_sternoclavicular"
HAnimJoint100.ulimit = [0,0,0]
HAnimJoint100.llimit = [0,0,0]
HAnimJoint101 = x3d.HAnimJoint()
HAnimJoint101.name = "l_shoulder"
HAnimJoint101.DEF = "OldMan_l_shoulder"
HAnimJoint101.ulimit = [0,0,0]
HAnimJoint101.llimit = [0,0,0]
HAnimJoint102 = x3d.HAnimJoint()
HAnimJoint102.name = "l_elbow"
HAnimJoint102.DEF = "OldMan_l_elbow"
HAnimJoint102.ulimit = [0,0,0]
HAnimJoint102.llimit = [0,0,0]
HAnimJoint103 = x3d.HAnimJoint()
HAnimJoint103.name = "l_radiocarpal"
HAnimJoint103.DEF = "OldMan_l_radiocarpal"
HAnimJoint103.ulimit = [0,0,0]
HAnimJoint103.llimit = [0,0,0]
HAnimJoint104 = x3d.HAnimJoint()
HAnimJoint104.name = "l_carpometacarpal_1"
HAnimJoint104.DEF = "OldMan_l_carpometacarpal_1"
HAnimJoint104.ulimit = [0,0,0]
HAnimJoint104.llimit = [0,0,0]
HAnimJoint105 = x3d.HAnimJoint()
HAnimJoint105.name = "l_metacarpophalangeal_1"
HAnimJoint105.DEF = "OldMan_l_metacarpophalangeal_1"
HAnimJoint105.ulimit = [0,0,0]
HAnimJoint105.llimit = [0,0,0]
HAnimJoint106 = x3d.HAnimJoint()
HAnimJoint106.name = "l_carpal_interphalangeal_1"
HAnimJoint106.DEF = "OldMan_l_carpal_interphalangeal_1"
HAnimJoint106.ulimit = [0,0,0]
HAnimJoint106.llimit = [0,0,0]

HAnimJoint105.children.append(HAnimJoint106)

HAnimJoint104.children.append(HAnimJoint105)
HAnimJoint107 = x3d.HAnimJoint()
HAnimJoint107.name = "l_carpometacarpal_2"
HAnimJoint107.DEF = "OldMan_l_carpometacarpal_2"
HAnimJoint107.ulimit = [0,0,0]
HAnimJoint107.llimit = [0,0,0]
HAnimJoint108 = x3d.HAnimJoint()
HAnimJoint108.name = "l_metacarpophalangeal_2"
HAnimJoint108.DEF = "OldMan_l_metacarpophalangeal_2"
HAnimJoint108.ulimit = [0,0,0]
HAnimJoint108.llimit = [0,0,0]
HAnimJoint109 = x3d.HAnimJoint()
HAnimJoint109.name = "l_carpal_proximal_interphalangeal_2"
HAnimJoint109.DEF = "OldMan_l_carpal_proximal_interphalangeal_2"
HAnimJoint109.ulimit = [0,0,0]
HAnimJoint109.llimit = [0,0,0]
HAnimJoint110 = x3d.HAnimJoint()
HAnimJoint110.name = "l_carpal_distal_interphalangeal_2"
HAnimJoint110.DEF = "OldMan_l_carpal_distal_interphalangeal_2"
HAnimJoint110.ulimit = [0,0,0]
HAnimJoint110.llimit = [0,0,0]

HAnimJoint109.children.append(HAnimJoint110)

HAnimJoint108.children.append(HAnimJoint109)

HAnimJoint107.children.append(HAnimJoint108)
HAnimJoint111 = x3d.HAnimJoint()
HAnimJoint111.name = "l_carpometacarpal_3"
HAnimJoint111.DEF = "OldMan_l_carpometacarpal_3"
HAnimJoint111.ulimit = [0,0,0]
HAnimJoint111.llimit = [0,0,0]
HAnimJoint112 = x3d.HAnimJoint()
HAnimJoint112.name = "l_metacarpophalangeal_3"
HAnimJoint112.DEF = "OldMan_l_metacarpophalangeal_3"
HAnimJoint112.ulimit = [0,0,0]
HAnimJoint112.llimit = [0,0,0]
HAnimJoint113 = x3d.HAnimJoint()
HAnimJoint113.name = "l_carpal_proximal_interphalangeal_3"
HAnimJoint113.DEF = "OldMan_l_carpal_proximal_interphalangeal_3"
HAnimJoint113.ulimit = [0,0,0]
HAnimJoint113.llimit = [0,0,0]
HAnimJoint114 = x3d.HAnimJoint()
HAnimJoint114.name = "l_carpal_distal_interphalangeal_3"
HAnimJoint114.DEF = "OldMan_l_carpal_distal_interphalangeal_3"
HAnimJoint114.ulimit = [0,0,0]
HAnimJoint114.llimit = [0,0,0]

HAnimJoint113.children.append(HAnimJoint114)

HAnimJoint112.children.append(HAnimJoint113)

HAnimJoint111.children.append(HAnimJoint112)
HAnimJoint115 = x3d.HAnimJoint()
HAnimJoint115.name = "l_carpometacarpal_4"
HAnimJoint115.DEF = "OldMan_l_carpometacarpal_4"
HAnimJoint115.ulimit = [0,0,0]
HAnimJoint115.llimit = [0,0,0]
HAnimJoint116 = x3d.HAnimJoint()
HAnimJoint116.name = "l_metacarpophalangeal_4"
HAnimJoint116.DEF = "OldMan_l_metacarpophalangeal_4"
HAnimJoint116.ulimit = [0,0,0]
HAnimJoint116.llimit = [0,0,0]
HAnimJoint117 = x3d.HAnimJoint()
HAnimJoint117.name = "l_carpal_proximal_interphalangeal_4"
HAnimJoint117.DEF = "OldMan_l_carpal_proximal_interphalangeal_4"
HAnimJoint117.ulimit = [0,0,0]
HAnimJoint117.llimit = [0,0,0]
HAnimJoint118 = x3d.HAnimJoint()
HAnimJoint118.name = "l_carpal_distal_interphalangeal_4"
HAnimJoint118.DEF = "OldMan_l_carpal_distal_interphalangeal_4"
HAnimJoint118.ulimit = [0,0,0]
HAnimJoint118.llimit = [0,0,0]

HAnimJoint117.children.append(HAnimJoint118)

HAnimJoint116.children.append(HAnimJoint117)

HAnimJoint115.children.append(HAnimJoint116)
HAnimJoint119 = x3d.HAnimJoint()
HAnimJoint119.name = "l_carpometacarpal_5"
HAnimJoint119.DEF = "OldMan_l_carpometacarpal_5"
HAnimJoint119.ulimit = [0,0,0]
HAnimJoint119.llimit = [0,0,0]
HAnimJoint120 = x3d.HAnimJoint()
HAnimJoint120.name = "l_metacarpophalangeal_5"
HAnimJoint120.DEF = "OldMan_l_metacarpophalangeal_5"
HAnimJoint120.ulimit = [0,0,0]
HAnimJoint120.llimit = [0,0,0]
HAnimJoint121 = x3d.HAnimJoint()
HAnimJoint121.name = "l_carpal_proximal_interphalangeal_5"
HAnimJoint121.DEF = "OldMan_l_carpal_proximal_interphalangeal_5"
HAnimJoint121.ulimit = [0,0,0]
HAnimJoint121.llimit = [0,0,0]
HAnimJoint122 = x3d.HAnimJoint()
HAnimJoint122.name = "l_carpal_distal_interphalangeal_5"
HAnimJoint122.DEF = "OldMan_l_carpal_distal_interphalangeal_5"
HAnimJoint122.ulimit = [0,0,0]
HAnimJoint122.llimit = [0,0,0]

HAnimJoint121.children.append(HAnimJoint122)

HAnimJoint120.children.append(HAnimJoint121)

HAnimJoint119.children.append(HAnimJoint120)

HAnimJoint115.children.append(HAnimJoint119)

HAnimJoint111.children.append(HAnimJoint115)

HAnimJoint107.children.append(HAnimJoint111)

HAnimJoint104.children.append(HAnimJoint107)

HAnimJoint103.children.append(HAnimJoint104)
HAnimJoint123 = x3d.HAnimJoint()
HAnimJoint123.name = "r_sternoclavicular"
HAnimJoint123.DEF = "OldMan_r_sternoclavicular"
HAnimJoint123.ulimit = [0,0,0]
HAnimJoint123.llimit = [0,0,0]
HAnimJoint124 = x3d.HAnimJoint()
HAnimJoint124.name = "r_acromioclavicular"
HAnimJoint124.DEF = "OldMan_r_acromioclavicular"
HAnimJoint124.ulimit = [0,0,0]
HAnimJoint124.llimit = [0,0,0]
HAnimJoint125 = x3d.HAnimJoint()
HAnimJoint125.name = "r_shoulder"
HAnimJoint125.DEF = "OldMan_r_shoulder"
HAnimJoint125.ulimit = [0,0,0]
HAnimJoint125.llimit = [0,0,0]
HAnimJoint126 = x3d.HAnimJoint()
HAnimJoint126.name = "r_elbow"
HAnimJoint126.DEF = "OldMan_r_elbow"
HAnimJoint126.ulimit = [0,0,0]
HAnimJoint126.llimit = [0,0,0]
HAnimJoint127 = x3d.HAnimJoint()
HAnimJoint127.name = "r_radiocarpal"
HAnimJoint127.DEF = "OldMan_r_radiocarpal"
HAnimJoint127.ulimit = [0,0,0]
HAnimJoint127.llimit = [0,0,0]
HAnimJoint128 = x3d.HAnimJoint()
HAnimJoint128.name = "r_carpometacarpal_1"
HAnimJoint128.DEF = "OldMan_r_carpometacarpal_1"
HAnimJoint128.ulimit = [0,0,0]
HAnimJoint128.llimit = [0,0,0]
HAnimJoint129 = x3d.HAnimJoint()
HAnimJoint129.name = "r_metacarpophalangeal_1"
HAnimJoint129.DEF = "OldMan_r_metacarpophalangeal_1"
HAnimJoint129.ulimit = [0,0,0]
HAnimJoint129.llimit = [0,0,0]
HAnimJoint130 = x3d.HAnimJoint()
HAnimJoint130.name = "r_carpal_interphalangeal_1"
HAnimJoint130.DEF = "OldMan_r_carpal_interphalangeal_1"
HAnimJoint130.ulimit = [0,0,0]
HAnimJoint130.llimit = [0,0,0]

HAnimJoint129.children.append(HAnimJoint130)

HAnimJoint128.children.append(HAnimJoint129)
HAnimJoint131 = x3d.HAnimJoint()
HAnimJoint131.name = "r_carpometacarpal_2"
HAnimJoint131.DEF = "OldMan_r_carpometacarpal_2"
HAnimJoint131.ulimit = [0,0,0]
HAnimJoint131.llimit = [0,0,0]
HAnimJoint132 = x3d.HAnimJoint()
HAnimJoint132.name = "r_metacarpophalangeal_2"
HAnimJoint132.DEF = "OldMan_r_metacarpophalangeal_2"
HAnimJoint132.ulimit = [0,0,0]
HAnimJoint132.llimit = [0,0,0]
HAnimJoint133 = x3d.HAnimJoint()
HAnimJoint133.name = "r_carpal_proximal_interphalangeal_2"
HAnimJoint133.DEF = "OldMan_r_carpal_proximal_interphalangeal_2"
HAnimJoint133.ulimit = [0,0,0]
HAnimJoint133.llimit = [0,0,0]
HAnimJoint134 = x3d.HAnimJoint()
HAnimJoint134.name = "r_carpal_distal_interphalangeal_2"
HAnimJoint134.DEF = "OldMan_r_carpal_distal_interphalangeal_2"
HAnimJoint134.ulimit = [0,0,0]
HAnimJoint134.llimit = [0,0,0]

HAnimJoint133.children.append(HAnimJoint134)

HAnimJoint132.children.append(HAnimJoint133)

HAnimJoint131.children.append(HAnimJoint132)
HAnimJoint135 = x3d.HAnimJoint()
HAnimJoint135.name = "r_carpometacarpal_3"
HAnimJoint135.DEF = "OldMan_r_carpometacarpal_3"
HAnimJoint135.ulimit = [0,0,0]
HAnimJoint135.llimit = [0,0,0]
HAnimJoint136 = x3d.HAnimJoint()
HAnimJoint136.name = "r_metacarpophalangeal_3"
HAnimJoint136.DEF = "OldMan_r_metacarpophalangeal_3"
HAnimJoint136.ulimit = [0,0,0]
HAnimJoint136.llimit = [0,0,0]
HAnimJoint137 = x3d.HAnimJoint()
HAnimJoint137.name = "r_carpal_proximal_interphalangeal_3"
HAnimJoint137.DEF = "OldMan_r_carpal_proximal_interphalangeal_3"
HAnimJoint137.ulimit = [0,0,0]
HAnimJoint137.llimit = [0,0,0]
HAnimJoint138 = x3d.HAnimJoint()
HAnimJoint138.name = "r_carpal_distal_interphalangeal_3"
HAnimJoint138.DEF = "OldMan_r_carpal_distal_interphalangeal_3"
HAnimJoint138.ulimit = [0,0,0]
HAnimJoint138.llimit = [0,0,0]

HAnimJoint137.children.append(HAnimJoint138)

HAnimJoint136.children.append(HAnimJoint137)

HAnimJoint135.children.append(HAnimJoint136)
HAnimJoint139 = x3d.HAnimJoint()
HAnimJoint139.name = "r_carpometacarpal_4"
HAnimJoint139.DEF = "OldMan_r_carpometacarpal_4"
HAnimJoint139.ulimit = [0,0,0]
HAnimJoint139.llimit = [0,0,0]
HAnimJoint140 = x3d.HAnimJoint()
HAnimJoint140.name = "r_metacarpophalangeal_4"
HAnimJoint140.DEF = "OldMan_r_metacarpophalangeal_4"
HAnimJoint140.ulimit = [0,0,0]
HAnimJoint140.llimit = [0,0,0]
HAnimJoint141 = x3d.HAnimJoint()
HAnimJoint141.name = "r_carpal_proximal_interphalangeal_4"
HAnimJoint141.DEF = "OldMan_r_carpal_proximal_interphalangeal_4"
HAnimJoint141.ulimit = [0,0,0]
HAnimJoint141.llimit = [0,0,0]
HAnimJoint142 = x3d.HAnimJoint()
HAnimJoint142.name = "r_carpal_distal_interphalangeal_4"
HAnimJoint142.DEF = "OldMan_r_carpal_distal_interphalangeal_4"
HAnimJoint142.ulimit = [0,0,0]
HAnimJoint142.llimit = [0,0,0]

HAnimJoint141.children.append(HAnimJoint142)

HAnimJoint140.children.append(HAnimJoint141)

HAnimJoint139.children.append(HAnimJoint140)
HAnimJoint143 = x3d.HAnimJoint()
HAnimJoint143.name = "r_carpometacarpal_5"
HAnimJoint143.DEF = "OldMan_r_carpometacarpal_5"
HAnimJoint143.ulimit = [0,0,0]
HAnimJoint143.llimit = [0,0,0]
HAnimJoint144 = x3d.HAnimJoint()
HAnimJoint144.name = "r_metacarpophalangeal_5"
HAnimJoint144.DEF = "OldMan_r_metacarpophalangeal_5"
HAnimJoint144.ulimit = [0,0,0]
HAnimJoint144.llimit = [0,0,0]
HAnimJoint145 = x3d.HAnimJoint()
HAnimJoint145.name = "r_carpal_proximal_interphalangeal_5"
HAnimJoint145.DEF = "OldMan_r_carpal_proximal_interphalangeal_5"
HAnimJoint145.ulimit = [0,0,0]
HAnimJoint145.llimit = [0,0,0]
HAnimJoint146 = x3d.HAnimJoint()
HAnimJoint146.name = "r_carpal_distal_interphalangeal_5"
HAnimJoint146.DEF = "OldMan_r_carpal_distal_interphalangeal_5"
HAnimJoint146.ulimit = [0,0,0]
HAnimJoint146.llimit = [0,0,0]

HAnimJoint145.children.append(HAnimJoint146)

HAnimJoint144.children.append(HAnimJoint145)

HAnimJoint143.children.append(HAnimJoint144)

HAnimJoint139.children.append(HAnimJoint143)

HAnimJoint135.children.append(HAnimJoint139)

HAnimJoint131.children.append(HAnimJoint135)

HAnimJoint128.children.append(HAnimJoint131)

HAnimJoint127.children.append(HAnimJoint128)

HAnimJoint126.children.append(HAnimJoint127)

HAnimJoint125.children.append(HAnimJoint126)

HAnimJoint124.children.append(HAnimJoint125)

HAnimJoint123.children.append(HAnimJoint124)

HAnimJoint103.children.append(HAnimJoint123)

HAnimJoint102.children.append(HAnimJoint103)

HAnimJoint101.children.append(HAnimJoint102)

HAnimJoint100.children.append(HAnimJoint101)

HAnimJoint99.children.append(HAnimJoint100)

HAnimJoint82.children.append(HAnimJoint99)

HAnimJoint81.children.append(HAnimJoint82)

HAnimJoint80.children.append(HAnimJoint81)

HAnimJoint79.children.append(HAnimJoint80)

HAnimJoint78.children.append(HAnimJoint79)

HAnimJoint77.children.append(HAnimJoint78)

HAnimJoint76.children.append(HAnimJoint77)

HAnimJoint75.children.append(HAnimJoint76)

HAnimJoint74.children.append(HAnimJoint75)

HAnimJoint73.children.append(HAnimJoint74)

HAnimJoint72.children.append(HAnimJoint73)

HAnimJoint71.children.append(HAnimJoint72)

HAnimJoint70.children.append(HAnimJoint71)

HAnimJoint69.children.append(HAnimJoint70)

HAnimJoint68.children.append(HAnimJoint69)

HAnimJoint67.children.append(HAnimJoint68)

HAnimJoint66.children.append(HAnimJoint67)

HAnimJoint53.children.append(HAnimJoint66)

HAnimJoint38.children.append(HAnimJoint53)

HAnimHumanoid35.skeleton.append(HAnimJoint38)

Group34.children.append(HAnimHumanoid35)

Scene13.children.append(Group34)

X3D0.Scene = Scene13
f = open("././WinterAndSpringTest_RoundTrip.x3d", "w")
f.write(X3D0.XML())
f.close()
