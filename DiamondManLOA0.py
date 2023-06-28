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
meta3.content = "DiamondManLOA0.x3d"

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.name = "description"
meta4.content = "HAnim skeletal structure for Level of Action (LOA) zero, with one diamond at the base node for the structure. HumanoidRoot only, so this is the minimum legal HAnim humanoid."

head1.children.append(meta4)
meta5 = x3d.meta()
meta5.name = "creator"
meta5.content = "Matthew T. Beitler"

head1.children.append(meta5)
meta6 = x3d.meta()
meta6.name = "translator"
meta6.content = "Joel S. Pawloski"

head1.children.append(meta6)
meta7 = x3d.meta()
meta7.name = "created"
meta7.content = "12 November 2001"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.name = "modified"
meta8.content = "23 December 2021"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "motto"
meta9.content = "(a) \"Diamonds are a girl's best friend.\" (b) \"Gosh, it sure is chilly in here.\""

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "reference"
meta10.content = "HAnim 2.0 specification, Appendix A: Nominal human body dimensions and levels of articulation (LOAs)"

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.name = "reference"
meta11.content = "https://www.web3d.org/documents/specifications/19774-1/V2.0/HAnim/BodyDimensionsAndLOAs.html"

head1.children.append(meta11)
meta12 = x3d.meta()
meta12.name = "reference"
meta12.content = "https://www.web3d.org/documents/specifications/19774-1/V2.0/HAnim/BodyDimensionsAndLOAs.html#LevelOfArticulationZero"

head1.children.append(meta12)
meta13 = x3d.meta()
meta13.name = "reference"
meta13.content = "HAnim 1.1 specification, Appendix A: Suggested Body Dimensions and Levels of Articulation, Level of Articulation Zero"

head1.children.append(meta13)
meta14 = x3d.meta()
meta14.name = "reference"
meta14.content = "http://HAnim.org/Specifications/HAnim1.1/appendices.html#appendixa"

head1.children.append(meta14)
meta15 = x3d.meta()
meta15.name = "reference"
meta15.content = "http://HAnim.org/Specifications/HAnim1.1/JointCenters1_1_LOA0.wrl"

head1.children.append(meta15)
meta16 = x3d.meta()
meta16.name = "reference"
meta16.content = "http://HAnim.org/Specifications/HAnim1.1/JointCenters1_1_LOA0-diamond.wrl"

head1.children.append(meta16)
meta17 = x3d.meta()
meta17.name = "reference"
meta17.content = "http://ece.uwaterloo.ca/~HAnim"

head1.children.append(meta17)
meta18 = x3d.meta()
meta18.name = "reference"
meta18.content = "http://www.cis.upenn.edu/~badler/anthro/89-71.pdf"

head1.children.append(meta18)
meta19 = x3d.meta()
meta19.name = "reference"
meta19.content = "http://www.cis.upenn.edu/~badler/anthro/89-71.ps"

head1.children.append(meta19)
meta20 = x3d.meta()
meta20.name = "reference"
meta20.content = "http://www.cis.upenn.edu/~beitler"

head1.children.append(meta20)
meta21 = x3d.meta()
meta21.name = "Image"
meta21.content = "humanoid_landmark_locations.gif"

head1.children.append(meta21)
meta22 = x3d.meta()
meta22.name = "Image"
meta22.content = "http://HAnim.org/Specifications/HAnim1.1/humanoid_landmark_locations.gif"

head1.children.append(meta22)
meta23 = x3d.meta()
meta23.name = "identifier"
meta23.content = "https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Templates/DiamondManLOA0.x3d"

head1.children.append(meta23)
meta24 = x3d.meta()
meta24.name = "generator"
meta24.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"

head1.children.append(meta24)
meta25 = x3d.meta()
meta25.name = "license"
meta25.content = "../license.html"

head1.children.append(meta25)

