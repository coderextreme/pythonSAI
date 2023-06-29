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
meta3.content = "HAnim1SpecificationLOA3Animation.x3d"

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.name = "description"
meta4.content = "HAnim Specification reference example providing full coverage and visibility of all specified HAnim constructs, plus motion animations. Geometry visualizations are derived from HAnim1SpecificationLOA3Invisible.x3d visualization report. Resusable exemplar animations also added via heads-up display (HUD) interface to confirm proper parent-child relationships."

head1.children.append(meta4)
meta5 = x3d.meta()
meta5.name = "reference"
meta5.content = "https://www.web3d.org/files/specifications/19774/V1.0/HAnim/BodyDimensionsAndLOAs.html#LOA3ExampleSourceWithDiamonds"

head1.children.append(meta5)
meta6 = x3d.meta()
meta6.name = "created"
meta6.content = "24 April 2013"

head1.children.append(meta6)
meta7 = x3d.meta()
meta7.name = "modified"
meta7.content = "19 February 2021"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.name = "Image"
meta8.content = "HAnim1SpecificationLOA3MotionH3DViewer.png"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "Image"
meta9.content = "HAnim1SpecificationLOA3MotionInstantReality.png"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "Image"
meta10.content = "HAnim1SpecificationLOA3MotionOctagaVS.png"

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.name = "Image"
meta11.content = "HAnim1SpecificationLOA3MotionView3dscene.png"

head1.children.append(meta11)
meta12 = x3d.meta()
meta12.name = "reference"
meta12.content = "HAnim1SpecificationLOA3Illustrated.x3d"

head1.children.append(meta12)
meta13 = x3d.meta()
meta13.name = "reference"
meta13.content = "HAnim1SpecificationLOA3Invisible.x3d"

head1.children.append(meta13)
meta14 = x3d.meta()
meta14.name = "reference"
meta14.content = "HAnimSpecificationExampleChangeLog.txt"

head1.children.append(meta14)
meta15 = x3d.meta()
meta15.name = "Image"
meta15.content = "images/BonesAllSkeletonFrontViewLOA1.png"

head1.children.append(meta15)
meta16 = x3d.meta()
meta16.name = "Image"
meta16.content = "images/BonesAllSkeletonFrontViewLOA2.png"

head1.children.append(meta16)
meta17 = x3d.meta()
meta17.name = "Image"
meta17.content = "images/BonesAllSkeletonFrontViewLOA3.png"

head1.children.append(meta17)
meta18 = x3d.meta()
meta18.name = "reference"
meta18.content = "Norman Badler et al., ANTHROPOMETRY FOR COMPUTER GRAPHICS HUMAN FIGURES, University of Pennsylvania, 1989."

head1.children.append(meta18)
meta19 = x3d.meta()
meta19.name = "reference"
meta19.content = "http://www.cis.upenn.edu/~badler/anthro/89-71.ps"

head1.children.append(meta19)
meta20 = x3d.meta()
meta20.name = "reference"
meta20.content = "tables/AnthropometryForComputerGraphicsHumanFigures89-71.pdf"

head1.children.append(meta20)
meta21 = x3d.meta()
meta21.name = "creator"
meta21.content = "Matthew T. Beitler, Joe D. Williams, Don Brutzman"

head1.children.append(meta21)
meta22 = x3d.meta()
meta22.name = "translator"
meta22.content = "Don Brutzman and Joe Williams"

head1.children.append(meta22)
meta23 = x3d.meta()
meta23.name = "generator"
meta23.content = "BS Contact Geo 8.001, http://www.bitmanagement.de/en/products/interactive-3d-clients/bs-contact-geo"

head1.children.append(meta23)
meta24 = x3d.meta()
meta24.name = "reference"
meta24.content = "originals/LOA3ExampleSourceWithDiamondsOriginal.wrl"

head1.children.append(meta24)
meta25 = x3d.meta()
meta25.name = "reference"
meta25.content = "originals/LOA3ExampleSourceWithDiamondsOriginal.x3d"

head1.children.append(meta25)
meta26 = x3d.meta()
meta26.name = "reference"
meta26.content = "originals/LOA3ExampleSourceWithDiamondsOriginalBsContactExport.x3d"

head1.children.append(meta26)
meta27 = x3d.meta()
meta27.name = "generator"
meta27.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"

head1.children.append(meta27)
meta28 = x3d.meta()
meta28.name = "identifier"
meta28.content = "https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Legacy/HAnim1SpecificationLOA3Animation.x3d"

head1.children.append(meta28)
meta29 = x3d.meta()
meta29.name = "license"
meta29.content = "../license.html"

head1.children.append(meta29)

X3D0.head = head1
Scene30 = x3d.Scene()
Background31 = x3d.Background()
Background31.skyColor = [0.3,0.3,0.3]

Scene30.children.append(Background31)
NavigationInfo32 = x3d.NavigationInfo()

Scene30.children.append(NavigationInfo32)
Group33 = x3d.Group()
Group33.DEF = "Original_WorldInfo"
WorldInfo34 = x3d.WorldInfo()
WorldInfo34.info = [" HANIM 200x Default Joint Centers, Level-Of-Articulation 3 HANIM 200x (VRML97) Author name: eMpTy (a.k.a. Matthew T. Beitler) HANIM 200x (VRML97) Author email: beitler@cis.upenn.edu or beitler@acm.org HANIM 200x (VRML97) Author homepage: http://www.cis.upenn.edu/~beitler HANIM 200x (VRML97) Compliance Date: August 12, 2003 HANIM 200x Compliance Information: http://HAnim.org/Specifications/HAnim200x Construction Info (joint centers): The joint centers of this figure are based on the work of Norman Badler, director of the Center for Human Modeling and Simulation at the University of Pennsylvania. The original document which these joint centers are based on can be found at: http://www.cis.upenn.edu/~badler/anthro/89-71.ps "]
WorldInfo34.title = "HANIM 200x Default Joint Centers, LOA3"

Group33.children.append(WorldInfo34)

Scene30.children.append(Group33)
#TODO move viewpoints to be internal to HAnimHumanoid
#Viewpoint centerOfRotation=\"0 0.9149 0.0016\" matches initial at-rest locaton of the sacroliac. Note that these viewpoints are external to the HAnimHumanoid and do not move with the human.
Viewpoint35 = x3d.Viewpoint()
Viewpoint35.centerOfRotation = [0,0.9149,0.0016]
Viewpoint35.description = "Humanoid LOA 3 Front"
Viewpoint35.position = [0,0.4,4]

Scene30.children.append(Viewpoint35)
Viewpoint36 = x3d.Viewpoint()
Viewpoint36.centerOfRotation = [0,0.9149,0.0016]
Viewpoint36.description = "Humanoid LOA 3 Front Close"
Viewpoint36.position = [0,0.8,2]

Scene30.children.append(Viewpoint36)
Viewpoint37 = x3d.Viewpoint()
Viewpoint37.centerOfRotation = [0,0.9149,0.0016]
Viewpoint37.description = "Humanoid LOA 3 Front Closer"
Viewpoint37.position = [0,1.2,1]

Scene30.children.append(Viewpoint37)
Viewpoint38 = x3d.Viewpoint()
Viewpoint38.centerOfRotation = [0,1.5,0.0016]
Viewpoint38.description = "Humanoid LOA 3 Front Face"
Viewpoint38.position = [0,1.63,1]

Scene30.children.append(Viewpoint38)
Viewpoint39 = x3d.Viewpoint()
Viewpoint39.centerOfRotation = [0,0.9149,0.0016]
Viewpoint39.description = "Humanoid LOA 3 Right Side"
Viewpoint39.orientation = [0,1,0,1.5708]
Viewpoint39.position = [2.6,0.8,0]

Scene30.children.append(Viewpoint39)
Viewpoint40 = x3d.Viewpoint()
Viewpoint40.centerOfRotation = [0,0.9149,0.0016]
Viewpoint40.description = "Humanoid LOA 3 Right Side Close"
Viewpoint40.orientation = [0,1,0,1.2]
Viewpoint40.position = [1,0.8,0.5]

Scene30.children.append(Viewpoint40)
Viewpoint41 = x3d.Viewpoint()
Viewpoint41.centerOfRotation = [0,0.9149,0.0016]
Viewpoint41.description = "Humanoid LOA 3 Left Side Close"
Viewpoint41.orientation = [0,1,0,-1.2]
Viewpoint41.position = [-1,0.8,0.5]

Scene30.children.append(Viewpoint41)
Viewpoint42 = x3d.Viewpoint()
Viewpoint42.centerOfRotation = [0,0.9149,0.0016]
Viewpoint42.description = "Humanoid LOA 3 Left Side"
Viewpoint42.orientation = [0,1,0,-1.5708]
Viewpoint42.position = [-2.6,0.8,0]

Scene30.children.append(Viewpoint42)
Viewpoint43 = x3d.Viewpoint()
Viewpoint43.centerOfRotation = [0,0.9149,0.0016]
Viewpoint43.description = "Humanoid LOA 3 Top"
Viewpoint43.orientation = [1,0,0,-1.5708]
Viewpoint43.position = [0,3.5,0]

Scene30.children.append(Viewpoint43)
HAnimHumanoid44 = x3d.HAnimHumanoid()
HAnimHumanoid44.name = "humanoid"
HAnimHumanoid44.DEF = "hanim_humanoid"
HAnimHumanoid44.info = ["authorName=Matthew T. Beitler Joe D. Williams Don Brutzman","authorEmail=HAnim@web3D.org","copyright=none","creationDate=12 May 1999","usageRestrictions=none","humanoidVersion=2.0","height=1.7504"]
HAnimHumanoid44.version = "2.0"
HAnimJoint45 = x3d.HAnimJoint()
HAnimJoint45.name = "humanoid_root"
HAnimJoint45.DEF = "hanim_humanoid_root"
HAnimJoint45.center = [0,0.824,0.0277]
HAnimJoint45.ulimit = [0,0,0]
HAnimJoint45.llimit = [0,0,0]
HAnimSegment46 = x3d.HAnimSegment()
HAnimSegment46.name = "sacrum"
HAnimSegment46.DEF = "hanim_sacrum"
#<HAnimJoint name='humanoid_root'/> visualization sphere within <HAnimSegment name='sacrum'/>
TouchSensor47 = x3d.TouchSensor()
TouchSensor47.description = "HAnimJoint HumanoidRoot, HAnimSegment sacrum"

HAnimSegment46.children.append(TouchSensor47)
Transform48 = x3d.Transform()
Transform48.translation = [0,0.824,0.0277]
Shape49 = x3d.Shape()
Shape49.DEF = "HAnimJointShape"
Sphere50 = x3d.Sphere()
Sphere50.radius = 0.006

Shape49.geometry = Sphere50
Appearance51 = x3d.Appearance()
Appearance51.DEF = "HAnimJointAppearance"
Material52 = x3d.Material()
Material52.diffuseColor = [1,0.5,0]
Material52.transparency = 0.5

Appearance51.material = Material52

Shape49.appearance = Appearance51

Transform48.children.append(Shape49)

HAnimSegment46.children.append(Transform48)
#HAnimSegment visualization line segment from parent <HAnimJoint name='humanoid_root'/> to <HAnimJoint name='sacroiliac'/>
Shape53 = x3d.Shape()
LineSet54 = x3d.LineSet()
LineSet54.vertexCount = [2]
Coordinate55 = x3d.Coordinate()
Coordinate55.point = (0.0000,0.8240,0.0277,0.0000,0.9149,0.0016)

LineSet54.coord = Coordinate55
ColorRGBA56 = x3d.ColorRGBA()
ColorRGBA56.DEF = "HAnimSegmentLineColorRGBA"
ColorRGBA56.color = [1,1,0,1,1,1,0,0.1]

LineSet54.color = ColorRGBA56

Shape53.geometry = LineSet54

HAnimSegment46.children.append(Shape53)
#HAnimSegment visualization line segment from parent <HAnimJoint name='humanoid_root'/> to <HAnimJoint name='vl5'/>
Shape57 = x3d.Shape()
LineSet58 = x3d.LineSet()
LineSet58.vertexCount = [2]
Coordinate59 = x3d.Coordinate()
Coordinate59.point = (0.0000,0.8240,0.0277,0.0028,1.0568,-0.0776)

LineSet58.coord = Coordinate59
ColorRGBA60 = x3d.ColorRGBA()
ColorRGBA60.USE = "HAnimSegmentLineColorRGBA"

LineSet58.color = ColorRGBA60

Shape57.geometry = LineSet58

HAnimSegment46.children.append(Shape57)

HAnimJoint45.children.append(HAnimSegment46)
HAnimJoint61 = x3d.HAnimJoint()
HAnimJoint61.name = "sacroiliac"
HAnimJoint61.DEF = "hanim_sacroiliac"
HAnimJoint61.center = [0,0.9149,0.0016]
HAnimJoint61.ulimit = [0,0,0]
HAnimJoint61.llimit = [0,0,0]
HAnimSegment62 = x3d.HAnimSegment()
HAnimSegment62.name = "pelvis"
HAnimSegment62.DEF = "hanim_pelvis"
#<HAnimJoint name='sacroiliac'/> visualization sphere within <HAnimSegment name='pelvis'/>
TouchSensor63 = x3d.TouchSensor()
TouchSensor63.description = "HAnimJoint sacroiliac, HAnimSegment pelvis"

HAnimSegment62.children.append(TouchSensor63)
Transform64 = x3d.Transform()
Transform64.translation = [0,0.9149,0.0016]
Shape65 = x3d.Shape()
Shape65.USE = "HAnimJointShape"

Transform64.children.append(Shape65)

HAnimSegment62.children.append(Transform64)
#HAnimSegment visualization line segment from parent <HAnimJoint name='sacroiliac'/> to <HAnimJoint name='l_hip'/>
Shape66 = x3d.Shape()
LineSet67 = x3d.LineSet()
LineSet67.vertexCount = [2]
Coordinate68 = x3d.Coordinate()
Coordinate68.point = (0.0000,0.9149,0.0016,0.0961,0.9124,-0.0001)

LineSet67.coord = Coordinate68
ColorRGBA69 = x3d.ColorRGBA()
ColorRGBA69.USE = "HAnimSegmentLineColorRGBA"

LineSet67.color = ColorRGBA69

Shape66.geometry = LineSet67

HAnimSegment62.children.append(Shape66)
#HAnimSegment visualization line segment from parent <HAnimJoint name='sacroiliac'/> to <HAnimJoint name='r_hip'/>
Shape70 = x3d.Shape()
LineSet71 = x3d.LineSet()
LineSet71.vertexCount = [2]
Coordinate72 = x3d.Coordinate()
Coordinate72.point = (0.0000,0.9149,0.0016,-0.0961,0.9124,-0.0001)

LineSet71.coord = Coordinate72
ColorRGBA73 = x3d.ColorRGBA()
ColorRGBA73.USE = "HAnimSegmentLineColorRGBA"

LineSet71.color = ColorRGBA73

Shape70.geometry = LineSet71

HAnimSegment62.children.append(Shape70)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='sacroiliac'/> to <HAnimSite name='r_iliocristale'/>
Shape74 = x3d.Shape()
LineSet75 = x3d.LineSet()
LineSet75.vertexCount = [2]
Coordinate76 = x3d.Coordinate()
Coordinate76.point = (0.0000,0.9149,0.0016,-0.1525,1.0628,0.0035)

LineSet75.coord = Coordinate76
ColorRGBA77 = x3d.ColorRGBA()
ColorRGBA77.DEF = "HAnimSiteLineColorRGBA"
ColorRGBA77.color = [1,0,0,1,1,0,0,0.1]

LineSet75.color = ColorRGBA77

Shape74.geometry = LineSet75

HAnimSegment62.children.append(Shape74)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='sacroiliac'/> to <HAnimSite name='r_trochanterion'/>
Shape78 = x3d.Shape()
LineSet79 = x3d.LineSet()
LineSet79.vertexCount = [2]
Coordinate80 = x3d.Coordinate()
Coordinate80.point = (0.0000,0.9149,0.0016,-0.1689,0.8419,0.0352)

LineSet79.coord = Coordinate80
ColorRGBA81 = x3d.ColorRGBA()
ColorRGBA81.USE = "HAnimSiteLineColorRGBA"

LineSet79.color = ColorRGBA81

Shape78.geometry = LineSet79

HAnimSegment62.children.append(Shape78)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='sacroiliac'/> to <HAnimSite name='l_iliocristale'/>
Shape82 = x3d.Shape()
LineSet83 = x3d.LineSet()
LineSet83.vertexCount = [2]
Coordinate84 = x3d.Coordinate()
Coordinate84.point = (0.0000,0.9149,0.0016,0.1612,1.0537,0.0008)

LineSet83.coord = Coordinate84
ColorRGBA85 = x3d.ColorRGBA()
ColorRGBA85.USE = "HAnimSiteLineColorRGBA"

LineSet83.color = ColorRGBA85

Shape82.geometry = LineSet83

HAnimSegment62.children.append(Shape82)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='sacroiliac'/> to <HAnimSite name='l_trochanterion'/>
Shape86 = x3d.Shape()
LineSet87 = x3d.LineSet()
LineSet87.vertexCount = [2]
Coordinate88 = x3d.Coordinate()
Coordinate88.point = (0.0000,0.9149,0.0016,0.1677,0.8336,0.0303)

LineSet87.coord = Coordinate88
ColorRGBA89 = x3d.ColorRGBA()
ColorRGBA89.USE = "HAnimSiteLineColorRGBA"

LineSet87.color = ColorRGBA89

Shape86.geometry = LineSet87

HAnimSegment62.children.append(Shape86)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='sacroiliac'/> to <HAnimSite name='r_asis'/>
Shape90 = x3d.Shape()
LineSet91 = x3d.LineSet()
LineSet91.vertexCount = [2]
Coordinate92 = x3d.Coordinate()
Coordinate92.point = (0.0000,0.9149,0.0016,-0.0887,1.0021,0.1112)

LineSet91.coord = Coordinate92
ColorRGBA93 = x3d.ColorRGBA()
ColorRGBA93.USE = "HAnimSiteLineColorRGBA"

LineSet91.color = ColorRGBA93

Shape90.geometry = LineSet91

HAnimSegment62.children.append(Shape90)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='sacroiliac'/> to <HAnimSite name='l_asis'/>
Shape94 = x3d.Shape()
LineSet95 = x3d.LineSet()
LineSet95.vertexCount = [2]
Coordinate96 = x3d.Coordinate()
Coordinate96.point = (0.0000,0.9149,0.0016,0.0925,0.9983,0.1052)

LineSet95.coord = Coordinate96
ColorRGBA97 = x3d.ColorRGBA()
ColorRGBA97.USE = "HAnimSiteLineColorRGBA"

LineSet95.color = ColorRGBA97

Shape94.geometry = LineSet95

HAnimSegment62.children.append(Shape94)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='sacroiliac'/> to <HAnimSite name='r_psis'/>
Shape98 = x3d.Shape()
LineSet99 = x3d.LineSet()
LineSet99.vertexCount = [2]
Coordinate100 = x3d.Coordinate()
Coordinate100.point = (0.0000,0.9149,0.0016,-0.0716,1.0190,-0.1138)

LineSet99.coord = Coordinate100
ColorRGBA101 = x3d.ColorRGBA()
ColorRGBA101.USE = "HAnimSiteLineColorRGBA"

LineSet99.color = ColorRGBA101

Shape98.geometry = LineSet99

HAnimSegment62.children.append(Shape98)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='sacroiliac'/> to <HAnimSite name='l_psis'/>
Shape102 = x3d.Shape()
LineSet103 = x3d.LineSet()
LineSet103.vertexCount = [2]
Coordinate104 = x3d.Coordinate()
Coordinate104.point = (0.0000,0.9149,0.0016,0.0774,1.0190,-0.1151)

LineSet103.coord = Coordinate104
ColorRGBA105 = x3d.ColorRGBA()
ColorRGBA105.USE = "HAnimSiteLineColorRGBA"

LineSet103.color = ColorRGBA105

Shape102.geometry = LineSet103

HAnimSegment62.children.append(Shape102)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='sacroiliac'/> to <HAnimSite name='crotch'/>
Shape106 = x3d.Shape()
LineSet107 = x3d.LineSet()
LineSet107.vertexCount = [2]
Coordinate108 = x3d.Coordinate()
Coordinate108.point = (0.0000,0.9149,0.0016,0.0034,0.8266,0.0257)

LineSet107.coord = Coordinate108
ColorRGBA109 = x3d.ColorRGBA()
ColorRGBA109.USE = "HAnimSiteLineColorRGBA"

LineSet107.color = ColorRGBA109

Shape106.geometry = LineSet107

HAnimSegment62.children.append(Shape106)
HAnimSite110 = x3d.HAnimSite()
HAnimSite110.name = "r_iliocristale_pt"
HAnimSite110.DEF = "hanim_r_iliocristale_pt"
HAnimSite110.translation = [-0.1525,1.0628,0.0035]
#HAnimSite visualization shape
TouchSensor111 = x3d.TouchSensor()
TouchSensor111.description = "HAnimSite r_iliocristale"

HAnimSite110.children.append(TouchSensor111)
Shape112 = x3d.Shape()
Shape112.DEF = "HAnimSiteShape"
IndexedFaceSet113 = x3d.IndexedFaceSet()
IndexedFaceSet113.DEF = "DiamondIFS"
IndexedFaceSet113.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet113.creaseAngle = 0.5
IndexedFaceSet113.solid = False
Coordinate114 = x3d.Coordinate()
Coordinate114.point = (0.0000,0.0080,0.0000,-0.0080,0.0000,0.0000,0.0000,0.0000,0.0080,0.0080,0.0000,0.0000,0.0000,0.0000,-0.0080,0.0000,-0.0080,0.0000)

IndexedFaceSet113.coord = Coordinate114

Shape112.geometry = IndexedFaceSet113
Appearance115 = x3d.Appearance()
Material116 = x3d.Material()
Material116.diffuseColor = [1,0,0]

Appearance115.material = Material116

Shape112.appearance = Appearance115

HAnimSite110.children.append(Shape112)

HAnimSegment62.children.append(HAnimSite110)
HAnimSite117 = x3d.HAnimSite()
HAnimSite117.name = "r_trochanterion_pt"
HAnimSite117.DEF = "hanim_r_trochanterion_pt"
HAnimSite117.translation = [-0.1689,0.8419,0.0352]
#HAnimSite visualization shape
TouchSensor118 = x3d.TouchSensor()
TouchSensor118.description = "HAnimSite r_trochanterion"

HAnimSite117.children.append(TouchSensor118)
Shape119 = x3d.Shape()
Shape119.USE = "HAnimSiteShape"

HAnimSite117.children.append(Shape119)

HAnimSegment62.children.append(HAnimSite117)
HAnimSite120 = x3d.HAnimSite()
HAnimSite120.name = "l_iliocristale_pt"
HAnimSite120.DEF = "hanim_l_iliocristale_pt"
HAnimSite120.translation = [0.1612,1.0537,0.0008]
#HAnimSite visualization shape
TouchSensor121 = x3d.TouchSensor()
TouchSensor121.description = "HAnimSite l_iliocristale"

HAnimSite120.children.append(TouchSensor121)
Shape122 = x3d.Shape()
Shape122.USE = "HAnimSiteShape"

HAnimSite120.children.append(Shape122)

HAnimSegment62.children.append(HAnimSite120)
HAnimSite123 = x3d.HAnimSite()
HAnimSite123.name = "l_trochanterion_pt"
HAnimSite123.DEF = "hanim_l_trochanterion_pt"
HAnimSite123.translation = [0.1677,0.8336,0.0303]
#HAnimSite visualization shape
TouchSensor124 = x3d.TouchSensor()
TouchSensor124.description = "HAnimSite l_trochanterion"

HAnimSite123.children.append(TouchSensor124)
Shape125 = x3d.Shape()
Shape125.USE = "HAnimSiteShape"

HAnimSite123.children.append(Shape125)

HAnimSegment62.children.append(HAnimSite123)
HAnimSite126 = x3d.HAnimSite()
HAnimSite126.name = "r_asis_pt"
HAnimSite126.DEF = "hanim_r_asis_pt"
HAnimSite126.translation = [-0.0887,1.0021,0.1112]
#HAnimSite visualization shape
TouchSensor127 = x3d.TouchSensor()
TouchSensor127.description = "HAnimSite r_asis"

HAnimSite126.children.append(TouchSensor127)
Shape128 = x3d.Shape()
Shape128.USE = "HAnimSiteShape"

HAnimSite126.children.append(Shape128)

HAnimSegment62.children.append(HAnimSite126)
HAnimSite129 = x3d.HAnimSite()
HAnimSite129.name = "l_asis_pt"
HAnimSite129.DEF = "hanim_l_asis_pt"
HAnimSite129.translation = [0.0925,0.9983,0.1052]
#HAnimSite visualization shape
TouchSensor130 = x3d.TouchSensor()
TouchSensor130.description = "HAnimSite l_asis"

HAnimSite129.children.append(TouchSensor130)
Shape131 = x3d.Shape()
Shape131.USE = "HAnimSiteShape"

HAnimSite129.children.append(Shape131)

HAnimSegment62.children.append(HAnimSite129)
HAnimSite132 = x3d.HAnimSite()
HAnimSite132.name = "r_psis_pt"
HAnimSite132.DEF = "hanim_r_psis_pt"
HAnimSite132.translation = [-0.0716,1.019,-0.1138]
#HAnimSite visualization shape
TouchSensor133 = x3d.TouchSensor()
TouchSensor133.description = "HAnimSite r_psis"

HAnimSite132.children.append(TouchSensor133)
Shape134 = x3d.Shape()
Shape134.USE = "HAnimSiteShape"

HAnimSite132.children.append(Shape134)

HAnimSegment62.children.append(HAnimSite132)
HAnimSite135 = x3d.HAnimSite()
HAnimSite135.name = "l_psis_pt"
HAnimSite135.DEF = "hanim_l_psis_pt"
HAnimSite135.translation = [0.0774,1.019,-0.1151]
#HAnimSite visualization shape
TouchSensor136 = x3d.TouchSensor()
TouchSensor136.description = "HAnimSite l_psis"

HAnimSite135.children.append(TouchSensor136)
Shape137 = x3d.Shape()
Shape137.USE = "HAnimSiteShape"

HAnimSite135.children.append(Shape137)

HAnimSegment62.children.append(HAnimSite135)
HAnimSite138 = x3d.HAnimSite()
HAnimSite138.name = "crotch_pt"
HAnimSite138.DEF = "hanim_crotch_pt"
HAnimSite138.translation = [0.0034,0.8266,0.0257]
#HAnimSite visualization shape
TouchSensor139 = x3d.TouchSensor()
TouchSensor139.description = "HAnimSite crotch"

HAnimSite138.children.append(TouchSensor139)
Shape140 = x3d.Shape()
Shape140.USE = "HAnimSiteShape"

HAnimSite138.children.append(Shape140)

HAnimSegment62.children.append(HAnimSite138)

HAnimJoint61.children.append(HAnimSegment62)
HAnimJoint141 = x3d.HAnimJoint()
HAnimJoint141.name = "l_hip"
HAnimJoint141.DEF = "hanim_l_hip"
HAnimJoint141.center = [0.0961,0.9124,-0.0001]
HAnimJoint141.ulimit = [0,0,0]
HAnimJoint141.llimit = [0,0,0]
HAnimSegment142 = x3d.HAnimSegment()
HAnimSegment142.name = "l_thigh"
HAnimSegment142.DEF = "hanim_l_thigh"
#<HAnimJoint name='l_hip'/> visualization sphere within <HAnimSegment name='l_thigh'/>
TouchSensor143 = x3d.TouchSensor()
TouchSensor143.description = "HAnimJoint l_hip, HAnimSegment l_thigh"

HAnimSegment142.children.append(TouchSensor143)
Transform144 = x3d.Transform()
Transform144.translation = [0.0961,0.9124,-0.0001]
Shape145 = x3d.Shape()
Shape145.USE = "HAnimJointShape"

Transform144.children.append(Shape145)

HAnimSegment142.children.append(Transform144)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_hip'/> to <HAnimJoint name='l_knee'/>
Shape146 = x3d.Shape()
LineSet147 = x3d.LineSet()
LineSet147.vertexCount = [2]
Coordinate148 = x3d.Coordinate()
Coordinate148.point = (0.0961,0.9124,-0.0001,0.1040,0.4867,0.0308)

LineSet147.coord = Coordinate148
ColorRGBA149 = x3d.ColorRGBA()
ColorRGBA149.USE = "HAnimSegmentLineColorRGBA"

LineSet147.color = ColorRGBA149

Shape146.geometry = LineSet147

HAnimSegment142.children.append(Shape146)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_hip'/> to <HAnimSite name='l_knee_crease'/>
Shape150 = x3d.Shape()
LineSet151 = x3d.LineSet()
LineSet151.vertexCount = [2]
Coordinate152 = x3d.Coordinate()
Coordinate152.point = (0.0961,0.9124,-0.0001,0.0993,0.4881,-0.0309)

LineSet151.coord = Coordinate152
ColorRGBA153 = x3d.ColorRGBA()
ColorRGBA153.USE = "HAnimSiteLineColorRGBA"

LineSet151.color = ColorRGBA153

Shape150.geometry = LineSet151

HAnimSegment142.children.append(Shape150)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_hip'/> to <HAnimSite name='l_femoral_lateral_epicn'/>
Shape154 = x3d.Shape()
LineSet155 = x3d.LineSet()
LineSet155.vertexCount = [2]
Coordinate156 = x3d.Coordinate()
Coordinate156.point = (0.0961,0.9124,-0.0001,0.1598,0.4967,0.0297)

LineSet155.coord = Coordinate156
ColorRGBA157 = x3d.ColorRGBA()
ColorRGBA157.USE = "HAnimSiteLineColorRGBA"

LineSet155.color = ColorRGBA157

Shape154.geometry = LineSet155

HAnimSegment142.children.append(Shape154)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_hip'/> to <HAnimSite name='l_femoral_medial_epicn'/>
Shape158 = x3d.Shape()
LineSet159 = x3d.LineSet()
LineSet159.vertexCount = [2]
Coordinate160 = x3d.Coordinate()
Coordinate160.point = (0.0961,0.9124,-0.0001,0.0398,0.4946,0.0303)

LineSet159.coord = Coordinate160
ColorRGBA161 = x3d.ColorRGBA()
ColorRGBA161.USE = "HAnimSiteLineColorRGBA"

LineSet159.color = ColorRGBA161

Shape158.geometry = LineSet159

HAnimSegment142.children.append(Shape158)
HAnimSite162 = x3d.HAnimSite()
HAnimSite162.name = "l_knee_crease_pt"
HAnimSite162.DEF = "hanim_l_knee_crease_pt"
HAnimSite162.translation = [0.0993,0.4881,-0.0309]
#HAnimSite visualization shape
TouchSensor163 = x3d.TouchSensor()
TouchSensor163.description = "HAnimSite l_knee_crease"

HAnimSite162.children.append(TouchSensor163)
Shape164 = x3d.Shape()
Shape164.USE = "HAnimSiteShape"

HAnimSite162.children.append(Shape164)

HAnimSegment142.children.append(HAnimSite162)
HAnimSite165 = x3d.HAnimSite()
HAnimSite165.name = "l_femoral_lateral_epicn_pt"
HAnimSite165.DEF = "hanim_l_femoral_lateral_epicn_pt"
HAnimSite165.translation = [0.1598,0.4967,0.0297]
#HAnimSite visualization shape
TouchSensor166 = x3d.TouchSensor()
TouchSensor166.description = "HAnimSite l_femoral_lateral_epicn"

HAnimSite165.children.append(TouchSensor166)
Shape167 = x3d.Shape()
Shape167.USE = "HAnimSiteShape"

HAnimSite165.children.append(Shape167)

HAnimSegment142.children.append(HAnimSite165)
HAnimSite168 = x3d.HAnimSite()
HAnimSite168.name = "l_femoral_medial_epicn_pt"
HAnimSite168.DEF = "hanim_l_femoral_medial_epicn_pt"
HAnimSite168.translation = [0.0398,0.4946,0.0303]
#HAnimSite visualization shape
TouchSensor169 = x3d.TouchSensor()
TouchSensor169.description = "HAnimSite l_femoral_medial_epicn"

HAnimSite168.children.append(TouchSensor169)
Shape170 = x3d.Shape()
Shape170.USE = "HAnimSiteShape"

HAnimSite168.children.append(Shape170)

HAnimSegment142.children.append(HAnimSite168)

HAnimJoint141.children.append(HAnimSegment142)
HAnimJoint171 = x3d.HAnimJoint()
HAnimJoint171.name = "l_knee"
HAnimJoint171.DEF = "hanim_l_knee"
HAnimJoint171.center = [0.104,0.4867,0.0308]
HAnimJoint171.ulimit = [0,0,0]
HAnimJoint171.llimit = [0,0,0]
HAnimSegment172 = x3d.HAnimSegment()
HAnimSegment172.name = "l_calf"
HAnimSegment172.DEF = "hanim_l_calf"
#<HAnimJoint name='l_knee'/> visualization sphere within <HAnimSegment name='l_calf'/>
TouchSensor173 = x3d.TouchSensor()
TouchSensor173.description = "HAnimJoint l_knee, HAnimSegment l_calf"

HAnimSegment172.children.append(TouchSensor173)
Transform174 = x3d.Transform()
Transform174.translation = [0.104,0.4867,0.0308]
Shape175 = x3d.Shape()
Shape175.USE = "HAnimJointShape"

Transform174.children.append(Shape175)

HAnimSegment172.children.append(Transform174)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_knee'/> to <HAnimJoint name='l_ankle'/>
Shape176 = x3d.Shape()
LineSet177 = x3d.LineSet()
LineSet177.vertexCount = [2]
Coordinate178 = x3d.Coordinate()
Coordinate178.point = (0.1040,0.4867,0.0308,0.1101,0.0656,-0.0736)

LineSet177.coord = Coordinate178
ColorRGBA179 = x3d.ColorRGBA()
ColorRGBA179.USE = "HAnimSegmentLineColorRGBA"

LineSet177.color = ColorRGBA179

Shape176.geometry = LineSet177

HAnimSegment172.children.append(Shape176)

HAnimJoint171.children.append(HAnimSegment172)
HAnimJoint180 = x3d.HAnimJoint()
HAnimJoint180.name = "l_ankle"
HAnimJoint180.DEF = "hanim_l_ankle"
HAnimJoint180.center = [0.1101,0.0656,-0.0736]
HAnimJoint180.ulimit = [0,0,0]
HAnimJoint180.llimit = [0,0,0]
HAnimSegment181 = x3d.HAnimSegment()
HAnimSegment181.name = "l_hindfoot"
HAnimSegment181.DEF = "hanim_l_hindfoot"
#<HAnimJoint name='l_ankle'/> visualization sphere within <HAnimSegment name='l_hindfoot'/>
TouchSensor182 = x3d.TouchSensor()
TouchSensor182.description = "HAnimJoint l_ankle, HAnimSegment l_hindfoot"

HAnimSegment181.children.append(TouchSensor182)
Transform183 = x3d.Transform()
Transform183.translation = [0.1101,0.0656,-0.0736]
Shape184 = x3d.Shape()
Shape184.USE = "HAnimJointShape"

Transform183.children.append(Shape184)

HAnimSegment181.children.append(Transform183)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_ankle'/> to <HAnimJoint name='l_subtalar'/>
Shape185 = x3d.Shape()
LineSet186 = x3d.LineSet()
LineSet186.vertexCount = [2]
Coordinate187 = x3d.Coordinate()
Coordinate187.point = (0.1101,0.0656,-0.0736,0.1086,0.0001,-0.0368)

LineSet186.coord = Coordinate187
ColorRGBA188 = x3d.ColorRGBA()
ColorRGBA188.USE = "HAnimSegmentLineColorRGBA"

LineSet186.color = ColorRGBA188

Shape185.geometry = LineSet186

HAnimSegment181.children.append(Shape185)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_ankle'/> to <HAnimSite name='l_lateral_malleolus'/>
Shape189 = x3d.Shape()
LineSet190 = x3d.LineSet()
LineSet190.vertexCount = [2]
Coordinate191 = x3d.Coordinate()
Coordinate191.point = (0.1101,0.0656,-0.0736,0.1308,0.0597,-0.1032)

LineSet190.coord = Coordinate191
ColorRGBA192 = x3d.ColorRGBA()
ColorRGBA192.USE = "HAnimSiteLineColorRGBA"

LineSet190.color = ColorRGBA192

Shape189.geometry = LineSet190

HAnimSegment181.children.append(Shape189)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_ankle'/> to <HAnimSite name='l_medial_malleolus'/>
Shape193 = x3d.Shape()
LineSet194 = x3d.LineSet()
LineSet194.vertexCount = [2]
Coordinate195 = x3d.Coordinate()
Coordinate195.point = (0.1101,0.0656,-0.0736,0.0890,0.0716,-0.0881)

LineSet194.coord = Coordinate195
ColorRGBA196 = x3d.ColorRGBA()
ColorRGBA196.USE = "HAnimSiteLineColorRGBA"

LineSet194.color = ColorRGBA196

Shape193.geometry = LineSet194

HAnimSegment181.children.append(Shape193)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_ankle'/> to <HAnimSite name='l_sphyrion'/>
Shape197 = x3d.Shape()
LineSet198 = x3d.LineSet()
LineSet198.vertexCount = [2]
Coordinate199 = x3d.Coordinate()
Coordinate199.point = (0.1101,0.0656,-0.0736,0.0890,0.0575,-0.0943)

LineSet198.coord = Coordinate199
ColorRGBA200 = x3d.ColorRGBA()
ColorRGBA200.USE = "HAnimSiteLineColorRGBA"

LineSet198.color = ColorRGBA200

Shape197.geometry = LineSet198

HAnimSegment181.children.append(Shape197)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_ankle'/> to <HAnimSite name='l_calcaneous_post'/>
Shape201 = x3d.Shape()
LineSet202 = x3d.LineSet()
LineSet202.vertexCount = [2]
Coordinate203 = x3d.Coordinate()
Coordinate203.point = (0.1101,0.0656,-0.0736,0.0974,0.0259,-0.1171)

LineSet202.coord = Coordinate203
ColorRGBA204 = x3d.ColorRGBA()
ColorRGBA204.USE = "HAnimSiteLineColorRGBA"

LineSet202.color = ColorRGBA204

Shape201.geometry = LineSet202

HAnimSegment181.children.append(Shape201)
HAnimSite205 = x3d.HAnimSite()
HAnimSite205.name = "l_lateral_malleolus_pt"
HAnimSite205.DEF = "hanim_l_lateral_malleolus_pt"
HAnimSite205.translation = [0.1308,0.0597,-0.1032]
#HAnimSite visualization shape
TouchSensor206 = x3d.TouchSensor()
TouchSensor206.description = "HAnimSite l_lateral_malleolus"

HAnimSite205.children.append(TouchSensor206)
Shape207 = x3d.Shape()
Shape207.USE = "HAnimSiteShape"

HAnimSite205.children.append(Shape207)

HAnimSegment181.children.append(HAnimSite205)
HAnimSite208 = x3d.HAnimSite()
HAnimSite208.name = "l_medial_malleolus_pt"
HAnimSite208.DEF = "hanim_l_medial_malleolus_pt"
HAnimSite208.translation = [0.089,0.0716,-0.0881]
#HAnimSite visualization shape
TouchSensor209 = x3d.TouchSensor()
TouchSensor209.description = "HAnimSite l_medial_malleolus"

HAnimSite208.children.append(TouchSensor209)
Shape210 = x3d.Shape()
Shape210.USE = "HAnimSiteShape"

HAnimSite208.children.append(Shape210)

HAnimSegment181.children.append(HAnimSite208)
HAnimSite211 = x3d.HAnimSite()
HAnimSite211.name = "l_sphyrion_pt"
HAnimSite211.DEF = "hanim_l_sphyrion_pt"
HAnimSite211.translation = [0.089,0.0575,-0.0943]
#HAnimSite visualization shape
TouchSensor212 = x3d.TouchSensor()
TouchSensor212.description = "HAnimSite l_sphyrion"

HAnimSite211.children.append(TouchSensor212)
Shape213 = x3d.Shape()
Shape213.USE = "HAnimSiteShape"

HAnimSite211.children.append(Shape213)

HAnimSegment181.children.append(HAnimSite211)
HAnimSite214 = x3d.HAnimSite()
HAnimSite214.name = "l_calcaneous_post_pt"
HAnimSite214.DEF = "hanim_l_calcaneous_post_pt"
HAnimSite214.translation = [0.0974,0.0259,-0.1171]
#HAnimSite visualization shape
TouchSensor215 = x3d.TouchSensor()
TouchSensor215.description = "HAnimSite l_calcaneous_post"

HAnimSite214.children.append(TouchSensor215)
Shape216 = x3d.Shape()
Shape216.USE = "HAnimSiteShape"

HAnimSite214.children.append(Shape216)

HAnimSegment181.children.append(HAnimSite214)

HAnimJoint180.children.append(HAnimSegment181)
HAnimJoint217 = x3d.HAnimJoint()
HAnimJoint217.name = "l_subtalar"
HAnimJoint217.DEF = "hanim_l_subtalar"
HAnimJoint217.center = [0.1086,0.0001,-0.0368]
HAnimJoint217.ulimit = [0,0,0]
HAnimJoint217.llimit = [0,0,0]
HAnimSegment218 = x3d.HAnimSegment()
HAnimSegment218.name = "l_midproximal"
HAnimSegment218.DEF = "hanim_l_midproximal"
#<HAnimJoint name='l_subtalar'/> visualization sphere within <HAnimSegment name='l_midproximal'/>
TouchSensor219 = x3d.TouchSensor()
TouchSensor219.description = "HAnimJoint l_subtalar, HAnimSegment l_midproximal"

HAnimSegment218.children.append(TouchSensor219)
Transform220 = x3d.Transform()
Transform220.translation = [0.1086,0.0001,-0.0368]
Shape221 = x3d.Shape()
Shape221.USE = "HAnimJointShape"

Transform220.children.append(Shape221)

HAnimSegment218.children.append(Transform220)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_subtalar'/> to <HAnimJoint name='l_midtarsal'/>
Shape222 = x3d.Shape()
LineSet223 = x3d.LineSet()
LineSet223.vertexCount = [2]
Coordinate224 = x3d.Coordinate()
Coordinate224.point = (0.1086,0.0001,-0.0368,0.1086,0.0001,0.0368)

LineSet223.coord = Coordinate224
ColorRGBA225 = x3d.ColorRGBA()
ColorRGBA225.USE = "HAnimSegmentLineColorRGBA"

LineSet223.color = ColorRGBA225

Shape222.geometry = LineSet223

HAnimSegment218.children.append(Shape222)

HAnimJoint217.children.append(HAnimSegment218)
HAnimJoint226 = x3d.HAnimJoint()
HAnimJoint226.name = "l_midtarsal"
HAnimJoint226.DEF = "hanim_l_midtarsal"
HAnimJoint226.center = [0.1086,0.0001,0.0368]
HAnimJoint226.ulimit = [0,0,0]
HAnimJoint226.llimit = [0,0,0]
HAnimSegment227 = x3d.HAnimSegment()
HAnimSegment227.name = "l_middistal"
HAnimSegment227.DEF = "hanim_l_middistal"
#<HAnimJoint name='l_midtarsal'/> visualization sphere within <HAnimSegment name='l_middistal'/>
TouchSensor228 = x3d.TouchSensor()
TouchSensor228.description = "HAnimJoint l_midtarsal, HAnimSegment l_middistal"

HAnimSegment227.children.append(TouchSensor228)
Transform229 = x3d.Transform()
Transform229.translation = [0.1086,0.0001,0.0368]
Shape230 = x3d.Shape()
Shape230.USE = "HAnimJointShape"

Transform229.children.append(Shape230)

HAnimSegment227.children.append(Transform229)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_midtarsal'/> to <HAnimJoint name='l_metatarsal'/>
Shape231 = x3d.Shape()
LineSet232 = x3d.LineSet()
LineSet232.vertexCount = [2]
Coordinate233 = x3d.Coordinate()
Coordinate233.point = (0.1086,0.0001,0.0368,0.1086,0.0000,0.0762)

LineSet232.coord = Coordinate233
ColorRGBA234 = x3d.ColorRGBA()
ColorRGBA234.USE = "HAnimSegmentLineColorRGBA"

LineSet232.color = ColorRGBA234

Shape231.geometry = LineSet232

HAnimSegment227.children.append(Shape231)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_midtarsal'/> to <HAnimSite name='l_metatarsal_pha1'/>
Shape235 = x3d.Shape()
LineSet236 = x3d.LineSet()
LineSet236.vertexCount = [2]
Coordinate237 = x3d.Coordinate()
Coordinate237.point = (0.1086,0.0001,0.0368,0.0816,0.0232,0.0106)

LineSet236.coord = Coordinate237
ColorRGBA238 = x3d.ColorRGBA()
ColorRGBA238.USE = "HAnimSiteLineColorRGBA"

LineSet236.color = ColorRGBA238

Shape235.geometry = LineSet236

HAnimSegment227.children.append(Shape235)
HAnimSite239 = x3d.HAnimSite()
HAnimSite239.name = "l_metatarsal_pha1_pt"
HAnimSite239.DEF = "hanim_l_metatarsal_pha1_pt"
HAnimSite239.translation = [0.0816,0.0232,0.0106]
#HAnimSite visualization shape
TouchSensor240 = x3d.TouchSensor()
TouchSensor240.description = "HAnimSite l_metatarsal_pha1"

HAnimSite239.children.append(TouchSensor240)
Shape241 = x3d.Shape()
Shape241.USE = "HAnimSiteShape"

HAnimSite239.children.append(Shape241)

HAnimSegment227.children.append(HAnimSite239)

HAnimJoint226.children.append(HAnimSegment227)
HAnimJoint242 = x3d.HAnimJoint()
HAnimJoint242.name = "l_metatarsal"
HAnimJoint242.DEF = "hanim_l_metatarsal"
HAnimJoint242.center = [0.1086,0,0.0762]
HAnimJoint242.ulimit = [0,0,0]
HAnimJoint242.llimit = [0,0,0]
HAnimSegment243 = x3d.HAnimSegment()
HAnimSegment243.name = "l_forefoot"
HAnimSegment243.DEF = "hanim_l_forefoot"
#<HAnimJoint name='l_metatarsal'/> visualization sphere within <HAnimSegment name='l_forefoot'/>
TouchSensor244 = x3d.TouchSensor()
TouchSensor244.description = "HAnimJoint l_metatarsal, HAnimSegment l_forefoot"

HAnimSegment243.children.append(TouchSensor244)
Transform245 = x3d.Transform()
Transform245.translation = [0.1086,0,0.0762]
Shape246 = x3d.Shape()
Shape246.USE = "HAnimJointShape"

Transform245.children.append(Shape246)

HAnimSegment243.children.append(Transform245)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_metatarsal'/> to <HAnimSite name='l_forefoot_tip'/>
Shape247 = x3d.Shape()
LineSet248 = x3d.LineSet()
LineSet248.vertexCount = [2]
Coordinate249 = x3d.Coordinate()
Coordinate249.point = (0.1086,0.0000,0.0762,0.1354,0.0016,0.1476)

LineSet248.coord = Coordinate249
ColorRGBA250 = x3d.ColorRGBA()
ColorRGBA250.USE = "HAnimSiteLineColorRGBA"

LineSet248.color = ColorRGBA250

Shape247.geometry = LineSet248

HAnimSegment243.children.append(Shape247)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_metatarsal'/> to <HAnimSite name='l_metatarsal_pha5'/>
Shape251 = x3d.Shape()
LineSet252 = x3d.LineSet()
LineSet252.vertexCount = [2]
Coordinate253 = x3d.Coordinate()
Coordinate253.point = (0.1086,0.0000,0.0762,0.1825,0.0070,0.0928)

LineSet252.coord = Coordinate253
ColorRGBA254 = x3d.ColorRGBA()
ColorRGBA254.USE = "HAnimSiteLineColorRGBA"

LineSet252.color = ColorRGBA254

Shape251.geometry = LineSet252

HAnimSegment243.children.append(Shape251)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_metatarsal'/> to <HAnimSite name='l_digit2'/>
Shape255 = x3d.Shape()
LineSet256 = x3d.LineSet()
LineSet256.vertexCount = [2]
Coordinate257 = x3d.Coordinate()
Coordinate257.point = (0.1086,0.0000,0.0762,0.1195,0.0079,0.1433)

LineSet256.coord = Coordinate257
ColorRGBA258 = x3d.ColorRGBA()
ColorRGBA258.USE = "HAnimSiteLineColorRGBA"

LineSet256.color = ColorRGBA258

Shape255.geometry = LineSet256

HAnimSegment243.children.append(Shape255)
HAnimSite259 = x3d.HAnimSite()
HAnimSite259.name = "l_forefoot_tip"
HAnimSite259.DEF = "hanim_l_forefoot_tip"
HAnimSite259.translation = [0.1354,0.0016,0.1476]
#HAnimSite visualization shape
TouchSensor260 = x3d.TouchSensor()
TouchSensor260.description = "HAnimSite l_forefoot_tip"

HAnimSite259.children.append(TouchSensor260)
Shape261 = x3d.Shape()
Shape261.USE = "HAnimSiteShape"

HAnimSite259.children.append(Shape261)

HAnimSegment243.children.append(HAnimSite259)
HAnimSite262 = x3d.HAnimSite()
HAnimSite262.name = "l_metatarsal_pha5_pt"
HAnimSite262.DEF = "hanim_l_metatarsal_pha5_pt"
HAnimSite262.translation = [0.1825,0.007,0.0928]
#HAnimSite visualization shape
TouchSensor263 = x3d.TouchSensor()
TouchSensor263.description = "HAnimSite l_metatarsal_pha5"

HAnimSite262.children.append(TouchSensor263)
Shape264 = x3d.Shape()
Shape264.USE = "HAnimSiteShape"

HAnimSite262.children.append(Shape264)

HAnimSegment243.children.append(HAnimSite262)
HAnimSite265 = x3d.HAnimSite()
HAnimSite265.name = "l_digit2_pt"
HAnimSite265.DEF = "hanim_l_digit2_pt"
HAnimSite265.translation = [0.1195,0.0079,0.1433]
#HAnimSite visualization shape
TouchSensor266 = x3d.TouchSensor()
TouchSensor266.description = "HAnimSite l_digit2"

HAnimSite265.children.append(TouchSensor266)
Shape267 = x3d.Shape()
Shape267.USE = "HAnimSiteShape"

HAnimSite265.children.append(Shape267)

HAnimSegment243.children.append(HAnimSite265)

HAnimJoint242.children.append(HAnimSegment243)

HAnimJoint226.children.append(HAnimJoint242)

HAnimJoint217.children.append(HAnimJoint226)

HAnimJoint180.children.append(HAnimJoint217)

HAnimJoint171.children.append(HAnimJoint180)

HAnimJoint141.children.append(HAnimJoint171)

HAnimJoint61.children.append(HAnimJoint141)
HAnimJoint268 = x3d.HAnimJoint()
HAnimJoint268.name = "r_hip"
HAnimJoint268.DEF = "hanim_r_hip"
HAnimJoint268.center = [-0.0961,0.9124,-0.0001]
HAnimJoint268.ulimit = [0,0,0]
HAnimJoint268.llimit = [0,0,0]
HAnimSegment269 = x3d.HAnimSegment()
HAnimSegment269.name = "r_thigh"
HAnimSegment269.DEF = "hanim_r_thigh"
#<HAnimJoint name='r_hip'/> visualization sphere within <HAnimSegment name='r_thigh'/>
TouchSensor270 = x3d.TouchSensor()
TouchSensor270.description = "HAnimJoint r_hip, HAnimSegment r_thigh"

HAnimSegment269.children.append(TouchSensor270)
Transform271 = x3d.Transform()
Transform271.translation = [-0.0961,0.9124,-0.0001]
Shape272 = x3d.Shape()
Shape272.USE = "HAnimJointShape"

Transform271.children.append(Shape272)

HAnimSegment269.children.append(Transform271)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_hip'/> to <HAnimJoint name='r_knee'/>
Shape273 = x3d.Shape()
LineSet274 = x3d.LineSet()
LineSet274.vertexCount = [2]
Coordinate275 = x3d.Coordinate()
Coordinate275.point = (-0.0961,0.9124,-0.0001,-0.1040,0.4867,0.0308)

LineSet274.coord = Coordinate275
ColorRGBA276 = x3d.ColorRGBA()
ColorRGBA276.USE = "HAnimSegmentLineColorRGBA"

LineSet274.color = ColorRGBA276

Shape273.geometry = LineSet274

HAnimSegment269.children.append(Shape273)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_hip'/> to <HAnimSite name='r_knee_crease'/>
Shape277 = x3d.Shape()
LineSet278 = x3d.LineSet()
LineSet278.vertexCount = [2]
Coordinate279 = x3d.Coordinate()
Coordinate279.point = (-0.0961,0.9124,-0.0001,-0.0825,0.4932,-0.0326)

LineSet278.coord = Coordinate279
ColorRGBA280 = x3d.ColorRGBA()
ColorRGBA280.USE = "HAnimSiteLineColorRGBA"

LineSet278.color = ColorRGBA280

Shape277.geometry = LineSet278

HAnimSegment269.children.append(Shape277)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_hip'/> to <HAnimSite name='r_femoral_lateral_epicn'/>
Shape281 = x3d.Shape()
LineSet282 = x3d.LineSet()
LineSet282.vertexCount = [2]
Coordinate283 = x3d.Coordinate()
Coordinate283.point = (-0.0961,0.9124,-0.0001,-0.1421,0.4992,0.0310)

LineSet282.coord = Coordinate283
ColorRGBA284 = x3d.ColorRGBA()
ColorRGBA284.USE = "HAnimSiteLineColorRGBA"

LineSet282.color = ColorRGBA284

Shape281.geometry = LineSet282

HAnimSegment269.children.append(Shape281)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_hip'/> to <HAnimSite name='r_femoral_medial_epicn'/>
Shape285 = x3d.Shape()
LineSet286 = x3d.LineSet()
LineSet286.vertexCount = [2]
Coordinate287 = x3d.Coordinate()
Coordinate287.point = (-0.0961,0.9124,-0.0001,-0.0221,0.5014,0.0289)

LineSet286.coord = Coordinate287
ColorRGBA288 = x3d.ColorRGBA()
ColorRGBA288.USE = "HAnimSiteLineColorRGBA"

LineSet286.color = ColorRGBA288

Shape285.geometry = LineSet286

HAnimSegment269.children.append(Shape285)
HAnimSite289 = x3d.HAnimSite()
HAnimSite289.name = "r_knee_crease_pt"
HAnimSite289.DEF = "hanim_r_knee_crease_pt"
HAnimSite289.translation = [-0.0825,0.4932,-0.0326]
#HAnimSite visualization shape
TouchSensor290 = x3d.TouchSensor()
TouchSensor290.description = "HAnimSite r_knee_crease"

HAnimSite289.children.append(TouchSensor290)
Shape291 = x3d.Shape()
Shape291.USE = "HAnimSiteShape"

HAnimSite289.children.append(Shape291)

HAnimSegment269.children.append(HAnimSite289)
HAnimSite292 = x3d.HAnimSite()
HAnimSite292.name = "r_femoral_lateral_epicn_pt"
HAnimSite292.DEF = "hanim_r_femoral_lateral_epicn_pt"
HAnimSite292.translation = [-0.1421,0.4992,0.031]
#HAnimSite visualization shape
TouchSensor293 = x3d.TouchSensor()
TouchSensor293.description = "HAnimSite r_femoral_lateral_epicn"

HAnimSite292.children.append(TouchSensor293)
Shape294 = x3d.Shape()
Shape294.USE = "HAnimSiteShape"

HAnimSite292.children.append(Shape294)

HAnimSegment269.children.append(HAnimSite292)
HAnimSite295 = x3d.HAnimSite()
HAnimSite295.name = "r_femoral_medial_epicn_pt"
HAnimSite295.DEF = "hanim_r_femoral_medial_epicn_pt"
HAnimSite295.translation = [-0.0221,0.5014,0.0289]
#HAnimSite visualization shape
TouchSensor296 = x3d.TouchSensor()
TouchSensor296.description = "HAnimSite r_femoral_medial_epicn"

HAnimSite295.children.append(TouchSensor296)
Shape297 = x3d.Shape()
Shape297.USE = "HAnimSiteShape"

HAnimSite295.children.append(Shape297)

HAnimSegment269.children.append(HAnimSite295)

HAnimJoint268.children.append(HAnimSegment269)
HAnimJoint298 = x3d.HAnimJoint()
HAnimJoint298.name = "r_knee"
HAnimJoint298.DEF = "hanim_r_knee"
HAnimJoint298.center = [-0.104,0.4867,0.0308]
HAnimJoint298.ulimit = [0,0,0]
HAnimJoint298.llimit = [0,0,0]
HAnimSegment299 = x3d.HAnimSegment()
HAnimSegment299.name = "r_calf"
HAnimSegment299.DEF = "hanim_r_calf"
#<HAnimJoint name='r_knee'/> visualization sphere within <HAnimSegment name='r_calf'/>
TouchSensor300 = x3d.TouchSensor()
TouchSensor300.description = "HAnimJoint r_knee, HAnimSegment r_calf"

HAnimSegment299.children.append(TouchSensor300)
Transform301 = x3d.Transform()
Transform301.translation = [-0.104,0.4867,0.0308]
Shape302 = x3d.Shape()
Shape302.USE = "HAnimJointShape"

Transform301.children.append(Shape302)

HAnimSegment299.children.append(Transform301)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_knee'/> to <HAnimJoint name='r_ankle'/>
Shape303 = x3d.Shape()
LineSet304 = x3d.LineSet()
LineSet304.vertexCount = [2]
Coordinate305 = x3d.Coordinate()
Coordinate305.point = (-0.1040,0.4867,0.0308,-0.1101,0.0656,-0.0736)

LineSet304.coord = Coordinate305
ColorRGBA306 = x3d.ColorRGBA()
ColorRGBA306.USE = "HAnimSegmentLineColorRGBA"

LineSet304.color = ColorRGBA306

Shape303.geometry = LineSet304

HAnimSegment299.children.append(Shape303)

HAnimJoint298.children.append(HAnimSegment299)
HAnimJoint307 = x3d.HAnimJoint()
HAnimJoint307.name = "r_ankle"
HAnimJoint307.DEF = "hanim_r_ankle"
HAnimJoint307.center = [-0.1101,0.0656,-0.0736]
HAnimJoint307.ulimit = [0,0,0]
HAnimJoint307.llimit = [0,0,0]
HAnimSegment308 = x3d.HAnimSegment()
HAnimSegment308.name = "r_hindfoot"
HAnimSegment308.DEF = "hanim_r_hindfoot"
#<HAnimJoint name='r_ankle'/> visualization sphere within <HAnimSegment name='r_hindfoot'/>
TouchSensor309 = x3d.TouchSensor()
TouchSensor309.description = "HAnimJoint r_ankle, HAnimSegment r_hindfoot"

HAnimSegment308.children.append(TouchSensor309)
Transform310 = x3d.Transform()
Transform310.translation = [-0.1101,0.0656,-0.0736]
Shape311 = x3d.Shape()
Shape311.USE = "HAnimJointShape"

Transform310.children.append(Shape311)

HAnimSegment308.children.append(Transform310)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_ankle'/> to <HAnimJoint name='r_subtalar'/>
Shape312 = x3d.Shape()
LineSet313 = x3d.LineSet()
LineSet313.vertexCount = [2]
Coordinate314 = x3d.Coordinate()
Coordinate314.point = (-0.1101,0.0656,-0.0736,-0.1086,0.0001,-0.0368)

LineSet313.coord = Coordinate314
ColorRGBA315 = x3d.ColorRGBA()
ColorRGBA315.USE = "HAnimSegmentLineColorRGBA"

LineSet313.color = ColorRGBA315

Shape312.geometry = LineSet313

HAnimSegment308.children.append(Shape312)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_ankle'/> to <HAnimSite name='r_lateral_malleolus'/>
Shape316 = x3d.Shape()
LineSet317 = x3d.LineSet()
LineSet317.vertexCount = [2]
Coordinate318 = x3d.Coordinate()
Coordinate318.point = (-0.1101,0.0656,-0.0736,-0.1006,0.0658,-0.1075)

LineSet317.coord = Coordinate318
ColorRGBA319 = x3d.ColorRGBA()
ColorRGBA319.USE = "HAnimSiteLineColorRGBA"

LineSet317.color = ColorRGBA319

Shape316.geometry = LineSet317

HAnimSegment308.children.append(Shape316)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_ankle'/> to <HAnimSite name='r_medial_malleolus'/>
Shape320 = x3d.Shape()
LineSet321 = x3d.LineSet()
LineSet321.vertexCount = [2]
Coordinate322 = x3d.Coordinate()
Coordinate322.point = (-0.1101,0.0656,-0.0736,-0.0591,0.0760,-0.0928)

LineSet321.coord = Coordinate322
ColorRGBA323 = x3d.ColorRGBA()
ColorRGBA323.USE = "HAnimSiteLineColorRGBA"

LineSet321.color = ColorRGBA323

Shape320.geometry = LineSet321

HAnimSegment308.children.append(Shape320)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_ankle'/> to <HAnimSite name='r_sphyrion'/>
Shape324 = x3d.Shape()
LineSet325 = x3d.LineSet()
LineSet325.vertexCount = [2]
Coordinate326 = x3d.Coordinate()
Coordinate326.point = (-0.1101,0.0656,-0.0736,-0.0603,0.0610,-0.1002)

LineSet325.coord = Coordinate326
ColorRGBA327 = x3d.ColorRGBA()
ColorRGBA327.USE = "HAnimSiteLineColorRGBA"

LineSet325.color = ColorRGBA327

Shape324.geometry = LineSet325

HAnimSegment308.children.append(Shape324)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_ankle'/> to <HAnimSite name='r_calcaneous_post'/>
Shape328 = x3d.Shape()
LineSet329 = x3d.LineSet()
LineSet329.vertexCount = [2]
Coordinate330 = x3d.Coordinate()
Coordinate330.point = (-0.1101,0.0656,-0.0736,-0.0692,0.0297,-0.1221)

LineSet329.coord = Coordinate330
ColorRGBA331 = x3d.ColorRGBA()
ColorRGBA331.USE = "HAnimSiteLineColorRGBA"

LineSet329.color = ColorRGBA331

Shape328.geometry = LineSet329

HAnimSegment308.children.append(Shape328)
HAnimSite332 = x3d.HAnimSite()
HAnimSite332.name = "r_lateral_malleolus_pt"
HAnimSite332.DEF = "hanim_r_lateral_malleolus_pt"
HAnimSite332.translation = [-0.1006,0.0658,-0.1075]
#HAnimSite visualization shape
TouchSensor333 = x3d.TouchSensor()
TouchSensor333.description = "HAnimSite r_lateral_malleolus"

HAnimSite332.children.append(TouchSensor333)
Shape334 = x3d.Shape()
Shape334.USE = "HAnimSiteShape"

HAnimSite332.children.append(Shape334)

HAnimSegment308.children.append(HAnimSite332)
HAnimSite335 = x3d.HAnimSite()
HAnimSite335.name = "r_medial_malleolus_pt"
HAnimSite335.DEF = "hanim_r_medial_malleolus_pt"
HAnimSite335.translation = [-0.0591,0.076,-0.0928]
#HAnimSite visualization shape
TouchSensor336 = x3d.TouchSensor()
TouchSensor336.description = "HAnimSite r_medial_malleolus"

HAnimSite335.children.append(TouchSensor336)
Shape337 = x3d.Shape()
Shape337.USE = "HAnimSiteShape"

HAnimSite335.children.append(Shape337)

HAnimSegment308.children.append(HAnimSite335)
HAnimSite338 = x3d.HAnimSite()
HAnimSite338.name = "r_sphyrion_pt"
HAnimSite338.DEF = "hanim_r_sphyrion_pt"
HAnimSite338.translation = [-0.0603,0.061,-0.1002]
#HAnimSite visualization shape
TouchSensor339 = x3d.TouchSensor()
TouchSensor339.description = "HAnimSite r_sphyrion"

HAnimSite338.children.append(TouchSensor339)
Shape340 = x3d.Shape()
Shape340.USE = "HAnimSiteShape"

HAnimSite338.children.append(Shape340)

HAnimSegment308.children.append(HAnimSite338)
HAnimSite341 = x3d.HAnimSite()
HAnimSite341.name = "r_calcaneous_post_pt"
HAnimSite341.DEF = "hanim_r_calcaneous_post_pt"
HAnimSite341.translation = [-0.0692,0.0297,-0.1221]
#HAnimSite visualization shape
TouchSensor342 = x3d.TouchSensor()
TouchSensor342.description = "HAnimSite r_calcaneous_post"

HAnimSite341.children.append(TouchSensor342)
Shape343 = x3d.Shape()
Shape343.USE = "HAnimSiteShape"

HAnimSite341.children.append(Shape343)

HAnimSegment308.children.append(HAnimSite341)

HAnimJoint307.children.append(HAnimSegment308)
HAnimJoint344 = x3d.HAnimJoint()
HAnimJoint344.name = "r_subtalar"
HAnimJoint344.DEF = "hanim_r_subtalar"
HAnimJoint344.center = [-0.1086,0.0001,-0.0368]
HAnimJoint344.ulimit = [0,0,0]
HAnimJoint344.llimit = [0,0,0]
HAnimSegment345 = x3d.HAnimSegment()
HAnimSegment345.name = "r_midproximal"
HAnimSegment345.DEF = "hanim_r_midproximal"
#<HAnimJoint name='r_subtalar'/> visualization sphere within <HAnimSegment name='r_midproximal'/>
TouchSensor346 = x3d.TouchSensor()
TouchSensor346.description = "HAnimJoint r_subtalar, HAnimSegment r_midproximal"

HAnimSegment345.children.append(TouchSensor346)
Transform347 = x3d.Transform()
Transform347.translation = [-0.1086,0.0001,-0.0368]
Shape348 = x3d.Shape()
Shape348.USE = "HAnimJointShape"

Transform347.children.append(Shape348)

HAnimSegment345.children.append(Transform347)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_subtalar'/> to <HAnimJoint name='r_midtarsal'/>
Shape349 = x3d.Shape()
LineSet350 = x3d.LineSet()
LineSet350.vertexCount = [2]
Coordinate351 = x3d.Coordinate()
Coordinate351.point = (-0.1086,0.0001,-0.0368,-0.1086,0.0001,0.0368)

LineSet350.coord = Coordinate351
ColorRGBA352 = x3d.ColorRGBA()
ColorRGBA352.USE = "HAnimSegmentLineColorRGBA"

LineSet350.color = ColorRGBA352

Shape349.geometry = LineSet350

HAnimSegment345.children.append(Shape349)

HAnimJoint344.children.append(HAnimSegment345)
HAnimJoint353 = x3d.HAnimJoint()
HAnimJoint353.name = "r_midtarsal"
HAnimJoint353.DEF = "hanim_r_midtarsal"
HAnimJoint353.center = [-0.1086,0.0001,0.0368]
HAnimJoint353.ulimit = [0,0,0]
HAnimJoint353.llimit = [0,0,0]
HAnimSegment354 = x3d.HAnimSegment()
HAnimSegment354.name = "r_middistal"
HAnimSegment354.DEF = "hanim_r_middistal"
#<HAnimJoint name='r_midtarsal'/> visualization sphere within <HAnimSegment name='r_middistal'/>
TouchSensor355 = x3d.TouchSensor()
TouchSensor355.description = "HAnimJoint r_midtarsal, HAnimSegment r_middistal"

HAnimSegment354.children.append(TouchSensor355)
Transform356 = x3d.Transform()
Transform356.translation = [-0.1086,0.0001,0.0368]
Shape357 = x3d.Shape()
Shape357.USE = "HAnimJointShape"

Transform356.children.append(Shape357)

HAnimSegment354.children.append(Transform356)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_midtarsal'/> to <HAnimJoint name='r_metatarsal'/>
Shape358 = x3d.Shape()
LineSet359 = x3d.LineSet()
LineSet359.vertexCount = [2]
Coordinate360 = x3d.Coordinate()
Coordinate360.point = (-0.1086,0.0001,0.0368,-0.1086,0.0000,0.0762)

LineSet359.coord = Coordinate360
ColorRGBA361 = x3d.ColorRGBA()
ColorRGBA361.USE = "HAnimSegmentLineColorRGBA"

LineSet359.color = ColorRGBA361

Shape358.geometry = LineSet359

HAnimSegment354.children.append(Shape358)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_midtarsal'/> to <HAnimSite name='r_metatarsal_pha1'/>
Shape362 = x3d.Shape()
LineSet363 = x3d.LineSet()
LineSet363.vertexCount = [2]
Coordinate364 = x3d.Coordinate()
Coordinate364.point = (-0.1086,0.0001,0.0368,-0.0521,0.0260,0.0127)

LineSet363.coord = Coordinate364
ColorRGBA365 = x3d.ColorRGBA()
ColorRGBA365.USE = "HAnimSiteLineColorRGBA"

LineSet363.color = ColorRGBA365

Shape362.geometry = LineSet363

HAnimSegment354.children.append(Shape362)
HAnimSite366 = x3d.HAnimSite()
HAnimSite366.name = "r_metatarsal_pha1_pt"
HAnimSite366.DEF = "hanim_r_metatarsal_pha1_pt"
HAnimSite366.translation = [-0.0521,0.026,0.0127]
#HAnimSite visualization shape
TouchSensor367 = x3d.TouchSensor()
TouchSensor367.description = "HAnimSite r_metatarsal_pha1"

HAnimSite366.children.append(TouchSensor367)
Shape368 = x3d.Shape()
Shape368.USE = "HAnimSiteShape"

HAnimSite366.children.append(Shape368)

HAnimSegment354.children.append(HAnimSite366)

HAnimJoint353.children.append(HAnimSegment354)
HAnimJoint369 = x3d.HAnimJoint()
HAnimJoint369.name = "r_metatarsal"
HAnimJoint369.DEF = "hanim_r_metatarsal"
HAnimJoint369.center = [-0.1086,0,0.0762]
HAnimJoint369.ulimit = [0,0,0]
HAnimJoint369.llimit = [0,0,0]
HAnimSegment370 = x3d.HAnimSegment()
HAnimSegment370.name = "r_forefoot"
HAnimSegment370.DEF = "hanim_r_forefoot"
#<HAnimJoint name='r_metatarsal'/> visualization sphere within <HAnimSegment name='r_forefoot'/>
TouchSensor371 = x3d.TouchSensor()
TouchSensor371.description = "HAnimJoint r_metatarsal, HAnimSegment r_forefoot"

HAnimSegment370.children.append(TouchSensor371)
Transform372 = x3d.Transform()
Transform372.translation = [-0.1086,0,0.0762]
Shape373 = x3d.Shape()
Shape373.USE = "HAnimJointShape"

Transform372.children.append(Shape373)

HAnimSegment370.children.append(Transform372)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_metatarsal'/> to <HAnimSite name='r_forefoot_tip'/>
Shape374 = x3d.Shape()
LineSet375 = x3d.LineSet()
LineSet375.vertexCount = [2]
Coordinate376 = x3d.Coordinate()
Coordinate376.point = (-0.1086,0.0000,0.0762,-0.1043,0.0227,0.1450)

LineSet375.coord = Coordinate376
ColorRGBA377 = x3d.ColorRGBA()
ColorRGBA377.USE = "HAnimSiteLineColorRGBA"

LineSet375.color = ColorRGBA377

Shape374.geometry = LineSet375

HAnimSegment370.children.append(Shape374)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_metatarsal'/> to <HAnimSite name='r_metatarsal_pha5'/>
Shape378 = x3d.Shape()
LineSet379 = x3d.LineSet()
LineSet379.vertexCount = [2]
Coordinate380 = x3d.Coordinate()
Coordinate380.point = (-0.1086,0.0000,0.0762,-0.1523,0.0166,0.0895)

LineSet379.coord = Coordinate380
ColorRGBA381 = x3d.ColorRGBA()
ColorRGBA381.USE = "HAnimSiteLineColorRGBA"

LineSet379.color = ColorRGBA381

Shape378.geometry = LineSet379

HAnimSegment370.children.append(Shape378)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_metatarsal'/> to <HAnimSite name='r_digit2'/>
Shape382 = x3d.Shape()
LineSet383 = x3d.LineSet()
LineSet383.vertexCount = [2]
Coordinate384 = x3d.Coordinate()
Coordinate384.point = (-0.1086,0.0000,0.0762,-0.0883,0.0134,0.1383)

LineSet383.coord = Coordinate384
ColorRGBA385 = x3d.ColorRGBA()
ColorRGBA385.USE = "HAnimSiteLineColorRGBA"

LineSet383.color = ColorRGBA385

Shape382.geometry = LineSet383

HAnimSegment370.children.append(Shape382)
HAnimSite386 = x3d.HAnimSite()
HAnimSite386.name = "r_forefoot_tip"
HAnimSite386.DEF = "hanim_r_forefoot_tip"
HAnimSite386.translation = [-0.1043,0.0227,0.145]
#HAnimSite visualization shape
TouchSensor387 = x3d.TouchSensor()
TouchSensor387.description = "HAnimSite r_forefoot_tip"

HAnimSite386.children.append(TouchSensor387)
Shape388 = x3d.Shape()
Shape388.USE = "HAnimSiteShape"

HAnimSite386.children.append(Shape388)

HAnimSegment370.children.append(HAnimSite386)
HAnimSite389 = x3d.HAnimSite()
HAnimSite389.name = "r_metatarsal_pha5_pt"
HAnimSite389.DEF = "hanim_r_metatarsal_pha5_pt"
HAnimSite389.translation = [-0.1523,0.0166,0.0895]
#HAnimSite visualization shape
TouchSensor390 = x3d.TouchSensor()
TouchSensor390.description = "HAnimSite r_metatarsal_pha5"

HAnimSite389.children.append(TouchSensor390)
Shape391 = x3d.Shape()
Shape391.USE = "HAnimSiteShape"

HAnimSite389.children.append(Shape391)

HAnimSegment370.children.append(HAnimSite389)
HAnimSite392 = x3d.HAnimSite()
HAnimSite392.name = "r_digit2_pt"
HAnimSite392.DEF = "hanim_r_digit2_pt"
HAnimSite392.translation = [-0.0883,0.0134,0.1383]
#HAnimSite visualization shape
TouchSensor393 = x3d.TouchSensor()
TouchSensor393.description = "HAnimSite r_digit2"

HAnimSite392.children.append(TouchSensor393)
Shape394 = x3d.Shape()
Shape394.USE = "HAnimSiteShape"

HAnimSite392.children.append(Shape394)

HAnimSegment370.children.append(HAnimSite392)

HAnimJoint369.children.append(HAnimSegment370)

HAnimJoint353.children.append(HAnimJoint369)

HAnimJoint344.children.append(HAnimJoint353)

HAnimJoint307.children.append(HAnimJoint344)

HAnimJoint298.children.append(HAnimJoint307)

HAnimJoint268.children.append(HAnimJoint298)

HAnimJoint61.children.append(HAnimJoint268)

HAnimJoint45.children.append(HAnimJoint61)
HAnimJoint395 = x3d.HAnimJoint()
HAnimJoint395.name = "vl5"
HAnimJoint395.DEF = "hanim_vl5"
HAnimJoint395.center = [0.0028,1.0568,-0.0776]
HAnimJoint395.ulimit = [0,0,0]
HAnimJoint395.llimit = [0,0,0]
HAnimSegment396 = x3d.HAnimSegment()
HAnimSegment396.name = "l5"
HAnimSegment396.DEF = "hanim_l5"
#<HAnimJoint name='vl5'/> visualization sphere within <HAnimSegment name='l5'/>
TouchSensor397 = x3d.TouchSensor()
TouchSensor397.description = "HAnimJoint vl5, HAnimSegment l5"

HAnimSegment396.children.append(TouchSensor397)
Transform398 = x3d.Transform()
Transform398.translation = [0.0028,1.0568,-0.0776]
Shape399 = x3d.Shape()
Shape399.USE = "HAnimJointShape"

Transform398.children.append(Shape399)

HAnimSegment396.children.append(Transform398)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vl5'/> to <HAnimJoint name='vl4'/>
Shape400 = x3d.Shape()
LineSet401 = x3d.LineSet()
LineSet401.vertexCount = [2]
Coordinate402 = x3d.Coordinate()
Coordinate402.point = (0.0028,1.0568,-0.0776,0.0035,1.0925,-0.0787)

LineSet401.coord = Coordinate402
ColorRGBA403 = x3d.ColorRGBA()
ColorRGBA403.USE = "HAnimSegmentLineColorRGBA"

LineSet401.color = ColorRGBA403

Shape400.geometry = LineSet401

HAnimSegment396.children.append(Shape400)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vl5'/> to <HAnimSite name='waist_preferred_post'/>
Shape404 = x3d.Shape()
LineSet405 = x3d.LineSet()
LineSet405.vertexCount = [2]
Coordinate406 = x3d.Coordinate()
Coordinate406.point = (0.0028,1.0568,-0.0776,0.0000,1.0915,-0.1091)

LineSet405.coord = Coordinate406
ColorRGBA407 = x3d.ColorRGBA()
ColorRGBA407.USE = "HAnimSiteLineColorRGBA"

LineSet405.color = ColorRGBA407

Shape404.geometry = LineSet405

HAnimSegment396.children.append(Shape404)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vl5'/> to <HAnimSite name='navel'/>
Shape408 = x3d.Shape()
LineSet409 = x3d.LineSet()
LineSet409.vertexCount = [2]
Coordinate410 = x3d.Coordinate()
Coordinate410.point = (0.0028,1.0568,-0.0776,0.0069,1.0966,0.1017)

LineSet409.coord = Coordinate410
ColorRGBA411 = x3d.ColorRGBA()
ColorRGBA411.USE = "HAnimSiteLineColorRGBA"

LineSet409.color = ColorRGBA411

Shape408.geometry = LineSet409

HAnimSegment396.children.append(Shape408)
HAnimSite412 = x3d.HAnimSite()
HAnimSite412.name = "waist_preferred_post_pt"
HAnimSite412.DEF = "hanim_waist_preferred_post_pt"
HAnimSite412.translation = [0,1.0915,-0.1091]
#HAnimSite visualization shape
TouchSensor413 = x3d.TouchSensor()
TouchSensor413.description = "HAnimSite waist_preferred_post"

HAnimSite412.children.append(TouchSensor413)
Shape414 = x3d.Shape()
Shape414.USE = "HAnimSiteShape"

HAnimSite412.children.append(Shape414)

HAnimSegment396.children.append(HAnimSite412)
HAnimSite415 = x3d.HAnimSite()
HAnimSite415.name = "navel_pt"
HAnimSite415.DEF = "hanim_navel_pt"
HAnimSite415.translation = [0.0069,1.0966,0.1017]
#HAnimSite visualization shape
TouchSensor416 = x3d.TouchSensor()
TouchSensor416.description = "HAnimSite navel"

HAnimSite415.children.append(TouchSensor416)
Shape417 = x3d.Shape()
Shape417.USE = "HAnimSiteShape"

HAnimSite415.children.append(Shape417)

HAnimSegment396.children.append(HAnimSite415)

HAnimJoint395.children.append(HAnimSegment396)
HAnimJoint418 = x3d.HAnimJoint()
HAnimJoint418.name = "vl4"
HAnimJoint418.DEF = "hanim_vl4"
HAnimJoint418.center = [0.0035,1.0925,-0.0787]
HAnimJoint418.ulimit = [0,0,0]
HAnimJoint418.llimit = [0,0,0]
HAnimSegment419 = x3d.HAnimSegment()
HAnimSegment419.name = "l4"
HAnimSegment419.DEF = "hanim_l4"
#<HAnimJoint name='vl4'/> visualization sphere within <HAnimSegment name='l4'/>
TouchSensor420 = x3d.TouchSensor()
TouchSensor420.description = "HAnimJoint vl4, HAnimSegment l4"

HAnimSegment419.children.append(TouchSensor420)
Transform421 = x3d.Transform()
Transform421.translation = [0.0035,1.0925,-0.0787]
Shape422 = x3d.Shape()
Shape422.USE = "HAnimJointShape"

Transform421.children.append(Shape422)

HAnimSegment419.children.append(Transform421)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vl4'/> to <HAnimJoint name='vl3'/>
Shape423 = x3d.Shape()
LineSet424 = x3d.LineSet()
LineSet424.vertexCount = [2]
Coordinate425 = x3d.Coordinate()
Coordinate425.point = (0.0035,1.0925,-0.0787,0.0041,1.1276,-0.0796)

LineSet424.coord = Coordinate425
ColorRGBA426 = x3d.ColorRGBA()
ColorRGBA426.USE = "HAnimSegmentLineColorRGBA"

LineSet424.color = ColorRGBA426

Shape423.geometry = LineSet424

HAnimSegment419.children.append(Shape423)

HAnimJoint418.children.append(HAnimSegment419)
HAnimJoint427 = x3d.HAnimJoint()
HAnimJoint427.name = "vl3"
HAnimJoint427.DEF = "hanim_vl3"
HAnimJoint427.center = [0.0041,1.1276,-0.0796]
HAnimJoint427.ulimit = [0,0,0]
HAnimJoint427.llimit = [0,0,0]
HAnimSegment428 = x3d.HAnimSegment()
HAnimSegment428.name = "l3"
HAnimSegment428.DEF = "hanim_l3"
#<HAnimJoint name='vl3'/> visualization sphere within <HAnimSegment name='l3'/>
TouchSensor429 = x3d.TouchSensor()
TouchSensor429.description = "HAnimJoint vl3, HAnimSegment l3"

HAnimSegment428.children.append(TouchSensor429)
Transform430 = x3d.Transform()
Transform430.translation = [0.0041,1.1276,-0.0796]
Shape431 = x3d.Shape()
Shape431.USE = "HAnimJointShape"

Transform430.children.append(Shape431)

HAnimSegment428.children.append(Transform430)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vl3'/> to <HAnimJoint name='vl2'/>
Shape432 = x3d.Shape()
LineSet433 = x3d.LineSet()
LineSet433.vertexCount = [2]
Coordinate434 = x3d.Coordinate()
Coordinate434.point = (0.0041,1.1276,-0.0796,0.0045,1.1546,-0.0800)

LineSet433.coord = Coordinate434
ColorRGBA435 = x3d.ColorRGBA()
ColorRGBA435.USE = "HAnimSegmentLineColorRGBA"

LineSet433.color = ColorRGBA435

Shape432.geometry = LineSet433

HAnimSegment428.children.append(Shape432)

HAnimJoint427.children.append(HAnimSegment428)
HAnimJoint436 = x3d.HAnimJoint()
HAnimJoint436.name = "vl2"
HAnimJoint436.DEF = "hanim_vl2"
HAnimJoint436.center = [0.0045,1.1546,-0.08]
HAnimJoint436.ulimit = [0,0,0]
HAnimJoint436.llimit = [0,0,0]
HAnimSegment437 = x3d.HAnimSegment()
HAnimSegment437.name = "l2"
HAnimSegment437.DEF = "hanim_l2"
#<HAnimJoint name='vl2'/> visualization sphere within <HAnimSegment name='l2'/>
TouchSensor438 = x3d.TouchSensor()
TouchSensor438.description = "HAnimJoint vl2, HAnimSegment l2"

HAnimSegment437.children.append(TouchSensor438)
Transform439 = x3d.Transform()
Transform439.translation = [0.0045,1.1546,-0.08]
Shape440 = x3d.Shape()
Shape440.USE = "HAnimJointShape"

Transform439.children.append(Shape440)

HAnimSegment437.children.append(Transform439)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vl2'/> to <HAnimJoint name='vl1'/>
Shape441 = x3d.Shape()
LineSet442 = x3d.LineSet()
LineSet442.vertexCount = [2]
Coordinate443 = x3d.Coordinate()
Coordinate443.point = (0.0045,1.1546,-0.0800,0.0048,1.1912,-0.0805)

LineSet442.coord = Coordinate443
ColorRGBA444 = x3d.ColorRGBA()
ColorRGBA444.USE = "HAnimSegmentLineColorRGBA"

LineSet442.color = ColorRGBA444

Shape441.geometry = LineSet442

HAnimSegment437.children.append(Shape441)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vl2'/> to <HAnimSite name='r_rib10'/>
Shape445 = x3d.Shape()
LineSet446 = x3d.LineSet()
LineSet446.vertexCount = [2]
Coordinate447 = x3d.Coordinate()
Coordinate447.point = (0.0045,1.1546,-0.0800,-0.0711,1.1941,0.1016)

LineSet446.coord = Coordinate447
ColorRGBA448 = x3d.ColorRGBA()
ColorRGBA448.USE = "HAnimSiteLineColorRGBA"

LineSet446.color = ColorRGBA448

Shape445.geometry = LineSet446

HAnimSegment437.children.append(Shape445)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vl2'/> to <HAnimSite name='l_rib10'/>
Shape449 = x3d.Shape()
LineSet450 = x3d.LineSet()
LineSet450.vertexCount = [2]
Coordinate451 = x3d.Coordinate()
Coordinate451.point = (0.0045,1.1546,-0.0800,0.0871,1.1925,0.0992)

LineSet450.coord = Coordinate451
ColorRGBA452 = x3d.ColorRGBA()
ColorRGBA452.USE = "HAnimSiteLineColorRGBA"

LineSet450.color = ColorRGBA452

Shape449.geometry = LineSet450

HAnimSegment437.children.append(Shape449)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vl2'/> to <HAnimSite name='rib10_midspine'/>
Shape453 = x3d.Shape()
LineSet454 = x3d.LineSet()
LineSet454.vertexCount = [2]
Coordinate455 = x3d.Coordinate()
Coordinate455.point = (0.0045,1.1546,-0.0800,0.0049,1.1908,-0.1113)

LineSet454.coord = Coordinate455
ColorRGBA456 = x3d.ColorRGBA()
ColorRGBA456.USE = "HAnimSiteLineColorRGBA"

LineSet454.color = ColorRGBA456

Shape453.geometry = LineSet454

HAnimSegment437.children.append(Shape453)
HAnimSite457 = x3d.HAnimSite()
HAnimSite457.name = "r_rib10_pt"
HAnimSite457.DEF = "hanim_r_rib10_pt"
HAnimSite457.translation = [-0.0711,1.1941,0.1016]
#HAnimSite visualization shape
TouchSensor458 = x3d.TouchSensor()
TouchSensor458.description = "HAnimSite r_rib10"

HAnimSite457.children.append(TouchSensor458)
Shape459 = x3d.Shape()
Shape459.USE = "HAnimSiteShape"

HAnimSite457.children.append(Shape459)

HAnimSegment437.children.append(HAnimSite457)
HAnimSite460 = x3d.HAnimSite()
HAnimSite460.name = "l_rib10_pt"
HAnimSite460.DEF = "hanim_l_rib10_pt"
HAnimSite460.translation = [0.0871,1.1925,0.0992]
#HAnimSite visualization shape
TouchSensor461 = x3d.TouchSensor()
TouchSensor461.description = "HAnimSite l_rib10"

HAnimSite460.children.append(TouchSensor461)
Shape462 = x3d.Shape()
Shape462.USE = "HAnimSiteShape"

HAnimSite460.children.append(Shape462)

HAnimSegment437.children.append(HAnimSite460)
HAnimSite463 = x3d.HAnimSite()
HAnimSite463.name = "rib10_midspine_pt"
HAnimSite463.DEF = "hanim_rib10_midspine_pt"
HAnimSite463.translation = [0.0049,1.1908,-0.1113]
#HAnimSite visualization shape
TouchSensor464 = x3d.TouchSensor()
TouchSensor464.description = "HAnimSite rib10_midspine"

HAnimSite463.children.append(TouchSensor464)
Shape465 = x3d.Shape()
Shape465.USE = "HAnimSiteShape"

HAnimSite463.children.append(Shape465)

HAnimSegment437.children.append(HAnimSite463)

HAnimJoint436.children.append(HAnimSegment437)
HAnimJoint466 = x3d.HAnimJoint()
HAnimJoint466.name = "vl1"
HAnimJoint466.DEF = "hanim_vl1"
HAnimJoint466.center = [0.0048,1.1912,-0.0805]
HAnimJoint466.ulimit = [0,0,0]
HAnimJoint466.llimit = [0,0,0]
HAnimSegment467 = x3d.HAnimSegment()
HAnimSegment467.name = "l1"
HAnimSegment467.DEF = "hanim_l1"
#<HAnimJoint name='vl1'/> visualization sphere within <HAnimSegment name='l1'/>
TouchSensor468 = x3d.TouchSensor()
TouchSensor468.description = "HAnimJoint vl1, HAnimSegment l1"

HAnimSegment467.children.append(TouchSensor468)
Transform469 = x3d.Transform()
Transform469.translation = [0.0048,1.1912,-0.0805]
Shape470 = x3d.Shape()
Shape470.USE = "HAnimJointShape"

Transform469.children.append(Shape470)

HAnimSegment467.children.append(Transform469)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vl1'/> to <HAnimJoint name='vt12'/>
Shape471 = x3d.Shape()
LineSet472 = x3d.LineSet()
LineSet472.vertexCount = [2]
Coordinate473 = x3d.Coordinate()
Coordinate473.point = (0.0048,1.1912,-0.0805,0.0051,1.2278,-0.0808)

LineSet472.coord = Coordinate473
ColorRGBA474 = x3d.ColorRGBA()
ColorRGBA474.USE = "HAnimSegmentLineColorRGBA"

LineSet472.color = ColorRGBA474

Shape471.geometry = LineSet472

HAnimSegment467.children.append(Shape471)

HAnimJoint466.children.append(HAnimSegment467)
HAnimJoint475 = x3d.HAnimJoint()
HAnimJoint475.name = "vt12"
HAnimJoint475.DEF = "hanim_vt12"
HAnimJoint475.center = [0.0051,1.2278,-0.0808]
HAnimJoint475.ulimit = [0,0,0]
HAnimJoint475.llimit = [0,0,0]
HAnimSegment476 = x3d.HAnimSegment()
HAnimSegment476.name = "t12"
HAnimSegment476.DEF = "hanim_t12"
#<HAnimJoint name='vt12'/> visualization sphere within <HAnimSegment name='t12'/>
TouchSensor477 = x3d.TouchSensor()
TouchSensor477.description = "HAnimJoint vt12, HAnimSegment t12"

HAnimSegment476.children.append(TouchSensor477)
Transform478 = x3d.Transform()
Transform478.translation = [0.0051,1.2278,-0.0808]
Shape479 = x3d.Shape()
Shape479.USE = "HAnimJointShape"

Transform478.children.append(Shape479)

HAnimSegment476.children.append(Transform478)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vt12'/> to <HAnimJoint name='vt11'/>
Shape480 = x3d.Shape()
LineSet481 = x3d.LineSet()
LineSet481.vertexCount = [2]
Coordinate482 = x3d.Coordinate()
Coordinate482.point = (0.0051,1.2278,-0.0808,0.0053,1.2679,-0.0810)

LineSet481.coord = Coordinate482
ColorRGBA483 = x3d.ColorRGBA()
ColorRGBA483.USE = "HAnimSegmentLineColorRGBA"

LineSet481.color = ColorRGBA483

Shape480.geometry = LineSet481

HAnimSegment476.children.append(Shape480)

HAnimJoint475.children.append(HAnimSegment476)
HAnimJoint484 = x3d.HAnimJoint()
HAnimJoint484.name = "vt11"
HAnimJoint484.DEF = "hanim_vt11"
HAnimJoint484.center = [0.0053,1.2679,-0.081]
HAnimJoint484.ulimit = [0,0,0]
HAnimJoint484.llimit = [0,0,0]
HAnimSegment485 = x3d.HAnimSegment()
HAnimSegment485.name = "t11"
HAnimSegment485.DEF = "hanim_t11"
#<HAnimJoint name='vt11'/> visualization sphere within <HAnimSegment name='t11'/>
TouchSensor486 = x3d.TouchSensor()
TouchSensor486.description = "HAnimJoint vt11, HAnimSegment t11"

HAnimSegment485.children.append(TouchSensor486)
Transform487 = x3d.Transform()
Transform487.translation = [0.0053,1.2679,-0.081]
Shape488 = x3d.Shape()
Shape488.USE = "HAnimJointShape"

Transform487.children.append(Shape488)

HAnimSegment485.children.append(Transform487)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vt11'/> to <HAnimJoint name='vt10'/>
Shape489 = x3d.Shape()
LineSet490 = x3d.LineSet()
LineSet490.vertexCount = [2]
Coordinate491 = x3d.Coordinate()
Coordinate491.point = (0.0053,1.2679,-0.0810,0.0056,1.2848,-0.0822)

LineSet490.coord = Coordinate491
ColorRGBA492 = x3d.ColorRGBA()
ColorRGBA492.USE = "HAnimSegmentLineColorRGBA"

LineSet490.color = ColorRGBA492

Shape489.geometry = LineSet490

HAnimSegment485.children.append(Shape489)

HAnimJoint484.children.append(HAnimSegment485)
HAnimJoint493 = x3d.HAnimJoint()
HAnimJoint493.name = "vt10"
HAnimJoint493.DEF = "hanim_vt10"
HAnimJoint493.center = [0.0056,1.2848,-0.0822]
HAnimJoint493.ulimit = [0,0,0]
HAnimJoint493.llimit = [0,0,0]
HAnimSegment494 = x3d.HAnimSegment()
HAnimSegment494.name = "t10"
HAnimSegment494.DEF = "hanim_t10"
#<HAnimJoint name='vt10'/> visualization sphere within <HAnimSegment name='t10'/>
TouchSensor495 = x3d.TouchSensor()
TouchSensor495.description = "HAnimJoint vt10, HAnimSegment t10"

HAnimSegment494.children.append(TouchSensor495)
Transform496 = x3d.Transform()
Transform496.translation = [0.0056,1.2848,-0.0822]
Shape497 = x3d.Shape()
Shape497.USE = "HAnimJointShape"

Transform496.children.append(Shape497)

HAnimSegment494.children.append(Transform496)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vt10'/> to <HAnimJoint name='vt9'/>
Shape498 = x3d.Shape()
LineSet499 = x3d.LineSet()
LineSet499.vertexCount = [2]
Coordinate500 = x3d.Coordinate()
Coordinate500.point = (0.0056,1.2848,-0.0822,0.0057,1.3126,-0.0838)

LineSet499.coord = Coordinate500
ColorRGBA501 = x3d.ColorRGBA()
ColorRGBA501.USE = "HAnimSegmentLineColorRGBA"

LineSet499.color = ColorRGBA501

Shape498.geometry = LineSet499

HAnimSegment494.children.append(Shape498)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vt10'/> to <HAnimSite name='substernale'/>
Shape502 = x3d.Shape()
LineSet503 = x3d.LineSet()
LineSet503.vertexCount = [2]
Coordinate504 = x3d.Coordinate()
Coordinate504.point = (0.0056,1.2848,-0.0822,0.0085,1.2995,0.1147)

LineSet503.coord = Coordinate504
ColorRGBA505 = x3d.ColorRGBA()
ColorRGBA505.USE = "HAnimSiteLineColorRGBA"

LineSet503.color = ColorRGBA505

Shape502.geometry = LineSet503

HAnimSegment494.children.append(Shape502)
HAnimSite506 = x3d.HAnimSite()
HAnimSite506.name = "substernale_pt"
HAnimSite506.DEF = "hanim_substernale_pt"
HAnimSite506.translation = [0.0085,1.2995,0.1147]
#HAnimSite visualization shape
TouchSensor507 = x3d.TouchSensor()
TouchSensor507.description = "HAnimSite substernale"

HAnimSite506.children.append(TouchSensor507)
Shape508 = x3d.Shape()
Shape508.USE = "HAnimSiteShape"

HAnimSite506.children.append(Shape508)

HAnimSegment494.children.append(HAnimSite506)

HAnimJoint493.children.append(HAnimSegment494)
HAnimJoint509 = x3d.HAnimJoint()
HAnimJoint509.name = "vt9"
HAnimJoint509.DEF = "hanim_vt9"
HAnimJoint509.center = [0.0057,1.3126,-0.0838]
HAnimJoint509.ulimit = [0,0,0]
HAnimJoint509.llimit = [0,0,0]
HAnimSegment510 = x3d.HAnimSegment()
HAnimSegment510.name = "t9"
HAnimSegment510.DEF = "hanim_t9"
#<HAnimJoint name='vt9'/> visualization sphere within <HAnimSegment name='t9'/>
TouchSensor511 = x3d.TouchSensor()
TouchSensor511.description = "HAnimJoint vt9, HAnimSegment t9"

HAnimSegment510.children.append(TouchSensor511)
Transform512 = x3d.Transform()
Transform512.translation = [0.0057,1.3126,-0.0838]
Shape513 = x3d.Shape()
Shape513.USE = "HAnimJointShape"

Transform512.children.append(Shape513)

HAnimSegment510.children.append(Transform512)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vt9'/> to <HAnimJoint name='vt8'/>
Shape514 = x3d.Shape()
LineSet515 = x3d.LineSet()
LineSet515.vertexCount = [2]
Coordinate516 = x3d.Coordinate()
Coordinate516.point = (0.0057,1.3126,-0.0838,0.0057,1.3382,-0.0845)

LineSet515.coord = Coordinate516
ColorRGBA517 = x3d.ColorRGBA()
ColorRGBA517.USE = "HAnimSegmentLineColorRGBA"

LineSet515.color = ColorRGBA517

Shape514.geometry = LineSet515

HAnimSegment510.children.append(Shape514)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vt9'/> to <HAnimSite name='r_thelion'/>
Shape518 = x3d.Shape()
LineSet519 = x3d.LineSet()
LineSet519.vertexCount = [2]
Coordinate520 = x3d.Coordinate()
Coordinate520.point = (0.0057,1.3126,-0.0838,-0.0736,1.3385,0.1217)

LineSet519.coord = Coordinate520
ColorRGBA521 = x3d.ColorRGBA()
ColorRGBA521.USE = "HAnimSiteLineColorRGBA"

LineSet519.color = ColorRGBA521

Shape518.geometry = LineSet519

HAnimSegment510.children.append(Shape518)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vt9'/> to <HAnimSite name='l_thelion'/>
Shape522 = x3d.Shape()
LineSet523 = x3d.LineSet()
LineSet523.vertexCount = [2]
Coordinate524 = x3d.Coordinate()
Coordinate524.point = (0.0057,1.3126,-0.0838,0.0918,1.3382,0.1192)

LineSet523.coord = Coordinate524
ColorRGBA525 = x3d.ColorRGBA()
ColorRGBA525.USE = "HAnimSiteLineColorRGBA"

LineSet523.color = ColorRGBA525

Shape522.geometry = LineSet523

HAnimSegment510.children.append(Shape522)
HAnimSite526 = x3d.HAnimSite()
HAnimSite526.name = "r_thelion_pt"
HAnimSite526.DEF = "hanim_r_thelion_pt"
HAnimSite526.translation = [-0.0736,1.3385,0.1217]
#HAnimSite visualization shape
TouchSensor527 = x3d.TouchSensor()
TouchSensor527.description = "HAnimSite r_thelion"

HAnimSite526.children.append(TouchSensor527)
Shape528 = x3d.Shape()
Shape528.USE = "HAnimSiteShape"

HAnimSite526.children.append(Shape528)

HAnimSegment510.children.append(HAnimSite526)
HAnimSite529 = x3d.HAnimSite()
HAnimSite529.name = "l_thelion_pt"
HAnimSite529.DEF = "hanim_l_thelion_pt"
HAnimSite529.translation = [0.0918,1.3382,0.1192]
#HAnimSite visualization shape
TouchSensor530 = x3d.TouchSensor()
TouchSensor530.description = "HAnimSite l_thelion"

HAnimSite529.children.append(TouchSensor530)
Shape531 = x3d.Shape()
Shape531.USE = "HAnimSiteShape"

HAnimSite529.children.append(Shape531)

HAnimSegment510.children.append(HAnimSite529)

HAnimJoint509.children.append(HAnimSegment510)
HAnimJoint532 = x3d.HAnimJoint()
HAnimJoint532.name = "vt8"
HAnimJoint532.DEF = "hanim_vt8"
HAnimJoint532.center = [0.0057,1.3382,-0.0845]
HAnimJoint532.ulimit = [0,0,0]
HAnimJoint532.llimit = [0,0,0]
HAnimSegment533 = x3d.HAnimSegment()
HAnimSegment533.name = "t8"
HAnimSegment533.DEF = "hanim_t8"
#<HAnimJoint name='vt8'/> visualization sphere within <HAnimSegment name='t8'/>
TouchSensor534 = x3d.TouchSensor()
TouchSensor534.description = "HAnimJoint vt8, HAnimSegment t8"

HAnimSegment533.children.append(TouchSensor534)
Transform535 = x3d.Transform()
Transform535.translation = [0.0057,1.3382,-0.0845]
Shape536 = x3d.Shape()
Shape536.USE = "HAnimJointShape"

Transform535.children.append(Shape536)

HAnimSegment533.children.append(Transform535)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vt8'/> to <HAnimJoint name='vt7'/>
Shape537 = x3d.Shape()
LineSet538 = x3d.LineSet()
LineSet538.vertexCount = [2]
Coordinate539 = x3d.Coordinate()
Coordinate539.point = (0.0057,1.3382,-0.0845,0.0058,1.3625,-0.0833)

LineSet538.coord = Coordinate539
ColorRGBA540 = x3d.ColorRGBA()
ColorRGBA540.USE = "HAnimSegmentLineColorRGBA"

LineSet538.color = ColorRGBA540

Shape537.geometry = LineSet538

HAnimSegment533.children.append(Shape537)

HAnimJoint532.children.append(HAnimSegment533)
HAnimJoint541 = x3d.HAnimJoint()
HAnimJoint541.name = "vt7"
HAnimJoint541.DEF = "hanim_vt7"
HAnimJoint541.center = [0.0058,1.3625,-0.0833]
HAnimJoint541.ulimit = [0,0,0]
HAnimJoint541.llimit = [0,0,0]
HAnimSegment542 = x3d.HAnimSegment()
HAnimSegment542.name = "t7"
HAnimSegment542.DEF = "hanim_t7"
#<HAnimJoint name='vt7'/> visualization sphere within <HAnimSegment name='t7'/>
TouchSensor543 = x3d.TouchSensor()
TouchSensor543.description = "HAnimJoint vt7, HAnimSegment t7"

HAnimSegment542.children.append(TouchSensor543)
Transform544 = x3d.Transform()
Transform544.translation = [0.0058,1.3625,-0.0833]
Shape545 = x3d.Shape()
Shape545.USE = "HAnimJointShape"

Transform544.children.append(Shape545)

HAnimSegment542.children.append(Transform544)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vt7'/> to <HAnimJoint name='vt6'/>
Shape546 = x3d.Shape()
LineSet547 = x3d.LineSet()
LineSet547.vertexCount = [2]
Coordinate548 = x3d.Coordinate()
Coordinate548.point = (0.0058,1.3625,-0.0833,0.0059,1.3866,-0.0800)

LineSet547.coord = Coordinate548
ColorRGBA549 = x3d.ColorRGBA()
ColorRGBA549.USE = "HAnimSegmentLineColorRGBA"

LineSet547.color = ColorRGBA549

Shape546.geometry = LineSet547

HAnimSegment542.children.append(Shape546)

HAnimJoint541.children.append(HAnimSegment542)
HAnimJoint550 = x3d.HAnimJoint()
HAnimJoint550.name = "vt6"
HAnimJoint550.DEF = "hanim_vt6"
HAnimJoint550.center = [0.0059,1.3866,-0.08]
HAnimJoint550.ulimit = [0,0,0]
HAnimJoint550.llimit = [0,0,0]
HAnimSegment551 = x3d.HAnimSegment()
HAnimSegment551.name = "t6"
HAnimSegment551.DEF = "hanim_t6"
#<HAnimJoint name='vt6'/> visualization sphere within <HAnimSegment name='t6'/>
TouchSensor552 = x3d.TouchSensor()
TouchSensor552.description = "HAnimJoint vt6, HAnimSegment t6"

HAnimSegment551.children.append(TouchSensor552)
Transform553 = x3d.Transform()
Transform553.translation = [0.0059,1.3866,-0.08]
Shape554 = x3d.Shape()
Shape554.USE = "HAnimJointShape"

Transform553.children.append(Shape554)

HAnimSegment551.children.append(Transform553)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vt6'/> to <HAnimJoint name='vt5'/>
Shape555 = x3d.Shape()
LineSet556 = x3d.LineSet()
LineSet556.vertexCount = [2]
Coordinate557 = x3d.Coordinate()
Coordinate557.point = (0.0059,1.3866,-0.0800,0.0060,1.4102,-0.0745)

LineSet556.coord = Coordinate557
ColorRGBA558 = x3d.ColorRGBA()
ColorRGBA558.USE = "HAnimSegmentLineColorRGBA"

LineSet556.color = ColorRGBA558

Shape555.geometry = LineSet556

HAnimSegment551.children.append(Shape555)

HAnimJoint550.children.append(HAnimSegment551)
HAnimJoint559 = x3d.HAnimJoint()
HAnimJoint559.name = "vt5"
HAnimJoint559.DEF = "hanim_vt5"
HAnimJoint559.center = [0.006,1.4102,-0.0745]
HAnimJoint559.ulimit = [0,0,0]
HAnimJoint559.llimit = [0,0,0]
HAnimSegment560 = x3d.HAnimSegment()
HAnimSegment560.name = "t5"
HAnimSegment560.DEF = "hanim_t5"
#<HAnimJoint name='vt5'/> visualization sphere within <HAnimSegment name='t5'/>
TouchSensor561 = x3d.TouchSensor()
TouchSensor561.description = "HAnimJoint vt5, HAnimSegment t5"

HAnimSegment560.children.append(TouchSensor561)
Transform562 = x3d.Transform()
Transform562.translation = [0.006,1.4102,-0.0745]
Shape563 = x3d.Shape()
Shape563.USE = "HAnimJointShape"

Transform562.children.append(Shape563)

HAnimSegment560.children.append(Transform562)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vt5'/> to <HAnimJoint name='vt4'/>
Shape564 = x3d.Shape()
LineSet565 = x3d.LineSet()
LineSet565.vertexCount = [2]
Coordinate566 = x3d.Coordinate()
Coordinate566.point = (0.0060,1.4102,-0.0745,0.0061,1.4320,-0.0675)

LineSet565.coord = Coordinate566
ColorRGBA567 = x3d.ColorRGBA()
ColorRGBA567.USE = "HAnimSegmentLineColorRGBA"

LineSet565.color = ColorRGBA567

Shape564.geometry = LineSet565

HAnimSegment560.children.append(Shape564)

HAnimJoint559.children.append(HAnimSegment560)
HAnimJoint568 = x3d.HAnimJoint()
HAnimJoint568.name = "vt4"
HAnimJoint568.DEF = "hanim_vt4"
HAnimJoint568.center = [0.0061,1.432,-0.0675]
HAnimJoint568.ulimit = [0,0,0]
HAnimJoint568.llimit = [0,0,0]
HAnimSegment569 = x3d.HAnimSegment()
HAnimSegment569.name = "t4"
HAnimSegment569.DEF = "hanim_t4"
#<HAnimJoint name='vt4'/> visualization sphere within <HAnimSegment name='t4'/>
TouchSensor570 = x3d.TouchSensor()
TouchSensor570.description = "HAnimJoint vt4, HAnimSegment t4"

HAnimSegment569.children.append(TouchSensor570)
Transform571 = x3d.Transform()
Transform571.translation = [0.0061,1.432,-0.0675]
Shape572 = x3d.Shape()
Shape572.USE = "HAnimJointShape"

Transform571.children.append(Shape572)

HAnimSegment569.children.append(Transform571)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vt4'/> to <HAnimJoint name='vt3'/>
Shape573 = x3d.Shape()
LineSet574 = x3d.LineSet()
LineSet574.vertexCount = [2]
Coordinate575 = x3d.Coordinate()
Coordinate575.point = (0.0061,1.4320,-0.0675,0.0062,1.4583,-0.0570)

LineSet574.coord = Coordinate575
ColorRGBA576 = x3d.ColorRGBA()
ColorRGBA576.USE = "HAnimSegmentLineColorRGBA"

LineSet574.color = ColorRGBA576

Shape573.geometry = LineSet574

HAnimSegment569.children.append(Shape573)

HAnimJoint568.children.append(HAnimSegment569)
HAnimJoint577 = x3d.HAnimJoint()
HAnimJoint577.name = "vt3"
HAnimJoint577.DEF = "hanim_vt3"
HAnimJoint577.center = [0.0062,1.4583,-0.057]
HAnimJoint577.ulimit = [0,0,0]
HAnimJoint577.llimit = [0,0,0]
HAnimSegment578 = x3d.HAnimSegment()
HAnimSegment578.name = "t3"
HAnimSegment578.DEF = "hanim_t3"
#<HAnimJoint name='vt3'/> visualization sphere within <HAnimSegment name='t3'/>
TouchSensor579 = x3d.TouchSensor()
TouchSensor579.description = "HAnimJoint vt3, HAnimSegment t3"

HAnimSegment578.children.append(TouchSensor579)
Transform580 = x3d.Transform()
Transform580.translation = [0.0062,1.4583,-0.057]
Shape581 = x3d.Shape()
Shape581.USE = "HAnimJointShape"

Transform580.children.append(Shape581)

HAnimSegment578.children.append(Transform580)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vt3'/> to <HAnimJoint name='vt2'/>
Shape582 = x3d.Shape()
LineSet583 = x3d.LineSet()
LineSet583.vertexCount = [2]
Coordinate584 = x3d.Coordinate()
Coordinate584.point = (0.0062,1.4583,-0.0570,0.0063,1.4761,-0.0484)

LineSet583.coord = Coordinate584
ColorRGBA585 = x3d.ColorRGBA()
ColorRGBA585.USE = "HAnimSegmentLineColorRGBA"

LineSet583.color = ColorRGBA585

Shape582.geometry = LineSet583

HAnimSegment578.children.append(Shape582)

HAnimJoint577.children.append(HAnimSegment578)
HAnimJoint586 = x3d.HAnimJoint()
HAnimJoint586.name = "vt2"
HAnimJoint586.DEF = "hanim_vt2"
HAnimJoint586.center = [0.0063,1.4761,-0.0484]
HAnimJoint586.ulimit = [0,0,0]
HAnimJoint586.llimit = [0,0,0]
HAnimSegment587 = x3d.HAnimSegment()
HAnimSegment587.name = "t2"
HAnimSegment587.DEF = "hanim_t2"
#<HAnimJoint name='vt2'/> visualization sphere within <HAnimSegment name='t2'/>
TouchSensor588 = x3d.TouchSensor()
TouchSensor588.description = "HAnimJoint vt2, HAnimSegment t2"

HAnimSegment587.children.append(TouchSensor588)
Transform589 = x3d.Transform()
Transform589.translation = [0.0063,1.4761,-0.0484]
Shape590 = x3d.Shape()
Shape590.USE = "HAnimJointShape"

Transform589.children.append(Shape590)

HAnimSegment587.children.append(Transform589)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vt2'/> to <HAnimJoint name='vt1'/>
Shape591 = x3d.Shape()
LineSet592 = x3d.LineSet()
LineSet592.vertexCount = [2]
Coordinate593 = x3d.Coordinate()
Coordinate593.point = (0.0063,1.4761,-0.0484,0.0065,1.4951,-0.0387)

LineSet592.coord = Coordinate593
ColorRGBA594 = x3d.ColorRGBA()
ColorRGBA594.USE = "HAnimSegmentLineColorRGBA"

LineSet592.color = ColorRGBA594

Shape591.geometry = LineSet592

HAnimSegment587.children.append(Shape591)

HAnimJoint586.children.append(HAnimSegment587)
HAnimJoint595 = x3d.HAnimJoint()
HAnimJoint595.name = "vt1"
HAnimJoint595.DEF = "hanim_vt1"
HAnimJoint595.center = [0.0065,1.4951,-0.0387]
HAnimJoint595.ulimit = [0,0,0]
HAnimJoint595.llimit = [0,0,0]
HAnimSegment596 = x3d.HAnimSegment()
HAnimSegment596.name = "t1"
HAnimSegment596.DEF = "hanim_t1"
#<HAnimJoint name='vt1'/> visualization sphere within <HAnimSegment name='t1'/>
TouchSensor597 = x3d.TouchSensor()
TouchSensor597.description = "HAnimJoint vt1, HAnimSegment t1"

HAnimSegment596.children.append(TouchSensor597)
Transform598 = x3d.Transform()
Transform598.translation = [0.0065,1.4951,-0.0387]
Shape599 = x3d.Shape()
Shape599.USE = "HAnimJointShape"

Transform598.children.append(Shape599)

HAnimSegment596.children.append(Transform598)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vt1'/> to <HAnimJoint name='vc7'/>
Shape600 = x3d.Shape()
LineSet601 = x3d.LineSet()
LineSet601.vertexCount = [2]
Coordinate602 = x3d.Coordinate()
Coordinate602.point = (0.0065,1.4951,-0.0387,0.0066,1.5132,-0.0301)

LineSet601.coord = Coordinate602
ColorRGBA603 = x3d.ColorRGBA()
ColorRGBA603.USE = "HAnimSegmentLineColorRGBA"

LineSet601.color = ColorRGBA603

Shape600.geometry = LineSet601

HAnimSegment596.children.append(Shape600)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vt1'/> to <HAnimJoint name='l_sternoclavicular'/>
Shape604 = x3d.Shape()
LineSet605 = x3d.LineSet()
LineSet605.vertexCount = [2]
Coordinate606 = x3d.Coordinate()
Coordinate606.point = (0.0065,1.4951,-0.0387,0.0820,1.4488,-0.0353)

LineSet605.coord = Coordinate606
ColorRGBA607 = x3d.ColorRGBA()
ColorRGBA607.USE = "HAnimSegmentLineColorRGBA"

LineSet605.color = ColorRGBA607

Shape604.geometry = LineSet605

HAnimSegment596.children.append(Shape604)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vt1'/> to <HAnimJoint name='r_sternoclavicular'/>
Shape608 = x3d.Shape()
LineSet609 = x3d.LineSet()
LineSet609.vertexCount = [2]
Coordinate610 = x3d.Coordinate()
Coordinate610.point = (0.0065,1.4951,-0.0387,-0.0820,1.4488,-0.0353)

LineSet609.coord = Coordinate610
ColorRGBA611 = x3d.ColorRGBA()
ColorRGBA611.USE = "HAnimSegmentLineColorRGBA"

LineSet609.color = ColorRGBA611

Shape608.geometry = LineSet609

HAnimSegment596.children.append(Shape608)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vt1'/> to <HAnimSite name='suprasternale'/>
Shape612 = x3d.Shape()
LineSet613 = x3d.LineSet()
LineSet613.vertexCount = [2]
Coordinate614 = x3d.Coordinate()
Coordinate614.point = (0.0065,1.4951,-0.0387,0.0084,1.4714,0.0551)

LineSet613.coord = Coordinate614
ColorRGBA615 = x3d.ColorRGBA()
ColorRGBA615.USE = "HAnimSiteLineColorRGBA"

LineSet613.color = ColorRGBA615

Shape612.geometry = LineSet613

HAnimSegment596.children.append(Shape612)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vt1'/> to <HAnimSite name='cervicale'/>
Shape616 = x3d.Shape()
LineSet617 = x3d.LineSet()
LineSet617.vertexCount = [2]
Coordinate618 = x3d.Coordinate()
Coordinate618.point = (0.0065,1.4951,-0.0387,0.0064,1.5200,-0.0815)

LineSet617.coord = Coordinate618
ColorRGBA619 = x3d.ColorRGBA()
ColorRGBA619.USE = "HAnimSiteLineColorRGBA"

LineSet617.color = ColorRGBA619

Shape616.geometry = LineSet617

HAnimSegment596.children.append(Shape616)
HAnimSite620 = x3d.HAnimSite()
HAnimSite620.name = "suprasternale_pt"
HAnimSite620.DEF = "hanim_suprasternale_pt"
HAnimSite620.translation = [0.0084,1.4714,0.0551]
#HAnimSite visualization shape
TouchSensor621 = x3d.TouchSensor()
TouchSensor621.description = "HAnimSite suprasternale"

HAnimSite620.children.append(TouchSensor621)
Shape622 = x3d.Shape()
Shape622.USE = "HAnimSiteShape"

HAnimSite620.children.append(Shape622)

HAnimSegment596.children.append(HAnimSite620)
HAnimSite623 = x3d.HAnimSite()
HAnimSite623.name = "cervicale_pt"
HAnimSite623.DEF = "hanim_cervicale_pt"
HAnimSite623.translation = [0.0064,1.52,-0.0815]
#HAnimSite visualization shape
TouchSensor624 = x3d.TouchSensor()
TouchSensor624.description = "HAnimSite cervicale"

HAnimSite623.children.append(TouchSensor624)
Shape625 = x3d.Shape()
Shape625.USE = "HAnimSiteShape"

HAnimSite623.children.append(Shape625)

HAnimSegment596.children.append(HAnimSite623)

HAnimJoint595.children.append(HAnimSegment596)
HAnimJoint626 = x3d.HAnimJoint()
HAnimJoint626.name = "vc7"
HAnimJoint626.DEF = "hanim_vc7"
HAnimJoint626.center = [0.0066,1.5132,-0.0301]
HAnimJoint626.ulimit = [0,0,0]
HAnimJoint626.llimit = [0,0,0]
HAnimSegment627 = x3d.HAnimSegment()
HAnimSegment627.name = "c7"
HAnimSegment627.DEF = "hanim_c7"
#<HAnimJoint name='vc7'/> visualization sphere within <HAnimSegment name='c7'/>
TouchSensor628 = x3d.TouchSensor()
TouchSensor628.description = "HAnimJoint vc7, HAnimSegment c7"

HAnimSegment627.children.append(TouchSensor628)
Transform629 = x3d.Transform()
Transform629.translation = [0.0066,1.5132,-0.0301]
Shape630 = x3d.Shape()
Shape630.USE = "HAnimJointShape"

Transform629.children.append(Shape630)

HAnimSegment627.children.append(Transform629)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vc7'/> to <HAnimJoint name='vc6'/>
Shape631 = x3d.Shape()
LineSet632 = x3d.LineSet()
LineSet632.vertexCount = [2]
Coordinate633 = x3d.Coordinate()
Coordinate633.point = (0.0066,1.5132,-0.0301,0.0066,1.5357,-0.0143)

LineSet632.coord = Coordinate633
ColorRGBA634 = x3d.ColorRGBA()
ColorRGBA634.USE = "HAnimSegmentLineColorRGBA"

LineSet632.color = ColorRGBA634

Shape631.geometry = LineSet632

HAnimSegment627.children.append(Shape631)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vc7'/> to <HAnimSite name='r_neck_base'/>
Shape635 = x3d.Shape()
LineSet636 = x3d.LineSet()
LineSet636.vertexCount = [2]
Coordinate637 = x3d.Coordinate()
Coordinate637.point = (0.0066,1.5132,-0.0301,-0.0419,1.5149,-0.0220)

LineSet636.coord = Coordinate637
ColorRGBA638 = x3d.ColorRGBA()
ColorRGBA638.USE = "HAnimSiteLineColorRGBA"

LineSet636.color = ColorRGBA638

Shape635.geometry = LineSet636

HAnimSegment627.children.append(Shape635)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vc7'/> to <HAnimSite name='l_neck_base'/>
Shape639 = x3d.Shape()
LineSet640 = x3d.LineSet()
LineSet640.vertexCount = [2]
Coordinate641 = x3d.Coordinate()
Coordinate641.point = (0.0066,1.5132,-0.0301,0.0646,1.5141,-0.0380)

LineSet640.coord = Coordinate641
ColorRGBA642 = x3d.ColorRGBA()
ColorRGBA642.USE = "HAnimSiteLineColorRGBA"

LineSet640.color = ColorRGBA642

Shape639.geometry = LineSet640

HAnimSegment627.children.append(Shape639)
HAnimSite643 = x3d.HAnimSite()
HAnimSite643.name = "r_neck_base_pt"
HAnimSite643.DEF = "hanim_r_neck_base_pt"
HAnimSite643.translation = [-0.0419,1.5149,-0.022]
#HAnimSite visualization shape
TouchSensor644 = x3d.TouchSensor()
TouchSensor644.description = "HAnimSite r_neck_base"

HAnimSite643.children.append(TouchSensor644)
Shape645 = x3d.Shape()
Shape645.USE = "HAnimSiteShape"

HAnimSite643.children.append(Shape645)

HAnimSegment627.children.append(HAnimSite643)
HAnimSite646 = x3d.HAnimSite()
HAnimSite646.name = "l_neck_base_pt"
HAnimSite646.DEF = "hanim_l_neck_base_pt"
HAnimSite646.translation = [0.0646,1.5141,-0.038]
#HAnimSite visualization shape
TouchSensor647 = x3d.TouchSensor()
TouchSensor647.description = "HAnimSite l_neck_base"

HAnimSite646.children.append(TouchSensor647)
Shape648 = x3d.Shape()
Shape648.USE = "HAnimSiteShape"

HAnimSite646.children.append(Shape648)

HAnimSegment627.children.append(HAnimSite646)

HAnimJoint626.children.append(HAnimSegment627)
HAnimJoint649 = x3d.HAnimJoint()
HAnimJoint649.name = "vc6"
HAnimJoint649.DEF = "hanim_vc6"
HAnimJoint649.center = [0.0066,1.5357,-0.0143]
HAnimJoint649.ulimit = [0,0,0]
HAnimJoint649.llimit = [0,0,0]
HAnimSegment650 = x3d.HAnimSegment()
HAnimSegment650.name = "c6"
HAnimSegment650.DEF = "hanim_c6"
#<HAnimJoint name='vc6'/> visualization sphere within <HAnimSegment name='c6'/>
TouchSensor651 = x3d.TouchSensor()
TouchSensor651.description = "HAnimJoint vc6, HAnimSegment c6"

HAnimSegment650.children.append(TouchSensor651)
Transform652 = x3d.Transform()
Transform652.translation = [0.0066,1.5357,-0.0143]
Shape653 = x3d.Shape()
Shape653.USE = "HAnimJointShape"

Transform652.children.append(Shape653)

HAnimSegment650.children.append(Transform652)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vc6'/> to <HAnimJoint name='vc5'/>
Shape654 = x3d.Shape()
LineSet655 = x3d.LineSet()
LineSet655.vertexCount = [2]
Coordinate656 = x3d.Coordinate()
Coordinate656.point = (0.0066,1.5357,-0.0143,0.0066,1.5520,-0.0082)

LineSet655.coord = Coordinate656
ColorRGBA657 = x3d.ColorRGBA()
ColorRGBA657.USE = "HAnimSegmentLineColorRGBA"

LineSet655.color = ColorRGBA657

Shape654.geometry = LineSet655

HAnimSegment650.children.append(Shape654)

HAnimJoint649.children.append(HAnimSegment650)
HAnimJoint658 = x3d.HAnimJoint()
HAnimJoint658.name = "vc5"
HAnimJoint658.DEF = "hanim_vc5"
HAnimJoint658.center = [0.0066,1.552,-0.0082]
HAnimJoint658.ulimit = [0,0,0]
HAnimJoint658.llimit = [0,0,0]
HAnimSegment659 = x3d.HAnimSegment()
HAnimSegment659.name = "c5"
HAnimSegment659.DEF = "hanim_c5"
#<HAnimJoint name='vc5'/> visualization sphere within <HAnimSegment name='c5'/>
TouchSensor660 = x3d.TouchSensor()
TouchSensor660.description = "HAnimJoint vc5, HAnimSegment c5"

HAnimSegment659.children.append(TouchSensor660)
Transform661 = x3d.Transform()
Transform661.translation = [0.0066,1.552,-0.0082]
Shape662 = x3d.Shape()
Shape662.USE = "HAnimJointShape"

Transform661.children.append(Shape662)

HAnimSegment659.children.append(Transform661)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vc5'/> to <HAnimJoint name='vc4'/>
Shape663 = x3d.Shape()
LineSet664 = x3d.LineSet()
LineSet664.vertexCount = [2]
Coordinate665 = x3d.Coordinate()
Coordinate665.point = (0.0066,1.5520,-0.0082,0.0066,1.5662,-0.0084)

LineSet664.coord = Coordinate665
ColorRGBA666 = x3d.ColorRGBA()
ColorRGBA666.USE = "HAnimSegmentLineColorRGBA"

LineSet664.color = ColorRGBA666

Shape663.geometry = LineSet664

HAnimSegment659.children.append(Shape663)

HAnimJoint658.children.append(HAnimSegment659)
HAnimJoint667 = x3d.HAnimJoint()
HAnimJoint667.name = "vc4"
HAnimJoint667.DEF = "hanim_vc4"
HAnimJoint667.center = [0.0066,1.5662,-0.0084]
HAnimJoint667.ulimit = [0,0,0]
HAnimJoint667.llimit = [0,0,0]
HAnimSegment668 = x3d.HAnimSegment()
HAnimSegment668.name = "c4"
HAnimSegment668.DEF = "hanim_c4"
#<HAnimJoint name='vc4'/> visualization sphere within <HAnimSegment name='c4'/>
TouchSensor669 = x3d.TouchSensor()
TouchSensor669.description = "HAnimJoint vc4, HAnimSegment c4"

HAnimSegment668.children.append(TouchSensor669)
Transform670 = x3d.Transform()
Transform670.translation = [0.0066,1.5662,-0.0084]
Shape671 = x3d.Shape()
Shape671.USE = "HAnimJointShape"

Transform670.children.append(Shape671)

HAnimSegment668.children.append(Transform670)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vc4'/> to <HAnimJoint name='vc3'/>
Shape672 = x3d.Shape()
LineSet673 = x3d.LineSet()
LineSet673.vertexCount = [2]
Coordinate674 = x3d.Coordinate()
Coordinate674.point = (0.0066,1.5662,-0.0084,0.0066,1.5800,-0.0103)

LineSet673.coord = Coordinate674
ColorRGBA675 = x3d.ColorRGBA()
ColorRGBA675.USE = "HAnimSegmentLineColorRGBA"

LineSet673.color = ColorRGBA675

Shape672.geometry = LineSet673

HAnimSegment668.children.append(Shape672)

HAnimJoint667.children.append(HAnimSegment668)
HAnimJoint676 = x3d.HAnimJoint()
HAnimJoint676.name = "vc3"
HAnimJoint676.DEF = "hanim_vc3"
HAnimJoint676.center = [0.0066,1.58,-0.0103]
HAnimJoint676.ulimit = [0,0,0]
HAnimJoint676.llimit = [0,0,0]
HAnimSegment677 = x3d.HAnimSegment()
HAnimSegment677.name = "c3"
HAnimSegment677.DEF = "hanim_c3"
#<HAnimJoint name='vc3'/> visualization sphere within <HAnimSegment name='c3'/>
TouchSensor678 = x3d.TouchSensor()
TouchSensor678.description = "HAnimJoint vc3, HAnimSegment c3"

HAnimSegment677.children.append(TouchSensor678)
Transform679 = x3d.Transform()
Transform679.translation = [0.0066,1.58,-0.0103]
Shape680 = x3d.Shape()
Shape680.USE = "HAnimJointShape"

Transform679.children.append(Shape680)

HAnimSegment677.children.append(Transform679)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vc3'/> to <HAnimJoint name='vc2'/>
Shape681 = x3d.Shape()
LineSet682 = x3d.LineSet()
LineSet682.vertexCount = [2]
Coordinate683 = x3d.Coordinate()
Coordinate683.point = (0.0066,1.5800,-0.0103,0.0066,1.5928,-0.0103)

LineSet682.coord = Coordinate683
ColorRGBA684 = x3d.ColorRGBA()
ColorRGBA684.USE = "HAnimSegmentLineColorRGBA"

LineSet682.color = ColorRGBA684

Shape681.geometry = LineSet682

HAnimSegment677.children.append(Shape681)

HAnimJoint676.children.append(HAnimSegment677)
HAnimJoint685 = x3d.HAnimJoint()
HAnimJoint685.name = "vc2"
HAnimJoint685.DEF = "hanim_vc2"
HAnimJoint685.center = [0.0066,1.5928,-0.0103]
HAnimJoint685.ulimit = [0,0,0]
HAnimJoint685.llimit = [0,0,0]
HAnimSegment686 = x3d.HAnimSegment()
HAnimSegment686.name = "c2"
HAnimSegment686.DEF = "hanim_c2"
#<HAnimJoint name='vc2'/> visualization sphere within <HAnimSegment name='c2'/>
TouchSensor687 = x3d.TouchSensor()
TouchSensor687.description = "HAnimJoint vc2, HAnimSegment c2"

HAnimSegment686.children.append(TouchSensor687)
Transform688 = x3d.Transform()
Transform688.translation = [0.0066,1.5928,-0.0103]
Shape689 = x3d.Shape()
Shape689.USE = "HAnimJointShape"

Transform688.children.append(Shape689)

HAnimSegment686.children.append(Transform688)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vc2'/> to <HAnimJoint name='vc1'/>
Shape690 = x3d.Shape()
LineSet691 = x3d.LineSet()
LineSet691.vertexCount = [2]
Coordinate692 = x3d.Coordinate()
Coordinate692.point = (0.0066,1.5928,-0.0103,0.0066,1.6144,-0.0034)

LineSet691.coord = Coordinate692
ColorRGBA693 = x3d.ColorRGBA()
ColorRGBA693.USE = "HAnimSegmentLineColorRGBA"

LineSet691.color = ColorRGBA693

Shape690.geometry = LineSet691

HAnimSegment686.children.append(Shape690)

HAnimJoint685.children.append(HAnimSegment686)
HAnimJoint694 = x3d.HAnimJoint()
HAnimJoint694.name = "vc1"
HAnimJoint694.DEF = "hanim_vc1"
HAnimJoint694.center = [0.0066,1.6144,-0.0034]
HAnimJoint694.ulimit = [0,0,0]
HAnimJoint694.llimit = [0,0,0]
HAnimSegment695 = x3d.HAnimSegment()
HAnimSegment695.name = "c1"
HAnimSegment695.DEF = "hanim_c1"
#<HAnimJoint name='vc1'/> visualization sphere within <HAnimSegment name='c1'/>
TouchSensor696 = x3d.TouchSensor()
TouchSensor696.description = "HAnimJoint vc1, HAnimSegment c1"

HAnimSegment695.children.append(TouchSensor696)
Transform697 = x3d.Transform()
Transform697.translation = [0.0066,1.6144,-0.0034]
Shape698 = x3d.Shape()
Shape698.USE = "HAnimJointShape"

Transform697.children.append(Shape698)

HAnimSegment695.children.append(Transform697)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vc1'/> to <HAnimJoint name='skullbase'/>
Shape699 = x3d.Shape()
LineSet700 = x3d.LineSet()
LineSet700.vertexCount = [2]
Coordinate701 = x3d.Coordinate()
Coordinate701.point = (0.0066,1.6144,-0.0034,0.0044,1.6209,0.0236)

LineSet700.coord = Coordinate701
ColorRGBA702 = x3d.ColorRGBA()
ColorRGBA702.USE = "HAnimSegmentLineColorRGBA"

LineSet700.color = ColorRGBA702

Shape699.geometry = LineSet700

HAnimSegment695.children.append(Shape699)

HAnimJoint694.children.append(HAnimSegment695)
HAnimJoint703 = x3d.HAnimJoint()
HAnimJoint703.name = "skullbase"
HAnimJoint703.DEF = "hanim_skullbase"
HAnimJoint703.center = [0.0044,1.6209,0.0236]
HAnimJoint703.ulimit = [0,0,0]
HAnimJoint703.llimit = [0,0,0]
HAnimSegment704 = x3d.HAnimSegment()
HAnimSegment704.name = "skull"
HAnimSegment704.DEF = "hanim_skull"
#<HAnimJoint name='skullbase'/> visualization sphere within <HAnimSegment name='skull'/>
TouchSensor705 = x3d.TouchSensor()
TouchSensor705.description = "HAnimJoint skullbase, HAnimSegment skull"

HAnimSegment704.children.append(TouchSensor705)
Transform706 = x3d.Transform()
Transform706.translation = [0.0044,1.6209,0.0236]
Shape707 = x3d.Shape()
Shape707.USE = "HAnimJointShape"

Transform706.children.append(Shape707)

HAnimSegment704.children.append(Transform706)
#HAnimSegment visualization line segment from parent <HAnimJoint name='skullbase'/> to <HAnimJoint name='l_eyeball_joint'/>
Shape708 = x3d.Shape()
LineSet709 = x3d.LineSet()
LineSet709.vertexCount = [2]
Coordinate710 = x3d.Coordinate()
Coordinate710.point = (0.0044,1.6209,0.0236,0.0336,1.6332,0.0502)

LineSet709.coord = Coordinate710
ColorRGBA711 = x3d.ColorRGBA()
ColorRGBA711.USE = "HAnimSegmentLineColorRGBA"

LineSet709.color = ColorRGBA711

Shape708.geometry = LineSet709

HAnimSegment704.children.append(Shape708)
#HAnimSegment visualization line segment from parent <HAnimJoint name='skullbase'/> to <HAnimJoint name='l_eyelid_joint'/>
Shape712 = x3d.Shape()
LineSet713 = x3d.LineSet()
LineSet713.vertexCount = [2]
Coordinate714 = x3d.Coordinate()
Coordinate714.point = (0.0044,1.6209,0.0236,0.0336,1.6332,0.0502)

LineSet713.coord = Coordinate714
ColorRGBA715 = x3d.ColorRGBA()
ColorRGBA715.USE = "HAnimSegmentLineColorRGBA"

LineSet713.color = ColorRGBA715

Shape712.geometry = LineSet713

HAnimSegment704.children.append(Shape712)
#HAnimSegment visualization line segment from parent <HAnimJoint name='skullbase'/> to <HAnimJoint name='l_eyebrow_joint'/>
Shape716 = x3d.Shape()
LineSet717 = x3d.LineSet()
LineSet717.vertexCount = [2]
Coordinate718 = x3d.Coordinate()
Coordinate718.point = (0.0044,1.6209,0.0236,0.0336,1.6350,0.0506)

LineSet717.coord = Coordinate718
ColorRGBA719 = x3d.ColorRGBA()
ColorRGBA719.USE = "HAnimSegmentLineColorRGBA"

LineSet717.color = ColorRGBA719

Shape716.geometry = LineSet717

HAnimSegment704.children.append(Shape716)
#HAnimSegment visualization line segment from parent <HAnimJoint name='skullbase'/> to <HAnimJoint name='r_eyeball_joint'/>
Shape720 = x3d.Shape()
LineSet721 = x3d.LineSet()
LineSet721.vertexCount = [2]
Coordinate722 = x3d.Coordinate()
Coordinate722.point = (0.0044,1.6209,0.0236,-0.0336,1.6332,0.0502)

LineSet721.coord = Coordinate722
ColorRGBA723 = x3d.ColorRGBA()
ColorRGBA723.USE = "HAnimSegmentLineColorRGBA"

LineSet721.color = ColorRGBA723

Shape720.geometry = LineSet721

HAnimSegment704.children.append(Shape720)
#HAnimSegment visualization line segment from parent <HAnimJoint name='skullbase'/> to <HAnimJoint name='r_eyelid_joint'/>
Shape724 = x3d.Shape()
LineSet725 = x3d.LineSet()
LineSet725.vertexCount = [2]
Coordinate726 = x3d.Coordinate()
Coordinate726.point = (0.0044,1.6209,0.0236,-0.0336,1.6332,0.0502)

LineSet725.coord = Coordinate726
ColorRGBA727 = x3d.ColorRGBA()
ColorRGBA727.USE = "HAnimSegmentLineColorRGBA"

LineSet725.color = ColorRGBA727

Shape724.geometry = LineSet725

HAnimSegment704.children.append(Shape724)
#HAnimSegment visualization line segment from parent <HAnimJoint name='skullbase'/> to <HAnimJoint name='r_eyebrow_joint'/>
Shape728 = x3d.Shape()
LineSet729 = x3d.LineSet()
LineSet729.vertexCount = [2]
Coordinate730 = x3d.Coordinate()
Coordinate730.point = (0.0044,1.6209,0.0236,-0.0336,1.6350,0.0506)

LineSet729.coord = Coordinate730
ColorRGBA731 = x3d.ColorRGBA()
ColorRGBA731.USE = "HAnimSegmentLineColorRGBA"

LineSet729.color = ColorRGBA731

Shape728.geometry = LineSet729

HAnimSegment704.children.append(Shape728)
#HAnimSegment visualization line segment from parent <HAnimJoint name='skullbase'/> to <HAnimJoint name='temporomandibular'/>
Shape732 = x3d.Shape()
LineSet733 = x3d.LineSet()
LineSet733.vertexCount = [2]
Coordinate734 = x3d.Coordinate()
Coordinate734.point = (0.0044,1.6209,0.0236,0.0000,1.6300,0.0150)

LineSet733.coord = Coordinate734
ColorRGBA735 = x3d.ColorRGBA()
ColorRGBA735.USE = "HAnimSegmentLineColorRGBA"

LineSet733.color = ColorRGBA735

Shape732.geometry = LineSet733

HAnimSegment704.children.append(Shape732)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='skullbase'/> to <HAnimSite name='skull_tip'/>
Shape736 = x3d.Shape()
LineSet737 = x3d.LineSet()
LineSet737.vertexCount = [2]
Coordinate738 = x3d.Coordinate()
Coordinate738.point = (0.0044,1.6209,0.0236,0.0050,1.7504,0.0055)

LineSet737.coord = Coordinate738
ColorRGBA739 = x3d.ColorRGBA()
ColorRGBA739.USE = "HAnimSiteLineColorRGBA"

LineSet737.color = ColorRGBA739

Shape736.geometry = LineSet737

HAnimSegment704.children.append(Shape736)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='skullbase'/> to <HAnimSite name='sellion'/>
Shape740 = x3d.Shape()
LineSet741 = x3d.LineSet()
LineSet741.vertexCount = [2]
Coordinate742 = x3d.Coordinate()
Coordinate742.point = (0.0044,1.6209,0.0236,0.0058,1.6316,0.0852)

LineSet741.coord = Coordinate742
ColorRGBA743 = x3d.ColorRGBA()
ColorRGBA743.USE = "HAnimSiteLineColorRGBA"

LineSet741.color = ColorRGBA743

Shape740.geometry = LineSet741

HAnimSegment704.children.append(Shape740)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='skullbase'/> to <HAnimSite name='r_infraorbitale'/>
Shape744 = x3d.Shape()
LineSet745 = x3d.LineSet()
LineSet745.vertexCount = [2]
Coordinate746 = x3d.Coordinate()
Coordinate746.point = (0.0044,1.6209,0.0236,-0.0237,1.6171,0.0752)

LineSet745.coord = Coordinate746
ColorRGBA747 = x3d.ColorRGBA()
ColorRGBA747.USE = "HAnimSiteLineColorRGBA"

LineSet745.color = ColorRGBA747

Shape744.geometry = LineSet745

HAnimSegment704.children.append(Shape744)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='skullbase'/> to <HAnimSite name='l_infraorbitale'/>
Shape748 = x3d.Shape()
LineSet749 = x3d.LineSet()
LineSet749.vertexCount = [2]
Coordinate750 = x3d.Coordinate()
Coordinate750.point = (0.0044,1.6209,0.0236,0.0341,1.6171,0.0752)

LineSet749.coord = Coordinate750
ColorRGBA751 = x3d.ColorRGBA()
ColorRGBA751.USE = "HAnimSiteLineColorRGBA"

LineSet749.color = ColorRGBA751

Shape748.geometry = LineSet749

HAnimSegment704.children.append(Shape748)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='skullbase'/> to <HAnimSite name='supramenton'/>
Shape752 = x3d.Shape()
LineSet753 = x3d.LineSet()
LineSet753.vertexCount = [2]
Coordinate754 = x3d.Coordinate()
Coordinate754.point = (0.0044,1.6209,0.0236,0.0061,1.5410,0.0805)

LineSet753.coord = Coordinate754
ColorRGBA755 = x3d.ColorRGBA()
ColorRGBA755.USE = "HAnimSiteLineColorRGBA"

LineSet753.color = ColorRGBA755

Shape752.geometry = LineSet753

HAnimSegment704.children.append(Shape752)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='skullbase'/> to <HAnimSite name='r_tragion'/>
Shape756 = x3d.Shape()
LineSet757 = x3d.LineSet()
LineSet757.vertexCount = [2]
Coordinate758 = x3d.Coordinate()
Coordinate758.point = (0.0044,1.6209,0.0236,-0.0646,1.6347,0.0302)

LineSet757.coord = Coordinate758
ColorRGBA759 = x3d.ColorRGBA()
ColorRGBA759.USE = "HAnimSiteLineColorRGBA"

LineSet757.color = ColorRGBA759

Shape756.geometry = LineSet757

HAnimSegment704.children.append(Shape756)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='skullbase'/> to <HAnimSite name='r_gonion'/>
Shape760 = x3d.Shape()
LineSet761 = x3d.LineSet()
LineSet761.vertexCount = [2]
Coordinate762 = x3d.Coordinate()
Coordinate762.point = (0.0044,1.6209,0.0236,-0.0520,1.5529,0.0347)

LineSet761.coord = Coordinate762
ColorRGBA763 = x3d.ColorRGBA()
ColorRGBA763.USE = "HAnimSiteLineColorRGBA"

LineSet761.color = ColorRGBA763

Shape760.geometry = LineSet761

HAnimSegment704.children.append(Shape760)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='skullbase'/> to <HAnimSite name='l_tragion'/>
Shape764 = x3d.Shape()
LineSet765 = x3d.LineSet()
LineSet765.vertexCount = [2]
Coordinate766 = x3d.Coordinate()
Coordinate766.point = (0.0044,1.6209,0.0236,0.0739,1.6348,0.0282)

LineSet765.coord = Coordinate766
ColorRGBA767 = x3d.ColorRGBA()
ColorRGBA767.USE = "HAnimSiteLineColorRGBA"

LineSet765.color = ColorRGBA767

Shape764.geometry = LineSet765

HAnimSegment704.children.append(Shape764)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='skullbase'/> to <HAnimSite name='l_gonion'/>
Shape768 = x3d.Shape()
LineSet769 = x3d.LineSet()
LineSet769.vertexCount = [2]
Coordinate770 = x3d.Coordinate()
Coordinate770.point = (0.0044,1.6209,0.0236,0.0631,1.5530,0.0330)

LineSet769.coord = Coordinate770
ColorRGBA771 = x3d.ColorRGBA()
ColorRGBA771.USE = "HAnimSiteLineColorRGBA"

LineSet769.color = ColorRGBA771

Shape768.geometry = LineSet769

HAnimSegment704.children.append(Shape768)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='skullbase'/> to <HAnimSite name='nuchale'/>
Shape772 = x3d.Shape()
LineSet773 = x3d.LineSet()
LineSet773.vertexCount = [2]
Coordinate774 = x3d.Coordinate()
Coordinate774.point = (0.0044,1.6209,0.0236,0.0039,1.5972,-0.0796)

LineSet773.coord = Coordinate774
ColorRGBA775 = x3d.ColorRGBA()
ColorRGBA775.USE = "HAnimSiteLineColorRGBA"

LineSet773.color = ColorRGBA775

Shape772.geometry = LineSet773

HAnimSegment704.children.append(Shape772)
#TODO move skull_tip x to zero
HAnimSite776 = x3d.HAnimSite()
HAnimSite776.name = "skull_tip"
HAnimSite776.DEF = "hanim_skull_tip"
HAnimSite776.translation = [0.005,1.7504,0.0055]
#HAnimSite visualization shape
TouchSensor777 = x3d.TouchSensor()
TouchSensor777.description = "HAnimSite skull_tip"

HAnimSite776.children.append(TouchSensor777)
Shape778 = x3d.Shape()
Shape778.USE = "HAnimSiteShape"

HAnimSite776.children.append(Shape778)

HAnimSegment704.children.append(HAnimSite776)
HAnimSite779 = x3d.HAnimSite()
HAnimSite779.name = "sellion_pt"
HAnimSite779.DEF = "hanim_sellion_pt"
HAnimSite779.translation = [0.0058,1.6316,0.0852]
#HAnimSite visualization shape
TouchSensor780 = x3d.TouchSensor()
TouchSensor780.description = "HAnimSite sellion"

HAnimSite779.children.append(TouchSensor780)
Shape781 = x3d.Shape()
Shape781.USE = "HAnimSiteShape"

HAnimSite779.children.append(Shape781)

HAnimSegment704.children.append(HAnimSite779)
HAnimSite782 = x3d.HAnimSite()
HAnimSite782.name = "r_infraorbitale_pt"
HAnimSite782.DEF = "hanim_r_infraorbitale_pt"
HAnimSite782.translation = [-0.0237,1.6171,0.0752]
#HAnimSite visualization shape
TouchSensor783 = x3d.TouchSensor()
TouchSensor783.description = "HAnimSite r_infraorbitale"

HAnimSite782.children.append(TouchSensor783)
Shape784 = x3d.Shape()
Shape784.USE = "HAnimSiteShape"

HAnimSite782.children.append(Shape784)

HAnimSegment704.children.append(HAnimSite782)
HAnimSite785 = x3d.HAnimSite()
HAnimSite785.name = "l_infraorbitale_pt"
HAnimSite785.DEF = "hanim_l_infraorbitale_pt"
HAnimSite785.translation = [0.0341,1.6171,0.0752]
#HAnimSite visualization shape
TouchSensor786 = x3d.TouchSensor()
TouchSensor786.description = "HAnimSite l_infraorbitale"

HAnimSite785.children.append(TouchSensor786)
Shape787 = x3d.Shape()
Shape787.USE = "HAnimSiteShape"

HAnimSite785.children.append(Shape787)

HAnimSegment704.children.append(HAnimSite785)
HAnimSite788 = x3d.HAnimSite()
HAnimSite788.name = "supramenton_pt"
HAnimSite788.DEF = "hanim_supramenton_pt"
HAnimSite788.translation = [0.0061,1.541,0.0805]
#HAnimSite visualization shape
TouchSensor789 = x3d.TouchSensor()
TouchSensor789.description = "HAnimSite supramenton"

HAnimSite788.children.append(TouchSensor789)
Shape790 = x3d.Shape()
Shape790.USE = "HAnimSiteShape"

HAnimSite788.children.append(Shape790)

HAnimSegment704.children.append(HAnimSite788)
HAnimSite791 = x3d.HAnimSite()
HAnimSite791.name = "r_tragion_pt"
HAnimSite791.DEF = "hanim_r_tragion_pt"
HAnimSite791.translation = [-0.0646,1.6347,0.0302]
#HAnimSite visualization shape
TouchSensor792 = x3d.TouchSensor()
TouchSensor792.description = "HAnimSite r_tragion"

HAnimSite791.children.append(TouchSensor792)
Shape793 = x3d.Shape()
Shape793.USE = "HAnimSiteShape"

HAnimSite791.children.append(Shape793)

HAnimSegment704.children.append(HAnimSite791)
HAnimSite794 = x3d.HAnimSite()
HAnimSite794.name = "r_gonion_pt"
HAnimSite794.DEF = "hanim_r_gonion_pt"
HAnimSite794.translation = [-0.052,1.5529,0.0347]
#HAnimSite visualization shape
TouchSensor795 = x3d.TouchSensor()
TouchSensor795.description = "HAnimSite r_gonion"

HAnimSite794.children.append(TouchSensor795)
Shape796 = x3d.Shape()
Shape796.USE = "HAnimSiteShape"

HAnimSite794.children.append(Shape796)

HAnimSegment704.children.append(HAnimSite794)
HAnimSite797 = x3d.HAnimSite()
HAnimSite797.name = "l_tragion_pt"
HAnimSite797.DEF = "hanim_l_tragion_pt"
HAnimSite797.translation = [0.0739,1.6348,0.0282]
#HAnimSite visualization shape
TouchSensor798 = x3d.TouchSensor()
TouchSensor798.description = "HAnimSite l_tragion"

HAnimSite797.children.append(TouchSensor798)
Shape799 = x3d.Shape()
Shape799.USE = "HAnimSiteShape"

HAnimSite797.children.append(Shape799)

HAnimSegment704.children.append(HAnimSite797)
HAnimSite800 = x3d.HAnimSite()
HAnimSite800.name = "l_gonion_pt"
HAnimSite800.DEF = "hanim_l_gonion_pt"
HAnimSite800.translation = [0.0631,1.553,0.033]
#HAnimSite visualization shape
TouchSensor801 = x3d.TouchSensor()
TouchSensor801.description = "HAnimSite l_gonion"

HAnimSite800.children.append(TouchSensor801)
Shape802 = x3d.Shape()
Shape802.USE = "HAnimSiteShape"

HAnimSite800.children.append(Shape802)

HAnimSegment704.children.append(HAnimSite800)
HAnimSite803 = x3d.HAnimSite()
HAnimSite803.name = "nuchale_pt"
HAnimSite803.DEF = "hanim_nuchale_pt"
HAnimSite803.translation = [0.0039,1.5972,-0.0796]
#HAnimSite visualization shape
TouchSensor804 = x3d.TouchSensor()
TouchSensor804.description = "HAnimSite nuchale"

HAnimSite803.children.append(TouchSensor804)
Shape805 = x3d.Shape()
Shape805.USE = "HAnimSiteShape"

HAnimSite803.children.append(Shape805)

HAnimSegment704.children.append(HAnimSite803)

HAnimJoint703.children.append(HAnimSegment704)
HAnimJoint806 = x3d.HAnimJoint()
HAnimJoint806.name = "l_eyeball_joint"
HAnimJoint806.DEF = "hanim_l_eyeball_joint"
HAnimJoint806.center = [0.0336,1.6332,0.0502]
HAnimJoint806.ulimit = [0,0,0]
HAnimJoint806.llimit = [0,0,0]
HAnimSegment807 = x3d.HAnimSegment()
HAnimSegment807.name = "l_eyeball"
HAnimSegment807.DEF = "hanim_l_eyeball"
#<HAnimJoint name='l_eyeball_joint'/> visualization sphere within <HAnimSegment name='l_eyeball'/>
TouchSensor808 = x3d.TouchSensor()
TouchSensor808.description = "HAnimJoint l_eyeball_joint, HAnimSegment l_eyeball"

HAnimSegment807.children.append(TouchSensor808)
Transform809 = x3d.Transform()
Transform809.translation = [0.0336,1.6332,0.0502]
Shape810 = x3d.Shape()
Shape810.USE = "HAnimJointShape"

Transform809.children.append(Shape810)

HAnimSegment807.children.append(Transform809)
#HAnimSite/Viewpoint visualization line segment from ancestor <HAnimJoint name='l_eyeball_joint'/> to <HAnimSite name='l_eyeball_site_view'/>
Shape811 = x3d.Shape()
LineSet812 = x3d.LineSet()
LineSet812.vertexCount = [2]
Coordinate813 = x3d.Coordinate()
Coordinate813.point = (0.0336,1.6332,0.0502,0.0340,1.6400,0.0500)

LineSet812.coord = Coordinate813
ColorRGBA814 = x3d.ColorRGBA()
ColorRGBA814.DEF = "HAnimSiteViewpointLineColorRGBA"
ColorRGBA814.color = [0,0,1,1,0,0,1,0.1]

LineSet812.color = ColorRGBA814

Shape811.geometry = LineSet812

HAnimSegment807.children.append(Shape811)
HAnimSite815 = x3d.HAnimSite()
HAnimSite815.name = "l_eyeball_site_view"
HAnimSite815.DEF = "hanim_l_eyeball_site_view"
HAnimSite815.translation = [0.034,1.64,0.05]
Viewpoint816 = x3d.Viewpoint()
Viewpoint816.DEF = "hanim_l_eyeball_site_viewpoint"
Viewpoint816.description = "l_eyeball_site_viewpoint looking forward"
Viewpoint816.orientation = [0,1,0,3.141593]
Viewpoint816.position = [0,0,0]

HAnimSite815.children.append(Viewpoint816)
#HAnimSite/Viewpoint visualization shape
Anchor817 = x3d.Anchor()
Anchor817.description = "HAnimSite Viewpoint hanim_l_eyeball_site_view"
Anchor817.url = ["#hanim_l_eyeball_site_viewpoint"]
LOD818 = x3d.LOD()
LOD818.forceTransitions = True
LOD818.range = [0.04]
WorldInfo819 = x3d.WorldInfo()
WorldInfo819.info = ["hide diamond when close"]

LOD818.children.append(WorldInfo819)
Shape820 = x3d.Shape()
Shape820.DEF = "HAnimSiteViewpointShape"
IndexedFaceSet821 = x3d.IndexedFaceSet()
IndexedFaceSet821.DEF = "SiteViewpointDiamondIFS"
IndexedFaceSet821.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet821.creaseAngle = 0.5
Coordinate822 = x3d.Coordinate()
Coordinate822.point = (0.0000,0.0100,0.0000,-0.0100,0.0000,0.0000,0.0000,0.0000,0.0100,0.0100,0.0000,0.0000,0.0000,0.0000,-0.0100,0.0000,-0.0100,0.0000)

IndexedFaceSet821.coord = Coordinate822

Shape820.geometry = IndexedFaceSet821
Appearance823 = x3d.Appearance()
Material824 = x3d.Material()
Material824.diffuseColor = [0,0,1]
Material824.transparency = 0.6

Appearance823.material = Material824

Shape820.appearance = Appearance823

LOD818.children.append(Shape820)

Anchor817.children.append(LOD818)

HAnimSite815.children.append(Anchor817)

HAnimSegment807.children.append(HAnimSite815)

HAnimJoint806.children.append(HAnimSegment807)

HAnimJoint703.children.append(HAnimJoint806)
HAnimJoint825 = x3d.HAnimJoint()
HAnimJoint825.name = "l_eyelid_joint"
HAnimJoint825.DEF = "hanim_l_eyelid_joint"
HAnimJoint825.center = [0.0336,1.6332,0.0502]
HAnimJoint825.ulimit = [0,0,0]
HAnimJoint825.llimit = [0,0,0]
HAnimSegment826 = x3d.HAnimSegment()
HAnimSegment826.name = "l_eyelid"
HAnimSegment826.DEF = "hanim_l_eyelid"
#<HAnimJoint name='l_eyelid_joint'/> visualization sphere within <HAnimSegment name='l_eyelid'/>
TouchSensor827 = x3d.TouchSensor()
TouchSensor827.description = "HAnimJoint l_eyelid_joint, HAnimSegment l_eyelid"

HAnimSegment826.children.append(TouchSensor827)
Transform828 = x3d.Transform()
Transform828.translation = [0.0336,1.6332,0.0502]
Shape829 = x3d.Shape()
Shape829.USE = "HAnimJointShape"

Transform828.children.append(Shape829)

HAnimSegment826.children.append(Transform828)

HAnimJoint825.children.append(HAnimSegment826)

HAnimJoint703.children.append(HAnimJoint825)
HAnimJoint830 = x3d.HAnimJoint()
HAnimJoint830.name = "l_eyebrow_joint"
HAnimJoint830.DEF = "hanim_l_eyebrow_joint"
HAnimJoint830.center = [0.0336,1.635,0.0506]
HAnimJoint830.ulimit = [0,0,0]
HAnimJoint830.llimit = [0,0,0]
HAnimSegment831 = x3d.HAnimSegment()
HAnimSegment831.name = "l_eyebrow"
HAnimSegment831.DEF = "hanim_l_eyebrow"
#<HAnimJoint name='l_eyebrow_joint'/> visualization sphere within <HAnimSegment name='l_eyebrow'/>
TouchSensor832 = x3d.TouchSensor()
TouchSensor832.description = "HAnimJoint l_eyebrow_joint, HAnimSegment l_eyebrow"

HAnimSegment831.children.append(TouchSensor832)
Transform833 = x3d.Transform()
Transform833.translation = [0.0336,1.635,0.0506]
Shape834 = x3d.Shape()
Shape834.USE = "HAnimJointShape"

Transform833.children.append(Shape834)

HAnimSegment831.children.append(Transform833)

HAnimJoint830.children.append(HAnimSegment831)

HAnimJoint703.children.append(HAnimJoint830)
HAnimJoint835 = x3d.HAnimJoint()
HAnimJoint835.name = "r_eyeball_joint"
HAnimJoint835.DEF = "hanim_r_eyeball_joint"
HAnimJoint835.center = [-0.0336,1.6332,0.0502]
HAnimJoint835.ulimit = [0,0,0]
HAnimJoint835.llimit = [0,0,0]
HAnimSegment836 = x3d.HAnimSegment()
HAnimSegment836.name = "r_eyeball"
HAnimSegment836.DEF = "hanim_r_eyeball"
#<HAnimJoint name='r_eyeball_joint'/> visualization sphere within <HAnimSegment name='r_eyeball'/>
TouchSensor837 = x3d.TouchSensor()
TouchSensor837.description = "HAnimJoint r_eyeball_joint, HAnimSegment r_eyeball"

HAnimSegment836.children.append(TouchSensor837)
Transform838 = x3d.Transform()
Transform838.translation = [-0.0336,1.6332,0.0502]
Shape839 = x3d.Shape()
Shape839.USE = "HAnimJointShape"

Transform838.children.append(Shape839)

HAnimSegment836.children.append(Transform838)
#HAnimSite/Viewpoint visualization line segment from ancestor <HAnimJoint name='r_eyeball_joint'/> to <HAnimSite name='r_eyeball_site_view'/>
Shape840 = x3d.Shape()
LineSet841 = x3d.LineSet()
LineSet841.vertexCount = [2]
Coordinate842 = x3d.Coordinate()
Coordinate842.point = (-0.0336,1.6332,0.0502,-0.0340,1.6400,0.0500)

LineSet841.coord = Coordinate842
ColorRGBA843 = x3d.ColorRGBA()
ColorRGBA843.USE = "HAnimSiteViewpointLineColorRGBA"

LineSet841.color = ColorRGBA843

Shape840.geometry = LineSet841

HAnimSegment836.children.append(Shape840)
HAnimSite844 = x3d.HAnimSite()
HAnimSite844.name = "r_eyeball_site_view"
HAnimSite844.DEF = "hanim_r_eyeball_site_view"
HAnimSite844.translation = [-0.034,1.64,0.05]
Viewpoint845 = x3d.Viewpoint()
Viewpoint845.DEF = "hanim_r_eyeball_site_viewpoint"
Viewpoint845.description = "r_eyeball_site_viewpoint looking forward"
Viewpoint845.orientation = [0,1,0,3.141593]
Viewpoint845.position = [0,0,0]

HAnimSite844.children.append(Viewpoint845)
#HAnimSite/Viewpoint visualization shape
Anchor846 = x3d.Anchor()
Anchor846.description = "HAnimSite Viewpoint hanim_r_eyeball_site_view"
Anchor846.url = ["#hanim_r_eyeball_site_viewpoint"]
LOD847 = x3d.LOD()
LOD847.forceTransitions = True
LOD847.range = [0.04]
WorldInfo848 = x3d.WorldInfo()
WorldInfo848.info = ["hide diamond when close"]

LOD847.children.append(WorldInfo848)
Shape849 = x3d.Shape()
Shape849.USE = "HAnimSiteViewpointShape"

LOD847.children.append(Shape849)

Anchor846.children.append(LOD847)

HAnimSite844.children.append(Anchor846)

HAnimSegment836.children.append(HAnimSite844)

HAnimJoint835.children.append(HAnimSegment836)

HAnimJoint703.children.append(HAnimJoint835)
HAnimJoint850 = x3d.HAnimJoint()
HAnimJoint850.name = "r_eyelid_joint"
HAnimJoint850.DEF = "hanim_r_eyelid_joint"
HAnimJoint850.center = [-0.0336,1.6332,0.0502]
HAnimJoint850.ulimit = [0,0,0]
HAnimJoint850.llimit = [0,0,0]
HAnimSegment851 = x3d.HAnimSegment()
HAnimSegment851.name = "r_eyelid"
HAnimSegment851.DEF = "hanim_r_eyelid"
#<HAnimJoint name='r_eyelid_joint'/> visualization sphere within <HAnimSegment name='r_eyelid'/>
TouchSensor852 = x3d.TouchSensor()
TouchSensor852.description = "HAnimJoint r_eyelid_joint, HAnimSegment r_eyelid"

HAnimSegment851.children.append(TouchSensor852)
Transform853 = x3d.Transform()
Transform853.translation = [-0.0336,1.6332,0.0502]
Shape854 = x3d.Shape()
Shape854.USE = "HAnimJointShape"

Transform853.children.append(Shape854)

HAnimSegment851.children.append(Transform853)

HAnimJoint850.children.append(HAnimSegment851)

HAnimJoint703.children.append(HAnimJoint850)
HAnimJoint855 = x3d.HAnimJoint()
HAnimJoint855.name = "r_eyebrow_joint"
HAnimJoint855.DEF = "hanim_r_eyebrow_joint"
HAnimJoint855.center = [-0.0336,1.635,0.0506]
HAnimJoint855.ulimit = [0,0,0]
HAnimJoint855.llimit = [0,0,0]
HAnimSegment856 = x3d.HAnimSegment()
HAnimSegment856.name = "r_eyebrow"
HAnimSegment856.DEF = "hanim_r_eyebrow"
#<HAnimJoint name='r_eyebrow_joint'/> visualization sphere within <HAnimSegment name='r_eyebrow'/>
TouchSensor857 = x3d.TouchSensor()
TouchSensor857.description = "HAnimJoint r_eyebrow_joint, HAnimSegment r_eyebrow"

HAnimSegment856.children.append(TouchSensor857)
Transform858 = x3d.Transform()
Transform858.translation = [-0.0336,1.635,0.0506]
Shape859 = x3d.Shape()
Shape859.USE = "HAnimJointShape"

Transform858.children.append(Shape859)

HAnimSegment856.children.append(Transform858)

HAnimJoint855.children.append(HAnimSegment856)

HAnimJoint703.children.append(HAnimJoint855)
#Single joint, single segment for jaw, two sites for left/right TMJs https://en.wikipedia.org/wiki/Temporomandibular_joint
HAnimJoint860 = x3d.HAnimJoint()
HAnimJoint860.name = "temporomandibular"
HAnimJoint860.DEF = "hanim_temporomandibular"
HAnimJoint860.center = [0,1.63,0.015]
HAnimJoint860.ulimit = [0,0,0]
HAnimJoint860.llimit = [0,0,0]
HAnimSegment861 = x3d.HAnimSegment()
HAnimSegment861.name = "jaw"
HAnimSegment861.DEF = "hanim_jaw"
#<HAnimJoint name='temporomandibular'/> visualization sphere within <HAnimSegment name='jaw'/>
TouchSensor862 = x3d.TouchSensor()
TouchSensor862.description = "HAnimJoint temporomandibular, HAnimSegment jaw"

HAnimSegment861.children.append(TouchSensor862)
Transform863 = x3d.Transform()
Transform863.translation = [0,1.63,0.015]
Shape864 = x3d.Shape()
Shape864.USE = "HAnimJointShape"

Transform863.children.append(Shape864)

HAnimSegment861.children.append(Transform863)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='temporomandibular'/> to <HAnimSite name='temporomandibular_l_site'/>
Shape865 = x3d.Shape()
LineSet866 = x3d.LineSet()
LineSet866.vertexCount = [2]
Coordinate867 = x3d.Coordinate()
Coordinate867.point = (0.0000,1.6300,0.0150,0.0450,1.6300,0.0000)

LineSet866.coord = Coordinate867
ColorRGBA868 = x3d.ColorRGBA()
ColorRGBA868.USE = "HAnimSiteLineColorRGBA"

LineSet866.color = ColorRGBA868

Shape865.geometry = LineSet866

HAnimSegment861.children.append(Shape865)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='temporomandibular'/> to <HAnimSite name='temporomandibular_r_site'/>
Shape869 = x3d.Shape()
LineSet870 = x3d.LineSet()
LineSet870.vertexCount = [2]
Coordinate871 = x3d.Coordinate()
Coordinate871.point = (0.0000,1.6300,0.0150,-0.0450,1.6300,0.0000)

LineSet870.coord = Coordinate871
ColorRGBA872 = x3d.ColorRGBA()
ColorRGBA872.USE = "HAnimSiteLineColorRGBA"

LineSet870.color = ColorRGBA872

Shape869.geometry = LineSet870

HAnimSegment861.children.append(Shape869)
HAnimSite873 = x3d.HAnimSite()
HAnimSite873.name = "temporomandibular_l_site_pt"
HAnimSite873.DEF = "hanim_temporomandibular_l_site_pt"
HAnimSite873.translation = [0.045,1.63,0]
#HAnimSite visualization shape
TouchSensor874 = x3d.TouchSensor()
TouchSensor874.description = "HAnimSite temporomandibular_l_site"

HAnimSite873.children.append(TouchSensor874)
Shape875 = x3d.Shape()
Shape875.USE = "HAnimSiteShape"

HAnimSite873.children.append(Shape875)

HAnimSegment861.children.append(HAnimSite873)
HAnimSite876 = x3d.HAnimSite()
HAnimSite876.name = "temporomandibular_r_site_pt"
HAnimSite876.DEF = "hanim_temporomandibular_r_site_pt"
HAnimSite876.translation = [-0.045,1.63,0]
#HAnimSite visualization shape
TouchSensor877 = x3d.TouchSensor()
TouchSensor877.description = "HAnimSite temporomandibular_r_site"

HAnimSite876.children.append(TouchSensor877)
Shape878 = x3d.Shape()
Shape878.USE = "HAnimSiteShape"

HAnimSite876.children.append(Shape878)

HAnimSegment861.children.append(HAnimSite876)

HAnimJoint860.children.append(HAnimSegment861)

HAnimJoint703.children.append(HAnimJoint860)

HAnimJoint694.children.append(HAnimJoint703)

HAnimJoint685.children.append(HAnimJoint694)

HAnimJoint676.children.append(HAnimJoint685)

HAnimJoint667.children.append(HAnimJoint676)

HAnimJoint658.children.append(HAnimJoint667)

HAnimJoint649.children.append(HAnimJoint658)

HAnimJoint626.children.append(HAnimJoint649)

HAnimJoint595.children.append(HAnimJoint626)
HAnimJoint879 = x3d.HAnimJoint()
HAnimJoint879.name = "l_sternoclavicular"
HAnimJoint879.DEF = "hanim_l_sternoclavicular"
HAnimJoint879.center = [0.082,1.4488,-0.0353]
HAnimJoint879.ulimit = [0,0,0]
HAnimJoint879.llimit = [0,0,0]
HAnimSegment880 = x3d.HAnimSegment()
HAnimSegment880.name = "l_clavicle"
HAnimSegment880.DEF = "hanim_l_clavicle"
#<HAnimJoint name='l_sternoclavicular'/> visualization sphere within <HAnimSegment name='l_clavicle'/>
TouchSensor881 = x3d.TouchSensor()
TouchSensor881.description = "HAnimJoint l_sternoclavicular, HAnimSegment l_clavicle"

HAnimSegment880.children.append(TouchSensor881)
Transform882 = x3d.Transform()
Transform882.translation = [0.082,1.4488,-0.0353]
Shape883 = x3d.Shape()
Shape883.USE = "HAnimJointShape"

Transform882.children.append(Shape883)

HAnimSegment880.children.append(Transform882)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_sternoclavicular'/> to <HAnimJoint name='l_acromioclavicular'/>
Shape884 = x3d.Shape()
LineSet885 = x3d.LineSet()
LineSet885.vertexCount = [2]
Coordinate886 = x3d.Coordinate()
Coordinate886.point = (0.0820,1.4488,-0.0353,0.0962,1.4269,-0.0424)

LineSet885.coord = Coordinate886
ColorRGBA887 = x3d.ColorRGBA()
ColorRGBA887.USE = "HAnimSegmentLineColorRGBA"

LineSet885.color = ColorRGBA887

Shape884.geometry = LineSet885

HAnimSegment880.children.append(Shape884)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_sternoclavicular'/> to <HAnimSite name='l_clavicale'/>
Shape888 = x3d.Shape()
LineSet889 = x3d.LineSet()
LineSet889.vertexCount = [2]
Coordinate890 = x3d.Coordinate()
Coordinate890.point = (0.0820,1.4488,-0.0353,0.0271,1.4943,0.0394)

LineSet889.coord = Coordinate890
ColorRGBA891 = x3d.ColorRGBA()
ColorRGBA891.USE = "HAnimSiteLineColorRGBA"

LineSet889.color = ColorRGBA891

Shape888.geometry = LineSet889

HAnimSegment880.children.append(Shape888)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_sternoclavicular'/> to <HAnimSite name='l_acromion'/>
Shape892 = x3d.Shape()
LineSet893 = x3d.LineSet()
LineSet893.vertexCount = [2]
Coordinate894 = x3d.Coordinate()
Coordinate894.point = (0.0820,1.4488,-0.0353,0.2032,1.4760,-0.0490)

LineSet893.coord = Coordinate894
ColorRGBA895 = x3d.ColorRGBA()
ColorRGBA895.USE = "HAnimSiteLineColorRGBA"

LineSet893.color = ColorRGBA895

Shape892.geometry = LineSet893

HAnimSegment880.children.append(Shape892)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_sternoclavicular'/> to <HAnimSite name='l_axilla_ant'/>
Shape896 = x3d.Shape()
LineSet897 = x3d.LineSet()
LineSet897.vertexCount = [2]
Coordinate898 = x3d.Coordinate()
Coordinate898.point = (0.0820,1.4488,-0.0353,0.1777,1.4065,-0.0075)

LineSet897.coord = Coordinate898
ColorRGBA899 = x3d.ColorRGBA()
ColorRGBA899.USE = "HAnimSiteLineColorRGBA"

LineSet897.color = ColorRGBA899

Shape896.geometry = LineSet897

HAnimSegment880.children.append(Shape896)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_sternoclavicular'/> to <HAnimSite name='l_axilla_post'/>
Shape900 = x3d.Shape()
LineSet901 = x3d.LineSet()
LineSet901.vertexCount = [2]
Coordinate902 = x3d.Coordinate()
Coordinate902.point = (0.0820,1.4488,-0.0353,0.1706,1.4072,-0.0875)

LineSet901.coord = Coordinate902
ColorRGBA903 = x3d.ColorRGBA()
ColorRGBA903.USE = "HAnimSiteLineColorRGBA"

LineSet901.color = ColorRGBA903

Shape900.geometry = LineSet901

HAnimSegment880.children.append(Shape900)
HAnimSite904 = x3d.HAnimSite()
HAnimSite904.name = "l_clavicale_pt"
HAnimSite904.DEF = "hanim_l_clavicale_pt"
HAnimSite904.translation = [0.0271,1.4943,0.0394]
#HAnimSite visualization shape
TouchSensor905 = x3d.TouchSensor()
TouchSensor905.description = "HAnimSite l_clavicale"

HAnimSite904.children.append(TouchSensor905)
Shape906 = x3d.Shape()
Shape906.USE = "HAnimSiteShape"

HAnimSite904.children.append(Shape906)

HAnimSegment880.children.append(HAnimSite904)
HAnimSite907 = x3d.HAnimSite()
HAnimSite907.name = "l_acromion_pt"
HAnimSite907.DEF = "hanim_l_acromion_pt"
HAnimSite907.translation = [0.2032,1.476,-0.049]
#HAnimSite visualization shape
TouchSensor908 = x3d.TouchSensor()
TouchSensor908.description = "HAnimSite l_acromion"

HAnimSite907.children.append(TouchSensor908)
Shape909 = x3d.Shape()
Shape909.USE = "HAnimSiteShape"

HAnimSite907.children.append(Shape909)

HAnimSegment880.children.append(HAnimSite907)
HAnimSite910 = x3d.HAnimSite()
HAnimSite910.name = "l_axilla_ant_pt"
HAnimSite910.DEF = "hanim_l_axilla_ant_pt"
HAnimSite910.translation = [0.1777,1.4065,-0.0075]
#HAnimSite visualization shape
TouchSensor911 = x3d.TouchSensor()
TouchSensor911.description = "HAnimSite l_axilla_ant"

HAnimSite910.children.append(TouchSensor911)
Shape912 = x3d.Shape()
Shape912.USE = "HAnimSiteShape"

HAnimSite910.children.append(Shape912)

HAnimSegment880.children.append(HAnimSite910)
HAnimSite913 = x3d.HAnimSite()
HAnimSite913.name = "l_axilla_post_pt"
HAnimSite913.DEF = "hanim_l_axilla_post_pt"
HAnimSite913.translation = [0.1706,1.4072,-0.0875]
#HAnimSite visualization shape
TouchSensor914 = x3d.TouchSensor()
TouchSensor914.description = "HAnimSite l_axilla_post"

HAnimSite913.children.append(TouchSensor914)
Shape915 = x3d.Shape()
Shape915.USE = "HAnimSiteShape"

HAnimSite913.children.append(Shape915)

HAnimSegment880.children.append(HAnimSite913)

HAnimJoint879.children.append(HAnimSegment880)
HAnimJoint916 = x3d.HAnimJoint()
HAnimJoint916.name = "l_acromioclavicular"
HAnimJoint916.DEF = "hanim_l_acromioclavicular"
HAnimJoint916.center = [0.0962,1.4269,-0.0424]
HAnimJoint916.ulimit = [0,0,0]
HAnimJoint916.llimit = [0,0,0]
HAnimSegment917 = x3d.HAnimSegment()
HAnimSegment917.name = "l_scapula"
HAnimSegment917.DEF = "hanim_l_scapula"
#<HAnimJoint name='l_acromioclavicular'/> visualization sphere within <HAnimSegment name='l_scapula'/>
TouchSensor918 = x3d.TouchSensor()
TouchSensor918.description = "HAnimJoint l_acromioclavicular, HAnimSegment l_scapula"

HAnimSegment917.children.append(TouchSensor918)
Transform919 = x3d.Transform()
Transform919.translation = [0.0962,1.4269,-0.0424]
Shape920 = x3d.Shape()
Shape920.USE = "HAnimJointShape"

Transform919.children.append(Shape920)

HAnimSegment917.children.append(Transform919)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_acromioclavicular'/> to <HAnimJoint name='l_shoulder'/>
Shape921 = x3d.Shape()
LineSet922 = x3d.LineSet()
LineSet922.vertexCount = [2]
Coordinate923 = x3d.Coordinate()
Coordinate923.point = (0.0962,1.4269,-0.0424,0.2029,1.4376,-0.0387)

LineSet922.coord = Coordinate923
ColorRGBA924 = x3d.ColorRGBA()
ColorRGBA924.USE = "HAnimSegmentLineColorRGBA"

LineSet922.color = ColorRGBA924

Shape921.geometry = LineSet922

HAnimSegment917.children.append(Shape921)

HAnimJoint916.children.append(HAnimSegment917)
HAnimJoint925 = x3d.HAnimJoint()
HAnimJoint925.name = "l_shoulder"
HAnimJoint925.DEF = "hanim_l_shoulder"
HAnimJoint925.center = [0.2029,1.4376,-0.0387]
HAnimJoint925.ulimit = [0,0,0]
HAnimJoint925.llimit = [0,0,0]
HAnimSegment926 = x3d.HAnimSegment()
HAnimSegment926.name = "l_upperarm"
HAnimSegment926.DEF = "hanim_l_upperarm"
#<HAnimJoint name='l_shoulder'/> visualization sphere within <HAnimSegment name='l_upperarm'/>
TouchSensor927 = x3d.TouchSensor()
TouchSensor927.description = "HAnimJoint l_shoulder, HAnimSegment l_upperarm"

HAnimSegment926.children.append(TouchSensor927)
Transform928 = x3d.Transform()
Transform928.translation = [0.2029,1.4376,-0.0387]
Shape929 = x3d.Shape()
Shape929.USE = "HAnimJointShape"

Transform928.children.append(Shape929)

HAnimSegment926.children.append(Transform928)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_shoulder'/> to <HAnimJoint name='l_elbow'/>
Shape930 = x3d.Shape()
LineSet931 = x3d.LineSet()
LineSet931.vertexCount = [2]
Coordinate932 = x3d.Coordinate()
Coordinate932.point = (0.2029,1.4376,-0.0387,0.2014,1.1357,-0.0682)

LineSet931.coord = Coordinate932
ColorRGBA933 = x3d.ColorRGBA()
ColorRGBA933.USE = "HAnimSegmentLineColorRGBA"

LineSet931.color = ColorRGBA933

Shape930.geometry = LineSet931

HAnimSegment926.children.append(Shape930)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_shoulder'/> to <HAnimSite name='l_humeral_lateral_epicn'/>
Shape934 = x3d.Shape()
LineSet935 = x3d.LineSet()
LineSet935.vertexCount = [2]
Coordinate936 = x3d.Coordinate()
Coordinate936.point = (0.2029,1.4376,-0.0387,0.2280,1.1482,-0.1100)

LineSet935.coord = Coordinate936
ColorRGBA937 = x3d.ColorRGBA()
ColorRGBA937.USE = "HAnimSiteLineColorRGBA"

LineSet935.color = ColorRGBA937

Shape934.geometry = LineSet935

HAnimSegment926.children.append(Shape934)
HAnimSite938 = x3d.HAnimSite()
HAnimSite938.name = "l_humeral_lateral_epicn_pt"
HAnimSite938.DEF = "hanim_l_humeral_lateral_epicn_pt"
HAnimSite938.translation = [0.228,1.1482,-0.11]
#HAnimSite visualization shape
TouchSensor939 = x3d.TouchSensor()
TouchSensor939.description = "HAnimSite l_humeral_lateral_epicn"

HAnimSite938.children.append(TouchSensor939)
Shape940 = x3d.Shape()
Shape940.USE = "HAnimSiteShape"

HAnimSite938.children.append(Shape940)

HAnimSegment926.children.append(HAnimSite938)

HAnimJoint925.children.append(HAnimSegment926)
HAnimJoint941 = x3d.HAnimJoint()
HAnimJoint941.name = "l_elbow"
HAnimJoint941.DEF = "hanim_l_elbow"
HAnimJoint941.center = [0.2014,1.1357,-0.0682]
HAnimJoint941.ulimit = [0,0,0]
HAnimJoint941.llimit = [0,0,0]
HAnimSegment942 = x3d.HAnimSegment()
HAnimSegment942.name = "l_forearm"
HAnimSegment942.DEF = "hanim_l_forearm"
#<HAnimJoint name='l_elbow'/> visualization sphere within <HAnimSegment name='l_forearm'/>
TouchSensor943 = x3d.TouchSensor()
TouchSensor943.description = "HAnimJoint l_elbow, HAnimSegment l_forearm"

HAnimSegment942.children.append(TouchSensor943)
Transform944 = x3d.Transform()
Transform944.translation = [0.2014,1.1357,-0.0682]
Shape945 = x3d.Shape()
Shape945.USE = "HAnimJointShape"

Transform944.children.append(Shape945)

HAnimSegment942.children.append(Transform944)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_elbow'/> to <HAnimJoint name='l_wrist'/>
Shape946 = x3d.Shape()
LineSet947 = x3d.LineSet()
LineSet947.vertexCount = [2]
Coordinate948 = x3d.Coordinate()
Coordinate948.point = (0.2014,1.1357,-0.0682,0.1984,0.8663,-0.0583)

LineSet947.coord = Coordinate948
ColorRGBA949 = x3d.ColorRGBA()
ColorRGBA949.USE = "HAnimSegmentLineColorRGBA"

LineSet947.color = ColorRGBA949

Shape946.geometry = LineSet947

HAnimSegment942.children.append(Shape946)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_elbow'/> to <HAnimSite name='l_radial_styloid'/>
Shape950 = x3d.Shape()
LineSet951 = x3d.LineSet()
LineSet951.vertexCount = [2]
Coordinate952 = x3d.Coordinate()
Coordinate952.point = (0.2014,1.1357,-0.0682,0.1901,0.8645,-0.0415)

LineSet951.coord = Coordinate952
ColorRGBA953 = x3d.ColorRGBA()
ColorRGBA953.USE = "HAnimSiteLineColorRGBA"

LineSet951.color = ColorRGBA953

Shape950.geometry = LineSet951

HAnimSegment942.children.append(Shape950)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_elbow'/> to <HAnimSite name='l_olecranon'/>
Shape954 = x3d.Shape()
LineSet955 = x3d.LineSet()
LineSet955.vertexCount = [2]
Coordinate956 = x3d.Coordinate()
Coordinate956.point = (0.2014,1.1357,-0.0682,0.1962,1.1375,-0.1123)

LineSet955.coord = Coordinate956
ColorRGBA957 = x3d.ColorRGBA()
ColorRGBA957.USE = "HAnimSiteLineColorRGBA"

LineSet955.color = ColorRGBA957

Shape954.geometry = LineSet955

HAnimSegment942.children.append(Shape954)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_elbow'/> to <HAnimSite name='l_humeral_medial_epicn'/>
Shape958 = x3d.Shape()
LineSet959 = x3d.LineSet()
LineSet959.vertexCount = [2]
Coordinate960 = x3d.Coordinate()
Coordinate960.point = (0.2014,1.1357,-0.0682,0.1735,1.1272,-0.1113)

LineSet959.coord = Coordinate960
ColorRGBA961 = x3d.ColorRGBA()
ColorRGBA961.USE = "HAnimSiteLineColorRGBA"

LineSet959.color = ColorRGBA961

Shape958.geometry = LineSet959

HAnimSegment942.children.append(Shape958)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_elbow'/> to <HAnimSite name='l_radiale'/>
Shape962 = x3d.Shape()
LineSet963 = x3d.LineSet()
LineSet963.vertexCount = [2]
Coordinate964 = x3d.Coordinate()
Coordinate964.point = (0.2014,1.1357,-0.0682,0.2182,1.1212,-0.1167)

LineSet963.coord = Coordinate964
ColorRGBA965 = x3d.ColorRGBA()
ColorRGBA965.USE = "HAnimSiteLineColorRGBA"

LineSet963.color = ColorRGBA965

Shape962.geometry = LineSet963

HAnimSegment942.children.append(Shape962)
HAnimSite966 = x3d.HAnimSite()
HAnimSite966.name = "l_radial_styloid_pt"
HAnimSite966.DEF = "hanim_l_radial_styloid_pt"
HAnimSite966.translation = [0.1901,0.8645,-0.0415]
#HAnimSite visualization shape
TouchSensor967 = x3d.TouchSensor()
TouchSensor967.description = "HAnimSite l_radial_styloid"

HAnimSite966.children.append(TouchSensor967)
Shape968 = x3d.Shape()
Shape968.USE = "HAnimSiteShape"

HAnimSite966.children.append(Shape968)

HAnimSegment942.children.append(HAnimSite966)
HAnimSite969 = x3d.HAnimSite()
HAnimSite969.name = "l_olecranon_pt"
HAnimSite969.DEF = "hanim_l_olecranon_pt"
HAnimSite969.translation = [0.1962,1.1375,-0.1123]
#HAnimSite visualization shape
TouchSensor970 = x3d.TouchSensor()
TouchSensor970.description = "HAnimSite l_olecranon"

HAnimSite969.children.append(TouchSensor970)
Shape971 = x3d.Shape()
Shape971.USE = "HAnimSiteShape"

HAnimSite969.children.append(Shape971)

HAnimSegment942.children.append(HAnimSite969)
HAnimSite972 = x3d.HAnimSite()
HAnimSite972.name = "l_humeral_medial_epicn_pt"
HAnimSite972.DEF = "hanim_l_humeral_medial_epicn_pt"
HAnimSite972.translation = [0.1735,1.1272,-0.1113]
#HAnimSite visualization shape
TouchSensor973 = x3d.TouchSensor()
TouchSensor973.description = "HAnimSite l_humeral_medial_epicn"

HAnimSite972.children.append(TouchSensor973)
Shape974 = x3d.Shape()
Shape974.USE = "HAnimSiteShape"

HAnimSite972.children.append(Shape974)

HAnimSegment942.children.append(HAnimSite972)
HAnimSite975 = x3d.HAnimSite()
HAnimSite975.name = "l_radiale_pt"
HAnimSite975.DEF = "hanim_l_radiale_pt"
HAnimSite975.translation = [0.2182,1.1212,-0.1167]
#HAnimSite visualization shape
TouchSensor976 = x3d.TouchSensor()
TouchSensor976.description = "HAnimSite l_radiale"

HAnimSite975.children.append(TouchSensor976)
Shape977 = x3d.Shape()
Shape977.USE = "HAnimSiteShape"

HAnimSite975.children.append(Shape977)

HAnimSegment942.children.append(HAnimSite975)

HAnimJoint941.children.append(HAnimSegment942)
HAnimJoint978 = x3d.HAnimJoint()
HAnimJoint978.name = "l_wrist"
HAnimJoint978.DEF = "hanim_l_wrist"
HAnimJoint978.center = [0.1984,0.8663,-0.0583]
HAnimJoint978.ulimit = [0,0,0]
HAnimJoint978.llimit = [0,0,0]
HAnimSegment979 = x3d.HAnimSegment()
HAnimSegment979.name = "l_hand"
HAnimSegment979.DEF = "hanim_l_hand"
#<HAnimJoint name='l_wrist'/> visualization sphere within <HAnimSegment name='l_hand'/>
TouchSensor980 = x3d.TouchSensor()
TouchSensor980.description = "HAnimJoint l_wrist, HAnimSegment l_hand"

HAnimSegment979.children.append(TouchSensor980)
Transform981 = x3d.Transform()
Transform981.translation = [0.1984,0.8663,-0.0583]
Shape982 = x3d.Shape()
Shape982.USE = "HAnimJointShape"

Transform981.children.append(Shape982)

HAnimSegment979.children.append(Transform981)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_wrist'/> to <HAnimJoint name='l_thumb1'/>
Shape983 = x3d.Shape()
LineSet984 = x3d.LineSet()
LineSet984.vertexCount = [2]
Coordinate985 = x3d.Coordinate()
Coordinate985.point = (0.1984,0.8663,-0.0583,0.1924,0.8472,-0.0534)

LineSet984.coord = Coordinate985
ColorRGBA986 = x3d.ColorRGBA()
ColorRGBA986.USE = "HAnimSegmentLineColorRGBA"

LineSet984.color = ColorRGBA986

Shape983.geometry = LineSet984

HAnimSegment979.children.append(Shape983)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_wrist'/> to <HAnimJoint name='l_index0'/>
Shape987 = x3d.Shape()
LineSet988 = x3d.LineSet()
LineSet988.vertexCount = [2]
Coordinate989 = x3d.Coordinate()
Coordinate989.point = (0.1984,0.8663,-0.0583,0.1983,0.8024,-0.0280)

LineSet988.coord = Coordinate989
ColorRGBA990 = x3d.ColorRGBA()
ColorRGBA990.USE = "HAnimSegmentLineColorRGBA"

LineSet988.color = ColorRGBA990

Shape987.geometry = LineSet988

HAnimSegment979.children.append(Shape987)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_wrist'/> to <HAnimJoint name='l_middle0'/>
Shape991 = x3d.Shape()
LineSet992 = x3d.LineSet()
LineSet992.vertexCount = [2]
Coordinate993 = x3d.Coordinate()
Coordinate993.point = (0.1984,0.8663,-0.0583,0.1987,0.8029,-0.0530)

LineSet992.coord = Coordinate993
ColorRGBA994 = x3d.ColorRGBA()
ColorRGBA994.USE = "HAnimSegmentLineColorRGBA"

LineSet992.color = ColorRGBA994

Shape991.geometry = LineSet992

HAnimSegment979.children.append(Shape991)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_wrist'/> to <HAnimJoint name='l_ring0'/>
Shape995 = x3d.Shape()
LineSet996 = x3d.LineSet()
LineSet996.vertexCount = [2]
Coordinate997 = x3d.Coordinate()
Coordinate997.point = (0.1984,0.8663,-0.0583,0.1956,0.8019,-0.0794)

LineSet996.coord = Coordinate997
ColorRGBA998 = x3d.ColorRGBA()
ColorRGBA998.USE = "HAnimSegmentLineColorRGBA"

LineSet996.color = ColorRGBA998

Shape995.geometry = LineSet996

HAnimSegment979.children.append(Shape995)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_wrist'/> to <HAnimJoint name='l_pinky0'/>
Shape999 = x3d.Shape()
LineSet1000 = x3d.LineSet()
LineSet1000.vertexCount = [2]
Coordinate1001 = x3d.Coordinate()
Coordinate1001.point = (0.1984,0.8663,-0.0583,0.1925,0.8066,-0.1036)

LineSet1000.coord = Coordinate1001
ColorRGBA1002 = x3d.ColorRGBA()
ColorRGBA1002.USE = "HAnimSegmentLineColorRGBA"

LineSet1000.color = ColorRGBA1002

Shape999.geometry = LineSet1000

HAnimSegment979.children.append(Shape999)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_wrist'/> to <HAnimSite name='l_metacarpal_pha2'/>
Shape1003 = x3d.Shape()
LineSet1004 = x3d.LineSet()
LineSet1004.vertexCount = [2]
Coordinate1005 = x3d.Coordinate()
Coordinate1005.point = (0.1984,0.8663,-0.0583,0.2009,0.8139,-0.0237)

LineSet1004.coord = Coordinate1005
ColorRGBA1006 = x3d.ColorRGBA()
ColorRGBA1006.USE = "HAnimSiteLineColorRGBA"

LineSet1004.color = ColorRGBA1006

Shape1003.geometry = LineSet1004

HAnimSegment979.children.append(Shape1003)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_wrist'/> to <HAnimSite name='l_ulnar_styloid'/>
Shape1007 = x3d.Shape()
LineSet1008 = x3d.LineSet()
LineSet1008.vertexCount = [2]
Coordinate1009 = x3d.Coordinate()
Coordinate1009.point = (0.1984,0.8663,-0.0583,0.2142,0.8529,-0.0648)

LineSet1008.coord = Coordinate1009
ColorRGBA1010 = x3d.ColorRGBA()
ColorRGBA1010.USE = "HAnimSiteLineColorRGBA"

LineSet1008.color = ColorRGBA1010

Shape1007.geometry = LineSet1008

HAnimSegment979.children.append(Shape1007)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_wrist'/> to <HAnimSite name='l_metacarpal_pha5'/>
Shape1011 = x3d.Shape()
LineSet1012 = x3d.LineSet()
LineSet1012.vertexCount = [2]
Coordinate1013 = x3d.Coordinate()
Coordinate1013.point = (0.1984,0.8663,-0.0583,0.1929,0.7860,-0.1122)

LineSet1012.coord = Coordinate1013
ColorRGBA1014 = x3d.ColorRGBA()
ColorRGBA1014.USE = "HAnimSiteLineColorRGBA"

LineSet1012.color = ColorRGBA1014

Shape1011.geometry = LineSet1012

HAnimSegment979.children.append(Shape1011)
#HAnimSite/Viewpoint visualization line segment from ancestor <HAnimJoint name='l_wrist'/> to <HAnimSite name='l_hand_front_view'/>
Shape1015 = x3d.Shape()
LineSet1016 = x3d.LineSet()
LineSet1016.vertexCount = [2]
Coordinate1017 = x3d.Coordinate()
Coordinate1017.point = (0.1984,0.8663,-0.0583,0.3000,0.7500,0.4500)

LineSet1016.coord = Coordinate1017
ColorRGBA1018 = x3d.ColorRGBA()
ColorRGBA1018.USE = "HAnimSiteViewpointLineColorRGBA"

LineSet1016.color = ColorRGBA1018

Shape1015.geometry = LineSet1016

HAnimSegment979.children.append(Shape1015)
HAnimSite1019 = x3d.HAnimSite()
HAnimSite1019.name = "l_metacarpal_pha2_pt"
HAnimSite1019.DEF = "hanim_l_metacarpal_pha2_pt"
HAnimSite1019.translation = [0.2009,0.8139,-0.0237]
#HAnimSite visualization shape
TouchSensor1020 = x3d.TouchSensor()
TouchSensor1020.description = "HAnimSite l_metacarpal_pha2"

HAnimSite1019.children.append(TouchSensor1020)
Shape1021 = x3d.Shape()
Shape1021.USE = "HAnimSiteShape"

HAnimSite1019.children.append(Shape1021)

HAnimSegment979.children.append(HAnimSite1019)
HAnimSite1022 = x3d.HAnimSite()
HAnimSite1022.name = "l_ulnar_styloid_pt"
HAnimSite1022.DEF = "hanim_l_ulnar_styloid_pt"
HAnimSite1022.translation = [0.2142,0.8529,-0.0648]
#HAnimSite visualization shape
TouchSensor1023 = x3d.TouchSensor()
TouchSensor1023.description = "HAnimSite l_ulnar_styloid"

HAnimSite1022.children.append(TouchSensor1023)
Shape1024 = x3d.Shape()
Shape1024.USE = "HAnimSiteShape"

HAnimSite1022.children.append(Shape1024)

HAnimSegment979.children.append(HAnimSite1022)
HAnimSite1025 = x3d.HAnimSite()
HAnimSite1025.name = "l_metacarpal_pha5_pt"
HAnimSite1025.DEF = "hanim_l_metacarpal_pha5_pt"
HAnimSite1025.translation = [0.1929,0.786,-0.1122]
#HAnimSite visualization shape
TouchSensor1026 = x3d.TouchSensor()
TouchSensor1026.description = "HAnimSite l_metacarpal_pha5"

HAnimSite1025.children.append(TouchSensor1026)
Shape1027 = x3d.Shape()
Shape1027.USE = "HAnimSiteShape"

HAnimSite1025.children.append(Shape1027)

HAnimSegment979.children.append(HAnimSite1025)
HAnimSite1028 = x3d.HAnimSite()
HAnimSite1028.name = "l_hand_front_view"
HAnimSite1028.DEF = "hanim_l_hand_front_view"
HAnimSite1028.translation = [0.3,0.75,0.45]
Viewpoint1029 = x3d.Viewpoint()
Viewpoint1029.DEF = "hanim_l_hand_front_viewpoint"
Viewpoint1029.centerOfRotation = [0,0.7,0]
Viewpoint1029.description = "left hand front"
Viewpoint1029.position = [0,0,0]

HAnimSite1028.children.append(Viewpoint1029)
#HAnimSite/Viewpoint visualization shape
Anchor1030 = x3d.Anchor()
Anchor1030.description = "HAnimSite Viewpoint hanim_l_hand_front_view"
Anchor1030.url = ["#hanim_l_hand_front_viewpoint"]
LOD1031 = x3d.LOD()
LOD1031.forceTransitions = True
LOD1031.range = [0.04]
WorldInfo1032 = x3d.WorldInfo()
WorldInfo1032.info = ["hide diamond when close"]

LOD1031.children.append(WorldInfo1032)
Shape1033 = x3d.Shape()
Shape1033.USE = "HAnimSiteViewpointShape"

LOD1031.children.append(Shape1033)

Anchor1030.children.append(LOD1031)

HAnimSite1028.children.append(Anchor1030)

HAnimSegment979.children.append(HAnimSite1028)

HAnimJoint978.children.append(HAnimSegment979)
HAnimJoint1034 = x3d.HAnimJoint()
HAnimJoint1034.name = "l_thumb1"
HAnimJoint1034.DEF = "hanim_l_thumb1"
HAnimJoint1034.center = [0.1924,0.8472,-0.0534]
HAnimJoint1034.ulimit = [0,0,0]
HAnimJoint1034.llimit = [0,0,0]
HAnimSegment1035 = x3d.HAnimSegment()
HAnimSegment1035.name = "l_thumb_metacarpal"
HAnimSegment1035.DEF = "hanim_l_thumb_metacarpal"
#<HAnimJoint name='l_thumb1'/> visualization sphere within <HAnimSegment name='l_thumb_metacarpal'/>
TouchSensor1036 = x3d.TouchSensor()
TouchSensor1036.description = "HAnimJoint l_thumb1, HAnimSegment l_thumb_metacarpal"

HAnimSegment1035.children.append(TouchSensor1036)
Transform1037 = x3d.Transform()
Transform1037.translation = [0.1924,0.8472,-0.0534]
Shape1038 = x3d.Shape()
Shape1038.USE = "HAnimJointShape"

Transform1037.children.append(Shape1038)

HAnimSegment1035.children.append(Transform1037)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_thumb1'/> to <HAnimJoint name='l_thumb2'/>
Shape1039 = x3d.Shape()
LineSet1040 = x3d.LineSet()
LineSet1040.vertexCount = [2]
Coordinate1041 = x3d.Coordinate()
Coordinate1041.point = (0.1924,0.8472,-0.0534,0.1951,0.8226,0.0246)

LineSet1040.coord = Coordinate1041
ColorRGBA1042 = x3d.ColorRGBA()
ColorRGBA1042.USE = "HAnimSegmentLineColorRGBA"

LineSet1040.color = ColorRGBA1042

Shape1039.geometry = LineSet1040

HAnimSegment1035.children.append(Shape1039)

HAnimJoint1034.children.append(HAnimSegment1035)
HAnimJoint1043 = x3d.HAnimJoint()
HAnimJoint1043.name = "l_thumb2"
HAnimJoint1043.DEF = "hanim_l_thumb2"
HAnimJoint1043.center = [0.1951,0.8226,0.0246]
HAnimJoint1043.ulimit = [0,0,0]
HAnimJoint1043.llimit = [0,0,0]
HAnimSegment1044 = x3d.HAnimSegment()
HAnimSegment1044.name = "l_thumb_proximal"
HAnimSegment1044.DEF = "hanim_l_thumb_proximal"
#<HAnimJoint name='l_thumb2'/> visualization sphere within <HAnimSegment name='l_thumb_proximal'/>
TouchSensor1045 = x3d.TouchSensor()
TouchSensor1045.description = "HAnimJoint l_thumb2, HAnimSegment l_thumb_proximal"

HAnimSegment1044.children.append(TouchSensor1045)
Transform1046 = x3d.Transform()
Transform1046.translation = [0.1951,0.8226,0.0246]
Shape1047 = x3d.Shape()
Shape1047.USE = "HAnimJointShape"

Transform1046.children.append(Shape1047)

HAnimSegment1044.children.append(Transform1046)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_thumb2'/> to <HAnimJoint name='l_thumb3'/>
Shape1048 = x3d.Shape()
LineSet1049 = x3d.LineSet()
LineSet1049.vertexCount = [2]
Coordinate1050 = x3d.Coordinate()
Coordinate1050.point = (0.1951,0.8226,0.0246,0.1955,0.8159,0.0464)

LineSet1049.coord = Coordinate1050
ColorRGBA1051 = x3d.ColorRGBA()
ColorRGBA1051.USE = "HAnimSegmentLineColorRGBA"

LineSet1049.color = ColorRGBA1051

Shape1048.geometry = LineSet1049

HAnimSegment1044.children.append(Shape1048)

HAnimJoint1043.children.append(HAnimSegment1044)
HAnimJoint1052 = x3d.HAnimJoint()
HAnimJoint1052.name = "l_thumb3"
HAnimJoint1052.DEF = "hanim_l_thumb3"
HAnimJoint1052.center = [0.1955,0.8159,0.0464]
HAnimJoint1052.ulimit = [0,0,0]
HAnimJoint1052.llimit = [0,0,0]
HAnimSegment1053 = x3d.HAnimSegment()
HAnimSegment1053.name = "l_thumb_distal"
HAnimSegment1053.DEF = "hanim_l_thumb_distal"
#<HAnimJoint name='l_thumb3'/> visualization sphere within <HAnimSegment name='l_thumb_distal'/>
TouchSensor1054 = x3d.TouchSensor()
TouchSensor1054.description = "HAnimJoint l_thumb3, HAnimSegment l_thumb_distal"

HAnimSegment1053.children.append(TouchSensor1054)
Transform1055 = x3d.Transform()
Transform1055.translation = [0.1955,0.8159,0.0464]
Shape1056 = x3d.Shape()
Shape1056.USE = "HAnimJointShape"

Transform1055.children.append(Shape1056)

HAnimSegment1053.children.append(Transform1055)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_thumb3'/> to <HAnimSite name='l_thumb_distal_tip'/>
Shape1057 = x3d.Shape()
LineSet1058 = x3d.LineSet()
LineSet1058.vertexCount = [2]
Coordinate1059 = x3d.Coordinate()
Coordinate1059.point = (0.1955,0.8159,0.0464,0.1982,0.8061,0.0759)

LineSet1058.coord = Coordinate1059
ColorRGBA1060 = x3d.ColorRGBA()
ColorRGBA1060.USE = "HAnimSiteLineColorRGBA"

LineSet1058.color = ColorRGBA1060

Shape1057.geometry = LineSet1058

HAnimSegment1053.children.append(Shape1057)
HAnimSite1061 = x3d.HAnimSite()
HAnimSite1061.name = "l_thumb_distal_tip"
HAnimSite1061.DEF = "hanim_l_thumb_distal_tip"
HAnimSite1061.translation = [0.1982,0.8061,0.0759]
#HAnimSite visualization shape
TouchSensor1062 = x3d.TouchSensor()
TouchSensor1062.description = "HAnimSite l_thumb_distal_tip"

HAnimSite1061.children.append(TouchSensor1062)
Shape1063 = x3d.Shape()
Shape1063.USE = "HAnimSiteShape"

HAnimSite1061.children.append(Shape1063)

HAnimSegment1053.children.append(HAnimSite1061)

HAnimJoint1052.children.append(HAnimSegment1053)

HAnimJoint1043.children.append(HAnimJoint1052)

HAnimJoint1034.children.append(HAnimJoint1043)

HAnimJoint978.children.append(HAnimJoint1034)
HAnimJoint1064 = x3d.HAnimJoint()
HAnimJoint1064.name = "l_index0"
HAnimJoint1064.DEF = "hanim_l_index0"
HAnimJoint1064.center = [0.1983,0.8024,-0.028]
HAnimJoint1064.ulimit = [0,0,0]
HAnimJoint1064.llimit = [0,0,0]
HAnimSegment1065 = x3d.HAnimSegment()
HAnimSegment1065.name = "l_index_metacarpal"
HAnimSegment1065.DEF = "hanim_l_index_metacarpal"
#<HAnimJoint name='l_index0'/> visualization sphere within <HAnimSegment name='l_index_metacarpal'/>
TouchSensor1066 = x3d.TouchSensor()
TouchSensor1066.description = "HAnimJoint l_index0, HAnimSegment l_index_metacarpal"

HAnimSegment1065.children.append(TouchSensor1066)
Transform1067 = x3d.Transform()
Transform1067.translation = [0.1983,0.8024,-0.028]
Shape1068 = x3d.Shape()
Shape1068.USE = "HAnimJointShape"

Transform1067.children.append(Shape1068)

HAnimSegment1065.children.append(Transform1067)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_index0'/> to <HAnimJoint name='l_index1'/>
Shape1069 = x3d.Shape()
LineSet1070 = x3d.LineSet()
LineSet1070.vertexCount = [2]
Coordinate1071 = x3d.Coordinate()
Coordinate1071.point = (0.1983,0.8024,-0.0280,0.1983,0.7815,-0.0280)

LineSet1070.coord = Coordinate1071
ColorRGBA1072 = x3d.ColorRGBA()
ColorRGBA1072.USE = "HAnimSegmentLineColorRGBA"

LineSet1070.color = ColorRGBA1072

Shape1069.geometry = LineSet1070

HAnimSegment1065.children.append(Shape1069)

HAnimJoint1064.children.append(HAnimSegment1065)
HAnimJoint1073 = x3d.HAnimJoint()
HAnimJoint1073.name = "l_index1"
HAnimJoint1073.DEF = "hanim_l_index1"
HAnimJoint1073.center = [0.1983,0.7815,-0.028]
HAnimJoint1073.ulimit = [0,0,0]
HAnimJoint1073.llimit = [0,0,0]
HAnimSegment1074 = x3d.HAnimSegment()
HAnimSegment1074.name = "l_index_proximal"
HAnimSegment1074.DEF = "hanim_l_index_proximal"
#<HAnimJoint name='l_index1'/> visualization sphere within <HAnimSegment name='l_index_proximal'/>
TouchSensor1075 = x3d.TouchSensor()
TouchSensor1075.description = "HAnimJoint l_index1, HAnimSegment l_index_proximal"

HAnimSegment1074.children.append(TouchSensor1075)
Transform1076 = x3d.Transform()
Transform1076.translation = [0.1983,0.7815,-0.028]
Shape1077 = x3d.Shape()
Shape1077.USE = "HAnimJointShape"

Transform1076.children.append(Shape1077)

HAnimSegment1074.children.append(Transform1076)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_index1'/> to <HAnimJoint name='l_index2'/>
Shape1078 = x3d.Shape()
LineSet1079 = x3d.LineSet()
LineSet1079.vertexCount = [2]
Coordinate1080 = x3d.Coordinate()
Coordinate1080.point = (0.1983,0.7815,-0.0280,0.2017,0.7363,-0.0248)

LineSet1079.coord = Coordinate1080
ColorRGBA1081 = x3d.ColorRGBA()
ColorRGBA1081.USE = "HAnimSegmentLineColorRGBA"

LineSet1079.color = ColorRGBA1081

Shape1078.geometry = LineSet1079

HAnimSegment1074.children.append(Shape1078)

HAnimJoint1073.children.append(HAnimSegment1074)
HAnimJoint1082 = x3d.HAnimJoint()
HAnimJoint1082.name = "l_index2"
HAnimJoint1082.DEF = "hanim_l_index2"
HAnimJoint1082.center = [0.2017,0.7363,-0.0248]
HAnimJoint1082.ulimit = [0,0,0]
HAnimJoint1082.llimit = [0,0,0]
HAnimSegment1083 = x3d.HAnimSegment()
HAnimSegment1083.name = "l_index_middle"
HAnimSegment1083.DEF = "hanim_l_index_middle"
#<HAnimJoint name='l_index2'/> visualization sphere within <HAnimSegment name='l_index_middle'/>
TouchSensor1084 = x3d.TouchSensor()
TouchSensor1084.description = "HAnimJoint l_index2, HAnimSegment l_index_middle"

HAnimSegment1083.children.append(TouchSensor1084)
Transform1085 = x3d.Transform()
Transform1085.translation = [0.2017,0.7363,-0.0248]
Shape1086 = x3d.Shape()
Shape1086.USE = "HAnimJointShape"

Transform1085.children.append(Shape1086)

HAnimSegment1083.children.append(Transform1085)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_index2'/> to <HAnimJoint name='l_index3'/>
Shape1087 = x3d.Shape()
LineSet1088 = x3d.LineSet()
LineSet1088.vertexCount = [2]
Coordinate1089 = x3d.Coordinate()
Coordinate1089.point = (0.2017,0.7363,-0.0248,0.2028,0.7139,-0.0236)

LineSet1088.coord = Coordinate1089
ColorRGBA1090 = x3d.ColorRGBA()
ColorRGBA1090.USE = "HAnimSegmentLineColorRGBA"

LineSet1088.color = ColorRGBA1090

Shape1087.geometry = LineSet1088

HAnimSegment1083.children.append(Shape1087)

HAnimJoint1082.children.append(HAnimSegment1083)
HAnimJoint1091 = x3d.HAnimJoint()
HAnimJoint1091.name = "l_index3"
HAnimJoint1091.DEF = "hanim_l_index3"
HAnimJoint1091.center = [0.2028,0.7139,-0.0236]
HAnimJoint1091.ulimit = [0,0,0]
HAnimJoint1091.llimit = [0,0,0]
HAnimSegment1092 = x3d.HAnimSegment()
HAnimSegment1092.name = "l_index_distal"
HAnimSegment1092.DEF = "hanim_l_index_distal"
#<HAnimJoint name='l_index3'/> visualization sphere within <HAnimSegment name='l_index_distal'/>
TouchSensor1093 = x3d.TouchSensor()
TouchSensor1093.description = "HAnimJoint l_index3, HAnimSegment l_index_distal"

HAnimSegment1092.children.append(TouchSensor1093)
Transform1094 = x3d.Transform()
Transform1094.translation = [0.2028,0.7139,-0.0236]
Shape1095 = x3d.Shape()
Shape1095.USE = "HAnimJointShape"

Transform1094.children.append(Shape1095)

HAnimSegment1092.children.append(Transform1094)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_index3'/> to <HAnimSite name='l_index_distal_tip'/>
Shape1096 = x3d.Shape()
LineSet1097 = x3d.LineSet()
LineSet1097.vertexCount = [2]
Coordinate1098 = x3d.Coordinate()
Coordinate1098.point = (0.2028,0.7139,-0.0236,0.2089,0.6858,-0.0245)

LineSet1097.coord = Coordinate1098
ColorRGBA1099 = x3d.ColorRGBA()
ColorRGBA1099.USE = "HAnimSiteLineColorRGBA"

LineSet1097.color = ColorRGBA1099

Shape1096.geometry = LineSet1097

HAnimSegment1092.children.append(Shape1096)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_index3'/> to <HAnimSite name='l_dactylion'/>
Shape1100 = x3d.Shape()
LineSet1101 = x3d.LineSet()
LineSet1101.vertexCount = [2]
Coordinate1102 = x3d.Coordinate()
Coordinate1102.point = (0.2028,0.7139,-0.0236,0.2056,0.6743,-0.0482)

LineSet1101.coord = Coordinate1102
ColorRGBA1103 = x3d.ColorRGBA()
ColorRGBA1103.USE = "HAnimSiteLineColorRGBA"

LineSet1101.color = ColorRGBA1103

Shape1100.geometry = LineSet1101

HAnimSegment1092.children.append(Shape1100)
HAnimSite1104 = x3d.HAnimSite()
HAnimSite1104.name = "l_index_distal_tip"
HAnimSite1104.DEF = "hanim_l_index_distal_tip"
HAnimSite1104.translation = [0.2089,0.6858,-0.0245]
#HAnimSite visualization shape
TouchSensor1105 = x3d.TouchSensor()
TouchSensor1105.description = "HAnimSite l_index_distal_tip"

HAnimSite1104.children.append(TouchSensor1105)
Shape1106 = x3d.Shape()
Shape1106.USE = "HAnimSiteShape"

HAnimSite1104.children.append(Shape1106)

HAnimSegment1092.children.append(HAnimSite1104)
HAnimSite1107 = x3d.HAnimSite()
HAnimSite1107.name = "l_dactylion_pt"
HAnimSite1107.DEF = "hanim_l_dactylion_pt"
HAnimSite1107.translation = [0.2056,0.6743,-0.0482]
#HAnimSite visualization shape
TouchSensor1108 = x3d.TouchSensor()
TouchSensor1108.description = "HAnimSite l_dactylion"

HAnimSite1107.children.append(TouchSensor1108)
Shape1109 = x3d.Shape()
Shape1109.USE = "HAnimSiteShape"

HAnimSite1107.children.append(Shape1109)

HAnimSegment1092.children.append(HAnimSite1107)

HAnimJoint1091.children.append(HAnimSegment1092)

HAnimJoint1082.children.append(HAnimJoint1091)

HAnimJoint1073.children.append(HAnimJoint1082)

HAnimJoint1064.children.append(HAnimJoint1073)

HAnimJoint978.children.append(HAnimJoint1064)
HAnimJoint1110 = x3d.HAnimJoint()
HAnimJoint1110.name = "l_middle0"
HAnimJoint1110.DEF = "hanim_l_middle0"
HAnimJoint1110.center = [0.1987,0.8029,-0.053]
HAnimJoint1110.ulimit = [0,0,0]
HAnimJoint1110.llimit = [0,0,0]
HAnimSegment1111 = x3d.HAnimSegment()
HAnimSegment1111.name = "l_middle_metacarpal"
HAnimSegment1111.DEF = "hanim_l_middle_metacarpal"
#<HAnimJoint name='l_middle0'/> visualization sphere within <HAnimSegment name='l_middle_metacarpal'/>
TouchSensor1112 = x3d.TouchSensor()
TouchSensor1112.description = "HAnimJoint l_middle0, HAnimSegment l_middle_metacarpal"

HAnimSegment1111.children.append(TouchSensor1112)
Transform1113 = x3d.Transform()
Transform1113.translation = [0.1987,0.8029,-0.053]
Shape1114 = x3d.Shape()
Shape1114.USE = "HAnimJointShape"

Transform1113.children.append(Shape1114)

HAnimSegment1111.children.append(Transform1113)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_middle0'/> to <HAnimJoint name='l_middle1'/>
Shape1115 = x3d.Shape()
LineSet1116 = x3d.LineSet()
LineSet1116.vertexCount = [2]
Coordinate1117 = x3d.Coordinate()
Coordinate1117.point = (0.1987,0.8029,-0.0530,0.1987,0.7818,-0.0530)

LineSet1116.coord = Coordinate1117
ColorRGBA1118 = x3d.ColorRGBA()
ColorRGBA1118.USE = "HAnimSegmentLineColorRGBA"

LineSet1116.color = ColorRGBA1118

Shape1115.geometry = LineSet1116

HAnimSegment1111.children.append(Shape1115)

HAnimJoint1110.children.append(HAnimSegment1111)
HAnimJoint1119 = x3d.HAnimJoint()
HAnimJoint1119.name = "l_middle1"
HAnimJoint1119.DEF = "hanim_l_middle1"
HAnimJoint1119.center = [0.1987,0.7818,-0.053]
HAnimJoint1119.ulimit = [0,0,0]
HAnimJoint1119.llimit = [0,0,0]
HAnimSegment1120 = x3d.HAnimSegment()
HAnimSegment1120.name = "l_middle_proximal"
HAnimSegment1120.DEF = "hanim_l_middle_proximal"
#<HAnimJoint name='l_middle1'/> visualization sphere within <HAnimSegment name='l_middle_proximal'/>
TouchSensor1121 = x3d.TouchSensor()
TouchSensor1121.description = "HAnimJoint l_middle1, HAnimSegment l_middle_proximal"

HAnimSegment1120.children.append(TouchSensor1121)
Transform1122 = x3d.Transform()
Transform1122.translation = [0.1987,0.7818,-0.053]
Shape1123 = x3d.Shape()
Shape1123.USE = "HAnimJointShape"

Transform1122.children.append(Shape1123)

HAnimSegment1120.children.append(Transform1122)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_middle1'/> to <HAnimJoint name='l_middle2'/>
Shape1124 = x3d.Shape()
LineSet1125 = x3d.LineSet()
LineSet1125.vertexCount = [2]
Coordinate1126 = x3d.Coordinate()
Coordinate1126.point = (0.1987,0.7818,-0.0530,0.2013,0.7273,-0.0503)

LineSet1125.coord = Coordinate1126
ColorRGBA1127 = x3d.ColorRGBA()
ColorRGBA1127.USE = "HAnimSegmentLineColorRGBA"

LineSet1125.color = ColorRGBA1127

Shape1124.geometry = LineSet1125

HAnimSegment1120.children.append(Shape1124)

HAnimJoint1119.children.append(HAnimSegment1120)
HAnimJoint1128 = x3d.HAnimJoint()
HAnimJoint1128.name = "l_middle2"
HAnimJoint1128.DEF = "hanim_l_middle2"
HAnimJoint1128.center = [0.2013,0.7273,-0.0503]
HAnimJoint1128.ulimit = [0,0,0]
HAnimJoint1128.llimit = [0,0,0]
HAnimSegment1129 = x3d.HAnimSegment()
HAnimSegment1129.name = "l_middle_middle"
HAnimSegment1129.DEF = "hanim_l_middle_middle"
#<HAnimJoint name='l_middle2'/> visualization sphere within <HAnimSegment name='l_middle_middle'/>
TouchSensor1130 = x3d.TouchSensor()
TouchSensor1130.description = "HAnimJoint l_middle2, HAnimSegment l_middle_middle"

HAnimSegment1129.children.append(TouchSensor1130)
Transform1131 = x3d.Transform()
Transform1131.translation = [0.2013,0.7273,-0.0503]
Shape1132 = x3d.Shape()
Shape1132.USE = "HAnimJointShape"

Transform1131.children.append(Shape1132)

HAnimSegment1129.children.append(Transform1131)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_middle2'/> to <HAnimJoint name='l_middle3'/>
Shape1133 = x3d.Shape()
LineSet1134 = x3d.LineSet()
LineSet1134.vertexCount = [2]
Coordinate1135 = x3d.Coordinate()
Coordinate1135.point = (0.2013,0.7273,-0.0503,0.2026,0.7011,-0.0494)

LineSet1134.coord = Coordinate1135
ColorRGBA1136 = x3d.ColorRGBA()
ColorRGBA1136.USE = "HAnimSegmentLineColorRGBA"

LineSet1134.color = ColorRGBA1136

Shape1133.geometry = LineSet1134

HAnimSegment1129.children.append(Shape1133)

HAnimJoint1128.children.append(HAnimSegment1129)
HAnimJoint1137 = x3d.HAnimJoint()
HAnimJoint1137.name = "l_middle3"
HAnimJoint1137.DEF = "hanim_l_middle3"
HAnimJoint1137.center = [0.2026,0.7011,-0.0494]
HAnimJoint1137.ulimit = [0,0,0]
HAnimJoint1137.llimit = [0,0,0]
HAnimSegment1138 = x3d.HAnimSegment()
HAnimSegment1138.name = "l_middle_distal"
HAnimSegment1138.DEF = "hanim_l_middle_distal"
#<HAnimJoint name='l_middle3'/> visualization sphere within <HAnimSegment name='l_middle_distal'/>
TouchSensor1139 = x3d.TouchSensor()
TouchSensor1139.description = "HAnimJoint l_middle3, HAnimSegment l_middle_distal"

HAnimSegment1138.children.append(TouchSensor1139)
Transform1140 = x3d.Transform()
Transform1140.translation = [0.2026,0.7011,-0.0494]
Shape1141 = x3d.Shape()
Shape1141.USE = "HAnimJointShape"

Transform1140.children.append(Shape1141)

HAnimSegment1138.children.append(Transform1140)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_middle3'/> to <HAnimSite name='l_middle_distal_tip'/>
Shape1142 = x3d.Shape()
LineSet1143 = x3d.LineSet()
LineSet1143.vertexCount = [2]
Coordinate1144 = x3d.Coordinate()
Coordinate1144.point = (0.2026,0.7011,-0.0494,0.2080,0.6731,-0.0491)

LineSet1143.coord = Coordinate1144
ColorRGBA1145 = x3d.ColorRGBA()
ColorRGBA1145.USE = "HAnimSiteLineColorRGBA"

LineSet1143.color = ColorRGBA1145

Shape1142.geometry = LineSet1143

HAnimSegment1138.children.append(Shape1142)
HAnimSite1146 = x3d.HAnimSite()
HAnimSite1146.name = "l_middle_distal_tip"
HAnimSite1146.DEF = "hanim_l_middle_distal_tip"
HAnimSite1146.translation = [0.208,0.6731,-0.0491]
#HAnimSite visualization shape
TouchSensor1147 = x3d.TouchSensor()
TouchSensor1147.description = "HAnimSite l_middle_distal_tip"

HAnimSite1146.children.append(TouchSensor1147)
Shape1148 = x3d.Shape()
Shape1148.USE = "HAnimSiteShape"

HAnimSite1146.children.append(Shape1148)

HAnimSegment1138.children.append(HAnimSite1146)

HAnimJoint1137.children.append(HAnimSegment1138)

HAnimJoint1128.children.append(HAnimJoint1137)

HAnimJoint1119.children.append(HAnimJoint1128)

HAnimJoint1110.children.append(HAnimJoint1119)

HAnimJoint978.children.append(HAnimJoint1110)
HAnimJoint1149 = x3d.HAnimJoint()
HAnimJoint1149.name = "l_ring0"
HAnimJoint1149.DEF = "hanim_l_ring0"
HAnimJoint1149.center = [0.1956,0.8019,-0.0794]
HAnimJoint1149.ulimit = [0,0,0]
HAnimJoint1149.llimit = [0,0,0]
HAnimSegment1150 = x3d.HAnimSegment()
HAnimSegment1150.name = "l_ring_metacarpal"
HAnimSegment1150.DEF = "hanim_l_ring_metacarpal"
#<HAnimJoint name='l_ring0'/> visualization sphere within <HAnimSegment name='l_ring_metacarpal'/>
TouchSensor1151 = x3d.TouchSensor()
TouchSensor1151.description = "HAnimJoint l_ring0, HAnimSegment l_ring_metacarpal"

HAnimSegment1150.children.append(TouchSensor1151)
Transform1152 = x3d.Transform()
Transform1152.translation = [0.1956,0.8019,-0.0794]
Shape1153 = x3d.Shape()
Shape1153.USE = "HAnimJointShape"

Transform1152.children.append(Shape1153)

HAnimSegment1150.children.append(Transform1152)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_ring0'/> to <HAnimJoint name='l_ring1'/>
Shape1154 = x3d.Shape()
LineSet1155 = x3d.LineSet()
LineSet1155.vertexCount = [2]
Coordinate1156 = x3d.Coordinate()
Coordinate1156.point = (0.1956,0.8019,-0.0794,0.1956,0.7815,-0.0794)

LineSet1155.coord = Coordinate1156
ColorRGBA1157 = x3d.ColorRGBA()
ColorRGBA1157.USE = "HAnimSegmentLineColorRGBA"

LineSet1155.color = ColorRGBA1157

Shape1154.geometry = LineSet1155

HAnimSegment1150.children.append(Shape1154)

HAnimJoint1149.children.append(HAnimSegment1150)
HAnimJoint1158 = x3d.HAnimJoint()
HAnimJoint1158.name = "l_ring1"
HAnimJoint1158.DEF = "hanim_l_ring1"
HAnimJoint1158.center = [0.1956,0.7815,-0.0794]
HAnimJoint1158.ulimit = [0,0,0]
HAnimJoint1158.llimit = [0,0,0]
HAnimSegment1159 = x3d.HAnimSegment()
HAnimSegment1159.name = "l_ring_proximal"
HAnimSegment1159.DEF = "hanim_l_ring_proximal"
#<HAnimJoint name='l_ring1'/> visualization sphere within <HAnimSegment name='l_ring_proximal'/>
TouchSensor1160 = x3d.TouchSensor()
TouchSensor1160.description = "HAnimJoint l_ring1, HAnimSegment l_ring_proximal"

HAnimSegment1159.children.append(TouchSensor1160)
Transform1161 = x3d.Transform()
Transform1161.translation = [0.1956,0.7815,-0.0794]
Shape1162 = x3d.Shape()
Shape1162.USE = "HAnimJointShape"

Transform1161.children.append(Shape1162)

HAnimSegment1159.children.append(Transform1161)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_ring1'/> to <HAnimJoint name='l_ring2'/>
Shape1163 = x3d.Shape()
LineSet1164 = x3d.LineSet()
LineSet1164.vertexCount = [2]
Coordinate1165 = x3d.Coordinate()
Coordinate1165.point = (0.1956,0.7815,-0.0794,0.1973,0.7287,-0.0777)

LineSet1164.coord = Coordinate1165
ColorRGBA1166 = x3d.ColorRGBA()
ColorRGBA1166.USE = "HAnimSegmentLineColorRGBA"

LineSet1164.color = ColorRGBA1166

Shape1163.geometry = LineSet1164

HAnimSegment1159.children.append(Shape1163)

HAnimJoint1158.children.append(HAnimSegment1159)
HAnimJoint1167 = x3d.HAnimJoint()
HAnimJoint1167.name = "l_ring2"
HAnimJoint1167.DEF = "hanim_l_ring2"
HAnimJoint1167.center = [0.1973,0.7287,-0.0777]
HAnimJoint1167.ulimit = [0,0,0]
HAnimJoint1167.llimit = [0,0,0]
HAnimSegment1168 = x3d.HAnimSegment()
HAnimSegment1168.name = "l_ring_middle"
HAnimSegment1168.DEF = "hanim_l_ring_middle"
#<HAnimJoint name='l_ring2'/> visualization sphere within <HAnimSegment name='l_ring_middle'/>
TouchSensor1169 = x3d.TouchSensor()
TouchSensor1169.description = "HAnimJoint l_ring2, HAnimSegment l_ring_middle"

HAnimSegment1168.children.append(TouchSensor1169)
Transform1170 = x3d.Transform()
Transform1170.translation = [0.1973,0.7287,-0.0777]
Shape1171 = x3d.Shape()
Shape1171.USE = "HAnimJointShape"

Transform1170.children.append(Shape1171)

HAnimSegment1168.children.append(Transform1170)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_ring2'/> to <HAnimJoint name='l_ring3'/>
Shape1172 = x3d.Shape()
LineSet1173 = x3d.LineSet()
LineSet1173.vertexCount = [2]
Coordinate1174 = x3d.Coordinate()
Coordinate1174.point = (0.1973,0.7287,-0.0777,0.1983,0.7045,-0.0767)

LineSet1173.coord = Coordinate1174
ColorRGBA1175 = x3d.ColorRGBA()
ColorRGBA1175.USE = "HAnimSegmentLineColorRGBA"

LineSet1173.color = ColorRGBA1175

Shape1172.geometry = LineSet1173

HAnimSegment1168.children.append(Shape1172)

HAnimJoint1167.children.append(HAnimSegment1168)
HAnimJoint1176 = x3d.HAnimJoint()
HAnimJoint1176.name = "l_ring3"
HAnimJoint1176.DEF = "hanim_l_ring3"
HAnimJoint1176.center = [0.1983,0.7045,-0.0767]
HAnimJoint1176.ulimit = [0,0,0]
HAnimJoint1176.llimit = [0,0,0]
HAnimSegment1177 = x3d.HAnimSegment()
HAnimSegment1177.name = "l_ring_distal"
HAnimSegment1177.DEF = "hanim_l_ring_distal"
#<HAnimJoint name='l_ring3'/> visualization sphere within <HAnimSegment name='l_ring_distal'/>
TouchSensor1178 = x3d.TouchSensor()
TouchSensor1178.description = "HAnimJoint l_ring3, HAnimSegment l_ring_distal"

HAnimSegment1177.children.append(TouchSensor1178)
Transform1179 = x3d.Transform()
Transform1179.translation = [0.1983,0.7045,-0.0767]
Shape1180 = x3d.Shape()
Shape1180.USE = "HAnimJointShape"

Transform1179.children.append(Shape1180)

HAnimSegment1177.children.append(Transform1179)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_ring3'/> to <HAnimSite name='l_ring_distal_tip'/>
Shape1181 = x3d.Shape()
LineSet1182 = x3d.LineSet()
LineSet1182.vertexCount = [2]
Coordinate1183 = x3d.Coordinate()
Coordinate1183.point = (0.1983,0.7045,-0.0767,0.2035,0.6750,-0.0756)

LineSet1182.coord = Coordinate1183
ColorRGBA1184 = x3d.ColorRGBA()
ColorRGBA1184.USE = "HAnimSiteLineColorRGBA"

LineSet1182.color = ColorRGBA1184

Shape1181.geometry = LineSet1182

HAnimSegment1177.children.append(Shape1181)
HAnimSite1185 = x3d.HAnimSite()
HAnimSite1185.name = "l_ring_distal_tip"
HAnimSite1185.DEF = "hanim_l_ring_distal_tip"
HAnimSite1185.translation = [0.2035,0.675,-0.0756]
#HAnimSite visualization shape
TouchSensor1186 = x3d.TouchSensor()
TouchSensor1186.description = "HAnimSite l_ring_distal_tip"

HAnimSite1185.children.append(TouchSensor1186)
Shape1187 = x3d.Shape()
Shape1187.USE = "HAnimSiteShape"

HAnimSite1185.children.append(Shape1187)

HAnimSegment1177.children.append(HAnimSite1185)

HAnimJoint1176.children.append(HAnimSegment1177)

HAnimJoint1167.children.append(HAnimJoint1176)

HAnimJoint1158.children.append(HAnimJoint1167)

HAnimJoint1149.children.append(HAnimJoint1158)

HAnimJoint978.children.append(HAnimJoint1149)
HAnimJoint1188 = x3d.HAnimJoint()
HAnimJoint1188.name = "l_pinky0"
HAnimJoint1188.DEF = "hanim_l_pinky0"
HAnimJoint1188.center = [0.1925,0.8066,-0.1036]
HAnimJoint1188.ulimit = [0,0,0]
HAnimJoint1188.llimit = [0,0,0]
HAnimSegment1189 = x3d.HAnimSegment()
HAnimSegment1189.name = "l_pinky_metacarpal"
HAnimSegment1189.DEF = "hanim_l_pinky_metacarpal"
#<HAnimJoint name='l_pinky0'/> visualization sphere within <HAnimSegment name='l_pinky_metacarpal'/>
TouchSensor1190 = x3d.TouchSensor()
TouchSensor1190.description = "HAnimJoint l_pinky0, HAnimSegment l_pinky_metacarpal"

HAnimSegment1189.children.append(TouchSensor1190)
Transform1191 = x3d.Transform()
Transform1191.translation = [0.1925,0.8066,-0.1036]
Shape1192 = x3d.Shape()
Shape1192.USE = "HAnimJointShape"

Transform1191.children.append(Shape1192)

HAnimSegment1189.children.append(Transform1191)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_pinky0'/> to <HAnimJoint name='l_pinky1'/>
Shape1193 = x3d.Shape()
LineSet1194 = x3d.LineSet()
LineSet1194.vertexCount = [2]
Coordinate1195 = x3d.Coordinate()
Coordinate1195.point = (0.1925,0.8066,-0.1036,0.1925,0.7866,-0.1036)

LineSet1194.coord = Coordinate1195
ColorRGBA1196 = x3d.ColorRGBA()
ColorRGBA1196.USE = "HAnimSegmentLineColorRGBA"

LineSet1194.color = ColorRGBA1196

Shape1193.geometry = LineSet1194

HAnimSegment1189.children.append(Shape1193)

HAnimJoint1188.children.append(HAnimSegment1189)
HAnimJoint1197 = x3d.HAnimJoint()
HAnimJoint1197.name = "l_pinky1"
HAnimJoint1197.DEF = "hanim_l_pinky1"
HAnimJoint1197.center = [0.1925,0.7866,-0.1036]
HAnimJoint1197.ulimit = [0,0,0]
HAnimJoint1197.llimit = [0,0,0]
HAnimSegment1198 = x3d.HAnimSegment()
HAnimSegment1198.name = "l_pinky_proximal"
HAnimSegment1198.DEF = "hanim_l_pinky_proximal"
#<HAnimJoint name='l_pinky1'/> visualization sphere within <HAnimSegment name='l_pinky_proximal'/>
TouchSensor1199 = x3d.TouchSensor()
TouchSensor1199.description = "HAnimJoint l_pinky1, HAnimSegment l_pinky_proximal"

HAnimSegment1198.children.append(TouchSensor1199)
Transform1200 = x3d.Transform()
Transform1200.translation = [0.1925,0.7866,-0.1036]
Shape1201 = x3d.Shape()
Shape1201.USE = "HAnimJointShape"

Transform1200.children.append(Shape1201)

HAnimSegment1198.children.append(Transform1200)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_pinky1'/> to <HAnimJoint name='l_pinky2'/>
Shape1202 = x3d.Shape()
LineSet1203 = x3d.LineSet()
LineSet1203.vertexCount = [2]
Coordinate1204 = x3d.Coordinate()
Coordinate1204.point = (0.1925,0.7866,-0.1036,0.1938,0.7452,-0.1024)

LineSet1203.coord = Coordinate1204
ColorRGBA1205 = x3d.ColorRGBA()
ColorRGBA1205.USE = "HAnimSegmentLineColorRGBA"

LineSet1203.color = ColorRGBA1205

Shape1202.geometry = LineSet1203

HAnimSegment1198.children.append(Shape1202)

HAnimJoint1197.children.append(HAnimSegment1198)
HAnimJoint1206 = x3d.HAnimJoint()
HAnimJoint1206.name = "l_pinky2"
HAnimJoint1206.DEF = "hanim_l_pinky2"
HAnimJoint1206.center = [0.1938,0.7452,-0.1024]
HAnimJoint1206.ulimit = [0,0,0]
HAnimJoint1206.llimit = [0,0,0]
HAnimSegment1207 = x3d.HAnimSegment()
HAnimSegment1207.name = "l_pinky_middle"
HAnimSegment1207.DEF = "hanim_l_pinky_middle"
#<HAnimJoint name='l_pinky2'/> visualization sphere within <HAnimSegment name='l_pinky_middle'/>
TouchSensor1208 = x3d.TouchSensor()
TouchSensor1208.description = "HAnimJoint l_pinky2, HAnimSegment l_pinky_middle"

HAnimSegment1207.children.append(TouchSensor1208)
Transform1209 = x3d.Transform()
Transform1209.translation = [0.1938,0.7452,-0.1024]
Shape1210 = x3d.Shape()
Shape1210.USE = "HAnimJointShape"

Transform1209.children.append(Shape1210)

HAnimSegment1207.children.append(Transform1209)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_pinky2'/> to <HAnimJoint name='l_pinky3'/>
Shape1211 = x3d.Shape()
LineSet1212 = x3d.LineSet()
LineSet1212.vertexCount = [2]
Coordinate1213 = x3d.Coordinate()
Coordinate1213.point = (0.1938,0.7452,-0.1024,0.1948,0.7277,-0.1017)

LineSet1212.coord = Coordinate1213
ColorRGBA1214 = x3d.ColorRGBA()
ColorRGBA1214.USE = "HAnimSegmentLineColorRGBA"

LineSet1212.color = ColorRGBA1214

Shape1211.geometry = LineSet1212

HAnimSegment1207.children.append(Shape1211)

HAnimJoint1206.children.append(HAnimSegment1207)
HAnimJoint1215 = x3d.HAnimJoint()
HAnimJoint1215.name = "l_pinky3"
HAnimJoint1215.DEF = "hanim_l_pinky3"
HAnimJoint1215.center = [0.1948,0.7277,-0.1017]
HAnimJoint1215.ulimit = [0,0,0]
HAnimJoint1215.llimit = [0,0,0]
HAnimSegment1216 = x3d.HAnimSegment()
HAnimSegment1216.name = "l_pinky_distal"
HAnimSegment1216.DEF = "hanim_l_pinky_distal"
#<HAnimJoint name='l_pinky3'/> visualization sphere within <HAnimSegment name='l_pinky_distal'/>
TouchSensor1217 = x3d.TouchSensor()
TouchSensor1217.description = "HAnimJoint l_pinky3, HAnimSegment l_pinky_distal"

HAnimSegment1216.children.append(TouchSensor1217)
Transform1218 = x3d.Transform()
Transform1218.translation = [0.1948,0.7277,-0.1017]
Shape1219 = x3d.Shape()
Shape1219.USE = "HAnimJointShape"

Transform1218.children.append(Shape1219)

HAnimSegment1216.children.append(Transform1218)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_pinky3'/> to <HAnimSite name='l_pinky_distal_tip'/>
Shape1220 = x3d.Shape()
LineSet1221 = x3d.LineSet()
LineSet1221.vertexCount = [2]
Coordinate1222 = x3d.Coordinate()
Coordinate1222.point = (0.1948,0.7277,-0.1017,0.2014,0.7009,-0.1012)

LineSet1221.coord = Coordinate1222
ColorRGBA1223 = x3d.ColorRGBA()
ColorRGBA1223.USE = "HAnimSiteLineColorRGBA"

LineSet1221.color = ColorRGBA1223

Shape1220.geometry = LineSet1221

HAnimSegment1216.children.append(Shape1220)
HAnimSite1224 = x3d.HAnimSite()
HAnimSite1224.name = "l_pinky_distal_tip"
HAnimSite1224.DEF = "hanim_l_pinky_distal_tip"
HAnimSite1224.translation = [0.2014,0.7009,-0.1012]
#HAnimSite visualization shape
TouchSensor1225 = x3d.TouchSensor()
TouchSensor1225.description = "HAnimSite l_pinky_distal_tip"

HAnimSite1224.children.append(TouchSensor1225)
Shape1226 = x3d.Shape()
Shape1226.USE = "HAnimSiteShape"

HAnimSite1224.children.append(Shape1226)

HAnimSegment1216.children.append(HAnimSite1224)

HAnimJoint1215.children.append(HAnimSegment1216)

HAnimJoint1206.children.append(HAnimJoint1215)

HAnimJoint1197.children.append(HAnimJoint1206)

HAnimJoint1188.children.append(HAnimJoint1197)

HAnimJoint978.children.append(HAnimJoint1188)

HAnimJoint941.children.append(HAnimJoint978)

HAnimJoint925.children.append(HAnimJoint941)

HAnimJoint916.children.append(HAnimJoint925)

HAnimJoint879.children.append(HAnimJoint916)

HAnimJoint595.children.append(HAnimJoint879)
HAnimJoint1227 = x3d.HAnimJoint()
HAnimJoint1227.name = "r_sternoclavicular"
HAnimJoint1227.DEF = "hanim_r_sternoclavicular"
HAnimJoint1227.center = [-0.082,1.4488,-0.0353]
HAnimJoint1227.ulimit = [0,0,0]
HAnimJoint1227.llimit = [0,0,0]
HAnimSegment1228 = x3d.HAnimSegment()
HAnimSegment1228.name = "r_clavicle"
HAnimSegment1228.DEF = "hanim_r_clavicle"
#<HAnimJoint name='r_sternoclavicular'/> visualization sphere within <HAnimSegment name='r_clavicle'/>
TouchSensor1229 = x3d.TouchSensor()
TouchSensor1229.description = "HAnimJoint r_sternoclavicular, HAnimSegment r_clavicle"

HAnimSegment1228.children.append(TouchSensor1229)
Transform1230 = x3d.Transform()
Transform1230.translation = [-0.082,1.4488,-0.0353]
Shape1231 = x3d.Shape()
Shape1231.USE = "HAnimJointShape"

Transform1230.children.append(Shape1231)

HAnimSegment1228.children.append(Transform1230)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_sternoclavicular'/> to <HAnimJoint name='r_acromioclavicular'/>
Shape1232 = x3d.Shape()
LineSet1233 = x3d.LineSet()
LineSet1233.vertexCount = [2]
Coordinate1234 = x3d.Coordinate()
Coordinate1234.point = (-0.0820,1.4488,-0.0353,-0.0962,1.4269,-0.0424)

LineSet1233.coord = Coordinate1234
ColorRGBA1235 = x3d.ColorRGBA()
ColorRGBA1235.USE = "HAnimSegmentLineColorRGBA"

LineSet1233.color = ColorRGBA1235

Shape1232.geometry = LineSet1233

HAnimSegment1228.children.append(Shape1232)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_sternoclavicular'/> to <HAnimSite name='r_clavicale'/>
Shape1236 = x3d.Shape()
LineSet1237 = x3d.LineSet()
LineSet1237.vertexCount = [2]
Coordinate1238 = x3d.Coordinate()
Coordinate1238.point = (-0.0820,1.4488,-0.0353,-0.0115,1.4943,0.0400)

LineSet1237.coord = Coordinate1238
ColorRGBA1239 = x3d.ColorRGBA()
ColorRGBA1239.USE = "HAnimSiteLineColorRGBA"

LineSet1237.color = ColorRGBA1239

Shape1236.geometry = LineSet1237

HAnimSegment1228.children.append(Shape1236)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_sternoclavicular'/> to <HAnimSite name='r_acromion'/>
Shape1240 = x3d.Shape()
LineSet1241 = x3d.LineSet()
LineSet1241.vertexCount = [2]
Coordinate1242 = x3d.Coordinate()
Coordinate1242.point = (-0.0820,1.4488,-0.0353,-0.1905,1.4791,-0.0431)

LineSet1241.coord = Coordinate1242
ColorRGBA1243 = x3d.ColorRGBA()
ColorRGBA1243.USE = "HAnimSiteLineColorRGBA"

LineSet1241.color = ColorRGBA1243

Shape1240.geometry = LineSet1241

HAnimSegment1228.children.append(Shape1240)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_sternoclavicular'/> to <HAnimSite name='r_axilla_ant'/>
Shape1244 = x3d.Shape()
LineSet1245 = x3d.LineSet()
LineSet1245.vertexCount = [2]
Coordinate1246 = x3d.Coordinate()
Coordinate1246.point = (-0.0820,1.4488,-0.0353,-0.1626,1.4072,-0.0031)

LineSet1245.coord = Coordinate1246
ColorRGBA1247 = x3d.ColorRGBA()
ColorRGBA1247.USE = "HAnimSiteLineColorRGBA"

LineSet1245.color = ColorRGBA1247

Shape1244.geometry = LineSet1245

HAnimSegment1228.children.append(Shape1244)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_sternoclavicular'/> to <HAnimSite name='r_axilla_post'/>
Shape1248 = x3d.Shape()
LineSet1249 = x3d.LineSet()
LineSet1249.vertexCount = [2]
Coordinate1250 = x3d.Coordinate()
Coordinate1250.point = (-0.0820,1.4488,-0.0353,-0.1603,1.4098,-0.0826)

LineSet1249.coord = Coordinate1250
ColorRGBA1251 = x3d.ColorRGBA()
ColorRGBA1251.USE = "HAnimSiteLineColorRGBA"

LineSet1249.color = ColorRGBA1251

Shape1248.geometry = LineSet1249

HAnimSegment1228.children.append(Shape1248)
HAnimSite1252 = x3d.HAnimSite()
HAnimSite1252.name = "r_clavicale_pt"
HAnimSite1252.DEF = "hanim_r_clavicale_pt"
HAnimSite1252.translation = [-0.0115,1.4943,0.04]
#HAnimSite visualization shape
TouchSensor1253 = x3d.TouchSensor()
TouchSensor1253.description = "HAnimSite r_clavicale"

HAnimSite1252.children.append(TouchSensor1253)
Shape1254 = x3d.Shape()
Shape1254.USE = "HAnimSiteShape"

HAnimSite1252.children.append(Shape1254)

HAnimSegment1228.children.append(HAnimSite1252)
HAnimSite1255 = x3d.HAnimSite()
HAnimSite1255.name = "r_acromion_pt"
HAnimSite1255.DEF = "hanim_r_acromion_pt"
HAnimSite1255.translation = [-0.1905,1.4791,-0.0431]
#HAnimSite visualization shape
TouchSensor1256 = x3d.TouchSensor()
TouchSensor1256.description = "HAnimSite r_acromion"

HAnimSite1255.children.append(TouchSensor1256)
Shape1257 = x3d.Shape()
Shape1257.USE = "HAnimSiteShape"

HAnimSite1255.children.append(Shape1257)

HAnimSegment1228.children.append(HAnimSite1255)
HAnimSite1258 = x3d.HAnimSite()
HAnimSite1258.name = "r_axilla_ant_pt"
HAnimSite1258.DEF = "hanim_r_axilla_ant_pt"
HAnimSite1258.translation = [-0.1626,1.4072,-0.0031]
#HAnimSite visualization shape
TouchSensor1259 = x3d.TouchSensor()
TouchSensor1259.description = "HAnimSite r_axilla_ant"

HAnimSite1258.children.append(TouchSensor1259)
Shape1260 = x3d.Shape()
Shape1260.USE = "HAnimSiteShape"

HAnimSite1258.children.append(Shape1260)

HAnimSegment1228.children.append(HAnimSite1258)
HAnimSite1261 = x3d.HAnimSite()
HAnimSite1261.name = "r_axilla_post_pt"
HAnimSite1261.DEF = "hanim_r_axilla_post_pt"
HAnimSite1261.translation = [-0.1603,1.4098,-0.0826]
#HAnimSite visualization shape
TouchSensor1262 = x3d.TouchSensor()
TouchSensor1262.description = "HAnimSite r_axilla_post"

HAnimSite1261.children.append(TouchSensor1262)
Shape1263 = x3d.Shape()
Shape1263.USE = "HAnimSiteShape"

HAnimSite1261.children.append(Shape1263)

HAnimSegment1228.children.append(HAnimSite1261)

HAnimJoint1227.children.append(HAnimSegment1228)
HAnimJoint1264 = x3d.HAnimJoint()
HAnimJoint1264.name = "r_acromioclavicular"
HAnimJoint1264.DEF = "hanim_r_acromioclavicular"
HAnimJoint1264.center = [-0.0962,1.4269,-0.0424]
HAnimJoint1264.ulimit = [0,0,0]
HAnimJoint1264.llimit = [0,0,0]
HAnimSegment1265 = x3d.HAnimSegment()
HAnimSegment1265.name = "r_scapula"
HAnimSegment1265.DEF = "hanim_r_scapula"
#<HAnimJoint name='r_acromioclavicular'/> visualization sphere within <HAnimSegment name='r_scapula'/>
TouchSensor1266 = x3d.TouchSensor()
TouchSensor1266.description = "HAnimJoint r_acromioclavicular, HAnimSegment r_scapula"

HAnimSegment1265.children.append(TouchSensor1266)
Transform1267 = x3d.Transform()
Transform1267.translation = [-0.0962,1.4269,-0.0424]
Shape1268 = x3d.Shape()
Shape1268.USE = "HAnimJointShape"

Transform1267.children.append(Shape1268)

HAnimSegment1265.children.append(Transform1267)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_acromioclavicular'/> to <HAnimJoint name='r_shoulder'/>
Shape1269 = x3d.Shape()
LineSet1270 = x3d.LineSet()
LineSet1270.vertexCount = [2]
Coordinate1271 = x3d.Coordinate()
Coordinate1271.point = (-0.0962,1.4269,-0.0424,-0.2029,1.4376,-0.0387)

LineSet1270.coord = Coordinate1271
ColorRGBA1272 = x3d.ColorRGBA()
ColorRGBA1272.USE = "HAnimSegmentLineColorRGBA"

LineSet1270.color = ColorRGBA1272

Shape1269.geometry = LineSet1270

HAnimSegment1265.children.append(Shape1269)

HAnimJoint1264.children.append(HAnimSegment1265)
HAnimJoint1273 = x3d.HAnimJoint()
HAnimJoint1273.name = "r_shoulder"
HAnimJoint1273.DEF = "hanim_r_shoulder"
HAnimJoint1273.center = [-0.2029,1.4376,-0.0387]
HAnimJoint1273.ulimit = [0,0,0]
HAnimJoint1273.llimit = [0,0,0]
HAnimSegment1274 = x3d.HAnimSegment()
HAnimSegment1274.name = "r_upperarm"
HAnimSegment1274.DEF = "hanim_r_upperarm"
#<HAnimJoint name='r_shoulder'/> visualization sphere within <HAnimSegment name='r_upperarm'/>
TouchSensor1275 = x3d.TouchSensor()
TouchSensor1275.description = "HAnimJoint r_shoulder, HAnimSegment r_upperarm"

HAnimSegment1274.children.append(TouchSensor1275)
Transform1276 = x3d.Transform()
Transform1276.translation = [-0.2029,1.4376,-0.0387]
Shape1277 = x3d.Shape()
Shape1277.USE = "HAnimJointShape"

Transform1276.children.append(Shape1277)

HAnimSegment1274.children.append(Transform1276)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_shoulder'/> to <HAnimJoint name='r_elbow'/>
Shape1278 = x3d.Shape()
LineSet1279 = x3d.LineSet()
LineSet1279.vertexCount = [2]
Coordinate1280 = x3d.Coordinate()
Coordinate1280.point = (-0.2029,1.4376,-0.0387,-0.2014,1.1357,-0.0682)

LineSet1279.coord = Coordinate1280
ColorRGBA1281 = x3d.ColorRGBA()
ColorRGBA1281.USE = "HAnimSegmentLineColorRGBA"

LineSet1279.color = ColorRGBA1281

Shape1278.geometry = LineSet1279

HAnimSegment1274.children.append(Shape1278)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_shoulder'/> to <HAnimSite name='r_humeral_lateral_epicn'/>
Shape1282 = x3d.Shape()
LineSet1283 = x3d.LineSet()
LineSet1283.vertexCount = [2]
Coordinate1284 = x3d.Coordinate()
Coordinate1284.point = (-0.2029,1.4376,-0.0387,-0.2224,1.1517,-0.1033)

LineSet1283.coord = Coordinate1284
ColorRGBA1285 = x3d.ColorRGBA()
ColorRGBA1285.USE = "HAnimSiteLineColorRGBA"

LineSet1283.color = ColorRGBA1285

Shape1282.geometry = LineSet1283

HAnimSegment1274.children.append(Shape1282)
HAnimSite1286 = x3d.HAnimSite()
HAnimSite1286.name = "r_humeral_lateral_epicn_pt"
HAnimSite1286.DEF = "hanim_r_humeral_lateral_epicn_pt"
HAnimSite1286.translation = [-0.2224,1.1517,-0.1033]
#HAnimSite visualization shape
TouchSensor1287 = x3d.TouchSensor()
TouchSensor1287.description = "HAnimSite r_humeral_lateral_epicn"

HAnimSite1286.children.append(TouchSensor1287)
Shape1288 = x3d.Shape()
Shape1288.USE = "HAnimSiteShape"

HAnimSite1286.children.append(Shape1288)

HAnimSegment1274.children.append(HAnimSite1286)

HAnimJoint1273.children.append(HAnimSegment1274)
HAnimJoint1289 = x3d.HAnimJoint()
HAnimJoint1289.name = "r_elbow"
HAnimJoint1289.DEF = "hanim_r_elbow"
HAnimJoint1289.center = [-0.2014,1.1357,-0.0682]
HAnimJoint1289.ulimit = [0,0,0]
HAnimJoint1289.llimit = [0,0,0]
HAnimSegment1290 = x3d.HAnimSegment()
HAnimSegment1290.name = "r_forearm"
HAnimSegment1290.DEF = "hanim_r_forearm"
#<HAnimJoint name='r_elbow'/> visualization sphere within <HAnimSegment name='r_forearm'/>
TouchSensor1291 = x3d.TouchSensor()
TouchSensor1291.description = "HAnimJoint r_elbow, HAnimSegment r_forearm"

HAnimSegment1290.children.append(TouchSensor1291)
Transform1292 = x3d.Transform()
Transform1292.translation = [-0.2014,1.1357,-0.0682]
Shape1293 = x3d.Shape()
Shape1293.USE = "HAnimJointShape"

Transform1292.children.append(Shape1293)

HAnimSegment1290.children.append(Transform1292)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_elbow'/> to <HAnimJoint name='r_wrist'/>
Shape1294 = x3d.Shape()
LineSet1295 = x3d.LineSet()
LineSet1295.vertexCount = [2]
Coordinate1296 = x3d.Coordinate()
Coordinate1296.point = (-0.2014,1.1357,-0.0682,-0.1984,0.8663,-0.0583)

LineSet1295.coord = Coordinate1296
ColorRGBA1297 = x3d.ColorRGBA()
ColorRGBA1297.USE = "HAnimSegmentLineColorRGBA"

LineSet1295.color = ColorRGBA1297

Shape1294.geometry = LineSet1295

HAnimSegment1290.children.append(Shape1294)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_elbow'/> to <HAnimSite name='r_radial_styloid'/>
Shape1298 = x3d.Shape()
LineSet1299 = x3d.LineSet()
LineSet1299.vertexCount = [2]
Coordinate1300 = x3d.Coordinate()
Coordinate1300.point = (-0.2014,1.1357,-0.0682,-0.1884,0.8676,-0.0360)

LineSet1299.coord = Coordinate1300
ColorRGBA1301 = x3d.ColorRGBA()
ColorRGBA1301.USE = "HAnimSiteLineColorRGBA"

LineSet1299.color = ColorRGBA1301

Shape1298.geometry = LineSet1299

HAnimSegment1290.children.append(Shape1298)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_elbow'/> to <HAnimSite name='r_olecranon'/>
Shape1302 = x3d.Shape()
LineSet1303 = x3d.LineSet()
LineSet1303.vertexCount = [2]
Coordinate1304 = x3d.Coordinate()
Coordinate1304.point = (-0.2014,1.1357,-0.0682,-0.1907,1.1405,-0.1065)

LineSet1303.coord = Coordinate1304
ColorRGBA1305 = x3d.ColorRGBA()
ColorRGBA1305.USE = "HAnimSiteLineColorRGBA"

LineSet1303.color = ColorRGBA1305

Shape1302.geometry = LineSet1303

HAnimSegment1290.children.append(Shape1302)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_elbow'/> to <HAnimSite name='r_humeral_medial_epicn'/>
Shape1306 = x3d.Shape()
LineSet1307 = x3d.LineSet()
LineSet1307.vertexCount = [2]
Coordinate1308 = x3d.Coordinate()
Coordinate1308.point = (-0.2014,1.1357,-0.0682,-0.1680,1.1298,-0.1062)

LineSet1307.coord = Coordinate1308
ColorRGBA1309 = x3d.ColorRGBA()
ColorRGBA1309.USE = "HAnimSiteLineColorRGBA"

LineSet1307.color = ColorRGBA1309

Shape1306.geometry = LineSet1307

HAnimSegment1290.children.append(Shape1306)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_elbow'/> to <HAnimSite name='r_radiale'/>
Shape1310 = x3d.Shape()
LineSet1311 = x3d.LineSet()
LineSet1311.vertexCount = [2]
Coordinate1312 = x3d.Coordinate()
Coordinate1312.point = (-0.2014,1.1357,-0.0682,-0.2130,1.1305,-0.1091)

LineSet1311.coord = Coordinate1312
ColorRGBA1313 = x3d.ColorRGBA()
ColorRGBA1313.USE = "HAnimSiteLineColorRGBA"

LineSet1311.color = ColorRGBA1313

Shape1310.geometry = LineSet1311

HAnimSegment1290.children.append(Shape1310)
HAnimSite1314 = x3d.HAnimSite()
HAnimSite1314.name = "r_radial_styloid_pt"
HAnimSite1314.DEF = "hanim_r_radial_styloid_pt"
HAnimSite1314.translation = [-0.1884,0.8676,-0.036]
#HAnimSite visualization shape
TouchSensor1315 = x3d.TouchSensor()
TouchSensor1315.description = "HAnimSite r_radial_styloid"

HAnimSite1314.children.append(TouchSensor1315)
Shape1316 = x3d.Shape()
Shape1316.USE = "HAnimSiteShape"

HAnimSite1314.children.append(Shape1316)

HAnimSegment1290.children.append(HAnimSite1314)
HAnimSite1317 = x3d.HAnimSite()
HAnimSite1317.name = "r_olecranon_pt"
HAnimSite1317.DEF = "hanim_r_olecranon_pt"
HAnimSite1317.translation = [-0.1907,1.1405,-0.1065]
#HAnimSite visualization shape
TouchSensor1318 = x3d.TouchSensor()
TouchSensor1318.description = "HAnimSite r_olecranon"

HAnimSite1317.children.append(TouchSensor1318)
Shape1319 = x3d.Shape()
Shape1319.USE = "HAnimSiteShape"

HAnimSite1317.children.append(Shape1319)

HAnimSegment1290.children.append(HAnimSite1317)
HAnimSite1320 = x3d.HAnimSite()
HAnimSite1320.name = "r_humeral_medial_epicn_pt"
HAnimSite1320.DEF = "hanim_r_humeral_medial_epicn_pt"
HAnimSite1320.translation = [-0.168,1.1298,-0.1062]
#HAnimSite visualization shape
TouchSensor1321 = x3d.TouchSensor()
TouchSensor1321.description = "HAnimSite r_humeral_medial_epicn"

HAnimSite1320.children.append(TouchSensor1321)
Shape1322 = x3d.Shape()
Shape1322.USE = "HAnimSiteShape"

HAnimSite1320.children.append(Shape1322)

HAnimSegment1290.children.append(HAnimSite1320)
HAnimSite1323 = x3d.HAnimSite()
HAnimSite1323.name = "r_radiale_pt"
HAnimSite1323.DEF = "hanim_r_radiale_pt"
HAnimSite1323.translation = [-0.213,1.1305,-0.1091]
#HAnimSite visualization shape
TouchSensor1324 = x3d.TouchSensor()
TouchSensor1324.description = "HAnimSite r_radiale"

HAnimSite1323.children.append(TouchSensor1324)
Shape1325 = x3d.Shape()
Shape1325.USE = "HAnimSiteShape"

HAnimSite1323.children.append(Shape1325)

HAnimSegment1290.children.append(HAnimSite1323)

HAnimJoint1289.children.append(HAnimSegment1290)
HAnimJoint1326 = x3d.HAnimJoint()
HAnimJoint1326.name = "r_wrist"
HAnimJoint1326.DEF = "hanim_r_wrist"
HAnimJoint1326.center = [-0.1984,0.8663,-0.0583]
HAnimJoint1326.ulimit = [0,0,0]
HAnimJoint1326.llimit = [0,0,0]
HAnimSegment1327 = x3d.HAnimSegment()
HAnimSegment1327.name = "r_hand"
HAnimSegment1327.DEF = "hanim_r_hand"
#<HAnimJoint name='r_wrist'/> visualization sphere within <HAnimSegment name='r_hand'/>
TouchSensor1328 = x3d.TouchSensor()
TouchSensor1328.description = "HAnimJoint r_wrist, HAnimSegment r_hand"

HAnimSegment1327.children.append(TouchSensor1328)
Transform1329 = x3d.Transform()
Transform1329.translation = [-0.1984,0.8663,-0.0583]
Shape1330 = x3d.Shape()
Shape1330.USE = "HAnimJointShape"

Transform1329.children.append(Shape1330)

HAnimSegment1327.children.append(Transform1329)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_wrist'/> to <HAnimJoint name='r_thumb1'/>
Shape1331 = x3d.Shape()
LineSet1332 = x3d.LineSet()
LineSet1332.vertexCount = [2]
Coordinate1333 = x3d.Coordinate()
Coordinate1333.point = (-0.1984,0.8663,-0.0583,-0.1924,0.8472,-0.0534)

LineSet1332.coord = Coordinate1333
ColorRGBA1334 = x3d.ColorRGBA()
ColorRGBA1334.USE = "HAnimSegmentLineColorRGBA"

LineSet1332.color = ColorRGBA1334

Shape1331.geometry = LineSet1332

HAnimSegment1327.children.append(Shape1331)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_wrist'/> to <HAnimJoint name='r_index0'/>
Shape1335 = x3d.Shape()
LineSet1336 = x3d.LineSet()
LineSet1336.vertexCount = [2]
Coordinate1337 = x3d.Coordinate()
Coordinate1337.point = (-0.1984,0.8663,-0.0583,-0.1983,0.8024,-0.0280)

LineSet1336.coord = Coordinate1337
ColorRGBA1338 = x3d.ColorRGBA()
ColorRGBA1338.USE = "HAnimSegmentLineColorRGBA"

LineSet1336.color = ColorRGBA1338

Shape1335.geometry = LineSet1336

HAnimSegment1327.children.append(Shape1335)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_wrist'/> to <HAnimJoint name='r_middle0'/>
Shape1339 = x3d.Shape()
LineSet1340 = x3d.LineSet()
LineSet1340.vertexCount = [2]
Coordinate1341 = x3d.Coordinate()
Coordinate1341.point = (-0.1984,0.8663,-0.0583,-0.1987,0.8029,-0.0530)

LineSet1340.coord = Coordinate1341
ColorRGBA1342 = x3d.ColorRGBA()
ColorRGBA1342.USE = "HAnimSegmentLineColorRGBA"

LineSet1340.color = ColorRGBA1342

Shape1339.geometry = LineSet1340

HAnimSegment1327.children.append(Shape1339)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_wrist'/> to <HAnimJoint name='r_ring0'/>
Shape1343 = x3d.Shape()
LineSet1344 = x3d.LineSet()
LineSet1344.vertexCount = [2]
Coordinate1345 = x3d.Coordinate()
Coordinate1345.point = (-0.1984,0.8663,-0.0583,-0.1956,0.8019,-0.0794)

LineSet1344.coord = Coordinate1345
ColorRGBA1346 = x3d.ColorRGBA()
ColorRGBA1346.USE = "HAnimSegmentLineColorRGBA"

LineSet1344.color = ColorRGBA1346

Shape1343.geometry = LineSet1344

HAnimSegment1327.children.append(Shape1343)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_wrist'/> to <HAnimJoint name='r_pinky0'/>
Shape1347 = x3d.Shape()
LineSet1348 = x3d.LineSet()
LineSet1348.vertexCount = [2]
Coordinate1349 = x3d.Coordinate()
Coordinate1349.point = (-0.1984,0.8663,-0.0583,-0.1925,0.8066,-0.1036)

LineSet1348.coord = Coordinate1349
ColorRGBA1350 = x3d.ColorRGBA()
ColorRGBA1350.USE = "HAnimSegmentLineColorRGBA"

LineSet1348.color = ColorRGBA1350

Shape1347.geometry = LineSet1348

HAnimSegment1327.children.append(Shape1347)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_wrist'/> to <HAnimSite name='r_metacarpal_pha2'/>
Shape1351 = x3d.Shape()
LineSet1352 = x3d.LineSet()
LineSet1352.vertexCount = [2]
Coordinate1353 = x3d.Coordinate()
Coordinate1353.point = (-0.1984,0.8663,-0.0583,-0.1977,0.8169,-0.0177)

LineSet1352.coord = Coordinate1353
ColorRGBA1354 = x3d.ColorRGBA()
ColorRGBA1354.USE = "HAnimSiteLineColorRGBA"

LineSet1352.color = ColorRGBA1354

Shape1351.geometry = LineSet1352

HAnimSegment1327.children.append(Shape1351)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_wrist'/> to <HAnimSite name='r_ulnar_styloid'/>
Shape1355 = x3d.Shape()
LineSet1356 = x3d.LineSet()
LineSet1356.vertexCount = [2]
Coordinate1357 = x3d.Coordinate()
Coordinate1357.point = (-0.1984,0.8663,-0.0583,-0.2117,0.8562,-0.0584)

LineSet1356.coord = Coordinate1357
ColorRGBA1358 = x3d.ColorRGBA()
ColorRGBA1358.USE = "HAnimSiteLineColorRGBA"

LineSet1356.color = ColorRGBA1358

Shape1355.geometry = LineSet1356

HAnimSegment1327.children.append(Shape1355)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_wrist'/> to <HAnimSite name='r_metacarpal_pha5'/>
Shape1359 = x3d.Shape()
LineSet1360 = x3d.LineSet()
LineSet1360.vertexCount = [2]
Coordinate1361 = x3d.Coordinate()
Coordinate1361.point = (-0.1984,0.8663,-0.0583,-0.1929,0.7890,-0.1064)

LineSet1360.coord = Coordinate1361
ColorRGBA1362 = x3d.ColorRGBA()
ColorRGBA1362.USE = "HAnimSiteLineColorRGBA"

LineSet1360.color = ColorRGBA1362

Shape1359.geometry = LineSet1360

HAnimSegment1327.children.append(Shape1359)
#HAnimSite/Viewpoint visualization line segment from ancestor <HAnimJoint name='r_wrist'/> to <HAnimSite name='r_hand_front_view'/>
Shape1363 = x3d.Shape()
LineSet1364 = x3d.LineSet()
LineSet1364.vertexCount = [2]
Coordinate1365 = x3d.Coordinate()
Coordinate1365.point = (-0.1984,0.8663,-0.0583,-0.3000,0.7500,0.4500)

LineSet1364.coord = Coordinate1365
ColorRGBA1366 = x3d.ColorRGBA()
ColorRGBA1366.USE = "HAnimSiteViewpointLineColorRGBA"

LineSet1364.color = ColorRGBA1366

Shape1363.geometry = LineSet1364

HAnimSegment1327.children.append(Shape1363)
HAnimSite1367 = x3d.HAnimSite()
HAnimSite1367.name = "r_metacarpal_pha2_pt"
HAnimSite1367.DEF = "hanim_r_metacarpal_pha2_pt"
HAnimSite1367.translation = [-0.1977,0.8169,-0.0177]
#HAnimSite visualization shape
TouchSensor1368 = x3d.TouchSensor()
TouchSensor1368.description = "HAnimSite r_metacarpal_pha2"

HAnimSite1367.children.append(TouchSensor1368)
Shape1369 = x3d.Shape()
Shape1369.USE = "HAnimSiteShape"

HAnimSite1367.children.append(Shape1369)

HAnimSegment1327.children.append(HAnimSite1367)
HAnimSite1370 = x3d.HAnimSite()
HAnimSite1370.name = "r_ulnar_styloid_pt"
HAnimSite1370.DEF = "hanim_r_ulnar_styloid_pt"
HAnimSite1370.translation = [-0.2117,0.8562,-0.0584]
#HAnimSite visualization shape
TouchSensor1371 = x3d.TouchSensor()
TouchSensor1371.description = "HAnimSite r_ulnar_styloid"

HAnimSite1370.children.append(TouchSensor1371)
Shape1372 = x3d.Shape()
Shape1372.USE = "HAnimSiteShape"

HAnimSite1370.children.append(Shape1372)

HAnimSegment1327.children.append(HAnimSite1370)
HAnimSite1373 = x3d.HAnimSite()
HAnimSite1373.name = "r_metacarpal_pha5_pt"
HAnimSite1373.DEF = "hanim_r_metacarpal_pha5_pt"
HAnimSite1373.translation = [-0.1929,0.789,-0.1064]
#HAnimSite visualization shape
TouchSensor1374 = x3d.TouchSensor()
TouchSensor1374.description = "HAnimSite r_metacarpal_pha5"

HAnimSite1373.children.append(TouchSensor1374)
Shape1375 = x3d.Shape()
Shape1375.USE = "HAnimSiteShape"

HAnimSite1373.children.append(Shape1375)

HAnimSegment1327.children.append(HAnimSite1373)
HAnimSite1376 = x3d.HAnimSite()
HAnimSite1376.name = "r_hand_front_view"
HAnimSite1376.DEF = "hanim_r_hand_front_view"
HAnimSite1376.translation = [-0.3,0.75,0.45]
Viewpoint1377 = x3d.Viewpoint()
Viewpoint1377.DEF = "hanim_r_hand_front_viewpoint"
Viewpoint1377.centerOfRotation = [0,0.7,0]
Viewpoint1377.description = "right hand front"
Viewpoint1377.position = [0,0,0]

HAnimSite1376.children.append(Viewpoint1377)
#HAnimSite/Viewpoint visualization shape
Anchor1378 = x3d.Anchor()
Anchor1378.description = "HAnimSite Viewpoint hanim_r_hand_front_view"
Anchor1378.url = ["#hanim_r_hand_front_viewpoint"]
LOD1379 = x3d.LOD()
LOD1379.forceTransitions = True
LOD1379.range = [0.04]
WorldInfo1380 = x3d.WorldInfo()
WorldInfo1380.info = ["hide diamond when close"]

LOD1379.children.append(WorldInfo1380)
Shape1381 = x3d.Shape()
Shape1381.USE = "HAnimSiteViewpointShape"

LOD1379.children.append(Shape1381)

Anchor1378.children.append(LOD1379)

HAnimSite1376.children.append(Anchor1378)

HAnimSegment1327.children.append(HAnimSite1376)

HAnimJoint1326.children.append(HAnimSegment1327)
HAnimJoint1382 = x3d.HAnimJoint()
HAnimJoint1382.name = "r_thumb1"
HAnimJoint1382.DEF = "hanim_r_thumb1"
HAnimJoint1382.center = [-0.1924,0.8472,-0.0534]
HAnimJoint1382.ulimit = [0,0,0]
HAnimJoint1382.llimit = [0,0,0]
HAnimSegment1383 = x3d.HAnimSegment()
HAnimSegment1383.name = "r_thumb_metacarpal"
HAnimSegment1383.DEF = "hanim_r_thumb_metacarpal"
#<HAnimJoint name='r_thumb1'/> visualization sphere within <HAnimSegment name='r_thumb_metacarpal'/>
TouchSensor1384 = x3d.TouchSensor()
TouchSensor1384.description = "HAnimJoint r_thumb1, HAnimSegment r_thumb_metacarpal"

HAnimSegment1383.children.append(TouchSensor1384)
Transform1385 = x3d.Transform()
Transform1385.translation = [-0.1924,0.8472,-0.0534]
Shape1386 = x3d.Shape()
Shape1386.USE = "HAnimJointShape"

Transform1385.children.append(Shape1386)

HAnimSegment1383.children.append(Transform1385)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_thumb1'/> to <HAnimJoint name='r_thumb2'/>
Shape1387 = x3d.Shape()
LineSet1388 = x3d.LineSet()
LineSet1388.vertexCount = [2]
Coordinate1389 = x3d.Coordinate()
Coordinate1389.point = (-0.1924,0.8472,-0.0534,-0.1951,0.8226,0.0246)

LineSet1388.coord = Coordinate1389
ColorRGBA1390 = x3d.ColorRGBA()
ColorRGBA1390.USE = "HAnimSegmentLineColorRGBA"

LineSet1388.color = ColorRGBA1390

Shape1387.geometry = LineSet1388

HAnimSegment1383.children.append(Shape1387)

HAnimJoint1382.children.append(HAnimSegment1383)
HAnimJoint1391 = x3d.HAnimJoint()
HAnimJoint1391.name = "r_thumb2"
HAnimJoint1391.DEF = "hanim_r_thumb2"
HAnimJoint1391.center = [-0.1951,0.8226,0.0246]
HAnimJoint1391.ulimit = [0,0,0]
HAnimJoint1391.llimit = [0,0,0]
HAnimSegment1392 = x3d.HAnimSegment()
HAnimSegment1392.name = "r_thumb_proximal"
HAnimSegment1392.DEF = "hanim_r_thumb_proximal"
#<HAnimJoint name='r_thumb2'/> visualization sphere within <HAnimSegment name='r_thumb_proximal'/>
TouchSensor1393 = x3d.TouchSensor()
TouchSensor1393.description = "HAnimJoint r_thumb2, HAnimSegment r_thumb_proximal"

HAnimSegment1392.children.append(TouchSensor1393)
Transform1394 = x3d.Transform()
Transform1394.translation = [-0.1951,0.8226,0.0246]
Shape1395 = x3d.Shape()
Shape1395.USE = "HAnimJointShape"

Transform1394.children.append(Shape1395)

HAnimSegment1392.children.append(Transform1394)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_thumb2'/> to <HAnimJoint name='r_thumb3'/>
Shape1396 = x3d.Shape()
LineSet1397 = x3d.LineSet()
LineSet1397.vertexCount = [2]
Coordinate1398 = x3d.Coordinate()
Coordinate1398.point = (-0.1951,0.8226,0.0246,-0.1955,0.8159,0.0464)

LineSet1397.coord = Coordinate1398
ColorRGBA1399 = x3d.ColorRGBA()
ColorRGBA1399.USE = "HAnimSegmentLineColorRGBA"

LineSet1397.color = ColorRGBA1399

Shape1396.geometry = LineSet1397

HAnimSegment1392.children.append(Shape1396)

HAnimJoint1391.children.append(HAnimSegment1392)
HAnimJoint1400 = x3d.HAnimJoint()
HAnimJoint1400.name = "r_thumb3"
HAnimJoint1400.DEF = "hanim_r_thumb3"
HAnimJoint1400.center = [-0.1955,0.8159,0.0464]
HAnimJoint1400.ulimit = [0,0,0]
HAnimJoint1400.llimit = [0,0,0]
HAnimSegment1401 = x3d.HAnimSegment()
HAnimSegment1401.name = "r_thumb_distal"
HAnimSegment1401.DEF = "hanim_r_thumb_distal"
#<HAnimJoint name='r_thumb3'/> visualization sphere within <HAnimSegment name='r_thumb_distal'/>
TouchSensor1402 = x3d.TouchSensor()
TouchSensor1402.description = "HAnimJoint r_thumb3, HAnimSegment r_thumb_distal"

HAnimSegment1401.children.append(TouchSensor1402)
Transform1403 = x3d.Transform()
Transform1403.translation = [-0.1955,0.8159,0.0464]
Shape1404 = x3d.Shape()
Shape1404.USE = "HAnimJointShape"

Transform1403.children.append(Shape1404)

HAnimSegment1401.children.append(Transform1403)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_thumb3'/> to <HAnimSite name='r_thumb_distal_tip'/>
Shape1405 = x3d.Shape()
LineSet1406 = x3d.LineSet()
LineSet1406.vertexCount = [2]
Coordinate1407 = x3d.Coordinate()
Coordinate1407.point = (-0.1955,0.8159,0.0464,-0.1869,0.8090,0.0820)

LineSet1406.coord = Coordinate1407
ColorRGBA1408 = x3d.ColorRGBA()
ColorRGBA1408.USE = "HAnimSiteLineColorRGBA"

LineSet1406.color = ColorRGBA1408

Shape1405.geometry = LineSet1406

HAnimSegment1401.children.append(Shape1405)
HAnimSite1409 = x3d.HAnimSite()
HAnimSite1409.name = "r_thumb_distal_tip"
HAnimSite1409.DEF = "hanim_r_thumb_distal_tip"
HAnimSite1409.translation = [-0.1869,0.809,0.082]
#HAnimSite visualization shape
TouchSensor1410 = x3d.TouchSensor()
TouchSensor1410.description = "HAnimSite r_thumb_distal_tip"

HAnimSite1409.children.append(TouchSensor1410)
Shape1411 = x3d.Shape()
Shape1411.USE = "HAnimSiteShape"

HAnimSite1409.children.append(Shape1411)

HAnimSegment1401.children.append(HAnimSite1409)

HAnimJoint1400.children.append(HAnimSegment1401)

HAnimJoint1391.children.append(HAnimJoint1400)

HAnimJoint1382.children.append(HAnimJoint1391)

HAnimJoint1326.children.append(HAnimJoint1382)
HAnimJoint1412 = x3d.HAnimJoint()
HAnimJoint1412.name = "r_index0"
HAnimJoint1412.DEF = "hanim_r_index0"
HAnimJoint1412.center = [-0.1983,0.8024,-0.028]
HAnimJoint1412.ulimit = [0,0,0]
HAnimJoint1412.llimit = [0,0,0]
HAnimSegment1413 = x3d.HAnimSegment()
HAnimSegment1413.name = "r_index_metacarpal"
HAnimSegment1413.DEF = "hanim_r_index_metacarpal"
#<HAnimJoint name='r_index0'/> visualization sphere within <HAnimSegment name='r_index_metacarpal'/>
TouchSensor1414 = x3d.TouchSensor()
TouchSensor1414.description = "HAnimJoint r_index0, HAnimSegment r_index_metacarpal"

HAnimSegment1413.children.append(TouchSensor1414)
Transform1415 = x3d.Transform()
Transform1415.translation = [-0.1983,0.8024,-0.028]
Shape1416 = x3d.Shape()
Shape1416.USE = "HAnimJointShape"

Transform1415.children.append(Shape1416)

HAnimSegment1413.children.append(Transform1415)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_index0'/> to <HAnimJoint name='r_index1'/>
Shape1417 = x3d.Shape()
LineSet1418 = x3d.LineSet()
LineSet1418.vertexCount = [2]
Coordinate1419 = x3d.Coordinate()
Coordinate1419.point = (-0.1983,0.8024,-0.0280,-0.1983,0.7815,-0.0280)

LineSet1418.coord = Coordinate1419
ColorRGBA1420 = x3d.ColorRGBA()
ColorRGBA1420.USE = "HAnimSegmentLineColorRGBA"

LineSet1418.color = ColorRGBA1420

Shape1417.geometry = LineSet1418

HAnimSegment1413.children.append(Shape1417)

HAnimJoint1412.children.append(HAnimSegment1413)
HAnimJoint1421 = x3d.HAnimJoint()
HAnimJoint1421.name = "r_index1"
HAnimJoint1421.DEF = "hanim_r_index1"
HAnimJoint1421.center = [-0.1983,0.7815,-0.028]
HAnimJoint1421.ulimit = [0,0,0]
HAnimJoint1421.llimit = [0,0,0]
HAnimSegment1422 = x3d.HAnimSegment()
HAnimSegment1422.name = "r_index_proximal"
HAnimSegment1422.DEF = "hanim_r_index_proximal"
#<HAnimJoint name='r_index1'/> visualization sphere within <HAnimSegment name='r_index_proximal'/>
TouchSensor1423 = x3d.TouchSensor()
TouchSensor1423.description = "HAnimJoint r_index1, HAnimSegment r_index_proximal"

HAnimSegment1422.children.append(TouchSensor1423)
Transform1424 = x3d.Transform()
Transform1424.translation = [-0.1983,0.7815,-0.028]
Shape1425 = x3d.Shape()
Shape1425.USE = "HAnimJointShape"

Transform1424.children.append(Shape1425)

HAnimSegment1422.children.append(Transform1424)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_index1'/> to <HAnimJoint name='r_index2'/>
Shape1426 = x3d.Shape()
LineSet1427 = x3d.LineSet()
LineSet1427.vertexCount = [2]
Coordinate1428 = x3d.Coordinate()
Coordinate1428.point = (-0.1983,0.7815,-0.0280,-0.2017,0.7363,-0.0248)

LineSet1427.coord = Coordinate1428
ColorRGBA1429 = x3d.ColorRGBA()
ColorRGBA1429.USE = "HAnimSegmentLineColorRGBA"

LineSet1427.color = ColorRGBA1429

Shape1426.geometry = LineSet1427

HAnimSegment1422.children.append(Shape1426)

HAnimJoint1421.children.append(HAnimSegment1422)
HAnimJoint1430 = x3d.HAnimJoint()
HAnimJoint1430.name = "r_index2"
HAnimJoint1430.DEF = "hanim_r_index2"
HAnimJoint1430.center = [-0.2017,0.7363,-0.0248]
HAnimJoint1430.ulimit = [0,0,0]
HAnimJoint1430.llimit = [0,0,0]
HAnimSegment1431 = x3d.HAnimSegment()
HAnimSegment1431.name = "r_index_middle"
HAnimSegment1431.DEF = "hanim_r_index_middle"
#<HAnimJoint name='r_index2'/> visualization sphere within <HAnimSegment name='r_index_middle'/>
TouchSensor1432 = x3d.TouchSensor()
TouchSensor1432.description = "HAnimJoint r_index2, HAnimSegment r_index_middle"

HAnimSegment1431.children.append(TouchSensor1432)
Transform1433 = x3d.Transform()
Transform1433.translation = [-0.2017,0.7363,-0.0248]
Shape1434 = x3d.Shape()
Shape1434.USE = "HAnimJointShape"

Transform1433.children.append(Shape1434)

HAnimSegment1431.children.append(Transform1433)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_index2'/> to <HAnimJoint name='r_index3'/>
Shape1435 = x3d.Shape()
LineSet1436 = x3d.LineSet()
LineSet1436.vertexCount = [2]
Coordinate1437 = x3d.Coordinate()
Coordinate1437.point = (-0.2017,0.7363,-0.0248,-0.2028,0.7139,-0.0236)

LineSet1436.coord = Coordinate1437
ColorRGBA1438 = x3d.ColorRGBA()
ColorRGBA1438.USE = "HAnimSegmentLineColorRGBA"

LineSet1436.color = ColorRGBA1438

Shape1435.geometry = LineSet1436

HAnimSegment1431.children.append(Shape1435)

HAnimJoint1430.children.append(HAnimSegment1431)
HAnimJoint1439 = x3d.HAnimJoint()
HAnimJoint1439.name = "r_index3"
HAnimJoint1439.DEF = "hanim_r_index3"
HAnimJoint1439.center = [-0.2028,0.7139,-0.0236]
HAnimJoint1439.ulimit = [0,0,0]
HAnimJoint1439.llimit = [0,0,0]
HAnimSegment1440 = x3d.HAnimSegment()
HAnimSegment1440.name = "r_index_distal"
HAnimSegment1440.DEF = "hanim_r_index_distal"
#<HAnimJoint name='r_index3'/> visualization sphere within <HAnimSegment name='r_index_distal'/>
TouchSensor1441 = x3d.TouchSensor()
TouchSensor1441.description = "HAnimJoint r_index3, HAnimSegment r_index_distal"

HAnimSegment1440.children.append(TouchSensor1441)
Transform1442 = x3d.Transform()
Transform1442.translation = [-0.2028,0.7139,-0.0236]
Shape1443 = x3d.Shape()
Shape1443.USE = "HAnimJointShape"

Transform1442.children.append(Shape1443)

HAnimSegment1440.children.append(Transform1442)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_index3'/> to <HAnimSite name='r_index_distal_tip'/>
Shape1444 = x3d.Shape()
LineSet1445 = x3d.LineSet()
LineSet1445.vertexCount = [2]
Coordinate1446 = x3d.Coordinate()
Coordinate1446.point = (-0.2028,0.7139,-0.0236,-0.1980,0.6883,-0.0180)

LineSet1445.coord = Coordinate1446
ColorRGBA1447 = x3d.ColorRGBA()
ColorRGBA1447.USE = "HAnimSiteLineColorRGBA"

LineSet1445.color = ColorRGBA1447

Shape1444.geometry = LineSet1445

HAnimSegment1440.children.append(Shape1444)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_index3'/> to <HAnimSite name='r_dactylion'/>
Shape1448 = x3d.Shape()
LineSet1449 = x3d.LineSet()
LineSet1449.vertexCount = [2]
Coordinate1450 = x3d.Coordinate()
Coordinate1450.point = (-0.2028,0.7139,-0.0236,-0.1941,0.6772,-0.0423)

LineSet1449.coord = Coordinate1450
ColorRGBA1451 = x3d.ColorRGBA()
ColorRGBA1451.USE = "HAnimSiteLineColorRGBA"

LineSet1449.color = ColorRGBA1451

Shape1448.geometry = LineSet1449

HAnimSegment1440.children.append(Shape1448)
HAnimSite1452 = x3d.HAnimSite()
HAnimSite1452.name = "r_index_distal_tip"
HAnimSite1452.DEF = "hanim_r_index_distal_tip"
HAnimSite1452.translation = [-0.198,0.6883,-0.018]
#HAnimSite visualization shape
TouchSensor1453 = x3d.TouchSensor()
TouchSensor1453.description = "HAnimSite r_index_distal_tip"

HAnimSite1452.children.append(TouchSensor1453)
Shape1454 = x3d.Shape()
Shape1454.USE = "HAnimSiteShape"

HAnimSite1452.children.append(Shape1454)

HAnimSegment1440.children.append(HAnimSite1452)
HAnimSite1455 = x3d.HAnimSite()
HAnimSite1455.name = "r_dactylion_pt"
HAnimSite1455.DEF = "hanim_r_dactylion_pt"
HAnimSite1455.translation = [-0.1941,0.6772,-0.0423]
#HAnimSite visualization shape
TouchSensor1456 = x3d.TouchSensor()
TouchSensor1456.description = "HAnimSite r_dactylion"

HAnimSite1455.children.append(TouchSensor1456)
Shape1457 = x3d.Shape()
Shape1457.USE = "HAnimSiteShape"

HAnimSite1455.children.append(Shape1457)

HAnimSegment1440.children.append(HAnimSite1455)

HAnimJoint1439.children.append(HAnimSegment1440)

HAnimJoint1430.children.append(HAnimJoint1439)

HAnimJoint1421.children.append(HAnimJoint1430)

HAnimJoint1412.children.append(HAnimJoint1421)

HAnimJoint1326.children.append(HAnimJoint1412)
HAnimJoint1458 = x3d.HAnimJoint()
HAnimJoint1458.name = "r_middle0"
HAnimJoint1458.DEF = "hanim_r_middle0"
HAnimJoint1458.center = [-0.1987,0.8029,-0.053]
HAnimJoint1458.ulimit = [0,0,0]
HAnimJoint1458.llimit = [0,0,0]
HAnimSegment1459 = x3d.HAnimSegment()
HAnimSegment1459.name = "r_middle_metacarpal"
HAnimSegment1459.DEF = "hanim_r_middle_metacarpal"
#<HAnimJoint name='r_middle0'/> visualization sphere within <HAnimSegment name='r_middle_metacarpal'/>
TouchSensor1460 = x3d.TouchSensor()
TouchSensor1460.description = "HAnimJoint r_middle0, HAnimSegment r_middle_metacarpal"

HAnimSegment1459.children.append(TouchSensor1460)
Transform1461 = x3d.Transform()
Transform1461.translation = [-0.1987,0.8029,-0.053]
Shape1462 = x3d.Shape()
Shape1462.USE = "HAnimJointShape"

Transform1461.children.append(Shape1462)

HAnimSegment1459.children.append(Transform1461)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_middle0'/> to <HAnimJoint name='r_middle1'/>
Shape1463 = x3d.Shape()
LineSet1464 = x3d.LineSet()
LineSet1464.vertexCount = [2]
Coordinate1465 = x3d.Coordinate()
Coordinate1465.point = (-0.1987,0.8029,-0.0530,-0.1987,0.7818,-0.0530)

LineSet1464.coord = Coordinate1465
ColorRGBA1466 = x3d.ColorRGBA()
ColorRGBA1466.USE = "HAnimSegmentLineColorRGBA"

LineSet1464.color = ColorRGBA1466

Shape1463.geometry = LineSet1464

HAnimSegment1459.children.append(Shape1463)

HAnimJoint1458.children.append(HAnimSegment1459)
HAnimJoint1467 = x3d.HAnimJoint()
HAnimJoint1467.name = "r_middle1"
HAnimJoint1467.DEF = "hanim_r_middle1"
HAnimJoint1467.center = [-0.1987,0.7818,-0.053]
HAnimJoint1467.ulimit = [0,0,0]
HAnimJoint1467.llimit = [0,0,0]
HAnimSegment1468 = x3d.HAnimSegment()
HAnimSegment1468.name = "r_middle_proximal"
HAnimSegment1468.DEF = "hanim_r_middle_proximal"
#<HAnimJoint name='r_middle1'/> visualization sphere within <HAnimSegment name='r_middle_proximal'/>
TouchSensor1469 = x3d.TouchSensor()
TouchSensor1469.description = "HAnimJoint r_middle1, HAnimSegment r_middle_proximal"

HAnimSegment1468.children.append(TouchSensor1469)
Transform1470 = x3d.Transform()
Transform1470.translation = [-0.1987,0.7818,-0.053]
Shape1471 = x3d.Shape()
Shape1471.USE = "HAnimJointShape"

Transform1470.children.append(Shape1471)

HAnimSegment1468.children.append(Transform1470)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_middle1'/> to <HAnimJoint name='r_middle2'/>
Shape1472 = x3d.Shape()
LineSet1473 = x3d.LineSet()
LineSet1473.vertexCount = [2]
Coordinate1474 = x3d.Coordinate()
Coordinate1474.point = (-0.1987,0.7818,-0.0530,-0.2013,0.7273,-0.0503)

LineSet1473.coord = Coordinate1474
ColorRGBA1475 = x3d.ColorRGBA()
ColorRGBA1475.USE = "HAnimSegmentLineColorRGBA"

LineSet1473.color = ColorRGBA1475

Shape1472.geometry = LineSet1473

HAnimSegment1468.children.append(Shape1472)

HAnimJoint1467.children.append(HAnimSegment1468)
HAnimJoint1476 = x3d.HAnimJoint()
HAnimJoint1476.name = "r_middle2"
HAnimJoint1476.DEF = "hanim_r_middle2"
HAnimJoint1476.center = [-0.2013,0.7273,-0.0503]
HAnimJoint1476.ulimit = [0,0,0]
HAnimJoint1476.llimit = [0,0,0]
HAnimSegment1477 = x3d.HAnimSegment()
HAnimSegment1477.name = "r_middle_middle"
HAnimSegment1477.DEF = "hanim_r_middle_middle"
#<HAnimJoint name='r_middle2'/> visualization sphere within <HAnimSegment name='r_middle_middle'/>
TouchSensor1478 = x3d.TouchSensor()
TouchSensor1478.description = "HAnimJoint r_middle2, HAnimSegment r_middle_middle"

HAnimSegment1477.children.append(TouchSensor1478)
Transform1479 = x3d.Transform()
Transform1479.translation = [-0.2013,0.7273,-0.0503]
Shape1480 = x3d.Shape()
Shape1480.USE = "HAnimJointShape"

Transform1479.children.append(Shape1480)

HAnimSegment1477.children.append(Transform1479)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_middle2'/> to <HAnimJoint name='r_middle3'/>
Shape1481 = x3d.Shape()
LineSet1482 = x3d.LineSet()
LineSet1482.vertexCount = [2]
Coordinate1483 = x3d.Coordinate()
Coordinate1483.point = (-0.2013,0.7273,-0.0503,-0.2026,0.7011,-0.0494)

LineSet1482.coord = Coordinate1483
ColorRGBA1484 = x3d.ColorRGBA()
ColorRGBA1484.USE = "HAnimSegmentLineColorRGBA"

LineSet1482.color = ColorRGBA1484

Shape1481.geometry = LineSet1482

HAnimSegment1477.children.append(Shape1481)

HAnimJoint1476.children.append(HAnimSegment1477)
HAnimJoint1485 = x3d.HAnimJoint()
HAnimJoint1485.name = "r_middle3"
HAnimJoint1485.DEF = "hanim_r_middle3"
HAnimJoint1485.center = [-0.2026,0.7011,-0.0494]
HAnimJoint1485.ulimit = [0,0,0]
HAnimJoint1485.llimit = [0,0,0]
HAnimSegment1486 = x3d.HAnimSegment()
HAnimSegment1486.name = "r_middle_distal"
HAnimSegment1486.DEF = "hanim_r_middle_distal"
#<HAnimJoint name='r_middle3'/> visualization sphere within <HAnimSegment name='r_middle_distal'/>
TouchSensor1487 = x3d.TouchSensor()
TouchSensor1487.description = "HAnimJoint r_middle3, HAnimSegment r_middle_distal"

HAnimSegment1486.children.append(TouchSensor1487)
Transform1488 = x3d.Transform()
Transform1488.translation = [-0.2026,0.7011,-0.0494]
Shape1489 = x3d.Shape()
Shape1489.USE = "HAnimJointShape"

Transform1488.children.append(Shape1489)

HAnimSegment1486.children.append(Transform1488)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_middle3'/> to <HAnimSite name='r_middle_distal_tip'/>
Shape1490 = x3d.Shape()
LineSet1491 = x3d.LineSet()
LineSet1491.vertexCount = [2]
Coordinate1492 = x3d.Coordinate()
Coordinate1492.point = (-0.2026,0.7011,-0.0494,-0.1969,0.6758,-0.0427)

LineSet1491.coord = Coordinate1492
ColorRGBA1493 = x3d.ColorRGBA()
ColorRGBA1493.USE = "HAnimSiteLineColorRGBA"

LineSet1491.color = ColorRGBA1493

Shape1490.geometry = LineSet1491

HAnimSegment1486.children.append(Shape1490)
HAnimSite1494 = x3d.HAnimSite()
HAnimSite1494.name = "r_middle_distal_tip"
HAnimSite1494.DEF = "hanim_r_middle_distal_tip"
HAnimSite1494.translation = [-0.1969,0.6758,-0.0427]
#HAnimSite visualization shape
TouchSensor1495 = x3d.TouchSensor()
TouchSensor1495.description = "HAnimSite r_middle_distal_tip"

HAnimSite1494.children.append(TouchSensor1495)
Shape1496 = x3d.Shape()
Shape1496.USE = "HAnimSiteShape"

HAnimSite1494.children.append(Shape1496)

HAnimSegment1486.children.append(HAnimSite1494)

HAnimJoint1485.children.append(HAnimSegment1486)

HAnimJoint1476.children.append(HAnimJoint1485)

HAnimJoint1467.children.append(HAnimJoint1476)

HAnimJoint1458.children.append(HAnimJoint1467)

HAnimJoint1326.children.append(HAnimJoint1458)
HAnimJoint1497 = x3d.HAnimJoint()
HAnimJoint1497.name = "r_ring0"
HAnimJoint1497.DEF = "hanim_r_ring0"
HAnimJoint1497.center = [-0.1956,0.8019,-0.0794]
HAnimJoint1497.ulimit = [0,0,0]
HAnimJoint1497.llimit = [0,0,0]
HAnimSegment1498 = x3d.HAnimSegment()
HAnimSegment1498.name = "r_ring_metacarpal"
HAnimSegment1498.DEF = "hanim_r_ring_metacarpal"
#<HAnimJoint name='r_ring0'/> visualization sphere within <HAnimSegment name='r_ring_metacarpal'/>
TouchSensor1499 = x3d.TouchSensor()
TouchSensor1499.description = "HAnimJoint r_ring0, HAnimSegment r_ring_metacarpal"

HAnimSegment1498.children.append(TouchSensor1499)
Transform1500 = x3d.Transform()
Transform1500.translation = [-0.1956,0.8019,-0.0794]
Shape1501 = x3d.Shape()
Shape1501.USE = "HAnimJointShape"

Transform1500.children.append(Shape1501)

HAnimSegment1498.children.append(Transform1500)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_ring0'/> to <HAnimJoint name='r_ring1'/>
Shape1502 = x3d.Shape()
LineSet1503 = x3d.LineSet()
LineSet1503.vertexCount = [2]
Coordinate1504 = x3d.Coordinate()
Coordinate1504.point = (-0.1956,0.8019,-0.0794,-0.1956,0.7815,-0.0794)

LineSet1503.coord = Coordinate1504
ColorRGBA1505 = x3d.ColorRGBA()
ColorRGBA1505.USE = "HAnimSegmentLineColorRGBA"

LineSet1503.color = ColorRGBA1505

Shape1502.geometry = LineSet1503

HAnimSegment1498.children.append(Shape1502)

HAnimJoint1497.children.append(HAnimSegment1498)
HAnimJoint1506 = x3d.HAnimJoint()
HAnimJoint1506.name = "r_ring1"
HAnimJoint1506.DEF = "hanim_r_ring1"
HAnimJoint1506.center = [-0.1956,0.7815,-0.0794]
HAnimJoint1506.ulimit = [0,0,0]
HAnimJoint1506.llimit = [0,0,0]
HAnimSegment1507 = x3d.HAnimSegment()
HAnimSegment1507.name = "r_ring_proximal"
HAnimSegment1507.DEF = "hanim_r_ring_proximal"
#<HAnimJoint name='r_ring1'/> visualization sphere within <HAnimSegment name='r_ring_proximal'/>
TouchSensor1508 = x3d.TouchSensor()
TouchSensor1508.description = "HAnimJoint r_ring1, HAnimSegment r_ring_proximal"

HAnimSegment1507.children.append(TouchSensor1508)
Transform1509 = x3d.Transform()
Transform1509.translation = [-0.1956,0.7815,-0.0794]
Shape1510 = x3d.Shape()
Shape1510.USE = "HAnimJointShape"

Transform1509.children.append(Shape1510)

HAnimSegment1507.children.append(Transform1509)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_ring1'/> to <HAnimJoint name='r_ring2'/>
Shape1511 = x3d.Shape()
LineSet1512 = x3d.LineSet()
LineSet1512.vertexCount = [2]
Coordinate1513 = x3d.Coordinate()
Coordinate1513.point = (-0.1956,0.7815,-0.0794,-0.1973,0.7287,-0.0777)

LineSet1512.coord = Coordinate1513
ColorRGBA1514 = x3d.ColorRGBA()
ColorRGBA1514.USE = "HAnimSegmentLineColorRGBA"

LineSet1512.color = ColorRGBA1514

Shape1511.geometry = LineSet1512

HAnimSegment1507.children.append(Shape1511)

HAnimJoint1506.children.append(HAnimSegment1507)
HAnimJoint1515 = x3d.HAnimJoint()
HAnimJoint1515.name = "r_ring2"
HAnimJoint1515.DEF = "hanim_r_ring2"
HAnimJoint1515.center = [-0.1973,0.7287,-0.0777]
HAnimJoint1515.ulimit = [0,0,0]
HAnimJoint1515.llimit = [0,0,0]
HAnimSegment1516 = x3d.HAnimSegment()
HAnimSegment1516.name = "r_ring_middle"
HAnimSegment1516.DEF = "hanim_r_ring_middle"
#<HAnimJoint name='r_ring2'/> visualization sphere within <HAnimSegment name='r_ring_middle'/>
TouchSensor1517 = x3d.TouchSensor()
TouchSensor1517.description = "HAnimJoint r_ring2, HAnimSegment r_ring_middle"

HAnimSegment1516.children.append(TouchSensor1517)
Transform1518 = x3d.Transform()
Transform1518.translation = [-0.1973,0.7287,-0.0777]
Shape1519 = x3d.Shape()
Shape1519.USE = "HAnimJointShape"

Transform1518.children.append(Shape1519)

HAnimSegment1516.children.append(Transform1518)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_ring2'/> to <HAnimJoint name='r_ring3'/>
Shape1520 = x3d.Shape()
LineSet1521 = x3d.LineSet()
LineSet1521.vertexCount = [2]
Coordinate1522 = x3d.Coordinate()
Coordinate1522.point = (-0.1973,0.7287,-0.0777,-0.1983,0.7045,-0.0767)

LineSet1521.coord = Coordinate1522
ColorRGBA1523 = x3d.ColorRGBA()
ColorRGBA1523.USE = "HAnimSegmentLineColorRGBA"

LineSet1521.color = ColorRGBA1523

Shape1520.geometry = LineSet1521

HAnimSegment1516.children.append(Shape1520)

HAnimJoint1515.children.append(HAnimSegment1516)
HAnimJoint1524 = x3d.HAnimJoint()
HAnimJoint1524.name = "r_ring3"
HAnimJoint1524.DEF = "hanim_r_ring3"
HAnimJoint1524.center = [-0.1983,0.7045,-0.0767]
HAnimJoint1524.ulimit = [0,0,0]
HAnimJoint1524.llimit = [0,0,0]
HAnimSegment1525 = x3d.HAnimSegment()
HAnimSegment1525.name = "r_ring_distal"
HAnimSegment1525.DEF = "hanim_r_ring_distal"
#<HAnimJoint name='r_ring3'/> visualization sphere within <HAnimSegment name='r_ring_distal'/>
TouchSensor1526 = x3d.TouchSensor()
TouchSensor1526.description = "HAnimJoint r_ring3, HAnimSegment r_ring_distal"

HAnimSegment1525.children.append(TouchSensor1526)
Transform1527 = x3d.Transform()
Transform1527.translation = [-0.1983,0.7045,-0.0767]
Shape1528 = x3d.Shape()
Shape1528.USE = "HAnimJointShape"

Transform1527.children.append(Shape1528)

HAnimSegment1525.children.append(Transform1527)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_ring3'/> to <HAnimSite name='r_ring_distal_tip'/>
Shape1529 = x3d.Shape()
LineSet1530 = x3d.LineSet()
LineSet1530.vertexCount = [2]
Coordinate1531 = x3d.Coordinate()
Coordinate1531.point = (-0.1983,0.7045,-0.0767,-0.1934,0.6778,-0.0693)

LineSet1530.coord = Coordinate1531
ColorRGBA1532 = x3d.ColorRGBA()
ColorRGBA1532.USE = "HAnimSiteLineColorRGBA"

LineSet1530.color = ColorRGBA1532

Shape1529.geometry = LineSet1530

HAnimSegment1525.children.append(Shape1529)
HAnimSite1533 = x3d.HAnimSite()
HAnimSite1533.name = "r_ring_distal_tip"
HAnimSite1533.DEF = "hanim_r_ring_distal_tip"
HAnimSite1533.translation = [-0.1934,0.6778,-0.0693]
#HAnimSite visualization shape
TouchSensor1534 = x3d.TouchSensor()
TouchSensor1534.description = "HAnimSite r_ring_distal_tip"

HAnimSite1533.children.append(TouchSensor1534)
Shape1535 = x3d.Shape()
Shape1535.USE = "HAnimSiteShape"

HAnimSite1533.children.append(Shape1535)

HAnimSegment1525.children.append(HAnimSite1533)

HAnimJoint1524.children.append(HAnimSegment1525)

HAnimJoint1515.children.append(HAnimJoint1524)

HAnimJoint1506.children.append(HAnimJoint1515)

HAnimJoint1497.children.append(HAnimJoint1506)

HAnimJoint1326.children.append(HAnimJoint1497)
HAnimJoint1536 = x3d.HAnimJoint()
HAnimJoint1536.name = "r_pinky0"
HAnimJoint1536.DEF = "hanim_r_pinky0"
HAnimJoint1536.center = [-0.1925,0.8066,-0.1036]
HAnimJoint1536.ulimit = [0,0,0]
HAnimJoint1536.llimit = [0,0,0]
HAnimSegment1537 = x3d.HAnimSegment()
HAnimSegment1537.name = "r_pinky_metacarpal"
HAnimSegment1537.DEF = "hanim_r_pinky_metacarpal"
#<HAnimJoint name='r_pinky0'/> visualization sphere within <HAnimSegment name='r_pinky_metacarpal'/>
TouchSensor1538 = x3d.TouchSensor()
TouchSensor1538.description = "HAnimJoint r_pinky0, HAnimSegment r_pinky_metacarpal"

HAnimSegment1537.children.append(TouchSensor1538)
Transform1539 = x3d.Transform()
Transform1539.translation = [-0.1925,0.8066,-0.1036]
Shape1540 = x3d.Shape()
Shape1540.USE = "HAnimJointShape"

Transform1539.children.append(Shape1540)

HAnimSegment1537.children.append(Transform1539)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_pinky0'/> to <HAnimJoint name='r_pinky1'/>
Shape1541 = x3d.Shape()
LineSet1542 = x3d.LineSet()
LineSet1542.vertexCount = [2]
Coordinate1543 = x3d.Coordinate()
Coordinate1543.point = (-0.1925,0.8066,-0.1036,-0.1925,0.7866,-0.1036)

LineSet1542.coord = Coordinate1543
ColorRGBA1544 = x3d.ColorRGBA()
ColorRGBA1544.USE = "HAnimSegmentLineColorRGBA"

LineSet1542.color = ColorRGBA1544

Shape1541.geometry = LineSet1542

HAnimSegment1537.children.append(Shape1541)

HAnimJoint1536.children.append(HAnimSegment1537)
HAnimJoint1545 = x3d.HAnimJoint()
HAnimJoint1545.name = "r_pinky1"
HAnimJoint1545.DEF = "hanim_r_pinky1"
HAnimJoint1545.center = [-0.1925,0.7866,-0.1036]
HAnimJoint1545.ulimit = [0,0,0]
HAnimJoint1545.llimit = [0,0,0]
HAnimSegment1546 = x3d.HAnimSegment()
HAnimSegment1546.name = "r_pinky_proximal"
HAnimSegment1546.DEF = "hanim_r_pinky_proximal"
#<HAnimJoint name='r_pinky1'/> visualization sphere within <HAnimSegment name='r_pinky_proximal'/>
TouchSensor1547 = x3d.TouchSensor()
TouchSensor1547.description = "HAnimJoint r_pinky1, HAnimSegment r_pinky_proximal"

HAnimSegment1546.children.append(TouchSensor1547)
Transform1548 = x3d.Transform()
Transform1548.translation = [-0.1925,0.7866,-0.1036]
Shape1549 = x3d.Shape()
Shape1549.USE = "HAnimJointShape"

Transform1548.children.append(Shape1549)

HAnimSegment1546.children.append(Transform1548)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_pinky1'/> to <HAnimJoint name='r_pinky2'/>
Shape1550 = x3d.Shape()
LineSet1551 = x3d.LineSet()
LineSet1551.vertexCount = [2]
Coordinate1552 = x3d.Coordinate()
Coordinate1552.point = (-0.1925,0.7866,-0.1036,-0.1938,0.7452,-0.1024)

LineSet1551.coord = Coordinate1552
ColorRGBA1553 = x3d.ColorRGBA()
ColorRGBA1553.USE = "HAnimSegmentLineColorRGBA"

LineSet1551.color = ColorRGBA1553

Shape1550.geometry = LineSet1551

HAnimSegment1546.children.append(Shape1550)

HAnimJoint1545.children.append(HAnimSegment1546)
HAnimJoint1554 = x3d.HAnimJoint()
HAnimJoint1554.name = "r_pinky2"
HAnimJoint1554.DEF = "hanim_r_pinky2"
HAnimJoint1554.center = [-0.1938,0.7452,-0.1024]
HAnimJoint1554.ulimit = [0,0,0]
HAnimJoint1554.llimit = [0,0,0]
HAnimSegment1555 = x3d.HAnimSegment()
HAnimSegment1555.name = "r_pinky_middle"
HAnimSegment1555.DEF = "hanim_r_pinky_middle"
#<HAnimJoint name='r_pinky2'/> visualization sphere within <HAnimSegment name='r_pinky_middle'/>
TouchSensor1556 = x3d.TouchSensor()
TouchSensor1556.description = "HAnimJoint r_pinky2, HAnimSegment r_pinky_middle"

HAnimSegment1555.children.append(TouchSensor1556)
Transform1557 = x3d.Transform()
Transform1557.translation = [-0.1938,0.7452,-0.1024]
Shape1558 = x3d.Shape()
Shape1558.USE = "HAnimJointShape"

Transform1557.children.append(Shape1558)

HAnimSegment1555.children.append(Transform1557)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_pinky2'/> to <HAnimJoint name='r_pinky3'/>
Shape1559 = x3d.Shape()
LineSet1560 = x3d.LineSet()
LineSet1560.vertexCount = [2]
Coordinate1561 = x3d.Coordinate()
Coordinate1561.point = (-0.1938,0.7452,-0.1024,-0.1948,0.7277,-0.1017)

LineSet1560.coord = Coordinate1561
ColorRGBA1562 = x3d.ColorRGBA()
ColorRGBA1562.USE = "HAnimSegmentLineColorRGBA"

LineSet1560.color = ColorRGBA1562

Shape1559.geometry = LineSet1560

HAnimSegment1555.children.append(Shape1559)

HAnimJoint1554.children.append(HAnimSegment1555)
HAnimJoint1563 = x3d.HAnimJoint()
HAnimJoint1563.name = "r_pinky3"
HAnimJoint1563.DEF = "hanim_r_pinky3"
HAnimJoint1563.center = [-0.1948,0.7277,-0.1017]
HAnimJoint1563.ulimit = [0,0,0]
HAnimJoint1563.llimit = [0,0,0]
HAnimSegment1564 = x3d.HAnimSegment()
HAnimSegment1564.name = "r_pinky_distal"
HAnimSegment1564.DEF = "hanim_r_pinky_distal"
#<HAnimJoint name='r_pinky3'/> visualization sphere within <HAnimSegment name='r_pinky_distal'/>
TouchSensor1565 = x3d.TouchSensor()
TouchSensor1565.description = "HAnimJoint r_pinky3, HAnimSegment r_pinky_distal"

HAnimSegment1564.children.append(TouchSensor1565)
Transform1566 = x3d.Transform()
Transform1566.translation = [-0.1948,0.7277,-0.1017]
Shape1567 = x3d.Shape()
Shape1567.USE = "HAnimJointShape"

Transform1566.children.append(Shape1567)

HAnimSegment1564.children.append(Transform1566)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_pinky3'/> to <HAnimSite name='r_pinky_distal_tip'/>
Shape1568 = x3d.Shape()
LineSet1569 = x3d.LineSet()
LineSet1569.vertexCount = [2]
Coordinate1570 = x3d.Coordinate()
Coordinate1570.point = (-0.1948,0.7277,-0.1017,-0.1938,0.7035,-0.0949)

LineSet1569.coord = Coordinate1570
ColorRGBA1571 = x3d.ColorRGBA()
ColorRGBA1571.USE = "HAnimSiteLineColorRGBA"

LineSet1569.color = ColorRGBA1571

Shape1568.geometry = LineSet1569

HAnimSegment1564.children.append(Shape1568)
HAnimSite1572 = x3d.HAnimSite()
HAnimSite1572.name = "r_pinky_distal_tip"
HAnimSite1572.DEF = "hanim_r_pinky_distal_tip"
HAnimSite1572.translation = [-0.1938,0.7035,-0.0949]
#HAnimSite visualization shape
TouchSensor1573 = x3d.TouchSensor()
TouchSensor1573.description = "HAnimSite r_pinky_distal_tip"

HAnimSite1572.children.append(TouchSensor1573)
Shape1574 = x3d.Shape()
Shape1574.USE = "HAnimSiteShape"

HAnimSite1572.children.append(Shape1574)

HAnimSegment1564.children.append(HAnimSite1572)

HAnimJoint1563.children.append(HAnimSegment1564)

HAnimJoint1554.children.append(HAnimJoint1563)

HAnimJoint1545.children.append(HAnimJoint1554)

HAnimJoint1536.children.append(HAnimJoint1545)

HAnimJoint1326.children.append(HAnimJoint1536)

HAnimJoint1289.children.append(HAnimJoint1326)

HAnimJoint1273.children.append(HAnimJoint1289)

HAnimJoint1264.children.append(HAnimJoint1273)

HAnimJoint1227.children.append(HAnimJoint1264)

HAnimJoint595.children.append(HAnimJoint1227)

HAnimJoint586.children.append(HAnimJoint595)

HAnimJoint577.children.append(HAnimJoint586)

HAnimJoint568.children.append(HAnimJoint577)

HAnimJoint559.children.append(HAnimJoint568)

HAnimJoint550.children.append(HAnimJoint559)

HAnimJoint541.children.append(HAnimJoint550)

HAnimJoint532.children.append(HAnimJoint541)

HAnimJoint509.children.append(HAnimJoint532)

HAnimJoint493.children.append(HAnimJoint509)

HAnimJoint484.children.append(HAnimJoint493)

HAnimJoint475.children.append(HAnimJoint484)

HAnimJoint466.children.append(HAnimJoint475)

HAnimJoint436.children.append(HAnimJoint466)

HAnimJoint427.children.append(HAnimJoint436)

HAnimJoint418.children.append(HAnimJoint427)

HAnimJoint395.children.append(HAnimJoint418)

HAnimJoint45.children.append(HAnimJoint395)

HAnimHumanoid44.skeleton.append(HAnimJoint45)
#USE nodes for inverse kinematics (IK) engines and other tools
#Top-level HAnimSite/Viewpoint nodes for viewing the humanoid without being affected by body motion
HAnimSite1575 = x3d.HAnimSite()
HAnimSite1575.name = "l_inclined_view"
HAnimSite1575.DEF = "hanim_l_inclined_view"
HAnimSite1575.rotation = [-0.113,0.993,0.0347,0.671]
HAnimSite1575.translation = [1.62,1.05,2.06]
Viewpoint1576 = x3d.Viewpoint()
Viewpoint1576.DEF = "hanim_l_inclined_viewpoint"
Viewpoint1576.description = "left inclined"
Viewpoint1576.position = [0,0,0]

HAnimSite1575.children.append(Viewpoint1576)
#HAnimSite/Viewpoint visualization shape
Anchor1577 = x3d.Anchor()
Anchor1577.description = "HAnimSite Viewpoint hanim_l_inclined_view"
Anchor1577.url = ["#hanim_l_inclined_viewpoint"]
LOD1578 = x3d.LOD()
LOD1578.forceTransitions = True
LOD1578.range = [0.04]
WorldInfo1579 = x3d.WorldInfo()
WorldInfo1579.info = ["hide diamond when close"]

LOD1578.children.append(WorldInfo1579)
Shape1580 = x3d.Shape()
Shape1580.USE = "HAnimSiteViewpointShape"

LOD1578.children.append(Shape1580)

Anchor1577.children.append(LOD1578)

HAnimSite1575.children.append(Anchor1577)

HAnimHumanoid44.viewpoints.append(HAnimSite1575)
HAnimSite1581 = x3d.HAnimSite()
HAnimSite1581.name = "r_inclined_view"
HAnimSite1581.DEF = "hanim_r_inclined_view"
HAnimSite1581.rotation = [-0.113,-0.993,0.0347,0.671]
HAnimSite1581.translation = [-1.62,1.05,2.06]
Viewpoint1582 = x3d.Viewpoint()
Viewpoint1582.DEF = "hanim_r_inclined_viewpoint"
Viewpoint1582.centerOfRotation = [0,0.9,0]
Viewpoint1582.description = "right inclined"
Viewpoint1582.position = [0,0,0]

HAnimSite1581.children.append(Viewpoint1582)
#HAnimSite/Viewpoint visualization shape
Anchor1583 = x3d.Anchor()
Anchor1583.description = "HAnimSite Viewpoint hanim_r_inclined_view"
Anchor1583.url = ["#hanim_r_inclined_viewpoint"]
LOD1584 = x3d.LOD()
LOD1584.forceTransitions = True
LOD1584.range = [0.04]
WorldInfo1585 = x3d.WorldInfo()
WorldInfo1585.info = ["hide diamond when close"]

LOD1584.children.append(WorldInfo1585)
Shape1586 = x3d.Shape()
Shape1586.USE = "HAnimSiteViewpointShape"

LOD1584.children.append(Shape1586)

Anchor1583.children.append(LOD1584)

HAnimSite1581.children.append(Anchor1583)

HAnimHumanoid44.viewpoints.append(HAnimSite1581)
HAnimSite1587 = x3d.HAnimSite()
HAnimSite1587.name = "front_view"
HAnimSite1587.DEF = "hanim_front_view"
HAnimSite1587.translation = [0,0.85,2.58]
Viewpoint1588 = x3d.Viewpoint()
Viewpoint1588.DEF = "hanim_front_viewpoint"
Viewpoint1588.centerOfRotation = [0,0.9,0]
Viewpoint1588.description = "front"
Viewpoint1588.position = [0,0,0]

HAnimSite1587.children.append(Viewpoint1588)
#HAnimSite/Viewpoint visualization shape
Anchor1589 = x3d.Anchor()
Anchor1589.description = "HAnimSite Viewpoint hanim_front_view"
Anchor1589.url = ["#hanim_front_viewpoint"]
LOD1590 = x3d.LOD()
LOD1590.forceTransitions = True
LOD1590.range = [0.04]
WorldInfo1591 = x3d.WorldInfo()
WorldInfo1591.info = ["hide diamond when close"]

LOD1590.children.append(WorldInfo1591)
Shape1592 = x3d.Shape()
Shape1592.USE = "HAnimSiteViewpointShape"

LOD1590.children.append(Shape1592)

Anchor1589.children.append(LOD1590)

HAnimSite1587.children.append(Anchor1589)

HAnimHumanoid44.viewpoints.append(HAnimSite1587)
HAnimSite1593 = x3d.HAnimSite()
HAnimSite1593.name = "back_view"
HAnimSite1593.DEF = "hanim_back_view"
HAnimSite1593.rotation = [0,1,0,3.14]
HAnimSite1593.translation = [0,0.85,-2.58]
Viewpoint1594 = x3d.Viewpoint()
Viewpoint1594.DEF = "hanim_back_viewpoint"
Viewpoint1594.centerOfRotation = [0,0.9,0]
Viewpoint1594.description = "back"
Viewpoint1594.position = [0,0,0]

HAnimSite1593.children.append(Viewpoint1594)
#HAnimSite/Viewpoint visualization shape
Anchor1595 = x3d.Anchor()
Anchor1595.description = "HAnimSite Viewpoint hanim_back_view"
Anchor1595.url = ["#hanim_back_viewpoint"]
LOD1596 = x3d.LOD()
LOD1596.forceTransitions = True
LOD1596.range = [0.04]
WorldInfo1597 = x3d.WorldInfo()
WorldInfo1597.info = ["hide diamond when close"]

LOD1596.children.append(WorldInfo1597)
Shape1598 = x3d.Shape()
Shape1598.USE = "HAnimSiteViewpointShape"

LOD1596.children.append(Shape1598)

Anchor1595.children.append(LOD1596)

HAnimSite1593.children.append(Anchor1595)

HAnimHumanoid44.viewpoints.append(HAnimSite1593)
HAnimSite1599 = x3d.HAnimSite()
HAnimSite1599.name = "l_side_view"
HAnimSite1599.DEF = "hanim_l_side_view"
HAnimSite1599.rotation = [0,1,0,1.5708]
HAnimSite1599.translation = [2.6,0.854,0]
Viewpoint1600 = x3d.Viewpoint()
Viewpoint1600.DEF = "hanim_l_side_viewpoint"
Viewpoint1600.centerOfRotation = [0,0.9,0]
Viewpoint1600.description = "left side"
Viewpoint1600.position = [0,0,0]

HAnimSite1599.children.append(Viewpoint1600)
#HAnimSite/Viewpoint visualization shape
Anchor1601 = x3d.Anchor()
Anchor1601.description = "HAnimSite Viewpoint hanim_l_side_view"
Anchor1601.url = ["#hanim_l_side_viewpoint"]
LOD1602 = x3d.LOD()
LOD1602.forceTransitions = True
LOD1602.range = [0.04]
WorldInfo1603 = x3d.WorldInfo()
WorldInfo1603.info = ["hide diamond when close"]

LOD1602.children.append(WorldInfo1603)
Shape1604 = x3d.Shape()
Shape1604.USE = "HAnimSiteViewpointShape"

LOD1602.children.append(Shape1604)

Anchor1601.children.append(LOD1602)

HAnimSite1599.children.append(Anchor1601)

HAnimHumanoid44.viewpoints.append(HAnimSite1599)
HAnimSite1605 = x3d.HAnimSite()
HAnimSite1605.name = "Top_view"
HAnimSite1605.DEF = "hanim_Top_view"
HAnimSite1605.rotation = [1,0,0,-1.57]
HAnimSite1605.translation = [0,3.5,0]
Viewpoint1606 = x3d.Viewpoint()
Viewpoint1606.DEF = "hanim_Top_viewpoint"
Viewpoint1606.centerOfRotation = [0,0.9,0]
Viewpoint1606.description = "Top"
Viewpoint1606.position = [0,0,0]

HAnimSite1605.children.append(Viewpoint1606)
#HAnimSite/Viewpoint visualization shape
Anchor1607 = x3d.Anchor()
Anchor1607.description = "HAnimSite Viewpoint hanim_Top_view"
Anchor1607.url = ["#hanim_Top_viewpoint"]
LOD1608 = x3d.LOD()
LOD1608.forceTransitions = True
LOD1608.range = [0.04]
WorldInfo1609 = x3d.WorldInfo()
WorldInfo1609.info = ["hide diamond when close"]

LOD1608.children.append(WorldInfo1609)
Shape1610 = x3d.Shape()
Shape1610.USE = "HAnimSiteViewpointShape"

LOD1608.children.append(Shape1610)

Anchor1607.children.append(LOD1608)

HAnimSite1605.children.append(Anchor1607)

HAnimHumanoid44.viewpoints.append(HAnimSite1605)
HAnimSite1611 = x3d.HAnimSite()
HAnimSite1611.name = "front_close_view"
HAnimSite1611.DEF = "hanim_front_close_view"
HAnimSite1611.translation = [0,0.854,1.575]
Viewpoint1612 = x3d.Viewpoint()
Viewpoint1612.DEF = "hanim_front_close_viewpoint"
Viewpoint1612.centerOfRotation = [0,0,1.575]
Viewpoint1612.description = "front close"
Viewpoint1612.position = [0,0,0]

HAnimSite1611.children.append(Viewpoint1612)
#HAnimSite/Viewpoint visualization shape
Anchor1613 = x3d.Anchor()
Anchor1613.description = "HAnimSite Viewpoint hanim_front_close_view"
Anchor1613.url = ["#hanim_front_close_viewpoint"]
LOD1614 = x3d.LOD()
LOD1614.forceTransitions = True
LOD1614.range = [0.04]
WorldInfo1615 = x3d.WorldInfo()
WorldInfo1615.info = ["hide diamond when close"]

LOD1614.children.append(WorldInfo1615)
Shape1616 = x3d.Shape()
Shape1616.USE = "HAnimSiteViewpointShape"

LOD1614.children.append(Shape1616)

Anchor1613.children.append(LOD1614)

HAnimSite1611.children.append(Anchor1613)

HAnimHumanoid44.viewpoints.append(HAnimSite1611)
HAnimSite1617 = x3d.HAnimSite()
HAnimSite1617.name = "side_close_view"
HAnimSite1617.DEF = "hanim_side_close_view"
HAnimSite1617.rotation = [0,1,0,1.5708]
HAnimSite1617.translation = [1.56,0.854,0]
Viewpoint1618 = x3d.Viewpoint()
Viewpoint1618.DEF = "hanim_side_close_viewpoint"
Viewpoint1618.centerOfRotation = [1.6,0,0]
Viewpoint1618.description = "side close"
Viewpoint1618.position = [0,0,0]

HAnimSite1617.children.append(Viewpoint1618)
#HAnimSite/Viewpoint visualization shape
Anchor1619 = x3d.Anchor()
Anchor1619.description = "HAnimSite Viewpoint hanim_side_close_view"
Anchor1619.url = ["#hanim_side_close_viewpoint"]
LOD1620 = x3d.LOD()
LOD1620.forceTransitions = True
LOD1620.range = [0.04]
WorldInfo1621 = x3d.WorldInfo()
WorldInfo1621.info = ["hide diamond when close"]

LOD1620.children.append(WorldInfo1621)
Shape1622 = x3d.Shape()
Shape1622.USE = "HAnimSiteViewpointShape"

LOD1620.children.append(Shape1622)

Anchor1619.children.append(LOD1620)

HAnimSite1617.children.append(Anchor1619)

HAnimHumanoid44.viewpoints.append(HAnimSite1617)
HAnimSite1623 = x3d.HAnimSite()
HAnimSite1623.name = "head_front_close_view"
HAnimSite1623.DEF = "hanim_head_front_close_view"
HAnimSite1623.translation = [0,1.5,1]
Viewpoint1624 = x3d.Viewpoint()
Viewpoint1624.DEF = "hanim_head_front_close_viewpoint"
Viewpoint1624.centerOfRotation = [0,0,1]
Viewpoint1624.description = "head front close"
Viewpoint1624.position = [0,0,0]

HAnimSite1623.children.append(Viewpoint1624)
#HAnimSite/Viewpoint visualization shape
Anchor1625 = x3d.Anchor()
Anchor1625.description = "HAnimSite Viewpoint hanim_head_front_close_view"
Anchor1625.url = ["#hanim_head_front_close_viewpoint"]
LOD1626 = x3d.LOD()
LOD1626.forceTransitions = True
LOD1626.range = [0.04]
WorldInfo1627 = x3d.WorldInfo()
WorldInfo1627.info = ["hide diamond when close"]

LOD1626.children.append(WorldInfo1627)
Shape1628 = x3d.Shape()
Shape1628.USE = "HAnimSiteViewpointShape"

LOD1626.children.append(Shape1628)

Anchor1625.children.append(LOD1626)

HAnimSite1623.children.append(Anchor1625)

HAnimHumanoid44.viewpoints.append(HAnimSite1623)
HAnimSite1629 = x3d.HAnimSite()
HAnimSite1629.name = "chest_front_close_view"
HAnimSite1629.DEF = "hanim_chest_front_close_view"
HAnimSite1629.translation = [0,1.2,1]
Viewpoint1630 = x3d.Viewpoint()
Viewpoint1630.DEF = "hanim_chest_front_close_viewpoint"
Viewpoint1630.centerOfRotation = [0,0,1]
Viewpoint1630.description = "chest front close"
Viewpoint1630.position = [0,0,0]

HAnimSite1629.children.append(Viewpoint1630)
#HAnimSite/Viewpoint visualization shape
Anchor1631 = x3d.Anchor()
Anchor1631.description = "HAnimSite Viewpoint hanim_chest_front_close_view"
Anchor1631.url = ["#hanim_chest_front_close_viewpoint"]
LOD1632 = x3d.LOD()
LOD1632.forceTransitions = True
LOD1632.range = [0.04]
WorldInfo1633 = x3d.WorldInfo()
WorldInfo1633.info = ["hide diamond when close"]

LOD1632.children.append(WorldInfo1633)
Shape1634 = x3d.Shape()
Shape1634.USE = "HAnimSiteViewpointShape"

LOD1632.children.append(Shape1634)

Anchor1631.children.append(LOD1632)

HAnimSite1629.children.append(Anchor1631)

HAnimHumanoid44.viewpoints.append(HAnimSite1629)
HAnimSite1635 = x3d.HAnimSite()
HAnimSite1635.name = "pelvis_front_close_view"
HAnimSite1635.DEF = "hanim_pelvis_front_close_view"
HAnimSite1635.translation = [0,0.8,1]
Viewpoint1636 = x3d.Viewpoint()
Viewpoint1636.DEF = "hanim_pelvis_front_close_viewpoint"
Viewpoint1636.centerOfRotation = [0,0,1]
Viewpoint1636.description = "pelvis front close"
Viewpoint1636.position = [0,0,0]

HAnimSite1635.children.append(Viewpoint1636)
#HAnimSite/Viewpoint visualization shape
Anchor1637 = x3d.Anchor()
Anchor1637.description = "HAnimSite Viewpoint hanim_pelvis_front_close_view"
Anchor1637.url = ["#hanim_pelvis_front_close_viewpoint"]
LOD1638 = x3d.LOD()
LOD1638.forceTransitions = True
LOD1638.range = [0.04]
WorldInfo1639 = x3d.WorldInfo()
WorldInfo1639.info = ["hide diamond when close"]

LOD1638.children.append(WorldInfo1639)
Shape1640 = x3d.Shape()
Shape1640.USE = "HAnimSiteViewpointShape"

LOD1638.children.append(Shape1640)

Anchor1637.children.append(LOD1638)

HAnimSite1635.children.append(Anchor1637)

HAnimHumanoid44.viewpoints.append(HAnimSite1635)
HAnimSite1641 = x3d.HAnimSite()
HAnimSite1641.name = "knees_front_close_view"
HAnimSite1641.DEF = "hanim_knees_front_close_view"
HAnimSite1641.translation = [0,0.4,1]
Viewpoint1642 = x3d.Viewpoint()
Viewpoint1642.DEF = "hanim_knees_front_close_viewpoint"
Viewpoint1642.centerOfRotation = [0,0.4,0]
Viewpoint1642.description = "knees front close"
Viewpoint1642.position = [0,0,0]

HAnimSite1641.children.append(Viewpoint1642)
#HAnimSite/Viewpoint visualization shape
Anchor1643 = x3d.Anchor()
Anchor1643.description = "HAnimSite Viewpoint hanim_knees_front_close_view"
Anchor1643.url = ["#hanim_knees_front_close_viewpoint"]
LOD1644 = x3d.LOD()
LOD1644.forceTransitions = True
LOD1644.range = [0.04]
WorldInfo1645 = x3d.WorldInfo()
WorldInfo1645.info = ["hide diamond when close"]

LOD1644.children.append(WorldInfo1645)
Shape1646 = x3d.Shape()
Shape1646.USE = "HAnimSiteViewpointShape"

LOD1644.children.append(Shape1646)

Anchor1643.children.append(LOD1644)

HAnimSite1641.children.append(Anchor1643)

HAnimHumanoid44.viewpoints.append(HAnimSite1641)
HAnimSite1647 = x3d.HAnimSite()
HAnimSite1647.name = "feet_front_close_view"
HAnimSite1647.DEF = "hanim_feet_front_close_view"
HAnimSite1647.translation = [0,0,1]
Viewpoint1648 = x3d.Viewpoint()
Viewpoint1648.DEF = "hanim_feet_front_close_viewpoint"
Viewpoint1648.description = "feet front close"
Viewpoint1648.position = [0,0,0]

HAnimSite1647.children.append(Viewpoint1648)
#HAnimSite/Viewpoint visualization shape
Anchor1649 = x3d.Anchor()
Anchor1649.description = "HAnimSite Viewpoint hanim_feet_front_close_view"
Anchor1649.url = ["#hanim_feet_front_close_viewpoint"]
LOD1650 = x3d.LOD()
LOD1650.forceTransitions = True
LOD1650.range = [0.04]
WorldInfo1651 = x3d.WorldInfo()
WorldInfo1651.info = ["hide diamond when close"]

LOD1650.children.append(WorldInfo1651)
Shape1652 = x3d.Shape()
Shape1652.USE = "HAnimSiteViewpointShape"

LOD1650.children.append(Shape1652)

Anchor1649.children.append(LOD1650)

HAnimSite1647.children.append(Anchor1649)

HAnimHumanoid44.viewpoints.append(HAnimSite1647)
HAnimSite1653 = x3d.HAnimSite()
HAnimSite1653.name = "eye_level_view"
HAnimSite1653.DEF = "hanim_eye_level_view"
HAnimSite1653.translation = [0,1.6332,0.0502]
Viewpoint1654 = x3d.Viewpoint()
Viewpoint1654.DEF = "hanim_eye_level_viewpoint"
Viewpoint1654.description = "eye level looking forward"
Viewpoint1654.orientation = [0,1,0,3.141593]
Viewpoint1654.position = [0,0,0]

HAnimSite1653.children.append(Viewpoint1654)
#HAnimSite/Viewpoint visualization shape
Anchor1655 = x3d.Anchor()
Anchor1655.description = "HAnimSite Viewpoint hanim_eye_level_view"
Anchor1655.url = ["#hanim_eye_level_viewpoint"]
LOD1656 = x3d.LOD()
LOD1656.forceTransitions = True
LOD1656.range = [0.04]
WorldInfo1657 = x3d.WorldInfo()
WorldInfo1657.info = ["hide diamond when close"]

LOD1656.children.append(WorldInfo1657)
Shape1658 = x3d.Shape()
Shape1658.USE = "HAnimSiteViewpointShape"

LOD1656.children.append(Shape1658)

Anchor1655.children.append(LOD1656)

HAnimSite1653.children.append(Anchor1655)

HAnimHumanoid44.viewpoints.append(HAnimSite1653)
HAnimSite1659 = x3d.HAnimSite()
HAnimSite1659.USE = "hanim_l_eyeball_site_view"

HAnimHumanoid44.sites.append(HAnimSite1659)
HAnimSite1660 = x3d.HAnimSite()
HAnimSite1660.USE = "hanim_r_eyeball_site_view"

HAnimHumanoid44.sites.append(HAnimSite1660)
HAnimSite1661 = x3d.HAnimSite()
HAnimSite1661.USE = "hanim_l_hand_front_view"

HAnimHumanoid44.sites.append(HAnimSite1661)
HAnimSite1662 = x3d.HAnimSite()
HAnimSite1662.USE = "hanim_r_hand_front_view"

HAnimHumanoid44.sites.append(HAnimSite1662)
HAnimJoint1663 = x3d.HAnimJoint()
HAnimJoint1663.USE = "hanim_humanoid_root"

HAnimHumanoid44.joints.append(HAnimJoint1663)
HAnimJoint1664 = x3d.HAnimJoint()
HAnimJoint1664.USE = "hanim_sacroiliac"

HAnimHumanoid44.joints.append(HAnimJoint1664)
HAnimJoint1665 = x3d.HAnimJoint()
HAnimJoint1665.USE = "hanim_vl5"

HAnimHumanoid44.joints.append(HAnimJoint1665)
HAnimJoint1666 = x3d.HAnimJoint()
HAnimJoint1666.USE = "hanim_vl4"

HAnimHumanoid44.joints.append(HAnimJoint1666)
HAnimJoint1667 = x3d.HAnimJoint()
HAnimJoint1667.USE = "hanim_vl3"

HAnimHumanoid44.joints.append(HAnimJoint1667)
HAnimJoint1668 = x3d.HAnimJoint()
HAnimJoint1668.USE = "hanim_vl2"

HAnimHumanoid44.joints.append(HAnimJoint1668)
HAnimJoint1669 = x3d.HAnimJoint()
HAnimJoint1669.USE = "hanim_vl1"

HAnimHumanoid44.joints.append(HAnimJoint1669)
HAnimJoint1670 = x3d.HAnimJoint()
HAnimJoint1670.USE = "hanim_vt12"

HAnimHumanoid44.joints.append(HAnimJoint1670)
HAnimJoint1671 = x3d.HAnimJoint()
HAnimJoint1671.USE = "hanim_vt11"

HAnimHumanoid44.joints.append(HAnimJoint1671)
HAnimJoint1672 = x3d.HAnimJoint()
HAnimJoint1672.USE = "hanim_vt10"

HAnimHumanoid44.joints.append(HAnimJoint1672)
HAnimJoint1673 = x3d.HAnimJoint()
HAnimJoint1673.USE = "hanim_vt9"

HAnimHumanoid44.joints.append(HAnimJoint1673)
HAnimJoint1674 = x3d.HAnimJoint()
HAnimJoint1674.USE = "hanim_vt8"

HAnimHumanoid44.joints.append(HAnimJoint1674)
HAnimJoint1675 = x3d.HAnimJoint()
HAnimJoint1675.USE = "hanim_vt7"

HAnimHumanoid44.joints.append(HAnimJoint1675)
HAnimJoint1676 = x3d.HAnimJoint()
HAnimJoint1676.USE = "hanim_vt6"

HAnimHumanoid44.joints.append(HAnimJoint1676)
HAnimJoint1677 = x3d.HAnimJoint()
HAnimJoint1677.USE = "hanim_vt5"

HAnimHumanoid44.joints.append(HAnimJoint1677)
HAnimJoint1678 = x3d.HAnimJoint()
HAnimJoint1678.USE = "hanim_vt4"

HAnimHumanoid44.joints.append(HAnimJoint1678)
HAnimJoint1679 = x3d.HAnimJoint()
HAnimJoint1679.USE = "hanim_vt3"

HAnimHumanoid44.joints.append(HAnimJoint1679)
HAnimJoint1680 = x3d.HAnimJoint()
HAnimJoint1680.USE = "hanim_vt2"

HAnimHumanoid44.joints.append(HAnimJoint1680)
HAnimJoint1681 = x3d.HAnimJoint()
HAnimJoint1681.USE = "hanim_vt1"

HAnimHumanoid44.joints.append(HAnimJoint1681)
HAnimJoint1682 = x3d.HAnimJoint()
HAnimJoint1682.USE = "hanim_vc7"

HAnimHumanoid44.joints.append(HAnimJoint1682)
HAnimJoint1683 = x3d.HAnimJoint()
HAnimJoint1683.USE = "hanim_vc6"

HAnimHumanoid44.joints.append(HAnimJoint1683)
HAnimJoint1684 = x3d.HAnimJoint()
HAnimJoint1684.USE = "hanim_vc5"

HAnimHumanoid44.joints.append(HAnimJoint1684)
HAnimJoint1685 = x3d.HAnimJoint()
HAnimJoint1685.USE = "hanim_vc4"

HAnimHumanoid44.joints.append(HAnimJoint1685)
HAnimJoint1686 = x3d.HAnimJoint()
HAnimJoint1686.USE = "hanim_vc3"

HAnimHumanoid44.joints.append(HAnimJoint1686)
HAnimJoint1687 = x3d.HAnimJoint()
HAnimJoint1687.USE = "hanim_vc2"

HAnimHumanoid44.joints.append(HAnimJoint1687)
HAnimJoint1688 = x3d.HAnimJoint()
HAnimJoint1688.USE = "hanim_vc1"

HAnimHumanoid44.joints.append(HAnimJoint1688)
HAnimJoint1689 = x3d.HAnimJoint()
HAnimJoint1689.USE = "hanim_skullbase"

HAnimHumanoid44.joints.append(HAnimJoint1689)
HAnimJoint1690 = x3d.HAnimJoint()
HAnimJoint1690.USE = "hanim_temporomandibular"

HAnimHumanoid44.joints.append(HAnimJoint1690)
HAnimJoint1691 = x3d.HAnimJoint()
HAnimJoint1691.USE = "hanim_l_acromioclavicular"

HAnimHumanoid44.joints.append(HAnimJoint1691)
HAnimJoint1692 = x3d.HAnimJoint()
HAnimJoint1692.USE = "hanim_r_acromioclavicular"

HAnimHumanoid44.joints.append(HAnimJoint1692)
HAnimJoint1693 = x3d.HAnimJoint()
HAnimJoint1693.USE = "hanim_l_ankle"

HAnimHumanoid44.joints.append(HAnimJoint1693)
HAnimJoint1694 = x3d.HAnimJoint()
HAnimJoint1694.USE = "hanim_r_ankle"

HAnimHumanoid44.joints.append(HAnimJoint1694)
HAnimJoint1695 = x3d.HAnimJoint()
HAnimJoint1695.USE = "hanim_l_elbow"

HAnimHumanoid44.joints.append(HAnimJoint1695)
HAnimJoint1696 = x3d.HAnimJoint()
HAnimJoint1696.USE = "hanim_r_elbow"

HAnimHumanoid44.joints.append(HAnimJoint1696)
HAnimJoint1697 = x3d.HAnimJoint()
HAnimJoint1697.USE = "hanim_l_eyeball_joint"

HAnimHumanoid44.joints.append(HAnimJoint1697)
HAnimJoint1698 = x3d.HAnimJoint()
HAnimJoint1698.USE = "hanim_r_eyeball_joint"

HAnimHumanoid44.joints.append(HAnimJoint1698)
HAnimJoint1699 = x3d.HAnimJoint()
HAnimJoint1699.USE = "hanim_l_eyebrow_joint"

HAnimHumanoid44.joints.append(HAnimJoint1699)
HAnimJoint1700 = x3d.HAnimJoint()
HAnimJoint1700.USE = "hanim_r_eyebrow_joint"

HAnimHumanoid44.joints.append(HAnimJoint1700)
HAnimJoint1701 = x3d.HAnimJoint()
HAnimJoint1701.USE = "hanim_l_eyelid_joint"

HAnimHumanoid44.joints.append(HAnimJoint1701)
HAnimJoint1702 = x3d.HAnimJoint()
HAnimJoint1702.USE = "hanim_r_eyelid_joint"

HAnimHumanoid44.joints.append(HAnimJoint1702)
HAnimJoint1703 = x3d.HAnimJoint()
HAnimJoint1703.USE = "hanim_l_hip"

HAnimHumanoid44.joints.append(HAnimJoint1703)
HAnimJoint1704 = x3d.HAnimJoint()
HAnimJoint1704.USE = "hanim_r_hip"

HAnimHumanoid44.joints.append(HAnimJoint1704)
HAnimJoint1705 = x3d.HAnimJoint()
HAnimJoint1705.USE = "hanim_l_index0"

HAnimHumanoid44.joints.append(HAnimJoint1705)
HAnimJoint1706 = x3d.HAnimJoint()
HAnimJoint1706.USE = "hanim_r_index0"

HAnimHumanoid44.joints.append(HAnimJoint1706)
HAnimJoint1707 = x3d.HAnimJoint()
HAnimJoint1707.USE = "hanim_l_index1"

HAnimHumanoid44.joints.append(HAnimJoint1707)
HAnimJoint1708 = x3d.HAnimJoint()
HAnimJoint1708.USE = "hanim_r_index1"

HAnimHumanoid44.joints.append(HAnimJoint1708)
HAnimJoint1709 = x3d.HAnimJoint()
HAnimJoint1709.USE = "hanim_l_index2"

HAnimHumanoid44.joints.append(HAnimJoint1709)
HAnimJoint1710 = x3d.HAnimJoint()
HAnimJoint1710.USE = "hanim_r_index2"

HAnimHumanoid44.joints.append(HAnimJoint1710)
HAnimJoint1711 = x3d.HAnimJoint()
HAnimJoint1711.USE = "hanim_l_index3"

HAnimHumanoid44.joints.append(HAnimJoint1711)
HAnimJoint1712 = x3d.HAnimJoint()
HAnimJoint1712.USE = "hanim_r_index3"

HAnimHumanoid44.joints.append(HAnimJoint1712)
HAnimJoint1713 = x3d.HAnimJoint()
HAnimJoint1713.USE = "hanim_l_knee"

HAnimHumanoid44.joints.append(HAnimJoint1713)
HAnimJoint1714 = x3d.HAnimJoint()
HAnimJoint1714.USE = "hanim_r_knee"

HAnimHumanoid44.joints.append(HAnimJoint1714)
HAnimJoint1715 = x3d.HAnimJoint()
HAnimJoint1715.USE = "hanim_l_metatarsal"

HAnimHumanoid44.joints.append(HAnimJoint1715)
HAnimJoint1716 = x3d.HAnimJoint()
HAnimJoint1716.USE = "hanim_r_metatarsal"

HAnimHumanoid44.joints.append(HAnimJoint1716)
HAnimJoint1717 = x3d.HAnimJoint()
HAnimJoint1717.USE = "hanim_l_middle0"

HAnimHumanoid44.joints.append(HAnimJoint1717)
HAnimJoint1718 = x3d.HAnimJoint()
HAnimJoint1718.USE = "hanim_r_middle0"

HAnimHumanoid44.joints.append(HAnimJoint1718)
HAnimJoint1719 = x3d.HAnimJoint()
HAnimJoint1719.USE = "hanim_l_middle1"

HAnimHumanoid44.joints.append(HAnimJoint1719)
HAnimJoint1720 = x3d.HAnimJoint()
HAnimJoint1720.USE = "hanim_r_middle1"

HAnimHumanoid44.joints.append(HAnimJoint1720)
HAnimJoint1721 = x3d.HAnimJoint()
HAnimJoint1721.USE = "hanim_l_middle2"

HAnimHumanoid44.joints.append(HAnimJoint1721)
HAnimJoint1722 = x3d.HAnimJoint()
HAnimJoint1722.USE = "hanim_r_middle2"

HAnimHumanoid44.joints.append(HAnimJoint1722)
HAnimJoint1723 = x3d.HAnimJoint()
HAnimJoint1723.USE = "hanim_l_middle3"

HAnimHumanoid44.joints.append(HAnimJoint1723)
HAnimJoint1724 = x3d.HAnimJoint()
HAnimJoint1724.USE = "hanim_r_middle3"

HAnimHumanoid44.joints.append(HAnimJoint1724)
HAnimJoint1725 = x3d.HAnimJoint()
HAnimJoint1725.USE = "hanim_l_midtarsal"

HAnimHumanoid44.joints.append(HAnimJoint1725)
HAnimJoint1726 = x3d.HAnimJoint()
HAnimJoint1726.USE = "hanim_r_midtarsal"

HAnimHumanoid44.joints.append(HAnimJoint1726)
HAnimJoint1727 = x3d.HAnimJoint()
HAnimJoint1727.USE = "hanim_l_pinky0"

HAnimHumanoid44.joints.append(HAnimJoint1727)
HAnimJoint1728 = x3d.HAnimJoint()
HAnimJoint1728.USE = "hanim_r_pinky0"

HAnimHumanoid44.joints.append(HAnimJoint1728)
HAnimJoint1729 = x3d.HAnimJoint()
HAnimJoint1729.USE = "hanim_l_pinky1"

HAnimHumanoid44.joints.append(HAnimJoint1729)
HAnimJoint1730 = x3d.HAnimJoint()
HAnimJoint1730.USE = "hanim_r_pinky1"

HAnimHumanoid44.joints.append(HAnimJoint1730)
HAnimJoint1731 = x3d.HAnimJoint()
HAnimJoint1731.USE = "hanim_l_pinky2"

HAnimHumanoid44.joints.append(HAnimJoint1731)
HAnimJoint1732 = x3d.HAnimJoint()
HAnimJoint1732.USE = "hanim_r_pinky2"

HAnimHumanoid44.joints.append(HAnimJoint1732)
HAnimJoint1733 = x3d.HAnimJoint()
HAnimJoint1733.USE = "hanim_l_pinky3"

HAnimHumanoid44.joints.append(HAnimJoint1733)
HAnimJoint1734 = x3d.HAnimJoint()
HAnimJoint1734.USE = "hanim_r_pinky3"

HAnimHumanoid44.joints.append(HAnimJoint1734)
HAnimJoint1735 = x3d.HAnimJoint()
HAnimJoint1735.USE = "hanim_l_ring0"

HAnimHumanoid44.joints.append(HAnimJoint1735)
HAnimJoint1736 = x3d.HAnimJoint()
HAnimJoint1736.USE = "hanim_r_ring0"

HAnimHumanoid44.joints.append(HAnimJoint1736)
HAnimJoint1737 = x3d.HAnimJoint()
HAnimJoint1737.USE = "hanim_l_ring1"

HAnimHumanoid44.joints.append(HAnimJoint1737)
HAnimJoint1738 = x3d.HAnimJoint()
HAnimJoint1738.USE = "hanim_r_ring1"

HAnimHumanoid44.joints.append(HAnimJoint1738)
HAnimJoint1739 = x3d.HAnimJoint()
HAnimJoint1739.USE = "hanim_l_ring2"

HAnimHumanoid44.joints.append(HAnimJoint1739)
HAnimJoint1740 = x3d.HAnimJoint()
HAnimJoint1740.USE = "hanim_r_ring2"

HAnimHumanoid44.joints.append(HAnimJoint1740)
HAnimJoint1741 = x3d.HAnimJoint()
HAnimJoint1741.USE = "hanim_l_ring3"

HAnimHumanoid44.joints.append(HAnimJoint1741)
HAnimJoint1742 = x3d.HAnimJoint()
HAnimJoint1742.USE = "hanim_r_ring3"

HAnimHumanoid44.joints.append(HAnimJoint1742)
HAnimJoint1743 = x3d.HAnimJoint()
HAnimJoint1743.USE = "hanim_l_shoulder"

HAnimHumanoid44.joints.append(HAnimJoint1743)
HAnimJoint1744 = x3d.HAnimJoint()
HAnimJoint1744.USE = "hanim_r_shoulder"

HAnimHumanoid44.joints.append(HAnimJoint1744)
HAnimJoint1745 = x3d.HAnimJoint()
HAnimJoint1745.USE = "hanim_l_sternoclavicular"

HAnimHumanoid44.joints.append(HAnimJoint1745)
HAnimJoint1746 = x3d.HAnimJoint()
HAnimJoint1746.USE = "hanim_r_sternoclavicular"

HAnimHumanoid44.joints.append(HAnimJoint1746)
HAnimJoint1747 = x3d.HAnimJoint()
HAnimJoint1747.USE = "hanim_l_subtalar"

HAnimHumanoid44.joints.append(HAnimJoint1747)
HAnimJoint1748 = x3d.HAnimJoint()
HAnimJoint1748.USE = "hanim_r_subtalar"

HAnimHumanoid44.joints.append(HAnimJoint1748)
HAnimJoint1749 = x3d.HAnimJoint()
HAnimJoint1749.USE = "hanim_l_thumb1"

HAnimHumanoid44.joints.append(HAnimJoint1749)
HAnimJoint1750 = x3d.HAnimJoint()
HAnimJoint1750.USE = "hanim_r_thumb1"

HAnimHumanoid44.joints.append(HAnimJoint1750)
HAnimJoint1751 = x3d.HAnimJoint()
HAnimJoint1751.USE = "hanim_l_thumb2"

HAnimHumanoid44.joints.append(HAnimJoint1751)
HAnimJoint1752 = x3d.HAnimJoint()
HAnimJoint1752.USE = "hanim_r_thumb2"

HAnimHumanoid44.joints.append(HAnimJoint1752)
HAnimJoint1753 = x3d.HAnimJoint()
HAnimJoint1753.USE = "hanim_l_thumb3"

HAnimHumanoid44.joints.append(HAnimJoint1753)
HAnimJoint1754 = x3d.HAnimJoint()
HAnimJoint1754.USE = "hanim_r_thumb3"

HAnimHumanoid44.joints.append(HAnimJoint1754)
HAnimJoint1755 = x3d.HAnimJoint()
HAnimJoint1755.USE = "hanim_l_wrist"

HAnimHumanoid44.joints.append(HAnimJoint1755)
HAnimJoint1756 = x3d.HAnimJoint()
HAnimJoint1756.USE = "hanim_r_wrist"

HAnimHumanoid44.joints.append(HAnimJoint1756)
HAnimSegment1757 = x3d.HAnimSegment()
HAnimSegment1757.USE = "hanim_pelvis"

HAnimHumanoid44.segments.append(HAnimSegment1757)
HAnimSegment1758 = x3d.HAnimSegment()
HAnimSegment1758.USE = "hanim_skull"

HAnimHumanoid44.segments.append(HAnimSegment1758)
HAnimSegment1759 = x3d.HAnimSegment()
HAnimSegment1759.USE = "hanim_jaw"

HAnimHumanoid44.segments.append(HAnimSegment1759)
HAnimSegment1760 = x3d.HAnimSegment()
HAnimSegment1760.USE = "hanim_c1"

HAnimHumanoid44.segments.append(HAnimSegment1760)
HAnimSegment1761 = x3d.HAnimSegment()
HAnimSegment1761.USE = "hanim_c2"

HAnimHumanoid44.segments.append(HAnimSegment1761)
HAnimSegment1762 = x3d.HAnimSegment()
HAnimSegment1762.USE = "hanim_c3"

HAnimHumanoid44.segments.append(HAnimSegment1762)
HAnimSegment1763 = x3d.HAnimSegment()
HAnimSegment1763.USE = "hanim_c4"

HAnimHumanoid44.segments.append(HAnimSegment1763)
HAnimSegment1764 = x3d.HAnimSegment()
HAnimSegment1764.USE = "hanim_c5"

HAnimHumanoid44.segments.append(HAnimSegment1764)
HAnimSegment1765 = x3d.HAnimSegment()
HAnimSegment1765.USE = "hanim_c6"

HAnimHumanoid44.segments.append(HAnimSegment1765)
HAnimSegment1766 = x3d.HAnimSegment()
HAnimSegment1766.USE = "hanim_c7"

HAnimHumanoid44.segments.append(HAnimSegment1766)
HAnimSegment1767 = x3d.HAnimSegment()
HAnimSegment1767.USE = "hanim_t1"

HAnimHumanoid44.segments.append(HAnimSegment1767)
HAnimSegment1768 = x3d.HAnimSegment()
HAnimSegment1768.USE = "hanim_t2"

HAnimHumanoid44.segments.append(HAnimSegment1768)
HAnimSegment1769 = x3d.HAnimSegment()
HAnimSegment1769.USE = "hanim_t3"

HAnimHumanoid44.segments.append(HAnimSegment1769)
HAnimSegment1770 = x3d.HAnimSegment()
HAnimSegment1770.USE = "hanim_t4"

HAnimHumanoid44.segments.append(HAnimSegment1770)
HAnimSegment1771 = x3d.HAnimSegment()
HAnimSegment1771.USE = "hanim_t5"

HAnimHumanoid44.segments.append(HAnimSegment1771)
HAnimSegment1772 = x3d.HAnimSegment()
HAnimSegment1772.USE = "hanim_t6"

HAnimHumanoid44.segments.append(HAnimSegment1772)
HAnimSegment1773 = x3d.HAnimSegment()
HAnimSegment1773.USE = "hanim_t7"

HAnimHumanoid44.segments.append(HAnimSegment1773)
HAnimSegment1774 = x3d.HAnimSegment()
HAnimSegment1774.USE = "hanim_t8"

HAnimHumanoid44.segments.append(HAnimSegment1774)
HAnimSegment1775 = x3d.HAnimSegment()
HAnimSegment1775.USE = "hanim_t9"

HAnimHumanoid44.segments.append(HAnimSegment1775)
HAnimSegment1776 = x3d.HAnimSegment()
HAnimSegment1776.USE = "hanim_t10"

HAnimHumanoid44.segments.append(HAnimSegment1776)
HAnimSegment1777 = x3d.HAnimSegment()
HAnimSegment1777.USE = "hanim_t11"

HAnimHumanoid44.segments.append(HAnimSegment1777)
HAnimSegment1778 = x3d.HAnimSegment()
HAnimSegment1778.USE = "hanim_t12"

HAnimHumanoid44.segments.append(HAnimSegment1778)
HAnimSegment1779 = x3d.HAnimSegment()
HAnimSegment1779.USE = "hanim_l1"

HAnimHumanoid44.segments.append(HAnimSegment1779)
HAnimSegment1780 = x3d.HAnimSegment()
HAnimSegment1780.USE = "hanim_l2"

HAnimHumanoid44.segments.append(HAnimSegment1780)
HAnimSegment1781 = x3d.HAnimSegment()
HAnimSegment1781.USE = "hanim_l3"

HAnimHumanoid44.segments.append(HAnimSegment1781)
HAnimSegment1782 = x3d.HAnimSegment()
HAnimSegment1782.USE = "hanim_l4"

HAnimHumanoid44.segments.append(HAnimSegment1782)
HAnimSegment1783 = x3d.HAnimSegment()
HAnimSegment1783.USE = "hanim_l5"

HAnimHumanoid44.segments.append(HAnimSegment1783)
HAnimSegment1784 = x3d.HAnimSegment()
HAnimSegment1784.USE = "hanim_sacrum"

HAnimHumanoid44.segments.append(HAnimSegment1784)
HAnimSegment1785 = x3d.HAnimSegment()
HAnimSegment1785.USE = "hanim_l_calf"

HAnimHumanoid44.segments.append(HAnimSegment1785)
HAnimSegment1786 = x3d.HAnimSegment()
HAnimSegment1786.USE = "hanim_r_calf"

HAnimHumanoid44.segments.append(HAnimSegment1786)
HAnimSegment1787 = x3d.HAnimSegment()
HAnimSegment1787.USE = "hanim_l_clavicle"

HAnimHumanoid44.segments.append(HAnimSegment1787)
HAnimSegment1788 = x3d.HAnimSegment()
HAnimSegment1788.USE = "hanim_r_clavicle"

HAnimHumanoid44.segments.append(HAnimSegment1788)
HAnimSegment1789 = x3d.HAnimSegment()
HAnimSegment1789.USE = "hanim_l_eyeball"

HAnimHumanoid44.segments.append(HAnimSegment1789)
HAnimSegment1790 = x3d.HAnimSegment()
HAnimSegment1790.USE = "hanim_r_eyeball"

HAnimHumanoid44.segments.append(HAnimSegment1790)
HAnimSegment1791 = x3d.HAnimSegment()
HAnimSegment1791.USE = "hanim_l_eyebrow"

HAnimHumanoid44.segments.append(HAnimSegment1791)
HAnimSegment1792 = x3d.HAnimSegment()
HAnimSegment1792.USE = "hanim_r_eyebrow"

HAnimHumanoid44.segments.append(HAnimSegment1792)
HAnimSegment1793 = x3d.HAnimSegment()
HAnimSegment1793.USE = "hanim_l_eyelid"

HAnimHumanoid44.segments.append(HAnimSegment1793)
HAnimSegment1794 = x3d.HAnimSegment()
HAnimSegment1794.USE = "hanim_r_eyelid"

HAnimHumanoid44.segments.append(HAnimSegment1794)
HAnimSegment1795 = x3d.HAnimSegment()
HAnimSegment1795.USE = "hanim_l_forearm"

HAnimHumanoid44.segments.append(HAnimSegment1795)
HAnimSegment1796 = x3d.HAnimSegment()
HAnimSegment1796.USE = "hanim_r_forearm"

HAnimHumanoid44.segments.append(HAnimSegment1796)
HAnimSegment1797 = x3d.HAnimSegment()
HAnimSegment1797.USE = "hanim_l_forefoot"

HAnimHumanoid44.segments.append(HAnimSegment1797)
HAnimSegment1798 = x3d.HAnimSegment()
HAnimSegment1798.USE = "hanim_r_forefoot"

HAnimHumanoid44.segments.append(HAnimSegment1798)
HAnimSegment1799 = x3d.HAnimSegment()
HAnimSegment1799.USE = "hanim_l_hand"

HAnimHumanoid44.segments.append(HAnimSegment1799)
HAnimSegment1800 = x3d.HAnimSegment()
HAnimSegment1800.USE = "hanim_r_hand"

HAnimHumanoid44.segments.append(HAnimSegment1800)
HAnimSegment1801 = x3d.HAnimSegment()
HAnimSegment1801.USE = "hanim_l_hindfoot"

HAnimHumanoid44.segments.append(HAnimSegment1801)
HAnimSegment1802 = x3d.HAnimSegment()
HAnimSegment1802.USE = "hanim_r_hindfoot"

HAnimHumanoid44.segments.append(HAnimSegment1802)
HAnimSegment1803 = x3d.HAnimSegment()
HAnimSegment1803.USE = "hanim_l_index_distal"

HAnimHumanoid44.segments.append(HAnimSegment1803)
HAnimSegment1804 = x3d.HAnimSegment()
HAnimSegment1804.USE = "hanim_r_index_distal"

HAnimHumanoid44.segments.append(HAnimSegment1804)
HAnimSegment1805 = x3d.HAnimSegment()
HAnimSegment1805.USE = "hanim_l_index_metacarpal"

HAnimHumanoid44.segments.append(HAnimSegment1805)
HAnimSegment1806 = x3d.HAnimSegment()
HAnimSegment1806.USE = "hanim_r_index_metacarpal"

HAnimHumanoid44.segments.append(HAnimSegment1806)
HAnimSegment1807 = x3d.HAnimSegment()
HAnimSegment1807.USE = "hanim_l_index_middle"

HAnimHumanoid44.segments.append(HAnimSegment1807)
HAnimSegment1808 = x3d.HAnimSegment()
HAnimSegment1808.USE = "hanim_r_index_middle"

HAnimHumanoid44.segments.append(HAnimSegment1808)
HAnimSegment1809 = x3d.HAnimSegment()
HAnimSegment1809.USE = "hanim_l_index_proximal"

HAnimHumanoid44.segments.append(HAnimSegment1809)
HAnimSegment1810 = x3d.HAnimSegment()
HAnimSegment1810.USE = "hanim_r_index_proximal"

HAnimHumanoid44.segments.append(HAnimSegment1810)
HAnimSegment1811 = x3d.HAnimSegment()
HAnimSegment1811.USE = "hanim_l_middistal"

HAnimHumanoid44.segments.append(HAnimSegment1811)
HAnimSegment1812 = x3d.HAnimSegment()
HAnimSegment1812.USE = "hanim_r_middistal"

HAnimHumanoid44.segments.append(HAnimSegment1812)
HAnimSegment1813 = x3d.HAnimSegment()
HAnimSegment1813.USE = "hanim_l_middle_distal"

HAnimHumanoid44.segments.append(HAnimSegment1813)
HAnimSegment1814 = x3d.HAnimSegment()
HAnimSegment1814.USE = "hanim_r_middle_distal"

HAnimHumanoid44.segments.append(HAnimSegment1814)
HAnimSegment1815 = x3d.HAnimSegment()
HAnimSegment1815.USE = "hanim_l_middle_metacarpal"

HAnimHumanoid44.segments.append(HAnimSegment1815)
HAnimSegment1816 = x3d.HAnimSegment()
HAnimSegment1816.USE = "hanim_r_middle_metacarpal"

HAnimHumanoid44.segments.append(HAnimSegment1816)
HAnimSegment1817 = x3d.HAnimSegment()
HAnimSegment1817.USE = "hanim_l_middle_middle"

HAnimHumanoid44.segments.append(HAnimSegment1817)
HAnimSegment1818 = x3d.HAnimSegment()
HAnimSegment1818.USE = "hanim_r_middle_middle"

HAnimHumanoid44.segments.append(HAnimSegment1818)
HAnimSegment1819 = x3d.HAnimSegment()
HAnimSegment1819.USE = "hanim_l_middle_proximal"

HAnimHumanoid44.segments.append(HAnimSegment1819)
HAnimSegment1820 = x3d.HAnimSegment()
HAnimSegment1820.USE = "hanim_r_middle_proximal"

HAnimHumanoid44.segments.append(HAnimSegment1820)
HAnimSegment1821 = x3d.HAnimSegment()
HAnimSegment1821.USE = "hanim_l_midproximal"

HAnimHumanoid44.segments.append(HAnimSegment1821)
HAnimSegment1822 = x3d.HAnimSegment()
HAnimSegment1822.USE = "hanim_r_midproximal"

HAnimHumanoid44.segments.append(HAnimSegment1822)
HAnimSegment1823 = x3d.HAnimSegment()
HAnimSegment1823.USE = "hanim_l_pinky_distal"

HAnimHumanoid44.segments.append(HAnimSegment1823)
HAnimSegment1824 = x3d.HAnimSegment()
HAnimSegment1824.USE = "hanim_r_pinky_distal"

HAnimHumanoid44.segments.append(HAnimSegment1824)
HAnimSegment1825 = x3d.HAnimSegment()
HAnimSegment1825.USE = "hanim_l_pinky_metacarpal"

HAnimHumanoid44.segments.append(HAnimSegment1825)
HAnimSegment1826 = x3d.HAnimSegment()
HAnimSegment1826.USE = "hanim_r_pinky_metacarpal"

HAnimHumanoid44.segments.append(HAnimSegment1826)
HAnimSegment1827 = x3d.HAnimSegment()
HAnimSegment1827.USE = "hanim_l_pinky_middle"

HAnimHumanoid44.segments.append(HAnimSegment1827)
HAnimSegment1828 = x3d.HAnimSegment()
HAnimSegment1828.USE = "hanim_r_pinky_middle"

HAnimHumanoid44.segments.append(HAnimSegment1828)
HAnimSegment1829 = x3d.HAnimSegment()
HAnimSegment1829.USE = "hanim_l_pinky_proximal"

HAnimHumanoid44.segments.append(HAnimSegment1829)
HAnimSegment1830 = x3d.HAnimSegment()
HAnimSegment1830.USE = "hanim_r_pinky_proximal"

HAnimHumanoid44.segments.append(HAnimSegment1830)
HAnimSegment1831 = x3d.HAnimSegment()
HAnimSegment1831.USE = "hanim_l_ring_distal"

HAnimHumanoid44.segments.append(HAnimSegment1831)
HAnimSegment1832 = x3d.HAnimSegment()
HAnimSegment1832.USE = "hanim_r_ring_distal"

HAnimHumanoid44.segments.append(HAnimSegment1832)
HAnimSegment1833 = x3d.HAnimSegment()
HAnimSegment1833.USE = "hanim_l_ring_metacarpal"

HAnimHumanoid44.segments.append(HAnimSegment1833)
HAnimSegment1834 = x3d.HAnimSegment()
HAnimSegment1834.USE = "hanim_r_ring_metacarpal"

HAnimHumanoid44.segments.append(HAnimSegment1834)
HAnimSegment1835 = x3d.HAnimSegment()
HAnimSegment1835.USE = "hanim_l_ring_middle"

HAnimHumanoid44.segments.append(HAnimSegment1835)
HAnimSegment1836 = x3d.HAnimSegment()
HAnimSegment1836.USE = "hanim_r_ring_middle"

HAnimHumanoid44.segments.append(HAnimSegment1836)
HAnimSegment1837 = x3d.HAnimSegment()
HAnimSegment1837.USE = "hanim_l_ring_proximal"

HAnimHumanoid44.segments.append(HAnimSegment1837)
HAnimSegment1838 = x3d.HAnimSegment()
HAnimSegment1838.USE = "hanim_r_ring_proximal"

HAnimHumanoid44.segments.append(HAnimSegment1838)
HAnimSegment1839 = x3d.HAnimSegment()
HAnimSegment1839.USE = "hanim_l_scapula"

HAnimHumanoid44.segments.append(HAnimSegment1839)
HAnimSegment1840 = x3d.HAnimSegment()
HAnimSegment1840.USE = "hanim_r_scapula"

HAnimHumanoid44.segments.append(HAnimSegment1840)
HAnimSegment1841 = x3d.HAnimSegment()
HAnimSegment1841.USE = "hanim_l_thigh"

HAnimHumanoid44.segments.append(HAnimSegment1841)
HAnimSegment1842 = x3d.HAnimSegment()
HAnimSegment1842.USE = "hanim_r_thigh"

HAnimHumanoid44.segments.append(HAnimSegment1842)
HAnimSegment1843 = x3d.HAnimSegment()
HAnimSegment1843.USE = "hanim_l_thumb_distal"

HAnimHumanoid44.segments.append(HAnimSegment1843)
HAnimSegment1844 = x3d.HAnimSegment()
HAnimSegment1844.USE = "hanim_r_thumb_distal"

HAnimHumanoid44.segments.append(HAnimSegment1844)
HAnimSegment1845 = x3d.HAnimSegment()
HAnimSegment1845.USE = "hanim_l_thumb_metacarpal"

HAnimHumanoid44.segments.append(HAnimSegment1845)
HAnimSegment1846 = x3d.HAnimSegment()
HAnimSegment1846.USE = "hanim_r_thumb_metacarpal"

HAnimHumanoid44.segments.append(HAnimSegment1846)
HAnimSegment1847 = x3d.HAnimSegment()
HAnimSegment1847.USE = "hanim_l_thumb_proximal"

HAnimHumanoid44.segments.append(HAnimSegment1847)
HAnimSegment1848 = x3d.HAnimSegment()
HAnimSegment1848.USE = "hanim_r_thumb_proximal"

HAnimHumanoid44.segments.append(HAnimSegment1848)
HAnimSegment1849 = x3d.HAnimSegment()
HAnimSegment1849.USE = "hanim_l_upperarm"

HAnimHumanoid44.segments.append(HAnimSegment1849)
HAnimSegment1850 = x3d.HAnimSegment()
HAnimSegment1850.USE = "hanim_r_upperarm"

HAnimHumanoid44.segments.append(HAnimSegment1850)
HAnimSite1851 = x3d.HAnimSite()
HAnimSite1851.USE = "hanim_crotch_pt"

HAnimHumanoid44.sites.append(HAnimSite1851)
HAnimSite1852 = x3d.HAnimSite()
HAnimSite1852.USE = "hanim_skull_tip"

HAnimHumanoid44.sites.append(HAnimSite1852)
HAnimSite1853 = x3d.HAnimSite()
HAnimSite1853.USE = "hanim_sellion_pt"

HAnimHumanoid44.sites.append(HAnimSite1853)
HAnimSite1854 = x3d.HAnimSite()
HAnimSite1854.USE = "hanim_supramenton_pt"

HAnimHumanoid44.sites.append(HAnimSite1854)
HAnimSite1855 = x3d.HAnimSite()
HAnimSite1855.USE = "hanim_nuchale_pt"

HAnimHumanoid44.sites.append(HAnimSite1855)
HAnimSite1856 = x3d.HAnimSite()
HAnimSite1856.USE = "hanim_suprasternale_pt"

HAnimHumanoid44.sites.append(HAnimSite1856)
HAnimSite1857 = x3d.HAnimSite()
HAnimSite1857.USE = "hanim_cervicale_pt"

HAnimHumanoid44.sites.append(HAnimSite1857)
HAnimSite1858 = x3d.HAnimSite()
HAnimSite1858.USE = "hanim_substernale_pt"

HAnimHumanoid44.sites.append(HAnimSite1858)
HAnimSite1859 = x3d.HAnimSite()
HAnimSite1859.USE = "hanim_rib10_midspine_pt"

HAnimHumanoid44.sites.append(HAnimSite1859)
HAnimSite1860 = x3d.HAnimSite()
HAnimSite1860.USE = "hanim_waist_preferred_post_pt"

HAnimHumanoid44.sites.append(HAnimSite1860)
HAnimSite1861 = x3d.HAnimSite()
HAnimSite1861.USE = "hanim_navel_pt"

HAnimHumanoid44.sites.append(HAnimSite1861)
HAnimSite1862 = x3d.HAnimSite()
HAnimSite1862.USE = "hanim_l_acromion_pt"

HAnimHumanoid44.sites.append(HAnimSite1862)
HAnimSite1863 = x3d.HAnimSite()
HAnimSite1863.USE = "hanim_r_acromion_pt"

HAnimHumanoid44.sites.append(HAnimSite1863)
HAnimSite1864 = x3d.HAnimSite()
HAnimSite1864.USE = "hanim_r_asis_pt"

HAnimHumanoid44.sites.append(HAnimSite1864)
HAnimSite1865 = x3d.HAnimSite()
HAnimSite1865.USE = "hanim_l_asis_pt"

HAnimHumanoid44.sites.append(HAnimSite1865)
HAnimSite1866 = x3d.HAnimSite()
HAnimSite1866.USE = "hanim_l_axilla_ant_pt"

HAnimHumanoid44.sites.append(HAnimSite1866)
HAnimSite1867 = x3d.HAnimSite()
HAnimSite1867.USE = "hanim_r_axilla_ant_pt"

HAnimHumanoid44.sites.append(HAnimSite1867)
HAnimSite1868 = x3d.HAnimSite()
HAnimSite1868.USE = "hanim_l_axilla_post_pt"

HAnimHumanoid44.sites.append(HAnimSite1868)
HAnimSite1869 = x3d.HAnimSite()
HAnimSite1869.USE = "hanim_r_axilla_post_pt"

HAnimHumanoid44.sites.append(HAnimSite1869)
HAnimSite1870 = x3d.HAnimSite()
HAnimSite1870.USE = "hanim_l_calcaneous_post_pt"

HAnimHumanoid44.sites.append(HAnimSite1870)
HAnimSite1871 = x3d.HAnimSite()
HAnimSite1871.USE = "hanim_r_calcaneous_post_pt"

HAnimHumanoid44.sites.append(HAnimSite1871)
HAnimSite1872 = x3d.HAnimSite()
HAnimSite1872.USE = "hanim_l_clavicale_pt"

HAnimHumanoid44.sites.append(HAnimSite1872)
HAnimSite1873 = x3d.HAnimSite()
HAnimSite1873.USE = "hanim_r_clavicale_pt"

HAnimHumanoid44.sites.append(HAnimSite1873)
HAnimSite1874 = x3d.HAnimSite()
HAnimSite1874.USE = "hanim_l_dactylion_pt"

HAnimHumanoid44.sites.append(HAnimSite1874)
HAnimSite1875 = x3d.HAnimSite()
HAnimSite1875.USE = "hanim_r_dactylion_pt"

HAnimHumanoid44.sites.append(HAnimSite1875)
HAnimSite1876 = x3d.HAnimSite()
HAnimSite1876.USE = "hanim_l_digit2_pt"

HAnimHumanoid44.sites.append(HAnimSite1876)
HAnimSite1877 = x3d.HAnimSite()
HAnimSite1877.USE = "hanim_r_digit2_pt"

HAnimHumanoid44.sites.append(HAnimSite1877)
HAnimSite1878 = x3d.HAnimSite()
HAnimSite1878.USE = "hanim_l_femoral_lateral_epicn_pt"

HAnimHumanoid44.sites.append(HAnimSite1878)
HAnimSite1879 = x3d.HAnimSite()
HAnimSite1879.USE = "hanim_r_femoral_lateral_epicn_pt"

HAnimHumanoid44.sites.append(HAnimSite1879)
HAnimSite1880 = x3d.HAnimSite()
HAnimSite1880.USE = "hanim_l_femoral_medial_epicn_pt"

HAnimHumanoid44.sites.append(HAnimSite1880)
HAnimSite1881 = x3d.HAnimSite()
HAnimSite1881.USE = "hanim_r_femoral_medial_epicn_pt"

HAnimHumanoid44.sites.append(HAnimSite1881)
HAnimSite1882 = x3d.HAnimSite()
HAnimSite1882.USE = "hanim_l_forefoot_tip"

HAnimHumanoid44.sites.append(HAnimSite1882)
HAnimSite1883 = x3d.HAnimSite()
HAnimSite1883.USE = "hanim_r_forefoot_tip"

HAnimHumanoid44.sites.append(HAnimSite1883)
HAnimSite1884 = x3d.HAnimSite()
HAnimSite1884.USE = "hanim_r_gonion_pt"

HAnimHumanoid44.sites.append(HAnimSite1884)
HAnimSite1885 = x3d.HAnimSite()
HAnimSite1885.USE = "hanim_l_gonion_pt"

HAnimHumanoid44.sites.append(HAnimSite1885)
HAnimSite1886 = x3d.HAnimSite()
HAnimSite1886.USE = "hanim_l_humeral_lateral_epicn_pt"

HAnimHumanoid44.sites.append(HAnimSite1886)
HAnimSite1887 = x3d.HAnimSite()
HAnimSite1887.USE = "hanim_r_humeral_lateral_epicn_pt"

HAnimHumanoid44.sites.append(HAnimSite1887)
HAnimSite1888 = x3d.HAnimSite()
HAnimSite1888.USE = "hanim_l_humeral_medial_epicn_pt"

HAnimHumanoid44.sites.append(HAnimSite1888)
HAnimSite1889 = x3d.HAnimSite()
HAnimSite1889.USE = "hanim_r_humeral_medial_epicn_pt"

HAnimHumanoid44.sites.append(HAnimSite1889)
HAnimSite1890 = x3d.HAnimSite()
HAnimSite1890.USE = "hanim_r_iliocristale_pt"

HAnimHumanoid44.sites.append(HAnimSite1890)
HAnimSite1891 = x3d.HAnimSite()
HAnimSite1891.USE = "hanim_l_iliocristale_pt"

HAnimHumanoid44.sites.append(HAnimSite1891)
HAnimSite1892 = x3d.HAnimSite()
HAnimSite1892.USE = "hanim_l_index_distal_tip"

HAnimHumanoid44.sites.append(HAnimSite1892)
HAnimSite1893 = x3d.HAnimSite()
HAnimSite1893.USE = "hanim_r_index_distal_tip"

HAnimHumanoid44.sites.append(HAnimSite1893)
HAnimSite1894 = x3d.HAnimSite()
HAnimSite1894.USE = "hanim_r_infraorbitale_pt"

HAnimHumanoid44.sites.append(HAnimSite1894)
HAnimSite1895 = x3d.HAnimSite()
HAnimSite1895.USE = "hanim_l_infraorbitale_pt"

HAnimHumanoid44.sites.append(HAnimSite1895)
HAnimSite1896 = x3d.HAnimSite()
HAnimSite1896.USE = "hanim_l_knee_crease_pt"

HAnimHumanoid44.sites.append(HAnimSite1896)
HAnimSite1897 = x3d.HAnimSite()
HAnimSite1897.USE = "hanim_r_knee_crease_pt"

HAnimHumanoid44.sites.append(HAnimSite1897)
HAnimSite1898 = x3d.HAnimSite()
HAnimSite1898.USE = "hanim_l_lateral_malleolus_pt"

HAnimHumanoid44.sites.append(HAnimSite1898)
HAnimSite1899 = x3d.HAnimSite()
HAnimSite1899.USE = "hanim_r_lateral_malleolus_pt"

HAnimHumanoid44.sites.append(HAnimSite1899)
HAnimSite1900 = x3d.HAnimSite()
HAnimSite1900.USE = "hanim_l_medial_malleolus_pt"

HAnimHumanoid44.sites.append(HAnimSite1900)
HAnimSite1901 = x3d.HAnimSite()
HAnimSite1901.USE = "hanim_r_medial_malleolus_pt"

HAnimHumanoid44.sites.append(HAnimSite1901)
HAnimSite1902 = x3d.HAnimSite()
HAnimSite1902.USE = "hanim_l_metacarpal_pha2_pt"

HAnimHumanoid44.sites.append(HAnimSite1902)
HAnimSite1903 = x3d.HAnimSite()
HAnimSite1903.USE = "hanim_r_metacarpal_pha2_pt"

HAnimHumanoid44.sites.append(HAnimSite1903)
HAnimSite1904 = x3d.HAnimSite()
HAnimSite1904.USE = "hanim_l_metacarpal_pha5_pt"

HAnimHumanoid44.sites.append(HAnimSite1904)
HAnimSite1905 = x3d.HAnimSite()
HAnimSite1905.USE = "hanim_r_metacarpal_pha5_pt"

HAnimHumanoid44.sites.append(HAnimSite1905)
HAnimSite1906 = x3d.HAnimSite()
HAnimSite1906.USE = "hanim_l_metatarsal_pha1_pt"

HAnimHumanoid44.sites.append(HAnimSite1906)
HAnimSite1907 = x3d.HAnimSite()
HAnimSite1907.USE = "hanim_r_metatarsal_pha1_pt"

HAnimHumanoid44.sites.append(HAnimSite1907)
HAnimSite1908 = x3d.HAnimSite()
HAnimSite1908.USE = "hanim_l_metatarsal_pha5_pt"

HAnimHumanoid44.sites.append(HAnimSite1908)
HAnimSite1909 = x3d.HAnimSite()
HAnimSite1909.USE = "hanim_r_metatarsal_pha5_pt"

HAnimHumanoid44.sites.append(HAnimSite1909)
HAnimSite1910 = x3d.HAnimSite()
HAnimSite1910.USE = "hanim_l_middle_distal_tip"

HAnimHumanoid44.sites.append(HAnimSite1910)
HAnimSite1911 = x3d.HAnimSite()
HAnimSite1911.USE = "hanim_r_middle_distal_tip"

HAnimHumanoid44.sites.append(HAnimSite1911)
HAnimSite1912 = x3d.HAnimSite()
HAnimSite1912.USE = "hanim_r_neck_base_pt"

HAnimHumanoid44.sites.append(HAnimSite1912)
HAnimSite1913 = x3d.HAnimSite()
HAnimSite1913.USE = "hanim_l_neck_base_pt"

HAnimHumanoid44.sites.append(HAnimSite1913)
HAnimSite1914 = x3d.HAnimSite()
HAnimSite1914.USE = "hanim_l_olecranon_pt"

HAnimHumanoid44.sites.append(HAnimSite1914)
HAnimSite1915 = x3d.HAnimSite()
HAnimSite1915.USE = "hanim_r_olecranon_pt"

HAnimHumanoid44.sites.append(HAnimSite1915)
HAnimSite1916 = x3d.HAnimSite()
HAnimSite1916.USE = "hanim_l_pinky_distal_tip"

HAnimHumanoid44.sites.append(HAnimSite1916)
HAnimSite1917 = x3d.HAnimSite()
HAnimSite1917.USE = "hanim_r_pinky_distal_tip"

HAnimHumanoid44.sites.append(HAnimSite1917)
HAnimSite1918 = x3d.HAnimSite()
HAnimSite1918.USE = "hanim_r_psis_pt"

HAnimHumanoid44.sites.append(HAnimSite1918)
HAnimSite1919 = x3d.HAnimSite()
HAnimSite1919.USE = "hanim_l_psis_pt"

HAnimHumanoid44.sites.append(HAnimSite1919)
HAnimSite1920 = x3d.HAnimSite()
HAnimSite1920.USE = "hanim_l_radial_styloid_pt"

HAnimHumanoid44.sites.append(HAnimSite1920)
HAnimSite1921 = x3d.HAnimSite()
HAnimSite1921.USE = "hanim_r_radial_styloid_pt"

HAnimHumanoid44.sites.append(HAnimSite1921)
HAnimSite1922 = x3d.HAnimSite()
HAnimSite1922.USE = "hanim_l_radiale_pt"

HAnimHumanoid44.sites.append(HAnimSite1922)
HAnimSite1923 = x3d.HAnimSite()
HAnimSite1923.USE = "hanim_r_radiale_pt"

HAnimHumanoid44.sites.append(HAnimSite1923)
HAnimSite1924 = x3d.HAnimSite()
HAnimSite1924.USE = "hanim_r_rib10_pt"

HAnimHumanoid44.sites.append(HAnimSite1924)
HAnimSite1925 = x3d.HAnimSite()
HAnimSite1925.USE = "hanim_l_rib10_pt"

HAnimHumanoid44.sites.append(HAnimSite1925)
HAnimSite1926 = x3d.HAnimSite()
HAnimSite1926.USE = "hanim_l_ring_distal_tip"

HAnimHumanoid44.sites.append(HAnimSite1926)
HAnimSite1927 = x3d.HAnimSite()
HAnimSite1927.USE = "hanim_r_ring_distal_tip"

HAnimHumanoid44.sites.append(HAnimSite1927)
HAnimSite1928 = x3d.HAnimSite()
HAnimSite1928.USE = "hanim_temporomandibular_l_site_pt"

HAnimHumanoid44.sites.append(HAnimSite1928)
HAnimSite1929 = x3d.HAnimSite()
HAnimSite1929.USE = "hanim_temporomandibular_r_site_pt"

HAnimHumanoid44.sites.append(HAnimSite1929)
HAnimSite1930 = x3d.HAnimSite()
HAnimSite1930.USE = "hanim_l_sphyrion_pt"

HAnimHumanoid44.sites.append(HAnimSite1930)
HAnimSite1931 = x3d.HAnimSite()
HAnimSite1931.USE = "hanim_r_sphyrion_pt"

HAnimHumanoid44.sites.append(HAnimSite1931)
HAnimSite1932 = x3d.HAnimSite()
HAnimSite1932.USE = "hanim_r_thelion_pt"

HAnimHumanoid44.sites.append(HAnimSite1932)
HAnimSite1933 = x3d.HAnimSite()
HAnimSite1933.USE = "hanim_l_thelion_pt"

HAnimHumanoid44.sites.append(HAnimSite1933)
HAnimSite1934 = x3d.HAnimSite()
HAnimSite1934.USE = "hanim_l_thumb_distal_tip"

HAnimHumanoid44.sites.append(HAnimSite1934)
HAnimSite1935 = x3d.HAnimSite()
HAnimSite1935.USE = "hanim_r_thumb_distal_tip"

HAnimHumanoid44.sites.append(HAnimSite1935)
HAnimSite1936 = x3d.HAnimSite()
HAnimSite1936.USE = "hanim_r_tragion_pt"

HAnimHumanoid44.sites.append(HAnimSite1936)
HAnimSite1937 = x3d.HAnimSite()
HAnimSite1937.USE = "hanim_l_tragion_pt"

HAnimHumanoid44.sites.append(HAnimSite1937)
HAnimSite1938 = x3d.HAnimSite()
HAnimSite1938.USE = "hanim_r_trochanterion_pt"

HAnimHumanoid44.sites.append(HAnimSite1938)
HAnimSite1939 = x3d.HAnimSite()
HAnimSite1939.USE = "hanim_l_trochanterion_pt"

HAnimHumanoid44.sites.append(HAnimSite1939)
HAnimSite1940 = x3d.HAnimSite()
HAnimSite1940.USE = "hanim_l_ulnar_styloid_pt"

HAnimHumanoid44.sites.append(HAnimSite1940)
HAnimSite1941 = x3d.HAnimSite()
HAnimSite1941.USE = "hanim_r_ulnar_styloid_pt"

HAnimHumanoid44.sites.append(HAnimSite1941)

Scene30.children.append(HAnimHumanoid44)
Group1942 = x3d.Group()
Group1942.DEF = "StopAnimation"
TimeSensor1943 = x3d.TimeSensor()
TimeSensor1943.DEF = "StopTimer"
TimeSensor1943.cycleInterval = 5.73
TimeSensor1943.loop = True

Group1942.children.append(TimeSensor1943)
PositionInterpolator1944 = x3d.PositionInterpolator()
PositionInterpolator1944.DEF = "Stop_humanoid_root_TranslationInterpolator"
PositionInterpolator1944.key = [0,0.5,1]
PositionInterpolator1944.keyValue = (0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000)

Group1942.children.append(PositionInterpolator1944)
OrientationInterpolator1945 = x3d.OrientationInterpolator()
OrientationInterpolator1945.DEF = "Stop_humanoid_root_RotationInterpolator"
OrientationInterpolator1945.key = [0,0.5,1]
OrientationInterpolator1945.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1945)
OrientationInterpolator1946 = x3d.OrientationInterpolator()
OrientationInterpolator1946.DEF = "Stop_sacroiliac_RotationInterpolator"
OrientationInterpolator1946.key = [0,0.5,1]
OrientationInterpolator1946.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1946)
OrientationInterpolator1947 = x3d.OrientationInterpolator()
OrientationInterpolator1947.DEF = "Stop_l_hip_RotationInterpolator"
OrientationInterpolator1947.key = [0,0.5,1]
OrientationInterpolator1947.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1947)
OrientationInterpolator1948 = x3d.OrientationInterpolator()
OrientationInterpolator1948.DEF = "Stop_l_knee_RotationInterpolator"
OrientationInterpolator1948.key = [0,0.5,1]
OrientationInterpolator1948.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1948)
OrientationInterpolator1949 = x3d.OrientationInterpolator()
OrientationInterpolator1949.DEF = "Stop_l_ankle_RotationInterpolator"
OrientationInterpolator1949.key = [0,0.5,1]
OrientationInterpolator1949.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1949)
OrientationInterpolator1950 = x3d.OrientationInterpolator()
OrientationInterpolator1950.DEF = "Stop_l_subtalar_RotationInterpolator"
OrientationInterpolator1950.key = [0,0.5,1]
OrientationInterpolator1950.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1950)
OrientationInterpolator1951 = x3d.OrientationInterpolator()
OrientationInterpolator1951.DEF = "Stop_l_midtarsal_RotationInterpolator"
OrientationInterpolator1951.key = [0,0.5,1]
OrientationInterpolator1951.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1951)
OrientationInterpolator1952 = x3d.OrientationInterpolator()
OrientationInterpolator1952.DEF = "Stop_l_metatarsal_RotationInterpolator"
OrientationInterpolator1952.key = [0,0.5,1]
OrientationInterpolator1952.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1952)
OrientationInterpolator1953 = x3d.OrientationInterpolator()
OrientationInterpolator1953.DEF = "Stop_r_hip_RotationInterpolator"
OrientationInterpolator1953.key = [0,0.5,1]
OrientationInterpolator1953.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1953)
OrientationInterpolator1954 = x3d.OrientationInterpolator()
OrientationInterpolator1954.DEF = "Stop_r_knee_RotationInterpolator"
OrientationInterpolator1954.key = [0,0.5,1]
OrientationInterpolator1954.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1954)
OrientationInterpolator1955 = x3d.OrientationInterpolator()
OrientationInterpolator1955.DEF = "Stop_r_ankle_RotationInterpolator"
OrientationInterpolator1955.key = [0,0.5,1]
OrientationInterpolator1955.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1955)
OrientationInterpolator1956 = x3d.OrientationInterpolator()
OrientationInterpolator1956.DEF = "Stop_r_subtalar_RotationInterpolator"
OrientationInterpolator1956.key = [0,0.5,1]
OrientationInterpolator1956.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1956)
OrientationInterpolator1957 = x3d.OrientationInterpolator()
OrientationInterpolator1957.DEF = "Stop_r_midtarsal_RotationInterpolator"
OrientationInterpolator1957.key = [0,0.5,1]
OrientationInterpolator1957.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1957)
OrientationInterpolator1958 = x3d.OrientationInterpolator()
OrientationInterpolator1958.DEF = "Stop_r_metatarsal_RotationInterpolator"
OrientationInterpolator1958.key = [0,0.5,1]
OrientationInterpolator1958.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1958)
OrientationInterpolator1959 = x3d.OrientationInterpolator()
OrientationInterpolator1959.DEF = "Stop_vl5_RotationInterpolator"
OrientationInterpolator1959.key = [0,0.5,1]
OrientationInterpolator1959.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1959)
OrientationInterpolator1960 = x3d.OrientationInterpolator()
OrientationInterpolator1960.DEF = "Stop_vl4_RotationInterpolator"
OrientationInterpolator1960.key = [0,0.5,1]
OrientationInterpolator1960.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1960)
OrientationInterpolator1961 = x3d.OrientationInterpolator()
OrientationInterpolator1961.DEF = "Stop_vl3_RotationInterpolator"
OrientationInterpolator1961.key = [0,0.5,1]
OrientationInterpolator1961.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1961)
OrientationInterpolator1962 = x3d.OrientationInterpolator()
OrientationInterpolator1962.DEF = "Stop_vl2_RotationInterpolator"
OrientationInterpolator1962.key = [0,0.5,1]
OrientationInterpolator1962.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1962)
OrientationInterpolator1963 = x3d.OrientationInterpolator()
OrientationInterpolator1963.DEF = "Stop_vl1_RotationInterpolator"
OrientationInterpolator1963.key = [0,0.5,1]
OrientationInterpolator1963.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1963)
OrientationInterpolator1964 = x3d.OrientationInterpolator()
OrientationInterpolator1964.DEF = "Stop_vt12_RotationInterpolator"
OrientationInterpolator1964.key = [0,0.5,1]
OrientationInterpolator1964.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1964)
OrientationInterpolator1965 = x3d.OrientationInterpolator()
OrientationInterpolator1965.DEF = "Stop_vt11_RotationInterpolator"
OrientationInterpolator1965.key = [0,0.5,1]
OrientationInterpolator1965.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1965)
OrientationInterpolator1966 = x3d.OrientationInterpolator()
OrientationInterpolator1966.DEF = "Stop_vt10_RotationInterpolator"
OrientationInterpolator1966.key = [0,0.5,1]
OrientationInterpolator1966.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1966)
OrientationInterpolator1967 = x3d.OrientationInterpolator()
OrientationInterpolator1967.DEF = "Stop_vt9_RotationInterpolator"
OrientationInterpolator1967.key = [0,0.5,1]
OrientationInterpolator1967.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1967)
OrientationInterpolator1968 = x3d.OrientationInterpolator()
OrientationInterpolator1968.DEF = "Stop_vt8_RotationInterpolator"
OrientationInterpolator1968.key = [0,0.5,1]
OrientationInterpolator1968.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1968)
OrientationInterpolator1969 = x3d.OrientationInterpolator()
OrientationInterpolator1969.DEF = "Stop_vt7_RotationInterpolator"
OrientationInterpolator1969.key = [0,0.5,1]
OrientationInterpolator1969.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1969)
OrientationInterpolator1970 = x3d.OrientationInterpolator()
OrientationInterpolator1970.DEF = "Stop_vt6_RotationInterpolator"
OrientationInterpolator1970.key = [0,0.5,1]
OrientationInterpolator1970.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1970)
OrientationInterpolator1971 = x3d.OrientationInterpolator()
OrientationInterpolator1971.DEF = "Stop_vt5_RotationInterpolator"
OrientationInterpolator1971.key = [0,0.5,1]
OrientationInterpolator1971.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1971)
OrientationInterpolator1972 = x3d.OrientationInterpolator()
OrientationInterpolator1972.DEF = "Stop_vt4_RotationInterpolator"
OrientationInterpolator1972.key = [0,0.5,1]
OrientationInterpolator1972.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1972)
OrientationInterpolator1973 = x3d.OrientationInterpolator()
OrientationInterpolator1973.DEF = "Stop_vt3_RotationInterpolator"
OrientationInterpolator1973.key = [0,0.5,1]
OrientationInterpolator1973.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1973)
OrientationInterpolator1974 = x3d.OrientationInterpolator()
OrientationInterpolator1974.DEF = "Stop_vt2_RotationInterpolator"
OrientationInterpolator1974.key = [0,0.5,1]
OrientationInterpolator1974.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1974)
OrientationInterpolator1975 = x3d.OrientationInterpolator()
OrientationInterpolator1975.DEF = "Stop_vt1_RotationInterpolator"
OrientationInterpolator1975.key = [0,0.5,1]
OrientationInterpolator1975.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1975)
OrientationInterpolator1976 = x3d.OrientationInterpolator()
OrientationInterpolator1976.DEF = "Stop_vc7_RotationInterpolator"
OrientationInterpolator1976.key = [0,0.5,1]
OrientationInterpolator1976.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1976)
OrientationInterpolator1977 = x3d.OrientationInterpolator()
OrientationInterpolator1977.DEF = "Stop_vc6_RotationInterpolator"
OrientationInterpolator1977.key = [0,0.5,1]
OrientationInterpolator1977.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1977)
OrientationInterpolator1978 = x3d.OrientationInterpolator()
OrientationInterpolator1978.DEF = "Stop_vc5_RotationInterpolator"
OrientationInterpolator1978.key = [0,0.5,1]
OrientationInterpolator1978.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1978)
OrientationInterpolator1979 = x3d.OrientationInterpolator()
OrientationInterpolator1979.DEF = "Stop_vc4_RotationInterpolator"
OrientationInterpolator1979.key = [0,0.5,1]
OrientationInterpolator1979.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1979)
OrientationInterpolator1980 = x3d.OrientationInterpolator()
OrientationInterpolator1980.DEF = "Stop_vc3_RotationInterpolator"
OrientationInterpolator1980.key = [0,0.5,1]
OrientationInterpolator1980.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1980)
OrientationInterpolator1981 = x3d.OrientationInterpolator()
OrientationInterpolator1981.DEF = "Stop_vc2_RotationInterpolator"
OrientationInterpolator1981.key = [0,0.5,1]
OrientationInterpolator1981.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1981)
OrientationInterpolator1982 = x3d.OrientationInterpolator()
OrientationInterpolator1982.DEF = "Stop_vc1_RotationInterpolator"
OrientationInterpolator1982.key = [0,0.5,1]
OrientationInterpolator1982.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1982)
OrientationInterpolator1983 = x3d.OrientationInterpolator()
OrientationInterpolator1983.DEF = "Stop_skullbase_RotationInterpolator"
OrientationInterpolator1983.key = [0,0.5,1]
OrientationInterpolator1983.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1983)
OrientationInterpolator1984 = x3d.OrientationInterpolator()
OrientationInterpolator1984.DEF = "Stop_l_eyeball_joint_RotationInterpolator"
OrientationInterpolator1984.key = [0,0.5,1]
OrientationInterpolator1984.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1984)
OrientationInterpolator1985 = x3d.OrientationInterpolator()
OrientationInterpolator1985.DEF = "Stop_r_eyeball_joint_RotationInterpolator"
OrientationInterpolator1985.key = [0,0.5,1]
OrientationInterpolator1985.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1985)
OrientationInterpolator1986 = x3d.OrientationInterpolator()
OrientationInterpolator1986.DEF = "Stop_l_sternoclavicular_RotationInterpolator"
OrientationInterpolator1986.key = [0,0.5,1]
OrientationInterpolator1986.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1986)
OrientationInterpolator1987 = x3d.OrientationInterpolator()
OrientationInterpolator1987.DEF = "Stop_l_acromioclavicular_RotationInterpolator"
OrientationInterpolator1987.key = [0,0.5,1]
OrientationInterpolator1987.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1987)
OrientationInterpolator1988 = x3d.OrientationInterpolator()
OrientationInterpolator1988.DEF = "Stop_l_shoulder_RotationInterpolator"
OrientationInterpolator1988.key = [0,0.5,1]
OrientationInterpolator1988.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1988)
OrientationInterpolator1989 = x3d.OrientationInterpolator()
OrientationInterpolator1989.DEF = "Stop_l_elbow_RotationInterpolator"
OrientationInterpolator1989.key = [0,0.5,1]
OrientationInterpolator1989.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1989)
OrientationInterpolator1990 = x3d.OrientationInterpolator()
OrientationInterpolator1990.DEF = "Stop_l_wrist_RotationInterpolator"
OrientationInterpolator1990.key = [0,0.5,1]
OrientationInterpolator1990.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1990)
OrientationInterpolator1991 = x3d.OrientationInterpolator()
OrientationInterpolator1991.DEF = "Stop_l_thumb1_RotationInterpolator"
OrientationInterpolator1991.key = [0,0.5,1]
OrientationInterpolator1991.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1991)
OrientationInterpolator1992 = x3d.OrientationInterpolator()
OrientationInterpolator1992.DEF = "Stop_l_thumb2_RotationInterpolator"
OrientationInterpolator1992.key = [0,0.5,1]
OrientationInterpolator1992.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1992)
OrientationInterpolator1993 = x3d.OrientationInterpolator()
OrientationInterpolator1993.DEF = "Stop_l_thumb3_RotationInterpolator"
OrientationInterpolator1993.key = [0,0.5,1]
OrientationInterpolator1993.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1993)
OrientationInterpolator1994 = x3d.OrientationInterpolator()
OrientationInterpolator1994.DEF = "Stop_l_index0_RotationInterpolator"
OrientationInterpolator1994.key = [0,0.5,1]
OrientationInterpolator1994.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1994)
OrientationInterpolator1995 = x3d.OrientationInterpolator()
OrientationInterpolator1995.DEF = "Stop_l_index1_RotationInterpolator"
OrientationInterpolator1995.key = [0,0.5,1]
OrientationInterpolator1995.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1995)
OrientationInterpolator1996 = x3d.OrientationInterpolator()
OrientationInterpolator1996.DEF = "Stop_l_index2_RotationInterpolator"
OrientationInterpolator1996.key = [0,0.5,1]
OrientationInterpolator1996.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1996)
OrientationInterpolator1997 = x3d.OrientationInterpolator()
OrientationInterpolator1997.DEF = "Stop_l_index3_RotationInterpolator"
OrientationInterpolator1997.key = [0,0.5,1]
OrientationInterpolator1997.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1997)
OrientationInterpolator1998 = x3d.OrientationInterpolator()
OrientationInterpolator1998.DEF = "Stop_l_middle0_RotationInterpolator"
OrientationInterpolator1998.key = [0,0.5,1]
OrientationInterpolator1998.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1998)
OrientationInterpolator1999 = x3d.OrientationInterpolator()
OrientationInterpolator1999.DEF = "Stop_l_middle1_RotationInterpolator"
OrientationInterpolator1999.key = [0,0.5,1]
OrientationInterpolator1999.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator1999)
OrientationInterpolator2000 = x3d.OrientationInterpolator()
OrientationInterpolator2000.DEF = "Stop_l_middle2_RotationInterpolator"
OrientationInterpolator2000.key = [0,0.5,1]
OrientationInterpolator2000.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator2000)
OrientationInterpolator2001 = x3d.OrientationInterpolator()
OrientationInterpolator2001.DEF = "Stop_l_middle3_RotationInterpolator"
OrientationInterpolator2001.key = [0,0.5,1]
OrientationInterpolator2001.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator2001)
OrientationInterpolator2002 = x3d.OrientationInterpolator()
OrientationInterpolator2002.DEF = "Stop_l_ring0_RotationInterpolator"
OrientationInterpolator2002.key = [0,0.5,1]
OrientationInterpolator2002.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator2002)
OrientationInterpolator2003 = x3d.OrientationInterpolator()
OrientationInterpolator2003.DEF = "Stop_l_ring1_RotationInterpolator"
OrientationInterpolator2003.key = [0,0.5,1]
OrientationInterpolator2003.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator2003)
OrientationInterpolator2004 = x3d.OrientationInterpolator()
OrientationInterpolator2004.DEF = "Stop_l_ring2_RotationInterpolator"
OrientationInterpolator2004.key = [0,0.5,1]
OrientationInterpolator2004.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator2004)
OrientationInterpolator2005 = x3d.OrientationInterpolator()
OrientationInterpolator2005.DEF = "Stop_l_ring3_RotationInterpolator"
OrientationInterpolator2005.key = [0,0.5,1]
OrientationInterpolator2005.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator2005)
OrientationInterpolator2006 = x3d.OrientationInterpolator()
OrientationInterpolator2006.DEF = "Stop_l_pinky0_RotationInterpolator"
OrientationInterpolator2006.key = [0,0.5,1]
OrientationInterpolator2006.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator2006)
OrientationInterpolator2007 = x3d.OrientationInterpolator()
OrientationInterpolator2007.DEF = "Stop_l_pinky1_RotationInterpolator"
OrientationInterpolator2007.key = [0,0.5,1]
OrientationInterpolator2007.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator2007)
OrientationInterpolator2008 = x3d.OrientationInterpolator()
OrientationInterpolator2008.DEF = "Stop_l_pinky2_RotationInterpolator"
OrientationInterpolator2008.key = [0,0.5,1]
OrientationInterpolator2008.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator2008)
OrientationInterpolator2009 = x3d.OrientationInterpolator()
OrientationInterpolator2009.DEF = "Stop_l_pinky3_RotationInterpolator"
OrientationInterpolator2009.key = [0,0.5,1]
OrientationInterpolator2009.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator2009)
OrientationInterpolator2010 = x3d.OrientationInterpolator()
OrientationInterpolator2010.DEF = "Stop_r_sternoclavicular_RotationInterpolator"
OrientationInterpolator2010.key = [0,0.5,1]
OrientationInterpolator2010.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator2010)
OrientationInterpolator2011 = x3d.OrientationInterpolator()
OrientationInterpolator2011.DEF = "Stop_r_acromioclavicular_RotationInterpolator"
OrientationInterpolator2011.key = [0,0.5,1]
OrientationInterpolator2011.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator2011)
OrientationInterpolator2012 = x3d.OrientationInterpolator()
OrientationInterpolator2012.DEF = "Stop_r_shoulder_RotationInterpolator"
OrientationInterpolator2012.key = [0,0.5,1]
OrientationInterpolator2012.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator2012)
OrientationInterpolator2013 = x3d.OrientationInterpolator()
OrientationInterpolator2013.DEF = "Stop_r_elbow_RotationInterpolator"
OrientationInterpolator2013.key = [0,0.5,1]
OrientationInterpolator2013.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator2013)
OrientationInterpolator2014 = x3d.OrientationInterpolator()
OrientationInterpolator2014.DEF = "Stop_r_wrist_RotationInterpolator"
OrientationInterpolator2014.key = [0,0.5,1]
OrientationInterpolator2014.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator2014)
OrientationInterpolator2015 = x3d.OrientationInterpolator()
OrientationInterpolator2015.DEF = "Stop_r_thumb1_RotationInterpolator"
OrientationInterpolator2015.key = [0,0.5,1]
OrientationInterpolator2015.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator2015)
OrientationInterpolator2016 = x3d.OrientationInterpolator()
OrientationInterpolator2016.DEF = "Stop_r_thumb2_RotationInterpolator"
OrientationInterpolator2016.key = [0,0.5,1]
OrientationInterpolator2016.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator2016)
OrientationInterpolator2017 = x3d.OrientationInterpolator()
OrientationInterpolator2017.DEF = "Stop_r_thumb3_RotationInterpolator"
OrientationInterpolator2017.key = [0,0.5,1]
OrientationInterpolator2017.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator2017)
OrientationInterpolator2018 = x3d.OrientationInterpolator()
OrientationInterpolator2018.DEF = "Stop_r_index0_RotationInterpolator"
OrientationInterpolator2018.key = [0,0.5,1]
OrientationInterpolator2018.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator2018)
OrientationInterpolator2019 = x3d.OrientationInterpolator()
OrientationInterpolator2019.DEF = "Stop_r_index1_RotationInterpolator"
OrientationInterpolator2019.key = [0,0.5,1]
OrientationInterpolator2019.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator2019)
OrientationInterpolator2020 = x3d.OrientationInterpolator()
OrientationInterpolator2020.DEF = "Stop_r_index2_RotationInterpolator"
OrientationInterpolator2020.key = [0,0.5,1]
OrientationInterpolator2020.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator2020)
OrientationInterpolator2021 = x3d.OrientationInterpolator()
OrientationInterpolator2021.DEF = "Stop_r_index3_RotationInterpolator"
OrientationInterpolator2021.key = [0,0.5,1]
OrientationInterpolator2021.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator2021)
OrientationInterpolator2022 = x3d.OrientationInterpolator()
OrientationInterpolator2022.DEF = "Stop_r_middle0_RotationInterpolator"
OrientationInterpolator2022.key = [0,0.5,1]
OrientationInterpolator2022.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator2022)
OrientationInterpolator2023 = x3d.OrientationInterpolator()
OrientationInterpolator2023.DEF = "Stop_r_middle1_RotationInterpolator"
OrientationInterpolator2023.key = [0,0.5,1]
OrientationInterpolator2023.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator2023)
OrientationInterpolator2024 = x3d.OrientationInterpolator()
OrientationInterpolator2024.DEF = "Stop_r_middle2_RotationInterpolator"
OrientationInterpolator2024.key = [0,0.5,1]
OrientationInterpolator2024.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator2024)
OrientationInterpolator2025 = x3d.OrientationInterpolator()
OrientationInterpolator2025.DEF = "Stop_r_middle3_RotationInterpolator"
OrientationInterpolator2025.key = [0,0.5,1]
OrientationInterpolator2025.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator2025)
OrientationInterpolator2026 = x3d.OrientationInterpolator()
OrientationInterpolator2026.DEF = "Stop_r_ring0_RotationInterpolator"
OrientationInterpolator2026.key = [0,0.5,1]
OrientationInterpolator2026.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator2026)
OrientationInterpolator2027 = x3d.OrientationInterpolator()
OrientationInterpolator2027.DEF = "Stop_r_ring1_RotationInterpolator"
OrientationInterpolator2027.key = [0,0.5,1]
OrientationInterpolator2027.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator2027)
OrientationInterpolator2028 = x3d.OrientationInterpolator()
OrientationInterpolator2028.DEF = "Stop_r_ring2_RotationInterpolator"
OrientationInterpolator2028.key = [0,0.5,1]
OrientationInterpolator2028.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator2028)
OrientationInterpolator2029 = x3d.OrientationInterpolator()
OrientationInterpolator2029.DEF = "Stop_r_ring3_RotationInterpolator"
OrientationInterpolator2029.key = [0,0.5,1]
OrientationInterpolator2029.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator2029)
OrientationInterpolator2030 = x3d.OrientationInterpolator()
OrientationInterpolator2030.DEF = "Stop_r_pinky0_RotationInterpolator"
OrientationInterpolator2030.key = [0,0.5,1]
OrientationInterpolator2030.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator2030)
OrientationInterpolator2031 = x3d.OrientationInterpolator()
OrientationInterpolator2031.DEF = "Stop_r_pinky1_RotationInterpolator"
OrientationInterpolator2031.key = [0,0.5,1]
OrientationInterpolator2031.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator2031)
OrientationInterpolator2032 = x3d.OrientationInterpolator()
OrientationInterpolator2032.DEF = "Stop_r_pinky2_RotationInterpolator"
OrientationInterpolator2032.key = [0,0.5,1]
OrientationInterpolator2032.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator2032)
OrientationInterpolator2033 = x3d.OrientationInterpolator()
OrientationInterpolator2033.DEF = "Stop_r_pinky3_RotationInterpolator"
OrientationInterpolator2033.key = [0,0.5,1]
OrientationInterpolator2033.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group1942.children.append(OrientationInterpolator2033)
ROUTE2034 = x3d.ROUTE()
ROUTE2034.fromField = "fraction_changed"
ROUTE2034.fromNode = "StopTimer"
ROUTE2034.toField = "set_fraction"
ROUTE2034.toNode = "Stop_humanoid_root_TranslationInterpolator"

Group1942.children.append(ROUTE2034)
ROUTE2035 = x3d.ROUTE()
ROUTE2035.fromField = "fraction_changed"
ROUTE2035.fromNode = "StopTimer"
ROUTE2035.toField = "set_fraction"
ROUTE2035.toNode = "Stop_humanoid_root_RotationInterpolator"

Group1942.children.append(ROUTE2035)
ROUTE2036 = x3d.ROUTE()
ROUTE2036.fromField = "fraction_changed"
ROUTE2036.fromNode = "StopTimer"
ROUTE2036.toField = "set_fraction"
ROUTE2036.toNode = "Stop_sacroiliac_RotationInterpolator"

Group1942.children.append(ROUTE2036)
ROUTE2037 = x3d.ROUTE()
ROUTE2037.fromField = "fraction_changed"
ROUTE2037.fromNode = "StopTimer"
ROUTE2037.toField = "set_fraction"
ROUTE2037.toNode = "Stop_l_hip_RotationInterpolator"

Group1942.children.append(ROUTE2037)
ROUTE2038 = x3d.ROUTE()
ROUTE2038.fromField = "fraction_changed"
ROUTE2038.fromNode = "StopTimer"
ROUTE2038.toField = "set_fraction"
ROUTE2038.toNode = "Stop_l_knee_RotationInterpolator"

Group1942.children.append(ROUTE2038)
ROUTE2039 = x3d.ROUTE()
ROUTE2039.fromField = "fraction_changed"
ROUTE2039.fromNode = "StopTimer"
ROUTE2039.toField = "set_fraction"
ROUTE2039.toNode = "Stop_l_ankle_RotationInterpolator"

Group1942.children.append(ROUTE2039)
ROUTE2040 = x3d.ROUTE()
ROUTE2040.fromField = "fraction_changed"
ROUTE2040.fromNode = "StopTimer"
ROUTE2040.toField = "set_fraction"
ROUTE2040.toNode = "Stop_l_subtalar_RotationInterpolator"

Group1942.children.append(ROUTE2040)
ROUTE2041 = x3d.ROUTE()
ROUTE2041.fromField = "fraction_changed"
ROUTE2041.fromNode = "StopTimer"
ROUTE2041.toField = "set_fraction"
ROUTE2041.toNode = "Stop_l_midtarsal_RotationInterpolator"

Group1942.children.append(ROUTE2041)
ROUTE2042 = x3d.ROUTE()
ROUTE2042.fromField = "fraction_changed"
ROUTE2042.fromNode = "StopTimer"
ROUTE2042.toField = "set_fraction"
ROUTE2042.toNode = "Stop_l_metatarsal_RotationInterpolator"

Group1942.children.append(ROUTE2042)
ROUTE2043 = x3d.ROUTE()
ROUTE2043.fromField = "fraction_changed"
ROUTE2043.fromNode = "StopTimer"
ROUTE2043.toField = "set_fraction"
ROUTE2043.toNode = "Stop_r_hip_RotationInterpolator"

Group1942.children.append(ROUTE2043)
ROUTE2044 = x3d.ROUTE()
ROUTE2044.fromField = "fraction_changed"
ROUTE2044.fromNode = "StopTimer"
ROUTE2044.toField = "set_fraction"
ROUTE2044.toNode = "Stop_r_knee_RotationInterpolator"

Group1942.children.append(ROUTE2044)
ROUTE2045 = x3d.ROUTE()
ROUTE2045.fromField = "fraction_changed"
ROUTE2045.fromNode = "StopTimer"
ROUTE2045.toField = "set_fraction"
ROUTE2045.toNode = "Stop_r_ankle_RotationInterpolator"

Group1942.children.append(ROUTE2045)
ROUTE2046 = x3d.ROUTE()
ROUTE2046.fromField = "fraction_changed"
ROUTE2046.fromNode = "StopTimer"
ROUTE2046.toField = "set_fraction"
ROUTE2046.toNode = "Stop_r_subtalar_RotationInterpolator"

Group1942.children.append(ROUTE2046)
ROUTE2047 = x3d.ROUTE()
ROUTE2047.fromField = "fraction_changed"
ROUTE2047.fromNode = "StopTimer"
ROUTE2047.toField = "set_fraction"
ROUTE2047.toNode = "Stop_r_midtarsal_RotationInterpolator"

Group1942.children.append(ROUTE2047)
ROUTE2048 = x3d.ROUTE()
ROUTE2048.fromField = "fraction_changed"
ROUTE2048.fromNode = "StopTimer"
ROUTE2048.toField = "set_fraction"
ROUTE2048.toNode = "Stop_r_metatarsal_RotationInterpolator"

Group1942.children.append(ROUTE2048)
ROUTE2049 = x3d.ROUTE()
ROUTE2049.fromField = "fraction_changed"
ROUTE2049.fromNode = "StopTimer"
ROUTE2049.toField = "set_fraction"
ROUTE2049.toNode = "Stop_vl5_RotationInterpolator"

Group1942.children.append(ROUTE2049)
ROUTE2050 = x3d.ROUTE()
ROUTE2050.fromField = "fraction_changed"
ROUTE2050.fromNode = "StopTimer"
ROUTE2050.toField = "set_fraction"
ROUTE2050.toNode = "Stop_vl4_RotationInterpolator"

Group1942.children.append(ROUTE2050)
ROUTE2051 = x3d.ROUTE()
ROUTE2051.fromField = "fraction_changed"
ROUTE2051.fromNode = "StopTimer"
ROUTE2051.toField = "set_fraction"
ROUTE2051.toNode = "Stop_vl3_RotationInterpolator"

Group1942.children.append(ROUTE2051)
ROUTE2052 = x3d.ROUTE()
ROUTE2052.fromField = "fraction_changed"
ROUTE2052.fromNode = "StopTimer"
ROUTE2052.toField = "set_fraction"
ROUTE2052.toNode = "Stop_vl2_RotationInterpolator"

Group1942.children.append(ROUTE2052)
ROUTE2053 = x3d.ROUTE()
ROUTE2053.fromField = "fraction_changed"
ROUTE2053.fromNode = "StopTimer"
ROUTE2053.toField = "set_fraction"
ROUTE2053.toNode = "Stop_vl1_RotationInterpolator"

Group1942.children.append(ROUTE2053)
ROUTE2054 = x3d.ROUTE()
ROUTE2054.fromField = "fraction_changed"
ROUTE2054.fromNode = "StopTimer"
ROUTE2054.toField = "set_fraction"
ROUTE2054.toNode = "Stop_vt12_RotationInterpolator"

Group1942.children.append(ROUTE2054)
ROUTE2055 = x3d.ROUTE()
ROUTE2055.fromField = "fraction_changed"
ROUTE2055.fromNode = "StopTimer"
ROUTE2055.toField = "set_fraction"
ROUTE2055.toNode = "Stop_vt11_RotationInterpolator"

Group1942.children.append(ROUTE2055)
ROUTE2056 = x3d.ROUTE()
ROUTE2056.fromField = "fraction_changed"
ROUTE2056.fromNode = "StopTimer"
ROUTE2056.toField = "set_fraction"
ROUTE2056.toNode = "Stop_vt10_RotationInterpolator"

Group1942.children.append(ROUTE2056)
ROUTE2057 = x3d.ROUTE()
ROUTE2057.fromField = "fraction_changed"
ROUTE2057.fromNode = "StopTimer"
ROUTE2057.toField = "set_fraction"
ROUTE2057.toNode = "Stop_vt9_RotationInterpolator"

Group1942.children.append(ROUTE2057)
ROUTE2058 = x3d.ROUTE()
ROUTE2058.fromField = "fraction_changed"
ROUTE2058.fromNode = "StopTimer"
ROUTE2058.toField = "set_fraction"
ROUTE2058.toNode = "Stop_vt8_RotationInterpolator"

Group1942.children.append(ROUTE2058)
ROUTE2059 = x3d.ROUTE()
ROUTE2059.fromField = "fraction_changed"
ROUTE2059.fromNode = "StopTimer"
ROUTE2059.toField = "set_fraction"
ROUTE2059.toNode = "Stop_vt7_RotationInterpolator"

Group1942.children.append(ROUTE2059)
ROUTE2060 = x3d.ROUTE()
ROUTE2060.fromField = "fraction_changed"
ROUTE2060.fromNode = "StopTimer"
ROUTE2060.toField = "set_fraction"
ROUTE2060.toNode = "Stop_vt6_RotationInterpolator"

Group1942.children.append(ROUTE2060)
ROUTE2061 = x3d.ROUTE()
ROUTE2061.fromField = "fraction_changed"
ROUTE2061.fromNode = "StopTimer"
ROUTE2061.toField = "set_fraction"
ROUTE2061.toNode = "Stop_vt5_RotationInterpolator"

Group1942.children.append(ROUTE2061)
ROUTE2062 = x3d.ROUTE()
ROUTE2062.fromField = "fraction_changed"
ROUTE2062.fromNode = "StopTimer"
ROUTE2062.toField = "set_fraction"
ROUTE2062.toNode = "Stop_vt4_RotationInterpolator"

Group1942.children.append(ROUTE2062)
ROUTE2063 = x3d.ROUTE()
ROUTE2063.fromField = "fraction_changed"
ROUTE2063.fromNode = "StopTimer"
ROUTE2063.toField = "set_fraction"
ROUTE2063.toNode = "Stop_vt3_RotationInterpolator"

Group1942.children.append(ROUTE2063)
ROUTE2064 = x3d.ROUTE()
ROUTE2064.fromField = "fraction_changed"
ROUTE2064.fromNode = "StopTimer"
ROUTE2064.toField = "set_fraction"
ROUTE2064.toNode = "Stop_vt2_RotationInterpolator"

Group1942.children.append(ROUTE2064)
ROUTE2065 = x3d.ROUTE()
ROUTE2065.fromField = "fraction_changed"
ROUTE2065.fromNode = "StopTimer"
ROUTE2065.toField = "set_fraction"
ROUTE2065.toNode = "Stop_vt1_RotationInterpolator"

Group1942.children.append(ROUTE2065)
ROUTE2066 = x3d.ROUTE()
ROUTE2066.fromField = "fraction_changed"
ROUTE2066.fromNode = "StopTimer"
ROUTE2066.toField = "set_fraction"
ROUTE2066.toNode = "Stop_vc7_RotationInterpolator"

Group1942.children.append(ROUTE2066)
ROUTE2067 = x3d.ROUTE()
ROUTE2067.fromField = "fraction_changed"
ROUTE2067.fromNode = "StopTimer"
ROUTE2067.toField = "set_fraction"
ROUTE2067.toNode = "Stop_vc6_RotationInterpolator"

Group1942.children.append(ROUTE2067)
ROUTE2068 = x3d.ROUTE()
ROUTE2068.fromField = "fraction_changed"
ROUTE2068.fromNode = "StopTimer"
ROUTE2068.toField = "set_fraction"
ROUTE2068.toNode = "Stop_vc5_RotationInterpolator"

Group1942.children.append(ROUTE2068)
ROUTE2069 = x3d.ROUTE()
ROUTE2069.fromField = "fraction_changed"
ROUTE2069.fromNode = "StopTimer"
ROUTE2069.toField = "set_fraction"
ROUTE2069.toNode = "Stop_vc4_RotationInterpolator"

Group1942.children.append(ROUTE2069)
ROUTE2070 = x3d.ROUTE()
ROUTE2070.fromField = "fraction_changed"
ROUTE2070.fromNode = "StopTimer"
ROUTE2070.toField = "set_fraction"
ROUTE2070.toNode = "Stop_vc3_RotationInterpolator"

Group1942.children.append(ROUTE2070)
ROUTE2071 = x3d.ROUTE()
ROUTE2071.fromField = "fraction_changed"
ROUTE2071.fromNode = "StopTimer"
ROUTE2071.toField = "set_fraction"
ROUTE2071.toNode = "Stop_vc2_RotationInterpolator"

Group1942.children.append(ROUTE2071)
ROUTE2072 = x3d.ROUTE()
ROUTE2072.fromField = "fraction_changed"
ROUTE2072.fromNode = "StopTimer"
ROUTE2072.toField = "set_fraction"
ROUTE2072.toNode = "Stop_vc1_RotationInterpolator"

Group1942.children.append(ROUTE2072)
ROUTE2073 = x3d.ROUTE()
ROUTE2073.fromField = "fraction_changed"
ROUTE2073.fromNode = "StopTimer"
ROUTE2073.toField = "set_fraction"
ROUTE2073.toNode = "Stop_skullbase_RotationInterpolator"

Group1942.children.append(ROUTE2073)
ROUTE2074 = x3d.ROUTE()
ROUTE2074.fromField = "fraction_changed"
ROUTE2074.fromNode = "StopTimer"
ROUTE2074.toField = "set_fraction"
ROUTE2074.toNode = "Stop_l_eyeball_joint_RotationInterpolator"

Group1942.children.append(ROUTE2074)
ROUTE2075 = x3d.ROUTE()
ROUTE2075.fromField = "fraction_changed"
ROUTE2075.fromNode = "StopTimer"
ROUTE2075.toField = "set_fraction"
ROUTE2075.toNode = "Stop_r_eyeball_joint_RotationInterpolator"

Group1942.children.append(ROUTE2075)
ROUTE2076 = x3d.ROUTE()
ROUTE2076.fromField = "fraction_changed"
ROUTE2076.fromNode = "StopTimer"
ROUTE2076.toField = "set_fraction"
ROUTE2076.toNode = "Stop_l_sternoclavicular_RotationInterpolator"

Group1942.children.append(ROUTE2076)
ROUTE2077 = x3d.ROUTE()
ROUTE2077.fromField = "fraction_changed"
ROUTE2077.fromNode = "StopTimer"
ROUTE2077.toField = "set_fraction"
ROUTE2077.toNode = "Stop_l_acromioclavicular_RotationInterpolator"

Group1942.children.append(ROUTE2077)
ROUTE2078 = x3d.ROUTE()
ROUTE2078.fromField = "fraction_changed"
ROUTE2078.fromNode = "StopTimer"
ROUTE2078.toField = "set_fraction"
ROUTE2078.toNode = "Stop_l_shoulder_RotationInterpolator"

Group1942.children.append(ROUTE2078)
ROUTE2079 = x3d.ROUTE()
ROUTE2079.fromField = "fraction_changed"
ROUTE2079.fromNode = "StopTimer"
ROUTE2079.toField = "set_fraction"
ROUTE2079.toNode = "Stop_l_elbow_RotationInterpolator"

Group1942.children.append(ROUTE2079)
ROUTE2080 = x3d.ROUTE()
ROUTE2080.fromField = "fraction_changed"
ROUTE2080.fromNode = "StopTimer"
ROUTE2080.toField = "set_fraction"
ROUTE2080.toNode = "Stop_l_wrist_RotationInterpolator"

Group1942.children.append(ROUTE2080)
ROUTE2081 = x3d.ROUTE()
ROUTE2081.fromField = "fraction_changed"
ROUTE2081.fromNode = "StopTimer"
ROUTE2081.toField = "set_fraction"
ROUTE2081.toNode = "Stop_l_thumb1_RotationInterpolator"

Group1942.children.append(ROUTE2081)
ROUTE2082 = x3d.ROUTE()
ROUTE2082.fromField = "fraction_changed"
ROUTE2082.fromNode = "StopTimer"
ROUTE2082.toField = "set_fraction"
ROUTE2082.toNode = "Stop_l_thumb2_RotationInterpolator"

Group1942.children.append(ROUTE2082)
ROUTE2083 = x3d.ROUTE()
ROUTE2083.fromField = "fraction_changed"
ROUTE2083.fromNode = "StopTimer"
ROUTE2083.toField = "set_fraction"
ROUTE2083.toNode = "Stop_l_thumb3_RotationInterpolator"

Group1942.children.append(ROUTE2083)
ROUTE2084 = x3d.ROUTE()
ROUTE2084.fromField = "fraction_changed"
ROUTE2084.fromNode = "StopTimer"
ROUTE2084.toField = "set_fraction"
ROUTE2084.toNode = "Stop_l_index0_RotationInterpolator"

Group1942.children.append(ROUTE2084)
ROUTE2085 = x3d.ROUTE()
ROUTE2085.fromField = "fraction_changed"
ROUTE2085.fromNode = "StopTimer"
ROUTE2085.toField = "set_fraction"
ROUTE2085.toNode = "Stop_l_index1_RotationInterpolator"

Group1942.children.append(ROUTE2085)
ROUTE2086 = x3d.ROUTE()
ROUTE2086.fromField = "fraction_changed"
ROUTE2086.fromNode = "StopTimer"
ROUTE2086.toField = "set_fraction"
ROUTE2086.toNode = "Stop_l_index2_RotationInterpolator"

Group1942.children.append(ROUTE2086)
ROUTE2087 = x3d.ROUTE()
ROUTE2087.fromField = "fraction_changed"
ROUTE2087.fromNode = "StopTimer"
ROUTE2087.toField = "set_fraction"
ROUTE2087.toNode = "Stop_l_index3_RotationInterpolator"

Group1942.children.append(ROUTE2087)
ROUTE2088 = x3d.ROUTE()
ROUTE2088.fromField = "fraction_changed"
ROUTE2088.fromNode = "StopTimer"
ROUTE2088.toField = "set_fraction"
ROUTE2088.toNode = "Stop_l_middle0_RotationInterpolator"

Group1942.children.append(ROUTE2088)
ROUTE2089 = x3d.ROUTE()
ROUTE2089.fromField = "fraction_changed"
ROUTE2089.fromNode = "StopTimer"
ROUTE2089.toField = "set_fraction"
ROUTE2089.toNode = "Stop_l_middle1_RotationInterpolator"

Group1942.children.append(ROUTE2089)
ROUTE2090 = x3d.ROUTE()
ROUTE2090.fromField = "fraction_changed"
ROUTE2090.fromNode = "StopTimer"
ROUTE2090.toField = "set_fraction"
ROUTE2090.toNode = "Stop_l_middle2_RotationInterpolator"

Group1942.children.append(ROUTE2090)
ROUTE2091 = x3d.ROUTE()
ROUTE2091.fromField = "fraction_changed"
ROUTE2091.fromNode = "StopTimer"
ROUTE2091.toField = "set_fraction"
ROUTE2091.toNode = "Stop_l_middle3_RotationInterpolator"

Group1942.children.append(ROUTE2091)
ROUTE2092 = x3d.ROUTE()
ROUTE2092.fromField = "fraction_changed"
ROUTE2092.fromNode = "StopTimer"
ROUTE2092.toField = "set_fraction"
ROUTE2092.toNode = "Stop_l_ring0_RotationInterpolator"

Group1942.children.append(ROUTE2092)
ROUTE2093 = x3d.ROUTE()
ROUTE2093.fromField = "fraction_changed"
ROUTE2093.fromNode = "StopTimer"
ROUTE2093.toField = "set_fraction"
ROUTE2093.toNode = "Stop_l_ring1_RotationInterpolator"

Group1942.children.append(ROUTE2093)
ROUTE2094 = x3d.ROUTE()
ROUTE2094.fromField = "fraction_changed"
ROUTE2094.fromNode = "StopTimer"
ROUTE2094.toField = "set_fraction"
ROUTE2094.toNode = "Stop_l_ring2_RotationInterpolator"

Group1942.children.append(ROUTE2094)
ROUTE2095 = x3d.ROUTE()
ROUTE2095.fromField = "fraction_changed"
ROUTE2095.fromNode = "StopTimer"
ROUTE2095.toField = "set_fraction"
ROUTE2095.toNode = "Stop_l_ring3_RotationInterpolator"

Group1942.children.append(ROUTE2095)
ROUTE2096 = x3d.ROUTE()
ROUTE2096.fromField = "fraction_changed"
ROUTE2096.fromNode = "StopTimer"
ROUTE2096.toField = "set_fraction"
ROUTE2096.toNode = "Stop_l_pinky0_RotationInterpolator"

Group1942.children.append(ROUTE2096)
ROUTE2097 = x3d.ROUTE()
ROUTE2097.fromField = "fraction_changed"
ROUTE2097.fromNode = "StopTimer"
ROUTE2097.toField = "set_fraction"
ROUTE2097.toNode = "Stop_l_pinky1_RotationInterpolator"

Group1942.children.append(ROUTE2097)
ROUTE2098 = x3d.ROUTE()
ROUTE2098.fromField = "fraction_changed"
ROUTE2098.fromNode = "StopTimer"
ROUTE2098.toField = "set_fraction"
ROUTE2098.toNode = "Stop_l_pinky2_RotationInterpolator"

Group1942.children.append(ROUTE2098)
ROUTE2099 = x3d.ROUTE()
ROUTE2099.fromField = "fraction_changed"
ROUTE2099.fromNode = "StopTimer"
ROUTE2099.toField = "set_fraction"
ROUTE2099.toNode = "Stop_l_pinky3_RotationInterpolator"

Group1942.children.append(ROUTE2099)
ROUTE2100 = x3d.ROUTE()
ROUTE2100.fromField = "fraction_changed"
ROUTE2100.fromNode = "StopTimer"
ROUTE2100.toField = "set_fraction"
ROUTE2100.toNode = "Stop_r_sternoclavicular_RotationInterpolator"

Group1942.children.append(ROUTE2100)
ROUTE2101 = x3d.ROUTE()
ROUTE2101.fromField = "fraction_changed"
ROUTE2101.fromNode = "StopTimer"
ROUTE2101.toField = "set_fraction"
ROUTE2101.toNode = "Stop_r_acromioclavicular_RotationInterpolator"

Group1942.children.append(ROUTE2101)
ROUTE2102 = x3d.ROUTE()
ROUTE2102.fromField = "fraction_changed"
ROUTE2102.fromNode = "StopTimer"
ROUTE2102.toField = "set_fraction"
ROUTE2102.toNode = "Stop_r_shoulder_RotationInterpolator"

Group1942.children.append(ROUTE2102)
ROUTE2103 = x3d.ROUTE()
ROUTE2103.fromField = "fraction_changed"
ROUTE2103.fromNode = "StopTimer"
ROUTE2103.toField = "set_fraction"
ROUTE2103.toNode = "Stop_r_elbow_RotationInterpolator"

Group1942.children.append(ROUTE2103)
ROUTE2104 = x3d.ROUTE()
ROUTE2104.fromField = "fraction_changed"
ROUTE2104.fromNode = "StopTimer"
ROUTE2104.toField = "set_fraction"
ROUTE2104.toNode = "Stop_r_wrist_RotationInterpolator"

Group1942.children.append(ROUTE2104)
ROUTE2105 = x3d.ROUTE()
ROUTE2105.fromField = "fraction_changed"
ROUTE2105.fromNode = "StopTimer"
ROUTE2105.toField = "set_fraction"
ROUTE2105.toNode = "Stop_r_thumb1_RotationInterpolator"

Group1942.children.append(ROUTE2105)
ROUTE2106 = x3d.ROUTE()
ROUTE2106.fromField = "fraction_changed"
ROUTE2106.fromNode = "StopTimer"
ROUTE2106.toField = "set_fraction"
ROUTE2106.toNode = "Stop_r_thumb2_RotationInterpolator"

Group1942.children.append(ROUTE2106)
ROUTE2107 = x3d.ROUTE()
ROUTE2107.fromField = "fraction_changed"
ROUTE2107.fromNode = "StopTimer"
ROUTE2107.toField = "set_fraction"
ROUTE2107.toNode = "Stop_r_thumb3_RotationInterpolator"

Group1942.children.append(ROUTE2107)
ROUTE2108 = x3d.ROUTE()
ROUTE2108.fromField = "fraction_changed"
ROUTE2108.fromNode = "StopTimer"
ROUTE2108.toField = "set_fraction"
ROUTE2108.toNode = "Stop_r_index0_RotationInterpolator"

Group1942.children.append(ROUTE2108)
ROUTE2109 = x3d.ROUTE()
ROUTE2109.fromField = "fraction_changed"
ROUTE2109.fromNode = "StopTimer"
ROUTE2109.toField = "set_fraction"
ROUTE2109.toNode = "Stop_r_index1_RotationInterpolator"

Group1942.children.append(ROUTE2109)
ROUTE2110 = x3d.ROUTE()
ROUTE2110.fromField = "fraction_changed"
ROUTE2110.fromNode = "StopTimer"
ROUTE2110.toField = "set_fraction"
ROUTE2110.toNode = "Stop_r_index2_RotationInterpolator"

Group1942.children.append(ROUTE2110)
ROUTE2111 = x3d.ROUTE()
ROUTE2111.fromField = "fraction_changed"
ROUTE2111.fromNode = "StopTimer"
ROUTE2111.toField = "set_fraction"
ROUTE2111.toNode = "Stop_r_index3_RotationInterpolator"

Group1942.children.append(ROUTE2111)
ROUTE2112 = x3d.ROUTE()
ROUTE2112.fromField = "fraction_changed"
ROUTE2112.fromNode = "StopTimer"
ROUTE2112.toField = "set_fraction"
ROUTE2112.toNode = "Stop_r_middle0_RotationInterpolator"

Group1942.children.append(ROUTE2112)
ROUTE2113 = x3d.ROUTE()
ROUTE2113.fromField = "fraction_changed"
ROUTE2113.fromNode = "StopTimer"
ROUTE2113.toField = "set_fraction"
ROUTE2113.toNode = "Stop_r_middle1_RotationInterpolator"

Group1942.children.append(ROUTE2113)
ROUTE2114 = x3d.ROUTE()
ROUTE2114.fromField = "fraction_changed"
ROUTE2114.fromNode = "StopTimer"
ROUTE2114.toField = "set_fraction"
ROUTE2114.toNode = "Stop_r_middle2_RotationInterpolator"

Group1942.children.append(ROUTE2114)
ROUTE2115 = x3d.ROUTE()
ROUTE2115.fromField = "fraction_changed"
ROUTE2115.fromNode = "StopTimer"
ROUTE2115.toField = "set_fraction"
ROUTE2115.toNode = "Stop_r_middle3_RotationInterpolator"

Group1942.children.append(ROUTE2115)
ROUTE2116 = x3d.ROUTE()
ROUTE2116.fromField = "fraction_changed"
ROUTE2116.fromNode = "StopTimer"
ROUTE2116.toField = "set_fraction"
ROUTE2116.toNode = "Stop_r_ring0_RotationInterpolator"

Group1942.children.append(ROUTE2116)
ROUTE2117 = x3d.ROUTE()
ROUTE2117.fromField = "fraction_changed"
ROUTE2117.fromNode = "StopTimer"
ROUTE2117.toField = "set_fraction"
ROUTE2117.toNode = "Stop_r_ring1_RotationInterpolator"

Group1942.children.append(ROUTE2117)
ROUTE2118 = x3d.ROUTE()
ROUTE2118.fromField = "fraction_changed"
ROUTE2118.fromNode = "StopTimer"
ROUTE2118.toField = "set_fraction"
ROUTE2118.toNode = "Stop_r_ring2_RotationInterpolator"

Group1942.children.append(ROUTE2118)
ROUTE2119 = x3d.ROUTE()
ROUTE2119.fromField = "fraction_changed"
ROUTE2119.fromNode = "StopTimer"
ROUTE2119.toField = "set_fraction"
ROUTE2119.toNode = "Stop_r_ring3_RotationInterpolator"

Group1942.children.append(ROUTE2119)
ROUTE2120 = x3d.ROUTE()
ROUTE2120.fromField = "fraction_changed"
ROUTE2120.fromNode = "StopTimer"
ROUTE2120.toField = "set_fraction"
ROUTE2120.toNode = "Stop_r_pinky0_RotationInterpolator"

Group1942.children.append(ROUTE2120)
ROUTE2121 = x3d.ROUTE()
ROUTE2121.fromField = "fraction_changed"
ROUTE2121.fromNode = "StopTimer"
ROUTE2121.toField = "set_fraction"
ROUTE2121.toNode = "Stop_r_pinky1_RotationInterpolator"

Group1942.children.append(ROUTE2121)
ROUTE2122 = x3d.ROUTE()
ROUTE2122.fromField = "fraction_changed"
ROUTE2122.fromNode = "StopTimer"
ROUTE2122.toField = "set_fraction"
ROUTE2122.toNode = "Stop_r_pinky2_RotationInterpolator"

Group1942.children.append(ROUTE2122)
ROUTE2123 = x3d.ROUTE()
ROUTE2123.fromField = "fraction_changed"
ROUTE2123.fromNode = "StopTimer"
ROUTE2123.toField = "set_fraction"
ROUTE2123.toNode = "Stop_r_pinky3_RotationInterpolator"

Group1942.children.append(ROUTE2123)
ROUTE2124 = x3d.ROUTE()
ROUTE2124.fromField = "value_changed"
ROUTE2124.fromNode = "Stop_humanoid_root_TranslationInterpolator"
ROUTE2124.toField = "translation"
ROUTE2124.toNode = "hanim_humanoid_root"

Group1942.children.append(ROUTE2124)
ROUTE2125 = x3d.ROUTE()
ROUTE2125.fromField = "value_changed"
ROUTE2125.fromNode = "Stop_humanoid_root_RotationInterpolator"
ROUTE2125.toField = "rotation"
ROUTE2125.toNode = "hanim_humanoid_root"

Group1942.children.append(ROUTE2125)
ROUTE2126 = x3d.ROUTE()
ROUTE2126.fromField = "value_changed"
ROUTE2126.fromNode = "Stop_sacroiliac_RotationInterpolator"
ROUTE2126.toField = "rotation"
ROUTE2126.toNode = "hanim_sacroiliac"

Group1942.children.append(ROUTE2126)
ROUTE2127 = x3d.ROUTE()
ROUTE2127.fromField = "value_changed"
ROUTE2127.fromNode = "Stop_l_hip_RotationInterpolator"
ROUTE2127.toField = "rotation"
ROUTE2127.toNode = "hanim_l_hip"

Group1942.children.append(ROUTE2127)
ROUTE2128 = x3d.ROUTE()
ROUTE2128.fromField = "value_changed"
ROUTE2128.fromNode = "Stop_l_knee_RotationInterpolator"
ROUTE2128.toField = "rotation"
ROUTE2128.toNode = "hanim_l_knee"

Group1942.children.append(ROUTE2128)
ROUTE2129 = x3d.ROUTE()
ROUTE2129.fromField = "value_changed"
ROUTE2129.fromNode = "Stop_l_ankle_RotationInterpolator"
ROUTE2129.toField = "rotation"
ROUTE2129.toNode = "hanim_l_ankle"

Group1942.children.append(ROUTE2129)
ROUTE2130 = x3d.ROUTE()
ROUTE2130.fromField = "value_changed"
ROUTE2130.fromNode = "Stop_l_subtalar_RotationInterpolator"
ROUTE2130.toField = "rotation"
ROUTE2130.toNode = "hanim_l_subtalar"

Group1942.children.append(ROUTE2130)
ROUTE2131 = x3d.ROUTE()
ROUTE2131.fromField = "value_changed"
ROUTE2131.fromNode = "Stop_l_midtarsal_RotationInterpolator"
ROUTE2131.toField = "rotation"
ROUTE2131.toNode = "hanim_l_midtarsal"

Group1942.children.append(ROUTE2131)
ROUTE2132 = x3d.ROUTE()
ROUTE2132.fromField = "value_changed"
ROUTE2132.fromNode = "Stop_l_metatarsal_RotationInterpolator"
ROUTE2132.toField = "rotation"
ROUTE2132.toNode = "hanim_l_metatarsal"

Group1942.children.append(ROUTE2132)
ROUTE2133 = x3d.ROUTE()
ROUTE2133.fromField = "value_changed"
ROUTE2133.fromNode = "Stop_r_hip_RotationInterpolator"
ROUTE2133.toField = "rotation"
ROUTE2133.toNode = "hanim_r_hip"

Group1942.children.append(ROUTE2133)
ROUTE2134 = x3d.ROUTE()
ROUTE2134.fromField = "value_changed"
ROUTE2134.fromNode = "Stop_r_knee_RotationInterpolator"
ROUTE2134.toField = "rotation"
ROUTE2134.toNode = "hanim_r_knee"

Group1942.children.append(ROUTE2134)
ROUTE2135 = x3d.ROUTE()
ROUTE2135.fromField = "value_changed"
ROUTE2135.fromNode = "Stop_r_ankle_RotationInterpolator"
ROUTE2135.toField = "rotation"
ROUTE2135.toNode = "hanim_r_ankle"

Group1942.children.append(ROUTE2135)
ROUTE2136 = x3d.ROUTE()
ROUTE2136.fromField = "value_changed"
ROUTE2136.fromNode = "Stop_r_subtalar_RotationInterpolator"
ROUTE2136.toField = "rotation"
ROUTE2136.toNode = "hanim_r_subtalar"

Group1942.children.append(ROUTE2136)
ROUTE2137 = x3d.ROUTE()
ROUTE2137.fromField = "value_changed"
ROUTE2137.fromNode = "Stop_r_midtarsal_RotationInterpolator"
ROUTE2137.toField = "rotation"
ROUTE2137.toNode = "hanim_r_midtarsal"

Group1942.children.append(ROUTE2137)
ROUTE2138 = x3d.ROUTE()
ROUTE2138.fromField = "value_changed"
ROUTE2138.fromNode = "Stop_r_metatarsal_RotationInterpolator"
ROUTE2138.toField = "rotation"
ROUTE2138.toNode = "hanim_r_metatarsal"

Group1942.children.append(ROUTE2138)
ROUTE2139 = x3d.ROUTE()
ROUTE2139.fromField = "value_changed"
ROUTE2139.fromNode = "Stop_vl5_RotationInterpolator"
ROUTE2139.toField = "rotation"
ROUTE2139.toNode = "hanim_vl5"

Group1942.children.append(ROUTE2139)
ROUTE2140 = x3d.ROUTE()
ROUTE2140.fromField = "value_changed"
ROUTE2140.fromNode = "Stop_vl4_RotationInterpolator"
ROUTE2140.toField = "rotation"
ROUTE2140.toNode = "hanim_vl4"

Group1942.children.append(ROUTE2140)
ROUTE2141 = x3d.ROUTE()
ROUTE2141.fromField = "value_changed"
ROUTE2141.fromNode = "Stop_vl3_RotationInterpolator"
ROUTE2141.toField = "rotation"
ROUTE2141.toNode = "hanim_vl3"

Group1942.children.append(ROUTE2141)
ROUTE2142 = x3d.ROUTE()
ROUTE2142.fromField = "value_changed"
ROUTE2142.fromNode = "Stop_vl2_RotationInterpolator"
ROUTE2142.toField = "rotation"
ROUTE2142.toNode = "hanim_vl2"

Group1942.children.append(ROUTE2142)
ROUTE2143 = x3d.ROUTE()
ROUTE2143.fromField = "value_changed"
ROUTE2143.fromNode = "Stop_vl1_RotationInterpolator"
ROUTE2143.toField = "rotation"
ROUTE2143.toNode = "hanim_vl1"

Group1942.children.append(ROUTE2143)
ROUTE2144 = x3d.ROUTE()
ROUTE2144.fromField = "value_changed"
ROUTE2144.fromNode = "Stop_vt12_RotationInterpolator"
ROUTE2144.toField = "rotation"
ROUTE2144.toNode = "hanim_vt12"

Group1942.children.append(ROUTE2144)
ROUTE2145 = x3d.ROUTE()
ROUTE2145.fromField = "value_changed"
ROUTE2145.fromNode = "Stop_vt11_RotationInterpolator"
ROUTE2145.toField = "rotation"
ROUTE2145.toNode = "hanim_vt11"

Group1942.children.append(ROUTE2145)
ROUTE2146 = x3d.ROUTE()
ROUTE2146.fromField = "value_changed"
ROUTE2146.fromNode = "Stop_vt10_RotationInterpolator"
ROUTE2146.toField = "rotation"
ROUTE2146.toNode = "hanim_vt10"

Group1942.children.append(ROUTE2146)
ROUTE2147 = x3d.ROUTE()
ROUTE2147.fromField = "value_changed"
ROUTE2147.fromNode = "Stop_vt9_RotationInterpolator"
ROUTE2147.toField = "rotation"
ROUTE2147.toNode = "hanim_vt9"

Group1942.children.append(ROUTE2147)
ROUTE2148 = x3d.ROUTE()
ROUTE2148.fromField = "value_changed"
ROUTE2148.fromNode = "Stop_vt8_RotationInterpolator"
ROUTE2148.toField = "rotation"
ROUTE2148.toNode = "hanim_vt8"

Group1942.children.append(ROUTE2148)
ROUTE2149 = x3d.ROUTE()
ROUTE2149.fromField = "value_changed"
ROUTE2149.fromNode = "Stop_vt7_RotationInterpolator"
ROUTE2149.toField = "rotation"
ROUTE2149.toNode = "hanim_vt7"

Group1942.children.append(ROUTE2149)
ROUTE2150 = x3d.ROUTE()
ROUTE2150.fromField = "value_changed"
ROUTE2150.fromNode = "Stop_vt6_RotationInterpolator"
ROUTE2150.toField = "rotation"
ROUTE2150.toNode = "hanim_vt6"

Group1942.children.append(ROUTE2150)
ROUTE2151 = x3d.ROUTE()
ROUTE2151.fromField = "value_changed"
ROUTE2151.fromNode = "Stop_vt5_RotationInterpolator"
ROUTE2151.toField = "rotation"
ROUTE2151.toNode = "hanim_vt5"

Group1942.children.append(ROUTE2151)
ROUTE2152 = x3d.ROUTE()
ROUTE2152.fromField = "value_changed"
ROUTE2152.fromNode = "Stop_vt4_RotationInterpolator"
ROUTE2152.toField = "rotation"
ROUTE2152.toNode = "hanim_vt4"

Group1942.children.append(ROUTE2152)
ROUTE2153 = x3d.ROUTE()
ROUTE2153.fromField = "value_changed"
ROUTE2153.fromNode = "Stop_vt3_RotationInterpolator"
ROUTE2153.toField = "rotation"
ROUTE2153.toNode = "hanim_vt3"

Group1942.children.append(ROUTE2153)
ROUTE2154 = x3d.ROUTE()
ROUTE2154.fromField = "value_changed"
ROUTE2154.fromNode = "Stop_vt2_RotationInterpolator"
ROUTE2154.toField = "rotation"
ROUTE2154.toNode = "hanim_vt2"

Group1942.children.append(ROUTE2154)
ROUTE2155 = x3d.ROUTE()
ROUTE2155.fromField = "value_changed"
ROUTE2155.fromNode = "Stop_vt1_RotationInterpolator"
ROUTE2155.toField = "rotation"
ROUTE2155.toNode = "hanim_vt1"

Group1942.children.append(ROUTE2155)
ROUTE2156 = x3d.ROUTE()
ROUTE2156.fromField = "value_changed"
ROUTE2156.fromNode = "Stop_vc7_RotationInterpolator"
ROUTE2156.toField = "rotation"
ROUTE2156.toNode = "hanim_vc7"

Group1942.children.append(ROUTE2156)
ROUTE2157 = x3d.ROUTE()
ROUTE2157.fromField = "value_changed"
ROUTE2157.fromNode = "Stop_vc6_RotationInterpolator"
ROUTE2157.toField = "rotation"
ROUTE2157.toNode = "hanim_vc6"

Group1942.children.append(ROUTE2157)
ROUTE2158 = x3d.ROUTE()
ROUTE2158.fromField = "value_changed"
ROUTE2158.fromNode = "Stop_vc5_RotationInterpolator"
ROUTE2158.toField = "rotation"
ROUTE2158.toNode = "hanim_vc5"

Group1942.children.append(ROUTE2158)
ROUTE2159 = x3d.ROUTE()
ROUTE2159.fromField = "value_changed"
ROUTE2159.fromNode = "Stop_vc4_RotationInterpolator"
ROUTE2159.toField = "rotation"
ROUTE2159.toNode = "hanim_vc4"

Group1942.children.append(ROUTE2159)
ROUTE2160 = x3d.ROUTE()
ROUTE2160.fromField = "value_changed"
ROUTE2160.fromNode = "Stop_vc3_RotationInterpolator"
ROUTE2160.toField = "rotation"
ROUTE2160.toNode = "hanim_vc3"

Group1942.children.append(ROUTE2160)
ROUTE2161 = x3d.ROUTE()
ROUTE2161.fromField = "value_changed"
ROUTE2161.fromNode = "Stop_vc2_RotationInterpolator"
ROUTE2161.toField = "rotation"
ROUTE2161.toNode = "hanim_vc2"

Group1942.children.append(ROUTE2161)
ROUTE2162 = x3d.ROUTE()
ROUTE2162.fromField = "value_changed"
ROUTE2162.fromNode = "Stop_vc1_RotationInterpolator"
ROUTE2162.toField = "rotation"
ROUTE2162.toNode = "hanim_vc1"

Group1942.children.append(ROUTE2162)
ROUTE2163 = x3d.ROUTE()
ROUTE2163.fromField = "value_changed"
ROUTE2163.fromNode = "Stop_skullbase_RotationInterpolator"
ROUTE2163.toField = "rotation"
ROUTE2163.toNode = "hanim_skullbase"

Group1942.children.append(ROUTE2163)
ROUTE2164 = x3d.ROUTE()
ROUTE2164.fromField = "value_changed"
ROUTE2164.fromNode = "Stop_l_eyeball_joint_RotationInterpolator"
ROUTE2164.toField = "rotation"
ROUTE2164.toNode = "hanim_l_eyeball_joint"

Group1942.children.append(ROUTE2164)
ROUTE2165 = x3d.ROUTE()
ROUTE2165.fromField = "value_changed"
ROUTE2165.fromNode = "Stop_r_eyeball_joint_RotationInterpolator"
ROUTE2165.toField = "rotation"
ROUTE2165.toNode = "hanim_r_eyeball_joint"

Group1942.children.append(ROUTE2165)
ROUTE2166 = x3d.ROUTE()
ROUTE2166.fromField = "value_changed"
ROUTE2166.fromNode = "Stop_l_sternoclavicular_RotationInterpolator"
ROUTE2166.toField = "rotation"
ROUTE2166.toNode = "hanim_l_sternoclavicular"

Group1942.children.append(ROUTE2166)
ROUTE2167 = x3d.ROUTE()
ROUTE2167.fromField = "value_changed"
ROUTE2167.fromNode = "Stop_l_acromioclavicular_RotationInterpolator"
ROUTE2167.toField = "rotation"
ROUTE2167.toNode = "hanim_l_acromioclavicular"

Group1942.children.append(ROUTE2167)
ROUTE2168 = x3d.ROUTE()
ROUTE2168.fromField = "value_changed"
ROUTE2168.fromNode = "Stop_l_shoulder_RotationInterpolator"
ROUTE2168.toField = "rotation"
ROUTE2168.toNode = "hanim_l_shoulder"

Group1942.children.append(ROUTE2168)
ROUTE2169 = x3d.ROUTE()
ROUTE2169.fromField = "value_changed"
ROUTE2169.fromNode = "Stop_l_elbow_RotationInterpolator"
ROUTE2169.toField = "rotation"
ROUTE2169.toNode = "hanim_l_elbow"

Group1942.children.append(ROUTE2169)
ROUTE2170 = x3d.ROUTE()
ROUTE2170.fromField = "value_changed"
ROUTE2170.fromNode = "Stop_l_wrist_RotationInterpolator"
ROUTE2170.toField = "rotation"
ROUTE2170.toNode = "hanim_l_wrist"

Group1942.children.append(ROUTE2170)
ROUTE2171 = x3d.ROUTE()
ROUTE2171.fromField = "value_changed"
ROUTE2171.fromNode = "Stop_l_thumb1_RotationInterpolator"
ROUTE2171.toField = "rotation"
ROUTE2171.toNode = "hanim_l_thumb1"

Group1942.children.append(ROUTE2171)
ROUTE2172 = x3d.ROUTE()
ROUTE2172.fromField = "value_changed"
ROUTE2172.fromNode = "Stop_l_thumb2_RotationInterpolator"
ROUTE2172.toField = "rotation"
ROUTE2172.toNode = "hanim_l_thumb2"

Group1942.children.append(ROUTE2172)
ROUTE2173 = x3d.ROUTE()
ROUTE2173.fromField = "value_changed"
ROUTE2173.fromNode = "Stop_l_thumb3_RotationInterpolator"
ROUTE2173.toField = "rotation"
ROUTE2173.toNode = "hanim_l_thumb3"

Group1942.children.append(ROUTE2173)
ROUTE2174 = x3d.ROUTE()
ROUTE2174.fromField = "value_changed"
ROUTE2174.fromNode = "Stop_l_index0_RotationInterpolator"
ROUTE2174.toField = "rotation"
ROUTE2174.toNode = "hanim_l_index0"

Group1942.children.append(ROUTE2174)
ROUTE2175 = x3d.ROUTE()
ROUTE2175.fromField = "value_changed"
ROUTE2175.fromNode = "Stop_l_index1_RotationInterpolator"
ROUTE2175.toField = "rotation"
ROUTE2175.toNode = "hanim_l_index1"

Group1942.children.append(ROUTE2175)
ROUTE2176 = x3d.ROUTE()
ROUTE2176.fromField = "value_changed"
ROUTE2176.fromNode = "Stop_l_index2_RotationInterpolator"
ROUTE2176.toField = "rotation"
ROUTE2176.toNode = "hanim_l_index2"

Group1942.children.append(ROUTE2176)
ROUTE2177 = x3d.ROUTE()
ROUTE2177.fromField = "value_changed"
ROUTE2177.fromNode = "Stop_l_index3_RotationInterpolator"
ROUTE2177.toField = "rotation"
ROUTE2177.toNode = "hanim_l_index3"

Group1942.children.append(ROUTE2177)
ROUTE2178 = x3d.ROUTE()
ROUTE2178.fromField = "value_changed"
ROUTE2178.fromNode = "Stop_l_middle0_RotationInterpolator"
ROUTE2178.toField = "rotation"
ROUTE2178.toNode = "hanim_l_middle0"

Group1942.children.append(ROUTE2178)
ROUTE2179 = x3d.ROUTE()
ROUTE2179.fromField = "value_changed"
ROUTE2179.fromNode = "Stop_l_middle1_RotationInterpolator"
ROUTE2179.toField = "rotation"
ROUTE2179.toNode = "hanim_l_middle1"

Group1942.children.append(ROUTE2179)
ROUTE2180 = x3d.ROUTE()
ROUTE2180.fromField = "value_changed"
ROUTE2180.fromNode = "Stop_l_middle2_RotationInterpolator"
ROUTE2180.toField = "rotation"
ROUTE2180.toNode = "hanim_l_middle2"

Group1942.children.append(ROUTE2180)
ROUTE2181 = x3d.ROUTE()
ROUTE2181.fromField = "value_changed"
ROUTE2181.fromNode = "Stop_l_middle3_RotationInterpolator"
ROUTE2181.toField = "rotation"
ROUTE2181.toNode = "hanim_l_middle3"

Group1942.children.append(ROUTE2181)
ROUTE2182 = x3d.ROUTE()
ROUTE2182.fromField = "value_changed"
ROUTE2182.fromNode = "Stop_l_ring0_RotationInterpolator"
ROUTE2182.toField = "rotation"
ROUTE2182.toNode = "hanim_l_ring0"

Group1942.children.append(ROUTE2182)
ROUTE2183 = x3d.ROUTE()
ROUTE2183.fromField = "value_changed"
ROUTE2183.fromNode = "Stop_l_ring1_RotationInterpolator"
ROUTE2183.toField = "rotation"
ROUTE2183.toNode = "hanim_l_ring1"

Group1942.children.append(ROUTE2183)
ROUTE2184 = x3d.ROUTE()
ROUTE2184.fromField = "value_changed"
ROUTE2184.fromNode = "Stop_l_ring2_RotationInterpolator"
ROUTE2184.toField = "rotation"
ROUTE2184.toNode = "hanim_l_ring2"

Group1942.children.append(ROUTE2184)
ROUTE2185 = x3d.ROUTE()
ROUTE2185.fromField = "value_changed"
ROUTE2185.fromNode = "Stop_l_ring3_RotationInterpolator"
ROUTE2185.toField = "rotation"
ROUTE2185.toNode = "hanim_l_ring3"

Group1942.children.append(ROUTE2185)
ROUTE2186 = x3d.ROUTE()
ROUTE2186.fromField = "value_changed"
ROUTE2186.fromNode = "Stop_l_pinky0_RotationInterpolator"
ROUTE2186.toField = "rotation"
ROUTE2186.toNode = "hanim_l_pinky0"

Group1942.children.append(ROUTE2186)
ROUTE2187 = x3d.ROUTE()
ROUTE2187.fromField = "value_changed"
ROUTE2187.fromNode = "Stop_l_pinky1_RotationInterpolator"
ROUTE2187.toField = "rotation"
ROUTE2187.toNode = "hanim_l_pinky1"

Group1942.children.append(ROUTE2187)
ROUTE2188 = x3d.ROUTE()
ROUTE2188.fromField = "value_changed"
ROUTE2188.fromNode = "Stop_l_pinky2_RotationInterpolator"
ROUTE2188.toField = "rotation"
ROUTE2188.toNode = "hanim_l_pinky2"

Group1942.children.append(ROUTE2188)
ROUTE2189 = x3d.ROUTE()
ROUTE2189.fromField = "value_changed"
ROUTE2189.fromNode = "Stop_l_pinky3_RotationInterpolator"
ROUTE2189.toField = "rotation"
ROUTE2189.toNode = "hanim_l_pinky3"

Group1942.children.append(ROUTE2189)
ROUTE2190 = x3d.ROUTE()
ROUTE2190.fromField = "value_changed"
ROUTE2190.fromNode = "Stop_r_sternoclavicular_RotationInterpolator"
ROUTE2190.toField = "rotation"
ROUTE2190.toNode = "hanim_r_sternoclavicular"

Group1942.children.append(ROUTE2190)
ROUTE2191 = x3d.ROUTE()
ROUTE2191.fromField = "value_changed"
ROUTE2191.fromNode = "Stop_r_acromioclavicular_RotationInterpolator"
ROUTE2191.toField = "rotation"
ROUTE2191.toNode = "hanim_r_acromioclavicular"

Group1942.children.append(ROUTE2191)
ROUTE2192 = x3d.ROUTE()
ROUTE2192.fromField = "value_changed"
ROUTE2192.fromNode = "Stop_r_shoulder_RotationInterpolator"
ROUTE2192.toField = "rotation"
ROUTE2192.toNode = "hanim_r_shoulder"

Group1942.children.append(ROUTE2192)
ROUTE2193 = x3d.ROUTE()
ROUTE2193.fromField = "value_changed"
ROUTE2193.fromNode = "Stop_r_elbow_RotationInterpolator"
ROUTE2193.toField = "rotation"
ROUTE2193.toNode = "hanim_r_elbow"

Group1942.children.append(ROUTE2193)
ROUTE2194 = x3d.ROUTE()
ROUTE2194.fromField = "value_changed"
ROUTE2194.fromNode = "Stop_r_wrist_RotationInterpolator"
ROUTE2194.toField = "rotation"
ROUTE2194.toNode = "hanim_r_wrist"

Group1942.children.append(ROUTE2194)
ROUTE2195 = x3d.ROUTE()
ROUTE2195.fromField = "value_changed"
ROUTE2195.fromNode = "Stop_r_thumb1_RotationInterpolator"
ROUTE2195.toField = "rotation"
ROUTE2195.toNode = "hanim_r_thumb1"

Group1942.children.append(ROUTE2195)
ROUTE2196 = x3d.ROUTE()
ROUTE2196.fromField = "value_changed"
ROUTE2196.fromNode = "Stop_r_thumb2_RotationInterpolator"
ROUTE2196.toField = "rotation"
ROUTE2196.toNode = "hanim_r_thumb2"

Group1942.children.append(ROUTE2196)
ROUTE2197 = x3d.ROUTE()
ROUTE2197.fromField = "value_changed"
ROUTE2197.fromNode = "Stop_r_thumb3_RotationInterpolator"
ROUTE2197.toField = "rotation"
ROUTE2197.toNode = "hanim_r_thumb3"

Group1942.children.append(ROUTE2197)
ROUTE2198 = x3d.ROUTE()
ROUTE2198.fromField = "value_changed"
ROUTE2198.fromNode = "Stop_r_index0_RotationInterpolator"
ROUTE2198.toField = "rotation"
ROUTE2198.toNode = "hanim_r_index0"

Group1942.children.append(ROUTE2198)
ROUTE2199 = x3d.ROUTE()
ROUTE2199.fromField = "value_changed"
ROUTE2199.fromNode = "Stop_r_index1_RotationInterpolator"
ROUTE2199.toField = "rotation"
ROUTE2199.toNode = "hanim_r_index1"

Group1942.children.append(ROUTE2199)
ROUTE2200 = x3d.ROUTE()
ROUTE2200.fromField = "value_changed"
ROUTE2200.fromNode = "Stop_r_index2_RotationInterpolator"
ROUTE2200.toField = "rotation"
ROUTE2200.toNode = "hanim_r_index2"

Group1942.children.append(ROUTE2200)
ROUTE2201 = x3d.ROUTE()
ROUTE2201.fromField = "value_changed"
ROUTE2201.fromNode = "Stop_r_index3_RotationInterpolator"
ROUTE2201.toField = "rotation"
ROUTE2201.toNode = "hanim_r_index3"

Group1942.children.append(ROUTE2201)
ROUTE2202 = x3d.ROUTE()
ROUTE2202.fromField = "value_changed"
ROUTE2202.fromNode = "Stop_r_middle0_RotationInterpolator"
ROUTE2202.toField = "rotation"
ROUTE2202.toNode = "hanim_r_middle0"

Group1942.children.append(ROUTE2202)
ROUTE2203 = x3d.ROUTE()
ROUTE2203.fromField = "value_changed"
ROUTE2203.fromNode = "Stop_r_middle1_RotationInterpolator"
ROUTE2203.toField = "rotation"
ROUTE2203.toNode = "hanim_r_middle1"

Group1942.children.append(ROUTE2203)
ROUTE2204 = x3d.ROUTE()
ROUTE2204.fromField = "value_changed"
ROUTE2204.fromNode = "Stop_r_middle2_RotationInterpolator"
ROUTE2204.toField = "rotation"
ROUTE2204.toNode = "hanim_r_middle2"

Group1942.children.append(ROUTE2204)
ROUTE2205 = x3d.ROUTE()
ROUTE2205.fromField = "value_changed"
ROUTE2205.fromNode = "Stop_r_middle3_RotationInterpolator"
ROUTE2205.toField = "rotation"
ROUTE2205.toNode = "hanim_r_middle3"

Group1942.children.append(ROUTE2205)
ROUTE2206 = x3d.ROUTE()
ROUTE2206.fromField = "value_changed"
ROUTE2206.fromNode = "Stop_r_ring0_RotationInterpolator"
ROUTE2206.toField = "rotation"
ROUTE2206.toNode = "hanim_r_ring0"

Group1942.children.append(ROUTE2206)
ROUTE2207 = x3d.ROUTE()
ROUTE2207.fromField = "value_changed"
ROUTE2207.fromNode = "Stop_r_ring1_RotationInterpolator"
ROUTE2207.toField = "rotation"
ROUTE2207.toNode = "hanim_r_ring1"

Group1942.children.append(ROUTE2207)
ROUTE2208 = x3d.ROUTE()
ROUTE2208.fromField = "value_changed"
ROUTE2208.fromNode = "Stop_r_ring2_RotationInterpolator"
ROUTE2208.toField = "rotation"
ROUTE2208.toNode = "hanim_r_ring2"

Group1942.children.append(ROUTE2208)
ROUTE2209 = x3d.ROUTE()
ROUTE2209.fromField = "value_changed"
ROUTE2209.fromNode = "Stop_r_ring3_RotationInterpolator"
ROUTE2209.toField = "rotation"
ROUTE2209.toNode = "hanim_r_ring3"

Group1942.children.append(ROUTE2209)
ROUTE2210 = x3d.ROUTE()
ROUTE2210.fromField = "value_changed"
ROUTE2210.fromNode = "Stop_r_pinky0_RotationInterpolator"
ROUTE2210.toField = "rotation"
ROUTE2210.toNode = "hanim_r_pinky0"

Group1942.children.append(ROUTE2210)
ROUTE2211 = x3d.ROUTE()
ROUTE2211.fromField = "value_changed"
ROUTE2211.fromNode = "Stop_r_pinky1_RotationInterpolator"
ROUTE2211.toField = "rotation"
ROUTE2211.toNode = "hanim_r_pinky1"

Group1942.children.append(ROUTE2211)
ROUTE2212 = x3d.ROUTE()
ROUTE2212.fromField = "value_changed"
ROUTE2212.fromNode = "Stop_r_pinky2_RotationInterpolator"
ROUTE2212.toField = "rotation"
ROUTE2212.toNode = "hanim_r_pinky2"

Group1942.children.append(ROUTE2212)
ROUTE2213 = x3d.ROUTE()
ROUTE2213.fromField = "value_changed"
ROUTE2213.fromNode = "Stop_r_pinky3_RotationInterpolator"
ROUTE2213.toField = "rotation"
ROUTE2213.toNode = "hanim_r_pinky3"

Group1942.children.append(ROUTE2213)

Scene30.children.append(Group1942)
Group2214 = x3d.Group()
Group2214.DEF = "StandAnimation"
TimeSensor2215 = x3d.TimeSensor()
TimeSensor2215.DEF = "StandTimer"
TimeSensor2215.cycleInterval = 5.73
TimeSensor2215.loop = True

Group2214.children.append(TimeSensor2215)
OrientationInterpolator2216 = x3d.OrientationInterpolator()
OrientationInterpolator2216.DEF = "Stand_r_metatarsal_PitchInterpolator"
OrientationInterpolator2216.key = [0,0.2,0.4,0.6,0.7,1]
OrientationInterpolator2216.keyValue = (1.0000,0.0000,0.0000,0.0000,-1.0000,0.0000,0.0000,0.0150,1.0000,0.0000,0.0000,0.1700,-1.0000,0.0000,0.0000,0.0250,1.0000,0.0000,0.0000,0.0100,1.0000,0.0000,0.0000,0.0000)

Group2214.children.append(OrientationInterpolator2216)
OrientationInterpolator2217 = x3d.OrientationInterpolator()
OrientationInterpolator2217.DEF = "Stand_r_ankle_RotationInterpolator"
OrientationInterpolator2217.key = [0,0.5,1]
OrientationInterpolator2217.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2214.children.append(OrientationInterpolator2217)
OrientationInterpolator2218 = x3d.OrientationInterpolator()
OrientationInterpolator2218.DEF = "Stand_r_knee_RotationInterpolator"
OrientationInterpolator2218.key = [0,0.5,1]
OrientationInterpolator2218.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2214.children.append(OrientationInterpolator2218)
OrientationInterpolator2219 = x3d.OrientationInterpolator()
OrientationInterpolator2219.DEF = "Stand_r_hip_RotationInterpolator"
OrientationInterpolator2219.key = [0,0.5,1]
OrientationInterpolator2219.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2214.children.append(OrientationInterpolator2219)
OrientationInterpolator2220 = x3d.OrientationInterpolator()
OrientationInterpolator2220.DEF = "Stand_l_ankle_RotationInterpolator"
OrientationInterpolator2220.key = [0,0.5,1]
OrientationInterpolator2220.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2214.children.append(OrientationInterpolator2220)
OrientationInterpolator2221 = x3d.OrientationInterpolator()
OrientationInterpolator2221.DEF = "Stand_l_knee_RotationInterpolator"
OrientationInterpolator2221.key = [0,0.5,1]
OrientationInterpolator2221.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2214.children.append(OrientationInterpolator2221)
OrientationInterpolator2222 = x3d.OrientationInterpolator()
OrientationInterpolator2222.DEF = "Stand_l_hip_RotationInterpolator"
OrientationInterpolator2222.key = [0,0.5,1]
OrientationInterpolator2222.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2214.children.append(OrientationInterpolator2222)
OrientationInterpolator2223 = x3d.OrientationInterpolator()
OrientationInterpolator2223.DEF = "Stand_r_wrist_RotationInterpolator"
OrientationInterpolator2223.key = [0,0.5,1]
OrientationInterpolator2223.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,-1.0000,0.2500,0.0000,0.0000,1.0000,0.0000)

Group2214.children.append(OrientationInterpolator2223)
OrientationInterpolator2224 = x3d.OrientationInterpolator()
OrientationInterpolator2224.DEF = "Stand_r_elbow_RotationInterpolator"
OrientationInterpolator2224.key = [0,0.5,1]
OrientationInterpolator2224.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2214.children.append(OrientationInterpolator2224)
OrientationInterpolator2225 = x3d.OrientationInterpolator()
OrientationInterpolator2225.DEF = "Stand_r_shoulder_RotationInterpolator"
OrientationInterpolator2225.key = [0,0.5,1]
OrientationInterpolator2225.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2214.children.append(OrientationInterpolator2225)
OrientationInterpolator2226 = x3d.OrientationInterpolator()
OrientationInterpolator2226.DEF = "Stand_l_wrist_RotationInterpolator"
OrientationInterpolator2226.key = [0,0.5,1]
OrientationInterpolator2226.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2214.children.append(OrientationInterpolator2226)
OrientationInterpolator2227 = x3d.OrientationInterpolator()
OrientationInterpolator2227.DEF = "Stand_l_elbow_RotationInterpolator"
OrientationInterpolator2227.key = [0,0.5,1]
OrientationInterpolator2227.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2214.children.append(OrientationInterpolator2227)
OrientationInterpolator2228 = x3d.OrientationInterpolator()
OrientationInterpolator2228.DEF = "Stand_l_shoulder_RotationInterpolator"
OrientationInterpolator2228.key = [0,0.5,1]
OrientationInterpolator2228.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2214.children.append(OrientationInterpolator2228)
OrientationInterpolator2229 = x3d.OrientationInterpolator()
OrientationInterpolator2229.DEF = "Stand_head_RotationInterpolator"
OrientationInterpolator2229.key = [0,0.5,1]
OrientationInterpolator2229.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2214.children.append(OrientationInterpolator2229)
OrientationInterpolator2230 = x3d.OrientationInterpolator()
OrientationInterpolator2230.DEF = "Stand_neck_RotationInterpolator"
OrientationInterpolator2230.key = [0,0.5,1]
OrientationInterpolator2230.keyValue = (0.0000,0.0000,1.0000,0.0000,-1.0000,0.0000,0.0000,0.5000,0.0000,0.0000,1.0000,0.0000)

Group2214.children.append(OrientationInterpolator2230)
OrientationInterpolator2231 = x3d.OrientationInterpolator()
OrientationInterpolator2231.DEF = "Stand_l_eyeball_RotationInterpolator"
OrientationInterpolator2231.key = [0,0.4,0.7,1]
OrientationInterpolator2231.keyValue = (0.0000,0.0000,1.0000,0.0000,-1.0000,0.0000,0.0000,0.5000,1.0000,0.0000,0.0000,0.4500,0.0000,0.0000,1.0000,0.0000)

Group2214.children.append(OrientationInterpolator2231)
OrientationInterpolator2232 = x3d.OrientationInterpolator()
OrientationInterpolator2232.DEF = "Stand_r_eyeball_RotationInterpolator"
OrientationInterpolator2232.key = [0,0.4,0.7,1]
OrientationInterpolator2232.keyValue = (0.0000,0.0000,1.0000,0.0000,-1.0000,0.0000,0.0000,0.5000,1.0000,0.0000,0.0000,0.4500,0.0000,0.0000,1.0000,0.0000)

Group2214.children.append(OrientationInterpolator2232)
OrientationInterpolator2233 = x3d.OrientationInterpolator()
OrientationInterpolator2233.DEF = "Stand_lower_body_RotationInterpolator"
OrientationInterpolator2233.key = [0,0.5,1]
OrientationInterpolator2233.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2214.children.append(OrientationInterpolator2233)
OrientationInterpolator2234 = x3d.OrientationInterpolator()
OrientationInterpolator2234.DEF = "Stand_upper_body_RotationInterpolator"
OrientationInterpolator2234.key = [0,0.5,1]
OrientationInterpolator2234.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2214.children.append(OrientationInterpolator2234)
OrientationInterpolator2235 = x3d.OrientationInterpolator()
OrientationInterpolator2235.DEF = "Stand_whole_body_RotationInterpolator"
OrientationInterpolator2235.key = [0,0.5,1]
OrientationInterpolator2235.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2214.children.append(OrientationInterpolator2235)
PositionInterpolator2236 = x3d.PositionInterpolator()
PositionInterpolator2236.DEF = "Stand_whole_body_TranslationInterpolator"
PositionInterpolator2236.key = [0,0.5,1]
PositionInterpolator2236.keyValue = (0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000)

Group2214.children.append(PositionInterpolator2236)
OrientationInterpolator2237 = x3d.OrientationInterpolator()
OrientationInterpolator2237.DEF = "Stand_l_sternoclavicular_RollInterpolator"
OrientationInterpolator2237.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2237.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2214.children.append(OrientationInterpolator2237)
OrientationInterpolator2238 = x3d.OrientationInterpolator()
OrientationInterpolator2238.DEF = "Stand_l_acromioclavicular_RollInterpolator"
OrientationInterpolator2238.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2238.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2214.children.append(OrientationInterpolator2238)
OrientationInterpolator2239 = x3d.OrientationInterpolator()
OrientationInterpolator2239.DEF = "Stand_r_sternoclavicular_RollInterpolator"
OrientationInterpolator2239.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2239.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2214.children.append(OrientationInterpolator2239)
OrientationInterpolator2240 = x3d.OrientationInterpolator()
OrientationInterpolator2240.DEF = "Stand_r_acromioclavicular_RollInterpolator"
OrientationInterpolator2240.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2240.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2214.children.append(OrientationInterpolator2240)
OrientationInterpolator2241 = x3d.OrientationInterpolator()
OrientationInterpolator2241.DEF = "Stand_sacroiliac_YawInterpolator"
OrientationInterpolator2241.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2241.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2214.children.append(OrientationInterpolator2241)
OrientationInterpolator2242 = x3d.OrientationInterpolator()
OrientationInterpolator2242.DEF = "Stand_vl5_YawInterpolator"
OrientationInterpolator2242.key = [0,0.2,0.4,0.5,0.6,0.8,1]
OrientationInterpolator2242.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2214.children.append(OrientationInterpolator2242)
OrientationInterpolator2243 = x3d.OrientationInterpolator()
OrientationInterpolator2243.DEF = "Stand_vc6_YawInterpolator"
OrientationInterpolator2243.key = [0,0.2,0.4,0.5,0.6,0.8,1]
OrientationInterpolator2243.keyValue = (0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,-1.0000,0.0000,0.0000,0.0000,0.0000,-1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000)

Group2214.children.append(OrientationInterpolator2243)
OrientationInterpolator2244 = x3d.OrientationInterpolator()
OrientationInterpolator2244.DEF = "Stand_l_thumb1_PitchInterpolator"
OrientationInterpolator2244.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2244.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2214.children.append(OrientationInterpolator2244)
OrientationInterpolator2245 = x3d.OrientationInterpolator()
OrientationInterpolator2245.DEF = "Stand_r_thumb1_PitchInterpolator"
OrientationInterpolator2245.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2245.keyValue = (1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.5000,1.0000,0.0000,0.0000,0.1000,1.0000,0.0000,0.0000,0.2700,1.0000,0.0000,0.0000,0.2000,1.0000,0.0000,0.0000,0.0000)

Group2214.children.append(OrientationInterpolator2245)
OrientationInterpolator2246 = x3d.OrientationInterpolator()
OrientationInterpolator2246.DEF = "Stand_r_index1_RollInterpolator"
OrientationInterpolator2246.key = [0,0.2,0.4,0.5,0.8,1]
OrientationInterpolator2246.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.1000,0.0000,0.0000,1.0000,0.2000,0.0000,0.0000,1.0000,0.3000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2214.children.append(OrientationInterpolator2246)
OrientationInterpolator2247 = x3d.OrientationInterpolator()
OrientationInterpolator2247.DEF = "Stand_r_index2_RollInterpolator"
OrientationInterpolator2247.key = [0,0.2,0.4,0.5,0.8,1]
OrientationInterpolator2247.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.4000,0.0000,0.0000,1.0000,0.3200,0.0000,0.0000,1.0000,0.2500,0.0000,0.0000,1.0000,0.2000,0.0000,0.0000,1.0000,0.0000)

Group2214.children.append(OrientationInterpolator2247)
OrientationInterpolator2248 = x3d.OrientationInterpolator()
OrientationInterpolator2248.DEF = "Stand_r_index3_RollInterpolator"
OrientationInterpolator2248.key = [0,0.2,0.4,0.5,0.8,1]
OrientationInterpolator2248.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.2000,0.0000,0.0000,1.0000,0.3000,0.0000,0.0000,1.0000,0.3500,0.0000,0.0000,1.0000,0.2000,0.0000,0.0000,1.0000,0.0000)

Group2214.children.append(OrientationInterpolator2248)
ROUTE2249 = x3d.ROUTE()
ROUTE2249.fromField = "fraction_changed"
ROUTE2249.fromNode = "StandTimer"
ROUTE2249.toField = "set_fraction"
ROUTE2249.toNode = "Stand_r_ankle_RotationInterpolator"

Group2214.children.append(ROUTE2249)
ROUTE2250 = x3d.ROUTE()
ROUTE2250.fromField = "fraction_changed"
ROUTE2250.fromNode = "StandTimer"
ROUTE2250.toField = "set_fraction"
ROUTE2250.toNode = "Stand_r_knee_RotationInterpolator"

Group2214.children.append(ROUTE2250)
ROUTE2251 = x3d.ROUTE()
ROUTE2251.fromField = "fraction_changed"
ROUTE2251.fromNode = "StandTimer"
ROUTE2251.toField = "set_fraction"
ROUTE2251.toNode = "Stand_r_hip_RotationInterpolator"

Group2214.children.append(ROUTE2251)
ROUTE2252 = x3d.ROUTE()
ROUTE2252.fromField = "fraction_changed"
ROUTE2252.fromNode = "StandTimer"
ROUTE2252.toField = "set_fraction"
ROUTE2252.toNode = "Stand_l_ankle_RotationInterpolator"

Group2214.children.append(ROUTE2252)
ROUTE2253 = x3d.ROUTE()
ROUTE2253.fromField = "fraction_changed"
ROUTE2253.fromNode = "StandTimer"
ROUTE2253.toField = "set_fraction"
ROUTE2253.toNode = "Stand_l_knee_RotationInterpolator"

Group2214.children.append(ROUTE2253)
ROUTE2254 = x3d.ROUTE()
ROUTE2254.fromField = "fraction_changed"
ROUTE2254.fromNode = "StandTimer"
ROUTE2254.toField = "set_fraction"
ROUTE2254.toNode = "Stand_l_hip_RotationInterpolator"

Group2214.children.append(ROUTE2254)
ROUTE2255 = x3d.ROUTE()
ROUTE2255.fromField = "fraction_changed"
ROUTE2255.fromNode = "StandTimer"
ROUTE2255.toField = "set_fraction"
ROUTE2255.toNode = "Stand_lower_body_RotationInterpolator"

Group2214.children.append(ROUTE2255)
ROUTE2256 = x3d.ROUTE()
ROUTE2256.fromField = "fraction_changed"
ROUTE2256.fromNode = "StandTimer"
ROUTE2256.toField = "set_fraction"
ROUTE2256.toNode = "Stand_r_wrist_RotationInterpolator"

Group2214.children.append(ROUTE2256)
ROUTE2257 = x3d.ROUTE()
ROUTE2257.fromField = "fraction_changed"
ROUTE2257.fromNode = "StandTimer"
ROUTE2257.toField = "set_fraction"
ROUTE2257.toNode = "Stand_r_elbow_RotationInterpolator"

Group2214.children.append(ROUTE2257)
ROUTE2258 = x3d.ROUTE()
ROUTE2258.fromField = "fraction_changed"
ROUTE2258.fromNode = "StandTimer"
ROUTE2258.toField = "set_fraction"
ROUTE2258.toNode = "Stand_r_shoulder_RotationInterpolator"

Group2214.children.append(ROUTE2258)
ROUTE2259 = x3d.ROUTE()
ROUTE2259.fromField = "fraction_changed"
ROUTE2259.fromNode = "StandTimer"
ROUTE2259.toField = "set_fraction"
ROUTE2259.toNode = "Stand_l_wrist_RotationInterpolator"

Group2214.children.append(ROUTE2259)
ROUTE2260 = x3d.ROUTE()
ROUTE2260.fromField = "fraction_changed"
ROUTE2260.fromNode = "StandTimer"
ROUTE2260.toField = "set_fraction"
ROUTE2260.toNode = "Stand_l_elbow_RotationInterpolator"

Group2214.children.append(ROUTE2260)
ROUTE2261 = x3d.ROUTE()
ROUTE2261.fromField = "fraction_changed"
ROUTE2261.fromNode = "StandTimer"
ROUTE2261.toField = "set_fraction"
ROUTE2261.toNode = "Stand_l_shoulder_RotationInterpolator"

Group2214.children.append(ROUTE2261)
ROUTE2262 = x3d.ROUTE()
ROUTE2262.fromField = "fraction_changed"
ROUTE2262.fromNode = "StandTimer"
ROUTE2262.toField = "set_fraction"
ROUTE2262.toNode = "Stand_head_RotationInterpolator"

Group2214.children.append(ROUTE2262)
ROUTE2263 = x3d.ROUTE()
ROUTE2263.fromField = "fraction_changed"
ROUTE2263.fromNode = "StandTimer"
ROUTE2263.toField = "set_fraction"
ROUTE2263.toNode = "Stand_neck_RotationInterpolator"

Group2214.children.append(ROUTE2263)
ROUTE2264 = x3d.ROUTE()
ROUTE2264.fromField = "fraction_changed"
ROUTE2264.fromNode = "StandTimer"
ROUTE2264.toField = "set_fraction"
ROUTE2264.toNode = "Stand_l_eyeball_RotationInterpolator"

Group2214.children.append(ROUTE2264)
ROUTE2265 = x3d.ROUTE()
ROUTE2265.fromField = "fraction_changed"
ROUTE2265.fromNode = "StandTimer"
ROUTE2265.toField = "set_fraction"
ROUTE2265.toNode = "Stand_r_eyeball_RotationInterpolator"

Group2214.children.append(ROUTE2265)
ROUTE2266 = x3d.ROUTE()
ROUTE2266.fromField = "fraction_changed"
ROUTE2266.fromNode = "StandTimer"
ROUTE2266.toField = "set_fraction"
ROUTE2266.toNode = "Stand_upper_body_RotationInterpolator"

Group2214.children.append(ROUTE2266)
ROUTE2267 = x3d.ROUTE()
ROUTE2267.fromField = "fraction_changed"
ROUTE2267.fromNode = "StandTimer"
ROUTE2267.toField = "set_fraction"
ROUTE2267.toNode = "Stand_whole_body_RotationInterpolator"

Group2214.children.append(ROUTE2267)
ROUTE2268 = x3d.ROUTE()
ROUTE2268.fromField = "fraction_changed"
ROUTE2268.fromNode = "StandTimer"
ROUTE2268.toField = "set_fraction"
ROUTE2268.toNode = "Stand_whole_body_TranslationInterpolator"

Group2214.children.append(ROUTE2268)
ROUTE2269 = x3d.ROUTE()
ROUTE2269.fromField = "fraction_changed"
ROUTE2269.fromNode = "StandTimer"
ROUTE2269.toField = "set_fraction"
ROUTE2269.toNode = "Stand_l_sternoclavicular_RollInterpolator"

Group2214.children.append(ROUTE2269)
ROUTE2270 = x3d.ROUTE()
ROUTE2270.fromField = "fraction_changed"
ROUTE2270.fromNode = "StandTimer"
ROUTE2270.toField = "set_fraction"
ROUTE2270.toNode = "Stand_l_acromioclavicular_RollInterpolator"

Group2214.children.append(ROUTE2270)
ROUTE2271 = x3d.ROUTE()
ROUTE2271.fromField = "fraction_changed"
ROUTE2271.fromNode = "StandTimer"
ROUTE2271.toField = "set_fraction"
ROUTE2271.toNode = "Stand_r_sternoclavicular_RollInterpolator"

Group2214.children.append(ROUTE2271)
ROUTE2272 = x3d.ROUTE()
ROUTE2272.fromField = "fraction_changed"
ROUTE2272.fromNode = "StandTimer"
ROUTE2272.toField = "set_fraction"
ROUTE2272.toNode = "Stand_r_acromioclavicular_RollInterpolator"

Group2214.children.append(ROUTE2272)
ROUTE2273 = x3d.ROUTE()
ROUTE2273.fromField = "fraction_changed"
ROUTE2273.fromNode = "StandTimer"
ROUTE2273.toField = "set_fraction"
ROUTE2273.toNode = "Stand_r_metatarsal_PitchInterpolator"

Group2214.children.append(ROUTE2273)
ROUTE2274 = x3d.ROUTE()
ROUTE2274.fromField = "fraction_changed"
ROUTE2274.fromNode = "StandTimer"
ROUTE2274.toField = "set_fraction"
ROUTE2274.toNode = "Stand_sacroiliac_YawInterpolator"

Group2214.children.append(ROUTE2274)
ROUTE2275 = x3d.ROUTE()
ROUTE2275.fromField = "fraction_changed"
ROUTE2275.fromNode = "StandTimer"
ROUTE2275.toField = "set_fraction"
ROUTE2275.toNode = "Stand_vl5_YawInterpolator"

Group2214.children.append(ROUTE2275)
ROUTE2276 = x3d.ROUTE()
ROUTE2276.fromField = "fraction_changed"
ROUTE2276.fromNode = "StandTimer"
ROUTE2276.toField = "set_fraction"
ROUTE2276.toNode = "Stand_vc6_YawInterpolator"

Group2214.children.append(ROUTE2276)
ROUTE2277 = x3d.ROUTE()
ROUTE2277.fromField = "fraction_changed"
ROUTE2277.fromNode = "StandTimer"
ROUTE2277.toField = "set_fraction"
ROUTE2277.toNode = "Stand_l_thumb1_PitchInterpolator"

Group2214.children.append(ROUTE2277)
ROUTE2278 = x3d.ROUTE()
ROUTE2278.fromField = "fraction_changed"
ROUTE2278.fromNode = "StandTimer"
ROUTE2278.toField = "set_fraction"
ROUTE2278.toNode = "Stand_r_thumb1_PitchInterpolator"

Group2214.children.append(ROUTE2278)
ROUTE2279 = x3d.ROUTE()
ROUTE2279.fromField = "fraction_changed"
ROUTE2279.fromNode = "StandTimer"
ROUTE2279.toField = "set_fraction"
ROUTE2279.toNode = "Stand_r_index1_RollInterpolator"

Group2214.children.append(ROUTE2279)
ROUTE2280 = x3d.ROUTE()
ROUTE2280.fromField = "fraction_changed"
ROUTE2280.fromNode = "StandTimer"
ROUTE2280.toField = "set_fraction"
ROUTE2280.toNode = "Stand_r_index2_RollInterpolator"

Group2214.children.append(ROUTE2280)
ROUTE2281 = x3d.ROUTE()
ROUTE2281.fromField = "fraction_changed"
ROUTE2281.fromNode = "StandTimer"
ROUTE2281.toField = "set_fraction"
ROUTE2281.toNode = "Stand_r_index3_RollInterpolator"

Group2214.children.append(ROUTE2281)
ROUTE2282 = x3d.ROUTE()
ROUTE2282.fromField = "value_changed"
ROUTE2282.fromNode = "Stand_r_ankle_RotationInterpolator"
ROUTE2282.toField = "rotation"
ROUTE2282.toNode = "hanim_r_ankle"

Group2214.children.append(ROUTE2282)
ROUTE2283 = x3d.ROUTE()
ROUTE2283.fromField = "value_changed"
ROUTE2283.fromNode = "Stand_r_knee_RotationInterpolator"
ROUTE2283.toField = "rotation"
ROUTE2283.toNode = "hanim_r_knee"

Group2214.children.append(ROUTE2283)
ROUTE2284 = x3d.ROUTE()
ROUTE2284.fromField = "value_changed"
ROUTE2284.fromNode = "Stand_r_hip_RotationInterpolator"
ROUTE2284.toField = "rotation"
ROUTE2284.toNode = "hanim_r_hip"

Group2214.children.append(ROUTE2284)
ROUTE2285 = x3d.ROUTE()
ROUTE2285.fromField = "value_changed"
ROUTE2285.fromNode = "Stand_l_ankle_RotationInterpolator"
ROUTE2285.toField = "rotation"
ROUTE2285.toNode = "hanim_l_ankle"

Group2214.children.append(ROUTE2285)
ROUTE2286 = x3d.ROUTE()
ROUTE2286.fromField = "value_changed"
ROUTE2286.fromNode = "Stand_l_knee_RotationInterpolator"
ROUTE2286.toField = "rotation"
ROUTE2286.toNode = "hanim_l_knee"

Group2214.children.append(ROUTE2286)
ROUTE2287 = x3d.ROUTE()
ROUTE2287.fromField = "value_changed"
ROUTE2287.fromNode = "Stand_l_hip_RotationInterpolator"
ROUTE2287.toField = "rotation"
ROUTE2287.toNode = "hanim_l_hip"

Group2214.children.append(ROUTE2287)
ROUTE2288 = x3d.ROUTE()
ROUTE2288.fromField = "value_changed"
ROUTE2288.fromNode = "Stand_r_wrist_RotationInterpolator"
ROUTE2288.toField = "rotation"
ROUTE2288.toNode = "hanim_r_wrist"

Group2214.children.append(ROUTE2288)
ROUTE2289 = x3d.ROUTE()
ROUTE2289.fromField = "value_changed"
ROUTE2289.fromNode = "Stand_r_elbow_RotationInterpolator"
ROUTE2289.toField = "rotation"
ROUTE2289.toNode = "hanim_r_elbow"

Group2214.children.append(ROUTE2289)
ROUTE2290 = x3d.ROUTE()
ROUTE2290.fromField = "value_changed"
ROUTE2290.fromNode = "Stand_r_shoulder_RotationInterpolator"
ROUTE2290.toField = "rotation"
ROUTE2290.toNode = "hanim_r_shoulder"

Group2214.children.append(ROUTE2290)
ROUTE2291 = x3d.ROUTE()
ROUTE2291.fromField = "value_changed"
ROUTE2291.fromNode = "Stand_l_wrist_RotationInterpolator"
ROUTE2291.toField = "rotation"
ROUTE2291.toNode = "hanim_l_wrist"

Group2214.children.append(ROUTE2291)
ROUTE2292 = x3d.ROUTE()
ROUTE2292.fromField = "value_changed"
ROUTE2292.fromNode = "Stand_l_elbow_RotationInterpolator"
ROUTE2292.toField = "rotation"
ROUTE2292.toNode = "hanim_l_elbow"

Group2214.children.append(ROUTE2292)
ROUTE2293 = x3d.ROUTE()
ROUTE2293.fromField = "value_changed"
ROUTE2293.fromNode = "Stand_l_shoulder_RotationInterpolator"
ROUTE2293.toField = "rotation"
ROUTE2293.toNode = "hanim_l_shoulder"

Group2214.children.append(ROUTE2293)
ROUTE2294 = x3d.ROUTE()
ROUTE2294.fromField = "value_changed"
ROUTE2294.fromNode = "Stand_head_RotationInterpolator"
ROUTE2294.toField = "rotation"
ROUTE2294.toNode = "hanim_skullbase"

Group2214.children.append(ROUTE2294)
ROUTE2295 = x3d.ROUTE()
ROUTE2295.fromField = "value_changed"
ROUTE2295.fromNode = "Stand_neck_RotationInterpolator"
ROUTE2295.toField = "rotation"
ROUTE2295.toNode = "hanim_vc7"

Group2214.children.append(ROUTE2295)
ROUTE2296 = x3d.ROUTE()
ROUTE2296.fromField = "value_changed"
ROUTE2296.fromNode = "Stand_l_eyeball_RotationInterpolator"
ROUTE2296.toField = "rotation"
ROUTE2296.toNode = "hanim_l_eyeball_joint"

Group2214.children.append(ROUTE2296)
ROUTE2297 = x3d.ROUTE()
ROUTE2297.fromField = "value_changed"
ROUTE2297.fromNode = "Stand_r_eyeball_RotationInterpolator"
ROUTE2297.toField = "rotation"
ROUTE2297.toNode = "hanim_r_eyeball_joint"

Group2214.children.append(ROUTE2297)
ROUTE2298 = x3d.ROUTE()
ROUTE2298.fromField = "value_changed"
ROUTE2298.fromNode = "Stand_upper_body_RotationInterpolator"
ROUTE2298.toField = "rotation"
ROUTE2298.toNode = "hanim_vl1"

Group2214.children.append(ROUTE2298)
ROUTE2299 = x3d.ROUTE()
ROUTE2299.fromField = "value_changed"
ROUTE2299.fromNode = "Stand_lower_body_RotationInterpolator"
ROUTE2299.toField = "rotation"
ROUTE2299.toNode = "hanim_sacroiliac"

Group2214.children.append(ROUTE2299)
ROUTE2300 = x3d.ROUTE()
ROUTE2300.fromField = "value_changed"
ROUTE2300.fromNode = "Stand_whole_body_RotationInterpolator"
ROUTE2300.toField = "rotation"
ROUTE2300.toNode = "hanim_humanoid_root"

Group2214.children.append(ROUTE2300)
ROUTE2301 = x3d.ROUTE()
ROUTE2301.fromField = "value_changed"
ROUTE2301.fromNode = "Stand_whole_body_TranslationInterpolator"
ROUTE2301.toField = "translation"
ROUTE2301.toNode = "hanim_humanoid_root"

Group2214.children.append(ROUTE2301)
ROUTE2302 = x3d.ROUTE()
ROUTE2302.fromField = "value_changed"
ROUTE2302.fromNode = "Stand_l_sternoclavicular_RollInterpolator"
ROUTE2302.toField = "rotation"
ROUTE2302.toNode = "hanim_l_sternoclavicular"

Group2214.children.append(ROUTE2302)
ROUTE2303 = x3d.ROUTE()
ROUTE2303.fromField = "value_changed"
ROUTE2303.fromNode = "Stand_l_acromioclavicular_RollInterpolator"
ROUTE2303.toField = "rotation"
ROUTE2303.toNode = "hanim_l_acromioclavicular"

Group2214.children.append(ROUTE2303)
ROUTE2304 = x3d.ROUTE()
ROUTE2304.fromField = "value_changed"
ROUTE2304.fromNode = "Stand_r_sternoclavicular_RollInterpolator"
ROUTE2304.toField = "rotation"
ROUTE2304.toNode = "hanim_r_sternoclavicular"

Group2214.children.append(ROUTE2304)
ROUTE2305 = x3d.ROUTE()
ROUTE2305.fromField = "value_changed"
ROUTE2305.fromNode = "Stand_r_acromioclavicular_RollInterpolator"
ROUTE2305.toField = "rotation"
ROUTE2305.toNode = "hanim_r_acromioclavicular"

Group2214.children.append(ROUTE2305)
ROUTE2306 = x3d.ROUTE()
ROUTE2306.fromField = "value_changed"
ROUTE2306.fromNode = "Stand_r_metatarsal_PitchInterpolator"
ROUTE2306.toField = "rotation"
ROUTE2306.toNode = "hanim_l_metatarsal"

Group2214.children.append(ROUTE2306)
ROUTE2307 = x3d.ROUTE()
ROUTE2307.fromField = "value_changed"
ROUTE2307.fromNode = "Stand_r_metatarsal_PitchInterpolator"
ROUTE2307.toField = "rotation"
ROUTE2307.toNode = "hanim_r_metatarsal"

Group2214.children.append(ROUTE2307)
ROUTE2308 = x3d.ROUTE()
ROUTE2308.fromField = "value_changed"
ROUTE2308.fromNode = "Stand_sacroiliac_YawInterpolator"
ROUTE2308.toField = "rotation"
ROUTE2308.toNode = "hanim_sacroiliac"

Group2214.children.append(ROUTE2308)
ROUTE2309 = x3d.ROUTE()
ROUTE2309.fromField = "value_changed"
ROUTE2309.fromNode = "Stand_vl5_YawInterpolator"
ROUTE2309.toField = "rotation"
ROUTE2309.toNode = "hanim_vl5"

Group2214.children.append(ROUTE2309)
ROUTE2310 = x3d.ROUTE()
ROUTE2310.fromField = "value_changed"
ROUTE2310.fromNode = "Stand_vc6_YawInterpolator"
ROUTE2310.toField = "rotation"
ROUTE2310.toNode = "hanim_vc6"

Group2214.children.append(ROUTE2310)
ROUTE2311 = x3d.ROUTE()
ROUTE2311.fromField = "value_changed"
ROUTE2311.fromNode = "Stand_l_thumb1_PitchInterpolator"
ROUTE2311.toField = "rotation"
ROUTE2311.toNode = "hanim_l_thumb1"

Group2214.children.append(ROUTE2311)
ROUTE2312 = x3d.ROUTE()
ROUTE2312.fromField = "value_changed"
ROUTE2312.fromNode = "Stand_r_thumb1_PitchInterpolator"
ROUTE2312.toField = "rotation"
ROUTE2312.toNode = "hanim_r_thumb1"

Group2214.children.append(ROUTE2312)
ROUTE2313 = x3d.ROUTE()
ROUTE2313.fromField = "value_changed"
ROUTE2313.fromNode = "Stand_r_index1_RollInterpolator"
ROUTE2313.toField = "rotation"
ROUTE2313.toNode = "hanim_r_index1"

Group2214.children.append(ROUTE2313)
ROUTE2314 = x3d.ROUTE()
ROUTE2314.fromField = "value_changed"
ROUTE2314.fromNode = "Stand_r_index2_RollInterpolator"
ROUTE2314.toField = "rotation"
ROUTE2314.toNode = "hanim_r_index2"

Group2214.children.append(ROUTE2314)
ROUTE2315 = x3d.ROUTE()
ROUTE2315.fromField = "value_changed"
ROUTE2315.fromNode = "Stand_r_index3_RollInterpolator"
ROUTE2315.toField = "rotation"
ROUTE2315.toNode = "hanim_r_index3"

Group2214.children.append(ROUTE2315)
ROUTE2316 = x3d.ROUTE()
ROUTE2316.fromField = "value_changed"
ROUTE2316.fromNode = "Stand_r_index1_RollInterpolator"
ROUTE2316.toField = "rotation"
ROUTE2316.toNode = "hanim_r_middle1"

Group2214.children.append(ROUTE2316)
ROUTE2317 = x3d.ROUTE()
ROUTE2317.fromField = "value_changed"
ROUTE2317.fromNode = "Stand_r_index2_RollInterpolator"
ROUTE2317.toField = "rotation"
ROUTE2317.toNode = "hanim_r_middle2"

Group2214.children.append(ROUTE2317)
ROUTE2318 = x3d.ROUTE()
ROUTE2318.fromField = "value_changed"
ROUTE2318.fromNode = "Stand_r_index3_RollInterpolator"
ROUTE2318.toField = "rotation"
ROUTE2318.toNode = "hanim_r_middle3"

Group2214.children.append(ROUTE2318)
ROUTE2319 = x3d.ROUTE()
ROUTE2319.fromField = "value_changed"
ROUTE2319.fromNode = "Stand_r_index1_RollInterpolator"
ROUTE2319.toField = "rotation"
ROUTE2319.toNode = "hanim_r_ring1"

Group2214.children.append(ROUTE2319)
ROUTE2320 = x3d.ROUTE()
ROUTE2320.fromField = "value_changed"
ROUTE2320.fromNode = "Stand_r_index2_RollInterpolator"
ROUTE2320.toField = "rotation"
ROUTE2320.toNode = "hanim_r_ring2"

Group2214.children.append(ROUTE2320)
ROUTE2321 = x3d.ROUTE()
ROUTE2321.fromField = "value_changed"
ROUTE2321.fromNode = "Stand_r_index3_RollInterpolator"
ROUTE2321.toField = "rotation"
ROUTE2321.toNode = "hanim_r_ring3"

Group2214.children.append(ROUTE2321)
ROUTE2322 = x3d.ROUTE()
ROUTE2322.fromField = "value_changed"
ROUTE2322.fromNode = "Stand_r_index1_RollInterpolator"
ROUTE2322.toField = "rotation"
ROUTE2322.toNode = "hanim_r_pinky1"

Group2214.children.append(ROUTE2322)
ROUTE2323 = x3d.ROUTE()
ROUTE2323.fromField = "value_changed"
ROUTE2323.fromNode = "Stand_r_index2_RollInterpolator"
ROUTE2323.toField = "rotation"
ROUTE2323.toNode = "hanim_r_pinky2"

Group2214.children.append(ROUTE2323)
ROUTE2324 = x3d.ROUTE()
ROUTE2324.fromField = "value_changed"
ROUTE2324.fromNode = "Stand_r_index3_RollInterpolator"
ROUTE2324.toField = "rotation"
ROUTE2324.toNode = "hanim_r_pinky3"

Group2214.children.append(ROUTE2324)

Scene30.children.append(Group2214)
Group2325 = x3d.Group()
Group2325.DEF = "PitchesAnimation"
TimeSensor2326 = x3d.TimeSensor()
TimeSensor2326.DEF = "PitchTimer"
TimeSensor2326.cycleInterval = 5.73
TimeSensor2326.loop = True

Group2325.children.append(TimeSensor2326)
OrientationInterpolator2327 = x3d.OrientationInterpolator()
OrientationInterpolator2327.DEF = "Pitch_r_metatarsal_PitchInterpolator"
OrientationInterpolator2327.key = [0,0.2,0.4,0.6,0.7,1]
OrientationInterpolator2327.keyValue = (1.0000,0.0000,0.0000,0.0000,-1.0000,0.0000,0.0000,0.5000,-1.0000,0.0000,0.0000,0.7000,1.0000,0.0000,0.0000,0.7500,-1.0000,0.0000,0.0000,0.2000,1.0000,0.0000,0.0000,0.0000)

Group2325.children.append(OrientationInterpolator2327)
OrientationInterpolator2328 = x3d.OrientationInterpolator()
OrientationInterpolator2328.DEF = "Pitches_r_ankle_RotationInterpolator"
OrientationInterpolator2328.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator2328.keyValue = (0.0000,0.0000,1.0000,0.0000,1.0000,0.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000,-1.0000,0.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000)

Group2325.children.append(OrientationInterpolator2328)
OrientationInterpolator2329 = x3d.OrientationInterpolator()
OrientationInterpolator2329.DEF = "Pitches_r_knee_RotationInterpolator"
OrientationInterpolator2329.key = [0,0.5,1]
OrientationInterpolator2329.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2325.children.append(OrientationInterpolator2329)
OrientationInterpolator2330 = x3d.OrientationInterpolator()
OrientationInterpolator2330.DEF = "Pitches_r_hip_RotationInterpolator"
OrientationInterpolator2330.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator2330.keyValue = (0.0000,0.0000,1.0000,0.0000,-1.0000,0.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000,1.0000,0.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000)

Group2325.children.append(OrientationInterpolator2330)
OrientationInterpolator2331 = x3d.OrientationInterpolator()
OrientationInterpolator2331.DEF = "Pitches_l_ankle_RotationInterpolator"
OrientationInterpolator2331.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator2331.keyValue = (0.0000,0.0000,1.0000,0.0000,-1.0000,0.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000,1.0000,0.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000)

Group2325.children.append(OrientationInterpolator2331)
OrientationInterpolator2332 = x3d.OrientationInterpolator()
OrientationInterpolator2332.DEF = "Pitches_l_knee_RotationInterpolator"
OrientationInterpolator2332.key = [0,0.5,1]
OrientationInterpolator2332.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2325.children.append(OrientationInterpolator2332)
OrientationInterpolator2333 = x3d.OrientationInterpolator()
OrientationInterpolator2333.DEF = "Pitches_l_hip_RotationInterpolator"
OrientationInterpolator2333.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator2333.keyValue = (0.0000,0.0000,1.0000,0.0000,1.0000,0.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000,-1.0000,0.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000)

Group2325.children.append(OrientationInterpolator2333)
OrientationInterpolator2334 = x3d.OrientationInterpolator()
OrientationInterpolator2334.DEF = "Pitches_r_wrist_RotationInterpolator"
OrientationInterpolator2334.key = [0,0.5,1]
OrientationInterpolator2334.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2325.children.append(OrientationInterpolator2334)
OrientationInterpolator2335 = x3d.OrientationInterpolator()
OrientationInterpolator2335.DEF = "Pitches_r_elbow_RotationInterpolator"
OrientationInterpolator2335.key = [0,0.5,1]
OrientationInterpolator2335.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2325.children.append(OrientationInterpolator2335)
OrientationInterpolator2336 = x3d.OrientationInterpolator()
OrientationInterpolator2336.DEF = "Pitches_r_shoulder_RotationInterpolator"
OrientationInterpolator2336.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator2336.keyValue = (0.0000,0.0000,1.0000,0.0000,1.0000,0.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000,-1.0000,0.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000)

Group2325.children.append(OrientationInterpolator2336)
OrientationInterpolator2337 = x3d.OrientationInterpolator()
OrientationInterpolator2337.DEF = "Pitches_l_wrist_RotationInterpolator"
OrientationInterpolator2337.key = [0,0.5,1]
OrientationInterpolator2337.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2325.children.append(OrientationInterpolator2337)
OrientationInterpolator2338 = x3d.OrientationInterpolator()
OrientationInterpolator2338.DEF = "Pitches_l_elbow_RotationInterpolator"
OrientationInterpolator2338.key = [0,0.5,1]
OrientationInterpolator2338.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2325.children.append(OrientationInterpolator2338)
OrientationInterpolator2339 = x3d.OrientationInterpolator()
OrientationInterpolator2339.DEF = "Pitches_l_shoulder_RotationInterpolator"
OrientationInterpolator2339.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator2339.keyValue = (0.0000,0.0000,1.0000,0.0000,-1.0000,0.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000,1.0000,0.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000)

Group2325.children.append(OrientationInterpolator2339)
OrientationInterpolator2340 = x3d.OrientationInterpolator()
OrientationInterpolator2340.DEF = "Pitches_head_RotationInterpolator"
OrientationInterpolator2340.key = [0,0.5,1]
OrientationInterpolator2340.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2325.children.append(OrientationInterpolator2340)
OrientationInterpolator2341 = x3d.OrientationInterpolator()
OrientationInterpolator2341.DEF = "Pitches_neck_RotationInterpolator"
OrientationInterpolator2341.key = [0,0.25,0.55,1]
OrientationInterpolator2341.keyValue = (0.0000,0.0000,1.0000,0.0000,1.0000,0.0000,0.0000,0.5500,-1.0000,0.0000,0.0000,1.0500,0.0000,0.0000,1.0000,0.0000)

Group2325.children.append(OrientationInterpolator2341)
OrientationInterpolator2342 = x3d.OrientationInterpolator()
OrientationInterpolator2342.DEF = "Pitches_lower_body_RotationInterpolator"
OrientationInterpolator2342.key = [0,0.5,1]
OrientationInterpolator2342.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2325.children.append(OrientationInterpolator2342)
OrientationInterpolator2343 = x3d.OrientationInterpolator()
OrientationInterpolator2343.DEF = "Pitches_upper_body_RotationInterpolator"
OrientationInterpolator2343.key = [0,0.5,1]
OrientationInterpolator2343.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2325.children.append(OrientationInterpolator2343)
OrientationInterpolator2344 = x3d.OrientationInterpolator()
OrientationInterpolator2344.DEF = "Pitches_whole_body_RotationInterpolator"
OrientationInterpolator2344.key = [0,0.5,1]
OrientationInterpolator2344.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2325.children.append(OrientationInterpolator2344)
PositionInterpolator2345 = x3d.PositionInterpolator()
PositionInterpolator2345.DEF = "Pitches_whole_body_TranslationInterpolator"
PositionInterpolator2345.key = [0,0.125,0.25,0.375,0.5,0.625,0.75,0.875,1]
PositionInterpolator2345.keyValue = (0.0000,0.0000,0.0000,0.0000,-0.1500,0.0000,0.0000,-0.7000,0.0000,0.0000,-0.1500,0.0000,0.0000,0.0000,0.0000,0.0000,-0.1500,0.0000,0.0000,-0.7000,0.0000,0.0000,-0.1500,0.0000,0.0000,0.0000,0.0000)

Group2325.children.append(PositionInterpolator2345)
OrientationInterpolator2346 = x3d.OrientationInterpolator()
OrientationInterpolator2346.DEF = "Pitch_l_sternoclavicular_RollInterpolator"
OrientationInterpolator2346.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2346.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2325.children.append(OrientationInterpolator2346)
OrientationInterpolator2347 = x3d.OrientationInterpolator()
OrientationInterpolator2347.DEF = "Pitch_l_acromioclavicular_RollInterpolator"
OrientationInterpolator2347.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2347.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2325.children.append(OrientationInterpolator2347)
OrientationInterpolator2348 = x3d.OrientationInterpolator()
OrientationInterpolator2348.DEF = "Pitch_r_sternoclavicular_RollInterpolator"
OrientationInterpolator2348.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2348.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2325.children.append(OrientationInterpolator2348)
OrientationInterpolator2349 = x3d.OrientationInterpolator()
OrientationInterpolator2349.DEF = "Pitch_r_acromioclavicular_RollInterpolator"
OrientationInterpolator2349.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2349.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2325.children.append(OrientationInterpolator2349)
OrientationInterpolator2350 = x3d.OrientationInterpolator()
OrientationInterpolator2350.DEF = "Pitch_sacroiliac_YawInterpolator"
OrientationInterpolator2350.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2350.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2325.children.append(OrientationInterpolator2350)
OrientationInterpolator2351 = x3d.OrientationInterpolator()
OrientationInterpolator2351.DEF = "Pitch_vl5_YawInterpolator"
OrientationInterpolator2351.key = [0,0.2,0.4,0.5,0.6,0.8,1]
OrientationInterpolator2351.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2325.children.append(OrientationInterpolator2351)
OrientationInterpolator2352 = x3d.OrientationInterpolator()
OrientationInterpolator2352.DEF = "Pitch_vc6_YawInterpolator"
OrientationInterpolator2352.key = [0,0.2,0.4,0.5,0.6,0.8,1]
OrientationInterpolator2352.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2325.children.append(OrientationInterpolator2352)
OrientationInterpolator2353 = x3d.OrientationInterpolator()
OrientationInterpolator2353.DEF = "Pitch_l_thumb1_PitchInterpolator"
OrientationInterpolator2353.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2353.keyValue = (1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.2500,1.0000,0.0000,0.0000,0.3000,1.0000,0.0000,0.0000,0.2700,1.0000,0.0000,0.0000,0.2000,1.0000,0.0000,0.0000,0.0000)

Group2325.children.append(OrientationInterpolator2353)
OrientationInterpolator2354 = x3d.OrientationInterpolator()
OrientationInterpolator2354.DEF = "Pitch_r_thumb1_PitchInterpolator"
OrientationInterpolator2354.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2354.keyValue = (1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.2500,1.0000,0.0000,0.0000,0.3000,1.0000,0.0000,0.0000,0.2700,1.0000,0.0000,0.0000,0.2000,1.0000,0.0000,0.0000,0.0000)

Group2325.children.append(OrientationInterpolator2354)
ROUTE2355 = x3d.ROUTE()
ROUTE2355.fromField = "fraction_changed"
ROUTE2355.fromNode = "PitchTimer"
ROUTE2355.toField = "set_fraction"
ROUTE2355.toNode = "Pitches_r_ankle_RotationInterpolator"

Group2325.children.append(ROUTE2355)
ROUTE2356 = x3d.ROUTE()
ROUTE2356.fromField = "fraction_changed"
ROUTE2356.fromNode = "PitchTimer"
ROUTE2356.toField = "set_fraction"
ROUTE2356.toNode = "Pitches_r_knee_RotationInterpolator"

Group2325.children.append(ROUTE2356)
ROUTE2357 = x3d.ROUTE()
ROUTE2357.fromField = "fraction_changed"
ROUTE2357.fromNode = "PitchTimer"
ROUTE2357.toField = "set_fraction"
ROUTE2357.toNode = "Pitches_r_hip_RotationInterpolator"

Group2325.children.append(ROUTE2357)
ROUTE2358 = x3d.ROUTE()
ROUTE2358.fromField = "fraction_changed"
ROUTE2358.fromNode = "PitchTimer"
ROUTE2358.toField = "set_fraction"
ROUTE2358.toNode = "Pitches_l_ankle_RotationInterpolator"

Group2325.children.append(ROUTE2358)
ROUTE2359 = x3d.ROUTE()
ROUTE2359.fromField = "fraction_changed"
ROUTE2359.fromNode = "PitchTimer"
ROUTE2359.toField = "set_fraction"
ROUTE2359.toNode = "Pitches_l_knee_RotationInterpolator"

Group2325.children.append(ROUTE2359)
ROUTE2360 = x3d.ROUTE()
ROUTE2360.fromField = "fraction_changed"
ROUTE2360.fromNode = "PitchTimer"
ROUTE2360.toField = "set_fraction"
ROUTE2360.toNode = "Pitches_l_hip_RotationInterpolator"

Group2325.children.append(ROUTE2360)
ROUTE2361 = x3d.ROUTE()
ROUTE2361.fromField = "fraction_changed"
ROUTE2361.fromNode = "PitchTimer"
ROUTE2361.toField = "set_fraction"
ROUTE2361.toNode = "Pitches_lower_body_RotationInterpolator"

Group2325.children.append(ROUTE2361)
ROUTE2362 = x3d.ROUTE()
ROUTE2362.fromField = "fraction_changed"
ROUTE2362.fromNode = "PitchTimer"
ROUTE2362.toField = "set_fraction"
ROUTE2362.toNode = "Pitches_r_wrist_RotationInterpolator"

Group2325.children.append(ROUTE2362)
ROUTE2363 = x3d.ROUTE()
ROUTE2363.fromField = "fraction_changed"
ROUTE2363.fromNode = "PitchTimer"
ROUTE2363.toField = "set_fraction"
ROUTE2363.toNode = "Pitches_r_elbow_RotationInterpolator"

Group2325.children.append(ROUTE2363)
ROUTE2364 = x3d.ROUTE()
ROUTE2364.fromField = "fraction_changed"
ROUTE2364.fromNode = "PitchTimer"
ROUTE2364.toField = "set_fraction"
ROUTE2364.toNode = "Pitches_r_shoulder_RotationInterpolator"

Group2325.children.append(ROUTE2364)
ROUTE2365 = x3d.ROUTE()
ROUTE2365.fromField = "fraction_changed"
ROUTE2365.fromNode = "PitchTimer"
ROUTE2365.toField = "set_fraction"
ROUTE2365.toNode = "Pitches_l_wrist_RotationInterpolator"

Group2325.children.append(ROUTE2365)
ROUTE2366 = x3d.ROUTE()
ROUTE2366.fromField = "fraction_changed"
ROUTE2366.fromNode = "PitchTimer"
ROUTE2366.toField = "set_fraction"
ROUTE2366.toNode = "Pitches_l_elbow_RotationInterpolator"

Group2325.children.append(ROUTE2366)
ROUTE2367 = x3d.ROUTE()
ROUTE2367.fromField = "fraction_changed"
ROUTE2367.fromNode = "PitchTimer"
ROUTE2367.toField = "set_fraction"
ROUTE2367.toNode = "Pitches_l_shoulder_RotationInterpolator"

Group2325.children.append(ROUTE2367)
ROUTE2368 = x3d.ROUTE()
ROUTE2368.fromField = "fraction_changed"
ROUTE2368.fromNode = "PitchTimer"
ROUTE2368.toField = "set_fraction"
ROUTE2368.toNode = "Pitches_head_RotationInterpolator"

Group2325.children.append(ROUTE2368)
ROUTE2369 = x3d.ROUTE()
ROUTE2369.fromField = "fraction_changed"
ROUTE2369.fromNode = "PitchTimer"
ROUTE2369.toField = "set_fraction"
ROUTE2369.toNode = "Pitches_neck_RotationInterpolator"

Group2325.children.append(ROUTE2369)
ROUTE2370 = x3d.ROUTE()
ROUTE2370.fromField = "fraction_changed"
ROUTE2370.fromNode = "PitchTimer"
ROUTE2370.toField = "set_fraction"
ROUTE2370.toNode = "Pitches_upper_body_RotationInterpolator"

Group2325.children.append(ROUTE2370)
ROUTE2371 = x3d.ROUTE()
ROUTE2371.fromField = "fraction_changed"
ROUTE2371.fromNode = "PitchTimer"
ROUTE2371.toField = "set_fraction"
ROUTE2371.toNode = "Pitches_whole_body_RotationInterpolator"

Group2325.children.append(ROUTE2371)
ROUTE2372 = x3d.ROUTE()
ROUTE2372.fromField = "fraction_changed"
ROUTE2372.fromNode = "PitchTimer"
ROUTE2372.toField = "set_fraction"
ROUTE2372.toNode = "Pitches_whole_body_TranslationInterpolator"

Group2325.children.append(ROUTE2372)
ROUTE2373 = x3d.ROUTE()
ROUTE2373.fromField = "fraction_changed"
ROUTE2373.fromNode = "PitchTimer"
ROUTE2373.toField = "set_fraction"
ROUTE2373.toNode = "Pitch_l_sternoclavicular_RollInterpolator"

Group2325.children.append(ROUTE2373)
ROUTE2374 = x3d.ROUTE()
ROUTE2374.fromField = "fraction_changed"
ROUTE2374.fromNode = "PitchTimer"
ROUTE2374.toField = "set_fraction"
ROUTE2374.toNode = "Pitch_l_acromioclavicular_RollInterpolator"

Group2325.children.append(ROUTE2374)
ROUTE2375 = x3d.ROUTE()
ROUTE2375.fromField = "fraction_changed"
ROUTE2375.fromNode = "PitchTimer"
ROUTE2375.toField = "set_fraction"
ROUTE2375.toNode = "Pitch_r_sternoclavicular_RollInterpolator"

Group2325.children.append(ROUTE2375)
ROUTE2376 = x3d.ROUTE()
ROUTE2376.fromField = "fraction_changed"
ROUTE2376.fromNode = "PitchTimer"
ROUTE2376.toField = "set_fraction"
ROUTE2376.toNode = "Pitch_r_acromioclavicular_RollInterpolator"

Group2325.children.append(ROUTE2376)
ROUTE2377 = x3d.ROUTE()
ROUTE2377.fromField = "fraction_changed"
ROUTE2377.fromNode = "PitchTimer"
ROUTE2377.toField = "set_fraction"
ROUTE2377.toNode = "Pitch_r_metatarsal_PitchInterpolator"

Group2325.children.append(ROUTE2377)
ROUTE2378 = x3d.ROUTE()
ROUTE2378.fromField = "fraction_changed"
ROUTE2378.fromNode = "PitchTimer"
ROUTE2378.toField = "set_fraction"
ROUTE2378.toNode = "Pitch_sacroiliac_YawInterpolator"

Group2325.children.append(ROUTE2378)
ROUTE2379 = x3d.ROUTE()
ROUTE2379.fromField = "fraction_changed"
ROUTE2379.fromNode = "PitchTimer"
ROUTE2379.toField = "set_fraction"
ROUTE2379.toNode = "Pitch_vl5_YawInterpolator"

Group2325.children.append(ROUTE2379)
ROUTE2380 = x3d.ROUTE()
ROUTE2380.fromField = "fraction_changed"
ROUTE2380.fromNode = "PitchTimer"
ROUTE2380.toField = "set_fraction"
ROUTE2380.toNode = "Pitch_vc6_YawInterpolator"

Group2325.children.append(ROUTE2380)
ROUTE2381 = x3d.ROUTE()
ROUTE2381.fromField = "fraction_changed"
ROUTE2381.fromNode = "PitchTimer"
ROUTE2381.toField = "set_fraction"
ROUTE2381.toNode = "Pitch_l_thumb1_PitchInterpolator"

Group2325.children.append(ROUTE2381)
ROUTE2382 = x3d.ROUTE()
ROUTE2382.fromField = "fraction_changed"
ROUTE2382.fromNode = "PitchTimer"
ROUTE2382.toField = "set_fraction"
ROUTE2382.toNode = "Pitch_r_thumb1_PitchInterpolator"

Group2325.children.append(ROUTE2382)
ROUTE2383 = x3d.ROUTE()
ROUTE2383.fromField = "value_changed"
ROUTE2383.fromNode = "Pitches_r_ankle_RotationInterpolator"
ROUTE2383.toField = "rotation"
ROUTE2383.toNode = "hanim_r_ankle"

Group2325.children.append(ROUTE2383)
ROUTE2384 = x3d.ROUTE()
ROUTE2384.fromField = "value_changed"
ROUTE2384.fromNode = "Pitches_r_knee_RotationInterpolator"
ROUTE2384.toField = "rotation"
ROUTE2384.toNode = "hanim_r_knee"

Group2325.children.append(ROUTE2384)
ROUTE2385 = x3d.ROUTE()
ROUTE2385.fromField = "value_changed"
ROUTE2385.fromNode = "Pitches_r_hip_RotationInterpolator"
ROUTE2385.toField = "rotation"
ROUTE2385.toNode = "hanim_r_hip"

Group2325.children.append(ROUTE2385)
ROUTE2386 = x3d.ROUTE()
ROUTE2386.fromField = "value_changed"
ROUTE2386.fromNode = "Pitches_l_ankle_RotationInterpolator"
ROUTE2386.toField = "rotation"
ROUTE2386.toNode = "hanim_l_ankle"

Group2325.children.append(ROUTE2386)
ROUTE2387 = x3d.ROUTE()
ROUTE2387.fromField = "value_changed"
ROUTE2387.fromNode = "Pitches_l_knee_RotationInterpolator"
ROUTE2387.toField = "rotation"
ROUTE2387.toNode = "hanim_l_knee"

Group2325.children.append(ROUTE2387)
ROUTE2388 = x3d.ROUTE()
ROUTE2388.fromField = "value_changed"
ROUTE2388.fromNode = "Pitches_l_hip_RotationInterpolator"
ROUTE2388.toField = "rotation"
ROUTE2388.toNode = "hanim_l_hip"

Group2325.children.append(ROUTE2388)
ROUTE2389 = x3d.ROUTE()
ROUTE2389.fromField = "value_changed"
ROUTE2389.fromNode = "Pitches_lower_body_RotationInterpolator"
ROUTE2389.toField = "rotation"
ROUTE2389.toNode = "hanim_sacroiliac"

Group2325.children.append(ROUTE2389)
ROUTE2390 = x3d.ROUTE()
ROUTE2390.fromField = "value_changed"
ROUTE2390.fromNode = "Pitches_r_wrist_RotationInterpolator"
ROUTE2390.toField = "rotation"
ROUTE2390.toNode = "hanim_r_wrist"

Group2325.children.append(ROUTE2390)
ROUTE2391 = x3d.ROUTE()
ROUTE2391.fromField = "value_changed"
ROUTE2391.fromNode = "Pitches_r_elbow_RotationInterpolator"
ROUTE2391.toField = "rotation"
ROUTE2391.toNode = "hanim_r_elbow"

Group2325.children.append(ROUTE2391)
ROUTE2392 = x3d.ROUTE()
ROUTE2392.fromField = "value_changed"
ROUTE2392.fromNode = "Pitches_r_shoulder_RotationInterpolator"
ROUTE2392.toField = "rotation"
ROUTE2392.toNode = "hanim_r_shoulder"

Group2325.children.append(ROUTE2392)
ROUTE2393 = x3d.ROUTE()
ROUTE2393.fromField = "value_changed"
ROUTE2393.fromNode = "Pitches_l_wrist_RotationInterpolator"
ROUTE2393.toField = "rotation"
ROUTE2393.toNode = "hanim_l_wrist"

Group2325.children.append(ROUTE2393)
ROUTE2394 = x3d.ROUTE()
ROUTE2394.fromField = "value_changed"
ROUTE2394.fromNode = "Pitches_l_elbow_RotationInterpolator"
ROUTE2394.toField = "rotation"
ROUTE2394.toNode = "hanim_l_elbow"

Group2325.children.append(ROUTE2394)
ROUTE2395 = x3d.ROUTE()
ROUTE2395.fromField = "value_changed"
ROUTE2395.fromNode = "Pitches_l_shoulder_RotationInterpolator"
ROUTE2395.toField = "rotation"
ROUTE2395.toNode = "hanim_l_shoulder"

Group2325.children.append(ROUTE2395)
ROUTE2396 = x3d.ROUTE()
ROUTE2396.fromField = "value_changed"
ROUTE2396.fromNode = "Pitches_head_RotationInterpolator"
ROUTE2396.toField = "rotation"
ROUTE2396.toNode = "hanim_skullbase"

Group2325.children.append(ROUTE2396)
ROUTE2397 = x3d.ROUTE()
ROUTE2397.fromField = "value_changed"
ROUTE2397.fromNode = "Pitches_neck_RotationInterpolator"
ROUTE2397.toField = "rotation"
ROUTE2397.toNode = "hanim_vc4"

Group2325.children.append(ROUTE2397)
ROUTE2398 = x3d.ROUTE()
ROUTE2398.fromField = "value_changed"
ROUTE2398.fromNode = "Pitches_upper_body_RotationInterpolator"
ROUTE2398.toField = "rotation"
ROUTE2398.toNode = "hanim_vl1"

Group2325.children.append(ROUTE2398)
ROUTE2399 = x3d.ROUTE()
ROUTE2399.fromField = "value_changed"
ROUTE2399.fromNode = "Pitches_whole_body_RotationInterpolator"
ROUTE2399.toField = "rotation"
ROUTE2399.toNode = "hanim_humanoid_root"

Group2325.children.append(ROUTE2399)
ROUTE2400 = x3d.ROUTE()
ROUTE2400.fromField = "value_changed"
ROUTE2400.fromNode = "Pitches_whole_body_TranslationInterpolator"
ROUTE2400.toField = "translation"
ROUTE2400.toNode = "hanim_humanoid_root"

Group2325.children.append(ROUTE2400)
ROUTE2401 = x3d.ROUTE()
ROUTE2401.fromField = "value_changed"
ROUTE2401.fromNode = "Pitch_l_sternoclavicular_RollInterpolator"
ROUTE2401.toField = "rotation"
ROUTE2401.toNode = "hanim_l_sternoclavicular"

Group2325.children.append(ROUTE2401)
ROUTE2402 = x3d.ROUTE()
ROUTE2402.fromField = "value_changed"
ROUTE2402.fromNode = "Pitch_l_acromioclavicular_RollInterpolator"
ROUTE2402.toField = "rotation"
ROUTE2402.toNode = "hanim_l_acromioclavicular"

Group2325.children.append(ROUTE2402)
ROUTE2403 = x3d.ROUTE()
ROUTE2403.fromField = "value_changed"
ROUTE2403.fromNode = "Pitch_r_sternoclavicular_RollInterpolator"
ROUTE2403.toField = "rotation"
ROUTE2403.toNode = "hanim_r_sternoclavicular"

Group2325.children.append(ROUTE2403)
ROUTE2404 = x3d.ROUTE()
ROUTE2404.fromField = "value_changed"
ROUTE2404.fromNode = "Pitch_r_acromioclavicular_RollInterpolator"
ROUTE2404.toField = "rotation"
ROUTE2404.toNode = "hanim_r_acromioclavicular"

Group2325.children.append(ROUTE2404)
ROUTE2405 = x3d.ROUTE()
ROUTE2405.fromField = "value_changed"
ROUTE2405.fromNode = "Pitch_r_metatarsal_PitchInterpolator"
ROUTE2405.toField = "rotation"
ROUTE2405.toNode = "hanim_l_metatarsal"

Group2325.children.append(ROUTE2405)
ROUTE2406 = x3d.ROUTE()
ROUTE2406.fromField = "value_changed"
ROUTE2406.fromNode = "Pitch_r_metatarsal_PitchInterpolator"
ROUTE2406.toField = "rotation"
ROUTE2406.toNode = "hanim_r_metatarsal"

Group2325.children.append(ROUTE2406)
ROUTE2407 = x3d.ROUTE()
ROUTE2407.fromField = "value_changed"
ROUTE2407.fromNode = "Pitch_sacroiliac_YawInterpolator"
ROUTE2407.toField = "rotation"
ROUTE2407.toNode = "hanim_sacroiliac"

Group2325.children.append(ROUTE2407)
ROUTE2408 = x3d.ROUTE()
ROUTE2408.fromField = "value_changed"
ROUTE2408.fromNode = "Pitch_vl5_YawInterpolator"
ROUTE2408.toField = "rotation"
ROUTE2408.toNode = "hanim_vl5"

Group2325.children.append(ROUTE2408)
ROUTE2409 = x3d.ROUTE()
ROUTE2409.fromField = "value_changed"
ROUTE2409.fromNode = "Pitch_vc6_YawInterpolator"
ROUTE2409.toField = "rotation"
ROUTE2409.toNode = "hanim_vc6"

Group2325.children.append(ROUTE2409)
ROUTE2410 = x3d.ROUTE()
ROUTE2410.fromField = "value_changed"
ROUTE2410.fromNode = "Pitch_l_thumb1_PitchInterpolator"
ROUTE2410.toField = "rotation"
ROUTE2410.toNode = "hanim_l_thumb1"

Group2325.children.append(ROUTE2410)
ROUTE2411 = x3d.ROUTE()
ROUTE2411.fromField = "value_changed"
ROUTE2411.fromNode = "Pitch_r_thumb1_PitchInterpolator"
ROUTE2411.toField = "rotation"
ROUTE2411.toNode = "hanim_r_thumb1"

Group2325.children.append(ROUTE2411)

Scene30.children.append(Group2325)
Group2412 = x3d.Group()
Group2412.DEF = "YawsAnimation"
TimeSensor2413 = x3d.TimeSensor()
TimeSensor2413.DEF = "YawTimer"
TimeSensor2413.cycleInterval = 5.73
TimeSensor2413.loop = True

Group2412.children.append(TimeSensor2413)
OrientationInterpolator2414 = x3d.OrientationInterpolator()
OrientationInterpolator2414.DEF = "Yaw_r_metatarsal_PitchInterpolator"
OrientationInterpolator2414.key = [0,0.2,0.4,0.6,0.7,1]
OrientationInterpolator2414.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2412.children.append(OrientationInterpolator2414)
OrientationInterpolator2415 = x3d.OrientationInterpolator()
OrientationInterpolator2415.DEF = "Yaws_r_ankle_RotationInterpolator"
OrientationInterpolator2415.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator2415.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,-1.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000,0.0000,1.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000)

Group2412.children.append(OrientationInterpolator2415)
OrientationInterpolator2416 = x3d.OrientationInterpolator()
OrientationInterpolator2416.DEF = "Yaws_r_knee_RotationInterpolator"
OrientationInterpolator2416.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator2416.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,1.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000,0.0000,-1.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000)

Group2412.children.append(OrientationInterpolator2416)
OrientationInterpolator2417 = x3d.OrientationInterpolator()
OrientationInterpolator2417.DEF = "Yaws_r_hip_RotationInterpolator"
OrientationInterpolator2417.key = [0,0.5,1]
OrientationInterpolator2417.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2412.children.append(OrientationInterpolator2417)
OrientationInterpolator2418 = x3d.OrientationInterpolator()
OrientationInterpolator2418.DEF = "Yaws_l_ankle_RotationInterpolator"
OrientationInterpolator2418.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator2418.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,1.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000,0.0000,-1.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000)

Group2412.children.append(OrientationInterpolator2418)
OrientationInterpolator2419 = x3d.OrientationInterpolator()
OrientationInterpolator2419.DEF = "Yaws_l_knee_RotationInterpolator"
OrientationInterpolator2419.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator2419.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,-1.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000,0.0000,1.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000)

Group2412.children.append(OrientationInterpolator2419)
OrientationInterpolator2420 = x3d.OrientationInterpolator()
OrientationInterpolator2420.DEF = "Yaws_l_hip_RotationInterpolator"
OrientationInterpolator2420.key = [0,0.5,1]
OrientationInterpolator2420.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2412.children.append(OrientationInterpolator2420)
OrientationInterpolator2421 = x3d.OrientationInterpolator()
OrientationInterpolator2421.DEF = "Yaws_r_wrist_RotationInterpolator"
OrientationInterpolator2421.key = [0,0.5,1]
OrientationInterpolator2421.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2412.children.append(OrientationInterpolator2421)
OrientationInterpolator2422 = x3d.OrientationInterpolator()
OrientationInterpolator2422.DEF = "Yaws_r_elbow_RotationInterpolator"
OrientationInterpolator2422.key = [0,0.5,1]
OrientationInterpolator2422.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2412.children.append(OrientationInterpolator2422)
OrientationInterpolator2423 = x3d.OrientationInterpolator()
OrientationInterpolator2423.DEF = "Yaws_r_shoulder_RotationInterpolator"
OrientationInterpolator2423.key = [0,0.5,1]
OrientationInterpolator2423.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2412.children.append(OrientationInterpolator2423)
OrientationInterpolator2424 = x3d.OrientationInterpolator()
OrientationInterpolator2424.DEF = "Yaws_l_wrist_RotationInterpolator"
OrientationInterpolator2424.key = [0,0.5,1]
OrientationInterpolator2424.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2412.children.append(OrientationInterpolator2424)
OrientationInterpolator2425 = x3d.OrientationInterpolator()
OrientationInterpolator2425.DEF = "Yaws_l_elbow_RotationInterpolator"
OrientationInterpolator2425.key = [0,0.5,1]
OrientationInterpolator2425.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2412.children.append(OrientationInterpolator2425)
OrientationInterpolator2426 = x3d.OrientationInterpolator()
OrientationInterpolator2426.DEF = "Yaws_l_shoulder_RotationInterpolator"
OrientationInterpolator2426.key = [0,0.5,1]
OrientationInterpolator2426.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2412.children.append(OrientationInterpolator2426)
OrientationInterpolator2427 = x3d.OrientationInterpolator()
OrientationInterpolator2427.DEF = "Yaws_head_RotationInterpolator"
OrientationInterpolator2427.key = [0,0.5,1]
OrientationInterpolator2427.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2412.children.append(OrientationInterpolator2427)
OrientationInterpolator2428 = x3d.OrientationInterpolator()
OrientationInterpolator2428.DEF = "Yaws_neck_RotationInterpolator"
OrientationInterpolator2428.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator2428.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,1.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000,0.0000,-1.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000)

Group2412.children.append(OrientationInterpolator2428)
OrientationInterpolator2429 = x3d.OrientationInterpolator()
OrientationInterpolator2429.DEF = "Yaws_upper_body_RotationInterpolator"
OrientationInterpolator2429.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator2429.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,-1.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000,0.0000,1.0000,0.0000,1.5000,0.0000,0.0000,1.0000,0.0000)

Group2412.children.append(OrientationInterpolator2429)
OrientationInterpolator2430 = x3d.OrientationInterpolator()
OrientationInterpolator2430.DEF = "Yaws_lower_body_RotationInterpolator"
OrientationInterpolator2430.key = [0,0.5,1]
OrientationInterpolator2430.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2412.children.append(OrientationInterpolator2430)
OrientationInterpolator2431 = x3d.OrientationInterpolator()
OrientationInterpolator2431.DEF = "Yaws_whole_body_RotationInterpolator"
OrientationInterpolator2431.key = [0,0.5,1]
OrientationInterpolator2431.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2412.children.append(OrientationInterpolator2431)
PositionInterpolator2432 = x3d.PositionInterpolator()
PositionInterpolator2432.DEF = "Yaws_whole_body_TranslationInterpolator"
PositionInterpolator2432.key = [0,0.5,1]
PositionInterpolator2432.keyValue = (0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000)

Group2412.children.append(PositionInterpolator2432)
OrientationInterpolator2433 = x3d.OrientationInterpolator()
OrientationInterpolator2433.DEF = "Yaw_l_sternoclavicular_RollInterpolator"
OrientationInterpolator2433.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2433.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2412.children.append(OrientationInterpolator2433)
OrientationInterpolator2434 = x3d.OrientationInterpolator()
OrientationInterpolator2434.DEF = "Yaw_l_acromioclavicular_RollInterpolator"
OrientationInterpolator2434.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2434.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2412.children.append(OrientationInterpolator2434)
OrientationInterpolator2435 = x3d.OrientationInterpolator()
OrientationInterpolator2435.DEF = "Yaw_r_sternoclavicular_RollInterpolator"
OrientationInterpolator2435.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2435.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2412.children.append(OrientationInterpolator2435)
OrientationInterpolator2436 = x3d.OrientationInterpolator()
OrientationInterpolator2436.DEF = "Yaw_r_acromioclavicular_RollInterpolator"
OrientationInterpolator2436.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2436.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2412.children.append(OrientationInterpolator2436)
OrientationInterpolator2437 = x3d.OrientationInterpolator()
OrientationInterpolator2437.DEF = "Yaw_sacroiliac_YawInterpolator"
OrientationInterpolator2437.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2437.keyValue = (0.0000,1.0000,0.0000,0.0000,0.0000,-1.0000,0.0000,0.1000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.2400,0.0000,-1.0000,0.0000,0.4000,0.0000,1.0000,0.0000,0.0000)

Group2412.children.append(OrientationInterpolator2437)
OrientationInterpolator2438 = x3d.OrientationInterpolator()
OrientationInterpolator2438.DEF = "Yaw_vl5_YawInterpolator"
OrientationInterpolator2438.key = [0,0.2,0.4,0.5,0.6,0.8,1]
OrientationInterpolator2438.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2412.children.append(OrientationInterpolator2438)
OrientationInterpolator2439 = x3d.OrientationInterpolator()
OrientationInterpolator2439.DEF = "Yaw_vc6_YawInterpolator"
OrientationInterpolator2439.key = [0,0.2,0.4,0.5,0.6,0.8,1]
OrientationInterpolator2439.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2412.children.append(OrientationInterpolator2439)
OrientationInterpolator2440 = x3d.OrientationInterpolator()
OrientationInterpolator2440.DEF = "Yaw_l_thumb1_PitchInterpolator"
OrientationInterpolator2440.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2440.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2412.children.append(OrientationInterpolator2440)
OrientationInterpolator2441 = x3d.OrientationInterpolator()
OrientationInterpolator2441.DEF = "Yaw_r_thumb1_PitchInterpolator"
OrientationInterpolator2441.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2441.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2412.children.append(OrientationInterpolator2441)
ROUTE2442 = x3d.ROUTE()
ROUTE2442.fromField = "fraction_changed"
ROUTE2442.fromNode = "YawTimer"
ROUTE2442.toField = "set_fraction"
ROUTE2442.toNode = "Yaws_r_ankle_RotationInterpolator"

Group2412.children.append(ROUTE2442)
ROUTE2443 = x3d.ROUTE()
ROUTE2443.fromField = "fraction_changed"
ROUTE2443.fromNode = "YawTimer"
ROUTE2443.toField = "set_fraction"
ROUTE2443.toNode = "Yaws_r_knee_RotationInterpolator"

Group2412.children.append(ROUTE2443)
ROUTE2444 = x3d.ROUTE()
ROUTE2444.fromField = "fraction_changed"
ROUTE2444.fromNode = "YawTimer"
ROUTE2444.toField = "set_fraction"
ROUTE2444.toNode = "Yaws_r_hip_RotationInterpolator"

Group2412.children.append(ROUTE2444)
ROUTE2445 = x3d.ROUTE()
ROUTE2445.fromField = "fraction_changed"
ROUTE2445.fromNode = "YawTimer"
ROUTE2445.toField = "set_fraction"
ROUTE2445.toNode = "Yaws_l_ankle_RotationInterpolator"

Group2412.children.append(ROUTE2445)
ROUTE2446 = x3d.ROUTE()
ROUTE2446.fromField = "fraction_changed"
ROUTE2446.fromNode = "YawTimer"
ROUTE2446.toField = "set_fraction"
ROUTE2446.toNode = "Yaws_l_knee_RotationInterpolator"

Group2412.children.append(ROUTE2446)
ROUTE2447 = x3d.ROUTE()
ROUTE2447.fromField = "fraction_changed"
ROUTE2447.fromNode = "YawTimer"
ROUTE2447.toField = "set_fraction"
ROUTE2447.toNode = "Yaws_l_hip_RotationInterpolator"

Group2412.children.append(ROUTE2447)
ROUTE2448 = x3d.ROUTE()
ROUTE2448.fromField = "fraction_changed"
ROUTE2448.fromNode = "YawTimer"
ROUTE2448.toField = "set_fraction"
ROUTE2448.toNode = "Yaws_lower_body_RotationInterpolator"

Group2412.children.append(ROUTE2448)
ROUTE2449 = x3d.ROUTE()
ROUTE2449.fromField = "fraction_changed"
ROUTE2449.fromNode = "YawTimer"
ROUTE2449.toField = "set_fraction"
ROUTE2449.toNode = "Yaws_r_wrist_RotationInterpolator"

Group2412.children.append(ROUTE2449)
ROUTE2450 = x3d.ROUTE()
ROUTE2450.fromField = "fraction_changed"
ROUTE2450.fromNode = "YawTimer"
ROUTE2450.toField = "set_fraction"
ROUTE2450.toNode = "Yaws_r_elbow_RotationInterpolator"

Group2412.children.append(ROUTE2450)
ROUTE2451 = x3d.ROUTE()
ROUTE2451.fromField = "fraction_changed"
ROUTE2451.fromNode = "YawTimer"
ROUTE2451.toField = "set_fraction"
ROUTE2451.toNode = "Yaws_r_shoulder_RotationInterpolator"

Group2412.children.append(ROUTE2451)
ROUTE2452 = x3d.ROUTE()
ROUTE2452.fromField = "fraction_changed"
ROUTE2452.fromNode = "YawTimer"
ROUTE2452.toField = "set_fraction"
ROUTE2452.toNode = "Yaws_l_wrist_RotationInterpolator"

Group2412.children.append(ROUTE2452)
ROUTE2453 = x3d.ROUTE()
ROUTE2453.fromField = "fraction_changed"
ROUTE2453.fromNode = "YawTimer"
ROUTE2453.toField = "set_fraction"
ROUTE2453.toNode = "Yaws_l_elbow_RotationInterpolator"

Group2412.children.append(ROUTE2453)
ROUTE2454 = x3d.ROUTE()
ROUTE2454.fromField = "fraction_changed"
ROUTE2454.fromNode = "YawTimer"
ROUTE2454.toField = "set_fraction"
ROUTE2454.toNode = "Yaws_l_shoulder_RotationInterpolator"

Group2412.children.append(ROUTE2454)
ROUTE2455 = x3d.ROUTE()
ROUTE2455.fromField = "fraction_changed"
ROUTE2455.fromNode = "YawTimer"
ROUTE2455.toField = "set_fraction"
ROUTE2455.toNode = "Yaws_head_RotationInterpolator"

Group2412.children.append(ROUTE2455)
ROUTE2456 = x3d.ROUTE()
ROUTE2456.fromField = "fraction_changed"
ROUTE2456.fromNode = "YawTimer"
ROUTE2456.toField = "set_fraction"
ROUTE2456.toNode = "Yaws_neck_RotationInterpolator"

Group2412.children.append(ROUTE2456)
ROUTE2457 = x3d.ROUTE()
ROUTE2457.fromField = "fraction_changed"
ROUTE2457.fromNode = "YawTimer"
ROUTE2457.toField = "set_fraction"
ROUTE2457.toNode = "Yaws_upper_body_RotationInterpolator"

Group2412.children.append(ROUTE2457)
ROUTE2458 = x3d.ROUTE()
ROUTE2458.fromField = "fraction_changed"
ROUTE2458.fromNode = "YawTimer"
ROUTE2458.toField = "set_fraction"
ROUTE2458.toNode = "Yaws_whole_body_RotationInterpolator"

Group2412.children.append(ROUTE2458)
ROUTE2459 = x3d.ROUTE()
ROUTE2459.fromField = "fraction_changed"
ROUTE2459.fromNode = "YawTimer"
ROUTE2459.toField = "set_fraction"
ROUTE2459.toNode = "Yaws_whole_body_TranslationInterpolator"

Group2412.children.append(ROUTE2459)
ROUTE2460 = x3d.ROUTE()
ROUTE2460.fromField = "fraction_changed"
ROUTE2460.fromNode = "YawTimer"
ROUTE2460.toField = "set_fraction"
ROUTE2460.toNode = "Yaw_l_sternoclavicular_RollInterpolator"

Group2412.children.append(ROUTE2460)
ROUTE2461 = x3d.ROUTE()
ROUTE2461.fromField = "fraction_changed"
ROUTE2461.fromNode = "YawTimer"
ROUTE2461.toField = "set_fraction"
ROUTE2461.toNode = "Yaw_l_acromioclavicular_RollInterpolator"

Group2412.children.append(ROUTE2461)
ROUTE2462 = x3d.ROUTE()
ROUTE2462.fromField = "fraction_changed"
ROUTE2462.fromNode = "YawTimer"
ROUTE2462.toField = "set_fraction"
ROUTE2462.toNode = "Yaw_r_sternoclavicular_RollInterpolator"

Group2412.children.append(ROUTE2462)
ROUTE2463 = x3d.ROUTE()
ROUTE2463.fromField = "fraction_changed"
ROUTE2463.fromNode = "YawTimer"
ROUTE2463.toField = "set_fraction"
ROUTE2463.toNode = "Yaw_r_acromioclavicular_RollInterpolator"

Group2412.children.append(ROUTE2463)
ROUTE2464 = x3d.ROUTE()
ROUTE2464.fromField = "fraction_changed"
ROUTE2464.fromNode = "YawTimer"
ROUTE2464.toField = "set_fraction"
ROUTE2464.toNode = "Yaw_r_metatarsal_PitchInterpolator"

Group2412.children.append(ROUTE2464)
ROUTE2465 = x3d.ROUTE()
ROUTE2465.fromField = "fraction_changed"
ROUTE2465.fromNode = "YawTimer"
ROUTE2465.toField = "set_fraction"
ROUTE2465.toNode = "Yaw_sacroiliac_YawInterpolator"

Group2412.children.append(ROUTE2465)
ROUTE2466 = x3d.ROUTE()
ROUTE2466.fromField = "fraction_changed"
ROUTE2466.fromNode = "YawTimer"
ROUTE2466.toField = "set_fraction"
ROUTE2466.toNode = "Yaw_vl5_YawInterpolator"

Group2412.children.append(ROUTE2466)
ROUTE2467 = x3d.ROUTE()
ROUTE2467.fromField = "fraction_changed"
ROUTE2467.fromNode = "YawTimer"
ROUTE2467.toField = "set_fraction"
ROUTE2467.toNode = "Yaw_vc6_YawInterpolator"

Group2412.children.append(ROUTE2467)
ROUTE2468 = x3d.ROUTE()
ROUTE2468.fromField = "fraction_changed"
ROUTE2468.fromNode = "YawTimer"
ROUTE2468.toField = "set_fraction"
ROUTE2468.toNode = "Yaw_l_thumb1_PitchInterpolator"

Group2412.children.append(ROUTE2468)
ROUTE2469 = x3d.ROUTE()
ROUTE2469.fromField = "fraction_changed"
ROUTE2469.fromNode = "YawTimer"
ROUTE2469.toField = "set_fraction"
ROUTE2469.toNode = "Yaw_r_thumb1_PitchInterpolator"

Group2412.children.append(ROUTE2469)
ROUTE2470 = x3d.ROUTE()
ROUTE2470.fromField = "value_changed"
ROUTE2470.fromNode = "Yaws_r_ankle_RotationInterpolator"
ROUTE2470.toField = "rotation"
ROUTE2470.toNode = "hanim_r_ankle"

Group2412.children.append(ROUTE2470)
ROUTE2471 = x3d.ROUTE()
ROUTE2471.fromField = "value_changed"
ROUTE2471.fromNode = "Yaws_r_knee_RotationInterpolator"
ROUTE2471.toField = "rotation"
ROUTE2471.toNode = "hanim_r_knee"

Group2412.children.append(ROUTE2471)
ROUTE2472 = x3d.ROUTE()
ROUTE2472.fromField = "value_changed"
ROUTE2472.fromNode = "Yaws_r_hip_RotationInterpolator"
ROUTE2472.toField = "rotation"
ROUTE2472.toNode = "hanim_r_hip"

Group2412.children.append(ROUTE2472)
ROUTE2473 = x3d.ROUTE()
ROUTE2473.fromField = "value_changed"
ROUTE2473.fromNode = "Yaws_l_ankle_RotationInterpolator"
ROUTE2473.toField = "rotation"
ROUTE2473.toNode = "hanim_l_ankle"

Group2412.children.append(ROUTE2473)
ROUTE2474 = x3d.ROUTE()
ROUTE2474.fromField = "value_changed"
ROUTE2474.fromNode = "Yaws_l_knee_RotationInterpolator"
ROUTE2474.toField = "rotation"
ROUTE2474.toNode = "hanim_l_knee"

Group2412.children.append(ROUTE2474)
ROUTE2475 = x3d.ROUTE()
ROUTE2475.fromField = "value_changed"
ROUTE2475.fromNode = "Yaws_l_hip_RotationInterpolator"
ROUTE2475.toField = "rotation"
ROUTE2475.toNode = "hanim_l_hip"

Group2412.children.append(ROUTE2475)
ROUTE2476 = x3d.ROUTE()
ROUTE2476.fromField = "value_changed"
ROUTE2476.fromNode = "Yaws_lower_body_RotationInterpolator"
ROUTE2476.toField = "rotation"
ROUTE2476.toNode = "hanim_sacroiliac"

Group2412.children.append(ROUTE2476)
ROUTE2477 = x3d.ROUTE()
ROUTE2477.fromField = "value_changed"
ROUTE2477.fromNode = "Yaws_r_wrist_RotationInterpolator"
ROUTE2477.toField = "rotation"
ROUTE2477.toNode = "hanim_r_wrist"

Group2412.children.append(ROUTE2477)
ROUTE2478 = x3d.ROUTE()
ROUTE2478.fromField = "value_changed"
ROUTE2478.fromNode = "Yaws_r_elbow_RotationInterpolator"
ROUTE2478.toField = "rotation"
ROUTE2478.toNode = "hanim_r_elbow"

Group2412.children.append(ROUTE2478)
ROUTE2479 = x3d.ROUTE()
ROUTE2479.fromField = "value_changed"
ROUTE2479.fromNode = "Yaws_r_shoulder_RotationInterpolator"
ROUTE2479.toField = "rotation"
ROUTE2479.toNode = "hanim_r_shoulder"

Group2412.children.append(ROUTE2479)
ROUTE2480 = x3d.ROUTE()
ROUTE2480.fromField = "value_changed"
ROUTE2480.fromNode = "Yaws_l_wrist_RotationInterpolator"
ROUTE2480.toField = "rotation"
ROUTE2480.toNode = "hanim_l_wrist"

Group2412.children.append(ROUTE2480)
ROUTE2481 = x3d.ROUTE()
ROUTE2481.fromField = "value_changed"
ROUTE2481.fromNode = "Yaws_l_elbow_RotationInterpolator"
ROUTE2481.toField = "rotation"
ROUTE2481.toNode = "hanim_l_elbow"

Group2412.children.append(ROUTE2481)
ROUTE2482 = x3d.ROUTE()
ROUTE2482.fromField = "value_changed"
ROUTE2482.fromNode = "Yaws_l_shoulder_RotationInterpolator"
ROUTE2482.toField = "rotation"
ROUTE2482.toNode = "hanim_l_shoulder"

Group2412.children.append(ROUTE2482)
ROUTE2483 = x3d.ROUTE()
ROUTE2483.fromField = "value_changed"
ROUTE2483.fromNode = "Yaws_head_RotationInterpolator"
ROUTE2483.toField = "rotation"
ROUTE2483.toNode = "hanim_skullbase"

Group2412.children.append(ROUTE2483)
ROUTE2484 = x3d.ROUTE()
ROUTE2484.fromField = "value_changed"
ROUTE2484.fromNode = "Yaws_neck_RotationInterpolator"
ROUTE2484.toField = "rotation"
ROUTE2484.toNode = "hanim_vc4"

Group2412.children.append(ROUTE2484)
ROUTE2485 = x3d.ROUTE()
ROUTE2485.fromField = "value_changed"
ROUTE2485.fromNode = "Yaws_upper_body_RotationInterpolator"
ROUTE2485.toField = "rotation"
ROUTE2485.toNode = "hanim_vl1"

Group2412.children.append(ROUTE2485)
ROUTE2486 = x3d.ROUTE()
ROUTE2486.fromField = "value_changed"
ROUTE2486.fromNode = "Yaws_whole_body_RotationInterpolator"
ROUTE2486.toField = "rotation"
ROUTE2486.toNode = "hanim_humanoid_root"

Group2412.children.append(ROUTE2486)
ROUTE2487 = x3d.ROUTE()
ROUTE2487.fromField = "value_changed"
ROUTE2487.fromNode = "Yaws_whole_body_TranslationInterpolator"
ROUTE2487.toField = "translation"
ROUTE2487.toNode = "hanim_humanoid_root"

Group2412.children.append(ROUTE2487)
ROUTE2488 = x3d.ROUTE()
ROUTE2488.fromField = "value_changed"
ROUTE2488.fromNode = "Yaw_l_sternoclavicular_RollInterpolator"
ROUTE2488.toField = "rotation"
ROUTE2488.toNode = "hanim_l_sternoclavicular"

Group2412.children.append(ROUTE2488)
ROUTE2489 = x3d.ROUTE()
ROUTE2489.fromField = "value_changed"
ROUTE2489.fromNode = "Yaw_l_acromioclavicular_RollInterpolator"
ROUTE2489.toField = "rotation"
ROUTE2489.toNode = "hanim_l_acromioclavicular"

Group2412.children.append(ROUTE2489)
ROUTE2490 = x3d.ROUTE()
ROUTE2490.fromField = "value_changed"
ROUTE2490.fromNode = "Yaw_r_sternoclavicular_RollInterpolator"
ROUTE2490.toField = "rotation"
ROUTE2490.toNode = "hanim_r_sternoclavicular"

Group2412.children.append(ROUTE2490)
ROUTE2491 = x3d.ROUTE()
ROUTE2491.fromField = "value_changed"
ROUTE2491.fromNode = "Yaw_r_acromioclavicular_RollInterpolator"
ROUTE2491.toField = "rotation"
ROUTE2491.toNode = "hanim_r_acromioclavicular"

Group2412.children.append(ROUTE2491)
ROUTE2492 = x3d.ROUTE()
ROUTE2492.fromField = "value_changed"
ROUTE2492.fromNode = "Yaw_r_metatarsal_PitchInterpolator"
ROUTE2492.toField = "rotation"
ROUTE2492.toNode = "hanim_l_metatarsal"

Group2412.children.append(ROUTE2492)
ROUTE2493 = x3d.ROUTE()
ROUTE2493.fromField = "value_changed"
ROUTE2493.fromNode = "Yaw_r_metatarsal_PitchInterpolator"
ROUTE2493.toField = "rotation"
ROUTE2493.toNode = "hanim_r_metatarsal"

Group2412.children.append(ROUTE2493)
ROUTE2494 = x3d.ROUTE()
ROUTE2494.fromField = "value_changed"
ROUTE2494.fromNode = "Yaw_sacroiliac_YawInterpolator"
ROUTE2494.toField = "rotation"
ROUTE2494.toNode = "hanim_sacroiliac"

Group2412.children.append(ROUTE2494)
ROUTE2495 = x3d.ROUTE()
ROUTE2495.fromField = "value_changed"
ROUTE2495.fromNode = "Yaw_vl5_YawInterpolator"
ROUTE2495.toField = "rotation"
ROUTE2495.toNode = "hanim_vl5"

Group2412.children.append(ROUTE2495)
ROUTE2496 = x3d.ROUTE()
ROUTE2496.fromField = "value_changed"
ROUTE2496.fromNode = "Yaw_vc6_YawInterpolator"
ROUTE2496.toField = "rotation"
ROUTE2496.toNode = "hanim_vc6"

Group2412.children.append(ROUTE2496)
ROUTE2497 = x3d.ROUTE()
ROUTE2497.fromField = "value_changed"
ROUTE2497.fromNode = "Yaw_l_thumb1_PitchInterpolator"
ROUTE2497.toField = "rotation"
ROUTE2497.toNode = "hanim_l_thumb1"

Group2412.children.append(ROUTE2497)
ROUTE2498 = x3d.ROUTE()
ROUTE2498.fromField = "value_changed"
ROUTE2498.fromNode = "Yaw_r_thumb1_PitchInterpolator"
ROUTE2498.toField = "rotation"
ROUTE2498.toNode = "hanim_r_thumb1"

Group2412.children.append(ROUTE2498)

Scene30.children.append(Group2412)
Group2499 = x3d.Group()
Group2499.DEF = "RollsAnimation"
TimeSensor2500 = x3d.TimeSensor()
TimeSensor2500.DEF = "RollTimer"
TimeSensor2500.cycleInterval = 5.73
TimeSensor2500.loop = True

Group2499.children.append(TimeSensor2500)
OrientationInterpolator2501 = x3d.OrientationInterpolator()
OrientationInterpolator2501.DEF = "Roll_r_metatarsal_PitchInterpolator"
OrientationInterpolator2501.key = [0,0.2,0.4,0.6,0.7,1]
OrientationInterpolator2501.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2499.children.append(OrientationInterpolator2501)
OrientationInterpolator2502 = x3d.OrientationInterpolator()
OrientationInterpolator2502.DEF = "Rolls_r_ankle_RotationInterpolator"
OrientationInterpolator2502.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator2502.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,1.5000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,1.5000,0.0000,0.0000,1.0000,0.0000)

Group2499.children.append(OrientationInterpolator2502)
OrientationInterpolator2503 = x3d.OrientationInterpolator()
OrientationInterpolator2503.DEF = "Rolls_r_knee_RotationInterpolator"
OrientationInterpolator2503.key = [0,0.5,1]
OrientationInterpolator2503.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2499.children.append(OrientationInterpolator2503)
OrientationInterpolator2504 = x3d.OrientationInterpolator()
OrientationInterpolator2504.DEF = "Rolls_r_hip_RotationInterpolator"
OrientationInterpolator2504.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator2504.keyValue = (0.0000,0.0000,-1.0000,0.0000,0.0000,0.0000,-1.0000,1.5000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,-1.0000,1.5000,0.0000,0.0000,1.0000,0.0000)

Group2499.children.append(OrientationInterpolator2504)
OrientationInterpolator2505 = x3d.OrientationInterpolator()
OrientationInterpolator2505.DEF = "Rolls_l_ankle_RotationInterpolator"
OrientationInterpolator2505.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator2505.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,-1.0000,1.5000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,-1.0000,1.5000,0.0000,0.0000,1.0000,0.0000)

Group2499.children.append(OrientationInterpolator2505)
OrientationInterpolator2506 = x3d.OrientationInterpolator()
OrientationInterpolator2506.DEF = "Rolls_l_knee_RotationInterpolator"
OrientationInterpolator2506.key = [0,0.5,1]
OrientationInterpolator2506.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2499.children.append(OrientationInterpolator2506)
OrientationInterpolator2507 = x3d.OrientationInterpolator()
OrientationInterpolator2507.DEF = "Rolls_l_hip_RotationInterpolator"
OrientationInterpolator2507.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator2507.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,1.5000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,1.5000,0.0000,0.0000,1.0000,0.0000)

Group2499.children.append(OrientationInterpolator2507)
OrientationInterpolator2508 = x3d.OrientationInterpolator()
OrientationInterpolator2508.DEF = "Rolls_r_wrist_RotationInterpolator"
OrientationInterpolator2508.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator2508.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,-1.0000,1.5000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,1.5000,0.0000,0.0000,1.0000,0.0000)

Group2499.children.append(OrientationInterpolator2508)
OrientationInterpolator2509 = x3d.OrientationInterpolator()
OrientationInterpolator2509.DEF = "Rolls_r_elbow_RotationInterpolator"
OrientationInterpolator2509.key = [0,0.5,1]
OrientationInterpolator2509.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2499.children.append(OrientationInterpolator2509)
OrientationInterpolator2510 = x3d.OrientationInterpolator()
OrientationInterpolator2510.DEF = "Rolls_r_shoulder_RotationInterpolator"
OrientationInterpolator2510.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator2510.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,-1.0000,1.5000,0.0000,0.0000,-1.0000,3.0000,0.0000,0.0000,-1.0000,1.5000,0.0000,0.0000,1.0000,0.0000)

Group2499.children.append(OrientationInterpolator2510)
OrientationInterpolator2511 = x3d.OrientationInterpolator()
OrientationInterpolator2511.DEF = "Rolls_l_wrist_RotationInterpolator"
OrientationInterpolator2511.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator2511.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,1.5000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,-1.0000,1.5000,0.0000,0.0000,1.0000,0.0000)

Group2499.children.append(OrientationInterpolator2511)
OrientationInterpolator2512 = x3d.OrientationInterpolator()
OrientationInterpolator2512.DEF = "Rolls_l_elbow_RotationInterpolator"
OrientationInterpolator2512.key = [0,0.5,1]
OrientationInterpolator2512.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2499.children.append(OrientationInterpolator2512)
OrientationInterpolator2513 = x3d.OrientationInterpolator()
OrientationInterpolator2513.DEF = "Rolls_l_shoulder_RotationInterpolator"
OrientationInterpolator2513.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator2513.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,1.5000,0.0000,0.0000,1.0000,3.0000,0.0000,0.0000,1.0000,1.5000,0.0000,0.0000,1.0000,0.0000)

Group2499.children.append(OrientationInterpolator2513)
OrientationInterpolator2514 = x3d.OrientationInterpolator()
OrientationInterpolator2514.DEF = "Rolls_head_RotationInterpolator"
OrientationInterpolator2514.key = [0,0.5,1]
OrientationInterpolator2514.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2499.children.append(OrientationInterpolator2514)
OrientationInterpolator2515 = x3d.OrientationInterpolator()
OrientationInterpolator2515.DEF = "Rolls_neck_RotationInterpolator"
OrientationInterpolator2515.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator2515.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,1.2500,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,-1.0000,1.2500,0.0000,0.0000,1.0000,0.0000)

Group2499.children.append(OrientationInterpolator2515)
OrientationInterpolator2516 = x3d.OrientationInterpolator()
OrientationInterpolator2516.DEF = "Rolls_lower_body_RotationInterpolator"
OrientationInterpolator2516.key = [0,0.5,1]
OrientationInterpolator2516.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2499.children.append(OrientationInterpolator2516)
OrientationInterpolator2517 = x3d.OrientationInterpolator()
OrientationInterpolator2517.DEF = "Rolls_upper_body_RotationInterpolator"
OrientationInterpolator2517.key = [0,0.5,1]
OrientationInterpolator2517.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2499.children.append(OrientationInterpolator2517)
OrientationInterpolator2518 = x3d.OrientationInterpolator()
OrientationInterpolator2518.DEF = "Rolls_whole_body_RotationInterpolator"
OrientationInterpolator2518.key = [0,0.5,1]
OrientationInterpolator2518.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2499.children.append(OrientationInterpolator2518)
PositionInterpolator2519 = x3d.PositionInterpolator()
PositionInterpolator2519.DEF = "Rolls_whole_body_TranslationInterpolator"
PositionInterpolator2519.key = [0,0.125,0.25,0.375,0.5,0.625,0.75,0.875,1]
PositionInterpolator2519.keyValue = (0.0000,0.0000,0.0000,0.0000,-0.2500,0.0000,0.0000,-0.8000,0.0000,0.0000,-0.2500,0.0000,0.0000,0.0000,0.0000,0.0000,-0.2500,0.0000,0.0000,-0.8000,0.0000,0.0000,-0.2500,0.0000,0.0000,0.0000,0.0000)

Group2499.children.append(PositionInterpolator2519)
OrientationInterpolator2520 = x3d.OrientationInterpolator()
OrientationInterpolator2520.DEF = "Roll_l_sternoclavicular_RollInterpolator"
OrientationInterpolator2520.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2520.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.2000,0.0000,0.0000,1.0000,0.2200,0.0000,0.0000,1.0000,0.2000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2499.children.append(OrientationInterpolator2520)
OrientationInterpolator2521 = x3d.OrientationInterpolator()
OrientationInterpolator2521.DEF = "Roll_l_acromioclavicular_RollInterpolator"
OrientationInterpolator2521.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2521.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0500,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2499.children.append(OrientationInterpolator2521)
OrientationInterpolator2522 = x3d.OrientationInterpolator()
OrientationInterpolator2522.DEF = "Roll_r_sternoclavicular_RollInterpolator"
OrientationInterpolator2522.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2522.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,-0.2000,0.0000,0.0000,1.0000,-0.2200,0.0000,0.0000,1.0000,-0.2000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2499.children.append(OrientationInterpolator2522)
OrientationInterpolator2523 = x3d.OrientationInterpolator()
OrientationInterpolator2523.DEF = "Roll_r_acromioclavicular_RollInterpolator"
OrientationInterpolator2523.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2523.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,-0.0500,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2499.children.append(OrientationInterpolator2523)
OrientationInterpolator2524 = x3d.OrientationInterpolator()
OrientationInterpolator2524.DEF = "Roll_sacroiliac_YawInterpolator"
OrientationInterpolator2524.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2524.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2499.children.append(OrientationInterpolator2524)
OrientationInterpolator2525 = x3d.OrientationInterpolator()
OrientationInterpolator2525.DEF = "Roll_vl5_YawInterpolator"
OrientationInterpolator2525.key = [0,0.2,0.4,0.5,0.6,0.8,1]
OrientationInterpolator2525.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2499.children.append(OrientationInterpolator2525)
OrientationInterpolator2526 = x3d.OrientationInterpolator()
OrientationInterpolator2526.DEF = "Roll_vc6_YawInterpolator"
OrientationInterpolator2526.key = [0,0.2,0.4,0.5,0.6,0.8,1]
OrientationInterpolator2526.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2499.children.append(OrientationInterpolator2526)
OrientationInterpolator2527 = x3d.OrientationInterpolator()
OrientationInterpolator2527.DEF = "Roll_l_thumb1_PitchInterpolator"
OrientationInterpolator2527.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2527.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2499.children.append(OrientationInterpolator2527)
OrientationInterpolator2528 = x3d.OrientationInterpolator()
OrientationInterpolator2528.DEF = "Roll_r_thumb1_PitchInterpolator"
OrientationInterpolator2528.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2528.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2499.children.append(OrientationInterpolator2528)
ROUTE2529 = x3d.ROUTE()
ROUTE2529.fromField = "fraction_changed"
ROUTE2529.fromNode = "RollTimer"
ROUTE2529.toField = "set_fraction"
ROUTE2529.toNode = "Rolls_r_ankle_RotationInterpolator"

Group2499.children.append(ROUTE2529)
ROUTE2530 = x3d.ROUTE()
ROUTE2530.fromField = "fraction_changed"
ROUTE2530.fromNode = "RollTimer"
ROUTE2530.toField = "set_fraction"
ROUTE2530.toNode = "Rolls_r_knee_RotationInterpolator"

Group2499.children.append(ROUTE2530)
ROUTE2531 = x3d.ROUTE()
ROUTE2531.fromField = "fraction_changed"
ROUTE2531.fromNode = "RollTimer"
ROUTE2531.toField = "set_fraction"
ROUTE2531.toNode = "Rolls_r_hip_RotationInterpolator"

Group2499.children.append(ROUTE2531)
ROUTE2532 = x3d.ROUTE()
ROUTE2532.fromField = "fraction_changed"
ROUTE2532.fromNode = "RollTimer"
ROUTE2532.toField = "set_fraction"
ROUTE2532.toNode = "Rolls_l_ankle_RotationInterpolator"

Group2499.children.append(ROUTE2532)
ROUTE2533 = x3d.ROUTE()
ROUTE2533.fromField = "fraction_changed"
ROUTE2533.fromNode = "RollTimer"
ROUTE2533.toField = "set_fraction"
ROUTE2533.toNode = "Rolls_l_knee_RotationInterpolator"

Group2499.children.append(ROUTE2533)
ROUTE2534 = x3d.ROUTE()
ROUTE2534.fromField = "fraction_changed"
ROUTE2534.fromNode = "RollTimer"
ROUTE2534.toField = "set_fraction"
ROUTE2534.toNode = "Rolls_l_hip_RotationInterpolator"

Group2499.children.append(ROUTE2534)
ROUTE2535 = x3d.ROUTE()
ROUTE2535.fromField = "fraction_changed"
ROUTE2535.fromNode = "RollTimer"
ROUTE2535.toField = "set_fraction"
ROUTE2535.toNode = "Rolls_lower_body_RotationInterpolator"

Group2499.children.append(ROUTE2535)
ROUTE2536 = x3d.ROUTE()
ROUTE2536.fromField = "fraction_changed"
ROUTE2536.fromNode = "RollTimer"
ROUTE2536.toField = "set_fraction"
ROUTE2536.toNode = "Rolls_r_wrist_RotationInterpolator"

Group2499.children.append(ROUTE2536)
ROUTE2537 = x3d.ROUTE()
ROUTE2537.fromField = "fraction_changed"
ROUTE2537.fromNode = "RollTimer"
ROUTE2537.toField = "set_fraction"
ROUTE2537.toNode = "Rolls_r_elbow_RotationInterpolator"

Group2499.children.append(ROUTE2537)
ROUTE2538 = x3d.ROUTE()
ROUTE2538.fromField = "fraction_changed"
ROUTE2538.fromNode = "RollTimer"
ROUTE2538.toField = "set_fraction"
ROUTE2538.toNode = "Rolls_r_shoulder_RotationInterpolator"

Group2499.children.append(ROUTE2538)
ROUTE2539 = x3d.ROUTE()
ROUTE2539.fromField = "fraction_changed"
ROUTE2539.fromNode = "RollTimer"
ROUTE2539.toField = "set_fraction"
ROUTE2539.toNode = "Rolls_l_wrist_RotationInterpolator"

Group2499.children.append(ROUTE2539)
ROUTE2540 = x3d.ROUTE()
ROUTE2540.fromField = "fraction_changed"
ROUTE2540.fromNode = "RollTimer"
ROUTE2540.toField = "set_fraction"
ROUTE2540.toNode = "Rolls_l_elbow_RotationInterpolator"

Group2499.children.append(ROUTE2540)
ROUTE2541 = x3d.ROUTE()
ROUTE2541.fromField = "fraction_changed"
ROUTE2541.fromNode = "RollTimer"
ROUTE2541.toField = "set_fraction"
ROUTE2541.toNode = "Rolls_l_shoulder_RotationInterpolator"

Group2499.children.append(ROUTE2541)
ROUTE2542 = x3d.ROUTE()
ROUTE2542.fromField = "fraction_changed"
ROUTE2542.fromNode = "RollTimer"
ROUTE2542.toField = "set_fraction"
ROUTE2542.toNode = "Rolls_head_RotationInterpolator"

Group2499.children.append(ROUTE2542)
ROUTE2543 = x3d.ROUTE()
ROUTE2543.fromField = "fraction_changed"
ROUTE2543.fromNode = "RollTimer"
ROUTE2543.toField = "set_fraction"
ROUTE2543.toNode = "Rolls_neck_RotationInterpolator"

Group2499.children.append(ROUTE2543)
ROUTE2544 = x3d.ROUTE()
ROUTE2544.fromField = "fraction_changed"
ROUTE2544.fromNode = "RollTimer"
ROUTE2544.toField = "set_fraction"
ROUTE2544.toNode = "Rolls_upper_body_RotationInterpolator"

Group2499.children.append(ROUTE2544)
ROUTE2545 = x3d.ROUTE()
ROUTE2545.fromField = "fraction_changed"
ROUTE2545.fromNode = "RollTimer"
ROUTE2545.toField = "set_fraction"
ROUTE2545.toNode = "Rolls_whole_body_RotationInterpolator"

Group2499.children.append(ROUTE2545)
ROUTE2546 = x3d.ROUTE()
ROUTE2546.fromField = "fraction_changed"
ROUTE2546.fromNode = "RollTimer"
ROUTE2546.toField = "set_fraction"
ROUTE2546.toNode = "Rolls_whole_body_TranslationInterpolator"

Group2499.children.append(ROUTE2546)
ROUTE2547 = x3d.ROUTE()
ROUTE2547.fromField = "fraction_changed"
ROUTE2547.fromNode = "RollTimer"
ROUTE2547.toField = "set_fraction"
ROUTE2547.toNode = "Roll_l_sternoclavicular_RollInterpolator"

Group2499.children.append(ROUTE2547)
ROUTE2548 = x3d.ROUTE()
ROUTE2548.fromField = "fraction_changed"
ROUTE2548.fromNode = "RollTimer"
ROUTE2548.toField = "set_fraction"
ROUTE2548.toNode = "Roll_l_acromioclavicular_RollInterpolator"

Group2499.children.append(ROUTE2548)
ROUTE2549 = x3d.ROUTE()
ROUTE2549.fromField = "fraction_changed"
ROUTE2549.fromNode = "RollTimer"
ROUTE2549.toField = "set_fraction"
ROUTE2549.toNode = "Roll_r_sternoclavicular_RollInterpolator"

Group2499.children.append(ROUTE2549)
ROUTE2550 = x3d.ROUTE()
ROUTE2550.fromField = "fraction_changed"
ROUTE2550.fromNode = "RollTimer"
ROUTE2550.toField = "set_fraction"
ROUTE2550.toNode = "Roll_r_acromioclavicular_RollInterpolator"

Group2499.children.append(ROUTE2550)
ROUTE2551 = x3d.ROUTE()
ROUTE2551.fromField = "fraction_changed"
ROUTE2551.fromNode = "RollTimer"
ROUTE2551.toField = "set_fraction"
ROUTE2551.toNode = "Roll_r_metatarsal_PitchInterpolator"

Group2499.children.append(ROUTE2551)
ROUTE2552 = x3d.ROUTE()
ROUTE2552.fromField = "fraction_changed"
ROUTE2552.fromNode = "RollTimer"
ROUTE2552.toField = "set_fraction"
ROUTE2552.toNode = "Roll_sacroiliac_YawInterpolator"

Group2499.children.append(ROUTE2552)
ROUTE2553 = x3d.ROUTE()
ROUTE2553.fromField = "fraction_changed"
ROUTE2553.fromNode = "RollTimer"
ROUTE2553.toField = "set_fraction"
ROUTE2553.toNode = "Roll_vl5_YawInterpolator"

Group2499.children.append(ROUTE2553)
ROUTE2554 = x3d.ROUTE()
ROUTE2554.fromField = "fraction_changed"
ROUTE2554.fromNode = "RollTimer"
ROUTE2554.toField = "set_fraction"
ROUTE2554.toNode = "Roll_vc6_YawInterpolator"

Group2499.children.append(ROUTE2554)
ROUTE2555 = x3d.ROUTE()
ROUTE2555.fromField = "fraction_changed"
ROUTE2555.fromNode = "RollTimer"
ROUTE2555.toField = "set_fraction"
ROUTE2555.toNode = "Roll_l_thumb1_PitchInterpolator"

Group2499.children.append(ROUTE2555)
ROUTE2556 = x3d.ROUTE()
ROUTE2556.fromField = "fraction_changed"
ROUTE2556.fromNode = "RollTimer"
ROUTE2556.toField = "set_fraction"
ROUTE2556.toNode = "Roll_r_thumb1_PitchInterpolator"

Group2499.children.append(ROUTE2556)
ROUTE2557 = x3d.ROUTE()
ROUTE2557.fromField = "value_changed"
ROUTE2557.fromNode = "Rolls_r_ankle_RotationInterpolator"
ROUTE2557.toField = "rotation"
ROUTE2557.toNode = "hanim_r_ankle"

Group2499.children.append(ROUTE2557)
ROUTE2558 = x3d.ROUTE()
ROUTE2558.fromField = "value_changed"
ROUTE2558.fromNode = "Rolls_r_knee_RotationInterpolator"
ROUTE2558.toField = "rotation"
ROUTE2558.toNode = "hanim_r_knee"

Group2499.children.append(ROUTE2558)
ROUTE2559 = x3d.ROUTE()
ROUTE2559.fromField = "value_changed"
ROUTE2559.fromNode = "Rolls_r_hip_RotationInterpolator"
ROUTE2559.toField = "rotation"
ROUTE2559.toNode = "hanim_r_hip"

Group2499.children.append(ROUTE2559)
ROUTE2560 = x3d.ROUTE()
ROUTE2560.fromField = "value_changed"
ROUTE2560.fromNode = "Rolls_l_ankle_RotationInterpolator"
ROUTE2560.toField = "rotation"
ROUTE2560.toNode = "hanim_l_ankle"

Group2499.children.append(ROUTE2560)
ROUTE2561 = x3d.ROUTE()
ROUTE2561.fromField = "value_changed"
ROUTE2561.fromNode = "Rolls_l_knee_RotationInterpolator"
ROUTE2561.toField = "rotation"
ROUTE2561.toNode = "hanim_l_knee"

Group2499.children.append(ROUTE2561)
ROUTE2562 = x3d.ROUTE()
ROUTE2562.fromField = "value_changed"
ROUTE2562.fromNode = "Rolls_l_hip_RotationInterpolator"
ROUTE2562.toField = "rotation"
ROUTE2562.toNode = "hanim_l_hip"

Group2499.children.append(ROUTE2562)
ROUTE2563 = x3d.ROUTE()
ROUTE2563.fromField = "value_changed"
ROUTE2563.fromNode = "Rolls_lower_body_RotationInterpolator"
ROUTE2563.toField = "rotation"
ROUTE2563.toNode = "hanim_sacroiliac"

Group2499.children.append(ROUTE2563)
ROUTE2564 = x3d.ROUTE()
ROUTE2564.fromField = "value_changed"
ROUTE2564.fromNode = "Rolls_r_wrist_RotationInterpolator"
ROUTE2564.toField = "rotation"
ROUTE2564.toNode = "hanim_r_wrist"

Group2499.children.append(ROUTE2564)
ROUTE2565 = x3d.ROUTE()
ROUTE2565.fromField = "value_changed"
ROUTE2565.fromNode = "Rolls_r_elbow_RotationInterpolator"
ROUTE2565.toField = "rotation"
ROUTE2565.toNode = "hanim_r_elbow"

Group2499.children.append(ROUTE2565)
ROUTE2566 = x3d.ROUTE()
ROUTE2566.fromField = "value_changed"
ROUTE2566.fromNode = "Rolls_r_shoulder_RotationInterpolator"
ROUTE2566.toField = "rotation"
ROUTE2566.toNode = "hanim_r_shoulder"

Group2499.children.append(ROUTE2566)
ROUTE2567 = x3d.ROUTE()
ROUTE2567.fromField = "value_changed"
ROUTE2567.fromNode = "Rolls_l_wrist_RotationInterpolator"
ROUTE2567.toField = "rotation"
ROUTE2567.toNode = "hanim_l_wrist"

Group2499.children.append(ROUTE2567)
ROUTE2568 = x3d.ROUTE()
ROUTE2568.fromField = "value_changed"
ROUTE2568.fromNode = "Rolls_l_elbow_RotationInterpolator"
ROUTE2568.toField = "rotation"
ROUTE2568.toNode = "hanim_l_elbow"

Group2499.children.append(ROUTE2568)
ROUTE2569 = x3d.ROUTE()
ROUTE2569.fromField = "value_changed"
ROUTE2569.fromNode = "Rolls_l_shoulder_RotationInterpolator"
ROUTE2569.toField = "rotation"
ROUTE2569.toNode = "hanim_l_shoulder"

Group2499.children.append(ROUTE2569)
ROUTE2570 = x3d.ROUTE()
ROUTE2570.fromField = "value_changed"
ROUTE2570.fromNode = "Rolls_head_RotationInterpolator"
ROUTE2570.toField = "rotation"
ROUTE2570.toNode = "hanim_skullbase"

Group2499.children.append(ROUTE2570)
ROUTE2571 = x3d.ROUTE()
ROUTE2571.fromField = "value_changed"
ROUTE2571.fromNode = "Rolls_neck_RotationInterpolator"
ROUTE2571.toField = "rotation"
ROUTE2571.toNode = "hanim_vc4"

Group2499.children.append(ROUTE2571)
ROUTE2572 = x3d.ROUTE()
ROUTE2572.fromField = "value_changed"
ROUTE2572.fromNode = "Rolls_upper_body_RotationInterpolator"
ROUTE2572.toField = "rotation"
ROUTE2572.toNode = "hanim_vl1"

Group2499.children.append(ROUTE2572)
ROUTE2573 = x3d.ROUTE()
ROUTE2573.fromField = "value_changed"
ROUTE2573.fromNode = "Rolls_whole_body_RotationInterpolator"
ROUTE2573.toField = "rotation"
ROUTE2573.toNode = "hanim_humanoid_root"

Group2499.children.append(ROUTE2573)
ROUTE2574 = x3d.ROUTE()
ROUTE2574.fromField = "value_changed"
ROUTE2574.fromNode = "Rolls_whole_body_TranslationInterpolator"
ROUTE2574.toField = "translation"
ROUTE2574.toNode = "hanim_humanoid_root"

Group2499.children.append(ROUTE2574)
ROUTE2575 = x3d.ROUTE()
ROUTE2575.fromField = "value_changed"
ROUTE2575.fromNode = "Roll_l_sternoclavicular_RollInterpolator"
ROUTE2575.toField = "rotation"
ROUTE2575.toNode = "hanim_l_sternoclavicular"

Group2499.children.append(ROUTE2575)
ROUTE2576 = x3d.ROUTE()
ROUTE2576.fromField = "value_changed"
ROUTE2576.fromNode = "Roll_l_acromioclavicular_RollInterpolator"
ROUTE2576.toField = "rotation"
ROUTE2576.toNode = "hanim_l_acromioclavicular"

Group2499.children.append(ROUTE2576)
ROUTE2577 = x3d.ROUTE()
ROUTE2577.fromField = "value_changed"
ROUTE2577.fromNode = "Roll_r_sternoclavicular_RollInterpolator"
ROUTE2577.toField = "rotation"
ROUTE2577.toNode = "hanim_r_sternoclavicular"

Group2499.children.append(ROUTE2577)
ROUTE2578 = x3d.ROUTE()
ROUTE2578.fromField = "value_changed"
ROUTE2578.fromNode = "Roll_r_acromioclavicular_RollInterpolator"
ROUTE2578.toField = "rotation"
ROUTE2578.toNode = "hanim_r_acromioclavicular"

Group2499.children.append(ROUTE2578)
ROUTE2579 = x3d.ROUTE()
ROUTE2579.fromField = "value_changed"
ROUTE2579.fromNode = "Roll_r_metatarsal_PitchInterpolator"
ROUTE2579.toField = "rotation"
ROUTE2579.toNode = "hanim_l_metatarsal"

Group2499.children.append(ROUTE2579)
ROUTE2580 = x3d.ROUTE()
ROUTE2580.fromField = "value_changed"
ROUTE2580.fromNode = "Roll_r_metatarsal_PitchInterpolator"
ROUTE2580.toField = "rotation"
ROUTE2580.toNode = "hanim_r_metatarsal"

Group2499.children.append(ROUTE2580)
ROUTE2581 = x3d.ROUTE()
ROUTE2581.fromField = "value_changed"
ROUTE2581.fromNode = "Roll_sacroiliac_YawInterpolator"
ROUTE2581.toField = "rotation"
ROUTE2581.toNode = "hanim_sacroiliac"

Group2499.children.append(ROUTE2581)
ROUTE2582 = x3d.ROUTE()
ROUTE2582.fromField = "value_changed"
ROUTE2582.fromNode = "Roll_vl5_YawInterpolator"
ROUTE2582.toField = "rotation"
ROUTE2582.toNode = "hanim_vl5"

Group2499.children.append(ROUTE2582)
ROUTE2583 = x3d.ROUTE()
ROUTE2583.fromField = "value_changed"
ROUTE2583.fromNode = "Roll_vc6_YawInterpolator"
ROUTE2583.toField = "rotation"
ROUTE2583.toNode = "hanim_vc6"

Group2499.children.append(ROUTE2583)
ROUTE2584 = x3d.ROUTE()
ROUTE2584.fromField = "value_changed"
ROUTE2584.fromNode = "Roll_l_thumb1_PitchInterpolator"
ROUTE2584.toField = "rotation"
ROUTE2584.toNode = "hanim_l_thumb1"

Group2499.children.append(ROUTE2584)
ROUTE2585 = x3d.ROUTE()
ROUTE2585.fromField = "value_changed"
ROUTE2585.fromNode = "Roll_r_thumb1_PitchInterpolator"
ROUTE2585.toField = "rotation"
ROUTE2585.toNode = "hanim_r_thumb1"

Group2499.children.append(ROUTE2585)

Scene30.children.append(Group2499)
Group2586 = x3d.Group()
Group2586.DEF = "WalkAnimation"
TimeSensor2587 = x3d.TimeSensor()
TimeSensor2587.DEF = "WalkTimer"
TimeSensor2587.cycleInterval = 1.73
TimeSensor2587.loop = True

Group2586.children.append(TimeSensor2587)
OrientationInterpolator2588 = x3d.OrientationInterpolator()
OrientationInterpolator2588.DEF = "Walk_r_metatarsal_PitchInterpolator"
OrientationInterpolator2588.key = [0,0.2,0.4,0.6,0.7,1]
OrientationInterpolator2588.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2586.children.append(OrientationInterpolator2588)
OrientationInterpolator2589 = x3d.OrientationInterpolator()
OrientationInterpolator2589.DEF = "Walk_r_ankle_RotationInterpolator"
OrientationInterpolator2589.key = [0,0.125,0.2083,0.375,0.4583,0.5,0.6667,0.75,0.7917,0.9167,1]
OrientationInterpolator2589.keyValue = (0.0000,0.0000,1.0000,0.0000,-1.0000,0.0000,0.0000,0.3533,-1.0000,0.0000,0.0000,0.1072,1.0000,0.0000,0.0000,0.2612,1.0000,0.0000,0.0000,0.1268,-1.0000,0.0000,0.0000,0.0179,-1.0000,0.0000,0.0000,0.0582,-1.0000,0.0000,0.0000,0.2398,-1.0000,0.0000,0.0000,0.3500,-1.0000,0.0000,0.0000,0.3322,0.0000,0.0000,1.0000,0.0000)

Group2586.children.append(OrientationInterpolator2589)
OrientationInterpolator2590 = x3d.OrientationInterpolator()
OrientationInterpolator2590.DEF = "Walk_r_knee_RotationInterpolator"
OrientationInterpolator2590.key = [0,0.125,0.2083,0.2917,0.375,0.5,0.6667,0.7917,0.9167,1]
OrientationInterpolator2590.keyValue = (1.0000,0.0000,0.0000,0.8573,1.0000,0.0000,0.0000,0.8926,1.0000,0.0000,0.0000,0.5351,1.0000,0.0000,0.0000,0.1756,1.0000,0.0000,0.0000,0.1194,1.0000,0.0000,0.0000,0.3153,1.0000,0.0000,0.0000,0.0935,1.0000,0.0000,0.0000,0.0856,1.0000,0.0000,0.0000,0.2475,1.0000,0.0000,0.0000,0.8573)

Group2586.children.append(OrientationInterpolator2590)
OrientationInterpolator2591 = x3d.OrientationInterpolator()
OrientationInterpolator2591.DEF = "Walk_r_hip_RotationInterpolator"
OrientationInterpolator2591.key = [0,0.125,0.2083,0.2917,0.375,0.5,0.6667,0.7917,0.9167,1]
OrientationInterpolator2591.keyValue = (-0.5831,0.0351,0.8116,0.1481,-0.9950,0.0230,0.0967,0.4683,-1.0000,0.0019,0.0080,0.4732,-0.9980,-0.0158,-0.0610,0.5079,-0.9911,-0.0354,-0.1286,0.5419,-0.9131,-0.0624,-0.4030,0.3361,-0.4306,-0.0796,-0.8990,0.0704,1.0000,0.0000,0.0000,0.2571,0.9891,-0.0280,0.1444,0.3879,-0.5831,0.0351,0.8116,0.1481)

Group2586.children.append(OrientationInterpolator2591)
OrientationInterpolator2592 = x3d.OrientationInterpolator()
OrientationInterpolator2592.DEF = "Walk_l_ankle_RotationInterpolator"
OrientationInterpolator2592.key = [0,0.125,0.2083,0.375,0.6667,0.9167,1]
OrientationInterpolator2592.keyValue = (-1.0000,0.0000,0.0000,0.0671,-1.0000,0.0000,0.0000,0.2152,-1.0000,0.0000,0.0000,0.3184,-1.0000,0.0000,0.0000,0.4717,-1.0000,0.0000,0.0000,0.2912,1.0000,0.0000,0.0000,0.1222,-1.0000,0.0000,0.0000,0.0671)

Group2586.children.append(OrientationInterpolator2592)
OrientationInterpolator2593 = x3d.OrientationInterpolator()
OrientationInterpolator2593.DEF = "Walk_l_knee_RotationInterpolator"
OrientationInterpolator2593.key = [0,0.2083,0.375,0.5,0.6667,0.7917,0.9167,1]
OrientationInterpolator2593.keyValue = (1.0000,0.0000,0.0000,0.3226,1.0000,0.0000,0.0000,0.1556,1.0000,0.0000,0.0000,0.0868,1.0000,0.0000,0.0000,0.8751,1.0000,0.0000,0.0000,1.1310,1.0000,0.0000,0.0000,0.0996,1.0000,0.0000,0.0000,0.3942,1.0000,0.0000,0.0000,0.3226)

Group2586.children.append(OrientationInterpolator2593)
OrientationInterpolator2594 = x3d.OrientationInterpolator()
OrientationInterpolator2594.DEF = "Walk_l_hip_RotationInterpolator"
OrientationInterpolator2594.key = [0,0.25,0.375,0.5,0.6667,0.7917,0.9167,1]
OrientationInterpolator2594.keyValue = (-0.8730,0.0609,0.4840,0.2865,0.9963,-0.0106,0.0848,0.2488,0.9965,0.0159,-0.0822,0.3836,-0.7018,-0.0322,-0.7117,0.1289,-1.0000,0.0000,0.0000,0.5518,-0.9964,0.0223,0.0817,0.5351,-0.9809,0.0491,0.1881,0.5204,-0.8730,0.0609,0.4840,0.2865)

Group2586.children.append(OrientationInterpolator2594)
OrientationInterpolator2595 = x3d.OrientationInterpolator()
OrientationInterpolator2595.DEF = "Walk_lower_body_RotationInterpolator"
OrientationInterpolator2595.key = [0,0.5,1]
OrientationInterpolator2595.keyValue = (0.0000,0.0000,-1.0000,0.1056,0.0000,0.0000,1.0000,0.0902,0.0000,0.0000,-1.0000,0.1056)

Group2586.children.append(OrientationInterpolator2595)
OrientationInterpolator2596 = x3d.OrientationInterpolator()
OrientationInterpolator2596.DEF = "Walk_r_wrist_RotationInterpolator"
OrientationInterpolator2596.key = [0,0.375,0.9167,1]
OrientationInterpolator2596.keyValue = (-0.8129,0.4759,-0.3357,0.1346,0.1533,-0.9878,0.0258,0.3902,-0.5701,0.7604,-0.3110,0.3660,-0.8129,0.4759,-0.3357,0.1346)

Group2586.children.append(OrientationInterpolator2596)
OrientationInterpolator2597 = x3d.OrientationInterpolator()
OrientationInterpolator2597.DEF = "Walk_r_elbow_RotationInterpolator"
OrientationInterpolator2597.key = [0,0.375,0.9167,1]
OrientationInterpolator2597.keyValue = (-1.0000,0.0000,0.0000,0.4115,-1.0000,0.0000,0.0000,0.0925,-1.0000,0.0000,0.0000,0.5726,-1.0000,0.0000,0.0000,0.4115)

Group2586.children.append(OrientationInterpolator2597)
OrientationInterpolator2598 = x3d.OrientationInterpolator()
OrientationInterpolator2598.DEF = "Walk_r_shoulder_RotationInterpolator"
OrientationInterpolator2598.key = [0,0.375,0.9167,1]
OrientationInterpolator2598.keyValue = (-1.0000,0.0000,0.0000,0.0935,1.0000,0.0000,0.0000,0.3197,-1.0000,0.0000,0.0000,0.1564,-1.0000,0.0000,0.0000,0.0935)

Group2586.children.append(OrientationInterpolator2598)
OrientationInterpolator2599 = x3d.OrientationInterpolator()
OrientationInterpolator2599.DEF = "Walk_l_wrist_RotationInterpolator"
OrientationInterpolator2599.key = [0,0.375,0.9167,1]
OrientationInterpolator2599.keyValue = (0.0000,-1.0000,0.0000,0.4611,-0.3302,-0.9275,0.1755,0.5389,0.0328,-0.9993,-0.0172,0.4920,0.0000,-1.0000,0.0000,0.4611)

Group2586.children.append(OrientationInterpolator2599)
OrientationInterpolator2600 = x3d.OrientationInterpolator()
OrientationInterpolator2600.DEF = "Walk_l_elbow_RotationInterpolator"
OrientationInterpolator2600.key = [0,0.375,0.9167,1]
OrientationInterpolator2600.keyValue = (-1.0000,0.0000,0.0000,0.0660,-1.0000,0.0000,0.0000,0.4884,-1.0000,0.0000,0.0000,0.0178,-1.0000,0.0000,0.0000,0.0660)

Group2586.children.append(OrientationInterpolator2600)
OrientationInterpolator2601 = x3d.OrientationInterpolator()
OrientationInterpolator2601.DEF = "Walk_l_shoulder_RotationInterpolator"
OrientationInterpolator2601.key = [0,0.375,0.9167,1]
OrientationInterpolator2601.keyValue = (1.0000,0.0000,0.0000,0.1189,-1.0000,0.0000,0.0000,0.1861,1.0000,0.0000,0.0000,0.3357,1.0000,0.0000,0.0000,0.1189)

Group2586.children.append(OrientationInterpolator2601)
OrientationInterpolator2602 = x3d.OrientationInterpolator()
OrientationInterpolator2602.DEF = "Walk_head_RotationInterpolator"
OrientationInterpolator2602.key = [0,0.375,0.4167,0.5,0.5833,0.6667,0.75,0.8333,0.9167,1]
OrientationInterpolator2602.keyValue = (0.0000,-1.0000,0.0000,0.0864,0.0000,1.0000,0.0000,0.1825,0.0000,1.0000,0.0000,0.1505,0.0000,1.0000,0.0000,0.1053,0.0000,1.0000,0.0000,0.0439,0.0000,-1.0000,0.0000,0.0312,0.0000,-1.0000,0.0000,0.0794,0.0000,-1.0000,0.0000,0.1616,0.0000,-1.0000,0.0000,0.1550,0.0000,-1.0000,0.0000,0.0864)

Group2586.children.append(OrientationInterpolator2602)
OrientationInterpolator2603 = x3d.OrientationInterpolator()
OrientationInterpolator2603.DEF = "Walk_neck_RotationInterpolator"
OrientationInterpolator2603.key = [0,1]
OrientationInterpolator2603.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2586.children.append(OrientationInterpolator2603)
OrientationInterpolator2604 = x3d.OrientationInterpolator()
OrientationInterpolator2604.DEF = "Walk_upper_body_RotationInterpolator"
OrientationInterpolator2604.key = [0,0.2083,0.375,0.75,0.8333,1]
OrientationInterpolator2604.keyValue = (0.0000,1.0000,0.0000,0.0826,-0.0197,-0.5974,0.8017,0.0823,0.0093,-0.9648,0.2627,0.1734,-0.0124,0.9549,-0.2968,0.0873,-0.0081,0.9691,-0.2463,0.1580,0.0000,1.0000,0.0000,0.0826)

Group2586.children.append(OrientationInterpolator2604)
OrientationInterpolator2605 = x3d.OrientationInterpolator()
OrientationInterpolator2605.DEF = "Walk_whole_body_RotationInterpolator"
OrientationInterpolator2605.key = [0,1]
OrientationInterpolator2605.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2586.children.append(OrientationInterpolator2605)
PositionInterpolator2606 = x3d.PositionInterpolator()
PositionInterpolator2606.DEF = "Walk_whole_body_TranslationInterpolator"
PositionInterpolator2606.key = [0,0.04167,0.125,0.1667,0.2083,0.25,0.2917,0.375,0.4583,0.5,0.5417,0.5833,0.625,0.7083,0.75,0.7917,0.875,0.9167,1]
PositionInterpolator2606.keyValue = (0.0000,-0.0093,0.0000,0.0000,-0.0039,0.0000,0.0000,-0.0088,0.0000,0.0000,-0.0149,0.0000,0.0000,-0.0264,0.0000,0.0000,-0.0393,0.0000,0.0000,-0.0502,0.0000,0.0000,-0.0747,0.0000,0.0000,-0.0273,0.0000,0.0000,-0.0161,0.0000,0.0000,-0.0113,0.0000,0.0000,-0.0058,0.0000,0.0000,-0.0020,0.0000,0.0000,-0.0026,0.0000,0.0000,-0.0143,0.0000,0.0000,-0.0380,0.0000,0.0000,-0.0565,0.0000,0.0000,-0.0450,0.0000,0.0000,-0.0093,0.0000)

Group2586.children.append(PositionInterpolator2606)
OrientationInterpolator2607 = x3d.OrientationInterpolator()
OrientationInterpolator2607.DEF = "Walk_l_sternoclavicular_RollInterpolator"
OrientationInterpolator2607.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2607.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2586.children.append(OrientationInterpolator2607)
OrientationInterpolator2608 = x3d.OrientationInterpolator()
OrientationInterpolator2608.DEF = "Walk_l_acromioclavicular_RollInterpolator"
OrientationInterpolator2608.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2608.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2586.children.append(OrientationInterpolator2608)
OrientationInterpolator2609 = x3d.OrientationInterpolator()
OrientationInterpolator2609.DEF = "Walk_r_sternoclavicular_RollInterpolator"
OrientationInterpolator2609.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2609.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2586.children.append(OrientationInterpolator2609)
OrientationInterpolator2610 = x3d.OrientationInterpolator()
OrientationInterpolator2610.DEF = "Walk_r_acromioclavicular_RollInterpolator"
OrientationInterpolator2610.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2610.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2586.children.append(OrientationInterpolator2610)
OrientationInterpolator2611 = x3d.OrientationInterpolator()
OrientationInterpolator2611.DEF = "Walk_sacroiliac_YawInterpolator"
OrientationInterpolator2611.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2611.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2586.children.append(OrientationInterpolator2611)
OrientationInterpolator2612 = x3d.OrientationInterpolator()
OrientationInterpolator2612.DEF = "Walk_vl5_YawInterpolator"
OrientationInterpolator2612.key = [0,0.2,0.4,0.5,0.6,0.8,1]
OrientationInterpolator2612.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2586.children.append(OrientationInterpolator2612)
OrientationInterpolator2613 = x3d.OrientationInterpolator()
OrientationInterpolator2613.DEF = "Walk_vc6_YawInterpolator"
OrientationInterpolator2613.key = [0,0.2,0.4,0.5,0.6,0.8,1]
OrientationInterpolator2613.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2586.children.append(OrientationInterpolator2613)
OrientationInterpolator2614 = x3d.OrientationInterpolator()
OrientationInterpolator2614.DEF = "Walk_l_thumb1_PitchInterpolator"
OrientationInterpolator2614.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2614.keyValue = (1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.2500,1.0000,0.0000,0.0000,0.5000,1.0000,0.0000,0.0000,0.7000,1.0000,0.0000,0.0000,0.2000,1.0000,0.0000,0.0000,0.0000)

Group2586.children.append(OrientationInterpolator2614)
OrientationInterpolator2615 = x3d.OrientationInterpolator()
OrientationInterpolator2615.DEF = "Walk_r_thumb1_PitchInterpolator"
OrientationInterpolator2615.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2615.keyValue = (1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.2500,1.0000,0.0000,0.0000,0.5000,1.0000,0.0000,0.0000,0.7000,1.0000,0.0000,0.0000,0.2000,1.0000,0.0000,0.0000,0.0000)

Group2586.children.append(OrientationInterpolator2615)
ROUTE2616 = x3d.ROUTE()
ROUTE2616.fromField = "fraction_changed"
ROUTE2616.fromNode = "WalkTimer"
ROUTE2616.toField = "set_fraction"
ROUTE2616.toNode = "Walk_r_ankle_RotationInterpolator"

Group2586.children.append(ROUTE2616)
ROUTE2617 = x3d.ROUTE()
ROUTE2617.fromField = "fraction_changed"
ROUTE2617.fromNode = "WalkTimer"
ROUTE2617.toField = "set_fraction"
ROUTE2617.toNode = "Walk_r_knee_RotationInterpolator"

Group2586.children.append(ROUTE2617)
ROUTE2618 = x3d.ROUTE()
ROUTE2618.fromField = "fraction_changed"
ROUTE2618.fromNode = "WalkTimer"
ROUTE2618.toField = "set_fraction"
ROUTE2618.toNode = "Walk_r_hip_RotationInterpolator"

Group2586.children.append(ROUTE2618)
ROUTE2619 = x3d.ROUTE()
ROUTE2619.fromField = "fraction_changed"
ROUTE2619.fromNode = "WalkTimer"
ROUTE2619.toField = "set_fraction"
ROUTE2619.toNode = "Walk_l_ankle_RotationInterpolator"

Group2586.children.append(ROUTE2619)
ROUTE2620 = x3d.ROUTE()
ROUTE2620.fromField = "fraction_changed"
ROUTE2620.fromNode = "WalkTimer"
ROUTE2620.toField = "set_fraction"
ROUTE2620.toNode = "Walk_l_knee_RotationInterpolator"

Group2586.children.append(ROUTE2620)
ROUTE2621 = x3d.ROUTE()
ROUTE2621.fromField = "fraction_changed"
ROUTE2621.fromNode = "WalkTimer"
ROUTE2621.toField = "set_fraction"
ROUTE2621.toNode = "Walk_l_hip_RotationInterpolator"

Group2586.children.append(ROUTE2621)
ROUTE2622 = x3d.ROUTE()
ROUTE2622.fromField = "fraction_changed"
ROUTE2622.fromNode = "WalkTimer"
ROUTE2622.toField = "set_fraction"
ROUTE2622.toNode = "Walk_lower_body_RotationInterpolator"

Group2586.children.append(ROUTE2622)
ROUTE2623 = x3d.ROUTE()
ROUTE2623.fromField = "fraction_changed"
ROUTE2623.fromNode = "WalkTimer"
ROUTE2623.toField = "set_fraction"
ROUTE2623.toNode = "Walk_r_wrist_RotationInterpolator"

Group2586.children.append(ROUTE2623)
ROUTE2624 = x3d.ROUTE()
ROUTE2624.fromField = "fraction_changed"
ROUTE2624.fromNode = "WalkTimer"
ROUTE2624.toField = "set_fraction"
ROUTE2624.toNode = "Walk_r_elbow_RotationInterpolator"

Group2586.children.append(ROUTE2624)
ROUTE2625 = x3d.ROUTE()
ROUTE2625.fromField = "fraction_changed"
ROUTE2625.fromNode = "WalkTimer"
ROUTE2625.toField = "set_fraction"
ROUTE2625.toNode = "Walk_r_shoulder_RotationInterpolator"

Group2586.children.append(ROUTE2625)
ROUTE2626 = x3d.ROUTE()
ROUTE2626.fromField = "fraction_changed"
ROUTE2626.fromNode = "WalkTimer"
ROUTE2626.toField = "set_fraction"
ROUTE2626.toNode = "Walk_l_wrist_RotationInterpolator"

Group2586.children.append(ROUTE2626)
ROUTE2627 = x3d.ROUTE()
ROUTE2627.fromField = "fraction_changed"
ROUTE2627.fromNode = "WalkTimer"
ROUTE2627.toField = "set_fraction"
ROUTE2627.toNode = "Walk_l_elbow_RotationInterpolator"

Group2586.children.append(ROUTE2627)
ROUTE2628 = x3d.ROUTE()
ROUTE2628.fromField = "fraction_changed"
ROUTE2628.fromNode = "WalkTimer"
ROUTE2628.toField = "set_fraction"
ROUTE2628.toNode = "Walk_l_shoulder_RotationInterpolator"

Group2586.children.append(ROUTE2628)
ROUTE2629 = x3d.ROUTE()
ROUTE2629.fromField = "fraction_changed"
ROUTE2629.fromNode = "WalkTimer"
ROUTE2629.toField = "set_fraction"
ROUTE2629.toNode = "Walk_head_RotationInterpolator"

Group2586.children.append(ROUTE2629)
ROUTE2630 = x3d.ROUTE()
ROUTE2630.fromField = "fraction_changed"
ROUTE2630.fromNode = "WalkTimer"
ROUTE2630.toField = "set_fraction"
ROUTE2630.toNode = "Walk_neck_RotationInterpolator"

Group2586.children.append(ROUTE2630)
ROUTE2631 = x3d.ROUTE()
ROUTE2631.fromField = "fraction_changed"
ROUTE2631.fromNode = "WalkTimer"
ROUTE2631.toField = "set_fraction"
ROUTE2631.toNode = "Walk_upper_body_RotationInterpolator"

Group2586.children.append(ROUTE2631)
ROUTE2632 = x3d.ROUTE()
ROUTE2632.fromField = "fraction_changed"
ROUTE2632.fromNode = "WalkTimer"
ROUTE2632.toField = "set_fraction"
ROUTE2632.toNode = "Walk_whole_body_RotationInterpolator"

Group2586.children.append(ROUTE2632)
ROUTE2633 = x3d.ROUTE()
ROUTE2633.fromField = "fraction_changed"
ROUTE2633.fromNode = "WalkTimer"
ROUTE2633.toField = "set_fraction"
ROUTE2633.toNode = "Walk_whole_body_TranslationInterpolator"

Group2586.children.append(ROUTE2633)
ROUTE2634 = x3d.ROUTE()
ROUTE2634.fromField = "fraction_changed"
ROUTE2634.fromNode = "WalkTimer"
ROUTE2634.toField = "set_fraction"
ROUTE2634.toNode = "Walk_l_sternoclavicular_RollInterpolator"

Group2586.children.append(ROUTE2634)
ROUTE2635 = x3d.ROUTE()
ROUTE2635.fromField = "fraction_changed"
ROUTE2635.fromNode = "WalkTimer"
ROUTE2635.toField = "set_fraction"
ROUTE2635.toNode = "Walk_l_acromioclavicular_RollInterpolator"

Group2586.children.append(ROUTE2635)
ROUTE2636 = x3d.ROUTE()
ROUTE2636.fromField = "fraction_changed"
ROUTE2636.fromNode = "WalkTimer"
ROUTE2636.toField = "set_fraction"
ROUTE2636.toNode = "Walk_r_sternoclavicular_RollInterpolator"

Group2586.children.append(ROUTE2636)
ROUTE2637 = x3d.ROUTE()
ROUTE2637.fromField = "fraction_changed"
ROUTE2637.fromNode = "WalkTimer"
ROUTE2637.toField = "set_fraction"
ROUTE2637.toNode = "Walk_r_acromioclavicular_RollInterpolator"

Group2586.children.append(ROUTE2637)
ROUTE2638 = x3d.ROUTE()
ROUTE2638.fromField = "fraction_changed"
ROUTE2638.fromNode = "WalkTimer"
ROUTE2638.toField = "set_fraction"
ROUTE2638.toNode = "Walk_r_metatarsal_PitchInterpolator"

Group2586.children.append(ROUTE2638)
ROUTE2639 = x3d.ROUTE()
ROUTE2639.fromField = "fraction_changed"
ROUTE2639.fromNode = "WalkTimer"
ROUTE2639.toField = "set_fraction"
ROUTE2639.toNode = "Walk_sacroiliac_YawInterpolator"

Group2586.children.append(ROUTE2639)
ROUTE2640 = x3d.ROUTE()
ROUTE2640.fromField = "fraction_changed"
ROUTE2640.fromNode = "WalkTimer"
ROUTE2640.toField = "set_fraction"
ROUTE2640.toNode = "Walk_vl5_YawInterpolator"

Group2586.children.append(ROUTE2640)
ROUTE2641 = x3d.ROUTE()
ROUTE2641.fromField = "fraction_changed"
ROUTE2641.fromNode = "WalkTimer"
ROUTE2641.toField = "set_fraction"
ROUTE2641.toNode = "Walk_vc6_YawInterpolator"

Group2586.children.append(ROUTE2641)
ROUTE2642 = x3d.ROUTE()
ROUTE2642.fromField = "fraction_changed"
ROUTE2642.fromNode = "WalkTimer"
ROUTE2642.toField = "set_fraction"
ROUTE2642.toNode = "Walk_l_thumb1_PitchInterpolator"

Group2586.children.append(ROUTE2642)
ROUTE2643 = x3d.ROUTE()
ROUTE2643.fromField = "fraction_changed"
ROUTE2643.fromNode = "WalkTimer"
ROUTE2643.toField = "set_fraction"
ROUTE2643.toNode = "Walk_r_thumb1_PitchInterpolator"

Group2586.children.append(ROUTE2643)
ROUTE2644 = x3d.ROUTE()
ROUTE2644.fromField = "value_changed"
ROUTE2644.fromNode = "Walk_r_ankle_RotationInterpolator"
ROUTE2644.toField = "rotation"
ROUTE2644.toNode = "hanim_r_ankle"

Group2586.children.append(ROUTE2644)
ROUTE2645 = x3d.ROUTE()
ROUTE2645.fromField = "value_changed"
ROUTE2645.fromNode = "Walk_r_knee_RotationInterpolator"
ROUTE2645.toField = "rotation"
ROUTE2645.toNode = "hanim_r_knee"

Group2586.children.append(ROUTE2645)
ROUTE2646 = x3d.ROUTE()
ROUTE2646.fromField = "value_changed"
ROUTE2646.fromNode = "Walk_r_hip_RotationInterpolator"
ROUTE2646.toField = "rotation"
ROUTE2646.toNode = "hanim_r_hip"

Group2586.children.append(ROUTE2646)
ROUTE2647 = x3d.ROUTE()
ROUTE2647.fromField = "value_changed"
ROUTE2647.fromNode = "Walk_l_ankle_RotationInterpolator"
ROUTE2647.toField = "rotation"
ROUTE2647.toNode = "hanim_l_ankle"

Group2586.children.append(ROUTE2647)
ROUTE2648 = x3d.ROUTE()
ROUTE2648.fromField = "value_changed"
ROUTE2648.fromNode = "Walk_l_knee_RotationInterpolator"
ROUTE2648.toField = "rotation"
ROUTE2648.toNode = "hanim_l_knee"

Group2586.children.append(ROUTE2648)
ROUTE2649 = x3d.ROUTE()
ROUTE2649.fromField = "value_changed"
ROUTE2649.fromNode = "Walk_l_hip_RotationInterpolator"
ROUTE2649.toField = "rotation"
ROUTE2649.toNode = "hanim_l_hip"

Group2586.children.append(ROUTE2649)
ROUTE2650 = x3d.ROUTE()
ROUTE2650.fromField = "value_changed"
ROUTE2650.fromNode = "Walk_lower_body_RotationInterpolator"
ROUTE2650.toField = "rotation"
ROUTE2650.toNode = "hanim_sacroiliac"

Group2586.children.append(ROUTE2650)
ROUTE2651 = x3d.ROUTE()
ROUTE2651.fromField = "value_changed"
ROUTE2651.fromNode = "Walk_r_wrist_RotationInterpolator"
ROUTE2651.toField = "rotation"
ROUTE2651.toNode = "hanim_r_wrist"

Group2586.children.append(ROUTE2651)
ROUTE2652 = x3d.ROUTE()
ROUTE2652.fromField = "value_changed"
ROUTE2652.fromNode = "Walk_r_elbow_RotationInterpolator"
ROUTE2652.toField = "rotation"
ROUTE2652.toNode = "hanim_r_elbow"

Group2586.children.append(ROUTE2652)
ROUTE2653 = x3d.ROUTE()
ROUTE2653.fromField = "value_changed"
ROUTE2653.fromNode = "Walk_r_shoulder_RotationInterpolator"
ROUTE2653.toField = "rotation"
ROUTE2653.toNode = "hanim_r_shoulder"

Group2586.children.append(ROUTE2653)
ROUTE2654 = x3d.ROUTE()
ROUTE2654.fromField = "value_changed"
ROUTE2654.fromNode = "Walk_l_wrist_RotationInterpolator"
ROUTE2654.toField = "rotation"
ROUTE2654.toNode = "hanim_l_wrist"

Group2586.children.append(ROUTE2654)
ROUTE2655 = x3d.ROUTE()
ROUTE2655.fromField = "value_changed"
ROUTE2655.fromNode = "Walk_l_elbow_RotationInterpolator"
ROUTE2655.toField = "rotation"
ROUTE2655.toNode = "hanim_l_elbow"

Group2586.children.append(ROUTE2655)
ROUTE2656 = x3d.ROUTE()
ROUTE2656.fromField = "value_changed"
ROUTE2656.fromNode = "Walk_l_shoulder_RotationInterpolator"
ROUTE2656.toField = "rotation"
ROUTE2656.toNode = "hanim_l_shoulder"

Group2586.children.append(ROUTE2656)
ROUTE2657 = x3d.ROUTE()
ROUTE2657.fromField = "value_changed"
ROUTE2657.fromNode = "Walk_head_RotationInterpolator"
ROUTE2657.toField = "rotation"
ROUTE2657.toNode = "hanim_skullbase"

Group2586.children.append(ROUTE2657)
ROUTE2658 = x3d.ROUTE()
ROUTE2658.fromField = "value_changed"
ROUTE2658.fromNode = "Walk_neck_RotationInterpolator"
ROUTE2658.toField = "rotation"
ROUTE2658.toNode = "hanim_vc4"

Group2586.children.append(ROUTE2658)
ROUTE2659 = x3d.ROUTE()
ROUTE2659.fromField = "value_changed"
ROUTE2659.fromNode = "Walk_upper_body_RotationInterpolator"
ROUTE2659.toField = "rotation"
ROUTE2659.toNode = "hanim_vl1"

Group2586.children.append(ROUTE2659)
ROUTE2660 = x3d.ROUTE()
ROUTE2660.fromField = "value_changed"
ROUTE2660.fromNode = "Walk_whole_body_RotationInterpolator"
ROUTE2660.toField = "rotation"
ROUTE2660.toNode = "hanim_humanoid_root"

Group2586.children.append(ROUTE2660)
ROUTE2661 = x3d.ROUTE()
ROUTE2661.fromField = "value_changed"
ROUTE2661.fromNode = "Walk_whole_body_TranslationInterpolator"
ROUTE2661.toField = "translation"
ROUTE2661.toNode = "hanim_humanoid_root"

Group2586.children.append(ROUTE2661)
ROUTE2662 = x3d.ROUTE()
ROUTE2662.fromField = "value_changed"
ROUTE2662.fromNode = "Walk_l_sternoclavicular_RollInterpolator"
ROUTE2662.toField = "rotation"
ROUTE2662.toNode = "hanim_l_sternoclavicular"

Group2586.children.append(ROUTE2662)
ROUTE2663 = x3d.ROUTE()
ROUTE2663.fromField = "value_changed"
ROUTE2663.fromNode = "Walk_l_acromioclavicular_RollInterpolator"
ROUTE2663.toField = "rotation"
ROUTE2663.toNode = "hanim_l_acromioclavicular"

Group2586.children.append(ROUTE2663)
ROUTE2664 = x3d.ROUTE()
ROUTE2664.fromField = "value_changed"
ROUTE2664.fromNode = "Walk_r_sternoclavicular_RollInterpolator"
ROUTE2664.toField = "rotation"
ROUTE2664.toNode = "hanim_r_sternoclavicular"

Group2586.children.append(ROUTE2664)
ROUTE2665 = x3d.ROUTE()
ROUTE2665.fromField = "value_changed"
ROUTE2665.fromNode = "Walk_r_acromioclavicular_RollInterpolator"
ROUTE2665.toField = "rotation"
ROUTE2665.toNode = "hanim_r_acromioclavicular"

Group2586.children.append(ROUTE2665)
ROUTE2666 = x3d.ROUTE()
ROUTE2666.fromField = "value_changed"
ROUTE2666.fromNode = "Walk_r_metatarsal_PitchInterpolator"
ROUTE2666.toField = "rotation"
ROUTE2666.toNode = "hanim_l_metatarsal"

Group2586.children.append(ROUTE2666)
ROUTE2667 = x3d.ROUTE()
ROUTE2667.fromField = "value_changed"
ROUTE2667.fromNode = "Walk_r_metatarsal_PitchInterpolator"
ROUTE2667.toField = "rotation"
ROUTE2667.toNode = "hanim_r_metatarsal"

Group2586.children.append(ROUTE2667)
ROUTE2668 = x3d.ROUTE()
ROUTE2668.fromField = "value_changed"
ROUTE2668.fromNode = "Walk_sacroiliac_YawInterpolator"
ROUTE2668.toField = "rotation"
ROUTE2668.toNode = "hanim_sacroiliac"

Group2586.children.append(ROUTE2668)
ROUTE2669 = x3d.ROUTE()
ROUTE2669.fromField = "value_changed"
ROUTE2669.fromNode = "Walk_vl5_YawInterpolator"
ROUTE2669.toField = "rotation"
ROUTE2669.toNode = "hanim_vl5"

Group2586.children.append(ROUTE2669)
ROUTE2670 = x3d.ROUTE()
ROUTE2670.fromField = "value_changed"
ROUTE2670.fromNode = "Walk_vc6_YawInterpolator"
ROUTE2670.toField = "rotation"
ROUTE2670.toNode = "hanim_vc6"

Group2586.children.append(ROUTE2670)
ROUTE2671 = x3d.ROUTE()
ROUTE2671.fromField = "value_changed"
ROUTE2671.fromNode = "Walk_l_thumb1_PitchInterpolator"
ROUTE2671.toField = "rotation"
ROUTE2671.toNode = "hanim_l_thumb1"

Group2586.children.append(ROUTE2671)
ROUTE2672 = x3d.ROUTE()
ROUTE2672.fromField = "value_changed"
ROUTE2672.fromNode = "Walk_r_thumb1_PitchInterpolator"
ROUTE2672.toField = "rotation"
ROUTE2672.toNode = "hanim_r_thumb1"

Group2586.children.append(ROUTE2672)

Scene30.children.append(Group2586)
Group2673 = x3d.Group()
Group2673.DEF = "RunAnimation"
TimeSensor2674 = x3d.TimeSensor()
TimeSensor2674.DEF = "RunTimer"
TimeSensor2674.cycleInterval = 0.9
TimeSensor2674.loop = True

Group2673.children.append(TimeSensor2674)
OrientationInterpolator2675 = x3d.OrientationInterpolator()
OrientationInterpolator2675.DEF = "Run_r_metatarsal_PitchInterpolator"
OrientationInterpolator2675.key = [0,0.2,0.4,0.6,0.7,1]
OrientationInterpolator2675.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2673.children.append(OrientationInterpolator2675)
OrientationInterpolator2676 = x3d.OrientationInterpolator()
OrientationInterpolator2676.DEF = "Run_l_hip_RotationInterpolator_Run"
OrientationInterpolator2676.key = [0,0.2182,0.4909,0.7455,1]
OrientationInterpolator2676.keyValue = (-0.9900,0.0330,0.0400,1.4200,-0.9900,0.1328,0.0670,0.4200,0.9900,0.0140,0.0090,0.9000,-0.9900,0.0703,0.0500,0.7000,-0.9900,0.0330,0.0400,1.4200)

Group2673.children.append(OrientationInterpolator2676)
OrientationInterpolator2677 = x3d.OrientationInterpolator()
OrientationInterpolator2677.DEF = "Run_l_knee_RotationInterpolator_Run"
OrientationInterpolator2677.key = [0,0.2182,0.4909,0.7455,1]
OrientationInterpolator2677.keyValue = (1.0000,0.0000,0.0000,1.0100,1.0000,0.0000,0.0000,0.4260,1.0000,0.0000,0.0000,0.7050,1.0000,0.0000,0.0000,2.1790,1.0000,0.0000,0.0000,1.0100)

Group2673.children.append(OrientationInterpolator2677)
OrientationInterpolator2678 = x3d.OrientationInterpolator()
OrientationInterpolator2678.DEF = "Run_l_ankle_RotationInterpolator_Run"
OrientationInterpolator2678.key = [0,0.22,0.3,0.4,1]
OrientationInterpolator2678.keyValue = (1.0000,0.0000,0.0000,0.0374,-1.0000,0.0000,0.0000,0.1037,-1.0000,0.0000,0.0000,0.4328,1.0000,0.0000,0.0000,0.1929,1.0000,0.0000,0.0000,0.0357)

Group2673.children.append(OrientationInterpolator2678)
OrientationInterpolator2679 = x3d.OrientationInterpolator()
OrientationInterpolator2679.DEF = "Run_r_hip_RotationInterpolator_Run"
OrientationInterpolator2679.key = [0,0.2545,0.4909,0.7091,1]
OrientationInterpolator2679.keyValue = (0.9900,-0.0140,0.0090,0.9000,-0.9900,-0.0703,-0.0500,0.7000,-0.9900,-0.0330,0.0400,1.4200,-0.9900,-0.1328,-0.0670,0.4200,0.9900,-0.0140,0.0090,0.9000)

Group2673.children.append(OrientationInterpolator2679)
OrientationInterpolator2680 = x3d.OrientationInterpolator()
OrientationInterpolator2680.DEF = "Run_r_knee_RotationInterpolator_Run"
OrientationInterpolator2680.key = [0,0.2545,0.4909,0.7091,1]
OrientationInterpolator2680.keyValue = (1.0000,0.0000,0.0000,0.7050,1.0000,0.0000,0.0000,2.1790,1.0000,0.0000,0.0000,1.0100,1.0000,0.0000,0.0000,0.4260,1.0000,0.0000,0.0000,0.7050)

Group2673.children.append(OrientationInterpolator2680)
OrientationInterpolator2681 = x3d.OrientationInterpolator()
OrientationInterpolator2681.DEF = "Run_r_ankle_RotationInterpolator_Run"
OrientationInterpolator2681.key = [0,0.4,0.71,0.8,0.82,1]
OrientationInterpolator2681.keyValue = (1.0000,0.0000,0.0000,0.2323,-1.0000,0.0000,0.0000,0.0784,-1.0000,0.0000,0.0000,0.3200,-1.0000,0.0000,0.0000,0.3740,-1.0000,0.0000,0.0000,0.3478,1.0000,0.0000,0.0000,0.2323)

Group2673.children.append(OrientationInterpolator2681)
OrientationInterpolator2682 = x3d.OrientationInterpolator()
OrientationInterpolator2682.DEF = "Run_l_shoulder_RotationInterpolator_Run"
OrientationInterpolator2682.key = [0,0.2182,0.4909,0.7455,1]
OrientationInterpolator2682.keyValue = (0.9900,-0.0740,0.2500,1.5000,0.9900,-0.0920,0.4400,0.3000,-0.9900,0.1360,0.2500,0.8500,0.9900,-0.0810,0.3800,0.4000,0.9900,-0.0740,0.2500,1.5000)

Group2673.children.append(OrientationInterpolator2682)
OrientationInterpolator2683 = x3d.OrientationInterpolator()
OrientationInterpolator2683.DEF = "Run_l_elbow_RotationInterpolator_Run"
OrientationInterpolator2683.key = [0,0.2182,0.4909,0.7455,1]
OrientationInterpolator2683.keyValue = (-1.0000,0.0000,0.0000,1.8500,-0.9900,-0.1900,0.1800,1.3500,-1.0000,0.0000,0.0000,0.9750,-0.9900,-0.0900,-0.0200,1.5500,-1.0000,0.0000,0.0000,1.8500)

Group2673.children.append(OrientationInterpolator2683)
OrientationInterpolator2684 = x3d.OrientationInterpolator()
OrientationInterpolator2684.DEF = "Run_l_wrist_RotationInterpolator_Run"
OrientationInterpolator2684.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator2684.keyValue = (-0.2500,-1.0000,0.0800,0.1400,0.2500,1.0000,0.0800,0.1400,0.0000,0.0000,1.0000,0.0000,-0.2500,1.0000,0.0800,-0.1400,-0.2500,1.0000,0.0800,0.1400)

Group2673.children.append(OrientationInterpolator2684)
OrientationInterpolator2685 = x3d.OrientationInterpolator()
OrientationInterpolator2685.DEF = "Run_r_shoulder_RotationInterpolator_Run"
OrientationInterpolator2685.key = [0,0.2545,0.4909,0.7091,1]
OrientationInterpolator2685.keyValue = (-0.9900,-0.1360,-0.2500,0.8500,0.9900,0.0810,-0.3800,0.4000,0.9900,0.0740,-0.2500,1.5000,0.9900,0.0810,-0.3800,0.4000,-0.9900,-0.1360,-0.2500,0.8500)

Group2673.children.append(OrientationInterpolator2685)
OrientationInterpolator2686 = x3d.OrientationInterpolator()
OrientationInterpolator2686.DEF = "Run_r_elbow_RotationInterpolator_Run"
OrientationInterpolator2686.key = [0,0.2545,0.4909,0.7091,1]
OrientationInterpolator2686.keyValue = (-1.0000,0.0000,0.0000,0.9750,-0.9900,0.0900,0.0200,1.5500,-1.0000,0.0000,0.0000,1.8500,-0.9900,0.1900,-0.1800,1.3500,-1.0000,0.0000,0.0000,0.9750)

Group2673.children.append(OrientationInterpolator2686)
OrientationInterpolator2687 = x3d.OrientationInterpolator()
OrientationInterpolator2687.DEF = "Run_r_wrist_RotationInterpolator_Run"
OrientationInterpolator2687.key = [0,1]
OrientationInterpolator2687.keyValue = (-0.9177,-0.2372,-0.3185,0.2143,-0.9177,-0.2372,-0.3185,0.2143)

Group2673.children.append(OrientationInterpolator2687)
OrientationInterpolator2688 = x3d.OrientationInterpolator()
OrientationInterpolator2688.DEF = "Run_lower_body_RotationInterpolator_Run"
OrientationInterpolator2688.key = [0,0.2182,0.4909,0.7455,1]
OrientationInterpolator2688.keyValue = (0.0000,-1.0000,0.0000,0.1250,0.0000,0.0000,1.0000,0.0000,0.0000,1.0000,0.0000,0.1250,0.0000,0.0000,1.0000,0.0000,0.0000,-1.0000,0.0000,0.1250)

Group2673.children.append(OrientationInterpolator2688)
OrientationInterpolator2689 = x3d.OrientationInterpolator()
OrientationInterpolator2689.DEF = "Run_head_RotationInterpolator_Run"
OrientationInterpolator2689.key = [0,0.2545,0.4909,0.7091,1]
OrientationInterpolator2689.keyValue = (1.0000,0.0000,0.0000,0.0800,1.0000,0.0000,0.0000,0.1200,1.0000,0.0000,0.0000,0.3000,1.0000,0.0000,0.0000,0.3000,1.0000,0.0000,0.0000,0.0800)

Group2673.children.append(OrientationInterpolator2689)
OrientationInterpolator2690 = x3d.OrientationInterpolator()
OrientationInterpolator2690.DEF = "Run_neck_RotationInterpolator_Run"
OrientationInterpolator2690.key = [0,0.2545,0.4909,0.7091,1]
OrientationInterpolator2690.keyValue = (0.7000,0.0000,0.0000,0.4000,-0.7000,-0.7000,0.0000,0.4000,0.0000,0.0000,0.0000,0.4000,-0.7000,0.7000,0.0000,0.4000,0.7000,0.0000,0.0000,0.4000)

Group2673.children.append(OrientationInterpolator2690)
OrientationInterpolator2691 = x3d.OrientationInterpolator()
OrientationInterpolator2691.DEF = "Run_upper_body_RotationInterpolator_Run"
OrientationInterpolator2691.key = [0,0.2545,0.4909,0.7636,1]
OrientationInterpolator2691.keyValue = (0.9700,0.6500,0.0860,0.5000,0.9000,0.0030,-0.0200,0.3800,0.9500,-0.6800,-0.0860,0.5000,0.9000,0.0040,-0.0250,0.4000,0.9700,0.6500,0.0860,0.5000)

Group2673.children.append(OrientationInterpolator2691)
OrientationInterpolator2692 = x3d.OrientationInterpolator()
OrientationInterpolator2692.DEF = "Run_whole_body_RotationInterpolator_Run"
OrientationInterpolator2692.key = [0,0.25,0.5,0.75,1]
OrientationInterpolator2692.keyValue = (1.0000,0.0000,0.0000,0.0600,1.0000,0.0000,0.0000,0.1670,1.0000,0.0000,0.0000,0.0600,1.0000,0.0000,0.0000,0.1680,1.0000,0.0000,0.0000,0.0600)

Group2673.children.append(OrientationInterpolator2692)
PositionInterpolator2693 = x3d.PositionInterpolator()
PositionInterpolator2693.DEF = "Run_whole_body_TranslationInterpolator_Run"
PositionInterpolator2693.key = [0,0.22,0.3,0.31,0.5,0.69,0.7,0.78,1]
PositionInterpolator2693.keyValue = (0.0000,-0.0100,0.0000,0.0000,-0.0370,0.0000,0.0000,-0.0490,0.0000,0.0000,-0.0370,0.0000,0.0000,-0.0100,0.0000,0.0000,-0.0370,0.0000,0.0000,-0.0490,0.0000,0.0000,-0.0370,0.0000,0.0000,-0.0100,0.0000)

Group2673.children.append(PositionInterpolator2693)
OrientationInterpolator2694 = x3d.OrientationInterpolator()
OrientationInterpolator2694.DEF = "Run_l_sternoclavicular_RollInterpolator"
OrientationInterpolator2694.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2694.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2673.children.append(OrientationInterpolator2694)
OrientationInterpolator2695 = x3d.OrientationInterpolator()
OrientationInterpolator2695.DEF = "Run_l_acromioclavicular_RollInterpolator"
OrientationInterpolator2695.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2695.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2673.children.append(OrientationInterpolator2695)
OrientationInterpolator2696 = x3d.OrientationInterpolator()
OrientationInterpolator2696.DEF = "Run_r_sternoclavicular_RollInterpolator"
OrientationInterpolator2696.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2696.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2673.children.append(OrientationInterpolator2696)
OrientationInterpolator2697 = x3d.OrientationInterpolator()
OrientationInterpolator2697.DEF = "Run_r_acromioclavicular_RollInterpolator"
OrientationInterpolator2697.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2697.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2673.children.append(OrientationInterpolator2697)
OrientationInterpolator2698 = x3d.OrientationInterpolator()
OrientationInterpolator2698.DEF = "Run_sacroiliac_YawInterpolator"
OrientationInterpolator2698.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2698.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2673.children.append(OrientationInterpolator2698)
OrientationInterpolator2699 = x3d.OrientationInterpolator()
OrientationInterpolator2699.DEF = "Run_vl5_YawInterpolator"
OrientationInterpolator2699.key = [0,0.2,0.4,0.5,0.6,0.8,1]
OrientationInterpolator2699.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2673.children.append(OrientationInterpolator2699)
OrientationInterpolator2700 = x3d.OrientationInterpolator()
OrientationInterpolator2700.DEF = "Run_vc6_YawInterpolator"
OrientationInterpolator2700.key = [0,0.2,0.4,0.5,0.6,0.8,1]
OrientationInterpolator2700.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2673.children.append(OrientationInterpolator2700)
OrientationInterpolator2701 = x3d.OrientationInterpolator()
OrientationInterpolator2701.DEF = "Run_l_thumb1_PitchInterpolator"
OrientationInterpolator2701.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2701.keyValue = (1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.2500,1.0000,0.0000,0.0000,0.7000,1.0000,0.0000,0.0000,0.2700,1.0000,0.0000,0.0000,0.2000,1.0000,0.0000,0.0000,0.0000)

Group2673.children.append(OrientationInterpolator2701)
OrientationInterpolator2702 = x3d.OrientationInterpolator()
OrientationInterpolator2702.DEF = "Run_r_thumb1_PitchInterpolator"
OrientationInterpolator2702.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2702.keyValue = (1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.2500,1.0000,0.0000,0.0000,0.7000,1.0000,0.0000,0.0000,0.2700,1.0000,0.0000,0.0000,0.2000,1.0000,0.0000,0.0000,0.0000)

Group2673.children.append(OrientationInterpolator2702)
ROUTE2703 = x3d.ROUTE()
ROUTE2703.fromField = "fraction_changed"
ROUTE2703.fromNode = "RunTimer"
ROUTE2703.toField = "set_fraction"
ROUTE2703.toNode = "Run_r_ankle_RotationInterpolator_Run"

Group2673.children.append(ROUTE2703)
ROUTE2704 = x3d.ROUTE()
ROUTE2704.fromField = "fraction_changed"
ROUTE2704.fromNode = "RunTimer"
ROUTE2704.toField = "set_fraction"
ROUTE2704.toNode = "Run_r_knee_RotationInterpolator_Run"

Group2673.children.append(ROUTE2704)
ROUTE2705 = x3d.ROUTE()
ROUTE2705.fromField = "fraction_changed"
ROUTE2705.fromNode = "RunTimer"
ROUTE2705.toField = "set_fraction"
ROUTE2705.toNode = "Run_r_hip_RotationInterpolator_Run"

Group2673.children.append(ROUTE2705)
ROUTE2706 = x3d.ROUTE()
ROUTE2706.fromField = "fraction_changed"
ROUTE2706.fromNode = "RunTimer"
ROUTE2706.toField = "set_fraction"
ROUTE2706.toNode = "Run_l_ankle_RotationInterpolator_Run"

Group2673.children.append(ROUTE2706)
ROUTE2707 = x3d.ROUTE()
ROUTE2707.fromField = "fraction_changed"
ROUTE2707.fromNode = "RunTimer"
ROUTE2707.toField = "set_fraction"
ROUTE2707.toNode = "Run_l_knee_RotationInterpolator_Run"

Group2673.children.append(ROUTE2707)
ROUTE2708 = x3d.ROUTE()
ROUTE2708.fromField = "fraction_changed"
ROUTE2708.fromNode = "RunTimer"
ROUTE2708.toField = "set_fraction"
ROUTE2708.toNode = "Run_l_hip_RotationInterpolator_Run"

Group2673.children.append(ROUTE2708)
ROUTE2709 = x3d.ROUTE()
ROUTE2709.fromField = "fraction_changed"
ROUTE2709.fromNode = "RunTimer"
ROUTE2709.toField = "set_fraction"
ROUTE2709.toNode = "Run_lower_body_RotationInterpolator_Run"

Group2673.children.append(ROUTE2709)
ROUTE2710 = x3d.ROUTE()
ROUTE2710.fromField = "fraction_changed"
ROUTE2710.fromNode = "RunTimer"
ROUTE2710.toField = "set_fraction"
ROUTE2710.toNode = "Run_r_wrist_RotationInterpolator_Run"

Group2673.children.append(ROUTE2710)
ROUTE2711 = x3d.ROUTE()
ROUTE2711.fromField = "fraction_changed"
ROUTE2711.fromNode = "RunTimer"
ROUTE2711.toField = "set_fraction"
ROUTE2711.toNode = "Run_r_elbow_RotationInterpolator_Run"

Group2673.children.append(ROUTE2711)
ROUTE2712 = x3d.ROUTE()
ROUTE2712.fromField = "fraction_changed"
ROUTE2712.fromNode = "RunTimer"
ROUTE2712.toField = "set_fraction"
ROUTE2712.toNode = "Run_r_shoulder_RotationInterpolator_Run"

Group2673.children.append(ROUTE2712)
ROUTE2713 = x3d.ROUTE()
ROUTE2713.fromField = "fraction_changed"
ROUTE2713.fromNode = "RunTimer"
ROUTE2713.toField = "set_fraction"
ROUTE2713.toNode = "Run_l_wrist_RotationInterpolator_Run"

Group2673.children.append(ROUTE2713)
ROUTE2714 = x3d.ROUTE()
ROUTE2714.fromField = "fraction_changed"
ROUTE2714.fromNode = "RunTimer"
ROUTE2714.toField = "set_fraction"
ROUTE2714.toNode = "Run_l_elbow_RotationInterpolator_Run"

Group2673.children.append(ROUTE2714)
ROUTE2715 = x3d.ROUTE()
ROUTE2715.fromField = "fraction_changed"
ROUTE2715.fromNode = "RunTimer"
ROUTE2715.toField = "set_fraction"
ROUTE2715.toNode = "Run_l_shoulder_RotationInterpolator_Run"

Group2673.children.append(ROUTE2715)
ROUTE2716 = x3d.ROUTE()
ROUTE2716.fromField = "fraction_changed"
ROUTE2716.fromNode = "RunTimer"
ROUTE2716.toField = "set_fraction"
ROUTE2716.toNode = "Run_head_RotationInterpolator_Run"

Group2673.children.append(ROUTE2716)
ROUTE2717 = x3d.ROUTE()
ROUTE2717.fromField = "fraction_changed"
ROUTE2717.fromNode = "RunTimer"
ROUTE2717.toField = "set_fraction"
ROUTE2717.toNode = "Run_neck_RotationInterpolator_Run"

Group2673.children.append(ROUTE2717)
ROUTE2718 = x3d.ROUTE()
ROUTE2718.fromField = "fraction_changed"
ROUTE2718.fromNode = "RunTimer"
ROUTE2718.toField = "set_fraction"
ROUTE2718.toNode = "Run_upper_body_RotationInterpolator_Run"

Group2673.children.append(ROUTE2718)
ROUTE2719 = x3d.ROUTE()
ROUTE2719.fromField = "fraction_changed"
ROUTE2719.fromNode = "RunTimer"
ROUTE2719.toField = "set_fraction"
ROUTE2719.toNode = "Run_whole_body_RotationInterpolator_Run"

Group2673.children.append(ROUTE2719)
ROUTE2720 = x3d.ROUTE()
ROUTE2720.fromField = "fraction_changed"
ROUTE2720.fromNode = "RunTimer"
ROUTE2720.toField = "set_fraction"
ROUTE2720.toNode = "Run_whole_body_TranslationInterpolator_Run"

Group2673.children.append(ROUTE2720)
ROUTE2721 = x3d.ROUTE()
ROUTE2721.fromField = "fraction_changed"
ROUTE2721.fromNode = "RunTimer"
ROUTE2721.toField = "set_fraction"
ROUTE2721.toNode = "Run_l_sternoclavicular_RollInterpolator"

Group2673.children.append(ROUTE2721)
ROUTE2722 = x3d.ROUTE()
ROUTE2722.fromField = "fraction_changed"
ROUTE2722.fromNode = "RunTimer"
ROUTE2722.toField = "set_fraction"
ROUTE2722.toNode = "Run_l_acromioclavicular_RollInterpolator"

Group2673.children.append(ROUTE2722)
ROUTE2723 = x3d.ROUTE()
ROUTE2723.fromField = "fraction_changed"
ROUTE2723.fromNode = "RunTimer"
ROUTE2723.toField = "set_fraction"
ROUTE2723.toNode = "Run_r_sternoclavicular_RollInterpolator"

Group2673.children.append(ROUTE2723)
ROUTE2724 = x3d.ROUTE()
ROUTE2724.fromField = "fraction_changed"
ROUTE2724.fromNode = "RunTimer"
ROUTE2724.toField = "set_fraction"
ROUTE2724.toNode = "Run_r_acromioclavicular_RollInterpolator"

Group2673.children.append(ROUTE2724)
ROUTE2725 = x3d.ROUTE()
ROUTE2725.fromField = "fraction_changed"
ROUTE2725.fromNode = "RunTimer"
ROUTE2725.toField = "set_fraction"
ROUTE2725.toNode = "Run_r_metatarsal_PitchInterpolator"

Group2673.children.append(ROUTE2725)
ROUTE2726 = x3d.ROUTE()
ROUTE2726.fromField = "fraction_changed"
ROUTE2726.fromNode = "RunTimer"
ROUTE2726.toField = "set_fraction"
ROUTE2726.toNode = "Run_sacroiliac_YawInterpolator"

Group2673.children.append(ROUTE2726)
ROUTE2727 = x3d.ROUTE()
ROUTE2727.fromField = "fraction_changed"
ROUTE2727.fromNode = "RunTimer"
ROUTE2727.toField = "set_fraction"
ROUTE2727.toNode = "Run_vl5_YawInterpolator"

Group2673.children.append(ROUTE2727)
ROUTE2728 = x3d.ROUTE()
ROUTE2728.fromField = "fraction_changed"
ROUTE2728.fromNode = "RunTimer"
ROUTE2728.toField = "set_fraction"
ROUTE2728.toNode = "Run_vc6_YawInterpolator"

Group2673.children.append(ROUTE2728)
ROUTE2729 = x3d.ROUTE()
ROUTE2729.fromField = "fraction_changed"
ROUTE2729.fromNode = "RunTimer"
ROUTE2729.toField = "set_fraction"
ROUTE2729.toNode = "Run_l_thumb1_PitchInterpolator"

Group2673.children.append(ROUTE2729)
ROUTE2730 = x3d.ROUTE()
ROUTE2730.fromField = "fraction_changed"
ROUTE2730.fromNode = "RunTimer"
ROUTE2730.toField = "set_fraction"
ROUTE2730.toNode = "Run_r_thumb1_PitchInterpolator"

Group2673.children.append(ROUTE2730)
ROUTE2731 = x3d.ROUTE()
ROUTE2731.fromField = "value_changed"
ROUTE2731.fromNode = "Run_r_ankle_RotationInterpolator_Run"
ROUTE2731.toField = "rotation"
ROUTE2731.toNode = "hanim_r_ankle"

Group2673.children.append(ROUTE2731)
ROUTE2732 = x3d.ROUTE()
ROUTE2732.fromField = "value_changed"
ROUTE2732.fromNode = "Run_r_knee_RotationInterpolator_Run"
ROUTE2732.toField = "rotation"
ROUTE2732.toNode = "hanim_r_knee"

Group2673.children.append(ROUTE2732)
ROUTE2733 = x3d.ROUTE()
ROUTE2733.fromField = "value_changed"
ROUTE2733.fromNode = "Run_r_hip_RotationInterpolator_Run"
ROUTE2733.toField = "rotation"
ROUTE2733.toNode = "hanim_r_hip"

Group2673.children.append(ROUTE2733)
ROUTE2734 = x3d.ROUTE()
ROUTE2734.fromField = "value_changed"
ROUTE2734.fromNode = "Run_l_ankle_RotationInterpolator_Run"
ROUTE2734.toField = "rotation"
ROUTE2734.toNode = "hanim_l_ankle"

Group2673.children.append(ROUTE2734)
ROUTE2735 = x3d.ROUTE()
ROUTE2735.fromField = "value_changed"
ROUTE2735.fromNode = "Run_l_knee_RotationInterpolator_Run"
ROUTE2735.toField = "rotation"
ROUTE2735.toNode = "hanim_l_knee"

Group2673.children.append(ROUTE2735)
ROUTE2736 = x3d.ROUTE()
ROUTE2736.fromField = "value_changed"
ROUTE2736.fromNode = "Run_l_hip_RotationInterpolator_Run"
ROUTE2736.toField = "rotation"
ROUTE2736.toNode = "hanim_l_hip"

Group2673.children.append(ROUTE2736)
ROUTE2737 = x3d.ROUTE()
ROUTE2737.fromField = "value_changed"
ROUTE2737.fromNode = "Run_r_wrist_RotationInterpolator_Run"
ROUTE2737.toField = "rotation"
ROUTE2737.toNode = "hanim_r_wrist"

Group2673.children.append(ROUTE2737)
ROUTE2738 = x3d.ROUTE()
ROUTE2738.fromField = "value_changed"
ROUTE2738.fromNode = "Run_r_elbow_RotationInterpolator_Run"
ROUTE2738.toField = "rotation"
ROUTE2738.toNode = "hanim_r_elbow"

Group2673.children.append(ROUTE2738)
ROUTE2739 = x3d.ROUTE()
ROUTE2739.fromField = "value_changed"
ROUTE2739.fromNode = "Run_r_shoulder_RotationInterpolator_Run"
ROUTE2739.toField = "rotation"
ROUTE2739.toNode = "hanim_r_shoulder"

Group2673.children.append(ROUTE2739)
ROUTE2740 = x3d.ROUTE()
ROUTE2740.fromField = "value_changed"
ROUTE2740.fromNode = "Run_l_wrist_RotationInterpolator_Run"
ROUTE2740.toField = "rotation"
ROUTE2740.toNode = "hanim_l_wrist"

Group2673.children.append(ROUTE2740)
ROUTE2741 = x3d.ROUTE()
ROUTE2741.fromField = "value_changed"
ROUTE2741.fromNode = "Run_l_elbow_RotationInterpolator_Run"
ROUTE2741.toField = "rotation"
ROUTE2741.toNode = "hanim_l_elbow"

Group2673.children.append(ROUTE2741)
ROUTE2742 = x3d.ROUTE()
ROUTE2742.fromField = "value_changed"
ROUTE2742.fromNode = "Run_l_shoulder_RotationInterpolator_Run"
ROUTE2742.toField = "rotation"
ROUTE2742.toNode = "hanim_l_shoulder"

Group2673.children.append(ROUTE2742)
ROUTE2743 = x3d.ROUTE()
ROUTE2743.fromField = "value_changed"
ROUTE2743.fromNode = "Run_lower_body_RotationInterpolator_Run"
ROUTE2743.toField = "rotation"
ROUTE2743.toNode = "hanim_sacroiliac"

Group2673.children.append(ROUTE2743)
ROUTE2744 = x3d.ROUTE()
ROUTE2744.fromField = "value_changed"
ROUTE2744.fromNode = "Run_head_RotationInterpolator_Run"
ROUTE2744.toField = "rotation"
ROUTE2744.toNode = "hanim_skullbase"

Group2673.children.append(ROUTE2744)
ROUTE2745 = x3d.ROUTE()
ROUTE2745.fromField = "value_changed"
ROUTE2745.fromNode = "Run_neck_RotationInterpolator_Run"
ROUTE2745.toField = "rotation"
ROUTE2745.toNode = "hanim_vc4"

Group2673.children.append(ROUTE2745)
ROUTE2746 = x3d.ROUTE()
ROUTE2746.fromField = "value_changed"
ROUTE2746.fromNode = "Run_upper_body_RotationInterpolator_Run"
ROUTE2746.toField = "rotation"
ROUTE2746.toNode = "hanim_vl1"

Group2673.children.append(ROUTE2746)
ROUTE2747 = x3d.ROUTE()
ROUTE2747.fromField = "value_changed"
ROUTE2747.fromNode = "Run_whole_body_RotationInterpolator_Run"
ROUTE2747.toField = "rotation"
ROUTE2747.toNode = "hanim_humanoid_root"

Group2673.children.append(ROUTE2747)
ROUTE2748 = x3d.ROUTE()
ROUTE2748.fromField = "value_changed"
ROUTE2748.fromNode = "Run_whole_body_TranslationInterpolator_Run"
ROUTE2748.toField = "translation"
ROUTE2748.toNode = "hanim_humanoid_root"

Group2673.children.append(ROUTE2748)
ROUTE2749 = x3d.ROUTE()
ROUTE2749.fromField = "value_changed"
ROUTE2749.fromNode = "Run_l_sternoclavicular_RollInterpolator"
ROUTE2749.toField = "rotation"
ROUTE2749.toNode = "hanim_l_sternoclavicular"

Group2673.children.append(ROUTE2749)
ROUTE2750 = x3d.ROUTE()
ROUTE2750.fromField = "value_changed"
ROUTE2750.fromNode = "Run_l_acromioclavicular_RollInterpolator"
ROUTE2750.toField = "rotation"
ROUTE2750.toNode = "hanim_l_acromioclavicular"

Group2673.children.append(ROUTE2750)
ROUTE2751 = x3d.ROUTE()
ROUTE2751.fromField = "value_changed"
ROUTE2751.fromNode = "Run_r_sternoclavicular_RollInterpolator"
ROUTE2751.toField = "rotation"
ROUTE2751.toNode = "hanim_r_sternoclavicular"

Group2673.children.append(ROUTE2751)
ROUTE2752 = x3d.ROUTE()
ROUTE2752.fromField = "value_changed"
ROUTE2752.fromNode = "Run_r_acromioclavicular_RollInterpolator"
ROUTE2752.toField = "rotation"
ROUTE2752.toNode = "hanim_r_acromioclavicular"

Group2673.children.append(ROUTE2752)
ROUTE2753 = x3d.ROUTE()
ROUTE2753.fromField = "value_changed"
ROUTE2753.fromNode = "Run_r_metatarsal_PitchInterpolator"
ROUTE2753.toField = "rotation"
ROUTE2753.toNode = "hanim_l_metatarsal"

Group2673.children.append(ROUTE2753)
ROUTE2754 = x3d.ROUTE()
ROUTE2754.fromField = "value_changed"
ROUTE2754.fromNode = "Run_r_metatarsal_PitchInterpolator"
ROUTE2754.toField = "rotation"
ROUTE2754.toNode = "hanim_r_metatarsal"

Group2673.children.append(ROUTE2754)
ROUTE2755 = x3d.ROUTE()
ROUTE2755.fromField = "value_changed"
ROUTE2755.fromNode = "Run_sacroiliac_YawInterpolator"
ROUTE2755.toField = "rotation"
ROUTE2755.toNode = "hanim_sacroiliac"

Group2673.children.append(ROUTE2755)
ROUTE2756 = x3d.ROUTE()
ROUTE2756.fromField = "value_changed"
ROUTE2756.fromNode = "Run_vl5_YawInterpolator"
ROUTE2756.toField = "rotation"
ROUTE2756.toNode = "hanim_vl5"

Group2673.children.append(ROUTE2756)
ROUTE2757 = x3d.ROUTE()
ROUTE2757.fromField = "value_changed"
ROUTE2757.fromNode = "Run_vc6_YawInterpolator"
ROUTE2757.toField = "rotation"
ROUTE2757.toNode = "hanim_vc6"

Group2673.children.append(ROUTE2757)
ROUTE2758 = x3d.ROUTE()
ROUTE2758.fromField = "value_changed"
ROUTE2758.fromNode = "Run_l_thumb1_PitchInterpolator"
ROUTE2758.toField = "rotation"
ROUTE2758.toNode = "hanim_l_thumb1"

Group2673.children.append(ROUTE2758)
ROUTE2759 = x3d.ROUTE()
ROUTE2759.fromField = "value_changed"
ROUTE2759.fromNode = "Run_r_thumb1_PitchInterpolator"
ROUTE2759.toField = "rotation"
ROUTE2759.toNode = "hanim_r_thumb1"

Group2673.children.append(ROUTE2759)

Scene30.children.append(Group2673)
Group2760 = x3d.Group()
Group2760.DEF = "JumpAnimation"
TimeSensor2761 = x3d.TimeSensor()
TimeSensor2761.DEF = "JumpTimer"
TimeSensor2761.cycleInterval = 3.73
TimeSensor2761.loop = True

Group2760.children.append(TimeSensor2761)
OrientationInterpolator2762 = x3d.OrientationInterpolator()
OrientationInterpolator2762.DEF = "Jump_r_metatarsal_PitchInterpolator"
OrientationInterpolator2762.key = [0,0.2,0.4,0.6,0.7,1]
OrientationInterpolator2762.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2760.children.append(OrientationInterpolator2762)
OrientationInterpolator2763 = x3d.OrientationInterpolator()
OrientationInterpolator2763.DEF = "Jump_r_ankle_RotationInterpolator"
OrientationInterpolator2763.key = [0,0.1,0.15,0.25,0.28,0.32,0.35,0.64,0.76,0.84,0.88,0.92,0.96,1]
OrientationInterpolator2763.keyValue = (0.0000,0.0000,1.0000,0.0000,-1.0000,0.0000,0.0000,0.6735,-1.0000,0.0000,0.0000,0.6735,-1.0000,0.0000,0.0000,0.3527,-1.0000,0.0000,0.0000,0.3038,-1.0000,0.0000,0.0000,0.0796,1.0000,0.0000,0.0000,1.3000,1.0000,0.0000,0.0000,0.6509,1.0000,0.0000,0.0000,0.3001,-1.0000,0.0000,0.0000,0.2087,-1.0000,0.0000,0.0000,0.3756,-1.0000,0.0000,0.0000,0.3279,-1.0000,0.0000,0.0000,0.1193,0.0000,0.0000,1.0000,0.0000)

Group2760.children.append(OrientationInterpolator2763)
OrientationInterpolator2764 = x3d.OrientationInterpolator()
OrientationInterpolator2764.DEF = "Jump_r_knee_RotationInterpolator"
OrientationInterpolator2764.key = [0,0.2,0.25,0.3,0.64,0.76,0.88,1]
OrientationInterpolator2764.keyValue = (0.0000,0.0000,1.0000,0.0000,1.0000,0.0000,0.0000,2.5000,1.0000,0.0000,0.0000,1.7000,0.0000,0.0000,1.0000,0.0000,1.0000,0.0000,0.0000,0.9507,1.0000,0.0000,0.0000,0.5845,1.0000,0.0000,0.0000,0.9054,0.0000,0.0000,1.0000,0.0000)

Group2760.children.append(OrientationInterpolator2764)
OrientationInterpolator2765 = x3d.OrientationInterpolator()
OrientationInterpolator2765.DEF = "Jump_r_hip_RotationInterpolator"
OrientationInterpolator2765.key = [0,0.18,0.24,0.26,0.28,0.32,0.48,0.64,0.76,0.88,1]
OrientationInterpolator2765.keyValue = (0.0000,0.0000,1.0000,0.0000,-1.0000,0.0000,0.0000,1.6300,-1.0000,0.0000,0.0000,1.7000,-1.0000,0.0000,0.0000,1.5500,-1.0000,0.0000,0.0000,0.8943,-1.0000,0.0000,0.0000,0.3698,0.0000,0.0000,1.0000,0.0000,-1.0000,0.0000,0.0000,0.4963,-1.0000,0.0000,0.0000,0.3829,-1.0000,0.0000,0.0000,0.5169,0.0000,0.0000,1.0000,0.0000)

Group2760.children.append(OrientationInterpolator2765)
OrientationInterpolator2766 = x3d.OrientationInterpolator()
OrientationInterpolator2766.DEF = "Jump_l_ankle_RotationInterpolator"
OrientationInterpolator2766.key = [0,0.28,0.32,0.36,0.4,0.44,0.48,0.64,0.76,0.84,0.88,0.92,0.96,1]
OrientationInterpolator2766.keyValue = (0.0000,0.0000,1.0000,0.0000,-1.0000,0.0000,0.0000,0.6250,-1.0000,0.0000,0.0000,0.6250,-1.0000,0.0000,0.0000,0.3364,-1.0000,0.0000,0.0000,0.2742,-1.0000,0.0000,0.0000,0.0508,1.0000,0.0000,0.0000,0.2833,1.0000,0.0000,0.0000,0.6667,1.0000,0.0000,0.0000,0.2833,-1.0000,0.0000,0.0000,0.2108,-1.0000,0.0000,0.0000,0.3750,-1.0000,0.0000,0.0000,0.3146,-1.0000,0.0000,0.0000,0.1174,0.0000,0.0000,1.0000,0.0000)

Group2760.children.append(OrientationInterpolator2766)
OrientationInterpolator2767 = x3d.OrientationInterpolator()
OrientationInterpolator2767.DEF = "Jump_l_knee_RotationInterpolator"
OrientationInterpolator2767.key = [0,0.28,0.32,0.48,0.64,0.76,0.88,1]
OrientationInterpolator2767.keyValue = (0.0000,0.0000,1.0000,0.0000,1.0000,0.0000,0.0000,2.0470,1.0000,0.0000,0.0000,2.0470,0.0000,0.0000,1.0000,0.0000,1.0000,0.0000,0.0000,1.5660,1.0000,0.0000,0.0000,0.5913,1.0000,0.0000,0.0000,0.9235,0.0000,0.0000,1.0000,0.0000)

Group2760.children.append(OrientationInterpolator2767)
OrientationInterpolator2768 = x3d.OrientationInterpolator()
OrientationInterpolator2768.DEF = "Jump_l_hip_RotationInterpolator"
OrientationInterpolator2768.key = [0,0.28,0.32,0.36,0.4,0.44,0.48,0.64,0.76,0.88,1]
OrientationInterpolator2768.keyValue = (0.0000,0.0000,1.0000,0.0000,1.0000,0.0000,0.0000,4.3490,1.0000,0.0000,0.0000,4.3490,1.0000,0.0000,0.0000,4.6150,-1.0000,0.0000,0.0000,0.9136,-1.0000,0.0000,0.0000,0.3614,0.0000,0.0000,1.0000,0.0000,-1.0000,0.0000,0.0000,0.7869,-1.0000,0.0000,0.0000,0.3918,-1.0000,0.0000,0.0000,0.5433,0.0000,0.0000,1.0000,0.0000)

Group2760.children.append(OrientationInterpolator2768)
OrientationInterpolator2769 = x3d.OrientationInterpolator()
OrientationInterpolator2769.DEF = "Jump_lower_body_RotationInterpolator"
OrientationInterpolator2769.key = [0,0.28,0.32,0.48,0.76,1]
OrientationInterpolator2769.keyValue = (0.0000,0.0000,1.0000,0.0000,1.0000,0.0000,0.0000,0.1892,1.0000,0.0000,0.0000,0.1892,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2760.children.append(OrientationInterpolator2769)
OrientationInterpolator2770 = x3d.OrientationInterpolator()
OrientationInterpolator2770.DEF = "Jump_r_wrist_RotationInterpolator"
OrientationInterpolator2770.key = [0,0.28,0.32,0.64,0.76,1]
OrientationInterpolator2770.keyValue = (0.0000,0.0000,1.0000,0.0000,-0.0585,0.9839,-0.1688,1.8596,-0.0585,0.9839,-0.1688,1.8596,-0.0022,0.9980,-0.0630,1.4607,0.0000,1.0000,0.0000,0.4973,0.0000,0.0000,1.0000,0.0000)

Group2760.children.append(OrientationInterpolator2770)
OrientationInterpolator2771 = x3d.OrientationInterpolator()
OrientationInterpolator2771.DEF = "Jump_r_elbow_RotationInterpolator"
OrientationInterpolator2771.key = [0,0.28,0.32,0.64,0.76,1]
OrientationInterpolator2771.keyValue = (0.0000,0.0000,1.0000,0.0000,-1.0000,0.0000,0.0000,0.0415,-1.0000,0.0000,0.0000,0.0415,-1.0000,0.0000,0.0000,0.5855,-1.0000,0.0000,0.0000,0.5852,0.0000,0.0000,1.0000,0.0000)

Group2760.children.append(OrientationInterpolator2771)
OrientationInterpolator2772 = x3d.OrientationInterpolator()
OrientationInterpolator2772.DEF = "Jump_r_shoulder_RotationInterpolator"
OrientationInterpolator2772.key = [0,0.28,0.32,0.64,0.76,0.88,1]
OrientationInterpolator2772.keyValue = (0.0000,0.0000,1.0000,0.0000,0.9992,0.0204,0.0356,4.6880,0.9992,0.0204,0.0356,4.6880,0.9989,-0.0462,0.0052,4.0790,-0.8687,-0.2525,-0.4261,1.5010,-0.9410,-0.2893,-0.1754,0.4788,0.0000,0.0000,1.0000,0.0000)

Group2760.children.append(OrientationInterpolator2772)
OrientationInterpolator2773 = x3d.OrientationInterpolator()
OrientationInterpolator2773.DEF = "Jump_l_wrist_RotationInterpolator"
OrientationInterpolator2773.key = [0,0.48,0.52,0.64,0.76,0.88,1]
OrientationInterpolator2773.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0673,0.9895,-0.1281,4.1557,0.0673,0.9895,-0.1281,4.1557,0.0036,0.9999,0.0136,4.5822,0.0000,-1.0000,0.0000,0.6559,-0.0005,-1.0000,0.0013,1.2840,0.0000,0.0000,1.0000,0.0000)

Group2760.children.append(OrientationInterpolator2773)
OrientationInterpolator2774 = x3d.OrientationInterpolator()
OrientationInterpolator2774.DEF = "Jump_l_elbow_RotationInterpolator"
OrientationInterpolator2774.key = [0,0.28,0.32,0.58,0.72,1]
OrientationInterpolator2774.keyValue = (0.0000,0.0000,1.0000,0.0000,-1.0000,0.0000,0.0000,1.1300,-1.0000,0.0000,0.0000,1.7000,-1.0000,0.0000,0.0000,1.7000,-1.0000,0.0000,0.0000,0.4000,0.0000,0.0000,1.0000,0.0000)

Group2760.children.append(OrientationInterpolator2774)
OrientationInterpolator2775 = x3d.OrientationInterpolator()
OrientationInterpolator2775.DEF = "Jump_l_shoulder_RotationInterpolator"
OrientationInterpolator2775.key = [0,0.28,0.32,0.64,0.76,0.88,1]
OrientationInterpolator2775.keyValue = (0.0000,0.0000,1.0000,0.0000,-0.9987,0.0255,0.0450,1.5700,-0.9987,0.0255,0.0450,1.5700,1.0000,0.0004,0.0031,4.1140,-0.8413,0.3238,0.4329,1.4530,-0.8770,0.4198,0.2337,0.6009,0.0000,0.0000,1.0000,0.0000)

Group2760.children.append(OrientationInterpolator2775)
OrientationInterpolator2776 = x3d.OrientationInterpolator()
OrientationInterpolator2776.DEF = "Jump_head_RotationInterpolator"
OrientationInterpolator2776.key = [0,0.28,0.32,0.48,0.76,1]
OrientationInterpolator2776.keyValue = (0.0000,0.0000,1.0000,0.0000,-1.0000,0.0000,0.0000,0.5989,-1.0000,0.0000,0.0000,0.5989,-1.0000,0.0000,0.0000,0.3216,1.0000,0.0000,0.0000,0.0650,0.0000,0.0000,1.0000,0.0000)

Group2760.children.append(OrientationInterpolator2776)
OrientationInterpolator2777 = x3d.OrientationInterpolator()
OrientationInterpolator2777.DEF = "Jump_neck_RotationInterpolator"
OrientationInterpolator2777.key = [0,0.28,0.32,0.48,0.76,1]
OrientationInterpolator2777.keyValue = (0.0000,0.0000,1.0000,0.0000,-1.0000,0.0000,0.0000,0.1942,-1.0000,0.0000,0.0000,0.1942,0.0000,0.0000,1.0000,0.0000,1.0000,0.0000,0.0000,0.2284,0.0000,0.0000,1.0000,0.0000)

Group2760.children.append(OrientationInterpolator2777)
OrientationInterpolator2778 = x3d.OrientationInterpolator()
OrientationInterpolator2778.DEF = "Jump_upper_body_RotationInterpolator"
OrientationInterpolator2778.key = [0,0.22,0.28,0.34,0.71,0.88,1]
OrientationInterpolator2778.keyValue = (0.0000,0.0000,1.0000,0.0000,1.0000,0.0000,0.0000,1.0500,1.0000,0.0000,0.0000,1.0510,-1.0000,0.0000,0.0000,0.2570,1.0000,0.0000,0.0000,0.2171,1.0000,0.0000,0.0000,0.3465,0.0000,0.0000,1.0000,0.0000)

Group2760.children.append(OrientationInterpolator2778)
OrientationInterpolator2779 = x3d.OrientationInterpolator()
OrientationInterpolator2779.DEF = "Jump_whole_body_RotationInterpolator"
OrientationInterpolator2779.key = [0,0.28,0.32,0.48,0.64,0.76,1]
OrientationInterpolator2779.keyValue = (0.0000,0.0000,1.0000,0.0000,1.0000,0.0000,0.0000,0.3273,1.0000,0.0000,0.0000,0.3273,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2760.children.append(OrientationInterpolator2779)
PositionInterpolator2780 = x3d.PositionInterpolator()
PositionInterpolator2780.DEF = "Jump_whole_body_TranslationInterpolator"
PositionInterpolator2780.key = [0,0.04,0.07,0.11,0.15,0.19,0.22,0.25,0.27,0.31,0.33,0.35,0.38,0.53,0.544,0.76,0.8,0.84,0.88,0.92,0.96,1]
PositionInterpolator2780.keyValue = (0.0000,0.0000,0.0000,0.0000,-0.0126,-0.0129,0.0000,-0.0471,-0.0374,-0.0003,-0.1049,-0.0535,-0.0006,-0.1892,-0.0656,-0.0008,-0.2860,-0.0628,-0.0010,-0.3795,-0.0515,-0.0011,-0.4484,-0.0366,-0.0011,-0.4484,-0.0366,-0.0011,-0.2500,-0.1499,-0.0009,-0.0500,-0.0636,-0.0005,0.1500,-0.0549,0.0005,0.5500,0.0273,0.0002,1.3850,0.0069,0.0002,1.3950,0.0069,0.0000,0.3500,0.0215,0.0000,-0.0130,-0.0106,0.0000,-0.0693,-0.0106,0.0001,-0.1037,-0.0051,0.0001,-0.0720,-0.0076,0.0001,-0.0163,-0.0049,0.0000,0.0000,0.0000)

Group2760.children.append(PositionInterpolator2780)
OrientationInterpolator2781 = x3d.OrientationInterpolator()
OrientationInterpolator2781.DEF = "Jump_l_sternoclavicular_RollInterpolator"
OrientationInterpolator2781.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2781.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.2000,0.0000,0.0000,1.0000,0.2200,0.0000,0.0000,1.0000,0.2000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2760.children.append(OrientationInterpolator2781)
OrientationInterpolator2782 = x3d.OrientationInterpolator()
OrientationInterpolator2782.DEF = "Jump_l_acromioclavicular_RollInterpolator"
OrientationInterpolator2782.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2782.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0500,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2760.children.append(OrientationInterpolator2782)
OrientationInterpolator2783 = x3d.OrientationInterpolator()
OrientationInterpolator2783.DEF = "Jump_r_sternoclavicular_RollInterpolator"
OrientationInterpolator2783.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2783.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,-0.2000,0.0000,0.0000,1.0000,-0.2200,0.0000,0.0000,1.0000,-0.2000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2760.children.append(OrientationInterpolator2783)
OrientationInterpolator2784 = x3d.OrientationInterpolator()
OrientationInterpolator2784.DEF = "Jump_r_acromioclavicular_RollInterpolator"
OrientationInterpolator2784.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2784.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,-0.0500,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2760.children.append(OrientationInterpolator2784)
OrientationInterpolator2785 = x3d.OrientationInterpolator()
OrientationInterpolator2785.DEF = "Jump_sacroiliac_YawInterpolator"
OrientationInterpolator2785.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2785.keyValue = (0.0000,1.0000,0.0000,0.0000,0.0000,-1.0000,0.0000,0.1000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,-1.0000,0.2400,0.0000,-1.0000,0.0000,0.4000,0.0000,1.0000,0.0000,0.0000)

Group2760.children.append(OrientationInterpolator2785)
OrientationInterpolator2786 = x3d.OrientationInterpolator()
OrientationInterpolator2786.DEF = "Jump_vl5_YawInterpolator"
OrientationInterpolator2786.key = [0,0.2,0.4,0.5,0.6,0.8,1]
OrientationInterpolator2786.keyValue = (0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,-0.1000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.6000,0.0000,1.0000,0.0000,0.1000,0.0000,1.0000,0.0000,0.0000)

Group2760.children.append(OrientationInterpolator2786)
OrientationInterpolator2787 = x3d.OrientationInterpolator()
OrientationInterpolator2787.DEF = "Jump_vc6_YawInterpolator"
OrientationInterpolator2787.key = [0,0.2,0.4,0.5,0.6,0.8,1]
OrientationInterpolator2787.keyValue = (0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.8000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,-1.0000,0.0000,0.0000,0.6000,0.0000,-1.0000,0.0000,0.8000,0.0000,1.0000,0.0000,0.0000)

Group2760.children.append(OrientationInterpolator2787)
OrientationInterpolator2788 = x3d.OrientationInterpolator()
OrientationInterpolator2788.DEF = "Jump_l_thumb1_PitchInterpolator"
OrientationInterpolator2788.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2788.keyValue = (1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.5000,1.0000,0.0000,0.0000,1.1000,1.0000,0.0000,0.0000,0.7000,1.0000,0.0000,0.0000,0.2000,1.0000,0.0000,0.0000,0.0000)

Group2760.children.append(OrientationInterpolator2788)
OrientationInterpolator2789 = x3d.OrientationInterpolator()
OrientationInterpolator2789.DEF = "Jump_r_thumb1_PitchInterpolator"
OrientationInterpolator2789.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2789.keyValue = (1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.5000,1.0000,0.0000,0.0000,1.1000,1.0000,0.0000,0.0000,0.7000,1.0000,0.0000,0.0000,0.2000,1.0000,0.0000,0.0000,0.0000)

Group2760.children.append(OrientationInterpolator2789)
ROUTE2790 = x3d.ROUTE()
ROUTE2790.fromField = "fraction_changed"
ROUTE2790.fromNode = "JumpTimer"
ROUTE2790.toField = "set_fraction"
ROUTE2790.toNode = "Jump_r_ankle_RotationInterpolator"

Group2760.children.append(ROUTE2790)
ROUTE2791 = x3d.ROUTE()
ROUTE2791.fromField = "fraction_changed"
ROUTE2791.fromNode = "JumpTimer"
ROUTE2791.toField = "set_fraction"
ROUTE2791.toNode = "Jump_r_knee_RotationInterpolator"

Group2760.children.append(ROUTE2791)
ROUTE2792 = x3d.ROUTE()
ROUTE2792.fromField = "fraction_changed"
ROUTE2792.fromNode = "JumpTimer"
ROUTE2792.toField = "set_fraction"
ROUTE2792.toNode = "Jump_r_hip_RotationInterpolator"

Group2760.children.append(ROUTE2792)
ROUTE2793 = x3d.ROUTE()
ROUTE2793.fromField = "fraction_changed"
ROUTE2793.fromNode = "JumpTimer"
ROUTE2793.toField = "set_fraction"
ROUTE2793.toNode = "Jump_l_ankle_RotationInterpolator"

Group2760.children.append(ROUTE2793)
ROUTE2794 = x3d.ROUTE()
ROUTE2794.fromField = "fraction_changed"
ROUTE2794.fromNode = "JumpTimer"
ROUTE2794.toField = "set_fraction"
ROUTE2794.toNode = "Jump_l_knee_RotationInterpolator"

Group2760.children.append(ROUTE2794)
ROUTE2795 = x3d.ROUTE()
ROUTE2795.fromField = "fraction_changed"
ROUTE2795.fromNode = "JumpTimer"
ROUTE2795.toField = "set_fraction"
ROUTE2795.toNode = "Jump_l_hip_RotationInterpolator"

Group2760.children.append(ROUTE2795)
ROUTE2796 = x3d.ROUTE()
ROUTE2796.fromField = "fraction_changed"
ROUTE2796.fromNode = "JumpTimer"
ROUTE2796.toField = "set_fraction"
ROUTE2796.toNode = "Jump_lower_body_RotationInterpolator"

Group2760.children.append(ROUTE2796)
ROUTE2797 = x3d.ROUTE()
ROUTE2797.fromField = "fraction_changed"
ROUTE2797.fromNode = "JumpTimer"
ROUTE2797.toField = "set_fraction"
ROUTE2797.toNode = "Jump_r_wrist_RotationInterpolator"

Group2760.children.append(ROUTE2797)
ROUTE2798 = x3d.ROUTE()
ROUTE2798.fromField = "fraction_changed"
ROUTE2798.fromNode = "JumpTimer"
ROUTE2798.toField = "set_fraction"
ROUTE2798.toNode = "Jump_r_elbow_RotationInterpolator"

Group2760.children.append(ROUTE2798)
ROUTE2799 = x3d.ROUTE()
ROUTE2799.fromField = "fraction_changed"
ROUTE2799.fromNode = "JumpTimer"
ROUTE2799.toField = "set_fraction"
ROUTE2799.toNode = "Jump_r_shoulder_RotationInterpolator"

Group2760.children.append(ROUTE2799)
ROUTE2800 = x3d.ROUTE()
ROUTE2800.fromField = "fraction_changed"
ROUTE2800.fromNode = "JumpTimer"
ROUTE2800.toField = "set_fraction"
ROUTE2800.toNode = "Jump_l_wrist_RotationInterpolator"

Group2760.children.append(ROUTE2800)
ROUTE2801 = x3d.ROUTE()
ROUTE2801.fromField = "fraction_changed"
ROUTE2801.fromNode = "JumpTimer"
ROUTE2801.toField = "set_fraction"
ROUTE2801.toNode = "Jump_l_elbow_RotationInterpolator"

Group2760.children.append(ROUTE2801)
ROUTE2802 = x3d.ROUTE()
ROUTE2802.fromField = "fraction_changed"
ROUTE2802.fromNode = "JumpTimer"
ROUTE2802.toField = "set_fraction"
ROUTE2802.toNode = "Jump_l_shoulder_RotationInterpolator"

Group2760.children.append(ROUTE2802)
ROUTE2803 = x3d.ROUTE()
ROUTE2803.fromField = "fraction_changed"
ROUTE2803.fromNode = "JumpTimer"
ROUTE2803.toField = "set_fraction"
ROUTE2803.toNode = "Jump_head_RotationInterpolator"

Group2760.children.append(ROUTE2803)
ROUTE2804 = x3d.ROUTE()
ROUTE2804.fromField = "fraction_changed"
ROUTE2804.fromNode = "JumpTimer"
ROUTE2804.toField = "set_fraction"
ROUTE2804.toNode = "Jump_neck_RotationInterpolator"

Group2760.children.append(ROUTE2804)
ROUTE2805 = x3d.ROUTE()
ROUTE2805.fromField = "fraction_changed"
ROUTE2805.fromNode = "JumpTimer"
ROUTE2805.toField = "set_fraction"
ROUTE2805.toNode = "Jump_upper_body_RotationInterpolator"

Group2760.children.append(ROUTE2805)
ROUTE2806 = x3d.ROUTE()
ROUTE2806.fromField = "fraction_changed"
ROUTE2806.fromNode = "JumpTimer"
ROUTE2806.toField = "set_fraction"
ROUTE2806.toNode = "Jump_whole_body_RotationInterpolator"

Group2760.children.append(ROUTE2806)
ROUTE2807 = x3d.ROUTE()
ROUTE2807.fromField = "fraction_changed"
ROUTE2807.fromNode = "JumpTimer"
ROUTE2807.toField = "set_fraction"
ROUTE2807.toNode = "Jump_whole_body_TranslationInterpolator"

Group2760.children.append(ROUTE2807)
ROUTE2808 = x3d.ROUTE()
ROUTE2808.fromField = "fraction_changed"
ROUTE2808.fromNode = "JumpTimer"
ROUTE2808.toField = "set_fraction"
ROUTE2808.toNode = "Jump_l_sternoclavicular_RollInterpolator"

Group2760.children.append(ROUTE2808)
ROUTE2809 = x3d.ROUTE()
ROUTE2809.fromField = "fraction_changed"
ROUTE2809.fromNode = "JumpTimer"
ROUTE2809.toField = "set_fraction"
ROUTE2809.toNode = "Jump_l_acromioclavicular_RollInterpolator"

Group2760.children.append(ROUTE2809)
ROUTE2810 = x3d.ROUTE()
ROUTE2810.fromField = "fraction_changed"
ROUTE2810.fromNode = "JumpTimer"
ROUTE2810.toField = "set_fraction"
ROUTE2810.toNode = "Jump_r_sternoclavicular_RollInterpolator"

Group2760.children.append(ROUTE2810)
ROUTE2811 = x3d.ROUTE()
ROUTE2811.fromField = "fraction_changed"
ROUTE2811.fromNode = "JumpTimer"
ROUTE2811.toField = "set_fraction"
ROUTE2811.toNode = "Jump_r_acromioclavicular_RollInterpolator"

Group2760.children.append(ROUTE2811)
ROUTE2812 = x3d.ROUTE()
ROUTE2812.fromField = "fraction_changed"
ROUTE2812.fromNode = "JumpTimer"
ROUTE2812.toField = "set_fraction"
ROUTE2812.toNode = "Jump_r_metatarsal_PitchInterpolator"

Group2760.children.append(ROUTE2812)
ROUTE2813 = x3d.ROUTE()
ROUTE2813.fromField = "fraction_changed"
ROUTE2813.fromNode = "JumpTimer"
ROUTE2813.toField = "set_fraction"
ROUTE2813.toNode = "Jump_sacroiliac_YawInterpolator"

Group2760.children.append(ROUTE2813)
ROUTE2814 = x3d.ROUTE()
ROUTE2814.fromField = "fraction_changed"
ROUTE2814.fromNode = "JumpTimer"
ROUTE2814.toField = "set_fraction"
ROUTE2814.toNode = "Jump_vl5_YawInterpolator"

Group2760.children.append(ROUTE2814)
ROUTE2815 = x3d.ROUTE()
ROUTE2815.fromField = "fraction_changed"
ROUTE2815.fromNode = "JumpTimer"
ROUTE2815.toField = "set_fraction"
ROUTE2815.toNode = "Jump_vc6_YawInterpolator"

Group2760.children.append(ROUTE2815)
ROUTE2816 = x3d.ROUTE()
ROUTE2816.fromField = "fraction_changed"
ROUTE2816.fromNode = "JumpTimer"
ROUTE2816.toField = "set_fraction"
ROUTE2816.toNode = "Jump_l_thumb1_PitchInterpolator"

Group2760.children.append(ROUTE2816)
ROUTE2817 = x3d.ROUTE()
ROUTE2817.fromField = "fraction_changed"
ROUTE2817.fromNode = "JumpTimer"
ROUTE2817.toField = "set_fraction"
ROUTE2817.toNode = "Jump_r_thumb1_PitchInterpolator"

Group2760.children.append(ROUTE2817)
ROUTE2818 = x3d.ROUTE()
ROUTE2818.fromField = "value_changed"
ROUTE2818.fromNode = "Jump_r_ankle_RotationInterpolator"
ROUTE2818.toField = "rotation"
ROUTE2818.toNode = "hanim_r_ankle"

Group2760.children.append(ROUTE2818)
ROUTE2819 = x3d.ROUTE()
ROUTE2819.fromField = "value_changed"
ROUTE2819.fromNode = "Jump_r_knee_RotationInterpolator"
ROUTE2819.toField = "rotation"
ROUTE2819.toNode = "hanim_r_knee"

Group2760.children.append(ROUTE2819)
ROUTE2820 = x3d.ROUTE()
ROUTE2820.fromField = "value_changed"
ROUTE2820.fromNode = "Jump_r_hip_RotationInterpolator"
ROUTE2820.toField = "rotation"
ROUTE2820.toNode = "hanim_r_hip"

Group2760.children.append(ROUTE2820)
ROUTE2821 = x3d.ROUTE()
ROUTE2821.fromField = "value_changed"
ROUTE2821.fromNode = "Jump_l_ankle_RotationInterpolator"
ROUTE2821.toField = "rotation"
ROUTE2821.toNode = "hanim_l_ankle"

Group2760.children.append(ROUTE2821)
ROUTE2822 = x3d.ROUTE()
ROUTE2822.fromField = "value_changed"
ROUTE2822.fromNode = "Jump_l_knee_RotationInterpolator"
ROUTE2822.toField = "rotation"
ROUTE2822.toNode = "hanim_l_knee"

Group2760.children.append(ROUTE2822)
ROUTE2823 = x3d.ROUTE()
ROUTE2823.fromField = "value_changed"
ROUTE2823.fromNode = "Jump_l_hip_RotationInterpolator"
ROUTE2823.toField = "rotation"
ROUTE2823.toNode = "hanim_l_hip"

Group2760.children.append(ROUTE2823)
ROUTE2824 = x3d.ROUTE()
ROUTE2824.fromField = "value_changed"
ROUTE2824.fromNode = "Jump_lower_body_RotationInterpolator"
ROUTE2824.toField = "rotation"
ROUTE2824.toNode = "hanim_sacroiliac"

Group2760.children.append(ROUTE2824)
ROUTE2825 = x3d.ROUTE()
ROUTE2825.fromField = "value_changed"
ROUTE2825.fromNode = "Jump_r_wrist_RotationInterpolator"
ROUTE2825.toField = "rotation"
ROUTE2825.toNode = "hanim_r_wrist"

Group2760.children.append(ROUTE2825)
ROUTE2826 = x3d.ROUTE()
ROUTE2826.fromField = "value_changed"
ROUTE2826.fromNode = "Jump_r_elbow_RotationInterpolator"
ROUTE2826.toField = "rotation"
ROUTE2826.toNode = "hanim_r_elbow"

Group2760.children.append(ROUTE2826)
ROUTE2827 = x3d.ROUTE()
ROUTE2827.fromField = "value_changed"
ROUTE2827.fromNode = "Jump_r_shoulder_RotationInterpolator"
ROUTE2827.toField = "rotation"
ROUTE2827.toNode = "hanim_r_shoulder"

Group2760.children.append(ROUTE2827)
ROUTE2828 = x3d.ROUTE()
ROUTE2828.fromField = "value_changed"
ROUTE2828.fromNode = "Jump_l_wrist_RotationInterpolator"
ROUTE2828.toField = "rotation"
ROUTE2828.toNode = "hanim_l_wrist"

Group2760.children.append(ROUTE2828)
ROUTE2829 = x3d.ROUTE()
ROUTE2829.fromField = "value_changed"
ROUTE2829.fromNode = "Jump_l_elbow_RotationInterpolator"
ROUTE2829.toField = "rotation"
ROUTE2829.toNode = "hanim_l_elbow"

Group2760.children.append(ROUTE2829)
ROUTE2830 = x3d.ROUTE()
ROUTE2830.fromField = "value_changed"
ROUTE2830.fromNode = "Jump_l_shoulder_RotationInterpolator"
ROUTE2830.toField = "rotation"
ROUTE2830.toNode = "hanim_l_shoulder"

Group2760.children.append(ROUTE2830)
ROUTE2831 = x3d.ROUTE()
ROUTE2831.fromField = "value_changed"
ROUTE2831.fromNode = "Jump_head_RotationInterpolator"
ROUTE2831.toField = "rotation"
ROUTE2831.toNode = "hanim_skullbase"

Group2760.children.append(ROUTE2831)
ROUTE2832 = x3d.ROUTE()
ROUTE2832.fromField = "value_changed"
ROUTE2832.fromNode = "Jump_neck_RotationInterpolator"
ROUTE2832.toField = "rotation"
ROUTE2832.toNode = "hanim_vc4"

Group2760.children.append(ROUTE2832)
ROUTE2833 = x3d.ROUTE()
ROUTE2833.fromField = "value_changed"
ROUTE2833.fromNode = "Jump_upper_body_RotationInterpolator"
ROUTE2833.toField = "rotation"
ROUTE2833.toNode = "hanim_vl1"

Group2760.children.append(ROUTE2833)
ROUTE2834 = x3d.ROUTE()
ROUTE2834.fromField = "value_changed"
ROUTE2834.fromNode = "Jump_whole_body_RotationInterpolator"
ROUTE2834.toField = "rotation"
ROUTE2834.toNode = "hanim_humanoid_root"

Group2760.children.append(ROUTE2834)
ROUTE2835 = x3d.ROUTE()
ROUTE2835.fromField = "value_changed"
ROUTE2835.fromNode = "Jump_whole_body_TranslationInterpolator"
ROUTE2835.toField = "translation"
ROUTE2835.toNode = "hanim_humanoid_root"

Group2760.children.append(ROUTE2835)
ROUTE2836 = x3d.ROUTE()
ROUTE2836.fromField = "value_changed"
ROUTE2836.fromNode = "Jump_l_sternoclavicular_RollInterpolator"
ROUTE2836.toField = "rotation"
ROUTE2836.toNode = "hanim_l_sternoclavicular"

Group2760.children.append(ROUTE2836)
ROUTE2837 = x3d.ROUTE()
ROUTE2837.fromField = "value_changed"
ROUTE2837.fromNode = "Jump_l_acromioclavicular_RollInterpolator"
ROUTE2837.toField = "rotation"
ROUTE2837.toNode = "hanim_l_acromioclavicular"

Group2760.children.append(ROUTE2837)
ROUTE2838 = x3d.ROUTE()
ROUTE2838.fromField = "value_changed"
ROUTE2838.fromNode = "Jump_r_sternoclavicular_RollInterpolator"
ROUTE2838.toField = "rotation"
ROUTE2838.toNode = "hanim_r_sternoclavicular"

Group2760.children.append(ROUTE2838)
ROUTE2839 = x3d.ROUTE()
ROUTE2839.fromField = "value_changed"
ROUTE2839.fromNode = "Jump_r_acromioclavicular_RollInterpolator"
ROUTE2839.toField = "rotation"
ROUTE2839.toNode = "hanim_r_acromioclavicular"

Group2760.children.append(ROUTE2839)
ROUTE2840 = x3d.ROUTE()
ROUTE2840.fromField = "value_changed"
ROUTE2840.fromNode = "Jump_r_metatarsal_PitchInterpolator"
ROUTE2840.toField = "rotation"
ROUTE2840.toNode = "hanim_l_metatarsal"

Group2760.children.append(ROUTE2840)
ROUTE2841 = x3d.ROUTE()
ROUTE2841.fromField = "value_changed"
ROUTE2841.fromNode = "Jump_r_metatarsal_PitchInterpolator"
ROUTE2841.toField = "rotation"
ROUTE2841.toNode = "hanim_r_metatarsal"

Group2760.children.append(ROUTE2841)
ROUTE2842 = x3d.ROUTE()
ROUTE2842.fromField = "value_changed"
ROUTE2842.fromNode = "Jump_sacroiliac_YawInterpolator"
ROUTE2842.toField = "rotation"
ROUTE2842.toNode = "hanim_sacroiliac"

Group2760.children.append(ROUTE2842)
ROUTE2843 = x3d.ROUTE()
ROUTE2843.fromField = "value_changed"
ROUTE2843.fromNode = "Jump_vl5_YawInterpolator"
ROUTE2843.toField = "rotation"
ROUTE2843.toNode = "hanim_vl5"

Group2760.children.append(ROUTE2843)
ROUTE2844 = x3d.ROUTE()
ROUTE2844.fromField = "value_changed"
ROUTE2844.fromNode = "Jump_vc6_YawInterpolator"
ROUTE2844.toField = "rotation"
ROUTE2844.toNode = "hanim_vc6"

Group2760.children.append(ROUTE2844)
ROUTE2845 = x3d.ROUTE()
ROUTE2845.fromField = "value_changed"
ROUTE2845.fromNode = "Jump_l_thumb1_PitchInterpolator"
ROUTE2845.toField = "rotation"
ROUTE2845.toNode = "hanim_l_thumb1"

Group2760.children.append(ROUTE2845)
ROUTE2846 = x3d.ROUTE()
ROUTE2846.fromField = "value_changed"
ROUTE2846.fromNode = "Jump_r_thumb1_PitchInterpolator"
ROUTE2846.toField = "rotation"
ROUTE2846.toNode = "hanim_r_thumb1"

Group2760.children.append(ROUTE2846)

Scene30.children.append(Group2760)
Group2847 = x3d.Group()
Group2847.DEF = "KickAnimation"
TimeSensor2848 = x3d.TimeSensor()
TimeSensor2848.DEF = "KickTimer"
TimeSensor2848.cycleInterval = 3.73
TimeSensor2848.loop = True

Group2847.children.append(TimeSensor2848)
OrientationInterpolator2849 = x3d.OrientationInterpolator()
OrientationInterpolator2849.DEF = "Kick_l_sternoclavicular_RollInterpolator"
OrientationInterpolator2849.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2849.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.2000,0.0000,0.0000,1.0000,0.2200,0.0000,0.0000,1.0000,0.2000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2847.children.append(OrientationInterpolator2849)
OrientationInterpolator2850 = x3d.OrientationInterpolator()
OrientationInterpolator2850.DEF = "Kick_l_acromioclavicular_RollInterpolator"
OrientationInterpolator2850.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2850.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0500,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2847.children.append(OrientationInterpolator2850)
OrientationInterpolator2851 = x3d.OrientationInterpolator()
OrientationInterpolator2851.DEF = "Kick_l_shoulder_RollInterpolator"
OrientationInterpolator2851.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2851.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,1.7600,-0.2500,0.0000,1.0000,1.7600,0.0000,0.0000,1.0000,1.2560,0.0000,0.0000,1.0000,0.0500,0.0000,0.0000,1.0000,0.0000)

Group2847.children.append(OrientationInterpolator2851)
OrientationInterpolator2852 = x3d.OrientationInterpolator()
OrientationInterpolator2852.DEF = "Kick_l_ForeArm_PitchInterpolator"
OrientationInterpolator2852.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2852.keyValue = (1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,-0.5500,-1.0000,0.2500,0.0000,2.5500,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000)

Group2847.children.append(OrientationInterpolator2852)
OrientationInterpolator2853 = x3d.OrientationInterpolator()
OrientationInterpolator2853.DEF = "Kick_l_wrist_RollInterpolator"
OrientationInterpolator2853.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2853.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,1.0000,0.0000,0.5500,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2847.children.append(OrientationInterpolator2853)
OrientationInterpolator2854 = x3d.OrientationInterpolator()
OrientationInterpolator2854.DEF = "Kick_l_thumb1_PitchInterpolator"
OrientationInterpolator2854.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2854.keyValue = (1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.5000,1.0000,0.0000,0.0000,1.1000,1.0000,0.0000,0.0000,0.7000,1.0000,0.0000,0.0000,0.2000,1.0000,0.0000,0.0000,0.0000)

Group2847.children.append(OrientationInterpolator2854)
OrientationInterpolator2855 = x3d.OrientationInterpolator()
OrientationInterpolator2855.DEF = "Kick_r_sternoclavicular_RollInterpolator"
OrientationInterpolator2855.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2855.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,-0.2000,0.0000,0.0000,1.0000,-0.2200,0.0000,0.0000,1.0000,-0.2000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2847.children.append(OrientationInterpolator2855)
OrientationInterpolator2856 = x3d.OrientationInterpolator()
OrientationInterpolator2856.DEF = "Kick_r_acromioclavicular_RollInterpolator"
OrientationInterpolator2856.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2856.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,-0.0500,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2847.children.append(OrientationInterpolator2856)
OrientationInterpolator2857 = x3d.OrientationInterpolator()
OrientationInterpolator2857.DEF = "Kick_r_shoulder_RollInterpolator"
OrientationInterpolator2857.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2857.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,-1.7600,0.2500,0.0000,1.0000,-1.7600,0.0000,0.0000,1.0000,-1.2560,0.0000,0.0000,1.0000,-0.0500,0.0000,0.0000,1.0000,0.0000)

Group2847.children.append(OrientationInterpolator2857)
OrientationInterpolator2858 = x3d.OrientationInterpolator()
OrientationInterpolator2858.DEF = "Kick_r_ForeArm_PitchInterpolator"
OrientationInterpolator2858.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2858.keyValue = (1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,-0.5500,1.0000,0.2500,0.0000,-2.5500,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000)

Group2847.children.append(OrientationInterpolator2858)
OrientationInterpolator2859 = x3d.OrientationInterpolator()
OrientationInterpolator2859.DEF = "Kick_r_wrist_RollInterpolator"
OrientationInterpolator2859.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2859.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,1.0000,0.0000,-0.5500,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2847.children.append(OrientationInterpolator2859)
OrientationInterpolator2860 = x3d.OrientationInterpolator()
OrientationInterpolator2860.DEF = "Kick_r_thumb1_PitchInterpolator"
OrientationInterpolator2860.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2860.keyValue = (1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.5000,1.0000,0.0000,0.0000,1.1000,1.0000,0.0000,0.0000,0.7000,1.0000,0.0000,0.0000,0.2000,1.0000,0.0000,0.0000,0.0000)

Group2847.children.append(OrientationInterpolator2860)
OrientationInterpolator2861 = x3d.OrientationInterpolator()
OrientationInterpolator2861.DEF = "Kick_r_hip_PitchInterpolator"
OrientationInterpolator2861.key = [0,0.2,0.3,0.5,0.6,0.9,1]
OrientationInterpolator2861.keyValue = (1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.9000,-1.0000,0.0000,0.0000,1.7500,-1.0000,0.0000,0.0000,2.2500,-1.0000,0.0000,0.0000,2.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000)

Group2847.children.append(OrientationInterpolator2861)
OrientationInterpolator2862 = x3d.OrientationInterpolator()
OrientationInterpolator2862.DEF = "Kick_r_knee_PitchInterpolator"
OrientationInterpolator2862.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2862.keyValue = (0.0000,0.0000,1.0000,0.0000,1.0000,0.0000,0.0000,1.9500,1.0000,0.0000,0.0000,1.7500,-1.0000,0.0000,0.0000,0.2800,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000)

Group2847.children.append(OrientationInterpolator2862)
OrientationInterpolator2863 = x3d.OrientationInterpolator()
OrientationInterpolator2863.DEF = "Kick_l_hip_PitchInterpolator"
OrientationInterpolator2863.key = [0,0.2,0.3,0.5,0.6,0.9,1]
OrientationInterpolator2863.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2847.children.append(OrientationInterpolator2863)
OrientationInterpolator2864 = x3d.OrientationInterpolator()
OrientationInterpolator2864.DEF = "Kick_l_knee_PitchInterpolator"
OrientationInterpolator2864.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2864.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2847.children.append(OrientationInterpolator2864)
OrientationInterpolator2865 = x3d.OrientationInterpolator()
OrientationInterpolator2865.DEF = "Kick_r_ankle_PitchInterpolator"
OrientationInterpolator2865.key = [0,0.2,0.4,0.6,0.7,1]
OrientationInterpolator2865.keyValue = (0.0000,0.0000,1.0000,0.0000,-1.0000,0.0000,0.0000,0.9000,-1.0000,0.0000,0.0000,0.9500,1.0000,0.0000,0.0000,0.7500,-1.0000,0.0000,0.0000,0.0500,1.0000,0.0000,0.0000,0.0000)

Group2847.children.append(OrientationInterpolator2865)
OrientationInterpolator2866 = x3d.OrientationInterpolator()
OrientationInterpolator2866.DEF = "Kick_r_metatarsal_PitchInterpolator"
OrientationInterpolator2866.key = [0,0.2,0.4,0.6,0.7,1]
OrientationInterpolator2866.keyValue = (1.0000,0.0000,0.0000,0.0000,-1.0000,0.0000,0.0000,0.5000,-1.0000,0.0000,0.0000,0.7000,1.0000,0.0000,0.0000,0.7500,-1.0000,0.0000,0.0000,0.2000,1.0000,0.0000,0.0000,0.0000)

Group2847.children.append(OrientationInterpolator2866)
OrientationInterpolator2867 = x3d.OrientationInterpolator()
OrientationInterpolator2867.DEF = "Kick_sacroiliac_YawInterpolator"
OrientationInterpolator2867.key = [0,0.2,0.4,0.6,0.8,1]
OrientationInterpolator2867.keyValue = (0.0000,1.0000,0.0000,0.0000,0.0000,-1.0000,0.0000,0.1000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,-1.0000,0.2400,0.0000,-1.0000,0.0000,0.4000,0.0000,1.0000,0.0000,0.0000)

Group2847.children.append(OrientationInterpolator2867)
OrientationInterpolator2868 = x3d.OrientationInterpolator()
OrientationInterpolator2868.DEF = "Kick_vl5_YawInterpolator"
OrientationInterpolator2868.key = [0,0.2,0.4,0.5,0.6,0.8,1]
OrientationInterpolator2868.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2847.children.append(OrientationInterpolator2868)
OrientationInterpolator2869 = x3d.OrientationInterpolator()
OrientationInterpolator2869.DEF = "Kick_vc6_YawInterpolator"
OrientationInterpolator2869.key = [0,0.2,0.4,0.5,0.6,0.8,1]
OrientationInterpolator2869.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2847.children.append(OrientationInterpolator2869)
OrientationInterpolator2870 = x3d.OrientationInterpolator()
OrientationInterpolator2870.DEF = "Kick_lower_body_RotationInterpolator"
OrientationInterpolator2870.key = [0,0.5,1]
OrientationInterpolator2870.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2847.children.append(OrientationInterpolator2870)
OrientationInterpolator2871 = x3d.OrientationInterpolator()
OrientationInterpolator2871.DEF = "Kick_upper_body_RotationInterpolator"
OrientationInterpolator2871.key = [0,0.5,1]
OrientationInterpolator2871.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2847.children.append(OrientationInterpolator2871)
OrientationInterpolator2872 = x3d.OrientationInterpolator()
OrientationInterpolator2872.DEF = "Kick_whole_body_RotationInterpolator"
OrientationInterpolator2872.key = [0,0.5,1]
OrientationInterpolator2872.keyValue = (0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000,0.0000,0.0000,1.0000,0.0000)

Group2847.children.append(OrientationInterpolator2872)
PositionInterpolator2873 = x3d.PositionInterpolator()
PositionInterpolator2873.DEF = "Kick_whole_body_TranslationInterpolator"
PositionInterpolator2873.key = [0,0.5,1]
PositionInterpolator2873.keyValue = (0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000)

Group2847.children.append(PositionInterpolator2873)
OrientationInterpolator2874 = x3d.OrientationInterpolator()
OrientationInterpolator2874.DEF = "Kick_neck_RotationInterpolator"
OrientationInterpolator2874.key = [0,0.25,0.55,1]
OrientationInterpolator2874.keyValue = (0.0000,0.0000,1.0000,0.0000,1.0000,0.0000,0.0000,0.7000,1.0000,0.0000,0.0000,0.5000,0.0000,0.0000,1.0000,0.0000)

Group2847.children.append(OrientationInterpolator2874)
ROUTE2875 = x3d.ROUTE()
ROUTE2875.fromField = "fraction_changed"
ROUTE2875.fromNode = "KickTimer"
ROUTE2875.toField = "set_fraction"
ROUTE2875.toNode = "Kick_l_sternoclavicular_RollInterpolator"

Group2847.children.append(ROUTE2875)
ROUTE2876 = x3d.ROUTE()
ROUTE2876.fromField = "fraction_changed"
ROUTE2876.fromNode = "KickTimer"
ROUTE2876.toField = "set_fraction"
ROUTE2876.toNode = "Kick_l_acromioclavicular_RollInterpolator"

Group2847.children.append(ROUTE2876)
ROUTE2877 = x3d.ROUTE()
ROUTE2877.fromField = "fraction_changed"
ROUTE2877.fromNode = "KickTimer"
ROUTE2877.toField = "set_fraction"
ROUTE2877.toNode = "Kick_l_shoulder_RollInterpolator"

Group2847.children.append(ROUTE2877)
ROUTE2878 = x3d.ROUTE()
ROUTE2878.fromField = "fraction_changed"
ROUTE2878.fromNode = "KickTimer"
ROUTE2878.toField = "set_fraction"
ROUTE2878.toNode = "Kick_l_ForeArm_PitchInterpolator"

Group2847.children.append(ROUTE2878)
ROUTE2879 = x3d.ROUTE()
ROUTE2879.fromField = "fraction_changed"
ROUTE2879.fromNode = "KickTimer"
ROUTE2879.toField = "set_fraction"
ROUTE2879.toNode = "Kick_l_wrist_RollInterpolator"

Group2847.children.append(ROUTE2879)
ROUTE2880 = x3d.ROUTE()
ROUTE2880.fromField = "fraction_changed"
ROUTE2880.fromNode = "KickTimer"
ROUTE2880.toField = "set_fraction"
ROUTE2880.toNode = "Kick_l_thumb1_PitchInterpolator"

Group2847.children.append(ROUTE2880)
ROUTE2881 = x3d.ROUTE()
ROUTE2881.fromField = "fraction_changed"
ROUTE2881.fromNode = "KickTimer"
ROUTE2881.toField = "set_fraction"
ROUTE2881.toNode = "Kick_r_sternoclavicular_RollInterpolator"

Group2847.children.append(ROUTE2881)
ROUTE2882 = x3d.ROUTE()
ROUTE2882.fromField = "fraction_changed"
ROUTE2882.fromNode = "KickTimer"
ROUTE2882.toField = "set_fraction"
ROUTE2882.toNode = "Kick_r_acromioclavicular_RollInterpolator"

Group2847.children.append(ROUTE2882)
ROUTE2883 = x3d.ROUTE()
ROUTE2883.fromField = "fraction_changed"
ROUTE2883.fromNode = "KickTimer"
ROUTE2883.toField = "set_fraction"
ROUTE2883.toNode = "Kick_r_shoulder_RollInterpolator"

Group2847.children.append(ROUTE2883)
ROUTE2884 = x3d.ROUTE()
ROUTE2884.fromField = "fraction_changed"
ROUTE2884.fromNode = "KickTimer"
ROUTE2884.toField = "set_fraction"
ROUTE2884.toNode = "Kick_r_ForeArm_PitchInterpolator"

Group2847.children.append(ROUTE2884)
ROUTE2885 = x3d.ROUTE()
ROUTE2885.fromField = "fraction_changed"
ROUTE2885.fromNode = "KickTimer"
ROUTE2885.toField = "set_fraction"
ROUTE2885.toNode = "Kick_r_wrist_RollInterpolator"

Group2847.children.append(ROUTE2885)
ROUTE2886 = x3d.ROUTE()
ROUTE2886.fromField = "fraction_changed"
ROUTE2886.fromNode = "KickTimer"
ROUTE2886.toField = "set_fraction"
ROUTE2886.toNode = "Kick_r_thumb1_PitchInterpolator"

Group2847.children.append(ROUTE2886)
ROUTE2887 = x3d.ROUTE()
ROUTE2887.fromField = "fraction_changed"
ROUTE2887.fromNode = "KickTimer"
ROUTE2887.toField = "set_fraction"
ROUTE2887.toNode = "Kick_r_hip_PitchInterpolator"

Group2847.children.append(ROUTE2887)
ROUTE2888 = x3d.ROUTE()
ROUTE2888.fromField = "fraction_changed"
ROUTE2888.fromNode = "KickTimer"
ROUTE2888.toField = "set_fraction"
ROUTE2888.toNode = "Kick_r_knee_PitchInterpolator"

Group2847.children.append(ROUTE2888)
ROUTE2889 = x3d.ROUTE()
ROUTE2889.fromField = "fraction_changed"
ROUTE2889.fromNode = "KickTimer"
ROUTE2889.toField = "set_fraction"
ROUTE2889.toNode = "Kick_l_hip_PitchInterpolator"

Group2847.children.append(ROUTE2889)
ROUTE2890 = x3d.ROUTE()
ROUTE2890.fromField = "fraction_changed"
ROUTE2890.fromNode = "KickTimer"
ROUTE2890.toField = "set_fraction"
ROUTE2890.toNode = "Kick_l_knee_PitchInterpolator"

Group2847.children.append(ROUTE2890)
ROUTE2891 = x3d.ROUTE()
ROUTE2891.fromField = "fraction_changed"
ROUTE2891.fromNode = "KickTimer"
ROUTE2891.toField = "set_fraction"
ROUTE2891.toNode = "Kick_r_ankle_PitchInterpolator"

Group2847.children.append(ROUTE2891)
ROUTE2892 = x3d.ROUTE()
ROUTE2892.fromField = "fraction_changed"
ROUTE2892.fromNode = "KickTimer"
ROUTE2892.toField = "set_fraction"
ROUTE2892.toNode = "Kick_r_metatarsal_PitchInterpolator"

Group2847.children.append(ROUTE2892)
ROUTE2893 = x3d.ROUTE()
ROUTE2893.fromField = "fraction_changed"
ROUTE2893.fromNode = "KickTimer"
ROUTE2893.toField = "set_fraction"
ROUTE2893.toNode = "Kick_sacroiliac_YawInterpolator"

Group2847.children.append(ROUTE2893)
ROUTE2894 = x3d.ROUTE()
ROUTE2894.fromField = "fraction_changed"
ROUTE2894.fromNode = "KickTimer"
ROUTE2894.toField = "set_fraction"
ROUTE2894.toNode = "Kick_vl5_YawInterpolator"

Group2847.children.append(ROUTE2894)
ROUTE2895 = x3d.ROUTE()
ROUTE2895.fromField = "fraction_changed"
ROUTE2895.fromNode = "KickTimer"
ROUTE2895.toField = "set_fraction"
ROUTE2895.toNode = "Kick_vc6_YawInterpolator"

Group2847.children.append(ROUTE2895)
ROUTE2896 = x3d.ROUTE()
ROUTE2896.fromField = "fraction_changed"
ROUTE2896.fromNode = "KickTimer"
ROUTE2896.toField = "set_fraction"
ROUTE2896.toNode = "Kick_lower_body_RotationInterpolator"

Group2847.children.append(ROUTE2896)
ROUTE2897 = x3d.ROUTE()
ROUTE2897.fromField = "fraction_changed"
ROUTE2897.fromNode = "KickTimer"
ROUTE2897.toField = "set_fraction"
ROUTE2897.toNode = "Kick_upper_body_RotationInterpolator"

Group2847.children.append(ROUTE2897)
ROUTE2898 = x3d.ROUTE()
ROUTE2898.fromField = "fraction_changed"
ROUTE2898.fromNode = "KickTimer"
ROUTE2898.toField = "set_fraction"
ROUTE2898.toNode = "Kick_whole_body_RotationInterpolator"

Group2847.children.append(ROUTE2898)
ROUTE2899 = x3d.ROUTE()
ROUTE2899.fromField = "fraction_changed"
ROUTE2899.fromNode = "KickTimer"
ROUTE2899.toField = "set_fraction"
ROUTE2899.toNode = "Kick_whole_body_TranslationInterpolator"

Group2847.children.append(ROUTE2899)
ROUTE2900 = x3d.ROUTE()
ROUTE2900.fromField = "fraction_changed"
ROUTE2900.fromNode = "KickTimer"
ROUTE2900.toField = "set_fraction"
ROUTE2900.toNode = "Kick_neck_RotationInterpolator"

Group2847.children.append(ROUTE2900)
ROUTE2901 = x3d.ROUTE()
ROUTE2901.fromField = "value_changed"
ROUTE2901.fromNode = "Kick_l_sternoclavicular_RollInterpolator"
ROUTE2901.toField = "rotation"
ROUTE2901.toNode = "hanim_l_sternoclavicular"

Group2847.children.append(ROUTE2901)
ROUTE2902 = x3d.ROUTE()
ROUTE2902.fromField = "value_changed"
ROUTE2902.fromNode = "Kick_l_acromioclavicular_RollInterpolator"
ROUTE2902.toField = "rotation"
ROUTE2902.toNode = "hanim_l_acromioclavicular"

Group2847.children.append(ROUTE2902)
ROUTE2903 = x3d.ROUTE()
ROUTE2903.fromField = "value_changed"
ROUTE2903.fromNode = "Kick_l_shoulder_RollInterpolator"
ROUTE2903.toField = "rotation"
ROUTE2903.toNode = "hanim_l_shoulder"

Group2847.children.append(ROUTE2903)
ROUTE2904 = x3d.ROUTE()
ROUTE2904.fromField = "value_changed"
ROUTE2904.fromNode = "Kick_l_ForeArm_PitchInterpolator"
ROUTE2904.toField = "rotation"
ROUTE2904.toNode = "hanim_l_elbow"

Group2847.children.append(ROUTE2904)
ROUTE2905 = x3d.ROUTE()
ROUTE2905.fromField = "value_changed"
ROUTE2905.fromNode = "Kick_l_wrist_RollInterpolator"
ROUTE2905.toField = "rotation"
ROUTE2905.toNode = "hanim_l_wrist"

Group2847.children.append(ROUTE2905)
ROUTE2906 = x3d.ROUTE()
ROUTE2906.fromField = "value_changed"
ROUTE2906.fromNode = "Kick_l_thumb1_PitchInterpolator"
ROUTE2906.toField = "rotation"
ROUTE2906.toNode = "hanim_l_thumb1"

Group2847.children.append(ROUTE2906)
ROUTE2907 = x3d.ROUTE()
ROUTE2907.fromField = "value_changed"
ROUTE2907.fromNode = "Kick_r_sternoclavicular_RollInterpolator"
ROUTE2907.toField = "rotation"
ROUTE2907.toNode = "hanim_r_sternoclavicular"

Group2847.children.append(ROUTE2907)
ROUTE2908 = x3d.ROUTE()
ROUTE2908.fromField = "value_changed"
ROUTE2908.fromNode = "Kick_r_acromioclavicular_RollInterpolator"
ROUTE2908.toField = "rotation"
ROUTE2908.toNode = "hanim_r_acromioclavicular"

Group2847.children.append(ROUTE2908)
ROUTE2909 = x3d.ROUTE()
ROUTE2909.fromField = "value_changed"
ROUTE2909.fromNode = "Kick_r_shoulder_RollInterpolator"
ROUTE2909.toField = "rotation"
ROUTE2909.toNode = "hanim_r_shoulder"

Group2847.children.append(ROUTE2909)
ROUTE2910 = x3d.ROUTE()
ROUTE2910.fromField = "value_changed"
ROUTE2910.fromNode = "Kick_r_ForeArm_PitchInterpolator"
ROUTE2910.toField = "rotation"
ROUTE2910.toNode = "hanim_r_elbow"

Group2847.children.append(ROUTE2910)
ROUTE2911 = x3d.ROUTE()
ROUTE2911.fromField = "value_changed"
ROUTE2911.fromNode = "Kick_r_wrist_RollInterpolator"
ROUTE2911.toField = "rotation"
ROUTE2911.toNode = "hanim_r_wrist"

Group2847.children.append(ROUTE2911)
ROUTE2912 = x3d.ROUTE()
ROUTE2912.fromField = "value_changed"
ROUTE2912.fromNode = "Kick_r_thumb1_PitchInterpolator"
ROUTE2912.toField = "rotation"
ROUTE2912.toNode = "hanim_r_thumb1"

Group2847.children.append(ROUTE2912)
ROUTE2913 = x3d.ROUTE()
ROUTE2913.fromField = "value_changed"
ROUTE2913.fromNode = "Kick_r_hip_PitchInterpolator"
ROUTE2913.toField = "rotation"
ROUTE2913.toNode = "hanim_r_hip"

Group2847.children.append(ROUTE2913)
ROUTE2914 = x3d.ROUTE()
ROUTE2914.fromField = "value_changed"
ROUTE2914.fromNode = "Kick_r_knee_PitchInterpolator"
ROUTE2914.toField = "rotation"
ROUTE2914.toNode = "hanim_r_knee"

Group2847.children.append(ROUTE2914)
ROUTE2915 = x3d.ROUTE()
ROUTE2915.fromField = "value_changed"
ROUTE2915.fromNode = "Kick_r_ankle_PitchInterpolator"
ROUTE2915.toField = "rotation"
ROUTE2915.toNode = "hanim_r_ankle"

Group2847.children.append(ROUTE2915)
ROUTE2916 = x3d.ROUTE()
ROUTE2916.fromField = "value_changed"
ROUTE2916.fromNode = "Kick_r_metatarsal_PitchInterpolator"
ROUTE2916.toField = "rotation"
ROUTE2916.toNode = "hanim_r_metatarsal"

Group2847.children.append(ROUTE2916)
ROUTE2917 = x3d.ROUTE()
ROUTE2917.fromField = "value_changed"
ROUTE2917.fromNode = "Kick_l_hip_PitchInterpolator"
ROUTE2917.toField = "rotation"
ROUTE2917.toNode = "hanim_l_hip"

Group2847.children.append(ROUTE2917)
ROUTE2918 = x3d.ROUTE()
ROUTE2918.fromField = "value_changed"
ROUTE2918.fromNode = "Kick_l_knee_PitchInterpolator"
ROUTE2918.toField = "rotation"
ROUTE2918.toNode = "hanim_l_knee"

Group2847.children.append(ROUTE2918)
ROUTE2919 = x3d.ROUTE()
ROUTE2919.fromField = "value_changed"
ROUTE2919.fromNode = "Kick_r_ankle_PitchInterpolator"
ROUTE2919.toField = "rotation"
ROUTE2919.toNode = "hanim_l_ankle"

Group2847.children.append(ROUTE2919)
ROUTE2920 = x3d.ROUTE()
ROUTE2920.fromField = "value_changed"
ROUTE2920.fromNode = "Kick_r_metatarsal_PitchInterpolator"
ROUTE2920.toField = "rotation"
ROUTE2920.toNode = "hanim_l_metatarsal"

Group2847.children.append(ROUTE2920)
ROUTE2921 = x3d.ROUTE()
ROUTE2921.fromField = "value_changed"
ROUTE2921.fromNode = "Kick_sacroiliac_YawInterpolator"
ROUTE2921.toField = "rotation"
ROUTE2921.toNode = "hanim_sacroiliac"

Group2847.children.append(ROUTE2921)
ROUTE2922 = x3d.ROUTE()
ROUTE2922.fromField = "value_changed"
ROUTE2922.fromNode = "Kick_vl5_YawInterpolator"
ROUTE2922.toField = "rotation"
ROUTE2922.toNode = "hanim_vl5"

Group2847.children.append(ROUTE2922)
ROUTE2923 = x3d.ROUTE()
ROUTE2923.fromField = "value_changed"
ROUTE2923.fromNode = "Kick_vc6_YawInterpolator"
ROUTE2923.toField = "rotation"
ROUTE2923.toNode = "hanim_vc6"

Group2847.children.append(ROUTE2923)
ROUTE2924 = x3d.ROUTE()
ROUTE2924.fromField = "value_changed"
ROUTE2924.fromNode = "Kick_upper_body_RotationInterpolator"
ROUTE2924.toField = "rotation"
ROUTE2924.toNode = "hanim_vl1"

Group2847.children.append(ROUTE2924)
ROUTE2925 = x3d.ROUTE()
ROUTE2925.fromField = "value_changed"
ROUTE2925.fromNode = "Kick_lower_body_RotationInterpolator"
ROUTE2925.toField = "rotation"
ROUTE2925.toNode = "hanim_sacroiliac"

Group2847.children.append(ROUTE2925)
ROUTE2926 = x3d.ROUTE()
ROUTE2926.fromField = "value_changed"
ROUTE2926.fromNode = "Kick_whole_body_RotationInterpolator"
ROUTE2926.toField = "rotation"
ROUTE2926.toNode = "hanim_humanoid_root"

Group2847.children.append(ROUTE2926)
ROUTE2927 = x3d.ROUTE()
ROUTE2927.fromField = "value_changed"
ROUTE2927.fromNode = "Kick_whole_body_TranslationInterpolator"
ROUTE2927.toField = "translation"
ROUTE2927.toNode = "hanim_humanoid_root"

Group2847.children.append(ROUTE2927)
ROUTE2928 = x3d.ROUTE()
ROUTE2928.fromField = "value_changed"
ROUTE2928.fromNode = "Kick_neck_RotationInterpolator"
ROUTE2928.toField = "rotation"
ROUTE2928.toNode = "hanim_vc4"

Group2847.children.append(ROUTE2928)

Scene30.children.append(Group2847)
Group2929 = x3d.Group()
Group2929.DEF = "UserInterface"
#Authoring hint: these axes are aligned within local coordinate system
Transform2930 = x3d.Transform()
Transform2930.DEF = "CoordinateAxesAdjustedScale"
Transform2930.scale = [0.175,0.175,0.175]
Inline2931 = x3d.Inline()
Inline2931.DEF = "CoordinateAxes"
Inline2931.url = ["../../X3dForWebAuthors/Chapter03Grouping/CoordinateAxes.x3d","https://X3dGraphics.com/examples/X3dForWebAuthors/Chapter03Grouping/CoordinateAxes.x3d","../../X3dForWebAuthors/Chapter03Grouping/CoordinateAxes.wrl","https://X3dGraphics.com/examples/X3dForWebAuthors/Chapter03Grouping/CoordinateAxes.wrl"]

Transform2930.children.append(Inline2931)

Group2929.children.append(Transform2930)
Transform2932 = x3d.Transform()
Transform2932.DEF = "cordsys"
Transform2932.scale = [0.175,0.175,0.175]
#<Inline bboxCenter='0.05143541 0.07883984 0.04731131' bboxSize='2.202872 2.25768 2.194624' url='\"JointCoordinateAxes.x3dv\"'/>

Group2929.children.append(Transform2932)
ProximitySensor2933 = x3d.ProximitySensor()
ProximitySensor2933.DEF = "HudProximitySensor"
ProximitySensor2933.center = [0,20,0]
ProximitySensor2933.size = [500,100,500]

Group2929.children.append(ProximitySensor2933)
Transform2934 = x3d.Transform()
Transform2934.DEF = "Stage"
Transform2934.scale = [1,0.0125,1]
Transform2934.translation = [0,-0.0125,0]
Shape2935 = x3d.Shape()
Appearance2936 = x3d.Appearance()
Material2937 = x3d.Material()
Material2937.transparency = 0.6

Appearance2936.material = Material2937

Shape2935.appearance = Appearance2936
Box2938 = x3d.Box()

Shape2935.geometry = Box2938

Transform2934.children.append(Shape2935)
Transform2939 = x3d.Transform()
Transform2939.DEF = "Circle0"
Transform2939.scale = [1.175,1,1.175]
Shape2940 = x3d.Shape()
Appearance2941 = x3d.Appearance()
Material2942 = x3d.Material()
Material2942.diffuseColor = [0.9,0,0.7]
Material2942.emissiveColor = [0.424956,0.483976,1]

Appearance2941.material = Material2942

Shape2940.appearance = Appearance2941
IndexedLineSet2943 = x3d.IndexedLineSet()
IndexedLineSet2943.DEF = "Orbit1"
IndexedLineSet2943.coordIndex = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,-1]
Coordinate2944 = x3d.Coordinate()
Coordinate2944.point = (1.0000,0.0000,0.0000,0.9950,0.0000,-0.1050,0.9790,0.0000,-0.2080,0.9510,0.0000,-0.3090,0.9140,0.0000,-0.4070,0.8660,0.0000,-0.5000,0.8090,0.0000,-0.5880,0.7430,0.0000,-0.6690,0.6690,0.0000,-0.7430,0.5880,0.0000,-0.8090,0.5000,0.0000,-0.8660,0.4070,0.0000,-0.9140,0.3090,0.0000,-0.9510,0.2080,0.0000,-0.9780,0.1050,0.0000,-0.9950,0.0000,0.0000,-1.0000,-0.1050,0.0000,-0.9945,-0.2080,0.0000,-0.9780,-0.3090,0.0000,-0.9510,-0.4070,0.0000,-0.9140,-0.5000,0.0000,-0.8660,-0.5880,0.0000,-0.8090,-0.6690,0.0000,-0.7430,-0.7430,0.0000,-0.6690,-0.8090,0.0000,-0.5880,-0.8660,0.0000,-0.5000,-0.9140,0.0000,-0.4070,-0.9510,0.0000,-0.3090,-0.9780,0.0000,-0.2080,-0.9950,0.0000,-0.1050,-1.0000,0.0000,0.0000,-0.9950,0.0000,0.1050,-0.9780,0.0000,0.2080,-0.9510,0.0000,0.3090,-0.9140,0.0000,0.4070,-0.8660,0.0000,0.5000,-0.8090,0.0000,0.5880,-0.7430,0.0000,0.6690,-0.6690,0.0000,0.7430,-0.5880,0.0000,0.8090,-0.5000,0.0000,0.8660,-0.4070,0.0000,0.9140,-0.3090,0.0000,0.9510,-0.2080,0.0000,0.9780,-0.1050,0.0000,0.9950,0.0000,0.0000,1.0000,0.1050,0.0000,0.9950,0.2080,0.0000,0.9780,0.3090,0.0000,0.9510,0.4070,0.0000,0.9140,0.5000,0.0000,0.8660,0.5880,0.0000,0.8090,0.6690,0.0000,0.7430,0.7430,0.0000,0.6690,0.8090,0.0000,0.5880,0.8660,0.0000,0.5000,0.9140,0.0000,0.4070,0.9510,0.0000,0.3090,0.9780,0.0000,0.2080,0.9950,0.0000,0.1040,1.0000,0.0000,0.0000)

IndexedLineSet2943.coord = Coordinate2944

Shape2940.geometry = IndexedLineSet2943

Transform2939.children.append(Shape2940)

Transform2934.children.append(Transform2939)
Transform2945 = x3d.Transform()
Transform2945.DEF = "Circle1"
Transform2945.scale = [0.5,1,0.5]
Shape2946 = x3d.Shape()
Appearance2947 = x3d.Appearance()
Material2948 = x3d.Material()
Material2948.diffuseColor = [0.9,0,0.7]
Material2948.emissiveColor = [0.424956,0.483976,1]

Appearance2947.material = Material2948

Shape2946.appearance = Appearance2947
IndexedLineSet2949 = x3d.IndexedLineSet()
IndexedLineSet2949.USE = "Orbit1"

Shape2946.geometry = IndexedLineSet2949

Transform2945.children.append(Shape2946)

Transform2934.children.append(Transform2945)
Transform2950 = x3d.Transform()
Transform2950.DEF = "Circle2"
Transform2950.scale = [0.25,1,0.25]
Shape2951 = x3d.Shape()
Appearance2952 = x3d.Appearance()
Material2953 = x3d.Material()
Material2953.diffuseColor = [0.9,0,0.7]
Material2953.emissiveColor = [0.424956,0.483976,1]

Appearance2952.material = Material2953

Shape2951.appearance = Appearance2952
IndexedLineSet2954 = x3d.IndexedLineSet()
IndexedLineSet2954.USE = "Orbit1"

Shape2951.geometry = IndexedLineSet2954

Transform2950.children.append(Shape2951)

Transform2934.children.append(Transform2950)

Group2929.children.append(Transform2934)
Transform2955 = x3d.Transform()
Transform2955.DEF = "HudXform"
Transform2955.rotation = [-0.09996068,0.9942513,0.03837026,0.7131352]
Transform2955.translation = [1.705442,1.042139,1.989742]
Transform2956 = x3d.Transform()
Transform2956.scale = [0.035,0.035,0.035]
Transform2956.translation = [-0.42,-0.2,-0.75]
Transform2957 = x3d.Transform()
Transform2957.DEF = "StandTransform"
Transform2957.translation = [0,-1,0]
TouchSensor2958 = x3d.TouchSensor()
TouchSensor2958.DEF = "Stand_Touch"
TouchSensor2958.description = "touch to select"

Transform2957.children.append(TouchSensor2958)
Shape2959 = x3d.Shape()
Shape2959.DEF = "StandTextShape"
Appearance2960 = x3d.Appearance()
Material2961 = x3d.Material()
Material2961.DEF = "text_color"
Material2961.ambientIntensity = 1
Material2961.diffuseColor = [0.819,0.521,0.169]
Material2961.emissiveColor = [0.819,0.521,0.169]
Material2961.specularColor = [0.819,0.521,0.169]

Appearance2960.material = Material2961

Shape2959.appearance = Appearance2960
Text2962 = x3d.Text()
Text2962.string = ["Stand"]

Shape2959.geometry = Text2962

Transform2957.children.append(Shape2959)
Shape2963 = x3d.Shape()
Shape2963.DEF = "Stand_Back"
Appearance2964 = x3d.Appearance()
Material2965 = x3d.Material()
Material2965.DEF = "Clear"
Material2965.ambientIntensity = 1
Material2965.diffuseColor = [0,0.5,0]
Material2965.emissiveColor = [0,0.5,0]
Material2965.transparency = 0.8

Appearance2964.material = Material2965

Shape2963.appearance = Appearance2964
IndexedFaceSet2966 = x3d.IndexedFaceSet()
IndexedFaceSet2966.DEF = "Backing"
IndexedFaceSet2966.coordIndex = [0,1,2,3,-1]
Coordinate2967 = x3d.Coordinate()
Coordinate2967.point = (-0.2000,-1.2000,-0.0100,2.5000,-1.2000,-0.0100,2.5000,0.7500,-0.0100,-0.2000,0.7500,-0.0100)

IndexedFaceSet2966.coord = Coordinate2967

Shape2963.geometry = IndexedFaceSet2966

Transform2957.children.append(Shape2963)

Transform2956.children.append(Transform2957)
Transform2968 = x3d.Transform()
Transform2968.DEF = "PitchTransform"
Transform2968.translation = [3,-1,0]
TouchSensor2969 = x3d.TouchSensor()
TouchSensor2969.DEF = "Pitch_Touch"
TouchSensor2969.description = "touch to select"

Transform2968.children.append(TouchSensor2969)
Shape2970 = x3d.Shape()
Shape2970.DEF = "PitchTextShape"
Appearance2971 = x3d.Appearance()
Material2972 = x3d.Material()
Material2972.USE = "text_color"

Appearance2971.material = Material2972

Shape2970.appearance = Appearance2971
Text2973 = x3d.Text()
Text2973.string = ["Pitch"]

Shape2970.geometry = Text2973

Transform2968.children.append(Shape2970)
Shape2974 = x3d.Shape()
Shape2974.DEF = "Pitch_Back"
Appearance2975 = x3d.Appearance()
Material2976 = x3d.Material()
Material2976.USE = "Clear"

Appearance2975.material = Material2976

Shape2974.appearance = Appearance2975
IndexedFaceSet2977 = x3d.IndexedFaceSet()
IndexedFaceSet2977.USE = "Backing"

Shape2974.geometry = IndexedFaceSet2977

Transform2968.children.append(Shape2974)

Transform2956.children.append(Transform2968)
Transform2978 = x3d.Transform()
Transform2978.DEF = "YawTransform"
Transform2978.translation = [6,-1,0]
TouchSensor2979 = x3d.TouchSensor()
TouchSensor2979.DEF = "Yaw_Touch"
TouchSensor2979.description = "touch to select"

Transform2978.children.append(TouchSensor2979)
Shape2980 = x3d.Shape()
Shape2980.DEF = "YawText"
Appearance2981 = x3d.Appearance()
Material2982 = x3d.Material()
Material2982.USE = "text_color"

Appearance2981.material = Material2982

Shape2980.appearance = Appearance2981
Text2983 = x3d.Text()
Text2983.string = ["Yaw"]

Shape2980.geometry = Text2983

Transform2978.children.append(Shape2980)
Shape2984 = x3d.Shape()
Shape2984.DEF = "Yaw_Back"
Appearance2985 = x3d.Appearance()
Material2986 = x3d.Material()
Material2986.USE = "Clear"

Appearance2985.material = Material2986

Shape2984.appearance = Appearance2985
IndexedFaceSet2987 = x3d.IndexedFaceSet()
IndexedFaceSet2987.USE = "Backing"

Shape2984.geometry = IndexedFaceSet2987

Transform2978.children.append(Shape2984)

Transform2956.children.append(Transform2978)
Transform2988 = x3d.Transform()
Transform2988.DEF = "RollTransform"
Transform2988.translation = [9,-1,0]
TouchSensor2989 = x3d.TouchSensor()
TouchSensor2989.DEF = "Roll_Touch"
TouchSensor2989.description = "touch to select"

Transform2988.children.append(TouchSensor2989)
Shape2990 = x3d.Shape()
Shape2990.DEF = "_RollInterpolator"
Appearance2991 = x3d.Appearance()
Material2992 = x3d.Material()
Material2992.USE = "text_color"

Appearance2991.material = Material2992

Shape2990.appearance = Appearance2991
Text2993 = x3d.Text()
Text2993.string = ["Roll"]

Shape2990.geometry = Text2993

Transform2988.children.append(Shape2990)
Shape2994 = x3d.Shape()
Shape2994.DEF = "Roll_Back"
Appearance2995 = x3d.Appearance()
Material2996 = x3d.Material()
Material2996.USE = "Clear"

Appearance2995.material = Material2996

Shape2994.appearance = Appearance2995
IndexedFaceSet2997 = x3d.IndexedFaceSet()
IndexedFaceSet2997.USE = "Backing"

Shape2994.geometry = IndexedFaceSet2997

Transform2988.children.append(Shape2994)

Transform2956.children.append(Transform2988)
Transform2998 = x3d.Transform()
Transform2998.DEF = "WalkTransform"
Transform2998.translation = [12,-1,0]
TouchSensor2999 = x3d.TouchSensor()
TouchSensor2999.DEF = "Walk_Touch"
TouchSensor2999.description = "touch to select"

Transform2998.children.append(TouchSensor2999)
Shape3000 = x3d.Shape()
Shape3000.DEF = "WalkText"
Appearance3001 = x3d.Appearance()
Material3002 = x3d.Material()
Material3002.USE = "text_color"

Appearance3001.material = Material3002

Shape3000.appearance = Appearance3001
Text3003 = x3d.Text()
Text3003.string = ["Walk"]

Shape3000.geometry = Text3003

Transform2998.children.append(Shape3000)
Shape3004 = x3d.Shape()
Shape3004.DEF = "Walk_Back"
Appearance3005 = x3d.Appearance()
Material3006 = x3d.Material()
Material3006.USE = "Clear"

Appearance3005.material = Material3006

Shape3004.appearance = Appearance3005
IndexedFaceSet3007 = x3d.IndexedFaceSet()
IndexedFaceSet3007.USE = "Backing"

Shape3004.geometry = IndexedFaceSet3007

Transform2998.children.append(Shape3004)

Transform2956.children.append(Transform2998)
Transform3008 = x3d.Transform()
Transform3008.DEF = "RunTransform"
Transform3008.translation = [15,-1,0]
TouchSensor3009 = x3d.TouchSensor()
TouchSensor3009.DEF = "Run_Touch"
TouchSensor3009.description = "touch to select"

Transform3008.children.append(TouchSensor3009)
Shape3010 = x3d.Shape()
Shape3010.DEF = "RunText"
Appearance3011 = x3d.Appearance()
Material3012 = x3d.Material()
Material3012.USE = "text_color"

Appearance3011.material = Material3012

Shape3010.appearance = Appearance3011
Text3013 = x3d.Text()
Text3013.string = ["Run"]

Shape3010.geometry = Text3013

Transform3008.children.append(Shape3010)
Shape3014 = x3d.Shape()
Shape3014.DEF = "Run_Back"
Appearance3015 = x3d.Appearance()
Material3016 = x3d.Material()
Material3016.USE = "Clear"

Appearance3015.material = Material3016

Shape3014.appearance = Appearance3015
IndexedFaceSet3017 = x3d.IndexedFaceSet()
IndexedFaceSet3017.USE = "Backing"

Shape3014.geometry = IndexedFaceSet3017

Transform3008.children.append(Shape3014)

Transform2956.children.append(Transform3008)
Transform3018 = x3d.Transform()
Transform3018.DEF = "JumpTransform"
Transform3018.translation = [18,-1,0]
TouchSensor3019 = x3d.TouchSensor()
TouchSensor3019.DEF = "Jump_Touch"
TouchSensor3019.description = "touch to select"

Transform3018.children.append(TouchSensor3019)
Shape3020 = x3d.Shape()
Shape3020.DEF = "Jump"
Appearance3021 = x3d.Appearance()
Material3022 = x3d.Material()
Material3022.USE = "text_color"

Appearance3021.material = Material3022

Shape3020.appearance = Appearance3021
Text3023 = x3d.Text()
Text3023.string = ["Jump"]

Shape3020.geometry = Text3023

Transform3018.children.append(Shape3020)
Shape3024 = x3d.Shape()
Shape3024.DEF = "Jump_Back"
Appearance3025 = x3d.Appearance()
Material3026 = x3d.Material()
Material3026.USE = "Clear"

Appearance3025.material = Material3026

Shape3024.appearance = Appearance3025
IndexedFaceSet3027 = x3d.IndexedFaceSet()
IndexedFaceSet3027.USE = "Backing"

Shape3024.geometry = IndexedFaceSet3027

Transform3018.children.append(Shape3024)

Transform2956.children.append(Transform3018)
Transform3028 = x3d.Transform()
Transform3028.DEF = "KickTransform"
Transform3028.translation = [21,-1,0]
TouchSensor3029 = x3d.TouchSensor()
TouchSensor3029.DEF = "Kick_Touch"
TouchSensor3029.description = "touch to select"

Transform3028.children.append(TouchSensor3029)
Shape3030 = x3d.Shape()
Shape3030.DEF = "KickText"
Appearance3031 = x3d.Appearance()
Material3032 = x3d.Material()
Material3032.USE = "text_color"

Appearance3031.material = Material3032

Shape3030.appearance = Appearance3031
Text3033 = x3d.Text()
Text3033.string = ["Kick"]

Shape3030.geometry = Text3033

Transform3028.children.append(Shape3030)
Shape3034 = x3d.Shape()
Shape3034.DEF = "Kick_Back"
Appearance3035 = x3d.Appearance()
Material3036 = x3d.Material()
Material3036.USE = "Clear"

Appearance3035.material = Material3036

Shape3034.appearance = Appearance3035
IndexedFaceSet3037 = x3d.IndexedFaceSet()
IndexedFaceSet3037.USE = "Backing"

Shape3034.geometry = IndexedFaceSet3037

Transform3028.children.append(Shape3034)

Transform2956.children.append(Transform3028)
Transform3038 = x3d.Transform()
Transform3038.DEF = "Stop_Text"
Transform3038.translation = [0,1.4,0]
TouchSensor3039 = x3d.TouchSensor()
TouchSensor3039.DEF = "Stop_Touch"
TouchSensor3039.description = "touch to select"

Transform3038.children.append(TouchSensor3039)
Shape3040 = x3d.Shape()
Shape3040.DEF = "StopText"
Appearance3041 = x3d.Appearance()
Material3042 = x3d.Material()
Material3042.USE = "text_color"

Appearance3041.material = Material3042

Shape3040.appearance = Appearance3041
Text3043 = x3d.Text()
Text3043.string = ["Stop","Default Pose"]

Shape3040.geometry = Text3043

Transform3038.children.append(Shape3040)
Shape3044 = x3d.Shape()
Shape3044.DEF = "Stop_Back"
Appearance3045 = x3d.Appearance()
Material3046 = x3d.Material()
Material3046.USE = "Clear"

Appearance3045.material = Material3046

Shape3044.appearance = Appearance3045
IndexedFaceSet3047 = x3d.IndexedFaceSet()
IndexedFaceSet3047.USE = "Backing"

Shape3044.geometry = IndexedFaceSet3047

Transform3038.children.append(Shape3044)

Transform2956.children.append(Transform3038)

Transform2955.children.append(Transform2956)

Group2929.children.append(Transform2955)
ROUTE3048 = x3d.ROUTE()
ROUTE3048.fromField = "position_changed"
ROUTE3048.fromNode = "HudProximitySensor"
ROUTE3048.toField = "translation"
ROUTE3048.toNode = "HudXform"

Group2929.children.append(ROUTE3048)
ROUTE3049 = x3d.ROUTE()
ROUTE3049.fromField = "orientation_changed"
ROUTE3049.fromNode = "HudProximitySensor"
ROUTE3049.toField = "rotation"
ROUTE3049.toNode = "HudXform"

Group2929.children.append(ROUTE3049)

Scene30.children.append(Group2929)
Group3050 = x3d.Group()
Group3050.DEF = "BehaviorSynchronization"
ROUTE3051 = x3d.ROUTE()
ROUTE3051.fromField = "touchTime"
ROUTE3051.fromNode = "Stand_Touch"
ROUTE3051.toField = "stopTime"
ROUTE3051.toNode = "PitchTimer"

Group3050.children.append(ROUTE3051)
ROUTE3052 = x3d.ROUTE()
ROUTE3052.fromField = "touchTime"
ROUTE3052.fromNode = "Stand_Touch"
ROUTE3052.toField = "stopTime"
ROUTE3052.toNode = "YawTimer"

Group3050.children.append(ROUTE3052)
ROUTE3053 = x3d.ROUTE()
ROUTE3053.fromField = "touchTime"
ROUTE3053.fromNode = "Stand_Touch"
ROUTE3053.toField = "stopTime"
ROUTE3053.toNode = "RollTimer"

Group3050.children.append(ROUTE3053)
ROUTE3054 = x3d.ROUTE()
ROUTE3054.fromField = "touchTime"
ROUTE3054.fromNode = "Stand_Touch"
ROUTE3054.toField = "stopTime"
ROUTE3054.toNode = "WalkTimer"

Group3050.children.append(ROUTE3054)
ROUTE3055 = x3d.ROUTE()
ROUTE3055.fromField = "touchTime"
ROUTE3055.fromNode = "Stand_Touch"
ROUTE3055.toField = "stopTime"
ROUTE3055.toNode = "RunTimer"

Group3050.children.append(ROUTE3055)
ROUTE3056 = x3d.ROUTE()
ROUTE3056.fromField = "touchTime"
ROUTE3056.fromNode = "Stand_Touch"
ROUTE3056.toField = "stopTime"
ROUTE3056.toNode = "JumpTimer"

Group3050.children.append(ROUTE3056)
ROUTE3057 = x3d.ROUTE()
ROUTE3057.fromField = "touchTime"
ROUTE3057.fromNode = "Stand_Touch"
ROUTE3057.toField = "stopTime"
ROUTE3057.toNode = "KickTimer"

Group3050.children.append(ROUTE3057)
ROUTE3058 = x3d.ROUTE()
ROUTE3058.fromField = "touchTime"
ROUTE3058.fromNode = "Stand_Touch"
ROUTE3058.toField = "stopTime"
ROUTE3058.toNode = "StopTimer"

Group3050.children.append(ROUTE3058)
ROUTE3059 = x3d.ROUTE()
ROUTE3059.fromField = "touchTime"
ROUTE3059.fromNode = "Stand_Touch"
ROUTE3059.toField = "startTime"
ROUTE3059.toNode = "StandTimer"

Group3050.children.append(ROUTE3059)
ROUTE3060 = x3d.ROUTE()
ROUTE3060.fromField = "touchTime"
ROUTE3060.fromNode = "Pitch_Touch"
ROUTE3060.toField = "stopTime"
ROUTE3060.toNode = "StandTimer"

Group3050.children.append(ROUTE3060)
ROUTE3061 = x3d.ROUTE()
ROUTE3061.fromField = "touchTime"
ROUTE3061.fromNode = "Pitch_Touch"
ROUTE3061.toField = "stopTime"
ROUTE3061.toNode = "YawTimer"

Group3050.children.append(ROUTE3061)
ROUTE3062 = x3d.ROUTE()
ROUTE3062.fromField = "touchTime"
ROUTE3062.fromNode = "Pitch_Touch"
ROUTE3062.toField = "stopTime"
ROUTE3062.toNode = "RollTimer"

Group3050.children.append(ROUTE3062)
ROUTE3063 = x3d.ROUTE()
ROUTE3063.fromField = "touchTime"
ROUTE3063.fromNode = "Pitch_Touch"
ROUTE3063.toField = "stopTime"
ROUTE3063.toNode = "WalkTimer"

Group3050.children.append(ROUTE3063)
ROUTE3064 = x3d.ROUTE()
ROUTE3064.fromField = "touchTime"
ROUTE3064.fromNode = "Pitch_Touch"
ROUTE3064.toField = "stopTime"
ROUTE3064.toNode = "RunTimer"

Group3050.children.append(ROUTE3064)
ROUTE3065 = x3d.ROUTE()
ROUTE3065.fromField = "touchTime"
ROUTE3065.fromNode = "Pitch_Touch"
ROUTE3065.toField = "stopTime"
ROUTE3065.toNode = "JumpTimer"

Group3050.children.append(ROUTE3065)
ROUTE3066 = x3d.ROUTE()
ROUTE3066.fromField = "touchTime"
ROUTE3066.fromNode = "Pitch_Touch"
ROUTE3066.toField = "stopTime"
ROUTE3066.toNode = "KickTimer"

Group3050.children.append(ROUTE3066)
ROUTE3067 = x3d.ROUTE()
ROUTE3067.fromField = "touchTime"
ROUTE3067.fromNode = "Pitch_Touch"
ROUTE3067.toField = "stopTime"
ROUTE3067.toNode = "StopTimer"

Group3050.children.append(ROUTE3067)
ROUTE3068 = x3d.ROUTE()
ROUTE3068.fromField = "touchTime"
ROUTE3068.fromNode = "Pitch_Touch"
ROUTE3068.toField = "startTime"
ROUTE3068.toNode = "PitchTimer"

Group3050.children.append(ROUTE3068)
ROUTE3069 = x3d.ROUTE()
ROUTE3069.fromField = "touchTime"
ROUTE3069.fromNode = "Yaw_Touch"
ROUTE3069.toField = "stopTime"
ROUTE3069.toNode = "StandTimer"

Group3050.children.append(ROUTE3069)
ROUTE3070 = x3d.ROUTE()
ROUTE3070.fromField = "touchTime"
ROUTE3070.fromNode = "Yaw_Touch"
ROUTE3070.toField = "stopTime"
ROUTE3070.toNode = "PitchTimer"

Group3050.children.append(ROUTE3070)
ROUTE3071 = x3d.ROUTE()
ROUTE3071.fromField = "touchTime"
ROUTE3071.fromNode = "Yaw_Touch"
ROUTE3071.toField = "stopTime"
ROUTE3071.toNode = "RollTimer"

Group3050.children.append(ROUTE3071)
ROUTE3072 = x3d.ROUTE()
ROUTE3072.fromField = "touchTime"
ROUTE3072.fromNode = "Yaw_Touch"
ROUTE3072.toField = "stopTime"
ROUTE3072.toNode = "WalkTimer"

Group3050.children.append(ROUTE3072)
ROUTE3073 = x3d.ROUTE()
ROUTE3073.fromField = "touchTime"
ROUTE3073.fromNode = "Yaw_Touch"
ROUTE3073.toField = "stopTime"
ROUTE3073.toNode = "RunTimer"

Group3050.children.append(ROUTE3073)
ROUTE3074 = x3d.ROUTE()
ROUTE3074.fromField = "touchTime"
ROUTE3074.fromNode = "Yaw_Touch"
ROUTE3074.toField = "stopTime"
ROUTE3074.toNode = "JumpTimer"

Group3050.children.append(ROUTE3074)
ROUTE3075 = x3d.ROUTE()
ROUTE3075.fromField = "touchTime"
ROUTE3075.fromNode = "Yaw_Touch"
ROUTE3075.toField = "stopTime"
ROUTE3075.toNode = "KickTimer"

Group3050.children.append(ROUTE3075)
ROUTE3076 = x3d.ROUTE()
ROUTE3076.fromField = "touchTime"
ROUTE3076.fromNode = "Yaw_Touch"
ROUTE3076.toField = "stopTime"
ROUTE3076.toNode = "StopTimer"

Group3050.children.append(ROUTE3076)
ROUTE3077 = x3d.ROUTE()
ROUTE3077.fromField = "touchTime"
ROUTE3077.fromNode = "Yaw_Touch"
ROUTE3077.toField = "startTime"
ROUTE3077.toNode = "YawTimer"

Group3050.children.append(ROUTE3077)
ROUTE3078 = x3d.ROUTE()
ROUTE3078.fromField = "touchTime"
ROUTE3078.fromNode = "Walk_Touch"
ROUTE3078.toField = "stopTime"
ROUTE3078.toNode = "StandTimer"

Group3050.children.append(ROUTE3078)
ROUTE3079 = x3d.ROUTE()
ROUTE3079.fromField = "touchTime"
ROUTE3079.fromNode = "Walk_Touch"
ROUTE3079.toField = "stopTime"
ROUTE3079.toNode = "PitchTimer"

Group3050.children.append(ROUTE3079)
ROUTE3080 = x3d.ROUTE()
ROUTE3080.fromField = "touchTime"
ROUTE3080.fromNode = "Walk_Touch"
ROUTE3080.toField = "stopTime"
ROUTE3080.toNode = "YawTimer"

Group3050.children.append(ROUTE3080)
ROUTE3081 = x3d.ROUTE()
ROUTE3081.fromField = "touchTime"
ROUTE3081.fromNode = "Walk_Touch"
ROUTE3081.toField = "stopTime"
ROUTE3081.toNode = "RollTimer"

Group3050.children.append(ROUTE3081)
ROUTE3082 = x3d.ROUTE()
ROUTE3082.fromField = "touchTime"
ROUTE3082.fromNode = "Walk_Touch"
ROUTE3082.toField = "stopTime"
ROUTE3082.toNode = "RunTimer"

Group3050.children.append(ROUTE3082)
ROUTE3083 = x3d.ROUTE()
ROUTE3083.fromField = "touchTime"
ROUTE3083.fromNode = "Walk_Touch"
ROUTE3083.toField = "stopTime"
ROUTE3083.toNode = "JumpTimer"

Group3050.children.append(ROUTE3083)
ROUTE3084 = x3d.ROUTE()
ROUTE3084.fromField = "touchTime"
ROUTE3084.fromNode = "Walk_Touch"
ROUTE3084.toField = "stopTime"
ROUTE3084.toNode = "KickTimer"

Group3050.children.append(ROUTE3084)
ROUTE3085 = x3d.ROUTE()
ROUTE3085.fromField = "touchTime"
ROUTE3085.fromNode = "Walk_Touch"
ROUTE3085.toField = "stopTime"
ROUTE3085.toNode = "StopTimer"

Group3050.children.append(ROUTE3085)
ROUTE3086 = x3d.ROUTE()
ROUTE3086.fromField = "touchTime"
ROUTE3086.fromNode = "Walk_Touch"
ROUTE3086.toField = "startTime"
ROUTE3086.toNode = "WalkTimer"

Group3050.children.append(ROUTE3086)
ROUTE3087 = x3d.ROUTE()
ROUTE3087.fromField = "touchTime"
ROUTE3087.fromNode = "Roll_Touch"
ROUTE3087.toField = "stopTime"
ROUTE3087.toNode = "StandTimer"

Group3050.children.append(ROUTE3087)
ROUTE3088 = x3d.ROUTE()
ROUTE3088.fromField = "touchTime"
ROUTE3088.fromNode = "Roll_Touch"
ROUTE3088.toField = "stopTime"
ROUTE3088.toNode = "PitchTimer"

Group3050.children.append(ROUTE3088)
ROUTE3089 = x3d.ROUTE()
ROUTE3089.fromField = "touchTime"
ROUTE3089.fromNode = "Roll_Touch"
ROUTE3089.toField = "stopTime"
ROUTE3089.toNode = "YawTimer"

Group3050.children.append(ROUTE3089)
ROUTE3090 = x3d.ROUTE()
ROUTE3090.fromField = "touchTime"
ROUTE3090.fromNode = "Roll_Touch"
ROUTE3090.toField = "stopTime"
ROUTE3090.toNode = "WalkTimer"

Group3050.children.append(ROUTE3090)
ROUTE3091 = x3d.ROUTE()
ROUTE3091.fromField = "touchTime"
ROUTE3091.fromNode = "Roll_Touch"
ROUTE3091.toField = "stopTime"
ROUTE3091.toNode = "RunTimer"

Group3050.children.append(ROUTE3091)
ROUTE3092 = x3d.ROUTE()
ROUTE3092.fromField = "touchTime"
ROUTE3092.fromNode = "Roll_Touch"
ROUTE3092.toField = "stopTime"
ROUTE3092.toNode = "JumpTimer"

Group3050.children.append(ROUTE3092)
ROUTE3093 = x3d.ROUTE()
ROUTE3093.fromField = "touchTime"
ROUTE3093.fromNode = "Roll_Touch"
ROUTE3093.toField = "stopTime"
ROUTE3093.toNode = "KickTimer"

Group3050.children.append(ROUTE3093)
ROUTE3094 = x3d.ROUTE()
ROUTE3094.fromField = "touchTime"
ROUTE3094.fromNode = "Roll_Touch"
ROUTE3094.toField = "stopTime"
ROUTE3094.toNode = "StopTimer"

Group3050.children.append(ROUTE3094)
ROUTE3095 = x3d.ROUTE()
ROUTE3095.fromField = "touchTime"
ROUTE3095.fromNode = "Roll_Touch"
ROUTE3095.toField = "startTime"
ROUTE3095.toNode = "RollTimer"

Group3050.children.append(ROUTE3095)
ROUTE3096 = x3d.ROUTE()
ROUTE3096.fromField = "touchTime"
ROUTE3096.fromNode = "Run_Touch"
ROUTE3096.toField = "stopTime"
ROUTE3096.toNode = "StandTimer"

Group3050.children.append(ROUTE3096)
ROUTE3097 = x3d.ROUTE()
ROUTE3097.fromField = "touchTime"
ROUTE3097.fromNode = "Run_Touch"
ROUTE3097.toField = "stopTime"
ROUTE3097.toNode = "PitchTimer"

Group3050.children.append(ROUTE3097)
ROUTE3098 = x3d.ROUTE()
ROUTE3098.fromField = "touchTime"
ROUTE3098.fromNode = "Run_Touch"
ROUTE3098.toField = "stopTime"
ROUTE3098.toNode = "YawTimer"

Group3050.children.append(ROUTE3098)
ROUTE3099 = x3d.ROUTE()
ROUTE3099.fromField = "touchTime"
ROUTE3099.fromNode = "Run_Touch"
ROUTE3099.toField = "stopTime"
ROUTE3099.toNode = "RollTimer"

Group3050.children.append(ROUTE3099)
ROUTE3100 = x3d.ROUTE()
ROUTE3100.fromField = "touchTime"
ROUTE3100.fromNode = "Run_Touch"
ROUTE3100.toField = "stopTime"
ROUTE3100.toNode = "WalkTimer"

Group3050.children.append(ROUTE3100)
ROUTE3101 = x3d.ROUTE()
ROUTE3101.fromField = "touchTime"
ROUTE3101.fromNode = "Run_Touch"
ROUTE3101.toField = "stopTime"
ROUTE3101.toNode = "JumpTimer"

Group3050.children.append(ROUTE3101)
ROUTE3102 = x3d.ROUTE()
ROUTE3102.fromField = "touchTime"
ROUTE3102.fromNode = "Run_Touch"
ROUTE3102.toField = "stopTime"
ROUTE3102.toNode = "KickTimer"

Group3050.children.append(ROUTE3102)
ROUTE3103 = x3d.ROUTE()
ROUTE3103.fromField = "touchTime"
ROUTE3103.fromNode = "Run_Touch"
ROUTE3103.toField = "stopTime"
ROUTE3103.toNode = "StopTimer"

Group3050.children.append(ROUTE3103)
ROUTE3104 = x3d.ROUTE()
ROUTE3104.fromField = "touchTime"
ROUTE3104.fromNode = "Run_Touch"
ROUTE3104.toField = "startTime"
ROUTE3104.toNode = "RunTimer"

Group3050.children.append(ROUTE3104)
ROUTE3105 = x3d.ROUTE()
ROUTE3105.fromField = "touchTime"
ROUTE3105.fromNode = "Jump_Touch"
ROUTE3105.toField = "stopTime"
ROUTE3105.toNode = "StandTimer"

Group3050.children.append(ROUTE3105)
ROUTE3106 = x3d.ROUTE()
ROUTE3106.fromField = "touchTime"
ROUTE3106.fromNode = "Jump_Touch"
ROUTE3106.toField = "stopTime"
ROUTE3106.toNode = "PitchTimer"

Group3050.children.append(ROUTE3106)
ROUTE3107 = x3d.ROUTE()
ROUTE3107.fromField = "touchTime"
ROUTE3107.fromNode = "Jump_Touch"
ROUTE3107.toField = "stopTime"
ROUTE3107.toNode = "YawTimer"

Group3050.children.append(ROUTE3107)
ROUTE3108 = x3d.ROUTE()
ROUTE3108.fromField = "touchTime"
ROUTE3108.fromNode = "Jump_Touch"
ROUTE3108.toField = "stopTime"
ROUTE3108.toNode = "RollTimer"

Group3050.children.append(ROUTE3108)
ROUTE3109 = x3d.ROUTE()
ROUTE3109.fromField = "touchTime"
ROUTE3109.fromNode = "Jump_Touch"
ROUTE3109.toField = "stopTime"
ROUTE3109.toNode = "WalkTimer"

Group3050.children.append(ROUTE3109)
ROUTE3110 = x3d.ROUTE()
ROUTE3110.fromField = "touchTime"
ROUTE3110.fromNode = "Jump_Touch"
ROUTE3110.toField = "stopTime"
ROUTE3110.toNode = "RunTimer"

Group3050.children.append(ROUTE3110)
ROUTE3111 = x3d.ROUTE()
ROUTE3111.fromField = "touchTime"
ROUTE3111.fromNode = "Jump_Touch"
ROUTE3111.toField = "stopTime"
ROUTE3111.toNode = "KickTimer"

Group3050.children.append(ROUTE3111)
ROUTE3112 = x3d.ROUTE()
ROUTE3112.fromField = "touchTime"
ROUTE3112.fromNode = "Jump_Touch"
ROUTE3112.toField = "stopTime"
ROUTE3112.toNode = "StopTimer"

Group3050.children.append(ROUTE3112)
ROUTE3113 = x3d.ROUTE()
ROUTE3113.fromField = "touchTime"
ROUTE3113.fromNode = "Jump_Touch"
ROUTE3113.toField = "startTime"
ROUTE3113.toNode = "JumpTimer"

Group3050.children.append(ROUTE3113)
ROUTE3114 = x3d.ROUTE()
ROUTE3114.fromField = "touchTime"
ROUTE3114.fromNode = "Kick_Touch"
ROUTE3114.toField = "stopTime"
ROUTE3114.toNode = "StandTimer"

Group3050.children.append(ROUTE3114)
ROUTE3115 = x3d.ROUTE()
ROUTE3115.fromField = "touchTime"
ROUTE3115.fromNode = "Kick_Touch"
ROUTE3115.toField = "stopTime"
ROUTE3115.toNode = "PitchTimer"

Group3050.children.append(ROUTE3115)
ROUTE3116 = x3d.ROUTE()
ROUTE3116.fromField = "touchTime"
ROUTE3116.fromNode = "Kick_Touch"
ROUTE3116.toField = "stopTime"
ROUTE3116.toNode = "YawTimer"

Group3050.children.append(ROUTE3116)
ROUTE3117 = x3d.ROUTE()
ROUTE3117.fromField = "touchTime"
ROUTE3117.fromNode = "Kick_Touch"
ROUTE3117.toField = "stopTime"
ROUTE3117.toNode = "RollTimer"

Group3050.children.append(ROUTE3117)
ROUTE3118 = x3d.ROUTE()
ROUTE3118.fromField = "touchTime"
ROUTE3118.fromNode = "Kick_Touch"
ROUTE3118.toField = "stopTime"
ROUTE3118.toNode = "WalkTimer"

Group3050.children.append(ROUTE3118)
ROUTE3119 = x3d.ROUTE()
ROUTE3119.fromField = "touchTime"
ROUTE3119.fromNode = "Kick_Touch"
ROUTE3119.toField = "stopTime"
ROUTE3119.toNode = "RunTimer"

Group3050.children.append(ROUTE3119)
ROUTE3120 = x3d.ROUTE()
ROUTE3120.fromField = "touchTime"
ROUTE3120.fromNode = "Kick_Touch"
ROUTE3120.toField = "stopTime"
ROUTE3120.toNode = "JumpTimer"

Group3050.children.append(ROUTE3120)
ROUTE3121 = x3d.ROUTE()
ROUTE3121.fromField = "touchTime"
ROUTE3121.fromNode = "Kick_Touch"
ROUTE3121.toField = "stopTime"
ROUTE3121.toNode = "StopTimer"

Group3050.children.append(ROUTE3121)
ROUTE3122 = x3d.ROUTE()
ROUTE3122.fromField = "touchTime"
ROUTE3122.fromNode = "Kick_Touch"
ROUTE3122.toField = "startTime"
ROUTE3122.toNode = "KickTimer"

Group3050.children.append(ROUTE3122)
ROUTE3123 = x3d.ROUTE()
ROUTE3123.fromField = "touchTime"
ROUTE3123.fromNode = "Stop_Touch"
ROUTE3123.toField = "stopTime"
ROUTE3123.toNode = "StandTimer"

Group3050.children.append(ROUTE3123)
ROUTE3124 = x3d.ROUTE()
ROUTE3124.fromField = "touchTime"
ROUTE3124.fromNode = "Stop_Touch"
ROUTE3124.toField = "stopTime"
ROUTE3124.toNode = "PitchTimer"

Group3050.children.append(ROUTE3124)
ROUTE3125 = x3d.ROUTE()
ROUTE3125.fromField = "touchTime"
ROUTE3125.fromNode = "Stop_Touch"
ROUTE3125.toField = "stopTime"
ROUTE3125.toNode = "YawTimer"

Group3050.children.append(ROUTE3125)
ROUTE3126 = x3d.ROUTE()
ROUTE3126.fromField = "touchTime"
ROUTE3126.fromNode = "Stop_Touch"
ROUTE3126.toField = "stopTime"
ROUTE3126.toNode = "RollTimer"

Group3050.children.append(ROUTE3126)
ROUTE3127 = x3d.ROUTE()
ROUTE3127.fromField = "touchTime"
ROUTE3127.fromNode = "Stop_Touch"
ROUTE3127.toField = "stopTime"
ROUTE3127.toNode = "WalkTimer"

Group3050.children.append(ROUTE3127)
ROUTE3128 = x3d.ROUTE()
ROUTE3128.fromField = "touchTime"
ROUTE3128.fromNode = "Stop_Touch"
ROUTE3128.toField = "stopTime"
ROUTE3128.toNode = "RunTimer"

Group3050.children.append(ROUTE3128)
ROUTE3129 = x3d.ROUTE()
ROUTE3129.fromField = "touchTime"
ROUTE3129.fromNode = "Stop_Touch"
ROUTE3129.toField = "stopTime"
ROUTE3129.toNode = "JumpTimer"

Group3050.children.append(ROUTE3129)
ROUTE3130 = x3d.ROUTE()
ROUTE3130.fromField = "touchTime"
ROUTE3130.fromNode = "Stop_Touch"
ROUTE3130.toField = "stopTime"
ROUTE3130.toNode = "KickTimer"

Group3050.children.append(ROUTE3130)
ROUTE3131 = x3d.ROUTE()
ROUTE3131.fromField = "touchTime"
ROUTE3131.fromNode = "Stop_Touch"
ROUTE3131.toField = "startTime"
ROUTE3131.toNode = "StopTimer"

Group3050.children.append(ROUTE3131)

Scene30.children.append(Group3050)

X3D0.Scene = Scene30
f = open("././HAnim1SpecificationLOA3Animation_RoundTrip.x3d", "w")
f.write(X3D0.XML())
f.close()
