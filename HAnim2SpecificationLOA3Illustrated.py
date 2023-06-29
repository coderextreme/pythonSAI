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
meta3.content = "HAnim2SpecificationLOA3Illustrated.x3d"

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.name = "description"
meta4.content = "HAnim Specification reference example providing full coverage (and no illustrated visibility) of all specified HAnim constructs, also suitable for re-use as an authoring template."

head1.children.append(meta4)
meta5 = x3d.meta()
meta5.name = "reference"
meta5.content = "https://www.web3d.org/files/specifications/19774/V1.0/HAnim/BodyDimensionsAndLOAs.html#LOA3ExampleSourceWithDiamonds"

head1.children.append(meta5)
meta6 = x3d.meta()
meta6.name = "created"
meta6.content = "18 February 2021"

head1.children.append(meta6)
meta7 = x3d.meta()
meta7.name = "modified"
meta7.content = "23 December 2021"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.name = "creator"
meta8.content = "Don Brutzman"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "reference"
meta9.content = "HAnim2SpecificationLOA3Invisible.x3d"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "reference"
meta10.content = "HAnim2SpecificationLOA3Animation.x3d"

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.name = "reference"
meta11.content = "HAnimSpecificationExampleChangeLog.txt"

head1.children.append(meta11)
meta12 = x3d.meta()
meta12.name = "Image"
meta12.content = "images/BonesAllSkeletonFrontViewLOA1.png"

head1.children.append(meta12)
meta13 = x3d.meta()
meta13.name = "Image"
meta13.content = "images/BonesAllSkeletonFrontViewLOA2.png"

head1.children.append(meta13)
meta14 = x3d.meta()
meta14.name = "Image"
meta14.content = "images/BonesAllSkeletonFrontViewLOA3.png"

head1.children.append(meta14)
meta15 = x3d.meta()
meta15.name = "TODO"
meta15.content = "move relevant HAnimSite/Viewpoint pairs into skeleton at appropriate locations"

head1.children.append(meta15)
meta16 = x3d.meta()
meta16.name = "TODO"
meta16.content = "insert MetadataInteger nodes indicating LOA for each Joint and Segment"

head1.children.append(meta16)
meta17 = x3d.meta()
meta17.name = "reference"
meta17.content = "Norman Badler et al., ANTHROPOMETRY FOR COMPUTER GRAPHICS HUMAN FIGURES, University of Pennsylvania, 1989."

head1.children.append(meta17)
meta18 = x3d.meta()
meta18.name = "reference"
meta18.content = "http://www.cis.upenn.edu/~badler/anthro/89-71.ps"

head1.children.append(meta18)
meta19 = x3d.meta()
meta19.name = "reference"
meta19.content = "tables/AnthropometryForComputerGraphicsHumanFigures89-71.pdf"

head1.children.append(meta19)
meta20 = x3d.meta()
meta20.name = "translator"
meta20.content = "Don Brutzman and Joe Williams"

head1.children.append(meta20)
meta21 = x3d.meta()
meta21.name = "generator"
meta21.content = "BS Contact Geo 8.001, http://www.bitmanagement.de/en/products/interactive-3d-clients/bs-contact-geo"

head1.children.append(meta21)
meta22 = x3d.meta()
meta22.name = "reference"
meta22.content = "originals/LOA3ExampleSourceWithDiamondsOriginal.wrl"

head1.children.append(meta22)
meta23 = x3d.meta()
meta23.name = "reference"
meta23.content = "originals/LOA3ExampleSourceWithDiamondsOriginal.x3d"

head1.children.append(meta23)
meta24 = x3d.meta()
meta24.name = "reference"
meta24.content = "originals/LOA3ExampleSourceWithDiamondsOriginalBsContactExport.x3d"

head1.children.append(meta24)
meta25 = x3d.meta()
meta25.name = "reference"
meta25.content = "HAnim Specification Table 4.4 - Face Joint object names, https://www.web3d.org/files/specifications/19774/V1.0/HAnim/concepts.html#FaceJointObjectNames"

head1.children.append(meta25)
meta26 = x3d.meta()
meta26.name = "generator"
meta26.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"

head1.children.append(meta26)
meta27 = x3d.meta()
meta27.name = "identifier"
meta27.content = "https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Specifications/HAnim2SpecificationLOA3Illustrated.x3d"

head1.children.append(meta27)
meta28 = x3d.meta()
meta28.name = "license"
meta28.content = "../license.html"

head1.children.append(meta28)

X3D0.head = head1
Scene29 = x3d.Scene()
Background30 = x3d.Background()
Background30.skyColor = [0.3,0.3,0.3]

Scene29.children.append(Background30)
NavigationInfo31 = x3d.NavigationInfo()

Scene29.children.append(NavigationInfo31)
Group32 = x3d.Group()
Group32.DEF = "Original_WorldInfo"
WorldInfo33 = x3d.WorldInfo()
WorldInfo33.info = [" HANIM 200x Default Joint Centers, Level-Of-Articulation 3 HANIM 200x (VRML97) Author name: eMpTy (a.k.a. Matthew T. Beitler) HANIM 200x (VRML97) Author email: beitler@cis.upenn.edu or beitler@acm.org HANIM 200x (VRML97) Author homepage: http://www.cis.upenn.edu/~beitler HANIM 200x (VRML97) Compliance Date: August 12, 2003 HANIM 200x Compliance Information: http://HAnim.org/Specifications/HAnim200x Construction Info (joint centers): The joint centers of this figure are based on the work of Norman Badler, director of the Center for Human Modeling and Simulation at the University of Pennsylvania. The original document which these joint centers are based on can be found at: http://www.cis.upenn.edu/~badler/anthro/89-71.ps "]
WorldInfo33.title = "HANIM 200x Default Joint Centers, LOA3"

Group32.children.append(WorldInfo33)

Scene29.children.append(Group32)
#TODO move viewpoints to be internal to HAnimHumanoid
#Viewpoint centerOfRotation=\"0 0.9149 0.0016\" matches initial at-rest locaton of the sacroliac. Note that these viewpoints are external to the HAnimHumanoid and do not move with the human.
Viewpoint34 = x3d.Viewpoint()
Viewpoint34.centerOfRotation = [0,0.9149,0.0016]
Viewpoint34.description = "Humanoid LOA 3 Front"
Viewpoint34.position = [0,0.4,4]

Scene29.children.append(Viewpoint34)
Viewpoint35 = x3d.Viewpoint()
Viewpoint35.centerOfRotation = [0,0.9149,0.0016]
Viewpoint35.description = "Humanoid LOA 3 Front Close"
Viewpoint35.position = [0,0.8,2]

Scene29.children.append(Viewpoint35)
Viewpoint36 = x3d.Viewpoint()
Viewpoint36.centerOfRotation = [0,0.9149,0.0016]
Viewpoint36.description = "Humanoid LOA 3 Front Closer"
Viewpoint36.position = [0,1.2,1]

Scene29.children.append(Viewpoint36)
Viewpoint37 = x3d.Viewpoint()
Viewpoint37.centerOfRotation = [0,1.5,0.0016]
Viewpoint37.description = "Humanoid LOA 3 Front Face"
Viewpoint37.position = [0,1.63,1]

Scene29.children.append(Viewpoint37)
Viewpoint38 = x3d.Viewpoint()
Viewpoint38.centerOfRotation = [0,0.9149,0.0016]
Viewpoint38.description = "Humanoid LOA 3 Right Side"
Viewpoint38.orientation = [0,1,0,1.5708]
Viewpoint38.position = [2.6,0.8,0]

Scene29.children.append(Viewpoint38)
Viewpoint39 = x3d.Viewpoint()
Viewpoint39.centerOfRotation = [0,0.9149,0.0016]
Viewpoint39.description = "Humanoid LOA 3 Right Side Close"
Viewpoint39.orientation = [0,1,0,1.2]
Viewpoint39.position = [1,0.8,0.5]

Scene29.children.append(Viewpoint39)
Viewpoint40 = x3d.Viewpoint()
Viewpoint40.centerOfRotation = [0,0.9149,0.0016]
Viewpoint40.description = "Humanoid LOA 3 Left Side Close"
Viewpoint40.orientation = [0,1,0,-1.2]
Viewpoint40.position = [-1,0.8,0.5]

Scene29.children.append(Viewpoint40)
Viewpoint41 = x3d.Viewpoint()
Viewpoint41.centerOfRotation = [0,0.9149,0.0016]
Viewpoint41.description = "Humanoid LOA 3 Left Side"
Viewpoint41.orientation = [0,1,0,-1.5708]
Viewpoint41.position = [-2.6,0.8,0]

Scene29.children.append(Viewpoint41)
Viewpoint42 = x3d.Viewpoint()
Viewpoint42.centerOfRotation = [0,0.9149,0.0016]
Viewpoint42.description = "Humanoid LOA 3 Top"
Viewpoint42.orientation = [1,0,0,-1.5708]
Viewpoint42.position = [0,3.5,0]

Scene29.children.append(Viewpoint42)
HAnimHumanoid43 = x3d.HAnimHumanoid()
HAnimHumanoid43.name = "humanoid"
HAnimHumanoid43.DEF = "hanim_humanoid"
HAnimHumanoid43.loa = 3
HAnimHumanoid43.version = "2.0"
#original HAnimHumanoid info='\"authorName=Matthew T. Beitler Joe D. Williams Don Brutzman\" \"authorEmail=HAnim@web3D.org\" \"copyright=none\" \"creationDate=12 May 1999\" \"usageRestrictions=none\" \"humanoidVersion=2.0\" \"height=1.7504\"'
#Only one root HAnimJoint is allowed
#original HAnimHumanoid info='\"authorName=Matthew T. Beitler Joe D. Williams Don Brutzman\" \"authorEmail=HAnim@web3D.org\" \"copyright=none\" \"creationDate=12 May 1999\" \"usageRestrictions=none\" \"humanoidVersion=2.0\" \"height=1.7504\"'
#Only one root HAnimJoint is allowed
#USE nodes go here for access by inverse kinematics (IK) engines and other tools
#Top-level HAnimSite/Viewpoint nodes that move with the human center but are unaffected by body animation
#original HAnimHumanoid info='\"authorName=Matthew T. Beitler Joe D. Williams Don Brutzman\" \"authorEmail=HAnim@web3D.org\" \"copyright=none\" \"creationDate=12 May 1999\" \"usageRestrictions=none\" \"humanoidVersion=2.0\" \"height=1.7504\"'
#Only one root HAnimJoint is expected
#USE nodes go here for access by inverse kinematics (IK) engines and other tools
#Top-level HAnimSite/Viewpoint nodes that move with the human center but are unaffected by body animation
#original HAnimHumanoid info='\"authorName=Matthew T. Beitler Joe D. Williams Don Brutzman\" \"authorEmail=HAnim@web3D.org\" \"copyright=none\" \"creationDate=12 May 1999\" \"usageRestrictions=none\" \"humanoidVersion=2.0\" \"height=1.7504\"'
#Only one root HAnimJoint is expected
#USE nodes go here for access by inverse kinematics (IK) engines and other tools
#Top-level HAnimSite/Viewpoint nodes that move with the human center but are unaffected by body animation
#original HAnimHumanoid info='\"authorName=Matthew T. Beitler Joe D. Williams Don Brutzman\" \"authorEmail=HAnim@web3D.org\" \"copyright=none\" \"creationDate=12 May 1999\" \"usageRestrictions=none\" \"humanoidVersion=2.0\" \"height=1.7504\"'
#Only one root HAnimJoint is expected
#USE nodes go here for access by inverse kinematics (IK) engines and other tools
#Top-level HAnimSite/Viewpoint nodes that move with the human center but are unaffected by body animation
#original HAnimHumanoid info='\"authorName=Matthew T. Beitler Joe D. Williams Don Brutzman\" \"authorEmail=HAnim@web3D.org\" \"copyright=none\" \"creationDate=12 May 1999\" \"usageRestrictions=none\" \"humanoidVersion=2.0\" \"height=1.7504\"'
#Only one root HAnimJoint is expected
#USE nodes go here for access by inverse kinematics (IK) engines and other tools
#Top-level HAnimSite/Viewpoint nodes that move with the human center but are unaffected by body animation
#original HAnimHumanoid info='\"authorName=Matthew T. Beitler Joe D. Williams Don Brutzman\" \"authorEmail=HAnim@web3D.org\" \"copyright=none\" \"creationDate=12 May 1999\" \"usageRestrictions=none\" \"humanoidVersion=2.0\" \"height=1.7504\"'
#Only one root HAnimJoint is expected
#USE nodes go here for access by inverse kinematics (IK) engines and other tools
#Top-level HAnimSite/Viewpoint nodes that move with the human center but are unaffected by body animation
#original HAnimHumanoid info='\"authorName=Matthew T. Beitler Joe D. Williams Don Brutzman\" \"authorEmail=HAnim@web3D.org\" \"copyright=none\" \"creationDate=12 May 1999\" \"usageRestrictions=none\" \"humanoidVersion=2.0\" \"height=1.7504\"'
#Only one root HAnimJoint is expected
#USE nodes go here for access by inverse kinematics (IK) engines and other tools
#Top-level HAnimSite/Viewpoint nodes that move with the human center but are unaffected by body animation
#TODO move relevant HAnimSite/Viewpoint pairs into skeleton at appropriate locations, if so also revert containerField to default
#original HAnimHumanoid info='\"authorName=Matthew T. Beitler Joe D. Williams Don Brutzman\" \"authorEmail=HAnim@web3D.org\" \"copyright=none\" \"creationDate=12 May 1999\" \"usageRestrictions=none\" \"humanoidVersion=2.0\" \"height=1.7504\"'
#Only one root HAnimJoint is expected
#USE nodes go here for access by inverse kinematics (IK) engines and other tools
#Top-level HAnimSite/Viewpoint nodes that move with the human center but are unaffected by body animation
#TODO move relevant HAnimSite/Viewpoint pairs into skeleton at appropriate locations, if so also revert containerField to default
#original HAnimHumanoid info='\"authorName=Matthew T. Beitler Joe D. Williams Don Brutzman\" \"authorEmail=HAnim@web3D.org\" \"copyright=none\" \"creationDate=12 May 1999\" \"usageRestrictions=none\" \"humanoidVersion=2.0\" \"height=1.7504\"'
#Only one root HAnimJoint is expected
#USE nodes go here for access by inverse kinematics (IK) engines and other tools
#Top-level HAnimSite/Viewpoint nodes that move with the human center but are unaffected by body animation
#TODO move relevant HAnimSite/Viewpoint pairs into skeleton at appropriate locations, if so also revert containerField to default
#original HAnimHumanoid info='\"authorName=Matthew T. Beitler Joe D. Williams Don Brutzman\" \"authorEmail=HAnim@web3D.org\" \"copyright=none\" \"creationDate=12 May 1999\" \"usageRestrictions=none\" \"humanoidVersion=2.0\" \"height=1.7504\"'
#Only one root HAnimJoint is expected
#USE nodes go here for access by inverse kinematics (IK) engines and other tools
#Top-level HAnimSite/Viewpoint nodes that move with the human center but are unaffected by body animation
#TODO move relevant HAnimSite/Viewpoint pairs into skeleton at appropriate locations, if so also revert containerField to default
#original HAnimHumanoid info='\"authorName=Matthew T. Beitler Joe D. Williams Don Brutzman\" \"authorEmail=HAnim@web3D.org\" \"copyright=none\" \"creationDate=12 May 1999\" \"usageRestrictions=none\" \"humanoidVersion=2.0\" \"height=1.7504\"'
#Only one root HAnimJoint is expected
#USE nodes go here for access by inverse kinematics (IK) engines and other tools
#Top-level HAnimSite/Viewpoint nodes that move with the human center but are unaffected by body animation
#TODO move relevant HAnimSite/Viewpoint pairs into skeleton at appropriate locations, if so also revert containerField to default
#original HAnimHumanoid info='\"authorName=Matthew T. Beitler Joe D. Williams Don Brutzman\" \"authorEmail=HAnim@web3D.org\" \"copyright=none\" \"creationDate=12 May 1999\" \"usageRestrictions=none\" \"humanoidVersion=2.0\" \"height=1.7504\"'
#Only one root HAnimJoint is expected
#USE nodes go here for access by inverse kinematics (IK) engines and other tools
#Top-level HAnimSite/Viewpoint nodes that move with the human center but are unaffected by body animation
#TODO move relevant HAnimSite/Viewpoint pairs into skeleton at appropriate locations, if so also revert containerField to default
#original HAnimHumanoid info='\"authorName=Matthew T. Beitler Joe D. Williams Don Brutzman\" \"authorEmail=HAnim@web3D.org\" \"copyright=none\" \"creationDate=12 May 1999\" \"usageRestrictions=none\" \"humanoidVersion=2.0\" \"height=1.7504\"'
#Only one root HAnimJoint is expected
#USE nodes go here for access by inverse kinematics (IK) engines and other tools
#Top-level HAnimSite/Viewpoint nodes that move with the human center but are unaffected by body animation
#TODO move relevant HAnimSite/Viewpoint pairs into skeleton at appropriate locations, if so also revert containerField to default
#original HAnimHumanoid info='\"authorName=Matthew T. Beitler Joe D. Williams Don Brutzman\" \"authorEmail=HAnim@web3D.org\" \"copyright=none\" \"creationDate=12 May 1999\" \"usageRestrictions=none\" \"humanoidVersion=2.0\" \"height=1.7504\"'
#Only one root HAnimJoint is expected
#USE nodes go here for access by inverse kinematics (IK) engines and other tools
#Top-level HAnimSite/Viewpoint nodes that move with the human center but are unaffected by body animation
#TODO move relevant HAnimSite/Viewpoint pairs into skeleton at appropriate locations, if so also revert containerField to default
#right between the eyes, stationary position not animating except with body itself
MetadataSet44 = x3d.MetadataSet()
MetadataSet44.name = "HAnimHumanoid.info"
MetadataSet44.reference = "https://www.web3d.org/documents/specifications/19774/V2.0/Architecture/ObjectInterfaces.html#Humanoid"
MetadataString45 = x3d.MetadataString()
MetadataString45.name = "authorName"
MetadataString45.value = ["Matthew T. Beitler Joe D. Williams Don Brutzman"]

MetadataSet44.value = MetadataString45
MetadataString46 = x3d.MetadataString()
MetadataString46.name = "authorEmail"
MetadataString46.value = ["HAnim@web3D.org"]

MetadataSet44.value = MetadataString46
MetadataString47 = x3d.MetadataString()
MetadataString47.name = "copyright"
MetadataString47.value = ["none"]

MetadataSet44.value = MetadataString47
MetadataString48 = x3d.MetadataString()
MetadataString48.name = "creationDate"
MetadataString48.value = ["12 May 1999"]

MetadataSet44.value = MetadataString48
MetadataFloat49 = x3d.MetadataFloat()
MetadataFloat49.name = "height"
MetadataFloat49.value = [1.7504]

MetadataSet44.value = MetadataFloat49
MetadataString50 = x3d.MetadataString()
MetadataString50.name = "humanoidVersion"
MetadataString50.value = ["2.0"]

MetadataSet44.value = MetadataString50
MetadataString51 = x3d.MetadataString()
MetadataString51.name = "usageRestrictions"
MetadataString51.value = ["none"]

MetadataSet44.value = MetadataString51

HAnimHumanoid43.metadata = MetadataSet44
HAnimJoint52 = x3d.HAnimJoint()
HAnimJoint52.name = "humanoid_root"
HAnimJoint52.DEF = "hanim_humanoid_root"
HAnimJoint52.center = [0,0.824,0.0277]
HAnimJoint52.ulimit = [0,0,0]
HAnimJoint52.llimit = [0,0,0]
HAnimSegment53 = x3d.HAnimSegment()
HAnimSegment53.name = "sacrum"
HAnimSegment53.DEF = "hanim_sacrum"
#Visualization sphere for <HAnimJoint name='humanoid_root'/> is placed within <HAnimSegment name='sacrum'/>
TouchSensor54 = x3d.TouchSensor()
TouchSensor54.description = "HAnimJoint humanoid_root, HAnimSegment sacrum"

HAnimSegment53.children.append(TouchSensor54)
Transform55 = x3d.Transform()
Transform55.translation = [0,0.824,0.0277]
Shape56 = x3d.Shape()
Shape56.DEF = "HAnimJointShape"
Sphere57 = x3d.Sphere()
Sphere57.radius = 0.006

Shape56.geometry = Sphere57
Appearance58 = x3d.Appearance()
Appearance58.DEF = "HAnimJointAppearance"
Material59 = x3d.Material()
Material59.diffuseColor = [1,0.5,0]
Material59.transparency = 0.5

Appearance58.material = Material59

Shape56.appearance = Appearance58

Transform55.children.append(Shape56)

HAnimSegment53.children.append(Transform55)
#HAnimSegment visualization line from current <HAnimJoint name='humanoid_root'/> to child <HAnimJoint name='sacroiliac'/>
Shape60 = x3d.Shape()
LineSet61 = x3d.LineSet()
LineSet61.vertexCount = [2]
Coordinate62 = x3d.Coordinate()
Coordinate62.point = (0.0000,0.8240,0.0277,0.0000,0.9149,0.0016)

LineSet61.coord = Coordinate62
ColorRGBA63 = x3d.ColorRGBA()
ColorRGBA63.DEF = "HAnimSegmentLineColorRGBA"
ColorRGBA63.color = [1,1,0,1,1,1,0,0.1]

LineSet61.color = ColorRGBA63

Shape60.geometry = LineSet61

HAnimSegment53.children.append(Shape60)
#HAnimSegment visualization line from current <HAnimJoint name='humanoid_root'/> to child <HAnimJoint name='vl5'/>
Shape64 = x3d.Shape()
LineSet65 = x3d.LineSet()
LineSet65.vertexCount = [2]
Coordinate66 = x3d.Coordinate()
Coordinate66.point = (0.0000,0.8240,0.0277,0.0028,1.0568,-0.0776)

LineSet65.coord = Coordinate66
ColorRGBA67 = x3d.ColorRGBA()
ColorRGBA67.USE = "HAnimSegmentLineColorRGBA"

LineSet65.color = ColorRGBA67

Shape64.geometry = LineSet65

HAnimSegment53.children.append(Shape64)

HAnimJoint52.children.append(HAnimSegment53)
HAnimJoint68 = x3d.HAnimJoint()
HAnimJoint68.name = "sacroiliac"
HAnimJoint68.DEF = "hanim_sacroiliac"
HAnimJoint68.center = [0,0.9149,0.0016]
HAnimJoint68.ulimit = [0,0,0]
HAnimJoint68.llimit = [0,0,0]
HAnimSegment69 = x3d.HAnimSegment()
HAnimSegment69.name = "pelvis"
HAnimSegment69.DEF = "hanim_pelvis"
#Visualization sphere for <HAnimJoint name='sacroiliac'/> is placed within <HAnimSegment name='pelvis'/>
TouchSensor70 = x3d.TouchSensor()
TouchSensor70.description = "HAnimJoint sacroiliac, HAnimSegment pelvis"

HAnimSegment69.children.append(TouchSensor70)
Transform71 = x3d.Transform()
Transform71.translation = [0,0.9149,0.0016]
Shape72 = x3d.Shape()
Shape72.USE = "HAnimJointShape"

Transform71.children.append(Shape72)

HAnimSegment69.children.append(Transform71)
#HAnimSegment visualization line from current <HAnimJoint name='sacroiliac'/> to child <HAnimJoint name='l_hip'/>
Shape73 = x3d.Shape()
LineSet74 = x3d.LineSet()
LineSet74.vertexCount = [2]
Coordinate75 = x3d.Coordinate()
Coordinate75.point = (0.0000,0.9149,0.0016,0.0961,0.9124,-0.0001)

LineSet74.coord = Coordinate75
ColorRGBA76 = x3d.ColorRGBA()
ColorRGBA76.USE = "HAnimSegmentLineColorRGBA"

LineSet74.color = ColorRGBA76

Shape73.geometry = LineSet74

HAnimSegment69.children.append(Shape73)
#HAnimSegment visualization line from current <HAnimJoint name='sacroiliac'/> to child <HAnimJoint name='r_hip'/>
Shape77 = x3d.Shape()
LineSet78 = x3d.LineSet()
LineSet78.vertexCount = [2]
Coordinate79 = x3d.Coordinate()
Coordinate79.point = (0.0000,0.9149,0.0016,-0.0961,0.9124,-0.0001)

LineSet78.coord = Coordinate79
ColorRGBA80 = x3d.ColorRGBA()
ColorRGBA80.USE = "HAnimSegmentLineColorRGBA"

LineSet78.color = ColorRGBA80

Shape77.geometry = LineSet78

HAnimSegment69.children.append(Shape77)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='sacroiliac'/> to <HAnimSite name='r_iliocristale_pt'/>
Shape81 = x3d.Shape()
LineSet82 = x3d.LineSet()
LineSet82.vertexCount = [2]
Coordinate83 = x3d.Coordinate()
Coordinate83.point = (0.0000,0.9149,0.0016,-0.1525,1.0628,0.0035)

LineSet82.coord = Coordinate83
ColorRGBA84 = x3d.ColorRGBA()
ColorRGBA84.DEF = "HAnimSiteLineColorRGBA"
ColorRGBA84.color = [1,0,0,1,1,0,0,0.1]

LineSet82.color = ColorRGBA84

Shape81.geometry = LineSet82

HAnimSegment69.children.append(Shape81)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='sacroiliac'/> to <HAnimSite name='r_trochanterion_pt'/>
Shape85 = x3d.Shape()
LineSet86 = x3d.LineSet()
LineSet86.vertexCount = [2]
Coordinate87 = x3d.Coordinate()
Coordinate87.point = (0.0000,0.9149,0.0016,-0.1689,0.8419,0.0352)

LineSet86.coord = Coordinate87
ColorRGBA88 = x3d.ColorRGBA()
ColorRGBA88.USE = "HAnimSiteLineColorRGBA"

LineSet86.color = ColorRGBA88

Shape85.geometry = LineSet86

HAnimSegment69.children.append(Shape85)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='sacroiliac'/> to <HAnimSite name='l_iliocristale_pt'/>
Shape89 = x3d.Shape()
LineSet90 = x3d.LineSet()
LineSet90.vertexCount = [2]
Coordinate91 = x3d.Coordinate()
Coordinate91.point = (0.0000,0.9149,0.0016,0.1612,1.0537,0.0008)

LineSet90.coord = Coordinate91
ColorRGBA92 = x3d.ColorRGBA()
ColorRGBA92.USE = "HAnimSiteLineColorRGBA"

LineSet90.color = ColorRGBA92

Shape89.geometry = LineSet90

HAnimSegment69.children.append(Shape89)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='sacroiliac'/> to <HAnimSite name='l_trochanterion_pt'/>
Shape93 = x3d.Shape()
LineSet94 = x3d.LineSet()
LineSet94.vertexCount = [2]
Coordinate95 = x3d.Coordinate()
Coordinate95.point = (0.0000,0.9149,0.0016,0.1677,0.8336,0.0303)

LineSet94.coord = Coordinate95
ColorRGBA96 = x3d.ColorRGBA()
ColorRGBA96.USE = "HAnimSiteLineColorRGBA"

LineSet94.color = ColorRGBA96

Shape93.geometry = LineSet94

HAnimSegment69.children.append(Shape93)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='sacroiliac'/> to <HAnimSite name='r_asis_pt'/>
Shape97 = x3d.Shape()
LineSet98 = x3d.LineSet()
LineSet98.vertexCount = [2]
Coordinate99 = x3d.Coordinate()
Coordinate99.point = (0.0000,0.9149,0.0016,-0.0887,1.0021,0.1112)

LineSet98.coord = Coordinate99
ColorRGBA100 = x3d.ColorRGBA()
ColorRGBA100.USE = "HAnimSiteLineColorRGBA"

LineSet98.color = ColorRGBA100

Shape97.geometry = LineSet98

HAnimSegment69.children.append(Shape97)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='sacroiliac'/> to <HAnimSite name='l_asis_pt'/>
Shape101 = x3d.Shape()
LineSet102 = x3d.LineSet()
LineSet102.vertexCount = [2]
Coordinate103 = x3d.Coordinate()
Coordinate103.point = (0.0000,0.9149,0.0016,0.0925,0.9983,0.1052)

LineSet102.coord = Coordinate103
ColorRGBA104 = x3d.ColorRGBA()
ColorRGBA104.USE = "HAnimSiteLineColorRGBA"

LineSet102.color = ColorRGBA104

Shape101.geometry = LineSet102

HAnimSegment69.children.append(Shape101)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='sacroiliac'/> to <HAnimSite name='r_psis_pt'/>
Shape105 = x3d.Shape()
LineSet106 = x3d.LineSet()
LineSet106.vertexCount = [2]
Coordinate107 = x3d.Coordinate()
Coordinate107.point = (0.0000,0.9149,0.0016,-0.0716,1.0190,-0.1138)

LineSet106.coord = Coordinate107
ColorRGBA108 = x3d.ColorRGBA()
ColorRGBA108.USE = "HAnimSiteLineColorRGBA"

LineSet106.color = ColorRGBA108

Shape105.geometry = LineSet106

HAnimSegment69.children.append(Shape105)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='sacroiliac'/> to <HAnimSite name='l_psis_pt'/>
Shape109 = x3d.Shape()
LineSet110 = x3d.LineSet()
LineSet110.vertexCount = [2]
Coordinate111 = x3d.Coordinate()
Coordinate111.point = (0.0000,0.9149,0.0016,0.0774,1.0190,-0.1151)

LineSet110.coord = Coordinate111
ColorRGBA112 = x3d.ColorRGBA()
ColorRGBA112.USE = "HAnimSiteLineColorRGBA"

LineSet110.color = ColorRGBA112

Shape109.geometry = LineSet110

HAnimSegment69.children.append(Shape109)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='sacroiliac'/> to <HAnimSite name='crotch_pt'/>
Shape113 = x3d.Shape()
LineSet114 = x3d.LineSet()
LineSet114.vertexCount = [2]
Coordinate115 = x3d.Coordinate()
Coordinate115.point = (0.0000,0.9149,0.0016,0.0034,0.8266,0.0257)

LineSet114.coord = Coordinate115
ColorRGBA116 = x3d.ColorRGBA()
ColorRGBA116.USE = "HAnimSiteLineColorRGBA"

LineSet114.color = ColorRGBA116

Shape113.geometry = LineSet114

HAnimSegment69.children.append(Shape113)
HAnimSite117 = x3d.HAnimSite()
HAnimSite117.name = "r_iliocristale_pt"
HAnimSite117.DEF = "hanim_r_iliocristale_pt"
HAnimSite117.translation = [-0.1525,1.0628,0.0035]
#HAnimSite visualization shape
TouchSensor118 = x3d.TouchSensor()
TouchSensor118.description = "HAnimSite r_iliocristale_pt"

HAnimSite117.children.append(TouchSensor118)
Shape119 = x3d.Shape()
Shape119.DEF = "HAnimSiteShape"
IndexedFaceSet120 = x3d.IndexedFaceSet()
IndexedFaceSet120.DEF = "DiamondIFS"
IndexedFaceSet120.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet120.creaseAngle = 0.5
IndexedFaceSet120.solid = False
Coordinate121 = x3d.Coordinate()
Coordinate121.point = (0.0000,0.0080,0.0000,-0.0080,0.0000,0.0000,0.0000,0.0000,0.0080,0.0080,0.0000,0.0000,0.0000,0.0000,-0.0080,0.0000,-0.0080,0.0000)

IndexedFaceSet120.coord = Coordinate121

Shape119.geometry = IndexedFaceSet120
Appearance122 = x3d.Appearance()
Material123 = x3d.Material()
Material123.diffuseColor = [1,0,0]

Appearance122.material = Material123

Shape119.appearance = Appearance122

HAnimSite117.children.append(Shape119)

HAnimSegment69.children.append(HAnimSite117)
HAnimSite124 = x3d.HAnimSite()
HAnimSite124.name = "r_trochanterion_pt"
HAnimSite124.DEF = "hanim_r_trochanterion_pt"
HAnimSite124.translation = [-0.1689,0.8419,0.0352]
#HAnimSite visualization shape
TouchSensor125 = x3d.TouchSensor()
TouchSensor125.description = "HAnimSite r_trochanterion_pt"

HAnimSite124.children.append(TouchSensor125)
Shape126 = x3d.Shape()
Shape126.USE = "HAnimSiteShape"

HAnimSite124.children.append(Shape126)

HAnimSegment69.children.append(HAnimSite124)
HAnimSite127 = x3d.HAnimSite()
HAnimSite127.name = "l_iliocristale_pt"
HAnimSite127.DEF = "hanim_l_iliocristale_pt"
HAnimSite127.translation = [0.1612,1.0537,0.0008]
#HAnimSite visualization shape
TouchSensor128 = x3d.TouchSensor()
TouchSensor128.description = "HAnimSite l_iliocristale_pt"

HAnimSite127.children.append(TouchSensor128)
Shape129 = x3d.Shape()
Shape129.USE = "HAnimSiteShape"

HAnimSite127.children.append(Shape129)

HAnimSegment69.children.append(HAnimSite127)
HAnimSite130 = x3d.HAnimSite()
HAnimSite130.name = "l_trochanterion_pt"
HAnimSite130.DEF = "hanim_l_trochanterion_pt"
HAnimSite130.translation = [0.1677,0.8336,0.0303]
#HAnimSite visualization shape
TouchSensor131 = x3d.TouchSensor()
TouchSensor131.description = "HAnimSite l_trochanterion_pt"

HAnimSite130.children.append(TouchSensor131)
Shape132 = x3d.Shape()
Shape132.USE = "HAnimSiteShape"

HAnimSite130.children.append(Shape132)

HAnimSegment69.children.append(HAnimSite130)
HAnimSite133 = x3d.HAnimSite()
HAnimSite133.name = "r_asis_pt"
HAnimSite133.DEF = "hanim_r_asis_pt"
HAnimSite133.translation = [-0.0887,1.0021,0.1112]
#HAnimSite visualization shape
TouchSensor134 = x3d.TouchSensor()
TouchSensor134.description = "HAnimSite r_asis_pt"

HAnimSite133.children.append(TouchSensor134)
Shape135 = x3d.Shape()
Shape135.USE = "HAnimSiteShape"

HAnimSite133.children.append(Shape135)

HAnimSegment69.children.append(HAnimSite133)
HAnimSite136 = x3d.HAnimSite()
HAnimSite136.name = "l_asis_pt"
HAnimSite136.DEF = "hanim_l_asis_pt"
HAnimSite136.translation = [0.0925,0.9983,0.1052]
#HAnimSite visualization shape
TouchSensor137 = x3d.TouchSensor()
TouchSensor137.description = "HAnimSite l_asis_pt"

HAnimSite136.children.append(TouchSensor137)
Shape138 = x3d.Shape()
Shape138.USE = "HAnimSiteShape"

HAnimSite136.children.append(Shape138)

HAnimSegment69.children.append(HAnimSite136)
HAnimSite139 = x3d.HAnimSite()
HAnimSite139.name = "r_psis_pt"
HAnimSite139.DEF = "hanim_r_psis_pt"
HAnimSite139.translation = [-0.0716,1.019,-0.1138]
#HAnimSite visualization shape
TouchSensor140 = x3d.TouchSensor()
TouchSensor140.description = "HAnimSite r_psis_pt"

HAnimSite139.children.append(TouchSensor140)
Shape141 = x3d.Shape()
Shape141.USE = "HAnimSiteShape"

HAnimSite139.children.append(Shape141)

HAnimSegment69.children.append(HAnimSite139)
HAnimSite142 = x3d.HAnimSite()
HAnimSite142.name = "l_psis_pt"
HAnimSite142.DEF = "hanim_l_psis_pt"
HAnimSite142.translation = [0.0774,1.019,-0.1151]
#HAnimSite visualization shape
TouchSensor143 = x3d.TouchSensor()
TouchSensor143.description = "HAnimSite l_psis_pt"

HAnimSite142.children.append(TouchSensor143)
Shape144 = x3d.Shape()
Shape144.USE = "HAnimSiteShape"

HAnimSite142.children.append(Shape144)

HAnimSegment69.children.append(HAnimSite142)
HAnimSite145 = x3d.HAnimSite()
HAnimSite145.name = "crotch_pt"
HAnimSite145.DEF = "hanim_crotch_pt"
HAnimSite145.translation = [0.0034,0.8266,0.0257]
#HAnimSite visualization shape
TouchSensor146 = x3d.TouchSensor()
TouchSensor146.description = "HAnimSite crotch_pt"

HAnimSite145.children.append(TouchSensor146)
Shape147 = x3d.Shape()
Shape147.USE = "HAnimSiteShape"

HAnimSite145.children.append(Shape147)

HAnimSegment69.children.append(HAnimSite145)

HAnimJoint68.children.append(HAnimSegment69)
HAnimJoint148 = x3d.HAnimJoint()
HAnimJoint148.name = "l_hip"
HAnimJoint148.DEF = "hanim_l_hip"
HAnimJoint148.center = [0.0961,0.9124,-0.0001]
HAnimJoint148.ulimit = [0,0,0]
HAnimJoint148.llimit = [0,0,0]
HAnimSegment149 = x3d.HAnimSegment()
HAnimSegment149.name = "l_thigh"
HAnimSegment149.DEF = "hanim_l_thigh"
#Visualization sphere for <HAnimJoint name='l_hip'/> is placed within <HAnimSegment name='l_thigh'/>
TouchSensor150 = x3d.TouchSensor()
TouchSensor150.description = "HAnimJoint l_hip, HAnimSegment l_thigh"

HAnimSegment149.children.append(TouchSensor150)
Transform151 = x3d.Transform()
Transform151.translation = [0.0961,0.9124,-0.0001]
Shape152 = x3d.Shape()
Shape152.USE = "HAnimJointShape"

Transform151.children.append(Shape152)

HAnimSegment149.children.append(Transform151)
#HAnimSegment visualization line from current <HAnimJoint name='l_hip'/> to child <HAnimJoint name='l_knee'/>
Shape153 = x3d.Shape()
LineSet154 = x3d.LineSet()
LineSet154.vertexCount = [2]
Coordinate155 = x3d.Coordinate()
Coordinate155.point = (0.0961,0.9124,-0.0001,0.1040,0.4867,0.0308)

LineSet154.coord = Coordinate155
ColorRGBA156 = x3d.ColorRGBA()
ColorRGBA156.USE = "HAnimSegmentLineColorRGBA"

LineSet154.color = ColorRGBA156

Shape153.geometry = LineSet154

HAnimSegment149.children.append(Shape153)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_hip'/> to <HAnimSite name='l_knee_crease_pt'/>
Shape157 = x3d.Shape()
LineSet158 = x3d.LineSet()
LineSet158.vertexCount = [2]
Coordinate159 = x3d.Coordinate()
Coordinate159.point = (0.0961,0.9124,-0.0001,0.0993,0.4881,-0.0309)

LineSet158.coord = Coordinate159
ColorRGBA160 = x3d.ColorRGBA()
ColorRGBA160.USE = "HAnimSiteLineColorRGBA"

LineSet158.color = ColorRGBA160

Shape157.geometry = LineSet158

HAnimSegment149.children.append(Shape157)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_hip'/> to <HAnimSite name='l_femoral_lateral_epicn_pt'/>
Shape161 = x3d.Shape()
LineSet162 = x3d.LineSet()
LineSet162.vertexCount = [2]
Coordinate163 = x3d.Coordinate()
Coordinate163.point = (0.0961,0.9124,-0.0001,0.1598,0.4967,0.0297)

LineSet162.coord = Coordinate163
ColorRGBA164 = x3d.ColorRGBA()
ColorRGBA164.USE = "HAnimSiteLineColorRGBA"

LineSet162.color = ColorRGBA164

Shape161.geometry = LineSet162

HAnimSegment149.children.append(Shape161)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_hip'/> to <HAnimSite name='l_femoral_medial_epicn_pt'/>
Shape165 = x3d.Shape()
LineSet166 = x3d.LineSet()
LineSet166.vertexCount = [2]
Coordinate167 = x3d.Coordinate()
Coordinate167.point = (0.0961,0.9124,-0.0001,0.0398,0.4946,0.0303)

LineSet166.coord = Coordinate167
ColorRGBA168 = x3d.ColorRGBA()
ColorRGBA168.USE = "HAnimSiteLineColorRGBA"

LineSet166.color = ColorRGBA168

Shape165.geometry = LineSet166

HAnimSegment149.children.append(Shape165)
HAnimSite169 = x3d.HAnimSite()
HAnimSite169.name = "l_knee_crease_pt"
HAnimSite169.DEF = "hanim_l_knee_crease_pt"
HAnimSite169.translation = [0.0993,0.4881,-0.0309]
#HAnimSite visualization shape
TouchSensor170 = x3d.TouchSensor()
TouchSensor170.description = "HAnimSite l_knee_crease_pt"

HAnimSite169.children.append(TouchSensor170)
Shape171 = x3d.Shape()
Shape171.USE = "HAnimSiteShape"

HAnimSite169.children.append(Shape171)

HAnimSegment149.children.append(HAnimSite169)
HAnimSite172 = x3d.HAnimSite()
HAnimSite172.name = "l_femoral_lateral_epicondyle_pt"
HAnimSite172.DEF = "hanim_l_femoral_lateral_epicondyle_pt"
HAnimSite172.translation = [0.1598,0.4967,0.0297]
#HAnimSite visualization shape
TouchSensor173 = x3d.TouchSensor()
TouchSensor173.description = "HAnimSite l_femoral_lateral_epicn_pt"

HAnimSite172.children.append(TouchSensor173)
Shape174 = x3d.Shape()
Shape174.USE = "HAnimSiteShape"

HAnimSite172.children.append(Shape174)

HAnimSegment149.children.append(HAnimSite172)
HAnimSite175 = x3d.HAnimSite()
HAnimSite175.name = "l_femoral_medial_epicondyle_pt"
HAnimSite175.DEF = "hanim_l_femoral_medial_epicondyle_pt"
HAnimSite175.translation = [0.0398,0.4946,0.0303]
#HAnimSite visualization shape
TouchSensor176 = x3d.TouchSensor()
TouchSensor176.description = "HAnimSite l_femoral_medial_epicn_pt"

HAnimSite175.children.append(TouchSensor176)
Shape177 = x3d.Shape()
Shape177.USE = "HAnimSiteShape"

HAnimSite175.children.append(Shape177)

HAnimSegment149.children.append(HAnimSite175)

HAnimJoint148.children.append(HAnimSegment149)
HAnimJoint178 = x3d.HAnimJoint()
HAnimJoint178.name = "l_knee"
HAnimJoint178.DEF = "hanim_l_knee"
HAnimJoint178.center = [0.104,0.4867,0.0308]
HAnimJoint178.ulimit = [0,0,0]
HAnimJoint178.llimit = [0,0,0]
HAnimSegment179 = x3d.HAnimSegment()
HAnimSegment179.name = "l_calf"
HAnimSegment179.DEF = "hanim_l_calf"
#Visualization sphere for <HAnimJoint name='l_knee'/> is placed within <HAnimSegment name='l_calf'/>
TouchSensor180 = x3d.TouchSensor()
TouchSensor180.description = "HAnimJoint l_knee, HAnimSegment l_calf"

HAnimSegment179.children.append(TouchSensor180)
Transform181 = x3d.Transform()
Transform181.translation = [0.104,0.4867,0.0308]
Shape182 = x3d.Shape()
Shape182.USE = "HAnimJointShape"

Transform181.children.append(Shape182)

HAnimSegment179.children.append(Transform181)
#HAnimSegment visualization line from current <HAnimJoint name='l_knee'/> to child <HAnimJoint name='l_talocrural'/>
Shape183 = x3d.Shape()
LineSet184 = x3d.LineSet()
LineSet184.vertexCount = [2]
Coordinate185 = x3d.Coordinate()
Coordinate185.point = (0.1040,0.4867,0.0308,0.1101,0.0656,-0.0736)

LineSet184.coord = Coordinate185
ColorRGBA186 = x3d.ColorRGBA()
ColorRGBA186.USE = "HAnimSegmentLineColorRGBA"

LineSet184.color = ColorRGBA186

Shape183.geometry = LineSet184

HAnimSegment179.children.append(Shape183)

HAnimJoint178.children.append(HAnimSegment179)
HAnimJoint187 = x3d.HAnimJoint()
HAnimJoint187.name = "l_talocrural"
HAnimJoint187.DEF = "hanim_l_talocrural"
HAnimJoint187.center = [0.1101,0.0656,-0.0736]
HAnimJoint187.ulimit = [0,0,0]
HAnimJoint187.llimit = [0,0,0]
HAnimSegment188 = x3d.HAnimSegment()
HAnimSegment188.name = "l_talus"
HAnimSegment188.DEF = "hanim_l_talus"
#Visualization sphere for <HAnimJoint name='l_talocrural'/> is placed within <HAnimSegment name='l_talus'/>
TouchSensor189 = x3d.TouchSensor()
TouchSensor189.description = "HAnimJoint l_talocrural, HAnimSegment l_talus"

HAnimSegment188.children.append(TouchSensor189)
Transform190 = x3d.Transform()
Transform190.translation = [0.1101,0.0656,-0.0736]
Shape191 = x3d.Shape()
Shape191.USE = "HAnimJointShape"

Transform190.children.append(Shape191)

HAnimSegment188.children.append(Transform190)
#HAnimSegment visualization line from current <HAnimJoint name='l_talocrural'/> to child <HAnimJoint name='l_tarsometatarsal_2'/>
Shape192 = x3d.Shape()
LineSet193 = x3d.LineSet()
LineSet193.vertexCount = [2]
Coordinate194 = x3d.Coordinate()
Coordinate194.point = (0.1101,0.0656,-0.0736,0.1086,0.0001,-0.0368)

LineSet193.coord = Coordinate194
ColorRGBA195 = x3d.ColorRGBA()
ColorRGBA195.USE = "HAnimSegmentLineColorRGBA"

LineSet193.color = ColorRGBA195

Shape192.geometry = LineSet193

HAnimSegment188.children.append(Shape192)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_talocrural'/> to <HAnimSite name='l_lateral_malleolus_pt'/>
Shape196 = x3d.Shape()
LineSet197 = x3d.LineSet()
LineSet197.vertexCount = [2]
Coordinate198 = x3d.Coordinate()
Coordinate198.point = (0.1101,0.0656,-0.0736,0.1308,0.0597,-0.1032)

LineSet197.coord = Coordinate198
ColorRGBA199 = x3d.ColorRGBA()
ColorRGBA199.USE = "HAnimSiteLineColorRGBA"

LineSet197.color = ColorRGBA199

Shape196.geometry = LineSet197

HAnimSegment188.children.append(Shape196)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_talocrural'/> to <HAnimSite name='l_medial_malleolus_pt'/>
Shape200 = x3d.Shape()
LineSet201 = x3d.LineSet()
LineSet201.vertexCount = [2]
Coordinate202 = x3d.Coordinate()
Coordinate202.point = (0.1101,0.0656,-0.0736,0.0890,0.0716,-0.0881)

LineSet201.coord = Coordinate202
ColorRGBA203 = x3d.ColorRGBA()
ColorRGBA203.USE = "HAnimSiteLineColorRGBA"

LineSet201.color = ColorRGBA203

Shape200.geometry = LineSet201

HAnimSegment188.children.append(Shape200)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_talocrural'/> to <HAnimSite name='l_sphyrion_pt'/>
Shape204 = x3d.Shape()
LineSet205 = x3d.LineSet()
LineSet205.vertexCount = [2]
Coordinate206 = x3d.Coordinate()
Coordinate206.point = (0.1101,0.0656,-0.0736,0.0890,0.0575,-0.0943)

LineSet205.coord = Coordinate206
ColorRGBA207 = x3d.ColorRGBA()
ColorRGBA207.USE = "HAnimSiteLineColorRGBA"

LineSet205.color = ColorRGBA207

Shape204.geometry = LineSet205

HAnimSegment188.children.append(Shape204)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_talocrural'/> to <HAnimSite name='l_calcaneous_post_pt'/>
Shape208 = x3d.Shape()
LineSet209 = x3d.LineSet()
LineSet209.vertexCount = [2]
Coordinate210 = x3d.Coordinate()
Coordinate210.point = (0.1101,0.0656,-0.0736,0.0974,0.0259,-0.1171)

LineSet209.coord = Coordinate210
ColorRGBA211 = x3d.ColorRGBA()
ColorRGBA211.USE = "HAnimSiteLineColorRGBA"

LineSet209.color = ColorRGBA211

Shape208.geometry = LineSet209

HAnimSegment188.children.append(Shape208)
HAnimSite212 = x3d.HAnimSite()
HAnimSite212.name = "l_lateral_malleolus_pt"
HAnimSite212.DEF = "hanim_l_lateral_malleolus_pt"
HAnimSite212.translation = [0.1308,0.0597,-0.1032]
#HAnimSite visualization shape
TouchSensor213 = x3d.TouchSensor()
TouchSensor213.description = "HAnimSite l_lateral_malleolus_pt"

HAnimSite212.children.append(TouchSensor213)
Shape214 = x3d.Shape()
Shape214.USE = "HAnimSiteShape"

HAnimSite212.children.append(Shape214)

HAnimSegment188.children.append(HAnimSite212)
HAnimSite215 = x3d.HAnimSite()
HAnimSite215.name = "l_medial_malleolus_pt"
HAnimSite215.DEF = "hanim_l_medial_malleolus_pt"
HAnimSite215.translation = [0.089,0.0716,-0.0881]
#HAnimSite visualization shape
TouchSensor216 = x3d.TouchSensor()
TouchSensor216.description = "HAnimSite l_medial_malleolus_pt"

HAnimSite215.children.append(TouchSensor216)
Shape217 = x3d.Shape()
Shape217.USE = "HAnimSiteShape"

HAnimSite215.children.append(Shape217)

HAnimSegment188.children.append(HAnimSite215)
HAnimSite218 = x3d.HAnimSite()
HAnimSite218.name = "l_sphyrion_pt"
HAnimSite218.DEF = "hanim_l_sphyrion_pt"
HAnimSite218.translation = [0.089,0.0575,-0.0943]
#HAnimSite visualization shape
TouchSensor219 = x3d.TouchSensor()
TouchSensor219.description = "HAnimSite l_sphyrion_pt"

HAnimSite218.children.append(TouchSensor219)
Shape220 = x3d.Shape()
Shape220.USE = "HAnimSiteShape"

HAnimSite218.children.append(Shape220)

HAnimSegment188.children.append(HAnimSite218)
HAnimSite221 = x3d.HAnimSite()
HAnimSite221.name = "l_calcaneus_posterior_pt"
HAnimSite221.DEF = "hanim_l_calcaneus_posterior_pt"
HAnimSite221.translation = [0.0974,0.0259,-0.1171]
#HAnimSite visualization shape
TouchSensor222 = x3d.TouchSensor()
TouchSensor222.description = "HAnimSite l_calcaneous_post_pt"

HAnimSite221.children.append(TouchSensor222)
Shape223 = x3d.Shape()
Shape223.USE = "HAnimSiteShape"

HAnimSite221.children.append(Shape223)

HAnimSegment188.children.append(HAnimSite221)

HAnimJoint187.children.append(HAnimSegment188)
HAnimJoint224 = x3d.HAnimJoint()
HAnimJoint224.name = "l_tarsometatarsal_2"
HAnimJoint224.DEF = "hanim_l_tarsometatarsal_2"
HAnimJoint224.center = [0.1086,0.0001,-0.0368]
HAnimJoint224.ulimit = [0,0,0]
HAnimJoint224.llimit = [0,0,0]
HAnimSegment225 = x3d.HAnimSegment()
HAnimSegment225.name = "l_metatarsal_2"
HAnimSegment225.DEF = "hanim_l_metatarsal_2"
#Visualization sphere for <HAnimJoint name='l_tarsometatarsal_2'/> is placed within <HAnimSegment name='l_metatarsal_2'/>
TouchSensor226 = x3d.TouchSensor()
TouchSensor226.description = "HAnimJoint l_tarsometatarsal_2, HAnimSegment l_metatarsal_2"

HAnimSegment225.children.append(TouchSensor226)
Transform227 = x3d.Transform()
Transform227.translation = [0.1086,0.0001,-0.0368]
Shape228 = x3d.Shape()
Shape228.USE = "HAnimJointShape"

Transform227.children.append(Shape228)

HAnimSegment225.children.append(Transform227)
#HAnimSegment visualization line from current <HAnimJoint name='l_tarsometatarsal_2'/> to child <HAnimJoint name='l_metatarsophalangeal_2'/>
Shape229 = x3d.Shape()
LineSet230 = x3d.LineSet()
LineSet230.vertexCount = [2]
Coordinate231 = x3d.Coordinate()
Coordinate231.point = (0.1086,0.0001,-0.0368,0.1086,0.0001,0.0368)

LineSet230.coord = Coordinate231
ColorRGBA232 = x3d.ColorRGBA()
ColorRGBA232.USE = "HAnimSegmentLineColorRGBA"

LineSet230.color = ColorRGBA232

Shape229.geometry = LineSet230

HAnimSegment225.children.append(Shape229)

HAnimJoint224.children.append(HAnimSegment225)
HAnimJoint233 = x3d.HAnimJoint()
HAnimJoint233.name = "l_metatarsophalangeal_2"
HAnimJoint233.DEF = "hanim_l_metatarsophalangeal_2"
HAnimJoint233.center = [0.1086,0.0001,0.0368]
HAnimJoint233.ulimit = [0,0,0]
HAnimJoint233.llimit = [0,0,0]
HAnimSegment234 = x3d.HAnimSegment()
HAnimSegment234.name = "l_tarsal_proximal_phalanx_2"
HAnimSegment234.DEF = "hanim_l_tarsal_proximal_phalanx_2"
#Visualization sphere for <HAnimJoint name='l_metatarsophalangeal_2'/> is placed within <HAnimSegment name='l_tarsal_proximal_phalanx_2'/>
TouchSensor235 = x3d.TouchSensor()
TouchSensor235.description = "HAnimJoint l_metatarsophalangeal_2, HAnimSegment l_tarsal_proximal_phalanx_2"

HAnimSegment234.children.append(TouchSensor235)
Transform236 = x3d.Transform()
Transform236.translation = [0.1086,0.0001,0.0368]
Shape237 = x3d.Shape()
Shape237.USE = "HAnimJointShape"

Transform236.children.append(Shape237)

HAnimSegment234.children.append(Transform236)
#HAnimSegment visualization line from current <HAnimJoint name='l_metatarsophalangeal_2'/> to child <HAnimJoint name='l_tarsal_distal_interphalangeal_2'/>
Shape238 = x3d.Shape()
LineSet239 = x3d.LineSet()
LineSet239.vertexCount = [2]
Coordinate240 = x3d.Coordinate()
Coordinate240.point = (0.1086,0.0001,0.0368,0.1086,0.0000,0.0762)

LineSet239.coord = Coordinate240
ColorRGBA241 = x3d.ColorRGBA()
ColorRGBA241.USE = "HAnimSegmentLineColorRGBA"

LineSet239.color = ColorRGBA241

Shape238.geometry = LineSet239

HAnimSegment234.children.append(Shape238)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_metatarsophalangeal_2'/> to <HAnimSite name='l_metatarsal_pha1_pt'/>
Shape242 = x3d.Shape()
LineSet243 = x3d.LineSet()
LineSet243.vertexCount = [2]
Coordinate244 = x3d.Coordinate()
Coordinate244.point = (0.1086,0.0001,0.0368,0.0816,0.0232,0.0106)

LineSet243.coord = Coordinate244
ColorRGBA245 = x3d.ColorRGBA()
ColorRGBA245.USE = "HAnimSiteLineColorRGBA"

LineSet243.color = ColorRGBA245

Shape242.geometry = LineSet243

HAnimSegment234.children.append(Shape242)
HAnimSite246 = x3d.HAnimSite()
HAnimSite246.name = "l_metatarsal_phalanx_1_pt"
HAnimSite246.DEF = "hanim_l_metatarsal_phalanx_1_pt"
HAnimSite246.translation = [0.0816,0.0232,0.0106]
#HAnimSite visualization shape
TouchSensor247 = x3d.TouchSensor()
TouchSensor247.description = "HAnimSite l_metatarsal_pha1_pt"

HAnimSite246.children.append(TouchSensor247)
Shape248 = x3d.Shape()
Shape248.USE = "HAnimSiteShape"

HAnimSite246.children.append(Shape248)

HAnimSegment234.children.append(HAnimSite246)

HAnimJoint233.children.append(HAnimSegment234)
HAnimJoint249 = x3d.HAnimJoint()
HAnimJoint249.name = "l_tarsal_distal_interphalangeal_2"
HAnimJoint249.DEF = "hanim_l_tarsal_distal_interphalangeal_2"
HAnimJoint249.center = [0.1086,0,0.0762]
HAnimJoint249.ulimit = [0,0,0]
HAnimJoint249.llimit = [0,0,0]
HAnimSegment250 = x3d.HAnimSegment()
HAnimSegment250.name = "l_tarsal_distal_phalanx_2"
HAnimSegment250.DEF = "hanim_l_tarsal_distal_phalanx_2"
#Visualization sphere for <HAnimJoint name='l_tarsal_distal_interphalangeal_2'/> is placed within <HAnimSegment name='l_tarsal_distal_phalanx_2'/>
TouchSensor251 = x3d.TouchSensor()
TouchSensor251.description = "HAnimJoint l_tarsal_distal_interphalangeal_2, HAnimSegment l_tarsal_distal_phalanx_2"

HAnimSegment250.children.append(TouchSensor251)
Transform252 = x3d.Transform()
Transform252.translation = [0.1086,0,0.0762]
Shape253 = x3d.Shape()
Shape253.USE = "HAnimJointShape"

Transform252.children.append(Shape253)

HAnimSegment250.children.append(Transform252)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_tarsal_distal_interphalangeal_2'/> to <HAnimSite name='l_forefoot_tip'/>
Shape254 = x3d.Shape()
LineSet255 = x3d.LineSet()
LineSet255.vertexCount = [2]
Coordinate256 = x3d.Coordinate()
Coordinate256.point = (0.1086,0.0000,0.0762,0.1354,0.0016,0.1476)

LineSet255.coord = Coordinate256
ColorRGBA257 = x3d.ColorRGBA()
ColorRGBA257.USE = "HAnimSiteLineColorRGBA"

LineSet255.color = ColorRGBA257

Shape254.geometry = LineSet255

HAnimSegment250.children.append(Shape254)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_tarsal_distal_interphalangeal_2'/> to <HAnimSite name='l_metatarsal_pha5_pt'/>
Shape258 = x3d.Shape()
LineSet259 = x3d.LineSet()
LineSet259.vertexCount = [2]
Coordinate260 = x3d.Coordinate()
Coordinate260.point = (0.1086,0.0000,0.0762,0.1825,0.0070,0.0928)

LineSet259.coord = Coordinate260
ColorRGBA261 = x3d.ColorRGBA()
ColorRGBA261.USE = "HAnimSiteLineColorRGBA"

LineSet259.color = ColorRGBA261

Shape258.geometry = LineSet259

HAnimSegment250.children.append(Shape258)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_tarsal_distal_interphalangeal_2'/> to <HAnimSite name='l_digit2_pt'/>
Shape262 = x3d.Shape()
LineSet263 = x3d.LineSet()
LineSet263.vertexCount = [2]
Coordinate264 = x3d.Coordinate()
Coordinate264.point = (0.1086,0.0000,0.0762,0.1195,0.0079,0.1433)

LineSet263.coord = Coordinate264
ColorRGBA265 = x3d.ColorRGBA()
ColorRGBA265.USE = "HAnimSiteLineColorRGBA"

LineSet263.color = ColorRGBA265

Shape262.geometry = LineSet263

HAnimSegment250.children.append(Shape262)
HAnimSite266 = x3d.HAnimSite()
HAnimSite266.name = "l_forefoot_tip_pt"
HAnimSite266.DEF = "hanim_l_forefoot_tip_pt"
HAnimSite266.translation = [0.1354,0.0016,0.1476]
#HAnimSite visualization shape
TouchSensor267 = x3d.TouchSensor()
TouchSensor267.description = "HAnimSite l_forefoot_tip"

HAnimSite266.children.append(TouchSensor267)
Shape268 = x3d.Shape()
Shape268.USE = "HAnimSiteShape"

HAnimSite266.children.append(Shape268)

HAnimSegment250.children.append(HAnimSite266)
HAnimSite269 = x3d.HAnimSite()
HAnimSite269.name = "l_metatarsal_phalanx_5_pt"
HAnimSite269.DEF = "hanim_l_metatarsal_phalanx_5_pt"
HAnimSite269.translation = [0.1825,0.007,0.0928]
#HAnimSite visualization shape
TouchSensor270 = x3d.TouchSensor()
TouchSensor270.description = "HAnimSite l_metatarsal_pha5_pt"

HAnimSite269.children.append(TouchSensor270)
Shape271 = x3d.Shape()
Shape271.USE = "HAnimSiteShape"

HAnimSite269.children.append(Shape271)

HAnimSegment250.children.append(HAnimSite269)
HAnimSite272 = x3d.HAnimSite()
HAnimSite272.name = "l_tarsal_distal_phalanx_2_pt"
HAnimSite272.DEF = "hanim_l_tarsal_distal_phalanx_2_pt"
HAnimSite272.translation = [0.1195,0.0079,0.1433]
#HAnimSite visualization shape
TouchSensor273 = x3d.TouchSensor()
TouchSensor273.description = "HAnimSite l_digit2_pt"

HAnimSite272.children.append(TouchSensor273)
Shape274 = x3d.Shape()
Shape274.USE = "HAnimSiteShape"

HAnimSite272.children.append(Shape274)

HAnimSegment250.children.append(HAnimSite272)

HAnimJoint249.children.append(HAnimSegment250)

HAnimJoint233.children.append(HAnimJoint249)

HAnimJoint224.children.append(HAnimJoint233)

HAnimJoint187.children.append(HAnimJoint224)

HAnimJoint178.children.append(HAnimJoint187)

HAnimJoint148.children.append(HAnimJoint178)

HAnimJoint68.children.append(HAnimJoint148)
HAnimJoint275 = x3d.HAnimJoint()
HAnimJoint275.name = "r_hip"
HAnimJoint275.DEF = "hanim_r_hip"
HAnimJoint275.center = [-0.0961,0.9124,-0.0001]
HAnimJoint275.ulimit = [0,0,0]
HAnimJoint275.llimit = [0,0,0]
HAnimSegment276 = x3d.HAnimSegment()
HAnimSegment276.name = "r_thigh"
HAnimSegment276.DEF = "hanim_r_thigh"
#Visualization sphere for <HAnimJoint name='r_hip'/> is placed within <HAnimSegment name='r_thigh'/>
TouchSensor277 = x3d.TouchSensor()
TouchSensor277.description = "HAnimJoint r_hip, HAnimSegment r_thigh"

HAnimSegment276.children.append(TouchSensor277)
Transform278 = x3d.Transform()
Transform278.translation = [-0.0961,0.9124,-0.0001]
Shape279 = x3d.Shape()
Shape279.USE = "HAnimJointShape"

Transform278.children.append(Shape279)

HAnimSegment276.children.append(Transform278)
#HAnimSegment visualization line from current <HAnimJoint name='r_hip'/> to child <HAnimJoint name='r_knee'/>
Shape280 = x3d.Shape()
LineSet281 = x3d.LineSet()
LineSet281.vertexCount = [2]
Coordinate282 = x3d.Coordinate()
Coordinate282.point = (-0.0961,0.9124,-0.0001,-0.1040,0.4867,0.0308)

LineSet281.coord = Coordinate282
ColorRGBA283 = x3d.ColorRGBA()
ColorRGBA283.USE = "HAnimSegmentLineColorRGBA"

LineSet281.color = ColorRGBA283

Shape280.geometry = LineSet281

HAnimSegment276.children.append(Shape280)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_hip'/> to <HAnimSite name='r_knee_crease_pt'/>
Shape284 = x3d.Shape()
LineSet285 = x3d.LineSet()
LineSet285.vertexCount = [2]
Coordinate286 = x3d.Coordinate()
Coordinate286.point = (-0.0961,0.9124,-0.0001,-0.0825,0.4932,-0.0326)

LineSet285.coord = Coordinate286
ColorRGBA287 = x3d.ColorRGBA()
ColorRGBA287.USE = "HAnimSiteLineColorRGBA"

LineSet285.color = ColorRGBA287

Shape284.geometry = LineSet285

HAnimSegment276.children.append(Shape284)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_hip'/> to <HAnimSite name='r_femoral_lateral_epicn_pt'/>
Shape288 = x3d.Shape()
LineSet289 = x3d.LineSet()
LineSet289.vertexCount = [2]
Coordinate290 = x3d.Coordinate()
Coordinate290.point = (-0.0961,0.9124,-0.0001,-0.1421,0.4992,0.0310)

LineSet289.coord = Coordinate290
ColorRGBA291 = x3d.ColorRGBA()
ColorRGBA291.USE = "HAnimSiteLineColorRGBA"

LineSet289.color = ColorRGBA291

Shape288.geometry = LineSet289

HAnimSegment276.children.append(Shape288)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_hip'/> to <HAnimSite name='r_femoral_medial_epicn_pt'/>
Shape292 = x3d.Shape()
LineSet293 = x3d.LineSet()
LineSet293.vertexCount = [2]
Coordinate294 = x3d.Coordinate()
Coordinate294.point = (-0.0961,0.9124,-0.0001,-0.0221,0.5014,0.0289)

LineSet293.coord = Coordinate294
ColorRGBA295 = x3d.ColorRGBA()
ColorRGBA295.USE = "HAnimSiteLineColorRGBA"

LineSet293.color = ColorRGBA295

Shape292.geometry = LineSet293

HAnimSegment276.children.append(Shape292)
HAnimSite296 = x3d.HAnimSite()
HAnimSite296.name = "r_knee_crease_pt"
HAnimSite296.DEF = "hanim_r_knee_crease_pt"
HAnimSite296.translation = [-0.0825,0.4932,-0.0326]
#HAnimSite visualization shape
TouchSensor297 = x3d.TouchSensor()
TouchSensor297.description = "HAnimSite r_knee_crease_pt"

HAnimSite296.children.append(TouchSensor297)
Shape298 = x3d.Shape()
Shape298.USE = "HAnimSiteShape"

HAnimSite296.children.append(Shape298)

HAnimSegment276.children.append(HAnimSite296)
HAnimSite299 = x3d.HAnimSite()
HAnimSite299.name = "r_femoral_lateral_epicondyle_pt"
HAnimSite299.DEF = "hanim_r_femoral_lateral_epicondyle_pt"
HAnimSite299.translation = [-0.1421,0.4992,0.031]
#HAnimSite visualization shape
TouchSensor300 = x3d.TouchSensor()
TouchSensor300.description = "HAnimSite r_femoral_lateral_epicn_pt"

HAnimSite299.children.append(TouchSensor300)
Shape301 = x3d.Shape()
Shape301.USE = "HAnimSiteShape"

HAnimSite299.children.append(Shape301)

HAnimSegment276.children.append(HAnimSite299)
HAnimSite302 = x3d.HAnimSite()
HAnimSite302.name = "r_femoral_medial_epicondyle_pt"
HAnimSite302.DEF = "hanim_r_femoral_medial_epicondyle_pt"
HAnimSite302.translation = [-0.0221,0.5014,0.0289]
#HAnimSite visualization shape
TouchSensor303 = x3d.TouchSensor()
TouchSensor303.description = "HAnimSite r_femoral_medial_epicn_pt"

HAnimSite302.children.append(TouchSensor303)
Shape304 = x3d.Shape()
Shape304.USE = "HAnimSiteShape"

HAnimSite302.children.append(Shape304)

HAnimSegment276.children.append(HAnimSite302)

HAnimJoint275.children.append(HAnimSegment276)
HAnimJoint305 = x3d.HAnimJoint()
HAnimJoint305.name = "r_knee"
HAnimJoint305.DEF = "hanim_r_knee"
HAnimJoint305.center = [-0.104,0.4867,0.0308]
HAnimJoint305.ulimit = [0,0,0]
HAnimJoint305.llimit = [0,0,0]
HAnimSegment306 = x3d.HAnimSegment()
HAnimSegment306.name = "r_calf"
HAnimSegment306.DEF = "hanim_r_calf"
#Visualization sphere for <HAnimJoint name='r_knee'/> is placed within <HAnimSegment name='r_calf'/>
TouchSensor307 = x3d.TouchSensor()
TouchSensor307.description = "HAnimJoint r_knee, HAnimSegment r_calf"

HAnimSegment306.children.append(TouchSensor307)
Transform308 = x3d.Transform()
Transform308.translation = [-0.104,0.4867,0.0308]
Shape309 = x3d.Shape()
Shape309.USE = "HAnimJointShape"

Transform308.children.append(Shape309)

HAnimSegment306.children.append(Transform308)
#HAnimSegment visualization line from current <HAnimJoint name='r_knee'/> to child <HAnimJoint name='r_talocrural'/>
Shape310 = x3d.Shape()
LineSet311 = x3d.LineSet()
LineSet311.vertexCount = [2]
Coordinate312 = x3d.Coordinate()
Coordinate312.point = (-0.1040,0.4867,0.0308,-0.1101,0.0656,-0.0736)

LineSet311.coord = Coordinate312
ColorRGBA313 = x3d.ColorRGBA()
ColorRGBA313.USE = "HAnimSegmentLineColorRGBA"

LineSet311.color = ColorRGBA313

Shape310.geometry = LineSet311

HAnimSegment306.children.append(Shape310)

HAnimJoint305.children.append(HAnimSegment306)
HAnimJoint314 = x3d.HAnimJoint()
HAnimJoint314.name = "r_talocrural"
HAnimJoint314.DEF = "hanim_r_talocrural"
HAnimJoint314.center = [-0.1101,0.0656,-0.0736]
HAnimJoint314.ulimit = [0,0,0]
HAnimJoint314.llimit = [0,0,0]
HAnimSegment315 = x3d.HAnimSegment()
HAnimSegment315.name = "r_talus"
HAnimSegment315.DEF = "hanim_r_talus"
#Visualization sphere for <HAnimJoint name='r_talocrural'/> is placed within <HAnimSegment name='r_talus'/>
TouchSensor316 = x3d.TouchSensor()
TouchSensor316.description = "HAnimJoint r_talocrural, HAnimSegment r_talus"

HAnimSegment315.children.append(TouchSensor316)
Transform317 = x3d.Transform()
Transform317.translation = [-0.1101,0.0656,-0.0736]
Shape318 = x3d.Shape()
Shape318.USE = "HAnimJointShape"

Transform317.children.append(Shape318)

HAnimSegment315.children.append(Transform317)
#HAnimSegment visualization line from current <HAnimJoint name='r_talocrural'/> to child <HAnimJoint name='r_tarsometatarsal_2'/>
Shape319 = x3d.Shape()
LineSet320 = x3d.LineSet()
LineSet320.vertexCount = [2]
Coordinate321 = x3d.Coordinate()
Coordinate321.point = (-0.1101,0.0656,-0.0736,-0.1086,0.0001,-0.0368)

LineSet320.coord = Coordinate321
ColorRGBA322 = x3d.ColorRGBA()
ColorRGBA322.USE = "HAnimSegmentLineColorRGBA"

LineSet320.color = ColorRGBA322

Shape319.geometry = LineSet320

HAnimSegment315.children.append(Shape319)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_talocrural'/> to <HAnimSite name='r_lateral_malleolus_pt'/>
Shape323 = x3d.Shape()
LineSet324 = x3d.LineSet()
LineSet324.vertexCount = [2]
Coordinate325 = x3d.Coordinate()
Coordinate325.point = (-0.1101,0.0656,-0.0736,-0.1006,0.0658,-0.1075)

LineSet324.coord = Coordinate325
ColorRGBA326 = x3d.ColorRGBA()
ColorRGBA326.USE = "HAnimSiteLineColorRGBA"

LineSet324.color = ColorRGBA326

Shape323.geometry = LineSet324

HAnimSegment315.children.append(Shape323)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_talocrural'/> to <HAnimSite name='r_medial_malleolus_pt'/>
Shape327 = x3d.Shape()
LineSet328 = x3d.LineSet()
LineSet328.vertexCount = [2]
Coordinate329 = x3d.Coordinate()
Coordinate329.point = (-0.1101,0.0656,-0.0736,-0.0591,0.0760,-0.0928)

LineSet328.coord = Coordinate329
ColorRGBA330 = x3d.ColorRGBA()
ColorRGBA330.USE = "HAnimSiteLineColorRGBA"

LineSet328.color = ColorRGBA330

Shape327.geometry = LineSet328

HAnimSegment315.children.append(Shape327)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_talocrural'/> to <HAnimSite name='r_sphyrion_pt'/>
Shape331 = x3d.Shape()
LineSet332 = x3d.LineSet()
LineSet332.vertexCount = [2]
Coordinate333 = x3d.Coordinate()
Coordinate333.point = (-0.1101,0.0656,-0.0736,-0.0603,0.0610,-0.1002)

LineSet332.coord = Coordinate333
ColorRGBA334 = x3d.ColorRGBA()
ColorRGBA334.USE = "HAnimSiteLineColorRGBA"

LineSet332.color = ColorRGBA334

Shape331.geometry = LineSet332

HAnimSegment315.children.append(Shape331)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_talocrural'/> to <HAnimSite name='r_calcaneous_post_pt'/>
Shape335 = x3d.Shape()
LineSet336 = x3d.LineSet()
LineSet336.vertexCount = [2]
Coordinate337 = x3d.Coordinate()
Coordinate337.point = (-0.1101,0.0656,-0.0736,-0.0692,0.0297,-0.1221)

LineSet336.coord = Coordinate337
ColorRGBA338 = x3d.ColorRGBA()
ColorRGBA338.USE = "HAnimSiteLineColorRGBA"

LineSet336.color = ColorRGBA338

Shape335.geometry = LineSet336

HAnimSegment315.children.append(Shape335)
HAnimSite339 = x3d.HAnimSite()
HAnimSite339.name = "r_lateral_malleolus_pt"
HAnimSite339.DEF = "hanim_r_lateral_malleolus_pt"
HAnimSite339.translation = [-0.1006,0.0658,-0.1075]
#HAnimSite visualization shape
TouchSensor340 = x3d.TouchSensor()
TouchSensor340.description = "HAnimSite r_lateral_malleolus_pt"

HAnimSite339.children.append(TouchSensor340)
Shape341 = x3d.Shape()
Shape341.USE = "HAnimSiteShape"

HAnimSite339.children.append(Shape341)

HAnimSegment315.children.append(HAnimSite339)
HAnimSite342 = x3d.HAnimSite()
HAnimSite342.name = "r_medial_malleolus_pt"
HAnimSite342.DEF = "hanim_r_medial_malleolus_pt"
HAnimSite342.translation = [-0.0591,0.076,-0.0928]
#HAnimSite visualization shape
TouchSensor343 = x3d.TouchSensor()
TouchSensor343.description = "HAnimSite r_medial_malleolus_pt"

HAnimSite342.children.append(TouchSensor343)
Shape344 = x3d.Shape()
Shape344.USE = "HAnimSiteShape"

HAnimSite342.children.append(Shape344)

HAnimSegment315.children.append(HAnimSite342)
HAnimSite345 = x3d.HAnimSite()
HAnimSite345.name = "r_sphyrion_pt"
HAnimSite345.DEF = "hanim_r_sphyrion_pt"
HAnimSite345.translation = [-0.0603,0.061,-0.1002]
#HAnimSite visualization shape
TouchSensor346 = x3d.TouchSensor()
TouchSensor346.description = "HAnimSite r_sphyrion_pt"

HAnimSite345.children.append(TouchSensor346)
Shape347 = x3d.Shape()
Shape347.USE = "HAnimSiteShape"

HAnimSite345.children.append(Shape347)

HAnimSegment315.children.append(HAnimSite345)
HAnimSite348 = x3d.HAnimSite()
HAnimSite348.name = "r_calcaneus_posterior_pt"
HAnimSite348.DEF = "hanim_r_calcaneus_posterior_pt"
HAnimSite348.translation = [-0.0692,0.0297,-0.1221]
#HAnimSite visualization shape
TouchSensor349 = x3d.TouchSensor()
TouchSensor349.description = "HAnimSite r_calcaneous_post_pt"

HAnimSite348.children.append(TouchSensor349)
Shape350 = x3d.Shape()
Shape350.USE = "HAnimSiteShape"

HAnimSite348.children.append(Shape350)

HAnimSegment315.children.append(HAnimSite348)

HAnimJoint314.children.append(HAnimSegment315)
HAnimJoint351 = x3d.HAnimJoint()
HAnimJoint351.name = "r_tarsometatarsal_2"
HAnimJoint351.DEF = "hanim_r_tarsometatarsal_2"
HAnimJoint351.center = [-0.1086,0.0001,-0.0368]
HAnimJoint351.ulimit = [0,0,0]
HAnimJoint351.llimit = [0,0,0]
HAnimSegment352 = x3d.HAnimSegment()
HAnimSegment352.name = "r_metatarsal_2"
HAnimSegment352.DEF = "hanim_r_metatarsal_2"
#Visualization sphere for <HAnimJoint name='r_tarsometatarsal_2'/> is placed within <HAnimSegment name='r_metatarsal_2'/>
TouchSensor353 = x3d.TouchSensor()
TouchSensor353.description = "HAnimJoint r_tarsometatarsal_2, HAnimSegment r_metatarsal_2"

HAnimSegment352.children.append(TouchSensor353)
Transform354 = x3d.Transform()
Transform354.translation = [-0.1086,0.0001,-0.0368]
Shape355 = x3d.Shape()
Shape355.USE = "HAnimJointShape"

Transform354.children.append(Shape355)

HAnimSegment352.children.append(Transform354)
#HAnimSegment visualization line from current <HAnimJoint name='r_tarsometatarsal_2'/> to child <HAnimJoint name='r_metatarsophalangeal_2'/>
Shape356 = x3d.Shape()
LineSet357 = x3d.LineSet()
LineSet357.vertexCount = [2]
Coordinate358 = x3d.Coordinate()
Coordinate358.point = (-0.1086,0.0001,-0.0368,-0.1086,0.0001,0.0368)

LineSet357.coord = Coordinate358
ColorRGBA359 = x3d.ColorRGBA()
ColorRGBA359.USE = "HAnimSegmentLineColorRGBA"

LineSet357.color = ColorRGBA359

Shape356.geometry = LineSet357

HAnimSegment352.children.append(Shape356)

HAnimJoint351.children.append(HAnimSegment352)
HAnimJoint360 = x3d.HAnimJoint()
HAnimJoint360.name = "r_metatarsophalangeal_2"
HAnimJoint360.DEF = "hanim_r_metatarsophalangeal_2"
HAnimJoint360.center = [-0.1086,0.0001,0.0368]
HAnimJoint360.ulimit = [0,0,0]
HAnimJoint360.llimit = [0,0,0]
HAnimSegment361 = x3d.HAnimSegment()
HAnimSegment361.name = "r_tarsal_proximal_phalanx_2"
HAnimSegment361.DEF = "hanim_r_tarsal_proximal_phalanx_2"
#Visualization sphere for <HAnimJoint name='r_metatarsophalangeal_2'/> is placed within <HAnimSegment name='r_tarsal_proximal_phalanx_2'/>
TouchSensor362 = x3d.TouchSensor()
TouchSensor362.description = "HAnimJoint r_metatarsophalangeal_2, HAnimSegment r_tarsal_proximal_phalanx_2"

HAnimSegment361.children.append(TouchSensor362)
Transform363 = x3d.Transform()
Transform363.translation = [-0.1086,0.0001,0.0368]
Shape364 = x3d.Shape()
Shape364.USE = "HAnimJointShape"

Transform363.children.append(Shape364)

HAnimSegment361.children.append(Transform363)
#HAnimSegment visualization line from current <HAnimJoint name='r_metatarsophalangeal_2'/> to child <HAnimJoint name='r_tarsal_distal_interphalangeal_2'/>
Shape365 = x3d.Shape()
LineSet366 = x3d.LineSet()
LineSet366.vertexCount = [2]
Coordinate367 = x3d.Coordinate()
Coordinate367.point = (-0.1086,0.0001,0.0368,-0.1086,0.0000,0.0762)

LineSet366.coord = Coordinate367
ColorRGBA368 = x3d.ColorRGBA()
ColorRGBA368.USE = "HAnimSegmentLineColorRGBA"

LineSet366.color = ColorRGBA368

Shape365.geometry = LineSet366

HAnimSegment361.children.append(Shape365)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_metatarsophalangeal_2'/> to <HAnimSite name='r_metatarsal_pha1_pt'/>
Shape369 = x3d.Shape()
LineSet370 = x3d.LineSet()
LineSet370.vertexCount = [2]
Coordinate371 = x3d.Coordinate()
Coordinate371.point = (-0.1086,0.0001,0.0368,-0.0521,0.0260,0.0127)

LineSet370.coord = Coordinate371
ColorRGBA372 = x3d.ColorRGBA()
ColorRGBA372.USE = "HAnimSiteLineColorRGBA"

LineSet370.color = ColorRGBA372

Shape369.geometry = LineSet370

HAnimSegment361.children.append(Shape369)
HAnimSite373 = x3d.HAnimSite()
HAnimSite373.name = "r_metatarsal_phalanx_1_pt"
HAnimSite373.DEF = "hanim_r_metatarsal_phalanx_1_pt"
HAnimSite373.translation = [-0.0521,0.026,0.0127]
#HAnimSite visualization shape
TouchSensor374 = x3d.TouchSensor()
TouchSensor374.description = "HAnimSite r_metatarsal_pha1_pt"

HAnimSite373.children.append(TouchSensor374)
Shape375 = x3d.Shape()
Shape375.USE = "HAnimSiteShape"

HAnimSite373.children.append(Shape375)

HAnimSegment361.children.append(HAnimSite373)

HAnimJoint360.children.append(HAnimSegment361)
HAnimJoint376 = x3d.HAnimJoint()
HAnimJoint376.name = "r_tarsal_distal_interphalangeal_2"
HAnimJoint376.DEF = "hanim_r_tarsal_distal_interphalangeal_2"
HAnimJoint376.center = [-0.1086,0,0.0762]
HAnimJoint376.ulimit = [0,0,0]
HAnimJoint376.llimit = [0,0,0]
HAnimSegment377 = x3d.HAnimSegment()
HAnimSegment377.name = "r_tarsal_distal_phalanx_2"
HAnimSegment377.DEF = "hanim_r_tarsal_distal_phalanx_2"
#Visualization sphere for <HAnimJoint name='r_tarsal_distal_interphalangeal_2'/> is placed within <HAnimSegment name='r_tarsal_distal_phalanx_2'/>
TouchSensor378 = x3d.TouchSensor()
TouchSensor378.description = "HAnimJoint r_tarsal_distal_interphalangeal_2, HAnimSegment r_tarsal_distal_phalanx_2"

HAnimSegment377.children.append(TouchSensor378)
Transform379 = x3d.Transform()
Transform379.translation = [-0.1086,0,0.0762]
Shape380 = x3d.Shape()
Shape380.USE = "HAnimJointShape"

Transform379.children.append(Shape380)

HAnimSegment377.children.append(Transform379)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_tarsal_distal_interphalangeal_2'/> to <HAnimSite name='r_forefoot_tip'/>
Shape381 = x3d.Shape()
LineSet382 = x3d.LineSet()
LineSet382.vertexCount = [2]
Coordinate383 = x3d.Coordinate()
Coordinate383.point = (-0.1086,0.0000,0.0762,-0.1043,0.0227,0.1450)

LineSet382.coord = Coordinate383
ColorRGBA384 = x3d.ColorRGBA()
ColorRGBA384.USE = "HAnimSiteLineColorRGBA"

LineSet382.color = ColorRGBA384

Shape381.geometry = LineSet382

HAnimSegment377.children.append(Shape381)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_tarsal_distal_interphalangeal_2'/> to <HAnimSite name='r_metatarsal_pha5_pt'/>
Shape385 = x3d.Shape()
LineSet386 = x3d.LineSet()
LineSet386.vertexCount = [2]
Coordinate387 = x3d.Coordinate()
Coordinate387.point = (-0.1086,0.0000,0.0762,-0.1523,0.0166,0.0895)

LineSet386.coord = Coordinate387
ColorRGBA388 = x3d.ColorRGBA()
ColorRGBA388.USE = "HAnimSiteLineColorRGBA"

LineSet386.color = ColorRGBA388

Shape385.geometry = LineSet386

HAnimSegment377.children.append(Shape385)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_tarsal_distal_interphalangeal_2'/> to <HAnimSite name='r_digit2_pt'/>
Shape389 = x3d.Shape()
LineSet390 = x3d.LineSet()
LineSet390.vertexCount = [2]
Coordinate391 = x3d.Coordinate()
Coordinate391.point = (-0.1086,0.0000,0.0762,-0.0883,0.0134,0.1383)

LineSet390.coord = Coordinate391
ColorRGBA392 = x3d.ColorRGBA()
ColorRGBA392.USE = "HAnimSiteLineColorRGBA"

LineSet390.color = ColorRGBA392

Shape389.geometry = LineSet390

HAnimSegment377.children.append(Shape389)
HAnimSite393 = x3d.HAnimSite()
HAnimSite393.name = "r_forefoot_tip_pt"
HAnimSite393.DEF = "hanim_r_forefoot_tip_pt"
HAnimSite393.translation = [-0.1043,0.0227,0.145]
#HAnimSite visualization shape
TouchSensor394 = x3d.TouchSensor()
TouchSensor394.description = "HAnimSite r_forefoot_tip"

HAnimSite393.children.append(TouchSensor394)
Shape395 = x3d.Shape()
Shape395.USE = "HAnimSiteShape"

HAnimSite393.children.append(Shape395)

HAnimSegment377.children.append(HAnimSite393)
HAnimSite396 = x3d.HAnimSite()
HAnimSite396.name = "r_metatarsal_phalanx_5_pt"
HAnimSite396.DEF = "hanim_r_metatarsal_phalanx_5_pt"
HAnimSite396.translation = [-0.1523,0.0166,0.0895]
#HAnimSite visualization shape
TouchSensor397 = x3d.TouchSensor()
TouchSensor397.description = "HAnimSite r_metatarsal_pha5_pt"

HAnimSite396.children.append(TouchSensor397)
Shape398 = x3d.Shape()
Shape398.USE = "HAnimSiteShape"

HAnimSite396.children.append(Shape398)

HAnimSegment377.children.append(HAnimSite396)
HAnimSite399 = x3d.HAnimSite()
HAnimSite399.name = "r_tarsal_distal_phalanx_2_pt"
HAnimSite399.DEF = "hanim_r_tarsal_distal_phalanx_2_pt"
HAnimSite399.translation = [-0.0883,0.0134,0.1383]
#HAnimSite visualization shape
TouchSensor400 = x3d.TouchSensor()
TouchSensor400.description = "HAnimSite r_digit2_pt"

HAnimSite399.children.append(TouchSensor400)
Shape401 = x3d.Shape()
Shape401.USE = "HAnimSiteShape"

HAnimSite399.children.append(Shape401)

HAnimSegment377.children.append(HAnimSite399)

HAnimJoint376.children.append(HAnimSegment377)

HAnimJoint360.children.append(HAnimJoint376)

HAnimJoint351.children.append(HAnimJoint360)

HAnimJoint314.children.append(HAnimJoint351)

HAnimJoint305.children.append(HAnimJoint314)

HAnimJoint275.children.append(HAnimJoint305)

HAnimJoint68.children.append(HAnimJoint275)

HAnimJoint52.children.append(HAnimJoint68)
HAnimJoint402 = x3d.HAnimJoint()
HAnimJoint402.name = "vl5"
HAnimJoint402.DEF = "hanim_vl5"
HAnimJoint402.center = [0.0028,1.0568,-0.0776]
HAnimJoint402.ulimit = [0,0,0]
HAnimJoint402.llimit = [0,0,0]
HAnimSegment403 = x3d.HAnimSegment()
HAnimSegment403.name = "l5"
HAnimSegment403.DEF = "hanim_l5"
#Visualization sphere for <HAnimJoint name='vl5'/> is placed within <HAnimSegment name='l5'/>
TouchSensor404 = x3d.TouchSensor()
TouchSensor404.description = "HAnimJoint vl5, HAnimSegment l5"

HAnimSegment403.children.append(TouchSensor404)
Transform405 = x3d.Transform()
Transform405.translation = [0.0028,1.0568,-0.0776]
Shape406 = x3d.Shape()
Shape406.USE = "HAnimJointShape"

Transform405.children.append(Shape406)

HAnimSegment403.children.append(Transform405)
#HAnimSegment visualization line from current <HAnimJoint name='vl5'/> to child <HAnimJoint name='vl4'/>
Shape407 = x3d.Shape()
LineSet408 = x3d.LineSet()
LineSet408.vertexCount = [2]
Coordinate409 = x3d.Coordinate()
Coordinate409.point = (0.0028,1.0568,-0.0776,0.0035,1.0925,-0.0787)

LineSet408.coord = Coordinate409
ColorRGBA410 = x3d.ColorRGBA()
ColorRGBA410.USE = "HAnimSegmentLineColorRGBA"

LineSet408.color = ColorRGBA410

Shape407.geometry = LineSet408

HAnimSegment403.children.append(Shape407)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vl5'/> to <HAnimSite name='waist_preferred_post_pt'/>
Shape411 = x3d.Shape()
LineSet412 = x3d.LineSet()
LineSet412.vertexCount = [2]
Coordinate413 = x3d.Coordinate()
Coordinate413.point = (0.0028,1.0568,-0.0776,0.0000,1.0915,-0.1091)

LineSet412.coord = Coordinate413
ColorRGBA414 = x3d.ColorRGBA()
ColorRGBA414.USE = "HAnimSiteLineColorRGBA"

LineSet412.color = ColorRGBA414

Shape411.geometry = LineSet412

HAnimSegment403.children.append(Shape411)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vl5'/> to <HAnimSite name='navel_pt'/>
Shape415 = x3d.Shape()
LineSet416 = x3d.LineSet()
LineSet416.vertexCount = [2]
Coordinate417 = x3d.Coordinate()
Coordinate417.point = (0.0028,1.0568,-0.0776,0.0069,1.0966,0.1017)

LineSet416.coord = Coordinate417
ColorRGBA418 = x3d.ColorRGBA()
ColorRGBA418.USE = "HAnimSiteLineColorRGBA"

LineSet416.color = ColorRGBA418

Shape415.geometry = LineSet416

HAnimSegment403.children.append(Shape415)
HAnimSite419 = x3d.HAnimSite()
HAnimSite419.name = "waist_preferred_posterior_pt"
HAnimSite419.DEF = "hanim_waist_preferred_posterior_pt"
HAnimSite419.translation = [0,1.0915,-0.1091]
#HAnimSite visualization shape
TouchSensor420 = x3d.TouchSensor()
TouchSensor420.description = "HAnimSite waist_preferred_post_pt"

HAnimSite419.children.append(TouchSensor420)
Shape421 = x3d.Shape()
Shape421.USE = "HAnimSiteShape"

HAnimSite419.children.append(Shape421)

HAnimSegment403.children.append(HAnimSite419)
HAnimSite422 = x3d.HAnimSite()
HAnimSite422.name = "navel_pt"
HAnimSite422.DEF = "hanim_navel_pt"
HAnimSite422.translation = [0.0069,1.0966,0.1017]
#HAnimSite visualization shape
TouchSensor423 = x3d.TouchSensor()
TouchSensor423.description = "HAnimSite navel_pt"

HAnimSite422.children.append(TouchSensor423)
Shape424 = x3d.Shape()
Shape424.USE = "HAnimSiteShape"

HAnimSite422.children.append(Shape424)

HAnimSegment403.children.append(HAnimSite422)

HAnimJoint402.children.append(HAnimSegment403)
HAnimJoint425 = x3d.HAnimJoint()
HAnimJoint425.name = "vl4"
HAnimJoint425.DEF = "hanim_vl4"
HAnimJoint425.center = [0.0035,1.0925,-0.0787]
HAnimJoint425.ulimit = [0,0,0]
HAnimJoint425.llimit = [0,0,0]
HAnimSegment426 = x3d.HAnimSegment()
HAnimSegment426.name = "l4"
HAnimSegment426.DEF = "hanim_l4"
#Visualization sphere for <HAnimJoint name='vl4'/> is placed within <HAnimSegment name='l4'/>
TouchSensor427 = x3d.TouchSensor()
TouchSensor427.description = "HAnimJoint vl4, HAnimSegment l4"

HAnimSegment426.children.append(TouchSensor427)
Transform428 = x3d.Transform()
Transform428.translation = [0.0035,1.0925,-0.0787]
Shape429 = x3d.Shape()
Shape429.USE = "HAnimJointShape"

Transform428.children.append(Shape429)

HAnimSegment426.children.append(Transform428)
#HAnimSegment visualization line from current <HAnimJoint name='vl4'/> to child <HAnimJoint name='vl3'/>
Shape430 = x3d.Shape()
LineSet431 = x3d.LineSet()
LineSet431.vertexCount = [2]
Coordinate432 = x3d.Coordinate()
Coordinate432.point = (0.0035,1.0925,-0.0787,0.0041,1.1276,-0.0796)

LineSet431.coord = Coordinate432
ColorRGBA433 = x3d.ColorRGBA()
ColorRGBA433.USE = "HAnimSegmentLineColorRGBA"

LineSet431.color = ColorRGBA433

Shape430.geometry = LineSet431

HAnimSegment426.children.append(Shape430)

HAnimJoint425.children.append(HAnimSegment426)
HAnimJoint434 = x3d.HAnimJoint()
HAnimJoint434.name = "vl3"
HAnimJoint434.DEF = "hanim_vl3"
HAnimJoint434.center = [0.0041,1.1276,-0.0796]
HAnimJoint434.ulimit = [0,0,0]
HAnimJoint434.llimit = [0,0,0]
HAnimSegment435 = x3d.HAnimSegment()
HAnimSegment435.name = "l3"
HAnimSegment435.DEF = "hanim_l3"
#Visualization sphere for <HAnimJoint name='vl3'/> is placed within <HAnimSegment name='l3'/>
TouchSensor436 = x3d.TouchSensor()
TouchSensor436.description = "HAnimJoint vl3, HAnimSegment l3"

HAnimSegment435.children.append(TouchSensor436)
Transform437 = x3d.Transform()
Transform437.translation = [0.0041,1.1276,-0.0796]
Shape438 = x3d.Shape()
Shape438.USE = "HAnimJointShape"

Transform437.children.append(Shape438)

HAnimSegment435.children.append(Transform437)
#HAnimSegment visualization line from current <HAnimJoint name='vl3'/> to child <HAnimJoint name='vl2'/>
Shape439 = x3d.Shape()
LineSet440 = x3d.LineSet()
LineSet440.vertexCount = [2]
Coordinate441 = x3d.Coordinate()
Coordinate441.point = (0.0041,1.1276,-0.0796,0.0045,1.1546,-0.0800)

LineSet440.coord = Coordinate441
ColorRGBA442 = x3d.ColorRGBA()
ColorRGBA442.USE = "HAnimSegmentLineColorRGBA"

LineSet440.color = ColorRGBA442

Shape439.geometry = LineSet440

HAnimSegment435.children.append(Shape439)

HAnimJoint434.children.append(HAnimSegment435)
HAnimJoint443 = x3d.HAnimJoint()
HAnimJoint443.name = "vl2"
HAnimJoint443.DEF = "hanim_vl2"
HAnimJoint443.center = [0.0045,1.1546,-0.08]
HAnimJoint443.ulimit = [0,0,0]
HAnimJoint443.llimit = [0,0,0]
HAnimSegment444 = x3d.HAnimSegment()
HAnimSegment444.name = "l2"
HAnimSegment444.DEF = "hanim_l2"
#Visualization sphere for <HAnimJoint name='vl2'/> is placed within <HAnimSegment name='l2'/>
TouchSensor445 = x3d.TouchSensor()
TouchSensor445.description = "HAnimJoint vl2, HAnimSegment l2"

HAnimSegment444.children.append(TouchSensor445)
Transform446 = x3d.Transform()
Transform446.translation = [0.0045,1.1546,-0.08]
Shape447 = x3d.Shape()
Shape447.USE = "HAnimJointShape"

Transform446.children.append(Shape447)

HAnimSegment444.children.append(Transform446)
#HAnimSegment visualization line from current <HAnimJoint name='vl2'/> to child <HAnimJoint name='vl1'/>
Shape448 = x3d.Shape()
LineSet449 = x3d.LineSet()
LineSet449.vertexCount = [2]
Coordinate450 = x3d.Coordinate()
Coordinate450.point = (0.0045,1.1546,-0.0800,0.0048,1.1912,-0.0805)

LineSet449.coord = Coordinate450
ColorRGBA451 = x3d.ColorRGBA()
ColorRGBA451.USE = "HAnimSegmentLineColorRGBA"

LineSet449.color = ColorRGBA451

Shape448.geometry = LineSet449

HAnimSegment444.children.append(Shape448)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vl2'/> to <HAnimSite name='r_rib10_pt'/>
Shape452 = x3d.Shape()
LineSet453 = x3d.LineSet()
LineSet453.vertexCount = [2]
Coordinate454 = x3d.Coordinate()
Coordinate454.point = (0.0045,1.1546,-0.0800,-0.0711,1.1941,0.1016)

LineSet453.coord = Coordinate454
ColorRGBA455 = x3d.ColorRGBA()
ColorRGBA455.USE = "HAnimSiteLineColorRGBA"

LineSet453.color = ColorRGBA455

Shape452.geometry = LineSet453

HAnimSegment444.children.append(Shape452)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vl2'/> to <HAnimSite name='l_rib10_pt'/>
Shape456 = x3d.Shape()
LineSet457 = x3d.LineSet()
LineSet457.vertexCount = [2]
Coordinate458 = x3d.Coordinate()
Coordinate458.point = (0.0045,1.1546,-0.0800,0.0871,1.1925,0.0992)

LineSet457.coord = Coordinate458
ColorRGBA459 = x3d.ColorRGBA()
ColorRGBA459.USE = "HAnimSiteLineColorRGBA"

LineSet457.color = ColorRGBA459

Shape456.geometry = LineSet457

HAnimSegment444.children.append(Shape456)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vl2'/> to <HAnimSite name='rib10_midspine_pt'/>
Shape460 = x3d.Shape()
LineSet461 = x3d.LineSet()
LineSet461.vertexCount = [2]
Coordinate462 = x3d.Coordinate()
Coordinate462.point = (0.0045,1.1546,-0.0800,0.0049,1.1908,-0.1113)

LineSet461.coord = Coordinate462
ColorRGBA463 = x3d.ColorRGBA()
ColorRGBA463.USE = "HAnimSiteLineColorRGBA"

LineSet461.color = ColorRGBA463

Shape460.geometry = LineSet461

HAnimSegment444.children.append(Shape460)
HAnimSite464 = x3d.HAnimSite()
HAnimSite464.name = "r_rib10_pt"
HAnimSite464.DEF = "hanim_r_rib10_pt"
HAnimSite464.translation = [-0.0711,1.1941,0.1016]
#HAnimSite visualization shape
TouchSensor465 = x3d.TouchSensor()
TouchSensor465.description = "HAnimSite r_rib10_pt"

HAnimSite464.children.append(TouchSensor465)
Shape466 = x3d.Shape()
Shape466.USE = "HAnimSiteShape"

HAnimSite464.children.append(Shape466)

HAnimSegment444.children.append(HAnimSite464)
HAnimSite467 = x3d.HAnimSite()
HAnimSite467.name = "l_rib10_pt"
HAnimSite467.DEF = "hanim_l_rib10_pt"
HAnimSite467.translation = [0.0871,1.1925,0.0992]
#HAnimSite visualization shape
TouchSensor468 = x3d.TouchSensor()
TouchSensor468.description = "HAnimSite l_rib10_pt"

HAnimSite467.children.append(TouchSensor468)
Shape469 = x3d.Shape()
Shape469.USE = "HAnimSiteShape"

HAnimSite467.children.append(Shape469)

HAnimSegment444.children.append(HAnimSite467)
HAnimSite470 = x3d.HAnimSite()
HAnimSite470.name = "rib10_midspine_pt"
HAnimSite470.DEF = "hanim_rib10_midspine_pt"
HAnimSite470.translation = [0.0049,1.1908,-0.1113]
#HAnimSite visualization shape
TouchSensor471 = x3d.TouchSensor()
TouchSensor471.description = "HAnimSite rib10_midspine_pt"

HAnimSite470.children.append(TouchSensor471)
Shape472 = x3d.Shape()
Shape472.USE = "HAnimSiteShape"

HAnimSite470.children.append(Shape472)

HAnimSegment444.children.append(HAnimSite470)

HAnimJoint443.children.append(HAnimSegment444)
HAnimJoint473 = x3d.HAnimJoint()
HAnimJoint473.name = "vl1"
HAnimJoint473.DEF = "hanim_vl1"
HAnimJoint473.center = [0.0048,1.1912,-0.0805]
HAnimJoint473.ulimit = [0,0,0]
HAnimJoint473.llimit = [0,0,0]
HAnimSegment474 = x3d.HAnimSegment()
HAnimSegment474.name = "l1"
HAnimSegment474.DEF = "hanim_l1"
#Visualization sphere for <HAnimJoint name='vl1'/> is placed within <HAnimSegment name='l1'/>
TouchSensor475 = x3d.TouchSensor()
TouchSensor475.description = "HAnimJoint vl1, HAnimSegment l1"

HAnimSegment474.children.append(TouchSensor475)
Transform476 = x3d.Transform()
Transform476.translation = [0.0048,1.1912,-0.0805]
Shape477 = x3d.Shape()
Shape477.USE = "HAnimJointShape"

Transform476.children.append(Shape477)

HAnimSegment474.children.append(Transform476)
#HAnimSegment visualization line from current <HAnimJoint name='vl1'/> to child <HAnimJoint name='vt12'/>
Shape478 = x3d.Shape()
LineSet479 = x3d.LineSet()
LineSet479.vertexCount = [2]
Coordinate480 = x3d.Coordinate()
Coordinate480.point = (0.0048,1.1912,-0.0805,0.0051,1.2278,-0.0808)

LineSet479.coord = Coordinate480
ColorRGBA481 = x3d.ColorRGBA()
ColorRGBA481.USE = "HAnimSegmentLineColorRGBA"

LineSet479.color = ColorRGBA481

Shape478.geometry = LineSet479

HAnimSegment474.children.append(Shape478)

HAnimJoint473.children.append(HAnimSegment474)
HAnimJoint482 = x3d.HAnimJoint()
HAnimJoint482.name = "vt12"
HAnimJoint482.DEF = "hanim_vt12"
HAnimJoint482.center = [0.0051,1.2278,-0.0808]
HAnimJoint482.ulimit = [0,0,0]
HAnimJoint482.llimit = [0,0,0]
HAnimSegment483 = x3d.HAnimSegment()
HAnimSegment483.name = "t12"
HAnimSegment483.DEF = "hanim_t12"
#Visualization sphere for <HAnimJoint name='vt12'/> is placed within <HAnimSegment name='t12'/>
TouchSensor484 = x3d.TouchSensor()
TouchSensor484.description = "HAnimJoint vt12, HAnimSegment t12"

HAnimSegment483.children.append(TouchSensor484)
Transform485 = x3d.Transform()
Transform485.translation = [0.0051,1.2278,-0.0808]
Shape486 = x3d.Shape()
Shape486.USE = "HAnimJointShape"

Transform485.children.append(Shape486)

HAnimSegment483.children.append(Transform485)
#HAnimSegment visualization line from current <HAnimJoint name='vt12'/> to child <HAnimJoint name='vt11'/>
Shape487 = x3d.Shape()
LineSet488 = x3d.LineSet()
LineSet488.vertexCount = [2]
Coordinate489 = x3d.Coordinate()
Coordinate489.point = (0.0051,1.2278,-0.0808,0.0053,1.2679,-0.0810)

LineSet488.coord = Coordinate489
ColorRGBA490 = x3d.ColorRGBA()
ColorRGBA490.USE = "HAnimSegmentLineColorRGBA"

LineSet488.color = ColorRGBA490

Shape487.geometry = LineSet488

HAnimSegment483.children.append(Shape487)

HAnimJoint482.children.append(HAnimSegment483)
HAnimJoint491 = x3d.HAnimJoint()
HAnimJoint491.name = "vt11"
HAnimJoint491.DEF = "hanim_vt11"
HAnimJoint491.center = [0.0053,1.2679,-0.081]
HAnimJoint491.ulimit = [0,0,0]
HAnimJoint491.llimit = [0,0,0]
HAnimSegment492 = x3d.HAnimSegment()
HAnimSegment492.name = "t11"
HAnimSegment492.DEF = "hanim_t11"
#Visualization sphere for <HAnimJoint name='vt11'/> is placed within <HAnimSegment name='t11'/>
TouchSensor493 = x3d.TouchSensor()
TouchSensor493.description = "HAnimJoint vt11, HAnimSegment t11"

HAnimSegment492.children.append(TouchSensor493)
Transform494 = x3d.Transform()
Transform494.translation = [0.0053,1.2679,-0.081]
Shape495 = x3d.Shape()
Shape495.USE = "HAnimJointShape"

Transform494.children.append(Shape495)

HAnimSegment492.children.append(Transform494)
#HAnimSegment visualization line from current <HAnimJoint name='vt11'/> to child <HAnimJoint name='vt10'/>
Shape496 = x3d.Shape()
LineSet497 = x3d.LineSet()
LineSet497.vertexCount = [2]
Coordinate498 = x3d.Coordinate()
Coordinate498.point = (0.0053,1.2679,-0.0810,0.0056,1.2848,-0.0822)

LineSet497.coord = Coordinate498
ColorRGBA499 = x3d.ColorRGBA()
ColorRGBA499.USE = "HAnimSegmentLineColorRGBA"

LineSet497.color = ColorRGBA499

Shape496.geometry = LineSet497

HAnimSegment492.children.append(Shape496)

HAnimJoint491.children.append(HAnimSegment492)
HAnimJoint500 = x3d.HAnimJoint()
HAnimJoint500.name = "vt10"
HAnimJoint500.DEF = "hanim_vt10"
HAnimJoint500.center = [0.0056,1.2848,-0.0822]
HAnimJoint500.ulimit = [0,0,0]
HAnimJoint500.llimit = [0,0,0]
HAnimSegment501 = x3d.HAnimSegment()
HAnimSegment501.name = "t10"
HAnimSegment501.DEF = "hanim_t10"
#Visualization sphere for <HAnimJoint name='vt10'/> is placed within <HAnimSegment name='t10'/>
TouchSensor502 = x3d.TouchSensor()
TouchSensor502.description = "HAnimJoint vt10, HAnimSegment t10"

HAnimSegment501.children.append(TouchSensor502)
Transform503 = x3d.Transform()
Transform503.translation = [0.0056,1.2848,-0.0822]
Shape504 = x3d.Shape()
Shape504.USE = "HAnimJointShape"

Transform503.children.append(Shape504)

HAnimSegment501.children.append(Transform503)
#HAnimSegment visualization line from current <HAnimJoint name='vt10'/> to child <HAnimJoint name='vt9'/>
Shape505 = x3d.Shape()
LineSet506 = x3d.LineSet()
LineSet506.vertexCount = [2]
Coordinate507 = x3d.Coordinate()
Coordinate507.point = (0.0056,1.2848,-0.0822,0.0057,1.3126,-0.0838)

LineSet506.coord = Coordinate507
ColorRGBA508 = x3d.ColorRGBA()
ColorRGBA508.USE = "HAnimSegmentLineColorRGBA"

LineSet506.color = ColorRGBA508

Shape505.geometry = LineSet506

HAnimSegment501.children.append(Shape505)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vt10'/> to <HAnimSite name='substernale_pt'/>
Shape509 = x3d.Shape()
LineSet510 = x3d.LineSet()
LineSet510.vertexCount = [2]
Coordinate511 = x3d.Coordinate()
Coordinate511.point = (0.0056,1.2848,-0.0822,0.0085,1.2995,0.1147)

LineSet510.coord = Coordinate511
ColorRGBA512 = x3d.ColorRGBA()
ColorRGBA512.USE = "HAnimSiteLineColorRGBA"

LineSet510.color = ColorRGBA512

Shape509.geometry = LineSet510

HAnimSegment501.children.append(Shape509)
HAnimSite513 = x3d.HAnimSite()
HAnimSite513.name = "substernale_pt"
HAnimSite513.DEF = "hanim_substernale_pt"
HAnimSite513.translation = [0.0085,1.2995,0.1147]
#HAnimSite visualization shape
TouchSensor514 = x3d.TouchSensor()
TouchSensor514.description = "HAnimSite substernale_pt"

HAnimSite513.children.append(TouchSensor514)
Shape515 = x3d.Shape()
Shape515.USE = "HAnimSiteShape"

HAnimSite513.children.append(Shape515)

HAnimSegment501.children.append(HAnimSite513)

HAnimJoint500.children.append(HAnimSegment501)
HAnimJoint516 = x3d.HAnimJoint()
HAnimJoint516.name = "vt9"
HAnimJoint516.DEF = "hanim_vt9"
HAnimJoint516.center = [0.0057,1.3126,-0.0838]
HAnimJoint516.ulimit = [0,0,0]
HAnimJoint516.llimit = [0,0,0]
HAnimSegment517 = x3d.HAnimSegment()
HAnimSegment517.name = "t9"
HAnimSegment517.DEF = "hanim_t9"
#Visualization sphere for <HAnimJoint name='vt9'/> is placed within <HAnimSegment name='t9'/>
TouchSensor518 = x3d.TouchSensor()
TouchSensor518.description = "HAnimJoint vt9, HAnimSegment t9"

HAnimSegment517.children.append(TouchSensor518)
Transform519 = x3d.Transform()
Transform519.translation = [0.0057,1.3126,-0.0838]
Shape520 = x3d.Shape()
Shape520.USE = "HAnimJointShape"

Transform519.children.append(Shape520)

HAnimSegment517.children.append(Transform519)
#HAnimSegment visualization line from current <HAnimJoint name='vt9'/> to child <HAnimJoint name='vt8'/>
Shape521 = x3d.Shape()
LineSet522 = x3d.LineSet()
LineSet522.vertexCount = [2]
Coordinate523 = x3d.Coordinate()
Coordinate523.point = (0.0057,1.3126,-0.0838,0.0057,1.3382,-0.0845)

LineSet522.coord = Coordinate523
ColorRGBA524 = x3d.ColorRGBA()
ColorRGBA524.USE = "HAnimSegmentLineColorRGBA"

LineSet522.color = ColorRGBA524

Shape521.geometry = LineSet522

HAnimSegment517.children.append(Shape521)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vt9'/> to <HAnimSite name='r_thelion_pt'/>
Shape525 = x3d.Shape()
LineSet526 = x3d.LineSet()
LineSet526.vertexCount = [2]
Coordinate527 = x3d.Coordinate()
Coordinate527.point = (0.0057,1.3126,-0.0838,-0.0736,1.3385,0.1217)

LineSet526.coord = Coordinate527
ColorRGBA528 = x3d.ColorRGBA()
ColorRGBA528.USE = "HAnimSiteLineColorRGBA"

LineSet526.color = ColorRGBA528

Shape525.geometry = LineSet526

HAnimSegment517.children.append(Shape525)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vt9'/> to <HAnimSite name='l_thelion_pt'/>
Shape529 = x3d.Shape()
LineSet530 = x3d.LineSet()
LineSet530.vertexCount = [2]
Coordinate531 = x3d.Coordinate()
Coordinate531.point = (0.0057,1.3126,-0.0838,0.0918,1.3382,0.1192)

LineSet530.coord = Coordinate531
ColorRGBA532 = x3d.ColorRGBA()
ColorRGBA532.USE = "HAnimSiteLineColorRGBA"

LineSet530.color = ColorRGBA532

Shape529.geometry = LineSet530

HAnimSegment517.children.append(Shape529)
HAnimSite533 = x3d.HAnimSite()
HAnimSite533.name = "r_thelion_pt"
HAnimSite533.DEF = "hanim_r_thelion_pt"
HAnimSite533.translation = [-0.0736,1.3385,0.1217]
#HAnimSite visualization shape
TouchSensor534 = x3d.TouchSensor()
TouchSensor534.description = "HAnimSite r_thelion_pt"

HAnimSite533.children.append(TouchSensor534)
Shape535 = x3d.Shape()
Shape535.USE = "HAnimSiteShape"

HAnimSite533.children.append(Shape535)

HAnimSegment517.children.append(HAnimSite533)
HAnimSite536 = x3d.HAnimSite()
HAnimSite536.name = "l_thelion_pt"
HAnimSite536.DEF = "hanim_l_thelion_pt"
HAnimSite536.translation = [0.0918,1.3382,0.1192]
#HAnimSite visualization shape
TouchSensor537 = x3d.TouchSensor()
TouchSensor537.description = "HAnimSite l_thelion_pt"

HAnimSite536.children.append(TouchSensor537)
Shape538 = x3d.Shape()
Shape538.USE = "HAnimSiteShape"

HAnimSite536.children.append(Shape538)

HAnimSegment517.children.append(HAnimSite536)

HAnimJoint516.children.append(HAnimSegment517)
HAnimJoint539 = x3d.HAnimJoint()
HAnimJoint539.name = "vt8"
HAnimJoint539.DEF = "hanim_vt8"
HAnimJoint539.center = [0.0057,1.3382,-0.0845]
HAnimJoint539.ulimit = [0,0,0]
HAnimJoint539.llimit = [0,0,0]
HAnimSegment540 = x3d.HAnimSegment()
HAnimSegment540.name = "t8"
HAnimSegment540.DEF = "hanim_t8"
#Visualization sphere for <HAnimJoint name='vt8'/> is placed within <HAnimSegment name='t8'/>
TouchSensor541 = x3d.TouchSensor()
TouchSensor541.description = "HAnimJoint vt8, HAnimSegment t8"

HAnimSegment540.children.append(TouchSensor541)
Transform542 = x3d.Transform()
Transform542.translation = [0.0057,1.3382,-0.0845]
Shape543 = x3d.Shape()
Shape543.USE = "HAnimJointShape"

Transform542.children.append(Shape543)

HAnimSegment540.children.append(Transform542)
#HAnimSegment visualization line from current <HAnimJoint name='vt8'/> to child <HAnimJoint name='vt7'/>
Shape544 = x3d.Shape()
LineSet545 = x3d.LineSet()
LineSet545.vertexCount = [2]
Coordinate546 = x3d.Coordinate()
Coordinate546.point = (0.0057,1.3382,-0.0845,0.0058,1.3625,-0.0833)

LineSet545.coord = Coordinate546
ColorRGBA547 = x3d.ColorRGBA()
ColorRGBA547.USE = "HAnimSegmentLineColorRGBA"

LineSet545.color = ColorRGBA547

Shape544.geometry = LineSet545

HAnimSegment540.children.append(Shape544)

HAnimJoint539.children.append(HAnimSegment540)
HAnimJoint548 = x3d.HAnimJoint()
HAnimJoint548.name = "vt7"
HAnimJoint548.DEF = "hanim_vt7"
HAnimJoint548.center = [0.0058,1.3625,-0.0833]
HAnimJoint548.ulimit = [0,0,0]
HAnimJoint548.llimit = [0,0,0]
HAnimSegment549 = x3d.HAnimSegment()
HAnimSegment549.name = "t7"
HAnimSegment549.DEF = "hanim_t7"
#Visualization sphere for <HAnimJoint name='vt7'/> is placed within <HAnimSegment name='t7'/>
TouchSensor550 = x3d.TouchSensor()
TouchSensor550.description = "HAnimJoint vt7, HAnimSegment t7"

HAnimSegment549.children.append(TouchSensor550)
Transform551 = x3d.Transform()
Transform551.translation = [0.0058,1.3625,-0.0833]
Shape552 = x3d.Shape()
Shape552.USE = "HAnimJointShape"

Transform551.children.append(Shape552)

HAnimSegment549.children.append(Transform551)
#HAnimSegment visualization line from current <HAnimJoint name='vt7'/> to child <HAnimJoint name='vt6'/>
Shape553 = x3d.Shape()
LineSet554 = x3d.LineSet()
LineSet554.vertexCount = [2]
Coordinate555 = x3d.Coordinate()
Coordinate555.point = (0.0058,1.3625,-0.0833,0.0059,1.3866,-0.0800)

LineSet554.coord = Coordinate555
ColorRGBA556 = x3d.ColorRGBA()
ColorRGBA556.USE = "HAnimSegmentLineColorRGBA"

LineSet554.color = ColorRGBA556

Shape553.geometry = LineSet554

HAnimSegment549.children.append(Shape553)

HAnimJoint548.children.append(HAnimSegment549)
HAnimJoint557 = x3d.HAnimJoint()
HAnimJoint557.name = "vt6"
HAnimJoint557.DEF = "hanim_vt6"
HAnimJoint557.center = [0.0059,1.3866,-0.08]
HAnimJoint557.ulimit = [0,0,0]
HAnimJoint557.llimit = [0,0,0]
HAnimSegment558 = x3d.HAnimSegment()
HAnimSegment558.name = "t6"
HAnimSegment558.DEF = "hanim_t6"
#Visualization sphere for <HAnimJoint name='vt6'/> is placed within <HAnimSegment name='t6'/>
TouchSensor559 = x3d.TouchSensor()
TouchSensor559.description = "HAnimJoint vt6, HAnimSegment t6"

HAnimSegment558.children.append(TouchSensor559)
Transform560 = x3d.Transform()
Transform560.translation = [0.0059,1.3866,-0.08]
Shape561 = x3d.Shape()
Shape561.USE = "HAnimJointShape"

Transform560.children.append(Shape561)

HAnimSegment558.children.append(Transform560)
#HAnimSegment visualization line from current <HAnimJoint name='vt6'/> to child <HAnimJoint name='vt5'/>
Shape562 = x3d.Shape()
LineSet563 = x3d.LineSet()
LineSet563.vertexCount = [2]
Coordinate564 = x3d.Coordinate()
Coordinate564.point = (0.0059,1.3866,-0.0800,0.0060,1.4102,-0.0745)

LineSet563.coord = Coordinate564
ColorRGBA565 = x3d.ColorRGBA()
ColorRGBA565.USE = "HAnimSegmentLineColorRGBA"

LineSet563.color = ColorRGBA565

Shape562.geometry = LineSet563

HAnimSegment558.children.append(Shape562)

HAnimJoint557.children.append(HAnimSegment558)
HAnimJoint566 = x3d.HAnimJoint()
HAnimJoint566.name = "vt5"
HAnimJoint566.DEF = "hanim_vt5"
HAnimJoint566.center = [0.006,1.4102,-0.0745]
HAnimJoint566.ulimit = [0,0,0]
HAnimJoint566.llimit = [0,0,0]
HAnimSegment567 = x3d.HAnimSegment()
HAnimSegment567.name = "t5"
HAnimSegment567.DEF = "hanim_t5"
#Visualization sphere for <HAnimJoint name='vt5'/> is placed within <HAnimSegment name='t5'/>
TouchSensor568 = x3d.TouchSensor()
TouchSensor568.description = "HAnimJoint vt5, HAnimSegment t5"

HAnimSegment567.children.append(TouchSensor568)
Transform569 = x3d.Transform()
Transform569.translation = [0.006,1.4102,-0.0745]
Shape570 = x3d.Shape()
Shape570.USE = "HAnimJointShape"

Transform569.children.append(Shape570)

HAnimSegment567.children.append(Transform569)
#HAnimSegment visualization line from current <HAnimJoint name='vt5'/> to child <HAnimJoint name='vt4'/>
Shape571 = x3d.Shape()
LineSet572 = x3d.LineSet()
LineSet572.vertexCount = [2]
Coordinate573 = x3d.Coordinate()
Coordinate573.point = (0.0060,1.4102,-0.0745,0.0061,1.4320,-0.0675)

LineSet572.coord = Coordinate573
ColorRGBA574 = x3d.ColorRGBA()
ColorRGBA574.USE = "HAnimSegmentLineColorRGBA"

LineSet572.color = ColorRGBA574

Shape571.geometry = LineSet572

HAnimSegment567.children.append(Shape571)

HAnimJoint566.children.append(HAnimSegment567)
HAnimJoint575 = x3d.HAnimJoint()
HAnimJoint575.name = "vt4"
HAnimJoint575.DEF = "hanim_vt4"
HAnimJoint575.center = [0.0061,1.432,-0.0675]
HAnimJoint575.ulimit = [0,0,0]
HAnimJoint575.llimit = [0,0,0]
HAnimSegment576 = x3d.HAnimSegment()
HAnimSegment576.name = "t4"
HAnimSegment576.DEF = "hanim_t4"
#Visualization sphere for <HAnimJoint name='vt4'/> is placed within <HAnimSegment name='t4'/>
TouchSensor577 = x3d.TouchSensor()
TouchSensor577.description = "HAnimJoint vt4, HAnimSegment t4"

HAnimSegment576.children.append(TouchSensor577)
Transform578 = x3d.Transform()
Transform578.translation = [0.0061,1.432,-0.0675]
Shape579 = x3d.Shape()
Shape579.USE = "HAnimJointShape"

Transform578.children.append(Shape579)

HAnimSegment576.children.append(Transform578)
#HAnimSegment visualization line from current <HAnimJoint name='vt4'/> to child <HAnimJoint name='vt3'/>
Shape580 = x3d.Shape()
LineSet581 = x3d.LineSet()
LineSet581.vertexCount = [2]
Coordinate582 = x3d.Coordinate()
Coordinate582.point = (0.0061,1.4320,-0.0675,0.0062,1.4583,-0.0570)

LineSet581.coord = Coordinate582
ColorRGBA583 = x3d.ColorRGBA()
ColorRGBA583.USE = "HAnimSegmentLineColorRGBA"

LineSet581.color = ColorRGBA583

Shape580.geometry = LineSet581

HAnimSegment576.children.append(Shape580)

HAnimJoint575.children.append(HAnimSegment576)
HAnimJoint584 = x3d.HAnimJoint()
HAnimJoint584.name = "vt3"
HAnimJoint584.DEF = "hanim_vt3"
HAnimJoint584.center = [0.0062,1.4583,-0.057]
HAnimJoint584.ulimit = [0,0,0]
HAnimJoint584.llimit = [0,0,0]
HAnimSegment585 = x3d.HAnimSegment()
HAnimSegment585.name = "t3"
HAnimSegment585.DEF = "hanim_t3"
#Visualization sphere for <HAnimJoint name='vt3'/> is placed within <HAnimSegment name='t3'/>
TouchSensor586 = x3d.TouchSensor()
TouchSensor586.description = "HAnimJoint vt3, HAnimSegment t3"

HAnimSegment585.children.append(TouchSensor586)
Transform587 = x3d.Transform()
Transform587.translation = [0.0062,1.4583,-0.057]
Shape588 = x3d.Shape()
Shape588.USE = "HAnimJointShape"

Transform587.children.append(Shape588)

HAnimSegment585.children.append(Transform587)
#HAnimSegment visualization line from current <HAnimJoint name='vt3'/> to child <HAnimJoint name='vt2'/>
Shape589 = x3d.Shape()
LineSet590 = x3d.LineSet()
LineSet590.vertexCount = [2]
Coordinate591 = x3d.Coordinate()
Coordinate591.point = (0.0062,1.4583,-0.0570,0.0063,1.4761,-0.0484)

LineSet590.coord = Coordinate591
ColorRGBA592 = x3d.ColorRGBA()
ColorRGBA592.USE = "HAnimSegmentLineColorRGBA"

LineSet590.color = ColorRGBA592

Shape589.geometry = LineSet590

HAnimSegment585.children.append(Shape589)

HAnimJoint584.children.append(HAnimSegment585)
HAnimJoint593 = x3d.HAnimJoint()
HAnimJoint593.name = "vt2"
HAnimJoint593.DEF = "hanim_vt2"
HAnimJoint593.center = [0.0063,1.4761,-0.0484]
HAnimJoint593.ulimit = [0,0,0]
HAnimJoint593.llimit = [0,0,0]
HAnimSegment594 = x3d.HAnimSegment()
HAnimSegment594.name = "t2"
HAnimSegment594.DEF = "hanim_t2"
#Visualization sphere for <HAnimJoint name='vt2'/> is placed within <HAnimSegment name='t2'/>
TouchSensor595 = x3d.TouchSensor()
TouchSensor595.description = "HAnimJoint vt2, HAnimSegment t2"

HAnimSegment594.children.append(TouchSensor595)
Transform596 = x3d.Transform()
Transform596.translation = [0.0063,1.4761,-0.0484]
Shape597 = x3d.Shape()
Shape597.USE = "HAnimJointShape"

Transform596.children.append(Shape597)

HAnimSegment594.children.append(Transform596)
#HAnimSegment visualization line from current <HAnimJoint name='vt2'/> to child <HAnimJoint name='vt1'/>
Shape598 = x3d.Shape()
LineSet599 = x3d.LineSet()
LineSet599.vertexCount = [2]
Coordinate600 = x3d.Coordinate()
Coordinate600.point = (0.0063,1.4761,-0.0484,0.0065,1.4951,-0.0387)

LineSet599.coord = Coordinate600
ColorRGBA601 = x3d.ColorRGBA()
ColorRGBA601.USE = "HAnimSegmentLineColorRGBA"

LineSet599.color = ColorRGBA601

Shape598.geometry = LineSet599

HAnimSegment594.children.append(Shape598)

HAnimJoint593.children.append(HAnimSegment594)
HAnimJoint602 = x3d.HAnimJoint()
HAnimJoint602.name = "vt1"
HAnimJoint602.DEF = "hanim_vt1"
HAnimJoint602.center = [0.0065,1.4951,-0.0387]
HAnimJoint602.ulimit = [0,0,0]
HAnimJoint602.llimit = [0,0,0]
HAnimSegment603 = x3d.HAnimSegment()
HAnimSegment603.name = "t1"
HAnimSegment603.DEF = "hanim_t1"
#Visualization sphere for <HAnimJoint name='vt1'/> is placed within <HAnimSegment name='t1'/>
TouchSensor604 = x3d.TouchSensor()
TouchSensor604.description = "HAnimJoint vt1, HAnimSegment t1"

HAnimSegment603.children.append(TouchSensor604)
Transform605 = x3d.Transform()
Transform605.translation = [0.0065,1.4951,-0.0387]
Shape606 = x3d.Shape()
Shape606.USE = "HAnimJointShape"

Transform605.children.append(Shape606)

HAnimSegment603.children.append(Transform605)
#HAnimSegment visualization line from current <HAnimJoint name='vt1'/> to child <HAnimJoint name='vc7'/>
Shape607 = x3d.Shape()
LineSet608 = x3d.LineSet()
LineSet608.vertexCount = [2]
Coordinate609 = x3d.Coordinate()
Coordinate609.point = (0.0065,1.4951,-0.0387,0.0066,1.5132,-0.0301)

LineSet608.coord = Coordinate609
ColorRGBA610 = x3d.ColorRGBA()
ColorRGBA610.USE = "HAnimSegmentLineColorRGBA"

LineSet608.color = ColorRGBA610

Shape607.geometry = LineSet608

HAnimSegment603.children.append(Shape607)
#HAnimSegment visualization line from current <HAnimJoint name='vt1'/> to child <HAnimJoint name='l_sternoclavicular'/>
Shape611 = x3d.Shape()
LineSet612 = x3d.LineSet()
LineSet612.vertexCount = [2]
Coordinate613 = x3d.Coordinate()
Coordinate613.point = (0.0065,1.4951,-0.0387,0.0820,1.4488,-0.0353)

LineSet612.coord = Coordinate613
ColorRGBA614 = x3d.ColorRGBA()
ColorRGBA614.USE = "HAnimSegmentLineColorRGBA"

LineSet612.color = ColorRGBA614

Shape611.geometry = LineSet612

HAnimSegment603.children.append(Shape611)
#HAnimSegment visualization line from current <HAnimJoint name='vt1'/> to child <HAnimJoint name='r_sternoclavicular'/>
Shape615 = x3d.Shape()
LineSet616 = x3d.LineSet()
LineSet616.vertexCount = [2]
Coordinate617 = x3d.Coordinate()
Coordinate617.point = (0.0065,1.4951,-0.0387,-0.0820,1.4488,-0.0353)

LineSet616.coord = Coordinate617
ColorRGBA618 = x3d.ColorRGBA()
ColorRGBA618.USE = "HAnimSegmentLineColorRGBA"

LineSet616.color = ColorRGBA618

Shape615.geometry = LineSet616

HAnimSegment603.children.append(Shape615)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vt1'/> to <HAnimSite name='suprasternale_pt'/>
Shape619 = x3d.Shape()
LineSet620 = x3d.LineSet()
LineSet620.vertexCount = [2]
Coordinate621 = x3d.Coordinate()
Coordinate621.point = (0.0065,1.4951,-0.0387,0.0084,1.4714,0.0551)

LineSet620.coord = Coordinate621
ColorRGBA622 = x3d.ColorRGBA()
ColorRGBA622.USE = "HAnimSiteLineColorRGBA"

LineSet620.color = ColorRGBA622

Shape619.geometry = LineSet620

HAnimSegment603.children.append(Shape619)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vt1'/> to <HAnimSite name='cervicale_pt'/>
Shape623 = x3d.Shape()
LineSet624 = x3d.LineSet()
LineSet624.vertexCount = [2]
Coordinate625 = x3d.Coordinate()
Coordinate625.point = (0.0065,1.4951,-0.0387,0.0064,1.5200,-0.0815)

LineSet624.coord = Coordinate625
ColorRGBA626 = x3d.ColorRGBA()
ColorRGBA626.USE = "HAnimSiteLineColorRGBA"

LineSet624.color = ColorRGBA626

Shape623.geometry = LineSet624

HAnimSegment603.children.append(Shape623)
HAnimSite627 = x3d.HAnimSite()
HAnimSite627.name = "suprasternale_pt"
HAnimSite627.DEF = "hanim_suprasternale_pt"
HAnimSite627.translation = [0.0084,1.4714,0.0551]
#HAnimSite visualization shape
TouchSensor628 = x3d.TouchSensor()
TouchSensor628.description = "HAnimSite suprasternale_pt"

HAnimSite627.children.append(TouchSensor628)
Shape629 = x3d.Shape()
Shape629.USE = "HAnimSiteShape"

HAnimSite627.children.append(Shape629)

HAnimSegment603.children.append(HAnimSite627)
HAnimSite630 = x3d.HAnimSite()
HAnimSite630.name = "cervicale_pt"
HAnimSite630.DEF = "hanim_cervicale_pt"
HAnimSite630.translation = [0.0064,1.52,-0.0815]
#HAnimSite visualization shape
TouchSensor631 = x3d.TouchSensor()
TouchSensor631.description = "HAnimSite cervicale_pt"

HAnimSite630.children.append(TouchSensor631)
Shape632 = x3d.Shape()
Shape632.USE = "HAnimSiteShape"

HAnimSite630.children.append(Shape632)

HAnimSegment603.children.append(HAnimSite630)

HAnimJoint602.children.append(HAnimSegment603)
HAnimJoint633 = x3d.HAnimJoint()
HAnimJoint633.name = "vc7"
HAnimJoint633.DEF = "hanim_vc7"
HAnimJoint633.center = [0.0066,1.5132,-0.0301]
HAnimJoint633.ulimit = [0,0,0]
HAnimJoint633.llimit = [0,0,0]
HAnimSegment634 = x3d.HAnimSegment()
HAnimSegment634.name = "c7"
HAnimSegment634.DEF = "hanim_c7"
#Visualization sphere for <HAnimJoint name='vc7'/> is placed within <HAnimSegment name='c7'/>
TouchSensor635 = x3d.TouchSensor()
TouchSensor635.description = "HAnimJoint vc7, HAnimSegment c7"

HAnimSegment634.children.append(TouchSensor635)
Transform636 = x3d.Transform()
Transform636.translation = [0.0066,1.5132,-0.0301]
Shape637 = x3d.Shape()
Shape637.USE = "HAnimJointShape"

Transform636.children.append(Shape637)

HAnimSegment634.children.append(Transform636)
#HAnimSegment visualization line from current <HAnimJoint name='vc7'/> to child <HAnimJoint name='vc6'/>
Shape638 = x3d.Shape()
LineSet639 = x3d.LineSet()
LineSet639.vertexCount = [2]
Coordinate640 = x3d.Coordinate()
Coordinate640.point = (0.0066,1.5132,-0.0301,0.0066,1.5357,-0.0143)

LineSet639.coord = Coordinate640
ColorRGBA641 = x3d.ColorRGBA()
ColorRGBA641.USE = "HAnimSegmentLineColorRGBA"

LineSet639.color = ColorRGBA641

Shape638.geometry = LineSet639

HAnimSegment634.children.append(Shape638)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vc7'/> to <HAnimSite name='r_neck_base_pt'/>
Shape642 = x3d.Shape()
LineSet643 = x3d.LineSet()
LineSet643.vertexCount = [2]
Coordinate644 = x3d.Coordinate()
Coordinate644.point = (0.0066,1.5132,-0.0301,-0.0419,1.5149,-0.0220)

LineSet643.coord = Coordinate644
ColorRGBA645 = x3d.ColorRGBA()
ColorRGBA645.USE = "HAnimSiteLineColorRGBA"

LineSet643.color = ColorRGBA645

Shape642.geometry = LineSet643

HAnimSegment634.children.append(Shape642)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vc7'/> to <HAnimSite name='l_neck_base_pt'/>
Shape646 = x3d.Shape()
LineSet647 = x3d.LineSet()
LineSet647.vertexCount = [2]
Coordinate648 = x3d.Coordinate()
Coordinate648.point = (0.0066,1.5132,-0.0301,0.0646,1.5141,-0.0380)

LineSet647.coord = Coordinate648
ColorRGBA649 = x3d.ColorRGBA()
ColorRGBA649.USE = "HAnimSiteLineColorRGBA"

LineSet647.color = ColorRGBA649

Shape646.geometry = LineSet647

HAnimSegment634.children.append(Shape646)
HAnimSite650 = x3d.HAnimSite()
HAnimSite650.name = "r_neck_base_pt"
HAnimSite650.DEF = "hanim_r_neck_base_pt"
HAnimSite650.translation = [-0.0419,1.5149,-0.022]
#HAnimSite visualization shape
TouchSensor651 = x3d.TouchSensor()
TouchSensor651.description = "HAnimSite r_neck_base_pt"

HAnimSite650.children.append(TouchSensor651)
Shape652 = x3d.Shape()
Shape652.USE = "HAnimSiteShape"

HAnimSite650.children.append(Shape652)

HAnimSegment634.children.append(HAnimSite650)
HAnimSite653 = x3d.HAnimSite()
HAnimSite653.name = "l_neck_base_pt"
HAnimSite653.DEF = "hanim_l_neck_base_pt"
HAnimSite653.translation = [0.0646,1.5141,-0.038]
#HAnimSite visualization shape
TouchSensor654 = x3d.TouchSensor()
TouchSensor654.description = "HAnimSite l_neck_base_pt"

HAnimSite653.children.append(TouchSensor654)
Shape655 = x3d.Shape()
Shape655.USE = "HAnimSiteShape"

HAnimSite653.children.append(Shape655)

HAnimSegment634.children.append(HAnimSite653)

HAnimJoint633.children.append(HAnimSegment634)
HAnimJoint656 = x3d.HAnimJoint()
HAnimJoint656.name = "vc6"
HAnimJoint656.DEF = "hanim_vc6"
HAnimJoint656.center = [0.0066,1.5357,-0.0143]
HAnimJoint656.ulimit = [0,0,0]
HAnimJoint656.llimit = [0,0,0]
HAnimSegment657 = x3d.HAnimSegment()
HAnimSegment657.name = "c6"
HAnimSegment657.DEF = "hanim_c6"
#Visualization sphere for <HAnimJoint name='vc6'/> is placed within <HAnimSegment name='c6'/>
TouchSensor658 = x3d.TouchSensor()
TouchSensor658.description = "HAnimJoint vc6, HAnimSegment c6"

HAnimSegment657.children.append(TouchSensor658)
Transform659 = x3d.Transform()
Transform659.translation = [0.0066,1.5357,-0.0143]
Shape660 = x3d.Shape()
Shape660.USE = "HAnimJointShape"

Transform659.children.append(Shape660)

HAnimSegment657.children.append(Transform659)
#HAnimSegment visualization line from current <HAnimJoint name='vc6'/> to child <HAnimJoint name='vc5'/>
Shape661 = x3d.Shape()
LineSet662 = x3d.LineSet()
LineSet662.vertexCount = [2]
Coordinate663 = x3d.Coordinate()
Coordinate663.point = (0.0066,1.5357,-0.0143,0.0066,1.5520,-0.0082)

LineSet662.coord = Coordinate663
ColorRGBA664 = x3d.ColorRGBA()
ColorRGBA664.USE = "HAnimSegmentLineColorRGBA"

LineSet662.color = ColorRGBA664

Shape661.geometry = LineSet662

HAnimSegment657.children.append(Shape661)

HAnimJoint656.children.append(HAnimSegment657)
HAnimJoint665 = x3d.HAnimJoint()
HAnimJoint665.name = "vc5"
HAnimJoint665.DEF = "hanim_vc5"
HAnimJoint665.center = [0.0066,1.552,-0.0082]
HAnimJoint665.ulimit = [0,0,0]
HAnimJoint665.llimit = [0,0,0]
HAnimSegment666 = x3d.HAnimSegment()
HAnimSegment666.name = "c5"
HAnimSegment666.DEF = "hanim_c5"
#Visualization sphere for <HAnimJoint name='vc5'/> is placed within <HAnimSegment name='c5'/>
TouchSensor667 = x3d.TouchSensor()
TouchSensor667.description = "HAnimJoint vc5, HAnimSegment c5"

HAnimSegment666.children.append(TouchSensor667)
Transform668 = x3d.Transform()
Transform668.translation = [0.0066,1.552,-0.0082]
Shape669 = x3d.Shape()
Shape669.USE = "HAnimJointShape"

Transform668.children.append(Shape669)

HAnimSegment666.children.append(Transform668)
#HAnimSegment visualization line from current <HAnimJoint name='vc5'/> to child <HAnimJoint name='vc4'/>
Shape670 = x3d.Shape()
LineSet671 = x3d.LineSet()
LineSet671.vertexCount = [2]
Coordinate672 = x3d.Coordinate()
Coordinate672.point = (0.0066,1.5520,-0.0082,0.0066,1.5662,-0.0084)

LineSet671.coord = Coordinate672
ColorRGBA673 = x3d.ColorRGBA()
ColorRGBA673.USE = "HAnimSegmentLineColorRGBA"

LineSet671.color = ColorRGBA673

Shape670.geometry = LineSet671

HAnimSegment666.children.append(Shape670)

HAnimJoint665.children.append(HAnimSegment666)
HAnimJoint674 = x3d.HAnimJoint()
HAnimJoint674.name = "vc4"
HAnimJoint674.DEF = "hanim_vc4"
HAnimJoint674.center = [0.0066,1.5662,-0.0084]
HAnimJoint674.ulimit = [0,0,0]
HAnimJoint674.llimit = [0,0,0]
HAnimSegment675 = x3d.HAnimSegment()
HAnimSegment675.name = "c4"
HAnimSegment675.DEF = "hanim_c4"
#Visualization sphere for <HAnimJoint name='vc4'/> is placed within <HAnimSegment name='c4'/>
TouchSensor676 = x3d.TouchSensor()
TouchSensor676.description = "HAnimJoint vc4, HAnimSegment c4"

HAnimSegment675.children.append(TouchSensor676)
Transform677 = x3d.Transform()
Transform677.translation = [0.0066,1.5662,-0.0084]
Shape678 = x3d.Shape()
Shape678.USE = "HAnimJointShape"

Transform677.children.append(Shape678)

HAnimSegment675.children.append(Transform677)
#HAnimSegment visualization line from current <HAnimJoint name='vc4'/> to child <HAnimJoint name='vc3'/>
Shape679 = x3d.Shape()
LineSet680 = x3d.LineSet()
LineSet680.vertexCount = [2]
Coordinate681 = x3d.Coordinate()
Coordinate681.point = (0.0066,1.5662,-0.0084,0.0066,1.5800,-0.0103)

LineSet680.coord = Coordinate681
ColorRGBA682 = x3d.ColorRGBA()
ColorRGBA682.USE = "HAnimSegmentLineColorRGBA"

LineSet680.color = ColorRGBA682

Shape679.geometry = LineSet680

HAnimSegment675.children.append(Shape679)

HAnimJoint674.children.append(HAnimSegment675)
HAnimJoint683 = x3d.HAnimJoint()
HAnimJoint683.name = "vc3"
HAnimJoint683.DEF = "hanim_vc3"
HAnimJoint683.center = [0.0066,1.58,-0.0103]
HAnimJoint683.ulimit = [0,0,0]
HAnimJoint683.llimit = [0,0,0]
HAnimSegment684 = x3d.HAnimSegment()
HAnimSegment684.name = "c3"
HAnimSegment684.DEF = "hanim_c3"
#Visualization sphere for <HAnimJoint name='vc3'/> is placed within <HAnimSegment name='c3'/>
TouchSensor685 = x3d.TouchSensor()
TouchSensor685.description = "HAnimJoint vc3, HAnimSegment c3"

HAnimSegment684.children.append(TouchSensor685)
Transform686 = x3d.Transform()
Transform686.translation = [0.0066,1.58,-0.0103]
Shape687 = x3d.Shape()
Shape687.USE = "HAnimJointShape"

Transform686.children.append(Shape687)

HAnimSegment684.children.append(Transform686)
#HAnimSegment visualization line from current <HAnimJoint name='vc3'/> to child <HAnimJoint name='vc2'/>
Shape688 = x3d.Shape()
LineSet689 = x3d.LineSet()
LineSet689.vertexCount = [2]
Coordinate690 = x3d.Coordinate()
Coordinate690.point = (0.0066,1.5800,-0.0103,0.0066,1.5928,-0.0103)

LineSet689.coord = Coordinate690
ColorRGBA691 = x3d.ColorRGBA()
ColorRGBA691.USE = "HAnimSegmentLineColorRGBA"

LineSet689.color = ColorRGBA691

Shape688.geometry = LineSet689

HAnimSegment684.children.append(Shape688)

HAnimJoint683.children.append(HAnimSegment684)
HAnimJoint692 = x3d.HAnimJoint()
HAnimJoint692.name = "vc2"
HAnimJoint692.DEF = "hanim_vc2"
HAnimJoint692.center = [0.0066,1.5928,-0.0103]
HAnimJoint692.ulimit = [0,0,0]
HAnimJoint692.llimit = [0,0,0]
HAnimSegment693 = x3d.HAnimSegment()
HAnimSegment693.name = "c2"
HAnimSegment693.DEF = "hanim_c2"
#Visualization sphere for <HAnimJoint name='vc2'/> is placed within <HAnimSegment name='c2'/>
TouchSensor694 = x3d.TouchSensor()
TouchSensor694.description = "HAnimJoint vc2, HAnimSegment c2"

HAnimSegment693.children.append(TouchSensor694)
Transform695 = x3d.Transform()
Transform695.translation = [0.0066,1.5928,-0.0103]
Shape696 = x3d.Shape()
Shape696.USE = "HAnimJointShape"

Transform695.children.append(Shape696)

HAnimSegment693.children.append(Transform695)
#HAnimSegment visualization line from current <HAnimJoint name='vc2'/> to child <HAnimJoint name='vc1'/>
Shape697 = x3d.Shape()
LineSet698 = x3d.LineSet()
LineSet698.vertexCount = [2]
Coordinate699 = x3d.Coordinate()
Coordinate699.point = (0.0066,1.5928,-0.0103,0.0066,1.6144,-0.0034)

LineSet698.coord = Coordinate699
ColorRGBA700 = x3d.ColorRGBA()
ColorRGBA700.USE = "HAnimSegmentLineColorRGBA"

LineSet698.color = ColorRGBA700

Shape697.geometry = LineSet698

HAnimSegment693.children.append(Shape697)

HAnimJoint692.children.append(HAnimSegment693)
HAnimJoint701 = x3d.HAnimJoint()
HAnimJoint701.name = "vc1"
HAnimJoint701.DEF = "hanim_vc1"
HAnimJoint701.center = [0.0066,1.6144,-0.0034]
HAnimJoint701.ulimit = [0,0,0]
HAnimJoint701.llimit = [0,0,0]
HAnimSegment702 = x3d.HAnimSegment()
HAnimSegment702.name = "c1"
HAnimSegment702.DEF = "hanim_c1"
#Visualization sphere for <HAnimJoint name='vc1'/> is placed within <HAnimSegment name='c1'/>
TouchSensor703 = x3d.TouchSensor()
TouchSensor703.description = "HAnimJoint vc1, HAnimSegment c1"

HAnimSegment702.children.append(TouchSensor703)
Transform704 = x3d.Transform()
Transform704.translation = [0.0066,1.6144,-0.0034]
Shape705 = x3d.Shape()
Shape705.USE = "HAnimJointShape"

Transform704.children.append(Shape705)

HAnimSegment702.children.append(Transform704)
#HAnimSegment visualization line from current <HAnimJoint name='vc1'/> to child <HAnimJoint name='skullbase'/>
Shape706 = x3d.Shape()
LineSet707 = x3d.LineSet()
LineSet707.vertexCount = [2]
Coordinate708 = x3d.Coordinate()
Coordinate708.point = (0.0066,1.6144,-0.0034,0.0044,1.6209,0.0236)

LineSet707.coord = Coordinate708
ColorRGBA709 = x3d.ColorRGBA()
ColorRGBA709.USE = "HAnimSegmentLineColorRGBA"

LineSet707.color = ColorRGBA709

Shape706.geometry = LineSet707

HAnimSegment702.children.append(Shape706)

HAnimJoint701.children.append(HAnimSegment702)
HAnimJoint710 = x3d.HAnimJoint()
HAnimJoint710.name = "skullbase"
HAnimJoint710.DEF = "hanim_skullbase"
HAnimJoint710.center = [0.0044,1.6209,0.0236]
HAnimJoint710.ulimit = [0,0,0]
HAnimJoint710.llimit = [0,0,0]
HAnimSegment711 = x3d.HAnimSegment()
HAnimSegment711.name = "skull"
HAnimSegment711.DEF = "hanim_skull"
#Visualization sphere for <HAnimJoint name='skullbase'/> is placed within <HAnimSegment name='skull'/>
TouchSensor712 = x3d.TouchSensor()
TouchSensor712.description = "HAnimJoint skullbase, HAnimSegment skull"

HAnimSegment711.children.append(TouchSensor712)
Transform713 = x3d.Transform()
Transform713.translation = [0.0044,1.6209,0.0236]
Shape714 = x3d.Shape()
Shape714.USE = "HAnimJointShape"

Transform713.children.append(Shape714)

HAnimSegment711.children.append(Transform713)
#HAnimSegment visualization line from current <HAnimJoint name='skullbase'/> to child <HAnimJoint name='l_eyeball_joint'/>
Shape715 = x3d.Shape()
LineSet716 = x3d.LineSet()
LineSet716.vertexCount = [2]
Coordinate717 = x3d.Coordinate()
Coordinate717.point = (0.0044,1.6209,0.0236,0.0336,1.6332,0.0502)

LineSet716.coord = Coordinate717
ColorRGBA718 = x3d.ColorRGBA()
ColorRGBA718.USE = "HAnimSegmentLineColorRGBA"

LineSet716.color = ColorRGBA718

Shape715.geometry = LineSet716

HAnimSegment711.children.append(Shape715)
#HAnimSegment visualization line from current <HAnimJoint name='skullbase'/> to child <HAnimJoint name='l_eyelid_joint'/>
Shape719 = x3d.Shape()
LineSet720 = x3d.LineSet()
LineSet720.vertexCount = [2]
Coordinate721 = x3d.Coordinate()
Coordinate721.point = (0.0044,1.6209,0.0236,0.0336,1.6332,0.0502)

LineSet720.coord = Coordinate721
ColorRGBA722 = x3d.ColorRGBA()
ColorRGBA722.USE = "HAnimSegmentLineColorRGBA"

LineSet720.color = ColorRGBA722

Shape719.geometry = LineSet720

HAnimSegment711.children.append(Shape719)
#HAnimSegment visualization line from current <HAnimJoint name='skullbase'/> to child <HAnimJoint name='l_eyebrow_joint'/>
Shape723 = x3d.Shape()
LineSet724 = x3d.LineSet()
LineSet724.vertexCount = [2]
Coordinate725 = x3d.Coordinate()
Coordinate725.point = (0.0044,1.6209,0.0236,0.0336,1.6350,0.0506)

LineSet724.coord = Coordinate725
ColorRGBA726 = x3d.ColorRGBA()
ColorRGBA726.USE = "HAnimSegmentLineColorRGBA"

LineSet724.color = ColorRGBA726

Shape723.geometry = LineSet724

HAnimSegment711.children.append(Shape723)
#HAnimSegment visualization line from current <HAnimJoint name='skullbase'/> to child <HAnimJoint name='r_eyeball_joint'/>
Shape727 = x3d.Shape()
LineSet728 = x3d.LineSet()
LineSet728.vertexCount = [2]
Coordinate729 = x3d.Coordinate()
Coordinate729.point = (0.0044,1.6209,0.0236,-0.0336,1.6332,0.0502)

LineSet728.coord = Coordinate729
ColorRGBA730 = x3d.ColorRGBA()
ColorRGBA730.USE = "HAnimSegmentLineColorRGBA"

LineSet728.color = ColorRGBA730

Shape727.geometry = LineSet728

HAnimSegment711.children.append(Shape727)
#HAnimSegment visualization line from current <HAnimJoint name='skullbase'/> to child <HAnimJoint name='r_eyelid_joint'/>
Shape731 = x3d.Shape()
LineSet732 = x3d.LineSet()
LineSet732.vertexCount = [2]
Coordinate733 = x3d.Coordinate()
Coordinate733.point = (0.0044,1.6209,0.0236,-0.0336,1.6332,0.0502)

LineSet732.coord = Coordinate733
ColorRGBA734 = x3d.ColorRGBA()
ColorRGBA734.USE = "HAnimSegmentLineColorRGBA"

LineSet732.color = ColorRGBA734

Shape731.geometry = LineSet732

HAnimSegment711.children.append(Shape731)
#HAnimSegment visualization line from current <HAnimJoint name='skullbase'/> to child <HAnimJoint name='r_eyebrow_joint'/>
Shape735 = x3d.Shape()
LineSet736 = x3d.LineSet()
LineSet736.vertexCount = [2]
Coordinate737 = x3d.Coordinate()
Coordinate737.point = (0.0044,1.6209,0.0236,-0.0336,1.6350,0.0506)

LineSet736.coord = Coordinate737
ColorRGBA738 = x3d.ColorRGBA()
ColorRGBA738.USE = "HAnimSegmentLineColorRGBA"

LineSet736.color = ColorRGBA738

Shape735.geometry = LineSet736

HAnimSegment711.children.append(Shape735)
#HAnimSegment visualization line from current <HAnimJoint name='skullbase'/> to child <HAnimJoint name='temporomandibular'/>
Shape739 = x3d.Shape()
LineSet740 = x3d.LineSet()
LineSet740.vertexCount = [2]
Coordinate741 = x3d.Coordinate()
Coordinate741.point = (0.0044,1.6209,0.0236,0.0000,1.6300,0.0150)

LineSet740.coord = Coordinate741
ColorRGBA742 = x3d.ColorRGBA()
ColorRGBA742.USE = "HAnimSegmentLineColorRGBA"

LineSet740.color = ColorRGBA742

Shape739.geometry = LineSet740

HAnimSegment711.children.append(Shape739)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='skullbase'/> to <HAnimSite name='skull_tip'/>
Shape743 = x3d.Shape()
LineSet744 = x3d.LineSet()
LineSet744.vertexCount = [2]
Coordinate745 = x3d.Coordinate()
Coordinate745.point = (0.0044,1.6209,0.0236,0.0050,1.7504,0.0055)

LineSet744.coord = Coordinate745
ColorRGBA746 = x3d.ColorRGBA()
ColorRGBA746.USE = "HAnimSiteLineColorRGBA"

LineSet744.color = ColorRGBA746

Shape743.geometry = LineSet744

HAnimSegment711.children.append(Shape743)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='skullbase'/> to <HAnimSite name='sellion_pt'/>
Shape747 = x3d.Shape()
LineSet748 = x3d.LineSet()
LineSet748.vertexCount = [2]
Coordinate749 = x3d.Coordinate()
Coordinate749.point = (0.0044,1.6209,0.0236,0.0058,1.6316,0.0852)

LineSet748.coord = Coordinate749
ColorRGBA750 = x3d.ColorRGBA()
ColorRGBA750.USE = "HAnimSiteLineColorRGBA"

LineSet748.color = ColorRGBA750

Shape747.geometry = LineSet748

HAnimSegment711.children.append(Shape747)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='skullbase'/> to <HAnimSite name='r_infraorbitale_pt'/>
Shape751 = x3d.Shape()
LineSet752 = x3d.LineSet()
LineSet752.vertexCount = [2]
Coordinate753 = x3d.Coordinate()
Coordinate753.point = (0.0044,1.6209,0.0236,-0.0237,1.6171,0.0752)

LineSet752.coord = Coordinate753
ColorRGBA754 = x3d.ColorRGBA()
ColorRGBA754.USE = "HAnimSiteLineColorRGBA"

LineSet752.color = ColorRGBA754

Shape751.geometry = LineSet752

HAnimSegment711.children.append(Shape751)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='skullbase'/> to <HAnimSite name='l_infraorbitale_pt'/>
Shape755 = x3d.Shape()
LineSet756 = x3d.LineSet()
LineSet756.vertexCount = [2]
Coordinate757 = x3d.Coordinate()
Coordinate757.point = (0.0044,1.6209,0.0236,0.0341,1.6171,0.0752)

LineSet756.coord = Coordinate757
ColorRGBA758 = x3d.ColorRGBA()
ColorRGBA758.USE = "HAnimSiteLineColorRGBA"

LineSet756.color = ColorRGBA758

Shape755.geometry = LineSet756

HAnimSegment711.children.append(Shape755)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='skullbase'/> to <HAnimSite name='supramenton_pt'/>
Shape759 = x3d.Shape()
LineSet760 = x3d.LineSet()
LineSet760.vertexCount = [2]
Coordinate761 = x3d.Coordinate()
Coordinate761.point = (0.0044,1.6209,0.0236,0.0061,1.5410,0.0805)

LineSet760.coord = Coordinate761
ColorRGBA762 = x3d.ColorRGBA()
ColorRGBA762.USE = "HAnimSiteLineColorRGBA"

LineSet760.color = ColorRGBA762

Shape759.geometry = LineSet760

HAnimSegment711.children.append(Shape759)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='skullbase'/> to <HAnimSite name='r_tragion_pt'/>
Shape763 = x3d.Shape()
LineSet764 = x3d.LineSet()
LineSet764.vertexCount = [2]
Coordinate765 = x3d.Coordinate()
Coordinate765.point = (0.0044,1.6209,0.0236,-0.0646,1.6347,0.0302)

LineSet764.coord = Coordinate765
ColorRGBA766 = x3d.ColorRGBA()
ColorRGBA766.USE = "HAnimSiteLineColorRGBA"

LineSet764.color = ColorRGBA766

Shape763.geometry = LineSet764

HAnimSegment711.children.append(Shape763)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='skullbase'/> to <HAnimSite name='r_gonion_pt'/>
Shape767 = x3d.Shape()
LineSet768 = x3d.LineSet()
LineSet768.vertexCount = [2]
Coordinate769 = x3d.Coordinate()
Coordinate769.point = (0.0044,1.6209,0.0236,-0.0520,1.5529,0.0347)

LineSet768.coord = Coordinate769
ColorRGBA770 = x3d.ColorRGBA()
ColorRGBA770.USE = "HAnimSiteLineColorRGBA"

LineSet768.color = ColorRGBA770

Shape767.geometry = LineSet768

HAnimSegment711.children.append(Shape767)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='skullbase'/> to <HAnimSite name='l_tragion_pt'/>
Shape771 = x3d.Shape()
LineSet772 = x3d.LineSet()
LineSet772.vertexCount = [2]
Coordinate773 = x3d.Coordinate()
Coordinate773.point = (0.0044,1.6209,0.0236,0.0739,1.6348,0.0282)

LineSet772.coord = Coordinate773
ColorRGBA774 = x3d.ColorRGBA()
ColorRGBA774.USE = "HAnimSiteLineColorRGBA"

LineSet772.color = ColorRGBA774

Shape771.geometry = LineSet772

HAnimSegment711.children.append(Shape771)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='skullbase'/> to <HAnimSite name='l_gonion_pt'/>
Shape775 = x3d.Shape()
LineSet776 = x3d.LineSet()
LineSet776.vertexCount = [2]
Coordinate777 = x3d.Coordinate()
Coordinate777.point = (0.0044,1.6209,0.0236,0.0631,1.5530,0.0330)

LineSet776.coord = Coordinate777
ColorRGBA778 = x3d.ColorRGBA()
ColorRGBA778.USE = "HAnimSiteLineColorRGBA"

LineSet776.color = ColorRGBA778

Shape775.geometry = LineSet776

HAnimSegment711.children.append(Shape775)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='skullbase'/> to <HAnimSite name='nuchale_pt'/>
Shape779 = x3d.Shape()
LineSet780 = x3d.LineSet()
LineSet780.vertexCount = [2]
Coordinate781 = x3d.Coordinate()
Coordinate781.point = (0.0044,1.6209,0.0236,0.0039,1.5972,-0.0796)

LineSet780.coord = Coordinate781
ColorRGBA782 = x3d.ColorRGBA()
ColorRGBA782.USE = "HAnimSiteLineColorRGBA"

LineSet780.color = ColorRGBA782

Shape779.geometry = LineSet780

HAnimSegment711.children.append(Shape779)
HAnimSite783 = x3d.HAnimSite()
HAnimSite783.name = "skull_vertex_pt"
HAnimSite783.DEF = "hanim_skull_vertex_pt"
HAnimSite783.translation = [0.005,1.7504,0.0055]
#TODO move skull_tip x to zero, check others for symmetry
#HAnimSite visualization shape
TouchSensor784 = x3d.TouchSensor()
TouchSensor784.description = "HAnimSite skull_tip"

HAnimSite783.children.append(TouchSensor784)
Shape785 = x3d.Shape()
Shape785.USE = "HAnimSiteShape"

HAnimSite783.children.append(Shape785)

HAnimSegment711.children.append(HAnimSite783)
HAnimSite786 = x3d.HAnimSite()
HAnimSite786.name = "sellion_pt"
HAnimSite786.DEF = "hanim_sellion_pt"
HAnimSite786.translation = [0.0058,1.6316,0.0852]
#HAnimSite visualization shape
TouchSensor787 = x3d.TouchSensor()
TouchSensor787.description = "HAnimSite sellion_pt"

HAnimSite786.children.append(TouchSensor787)
Shape788 = x3d.Shape()
Shape788.USE = "HAnimSiteShape"

HAnimSite786.children.append(Shape788)

HAnimSegment711.children.append(HAnimSite786)
HAnimSite789 = x3d.HAnimSite()
HAnimSite789.name = "r_infraorbitale_pt"
HAnimSite789.DEF = "hanim_r_infraorbitale_pt"
HAnimSite789.translation = [-0.0237,1.6171,0.0752]
#HAnimSite visualization shape
TouchSensor790 = x3d.TouchSensor()
TouchSensor790.description = "HAnimSite r_infraorbitale_pt"

HAnimSite789.children.append(TouchSensor790)
Shape791 = x3d.Shape()
Shape791.USE = "HAnimSiteShape"

HAnimSite789.children.append(Shape791)

HAnimSegment711.children.append(HAnimSite789)
HAnimSite792 = x3d.HAnimSite()
HAnimSite792.name = "l_infraorbitale_pt"
HAnimSite792.DEF = "hanim_l_infraorbitale_pt"
HAnimSite792.translation = [0.0341,1.6171,0.0752]
#HAnimSite visualization shape
TouchSensor793 = x3d.TouchSensor()
TouchSensor793.description = "HAnimSite l_infraorbitale_pt"

HAnimSite792.children.append(TouchSensor793)
Shape794 = x3d.Shape()
Shape794.USE = "HAnimSiteShape"

HAnimSite792.children.append(Shape794)

HAnimSegment711.children.append(HAnimSite792)
HAnimSite795 = x3d.HAnimSite()
HAnimSite795.name = "supramenton_pt"
HAnimSite795.DEF = "hanim_supramenton_pt"
HAnimSite795.translation = [0.0061,1.541,0.0805]
#HAnimSite visualization shape
TouchSensor796 = x3d.TouchSensor()
TouchSensor796.description = "HAnimSite supramenton_pt"

HAnimSite795.children.append(TouchSensor796)
Shape797 = x3d.Shape()
Shape797.USE = "HAnimSiteShape"

HAnimSite795.children.append(Shape797)

HAnimSegment711.children.append(HAnimSite795)
HAnimSite798 = x3d.HAnimSite()
HAnimSite798.name = "r_tragion_pt"
HAnimSite798.DEF = "hanim_r_tragion_pt"
HAnimSite798.translation = [-0.0646,1.6347,0.0302]
#HAnimSite visualization shape
TouchSensor799 = x3d.TouchSensor()
TouchSensor799.description = "HAnimSite r_tragion_pt"

HAnimSite798.children.append(TouchSensor799)
Shape800 = x3d.Shape()
Shape800.USE = "HAnimSiteShape"

HAnimSite798.children.append(Shape800)

HAnimSegment711.children.append(HAnimSite798)
HAnimSite801 = x3d.HAnimSite()
HAnimSite801.name = "r_gonion_pt"
HAnimSite801.DEF = "hanim_r_gonion_pt"
HAnimSite801.translation = [-0.052,1.5529,0.0347]
#HAnimSite visualization shape
TouchSensor802 = x3d.TouchSensor()
TouchSensor802.description = "HAnimSite r_gonion_pt"

HAnimSite801.children.append(TouchSensor802)
Shape803 = x3d.Shape()
Shape803.USE = "HAnimSiteShape"

HAnimSite801.children.append(Shape803)

HAnimSegment711.children.append(HAnimSite801)
HAnimSite804 = x3d.HAnimSite()
HAnimSite804.name = "l_tragion_pt"
HAnimSite804.DEF = "hanim_l_tragion_pt"
HAnimSite804.translation = [0.0739,1.6348,0.0282]
#HAnimSite visualization shape
TouchSensor805 = x3d.TouchSensor()
TouchSensor805.description = "HAnimSite l_tragion_pt"

HAnimSite804.children.append(TouchSensor805)
Shape806 = x3d.Shape()
Shape806.USE = "HAnimSiteShape"

HAnimSite804.children.append(Shape806)

HAnimSegment711.children.append(HAnimSite804)
HAnimSite807 = x3d.HAnimSite()
HAnimSite807.name = "l_gonion_pt"
HAnimSite807.DEF = "hanim_l_gonion_pt"
HAnimSite807.translation = [0.0631,1.553,0.033]
#HAnimSite visualization shape
TouchSensor808 = x3d.TouchSensor()
TouchSensor808.description = "HAnimSite l_gonion_pt"

HAnimSite807.children.append(TouchSensor808)
Shape809 = x3d.Shape()
Shape809.USE = "HAnimSiteShape"

HAnimSite807.children.append(Shape809)

HAnimSegment711.children.append(HAnimSite807)
HAnimSite810 = x3d.HAnimSite()
HAnimSite810.name = "nuchale_pt"
HAnimSite810.DEF = "hanim_nuchale_pt"
HAnimSite810.translation = [0.0039,1.5972,-0.0796]
#HAnimSite visualization shape
TouchSensor811 = x3d.TouchSensor()
TouchSensor811.description = "HAnimSite nuchale_pt"

HAnimSite810.children.append(TouchSensor811)
Shape812 = x3d.Shape()
Shape812.USE = "HAnimSiteShape"

HAnimSite810.children.append(Shape812)

HAnimSegment711.children.append(HAnimSite810)

HAnimJoint710.children.append(HAnimSegment711)
HAnimJoint813 = x3d.HAnimJoint()
HAnimJoint813.name = "l_eyeball_joint"
HAnimJoint813.DEF = "hanim_l_eyeball_joint"
HAnimJoint813.center = [0.0336,1.6332,0.0502]
HAnimJoint813.ulimit = [0,0,0]
HAnimJoint813.llimit = [0,0,0]
HAnimSegment814 = x3d.HAnimSegment()
HAnimSegment814.name = "l_eyeball"
HAnimSegment814.DEF = "hanim_l_eyeball"
#Visualization sphere for <HAnimJoint name='l_eyeball_joint'/> is placed within <HAnimSegment name='l_eyeball'/>
TouchSensor815 = x3d.TouchSensor()
TouchSensor815.description = "HAnimJoint l_eyeball_joint, HAnimSegment l_eyeball"

HAnimSegment814.children.append(TouchSensor815)
Transform816 = x3d.Transform()
Transform816.translation = [0.0336,1.6332,0.0502]
Shape817 = x3d.Shape()
Shape817.USE = "HAnimJointShape"

Transform816.children.append(Shape817)

HAnimSegment814.children.append(Transform816)
#HAnimSite/Viewpoint visualization line segment from ancestor <HAnimJoint name='l_eyeball_joint'/> to <HAnimSite name='l_eyeball_site_view'/>
Shape818 = x3d.Shape()
LineSet819 = x3d.LineSet()
LineSet819.vertexCount = [2]
Coordinate820 = x3d.Coordinate()
Coordinate820.point = (0.0336,1.6332,0.0502,0.0340,1.6400,0.0500)

LineSet819.coord = Coordinate820
ColorRGBA821 = x3d.ColorRGBA()
ColorRGBA821.DEF = "HAnimSiteViewpointLineColorRGBA"
ColorRGBA821.color = [1,1,0,1,1,1,0,0.1]

LineSet819.color = ColorRGBA821

Shape818.geometry = LineSet819

HAnimSegment814.children.append(Shape818)
HAnimSite822 = x3d.HAnimSite()
HAnimSite822.name = "l_eyeball_site_view"
HAnimSite822.DEF = "hanim_l_eyeball_site_view"
HAnimSite822.translation = [0.034,1.64,0.05]
#HAnimSite visualization shape
TouchSensor823 = x3d.TouchSensor()
TouchSensor823.description = "HAnimSite l_eyeball_site_view"

HAnimSite822.children.append(TouchSensor823)
Shape824 = x3d.Shape()
Shape824.USE = "HAnimSiteShape"

HAnimSite822.children.append(Shape824)
Viewpoint825 = x3d.Viewpoint()
Viewpoint825.DEF = "hanim_l_eyeball_site_viewpoint"
Viewpoint825.description = "l_eyeball_site_viewpoint looking forward"
Viewpoint825.orientation = [0,1,0,3.141593]
Viewpoint825.position = [0,0,0]

HAnimSite822.children.append(Viewpoint825)
#HAnimSite/Viewpoint visualization shape
Anchor826 = x3d.Anchor()
Anchor826.description = "HAnimSite hanim_l_eyeball_site_view Viewpoint"
Anchor826.url = ["#hanim_l_eyeball_site_viewpoint"]
LOD827 = x3d.LOD()
LOD827.forceTransitions = True
LOD827.range = [0.04]
WorldInfo828 = x3d.WorldInfo()
WorldInfo828.info = ["hide diamond when close"]

LOD827.children.append(WorldInfo828)
Shape829 = x3d.Shape()
Shape829.DEF = "HAnimSiteViewpointShape"
IndexedFaceSet830 = x3d.IndexedFaceSet()
IndexedFaceSet830.DEF = "SiteViewpointDiamondIFS"
IndexedFaceSet830.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet830.creaseAngle = 0.5
Coordinate831 = x3d.Coordinate()
Coordinate831.point = (0.0000,0.0100,0.0000,-0.0100,0.0000,0.0000,0.0000,0.0000,0.0100,0.0100,0.0000,0.0000,0.0000,0.0000,-0.0100,0.0000,-0.0100,0.0000)

IndexedFaceSet830.coord = Coordinate831

Shape829.geometry = IndexedFaceSet830
Appearance832 = x3d.Appearance()
Material833 = x3d.Material()
Material833.diffuseColor = [1,1,0]
Material833.transparency = 0.3

Appearance832.material = Material833

Shape829.appearance = Appearance832

LOD827.children.append(Shape829)

Anchor826.children.append(LOD827)

HAnimSite822.children.append(Anchor826)

HAnimSegment814.children.append(HAnimSite822)

HAnimJoint813.children.append(HAnimSegment814)

HAnimJoint710.children.append(HAnimJoint813)
HAnimJoint834 = x3d.HAnimJoint()
HAnimJoint834.name = "l_eyelid_joint"
HAnimJoint834.DEF = "hanim_l_eyelid_joint"
HAnimJoint834.center = [0.0336,1.6332,0.0502]
HAnimJoint834.ulimit = [0,0,0]
HAnimJoint834.llimit = [0,0,0]
HAnimSegment835 = x3d.HAnimSegment()
HAnimSegment835.name = "l_eyelid"
HAnimSegment835.DEF = "hanim_l_eyelid"
#Visualization sphere for <HAnimJoint name='l_eyelid_joint'/> is placed within <HAnimSegment name='l_eyelid'/>
TouchSensor836 = x3d.TouchSensor()
TouchSensor836.description = "HAnimJoint l_eyelid_joint, HAnimSegment l_eyelid"

HAnimSegment835.children.append(TouchSensor836)
Transform837 = x3d.Transform()
Transform837.translation = [0.0336,1.6332,0.0502]
Shape838 = x3d.Shape()
Shape838.USE = "HAnimJointShape"

Transform837.children.append(Shape838)

HAnimSegment835.children.append(Transform837)

HAnimJoint834.children.append(HAnimSegment835)

HAnimJoint710.children.append(HAnimJoint834)
HAnimJoint839 = x3d.HAnimJoint()
HAnimJoint839.name = "l_eyebrow_joint"
HAnimJoint839.DEF = "hanim_l_eyebrow_joint"
HAnimJoint839.center = [0.0336,1.635,0.0506]
HAnimJoint839.ulimit = [0,0,0]
HAnimJoint839.llimit = [0,0,0]
HAnimSegment840 = x3d.HAnimSegment()
HAnimSegment840.name = "l_eyebrow"
HAnimSegment840.DEF = "hanim_l_eyebrow"
#Visualization sphere for <HAnimJoint name='l_eyebrow_joint'/> is placed within <HAnimSegment name='l_eyebrow'/>
TouchSensor841 = x3d.TouchSensor()
TouchSensor841.description = "HAnimJoint l_eyebrow_joint, HAnimSegment l_eyebrow"

HAnimSegment840.children.append(TouchSensor841)
Transform842 = x3d.Transform()
Transform842.translation = [0.0336,1.635,0.0506]
Shape843 = x3d.Shape()
Shape843.USE = "HAnimJointShape"

Transform842.children.append(Shape843)

HAnimSegment840.children.append(Transform842)

HAnimJoint839.children.append(HAnimSegment840)

HAnimJoint710.children.append(HAnimJoint839)
HAnimJoint844 = x3d.HAnimJoint()
HAnimJoint844.name = "r_eyeball_joint"
HAnimJoint844.DEF = "hanim_r_eyeball_joint"
HAnimJoint844.center = [-0.0336,1.6332,0.0502]
HAnimJoint844.ulimit = [0,0,0]
HAnimJoint844.llimit = [0,0,0]
HAnimSegment845 = x3d.HAnimSegment()
HAnimSegment845.name = "r_eyeball"
HAnimSegment845.DEF = "hanim_r_eyeball"
#Visualization sphere for <HAnimJoint name='r_eyeball_joint'/> is placed within <HAnimSegment name='r_eyeball'/>
TouchSensor846 = x3d.TouchSensor()
TouchSensor846.description = "HAnimJoint r_eyeball_joint, HAnimSegment r_eyeball"

HAnimSegment845.children.append(TouchSensor846)
Transform847 = x3d.Transform()
Transform847.translation = [-0.0336,1.6332,0.0502]
Shape848 = x3d.Shape()
Shape848.USE = "HAnimJointShape"

Transform847.children.append(Shape848)

HAnimSegment845.children.append(Transform847)
#HAnimSite/Viewpoint visualization line segment from ancestor <HAnimJoint name='r_eyeball_joint'/> to <HAnimSite name='r_eyeball_site_view'/>
Shape849 = x3d.Shape()
LineSet850 = x3d.LineSet()
LineSet850.vertexCount = [2]
Coordinate851 = x3d.Coordinate()
Coordinate851.point = (-0.0336,1.6332,0.0502,-0.0340,1.6400,0.0500)

LineSet850.coord = Coordinate851
ColorRGBA852 = x3d.ColorRGBA()
ColorRGBA852.USE = "HAnimSiteViewpointLineColorRGBA"

LineSet850.color = ColorRGBA852

Shape849.geometry = LineSet850

HAnimSegment845.children.append(Shape849)
HAnimSite853 = x3d.HAnimSite()
HAnimSite853.name = "r_eyeball_site_view"
HAnimSite853.DEF = "hanim_r_eyeball_site_view"
HAnimSite853.translation = [-0.034,1.64,0.05]
#HAnimSite visualization shape
TouchSensor854 = x3d.TouchSensor()
TouchSensor854.description = "HAnimSite r_eyeball_site_view"

HAnimSite853.children.append(TouchSensor854)
Shape855 = x3d.Shape()
Shape855.USE = "HAnimSiteShape"

HAnimSite853.children.append(Shape855)
Viewpoint856 = x3d.Viewpoint()
Viewpoint856.DEF = "hanim_r_eyeball_site_viewpoint"
Viewpoint856.description = "r_eyeball_site_viewpoint looking forward"
Viewpoint856.orientation = [0,1,0,3.141593]
Viewpoint856.position = [0,0,0]

HAnimSite853.children.append(Viewpoint856)
#HAnimSite/Viewpoint visualization shape
Anchor857 = x3d.Anchor()
Anchor857.description = "HAnimSite hanim_r_eyeball_site_view Viewpoint"
Anchor857.url = ["#hanim_r_eyeball_site_viewpoint"]
LOD858 = x3d.LOD()
LOD858.forceTransitions = True
LOD858.range = [0.04]
WorldInfo859 = x3d.WorldInfo()
WorldInfo859.info = ["hide diamond when close"]

LOD858.children.append(WorldInfo859)
Shape860 = x3d.Shape()
Shape860.USE = "HAnimSiteViewpointShape"

LOD858.children.append(Shape860)

Anchor857.children.append(LOD858)

HAnimSite853.children.append(Anchor857)

HAnimSegment845.children.append(HAnimSite853)

HAnimJoint844.children.append(HAnimSegment845)

HAnimJoint710.children.append(HAnimJoint844)
HAnimJoint861 = x3d.HAnimJoint()
HAnimJoint861.name = "r_eyelid_joint"
HAnimJoint861.DEF = "hanim_r_eyelid_joint"
HAnimJoint861.center = [-0.0336,1.6332,0.0502]
HAnimJoint861.ulimit = [0,0,0]
HAnimJoint861.llimit = [0,0,0]
HAnimSegment862 = x3d.HAnimSegment()
HAnimSegment862.name = "r_eyelid"
HAnimSegment862.DEF = "hanim_r_eyelid"
#Visualization sphere for <HAnimJoint name='r_eyelid_joint'/> is placed within <HAnimSegment name='r_eyelid'/>
TouchSensor863 = x3d.TouchSensor()
TouchSensor863.description = "HAnimJoint r_eyelid_joint, HAnimSegment r_eyelid"

HAnimSegment862.children.append(TouchSensor863)
Transform864 = x3d.Transform()
Transform864.translation = [-0.0336,1.6332,0.0502]
Shape865 = x3d.Shape()
Shape865.USE = "HAnimJointShape"

Transform864.children.append(Shape865)

HAnimSegment862.children.append(Transform864)

HAnimJoint861.children.append(HAnimSegment862)

HAnimJoint710.children.append(HAnimJoint861)
HAnimJoint866 = x3d.HAnimJoint()
HAnimJoint866.name = "r_eyebrow_joint"
HAnimJoint866.DEF = "hanim_r_eyebrow_joint"
HAnimJoint866.center = [-0.0336,1.635,0.0506]
HAnimJoint866.ulimit = [0,0,0]
HAnimJoint866.llimit = [0,0,0]
HAnimSegment867 = x3d.HAnimSegment()
HAnimSegment867.name = "r_eyebrow"
HAnimSegment867.DEF = "hanim_r_eyebrow"
#Visualization sphere for <HAnimJoint name='r_eyebrow_joint'/> is placed within <HAnimSegment name='r_eyebrow'/>
TouchSensor868 = x3d.TouchSensor()
TouchSensor868.description = "HAnimJoint r_eyebrow_joint, HAnimSegment r_eyebrow"

HAnimSegment867.children.append(TouchSensor868)
Transform869 = x3d.Transform()
Transform869.translation = [-0.0336,1.635,0.0506]
Shape870 = x3d.Shape()
Shape870.USE = "HAnimJointShape"

Transform869.children.append(Shape870)

HAnimSegment867.children.append(Transform869)

HAnimJoint866.children.append(HAnimSegment867)

HAnimJoint710.children.append(HAnimJoint866)
HAnimJoint871 = x3d.HAnimJoint()
HAnimJoint871.name = "temporomandibular"
HAnimJoint871.DEF = "hanim_temporomandibular"
HAnimJoint871.center = [0,1.63,0.015]
HAnimJoint871.ulimit = [0,0,0]
HAnimJoint871.llimit = [0,0,0]
#Single joint, single segment for jaw, two sites for left/right TMJs https://en.wikipedia.org/wiki/Temporomandibular_joint
HAnimSegment872 = x3d.HAnimSegment()
HAnimSegment872.name = "jaw"
HAnimSegment872.DEF = "hanim_jaw"
#Visualization sphere for <HAnimJoint name='temporomandibular'/> is placed within <HAnimSegment name='jaw'/>
TouchSensor873 = x3d.TouchSensor()
TouchSensor873.description = "HAnimJoint temporomandibular, HAnimSegment jaw"

HAnimSegment872.children.append(TouchSensor873)
Transform874 = x3d.Transform()
Transform874.translation = [0,1.63,0.015]
Shape875 = x3d.Shape()
Shape875.USE = "HAnimJointShape"

Transform874.children.append(Shape875)

HAnimSegment872.children.append(Transform874)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='temporomandibular'/> to <HAnimSite name='temporomandibular_l_site_pt'/>
Shape876 = x3d.Shape()
LineSet877 = x3d.LineSet()
LineSet877.vertexCount = [2]
Coordinate878 = x3d.Coordinate()
Coordinate878.point = (0.0000,1.6300,0.0150,0.0450,1.6300,0.0000)

LineSet877.coord = Coordinate878
ColorRGBA879 = x3d.ColorRGBA()
ColorRGBA879.USE = "HAnimSiteLineColorRGBA"

LineSet877.color = ColorRGBA879

Shape876.geometry = LineSet877

HAnimSegment872.children.append(Shape876)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='temporomandibular'/> to <HAnimSite name='temporomandibular_r_site_pt'/>
Shape880 = x3d.Shape()
LineSet881 = x3d.LineSet()
LineSet881.vertexCount = [2]
Coordinate882 = x3d.Coordinate()
Coordinate882.point = (0.0000,1.6300,0.0150,-0.0450,1.6300,0.0000)

LineSet881.coord = Coordinate882
ColorRGBA883 = x3d.ColorRGBA()
ColorRGBA883.USE = "HAnimSiteLineColorRGBA"

LineSet881.color = ColorRGBA883

Shape880.geometry = LineSet881

HAnimSegment872.children.append(Shape880)
HAnimSite884 = x3d.HAnimSite()
HAnimSite884.name = "temporomandibular_l_site_pt"
HAnimSite884.DEF = "hanim_temporomandibular_l_site_pt"
HAnimSite884.translation = [0.045,1.63,0]
#HAnimSite visualization shape
TouchSensor885 = x3d.TouchSensor()
TouchSensor885.description = "HAnimSite temporomandibular_l_site_pt"

HAnimSite884.children.append(TouchSensor885)
Shape886 = x3d.Shape()
Shape886.USE = "HAnimSiteShape"

HAnimSite884.children.append(Shape886)

HAnimSegment872.children.append(HAnimSite884)
HAnimSite887 = x3d.HAnimSite()
HAnimSite887.name = "temporomandibular_r_site_pt"
HAnimSite887.DEF = "hanim_temporomandibular_r_site_pt"
HAnimSite887.translation = [-0.045,1.63,0]
#HAnimSite visualization shape
TouchSensor888 = x3d.TouchSensor()
TouchSensor888.description = "HAnimSite temporomandibular_r_site_pt"

HAnimSite887.children.append(TouchSensor888)
Shape889 = x3d.Shape()
Shape889.USE = "HAnimSiteShape"

HAnimSite887.children.append(Shape889)

HAnimSegment872.children.append(HAnimSite887)

HAnimJoint871.children.append(HAnimSegment872)

HAnimJoint710.children.append(HAnimJoint871)

HAnimJoint701.children.append(HAnimJoint710)

HAnimJoint692.children.append(HAnimJoint701)

HAnimJoint683.children.append(HAnimJoint692)

HAnimJoint674.children.append(HAnimJoint683)

HAnimJoint665.children.append(HAnimJoint674)

HAnimJoint656.children.append(HAnimJoint665)

HAnimJoint633.children.append(HAnimJoint656)

HAnimJoint602.children.append(HAnimJoint633)
HAnimJoint890 = x3d.HAnimJoint()
HAnimJoint890.name = "l_sternoclavicular"
HAnimJoint890.DEF = "hanim_l_sternoclavicular"
HAnimJoint890.center = [0.082,1.4488,-0.0353]
HAnimJoint890.ulimit = [0,0,0]
HAnimJoint890.llimit = [0,0,0]
HAnimSegment891 = x3d.HAnimSegment()
HAnimSegment891.name = "l_clavicle"
HAnimSegment891.DEF = "hanim_l_clavicle"
#Visualization sphere for <HAnimJoint name='l_sternoclavicular'/> is placed within <HAnimSegment name='l_clavicle'/>
TouchSensor892 = x3d.TouchSensor()
TouchSensor892.description = "HAnimJoint l_sternoclavicular, HAnimSegment l_clavicle"

HAnimSegment891.children.append(TouchSensor892)
Transform893 = x3d.Transform()
Transform893.translation = [0.082,1.4488,-0.0353]
Shape894 = x3d.Shape()
Shape894.USE = "HAnimJointShape"

Transform893.children.append(Shape894)

HAnimSegment891.children.append(Transform893)
#HAnimSegment visualization line from current <HAnimJoint name='l_sternoclavicular'/> to child <HAnimJoint name='l_acromioclavicular'/>
Shape895 = x3d.Shape()
LineSet896 = x3d.LineSet()
LineSet896.vertexCount = [2]
Coordinate897 = x3d.Coordinate()
Coordinate897.point = (0.0820,1.4488,-0.0353,0.0962,1.4269,-0.0424)

LineSet896.coord = Coordinate897
ColorRGBA898 = x3d.ColorRGBA()
ColorRGBA898.USE = "HAnimSegmentLineColorRGBA"

LineSet896.color = ColorRGBA898

Shape895.geometry = LineSet896

HAnimSegment891.children.append(Shape895)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_sternoclavicular'/> to <HAnimSite name='l_clavicale_pt'/>
Shape899 = x3d.Shape()
LineSet900 = x3d.LineSet()
LineSet900.vertexCount = [2]
Coordinate901 = x3d.Coordinate()
Coordinate901.point = (0.0820,1.4488,-0.0353,0.0271,1.4943,0.0394)

LineSet900.coord = Coordinate901
ColorRGBA902 = x3d.ColorRGBA()
ColorRGBA902.USE = "HAnimSiteLineColorRGBA"

LineSet900.color = ColorRGBA902

Shape899.geometry = LineSet900

HAnimSegment891.children.append(Shape899)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_sternoclavicular'/> to <HAnimSite name='l_acromion_pt'/>
Shape903 = x3d.Shape()
LineSet904 = x3d.LineSet()
LineSet904.vertexCount = [2]
Coordinate905 = x3d.Coordinate()
Coordinate905.point = (0.0820,1.4488,-0.0353,0.2032,1.4760,-0.0490)

LineSet904.coord = Coordinate905
ColorRGBA906 = x3d.ColorRGBA()
ColorRGBA906.USE = "HAnimSiteLineColorRGBA"

LineSet904.color = ColorRGBA906

Shape903.geometry = LineSet904

HAnimSegment891.children.append(Shape903)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_sternoclavicular'/> to <HAnimSite name='l_axilla_ant_pt'/>
Shape907 = x3d.Shape()
LineSet908 = x3d.LineSet()
LineSet908.vertexCount = [2]
Coordinate909 = x3d.Coordinate()
Coordinate909.point = (0.0820,1.4488,-0.0353,0.1777,1.4065,-0.0075)

LineSet908.coord = Coordinate909
ColorRGBA910 = x3d.ColorRGBA()
ColorRGBA910.USE = "HAnimSiteLineColorRGBA"

LineSet908.color = ColorRGBA910

Shape907.geometry = LineSet908

HAnimSegment891.children.append(Shape907)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_sternoclavicular'/> to <HAnimSite name='l_axilla_post_pt'/>
Shape911 = x3d.Shape()
LineSet912 = x3d.LineSet()
LineSet912.vertexCount = [2]
Coordinate913 = x3d.Coordinate()
Coordinate913.point = (0.0820,1.4488,-0.0353,0.1706,1.4072,-0.0875)

LineSet912.coord = Coordinate913
ColorRGBA914 = x3d.ColorRGBA()
ColorRGBA914.USE = "HAnimSiteLineColorRGBA"

LineSet912.color = ColorRGBA914

Shape911.geometry = LineSet912

HAnimSegment891.children.append(Shape911)
HAnimSite915 = x3d.HAnimSite()
HAnimSite915.name = "l_clavicle_pt"
HAnimSite915.DEF = "hanim_l_clavicle_pt"
HAnimSite915.translation = [0.0271,1.4943,0.0394]
#HAnimSite visualization shape
TouchSensor916 = x3d.TouchSensor()
TouchSensor916.description = "HAnimSite l_clavicale_pt"

HAnimSite915.children.append(TouchSensor916)
Shape917 = x3d.Shape()
Shape917.USE = "HAnimSiteShape"

HAnimSite915.children.append(Shape917)

HAnimSegment891.children.append(HAnimSite915)
HAnimSite918 = x3d.HAnimSite()
HAnimSite918.name = "l_acromion_pt"
HAnimSite918.DEF = "hanim_l_acromion_pt"
HAnimSite918.translation = [0.2032,1.476,-0.049]
#HAnimSite visualization shape
TouchSensor919 = x3d.TouchSensor()
TouchSensor919.description = "HAnimSite l_acromion_pt"

HAnimSite918.children.append(TouchSensor919)
Shape920 = x3d.Shape()
Shape920.USE = "HAnimSiteShape"

HAnimSite918.children.append(Shape920)

HAnimSegment891.children.append(HAnimSite918)
HAnimSite921 = x3d.HAnimSite()
HAnimSite921.name = "l_axilla_proximal_pt"
HAnimSite921.DEF = "hanim_l_axilla_proximal_pt"
HAnimSite921.translation = [0.1777,1.4065,-0.0075]
#HAnimSite visualization shape
TouchSensor922 = x3d.TouchSensor()
TouchSensor922.description = "HAnimSite l_axilla_ant_pt"

HAnimSite921.children.append(TouchSensor922)
Shape923 = x3d.Shape()
Shape923.USE = "HAnimSiteShape"

HAnimSite921.children.append(Shape923)

HAnimSegment891.children.append(HAnimSite921)
HAnimSite924 = x3d.HAnimSite()
HAnimSite924.name = "l_axilla_distal_pt"
HAnimSite924.DEF = "hanim_l_axilla_distal_pt"
HAnimSite924.translation = [0.1706,1.4072,-0.0875]
#HAnimSite visualization shape
TouchSensor925 = x3d.TouchSensor()
TouchSensor925.description = "HAnimSite l_axilla_post_pt"

HAnimSite924.children.append(TouchSensor925)
Shape926 = x3d.Shape()
Shape926.USE = "HAnimSiteShape"

HAnimSite924.children.append(Shape926)

HAnimSegment891.children.append(HAnimSite924)

HAnimJoint890.children.append(HAnimSegment891)
HAnimJoint927 = x3d.HAnimJoint()
HAnimJoint927.name = "l_acromioclavicular"
HAnimJoint927.DEF = "hanim_l_acromioclavicular"
HAnimJoint927.center = [0.0962,1.4269,-0.0424]
HAnimJoint927.ulimit = [0,0,0]
HAnimJoint927.llimit = [0,0,0]
HAnimSegment928 = x3d.HAnimSegment()
HAnimSegment928.name = "l_scapula"
HAnimSegment928.DEF = "hanim_l_scapula"
#Visualization sphere for <HAnimJoint name='l_acromioclavicular'/> is placed within <HAnimSegment name='l_scapula'/>
TouchSensor929 = x3d.TouchSensor()
TouchSensor929.description = "HAnimJoint l_acromioclavicular, HAnimSegment l_scapula"

HAnimSegment928.children.append(TouchSensor929)
Transform930 = x3d.Transform()
Transform930.translation = [0.0962,1.4269,-0.0424]
Shape931 = x3d.Shape()
Shape931.USE = "HAnimJointShape"

Transform930.children.append(Shape931)

HAnimSegment928.children.append(Transform930)
#HAnimSegment visualization line from current <HAnimJoint name='l_acromioclavicular'/> to child <HAnimJoint name='l_shoulder'/>
Shape932 = x3d.Shape()
LineSet933 = x3d.LineSet()
LineSet933.vertexCount = [2]
Coordinate934 = x3d.Coordinate()
Coordinate934.point = (0.0962,1.4269,-0.0424,0.2029,1.4376,-0.0387)

LineSet933.coord = Coordinate934
ColorRGBA935 = x3d.ColorRGBA()
ColorRGBA935.USE = "HAnimSegmentLineColorRGBA"

LineSet933.color = ColorRGBA935

Shape932.geometry = LineSet933

HAnimSegment928.children.append(Shape932)

HAnimJoint927.children.append(HAnimSegment928)
HAnimJoint936 = x3d.HAnimJoint()
HAnimJoint936.name = "l_shoulder"
HAnimJoint936.DEF = "hanim_l_shoulder"
HAnimJoint936.center = [0.2029,1.4376,-0.0387]
HAnimJoint936.ulimit = [0,0,0]
HAnimJoint936.llimit = [0,0,0]
HAnimSegment937 = x3d.HAnimSegment()
HAnimSegment937.name = "l_upperarm"
HAnimSegment937.DEF = "hanim_l_upperarm"
#Visualization sphere for <HAnimJoint name='l_shoulder'/> is placed within <HAnimSegment name='l_upperarm'/>
TouchSensor938 = x3d.TouchSensor()
TouchSensor938.description = "HAnimJoint l_shoulder, HAnimSegment l_upperarm"

HAnimSegment937.children.append(TouchSensor938)
Transform939 = x3d.Transform()
Transform939.translation = [0.2029,1.4376,-0.0387]
Shape940 = x3d.Shape()
Shape940.USE = "HAnimJointShape"

Transform939.children.append(Shape940)

HAnimSegment937.children.append(Transform939)
#HAnimSegment visualization line from current <HAnimJoint name='l_shoulder'/> to child <HAnimJoint name='l_elbow'/>
Shape941 = x3d.Shape()
LineSet942 = x3d.LineSet()
LineSet942.vertexCount = [2]
Coordinate943 = x3d.Coordinate()
Coordinate943.point = (0.2029,1.4376,-0.0387,0.2014,1.1357,-0.0682)

LineSet942.coord = Coordinate943
ColorRGBA944 = x3d.ColorRGBA()
ColorRGBA944.USE = "HAnimSegmentLineColorRGBA"

LineSet942.color = ColorRGBA944

Shape941.geometry = LineSet942

HAnimSegment937.children.append(Shape941)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_shoulder'/> to <HAnimSite name='l_humeral_lateral_epicn_pt'/>
Shape945 = x3d.Shape()
LineSet946 = x3d.LineSet()
LineSet946.vertexCount = [2]
Coordinate947 = x3d.Coordinate()
Coordinate947.point = (0.2029,1.4376,-0.0387,0.2280,1.1482,-0.1100)

LineSet946.coord = Coordinate947
ColorRGBA948 = x3d.ColorRGBA()
ColorRGBA948.USE = "HAnimSiteLineColorRGBA"

LineSet946.color = ColorRGBA948

Shape945.geometry = LineSet946

HAnimSegment937.children.append(Shape945)
HAnimSite949 = x3d.HAnimSite()
HAnimSite949.name = "l_humeral_lateral_epicondyle_pt"
HAnimSite949.DEF = "hanim_l_humeral_lateral_epicondyle_pt"
HAnimSite949.translation = [0.228,1.1482,-0.11]
#HAnimSite visualization shape
TouchSensor950 = x3d.TouchSensor()
TouchSensor950.description = "HAnimSite l_humeral_lateral_epicn_pt"

HAnimSite949.children.append(TouchSensor950)
Shape951 = x3d.Shape()
Shape951.USE = "HAnimSiteShape"

HAnimSite949.children.append(Shape951)

HAnimSegment937.children.append(HAnimSite949)

HAnimJoint936.children.append(HAnimSegment937)
HAnimJoint952 = x3d.HAnimJoint()
HAnimJoint952.name = "l_elbow"
HAnimJoint952.DEF = "hanim_l_elbow"
HAnimJoint952.center = [0.2014,1.1357,-0.0682]
HAnimJoint952.ulimit = [0,0,0]
HAnimJoint952.llimit = [0,0,0]
HAnimSegment953 = x3d.HAnimSegment()
HAnimSegment953.name = "l_forearm"
HAnimSegment953.DEF = "hanim_l_forearm"
#Visualization sphere for <HAnimJoint name='l_elbow'/> is placed within <HAnimSegment name='l_forearm'/>
TouchSensor954 = x3d.TouchSensor()
TouchSensor954.description = "HAnimJoint l_elbow, HAnimSegment l_forearm"

HAnimSegment953.children.append(TouchSensor954)
Transform955 = x3d.Transform()
Transform955.translation = [0.2014,1.1357,-0.0682]
Shape956 = x3d.Shape()
Shape956.USE = "HAnimJointShape"

Transform955.children.append(Shape956)

HAnimSegment953.children.append(Transform955)
#HAnimSegment visualization line from current <HAnimJoint name='l_elbow'/> to child <HAnimJoint name='l_radiocarpal'/>
Shape957 = x3d.Shape()
LineSet958 = x3d.LineSet()
LineSet958.vertexCount = [2]
Coordinate959 = x3d.Coordinate()
Coordinate959.point = (0.2014,1.1357,-0.0682,0.1984,0.8663,-0.0583)

LineSet958.coord = Coordinate959
ColorRGBA960 = x3d.ColorRGBA()
ColorRGBA960.USE = "HAnimSegmentLineColorRGBA"

LineSet958.color = ColorRGBA960

Shape957.geometry = LineSet958

HAnimSegment953.children.append(Shape957)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_elbow'/> to <HAnimSite name='l_radial_styloid_pt'/>
Shape961 = x3d.Shape()
LineSet962 = x3d.LineSet()
LineSet962.vertexCount = [2]
Coordinate963 = x3d.Coordinate()
Coordinate963.point = (0.2014,1.1357,-0.0682,0.1901,0.8645,-0.0415)

LineSet962.coord = Coordinate963
ColorRGBA964 = x3d.ColorRGBA()
ColorRGBA964.USE = "HAnimSiteLineColorRGBA"

LineSet962.color = ColorRGBA964

Shape961.geometry = LineSet962

HAnimSegment953.children.append(Shape961)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_elbow'/> to <HAnimSite name='l_olecranon_pt'/>
Shape965 = x3d.Shape()
LineSet966 = x3d.LineSet()
LineSet966.vertexCount = [2]
Coordinate967 = x3d.Coordinate()
Coordinate967.point = (0.2014,1.1357,-0.0682,0.1962,1.1375,-0.1123)

LineSet966.coord = Coordinate967
ColorRGBA968 = x3d.ColorRGBA()
ColorRGBA968.USE = "HAnimSiteLineColorRGBA"

LineSet966.color = ColorRGBA968

Shape965.geometry = LineSet966

HAnimSegment953.children.append(Shape965)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_elbow'/> to <HAnimSite name='l_humeral_medial_epicn_pt'/>
Shape969 = x3d.Shape()
LineSet970 = x3d.LineSet()
LineSet970.vertexCount = [2]
Coordinate971 = x3d.Coordinate()
Coordinate971.point = (0.2014,1.1357,-0.0682,0.1735,1.1272,-0.1113)

LineSet970.coord = Coordinate971
ColorRGBA972 = x3d.ColorRGBA()
ColorRGBA972.USE = "HAnimSiteLineColorRGBA"

LineSet970.color = ColorRGBA972

Shape969.geometry = LineSet970

HAnimSegment953.children.append(Shape969)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_elbow'/> to <HAnimSite name='l_radiale_pt'/>
Shape973 = x3d.Shape()
LineSet974 = x3d.LineSet()
LineSet974.vertexCount = [2]
Coordinate975 = x3d.Coordinate()
Coordinate975.point = (0.2014,1.1357,-0.0682,0.2182,1.1212,-0.1167)

LineSet974.coord = Coordinate975
ColorRGBA976 = x3d.ColorRGBA()
ColorRGBA976.USE = "HAnimSiteLineColorRGBA"

LineSet974.color = ColorRGBA976

Shape973.geometry = LineSet974

HAnimSegment953.children.append(Shape973)
HAnimSite977 = x3d.HAnimSite()
HAnimSite977.name = "l_radial_styloid_pt"
HAnimSite977.DEF = "hanim_l_radial_styloid_pt"
HAnimSite977.translation = [0.1901,0.8645,-0.0415]
#HAnimSite visualization shape
TouchSensor978 = x3d.TouchSensor()
TouchSensor978.description = "HAnimSite l_radial_styloid_pt"

HAnimSite977.children.append(TouchSensor978)
Shape979 = x3d.Shape()
Shape979.USE = "HAnimSiteShape"

HAnimSite977.children.append(Shape979)

HAnimSegment953.children.append(HAnimSite977)
HAnimSite980 = x3d.HAnimSite()
HAnimSite980.name = "l_olecranon_pt"
HAnimSite980.DEF = "hanim_l_olecranon_pt"
HAnimSite980.translation = [0.1962,1.1375,-0.1123]
#HAnimSite visualization shape
TouchSensor981 = x3d.TouchSensor()
TouchSensor981.description = "HAnimSite l_olecranon_pt"

HAnimSite980.children.append(TouchSensor981)
Shape982 = x3d.Shape()
Shape982.USE = "HAnimSiteShape"

HAnimSite980.children.append(Shape982)

HAnimSegment953.children.append(HAnimSite980)
HAnimSite983 = x3d.HAnimSite()
HAnimSite983.name = "l_humeral_medial_epicondyle_pt"
HAnimSite983.DEF = "hanim_l_humeral_medial_epicondyle_pt"
HAnimSite983.translation = [0.1735,1.1272,-0.1113]
#HAnimSite visualization shape
TouchSensor984 = x3d.TouchSensor()
TouchSensor984.description = "HAnimSite l_humeral_medial_epicn_pt"

HAnimSite983.children.append(TouchSensor984)
Shape985 = x3d.Shape()
Shape985.USE = "HAnimSiteShape"

HAnimSite983.children.append(Shape985)

HAnimSegment953.children.append(HAnimSite983)
HAnimSite986 = x3d.HAnimSite()
HAnimSite986.name = "l_radiale_pt"
HAnimSite986.DEF = "hanim_l_radiale_pt"
HAnimSite986.translation = [0.2182,1.1212,-0.1167]
#HAnimSite visualization shape
TouchSensor987 = x3d.TouchSensor()
TouchSensor987.description = "HAnimSite l_radiale_pt"

HAnimSite986.children.append(TouchSensor987)
Shape988 = x3d.Shape()
Shape988.USE = "HAnimSiteShape"

HAnimSite986.children.append(Shape988)

HAnimSegment953.children.append(HAnimSite986)

HAnimJoint952.children.append(HAnimSegment953)
HAnimJoint989 = x3d.HAnimJoint()
HAnimJoint989.name = "l_radiocarpal"
HAnimJoint989.DEF = "hanim_l_radiocarpal"
HAnimJoint989.center = [0.1984,0.8663,-0.0583]
HAnimJoint989.ulimit = [0,0,0]
HAnimJoint989.llimit = [0,0,0]
HAnimSegment990 = x3d.HAnimSegment()
HAnimSegment990.name = "l_carpal"
HAnimSegment990.DEF = "hanim_l_carpal"
#Visualization sphere for <HAnimJoint name='l_radiocarpal'/> is placed within <HAnimSegment name='l_carpal'/>
TouchSensor991 = x3d.TouchSensor()
TouchSensor991.description = "HAnimJoint l_radiocarpal, HAnimSegment l_carpal"

HAnimSegment990.children.append(TouchSensor991)
Transform992 = x3d.Transform()
Transform992.translation = [0.1984,0.8663,-0.0583]
Shape993 = x3d.Shape()
Shape993.USE = "HAnimJointShape"

Transform992.children.append(Shape993)

HAnimSegment990.children.append(Transform992)
#HAnimSegment visualization line from current <HAnimJoint name='l_radiocarpal'/> to child <HAnimJoint name='l_thumb1'/>
Shape994 = x3d.Shape()
LineSet995 = x3d.LineSet()
LineSet995.vertexCount = [2]
Coordinate996 = x3d.Coordinate()
Coordinate996.point = (0.1984,0.8663,-0.0583,0.1924,0.8472,-0.0534)

LineSet995.coord = Coordinate996
ColorRGBA997 = x3d.ColorRGBA()
ColorRGBA997.USE = "HAnimSegmentLineColorRGBA"

LineSet995.color = ColorRGBA997

Shape994.geometry = LineSet995

HAnimSegment990.children.append(Shape994)
#HAnimSegment visualization line from current <HAnimJoint name='l_radiocarpal'/> to child <HAnimJoint name='l_index0'/>
Shape998 = x3d.Shape()
LineSet999 = x3d.LineSet()
LineSet999.vertexCount = [2]
Coordinate1000 = x3d.Coordinate()
Coordinate1000.point = (0.1984,0.8663,-0.0583,0.1983,0.8024,-0.0280)

LineSet999.coord = Coordinate1000
ColorRGBA1001 = x3d.ColorRGBA()
ColorRGBA1001.USE = "HAnimSegmentLineColorRGBA"

LineSet999.color = ColorRGBA1001

Shape998.geometry = LineSet999

HAnimSegment990.children.append(Shape998)
#HAnimSegment visualization line from current <HAnimJoint name='l_radiocarpal'/> to child <HAnimJoint name='l_middle0'/>
Shape1002 = x3d.Shape()
LineSet1003 = x3d.LineSet()
LineSet1003.vertexCount = [2]
Coordinate1004 = x3d.Coordinate()
Coordinate1004.point = (0.1984,0.8663,-0.0583,0.1987,0.8029,-0.0530)

LineSet1003.coord = Coordinate1004
ColorRGBA1005 = x3d.ColorRGBA()
ColorRGBA1005.USE = "HAnimSegmentLineColorRGBA"

LineSet1003.color = ColorRGBA1005

Shape1002.geometry = LineSet1003

HAnimSegment990.children.append(Shape1002)
#HAnimSegment visualization line from current <HAnimJoint name='l_radiocarpal'/> to child <HAnimJoint name='l_ring0'/>
Shape1006 = x3d.Shape()
LineSet1007 = x3d.LineSet()
LineSet1007.vertexCount = [2]
Coordinate1008 = x3d.Coordinate()
Coordinate1008.point = (0.1984,0.8663,-0.0583,0.1956,0.8019,-0.0794)

LineSet1007.coord = Coordinate1008
ColorRGBA1009 = x3d.ColorRGBA()
ColorRGBA1009.USE = "HAnimSegmentLineColorRGBA"

LineSet1007.color = ColorRGBA1009

Shape1006.geometry = LineSet1007

HAnimSegment990.children.append(Shape1006)
#HAnimSegment visualization line from current <HAnimJoint name='l_radiocarpal'/> to child <HAnimJoint name='l_pinky0'/>
Shape1010 = x3d.Shape()
LineSet1011 = x3d.LineSet()
LineSet1011.vertexCount = [2]
Coordinate1012 = x3d.Coordinate()
Coordinate1012.point = (0.1984,0.8663,-0.0583,0.1925,0.8066,-0.1036)

LineSet1011.coord = Coordinate1012
ColorRGBA1013 = x3d.ColorRGBA()
ColorRGBA1013.USE = "HAnimSegmentLineColorRGBA"

LineSet1011.color = ColorRGBA1013

Shape1010.geometry = LineSet1011

HAnimSegment990.children.append(Shape1010)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_radiocarpal'/> to <HAnimSite name='l_metacarpal_pha2_pt'/>
Shape1014 = x3d.Shape()
LineSet1015 = x3d.LineSet()
LineSet1015.vertexCount = [2]
Coordinate1016 = x3d.Coordinate()
Coordinate1016.point = (0.1984,0.8663,-0.0583,0.2009,0.8139,-0.0237)

LineSet1015.coord = Coordinate1016
ColorRGBA1017 = x3d.ColorRGBA()
ColorRGBA1017.USE = "HAnimSiteLineColorRGBA"

LineSet1015.color = ColorRGBA1017

Shape1014.geometry = LineSet1015

HAnimSegment990.children.append(Shape1014)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_radiocarpal'/> to <HAnimSite name='l_ulnar_styloid_pt'/>
Shape1018 = x3d.Shape()
LineSet1019 = x3d.LineSet()
LineSet1019.vertexCount = [2]
Coordinate1020 = x3d.Coordinate()
Coordinate1020.point = (0.1984,0.8663,-0.0583,0.2142,0.8529,-0.0648)

LineSet1019.coord = Coordinate1020
ColorRGBA1021 = x3d.ColorRGBA()
ColorRGBA1021.USE = "HAnimSiteLineColorRGBA"

LineSet1019.color = ColorRGBA1021

Shape1018.geometry = LineSet1019

HAnimSegment990.children.append(Shape1018)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_radiocarpal'/> to <HAnimSite name='l_metacarpal_pha5_pt'/>
Shape1022 = x3d.Shape()
LineSet1023 = x3d.LineSet()
LineSet1023.vertexCount = [2]
Coordinate1024 = x3d.Coordinate()
Coordinate1024.point = (0.1984,0.8663,-0.0583,0.1929,0.7860,-0.1122)

LineSet1023.coord = Coordinate1024
ColorRGBA1025 = x3d.ColorRGBA()
ColorRGBA1025.USE = "HAnimSiteLineColorRGBA"

LineSet1023.color = ColorRGBA1025

Shape1022.geometry = LineSet1023

HAnimSegment990.children.append(Shape1022)
#HAnimSite/Viewpoint visualization line segment from ancestor <HAnimJoint name='l_radiocarpal'/> to <HAnimSite name='l_hand_front_view'/>
Shape1026 = x3d.Shape()
LineSet1027 = x3d.LineSet()
LineSet1027.vertexCount = [2]
Coordinate1028 = x3d.Coordinate()
Coordinate1028.point = (0.1984,0.8663,-0.0583,0.3000,0.7500,0.4500)

LineSet1027.coord = Coordinate1028
ColorRGBA1029 = x3d.ColorRGBA()
ColorRGBA1029.USE = "HAnimSiteViewpointLineColorRGBA"

LineSet1027.color = ColorRGBA1029

Shape1026.geometry = LineSet1027

HAnimSegment990.children.append(Shape1026)
HAnimSite1030 = x3d.HAnimSite()
HAnimSite1030.name = "l_metacarpal_phalanx_2_pt"
HAnimSite1030.DEF = "hanim_l_metacarpal_phalanx_2_pt"
HAnimSite1030.translation = [0.2009,0.8139,-0.0237]
#HAnimSite visualization shape
TouchSensor1031 = x3d.TouchSensor()
TouchSensor1031.description = "HAnimSite l_metacarpal_pha2_pt"

HAnimSite1030.children.append(TouchSensor1031)
Shape1032 = x3d.Shape()
Shape1032.USE = "HAnimSiteShape"

HAnimSite1030.children.append(Shape1032)

HAnimSegment990.children.append(HAnimSite1030)
HAnimSite1033 = x3d.HAnimSite()
HAnimSite1033.name = "l_ulnar_styloid_pt"
HAnimSite1033.DEF = "hanim_l_ulnar_styloid_pt"
HAnimSite1033.translation = [0.2142,0.8529,-0.0648]
#HAnimSite visualization shape
TouchSensor1034 = x3d.TouchSensor()
TouchSensor1034.description = "HAnimSite l_ulnar_styloid_pt"

HAnimSite1033.children.append(TouchSensor1034)
Shape1035 = x3d.Shape()
Shape1035.USE = "HAnimSiteShape"

HAnimSite1033.children.append(Shape1035)

HAnimSegment990.children.append(HAnimSite1033)
HAnimSite1036 = x3d.HAnimSite()
HAnimSite1036.name = "l_metacarpal_phalanx_5_pt"
HAnimSite1036.DEF = "hanim_l_metacarpal_phalanx_5_pt"
HAnimSite1036.translation = [0.1929,0.786,-0.1122]
#HAnimSite visualization shape
TouchSensor1037 = x3d.TouchSensor()
TouchSensor1037.description = "HAnimSite l_metacarpal_pha5_pt"

HAnimSite1036.children.append(TouchSensor1037)
Shape1038 = x3d.Shape()
Shape1038.USE = "HAnimSiteShape"

HAnimSite1036.children.append(Shape1038)

HAnimSegment990.children.append(HAnimSite1036)
HAnimSite1039 = x3d.HAnimSite()
HAnimSite1039.name = "l_hand_front_view"
HAnimSite1039.DEF = "hanim_l_hand_front_view"
HAnimSite1039.translation = [0.3,0.75,0.45]
#HAnimSite visualization shape
TouchSensor1040 = x3d.TouchSensor()
TouchSensor1040.description = "HAnimSite l_hand_front_view"

HAnimSite1039.children.append(TouchSensor1040)
Shape1041 = x3d.Shape()
Shape1041.USE = "HAnimSiteShape"

HAnimSite1039.children.append(Shape1041)
Viewpoint1042 = x3d.Viewpoint()
Viewpoint1042.DEF = "hanim_l_hand_front_viewpoint"
Viewpoint1042.centerOfRotation = [0,0.7,0]
Viewpoint1042.description = "left hand front"
Viewpoint1042.position = [0,0,0]

HAnimSite1039.children.append(Viewpoint1042)
#HAnimSite/Viewpoint visualization shape
Anchor1043 = x3d.Anchor()
Anchor1043.description = "HAnimSite hanim_l_hand_front_view Viewpoint"
Anchor1043.url = ["#hanim_l_hand_front_viewpoint"]
LOD1044 = x3d.LOD()
LOD1044.forceTransitions = True
LOD1044.range = [0.04]
WorldInfo1045 = x3d.WorldInfo()
WorldInfo1045.info = ["hide diamond when close"]

LOD1044.children.append(WorldInfo1045)
Shape1046 = x3d.Shape()
Shape1046.USE = "HAnimSiteViewpointShape"

LOD1044.children.append(Shape1046)

Anchor1043.children.append(LOD1044)

HAnimSite1039.children.append(Anchor1043)

HAnimSegment990.children.append(HAnimSite1039)

HAnimJoint989.children.append(HAnimSegment990)
HAnimJoint1047 = x3d.HAnimJoint()
HAnimJoint1047.name = "l_carpometacarpal_1"
HAnimJoint1047.DEF = "hanim_l_carpometacarpal_1"
HAnimJoint1047.center = [0.1924,0.8472,-0.0534]
HAnimJoint1047.ulimit = [0,0,0]
HAnimJoint1047.llimit = [0,0,0]
HAnimSegment1048 = x3d.HAnimSegment()
HAnimSegment1048.name = "l_metacarpal_1"
HAnimSegment1048.DEF = "hanim_l_metacarpal_1"
#Visualization sphere for <HAnimJoint name='l_thumb1'/> is placed within <HAnimSegment name='l_metacarpal_1'/>
TouchSensor1049 = x3d.TouchSensor()
TouchSensor1049.description = "HAnimJoint l_thumb1, HAnimSegment l_metacarpal_1"

HAnimSegment1048.children.append(TouchSensor1049)
Transform1050 = x3d.Transform()
Transform1050.translation = [0.1924,0.8472,-0.0534]
Shape1051 = x3d.Shape()
Shape1051.USE = "HAnimJointShape"

Transform1050.children.append(Shape1051)

HAnimSegment1048.children.append(Transform1050)
#HAnimSegment visualization line from current <HAnimJoint name='l_thumb1'/> to child <HAnimJoint name='l_thumb2'/>
Shape1052 = x3d.Shape()
LineSet1053 = x3d.LineSet()
LineSet1053.vertexCount = [2]
Coordinate1054 = x3d.Coordinate()
Coordinate1054.point = (0.1924,0.8472,-0.0534,0.1951,0.8226,0.0246)

LineSet1053.coord = Coordinate1054
ColorRGBA1055 = x3d.ColorRGBA()
ColorRGBA1055.USE = "HAnimSegmentLineColorRGBA"

LineSet1053.color = ColorRGBA1055

Shape1052.geometry = LineSet1053

HAnimSegment1048.children.append(Shape1052)

HAnimJoint1047.children.append(HAnimSegment1048)
HAnimJoint1056 = x3d.HAnimJoint()
HAnimJoint1056.name = "l_metacarpophalangeal_1"
HAnimJoint1056.DEF = "hanim_l_metacarpophalangeal_1"
HAnimJoint1056.center = [0.1951,0.8226,0.0246]
HAnimJoint1056.ulimit = [0,0,0]
HAnimJoint1056.llimit = [0,0,0]
HAnimSegment1057 = x3d.HAnimSegment()
HAnimSegment1057.name = "l_carpal_proximal_phalanx_1"
HAnimSegment1057.DEF = "hanim_l_carpal_proximal_phalanx_1"
#Visualization sphere for <HAnimJoint name='l_thumb2'/> is placed within <HAnimSegment name='l_carpal_proximal_phalanx_1'/>
TouchSensor1058 = x3d.TouchSensor()
TouchSensor1058.description = "HAnimJoint l_thumb2, HAnimSegment l_carpal_proximal_phalanx_1"

HAnimSegment1057.children.append(TouchSensor1058)
Transform1059 = x3d.Transform()
Transform1059.translation = [0.1951,0.8226,0.0246]
Shape1060 = x3d.Shape()
Shape1060.USE = "HAnimJointShape"

Transform1059.children.append(Shape1060)

HAnimSegment1057.children.append(Transform1059)
#HAnimSegment visualization line from current <HAnimJoint name='l_thumb2'/> to child <HAnimJoint name='l_thumb3'/>
Shape1061 = x3d.Shape()
LineSet1062 = x3d.LineSet()
LineSet1062.vertexCount = [2]
Coordinate1063 = x3d.Coordinate()
Coordinate1063.point = (0.1951,0.8226,0.0246,0.1955,0.8159,0.0464)

LineSet1062.coord = Coordinate1063
ColorRGBA1064 = x3d.ColorRGBA()
ColorRGBA1064.USE = "HAnimSegmentLineColorRGBA"

LineSet1062.color = ColorRGBA1064

Shape1061.geometry = LineSet1062

HAnimSegment1057.children.append(Shape1061)

HAnimJoint1056.children.append(HAnimSegment1057)
HAnimJoint1065 = x3d.HAnimJoint()
HAnimJoint1065.name = "l_carpal_interphalangeal_1"
HAnimJoint1065.DEF = "hanim_l_carpal_interphalangeal_1"
HAnimJoint1065.center = [0.1955,0.8159,0.0464]
HAnimJoint1065.ulimit = [0,0,0]
HAnimJoint1065.llimit = [0,0,0]
HAnimSegment1066 = x3d.HAnimSegment()
HAnimSegment1066.name = "l_carpal_distal_phalanx_1"
HAnimSegment1066.DEF = "hanim_l_carpal_distal_phalanx_1"
#Visualization sphere for <HAnimJoint name='l_thumb3'/> is placed within <HAnimSegment name='l_carpal_distal_phalanx_1'/>
TouchSensor1067 = x3d.TouchSensor()
TouchSensor1067.description = "HAnimJoint l_thumb3, HAnimSegment l_carpal_distal_phalanx_1"

HAnimSegment1066.children.append(TouchSensor1067)
Transform1068 = x3d.Transform()
Transform1068.translation = [0.1955,0.8159,0.0464]
Shape1069 = x3d.Shape()
Shape1069.USE = "HAnimJointShape"

Transform1068.children.append(Shape1069)

HAnimSegment1066.children.append(Transform1068)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_thumb3'/> to <HAnimSite name='l_thumb_distal_tip'/>
Shape1070 = x3d.Shape()
LineSet1071 = x3d.LineSet()
LineSet1071.vertexCount = [2]
Coordinate1072 = x3d.Coordinate()
Coordinate1072.point = (0.1955,0.8159,0.0464,0.1982,0.8061,0.0759)

LineSet1071.coord = Coordinate1072
ColorRGBA1073 = x3d.ColorRGBA()
ColorRGBA1073.USE = "HAnimSiteLineColorRGBA"

LineSet1071.color = ColorRGBA1073

Shape1070.geometry = LineSet1071

HAnimSegment1066.children.append(Shape1070)
HAnimSite1074 = x3d.HAnimSite()
HAnimSite1074.name = "l_carpal_distal_phalanx_1_pt"
HAnimSite1074.DEF = "hanim_l_carpal_distal_phalanx_1_pt"
HAnimSite1074.translation = [0.1982,0.8061,0.0759]
#HAnimSite visualization shape
TouchSensor1075 = x3d.TouchSensor()
TouchSensor1075.description = "HAnimSite l_thumb_distal_tip"

HAnimSite1074.children.append(TouchSensor1075)
Shape1076 = x3d.Shape()
Shape1076.USE = "HAnimSiteShape"

HAnimSite1074.children.append(Shape1076)

HAnimSegment1066.children.append(HAnimSite1074)

HAnimJoint1065.children.append(HAnimSegment1066)

HAnimJoint1056.children.append(HAnimJoint1065)

HAnimJoint1047.children.append(HAnimJoint1056)

HAnimJoint989.children.append(HAnimJoint1047)
HAnimJoint1077 = x3d.HAnimJoint()
HAnimJoint1077.name = "l_carpometacarpal_2"
HAnimJoint1077.DEF = "hanim_l_carpometacarpal_2"
HAnimJoint1077.center = [0.1983,0.8024,-0.028]
HAnimJoint1077.ulimit = [0,0,0]
HAnimJoint1077.llimit = [0,0,0]
HAnimSegment1078 = x3d.HAnimSegment()
HAnimSegment1078.name = "l_metacarpal_2"
HAnimSegment1078.DEF = "hanim_l_metacarpal_2"
#Visualization sphere for <HAnimJoint name='l_index0'/> is placed within <HAnimSegment name='l_metacarpal_2'/>
TouchSensor1079 = x3d.TouchSensor()
TouchSensor1079.description = "HAnimJoint l_index0, HAnimSegment l_metacarpal_2"

HAnimSegment1078.children.append(TouchSensor1079)
Transform1080 = x3d.Transform()
Transform1080.translation = [0.1983,0.8024,-0.028]
Shape1081 = x3d.Shape()
Shape1081.USE = "HAnimJointShape"

Transform1080.children.append(Shape1081)

HAnimSegment1078.children.append(Transform1080)
#HAnimSegment visualization line from current <HAnimJoint name='l_index0'/> to child <HAnimJoint name='l_index1'/>
Shape1082 = x3d.Shape()
LineSet1083 = x3d.LineSet()
LineSet1083.vertexCount = [2]
Coordinate1084 = x3d.Coordinate()
Coordinate1084.point = (0.1983,0.8024,-0.0280,0.1983,0.7815,-0.0280)

LineSet1083.coord = Coordinate1084
ColorRGBA1085 = x3d.ColorRGBA()
ColorRGBA1085.USE = "HAnimSegmentLineColorRGBA"

LineSet1083.color = ColorRGBA1085

Shape1082.geometry = LineSet1083

HAnimSegment1078.children.append(Shape1082)

HAnimJoint1077.children.append(HAnimSegment1078)
HAnimJoint1086 = x3d.HAnimJoint()
HAnimJoint1086.name = "l_metacarpophalangeal_2"
HAnimJoint1086.DEF = "hanim_l_metacarpophalangeal_2"
HAnimJoint1086.center = [0.1983,0.7815,-0.028]
HAnimJoint1086.ulimit = [0,0,0]
HAnimJoint1086.llimit = [0,0,0]
HAnimSegment1087 = x3d.HAnimSegment()
HAnimSegment1087.name = "l_carpal_proximal_phalanx_2"
HAnimSegment1087.DEF = "hanim_l_carpal_proximal_phalanx_2"
#Visualization sphere for <HAnimJoint name='l_index1'/> is placed within <HAnimSegment name='l_carpal_proximal_phalanx_2'/>
TouchSensor1088 = x3d.TouchSensor()
TouchSensor1088.description = "HAnimJoint l_index1, HAnimSegment l_carpal_proximal_phalanx_2"

HAnimSegment1087.children.append(TouchSensor1088)
Transform1089 = x3d.Transform()
Transform1089.translation = [0.1983,0.7815,-0.028]
Shape1090 = x3d.Shape()
Shape1090.USE = "HAnimJointShape"

Transform1089.children.append(Shape1090)

HAnimSegment1087.children.append(Transform1089)
#HAnimSegment visualization line from current <HAnimJoint name='l_index1'/> to child <HAnimJoint name='l_index2'/>
Shape1091 = x3d.Shape()
LineSet1092 = x3d.LineSet()
LineSet1092.vertexCount = [2]
Coordinate1093 = x3d.Coordinate()
Coordinate1093.point = (0.1983,0.7815,-0.0280,0.2017,0.7363,-0.0248)

LineSet1092.coord = Coordinate1093
ColorRGBA1094 = x3d.ColorRGBA()
ColorRGBA1094.USE = "HAnimSegmentLineColorRGBA"

LineSet1092.color = ColorRGBA1094

Shape1091.geometry = LineSet1092

HAnimSegment1087.children.append(Shape1091)

HAnimJoint1086.children.append(HAnimSegment1087)
HAnimJoint1095 = x3d.HAnimJoint()
HAnimJoint1095.name = "l_carpal_proximal_interphalangeal_2"
HAnimJoint1095.DEF = "hanim_l_carpal_proximal_interphalangeal_2"
HAnimJoint1095.center = [0.2017,0.7363,-0.0248]
HAnimJoint1095.ulimit = [0,0,0]
HAnimJoint1095.llimit = [0,0,0]
HAnimSegment1096 = x3d.HAnimSegment()
HAnimSegment1096.name = "l_carpal_middle_phalanx_2"
HAnimSegment1096.DEF = "hanim_l_carpal_middle_phalanx_2"
#Visualization sphere for <HAnimJoint name='l_index2'/> is placed within <HAnimSegment name='l_carpal_middle_phalanx_2'/>
TouchSensor1097 = x3d.TouchSensor()
TouchSensor1097.description = "HAnimJoint l_index2, HAnimSegment l_carpal_middle_phalanx_2"

HAnimSegment1096.children.append(TouchSensor1097)
Transform1098 = x3d.Transform()
Transform1098.translation = [0.2017,0.7363,-0.0248]
Shape1099 = x3d.Shape()
Shape1099.USE = "HAnimJointShape"

Transform1098.children.append(Shape1099)

HAnimSegment1096.children.append(Transform1098)
#HAnimSegment visualization line from current <HAnimJoint name='l_index2'/> to child <HAnimJoint name='l_index3'/>
Shape1100 = x3d.Shape()
LineSet1101 = x3d.LineSet()
LineSet1101.vertexCount = [2]
Coordinate1102 = x3d.Coordinate()
Coordinate1102.point = (0.2017,0.7363,-0.0248,0.2028,0.7139,-0.0236)

LineSet1101.coord = Coordinate1102
ColorRGBA1103 = x3d.ColorRGBA()
ColorRGBA1103.USE = "HAnimSegmentLineColorRGBA"

LineSet1101.color = ColorRGBA1103

Shape1100.geometry = LineSet1101

HAnimSegment1096.children.append(Shape1100)

HAnimJoint1095.children.append(HAnimSegment1096)
HAnimJoint1104 = x3d.HAnimJoint()
HAnimJoint1104.name = "l_carpal_distal_interphalangeal_2"
HAnimJoint1104.DEF = "hanim_l_carpal_distal_interphalangeal_2"
HAnimJoint1104.center = [0.2028,0.7139,-0.0236]
HAnimJoint1104.ulimit = [0,0,0]
HAnimJoint1104.llimit = [0,0,0]
HAnimSegment1105 = x3d.HAnimSegment()
HAnimSegment1105.name = "l_carpal_distal_phalanx_2"
HAnimSegment1105.DEF = "hanim_l_carpal_distal_phalanx_2"
#Visualization sphere for <HAnimJoint name='l_index3'/> is placed within <HAnimSegment name='l_carpal_distal_phalanx_2'/>
TouchSensor1106 = x3d.TouchSensor()
TouchSensor1106.description = "HAnimJoint l_index3, HAnimSegment l_carpal_distal_phalanx_2"

HAnimSegment1105.children.append(TouchSensor1106)
Transform1107 = x3d.Transform()
Transform1107.translation = [0.2028,0.7139,-0.0236]
Shape1108 = x3d.Shape()
Shape1108.USE = "HAnimJointShape"

Transform1107.children.append(Shape1108)

HAnimSegment1105.children.append(Transform1107)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_index3'/> to <HAnimSite name='l_index_distal_tip'/>
Shape1109 = x3d.Shape()
LineSet1110 = x3d.LineSet()
LineSet1110.vertexCount = [2]
Coordinate1111 = x3d.Coordinate()
Coordinate1111.point = (0.2028,0.7139,-0.0236,0.2089,0.6858,-0.0245)

LineSet1110.coord = Coordinate1111
ColorRGBA1112 = x3d.ColorRGBA()
ColorRGBA1112.USE = "HAnimSiteLineColorRGBA"

LineSet1110.color = ColorRGBA1112

Shape1109.geometry = LineSet1110

HAnimSegment1105.children.append(Shape1109)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_index3'/> to <HAnimSite name='l_dactylion_pt'/>
Shape1113 = x3d.Shape()
LineSet1114 = x3d.LineSet()
LineSet1114.vertexCount = [2]
Coordinate1115 = x3d.Coordinate()
Coordinate1115.point = (0.2028,0.7139,-0.0236,0.2056,0.6743,-0.0482)

LineSet1114.coord = Coordinate1115
ColorRGBA1116 = x3d.ColorRGBA()
ColorRGBA1116.USE = "HAnimSiteLineColorRGBA"

LineSet1114.color = ColorRGBA1116

Shape1113.geometry = LineSet1114

HAnimSegment1105.children.append(Shape1113)
HAnimSite1117 = x3d.HAnimSite()
HAnimSite1117.name = "l_carpal_distal_phalanx_2_pt"
HAnimSite1117.DEF = "hanim_l_carpal_distal_phalanx_2_pt"
HAnimSite1117.translation = [0.2089,0.6858,-0.0245]
#HAnimSite visualization shape
TouchSensor1118 = x3d.TouchSensor()
TouchSensor1118.description = "HAnimSite l_index_distal_tip"

HAnimSite1117.children.append(TouchSensor1118)
Shape1119 = x3d.Shape()
Shape1119.USE = "HAnimSiteShape"

HAnimSite1117.children.append(Shape1119)

HAnimSegment1105.children.append(HAnimSite1117)
HAnimSite1120 = x3d.HAnimSite()
HAnimSite1120.name = "l_dactylion_pt"
HAnimSite1120.DEF = "hanim_l_dactylion_pt"
HAnimSite1120.translation = [0.2056,0.6743,-0.0482]
#HAnimSite visualization shape
TouchSensor1121 = x3d.TouchSensor()
TouchSensor1121.description = "HAnimSite l_dactylion_pt"

HAnimSite1120.children.append(TouchSensor1121)
Shape1122 = x3d.Shape()
Shape1122.USE = "HAnimSiteShape"

HAnimSite1120.children.append(Shape1122)

HAnimSegment1105.children.append(HAnimSite1120)

HAnimJoint1104.children.append(HAnimSegment1105)

HAnimJoint1095.children.append(HAnimJoint1104)

HAnimJoint1086.children.append(HAnimJoint1095)

HAnimJoint1077.children.append(HAnimJoint1086)

HAnimJoint989.children.append(HAnimJoint1077)
HAnimJoint1123 = x3d.HAnimJoint()
HAnimJoint1123.name = "l_carpometacarpal_3"
HAnimJoint1123.DEF = "hanim_l_carpometacarpal_3"
HAnimJoint1123.center = [0.1987,0.8029,-0.053]
HAnimJoint1123.ulimit = [0,0,0]
HAnimJoint1123.llimit = [0,0,0]
HAnimSegment1124 = x3d.HAnimSegment()
HAnimSegment1124.name = "l_metacarpal_3"
HAnimSegment1124.DEF = "hanim_l_metacarpal_3"
#Visualization sphere for <HAnimJoint name='l_middle0'/> is placed within <HAnimSegment name='l_metacarpal_3'/>
TouchSensor1125 = x3d.TouchSensor()
TouchSensor1125.description = "HAnimJoint l_middle0, HAnimSegment l_metacarpal_3"

HAnimSegment1124.children.append(TouchSensor1125)
Transform1126 = x3d.Transform()
Transform1126.translation = [0.1987,0.8029,-0.053]
Shape1127 = x3d.Shape()
Shape1127.USE = "HAnimJointShape"

Transform1126.children.append(Shape1127)

HAnimSegment1124.children.append(Transform1126)
#HAnimSegment visualization line from current <HAnimJoint name='l_middle0'/> to child <HAnimJoint name='l_middle1'/>
Shape1128 = x3d.Shape()
LineSet1129 = x3d.LineSet()
LineSet1129.vertexCount = [2]
Coordinate1130 = x3d.Coordinate()
Coordinate1130.point = (0.1987,0.8029,-0.0530,0.1987,0.7818,-0.0530)

LineSet1129.coord = Coordinate1130
ColorRGBA1131 = x3d.ColorRGBA()
ColorRGBA1131.USE = "HAnimSegmentLineColorRGBA"

LineSet1129.color = ColorRGBA1131

Shape1128.geometry = LineSet1129

HAnimSegment1124.children.append(Shape1128)

HAnimJoint1123.children.append(HAnimSegment1124)
HAnimJoint1132 = x3d.HAnimJoint()
HAnimJoint1132.name = "l_metacarpophalangeal_3"
HAnimJoint1132.DEF = "hanim_l_metacarpophalangeal_3"
HAnimJoint1132.center = [0.1987,0.7818,-0.053]
HAnimJoint1132.ulimit = [0,0,0]
HAnimJoint1132.llimit = [0,0,0]
HAnimSegment1133 = x3d.HAnimSegment()
HAnimSegment1133.name = "l_carpal_proximal_phalanx_3"
HAnimSegment1133.DEF = "hanim_l_carpal_proximal_phalanx_3"
#Visualization sphere for <HAnimJoint name='l_middle1'/> is placed within <HAnimSegment name='l_carpal_proximal_phalanx_3'/>
TouchSensor1134 = x3d.TouchSensor()
TouchSensor1134.description = "HAnimJoint l_middle1, HAnimSegment l_carpal_proximal_phalanx_3"

HAnimSegment1133.children.append(TouchSensor1134)
Transform1135 = x3d.Transform()
Transform1135.translation = [0.1987,0.7818,-0.053]
Shape1136 = x3d.Shape()
Shape1136.USE = "HAnimJointShape"

Transform1135.children.append(Shape1136)

HAnimSegment1133.children.append(Transform1135)
#HAnimSegment visualization line from current <HAnimJoint name='l_middle1'/> to child <HAnimJoint name='l_middle2'/>
Shape1137 = x3d.Shape()
LineSet1138 = x3d.LineSet()
LineSet1138.vertexCount = [2]
Coordinate1139 = x3d.Coordinate()
Coordinate1139.point = (0.1987,0.7818,-0.0530,0.2013,0.7273,-0.0503)

LineSet1138.coord = Coordinate1139
ColorRGBA1140 = x3d.ColorRGBA()
ColorRGBA1140.USE = "HAnimSegmentLineColorRGBA"

LineSet1138.color = ColorRGBA1140

Shape1137.geometry = LineSet1138

HAnimSegment1133.children.append(Shape1137)

HAnimJoint1132.children.append(HAnimSegment1133)
HAnimJoint1141 = x3d.HAnimJoint()
HAnimJoint1141.name = "l_carpal_proximal_interphalangeal_3"
HAnimJoint1141.DEF = "hanim_l_carpal_proximal_interphalangeal_3"
HAnimJoint1141.center = [0.2013,0.7273,-0.0503]
HAnimJoint1141.ulimit = [0,0,0]
HAnimJoint1141.llimit = [0,0,0]
HAnimSegment1142 = x3d.HAnimSegment()
HAnimSegment1142.name = "l_carpal_middle_phalanx_3"
HAnimSegment1142.DEF = "hanim_l_carpal_middle_phalanx_3"
#Visualization sphere for <HAnimJoint name='l_middle2'/> is placed within <HAnimSegment name='l_carpal_middle_phalanx_3'/>
TouchSensor1143 = x3d.TouchSensor()
TouchSensor1143.description = "HAnimJoint l_middle2, HAnimSegment l_carpal_middle_phalanx_3"

HAnimSegment1142.children.append(TouchSensor1143)
Transform1144 = x3d.Transform()
Transform1144.translation = [0.2013,0.7273,-0.0503]
Shape1145 = x3d.Shape()
Shape1145.USE = "HAnimJointShape"

Transform1144.children.append(Shape1145)

HAnimSegment1142.children.append(Transform1144)
#HAnimSegment visualization line from current <HAnimJoint name='l_middle2'/> to child <HAnimJoint name='l_middle3'/>
Shape1146 = x3d.Shape()
LineSet1147 = x3d.LineSet()
LineSet1147.vertexCount = [2]
Coordinate1148 = x3d.Coordinate()
Coordinate1148.point = (0.2013,0.7273,-0.0503,0.2026,0.7011,-0.0494)

LineSet1147.coord = Coordinate1148
ColorRGBA1149 = x3d.ColorRGBA()
ColorRGBA1149.USE = "HAnimSegmentLineColorRGBA"

LineSet1147.color = ColorRGBA1149

Shape1146.geometry = LineSet1147

HAnimSegment1142.children.append(Shape1146)

HAnimJoint1141.children.append(HAnimSegment1142)
HAnimJoint1150 = x3d.HAnimJoint()
HAnimJoint1150.name = "l_carpal_distal_interphalangeal_3"
HAnimJoint1150.DEF = "hanim_l_carpal_distal_interphalangeal_3"
HAnimJoint1150.center = [0.2026,0.7011,-0.0494]
HAnimJoint1150.ulimit = [0,0,0]
HAnimJoint1150.llimit = [0,0,0]
HAnimSegment1151 = x3d.HAnimSegment()
HAnimSegment1151.name = "l_carpal_distal_phalanx_3"
HAnimSegment1151.DEF = "hanim_l_carpal_distal_phalanx_3"
#Visualization sphere for <HAnimJoint name='l_middle3'/> is placed within <HAnimSegment name='l_carpal_distal_phalanx_3'/>
TouchSensor1152 = x3d.TouchSensor()
TouchSensor1152.description = "HAnimJoint l_middle3, HAnimSegment l_carpal_distal_phalanx_3"

HAnimSegment1151.children.append(TouchSensor1152)
Transform1153 = x3d.Transform()
Transform1153.translation = [0.2026,0.7011,-0.0494]
Shape1154 = x3d.Shape()
Shape1154.USE = "HAnimJointShape"

Transform1153.children.append(Shape1154)

HAnimSegment1151.children.append(Transform1153)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_middle3'/> to <HAnimSite name='l_middle_distal_tip'/>
Shape1155 = x3d.Shape()
LineSet1156 = x3d.LineSet()
LineSet1156.vertexCount = [2]
Coordinate1157 = x3d.Coordinate()
Coordinate1157.point = (0.2026,0.7011,-0.0494,0.2080,0.6731,-0.0491)

LineSet1156.coord = Coordinate1157
ColorRGBA1158 = x3d.ColorRGBA()
ColorRGBA1158.USE = "HAnimSiteLineColorRGBA"

LineSet1156.color = ColorRGBA1158

Shape1155.geometry = LineSet1156

HAnimSegment1151.children.append(Shape1155)
HAnimSite1159 = x3d.HAnimSite()
HAnimSite1159.name = "l_carpal_distal_phalanx_3_pt"
HAnimSite1159.DEF = "hanim_l_carpal_distal_phalanx_3_pt"
HAnimSite1159.translation = [0.208,0.6731,-0.0491]
#HAnimSite visualization shape
TouchSensor1160 = x3d.TouchSensor()
TouchSensor1160.description = "HAnimSite l_middle_distal_tip"

HAnimSite1159.children.append(TouchSensor1160)
Shape1161 = x3d.Shape()
Shape1161.USE = "HAnimSiteShape"

HAnimSite1159.children.append(Shape1161)

HAnimSegment1151.children.append(HAnimSite1159)

HAnimJoint1150.children.append(HAnimSegment1151)

HAnimJoint1141.children.append(HAnimJoint1150)

HAnimJoint1132.children.append(HAnimJoint1141)

HAnimJoint1123.children.append(HAnimJoint1132)

HAnimJoint989.children.append(HAnimJoint1123)
HAnimJoint1162 = x3d.HAnimJoint()
HAnimJoint1162.name = "l_carpometacarpal_4"
HAnimJoint1162.DEF = "hanim_l_carpometacarpal_4"
HAnimJoint1162.center = [0.1956,0.8019,-0.0794]
HAnimJoint1162.ulimit = [0,0,0]
HAnimJoint1162.llimit = [0,0,0]
HAnimSegment1163 = x3d.HAnimSegment()
HAnimSegment1163.name = "l_metacarpal_4"
HAnimSegment1163.DEF = "hanim_l_metacarpal_4"
#Visualization sphere for <HAnimJoint name='l_ring0'/> is placed within <HAnimSegment name='l_metacarpal_4'/>
TouchSensor1164 = x3d.TouchSensor()
TouchSensor1164.description = "HAnimJoint l_ring0, HAnimSegment l_metacarpal_4"

HAnimSegment1163.children.append(TouchSensor1164)
Transform1165 = x3d.Transform()
Transform1165.translation = [0.1956,0.8019,-0.0794]
Shape1166 = x3d.Shape()
Shape1166.USE = "HAnimJointShape"

Transform1165.children.append(Shape1166)

HAnimSegment1163.children.append(Transform1165)
#HAnimSegment visualization line from current <HAnimJoint name='l_ring0'/> to child <HAnimJoint name='l_ring1'/>
Shape1167 = x3d.Shape()
LineSet1168 = x3d.LineSet()
LineSet1168.vertexCount = [2]
Coordinate1169 = x3d.Coordinate()
Coordinate1169.point = (0.1956,0.8019,-0.0794,0.1956,0.7815,-0.0794)

LineSet1168.coord = Coordinate1169
ColorRGBA1170 = x3d.ColorRGBA()
ColorRGBA1170.USE = "HAnimSegmentLineColorRGBA"

LineSet1168.color = ColorRGBA1170

Shape1167.geometry = LineSet1168

HAnimSegment1163.children.append(Shape1167)

HAnimJoint1162.children.append(HAnimSegment1163)
HAnimJoint1171 = x3d.HAnimJoint()
HAnimJoint1171.name = "l_metacarpophalangeal_4"
HAnimJoint1171.DEF = "hanim_l_metacarpophalangeal_4"
HAnimJoint1171.center = [0.1956,0.7815,-0.0794]
HAnimJoint1171.ulimit = [0,0,0]
HAnimJoint1171.llimit = [0,0,0]
HAnimSegment1172 = x3d.HAnimSegment()
HAnimSegment1172.name = "l_carpal_proximal_phalanx_4"
HAnimSegment1172.DEF = "hanim_l_carpal_proximal_phalanx_4"
#Visualization sphere for <HAnimJoint name='l_ring1'/> is placed within <HAnimSegment name='l_carpal_proximal_phalanx_4'/>
TouchSensor1173 = x3d.TouchSensor()
TouchSensor1173.description = "HAnimJoint l_ring1, HAnimSegment l_carpal_proximal_phalanx_4"

HAnimSegment1172.children.append(TouchSensor1173)
Transform1174 = x3d.Transform()
Transform1174.translation = [0.1956,0.7815,-0.0794]
Shape1175 = x3d.Shape()
Shape1175.USE = "HAnimJointShape"

Transform1174.children.append(Shape1175)

HAnimSegment1172.children.append(Transform1174)
#HAnimSegment visualization line from current <HAnimJoint name='l_ring1'/> to child <HAnimJoint name='l_ring2'/>
Shape1176 = x3d.Shape()
LineSet1177 = x3d.LineSet()
LineSet1177.vertexCount = [2]
Coordinate1178 = x3d.Coordinate()
Coordinate1178.point = (0.1956,0.7815,-0.0794,0.1973,0.7287,-0.0777)

LineSet1177.coord = Coordinate1178
ColorRGBA1179 = x3d.ColorRGBA()
ColorRGBA1179.USE = "HAnimSegmentLineColorRGBA"

LineSet1177.color = ColorRGBA1179

Shape1176.geometry = LineSet1177

HAnimSegment1172.children.append(Shape1176)

HAnimJoint1171.children.append(HAnimSegment1172)
HAnimJoint1180 = x3d.HAnimJoint()
HAnimJoint1180.name = "l_carpal_proximal_interphalangeal_4"
HAnimJoint1180.DEF = "hanim_l_carpal_proximal_interphalangeal_4"
HAnimJoint1180.center = [0.1973,0.7287,-0.0777]
HAnimJoint1180.ulimit = [0,0,0]
HAnimJoint1180.llimit = [0,0,0]
HAnimSegment1181 = x3d.HAnimSegment()
HAnimSegment1181.name = "l_carpal_middle_phalanx_4"
HAnimSegment1181.DEF = "hanim_l_carpal_middle_phalanx_4"
#Visualization sphere for <HAnimJoint name='l_ring2'/> is placed within <HAnimSegment name='l_carpal_middle_phalanx_4'/>
TouchSensor1182 = x3d.TouchSensor()
TouchSensor1182.description = "HAnimJoint l_ring2, HAnimSegment l_carpal_middle_phalanx_4"

HAnimSegment1181.children.append(TouchSensor1182)
Transform1183 = x3d.Transform()
Transform1183.translation = [0.1973,0.7287,-0.0777]
Shape1184 = x3d.Shape()
Shape1184.USE = "HAnimJointShape"

Transform1183.children.append(Shape1184)

HAnimSegment1181.children.append(Transform1183)
#HAnimSegment visualization line from current <HAnimJoint name='l_ring2'/> to child <HAnimJoint name='l_ring3'/>
Shape1185 = x3d.Shape()
LineSet1186 = x3d.LineSet()
LineSet1186.vertexCount = [2]
Coordinate1187 = x3d.Coordinate()
Coordinate1187.point = (0.1973,0.7287,-0.0777,0.1983,0.7045,-0.0767)

LineSet1186.coord = Coordinate1187
ColorRGBA1188 = x3d.ColorRGBA()
ColorRGBA1188.USE = "HAnimSegmentLineColorRGBA"

LineSet1186.color = ColorRGBA1188

Shape1185.geometry = LineSet1186

HAnimSegment1181.children.append(Shape1185)

HAnimJoint1180.children.append(HAnimSegment1181)
HAnimJoint1189 = x3d.HAnimJoint()
HAnimJoint1189.name = "l_carpal_distal_interphalangeal_4"
HAnimJoint1189.DEF = "hanim_l_carpal_distal_interphalangeal_4"
HAnimJoint1189.center = [0.1983,0.7045,-0.0767]
HAnimJoint1189.ulimit = [0,0,0]
HAnimJoint1189.llimit = [0,0,0]
HAnimSegment1190 = x3d.HAnimSegment()
HAnimSegment1190.name = "l_carpal_distal_phalanx_4"
HAnimSegment1190.DEF = "hanim_l_carpal_distal_phalanx_4"
#Visualization sphere for <HAnimJoint name='l_ring3'/> is placed within <HAnimSegment name='l_carpal_distal_phalanx_4'/>
TouchSensor1191 = x3d.TouchSensor()
TouchSensor1191.description = "HAnimJoint l_ring3, HAnimSegment l_carpal_distal_phalanx_4"

HAnimSegment1190.children.append(TouchSensor1191)
Transform1192 = x3d.Transform()
Transform1192.translation = [0.1983,0.7045,-0.0767]
Shape1193 = x3d.Shape()
Shape1193.USE = "HAnimJointShape"

Transform1192.children.append(Shape1193)

HAnimSegment1190.children.append(Transform1192)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_ring3'/> to <HAnimSite name='l_ring_distal_tip'/>
Shape1194 = x3d.Shape()
LineSet1195 = x3d.LineSet()
LineSet1195.vertexCount = [2]
Coordinate1196 = x3d.Coordinate()
Coordinate1196.point = (0.1983,0.7045,-0.0767,0.2035,0.6750,-0.0756)

LineSet1195.coord = Coordinate1196
ColorRGBA1197 = x3d.ColorRGBA()
ColorRGBA1197.USE = "HAnimSiteLineColorRGBA"

LineSet1195.color = ColorRGBA1197

Shape1194.geometry = LineSet1195

HAnimSegment1190.children.append(Shape1194)
HAnimSite1198 = x3d.HAnimSite()
HAnimSite1198.name = "l_carpal_distal_phalanx_4_pt"
HAnimSite1198.DEF = "hanim_l_carpal_distal_phalanx_4_pt"
HAnimSite1198.translation = [0.2035,0.675,-0.0756]
#HAnimSite visualization shape
TouchSensor1199 = x3d.TouchSensor()
TouchSensor1199.description = "HAnimSite l_ring_distal_tip"

HAnimSite1198.children.append(TouchSensor1199)
Shape1200 = x3d.Shape()
Shape1200.USE = "HAnimSiteShape"

HAnimSite1198.children.append(Shape1200)

HAnimSegment1190.children.append(HAnimSite1198)

HAnimJoint1189.children.append(HAnimSegment1190)

HAnimJoint1180.children.append(HAnimJoint1189)

HAnimJoint1171.children.append(HAnimJoint1180)

HAnimJoint1162.children.append(HAnimJoint1171)

HAnimJoint989.children.append(HAnimJoint1162)
HAnimJoint1201 = x3d.HAnimJoint()
HAnimJoint1201.name = "l_carpometacarpal_5"
HAnimJoint1201.DEF = "hanim_l_carpometacarpal_5"
HAnimJoint1201.center = [0.1925,0.8066,-0.1036]
HAnimJoint1201.ulimit = [0,0,0]
HAnimJoint1201.llimit = [0,0,0]
HAnimSegment1202 = x3d.HAnimSegment()
HAnimSegment1202.name = "l_metacarpal_5"
HAnimSegment1202.DEF = "hanim_l_metacarpal_5"
#Visualization sphere for <HAnimJoint name='l_pinky0'/> is placed within <HAnimSegment name='l_metacarpal_5'/>
TouchSensor1203 = x3d.TouchSensor()
TouchSensor1203.description = "HAnimJoint l_pinky0, HAnimSegment l_metacarpal_5"

HAnimSegment1202.children.append(TouchSensor1203)
Transform1204 = x3d.Transform()
Transform1204.translation = [0.1925,0.8066,-0.1036]
Shape1205 = x3d.Shape()
Shape1205.USE = "HAnimJointShape"

Transform1204.children.append(Shape1205)

HAnimSegment1202.children.append(Transform1204)
#HAnimSegment visualization line from current <HAnimJoint name='l_pinky0'/> to child <HAnimJoint name='l_pinky1'/>
Shape1206 = x3d.Shape()
LineSet1207 = x3d.LineSet()
LineSet1207.vertexCount = [2]
Coordinate1208 = x3d.Coordinate()
Coordinate1208.point = (0.1925,0.8066,-0.1036,0.1925,0.7866,-0.1036)

LineSet1207.coord = Coordinate1208
ColorRGBA1209 = x3d.ColorRGBA()
ColorRGBA1209.USE = "HAnimSegmentLineColorRGBA"

LineSet1207.color = ColorRGBA1209

Shape1206.geometry = LineSet1207

HAnimSegment1202.children.append(Shape1206)

HAnimJoint1201.children.append(HAnimSegment1202)
HAnimJoint1210 = x3d.HAnimJoint()
HAnimJoint1210.name = "l_metacarpophalangeal_5"
HAnimJoint1210.DEF = "hanim_l_metacarpophalangeal_5"
HAnimJoint1210.center = [0.1925,0.7866,-0.1036]
HAnimJoint1210.ulimit = [0,0,0]
HAnimJoint1210.llimit = [0,0,0]
HAnimSegment1211 = x3d.HAnimSegment()
HAnimSegment1211.name = "l_carpal_proximal_phalanx_5"
HAnimSegment1211.DEF = "hanim_l_carpal_proximal_phalanx_5"
#Visualization sphere for <HAnimJoint name='l_pinky1'/> is placed within <HAnimSegment name='l_carpal_proximal_phalanx_5'/>
TouchSensor1212 = x3d.TouchSensor()
TouchSensor1212.description = "HAnimJoint l_pinky1, HAnimSegment l_carpal_proximal_phalanx_5"

HAnimSegment1211.children.append(TouchSensor1212)
Transform1213 = x3d.Transform()
Transform1213.translation = [0.1925,0.7866,-0.1036]
Shape1214 = x3d.Shape()
Shape1214.USE = "HAnimJointShape"

Transform1213.children.append(Shape1214)

HAnimSegment1211.children.append(Transform1213)
#HAnimSegment visualization line from current <HAnimJoint name='l_pinky1'/> to child <HAnimJoint name='l_pinky2'/>
Shape1215 = x3d.Shape()
LineSet1216 = x3d.LineSet()
LineSet1216.vertexCount = [2]
Coordinate1217 = x3d.Coordinate()
Coordinate1217.point = (0.1925,0.7866,-0.1036,0.1938,0.7452,-0.1024)

LineSet1216.coord = Coordinate1217
ColorRGBA1218 = x3d.ColorRGBA()
ColorRGBA1218.USE = "HAnimSegmentLineColorRGBA"

LineSet1216.color = ColorRGBA1218

Shape1215.geometry = LineSet1216

HAnimSegment1211.children.append(Shape1215)

HAnimJoint1210.children.append(HAnimSegment1211)
HAnimJoint1219 = x3d.HAnimJoint()
HAnimJoint1219.name = "l_carpal_proximal_interphalangeal_5"
HAnimJoint1219.DEF = "hanim_l_carpal_proximal_interphalangeal_5"
HAnimJoint1219.center = [0.1938,0.7452,-0.1024]
HAnimJoint1219.ulimit = [0,0,0]
HAnimJoint1219.llimit = [0,0,0]
HAnimSegment1220 = x3d.HAnimSegment()
HAnimSegment1220.name = "l_carpal_middle_phalanx_5"
HAnimSegment1220.DEF = "hanim_l_carpal_middle_phalanx_5"
#Visualization sphere for <HAnimJoint name='l_pinky2'/> is placed within <HAnimSegment name='l_carpal_middle_phalanx_5'/>
TouchSensor1221 = x3d.TouchSensor()
TouchSensor1221.description = "HAnimJoint l_pinky2, HAnimSegment l_carpal_middle_phalanx_5"

HAnimSegment1220.children.append(TouchSensor1221)
Transform1222 = x3d.Transform()
Transform1222.translation = [0.1938,0.7452,-0.1024]
Shape1223 = x3d.Shape()
Shape1223.USE = "HAnimJointShape"

Transform1222.children.append(Shape1223)

HAnimSegment1220.children.append(Transform1222)
#HAnimSegment visualization line from current <HAnimJoint name='l_pinky2'/> to child <HAnimJoint name='l_pinky3'/>
Shape1224 = x3d.Shape()
LineSet1225 = x3d.LineSet()
LineSet1225.vertexCount = [2]
Coordinate1226 = x3d.Coordinate()
Coordinate1226.point = (0.1938,0.7452,-0.1024,0.1948,0.7277,-0.1017)

LineSet1225.coord = Coordinate1226
ColorRGBA1227 = x3d.ColorRGBA()
ColorRGBA1227.USE = "HAnimSegmentLineColorRGBA"

LineSet1225.color = ColorRGBA1227

Shape1224.geometry = LineSet1225

HAnimSegment1220.children.append(Shape1224)

HAnimJoint1219.children.append(HAnimSegment1220)
HAnimJoint1228 = x3d.HAnimJoint()
HAnimJoint1228.name = "l_carpal_distal_interphalangeal_5"
HAnimJoint1228.DEF = "hanim_l_carpal_distal_interphalangeal_5"
HAnimJoint1228.center = [0.1948,0.7277,-0.1017]
HAnimJoint1228.ulimit = [0,0,0]
HAnimJoint1228.llimit = [0,0,0]
HAnimSegment1229 = x3d.HAnimSegment()
HAnimSegment1229.name = "l_carpal_distal_phalanx_5"
HAnimSegment1229.DEF = "hanim_l_carpal_distal_phalanx_5"
#Visualization sphere for <HAnimJoint name='l_pinky3'/> is placed within <HAnimSegment name='l_carpal_distal_phalanx_5'/>
TouchSensor1230 = x3d.TouchSensor()
TouchSensor1230.description = "HAnimJoint l_pinky3, HAnimSegment l_carpal_distal_phalanx_5"

HAnimSegment1229.children.append(TouchSensor1230)
Transform1231 = x3d.Transform()
Transform1231.translation = [0.1948,0.7277,-0.1017]
Shape1232 = x3d.Shape()
Shape1232.USE = "HAnimJointShape"

Transform1231.children.append(Shape1232)

HAnimSegment1229.children.append(Transform1231)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_pinky3'/> to <HAnimSite name='l_pinky_distal_tip'/>
Shape1233 = x3d.Shape()
LineSet1234 = x3d.LineSet()
LineSet1234.vertexCount = [2]
Coordinate1235 = x3d.Coordinate()
Coordinate1235.point = (0.1948,0.7277,-0.1017,0.2014,0.7009,-0.1012)

LineSet1234.coord = Coordinate1235
ColorRGBA1236 = x3d.ColorRGBA()
ColorRGBA1236.USE = "HAnimSiteLineColorRGBA"

LineSet1234.color = ColorRGBA1236

Shape1233.geometry = LineSet1234

HAnimSegment1229.children.append(Shape1233)
HAnimSite1237 = x3d.HAnimSite()
HAnimSite1237.name = "l_carpal_distal_phalanx_5_pt"
HAnimSite1237.DEF = "hanim_l_carpal_distal_phalanx_5_pt"
HAnimSite1237.translation = [0.2014,0.7009,-0.1012]
#HAnimSite visualization shape
TouchSensor1238 = x3d.TouchSensor()
TouchSensor1238.description = "HAnimSite l_pinky_distal_tip"

HAnimSite1237.children.append(TouchSensor1238)
Shape1239 = x3d.Shape()
Shape1239.USE = "HAnimSiteShape"

HAnimSite1237.children.append(Shape1239)

HAnimSegment1229.children.append(HAnimSite1237)

HAnimJoint1228.children.append(HAnimSegment1229)

HAnimJoint1219.children.append(HAnimJoint1228)

HAnimJoint1210.children.append(HAnimJoint1219)

HAnimJoint1201.children.append(HAnimJoint1210)

HAnimJoint989.children.append(HAnimJoint1201)

HAnimJoint952.children.append(HAnimJoint989)

HAnimJoint936.children.append(HAnimJoint952)

HAnimJoint927.children.append(HAnimJoint936)

HAnimJoint890.children.append(HAnimJoint927)

HAnimJoint602.children.append(HAnimJoint890)
HAnimJoint1240 = x3d.HAnimJoint()
HAnimJoint1240.name = "r_sternoclavicular"
HAnimJoint1240.DEF = "hanim_r_sternoclavicular"
HAnimJoint1240.center = [-0.082,1.4488,-0.0353]
HAnimJoint1240.ulimit = [0,0,0]
HAnimJoint1240.llimit = [0,0,0]
HAnimSegment1241 = x3d.HAnimSegment()
HAnimSegment1241.name = "r_clavicle"
HAnimSegment1241.DEF = "hanim_r_clavicle"
#Visualization sphere for <HAnimJoint name='r_sternoclavicular'/> is placed within <HAnimSegment name='r_clavicle'/>
TouchSensor1242 = x3d.TouchSensor()
TouchSensor1242.description = "HAnimJoint r_sternoclavicular, HAnimSegment r_clavicle"

HAnimSegment1241.children.append(TouchSensor1242)
Transform1243 = x3d.Transform()
Transform1243.translation = [-0.082,1.4488,-0.0353]
Shape1244 = x3d.Shape()
Shape1244.USE = "HAnimJointShape"

Transform1243.children.append(Shape1244)

HAnimSegment1241.children.append(Transform1243)
#HAnimSegment visualization line from current <HAnimJoint name='r_sternoclavicular'/> to child <HAnimJoint name='r_acromioclavicular'/>
Shape1245 = x3d.Shape()
LineSet1246 = x3d.LineSet()
LineSet1246.vertexCount = [2]
Coordinate1247 = x3d.Coordinate()
Coordinate1247.point = (-0.0820,1.4488,-0.0353,-0.0962,1.4269,-0.0424)

LineSet1246.coord = Coordinate1247
ColorRGBA1248 = x3d.ColorRGBA()
ColorRGBA1248.USE = "HAnimSegmentLineColorRGBA"

LineSet1246.color = ColorRGBA1248

Shape1245.geometry = LineSet1246

HAnimSegment1241.children.append(Shape1245)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_sternoclavicular'/> to <HAnimSite name='r_clavicale_pt'/>
Shape1249 = x3d.Shape()
LineSet1250 = x3d.LineSet()
LineSet1250.vertexCount = [2]
Coordinate1251 = x3d.Coordinate()
Coordinate1251.point = (-0.0820,1.4488,-0.0353,-0.0115,1.4943,0.0400)

LineSet1250.coord = Coordinate1251
ColorRGBA1252 = x3d.ColorRGBA()
ColorRGBA1252.USE = "HAnimSiteLineColorRGBA"

LineSet1250.color = ColorRGBA1252

Shape1249.geometry = LineSet1250

HAnimSegment1241.children.append(Shape1249)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_sternoclavicular'/> to <HAnimSite name='r_acromion_pt'/>
Shape1253 = x3d.Shape()
LineSet1254 = x3d.LineSet()
LineSet1254.vertexCount = [2]
Coordinate1255 = x3d.Coordinate()
Coordinate1255.point = (-0.0820,1.4488,-0.0353,-0.1905,1.4791,-0.0431)

LineSet1254.coord = Coordinate1255
ColorRGBA1256 = x3d.ColorRGBA()
ColorRGBA1256.USE = "HAnimSiteLineColorRGBA"

LineSet1254.color = ColorRGBA1256

Shape1253.geometry = LineSet1254

HAnimSegment1241.children.append(Shape1253)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_sternoclavicular'/> to <HAnimSite name='r_axilla_ant_pt'/>
Shape1257 = x3d.Shape()
LineSet1258 = x3d.LineSet()
LineSet1258.vertexCount = [2]
Coordinate1259 = x3d.Coordinate()
Coordinate1259.point = (-0.0820,1.4488,-0.0353,-0.1626,1.4072,-0.0031)

LineSet1258.coord = Coordinate1259
ColorRGBA1260 = x3d.ColorRGBA()
ColorRGBA1260.USE = "HAnimSiteLineColorRGBA"

LineSet1258.color = ColorRGBA1260

Shape1257.geometry = LineSet1258

HAnimSegment1241.children.append(Shape1257)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_sternoclavicular'/> to <HAnimSite name='r_axilla_post_pt'/>
Shape1261 = x3d.Shape()
LineSet1262 = x3d.LineSet()
LineSet1262.vertexCount = [2]
Coordinate1263 = x3d.Coordinate()
Coordinate1263.point = (-0.0820,1.4488,-0.0353,-0.1603,1.4098,-0.0826)

LineSet1262.coord = Coordinate1263
ColorRGBA1264 = x3d.ColorRGBA()
ColorRGBA1264.USE = "HAnimSiteLineColorRGBA"

LineSet1262.color = ColorRGBA1264

Shape1261.geometry = LineSet1262

HAnimSegment1241.children.append(Shape1261)
HAnimSite1265 = x3d.HAnimSite()
HAnimSite1265.name = "r_clavicle_pt"
HAnimSite1265.DEF = "hanim_r_clavicle_pt"
HAnimSite1265.translation = [-0.0115,1.4943,0.04]
#HAnimSite visualization shape
TouchSensor1266 = x3d.TouchSensor()
TouchSensor1266.description = "HAnimSite r_clavicale_pt"

HAnimSite1265.children.append(TouchSensor1266)
Shape1267 = x3d.Shape()
Shape1267.USE = "HAnimSiteShape"

HAnimSite1265.children.append(Shape1267)

HAnimSegment1241.children.append(HAnimSite1265)
HAnimSite1268 = x3d.HAnimSite()
HAnimSite1268.name = "r_acromion_pt"
HAnimSite1268.DEF = "hanim_r_acromion_pt"
HAnimSite1268.translation = [-0.1905,1.4791,-0.0431]
#HAnimSite visualization shape
TouchSensor1269 = x3d.TouchSensor()
TouchSensor1269.description = "HAnimSite r_acromion_pt"

HAnimSite1268.children.append(TouchSensor1269)
Shape1270 = x3d.Shape()
Shape1270.USE = "HAnimSiteShape"

HAnimSite1268.children.append(Shape1270)

HAnimSegment1241.children.append(HAnimSite1268)
HAnimSite1271 = x3d.HAnimSite()
HAnimSite1271.name = "r_axilla_proximal_pt"
HAnimSite1271.DEF = "hanim_r_axilla_proximal_pt"
HAnimSite1271.translation = [-0.1626,1.4072,-0.0031]
#HAnimSite visualization shape
TouchSensor1272 = x3d.TouchSensor()
TouchSensor1272.description = "HAnimSite r_axilla_ant_pt"

HAnimSite1271.children.append(TouchSensor1272)
Shape1273 = x3d.Shape()
Shape1273.USE = "HAnimSiteShape"

HAnimSite1271.children.append(Shape1273)

HAnimSegment1241.children.append(HAnimSite1271)
HAnimSite1274 = x3d.HAnimSite()
HAnimSite1274.name = "r_axilla_distal_pt"
HAnimSite1274.DEF = "hanim_r_axilla_distal_pt"
HAnimSite1274.translation = [-0.1603,1.4098,-0.0826]
#HAnimSite visualization shape
TouchSensor1275 = x3d.TouchSensor()
TouchSensor1275.description = "HAnimSite r_axilla_post_pt"

HAnimSite1274.children.append(TouchSensor1275)
Shape1276 = x3d.Shape()
Shape1276.USE = "HAnimSiteShape"

HAnimSite1274.children.append(Shape1276)

HAnimSegment1241.children.append(HAnimSite1274)

HAnimJoint1240.children.append(HAnimSegment1241)
HAnimJoint1277 = x3d.HAnimJoint()
HAnimJoint1277.name = "r_acromioclavicular"
HAnimJoint1277.DEF = "hanim_r_acromioclavicular"
HAnimJoint1277.center = [-0.0962,1.4269,-0.0424]
HAnimJoint1277.ulimit = [0,0,0]
HAnimJoint1277.llimit = [0,0,0]
HAnimSegment1278 = x3d.HAnimSegment()
HAnimSegment1278.name = "r_scapula"
HAnimSegment1278.DEF = "hanim_r_scapula"
#Visualization sphere for <HAnimJoint name='r_acromioclavicular'/> is placed within <HAnimSegment name='r_scapula'/>
TouchSensor1279 = x3d.TouchSensor()
TouchSensor1279.description = "HAnimJoint r_acromioclavicular, HAnimSegment r_scapula"

HAnimSegment1278.children.append(TouchSensor1279)
Transform1280 = x3d.Transform()
Transform1280.translation = [-0.0962,1.4269,-0.0424]
Shape1281 = x3d.Shape()
Shape1281.USE = "HAnimJointShape"

Transform1280.children.append(Shape1281)

HAnimSegment1278.children.append(Transform1280)
#HAnimSegment visualization line from current <HAnimJoint name='r_acromioclavicular'/> to child <HAnimJoint name='r_shoulder'/>
Shape1282 = x3d.Shape()
LineSet1283 = x3d.LineSet()
LineSet1283.vertexCount = [2]
Coordinate1284 = x3d.Coordinate()
Coordinate1284.point = (-0.0962,1.4269,-0.0424,-0.2029,1.4376,-0.0387)

LineSet1283.coord = Coordinate1284
ColorRGBA1285 = x3d.ColorRGBA()
ColorRGBA1285.USE = "HAnimSegmentLineColorRGBA"

LineSet1283.color = ColorRGBA1285

Shape1282.geometry = LineSet1283

HAnimSegment1278.children.append(Shape1282)

HAnimJoint1277.children.append(HAnimSegment1278)
HAnimJoint1286 = x3d.HAnimJoint()
HAnimJoint1286.name = "r_shoulder"
HAnimJoint1286.DEF = "hanim_r_shoulder"
HAnimJoint1286.center = [-0.2029,1.4376,-0.0387]
HAnimJoint1286.ulimit = [0,0,0]
HAnimJoint1286.llimit = [0,0,0]
HAnimSegment1287 = x3d.HAnimSegment()
HAnimSegment1287.name = "r_upperarm"
HAnimSegment1287.DEF = "hanim_r_upperarm"
#Visualization sphere for <HAnimJoint name='r_shoulder'/> is placed within <HAnimSegment name='r_upperarm'/>
TouchSensor1288 = x3d.TouchSensor()
TouchSensor1288.description = "HAnimJoint r_shoulder, HAnimSegment r_upperarm"

HAnimSegment1287.children.append(TouchSensor1288)
Transform1289 = x3d.Transform()
Transform1289.translation = [-0.2029,1.4376,-0.0387]
Shape1290 = x3d.Shape()
Shape1290.USE = "HAnimJointShape"

Transform1289.children.append(Shape1290)

HAnimSegment1287.children.append(Transform1289)
#HAnimSegment visualization line from current <HAnimJoint name='r_shoulder'/> to child <HAnimJoint name='r_elbow'/>
Shape1291 = x3d.Shape()
LineSet1292 = x3d.LineSet()
LineSet1292.vertexCount = [2]
Coordinate1293 = x3d.Coordinate()
Coordinate1293.point = (-0.2029,1.4376,-0.0387,-0.2014,1.1357,-0.0682)

LineSet1292.coord = Coordinate1293
ColorRGBA1294 = x3d.ColorRGBA()
ColorRGBA1294.USE = "HAnimSegmentLineColorRGBA"

LineSet1292.color = ColorRGBA1294

Shape1291.geometry = LineSet1292

HAnimSegment1287.children.append(Shape1291)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_shoulder'/> to <HAnimSite name='r_humeral_lateral_epicn_pt'/>
Shape1295 = x3d.Shape()
LineSet1296 = x3d.LineSet()
LineSet1296.vertexCount = [2]
Coordinate1297 = x3d.Coordinate()
Coordinate1297.point = (-0.2029,1.4376,-0.0387,-0.2224,1.1517,-0.1033)

LineSet1296.coord = Coordinate1297
ColorRGBA1298 = x3d.ColorRGBA()
ColorRGBA1298.USE = "HAnimSiteLineColorRGBA"

LineSet1296.color = ColorRGBA1298

Shape1295.geometry = LineSet1296

HAnimSegment1287.children.append(Shape1295)
HAnimSite1299 = x3d.HAnimSite()
HAnimSite1299.name = "r_humeral_lateral_epicondyle_pt"
HAnimSite1299.DEF = "hanim_r_humeral_lateral_epicondyle_pt"
HAnimSite1299.translation = [-0.2224,1.1517,-0.1033]
#HAnimSite visualization shape
TouchSensor1300 = x3d.TouchSensor()
TouchSensor1300.description = "HAnimSite r_humeral_lateral_epicn_pt"

HAnimSite1299.children.append(TouchSensor1300)
Shape1301 = x3d.Shape()
Shape1301.USE = "HAnimSiteShape"

HAnimSite1299.children.append(Shape1301)

HAnimSegment1287.children.append(HAnimSite1299)

HAnimJoint1286.children.append(HAnimSegment1287)
HAnimJoint1302 = x3d.HAnimJoint()
HAnimJoint1302.name = "r_elbow"
HAnimJoint1302.DEF = "hanim_r_elbow"
HAnimJoint1302.center = [-0.2014,1.1357,-0.0682]
HAnimJoint1302.ulimit = [0,0,0]
HAnimJoint1302.llimit = [0,0,0]
HAnimSegment1303 = x3d.HAnimSegment()
HAnimSegment1303.name = "r_forearm"
HAnimSegment1303.DEF = "hanim_r_forearm"
#Visualization sphere for <HAnimJoint name='r_elbow'/> is placed within <HAnimSegment name='r_forearm'/>
TouchSensor1304 = x3d.TouchSensor()
TouchSensor1304.description = "HAnimJoint r_elbow, HAnimSegment r_forearm"

HAnimSegment1303.children.append(TouchSensor1304)
Transform1305 = x3d.Transform()
Transform1305.translation = [-0.2014,1.1357,-0.0682]
Shape1306 = x3d.Shape()
Shape1306.USE = "HAnimJointShape"

Transform1305.children.append(Shape1306)

HAnimSegment1303.children.append(Transform1305)
#HAnimSegment visualization line from current <HAnimJoint name='r_elbow'/> to child <HAnimJoint name='r_radiocarpal'/>
Shape1307 = x3d.Shape()
LineSet1308 = x3d.LineSet()
LineSet1308.vertexCount = [2]
Coordinate1309 = x3d.Coordinate()
Coordinate1309.point = (-0.2014,1.1357,-0.0682,-0.1984,0.8663,-0.0583)

LineSet1308.coord = Coordinate1309
ColorRGBA1310 = x3d.ColorRGBA()
ColorRGBA1310.USE = "HAnimSegmentLineColorRGBA"

LineSet1308.color = ColorRGBA1310

Shape1307.geometry = LineSet1308

HAnimSegment1303.children.append(Shape1307)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_elbow'/> to <HAnimSite name='r_radial_styloid_pt'/>
Shape1311 = x3d.Shape()
LineSet1312 = x3d.LineSet()
LineSet1312.vertexCount = [2]
Coordinate1313 = x3d.Coordinate()
Coordinate1313.point = (-0.2014,1.1357,-0.0682,-0.1884,0.8676,-0.0360)

LineSet1312.coord = Coordinate1313
ColorRGBA1314 = x3d.ColorRGBA()
ColorRGBA1314.USE = "HAnimSiteLineColorRGBA"

LineSet1312.color = ColorRGBA1314

Shape1311.geometry = LineSet1312

HAnimSegment1303.children.append(Shape1311)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_elbow'/> to <HAnimSite name='r_olecranon_pt'/>
Shape1315 = x3d.Shape()
LineSet1316 = x3d.LineSet()
LineSet1316.vertexCount = [2]
Coordinate1317 = x3d.Coordinate()
Coordinate1317.point = (-0.2014,1.1357,-0.0682,-0.1907,1.1405,-0.1065)

LineSet1316.coord = Coordinate1317
ColorRGBA1318 = x3d.ColorRGBA()
ColorRGBA1318.USE = "HAnimSiteLineColorRGBA"

LineSet1316.color = ColorRGBA1318

Shape1315.geometry = LineSet1316

HAnimSegment1303.children.append(Shape1315)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_elbow'/> to <HAnimSite name='r_humeral_medial_epicn_pt'/>
Shape1319 = x3d.Shape()
LineSet1320 = x3d.LineSet()
LineSet1320.vertexCount = [2]
Coordinate1321 = x3d.Coordinate()
Coordinate1321.point = (-0.2014,1.1357,-0.0682,-0.1680,1.1298,-0.1062)

LineSet1320.coord = Coordinate1321
ColorRGBA1322 = x3d.ColorRGBA()
ColorRGBA1322.USE = "HAnimSiteLineColorRGBA"

LineSet1320.color = ColorRGBA1322

Shape1319.geometry = LineSet1320

HAnimSegment1303.children.append(Shape1319)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_elbow'/> to <HAnimSite name='r_radiale_pt'/>
Shape1323 = x3d.Shape()
LineSet1324 = x3d.LineSet()
LineSet1324.vertexCount = [2]
Coordinate1325 = x3d.Coordinate()
Coordinate1325.point = (-0.2014,1.1357,-0.0682,-0.2130,1.1305,-0.1091)

LineSet1324.coord = Coordinate1325
ColorRGBA1326 = x3d.ColorRGBA()
ColorRGBA1326.USE = "HAnimSiteLineColorRGBA"

LineSet1324.color = ColorRGBA1326

Shape1323.geometry = LineSet1324

HAnimSegment1303.children.append(Shape1323)
HAnimSite1327 = x3d.HAnimSite()
HAnimSite1327.name = "r_radial_styloid_pt"
HAnimSite1327.DEF = "hanim_r_radial_styloid_pt"
HAnimSite1327.translation = [-0.1884,0.8676,-0.036]
#HAnimSite visualization shape
TouchSensor1328 = x3d.TouchSensor()
TouchSensor1328.description = "HAnimSite r_radial_styloid_pt"

HAnimSite1327.children.append(TouchSensor1328)
Shape1329 = x3d.Shape()
Shape1329.USE = "HAnimSiteShape"

HAnimSite1327.children.append(Shape1329)

HAnimSegment1303.children.append(HAnimSite1327)
HAnimSite1330 = x3d.HAnimSite()
HAnimSite1330.name = "r_olecranon_pt"
HAnimSite1330.DEF = "hanim_r_olecranon_pt"
HAnimSite1330.translation = [-0.1907,1.1405,-0.1065]
#HAnimSite visualization shape
TouchSensor1331 = x3d.TouchSensor()
TouchSensor1331.description = "HAnimSite r_olecranon_pt"

HAnimSite1330.children.append(TouchSensor1331)
Shape1332 = x3d.Shape()
Shape1332.USE = "HAnimSiteShape"

HAnimSite1330.children.append(Shape1332)

HAnimSegment1303.children.append(HAnimSite1330)
HAnimSite1333 = x3d.HAnimSite()
HAnimSite1333.name = "r_humeral_medial_epicondyle_pt"
HAnimSite1333.DEF = "hanim_r_humeral_medial_epicondyle_pt"
HAnimSite1333.translation = [-0.168,1.1298,-0.1062]
#HAnimSite visualization shape
TouchSensor1334 = x3d.TouchSensor()
TouchSensor1334.description = "HAnimSite r_humeral_medial_epicn_pt"

HAnimSite1333.children.append(TouchSensor1334)
Shape1335 = x3d.Shape()
Shape1335.USE = "HAnimSiteShape"

HAnimSite1333.children.append(Shape1335)

HAnimSegment1303.children.append(HAnimSite1333)
HAnimSite1336 = x3d.HAnimSite()
HAnimSite1336.name = "r_radiale_pt"
HAnimSite1336.DEF = "hanim_r_radiale_pt"
HAnimSite1336.translation = [-0.213,1.1305,-0.1091]
#HAnimSite visualization shape
TouchSensor1337 = x3d.TouchSensor()
TouchSensor1337.description = "HAnimSite r_radiale_pt"

HAnimSite1336.children.append(TouchSensor1337)
Shape1338 = x3d.Shape()
Shape1338.USE = "HAnimSiteShape"

HAnimSite1336.children.append(Shape1338)

HAnimSegment1303.children.append(HAnimSite1336)

HAnimJoint1302.children.append(HAnimSegment1303)
HAnimJoint1339 = x3d.HAnimJoint()
HAnimJoint1339.name = "r_radiocarpal"
HAnimJoint1339.DEF = "hanim_r_radiocarpal"
HAnimJoint1339.center = [-0.1984,0.8663,-0.0583]
HAnimJoint1339.ulimit = [0,0,0]
HAnimJoint1339.llimit = [0,0,0]
HAnimSegment1340 = x3d.HAnimSegment()
HAnimSegment1340.name = "r_carpal"
HAnimSegment1340.DEF = "hanim_r_carpal"
#Visualization sphere for <HAnimJoint name='r_radiocarpal'/> is placed within <HAnimSegment name='r_carpal'/>
TouchSensor1341 = x3d.TouchSensor()
TouchSensor1341.description = "HAnimJoint r_radiocarpal, HAnimSegment r_carpal"

HAnimSegment1340.children.append(TouchSensor1341)
Transform1342 = x3d.Transform()
Transform1342.translation = [-0.1984,0.8663,-0.0583]
Shape1343 = x3d.Shape()
Shape1343.USE = "HAnimJointShape"

Transform1342.children.append(Shape1343)

HAnimSegment1340.children.append(Transform1342)
#HAnimSegment visualization line from current <HAnimJoint name='r_radiocarpal'/> to child <HAnimJoint name='r_thumb1'/>
Shape1344 = x3d.Shape()
LineSet1345 = x3d.LineSet()
LineSet1345.vertexCount = [2]
Coordinate1346 = x3d.Coordinate()
Coordinate1346.point = (-0.1984,0.8663,-0.0583,-0.1924,0.8472,-0.0534)

LineSet1345.coord = Coordinate1346
ColorRGBA1347 = x3d.ColorRGBA()
ColorRGBA1347.USE = "HAnimSegmentLineColorRGBA"

LineSet1345.color = ColorRGBA1347

Shape1344.geometry = LineSet1345

HAnimSegment1340.children.append(Shape1344)
#HAnimSegment visualization line from current <HAnimJoint name='r_radiocarpal'/> to child <HAnimJoint name='r_index0'/>
Shape1348 = x3d.Shape()
LineSet1349 = x3d.LineSet()
LineSet1349.vertexCount = [2]
Coordinate1350 = x3d.Coordinate()
Coordinate1350.point = (-0.1984,0.8663,-0.0583,-0.1983,0.8024,-0.0280)

LineSet1349.coord = Coordinate1350
ColorRGBA1351 = x3d.ColorRGBA()
ColorRGBA1351.USE = "HAnimSegmentLineColorRGBA"

LineSet1349.color = ColorRGBA1351

Shape1348.geometry = LineSet1349

HAnimSegment1340.children.append(Shape1348)
#HAnimSegment visualization line from current <HAnimJoint name='r_radiocarpal'/> to child <HAnimJoint name='r_middle0'/>
Shape1352 = x3d.Shape()
LineSet1353 = x3d.LineSet()
LineSet1353.vertexCount = [2]
Coordinate1354 = x3d.Coordinate()
Coordinate1354.point = (-0.1984,0.8663,-0.0583,-0.1987,0.8029,-0.0530)

LineSet1353.coord = Coordinate1354
ColorRGBA1355 = x3d.ColorRGBA()
ColorRGBA1355.USE = "HAnimSegmentLineColorRGBA"

LineSet1353.color = ColorRGBA1355

Shape1352.geometry = LineSet1353

HAnimSegment1340.children.append(Shape1352)
#HAnimSegment visualization line from current <HAnimJoint name='r_radiocarpal'/> to child <HAnimJoint name='r_ring0'/>
Shape1356 = x3d.Shape()
LineSet1357 = x3d.LineSet()
LineSet1357.vertexCount = [2]
Coordinate1358 = x3d.Coordinate()
Coordinate1358.point = (-0.1984,0.8663,-0.0583,-0.1956,0.8019,-0.0794)

LineSet1357.coord = Coordinate1358
ColorRGBA1359 = x3d.ColorRGBA()
ColorRGBA1359.USE = "HAnimSegmentLineColorRGBA"

LineSet1357.color = ColorRGBA1359

Shape1356.geometry = LineSet1357

HAnimSegment1340.children.append(Shape1356)
#HAnimSegment visualization line from current <HAnimJoint name='r_radiocarpal'/> to child <HAnimJoint name='r_pinky0'/>
Shape1360 = x3d.Shape()
LineSet1361 = x3d.LineSet()
LineSet1361.vertexCount = [2]
Coordinate1362 = x3d.Coordinate()
Coordinate1362.point = (-0.1984,0.8663,-0.0583,-0.1925,0.8066,-0.1036)

LineSet1361.coord = Coordinate1362
ColorRGBA1363 = x3d.ColorRGBA()
ColorRGBA1363.USE = "HAnimSegmentLineColorRGBA"

LineSet1361.color = ColorRGBA1363

Shape1360.geometry = LineSet1361

HAnimSegment1340.children.append(Shape1360)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_radiocarpal'/> to <HAnimSite name='r_metacarpal_pha2_pt'/>
Shape1364 = x3d.Shape()
LineSet1365 = x3d.LineSet()
LineSet1365.vertexCount = [2]
Coordinate1366 = x3d.Coordinate()
Coordinate1366.point = (-0.1984,0.8663,-0.0583,-0.1977,0.8169,-0.0177)

LineSet1365.coord = Coordinate1366
ColorRGBA1367 = x3d.ColorRGBA()
ColorRGBA1367.USE = "HAnimSiteLineColorRGBA"

LineSet1365.color = ColorRGBA1367

Shape1364.geometry = LineSet1365

HAnimSegment1340.children.append(Shape1364)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_radiocarpal'/> to <HAnimSite name='r_ulnar_styloid_pt'/>
Shape1368 = x3d.Shape()
LineSet1369 = x3d.LineSet()
LineSet1369.vertexCount = [2]
Coordinate1370 = x3d.Coordinate()
Coordinate1370.point = (-0.1984,0.8663,-0.0583,-0.2117,0.8562,-0.0584)

LineSet1369.coord = Coordinate1370
ColorRGBA1371 = x3d.ColorRGBA()
ColorRGBA1371.USE = "HAnimSiteLineColorRGBA"

LineSet1369.color = ColorRGBA1371

Shape1368.geometry = LineSet1369

HAnimSegment1340.children.append(Shape1368)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_radiocarpal'/> to <HAnimSite name='r_metacarpal_pha5_pt'/>
Shape1372 = x3d.Shape()
LineSet1373 = x3d.LineSet()
LineSet1373.vertexCount = [2]
Coordinate1374 = x3d.Coordinate()
Coordinate1374.point = (-0.1984,0.8663,-0.0583,-0.1929,0.7890,-0.1064)

LineSet1373.coord = Coordinate1374
ColorRGBA1375 = x3d.ColorRGBA()
ColorRGBA1375.USE = "HAnimSiteLineColorRGBA"

LineSet1373.color = ColorRGBA1375

Shape1372.geometry = LineSet1373

HAnimSegment1340.children.append(Shape1372)
#HAnimSite/Viewpoint visualization line segment from ancestor <HAnimJoint name='r_radiocarpal'/> to <HAnimSite name='r_hand_front_view'/>
Shape1376 = x3d.Shape()
LineSet1377 = x3d.LineSet()
LineSet1377.vertexCount = [2]
Coordinate1378 = x3d.Coordinate()
Coordinate1378.point = (-0.1984,0.8663,-0.0583,-0.3000,0.7500,0.4500)

LineSet1377.coord = Coordinate1378
ColorRGBA1379 = x3d.ColorRGBA()
ColorRGBA1379.USE = "HAnimSiteViewpointLineColorRGBA"

LineSet1377.color = ColorRGBA1379

Shape1376.geometry = LineSet1377

HAnimSegment1340.children.append(Shape1376)
HAnimSite1380 = x3d.HAnimSite()
HAnimSite1380.name = "r_metacarpal_phalanx_2_pt"
HAnimSite1380.DEF = "hanim_r_metacarpal_phalanx_2_pt"
HAnimSite1380.translation = [-0.1977,0.8169,-0.0177]
#HAnimSite visualization shape
TouchSensor1381 = x3d.TouchSensor()
TouchSensor1381.description = "HAnimSite r_metacarpal_pha2_pt"

HAnimSite1380.children.append(TouchSensor1381)
Shape1382 = x3d.Shape()
Shape1382.USE = "HAnimSiteShape"

HAnimSite1380.children.append(Shape1382)

HAnimSegment1340.children.append(HAnimSite1380)
HAnimSite1383 = x3d.HAnimSite()
HAnimSite1383.name = "r_ulnar_styloid_pt"
HAnimSite1383.DEF = "hanim_r_ulnar_styloid_pt"
HAnimSite1383.translation = [-0.2117,0.8562,-0.0584]
#HAnimSite visualization shape
TouchSensor1384 = x3d.TouchSensor()
TouchSensor1384.description = "HAnimSite r_ulnar_styloid_pt"

HAnimSite1383.children.append(TouchSensor1384)
Shape1385 = x3d.Shape()
Shape1385.USE = "HAnimSiteShape"

HAnimSite1383.children.append(Shape1385)

HAnimSegment1340.children.append(HAnimSite1383)
HAnimSite1386 = x3d.HAnimSite()
HAnimSite1386.name = "r_metacarpal_phalanx_5_pt"
HAnimSite1386.DEF = "hanim_r_metacarpal_phalanx_5_pt"
HAnimSite1386.translation = [-0.1929,0.789,-0.1064]
#HAnimSite visualization shape
TouchSensor1387 = x3d.TouchSensor()
TouchSensor1387.description = "HAnimSite r_metacarpal_pha5_pt"

HAnimSite1386.children.append(TouchSensor1387)
Shape1388 = x3d.Shape()
Shape1388.USE = "HAnimSiteShape"

HAnimSite1386.children.append(Shape1388)

HAnimSegment1340.children.append(HAnimSite1386)
HAnimSite1389 = x3d.HAnimSite()
HAnimSite1389.name = "r_hand_front_view"
HAnimSite1389.DEF = "hanim_r_hand_front_view"
HAnimSite1389.translation = [-0.3,0.75,0.45]
#HAnimSite visualization shape
TouchSensor1390 = x3d.TouchSensor()
TouchSensor1390.description = "HAnimSite r_hand_front_view"

HAnimSite1389.children.append(TouchSensor1390)
Shape1391 = x3d.Shape()
Shape1391.USE = "HAnimSiteShape"

HAnimSite1389.children.append(Shape1391)
Viewpoint1392 = x3d.Viewpoint()
Viewpoint1392.DEF = "hanim_r_hand_front_viewpoint"
Viewpoint1392.centerOfRotation = [0,0.7,0]
Viewpoint1392.description = "right hand front"
Viewpoint1392.position = [0,0,0]

HAnimSite1389.children.append(Viewpoint1392)
#HAnimSite/Viewpoint visualization shape
Anchor1393 = x3d.Anchor()
Anchor1393.description = "HAnimSite hanim_r_hand_front_view Viewpoint"
Anchor1393.url = ["#hanim_r_hand_front_viewpoint"]
LOD1394 = x3d.LOD()
LOD1394.forceTransitions = True
LOD1394.range = [0.04]
WorldInfo1395 = x3d.WorldInfo()
WorldInfo1395.info = ["hide diamond when close"]

LOD1394.children.append(WorldInfo1395)
Shape1396 = x3d.Shape()
Shape1396.USE = "HAnimSiteViewpointShape"

LOD1394.children.append(Shape1396)

Anchor1393.children.append(LOD1394)

HAnimSite1389.children.append(Anchor1393)

HAnimSegment1340.children.append(HAnimSite1389)

HAnimJoint1339.children.append(HAnimSegment1340)
HAnimJoint1397 = x3d.HAnimJoint()
HAnimJoint1397.name = "r_carpometacarpal_1"
HAnimJoint1397.DEF = "hanim_r_carpometacarpal_1"
HAnimJoint1397.center = [-0.1924,0.8472,-0.0534]
HAnimJoint1397.ulimit = [0,0,0]
HAnimJoint1397.llimit = [0,0,0]
HAnimSegment1398 = x3d.HAnimSegment()
HAnimSegment1398.name = "r_metacarpal_1"
HAnimSegment1398.DEF = "hanim_r_metacarpal_1"
#Visualization sphere for <HAnimJoint name='r_thumb1'/> is placed within <HAnimSegment name='r_metacarpal_1'/>
TouchSensor1399 = x3d.TouchSensor()
TouchSensor1399.description = "HAnimJoint r_thumb1, HAnimSegment r_metacarpal_1"

HAnimSegment1398.children.append(TouchSensor1399)
Transform1400 = x3d.Transform()
Transform1400.translation = [-0.1924,0.8472,-0.0534]
Shape1401 = x3d.Shape()
Shape1401.USE = "HAnimJointShape"

Transform1400.children.append(Shape1401)

HAnimSegment1398.children.append(Transform1400)
#HAnimSegment visualization line from current <HAnimJoint name='r_thumb1'/> to child <HAnimJoint name='r_thumb2'/>
Shape1402 = x3d.Shape()
LineSet1403 = x3d.LineSet()
LineSet1403.vertexCount = [2]
Coordinate1404 = x3d.Coordinate()
Coordinate1404.point = (-0.1924,0.8472,-0.0534,-0.1951,0.8226,0.0246)

LineSet1403.coord = Coordinate1404
ColorRGBA1405 = x3d.ColorRGBA()
ColorRGBA1405.USE = "HAnimSegmentLineColorRGBA"

LineSet1403.color = ColorRGBA1405

Shape1402.geometry = LineSet1403

HAnimSegment1398.children.append(Shape1402)

HAnimJoint1397.children.append(HAnimSegment1398)
HAnimJoint1406 = x3d.HAnimJoint()
HAnimJoint1406.name = "r_metacarpophalangeal_1"
HAnimJoint1406.DEF = "hanim_r_metacarpophalangeal_1"
HAnimJoint1406.center = [-0.1951,0.8226,0.0246]
HAnimJoint1406.ulimit = [0,0,0]
HAnimJoint1406.llimit = [0,0,0]
HAnimSegment1407 = x3d.HAnimSegment()
HAnimSegment1407.name = "r_carpal_proximal_phalanx_1"
HAnimSegment1407.DEF = "hanim_r_carpal_proximal_phalanx_1"
#Visualization sphere for <HAnimJoint name='r_thumb2'/> is placed within <HAnimSegment name='r_carpal_proximal_phalanx_1'/>
TouchSensor1408 = x3d.TouchSensor()
TouchSensor1408.description = "HAnimJoint r_thumb2, HAnimSegment r_carpal_proximal_phalanx_1"

HAnimSegment1407.children.append(TouchSensor1408)
Transform1409 = x3d.Transform()
Transform1409.translation = [-0.1951,0.8226,0.0246]
Shape1410 = x3d.Shape()
Shape1410.USE = "HAnimJointShape"

Transform1409.children.append(Shape1410)

HAnimSegment1407.children.append(Transform1409)
#HAnimSegment visualization line from current <HAnimJoint name='r_thumb2'/> to child <HAnimJoint name='r_thumb3'/>
Shape1411 = x3d.Shape()
LineSet1412 = x3d.LineSet()
LineSet1412.vertexCount = [2]
Coordinate1413 = x3d.Coordinate()
Coordinate1413.point = (-0.1951,0.8226,0.0246,-0.1955,0.8159,0.0464)

LineSet1412.coord = Coordinate1413
ColorRGBA1414 = x3d.ColorRGBA()
ColorRGBA1414.USE = "HAnimSegmentLineColorRGBA"

LineSet1412.color = ColorRGBA1414

Shape1411.geometry = LineSet1412

HAnimSegment1407.children.append(Shape1411)

HAnimJoint1406.children.append(HAnimSegment1407)
HAnimJoint1415 = x3d.HAnimJoint()
HAnimJoint1415.name = "r_carpal_interphalangeal_1"
HAnimJoint1415.DEF = "hanim_r_carpal_interphalangeal_1"
HAnimJoint1415.center = [-0.1955,0.8159,0.0464]
HAnimJoint1415.ulimit = [0,0,0]
HAnimJoint1415.llimit = [0,0,0]
HAnimSegment1416 = x3d.HAnimSegment()
HAnimSegment1416.name = "r_carpal_distal_phalanx_1"
HAnimSegment1416.DEF = "hanim_r_carpal_distal_phalanx_1"
#Visualization sphere for <HAnimJoint name='r_thumb3'/> is placed within <HAnimSegment name='r_carpal_distal_phalanx_1'/>
TouchSensor1417 = x3d.TouchSensor()
TouchSensor1417.description = "HAnimJoint r_thumb3, HAnimSegment r_carpal_distal_phalanx_1"

HAnimSegment1416.children.append(TouchSensor1417)
Transform1418 = x3d.Transform()
Transform1418.translation = [-0.1955,0.8159,0.0464]
Shape1419 = x3d.Shape()
Shape1419.USE = "HAnimJointShape"

Transform1418.children.append(Shape1419)

HAnimSegment1416.children.append(Transform1418)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_thumb3'/> to <HAnimSite name='r_thumb_distal_tip'/>
Shape1420 = x3d.Shape()
LineSet1421 = x3d.LineSet()
LineSet1421.vertexCount = [2]
Coordinate1422 = x3d.Coordinate()
Coordinate1422.point = (-0.1955,0.8159,0.0464,-0.1869,0.8090,0.0820)

LineSet1421.coord = Coordinate1422
ColorRGBA1423 = x3d.ColorRGBA()
ColorRGBA1423.USE = "HAnimSiteLineColorRGBA"

LineSet1421.color = ColorRGBA1423

Shape1420.geometry = LineSet1421

HAnimSegment1416.children.append(Shape1420)
HAnimSite1424 = x3d.HAnimSite()
HAnimSite1424.name = "r_carpal_distal_phalanx_1_pt"
HAnimSite1424.DEF = "hanim_r_carpal_distal_phalanx_1_pt"
HAnimSite1424.translation = [-0.1869,0.809,0.082]
#HAnimSite visualization shape
TouchSensor1425 = x3d.TouchSensor()
TouchSensor1425.description = "HAnimSite r_thumb_distal_tip"

HAnimSite1424.children.append(TouchSensor1425)
Shape1426 = x3d.Shape()
Shape1426.USE = "HAnimSiteShape"

HAnimSite1424.children.append(Shape1426)

HAnimSegment1416.children.append(HAnimSite1424)

HAnimJoint1415.children.append(HAnimSegment1416)

HAnimJoint1406.children.append(HAnimJoint1415)

HAnimJoint1397.children.append(HAnimJoint1406)

HAnimJoint1339.children.append(HAnimJoint1397)
HAnimJoint1427 = x3d.HAnimJoint()
HAnimJoint1427.name = "r_carpometacarpal_2"
HAnimJoint1427.DEF = "hanim_r_carpometacarpal_2"
HAnimJoint1427.center = [-0.1983,0.8024,-0.028]
HAnimJoint1427.ulimit = [0,0,0]
HAnimJoint1427.llimit = [0,0,0]
HAnimSegment1428 = x3d.HAnimSegment()
HAnimSegment1428.name = "r_metacarpal_2"
HAnimSegment1428.DEF = "hanim_r_metacarpal_2"
#Visualization sphere for <HAnimJoint name='r_index0'/> is placed within <HAnimSegment name='r_metacarpal_2'/>
TouchSensor1429 = x3d.TouchSensor()
TouchSensor1429.description = "HAnimJoint r_index0, HAnimSegment r_metacarpal_2"

HAnimSegment1428.children.append(TouchSensor1429)
Transform1430 = x3d.Transform()
Transform1430.translation = [-0.1983,0.8024,-0.028]
Shape1431 = x3d.Shape()
Shape1431.USE = "HAnimJointShape"

Transform1430.children.append(Shape1431)

HAnimSegment1428.children.append(Transform1430)
#HAnimSegment visualization line from current <HAnimJoint name='r_index0'/> to child <HAnimJoint name='r_index1'/>
Shape1432 = x3d.Shape()
LineSet1433 = x3d.LineSet()
LineSet1433.vertexCount = [2]
Coordinate1434 = x3d.Coordinate()
Coordinate1434.point = (-0.1983,0.8024,-0.0280,-0.1983,0.7815,-0.0280)

LineSet1433.coord = Coordinate1434
ColorRGBA1435 = x3d.ColorRGBA()
ColorRGBA1435.USE = "HAnimSegmentLineColorRGBA"

LineSet1433.color = ColorRGBA1435

Shape1432.geometry = LineSet1433

HAnimSegment1428.children.append(Shape1432)

HAnimJoint1427.children.append(HAnimSegment1428)
HAnimJoint1436 = x3d.HAnimJoint()
HAnimJoint1436.name = "r_metacarpophalangeal_2"
HAnimJoint1436.DEF = "hanim_r_metacarpophalangeal_2"
HAnimJoint1436.center = [-0.1983,0.7815,-0.028]
HAnimJoint1436.ulimit = [0,0,0]
HAnimJoint1436.llimit = [0,0,0]
HAnimSegment1437 = x3d.HAnimSegment()
HAnimSegment1437.name = "r_carpal_proximal_phalanx_2"
HAnimSegment1437.DEF = "hanim_r_carpal_proximal_phalanx_2"
#Visualization sphere for <HAnimJoint name='r_index1'/> is placed within <HAnimSegment name='r_carpal_proximal_phalanx_2'/>
TouchSensor1438 = x3d.TouchSensor()
TouchSensor1438.description = "HAnimJoint r_index1, HAnimSegment r_carpal_proximal_phalanx_2"

HAnimSegment1437.children.append(TouchSensor1438)
Transform1439 = x3d.Transform()
Transform1439.translation = [-0.1983,0.7815,-0.028]
Shape1440 = x3d.Shape()
Shape1440.USE = "HAnimJointShape"

Transform1439.children.append(Shape1440)

HAnimSegment1437.children.append(Transform1439)
#HAnimSegment visualization line from current <HAnimJoint name='r_index1'/> to child <HAnimJoint name='r_index2'/>
Shape1441 = x3d.Shape()
LineSet1442 = x3d.LineSet()
LineSet1442.vertexCount = [2]
Coordinate1443 = x3d.Coordinate()
Coordinate1443.point = (-0.1983,0.7815,-0.0280,-0.2017,0.7363,-0.0248)

LineSet1442.coord = Coordinate1443
ColorRGBA1444 = x3d.ColorRGBA()
ColorRGBA1444.USE = "HAnimSegmentLineColorRGBA"

LineSet1442.color = ColorRGBA1444

Shape1441.geometry = LineSet1442

HAnimSegment1437.children.append(Shape1441)

HAnimJoint1436.children.append(HAnimSegment1437)
HAnimJoint1445 = x3d.HAnimJoint()
HAnimJoint1445.name = "r_carpal_proximal_interphalangeal_2"
HAnimJoint1445.DEF = "hanim_r_carpal_proximal_interphalangeal_2"
HAnimJoint1445.center = [-0.2017,0.7363,-0.0248]
HAnimJoint1445.ulimit = [0,0,0]
HAnimJoint1445.llimit = [0,0,0]
HAnimSegment1446 = x3d.HAnimSegment()
HAnimSegment1446.name = "r_carpal_middle_phalanx_2"
HAnimSegment1446.DEF = "hanim_r_carpal_middle_phalanx_2"
#Visualization sphere for <HAnimJoint name='r_index2'/> is placed within <HAnimSegment name='r_carpal_middle_phalanx_2'/>
TouchSensor1447 = x3d.TouchSensor()
TouchSensor1447.description = "HAnimJoint r_index2, HAnimSegment r_carpal_middle_phalanx_2"

HAnimSegment1446.children.append(TouchSensor1447)
Transform1448 = x3d.Transform()
Transform1448.translation = [-0.2017,0.7363,-0.0248]
Shape1449 = x3d.Shape()
Shape1449.USE = "HAnimJointShape"

Transform1448.children.append(Shape1449)

HAnimSegment1446.children.append(Transform1448)
#HAnimSegment visualization line from current <HAnimJoint name='r_index2'/> to child <HAnimJoint name='r_index3'/>
Shape1450 = x3d.Shape()
LineSet1451 = x3d.LineSet()
LineSet1451.vertexCount = [2]
Coordinate1452 = x3d.Coordinate()
Coordinate1452.point = (-0.2017,0.7363,-0.0248,-0.2028,0.7139,-0.0236)

LineSet1451.coord = Coordinate1452
ColorRGBA1453 = x3d.ColorRGBA()
ColorRGBA1453.USE = "HAnimSegmentLineColorRGBA"

LineSet1451.color = ColorRGBA1453

Shape1450.geometry = LineSet1451

HAnimSegment1446.children.append(Shape1450)

HAnimJoint1445.children.append(HAnimSegment1446)
HAnimJoint1454 = x3d.HAnimJoint()
HAnimJoint1454.name = "r_carpal_distal_interphalangeal_2"
HAnimJoint1454.DEF = "hanim_r_carpal_distal_interphalangeal_2"
HAnimJoint1454.center = [-0.2028,0.7139,-0.0236]
HAnimJoint1454.ulimit = [0,0,0]
HAnimJoint1454.llimit = [0,0,0]
HAnimSegment1455 = x3d.HAnimSegment()
HAnimSegment1455.name = "r_carpal_distal_phalanx_2"
HAnimSegment1455.DEF = "hanim_r_carpal_distal_phalanx_2"
#Visualization sphere for <HAnimJoint name='r_index3'/> is placed within <HAnimSegment name='r_carpal_distal_phalanx_2'/>
TouchSensor1456 = x3d.TouchSensor()
TouchSensor1456.description = "HAnimJoint r_index3, HAnimSegment r_carpal_distal_phalanx_2"

HAnimSegment1455.children.append(TouchSensor1456)
Transform1457 = x3d.Transform()
Transform1457.translation = [-0.2028,0.7139,-0.0236]
Shape1458 = x3d.Shape()
Shape1458.USE = "HAnimJointShape"

Transform1457.children.append(Shape1458)

HAnimSegment1455.children.append(Transform1457)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_index3'/> to <HAnimSite name='r_index_distal_tip'/>
Shape1459 = x3d.Shape()
LineSet1460 = x3d.LineSet()
LineSet1460.vertexCount = [2]
Coordinate1461 = x3d.Coordinate()
Coordinate1461.point = (-0.2028,0.7139,-0.0236,-0.1980,0.6883,-0.0180)

LineSet1460.coord = Coordinate1461
ColorRGBA1462 = x3d.ColorRGBA()
ColorRGBA1462.USE = "HAnimSiteLineColorRGBA"

LineSet1460.color = ColorRGBA1462

Shape1459.geometry = LineSet1460

HAnimSegment1455.children.append(Shape1459)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_index3'/> to <HAnimSite name='r_dactylion_pt'/>
Shape1463 = x3d.Shape()
LineSet1464 = x3d.LineSet()
LineSet1464.vertexCount = [2]
Coordinate1465 = x3d.Coordinate()
Coordinate1465.point = (-0.2028,0.7139,-0.0236,-0.1941,0.6772,-0.0423)

LineSet1464.coord = Coordinate1465
ColorRGBA1466 = x3d.ColorRGBA()
ColorRGBA1466.USE = "HAnimSiteLineColorRGBA"

LineSet1464.color = ColorRGBA1466

Shape1463.geometry = LineSet1464

HAnimSegment1455.children.append(Shape1463)
HAnimSite1467 = x3d.HAnimSite()
HAnimSite1467.name = "r_carpal_distal_phalanx_2_pt"
HAnimSite1467.DEF = "hanim_r_carpal_distal_phalanx_2_pt"
HAnimSite1467.translation = [-0.198,0.6883,-0.018]
#HAnimSite visualization shape
TouchSensor1468 = x3d.TouchSensor()
TouchSensor1468.description = "HAnimSite r_index_distal_tip"

HAnimSite1467.children.append(TouchSensor1468)
Shape1469 = x3d.Shape()
Shape1469.USE = "HAnimSiteShape"

HAnimSite1467.children.append(Shape1469)

HAnimSegment1455.children.append(HAnimSite1467)
HAnimSite1470 = x3d.HAnimSite()
HAnimSite1470.name = "r_dactylion_pt"
HAnimSite1470.DEF = "hanim_r_dactylion_pt"
HAnimSite1470.translation = [-0.1941,0.6772,-0.0423]
#HAnimSite visualization shape
TouchSensor1471 = x3d.TouchSensor()
TouchSensor1471.description = "HAnimSite r_dactylion_pt"

HAnimSite1470.children.append(TouchSensor1471)
Shape1472 = x3d.Shape()
Shape1472.USE = "HAnimSiteShape"

HAnimSite1470.children.append(Shape1472)

HAnimSegment1455.children.append(HAnimSite1470)

HAnimJoint1454.children.append(HAnimSegment1455)

HAnimJoint1445.children.append(HAnimJoint1454)

HAnimJoint1436.children.append(HAnimJoint1445)

HAnimJoint1427.children.append(HAnimJoint1436)

HAnimJoint1339.children.append(HAnimJoint1427)
HAnimJoint1473 = x3d.HAnimJoint()
HAnimJoint1473.name = "r_carpometacarpal_3"
HAnimJoint1473.DEF = "hanim_r_carpometacarpal_3"
HAnimJoint1473.center = [-0.1987,0.8029,-0.053]
HAnimJoint1473.ulimit = [0,0,0]
HAnimJoint1473.llimit = [0,0,0]
HAnimSegment1474 = x3d.HAnimSegment()
HAnimSegment1474.name = "r_metacarpal_3"
HAnimSegment1474.DEF = "hanim_r_metacarpal_3"
#Visualization sphere for <HAnimJoint name='r_middle0'/> is placed within <HAnimSegment name='r_metacarpal_3'/>
TouchSensor1475 = x3d.TouchSensor()
TouchSensor1475.description = "HAnimJoint r_middle0, HAnimSegment r_metacarpal_3"

HAnimSegment1474.children.append(TouchSensor1475)
Transform1476 = x3d.Transform()
Transform1476.translation = [-0.1987,0.8029,-0.053]
Shape1477 = x3d.Shape()
Shape1477.USE = "HAnimJointShape"

Transform1476.children.append(Shape1477)

HAnimSegment1474.children.append(Transform1476)
#HAnimSegment visualization line from current <HAnimJoint name='r_middle0'/> to child <HAnimJoint name='r_middle1'/>
Shape1478 = x3d.Shape()
LineSet1479 = x3d.LineSet()
LineSet1479.vertexCount = [2]
Coordinate1480 = x3d.Coordinate()
Coordinate1480.point = (-0.1987,0.8029,-0.0530,-0.1987,0.7818,-0.0530)

LineSet1479.coord = Coordinate1480
ColorRGBA1481 = x3d.ColorRGBA()
ColorRGBA1481.USE = "HAnimSegmentLineColorRGBA"

LineSet1479.color = ColorRGBA1481

Shape1478.geometry = LineSet1479

HAnimSegment1474.children.append(Shape1478)

HAnimJoint1473.children.append(HAnimSegment1474)
HAnimJoint1482 = x3d.HAnimJoint()
HAnimJoint1482.name = "r_metacarpophalangeal_3"
HAnimJoint1482.DEF = "hanim_r_metacarpophalangeal_3"
HAnimJoint1482.center = [-0.1987,0.7818,-0.053]
HAnimJoint1482.ulimit = [0,0,0]
HAnimJoint1482.llimit = [0,0,0]
HAnimSegment1483 = x3d.HAnimSegment()
HAnimSegment1483.name = "r_carpal_proximal_phalanx_3"
HAnimSegment1483.DEF = "hanim_r_carpal_proximal_phalanx_3"
#Visualization sphere for <HAnimJoint name='r_middle1'/> is placed within <HAnimSegment name='r_carpal_proximal_phalanx_3'/>
TouchSensor1484 = x3d.TouchSensor()
TouchSensor1484.description = "HAnimJoint r_middle1, HAnimSegment r_carpal_proximal_phalanx_3"

HAnimSegment1483.children.append(TouchSensor1484)
Transform1485 = x3d.Transform()
Transform1485.translation = [-0.1987,0.7818,-0.053]
Shape1486 = x3d.Shape()
Shape1486.USE = "HAnimJointShape"

Transform1485.children.append(Shape1486)

HAnimSegment1483.children.append(Transform1485)
#HAnimSegment visualization line from current <HAnimJoint name='r_middle1'/> to child <HAnimJoint name='r_middle2'/>
Shape1487 = x3d.Shape()
LineSet1488 = x3d.LineSet()
LineSet1488.vertexCount = [2]
Coordinate1489 = x3d.Coordinate()
Coordinate1489.point = (-0.1987,0.7818,-0.0530,-0.2013,0.7273,-0.0503)

LineSet1488.coord = Coordinate1489
ColorRGBA1490 = x3d.ColorRGBA()
ColorRGBA1490.USE = "HAnimSegmentLineColorRGBA"

LineSet1488.color = ColorRGBA1490

Shape1487.geometry = LineSet1488

HAnimSegment1483.children.append(Shape1487)

HAnimJoint1482.children.append(HAnimSegment1483)
HAnimJoint1491 = x3d.HAnimJoint()
HAnimJoint1491.name = "r_carpal_proximal_interphalangeal_3"
HAnimJoint1491.DEF = "hanim_r_carpal_proximal_interphalangeal_3"
HAnimJoint1491.center = [-0.2013,0.7273,-0.0503]
HAnimJoint1491.ulimit = [0,0,0]
HAnimJoint1491.llimit = [0,0,0]
HAnimSegment1492 = x3d.HAnimSegment()
HAnimSegment1492.name = "r_carpal_middle_phalanx_3"
HAnimSegment1492.DEF = "hanim_r_carpal_middle_phalanx_3"
#Visualization sphere for <HAnimJoint name='r_middle2'/> is placed within <HAnimSegment name='r_carpal_middle_phalanx_3'/>
TouchSensor1493 = x3d.TouchSensor()
TouchSensor1493.description = "HAnimJoint r_middle2, HAnimSegment r_carpal_middle_phalanx_3"

HAnimSegment1492.children.append(TouchSensor1493)
Transform1494 = x3d.Transform()
Transform1494.translation = [-0.2013,0.7273,-0.0503]
Shape1495 = x3d.Shape()
Shape1495.USE = "HAnimJointShape"

Transform1494.children.append(Shape1495)

HAnimSegment1492.children.append(Transform1494)
#HAnimSegment visualization line from current <HAnimJoint name='r_middle2'/> to child <HAnimJoint name='r_middle3'/>
Shape1496 = x3d.Shape()
LineSet1497 = x3d.LineSet()
LineSet1497.vertexCount = [2]
Coordinate1498 = x3d.Coordinate()
Coordinate1498.point = (-0.2013,0.7273,-0.0503,-0.2026,0.7011,-0.0494)

LineSet1497.coord = Coordinate1498
ColorRGBA1499 = x3d.ColorRGBA()
ColorRGBA1499.USE = "HAnimSegmentLineColorRGBA"

LineSet1497.color = ColorRGBA1499

Shape1496.geometry = LineSet1497

HAnimSegment1492.children.append(Shape1496)

HAnimJoint1491.children.append(HAnimSegment1492)
HAnimJoint1500 = x3d.HAnimJoint()
HAnimJoint1500.name = "r_carpal_distal_interphalangeal_3"
HAnimJoint1500.DEF = "hanim_r_carpal_distal_interphalangeal_3"
HAnimJoint1500.center = [-0.2026,0.7011,-0.0494]
HAnimJoint1500.ulimit = [0,0,0]
HAnimJoint1500.llimit = [0,0,0]
HAnimSegment1501 = x3d.HAnimSegment()
HAnimSegment1501.name = "r_carpal_distal_phalanx_3"
HAnimSegment1501.DEF = "hanim_r_carpal_distal_phalanx_3"
#Visualization sphere for <HAnimJoint name='r_middle3'/> is placed within <HAnimSegment name='r_carpal_distal_phalanx_3'/>
TouchSensor1502 = x3d.TouchSensor()
TouchSensor1502.description = "HAnimJoint r_middle3, HAnimSegment r_carpal_distal_phalanx_3"

HAnimSegment1501.children.append(TouchSensor1502)
Transform1503 = x3d.Transform()
Transform1503.translation = [-0.2026,0.7011,-0.0494]
Shape1504 = x3d.Shape()
Shape1504.USE = "HAnimJointShape"

Transform1503.children.append(Shape1504)

HAnimSegment1501.children.append(Transform1503)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_middle3'/> to <HAnimSite name='r_middle_distal_tip'/>
Shape1505 = x3d.Shape()
LineSet1506 = x3d.LineSet()
LineSet1506.vertexCount = [2]
Coordinate1507 = x3d.Coordinate()
Coordinate1507.point = (-0.2026,0.7011,-0.0494,-0.1969,0.6758,-0.0427)

LineSet1506.coord = Coordinate1507
ColorRGBA1508 = x3d.ColorRGBA()
ColorRGBA1508.USE = "HAnimSiteLineColorRGBA"

LineSet1506.color = ColorRGBA1508

Shape1505.geometry = LineSet1506

HAnimSegment1501.children.append(Shape1505)
HAnimSite1509 = x3d.HAnimSite()
HAnimSite1509.name = "r_carpal_distal_phalanx_3_pt"
HAnimSite1509.DEF = "hanim_r_carpal_distal_phalanx_3_pt"
HAnimSite1509.translation = [-0.1969,0.6758,-0.0427]
#HAnimSite visualization shape
TouchSensor1510 = x3d.TouchSensor()
TouchSensor1510.description = "HAnimSite r_middle_distal_tip"

HAnimSite1509.children.append(TouchSensor1510)
Shape1511 = x3d.Shape()
Shape1511.USE = "HAnimSiteShape"

HAnimSite1509.children.append(Shape1511)

HAnimSegment1501.children.append(HAnimSite1509)

HAnimJoint1500.children.append(HAnimSegment1501)

HAnimJoint1491.children.append(HAnimJoint1500)

HAnimJoint1482.children.append(HAnimJoint1491)

HAnimJoint1473.children.append(HAnimJoint1482)

HAnimJoint1339.children.append(HAnimJoint1473)
HAnimJoint1512 = x3d.HAnimJoint()
HAnimJoint1512.name = "r_carpometacarpal_4"
HAnimJoint1512.DEF = "hanim_r_carpometacarpal_4"
HAnimJoint1512.center = [-0.1956,0.8019,-0.0794]
HAnimJoint1512.ulimit = [0,0,0]
HAnimJoint1512.llimit = [0,0,0]
HAnimSegment1513 = x3d.HAnimSegment()
HAnimSegment1513.name = "r_metacarpal_4"
HAnimSegment1513.DEF = "hanim_r_metacarpal_4"
#Visualization sphere for <HAnimJoint name='r_ring0'/> is placed within <HAnimSegment name='r_metacarpal_4'/>
TouchSensor1514 = x3d.TouchSensor()
TouchSensor1514.description = "HAnimJoint r_ring0, HAnimSegment r_metacarpal_4"

HAnimSegment1513.children.append(TouchSensor1514)
Transform1515 = x3d.Transform()
Transform1515.translation = [-0.1956,0.8019,-0.0794]
Shape1516 = x3d.Shape()
Shape1516.USE = "HAnimJointShape"

Transform1515.children.append(Shape1516)

HAnimSegment1513.children.append(Transform1515)
#HAnimSegment visualization line from current <HAnimJoint name='r_ring0'/> to child <HAnimJoint name='r_ring1'/>
Shape1517 = x3d.Shape()
LineSet1518 = x3d.LineSet()
LineSet1518.vertexCount = [2]
Coordinate1519 = x3d.Coordinate()
Coordinate1519.point = (-0.1956,0.8019,-0.0794,-0.1956,0.7815,-0.0794)

LineSet1518.coord = Coordinate1519
ColorRGBA1520 = x3d.ColorRGBA()
ColorRGBA1520.USE = "HAnimSegmentLineColorRGBA"

LineSet1518.color = ColorRGBA1520

Shape1517.geometry = LineSet1518

HAnimSegment1513.children.append(Shape1517)

HAnimJoint1512.children.append(HAnimSegment1513)
HAnimJoint1521 = x3d.HAnimJoint()
HAnimJoint1521.name = "r_metacarpophalangeal_4"
HAnimJoint1521.DEF = "hanim_r_metacarpophalangeal_4"
HAnimJoint1521.center = [-0.1956,0.7815,-0.0794]
HAnimJoint1521.ulimit = [0,0,0]
HAnimJoint1521.llimit = [0,0,0]
HAnimSegment1522 = x3d.HAnimSegment()
HAnimSegment1522.name = "r_carpal_proximal_phalanx_4"
HAnimSegment1522.DEF = "hanim_r_carpal_proximal_phalanx_4"
#Visualization sphere for <HAnimJoint name='r_ring1'/> is placed within <HAnimSegment name='r_carpal_proximal_phalanx_4'/>
TouchSensor1523 = x3d.TouchSensor()
TouchSensor1523.description = "HAnimJoint r_ring1, HAnimSegment r_carpal_proximal_phalanx_4"

HAnimSegment1522.children.append(TouchSensor1523)
Transform1524 = x3d.Transform()
Transform1524.translation = [-0.1956,0.7815,-0.0794]
Shape1525 = x3d.Shape()
Shape1525.USE = "HAnimJointShape"

Transform1524.children.append(Shape1525)

HAnimSegment1522.children.append(Transform1524)
#HAnimSegment visualization line from current <HAnimJoint name='r_ring1'/> to child <HAnimJoint name='r_ring2'/>
Shape1526 = x3d.Shape()
LineSet1527 = x3d.LineSet()
LineSet1527.vertexCount = [2]
Coordinate1528 = x3d.Coordinate()
Coordinate1528.point = (-0.1956,0.7815,-0.0794,-0.1973,0.7287,-0.0777)

LineSet1527.coord = Coordinate1528
ColorRGBA1529 = x3d.ColorRGBA()
ColorRGBA1529.USE = "HAnimSegmentLineColorRGBA"

LineSet1527.color = ColorRGBA1529

Shape1526.geometry = LineSet1527

HAnimSegment1522.children.append(Shape1526)

HAnimJoint1521.children.append(HAnimSegment1522)
HAnimJoint1530 = x3d.HAnimJoint()
HAnimJoint1530.name = "r_carpal_proximal_interphalangeal_4"
HAnimJoint1530.DEF = "hanim_r_carpal_proximal_interphalangeal_4"
HAnimJoint1530.center = [-0.1973,0.7287,-0.0777]
HAnimJoint1530.ulimit = [0,0,0]
HAnimJoint1530.llimit = [0,0,0]
HAnimSegment1531 = x3d.HAnimSegment()
HAnimSegment1531.name = "r_carpal_middle_phalanx_4"
HAnimSegment1531.DEF = "hanim_r_carpal_middle_phalanx_4"
#Visualization sphere for <HAnimJoint name='r_ring2'/> is placed within <HAnimSegment name='r_carpal_middle_phalanx_4'/>
TouchSensor1532 = x3d.TouchSensor()
TouchSensor1532.description = "HAnimJoint r_ring2, HAnimSegment r_carpal_middle_phalanx_4"

HAnimSegment1531.children.append(TouchSensor1532)
Transform1533 = x3d.Transform()
Transform1533.translation = [-0.1973,0.7287,-0.0777]
Shape1534 = x3d.Shape()
Shape1534.USE = "HAnimJointShape"

Transform1533.children.append(Shape1534)

HAnimSegment1531.children.append(Transform1533)
#HAnimSegment visualization line from current <HAnimJoint name='r_ring2'/> to child <HAnimJoint name='r_ring3'/>
Shape1535 = x3d.Shape()
LineSet1536 = x3d.LineSet()
LineSet1536.vertexCount = [2]
Coordinate1537 = x3d.Coordinate()
Coordinate1537.point = (-0.1973,0.7287,-0.0777,-0.1983,0.7045,-0.0767)

LineSet1536.coord = Coordinate1537
ColorRGBA1538 = x3d.ColorRGBA()
ColorRGBA1538.USE = "HAnimSegmentLineColorRGBA"

LineSet1536.color = ColorRGBA1538

Shape1535.geometry = LineSet1536

HAnimSegment1531.children.append(Shape1535)

HAnimJoint1530.children.append(HAnimSegment1531)
HAnimJoint1539 = x3d.HAnimJoint()
HAnimJoint1539.name = "r_carpal_distal_interphalangeal_4"
HAnimJoint1539.DEF = "hanim_r_carpal_distal_interphalangeal_4"
HAnimJoint1539.center = [-0.1983,0.7045,-0.0767]
HAnimJoint1539.ulimit = [0,0,0]
HAnimJoint1539.llimit = [0,0,0]
HAnimSegment1540 = x3d.HAnimSegment()
HAnimSegment1540.name = "r_carpal_distal_phalanx_4"
HAnimSegment1540.DEF = "hanim_r_carpal_distal_phalanx_4"
#Visualization sphere for <HAnimJoint name='r_ring3'/> is placed within <HAnimSegment name='r_carpal_distal_phalanx_4'/>
TouchSensor1541 = x3d.TouchSensor()
TouchSensor1541.description = "HAnimJoint r_ring3, HAnimSegment r_carpal_distal_phalanx_4"

HAnimSegment1540.children.append(TouchSensor1541)
Transform1542 = x3d.Transform()
Transform1542.translation = [-0.1983,0.7045,-0.0767]
Shape1543 = x3d.Shape()
Shape1543.USE = "HAnimJointShape"

Transform1542.children.append(Shape1543)

HAnimSegment1540.children.append(Transform1542)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_ring3'/> to <HAnimSite name='r_ring_distal_tip'/>
Shape1544 = x3d.Shape()
LineSet1545 = x3d.LineSet()
LineSet1545.vertexCount = [2]
Coordinate1546 = x3d.Coordinate()
Coordinate1546.point = (-0.1983,0.7045,-0.0767,-0.1934,0.6778,-0.0693)

LineSet1545.coord = Coordinate1546
ColorRGBA1547 = x3d.ColorRGBA()
ColorRGBA1547.USE = "HAnimSiteLineColorRGBA"

LineSet1545.color = ColorRGBA1547

Shape1544.geometry = LineSet1545

HAnimSegment1540.children.append(Shape1544)
HAnimSite1548 = x3d.HAnimSite()
HAnimSite1548.name = "r_carpal_distal_phalanx_4_pt"
HAnimSite1548.DEF = "hanim_r_carpal_distal_phalanx_4_pt"
HAnimSite1548.translation = [-0.1934,0.6778,-0.0693]
#HAnimSite visualization shape
TouchSensor1549 = x3d.TouchSensor()
TouchSensor1549.description = "HAnimSite r_ring_distal_tip"

HAnimSite1548.children.append(TouchSensor1549)
Shape1550 = x3d.Shape()
Shape1550.USE = "HAnimSiteShape"

HAnimSite1548.children.append(Shape1550)

HAnimSegment1540.children.append(HAnimSite1548)

HAnimJoint1539.children.append(HAnimSegment1540)

HAnimJoint1530.children.append(HAnimJoint1539)

HAnimJoint1521.children.append(HAnimJoint1530)

HAnimJoint1512.children.append(HAnimJoint1521)

HAnimJoint1339.children.append(HAnimJoint1512)
HAnimJoint1551 = x3d.HAnimJoint()
HAnimJoint1551.name = "r_carpometacarpal_5"
HAnimJoint1551.DEF = "hanim_r_carpometacarpal_5"
HAnimJoint1551.center = [-0.1925,0.8066,-0.1036]
HAnimJoint1551.ulimit = [0,0,0]
HAnimJoint1551.llimit = [0,0,0]
HAnimSegment1552 = x3d.HAnimSegment()
HAnimSegment1552.name = "r_metacarpal_5"
HAnimSegment1552.DEF = "hanim_r_metacarpal_5"
#Visualization sphere for <HAnimJoint name='r_pinky0'/> is placed within <HAnimSegment name='r_metacarpal_5'/>
TouchSensor1553 = x3d.TouchSensor()
TouchSensor1553.description = "HAnimJoint r_pinky0, HAnimSegment r_metacarpal_5"

HAnimSegment1552.children.append(TouchSensor1553)
Transform1554 = x3d.Transform()
Transform1554.translation = [-0.1925,0.8066,-0.1036]
Shape1555 = x3d.Shape()
Shape1555.USE = "HAnimJointShape"

Transform1554.children.append(Shape1555)

HAnimSegment1552.children.append(Transform1554)
#HAnimSegment visualization line from current <HAnimJoint name='r_pinky0'/> to child <HAnimJoint name='r_pinky1'/>
Shape1556 = x3d.Shape()
LineSet1557 = x3d.LineSet()
LineSet1557.vertexCount = [2]
Coordinate1558 = x3d.Coordinate()
Coordinate1558.point = (-0.1925,0.8066,-0.1036,-0.1925,0.7866,-0.1036)

LineSet1557.coord = Coordinate1558
ColorRGBA1559 = x3d.ColorRGBA()
ColorRGBA1559.USE = "HAnimSegmentLineColorRGBA"

LineSet1557.color = ColorRGBA1559

Shape1556.geometry = LineSet1557

HAnimSegment1552.children.append(Shape1556)

HAnimJoint1551.children.append(HAnimSegment1552)
HAnimJoint1560 = x3d.HAnimJoint()
HAnimJoint1560.name = "r_metacarpophalangeal_5"
HAnimJoint1560.DEF = "hanim_r_metacarpophalangeal_5"
HAnimJoint1560.center = [-0.1925,0.7866,-0.1036]
HAnimJoint1560.ulimit = [0,0,0]
HAnimJoint1560.llimit = [0,0,0]
HAnimSegment1561 = x3d.HAnimSegment()
HAnimSegment1561.name = "r_carpal_proximal_phalanx_5"
HAnimSegment1561.DEF = "hanim_r_carpal_proximal_phalanx_5"
#Visualization sphere for <HAnimJoint name='r_pinky1'/> is placed within <HAnimSegment name='r_carpal_proximal_phalanx_5'/>
TouchSensor1562 = x3d.TouchSensor()
TouchSensor1562.description = "HAnimJoint r_pinky1, HAnimSegment r_carpal_proximal_phalanx_5"

HAnimSegment1561.children.append(TouchSensor1562)
Transform1563 = x3d.Transform()
Transform1563.translation = [-0.1925,0.7866,-0.1036]
Shape1564 = x3d.Shape()
Shape1564.USE = "HAnimJointShape"

Transform1563.children.append(Shape1564)

HAnimSegment1561.children.append(Transform1563)
#HAnimSegment visualization line from current <HAnimJoint name='r_pinky1'/> to child <HAnimJoint name='r_pinky2'/>
Shape1565 = x3d.Shape()
LineSet1566 = x3d.LineSet()
LineSet1566.vertexCount = [2]
Coordinate1567 = x3d.Coordinate()
Coordinate1567.point = (-0.1925,0.7866,-0.1036,-0.1938,0.7452,-0.1024)

LineSet1566.coord = Coordinate1567
ColorRGBA1568 = x3d.ColorRGBA()
ColorRGBA1568.USE = "HAnimSegmentLineColorRGBA"

LineSet1566.color = ColorRGBA1568

Shape1565.geometry = LineSet1566

HAnimSegment1561.children.append(Shape1565)

HAnimJoint1560.children.append(HAnimSegment1561)
HAnimJoint1569 = x3d.HAnimJoint()
HAnimJoint1569.name = "r_carpal_proximal_interphalangeal_5"
HAnimJoint1569.DEF = "hanim_r_carpal_proximal_interphalangeal_5"
HAnimJoint1569.center = [-0.1938,0.7452,-0.1024]
HAnimJoint1569.ulimit = [0,0,0]
HAnimJoint1569.llimit = [0,0,0]
HAnimSegment1570 = x3d.HAnimSegment()
HAnimSegment1570.name = "r_carpal_middle_phalanx_5"
HAnimSegment1570.DEF = "hanim_r_carpal_middle_phalanx_5"
#Visualization sphere for <HAnimJoint name='r_pinky2'/> is placed within <HAnimSegment name='r_carpal_middle_phalanx_5'/>
TouchSensor1571 = x3d.TouchSensor()
TouchSensor1571.description = "HAnimJoint r_pinky2, HAnimSegment r_carpal_middle_phalanx_5"

HAnimSegment1570.children.append(TouchSensor1571)
Transform1572 = x3d.Transform()
Transform1572.translation = [-0.1938,0.7452,-0.1024]
Shape1573 = x3d.Shape()
Shape1573.USE = "HAnimJointShape"

Transform1572.children.append(Shape1573)

HAnimSegment1570.children.append(Transform1572)
#HAnimSegment visualization line from current <HAnimJoint name='r_pinky2'/> to child <HAnimJoint name='r_pinky3'/>
Shape1574 = x3d.Shape()
LineSet1575 = x3d.LineSet()
LineSet1575.vertexCount = [2]
Coordinate1576 = x3d.Coordinate()
Coordinate1576.point = (-0.1938,0.7452,-0.1024,-0.1948,0.7277,-0.1017)

LineSet1575.coord = Coordinate1576
ColorRGBA1577 = x3d.ColorRGBA()
ColorRGBA1577.USE = "HAnimSegmentLineColorRGBA"

LineSet1575.color = ColorRGBA1577

Shape1574.geometry = LineSet1575

HAnimSegment1570.children.append(Shape1574)

HAnimJoint1569.children.append(HAnimSegment1570)
HAnimJoint1578 = x3d.HAnimJoint()
HAnimJoint1578.name = "r_carpal_distal_interphalangeal_5"
HAnimJoint1578.DEF = "hanim_r_carpal_distal_interphalangeal_5"
HAnimJoint1578.center = [-0.1948,0.7277,-0.1017]
HAnimJoint1578.ulimit = [0,0,0]
HAnimJoint1578.llimit = [0,0,0]
HAnimSegment1579 = x3d.HAnimSegment()
HAnimSegment1579.name = "r_carpal_distal_phalanx_5"
HAnimSegment1579.DEF = "hanim_r_carpal_distal_phalanx_5"
#Visualization sphere for <HAnimJoint name='r_pinky3'/> is placed within <HAnimSegment name='r_carpal_distal_phalanx_5'/>
TouchSensor1580 = x3d.TouchSensor()
TouchSensor1580.description = "HAnimJoint r_pinky3, HAnimSegment r_carpal_distal_phalanx_5"

HAnimSegment1579.children.append(TouchSensor1580)
Transform1581 = x3d.Transform()
Transform1581.translation = [-0.1948,0.7277,-0.1017]
Shape1582 = x3d.Shape()
Shape1582.USE = "HAnimJointShape"

Transform1581.children.append(Shape1582)

HAnimSegment1579.children.append(Transform1581)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_pinky3'/> to <HAnimSite name='r_pinky_distal_tip'/>
Shape1583 = x3d.Shape()
LineSet1584 = x3d.LineSet()
LineSet1584.vertexCount = [2]
Coordinate1585 = x3d.Coordinate()
Coordinate1585.point = (-0.1948,0.7277,-0.1017,-0.1938,0.7035,-0.0949)

LineSet1584.coord = Coordinate1585
ColorRGBA1586 = x3d.ColorRGBA()
ColorRGBA1586.USE = "HAnimSiteLineColorRGBA"

LineSet1584.color = ColorRGBA1586

Shape1583.geometry = LineSet1584

HAnimSegment1579.children.append(Shape1583)
HAnimSite1587 = x3d.HAnimSite()
HAnimSite1587.name = "r_carpal_distal_phalanx_5_pt"
HAnimSite1587.DEF = "hanim_r_carpal_distal_phalanx_5_pt"
HAnimSite1587.translation = [-0.1938,0.7035,-0.0949]
#HAnimSite visualization shape
TouchSensor1588 = x3d.TouchSensor()
TouchSensor1588.description = "HAnimSite r_pinky_distal_tip"

HAnimSite1587.children.append(TouchSensor1588)
Shape1589 = x3d.Shape()
Shape1589.USE = "HAnimSiteShape"

HAnimSite1587.children.append(Shape1589)

HAnimSegment1579.children.append(HAnimSite1587)

HAnimJoint1578.children.append(HAnimSegment1579)

HAnimJoint1569.children.append(HAnimJoint1578)

HAnimJoint1560.children.append(HAnimJoint1569)

HAnimJoint1551.children.append(HAnimJoint1560)

HAnimJoint1339.children.append(HAnimJoint1551)

HAnimJoint1302.children.append(HAnimJoint1339)

HAnimJoint1286.children.append(HAnimJoint1302)

HAnimJoint1277.children.append(HAnimJoint1286)

HAnimJoint1240.children.append(HAnimJoint1277)

HAnimJoint602.children.append(HAnimJoint1240)

HAnimJoint593.children.append(HAnimJoint602)

HAnimJoint584.children.append(HAnimJoint593)

HAnimJoint575.children.append(HAnimJoint584)

HAnimJoint566.children.append(HAnimJoint575)

HAnimJoint557.children.append(HAnimJoint566)

HAnimJoint548.children.append(HAnimJoint557)

HAnimJoint539.children.append(HAnimJoint548)

HAnimJoint516.children.append(HAnimJoint539)

HAnimJoint500.children.append(HAnimJoint516)

HAnimJoint491.children.append(HAnimJoint500)

HAnimJoint482.children.append(HAnimJoint491)

HAnimJoint473.children.append(HAnimJoint482)

HAnimJoint443.children.append(HAnimJoint473)

HAnimJoint434.children.append(HAnimJoint443)

HAnimJoint425.children.append(HAnimJoint434)

HAnimJoint402.children.append(HAnimJoint425)

HAnimJoint52.children.append(HAnimJoint402)

HAnimHumanoid43.skeleton.append(HAnimJoint52)
HAnimSite1590 = x3d.HAnimSite()
HAnimSite1590.name = "l_inclined_view"
HAnimSite1590.DEF = "hanim_l_inclined_view"
HAnimSite1590.rotation = [-0.113,0.993,0.0347,0.671]
HAnimSite1590.translation = [1.62,1.05,2.06]
#HAnimSite visualization shape
TouchSensor1591 = x3d.TouchSensor()
TouchSensor1591.description = "HAnimSite l_inclined_view"

HAnimSite1590.children.append(TouchSensor1591)
Shape1592 = x3d.Shape()
Shape1592.USE = "HAnimSiteShape"

HAnimSite1590.children.append(Shape1592)
Viewpoint1593 = x3d.Viewpoint()
Viewpoint1593.DEF = "hanim_l_inclined_viewpoint"
Viewpoint1593.description = "left inclined"
Viewpoint1593.position = [0,0,0]

HAnimSite1590.children.append(Viewpoint1593)
#HAnimSite/Viewpoint visualization shape
Anchor1594 = x3d.Anchor()
Anchor1594.description = "HAnimSite hanim_l_inclined_view Viewpoint"
Anchor1594.url = ["#hanim_l_inclined_viewpoint"]
LOD1595 = x3d.LOD()
LOD1595.forceTransitions = True
LOD1595.range = [0.04]
WorldInfo1596 = x3d.WorldInfo()
WorldInfo1596.info = ["hide diamond when close"]

LOD1595.children.append(WorldInfo1596)
Shape1597 = x3d.Shape()
Shape1597.USE = "HAnimSiteViewpointShape"

LOD1595.children.append(Shape1597)

Anchor1594.children.append(LOD1595)

HAnimSite1590.children.append(Anchor1594)

HAnimHumanoid43.viewpoints.append(HAnimSite1590)
HAnimSite1598 = x3d.HAnimSite()
HAnimSite1598.name = "r_inclined_view"
HAnimSite1598.DEF = "hanim_r_inclined_view"
HAnimSite1598.rotation = [-0.113,-0.993,0.0347,0.671]
HAnimSite1598.translation = [-1.62,1.05,2.06]
#HAnimSite visualization shape
TouchSensor1599 = x3d.TouchSensor()
TouchSensor1599.description = "HAnimSite r_inclined_view"

HAnimSite1598.children.append(TouchSensor1599)
Shape1600 = x3d.Shape()
Shape1600.USE = "HAnimSiteShape"

HAnimSite1598.children.append(Shape1600)
Viewpoint1601 = x3d.Viewpoint()
Viewpoint1601.DEF = "hanim_r_inclined_viewpoint"
Viewpoint1601.centerOfRotation = [0,0.9,0]
Viewpoint1601.description = "right inclined"
Viewpoint1601.position = [0,0,0]

HAnimSite1598.children.append(Viewpoint1601)
#HAnimSite/Viewpoint visualization shape
Anchor1602 = x3d.Anchor()
Anchor1602.description = "HAnimSite hanim_r_inclined_view Viewpoint"
Anchor1602.url = ["#hanim_r_inclined_viewpoint"]
LOD1603 = x3d.LOD()
LOD1603.forceTransitions = True
LOD1603.range = [0.04]
WorldInfo1604 = x3d.WorldInfo()
WorldInfo1604.info = ["hide diamond when close"]

LOD1603.children.append(WorldInfo1604)
Shape1605 = x3d.Shape()
Shape1605.USE = "HAnimSiteViewpointShape"

LOD1603.children.append(Shape1605)

Anchor1602.children.append(LOD1603)

HAnimSite1598.children.append(Anchor1602)

HAnimHumanoid43.viewpoints.append(HAnimSite1598)
HAnimSite1606 = x3d.HAnimSite()
HAnimSite1606.name = "front_view"
HAnimSite1606.DEF = "hanim_front_view"
HAnimSite1606.translation = [0,0.85,2.58]
#HAnimSite visualization shape
TouchSensor1607 = x3d.TouchSensor()
TouchSensor1607.description = "HAnimSite front_view"

HAnimSite1606.children.append(TouchSensor1607)
Shape1608 = x3d.Shape()
Shape1608.USE = "HAnimSiteShape"

HAnimSite1606.children.append(Shape1608)
Viewpoint1609 = x3d.Viewpoint()
Viewpoint1609.DEF = "hanim_front_viewpoint"
Viewpoint1609.centerOfRotation = [0,0.9,0]
Viewpoint1609.description = "front"
Viewpoint1609.position = [0,0,0]

HAnimSite1606.children.append(Viewpoint1609)
#HAnimSite/Viewpoint visualization shape
Anchor1610 = x3d.Anchor()
Anchor1610.description = "HAnimSite hanim_front_view Viewpoint"
Anchor1610.url = ["#hanim_front_viewpoint"]
LOD1611 = x3d.LOD()
LOD1611.forceTransitions = True
LOD1611.range = [0.04]
WorldInfo1612 = x3d.WorldInfo()
WorldInfo1612.info = ["hide diamond when close"]

LOD1611.children.append(WorldInfo1612)
Shape1613 = x3d.Shape()
Shape1613.USE = "HAnimSiteViewpointShape"

LOD1611.children.append(Shape1613)

Anchor1610.children.append(LOD1611)

HAnimSite1606.children.append(Anchor1610)

HAnimHumanoid43.viewpoints.append(HAnimSite1606)
HAnimSite1614 = x3d.HAnimSite()
HAnimSite1614.name = "back_view"
HAnimSite1614.DEF = "hanim_back_view"
HAnimSite1614.rotation = [0,1,0,3.14]
HAnimSite1614.translation = [0,0.85,-2.58]
#HAnimSite visualization shape
TouchSensor1615 = x3d.TouchSensor()
TouchSensor1615.description = "HAnimSite back_view"

HAnimSite1614.children.append(TouchSensor1615)
Shape1616 = x3d.Shape()
Shape1616.USE = "HAnimSiteShape"

HAnimSite1614.children.append(Shape1616)
Viewpoint1617 = x3d.Viewpoint()
Viewpoint1617.DEF = "hanim_back_viewpoint"
Viewpoint1617.centerOfRotation = [0,0.9,0]
Viewpoint1617.description = "back"
Viewpoint1617.position = [0,0,0]

HAnimSite1614.children.append(Viewpoint1617)
#HAnimSite/Viewpoint visualization shape
Anchor1618 = x3d.Anchor()
Anchor1618.description = "HAnimSite hanim_back_view Viewpoint"
Anchor1618.url = ["#hanim_back_viewpoint"]
LOD1619 = x3d.LOD()
LOD1619.forceTransitions = True
LOD1619.range = [0.04]
WorldInfo1620 = x3d.WorldInfo()
WorldInfo1620.info = ["hide diamond when close"]

LOD1619.children.append(WorldInfo1620)
Shape1621 = x3d.Shape()
Shape1621.USE = "HAnimSiteViewpointShape"

LOD1619.children.append(Shape1621)

Anchor1618.children.append(LOD1619)

HAnimSite1614.children.append(Anchor1618)

HAnimHumanoid43.viewpoints.append(HAnimSite1614)
HAnimSite1622 = x3d.HAnimSite()
HAnimSite1622.name = "l_side_view"
HAnimSite1622.DEF = "hanim_l_side_view"
HAnimSite1622.rotation = [0,1,0,1.5708]
HAnimSite1622.translation = [2.6,0.854,0]
#HAnimSite visualization shape
TouchSensor1623 = x3d.TouchSensor()
TouchSensor1623.description = "HAnimSite l_side_view"

HAnimSite1622.children.append(TouchSensor1623)
Shape1624 = x3d.Shape()
Shape1624.USE = "HAnimSiteShape"

HAnimSite1622.children.append(Shape1624)
Viewpoint1625 = x3d.Viewpoint()
Viewpoint1625.DEF = "hanim_l_side_viewpoint"
Viewpoint1625.centerOfRotation = [0,0.9,0]
Viewpoint1625.description = "left side"
Viewpoint1625.position = [0,0,0]

HAnimSite1622.children.append(Viewpoint1625)
#HAnimSite/Viewpoint visualization shape
Anchor1626 = x3d.Anchor()
Anchor1626.description = "HAnimSite hanim_l_side_view Viewpoint"
Anchor1626.url = ["#hanim_l_side_viewpoint"]
LOD1627 = x3d.LOD()
LOD1627.forceTransitions = True
LOD1627.range = [0.04]
WorldInfo1628 = x3d.WorldInfo()
WorldInfo1628.info = ["hide diamond when close"]

LOD1627.children.append(WorldInfo1628)
Shape1629 = x3d.Shape()
Shape1629.USE = "HAnimSiteViewpointShape"

LOD1627.children.append(Shape1629)

Anchor1626.children.append(LOD1627)

HAnimSite1622.children.append(Anchor1626)

HAnimHumanoid43.viewpoints.append(HAnimSite1622)
HAnimSite1630 = x3d.HAnimSite()
HAnimSite1630.name = "Top_view"
HAnimSite1630.DEF = "hanim_Top_view"
HAnimSite1630.rotation = [1,0,0,-1.57]
HAnimSite1630.translation = [0,3.5,0]
#HAnimSite visualization shape
TouchSensor1631 = x3d.TouchSensor()
TouchSensor1631.description = "HAnimSite Top_view"

HAnimSite1630.children.append(TouchSensor1631)
Shape1632 = x3d.Shape()
Shape1632.USE = "HAnimSiteShape"

HAnimSite1630.children.append(Shape1632)
Viewpoint1633 = x3d.Viewpoint()
Viewpoint1633.DEF = "hanim_Top_viewpoint"
Viewpoint1633.centerOfRotation = [0,0.9,0]
Viewpoint1633.description = "Top"
Viewpoint1633.position = [0,0,0]

HAnimSite1630.children.append(Viewpoint1633)
#HAnimSite/Viewpoint visualization shape
Anchor1634 = x3d.Anchor()
Anchor1634.description = "HAnimSite hanim_Top_view Viewpoint"
Anchor1634.url = ["#hanim_Top_viewpoint"]
LOD1635 = x3d.LOD()
LOD1635.forceTransitions = True
LOD1635.range = [0.04]
WorldInfo1636 = x3d.WorldInfo()
WorldInfo1636.info = ["hide diamond when close"]

LOD1635.children.append(WorldInfo1636)
Shape1637 = x3d.Shape()
Shape1637.USE = "HAnimSiteViewpointShape"

LOD1635.children.append(Shape1637)

Anchor1634.children.append(LOD1635)

HAnimSite1630.children.append(Anchor1634)

HAnimHumanoid43.viewpoints.append(HAnimSite1630)
HAnimSite1638 = x3d.HAnimSite()
HAnimSite1638.name = "front_close_view"
HAnimSite1638.DEF = "hanim_front_close_view"
HAnimSite1638.translation = [0,0.854,1.575]
#HAnimSite visualization shape
TouchSensor1639 = x3d.TouchSensor()
TouchSensor1639.description = "HAnimSite front_close_view"

HAnimSite1638.children.append(TouchSensor1639)
Shape1640 = x3d.Shape()
Shape1640.USE = "HAnimSiteShape"

HAnimSite1638.children.append(Shape1640)
Viewpoint1641 = x3d.Viewpoint()
Viewpoint1641.DEF = "hanim_front_close_viewpoint"
Viewpoint1641.centerOfRotation = [0,0,1.575]
Viewpoint1641.description = "front close"
Viewpoint1641.position = [0,0,0]

HAnimSite1638.children.append(Viewpoint1641)
#HAnimSite/Viewpoint visualization shape
Anchor1642 = x3d.Anchor()
Anchor1642.description = "HAnimSite hanim_front_close_view Viewpoint"
Anchor1642.url = ["#hanim_front_close_viewpoint"]
LOD1643 = x3d.LOD()
LOD1643.forceTransitions = True
LOD1643.range = [0.04]
WorldInfo1644 = x3d.WorldInfo()
WorldInfo1644.info = ["hide diamond when close"]

LOD1643.children.append(WorldInfo1644)
Shape1645 = x3d.Shape()
Shape1645.USE = "HAnimSiteViewpointShape"

LOD1643.children.append(Shape1645)

Anchor1642.children.append(LOD1643)

HAnimSite1638.children.append(Anchor1642)

HAnimHumanoid43.viewpoints.append(HAnimSite1638)
HAnimSite1646 = x3d.HAnimSite()
HAnimSite1646.name = "side_close_view"
HAnimSite1646.DEF = "hanim_side_close_view"
HAnimSite1646.rotation = [0,1,0,1.5708]
HAnimSite1646.translation = [1.56,0.854,0]
#HAnimSite visualization shape
TouchSensor1647 = x3d.TouchSensor()
TouchSensor1647.description = "HAnimSite side_close_view"

HAnimSite1646.children.append(TouchSensor1647)
Shape1648 = x3d.Shape()
Shape1648.USE = "HAnimSiteShape"

HAnimSite1646.children.append(Shape1648)
Viewpoint1649 = x3d.Viewpoint()
Viewpoint1649.DEF = "hanim_side_close_viewpoint"
Viewpoint1649.centerOfRotation = [1.6,0,0]
Viewpoint1649.description = "side close"
Viewpoint1649.position = [0,0,0]

HAnimSite1646.children.append(Viewpoint1649)
#HAnimSite/Viewpoint visualization shape
Anchor1650 = x3d.Anchor()
Anchor1650.description = "HAnimSite hanim_side_close_view Viewpoint"
Anchor1650.url = ["#hanim_side_close_viewpoint"]
LOD1651 = x3d.LOD()
LOD1651.forceTransitions = True
LOD1651.range = [0.04]
WorldInfo1652 = x3d.WorldInfo()
WorldInfo1652.info = ["hide diamond when close"]

LOD1651.children.append(WorldInfo1652)
Shape1653 = x3d.Shape()
Shape1653.USE = "HAnimSiteViewpointShape"

LOD1651.children.append(Shape1653)

Anchor1650.children.append(LOD1651)

HAnimSite1646.children.append(Anchor1650)

HAnimHumanoid43.viewpoints.append(HAnimSite1646)
HAnimSite1654 = x3d.HAnimSite()
HAnimSite1654.name = "head_front_close_view"
HAnimSite1654.DEF = "hanim_head_front_close_view"
HAnimSite1654.translation = [0,1.5,1]
#HAnimSite visualization shape
TouchSensor1655 = x3d.TouchSensor()
TouchSensor1655.description = "HAnimSite head_front_close_view"

HAnimSite1654.children.append(TouchSensor1655)
Shape1656 = x3d.Shape()
Shape1656.USE = "HAnimSiteShape"

HAnimSite1654.children.append(Shape1656)
Viewpoint1657 = x3d.Viewpoint()
Viewpoint1657.DEF = "hanim_head_front_close_viewpoint"
Viewpoint1657.centerOfRotation = [0,0,1]
Viewpoint1657.description = "head front close"
Viewpoint1657.position = [0,0,0]

HAnimSite1654.children.append(Viewpoint1657)
#HAnimSite/Viewpoint visualization shape
Anchor1658 = x3d.Anchor()
Anchor1658.description = "HAnimSite hanim_head_front_close_view Viewpoint"
Anchor1658.url = ["#hanim_head_front_close_viewpoint"]
LOD1659 = x3d.LOD()
LOD1659.forceTransitions = True
LOD1659.range = [0.04]
WorldInfo1660 = x3d.WorldInfo()
WorldInfo1660.info = ["hide diamond when close"]

LOD1659.children.append(WorldInfo1660)
Shape1661 = x3d.Shape()
Shape1661.USE = "HAnimSiteViewpointShape"

LOD1659.children.append(Shape1661)

Anchor1658.children.append(LOD1659)

HAnimSite1654.children.append(Anchor1658)

HAnimHumanoid43.viewpoints.append(HAnimSite1654)
HAnimSite1662 = x3d.HAnimSite()
HAnimSite1662.name = "chest_front_close_view"
HAnimSite1662.DEF = "hanim_chest_front_close_view"
HAnimSite1662.translation = [0,1.2,1]
#HAnimSite visualization shape
TouchSensor1663 = x3d.TouchSensor()
TouchSensor1663.description = "HAnimSite chest_front_close_view"

HAnimSite1662.children.append(TouchSensor1663)
Shape1664 = x3d.Shape()
Shape1664.USE = "HAnimSiteShape"

HAnimSite1662.children.append(Shape1664)
Viewpoint1665 = x3d.Viewpoint()
Viewpoint1665.DEF = "hanim_chest_front_close_viewpoint"
Viewpoint1665.centerOfRotation = [0,0,1]
Viewpoint1665.description = "chest front close"
Viewpoint1665.position = [0,0,0]

HAnimSite1662.children.append(Viewpoint1665)
#HAnimSite/Viewpoint visualization shape
Anchor1666 = x3d.Anchor()
Anchor1666.description = "HAnimSite hanim_chest_front_close_view Viewpoint"
Anchor1666.url = ["#hanim_chest_front_close_viewpoint"]
LOD1667 = x3d.LOD()
LOD1667.forceTransitions = True
LOD1667.range = [0.04]
WorldInfo1668 = x3d.WorldInfo()
WorldInfo1668.info = ["hide diamond when close"]

LOD1667.children.append(WorldInfo1668)
Shape1669 = x3d.Shape()
Shape1669.USE = "HAnimSiteViewpointShape"

LOD1667.children.append(Shape1669)

Anchor1666.children.append(LOD1667)

HAnimSite1662.children.append(Anchor1666)

HAnimHumanoid43.viewpoints.append(HAnimSite1662)
HAnimSite1670 = x3d.HAnimSite()
HAnimSite1670.name = "pelvis_front_close_view"
HAnimSite1670.DEF = "hanim_pelvis_front_close_view"
HAnimSite1670.translation = [0,0.8,1]
#HAnimSite visualization shape
TouchSensor1671 = x3d.TouchSensor()
TouchSensor1671.description = "HAnimSite pelvis_front_close_view"

HAnimSite1670.children.append(TouchSensor1671)
Shape1672 = x3d.Shape()
Shape1672.USE = "HAnimSiteShape"

HAnimSite1670.children.append(Shape1672)
Viewpoint1673 = x3d.Viewpoint()
Viewpoint1673.DEF = "hanim_pelvis_front_close_viewpoint"
Viewpoint1673.centerOfRotation = [0,0,1]
Viewpoint1673.description = "pelvis front close"
Viewpoint1673.position = [0,0,0]

HAnimSite1670.children.append(Viewpoint1673)
#HAnimSite/Viewpoint visualization shape
Anchor1674 = x3d.Anchor()
Anchor1674.description = "HAnimSite hanim_pelvis_front_close_view Viewpoint"
Anchor1674.url = ["#hanim_pelvis_front_close_viewpoint"]
LOD1675 = x3d.LOD()
LOD1675.forceTransitions = True
LOD1675.range = [0.04]
WorldInfo1676 = x3d.WorldInfo()
WorldInfo1676.info = ["hide diamond when close"]

LOD1675.children.append(WorldInfo1676)
Shape1677 = x3d.Shape()
Shape1677.USE = "HAnimSiteViewpointShape"

LOD1675.children.append(Shape1677)

Anchor1674.children.append(LOD1675)

HAnimSite1670.children.append(Anchor1674)

HAnimHumanoid43.viewpoints.append(HAnimSite1670)
HAnimSite1678 = x3d.HAnimSite()
HAnimSite1678.name = "knees_front_close_view"
HAnimSite1678.DEF = "hanim_knees_front_close_view"
HAnimSite1678.translation = [0,0.4,1]
#HAnimSite visualization shape
TouchSensor1679 = x3d.TouchSensor()
TouchSensor1679.description = "HAnimSite knees_front_close_view"

HAnimSite1678.children.append(TouchSensor1679)
Shape1680 = x3d.Shape()
Shape1680.USE = "HAnimSiteShape"

HAnimSite1678.children.append(Shape1680)
Viewpoint1681 = x3d.Viewpoint()
Viewpoint1681.DEF = "hanim_knees_front_close_viewpoint"
Viewpoint1681.centerOfRotation = [0,0.4,0]
Viewpoint1681.description = "knees front close"
Viewpoint1681.position = [0,0,0]

HAnimSite1678.children.append(Viewpoint1681)
#HAnimSite/Viewpoint visualization shape
Anchor1682 = x3d.Anchor()
Anchor1682.description = "HAnimSite hanim_knees_front_close_view Viewpoint"
Anchor1682.url = ["#hanim_knees_front_close_viewpoint"]
LOD1683 = x3d.LOD()
LOD1683.forceTransitions = True
LOD1683.range = [0.04]
WorldInfo1684 = x3d.WorldInfo()
WorldInfo1684.info = ["hide diamond when close"]

LOD1683.children.append(WorldInfo1684)
Shape1685 = x3d.Shape()
Shape1685.USE = "HAnimSiteViewpointShape"

LOD1683.children.append(Shape1685)

Anchor1682.children.append(LOD1683)

HAnimSite1678.children.append(Anchor1682)

HAnimHumanoid43.viewpoints.append(HAnimSite1678)
HAnimSite1686 = x3d.HAnimSite()
HAnimSite1686.name = "feet_front_close_view"
HAnimSite1686.DEF = "hanim_feet_front_close_view"
HAnimSite1686.translation = [0,0,1]
#HAnimSite visualization shape
TouchSensor1687 = x3d.TouchSensor()
TouchSensor1687.description = "HAnimSite feet_front_close_view"

HAnimSite1686.children.append(TouchSensor1687)
Shape1688 = x3d.Shape()
Shape1688.USE = "HAnimSiteShape"

HAnimSite1686.children.append(Shape1688)
Viewpoint1689 = x3d.Viewpoint()
Viewpoint1689.DEF = "hanim_feet_front_close_viewpoint"
Viewpoint1689.description = "feet front close"
Viewpoint1689.position = [0,0,0]

HAnimSite1686.children.append(Viewpoint1689)
#HAnimSite/Viewpoint visualization shape
Anchor1690 = x3d.Anchor()
Anchor1690.description = "HAnimSite hanim_feet_front_close_view Viewpoint"
Anchor1690.url = ["#hanim_feet_front_close_viewpoint"]
LOD1691 = x3d.LOD()
LOD1691.forceTransitions = True
LOD1691.range = [0.04]
WorldInfo1692 = x3d.WorldInfo()
WorldInfo1692.info = ["hide diamond when close"]

LOD1691.children.append(WorldInfo1692)
Shape1693 = x3d.Shape()
Shape1693.USE = "HAnimSiteViewpointShape"

LOD1691.children.append(Shape1693)

Anchor1690.children.append(LOD1691)

HAnimSite1686.children.append(Anchor1690)

HAnimHumanoid43.viewpoints.append(HAnimSite1686)
HAnimSite1694 = x3d.HAnimSite()
HAnimSite1694.name = "eye_level_view"
HAnimSite1694.DEF = "hanim_eye_level_view"
HAnimSite1694.translation = [0,1.6332,0.0502]
#HAnimSite visualization shape
TouchSensor1695 = x3d.TouchSensor()
TouchSensor1695.description = "HAnimSite eye_level_view"

HAnimSite1694.children.append(TouchSensor1695)
Shape1696 = x3d.Shape()
Shape1696.USE = "HAnimSiteShape"

HAnimSite1694.children.append(Shape1696)
Viewpoint1697 = x3d.Viewpoint()
Viewpoint1697.DEF = "hanim_eye_level_viewpoint"
Viewpoint1697.description = "eye level looking forward"
Viewpoint1697.orientation = [0,1,0,3.141593]
Viewpoint1697.position = [0,0,0]

HAnimSite1694.children.append(Viewpoint1697)
#HAnimSite/Viewpoint visualization shape
Anchor1698 = x3d.Anchor()
Anchor1698.description = "HAnimSite hanim_eye_level_view Viewpoint"
Anchor1698.url = ["#hanim_eye_level_viewpoint"]
LOD1699 = x3d.LOD()
LOD1699.forceTransitions = True
LOD1699.range = [0.04]
WorldInfo1700 = x3d.WorldInfo()
WorldInfo1700.info = ["hide diamond when close"]

LOD1699.children.append(WorldInfo1700)
Shape1701 = x3d.Shape()
Shape1701.USE = "HAnimSiteViewpointShape"

LOD1699.children.append(Shape1701)

Anchor1698.children.append(LOD1699)

HAnimSite1694.children.append(Anchor1698)

HAnimHumanoid43.viewpoints.append(HAnimSite1694)
HAnimSite1702 = x3d.HAnimSite()
HAnimSite1702.USE = "hanim_l_eyeball_site_view"

HAnimHumanoid43.sites.append(HAnimSite1702)
HAnimSite1703 = x3d.HAnimSite()
HAnimSite1703.USE = "hanim_r_eyeball_site_view"

HAnimHumanoid43.sites.append(HAnimSite1703)
HAnimSite1704 = x3d.HAnimSite()
HAnimSite1704.USE = "hanim_l_hand_front_view"

HAnimHumanoid43.sites.append(HAnimSite1704)
HAnimSite1705 = x3d.HAnimSite()
HAnimSite1705.USE = "hanim_r_hand_front_view"

HAnimHumanoid43.sites.append(HAnimSite1705)
HAnimJoint1706 = x3d.HAnimJoint()
HAnimJoint1706.USE = "hanim_humanoid_root"

HAnimHumanoid43.joints.append(HAnimJoint1706)
HAnimJoint1707 = x3d.HAnimJoint()
HAnimJoint1707.USE = "hanim_sacroiliac"

HAnimHumanoid43.joints.append(HAnimJoint1707)
HAnimJoint1708 = x3d.HAnimJoint()
HAnimJoint1708.USE = "hanim_vl5"

HAnimHumanoid43.joints.append(HAnimJoint1708)
HAnimJoint1709 = x3d.HAnimJoint()
HAnimJoint1709.USE = "hanim_vl4"

HAnimHumanoid43.joints.append(HAnimJoint1709)
HAnimJoint1710 = x3d.HAnimJoint()
HAnimJoint1710.USE = "hanim_vl3"

HAnimHumanoid43.joints.append(HAnimJoint1710)
HAnimJoint1711 = x3d.HAnimJoint()
HAnimJoint1711.USE = "hanim_vl2"

HAnimHumanoid43.joints.append(HAnimJoint1711)
HAnimJoint1712 = x3d.HAnimJoint()
HAnimJoint1712.USE = "hanim_vl1"

HAnimHumanoid43.joints.append(HAnimJoint1712)
HAnimJoint1713 = x3d.HAnimJoint()
HAnimJoint1713.USE = "hanim_vt12"

HAnimHumanoid43.joints.append(HAnimJoint1713)
HAnimJoint1714 = x3d.HAnimJoint()
HAnimJoint1714.USE = "hanim_vt11"

HAnimHumanoid43.joints.append(HAnimJoint1714)
HAnimJoint1715 = x3d.HAnimJoint()
HAnimJoint1715.USE = "hanim_vt10"

HAnimHumanoid43.joints.append(HAnimJoint1715)
HAnimJoint1716 = x3d.HAnimJoint()
HAnimJoint1716.USE = "hanim_vt9"

HAnimHumanoid43.joints.append(HAnimJoint1716)
HAnimJoint1717 = x3d.HAnimJoint()
HAnimJoint1717.USE = "hanim_vt8"

HAnimHumanoid43.joints.append(HAnimJoint1717)
HAnimJoint1718 = x3d.HAnimJoint()
HAnimJoint1718.USE = "hanim_vt7"

HAnimHumanoid43.joints.append(HAnimJoint1718)
HAnimJoint1719 = x3d.HAnimJoint()
HAnimJoint1719.USE = "hanim_vt6"

HAnimHumanoid43.joints.append(HAnimJoint1719)
HAnimJoint1720 = x3d.HAnimJoint()
HAnimJoint1720.USE = "hanim_vt5"

HAnimHumanoid43.joints.append(HAnimJoint1720)
HAnimJoint1721 = x3d.HAnimJoint()
HAnimJoint1721.USE = "hanim_vt4"

HAnimHumanoid43.joints.append(HAnimJoint1721)
HAnimJoint1722 = x3d.HAnimJoint()
HAnimJoint1722.USE = "hanim_vt3"

HAnimHumanoid43.joints.append(HAnimJoint1722)
HAnimJoint1723 = x3d.HAnimJoint()
HAnimJoint1723.USE = "hanim_vt2"

HAnimHumanoid43.joints.append(HAnimJoint1723)
HAnimJoint1724 = x3d.HAnimJoint()
HAnimJoint1724.USE = "hanim_vt1"

HAnimHumanoid43.joints.append(HAnimJoint1724)
HAnimJoint1725 = x3d.HAnimJoint()
HAnimJoint1725.USE = "hanim_vc7"

HAnimHumanoid43.joints.append(HAnimJoint1725)
HAnimJoint1726 = x3d.HAnimJoint()
HAnimJoint1726.USE = "hanim_vc6"

HAnimHumanoid43.joints.append(HAnimJoint1726)
HAnimJoint1727 = x3d.HAnimJoint()
HAnimJoint1727.USE = "hanim_vc5"

HAnimHumanoid43.joints.append(HAnimJoint1727)
HAnimJoint1728 = x3d.HAnimJoint()
HAnimJoint1728.USE = "hanim_vc4"

HAnimHumanoid43.joints.append(HAnimJoint1728)
HAnimJoint1729 = x3d.HAnimJoint()
HAnimJoint1729.USE = "hanim_vc3"

HAnimHumanoid43.joints.append(HAnimJoint1729)
HAnimJoint1730 = x3d.HAnimJoint()
HAnimJoint1730.USE = "hanim_vc2"

HAnimHumanoid43.joints.append(HAnimJoint1730)
HAnimJoint1731 = x3d.HAnimJoint()
HAnimJoint1731.USE = "hanim_vc1"

HAnimHumanoid43.joints.append(HAnimJoint1731)
HAnimJoint1732 = x3d.HAnimJoint()
HAnimJoint1732.USE = "hanim_skullbase"

HAnimHumanoid43.joints.append(HAnimJoint1732)
HAnimJoint1733 = x3d.HAnimJoint()
HAnimJoint1733.USE = "hanim_temporomandibular"

HAnimHumanoid43.joints.append(HAnimJoint1733)
HAnimJoint1734 = x3d.HAnimJoint()
HAnimJoint1734.USE = "hanim_l_acromioclavicular"

HAnimHumanoid43.joints.append(HAnimJoint1734)
HAnimJoint1735 = x3d.HAnimJoint()
HAnimJoint1735.USE = "hanim_r_acromioclavicular"

HAnimHumanoid43.joints.append(HAnimJoint1735)
HAnimJoint1736 = x3d.HAnimJoint()
HAnimJoint1736.USE = "hanim_l_carpal_distal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1736)
HAnimJoint1737 = x3d.HAnimJoint()
HAnimJoint1737.USE = "hanim_r_carpal_distal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1737)
HAnimJoint1738 = x3d.HAnimJoint()
HAnimJoint1738.USE = "hanim_l_carpal_distal_interphalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint1738)
HAnimJoint1739 = x3d.HAnimJoint()
HAnimJoint1739.USE = "hanim_r_carpal_distal_interphalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint1739)
HAnimJoint1740 = x3d.HAnimJoint()
HAnimJoint1740.USE = "hanim_l_carpal_distal_interphalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint1740)
HAnimJoint1741 = x3d.HAnimJoint()
HAnimJoint1741.USE = "hanim_r_carpal_distal_interphalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint1741)
HAnimJoint1742 = x3d.HAnimJoint()
HAnimJoint1742.USE = "hanim_l_carpal_distal_interphalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint1742)
HAnimJoint1743 = x3d.HAnimJoint()
HAnimJoint1743.USE = "hanim_r_carpal_distal_interphalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint1743)
HAnimJoint1744 = x3d.HAnimJoint()
HAnimJoint1744.USE = "hanim_l_carpal_interphalangeal_1"

HAnimHumanoid43.joints.append(HAnimJoint1744)
HAnimJoint1745 = x3d.HAnimJoint()
HAnimJoint1745.USE = "hanim_r_carpal_interphalangeal_1"

HAnimHumanoid43.joints.append(HAnimJoint1745)
HAnimJoint1746 = x3d.HAnimJoint()
HAnimJoint1746.USE = "hanim_l_carpal_proximal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1746)
HAnimJoint1747 = x3d.HAnimJoint()
HAnimJoint1747.USE = "hanim_r_carpal_proximal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1747)
HAnimJoint1748 = x3d.HAnimJoint()
HAnimJoint1748.USE = "hanim_l_carpal_proximal_interphalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint1748)
HAnimJoint1749 = x3d.HAnimJoint()
HAnimJoint1749.USE = "hanim_r_carpal_proximal_interphalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint1749)
HAnimJoint1750 = x3d.HAnimJoint()
HAnimJoint1750.USE = "hanim_l_carpal_proximal_interphalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint1750)
HAnimJoint1751 = x3d.HAnimJoint()
HAnimJoint1751.USE = "hanim_r_carpal_proximal_interphalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint1751)
HAnimJoint1752 = x3d.HAnimJoint()
HAnimJoint1752.USE = "hanim_l_carpal_proximal_interphalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint1752)
HAnimJoint1753 = x3d.HAnimJoint()
HAnimJoint1753.USE = "hanim_r_carpal_proximal_interphalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint1753)
HAnimJoint1754 = x3d.HAnimJoint()
HAnimJoint1754.USE = "hanim_l_carpometacarpal_1"

HAnimHumanoid43.joints.append(HAnimJoint1754)
HAnimJoint1755 = x3d.HAnimJoint()
HAnimJoint1755.USE = "hanim_r_carpometacarpal_1"

HAnimHumanoid43.joints.append(HAnimJoint1755)
HAnimJoint1756 = x3d.HAnimJoint()
HAnimJoint1756.USE = "hanim_l_carpometacarpal_2"

HAnimHumanoid43.joints.append(HAnimJoint1756)
HAnimJoint1757 = x3d.HAnimJoint()
HAnimJoint1757.USE = "hanim_r_carpometacarpal_2"

HAnimHumanoid43.joints.append(HAnimJoint1757)
HAnimJoint1758 = x3d.HAnimJoint()
HAnimJoint1758.USE = "hanim_l_carpometacarpal_3"

HAnimHumanoid43.joints.append(HAnimJoint1758)
HAnimJoint1759 = x3d.HAnimJoint()
HAnimJoint1759.USE = "hanim_r_carpometacarpal_3"

HAnimHumanoid43.joints.append(HAnimJoint1759)
HAnimJoint1760 = x3d.HAnimJoint()
HAnimJoint1760.USE = "hanim_l_carpometacarpal_4"

HAnimHumanoid43.joints.append(HAnimJoint1760)
HAnimJoint1761 = x3d.HAnimJoint()
HAnimJoint1761.USE = "hanim_r_carpometacarpal_4"

HAnimHumanoid43.joints.append(HAnimJoint1761)
HAnimJoint1762 = x3d.HAnimJoint()
HAnimJoint1762.USE = "hanim_l_carpometacarpal_5"

HAnimHumanoid43.joints.append(HAnimJoint1762)
HAnimJoint1763 = x3d.HAnimJoint()
HAnimJoint1763.USE = "hanim_r_carpometacarpal_5"

HAnimHumanoid43.joints.append(HAnimJoint1763)
HAnimJoint1764 = x3d.HAnimJoint()
HAnimJoint1764.USE = "hanim_l_elbow"

HAnimHumanoid43.joints.append(HAnimJoint1764)
HAnimJoint1765 = x3d.HAnimJoint()
HAnimJoint1765.USE = "hanim_r_elbow"

HAnimHumanoid43.joints.append(HAnimJoint1765)
HAnimJoint1766 = x3d.HAnimJoint()
HAnimJoint1766.USE = "hanim_l_eyeball_joint"

HAnimHumanoid43.joints.append(HAnimJoint1766)
HAnimJoint1767 = x3d.HAnimJoint()
HAnimJoint1767.USE = "hanim_r_eyeball_joint"

HAnimHumanoid43.joints.append(HAnimJoint1767)
HAnimJoint1768 = x3d.HAnimJoint()
HAnimJoint1768.USE = "hanim_l_eyebrow_joint"

HAnimHumanoid43.joints.append(HAnimJoint1768)
HAnimJoint1769 = x3d.HAnimJoint()
HAnimJoint1769.USE = "hanim_r_eyebrow_joint"

HAnimHumanoid43.joints.append(HAnimJoint1769)
HAnimJoint1770 = x3d.HAnimJoint()
HAnimJoint1770.USE = "hanim_l_eyelid_joint"

HAnimHumanoid43.joints.append(HAnimJoint1770)
HAnimJoint1771 = x3d.HAnimJoint()
HAnimJoint1771.USE = "hanim_r_eyelid_joint"

HAnimHumanoid43.joints.append(HAnimJoint1771)
HAnimJoint1772 = x3d.HAnimJoint()
HAnimJoint1772.USE = "hanim_l_hip"

HAnimHumanoid43.joints.append(HAnimJoint1772)
HAnimJoint1773 = x3d.HAnimJoint()
HAnimJoint1773.USE = "hanim_r_hip"

HAnimHumanoid43.joints.append(HAnimJoint1773)
HAnimJoint1774 = x3d.HAnimJoint()
HAnimJoint1774.USE = "hanim_l_knee"

HAnimHumanoid43.joints.append(HAnimJoint1774)
HAnimJoint1775 = x3d.HAnimJoint()
HAnimJoint1775.USE = "hanim_r_knee"

HAnimHumanoid43.joints.append(HAnimJoint1775)
HAnimJoint1776 = x3d.HAnimJoint()
HAnimJoint1776.USE = "hanim_l_metacarpophalangeal_1"

HAnimHumanoid43.joints.append(HAnimJoint1776)
HAnimJoint1777 = x3d.HAnimJoint()
HAnimJoint1777.USE = "hanim_r_metacarpophalangeal_1"

HAnimHumanoid43.joints.append(HAnimJoint1777)
HAnimJoint1778 = x3d.HAnimJoint()
HAnimJoint1778.USE = "hanim_l_metacarpophalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1778)
HAnimJoint1779 = x3d.HAnimJoint()
HAnimJoint1779.USE = "hanim_r_metacarpophalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1779)
HAnimJoint1780 = x3d.HAnimJoint()
HAnimJoint1780.USE = "hanim_l_metacarpophalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint1780)
HAnimJoint1781 = x3d.HAnimJoint()
HAnimJoint1781.USE = "hanim_r_metacarpophalangeal_3"

HAnimHumanoid43.joints.append(HAnimJoint1781)
HAnimJoint1782 = x3d.HAnimJoint()
HAnimJoint1782.USE = "hanim_l_metacarpophalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint1782)
HAnimJoint1783 = x3d.HAnimJoint()
HAnimJoint1783.USE = "hanim_r_metacarpophalangeal_4"

HAnimHumanoid43.joints.append(HAnimJoint1783)
HAnimJoint1784 = x3d.HAnimJoint()
HAnimJoint1784.USE = "hanim_l_metacarpophalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint1784)
HAnimJoint1785 = x3d.HAnimJoint()
HAnimJoint1785.USE = "hanim_r_metacarpophalangeal_5"

HAnimHumanoid43.joints.append(HAnimJoint1785)
HAnimJoint1786 = x3d.HAnimJoint()
HAnimJoint1786.USE = "hanim_l_metatarsophalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1786)
HAnimJoint1787 = x3d.HAnimJoint()
HAnimJoint1787.USE = "hanim_r_metatarsophalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1787)
HAnimJoint1788 = x3d.HAnimJoint()
HAnimJoint1788.USE = "hanim_l_radiocarpal"

HAnimHumanoid43.joints.append(HAnimJoint1788)
HAnimJoint1789 = x3d.HAnimJoint()
HAnimJoint1789.USE = "hanim_r_radiocarpal"

HAnimHumanoid43.joints.append(HAnimJoint1789)
HAnimJoint1790 = x3d.HAnimJoint()
HAnimJoint1790.USE = "hanim_l_shoulder"

HAnimHumanoid43.joints.append(HAnimJoint1790)
HAnimJoint1791 = x3d.HAnimJoint()
HAnimJoint1791.USE = "hanim_r_shoulder"

HAnimHumanoid43.joints.append(HAnimJoint1791)
HAnimJoint1792 = x3d.HAnimJoint()
HAnimJoint1792.USE = "hanim_l_sternoclavicular"

HAnimHumanoid43.joints.append(HAnimJoint1792)
HAnimJoint1793 = x3d.HAnimJoint()
HAnimJoint1793.USE = "hanim_r_sternoclavicular"

HAnimHumanoid43.joints.append(HAnimJoint1793)
HAnimJoint1794 = x3d.HAnimJoint()
HAnimJoint1794.USE = "hanim_l_talocrural"

HAnimHumanoid43.joints.append(HAnimJoint1794)
HAnimJoint1795 = x3d.HAnimJoint()
HAnimJoint1795.USE = "hanim_r_talocrural"

HAnimHumanoid43.joints.append(HAnimJoint1795)
HAnimJoint1796 = x3d.HAnimJoint()
HAnimJoint1796.USE = "hanim_l_tarsal_distal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1796)
HAnimJoint1797 = x3d.HAnimJoint()
HAnimJoint1797.USE = "hanim_r_tarsal_distal_interphalangeal_2"

HAnimHumanoid43.joints.append(HAnimJoint1797)
HAnimJoint1798 = x3d.HAnimJoint()
HAnimJoint1798.USE = "hanim_l_tarsometatarsal_2"

HAnimHumanoid43.joints.append(HAnimJoint1798)
HAnimJoint1799 = x3d.HAnimJoint()
HAnimJoint1799.USE = "hanim_r_tarsometatarsal_2"

HAnimHumanoid43.joints.append(HAnimJoint1799)
HAnimSegment1800 = x3d.HAnimSegment()
HAnimSegment1800.USE = "hanim_pelvis"

HAnimHumanoid43.segments.append(HAnimSegment1800)
HAnimSegment1801 = x3d.HAnimSegment()
HAnimSegment1801.USE = "hanim_skull"

HAnimHumanoid43.segments.append(HAnimSegment1801)
HAnimSegment1802 = x3d.HAnimSegment()
HAnimSegment1802.USE = "hanim_jaw"

HAnimHumanoid43.segments.append(HAnimSegment1802)
HAnimSegment1803 = x3d.HAnimSegment()
HAnimSegment1803.USE = "hanim_c1"

HAnimHumanoid43.segments.append(HAnimSegment1803)
HAnimSegment1804 = x3d.HAnimSegment()
HAnimSegment1804.USE = "hanim_c2"

HAnimHumanoid43.segments.append(HAnimSegment1804)
HAnimSegment1805 = x3d.HAnimSegment()
HAnimSegment1805.USE = "hanim_c3"

HAnimHumanoid43.segments.append(HAnimSegment1805)
HAnimSegment1806 = x3d.HAnimSegment()
HAnimSegment1806.USE = "hanim_c4"

HAnimHumanoid43.segments.append(HAnimSegment1806)
HAnimSegment1807 = x3d.HAnimSegment()
HAnimSegment1807.USE = "hanim_c5"

HAnimHumanoid43.segments.append(HAnimSegment1807)
HAnimSegment1808 = x3d.HAnimSegment()
HAnimSegment1808.USE = "hanim_c6"

HAnimHumanoid43.segments.append(HAnimSegment1808)
HAnimSegment1809 = x3d.HAnimSegment()
HAnimSegment1809.USE = "hanim_c7"

HAnimHumanoid43.segments.append(HAnimSegment1809)
HAnimSegment1810 = x3d.HAnimSegment()
HAnimSegment1810.USE = "hanim_t1"

HAnimHumanoid43.segments.append(HAnimSegment1810)
HAnimSegment1811 = x3d.HAnimSegment()
HAnimSegment1811.USE = "hanim_t2"

HAnimHumanoid43.segments.append(HAnimSegment1811)
HAnimSegment1812 = x3d.HAnimSegment()
HAnimSegment1812.USE = "hanim_t3"

HAnimHumanoid43.segments.append(HAnimSegment1812)
HAnimSegment1813 = x3d.HAnimSegment()
HAnimSegment1813.USE = "hanim_t4"

HAnimHumanoid43.segments.append(HAnimSegment1813)
HAnimSegment1814 = x3d.HAnimSegment()
HAnimSegment1814.USE = "hanim_t5"

HAnimHumanoid43.segments.append(HAnimSegment1814)
HAnimSegment1815 = x3d.HAnimSegment()
HAnimSegment1815.USE = "hanim_t6"

HAnimHumanoid43.segments.append(HAnimSegment1815)
HAnimSegment1816 = x3d.HAnimSegment()
HAnimSegment1816.USE = "hanim_t7"

HAnimHumanoid43.segments.append(HAnimSegment1816)
HAnimSegment1817 = x3d.HAnimSegment()
HAnimSegment1817.USE = "hanim_t8"

HAnimHumanoid43.segments.append(HAnimSegment1817)
HAnimSegment1818 = x3d.HAnimSegment()
HAnimSegment1818.USE = "hanim_t9"

HAnimHumanoid43.segments.append(HAnimSegment1818)
HAnimSegment1819 = x3d.HAnimSegment()
HAnimSegment1819.USE = "hanim_t10"

HAnimHumanoid43.segments.append(HAnimSegment1819)
HAnimSegment1820 = x3d.HAnimSegment()
HAnimSegment1820.USE = "hanim_t11"

HAnimHumanoid43.segments.append(HAnimSegment1820)
HAnimSegment1821 = x3d.HAnimSegment()
HAnimSegment1821.USE = "hanim_t12"

HAnimHumanoid43.segments.append(HAnimSegment1821)
HAnimSegment1822 = x3d.HAnimSegment()
HAnimSegment1822.USE = "hanim_l1"

HAnimHumanoid43.segments.append(HAnimSegment1822)
HAnimSegment1823 = x3d.HAnimSegment()
HAnimSegment1823.USE = "hanim_l2"

HAnimHumanoid43.segments.append(HAnimSegment1823)
HAnimSegment1824 = x3d.HAnimSegment()
HAnimSegment1824.USE = "hanim_l3"

HAnimHumanoid43.segments.append(HAnimSegment1824)
HAnimSegment1825 = x3d.HAnimSegment()
HAnimSegment1825.USE = "hanim_l4"

HAnimHumanoid43.segments.append(HAnimSegment1825)
HAnimSegment1826 = x3d.HAnimSegment()
HAnimSegment1826.USE = "hanim_l5"

HAnimHumanoid43.segments.append(HAnimSegment1826)
HAnimSegment1827 = x3d.HAnimSegment()
HAnimSegment1827.USE = "hanim_sacrum"

HAnimHumanoid43.segments.append(HAnimSegment1827)
HAnimSegment1828 = x3d.HAnimSegment()
HAnimSegment1828.USE = "hanim_l_calf"

HAnimHumanoid43.segments.append(HAnimSegment1828)
HAnimSegment1829 = x3d.HAnimSegment()
HAnimSegment1829.USE = "hanim_r_calf"

HAnimHumanoid43.segments.append(HAnimSegment1829)
HAnimSegment1830 = x3d.HAnimSegment()
HAnimSegment1830.USE = "hanim_l_carpal"

HAnimHumanoid43.segments.append(HAnimSegment1830)
HAnimSegment1831 = x3d.HAnimSegment()
HAnimSegment1831.USE = "hanim_r_carpal"

HAnimHumanoid43.segments.append(HAnimSegment1831)
HAnimSegment1832 = x3d.HAnimSegment()
HAnimSegment1832.USE = "hanim_l_carpal_distal_phalanx_1"

HAnimHumanoid43.segments.append(HAnimSegment1832)
HAnimSegment1833 = x3d.HAnimSegment()
HAnimSegment1833.USE = "hanim_r_carpal_distal_phalanx_1"

HAnimHumanoid43.segments.append(HAnimSegment1833)
HAnimSegment1834 = x3d.HAnimSegment()
HAnimSegment1834.USE = "hanim_l_carpal_distal_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment1834)
HAnimSegment1835 = x3d.HAnimSegment()
HAnimSegment1835.USE = "hanim_r_carpal_distal_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment1835)
HAnimSegment1836 = x3d.HAnimSegment()
HAnimSegment1836.USE = "hanim_l_carpal_distal_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment1836)
HAnimSegment1837 = x3d.HAnimSegment()
HAnimSegment1837.USE = "hanim_r_carpal_distal_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment1837)
HAnimSegment1838 = x3d.HAnimSegment()
HAnimSegment1838.USE = "hanim_l_carpal_distal_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment1838)
HAnimSegment1839 = x3d.HAnimSegment()
HAnimSegment1839.USE = "hanim_r_carpal_distal_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment1839)
HAnimSegment1840 = x3d.HAnimSegment()
HAnimSegment1840.USE = "hanim_l_carpal_distal_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment1840)
HAnimSegment1841 = x3d.HAnimSegment()
HAnimSegment1841.USE = "hanim_r_carpal_distal_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment1841)
HAnimSegment1842 = x3d.HAnimSegment()
HAnimSegment1842.USE = "hanim_l_carpal_middle_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment1842)
HAnimSegment1843 = x3d.HAnimSegment()
HAnimSegment1843.USE = "hanim_r_carpal_middle_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment1843)
HAnimSegment1844 = x3d.HAnimSegment()
HAnimSegment1844.USE = "hanim_l_carpal_middle_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment1844)
HAnimSegment1845 = x3d.HAnimSegment()
HAnimSegment1845.USE = "hanim_r_carpal_middle_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment1845)
HAnimSegment1846 = x3d.HAnimSegment()
HAnimSegment1846.USE = "hanim_l_carpal_middle_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment1846)
HAnimSegment1847 = x3d.HAnimSegment()
HAnimSegment1847.USE = "hanim_r_carpal_middle_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment1847)
HAnimSegment1848 = x3d.HAnimSegment()
HAnimSegment1848.USE = "hanim_l_carpal_middle_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment1848)
HAnimSegment1849 = x3d.HAnimSegment()
HAnimSegment1849.USE = "hanim_r_carpal_middle_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment1849)
HAnimSegment1850 = x3d.HAnimSegment()
HAnimSegment1850.USE = "hanim_l_carpal_proximal_phalanx_1"

HAnimHumanoid43.segments.append(HAnimSegment1850)
HAnimSegment1851 = x3d.HAnimSegment()
HAnimSegment1851.USE = "hanim_r_carpal_proximal_phalanx_1"

HAnimHumanoid43.segments.append(HAnimSegment1851)
HAnimSegment1852 = x3d.HAnimSegment()
HAnimSegment1852.USE = "hanim_l_carpal_proximal_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment1852)
HAnimSegment1853 = x3d.HAnimSegment()
HAnimSegment1853.USE = "hanim_r_carpal_proximal_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment1853)
HAnimSegment1854 = x3d.HAnimSegment()
HAnimSegment1854.USE = "hanim_l_carpal_proximal_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment1854)
HAnimSegment1855 = x3d.HAnimSegment()
HAnimSegment1855.USE = "hanim_r_carpal_proximal_phalanx_3"

HAnimHumanoid43.segments.append(HAnimSegment1855)
HAnimSegment1856 = x3d.HAnimSegment()
HAnimSegment1856.USE = "hanim_l_carpal_proximal_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment1856)
HAnimSegment1857 = x3d.HAnimSegment()
HAnimSegment1857.USE = "hanim_r_carpal_proximal_phalanx_4"

HAnimHumanoid43.segments.append(HAnimSegment1857)
HAnimSegment1858 = x3d.HAnimSegment()
HAnimSegment1858.USE = "hanim_l_carpal_proximal_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment1858)
HAnimSegment1859 = x3d.HAnimSegment()
HAnimSegment1859.USE = "hanim_r_carpal_proximal_phalanx_5"

HAnimHumanoid43.segments.append(HAnimSegment1859)
HAnimSegment1860 = x3d.HAnimSegment()
HAnimSegment1860.USE = "hanim_l_clavicle"

HAnimHumanoid43.segments.append(HAnimSegment1860)
HAnimSegment1861 = x3d.HAnimSegment()
HAnimSegment1861.USE = "hanim_r_clavicle"

HAnimHumanoid43.segments.append(HAnimSegment1861)
HAnimSegment1862 = x3d.HAnimSegment()
HAnimSegment1862.USE = "hanim_l_eyeball"

HAnimHumanoid43.segments.append(HAnimSegment1862)
HAnimSegment1863 = x3d.HAnimSegment()
HAnimSegment1863.USE = "hanim_r_eyeball"

HAnimHumanoid43.segments.append(HAnimSegment1863)
HAnimSegment1864 = x3d.HAnimSegment()
HAnimSegment1864.USE = "hanim_l_eyebrow"

HAnimHumanoid43.segments.append(HAnimSegment1864)
HAnimSegment1865 = x3d.HAnimSegment()
HAnimSegment1865.USE = "hanim_r_eyebrow"

HAnimHumanoid43.segments.append(HAnimSegment1865)
HAnimSegment1866 = x3d.HAnimSegment()
HAnimSegment1866.USE = "hanim_l_eyelid"

HAnimHumanoid43.segments.append(HAnimSegment1866)
HAnimSegment1867 = x3d.HAnimSegment()
HAnimSegment1867.USE = "hanim_r_eyelid"

HAnimHumanoid43.segments.append(HAnimSegment1867)
HAnimSegment1868 = x3d.HAnimSegment()
HAnimSegment1868.USE = "hanim_l_forearm"

HAnimHumanoid43.segments.append(HAnimSegment1868)
HAnimSegment1869 = x3d.HAnimSegment()
HAnimSegment1869.USE = "hanim_r_forearm"

HAnimHumanoid43.segments.append(HAnimSegment1869)
HAnimSegment1870 = x3d.HAnimSegment()
HAnimSegment1870.USE = "hanim_l_metacarpal_1"

HAnimHumanoid43.segments.append(HAnimSegment1870)
HAnimSegment1871 = x3d.HAnimSegment()
HAnimSegment1871.USE = "hanim_r_metacarpal_1"

HAnimHumanoid43.segments.append(HAnimSegment1871)
HAnimSegment1872 = x3d.HAnimSegment()
HAnimSegment1872.USE = "hanim_l_metacarpal_2"

HAnimHumanoid43.segments.append(HAnimSegment1872)
HAnimSegment1873 = x3d.HAnimSegment()
HAnimSegment1873.USE = "hanim_r_metacarpal_2"

HAnimHumanoid43.segments.append(HAnimSegment1873)
HAnimSegment1874 = x3d.HAnimSegment()
HAnimSegment1874.USE = "hanim_l_metacarpal_3"

HAnimHumanoid43.segments.append(HAnimSegment1874)
HAnimSegment1875 = x3d.HAnimSegment()
HAnimSegment1875.USE = "hanim_r_metacarpal_3"

HAnimHumanoid43.segments.append(HAnimSegment1875)
HAnimSegment1876 = x3d.HAnimSegment()
HAnimSegment1876.USE = "hanim_l_metacarpal_4"

HAnimHumanoid43.segments.append(HAnimSegment1876)
HAnimSegment1877 = x3d.HAnimSegment()
HAnimSegment1877.USE = "hanim_r_metacarpal_4"

HAnimHumanoid43.segments.append(HAnimSegment1877)
HAnimSegment1878 = x3d.HAnimSegment()
HAnimSegment1878.USE = "hanim_l_metacarpal_5"

HAnimHumanoid43.segments.append(HAnimSegment1878)
HAnimSegment1879 = x3d.HAnimSegment()
HAnimSegment1879.USE = "hanim_r_metacarpal_5"

HAnimHumanoid43.segments.append(HAnimSegment1879)
HAnimSegment1880 = x3d.HAnimSegment()
HAnimSegment1880.USE = "hanim_l_metatarsal_2"

HAnimHumanoid43.segments.append(HAnimSegment1880)
HAnimSegment1881 = x3d.HAnimSegment()
HAnimSegment1881.USE = "hanim_r_metatarsal_2"

HAnimHumanoid43.segments.append(HAnimSegment1881)
HAnimSegment1882 = x3d.HAnimSegment()
HAnimSegment1882.USE = "hanim_l_scapula"

HAnimHumanoid43.segments.append(HAnimSegment1882)
HAnimSegment1883 = x3d.HAnimSegment()
HAnimSegment1883.USE = "hanim_r_scapula"

HAnimHumanoid43.segments.append(HAnimSegment1883)
HAnimSegment1884 = x3d.HAnimSegment()
HAnimSegment1884.USE = "hanim_l_talus"

HAnimHumanoid43.segments.append(HAnimSegment1884)
HAnimSegment1885 = x3d.HAnimSegment()
HAnimSegment1885.USE = "hanim_r_talus"

HAnimHumanoid43.segments.append(HAnimSegment1885)
HAnimSegment1886 = x3d.HAnimSegment()
HAnimSegment1886.USE = "hanim_l_tarsal_distal_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment1886)
HAnimSegment1887 = x3d.HAnimSegment()
HAnimSegment1887.USE = "hanim_r_tarsal_distal_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment1887)
HAnimSegment1888 = x3d.HAnimSegment()
HAnimSegment1888.USE = "hanim_l_tarsal_proximal_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment1888)
HAnimSegment1889 = x3d.HAnimSegment()
HAnimSegment1889.USE = "hanim_r_tarsal_proximal_phalanx_2"

HAnimHumanoid43.segments.append(HAnimSegment1889)
HAnimSegment1890 = x3d.HAnimSegment()
HAnimSegment1890.USE = "hanim_l_thigh"

HAnimHumanoid43.segments.append(HAnimSegment1890)
HAnimSegment1891 = x3d.HAnimSegment()
HAnimSegment1891.USE = "hanim_r_thigh"

HAnimHumanoid43.segments.append(HAnimSegment1891)
HAnimSegment1892 = x3d.HAnimSegment()
HAnimSegment1892.USE = "hanim_l_upperarm"

HAnimHumanoid43.segments.append(HAnimSegment1892)
HAnimSegment1893 = x3d.HAnimSegment()
HAnimSegment1893.USE = "hanim_r_upperarm"

HAnimHumanoid43.segments.append(HAnimSegment1893)
HAnimSite1894 = x3d.HAnimSite()
HAnimSite1894.USE = "hanim_crotch_pt"

HAnimHumanoid43.sites.append(HAnimSite1894)
HAnimSite1895 = x3d.HAnimSite()
HAnimSite1895.USE = "hanim_skull_vertex_pt"

HAnimHumanoid43.sites.append(HAnimSite1895)
HAnimSite1896 = x3d.HAnimSite()
HAnimSite1896.USE = "hanim_sellion_pt"

HAnimHumanoid43.sites.append(HAnimSite1896)
HAnimSite1897 = x3d.HAnimSite()
HAnimSite1897.USE = "hanim_supramenton_pt"

HAnimHumanoid43.sites.append(HAnimSite1897)
HAnimSite1898 = x3d.HAnimSite()
HAnimSite1898.USE = "hanim_nuchale_pt"

HAnimHumanoid43.sites.append(HAnimSite1898)
HAnimSite1899 = x3d.HAnimSite()
HAnimSite1899.USE = "hanim_suprasternale_pt"

HAnimHumanoid43.sites.append(HAnimSite1899)
HAnimSite1900 = x3d.HAnimSite()
HAnimSite1900.USE = "hanim_cervicale_pt"

HAnimHumanoid43.sites.append(HAnimSite1900)
HAnimSite1901 = x3d.HAnimSite()
HAnimSite1901.USE = "hanim_substernale_pt"

HAnimHumanoid43.sites.append(HAnimSite1901)
HAnimSite1902 = x3d.HAnimSite()
HAnimSite1902.USE = "hanim_rib10_midspine_pt"

HAnimHumanoid43.sites.append(HAnimSite1902)
HAnimSite1903 = x3d.HAnimSite()
HAnimSite1903.USE = "hanim_waist_preferred_posterior_pt"

HAnimHumanoid43.sites.append(HAnimSite1903)
HAnimSite1904 = x3d.HAnimSite()
HAnimSite1904.USE = "hanim_navel_pt"

HAnimHumanoid43.sites.append(HAnimSite1904)
HAnimSite1905 = x3d.HAnimSite()
HAnimSite1905.USE = "hanim_l_acromion_pt"

HAnimHumanoid43.sites.append(HAnimSite1905)
HAnimSite1906 = x3d.HAnimSite()
HAnimSite1906.USE = "hanim_r_acromion_pt"

HAnimHumanoid43.sites.append(HAnimSite1906)
HAnimSite1907 = x3d.HAnimSite()
HAnimSite1907.USE = "hanim_r_asis_pt"

HAnimHumanoid43.sites.append(HAnimSite1907)
HAnimSite1908 = x3d.HAnimSite()
HAnimSite1908.USE = "hanim_l_asis_pt"

HAnimHumanoid43.sites.append(HAnimSite1908)
HAnimSite1909 = x3d.HAnimSite()
HAnimSite1909.USE = "hanim_l_axilla_distal_pt"

HAnimHumanoid43.sites.append(HAnimSite1909)
HAnimSite1910 = x3d.HAnimSite()
HAnimSite1910.USE = "hanim_r_axilla_distal_pt"

HAnimHumanoid43.sites.append(HAnimSite1910)
HAnimSite1911 = x3d.HAnimSite()
HAnimSite1911.USE = "hanim_l_axilla_proximal_pt"

HAnimHumanoid43.sites.append(HAnimSite1911)
HAnimSite1912 = x3d.HAnimSite()
HAnimSite1912.USE = "hanim_r_axilla_proximal_pt"

HAnimHumanoid43.sites.append(HAnimSite1912)
HAnimSite1913 = x3d.HAnimSite()
HAnimSite1913.USE = "hanim_l_calcaneus_posterior_pt"

HAnimHumanoid43.sites.append(HAnimSite1913)
HAnimSite1914 = x3d.HAnimSite()
HAnimSite1914.USE = "hanim_r_calcaneus_posterior_pt"

HAnimHumanoid43.sites.append(HAnimSite1914)
HAnimSite1915 = x3d.HAnimSite()
HAnimSite1915.USE = "hanim_l_carpal_distal_phalanx_1_pt"

HAnimHumanoid43.sites.append(HAnimSite1915)
HAnimSite1916 = x3d.HAnimSite()
HAnimSite1916.USE = "hanim_r_carpal_distal_phalanx_1_pt"

HAnimHumanoid43.sites.append(HAnimSite1916)
HAnimSite1917 = x3d.HAnimSite()
HAnimSite1917.USE = "hanim_l_carpal_distal_phalanx_2_pt"

HAnimHumanoid43.sites.append(HAnimSite1917)
HAnimSite1918 = x3d.HAnimSite()
HAnimSite1918.USE = "hanim_r_carpal_distal_phalanx_2_pt"

HAnimHumanoid43.sites.append(HAnimSite1918)
HAnimSite1919 = x3d.HAnimSite()
HAnimSite1919.USE = "hanim_l_carpal_distal_phalanx_3_pt"

HAnimHumanoid43.sites.append(HAnimSite1919)
HAnimSite1920 = x3d.HAnimSite()
HAnimSite1920.USE = "hanim_r_carpal_distal_phalanx_3_pt"

HAnimHumanoid43.sites.append(HAnimSite1920)
HAnimSite1921 = x3d.HAnimSite()
HAnimSite1921.USE = "hanim_l_carpal_distal_phalanx_4_pt"

HAnimHumanoid43.sites.append(HAnimSite1921)
HAnimSite1922 = x3d.HAnimSite()
HAnimSite1922.USE = "hanim_r_carpal_distal_phalanx_4_pt"

HAnimHumanoid43.sites.append(HAnimSite1922)
HAnimSite1923 = x3d.HAnimSite()
HAnimSite1923.USE = "hanim_l_carpal_distal_phalanx_5_pt"

HAnimHumanoid43.sites.append(HAnimSite1923)
HAnimSite1924 = x3d.HAnimSite()
HAnimSite1924.USE = "hanim_r_carpal_distal_phalanx_5_pt"

HAnimHumanoid43.sites.append(HAnimSite1924)
HAnimSite1925 = x3d.HAnimSite()
HAnimSite1925.USE = "hanim_l_clavicle_pt"

HAnimHumanoid43.sites.append(HAnimSite1925)
HAnimSite1926 = x3d.HAnimSite()
HAnimSite1926.USE = "hanim_r_clavicle_pt"

HAnimHumanoid43.sites.append(HAnimSite1926)
HAnimSite1927 = x3d.HAnimSite()
HAnimSite1927.USE = "hanim_l_dactylion_pt"

HAnimHumanoid43.sites.append(HAnimSite1927)
HAnimSite1928 = x3d.HAnimSite()
HAnimSite1928.USE = "hanim_r_dactylion_pt"

HAnimHumanoid43.sites.append(HAnimSite1928)
HAnimSite1929 = x3d.HAnimSite()
HAnimSite1929.USE = "hanim_l_femoral_lateral_epicondyle_pt"

HAnimHumanoid43.sites.append(HAnimSite1929)
HAnimSite1930 = x3d.HAnimSite()
HAnimSite1930.USE = "hanim_r_femoral_lateral_epicondyle_pt"

HAnimHumanoid43.sites.append(HAnimSite1930)
HAnimSite1931 = x3d.HAnimSite()
HAnimSite1931.USE = "hanim_l_femoral_medial_epicondyle_pt"

HAnimHumanoid43.sites.append(HAnimSite1931)
HAnimSite1932 = x3d.HAnimSite()
HAnimSite1932.USE = "hanim_r_femoral_medial_epicondyle_pt"

HAnimHumanoid43.sites.append(HAnimSite1932)
HAnimSite1933 = x3d.HAnimSite()
HAnimSite1933.USE = "hanim_l_forefoot_tip_pt"

HAnimHumanoid43.sites.append(HAnimSite1933)
HAnimSite1934 = x3d.HAnimSite()
HAnimSite1934.USE = "hanim_r_forefoot_tip_pt"

HAnimHumanoid43.sites.append(HAnimSite1934)
HAnimSite1935 = x3d.HAnimSite()
HAnimSite1935.USE = "hanim_r_gonion_pt"

HAnimHumanoid43.sites.append(HAnimSite1935)
HAnimSite1936 = x3d.HAnimSite()
HAnimSite1936.USE = "hanim_l_gonion_pt"

HAnimHumanoid43.sites.append(HAnimSite1936)
HAnimSite1937 = x3d.HAnimSite()
HAnimSite1937.USE = "hanim_l_humeral_lateral_epicondyle_pt"

HAnimHumanoid43.sites.append(HAnimSite1937)
HAnimSite1938 = x3d.HAnimSite()
HAnimSite1938.USE = "hanim_r_humeral_lateral_epicondyle_pt"

HAnimHumanoid43.sites.append(HAnimSite1938)
HAnimSite1939 = x3d.HAnimSite()
HAnimSite1939.USE = "hanim_l_humeral_medial_epicondyle_pt"

HAnimHumanoid43.sites.append(HAnimSite1939)
HAnimSite1940 = x3d.HAnimSite()
HAnimSite1940.USE = "hanim_r_humeral_medial_epicondyle_pt"

HAnimHumanoid43.sites.append(HAnimSite1940)
HAnimSite1941 = x3d.HAnimSite()
HAnimSite1941.USE = "hanim_r_iliocristale_pt"

HAnimHumanoid43.sites.append(HAnimSite1941)
HAnimSite1942 = x3d.HAnimSite()
HAnimSite1942.USE = "hanim_l_iliocristale_pt"

HAnimHumanoid43.sites.append(HAnimSite1942)
HAnimSite1943 = x3d.HAnimSite()
HAnimSite1943.USE = "hanim_r_infraorbitale_pt"

HAnimHumanoid43.sites.append(HAnimSite1943)
HAnimSite1944 = x3d.HAnimSite()
HAnimSite1944.USE = "hanim_l_infraorbitale_pt"

HAnimHumanoid43.sites.append(HAnimSite1944)
HAnimSite1945 = x3d.HAnimSite()
HAnimSite1945.USE = "hanim_l_knee_crease_pt"

HAnimHumanoid43.sites.append(HAnimSite1945)
HAnimSite1946 = x3d.HAnimSite()
HAnimSite1946.USE = "hanim_r_knee_crease_pt"

HAnimHumanoid43.sites.append(HAnimSite1946)
HAnimSite1947 = x3d.HAnimSite()
HAnimSite1947.USE = "hanim_l_lateral_malleolus_pt"

HAnimHumanoid43.sites.append(HAnimSite1947)
HAnimSite1948 = x3d.HAnimSite()
HAnimSite1948.USE = "hanim_r_lateral_malleolus_pt"

HAnimHumanoid43.sites.append(HAnimSite1948)
HAnimSite1949 = x3d.HAnimSite()
HAnimSite1949.USE = "hanim_l_medial_malleolus_pt"

HAnimHumanoid43.sites.append(HAnimSite1949)
HAnimSite1950 = x3d.HAnimSite()
HAnimSite1950.USE = "hanim_r_medial_malleolus_pt"

HAnimHumanoid43.sites.append(HAnimSite1950)
HAnimSite1951 = x3d.HAnimSite()
HAnimSite1951.USE = "hanim_l_metacarpal_phalanx_2_pt"

HAnimHumanoid43.sites.append(HAnimSite1951)
HAnimSite1952 = x3d.HAnimSite()
HAnimSite1952.USE = "hanim_r_metacarpal_phalanx_2_pt"

HAnimHumanoid43.sites.append(HAnimSite1952)
HAnimSite1953 = x3d.HAnimSite()
HAnimSite1953.USE = "hanim_l_metacarpal_phalanx_5_pt"

HAnimHumanoid43.sites.append(HAnimSite1953)
HAnimSite1954 = x3d.HAnimSite()
HAnimSite1954.USE = "hanim_r_metacarpal_phalanx_5_pt"

HAnimHumanoid43.sites.append(HAnimSite1954)
HAnimSite1955 = x3d.HAnimSite()
HAnimSite1955.USE = "hanim_l_metatarsal_phalanx_1_pt"

HAnimHumanoid43.sites.append(HAnimSite1955)
HAnimSite1956 = x3d.HAnimSite()
HAnimSite1956.USE = "hanim_r_metatarsal_phalanx_1_pt"

HAnimHumanoid43.sites.append(HAnimSite1956)
HAnimSite1957 = x3d.HAnimSite()
HAnimSite1957.USE = "hanim_l_metatarsal_phalanx_5_pt"

HAnimHumanoid43.sites.append(HAnimSite1957)
HAnimSite1958 = x3d.HAnimSite()
HAnimSite1958.USE = "hanim_r_metatarsal_phalanx_5_pt"

HAnimHumanoid43.sites.append(HAnimSite1958)
HAnimSite1959 = x3d.HAnimSite()
HAnimSite1959.USE = "hanim_r_neck_base_pt"

HAnimHumanoid43.sites.append(HAnimSite1959)
HAnimSite1960 = x3d.HAnimSite()
HAnimSite1960.USE = "hanim_l_neck_base_pt"

HAnimHumanoid43.sites.append(HAnimSite1960)
HAnimSite1961 = x3d.HAnimSite()
HAnimSite1961.USE = "hanim_l_olecranon_pt"

HAnimHumanoid43.sites.append(HAnimSite1961)
HAnimSite1962 = x3d.HAnimSite()
HAnimSite1962.USE = "hanim_r_olecranon_pt"

HAnimHumanoid43.sites.append(HAnimSite1962)
HAnimSite1963 = x3d.HAnimSite()
HAnimSite1963.USE = "hanim_r_psis_pt"

HAnimHumanoid43.sites.append(HAnimSite1963)
HAnimSite1964 = x3d.HAnimSite()
HAnimSite1964.USE = "hanim_l_psis_pt"

HAnimHumanoid43.sites.append(HAnimSite1964)
HAnimSite1965 = x3d.HAnimSite()
HAnimSite1965.USE = "hanim_l_radial_styloid_pt"

HAnimHumanoid43.sites.append(HAnimSite1965)
HAnimSite1966 = x3d.HAnimSite()
HAnimSite1966.USE = "hanim_r_radial_styloid_pt"

HAnimHumanoid43.sites.append(HAnimSite1966)
HAnimSite1967 = x3d.HAnimSite()
HAnimSite1967.USE = "hanim_l_radiale_pt"

HAnimHumanoid43.sites.append(HAnimSite1967)
HAnimSite1968 = x3d.HAnimSite()
HAnimSite1968.USE = "hanim_r_radiale_pt"

HAnimHumanoid43.sites.append(HAnimSite1968)
HAnimSite1969 = x3d.HAnimSite()
HAnimSite1969.USE = "hanim_r_rib10_pt"

HAnimHumanoid43.sites.append(HAnimSite1969)
HAnimSite1970 = x3d.HAnimSite()
HAnimSite1970.USE = "hanim_l_rib10_pt"

HAnimHumanoid43.sites.append(HAnimSite1970)
HAnimSite1971 = x3d.HAnimSite()
HAnimSite1971.USE = "hanim_temporomandibular_l_site_pt"

HAnimHumanoid43.sites.append(HAnimSite1971)
HAnimSite1972 = x3d.HAnimSite()
HAnimSite1972.USE = "hanim_temporomandibular_r_site_pt"

HAnimHumanoid43.sites.append(HAnimSite1972)
HAnimSite1973 = x3d.HAnimSite()
HAnimSite1973.USE = "hanim_l_sphyrion_pt"

HAnimHumanoid43.sites.append(HAnimSite1973)
HAnimSite1974 = x3d.HAnimSite()
HAnimSite1974.USE = "hanim_r_sphyrion_pt"

HAnimHumanoid43.sites.append(HAnimSite1974)
HAnimSite1975 = x3d.HAnimSite()
HAnimSite1975.USE = "hanim_l_tarsal_distal_phalanx_2_pt"

HAnimHumanoid43.sites.append(HAnimSite1975)
HAnimSite1976 = x3d.HAnimSite()
HAnimSite1976.USE = "hanim_r_tarsal_distal_phalanx_2_pt"

HAnimHumanoid43.sites.append(HAnimSite1976)
HAnimSite1977 = x3d.HAnimSite()
HAnimSite1977.USE = "hanim_r_thelion_pt"

HAnimHumanoid43.sites.append(HAnimSite1977)
HAnimSite1978 = x3d.HAnimSite()
HAnimSite1978.USE = "hanim_l_thelion_pt"

HAnimHumanoid43.sites.append(HAnimSite1978)
HAnimSite1979 = x3d.HAnimSite()
HAnimSite1979.USE = "hanim_r_tragion_pt"

HAnimHumanoid43.sites.append(HAnimSite1979)
HAnimSite1980 = x3d.HAnimSite()
HAnimSite1980.USE = "hanim_l_tragion_pt"

HAnimHumanoid43.sites.append(HAnimSite1980)
HAnimSite1981 = x3d.HAnimSite()
HAnimSite1981.USE = "hanim_r_trochanterion_pt"

HAnimHumanoid43.sites.append(HAnimSite1981)
HAnimSite1982 = x3d.HAnimSite()
HAnimSite1982.USE = "hanim_l_trochanterion_pt"

HAnimHumanoid43.sites.append(HAnimSite1982)
HAnimSite1983 = x3d.HAnimSite()
HAnimSite1983.USE = "hanim_l_ulnar_styloid_pt"

HAnimHumanoid43.sites.append(HAnimSite1983)
HAnimSite1984 = x3d.HAnimSite()
HAnimSite1984.USE = "hanim_r_ulnar_styloid_pt"

HAnimHumanoid43.sites.append(HAnimSite1984)

Scene29.children.append(HAnimHumanoid43)

X3D0.Scene = Scene29
f = open("././HAnim2SpecificationLOA3Illustrated_RoundTrip.x3d", "w")
f.write(X3D0.XML())
f.close()