X3D0.head = head1
Scene26 = x3d.Scene()
WorldInfo27 = x3d.WorldInfo()
WorldInfo27.info = ["HAnim 2.0 Default Joint Centers, Level Of Articulation (LOA) 0 -------------------------------------------------------- HANIM 1.1 (VRML 2.0) Author name: eMpTy (a.k.a. Matthew T. Beitler) HANIM 1.1 (VRML 2.0) Author email: beitler@graphics.cis.upenn.edu or beitler@acm.org HANIM 1.1 (VRML 2.0) Author homepage: http://www.cis.upenn.edu/~beitler HANIM 1.1 (VRML 2.0) Compliance Date: May 12, 1999 HANIM 1.1 Compliance Information: http://ece.uwaterloo.ca/~HAnim/ Construction Info (joint centers): The joint centers of this figure are based on the work of Norman Badler, director of the Center for Human Modeling and Simulation at the University of Pennsylvania. The original document which these joint centers are based on can be found at: http://www.cis.upenn.edu/~badler/anthro/89-71.ps, .pdf"]
WorldInfo27.title = "HANIM 2.0 Default Joint Centers, LOA0"

Scene26.children.append(WorldInfo27)
NavigationInfo28 = x3d.NavigationInfo()
NavigationInfo28.speed = 1.5

Scene26.children.append(NavigationInfo28)
Viewpoint29 = x3d.Viewpoint()
Viewpoint29.centerOfRotation = [0,1,0]
Viewpoint29.description = "Diamond Man, LOA 0"
Viewpoint29.position = [0,1,3]

Scene26.children.append(Viewpoint29)
HAnimHumanoid30 = x3d.HAnimHumanoid()
HAnimHumanoid30.name = "humanoid"
HAnimHumanoid30.DEF = "hanim_humanoid"
HAnimHumanoid30.loa = 0
HAnimHumanoid30.version = "2.0"
#original HAnimHumanoid info='\"authorEmail=beitler@graphics.cis.upenn.edu beitler@acm.org\" \"authorName=Matthew T. Beitler\" \"copyright=Copyright 1999 Matthew T. Beitler\" \"creationDate=05/12/99\" \"humanoidVersion=JointCenters 1.1 LOA0\" \"usageRestrictions=PERMISSION TO FULLY USE THIS SCENE GRAPH IS GRANTED PROVIDED THIS COPYRIGHT INFORMATION AND DOCUMENTATION OF THE ORIGINAL AUTHOR IS INCLUDED. This humanoid scene graph is provided _as-is_ and without warranty of any kind express implied or otherwise including without limitation any warranty of merchantability or fitness for a particular purpose.\"'
MetadataSet31 = x3d.MetadataSet()
MetadataSet31.name = "HAnimHumanoid.info"
MetadataSet31.reference = "https://www.web3d.org/documents/specifications/19774/V2.0/Architecture/ObjectInterfaces.html#Humanoid"
MetadataString32 = x3d.MetadataString()
MetadataString32.name = "authorEmail"
MetadataString32.value = ["beitler@graphics.cis.upenn.edu beitler@acm.org"]

MetadataSet31.value.append(MetadataString32)
MetadataString33 = x3d.MetadataString()
MetadataString33.name = "authorName"
MetadataString33.value = ["Matthew T. Beitler"]

MetadataSet31.value.append(MetadataString33)
MetadataString34 = x3d.MetadataString()
MetadataString34.name = "copyright"
MetadataString34.value = ["Copyright 1999 Matthew T. Beitler"]

MetadataSet31.value.append(MetadataString34)
MetadataString35 = x3d.MetadataString()
MetadataString35.name = "creationDate"
MetadataString35.value = ["05/12/99"]

MetadataSet31.value.append(MetadataString35)
MetadataString36 = x3d.MetadataString()
MetadataString36.name = "humanoidVersion"
MetadataString36.value = ["JointCenters 1.1 LOA0"]

MetadataSet31.value.append(MetadataString36)
MetadataString37 = x3d.MetadataString()
MetadataString37.name = "usageRestrictions"
MetadataString37.value = ["PERMISSION TO FULLY USE THIS SCENE GRAPH IS GRANTED PROVIDED THIS COPYRIGHT INFORMATION AND DOCUMENTATION OF THE ORIGINAL AUTHOR IS INCLUDED. This humanoid scene graph is provided _as-is_ and without warranty of any kind express implied or otherwise including without limitation any warranty of merchantability or fitness for a particular purpose."]

MetadataSet31.value.append(MetadataString37)

