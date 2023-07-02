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
meta3.content = "HAnim1SpecificationLOA3Illustrated.x3d"

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.name = "description"
meta4.content = "HAnim Specification reference example providing full coverage and visibility of all specified HAnim constructs, also suitable for re-use as an authoring template. Geometry visualizations are derived from HAnim1SpecificationLOA3Invisible.x3d visualization report. Resusable exemplar animations also added via heads-up display (HUD) interface to confirm proper parent-child relationships."

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
meta8.name = "creator"
meta8.content = "Matthew T. Beitler, Joe D. Williams, Don Brutzman"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "Image"
meta9.content = "HAnim1SpecificationLOA3Illustrated.png"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "Image"
meta10.content = "HAnim1SpecificationLOA3IllustratedLeftSide.png"

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.name = "reference"
meta11.content = "HAnim1SpecificationLOA3Invisible.x3d"

head1.children.append(meta11)
meta12 = x3d.meta()
meta12.name = "reference"
meta12.content = "HAnim1SpecificationLOA3Animation.x3d"

head1.children.append(meta12)
meta13 = x3d.meta()
meta13.name = "reference"
meta13.content = "HAnimSpecificationExampleChangeLog.txt"

head1.children.append(meta13)
meta14 = x3d.meta()
meta14.name = "Image"
meta14.content = "images/BonesAllSkeletonFrontViewLOA1.png"

head1.children.append(meta14)
meta15 = x3d.meta()
meta15.name = "Image"
meta15.content = "images/BonesAllSkeletonFrontViewLOA2.png"

head1.children.append(meta15)
meta16 = x3d.meta()
meta16.name = "Image"
meta16.content = "images/BonesAllSkeletonFrontViewLOA3.png"

head1.children.append(meta16)
meta17 = x3d.meta()
meta17.name = "TODO"
meta17.content = "move relevant HAnimSite/Viewpoint pairs into skeleton at appropriate locations"

head1.children.append(meta17)
meta18 = x3d.meta()
meta18.name = "warning"
meta18.content = "BS Contact and H3DViewer have polygon-culling problems at close range (possibly related to avatarSize), other players look OK"

head1.children.append(meta18)
meta19 = x3d.meta()
meta19.name = "TODO"
meta19.content = "insert MetadataInteger nodes indicating LOA for each Joint and Segment"

head1.children.append(meta19)
meta20 = x3d.meta()
meta20.name = "reference"
meta20.content = "Norman Badler et al., ANTHROPOMETRY FOR COMPUTER GRAPHICS HUMAN FIGURES, University of Pennsylvania, 1989."

head1.children.append(meta20)
meta21 = x3d.meta()
meta21.name = "reference"
meta21.content = "http://www.cis.upenn.edu/~badler/anthro/89-71.ps"

head1.children.append(meta21)
meta22 = x3d.meta()
meta22.name = "reference"
meta22.content = "tables/AnthropometryForComputerGraphicsHumanFigures89-71.pdf"

head1.children.append(meta22)
meta23 = x3d.meta()
meta23.name = "translator"
meta23.content = "Don Brutzman and Joe Williams"

head1.children.append(meta23)
meta24 = x3d.meta()
meta24.name = "generator"
meta24.content = "BS Contact Geo 8.001, http://www.bitmanagement.de/en/products/interactive-3d-clients/bs-contact-geo"

head1.children.append(meta24)
meta25 = x3d.meta()
meta25.name = "reference"
meta25.content = "originals/LOA3ExampleSourceWithDiamondsOriginal.wrl"

head1.children.append(meta25)
meta26 = x3d.meta()
meta26.name = "reference"
meta26.content = "originals/LOA3ExampleSourceWithDiamondsOriginal.x3d"

head1.children.append(meta26)
meta27 = x3d.meta()
meta27.name = "reference"
meta27.content = "originals/LOA3ExampleSourceWithDiamondsOriginalBsContactExport.x3d"

head1.children.append(meta27)
meta28 = x3d.meta()
meta28.name = "reference"
meta28.content = "HAnim Specification Table 4.4 - Face Joint object names, https://www.web3d.org/files/specifications/19774/V1.0/HAnim/concepts.html#FaceJointObjectNames"

head1.children.append(meta28)
meta29 = x3d.meta()
meta29.name = "generator"
meta29.content = "X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"

head1.children.append(meta29)
meta30 = x3d.meta()
meta30.name = "identifier"
meta30.content = "https://www.web3d.org/x3d/content/examples/HumanoidAnimation/Legacy/HAnim1SpecificationLOA3Illustrated.x3d"

head1.children.append(meta30)
meta31 = x3d.meta()
meta31.name = "license"
meta31.content = "../license.html"

head1.children.append(meta31)

X3D0.head = head1
Scene32 = x3d.Scene()
Background33 = x3d.Background()

Scene32.children.append(Background33)
NavigationInfo34 = x3d.NavigationInfo()

Scene32.children.append(NavigationInfo34)
Group35 = x3d.Group()
Group35.DEF = "Original_WorldInfo"
WorldInfo36 = x3d.WorldInfo()
WorldInfo36.info = [" HANIM 200x Default Joint Centers, Level-Of-Articulation 3 HANIM 200x (VRML97) Author name: eMpTy (a.k.a. Matthew T. Beitler) HANIM 200x (VRML97) Author email: beitler@cis.upenn.edu or beitler@acm.org HANIM 200x (VRML97) Author homepage: http://www.cis.upenn.edu/~beitler HANIM 200x (VRML97) Compliance Date: August 12, 2003 HANIM 200x Compliance Information: http://HAnim.org/Specifications/HAnim200x Construction Info (joint centers): The joint centers of this figure are based on the work of Norman Badler, director of the Center for Human Modeling and Simulation at the University of Pennsylvania. The original document which these joint centers are based on can be found at: http://www.cis.upenn.edu/~badler/anthro/89-71.ps "]
WorldInfo36.title = "HANIM 200x Default Joint Centers, LOA3"

Group35.children.append(WorldInfo36)

Scene32.children.append(Group35)
#TODO move viewpoints to be internal to HAnimHumanoid
#Viewpoint centerOfRotation=\"0 0.9149 0.0016\" matches initial at-rest locaton of the sacroliac. Note that these viewpoints are external to the HAnimHumanoid and do not move with the human.
Viewpoint37 = x3d.Viewpoint()
Viewpoint37.centerOfRotation = [0,0.9149,0.0016]
Viewpoint37.description = "Humanoid LOA 3 Front"
Viewpoint37.position = [0,0.4,4]

Scene32.children.append(Viewpoint37)
Viewpoint38 = x3d.Viewpoint()
Viewpoint38.centerOfRotation = [0,0.9149,0.0016]
Viewpoint38.description = "Humanoid LOA 3 Front Close"
Viewpoint38.position = [0,0.8,2]

Scene32.children.append(Viewpoint38)
Viewpoint39 = x3d.Viewpoint()
Viewpoint39.centerOfRotation = [0,0.9149,0.0016]
Viewpoint39.description = "Humanoid LOA 3 Front Closer"
Viewpoint39.position = [0,1.2,1]

Scene32.children.append(Viewpoint39)
Viewpoint40 = x3d.Viewpoint()
Viewpoint40.centerOfRotation = [0,1.5,0.0016]
Viewpoint40.description = "Humanoid LOA 3 Front Face"
Viewpoint40.position = [0,1.63,1]

Scene32.children.append(Viewpoint40)
Viewpoint41 = x3d.Viewpoint()
Viewpoint41.centerOfRotation = [0,0.9149,0.0016]
Viewpoint41.description = "Humanoid LOA 3 Right Side"
Viewpoint41.orientation = [0,1,0,1.5708]
Viewpoint41.position = [2.6,0.8,0]

Scene32.children.append(Viewpoint41)
Viewpoint42 = x3d.Viewpoint()
Viewpoint42.centerOfRotation = [0,0.9149,0.0016]
Viewpoint42.description = "Humanoid LOA 3 Right Side Close"
Viewpoint42.orientation = [0,1,0,1.2]
Viewpoint42.position = [1,0.8,0.5]

Scene32.children.append(Viewpoint42)
Viewpoint43 = x3d.Viewpoint()
Viewpoint43.centerOfRotation = [0,0.9149,0.0016]
Viewpoint43.description = "Humanoid LOA 3 Left Side Close"
Viewpoint43.orientation = [0,1,0,-1.2]
Viewpoint43.position = [-1,0.8,0.5]

Scene32.children.append(Viewpoint43)
Viewpoint44 = x3d.Viewpoint()
Viewpoint44.centerOfRotation = [0,0.9149,0.0016]
Viewpoint44.description = "Humanoid LOA 3 Left Side"
Viewpoint44.orientation = [0,1,0,-1.5708]
Viewpoint44.position = [-2.6,0.8,0]

Scene32.children.append(Viewpoint44)
Viewpoint45 = x3d.Viewpoint()
Viewpoint45.centerOfRotation = [0,0.9149,0.0016]
Viewpoint45.description = "Humanoid LOA 3 Top"
Viewpoint45.orientation = [1,0,0,-1.5708]
Viewpoint45.position = [0,3.5,0]

Scene32.children.append(Viewpoint45)
HAnimHumanoid46 = x3d.HAnimHumanoid()
HAnimHumanoid46.name = "humanoid"
HAnimHumanoid46.DEF = "hanim_humanoid"
HAnimHumanoid46.info = ["authorName=Matthew T. Beitler Joe D. Williams Don Brutzman","authorEmail=HAnim@web3D.org","copyright=none","creationDate=12 May 1999","usageRestrictions=none","humanoidVersion=2.0","height=1.7504"]
HAnimHumanoid46.version = "2.0"
#Only one root HAnimJoint is expected
#USE nodes go here for access by inverse kinematics (IK) engines and other tools
#Top-level HAnimSite/Viewpoint nodes that move with the human center but are unaffected by body animation
#TODO move relevant HAnimSite/Viewpoint pairs into skeleton at appropriate locations, if so also revert containerField to default
#right between the eyes, stationary position not animating except with body itself
HAnimJoint47 = x3d.HAnimJoint()
HAnimJoint47.name = "humanoid_root"
HAnimJoint47.DEF = "hanim_humanoid_root"
HAnimJoint47.center = [0,0.824,0.0277]
HAnimJoint47.ulimit = [0,0,0]
HAnimJoint47.llimit = [0,0,0]
HAnimSegment48 = x3d.HAnimSegment()
HAnimSegment48.name = "sacrum"
HAnimSegment48.DEF = "hanim_sacrum"
#<HAnimJoint name='humanoid_root'/> visualization sphere is placed within <HAnimSegment name='sacrum'/>
TouchSensor49 = x3d.TouchSensor()
TouchSensor49.description = "HAnimJoint HumanoidRoot, HAnimSegment sacrum"

HAnimSegment48.children.append(TouchSensor49)
Transform50 = x3d.Transform()
Transform50.translation = [0,0.824,0.0277]
Shape51 = x3d.Shape()
Shape51.DEF = "HAnimJointShape"
Sphere52 = x3d.Sphere()
Sphere52.radius = 0.006

Shape51.geometry = Sphere52
Appearance53 = x3d.Appearance()
Appearance53.DEF = "HAnimJointAppearance"
Material54 = x3d.Material()
Material54.diffuseColor = [1,0.5,0]
Material54.transparency = 0.5

Appearance53.material = Material54

Shape51.appearance = Appearance53

Transform50.children.append(Shape51)

HAnimSegment48.children.append(Transform50)
#HAnimSegment visualization line segment from parent <HAnimJoint name='humanoid_root'/> to <HAnimJoint name='sacroiliac'/>
Shape55 = x3d.Shape()
LineSet56 = x3d.LineSet()
LineSet56.vertexCount = [2]
Coordinate57 = x3d.Coordinate()

LineSet56.coord = Coordinate57
ColorRGBA58 = x3d.ColorRGBA()
ColorRGBA58.DEF = "HAnimSegmentLineColorRGBA"

LineSet56.color = ColorRGBA58

Shape55.geometry = LineSet56

HAnimSegment48.children.append(Shape55)
#HAnimSegment visualization line segment from parent <HAnimJoint name='humanoid_root'/> to <HAnimJoint name='vl5'/>
Shape59 = x3d.Shape()
LineSet60 = x3d.LineSet()
LineSet60.vertexCount = [2]
Coordinate61 = x3d.Coordinate()

LineSet60.coord = Coordinate61
ColorRGBA62 = x3d.ColorRGBA()
ColorRGBA62.USE = "HAnimSegmentLineColorRGBA"

LineSet60.color = ColorRGBA62

Shape59.geometry = LineSet60

HAnimSegment48.children.append(Shape59)

HAnimJoint47.children.append(HAnimSegment48)
HAnimJoint63 = x3d.HAnimJoint()
HAnimJoint63.name = "sacroiliac"
HAnimJoint63.DEF = "hanim_sacroiliac"
HAnimJoint63.center = [0,0.9149,0.0016]
HAnimJoint63.ulimit = [0,0,0]
HAnimJoint63.llimit = [0,0,0]
HAnimSegment64 = x3d.HAnimSegment()
HAnimSegment64.name = "pelvis"
HAnimSegment64.DEF = "hanim_pelvis"
#<HAnimJoint name='sacroiliac'/> visualization sphere is placed within <HAnimSegment name='pelvis'/>
TouchSensor65 = x3d.TouchSensor()
TouchSensor65.description = "HAnimJoint sacroiliac, HAnimSegment pelvis"

HAnimSegment64.children.append(TouchSensor65)
Transform66 = x3d.Transform()
Transform66.translation = [0,0.9149,0.0016]
Shape67 = x3d.Shape()
Shape67.USE = "HAnimJointShape"

Transform66.children.append(Shape67)

HAnimSegment64.children.append(Transform66)
#HAnimSegment visualization line segment from parent <HAnimJoint name='sacroiliac'/> to <HAnimJoint name='l_hip'/>
Shape68 = x3d.Shape()
LineSet69 = x3d.LineSet()
LineSet69.vertexCount = [2]
Coordinate70 = x3d.Coordinate()

LineSet69.coord = Coordinate70
ColorRGBA71 = x3d.ColorRGBA()
ColorRGBA71.USE = "HAnimSegmentLineColorRGBA"

LineSet69.color = ColorRGBA71

Shape68.geometry = LineSet69

HAnimSegment64.children.append(Shape68)
#HAnimSegment visualization line segment from parent <HAnimJoint name='sacroiliac'/> to <HAnimJoint name='r_hip'/>
Shape72 = x3d.Shape()
LineSet73 = x3d.LineSet()
LineSet73.vertexCount = [2]
Coordinate74 = x3d.Coordinate()

LineSet73.coord = Coordinate74
ColorRGBA75 = x3d.ColorRGBA()
ColorRGBA75.USE = "HAnimSegmentLineColorRGBA"

LineSet73.color = ColorRGBA75

Shape72.geometry = LineSet73

HAnimSegment64.children.append(Shape72)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='sacroiliac'/> to <HAnimSite name='r_iliocristale'/>
Shape76 = x3d.Shape()
LineSet77 = x3d.LineSet()
LineSet77.vertexCount = [2]
Coordinate78 = x3d.Coordinate()

LineSet77.coord = Coordinate78
ColorRGBA79 = x3d.ColorRGBA()
ColorRGBA79.DEF = "HAnimSiteLineColorRGBA"

LineSet77.color = ColorRGBA79

Shape76.geometry = LineSet77

HAnimSegment64.children.append(Shape76)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='sacroiliac'/> to <HAnimSite name='r_trochanterion'/>
Shape80 = x3d.Shape()
LineSet81 = x3d.LineSet()
LineSet81.vertexCount = [2]
Coordinate82 = x3d.Coordinate()

LineSet81.coord = Coordinate82
ColorRGBA83 = x3d.ColorRGBA()
ColorRGBA83.USE = "HAnimSiteLineColorRGBA"

LineSet81.color = ColorRGBA83

Shape80.geometry = LineSet81

HAnimSegment64.children.append(Shape80)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='sacroiliac'/> to <HAnimSite name='l_iliocristale'/>
Shape84 = x3d.Shape()
LineSet85 = x3d.LineSet()
LineSet85.vertexCount = [2]
Coordinate86 = x3d.Coordinate()

LineSet85.coord = Coordinate86
ColorRGBA87 = x3d.ColorRGBA()
ColorRGBA87.USE = "HAnimSiteLineColorRGBA"

LineSet85.color = ColorRGBA87

Shape84.geometry = LineSet85

HAnimSegment64.children.append(Shape84)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='sacroiliac'/> to <HAnimSite name='l_trochanterion'/>
Shape88 = x3d.Shape()
LineSet89 = x3d.LineSet()
LineSet89.vertexCount = [2]
Coordinate90 = x3d.Coordinate()

LineSet89.coord = Coordinate90
ColorRGBA91 = x3d.ColorRGBA()
ColorRGBA91.USE = "HAnimSiteLineColorRGBA"

LineSet89.color = ColorRGBA91

Shape88.geometry = LineSet89

HAnimSegment64.children.append(Shape88)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='sacroiliac'/> to <HAnimSite name='r_asis'/>
Shape92 = x3d.Shape()
LineSet93 = x3d.LineSet()
LineSet93.vertexCount = [2]
Coordinate94 = x3d.Coordinate()

LineSet93.coord = Coordinate94
ColorRGBA95 = x3d.ColorRGBA()
ColorRGBA95.USE = "HAnimSiteLineColorRGBA"

LineSet93.color = ColorRGBA95

Shape92.geometry = LineSet93

HAnimSegment64.children.append(Shape92)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='sacroiliac'/> to <HAnimSite name='l_asis'/>
Shape96 = x3d.Shape()
LineSet97 = x3d.LineSet()
LineSet97.vertexCount = [2]
Coordinate98 = x3d.Coordinate()

LineSet97.coord = Coordinate98
ColorRGBA99 = x3d.ColorRGBA()
ColorRGBA99.USE = "HAnimSiteLineColorRGBA"

LineSet97.color = ColorRGBA99

Shape96.geometry = LineSet97

HAnimSegment64.children.append(Shape96)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='sacroiliac'/> to <HAnimSite name='r_psis'/>
Shape100 = x3d.Shape()
LineSet101 = x3d.LineSet()
LineSet101.vertexCount = [2]
Coordinate102 = x3d.Coordinate()

LineSet101.coord = Coordinate102
ColorRGBA103 = x3d.ColorRGBA()
ColorRGBA103.USE = "HAnimSiteLineColorRGBA"

LineSet101.color = ColorRGBA103

Shape100.geometry = LineSet101

HAnimSegment64.children.append(Shape100)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='sacroiliac'/> to <HAnimSite name='l_psis'/>
Shape104 = x3d.Shape()
LineSet105 = x3d.LineSet()
LineSet105.vertexCount = [2]
Coordinate106 = x3d.Coordinate()

LineSet105.coord = Coordinate106
ColorRGBA107 = x3d.ColorRGBA()
ColorRGBA107.USE = "HAnimSiteLineColorRGBA"

LineSet105.color = ColorRGBA107

Shape104.geometry = LineSet105

HAnimSegment64.children.append(Shape104)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='sacroiliac'/> to <HAnimSite name='crotch'/>
Shape108 = x3d.Shape()
LineSet109 = x3d.LineSet()
LineSet109.vertexCount = [2]
Coordinate110 = x3d.Coordinate()

LineSet109.coord = Coordinate110
ColorRGBA111 = x3d.ColorRGBA()
ColorRGBA111.USE = "HAnimSiteLineColorRGBA"

LineSet109.color = ColorRGBA111

Shape108.geometry = LineSet109

HAnimSegment64.children.append(Shape108)
HAnimSite112 = x3d.HAnimSite()
HAnimSite112.name = "r_iliocristale_pt"
HAnimSite112.DEF = "hanim_r_iliocristale_pt"
HAnimSite112.translation = [-0.1525,1.0628,0.0035]
#HAnimSite visualization shape
TouchSensor113 = x3d.TouchSensor()
TouchSensor113.description = "HAnimSite r_iliocristale"

HAnimSite112.children.append(TouchSensor113)
Shape114 = x3d.Shape()
Shape114.DEF = "HAnimSiteShape"
IndexedFaceSet115 = x3d.IndexedFaceSet()
IndexedFaceSet115.DEF = "DiamondIFS"
IndexedFaceSet115.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet115.creaseAngle = 0.5
IndexedFaceSet115.solid = False
Coordinate116 = x3d.Coordinate()

IndexedFaceSet115.coord = Coordinate116

Shape114.geometry = IndexedFaceSet115
Appearance117 = x3d.Appearance()
Material118 = x3d.Material()
Material118.diffuseColor = [1,0,0]

Appearance117.material = Material118

Shape114.appearance = Appearance117

HAnimSite112.children.append(Shape114)

HAnimSegment64.children.append(HAnimSite112)
HAnimSite119 = x3d.HAnimSite()
HAnimSite119.name = "r_trochanterion_pt"
HAnimSite119.DEF = "hanim_r_trochanterion_pt"
HAnimSite119.translation = [-0.1689,0.8419,0.0352]
#HAnimSite visualization shape
TouchSensor120 = x3d.TouchSensor()
TouchSensor120.description = "HAnimSite r_trochanterion"

HAnimSite119.children.append(TouchSensor120)
Shape121 = x3d.Shape()
Shape121.USE = "HAnimSiteShape"

HAnimSite119.children.append(Shape121)

HAnimSegment64.children.append(HAnimSite119)
HAnimSite122 = x3d.HAnimSite()
HAnimSite122.name = "l_iliocristale_pt"
HAnimSite122.DEF = "hanim_l_iliocristale_pt"
HAnimSite122.translation = [0.1612,1.0537,0.0008]
#HAnimSite visualization shape
TouchSensor123 = x3d.TouchSensor()
TouchSensor123.description = "HAnimSite l_iliocristale"

HAnimSite122.children.append(TouchSensor123)
Shape124 = x3d.Shape()
Shape124.USE = "HAnimSiteShape"

HAnimSite122.children.append(Shape124)

HAnimSegment64.children.append(HAnimSite122)
HAnimSite125 = x3d.HAnimSite()
HAnimSite125.name = "l_trochanterion_pt"
HAnimSite125.DEF = "hanim_l_trochanterion_pt"
HAnimSite125.translation = [0.1677,0.8336,0.0303]
#HAnimSite visualization shape
TouchSensor126 = x3d.TouchSensor()
TouchSensor126.description = "HAnimSite l_trochanterion"

HAnimSite125.children.append(TouchSensor126)
Shape127 = x3d.Shape()
Shape127.USE = "HAnimSiteShape"

HAnimSite125.children.append(Shape127)

HAnimSegment64.children.append(HAnimSite125)
HAnimSite128 = x3d.HAnimSite()
HAnimSite128.name = "r_asis_pt"
HAnimSite128.DEF = "hanim_r_asis_pt"
HAnimSite128.translation = [-0.0887,1.0021,0.1112]
#HAnimSite visualization shape
TouchSensor129 = x3d.TouchSensor()
TouchSensor129.description = "HAnimSite r_asis"

HAnimSite128.children.append(TouchSensor129)
Shape130 = x3d.Shape()
Shape130.USE = "HAnimSiteShape"

HAnimSite128.children.append(Shape130)

HAnimSegment64.children.append(HAnimSite128)
HAnimSite131 = x3d.HAnimSite()
HAnimSite131.name = "l_asis_pt"
HAnimSite131.DEF = "hanim_l_asis_pt"
HAnimSite131.translation = [0.0925,0.9983,0.1052]
#HAnimSite visualization shape
TouchSensor132 = x3d.TouchSensor()
TouchSensor132.description = "HAnimSite l_asis"

HAnimSite131.children.append(TouchSensor132)
Shape133 = x3d.Shape()
Shape133.USE = "HAnimSiteShape"

HAnimSite131.children.append(Shape133)

HAnimSegment64.children.append(HAnimSite131)
HAnimSite134 = x3d.HAnimSite()
HAnimSite134.name = "r_psis_pt"
HAnimSite134.DEF = "hanim_r_psis_pt"
HAnimSite134.translation = [-0.0716,1.019,-0.1138]
#HAnimSite visualization shape
TouchSensor135 = x3d.TouchSensor()
TouchSensor135.description = "HAnimSite r_psis"

HAnimSite134.children.append(TouchSensor135)
Shape136 = x3d.Shape()
Shape136.USE = "HAnimSiteShape"

HAnimSite134.children.append(Shape136)

HAnimSegment64.children.append(HAnimSite134)
HAnimSite137 = x3d.HAnimSite()
HAnimSite137.name = "l_psis_pt"
HAnimSite137.DEF = "hanim_l_psis_pt"
HAnimSite137.translation = [0.0774,1.019,-0.1151]
#HAnimSite visualization shape
TouchSensor138 = x3d.TouchSensor()
TouchSensor138.description = "HAnimSite l_psis"

HAnimSite137.children.append(TouchSensor138)
Shape139 = x3d.Shape()
Shape139.USE = "HAnimSiteShape"

HAnimSite137.children.append(Shape139)

HAnimSegment64.children.append(HAnimSite137)
HAnimSite140 = x3d.HAnimSite()
HAnimSite140.name = "crotch_pt"
HAnimSite140.DEF = "hanim_crotch_pt"
HAnimSite140.translation = [0.0034,0.8266,0.0257]
#HAnimSite visualization shape
TouchSensor141 = x3d.TouchSensor()
TouchSensor141.description = "HAnimSite crotch"

HAnimSite140.children.append(TouchSensor141)
Shape142 = x3d.Shape()
Shape142.USE = "HAnimSiteShape"

HAnimSite140.children.append(Shape142)

HAnimSegment64.children.append(HAnimSite140)

HAnimJoint63.children.append(HAnimSegment64)
HAnimJoint143 = x3d.HAnimJoint()
HAnimJoint143.name = "l_hip"
HAnimJoint143.DEF = "hanim_l_hip"
HAnimJoint143.center = [0.0961,0.9124,-0.0001]
HAnimJoint143.ulimit = [0,0,0]
HAnimJoint143.llimit = [0,0,0]
HAnimSegment144 = x3d.HAnimSegment()
HAnimSegment144.name = "l_thigh"
HAnimSegment144.DEF = "hanim_l_thigh"
#<HAnimJoint name='l_hip'/> visualization sphere is placed within <HAnimSegment name='l_thigh'/>
TouchSensor145 = x3d.TouchSensor()
TouchSensor145.description = "HAnimJoint l_hip, HAnimSegment l_thigh"

HAnimSegment144.children.append(TouchSensor145)
Transform146 = x3d.Transform()
Transform146.translation = [0.0961,0.9124,-0.0001]
Shape147 = x3d.Shape()
Shape147.USE = "HAnimJointShape"

Transform146.children.append(Shape147)

HAnimSegment144.children.append(Transform146)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_hip'/> to <HAnimJoint name='l_knee'/>
Shape148 = x3d.Shape()
LineSet149 = x3d.LineSet()
LineSet149.vertexCount = [2]
Coordinate150 = x3d.Coordinate()

LineSet149.coord = Coordinate150
ColorRGBA151 = x3d.ColorRGBA()
ColorRGBA151.USE = "HAnimSegmentLineColorRGBA"

LineSet149.color = ColorRGBA151

Shape148.geometry = LineSet149

HAnimSegment144.children.append(Shape148)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_hip'/> to <HAnimSite name='l_knee_crease'/>
Shape152 = x3d.Shape()
LineSet153 = x3d.LineSet()
LineSet153.vertexCount = [2]
Coordinate154 = x3d.Coordinate()

LineSet153.coord = Coordinate154
ColorRGBA155 = x3d.ColorRGBA()
ColorRGBA155.USE = "HAnimSiteLineColorRGBA"

LineSet153.color = ColorRGBA155

Shape152.geometry = LineSet153

HAnimSegment144.children.append(Shape152)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_hip'/> to <HAnimSite name='l_femoral_lateral_epicn'/>
Shape156 = x3d.Shape()
LineSet157 = x3d.LineSet()
LineSet157.vertexCount = [2]
Coordinate158 = x3d.Coordinate()

LineSet157.coord = Coordinate158
ColorRGBA159 = x3d.ColorRGBA()
ColorRGBA159.USE = "HAnimSiteLineColorRGBA"

LineSet157.color = ColorRGBA159

Shape156.geometry = LineSet157

HAnimSegment144.children.append(Shape156)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_hip'/> to <HAnimSite name='l_femoral_medial_epicn'/>
Shape160 = x3d.Shape()
LineSet161 = x3d.LineSet()
LineSet161.vertexCount = [2]
Coordinate162 = x3d.Coordinate()

LineSet161.coord = Coordinate162
ColorRGBA163 = x3d.ColorRGBA()
ColorRGBA163.USE = "HAnimSiteLineColorRGBA"

LineSet161.color = ColorRGBA163

Shape160.geometry = LineSet161

HAnimSegment144.children.append(Shape160)
HAnimSite164 = x3d.HAnimSite()
HAnimSite164.name = "l_knee_crease_pt"
HAnimSite164.DEF = "hanim_l_knee_crease_pt"
HAnimSite164.translation = [0.0993,0.4881,-0.0309]
#HAnimSite visualization shape
TouchSensor165 = x3d.TouchSensor()
TouchSensor165.description = "HAnimSite l_knee_crease"

HAnimSite164.children.append(TouchSensor165)
Shape166 = x3d.Shape()
Shape166.USE = "HAnimSiteShape"

HAnimSite164.children.append(Shape166)

HAnimSegment144.children.append(HAnimSite164)
HAnimSite167 = x3d.HAnimSite()
HAnimSite167.name = "l_femoral_lateral_epicn_pt"
HAnimSite167.DEF = "hanim_l_femoral_lateral_epicn_pt"
HAnimSite167.translation = [0.1598,0.4967,0.0297]
#HAnimSite visualization shape
TouchSensor168 = x3d.TouchSensor()
TouchSensor168.description = "HAnimSite l_femoral_lateral_epicn"

HAnimSite167.children.append(TouchSensor168)
Shape169 = x3d.Shape()
Shape169.USE = "HAnimSiteShape"

HAnimSite167.children.append(Shape169)

HAnimSegment144.children.append(HAnimSite167)
HAnimSite170 = x3d.HAnimSite()
HAnimSite170.name = "l_femoral_medial_epicn_pt"
HAnimSite170.DEF = "hanim_l_femoral_medial_epicn_pt"
HAnimSite170.translation = [0.0398,0.4946,0.0303]
#HAnimSite visualization shape
TouchSensor171 = x3d.TouchSensor()
TouchSensor171.description = "HAnimSite l_femoral_medial_epicn"

HAnimSite170.children.append(TouchSensor171)
Shape172 = x3d.Shape()
Shape172.USE = "HAnimSiteShape"

HAnimSite170.children.append(Shape172)

HAnimSegment144.children.append(HAnimSite170)

HAnimJoint143.children.append(HAnimSegment144)
HAnimJoint173 = x3d.HAnimJoint()
HAnimJoint173.name = "l_knee"
HAnimJoint173.DEF = "hanim_l_knee"
HAnimJoint173.center = [0.104,0.4867,0.0308]
HAnimJoint173.ulimit = [0,0,0]
HAnimJoint173.llimit = [0,0,0]
HAnimSegment174 = x3d.HAnimSegment()
HAnimSegment174.name = "l_calf"
HAnimSegment174.DEF = "hanim_l_calf"
#<HAnimJoint name='l_knee'/> visualization sphere is placed within <HAnimSegment name='l_calf'/>
TouchSensor175 = x3d.TouchSensor()
TouchSensor175.description = "HAnimJoint l_knee, HAnimSegment l_calf"

HAnimSegment174.children.append(TouchSensor175)
Transform176 = x3d.Transform()
Transform176.translation = [0.104,0.4867,0.0308]
Shape177 = x3d.Shape()
Shape177.USE = "HAnimJointShape"

Transform176.children.append(Shape177)

HAnimSegment174.children.append(Transform176)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_knee'/> to <HAnimJoint name='l_ankle'/>
Shape178 = x3d.Shape()
LineSet179 = x3d.LineSet()
LineSet179.vertexCount = [2]
Coordinate180 = x3d.Coordinate()

LineSet179.coord = Coordinate180
ColorRGBA181 = x3d.ColorRGBA()
ColorRGBA181.USE = "HAnimSegmentLineColorRGBA"

LineSet179.color = ColorRGBA181

Shape178.geometry = LineSet179

HAnimSegment174.children.append(Shape178)

HAnimJoint173.children.append(HAnimSegment174)
HAnimJoint182 = x3d.HAnimJoint()
HAnimJoint182.name = "l_ankle"
HAnimJoint182.DEF = "hanim_l_ankle"
HAnimJoint182.center = [0.1101,0.0656,-0.0736]
HAnimJoint182.ulimit = [0,0,0]
HAnimJoint182.llimit = [0,0,0]
HAnimSegment183 = x3d.HAnimSegment()
HAnimSegment183.name = "l_hindfoot"
HAnimSegment183.DEF = "hanim_l_hindfoot"
#<HAnimJoint name='l_ankle'/> visualization sphere is placed within <HAnimSegment name='l_hindfoot'/>
TouchSensor184 = x3d.TouchSensor()
TouchSensor184.description = "HAnimJoint l_ankle, HAnimSegment l_hindfoot"

HAnimSegment183.children.append(TouchSensor184)
Transform185 = x3d.Transform()
Transform185.translation = [0.1101,0.0656,-0.0736]
Shape186 = x3d.Shape()
Shape186.USE = "HAnimJointShape"

Transform185.children.append(Shape186)

HAnimSegment183.children.append(Transform185)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_ankle'/> to <HAnimJoint name='l_subtalar'/>
Shape187 = x3d.Shape()
LineSet188 = x3d.LineSet()
LineSet188.vertexCount = [2]
Coordinate189 = x3d.Coordinate()

LineSet188.coord = Coordinate189
ColorRGBA190 = x3d.ColorRGBA()
ColorRGBA190.USE = "HAnimSegmentLineColorRGBA"

LineSet188.color = ColorRGBA190

Shape187.geometry = LineSet188

HAnimSegment183.children.append(Shape187)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_ankle'/> to <HAnimSite name='l_lateral_malleolus'/>
Shape191 = x3d.Shape()
LineSet192 = x3d.LineSet()
LineSet192.vertexCount = [2]
Coordinate193 = x3d.Coordinate()

LineSet192.coord = Coordinate193
ColorRGBA194 = x3d.ColorRGBA()
ColorRGBA194.USE = "HAnimSiteLineColorRGBA"

LineSet192.color = ColorRGBA194

Shape191.geometry = LineSet192

HAnimSegment183.children.append(Shape191)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_ankle'/> to <HAnimSite name='l_medial_malleolus'/>
Shape195 = x3d.Shape()
LineSet196 = x3d.LineSet()
LineSet196.vertexCount = [2]
Coordinate197 = x3d.Coordinate()

LineSet196.coord = Coordinate197
ColorRGBA198 = x3d.ColorRGBA()
ColorRGBA198.USE = "HAnimSiteLineColorRGBA"

LineSet196.color = ColorRGBA198

Shape195.geometry = LineSet196

HAnimSegment183.children.append(Shape195)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_ankle'/> to <HAnimSite name='l_sphyrion'/>
Shape199 = x3d.Shape()
LineSet200 = x3d.LineSet()
LineSet200.vertexCount = [2]
Coordinate201 = x3d.Coordinate()

LineSet200.coord = Coordinate201
ColorRGBA202 = x3d.ColorRGBA()
ColorRGBA202.USE = "HAnimSiteLineColorRGBA"

LineSet200.color = ColorRGBA202

Shape199.geometry = LineSet200

HAnimSegment183.children.append(Shape199)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_ankle'/> to <HAnimSite name='l_calcaneous_post'/>
Shape203 = x3d.Shape()
LineSet204 = x3d.LineSet()
LineSet204.vertexCount = [2]
Coordinate205 = x3d.Coordinate()

LineSet204.coord = Coordinate205
ColorRGBA206 = x3d.ColorRGBA()
ColorRGBA206.USE = "HAnimSiteLineColorRGBA"

LineSet204.color = ColorRGBA206

Shape203.geometry = LineSet204

HAnimSegment183.children.append(Shape203)
HAnimSite207 = x3d.HAnimSite()
HAnimSite207.name = "l_lateral_malleolus_pt"
HAnimSite207.DEF = "hanim_l_lateral_malleolus_pt"
HAnimSite207.translation = [0.1308,0.0597,-0.1032]
#HAnimSite visualization shape
TouchSensor208 = x3d.TouchSensor()
TouchSensor208.description = "HAnimSite l_lateral_malleolus"

HAnimSite207.children.append(TouchSensor208)
Shape209 = x3d.Shape()
Shape209.USE = "HAnimSiteShape"

HAnimSite207.children.append(Shape209)

HAnimSegment183.children.append(HAnimSite207)
HAnimSite210 = x3d.HAnimSite()
HAnimSite210.name = "l_medial_malleolus_pt"
HAnimSite210.DEF = "hanim_l_medial_malleolus_pt"
HAnimSite210.translation = [0.089,0.0716,-0.0881]
#HAnimSite visualization shape
TouchSensor211 = x3d.TouchSensor()
TouchSensor211.description = "HAnimSite l_medial_malleolus"

HAnimSite210.children.append(TouchSensor211)
Shape212 = x3d.Shape()
Shape212.USE = "HAnimSiteShape"

HAnimSite210.children.append(Shape212)

HAnimSegment183.children.append(HAnimSite210)
HAnimSite213 = x3d.HAnimSite()
HAnimSite213.name = "l_sphyrion_pt"
HAnimSite213.DEF = "hanim_l_sphyrion_pt"
HAnimSite213.translation = [0.089,0.0575,-0.0943]
#HAnimSite visualization shape
TouchSensor214 = x3d.TouchSensor()
TouchSensor214.description = "HAnimSite l_sphyrion"

HAnimSite213.children.append(TouchSensor214)
Shape215 = x3d.Shape()
Shape215.USE = "HAnimSiteShape"

HAnimSite213.children.append(Shape215)

HAnimSegment183.children.append(HAnimSite213)
HAnimSite216 = x3d.HAnimSite()
HAnimSite216.name = "l_calcaneous_post_pt"
HAnimSite216.DEF = "hanim_l_calcaneous_post_pt"
HAnimSite216.translation = [0.0974,0.0259,-0.1171]
#HAnimSite visualization shape
TouchSensor217 = x3d.TouchSensor()
TouchSensor217.description = "HAnimSite l_calcaneous_post"

HAnimSite216.children.append(TouchSensor217)
Shape218 = x3d.Shape()
Shape218.USE = "HAnimSiteShape"

HAnimSite216.children.append(Shape218)

HAnimSegment183.children.append(HAnimSite216)

HAnimJoint182.children.append(HAnimSegment183)
HAnimJoint219 = x3d.HAnimJoint()
HAnimJoint219.name = "l_subtalar"
HAnimJoint219.DEF = "hanim_l_subtalar"
HAnimJoint219.center = [0.1086,0.0001,-0.0368]
HAnimJoint219.ulimit = [0,0,0]
HAnimJoint219.llimit = [0,0,0]
HAnimSegment220 = x3d.HAnimSegment()
HAnimSegment220.name = "l_midproximal"
HAnimSegment220.DEF = "hanim_l_midproximal"
#<HAnimJoint name='l_subtalar'/> visualization sphere is placed within <HAnimSegment name='l_midproximal'/>
TouchSensor221 = x3d.TouchSensor()
TouchSensor221.description = "HAnimJoint l_subtalar, HAnimSegment l_midproximal"

HAnimSegment220.children.append(TouchSensor221)
Transform222 = x3d.Transform()
Transform222.translation = [0.1086,0.0001,-0.0368]
Shape223 = x3d.Shape()
Shape223.USE = "HAnimJointShape"

Transform222.children.append(Shape223)

HAnimSegment220.children.append(Transform222)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_subtalar'/> to <HAnimJoint name='l_midtarsal'/>
Shape224 = x3d.Shape()
LineSet225 = x3d.LineSet()
LineSet225.vertexCount = [2]
Coordinate226 = x3d.Coordinate()

LineSet225.coord = Coordinate226
ColorRGBA227 = x3d.ColorRGBA()
ColorRGBA227.USE = "HAnimSegmentLineColorRGBA"

LineSet225.color = ColorRGBA227

Shape224.geometry = LineSet225

HAnimSegment220.children.append(Shape224)

HAnimJoint219.children.append(HAnimSegment220)
HAnimJoint228 = x3d.HAnimJoint()
HAnimJoint228.name = "l_midtarsal"
HAnimJoint228.DEF = "hanim_l_midtarsal"
HAnimJoint228.center = [0.1086,0.0001,0.0368]
HAnimJoint228.ulimit = [0,0,0]
HAnimJoint228.llimit = [0,0,0]
HAnimSegment229 = x3d.HAnimSegment()
HAnimSegment229.name = "l_middistal"
HAnimSegment229.DEF = "hanim_l_middistal"
#<HAnimJoint name='l_midtarsal'/> visualization sphere is placed within <HAnimSegment name='l_middistal'/>
TouchSensor230 = x3d.TouchSensor()
TouchSensor230.description = "HAnimJoint l_midtarsal, HAnimSegment l_middistal"

HAnimSegment229.children.append(TouchSensor230)
Transform231 = x3d.Transform()
Transform231.translation = [0.1086,0.0001,0.0368]
Shape232 = x3d.Shape()
Shape232.USE = "HAnimJointShape"

Transform231.children.append(Shape232)

HAnimSegment229.children.append(Transform231)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_midtarsal'/> to <HAnimJoint name='l_metatarsal'/>
Shape233 = x3d.Shape()
LineSet234 = x3d.LineSet()
LineSet234.vertexCount = [2]
Coordinate235 = x3d.Coordinate()

LineSet234.coord = Coordinate235
ColorRGBA236 = x3d.ColorRGBA()
ColorRGBA236.USE = "HAnimSegmentLineColorRGBA"

LineSet234.color = ColorRGBA236

Shape233.geometry = LineSet234

HAnimSegment229.children.append(Shape233)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_midtarsal'/> to <HAnimSite name='l_metatarsal_pha1'/>
Shape237 = x3d.Shape()
LineSet238 = x3d.LineSet()
LineSet238.vertexCount = [2]
Coordinate239 = x3d.Coordinate()

LineSet238.coord = Coordinate239
ColorRGBA240 = x3d.ColorRGBA()
ColorRGBA240.USE = "HAnimSiteLineColorRGBA"

LineSet238.color = ColorRGBA240

Shape237.geometry = LineSet238

HAnimSegment229.children.append(Shape237)
HAnimSite241 = x3d.HAnimSite()
HAnimSite241.name = "l_metatarsal_pha1_pt"
HAnimSite241.DEF = "hanim_l_metatarsal_pha1_pt"
HAnimSite241.translation = [0.0816,0.0232,0.0106]
#HAnimSite visualization shape
TouchSensor242 = x3d.TouchSensor()
TouchSensor242.description = "HAnimSite l_metatarsal_pha1"

HAnimSite241.children.append(TouchSensor242)
Shape243 = x3d.Shape()
Shape243.USE = "HAnimSiteShape"

HAnimSite241.children.append(Shape243)

HAnimSegment229.children.append(HAnimSite241)

HAnimJoint228.children.append(HAnimSegment229)
HAnimJoint244 = x3d.HAnimJoint()
HAnimJoint244.name = "l_metatarsal"
HAnimJoint244.DEF = "hanim_l_metatarsal"
HAnimJoint244.center = [0.1086,0,0.0762]
HAnimJoint244.ulimit = [0,0,0]
HAnimJoint244.llimit = [0,0,0]
HAnimSegment245 = x3d.HAnimSegment()
HAnimSegment245.name = "l_forefoot"
HAnimSegment245.DEF = "hanim_l_forefoot"
#<HAnimJoint name='l_metatarsal'/> visualization sphere is placed within <HAnimSegment name='l_forefoot'/>
TouchSensor246 = x3d.TouchSensor()
TouchSensor246.description = "HAnimJoint l_metatarsal, HAnimSegment l_forefoot"

HAnimSegment245.children.append(TouchSensor246)
Transform247 = x3d.Transform()
Transform247.translation = [0.1086,0,0.0762]
Shape248 = x3d.Shape()
Shape248.USE = "HAnimJointShape"

Transform247.children.append(Shape248)

HAnimSegment245.children.append(Transform247)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_metatarsal'/> to <HAnimSite name='l_forefoot_tip'/>
Shape249 = x3d.Shape()
LineSet250 = x3d.LineSet()
LineSet250.vertexCount = [2]
Coordinate251 = x3d.Coordinate()

LineSet250.coord = Coordinate251
ColorRGBA252 = x3d.ColorRGBA()
ColorRGBA252.USE = "HAnimSiteLineColorRGBA"

LineSet250.color = ColorRGBA252

Shape249.geometry = LineSet250

HAnimSegment245.children.append(Shape249)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_metatarsal'/> to <HAnimSite name='l_metatarsal_pha5'/>
Shape253 = x3d.Shape()
LineSet254 = x3d.LineSet()
LineSet254.vertexCount = [2]
Coordinate255 = x3d.Coordinate()

LineSet254.coord = Coordinate255
ColorRGBA256 = x3d.ColorRGBA()
ColorRGBA256.USE = "HAnimSiteLineColorRGBA"

LineSet254.color = ColorRGBA256

Shape253.geometry = LineSet254

HAnimSegment245.children.append(Shape253)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_metatarsal'/> to <HAnimSite name='l_digit2'/>
Shape257 = x3d.Shape()
LineSet258 = x3d.LineSet()
LineSet258.vertexCount = [2]
Coordinate259 = x3d.Coordinate()

LineSet258.coord = Coordinate259
ColorRGBA260 = x3d.ColorRGBA()
ColorRGBA260.USE = "HAnimSiteLineColorRGBA"

LineSet258.color = ColorRGBA260

Shape257.geometry = LineSet258

HAnimSegment245.children.append(Shape257)
HAnimSite261 = x3d.HAnimSite()
HAnimSite261.name = "l_forefoot_tip"
HAnimSite261.DEF = "hanim_l_forefoot_tip"
HAnimSite261.translation = [0.1354,0.0016,0.1476]
#HAnimSite visualization shape
TouchSensor262 = x3d.TouchSensor()
TouchSensor262.description = "HAnimSite l_forefoot_tip"

HAnimSite261.children.append(TouchSensor262)
Shape263 = x3d.Shape()
Shape263.USE = "HAnimSiteShape"

HAnimSite261.children.append(Shape263)

HAnimSegment245.children.append(HAnimSite261)
HAnimSite264 = x3d.HAnimSite()
HAnimSite264.name = "l_metatarsal_pha5_pt"
HAnimSite264.DEF = "hanim_l_metatarsal_pha5_pt"
HAnimSite264.translation = [0.1825,0.007,0.0928]
#HAnimSite visualization shape
TouchSensor265 = x3d.TouchSensor()
TouchSensor265.description = "HAnimSite l_metatarsal_pha5"

HAnimSite264.children.append(TouchSensor265)
Shape266 = x3d.Shape()
Shape266.USE = "HAnimSiteShape"

HAnimSite264.children.append(Shape266)

HAnimSegment245.children.append(HAnimSite264)
HAnimSite267 = x3d.HAnimSite()
HAnimSite267.name = "l_digit2_pt"
HAnimSite267.DEF = "hanim_l_digit2_pt"
HAnimSite267.translation = [0.1195,0.0079,0.1433]
#HAnimSite visualization shape
TouchSensor268 = x3d.TouchSensor()
TouchSensor268.description = "HAnimSite l_digit2"

HAnimSite267.children.append(TouchSensor268)
Shape269 = x3d.Shape()
Shape269.USE = "HAnimSiteShape"

HAnimSite267.children.append(Shape269)

HAnimSegment245.children.append(HAnimSite267)

HAnimJoint244.children.append(HAnimSegment245)

HAnimJoint228.children.append(HAnimJoint244)

HAnimJoint219.children.append(HAnimJoint228)

HAnimJoint182.children.append(HAnimJoint219)

HAnimJoint173.children.append(HAnimJoint182)

HAnimJoint143.children.append(HAnimJoint173)

HAnimJoint63.children.append(HAnimJoint143)
HAnimJoint270 = x3d.HAnimJoint()
HAnimJoint270.name = "r_hip"
HAnimJoint270.DEF = "hanim_r_hip"
HAnimJoint270.center = [-0.0961,0.9124,-0.0001]
HAnimJoint270.ulimit = [0,0,0]
HAnimJoint270.llimit = [0,0,0]
HAnimSegment271 = x3d.HAnimSegment()
HAnimSegment271.name = "r_thigh"
HAnimSegment271.DEF = "hanim_r_thigh"
#<HAnimJoint name='r_hip'/> visualization sphere is placed within <HAnimSegment name='r_thigh'/>
TouchSensor272 = x3d.TouchSensor()
TouchSensor272.description = "HAnimJoint r_hip, HAnimSegment r_thigh"

HAnimSegment271.children.append(TouchSensor272)
Transform273 = x3d.Transform()
Transform273.translation = [-0.0961,0.9124,-0.0001]
Shape274 = x3d.Shape()
Shape274.USE = "HAnimJointShape"

Transform273.children.append(Shape274)

HAnimSegment271.children.append(Transform273)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_hip'/> to <HAnimJoint name='r_knee'/>
Shape275 = x3d.Shape()
LineSet276 = x3d.LineSet()
LineSet276.vertexCount = [2]
Coordinate277 = x3d.Coordinate()

LineSet276.coord = Coordinate277
ColorRGBA278 = x3d.ColorRGBA()
ColorRGBA278.USE = "HAnimSegmentLineColorRGBA"

LineSet276.color = ColorRGBA278

Shape275.geometry = LineSet276

HAnimSegment271.children.append(Shape275)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_hip'/> to <HAnimSite name='r_knee_crease'/>
Shape279 = x3d.Shape()
LineSet280 = x3d.LineSet()
LineSet280.vertexCount = [2]
Coordinate281 = x3d.Coordinate()

LineSet280.coord = Coordinate281
ColorRGBA282 = x3d.ColorRGBA()
ColorRGBA282.USE = "HAnimSiteLineColorRGBA"

LineSet280.color = ColorRGBA282

Shape279.geometry = LineSet280

HAnimSegment271.children.append(Shape279)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_hip'/> to <HAnimSite name='r_femoral_lateral_epicn'/>
Shape283 = x3d.Shape()
LineSet284 = x3d.LineSet()
LineSet284.vertexCount = [2]
Coordinate285 = x3d.Coordinate()

LineSet284.coord = Coordinate285
ColorRGBA286 = x3d.ColorRGBA()
ColorRGBA286.USE = "HAnimSiteLineColorRGBA"

LineSet284.color = ColorRGBA286

Shape283.geometry = LineSet284

HAnimSegment271.children.append(Shape283)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_hip'/> to <HAnimSite name='r_femoral_medial_epicn'/>
Shape287 = x3d.Shape()
LineSet288 = x3d.LineSet()
LineSet288.vertexCount = [2]
Coordinate289 = x3d.Coordinate()

LineSet288.coord = Coordinate289
ColorRGBA290 = x3d.ColorRGBA()
ColorRGBA290.USE = "HAnimSiteLineColorRGBA"

LineSet288.color = ColorRGBA290

Shape287.geometry = LineSet288

HAnimSegment271.children.append(Shape287)
HAnimSite291 = x3d.HAnimSite()
HAnimSite291.name = "r_knee_crease_pt"
HAnimSite291.DEF = "hanim_r_knee_crease_pt"
HAnimSite291.translation = [-0.0825,0.4932,-0.0326]
#HAnimSite visualization shape
TouchSensor292 = x3d.TouchSensor()
TouchSensor292.description = "HAnimSite r_knee_crease"

HAnimSite291.children.append(TouchSensor292)
Shape293 = x3d.Shape()
Shape293.USE = "HAnimSiteShape"

HAnimSite291.children.append(Shape293)

HAnimSegment271.children.append(HAnimSite291)
HAnimSite294 = x3d.HAnimSite()
HAnimSite294.name = "r_femoral_lateral_epicn_pt"
HAnimSite294.DEF = "hanim_r_femoral_lateral_epicn_pt"
HAnimSite294.translation = [-0.1421,0.4992,0.031]
#HAnimSite visualization shape
TouchSensor295 = x3d.TouchSensor()
TouchSensor295.description = "HAnimSite r_femoral_lateral_epicn"

HAnimSite294.children.append(TouchSensor295)
Shape296 = x3d.Shape()
Shape296.USE = "HAnimSiteShape"

HAnimSite294.children.append(Shape296)

HAnimSegment271.children.append(HAnimSite294)
HAnimSite297 = x3d.HAnimSite()
HAnimSite297.name = "r_femoral_medial_epicn_pt"
HAnimSite297.DEF = "hanim_r_femoral_medial_epicn_pt"
HAnimSite297.translation = [-0.0221,0.5014,0.0289]
#HAnimSite visualization shape
TouchSensor298 = x3d.TouchSensor()
TouchSensor298.description = "HAnimSite r_femoral_medial_epicn"

HAnimSite297.children.append(TouchSensor298)
Shape299 = x3d.Shape()
Shape299.USE = "HAnimSiteShape"

HAnimSite297.children.append(Shape299)

HAnimSegment271.children.append(HAnimSite297)

HAnimJoint270.children.append(HAnimSegment271)
HAnimJoint300 = x3d.HAnimJoint()
HAnimJoint300.name = "r_knee"
HAnimJoint300.DEF = "hanim_r_knee"
HAnimJoint300.center = [-0.104,0.4867,0.0308]
HAnimJoint300.ulimit = [0,0,0]
HAnimJoint300.llimit = [0,0,0]
HAnimSegment301 = x3d.HAnimSegment()
HAnimSegment301.name = "r_calf"
HAnimSegment301.DEF = "hanim_r_calf"
#<HAnimJoint name='r_knee'/> visualization sphere is placed within <HAnimSegment name='r_calf'/>
TouchSensor302 = x3d.TouchSensor()
TouchSensor302.description = "HAnimJoint r_knee, HAnimSegment r_calf"

HAnimSegment301.children.append(TouchSensor302)
Transform303 = x3d.Transform()
Transform303.translation = [-0.104,0.4867,0.0308]
Shape304 = x3d.Shape()
Shape304.USE = "HAnimJointShape"

Transform303.children.append(Shape304)

HAnimSegment301.children.append(Transform303)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_knee'/> to <HAnimJoint name='r_ankle'/>
Shape305 = x3d.Shape()
LineSet306 = x3d.LineSet()
LineSet306.vertexCount = [2]
Coordinate307 = x3d.Coordinate()

LineSet306.coord = Coordinate307
ColorRGBA308 = x3d.ColorRGBA()
ColorRGBA308.USE = "HAnimSegmentLineColorRGBA"

LineSet306.color = ColorRGBA308

Shape305.geometry = LineSet306

HAnimSegment301.children.append(Shape305)

HAnimJoint300.children.append(HAnimSegment301)
HAnimJoint309 = x3d.HAnimJoint()
HAnimJoint309.name = "r_ankle"
HAnimJoint309.DEF = "hanim_r_ankle"
HAnimJoint309.center = [-0.1101,0.0656,-0.0736]
HAnimJoint309.ulimit = [0,0,0]
HAnimJoint309.llimit = [0,0,0]
HAnimSegment310 = x3d.HAnimSegment()
HAnimSegment310.name = "r_hindfoot"
HAnimSegment310.DEF = "hanim_r_hindfoot"
#<HAnimJoint name='r_ankle'/> visualization sphere is placed within <HAnimSegment name='r_hindfoot'/>
TouchSensor311 = x3d.TouchSensor()
TouchSensor311.description = "HAnimJoint r_ankle, HAnimSegment r_hindfoot"

HAnimSegment310.children.append(TouchSensor311)
Transform312 = x3d.Transform()
Transform312.translation = [-0.1101,0.0656,-0.0736]
Shape313 = x3d.Shape()
Shape313.USE = "HAnimJointShape"

Transform312.children.append(Shape313)

HAnimSegment310.children.append(Transform312)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_ankle'/> to <HAnimJoint name='r_subtalar'/>
Shape314 = x3d.Shape()
LineSet315 = x3d.LineSet()
LineSet315.vertexCount = [2]
Coordinate316 = x3d.Coordinate()

LineSet315.coord = Coordinate316
ColorRGBA317 = x3d.ColorRGBA()
ColorRGBA317.USE = "HAnimSegmentLineColorRGBA"

LineSet315.color = ColorRGBA317

Shape314.geometry = LineSet315

HAnimSegment310.children.append(Shape314)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_ankle'/> to <HAnimSite name='r_lateral_malleolus'/>
Shape318 = x3d.Shape()
LineSet319 = x3d.LineSet()
LineSet319.vertexCount = [2]
Coordinate320 = x3d.Coordinate()

LineSet319.coord = Coordinate320
ColorRGBA321 = x3d.ColorRGBA()
ColorRGBA321.USE = "HAnimSiteLineColorRGBA"

LineSet319.color = ColorRGBA321

Shape318.geometry = LineSet319

HAnimSegment310.children.append(Shape318)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_ankle'/> to <HAnimSite name='r_medial_malleolus'/>
Shape322 = x3d.Shape()
LineSet323 = x3d.LineSet()
LineSet323.vertexCount = [2]
Coordinate324 = x3d.Coordinate()

LineSet323.coord = Coordinate324
ColorRGBA325 = x3d.ColorRGBA()
ColorRGBA325.USE = "HAnimSiteLineColorRGBA"

LineSet323.color = ColorRGBA325

Shape322.geometry = LineSet323

HAnimSegment310.children.append(Shape322)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_ankle'/> to <HAnimSite name='r_sphyrion'/>
Shape326 = x3d.Shape()
LineSet327 = x3d.LineSet()
LineSet327.vertexCount = [2]
Coordinate328 = x3d.Coordinate()

LineSet327.coord = Coordinate328
ColorRGBA329 = x3d.ColorRGBA()
ColorRGBA329.USE = "HAnimSiteLineColorRGBA"

LineSet327.color = ColorRGBA329

Shape326.geometry = LineSet327

HAnimSegment310.children.append(Shape326)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_ankle'/> to <HAnimSite name='r_calcaneous_post'/>
Shape330 = x3d.Shape()
LineSet331 = x3d.LineSet()
LineSet331.vertexCount = [2]
Coordinate332 = x3d.Coordinate()

LineSet331.coord = Coordinate332
ColorRGBA333 = x3d.ColorRGBA()
ColorRGBA333.USE = "HAnimSiteLineColorRGBA"

LineSet331.color = ColorRGBA333

Shape330.geometry = LineSet331

HAnimSegment310.children.append(Shape330)
HAnimSite334 = x3d.HAnimSite()
HAnimSite334.name = "r_lateral_malleolus_pt"
HAnimSite334.DEF = "hanim_r_lateral_malleolus_pt"
HAnimSite334.translation = [-0.1006,0.0658,-0.1075]
#HAnimSite visualization shape
TouchSensor335 = x3d.TouchSensor()
TouchSensor335.description = "HAnimSite r_lateral_malleolus"

HAnimSite334.children.append(TouchSensor335)
Shape336 = x3d.Shape()
Shape336.USE = "HAnimSiteShape"

HAnimSite334.children.append(Shape336)

HAnimSegment310.children.append(HAnimSite334)
HAnimSite337 = x3d.HAnimSite()
HAnimSite337.name = "r_medial_malleolus_pt"
HAnimSite337.DEF = "hanim_r_medial_malleolus_pt"
HAnimSite337.translation = [-0.0591,0.076,-0.0928]
#HAnimSite visualization shape
TouchSensor338 = x3d.TouchSensor()
TouchSensor338.description = "HAnimSite r_medial_malleolus"

HAnimSite337.children.append(TouchSensor338)
Shape339 = x3d.Shape()
Shape339.USE = "HAnimSiteShape"

HAnimSite337.children.append(Shape339)

HAnimSegment310.children.append(HAnimSite337)
HAnimSite340 = x3d.HAnimSite()
HAnimSite340.name = "r_sphyrion_pt"
HAnimSite340.DEF = "hanim_r_sphyrion_pt"
HAnimSite340.translation = [-0.0603,0.061,-0.1002]
#HAnimSite visualization shape
TouchSensor341 = x3d.TouchSensor()
TouchSensor341.description = "HAnimSite r_sphyrion"

HAnimSite340.children.append(TouchSensor341)
Shape342 = x3d.Shape()
Shape342.USE = "HAnimSiteShape"

HAnimSite340.children.append(Shape342)

HAnimSegment310.children.append(HAnimSite340)
HAnimSite343 = x3d.HAnimSite()
HAnimSite343.name = "r_calcaneous_post_pt"
HAnimSite343.DEF = "hanim_r_calcaneous_post_pt"
HAnimSite343.translation = [-0.0692,0.0297,-0.1221]
#HAnimSite visualization shape
TouchSensor344 = x3d.TouchSensor()
TouchSensor344.description = "HAnimSite r_calcaneous_post"

HAnimSite343.children.append(TouchSensor344)
Shape345 = x3d.Shape()
Shape345.USE = "HAnimSiteShape"

HAnimSite343.children.append(Shape345)

HAnimSegment310.children.append(HAnimSite343)

HAnimJoint309.children.append(HAnimSegment310)
HAnimJoint346 = x3d.HAnimJoint()
HAnimJoint346.name = "r_subtalar"
HAnimJoint346.DEF = "hanim_r_subtalar"
HAnimJoint346.center = [-0.1086,0.0001,-0.0368]
HAnimJoint346.ulimit = [0,0,0]
HAnimJoint346.llimit = [0,0,0]
HAnimSegment347 = x3d.HAnimSegment()
HAnimSegment347.name = "r_midproximal"
HAnimSegment347.DEF = "hanim_r_midproximal"
#<HAnimJoint name='r_subtalar'/> visualization sphere is placed within <HAnimSegment name='r_midproximal'/>
TouchSensor348 = x3d.TouchSensor()
TouchSensor348.description = "HAnimJoint r_subtalar, HAnimSegment r_midproximal"

HAnimSegment347.children.append(TouchSensor348)
Transform349 = x3d.Transform()
Transform349.translation = [-0.1086,0.0001,-0.0368]
Shape350 = x3d.Shape()
Shape350.USE = "HAnimJointShape"

Transform349.children.append(Shape350)

HAnimSegment347.children.append(Transform349)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_subtalar'/> to <HAnimJoint name='r_midtarsal'/>
Shape351 = x3d.Shape()
LineSet352 = x3d.LineSet()
LineSet352.vertexCount = [2]
Coordinate353 = x3d.Coordinate()

LineSet352.coord = Coordinate353
ColorRGBA354 = x3d.ColorRGBA()
ColorRGBA354.USE = "HAnimSegmentLineColorRGBA"

LineSet352.color = ColorRGBA354

Shape351.geometry = LineSet352

HAnimSegment347.children.append(Shape351)

HAnimJoint346.children.append(HAnimSegment347)
HAnimJoint355 = x3d.HAnimJoint()
HAnimJoint355.name = "r_midtarsal"
HAnimJoint355.DEF = "hanim_r_midtarsal"
HAnimJoint355.center = [-0.1086,0.0001,0.0368]
HAnimJoint355.ulimit = [0,0,0]
HAnimJoint355.llimit = [0,0,0]
HAnimSegment356 = x3d.HAnimSegment()
HAnimSegment356.name = "r_middistal"
HAnimSegment356.DEF = "hanim_r_middistal"
#<HAnimJoint name='r_midtarsal'/> visualization sphere is placed within <HAnimSegment name='r_middistal'/>
TouchSensor357 = x3d.TouchSensor()
TouchSensor357.description = "HAnimJoint r_midtarsal, HAnimSegment r_middistal"

HAnimSegment356.children.append(TouchSensor357)
Transform358 = x3d.Transform()
Transform358.translation = [-0.1086,0.0001,0.0368]
Shape359 = x3d.Shape()
Shape359.USE = "HAnimJointShape"

Transform358.children.append(Shape359)

HAnimSegment356.children.append(Transform358)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_midtarsal'/> to <HAnimJoint name='r_metatarsal'/>
Shape360 = x3d.Shape()
LineSet361 = x3d.LineSet()
LineSet361.vertexCount = [2]
Coordinate362 = x3d.Coordinate()

LineSet361.coord = Coordinate362
ColorRGBA363 = x3d.ColorRGBA()
ColorRGBA363.USE = "HAnimSegmentLineColorRGBA"

LineSet361.color = ColorRGBA363

Shape360.geometry = LineSet361

HAnimSegment356.children.append(Shape360)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_midtarsal'/> to <HAnimSite name='r_metatarsal_pha1'/>
Shape364 = x3d.Shape()
LineSet365 = x3d.LineSet()
LineSet365.vertexCount = [2]
Coordinate366 = x3d.Coordinate()

LineSet365.coord = Coordinate366
ColorRGBA367 = x3d.ColorRGBA()
ColorRGBA367.USE = "HAnimSiteLineColorRGBA"

LineSet365.color = ColorRGBA367

Shape364.geometry = LineSet365

HAnimSegment356.children.append(Shape364)
HAnimSite368 = x3d.HAnimSite()
HAnimSite368.name = "r_metatarsal_pha1_pt"
HAnimSite368.DEF = "hanim_r_metatarsal_pha1_pt"
HAnimSite368.translation = [-0.0521,0.026,0.0127]
#HAnimSite visualization shape
TouchSensor369 = x3d.TouchSensor()
TouchSensor369.description = "HAnimSite r_metatarsal_pha1"

HAnimSite368.children.append(TouchSensor369)
Shape370 = x3d.Shape()
Shape370.USE = "HAnimSiteShape"

HAnimSite368.children.append(Shape370)

HAnimSegment356.children.append(HAnimSite368)

HAnimJoint355.children.append(HAnimSegment356)
HAnimJoint371 = x3d.HAnimJoint()
HAnimJoint371.name = "r_metatarsal"
HAnimJoint371.DEF = "hanim_r_metatarsal"
HAnimJoint371.center = [-0.1086,0,0.0762]
HAnimJoint371.ulimit = [0,0,0]
HAnimJoint371.llimit = [0,0,0]
HAnimSegment372 = x3d.HAnimSegment()
HAnimSegment372.name = "r_forefoot"
HAnimSegment372.DEF = "hanim_r_forefoot"
#<HAnimJoint name='r_metatarsal'/> visualization sphere is placed within <HAnimSegment name='r_forefoot'/>
TouchSensor373 = x3d.TouchSensor()
TouchSensor373.description = "HAnimJoint r_metatarsal, HAnimSegment r_forefoot"

HAnimSegment372.children.append(TouchSensor373)
Transform374 = x3d.Transform()
Transform374.translation = [-0.1086,0,0.0762]
Shape375 = x3d.Shape()
Shape375.USE = "HAnimJointShape"

Transform374.children.append(Shape375)

HAnimSegment372.children.append(Transform374)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_metatarsal'/> to <HAnimSite name='r_forefoot_tip'/>
Shape376 = x3d.Shape()
LineSet377 = x3d.LineSet()
LineSet377.vertexCount = [2]
Coordinate378 = x3d.Coordinate()

LineSet377.coord = Coordinate378
ColorRGBA379 = x3d.ColorRGBA()
ColorRGBA379.USE = "HAnimSiteLineColorRGBA"

LineSet377.color = ColorRGBA379

Shape376.geometry = LineSet377

HAnimSegment372.children.append(Shape376)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_metatarsal'/> to <HAnimSite name='r_metatarsal_pha5'/>
Shape380 = x3d.Shape()
LineSet381 = x3d.LineSet()
LineSet381.vertexCount = [2]
Coordinate382 = x3d.Coordinate()

LineSet381.coord = Coordinate382
ColorRGBA383 = x3d.ColorRGBA()
ColorRGBA383.USE = "HAnimSiteLineColorRGBA"

LineSet381.color = ColorRGBA383

Shape380.geometry = LineSet381

HAnimSegment372.children.append(Shape380)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_metatarsal'/> to <HAnimSite name='r_digit2'/>
Shape384 = x3d.Shape()
LineSet385 = x3d.LineSet()
LineSet385.vertexCount = [2]
Coordinate386 = x3d.Coordinate()

LineSet385.coord = Coordinate386
ColorRGBA387 = x3d.ColorRGBA()
ColorRGBA387.USE = "HAnimSiteLineColorRGBA"

LineSet385.color = ColorRGBA387

Shape384.geometry = LineSet385

HAnimSegment372.children.append(Shape384)
HAnimSite388 = x3d.HAnimSite()
HAnimSite388.name = "r_forefoot_tip"
HAnimSite388.DEF = "hanim_r_forefoot_tip"
HAnimSite388.translation = [-0.1043,0.0227,0.145]
#HAnimSite visualization shape
TouchSensor389 = x3d.TouchSensor()
TouchSensor389.description = "HAnimSite r_forefoot_tip"

HAnimSite388.children.append(TouchSensor389)
Shape390 = x3d.Shape()
Shape390.USE = "HAnimSiteShape"

HAnimSite388.children.append(Shape390)

HAnimSegment372.children.append(HAnimSite388)
HAnimSite391 = x3d.HAnimSite()
HAnimSite391.name = "r_metatarsal_pha5_pt"
HAnimSite391.DEF = "hanim_r_metatarsal_pha5_pt"
HAnimSite391.translation = [-0.1523,0.0166,0.0895]
#HAnimSite visualization shape
TouchSensor392 = x3d.TouchSensor()
TouchSensor392.description = "HAnimSite r_metatarsal_pha5"

HAnimSite391.children.append(TouchSensor392)
Shape393 = x3d.Shape()
Shape393.USE = "HAnimSiteShape"

HAnimSite391.children.append(Shape393)

HAnimSegment372.children.append(HAnimSite391)
HAnimSite394 = x3d.HAnimSite()
HAnimSite394.name = "r_digit2_pt"
HAnimSite394.DEF = "hanim_r_digit2_pt"
HAnimSite394.translation = [-0.0883,0.0134,0.1383]
#HAnimSite visualization shape
TouchSensor395 = x3d.TouchSensor()
TouchSensor395.description = "HAnimSite r_digit2"

HAnimSite394.children.append(TouchSensor395)
Shape396 = x3d.Shape()
Shape396.USE = "HAnimSiteShape"

HAnimSite394.children.append(Shape396)

HAnimSegment372.children.append(HAnimSite394)

HAnimJoint371.children.append(HAnimSegment372)

HAnimJoint355.children.append(HAnimJoint371)

HAnimJoint346.children.append(HAnimJoint355)

HAnimJoint309.children.append(HAnimJoint346)

HAnimJoint300.children.append(HAnimJoint309)

HAnimJoint270.children.append(HAnimJoint300)

HAnimJoint63.children.append(HAnimJoint270)

HAnimJoint47.children.append(HAnimJoint63)
HAnimJoint397 = x3d.HAnimJoint()
HAnimJoint397.name = "vl5"
HAnimJoint397.DEF = "hanim_vl5"
HAnimJoint397.center = [0.0028,1.0568,-0.0776]
HAnimJoint397.ulimit = [0,0,0]
HAnimJoint397.llimit = [0,0,0]
HAnimSegment398 = x3d.HAnimSegment()
HAnimSegment398.name = "l5"
HAnimSegment398.DEF = "hanim_l5"
#<HAnimJoint name='vl5'/> visualization sphere is placed within <HAnimSegment name='l5'/>
TouchSensor399 = x3d.TouchSensor()
TouchSensor399.description = "HAnimJoint vl5, HAnimSegment l5"

HAnimSegment398.children.append(TouchSensor399)
Transform400 = x3d.Transform()
Transform400.translation = [0.0028,1.0568,-0.0776]
Shape401 = x3d.Shape()
Shape401.USE = "HAnimJointShape"

Transform400.children.append(Shape401)

HAnimSegment398.children.append(Transform400)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vl5'/> to <HAnimJoint name='vl4'/>
Shape402 = x3d.Shape()
LineSet403 = x3d.LineSet()
LineSet403.vertexCount = [2]
Coordinate404 = x3d.Coordinate()

LineSet403.coord = Coordinate404
ColorRGBA405 = x3d.ColorRGBA()
ColorRGBA405.USE = "HAnimSegmentLineColorRGBA"

LineSet403.color = ColorRGBA405

Shape402.geometry = LineSet403

HAnimSegment398.children.append(Shape402)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vl5'/> to <HAnimSite name='waist_preferred_post'/>
Shape406 = x3d.Shape()
LineSet407 = x3d.LineSet()
LineSet407.vertexCount = [2]
Coordinate408 = x3d.Coordinate()

LineSet407.coord = Coordinate408
ColorRGBA409 = x3d.ColorRGBA()
ColorRGBA409.USE = "HAnimSiteLineColorRGBA"

LineSet407.color = ColorRGBA409

Shape406.geometry = LineSet407

HAnimSegment398.children.append(Shape406)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vl5'/> to <HAnimSite name='navel'/>
Shape410 = x3d.Shape()
LineSet411 = x3d.LineSet()
LineSet411.vertexCount = [2]
Coordinate412 = x3d.Coordinate()

LineSet411.coord = Coordinate412
ColorRGBA413 = x3d.ColorRGBA()
ColorRGBA413.USE = "HAnimSiteLineColorRGBA"

LineSet411.color = ColorRGBA413

Shape410.geometry = LineSet411

HAnimSegment398.children.append(Shape410)
HAnimSite414 = x3d.HAnimSite()
HAnimSite414.name = "waist_preferred_post_pt"
HAnimSite414.DEF = "hanim_waist_preferred_post_pt"
HAnimSite414.translation = [0,1.0915,-0.1091]
#HAnimSite visualization shape
TouchSensor415 = x3d.TouchSensor()
TouchSensor415.description = "HAnimSite waist_preferred_post"

HAnimSite414.children.append(TouchSensor415)
Shape416 = x3d.Shape()
Shape416.USE = "HAnimSiteShape"

HAnimSite414.children.append(Shape416)

HAnimSegment398.children.append(HAnimSite414)
HAnimSite417 = x3d.HAnimSite()
HAnimSite417.name = "navel_pt"
HAnimSite417.DEF = "hanim_navel_pt"
HAnimSite417.translation = [0.0069,1.0966,0.1017]
#HAnimSite visualization shape
TouchSensor418 = x3d.TouchSensor()
TouchSensor418.description = "HAnimSite navel"

HAnimSite417.children.append(TouchSensor418)
Shape419 = x3d.Shape()
Shape419.USE = "HAnimSiteShape"

HAnimSite417.children.append(Shape419)

HAnimSegment398.children.append(HAnimSite417)

HAnimJoint397.children.append(HAnimSegment398)
HAnimJoint420 = x3d.HAnimJoint()
HAnimJoint420.name = "vl4"
HAnimJoint420.DEF = "hanim_vl4"
HAnimJoint420.center = [0.0035,1.0925,-0.0787]
HAnimJoint420.ulimit = [0,0,0]
HAnimJoint420.llimit = [0,0,0]
HAnimSegment421 = x3d.HAnimSegment()
HAnimSegment421.name = "l4"
HAnimSegment421.DEF = "hanim_l4"
#<HAnimJoint name='vl4'/> visualization sphere is placed within <HAnimSegment name='l4'/>
TouchSensor422 = x3d.TouchSensor()
TouchSensor422.description = "HAnimJoint vl4, HAnimSegment l4"

HAnimSegment421.children.append(TouchSensor422)
Transform423 = x3d.Transform()
Transform423.translation = [0.0035,1.0925,-0.0787]
Shape424 = x3d.Shape()
Shape424.USE = "HAnimJointShape"

Transform423.children.append(Shape424)

HAnimSegment421.children.append(Transform423)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vl4'/> to <HAnimJoint name='vl3'/>
Shape425 = x3d.Shape()
LineSet426 = x3d.LineSet()
LineSet426.vertexCount = [2]
Coordinate427 = x3d.Coordinate()

LineSet426.coord = Coordinate427
ColorRGBA428 = x3d.ColorRGBA()
ColorRGBA428.USE = "HAnimSegmentLineColorRGBA"

LineSet426.color = ColorRGBA428

Shape425.geometry = LineSet426

HAnimSegment421.children.append(Shape425)

HAnimJoint420.children.append(HAnimSegment421)
HAnimJoint429 = x3d.HAnimJoint()
HAnimJoint429.name = "vl3"
HAnimJoint429.DEF = "hanim_vl3"
HAnimJoint429.center = [0.0041,1.1276,-0.0796]
HAnimJoint429.ulimit = [0,0,0]
HAnimJoint429.llimit = [0,0,0]
HAnimSegment430 = x3d.HAnimSegment()
HAnimSegment430.name = "l3"
HAnimSegment430.DEF = "hanim_l3"
#<HAnimJoint name='vl3'/> visualization sphere is placed within <HAnimSegment name='l3'/>
TouchSensor431 = x3d.TouchSensor()
TouchSensor431.description = "HAnimJoint vl3, HAnimSegment l3"

HAnimSegment430.children.append(TouchSensor431)
Transform432 = x3d.Transform()
Transform432.translation = [0.0041,1.1276,-0.0796]
Shape433 = x3d.Shape()
Shape433.USE = "HAnimJointShape"

Transform432.children.append(Shape433)

HAnimSegment430.children.append(Transform432)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vl3'/> to <HAnimJoint name='vl2'/>
Shape434 = x3d.Shape()
LineSet435 = x3d.LineSet()
LineSet435.vertexCount = [2]
Coordinate436 = x3d.Coordinate()

LineSet435.coord = Coordinate436
ColorRGBA437 = x3d.ColorRGBA()
ColorRGBA437.USE = "HAnimSegmentLineColorRGBA"

LineSet435.color = ColorRGBA437

Shape434.geometry = LineSet435

HAnimSegment430.children.append(Shape434)

HAnimJoint429.children.append(HAnimSegment430)
HAnimJoint438 = x3d.HAnimJoint()
HAnimJoint438.name = "vl2"
HAnimJoint438.DEF = "hanim_vl2"
HAnimJoint438.center = [0.0045,1.1546,-0.08]
HAnimJoint438.ulimit = [0,0,0]
HAnimJoint438.llimit = [0,0,0]
HAnimSegment439 = x3d.HAnimSegment()
HAnimSegment439.name = "l2"
HAnimSegment439.DEF = "hanim_l2"
#<HAnimJoint name='vl2'/> visualization sphere is placed within <HAnimSegment name='l2'/>
TouchSensor440 = x3d.TouchSensor()
TouchSensor440.description = "HAnimJoint vl2, HAnimSegment l2"

HAnimSegment439.children.append(TouchSensor440)
Transform441 = x3d.Transform()
Transform441.translation = [0.0045,1.1546,-0.08]
Shape442 = x3d.Shape()
Shape442.USE = "HAnimJointShape"

Transform441.children.append(Shape442)

HAnimSegment439.children.append(Transform441)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vl2'/> to <HAnimJoint name='vl1'/>
Shape443 = x3d.Shape()
LineSet444 = x3d.LineSet()
LineSet444.vertexCount = [2]
Coordinate445 = x3d.Coordinate()

LineSet444.coord = Coordinate445
ColorRGBA446 = x3d.ColorRGBA()
ColorRGBA446.USE = "HAnimSegmentLineColorRGBA"

LineSet444.color = ColorRGBA446

Shape443.geometry = LineSet444

HAnimSegment439.children.append(Shape443)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vl2'/> to <HAnimSite name='r_rib10'/>
Shape447 = x3d.Shape()
LineSet448 = x3d.LineSet()
LineSet448.vertexCount = [2]
Coordinate449 = x3d.Coordinate()

LineSet448.coord = Coordinate449
ColorRGBA450 = x3d.ColorRGBA()
ColorRGBA450.USE = "HAnimSiteLineColorRGBA"

LineSet448.color = ColorRGBA450

Shape447.geometry = LineSet448

HAnimSegment439.children.append(Shape447)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vl2'/> to <HAnimSite name='l_rib10'/>
Shape451 = x3d.Shape()
LineSet452 = x3d.LineSet()
LineSet452.vertexCount = [2]
Coordinate453 = x3d.Coordinate()

LineSet452.coord = Coordinate453
ColorRGBA454 = x3d.ColorRGBA()
ColorRGBA454.USE = "HAnimSiteLineColorRGBA"

LineSet452.color = ColorRGBA454

Shape451.geometry = LineSet452

HAnimSegment439.children.append(Shape451)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vl2'/> to <HAnimSite name='rib10_midspine'/>
Shape455 = x3d.Shape()
LineSet456 = x3d.LineSet()
LineSet456.vertexCount = [2]
Coordinate457 = x3d.Coordinate()

LineSet456.coord = Coordinate457
ColorRGBA458 = x3d.ColorRGBA()
ColorRGBA458.USE = "HAnimSiteLineColorRGBA"

LineSet456.color = ColorRGBA458

Shape455.geometry = LineSet456

HAnimSegment439.children.append(Shape455)
HAnimSite459 = x3d.HAnimSite()
HAnimSite459.name = "r_rib10_pt"
HAnimSite459.DEF = "hanim_r_rib10_pt"
HAnimSite459.translation = [-0.0711,1.1941,0.1016]
#HAnimSite visualization shape
TouchSensor460 = x3d.TouchSensor()
TouchSensor460.description = "HAnimSite r_rib10"

HAnimSite459.children.append(TouchSensor460)
Shape461 = x3d.Shape()
Shape461.USE = "HAnimSiteShape"

HAnimSite459.children.append(Shape461)

HAnimSegment439.children.append(HAnimSite459)
HAnimSite462 = x3d.HAnimSite()
HAnimSite462.name = "l_rib10_pt"
HAnimSite462.DEF = "hanim_l_rib10_pt"
HAnimSite462.translation = [0.0871,1.1925,0.0992]
#HAnimSite visualization shape
TouchSensor463 = x3d.TouchSensor()
TouchSensor463.description = "HAnimSite l_rib10"

HAnimSite462.children.append(TouchSensor463)
Shape464 = x3d.Shape()
Shape464.USE = "HAnimSiteShape"

HAnimSite462.children.append(Shape464)

HAnimSegment439.children.append(HAnimSite462)
HAnimSite465 = x3d.HAnimSite()
HAnimSite465.name = "rib10_midspine_pt"
HAnimSite465.DEF = "hanim_rib10_midspine_pt"
HAnimSite465.translation = [0.0049,1.1908,-0.1113]
#HAnimSite visualization shape
TouchSensor466 = x3d.TouchSensor()
TouchSensor466.description = "HAnimSite rib10_midspine"

HAnimSite465.children.append(TouchSensor466)
Shape467 = x3d.Shape()
Shape467.USE = "HAnimSiteShape"

HAnimSite465.children.append(Shape467)

HAnimSegment439.children.append(HAnimSite465)

HAnimJoint438.children.append(HAnimSegment439)
HAnimJoint468 = x3d.HAnimJoint()
HAnimJoint468.name = "vl1"
HAnimJoint468.DEF = "hanim_vl1"
HAnimJoint468.center = [0.0048,1.1912,-0.0805]
HAnimJoint468.ulimit = [0,0,0]
HAnimJoint468.llimit = [0,0,0]
HAnimSegment469 = x3d.HAnimSegment()
HAnimSegment469.name = "l1"
HAnimSegment469.DEF = "hanim_l1"
#<HAnimJoint name='vl1'/> visualization sphere is placed within <HAnimSegment name='l1'/>
TouchSensor470 = x3d.TouchSensor()
TouchSensor470.description = "HAnimJoint vl1, HAnimSegment l1"

HAnimSegment469.children.append(TouchSensor470)
Transform471 = x3d.Transform()
Transform471.translation = [0.0048,1.1912,-0.0805]
Shape472 = x3d.Shape()
Shape472.USE = "HAnimJointShape"

Transform471.children.append(Shape472)

HAnimSegment469.children.append(Transform471)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vl1'/> to <HAnimJoint name='vt12'/>
Shape473 = x3d.Shape()
LineSet474 = x3d.LineSet()
LineSet474.vertexCount = [2]
Coordinate475 = x3d.Coordinate()

LineSet474.coord = Coordinate475
ColorRGBA476 = x3d.ColorRGBA()
ColorRGBA476.USE = "HAnimSegmentLineColorRGBA"

LineSet474.color = ColorRGBA476

Shape473.geometry = LineSet474

HAnimSegment469.children.append(Shape473)

HAnimJoint468.children.append(HAnimSegment469)
HAnimJoint477 = x3d.HAnimJoint()
HAnimJoint477.name = "vt12"
HAnimJoint477.DEF = "hanim_vt12"
HAnimJoint477.center = [0.0051,1.2278,-0.0808]
HAnimJoint477.ulimit = [0,0,0]
HAnimJoint477.llimit = [0,0,0]
HAnimSegment478 = x3d.HAnimSegment()
HAnimSegment478.name = "t12"
HAnimSegment478.DEF = "hanim_t12"
#<HAnimJoint name='vt12'/> visualization sphere is placed within <HAnimSegment name='t12'/>
TouchSensor479 = x3d.TouchSensor()
TouchSensor479.description = "HAnimJoint vt12, HAnimSegment t12"

HAnimSegment478.children.append(TouchSensor479)
Transform480 = x3d.Transform()
Transform480.translation = [0.0051,1.2278,-0.0808]
Shape481 = x3d.Shape()
Shape481.USE = "HAnimJointShape"

Transform480.children.append(Shape481)

HAnimSegment478.children.append(Transform480)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vt12'/> to <HAnimJoint name='vt11'/>
Shape482 = x3d.Shape()
LineSet483 = x3d.LineSet()
LineSet483.vertexCount = [2]
Coordinate484 = x3d.Coordinate()

LineSet483.coord = Coordinate484
ColorRGBA485 = x3d.ColorRGBA()
ColorRGBA485.USE = "HAnimSegmentLineColorRGBA"

LineSet483.color = ColorRGBA485

Shape482.geometry = LineSet483

HAnimSegment478.children.append(Shape482)

HAnimJoint477.children.append(HAnimSegment478)
HAnimJoint486 = x3d.HAnimJoint()
HAnimJoint486.name = "vt11"
HAnimJoint486.DEF = "hanim_vt11"
HAnimJoint486.center = [0.0053,1.2679,-0.081]
HAnimJoint486.ulimit = [0,0,0]
HAnimJoint486.llimit = [0,0,0]
HAnimSegment487 = x3d.HAnimSegment()
HAnimSegment487.name = "t11"
HAnimSegment487.DEF = "hanim_t11"
#<HAnimJoint name='vt11'/> visualization sphere is placed within <HAnimSegment name='t11'/>
TouchSensor488 = x3d.TouchSensor()
TouchSensor488.description = "HAnimJoint vt11, HAnimSegment t11"

HAnimSegment487.children.append(TouchSensor488)
Transform489 = x3d.Transform()
Transform489.translation = [0.0053,1.2679,-0.081]
Shape490 = x3d.Shape()
Shape490.USE = "HAnimJointShape"

Transform489.children.append(Shape490)

HAnimSegment487.children.append(Transform489)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vt11'/> to <HAnimJoint name='vt10'/>
Shape491 = x3d.Shape()
LineSet492 = x3d.LineSet()
LineSet492.vertexCount = [2]
Coordinate493 = x3d.Coordinate()

LineSet492.coord = Coordinate493
ColorRGBA494 = x3d.ColorRGBA()
ColorRGBA494.USE = "HAnimSegmentLineColorRGBA"

LineSet492.color = ColorRGBA494

Shape491.geometry = LineSet492

HAnimSegment487.children.append(Shape491)

HAnimJoint486.children.append(HAnimSegment487)
HAnimJoint495 = x3d.HAnimJoint()
HAnimJoint495.name = "vt10"
HAnimJoint495.DEF = "hanim_vt10"
HAnimJoint495.center = [0.0056,1.2848,-0.0822]
HAnimJoint495.ulimit = [0,0,0]
HAnimJoint495.llimit = [0,0,0]
HAnimSegment496 = x3d.HAnimSegment()
HAnimSegment496.name = "t10"
HAnimSegment496.DEF = "hanim_t10"
#<HAnimJoint name='vt10'/> visualization sphere is placed within <HAnimSegment name='t10'/>
TouchSensor497 = x3d.TouchSensor()
TouchSensor497.description = "HAnimJoint vt10, HAnimSegment t10"

HAnimSegment496.children.append(TouchSensor497)
Transform498 = x3d.Transform()
Transform498.translation = [0.0056,1.2848,-0.0822]
Shape499 = x3d.Shape()
Shape499.USE = "HAnimJointShape"

Transform498.children.append(Shape499)

HAnimSegment496.children.append(Transform498)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vt10'/> to <HAnimJoint name='vt9'/>
Shape500 = x3d.Shape()
LineSet501 = x3d.LineSet()
LineSet501.vertexCount = [2]
Coordinate502 = x3d.Coordinate()

LineSet501.coord = Coordinate502
ColorRGBA503 = x3d.ColorRGBA()
ColorRGBA503.USE = "HAnimSegmentLineColorRGBA"

LineSet501.color = ColorRGBA503

Shape500.geometry = LineSet501

HAnimSegment496.children.append(Shape500)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vt10'/> to <HAnimSite name='substernale'/>
Shape504 = x3d.Shape()
LineSet505 = x3d.LineSet()
LineSet505.vertexCount = [2]
Coordinate506 = x3d.Coordinate()

LineSet505.coord = Coordinate506
ColorRGBA507 = x3d.ColorRGBA()
ColorRGBA507.USE = "HAnimSiteLineColorRGBA"

LineSet505.color = ColorRGBA507

Shape504.geometry = LineSet505

HAnimSegment496.children.append(Shape504)
HAnimSite508 = x3d.HAnimSite()
HAnimSite508.name = "substernale_pt"
HAnimSite508.DEF = "hanim_substernale_pt"
HAnimSite508.translation = [0.0085,1.2995,0.1147]
#HAnimSite visualization shape
TouchSensor509 = x3d.TouchSensor()
TouchSensor509.description = "HAnimSite substernale"

HAnimSite508.children.append(TouchSensor509)
Shape510 = x3d.Shape()
Shape510.USE = "HAnimSiteShape"

HAnimSite508.children.append(Shape510)

HAnimSegment496.children.append(HAnimSite508)

HAnimJoint495.children.append(HAnimSegment496)
HAnimJoint511 = x3d.HAnimJoint()
HAnimJoint511.name = "vt9"
HAnimJoint511.DEF = "hanim_vt9"
HAnimJoint511.center = [0.0057,1.3126,-0.0838]
HAnimJoint511.ulimit = [0,0,0]
HAnimJoint511.llimit = [0,0,0]
HAnimSegment512 = x3d.HAnimSegment()
HAnimSegment512.name = "t9"
HAnimSegment512.DEF = "hanim_t9"
#<HAnimJoint name='vt9'/> visualization sphere is placed within <HAnimSegment name='t9'/>
TouchSensor513 = x3d.TouchSensor()
TouchSensor513.description = "HAnimJoint vt9, HAnimSegment t9"

HAnimSegment512.children.append(TouchSensor513)
Transform514 = x3d.Transform()
Transform514.translation = [0.0057,1.3126,-0.0838]
Shape515 = x3d.Shape()
Shape515.USE = "HAnimJointShape"

Transform514.children.append(Shape515)

HAnimSegment512.children.append(Transform514)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vt9'/> to <HAnimJoint name='vt8'/>
Shape516 = x3d.Shape()
LineSet517 = x3d.LineSet()
LineSet517.vertexCount = [2]
Coordinate518 = x3d.Coordinate()

LineSet517.coord = Coordinate518
ColorRGBA519 = x3d.ColorRGBA()
ColorRGBA519.USE = "HAnimSegmentLineColorRGBA"

LineSet517.color = ColorRGBA519

Shape516.geometry = LineSet517

HAnimSegment512.children.append(Shape516)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vt9'/> to <HAnimSite name='r_thelion'/>
Shape520 = x3d.Shape()
LineSet521 = x3d.LineSet()
LineSet521.vertexCount = [2]
Coordinate522 = x3d.Coordinate()

LineSet521.coord = Coordinate522
ColorRGBA523 = x3d.ColorRGBA()
ColorRGBA523.USE = "HAnimSiteLineColorRGBA"

LineSet521.color = ColorRGBA523

Shape520.geometry = LineSet521

HAnimSegment512.children.append(Shape520)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vt9'/> to <HAnimSite name='l_thelion'/>
Shape524 = x3d.Shape()
LineSet525 = x3d.LineSet()
LineSet525.vertexCount = [2]
Coordinate526 = x3d.Coordinate()

LineSet525.coord = Coordinate526
ColorRGBA527 = x3d.ColorRGBA()
ColorRGBA527.USE = "HAnimSiteLineColorRGBA"

LineSet525.color = ColorRGBA527

Shape524.geometry = LineSet525

HAnimSegment512.children.append(Shape524)
HAnimSite528 = x3d.HAnimSite()
HAnimSite528.name = "r_thelion_pt"
HAnimSite528.DEF = "hanim_r_thelion_pt"
HAnimSite528.translation = [-0.0736,1.3385,0.1217]
#HAnimSite visualization shape
TouchSensor529 = x3d.TouchSensor()
TouchSensor529.description = "HAnimSite r_thelion"

HAnimSite528.children.append(TouchSensor529)
Shape530 = x3d.Shape()
Shape530.USE = "HAnimSiteShape"

HAnimSite528.children.append(Shape530)

HAnimSegment512.children.append(HAnimSite528)
HAnimSite531 = x3d.HAnimSite()
HAnimSite531.name = "l_thelion_pt"
HAnimSite531.DEF = "hanim_l_thelion_pt"
HAnimSite531.translation = [0.0918,1.3382,0.1192]
#HAnimSite visualization shape
TouchSensor532 = x3d.TouchSensor()
TouchSensor532.description = "HAnimSite l_thelion"

HAnimSite531.children.append(TouchSensor532)
Shape533 = x3d.Shape()
Shape533.USE = "HAnimSiteShape"

HAnimSite531.children.append(Shape533)

HAnimSegment512.children.append(HAnimSite531)

HAnimJoint511.children.append(HAnimSegment512)
HAnimJoint534 = x3d.HAnimJoint()
HAnimJoint534.name = "vt8"
HAnimJoint534.DEF = "hanim_vt8"
HAnimJoint534.center = [0.0057,1.3382,-0.0845]
HAnimJoint534.ulimit = [0,0,0]
HAnimJoint534.llimit = [0,0,0]
HAnimSegment535 = x3d.HAnimSegment()
HAnimSegment535.name = "t8"
HAnimSegment535.DEF = "hanim_t8"
#<HAnimJoint name='vt8'/> visualization sphere is placed within <HAnimSegment name='t8'/>
TouchSensor536 = x3d.TouchSensor()
TouchSensor536.description = "HAnimJoint vt8, HAnimSegment t8"

HAnimSegment535.children.append(TouchSensor536)
Transform537 = x3d.Transform()
Transform537.translation = [0.0057,1.3382,-0.0845]
Shape538 = x3d.Shape()
Shape538.USE = "HAnimJointShape"

Transform537.children.append(Shape538)

HAnimSegment535.children.append(Transform537)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vt8'/> to <HAnimJoint name='vt7'/>
Shape539 = x3d.Shape()
LineSet540 = x3d.LineSet()
LineSet540.vertexCount = [2]
Coordinate541 = x3d.Coordinate()

LineSet540.coord = Coordinate541
ColorRGBA542 = x3d.ColorRGBA()
ColorRGBA542.USE = "HAnimSegmentLineColorRGBA"

LineSet540.color = ColorRGBA542

Shape539.geometry = LineSet540

HAnimSegment535.children.append(Shape539)

HAnimJoint534.children.append(HAnimSegment535)
HAnimJoint543 = x3d.HAnimJoint()
HAnimJoint543.name = "vt7"
HAnimJoint543.DEF = "hanim_vt7"
HAnimJoint543.center = [0.0058,1.3625,-0.0833]
HAnimJoint543.ulimit = [0,0,0]
HAnimJoint543.llimit = [0,0,0]
HAnimSegment544 = x3d.HAnimSegment()
HAnimSegment544.name = "t7"
HAnimSegment544.DEF = "hanim_t7"
#<HAnimJoint name='vt7'/> visualization sphere is placed within <HAnimSegment name='t7'/>
TouchSensor545 = x3d.TouchSensor()
TouchSensor545.description = "HAnimJoint vt7, HAnimSegment t7"

HAnimSegment544.children.append(TouchSensor545)
Transform546 = x3d.Transform()
Transform546.translation = [0.0058,1.3625,-0.0833]
Shape547 = x3d.Shape()
Shape547.USE = "HAnimJointShape"

Transform546.children.append(Shape547)

HAnimSegment544.children.append(Transform546)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vt7'/> to <HAnimJoint name='vt6'/>
Shape548 = x3d.Shape()
LineSet549 = x3d.LineSet()
LineSet549.vertexCount = [2]
Coordinate550 = x3d.Coordinate()

LineSet549.coord = Coordinate550
ColorRGBA551 = x3d.ColorRGBA()
ColorRGBA551.USE = "HAnimSegmentLineColorRGBA"

LineSet549.color = ColorRGBA551

Shape548.geometry = LineSet549

HAnimSegment544.children.append(Shape548)

HAnimJoint543.children.append(HAnimSegment544)
HAnimJoint552 = x3d.HAnimJoint()
HAnimJoint552.name = "vt6"
HAnimJoint552.DEF = "hanim_vt6"
HAnimJoint552.center = [0.0059,1.3866,-0.08]
HAnimJoint552.ulimit = [0,0,0]
HAnimJoint552.llimit = [0,0,0]
HAnimSegment553 = x3d.HAnimSegment()
HAnimSegment553.name = "t6"
HAnimSegment553.DEF = "hanim_t6"
#<HAnimJoint name='vt6'/> visualization sphere is placed within <HAnimSegment name='t6'/>
TouchSensor554 = x3d.TouchSensor()
TouchSensor554.description = "HAnimJoint vt6, HAnimSegment t6"

HAnimSegment553.children.append(TouchSensor554)
Transform555 = x3d.Transform()
Transform555.translation = [0.0059,1.3866,-0.08]
Shape556 = x3d.Shape()
Shape556.USE = "HAnimJointShape"

Transform555.children.append(Shape556)

HAnimSegment553.children.append(Transform555)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vt6'/> to <HAnimJoint name='vt5'/>
Shape557 = x3d.Shape()
LineSet558 = x3d.LineSet()
LineSet558.vertexCount = [2]
Coordinate559 = x3d.Coordinate()

LineSet558.coord = Coordinate559
ColorRGBA560 = x3d.ColorRGBA()
ColorRGBA560.USE = "HAnimSegmentLineColorRGBA"

LineSet558.color = ColorRGBA560

Shape557.geometry = LineSet558

HAnimSegment553.children.append(Shape557)

HAnimJoint552.children.append(HAnimSegment553)
HAnimJoint561 = x3d.HAnimJoint()
HAnimJoint561.name = "vt5"
HAnimJoint561.DEF = "hanim_vt5"
HAnimJoint561.center = [0.006,1.4102,-0.0745]
HAnimJoint561.ulimit = [0,0,0]
HAnimJoint561.llimit = [0,0,0]
HAnimSegment562 = x3d.HAnimSegment()
HAnimSegment562.name = "t5"
HAnimSegment562.DEF = "hanim_t5"
#<HAnimJoint name='vt5'/> visualization sphere is placed within <HAnimSegment name='t5'/>
TouchSensor563 = x3d.TouchSensor()
TouchSensor563.description = "HAnimJoint vt5, HAnimSegment t5"

HAnimSegment562.children.append(TouchSensor563)
Transform564 = x3d.Transform()
Transform564.translation = [0.006,1.4102,-0.0745]
Shape565 = x3d.Shape()
Shape565.USE = "HAnimJointShape"

Transform564.children.append(Shape565)

HAnimSegment562.children.append(Transform564)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vt5'/> to <HAnimJoint name='vt4'/>
Shape566 = x3d.Shape()
LineSet567 = x3d.LineSet()
LineSet567.vertexCount = [2]
Coordinate568 = x3d.Coordinate()

LineSet567.coord = Coordinate568
ColorRGBA569 = x3d.ColorRGBA()
ColorRGBA569.USE = "HAnimSegmentLineColorRGBA"

LineSet567.color = ColorRGBA569

Shape566.geometry = LineSet567

HAnimSegment562.children.append(Shape566)

HAnimJoint561.children.append(HAnimSegment562)
HAnimJoint570 = x3d.HAnimJoint()
HAnimJoint570.name = "vt4"
HAnimJoint570.DEF = "hanim_vt4"
HAnimJoint570.center = [0.0061,1.432,-0.0675]
HAnimJoint570.ulimit = [0,0,0]
HAnimJoint570.llimit = [0,0,0]
HAnimSegment571 = x3d.HAnimSegment()
HAnimSegment571.name = "t4"
HAnimSegment571.DEF = "hanim_t4"
#<HAnimJoint name='vt4'/> visualization sphere is placed within <HAnimSegment name='t4'/>
TouchSensor572 = x3d.TouchSensor()
TouchSensor572.description = "HAnimJoint vt4, HAnimSegment t4"

HAnimSegment571.children.append(TouchSensor572)
Transform573 = x3d.Transform()
Transform573.translation = [0.0061,1.432,-0.0675]
Shape574 = x3d.Shape()
Shape574.USE = "HAnimJointShape"

Transform573.children.append(Shape574)

HAnimSegment571.children.append(Transform573)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vt4'/> to <HAnimJoint name='vt3'/>
Shape575 = x3d.Shape()
LineSet576 = x3d.LineSet()
LineSet576.vertexCount = [2]
Coordinate577 = x3d.Coordinate()

LineSet576.coord = Coordinate577
ColorRGBA578 = x3d.ColorRGBA()
ColorRGBA578.USE = "HAnimSegmentLineColorRGBA"

LineSet576.color = ColorRGBA578

Shape575.geometry = LineSet576

HAnimSegment571.children.append(Shape575)

HAnimJoint570.children.append(HAnimSegment571)
HAnimJoint579 = x3d.HAnimJoint()
HAnimJoint579.name = "vt3"
HAnimJoint579.DEF = "hanim_vt3"
HAnimJoint579.center = [0.0062,1.4583,-0.057]
HAnimJoint579.ulimit = [0,0,0]
HAnimJoint579.llimit = [0,0,0]
HAnimSegment580 = x3d.HAnimSegment()
HAnimSegment580.name = "t3"
HAnimSegment580.DEF = "hanim_t3"
#<HAnimJoint name='vt3'/> visualization sphere is placed within <HAnimSegment name='t3'/>
TouchSensor581 = x3d.TouchSensor()
TouchSensor581.description = "HAnimJoint vt3, HAnimSegment t3"

HAnimSegment580.children.append(TouchSensor581)
Transform582 = x3d.Transform()
Transform582.translation = [0.0062,1.4583,-0.057]
Shape583 = x3d.Shape()
Shape583.USE = "HAnimJointShape"

Transform582.children.append(Shape583)

HAnimSegment580.children.append(Transform582)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vt3'/> to <HAnimJoint name='vt2'/>
Shape584 = x3d.Shape()
LineSet585 = x3d.LineSet()
LineSet585.vertexCount = [2]
Coordinate586 = x3d.Coordinate()

LineSet585.coord = Coordinate586
ColorRGBA587 = x3d.ColorRGBA()
ColorRGBA587.USE = "HAnimSegmentLineColorRGBA"

LineSet585.color = ColorRGBA587

Shape584.geometry = LineSet585

HAnimSegment580.children.append(Shape584)

HAnimJoint579.children.append(HAnimSegment580)
HAnimJoint588 = x3d.HAnimJoint()
HAnimJoint588.name = "vt2"
HAnimJoint588.DEF = "hanim_vt2"
HAnimJoint588.center = [0.0063,1.4761,-0.0484]
HAnimJoint588.ulimit = [0,0,0]
HAnimJoint588.llimit = [0,0,0]
HAnimSegment589 = x3d.HAnimSegment()
HAnimSegment589.name = "t2"
HAnimSegment589.DEF = "hanim_t2"
#<HAnimJoint name='vt2'/> visualization sphere is placed within <HAnimSegment name='t2'/>
TouchSensor590 = x3d.TouchSensor()
TouchSensor590.description = "HAnimJoint vt2, HAnimSegment t2"

HAnimSegment589.children.append(TouchSensor590)
Transform591 = x3d.Transform()
Transform591.translation = [0.0063,1.4761,-0.0484]
Shape592 = x3d.Shape()
Shape592.USE = "HAnimJointShape"

Transform591.children.append(Shape592)

HAnimSegment589.children.append(Transform591)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vt2'/> to <HAnimJoint name='vt1'/>
Shape593 = x3d.Shape()
LineSet594 = x3d.LineSet()
LineSet594.vertexCount = [2]
Coordinate595 = x3d.Coordinate()

LineSet594.coord = Coordinate595
ColorRGBA596 = x3d.ColorRGBA()
ColorRGBA596.USE = "HAnimSegmentLineColorRGBA"

LineSet594.color = ColorRGBA596

Shape593.geometry = LineSet594

HAnimSegment589.children.append(Shape593)

HAnimJoint588.children.append(HAnimSegment589)
HAnimJoint597 = x3d.HAnimJoint()
HAnimJoint597.name = "vt1"
HAnimJoint597.DEF = "hanim_vt1"
HAnimJoint597.center = [0.0065,1.4951,-0.0387]
HAnimJoint597.ulimit = [0,0,0]
HAnimJoint597.llimit = [0,0,0]
HAnimSegment598 = x3d.HAnimSegment()
HAnimSegment598.name = "t1"
HAnimSegment598.DEF = "hanim_t1"
#<HAnimJoint name='vt1'/> visualization sphere is placed within <HAnimSegment name='t1'/>
TouchSensor599 = x3d.TouchSensor()
TouchSensor599.description = "HAnimJoint vt1, HAnimSegment t1"

HAnimSegment598.children.append(TouchSensor599)
Transform600 = x3d.Transform()
Transform600.translation = [0.0065,1.4951,-0.0387]
Shape601 = x3d.Shape()
Shape601.USE = "HAnimJointShape"

Transform600.children.append(Shape601)

HAnimSegment598.children.append(Transform600)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vt1'/> to <HAnimJoint name='vc7'/>
Shape602 = x3d.Shape()
LineSet603 = x3d.LineSet()
LineSet603.vertexCount = [2]
Coordinate604 = x3d.Coordinate()

LineSet603.coord = Coordinate604
ColorRGBA605 = x3d.ColorRGBA()
ColorRGBA605.USE = "HAnimSegmentLineColorRGBA"

LineSet603.color = ColorRGBA605

Shape602.geometry = LineSet603

HAnimSegment598.children.append(Shape602)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vt1'/> to <HAnimJoint name='l_sternoclavicular'/>
Shape606 = x3d.Shape()
LineSet607 = x3d.LineSet()
LineSet607.vertexCount = [2]
Coordinate608 = x3d.Coordinate()

LineSet607.coord = Coordinate608
ColorRGBA609 = x3d.ColorRGBA()
ColorRGBA609.USE = "HAnimSegmentLineColorRGBA"

LineSet607.color = ColorRGBA609

Shape606.geometry = LineSet607

HAnimSegment598.children.append(Shape606)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vt1'/> to <HAnimJoint name='r_sternoclavicular'/>
Shape610 = x3d.Shape()
LineSet611 = x3d.LineSet()
LineSet611.vertexCount = [2]
Coordinate612 = x3d.Coordinate()

LineSet611.coord = Coordinate612
ColorRGBA613 = x3d.ColorRGBA()
ColorRGBA613.USE = "HAnimSegmentLineColorRGBA"

LineSet611.color = ColorRGBA613

Shape610.geometry = LineSet611

HAnimSegment598.children.append(Shape610)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vt1'/> to <HAnimSite name='suprasternale'/>
Shape614 = x3d.Shape()
LineSet615 = x3d.LineSet()
LineSet615.vertexCount = [2]
Coordinate616 = x3d.Coordinate()

LineSet615.coord = Coordinate616
ColorRGBA617 = x3d.ColorRGBA()
ColorRGBA617.USE = "HAnimSiteLineColorRGBA"

LineSet615.color = ColorRGBA617

Shape614.geometry = LineSet615

HAnimSegment598.children.append(Shape614)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vt1'/> to <HAnimSite name='cervicale'/>
Shape618 = x3d.Shape()
LineSet619 = x3d.LineSet()
LineSet619.vertexCount = [2]
Coordinate620 = x3d.Coordinate()

LineSet619.coord = Coordinate620
ColorRGBA621 = x3d.ColorRGBA()
ColorRGBA621.USE = "HAnimSiteLineColorRGBA"

LineSet619.color = ColorRGBA621

Shape618.geometry = LineSet619

HAnimSegment598.children.append(Shape618)
HAnimSite622 = x3d.HAnimSite()
HAnimSite622.name = "suprasternale_pt"
HAnimSite622.DEF = "hanim_suprasternale_pt"
HAnimSite622.translation = [0.0084,1.4714,0.0551]
#HAnimSite visualization shape
TouchSensor623 = x3d.TouchSensor()
TouchSensor623.description = "HAnimSite suprasternale"

HAnimSite622.children.append(TouchSensor623)
Shape624 = x3d.Shape()
Shape624.USE = "HAnimSiteShape"

HAnimSite622.children.append(Shape624)

HAnimSegment598.children.append(HAnimSite622)
HAnimSite625 = x3d.HAnimSite()
HAnimSite625.name = "cervicale_pt"
HAnimSite625.DEF = "hanim_cervicale_pt"
HAnimSite625.translation = [0.0064,1.52,-0.0815]
#HAnimSite visualization shape
TouchSensor626 = x3d.TouchSensor()
TouchSensor626.description = "HAnimSite cervicale"

HAnimSite625.children.append(TouchSensor626)
Shape627 = x3d.Shape()
Shape627.USE = "HAnimSiteShape"

HAnimSite625.children.append(Shape627)

HAnimSegment598.children.append(HAnimSite625)

HAnimJoint597.children.append(HAnimSegment598)
HAnimJoint628 = x3d.HAnimJoint()
HAnimJoint628.name = "vc7"
HAnimJoint628.DEF = "hanim_vc7"
HAnimJoint628.center = [0.0066,1.5132,-0.0301]
HAnimJoint628.ulimit = [0,0,0]
HAnimJoint628.llimit = [0,0,0]
HAnimSegment629 = x3d.HAnimSegment()
HAnimSegment629.name = "c7"
HAnimSegment629.DEF = "hanim_c7"
#<HAnimJoint name='vc7'/> visualization sphere is placed within <HAnimSegment name='c7'/>
TouchSensor630 = x3d.TouchSensor()
TouchSensor630.description = "HAnimJoint vc7, HAnimSegment c7"

HAnimSegment629.children.append(TouchSensor630)
Transform631 = x3d.Transform()
Transform631.translation = [0.0066,1.5132,-0.0301]
Shape632 = x3d.Shape()
Shape632.USE = "HAnimJointShape"

Transform631.children.append(Shape632)

HAnimSegment629.children.append(Transform631)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vc7'/> to <HAnimJoint name='vc6'/>
Shape633 = x3d.Shape()
LineSet634 = x3d.LineSet()
LineSet634.vertexCount = [2]
Coordinate635 = x3d.Coordinate()

LineSet634.coord = Coordinate635
ColorRGBA636 = x3d.ColorRGBA()
ColorRGBA636.USE = "HAnimSegmentLineColorRGBA"

LineSet634.color = ColorRGBA636

Shape633.geometry = LineSet634

HAnimSegment629.children.append(Shape633)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vc7'/> to <HAnimSite name='r_neck_base'/>
Shape637 = x3d.Shape()
LineSet638 = x3d.LineSet()
LineSet638.vertexCount = [2]
Coordinate639 = x3d.Coordinate()

LineSet638.coord = Coordinate639
ColorRGBA640 = x3d.ColorRGBA()
ColorRGBA640.USE = "HAnimSiteLineColorRGBA"

LineSet638.color = ColorRGBA640

Shape637.geometry = LineSet638

HAnimSegment629.children.append(Shape637)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='vc7'/> to <HAnimSite name='l_neck_base'/>
Shape641 = x3d.Shape()
LineSet642 = x3d.LineSet()
LineSet642.vertexCount = [2]
Coordinate643 = x3d.Coordinate()

LineSet642.coord = Coordinate643
ColorRGBA644 = x3d.ColorRGBA()
ColorRGBA644.USE = "HAnimSiteLineColorRGBA"

LineSet642.color = ColorRGBA644

Shape641.geometry = LineSet642

HAnimSegment629.children.append(Shape641)
HAnimSite645 = x3d.HAnimSite()
HAnimSite645.name = "r_neck_base_pt"
HAnimSite645.DEF = "hanim_r_neck_base_pt"
HAnimSite645.translation = [-0.0419,1.5149,-0.022]
#HAnimSite visualization shape
TouchSensor646 = x3d.TouchSensor()
TouchSensor646.description = "HAnimSite r_neck_base"

HAnimSite645.children.append(TouchSensor646)
Shape647 = x3d.Shape()
Shape647.USE = "HAnimSiteShape"

HAnimSite645.children.append(Shape647)

HAnimSegment629.children.append(HAnimSite645)
HAnimSite648 = x3d.HAnimSite()
HAnimSite648.name = "l_neck_base_pt"
HAnimSite648.DEF = "hanim_l_neck_base_pt"
HAnimSite648.translation = [0.0646,1.5141,-0.038]
#HAnimSite visualization shape
TouchSensor649 = x3d.TouchSensor()
TouchSensor649.description = "HAnimSite l_neck_base"

HAnimSite648.children.append(TouchSensor649)
Shape650 = x3d.Shape()
Shape650.USE = "HAnimSiteShape"

HAnimSite648.children.append(Shape650)

HAnimSegment629.children.append(HAnimSite648)

HAnimJoint628.children.append(HAnimSegment629)
HAnimJoint651 = x3d.HAnimJoint()
HAnimJoint651.name = "vc6"
HAnimJoint651.DEF = "hanim_vc6"
HAnimJoint651.center = [0.0066,1.5357,-0.0143]
HAnimJoint651.ulimit = [0,0,0]
HAnimJoint651.llimit = [0,0,0]
HAnimSegment652 = x3d.HAnimSegment()
HAnimSegment652.name = "c6"
HAnimSegment652.DEF = "hanim_c6"
#<HAnimJoint name='vc6'/> visualization sphere is placed within <HAnimSegment name='c6'/>
TouchSensor653 = x3d.TouchSensor()
TouchSensor653.description = "HAnimJoint vc6, HAnimSegment c6"

HAnimSegment652.children.append(TouchSensor653)
Transform654 = x3d.Transform()
Transform654.translation = [0.0066,1.5357,-0.0143]
Shape655 = x3d.Shape()
Shape655.USE = "HAnimJointShape"

Transform654.children.append(Shape655)

HAnimSegment652.children.append(Transform654)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vc6'/> to <HAnimJoint name='vc5'/>
Shape656 = x3d.Shape()
LineSet657 = x3d.LineSet()
LineSet657.vertexCount = [2]
Coordinate658 = x3d.Coordinate()

LineSet657.coord = Coordinate658
ColorRGBA659 = x3d.ColorRGBA()
ColorRGBA659.USE = "HAnimSegmentLineColorRGBA"

LineSet657.color = ColorRGBA659

Shape656.geometry = LineSet657

HAnimSegment652.children.append(Shape656)

HAnimJoint651.children.append(HAnimSegment652)
HAnimJoint660 = x3d.HAnimJoint()
HAnimJoint660.name = "vc5"
HAnimJoint660.DEF = "hanim_vc5"
HAnimJoint660.center = [0.0066,1.552,-0.0082]
HAnimJoint660.ulimit = [0,0,0]
HAnimJoint660.llimit = [0,0,0]
HAnimSegment661 = x3d.HAnimSegment()
HAnimSegment661.name = "c5"
HAnimSegment661.DEF = "hanim_c5"
#<HAnimJoint name='vc5'/> visualization sphere is placed within <HAnimSegment name='c5'/>
TouchSensor662 = x3d.TouchSensor()
TouchSensor662.description = "HAnimJoint vc5, HAnimSegment c5"

HAnimSegment661.children.append(TouchSensor662)
Transform663 = x3d.Transform()
Transform663.translation = [0.0066,1.552,-0.0082]
Shape664 = x3d.Shape()
Shape664.USE = "HAnimJointShape"

Transform663.children.append(Shape664)

HAnimSegment661.children.append(Transform663)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vc5'/> to <HAnimJoint name='vc4'/>
Shape665 = x3d.Shape()
LineSet666 = x3d.LineSet()
LineSet666.vertexCount = [2]
Coordinate667 = x3d.Coordinate()

LineSet666.coord = Coordinate667
ColorRGBA668 = x3d.ColorRGBA()
ColorRGBA668.USE = "HAnimSegmentLineColorRGBA"

LineSet666.color = ColorRGBA668

Shape665.geometry = LineSet666

HAnimSegment661.children.append(Shape665)

HAnimJoint660.children.append(HAnimSegment661)
HAnimJoint669 = x3d.HAnimJoint()
HAnimJoint669.name = "vc4"
HAnimJoint669.DEF = "hanim_vc4"
HAnimJoint669.center = [0.0066,1.5662,-0.0084]
HAnimJoint669.ulimit = [0,0,0]
HAnimJoint669.llimit = [0,0,0]
HAnimSegment670 = x3d.HAnimSegment()
HAnimSegment670.name = "c4"
HAnimSegment670.DEF = "hanim_c4"
#<HAnimJoint name='vc4'/> visualization sphere is placed within <HAnimSegment name='c4'/>
TouchSensor671 = x3d.TouchSensor()
TouchSensor671.description = "HAnimJoint vc4, HAnimSegment c4"

HAnimSegment670.children.append(TouchSensor671)
Transform672 = x3d.Transform()
Transform672.translation = [0.0066,1.5662,-0.0084]
Shape673 = x3d.Shape()
Shape673.USE = "HAnimJointShape"

Transform672.children.append(Shape673)

HAnimSegment670.children.append(Transform672)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vc4'/> to <HAnimJoint name='vc3'/>
Shape674 = x3d.Shape()
LineSet675 = x3d.LineSet()
LineSet675.vertexCount = [2]
Coordinate676 = x3d.Coordinate()

LineSet675.coord = Coordinate676
ColorRGBA677 = x3d.ColorRGBA()
ColorRGBA677.USE = "HAnimSegmentLineColorRGBA"

LineSet675.color = ColorRGBA677

Shape674.geometry = LineSet675

HAnimSegment670.children.append(Shape674)

HAnimJoint669.children.append(HAnimSegment670)
HAnimJoint678 = x3d.HAnimJoint()
HAnimJoint678.name = "vc3"
HAnimJoint678.DEF = "hanim_vc3"
HAnimJoint678.center = [0.0066,1.58,-0.0103]
HAnimJoint678.ulimit = [0,0,0]
HAnimJoint678.llimit = [0,0,0]
HAnimSegment679 = x3d.HAnimSegment()
HAnimSegment679.name = "c3"
HAnimSegment679.DEF = "hanim_c3"
#<HAnimJoint name='vc3'/> visualization sphere is placed within <HAnimSegment name='c3'/>
TouchSensor680 = x3d.TouchSensor()
TouchSensor680.description = "HAnimJoint vc3, HAnimSegment c3"

HAnimSegment679.children.append(TouchSensor680)
Transform681 = x3d.Transform()
Transform681.translation = [0.0066,1.58,-0.0103]
Shape682 = x3d.Shape()
Shape682.USE = "HAnimJointShape"

Transform681.children.append(Shape682)

HAnimSegment679.children.append(Transform681)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vc3'/> to <HAnimJoint name='vc2'/>
Shape683 = x3d.Shape()
LineSet684 = x3d.LineSet()
LineSet684.vertexCount = [2]
Coordinate685 = x3d.Coordinate()

LineSet684.coord = Coordinate685
ColorRGBA686 = x3d.ColorRGBA()
ColorRGBA686.USE = "HAnimSegmentLineColorRGBA"

LineSet684.color = ColorRGBA686

Shape683.geometry = LineSet684

HAnimSegment679.children.append(Shape683)

HAnimJoint678.children.append(HAnimSegment679)
HAnimJoint687 = x3d.HAnimJoint()
HAnimJoint687.name = "vc2"
HAnimJoint687.DEF = "hanim_vc2"
HAnimJoint687.center = [0.0066,1.5928,-0.0103]
HAnimJoint687.ulimit = [0,0,0]
HAnimJoint687.llimit = [0,0,0]
HAnimSegment688 = x3d.HAnimSegment()
HAnimSegment688.name = "c2"
HAnimSegment688.DEF = "hanim_c2"
#<HAnimJoint name='vc2'/> visualization sphere is placed within <HAnimSegment name='c2'/>
TouchSensor689 = x3d.TouchSensor()
TouchSensor689.description = "HAnimJoint vc2, HAnimSegment c2"

HAnimSegment688.children.append(TouchSensor689)
Transform690 = x3d.Transform()
Transform690.translation = [0.0066,1.5928,-0.0103]
Shape691 = x3d.Shape()
Shape691.USE = "HAnimJointShape"

Transform690.children.append(Shape691)

HAnimSegment688.children.append(Transform690)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vc2'/> to <HAnimJoint name='vc1'/>
Shape692 = x3d.Shape()
LineSet693 = x3d.LineSet()
LineSet693.vertexCount = [2]
Coordinate694 = x3d.Coordinate()

LineSet693.coord = Coordinate694
ColorRGBA695 = x3d.ColorRGBA()
ColorRGBA695.USE = "HAnimSegmentLineColorRGBA"

LineSet693.color = ColorRGBA695

Shape692.geometry = LineSet693

HAnimSegment688.children.append(Shape692)

HAnimJoint687.children.append(HAnimSegment688)
HAnimJoint696 = x3d.HAnimJoint()
HAnimJoint696.name = "vc1"
HAnimJoint696.DEF = "hanim_vc1"
HAnimJoint696.center = [0.0066,1.6144,-0.0034]
HAnimJoint696.ulimit = [0,0,0]
HAnimJoint696.llimit = [0,0,0]
HAnimSegment697 = x3d.HAnimSegment()
HAnimSegment697.name = "c1"
HAnimSegment697.DEF = "hanim_c1"
#<HAnimJoint name='vc1'/> visualization sphere is placed within <HAnimSegment name='c1'/>
TouchSensor698 = x3d.TouchSensor()
TouchSensor698.description = "HAnimJoint vc1, HAnimSegment c1"

HAnimSegment697.children.append(TouchSensor698)
Transform699 = x3d.Transform()
Transform699.translation = [0.0066,1.6144,-0.0034]
Shape700 = x3d.Shape()
Shape700.USE = "HAnimJointShape"

Transform699.children.append(Shape700)

HAnimSegment697.children.append(Transform699)
#HAnimSegment visualization line segment from parent <HAnimJoint name='vc1'/> to <HAnimJoint name='skullbase'/>
Shape701 = x3d.Shape()
LineSet702 = x3d.LineSet()
LineSet702.vertexCount = [2]
Coordinate703 = x3d.Coordinate()

LineSet702.coord = Coordinate703
ColorRGBA704 = x3d.ColorRGBA()
ColorRGBA704.USE = "HAnimSegmentLineColorRGBA"

LineSet702.color = ColorRGBA704

Shape701.geometry = LineSet702

HAnimSegment697.children.append(Shape701)

HAnimJoint696.children.append(HAnimSegment697)
HAnimJoint705 = x3d.HAnimJoint()
HAnimJoint705.name = "skullbase"
HAnimJoint705.DEF = "hanim_skullbase"
HAnimJoint705.center = [0.0044,1.6209,0.0236]
HAnimJoint705.ulimit = [0,0,0]
HAnimJoint705.llimit = [0,0,0]
HAnimSegment706 = x3d.HAnimSegment()
HAnimSegment706.name = "skull"
HAnimSegment706.DEF = "hanim_skull"
#<HAnimJoint name='skullbase'/> visualization sphere is placed within <HAnimSegment name='skull'/>
TouchSensor707 = x3d.TouchSensor()
TouchSensor707.description = "HAnimJoint skullbase, HAnimSegment skull"

HAnimSegment706.children.append(TouchSensor707)
Transform708 = x3d.Transform()
Transform708.translation = [0.0044,1.6209,0.0236]
Shape709 = x3d.Shape()
Shape709.USE = "HAnimJointShape"

Transform708.children.append(Shape709)

HAnimSegment706.children.append(Transform708)
#HAnimSegment visualization line segment from parent <HAnimJoint name='skullbase'/> to <HAnimJoint name='l_eyeball_joint'/>
Shape710 = x3d.Shape()
LineSet711 = x3d.LineSet()
LineSet711.vertexCount = [2]
Coordinate712 = x3d.Coordinate()

LineSet711.coord = Coordinate712
ColorRGBA713 = x3d.ColorRGBA()
ColorRGBA713.USE = "HAnimSegmentLineColorRGBA"

LineSet711.color = ColorRGBA713

Shape710.geometry = LineSet711

HAnimSegment706.children.append(Shape710)
#HAnimSegment visualization line segment from parent <HAnimJoint name='skullbase'/> to <HAnimJoint name='l_eyelid_joint'/>
Shape714 = x3d.Shape()
LineSet715 = x3d.LineSet()
LineSet715.vertexCount = [2]
Coordinate716 = x3d.Coordinate()

LineSet715.coord = Coordinate716
ColorRGBA717 = x3d.ColorRGBA()
ColorRGBA717.USE = "HAnimSegmentLineColorRGBA"

LineSet715.color = ColorRGBA717

Shape714.geometry = LineSet715

HAnimSegment706.children.append(Shape714)
#HAnimSegment visualization line segment from parent <HAnimJoint name='skullbase'/> to <HAnimJoint name='l_eyebrow_joint'/>
Shape718 = x3d.Shape()
LineSet719 = x3d.LineSet()
LineSet719.vertexCount = [2]
Coordinate720 = x3d.Coordinate()

LineSet719.coord = Coordinate720
ColorRGBA721 = x3d.ColorRGBA()
ColorRGBA721.USE = "HAnimSegmentLineColorRGBA"

LineSet719.color = ColorRGBA721

Shape718.geometry = LineSet719

HAnimSegment706.children.append(Shape718)
#HAnimSegment visualization line segment from parent <HAnimJoint name='skullbase'/> to <HAnimJoint name='r_eyeball_joint'/>
Shape722 = x3d.Shape()
LineSet723 = x3d.LineSet()
LineSet723.vertexCount = [2]
Coordinate724 = x3d.Coordinate()

LineSet723.coord = Coordinate724
ColorRGBA725 = x3d.ColorRGBA()
ColorRGBA725.USE = "HAnimSegmentLineColorRGBA"

LineSet723.color = ColorRGBA725

Shape722.geometry = LineSet723

HAnimSegment706.children.append(Shape722)
#HAnimSegment visualization line segment from parent <HAnimJoint name='skullbase'/> to <HAnimJoint name='r_eyelid_joint'/>
Shape726 = x3d.Shape()
LineSet727 = x3d.LineSet()
LineSet727.vertexCount = [2]
Coordinate728 = x3d.Coordinate()

LineSet727.coord = Coordinate728
ColorRGBA729 = x3d.ColorRGBA()
ColorRGBA729.USE = "HAnimSegmentLineColorRGBA"

LineSet727.color = ColorRGBA729

Shape726.geometry = LineSet727

HAnimSegment706.children.append(Shape726)
#HAnimSegment visualization line segment from parent <HAnimJoint name='skullbase'/> to <HAnimJoint name='r_eyebrow_joint'/>
Shape730 = x3d.Shape()
LineSet731 = x3d.LineSet()
LineSet731.vertexCount = [2]
Coordinate732 = x3d.Coordinate()

LineSet731.coord = Coordinate732
ColorRGBA733 = x3d.ColorRGBA()
ColorRGBA733.USE = "HAnimSegmentLineColorRGBA"

LineSet731.color = ColorRGBA733

Shape730.geometry = LineSet731

HAnimSegment706.children.append(Shape730)
#HAnimSegment visualization line segment from parent <HAnimJoint name='skullbase'/> to <HAnimJoint name='temporomandibular'/>
Shape734 = x3d.Shape()
LineSet735 = x3d.LineSet()
LineSet735.vertexCount = [2]
Coordinate736 = x3d.Coordinate()

LineSet735.coord = Coordinate736
ColorRGBA737 = x3d.ColorRGBA()
ColorRGBA737.USE = "HAnimSegmentLineColorRGBA"

LineSet735.color = ColorRGBA737

Shape734.geometry = LineSet735

HAnimSegment706.children.append(Shape734)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='skullbase'/> to <HAnimSite name='skull_tip'/>
Shape738 = x3d.Shape()
LineSet739 = x3d.LineSet()
LineSet739.vertexCount = [2]
Coordinate740 = x3d.Coordinate()

LineSet739.coord = Coordinate740
ColorRGBA741 = x3d.ColorRGBA()
ColorRGBA741.USE = "HAnimSiteLineColorRGBA"

LineSet739.color = ColorRGBA741

Shape738.geometry = LineSet739

HAnimSegment706.children.append(Shape738)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='skullbase'/> to <HAnimSite name='sellion'/>
Shape742 = x3d.Shape()
LineSet743 = x3d.LineSet()
LineSet743.vertexCount = [2]
Coordinate744 = x3d.Coordinate()

LineSet743.coord = Coordinate744
ColorRGBA745 = x3d.ColorRGBA()
ColorRGBA745.USE = "HAnimSiteLineColorRGBA"

LineSet743.color = ColorRGBA745

Shape742.geometry = LineSet743

HAnimSegment706.children.append(Shape742)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='skullbase'/> to <HAnimSite name='r_infraorbitale'/>
Shape746 = x3d.Shape()
LineSet747 = x3d.LineSet()
LineSet747.vertexCount = [2]
Coordinate748 = x3d.Coordinate()

LineSet747.coord = Coordinate748
ColorRGBA749 = x3d.ColorRGBA()
ColorRGBA749.USE = "HAnimSiteLineColorRGBA"

LineSet747.color = ColorRGBA749

Shape746.geometry = LineSet747

HAnimSegment706.children.append(Shape746)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='skullbase'/> to <HAnimSite name='l_infraorbitale'/>
Shape750 = x3d.Shape()
LineSet751 = x3d.LineSet()
LineSet751.vertexCount = [2]
Coordinate752 = x3d.Coordinate()

LineSet751.coord = Coordinate752
ColorRGBA753 = x3d.ColorRGBA()
ColorRGBA753.USE = "HAnimSiteLineColorRGBA"

LineSet751.color = ColorRGBA753

Shape750.geometry = LineSet751

HAnimSegment706.children.append(Shape750)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='skullbase'/> to <HAnimSite name='supramenton'/>
Shape754 = x3d.Shape()
LineSet755 = x3d.LineSet()
LineSet755.vertexCount = [2]
Coordinate756 = x3d.Coordinate()

LineSet755.coord = Coordinate756
ColorRGBA757 = x3d.ColorRGBA()
ColorRGBA757.USE = "HAnimSiteLineColorRGBA"

LineSet755.color = ColorRGBA757

Shape754.geometry = LineSet755

HAnimSegment706.children.append(Shape754)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='skullbase'/> to <HAnimSite name='r_tragion'/>
Shape758 = x3d.Shape()
LineSet759 = x3d.LineSet()
LineSet759.vertexCount = [2]
Coordinate760 = x3d.Coordinate()

LineSet759.coord = Coordinate760
ColorRGBA761 = x3d.ColorRGBA()
ColorRGBA761.USE = "HAnimSiteLineColorRGBA"

LineSet759.color = ColorRGBA761

Shape758.geometry = LineSet759

HAnimSegment706.children.append(Shape758)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='skullbase'/> to <HAnimSite name='r_gonion'/>
Shape762 = x3d.Shape()
LineSet763 = x3d.LineSet()
LineSet763.vertexCount = [2]
Coordinate764 = x3d.Coordinate()

LineSet763.coord = Coordinate764
ColorRGBA765 = x3d.ColorRGBA()
ColorRGBA765.USE = "HAnimSiteLineColorRGBA"

LineSet763.color = ColorRGBA765

Shape762.geometry = LineSet763

HAnimSegment706.children.append(Shape762)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='skullbase'/> to <HAnimSite name='l_tragion'/>
Shape766 = x3d.Shape()
LineSet767 = x3d.LineSet()
LineSet767.vertexCount = [2]
Coordinate768 = x3d.Coordinate()

LineSet767.coord = Coordinate768
ColorRGBA769 = x3d.ColorRGBA()
ColorRGBA769.USE = "HAnimSiteLineColorRGBA"

LineSet767.color = ColorRGBA769

Shape766.geometry = LineSet767

HAnimSegment706.children.append(Shape766)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='skullbase'/> to <HAnimSite name='l_gonion'/>
Shape770 = x3d.Shape()
LineSet771 = x3d.LineSet()
LineSet771.vertexCount = [2]
Coordinate772 = x3d.Coordinate()

LineSet771.coord = Coordinate772
ColorRGBA773 = x3d.ColorRGBA()
ColorRGBA773.USE = "HAnimSiteLineColorRGBA"

LineSet771.color = ColorRGBA773

Shape770.geometry = LineSet771

HAnimSegment706.children.append(Shape770)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='skullbase'/> to <HAnimSite name='nuchale'/>
Shape774 = x3d.Shape()
LineSet775 = x3d.LineSet()
LineSet775.vertexCount = [2]
Coordinate776 = x3d.Coordinate()

LineSet775.coord = Coordinate776
ColorRGBA777 = x3d.ColorRGBA()
ColorRGBA777.USE = "HAnimSiteLineColorRGBA"

LineSet775.color = ColorRGBA777

Shape774.geometry = LineSet775

HAnimSegment706.children.append(Shape774)
HAnimSite778 = x3d.HAnimSite()
HAnimSite778.name = "skull_tip"
HAnimSite778.DEF = "hanim_skull_tip"
HAnimSite778.translation = [0.005,1.7504,0.0055]
#TODO move skull_tip x to zero, check others for symmetry
#HAnimSite visualization shape
TouchSensor779 = x3d.TouchSensor()
TouchSensor779.description = "HAnimSite skull_tip"

HAnimSite778.children.append(TouchSensor779)
Shape780 = x3d.Shape()
Shape780.USE = "HAnimSiteShape"

HAnimSite778.children.append(Shape780)

HAnimSegment706.children.append(HAnimSite778)
HAnimSite781 = x3d.HAnimSite()
HAnimSite781.name = "sellion_pt"
HAnimSite781.DEF = "hanim_sellion_pt"
HAnimSite781.translation = [0.0058,1.6316,0.0852]
#HAnimSite visualization shape
TouchSensor782 = x3d.TouchSensor()
TouchSensor782.description = "HAnimSite sellion"

HAnimSite781.children.append(TouchSensor782)
Shape783 = x3d.Shape()
Shape783.USE = "HAnimSiteShape"

HAnimSite781.children.append(Shape783)

HAnimSegment706.children.append(HAnimSite781)
HAnimSite784 = x3d.HAnimSite()
HAnimSite784.name = "r_infraorbitale_pt"
HAnimSite784.DEF = "hanim_r_infraorbitale_pt"
HAnimSite784.translation = [-0.0237,1.6171,0.0752]
#HAnimSite visualization shape
TouchSensor785 = x3d.TouchSensor()
TouchSensor785.description = "HAnimSite r_infraorbitale"

HAnimSite784.children.append(TouchSensor785)
Shape786 = x3d.Shape()
Shape786.USE = "HAnimSiteShape"

HAnimSite784.children.append(Shape786)

HAnimSegment706.children.append(HAnimSite784)
HAnimSite787 = x3d.HAnimSite()
HAnimSite787.name = "l_infraorbitale_pt"
HAnimSite787.DEF = "hanim_l_infraorbitale_pt"
HAnimSite787.translation = [0.0341,1.6171,0.0752]
#HAnimSite visualization shape
TouchSensor788 = x3d.TouchSensor()
TouchSensor788.description = "HAnimSite l_infraorbitale"

HAnimSite787.children.append(TouchSensor788)
Shape789 = x3d.Shape()
Shape789.USE = "HAnimSiteShape"

HAnimSite787.children.append(Shape789)

HAnimSegment706.children.append(HAnimSite787)
HAnimSite790 = x3d.HAnimSite()
HAnimSite790.name = "supramenton_pt"
HAnimSite790.DEF = "hanim_supramenton_pt"
HAnimSite790.translation = [0.0061,1.541,0.0805]
#HAnimSite visualization shape
TouchSensor791 = x3d.TouchSensor()
TouchSensor791.description = "HAnimSite supramenton"

HAnimSite790.children.append(TouchSensor791)
Shape792 = x3d.Shape()
Shape792.USE = "HAnimSiteShape"

HAnimSite790.children.append(Shape792)

HAnimSegment706.children.append(HAnimSite790)
HAnimSite793 = x3d.HAnimSite()
HAnimSite793.name = "r_tragion_pt"
HAnimSite793.DEF = "hanim_r_tragion_pt"
HAnimSite793.translation = [-0.0646,1.6347,0.0302]
#HAnimSite visualization shape
TouchSensor794 = x3d.TouchSensor()
TouchSensor794.description = "HAnimSite r_tragion"

HAnimSite793.children.append(TouchSensor794)
Shape795 = x3d.Shape()
Shape795.USE = "HAnimSiteShape"

HAnimSite793.children.append(Shape795)

HAnimSegment706.children.append(HAnimSite793)
HAnimSite796 = x3d.HAnimSite()
HAnimSite796.name = "r_gonion_pt"
HAnimSite796.DEF = "hanim_r_gonion_pt"
HAnimSite796.translation = [-0.052,1.5529,0.0347]
#HAnimSite visualization shape
TouchSensor797 = x3d.TouchSensor()
TouchSensor797.description = "HAnimSite r_gonion"

HAnimSite796.children.append(TouchSensor797)
Shape798 = x3d.Shape()
Shape798.USE = "HAnimSiteShape"

HAnimSite796.children.append(Shape798)

HAnimSegment706.children.append(HAnimSite796)
HAnimSite799 = x3d.HAnimSite()
HAnimSite799.name = "l_tragion_pt"
HAnimSite799.DEF = "hanim_l_tragion_pt"
HAnimSite799.translation = [0.0739,1.6348,0.0282]
#HAnimSite visualization shape
TouchSensor800 = x3d.TouchSensor()
TouchSensor800.description = "HAnimSite l_tragion"

HAnimSite799.children.append(TouchSensor800)
Shape801 = x3d.Shape()
Shape801.USE = "HAnimSiteShape"

HAnimSite799.children.append(Shape801)

HAnimSegment706.children.append(HAnimSite799)
HAnimSite802 = x3d.HAnimSite()
HAnimSite802.name = "l_gonion_pt"
HAnimSite802.DEF = "hanim_l_gonion_pt"
HAnimSite802.translation = [0.0631,1.553,0.033]
#HAnimSite visualization shape
TouchSensor803 = x3d.TouchSensor()
TouchSensor803.description = "HAnimSite l_gonion"

HAnimSite802.children.append(TouchSensor803)
Shape804 = x3d.Shape()
Shape804.USE = "HAnimSiteShape"

HAnimSite802.children.append(Shape804)

HAnimSegment706.children.append(HAnimSite802)
HAnimSite805 = x3d.HAnimSite()
HAnimSite805.name = "nuchale_pt"
HAnimSite805.DEF = "hanim_nuchale_pt"
HAnimSite805.translation = [0.0039,1.5972,-0.0796]
#HAnimSite visualization shape
TouchSensor806 = x3d.TouchSensor()
TouchSensor806.description = "HAnimSite nuchale"

HAnimSite805.children.append(TouchSensor806)
Shape807 = x3d.Shape()
Shape807.USE = "HAnimSiteShape"

HAnimSite805.children.append(Shape807)

HAnimSegment706.children.append(HAnimSite805)

HAnimJoint705.children.append(HAnimSegment706)
HAnimJoint808 = x3d.HAnimJoint()
HAnimJoint808.name = "l_eyeball_joint"
HAnimJoint808.DEF = "hanim_l_eyeball_joint"
HAnimJoint808.center = [0.0336,1.6332,0.0502]
HAnimJoint808.ulimit = [0,0,0]
HAnimJoint808.llimit = [0,0,0]
HAnimSegment809 = x3d.HAnimSegment()
HAnimSegment809.name = "l_eyeball"
HAnimSegment809.DEF = "hanim_l_eyeball"
#<HAnimJoint name='l_eyeball_joint'/> visualization sphere is placed within <HAnimSegment name='l_eyeball'/>
TouchSensor810 = x3d.TouchSensor()
TouchSensor810.description = "HAnimJoint l_eyeball_joint, HAnimSegment l_eyeball"

HAnimSegment809.children.append(TouchSensor810)
Transform811 = x3d.Transform()
Transform811.translation = [0.0336,1.6332,0.0502]
Shape812 = x3d.Shape()
Shape812.USE = "HAnimJointShape"

Transform811.children.append(Shape812)

HAnimSegment809.children.append(Transform811)
#HAnimSite/Viewpoint visualization line segment from ancestor <HAnimJoint name='l_eyeball_joint'/> to <HAnimSite name='l_eyeball_site_view'/>
Shape813 = x3d.Shape()
LineSet814 = x3d.LineSet()
LineSet814.vertexCount = [2]
Coordinate815 = x3d.Coordinate()

LineSet814.coord = Coordinate815
ColorRGBA816 = x3d.ColorRGBA()
ColorRGBA816.DEF = "HAnimSiteViewpointLineColorRGBA"

LineSet814.color = ColorRGBA816

Shape813.geometry = LineSet814

HAnimSegment809.children.append(Shape813)
HAnimSite817 = x3d.HAnimSite()
HAnimSite817.name = "l_eyeball_site_view"
HAnimSite817.DEF = "hanim_l_eyeball_site_view"
HAnimSite817.translation = [0.034,1.64,0.05]
#HAnimSite visualization shape
TouchSensor818 = x3d.TouchSensor()
TouchSensor818.description = "HAnimSite l_eyeball_site_view"

HAnimSite817.children.append(TouchSensor818)
Shape819 = x3d.Shape()
Shape819.USE = "HAnimSiteShape"

HAnimSite817.children.append(Shape819)
Viewpoint820 = x3d.Viewpoint()
Viewpoint820.DEF = "hanim_l_eyeball_site_viewpoint"
Viewpoint820.description = "l_eyeball_site_viewpoint looking forward"
Viewpoint820.orientation = [0,1,0,3.141593]
Viewpoint820.position = [0,0,0]

HAnimSite817.children.append(Viewpoint820)
#HAnimSite/Viewpoint visualization shape
Anchor821 = x3d.Anchor()
Anchor821.description = "HAnimSite hanim_l_eyeball_site_view Viewpoint"
Anchor821.url = ["#hanim_l_eyeball_site_viewpoint"]
LOD822 = x3d.LOD()
LOD822.forceTransitions = True
LOD822.range = [0.04]
WorldInfo823 = x3d.WorldInfo()
WorldInfo823.info = ["hide diamond when close"]

LOD822.children.append(WorldInfo823)
Shape824 = x3d.Shape()
Shape824.DEF = "HAnimSiteViewpointShape"
IndexedFaceSet825 = x3d.IndexedFaceSet()
IndexedFaceSet825.DEF = "SiteViewpointDiamondIFS"
IndexedFaceSet825.coordIndex = [0,1,2,-1,0,2,3,-1,0,3,4,-1,0,4,1,-1,5,2,1,-1,5,3,2,-1,5,4,3,-1,5,1,4,-1]
IndexedFaceSet825.creaseAngle = 0.5
Coordinate826 = x3d.Coordinate()

IndexedFaceSet825.coord = Coordinate826

Shape824.geometry = IndexedFaceSet825
Appearance827 = x3d.Appearance()
Material828 = x3d.Material()
Material828.diffuseColor = [0,0,1]
Material828.transparency = 0.6

Appearance827.material = Material828

Shape824.appearance = Appearance827

LOD822.children.append(Shape824)

Anchor821.children.append(LOD822)

HAnimSite817.children.append(Anchor821)

HAnimSegment809.children.append(HAnimSite817)

HAnimJoint808.children.append(HAnimSegment809)

HAnimJoint705.children.append(HAnimJoint808)
HAnimJoint829 = x3d.HAnimJoint()
HAnimJoint829.name = "l_eyelid_joint"
HAnimJoint829.DEF = "hanim_l_eyelid_joint"
HAnimJoint829.center = [0.0336,1.6332,0.0502]
HAnimJoint829.ulimit = [0,0,0]
HAnimJoint829.llimit = [0,0,0]
HAnimSegment830 = x3d.HAnimSegment()
HAnimSegment830.name = "l_eyelid"
HAnimSegment830.DEF = "hanim_l_eyelid"
#<HAnimJoint name='l_eyelid_joint'/> visualization sphere is placed within <HAnimSegment name='l_eyelid'/>
TouchSensor831 = x3d.TouchSensor()
TouchSensor831.description = "HAnimJoint l_eyelid_joint, HAnimSegment l_eyelid"

HAnimSegment830.children.append(TouchSensor831)
Transform832 = x3d.Transform()
Transform832.translation = [0.0336,1.6332,0.0502]
Shape833 = x3d.Shape()
Shape833.USE = "HAnimJointShape"

Transform832.children.append(Shape833)

HAnimSegment830.children.append(Transform832)

HAnimJoint829.children.append(HAnimSegment830)

HAnimJoint705.children.append(HAnimJoint829)
HAnimJoint834 = x3d.HAnimJoint()
HAnimJoint834.name = "l_eyebrow_joint"
HAnimJoint834.DEF = "hanim_l_eyebrow_joint"
HAnimJoint834.center = [0.0336,1.635,0.0506]
HAnimJoint834.ulimit = [0,0,0]
HAnimJoint834.llimit = [0,0,0]
HAnimSegment835 = x3d.HAnimSegment()
HAnimSegment835.name = "l_eyebrow"
HAnimSegment835.DEF = "hanim_l_eyebrow"
#<HAnimJoint name='l_eyebrow_joint'/> visualization sphere is placed within <HAnimSegment name='l_eyebrow'/>
TouchSensor836 = x3d.TouchSensor()
TouchSensor836.description = "HAnimJoint l_eyebrow_joint, HAnimSegment l_eyebrow"

HAnimSegment835.children.append(TouchSensor836)
Transform837 = x3d.Transform()
Transform837.translation = [0.0336,1.635,0.0506]
Shape838 = x3d.Shape()
Shape838.USE = "HAnimJointShape"

Transform837.children.append(Shape838)

HAnimSegment835.children.append(Transform837)

HAnimJoint834.children.append(HAnimSegment835)

HAnimJoint705.children.append(HAnimJoint834)
HAnimJoint839 = x3d.HAnimJoint()
HAnimJoint839.name = "r_eyeball_joint"
HAnimJoint839.DEF = "hanim_r_eyeball_joint"
HAnimJoint839.center = [-0.0336,1.6332,0.0502]
HAnimJoint839.ulimit = [0,0,0]
HAnimJoint839.llimit = [0,0,0]
HAnimSegment840 = x3d.HAnimSegment()
HAnimSegment840.name = "r_eyeball"
HAnimSegment840.DEF = "hanim_r_eyeball"
#<HAnimJoint name='r_eyeball_joint'/> visualization sphere is placed within <HAnimSegment name='r_eyeball'/>
TouchSensor841 = x3d.TouchSensor()
TouchSensor841.description = "HAnimJoint r_eyeball_joint, HAnimSegment r_eyeball"

HAnimSegment840.children.append(TouchSensor841)
Transform842 = x3d.Transform()
Transform842.translation = [-0.0336,1.6332,0.0502]
Shape843 = x3d.Shape()
Shape843.USE = "HAnimJointShape"

Transform842.children.append(Shape843)

HAnimSegment840.children.append(Transform842)
#HAnimSite/Viewpoint visualization line segment from ancestor <HAnimJoint name='r_eyeball_joint'/> to <HAnimSite name='r_eyeball_site_view'/>
Shape844 = x3d.Shape()
LineSet845 = x3d.LineSet()
LineSet845.vertexCount = [2]
Coordinate846 = x3d.Coordinate()

LineSet845.coord = Coordinate846
ColorRGBA847 = x3d.ColorRGBA()
ColorRGBA847.USE = "HAnimSiteViewpointLineColorRGBA"

LineSet845.color = ColorRGBA847

Shape844.geometry = LineSet845

HAnimSegment840.children.append(Shape844)
HAnimSite848 = x3d.HAnimSite()
HAnimSite848.name = "r_eyeball_site_view"
HAnimSite848.DEF = "hanim_r_eyeball_site_view"
HAnimSite848.translation = [-0.034,1.64,0.05]
#HAnimSite visualization shape
TouchSensor849 = x3d.TouchSensor()
TouchSensor849.description = "HAnimSite r_eyeball_site_view"

HAnimSite848.children.append(TouchSensor849)
Shape850 = x3d.Shape()
Shape850.USE = "HAnimSiteShape"

HAnimSite848.children.append(Shape850)
Viewpoint851 = x3d.Viewpoint()
Viewpoint851.DEF = "hanim_r_eyeball_site_viewpoint"
Viewpoint851.description = "r_eyeball_site_viewpoint looking forward"
Viewpoint851.orientation = [0,1,0,3.141593]
Viewpoint851.position = [0,0,0]

HAnimSite848.children.append(Viewpoint851)
#HAnimSite/Viewpoint visualization shape
Anchor852 = x3d.Anchor()
Anchor852.description = "HAnimSite hanim_r_eyeball_site_view Viewpoint"
Anchor852.url = ["#hanim_r_eyeball_site_viewpoint"]
LOD853 = x3d.LOD()
LOD853.forceTransitions = True
LOD853.range = [0.04]
WorldInfo854 = x3d.WorldInfo()
WorldInfo854.info = ["hide diamond when close"]

LOD853.children.append(WorldInfo854)
Shape855 = x3d.Shape()
Shape855.USE = "HAnimSiteViewpointShape"

LOD853.children.append(Shape855)

Anchor852.children.append(LOD853)

HAnimSite848.children.append(Anchor852)

HAnimSegment840.children.append(HAnimSite848)

HAnimJoint839.children.append(HAnimSegment840)

HAnimJoint705.children.append(HAnimJoint839)
HAnimJoint856 = x3d.HAnimJoint()
HAnimJoint856.name = "r_eyelid_joint"
HAnimJoint856.DEF = "hanim_r_eyelid_joint"
HAnimJoint856.center = [-0.0336,1.6332,0.0502]
HAnimJoint856.ulimit = [0,0,0]
HAnimJoint856.llimit = [0,0,0]
HAnimSegment857 = x3d.HAnimSegment()
HAnimSegment857.name = "r_eyelid"
HAnimSegment857.DEF = "hanim_r_eyelid"
#<HAnimJoint name='r_eyelid_joint'/> visualization sphere is placed within <HAnimSegment name='r_eyelid'/>
TouchSensor858 = x3d.TouchSensor()
TouchSensor858.description = "HAnimJoint r_eyelid_joint, HAnimSegment r_eyelid"

HAnimSegment857.children.append(TouchSensor858)
Transform859 = x3d.Transform()
Transform859.translation = [-0.0336,1.6332,0.0502]
Shape860 = x3d.Shape()
Shape860.USE = "HAnimJointShape"

Transform859.children.append(Shape860)

HAnimSegment857.children.append(Transform859)

HAnimJoint856.children.append(HAnimSegment857)

HAnimJoint705.children.append(HAnimJoint856)
HAnimJoint861 = x3d.HAnimJoint()
HAnimJoint861.name = "r_eyebrow_joint"
HAnimJoint861.DEF = "hanim_r_eyebrow_joint"
HAnimJoint861.center = [-0.0336,1.635,0.0506]
HAnimJoint861.ulimit = [0,0,0]
HAnimJoint861.llimit = [0,0,0]
HAnimSegment862 = x3d.HAnimSegment()
HAnimSegment862.name = "r_eyebrow"
HAnimSegment862.DEF = "hanim_r_eyebrow"
#<HAnimJoint name='r_eyebrow_joint'/> visualization sphere is placed within <HAnimSegment name='r_eyebrow'/>
TouchSensor863 = x3d.TouchSensor()
TouchSensor863.description = "HAnimJoint r_eyebrow_joint, HAnimSegment r_eyebrow"

HAnimSegment862.children.append(TouchSensor863)
Transform864 = x3d.Transform()
Transform864.translation = [-0.0336,1.635,0.0506]
Shape865 = x3d.Shape()
Shape865.USE = "HAnimJointShape"

Transform864.children.append(Shape865)

HAnimSegment862.children.append(Transform864)

HAnimJoint861.children.append(HAnimSegment862)

HAnimJoint705.children.append(HAnimJoint861)
HAnimJoint866 = x3d.HAnimJoint()
HAnimJoint866.name = "temporomandibular"
HAnimJoint866.DEF = "hanim_temporomandibular"
HAnimJoint866.center = [0,1.63,0.015]
HAnimJoint866.ulimit = [0,0,0]
HAnimJoint866.llimit = [0,0,0]
#Single joint, single segment for jaw, two sites for left/right TMJs https://en.wikipedia.org/wiki/Temporomandibular_joint
HAnimSegment867 = x3d.HAnimSegment()
HAnimSegment867.name = "jaw"
HAnimSegment867.DEF = "hanim_jaw"
#<HAnimJoint name='temporomandibular'/> visualization sphere is placed within <HAnimSegment name='jaw'/>
TouchSensor868 = x3d.TouchSensor()
TouchSensor868.description = "HAnimJoint temporomandibular, HAnimSegment jaw"

HAnimSegment867.children.append(TouchSensor868)
Transform869 = x3d.Transform()
Transform869.translation = [0,1.63,0.015]
Shape870 = x3d.Shape()
Shape870.USE = "HAnimJointShape"

Transform869.children.append(Shape870)

HAnimSegment867.children.append(Transform869)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='temporomandibular'/> to <HAnimSite name='temporomandibular_l_site'/>
Shape871 = x3d.Shape()
LineSet872 = x3d.LineSet()
LineSet872.vertexCount = [2]
Coordinate873 = x3d.Coordinate()

LineSet872.coord = Coordinate873
ColorRGBA874 = x3d.ColorRGBA()
ColorRGBA874.USE = "HAnimSiteLineColorRGBA"

LineSet872.color = ColorRGBA874

Shape871.geometry = LineSet872

HAnimSegment867.children.append(Shape871)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='temporomandibular'/> to <HAnimSite name='temporomandibular_r_site'/>
Shape875 = x3d.Shape()
LineSet876 = x3d.LineSet()
LineSet876.vertexCount = [2]
Coordinate877 = x3d.Coordinate()

LineSet876.coord = Coordinate877
ColorRGBA878 = x3d.ColorRGBA()
ColorRGBA878.USE = "HAnimSiteLineColorRGBA"

LineSet876.color = ColorRGBA878

Shape875.geometry = LineSet876

HAnimSegment867.children.append(Shape875)
HAnimSite879 = x3d.HAnimSite()
HAnimSite879.name = "temporomandibular_l_site_pt"
HAnimSite879.DEF = "hanim_temporomandibular_l_site_pt"
HAnimSite879.translation = [0.045,1.63,0]
#HAnimSite visualization shape
TouchSensor880 = x3d.TouchSensor()
TouchSensor880.description = "HAnimSite temporomandibular_l_site"

HAnimSite879.children.append(TouchSensor880)
Shape881 = x3d.Shape()
Shape881.USE = "HAnimSiteShape"

HAnimSite879.children.append(Shape881)

HAnimSegment867.children.append(HAnimSite879)
HAnimSite882 = x3d.HAnimSite()
HAnimSite882.name = "temporomandibular_r_site_pt"
HAnimSite882.DEF = "hanim_temporomandibular_r_site_pt"
HAnimSite882.translation = [-0.045,1.63,0]
#HAnimSite visualization shape
TouchSensor883 = x3d.TouchSensor()
TouchSensor883.description = "HAnimSite temporomandibular_r_site"

HAnimSite882.children.append(TouchSensor883)
Shape884 = x3d.Shape()
Shape884.USE = "HAnimSiteShape"

HAnimSite882.children.append(Shape884)

HAnimSegment867.children.append(HAnimSite882)

HAnimJoint866.children.append(HAnimSegment867)

HAnimJoint705.children.append(HAnimJoint866)

HAnimJoint696.children.append(HAnimJoint705)

HAnimJoint687.children.append(HAnimJoint696)

HAnimJoint678.children.append(HAnimJoint687)

HAnimJoint669.children.append(HAnimJoint678)

HAnimJoint660.children.append(HAnimJoint669)

HAnimJoint651.children.append(HAnimJoint660)

HAnimJoint628.children.append(HAnimJoint651)

HAnimJoint597.children.append(HAnimJoint628)
HAnimJoint885 = x3d.HAnimJoint()
HAnimJoint885.name = "l_sternoclavicular"
HAnimJoint885.DEF = "hanim_l_sternoclavicular"
HAnimJoint885.center = [0.082,1.4488,-0.0353]
HAnimJoint885.ulimit = [0,0,0]
HAnimJoint885.llimit = [0,0,0]
HAnimSegment886 = x3d.HAnimSegment()
HAnimSegment886.name = "l_clavicle"
HAnimSegment886.DEF = "hanim_l_clavicle"
#<HAnimJoint name='l_sternoclavicular'/> visualization sphere is placed within <HAnimSegment name='l_clavicle'/>
TouchSensor887 = x3d.TouchSensor()
TouchSensor887.description = "HAnimJoint l_sternoclavicular, HAnimSegment l_clavicle"

HAnimSegment886.children.append(TouchSensor887)
Transform888 = x3d.Transform()
Transform888.translation = [0.082,1.4488,-0.0353]
Shape889 = x3d.Shape()
Shape889.USE = "HAnimJointShape"

Transform888.children.append(Shape889)

HAnimSegment886.children.append(Transform888)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_sternoclavicular'/> to <HAnimJoint name='l_acromioclavicular'/>
Shape890 = x3d.Shape()
LineSet891 = x3d.LineSet()
LineSet891.vertexCount = [2]
Coordinate892 = x3d.Coordinate()

LineSet891.coord = Coordinate892
ColorRGBA893 = x3d.ColorRGBA()
ColorRGBA893.USE = "HAnimSegmentLineColorRGBA"

LineSet891.color = ColorRGBA893

Shape890.geometry = LineSet891

HAnimSegment886.children.append(Shape890)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_sternoclavicular'/> to <HAnimSite name='l_clavicale'/>
Shape894 = x3d.Shape()
LineSet895 = x3d.LineSet()
LineSet895.vertexCount = [2]
Coordinate896 = x3d.Coordinate()

LineSet895.coord = Coordinate896
ColorRGBA897 = x3d.ColorRGBA()
ColorRGBA897.USE = "HAnimSiteLineColorRGBA"

LineSet895.color = ColorRGBA897

Shape894.geometry = LineSet895

HAnimSegment886.children.append(Shape894)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_sternoclavicular'/> to <HAnimSite name='l_acromion'/>
Shape898 = x3d.Shape()
LineSet899 = x3d.LineSet()
LineSet899.vertexCount = [2]
Coordinate900 = x3d.Coordinate()

LineSet899.coord = Coordinate900
ColorRGBA901 = x3d.ColorRGBA()
ColorRGBA901.USE = "HAnimSiteLineColorRGBA"

LineSet899.color = ColorRGBA901

Shape898.geometry = LineSet899

HAnimSegment886.children.append(Shape898)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_sternoclavicular'/> to <HAnimSite name='l_axilla_ant'/>
Shape902 = x3d.Shape()
LineSet903 = x3d.LineSet()
LineSet903.vertexCount = [2]
Coordinate904 = x3d.Coordinate()

LineSet903.coord = Coordinate904
ColorRGBA905 = x3d.ColorRGBA()
ColorRGBA905.USE = "HAnimSiteLineColorRGBA"

LineSet903.color = ColorRGBA905

Shape902.geometry = LineSet903

HAnimSegment886.children.append(Shape902)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_sternoclavicular'/> to <HAnimSite name='l_axilla_post'/>
Shape906 = x3d.Shape()
LineSet907 = x3d.LineSet()
LineSet907.vertexCount = [2]
Coordinate908 = x3d.Coordinate()

LineSet907.coord = Coordinate908
ColorRGBA909 = x3d.ColorRGBA()
ColorRGBA909.USE = "HAnimSiteLineColorRGBA"

LineSet907.color = ColorRGBA909

Shape906.geometry = LineSet907

HAnimSegment886.children.append(Shape906)
HAnimSite910 = x3d.HAnimSite()
HAnimSite910.name = "l_clavicale_pt"
HAnimSite910.DEF = "hanim_l_clavicale_pt"
HAnimSite910.translation = [0.0271,1.4943,0.0394]
#HAnimSite visualization shape
TouchSensor911 = x3d.TouchSensor()
TouchSensor911.description = "HAnimSite l_clavicale"

HAnimSite910.children.append(TouchSensor911)
Shape912 = x3d.Shape()
Shape912.USE = "HAnimSiteShape"

HAnimSite910.children.append(Shape912)

HAnimSegment886.children.append(HAnimSite910)
HAnimSite913 = x3d.HAnimSite()
HAnimSite913.name = "l_acromion_pt"
HAnimSite913.DEF = "hanim_l_acromion_pt"
HAnimSite913.translation = [0.2032,1.476,-0.049]
#HAnimSite visualization shape
TouchSensor914 = x3d.TouchSensor()
TouchSensor914.description = "HAnimSite l_acromion"

HAnimSite913.children.append(TouchSensor914)
Shape915 = x3d.Shape()
Shape915.USE = "HAnimSiteShape"

HAnimSite913.children.append(Shape915)

HAnimSegment886.children.append(HAnimSite913)
HAnimSite916 = x3d.HAnimSite()
HAnimSite916.name = "l_axilla_ant_pt"
HAnimSite916.DEF = "hanim_l_axilla_ant_pt"
HAnimSite916.translation = [0.1777,1.4065,-0.0075]
#HAnimSite visualization shape
TouchSensor917 = x3d.TouchSensor()
TouchSensor917.description = "HAnimSite l_axilla_ant"

HAnimSite916.children.append(TouchSensor917)
Shape918 = x3d.Shape()
Shape918.USE = "HAnimSiteShape"

HAnimSite916.children.append(Shape918)

HAnimSegment886.children.append(HAnimSite916)
HAnimSite919 = x3d.HAnimSite()
HAnimSite919.name = "l_axilla_post_pt"
HAnimSite919.DEF = "hanim_l_axilla_post_pt"
HAnimSite919.translation = [0.1706,1.4072,-0.0875]
#HAnimSite visualization shape
TouchSensor920 = x3d.TouchSensor()
TouchSensor920.description = "HAnimSite l_axilla_post"

HAnimSite919.children.append(TouchSensor920)
Shape921 = x3d.Shape()
Shape921.USE = "HAnimSiteShape"

HAnimSite919.children.append(Shape921)

HAnimSegment886.children.append(HAnimSite919)

HAnimJoint885.children.append(HAnimSegment886)
HAnimJoint922 = x3d.HAnimJoint()
HAnimJoint922.name = "l_acromioclavicular"
HAnimJoint922.DEF = "hanim_l_acromioclavicular"
HAnimJoint922.center = [0.0962,1.4269,-0.0424]
HAnimJoint922.ulimit = [0,0,0]
HAnimJoint922.llimit = [0,0,0]
HAnimSegment923 = x3d.HAnimSegment()
HAnimSegment923.name = "l_scapula"
HAnimSegment923.DEF = "hanim_l_scapula"
#<HAnimJoint name='l_acromioclavicular'/> visualization sphere is placed within <HAnimSegment name='l_scapula'/>
TouchSensor924 = x3d.TouchSensor()
TouchSensor924.description = "HAnimJoint l_acromioclavicular, HAnimSegment l_scapula"

HAnimSegment923.children.append(TouchSensor924)
Transform925 = x3d.Transform()
Transform925.translation = [0.0962,1.4269,-0.0424]
Shape926 = x3d.Shape()
Shape926.USE = "HAnimJointShape"

Transform925.children.append(Shape926)

HAnimSegment923.children.append(Transform925)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_acromioclavicular'/> to <HAnimJoint name='l_shoulder'/>
Shape927 = x3d.Shape()
LineSet928 = x3d.LineSet()
LineSet928.vertexCount = [2]
Coordinate929 = x3d.Coordinate()

LineSet928.coord = Coordinate929
ColorRGBA930 = x3d.ColorRGBA()
ColorRGBA930.USE = "HAnimSegmentLineColorRGBA"

LineSet928.color = ColorRGBA930

Shape927.geometry = LineSet928

HAnimSegment923.children.append(Shape927)

HAnimJoint922.children.append(HAnimSegment923)
HAnimJoint931 = x3d.HAnimJoint()
HAnimJoint931.name = "l_shoulder"
HAnimJoint931.DEF = "hanim_l_shoulder"
HAnimJoint931.center = [0.2029,1.4376,-0.0387]
HAnimJoint931.ulimit = [0,0,0]
HAnimJoint931.llimit = [0,0,0]
HAnimSegment932 = x3d.HAnimSegment()
HAnimSegment932.name = "l_upperarm"
HAnimSegment932.DEF = "hanim_l_upperarm"
#<HAnimJoint name='l_shoulder'/> visualization sphere is placed within <HAnimSegment name='l_upperarm'/>
TouchSensor933 = x3d.TouchSensor()
TouchSensor933.description = "HAnimJoint l_shoulder, HAnimSegment l_upperarm"

HAnimSegment932.children.append(TouchSensor933)
Transform934 = x3d.Transform()
Transform934.translation = [0.2029,1.4376,-0.0387]
Shape935 = x3d.Shape()
Shape935.USE = "HAnimJointShape"

Transform934.children.append(Shape935)

HAnimSegment932.children.append(Transform934)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_shoulder'/> to <HAnimJoint name='l_elbow'/>
Shape936 = x3d.Shape()
LineSet937 = x3d.LineSet()
LineSet937.vertexCount = [2]
Coordinate938 = x3d.Coordinate()

LineSet937.coord = Coordinate938
ColorRGBA939 = x3d.ColorRGBA()
ColorRGBA939.USE = "HAnimSegmentLineColorRGBA"

LineSet937.color = ColorRGBA939

Shape936.geometry = LineSet937

HAnimSegment932.children.append(Shape936)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_shoulder'/> to <HAnimSite name='l_humeral_lateral_epicn'/>
Shape940 = x3d.Shape()
LineSet941 = x3d.LineSet()
LineSet941.vertexCount = [2]
Coordinate942 = x3d.Coordinate()

LineSet941.coord = Coordinate942
ColorRGBA943 = x3d.ColorRGBA()
ColorRGBA943.USE = "HAnimSiteLineColorRGBA"

LineSet941.color = ColorRGBA943

Shape940.geometry = LineSet941

HAnimSegment932.children.append(Shape940)
HAnimSite944 = x3d.HAnimSite()
HAnimSite944.name = "l_humeral_lateral_epicn_pt"
HAnimSite944.DEF = "hanim_l_humeral_lateral_epicn_pt"
HAnimSite944.translation = [0.228,1.1482,-0.11]
#HAnimSite visualization shape
TouchSensor945 = x3d.TouchSensor()
TouchSensor945.description = "HAnimSite l_humeral_lateral_epicn"

HAnimSite944.children.append(TouchSensor945)
Shape946 = x3d.Shape()
Shape946.USE = "HAnimSiteShape"

HAnimSite944.children.append(Shape946)

HAnimSegment932.children.append(HAnimSite944)

HAnimJoint931.children.append(HAnimSegment932)
HAnimJoint947 = x3d.HAnimJoint()
HAnimJoint947.name = "l_elbow"
HAnimJoint947.DEF = "hanim_l_elbow"
HAnimJoint947.center = [0.2014,1.1357,-0.0682]
HAnimJoint947.ulimit = [0,0,0]
HAnimJoint947.llimit = [0,0,0]
HAnimSegment948 = x3d.HAnimSegment()
HAnimSegment948.name = "l_forearm"
HAnimSegment948.DEF = "hanim_l_forearm"
#<HAnimJoint name='l_elbow'/> visualization sphere is placed within <HAnimSegment name='l_forearm'/>
TouchSensor949 = x3d.TouchSensor()
TouchSensor949.description = "HAnimJoint l_elbow, HAnimSegment l_forearm"

HAnimSegment948.children.append(TouchSensor949)
Transform950 = x3d.Transform()
Transform950.translation = [0.2014,1.1357,-0.0682]
Shape951 = x3d.Shape()
Shape951.USE = "HAnimJointShape"

Transform950.children.append(Shape951)

HAnimSegment948.children.append(Transform950)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_elbow'/> to <HAnimJoint name='l_wrist'/>
Shape952 = x3d.Shape()
LineSet953 = x3d.LineSet()
LineSet953.vertexCount = [2]
Coordinate954 = x3d.Coordinate()

LineSet953.coord = Coordinate954
ColorRGBA955 = x3d.ColorRGBA()
ColorRGBA955.USE = "HAnimSegmentLineColorRGBA"

LineSet953.color = ColorRGBA955

Shape952.geometry = LineSet953

HAnimSegment948.children.append(Shape952)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_elbow'/> to <HAnimSite name='l_radial_styloid'/>
Shape956 = x3d.Shape()
LineSet957 = x3d.LineSet()
LineSet957.vertexCount = [2]
Coordinate958 = x3d.Coordinate()

LineSet957.coord = Coordinate958
ColorRGBA959 = x3d.ColorRGBA()
ColorRGBA959.USE = "HAnimSiteLineColorRGBA"

LineSet957.color = ColorRGBA959

Shape956.geometry = LineSet957

HAnimSegment948.children.append(Shape956)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_elbow'/> to <HAnimSite name='l_olecranon'/>
Shape960 = x3d.Shape()
LineSet961 = x3d.LineSet()
LineSet961.vertexCount = [2]
Coordinate962 = x3d.Coordinate()

LineSet961.coord = Coordinate962
ColorRGBA963 = x3d.ColorRGBA()
ColorRGBA963.USE = "HAnimSiteLineColorRGBA"

LineSet961.color = ColorRGBA963

Shape960.geometry = LineSet961

HAnimSegment948.children.append(Shape960)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_elbow'/> to <HAnimSite name='l_humeral_medial_epicn'/>
Shape964 = x3d.Shape()
LineSet965 = x3d.LineSet()
LineSet965.vertexCount = [2]
Coordinate966 = x3d.Coordinate()

LineSet965.coord = Coordinate966
ColorRGBA967 = x3d.ColorRGBA()
ColorRGBA967.USE = "HAnimSiteLineColorRGBA"

LineSet965.color = ColorRGBA967

Shape964.geometry = LineSet965

HAnimSegment948.children.append(Shape964)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_elbow'/> to <HAnimSite name='l_radiale'/>
Shape968 = x3d.Shape()
LineSet969 = x3d.LineSet()
LineSet969.vertexCount = [2]
Coordinate970 = x3d.Coordinate()

LineSet969.coord = Coordinate970
ColorRGBA971 = x3d.ColorRGBA()
ColorRGBA971.USE = "HAnimSiteLineColorRGBA"

LineSet969.color = ColorRGBA971

Shape968.geometry = LineSet969

HAnimSegment948.children.append(Shape968)
HAnimSite972 = x3d.HAnimSite()
HAnimSite972.name = "l_radial_styloid_pt"
HAnimSite972.DEF = "hanim_l_radial_styloid_pt"
HAnimSite972.translation = [0.1901,0.8645,-0.0415]
#HAnimSite visualization shape
TouchSensor973 = x3d.TouchSensor()
TouchSensor973.description = "HAnimSite l_radial_styloid"

HAnimSite972.children.append(TouchSensor973)
Shape974 = x3d.Shape()
Shape974.USE = "HAnimSiteShape"

HAnimSite972.children.append(Shape974)

HAnimSegment948.children.append(HAnimSite972)
HAnimSite975 = x3d.HAnimSite()
HAnimSite975.name = "l_olecranon_pt"
HAnimSite975.DEF = "hanim_l_olecranon_pt"
HAnimSite975.translation = [0.1962,1.1375,-0.1123]
#HAnimSite visualization shape
TouchSensor976 = x3d.TouchSensor()
TouchSensor976.description = "HAnimSite l_olecranon"

HAnimSite975.children.append(TouchSensor976)
Shape977 = x3d.Shape()
Shape977.USE = "HAnimSiteShape"

HAnimSite975.children.append(Shape977)

HAnimSegment948.children.append(HAnimSite975)
HAnimSite978 = x3d.HAnimSite()
HAnimSite978.name = "l_humeral_medial_epicn_pt"
HAnimSite978.DEF = "hanim_l_humeral_medial_epicn_pt"
HAnimSite978.translation = [0.1735,1.1272,-0.1113]
#HAnimSite visualization shape
TouchSensor979 = x3d.TouchSensor()
TouchSensor979.description = "HAnimSite l_humeral_medial_epicn"

HAnimSite978.children.append(TouchSensor979)
Shape980 = x3d.Shape()
Shape980.USE = "HAnimSiteShape"

HAnimSite978.children.append(Shape980)

HAnimSegment948.children.append(HAnimSite978)
HAnimSite981 = x3d.HAnimSite()
HAnimSite981.name = "l_radiale_pt"
HAnimSite981.DEF = "hanim_l_radiale_pt"
HAnimSite981.translation = [0.2182,1.1212,-0.1167]
#HAnimSite visualization shape
TouchSensor982 = x3d.TouchSensor()
TouchSensor982.description = "HAnimSite l_radiale"

HAnimSite981.children.append(TouchSensor982)
Shape983 = x3d.Shape()
Shape983.USE = "HAnimSiteShape"

HAnimSite981.children.append(Shape983)

HAnimSegment948.children.append(HAnimSite981)

HAnimJoint947.children.append(HAnimSegment948)
HAnimJoint984 = x3d.HAnimJoint()
HAnimJoint984.name = "l_wrist"
HAnimJoint984.DEF = "hanim_l_wrist"
HAnimJoint984.center = [0.1984,0.8663,-0.0583]
HAnimJoint984.ulimit = [0,0,0]
HAnimJoint984.llimit = [0,0,0]
HAnimSegment985 = x3d.HAnimSegment()
HAnimSegment985.name = "l_hand"
HAnimSegment985.DEF = "hanim_l_hand"
#<HAnimJoint name='l_wrist'/> visualization sphere is placed within <HAnimSegment name='l_hand'/>
TouchSensor986 = x3d.TouchSensor()
TouchSensor986.description = "HAnimJoint l_wrist, HAnimSegment l_hand"

HAnimSegment985.children.append(TouchSensor986)
Transform987 = x3d.Transform()
Transform987.translation = [0.1984,0.8663,-0.0583]
Shape988 = x3d.Shape()
Shape988.USE = "HAnimJointShape"

Transform987.children.append(Shape988)

HAnimSegment985.children.append(Transform987)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_wrist'/> to <HAnimJoint name='l_thumb1'/>
Shape989 = x3d.Shape()
LineSet990 = x3d.LineSet()
LineSet990.vertexCount = [2]
Coordinate991 = x3d.Coordinate()

LineSet990.coord = Coordinate991
ColorRGBA992 = x3d.ColorRGBA()
ColorRGBA992.USE = "HAnimSegmentLineColorRGBA"

LineSet990.color = ColorRGBA992

Shape989.geometry = LineSet990

HAnimSegment985.children.append(Shape989)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_wrist'/> to <HAnimJoint name='l_index0'/>
Shape993 = x3d.Shape()
LineSet994 = x3d.LineSet()
LineSet994.vertexCount = [2]
Coordinate995 = x3d.Coordinate()

LineSet994.coord = Coordinate995
ColorRGBA996 = x3d.ColorRGBA()
ColorRGBA996.USE = "HAnimSegmentLineColorRGBA"

LineSet994.color = ColorRGBA996

Shape993.geometry = LineSet994

HAnimSegment985.children.append(Shape993)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_wrist'/> to <HAnimJoint name='l_middle0'/>
Shape997 = x3d.Shape()
LineSet998 = x3d.LineSet()
LineSet998.vertexCount = [2]
Coordinate999 = x3d.Coordinate()

LineSet998.coord = Coordinate999
ColorRGBA1000 = x3d.ColorRGBA()
ColorRGBA1000.USE = "HAnimSegmentLineColorRGBA"

LineSet998.color = ColorRGBA1000

Shape997.geometry = LineSet998

HAnimSegment985.children.append(Shape997)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_wrist'/> to <HAnimJoint name='l_ring0'/>
Shape1001 = x3d.Shape()
LineSet1002 = x3d.LineSet()
LineSet1002.vertexCount = [2]
Coordinate1003 = x3d.Coordinate()

LineSet1002.coord = Coordinate1003
ColorRGBA1004 = x3d.ColorRGBA()
ColorRGBA1004.USE = "HAnimSegmentLineColorRGBA"

LineSet1002.color = ColorRGBA1004

Shape1001.geometry = LineSet1002

HAnimSegment985.children.append(Shape1001)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_wrist'/> to <HAnimJoint name='l_pinky0'/>
Shape1005 = x3d.Shape()
LineSet1006 = x3d.LineSet()
LineSet1006.vertexCount = [2]
Coordinate1007 = x3d.Coordinate()

LineSet1006.coord = Coordinate1007
ColorRGBA1008 = x3d.ColorRGBA()
ColorRGBA1008.USE = "HAnimSegmentLineColorRGBA"

LineSet1006.color = ColorRGBA1008

Shape1005.geometry = LineSet1006

HAnimSegment985.children.append(Shape1005)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_wrist'/> to <HAnimSite name='l_metacarpal_pha2'/>
Shape1009 = x3d.Shape()
LineSet1010 = x3d.LineSet()
LineSet1010.vertexCount = [2]
Coordinate1011 = x3d.Coordinate()

LineSet1010.coord = Coordinate1011
ColorRGBA1012 = x3d.ColorRGBA()
ColorRGBA1012.USE = "HAnimSiteLineColorRGBA"

LineSet1010.color = ColorRGBA1012

Shape1009.geometry = LineSet1010

HAnimSegment985.children.append(Shape1009)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_wrist'/> to <HAnimSite name='l_ulnar_styloid'/>
Shape1013 = x3d.Shape()
LineSet1014 = x3d.LineSet()
LineSet1014.vertexCount = [2]
Coordinate1015 = x3d.Coordinate()

LineSet1014.coord = Coordinate1015
ColorRGBA1016 = x3d.ColorRGBA()
ColorRGBA1016.USE = "HAnimSiteLineColorRGBA"

LineSet1014.color = ColorRGBA1016

Shape1013.geometry = LineSet1014

HAnimSegment985.children.append(Shape1013)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_wrist'/> to <HAnimSite name='l_metacarpal_pha5'/>
Shape1017 = x3d.Shape()
LineSet1018 = x3d.LineSet()
LineSet1018.vertexCount = [2]
Coordinate1019 = x3d.Coordinate()

LineSet1018.coord = Coordinate1019
ColorRGBA1020 = x3d.ColorRGBA()
ColorRGBA1020.USE = "HAnimSiteLineColorRGBA"

LineSet1018.color = ColorRGBA1020

Shape1017.geometry = LineSet1018

HAnimSegment985.children.append(Shape1017)
#HAnimSite/Viewpoint visualization line segment from ancestor <HAnimJoint name='l_wrist'/> to <HAnimSite name='l_hand_front_view'/>
Shape1021 = x3d.Shape()
LineSet1022 = x3d.LineSet()
LineSet1022.vertexCount = [2]
Coordinate1023 = x3d.Coordinate()

LineSet1022.coord = Coordinate1023
ColorRGBA1024 = x3d.ColorRGBA()
ColorRGBA1024.USE = "HAnimSiteViewpointLineColorRGBA"

LineSet1022.color = ColorRGBA1024

Shape1021.geometry = LineSet1022

HAnimSegment985.children.append(Shape1021)
HAnimSite1025 = x3d.HAnimSite()
HAnimSite1025.name = "l_metacarpal_pha2_pt"
HAnimSite1025.DEF = "hanim_l_metacarpal_pha2_pt"
HAnimSite1025.translation = [0.2009,0.8139,-0.0237]
#HAnimSite visualization shape
TouchSensor1026 = x3d.TouchSensor()
TouchSensor1026.description = "HAnimSite l_metacarpal_pha2"

HAnimSite1025.children.append(TouchSensor1026)
Shape1027 = x3d.Shape()
Shape1027.USE = "HAnimSiteShape"

HAnimSite1025.children.append(Shape1027)

HAnimSegment985.children.append(HAnimSite1025)
HAnimSite1028 = x3d.HAnimSite()
HAnimSite1028.name = "l_ulnar_styloid_pt"
HAnimSite1028.DEF = "hanim_l_ulnar_styloid_pt"
HAnimSite1028.translation = [0.2142,0.8529,-0.0648]
#HAnimSite visualization shape
TouchSensor1029 = x3d.TouchSensor()
TouchSensor1029.description = "HAnimSite l_ulnar_styloid"

HAnimSite1028.children.append(TouchSensor1029)
Shape1030 = x3d.Shape()
Shape1030.USE = "HAnimSiteShape"

HAnimSite1028.children.append(Shape1030)

HAnimSegment985.children.append(HAnimSite1028)
HAnimSite1031 = x3d.HAnimSite()
HAnimSite1031.name = "l_metacarpal_pha5_pt"
HAnimSite1031.DEF = "hanim_l_metacarpal_pha5_pt"
HAnimSite1031.translation = [0.1929,0.786,-0.1122]
#HAnimSite visualization shape
TouchSensor1032 = x3d.TouchSensor()
TouchSensor1032.description = "HAnimSite l_metacarpal_pha5"

HAnimSite1031.children.append(TouchSensor1032)
Shape1033 = x3d.Shape()
Shape1033.USE = "HAnimSiteShape"

HAnimSite1031.children.append(Shape1033)

HAnimSegment985.children.append(HAnimSite1031)
HAnimSite1034 = x3d.HAnimSite()
HAnimSite1034.name = "l_hand_front_view"
HAnimSite1034.DEF = "hanim_l_hand_front_view"
HAnimSite1034.translation = [0.3,0.75,0.45]
#HAnimSite visualization shape
TouchSensor1035 = x3d.TouchSensor()
TouchSensor1035.description = "HAnimSite l_hand_front_view"

HAnimSite1034.children.append(TouchSensor1035)
Shape1036 = x3d.Shape()
Shape1036.USE = "HAnimSiteShape"

HAnimSite1034.children.append(Shape1036)
Viewpoint1037 = x3d.Viewpoint()
Viewpoint1037.DEF = "hanim_l_hand_front_viewpoint"
Viewpoint1037.centerOfRotation = [0,0.7,0]
Viewpoint1037.description = "left hand front"
Viewpoint1037.position = [0,0,0]

HAnimSite1034.children.append(Viewpoint1037)
#HAnimSite/Viewpoint visualization shape
Anchor1038 = x3d.Anchor()
Anchor1038.description = "HAnimSite hanim_l_hand_front_view Viewpoint"
Anchor1038.url = ["#hanim_l_hand_front_viewpoint"]
LOD1039 = x3d.LOD()
LOD1039.forceTransitions = True
LOD1039.range = [0.04]
WorldInfo1040 = x3d.WorldInfo()
WorldInfo1040.info = ["hide diamond when close"]

LOD1039.children.append(WorldInfo1040)
Shape1041 = x3d.Shape()
Shape1041.USE = "HAnimSiteViewpointShape"

LOD1039.children.append(Shape1041)

Anchor1038.children.append(LOD1039)

HAnimSite1034.children.append(Anchor1038)

HAnimSegment985.children.append(HAnimSite1034)

HAnimJoint984.children.append(HAnimSegment985)
HAnimJoint1042 = x3d.HAnimJoint()
HAnimJoint1042.name = "l_thumb1"
HAnimJoint1042.DEF = "hanim_l_thumb1"
HAnimJoint1042.center = [0.1924,0.8472,-0.0534]
HAnimJoint1042.ulimit = [0,0,0]
HAnimJoint1042.llimit = [0,0,0]
HAnimSegment1043 = x3d.HAnimSegment()
HAnimSegment1043.name = "l_thumb_metacarpal"
HAnimSegment1043.DEF = "hanim_l_thumb_metacarpal"
#<HAnimJoint name='l_thumb1'/> visualization sphere is placed within <HAnimSegment name='l_thumb_metacarpal'/>
TouchSensor1044 = x3d.TouchSensor()
TouchSensor1044.description = "HAnimJoint l_thumb1, HAnimSegment l_thumb_metacarpal"

HAnimSegment1043.children.append(TouchSensor1044)
Transform1045 = x3d.Transform()
Transform1045.translation = [0.1924,0.8472,-0.0534]
Shape1046 = x3d.Shape()
Shape1046.USE = "HAnimJointShape"

Transform1045.children.append(Shape1046)

HAnimSegment1043.children.append(Transform1045)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_thumb1'/> to <HAnimJoint name='l_thumb2'/>
Shape1047 = x3d.Shape()
LineSet1048 = x3d.LineSet()
LineSet1048.vertexCount = [2]
Coordinate1049 = x3d.Coordinate()

LineSet1048.coord = Coordinate1049
ColorRGBA1050 = x3d.ColorRGBA()
ColorRGBA1050.USE = "HAnimSegmentLineColorRGBA"

LineSet1048.color = ColorRGBA1050

Shape1047.geometry = LineSet1048

HAnimSegment1043.children.append(Shape1047)

HAnimJoint1042.children.append(HAnimSegment1043)
HAnimJoint1051 = x3d.HAnimJoint()
HAnimJoint1051.name = "l_thumb2"
HAnimJoint1051.DEF = "hanim_l_thumb2"
HAnimJoint1051.center = [0.1951,0.8226,0.0246]
HAnimJoint1051.ulimit = [0,0,0]
HAnimJoint1051.llimit = [0,0,0]
HAnimSegment1052 = x3d.HAnimSegment()
HAnimSegment1052.name = "l_thumb_proximal"
HAnimSegment1052.DEF = "hanim_l_thumb_proximal"
#<HAnimJoint name='l_thumb2'/> visualization sphere is placed within <HAnimSegment name='l_thumb_proximal'/>
TouchSensor1053 = x3d.TouchSensor()
TouchSensor1053.description = "HAnimJoint l_thumb2, HAnimSegment l_thumb_proximal"

HAnimSegment1052.children.append(TouchSensor1053)
Transform1054 = x3d.Transform()
Transform1054.translation = [0.1951,0.8226,0.0246]
Shape1055 = x3d.Shape()
Shape1055.USE = "HAnimJointShape"

Transform1054.children.append(Shape1055)

HAnimSegment1052.children.append(Transform1054)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_thumb2'/> to <HAnimJoint name='l_thumb3'/>
Shape1056 = x3d.Shape()
LineSet1057 = x3d.LineSet()
LineSet1057.vertexCount = [2]
Coordinate1058 = x3d.Coordinate()

LineSet1057.coord = Coordinate1058
ColorRGBA1059 = x3d.ColorRGBA()
ColorRGBA1059.USE = "HAnimSegmentLineColorRGBA"

LineSet1057.color = ColorRGBA1059

Shape1056.geometry = LineSet1057

HAnimSegment1052.children.append(Shape1056)

HAnimJoint1051.children.append(HAnimSegment1052)
HAnimJoint1060 = x3d.HAnimJoint()
HAnimJoint1060.name = "l_thumb3"
HAnimJoint1060.DEF = "hanim_l_thumb3"
HAnimJoint1060.center = [0.1955,0.8159,0.0464]
HAnimJoint1060.ulimit = [0,0,0]
HAnimJoint1060.llimit = [0,0,0]
HAnimSegment1061 = x3d.HAnimSegment()
HAnimSegment1061.name = "l_thumb_distal"
HAnimSegment1061.DEF = "hanim_l_thumb_distal"
#<HAnimJoint name='l_thumb3'/> visualization sphere is placed within <HAnimSegment name='l_thumb_distal'/>
TouchSensor1062 = x3d.TouchSensor()
TouchSensor1062.description = "HAnimJoint l_thumb3, HAnimSegment l_thumb_distal"

HAnimSegment1061.children.append(TouchSensor1062)
Transform1063 = x3d.Transform()
Transform1063.translation = [0.1955,0.8159,0.0464]
Shape1064 = x3d.Shape()
Shape1064.USE = "HAnimJointShape"

Transform1063.children.append(Shape1064)

HAnimSegment1061.children.append(Transform1063)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_thumb3'/> to <HAnimSite name='l_thumb_distal_tip'/>
Shape1065 = x3d.Shape()
LineSet1066 = x3d.LineSet()
LineSet1066.vertexCount = [2]
Coordinate1067 = x3d.Coordinate()

LineSet1066.coord = Coordinate1067
ColorRGBA1068 = x3d.ColorRGBA()
ColorRGBA1068.USE = "HAnimSiteLineColorRGBA"

LineSet1066.color = ColorRGBA1068

Shape1065.geometry = LineSet1066

HAnimSegment1061.children.append(Shape1065)
HAnimSite1069 = x3d.HAnimSite()
HAnimSite1069.name = "l_thumb_distal_tip"
HAnimSite1069.DEF = "hanim_l_thumb_distal_tip"
HAnimSite1069.translation = [0.1982,0.8061,0.0759]
#HAnimSite visualization shape
TouchSensor1070 = x3d.TouchSensor()
TouchSensor1070.description = "HAnimSite l_thumb_distal_tip"

HAnimSite1069.children.append(TouchSensor1070)
Shape1071 = x3d.Shape()
Shape1071.USE = "HAnimSiteShape"

HAnimSite1069.children.append(Shape1071)

HAnimSegment1061.children.append(HAnimSite1069)

HAnimJoint1060.children.append(HAnimSegment1061)

HAnimJoint1051.children.append(HAnimJoint1060)

HAnimJoint1042.children.append(HAnimJoint1051)

HAnimJoint984.children.append(HAnimJoint1042)
HAnimJoint1072 = x3d.HAnimJoint()
HAnimJoint1072.name = "l_index0"
HAnimJoint1072.DEF = "hanim_l_index0"
HAnimJoint1072.center = [0.1983,0.8024,-0.028]
HAnimJoint1072.ulimit = [0,0,0]
HAnimJoint1072.llimit = [0,0,0]
HAnimSegment1073 = x3d.HAnimSegment()
HAnimSegment1073.name = "l_index_metacarpal"
HAnimSegment1073.DEF = "hanim_l_index_metacarpal"
#<HAnimJoint name='l_index0'/> visualization sphere is placed within <HAnimSegment name='l_index_metacarpal'/>
TouchSensor1074 = x3d.TouchSensor()
TouchSensor1074.description = "HAnimJoint l_index0, HAnimSegment l_index_metacarpal"

HAnimSegment1073.children.append(TouchSensor1074)
Transform1075 = x3d.Transform()
Transform1075.translation = [0.1983,0.8024,-0.028]
Shape1076 = x3d.Shape()
Shape1076.USE = "HAnimJointShape"

Transform1075.children.append(Shape1076)

HAnimSegment1073.children.append(Transform1075)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_index0'/> to <HAnimJoint name='l_index1'/>
Shape1077 = x3d.Shape()
LineSet1078 = x3d.LineSet()
LineSet1078.vertexCount = [2]
Coordinate1079 = x3d.Coordinate()

LineSet1078.coord = Coordinate1079
ColorRGBA1080 = x3d.ColorRGBA()
ColorRGBA1080.USE = "HAnimSegmentLineColorRGBA"

LineSet1078.color = ColorRGBA1080

Shape1077.geometry = LineSet1078

HAnimSegment1073.children.append(Shape1077)

HAnimJoint1072.children.append(HAnimSegment1073)
HAnimJoint1081 = x3d.HAnimJoint()
HAnimJoint1081.name = "l_index1"
HAnimJoint1081.DEF = "hanim_l_index1"
HAnimJoint1081.center = [0.1983,0.7815,-0.028]
HAnimJoint1081.ulimit = [0,0,0]
HAnimJoint1081.llimit = [0,0,0]
HAnimSegment1082 = x3d.HAnimSegment()
HAnimSegment1082.name = "l_index_proximal"
HAnimSegment1082.DEF = "hanim_l_index_proximal"
#<HAnimJoint name='l_index1'/> visualization sphere is placed within <HAnimSegment name='l_index_proximal'/>
TouchSensor1083 = x3d.TouchSensor()
TouchSensor1083.description = "HAnimJoint l_index1, HAnimSegment l_index_proximal"

HAnimSegment1082.children.append(TouchSensor1083)
Transform1084 = x3d.Transform()
Transform1084.translation = [0.1983,0.7815,-0.028]
Shape1085 = x3d.Shape()
Shape1085.USE = "HAnimJointShape"

Transform1084.children.append(Shape1085)

HAnimSegment1082.children.append(Transform1084)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_index1'/> to <HAnimJoint name='l_index2'/>
Shape1086 = x3d.Shape()
LineSet1087 = x3d.LineSet()
LineSet1087.vertexCount = [2]
Coordinate1088 = x3d.Coordinate()

LineSet1087.coord = Coordinate1088
ColorRGBA1089 = x3d.ColorRGBA()
ColorRGBA1089.USE = "HAnimSegmentLineColorRGBA"

LineSet1087.color = ColorRGBA1089

Shape1086.geometry = LineSet1087

HAnimSegment1082.children.append(Shape1086)

HAnimJoint1081.children.append(HAnimSegment1082)
HAnimJoint1090 = x3d.HAnimJoint()
HAnimJoint1090.name = "l_index2"
HAnimJoint1090.DEF = "hanim_l_index2"
HAnimJoint1090.center = [0.2017,0.7363,-0.0248]
HAnimJoint1090.ulimit = [0,0,0]
HAnimJoint1090.llimit = [0,0,0]
HAnimSegment1091 = x3d.HAnimSegment()
HAnimSegment1091.name = "l_index_middle"
HAnimSegment1091.DEF = "hanim_l_index_middle"
#<HAnimJoint name='l_index2'/> visualization sphere is placed within <HAnimSegment name='l_index_middle'/>
TouchSensor1092 = x3d.TouchSensor()
TouchSensor1092.description = "HAnimJoint l_index2, HAnimSegment l_index_middle"

HAnimSegment1091.children.append(TouchSensor1092)
Transform1093 = x3d.Transform()
Transform1093.translation = [0.2017,0.7363,-0.0248]
Shape1094 = x3d.Shape()
Shape1094.USE = "HAnimJointShape"

Transform1093.children.append(Shape1094)

HAnimSegment1091.children.append(Transform1093)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_index2'/> to <HAnimJoint name='l_index3'/>
Shape1095 = x3d.Shape()
LineSet1096 = x3d.LineSet()
LineSet1096.vertexCount = [2]
Coordinate1097 = x3d.Coordinate()

LineSet1096.coord = Coordinate1097
ColorRGBA1098 = x3d.ColorRGBA()
ColorRGBA1098.USE = "HAnimSegmentLineColorRGBA"

LineSet1096.color = ColorRGBA1098

Shape1095.geometry = LineSet1096

HAnimSegment1091.children.append(Shape1095)

HAnimJoint1090.children.append(HAnimSegment1091)
HAnimJoint1099 = x3d.HAnimJoint()
HAnimJoint1099.name = "l_index3"
HAnimJoint1099.DEF = "hanim_l_index3"
HAnimJoint1099.center = [0.2028,0.7139,-0.0236]
HAnimJoint1099.ulimit = [0,0,0]
HAnimJoint1099.llimit = [0,0,0]
HAnimSegment1100 = x3d.HAnimSegment()
HAnimSegment1100.name = "l_index_distal"
HAnimSegment1100.DEF = "hanim_l_index_distal"
#<HAnimJoint name='l_index3'/> visualization sphere is placed within <HAnimSegment name='l_index_distal'/>
TouchSensor1101 = x3d.TouchSensor()
TouchSensor1101.description = "HAnimJoint l_index3, HAnimSegment l_index_distal"

HAnimSegment1100.children.append(TouchSensor1101)
Transform1102 = x3d.Transform()
Transform1102.translation = [0.2028,0.7139,-0.0236]
Shape1103 = x3d.Shape()
Shape1103.USE = "HAnimJointShape"

Transform1102.children.append(Shape1103)

HAnimSegment1100.children.append(Transform1102)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_index3'/> to <HAnimSite name='l_index_distal_tip'/>
Shape1104 = x3d.Shape()
LineSet1105 = x3d.LineSet()
LineSet1105.vertexCount = [2]
Coordinate1106 = x3d.Coordinate()

LineSet1105.coord = Coordinate1106
ColorRGBA1107 = x3d.ColorRGBA()
ColorRGBA1107.USE = "HAnimSiteLineColorRGBA"

LineSet1105.color = ColorRGBA1107

Shape1104.geometry = LineSet1105

HAnimSegment1100.children.append(Shape1104)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_index3'/> to <HAnimSite name='l_dactylion'/>
Shape1108 = x3d.Shape()
LineSet1109 = x3d.LineSet()
LineSet1109.vertexCount = [2]
Coordinate1110 = x3d.Coordinate()

LineSet1109.coord = Coordinate1110
ColorRGBA1111 = x3d.ColorRGBA()
ColorRGBA1111.USE = "HAnimSiteLineColorRGBA"

LineSet1109.color = ColorRGBA1111

Shape1108.geometry = LineSet1109

HAnimSegment1100.children.append(Shape1108)
HAnimSite1112 = x3d.HAnimSite()
HAnimSite1112.name = "l_index_distal_tip"
HAnimSite1112.DEF = "hanim_l_index_distal_tip"
HAnimSite1112.translation = [0.2089,0.6858,-0.0245]
#HAnimSite visualization shape
TouchSensor1113 = x3d.TouchSensor()
TouchSensor1113.description = "HAnimSite l_index_distal_tip"

HAnimSite1112.children.append(TouchSensor1113)
Shape1114 = x3d.Shape()
Shape1114.USE = "HAnimSiteShape"

HAnimSite1112.children.append(Shape1114)

HAnimSegment1100.children.append(HAnimSite1112)
HAnimSite1115 = x3d.HAnimSite()
HAnimSite1115.name = "l_dactylion_pt"
HAnimSite1115.DEF = "hanim_l_dactylion_pt"
HAnimSite1115.translation = [0.2056,0.6743,-0.0482]
#HAnimSite visualization shape
TouchSensor1116 = x3d.TouchSensor()
TouchSensor1116.description = "HAnimSite l_dactylion"

HAnimSite1115.children.append(TouchSensor1116)
Shape1117 = x3d.Shape()
Shape1117.USE = "HAnimSiteShape"

HAnimSite1115.children.append(Shape1117)

HAnimSegment1100.children.append(HAnimSite1115)

HAnimJoint1099.children.append(HAnimSegment1100)

HAnimJoint1090.children.append(HAnimJoint1099)

HAnimJoint1081.children.append(HAnimJoint1090)

HAnimJoint1072.children.append(HAnimJoint1081)

HAnimJoint984.children.append(HAnimJoint1072)
HAnimJoint1118 = x3d.HAnimJoint()
HAnimJoint1118.name = "l_middle0"
HAnimJoint1118.DEF = "hanim_l_middle0"
HAnimJoint1118.center = [0.1987,0.8029,-0.053]
HAnimJoint1118.ulimit = [0,0,0]
HAnimJoint1118.llimit = [0,0,0]
HAnimSegment1119 = x3d.HAnimSegment()
HAnimSegment1119.name = "l_middle_metacarpal"
HAnimSegment1119.DEF = "hanim_l_middle_metacarpal"
#<HAnimJoint name='l_middle0'/> visualization sphere is placed within <HAnimSegment name='l_middle_metacarpal'/>
TouchSensor1120 = x3d.TouchSensor()
TouchSensor1120.description = "HAnimJoint l_middle0, HAnimSegment l_middle_metacarpal"

HAnimSegment1119.children.append(TouchSensor1120)
Transform1121 = x3d.Transform()
Transform1121.translation = [0.1987,0.8029,-0.053]
Shape1122 = x3d.Shape()
Shape1122.USE = "HAnimJointShape"

Transform1121.children.append(Shape1122)

HAnimSegment1119.children.append(Transform1121)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_middle0'/> to <HAnimJoint name='l_middle1'/>
Shape1123 = x3d.Shape()
LineSet1124 = x3d.LineSet()
LineSet1124.vertexCount = [2]
Coordinate1125 = x3d.Coordinate()

LineSet1124.coord = Coordinate1125
ColorRGBA1126 = x3d.ColorRGBA()
ColorRGBA1126.USE = "HAnimSegmentLineColorRGBA"

LineSet1124.color = ColorRGBA1126

Shape1123.geometry = LineSet1124

HAnimSegment1119.children.append(Shape1123)

HAnimJoint1118.children.append(HAnimSegment1119)
HAnimJoint1127 = x3d.HAnimJoint()
HAnimJoint1127.name = "l_middle1"
HAnimJoint1127.DEF = "hanim_l_middle1"
HAnimJoint1127.center = [0.1987,0.7818,-0.053]
HAnimJoint1127.ulimit = [0,0,0]
HAnimJoint1127.llimit = [0,0,0]
HAnimSegment1128 = x3d.HAnimSegment()
HAnimSegment1128.name = "l_middle_proximal"
HAnimSegment1128.DEF = "hanim_l_middle_proximal"
#<HAnimJoint name='l_middle1'/> visualization sphere is placed within <HAnimSegment name='l_middle_proximal'/>
TouchSensor1129 = x3d.TouchSensor()
TouchSensor1129.description = "HAnimJoint l_middle1, HAnimSegment l_middle_proximal"

HAnimSegment1128.children.append(TouchSensor1129)
Transform1130 = x3d.Transform()
Transform1130.translation = [0.1987,0.7818,-0.053]
Shape1131 = x3d.Shape()
Shape1131.USE = "HAnimJointShape"

Transform1130.children.append(Shape1131)

HAnimSegment1128.children.append(Transform1130)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_middle1'/> to <HAnimJoint name='l_middle2'/>
Shape1132 = x3d.Shape()
LineSet1133 = x3d.LineSet()
LineSet1133.vertexCount = [2]
Coordinate1134 = x3d.Coordinate()

LineSet1133.coord = Coordinate1134
ColorRGBA1135 = x3d.ColorRGBA()
ColorRGBA1135.USE = "HAnimSegmentLineColorRGBA"

LineSet1133.color = ColorRGBA1135

Shape1132.geometry = LineSet1133

HAnimSegment1128.children.append(Shape1132)

HAnimJoint1127.children.append(HAnimSegment1128)
HAnimJoint1136 = x3d.HAnimJoint()
HAnimJoint1136.name = "l_middle2"
HAnimJoint1136.DEF = "hanim_l_middle2"
HAnimJoint1136.center = [0.2013,0.7273,-0.0503]
HAnimJoint1136.ulimit = [0,0,0]
HAnimJoint1136.llimit = [0,0,0]
HAnimSegment1137 = x3d.HAnimSegment()
HAnimSegment1137.name = "l_middle_middle"
HAnimSegment1137.DEF = "hanim_l_middle_middle"
#<HAnimJoint name='l_middle2'/> visualization sphere is placed within <HAnimSegment name='l_middle_middle'/>
TouchSensor1138 = x3d.TouchSensor()
TouchSensor1138.description = "HAnimJoint l_middle2, HAnimSegment l_middle_middle"

HAnimSegment1137.children.append(TouchSensor1138)
Transform1139 = x3d.Transform()
Transform1139.translation = [0.2013,0.7273,-0.0503]
Shape1140 = x3d.Shape()
Shape1140.USE = "HAnimJointShape"

Transform1139.children.append(Shape1140)

HAnimSegment1137.children.append(Transform1139)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_middle2'/> to <HAnimJoint name='l_middle3'/>
Shape1141 = x3d.Shape()
LineSet1142 = x3d.LineSet()
LineSet1142.vertexCount = [2]
Coordinate1143 = x3d.Coordinate()

LineSet1142.coord = Coordinate1143
ColorRGBA1144 = x3d.ColorRGBA()
ColorRGBA1144.USE = "HAnimSegmentLineColorRGBA"

LineSet1142.color = ColorRGBA1144

Shape1141.geometry = LineSet1142

HAnimSegment1137.children.append(Shape1141)

HAnimJoint1136.children.append(HAnimSegment1137)
HAnimJoint1145 = x3d.HAnimJoint()
HAnimJoint1145.name = "l_middle3"
HAnimJoint1145.DEF = "hanim_l_middle3"
HAnimJoint1145.center = [0.2026,0.7011,-0.0494]
HAnimJoint1145.ulimit = [0,0,0]
HAnimJoint1145.llimit = [0,0,0]
HAnimSegment1146 = x3d.HAnimSegment()
HAnimSegment1146.name = "l_middle_distal"
HAnimSegment1146.DEF = "hanim_l_middle_distal"
#<HAnimJoint name='l_middle3'/> visualization sphere is placed within <HAnimSegment name='l_middle_distal'/>
TouchSensor1147 = x3d.TouchSensor()
TouchSensor1147.description = "HAnimJoint l_middle3, HAnimSegment l_middle_distal"

HAnimSegment1146.children.append(TouchSensor1147)
Transform1148 = x3d.Transform()
Transform1148.translation = [0.2026,0.7011,-0.0494]
Shape1149 = x3d.Shape()
Shape1149.USE = "HAnimJointShape"

Transform1148.children.append(Shape1149)

HAnimSegment1146.children.append(Transform1148)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_middle3'/> to <HAnimSite name='l_middle_distal_tip'/>
Shape1150 = x3d.Shape()
LineSet1151 = x3d.LineSet()
LineSet1151.vertexCount = [2]
Coordinate1152 = x3d.Coordinate()

LineSet1151.coord = Coordinate1152
ColorRGBA1153 = x3d.ColorRGBA()
ColorRGBA1153.USE = "HAnimSiteLineColorRGBA"

LineSet1151.color = ColorRGBA1153

Shape1150.geometry = LineSet1151

HAnimSegment1146.children.append(Shape1150)
HAnimSite1154 = x3d.HAnimSite()
HAnimSite1154.name = "l_middle_distal_tip"
HAnimSite1154.DEF = "hanim_l_middle_distal_tip"
HAnimSite1154.translation = [0.208,0.6731,-0.0491]
#HAnimSite visualization shape
TouchSensor1155 = x3d.TouchSensor()
TouchSensor1155.description = "HAnimSite l_middle_distal_tip"

HAnimSite1154.children.append(TouchSensor1155)
Shape1156 = x3d.Shape()
Shape1156.USE = "HAnimSiteShape"

HAnimSite1154.children.append(Shape1156)

HAnimSegment1146.children.append(HAnimSite1154)

HAnimJoint1145.children.append(HAnimSegment1146)

HAnimJoint1136.children.append(HAnimJoint1145)

HAnimJoint1127.children.append(HAnimJoint1136)

HAnimJoint1118.children.append(HAnimJoint1127)

HAnimJoint984.children.append(HAnimJoint1118)
HAnimJoint1157 = x3d.HAnimJoint()
HAnimJoint1157.name = "l_ring0"
HAnimJoint1157.DEF = "hanim_l_ring0"
HAnimJoint1157.center = [0.1956,0.8019,-0.0794]
HAnimJoint1157.ulimit = [0,0,0]
HAnimJoint1157.llimit = [0,0,0]
HAnimSegment1158 = x3d.HAnimSegment()
HAnimSegment1158.name = "l_ring_metacarpal"
HAnimSegment1158.DEF = "hanim_l_ring_metacarpal"
#<HAnimJoint name='l_ring0'/> visualization sphere is placed within <HAnimSegment name='l_ring_metacarpal'/>
TouchSensor1159 = x3d.TouchSensor()
TouchSensor1159.description = "HAnimJoint l_ring0, HAnimSegment l_ring_metacarpal"

HAnimSegment1158.children.append(TouchSensor1159)
Transform1160 = x3d.Transform()
Transform1160.translation = [0.1956,0.8019,-0.0794]
Shape1161 = x3d.Shape()
Shape1161.USE = "HAnimJointShape"

Transform1160.children.append(Shape1161)

HAnimSegment1158.children.append(Transform1160)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_ring0'/> to <HAnimJoint name='l_ring1'/>
Shape1162 = x3d.Shape()
LineSet1163 = x3d.LineSet()
LineSet1163.vertexCount = [2]
Coordinate1164 = x3d.Coordinate()

LineSet1163.coord = Coordinate1164
ColorRGBA1165 = x3d.ColorRGBA()
ColorRGBA1165.USE = "HAnimSegmentLineColorRGBA"

LineSet1163.color = ColorRGBA1165

Shape1162.geometry = LineSet1163

HAnimSegment1158.children.append(Shape1162)

HAnimJoint1157.children.append(HAnimSegment1158)
HAnimJoint1166 = x3d.HAnimJoint()
HAnimJoint1166.name = "l_ring1"
HAnimJoint1166.DEF = "hanim_l_ring1"
HAnimJoint1166.center = [0.1956,0.7815,-0.0794]
HAnimJoint1166.ulimit = [0,0,0]
HAnimJoint1166.llimit = [0,0,0]
HAnimSegment1167 = x3d.HAnimSegment()
HAnimSegment1167.name = "l_ring_proximal"
HAnimSegment1167.DEF = "hanim_l_ring_proximal"
#<HAnimJoint name='l_ring1'/> visualization sphere is placed within <HAnimSegment name='l_ring_proximal'/>
TouchSensor1168 = x3d.TouchSensor()
TouchSensor1168.description = "HAnimJoint l_ring1, HAnimSegment l_ring_proximal"

HAnimSegment1167.children.append(TouchSensor1168)
Transform1169 = x3d.Transform()
Transform1169.translation = [0.1956,0.7815,-0.0794]
Shape1170 = x3d.Shape()
Shape1170.USE = "HAnimJointShape"

Transform1169.children.append(Shape1170)

HAnimSegment1167.children.append(Transform1169)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_ring1'/> to <HAnimJoint name='l_ring2'/>
Shape1171 = x3d.Shape()
LineSet1172 = x3d.LineSet()
LineSet1172.vertexCount = [2]
Coordinate1173 = x3d.Coordinate()

LineSet1172.coord = Coordinate1173
ColorRGBA1174 = x3d.ColorRGBA()
ColorRGBA1174.USE = "HAnimSegmentLineColorRGBA"

LineSet1172.color = ColorRGBA1174

Shape1171.geometry = LineSet1172

HAnimSegment1167.children.append(Shape1171)

HAnimJoint1166.children.append(HAnimSegment1167)
HAnimJoint1175 = x3d.HAnimJoint()
HAnimJoint1175.name = "l_ring2"
HAnimJoint1175.DEF = "hanim_l_ring2"
HAnimJoint1175.center = [0.1973,0.7287,-0.0777]
HAnimJoint1175.ulimit = [0,0,0]
HAnimJoint1175.llimit = [0,0,0]
HAnimSegment1176 = x3d.HAnimSegment()
HAnimSegment1176.name = "l_ring_middle"
HAnimSegment1176.DEF = "hanim_l_ring_middle"
#<HAnimJoint name='l_ring2'/> visualization sphere is placed within <HAnimSegment name='l_ring_middle'/>
TouchSensor1177 = x3d.TouchSensor()
TouchSensor1177.description = "HAnimJoint l_ring2, HAnimSegment l_ring_middle"

HAnimSegment1176.children.append(TouchSensor1177)
Transform1178 = x3d.Transform()
Transform1178.translation = [0.1973,0.7287,-0.0777]
Shape1179 = x3d.Shape()
Shape1179.USE = "HAnimJointShape"

Transform1178.children.append(Shape1179)

HAnimSegment1176.children.append(Transform1178)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_ring2'/> to <HAnimJoint name='l_ring3'/>
Shape1180 = x3d.Shape()
LineSet1181 = x3d.LineSet()
LineSet1181.vertexCount = [2]
Coordinate1182 = x3d.Coordinate()

LineSet1181.coord = Coordinate1182
ColorRGBA1183 = x3d.ColorRGBA()
ColorRGBA1183.USE = "HAnimSegmentLineColorRGBA"

LineSet1181.color = ColorRGBA1183

Shape1180.geometry = LineSet1181

HAnimSegment1176.children.append(Shape1180)

HAnimJoint1175.children.append(HAnimSegment1176)
HAnimJoint1184 = x3d.HAnimJoint()
HAnimJoint1184.name = "l_ring3"
HAnimJoint1184.DEF = "hanim_l_ring3"
HAnimJoint1184.center = [0.1983,0.7045,-0.0767]
HAnimJoint1184.ulimit = [0,0,0]
HAnimJoint1184.llimit = [0,0,0]
HAnimSegment1185 = x3d.HAnimSegment()
HAnimSegment1185.name = "l_ring_distal"
HAnimSegment1185.DEF = "hanim_l_ring_distal"
#<HAnimJoint name='l_ring3'/> visualization sphere is placed within <HAnimSegment name='l_ring_distal'/>
TouchSensor1186 = x3d.TouchSensor()
TouchSensor1186.description = "HAnimJoint l_ring3, HAnimSegment l_ring_distal"

HAnimSegment1185.children.append(TouchSensor1186)
Transform1187 = x3d.Transform()
Transform1187.translation = [0.1983,0.7045,-0.0767]
Shape1188 = x3d.Shape()
Shape1188.USE = "HAnimJointShape"

Transform1187.children.append(Shape1188)

HAnimSegment1185.children.append(Transform1187)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_ring3'/> to <HAnimSite name='l_ring_distal_tip'/>
Shape1189 = x3d.Shape()
LineSet1190 = x3d.LineSet()
LineSet1190.vertexCount = [2]
Coordinate1191 = x3d.Coordinate()

LineSet1190.coord = Coordinate1191
ColorRGBA1192 = x3d.ColorRGBA()
ColorRGBA1192.USE = "HAnimSiteLineColorRGBA"

LineSet1190.color = ColorRGBA1192

Shape1189.geometry = LineSet1190

HAnimSegment1185.children.append(Shape1189)
HAnimSite1193 = x3d.HAnimSite()
HAnimSite1193.name = "l_ring_distal_tip"
HAnimSite1193.DEF = "hanim_l_ring_distal_tip"
HAnimSite1193.translation = [0.2035,0.675,-0.0756]
#HAnimSite visualization shape
TouchSensor1194 = x3d.TouchSensor()
TouchSensor1194.description = "HAnimSite l_ring_distal_tip"

HAnimSite1193.children.append(TouchSensor1194)
Shape1195 = x3d.Shape()
Shape1195.USE = "HAnimSiteShape"

HAnimSite1193.children.append(Shape1195)

HAnimSegment1185.children.append(HAnimSite1193)

HAnimJoint1184.children.append(HAnimSegment1185)

HAnimJoint1175.children.append(HAnimJoint1184)

HAnimJoint1166.children.append(HAnimJoint1175)

HAnimJoint1157.children.append(HAnimJoint1166)

HAnimJoint984.children.append(HAnimJoint1157)
HAnimJoint1196 = x3d.HAnimJoint()
HAnimJoint1196.name = "l_pinky0"
HAnimJoint1196.DEF = "hanim_l_pinky0"
HAnimJoint1196.center = [0.1925,0.8066,-0.1036]
HAnimJoint1196.ulimit = [0,0,0]
HAnimJoint1196.llimit = [0,0,0]
HAnimSegment1197 = x3d.HAnimSegment()
HAnimSegment1197.name = "l_pinky_metacarpal"
HAnimSegment1197.DEF = "hanim_l_pinky_metacarpal"
#<HAnimJoint name='l_pinky0'/> visualization sphere is placed within <HAnimSegment name='l_pinky_metacarpal'/>
TouchSensor1198 = x3d.TouchSensor()
TouchSensor1198.description = "HAnimJoint l_pinky0, HAnimSegment l_pinky_metacarpal"

HAnimSegment1197.children.append(TouchSensor1198)
Transform1199 = x3d.Transform()
Transform1199.translation = [0.1925,0.8066,-0.1036]
Shape1200 = x3d.Shape()
Shape1200.USE = "HAnimJointShape"

Transform1199.children.append(Shape1200)

HAnimSegment1197.children.append(Transform1199)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_pinky0'/> to <HAnimJoint name='l_pinky1'/>
Shape1201 = x3d.Shape()
LineSet1202 = x3d.LineSet()
LineSet1202.vertexCount = [2]
Coordinate1203 = x3d.Coordinate()

LineSet1202.coord = Coordinate1203
ColorRGBA1204 = x3d.ColorRGBA()
ColorRGBA1204.USE = "HAnimSegmentLineColorRGBA"

LineSet1202.color = ColorRGBA1204

Shape1201.geometry = LineSet1202

HAnimSegment1197.children.append(Shape1201)

HAnimJoint1196.children.append(HAnimSegment1197)
HAnimJoint1205 = x3d.HAnimJoint()
HAnimJoint1205.name = "l_pinky1"
HAnimJoint1205.DEF = "hanim_l_pinky1"
HAnimJoint1205.center = [0.1925,0.7866,-0.1036]
HAnimJoint1205.ulimit = [0,0,0]
HAnimJoint1205.llimit = [0,0,0]
HAnimSegment1206 = x3d.HAnimSegment()
HAnimSegment1206.name = "l_pinky_proximal"
HAnimSegment1206.DEF = "hanim_l_pinky_proximal"
#<HAnimJoint name='l_pinky1'/> visualization sphere is placed within <HAnimSegment name='l_pinky_proximal'/>
TouchSensor1207 = x3d.TouchSensor()
TouchSensor1207.description = "HAnimJoint l_pinky1, HAnimSegment l_pinky_proximal"

HAnimSegment1206.children.append(TouchSensor1207)
Transform1208 = x3d.Transform()
Transform1208.translation = [0.1925,0.7866,-0.1036]
Shape1209 = x3d.Shape()
Shape1209.USE = "HAnimJointShape"

Transform1208.children.append(Shape1209)

HAnimSegment1206.children.append(Transform1208)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_pinky1'/> to <HAnimJoint name='l_pinky2'/>
Shape1210 = x3d.Shape()
LineSet1211 = x3d.LineSet()
LineSet1211.vertexCount = [2]
Coordinate1212 = x3d.Coordinate()

LineSet1211.coord = Coordinate1212
ColorRGBA1213 = x3d.ColorRGBA()
ColorRGBA1213.USE = "HAnimSegmentLineColorRGBA"

LineSet1211.color = ColorRGBA1213

Shape1210.geometry = LineSet1211

HAnimSegment1206.children.append(Shape1210)

HAnimJoint1205.children.append(HAnimSegment1206)
HAnimJoint1214 = x3d.HAnimJoint()
HAnimJoint1214.name = "l_pinky2"
HAnimJoint1214.DEF = "hanim_l_pinky2"
HAnimJoint1214.center = [0.1938,0.7452,-0.1024]
HAnimJoint1214.ulimit = [0,0,0]
HAnimJoint1214.llimit = [0,0,0]
HAnimSegment1215 = x3d.HAnimSegment()
HAnimSegment1215.name = "l_pinky_middle"
HAnimSegment1215.DEF = "hanim_l_pinky_middle"
#<HAnimJoint name='l_pinky2'/> visualization sphere is placed within <HAnimSegment name='l_pinky_middle'/>
TouchSensor1216 = x3d.TouchSensor()
TouchSensor1216.description = "HAnimJoint l_pinky2, HAnimSegment l_pinky_middle"

HAnimSegment1215.children.append(TouchSensor1216)
Transform1217 = x3d.Transform()
Transform1217.translation = [0.1938,0.7452,-0.1024]
Shape1218 = x3d.Shape()
Shape1218.USE = "HAnimJointShape"

Transform1217.children.append(Shape1218)

HAnimSegment1215.children.append(Transform1217)
#HAnimSegment visualization line segment from parent <HAnimJoint name='l_pinky2'/> to <HAnimJoint name='l_pinky3'/>
Shape1219 = x3d.Shape()
LineSet1220 = x3d.LineSet()
LineSet1220.vertexCount = [2]
Coordinate1221 = x3d.Coordinate()

LineSet1220.coord = Coordinate1221
ColorRGBA1222 = x3d.ColorRGBA()
ColorRGBA1222.USE = "HAnimSegmentLineColorRGBA"

LineSet1220.color = ColorRGBA1222

Shape1219.geometry = LineSet1220

HAnimSegment1215.children.append(Shape1219)

HAnimJoint1214.children.append(HAnimSegment1215)
HAnimJoint1223 = x3d.HAnimJoint()
HAnimJoint1223.name = "l_pinky3"
HAnimJoint1223.DEF = "hanim_l_pinky3"
HAnimJoint1223.center = [0.1948,0.7277,-0.1017]
HAnimJoint1223.ulimit = [0,0,0]
HAnimJoint1223.llimit = [0,0,0]
HAnimSegment1224 = x3d.HAnimSegment()
HAnimSegment1224.name = "l_pinky_distal"
HAnimSegment1224.DEF = "hanim_l_pinky_distal"
#<HAnimJoint name='l_pinky3'/> visualization sphere is placed within <HAnimSegment name='l_pinky_distal'/>
TouchSensor1225 = x3d.TouchSensor()
TouchSensor1225.description = "HAnimJoint l_pinky3, HAnimSegment l_pinky_distal"

HAnimSegment1224.children.append(TouchSensor1225)
Transform1226 = x3d.Transform()
Transform1226.translation = [0.1948,0.7277,-0.1017]
Shape1227 = x3d.Shape()
Shape1227.USE = "HAnimJointShape"

Transform1226.children.append(Shape1227)

HAnimSegment1224.children.append(Transform1226)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='l_pinky3'/> to <HAnimSite name='l_pinky_distal_tip'/>
Shape1228 = x3d.Shape()
LineSet1229 = x3d.LineSet()
LineSet1229.vertexCount = [2]
Coordinate1230 = x3d.Coordinate()

LineSet1229.coord = Coordinate1230
ColorRGBA1231 = x3d.ColorRGBA()
ColorRGBA1231.USE = "HAnimSiteLineColorRGBA"

LineSet1229.color = ColorRGBA1231

Shape1228.geometry = LineSet1229

HAnimSegment1224.children.append(Shape1228)
HAnimSite1232 = x3d.HAnimSite()
HAnimSite1232.name = "l_pinky_distal_tip"
HAnimSite1232.DEF = "hanim_l_pinky_distal_tip"
HAnimSite1232.translation = [0.2014,0.7009,-0.1012]
#HAnimSite visualization shape
TouchSensor1233 = x3d.TouchSensor()
TouchSensor1233.description = "HAnimSite l_pinky_distal_tip"

HAnimSite1232.children.append(TouchSensor1233)
Shape1234 = x3d.Shape()
Shape1234.USE = "HAnimSiteShape"

HAnimSite1232.children.append(Shape1234)

HAnimSegment1224.children.append(HAnimSite1232)

HAnimJoint1223.children.append(HAnimSegment1224)

HAnimJoint1214.children.append(HAnimJoint1223)

HAnimJoint1205.children.append(HAnimJoint1214)

HAnimJoint1196.children.append(HAnimJoint1205)

HAnimJoint984.children.append(HAnimJoint1196)

HAnimJoint947.children.append(HAnimJoint984)

HAnimJoint931.children.append(HAnimJoint947)

HAnimJoint922.children.append(HAnimJoint931)

HAnimJoint885.children.append(HAnimJoint922)

HAnimJoint597.children.append(HAnimJoint885)
HAnimJoint1235 = x3d.HAnimJoint()
HAnimJoint1235.name = "r_sternoclavicular"
HAnimJoint1235.DEF = "hanim_r_sternoclavicular"
HAnimJoint1235.center = [-0.082,1.4488,-0.0353]
HAnimJoint1235.ulimit = [0,0,0]
HAnimJoint1235.llimit = [0,0,0]
HAnimSegment1236 = x3d.HAnimSegment()
HAnimSegment1236.name = "r_clavicle"
HAnimSegment1236.DEF = "hanim_r_clavicle"
#<HAnimJoint name='r_sternoclavicular'/> visualization sphere is placed within <HAnimSegment name='r_clavicle'/>
TouchSensor1237 = x3d.TouchSensor()
TouchSensor1237.description = "HAnimJoint r_sternoclavicular, HAnimSegment r_clavicle"

HAnimSegment1236.children.append(TouchSensor1237)
Transform1238 = x3d.Transform()
Transform1238.translation = [-0.082,1.4488,-0.0353]
Shape1239 = x3d.Shape()
Shape1239.USE = "HAnimJointShape"

Transform1238.children.append(Shape1239)

HAnimSegment1236.children.append(Transform1238)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_sternoclavicular'/> to <HAnimJoint name='r_acromioclavicular'/>
Shape1240 = x3d.Shape()
LineSet1241 = x3d.LineSet()
LineSet1241.vertexCount = [2]
Coordinate1242 = x3d.Coordinate()

LineSet1241.coord = Coordinate1242
ColorRGBA1243 = x3d.ColorRGBA()
ColorRGBA1243.USE = "HAnimSegmentLineColorRGBA"

LineSet1241.color = ColorRGBA1243

Shape1240.geometry = LineSet1241

HAnimSegment1236.children.append(Shape1240)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_sternoclavicular'/> to <HAnimSite name='r_clavicale'/>
Shape1244 = x3d.Shape()
LineSet1245 = x3d.LineSet()
LineSet1245.vertexCount = [2]
Coordinate1246 = x3d.Coordinate()

LineSet1245.coord = Coordinate1246
ColorRGBA1247 = x3d.ColorRGBA()
ColorRGBA1247.USE = "HAnimSiteLineColorRGBA"

LineSet1245.color = ColorRGBA1247

Shape1244.geometry = LineSet1245

HAnimSegment1236.children.append(Shape1244)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_sternoclavicular'/> to <HAnimSite name='r_acromion'/>
Shape1248 = x3d.Shape()
LineSet1249 = x3d.LineSet()
LineSet1249.vertexCount = [2]
Coordinate1250 = x3d.Coordinate()

LineSet1249.coord = Coordinate1250
ColorRGBA1251 = x3d.ColorRGBA()
ColorRGBA1251.USE = "HAnimSiteLineColorRGBA"

LineSet1249.color = ColorRGBA1251

Shape1248.geometry = LineSet1249

HAnimSegment1236.children.append(Shape1248)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_sternoclavicular'/> to <HAnimSite name='r_axilla_ant'/>
Shape1252 = x3d.Shape()
LineSet1253 = x3d.LineSet()
LineSet1253.vertexCount = [2]
Coordinate1254 = x3d.Coordinate()

LineSet1253.coord = Coordinate1254
ColorRGBA1255 = x3d.ColorRGBA()
ColorRGBA1255.USE = "HAnimSiteLineColorRGBA"

LineSet1253.color = ColorRGBA1255

Shape1252.geometry = LineSet1253

HAnimSegment1236.children.append(Shape1252)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_sternoclavicular'/> to <HAnimSite name='r_axilla_post'/>
Shape1256 = x3d.Shape()
LineSet1257 = x3d.LineSet()
LineSet1257.vertexCount = [2]
Coordinate1258 = x3d.Coordinate()

LineSet1257.coord = Coordinate1258
ColorRGBA1259 = x3d.ColorRGBA()
ColorRGBA1259.USE = "HAnimSiteLineColorRGBA"

LineSet1257.color = ColorRGBA1259

Shape1256.geometry = LineSet1257

HAnimSegment1236.children.append(Shape1256)
HAnimSite1260 = x3d.HAnimSite()
HAnimSite1260.name = "r_clavicale_pt"
HAnimSite1260.DEF = "hanim_r_clavicale_pt"
HAnimSite1260.translation = [-0.0115,1.4943,0.04]
#HAnimSite visualization shape
TouchSensor1261 = x3d.TouchSensor()
TouchSensor1261.description = "HAnimSite r_clavicale"

HAnimSite1260.children.append(TouchSensor1261)
Shape1262 = x3d.Shape()
Shape1262.USE = "HAnimSiteShape"

HAnimSite1260.children.append(Shape1262)

HAnimSegment1236.children.append(HAnimSite1260)
HAnimSite1263 = x3d.HAnimSite()
HAnimSite1263.name = "r_acromion_pt"
HAnimSite1263.DEF = "hanim_r_acromion_pt"
HAnimSite1263.translation = [-0.1905,1.4791,-0.0431]
#HAnimSite visualization shape
TouchSensor1264 = x3d.TouchSensor()
TouchSensor1264.description = "HAnimSite r_acromion"

HAnimSite1263.children.append(TouchSensor1264)
Shape1265 = x3d.Shape()
Shape1265.USE = "HAnimSiteShape"

HAnimSite1263.children.append(Shape1265)

HAnimSegment1236.children.append(HAnimSite1263)
HAnimSite1266 = x3d.HAnimSite()
HAnimSite1266.name = "r_axilla_ant_pt"
HAnimSite1266.DEF = "hanim_r_axilla_ant_pt"
HAnimSite1266.translation = [-0.1626,1.4072,-0.0031]
#HAnimSite visualization shape
TouchSensor1267 = x3d.TouchSensor()
TouchSensor1267.description = "HAnimSite r_axilla_ant"

HAnimSite1266.children.append(TouchSensor1267)
Shape1268 = x3d.Shape()
Shape1268.USE = "HAnimSiteShape"

HAnimSite1266.children.append(Shape1268)

HAnimSegment1236.children.append(HAnimSite1266)
HAnimSite1269 = x3d.HAnimSite()
HAnimSite1269.name = "r_axilla_post_pt"
HAnimSite1269.DEF = "hanim_r_axilla_post_pt"
HAnimSite1269.translation = [-0.1603,1.4098,-0.0826]
#HAnimSite visualization shape
TouchSensor1270 = x3d.TouchSensor()
TouchSensor1270.description = "HAnimSite r_axilla_post"

HAnimSite1269.children.append(TouchSensor1270)
Shape1271 = x3d.Shape()
Shape1271.USE = "HAnimSiteShape"

HAnimSite1269.children.append(Shape1271)

HAnimSegment1236.children.append(HAnimSite1269)

HAnimJoint1235.children.append(HAnimSegment1236)
HAnimJoint1272 = x3d.HAnimJoint()
HAnimJoint1272.name = "r_acromioclavicular"
HAnimJoint1272.DEF = "hanim_r_acromioclavicular"
HAnimJoint1272.center = [-0.0962,1.4269,-0.0424]
HAnimJoint1272.ulimit = [0,0,0]
HAnimJoint1272.llimit = [0,0,0]
HAnimSegment1273 = x3d.HAnimSegment()
HAnimSegment1273.name = "r_scapula"
HAnimSegment1273.DEF = "hanim_r_scapula"
#<HAnimJoint name='r_acromioclavicular'/> visualization sphere is placed within <HAnimSegment name='r_scapula'/>
TouchSensor1274 = x3d.TouchSensor()
TouchSensor1274.description = "HAnimJoint r_acromioclavicular, HAnimSegment r_scapula"

HAnimSegment1273.children.append(TouchSensor1274)
Transform1275 = x3d.Transform()
Transform1275.translation = [-0.0962,1.4269,-0.0424]
Shape1276 = x3d.Shape()
Shape1276.USE = "HAnimJointShape"

Transform1275.children.append(Shape1276)

HAnimSegment1273.children.append(Transform1275)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_acromioclavicular'/> to <HAnimJoint name='r_shoulder'/>
Shape1277 = x3d.Shape()
LineSet1278 = x3d.LineSet()
LineSet1278.vertexCount = [2]
Coordinate1279 = x3d.Coordinate()

LineSet1278.coord = Coordinate1279
ColorRGBA1280 = x3d.ColorRGBA()
ColorRGBA1280.USE = "HAnimSegmentLineColorRGBA"

LineSet1278.color = ColorRGBA1280

Shape1277.geometry = LineSet1278

HAnimSegment1273.children.append(Shape1277)

HAnimJoint1272.children.append(HAnimSegment1273)
HAnimJoint1281 = x3d.HAnimJoint()
HAnimJoint1281.name = "r_shoulder"
HAnimJoint1281.DEF = "hanim_r_shoulder"
HAnimJoint1281.center = [-0.2029,1.4376,-0.0387]
HAnimJoint1281.ulimit = [0,0,0]
HAnimJoint1281.llimit = [0,0,0]
HAnimSegment1282 = x3d.HAnimSegment()
HAnimSegment1282.name = "r_upperarm"
HAnimSegment1282.DEF = "hanim_r_upperarm"
#<HAnimJoint name='r_shoulder'/> visualization sphere is placed within <HAnimSegment name='r_upperarm'/>
TouchSensor1283 = x3d.TouchSensor()
TouchSensor1283.description = "HAnimJoint r_shoulder, HAnimSegment r_upperarm"

HAnimSegment1282.children.append(TouchSensor1283)
Transform1284 = x3d.Transform()
Transform1284.translation = [-0.2029,1.4376,-0.0387]
Shape1285 = x3d.Shape()
Shape1285.USE = "HAnimJointShape"

Transform1284.children.append(Shape1285)

HAnimSegment1282.children.append(Transform1284)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_shoulder'/> to <HAnimJoint name='r_elbow'/>
Shape1286 = x3d.Shape()
LineSet1287 = x3d.LineSet()
LineSet1287.vertexCount = [2]
Coordinate1288 = x3d.Coordinate()

LineSet1287.coord = Coordinate1288
ColorRGBA1289 = x3d.ColorRGBA()
ColorRGBA1289.USE = "HAnimSegmentLineColorRGBA"

LineSet1287.color = ColorRGBA1289

Shape1286.geometry = LineSet1287

HAnimSegment1282.children.append(Shape1286)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_shoulder'/> to <HAnimSite name='r_humeral_lateral_epicn'/>
Shape1290 = x3d.Shape()
LineSet1291 = x3d.LineSet()
LineSet1291.vertexCount = [2]
Coordinate1292 = x3d.Coordinate()

LineSet1291.coord = Coordinate1292
ColorRGBA1293 = x3d.ColorRGBA()
ColorRGBA1293.USE = "HAnimSiteLineColorRGBA"

LineSet1291.color = ColorRGBA1293

Shape1290.geometry = LineSet1291

HAnimSegment1282.children.append(Shape1290)
HAnimSite1294 = x3d.HAnimSite()
HAnimSite1294.name = "r_humeral_lateral_epicn_pt"
HAnimSite1294.DEF = "hanim_r_humeral_lateral_epicn_pt"
HAnimSite1294.translation = [-0.2224,1.1517,-0.1033]
#HAnimSite visualization shape
TouchSensor1295 = x3d.TouchSensor()
TouchSensor1295.description = "HAnimSite r_humeral_lateral_epicn"

HAnimSite1294.children.append(TouchSensor1295)
Shape1296 = x3d.Shape()
Shape1296.USE = "HAnimSiteShape"

HAnimSite1294.children.append(Shape1296)

HAnimSegment1282.children.append(HAnimSite1294)

HAnimJoint1281.children.append(HAnimSegment1282)
HAnimJoint1297 = x3d.HAnimJoint()
HAnimJoint1297.name = "r_elbow"
HAnimJoint1297.DEF = "hanim_r_elbow"
HAnimJoint1297.center = [-0.2014,1.1357,-0.0682]
HAnimJoint1297.ulimit = [0,0,0]
HAnimJoint1297.llimit = [0,0,0]
HAnimSegment1298 = x3d.HAnimSegment()
HAnimSegment1298.name = "r_forearm"
HAnimSegment1298.DEF = "hanim_r_forearm"
#<HAnimJoint name='r_elbow'/> visualization sphere is placed within <HAnimSegment name='r_forearm'/>
TouchSensor1299 = x3d.TouchSensor()
TouchSensor1299.description = "HAnimJoint r_elbow, HAnimSegment r_forearm"

HAnimSegment1298.children.append(TouchSensor1299)
Transform1300 = x3d.Transform()
Transform1300.translation = [-0.2014,1.1357,-0.0682]
Shape1301 = x3d.Shape()
Shape1301.USE = "HAnimJointShape"

Transform1300.children.append(Shape1301)

HAnimSegment1298.children.append(Transform1300)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_elbow'/> to <HAnimJoint name='r_wrist'/>
Shape1302 = x3d.Shape()
LineSet1303 = x3d.LineSet()
LineSet1303.vertexCount = [2]
Coordinate1304 = x3d.Coordinate()

LineSet1303.coord = Coordinate1304
ColorRGBA1305 = x3d.ColorRGBA()
ColorRGBA1305.USE = "HAnimSegmentLineColorRGBA"

LineSet1303.color = ColorRGBA1305

Shape1302.geometry = LineSet1303

HAnimSegment1298.children.append(Shape1302)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_elbow'/> to <HAnimSite name='r_radial_styloid'/>
Shape1306 = x3d.Shape()
LineSet1307 = x3d.LineSet()
LineSet1307.vertexCount = [2]
Coordinate1308 = x3d.Coordinate()

LineSet1307.coord = Coordinate1308
ColorRGBA1309 = x3d.ColorRGBA()
ColorRGBA1309.USE = "HAnimSiteLineColorRGBA"

LineSet1307.color = ColorRGBA1309

Shape1306.geometry = LineSet1307

HAnimSegment1298.children.append(Shape1306)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_elbow'/> to <HAnimSite name='r_olecranon'/>
Shape1310 = x3d.Shape()
LineSet1311 = x3d.LineSet()
LineSet1311.vertexCount = [2]
Coordinate1312 = x3d.Coordinate()

LineSet1311.coord = Coordinate1312
ColorRGBA1313 = x3d.ColorRGBA()
ColorRGBA1313.USE = "HAnimSiteLineColorRGBA"

LineSet1311.color = ColorRGBA1313

Shape1310.geometry = LineSet1311

HAnimSegment1298.children.append(Shape1310)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_elbow'/> to <HAnimSite name='r_humeral_medial_epicn'/>
Shape1314 = x3d.Shape()
LineSet1315 = x3d.LineSet()
LineSet1315.vertexCount = [2]
Coordinate1316 = x3d.Coordinate()

LineSet1315.coord = Coordinate1316
ColorRGBA1317 = x3d.ColorRGBA()
ColorRGBA1317.USE = "HAnimSiteLineColorRGBA"

LineSet1315.color = ColorRGBA1317

Shape1314.geometry = LineSet1315

HAnimSegment1298.children.append(Shape1314)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_elbow'/> to <HAnimSite name='r_radiale'/>
Shape1318 = x3d.Shape()
LineSet1319 = x3d.LineSet()
LineSet1319.vertexCount = [2]
Coordinate1320 = x3d.Coordinate()

LineSet1319.coord = Coordinate1320
ColorRGBA1321 = x3d.ColorRGBA()
ColorRGBA1321.USE = "HAnimSiteLineColorRGBA"

LineSet1319.color = ColorRGBA1321

Shape1318.geometry = LineSet1319

HAnimSegment1298.children.append(Shape1318)
HAnimSite1322 = x3d.HAnimSite()
HAnimSite1322.name = "r_radial_styloid_pt"
HAnimSite1322.DEF = "hanim_r_radial_styloid_pt"
HAnimSite1322.translation = [-0.1884,0.8676,-0.036]
#HAnimSite visualization shape
TouchSensor1323 = x3d.TouchSensor()
TouchSensor1323.description = "HAnimSite r_radial_styloid"

HAnimSite1322.children.append(TouchSensor1323)
Shape1324 = x3d.Shape()
Shape1324.USE = "HAnimSiteShape"

HAnimSite1322.children.append(Shape1324)

HAnimSegment1298.children.append(HAnimSite1322)
HAnimSite1325 = x3d.HAnimSite()
HAnimSite1325.name = "r_olecranon_pt"
HAnimSite1325.DEF = "hanim_r_olecranon_pt"
HAnimSite1325.translation = [-0.1907,1.1405,-0.1065]
#HAnimSite visualization shape
TouchSensor1326 = x3d.TouchSensor()
TouchSensor1326.description = "HAnimSite r_olecranon"

HAnimSite1325.children.append(TouchSensor1326)
Shape1327 = x3d.Shape()
Shape1327.USE = "HAnimSiteShape"

HAnimSite1325.children.append(Shape1327)

HAnimSegment1298.children.append(HAnimSite1325)
HAnimSite1328 = x3d.HAnimSite()
HAnimSite1328.name = "r_humeral_medial_epicn_pt"
HAnimSite1328.DEF = "hanim_r_humeral_medial_epicn_pt"
HAnimSite1328.translation = [-0.168,1.1298,-0.1062]
#HAnimSite visualization shape
TouchSensor1329 = x3d.TouchSensor()
TouchSensor1329.description = "HAnimSite r_humeral_medial_epicn"

HAnimSite1328.children.append(TouchSensor1329)
Shape1330 = x3d.Shape()
Shape1330.USE = "HAnimSiteShape"

HAnimSite1328.children.append(Shape1330)

HAnimSegment1298.children.append(HAnimSite1328)
HAnimSite1331 = x3d.HAnimSite()
HAnimSite1331.name = "r_radiale_pt"
HAnimSite1331.DEF = "hanim_r_radiale_pt"
HAnimSite1331.translation = [-0.213,1.1305,-0.1091]
#HAnimSite visualization shape
TouchSensor1332 = x3d.TouchSensor()
TouchSensor1332.description = "HAnimSite r_radiale"

HAnimSite1331.children.append(TouchSensor1332)
Shape1333 = x3d.Shape()
Shape1333.USE = "HAnimSiteShape"

HAnimSite1331.children.append(Shape1333)

HAnimSegment1298.children.append(HAnimSite1331)

HAnimJoint1297.children.append(HAnimSegment1298)
HAnimJoint1334 = x3d.HAnimJoint()
HAnimJoint1334.name = "r_wrist"
HAnimJoint1334.DEF = "hanim_r_wrist"
HAnimJoint1334.center = [-0.1984,0.8663,-0.0583]
HAnimJoint1334.ulimit = [0,0,0]
HAnimJoint1334.llimit = [0,0,0]
HAnimSegment1335 = x3d.HAnimSegment()
HAnimSegment1335.name = "r_hand"
HAnimSegment1335.DEF = "hanim_r_hand"
#<HAnimJoint name='r_wrist'/> visualization sphere is placed within <HAnimSegment name='r_hand'/>
TouchSensor1336 = x3d.TouchSensor()
TouchSensor1336.description = "HAnimJoint r_wrist, HAnimSegment r_hand"

HAnimSegment1335.children.append(TouchSensor1336)
Transform1337 = x3d.Transform()
Transform1337.translation = [-0.1984,0.8663,-0.0583]
Shape1338 = x3d.Shape()
Shape1338.USE = "HAnimJointShape"

Transform1337.children.append(Shape1338)

HAnimSegment1335.children.append(Transform1337)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_wrist'/> to <HAnimJoint name='r_thumb1'/>
Shape1339 = x3d.Shape()
LineSet1340 = x3d.LineSet()
LineSet1340.vertexCount = [2]
Coordinate1341 = x3d.Coordinate()

LineSet1340.coord = Coordinate1341
ColorRGBA1342 = x3d.ColorRGBA()
ColorRGBA1342.USE = "HAnimSegmentLineColorRGBA"

LineSet1340.color = ColorRGBA1342

Shape1339.geometry = LineSet1340

HAnimSegment1335.children.append(Shape1339)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_wrist'/> to <HAnimJoint name='r_index0'/>
Shape1343 = x3d.Shape()
LineSet1344 = x3d.LineSet()
LineSet1344.vertexCount = [2]
Coordinate1345 = x3d.Coordinate()

LineSet1344.coord = Coordinate1345
ColorRGBA1346 = x3d.ColorRGBA()
ColorRGBA1346.USE = "HAnimSegmentLineColorRGBA"

LineSet1344.color = ColorRGBA1346

Shape1343.geometry = LineSet1344

HAnimSegment1335.children.append(Shape1343)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_wrist'/> to <HAnimJoint name='r_middle0'/>
Shape1347 = x3d.Shape()
LineSet1348 = x3d.LineSet()
LineSet1348.vertexCount = [2]
Coordinate1349 = x3d.Coordinate()

LineSet1348.coord = Coordinate1349
ColorRGBA1350 = x3d.ColorRGBA()
ColorRGBA1350.USE = "HAnimSegmentLineColorRGBA"

LineSet1348.color = ColorRGBA1350

Shape1347.geometry = LineSet1348

HAnimSegment1335.children.append(Shape1347)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_wrist'/> to <HAnimJoint name='r_ring0'/>
Shape1351 = x3d.Shape()
LineSet1352 = x3d.LineSet()
LineSet1352.vertexCount = [2]
Coordinate1353 = x3d.Coordinate()

LineSet1352.coord = Coordinate1353
ColorRGBA1354 = x3d.ColorRGBA()
ColorRGBA1354.USE = "HAnimSegmentLineColorRGBA"

LineSet1352.color = ColorRGBA1354

Shape1351.geometry = LineSet1352

HAnimSegment1335.children.append(Shape1351)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_wrist'/> to <HAnimJoint name='r_pinky0'/>
Shape1355 = x3d.Shape()
LineSet1356 = x3d.LineSet()
LineSet1356.vertexCount = [2]
Coordinate1357 = x3d.Coordinate()

LineSet1356.coord = Coordinate1357
ColorRGBA1358 = x3d.ColorRGBA()
ColorRGBA1358.USE = "HAnimSegmentLineColorRGBA"

LineSet1356.color = ColorRGBA1358

Shape1355.geometry = LineSet1356

HAnimSegment1335.children.append(Shape1355)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_wrist'/> to <HAnimSite name='r_metacarpal_pha2'/>
Shape1359 = x3d.Shape()
LineSet1360 = x3d.LineSet()
LineSet1360.vertexCount = [2]
Coordinate1361 = x3d.Coordinate()

LineSet1360.coord = Coordinate1361
ColorRGBA1362 = x3d.ColorRGBA()
ColorRGBA1362.USE = "HAnimSiteLineColorRGBA"

LineSet1360.color = ColorRGBA1362

Shape1359.geometry = LineSet1360

HAnimSegment1335.children.append(Shape1359)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_wrist'/> to <HAnimSite name='r_ulnar_styloid'/>
Shape1363 = x3d.Shape()
LineSet1364 = x3d.LineSet()
LineSet1364.vertexCount = [2]
Coordinate1365 = x3d.Coordinate()

LineSet1364.coord = Coordinate1365
ColorRGBA1366 = x3d.ColorRGBA()
ColorRGBA1366.USE = "HAnimSiteLineColorRGBA"

LineSet1364.color = ColorRGBA1366

Shape1363.geometry = LineSet1364

HAnimSegment1335.children.append(Shape1363)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_wrist'/> to <HAnimSite name='r_metacarpal_pha5'/>
Shape1367 = x3d.Shape()
LineSet1368 = x3d.LineSet()
LineSet1368.vertexCount = [2]
Coordinate1369 = x3d.Coordinate()

LineSet1368.coord = Coordinate1369
ColorRGBA1370 = x3d.ColorRGBA()
ColorRGBA1370.USE = "HAnimSiteLineColorRGBA"

LineSet1368.color = ColorRGBA1370

Shape1367.geometry = LineSet1368

HAnimSegment1335.children.append(Shape1367)
#HAnimSite/Viewpoint visualization line segment from ancestor <HAnimJoint name='r_wrist'/> to <HAnimSite name='r_hand_front_view'/>
Shape1371 = x3d.Shape()
LineSet1372 = x3d.LineSet()
LineSet1372.vertexCount = [2]
Coordinate1373 = x3d.Coordinate()

LineSet1372.coord = Coordinate1373
ColorRGBA1374 = x3d.ColorRGBA()
ColorRGBA1374.USE = "HAnimSiteViewpointLineColorRGBA"

LineSet1372.color = ColorRGBA1374

Shape1371.geometry = LineSet1372

HAnimSegment1335.children.append(Shape1371)
HAnimSite1375 = x3d.HAnimSite()
HAnimSite1375.name = "r_metacarpal_pha2_pt"
HAnimSite1375.DEF = "hanim_r_metacarpal_pha2_pt"
HAnimSite1375.translation = [-0.1977,0.8169,-0.0177]
#HAnimSite visualization shape
TouchSensor1376 = x3d.TouchSensor()
TouchSensor1376.description = "HAnimSite r_metacarpal_pha2"

HAnimSite1375.children.append(TouchSensor1376)
Shape1377 = x3d.Shape()
Shape1377.USE = "HAnimSiteShape"

HAnimSite1375.children.append(Shape1377)

HAnimSegment1335.children.append(HAnimSite1375)
HAnimSite1378 = x3d.HAnimSite()
HAnimSite1378.name = "r_ulnar_styloid_pt"
HAnimSite1378.DEF = "hanim_r_ulnar_styloid_pt"
HAnimSite1378.translation = [-0.2117,0.8562,-0.0584]
#HAnimSite visualization shape
TouchSensor1379 = x3d.TouchSensor()
TouchSensor1379.description = "HAnimSite r_ulnar_styloid"

HAnimSite1378.children.append(TouchSensor1379)
Shape1380 = x3d.Shape()
Shape1380.USE = "HAnimSiteShape"

HAnimSite1378.children.append(Shape1380)

HAnimSegment1335.children.append(HAnimSite1378)
HAnimSite1381 = x3d.HAnimSite()
HAnimSite1381.name = "r_metacarpal_pha5_pt"
HAnimSite1381.DEF = "hanim_r_metacarpal_pha5_pt"
HAnimSite1381.translation = [-0.1929,0.789,-0.1064]
#HAnimSite visualization shape
TouchSensor1382 = x3d.TouchSensor()
TouchSensor1382.description = "HAnimSite r_metacarpal_pha5"

HAnimSite1381.children.append(TouchSensor1382)
Shape1383 = x3d.Shape()
Shape1383.USE = "HAnimSiteShape"

HAnimSite1381.children.append(Shape1383)

HAnimSegment1335.children.append(HAnimSite1381)
HAnimSite1384 = x3d.HAnimSite()
HAnimSite1384.name = "r_hand_front_view"
HAnimSite1384.DEF = "hanim_r_hand_front_view"
HAnimSite1384.translation = [-0.3,0.75,0.45]
#HAnimSite visualization shape
TouchSensor1385 = x3d.TouchSensor()
TouchSensor1385.description = "HAnimSite r_hand_front_view"

HAnimSite1384.children.append(TouchSensor1385)
Shape1386 = x3d.Shape()
Shape1386.USE = "HAnimSiteShape"

HAnimSite1384.children.append(Shape1386)
Viewpoint1387 = x3d.Viewpoint()
Viewpoint1387.DEF = "hanim_r_hand_front_viewpoint"
Viewpoint1387.centerOfRotation = [0,0.7,0]
Viewpoint1387.description = "right hand front"
Viewpoint1387.position = [0,0,0]

HAnimSite1384.children.append(Viewpoint1387)
#HAnimSite/Viewpoint visualization shape
Anchor1388 = x3d.Anchor()
Anchor1388.description = "HAnimSite hanim_r_hand_front_view Viewpoint"
Anchor1388.url = ["#hanim_r_hand_front_viewpoint"]
LOD1389 = x3d.LOD()
LOD1389.forceTransitions = True
LOD1389.range = [0.04]
WorldInfo1390 = x3d.WorldInfo()
WorldInfo1390.info = ["hide diamond when close"]

LOD1389.children.append(WorldInfo1390)
Shape1391 = x3d.Shape()
Shape1391.USE = "HAnimSiteViewpointShape"

LOD1389.children.append(Shape1391)

Anchor1388.children.append(LOD1389)

HAnimSite1384.children.append(Anchor1388)

HAnimSegment1335.children.append(HAnimSite1384)

HAnimJoint1334.children.append(HAnimSegment1335)
HAnimJoint1392 = x3d.HAnimJoint()
HAnimJoint1392.name = "r_thumb1"
HAnimJoint1392.DEF = "hanim_r_thumb1"
HAnimJoint1392.center = [-0.1924,0.8472,-0.0534]
HAnimJoint1392.ulimit = [0,0,0]
HAnimJoint1392.llimit = [0,0,0]
HAnimSegment1393 = x3d.HAnimSegment()
HAnimSegment1393.name = "r_thumb_metacarpal"
HAnimSegment1393.DEF = "hanim_r_thumb_metacarpal"
#<HAnimJoint name='r_thumb1'/> visualization sphere is placed within <HAnimSegment name='r_thumb_metacarpal'/>
TouchSensor1394 = x3d.TouchSensor()
TouchSensor1394.description = "HAnimJoint r_thumb1, HAnimSegment r_thumb_metacarpal"

HAnimSegment1393.children.append(TouchSensor1394)
Transform1395 = x3d.Transform()
Transform1395.translation = [-0.1924,0.8472,-0.0534]
Shape1396 = x3d.Shape()
Shape1396.USE = "HAnimJointShape"

Transform1395.children.append(Shape1396)

HAnimSegment1393.children.append(Transform1395)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_thumb1'/> to <HAnimJoint name='r_thumb2'/>
Shape1397 = x3d.Shape()
LineSet1398 = x3d.LineSet()
LineSet1398.vertexCount = [2]
Coordinate1399 = x3d.Coordinate()

LineSet1398.coord = Coordinate1399
ColorRGBA1400 = x3d.ColorRGBA()
ColorRGBA1400.USE = "HAnimSegmentLineColorRGBA"

LineSet1398.color = ColorRGBA1400

Shape1397.geometry = LineSet1398

HAnimSegment1393.children.append(Shape1397)

HAnimJoint1392.children.append(HAnimSegment1393)
HAnimJoint1401 = x3d.HAnimJoint()
HAnimJoint1401.name = "r_thumb2"
HAnimJoint1401.DEF = "hanim_r_thumb2"
HAnimJoint1401.center = [-0.1951,0.8226,0.0246]
HAnimJoint1401.ulimit = [0,0,0]
HAnimJoint1401.llimit = [0,0,0]
HAnimSegment1402 = x3d.HAnimSegment()
HAnimSegment1402.name = "r_thumb_proximal"
HAnimSegment1402.DEF = "hanim_r_thumb_proximal"
#<HAnimJoint name='r_thumb2'/> visualization sphere is placed within <HAnimSegment name='r_thumb_proximal'/>
TouchSensor1403 = x3d.TouchSensor()
TouchSensor1403.description = "HAnimJoint r_thumb2, HAnimSegment r_thumb_proximal"

HAnimSegment1402.children.append(TouchSensor1403)
Transform1404 = x3d.Transform()
Transform1404.translation = [-0.1951,0.8226,0.0246]
Shape1405 = x3d.Shape()
Shape1405.USE = "HAnimJointShape"

Transform1404.children.append(Shape1405)

HAnimSegment1402.children.append(Transform1404)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_thumb2'/> to <HAnimJoint name='r_thumb3'/>
Shape1406 = x3d.Shape()
LineSet1407 = x3d.LineSet()
LineSet1407.vertexCount = [2]
Coordinate1408 = x3d.Coordinate()

LineSet1407.coord = Coordinate1408
ColorRGBA1409 = x3d.ColorRGBA()
ColorRGBA1409.USE = "HAnimSegmentLineColorRGBA"

LineSet1407.color = ColorRGBA1409

Shape1406.geometry = LineSet1407

HAnimSegment1402.children.append(Shape1406)

HAnimJoint1401.children.append(HAnimSegment1402)
HAnimJoint1410 = x3d.HAnimJoint()
HAnimJoint1410.name = "r_thumb3"
HAnimJoint1410.DEF = "hanim_r_thumb3"
HAnimJoint1410.center = [-0.1955,0.8159,0.0464]
HAnimJoint1410.ulimit = [0,0,0]
HAnimJoint1410.llimit = [0,0,0]
HAnimSegment1411 = x3d.HAnimSegment()
HAnimSegment1411.name = "r_thumb_distal"
HAnimSegment1411.DEF = "hanim_r_thumb_distal"
#<HAnimJoint name='r_thumb3'/> visualization sphere is placed within <HAnimSegment name='r_thumb_distal'/>
TouchSensor1412 = x3d.TouchSensor()
TouchSensor1412.description = "HAnimJoint r_thumb3, HAnimSegment r_thumb_distal"

HAnimSegment1411.children.append(TouchSensor1412)
Transform1413 = x3d.Transform()
Transform1413.translation = [-0.1955,0.8159,0.0464]
Shape1414 = x3d.Shape()
Shape1414.USE = "HAnimJointShape"

Transform1413.children.append(Shape1414)

HAnimSegment1411.children.append(Transform1413)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_thumb3'/> to <HAnimSite name='r_thumb_distal_tip'/>
Shape1415 = x3d.Shape()
LineSet1416 = x3d.LineSet()
LineSet1416.vertexCount = [2]
Coordinate1417 = x3d.Coordinate()

LineSet1416.coord = Coordinate1417
ColorRGBA1418 = x3d.ColorRGBA()
ColorRGBA1418.USE = "HAnimSiteLineColorRGBA"

LineSet1416.color = ColorRGBA1418

Shape1415.geometry = LineSet1416

HAnimSegment1411.children.append(Shape1415)
HAnimSite1419 = x3d.HAnimSite()
HAnimSite1419.name = "r_thumb_distal_tip"
HAnimSite1419.DEF = "hanim_r_thumb_distal_tip"
HAnimSite1419.translation = [-0.1869,0.809,0.082]
#HAnimSite visualization shape
TouchSensor1420 = x3d.TouchSensor()
TouchSensor1420.description = "HAnimSite r_thumb_distal_tip"

HAnimSite1419.children.append(TouchSensor1420)
Shape1421 = x3d.Shape()
Shape1421.USE = "HAnimSiteShape"

HAnimSite1419.children.append(Shape1421)

HAnimSegment1411.children.append(HAnimSite1419)

HAnimJoint1410.children.append(HAnimSegment1411)

HAnimJoint1401.children.append(HAnimJoint1410)

HAnimJoint1392.children.append(HAnimJoint1401)

HAnimJoint1334.children.append(HAnimJoint1392)
HAnimJoint1422 = x3d.HAnimJoint()
HAnimJoint1422.name = "r_index0"
HAnimJoint1422.DEF = "hanim_r_index0"
HAnimJoint1422.center = [-0.1983,0.8024,-0.028]
HAnimJoint1422.ulimit = [0,0,0]
HAnimJoint1422.llimit = [0,0,0]
HAnimSegment1423 = x3d.HAnimSegment()
HAnimSegment1423.name = "r_index_metacarpal"
HAnimSegment1423.DEF = "hanim_r_index_metacarpal"
#<HAnimJoint name='r_index0'/> visualization sphere is placed within <HAnimSegment name='r_index_metacarpal'/>
TouchSensor1424 = x3d.TouchSensor()
TouchSensor1424.description = "HAnimJoint r_index0, HAnimSegment r_index_metacarpal"

HAnimSegment1423.children.append(TouchSensor1424)
Transform1425 = x3d.Transform()
Transform1425.translation = [-0.1983,0.8024,-0.028]
Shape1426 = x3d.Shape()
Shape1426.USE = "HAnimJointShape"

Transform1425.children.append(Shape1426)

HAnimSegment1423.children.append(Transform1425)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_index0'/> to <HAnimJoint name='r_index1'/>
Shape1427 = x3d.Shape()
LineSet1428 = x3d.LineSet()
LineSet1428.vertexCount = [2]
Coordinate1429 = x3d.Coordinate()

LineSet1428.coord = Coordinate1429
ColorRGBA1430 = x3d.ColorRGBA()
ColorRGBA1430.USE = "HAnimSegmentLineColorRGBA"

LineSet1428.color = ColorRGBA1430

Shape1427.geometry = LineSet1428

HAnimSegment1423.children.append(Shape1427)

HAnimJoint1422.children.append(HAnimSegment1423)
HAnimJoint1431 = x3d.HAnimJoint()
HAnimJoint1431.name = "r_index1"
HAnimJoint1431.DEF = "hanim_r_index1"
HAnimJoint1431.center = [-0.1983,0.7815,-0.028]
HAnimJoint1431.ulimit = [0,0,0]
HAnimJoint1431.llimit = [0,0,0]
HAnimSegment1432 = x3d.HAnimSegment()
HAnimSegment1432.name = "r_index_proximal"
HAnimSegment1432.DEF = "hanim_r_index_proximal"
#<HAnimJoint name='r_index1'/> visualization sphere is placed within <HAnimSegment name='r_index_proximal'/>
TouchSensor1433 = x3d.TouchSensor()
TouchSensor1433.description = "HAnimJoint r_index1, HAnimSegment r_index_proximal"

HAnimSegment1432.children.append(TouchSensor1433)
Transform1434 = x3d.Transform()
Transform1434.translation = [-0.1983,0.7815,-0.028]
Shape1435 = x3d.Shape()
Shape1435.USE = "HAnimJointShape"

Transform1434.children.append(Shape1435)

HAnimSegment1432.children.append(Transform1434)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_index1'/> to <HAnimJoint name='r_index2'/>
Shape1436 = x3d.Shape()
LineSet1437 = x3d.LineSet()
LineSet1437.vertexCount = [2]
Coordinate1438 = x3d.Coordinate()

LineSet1437.coord = Coordinate1438
ColorRGBA1439 = x3d.ColorRGBA()
ColorRGBA1439.USE = "HAnimSegmentLineColorRGBA"

LineSet1437.color = ColorRGBA1439

Shape1436.geometry = LineSet1437

HAnimSegment1432.children.append(Shape1436)

HAnimJoint1431.children.append(HAnimSegment1432)
HAnimJoint1440 = x3d.HAnimJoint()
HAnimJoint1440.name = "r_index2"
HAnimJoint1440.DEF = "hanim_r_index2"
HAnimJoint1440.center = [-0.2017,0.7363,-0.0248]
HAnimJoint1440.ulimit = [0,0,0]
HAnimJoint1440.llimit = [0,0,0]
HAnimSegment1441 = x3d.HAnimSegment()
HAnimSegment1441.name = "r_index_middle"
HAnimSegment1441.DEF = "hanim_r_index_middle"
#<HAnimJoint name='r_index2'/> visualization sphere is placed within <HAnimSegment name='r_index_middle'/>
TouchSensor1442 = x3d.TouchSensor()
TouchSensor1442.description = "HAnimJoint r_index2, HAnimSegment r_index_middle"

HAnimSegment1441.children.append(TouchSensor1442)
Transform1443 = x3d.Transform()
Transform1443.translation = [-0.2017,0.7363,-0.0248]
Shape1444 = x3d.Shape()
Shape1444.USE = "HAnimJointShape"

Transform1443.children.append(Shape1444)

HAnimSegment1441.children.append(Transform1443)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_index2'/> to <HAnimJoint name='r_index3'/>
Shape1445 = x3d.Shape()
LineSet1446 = x3d.LineSet()
LineSet1446.vertexCount = [2]
Coordinate1447 = x3d.Coordinate()

LineSet1446.coord = Coordinate1447
ColorRGBA1448 = x3d.ColorRGBA()
ColorRGBA1448.USE = "HAnimSegmentLineColorRGBA"

LineSet1446.color = ColorRGBA1448

Shape1445.geometry = LineSet1446

HAnimSegment1441.children.append(Shape1445)

HAnimJoint1440.children.append(HAnimSegment1441)
HAnimJoint1449 = x3d.HAnimJoint()
HAnimJoint1449.name = "r_index3"
HAnimJoint1449.DEF = "hanim_r_index3"
HAnimJoint1449.center = [-0.2028,0.7139,-0.0236]
HAnimJoint1449.ulimit = [0,0,0]
HAnimJoint1449.llimit = [0,0,0]
HAnimSegment1450 = x3d.HAnimSegment()
HAnimSegment1450.name = "r_index_distal"
HAnimSegment1450.DEF = "hanim_r_index_distal"
#<HAnimJoint name='r_index3'/> visualization sphere is placed within <HAnimSegment name='r_index_distal'/>
TouchSensor1451 = x3d.TouchSensor()
TouchSensor1451.description = "HAnimJoint r_index3, HAnimSegment r_index_distal"

HAnimSegment1450.children.append(TouchSensor1451)
Transform1452 = x3d.Transform()
Transform1452.translation = [-0.2028,0.7139,-0.0236]
Shape1453 = x3d.Shape()
Shape1453.USE = "HAnimJointShape"

Transform1452.children.append(Shape1453)

HAnimSegment1450.children.append(Transform1452)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_index3'/> to <HAnimSite name='r_index_distal_tip'/>
Shape1454 = x3d.Shape()
LineSet1455 = x3d.LineSet()
LineSet1455.vertexCount = [2]
Coordinate1456 = x3d.Coordinate()

LineSet1455.coord = Coordinate1456
ColorRGBA1457 = x3d.ColorRGBA()
ColorRGBA1457.USE = "HAnimSiteLineColorRGBA"

LineSet1455.color = ColorRGBA1457

Shape1454.geometry = LineSet1455

HAnimSegment1450.children.append(Shape1454)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_index3'/> to <HAnimSite name='r_dactylion'/>
Shape1458 = x3d.Shape()
LineSet1459 = x3d.LineSet()
LineSet1459.vertexCount = [2]
Coordinate1460 = x3d.Coordinate()

LineSet1459.coord = Coordinate1460
ColorRGBA1461 = x3d.ColorRGBA()
ColorRGBA1461.USE = "HAnimSiteLineColorRGBA"

LineSet1459.color = ColorRGBA1461

Shape1458.geometry = LineSet1459

HAnimSegment1450.children.append(Shape1458)
HAnimSite1462 = x3d.HAnimSite()
HAnimSite1462.name = "r_index_distal_tip"
HAnimSite1462.DEF = "hanim_r_index_distal_tip"
HAnimSite1462.translation = [-0.198,0.6883,-0.018]
#HAnimSite visualization shape
TouchSensor1463 = x3d.TouchSensor()
TouchSensor1463.description = "HAnimSite r_index_distal_tip"

HAnimSite1462.children.append(TouchSensor1463)
Shape1464 = x3d.Shape()
Shape1464.USE = "HAnimSiteShape"

HAnimSite1462.children.append(Shape1464)

HAnimSegment1450.children.append(HAnimSite1462)
HAnimSite1465 = x3d.HAnimSite()
HAnimSite1465.name = "r_dactylion_pt"
HAnimSite1465.DEF = "hanim_r_dactylion_pt"
HAnimSite1465.translation = [-0.1941,0.6772,-0.0423]
#HAnimSite visualization shape
TouchSensor1466 = x3d.TouchSensor()
TouchSensor1466.description = "HAnimSite r_dactylion"

HAnimSite1465.children.append(TouchSensor1466)
Shape1467 = x3d.Shape()
Shape1467.USE = "HAnimSiteShape"

HAnimSite1465.children.append(Shape1467)

HAnimSegment1450.children.append(HAnimSite1465)

HAnimJoint1449.children.append(HAnimSegment1450)

HAnimJoint1440.children.append(HAnimJoint1449)

HAnimJoint1431.children.append(HAnimJoint1440)

HAnimJoint1422.children.append(HAnimJoint1431)

HAnimJoint1334.children.append(HAnimJoint1422)
HAnimJoint1468 = x3d.HAnimJoint()
HAnimJoint1468.name = "r_middle0"
HAnimJoint1468.DEF = "hanim_r_middle0"
HAnimJoint1468.center = [-0.1987,0.8029,-0.053]
HAnimJoint1468.ulimit = [0,0,0]
HAnimJoint1468.llimit = [0,0,0]
HAnimSegment1469 = x3d.HAnimSegment()
HAnimSegment1469.name = "r_middle_metacarpal"
HAnimSegment1469.DEF = "hanim_r_middle_metacarpal"
#<HAnimJoint name='r_middle0'/> visualization sphere is placed within <HAnimSegment name='r_middle_metacarpal'/>
TouchSensor1470 = x3d.TouchSensor()
TouchSensor1470.description = "HAnimJoint r_middle0, HAnimSegment r_middle_metacarpal"

HAnimSegment1469.children.append(TouchSensor1470)
Transform1471 = x3d.Transform()
Transform1471.translation = [-0.1987,0.8029,-0.053]
Shape1472 = x3d.Shape()
Shape1472.USE = "HAnimJointShape"

Transform1471.children.append(Shape1472)

HAnimSegment1469.children.append(Transform1471)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_middle0'/> to <HAnimJoint name='r_middle1'/>
Shape1473 = x3d.Shape()
LineSet1474 = x3d.LineSet()
LineSet1474.vertexCount = [2]
Coordinate1475 = x3d.Coordinate()

LineSet1474.coord = Coordinate1475
ColorRGBA1476 = x3d.ColorRGBA()
ColorRGBA1476.USE = "HAnimSegmentLineColorRGBA"

LineSet1474.color = ColorRGBA1476

Shape1473.geometry = LineSet1474

HAnimSegment1469.children.append(Shape1473)

HAnimJoint1468.children.append(HAnimSegment1469)
HAnimJoint1477 = x3d.HAnimJoint()
HAnimJoint1477.name = "r_middle1"
HAnimJoint1477.DEF = "hanim_r_middle1"
HAnimJoint1477.center = [-0.1987,0.7818,-0.053]
HAnimJoint1477.ulimit = [0,0,0]
HAnimJoint1477.llimit = [0,0,0]
HAnimSegment1478 = x3d.HAnimSegment()
HAnimSegment1478.name = "r_middle_proximal"
HAnimSegment1478.DEF = "hanim_r_middle_proximal"
#<HAnimJoint name='r_middle1'/> visualization sphere is placed within <HAnimSegment name='r_middle_proximal'/>
TouchSensor1479 = x3d.TouchSensor()
TouchSensor1479.description = "HAnimJoint r_middle1, HAnimSegment r_middle_proximal"

HAnimSegment1478.children.append(TouchSensor1479)
Transform1480 = x3d.Transform()
Transform1480.translation = [-0.1987,0.7818,-0.053]
Shape1481 = x3d.Shape()
Shape1481.USE = "HAnimJointShape"

Transform1480.children.append(Shape1481)

HAnimSegment1478.children.append(Transform1480)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_middle1'/> to <HAnimJoint name='r_middle2'/>
Shape1482 = x3d.Shape()
LineSet1483 = x3d.LineSet()
LineSet1483.vertexCount = [2]
Coordinate1484 = x3d.Coordinate()

LineSet1483.coord = Coordinate1484
ColorRGBA1485 = x3d.ColorRGBA()
ColorRGBA1485.USE = "HAnimSegmentLineColorRGBA"

LineSet1483.color = ColorRGBA1485

Shape1482.geometry = LineSet1483

HAnimSegment1478.children.append(Shape1482)

HAnimJoint1477.children.append(HAnimSegment1478)
HAnimJoint1486 = x3d.HAnimJoint()
HAnimJoint1486.name = "r_middle2"
HAnimJoint1486.DEF = "hanim_r_middle2"
HAnimJoint1486.center = [-0.2013,0.7273,-0.0503]
HAnimJoint1486.ulimit = [0,0,0]
HAnimJoint1486.llimit = [0,0,0]
HAnimSegment1487 = x3d.HAnimSegment()
HAnimSegment1487.name = "r_middle_middle"
HAnimSegment1487.DEF = "hanim_r_middle_middle"
#<HAnimJoint name='r_middle2'/> visualization sphere is placed within <HAnimSegment name='r_middle_middle'/>
TouchSensor1488 = x3d.TouchSensor()
TouchSensor1488.description = "HAnimJoint r_middle2, HAnimSegment r_middle_middle"

HAnimSegment1487.children.append(TouchSensor1488)
Transform1489 = x3d.Transform()
Transform1489.translation = [-0.2013,0.7273,-0.0503]
Shape1490 = x3d.Shape()
Shape1490.USE = "HAnimJointShape"

Transform1489.children.append(Shape1490)

HAnimSegment1487.children.append(Transform1489)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_middle2'/> to <HAnimJoint name='r_middle3'/>
Shape1491 = x3d.Shape()
LineSet1492 = x3d.LineSet()
LineSet1492.vertexCount = [2]
Coordinate1493 = x3d.Coordinate()

LineSet1492.coord = Coordinate1493
ColorRGBA1494 = x3d.ColorRGBA()
ColorRGBA1494.USE = "HAnimSegmentLineColorRGBA"

LineSet1492.color = ColorRGBA1494

Shape1491.geometry = LineSet1492

HAnimSegment1487.children.append(Shape1491)

HAnimJoint1486.children.append(HAnimSegment1487)
HAnimJoint1495 = x3d.HAnimJoint()
HAnimJoint1495.name = "r_middle3"
HAnimJoint1495.DEF = "hanim_r_middle3"
HAnimJoint1495.center = [-0.2026,0.7011,-0.0494]
HAnimJoint1495.ulimit = [0,0,0]
HAnimJoint1495.llimit = [0,0,0]
HAnimSegment1496 = x3d.HAnimSegment()
HAnimSegment1496.name = "r_middle_distal"
HAnimSegment1496.DEF = "hanim_r_middle_distal"
#<HAnimJoint name='r_middle3'/> visualization sphere is placed within <HAnimSegment name='r_middle_distal'/>
TouchSensor1497 = x3d.TouchSensor()
TouchSensor1497.description = "HAnimJoint r_middle3, HAnimSegment r_middle_distal"

HAnimSegment1496.children.append(TouchSensor1497)
Transform1498 = x3d.Transform()
Transform1498.translation = [-0.2026,0.7011,-0.0494]
Shape1499 = x3d.Shape()
Shape1499.USE = "HAnimJointShape"

Transform1498.children.append(Shape1499)

HAnimSegment1496.children.append(Transform1498)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_middle3'/> to <HAnimSite name='r_middle_distal_tip'/>
Shape1500 = x3d.Shape()
LineSet1501 = x3d.LineSet()
LineSet1501.vertexCount = [2]
Coordinate1502 = x3d.Coordinate()

LineSet1501.coord = Coordinate1502
ColorRGBA1503 = x3d.ColorRGBA()
ColorRGBA1503.USE = "HAnimSiteLineColorRGBA"

LineSet1501.color = ColorRGBA1503

Shape1500.geometry = LineSet1501

HAnimSegment1496.children.append(Shape1500)
HAnimSite1504 = x3d.HAnimSite()
HAnimSite1504.name = "r_middle_distal_tip"
HAnimSite1504.DEF = "hanim_r_middle_distal_tip"
HAnimSite1504.translation = [-0.1969,0.6758,-0.0427]
#HAnimSite visualization shape
TouchSensor1505 = x3d.TouchSensor()
TouchSensor1505.description = "HAnimSite r_middle_distal_tip"

HAnimSite1504.children.append(TouchSensor1505)
Shape1506 = x3d.Shape()
Shape1506.USE = "HAnimSiteShape"

HAnimSite1504.children.append(Shape1506)

HAnimSegment1496.children.append(HAnimSite1504)

HAnimJoint1495.children.append(HAnimSegment1496)

HAnimJoint1486.children.append(HAnimJoint1495)

HAnimJoint1477.children.append(HAnimJoint1486)

HAnimJoint1468.children.append(HAnimJoint1477)

HAnimJoint1334.children.append(HAnimJoint1468)
HAnimJoint1507 = x3d.HAnimJoint()
HAnimJoint1507.name = "r_ring0"
HAnimJoint1507.DEF = "hanim_r_ring0"
HAnimJoint1507.center = [-0.1956,0.8019,-0.0794]
HAnimJoint1507.ulimit = [0,0,0]
HAnimJoint1507.llimit = [0,0,0]
HAnimSegment1508 = x3d.HAnimSegment()
HAnimSegment1508.name = "r_ring_metacarpal"
HAnimSegment1508.DEF = "hanim_r_ring_metacarpal"
#<HAnimJoint name='r_ring0'/> visualization sphere is placed within <HAnimSegment name='r_ring_metacarpal'/>
TouchSensor1509 = x3d.TouchSensor()
TouchSensor1509.description = "HAnimJoint r_ring0, HAnimSegment r_ring_metacarpal"

HAnimSegment1508.children.append(TouchSensor1509)
Transform1510 = x3d.Transform()
Transform1510.translation = [-0.1956,0.8019,-0.0794]
Shape1511 = x3d.Shape()
Shape1511.USE = "HAnimJointShape"

Transform1510.children.append(Shape1511)

HAnimSegment1508.children.append(Transform1510)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_ring0'/> to <HAnimJoint name='r_ring1'/>
Shape1512 = x3d.Shape()
LineSet1513 = x3d.LineSet()
LineSet1513.vertexCount = [2]
Coordinate1514 = x3d.Coordinate()

LineSet1513.coord = Coordinate1514
ColorRGBA1515 = x3d.ColorRGBA()
ColorRGBA1515.USE = "HAnimSegmentLineColorRGBA"

LineSet1513.color = ColorRGBA1515

Shape1512.geometry = LineSet1513

HAnimSegment1508.children.append(Shape1512)

HAnimJoint1507.children.append(HAnimSegment1508)
HAnimJoint1516 = x3d.HAnimJoint()
HAnimJoint1516.name = "r_ring1"
HAnimJoint1516.DEF = "hanim_r_ring1"
HAnimJoint1516.center = [-0.1956,0.7815,-0.0794]
HAnimJoint1516.ulimit = [0,0,0]
HAnimJoint1516.llimit = [0,0,0]
HAnimSegment1517 = x3d.HAnimSegment()
HAnimSegment1517.name = "r_ring_proximal"
HAnimSegment1517.DEF = "hanim_r_ring_proximal"
#<HAnimJoint name='r_ring1'/> visualization sphere is placed within <HAnimSegment name='r_ring_proximal'/>
TouchSensor1518 = x3d.TouchSensor()
TouchSensor1518.description = "HAnimJoint r_ring1, HAnimSegment r_ring_proximal"

HAnimSegment1517.children.append(TouchSensor1518)
Transform1519 = x3d.Transform()
Transform1519.translation = [-0.1956,0.7815,-0.0794]
Shape1520 = x3d.Shape()
Shape1520.USE = "HAnimJointShape"

Transform1519.children.append(Shape1520)

HAnimSegment1517.children.append(Transform1519)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_ring1'/> to <HAnimJoint name='r_ring2'/>
Shape1521 = x3d.Shape()
LineSet1522 = x3d.LineSet()
LineSet1522.vertexCount = [2]
Coordinate1523 = x3d.Coordinate()

LineSet1522.coord = Coordinate1523
ColorRGBA1524 = x3d.ColorRGBA()
ColorRGBA1524.USE = "HAnimSegmentLineColorRGBA"

LineSet1522.color = ColorRGBA1524

Shape1521.geometry = LineSet1522

HAnimSegment1517.children.append(Shape1521)

HAnimJoint1516.children.append(HAnimSegment1517)
HAnimJoint1525 = x3d.HAnimJoint()
HAnimJoint1525.name = "r_ring2"
HAnimJoint1525.DEF = "hanim_r_ring2"
HAnimJoint1525.center = [-0.1973,0.7287,-0.0777]
HAnimJoint1525.ulimit = [0,0,0]
HAnimJoint1525.llimit = [0,0,0]
HAnimSegment1526 = x3d.HAnimSegment()
HAnimSegment1526.name = "r_ring_middle"
HAnimSegment1526.DEF = "hanim_r_ring_middle"
#<HAnimJoint name='r_ring2'/> visualization sphere is placed within <HAnimSegment name='r_ring_middle'/>
TouchSensor1527 = x3d.TouchSensor()
TouchSensor1527.description = "HAnimJoint r_ring2, HAnimSegment r_ring_middle"

HAnimSegment1526.children.append(TouchSensor1527)
Transform1528 = x3d.Transform()
Transform1528.translation = [-0.1973,0.7287,-0.0777]
Shape1529 = x3d.Shape()
Shape1529.USE = "HAnimJointShape"

Transform1528.children.append(Shape1529)

HAnimSegment1526.children.append(Transform1528)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_ring2'/> to <HAnimJoint name='r_ring3'/>
Shape1530 = x3d.Shape()
LineSet1531 = x3d.LineSet()
LineSet1531.vertexCount = [2]
Coordinate1532 = x3d.Coordinate()

LineSet1531.coord = Coordinate1532
ColorRGBA1533 = x3d.ColorRGBA()
ColorRGBA1533.USE = "HAnimSegmentLineColorRGBA"

LineSet1531.color = ColorRGBA1533

Shape1530.geometry = LineSet1531

HAnimSegment1526.children.append(Shape1530)

HAnimJoint1525.children.append(HAnimSegment1526)
HAnimJoint1534 = x3d.HAnimJoint()
HAnimJoint1534.name = "r_ring3"
HAnimJoint1534.DEF = "hanim_r_ring3"
HAnimJoint1534.center = [-0.1983,0.7045,-0.0767]
HAnimJoint1534.ulimit = [0,0,0]
HAnimJoint1534.llimit = [0,0,0]
HAnimSegment1535 = x3d.HAnimSegment()
HAnimSegment1535.name = "r_ring_distal"
HAnimSegment1535.DEF = "hanim_r_ring_distal"
#<HAnimJoint name='r_ring3'/> visualization sphere is placed within <HAnimSegment name='r_ring_distal'/>
TouchSensor1536 = x3d.TouchSensor()
TouchSensor1536.description = "HAnimJoint r_ring3, HAnimSegment r_ring_distal"

HAnimSegment1535.children.append(TouchSensor1536)
Transform1537 = x3d.Transform()
Transform1537.translation = [-0.1983,0.7045,-0.0767]
Shape1538 = x3d.Shape()
Shape1538.USE = "HAnimJointShape"

Transform1537.children.append(Shape1538)

HAnimSegment1535.children.append(Transform1537)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_ring3'/> to <HAnimSite name='r_ring_distal_tip'/>
Shape1539 = x3d.Shape()
LineSet1540 = x3d.LineSet()
LineSet1540.vertexCount = [2]
Coordinate1541 = x3d.Coordinate()

LineSet1540.coord = Coordinate1541
ColorRGBA1542 = x3d.ColorRGBA()
ColorRGBA1542.USE = "HAnimSiteLineColorRGBA"

LineSet1540.color = ColorRGBA1542

Shape1539.geometry = LineSet1540

HAnimSegment1535.children.append(Shape1539)
HAnimSite1543 = x3d.HAnimSite()
HAnimSite1543.name = "r_ring_distal_tip"
HAnimSite1543.DEF = "hanim_r_ring_distal_tip"
HAnimSite1543.translation = [-0.1934,0.6778,-0.0693]
#HAnimSite visualization shape
TouchSensor1544 = x3d.TouchSensor()
TouchSensor1544.description = "HAnimSite r_ring_distal_tip"

HAnimSite1543.children.append(TouchSensor1544)
Shape1545 = x3d.Shape()
Shape1545.USE = "HAnimSiteShape"

HAnimSite1543.children.append(Shape1545)

HAnimSegment1535.children.append(HAnimSite1543)

HAnimJoint1534.children.append(HAnimSegment1535)

HAnimJoint1525.children.append(HAnimJoint1534)

HAnimJoint1516.children.append(HAnimJoint1525)

HAnimJoint1507.children.append(HAnimJoint1516)

HAnimJoint1334.children.append(HAnimJoint1507)
HAnimJoint1546 = x3d.HAnimJoint()
HAnimJoint1546.name = "r_pinky0"
HAnimJoint1546.DEF = "hanim_r_pinky0"
HAnimJoint1546.center = [-0.1925,0.8066,-0.1036]
HAnimJoint1546.ulimit = [0,0,0]
HAnimJoint1546.llimit = [0,0,0]
HAnimSegment1547 = x3d.HAnimSegment()
HAnimSegment1547.name = "r_pinky_metacarpal"
HAnimSegment1547.DEF = "hanim_r_pinky_metacarpal"
#<HAnimJoint name='r_pinky0'/> visualization sphere is placed within <HAnimSegment name='r_pinky_metacarpal'/>
TouchSensor1548 = x3d.TouchSensor()
TouchSensor1548.description = "HAnimJoint r_pinky0, HAnimSegment r_pinky_metacarpal"

HAnimSegment1547.children.append(TouchSensor1548)
Transform1549 = x3d.Transform()
Transform1549.translation = [-0.1925,0.8066,-0.1036]
Shape1550 = x3d.Shape()
Shape1550.USE = "HAnimJointShape"

Transform1549.children.append(Shape1550)

HAnimSegment1547.children.append(Transform1549)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_pinky0'/> to <HAnimJoint name='r_pinky1'/>
Shape1551 = x3d.Shape()
LineSet1552 = x3d.LineSet()
LineSet1552.vertexCount = [2]
Coordinate1553 = x3d.Coordinate()

LineSet1552.coord = Coordinate1553
ColorRGBA1554 = x3d.ColorRGBA()
ColorRGBA1554.USE = "HAnimSegmentLineColorRGBA"

LineSet1552.color = ColorRGBA1554

Shape1551.geometry = LineSet1552

HAnimSegment1547.children.append(Shape1551)

HAnimJoint1546.children.append(HAnimSegment1547)
HAnimJoint1555 = x3d.HAnimJoint()
HAnimJoint1555.name = "r_pinky1"
HAnimJoint1555.DEF = "hanim_r_pinky1"
HAnimJoint1555.center = [-0.1925,0.7866,-0.1036]
HAnimJoint1555.ulimit = [0,0,0]
HAnimJoint1555.llimit = [0,0,0]
HAnimSegment1556 = x3d.HAnimSegment()
HAnimSegment1556.name = "r_pinky_proximal"
HAnimSegment1556.DEF = "hanim_r_pinky_proximal"
#<HAnimJoint name='r_pinky1'/> visualization sphere is placed within <HAnimSegment name='r_pinky_proximal'/>
TouchSensor1557 = x3d.TouchSensor()
TouchSensor1557.description = "HAnimJoint r_pinky1, HAnimSegment r_pinky_proximal"

HAnimSegment1556.children.append(TouchSensor1557)
Transform1558 = x3d.Transform()
Transform1558.translation = [-0.1925,0.7866,-0.1036]
Shape1559 = x3d.Shape()
Shape1559.USE = "HAnimJointShape"

Transform1558.children.append(Shape1559)

HAnimSegment1556.children.append(Transform1558)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_pinky1'/> to <HAnimJoint name='r_pinky2'/>
Shape1560 = x3d.Shape()
LineSet1561 = x3d.LineSet()
LineSet1561.vertexCount = [2]
Coordinate1562 = x3d.Coordinate()

LineSet1561.coord = Coordinate1562
ColorRGBA1563 = x3d.ColorRGBA()
ColorRGBA1563.USE = "HAnimSegmentLineColorRGBA"

LineSet1561.color = ColorRGBA1563

Shape1560.geometry = LineSet1561

HAnimSegment1556.children.append(Shape1560)

HAnimJoint1555.children.append(HAnimSegment1556)
HAnimJoint1564 = x3d.HAnimJoint()
HAnimJoint1564.name = "r_pinky2"
HAnimJoint1564.DEF = "hanim_r_pinky2"
HAnimJoint1564.center = [-0.1938,0.7452,-0.1024]
HAnimJoint1564.ulimit = [0,0,0]
HAnimJoint1564.llimit = [0,0,0]
HAnimSegment1565 = x3d.HAnimSegment()
HAnimSegment1565.name = "r_pinky_middle"
HAnimSegment1565.DEF = "hanim_r_pinky_middle"
#<HAnimJoint name='r_pinky2'/> visualization sphere is placed within <HAnimSegment name='r_pinky_middle'/>
TouchSensor1566 = x3d.TouchSensor()
TouchSensor1566.description = "HAnimJoint r_pinky2, HAnimSegment r_pinky_middle"

HAnimSegment1565.children.append(TouchSensor1566)
Transform1567 = x3d.Transform()
Transform1567.translation = [-0.1938,0.7452,-0.1024]
Shape1568 = x3d.Shape()
Shape1568.USE = "HAnimJointShape"

Transform1567.children.append(Shape1568)

HAnimSegment1565.children.append(Transform1567)
#HAnimSegment visualization line segment from parent <HAnimJoint name='r_pinky2'/> to <HAnimJoint name='r_pinky3'/>
Shape1569 = x3d.Shape()
LineSet1570 = x3d.LineSet()
LineSet1570.vertexCount = [2]
Coordinate1571 = x3d.Coordinate()

LineSet1570.coord = Coordinate1571
ColorRGBA1572 = x3d.ColorRGBA()
ColorRGBA1572.USE = "HAnimSegmentLineColorRGBA"

LineSet1570.color = ColorRGBA1572

Shape1569.geometry = LineSet1570

HAnimSegment1565.children.append(Shape1569)

HAnimJoint1564.children.append(HAnimSegment1565)
HAnimJoint1573 = x3d.HAnimJoint()
HAnimJoint1573.name = "r_pinky3"
HAnimJoint1573.DEF = "hanim_r_pinky3"
HAnimJoint1573.center = [-0.1948,0.7277,-0.1017]
HAnimJoint1573.ulimit = [0,0,0]
HAnimJoint1573.llimit = [0,0,0]
HAnimSegment1574 = x3d.HAnimSegment()
HAnimSegment1574.name = "r_pinky_distal"
HAnimSegment1574.DEF = "hanim_r_pinky_distal"
#<HAnimJoint name='r_pinky3'/> visualization sphere is placed within <HAnimSegment name='r_pinky_distal'/>
TouchSensor1575 = x3d.TouchSensor()
TouchSensor1575.description = "HAnimJoint r_pinky3, HAnimSegment r_pinky_distal"

HAnimSegment1574.children.append(TouchSensor1575)
Transform1576 = x3d.Transform()
Transform1576.translation = [-0.1948,0.7277,-0.1017]
Shape1577 = x3d.Shape()
Shape1577.USE = "HAnimJointShape"

Transform1576.children.append(Shape1577)

HAnimSegment1574.children.append(Transform1576)
#HAnimSite visualization line segment from ancestor <HAnimJoint name='r_pinky3'/> to <HAnimSite name='r_pinky_distal_tip'/>
Shape1578 = x3d.Shape()
LineSet1579 = x3d.LineSet()
LineSet1579.vertexCount = [2]
Coordinate1580 = x3d.Coordinate()

LineSet1579.coord = Coordinate1580
ColorRGBA1581 = x3d.ColorRGBA()
ColorRGBA1581.USE = "HAnimSiteLineColorRGBA"

LineSet1579.color = ColorRGBA1581

Shape1578.geometry = LineSet1579

HAnimSegment1574.children.append(Shape1578)
HAnimSite1582 = x3d.HAnimSite()
HAnimSite1582.name = "r_pinky_distal_tip"
HAnimSite1582.DEF = "hanim_r_pinky_distal_tip"
HAnimSite1582.translation = [-0.1938,0.7035,-0.0949]
#HAnimSite visualization shape
TouchSensor1583 = x3d.TouchSensor()
TouchSensor1583.description = "HAnimSite r_pinky_distal_tip"

HAnimSite1582.children.append(TouchSensor1583)
Shape1584 = x3d.Shape()
Shape1584.USE = "HAnimSiteShape"

HAnimSite1582.children.append(Shape1584)

HAnimSegment1574.children.append(HAnimSite1582)

HAnimJoint1573.children.append(HAnimSegment1574)

HAnimJoint1564.children.append(HAnimJoint1573)

HAnimJoint1555.children.append(HAnimJoint1564)

HAnimJoint1546.children.append(HAnimJoint1555)

HAnimJoint1334.children.append(HAnimJoint1546)

HAnimJoint1297.children.append(HAnimJoint1334)

HAnimJoint1281.children.append(HAnimJoint1297)

HAnimJoint1272.children.append(HAnimJoint1281)

HAnimJoint1235.children.append(HAnimJoint1272)

HAnimJoint597.children.append(HAnimJoint1235)

HAnimJoint588.children.append(HAnimJoint597)

HAnimJoint579.children.append(HAnimJoint588)

HAnimJoint570.children.append(HAnimJoint579)

HAnimJoint561.children.append(HAnimJoint570)

HAnimJoint552.children.append(HAnimJoint561)

HAnimJoint543.children.append(HAnimJoint552)

HAnimJoint534.children.append(HAnimJoint543)

HAnimJoint511.children.append(HAnimJoint534)

HAnimJoint495.children.append(HAnimJoint511)

HAnimJoint486.children.append(HAnimJoint495)

HAnimJoint477.children.append(HAnimJoint486)

HAnimJoint468.children.append(HAnimJoint477)

HAnimJoint438.children.append(HAnimJoint468)

HAnimJoint429.children.append(HAnimJoint438)

HAnimJoint420.children.append(HAnimJoint429)

HAnimJoint397.children.append(HAnimJoint420)

HAnimJoint47.children.append(HAnimJoint397)

HAnimHumanoid46.skeleton.append(HAnimJoint47)
HAnimSite1585 = x3d.HAnimSite()
HAnimSite1585.name = "l_inclined_view"
HAnimSite1585.DEF = "hanim_l_inclined_view"
HAnimSite1585.rotation = [-0.113,0.993,0.0347,0.671]
HAnimSite1585.translation = [1.62,1.05,2.06]
#HAnimSite visualization shape
TouchSensor1586 = x3d.TouchSensor()
TouchSensor1586.description = "HAnimSite l_inclined_view"

HAnimSite1585.children.append(TouchSensor1586)
Shape1587 = x3d.Shape()
Shape1587.USE = "HAnimSiteShape"

HAnimSite1585.children.append(Shape1587)
Viewpoint1588 = x3d.Viewpoint()
Viewpoint1588.DEF = "hanim_l_inclined_viewpoint"
Viewpoint1588.description = "left inclined"
Viewpoint1588.position = [0,0,0]

HAnimSite1585.children.append(Viewpoint1588)
#HAnimSite/Viewpoint visualization shape
Anchor1589 = x3d.Anchor()
Anchor1589.description = "HAnimSite hanim_l_inclined_view Viewpoint"
Anchor1589.url = ["#hanim_l_inclined_viewpoint"]
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

HAnimSite1585.children.append(Anchor1589)

HAnimHumanoid46.viewpoints.append(HAnimSite1585)
HAnimSite1593 = x3d.HAnimSite()
HAnimSite1593.name = "r_inclined_view"
HAnimSite1593.DEF = "hanim_r_inclined_view"
HAnimSite1593.rotation = [-0.113,-0.993,0.0347,0.671]
HAnimSite1593.translation = [-1.62,1.05,2.06]
#HAnimSite visualization shape
TouchSensor1594 = x3d.TouchSensor()
TouchSensor1594.description = "HAnimSite r_inclined_view"

HAnimSite1593.children.append(TouchSensor1594)
Shape1595 = x3d.Shape()
Shape1595.USE = "HAnimSiteShape"

HAnimSite1593.children.append(Shape1595)
Viewpoint1596 = x3d.Viewpoint()
Viewpoint1596.DEF = "hanim_r_inclined_viewpoint"
Viewpoint1596.centerOfRotation = [0,0.9,0]
Viewpoint1596.description = "right inclined"
Viewpoint1596.position = [0,0,0]

HAnimSite1593.children.append(Viewpoint1596)
#HAnimSite/Viewpoint visualization shape
Anchor1597 = x3d.Anchor()
Anchor1597.description = "HAnimSite hanim_r_inclined_view Viewpoint"
Anchor1597.url = ["#hanim_r_inclined_viewpoint"]
LOD1598 = x3d.LOD()
LOD1598.forceTransitions = True
LOD1598.range = [0.04]
WorldInfo1599 = x3d.WorldInfo()
WorldInfo1599.info = ["hide diamond when close"]

LOD1598.children.append(WorldInfo1599)
Shape1600 = x3d.Shape()
Shape1600.USE = "HAnimSiteViewpointShape"

LOD1598.children.append(Shape1600)

Anchor1597.children.append(LOD1598)

HAnimSite1593.children.append(Anchor1597)

HAnimHumanoid46.viewpoints.append(HAnimSite1593)
HAnimSite1601 = x3d.HAnimSite()
HAnimSite1601.name = "front_view"
HAnimSite1601.DEF = "hanim_front_view"
HAnimSite1601.translation = [0,0.85,2.58]
#HAnimSite visualization shape
TouchSensor1602 = x3d.TouchSensor()
TouchSensor1602.description = "HAnimSite front_view"

HAnimSite1601.children.append(TouchSensor1602)
Shape1603 = x3d.Shape()
Shape1603.USE = "HAnimSiteShape"

HAnimSite1601.children.append(Shape1603)
Viewpoint1604 = x3d.Viewpoint()
Viewpoint1604.DEF = "hanim_front_viewpoint"
Viewpoint1604.centerOfRotation = [0,0.9,0]
Viewpoint1604.description = "front"
Viewpoint1604.position = [0,0,0]

HAnimSite1601.children.append(Viewpoint1604)
#HAnimSite/Viewpoint visualization shape
Anchor1605 = x3d.Anchor()
Anchor1605.description = "HAnimSite hanim_front_view Viewpoint"
Anchor1605.url = ["#hanim_front_viewpoint"]
LOD1606 = x3d.LOD()
LOD1606.forceTransitions = True
LOD1606.range = [0.04]
WorldInfo1607 = x3d.WorldInfo()
WorldInfo1607.info = ["hide diamond when close"]

LOD1606.children.append(WorldInfo1607)
Shape1608 = x3d.Shape()
Shape1608.USE = "HAnimSiteViewpointShape"

LOD1606.children.append(Shape1608)

Anchor1605.children.append(LOD1606)

HAnimSite1601.children.append(Anchor1605)

HAnimHumanoid46.viewpoints.append(HAnimSite1601)
HAnimSite1609 = x3d.HAnimSite()
HAnimSite1609.name = "back_view"
HAnimSite1609.DEF = "hanim_back_view"
HAnimSite1609.rotation = [0,1,0,3.14]
HAnimSite1609.translation = [0,0.85,-2.58]
#HAnimSite visualization shape
TouchSensor1610 = x3d.TouchSensor()
TouchSensor1610.description = "HAnimSite back_view"

HAnimSite1609.children.append(TouchSensor1610)
Shape1611 = x3d.Shape()
Shape1611.USE = "HAnimSiteShape"

HAnimSite1609.children.append(Shape1611)
Viewpoint1612 = x3d.Viewpoint()
Viewpoint1612.DEF = "hanim_back_viewpoint"
Viewpoint1612.centerOfRotation = [0,0.9,0]
Viewpoint1612.description = "back"
Viewpoint1612.position = [0,0,0]

HAnimSite1609.children.append(Viewpoint1612)
#HAnimSite/Viewpoint visualization shape
Anchor1613 = x3d.Anchor()
Anchor1613.description = "HAnimSite hanim_back_view Viewpoint"
Anchor1613.url = ["#hanim_back_viewpoint"]
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

HAnimSite1609.children.append(Anchor1613)

HAnimHumanoid46.viewpoints.append(HAnimSite1609)
HAnimSite1617 = x3d.HAnimSite()
HAnimSite1617.name = "l_side_view"
HAnimSite1617.DEF = "hanim_l_side_view"
HAnimSite1617.rotation = [0,1,0,1.5708]
HAnimSite1617.translation = [2.6,0.854,0]
#HAnimSite visualization shape
TouchSensor1618 = x3d.TouchSensor()
TouchSensor1618.description = "HAnimSite l_side_view"

HAnimSite1617.children.append(TouchSensor1618)
Shape1619 = x3d.Shape()
Shape1619.USE = "HAnimSiteShape"

HAnimSite1617.children.append(Shape1619)
Viewpoint1620 = x3d.Viewpoint()
Viewpoint1620.DEF = "hanim_l_side_viewpoint"
Viewpoint1620.centerOfRotation = [0,0.9,0]
Viewpoint1620.description = "left side"
Viewpoint1620.position = [0,0,0]

HAnimSite1617.children.append(Viewpoint1620)
#HAnimSite/Viewpoint visualization shape
Anchor1621 = x3d.Anchor()
Anchor1621.description = "HAnimSite hanim_l_side_view Viewpoint"
Anchor1621.url = ["#hanim_l_side_viewpoint"]
LOD1622 = x3d.LOD()
LOD1622.forceTransitions = True
LOD1622.range = [0.04]
WorldInfo1623 = x3d.WorldInfo()
WorldInfo1623.info = ["hide diamond when close"]

LOD1622.children.append(WorldInfo1623)
Shape1624 = x3d.Shape()
Shape1624.USE = "HAnimSiteViewpointShape"

LOD1622.children.append(Shape1624)

Anchor1621.children.append(LOD1622)

HAnimSite1617.children.append(Anchor1621)

HAnimHumanoid46.viewpoints.append(HAnimSite1617)
HAnimSite1625 = x3d.HAnimSite()
HAnimSite1625.name = "Top_view"
HAnimSite1625.DEF = "hanim_Top_view"
HAnimSite1625.rotation = [1,0,0,-1.57]
HAnimSite1625.translation = [0,3.5,0]
#HAnimSite visualization shape
TouchSensor1626 = x3d.TouchSensor()
TouchSensor1626.description = "HAnimSite Top_view"

HAnimSite1625.children.append(TouchSensor1626)
Shape1627 = x3d.Shape()
Shape1627.USE = "HAnimSiteShape"

HAnimSite1625.children.append(Shape1627)
Viewpoint1628 = x3d.Viewpoint()
Viewpoint1628.DEF = "hanim_Top_viewpoint"
Viewpoint1628.centerOfRotation = [0,0.9,0]
Viewpoint1628.description = "Top"
Viewpoint1628.position = [0,0,0]

HAnimSite1625.children.append(Viewpoint1628)
#HAnimSite/Viewpoint visualization shape
Anchor1629 = x3d.Anchor()
Anchor1629.description = "HAnimSite hanim_Top_view Viewpoint"
Anchor1629.url = ["#hanim_Top_viewpoint"]
LOD1630 = x3d.LOD()
LOD1630.forceTransitions = True
LOD1630.range = [0.04]
WorldInfo1631 = x3d.WorldInfo()
WorldInfo1631.info = ["hide diamond when close"]

LOD1630.children.append(WorldInfo1631)
Shape1632 = x3d.Shape()
Shape1632.USE = "HAnimSiteViewpointShape"

LOD1630.children.append(Shape1632)

Anchor1629.children.append(LOD1630)

HAnimSite1625.children.append(Anchor1629)

HAnimHumanoid46.viewpoints.append(HAnimSite1625)
HAnimSite1633 = x3d.HAnimSite()
HAnimSite1633.name = "front_close_view"
HAnimSite1633.DEF = "hanim_front_close_view"
HAnimSite1633.translation = [0,0.854,1.575]
#HAnimSite visualization shape
TouchSensor1634 = x3d.TouchSensor()
TouchSensor1634.description = "HAnimSite front_close_view"

HAnimSite1633.children.append(TouchSensor1634)
Shape1635 = x3d.Shape()
Shape1635.USE = "HAnimSiteShape"

HAnimSite1633.children.append(Shape1635)
Viewpoint1636 = x3d.Viewpoint()
Viewpoint1636.DEF = "hanim_front_close_viewpoint"
Viewpoint1636.centerOfRotation = [0,0,1.575]
Viewpoint1636.description = "front close"
Viewpoint1636.position = [0,0,0]

HAnimSite1633.children.append(Viewpoint1636)
#HAnimSite/Viewpoint visualization shape
Anchor1637 = x3d.Anchor()
Anchor1637.description = "HAnimSite hanim_front_close_view Viewpoint"
Anchor1637.url = ["#hanim_front_close_viewpoint"]
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

HAnimSite1633.children.append(Anchor1637)

HAnimHumanoid46.viewpoints.append(HAnimSite1633)
HAnimSite1641 = x3d.HAnimSite()
HAnimSite1641.name = "side_close_view"
HAnimSite1641.DEF = "hanim_side_close_view"
HAnimSite1641.rotation = [0,1,0,1.5708]
HAnimSite1641.translation = [1.56,0.854,0]
#HAnimSite visualization shape
TouchSensor1642 = x3d.TouchSensor()
TouchSensor1642.description = "HAnimSite side_close_view"

HAnimSite1641.children.append(TouchSensor1642)
Shape1643 = x3d.Shape()
Shape1643.USE = "HAnimSiteShape"

HAnimSite1641.children.append(Shape1643)
Viewpoint1644 = x3d.Viewpoint()
Viewpoint1644.DEF = "hanim_side_close_viewpoint"
Viewpoint1644.centerOfRotation = [1.6,0,0]
Viewpoint1644.description = "side close"
Viewpoint1644.position = [0,0,0]

HAnimSite1641.children.append(Viewpoint1644)
#HAnimSite/Viewpoint visualization shape
Anchor1645 = x3d.Anchor()
Anchor1645.description = "HAnimSite hanim_side_close_view Viewpoint"
Anchor1645.url = ["#hanim_side_close_viewpoint"]
LOD1646 = x3d.LOD()
LOD1646.forceTransitions = True
LOD1646.range = [0.04]
WorldInfo1647 = x3d.WorldInfo()
WorldInfo1647.info = ["hide diamond when close"]

LOD1646.children.append(WorldInfo1647)
Shape1648 = x3d.Shape()
Shape1648.USE = "HAnimSiteViewpointShape"

LOD1646.children.append(Shape1648)

Anchor1645.children.append(LOD1646)

HAnimSite1641.children.append(Anchor1645)

HAnimHumanoid46.viewpoints.append(HAnimSite1641)
HAnimSite1649 = x3d.HAnimSite()
HAnimSite1649.name = "head_front_close_view"
HAnimSite1649.DEF = "hanim_head_front_close_view"
HAnimSite1649.translation = [0,1.5,1]
#HAnimSite visualization shape
TouchSensor1650 = x3d.TouchSensor()
TouchSensor1650.description = "HAnimSite head_front_close_view"

HAnimSite1649.children.append(TouchSensor1650)
Shape1651 = x3d.Shape()
Shape1651.USE = "HAnimSiteShape"

HAnimSite1649.children.append(Shape1651)
Viewpoint1652 = x3d.Viewpoint()
Viewpoint1652.DEF = "hanim_head_front_close_viewpoint"
Viewpoint1652.centerOfRotation = [0,0,1]
Viewpoint1652.description = "head front close"
Viewpoint1652.position = [0,0,0]

HAnimSite1649.children.append(Viewpoint1652)
#HAnimSite/Viewpoint visualization shape
Anchor1653 = x3d.Anchor()
Anchor1653.description = "HAnimSite hanim_head_front_close_view Viewpoint"
Anchor1653.url = ["#hanim_head_front_close_viewpoint"]
LOD1654 = x3d.LOD()
LOD1654.forceTransitions = True
LOD1654.range = [0.04]
WorldInfo1655 = x3d.WorldInfo()
WorldInfo1655.info = ["hide diamond when close"]

LOD1654.children.append(WorldInfo1655)
Shape1656 = x3d.Shape()
Shape1656.USE = "HAnimSiteViewpointShape"

LOD1654.children.append(Shape1656)

Anchor1653.children.append(LOD1654)

HAnimSite1649.children.append(Anchor1653)

HAnimHumanoid46.viewpoints.append(HAnimSite1649)
HAnimSite1657 = x3d.HAnimSite()
HAnimSite1657.name = "chest_front_close_view"
HAnimSite1657.DEF = "hanim_chest_front_close_view"
HAnimSite1657.translation = [0,1.2,1]
#HAnimSite visualization shape
TouchSensor1658 = x3d.TouchSensor()
TouchSensor1658.description = "HAnimSite chest_front_close_view"

HAnimSite1657.children.append(TouchSensor1658)
Shape1659 = x3d.Shape()
Shape1659.USE = "HAnimSiteShape"

HAnimSite1657.children.append(Shape1659)
Viewpoint1660 = x3d.Viewpoint()
Viewpoint1660.DEF = "hanim_chest_front_close_viewpoint"
Viewpoint1660.centerOfRotation = [0,0,1]
Viewpoint1660.description = "chest front close"
Viewpoint1660.position = [0,0,0]

HAnimSite1657.children.append(Viewpoint1660)
#HAnimSite/Viewpoint visualization shape
Anchor1661 = x3d.Anchor()
Anchor1661.description = "HAnimSite hanim_chest_front_close_view Viewpoint"
Anchor1661.url = ["#hanim_chest_front_close_viewpoint"]
LOD1662 = x3d.LOD()
LOD1662.forceTransitions = True
LOD1662.range = [0.04]
WorldInfo1663 = x3d.WorldInfo()
WorldInfo1663.info = ["hide diamond when close"]

LOD1662.children.append(WorldInfo1663)
Shape1664 = x3d.Shape()
Shape1664.USE = "HAnimSiteViewpointShape"

LOD1662.children.append(Shape1664)

Anchor1661.children.append(LOD1662)

HAnimSite1657.children.append(Anchor1661)

HAnimHumanoid46.viewpoints.append(HAnimSite1657)
HAnimSite1665 = x3d.HAnimSite()
HAnimSite1665.name = "pelvis_front_close_view"
HAnimSite1665.DEF = "hanim_pelvis_front_close_view"
HAnimSite1665.translation = [0,0.8,1]
#HAnimSite visualization shape
TouchSensor1666 = x3d.TouchSensor()
TouchSensor1666.description = "HAnimSite pelvis_front_close_view"

HAnimSite1665.children.append(TouchSensor1666)
Shape1667 = x3d.Shape()
Shape1667.USE = "HAnimSiteShape"

HAnimSite1665.children.append(Shape1667)
Viewpoint1668 = x3d.Viewpoint()
Viewpoint1668.DEF = "hanim_pelvis_front_close_viewpoint"
Viewpoint1668.centerOfRotation = [0,0,1]
Viewpoint1668.description = "pelvis front close"
Viewpoint1668.position = [0,0,0]

HAnimSite1665.children.append(Viewpoint1668)
#HAnimSite/Viewpoint visualization shape
Anchor1669 = x3d.Anchor()
Anchor1669.description = "HAnimSite hanim_pelvis_front_close_view Viewpoint"
Anchor1669.url = ["#hanim_pelvis_front_close_viewpoint"]
LOD1670 = x3d.LOD()
LOD1670.forceTransitions = True
LOD1670.range = [0.04]
WorldInfo1671 = x3d.WorldInfo()
WorldInfo1671.info = ["hide diamond when close"]

LOD1670.children.append(WorldInfo1671)
Shape1672 = x3d.Shape()
Shape1672.USE = "HAnimSiteViewpointShape"

LOD1670.children.append(Shape1672)

Anchor1669.children.append(LOD1670)

HAnimSite1665.children.append(Anchor1669)

HAnimHumanoid46.viewpoints.append(HAnimSite1665)
HAnimSite1673 = x3d.HAnimSite()
HAnimSite1673.name = "knees_front_close_view"
HAnimSite1673.DEF = "hanim_knees_front_close_view"
HAnimSite1673.translation = [0,0.4,1]
#HAnimSite visualization shape
TouchSensor1674 = x3d.TouchSensor()
TouchSensor1674.description = "HAnimSite knees_front_close_view"

HAnimSite1673.children.append(TouchSensor1674)
Shape1675 = x3d.Shape()
Shape1675.USE = "HAnimSiteShape"

HAnimSite1673.children.append(Shape1675)
Viewpoint1676 = x3d.Viewpoint()
Viewpoint1676.DEF = "hanim_knees_front_close_viewpoint"
Viewpoint1676.centerOfRotation = [0,0.4,0]
Viewpoint1676.description = "knees front close"
Viewpoint1676.position = [0,0,0]

HAnimSite1673.children.append(Viewpoint1676)
#HAnimSite/Viewpoint visualization shape
Anchor1677 = x3d.Anchor()
Anchor1677.description = "HAnimSite hanim_knees_front_close_view Viewpoint"
Anchor1677.url = ["#hanim_knees_front_close_viewpoint"]
LOD1678 = x3d.LOD()
LOD1678.forceTransitions = True
LOD1678.range = [0.04]
WorldInfo1679 = x3d.WorldInfo()
WorldInfo1679.info = ["hide diamond when close"]

LOD1678.children.append(WorldInfo1679)
Shape1680 = x3d.Shape()
Shape1680.USE = "HAnimSiteViewpointShape"

LOD1678.children.append(Shape1680)

Anchor1677.children.append(LOD1678)

HAnimSite1673.children.append(Anchor1677)

HAnimHumanoid46.viewpoints.append(HAnimSite1673)
HAnimSite1681 = x3d.HAnimSite()
HAnimSite1681.name = "feet_front_close_view"
HAnimSite1681.DEF = "hanim_feet_front_close_view"
HAnimSite1681.translation = [0,0,1]
#HAnimSite visualization shape
TouchSensor1682 = x3d.TouchSensor()
TouchSensor1682.description = "HAnimSite feet_front_close_view"

HAnimSite1681.children.append(TouchSensor1682)
Shape1683 = x3d.Shape()
Shape1683.USE = "HAnimSiteShape"

HAnimSite1681.children.append(Shape1683)
Viewpoint1684 = x3d.Viewpoint()
Viewpoint1684.DEF = "hanim_feet_front_close_viewpoint"
Viewpoint1684.description = "feet front close"
Viewpoint1684.position = [0,0,0]

HAnimSite1681.children.append(Viewpoint1684)
#HAnimSite/Viewpoint visualization shape
Anchor1685 = x3d.Anchor()
Anchor1685.description = "HAnimSite hanim_feet_front_close_view Viewpoint"
Anchor1685.url = ["#hanim_feet_front_close_viewpoint"]
LOD1686 = x3d.LOD()
LOD1686.forceTransitions = True
LOD1686.range = [0.04]
WorldInfo1687 = x3d.WorldInfo()
WorldInfo1687.info = ["hide diamond when close"]

LOD1686.children.append(WorldInfo1687)
Shape1688 = x3d.Shape()
Shape1688.USE = "HAnimSiteViewpointShape"

LOD1686.children.append(Shape1688)

Anchor1685.children.append(LOD1686)

HAnimSite1681.children.append(Anchor1685)

HAnimHumanoid46.viewpoints.append(HAnimSite1681)
HAnimSite1689 = x3d.HAnimSite()
HAnimSite1689.name = "eye_level_view"
HAnimSite1689.DEF = "hanim_eye_level_view"
HAnimSite1689.translation = [0,1.6332,0.0502]
#HAnimSite visualization shape
TouchSensor1690 = x3d.TouchSensor()
TouchSensor1690.description = "HAnimSite eye_level_view"

HAnimSite1689.children.append(TouchSensor1690)
Shape1691 = x3d.Shape()
Shape1691.USE = "HAnimSiteShape"

HAnimSite1689.children.append(Shape1691)
Viewpoint1692 = x3d.Viewpoint()
Viewpoint1692.DEF = "hanim_eye_level_viewpoint"
Viewpoint1692.description = "eye level looking forward"
Viewpoint1692.orientation = [0,1,0,3.141593]
Viewpoint1692.position = [0,0,0]

HAnimSite1689.children.append(Viewpoint1692)
#HAnimSite/Viewpoint visualization shape
Anchor1693 = x3d.Anchor()
Anchor1693.description = "HAnimSite hanim_eye_level_view Viewpoint"
Anchor1693.url = ["#hanim_eye_level_viewpoint"]
LOD1694 = x3d.LOD()
LOD1694.forceTransitions = True
LOD1694.range = [0.04]
WorldInfo1695 = x3d.WorldInfo()
WorldInfo1695.info = ["hide diamond when close"]

LOD1694.children.append(WorldInfo1695)
Shape1696 = x3d.Shape()
Shape1696.USE = "HAnimSiteViewpointShape"

LOD1694.children.append(Shape1696)

Anchor1693.children.append(LOD1694)

HAnimSite1689.children.append(Anchor1693)

HAnimHumanoid46.viewpoints.append(HAnimSite1689)
HAnimSite1697 = x3d.HAnimSite()
HAnimSite1697.USE = "hanim_l_eyeball_site_view"

HAnimHumanoid46.sites.append(HAnimSite1697)
HAnimSite1698 = x3d.HAnimSite()
HAnimSite1698.USE = "hanim_r_eyeball_site_view"

HAnimHumanoid46.sites.append(HAnimSite1698)
HAnimSite1699 = x3d.HAnimSite()
HAnimSite1699.USE = "hanim_l_hand_front_view"

HAnimHumanoid46.sites.append(HAnimSite1699)
HAnimSite1700 = x3d.HAnimSite()
HAnimSite1700.USE = "hanim_r_hand_front_view"

HAnimHumanoid46.sites.append(HAnimSite1700)
HAnimJoint1701 = x3d.HAnimJoint()
HAnimJoint1701.USE = "hanim_humanoid_root"

HAnimHumanoid46.joints.append(HAnimJoint1701)
HAnimJoint1702 = x3d.HAnimJoint()
HAnimJoint1702.USE = "hanim_sacroiliac"

HAnimHumanoid46.joints.append(HAnimJoint1702)
HAnimJoint1703 = x3d.HAnimJoint()
HAnimJoint1703.USE = "hanim_vl5"

HAnimHumanoid46.joints.append(HAnimJoint1703)
HAnimJoint1704 = x3d.HAnimJoint()
HAnimJoint1704.USE = "hanim_vl4"

HAnimHumanoid46.joints.append(HAnimJoint1704)
HAnimJoint1705 = x3d.HAnimJoint()
HAnimJoint1705.USE = "hanim_vl3"

HAnimHumanoid46.joints.append(HAnimJoint1705)
HAnimJoint1706 = x3d.HAnimJoint()
HAnimJoint1706.USE = "hanim_vl2"

HAnimHumanoid46.joints.append(HAnimJoint1706)
HAnimJoint1707 = x3d.HAnimJoint()
HAnimJoint1707.USE = "hanim_vl1"

HAnimHumanoid46.joints.append(HAnimJoint1707)
HAnimJoint1708 = x3d.HAnimJoint()
HAnimJoint1708.USE = "hanim_vt12"

HAnimHumanoid46.joints.append(HAnimJoint1708)
HAnimJoint1709 = x3d.HAnimJoint()
HAnimJoint1709.USE = "hanim_vt11"

HAnimHumanoid46.joints.append(HAnimJoint1709)
HAnimJoint1710 = x3d.HAnimJoint()
HAnimJoint1710.USE = "hanim_vt10"

HAnimHumanoid46.joints.append(HAnimJoint1710)
HAnimJoint1711 = x3d.HAnimJoint()
HAnimJoint1711.USE = "hanim_vt9"

HAnimHumanoid46.joints.append(HAnimJoint1711)
HAnimJoint1712 = x3d.HAnimJoint()
HAnimJoint1712.USE = "hanim_vt8"

HAnimHumanoid46.joints.append(HAnimJoint1712)
HAnimJoint1713 = x3d.HAnimJoint()
HAnimJoint1713.USE = "hanim_vt7"

HAnimHumanoid46.joints.append(HAnimJoint1713)
HAnimJoint1714 = x3d.HAnimJoint()
HAnimJoint1714.USE = "hanim_vt6"

HAnimHumanoid46.joints.append(HAnimJoint1714)
HAnimJoint1715 = x3d.HAnimJoint()
HAnimJoint1715.USE = "hanim_vt5"

HAnimHumanoid46.joints.append(HAnimJoint1715)
HAnimJoint1716 = x3d.HAnimJoint()
HAnimJoint1716.USE = "hanim_vt4"

HAnimHumanoid46.joints.append(HAnimJoint1716)
HAnimJoint1717 = x3d.HAnimJoint()
HAnimJoint1717.USE = "hanim_vt3"

HAnimHumanoid46.joints.append(HAnimJoint1717)
HAnimJoint1718 = x3d.HAnimJoint()
HAnimJoint1718.USE = "hanim_vt2"

HAnimHumanoid46.joints.append(HAnimJoint1718)
HAnimJoint1719 = x3d.HAnimJoint()
HAnimJoint1719.USE = "hanim_vt1"

HAnimHumanoid46.joints.append(HAnimJoint1719)
HAnimJoint1720 = x3d.HAnimJoint()
HAnimJoint1720.USE = "hanim_vc7"

HAnimHumanoid46.joints.append(HAnimJoint1720)
HAnimJoint1721 = x3d.HAnimJoint()
HAnimJoint1721.USE = "hanim_vc6"

HAnimHumanoid46.joints.append(HAnimJoint1721)
HAnimJoint1722 = x3d.HAnimJoint()
HAnimJoint1722.USE = "hanim_vc5"

HAnimHumanoid46.joints.append(HAnimJoint1722)
HAnimJoint1723 = x3d.HAnimJoint()
HAnimJoint1723.USE = "hanim_vc4"

HAnimHumanoid46.joints.append(HAnimJoint1723)
HAnimJoint1724 = x3d.HAnimJoint()
HAnimJoint1724.USE = "hanim_vc3"

HAnimHumanoid46.joints.append(HAnimJoint1724)
HAnimJoint1725 = x3d.HAnimJoint()
HAnimJoint1725.USE = "hanim_vc2"

HAnimHumanoid46.joints.append(HAnimJoint1725)
HAnimJoint1726 = x3d.HAnimJoint()
HAnimJoint1726.USE = "hanim_vc1"

HAnimHumanoid46.joints.append(HAnimJoint1726)
HAnimJoint1727 = x3d.HAnimJoint()
HAnimJoint1727.USE = "hanim_skullbase"

HAnimHumanoid46.joints.append(HAnimJoint1727)
HAnimJoint1728 = x3d.HAnimJoint()
HAnimJoint1728.USE = "hanim_temporomandibular"

HAnimHumanoid46.joints.append(HAnimJoint1728)
HAnimJoint1729 = x3d.HAnimJoint()
HAnimJoint1729.USE = "hanim_l_acromioclavicular"

HAnimHumanoid46.joints.append(HAnimJoint1729)
HAnimJoint1730 = x3d.HAnimJoint()
HAnimJoint1730.USE = "hanim_r_acromioclavicular"

HAnimHumanoid46.joints.append(HAnimJoint1730)
HAnimJoint1731 = x3d.HAnimJoint()
HAnimJoint1731.USE = "hanim_l_ankle"

HAnimHumanoid46.joints.append(HAnimJoint1731)
HAnimJoint1732 = x3d.HAnimJoint()
HAnimJoint1732.USE = "hanim_r_ankle"

HAnimHumanoid46.joints.append(HAnimJoint1732)
HAnimJoint1733 = x3d.HAnimJoint()
HAnimJoint1733.USE = "hanim_l_elbow"

HAnimHumanoid46.joints.append(HAnimJoint1733)
HAnimJoint1734 = x3d.HAnimJoint()
HAnimJoint1734.USE = "hanim_r_elbow"

HAnimHumanoid46.joints.append(HAnimJoint1734)
HAnimJoint1735 = x3d.HAnimJoint()
HAnimJoint1735.USE = "hanim_l_eyeball_joint"

HAnimHumanoid46.joints.append(HAnimJoint1735)
HAnimJoint1736 = x3d.HAnimJoint()
HAnimJoint1736.USE = "hanim_r_eyeball_joint"

HAnimHumanoid46.joints.append(HAnimJoint1736)
HAnimJoint1737 = x3d.HAnimJoint()
HAnimJoint1737.USE = "hanim_l_eyebrow_joint"

HAnimHumanoid46.joints.append(HAnimJoint1737)
HAnimJoint1738 = x3d.HAnimJoint()
HAnimJoint1738.USE = "hanim_r_eyebrow_joint"

HAnimHumanoid46.joints.append(HAnimJoint1738)
HAnimJoint1739 = x3d.HAnimJoint()
HAnimJoint1739.USE = "hanim_l_eyelid_joint"

HAnimHumanoid46.joints.append(HAnimJoint1739)
HAnimJoint1740 = x3d.HAnimJoint()
HAnimJoint1740.USE = "hanim_r_eyelid_joint"

HAnimHumanoid46.joints.append(HAnimJoint1740)
HAnimJoint1741 = x3d.HAnimJoint()
HAnimJoint1741.USE = "hanim_l_hip"

HAnimHumanoid46.joints.append(HAnimJoint1741)
HAnimJoint1742 = x3d.HAnimJoint()
HAnimJoint1742.USE = "hanim_r_hip"

HAnimHumanoid46.joints.append(HAnimJoint1742)
HAnimJoint1743 = x3d.HAnimJoint()
HAnimJoint1743.USE = "hanim_l_index0"

HAnimHumanoid46.joints.append(HAnimJoint1743)
HAnimJoint1744 = x3d.HAnimJoint()
HAnimJoint1744.USE = "hanim_r_index0"

HAnimHumanoid46.joints.append(HAnimJoint1744)
HAnimJoint1745 = x3d.HAnimJoint()
HAnimJoint1745.USE = "hanim_l_index1"

HAnimHumanoid46.joints.append(HAnimJoint1745)
HAnimJoint1746 = x3d.HAnimJoint()
HAnimJoint1746.USE = "hanim_r_index1"

HAnimHumanoid46.joints.append(HAnimJoint1746)
HAnimJoint1747 = x3d.HAnimJoint()
HAnimJoint1747.USE = "hanim_l_index2"

HAnimHumanoid46.joints.append(HAnimJoint1747)
HAnimJoint1748 = x3d.HAnimJoint()
HAnimJoint1748.USE = "hanim_r_index2"

HAnimHumanoid46.joints.append(HAnimJoint1748)
HAnimJoint1749 = x3d.HAnimJoint()
HAnimJoint1749.USE = "hanim_l_index3"

HAnimHumanoid46.joints.append(HAnimJoint1749)
HAnimJoint1750 = x3d.HAnimJoint()
HAnimJoint1750.USE = "hanim_r_index3"

HAnimHumanoid46.joints.append(HAnimJoint1750)
HAnimJoint1751 = x3d.HAnimJoint()
HAnimJoint1751.USE = "hanim_l_knee"

HAnimHumanoid46.joints.append(HAnimJoint1751)
HAnimJoint1752 = x3d.HAnimJoint()
HAnimJoint1752.USE = "hanim_r_knee"

HAnimHumanoid46.joints.append(HAnimJoint1752)
HAnimJoint1753 = x3d.HAnimJoint()
HAnimJoint1753.USE = "hanim_l_metatarsal"

HAnimHumanoid46.joints.append(HAnimJoint1753)
HAnimJoint1754 = x3d.HAnimJoint()
HAnimJoint1754.USE = "hanim_r_metatarsal"

HAnimHumanoid46.joints.append(HAnimJoint1754)
HAnimJoint1755 = x3d.HAnimJoint()
HAnimJoint1755.USE = "hanim_l_middle0"

HAnimHumanoid46.joints.append(HAnimJoint1755)
HAnimJoint1756 = x3d.HAnimJoint()
HAnimJoint1756.USE = "hanim_r_middle0"

HAnimHumanoid46.joints.append(HAnimJoint1756)
HAnimJoint1757 = x3d.HAnimJoint()
HAnimJoint1757.USE = "hanim_l_middle1"

HAnimHumanoid46.joints.append(HAnimJoint1757)
HAnimJoint1758 = x3d.HAnimJoint()
HAnimJoint1758.USE = "hanim_r_middle1"

HAnimHumanoid46.joints.append(HAnimJoint1758)
HAnimJoint1759 = x3d.HAnimJoint()
HAnimJoint1759.USE = "hanim_l_middle2"

HAnimHumanoid46.joints.append(HAnimJoint1759)
HAnimJoint1760 = x3d.HAnimJoint()
HAnimJoint1760.USE = "hanim_r_middle2"

HAnimHumanoid46.joints.append(HAnimJoint1760)
HAnimJoint1761 = x3d.HAnimJoint()
HAnimJoint1761.USE = "hanim_l_middle3"

HAnimHumanoid46.joints.append(HAnimJoint1761)
HAnimJoint1762 = x3d.HAnimJoint()
HAnimJoint1762.USE = "hanim_r_middle3"

HAnimHumanoid46.joints.append(HAnimJoint1762)
HAnimJoint1763 = x3d.HAnimJoint()
HAnimJoint1763.USE = "hanim_l_midtarsal"

HAnimHumanoid46.joints.append(HAnimJoint1763)
HAnimJoint1764 = x3d.HAnimJoint()
HAnimJoint1764.USE = "hanim_r_midtarsal"

HAnimHumanoid46.joints.append(HAnimJoint1764)
HAnimJoint1765 = x3d.HAnimJoint()
HAnimJoint1765.USE = "hanim_l_pinky0"

HAnimHumanoid46.joints.append(HAnimJoint1765)
HAnimJoint1766 = x3d.HAnimJoint()
HAnimJoint1766.USE = "hanim_r_pinky0"

HAnimHumanoid46.joints.append(HAnimJoint1766)
HAnimJoint1767 = x3d.HAnimJoint()
HAnimJoint1767.USE = "hanim_l_pinky1"

HAnimHumanoid46.joints.append(HAnimJoint1767)
HAnimJoint1768 = x3d.HAnimJoint()
HAnimJoint1768.USE = "hanim_r_pinky1"

HAnimHumanoid46.joints.append(HAnimJoint1768)
HAnimJoint1769 = x3d.HAnimJoint()
HAnimJoint1769.USE = "hanim_l_pinky2"

HAnimHumanoid46.joints.append(HAnimJoint1769)
HAnimJoint1770 = x3d.HAnimJoint()
HAnimJoint1770.USE = "hanim_r_pinky2"

HAnimHumanoid46.joints.append(HAnimJoint1770)
HAnimJoint1771 = x3d.HAnimJoint()
HAnimJoint1771.USE = "hanim_l_pinky3"

HAnimHumanoid46.joints.append(HAnimJoint1771)
HAnimJoint1772 = x3d.HAnimJoint()
HAnimJoint1772.USE = "hanim_r_pinky3"

HAnimHumanoid46.joints.append(HAnimJoint1772)
HAnimJoint1773 = x3d.HAnimJoint()
HAnimJoint1773.USE = "hanim_l_ring0"

HAnimHumanoid46.joints.append(HAnimJoint1773)
HAnimJoint1774 = x3d.HAnimJoint()
HAnimJoint1774.USE = "hanim_r_ring0"

HAnimHumanoid46.joints.append(HAnimJoint1774)
HAnimJoint1775 = x3d.HAnimJoint()
HAnimJoint1775.USE = "hanim_l_ring1"

HAnimHumanoid46.joints.append(HAnimJoint1775)
HAnimJoint1776 = x3d.HAnimJoint()
HAnimJoint1776.USE = "hanim_r_ring1"

HAnimHumanoid46.joints.append(HAnimJoint1776)
HAnimJoint1777 = x3d.HAnimJoint()
HAnimJoint1777.USE = "hanim_l_ring2"

HAnimHumanoid46.joints.append(HAnimJoint1777)
HAnimJoint1778 = x3d.HAnimJoint()
HAnimJoint1778.USE = "hanim_r_ring2"

HAnimHumanoid46.joints.append(HAnimJoint1778)
HAnimJoint1779 = x3d.HAnimJoint()
HAnimJoint1779.USE = "hanim_l_ring3"

HAnimHumanoid46.joints.append(HAnimJoint1779)
HAnimJoint1780 = x3d.HAnimJoint()
HAnimJoint1780.USE = "hanim_r_ring3"

HAnimHumanoid46.joints.append(HAnimJoint1780)
HAnimJoint1781 = x3d.HAnimJoint()
HAnimJoint1781.USE = "hanim_l_shoulder"

HAnimHumanoid46.joints.append(HAnimJoint1781)
HAnimJoint1782 = x3d.HAnimJoint()
HAnimJoint1782.USE = "hanim_r_shoulder"

HAnimHumanoid46.joints.append(HAnimJoint1782)
HAnimJoint1783 = x3d.HAnimJoint()
HAnimJoint1783.USE = "hanim_l_sternoclavicular"

HAnimHumanoid46.joints.append(HAnimJoint1783)
HAnimJoint1784 = x3d.HAnimJoint()
HAnimJoint1784.USE = "hanim_r_sternoclavicular"

HAnimHumanoid46.joints.append(HAnimJoint1784)
HAnimJoint1785 = x3d.HAnimJoint()
HAnimJoint1785.USE = "hanim_l_subtalar"

HAnimHumanoid46.joints.append(HAnimJoint1785)
HAnimJoint1786 = x3d.HAnimJoint()
HAnimJoint1786.USE = "hanim_r_subtalar"

HAnimHumanoid46.joints.append(HAnimJoint1786)
HAnimJoint1787 = x3d.HAnimJoint()
HAnimJoint1787.USE = "hanim_l_thumb1"

HAnimHumanoid46.joints.append(HAnimJoint1787)
HAnimJoint1788 = x3d.HAnimJoint()
HAnimJoint1788.USE = "hanim_r_thumb1"

HAnimHumanoid46.joints.append(HAnimJoint1788)
HAnimJoint1789 = x3d.HAnimJoint()
HAnimJoint1789.USE = "hanim_l_thumb2"

HAnimHumanoid46.joints.append(HAnimJoint1789)
HAnimJoint1790 = x3d.HAnimJoint()
HAnimJoint1790.USE = "hanim_r_thumb2"

HAnimHumanoid46.joints.append(HAnimJoint1790)
HAnimJoint1791 = x3d.HAnimJoint()
HAnimJoint1791.USE = "hanim_l_thumb3"

HAnimHumanoid46.joints.append(HAnimJoint1791)
HAnimJoint1792 = x3d.HAnimJoint()
HAnimJoint1792.USE = "hanim_r_thumb3"

HAnimHumanoid46.joints.append(HAnimJoint1792)
HAnimJoint1793 = x3d.HAnimJoint()
HAnimJoint1793.USE = "hanim_l_wrist"

HAnimHumanoid46.joints.append(HAnimJoint1793)
HAnimJoint1794 = x3d.HAnimJoint()
HAnimJoint1794.USE = "hanim_r_wrist"

HAnimHumanoid46.joints.append(HAnimJoint1794)
HAnimSegment1795 = x3d.HAnimSegment()
HAnimSegment1795.USE = "hanim_pelvis"

HAnimHumanoid46.segments.append(HAnimSegment1795)
HAnimSegment1796 = x3d.HAnimSegment()
HAnimSegment1796.USE = "hanim_skull"

HAnimHumanoid46.segments.append(HAnimSegment1796)
HAnimSegment1797 = x3d.HAnimSegment()
HAnimSegment1797.USE = "hanim_jaw"

HAnimHumanoid46.segments.append(HAnimSegment1797)
HAnimSegment1798 = x3d.HAnimSegment()
HAnimSegment1798.USE = "hanim_c1"

HAnimHumanoid46.segments.append(HAnimSegment1798)
HAnimSegment1799 = x3d.HAnimSegment()
HAnimSegment1799.USE = "hanim_c2"

HAnimHumanoid46.segments.append(HAnimSegment1799)
HAnimSegment1800 = x3d.HAnimSegment()
HAnimSegment1800.USE = "hanim_c3"

HAnimHumanoid46.segments.append(HAnimSegment1800)
HAnimSegment1801 = x3d.HAnimSegment()
HAnimSegment1801.USE = "hanim_c4"

HAnimHumanoid46.segments.append(HAnimSegment1801)
HAnimSegment1802 = x3d.HAnimSegment()
HAnimSegment1802.USE = "hanim_c5"

HAnimHumanoid46.segments.append(HAnimSegment1802)
HAnimSegment1803 = x3d.HAnimSegment()
HAnimSegment1803.USE = "hanim_c6"

HAnimHumanoid46.segments.append(HAnimSegment1803)
HAnimSegment1804 = x3d.HAnimSegment()
HAnimSegment1804.USE = "hanim_c7"

HAnimHumanoid46.segments.append(HAnimSegment1804)
HAnimSegment1805 = x3d.HAnimSegment()
HAnimSegment1805.USE = "hanim_t1"

HAnimHumanoid46.segments.append(HAnimSegment1805)
HAnimSegment1806 = x3d.HAnimSegment()
HAnimSegment1806.USE = "hanim_t2"

HAnimHumanoid46.segments.append(HAnimSegment1806)
HAnimSegment1807 = x3d.HAnimSegment()
HAnimSegment1807.USE = "hanim_t3"

HAnimHumanoid46.segments.append(HAnimSegment1807)
HAnimSegment1808 = x3d.HAnimSegment()
HAnimSegment1808.USE = "hanim_t4"

HAnimHumanoid46.segments.append(HAnimSegment1808)
HAnimSegment1809 = x3d.HAnimSegment()
HAnimSegment1809.USE = "hanim_t5"

HAnimHumanoid46.segments.append(HAnimSegment1809)
HAnimSegment1810 = x3d.HAnimSegment()
HAnimSegment1810.USE = "hanim_t6"

HAnimHumanoid46.segments.append(HAnimSegment1810)
HAnimSegment1811 = x3d.HAnimSegment()
HAnimSegment1811.USE = "hanim_t7"

HAnimHumanoid46.segments.append(HAnimSegment1811)
HAnimSegment1812 = x3d.HAnimSegment()
HAnimSegment1812.USE = "hanim_t8"

HAnimHumanoid46.segments.append(HAnimSegment1812)
HAnimSegment1813 = x3d.HAnimSegment()
HAnimSegment1813.USE = "hanim_t9"

HAnimHumanoid46.segments.append(HAnimSegment1813)
HAnimSegment1814 = x3d.HAnimSegment()
HAnimSegment1814.USE = "hanim_t10"

HAnimHumanoid46.segments.append(HAnimSegment1814)
HAnimSegment1815 = x3d.HAnimSegment()
HAnimSegment1815.USE = "hanim_t11"

HAnimHumanoid46.segments.append(HAnimSegment1815)
HAnimSegment1816 = x3d.HAnimSegment()
HAnimSegment1816.USE = "hanim_t12"

HAnimHumanoid46.segments.append(HAnimSegment1816)
HAnimSegment1817 = x3d.HAnimSegment()
HAnimSegment1817.USE = "hanim_l1"

HAnimHumanoid46.segments.append(HAnimSegment1817)
HAnimSegment1818 = x3d.HAnimSegment()
HAnimSegment1818.USE = "hanim_l2"

HAnimHumanoid46.segments.append(HAnimSegment1818)
HAnimSegment1819 = x3d.HAnimSegment()
HAnimSegment1819.USE = "hanim_l3"

HAnimHumanoid46.segments.append(HAnimSegment1819)
HAnimSegment1820 = x3d.HAnimSegment()
HAnimSegment1820.USE = "hanim_l4"

HAnimHumanoid46.segments.append(HAnimSegment1820)
HAnimSegment1821 = x3d.HAnimSegment()
HAnimSegment1821.USE = "hanim_l5"

HAnimHumanoid46.segments.append(HAnimSegment1821)
HAnimSegment1822 = x3d.HAnimSegment()
HAnimSegment1822.USE = "hanim_sacrum"

HAnimHumanoid46.segments.append(HAnimSegment1822)
HAnimSegment1823 = x3d.HAnimSegment()
HAnimSegment1823.USE = "hanim_l_calf"

HAnimHumanoid46.segments.append(HAnimSegment1823)
HAnimSegment1824 = x3d.HAnimSegment()
HAnimSegment1824.USE = "hanim_r_calf"

HAnimHumanoid46.segments.append(HAnimSegment1824)
HAnimSegment1825 = x3d.HAnimSegment()
HAnimSegment1825.USE = "hanim_l_clavicle"

HAnimHumanoid46.segments.append(HAnimSegment1825)
HAnimSegment1826 = x3d.HAnimSegment()
HAnimSegment1826.USE = "hanim_r_clavicle"

HAnimHumanoid46.segments.append(HAnimSegment1826)
HAnimSegment1827 = x3d.HAnimSegment()
HAnimSegment1827.USE = "hanim_l_eyeball"

HAnimHumanoid46.segments.append(HAnimSegment1827)
HAnimSegment1828 = x3d.HAnimSegment()
HAnimSegment1828.USE = "hanim_r_eyeball"

HAnimHumanoid46.segments.append(HAnimSegment1828)
HAnimSegment1829 = x3d.HAnimSegment()
HAnimSegment1829.USE = "hanim_l_eyebrow"

HAnimHumanoid46.segments.append(HAnimSegment1829)
HAnimSegment1830 = x3d.HAnimSegment()
HAnimSegment1830.USE = "hanim_r_eyebrow"

HAnimHumanoid46.segments.append(HAnimSegment1830)
HAnimSegment1831 = x3d.HAnimSegment()
HAnimSegment1831.USE = "hanim_l_eyelid"

HAnimHumanoid46.segments.append(HAnimSegment1831)
HAnimSegment1832 = x3d.HAnimSegment()
HAnimSegment1832.USE = "hanim_r_eyelid"

HAnimHumanoid46.segments.append(HAnimSegment1832)
HAnimSegment1833 = x3d.HAnimSegment()
HAnimSegment1833.USE = "hanim_l_forearm"

HAnimHumanoid46.segments.append(HAnimSegment1833)
HAnimSegment1834 = x3d.HAnimSegment()
HAnimSegment1834.USE = "hanim_r_forearm"

HAnimHumanoid46.segments.append(HAnimSegment1834)
HAnimSegment1835 = x3d.HAnimSegment()
HAnimSegment1835.USE = "hanim_l_forefoot"

HAnimHumanoid46.segments.append(HAnimSegment1835)
HAnimSegment1836 = x3d.HAnimSegment()
HAnimSegment1836.USE = "hanim_r_forefoot"

HAnimHumanoid46.segments.append(HAnimSegment1836)
HAnimSegment1837 = x3d.HAnimSegment()
HAnimSegment1837.USE = "hanim_l_hand"

HAnimHumanoid46.segments.append(HAnimSegment1837)
HAnimSegment1838 = x3d.HAnimSegment()
HAnimSegment1838.USE = "hanim_r_hand"

HAnimHumanoid46.segments.append(HAnimSegment1838)
HAnimSegment1839 = x3d.HAnimSegment()
HAnimSegment1839.USE = "hanim_l_hindfoot"

HAnimHumanoid46.segments.append(HAnimSegment1839)
HAnimSegment1840 = x3d.HAnimSegment()
HAnimSegment1840.USE = "hanim_r_hindfoot"

HAnimHumanoid46.segments.append(HAnimSegment1840)
HAnimSegment1841 = x3d.HAnimSegment()
HAnimSegment1841.USE = "hanim_l_index_distal"

HAnimHumanoid46.segments.append(HAnimSegment1841)
HAnimSegment1842 = x3d.HAnimSegment()
HAnimSegment1842.USE = "hanim_r_index_distal"

HAnimHumanoid46.segments.append(HAnimSegment1842)
HAnimSegment1843 = x3d.HAnimSegment()
HAnimSegment1843.USE = "hanim_l_index_metacarpal"

HAnimHumanoid46.segments.append(HAnimSegment1843)
HAnimSegment1844 = x3d.HAnimSegment()
HAnimSegment1844.USE = "hanim_r_index_metacarpal"

HAnimHumanoid46.segments.append(HAnimSegment1844)
HAnimSegment1845 = x3d.HAnimSegment()
HAnimSegment1845.USE = "hanim_l_index_middle"

HAnimHumanoid46.segments.append(HAnimSegment1845)
HAnimSegment1846 = x3d.HAnimSegment()
HAnimSegment1846.USE = "hanim_r_index_middle"

HAnimHumanoid46.segments.append(HAnimSegment1846)
HAnimSegment1847 = x3d.HAnimSegment()
HAnimSegment1847.USE = "hanim_l_index_proximal"

HAnimHumanoid46.segments.append(HAnimSegment1847)
HAnimSegment1848 = x3d.HAnimSegment()
HAnimSegment1848.USE = "hanim_r_index_proximal"

HAnimHumanoid46.segments.append(HAnimSegment1848)
HAnimSegment1849 = x3d.HAnimSegment()
HAnimSegment1849.USE = "hanim_l_middistal"

HAnimHumanoid46.segments.append(HAnimSegment1849)
HAnimSegment1850 = x3d.HAnimSegment()
HAnimSegment1850.USE = "hanim_r_middistal"

HAnimHumanoid46.segments.append(HAnimSegment1850)
HAnimSegment1851 = x3d.HAnimSegment()
HAnimSegment1851.USE = "hanim_l_middle_distal"

HAnimHumanoid46.segments.append(HAnimSegment1851)
HAnimSegment1852 = x3d.HAnimSegment()
HAnimSegment1852.USE = "hanim_r_middle_distal"

HAnimHumanoid46.segments.append(HAnimSegment1852)
HAnimSegment1853 = x3d.HAnimSegment()
HAnimSegment1853.USE = "hanim_l_middle_metacarpal"

HAnimHumanoid46.segments.append(HAnimSegment1853)
HAnimSegment1854 = x3d.HAnimSegment()
HAnimSegment1854.USE = "hanim_r_middle_metacarpal"

HAnimHumanoid46.segments.append(HAnimSegment1854)
HAnimSegment1855 = x3d.HAnimSegment()
HAnimSegment1855.USE = "hanim_l_middle_middle"

HAnimHumanoid46.segments.append(HAnimSegment1855)
HAnimSegment1856 = x3d.HAnimSegment()
HAnimSegment1856.USE = "hanim_r_middle_middle"

HAnimHumanoid46.segments.append(HAnimSegment1856)
HAnimSegment1857 = x3d.HAnimSegment()
HAnimSegment1857.USE = "hanim_l_middle_proximal"

HAnimHumanoid46.segments.append(HAnimSegment1857)
HAnimSegment1858 = x3d.HAnimSegment()
HAnimSegment1858.USE = "hanim_r_middle_proximal"

HAnimHumanoid46.segments.append(HAnimSegment1858)
HAnimSegment1859 = x3d.HAnimSegment()
HAnimSegment1859.USE = "hanim_l_midproximal"

HAnimHumanoid46.segments.append(HAnimSegment1859)
HAnimSegment1860 = x3d.HAnimSegment()
HAnimSegment1860.USE = "hanim_r_midproximal"

HAnimHumanoid46.segments.append(HAnimSegment1860)
HAnimSegment1861 = x3d.HAnimSegment()
HAnimSegment1861.USE = "hanim_l_pinky_distal"

HAnimHumanoid46.segments.append(HAnimSegment1861)
HAnimSegment1862 = x3d.HAnimSegment()
HAnimSegment1862.USE = "hanim_r_pinky_distal"

HAnimHumanoid46.segments.append(HAnimSegment1862)
HAnimSegment1863 = x3d.HAnimSegment()
HAnimSegment1863.USE = "hanim_l_pinky_metacarpal"

HAnimHumanoid46.segments.append(HAnimSegment1863)
HAnimSegment1864 = x3d.HAnimSegment()
HAnimSegment1864.USE = "hanim_r_pinky_metacarpal"

HAnimHumanoid46.segments.append(HAnimSegment1864)
HAnimSegment1865 = x3d.HAnimSegment()
HAnimSegment1865.USE = "hanim_l_pinky_middle"

HAnimHumanoid46.segments.append(HAnimSegment1865)
HAnimSegment1866 = x3d.HAnimSegment()
HAnimSegment1866.USE = "hanim_r_pinky_middle"

HAnimHumanoid46.segments.append(HAnimSegment1866)
HAnimSegment1867 = x3d.HAnimSegment()
HAnimSegment1867.USE = "hanim_l_pinky_proximal"

HAnimHumanoid46.segments.append(HAnimSegment1867)
HAnimSegment1868 = x3d.HAnimSegment()
HAnimSegment1868.USE = "hanim_r_pinky_proximal"

HAnimHumanoid46.segments.append(HAnimSegment1868)
HAnimSegment1869 = x3d.HAnimSegment()
HAnimSegment1869.USE = "hanim_l_ring_distal"

HAnimHumanoid46.segments.append(HAnimSegment1869)
HAnimSegment1870 = x3d.HAnimSegment()
HAnimSegment1870.USE = "hanim_r_ring_distal"

HAnimHumanoid46.segments.append(HAnimSegment1870)
HAnimSegment1871 = x3d.HAnimSegment()
HAnimSegment1871.USE = "hanim_l_ring_metacarpal"

HAnimHumanoid46.segments.append(HAnimSegment1871)
HAnimSegment1872 = x3d.HAnimSegment()
HAnimSegment1872.USE = "hanim_r_ring_metacarpal"

HAnimHumanoid46.segments.append(HAnimSegment1872)
HAnimSegment1873 = x3d.HAnimSegment()
HAnimSegment1873.USE = "hanim_l_ring_middle"

HAnimHumanoid46.segments.append(HAnimSegment1873)
HAnimSegment1874 = x3d.HAnimSegment()
HAnimSegment1874.USE = "hanim_r_ring_middle"

HAnimHumanoid46.segments.append(HAnimSegment1874)
HAnimSegment1875 = x3d.HAnimSegment()
HAnimSegment1875.USE = "hanim_l_ring_proximal"

HAnimHumanoid46.segments.append(HAnimSegment1875)
HAnimSegment1876 = x3d.HAnimSegment()
HAnimSegment1876.USE = "hanim_r_ring_proximal"

HAnimHumanoid46.segments.append(HAnimSegment1876)
HAnimSegment1877 = x3d.HAnimSegment()
HAnimSegment1877.USE = "hanim_l_scapula"

HAnimHumanoid46.segments.append(HAnimSegment1877)
HAnimSegment1878 = x3d.HAnimSegment()
HAnimSegment1878.USE = "hanim_r_scapula"

HAnimHumanoid46.segments.append(HAnimSegment1878)
HAnimSegment1879 = x3d.HAnimSegment()
HAnimSegment1879.USE = "hanim_l_thigh"

HAnimHumanoid46.segments.append(HAnimSegment1879)
HAnimSegment1880 = x3d.HAnimSegment()
HAnimSegment1880.USE = "hanim_r_thigh"

HAnimHumanoid46.segments.append(HAnimSegment1880)
HAnimSegment1881 = x3d.HAnimSegment()
HAnimSegment1881.USE = "hanim_l_thumb_distal"

HAnimHumanoid46.segments.append(HAnimSegment1881)
HAnimSegment1882 = x3d.HAnimSegment()
HAnimSegment1882.USE = "hanim_r_thumb_distal"

HAnimHumanoid46.segments.append(HAnimSegment1882)
HAnimSegment1883 = x3d.HAnimSegment()
HAnimSegment1883.USE = "hanim_l_thumb_metacarpal"

HAnimHumanoid46.segments.append(HAnimSegment1883)
HAnimSegment1884 = x3d.HAnimSegment()
HAnimSegment1884.USE = "hanim_r_thumb_metacarpal"

HAnimHumanoid46.segments.append(HAnimSegment1884)
HAnimSegment1885 = x3d.HAnimSegment()
HAnimSegment1885.USE = "hanim_l_thumb_proximal"

HAnimHumanoid46.segments.append(HAnimSegment1885)
HAnimSegment1886 = x3d.HAnimSegment()
HAnimSegment1886.USE = "hanim_r_thumb_proximal"

HAnimHumanoid46.segments.append(HAnimSegment1886)
HAnimSegment1887 = x3d.HAnimSegment()
HAnimSegment1887.USE = "hanim_l_upperarm"

HAnimHumanoid46.segments.append(HAnimSegment1887)
HAnimSegment1888 = x3d.HAnimSegment()
HAnimSegment1888.USE = "hanim_r_upperarm"

HAnimHumanoid46.segments.append(HAnimSegment1888)
HAnimSite1889 = x3d.HAnimSite()
HAnimSite1889.USE = "hanim_crotch_pt"

HAnimHumanoid46.sites.append(HAnimSite1889)
HAnimSite1890 = x3d.HAnimSite()
HAnimSite1890.USE = "hanim_skull_tip"

HAnimHumanoid46.sites.append(HAnimSite1890)
HAnimSite1891 = x3d.HAnimSite()
HAnimSite1891.USE = "hanim_sellion_pt"

HAnimHumanoid46.sites.append(HAnimSite1891)
HAnimSite1892 = x3d.HAnimSite()
HAnimSite1892.USE = "hanim_supramenton_pt"

HAnimHumanoid46.sites.append(HAnimSite1892)
HAnimSite1893 = x3d.HAnimSite()
HAnimSite1893.USE = "hanim_nuchale_pt"

HAnimHumanoid46.sites.append(HAnimSite1893)
HAnimSite1894 = x3d.HAnimSite()
HAnimSite1894.USE = "hanim_suprasternale_pt"

HAnimHumanoid46.sites.append(HAnimSite1894)
HAnimSite1895 = x3d.HAnimSite()
HAnimSite1895.USE = "hanim_cervicale_pt"

HAnimHumanoid46.sites.append(HAnimSite1895)
HAnimSite1896 = x3d.HAnimSite()
HAnimSite1896.USE = "hanim_substernale_pt"

HAnimHumanoid46.sites.append(HAnimSite1896)
HAnimSite1897 = x3d.HAnimSite()
HAnimSite1897.USE = "hanim_rib10_midspine_pt"

HAnimHumanoid46.sites.append(HAnimSite1897)
HAnimSite1898 = x3d.HAnimSite()
HAnimSite1898.USE = "hanim_waist_preferred_post_pt"

HAnimHumanoid46.sites.append(HAnimSite1898)
HAnimSite1899 = x3d.HAnimSite()
HAnimSite1899.USE = "hanim_navel_pt"

HAnimHumanoid46.sites.append(HAnimSite1899)
HAnimSite1900 = x3d.HAnimSite()
HAnimSite1900.USE = "hanim_l_acromion_pt"

HAnimHumanoid46.sites.append(HAnimSite1900)
HAnimSite1901 = x3d.HAnimSite()
HAnimSite1901.USE = "hanim_r_acromion_pt"

HAnimHumanoid46.sites.append(HAnimSite1901)
HAnimSite1902 = x3d.HAnimSite()
HAnimSite1902.USE = "hanim_r_asis_pt"

HAnimHumanoid46.sites.append(HAnimSite1902)
HAnimSite1903 = x3d.HAnimSite()
HAnimSite1903.USE = "hanim_l_asis_pt"

HAnimHumanoid46.sites.append(HAnimSite1903)
HAnimSite1904 = x3d.HAnimSite()
HAnimSite1904.USE = "hanim_l_axilla_ant_pt"

HAnimHumanoid46.sites.append(HAnimSite1904)
HAnimSite1905 = x3d.HAnimSite()
HAnimSite1905.USE = "hanim_r_axilla_ant_pt"

HAnimHumanoid46.sites.append(HAnimSite1905)
HAnimSite1906 = x3d.HAnimSite()
HAnimSite1906.USE = "hanim_l_axilla_post_pt"

HAnimHumanoid46.sites.append(HAnimSite1906)
HAnimSite1907 = x3d.HAnimSite()
HAnimSite1907.USE = "hanim_r_axilla_post_pt"

HAnimHumanoid46.sites.append(HAnimSite1907)
HAnimSite1908 = x3d.HAnimSite()
HAnimSite1908.USE = "hanim_l_calcaneous_post_pt"

HAnimHumanoid46.sites.append(HAnimSite1908)
HAnimSite1909 = x3d.HAnimSite()
HAnimSite1909.USE = "hanim_r_calcaneous_post_pt"

HAnimHumanoid46.sites.append(HAnimSite1909)
HAnimSite1910 = x3d.HAnimSite()
HAnimSite1910.USE = "hanim_l_clavicale_pt"

HAnimHumanoid46.sites.append(HAnimSite1910)
HAnimSite1911 = x3d.HAnimSite()
HAnimSite1911.USE = "hanim_r_clavicale_pt"

HAnimHumanoid46.sites.append(HAnimSite1911)
HAnimSite1912 = x3d.HAnimSite()
HAnimSite1912.USE = "hanim_l_dactylion_pt"

HAnimHumanoid46.sites.append(HAnimSite1912)
HAnimSite1913 = x3d.HAnimSite()
HAnimSite1913.USE = "hanim_r_dactylion_pt"

HAnimHumanoid46.sites.append(HAnimSite1913)
HAnimSite1914 = x3d.HAnimSite()
HAnimSite1914.USE = "hanim_l_digit2_pt"

HAnimHumanoid46.sites.append(HAnimSite1914)
HAnimSite1915 = x3d.HAnimSite()
HAnimSite1915.USE = "hanim_r_digit2_pt"

HAnimHumanoid46.sites.append(HAnimSite1915)
HAnimSite1916 = x3d.HAnimSite()
HAnimSite1916.USE = "hanim_l_femoral_lateral_epicn_pt"

HAnimHumanoid46.sites.append(HAnimSite1916)
HAnimSite1917 = x3d.HAnimSite()
HAnimSite1917.USE = "hanim_r_femoral_lateral_epicn_pt"

HAnimHumanoid46.sites.append(HAnimSite1917)
HAnimSite1918 = x3d.HAnimSite()
HAnimSite1918.USE = "hanim_l_femoral_medial_epicn_pt"

HAnimHumanoid46.sites.append(HAnimSite1918)
HAnimSite1919 = x3d.HAnimSite()
HAnimSite1919.USE = "hanim_r_femoral_medial_epicn_pt"

HAnimHumanoid46.sites.append(HAnimSite1919)
HAnimSite1920 = x3d.HAnimSite()
HAnimSite1920.USE = "hanim_l_forefoot_tip"

HAnimHumanoid46.sites.append(HAnimSite1920)
HAnimSite1921 = x3d.HAnimSite()
HAnimSite1921.USE = "hanim_r_forefoot_tip"

HAnimHumanoid46.sites.append(HAnimSite1921)
HAnimSite1922 = x3d.HAnimSite()
HAnimSite1922.USE = "hanim_r_gonion_pt"

HAnimHumanoid46.sites.append(HAnimSite1922)
HAnimSite1923 = x3d.HAnimSite()
HAnimSite1923.USE = "hanim_l_gonion_pt"

HAnimHumanoid46.sites.append(HAnimSite1923)
HAnimSite1924 = x3d.HAnimSite()
HAnimSite1924.USE = "hanim_l_humeral_lateral_epicn_pt"

HAnimHumanoid46.sites.append(HAnimSite1924)
HAnimSite1925 = x3d.HAnimSite()
HAnimSite1925.USE = "hanim_r_humeral_lateral_epicn_pt"

HAnimHumanoid46.sites.append(HAnimSite1925)
HAnimSite1926 = x3d.HAnimSite()
HAnimSite1926.USE = "hanim_l_humeral_medial_epicn_pt"

HAnimHumanoid46.sites.append(HAnimSite1926)
HAnimSite1927 = x3d.HAnimSite()
HAnimSite1927.USE = "hanim_r_humeral_medial_epicn_pt"

HAnimHumanoid46.sites.append(HAnimSite1927)
HAnimSite1928 = x3d.HAnimSite()
HAnimSite1928.USE = "hanim_r_iliocristale_pt"

HAnimHumanoid46.sites.append(HAnimSite1928)
HAnimSite1929 = x3d.HAnimSite()
HAnimSite1929.USE = "hanim_l_iliocristale_pt"

HAnimHumanoid46.sites.append(HAnimSite1929)
HAnimSite1930 = x3d.HAnimSite()
HAnimSite1930.USE = "hanim_l_index_distal_tip"

HAnimHumanoid46.sites.append(HAnimSite1930)
HAnimSite1931 = x3d.HAnimSite()
HAnimSite1931.USE = "hanim_r_index_distal_tip"

HAnimHumanoid46.sites.append(HAnimSite1931)
HAnimSite1932 = x3d.HAnimSite()
HAnimSite1932.USE = "hanim_r_infraorbitale_pt"

HAnimHumanoid46.sites.append(HAnimSite1932)
HAnimSite1933 = x3d.HAnimSite()
HAnimSite1933.USE = "hanim_l_infraorbitale_pt"

HAnimHumanoid46.sites.append(HAnimSite1933)
HAnimSite1934 = x3d.HAnimSite()
HAnimSite1934.USE = "hanim_l_knee_crease_pt"

HAnimHumanoid46.sites.append(HAnimSite1934)
HAnimSite1935 = x3d.HAnimSite()
HAnimSite1935.USE = "hanim_r_knee_crease_pt"

HAnimHumanoid46.sites.append(HAnimSite1935)
HAnimSite1936 = x3d.HAnimSite()
HAnimSite1936.USE = "hanim_l_lateral_malleolus_pt"

HAnimHumanoid46.sites.append(HAnimSite1936)
HAnimSite1937 = x3d.HAnimSite()
HAnimSite1937.USE = "hanim_r_lateral_malleolus_pt"

HAnimHumanoid46.sites.append(HAnimSite1937)
HAnimSite1938 = x3d.HAnimSite()
HAnimSite1938.USE = "hanim_l_medial_malleolus_pt"

HAnimHumanoid46.sites.append(HAnimSite1938)
HAnimSite1939 = x3d.HAnimSite()
HAnimSite1939.USE = "hanim_r_medial_malleolus_pt"

HAnimHumanoid46.sites.append(HAnimSite1939)
HAnimSite1940 = x3d.HAnimSite()
HAnimSite1940.USE = "hanim_l_metacarpal_pha2_pt"

HAnimHumanoid46.sites.append(HAnimSite1940)
HAnimSite1941 = x3d.HAnimSite()
HAnimSite1941.USE = "hanim_r_metacarpal_pha2_pt"

HAnimHumanoid46.sites.append(HAnimSite1941)
HAnimSite1942 = x3d.HAnimSite()
HAnimSite1942.USE = "hanim_l_metacarpal_pha5_pt"

HAnimHumanoid46.sites.append(HAnimSite1942)
HAnimSite1943 = x3d.HAnimSite()
HAnimSite1943.USE = "hanim_r_metacarpal_pha5_pt"

HAnimHumanoid46.sites.append(HAnimSite1943)
HAnimSite1944 = x3d.HAnimSite()
HAnimSite1944.USE = "hanim_l_metatarsal_pha1_pt"

HAnimHumanoid46.sites.append(HAnimSite1944)
HAnimSite1945 = x3d.HAnimSite()
HAnimSite1945.USE = "hanim_r_metatarsal_pha1_pt"

HAnimHumanoid46.sites.append(HAnimSite1945)
HAnimSite1946 = x3d.HAnimSite()
HAnimSite1946.USE = "hanim_l_metatarsal_pha5_pt"

HAnimHumanoid46.sites.append(HAnimSite1946)
HAnimSite1947 = x3d.HAnimSite()
HAnimSite1947.USE = "hanim_r_metatarsal_pha5_pt"

HAnimHumanoid46.sites.append(HAnimSite1947)
HAnimSite1948 = x3d.HAnimSite()
HAnimSite1948.USE = "hanim_l_middle_distal_tip"

HAnimHumanoid46.sites.append(HAnimSite1948)
HAnimSite1949 = x3d.HAnimSite()
HAnimSite1949.USE = "hanim_r_middle_distal_tip"

HAnimHumanoid46.sites.append(HAnimSite1949)
HAnimSite1950 = x3d.HAnimSite()
HAnimSite1950.USE = "hanim_r_neck_base_pt"

HAnimHumanoid46.sites.append(HAnimSite1950)
HAnimSite1951 = x3d.HAnimSite()
HAnimSite1951.USE = "hanim_l_neck_base_pt"

HAnimHumanoid46.sites.append(HAnimSite1951)
HAnimSite1952 = x3d.HAnimSite()
HAnimSite1952.USE = "hanim_l_olecranon_pt"

HAnimHumanoid46.sites.append(HAnimSite1952)
HAnimSite1953 = x3d.HAnimSite()
HAnimSite1953.USE = "hanim_r_olecranon_pt"

HAnimHumanoid46.sites.append(HAnimSite1953)
HAnimSite1954 = x3d.HAnimSite()
HAnimSite1954.USE = "hanim_l_pinky_distal_tip"

HAnimHumanoid46.sites.append(HAnimSite1954)
HAnimSite1955 = x3d.HAnimSite()
HAnimSite1955.USE = "hanim_r_pinky_distal_tip"

HAnimHumanoid46.sites.append(HAnimSite1955)
HAnimSite1956 = x3d.HAnimSite()
HAnimSite1956.USE = "hanim_r_psis_pt"

HAnimHumanoid46.sites.append(HAnimSite1956)
HAnimSite1957 = x3d.HAnimSite()
HAnimSite1957.USE = "hanim_l_psis_pt"

HAnimHumanoid46.sites.append(HAnimSite1957)
HAnimSite1958 = x3d.HAnimSite()
HAnimSite1958.USE = "hanim_l_radial_styloid_pt"

HAnimHumanoid46.sites.append(HAnimSite1958)
HAnimSite1959 = x3d.HAnimSite()
HAnimSite1959.USE = "hanim_r_radial_styloid_pt"

HAnimHumanoid46.sites.append(HAnimSite1959)
HAnimSite1960 = x3d.HAnimSite()
HAnimSite1960.USE = "hanim_l_radiale_pt"

HAnimHumanoid46.sites.append(HAnimSite1960)
HAnimSite1961 = x3d.HAnimSite()
HAnimSite1961.USE = "hanim_r_radiale_pt"

HAnimHumanoid46.sites.append(HAnimSite1961)
HAnimSite1962 = x3d.HAnimSite()
HAnimSite1962.USE = "hanim_r_rib10_pt"

HAnimHumanoid46.sites.append(HAnimSite1962)
HAnimSite1963 = x3d.HAnimSite()
HAnimSite1963.USE = "hanim_l_rib10_pt"

HAnimHumanoid46.sites.append(HAnimSite1963)
HAnimSite1964 = x3d.HAnimSite()
HAnimSite1964.USE = "hanim_l_ring_distal_tip"

HAnimHumanoid46.sites.append(HAnimSite1964)
HAnimSite1965 = x3d.HAnimSite()
HAnimSite1965.USE = "hanim_r_ring_distal_tip"

HAnimHumanoid46.sites.append(HAnimSite1965)
HAnimSite1966 = x3d.HAnimSite()
HAnimSite1966.USE = "hanim_temporomandibular_l_site_pt"

HAnimHumanoid46.sites.append(HAnimSite1966)
HAnimSite1967 = x3d.HAnimSite()
HAnimSite1967.USE = "hanim_temporomandibular_r_site_pt"

HAnimHumanoid46.sites.append(HAnimSite1967)
HAnimSite1968 = x3d.HAnimSite()
HAnimSite1968.USE = "hanim_l_sphyrion_pt"

HAnimHumanoid46.sites.append(HAnimSite1968)
HAnimSite1969 = x3d.HAnimSite()
HAnimSite1969.USE = "hanim_r_sphyrion_pt"

HAnimHumanoid46.sites.append(HAnimSite1969)
HAnimSite1970 = x3d.HAnimSite()
HAnimSite1970.USE = "hanim_r_thelion_pt"

HAnimHumanoid46.sites.append(HAnimSite1970)
HAnimSite1971 = x3d.HAnimSite()
HAnimSite1971.USE = "hanim_l_thelion_pt"

HAnimHumanoid46.sites.append(HAnimSite1971)
HAnimSite1972 = x3d.HAnimSite()
HAnimSite1972.USE = "hanim_l_thumb_distal_tip"

HAnimHumanoid46.sites.append(HAnimSite1972)
HAnimSite1973 = x3d.HAnimSite()
HAnimSite1973.USE = "hanim_r_thumb_distal_tip"

HAnimHumanoid46.sites.append(HAnimSite1973)
HAnimSite1974 = x3d.HAnimSite()
HAnimSite1974.USE = "hanim_r_tragion_pt"

HAnimHumanoid46.sites.append(HAnimSite1974)
HAnimSite1975 = x3d.HAnimSite()
HAnimSite1975.USE = "hanim_l_tragion_pt"

HAnimHumanoid46.sites.append(HAnimSite1975)
HAnimSite1976 = x3d.HAnimSite()
HAnimSite1976.USE = "hanim_r_trochanterion_pt"

HAnimHumanoid46.sites.append(HAnimSite1976)
HAnimSite1977 = x3d.HAnimSite()
HAnimSite1977.USE = "hanim_l_trochanterion_pt"

HAnimHumanoid46.sites.append(HAnimSite1977)
HAnimSite1978 = x3d.HAnimSite()
HAnimSite1978.USE = "hanim_l_ulnar_styloid_pt"

HAnimHumanoid46.sites.append(HAnimSite1978)
HAnimSite1979 = x3d.HAnimSite()
HAnimSite1979.USE = "hanim_r_ulnar_styloid_pt"

HAnimHumanoid46.sites.append(HAnimSite1979)

Scene32.children.append(HAnimHumanoid46)

X3D0.Scene = Scene32
f = open("././HAnim1SpecificationLOA3Illustrated_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