HAnimHumanoid30.metadata.append(MetadataSet31)
HAnimJoint38 = x3d.HAnimJoint()
HAnimJoint38.name = "humanoid_root"
HAnimJoint38.DEF = "hanim_humanoid_root"
HAnimJoint38.center = [0,0.824,0.0277]
HAnimJoint38.ulimit = [0,0,0]
HAnimJoint38.llimit = [0,0,0]
HAnimJoint39 = x3d.HAnimJoint()
HAnimJoint39.name = "sacroiliac"
HAnimJoint39.DEF = "hanim_sacroiliac"
HAnimJoint39.center = [0,0.9149,0.0016]
HAnimJoint39.ulimit = [0,0,0]
HAnimJoint39.llimit = [0,0,0]
HAnimSegment40 = x3d.HAnimSegment()
HAnimSegment40.name = "pelvis"
HAnimSegment40.DEF = "hanim_pelvis"
Transform41 = x3d.Transform()
Transform41.translation = [0,0.9149,0.0016]
Shape42 = x3d.Shape()
Shape42.DEF = "DiamondShape"
IndexedFaceSet43 = x3d.IndexedFaceSet()
IndexedFaceSet43.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet43.creaseAngle = 0.5
Coordinate44 = x3d.Coordinate()
Coordinate44.point = (0.0000,0.0100,0.0000,-0.0100,0.0000,0.0000,0.0000,0.0000,0.0100,0.0100,0.0000,0.0000,0.0000,0.0000,-0.0100,0.0000,-0.0100,0.0000)

IndexedFaceSet43.coord.append(Coordinate44)

Shape42.geometry = IndexedFaceSet43
Appearance45 = x3d.Appearance()
Material46 = x3d.Material()
Material46.diffuseColor = [1,1,0]

Appearance45.material = Material46

Shape42.appearance = Appearance45

Transform41.children.append(Shape42)

HAnimSegment40.children.append(Transform41)

HAnimJoint39.children.append(HAnimSegment40)

HAnimJoint38.children.append(HAnimJoint39)

HAnimHumanoid30.skeleton.append(HAnimJoint38)
HAnimSite47 = x3d.HAnimSite()
HAnimSite47.name = "site_view"
HAnimSite47.DEF = "hanim_site_view"
Viewpoint48 = x3d.Viewpoint()
Viewpoint48.DEF = "InclinedView"
Viewpoint48.description = "Inclined View"
Viewpoint48.orientation = [-0.113,0.993,0.0347,0.671]
Viewpoint48.position = [1.62,1.05,2.06]

HAnimSite47.children.append(Viewpoint48)
Viewpoint49 = x3d.Viewpoint()
Viewpoint49.DEF = "FrontView"
Viewpoint49.description = "Front View"
Viewpoint49.position = [0,0.854,2.57665]

HAnimSite47.children.append(Viewpoint49)
Viewpoint50 = x3d.Viewpoint()
Viewpoint50.DEF = "SideView"
Viewpoint50.description = "Side View"
Viewpoint50.orientation = [0,1,0,1.57079]
Viewpoint50.position = [2.5929,0.854,0]

HAnimSite47.children.append(Viewpoint50)
Viewpoint51 = x3d.Viewpoint()
Viewpoint51.DEF = "TopView"
Viewpoint51.description = "Top View"
Viewpoint51.orientation = [1,0,0,-1.57079]
Viewpoint51.position = [0,3.4495,0]

HAnimSite47.children.append(Viewpoint51)

HAnimHumanoid30.viewpoints.append(HAnimSite47)
HAnimJoint52 = x3d.HAnimJoint()
HAnimJoint52.USE = "hanim_humanoid_root"

HAnimHumanoid30.joints.append(HAnimJoint52)
HAnimJoint53 = x3d.HAnimJoint()
HAnimJoint53.USE = "hanim_sacroiliac"

HAnimHumanoid30.joints.append(HAnimJoint53)
HAnimSegment54 = x3d.HAnimSegment()
HAnimSegment54.USE = "hanim_pelvis"

HAnimHumanoid30.segments.append(HAnimSegment54)

Scene26.children.append(HAnimHumanoid30)

X3D0.Scene = Scene26
f = open("././DiamondManLOA0_RoundTrip.x3d", "w")
f.write(X3D0.XML())
f.close()
